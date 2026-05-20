---
name: hypothesis-build-views
description: Aggregate CRM-style hypothesis overlay views across repo (Layer 3) — by-hypothesis, by-artefact-type, orphans.
type: skill
---

# /hypothesis-build-views

Rebuild CRM-style hypothesis overlay views.

## Workflow

```bash
cd ~/jetix-os
python3 tools/build-hypothesis-views.py
```

Output 3 files в `crm/hypothesis-views/`:
1. `by-hypothesis.md` — H-NNN → list of linked artefacts (bidirectional aggregation)
2. `by-artefact-type.md` — group linked artefacts by top-level directory (wiki/concepts, decisions/, etc.)
3. `orphans.md` — hypotheses без any cross-links (need attention)

## How it works

1. Walks repo `*.md` files (excluding .git, node_modules, raw/external, archive)
2. Parses YAML frontmatter
3. Collects:
   - **Hypothesis-side:** files в `hypotheses/` с id=H-NNN; reads `linked_artefacts`
   - **Artefact-side:** all other MDs с `linked_hypotheses: [H-NNN]` frontmatter
4. Merges both sides → unified mapping H-NNN ↔ artefacts
5. Writes 3 view files

## Cross-link bidirectional pattern

```yaml
# В hypothesis MD (hypotheses/active/H-002-...md)
linked_artefacts:
  - wiki/concepts/pre-existing-partnership-positioning.md
  - decisions/REFLECTION-INBOX-2026-05-16.md

# В artefact MD (wiki/concepts/pre-existing-partnership-positioning.md)
linked_hypotheses:
  - H-002
```

Both sides surfaced в view. `/hypothesis-link` skill maintains both directions automatically.

## When to run

- After `/hypothesis-link` mass operations
- Before weekly review (`/hypothesis-dash` complement)
- Before sharing snapshot с stakeholders

## Cross-refs

- Build script: `tools/build-hypothesis-views.py`
- Documentation: `hypotheses/docs/crm-style-overlay.md`
- Output directory: `crm/hypothesis-views/`
- Skill: `.claude/skills/hypothesis-link.md` (maintains bidirectional links)
