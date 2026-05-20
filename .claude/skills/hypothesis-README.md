---
name: hypothesis-README
description: Index page для всех 9 `/hypothesis-*` skills (Layer 2 of 7-layer architecture).
type: skill-index
---

# `/hypothesis-*` Skills

9 canonical skills для hypotheses substrate (Layer 2 of 7-layer architecture).

## Roster

| Skill | Purpose | Layer |
|---|---|---|
| [/hypothesis-add](hypothesis-add.md) | Scaffold new H-NNN | 1 |
| [/hypothesis-update](hypothesis-update.md) | Update frontmatter / status transition / file move | 1+2 |
| [/hypothesis-close](hypothesis-close.md) | Terminal close (confirmed/refuted/paused) | 1+2 |
| [/hypothesis-dash](hypothesis-dash.md) | Aggregate dashboard + attention budget check | 2 |
| [/hypothesis-search](hypothesis-search.md) | Search across all hypothesis MDs | 2 |
| [/hypothesis-stuck](hypothesis-stuck.md) | Find stuck (testing >N days) | 2 |
| [/hypothesis-link](hypothesis-link.md) | Bidirectional link H-NNN ↔ artefact | 2+3 |
| [/hypothesis-build-table](hypothesis-build-table.md) | Rebuild xlsx/csv table layer | 2+7 |
| [/hypothesis-alpha-state](hypothesis-alpha-state.md) | OMG Essence alpha state update | 2+6 |

## CRM-analogous

Pattern modeled after `.claude/skills/crm-*.md`:
- `/crm-add` ↔ `/hypothesis-add`
- `/crm-update` ↔ `/hypothesis-update`
- `/crm-dash` ↔ `/hypothesis-dash`
- `/crm-search` ↔ `/hypothesis-search`
- `/crm-stuck` ↔ `/hypothesis-stuck`

## Schema references

All skills read `hypotheses/_schema/*.yaml`:
- `hypothesis.schema.yaml` (frontmatter contract)
- `status.yaml` (transitions)
- `categories.yaml` (8 categories)
- `alphas.yaml` (7 OMG Essence alphas)
- `ownership.yaml`
- `outputs.yaml`
- `resources.yaml`
- `fpf-strategic-regions.yaml` (5 регионов)
- `fgr-triple.yaml` (FPF B.3)

## Constitutional posture

- R1: skills scaffold structure; strategic prose ≠ generated (Ruslan / hybrid-ack)
- R11: Default-Deny novel actions; only canonical patterns
- R12: anti-extraction posture в substrate
- EP-5 / Layer 5: F-G-R mandatory frontmatter
