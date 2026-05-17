---
title: Real FPF-applied examples — inventory + ссылки для tinkering session
date: 2026-05-17 evening
type: research-inventory
purpose: |
  Compile ссылки на real-world FPF-applied artifacts которые Ruslan может изучить +
  сделать несколько mermaid диаграмм чтобы понять как FPF работает в практике.
  После tinkering → applies to Jetix projects.
language: russian
---

# 🔍 Real FPF examples — inventory для tinkering

## §1 In our repo (immediate access)

### 1.1 FPF-Spec.md worked examples (canonical Левенчуковские)
Path: `raw/external/ailev-FPF/FPF-Spec.md` (72,800 строк, vendored с upstream 16.05).

**Самый concrete real-world example — ⭐ Battery-Electric Bus Pack (2025 model year):**
- **Location:** строки 28199-28252 (B.1.2:7 §)
- **What:** реальный engineering case study — 16 modules → 4 strings → pack composition через **Γ_sys** (systemic aggregation pattern)
- **FPF primitives demonstrated:**
  - Holonic decomposition (A.1)
  - ComponentOf mereology (A.14)
  - Scope tagging (`scope=design`)
  - Attribute classification (Extensive / Intensive / Boolean)
  - BIC decisions (Promote / Forward / Encapsulate) — interface management
  - Cut-Stable test
  - WLNK (Weakest-Link bounds — SIL 2 fire rating)
  - Conformance Checklist (B.1.2:8) — CHK-GC-1..5
  - Cross-references: ISO 26262-2 Ed 3 / MBSE 2023-2025 / NASA-7120.5E
- **Why ⭐:** этот example **end-to-end runs** одним патерном (Γ_sys) на real domain. Перфектен для первого tinkering.

**Other worked examples в FPF-Spec.md:**

| Section | Topic | Line |
|---|---|---|
| A.2.4:9 | Role examples | ~3191 |
| A.2.6:12 | Worked examples | ~4551 |
| A.16.1:13 | Worked examples + invalid publications | ~21700 |
| B.3:6 | Archetypal grounding (worked examples) | ~30606 |
| B.5.2:15 | Worked examples (abductive loop) | ~32014 |
| C.2.2:5.1 | System illustration | ~33782 |
| C.2.2:5.2 | Episteme illustration | ~33798 |
| C.2.2a:13 | Worked examples | ~34106 |
| C.2.3:16 | Worked examples | ~34410 |
| C.2.LS:13 | Worked examples + composition notes | ~34602 |

### 1.2 Tseren FMT-exocortex-template (real production template)
Path: `raw/external/tseren-github-2026-05-17/FMT-exocortex-template/` (314 файлов, v0.31.0)
- **Что:** реальный template работающего personal exocortex / IWE substrate built on FPF principles
- **Key files:**
  - `ONTOLOGY.md` — FPF-typed entities
  - `.claude/rules/distinctions.md` — IWE-specific distinctions
  - `setup.sh` — installation flow
  - `.mcp.json` — IWE knowledge MCP server (`https://mcp.aisystant.com/mcp`)
- **Why interesting:** это live working template который Цэрэн использует / распространяет. Real adoption pattern.

---

## §2 External (linked from external research)

