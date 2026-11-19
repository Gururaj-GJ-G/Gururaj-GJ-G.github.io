# Contributing a case study or publication

Thanks for contributing. These rules exist because fraud write-ups get read by two audiences at
once: people who want to learn the method, and people looking for a reason to discredit it. Both
are served by the same thing — evidence you can defend, and nothing you cannot.

## 1. Hard rules

1. **No identifiable data.** No real names, phone numbers, email addresses, UPI IDs, account or
   card numbers, Aadhaar/PAN numbers, addresses, IP addresses, device IDs, order IDs or screenshots
   containing any of these. Replace them with synthetic values and say so.
2. **No employer or client identification.** Do not name a client, an employer, a merchant under
   investigation, or a payment provider's internal system. Describe the *type* of institution
   ("a mid-sized NBFC", "a card acquirer") instead.
3. **No unverified claim stated as fact.** If you did not verify it, write "suspected", "reported",
   "could not be confirmed", or leave it out. This applies especially to malware, data theft,
   attribution to a named group, and financial loss figures.
4. **No confidential material.** No internal SOPs, pricing, thresholds, rule identifiers, model
   weights or client deliverables from a paid engagement, unless the owner has released them.
5. **No personal data of the author beyond a public handle.** Credit is a name and a link, nothing more.
6. **No defamation.** Do not name a business as fraudulent unless there is a public, citable
   determination (regulator action, court order, published scheme notice).

## 2. Anonymising a case

Work down this list before you write a single line:

- **People** → role only: "the seller", "the analyst", "Account A", "Entity E004".
- **Businesses** → sector and scale: "a Bengaluru-based electronics reseller".
- **Amounts** → either keep the real amount (if it is not identifying) or round to a band
  (₹0–1 lakh, ₹1–5 lakh) and state that it is rounded.
- **Dates** → keep the month and year; drop the exact day unless the timeline matters.
- **Platforms** → keep the platform if the abuse pattern is platform-specific and public
  (e.g. a marketplace listing scam); otherwise say "a classifieds marketplace".
- **Screenshots** → redact names, numbers, profile photos and handles; keep the layout and the
  evidence-bearing detail.
- **Evidence files** → describe them, do not attach originals. If you attach a sample, regenerate it
  with synthetic content.

## 3. Evidence standard

Every factual claim in the piece should be traceable to one of:

- a screenshot or artefact you hold and have described (hashed, if you publish the hash);
- a public source you cite;
- an observation you made, stated as an observation.

If a claim has none of these, either soften it or remove it. "I could not confirm X" is a stronger
sentence than an unsupported X.

## 4. Structure and length

- Case study: 800–2,500 words. Publication: 600–4,000 words.
- Required sections are listed in the templates; do not rename them, the validator looks for them.
- Lead with the finding in the first paragraph. Assume the reader stops after two paragraphs.

## 5. Licensing and credit

- Write-ups are published under **CC BY 4.0** unless the author states otherwise in the front
  matter (`license:` field). Code snippets inside a write-up are MIT.
- Credit co-authors in `author:` and in an `## Acknowledgements` section if the contribution was
  substantial.
- Do not submit work you do not have the right to publish. If a case came out of employment, check
  your contract and your ex-employer's policy first; when in doubt, publish the method, not the case.

## 6. Review process

1. Open a pull request (Route A) or an issue (Route C) — see `README.md`.
2. CI runs `scripts/validate.py`. Fix anything it flags.
3. A maintainer reviews against `checklists/pre-publish-checklist.md` and leaves comments.
4. Two approvals are needed for anything describing a live or recent (under 12 months) case.
5. Merge, then the registry entry drives the portfolio card.

## 7. Withdrawing a piece

Open a PR that sets `status: withdrawn` in the front matter and removes the registry entry. The file
stays in the repository for the audit trail. Do not delete history.
