---
title: CRM-style hypothesis overlay — Layer 3
date: 2026-05-20
type: documentation
parent_layer: 3
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-crm-overlay
R: low
---

# Layer 3 — CRM-style Overlay

> Layer 3 of 7. Bidirectional frontmatter pattern: hypothesis MD ↔ artefact MD cross-links.
> Pattern modeled after CRM (`crm/people/<slug>.md` ↔ `crm/orgs/<slug>.md` cross-refs).

## §1 Concept

Hypotheses live в `hypotheses/{active,testing,...}/H-NNN-<slug>.md`.

External artefacts (wiki concepts, decisions, reports, etc.) can reference hypotheses
via frontmatter `linked_hypotheses: [H-NNN, ...]` field.

Hypotheses можно reference artefacts via `linked_artefacts: [<path>, ...]` field.

**Bidirectional pattern:** Both sides should mutually link.

## §2 Frontmatter schema extension

### Hypothesis-side (already в `hypotheses/_schema/hypothesis.schema.yaml`)
```yaml
linked_artefacts:
  - wiki/concepts/method-systems-thinking.md
  - decisions/REFLECTION-INBOX-2026-05-16.md
linked_hypotheses:
  - H-001  # related hypothesis
```

### Artefact-side (extension к existing MDs)
```yaml
# At top of artefact frontmatter, optional field:
linked_hypotheses:
  - H-002
  - H-005
```

**No requirement** to retro-extend все existing MDs. Only when actively cross-linked
via `/hypothesis-link` skill OR manually.

## §3 Skill mechanics

`/hypothesis-link <H-NNN> <artefact-path>` маintains both sides:

1. Read hypothesis frontmatter; append `<artefact-path>` к `linked_artefacts`
2. Read artefact frontmatter; append H-NNN к `linked_hypotheses`
3. Write back both files
4. Update `updated` field on оба
5. Append к `hypotheses/_log.md`

## §4 Aggregation views (auto-generated)

`tools/build-hypothesis-views.py` walks repo + builds 3 views в `crm/hypothesis-views/`:

### `by-hypothesis.md`
```
## H-002
- **Hypothesis file:** hypotheses/active/H-002-partnership-frame.md
- wiki/concepts/pre-existing-partnership-positioning.md _(via artefact-side)_
- decisions/REFLECTION-INBOX-2026-05-16.md _(via hypothesis-side)_
```

### `by-artefact-type.md`
Group by top-level dir (wiki/concepts, decisions, reports, ...) → see distribution.

### `orphans.md`
Hypotheses без linked_artefacts (review trigger).

Re-run after `/hypothesis-link` operations:
```bash
/hypothesis-build-views
# or direct: python3 tools/build-hypothesis-views.py
```

## §5 When to cross-link

✅ **Link when:**
- Hypothesis was inspired by / derives from specific wiki concept
- Hypothesis tests a claim в a decision record
- Hypothesis result will feed back to specific artefact §APPEND
- Hypothesis informs или is informed by a report

❌ **Don't link when:**
- Generic, unrelated mention
- Just want к find via search later (use `/hypothesis-search` instead)
- Reference is transient (skill name, person name — not artefact)

## §6 Comparison с CRM pattern

CRM:
- `crm/people/<slug>.md` cross-refs `crm/orgs/<slug>.md` via §11 sections
- Strategy hooks pre-fill via `crm/_schema/strategy-hooks.yaml`

Hypothesis overlay:
- `hypotheses/<status>/H-NNN-<slug>.md` cross-refs anywhere в repo
- `linked_hypotheses` frontmatter retrofits onto ANY artefact

Hypothesis overlay = **lighter weight** (no full template); artefact only adds 1-line frontmatter field.

## §7 Anti-patterns

- ❌ **One-way links** — only hypothesis-side OR only artefact-side; views show incomplete picture
- ❌ **Mass auto-linking** — Default-Deny (R11); per-link Ruslan or manual decision
- ❌ **Linking без frontmatter** — artefact needs YAML frontmatter; halt + warn
- ❌ **Circular dependency reliance** — links are navigational, not causal

## §8 Cross-refs

- **Skill (link):** `.claude/skills/hypothesis-link.md` (bidirectional patcher)
- **Skill (views):** `.claude/skills/hypothesis-build-views.md`
- **Build script:** `tools/build-hypothesis-views.py`
- **Output:** `crm/hypothesis-views/` (auto-generated; do not edit manually)
- **CRM analogous:** `crm/README.md` (§«CRM System» pattern)
- **Layer 7 complement:** `hypotheses/docs/excel-table-usage.md` (CSV/xlsx has different aggregation pattern)
