# VRINDAVAN — Phase 0.5 Master Validation

# **CURRENT DECISION: NO-GO FOR SHOPIFY IMPLEMENTATION**

Date: 2026-10-08. No store, theme, apps, accounts, purchases or messages were created or sent in this phase. Nothing here is a supplier quote, a courier rate, a tax ruling or a gateway commitment.
Status vocabulary: **VERIFIED · PARTIAL · UNVERIFIED · BLOCKED · ASSUMPTION** (plus OPEN = not started).

---
## 1. Master dashboard
| Gate | Current Status | Required Evidence | Owner | Next Action | Blocking? |
|---|---|---|---|---|---|
| Trademark | **BLOCKED** | Official IP India search report (OTP + captcha) + attorney view | Me | Run the search protocol in Phase 0.4 §2; save screenshots | YES |
| Supplier | **PARTIAL** (outreach **BLOCKED**) | Written supplier terms: single-order dispatch, blind shipping, packing, damage replacement, GSTIN verified | Me | Send Message A (see `VRINDAVAN_Stage1_Outreach_Final.md`) | YES |
| GST/HSN | **PARTIAL** (rates read in notification text; classification OPEN) | CA confirmation per material | Me + CA | Submit `VRINDAVAN_CA_GST_Questionnaire.md` | YES |
| Courier | **OPEN** (reported ranges only) | Actual rate card by slab/lane, COD, RTO | Me | Send `VRINDAVAN_Courier_Rate_Request.md` | YES |
| Payment | **PARTIAL** (PayU docs read; commercial terms unknown) | Written PayU answers (UPI, COD, login/guest checkout, settlement, KYC) | Me | Send questions in `VRINDAVAN_Payment_Gateway_Validation.md` | YES |
| Product Quality | **OPEN / BLOCKED** (no samples) | Physical samples scoring ≥ 80/100 with no hard fails | Me | Order samples after supplier qualification | YES |
| Economics | **PARTIAL** (model + supplier-cost ceilings; no real inputs) | Actual supplier + shipping data | Me → Claude | Return quotes/rates; I recalculate | YES |
| Brand | **PARTIAL** (direction provisionally accepted; ownership/trademark unverified) | Logo ownership/designer agreement, trademark risk, asset licences | Me | Complete `VRINDAVAN_Brand_Legal_Checklist.md` | YES |
Statuses change only when evidence exists. None is VERIFIED; none is FAILED.

---
## 2. What is preserved from earlier phases (nothing silently overwritten)
| Earlier finding | Source | Status in 0.5 |
|---|---|---|
| Quiet Mandir direction, palette/type rules | v0.3 | **Kept, provisional**; not redesigned |
| GST 18% assumption (v0.1) | v0.1 | **Superseded** by notification text read in 0.4; planning treatment: brass 5%, resin/composite 18% conservative, marble deity 0%/5% — **NOT CONFIRMED** |
| Gateway fees (PayU/Razorpay 2% + 18% GST on fee) | v0.4 | Kept (official pages); UPI MDR still unknown |
| Free shipping ≥ ₹1,499 + ₹49 COD fee + heavy embed | v0.3/0.4 | **Kept as an unlocked hypothesis** |
| 8-SKU pilot (v0.3/0.4) | v0.3/0.4 | **Revised** into 3 Core / 2 Backup / 3 Experimental (§5). Dropped: the ₹999 brass Ganesha (below the shipping threshold, weak CAC) and the separate ₹7,999 SKU 4b (its economics remain in the price sweep). Added: C3 Seated Ganesha 5–6 in at ₹1,499. |
| "No 7-day / free shipping everywhere" promise rule | v0.3/0.4 | Kept (see Claim Evidence Register) |
| Supplier tracker (24 leads) | v0.4 | Kept; now scored and tiered |
| Trademark lead "WAVES OF VRINDAVAN" (class 35/41/43) | v0.3/0.4 | Kept — aggregator-only, not evidence |
| Emblem Krishna-specific; wordmark-first logo option B | v0.3/0.4 | Kept |

