---
name: pulse-crowd
subtitle: Guided Virtual Crowd, UX Funnel & E-Commerce Simulator
tagline: Understand the market and your in-app UX before you enter it.
description: >-
  Run adaptive, guided virtual crowd & in-app UX funnel simulations (minimum
  1,000 virtual personas, scaling upward automatically with project complexity)
  tailored to dropshipping stores, e-commerce brands, future apps, future
  websites/landing funnels, B2B SaaS, and marketplaces. Asks the user which
  business type and audience they are targeting, pinpoints where users get
  stuck, distracted, or lost, and validates pricing & compliance before launch.
license: MIT
compatibility: >-
  Portable Agent Skill (agentskills.io). Requires Python 3.9+ standard library
  and a terminal/shell tool. Tested with Antigravity; compatible with Claude Code,
  OpenAI Codex CLI, OpenCode, Gemini CLI, and Cursor via SKILL.md discovery.
metadata:
  author: SamuelCoreLabs
  version: "2.2.0"
  category: product-validation
---

# PulseCrowd Guided Crowd, UX Funnel & E-Commerce Simulator (`pulse-crowd`)

Evaluate how **1,000 to 25,000+ virtual personas** react both to your **business model** (Discovery, Social Contagion, Week-2 Equilibrium) and **inside your actual product or store** (step-by-step UX journey tracking where users get **stuck**, **distracted**, **lost**, or hit **trust/price shocks**).

Works both on **existing codebases / Shopify themes** AND **pre-code future ideas** (future apps, future websites, or planned dropshipping stores).

---

## Core Invariants

1. **Ask & Ground First:** If the user has not yet specified their business type, stage (existing codebase vs. future pre-code idea), and key funnel/pricing constraints, **ask concise intake questions first** (Step 0) before generating any spec. When a codebase exists, verify parameters directly against real routes, UI components, cart/checkout logic, auth/KYC gates, and legal copy.
2. **Audience-Tailored Simulation:** Adapt virtual cohorts and UX funnel steps to the exact vertical using [references/audience-playbooks.md](./references/audience-playbooks.md) (`dropshipping`, `ecommerce`, `future_app`, `future_website`, `b2b_saas`, `marketplace`, `custom`).
3. **Pre-Dispatch Adaptive Sizing:** Always compute the virtual population size BEFORE simulating traffic using `scripts/size_swarm.py`.
4. **1,000-Persona Minimum Floor:** Never run a crowd test under `1,000` total virtual personas (`MIN_TOTAL_POPULATION = 1000`). Scale upward automatically for multi-sided, multi-step UX, commerce, or high-regulation products.
5. **Epistemic Honesty:** Report outputs explicitly as synthetic scenario-sensitivity metrics derived from user-provided / codebase assumptions—never as real empirical telemetry or live ROAS guarantees.

---

## Step-by-Step Guided Workflow

### Step 0: Conversational Business & Audience Intake (Required When Unspecified)
Whenever invoked with an open prompt (e.g., *"run pulse-crowd"*, *"help me test my launch"*, *"simulate my store/app"*), reply in the **user's language** and ask concise intake questions (using interactive multiple-choice if your host tool supports it, or brief numbered options) to identify:

