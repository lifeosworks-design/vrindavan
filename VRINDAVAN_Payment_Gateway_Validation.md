# VRINDAVAN — Payment Gateway Validation
Status: **PARTIAL.** PayU remains the conditional primary candidate; Razorpay the fallback. No account has been opened and no KYC shared. Nothing here has been sent.

## 1. The key CRO question
> **Can a first-time mobile customer complete prepaid checkout without being forced into unnecessary account creation?**
| Path | What the official docs say | Answer status |
|---|---|---|
| PayU **hosted checkout app** (cards/UPI/net banking) | PayU's Shopify FAQ does not mention any login requirement for this app | **UNVERIFIED** — likely guest-friendly, but not stated; ask PayU in writing |
| PayU **CommercePro Checkout / COD** | CommercePro **login widget** requires: login links shown, **guest checkout disabled**, captcha disabled on login/registration, default login sections hidden. To use Shopify's default COD with CommercePro, **deactivate "PayU OTP Login"** | **VERIFIED (docs): forced login/OTP risk exists for the CommercePro flow** |
| Razorpay Shopify app | UPI/cards/wallets/netbanking on Standard Checkout; no login requirement mentioned | **UNVERIFIED** (docs silent) |
| Shopify's own account settings | I did not check (no store; not to be created) | **UNVERIFIED** — confirm at the architecture stage |
**Working position:** prepaid via a guest-capable hosted/standard checkout; COD via Shopify's native manual COD + manual WhatsApp confirmation at pilot volume; adopt CommercePro COD **only if** PayU confirms it can run without forced login. A mobile checkout that demands an account or OTP before payment is a conversion risk, not a feature.

## 2. PayU — what is VERIFIED (official pages read)
From `docs.payu.in/docs/shopify-faqs` and `payu.in/pricing`: separate apps — hosted checkout (cards, UPI, net banking; supports offers), onsite cards (no UPI), CommercePro Checkout, CommercePro COD (eligibility + RTO rules by PIN, address, mobile, email, amount, AI signals; enablement via KAM/PayU Support; install CommercePro Checkout first); UPI must be enabled on the merchant account and "new accounts may start with limited modes"; refund timelines UPI 3–5 working days, credit card 5–7, debit 7–10, net banking 5–7, wallet instant–24h; Shopify cancel can trigger a refund by webhook; offer-transaction refunds only from the PayU dashboard. Pricing: **2% + 18% GST** cards/NB/wallets/BNPL; **3%** Amex/Diners/EMI/international; **P2P UPI zero MDR (no merchant UPI rate stated)**; no setup/annual fee; standard settlement **T+2**. Not specified anywhere I read: KYC documents, approval time, COD fees, domestic settlement detail in the Shopify docs, limits.

## 3. Questions to get **in writing** from PayU (send to your KAM/sales contact)
| # | Topic | Exact question | Answer (fill) |
|---|---|---|---|
| 1 | Shopify integration | Which app combination do you recommend for a new India store (hosted vs onsite vs CommercePro)? Does it work with Shopify's current checkout and my plan? Any theme edits required? | |
| 2 | UPI charges | What is the **merchant UPI MDR/fee** (incl. GST) for my category and plan? Any UPI collect/intent differences? | |
| 3 | Domestic card charges | Confirm credit/debit (Visa/MC/RuPay) rates incl. GST; differential for corporate/premium cards; EMI fee. | |
| 4 | Net banking charges | Confirm rate incl. GST; wallets/BNPL rates. | |
| 5 | COD capability | Is COD available to new merchants? Fee per COD order (flat/%)? RTO charges? COD remittance cycle? | |
| 6 | COD app requirements | What does CommercePro COD require (KAM enablement, thresholds, volume)? Timeline to enable? | |
| 7 | Guest checkout | **Can a first-time customer pay prepaid and COD as a guest** (no account)? Is guest checkout disabled by any app? | |
| 8 | Login / OTP | Is login or OTP mandatory in any flow? Can it be disabled or made optional? | |
| 9 | Settlement | Domestic settlement cycle (T+1/T+2), same-day/priority option and fee, settlement cut-off, payout holidays. | |
| 10 | Refund charges | Fee to issue refunds? Is MDR refunded/reversed? Dashboard refund timelines? Partial refunds? | |
| 11 | Failed-payment charges | Any fee for failed/abandoned/dropped transactions or retries? | |
| 12 | Minimum transaction | Minimum/maximum per-transaction value, daily/monthly caps for a new account, any rolling reserve. | |
| 13 | Onboarding | KYC documents (proprietorship/GST status/bank), website requirements before approval, approval timeline, whether a live store with policies is mandatory. | |
Extra: chargeback fees and process; GST invoice for fees; support SLA/KAM for small merchants; EMI/affordability widget terms.

## 4. Razorpay — shorter fallback comparison
**VERIFIED (official pages):** 2% platform fee + 18% GST on fee for cards, UPI, netbanking, wallets; setup ₹0; AMC ₹0; refund processing fee ₹0; settlement T+1 (instant is an add-on, price not shown); Shopify app "All-in-one Razorpay Payment Gateway"; supports UPI/cards/wallets/netbanking on **Standard Checkout only**; **Razorpay reviews the website before integration**; only the account owner can connect; COD and refunds **not specified** in the docs page I read.
**Ask Razorpay (only if PayU's answers to #2, #5–#9 or #13 fail):** (1) merchant UPI fee; (2) COD option for Shopify India and its fee/remittance; (3) guest checkout/forced login; (4) refund timelines/fees; (5) KYC documents + website requirements + timeline; (6) rolling reserve/limits for new accounts; (7) settlement days.
| Item | PayU | Razorpay |
|---|---|---|
| Cards/NB/wallets | 2% + GST (verified) | 2% + GST (verified) |
| UPI merchant fee | **unknown** | listed "2%… zero MDR" — ambiguous |
| COD for Shopify | CommercePro COD (verified, with login constraints) | unspecified |
| Settlement | T+2 (verified) | T+1 (verified) |
| Refund fee | not stated | ₹0 (verified) |
| Guest checkout | unverified (CommercePro: disabled) | unverified |

## 5. Decision rule (Gate: Payment)
**VERIFIED when:** one gateway has written answers to #2, #5–#9 and #13, with a guest-friendly prepaid path and a COD path that does not force login (or an acceptable alternative), and KYC is feasible for our entity. Until then: PayU = conditional primary; Razorpay = fallback; **no account opened until Gates 1, 3 and 7 are further along** (some gateways need a reviewable website — a sequencing dependency to handle at the architecture stage, not now).

## 6. Evidence to bring back
PayU/Razorpay written replies (email/PDF/screenshots) with date and sender; the filled answer column above; any fee schedule PDF.
