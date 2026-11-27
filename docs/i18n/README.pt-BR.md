# 🎯 pulse-crowd

> **Entenda o mercado antes de entrar nele.** Simulação adaptativa multi-rodadas de multidões virtuais (`1.000` a `25.000+` personas) para agentes de código com IA — teste lançamentos, atritos de onboarding, justiça de preços e risco regulatório antes de publicar.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português** · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Demo Interativa Ao Vivo](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Prévia CLI do PulseCrowd](../../assets/demo-preview.svg)

---

## Por que PulseCrowd?

| Abordagem | Tamanho da amostra | Detecção de riscos minoritários | Determinismo e IC | Portabilidade |
| :--- | :--- | :--- | :--- | :--- |
| **Prompt único no LLM** | 1 persona genérica | Oculta falhas legais e *cold-start* | Nenhum | Apenas prompt |
| **Script fixo de 10–15 personas** | ~15 personas fixas | Simplifica demais ou perde escala | Ad-hoc | Preso a uma ferramenta |
| **`pulse-crowd` (Esta Skill)** | **Adaptativo `1.000` – `25.000+`** | **Estratificado com piso estatístico** | **Monte Carlo determinístico IC 95%** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### O que faz
1. **Dimensionamento adaptativo (`scripts/size_swarm.py`):** Avalia arquitetura do produto, segmentos, alcance geográfico, planos de preço e risco regulatório com **piso mínimo rigoroso de `1.000` personas** até **`25.000+`**.
2. **Alocação estratificada de coortes:** Garante poder estatístico para coortes minoritárias críticas (auditores de privacidade, cidades do interior, críticos vocais).
3. **Simulação de contágio em 3 rodadas (`scripts/simulate_crowd.py`):**
   - **Rodada 1 — Descoberta e barreiras:** Atrito de onboarding, KYC/LGPD, percepção de preço e encaixe de valor.
   - **Rodada 2 — Contágio social assimétrico:** Amplificação negativa para bloqueios de conformidade não resolvidos.
   - **Rodada 3 — Equilíbrio da Semana 2 e Conversão B2B:** Liquidez regional, retenção e intervalo de confiança de 95%.
4. **Pontuação de Prontidão (`0–100`):** Limita o veredicto a `NO-GO` se `rejected_distrust > 15%`.

---

## Instalação rápida

### Opção 1: Via `npx skills` (Multi-Agente)
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### Opção 2: Manual via Git + Symlink
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### Opção 3: CLI Python via `pip`
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Verificar localmente
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## Documentação e Comunidade

- **Fluxo para Agentes:** [SKILL.md](../../SKILL.md) · **Esquema JSON:** [spec-schema.json](../../references/spec-schema.json) · **Metodologia:** [methodology.md](../../references/methodology.md)
- **Contribuir:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **Código de Conduta:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **Segurança:** [SECURITY.md](../../SECURITY.md) · **Licença:** [MIT](../../LICENSE)
