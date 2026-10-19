# VRINDAVAN — Courier / Aggregator Rate Request
Status: **NOT SENT.** Rates below are **UNKNOWN** — nothing here is a rate. You request them (account sign-up, sales contact, OTP and KYC are yours). Record answers in `VRINDAVAN_Courier_Rate_Comparison.csv` (42 rows = 7 couriers × 6 weight slabs).

## Who to ask
Shiprocket (aggregator) · Delhivery (direct rate card) · Blue Dart · DTDC · Amazon Shipping (**first confirm it accepts non-Amazon/Shopify orders**) · India Post Speed Post (remote PINs; confirm parcel COD) · any other courier your aggregator offers. Previously researched figures were blog-level only (Phase 0.3–0.4) and must be replaced by real quotes.

## Lanes (adjust origin to the actual supplier city once known)
L1 Moradabad → Delhi · L2 Jaipur → Mumbai · L3 Jaipur → Bengaluru · L4 Moradabad → Kolkata · L5 → Guwahati (NE/remote) · L6 → Leh or Srinagar (remote/hill)
Also ask for a **PIN-code serviceability list/API method** and a sample of **ODA (out-of-delivery-area) PINs**.

## Request message (WhatsApp / email / portal)
> Hello, I'm launching a small India-wide online store for devotional idols and décor (fragile, 0.4–13 kg packed, declared value ₹1,000–15,000), with prepaid and COD orders, pick-ups from [city]. Please send your **current rate card in writing (excl. GST)** for the lanes and weight slabs below:
> **Weight slabs:** 0–500 g · 500 g–1 kg · 1–2 kg · 2–3 kg · 3–5 kg · 5–10 kg (and per additional kg beyond 10 kg)
> **Lanes:** [L1–L6 above]
> For each, please state: (1) **prepaid forward charge**; (2) **COD fee** (flat and % of order value, and the minimum); (3) **RTO charge**; (4) **reverse pickup** charge; (5) **damage/loss claim** policy, liability cap, insurance/"protect" charge, and claim timeline/documents; (6) **volumetric weight** formula/divisor and weight-dispute handling; (7) **ODA/remote-area** surcharges and which PINs; (8) **fuel surcharge**; (9) GST applicable on freight; (10) **minimum charges** (minimum chargeable weight/freight); (11) **pickup charges** and pick-up SLA; (12) **expected transit time** (metro / tier-2 / remote); (13) serviceable PIN coverage and how to check it; (14) **COD remittance cycle** and fees for early remittance; (15) NDR (non-delivery report) rules and attempts; (16) tracking/webhook and Shopify integration; (17) any onboarding fee or minimum volume. Please also confirm the validity period of the quote. Thank you — [Name, phone]

## How to read the quotes (checklist)
- Compare **chargeable weight** = max(actual, volumetric). Example: a 30 × 20 × 20 cm packed box with a divisor of 5000 → 2.4 kg volumetric; if actual is 1.2 kg the courier bills 2.4 kg. Ask for the exact divisor.
- Add: base + fuel % + COD + ODA + insurance + GST. Convert to **₹ per parcel** and **% of price**.
- RTO: record it as a % of forward freight or flat; our model assumed 80–100% of forward freight (reported) — confirm.
- Damage claims: note the liability cap versus parcel value (a ₹12,000 marble piece with a ₹2,000 cap is a real risk).
- Red flags: no written claim process; "weight discrepancy" fees without photos; COD remittance > 7 days; refusal to quote fragile/heavy.

## What I need back
The filled CSV (or screenshots/PDFs of quotes) with quote date, source, and validity. I will recompute freight in the Pilot SKU Matrix and rerun Gate 4. Until then **free shipping and any delivery time stay unlocked.**