---
## 3. Supplier qualification (existing 24 leads — no new broad search)
Scoring rule: **unknown = 0.** Scale per criterion: 0 no evidence · 1 weak/indirect (snippet, vague claim, tiny-sample rating) · 2 explicit statement on the supplier's own page/listing · 3 written reply to our enquiry · 4 documented terms (quote/policy/contract) · 5 proven by sample/test. Full scores: `VRINDAVAN_Supplier_Qualification_Matrix.csv`.
**Reality check:** the highest evidence-based total is **11 / 55 (Baapstore)**. No supplier is anywhere near qualified; the scores show "who to ask first", not "who is good".
| Tier | Meaning | Suppliers (score /55) |
|---|---|---|
| **A** (contact first) | best-evidenced identity + relevant catalogue; **not verified** | Baapstore (11, platform; idols not seen) · Harihar Murti Bhandar (6, marble) · Jaipur Marble Emporium (5, marble) · Bemount Creations (5, resin) · Kamal Metals (4, brass) |
| **B** (missing evidence) | relevant lead, evidence thin | AYC Metals (3) · Arham Trades (5) · Icones Moorti Creation (5) · The Stone Studio (3) · Exotic India (2) · Veda Connection (2) · Aakrati, Indian Culture Handicraft, Vedic Vaani, Keshav Enterprises, Craftam, Satyam Gifts, Rati/P&R, Moorti India group (1 each, snippet only) |
| **C** (reject unless new evidence) | | GlowRoad (2; status conflicting) · Keshav Arts (4; rating 2.9) · Miraya (1; MOQ 500) |
**Gate thresholds I will apply when replies arrive:**
- *Eligible for a sample order:* written reply (score 3) on dropship/blind-ship, replacement and GSTIN, **and** GSTIN verified on the GST portal, **and** total ≥ 25/55.
- *Eligible for the pilot:* sample scores ≥ 80/100 (see Sample Test Protocol), packaging/shipping test with **zero** damage, written damage-replacement terms, total ≥ 40/55.
- Brass coverage matters most (brand-core Krishna + the economics); at least one brass supplier and one backup should pass before any marble/resin route is pursued.

---
## 4. Documents produced
1 this file · 2 `VRINDAVAN_Supplier_Qualification_Matrix.csv` · 3 `VRINDAVAN_Stage1_Outreach_Final.md` · 4 `VRINDAVAN_CA_GST_Questionnaire.md` · 5 `VRINDAVAN_Courier_Rate_Request.md` · 6 `VRINDAVAN_Courier_Rate_Comparison.csv` · 7 `VRINDAVAN_Payment_Gateway_Validation.md` · 8 `VRINDAVAN_Pilot_SKU_Matrix.csv` · 9 `VRINDAVAN_Sample_Test_Protocol.md` · 10 `VRINDAVAN_Claim_Evidence_Register.md` · 11 `VRINDAVAN_Brand_Legal_Checklist.md` · 12 `VRINDAVAN_My_Actions.md`

---
## 5. Pilot SKU selection (3 Core · 2 Backup · 3 Experimental)
Supplier prices are **UNKNOWN**; "placeholder cost" = 42% of selling price and is **not a quote**. Every number is a model output; every dimension/weight is a target. Full columns: `VRINDAVAN_Pilot_SKU_Matrix.csv`.
Selection logic: not by looks — by what each SKU *tests* and whether its economics can plausibly pass. Brass first (brand-core Krishna, best ceiling %, least GST ambiguity, moderate fragility); resin/composite only as backup/experiment because the GST treatment is unresolved (18% reading) and the cost ceiling is lower.
| ID | Role | Product | Material | Billing wt (kg) | Price | Why selected | Max supplier cost (gate) |
|---|---|---|---|---|---|---|---|
| C1 | Core | Radha-Krishna 9–10 in | Brass | 3.0 | ₹2,999 | Brand-core Krishna, core price point, detail fragility | ₹1,372 (45.7%) |
| C2 | Core | Lakshmi–Ganesha pair 6–7 in | Brass | 2.0 | ₹1,999 | Festival/gift demand, pair = AOV, mid weight | ₹870 (43.5%) |
| C3 | Core | Seated Ganesha 5–6 in | Brass | 1.5 | ₹1,499 | Highest-demand deity, entry price; tests whether ₹1,499 can ever pass | ₹612 (40.8%) |
| B1 | Backup | Hanuman (or Shiva) 12 in | Brass | 6.0 | ₹4,999 | Heavy-parcel test; non-Krishna coverage | ₹2,214 (44.3%) |
| B2 | Backup | Ganesha 8 in | Polyresin / cold-cast | 1.5 | ₹1,499 | Cheaper-material benchmark; only if CA confirms favourable GST | ₹505 (33.7%) |
| E1 | Experimental | Krishna with flute 10 in | Resin / cold-cast | 2.0 | ₹1,999 | Fragile-shape packaging stress test | ₹721 (36.1%) |
| E2 | Experimental | Ganesha/Lakshmi 9–12 in | Marble-composite | 5.0 | ₹4,999 | Heavy white-stone look; material-honesty + classification risk | ₹2,004 (40.1%) |
| E3 | Experimental | Radha-Krishna 12 in | Real marble | 13.0 | ₹12,000 | High-AOV, freight/breakage, possible exempt-deity status | ₹5,670 (47.2%) at 5% GST; ₹6,059 if exempt |
**Core products are not "approved"** — they are the three that could become launch products *if* quotes land under the ceilings and samples pass.

