---
id: CS-2026-002
title: "Loan-App Harassment: Nine Days From Panic to Remediation"
type: case-study
status: published
date: 2026-10-25
author: "Gururaj G J (Gururaj-GJ-G)"
category: forensics
jurisdiction: IN
platform: ""
loss: none
evidence: redacted-real
license: CC-BY-4.0
tags: [android, forensics, loan-apps, harassment, privacy]
summary: "A borrower's phone carried seven sideloaded APKs and her contacts were being used to pressure her. Nine days of device forensics, permission auditing and evidence packaging turned a panic into a documented case."
portfolio_card: true
---

# Loan-App Harassment: Nine Days From Panic to Remediation

## 1. Summary

Someone who had applied for two consumer loans contacted me in distress: repeated refusals,
then immediate harassment calls from foreign numbers, unknown applications on her handset, and a
fear that her identity had been taken. Over nine days I audited the device over ADB, identified
seven sideloaded packages, reconstructed what each one could access, guided remediation, and
packaged the evidence for a cybercrime complaint.

The finding that mattered was not exotic malware. It was a permission model: a handset that had
been persuaded to grant contacts, SMS and storage access to applications installed from outside
the store, and a lender ecosystem in which that address book is the collection mechanism.

## 2. Context

- **Who was exposed:** one individual borrower, not a business. The exposure was social as much as
  financial — her contacts were the leverage.
- **Platform:** a mid-range Android handset (Android 13), applications sideloaded as APK files
  rather than installed from the Play Store.
- **Timing:** October 2025, nine days from first contact to documented closure.
- **Why it matters:** the harm from predatory lending apps is not only a fraudulent debit. It is
  the use of an address book as a pressure instrument, which most device-security advice does not
  address.

## 3. What the parties saw

1. Two loan applications were declined; no money was disbursed.
2. Within days, calls arrived from foreign numbers, referencing people in her contact list by name.
3. She noticed applications on the handset she did not remember installing.
4. Messages escalated from reminders to threats of circulating photographs.

What was visible was harassment and unfamiliar icons. What was established afterwards was the
mechanism: which packages were present, what permissions each held, and when they were installed.

## 4. Method

1. **Stabilise before investigating.** Told her to stop installing anything, stop granting
   permissions, and keep the handset powered on and offline from unknown Wi-Fi.
2. **Inventory the device over ADB.** `adb shell pm list packages -3` for third-party packages,
   `adb shell dumpsys package <pkg>` for install time, installer and granted permissions, and a
   listing of `/sdcard/Download/*.apk` for the installers themselves.
3. **Map capability, not intent.** For each package, record which dangerous permissions were
   granted: contacts, SMS, call log, storage, accessibility. Capability is what a reviewer can
   evidence; intent is what a headline claims.
4. **Preserve evidence before removal.** Hash the APK files, screenshot the permission screens,
   export the call log and message headers with timestamps.
5. **Remediate in order.** Revoke accessibility and device-admin grants first, then uninstall,
   then rotate credentials and enable 2FA on the accounts the apps could reach.
6. **Package for the complaint.** One timeline, one evidence index, one plain-language narrative —
   the format a cybercrime portal accepts.

## 5. Evidence

| Artefact | What it shows | Integrity |
|---|---|---|
| Package inventory (`pm list packages -3`) | seven sideloaded packages | held, hashed |
| Per-package `dumpsys` output | install times, installers, granted permissions | held, hashed |
| APK files from `/sdcard/Download` | installers retained on device | held, hashed |
| Call log and message headers | harassment timeline from foreign numbers | held, redacted |
| Screenshots of permission screens | what was granted, when | held |

APKs are not published. Identifiers are withheld and the victim is not named.

## 6. Findings

- **Confirmed** — seven sideloaded packages were present, none installed through the Play Store.
- **Confirmed** — at least three held contacts and SMS permissions, and one held accessibility,
  which allows an application to read screen content and act on other apps.
- **Confirmed** — harassment calls began after the applications were installed and referenced
  contact-list names.
- **Probable** — the contact list was harvested by one or more of these packages and used to
  pressure the borrower; the timing and the specificity of the calls support it, but the flow was
  not observed directly.
- **Unconfirmed** — who operated the calling numbers, whether data was sold onward, and whether any
  single application was the sole collector. No attribution is made, and no application is named
  here.

## 7. Indicators and red flags

- Loan approval offered through a direct APK download link, not an app store.
- Requests for contacts, SMS or accessibility access justified as "KYC" or "verification".
- A loan app that asks for more permission than it needs to disburse and collect.
- Harassment calls that quote names from your address book.
- Multiple near-identical APKs in the Downloads folder — variants of the same package.
- Pressure to repay to a personal UPI handle or wallet rather than a lender account.

## 8. What stopped it / what would have stopped it

- Revoking accessibility and device-admin rights before uninstalling stopped the immediate
  surveillance channel.
- Never installing outside the Play Store would have prevented the whole chain.
- Android's permission dashboard, checked monthly, would have surfaced the grants earlier.
- A lender that could only debit a bank account — never read an address book — removes the
  leverage entirely.

## 9. Limitations

- Device-level inspection only: no server-side data was available, so exfiltration is inferred from
  capability and timing rather than observed traffic.
- Two of the packages could not be analysed statically without specialist tooling, so their
  behaviour is described from permissions and install context.
- The victim's account of the calls is the only record of the harassment itself; the call log
  evidences the numbers, not the content.
- Nothing here should be read as an allegation against any named lender or application.

## 10. References

- Indian Computer Emergency Response Team (CERT-In), guidance on reporting cyber incidents
  (accessed October 2025).
- National Cyber Crime Reporting Portal, procedure for filing a complaint
  (accessed October 2025).
- Digital Personal Data Protection Act, 2023 — data-principal rights and grievance redressal
  (accessed October 2025).

---

**Disclaimer.** This write-up describes a single documented instance and is published for
professional education. All personal and institutional identifiers have been removed or replaced
with synthetic values. Findings are limited to the evidence described above; nothing here should be
read as an allegation against any named or unnamed party.
