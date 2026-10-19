# VRINDAVAN — Phase 0.4 Validation Execution
Date: 2026-10-08 · No Shopify store, theme, Liquid, apps, domain, gateway or supplier connection was created. No supplier message was sent.
Companion files: `VRINDAVAN_Supplier_Evidence_Tracker.csv` (24 suppliers × 24 fields) · `VRINDAVAN_Stage1_Outreach_Ready_To_Send.md` (messages, not sent).

**Evidence labels:** VERIFIED = read or seen this session · REPORTED = secondary source only · ASSUMPTION = my placeholder, never a supplier quote · UNKNOWN = must be collected · LEGAL REVIEW REQUIRED = interpretation needed from a professional.

---
## 1. Executive decision
**NO-GO for Phase 1 (Shopify architecture/build).** None of the eight gates is VERIFIED. Three actions could not be executed from this environment and are BLOCKED on you: the official trademark search (OTP login + captcha), supplier outreach (no authorised channel; you must send), and getting real courier/gateway rate cards (need accounts/sales contact).
**What moved forward this phase:**
- GST: I read the actual notification text and found that **idols of wood, stone (incl. marble) and non-precious metals are in the 5% schedule, "deities made of stone, marble or wood" are in the exemption notification, and "other articles of plastics" sit in the 18% schedule** — which makes resin idols a real tax risk.
- Economics: rebuilt with product-specific GST and shown as **supplier-cost ceilings**, so you can judge any quote instantly.
- Payment: PayU's official docs read in full; the unresolved commercial questions are listed; a new conversion risk surfaced (PayU's COD/login flow requires disabling guest checkout).
**Conditional go-ahead:** continue external validation (§8 actions). Re-run this dashboard when replies, samples and rate cards arrive.

