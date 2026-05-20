---
name: hypothesis-stuck
description: Find hypotheses status=testing с updated >N days ago + recommended actions (close paused or resume).
type: skill
---

# /hypothesis-stuck

Surface stuck hypotheses для review.

## Arguments

| Flag | Required | Default | Описание |
|---|---|---|---|
| `--days N` | no | 14 | Threshold для «stuck» |
| `--status STATUS` | no | testing | Default testing; alt: active |
| `--owner OWNER` | no | all | Filter |

## Workflow

1. Walk `hypotheses/<status>/` directory
2. Parse frontmatter; compute days since `updated`
3. Filter: days > N → stuck list
4. Per stuck hypothesis output:
   - H-NNN [status] [category]: <title>
   - Last updated: <date> (N days ago)
   - Test method: <one-line>
   - Recommended actions:
     - Если updated > 30d: «Consider /hypothesis-close --outcome paused»
     - Если linked_artefacts changed recently (any artefact updated post hypothesis updated): «Resume / re-check signal»
     - Else: «Surface к Ruslan для decision»
5. Optionally append к `hypotheses/_log.md` weekly entry if `--weekly` flag set

## Examples

```bash
/hypothesis-stuck                    # default: testing > 14d
/hypothesis-stuck --days 30          # only longer-stuck
/hypothesis-stuck --status active    # active без test initiated
```

## Constitutional posture

- Surfaces only (R1): does NOT auto-close или auto-pause
- Default-Deny на bulk transitions (R11): per-hypothesis Ruslan decides

## Cross-refs

- `.claude/skills/crm-stuck.md` (analogous pattern)
- Pillar C §4.2: attention budget discipline
