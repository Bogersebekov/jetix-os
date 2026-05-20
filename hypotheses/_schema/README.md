---
title: hypotheses/_schema — frontmatter + enums reference
type: schema-index
created: 2026-05-20
---

# `hypotheses/_schema/`

Каноническая спецификация frontmatter + enums + cross-refs для всех hypothesis MDs.

## 9 schema files

| File | Назначение |
|---|---|
| [hypothesis.schema.yaml](hypothesis.schema.yaml) | required/optional fields + validation rules + enums roster |
| [status.yaml](status.yaml) | 5 statuses + transitions state machine |
| [categories.yaml](categories.yaml) | 8 categories (outreach / engineering / method / pitch / business / personal-dev / partnership / fpf-extension) |
| [alphas.yaml](alphas.yaml) | 7 OMG Essence 2.0:2024 alphas + state-graphs |
| [ownership.yaml](ownership.yaml) | 4 ownership types (ruslan / brigadier / agent-* / partner-*) |
| [outputs.yaml](outputs.yaml) | 6 output types (decision / artifact / learning / pivot / validation / null_result) |
| [resources.yaml](resources.yaml) | Reference к Platform v2 §3 32-resource framework |
| [fpf-strategic-regions.yaml](fpf-strategic-regions.yaml) | 5 регионов стратегирования Левенчук Методология Гл. 6 |
| [fgr-triple.yaml](fgr-triple.yaml) | FPF B.3 F-G-R triple specification |

## Cross-refs

- **FPF spec source:** `raw/external/ailev-FPF/FPF-Spec.md` (Part B.3 F-G-R)
- **Левенчук Методология 2025:** Гл. 4 (alphas) + Гл. 6 (5 регионов)
- **Foundation Part 5:** Compound learning substrate (learning_extracted output)
- **Foundation Part 7:** Project Lifecycle Substrate (stage-gate analogous mechanic)
- **Pillar C §4.2:** attention budget max 20 (RUSLAN-LAYER)
- **CRM analogous:** `crm/_schema/*.yaml` pattern (frontmatter + roles + statuses)

## Templates

См. `hypotheses/_templates/`:
- `hypothesis.md` — base / default
- `hypothesis-short.md` — 1-7d lifecycle
- `hypothesis-medium.md` — 1-3mo lifecycle
- `hypothesis-long.md` — 3-6mo+ lifecycle
