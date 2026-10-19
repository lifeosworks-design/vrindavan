# VRINDAVAN — Phase 0 Report v0.3: Validation Package
Date: 2026-10-08 · Status: VALIDATION ONLY. No theme, no Liquid, no apps, no domain, no gateway, no supplier API, no listings. Nothing has been sent to anyone.

## 0. How to read this
- **VERIFIED** = I opened the page / saw it myself this session. **REPORTED ⚠** = secondary source (blog, aggregator, law-firm note). **ASSUMPTION** = my placeholder. **UNKNOWN** = must be collected.
- **Honest limits:** (1) Museum references: the Met page returned HTTP 429 and the National Museum site could not be opened, so the museum-presentation section is from general knowledge, not from pages I read this session. (2) Temple architecture and colour symbolism come from encyclopaedic/secondary sources (colour symbolism from fashion/education blogs). (3) I did not run the IP India trademark search (it needs the live official portal). (4) Supplier facts come from IndiaMART/TradeIndia listing pages — self-reported by the seller. (5) Courier rates: no official rate card is public; all numbers are ⚠.
- **Changes since v0.2:** creative direction corrected (§1–§3); real Indian devotional references added; supplier evidence fields filled from listing pages; gateway fees from official pages; economics rebuilt on heavier, evidence-based shipping.

---
# PART I — CREATIVE CORRECTION: AUTHENTIC INDIAN DEVOTIONAL × MODERN PREMIUM
## 1. Central principle (adopted)
> **"An elegant modern digital experience inspired by entering a beautiful Indian mandir."**
> "Gallery" describes **quality of presentation** (space, light, restraint) — not the cultural identity. The cultural identity is **devotional and Indian**.
Renamed working direction: **"Quiet Mandir"** (Gallery dropped from the name to avoid the Western-museum reading). Still provisional — validated against the 8 pilot products' real photography (Gate 8).

## 2. What I studied and what I extracted (principles, not decoration)
**A. Temple architecture (secondary sources: Wikipedia "Hindu temple architecture / Garbhagriha", Sanskriti Magazine, a Brihadeshvara lighting paper cited in results)**
- *Journey inward:* bright outer world → pillared mandapa → antarala → dark sanctum (garbhagriha) holding one deity. → **Translate:** the site is a *sequence of thresholds*: bright, open home → deity "halls" → a quiet, focused product page where **one idol is the whole point**.
- *Light gradient:* glare outside, subdued filtered light, then a single lit deity. → **Translate:** lighter, airier browse pages; **warmer, calmer, more focused PDP**; warm radial glow behind the idol.
- *Grid and symmetry:* temple plans sit on a square grid (padas / mandala); symmetry and repetition. → **Translate:** strict centred axis for heroes, 4/8px grid, symmetrical product tiles; no random asymmetry.
- *Layered thresholds & circumambulation:* gateway (torana), steps, pradakshina path around the sanctum. → **Translate:** arch-framed entry (hero), "walk around" the product = swipe gallery (front/side/back/detail), generous breathing room.
- *Ornament is structural:* jali screens filter light; carved pillars carry meaning. → **Translate:** ornament appears as **edges and frames** (arch crop, thin border strip, jali as a footer tint), never as wallpaper.
- Not sourced this session: jali and torana specifics (search returned nothing) — flagged.

**B. Real Indian references I opened at 390px**
| Reference | What I saw | Extract | Avoid |
|---|---|---|---|
| **Sri Mandir** (devotional app/site) | Deep-brown + saffron palette; temple-icon mark; a **thin scalloped "toran/bandhanwar" strip** separating content from the bottom tab bar; bottom navigation (Explore / Puja / Chadhava…); "Trusted by 30 million+" ticker; hero blank at first paint | Ornament as a **thin strip**; saffron used as a warm accent against deep brown; bottom nav is normal in Indian devotional UX | Slow/blank hero; app-download banner above the header |
| **Cycle Pure Agarbathi** (cycle.in) | Deep-indigo UI, round category thumbnails photographed in **diya/marigold warm light**, copy "Fragrances for divine experiences", consent banner with an equal-weight *Decline* button | Diya-lit warm photography as the devotional signal; round/arch category entries; fair consent | Lazy-image placeholders visible; strong yellow banner button |
| **Nicobar** (India-rooted modern) | Wide-tracked light wordmark, rich red/gold/dark-green campaign photography, minimal text nav | Restrained UI, **richness comes from photography** | Campaign-heavy hero, not product-first |
| **Good Earth** (opened in v0.2) | Print language as identity; one medallion | Identity carried by a *repeatable motif* | Pattern-as-hero overload |
| **Amrapali** | Crest wordmark, bottom tab bar (Home/Shop/Account/Wishlist), INR selector, warm jharokha-toned photography; **newsletter modal covering the hero at first paint** | Bottom tab bar convention; warm-toned photography | First-paint modal |
| **Kama Ayurveda** (v0.2) | Festive hero, gift-threshold copy, category chips | Gift thresholds, chips | Colourful promo-led hero |
| **Exotic India / Stone Studio** (v0.2) | Cream + serif + one accent; placement photography | Cream/ivory is accepted in the category | Saturated orange; watermarks |
- Design-trade commentary (The Design People, Confetti, UnFoldMart — agency/trade pieces, not performance evidence): premium puja packaging pairs temple-art colours (saffron, ceremonial red, gold) **with restraint**, uses clean layouts with symbolic detailing, and gives fuller usage/ingredient information. A Medium case study uses the **temple arch** as the core device of a brand identity.

**C. Museum / heritage presentation (NOT verified this session — general convention, to be checked against NMI / CSMVS / the Met once reachable):** object shown upright, eye-level, single object on a neutral plinth, even raking light, a caption with *title, period/region, material, dimensions, accession/provenance*. → **Translate:** a **"museum label" spec block** on every PDP (Deity · Form · Material · Finish · Height · Width · Weight · Base · Origin region (if verified)).

**D. Colour symbolism (secondary: fashion/education blogs ⚠):** red/kumkum = auspicious (life force, prosperity); saffron = fire, sacrifice, renunciation, dhvaja flags — but **politically charged, never a neutral orange** (design-focused source); yellow/haldi = purification, Vishnu; blue = infinite (Krishna, Rama, Shiva Neelakantha); crimson + ivory + antique gold reads refined. Meanings vary by region and occasion. → **Saffron is not used as a UI colour.** Maroon (kumkum-deep) is the Indian secondary tone.

## 3. Palette v2 — "temple stone, brass, kumkum" (provisional)
Rule: **BASE** = temple-stone neutral · **PRIMARY ACCENT** = brass · **SECONDARY** = one Indian tone (temple maroon) · **PHOTOGRAPHY** = all the richness.
| Token | Hex | Use | Contrast (computed) |
|---|---|---|---|
| `--stone-ivory` | `#F7F1E6` | page background | — |
| `--sandstone` | `#EFE4D0` | alt sections, cards | — |
| `--ink` | `#231B16` | text, primary outline | 15.1:1 on ivory |
| `--ink-soft` | `#5A4D42` | secondary text | 7.3:1 on ivory |
| `--brass-deep` | `#8F5A0E` | accent text, hairlines, icons | 5.1:1 on ivory (4.6:1 on sandstone) → text ≥ 16px or 14px bold only |
| `--brass-logo` | `#D2961E` | **decoration only** (matches logo) | 2.3:1 → never text |
| `--maroon` (kumkum) | `#7B1E2B` | primary CTA fill, links, sale/price emphasis | 9.1:1 with ivory text |
| `--sanctum` (dark) | `#1E1712` | festival band, footer | ivory text 14.7:1; `#C9923A` text 6.5:1 |
| `--teal-eye` | `#1A8A8A`/navy eye | **logo only** (not a UI colour) | — |
Not used: saffron, bright gold gradients, metallic UI fills. Teal appears only inside the emblem.

