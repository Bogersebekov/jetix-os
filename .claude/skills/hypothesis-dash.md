---
name: hypothesis-dash
description: Aggregate dashboard view across all hypotheses — counts, top active, attention budget check, regenerate _index.md.
type: skill
---

# /hypothesis-dash

Aggregate view all hypotheses + attention budget compliance + regenerate `hypotheses/_index.md`.

## Arguments

| Flag | Required | Default | Описание |
|---|---|---|---|
| `--filter STATUS` | no | active+testing | Filter by status |
| `--category CAT` | no | all | Filter by category |
| `--owner OWNER` | no | all | Filter by owner |
| `--lifecycle SHORT\|MEDIUM\|LONG` | no | all | Filter |
| `--format md\|json` | no | md | Output format |
| `--rebuild-index` | no | true | Regenerate hypotheses/_index.md |

## Workflow

1. Walk `hypotheses/{active,testing,confirmed,refuted,paused,samples}/` для *.md files
2. Parse frontmatter каждой (yaml + standard fields)
3. Build aggregations:
   - Counts by status
   - Counts by category
   - Counts by F-grade (F2..F8 distribution)
   - Counts by lifecycle (short/medium/long)
   - Top 5-10 active (sorted by updated desc)
   - Recently closed (last 7 days; from log)
   - Attention budget: count active+testing vs 20 cap (Pillar C §4.2 RUSLAN-LAYER)
4. Render to markdown table OR json
5. Regenerate `hypotheses/_index.md` если `--rebuild-index` (default true)
6. Output к stdout + optionally к `hypotheses/_index.md`

## Attention budget alerts

- active + testing count ≤ 15: ✅ healthy
- 16-20: ⚠️ approaching cap — review `/hypothesis-stuck` для paused candidates
- > 20: 🛑 over budget — surface к Ruslan: must pause/close some

## Examples

```bash
# Default — active+testing dashboard + regen index
/hypothesis-dash

# Filter by category
/hypothesis-dash --category outreach

# JSON для programmatic
/hypothesis-dash --format json --filter testing
```

## Output sample (markdown)

```
# Hypotheses Dashboard — YYYY-MM-DD

## Counts by status
| Status | Count |
| active | N |
| testing | N |
| ...

## Top active (by updated desc)
- H-NNN [category]: <title> — F<X>/G:<scope>/R:<r>
- ...

## Attention budget
active + testing: N / 20  [status]
```

## Cross-refs

- `.claude/skills/crm-dash.md` (analogous pattern)
- `hypotheses/_index.md` (output target)
- Pillar C §4.2 RUSLAN-LAYER: attention budget cap
