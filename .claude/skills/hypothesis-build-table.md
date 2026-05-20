---
name: hypothesis-build-table
description: Rebuild hypotheses/tables/hypotheses.xlsx + .csv from all hypothesis MDs (Layer 7 Excel/CSV).
type: skill
---

# /hypothesis-build-table

Rebuild Excel/CSV table layer (Layer 7).

## Arguments

| Flag | Required | Default | Описание |
|---|---|---|---|
| `--csv-only` | no | false | Skip xlsx (if openpyxl unavailable) |
| `--include-samples` | no | true | Include samples/ in build |
| `--alphas-table` | no | true | Also rebuild alphas-state-graph.xlsx |

## Workflow

```bash
cd ~/jetix-os
python3 hypotheses/tables/_build-table.py [--csv-only] [--no-include-samples]
```

Script:
1. Walks `hypotheses/{active,testing,confirmed,refuted,paused,samples}/`
2. Parses frontmatter (yaml) per file
3. Aggregates rows; superset of all fields → columns
4. Writes:
   - `hypotheses/tables/hypotheses.csv`
   - `hypotheses/tables/hypotheses.xlsx` (если openpyxl available)
   - `hypotheses/tables/alphas-state-graph.xlsx` (если `--alphas-table`)
5. Output: file paths + row count

## Excel structure

`hypotheses.xlsx`:
- Sheet "Hypotheses" — все гипотезы; columns = frontmatter fields
- Header bold, gray fill
- Auto-width columns

`alphas-state-graph.xlsx`:
- Sheet per alpha (7 sheets)
- Per row: H-NNN / current state / state history (from `alphas/state-graphs/<H-NNN>-alpha-trail.md`)

## Examples

```bash
/hypothesis-build-table
# Output: hypotheses/tables/hypotheses.{csv,xlsx} (N rows)

/hypothesis-build-table --csv-only
# Output: hypotheses/tables/hypotheses.csv (skipped xlsx)
```

## Constitutional posture

- Excel = derived view (filesystem-authoritative MDs = source of truth)
- Idempotent — safe to re-run any time
- No data loss: regenerates from MD source

## Cross-refs

- `hypotheses/tables/_build-table.py` (executor)
- `hypotheses/tables/README.md` (usage docs)
- `hypotheses/docs/excel-table-usage.md` (Layer 7 documentation)
