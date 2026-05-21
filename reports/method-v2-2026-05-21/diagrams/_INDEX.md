---
title: Method V2 — Diagrams INDEX
date: 2026-05-21
type: method-v2-diagrams-index
phase: 15
prose_authored_by: brigadier-scribe
F: F3 assembly
G: method-v2-diagrams
total_diagrams: 40
---

# Method V2 — Diagrams INDEX (40 mermaid diagrams)

> **Что это.** Каталог всех 40 mermaid diagrams в Method V2 deliverable.
> Diagrams co-located inline в phase files (для reading flow); этот INDEX
> предоставляет mapping для cross-reference и reuse.

---

## §A Summary

| Stat | Value |
|---|---|
| **Total diagrams** | **40** |
| **Floor target** | 25 |
| **Stretch target** | 35 |
| **Actual delivered** | **40** (above stretch) |
| **Phases с diagrams** | 14 of 17 (phases 0/15/16 = scope/index/assembly, no diagrams expected) |

---

## §B Diagram inventory per phase

### Phase 0 — FPF lens + scope (no diagrams)

Scope-setting only. Tables present; no flowcharts needed.

### Phase 1 — Fundamental ontology (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D1** | `mindmap` | Fundamental ontology — Информация: воспринимаем / как обрабатываем / знание о методах | `01-fundamental-ontology.md` §D |
| **D2** | `graph LR` | Information flow в живой системе — sense → method select → process → action loop | `01-fundamental-ontology.md` §E |

### Phase 2 — Self-managing systems (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D3** | `classDiagram` | VSM 5 systems mapping для Jetix (System 1 ops до System 5 policy Ruslan) | `02-self-managing-systems.md` §G |
| **D4** | `stateDiagram-v2` | Цикл обратной связи sense→compare→decide→act→learn | `02-self-managing-systems.md` §H |

### Phase 3 — Self-development orientation (1 diagram)

| ID | Type | Subject | File |
|---|---|---|---|
| **D5** | `graph TD` | Motivation stack: base energy → growth mindset → SDT → flow → deliberate practice → mastery | `03-self-development-orientation.md` §G |

### Phase 4 — Info consumption + experience (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D6** | `mindmap` | Каналы потребления информации (8 categories) | `04-info-consumption-experience.md` §J |
| **D7** | `xychart-beta` | Накопление опыта — deliberate practice vs пассивное чтение (S-curves) | `04-info-consumption-experience.md` §K |

### Phase 5 — Method anatomy + ⭐⭐ §J meta-method (7 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D8** | `graph TD` | 7-step method anatomy (Plan → Execute → Reflection) | `05-method-anatomy-timing.md` §G |
| **D9** | `stateDiagram-v2` | OODA loop (Observe → Orient → Decide → Act) | `05-method-anatomy-timing.md` §H |
| **D10** | `graph TD` | Decision tree by domain (Cynefin × time scale) | `05-method-anatomy-timing.md` §I |
| **D11-meta** | `graph TD` | Quadrate logic — 4 уровня (raw / method / choice / **meta-method**) | `05-method-anatomy-timing.md` §J.11 |
| **D12-meta** | `sequenceDiagram` | 6 шагов мета-метода — Step 1-6 с compound learning | `05-method-anatomy-timing.md` §J.11 |
| **D13-meta** | `xychart-beta` | Градиент достаточности — quality of decision × info gathered | `05-method-anatomy-timing.md` §J.11 |
| **D14-meta** | `quadrantChart` | Default vs Meta-method × Routine vs High-stakes — где применять | `05-method-anatomy-timing.md` §J.11 |

