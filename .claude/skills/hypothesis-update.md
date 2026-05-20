---
name: hypothesis-update
description: Update hypothesis frontmatter (status / FPF / alphas / linked) + auto-move file across status dirs + append log.
type: skill
---

# /hypothesis-update

Update existing hypothesis frontmatter — supports status transitions, FPF upgrades, alpha state updates, linked_artefacts append.

## Arguments

| Flag | Required | Описание |
|---|---|---|
| `<H-NNN>` | yes | Hypothesis id |
| `--status STATUS` | no | One of {active, testing, confirmed, refuted, paused}; triggers file move |
| `--reason "<text>"` | no | Reason for change (logged) |
| `--fpf-F F2..F8` | no | Update F-grade |
| `--fpf-R low\|medium\|high` | no | Update reliability |
| `--add-artefact PATH` | no | Append к linked_artefacts |
| `--add-hypothesis H-NNN` | no | Append к linked_hypotheses |
| `--owner OWNER` | no | Change owner (rare; logged) |

## Workflow

1. Locate `H-NNN` файл: scan `hypotheses/{active,testing,confirmed,refuted,paused,samples}/`
2. Parse current frontmatter
3. Apply updates:
   - `--status` triggers transition validation per `_schema/status.yaml` transitions
   - For confirmed/refuted/paused → require `outcome` OR prompt user via skill prompt
   - Update `updated` к today
4. If status changed → move file from `<old>/` к `<new>/` directory (`git mv`)
5. Append к `hypotheses/_log.md`:
   ```
   ## YYYY-MM-DD HH:MM — H-NNN updated
   - Field: <field> — <old> → <new>
   - Reason: <reason>
   - New file path: hypotheses/<status>/<H-NNN>-<slug>.md
   ```
6. Output: confirmation + new file path

## State machine (per _schema/status.yaml)

Allowed transitions:
- `active` → `testing` | `paused`
- `testing` → `confirmed` | `refuted` | `paused`
- `paused` → `active`
- `confirmed` | `refuted` → terminal (но frontmatter editable для F-grade promotion)

Invalid transitions → halt + report.

## Examples

```bash
# Move to testing
/hypothesis-update H-002 --status testing --reason "outreach sequence sent к 5 L2 partners"

# Upgrade F-grade after corroboration
/hypothesis-update H-001 --fpf-F F4 --fpf-R medium --reason "applied к 3 domains; replicated"

# Link artefact
/hypothesis-update H-005 --add-artefact wiki/concepts/method-systems-thinking.md
```

## Validation gates

- Status transition allowed per status.yaml? else halt
- Required outputs (outcome/learning) for confirmed/refuted/paused
- F-grade monotonic (downgrade requires `--allow-downgrade` flag)

## Cross-refs

- `.claude/skills/hypothesis-close.md` (terminal close shortcut)
- `.claude/skills/crm-update.md` (analogous pattern)
