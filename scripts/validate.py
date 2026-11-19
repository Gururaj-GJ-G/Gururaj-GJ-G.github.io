#!/usr/bin/env python3
"""
Validate a case study or publication before it is published.

Checks front matter, required sections, length, the disclaimer, and a set of
safety patterns (contact details, national identifiers, payment-card numbers).

Usage:
    python scripts/validate.py path/to/CS-2026-001-slug.md
    python scripts/validate.py --all          # every file under case-studies/ and publications/
    python scripts/validate.py --registry     # registry entries point at real files

Exit code 0 = pass, 1 = fail. No third-party dependencies.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_KEYS = ["id", "title", "type", "status", "date", "author", "category",
                 "evidence", "summary", "portfolio_card"]
ALLOWED = {
    "type": {"case-study", "publication"},
    "status": {"draft", "review", "published", "withdrawn"},
    "evidence": {"synthetic", "redacted-real", "public-sources"},
    "category": {"marketplace", "payments", "merchant-risk", "aml", "ato", "forensics",
                 "methodology", "trust-and-safety", "ai-governance", "other"},
}
CASE_SECTIONS = ["## 1. Summary", "## 2. Context", "## 4. Method", "## 5. Evidence",
                 "## 6. Findings", "## 7. Indicators and red flags", "## 9. Limitations"]
PUB_SECTIONS = ["## Abstract", "## 1. The problem", "## 3. The proposed approach",
                "## 5. Trade-offs and failure modes", "## 7. Conclusion"]

# Safety patterns. Each is (label, regex, hint).
SAFETY = [
    ("email address", r"[\w.+-]+@[\w-]+\.[\w.]{2,}",
     "replace with a role label, e.g. 'the seller'"),
    ("phone number", r"(?:\+?91[\s-]?)?\b[6-9]\d{4}[\s-]?\d{5}\b",
     "remove or mask"),
    ("Aadhaar-style 12-digit number", r"\b\d{4}\s\d{4}\s\d{4}\b",
     "never publish national identifiers"),
    ("PAN", r"\b[A-Z]{5}\d{4}[A-Z]\b",
     "never publish national identifiers"),
    ("payment-card number", r"\b(?:\d[ -]?){13,19}\b",
     "use a masked form such as 4xxx-xxxx-xxxx-1234"),
    ("UPI handle", r"\b[\w.\-]{2,}@(?:okaxis|okhdfcbank|oksbi|okicici|paytm|ybl|apl|upi|axl)\b",
     "remove or replace with 'a UPI handle'"),
    ("IPv4 address", r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
     "redact infrastructure detail"),
    ("possible client/employer name", r"\b(?:Flipkart|Amazon|Accenture|Fintellix|Onsurity|Google)\b",
     "describe the institution by type and scale instead"),
]

WORD_RANGE = {"case-study": (700, 3000), "publication": (500, 4500)}


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def split_front_matter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    block = text[3:end].strip("\n")
    body = text[end + 4:]
    data = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
        data[key.strip()] = val
    return data, body


def validate(path):
    problems, warnings = [], []
    text = read(path)
    meta, body = split_front_matter(text)
    name = os.path.basename(path)

    if meta is None:
        return ["no YAML front matter found"], warnings

    for key in REQUIRED_KEYS:
        if key not in meta or meta[key] in ("", None):
            problems.append(f"front matter: missing or empty '{key}'")
    for key, allowed in ALLOWED.items():
        if key in meta and meta[key] not in allowed:
            problems.append(f"front matter: '{key}' is '{meta[key]}', expected one of {sorted(allowed)}")

    ident = str(meta.get("id", ""))
    if ident and not name.startswith(ident):
        problems.append(f"id '{ident}' does not match filename '{name}'")
    if ident and not re.fullmatch(r"(CS|PUB)-\d{4}-\d{3}", ident):
        problems.append(f"id '{ident}' should look like CS-2026-001 or PUB-2026-001")

    date = str(meta.get("date", ""))
    if date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        problems.append(f"date '{date}' should be ISO YYYY-MM-DD")

    summary = str(meta.get("summary", ""))
    if len(summary) > 240:
        problems.append(f"summary is {len(summary)} characters, keep it under 240")

    kind = meta.get("type", "case-study")
    required = CASE_SECTIONS if kind == "case-study" else PUB_SECTIONS
    for heading in required:
        if heading.lower() not in body.lower():
            problems.append(f"missing required section: {heading}")

    if "disclaimer" not in body.lower():
        problems.append("missing the Disclaimer paragraph at the end")

    words = len(re.findall(r"\b[\w'-]+\b", body))
    lo, hi = WORD_RANGE.get(kind, (0, 10 ** 6))
    if not lo <= words <= hi:
        warnings.append(f"body is {words} words, expected {lo}-{hi} for a {kind}")

    # Safety scan runs on the body only: front matter legitimately holds an email-free handle,
    # but the prose must never carry contact details or identifiers.
    for label, pattern, hint in SAFETY:
        for match in set(re.findall(pattern, body, flags=re.I)):
            if label == "payment-card number" and re.fullmatch(r"\d{4}", str(match)):
                continue
            if label == "possible client/employer name":
                # Allowed only inside an explicit limitation/attribution sentence.
                ctx = body.lower()
                if "no affiliation" in ctx or "not affiliated" in ctx:
                    continue
            problems.append(f"safety: found {label} ({match!r}) — {hint}")
    if re.search(r"\b(?:lorem ipsum|TODO|FIXME|XXX)\b", body, flags=re.I):
        problems.append("safety: placeholder text left in the body")

    return problems, warnings


def all_targets():
    out = []
    for folder in ("case-studies", "publications"):
        base = os.path.join(ROOT, folder)
        if not os.path.isdir(base):
            continue
        for dirpath, _, files in os.walk(base):
            for f in sorted(files):
                if f.endswith(".md"):
                    out.append(os.path.join(dirpath, f))
    return out


def check_registry():
    problems = []
    reg_path = os.path.join(ROOT, "index", "case-studies.json")
    if not os.path.exists(reg_path):
        return ["registry not found: index/case-studies.json"]
    data = json.loads(read(reg_path))
    seen = set()
    for entry in data.get("entries", []):
        ident = entry.get("id", "?")
        if ident in seen:
            problems.append(f"registry: duplicate id {ident}")
        seen.add(ident)
        for field in ("id", "type", "title", "date", "category", "summary", "url", "status"):
            if not entry.get(field):
                problems.append(f"registry: {ident} is missing '{field}'")
        url = entry.get("url", "")
        if url and not url.startswith("http") and not os.path.exists(os.path.join(ROOT, url)):
            problems.append(f"registry: {ident} points at a missing file: {url}")
        if len(str(entry.get("summary", ""))) > 240:
            problems.append(f"registry: {ident} summary is too long")
    return problems


def main(argv):
    if not argv:
        print(__doc__)
        return 1

    if argv[0] == "--registry":
        problems = check_registry()
        for p in problems:
            print(f"FAIL {p}")
        print("registry OK" if not problems else f"{len(problems)} problem(s)")
        return 1 if problems else 0

    targets = all_targets() if argv[0] == "--all" else argv
    failed = 0
    for path in targets:
        if not os.path.exists(path):
            print(f"FAIL {path}: file not found")
            failed += 1
            continue
        problems, warnings = validate(path)
        if problems:
            failed += 1
            print(f"FAIL {path}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"PASS {path}")
        for w in warnings:
            print(f"  ~ {w}")
    print(f"\n{len(targets) - failed}/{len(targets)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
