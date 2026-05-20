---
name: hypothesis-search
description: Grep across all hypothesis MDs (title / body / linked_artefacts) + ranked output.
type: skill
---

# /hypothesis-search

Search across all hypothesis files.

## Arguments

| Flag | Required | Описание |
|---|---|---|
| `<query>` | yes | Search string или regex |
| `--field title\|body\|artefact\|all` | no | Default: all |
| `--status STATUS` | no | Filter by status |
| `--category CAT` | no | Filter by category |
| `--limit N` | no | Default 20 |

## Workflow

1. Walk `hypotheses/{active,testing,confirmed,refuted,paused,samples}/` для *.md
2. Per field type:
   - `title` — match against `title:` frontmatter
   - `body` — full-text grep
   - `artefact` — match against `linked_artefacts:` list entries
   - `all` — union
3. Rank by:
   - Title match: weight 3.0
   - Body match: weight 1.0
   - Artefact match: weight 2.0
   - Multi-field bonus
4. Output ranked list:
   ```
   1. H-NNN [status] [category]: <title>
      Match: title (verbatim)
      File: hypotheses/active/H-NNN-<slug>.md
   2. ...
   ```

## Examples

```bash
/hypothesis-search "meta-method" --status active
/hypothesis-search "Левенчук" --field body --limit 5
/hypothesis-search "wiki/concepts/method-systems-thinking" --field artefact
```

## Cross-refs

- `.claude/skills/crm-search.md` (analogous pattern)
- `.claude/skills/search-kb.md` (general KB search; complement)
