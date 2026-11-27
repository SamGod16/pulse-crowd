# Contributing to `pulse-crowd`

Contributions, bug reports, calibration improvements, example specs, and documentation fixes are welcome!

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) when participating in issues or pull requests.

## Development Principles

1. **Zero external runtime dependencies:** Keep `scripts/*.py` strictly within the Python 3.9+ standard library so the skill works immediately across AI agent sandboxes without network package installs.
2. **Enforce the 1,000-persona floor:** Never bypass `MIN_TOTAL_POPULATION = 1000` or skip pre-simulation adaptive sizing in `scripts/size_swarm.py`.
3. **Agent Skills spec compliance:** Ensure `SKILL.md` frontmatter and links continue to pass `scripts/validate_skill.py`.
4. **Privacy & safety:** Never submit real user data, private company credentials, or API keys in examples or fixtures.

## Running Checks & Demo Locally

```bash
# 1. Validate SKILL.md frontmatter, links, JSON specs, and secret scan
python3 scripts/validate_skill.py

# 2. Run the full unittest suite
python3 -m unittest discover -s tests -v

# 3. Preview the interactive web demo locally
python3 -m http.server --directory docs 8080
```

## Pull Request Process

1. Fork the repository and create a topic branch from `main`.
2. Make focused changes and add unit tests in [tests/test_pulse_crowd_sim.py](tests/test_pulse_crowd_sim.py) for behavioral updates.
3. Verify both `validate_skill.py` and `unittest` exit with code `0` before opening a pull request.
4. Check our [good first issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) if you are looking for a place to start.
