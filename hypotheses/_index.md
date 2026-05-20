---
title: Hypotheses Index — auto-generated dashboard
type: index
generated_by: /hypothesis-dash (Phase 8 manual regen)
created: 2026-05-20
updated: 2026-05-20
---

# Hypotheses Index

> Auto-generated dashboard snapshot — Phase 8 close.
> Regenerate via `/hypothesis-dash` (Phase 2 skill).

## Counts by status

| Status | Count |
|---|---|
| active | 0 |
| testing | 0 |
| confirmed | 0 |
| refuted | 0 |
| paused | 0 |
| **samples (starter)** | 5 |

## Counts by category (samples)

| Category | Count |
|---|---|
| method | 3 (H-001, H-004, H-005) |
| outreach | 1 (H-002) |
| business | 1 (H-003) |

## Counts by F-grade (samples)

| F-grade | Count |
|---|---|
| F2 | 3 (H-002, H-003, H-004) |
| F3 | 2 (H-001, H-005) |

## Counts by lifecycle (samples)

| Lifecycle | Count |
|---|---|
| short | 0 |
| medium | 2 (H-002, H-004) |
| long | 3 (H-001, H-003, H-005) |

## Counts by strategic region (samples)

| Region | Count |
|---|---|
| catallactic | 4 (H-001, H-002, H-003, H-005) |
| unknown | 1 (H-004) |

## Attention budget

- Active + Testing: 0 / 20 (Pillar C §4.2 RUSLAN-LAYER cap) ✅ ready
- Samples в `samples/` do NOT count against budget (substrate exemplars)

## Sample roster (H-001..H-005)

| ID | Title | Category | Lifecycle | F | R |
|---|---|---|---|---|---|
| **H-001** | Meta-method applicable cross-domain | method | long | F3 | medium |
| **H-002** | Partnership-frame > cheatcode (L2 outreach) | outreach | medium | F2 | low |
| **H-003** | 3-tier funnel 3-6mo optimal | business | long | F2 | low |
| **H-004** | Imagination as 13th intellect component | method | medium | F2 | low |
| **H-005** | Method as 1st-class object → recursive engine | method | long | F3 | medium |

## Top active (samples — starter cohort)

Все 5 samples в `samples/` для exemplar purposes (NOT в `active/` operational pipeline).

**Migration path:** When Ruslan ready to test any sample, move к `active/` via `git mv`
(use real ID если desired или promote sample id).

## Substrate (canonical files)

- Architecture overview: [docs/architecture-overview.md](docs/architecture-overview.md)
- Workflow guide: [docs/workflow-guide.md](docs/workflow-guide.md)
- FPF F-G-R: [docs/fpf-integration.md](docs/fpf-integration.md) (Layer 5)
- Alpha-machinery: [docs/alpha-machinery-guide.md](docs/alpha-machinery-guide.md) (Layer 6)
- Excel/CSV usage: [docs/excel-table-usage.md](docs/excel-table-usage.md) (Layer 7)
- CRM-style overlay: [docs/crm-style-overlay.md](docs/crm-style-overlay.md) (Layer 3)
- Daily log inline: [docs/inline-daily-log-integration.md](docs/inline-daily-log-integration.md) (Layer 4)
- Diagrams: [docs/diagrams/](docs/diagrams/) (2 mermaid)
- Audit log: [_log.md](_log.md)
- Schema (9 files): [_schema/](_schema/)
- Templates (4 + README): [_templates/](_templates/)
- Tables: [tables/](tables/) (`hypotheses.xlsx`, `hypotheses.csv`, `alphas-state-graph.xlsx`)
- Samples: [samples/](samples/) (5 exemplars)
- Alphas (Layer 6): [alphas/](alphas/) (overview + 7 alphas + 7 state-graphs)
- Skills (Layer 2): `.claude/skills/hypothesis-*.md` (9 skills + README + build-views)
- Build script: `tools/build-hypothesis-views.py` (Layer 3 derived views)
- Build tables: `hypotheses/tables/_build-table.py` (Layer 7 derived)

## Build log

- Phase 0-8 records: [_BUILD-LOG/](_BUILD-LOG/)
- Final summary: [_BUILD-LOG/00-SUMMARY-FOR-RUSLAN.md](_BUILD-LOG/00-SUMMARY-FOR-RUSLAN.md)
