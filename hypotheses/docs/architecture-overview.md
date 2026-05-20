---
title: Hypotheses Substrate — Architecture Overview
date: 2026-05-20
type: architecture-doc
parent_layer: all
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-architecture
R: low
---

# Hypotheses Substrate — Architecture Overview

> 7-layer architecture для tracking 100-1000+ hypotheses в Jetix.
> Filesystem-authoritative; Excel/CSV = derived; CRM-analogous tooling pattern;
> FPF F-G-R native; OMG Essence alpha-machinery integrated; Левенчук-direct primary source.

## §1 Why hypotheses substrate

Jetix accumulates ideas / claims / observations daily — voice notes, research, conversations, reflections. Без structured tracking:
- Compound learning lost
- Promotion candidates buried
- Attention budget invisible
- Connection между гипотезами missed

Hypothesis substrate provides:
- ✅ Each claim gets explicit `success_criteria` + `refutation_criteria` (testable)
- ✅ F-G-R triple per claim (FPF trust calculus)
- ✅ Alpha state tracking (OMG Essence progress dimensions)
- ✅ Bidirectional cross-link к other artefacts (CRM-style)
- ✅ Excel/CSV view + dashboard skill
- ✅ Append-only audit (provenance)

## §2 7 Layers

| # | Layer | Purpose |
|---|---|---|
| 1 | **`hypotheses/` first-class dir** | Filesystem namespace + schema + templates + status dirs |
| 2 | **9 canonical skills** | `/hypothesis-*` skill family (add/update/close/dash/search/stuck/link/build-table/alpha-state) |
| 3 | **CRM-style overlay** | Bidirectional `linked_hypotheses` ↔ `linked_artefacts` frontmatter |
| 4 | **Inline daily log** | `_PLAN-OF-DAY` §3 «Active Hypotheses» section |
| 5 | **FPF F-G-R triple** | Mandatory frontmatter `fpf_F` / `fpf_G` / `fpf_R` |
| 6 | **OMG Essence alpha-machinery** | 7 alphas + state-graphs + 5 регионов стратегирования |
| 7 | **Excel/CSV table layer** | `hypotheses.xlsx` + `.csv` + `alphas-state-graph.xlsx` |

См. diagram: `diagrams/01-7-layer-architecture.md`.

## §3 File map (top-level)

```
hypotheses/
├── _index.md                          (auto-generated dashboard; Phase 8 regen)
├── _log.md                            (append-only audit trail)
├── _schema/                           (Layer 1)
│   ├── hypothesis.schema.yaml
│   ├── status.yaml, categories.yaml, alphas.yaml,
│   │   ownership.yaml, outputs.yaml, resources.yaml,
│   │   fpf-strategic-regions.yaml, fgr-triple.yaml
│   └── README.md
├── _templates/                        (Layer 1)
│   ├── hypothesis.md, hypothesis-{short,medium,long}.md
│   └── README.md
├── active/, testing/, confirmed/, refuted/, paused/   (status dirs)
├── samples/                           (Phase 8: H-001..H-005)
├── alphas/                            (Layer 6)
│   ├── _alphas-overview.md
│   ├── {stakeholder,opportunity,requirements,software-system,work,team,way-of-working}.md
│   └── state-graphs/                  (7 mermaid state-graphs)
├── tables/                            (Layer 7)
│   ├── _build-table.py, README.md
│   ├── hypotheses.xlsx, hypotheses.csv
│   └── alphas-state-graph.xlsx
├── docs/                              (this section)
│   ├── architecture-overview.md       (← this file)
│   ├── workflow-guide.md
│   ├── fpf-integration.md             (Layer 5)
│   ├── alpha-machinery-guide.md       (Layer 6)
│   ├── excel-table-usage.md           (Layer 7)
│   ├── crm-style-overlay.md           (Layer 3)
│   ├── inline-daily-log-integration.md (Layer 4)
│   └── diagrams/
│       ├── 01-7-layer-architecture.md
│       └── 02-hypothesis-lifecycle.md
└── _BUILD-LOG/                        (per-phase build log)
```

Plus skills (Layer 2): `.claude/skills/hypothesis-*.md` × 10 (9 + README).
Plus aggregation tool: `tools/build-hypothesis-views.py` (Layer 3).
Plus daily log template extension: `daily-logs/_PLAN-OF-DAY-template.md` (Layer 4).
Plus output views: `crm/hypothesis-views/` (Layer 3 derived).

## §4 Workflow

См. `hypotheses/docs/workflow-guide.md` для практический detail.

Core cycle:
```
/hypothesis-add → active
  ↓
(test method initiated)
  ↓
/hypothesis-update --status testing → testing/
  ↓
(test runs; alphas updated via /hypothesis-alpha-state)
  ↓
/hypothesis-close --outcome confirmed/refuted/paused → confirmed/ | refuted/ | paused/
  ↓
(weekly /hypothesis-dash; monthly /hypothesis-build-table; quarterly review)
```

## §5 Constitutional posture

| Rule | Application |
|---|---|
| **R1** | brigadier scaffolds structure; Ruslan authors hypothesis prose (Гипотеза + Метод теста sections) |
| **R2** | Foundation read-only; new namespace `hypotheses/` |
| **R6** | Provenance per hypothesis (created/updated/cross-cite/linked_artefacts) |
| **R11** | Default-Deny novel actions; CRM-analogous skill patterns only |
| **R12** | Anti-extraction substrate (no member extraction beyond agreed share) |
| **EP-5** | Mandatory F-G-R frontmatter (Layer 5) |
| **Append-only** | `_log.md` audit trail; file moves preserve history |
| **Filesystem-authoritative** | MD primary; Excel/CSV = derived view |

## §6 Cross-substrate integration

| Foundation | Integration |
|---|---|
| **Part 5 — Compound Learning** | `learning_extracted` at hypothesis closure feeds substrate |
| **Part 7 — Project Lifecycle Substrate** | Stage-gates analogous mechanic; closure → potential project bootstrap |
| **Part 11 — Strategic Direction Substrate** | High-F confirmed hypotheses → strategic insight candidates |
| **Pillar C §4.2** | Attention budget cap 20 enforced via `/hypothesis-dash` |

## §7 Substrate ready для

- 100-1000+ hypothesis tracking (status dirs scale)
- Daily workflow integration (Layer 4)
- Weekly reflection (`/hypothesis-dash` + `/hypothesis-stuck`)
- Monthly snapshot (Excel/CSV via `/hypothesis-build-table`)
- Quarterly review (promotion candidate sweep)
- Migration: 22 Tier B pool candidates + 17 DR pool items (manual review для conversion)

## §8 Cross-refs

- **Decision record:** `decisions/REFLECTION-INBOX-2026-05-16.md` §APPEND-2026-05-20-evening-hypothesis-tables-decision
- **Build prompt:** `prompts/scaffolding-hypotheses-architecture-2026-05-20.md`
- **EXPLAIN:** `prompts/explanations/_EXPLAIN-scaffolding-hypotheses-architecture-2026-05-20.md`
- **Decision analysis:** `daily-logs/_HYPOTHESIS-TABLES-DECISION-2026-05-20.md`
- **Workflow guide:** `hypotheses/docs/workflow-guide.md`
- **Skills index:** `.claude/skills/hypothesis-README.md`
- **Build log:** `hypotheses/_BUILD-LOG/` (per-phase records)
