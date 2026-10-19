# VRINDAVAN — Phase 0 Discovery Report (v0.1)
Date: 2026-10-08 · Status: DISCOVERY ONLY. Nothing built, bought, installed or connected.

## 0. Read this first: research limits (honest scope)
- **Logo NOT received.** I found no VRINDAVAN logo in this session's folder or in the folders I checked. Section 2 therefore contains no logo analysis. Please re-attach it.
- **Competitor review was text/markup-level.** I fetched all 14 sites as extracted text. I could not judge photography quality, colour, type, motion or real mobile feel. A visual, phone-width pass in the browser is still needed (proposed as Step 1b).
- **Creative references are thin.** Only The Citizenry and Mejuri were read in detail; Aesop returned 403; Awwwards was only skimmed through search results (names, not inspected). Treat section 4 as seeds, not a finished inspiration board.
- **Supplier research found no verified dropship-capable idol supplier.** Results were B2B listings and forum threads. Ranking in section 11 is by *approach*, not by named, verified vendor.
- **Many facts below come from secondary sources** (vendor blogs, law-firm summaries). Items marked ⚠ must be verified against an official source before any decision.

---
## 1. Executive summary
1. The Indian idol/artefact category is visually weak and trust-weak: blanket "Sale" badges, 40–78% fake-looking discounts, keyword-stuffed titles, broken countdowns, no reviews, sold-out items shown as buyable, inconsistent sizes. **The opportunity is not "better religious store" — it is credibility, restraint and product truth.**
2. Recommended direction: **"Quiet devotional gallery"** — calm, editorial, product-as-sculpture, real dimensions/weights/finish, honest pricing (no permanent sale), named material and origin.
3. **Biggest business risk is not design — it is pure dropshipping fragile goods (brass/stone/resin) with a 7-day promise and free shipping.** Damage, supplier inconsistency, no QC and COD RTO can erase margin. I recommend a *stock-light hybrid*: sample-test suppliers, then hold small stock of the top ~10 SKUs once validated.
4. **Do not promise "7 days" publicly** until 20+ real test shipments prove it.
5. Platform: Shopify Basic + a free Horizon-family or Online Store 2.0 theme customised lightly. **PayU is workable (UPI via hosted app; COD via CommercePro) but is probably not the best primary choice** — see §24.
6. Blocking decision: **supplier model + logo + business registration**. No design build should start before the first two are settled.

---
## 2. Brand analysis
- Logo analysis: **cannot be done — file not received.** Your brief describes gold tones, peacock feather, Krishna/flute and temple architecture; if accurate, the logo is dense and ornamental. My working hypothesis (to be validated against the file): keep the logo as the single ornamental element on the site; the rest of the UI stays flat, neutral and typographic, so the logo and products never compete with decoration.
- Name: "Vrindavan" is a place-name with strong Krishna/devotional resonance. It supports a Krishna-leaning hero story but could under-signal Shiva/Ganesha/Durga buyers. ⚠ Check trademark/name conflicts (Vrindavan is widely used) — a qualified professional should run this.

## 3. Web design research (what I could verify)
- Shopify's current theme family is **Horizon** (free, block-based, web-component architecture; launched Summer '25 Edition per most sources). Block flexibility helps; app compatibility with Shadow-DOM components can be an issue. Sources: Shopify theme store; CraftShift; ecommerce-platforms.com (secondary).
- Home-décor conversion is structurally low (high AOV, long consideration). Patterns that help: scaled lifestyle imagery, dimension-aware presentation, instalments/EMI, showroom-style PDPs (Fudge.ai, secondary).
- Awwwards e-commerce honourees in 2026 (names only, not inspected): Bucks Sauce, Outfit, Pixel Vault, Drop Edition, Gielly Green, LAB46. Awwwards-style motion-heavy builds are generally **bad fits for budget Android**; used only as idea sources.