## 4. Typography (provisional — must be specimen-tested on a real mid-range Android at 390/412px)
- **Verified:** *Tiro Devanagari Hindi* exists on Google Fonts (page title confirmed; supported scripts/weights/licence **not** confirmed by me). **Reported ⚠:** Noto Serif/Sans Devanagari are designed to harmonise with their Latin counterparts; Hind and Mukta are described as Indic-friendly UI faces (low-quality source).
- **Shortlist to test:** (1) **Tiro Devanagari Hindi** for headlines + deity names (check whether its Latin glyphs are acceptable); (2) **Noto Serif + Noto Serif Devanagari** as the safe, harmonised fallback; (3) UI/body: **Hind** or **Mukta** (Latin + Devanagari in one family) or Noto Sans. Max two families; self-host, subset, `font-display: swap`; Devanagari subset limited to the deity-name strings.
- Scale (mobile base 16px): H1 28/34, H2 22/28, H3 18/24, body 16/24, small 14/20, label caps 12/16 (letter-spaced). Prices tabular, 18px semibold.
- **Avoid:** script/calligraphic display faces (wedding), heavy slab "temple donation" faces, thin Garamond-style fashion serifs (Western luxury), decorative Devanagari faces.
- **Devanagari rule (purposeful only):** (a) deity names as the *bilingual label* on tiles and PDP titles — "गणेश · Ganesha" — it aids recognition and search, signals authenticity; (b) mantras/shlokas only on story/packaging with a verified source and Hindi/Sanskrit proofreader; (c) **never** as texture or background. Every string reviewed by a native reader before use.

