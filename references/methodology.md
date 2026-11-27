# Simulation Methodology & Calibration Reference

`pulse-crowd` combines **AI-assisted ground-truth extraction** with a **deterministic Python Agent-Based Crowd Simulation (ABM)** scaling dynamically to **>= 1,000 virtual personas** based on project complexity.

---

## 1. Two-Stage Adaptive Workflow

1. **Pre-Dispatch Adaptive Sizing (`scripts/size_swarm.py`):**
   - Before generating virtual personas, the project profile is scored across complexity axes:
     - `product_type`: developer CLI (`+100`), B2B SaaS (`+200`), B2C consumer (`+300`), community network (`+450`), DTC e-commerce brand (`+500`), dropshipping store (`+600`), two-sided marketplace (`+650`), regulated platform (`+850`)
     - `geographic_scope`: single city (`+0`), regional (`+500`), national (`+1300`), multi-country (`+2600`)
     - `regulatory_risk`: low (`+0`), medium (`+400`), high (`+1050` for minors/COPPA/LOPIVI, medical Art. 9 GDPR, or financial compliance)
     - `target_segments`, `pricing_tiers`, `acquisition_channels`, plus `ux_journey` depth (`+90` per step beyond 4 steps)
     - `lifecycle_stage` & `evaluation_depth`: multiplicative scope multipliers
   - **Hard Floor:** The simulator rejects runs below `1,000` virtual personas (`MIN_TOTAL_POPULATION = 1000`).
   - **Cohort Minimum Power Floor:** Every defined cohort receives at least `max(25, 1.5% of total)` virtual personas (capped only when cohort count exceeds budget share) using Largest Remainder apportionment so small critical cohorts remain measurable.

2. **Three-Round Crowd Contagion (`scripts/simulate_crowd.py`):**
   - **Round 1 — Discovery & Policy Gates:** Evaluates onboarding friction, privacy/regulatory blocks, pricing fairness, and baseline value fit with Gaussian trait dispersion around cohort anchors.
   - **Round 2 — Asymmetric Social Contagion:** Computes network spillover across peer cohorts and public discourse weighted by `social_voice_weight`. Unresolved complaints trigger stronger negative amplification (`1.35 + 0.8 * reg_defect_rate` vs `0.85`).
   - **Round 3 — Operational Equilibrium & Conversion:** Evaluates regional/segment liquidity match, Day-14 retention outcomes (`vocal_advocate`, `active_user`, `stalled_in_onboarding`, `churned_low_liquidity`, `rejected_distrust`), and B2B / consumer buyer conversion willingness.

3. **Optional In-App UX Journey Traversal (`ux_journey`):**
   - When `ux_journey` steps are provided, every virtual persona sequentially traverses each route/screen using deterministic UX traits (`patience`, `focus`, `comprehension`, `price_sensitivity`, `privacy_sensitivity`).
   - At each step, individual drop hazards are computed across four explicit behavioral failure modes:
     - `stuck`: triggered by `step_friction` (mandatory logins, heavy forms, KYC hurdles)
     - `distracted`: triggered by `distraction_load` (popups, spin wheels, upsell clutter, competing CTAs) and cumulative flow fatigue
     - `lost`: triggered by `confusion_risk` (unclear hierarchy, jargon, ambiguous navigation)
     - `trust_or_price_shock`: triggered by `surprise_cost` (hidden shipping/fees) and `trust_gap` (augmented by slow dropshipping delivery windows or weak return policies in `commerce_profile`)

4. **Optional E-Commerce & Dropshipping Unit Economics (`commerce_profile`):**
   - Combines UX survival across landing, cart, and checkout with individual consumer buy propensity to estimate synthetic Add-to-Cart rate, Cart Abandonment %, Store Conversion Rate %, Simulated CPA, Gross Profit per Order, Unit Margin after ad spend, and Break-Even Max CPC.

---

## 2. Readiness Rubric (0–100)

- **Baseline Specs (without `ux_journey`):** Combines `40%` normalized Day-14 sentiment + `25%` active/advocate retention + `20%` B2B conversion sub-score + `15%` inverse reject/stall rate.
- **Dual-Engine Specs (with `ux_journey`):** Blends `20%` end-to-end UX completion sub-score (`clamp(ux_completion_rate / 0.55, 0, 1)`) alongside `32%` sentiment, `20%` active retention, `16%` conversion, and `12%` inverse reject/stall rate.
- **Safety Gate:** If `rejected_distrust` exceeds `15%` of total virtual population, the score is hard-capped at `<= 45.0` (`NO-GO`).

---

## 3. Epistemic Honesty & Limitations

- Results are **synthetic scenario-sensitivity outputs** driven by grounded cohort, UX route, and store unit-economics assumptions.
- They stress-test UX bottlenecks, distraction overload, shipping surprises, compliance exposure, and ad CPC sensitivity **before** spending acquisition budget—they do **not** forecast live revenue or replace production analytics (e.g., PostHog/GA4), moderated usability testing, or legal counsel.