## 4. Best creative ideas discovered (filtered by the five-question test)
| Idea | Source | Improves shopping? | Perf risk | Verdict |
|---|---|---|---|---|
| Origin as chapter ("Moradabad · Brass", "Swamimalai · Bronze") with a one-line sensory description | The Citizenry (country modules) | Yes – provenance trust | Low | **Adopt** |
| Named third-party proof in its own block (not generic badges) | The Citizenry (Fair Trade), Mejuri (traceable gold) | Yes | Low | **Adopt** only if we have real proof (e.g. hallmark/lab-tested brass purity) |
| Multiple entry paths: by deity, by room/use (pooja room, desk, car), by occasion, by price | Citizenry, Exotic India | Yes | Low | **Adopt** (as filters + 4 homepage tiles) |
| Single-word image tiles for categories | Citizenry | Yes – less load | Low | **Adopt** |
| Footer as help hub; policy summary near purchase | Citizenry, Mejuri | Yes | Low | **Adopt**, plus summary on PDP |
| Verb-led single CTA per module; pause control on any carousel | Mejuri | Yes / a11y | Low | Adopt; avoid carousels in hero |
| Scale reference photo (hand / shelf / pooja unit) | Home-décor PDPs | Yes – cuts "height" complaints (seen in Vedansh reviews) | Low | **Adopt – mandatory** |
| Short product video (5–8 s turntable/light sweep) | Premium décor | Moderate | Medium (mp4, poster, lazy) | Adopt on hero SKUs only |
| 360° viewer | — | Marginal | High JS | **Reject for MVP** |
| Scroll-jacked storytelling, WebGL, cursor effects | Awwwards-type | No | High | **Reject** |
| Visual search (camera icon, Vaaree) | Vaaree | Unproven | Medium | Reject |
| Countdown timers | Vaaree/Swaba/Exotic | Hurts trust when broken/fake | Low | **Reject** |

## 5. Competitor analysis (14 sites; text-level evidence)
Common failures across the set: perpetual sale badges (StatueStudio, Cut n Curve, Stone Studio, Exotic India, Luxe), inflated strike-through prices of 61–78% (Swaba) and wrong discount arithmetic (Exotic India), titles stuffed with keywords and inconsistent units, no/thin reviews, broken UX artifacts (expired timers, "0+" counters, "Translation missing", "₹0.00" placeholders, hero CTAs pointing to wrong collections), mega-menus with 50–100+ overlapping links, sold-out items shown with Add to cart (Artarium).

| Site | Positioning | Works | Doesn't / avoid | Learn |
|---|---|---|---|---|
| StatueStudio | Decor + spiritual + gifting | Clear 5-category IA, free-shipping/tax note in cart, a11y skip links | Sale on ~everything, no reviews, thin hero | Clear IA and tax-inclusive messaging |
| Satvik Store | Brass specialist, 400+ items | Size-first titles, sold-out states, festival merchandising | Unproven "No.1" claims, no facets, truncated titles, "metal" vs "brass" | Size in a structured field, not title |
| eCraftIndia | Mass idols & figurines | Sub-category tiles, sitewide offer + prepaid nudge | Machine-written SEO copy, duplicate taxonomy, 5.0 from 1 review | Prepaid incentive visible in cart |
| Jaypore | Curated Indian lifestyle | (page content not retrievable) | — | Needs visual review |
| Exotic India Art | Heritage / lost-wax / 30 yrs | Showrooms, "Find your deity", "Shop by occasion", insured shipping | Duplicate routes (4 to Ganesha), no search visible, fake-feeling counters | Deity + occasion entry points |
| Swaba Handicraft | Discount décor | Simple nav | Fake urgency, 70% off, repetitive titles | Avoid entirely |
| VedanshCraft | Brass/pooja one-stop | Named testimonials w/ cities, WhatsApp bulk, accessibility toolbar | "0+" counters, stacked discounts, placeholder ₹0.00 | Named, balanced reviews |
| Luxe Artisanship | Brass, finish-based nav | Finish-based categories, COD + 7-day return + wishlist | Dead nav items, duplicated blocks, unclear copy | Navigate by finish/material |
| Artarium | Idols + car dashboard | Variant photography, scale-in-car shots | Catalogue looks "sold out", dup logo/search | Context-of-use photos |
| Krafteria | Regional crafts | Provenance (Tanjore, Nirmal…), price-band nav, notify-me, wishlist | Broad catalogue, duplicate sections | Regional provenance + price bands |
| Vaaree | Premium trendy home | Material label on cards, "From ₹" pricing, order tracking link | Banner walls, overlapping taxonomy, icon-only utilities | Material on card |
| Veda Connection | Gifting-led idols | Occasion gifting, WhatsApp bulk | Fake-looking trust badge, truncated descriptions | Gift-by-occasion |
| Cut n Curve | Composite-marble statues | 144 named reviews incl. packaging comments, marketplace presence | Wrong hero links, size mismatches title/URL | Reviews that mention packaging |
| The Stone Studio | Large stone statues | Founder note, placement stories, quote path | Watermarked images, "sdsdsd" alt text, no quote CTA | Founder voice + placement stories |