---
## 6. Unit economics engine
### 6.1 Variables (all editable; nothing locked)
**Verified inputs:** Shopify Payments unavailable in India; PayU/Razorpay 2% + 18% GST on the fee (official pages); GST notification entries (Phase 0.4 §3.2, copies of notification text).
**Reported ⚠:** Shopify extra 2% on third-party gateways; courier zone ranges and COD/RTO rules; COD RTO 20–40%.
**Assumptions:** chargeable weight = actual × 1.3 rounded up to 0.5 kg; freight ₹55 (≤0.5 kg), ₹110 (≤1 kg), +₹60/extra kg, +12% fuel; **low shipping = ×0.7, base = ×1.0, high = ×1.5**; packaging ₹25–110; prepaid fee 4.36% (2% + 18% GST + Shopify 2%); COD cost = max(₹40, 1.75%); COD RTO 30% with cost = 1.9 × freight + packaging; damage/replacement 5% of delivered orders at full replacement cost; ₹79 customer-paid shipping below ₹1,499; placeholder supplier cost 42%; GST 5%.
### 6.2 Line items at base shipping (per order placed, ₹)
| Price | Revenue incl. GST | **GST impact** | Revenue ex-GST (+net cust. shipping) | Placeholder supplier cost | Packaging | Shipping | Payment fee (prepaid) | COD cost | Exp. RTO cost (COD) | Replace reserve |
|---|---|---|---|---|---|---|---|---|---|---|
| ₹999 | 999 | −48 | 1,018 | 420 | 25 | 123 | 44 | 40 | 78 | 28 |
| ₹1,499 | 1,499 | −71 | 1,428 | 630 | 30 | 157 | 65 | 40 | 98 | 41 |
| ₹1,999 | 1,999 | −95 | 1,904 | 840 | 35 | 190 | 87 | 40 | 119 | 53 |
| ₹2,999 | 2,999 | −143 | 2,856 | 1,260 | 45 | 258 | 131 | 52 | 161 | 78 |
| ₹4,999 | 4,999 | −238 | 4,761 | 2,100 | 70 | 392 | 218 | 87 | 244 | 128 |
| ₹7,999 | 7,999 | −381 | 7,618 | 3,360 | 110 | 594 | 349 | 140 | 372 | 203 |
### 6.3 Contribution before advertising — low / base / high shipping
| Price | Ship low / base / high | **Prepaid** low / base / high | **COD** low / base / high | Blended (base) = **max CAC** | **Target CAC** (50%) | Prepaid after target CAC | COD after target CAC | Max supplier cost for gate |
|---|---|---|---|---|---|---|---|---|
| ₹999 | 86 / 123 / 185 | 418 / 379 / 314 | 238 / 190 / 109 | **284** | 142 | 237 | 48 | ₹401 (40.1%) |
| ₹1,499 | 110 / 157 / 235 | 554 / 505 / 423 | 334 / 273 / 171 | **389** | 194 | 310 | 78 | ₹612 (40.8%) |
| ₹1,999 | 133 / 190 / 286 | 759 / 699 / 598 | 478 / 403 / 278 | **551** | 276 | 423 | 128 | ₹870 (43.5%) |
| ₹2,999 | 180 / 258 / 386 | 1,167 / 1,085 / 950 | 755 / 654 / 486 | **869** | 435 | 650 | 219 | ₹1,372 (45.7%) |
| ₹4,999 | 274 / 392 / 588 | 1,977 / 1,853 / 1,648 | 1,298 / 1,144 / 888 | **1,499** | 749 | 1,104 | 395 | ₹2,361 (47.2%) |
| ₹7,999 | 416 / 594 / 890 | 3,189 / 3,003 / 2,692 | 2,109 / 1,876 / 1,490 | **2,439** | 1,220 | 1,783 | 657 | ₹3,840 (48.0%) |
(At the placeholder 42% cost. If real cost is 50% / 55% the blended falls to ₹213/169 at ₹999, ₹282/215 at ₹1,499, ₹408/319 at ₹1,999, ₹655/521 at ₹2,999, ₹1,142/919 at ₹4,999, ₹1,868/1,511 at ₹7,999.) Max supplier cost = highest cost still giving prepaid ≥ 30% and COD ≥ 20% of ex-GST revenue.
### 6.4 Which price balances attractiveness, contribution and conversion?
- **Conversion probability is UNKNOWN** — no traffic or test data exists, so I will not fabricate it. What can be said:
  - **Contribution:** a paid-acquisition CAC target is only comfortable from ≈ ₹1,999 upward (target CAC ₹276+); ₹999 and ₹1,499 leave ₹48–78 after target CAC on COD orders — they behave as add-on/gift products, not acquisition products. Higher prices always show more rupees but also higher RTO/damage/freight exposure and lower expected conversion.
  - **Attractiveness (observed in this project's competitor research, VERIFIED observations):** mainstream brass/idol listings I opened cluster around ₹1,000–5,000 (Veda Connection best-sellers ₹999–3,999; Vedansh ₹1,250–5,950; Jaypore brass idol ₹2,201 after 65% off a ₹6,290 list; Satvik small idols ₹419; StatueStudio best-sellers ₹3,000–25,000; eCraft mostly ₹395–995).
  - **Hypothesis to test (not a conclusion):** **₹1,999–₹2,999 is the most likely balance** for core brass SKUs; ₹1,499 only if supplier cost ≤ ₹612; ₹4,999+ as showpieces. Do not push the highest price.
- Test design after launch: price-ladder A/B on the same SKU family; measure CVR, COD share, RTO, refunds.

---
## 7. Objective launch gate (Phase 1 / Shopify implementation)
All **ten** must be met. Any unresolved item = **NO-GO**. No exceptions for design appeal.
| # | Mandatory condition | Pass test | Status now |
|---|---|---|---|
| 1 | ≥ 1 supplier verified for actual fulfilment | written terms (dropship, blind ship, packing, replacement) + GSTIN verified + sample shipped | **UNVERIFIED** |
| 2 | ≥ 3 products commercially viable | quotes ≤ ceilings; blended contribution ≥ target at real freight | **UNVERIFIED** (no quotes) |
| 3 | Supplier pricing documented | written quote with validity date | **UNVERIFIED** |
| 4 | Shipping economics documented | rate card by slab/lane incl. COD/RTO | **UNVERIFIED** |
| 5 | GST/HSN sufficiently confirmed | CA memo for each pilot material | **PARTIAL** |
| 6 | Sample quality passes | ≥ 80/100, no hard fail | **UNVERIFIED** (no samples) |
| 7 | Packaging/shipping test passes | 0 damaged parcels across the test set | **UNVERIFIED** |
| 8 | Payment path confirmed | PayU (or fallback) written terms | **PARTIAL** |
| 9 | Trademark risk assessed | search report + attorney view | **BLOCKED** |
| 10 | Delivery/returns promise supportable | claims in the Claim Evidence Register all evidenced | **UNVERIFIED** |
**Decision rule:** count of VERIFIED mandatory items must be 10/10. Currently **0/10 VERIFIED** → **NO-GO**.

---
## 8. Risks that could kill the model (keep visible)
1. No supplier accepts blind single-order dispatch at acceptable terms. 2. Brass/marble breakage and freight exceed the model. 3. Resin/composite GST resolves to 18% and removes those SKUs. 4. COD RTO runs 30%+. 5. PayU's COD flow forces login/OTP and cuts conversion. 6. Trademark conflict on VRINDAVAN in class 35. 7. Logo ownership/provenance unclear. 8. Delivery times in practice exceed any promise.

**NEXT DECISION POINT: AFTER EXTERNAL VALIDATION EVIDENCE IS RETURNED**
