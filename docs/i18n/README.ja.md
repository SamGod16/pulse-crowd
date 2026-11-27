# 🎯 pulse-crowd

> **参入前に市場を理解する。** AI コーディングエージェント向けの適応型マルチラウンド仮想群衆シミュレーション（`1,000`〜`25,000+` ペルソナ）。リリース前にローンチ反応、オンボーディング障壁、価格設定の妥当性、コンプライアンスリスクをストレステストします。

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · **日本語** · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 インタラクティブデモ](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![PulseCrowd CLI プレビュー](../../assets/demo-preview.svg)

---

## PulseCrowd の特長

| アプローチ | サンプル規模 | 少数派リスク検出 | 再現性と信頼区間 | ポータビリティ |
| :--- | :--- | :--- | :--- | :--- |
| **単一プロンプト** | 汎用 1 ペルソナ | 法務監査や地方のコールドスタートを見逃す | なし | プロンプト依存 |
| **固定 10〜15 人スクリプト** | 固定 ~15 人 | 過小評価または過剰実行 | 場当たり的 | 特定ツール専用 |
| **`pulse-crowd`（本スキル）** | **適応型 `1,000` – `25,000+`** | **層化割当＋最大剰余法による下限保証** | **シード固定 Monte Carlo 95% CI** | **Claude, Codex, Gemini CLI, OpenCode, Cursor, Antigravity** |

### 主な機能
1. **実行前適応サイジング (`scripts/size_swarm.py`)：** プロダクト構造、セグメント数、地理範囲、価格帯、規制リスク、ライフサイクルから自動で人口規模を算出し、**最小 `1,000` 人**を厳守しつつ **`25,000+`** まで拡張します。
2. **層化コホート配分：** 規制担当者や懐疑的なパワーユーザーなど少数派コホートも統計的に測定可能にします。
3. **3ラウンド伝播シミュレーション (`scripts/simulate_crowd.py`)：**
   - **Round 1（発見とポリシー障壁）：** オンボーディング摩擦、KYC/プライバシー障壁、価格の妥当性を評価。
   - **Round 2（非対称な社会的伝播）：** コンプライアンス未対応や課金不満によるネガティブ拡散を重み付け。
   - **Round 3（2週目の均衡と B2B 転換）：** 地域流動性、継続区分、B2B 転換率および 95% 信頼区間を算出。
4. **明確な安全性ゲート：** 不信離脱（`rejected_distrust`）が `15%` を超えるとスコアに関わらず判定を `NO-GO` に制限します。

---

## クイックインストール

### オプション 1: `npx skills`（マルチエージェント CLI）
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### オプション 2: 手動インストール（Git + シンボリックリンク）
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### オプション 3: `pip` で Python CLI を導入
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### 動作確認
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## ドキュメント・コミュニティ

- **スキル定義:** [SKILL.md](../../SKILL.md) · **スキーマ:** [spec-schema.json](../../references/spec-schema.json) · **数理モデル:** [methodology.md](../../references/methodology.md)
- **貢献ガイド:** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **行動規範:** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **セキュリティ:** [SECURITY.md](../../SECURITY.md) · **ライセンス:** [MIT](../../LICENSE)