**Whitespace:** none of the 13 readable sites combines (a) calm editorial design, (b) honest pricing, (c) structured specs, (d) real reviews with packaging feedback, and (e) clear delivery/COD/returns at the buy box. That is VRINDAVAN's position.

## 6. What VRINDAVAN should be
Quiet. Specific. Verifiable. A small, curated "gallery" of devotional objects; every product photographed on one consistent neutral set; every product page answering size/weight/material/finish/delivery/returns in two seconds on a phone; prices that are stable and honest.

## 7. What VRINDAVAN should not be
No sitewide sale badges; no countdowns; no fake scarcity or "X people viewing"; no "India's No.1" claims; no 70%-off strike-throughs; no mega-menu; no carousel hero; no stock "artisan" photos; no scroll-jacking; no ornamental borders/mandalas on UI chrome; no more than 2–3 apps in MVP.

## 8. Target customer (hypotheses to validate)
1. **Home-pooja buyer** (28–55, mobile, UPI/COD, buys Ganesha/Lakshmi/Krishna/Hanuman; festival-driven, Dhanteras/Diwali/Navratri). 2. **Gift buyer** (housewarming, wedding, corporate; wants packaging and a guaranteed arrival date). 3. **Décor-leaning urban buyer** (Buddha, abstract/minimal deity forms, desk/shelf pieces). 4. **Diaspora gifting** — out of scope (India-only).
Validate with 8–10 customer interviews and search-term data before locking categories.

## 9. Product strategy
- 15–30 SKUs at launch, not hundreds. Each SKU must have: real sample inspected, own photography (or supplier raw photos re-shot after sample arrival), measured dimensions/weight, packaging test (drop test), price sanity check vs §12.
- Price bands to test: ₹999–1,999 (gift/entry), ₹2,500–5,999 (core), ₹7,000–15,000 (showpiece). Competitor observed bands: ₹299–3,000 (eCraft), ₹1,000–5,000 (Veda/Vedansh), ₹3,000–25,000 (StatueStudio, Cut n Curve), up to ₹2.5 lakh (Stone Studio).
- ⚠ Avoid fragile large stone/marble in MVP (damage + freight).

## 10. Category strategy (proposal, 4 collections)
1. **Ganesha & Lakshmi** (Diwali/pooja core, highest search demand — verify with Keyword Planner).
2. **Krishna & Radha** (brand-aligned with the name).
3. **Shiva, Hanuman & Durga**.
4. **Buddha & Décor Pieces** (urban/gift).
Optional 5th later: Pooja essentials (lamps, thalis) — low price, low margin, good AOV add-on but dilutes premium; defer.
Cross-cutting filters, not extra collections: material, finish, height, use (pooja room / desk / car / gift), price.

## 11. Supplier research
**Finding: I could not verify any Indian supplier that formally offers a dropship programme with API/inventory sync for idols.** Evidence found was B2B listings (IndiaMART/TradeIndia/GlobalLinker: Moradabad, Aligarh, Ahmedabad; MOQs like 70 pcs or 1 kg), a Shopify forum thread suggesting GlowRoad (unverified), and Exotic India's dropship URL returning 404.

Ranked by *approach* (fitness for VRINDAVAN):
| Rank | Approach | Pros | Cons / risks | Verify |
|---|---|---|---|---|
| 1 | **Direct manufacturers/workshops (Moradabad, Jaipur, Swamimalai, Aligarh) – negotiated small-batch + per-order dispatch** | Best price, customisation, white-label packaging possible | Manual orders, MOQ, quality variance | Sample, GST invoice, packaging, dispatch SLA, damage policy |
| 2 | **Established online retailers with wholesale/B2B desk (e.g. Exotic India "Wholesale", Cut n Curve, Veda Connection)** | Better QC, brand-level consistency | Likely not true dropship; may not white-label; competitor conflict | Ask in writing |
| 3 | **Stock-light hybrid: buy 3–10 units of validated SKUs, ship via Shiprocket/Delhivery** | Controls QC, delivery time, branded packing, enables COD verification | Capital, storage | Needs a fulfilment address |
| 4 | Dropship platforms/apps (GlowRoad etc.) | Fast to start | Quality, branding and reliability unverified | Everything |
| 5 | Marketplace sourcing (Meesho etc.) | Cheap | No QC, no branding, customer may see same item cheaper | Avoid |

Supplier scorecard to use for each candidate (all unknown today): quality (sample), cost, shipping cost & carrier, dispatch SLA, COD support, order channel (API/CSV/WhatsApp), inventory sync, tracking sync, returns/damage replacement, branding/white-label, MOQ, GST invoice, reliability references.