---
## 2. Trademark — Gate status: **BLOCKED**
### What I verified (VERIFIED, screenshots taken)
- The official IP India Trade Marks public search (`tmrsearch.ipindia.gov.in/tmrpublicsearch/`) loads and requires **"Login with OTP"** — an email or 10-digit mobile number, a math captcha, then an OTP sent to that identity. Other visible buttons: *Class Details, Well Known Marks, Vienna Code Classification, International Non-Proprietary Names, Help, AI based Trademark Search*. The separate *E-Register* page only shows status for a known application number.
- I cannot complete this: it needs your personal email/phone to receive the OTP, and completing captchas is not something I will do. **No trademark conclusion is drawn from aggregator websites.**
### Exact search protocol (you run it; ~30 minutes)
| Step | Search | Classes | Record |
|---|---|---|---|
| 1 | Word mark **VRINDAVAN** | all classes first (overview), then 35, 6, 19, 20, 21, 14, 11, 4 | every hit |
| 2 | Variants: **VRINDABAN, BRINDAVAN, BRINDABAN, VRUNDAVAN, VRUNDABAN, VRINDAVANA, VRINDHAVAN, VRINDAWAN, BRINDAWAN, VRINDA** | 35, 6, 19, 20, 21, 14 | hits |
| 3 | Marks *containing* Vrindavan (portal's "contains"/similar options if offered) e.g. "… OF VRINDAVAN" | 35 first | hits |
| 4 | Device search via **Vienna Code Classification**: peacock feather/bird, flute/musical instrument, temple/dome/arch, lotus | 35, 6, 19, 20, 21, 14 | hits with images |
| 5 | Screenshot each results page + each relevant record (status, applicant, goods/services, dates) | | evidence folder |
Classes (Nice; **attorney to confirm**): 35 online retail (core); 6 statues/figurines of common metal; 19 statues of stone/marble; 20 statues of wood/wax/plaster/plastic (resin); 21 ornaments of porcelain/terracotta/glass; 14 precious-metal statuettes (if ever); 11/4 lamps/candles if added.
### Record table (fill in)
| Search term | Class | Mark found | Application/Reg. no. | Applicant | Status | Filing date | Goods/services | Conflict view | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| *(empty — not run)* | | | | | | | | **LEGAL REVIEW REQUIRED** | |
### Known lead (NOT official evidence — aggregator `registerkaro.in`, indexed from IP India, may lag)
- **WAVES OF VRINDAVAN**, word + device marks, **Classes 35, 41, 43**, filed 2 Aug 2026, applicant a Jalandhar partnership (apps 7900780–7900785). **Class 35 overlaps the class we would file for online retail.** Whether "WAVES OF" distinguishes it from VRINDAVAN, and whether pending marks block us = **LEGAL REVIEW REQUIRED**. Treat as a *potential conflict to investigate*, not a finding.
### Logo conflict assessment — **BLOCKED / LEGAL REVIEW REQUIRED**
- I cannot compare the emblem/wordmark with the register without the device (Vienna) search. Elements to check: peacock feather + flute, temple domes with flag, lotus, circular emblem; wordmark "VRINDAVAN".
- **Provenance:** I can't tell how the logo files were produced. If an AI image generator was used, confirm commercial-use terms, originality and registrability, and consider a vector redraw. **LEGAL REVIEW REQUIRED.**
- Place-name distinctiveness ("Vrindavan" is a place) and crowded-register risk = **LEGAL REVIEW REQUIRED**.
**Decision:** Brand risk is NOT assessed. Do not spend on brand assets, packaging or domains until the search report and an IP attorney's view exist.

---
## 3. GST / HSN — Gate status: **PARTIAL** (rates read; applicability needs CA)
### 3.1 What I could read (and the source quality)
- **Source A — IGST rate schedule:** *Notification 9/2025-Integrated Tax (Rate) dated 17-9-2025, [UPDATED, corrected 18-9-2025]* — the PDF at `courier.cbic.gov.in/ECCS/advisory/2025/…` is an **ICAI GST Committee printed copy** of the notification. I extracted the text locally and read the entries. It is the inter-state (IGST) version; the central-tax (intra-state) version mirrors it at half the rate but **I did not read it**.
- **Source B — exemption notification:** *Notification 10/2025-Central Tax (Rate), G.S.R. 660(E), 17 Sep 2025* — a copy of the Gazette PDF hosted on `taxo.online` (third-party host; text reads as the Gazette). It exempts **intra-State** supplies of goods listed in its schedule. The IGST exemption counterpart (10/2025-Integrated Tax (Rate)) **was not read** (only described by a law-firm site).
- I could **not** open these from `cbic-gst.gov.in` / `taxinformation.cbic.gov.in` (page redirect + TLS certificate error / 404). CBIC-hosted originals should be re-checked by the CA.
### 3.2 Verified entries (text read)
| Item | Notification / entry | What it says | Rate |
|---|---|---|---|
| Idols of wood, stone [including marble] and metals [other than precious metals] | 9/2025-IT(R), **Schedule I, S.No. 293** (Ch. 44, 68, 83) | listed | **5% IGST** |
| Wooden statuettes and ornaments (HSN 4420) | Schedule I, S.No. 305 | listed | 5% |
| Statues, statuettes, … ornamental goods essentially of stone (HSN 6802) | Schedule I, S.No. 401 | listed | 5% |
| Bells, gongs; **statuettes and other ornaments of base metal** (HSN 8306) | Schedule I, S.No. 420 | listed | 5% |
| Agarbatti, lobhan, dhoop batti, dhoop, sambrani | Schedule I | listed | 5% |
| **Other articles of copper** (HSN 7419; excludes brass kerosene pressure stove) | **Schedule II**, S.No. 321 | listed | **18%** |
| **Other articles of plastics and articles of other materials of headings 3901 to 3914** [other than bangles, plastic beads, feeding bottles] (HSN 3926) | **Schedule II**, S.No. 127 | listed | **18%** |
| **Deities made of stone, marble or wood** (Ch. 44 or 68) | 10/2025-**CT(R)**, S.No. 124 | exempt (intra-State central tax) | **Exempt (CGST)** |
| Idols made of clay (Ch. 69) | 10/2025-CT(R), S.No. 152 | exempt | Exempt (out of scope) |
| Goods not in the other schedules | 9/2025-IT(R) S.No. 639 | default | per Schedule III/other — not read |
**Not found in the exemption list:** metal deities (brass etc.), resin/plastic deities, marble/stone **decorative** figures (not described as deities).
### 3.3 Product-category matrix (what is VERIFIED vs what needs the CA)
| Category | VERIFIED from text | Still REPORTED/unknown | Needs CA — **do not lock** |
|---|---|---|---|
| **Brass religious idols** | Metal idols (non-precious) in 5% Schedule I (S.No. 293) and base-metal statuettes (S.No. 420) | Older sources say 12%/18% — outdated by this text; secondary sources cite a handicraft concession (13/2025-CT(R)) I did not read | Idol (293) vs statuette (8306) invoice description; any condition (e.g., handicraft/hand-made); **is brass-only décor (lamps, thalis) 7419 at 18% or 8306/7418?** |
| **Resin / polyresin / cold-cast idols** | No entry for resin idols; plastics fall into S.No. 127 (3926) at **18%**; the idol entry names only wood, stone, metals | I found no authority on cold-cast resin/metal-powder composites | **LEGAL REVIEW REQUIRED:** HSN for resin deities (3926 40 statuettes?) — assume 18% until confirmed |
| **Marble idols** | 5% as "idols of stone incl. marble" (S.No. 293) / 6802 (S.No. 401); **exempt (CGST)** if "deities made of stone, marble or wood" (S.No. 124) | Rajasthan AAR (30 Jul 2026, via taxscan) says exemption covers **actual deities**, not decorative statues; IGST exemption text not read | Is a murti sold online an "actual deity"? Inter-state exemption; ITC reversal on exempt supplies |
| **Wooden idols** | Wooden deities exempt (S.No. 124); other wooden statuettes/ornaments 5% (S.No. 305) | — | Deity vs ornament |
| **Decorative statues** | Stone 5% (401); base-metal 5% (420); wood 5% (305); plastic 18% (127) | — | Dual-use items (deity-looking décor) |
| **Products actually intended for worship** | Agarbatti etc. 5% | Pooja thalis, diyas, bells: not fully researched (bells under 8306 at 5%) | HSN for each accessory |
| **Marble-powder / composite "marble"** | no entry | — | **LEGAL REVIEW REQUIRED:** 6802 vs 3926 vs artificial-stone heading |
### 3.4 Planning treatment in the economics (assumptions, NOT conclusions)
Brass 5% · marble deity 0% best case / 5% safe case · resin and marble-composite **18% (conservative)**. If the CA confirms 5%, resin contribution at ₹1,499 rises from ≈₹348 to ≈₹505 (prepaid, 42% cost).
### 3.5 Exact questions for the CA (product-level)
| SKU | Product | Candidate treatment | Question |
|---|---|---|---|
| 1–4 | Brass Ganesha / Lakshmi-Ganesha / Radha-Krishna / Hanuman or Shiva | S.No. 293 or 420 → 5% | Which entry and HSN go on the invoice? Is 5% unconditional for idols of metal inter- and intra-state? Any "hand-made/handicraft" condition or supplier declaration needed? |
| 5–6 | Polyresin / cold-cast Ganesha, Krishna | 3926 at 18%? | HSN and rate for resin deities; does 3926 apply or does any idol/statuette entry? |
| 7 | Marble-composite Ganesha/Lakshmi | 6802 5% vs 3926 18% vs other | Classification of marble-dust + resin composites |
| 8 | Real-marble Radha-Krishna | exempt (124) vs 5% (293/401) | Does a deity sold to consumers qualify for exemption? Inter-state coverage (IGST 10/2025)? ITC reversal on inputs/freight? Invoice wording |
| all | Mixed baskets | — | Invoicing exempt + taxable items together; credit notes for returns |
General: (1) Is registration needed from day one for a dropshipper selling inter-state via own site? (Thresholds and inter-state rules.) (2) Dropship invoicing: supplier bills me, ships to my customer — valid bill-to/ship-to? place of supply? (3) ITC if supplier unregistered/composition. (4) TCS/TDS implications for gateway/courier settlements. (5) GST on COD fees and shipping charges; "free shipping" value of supply. (6) COD remittance accounting. (7) Composition scheme eligibility. (8) E-way bill triggers for heavy marble. (9) Entity choice vs trademark/brand ownership. (10) Legal Metrology declarations and who is "packer" in dropship. (11) E-Commerce Rules disclosures; DPDP notices.
**Decision:** No GST assumption is locked. Economics use the conservative treatment above until the CA answers.

---
## 4. Supplier validation — Gate status: **PARTIAL** (outreach **BLOCKED**)
- **Stage 1 outreach: BLOCKED — not sent.** Exact messages (WhatsApp EN/Hinglish, IndiaMART, Stage-2 email) are in `VRINDAVAN_Stage1_Outreach_Ready_To_Send.md`. I did not send anything and no supplier has replied.
- Evidence table: see the CSV (every field is "NOT STATED / UNKNOWN" unless the page said it). Summary:
| Supplier | Category | Dropship explicit? | White-label / blind? | COD? | MOQ | Price | Ship cost | Dispatch | Tracking | Returns | Damage replace | API/feed | GST invoice | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Baapstore** | platform (idols not seen) | **Stated** | **Stated** (brand-name dispatch) | **Stated** (no terms) | not stated | subscription-gated (Pro ₹24,999/yr) | flat ₹69 or ₹89/product (inconsistent) | not stated | handled by platform (stated) | ₹99/product, 5 days | wrong/defective free | not stated | not stated | own site | Medium (model) / Low (idols) |
| Kamal Metals | brass | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | IndiaMART; GST-verified badge | Medium identity / Low fit |
| AYC Metals | brass | not stated | … | … | … | … | … | … | … | … | … | … | … | IndiaMART | Low–Med |
| Arham Trades | polyresin | not stated | … | … | … | … | … | … | … | … | … | … | … | 4.1/5 (13), 23% 1-star | Low–Med |
| Bemount | polyresin | not stated | … | … | … | … | … | … | … | … | … | … | … | 5.0 from 3 reviews | Low–Med |
| Harihar Murti Bhandar | marble | not stated | custom carving only | not stated | not stated | not stated | crate packaging "across India" (own claim) | not stated | … | … | … | … | … | manufacturer; GST reg. 2025 | Medium (marble) |
| Jaipur Marble Emporium | marble | not stated | custom sizes | not stated | … | … | "supply everywhere" | … | … | … | … | … | … | 4.8 (35) | Medium |
| Icones Moorti | marble | not stated | … | … | … | listings ₹10k–37k/piece | "Pan India" claim | … | … | … | … | … | … | 3.9 | Low–Med |
| The Stone Studio | stone | not stated | not stated | not stated | not stated | negotiated | not stated | … | … | … | … | … | … | wholesale page | Low–Med |
(Other 15 rows — snippet-only leads, Exotic India, Veda Connection, GlowRoad, and two rejects — are in the CSV.)
**Rule applied:** a generic "dropshipping available" or "wholesale" statement is never recorded as dropship, white-label, COD or India-wide capability. **Zero suppliers are VERIFIED.** Baapstore is PARTIALLY VERIFIED as a *model* only.
**Decision:** Gate 1 cannot be called VERIFIED until at least one supplier confirms in writing: single-order dispatch, blind shipping, packing method, damage replacement and GSTIN (verified on the GST portal).

---
## 5. Pilot SKU table
Supplier prices are **UNKNOWN (variable)**. Dimensions/weights are design targets (ASSUMPTION). Shipping = model (§6). GST per §3.4. "Max supplier cost" = the highest ex-GST-treated supplier price per unit at which **prepaid contribution ≥ 30% and COD ≥ 20% of ex-GST revenue** (Gate 3 thresholds). Contribution is before advertising.
| # | SKU | Material | Target size / weight | Candidate route | Supplier price | GST used | Target price | Ship (model, chargeable kg) | Fragility | **Max supplier cost** (₹ and % of price) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Seated Ganesha 3–4 in | Brass | ~9 cm / 0.4 kg | Moradabad | **UNKNOWN** | 5% | ₹999 (₹79 shipping charged) | ₹123 (1.0) | Low | **₹401 (40.1%)** |
| 2 | Lakshmi–Ganesha pair 6–7 in | Brass | ~16 cm / 1.2 kg | Moradabad | UNKNOWN | 5% | ₹1,999 | ₹190 (2.0) | Medium | **₹870 (43.5%)** |
| 3 | Radha-Krishna 9–10 in | Brass | ~24 cm / 2.0 kg | Moradabad | UNKNOWN | 5% | ₹2,999 | ₹258 (3.0) | Med–High | **₹1,372 (45.7%)** |
| 4 | Hanuman or Shiva 12 in | Brass | ~30 cm / 4.5 kg | Moradabad/Jaipur | UNKNOWN | 5% | ₹4,999 | ₹459 (6.0) | Medium; heavy | **₹2,214 (44.3%)** |
| 4b | Same family, large 15 in | Brass | ~38 cm / 6 kg | same | UNKNOWN | 5% | ₹7,999 | ₹594 (8.0) | Medium; very heavy | **₹3,840 (48.0%)** |
| 5 | Ganesha 8 in | Polyresin / cold-cast | ~20 cm / 0.8 kg | Jaipur / Loni | UNKNOWN | **18% (conservative)** | ₹1,499 | ₹157 (1.5) | Medium (paint) | **₹505 (33.7%)** |
| 6 | Krishna with flute 10 in | Resin / cold-cast | ~25 cm / 1.2 kg | resin makers | UNKNOWN | 18% | ₹1,999 | ₹190 (2.0) | **High** | **₹721 (36.1%)** |
| 7 | Ganesha/Lakshmi 9–12 in | Marble-composite | ~28 cm / 3.5 kg | Jaipur/Mumbai | UNKNOWN | 18% | ₹4,999 | ₹392 (5.0) | Med; heavy | **₹2,004 (40.1%)** |
| 8 | Radha-Krishna 12 in (optional premium) | Real marble | ~30 cm / 10 kg | Jaipur marble | UNKNOWN (Icones' own listings: ₹10k–37k per piece) | 0% best / 5% safe | ₹12,000 | ₹930 (13.0) | **High**; very heavy | **₹6,059 (50.5%)** at 0% GST |
Why each: 1 tests the below-₹1,499 shipping rule and lightest parcel; 2 festival-pair AOV; 3 brand-name Krishna, detail fragility, core price; 4/4b heavy-parcel economics; 5 cheaper-material benchmark and the resin-GST risk; 6 fragile-shape packaging test; 7 composite honesty + classification risk; 8 high-AOV, exemption and freight test (run as quote/photo first if the sample cost is prohibitive).
**Reading the ceilings:** brass SKUs can only work if the supplier's landed price is roughly ≤ 40–48% of the selling price; resin SKUs only if ≤ ~34–36% at 18% GST (and typically need higher selling prices). Any quote above the ceiling fails Gate 3 for that SKU.

---
## 6. Unit economics (model; supplier costs shown as variable)
### Verified facts used
Shopify Payments is not available in India (Shopify Help, fetched). PayU 2% + 18% GST on the fee for cards/NB/wallets (PayU pricing, fetched). Razorpay 2% + 18% GST, ₹0 setup/AMC/refund fee (Razorpay pricing, fetched). Baapstore flat ₹69/₹89 shipping and ₹99 returns (fetched). GST entries in §3.2.
### Reported (⚠) inputs
Shopify extra 2% on third-party gateways (Basic); Delhivery 1 kg zone estimates ₹65–320, ₹32/500 g intra-city, fuel 10–18%, COD ₹35–40 or 1.5–2%, RTO 80–100% of forward freight; COD RTO 20–40% (vendor benchmark).
### Assumptions
Chargeable weight = actual × 1.3 rounded up to 0.5 kg; freight ₹55 (≤0.5 kg), ₹110 (≤1 kg), +₹60 per extra kg, +12% fuel; packaging ₹25–110 by size; prepaid fee = 2% + 18% GST + Shopify 2% = 4.36%; COD cost = max(₹40, 1.75% of price); COD RTO 30%, RTO cost = 1.9 × freight + packaging; damage/replacement reserve 5% of delivered orders × (cost + freight + packaging); ₹79 customer-paid shipping below ₹1,499; GST 5%; COD share 50% for blended CAC.
### Six price tiers — contribution before ads (₹, per order placed): prepaid / COD / blended; supplier cost as a variable
| Price | Revenue ex-GST | Ship | Pack | Payment (prepaid) | COD cost | Exp. RTO cost (COD) | Replace reserve @42% | Supplier cost = 35% | = 42% | = 50% | = 55% | **Max supplier cost** (gate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ₹999 | 1,018 (incl. ₹67 net shipping) | 123 | 25 | 44 | 40 | 78 | 28 | 452 / 241 / **347** | 379 / 190 / **284** | 295 / 131 / **213** | 242 / 95 / **169** | ₹401 |
| ₹1,499 | 1,428 | 157 | 30 | 65 | 40 | 98 | 41 | 615 / 350 / **482** | 505 / 273 / **389** | 379 / 185 / **282** | 300 / 129 / **215** | ₹612 |
| ₹1,999 | 1,904 | 190 | 35 | 87 | 40 | 119 | 53 | 846 / 506 / **676** | 699 / 403 / **551** | 531 / 286 / **408** | 426 / 212 / **319** | ₹870 |
| ₹2,999 | 2,856 | 258 | 45 | 131 | 52 | 161 | 78 | 1,305 / 808 / **1,056** | 1,085 / 654 / **869** | 833 / 477 / **655** | 675 / 367 / **521** | ₹1,372 |
| ₹4,999 | 4,761 | 392 | 70 | 218 | 87 | 244 | 128 | 2,221 / 1,401 / **1,811** | 1,853 / 1,144 / **1,499** | 1,433 / 850 / **1,142** | 1,171 / 667 / **919** | ₹2,361 |
| ₹7,999 | 7,618 | 594 | 110 | 349 | 140 | 372 | 203 | 3,591 / 2,288 / **2,939** | 3,003 / 1,876 / **2,439** | 2,331 / 1,406 / **1,868** | 1,911 / 1,112 / **1,511** | ₹3,840 |
**Maximum sustainable CAC** ≈ **50% of the blended figure** (the rest covers software, returns beyond the model, labour, profit). Example at 42% cost: ₹142 / 195 / 276 / 435 / 750 / 1,220 for ₹999 … ₹7,999. At ₹999–1,499 that is below what I would expect paid acquisition to cost (not verified) → those are add-on/gift SKUs.
### 8-SKU contribution grid (prepaid / COD / blended, per order placed)
| SKU | Cost 35% | 42% | 50% | 55% |
|---|---|---|---|---|
| 1 Brass ₹999 | 452 / 241 / 347 | 379 / 190 / 284 | 295 / 131 / 213 | 242 / 95 / 169 |
| 2 Brass ₹1,999 | 846 / 506 / 676 | 699 / 403 / 551 | 531 / 286 / 408 | 426 / 212 / 319 |
| 3 Brass ₹2,999 | 1,305 / 808 / 1,056 | 1,085 / 654 / 869 | 833 / 477 / 655 | 675 / 367 / 521 |
| 4 Brass ₹4,999 (4.5 kg) | 2,129 / 1,293 / 1,711 | 1,762 / 1,036 / 1,399 | 1,342 / 742 / 1,042 | 1,080 / 558 / 819 |
| 4b Brass ₹7,999 | 3,591 / 2,288 / 2,939 | 3,003 / 1,876 / 2,439 | 2,331 / 1,406 / 1,868 | 1,911 / 1,112 / 1,511 |
| 5 Resin ₹1,499 (18% GST) | 458 / 240 / 349 | 348 / 163 / 255 | 222 / 74 / 148 | 143 / 19 / 81 |
| 6 Resin ₹1,999 (18%) | 631 / 354 / 493 | 484 / 251 / 368 | 316 / 134 / 225 | 211 / 60 / 136 |
| 7 Composite ₹4,999 (18%) | 1,696 / 1,034 / 1,365 | 1,329 / 777 / 1,053 | 909 / 483 / 696 | 646 / 299 / 473 |
| 8 Marble ₹12,000 (0% GST) | 5,901 / 3,766 / 4,834 | 5,019 / 3,149 / 4,084 | 4,011 / 2,443 / 3,227 | 3,381 / 2,002 / 2,692 |
### Other sensitivities
COD RTO 20% / 30% / 40% — COD contribution: ₹1,499: 359 / 273 / 187; ₹2,999: 823 / 654 / 484; ₹4,999: 1,424 / 1,144 / 864. GST 18% instead of 5% on a brass SKU at ₹2,999: blended falls from ₹869 to ≈₹602. Freight +50% (if my weight/zone assumption is low) cuts ≈ ₹130–300 from SKUs 3–4b.
**Gate 3 verdict:** cannot be VERIFIED without real supplier cost. The ceilings above are the pass/fail line.

---
## 7. Shipping model — Gate status: **PARTIAL** (policy NOT locked)
- **Evidence status:** no official rate card obtained. Everything is ⚠ REPORTED/ASSUMPTION. Required: rate calculator output from an aggregator account and written courier terms (§8).
- **Shipping cost as % of price (model):** ₹999 12.3% · ₹1,499 10.5% · ₹1,999 9.5% · ₹2,999 8.6% · ₹4,999 7.8% · ₹7,999 7.4% · ₹12,000 7.8%.
### Policy comparison (per order, prepaid contribution at 42% cost)
| Policy | ₹999 | ₹1,499 | Comment |
|---|---|---|---|
| P1: Free shipping on everything | 379 − 67 = **312** | 505 | simplest message; hurts the smallest item most |
| P2: Free ≥ ₹1,499, ₹79 below | **379** | 505 | recommended hypothesis |
| P3: Free on prepaid only; COD pays shipping | — | — | would raise COD cost recovery but risks COD conversion; untested |
| P4: P2 + ₹49 COD fee | | | COD fee adds ≈ ₹42 net per COD order (≈ ₹29 expected after RTO) — economically small, behavioural benefit unknown |
| P5: Product-specific / heavy surcharge | | | for chargeable weight > 3 kg (SKUs 4, 4b, 7, 8) shipping is 7–8% of price — embed it in price and say "Insured delivery included" instead of "free" |
- **Prepaid incentive vs COD fee:** at ₹2,999 prepaid beats COD by ≈ ₹431; a ₹100 incentive costs ≈ ₹95 on every prepaid order and pays back if ≥ ~22% of would-be COD buyers switch to prepaid (model).
- **PIN-code delivery estimation (design only, not built):** (a) static PIN-prefix → zone table (metro / tier-2 / remote) filled from pilot AWB data — zero cost; (b) aggregator serviceability/ETD API if one exists for the chosen aggregator — **existence not verified**; (c) app. Remote/hill/NE PINs: COD off, delivery estimate widened or order declined.
- **Customer language (until tested):** *"Dispatched in 2–3 working days; delivery estimate shown for your PIN code."* Do not use "free shipping everywhere" or "7 days".
**Recommendation status:** policy P2 (+ heavy embed, + COD fee/prepaid-incentive test) is a **pilot hypothesis only**. It becomes a recommendation only after real freight quotes and pilot parcels.

---
## 8. Payment gateway — Gate status: **PARTIAL**
### PayU (official documentation read — `docs.payu.in/docs/shopify-faqs`; pricing page read)
**VERIFIED:** separate Shopify apps — hosted checkout (cards, UPI, net banking; supports offers), onsite cards app (cards only, **no UPI**, no offers), CommercePro Checkout, **CommercePro COD** (eligibility checks; RTO rules by PIN, address, mobile, email, cart amount, AI signals; enablement via KAM/PayU Support; install CommercePro Checkout first). UPI "must be enabled for your merchant account; new accounts may start with limited modes." Refund timelines: UPI 3–5 working days, credit cards 5–7, debit 7–10, net banking 5–7, wallets instant–24h; cancelling in Shopify can trigger a PayU refund through a webhook; offer-transaction refunds only from the PayU dashboard. Pricing page: 2% + 18% GST (cards/NB/wallets/BNPL), 3% (Amex/Diners/EMI/international), **P2P UPI zero MDR with no merchant UPI rate stated**, no setup/annual fees, **standard settlement T+2**.
**New risk found (docs):** CommercePro login requires *disabling guest checkout* and hiding default login sections; to use Shopify's default COD alongside CommercePro you must deactivate *PayU OTP Login*. → Forced login/OTP can cut mobile conversion; the pilot may instead use Shopify's **native manual COD** with manual confirmation (volume is small) and add CommercePro COD only if volume justifies it.
**Not specified anywhere I read:** KYC documents, approval timeline, KAM response times, domestic settlement detail in the Shopify docs, COD fees/enablement timelines, transaction limits, test UPI details, retry/signature handling for webhooks.
### Unresolved commercial questions to put to PayU (in writing)
1. Merchant **UPI MDR/fee** for my category and plan. 2. **COD (CommercePro) fee** per order/%, and eligibility for a new merchant. 3. COD enablement timeline and any volume minimum. 4. Can CommercePro COD run **without forced login/disabled guest checkout**? 5. **Domestic settlement cycle** and same-day option fee. 6. Refund fees; whether MDR is reversed on refunds; dashboard refund TAT. 7. **KYC documents** needed (proprietorship, GST status) and approval time. 8. Chargeback/dispute fees and process. 9. Compatibility with Shopify's current checkout on my plan; which app combination to use. 10. New-account transaction/daily limits and any rolling reserve. 11. GST invoice for fees. 12. EMI/"Affordability widget" terms and fees. 13. Is a live website with policies required before approval (Razorpay says its team reviews the website first)?
### Razorpay — fallback only
**VERIFIED (official pages):** 2% platform fee + 18% GST on the fee for cards/UPI/netbanking/wallets; ₹0 setup, ₹0 AMC, ₹0 refund processing fee; T+1 settlement (instant is an add-on, price not shown); Shopify app "All-in-one Razorpay Payment Gateway" with UPI, cards, wallets, netbanking on **Standard Checkout only**; **Razorpay reviews the website before integration**; only the account owner can connect. **Not specified in the docs I read:** COD, refunds, KYC details. The "UPI 2% / zero MDR" wording on its pricing page is ambiguous → ask.
**Decision:** **PayU remains the primary candidate (conditional);** Razorpay is the fallback if PayU's written answers to Q1, Q4, Q5 and Q7 are unfavourable. Fee differences among PayU, Razorpay and Cashfree (~2%, 2%, 1.95% listed) are negligible next to shipping. No accounts opened; no KYC shared.

---
## 9. Eight-gate status
| Gate | Status | Evidence | Missing evidence | Decision |
|---|---|---|---|---|
| 1 Supplier | **PARTIAL** | Baapstore own pages state white-label dropshipping + COD; 24 leads logged with GSTINs; zero written confirmations | Any supplier reply; idol availability at Baapstore; blind shipping/damage terms in writing; GSTIN portal checks | Hold. Send Stage 1 (BLOCKED on you) |
| 2 Product | **BLOCKED** | Sample checklist and pass/fail defined (v0.3) | No samples ordered/received | Hold until Gate 1 yields a sample-willing supplier |
| 3 Economics | **PARTIAL** | Model rebuilt; supplier-cost ceilings per SKU/price; GST-conditional | Real supplier cost, real freight, CA GST confirmation | Hold; ceilings are the pass/fail line |
| 4 Shipping | **PARTIAL** | Reported ranges; policy matrix; delivery wording fixed | Rate card (6 lanes × 4 weights, COD/prepaid), pilot AWB data | Hold; do not lock free shipping or any delivery time |
| 5 Payment | **PARTIAL** | PayU docs/pricing read; Razorpay fee/docs read; 13 open questions | PayU written UPI/COD/settlement/KYC answers | PayU conditional primary; Razorpay fallback; no accounts yet |
| 6 COD | **PARTIAL** | Simple rule set defined (v0.3 §21); PayU COD workflow verified in docs; login/guest-checkout risk found | Pilot COD RTO data; PayU COD terms | Hold; start with native COD + manual confirmation |
| 7 Legal | **BLOCKED** | GST notification text read (Schedule I/II entries, S.No. 124 exemption); TM portal confirmed to need OTP login | **Trademark search not run (BLOCKED)**; CA answers; attorney view; logo provenance | Hold; GST sub-gate PARTIAL, trademark sub-gate BLOCKED |
| 8 Brand | **BLOCKED** | Direction "Quiet Mandir" approved provisionally; palette/type/rules drafted (v0.3) | Real pilot photographs; static mockups + recognition test; font specimens on Android; Hindi proofreading | Hold; do not lock the visual system |
No gate is VERIFIED; none is FAILED.

---
## 10. Exact blockers
| # | Blocker | Owner | Unblocks |
|---|---|---|---|
| B1 | Run IP India search (OTP/captcha) and save evidence | You | Gate 7 (TM) |
| B2 | Send Stage 1 messages; verify GSTINs on GST portal; log replies | You | Gates 1, 2, 3 |
| B3 | CA consult with §3.5 questions (+ registration, invoicing) | You + CA | Gates 3, 7 |
| B4 | Rate cards: aggregator calculator + Delhivery/Blue Dart quotes | You | Gates 3, 4 |
| B5 | PayU written answers (§8 questions); Razorpay only if needed | You | Gates 5, 6 |
| B6 | Sample orders (SKUs 1–7; SKU 8 as quote/photos first) | You | Gate 2, 8 |
| B7 | Logo masters + provenance + IP attorney view | You / designer / attorney | Gates 7, 8 |
| B8 | Hindi-reading reviewer for Devanagari strings | You | Gate 8 |
| B9 | Budget limits for samples and tests | You | B6 |

## 11. Go / No-Go for Phase 1 (Shopify architecture)
**NO-GO.** Minimum commercial conditions and their current state:
| Condition | Required | Now |
|---|---|---|
| Viable supplier identified | ≥ 1 with written terms | **Not met** |
| ≥ 3–5 pilot products commercially viable | quotes within ceilings | **Not met** (no quotes) |
| Actual shipping economics understood | rate cards + pilot parcels | **Not met** |
| Quality/sample path established | samples pass checklist | **Not met** |
| GST position sufficiently understood | CA confirmation of HSN/rates | **Partly met** (text read; classification open — resin and composite are the largest unknowns) |
| Payment path confirmed | written PayU (or fallback) terms | **Not met** |
| Trademark risk assessed | search + attorney view | **Not met** |
| Initial customer promise supportable | tested delivery/returns | **Not met** (wording kept conservative) |
**Flip to GO when** B1–B7 produce: a supplier route with written blind-ship/replacement terms; ≥ 3 SKUs inside their cost ceilings and passing samples; real freight quotes; a CA memo; PayU (or Razorpay) written terms; a trademark search report with an acceptable attorney view; and a delivery promise backed by pilot AWB data.

## Sources
- IP India public search (OTP login seen): https://tmrsearch.ipindia.gov.in/tmrpublicsearch/ · E-register: https://tmrsearch.ipindia.gov.in/eregister/ · https://ipindia.gov.in/
- Notification 9/2025-Integrated Tax (Rate) [UPDATED] (ICAI print, CBIC-hosted URL): https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf
- Notification 10/2025-Central Tax (Rate), G.S.R. 660(E) (Gazette copy, third-party host): https://taxo.online/wp-content/uploads/2025/09/NN-10-2025_CT_R.pdf
- AAR commentary: https://www.taxscan.in/top-stories/marble-wooden-deities-eligible-for-gst-exemption-exemption-restricted-to-actual-idolsmurtis-aar-read-order-1451395 · Law-firm note on IGST 10/2025: https://www.saliencelegal.com/2025/09/cbic-has-issued-notification-no-10-2025-integrated-tax-rate-exempting-specified-inter-state-supplies-of-goods-from-igst-effective-from-22nd-september-2025/
- PayU: https://docs.payu.in/docs/shopify-faqs · http://payu.in/pricing/ · Razorpay: https://razorpay.com/pricing/ · https://razorpay.com/docs/payments/payment-gateway/ecommerce-plugins/shopify/ · Cashfree: https://www.cashfree.com/payment-gateway-charges · Shopify: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries
- Baapstore: https://www.baapstore.com/ · https://www.baapstore.com/pages/pricing · IndiaMART listings as cited in the tracker CSV
- Courier ranges (reported): https://www.clickpost.ai/blog/delhivery-courier-charges · COD/RTO (vendor): https://base.com/en-IN/blog/cod-return-rates-by-product-category-in-india-2026-report/
- Aggregator trademark lead (not evidence): https://www.registerkaro.in/trademark-search/waves-of-vrindavan-7900781
