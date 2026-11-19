---
id: PUB-2026-003
title: "Six Questions a Payment-Fraud Dashboard Should Answer"
type: publication
subtype: article
status: published
date: 2026-09-20
author: "Gururaj G J (Gururaj-GJ-G)"
category: payments
jurisdiction: IN
evidence: public-sources
license: CC-BY-4.0
tags: [dashboards, payments, metrics, operations]
summary: "Most fraud dashboards report activity. The useful ones answer six questions: what is leaking, where, from whom, why now, what did we miss, and what did we get wrong."
portfolio_card: true
---

# Six Questions a Payment-Fraud Dashboard Should Answer

## Abstract

Fraud dashboards usually report activity — alerts raised, cases closed, blocks applied. Activity is
easy to count and tells an operator almost nothing about whether losses are being prevented. This note
sets out six questions a payment-fraud dashboard should answer, with the metric and the trap for each,
and argues that the last two questions are the ones that separate a monitoring screen from a control.

## 1. The problem

A dashboard full of activity metrics creates a false sense of control. Alert volume rises, cases close,
the screen is green — while the loss rate climbs, because nobody is measuring the loss rate on that
screen. The metrics that matter are usually absent because they require joins across systems: the
payment record, the dispute record, the case record and the customer record.

## 2. Why current practice falls short

Three habits get in the way.

**Counting inputs.** Alerts, blocks and reviews are inputs. They say how busy the team is.

**Aggregating away the detail.** A monthly loss figure hides the fact that losses doubled in one
payment method, one merchant category and one time window. Aggregates conceal the pattern you need.

**No counterfactual.** Nobody records what would have happened without the control, so nobody can say
whether the control earned its cost.

## 3. The proposed approach

Six questions, in the order an operator should read them.

| Question | Metric | The trap |
|---|---|---|
| What is leaking? | Loss rate per ₹1,000 processed, by method | Reporting absolute losses; volume growth masks a falling rate |
| Where? | Loss rate by channel, merchant category, geography, ticket band | Averages hide a single hot cell — always break down to the cell |
| From whom? | Share of loss from repeat actors and linked accounts | First-party fraud looks like a customer problem until you count repeat devices |
| Why now? | Change versus the prior period, with the trigger identified | Attributing drift to "seasonality" without checking |
| What did we miss? | False-negative rate from post-hoc review of approved-and-disputed transactions | Only measuring the alerts you raised |
| What did we get wrong? | False-positive rate and customer friction cost per block | Treating declines as free |

The two that matter most are the last two. A false-negative review — sampling transactions that were
approved and later disputed — is the only way to see the fraud your rules did not catch. And a
false-positive count is the only way to see what the control costs in lost customers, which is a real
loss line that never appears in a fraud budget.

## 4. How it works in practice

A worked week, synthetic figures:

- Loss rate 0.41 per ₹1,000, up from 0.28 the prior week — question one flags it.
- Breakdown puts almost all of the increase in one ticket band and one payment method — question two
  localises it.
- Repeat-actor share in that cell is 63%, with a cluster of accounts sharing two device fingerprints —
  question three reframes it from "fraud spike" to "one ring".
- Change coincides with a checkout release — question four identifies the trigger.
- Post-hoc review of 200 approved-and-disputed transactions finds 9 with the same device cluster —
  question five proves the rule gap.
- Blocked customers in that cell number 41, of whom 6 complained — question six prices the control.

The output is not a screen. It is three sentences and one decision: tighten the rule for one cell,
revert part of the checkout change, and accept the friction cost in the other.

## 5. Trade-offs and failure modes

- **False-negative review is expensive.** Sampling needs judgement and time; a 200-transaction sample
  per week is a real cost and worth it.
- **Friction is hard to price honestly.** Complaint counts undercount silent abandonment, so treat the
  friction figure as a floor.
- **Segment definitions drift.** If "merchant category" is free text, every breakdown is noise.
- **Dashboard latency invites gaming.** A daily figure can be managed; a weekly trend cannot.

## 6. What to measure

- Loss rate per ₹1,000 processed, weekly, by cell.
- False-negative rate from the weekly post-hoc sample.
- False-positive rate and complaint rate per 1,000 blocks.
- Repeat-actor share of total loss.
- Time from first signal to case decision, median and 90th percentile.

## 7. Conclusion

If a dashboard cannot answer "what did we miss?" and "what did we get wrong?", it is a status screen,
not a control. Both questions are answerable with data most payment teams already hold — they simply
require sampling and a join that nobody has been asked to build.

---

**Disclaimer.** The views here are the author's own. All figures are synthetic and used to illustrate
a method.
