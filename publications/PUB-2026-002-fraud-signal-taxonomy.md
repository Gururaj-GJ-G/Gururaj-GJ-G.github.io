---
id: PUB-2026-002
title: "A Fraud Signal Taxonomy That Survives an Audit"
type: publication
subtype: methodology
status: published
date: 2026-10-15
author: "Gururaj G J (Gururaj-GJ-G)"
category: methodology
jurisdiction: GLOBAL
evidence: public-sources
license: CC-BY-4.0
tags: [signals, explainability, decisioning, governance]
summary: "Signals drift into folklore when nobody owns their definitions. Seven categories, a weight rationale per signal, and a version field turn a signal list into an auditable asset."
portfolio_card: true
---

# A Fraud Signal Taxonomy That Survives an Audit

## Abstract

Every fraud team accumulates signals. Few can say, on request, what a signal means, why it carries the
weight it does, when it changed, or which decisions it has driven. That gap is what an auditor,
regulator or challenger model finds first. This note proposes a taxonomy structure — seven
categories, per-signal weight rationale, explicit trigger conditions, and a version stamp — that keeps
a signal library defensible as it grows.

## 1. The problem

A signal that cannot be explained is a signal that cannot be defended. When a customer disputes a
block, the question is not "was the model right?" but "what did you observe, and why did that justify
the action?" A list of feature names answers neither part.

Three symptoms show the library has become folklore:

- two teams implement "impossible travel" with different thresholds and both call it the same signal;
- a weight is changed during an incident and nobody records it;
- a signal is retired but still fires inside a legacy rule pack.

## 2. Why current practice falls short

Feature stores solve retrieval, not meaning. Model registries version models, not the semantics of the
inputs. Neither tells an investigator that a signal means *this device changed the SIM in the last
twenty-four hours and the account changed its payout destination within the same window* — which is
the sentence that makes a decision defensible.

## 3. The proposed approach

**Seven categories.** Device, network, behaviour, authentication, account, linkage, transaction. The
split is not academic: each category has a different evidence source, a different retention period
and a different failure mode, so grouping by category makes it obvious where a library is thin. Most
teams are heavy on transaction and device signals and almost empty on linkage — which is where
mule and ring behaviour actually shows.

**A record per signal.** Every signal carries:

| Field | Why it exists |
|---|---|
| `id` | stable key, never reused |
| `name` | plain-language meaning, no jargon |
| `category` | one of the seven |
| `trigger` | the precise condition, in words an investigator can read |
| `evidence` | what the investigator is shown when it fires |
| `weight` | score impact, plus the reasoning for that value |
| `source` | system of record the signal is computed from |
| `version` | semantic version of the definition |
| `owner` | the team accountable for its accuracy |

**Named rule packs.** Signals score; packs decide. A pack is a named combination mapped to a typology
— account-takeover reset, impossible travel, emulator plus hooking, device farming, remote-control
takeover, payout-abuse chains, mule pass-through. Naming them makes coverage auditable: you can say
which typologies you detect and which you do not.

**Deterministic outcomes.** ALLOW, REVIEW or BLOCK, with the triggered signals, their evidence and a
narrative. A deterministic engine will not out-perform a good model on raw detection; it will survive
a conversation with a regulator, which is the binding constraint in most regulated environments.

## 4. How it works in practice

A decision narrative that an auditor can follow:

> **REVIEW** — score 62. Triggered: `DEV-SIM-CHANGE-01` (SIM changed 14 hours before the request;
> evidence: carrier record), `ACC-PAYOUT-CHANGE-02` (payout destination added 11 hours before
> request), `NET-ASN-NEW-03` (first sighting of this ASN for the account). Rule pack:
> payout-abuse chain. Not triggered: device compromise signals, so a takeover narrative is not
> supported — this is a payout-destination change, not a compromised handset.

Note what that narrative does: it states the decision, the signals, the evidence, and — critically —
what was *not* observed and why that matters. The last part is what most systems omit and what
investigators ask for.

## 5. Trade-offs and failure modes

- **Weights are opinions until calibrated.** Write the rationale at the time of writing, not later;
  "0.35 because it appeared in 62% of confirmed mule cases in Q3" is defensible, "0.35" is not.
- **Deterministic engines do not generalise.** They catch what you thought of. Pair them with
  monitoring for the typologies you have not named yet.
- **Taxonomies rot.** Without an owner per signal and a review cadence, the library becomes a museum
  within a year.
- **Explainability has a cost.** Narratives slow decisions slightly and require the evidence to be
  retrievable at decision time, which means retention policy has to be designed, not assumed.

## 6. What to measure

- **Signal coverage per category** — how many typologies each category can support.
- **Firing rate per signal** — a signal that never fires is dead weight; one that always fires is a
  broken threshold.
- **Narrative completeness** — share of decisions where every triggered signal has attached evidence.
- **Override rate** — how often investigators disagree with the engine, by pack. This is the best
  available feedback signal.
- **Definition churn** — signals changed per quarter, and whether each change was recorded.

## 7. Conclusion

Write the library as if it will be read aloud in a dispute, because one day it will be. Seven
categories, a reason for every weight, and a version on every definition cost a week and save the
argument.

---

**Disclaimer.** The views here are the author's own and describe a method, not a client engagement.
Any figures or cases are synthetic or drawn from public sources.
