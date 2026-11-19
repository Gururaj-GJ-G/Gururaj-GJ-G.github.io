---
id: PUB-2026-001
title: "What a Payment-Risk Reviewer Actually Wants From an Onboarding Pack"
type: publication
subtype: methodology
status: published
date: 2026-11-01
author: "Gururaj G J (Gururaj-GJ-G)"
category: merchant-risk
jurisdiction: GLOBAL
evidence: public-sources
license: CC-BY-4.0
tags: [merchant-risk, kyb, onboarding, evidence-packaging]
summary: "Merchant onboarding fails on evidence, not on the business model. A five-layer assessment and one well-built evidence pack answer the questions a reviewer is actually asking."
portfolio_card: true
---

# What a Payment-Risk Reviewer Actually Wants From an Onboarding Pack

## Abstract

Most merchant onboarding rejections are not judgements about a business model. They are the reviewer
being unable to answer four questions from the documents in front of them: who is this, what do they
sell, does the storefront support that claim, and where does the money go. This note sets out a
five-layer assessment structure and an evidence-package template that answer those questions in the
order a reviewer asks them. It is drawn from a compliance-first playbook prepared for a merchant-risk
advisory engagement; client details are omitted.

## 1. The problem

A merchant submits a company registration, a bank statement and a website link. The reviewer has to
decide, inside a service-level window, whether to approve, ask for more, or decline. When the pack is
thin the only safe answer is "ask for more", and every round trip costs days, frustrates a legitimate
merchant, and pushes the queue back.

The cost is asymmetric in a way that is worth stating plainly: a slow approval loses a customer; a
wrong approval can cost the acquirer far more, in fines, scheme penalties and chargebacks. Reviewers
behave accordingly, which is why vague packs get rejected rather than argued with.

## 2. Why current practice falls short

Three failure modes recur.

**Documents without structure.** Forty files with no cover note force the reviewer to reconstruct the
story. Reconstructed stories get rejected.

**Website claims without evidence.** "We sell electronics" is a statement, not evidence. A storefront
with three placeholder products, no returns policy and no business address contradicts the claim, and
the contradiction is what the reviewer records.

**Identity without linkage.** The registered entity, the bank account holder and the payout
beneficiary are frequently three different names. Unless the pack explains the relationship, it reads
as concealment — which is precisely the pattern transaction-laundering controls exist to catch.

## 3. The proposed approach

Assess and document in five layers. Each layer answers one reviewer question and produces one section
of the pack.

| Layer | Question it answers | Evidence it produces |
|---|---|---|
| Identity and KYB | Who is contracting, and who controls it? | registration, UBO chain, director IDs, authorisation to sign |
| Business model and storefront | What is sold, to whom, at what price? | live URLs, catalogue, pricing, shipping, returns, contact page |
| Category and product risk | Is anything restricted, regulated or prohibited? | product list with category mapping, licences where applicable |
| Early trading behaviour | Does actual traffic match the declared model? | first-90-day volumes, average ticket, refund and chargeback rates |
| Payout exposure and linkage | Where does the money land, and who else lands there? | settlement account proof, beneficiary linkage, shared-service disclosure |

The order matters. Reviewers start at identity, and a pack that answers layers one and five but not
two and three still gets returned.

## 4. How it works in practice

A worked shape, using a synthetic merchant:

1. **Cover note** — one page: what the business does, monthly volume expected, ticket size, the three
   things about this merchant that usually raise questions and the answer to each.
2. **Identity** — certificate of incorporation, UBO chart to natural persons, director identity,
   board resolution naming the signatory.
3. **Storefront** — screenshots with URLs and capture dates, catalogue extract, returns and refund
   policy, customer-service contact that actually answers.
4. **Category** — product list mapped to scheme and acquirer category rules, with the licence
   attached for anything regulated.
5. **Trading** — the first-90-day plan, plus any historical processing data with the same descriptors
   the merchant will bill under.
6. **Payout** — bank proof, a signed statement of the relationship between entity, account holder and
   beneficiary, and disclosure of any shared services with other merchants.

The single highest-value item is the descriptor in step six. A billing descriptor that does not match
the storefront is the most common reason a clean merchant gets flagged, and the cheapest thing to fix
before submission.

## 5. Trade-offs and failure modes

- **It costs the merchant real effort.** A five-layer pack is not a two-click form; it is defensible
  precisely because it is work. Self-serve onboarding needs a lighter path with the same information
  collected progressively.
- **It cannot fix a bad business.** A well-packaged prohibited merchant is still prohibited; the
  structure speeds the decline, it does not prevent it.
- **It decays.** A pack is a snapshot. The layer that matters after month three is trading behaviour,
  which requires monitoring rather than documentation.
- **It over-documents small merchants** if applied without proportion. Scale the evidence to the risk
  tier, not to the template.

## 6. What to measure

- **First-pass approval rate** — share of applications approved without a document request.
- **Median round trips** — document requests per application before decision.
- **Time to first transaction** — submission to first settled payment.
- **Post-approval mismatch rate** — approved merchants whose live descriptor or category differs from
  the declared one.
- **Early chargeback ratio at 90 days** — the honest test of whether the pack predicted anything.

## 7. Conclusion

Build the pack around the reviewer's four questions, in their order, and put the descriptor at the
front of your mind rather than the back. Most "merchant risk" problems at onboarding are evidence
problems, and evidence problems are fixable before submission.

---

**Disclaimer.** The views here are the author's own and describe a method, not a client engagement.
Any figures or cases are synthetic or drawn from public sources.
