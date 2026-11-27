## Summary

<!-- Briefly describe what this PR changes and why. -->

## Related Issue

<!-- Link related issue if applicable: Closes # -->

## Checklist

- [ ] Core scripts (`scripts/*.py`) remain 100% Python 3.9+ standard library with zero external runtime dependencies.
- [ ] Minimum 1,000-persona invariant (`MIN_TOTAL_POPULATION = 1000`) is preserved.
- [ ] Ran `python3 scripts/validate_skill.py` and it passed with zero errors.
- [ ] Ran `python3 -m unittest discover -s tests -v` and all tests passed.
- [ ] Updated docs/examples without including any real user PII or credentials.