## 5. Devotional micro-details — a budget, not a theme
| Detail | Rule | Cost |
|---|---|---|
| Arch crop (cusped ogee from the logo) | hero image + deity tiles; **max 1 arch frame per screen** | CSS `clip-path`/SVG mask, ~0 KB |
| Toran / scalloped strip (cf. Sri Mandir) | 8–12px strip as a section divider; ≤ 1 per page; maroon/brass on ivory | inline SVG, < 1 KB |
| Lotus divider (from logo) | section end-marks only | existing asset, vectorise |
| Jali tint | footer background at 4–6% opacity | SVG pattern, < 2 KB |
| Stone grain | 2–3% noise on ivory (optional) | skip if it hurts LCP |
| Diya glow | warm radial gradient behind the PDP idol | CSS gradient |
| Brass hairline | 1px `--brass-deep` rules | CSS |
| Custom icons (diya, bell, lotus, kalash) | line, 1.5px, only for trust points | SVG sprite |
**Budget rule:** ≤ 2 devotional details visible per mobile screen; none inside forms, cart, checkout; none behind text; nothing animates except a ≤ 200ms fade.
**Brass/metal language:** flat `--brass-deep` + hairlines + warm hover tint. **No** metallic gradients, hammered textures or bevels in UI. (Your wordmark's embossed gold is the one metallic element; ask the designer for flat versions.)

## 6. Product presentation = reverence + craftsmanship (rules)
**Photography:** idol upright, camera at the idol's eye-level, never looking down on the deity; full figure with room above and below; no cropped head/feet; clean sandstone/ivory sweep, soft warm side-light (no flash glare on brass); hero on a simple **padmasana/plinth**; scale shot beside a **diya or on a pooja shelf** (never held by a model, never beside food/alcohol/shoes/clutter); in-situ shot in a mandir niche (home/shelf); macro of finish/face/hands; back and base shot (builds trust). No promotional stickers, "SALE" ribbons, countdowns or price tags overlaid on the deity image.
**Deity colour cues (backdrop tints, subtle):** Krishna — peacock-blue/teal shadow, flute and feather props kept minimal; Shiva — ash/charcoal stone, darker backdrop; Ganesha — warm stone with a single marigold; Lakshmi — soft lotus-pink/red accent, brass lamps; Vishnu — pale-yellow/haldi cast; Durga — deep red accent; Hanuman — warm sindoor-orange accent. Validate with a Hindi-speaking reviewer; regional preferences differ.
**Copy:** use "murti" in storytelling and "idol/statue" where needed for search; describe, don't oversell; never "Sale!" next to a deity name in headings; neutral, respectful voice.
**Policy sensitivity:** idols that have been installed/worshipped should not be resold — returns policy should state this clearly (legal/CA/ops review).

## 7. Authenticity = evidence, not marketing
| Claim | Allowed only if… | Evidence | Where shown |
|---|---|---|---|
| "Brass" | supplier states alloy in writing + our check (magnet test: brass is non-magnetic; density/weight sanity; optionally a lab test) | supplier letter + test note | PDP spec "Material (supplier-stated; weight verified by us)" |
| "Handcrafted / handmade" | supplier confirms process per SKU in writing (cast + hand-finished vs machine) | written statement + process photos | PDP "Made by" line |
| "Made by Indian artisans" | named workshop + location confirmed | supplier identity, GST, photos | About / PDP origin region |
| "Pure …", "temple certified", "100% handcrafted" | **do not use** (no verifiable standard) | — | never |
| Dimensions & weight | we measured the sample | scale/ruler photo | PDP spec table |
| Origin ("Moradabad brass") | supplier's workshop location confirmed | listing + call | spec table + provenance line |
| "Inspected before dispatch" | actually done (checklist) | QC sheet | trust strip |
**Evidence badges (honest, small):** *Measured by us* · *Photographed by us* · *Packed with protective crate/foam* — each only when true.

## 8. Homepage — strongest version (journey inward; not blindly the template)
1. **Header** (wordmark, search, cart; no tab bar on launch).
2. **Threshold hero:** one idol in an arch crop on warm stone, a single line, one CTA ("Shop idols"). No carousel, no sale.
3. **Shop by deity:** arch-cropped tiles (only deities actually in stock), bilingual labels.
4. **Short devotional introduction (2–3 lines):** who we are and what "inspected, measured, honestly priced" means — only claims we can evidence.
5. **Featured pieces:** horizontal rail of 6 with price and delivery pill (only once proven).
6. **From workshop to mandir:** craft and material story with real photos (measured weight, finish close-ups) — appears only once pilot content exists; otherwise omit.
7. **Shop by purpose:** Home mandir · Gifting · Festivals.
8. **Festival edit** (seasonal dark `--sanctum` band, diya glow).
9. **Reviews** (real, with city; hidden until ≥ 5 real reviews).
10. **Trust strip:** PIN-code delivery estimate, COD terms, returns, secure payment.
11. **Footer:** emblem 1 mono, jali tint, lotus divider, policies, grievance contact.
Why this is not the template: sections 4/6/9 are *conditional on real evidence*; 7 and 8 are demand-driven; no storytelling filler.

## 9. Navigation (only what the real catalogue supports)
- **Launch (15–30 SKUs):** primary menu ≤ 5 items — *Shop by deity* (≤ 6: Ganesha, Krishna, Lakshmi, Shiva, Hanuman, Durga — add Vishnu only if stocked) · *Home mandir* · *Gifting* · *Festivals* · *About*. **Material (Brass/Resin/Marble)** = filter, not menu. Décor/Buddha only if stocked.
- Mobile: full-screen menu with deity tiles; search always one tap away; PDP has a breadcrumb.

## 10. The balance (where we land)
| Axis | Position | Why |
|---|---|---|
| Devotional ↔ Modern | 60 / 40 | devotion in light, colour, labels; modern in layout, type, speed |
| Traditional ↔ Contemporary | 55 / 45 | traditional forms (arch, torana), contemporary spacing |
| Spiritual ↔ Commercial | 55 / 45 | calm, no pressure tactics; clear price/buy box |
| Premium ↔ Accessible | 55 / 45 | premium presentation, ₹1.5k–8k entry/core prices |
| Indian ↔ Global quality | 65 / 35 | Indian cues carry identity; global UX standards carry performance |

## 11. Final design test (applied as a checklist — to be proven with mockups, Gate 8)
1. **Logo/names removed → still Indian & devotional?** Cues that survive: arch-cropped deity tiles, diya-warm brass photography, stone/brass/kumkum palette, toran strip, bilingual Devanagari labels, centred temple-like symmetry. If a 5-person test cannot name "Indian + devotional" within 5 seconds → too generic.
2. **Cheap religious template?** Fail triggers: > 2 ornaments per screen, ornamental fonts, saffron backgrounds, om/mandala wallpaper, sale stickers on deities. We pass only if the budget in §5 holds.
3. **Western luxury store?** Fail triggers: all-neutral white/black/gold only, thin fashion serifs, no Indian cues, lifestyle shots with Western props. We pass if §3–§6 hold.
Validation method (no coding): 3 static 390px mockups (home, collection, PDP) using real sample photos; 5–8 Indian users incl. 2 older (45+); record recognition, trust, "feels respectful?" and tap-clarity.

---
# PART II — SUPPLIERS
## 12. Supplier leads (A) — categories: VERIFIED · PARTIALLY VERIFIED · UNVERIFIED LEAD · REJECT
Definition used: **VERIFIED** = written/official evidence of dropshipping *for relevant products* + manufacturer/wholesaler status. **No supplier reaches VERIFIED.** Nothing here has been contacted.

| # | Supplier | Source | Category / location | Manufacturer/wholesaler evidence | Dropship | White-label | COD | India-wide ship | API | Still unknown | Status · Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Baapstore** | baapstore.com (own site, fetched) | Platform; "Home Decor" browse category exists; idols **not** seen | Reseller platform, subscription | **Stated** on own page ("dropshipping") | **Stated** ("whitelabel", dispatch under your brand) | **Stated** (COD available) | Not stated explicitly (pan-India implied? unverified) | Not stated (Shopify product sheets; they build Shopify store on Pro plan) | **Idol/pooja catalogue; weight limits; ₹69/₹89 flat shipping (page inconsistent) vs heavy items; returns ₹99/product, 5-day window; COD fee/remittance; quality** | **PARTIALLY VERIFIED** (model, not product fit) · Medium on model, Low on idols |
| 2 | Kamal Metals | IndiaMART profile (fetched) | Brass idols/brass; Moradabad, UP | Listed "Manufacturer", proprietorship, GST 09AKZPK9330Q1ZX, GST-verified badge, "17 yrs" membership, GST reg. 2017 | Not mentioned | Not mentioned | Not mentioned | Not mentioned | Not mentioned | Everything operational; MOQ | **UNVERIFIED LEAD** · Medium (identity), Low (fit) |
| 3 | AYC Metals (URL slug "yaqub-handicrafts") | IndiaMART (fetched) | Brass Ganesha, Kalpavriksha, dhoop burners; Moradabad | "Exporter & Manufacturer", GST-verified badge (no number shown), 5 yrs membership | No | No | No | No | No | Name mismatch (AYC vs Yaqub) to be clarified; MOQ | **UNVERIFIED LEAD** · Low–Medium |
| 4 | Aakrati Brassware | TradeIndia list (snippet only) | Brass idols; Aligarh | "18 yrs membership" (not fetched) | ? | ? | ? | ? | ? | All | **UNVERIFIED LEAD** · Low |
| 5 | Indian Culture Handicraft | TradeIndia list (snippet only) | Brass; Jaipur | Not fetched | ? | ? | ? | ? | ? | All | **UNVERIFIED LEAD** · Low |
| 6 | Vedic Vaani | GlobalLinker (snippet) | Puja items/idols; Mumbai | Lists GST + IEC (snippet) | ? | ? | ? | ? | ? | Whether manufacturer or retailer | **UNVERIFIED LEAD** · Low |
| 7 | Keshav Enterprises | GlobalLinker (snippet) | Brass idols; Aligarh | "Distributor and exporter" (snippet); MOQ 1 kg | ? | custom for bulk (snippet) | ? | ? | ? | All | **UNVERIFIED LEAD** · Low |
| 8 | **Arham Trades** | IndiaMART (fetched) | Polyresin Ganesha/Buddha; Jaipur | Sole proprietorship (2016), GST 08AQCPC6855D1Z1, "Exporter & Trader–Retailer" (trader, not clearly manufacturer on IndiaMART heading; snippet said manufacturer) | No | No | No | "deliver within assured time-frame" only | No | **Ratings 4.1/5 (13), 23% are 1-star**; MOQ; trader vs maker | **UNVERIFIED LEAD** · Low–Medium (caution) |
| 9 | Bemount Creations | IndiaMART (fetched) | Polyresin (29 listings), Ganesh, Hanuman, Laxmi-Ganesh; Loni, UP | GST nature "Manufacturer", GST 09AWDPA0599F1ZN (reg. 2021), "11 yrs" | No | No | No | "timely delivery" only | No | Rating 5.0 from **3** reviews (weak evidence); also makes trophies (not devotional-first) | **UNVERIFIED LEAD** · Low–Medium |
| 10 | Craftam Manufacturer | IndiaMART (snippet) | Resin Ganesha (dashboard); Jaipur | 51–100 employees, est. 2020 (snippet) | ? | ? | ? | ? | ? | Product fit (mostly small/dashboard) | **UNVERIFIED LEAD** · Low |
| 11 | Satyam Gifts | GlobalLinker (snippet) | Fibre/marble-powder Ganesh; Mumbai | Not fetched; MOQ 1; "dispatch within 3 days" claim | ? | ? | ? | ? | ? | Material is composite, not marble | **UNVERIFIED LEAD** · Low |
| 12 | Rati Greentech / P&R-Elysee Decor | GlobalLinker/IndiaMART (snippets) | Resin/composite; Delhi / Muzaffarnagar | Not fetched | ? | ? | ? | ? | ? | All | **UNVERIFIED LEAD** · Low |
| 13 | **Harihar Murti Bhandar** | IndiaMART (fetched) | Marble murtis; Kartarpura, Jaipur | "Manufacturer", GST 08HDTPS1874R1Z2 (reg. 2025), ≤10 employees, Vietnam White/Makrana marble stated, est. 2002 | No | No | No | **"Specialized wooden crate packaging for delivery across India" (stated)** | No | Header "9 yrs" vs "20+ years" conflict; GST registered only 2025; MOQ; freight cost | **UNVERIFIED LEAD** · Medium (for marble) |
| 14 | Icones Moorti Creation | IndiaMART (fetched) | Marble statues; Jaipur | "Exporter & Manufacturer", proprietor named, GST 08CZEPB7137C1ZP, ratings 3.9 (13?), HSN listed 6802 etc.; listed prices ₹10,000–37,000/piece | No | No | No | "across Pan India and Globe" (own claim) | No | Rating meaning; packaging; freight | **UNVERIFIED LEAD** · Low–Medium |
| 15 | Jaipur Marble Emporium | IndiaMART (fetched) | Marble/black-stone; Viratnagar, Jaipur | Sole proprietorship, GST 08EPDPM7411D1Z2, 4.8 (35 ratings), 84% response, "Payment Protected" badge, "Since 2019" vs "10 yrs" conflict | No | custom sizes only | No | "supply everywhere" (own wording) | No | Packaging, freight, quality | **UNVERIFIED LEAD** · Medium |
| 16 | Moorti India / Riddhi Siddhi / Sai Sagar / Sai Shradha | search snippets | Marble; Jaipur | Not fetched | ? | custom design (Moorti India, snippet) | ? | ? | ? | All | **UNVERIFIED LEAD** · Low |
| 17 | The Stone Studio (trade desk) | thestonestudio.in/wholesale (fetched) | Stone/Buddha/Hindu/garden statues; Bhubaneswar | Retailer-manufacturer; wholesale page: terms "once we have reached an agreement", phone/form route | Not stated | Not stated | Not stated | Site says free shipping on selected products | No | MOQ, margins, branding | **UNVERIFIED LEAD** · Low–Medium |
| 18 | Exotic India (wholesale) | official page 404; Faire brand page appears in search; affiliate programme (8%) | Brass etc. | Large retailer | Not verified | Not verified | Not verified | Insured shipping (own claim) | Not verified | Whether any B2B route exists; competitor conflict | **UNVERIFIED LEAD** · Low |
| 19 | Veda Connection (bulk) | vedaconnection.in (v0.1) | Idols; Delhi (Dwarka) | WhatsApp bulk-discount strip observed | Not verified | Not verified | Site states COD | Site states free shipping | — | Whether they supply other retailers | **UNVERIFIED LEAD** · Low |
| 20 | GlowRoad | blogs/forum | Resale app | Amazon-acquired 2022; status conflicts | Reported | ? | Reported | ? | ? | Active? idols? | **UNVERIFIED LEAD** · Very low |
| R1 | Miraya International (Moradabad) | listing | Brass | Nataraja listing **MOQ 500 pcs** | — | — | — | — | — | — | **REJECT** (MOQ) |
| R2 | Keshav Arts (Mathura) | IndiaMART (fetched) | Resin/cold-cast | Exporter & manufacturer, GST 09BWEPG0401L1ZT | No | No | No | No | No | **Rating 2.9 (7)** | **REJECT for now** (quality signal) |
| R3 | Meesho / IndiaMART / TradeIndia / ExportersIndia as "dropshipping"; Qikink / Printrove (POD merch); CJ/overseas; India→US dropship services | various | — | Marketplaces/directories/POD/imports | — | — | — | — | — | — | **REJECT** |
**GSTINs shown above are as displayed on listings — verify each on the official GST taxpayer search before engaging.** B2B listing ratings are small-sample and self-selected.

## 13. Outreach package (B / final)
**Approach (to maximise replies):** two stages. **Stage 1** = 6 must-answer questions by WhatsApp / IndiaMART. **Stage 2** = full email to those who reply. Do not share: brand name, volumes, margins, launch date, other suppliers' prices. Send during working hours; follow up once after 48h, once after 5 days. You send these (I will not send messages for you).

**A. WhatsApp (English)**
> Namaste, I'm starting a small online store for devotional idols in India and I'm looking for a manufacturing partner for [brass / resin / marble] murtis. A few quick questions:
> 1. Can you ship single orders directly to my customers without your branding on the parcel or invoice?
> 2. Do you have a catalogue with wholesale rates and dimensions/weights?
> 3. What is the minimum order, and can I order 2–3 samples first?
> 4. What are your dispatch time, courier and shipping charge per parcel?
> 5. If a piece arrives damaged or the order is returned, what is your replacement/return policy?
> 6. Do you give a GST invoice?
> Thank you — [Name]

**A2. WhatsApp (Hinglish — have a native reader check)**
> Namaste ji, main India mein ek chhota online murti store shuru kar raha/rahi hoon aur [brass / resin / marble] murtiyon ke liye supplier dhoondh raha/rahi hoon. Kuch sawaal: 1) Kya aap seedha mere customer ko single order bhej sakte hain, bina apne branding ke? 2) Catalogue aur wholesale rate (size/weight ke saath) mil sakta hai? 3) Minimum order kitna hai, aur kya pehle 2–3 sample mil sakte hain? 4) Dispatch time, courier aur shipping charge kitna hoga? 5) Toot-phoot ya return hone par replacement/return policy kya hai? 6) GST invoice milega? Dhanyavaad — [Name]

