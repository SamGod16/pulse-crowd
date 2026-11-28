# 🎯 pulse-crowd

> **Comprenez le marché — et l'UX interne de votre app — avant le lancement.** Simulation adaptative multi-tours de foules virtuelles et d'entonnoir UX (`1 000` à `25 000+` personas) pour agents IA — demande quel projet vous lancez (*dropshipping, e-commerce/DTC, future app/web pré-code, SaaS B2B, marketplace ou projet sur mesure*), repère où les utilisateurs **bloquent**, **se distraient** ou **se perdent**, et calcule la conversion et le **Break-Even Max CPC** avant de dépenser en publicité.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Français** · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Démo Interactive en Ligne](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases GitHub](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Aperçu CLI PulseCrowd](../../assets/demo-preview.svg)

---

## Pourquoi PulseCrowd ?

| Approche | Taille d'échantillon | Détection des risques minoritaires | Déterminisme & IC | Portabilité |
| :--- | :--- | :--- | :--- | :--- |
| **Prompt LLM unique** | 1 persona générique | Masque conformité et zones froides | Aucun | Prompt seul |
| **Script fixe de 10–15 personas** | ~15 personas fixes | Sous-représentatif ou rigide | Ad-hoc | Verrouillé |
| **`pulse-crowd` (Cette Skill)** | **Adaptatif `1 000` – `25 000+`** | **Stratifié avec plancher statistique** | **Monte Carlo déterministe IC 95 %** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Étape 0 : Accueil guidé & 7 modèles d'activité (`v2.1` – `v2.2`)
Invoquez `"run pulse-crowd"` (ou `python3 scripts/scaffold_spec.py --interactive`) : l'agent vous demande d'abord **quel projet vous créez** et s'il existe déjà un **code/thème Shopify** ou une **idée pré-code** ([audience-playbooks.md](../../references/audience-playbooks.md)) :
1. **Boutique Dropshipping** (`dropshipping_store`) — trafic froid TikTok/Meta, délais `10–25` j., popups, frais cachés, **Break-Even Max CPC**.
2. **Marque E-Commerce / DTC** (`ecommerce_brand`) — tailles/retours, panier glissant, checkout express, taux Add-to-Cart, CVR & CPA.
3. **Future App Mobile / Web** *(pré-code)* (`mobile_app`) — valeur dès le premier écran, inscription/KYC forcé, permissions, paywall.
4. **Futur Site Web / Tunnel de Leads** *(pré-code)* (`website_funnel`) — clarté du hero, tarification transparente, prise de RDV/formulaire.
5. **SaaS B2B & Outils Dev** (`b2b_saas` / `developer_tool`) — docs, essai gratuit/API, conversion *Basic* vs *Pro* et auditeurs sécurité.
6. **Marketplace Bilatérale / Plateforme Régulée** (`two_sided_marketplace` / `regulated_platform`) — liquidité locale, RGPD/KYC et barrière `> 15 %`.
7. **Autre / Projet Personnalisé (`v2.2`)** (`custom_project`) — extensions navigateur, bots Discord/Telegram, formations, newsletters, jeux indie ou services locaux.

### Étude de cas : Dropshipping à friction vs Marque DTC optimisée (`v2.0+`)
| Indicateur | Dropshipping cassé ([`dropshipping-store.json`](../../examples/dropshipping-store.json)) | Marque DTC optimisée ([`ecommerce-dtc-brand.json`](../../examples/ecommerce-dtc-brand.json)) |
| :--- | :--- | :--- |
| **Score Readiness** | **`14.0 / 100`** (`NO-GO`) | **`95.1 / 100`** (`GO`) |
| **Achèvement Funnel UX** | **`3.6%`** (`shipping-step` `70.0%` choc prix) | **`74.9%`** (`CartDrawer` `10.3%` distrait) |
| **CVR / Break-Even Max CPC** | `0.15%` CVR · **`$0.04`** *(perte à `$0.95`)* | `4.67%` CVR · **`$2.51`** *(rentable à `$0.85`)* |

### Fonctionnalités principales
1. **Dimensionnement adaptatif (`scripts/size_swarm.py`) :** Minimum strict de **`1 000` personas** jusqu'à **`25 000+`**.
2. **Allocation stratifiée :** Méthode au plus fort reste préservant les auditeurs légaux et acheteurs sceptiques.
3. **Simulation en 3 tours (`scripts/simulate_crowd.py`) :** Découverte & barrières → Contagion sociale asymétrique → Équilibre Semaine 2 & IC 95 %.
4. **Entonnoir UX écran par écran (`ux_journey`) :** Distingue **bloqués** (`stuck`), **distraits** (`distracted`), **perdus** (`lost`) et **choc prix/confiance**.
5. **Économie unitaire E-Commerce (`commerce_profile`) :** Add-to-Cart, abandon panier, CVR, CPA simulé et Break-Even Max CPC.
6. **Barrière de sécurité (`0–100`) :** `rejected_distrust > 15%` plafonne le verdict à `NO-GO`.

---

## Installation rapide

### Option 1 : Via `npx skills` (Multi-Agent)
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### Option 2 : Manuelle (Git + Symlink)
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### Option 3 : CLI Python via `pip`
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-init --interactive --lang en --out /tmp/my_project_spec.json
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/dropshipping-store.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Vérification locale
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## Documentation & Communauté

- **Spécification Agent Skill :** [SKILL.md](../../SKILL.md) · **Schéma JSON :** [spec-schema.json](../../references/spec-schema.json) · **Méthodologie :** [methodology.md](../../references/methodology.md)
- **Contribuer :** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **Code de conduite :** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **Sécurité :** [SECURITY.md](../../SECURITY.md) · **Licence :** [MIT](../../LICENSE)
