# 🎯 pulse-crowd

> **Поймите рынок и UX внутри продукта до запуска.** Пошаговый адаптивный симулятор виртуальной аудитории и UX-воронки (`1 000` – `25 000+` персон) для ИИ-агентов разработки — сначала уточняет тип бизнеса (*дропшиппинг, DTC-бренды, будущие приложения и сайты до написания кода, B2B SaaS, маркетплейсы или кастомные проекты*), находит экраны, где пользователи **застревают**, **отвлекаются** или **теряются**, и оценивает CVR и **Break-Even Max CPC** до запуска рекламы.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · **Русский**

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 Интерактивное демо](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Релизы](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![Предпросмотр PulseCrowd CLI](../../assets/demo-preview.svg)

---

## Зачем нужен PulseCrowd?

| Подход | Размер выборки | Выявление рисков меньшинств | Детерминизм и ДИ | Переносимость |
| :--- | :--- | :--- | :--- | :--- |
| **Один промпт в LLM** | 1 обобщённая персона | Скрывает комплаенс и «холодный старт» | Нет | Только промпт |
| **Скрипт на 10–15 персон** | Фикс. ~15 персон | Излишнее упрощение | Разовое решение | Привязка к инструменту |
| **`pulse-crowd` (Этот Skill)** | **Адаптивно `1 000` – `25 000+`** | **Стратификация со стат. минимумом** | **Монте-Карло 95% ДИ** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### Шаг 0: Управляемый опрос и 7 бизнес-вертикалей (`v2.1` – `v2.2`)
Запустите `"run pulse-crowd"` (или `python3 scripts/scaffold_spec.py --interactive`): агент сначала уточнит **тип бизнеса** и стадию (готовый **код/тема Shopify** или **идея до разработки**), подбирая профили и экраны по [audience-playbooks.md](../../references/audience-playbooks.md):
1. **Dropshipping-магазин** (`dropshipping_store`) — холодный трафик TikTok/Meta, доставка `10–25` дней, попапы, скрытая доставка, **Break-Even Max CPC**.
2. **E-Commerce / DTC-бренд** (`ecommerce_brand`) — размер/возвраты, выдвижная корзина, экспресс-оплата, ATC, CVR и CPA.
3. **Будущее мобильное/веб-приложение** *(до кода)* (`mobile_app`) — первый экран, ранняя регистрация/KYC, разрешения и пейволл.
4. **Будущий сайт / лид-воронка** *(до кода)* (`website_funnel`) — ясность первого экрана, отзывы, прозрачность цен и форма заявки.
5. **B2B SaaS и DevTools** (`b2b_saas` / `developer_tool`) — документация, триал/авторизация, первый API-вызов и конверсия *Basic/Pro*.
6. **Двусторонний маркетплейс / регуляторная платформа** (`two_sided_marketplace` / `regulated_platform`) — локальная ликвидность, GDPR/KYC и порог `> 15%`.
7. **Другой / кастомный проект (`v2.2`)** (`custom_project`) — расширения браузера, боты Discord/Telegram, курсы, рассылки, инди-игры, локальные сервисы.

### Кейс: проблемный дропшиппинг vs. оптимизированный DTC-бренд (`v2.0+`)
| Метрика | Проблемный Dropshipping ([`dropshipping-store.json`](../../examples/dropshipping-store.json)) | Оптимизированный DTC ([`ecommerce-dtc-brand.json`](../../examples/ecommerce-dtc-brand.json)) |
| :--- | :--- | :--- |
| **Readiness Score** | **`14.0 / 100`** (`NO-GO`) | **`95.1 / 100`** (`GO`) |
| **Прохождение UX-воронки** | **`3.6%`** (`shipping-step` `70.0%` ценовой шок) | **`74.9%`** (`CartDrawer` `10.3%` отвлечение) |
| **CVR / Break-Even Max CPC** | `0.15%` CVR · **`$0.04`** *(убыток при `$0.95`)* | `4.67%` CVR · **`$2.51`** *(прибыльно при `$0.85`)* |

### Ключевые возможности
1. **Адаптивный расчёт выборки (`scripts/size_swarm.py`):** минимум **`1 000`** с масштабированием до **`25 000+`** персон.
2. **Стратифицированное распределение когорт:** гарантирует измеримость критических меньшинств (аудиторы, скептики).
3. **3 раунда социального заражения (`scripts/simulate_crowd.py`):** Барьеры → Асимметричный негатив → Равновесие 2-й недели и 95% ДИ.
4. **Поэкранная UX-воронка (`ux_journey`):** разделяет **застревания** (`stuck`), **отвлечения** (`distracted`), **потерю навигации** (`lost`) и **шок цены/доверия**.
5. **Юнит-экономика E-Commerce (`commerce_profile`):** ATC, брошенные корзины, CVR, расчётный CPA и Break-Even Max CPC.
6. **Защитный барьер (`0–100`):** если `rejected_distrust > 15%`, вердикт ограничивается `NO-GO`.

---

## Быстрая установка

### Вариант 1: Через `npx skills` (Мульти-агентный CLI)
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### Вариант 2: Вручную через Git + Symlink
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### Вариант 3: Python CLI через `pip`
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-init --interactive --lang en --out /tmp/my_project_spec.json
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/dropshipping-store.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### Локальная проверка
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## Документация и сообщество

- **Спецификация Agent Skill:** [SKILL.md](../../SKILL.md) · **JSON Schema:** [spec-schema.json](../../references/spec-schema.json) · **Методология:** [methodology.md](../../references/methodology.md)
- **Участие в разработке:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **Кодекс поведения:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **Безопасность:** [SECURITY.md](../../SECURITY.md) · **Лицензия:** [MIT](../../LICENSE)
