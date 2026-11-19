---
id: CS-2026-001
title: "Payment-Direction Deception on a Classifieds Marketplace"
type: case-study
status: published
date: 2026-04-01
author: "Gururaj G J (Gururaj-GJ-G)"
category: marketplace
jurisdiction: IN
platform: ""
loss: prevented
evidence: redacted-real
license: CC-BY-4.0
tags: [social-engineering, payment-direction, marketplace-fraud, qr-code]
summary: "A seller was targeted within minutes of listing an item: two images implied a payment had been received when none had been sent. The seller checked the balance, not the screenshot, and no money moved."
portfolio_card: true
---

# Payment-Direction Deception on a Classifieds Marketplace

## 1. Summary

A seller published a classifieds listing and was contacted by an unknown party within minutes. The
contact sent two images — a QR-style graphic labelled as a ₹1.00 credit, and a photograph of a
merchant POS terminal — then asked the seller to complete a step to "release" the money. Neither
image evidenced an incoming payment. The seller checked the account balance rather than the
screenshot, recognised the payment-direction reversal, and declined to act. No funds left the
account.

The pattern matters because it needs no stolen credentials, no malware and no data breach. It needs
one misread step: a victim who confuses *receiving* money with *sending* money.

## 2. Context

- **Who was exposed:** an individual seller, not a business. The loss, had it succeeded, would have
  been the item's value plus whatever the "release" step demanded.
- **Platform:** a large Indian classifieds marketplace where sellers publish a contact number or
  accept in-app chat, so the conversation moves off-platform almost immediately.
- **Timing:** April 2026. The approach arrived within minutes of publication, consistent with
  automated monitoring of new listings rather than a human browsing the category.
- **Why it matters:** card, UPI and wallet controls do not help here, because the victim authorises
  the transfer themselves.

## 3. What the parties saw

1. Listing goes live; an unknown number opens contact on a messaging app.
2. First image: a QR-style graphic carrying a "Received Money ₹1.00" label.
3. Second image: a photograph of a merchant POS terminal showing a payment-processing interface.
4. Message: the "buyer" says the payment is on hold and asks the seller to scan a code or open a link
   to receive it.

What was visible at the time was a plausible-looking pair of screenshots. What was established later
is that neither artefact can evidence a credit: a QR graphic carries no transaction record, and a
photograph of a terminal shows a device, not a settlement.

## 4. Method

1. **Preserve first.** Capture the conversation with timestamps before replying to anything.
2. **Reconstruct the timeline.** Log message timestamps at second-level granularity to test whether
   first contact was human or automated.
3. **Examine the artefacts.** Image dimensions, compression and layout — whether the graphics match
   genuine app screenshots or are composites.
4. **Test the claim against the mechanism.** Ask what record a genuine credit would produce — a bank
   or UPI reference, an app notification, a balance change — and check whether any of it exists.
   None did.
5. **Read the ask.** Every payment-direction deception ends with an action that *sends* money or
   grants access. The ask is the tell, and it is the fastest thing to check.

## 5. Evidence

| Artefact | What it shows | Integrity |
|---|---|---|
| Listing page capture | publication time, item, contact route | held, hashed |
| Chat transcript export | contact arrived four minutes after publication | held, hashed |
| Image 1 — QR-style "received ₹1.00" | no transaction reference of any kind | held, hashed |
| Image 2 — POS terminal photograph | a device screen, not a settlement record | held, hashed |
| Sender number | off-platform, unverified identity | reported to platform |

Originals are not published and identifiers are withheld.

## 6. Findings

- **Confirmed** — contact was initiated within minutes of publication, before any negotiation.
- **Confirmed** — neither artefact contained a transaction reference, and the account balance did not
  change.
- **Confirmed** — the request that followed was an action that would have moved money outward.
- **Probable** — the approach was templated and sent to multiple new listings; the wording and
  cadence were not tailored to the item.
- **Unconfirmed** — who operated the number, and whether the POS photograph was genuine, borrowed or
  generated. No attribution is made.

## 7. Indicators and red flags

- Payment "confirmed" by an image, never by a balance, notification or reference number.
- Contact within minutes of publication.
- Any request to scan a code, open a link, or enter a PIN **in order to receive** money.
- A POS terminal or merchant-app screenshot offered as proof of a transfer to a personal account.
- Pressure to act before the item is inspected or collected.
- Move to a messaging app before the first real exchange.

## 8. What stopped it / what would have stopped it

- The seller checked the balance instead of the screenshot. That single habit defeats the pattern.
- A prompt on new listings — "never scan a code to receive money" — would remove most of the
  exposure at the point of contact.
- In-app chat with number masking delays the off-platform move.

## 9. Limitations

- Single case with no loss, so no loss figure is claimed.
- The sender's identity was never established; nothing here should be read as an allegation against
  any identifiable person.
- The judgement that the artefacts were composites rests on layout and metadata, not on device
  examination of the sender's phone.

## 10. References

- Reserve Bank of India, customer-awareness material on UPI "request money" and QR-code frauds
  (accessed April 2026).
- National Cyber Crime Reporting Portal, guidance on reporting unauthorised transactions
  (accessed April 2026).

---

**Disclaimer.** This write-up describes a single documented instance and is published for
professional education. All personal and institutional identifiers have been removed or replaced
with synthetic values. Findings are limited to the evidence described above; nothing here should be
read as an allegation against any named or unnamed party.
