# Pre-publish checklist

Copy this into the pull request description and tick every line. A maintainer will not merge with an
unticked box.

## Front matter
- [ ] `id` matches the filename prefix (`CS-2026-001` → `CS-2026-001-…md`)
- [ ] `status` is `review` or `published`
- [ ] `date` is the publication date, not the incident date
- [ ] `author` has a GitHub handle
- [ ] `category` is one of the allowed values
- [ ] `evidence` correctly says `synthetic`, `redacted-real` or `public-sources`
- [ ] `summary` is one or two sentences and contains no claim the body does not support

## Safety
- [ ] No real names, phone numbers, emails, UPI IDs, account/card numbers, Aadhaar/PAN, addresses, IPs or device IDs
- [ ] No employer, client or merchant under investigation is identifiable
- [ ] Screenshots are redacted and re-checked at 100% zoom, including edges and status bars
- [ ] No confidential SOP, threshold, pricing or rule identifier from a paid engagement
- [ ] No person or business is described as fraudulent without a public determination
- [ ] Data-protection position checked: DPDP Act 2023 for Indian personal data, contract terms for employer data

## Accuracy
- [ ] Every factual claim is traceable to an artefact, a public source, or a stated observation
- [ ] Findings are marked confirmed / probable / unconfirmed
- [ ] Amounts, dates and counts agree with the evidence section
- [ ] Unverified technical claims (malware, data theft, attribution) are hedged or removed
- [ ] Limitations section is present and honest

## Structure
- [ ] All required sections present, in order, with the template headings
- [ ] Word count within range (case study 800–2,500; publication 600–4,000)
- [ ] Disclaimer present at the end
- [ ] References have access dates

## Registry and portfolio
- [ ] Entry added to `index/case-studies.json` with matching id, title, date, category, status
- [ ] Card snippet added to the portfolio grid, or a link supplied for the maintainer
- [ ] Links tested; no more than two per card; no dead links
- [ ] `python scripts/validate.py <file>` passes locally
- [ ] CI check green on the pull request