**B. Email** — Subject: *Wholesale & single-order dispatch enquiry – [material] murtis*
> Dear [Supplier],
> We are setting up an online store for devotional idols in India and are evaluating manufacturers. Could you please confirm in writing:
> **Fulfilment** — (1) Do you support dropshipping (direct dispatch to our customers) with blind shipping — no supplier name, branding or invoice on the parcel? (2) Can you use plain or custom packaging/insert cards, and at what cost/MOQ?
> **Commercials** — (3) Catalogue with dimensions and weights; (4) wholesale price per item and MOQ per SKU; (5) sample order process, cost and lead time for 3 items; (6) GST invoice and HSN used.
> **Logistics** — (7) Dispatch time after order; courier(s); shipping cost by weight/zone; tracking number sharing; (8) COD support and remittance cycle; (9) Handling of RTO.
> **Loss & returns** — (10) Packing method for fragile pieces; (11) damaged-in-transit and wrong-item replacement policy; (12) return policy.
> **Operations & content** — (13) How orders are forwarded (WhatsApp/Excel/API/Shopify) and how stock/inventory is shared; (14) product photos/video of the exact piece and permission to use them.
> Please also share your GSTIN and workshop location. Thank you, [Name · phone]

**C. IndiaMART short message**
> Need [item/size] — first 2–3 samples please. Do you dispatch single orders to my customers (no branding)? Price/pc, MOQ, weight, dispatch time, courier, damage replacement, GST invoice. Reply with catalogue on WhatsApp [no.].

## 14. Information to collect from every supplier (M) — scorecard columns
Identity: legal name, GSTIN (verified on portal), workshop address, years in business, contact person · Product: material/alloy, process (cast/hand-finished), finish type, dimensions, weight, base type · Commercial: price/pc, MOQ, sample price, price validity, payment terms · Fulfilment: dropship yes/no, blind shipping, white-label/packaging options, dispatch SLA, courier, shipping cost by weight/zone, COD & remittance cycle · Loss: packing method, damage replacement, RTO policy, return policy · Systems: order channel (WhatsApp/Excel/API), stock updates, tracking sharing · Content: photo/video, permission to use · Proof: sample received date, QC score, references (2 other retailers they supply, if willing) · Red flags: refuses sample, demands large advance, no GSTIN, vague about packing.
Log in one sheet: supplier × (answers, date, response time, score). Response time itself is a signal.

---
# PART III — PILOT, SAMPLES, ECONOMICS
## 15. 8-SKU pilot proposal (C)
Selected to test the *business model*, not taste. **Supplier prices are UNKNOWN (to collect)**; dimensions/weights are *design targets (ASSUMPTION)* until suppliers send specs. Expected shipping is from the model (§19). "Contribution" = prepaid, before ads, at 42% cost ratio (ASSUMPTION) and 5% GST.
| # | SKU | Material | Target dim / weight | Candidate supplier route | Supplier price | Exp. ship (model) | Target price | Prepaid contribution (model) | Fragility | Why selected / demand hypothesis |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Seated Ganesha 3–4 in | Brass | ~9 cm / 0.3–0.5 kg | Moradabad (Kamal / AYC) | TBD | ~₹123 | ₹999 | ≈ ₹379 (with ₹79 customer-paid shipping) | Low | Tests the **below-₹1,499 shipping rule**, gift/add-on demand, lightest parcel |
| 2 | Lakshmi–Ganesha pair 6–7 in | Brass | ~16 cm / 1–1.5 kg | Moradabad | TBD | ~₹190 | ₹1,999–2,499 | ≈ ₹700 (₹1,999) | Medium | Diwali/Dhanteras demand hypothesis; pair = higher AOV; medium parcel |
| 3 | Radha-Krishna 9–10 in | Brass | ~24 cm / 2–2.5 kg | Moradabad | TBD | ~₹258 | ₹2,999–3,499 | ≈ ₹1,085 (₹2,999) | Medium–High (flute/arms) | **Brand-name resonance (Krishna)**; detail fragility; core price point |
| 4 | Standing Hanuman or Shiva 12–15 in | Brass | ~35 cm / 4–6 kg | Moradabad / Jaipur | TBD | ~₹390–590 | ₹4,999–7,999 | ≈ ₹1,853 (₹4,999) / ₹3,003 (₹7,999) | Medium; **heavy** | Heavy-parcel economics; non-Krishna deity coverage |
| 5 | Ganesha 8 in | Polyresin / cold-cast | ~20 cm / 0.8–1.2 kg | Jaipur / Loni resin makers | TBD | ~₹157–190 | ₹1,499–1,999 | ≈ ₹505–699 | Medium (paint chips) | Cheaper-material benchmark; paint/finish risk |
| 6 | Krishna with flute 10 in | Resin / cold-cast | ~25 cm / 1–1.5 kg | Resin makers | TBD | ~₹190 | ₹1,999–2,499 | ≈ ₹700+ | **High** (thin flute/crown) | **Fragile-shape stress test** for packaging |
| 7 | Ganesha or Lakshmi 9–12 in | Marble-composite ("marble dust") | ~25–30 cm / 3–6 kg | Jaipur / Mumbai composites | TBD | ~₹392 | ₹4,999 | ≈ ₹1,853 | Medium; heavy | Heavy white-stone aesthetic; **tests material honesty (composite ≠ marble)** and GST classification |
| 8 | Radha-Krishna 12 in (optional premium) | **Real marble** | ~30 cm / 8–12 kg | Jaipur marble (Harihar / Jaipur Marble Emporium / Icones) | TBD (Icones listings show ₹10,000–37,000 per piece — their prices, not ours) | ~₹930 (10 kg) | ₹12,000–15,000 | ≈ ₹4,448 (at ₹12,000, 5% GST) / ≈ ₹5,019 (0% if exempt as deity ⚠) | **High**; very heavy | High-AOV test; freight + breakage risk; possible GST exemption; wooden-crate packing (Harihar states it) |
Not in pilot (deliberately): Buddha/décor desk pieces and pooja accessories — add after the model is validated. If a premium real-marble sample is too costly, run SKU 8 as a quote + photo/video review only.
**Selection logic:** 3 weight classes (light ≤0.6 kg, medium 1–2.5 kg, heavy 4–10 kg); 3 materials; 3 fragility levels; ₹999 → ₹12–15k; 5 deities (Ganesha, Lakshmi, Krishna, Hanuman/Shiva); at least one SKU per candidate supplier cluster.

