# Audience Playbooks by Business Vertical

Use this reference during **Step 0 (Guided Intake)** and **Step 2 (Spec Construction)** to adapt virtual cohorts, `ux_journey` screens, and advice to the user's exact business model—whether they are running a live store/repo or validating a **future app, future website, or dropshipping store** pre-code.

---

## 1. Dropshipping Store (`dropshipping_store`)

**Typical traffic & risks:** Cold paid social traffic (`TikTok Ads`, `Meta Ads`), high sensitivity to perceived legitimacy, surprise shipping fees, long overseas fulfillment (`10–25` days), spin-the-wheel popups, and aggressive upsell clutter.

- **Recommended Cohorts:**
  1. `impulse_tiktok_shoppers` (`share: 0.45`, `is_commerce_buyer: true`) — low patience (`onboarding_friction` sensitivity), high `social_susceptibility` (`0.70+`), buys quickly if PDP matches the ad and checkout is frictionless.
  2. `price_comparators` (`share: 0.25`, `is_commerce_buyer: true`) — checks Amazon/AliExpress pricing; high sensitivity to `pricing_fairness` and `surprise_cost`.
  3. `trust_skeptic_buyers` (`share: 0.20`, `is_commerce_buyer: true`) — looks for real reviews, contact info, clear return window (`>= 30` days), and visible delivery ETA before checkout.
  4. `ad_comment_critics` (`share: 0.10`, `is_commerce_buyer: false`, `social_voice_weight: 2.2`) — leaves public ad comments if delivery windows look deceptive or urgency timers look fake.
- **Default `ux_journey` screens:** Ad Landing / Product Page -> Cart Drawer & Upsells -> Account / Shipping Gate -> Payment & Final Total.
- **High-ROI remediation advice:** Remove forced account creation before checkout, disclose shipping cost & delivery dates on the product page, cut distracting popups/countdown timers, and track Break-Even Max CPC vs assumed ad CPC.

---

## 2. E-Commerce / DTC Brand (`ecommerce_brand`)

**Typical traffic & risks:** Multi-channel discovery (organic search, Meta/IG, creators, email), sizing/spec doubts, cart abandonment at shipping calculation, repeat-buyer retention.

- **Recommended Cohorts:**
  1. `core_brand_buyers` (`share: 0.45`, `is_commerce_buyer: true`) — strong product-problem fit, values clarity and express checkout (`Shop Pay` / `Apple Pay`).
  2. `social_discovery_buyers` (`share: 0.25`, `is_commerce_buyer: true`) — impulse-oriented on mobile; drops off if page speed/navigation distracts.
  3. `spec_detail_researchers` (`share: 0.20`, `is_commerce_buyer: true`) — checks materials, sizing, warranty, and return policy (`>= 30` days).
  4. `community_reviewers` (`share: 0.10`, `is_commerce_buyer: false`, `social_voice_weight: 1.7`) — amplifies post-delivery satisfaction or shipping frustration.
- **Default `ux_journey` screens:** Mobile Product Page -> Slide Cart / Free-Shipping Bar -> Express Guest Checkout.

---

## 3. Future Mobile / Web App Concept (`mobile_app` or `b2c_consumer`, `lifecycle_stage: "concept"`)

**Typical stage:** Pre-code or early prototype. The user wants to validate whether real users understand the value proposition and where a planned screen sequence would lose them before investing weeks building it.

- **Recommended Cohorts:**
  1. `early_adopter_testers` (`share: 0.35`) — eager to try new apps, forgiving of minor rough edges, sensitive to unclear core payoff.
  2. `impatient_first_timers` (`share: 0.35`) — bounces immediately if asked to create an account, verify phone, or grant notifications/permissions before seeing value.
  3. `privacy_cautious_users` (`share: 0.18`) — triggers on premature KYC, tracking prompts, or unclear data usage.
  4. `skeptical_reviewers` (`share: 0.12`, `social_voice_weight: 1.8`) — challenges whether the app solves a real pain vs existing free tools.
- **Default `ux_journey` screens:** First Impression / Value Hook -> Permission / Signup Gate -> First Core Action -> Paywall / Retention Prompt.
- **High-ROI advice:** Delay signup & permissions until AFTER the user experiences the first "aha!" moment; eliminate multi-field onboarding forms before value delivery.

---

## 4. Future Website / Landing Page / Lead-Gen & Info-Product (`website_funnel`)

**Typical stage:** Pre-launch landing page, agency site, waitlist, service booking funnel, or digital product checkout.

- **Recommended Cohorts:**
  1. `high_intent_searchers` (`share: 0.35`, `is_commerce_buyer: true`) — arrived actively looking for a solution; drops if hero copy is vague or pricing is hidden.
  2. `cold_social_visitors` (`share: 0.35`) — short attention span; leaves if distracted by heavy nav menus, auto-playing clutter, or walls of text.
  3. `comparison_evaluators` (`share: 0.20`, `is_commerce_buyer: true`) — wants case studies, transparent tiers, FAQ, and trust badges.
  4. `skeptical_critics` (`share: 0.10`, `social_voice_weight: 1.7`) — spots hype claims without proof.
- **Default `ux_journey` screens:** Hero & Value Proposition -> Social Proof & Pricing/Offer -> Lead Form / Calendar / Checkout.

---

## 5. B2B SaaS & Developer Tools (`b2b_saas` / `developer_tool`)

**Typical cohorts:** Solo developers / individual users, team buyers (`is_b2b_buyer: true`), security/procurement auditors, and public tech forum critics (`Hacker News` / `Reddit`).

- **Default `ux_journey` screens:** Landing / Docs -> Trial / Auth Gate -> Workspace / First API Call -> Pricing / Team Upgrade.

---

## 6. Two-Sided Marketplaces & Regulated Platforms (`two_sided_marketplace` / `regulated_platform`)

**Typical cohorts:** Supply side + demand side (including metro vs secondary/rural liquidity gaps), B2B buyers, minors + guardians if applicable, and legal/GDPR/compliance auditors (`social_voice_weight: 2.0+`).

- Always pay close attention to `local_liquidity`, `liquidity_dependence`, and the `rejected_distrust > 15%` regulatory safety gate.

---

## 7. Other / Custom Projects (`custom_project`)

Use this playbook whenever the user selects **"Other / Custom"**—for example: **browser extensions, Discord/Telegram/Slack bots, newsletters, paid communities, online courses/info-products, indie games, desktop utilities, hardware, local services, or hybrid businesses**.

- **How to tailor from the user's description:**
  1. Ask 3–4 short questions: *What is it? How do people first find and try it? Who pays (or how is it monetized)? What could make someone hesitate or quit halfway?*
  2. Define 3–4 bespoke cohorts matching their real stakeholders:
     - `core_target_users` (primary users/subscribers/players/clients)
     - `curious_browsers` (low-patience cold visitors testing the first screen/hook)
     - `paid_or_pro_buyers` (if monetized via subscriptions, sponsorship, one-time, or service booking)
     - `skeptical_evaluators` (store/platform reviewers, privacy checkers, or price-sensitive critics)
  3. Map their concrete user path into `ux_journey` (e.g., *Install / Hook -> First Setup / Permission -> Core Value Moment -> Monetization / Retention*).

