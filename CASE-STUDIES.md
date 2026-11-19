# Case Studies & Publications — Publishing Kit

How a case study or publication gets from a draft to a public GitHub link, and from there onto the
**Case Studies & Publications** section of [gururaj-gj-g.github.io](https://gururaj-gj-g.github.io/).

This kit is for anyone publishing here — the site owner, a co-author, or an outside contributor who
has an investigation write-up worth sharing.

---

## 1. How publishing works

There are three routes. Pick the one that matches who is publishing.

### Route A — Contributor sends a case study to this repository (recommended)

Best when the piece should live alongside the others and appear on the portfolio.

1. **Fork** the repository (or, if you have write access, branch from `main`).
2. Copy a template:
   - case study → `templates/case-study.md`
   - article, paper or methodology note → `templates/publication.md`
3. Save it as `case-studies/CS-YYYY-NNN-short-slug.md` (case studies) or
   `publications/PUB-YYYY-NNN-short-slug.md` (publications). The `NNN` is the next free number;
   ask in an issue if you are unsure.
4. Fill in the front matter and every required section. Delete the guidance lines in *italics*.
5. Add one entry to `index/case-studies.json` (the registry the portfolio reads).
6. Run the checks locally:
   ```bash
   python scripts/validate.py case-studies/CS-2026-001-your-slug.md
   ```
7. Open a **pull request**. The `validate-case-study` workflow runs automatically. A PR that fails
   the check cannot be merged.
8. After merge, the piece is live at
   `https://github.com/<owner>/<repo>/blob/main/case-studies/<file>.md`, and the portfolio card is
   added with the snippet in `templates/portfolio-card.html`.

### Route B — Publish in your own repository, then link it

Best when the work belongs to you and you want to keep ownership.

1. Create a repository, e.g. `your-name/case-study-<slug>`, with the write-up in `README.md`.
2. Follow the same front matter and sections from the templates in this kit.
3. Send a one-line issue to this repository: title, one-paragraph summary, repo URL, and the
   category it belongs in. It gets added to `index/case-studies.json` and the portfolio grid.

### Route C — Issue-only submission

Best for a short finding, a red-flag pattern, or a case you can describe but not document in full.

1. Open an issue using the **Case study proposal** template.
2. Include: what happened, why it matters, what evidence exists, and what can be published safely.
3. It is reviewed like any other submission; a maintainer may convert it into a full write-up with
   you credited, or decline it with a reason.

---

## 2. What "published" means here

A case study is published when all of the following are true:

| Requirement | Why |
|---|---|
| Front matter complete and validated | Makes it indexable and sortable |
| Every required section present | Readers can follow the investigation, not just the conclusion |
| Synthetic or anonymised data only | Protects real customers, merchants and employers |
| Claims match the evidence held | The page must survive a reader asking "how do you know?" |
| Disclaimer line present | Readers know what kind of document they are reading |
| Registry entry added | Otherwise the piece is invisible on the portfolio |

---

## 3. Repository layout

These files live in the portfolio repository (`Gururaj-GJ-G.github.io`), alongside the site:

```
Gururaj-GJ-G.github.io/
├── index.html                  ← the Case Studies & Publications grid
├── style.css                   ← includes the reader-page typography
├── CASE-STUDIES.md             ← this guide
├── CONTRIBUTING.md             ← rules, anonymisation, evidence standards
├── case-studies/               ← one markdown file per case study
├── publications/               ← one markdown file per article or paper
├── cases/                      ← generated reader pages (commit these)
├── index/
│   └── case-studies.json       ← registry: drives the build and the cards
├── templates/
│   ├── case-study.md
│   ├── publication.md
│   └── portfolio-card.html
├── checklists/
│   └── pre-publish-checklist.md
├── scripts/
│   ├── validate.py             ← front matter + safety checks
│   └── build_cases.py          ← markdown → styled page in cases/
└── .github/
    ├── workflows/validate-case-study.yml
    ├── ISSUE_TEMPLATE/case-study-proposal.md
    └── pull_request_template.md
```

Writing is markdown; reading is HTML. `scripts/build_cases.py` converts each published entry into a
page under `cases/` that reuses the site stylesheet, so a reader never leaves the domain and never
sees raw markdown. Commit both the source and the generated page.

## 4. Naming and numbering

- Case studies: `CS-<year>-<3-digit sequence>-<kebab-slug>.md` → `CS-2026-001-olx-payment-direction-deception.md`
- Publications: `PUB-<year>-<3-digit sequence>-<kebab-slug>.md`
- Sequence numbers are never reused, even if a piece is withdrawn.
- The `id` in the front matter must match the filename prefix: `CS-2026-001`.

---

## 5. Review: what a maintainer checks

1. `python scripts/validate.py <file>` passes.
2. No real person, merchant, customer or employer is identifiable — see `CONTRIBUTING.md`.
3. No unverified technical claim (malware, data theft, attribution) is stated as fact.
4. Figures, dates and amounts agree with the evidence described in the piece.
5. The registry entry matches the file (id, title, date, category, status).
6. Two working links at most per card; no dead links.

Reviewers leave comments in the PR. A submission is merged once every item in
`checklists/pre-publish-checklist.md` is ticked.