## 12. Unit economics model (ILLUSTRATIVE — every input is an assumption to replace with real quotes)
Assumptions: product 8" brass Ganesha sold at ₹2,999 incl. GST; GST 18% ⚠ (HSN/rate unverified); supplier cost ₹1,350 ex-GST; free shipping, ~₹110 forward; Shopify Basic third-party fee 2% ⚠ (secondary); gateway ~2%+GST ⚠; COD courier fee ~₹45; RTO (COD) 30% ⚠ (vendor benchmarks: home & kitchen 30–38%); RTO cost ₹250 (forward + return + packing); prepaid damage/return 7%, ~₹560 loss each; apps ₹60/order.

| | Prepaid | COD |
|---|---|---|
| Revenue ex-GST (2,999/1.18) | 2,541 | 2,541 |
| Supplier cost | −1,350 | −1,350 |
| Shipping (free) | −110 | −110 |
| Payment/transaction fees | −131 | −45 (COD fee; ⚠ confirm no Shopify fee on manual methods) |
| Contribution if delivered | 950 | 1,036 |
| Expected returns / RTO | −39 | −(0.30×250)=−75 and 30% of orders earn nothing |
| Apps/software | −60 | −60 |
| **Contribution per order placed (pre-ads)** | **≈ ₹850** | **≈ ₹590** (0.70×1,036 − 75 − 60) |

- Blended (50% COD): ≈ ₹720 per order. **Max break-even CAC ≈ ₹720; target CAC ≤ ~₹360.**
- Supplier cost/price ratio here is 45%. **Rule of thumb: supplier cost ≤ ~40–45% of GST-inclusive price.**
- **Free shipping viability:** at ₹1,299 with ₹600 cost, contribution is only ≈ ₹250 prepaid → free shipping is *not* viable below ~₹1,500 unless cost ratio ≤ 40% or a threshold is used.
- **Max discount:** a 5% prepaid discount (₹150 ≈ ₹127 ex-GST) is affordable at the ₹2,999 level; deeper blanket discounts are not.
- **COD risk:** COD loses ~₹260 per order vs prepaid in this model and carries RTO noise; the lever is COD→prepaid nudges (case studies report large shifts but are single, vendor-reported) and pin-code/risk rules.
- The model ignores: marketing creative, returns of delivered COD, supplier damage chargebacks, GST ITC specifics, courier weight slabs (brass is heavy – shipping may be ₹150–300 for 2–3 kg; **this could break the model**).

