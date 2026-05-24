---
title: Diagrams INDEX — Research SOTA 2026-05-24 (10 diagrams)
phase: 8
parent_research: reports/research-sota-2026-05-24/
total_count: 10
spec_target: 8-12
status: complete
---

# 🎨 Diagrams INDEX — Research SOTA

10 mermaid diagrams created (within 8-12 spec) для visual support master doc `decisions/strategic/RESEARCH-SOTA-2026-05-24.md`.

---

## §1 Inventory

| # | File | Type | Phase | Description |
|---|---|---|---|---|
| 1 | `01-sota-concept-multi-tradition-decomposition.mmd` | mindmap | Phase 0/1 | SOTA concept × 5 traditions (phil-sci / Левенчук-МИМ / ML / engineering / Jetix) |
| 2 | `02-levenchuk-sota-time-decay-curve.mmd` | timeline | Phase 1 | Левенчук's 5+5=10y decay curve operationalised |
| 3 | `03-popper-kuhn-lakatos-feyerabend-laudan-comparison.mmd` | quadrantChart | Phase 2 | 5 phil-sci paradigms × SOTA stance (plurality × methodology-strictness) |
| 4 | `04-sota-tracking-mechanisms-flow.mmd` | flowchart LR | Phase 5 | 9 mechanisms lifecycle flow (preprint → peer review → benchmark → replication → standards) |
| 5 | `05-ml-sota-leaderboard-pattern.mmd` | sequenceDiagram | Phase 4 | Paper-with-code SoTA-claim lifecycle (research → publish → reproduce → leaderboard → saturate → replace) |
| 6 | `06-mim-sota-mastery-spectrum.mmd` | flowchart TB | Phase 6 | МИМ 7-step qualification × SOTA-disposition (Ученик → Революционер + 2y revalidation) |
| 7 | `07-jetix-sota-tracking-inventory.mmd` | mindmap | Phase 7 | Jetix 10-mechanism existing inventory (Foundation + Method V2 + sota-tracker + R12 + wiki pipeline + etc) |
| 8 | `08-jetix-sota-gaps-and-extensions.mmd` | flowchart LR | Phase 7 | 7 gaps → 7 extension proposals → Ruslan decision matrix |
| 9 | `09-sota-claim-honesty-discipline.mmd` | flowchart TD | Phase 7 §6 | 8-question honest-claim flow for partner-facing materials |
| 10 | `10-sota-vs-foundational-trade-off.mmd` | xychart + flowchart | Phase 1 §12 | Левенчук's anti-SOTA-chase strategy: tool decay vs trans-discipline decay × strategy |

---

## §2 Diagram-to-phase mapping

| Phase | Diagram(s) used |
|---|---|
| 0 (Pre-flight) | D-01 (concept decomp) |
| 1 (Левенчук SOTA) | D-02 (time-decay), D-10 (foundational tradeoff), D-06 (mastery) |
| 2 (Phil-sci) | D-03 (5-paradigm comparison) |
| 3 (Modern epistemology) | (no dedicated; cross-ref D-04) |
| 4 (ML SOTA) | D-05 (PWC lifecycle) |
| 5 (Tracking mechanisms) | D-04 (9-mechanism flow) |
| 6 (МИМ operational) | D-06 (mastery spectrum) |
| 7 (Jetix Lens) | D-07 (inventory), D-08 (gaps→extensions), D-09 (claim discipline) |
| 8 (this phase) | (all 10 consolidated) |

---

## §3 Diagram → strategic decision mapping (for Ruslan)

| If Ruslan considering | Diagram(s) to review |
|---|---|
| What SoTA means broadly | D-01, D-03 |
| Time-decay / year-stamping | D-02, D-06 |
| 5 phil-sci traditions positioning | D-03 |
| ML SoTA-tracking adoption | D-04, D-05 |
| МИМ-pattern adoption | D-06 |
| Jetix existing inventory | D-07 |
| 7 extension decisions | D-08 |
| Partner-facing SoTA discipline | D-09 |
| Foundational vs applied investment | D-10 |

---

## §4 Acceptance gate

- [x] 10 diagrams created (within 8-12 spec)
- [x] All diagrams use mermaid syntax
- [x] All diagrams have frontmatter (title, phase, research)
- [x] All diagrams have source where applicable
- [x] 6 different chart types used (mindmap, timeline, quadrantChart, flowchart LR/TB/TD, sequenceDiagram, xychart-beta)
- [x] Coverage spans all 8 phases (no gap)

---

*INDEX closure 2026-05-24. Diagrams ready for embedding в master doc + Wave 1 outreach materials.*
