# 🎯 pulse-crowd

> **시장에 진입하기 전에 먼저 시장을 이해하세요.** AI 코딩 에이전트를 위한 적응형 다중 라운드 가상 군중 시뮬레이션(`1,000` ~ `25,000+` 페르소나) — 출시 전 온보딩 장벽, 가격 공정성, 규제 리스크를 스트레스 테스트합니다.

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **한국어** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 라이브 인터랙티브 데모](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![PulseCrowd CLI 미리보기](../../assets/demo-preview.svg)

---

## 왜 PulseCrowd인가요?

| 접근 방식 | 샘플 규모 | 소수 집단 리스크 탐지 | 결정론적 재현 및 CI | 이식성 |
| :--- | :--- | :--- | :--- | :--- |
| **단일 LLM 프롬프트** | 일반 페르소나 1명 | 법적 감사·지역 콜드스타트 누락 | 없음 | 프롬프트 전용 |
| **고정 10–15명 스크립트** | 고정 ~15명 | 과소 대표 또는 불필요한 연산 | 임시 스크립트 | 특정 도구 종속 |
| **`pulse-crowd` (본 스킬)** | **적응형 `1,000` – `25,000+`** | **층화 배정 + 최대 잔여법 하한 보장** | **시드 기반 Monte Carlo 95% CI** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### 주요 기능
1. **실행 전 적응형 규모 산정 (`scripts/size_swarm.py`):** 제품 구조, 세그먼트, 지역 범위, 요금제, 규제 위험도에 따라 **최소 `1,000`명**을 보장하고 **`25,000+`명**까지 자동 확장합니다.
2. **층화 코호트 배분:** 규제 검토자나 회의적인 파워 유저 같은 핵심 소수 그룹도 측정 가능하도록 최소 통계 표본을 유지합니다.
3. **3라운드 사회적 전파 시뮬레이션 (`scripts/simulate_crowd.py`):**
   - **1라운드 — 발견 및 정책 관문:** 온보딩 마찰, 개인정보·규제 장벽, 가격 공정성을 모델링합니다.
   - **2라운드 — 비대칭 사회적 전파:** 미해결 규제/과금 불만에 더 높은 부정 가중치를 부여해 여론 확산을 계산합니다.
   - **3라운드 — 2주차 균형 및 B2B 전환:** 지역 유동성 격차, 유지율, B2B 전환율과 95% 신뢰구간을 산출합니다.
4. **투명한 준비도 점수 (`0–100`):** 불신 이탈률(`rejected_distrust > 15%`) 발생 시 `NO-GO` 안전 게이트를 적용합니다.

---

## 빠른 설치

### 옵션 1: `npx skills`로 전역 설치
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### 옵션 2: 수동 설치 (Git + 심볼릭 링크)
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### 옵션 3: `pip`으로 Python CLI 설치
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### 검증 실행
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## 기술 문서 및 커뮤니티

- **Skill 가이드:** [SKILL.md](../../SKILL.md) · **JSON 스키마:** [spec-schema.json](../../references/spec-schema.json) · **방법론:** [methodology.md](../../references/methodology.md)
- **기여 가이드:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **행동 강령:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **보안:** [SECURITY.md](../../SECURITY.md) · **라이선스:** [MIT](../../LICENSE)