### Phase 6 — Info asymmetry + ⭐⭐ §H meta-control (7 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D11** (Phase 6) | `graph LR` | Information asymmetry — Знание Тебя ⊂ Знание Меня + 4 uses | `06-info-asymmetry-reverse-eng.md` §E |
| **D12** (Phase 6) | `sequenceDiagram` | Reverse engineering process — observe→infer→predict→test→refine | `06-info-asymmetry-reverse-eng.md` §F |
| **D13-meta** (Phase 6 §H) | `graph TD` | 4-level control cascade (L0 ops → L1 peer → L2 strategic → L3 constitutional) | `06-info-asymmetry-reverse-eng.md` §H.13 |
| **D14-meta** (Phase 6 §H) | `classDiagram` | Intelligence layer variations (AI/partner/self-question/written/group/book/spaced) | `06-info-asymmetry-reverse-eng.md` §H.13 |
| **D15-meta** | `sequenceDiagram` | Meta-control flow — Ruslan (L2) → brigadier → server CC → output | `06-info-asymmetry-reverse-eng.md` §H.13 |
| **D16-meta** | `xychart-beta` | Pre-AI vs Exocortex era — leverage acquisition speed (10-20× shift) | `06-info-asymmetry-reverse-eng.md` §H.13 |
| **D17-meta** | `quadrantChart` | Leverage × R12 conformance — where Jetix lives (top-right) | `06-info-asymmetry-reverse-eng.md` §H.13 |

### Phase 7 — Positive direction + R12 (1 diagram)

| ID | Type | Subject | File |
|---|---|---|---|
| **D-quadrant** (Phase 7) | `quadrantChart` | Power × Intent — Big Tech / cooperatives / Jetix positioning | `07-positive-direction-r12.md` §F |

### Phase 8 — Scale plan (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D14** (Phase 8) | `graph TD` | 4-stage cascade (Solo → 10 partners → 100/1000 → 10K+) с Foundation constraints | `08-scale-plan.md` §G |
| **D15** (Phase 8) | `block-beta` | Resource distribution per stage (self-funded → $100K → $1M → $1B+) | `08-scale-plan.md` §H |

### Phase 9 — FPF universal language (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D16** (Phase 9) | `classDiagram` | FPF F-G-R triple structure + Formality / Group / Reliability subclasses | `09-fpf-universal-language.md` §H |
| **D17** (Phase 9) | `graph TD` | F2-F8 grade ladder с change cost увеличением | `09-fpf-universal-language.md` §I |

### Phase 10 — Exocortex + IA (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D18** | `block-beta` | Exocortex components stack — Bio brain / Personal / Substrate / AI / World | `10-exocortex-ia.md` §G |
| **D19** | `timeline` | IA history timeline — 4000 BCE writing → 2026 Jetix V2 | `10-exocortex-ia.md` §H |

### Phase 11 — Integration synthesis (3 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D20** | `mindmap` | Integration synthesis center — Foundation / Daily / Power / Ethics / Scaling / Communication / Tools | `11-integration-synthesis.md` §I |
| **D21** | `timeline` | Cadence — Daily / Weekly / Monthly / Quarterly / Annual rhythms | `11-integration-synthesis.md` §J |
| **D22** | `quadrantChart` | Position vs alternatives — depth × scope mapping (Левенчук, Karpathy, Naval, etc.) | `11-integration-synthesis.md` §K |

### Phase 12 ⭐ — Personal origin (4 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D-P12-1** | `journey` | Personal genesis journey — pre-foundation → system building → scale plan ready | `12-personal-origin-bootstrap.md` §J |
| **D-P12-2** | `graph LR` | Positive virus economic loop — 8 steps с R12 constraint + fork-and-leave | `12-personal-origin-bootstrap.md` §J |
| **D-P12-3** | `xychart-beta` | Wisdom accumulation curve — с exocortex (compound) vs без (linear) | `12-personal-origin-bootstrap.md` §J |
| **D-P12-4** | `quadrantChart` | Origin → scale — solo/collective × LLM-assisted/unassisted | `12-personal-origin-bootstrap.md` §J |

### Phase 13 — Wikipedia synthesis (2 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D23** | `mindmap` | Traditions cross-cite map — Jetix center, 12 tradition branches (~40 thinkers) | `12-wikipedia-deep-scan.md` §P |
| **D24** | `graph LR` | Common patterns across 12 traditions — converging themes | `12-wikipedia-deep-scan.md` §Q |

### Phase 14 — Examples (3 diagrams)

| ID | Type | Subject | File |
|---|---|---|---|
| **D25** | `journey` | Утро Руслана — 4 sections (wake / method selection / deep work / evening) | `13-examples-use-cases.md` §F |
| **D26** | `sequenceDiagram` | Hypothesis cycle — voice memo → /hypothesis-add → execute → measure → closure → wiki update | `13-examples-use-cases.md` §G |
| **D27** | `graph TD` | Society cascade Year 1 → Year 5+ с Foundation/R12/FPF constraints + risks | `13-examples-use-cases.md` §H |

