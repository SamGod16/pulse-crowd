# 🎯 pulse-crowd

> **출시 전에 시장 반응과 앱 내부 UX를 동시에 검증하세요.** AI 코딩 에이전트를 위한 가이드형 적응식 가상 군중 & UX 퍼널 시뮬레이터(`1,000` ~ `25,000+` 페르소나) — 먼저 어떤 비즈니스를 구축 중인지(*드롭쉬핑, DTC 이커머스, 코드 작성 전 미래 앱/웹사이트, B2B SaaS, 마켓플레이스, 커스텀 프로젝트*) 질문하고, 사용자가 어느 화면에서 **막히고**·**산만해지고**·**길을 잃는지** 추적하며 광고 집행 전 CVR과 **손익분기 Max CPC**를 계산합니다.

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

### Step 0: 가이드형 비즈니스 인테이크 및 7개 버티컬 (`v2.1` – `v2.2`)
`"run pulse-crowd"`를 호출하거나 `python3 scripts/scaffold_spec.py --interactive`를 실행하면 먼저 **프로젝트 유형**과 **기존 코드/Shopify 테마 여부 또는 코드 작성 전 기획 단계**인지 질문합니다([audience-playbooks.md](../../references/audience-playbooks.md)):
1. **드롭쉬핑 스토어** (`dropshipping_store`) — TikTok/Meta 콜드 트래픽, `10–25`일 배송 지연, 스핀 팝업, 숨겨진 배송비 충격, **손익분기 Max CPC**.
2. **DTC 이커머스 브랜드** (`ecommerce_brand`) — 사이즈/반품 정책, 슬라이드 장바구니, 간편 결제, 장바구니 담기(ATC)·CVR·CPA.
3. **미래 모바일 / 웹 앱** *(코드 작성 전)* (`mobile_app`) — 첫 화면 가치 전달, 조기 가입/KYC 장벽, 권한 요청 및 페이월 이탈.
4. **미래 웹사이트 / 리드 퍼널** *(코드 작성 전)* (`website_funnel`) — 히어로 카피 명확성, 사회적 증거, 요금 투명성 및 신청 폼 이탈.
5. **B2B SaaS 및 개발자 도구** (`b2b_saas` / `developer_tool`) — 문서 이해도, 인증/트라이얼 마찰, 첫 API 호출 및 *Basic/Pro* 전환율.
6. **양면 마켓플레이스 / 규제 플랫폼** (`two_sided_marketplace` / `regulated_platform`) — 지역 유동성 격차, 개인정보·규제, `> 15%` 안전 게이트.
7. **기타 / 커스텀 프로젝트 (`v2.2`)** (`custom_project`) — 브라우저 확장프로그램, Discord/Telegram 봇, 강의, 뉴스레터, 인디 게임, 로컬 서비스.

### 사례 비교: 고마찰 드롭쉬핑 vs. 최적화 DTC 스토어 (`v2.0+`)
| 지표 | 고마찰 드롭쉬핑 ([`dropshipping-store.json`](../../examples/dropshipping-store.json)) | 최적화 DTC 브랜드 ([`ecommerce-dtc-brand.json`](../../examples/ecommerce-dtc-brand.json)) |
| :--- | :--- | :--- |
| **준비도 점수 (Readiness)** | **`14.0 / 100`** (`NO-GO`) | **`95.1 / 100`** (`GO`) |
| **UX 퍼널 완주율** | **`3.6%`** (`shipping-step` `70.0%` 가격 충격) | **`74.9%`** (`CartDrawer` `10.3%` 산만함) |
| **CVR / 손익분기 Max CPC** | `0.15%` CVR · **`$0.04`** *(`$0.95` 클릭당 손실)* | `4.67%` CVR · **`$2.51`** *(`$0.85` 클릭당 수익)* |

### 주요 기능
1. **실행 전 적응형 규모 산정 (`scripts/size_swarm.py`):** **최소 `1,000`명**부터 **`25,000+`명**까지 자동 확장.
2. **층화 코호트 배분:** 규제 검토자 및 가격 민감형 비평가의 통계적 대표성 유지.
3. **3라운드 사회적 전파 시뮬레이션 (`scripts/simulate_crowd.py`):** 발견 장벽 → 비대칭 여론 확산 → 2주차 유지율 및 95% CI.
4. **화면별 인앱 UX 퍼널 (`ux_journey`):** **막힘** (`stuck`), **산만함** (`distracted`), **이탈/혼란** (`lost`), **가격/신뢰 충격** 정밀 추적.
5. **이커머스 단위 경제성 (`commerce_profile`):** ATC, 장바구니 이탈률, 스토어 CVR, 예상 CPA 및 손익분기 Max CPC 산출.
6. **투명한 안전 게이트 (`0–100`):** 불신 이탈률 `rejected_distrust > 15%` 시 `NO-GO` 자동 제한.

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

### 옵션 3: `pip`를 통한 Python CLI 설치
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-init --interactive --lang en --out /tmp/my_project_spec.json
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/dropshipping-store.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### 로컬 검증
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## 문서 및 커뮤니티

- **에이전트 스킬 명세:** [SKILL.md](../../SKILL.md) · **JSON 스키마:** [spec-schema.json](../../references/spec-schema.json) · **방법론:** [methodology.md](../../references/methodology.md)
- **기여하기:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **행동 강령:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **보안:** [SECURITY.md](../../SECURITY.md) · **라이선스:** [MIT](../../LICENSE)
