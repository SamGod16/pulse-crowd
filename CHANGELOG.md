# Changelog

All notable changes to `mirofish-crowd-sim` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-27

### Added
- Portable `SKILL.md` adhering to the Agent Skills open specification (`agentskills.io`).
- Adaptive pre-simulation sizing engine (`scripts/size_swarm.py`) enforcing a strict minimum of `1,000` virtual personas and scaling dynamically up to `25,000+` based on product complexity, geography, regulatory exposure, segments, and lifecycle stage.
- Multi-round Agent-Based Crowd Simulator (`scripts/simulate_crowd.py`) using Python 3 standard library only, supporting Monte Carlo confidence intervals across runs, cohort breakdown CSVs, stratified trace samples, and Readiness Score rubrics.
- Repository specification & security validator (`scripts/validate_skill.py`).
- Reference methodology (`references/methodology.md`), JSON Schema (`references/spec-schema.json`), two anonymized example specs (`examples/minimal-b2b-cli.json`, `examples/regulated-marketplace.json`), and `unittest` test suite (`tests/test_mirofish_crowd_sim.py`).
