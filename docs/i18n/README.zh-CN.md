# 🎯 pulse-crowd

> **在进入市场前先看清市场。** 面向 AI 编程代理的自适应多轮虚拟人群仿真工具（`1,000` 至 `25,000+` 虚拟用户画像）——在产品上线前压力测试发布表现、注册引导门槛、定价公平性与合规风险。

[English](../../README.md) · [Español](README.es.md) · **简体中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md) · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 在线交互演示](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 GitHub Releases](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 新手友好议题](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![PulseCrowd CLI 预览](../../assets/demo-preview.svg)

---

## 为什么选择 PulseCrowd？

| 方案 | 样本规模 | 少数群体风险发现 | 确定性与置信区间 | 可移植性 |
| :--- | :--- | :--- | :--- | :--- |
| **单条 LLM 发布提示词** | 1 个泛化角色 | 掩盖合规盲区与冷启动死角 | 无 | 仅限文本提示 |
| **固定 10–15 人测试脚本** | 固定 ~15 人 | 样本过小或算力浪费 | 临时拼凑 | 绑定单一工具 |
| **`pulse-crowd`（本 Skill）** | **自适应 `1,000` – `25,000+`** | **分层抽样 + 最大余数保底** | **固定种子蒙特卡洛 95% CI** | **支持 Claude、Codex、Gemini CLI、OpenCode、Cursor、Antigravity** |

### 核心功能
1. **调度前自适应规模计算（`scripts/size_swarm.py`）：** 综合评估产品架构、目标细分市场、地理覆盖、定价层级、获客渠道、监管风险与生命周期阶段，严格强制 **最低 `1,000` 名虚拟用户**，并可自动扩展至 **`25,000+`**。
2. **分层群体配额：** 采用最大余数法分配并设定单群组统计下限，确保合规审查员、偏远地区用户、挑剔意见领袖等少数群体可被量化评估。
3. **三轮智能体社交传染仿真（`scripts/simulate_crowd.py`）：**
   - **第一轮 — 发现与政策门槛：** 评估注册摩擦、隐私/合规阻碍、定价公平性与核心价值匹配度。
   - **第二轮 — 非对称社交传染：** 模拟同侪群体传播与公开舆情扩散，对未解决的合规或强迫付费投诉赋予更高负面权重。
   - **第三轮 — 第二周均衡与 B2B 转化：** 模拟区域流动性缺口、用户留存状态及 B2B Basic/Pro 付费转化率，并跨随机种子计算 95% 置信区间。
4. **透明的上线就绪评分（`0–100`）：** 内置合规信任安全闸门（当不信任拒用率 `rejected_distrust > 15%` 时直接锁定结论为 `NO-GO`）。

---

## 快速安装

### 方式一：通过 `npx skills` 全局安装
```bash
npx skills add SamuelCoreLabs/pulse-crowd -g
```

### 方式二：手动克隆并软链接
```bash
git clone https://github.com/SamuelCoreLabs/pulse-crowd.git ~/skills/pulse-crowd
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.config/opencode/skills
ln -sfn ~/skills/pulse-crowd ~/.agents/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.claude/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.codex/skills/pulse-crowd
ln -sfn ~/skills/pulse-crowd ~/.config/opencode/skills/pulse-crowd
```

### 方式三：通过 `pip` 安装 Python CLI
```bash
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-size --spec examples/minimal-b2b-cli.json
pulse-crowd-sim --spec examples/regulated-marketplace.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### 本地自检
```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

---

## 技术文档与社区

- **Agent Skill 规范：** [SKILL.md](../../SKILL.md) · **JSON Schema：** [spec-schema.json](../../references/spec-schema.json) · **数学方法论：** [methodology.md](../../references/methodology.md)
- **贡献指南：** [CONTRIBUTING.md](../../CONTRIBUTING.md) · **行为准则：** [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · **安全策略：** [SECURITY.md](../../SECURITY.md) · **开源协议：** [MIT](../../LICENSE)
