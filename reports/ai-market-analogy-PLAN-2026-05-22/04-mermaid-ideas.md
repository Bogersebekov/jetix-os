---
title: Phase 4 — Stage 2 mermaid diagrams ideas (~37 list)
date: 2026-05-22
type: phase-report
parent_prompt: prompts/ai-market-electricity-analogy-PLAN-2026-05-22.md
phase: 4
F: F2
G: ai-market-electricity-analogy-PLAN
prose_authored_by: brigadier-scribe (Cloud Cowork)
target_count: 30-40 (current proposal 37)
---

# Phase 4 — Stage 2 mermaid diagrams ideas (~37)

> Reference: Economic Model + Tokenomics deliverable Phase 13 mermaid pass — proven pattern. Stage 2 диаграмы target 30-40 range, current proposal **37**.

---

## Group A — AI market visualizations (8 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| A1 | AI firm financials comparison (Revenue × Margin) | `quadrantChart` | Phase 2 |
| A2 | AI investment flow Sankey (VC → firms → spending) | `sankey-beta` | Phase 3 |
| A3 | AI business models taxonomy | `mindmap` | Phase 4 |
| A4 | AI unit econ comparison (Cost-per-inference trends 2023-2026) | `xychart-beta` | Phase 5 |
| A5 | AI market consolidation timeline (M&A 2020-2026) | `timeline` | Phase 6 |
| A6 | AI firm ecosystem map (connections + dependencies) | `graph TD` | Phases 2-6 synthesis |
| A7 | AI talent flow (hiring/poaching patterns) | `sankey-beta` | Phase 6 |
| A8 | AI margin pressure (Gross margin trends per tier) | `xychart-beta` | Phase 5 |

---

## Group B — Electricity history visualizations (6 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| B1 | Electricity adoption waves 1880-1930 | `timeline` | Phase 7 |
| B2 | Electric grid evolution (branches of infrastructure) | `gitGraph` | Phase 7 |
| B3 | Edison vs Tesla AC/DC battle | `stateDiagram-v2` | Phase 7 |
| B4 | Insull standardization impact (before/after) | `graph LR` | Phase 7 |
| B5 | Electrical workforce growth 1880-1950 (electricians count × time) | `xychart-beta` | Phase 9 |
| B6 | Grid governance evolution (private → cooperative → public) | `graph TD` | Phase 10 |

---

## Group C — Analogy mapping (6 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| C1 | ⭐⭐ AI ↔ Electricity one-to-one map (most important) | `graph LR` or `classDiagram` | Phase 11 |
| C2 | Layer stack comparison (both stacks side-by-side) | `block-beta` | Phase 11 |
| C3 | Workforce analog (electricians ↔ AI-users mindmap) | `mindmap` | Phases 9, 16 |
| C4 | Disanalogies quadrant (where mapping breaks) | `quadrantChart` | Phase 12 |
| C5 | Predictive timeline (electricity precedent → AI prediction) | `gantt` | Phase 11 |
| C6 | Where Jetix sits in stack (layer placement) | `block-beta` | Phase 13 |

---

## Group D — Jetix layering thesis (5 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| D1 | Jetix layering stack (compute → models → methods → users) | `block-beta` | Phase 13 |
| D2 | Value-add per layer | `graph TD` | Phase 13 |
| D3 | Methods-as-appliances analog (class diagram) | `classDiagram` | Phase 13 |
| D4 | Talent training pipeline (8-tier progression) | `journey` | Phase 13 |
| D5 | Layer leverage thesis (Compute cost trends + Jetix value capture) | `xychart-beta` | Phase 13 |

---

## Group E — Token cooperation (8 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| E1 | Token cooperation variants overview | `mindmap` | Phase 14 |
| E2 | Acquisition mechanism flow (sequence) | `sequenceDiagram` | Phase 15 |
| E3 | Crisis rescue scenarios (decision tree) | `flowchart` | Phase 15 |
| E4 | Token economic flow (issuance → utility → governance) | `graph LR` | Phase 14 |
| E5 | Closed-loop dynamics (recursive 25% Sankey) | `sankey-beta` | Phase 14 |
| E6 | Governance impact mapping (triple-role × decision rights) | `graph TD` | Phase 14 |
| E7 | R12 conformance per variant (anti-extraction quadrant) | `quadrantChart` | Phase 14 |
| E8 | Risk × Reward matrix per variant | `quadrantChart` | Phase 16 |

---

## Group F — Master synthesis (4 diagrams)

| # | Diagram | mermaid type | Source phase |
|---|---|---|---|
| F1 | Full analogy + Jetix layering + token cooperation (master) | `graph TD` | All |
| F2 | Predictive 5-year trajectory (electricity precedent applied к AI) | `gantt` | Phase 11 + 13 |
| F3 | Economic effect summary (favourable effects per stakeholder) | `xychart-beta` | Phase 17 |
| F4 | Recommendation decision tree | `graph TD` | Phase 17 |

---

## Total count check

- Group A: 8
- Group B: 6
- Group C: 6
- Group D: 5
- Group E: 8
- Group F: 4
- **Total: 37 diagrams** ✅ (target range 30-40)

---

## Distribution by mermaid type

| Type | Count | Diagrams |
|---|---|---|
| `graph TD` | 5 | A6, B6, D2, E6, F1, F4 |
| `graph LR` | 3 | B4, C1, E4 |
| `block-beta` | 3 | C2, C6, D1 |
| `quadrantChart` | 4 | A1, C4, E7, E8 |
| `xychart-beta` | 5 | A4, A8, B5, D5, F3 |
| `sankey-beta` | 3 | A2, A7, E5 |
| `timeline` | 2 | A5, B1 |
| `gantt` | 2 | C5, F2 |
| `gitGraph` | 1 | B2 |
| `stateDiagram-v2` | 1 | B3 |
| `classDiagram` | 2 | C1 (alt), D3 |
| `mindmap` | 3 | A3, C3, E1 |
| `sequenceDiagram` | 1 | E2 |
| `flowchart` | 1 | E3 |
| `journey` | 1 | D4 |

Balanced spread across mermaid v10/v11 supported types.

---

## Reference patterns (from Economic Model + Tokenomics Phase 13)

Proven mermaid patterns to reuse:
- `quadrantChart` для capability × constraint mapping (works well для R12 conformance per variant)
- `sankey-beta` для flow visualization (proven работает для recursive 25% Economic Model)
- `block-beta` для layered architecture (worked для V10 Hybrid composition)
- `mindmap` для taxonomy (worked для business model taxonomy)
- `gantt` для temporal sequencing (worked для phased rollout)

---

## ⭐⭐ Critical diagram callout

**C1 — AI ↔ Electricity one-to-one map** = single most important diagram. Stage 2 should ideally **double C1**: provide both `graph LR` version и `classDiagram` version (С1a + С1b) — different visual affordances для same content. Counts as 1 logical diagram, 2 renderings.

---

## Cross-refs

- Economic Model Phase 13 mermaid pass: `reports/economic-model-tokenomics-2026-05-21/phase-13-mermaid-pass.md`
- Topic groups source: this PLAN's `02-scope-proposal.md`
- Structure source: this PLAN's `03-structure-proposal.md`

---

*Phase 4 closure 2026-05-22. 37 diagrams ideas across 6 groups; balanced mermaid type distribution.*