### 2.1 ⭐ Anatoly Levenchuk's canonical FPF repo
- **URL:** [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Что:** primary source FPF (нашу copy = его).
- **Tag:** «Pattern language and core specification for admissible action in problematic engineering, research, and mixed human/AI work»
- **Status:** «eternal alpha» — used в working projects + development programmes

### 2.2 jtprogru Gist — FPF Core Conceptual Specification (condensed)
- **URL:** [gist.github.com/jtprogru/dbf54077d191d575ace39b6245702be8](https://gist.github.com/jtprogru/dbf54077d191d575ace39b6245702be8)
- **Что:** September 2025 condensed FPF spec by Левенчук + LLMs assortment
- **Useful for:** quick overview если 72K строк = too much

### 2.3 CodeAlive-AI FPF Problem-Solving Skill (real AI adoption)
- **URL:** [github.com/CodeAlive-AI/fpf-problem-solving-skill](https://github.com/CodeAlive-AI/fpf-problem-solving-skill)
- **Что:** Claude Code agent skill implementing FPF для structured problem-solving
- **Status:** Archived (R/O since May 4, 2026); consolidated в `ai-driven-development/skills/fpf-problem-solving`
- **Структура:** `FPF/` submodule + `sections/` + `scripts/` + `SKILL.md` + `README.md`
- **License:** MIT

### 2.4 Awesome Skills listing
- **URL:** [awesomeskills.dev/en/skill/codealive-ai-fpf-problem-solving-skill](https://www.awesomeskills.dev/en/skill/codealive-ai-fpf-problem-solving-skill)
- Public skill catalog где FPF skill listed — может видны другие FPF adopters

### 2.5 Levenchuk's blog (case studies + applied FPF posts)
- **URL:** [ailev.livejournal.com](https://ailev.livejournal.com/)
- **What we have:** `raw/external/levenchuk-corpus-2026-05-17/02-livejournal/key-posts-captured-2026-05-17.md` (9 posts captured Tier 1)
- **What to search для cases:** ШСМ projects / engineering cases / methodology applications

---

## §3 Recommended изучения order (для tinkering session)

1. **30 минут:** Read [`raw/external/ailev-FPF/FPF-Spec.md`](raw/external/ailev-FPF/FPF-Spec.md) §B.1.2 entire (Γ_sys pattern + Bus Pack example) — строки ~27800-28253
2. **15 минут:** Look at [`raw/external/tseren-github-2026-05-17/FMT-exocortex-template/`](raw/external/tseren-github-2026-05-17/FMT-exocortex-template/) ONTOLOGY.md — Цэрэновская реализация FPF entities
3. **15 минут:** Scan [github.com/CodeAlive-AI/fpf-problem-solving-skill](https://github.com/CodeAlive-AI/fpf-problem-solving-skill) SKILL.md — как AI skill implements FPF reasoning
4. **30 минут:** Сделать mermaid диаграмму Bus Pack example по нашему style guide

---

## §4 Mermaid diagram candidates (что имеет смысл сделать)

### D-1: Battery-Electric Bus Pack — holonic structure
- Pack → 4 strings → 16 modules
- ComponentOf edges
- Scope=design tag visible
- BIC decisions (color-coded: Promote/Forward/Encapsulate)

### D-2: Γ_sys aggregation workflow
- 6 шагов flow: Graph → Attribute classify → BIC decide → Fold (Σ/min/∧) → Cut-Stable test → Outcome
- WLNK bound surfaced at fold step

### D-3: BIC decision tree (Promote / Forward / Encapsulate)
- Decision criteria per port type
- Real Bus Pack ports as examples

### D-4: Conformance Checklist as gate diagram
- 5 checks (CHK-GC-1..5)
- Pass/Fail with refactor or MHT escalation

### D-5: Tseren FMT entities mapping
- ONTOLOGY.md entities → FPF primitives mapping
- Pack / OWC / FMT relationships

---

## §5 После tinkering — applies to Jetix

Когда Ruslan понял Γ_sys pattern на Bus Pack — можно применить **к Jetix object level**:

**Jetix example: Foundation v1.0 как Γ_sys candidate**
- Foundation = pack
- 11 Parts = modules
- ComponentOf? PortionOf? — выбор mereology
- Scope = design (F8 LOCKED artefact) vs scope = operational (Phase B enforcement STUB)
- Attribute classification: Extensive (lines of spec) / Intensive (formality F8) / Boolean (LOCKED yes/no)
- BIC decisions for Foundation external ports (CLAUDE.md, principles/, shared/schemas/)
- Cut-Stable test: меняется ли поведение если split Foundation на 2 packs?

После этого упражнения = honest understanding **что Foundation реально является в FPF terms** (D-2 dispute resolved).

---

## §6 Status

- [x] Inventory собран (этот файл)
- [ ] Ruslan читает FPF-Spec.md B.1.2 Bus Pack
- [ ] Mermaid D-1 готов (Bus Pack holonic structure)
- [ ] Mermaid D-2 готов (Γ_sys workflow)
- [ ] Apply pattern к Jetix Foundation
- [ ] Update Phase 0 D-2 dispute resolution на базе applied understanding

[src: FPF-Spec.md §B.1.2:7 + WebSearch 2026-05-17 + Tseren FMT-exocortex repo]
