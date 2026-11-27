# Changelog

All notable changes to `pulse-crowd` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-11-27

### Added
- **In-App UX Journey Funnel (`ux_journey`):** Sequential per-persona traversal across application routes/screens modeling exact drop-off bottlenecks where users get **stuck** (`step_friction`), **distracted** (`distraction_load`), **lost** (`confusion_risk`), or hit **trust/price shocks** (`trust_gap` + `surprise_cost`).
- **E-Commerce & Dropshipping Support (`commerce_profile`, `ecommerce_brand`, `dropshipping_store`):** Models shipping delivery delays, hidden checkout shipping shocks, return-policy trust sensitivity, Add-to-Cart %, Cart Abandonment %, Store Conversion Rate, Simulated CPA, Unit Margin after ad spend, and Break-Even Max CPC.
- Two new benchmark example specs: `examples/dropshipping-store.json` and `examples/ecommerce-dtc-brand.json`.
- Expanded interactive browser demo (`docs/index.html`) with live UX Funnel Drop-Off visualization, E-Commerce Unit Economics breakdown, and 11-language support.
- Expanded `unittest` suite (`10` tests) verifying backward compatibility for v1 specs alongside UX funnel and e-commerce unit economics checks.

## [1.0.0] - 2026-11-27

### Added
- Portable `SKILL.md` adhering to the Agent Skills open specification (`agentskills.io`).
- Adaptive pre-simulation sizing engine (`scripts/size_swarm.py`) enforcing a strict minimum of `1,000` virtual personas and scaling dynamically up to `25,000+` based on product complexity, geography, regulatory exposure, segments, and lifecycle stage.
- Multi-round Agent-Based Crowd Simulator (`scripts/simulate_crowd.py`) using Python 3 standard library only, supporting Monte Carlo confidence intervals across runs, cohort breakdown CSVs, stratified trace samples, and Readiness Score rubrics.
- Repository specification & security validator (`scripts/validate_skill.py`).
- Zero-dependency Python packaging (`pyproject.toml`) exposing `pulse-crowd-size` and `pulse-crowd-sim` CLI entry points.
- GitHub Actions CI matrix across Python `3.9`–`3.14` (`.github/workflows/ci.yml`), PyPI Trusted Publishing workflow (`.github/workflows/publish-pypi.yml`), and Dependabot config.
- Interactive web demo (`docs/index.html`) deployed to GitHub Pages and terminal preview SVG (`assets/demo-preview.svg`).
- Community health documentation (`CODE_OF_CONDUCT.md`, `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md`, `SECURITY.md`).
- Reference methodology (`references/methodology.md`), JSON Schema (`references/spec-schema.json`), baseline example specs (`examples/minimal-b2b-cli.json`, `examples/regulated-marketplace.json`), and `unittest` test suite (`tests/test_pulse_crowd_sim.py`).
