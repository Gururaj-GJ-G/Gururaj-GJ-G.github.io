#!/usr/bin/env python3
"""
Build the reader pages for case studies and publications.

Reads index/case-studies.json, converts each registered markdown file into a
styled HTML page under cases/, and prints the word count and read time for each.

Usage:
    python scripts/build_cases.py

No third-party dependencies. Run it after editing any markdown file, and commit
the generated pages along with the source.
"""

import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "index", "case-studies.json")
OUT_DIR = os.path.join(ROOT, "cases")
WORDS_PER_MINUTE = 220


# ---------------------------------------------------------------- markdown

def escape(text):
    return html.escape(text, quote=False)


def inline(text):
    """Escape, then apply inline markdown. Code spans are protected first."""
    text = escape(text)
    spans = []

    def stash(match):
        spans.append("<code>" + match.group(1) + "</code>")
        return "\x00%d\x00" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)
    return text


def split_row(line):
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def md_to_html(text):
    lines = text.split("\n")
    out, i = [], 0
    list_kind = None
    code_buf = None

    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append("</%s>" % list_kind)
            list_kind = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if code_buf is None:
                close_list()
                code_buf = []
            else:
                out.append("<pre><code>%s</code></pre>" % escape("\n".join(code_buf)))
                code_buf = None
            i += 1
            continue
        if code_buf is not None:
            code_buf.append(line)
            i += 1
            continue

        if not stripped:
            close_list()
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < len(lines) and \
                re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            close_list()
            head = split_row(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            out.append("<table><thead><tr>%s</tr></thead><tbody>" %
                       "".join("<th>%s</th>" % inline(c) for c in head))
            for row in rows:
                out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in row))
            out.append("</tbody></table>")
            continue

        # horizontal rule (also the front-matter terminator when it survives)
        if re.match(r"^-{3,}$", stripped) or re.match(r"^\*{3,}$", stripped):
            close_list()
            out.append("<hr>")
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            close_list()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            close_list()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf)))
            continue

        # lists
        mu = re.match(r"^\s*[-*]\s+(.*)$", line)
        mo = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if mu or mo:
            kind = "ul" if mu else "ol"
            if list_kind != kind:
                close_list()
                out.append("<%s>" % kind)
                list_kind = kind
            item = [(mu or mo).group(1)]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                s2 = nxt.strip()
                if (not s2 or re.match(r"^\s*[-*]\s+", nxt) or re.match(r"^\s*\d+\.\s+", nxt)
                        or s2.startswith("#") or s2.startswith("|") or s2.startswith(">")
                        or s2.startswith("```") or re.match(r"^-{3,}$", s2)):
                    break
                item.append(s2)
                i += 1
            out.append("<li>%s</li>" % inline(" ".join(item)))
            continue

        # paragraph
        close_list()
        buf = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith("#") or nxt.startswith("|") or nxt.startswith(">")
                    or nxt.startswith("```") or re.match(r"^-{3,}$", nxt)
                    or re.match(r"^\s*[-*]\s+", lines[i]) or re.match(r"^\s*\d+\.\s+", lines[i])):
                break
            buf.append(nxt)
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))

    close_list()
    if code_buf is not None:
        out.append("<pre><code>%s</code></pre>" % escape("\n".join(code_buf)))
    return "\n".join(out)


MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def human_date(value):
    """2026-04-01 -> April 2026; 2026-04-13 -> 13 April 2026."""
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", str(value))
    if not m:
        return str(value)
    year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not 1 <= month <= 12:
        return str(value)
    if day == 1:
        return "%s %d" % (MONTHS[month - 1], year)
    return "%d %s %d" % (day, MONTHS[month - 1], year)


def strip_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            return text[end + 4:]
    return text


# ---------------------------------------------------------------- page shell

PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Gururaj G J</title>
<meta name="description" content="{summary}">
<meta name="author" content="Gururaj G J">
<meta name="theme-color" content="#05080f">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{summary}">
<meta property="og:type" content="article">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23070b14'/%3E%3Ctext x='32' y='43' font-family='Arial' font-size='30' font-weight='bold' fill='%2338bdf8' text-anchor='middle'%3EGJ%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
</head>
<body class="article-page">

<nav class="nav scrolled">
  <div class="container nav-inner">
    <a href="../index.html" class="brand">
      <span class="brand-mark">GJ</span>
      <span class="brand-text">Gururaj <em>G J</em></span>
    </a>
    <div class="nav-actions">
      <a class="btn btn-ghost btn-sm" href="../index.html#cases">&larr; Case studies &amp; publications</a>
    </div>
  </div>
</nav>

<main class="container article-shell">
  <article class="article">
    <div class="article-meta">
      <span class="article-kind">{kind}</span>
      <span>{date}</span>
      <span>{read} min read</span>
    </div>
{body}
  </article>
</main>

<footer>
  <div class="container footer-inner">
    <div class="footer-brand">Gururaj <em>G J</em></div>
    <p class="footer-line">Fraud Investigation &middot; Transaction Laundering &middot; Merchant Risk &middot; AML/CFT &middot; Trust &amp; Safety</p>
    <div class="footer-links">
      <a href="https://github.com/Gururaj-GJ-G" target="_blank" rel="noopener">GitHub</a>
      <a href="https://www.linkedin.com/in/gururaj-gj-52a062b4" target="_blank" rel="noopener">LinkedIn</a>
      <a href="mailto:gururaj.gj.guru@gmail.com">Email</a>
    </div>
    <p class="footer-copy">&copy; 2026 Gururaj G J &middot; Bengaluru, India</p>
  </div>
</footer>

</body>
</html>
"""


def main():
    if not os.path.exists(REGISTRY):
        print("registry not found: index/case-studies.json")
        return 1
    with open(REGISTRY, encoding="utf-8") as fh:
        registry = json.load(fh)

    os.makedirs(OUT_DIR, exist_ok=True)
    built = 0

    for entry in registry.get("entries", []):
        if entry.get("status") != "published":
            continue
        src = entry.get("url", "")
        if not src.endswith(".md"):
            continue
        src_path = os.path.join(ROOT, src)
        if not os.path.exists(src_path):
            print("MISSING %s" % src)
            continue

        with open(src_path, encoding="utf-8") as fh:
            raw = fh.read()
        body_md = strip_front_matter(raw)
        body_html = md_to_html(body_md)

        words = len(re.findall(r"\b[\w'-]+\b", body_md))
        read = max(1, round(words / WORDS_PER_MINUTE))

        out_name = os.path.splitext(os.path.basename(src))[0] + ".html"
        out_path = os.path.join(OUT_DIR, out_name)

        kind = "Case study" if entry.get("type") == "case-study" else "Publication"
        page = PAGE.format(
            title=html.escape(entry.get("title", "")),
            summary=html.escape(entry.get("summary", ""), quote=True),
            kind=kind,
            date=human_date(entry.get("date", "")),
            read=read,
            body=body_html,
        )
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(page)

        entry["page"] = "cases/" + out_name
        entry["read_minutes"] = read
        entry["words"] = words
        built += 1
        print("%-14s %5d words  %2d min  -> %s" % (entry.get("id"), words, read, entry["page"]))

    with open(REGISTRY, "w", encoding="utf-8") as fh:
        json.dump(registry, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print("\n%d page(s) built" % built)
    return 0


if __name__ == "__main__":
    sys.exit(main())