## 16. Formal sample-testing checklist (score 1–5; Critical = pass/fail)
Test every sample on arrival in **the supplier's own packaging** (photograph the unopened parcel), then ship a **second unit** through the real courier to a test address (metro, tier-2, remote).
| Group | Item | How to test | Pass threshold |
|---|---|---|---|
| **Product quality** | Finish | daylight + warm lamp inspection | ≥ 4; no visible pits/burrs on face/hands |
| | Detail | macro photo of face/hands/ornaments | ≥ 4, features crisp; matches supplier photo |
| | Paint/coating | fingernail scratch on hidden area; damp-cloth rub | ≥ 4; **no colour transfer/flaking** |
| | Material authenticity | magnet test (brass non-magnetic), weight vs claimed density, supplier alloy statement; marble vs composite by weight and chip-edge inspection | claim consistent with evidence; any mismatch = **Critical FAIL** |
| | Stability | tilt-test on a flat shelf | stable to ~10° tilt; base flat, no rocking |
| | Dimensions | ruler/calipers vs listing | within ±5% (±3 mm on small) |
| | Weight | digital scale | within ±5% of listing |
| | Defects | cracks, casting holes, loose parts, sharp edges, smell | **0 critical** (crack, missing part, wrong deity, face damage) |
| **Packaging** | Protection | inner wrap, void fill, rigid outer box/crate; photograph layers | each fragile protrusion wrapped; no free movement |
| | Damage resistance | actual shipped second unit + (optional) drop of a spare packed unit ~0.8 m | **0 breakage** across pilot parcels |
| | Presentation | clean outer box, no supplier branding if blind shipping promised | ≥ 4 |
| | Branding | plain or our insert card possible | yes/no (needed for white-label) |
| | Unboxing | 3 testers rate 1–5 | mean ≥ 4 |
| | Sustainability | minimal plastic, recyclable fill | ≥ 3 (informational) |
| **Fulfilment** | Processing time | order → supplier "ready" | ≤ 1 working day |
| | Dispatch time | order → pickup scan | ≤ 2 working days (≥ 90%) |
| | Courier & tracking | scan events | ≥ 4 scans, ≤ 24h lag; AWB shared same day |
| | Delivery time | order → delivered | metro ≤ 7 working days, others ≤ 10 (≥ 80%) |
| | Actual vs promised | compare to supplier promise | within +1 day |
| **Customer experience** | Expectation vs reality | 3 testers compare site-style photos with product | mean ≥ 4 |
| | Perceived value | testers guess price; compare to selling price | guess ≥ 85% of price |
| | Photography accuracy | colour/finish vs our photos | ΔE judged "same" by ≥ 2 of 3 |
| **Economics** | Landed cost | supplier price + shipping + packaging | cost ≤ 42–45% of price incl. GST |
| | Payment fee | gateway + Shopify | per §21 |
| | COD & RTO exposure | COD fee, RTO cost from quotes | per §19 |
| | Replacement exposure | damage rate × replacement cost | ≤ 5% of orders |
| | Contribution | model with real numbers | ≥ 30% of ex-GST revenue (prepaid), ≥ 20% (COD blended) |
**SKU pass:** product-quality weighted mean ≥ 4.0, no item < 3, **0 Critical**, packaging 0 breakage, economics pass. **Supplier pass:** ≥ 2 SKUs pass, dispatch/communication SLA met, written policies received. 10+ parcels is directional only — it cannot prove RTO or damage *rates*, only expose failure modes.

## 17. Updated unit economics (G)
**VERIFIED facts used:** Shopify Payments is not available in India — third-party gateway needed (Shopify Help, supported-countries page, fetched). PayU domestic fee 2% + 18% GST on fee (payu.in pricing, fetched). Razorpay 2% platform fee + 18% GST on fee, setup ₹0, refund processing ₹0 (razorpay.com/pricing, fetched). Cashfree: 1.95%/2.0% figures on its charges page, GST 18% (fetched; assignment of rates to modes unclear). Baapstore pricing page: Pro ₹24,999/yr, flat ₹69 or ₹89 shipping per product (inconsistent), returns/RTO ₹99/product (fetched).
**REPORTED ⚠:** Shopify 2% extra on third-party gateways (Basic); Delhivery 1 kg estimates by zone A ₹65–85, B ₹75–110, C ₹90–150, D ₹110–180, E ₹150–250, F ₹180–320; ₹32/500 g intra-city; fuel surcharge 10–18%; COD fee ₹35–40 or 1.5–2% (greater); RTO charge 80–100% of forward freight; COD RTO 20–40%; GST 5% total (2.5% central + equal state) on listed handicraft statues from 22 Sep 2025 (CBIC 13/2025-CT(Rate) via tax commentary — I could not read the official PDF).
**ASSUMPTIONS:** supplier cost 42% of GST-inclusive price (sensitivity 50%); blended 1 kg freight ₹110 (+₹60 each extra kg, +12% fuel), chargeable weight = actual × 1.3 rounded up to 0.5 kg; packaging ₹25–110 by size; prepaid fee = gateway 2% + 18% GST + Shopify 2% = 4.36%; COD cost = max(₹40, 1.75% of price); COD RTO 30%, RTO cost = 1.9 × forward freight + packaging (item resaleable); damage/replacement 5% of delivered orders at full replacement cost; ₹79 customer-paid shipping below ₹1,499; GST 5%; COD share 50%.
**Scenarios (₹ per order placed, before ads; rounded)**
| Price | Actual wt → charged | Revenue ex-GST (+ cust. ship) | COGS | Ship (ours) | Pack | Payment (prepaid) | COD cost | Exp. RTO cost (COD) | Exp. replace | **Prepaid** | **COD** | **COD + ₹49 fee** | **Blended 50/50 = max break-even CAC** | **Target CAC (≈50%)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ₹999 | 0.4 → 1.0 kg | 951 (+67) | 420 | 123 | 25 | 44 | 40 | 78 | 28 | **379** | **190** | **220** | **284** (300 with fee) | ~₹140 |
| ₹1,499 | 0.8 → 1.5 | 1,428 | 630 | 157 | 30 | 65 | 40 | 98 | 41 | **505** | **273** | **302** | **389** (404) | ~₹195 |
| ₹1,999 | 1.2 → 2.0 | 1,904 | 840 | 190 | 35 | 87 | 40 | 119 | 53 | **699** | **403** | **433** | **551** (566) | ~₹275 |
| ₹2,999 | 2.0 → 3.0 | 2,856 | 1,260 | 258 | 45 | 131 | 52 | 161 | 78 | **1,085** | **654** | **683** | **870** (884) | ~₹435 |
| ₹4,999 | 3.5 → 5.0 | 4,761 | 2,100 | 392 | 70 | 218 | 87 | 244 | 128 | **1,853** | **1,144** | **1,174** | **1,498** (1,514) | ~₹750 |
| ₹7,999 | 6.0 → 8.0 | 7,618 | 3,360 | 594 | 110 | 349 | 140 | 372 | 203 | **3,003** | **1,876** | **1,906** | **2,440** (2,454) | ~₹1,220 |
| ₹12,000 (SKU 8) | 10 → 13 | 11,429 | 5,040 | 930 | 180 | ~524 | — | — | — | **≈ 4,448** | **≈ 2,749** | — | **≈ 3,598** | ~₹1,800 |
**Sensitivities (blended, no COD fee):** cost 50% → ₹213 / 282 / 408 / 655 / 1,142 / 1,868 · GST 18% → ₹196 / 256 / 373 / 602 / 1,053 / 1,726 · COD RTO 20% → ₹316 / 432 / 608 / 954 / 1,638 / 2,662 · GST 0% (exempt deity) → ₹324 / 450 / 632 / 991 / 1,701 / 2,763. COD-only contribution at RTO 40%: ₹187 / 484 / 864 (for ₹1,499 / 2,999 / 4,999).
**Reading it:** (1) Shipping, not payment fees, is the largest controllable cost — and my weights/freight are assumptions; get real quotes. (2) COD earns ₹230–1,100 less than prepaid per order placed (RTO). (3) At ₹999–1,499 the break-even CAC (~₹280–390) is below what most paid-social funnels cost in India (not verified) → treat these as add-ons/gifts, not acquisition SKUs. (4) None of this includes software/app cost, returns of delivered orders, or labour.