## 13. Shopify architecture (native vs custom vs app vs external)
| Need | Choice |
|---|---|
| Storefront | Native theme (Horizon/OS2.0 free theme), light custom sections |
| Product data | **Native metafields** (height, weight, material, finish, base type, care, origin) + metaobjects for Deity/Material/Artisan-region pages |
| Collections/filters | Native collections + Shopify Search & Discovery (filters, synonyms) |
| Customer accounts | Native "new customer accounts" (passwordless OTP code; Google/Facebook/Apple/Shop sign-in available; Google needs your own Google Cloud credentials) ⚠ secondary sources |
| Wishlist | Evaluate native-adjacent lightweight app *or* localStorage wishlist in theme (zero apps) — decide later |
| Reviews | Shopify's free Product Reviews or a light reviews app (see §32) |
| Discounts/coupons | Native discounts |
| Shipping | Native shipping rates (free) + carrier aggregator for tracking |
| Notifications | Native email; WhatsApp via aggregator/gateway later |
| Payments | Third-party (Shopify Payments isn't available in India ⚠) |
| COD | App (PayU CommercePro COD, GoKwik, or similar) — native manual COD is basic |
| Analytics | GA4 + Meta + Shopify analytics via Google & YouTube/Facebook channels |
| Referral | **Defer** — not commercially useful before repeat purchase data |
Plan/cost (⚠ secondary): Basic ≈ ₹1,499/mo billed yearly + 18% GST; 2% third-party transaction fee on Basic, 1% Grow, ~0.6% Advanced. Grow beats Basic only above roughly ₹4 lakh/month revenue.

## 14. Site map (only pages with real value)
Home · Shop all · Collections (4) · Product · Search · Cart · Checkout · Account (login, orders, addresses) · Wishlist · **Track order** (courier link page + Shopify order status) · About/Our story (short) · Our craft (materials, how it's made, care) · Gift guide · Festival edit (seasonal, evergreen URL) · Contact (WhatsApp/email/phone, grievance officer) · FAQ · Shipping policy · Returns & refunds · Privacy · Terms · 404.
Skip at launch: blog, referral page, separate "Our Craft" if no real content.

## 15. Mobile UX strategy (primary)
- Design widths 360/375/390/412/430; one-hand reach; bottom tab bar (Home · Shop · Search · Wishlist · Cart) only if it tests better than a simple header; sticky Add-to-cart on PDP; filter/sort as bottom sheet; horizontal rails limited to 2 per page; image gallery swipe with dot count and pinch zoom; no autoplay carousel; address form with PIN-code autofill (city/state), OTP phone login; WhatsApp support button (not a floating widget that covers the CTA).
- Budget: LCP < 2.5s on mid-range Android 4G; total JS as small as possible; ≤ 1 web font family with 2 weights, `font-display: swap`.

## 16. Desktop UX strategy
Not a scaled phone: 12-col editorial grid, 2-up PDP (gallery left, sticky buy box right), larger imagery, split hero (image + calm text), hover swap only for secondary image, mega-menu avoided (simple 4-collection nav + search).

## 17. Homepage concept (mobile order)
1. Slim announcement (shipping/COD only if true).
2. Hero: one product-as-sculpture image, one-line promise, one CTA ("Shop Ganesha & Lakshmi" or season-led).
3. 4 category tiles (single-word labels, product imagery).
4. Bestsellers rail (6 items) with price, rating if real.
5. "Why VRINDAVAN": 3 verifiable commitments (inspected before dispatch, secure packaging, clear returns) — only if operationally real.
6. Shop by use / occasion (pooja room, gifting, festival).
7. Craft story (short, real photos).
8. Reviews (real, named, with city).
9. FAQ strip + footer help hub.

## 18. Collection page concept
Large 2-column grid on phone; card = image, short name (e.g. "Ganesha · Brass · 8 in"), price, rating (only if ≥ 3 reviews); filter bottom-sheet: height, material, finish, use, price; sort; no sale badges unless real compare-at; structured card title format `Deity — Material, Height`.

## 19. Product page concept (priority order)
1. Gallery (hero on neutral set → scale reference → detail/texture → in-situ → short video) 
2. Title, rating (real), price (incl. GST), compare-at only if genuinely previously sold at it 
3. Variant (size/finish) as chips, with dimension per variant 
4. **Delivery, COD, returns mini-block at buy box** (PIN-code check, estimated delivery range once validated) 
5. Sticky Add to cart / Buy now 
6. Spec table (height, width, weight, material, finish, base) 
7. Story/meaning (short, respectful) 
8. Care & placement (Vastu mention optional, factual) 
9. Reviews (with photos) 
10. FAQ (2–4 relevant) 
11. Related ("Complete the pooja corner"), recently viewed.
Excluded for MVP: 360°, AR, bundles builders, urgency widgets.

## 20. Cart concept
Slide-out cart on desktop, full-page-like drawer on phone; free-shipping line only if applicable; prepaid incentive line ("Pay online, save ₹X"); trust (secure payment, returns); note field for gift message; no upsell clutter (max 1 add-on, e.g. small lamp).

## 21. Checkout strategy
Use Shopify checkout (fast, trusted; customisation limited by plan). Address: PIN-first. Phone required (WhatsApp updates need opt-in). UPI first in payment order. COD behind eligibility rules (PIN/amount/risk) with phone OTP or WhatsApp confirmation. Evaluate third-party one-click checkout (GoKwik / Shiprocket Fastrr) only after baseline conversion is measured; they're quoted as % of GMV and add dependency.

## 22. Brand/design system (proposal pending logo)
- Palette: warm ivory background, deep ink text, one muted saffron-brass accent (sampled from logo gold, used sparingly), one deep green/peacock-blue for links/focus. Contrast AA minimum.
- Type: one serif display (e.g. an elegant variable serif with Devanagari support option) + one clean sans for UI; no more than 2 families, subset, self-hosted.
- Imagery: soft neutral set (warm grey/stone), consistent lighting, shadows grounded; one lifestyle shot per SKU.
- Components: restrained (no ornamental borders), 8-pt spacing, 44px touch targets, motion only for feedback (≤200ms) and respects `prefers-reduced-motion`.
- Logo use: leave untouched; clear space = height of flute-top; use mono version on dark.

## 23. Product content model (Shopify metafields)
`custom.deity` (metaobject) · `custom.material` · `custom.finish` · `custom.height_in/width_in` · `custom.weight_g` · `custom.base_included` · `custom.origin_region` · `custom.care` · `custom.story_short` · `custom.use_cases` (list) · `custom.occasions` (list) · `custom.packaging_notes` · `custom.hsn_code` · `custom.supplier_ref` (private, not on storefront) · `custom.lead_time_days`. Metaobjects: Deity, Material, Region/Artisan, FAQ.

## 24. Payment strategy
- Verified (PayU docs): PayU has separate Shopify apps — "Cards, UPI, NB" (hosted checkout, UPI supported), "Onsite Card Payments" (cards only, no UPI), CommercePro Checkout, **CommercePro COD** (eligibility + RTO controls, requires PayU enabling via KAM). Refunds: cancelling in Shopify can trigger PayU refund via webhook; UPI refunds 3–5 working days. Fees/limits are not on the page — ask PayU.
- **Challenge:** the PayU route uses a hosted redirect, requires KAM enablement and multiple apps; Razorpay and Cashfree are widely cited as the more common Shopify-India choices (secondary). Recommendation: **get quotes from PayU, Razorpay and Cashfree** and choose on MDR, settlement time, UPI success rate, COD tooling and onboarding speed — PayU stays acceptable if COD CommercePro and fees are favourable.
- Cannot verify: PayU fees, settlement timelines, KYC for a new business — requires PayU sales.

## 25. COD strategy
- Offer COD only with controls: PIN-code allow-list, order-value cap (e.g. ≤ ₹4,000 to start), phone OTP or WhatsApp confirm, risk scoring (PayU CommercePro or GoKwik), block repeat RTO numbers.
- Nudge to prepaid: visible prepaid saving (₹ amount often outperforms %, per vendor guidance ⚠), post-order WhatsApp "pay now" link within 30–60 min.
- Optional small COD fee or partial advance payment — test, as it can lower conversion.
- Track COD share, RTO %, confirmed-vs-shipped.

## 26. Shipping strategy
Free shipping only above a threshold or on validated margin SKUs (see §12); weight-based real quotes from Shiprocket/Delhivery/Bluedart via aggregator; branded packing slip; insured shipment for ≥ ₹5,000; show **estimated delivery as a range** only after test shipments. Never state "7 days" until proven (needs supplier dispatch SLA + courier zone data).

## 27. Returns strategy
Policy must be reasonable but safe for fragile goods: damaged/wrong item → replacement/refund with unboxing photo within 48h; change-of-mind returns optional (decide); religious-product return hygiene rule. ⚠ A "14 days" figure circulates; not confirmed in primary text. Have a lawyer confirm consumer-law minimums. Dropshipper bears the customer-facing liability.

## 28. Customer support
Single channel hub: email + WhatsApp Business (catalogue off) + phone hours; 48h acknowledgement ⚠ (cited from E-Commerce Rules commentary), named grievance officer on contact page; macros for damage, tracking, COD confirm; order-status page.

## 29. SEO strategy
Clean URLs (`/collections/ganesha-idols`, `/products/brass-ganesha-8-inch`); one canonical taxonomy (competitors suffer duplicates); short titles with deity+material+size; meta templates; Product, Organization, WebSite, BreadcrumbList, FAQ schema (Shopify themes output Product JSON-LD – verify); descriptive alt text; sitemap native; Search Console; Google Merchant Center feed (free listings) after policies are live; internal links from deity guides; avoid thin keyword-stuffed SEO blocks.

## 30. Analytics strategy
Events: view_item_list, view_item, search, add_to_cart, begin_checkout, add_shipping/payment info, purchase, wishlist_add, pincode_check, cod_selected, whatsapp_click. Metrics: sessions by source, CVR, AOV, CAC, COD %, RTO %, refunds %, damage %, delivery days, repeat rate. Stack: GA4 + Shopify analytics + Meta pixel/CAPI + Clarity (consent-aware).

## 31. Marketing strategy
Start with Meta (reels with product close-ups, festival), Google Shopping/Performance Max after catalog stable, WhatsApp remarketing (opt-in), email capture with festival reminders, Instagram organic via craft stories, influencer gifting later. Budget: unknown → open decision. No referral program until repeat purchase evidence.

## 32. App strategy
| App | Purpose | Native alternative | Verdict |
|---|---|---|---|
| COD tool (PayU CommercePro COD / GoKwik) | Eligibility, RTO, verification | Native manual COD (basic) | **Needed** |
| Reviews (free Shopify Product Reviews or lightweight) | Social proof | — | **Needed**; prefer light, SSR |
| Shipping/tracking aggregator (Shiprocket etc.) | Labels, tracking, NDR | Manual | **Needed** |
| Wishlist | Save items | Theme + localStorage | Defer / DIY |
| WhatsApp notifications | Order updates | Email | Phase 2 |
| Search & Discovery | Filters | Native | Use (free) |
| Upsell/bundles, popups, countdowns | — | — | **Reject** |
Target: ≤ 4 apps at launch.

## 33. Performance strategy
Shopify CDN WebP/AVIF; hero image `fetchpriority=high`, others lazy; fixed aspect ratios; srcset up to 3 sizes (max ~1200px width for gallery); video poster + lazy; one font family subset; no third-party chat widgets on load; defer pixels via consent; test with Lighthouse on throttled mid-range Android profile; budgets: LCP < 2.5s, CLS < 0.1, INP < 200ms, JS < 150KB compressed on PDP (target).

## 34. Accessibility
Semantic landmarks, skip link, visible focus, AA contrast, 44px targets, real labels on forms, descriptive alt text (competitors fail here), caption/transcript for video, reduced-motion, text-resize to 200%, no colour-only state, announce cart updates, tested with TalkBack.

## 35. Security
Shopify staff 2FA mandatory; least-privilege staff roles; owner account on dedicated business email; no API keys in theme; supplier/courier credentials in a password manager; PayU key/salt only in app settings; limit app permissions; review apps quarterly; privacy: collect only needed data.

## 36. Legal / compliance checklist (⚠ professional review required)
- **GST:** threshold ₹40 lakh (goods, most states) but inter-state supply of goods and e-commerce supply may force registration regardless of turnover; Notification 34/2023-CT carve-out conditions (no inter-state supply, etc.) — CA to confirm. A dropshipper selling across states almost certainly needs registration. HSN/rate for brass idols to confirm.
- **Consumer Protection (E-Commerce) Rules 2020:** disclosure of seller identity, total price, delivery, returns, grievance officer, country of origin; 48h acknowledge / 1-month resolve cited ⚠.
- **DPDP Act/Rules 2025:** notified 13 Nov 2025; consent/notice duties phase in ~May 2027 ⚠; plan clear notices, consent for marketing, data deletion.
- **Legal Metrology** (net quantity/MRP declarations on packaged goods) ⚠ check applicability.
- **Payments:** PayU/Razorpay KYC (PAN, bank, business proof).
- **Trademark / brand name & logo** check; **IEC** not needed (India-only).
- Policies: Privacy, Terms, Shipping, Returns, Contact with address.
- Cookies: India has no GDPR-style cookie law; DPDP consent still relevant for marketing tracking.

## 37. Complete project roadmap (31 phases, condensed)
0 Discovery (now) → 1 Brand+market research (customer interviews, keyword demand, logo audit) → 2 Product/category strategy (final 15–30 SKUs) → 3 Supplier research (samples, written terms) → 4 Unit economics (real quotes) → 5 Business/legal (entity, GST, bank, trademark) → 6 Domain + business email → 7 Shopify architecture (plan, metafields, apps) → 8 Information architecture → 9 UX/wireframes (mobile first, 360–430px) → 10 Design system → 11 Mobile storefront build → 12 Desktop adaptation → 13 Product data architecture & import → 14 Supplier workflow (order forwarding, tracking) → 15 Payments → 16 COD rules → 17 Shipping/carriers → 18 Returns/refunds → 19 Customer accounts → 20 Wishlist → 21 Reviews → 22 SEO → 23 Analytics → 24 Marketing setup → 25 Security → 26 Accessibility → 27 Performance → 28 Testing (devices, payment, COD, refund, damaged-order drill) → 29 Soft launch (friends/family + 20–50 real orders, caps) → 30 Full launch (before a festival, with buffer) → 31 Post-launch optimisation (weekly metrics, CAC, RTO, reviews).
**Critical path:** logo + supplier samples + legal registration + payment KYC. Design can proceed in parallel *after* the logo.

## 38. Open decisions
| # | Decision | Why it matters | Recommended | Alternatives | Blocks dev? |
|---|---|---|---|---|---|
| 1 | Logo file | Brand system | Provide vector/PNG | — | **Yes (design)** |
| 2 | Supplier model | Margin, delivery promise | Sample-first + stock-light hybrid | Pure dropship | **Yes (promises, pricing)** |
| 3 | Supplier & API | Automation | CSV/WhatsApp first, API later | Aggregator | No |
| 4 | Product catalogue | Content | 15–30 SKUs | — | Partial |
| 5 | Categories | IA | 4 collections (§10) | 3 or 5 | Yes (IA) |
| 6 | Prices | Margin | Per §12 | — | No |
| 7 | Photography | Conversion | Own set after sample | Supplier raw | Partial |
| 8 | Descriptions | SEO/trust | Short, factual, original | Supplier copy | No |
| 9 | Legal name/address/GST | Compliance, policies, payment KYC | Register entity + GST early | Sole proprietorship | **Yes (launch)** |
| 10 | Domain (vrindavan.in / .com availability) | Brand | Check availability; prefer .in or .com | — | No |
| 11 | PayU account / gateway choice | Payments | Quote 3 gateways | PayU only | Yes (launch) |
| 12 | COD rules | RTO | Caps + PIN list + OTP | No COD | No |
| 13 | Return policy | Trust, law | Damage-first policy | 7-day return | Yes (launch) |
| 14 | Support email/WhatsApp/phone | Trust | Business domain email + WhatsApp Business | — | Yes (launch) |
| 15 | Social handles | Marketing | Reserve now | — | No |
| 16 | Analytics setup | Measurement | GA4 + Meta | — | No |
| 17 | Marketing budget | CAC test | Define test budget | — | No |
| 18 | Apps | Cost/perf | ≤4 | — | No |
| 19 | Theme architecture | Build | Horizon-family/OS2.0 + custom sections | Fully custom theme | Yes (Phase 7) |
| 20 | Delivery promise | Trust | Range after test | "7 days" | Yes (copy) |

## 39. Risks
1. Dropshipped fragile brass: damage, inconsistent quality, no QC. 2. COD RTO 30%+. 3. Free-shipping margin on heavy items. 4. Unverified supplier reliability. 5. GST/regulatory missteps. 6. Brand name conflict. 7. Low conversion for high-AOV items. 8. Reviews cold-start (don't fake). 9. App/third-party script bloat. 10. Payment gateway onboarding delays. 11. Religious sensitivity of imagery/copy. 12. Competitor price undercutting by marketplaces.

## 40. Recommended next steps
1. Re-attach the logo. 2. Approve (or edit) the positioning "quiet devotional gallery" and the 4-collection plan. 3. Decide supplier model (sample-first + stock-light). 4. I run **Step 1b**: visual phone-width review (built-in browser) of 8–10 sites incl. non-category references, plus targeted supplier outreach list with message templates. 5. You provide 3–5 candidate SKUs and any supplier quotes so §12 can use real numbers. 6. Then Phase 1–4 proceed.

**THE NEXT DECISION WE NEED TO MAKE:** *Which sourcing model do we commit to testing — pure dropship, or sample-first with a small stock-light hybrid?* (and: send the logo).

---
## Sources
- PayU Shopify FAQ: https://docs.payu.in/docs/shopify-faqs
- Shopify COD help: https://help.Shopify.com/en/manual/payments/cash-on-delivery
- Shopify India pricing/fees (secondary): https://payglocal.in/blog/shopify-price-india-guide · https://razorpay.com/blog/shopify-payment-gateway-cost-india/
- Shopify customer accounts (secondary): https://eseospace.com/blog/shopify-customer-accounts/
- Horizon (secondary): https://themes.shopify.com/themes/horizon · https://craftshift.com/?p=20802
- COD/RTO benchmarks (vendor): https://base.com/en-IN/blog/cod-return-rates-by-product-category-in-india-2026-report/ · https://www.shopflo.com/customers/mridah
- DPDP Rules (law-firm summaries): https://www.jsalaw.com/wp-content/uploads/2025/11/JSA-Prism-InfoTech-November-2025-DPDP-Rules.Final_.pdf · https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/pdf/2025/11/dpdp-act-and-rules.pdf
- E-Commerce Rules 2020 (commentary): https://www.mondaq.com/india/dodd-frank-consumer-protection-act/976876/e-commerce-rules-2020
- GST (secondary): https://calcguru.in/?p=3364
- Awwwards e-commerce: https://www.awwwards.com/websites/winner_category_ecommerce/
- The Citizenry: https://www.the-citizenry.com/ · Mejuri: https://www.mejuri.com/
- Competitors reviewed: statuestudio.com, satvikstore.in, ecraftindia.com, exoticindiaart.in, swabahandicraft.shop, vedanshcraft.com, luxeartisanship.com, artarium.com, krafteria.com, vaaree.com, vedaconnection.in, cutncurve.com, thestonestudio.in (jaypore.com page content not retrievable)
