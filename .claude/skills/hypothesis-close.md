---
name: hypothesis-close
description: Terminal close hypothesis (confirmed | refuted | paused) — required outcome + learning_extracted + dir move + log.
type: skill
---

# /hypothesis-close

Closes hypothesis to terminal state. Wrapper над `/hypothesis-update` с required outputs.

## Arguments

| Flag | Required | Описание |
|---|---|---|
| `<H-NNN>` | yes | Hypothesis id |
| `--outcome confirmed\|refuted\|paused` | yes | Closure type |
| `--outcome-text "<text>"` | yes | Succinct result statement (1-3 sentences) |
| `--learning "<text>"` | no (paused) / yes (confirmed,refuted) | Compound learning extracted |
| `--reason "<text>"` | no | Why closure now |

## Workflow

1. Locate H-NNN; parse current frontmatter
2. Validate: hypothesis status currently `testing` OR `active` (per status.yaml transition rules)
3. Update frontmatter:
   - `status` → confirmed/refuted/paused
   - `outcome` → outcome-text
   - `learning_extracted` → learning
   - `updated` → today
4. Move file `hypotheses/<old>/` → `hypotheses/<outcome>/`
5. Append к `_log.md` с closure details
6. If `--outcome confirmed` and `fpf_R == high` — print «Promotion candidate» suggestion: «Consider promote к wiki/concepts/ via /ingest» (R1 — Ruslan decides)
7. Output: final archived path + summary

## Examples

```bash
/hypothesis-close H-001 \
  --outcome confirmed \
  --outcome-text "Meta-method успешно применён к 3 non-engineering domains (Education / Personal-dev / Pitch development); clean cycle execution each" \
  --learning "Meta-method generalizes beyond engineering: pattern «cycle defined → discipline → output → reflection» replicates" \
  --reason "3-domain replication test completed 2026-MM-DD"

/hypothesis-close H-XXX \
  --outcome paused \
  --outcome-text "Test paused — partner availability blocked further data collection" \
  --reason "resource constraint"
```

## Required fields per outcome

- `confirmed` / `refuted` → outcome-text + learning REQUIRED (compound learning extraction discipline per Foundation Part 5)
- `paused` → outcome-text required; learning optional

## Cross-refs

- Foundation Part 5: Compound Learning & Methodology Capture (learning_extracted feeds substrate)
- `.claude/skills/hypothesis-update.md` (general update)
- `hypotheses/_schema/status.yaml` (transition rules)
- `hypotheses/_schema/outputs.yaml` (output taxonomy)