## 18. Free shipping — validation of the working recommendation
Working rule: **free above ₹1,499 + test ₹49 COD fee + special treatment for heavy items.**
- **Holds in the model:** at ₹1,499 (0.8 kg) shipping ≈ ₹157 yet prepaid contribution is ≈ ₹505; shipping would need to reach ~₹500+ before contribution hits zero. The binding constraint is **CAC**, not shipping. ✔
- **Below ₹1,499:** charging ₹79 recovers ~₹67 of ~₹123 cost at ₹999 — keep the paid-shipping rule or bundle.
- **Heavy items:** at ₹7,999 / 6 kg shipping is ~₹594 (7.4% of price) and at 10 kg ~₹930 — fine if **priced in**; advertise "Insured delivery included" instead of "free shipping."
- **₹49 COD fee:** collects ≈ ₹42 net per COD order (~₹29 expected after RTO) — economically small; its value is behavioural. **Alternative:** prepaid incentive ₹100. At ₹2,999 the prepaid–COD gap is ₹431 per order; the ₹100 incentive costs ≈ ₹95 on every prepaid order; it pays for itself if ≥ **~22%** of would-be COD buyers switch to prepaid (model). Test both; don't lock.
- **Status:** NOT locked. Re-run when real courier/supplier rates arrive (Gate 4).

## 19. Shipping comparison (D) — evidence-limited
| Option | Evidence found | Fit | Verdict (provisional) |
|---|---|---|---|
| **Shiprocket (aggregator)** | Cached plan page: from ₹20–26 per 500 g (excl. GST; page ~3 yrs old ⚠); COD = max(% of value, flat) — values not published; blended ₹36–45/shipment claim in a review ⚠ | Multiple couriers, Shopify integration, NDR/tracking | **Primary starting route** (get dashboard quote) |
| **Delhivery** (via aggregator or direct) | No official public rate card. ⚠ 500 g ₹32 intra-city; 1 kg zones ₹65–320; COD ₹35–40 or 1.5–2%; RTO 80–100% of forward; fuel 10–18% | Widest India/PIN coverage | **Recommended courier on the aggregator; ask for direct rate card at volume** |
| **Blue Dart** | One blog: ₹200–300 for 2–3 kg ⚠ | Premium reliability claim unverified | Secondary for high-value/heavy; quote only |
| **DTDC** | One blog: ₹100–150 for 2–3 kg ⚠ | Mixed | Secondary option via aggregator |
| **Amazon Shipping / Easy Ship** | Easy Ship flat from ₹65; 2–5 kg handling ~₹80–130 — these are **Amazon-seller marketplace** fees ⚠; no evidence it serves Shopify orders | Not shown applicable | **Not recommended** until verified |
| **India Post (Speed Post)** | Est. 5 kg ₹225–540 excl. GST by distance ⚠ (my calc from a blog) | Reach into remote PINs; reliability/COD not verified | Consider only for remote PINs after verification |
| Ecom Express | Not researched; ownership/operating status not verified | — | Not recommended now |
**Parcel types (indicative, ⚠ ASSUMPTION model):** light 0.5 kg ≈ ₹55–120; medium 2 kg ≈ ₹190–260; heavy 6 kg ≈ ₹590 (model); fragile = +30% chargeable weight in my model; remote (zone E/F) 1 kg ₹150–320 ⚠ → **block COD to remote PINs, price remote shipping or decline**.
**Evidence to collect (rate-card request):** 6 lanes — Moradabad→Delhi, Jaipur→Mumbai, Jaipur→Bengaluru, Moradabad→Kolkata, →Guwahati (remote), →Leh/Srinagar (remote) — for 0.5 / 2 / 6 / 10 kg, prepaid and COD: base freight, fuel %, COD fee %, RTO %, damage/lost liability limit and insurance cost, volumetric divisor, weight-dispute policy, remittance cycle, pickup SLA.

## 20. Payment comparison (E)
| | **PayU** | **Razorpay** | **Cashfree** |
|---|---|---|---|
| Domestic cards / NB / wallets | 2% + 18% GST on fee (**official page**) | 2% + 18% GST on fee (**official page**) | 1.95%/2.0% listed (page unclear mapping) + GST |
| **UPI** | Page: P2P zero MDR; **merchant UPI rate not stated** | "2% platform fee" listed with "zero MDR" note — ambiguous | 1.95% block, but FAQ says UPI "as per applicable law" — ambiguous |
| Intl / Amex / EMI | 3% | up to 3% | 2.95–2.99% |
| Setup / AMC | none stated | ₹0 / ₹0 | ₹0 setup |
| Settlement | Standard **T+2** | **T+1** or instant (instant add-on, price not shown) | default T+2 per docs; T+1 under promo that appears expired; instant 0.30% + GST |
| Refunds | **Documented** in PayU Shopify docs: Shopify cancel can trigger refund via webhook; UPI 3–5 working days, cards 5–10 | ₹0 refund processing fee (stated) | Not extracted |
| **Shopify compatibility** | **Official docs:** hosted checkout app (cards/UPI/NB), onsite cards app, CommercePro checkout, **CommercePro COD with RTO rules**; requires KAM enablement for COD; key/salt; webhooks | Shopify app reported ⚠ (docs not opened) | Shopify plugin reported ⚠ (docs not opened) |
| **COD workflow** | **Verified** (CommercePro COD: eligibility checks, PIN/phone/amount/AI risk rules) | Not verified | Reported "COD tools" ⚠ not verified |
| Merchant requirements | KYC/KAM; **not published** | Not extracted | Not extracted |
| Documentation | Good Shopify-specific docs (read) | Not opened | Not opened (403) |
**Recommendation:** **PayU as primary — conditional**, because it is the only gateway whose *full Shopify + COD/RTO workflow* I could verify from official documentation, and its card/netbanking fee equals Razorpay's. Fee differences between the three are negligible (~₹1.5 on a ₹2,999 order for 0.05%). **Conditions (Gate 5):** PayU confirms in writing (a) merchant **UPI** rate, (b) CommercePro COD enablement for a new merchant, (c) settlement T+2 acceptable, (d) onboarding timeline. If any fails → **Razorpay** (transparent fees, T+1) is the fallback; open a Razorpay application in parallel only if PayU is slow. Note: Shopify's extra third-party fee (reported 2% on Basic) applies whichever you choose.

## 21. COD strategy (F) — simplest protective version
1. **Allow COD only for orders ≤ ₹3,999** at launch; above that, prepaid-only ("or pay 20% advance" later if demand justifies).
2. **Serviceable, non-remote PINs only** (block courier zone E/F and any PIN with no reliable delivery).
3. **Confirmation:** phone **OTP at checkout** if the COD tool provides it (PayU CommercePro mentions OTP-based flows); otherwise a **manual WhatsApp "reply YES" confirmation within 24h** for COD orders ≥ ₹1,999 before dispatch (volume is small at pilot).
4. **Price incentives:** A/B-test **₹100 prepaid incentive** vs **₹49 COD fee** (do not run both initially).
5. **Suspicious orders (manual review list, no extra app):** incomplete address, PIN/city mismatch, same phone different names, quantity ≥ 3, repeated orders to different addresses, very high value COD → call or convert to prepaid.
6. **Repeat customers:** whitelist after 1 delivered order; blacklist phone/address after 1 RTO.
7. **Kill switches:** after 30 COD orders, if RTO > 25% → drop the cap to ₹2,499 and add confirmation; if > 35% → disable COD above ₹1,999.
8. **Do not buy** a COD/checkout app until volume proves need — PayU CommercePro COD (if approved) already covers eligibility + RTO rules.
**Model sensitivity:** COD-only contribution at ₹2,999 drops from ₹654 (30% RTO) to ₹484 at 40% and rises to ₹823 at 20%.

