# 🎯 pulse-crowd

> **Understand the market before you enter it.** Adaptive multi-round virtual crowd simulation (`1,000` to `25,000+` personas) for AI coding agents — stress-test product launches, onboarding gates, pricing fairness, and compliance risk before shipping.

**English** · [Español](docs/i18n/README.es.md) · [简体中文](docs/i18n/README.zh-CN.md) · [日本語](docs/i18n/README.ja.md) · [한국어](docs/i18n/README.ko.md) · [Français](docs/i18n/README.fr.md) · [Deutsch](docs/i18n/README.de.md) · [Português](docs/i18n/README.pt-BR.md) · [Italiano](docs/i18n/README.it.md) · [हिन्दी](docs/i18n/README.hi.md) · [Русский](docs/i18n/README.ru.md)

[![CI](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamGod16/pulse-crowd?color=green)](https://github.com/SamGod16/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Agent Skills Standard](https://img.shields.io/badge/Agent_Skills-agentskills.io-green.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)
[![GitHub Stars](https://img.shields.io/github/stars/SamGod16/pulse-crowd?style=social)](https://github.com/SamGod16/pulse-crowd)

**[📊 Live Interactive Demo](https://samgod16.github.io/pulse-crowd/)** · **[📦 GitHub Releases](https://github.com/SamGod16/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamGod16/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)** · **[🐛 Report Bug](https://github.com/SamGod16/pulse-crowd/issues)**

![PulseCrowd Adaptive Crowd Simulation CLI Preview](assets/demo-preview.svg)

---

## Why PulseCrowd?

| Approach | Sample Size | Minority Risk Detection | Determinism & CI | Portability |
| :--- | :--- | :--- | :--- | :--- |
| **Single LLM launch prompt** | 1 generic persona | Hides compliance & cold-start edges | None | Prompt only |
| **Static 10–15 persona script** | Fixed ~15 personas | Oversimplifies or wastes scale | Ad-hoc | Tool-locked |
| **`pulse-crowd` (This Skill)** | **Adaptive `1,000` – `25,000+`** | **Stratified + Largest Remainder floor** | **Seeded Monte Carlo 95% CI** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### The Problem

Asking an AI assistant to "simulate a launch" in a single prompt—or testing a product against 10–15 synthetic personas—misses structural market dynamics:

- Small sample prompts hide minority failure modes (legal auditors, regional cold-start zones, skeptical power users, or guardian verification friction).
- Fixed, oversized test runs waste compute on simple developer utilities that only need a focused cohort mix.
- Proprietary single-tool orchestration scripts break across other AI assistants.

`pulse-crowd` packages a **portable Agent Skill** (`SKILL.md` + zero-dependency Python 3 stdlib tooling) that sizes the virtual crowd automatically **before** dispatch and runs deterministic multi-round simulations across **at least 1,000 virtual personas**. It works on codebases in **any programming language** (TypeScript, Next.js, Python, Go, Rust, Java, Swift, PHP) and responds in **any human language** you prompt your AI assistant in.

---

## How It Works

```mermaid
flowchart LR
    A["1. Ground-Truth Code Audit"] --> B["2. Build Spec JSON"]
    B --> C["3. size_swarm.py (>= 1,000 Personas)"]
    C --> D["Round 1: Discovery & Policy Gates"]
    D --> E["Round 2: Asymmetric Social Contagion"]
    E --> F["Round 3: Week-2 Equilibrium & B2B Conversion"]
    F --> G{"Distrust > 15%?"}
    G -->|Yes| H["Cap Verdict at NO-GO"]
    G -->|No| I["Readiness Score (0-100) + 95% CI"]
```

1. **Pre-Dispatch Adaptive Swarm Sizing (`scripts/size_swarm.py`):** Evaluates project complexity across product architecture, target segments, geographic footprint, pricing tiers, acquisition channels, regulatory risk, lifecycle stage, and desired depth. Enforces a strict **minimum floor of 1,000 virtual personas** and scales dynamically up to **25,000+** for complex, multi-sided, or regulated platforms.
2. **Stratified Cohort Allocation:** Uses Largest Remainder allocation with a per-cohort statistical power floor so critical minority cohorts (such as compliance reviewers or rural provinces) remain measurable.
3. **Three-Round Agent-Based Contagion Simulation (`scripts/simulate_crowd.py`):**
   - **Round 1 — Discovery & Policy Gates:** Models onboarding friction, regulatory/privacy barriers, pricing fairness, and baseline value fit per virtual individual.
   - **Round 2 — Asymmetric Social Contagion:** Simulates peer-cluster alignment and public discourse spillovers, applying higher negative weight when unresolved compliance or pay-to-rank complaints arise.
   - **Round 3 — Week-2 Equilibrium & B2B Conversion:** Simulates regional liquidity gaps, retention outcomes (`vocal_advocate`, `active_user`, `stalled_in_onboarding`, `churned_low_liquidity`, `rejected_distrust`), B2B Basic/Pro conversion hurdles, and Monte Carlo 95% confidence intervals across seeds.
4. **Transparent Readiness Scoring:** Produces a `0–100` Readiness Score with an explicit regulatory distrust safety gate (`rejected_distrust > 15%` caps verdict at `NO-GO`).

---

## Project Structure

```text
pulse-crowd/
├── SKILL.md                          # Core Agent Skills instructions and workflow
├── README.md                         # Project documentation
├── pyproject.toml                    # Zero-dependency Python packaging & CLI entry points
├── LICENSE                           # MIT License
├── CHANGELOG.md                      # Release history
├── CONTRIBUTING.md                   # Contribution and testing guidelines
├── CODE_OF_CONDUCT.md                # Contributor Covenant Code of Conduct
├── SECURITY.md                       # Private vulnerability reporting policy
├── assets/
│   └── demo-preview.svg              # Architecture & observed benchmark preview
├── docs/
│   ├── index.html                    # Interactive GitHub Pages web demo
│   └── i18n/                         # README translations (ES, ZH, JA, KO, FR, DE, PT-BR, IT, HI, RU)
├── .github/
│   ├── CODEOWNERS                    # Maintainer review enforcement
│   ├── dependabot.yml                # Automated GitHub Actions updates
│   ├── PULL_REQUEST_TEMPLATE.md      # Pull request checklist
│   ├── ISSUE_TEMPLATE/               # Structured bug, feature & Q&A templates
│   └── workflows/                    # CI matrix (Python 3.9–3.14) & PyPI release
├── scripts/
│   ├── size_swarm.py                 # Adaptive >= 1,000 population sizing calculator
│   ├── simulate_crowd.py             # 3-round agent-based crowd simulator + reporting
│   └── validate_skill.py             # SKILL.md spec, link, schema, and secret checker
├── references/
│   ├── methodology.md                # Mathematical formulation, rubric, and scope limits
│   └── spec-schema.json              # JSON Schema for project + cohort specifications
├── examples/
│   ├── minimal-b2b-cli.json          # Lean dev-tool spec (sizes to 1,500 personas)
│   └── regulated-marketplace.json    # Complex regional marketplace spec (sizes to 6,750 personas)
└── tests/
    └── test_pulse_crowd_sim.py       # Python unittest suite
```

---

## Requirements & Dependencies

- **Runtime:** Python `3.9+` (tested locally on `Python 3.9.6` and verified in CI across `3.9`–`3.14`).
- **External packages:** None. All core scripts use Python's standard library (`json`, `csv`, `math`, `random`, `statistics`, `argparse`, `pathlib`, `unittest`, `re`).
- **Optional CLI:** Node.js / `npx` if installing via the community `skills` CLI (`npx skills add`).

---

## Installation

Replace `SamGod16` with your GitHub username or organization if forking.

### Option 1: Install Globally via `npx skills` (Multi-Agent CLI)

Per Vercel Labs' [`skills`](https://github.com/vercel-labs/skills) CLI documentation (`-g` installs globally at the user level):

```bash
# Interactive multi-agent global install
npx skills add SamGod16/pulse-crowd -g

# Target specific agents non-interactively
npx skills add SamGod16/pulse-crowd -a claude-code -g -y
npx skills add SamGod16/pulse-crowd -a codex -g -y
npx skills add SamGod16/pulse-crowd -a opencode -g -y
```

### Option 2: Manual Global Installation (Clone / Symlink)

Clone the repository once, then link or copy it to the shared standard path (`~/.agents/skills/`) and any agent-native directories you use:

```bash
git clone https://github.com/SamGod16/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills

# Shared Agent Skills path (scanned by Codex, OpenCode, Gemini CLI, Cursor)
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd

# Agent-specific user-level skill directories
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

For workspace-only installation inside a single repository instead of global installation, place the folder under `.agents/skills/pulse-crowd/` (or `.claude/skills/pulse-crowd/`).

### Option 3: Install Python CLI via `pip` (from GitHub)

```bash
pip install git+https://github.com/SamGod16/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Verify Your Installation

Confirm the skill directory resolves cleanly and passes self-checks:

```bash
python3 ~/.agents/skills/pulse-crowd/scripts/validate_skill.py
python3 -m unittest discover -s ~/.agents/skills/pulse-crowd/tests -v
```

Expected confirmation: `Skill validation PASSED` and `Ran 6 tests ... OK`.

---

## Usage & Observed CLI Examples

### 1. Adaptive Sizing Check (Run Before Simulation)

Compare how the same sizing engine scales virtual traffic automatically for a small CLI tool vs. a regulated two-sided marketplace:

```bash
# Minimal single-city developer CLI -> sizes cleanly above the 1,000 floor (1,500)
python3 scripts/size_swarm.py --spec examples/minimal-b2b-cli.json

# Regulated regional two-sided marketplace -> scales upward automatically (6,750)
python3 scripts/size_swarm.py --spec examples/regulated-marketplace.json
```

### 2. Full 3-Round Crowd Simulation

```bash
python3 scripts/simulate_crowd.py \
  --spec examples/regulated-marketplace.json \
  --out-dir /tmp/pulse_crowd_demo_reg \
  --runs 3 \
  --seed 42
```

Verified output observed on `Python 3.9.6`:

```json
{
  "project_name": "Regional Youth Sports Scouting Marketplace (Post-Hardening)",
  "recommended_population": 6750,
  "complexity_tier": "complex_4k_8k",
  "monte_carlo": {
    "runs": 3,
    "base_seed": 42,
    "mean_readiness_score": 92.3,
    "score_ci95_half_width": 0.07,
    "mean_avg_r1": 0.452,
    "mean_avg_r2": 0.53,
    "mean_avg_r3": 0.649,
    "verdict": "GO (Conditional or Phase-1 Launch Ready)"
  },
  "out_dir": "/tmp/pulse_crowd_demo_reg"
}
```

And on the minimal tool (`examples/minimal-b2b-cli.json`): `recommended_population: 1500` (`lean_1k`), `mean_readiness_score: 90.0` (`±0.07`).

Generated output artifacts in `--out-dir`:
- `sizing_plan.json` — weighted complexity drivers and proportional cohort allocations
- `metrics.json` — Monte Carlo summary, outcomes distribution, B2B conversion counts, top friction counts
- `cohorts_summary.csv` — tabular breakdown per cohort
- `personas_sample.json` — stratified individual trace sample across extreme and median cases
- `report.md` — structured human-readable launch report

### 3. Prompting Your AI Agent Naturally

Once installed globally, prompt your assistant inside any codebase:

- *"Audit our current onboarding and pricing code, build a spec JSON for PulseCrowd, size the virtual crowd based on our project complexity (minimum 1,000 personas), and run a 3-round simulation."*
- *"Compare our current v1 authentication flow against a non-biometric alternative across at least 2,000 virtual users."*

### Expected Agent Workflow

When activated, a compatible agent will:
1. Read `SKILL.md` via progressive disclosure and inspect the target repository's real code/copy.
2. Construct a grounded JSON spec following [references/spec-schema.json](references/spec-schema.json).
3. Run `scripts/size_swarm.py` to compute adaptive traffic (`>= 1,000`).
4. Execute `scripts/simulate_crowd.py` across multiple seeds and present cohorts, friction drivers, and clear sensitivity disclaimers.

---

## Agent & Tool Compatibility Matrix

| Agent / Tool | Discovery Paths | Verification Status | Notes |
| :--- | :--- | :--- | :--- |
| **Antigravity IDE / CLI** | `.agents/skills/`, configured `skills.json` | **Confirmed (tested locally)** | Validated `SKILL.md` loading conventions and local script execution on macOS. |
| **Claude Code** | `~/.claude/skills/`, `.claude/skills/` | **Confirmed layout / Pending live CLI test** | Global directory inspected locally; conforms to `agentskills.io` `SKILL.md` format documented for Claude Code. |
| **OpenAI Codex CLI** | `~/.codex/skills/`, `~/.agents/skills/` | **Documented compatible / Untested live** | Follows official Codex skill discovery paths and stdlib shell execution. |
| **OpenCode** | `~/.config/opencode/skills/`, `~/.agents/skills/`, `~/.claude/skills/` | **Documented compatible / Untested live** | Scans OpenCode, Claude, and shared `.agents/skills/` directories natively. |
| **Gemini CLI** | `~/.gemini/skills/`, `~/.agents/skills/` | **Documented compatible / Untested live** | Follows `agentskills.io` spec and shared global path conventions. |
| **Cursor** | `~/.cursor/skills/`, `~/.agents/skills/` | **Documented compatible / Untested live** | Supports `SKILL.md` progressive disclosure per Cursor skills documentation. |

---

## Limitations & When Not to Use

- **Synthetic sensitivity model, not field telemetry:** Output scores measure directional sensitivity to calibrated assumptions (onboarding friction, regulatory exposure, regional density, paywall limits). They do **not** predict actual revenue or conversion rates in production.
- **Garbage-in, garbage-out calibration:** If the input JSON uses optimistic `value_fit` or ignores real codebase defects, simulation results will reflect optimistic assumptions. Always ground inputs in code and user research.
- **Not a substitute for legal, medical, or usability review:** The simulator models stakeholder pushback to compliance issues but does not provide legal clearance (GDPR, COPPA, LOPIVI) or replace moderated usability testing.
- **When not to use:** Do not use for purely internal library refactoring where there is no end-user onboarding, pricing, compliance, or adoption decision.

---

## Privacy & Security

- Runs 100% locally via Python 3 standard library—no telemetry, no external network calls, and no API keys required.
- All bundled specs in `examples/` are anonymized illustrative templates with zero personal identifiable information (PII).
- Automated CI/local validation (`scripts/validate_skill.py`) scans files for common secret patterns before distribution.

---

## Contributing

Contributions are welcome! Check our **[Good First Issues](https://github.com/SamGod16/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**, review [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md), and run both checks before opening a pull request:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## License

Licensed under the **[MIT License](LICENSE)** — Copyright (c) 2026 SamGod16.

**Why MIT?** For an open-source Agent Skill targeting broad developer and multi-agent adoption (`npx skills`, Claude Code, Codex, OpenCode), the MIT License offers minimal legal friction for commercial teams, solo developers, and forks while requiring only preservation of the copyright and permission notice.