---

## §C Diagram type variety

| Type | Count | Phases |
|---|---|---|
| `mindmap` | 4 | 1, 4, 11, 13 |
| `graph LR` | 3 | 1, 6, 13, 12-P12 |
| `graph TD` | 9 | 3, 5(×2), 6, 8, 11, 12, 14, 9 |
| `sequenceDiagram` | 4 | 5, 6(×2), 14 |
| `stateDiagram-v2` | 2 | 2, 5 |
| `classDiagram` | 3 | 2, 9, 6-H |
| `xychart-beta` | 4 | 4, 5, 6-H, 12-P12 |
| `quadrantChart` | 5 | 5, 6-H, 7, 11, 12-P12 |
| `timeline` | 2 | 10, 11 |
| `journey` | 2 | 12-P12, 14 |
| `block-beta` | 2 | 8, 10 |

**11 unique mermaid types**. Variety per CRITICAL IMPORTANCE MANDATE §17.0.

---

## §D Diagram by purpose

| Purpose | Diagrams |
|---|---|
| **Conceptual structure** (mindmap / classDiagram) | D1, D3, D6, D14-meta(P6), D16(P9), D20, D23 |
| **Process flow** (sequenceDiagram / stateDiagram) | D4, D9, D12-meta, D12(P6), D15-meta, D26 |
| **Hierarchy / cascade** (graph TD) | D5, D8, D10, D11-meta, D13-meta(P6), D14(P8), D17(P9), D27 |
| **Time progression** (timeline / journey) | D19, D21, D-P12-1, D25 |
| **Quantitative comparison** (xychart-beta) | D7, D13-meta, D16-meta, D-P12-3 |
| **2D positioning** (quadrantChart) | D14-meta, D17-meta, D-quadrant, D22, D-P12-4 |
| **Component stacking** (block-beta) | D15(P8), D18(P10) |
| **Relational** (graph LR) | D2, D11(P6), D-P12-2, D24 |

---

## §E Cross-reference matrix

Diagrams referenced from multiple phases (high reuse value):

| Diagram | Primary location | Cross-referenced from |
|---|---|---|
| D3 VSM mapping | Phase 2 §G | Phase 6 §H.7; Phase 11 §C.4 |
| D11-meta Quadrate logic | Phase 5 §J.11 | Phase 11 §C; Phase 12 §H |
| D13-meta (P6) Control cascade | Phase 6 §H.13 | Phase 8 §G; Phase 14 §D |
| D17-meta Leverage × R12 | Phase 6 §H.13 | Phase 7 §F; Phase 8 §D.2 |
| D-quadrant Power × Intent | Phase 7 §F | Phase 11 §K |
| D14 (P8) 4-stage cascade | Phase 8 §G | Phase 12 §I; Phase 14 §H |
| D-P12-2 Positive virus | Phase 12 §J | Phase 8 §B.G.1 |
| D23 Traditions map | Phase 13 §P | Phase 11 §E |

---

## §F Notes для diagram reuse

**Если использовать diagram в downstream documents:**
1. Привести source phase file inline
2. Сохранить F-G-R triple metadata
3. Update если concept evolved (don't fork silently — Phase 9 FPF discipline)
4. Mermaid syntax verified rendering pre-publish

**Style discipline applied:**
- Subgraphs для logical grouping где applicable
- Color coding by category (warm = action; cool = passive; красный = constitutional)
- Notes для diagram explanation 2-3 sentence preceding
- ID system consistent (D1-D27 + D11-meta — D17-meta + D-P12-{1-4} + D-quadrant)

---

## §G What's NOT в diagrams (intentional gaps)

- **Не диаграммы для финансовой модели** (DR-26 unit-econ separate deliverable)
- **Не диаграммы для constitutional text** (Pillar C Tier 2 textual; Phase 7 / 13 references)
- **Не диаграммы для specific partner names** (KA-03 confidential; abstract в diagrams)
- **Не AI-architecture deep diagrams** (V1 territory; this V2 = human-language)

---

*Phase 15 closure 2026-05-21. brigadier-scribe; 40 mermaid diagrams catalogued; 11 unique types; cross-reference matrix complete.*
