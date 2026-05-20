---
title: Excel/CSV table layer — usage workflow (Layer 7)
date: 2026-05-20
type: documentation
parent_layer: 7
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-excel-usage
R: low
---

# Layer 7 — Excel/CSV Usage Workflow

> Layer 7 of 7. Excel/CSV table layer = derived view over filesystem MDs.

## §1 When use Excel/CSV vs MD?

| Use case | Tool |
|---|---|
| Add/edit single hypothesis | MD file (via `/hypothesis-add` или direct edit) |
| Status transition | Skill (`/hypothesis-update` или `/hypothesis-close`) |
| Visual scan все active hypotheses | `hypotheses.xlsx` (Sort/Filter) |
| Pivot table by category × F-grade | `hypotheses.xlsx` (Excel built-in) |
| Quick grep / awk filter | `hypotheses.csv` |
| Share snapshot с partner / investor | `hypotheses.xlsx` |
| Alpha state distribution analysis | `alphas-state-graph.xlsx` |

**Critical rule:** MD = source of truth. Excel/CSV = view. Never edit Excel as authoritative — regen overwrites.

## §2 Rebuild workflow

После каждой series of hypothesis changes:
```bash
/hypothesis-build-table
```

Or direct:
```bash
cd ~/jetix-os
python3 hypotheses/tables/_build-table.py
```

Output (example):
```
Collected 5 hypotheses (include_samples=True)
Wrote hypotheses/tables/hypotheses.csv
Wrote hypotheses/tables/hypotheses.xlsx
Wrote hypotheses/tables/alphas-state-graph.xlsx
Done. 5 rows.
```

## §3 CSV git-diff workflow

CSV is git-diff-able (unlike xlsx binary). Commit pattern:
```bash
# After /hypothesis-build-table
git add hypotheses/tables/hypotheses.csv  # commit CSV (diff-readable)
# Skip xlsx (binary; can be re-generated)
git commit -m "[hypotheses] update table after H-NNN closure"
```

Or include xlsx if want versioned snapshots — Ruslan decides per repo policy.

## §4 Excel pivot ideas

`hypotheses.xlsx` supports rich Excel operations:

**Pivot 1: category × status**
- Rows: category
- Columns: status
- Values: count of id
- → see distribution of active/testing/confirmed/refuted/paused per domain

**Pivot 2: fpf_F × fpf_R distribution**
- Rows: fpf_F
- Columns: fpf_R
- Values: count
- → see overall F-grade calibration

**Pivot 3: owner × category**
- → who owns what

**Filter view: active+testing only**
- Filter status in [active, testing] → attention budget view (Pillar C §4.2 cap = 20)

## §5 Alphas-state-graph.xlsx insights

7 sheets (one per OMG Essence alpha):
- **Sheet "stakeholder":** все гипотезы с stakeholder alpha tracked + current state
- **Sheet "opportunity":** similar для opportunity
- ... etc для requirements / software-system / work / team / way-of-working

Insights:
- Stakeholder state distribution → maturity of partnership pipeline
- Work state distribution → cycle health
- Way-of-working state → method maturity (recursive self-tracking)

## §6 CSV scripting examples

Quick filters via awk/grep:

```bash
# All active
awk -F, 'NR==1 || $4=="active"' hypotheses/tables/hypotheses.csv

# All F4+ (potential promotion candidates)
awk -F, 'NR==1 || $11 ~ /F[4-8]/' hypotheses/tables/hypotheses.csv

# All в category=outreach
awk -F, 'NR==1 || $6=="outreach"' hypotheses/tables/hypotheses.csv

# Count by status
awk -F, 'NR>1 {print $4}' hypotheses/tables/hypotheses.csv | sort | uniq -c
```

## §7 Python read examples

```python
import openpyxl
wb = openpyxl.load_workbook("hypotheses/tables/hypotheses.xlsx")
ws = wb["Hypotheses"]

# Get all H-NNN ids
ids = [ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)]

# All testing hypotheses
testing = []
for r in range(2, ws.max_row + 1):
    if ws.cell(row=r, column=4).value == "testing":
        testing.append((ws.cell(row=r, column=1).value, ws.cell(row=r, column=2).value))
```

Or pandas:
```python
import pandas as pd
df = pd.read_csv("hypotheses/tables/hypotheses.csv")
df_active = df[df["status"] == "active"]
df_active.groupby("category").size()
```

## §8 Anti-patterns

- ❌ **Edit xlsx as canonical** — get overwritten
- ❌ **Skip rebuild after MD changes** — table stale
- ❌ **Commit xlsx без CSV** — CSV is git-diff readable, xlsx not
- ❌ **Treat alphas-state-graph as authoritative trail** — actual trail в `hypotheses/alphas/state-graphs/<H-NNN>-alpha-trail.md`

## §9 Cross-refs

- Skill: `.claude/skills/hypothesis-build-table.md`
- Build script: `hypotheses/tables/_build-table.py`
- README: `hypotheses/tables/README.md`
- Schema: `hypotheses/_schema/hypothesis.schema.yaml`
- Alpha trails: `hypotheses/alphas/state-graphs/`
