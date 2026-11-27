# 🎯 pulse-crowd

> **Comprendi il mercato prima di entrarci.** Simulazione adattiva multi-round di folle virtuali (`1.000`–`25.000+` personas) per agenti di coding IA — metti alla prova lanci di prodotto, barriere di onboarding, equità dei prezzi e rischi normativi prima del rilascio.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · **Italiano** · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamGod16/pulse-crowd?color=green)](https://github.com/SamGod16/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Demo Interattiva Live](https://samgod16.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamGod16/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamGod16/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Anteprima CLI PulseCrowd](../../assets/demo-preview.svg)

---

## Perché PulseCrowd?

| Approccio | Dimensione campione | Rilevamento rischi di minoranza | Determinismo & IC | Portabilità |
| :--- | :--- | :--- | :--- | :--- |
| **Singolo prompt LLM** | 1 persona generica | Nasconde rischi legali e *cold-start* | Nessuno | Solo prompt |
| **Script fisso 10–15 personas** | ~15 personas fisse | Troppo semplificato o rigido | Ad-hoc | Legato a un solo tool |
| **`pulse-crowd` (Questa Skill)** | **Adattivo `1.000` – `25.000+`** | **Stratificato con soglia statistica** | **Monte Carlo deterministico IC 95%** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Cosa fa
1. **Dimensionamento adattivo (`scripts/size_swarm.py`):** Valuta architettura, segmenti, area geografica, piani tariffari e rischio normativo garantendo almeno **`1.000` personas** fino a **`25.000+`**.
2. **Allocazione stratificata:** Preserva la rappresentanza statistica di revisori privacy, aree rurali e critici scettici.
3. **Simulazione in 3 round (`scripts/simulate_crowd.py`):** Scoperta & policy -> Contagio sociale asimmetrico -> Equilibrio alla settimana 2 & conversione B2B con IC al 95%.
4. **Punteggio di maturità (`0–100`):** Blocca il verdetto a `NO-GO` se `rejected_distrust > 15%`.

---

## Installazione rapida

```bash
# Opzione 1: Multi-Agente con npx skills
npx skills add SamGod16/pulse-crowd -g

# Opzione 2: Python CLI con pip
pip install git+https://github.com/SamGod16/pulse-crowd.git
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Documentazione
[SKILL.md](../../SKILL.md) · [spec-schema.json](../../references/spec-schema.json) · [methodology.md](../../references/methodology.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · [SECURITY.md](../../SECURITY.md) · [MIT](../../LICENSE)
