---
name: hypothesis-add
description: Scaffold new hypothesis в hypotheses/active/ with H-NNN id + template + FPF F-G-R mandatory frontmatter.
type: skill
---

# /hypothesis-add

Создаёт новый H-NNN file в `hypotheses/active/<H-NNN>-<slug>.md` с pre-filled frontmatter из template.

## Arguments

| Flag | Required | Default | Описание |
|---|---|---|---|
| `<slug>` | yes | — | kebab-case identifier |
| `--category CAT` | no | prompt | См. `hypotheses/_schema/categories.yaml` (8 values) |
| `--owner OWNER` | no | `ruslan` | См. `hypotheses/_schema/ownership.yaml` |
| `--lifecycle short\|medium\|long` | no | `medium` | См. `hypotheses/_templates/` |
| `--title "<text>"` | no | prompt | One-line statement |
| `--fpf-F F2..F8` | no | `F2` | Per FPF B.3 |
| `--fpf-G "<scope>"` | no | prompt | Group scope |
| `--fpf-R low\|medium\|high` | no | `low` | Reliability |
| `--strategic-region REGION` | no | `catallactic` | См. `_schema/fpf-strategic-regions.yaml` |

## Workflow

1. Прочитать `hypotheses/_schema/hypothesis.schema.yaml` для required_fields
2. Determine next H-NNN id: scan `hypotheses/{active,testing,confirmed,refuted,paused,samples}/` для max `H-(\d{3})` → +1
3. Прочитать `hypotheses/_templates/hypothesis-<lifecycle>.md`
4. Substitute placeholders: `id` / `slug` / `title` / `created` / `owner` / `category` / `lifecycle` / FPF triple / `strategic_region`
5. Write к `hypotheses/active/<H-NNN>-<slug>.md`
6. Validate: F-G-R triple present (Layer 5 mandatory); если missing → halt + report
7. Append к `hypotheses/_log.md`:
   ```
   ## YYYY-MM-DD HH:MM — H-NNN created
   - Title: <title>
   - Owner: <owner>
   - Category: <category>
   - Lifecycle: <lifecycle>
   - FPF: <F>/<G>/<R>
   - File: hypotheses/active/<H-NNN>-<slug>.md
   ```
8. Output: full file path + reminder: «Ruslan edits prose в Гипотеза + Метод теста sections»

## Examples

```bash
/hypothesis-add partnership-frame-better-than-cheatcode-l2 \
  --category outreach \
  --lifecycle medium \
  --title "Partnership-frame outperforms cheat-code positioning для L2 outreach" \
  --fpf-F F2 \
  --fpf-G outreach-pipeline \
  --fpf-R low
# Output: hypotheses/active/H-006-partnership-frame-better-than-cheatcode-l2.md
```

## Validation gate

- F-G-R triple mandatory per `_schema/hypothesis.schema.yaml` validation rules
- Slug uniqueness check across all `hypotheses/*/H-*.md`
- Default-Deny: если category/owner not in enum → halt + report (per R11)

## Cross-refs

- Schema: `hypotheses/_schema/hypothesis.schema.yaml`
- Templates: `hypotheses/_templates/`
- Log: `hypotheses/_log.md`
- Analogous: `.claude/skills/crm-add.md`
