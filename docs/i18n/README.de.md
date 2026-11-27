# 🎯 pulse-crowd

> **Den Markt verstehen, bevor man ihn betritt.** Adaptive, mehrstufige virtuelle Crowd-Simulation (`1.000` bis `25.000+` Personas) für KI-Coding-Agents — testen Sie Produktlaunches, Onboarding-Hürden, Preismodelle und Compliance-Risiken vor dem Release.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · **Deutsch** · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamGod16/pulse-crowd?color=green)](https://github.com/SamGod16/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Interaktive Live-Demo](https://samgod16.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamGod16/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamGod16/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![PulseCrowd CLI-Vorschau](../../assets/demo-preview.svg)

---

## Warum PulseCrowd?

| Ansatz | Stichprobengröße | Erkennung von Minderheitsrisiken | Determinismus & CI | Portabilität |
| :--- | :--- | :--- | :--- | :--- |
| **Einzelner LLM-Prompt** | 1 generische Persona | Verbirgt Compliance- & Cold-Start-Risiken | Keiner | Nur Prompt |
| **Fixes 10–15 Personas Skript** | Fix ~15 Personas | Übervereinfacht oder unflexibel | Ad-hoc | Tool-gebunden |
| **`pulse-crowd` (Dieser Skill)** | **Adaptiv `1.000` – `25.000+`** | **Stratifiziert mit statistischem Minimum** | **Monte-Carlo-95%-Konfidenzintervall** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Funktionen
1. **Adaptives Pre-Dispatch-Sizing (`scripts/size_swarm.py`):** Bewertet Produktarchitektur, Segmente, Geografie, Preisstufen und Regulierungsrisiken mit einem **strikten Minimum von `1.000` Personas** bis **`25.000+`**.
2. **Stratifizierte Kohorten-Verteilung:** Hare-Niemeyer-Verfahren (*Largest Remainder*) stellt sicher, dass kritische Minderheiten (Datenschutzprüfer, ländliche Regionen, Kritiker) messbar bleiben.
3. **3-Runden-Kontagion-Simulation (`scripts/simulate_crowd.py`):**
   - **Runde 1 — Discovery & Policy-Gates:** Onboarding-Reibung, DSGVO/KYC-Hürden und Preisakzeptanz.
   - **Runde 2 — Asymmetrische soziale Ansteckung:** Stärkere Negativgewichtung bei ungelösten Compliance- oder Bezahlschranken-Problemen.
   - **Runde 3 — Woche-2-Gleichgewicht & B2B-Conversion:** Regionale Liquidität, Retention und 95%-KI über mehrere Seeds.
4. **Klares Sicherheits-Gate (`0–100`):** Bei `rejected_distrust > 15%` wird das Urteil auf `NO-GO` begrenzt.

---

## Schnellinstallation

### Option 1: Global via `npx skills`
```bash
npx skills add SamGod16/pulse-crowd -g
```

### Option 2: Manuell via Git + Symlink
```bash
git clone https://github.com/SamGod16/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### Option 3: Python-CLI via `pip`
```bash
pip install git+https://github.com/SamGod16/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Prüfung ausführen
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## Dokumentation & Community

- **Agent-Workflow:** [SKILL.md](../../SKILL.md) · **JSON-Schema:** [spec-schema.json](../../references/spec-schema.json) · **Methodik:** [methodology.md](../../references/methodology.md)
- **Mitwirken:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **Verhaltenskodex:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **Sicherheit:** [SECURITY.md](../../SECURITY.md) · **Lizenz:** [MIT](../../LICENSE)
