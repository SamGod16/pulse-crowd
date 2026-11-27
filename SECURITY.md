# Security Policy

## Supported Versions

Only the latest release on the `main` branch (`v1.0.x`) is actively maintained and supported with security fixes.

| Version | Supported |
| :--- | :--- |
| `1.0.x` (`main`) | Yes |

## Reporting a Vulnerability

Please **do not** open public GitHub issues for suspected security vulnerabilities (such as path traversal, unsafe file parsing, workflow injection, or unintended secret exposure).

Instead, report vulnerabilities privately through **[GitHub Private Vulnerability Reporting](https://github.com/SamGod16/pulse-crowd/security/advisories/new)** so they can be verified and patched before public disclosure.

### Security Design Notes

- Core scripts (`scripts/*.py`) run strictly offline using only the Python 3.9+ standard library.
- `scripts/validate_skill.py` automatically scans tracked files for common credential patterns on every CI run.
- Simulation inputs and examples must never include personal identifiable information (PII) or real API credentials.
