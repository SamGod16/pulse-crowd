---
name: pulse-crowd
subtitle: Adaptive Virtual Crowd & UX Funnel Simulation
tagline: Understand the market and your in-app UX before you enter it.
description: >-
  Run adaptive, multi-round virtual crowd & in-app UX funnel simulations (minimum
  1,000 virtual personas, scaling upward automatically with project complexity)
  to stress-test product launches, in-app drop-offs (where users get stuck,
  distracted, or lost), e-commerce/dropshipping stores, pricing tiers, B2B
  conversion, and regulatory compliance before shipping. Use when evaluating
  market readiness, UX funnels, Shopify/DTC/dropshipping conversion, pricing
  changes, compliance pivots, or go-to-market launches across any AI agent.
license: MIT
compatibility: >-
  Portable Agent Skill (agentskills.io). Requires Python 3.9+ standard library
  and a terminal/shell tool. Tested with Antigravity; compatible with Claude Code,
  OpenAI Codex CLI, OpenCode, Gemini CLI, and Cursor via SKILL.md discovery.
metadata:
  author: SamuelCoreLabs
  version: "2.0.0"
  category: product-validation
---

# PulseCrowd Dual-Engine Crowd & UX Simulator (`pulse-crowd`)

Evaluate how **1,000 to 25,000+ virtual personas** react both to your **business model** (Discovery, Social Contagion, Week-2 Equilibrium) and **inside your actual application** (step-by-step UX journey tracking where users get **stuck**, **distracted**, **lost**, or hit **trust/price shocks**)—including specialized support for **E-Commerce & Dropshipping** stores.

This skill works across any coding agent with shell access and requires zero external Python dependencies.

---

## Core Invariants

1. **Ground-Truth First:** Extract parameters directly from real routes, components, Shopify/Liquid themes, cart/checkout code, auth/KYC gates, legal policies, and UI copy—never from wishful marketing slogans.
2. **Pre-Dispatch Adaptive Sizing:** Always compute the virtual population size BEFORE simulating traffic using `scripts/size_swarm.py`.
3. **1,000-Persona Minimum Floor:** Never run a crowd test under `1,000` total virtual personas (`MIN_TOTAL_POPULATION = 1000`). Scale upward automatically for multi-sided, multi-step UX, commerce, or high-regulation products.
4. **Epistemic Honesty:** Report outputs explicitly as synthetic scenario-sensitivity metrics derived from codebase assumptions, never as real empirical conversion telemetry or live ad-platform ROAS guarantees.

---

## Step-by-Step Execution Workflow

### Step 1: Audit the Target Codebase (Business + In-App UX Routes)
Inspect the repository (`app/`, `pages/`, `src/`, `sections/*.liquid`, `components/`, pricing/auth/checkout files) and document:
- **Business model & cohorts:** Core value proposition, free vs paid gates, B2B buyers vs consumers, compliance/legal reviewers, and social skeptics.
- **In-app user journey screens (`ux_journey`):** Trace the concrete sequence of screens/components users walk through (e.g., `Landing / Ad Hero` -> `Signup / KYC` -> `Product Page / Dashboard` -> `Cart Drawer` -> `Checkout`), scoring for each file:
  - `step_friction` (**stuck**): mandatory account walls, long forms, KYC/selfies, blocking spinners.
  - `distraction_load` (**distracted**): spin-the-wheel popups, aggressive upsells, competing CTAs, cluttered nav bars.
  - `confusion_risk` (**lost**): jargon, unclear next step, buried controls, ambiguous copy.
  - `trust_gap` & `surprise_cost`: missing social proof/return policy, countdown spam, hidden shipping/fees revealed late.
- **E-Commerce / Dropshipping (`commerce_profile`):** If auditing a store (`ecommerce_brand` or `dropshipping_store`), capture AOV, margin %, estimated CPC, shipping window (`shipping_days_min`/`max`), hidden checkout shipping (`hidden_shipping_at_checkout`), and return policy days.

### Step 2: Build the Specification JSON
Create a working JSON file matching [references/spec-schema.json](./references/spec-schema.json). Start from the closest template:
- SaaS / CLI / DevTool: [examples/minimal-b2b-cli.json](./examples/minimal-b2b-cli.json)
- Regulated Marketplace: [examples/regulated-marketplace.json](./examples/regulated-marketplace.json)
- Dropshipping Store: [examples/dropshipping-store.json](./examples/dropshipping-store.json)
- DTC E-Commerce Brand: [examples/ecommerce-dtc-brand.json](./examples/ecommerce-dtc-brand.json)

### Step 3: Calculate Adaptive Swarm Size (Before Dispatch)
Run the sizing engine first so traffic scales proportionally to project and UX journey complexity:

```bash
python3 scripts/size_swarm.py --spec /path/to/project_spec.json --out /tmp/sizing_plan.json
```

### Step 4: Execute the 1,000+ Crowd & UX Funnel Simulation
Run the simulator across multiple Monte Carlo seeds:

```bash
python3 scripts/simulate_crowd.py --spec /path/to/project_spec.json --out-dir /tmp/pulse_crowd_out --runs 5 --seed 42
```

(Optional qualitative enrichment: if your host agent supports parallel subagents, run brief qualitative reviews with 6–12 anchor personas over specific UI components first to calibrate `step_friction`, `distraction_load`, and `confusion_risk`, then expand across all `>= 1,000` personas.)

### Step 5: Analyze Outputs & Recommend Code-Level Fixes
Read `/tmp/pulse_crowd_out/metrics.json` and `/tmp/pulse_crowd_out/report.md`:
1. Summarize the adaptive population size chosen and the overall Readiness Score (`0–100`) with 95% CI.
2. When `ux_journey` is present, pinpoint the exact **`biggest_bottleneck`** (`component_or_route`), cumulative retention curve, and whether users dropped due to getting **stuck**, **distracted**, **lost**, or **trust/price shock**.
3. When `commerce_profile` is present, report simulated Add-to-Cart, Cart Abandonment, Store CVR, Simulated CPA, and Break-Even Max CPC sensitivity.
4. Clearly label all figures as **synthetic sensitivity simulation results** and outline empirical post-launch validation checks needed with real users (e.g., session recordings, funnel analytics, live split tests).
5. Deliver the final summary, risk breakdown, and remediation plan in the **same human language the user prompted in** (supporting any language seamlessly), regardless of whether the audited codebase uses TypeScript, Liquid, Python, Go, Rust, Java, Swift, or any other stack.

See [references/methodology.md](./references/methodology.md) for the exact equations, UX funnel hazards, and contagion rules.
