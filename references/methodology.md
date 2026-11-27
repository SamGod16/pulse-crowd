# Simulation Methodology & Calibration Reference

`pulse-crowd` combines **AI-assisted ground-truth extraction** with a **deterministic Python Agent-Based Crowd Simulation (ABM)** scaling dynamically to **>= 1,000 virtual personas** based on project complexity.

---

## 1. Two-Stage Adaptive Workflow

1. **Pre-Dispatch Adaptive Sizing (`scripts/size_swarm.py`):**
   - Before generating virtual personas, the project profile is scored across five axes:
     - `product_type`: developer CLI (`+100`), B2B SaaS (`+200`), B2C app (`+300`), community network (`+450`), two-sided marketplace (`+650`), regulated platform (`+850`)
     - `geographic_scope`: single city (`+0`), regional (`+500`), national (`+1300`), multi-country (`+2600`)
     - `regulatory_risk`: low (`+0`), medium (`+400`), high (`+1050` for minors/COPPA/LOPIVI, medical Art. 9 GDPR, or financial compliance)
     - `target_segments`, `pricing_tiers`, `acquisition_channels`: additive complexity drivers
     - `lifecycle_stage` & `evaluation_depth`: multiplicative scope multipliers
   - **Hard Floor:** The simulator rejects runs below `1,000` virtual personas (`MIN_TOTAL_POPULATION = 1000`). Smaller, single-segment projects receive lean ~1,000–1,500 cohorts; multi-sided regulated or national projects scale automatically to 3,000–12,000+ virtual personas.
   - **Cohort Minimum Power Floor:** Every defined cohort receives at least `max(25, 1.5% of total)` virtual personas (capped only when cohort count exceeds budget share) using Largest Remainder apportionment so small critical cohorts (e.g., legal auditors or rural regions) remain measurable.

2. **Three-Round Crowd Contagion (`scripts/simulate_crowd.py`):**
   - **Round 1 — Discovery & Policy Gates:** Each virtual persona evaluates onboarding friction (`onboarding_friction`), privacy/regulatory blocks (`regulatory_blocker_risk`), pricing fairness (`pricing_fairness`), and personal `value_fit` with Gaussian trait dispersion around cohort anchors.
   - **Round 2 — Asymmetric Social Contagion:** Computes network spillover across peer cohorts and public discourse weighted by `social_voice_weight`. When unresolved regulatory or pay-to-rank complaints exceed threshold, negative amplification exceeds positive social proof (`1.35 + 0.8 * reg_defect_rate` vs `0.85`).
   - **Round 3 — Operational Equilibrium & B2B Conversion:** Evaluates regional/segment liquidity match (`local_liquidity * liquidity_dependence`), drop-off outcomes (`vocal_advocate`, `active_user`, `stalled_in_onboarding`, `churned_low_liquidity`, `rejected_distrust`), and pricing conversion (`yes_pro`, `yes_basic`, `no_free_user_only`, `never`).

---

## 2. Readiness Rubric (0–100)

The weighted score combines four normalized components on the primary run (and averaged across Monte Carlo `--runs`):

- **40%** Normalized Day-14 mean sentiment `(avg_r3 + 1) / 2`
- **25%** Active + Advocate retention rate
- **20%** Normalized B2B paid conversion rate (`clamp(b2b_conv_rate / 0.65, 0.0, 1.0)`, falling back to active retention rate when `is_b2b_buyer` cohorts are absent)
- **15%** Inverse stall + distrust drop-off rate

**Safety Gate:** If `rejected_distrust` exceeds `15%` of total virtual population, the score is hard-capped at `<= 45.0` (`NO-GO`) to prevent high average hype from masking severe regulatory or ethical rejection.

---

## 3. Epistemic Honesty & Limitations

- Results are **synthetic scenario sensitivity outputs** driven by the project spec's cohort parameters.
- They stress-test pricing tiers, onboarding friction, cold-start asymmetries, and compliance exposure **before** writing distribution campaigns—they do **not** forecast real-world revenue or replace live analytics, usability testing, or qualified legal counsel.
