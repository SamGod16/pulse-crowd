# Contributing to `mirofish-crowd-sim`

Contributions, bug reports, calibration improvements, and documentation fixes are welcome.

## Development Principles

1. **Zero external runtime dependencies:** Keep `scripts/*.py` strictly within the Python 3.9+ standard library so the skill works immediately across AI agent sandboxes without network package installs.
2. **Enforce the 1,000-persona floor:** Never bypass `MIN_TOTAL_POPULATION = 1000` or skip pre-simulation adaptive sizing in `scripts/size_swarm.py`.
3. **Agent Skills spec compliance:** Ensure `SKILL.md` frontmatter and links continue to pass `scripts/validate_skill.py`.
4. **Privacy & safety:** Never submit real user data, private company credentials, or API keys in examples or fixtures.

## Running Checks Locally

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

Please ensure both commands exit with code `0` before opening a pull request.
