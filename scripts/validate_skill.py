#!/usr/bin/env python3
"""
Skill Package & Agent Skills Specification Validator for pulse-crowd.

Verifies:
1. SKILL.md YAML frontmatter obeys agentskills.io naming, length, and required fields.
2. Relative markdown links in SKILL.md and README.md point to real existing files.
3. Example JSON files validate cleanly against project sizing/simulation rules.
4. No accidental secret patterns exist in tracked text files.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAME_REGEX = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_REGEX = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)#]+)")
SECRET_REGEXES = [
    re.compile(r"sk-ant-[A-Za-z0-9\-_]{12,}"),
    re.compile(r"sk_(?:live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md closing YAML frontmatter '---' not found")
    block = text[4:end]
    result: dict[str, str] = {}
    current_key: str | None = None
    buffer: list[str] = []

    for line in block.splitlines():
        if line.startswith((" ", "\t")) and current_key is not None:
            buffer.append(line.strip())
            continue
        if current_key is not None:
            result[current_key] = " ".join(buffer).strip()
            current_key = None
            buffer = []
        if ":" in line and not line.strip().startswith("#"):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val in (">-", "|", ">", "|-"):
                current_key = key
                buffer = []
            elif val:
                result[key] = val.strip('"').strip("'")
            else:
                current_key = key
                buffer = []
    if current_key is not None:
        result[current_key] = " ".join(buffer).strip()
    return result


def validate_repo(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        return ["Missing required SKILL.md at repository root"]

    skill_text = skill_md.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(skill_text)
    except ValueError as exc:
        return [str(exc)]

    name = fm.get("name", "")
    description = fm.get("description", "")
    compatibility = fm.get("compatibility", "")

    if not name or len(name) > 64 or not NAME_REGEX.match(name):
        errors.append(
            f"Invalid frontmatter 'name': '{name}' (must be <=64 chars matching ^[a-z0-9]+(-[a-z0-9]+)*$)"
        )
    if not description or len(description) > 1024:
        errors.append("Frontmatter 'description' must be 1..1024 characters")
    if compatibility and len(compatibility) > 500:
        errors.append("Frontmatter 'compatibility' must be <=500 characters")

    for doc_name in ("SKILL.md", "README.md", "CONTRIBUTING.md"):
        doc_path = root / doc_name
        if not doc_path.exists():
            continue
        doc_text = doc_path.read_text(encoding="utf-8")
        for match in LINK_REGEX.finditer(doc_text):
            rel = match.group(1).strip()
            target = (doc_path.parent / rel).resolve()
            if not target.exists():
                errors.append(f"Broken relative link in {doc_name}: {rel}")

    examples_dir = root / "examples"
    if examples_dir.exists():
        for ex in sorted(examples_dir.glob("*.json")):
            try:
                data = json.loads(ex.read_text(encoding="utf-8"))
                if "cohorts" not in data or len(data["cohorts"]) < 2:
                    errors.append(f"Example {ex.name} must define >=2 cohorts")
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in {ex.name}: {exc}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in (".git", "__pycache__", "sim_output") for part in path.parts):
            continue
        if path.suffix in (".pyc", ".png", ".jpg", ".zip"):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pat in SECRET_REGEXES:
            if pat.search(content):
                errors.append(f"Potential credential pattern matched in {path.relative_to(root)}")

    return errors


def main() -> int:
    errors = validate_repo()
    if errors:
        print("Skill validation FAILED:", file=sys.stderr)
        for err in errors:
            print(f" - {err}", file=sys.stderr)
        return 1
    print("Skill validation PASSED: SKILL.md frontmatter, links, schemas, and secret scan are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
