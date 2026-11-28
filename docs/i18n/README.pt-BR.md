# 🎯 pulse-crowd

> **Entenda o mercado — e a UX dentro do seu app — antes de lançar.** Simulação guiada e adaptativa de multidões virtuais e funil UX (`1.000` a `25.000+` personas) para agentes de IA — pergunta primeiro qual negócio você está construindo (*dropshipping, e-commerce/DTC, futuro app/site pré-código, SaaS B2B, marketplace ou projeto custom*), mostra onde usuários **travam**, **se distraem** ou **se perdem**, e estima CVR e **Break-Even Max CPC** antes de gastar com anúncios.

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

### Passo 0: Intake Guiado & 7 Verticais de Negócio (`v2.1` – `v2.2`)
Ao chamar `"run pulse-crowd"` (ou `python3 scripts/scaffold_spec.py --interactive`), o agente pergunta primeiro **o que você está criando** e se já existe **código/loja Shopify** ou uma **ideia pré-código** ([audience-playbooks.md](../../references/audience-playbooks.md)):
1. **Loja Dropshipping** (`dropshipping_store`) — tráfego frio TikTok/Meta, entrega `10–25` dias, popups, frete surpresa e **Break-Even Max CPC**.
2. **E-Commerce / Marca DTC** (`ecommerce_brand`) — dúvidas de tamanho/troca, carrinho lateral, checkout express, ATC, CVR e CPA.
3. **Futuro App Mobile / Web** *(pré-código)* (`mobile_app`) — gancho inicial, cadastro/KYC precoce, permissões e paywall.
4. **Futuro Site / Funil de Leads** *(pré-código)* (`website_funnel`) — clareza da headline, prova social, preços visíveis e formulário/agenda.
5. **SaaS B2B & Ferramentas Dev** (`b2b_saas` / `developer_tool`) — docs, trial/auth, primeira chamada API e conversão *Basic* vs *Pro*.
6. **Marketplace Bilateral ou Plataforma Regulada** (`two_sided_marketplace` / `regulated_platform`) — liquidez local, LGPD/KYC e trava `> 15%`.
7. **Outro / Projeto Personalizado (`v2.2`)** (`custom_project`) — extensões, bots de Discord/Telegram, cursos, newsletters, jogos indie ou serviços locais.

### Estudo de Caso: Dropshipping com Fricção vs. Marca DTC Otimizada (`v2.0+`)
| Métrica | Dropshipping Quebrado ([`dropshipping-store.json`](../../examples/dropshipping-store.json)) | Marca DTC Otimizada ([`ecommerce-dtc-brand.json`](../../examples/ecommerce-dtc-brand.json)) |
| :--- | :--- | :--- |
| **Readiness Score** | **`14.0 / 100`** (`NO-GO`) | **`95.1 / 100`** (`GO`) |
| **Conclusão Funil UX** | **`3.6%`** (`shipping-step` `70.0%` choque preço) | **`74.9%`** (`CartDrawer` `10.3%` distração) |
| **CVR / Break-Even Max CPC** | `0.15%` CVR · **`$0.04`** *(prejuízo a `$0.95`)* | `4.67%` CVR · **`$2.51`** *(lucrativo a `$0.85`)* |

### O que faz
1. **Dimensionamento adaptativo (`scripts/size_swarm.py`):** Garante **mínimo rigoroso de `1.000` personas** até **`25.000+`**.
2. **Alocação estratificada de coortes:** Preserva poder estatístico para auditores de privacidade e compradores céticos.
3. **Simulação em 3 rodadas (`scripts/simulate_crowd.py`):** Descoberta → Contágio social assimétrico → Equilíbrio Semana 2 e IC 95%.
4. **Funil UX tela por tela (`ux_journey`):** Identifica **travados** (`stuck`), **distraídos** (`distracted`), **perdidos** (`lost`) e **choque de preço/confiança**.
5. **Economia Unitária E-Commerce (`commerce_profile`):** Add-to-Cart, abandono de carrinho, CVR, CPA simulado e Break-Even Max CPC.
6. **Trava de Segurança (`0–100`):** Limita o veredito a `NO-GO` se `rejected_distrust > 15%`.

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
pulse-crowd-init --interactive --lang en --out /tmp/my_project_spec.json
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/dropshipping-store.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
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
