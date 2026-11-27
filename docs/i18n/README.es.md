# 🎯 pulse-crowd

> **Comprende el mercado y la UX dentro de tu app antes de lanzar.** Simulación adaptativa multi-ronda de multitudes virtuales (`1,000` a `25,000+` personas) para agentes IA — detecta en qué pantalla se **atasca**, **distrae** o **pierde** la gente, pon a prueba tiendas **e-commerce y dropshipping**, y valida precios o riesgos legales antes de publicar.

[English](../../README.md) · **Español** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Demo Interactiva en Vivo](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases en GitHub](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Vista previa CLI de PulseCrowd](../../assets/demo-preview.svg)

---

## ¿Por qué PulseCrowd?

| Enfoque | Tamaño de muestra | Detección de riesgos minoritarios | Determinismo y CI | Portabilidad |
| :--- | :--- | :--- | :--- | :--- |
| **Prompt único a un LLM** | 1 persona genérica | Oculta fallos legales y arranque en frío | Ninguno | Solo prompt |
| **Script fijo de 10–15 personas** | ~15 personas fijas | Simplifica en exceso o desperdicia escala | Ad-hoc | Atado a una herramienta |
| **`pulse-crowd` (Esta Skill)** | **Adaptativo `1,000` – `25,000+`** | **Estratificado con mínimo estadístico** | **Monte Carlo con IC 95%** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Caso 1: Dropshipping con Fricción UX vs. Marca DTC Optimizada (`v2.0`)

Simulación directa con `scripts/simulate_crowd.py --runs 3 --seed 42` paso a paso por las pantallas reales (`Landing → Carrito → Registro/Envío → Checkout`):

| Métrica | Tienda Dropshipping ([`dropshipping-store.json`](../../examples/dropshipping-store.json)) | Marca DTC Optimizada ([`ecommerce-dtc-brand.json`](../../examples/ecommerce-dtc-brand.json)) |
| :--- | :--- | :--- |
| **Puntuación Readiness** | **`14.0 / 100`** (`NO-GO`) | **`95.1 / 100`** (`GO`) |
| **Finalización Embudo UX** | **`3.6%`** | **`74.9%`** |
| **Cuello de Botella #1** | `app/checkout/shipping-step.tsx` (`70.0%` caída · `trust_or_price_shock`) | `components/CartDrawer.tsx` (`10.3%` caída · `distracted`) |
| **Add-to-Cart / Conversión** | `2.2%` ATC · `0.15%` CVR (`93.3%` abandono) | `13.0%` ATC · `4.67%` CVR (`63.9%` abandono) |
| **CPC Máximo Rentable** | **`$0.04`** *(quema dinero a `$0.95` CPC)* | **`$2.51`** *(rentable a `$0.85` CPC)* |

### Caso 2: Marketplace Regulado (`6,750` Personas Virtuales)

Simulación real ejecutada con `scripts/simulate_crowd.py` (`--runs 3 --seed 42`) sobre un marketplace regulado antes y después de corregir fricción KYC, riesgos de privacidad de menores y percepción de precios:

| Métrica | Antes (Sin Endurecer) | Después ([`regulated-marketplace.json`](../../examples/regulated-marketplace.json)) |
| :--- | :--- | :--- |
| **Puntuación Readiness** | **`11.7 / 100`** (`±0.35 IC95`) | **`92.3 / 100`** (`±0.07 IC95`) |
| **Sentimiento (`R1 → R2 → R3`)** | `-0.473 → -0.681 → -0.443` | `+0.452 → +0.530 → +0.649` |
| **Retención vs. Rechazos** | `22` activos · `5,838` rechazos por desconfianza | `6,583` activos/promotores · `0` rechazos por desconfianza |
| **Veredicto** | **NO-GO** *(Espiral de rechazo regulatorio)* | **GO** *(Listo para Lanzamiento Fase 1)* |

### Qué hace
1. **Dimensionamiento adaptativo previo (`scripts/size_swarm.py`):** Evalúa la complejidad real (tipo de producto, segmentos, geografía, niveles de precio, canales, riesgo regulatorio y fase) y exige un **mínimo estricto de 1,000 personas virtuales**, escalando hasta **25,000+**.
2. **Asignación estratificada por cohortes:** Usa asignación de Resto Mayor (*Largest Remainder*) garantizando representación estadística para cohortes minoritarias críticas (auditores legales, zonas rurales, críticos escépticos).
3. **Simulación de contagio en 3 rondas (`scripts/simulate_crowd.py`):**
   - **Ronda 1 — Descubrimiento y barreras:** Modela fricción de *onboarding*, bloqueos legales/privacidad, percepción de precios y encaje de valor.
   - **Ronda 2 — Contagio social asimétrico:** Simula influencia entre pares y altavoces públicos con mayor peso negativo ante quejas regulatorias o de pago.
   - **Ronda 3 — Equilibrio en la semana 2 y conversión B2B:** Estima brechas de liquidez regional, retención y conversión B2B con intervalos de confianza Monte Carlo al 95%.
4. **Embudo UX dentro de la aplicación (`ux_journey`):** Simula paso a paso por qué pantalla abandona la gente: **atascados** (`step_friction`), **distraídos** (`distraction_load`), **perdidos** (`confusion_risk`) o **shock de precio/envío** (`surprise_cost`).
5. **E-Commerce y Dropshipping (`commerce_profile`):** Estima tasa Add-to-Cart, abandono de carrito, conversión (CVR), CPA simulado y CPC máximo rentable según AOV, margen y días de envío.
6. **Puntuación de preparación (`0–100`):** Incluye puerta de seguridad regulatoria explícita (`rejected_distrust > 15%` limita el veredicto a `NO-GO`).

Compatible con **cualquier stack tecnológico** del proyecto objetivo (TypeScript, Next.js, Python, Go, Rust, Java, móvil) y respuestas del agente en **cualquier idioma**.

### Asistente guiado y adaptación por tipo de negocio
Al invocar la skill (p. ej. *"usa pulse-crowd para probar mi negocio"*), el agente te pregunta primero en tu idioma **qué tipo de proyecto es** (*Tienda Dropshipping*, *E-Commerce / Marca DTC*, *Futura App móvil/web*, *Futura Web / Funnel de leads*, *SaaS B2B*, *Marketplace* u **Otro proyecto personalizado** donde describes libremente lo que estás creando) y si ya tienes código/tienda o es una idea previa al desarrollo, adaptando las audiencias ([audience-playbooks.md](../../references/audience-playbooks.md)) y pantallas UX a tu caso real.

También puedes lanzar el asistente interactivo en terminal:
```bash
python3 scripts/scaffold_spec.py --interactive --lang es --out /tmp/mi_negocio.json
```

---

## Instalación rápida

### Opción 1: Vía `npx skills` (Multi-Agente)
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### Opción 2: Instalación manual global (Git + Symlink)
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### Opción 3: CLI de Python vía `pip`
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Verificar instalación
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## Documentación técnica y comunidad

- **Flujo para agentes:** [SKILL.md](../../SKILL.md) · **Esquema JSON:** [spec-schema.json](../../references/spec-schema.json) · **Metodología:** [methodology.md](../../references/methodology.md)
- **Contribuciones:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **Código de conducta:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **Seguridad:** [SECURITY.md](../../SECURITY.md) · **Licencia:** [MIT](../../LICENSE)
