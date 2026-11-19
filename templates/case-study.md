---
id: CS-YYYY-NNN
title: "Short, concrete title — what happened, not what it proves"
type: case-study
status: draft            # draft | review | published | withdrawn
date: YYYY-MM-DD         # date of publication, not of the incident
author: "Your Name (github-handle)"
category: marketplace    # marketplace | payments | merchant-risk | aml | ato | forensics | other
jurisdiction: IN         # ISO country code, or GLOBAL
platform: ""             # public platform name if the pattern is platform-specific, else leave blank
loss: none               # none | prevented | reported — never invent a figure
evidence: synthetic      # synthetic | redacted-real | public-sources
license: CC-BY-4.0
tags: [tag-one, tag-two]
summary: "One or two sentences a reader could quote. No jargon, no hype."
portfolio_card: true
---

# Title again, as a heading

*Everything in italics is guidance — delete it before submitting.*

## 1. Summary

*Three to five sentences: what happened, how it was detected, what it cost, what the outcome was.
A reader who stops here must not be misled.*

## 2. Context

*Who was exposed, on what kind of platform, and why it mattered. Describe institutions by type and
scale, never by name. State the timeframe to the month.*

## 3. What the parties saw

*The signals available at the time, in the order they appeared. Separate what was visible from what
was later established.*

## 4. Method

*How you investigated. Tooling, sequence, and the reasoning behind each step. This is the section
other investigators will copy — make it repeatable.*

1. …
2. …
3. …

## 5. Evidence

*What you held: artefacts, screenshots (redacted), hashes, message logs, registry or public records.
Describe, do not attach originals. If you published a hash, give it here.*

| Artefact | What it shows | Integrity |
|---|---|---|
| e.g. listing screenshot | price and contact route | SHA-256 `…` |

## 6. Findings

*What the evidence supports, stated at the strength the evidence allows. Mark each finding
**confirmed**, **probable** or **unconfirmed**.*

- **Confirmed** — …
- **Probable** — …
- **Unconfirmed** — …

## 7. Indicators and red flags

*The transferable part: what a reader should watch for next time. Bullet form, one line each.*

## 8. What stopped it / what would have stopped it

*Controls, checks, or user behaviour that worked, and the ones that would have caught it earlier.*

## 9. Limitations

*What you could not verify, what you assumed, what would change the conclusion. Never leave this
section out — it is what makes the rest credible.*

## 10. References

*Public sources only, one per line, with access dates.*

---

**Disclaimer.** This write-up describes a single documented instance and is published for
professional education. All personal and institutional identifiers have been removed or replaced
with synthetic values. Findings are limited to the evidence described above; nothing here should be
read as an allegation against any named or unnamed party.
