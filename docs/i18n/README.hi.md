# 🎯 pulse-crowd

> **बाज़ार में उतरने से पहले बाज़ार को समझें।** AI कोडिंग एजेंट्स के लिए अनुकूली मल्टी-राउंड वर्चुअल क्राउड सिमुलेशन (`1,000` से `25,000+` वर्चुअल पर्सोना) — लॉन्च से पहले ऑनबोर्डिंग, प्राइसिंग और रेगुलेटरी जोखिमों की स्ट्रेस-टेस्टिंग करें।

[English](../../README.md) · [Español](README.es.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · **हिन्दी** · [Русский](README.ru.md)

[![CI](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelCoreLabs/pulse-crowd/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SamuelCoreLabs/pulse-crowd?color=green)](https://github.com/SamuelCoreLabs/pulse-crowd/releases)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.9+ stdlib](https://img.shields.io/badge/Python-3.9%2B%20stdlib-informational.svg)

**[📊 लाइव इंटरैक्टिव डेमो](https://samuelcorelabs.github.io/pulse-crowd/)** · **[📦 Releases](https://github.com/SamuelCoreLabs/pulse-crowd/releases)** · **[🌱 Good First Issues](https://github.com/SamuelCoreLabs/pulse-crowd/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**

![PulseCrowd CLI पूर्वावलोकन](../../assets/demo-preview.svg)

---

## PulseCrowd क्यों?

1. **प्री-डिस्पैच अनुकूली साइजिंग (`scripts/size_swarm.py`):** प्रोजेक्ट की जटिलता के आधार पर कम से कम **`1,000`** से **`25,000+`** वर्चुअल उपयोगकर्ता स्वचालित रूप से निर्धारित करता है।
2. **स्तरीकृत कोहोर्ट आवंटन:** अनुपालन समीक्षकों और क्षेत्रीय अल्पसंख्यक समूहों के लिए न्यूनतम सांख्यिकीय प्रतिनिधित्व सुनिश्चित करता है।
3. **3-राउंड सिमुलेशन (`scripts/simulate_crowd.py`):** डिस्कवरी -> सोशल कंटेजियन -> सप्ताह-2 संतुलन और B2B रूपांतरण (95% Monte Carlo विश्वास अंतराल के साथ)।
4. **सुरक्षा गेट:** यदि `rejected_distrust > 15%` हो, तो निर्णय को `NO-GO` पर सीमित करता है।

---

## त्वरित इंस्टॉलेशन

```bash
# विकल्प 1: npx skills (Claude Code, Codex, OpenCode, Gemini CLI, Cursor)
npx skills add SamuelCoreLabs/pulse-crowd -g

# विकल्प 2: pip के माध्यम से Python CLI (शून्य बाहरी निर्भरता)
pip install git+https://github.com/SamuelCoreLabs/pulse-crowd.git
pulse-crowd-sim --spec examples/minimal-b2b-cli.json --out-dir /tmp/pulse_crowd_demo --runs 3 --seed 42
```

### दस्तावेज़ और समुदाय
[SKILL.md](../../SKILL.md) · [spec-schema.json](../../references/spec-schema.json) · [methodology.md](../../references/methodology.md) · [CONTRIBUTING.md](../../CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) · [SECURITY.md](../../SECURITY.md) · [MIT](../../LICENSE)
