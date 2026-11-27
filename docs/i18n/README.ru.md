# 🎯 pulse-crowd

> **Поймите рынок до выхода на него.** Адаптивная многораундовая симуляция виртуальной аудитории (`1 000` – `25 000+` персон) для ИИ-агентов разработки — стресс-тест запуска продукта, онбординга, ценообразования и регуляторных рисков до релиза.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · **Русский**

[![CI](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamGod16/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamGod16/pulse-crowd?color=green)](https://github.com/SamGod16/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Интерактивное демо](https://samgod16.github.io/pulse-crowd/)** · **[📦 Релизы](https://github.com/SamGod16/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamGod16/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Предпросмотр PulseCrowd CLI](../../assets/demo-preview.svg)

---

## Зачем нужен PulseCrowd?

| Подход | Размер выборки | Выявление рисков меньшинств | Детерминизм и ДИ | Переносимость |
| :--- | :--- | :--- | :--- | :--- |
| **Один промпт в LLM** | 1 обобщённая персона | Скрывает комплаенс и «холодный старт» | Нет | Только промпт |
| **Скрипт на 10–15 персон** | Фикс. ~15 персон | Излишнее упрощение | Разовое решение | Привязка к инструменту |
| **`pulse-crowd` (Этот Skill)** | **Адаптивно `1 000` – `25 000+`** | **Стратификация со стат. минимумом** | **Монте-Карло 95% ДИ** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Ключевые возможности
1. **Адаптивный расчёт размера аудитории (`scripts/size_swarm.py`):** минимум **`1 000`** персон с масштабированием до **`25 000+`** в зависимости от сложности, географии и регуляторного риска.
2. **Стратифицированное распределение когорт:** гарантирует измеримость редких критических групп (аудиторы безопасности, региональные пользователи, скептики).
3. **3 раунда социального заражения (`scripts/simulate_crowd.py`):** Знакомство и барьеры -> Асимметричное социальное влияние -> Равновесие 2-й недели и B2B-конверсия с 95% ДИ.
4. **Защитный барьер (`0–100`):** если `rejected_distrust > 15%`, вердикт принудительно ограничивается статусом `NO-GO`.

---

## Быстрая установка

```bash
# Вариант 1: Глобально через npx skills
npx skills add SamGod16/pulse-crowd -g

# Вариант 2: Python CLI через pip (без внешних зависимостей)
pip install git+https://github.com/SamGod16/pulse-crowd.git
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Документация и сообщество
[SKILL.md](../../SKILL.md) · [spec-schema.json](../../references/spec-schema.json) · [methodology.md](../../references/methodology.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · [SECURITY.md](../../SECURITY.md) · [MIT](../../LICENSE)