1. **What kind of business or project are you testing?**
   - **Dropshipping Store** (1-product / niche Shopify/WooCommerce, TikTok/Meta Ads)
   - **E-Commerce / DTC Brand** (own brand, repeat buyers, multi-SKU)
   - **Future Mobile or Web App** (idea/concept before writing code, or early prototype)
   - **Future Website / Landing Page / Lead Funnel** (waitlist, booking, info-product, agency funnel)
   - **B2B SaaS / Developer Tool** (subscriptions, free trial, dev docs, team buyers)
   - **Two-Sided Marketplace or Regulated Platform** (supply/demand liquidity, minors, GDPR/KYC)
   - **Other / Custom Project** (browser extension, bot, course/info-product, newsletter, community, indie game, hardware, local service, etc. — ask the user to describe what they're building in 1–2 lines!)

2. **Do you already have code/store files here, or is it a future project you're planning?**
   - If existing codebase/store exists: confirm target directory/URL/theme files to audit.
   - If pre-code future idea: gather concrete assumptions from the user (never invent fake metrics silently).

3. **Targeted follow-up questions (ask ONLY the 3–5 questions relevant to their chosen track):**
   - **If Dropshipping / E-Commerce:**
     - What are the product, AOV/price, approximate gross margin %, and main ad channel / estimated CPC?
     - What is the shipping delivery window (days) and return policy window? Are shipping fees shown upfront on the product page or calculated only at checkout?
     - Any cart popups (spin-the-wheel, timers, multi-step upsells) or mandatory account login before payment?
   - **If Future App / Future Website / SaaS / Marketplace:**
     - Who is the primary target user vs. who might be skeptical (e.g., parents, privacy auditors, enterprise security, price comparators)?
     - Walk me through the intended steps from landing to value/payment (e.g., do you force signup/KYC/card upfront before showing value?).
     - What is the pricing model (free, freemium, subscription, one-time) and any legal/privacy exposure?
   - **If Other / Custom Project:**
     - Briefly describe what you're building and how users discover/access it (e.g., Chrome Web Store, Telegram link, newsletter signup, local booking).
     - Who are your target users/buyers, and what could cause distrust or drop-off (permissions, store review, price, unclear setup)?
     - What are the exact steps from first click to core payoff or payment?

*(If the user already provided all answers upfront or pointed directly to a full spec/codebase, skip already-answered questions and move immediately to Step 1.)*

---

### Step 1: Audit Codebase (If Available) or Scaffold from Intake Answers
- **If existing repo/store exists:** Inspect routes (`app/`, `pages/`, `src/`, `sections/*.liquid`, `components/CartDrawer*`, `checkout/`, `pricing`, `auth/kyc`, legal policies) and map real files (`component_or_route`) to `ux_journey` friction (`step_friction`, `distraction_load`, `confusion_risk`, `trust_gap`, `surprise_cost`).
- **If validating a future app, future website, or planned dropshipping store (or starting fast):** Scaffold a tailored base JSON matching [references/spec-schema.json](./references/spec-schema.json) and [references/audience-playbooks.md](./references/audience-playbooks.md) using:

```bash
python3 scripts/scaffold_spec.py \
  --business-type dropshipping \
  --name "My Store" \
  --stage pre_launch \
  --aov 49 --margin-pct 62 --cpc 0.90 --shipping-days-max 14 \
  --out /tmp/project_spec.json
```

*(Supported `--business-type` values: `dropshipping`, `ecommerce`, `future_app`, `future_website`, `b2b_saas`, `marketplace`, `custom`; or run `python3 scripts/scaffold_spec.py --interactive` directly.)* Refine the generated cohorts and `ux_journey` steps to match the user's exact answers or audited code files.

---

### Step 2: Calculate Adaptive Swarm Size (Before Dispatch)
Run the sizing engine first so virtual traffic scales proportionally to project, audience, and UX journey complexity:

```bash
python3 scripts/size_swarm.py --spec /tmp/project_spec.json --out /tmp/sizing_plan.json
```

---

### Step 3: Execute the 1,000+ Crowd, UX Funnel & Commerce Simulation
Run across multiple Monte Carlo seeds:

```bash
python3 scripts/simulate_crowd.py --spec /tmp/project_spec.json --out-dir /tmp/pulse_crowd_out --runs 5 --seed 42
```

(Optional enrichment: if your host agent supports parallel subagents, run brief qualitative evaluations with 6–12 anchor personas representing the chosen vertical—e.g., impatient TikTok shopper, Amazon price checker, skeptic auditor—before finalizing cohort/step parameters.)

---

### Step 4: Help the User Act on Outputs (In Their Language)
Read `/tmp/pulse_crowd_out/metrics.json` and `/tmp/pulse_crowd_out/report.md` and help the user directly:
1. Explain the Readiness Score (`0–100`), Verdict (`GO` / `HOLD` / `NO-GO`), adaptive sample size (`>= 1,000`), and 95% confidence interval.
2. Point out the **exact step/screen** (`biggest_bottleneck`) where virtual users drop off and why they get **stuck**, **distracted**, **lost**, or hit **price/trust shocks**.
3. For **Dropshipping / E-Commerce**, report simulated Add-to-Cart, Cart Abandonment, Store CVR, Simulated CPA, and **Break-Even Max CPC**, then give concrete CRO & fulfillment fixes tailored to their answers (and re-run with a remediated spec to prove the Before/After delta!).
4. For **Future Apps / Future Websites**, turn findings into concrete wireframe/flow changes BEFORE coding (or exact code edits if auditing an existing repo).
5. Clearly label every figure as **synthetic sensitivity simulation output** and recommend lightweight empirical checks after launch. Always reply in the **same human language** the user wrote in.

See [references/methodology.md](./references/methodology.md) and [references/audience-playbooks.md](./references/audience-playbooks.md) for equations and vertical archetypes.