---
# PART IV — LEGAL
## 22. GST / tax (H) — NOT settled; questions for the CA
**What I found (all secondary — official PDFs could not be read):**
- Reported: **Notification 13/2025-Central Tax (Rate), dated 17 Sep 2025, effective 22 Sep 2025** lists handicraft entries at **2.5% central tax** (⇒ 5% total with an equal state tax or 5% IGST): HSN **6802** carved stone statues/statuettes; **8306** base-metal statuettes/idols; **7419 80** brass/copper artware; **4420** wooden statuettes/ornaments (taxguru, taxheal, tax commentary). A CBIC IGST (Rate) 9/2025 PDF exists on courier.cbic.gov.in but I could not read the entries.
- Reported: **marble/wooden deities** — a Rajasthan AAR (30 Jul 2026) says the central-tax exemption on **actual deities/murtis** applies from 22 Sep 2025 (Chapters 44/68); **decorative statues that are not deities may not qualify**. Source notification numbers conflict across sites (9/2025, 10/2025).
- Older/other listings still show 12% or 18% (e.g., plated statuettes 18%) — likely outdated or different items.
- **Resin / polyresin / marble-composite:** I found **no** reliable classification (could be plastics 3926 or other heads; rate unknown).
| Product | Status |
|---|---|
| Brass idols/statues | Reported 5% (HSN 8306/7419) — unconfirmed |
| Marble | Reported exemption for deities; 5% for other carved stone — unconfirmed |
| Wood | Same pattern — unconfirmed |
| Resin/composite | **Unknown** |
| Decorative artefacts | Reported 5% for listed handicrafts; condition/definition unclear |
| Religious-use products (lamps, bells, thalis, incense) | Not researched |
**Questions for the CA (do not treat as answered):**
1. HSN code and GST rate for each pilot SKU (brass idol, painted brass, polyresin, marble-composite, real-marble deity, decorative figure, diya/bell/thali).
2. Does the 5% (or exemption) depend on being "handicraft/made predominantly by hand" or the seller being registered? How do I evidence it (supplier declaration)?
3. If I sell exempt deities and 5% items together: registration, ITC treatment, invoice formats.
4. Resin/polyresin and marble-powder composites: correct HSN and rate.
5. **Do I need GST registration from day one** as a dropshipper selling inter-state via my own site? (Threshold ₹40 lakh for goods in most states, but inter-state supply and certain categories change this; Notification 34/2023-CT conditions.)
6. Dropship invoicing: supplier invoices me with *ship-to = my customer* — is "bill-to/ship-to" valid? Who raises the tax invoice to the customer and from which state? Place-of-supply consequences?
7. Input tax credit on supplier invoices if supplier is unregistered/composition.
8. Do payment gateway or courier settlements trigger **TCS/TDS** for me? Is the gateway an "e-commerce operator"?
9. COD collections: GST treatment and courier COD remittance accounting.
10. Shipping charges and COD fees: GST rate and whether "free shipping" affects the value of supply.
11. Returns/refunds/credit notes for exempt vs taxable items.
12. Composition scheme eligibility (if any) for an e-commerce seller.
13. E-way bill triggers for heavy marble consignments.
14. MSME/Udyam, entity type (proprietorship vs LLP/Pvt Ltd) trade-offs for a brand you want to trademark.
15. Legal Metrology declarations (net quantity/dimensions) for imported/packaged goods; who is "manufacturer/packer" label-wise in dropship?
16. Consumer Protection (E-Commerce) Rules — disclosures I must show (country of origin, seller name, grievance officer) and applicability to a dropship store.
17. DPDP Act/Rules 2025 (notified 13 Nov 2025; main duties ~May 2027 ⚠): notice/consent wording for WhatsApp marketing.
18. Any restriction/licensing for selling religious articles or for ivory/animal-material look-alikes (e.g., ensure no actual restricted materials).

## 23. Trademark (I) — not cleared
**Findings (secondary):** a third-party register aggregator (registerkaro.in) lists **WAVES OF VRINDAVAN** filings — word marks and device marks in **Classes 35, 41, 43**, filed 2 Aug 2026 in Delhi by a Jalandhar partnership (applications 7900780–7900785); I found **no VRINDAVAN-only mark in Classes 14, 20, 21** in those results. **Absence from a search aggregator is not clearance** — it indexes selectively and lags the register.
**Official source:** IP India — https://ipindia.gov.in/ → *Trade Marks → Public Search* (tmrsearch.ipindia.gov.in). I have **not** run it.
**What to search (free, do now):** word mark "VRINDAVAN" with phonetic/similar options; variants **VRINDABAN, BRINDAVAN, BRINDABAN, VRUNDAVAN, VRINDAVANA, VRINDA, VRINDHAVAN**; plus device-mark (Vienna) searches for peacock feather/flute/temple-arch logos. **Classes to consider with an attorney (Nice, to confirm):** **35** (online retail of idols/décor — core for a reseller), **6** (statues/figurines of common metal), **19** (statues of stone/marble), **20** (statues of wood/wax/plaster/plastic — resin), **21** (ornaments of porcelain/terracotta/glass), **14** (statuettes of precious metal, if ever), **11/4** (lamps/candles if added), **24/25** only if textiles/apparel.
**Risks to ask the attorney about:** (a) "Vrindavan" is a **place name** — distinctiveness/geographical-descriptiveness objections and a likely crowded register; (b) **device mark** — the emblem is a Krishna-iconography composition; check conflicts with existing temple/trust marks; (c) **logo provenance:** I cannot tell how the logo files were produced; if an AI image generator was used, confirm the tool's commercial-use terms, registrability and originality (and consider a vector redraw by a designer); (d) timing: register before heavy ad spend; you may use "TM" while pending.
**Do not claim legal clearance** until a professional search report is in hand.

## 24. Logo (K) — options and what to do NOW
| Option | Description | Pros | Cons |
|---|---|---|---|
| **A** | Current logo set unchanged, used everywhere | no cost, consistent with approval | emblem is Krishna-specific; detailed; embossed look at small sizes |
| **B (recommended now)** | **Wordmark-first system; emblem secondary** (header = wordmark; emblem = footer, packaging, 404, social avatar). Add flat (SVG, one-colour) wordmark + favicon derivative from the existing files. No redesign. | prominence of the wordmark as you asked; the wordmark has no Krishna iconography; lotus divider is pan-devotional; minimal spend | still the name "Vrindavan" leans Krishna |
| **C** | Future neutral brand symbol (e.g., arch + lotus) | works for all deities | costs time/money; breaks equity; premature |
**Recommend B now.** Triggers to revisit C: (1) non-Krishna SKUs exceed ~50% of orders; (2) interviews show non-Krishna devotees feel the brand "isn't for them"; (3) trademark advice says the emblem is risky. Use emblem 2 (circle) only for Krishna-centric surfaces (social avatar, a "Krishna" collection banner); never on Shiva/Hanuman/Durga product pages. **Do not redesign yet.**

## 25. Provisional design system (J) — "Quiet Mandir" v0 (not locked; Gate 8)
- **Colour & type:** §3–§4. **Spacing:** 4px base; 16px side gutter at 360–430px; section spacing 48 (mobile) / 80 (desktop); content max 1200px; touch targets ≥ 48px.
- **Buttons:** primary = `--maroon` fill, ivory text, 48px high, 4px radius, medium weight, full-width on mobile; secondary = 1px `--ink` outline; tertiary = brass-underlined text link; disabled = sandstone; focus ring = 2px `--brass-deep` offset 2px. No gradients, no shadows beyond 1px.
- **Cards:** borderless, image-led, 4:5 image, 8px radius (arch crop only for deity tiles/hero), name 2 lines max + material·height line, price, rating only if ≥ 3 real reviews; no sale ribbon unless a real markdown with a genuine previous price.
- **Navigation:** minimal; ≤ 5 items; full-screen mobile menu with arch deity tiles; search prominent.
- **Mobile header (56px):** menu icon left, **wordmark centred at ~120–130px wide**, search + cart right; **no tab bar at launch** (sticky Add to Cart owns the bottom on PDP); no announcement bar unless delivery/COD info is true and ≤ 1 line.
- **Desktop header:** wordmark centred (~170px), nav left, search/account/cart right, 1px brass hairline below; no mega-menu.
- **Product gallery (mobile):** full-width 4:5, swipe with dot count and **next image peeking**, tap-to-zoom; order = hero idol → scale/in-situ → macro face/hands → back/base → short video (hero SKUs only). Warm radial glow behind the idol on PDP.
- **Buy box:** title (deity · form · material · height), price incl. GST, delivery pill/PIN check, variant chips (size/finish), **sticky Add to Cart (maroon)** + secondary "Buy now"; payment line "UPI · Cards · COD available (see terms)"; trust trio; accordions: *Story · Details (museum label) · Care · Shipping & Returns*.
- **Collection layout:** 2-column grid on phone, **bottom Sort/Filter pill** → bottom-sheet filters (deity, material, height, price, use); count + breadcrumb; consistent card title template.
- **Footer:** `--sanctum` background, emblem 1 mono (brass), jali tint 4–6%, lotus divider, policies, grievance contact, WhatsApp/email.
- **Accessibility/performance:** AA contrast (table above), `prefers-reduced-motion`, ≤ 1 hero image (LCP), AVIF/WebP, ≤ 2 font families, devotional details ≤ 5 KB total.

