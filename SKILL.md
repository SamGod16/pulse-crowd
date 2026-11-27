---
name: pulse-crowd
subtitle: Adaptive Virtual Crowd Simulation
tagline: Understand the market before you enter it.
description: >-
  Run adaptive, multi-round virtual crowd simulations (minimum 1,000 virtual
  personas, scaling upward automatically with project complexity) to stress-test
  product launches, onboarding friction, pricing tiers, B2B conversion, and
  regulatory compliance before shipping. Use when evaluating market readiness,
  pricing changes, compliance pivots, or go-to-market launches across any AI agent.
license: MIT
compatibility: >-
  Portable Agent Skill (agentskills.io). Requires Python 3.9+ standard library
  and a terminal/shell tool. Tested with Antigravity; compatible with Claude Code,
  OpenAI Codex CLI, OpenCode, Gemini CLI, and Cursor via SKILL.md discovery.
metadata:
  author: SamGod16
  version: "1.0.0"
  category: product-validation
---

# PulseCrowd Adaptive Crowd Simulator (`pulse-crowd`)

Evaluate how a real market of **1,000 to 25,000+ virtual personas** reacts to a product across **Discovery**, **Social Contagion**, and **Week-2 Equilibrium** before spending acquisition budget.

This skill works across any coding agent with shell access. It does not depend on proprietary workflow orchestration APIs.

---

## Core Invariants

1. **Ground-Truth First:** Extract project parameters directly from the actual codebase, pricing logic, auth/KYC code, legal policies, and UI copy—never from aspirational marketing slogans.
2. **Pre-Dispatch Adaptive Sizing:** Always compute the virtual population size BEFORE simulating traffic using `scripts/size_swarm.py`.
3. **1,000-Persona Minimum Floor:** Never run a crowd test under `1,000` total virtual personas (`MIN_TOTAL_POPULATION = 1000`). Scale upward automatically for multi-sided, multi-region, or high-regulation products.
4. **Epistemic Honesty:** Report outputs explicitly as synthetic scenario-sensitivity metrics derived from project assumptions, never as real empirical conversion telemetry.

---

## Step-by-Step Execution Workflow

### Step 1: Audit the Target Project
Inspect the user's codebase or proposal and document:
- Core value proposition, free vs paid gates, and pricing limits.
- Onboarding friction (e.g., document KYC, selfies, multi-step forms).
- Regulatory exposure (e.g., minors/guardianship laws, GDPR/medical special categories, IP/third-party privacy).
- Regional or segment cold-start asymmetry (e.g., metro hub vs rural/secondary areas).

### Step 2: Build the Project & Cohort Specification JSON
Create a working JSON file matching [references/spec-schema.json](./references/spec-schema.json). You can start from [examples/minimal-b2b-cli.json](./examples/minimal-b2b-cli.json) or [examples/regulated-marketplace.json](./examples/regulated-marketplace.json).

Include cohorts covering every side of the market plus institutional/skeptic voices:
- End-user segments (e.g., free tier, minors + parents if applicable, power users).
- B2B buyers (`is_b2b_buyer: true`) mapped to Basic/Pro tiers.
- Regulators, domain specialists, and vocal community critics with higher `social_voice_weight`.

### Step 3: Calculate Adaptive Swarm Size (Before Dispatch)
Run the sizing engine first so traffic scales proportionally to project complexity:

```bash
python3 scripts/size_swarm.py --spec /path/to/project_spec.json --out /tmp/sizing_plan.json
```

Inspect `recommended_population`, `complexity_tier`, and `cohort_allocations`.
- Focused single-region tools typically size around **1,100–1,600** virtual personas.
- Multi-sided or regulated regional marketplaces scale to **3,500–8,000+**.
- Multi-country or stress-test profiles scale further (up to `25,000` by default).

### Step 4: Execute the 1,000+ Crowd Simulation
Run the 3-round agent-based contagion simulator across multiple Monte Carlo seeds:

```bash
python3 scripts/simulate_crowd.py --spec /path/to/project_spec.json --out-dir /tmp/pulse_crowd_out --runs 5 --seed 42
```

(Optional qualitative enrichment: if your host agent supports parallel subagents, you may run qualitative interviews with 6–12 anchor personas first to refine cohort parameters such as `onboarding_friction` and `pricing_fairness`, then expand via `simulate_crowd.py` across all `>= 1,000` personas.)

### Step 5: Analyze Outputs & Recommend Fixes
Read `/tmp/pulse_crowd_out/metrics.json` and `/tmp/pulse_crowd_out/report.md`:
1. Summarize the adaptive population size chosen and why.
2. Report the Readiness Score (`0–100`), 95% confidence interval across `--runs`, sentiment shift (`R1 -> R2 -> R3`), B2B paid conversion rate, and top friction categories.
3. Compare baseline vs remediated specs whenever iterating on fixes.
4. Clearly label all figures as **synthetic sensitivity simulation results** and outline empirical post-launch validation checks needed with real users.

See [references/methodology.md](./references/methodology.md) for the exact scoring equations and contagion rules.