## 26. Mobile journey notes (390/412px)
HOME (arch hero + deity tiles, LCP-safe) → COLLECTION (bottom sort/filter pill, 2-col) → **PRODUCT (most carefully designed)**: gallery peek, spec "museum label", PIN-code check, sticky ATC, accordions, honest delivery text, COD messaging as a plain line near price ("COD available · ₹49 handling" only once the fee decision is made), reviews only when real → CART (slide-up sheet; shows delivery estimate, prepaid incentive line, note field for gift message; one optional add-on max) → CHECKOUT (Shopify checkout; PIN-first address, phone required, UPI first; checkout branding is limited by plan — verify what Basic allows before promising styling) → ORDER (confirmation + WhatsApp opt-in (opt-in required), tracking link, order-status page). Nothing devotional appears inside forms/checkout.

---
# PART V — GATES, ACTIONS
## 27. Validation gates (K)
| Gate | Pass criteria | Evidence | Status |
|---|---|---|---|
| **1 Supplier** | ≥ 1 credible fulfilment route: written confirmation of single-order dispatch, packing method, damage replacement, GSTIN verified | replies + GST portal check | **OPEN** — leads only; Baapstore partially verified (model) |
| **2 Product** | ≥ 5 of 8 SKUs pass §16; 0 critical defects; 0 breakage | scorecards + photos | **OPEN** |
| **3 Economics** | Real landed cost ≤ 42–45%; blended contribution ≥ 30%/20% | updated §17 | **OPEN** |
| **4 Shipping** | Real rate card (6 lanes × 4 weights, COD/prepaid); pilot delivery data | rate cards + AWB logs | **OPEN** |
| **5 Payment** | Gateway chosen with written fees incl. UPI, COD enablement, settlement | PayU/Razorpay written replies | **OPEN** (PayU conditional) |
| **6 COD** | Rules defined; pilot COD RTO ≤ 25% at launch cap | pilot data | **OPEN** |
| **7 Legal** | CA answers critical items (GST registration/rates, invoicing); trademark search done + attorney view | CA memo, search report | **OPEN** |
| **8 Brand** | 3 static mockups with real photos pass recognition/trust test; type specimens tested on Android | test notes | **OPEN** |
**Only after Gates 1–8:** Shopify architecture. Not before.

## 28. Exact actions for you (L), in order
1. **Trademark (free, today):** run the IP India public search for VRINDAVAN + variants (§23); save screenshots. Book a short IP-attorney consult.
2. **GST/CA:** send §22 questions to a CA; ask them to confirm registration need and the rate/HSN for 8 SKUs.
3. **Supplier outreach:** send Stage 1 messages to ~12 suppliers (4 Moradabad brass: Kamal, AYC + 2 more; 3 resin/composite: Arham, Bemount, one more; 3 Jaipur marble: Harihar, Jaipur Marble Emporium, Icones; Baapstore; Stone Studio). Verify each GSTIN on the official GST portal first. Log replies in the scorecard.
4. **Courier & gateway quotes:** open a Shiprocket (or similar) seller account *to see the rate calculator only* (no commitment) and request Delhivery/Blue Dart rate cards; ask PayU (and Razorpay as fallback) for the written items in §20. *(Creating accounts/sharing KYC is your call — I will not do it.)*
5. **Logo assets:** ask the designer for SVG/high-res masters, a flat one-colour wordmark, a favicon derivative, and confirmation of how the logo was produced and who owns it.
6. **Pilot SKUs:** from responders, pick suppliers, order samples for SKUs 1–7 (SKU 8 as quote/photo/video first).
7. **Review:** send me replies/photos/quotes; I rerun §17 and the scorecards. Then we run Gate 8 mockups.

## 29. Open items I need back from you
Supplier replies and sample photos · rate cards · gateway written quotes · CA memo · trademark search screenshots · logo masters and provenance · any budget limits for samples (SKU 8 especially) · a Hindi-reading reviewer for Devanagari strings.

## Sources
- Shopify Help — Shopify Payments supported countries (India not listed): https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries
- PayU Shopify docs: https://docs.payu.in/docs/shopify-faqs · PayU pricing: http://payu.in/pricing/
- Razorpay pricing: https://razorpay.com/pricing/ · Cashfree charges: https://www.cashfree.com/payment-gateway-charges
- Baapstore: https://www.baapstore.com/ · https://www.baapstore.com/pages/pricing
- The Stone Studio wholesale: https://www.thestonestudio.in/wholesale/
- IndiaMART listings (self-reported): Kamal Metals https://www.indiamart.com/kamalmetals-moradabad/ · AYC Metals https://www.indiamart.com/yaqub-handicrafts/products-and-services.html · Arham Trades https://m.indiamart.com/arhamtrades/testimonial.html · Bemount https://m.indiamart.com/bemountcreations/profile.html · Keshav Arts https://m.indiamart.com/keshavarts · Harihar https://m.indiamart.com/hariharmurtibhandar/profile.html · Icones https://m.indiamart.com/iskcon-moorti-creation · Jaipur Marble Emporium https://m.indiamart.com/jaipurmarbleemporium/
- GST (secondary): https://taxguru.in/goods-and-service-tax/gst-rates-handicrafts-jewellery-artware-revised-22-sept-2025.html · https://www.taxscan.in/top-stories/marble-wooden-deities-eligible-for-gst-exemption-exemption-restricted-to-actual-idolsmurtis-aar-read-order-1451395 · CBIC IGST 9/2025 PDF (unread): https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf
- Courier/rates (secondary ⚠): https://www.clickpost.ai/blog/delhivery-courier-charges · https://www.shiprocket.in/blog/delhivery-courier-charges/ · https://www.shiprocket.in/price-compare/ · https://www.icarry.in/pages/blog/amazon-seller-shipping-india.html · https://www.clickpost.ai/blog/india-post-courier-charges
- COD/RTO (vendor): https://base.com/en-IN/blog/cod-return-rates-by-product-category-in-india-2026-report/
- Trademark (aggregator): https://www.registerkaro.in/trademark-search/waves-of-vrindavan-7900781 · Official: https://ipindia.gov.in/
- Temple architecture: https://en.wikipedia.org/wiki/Hindu_temple_architecture · https://en.wikipedia.org/wiki/Garbhagriha · https://www.sanskritimagazine.com/the-symbolism-of-hindu-temple-architecture-a-sacred-science/
- Design/trade commentary: https://thedesignpeople.in/beyond-tradition-indias-spiritual-market/ · https://confetti.design/blog/ayurvedic-packaging-design · https://medium.com/@balajishekar87/godavari-rediscovering-the-art-of-branding-through-tradition-8532a43027dd
- Colour symbolism (blogs ⚠): https://www.gktoday.in/colour-symbolism-in-indian-culture-and-festivals/ · https://www.azafashions.com/blog/the-colors-of-india-symbolism-in-fashion-and-culture/
- Real Indian references opened at 390px: srimandir.com, cycle.in, nicobar.com, amrapalijewels.com, goodearth.in, kamaayurveda.com, exoticindiaart.in, thestonestudio.in
- Fonts: https://fonts.google.com/specimen/Tiro+Devanagari+Hindi (existence only)
