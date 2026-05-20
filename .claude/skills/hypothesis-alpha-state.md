---
name: hypothesis-alpha-state
description: Update OMG Essence alpha state для hypothesis (Layer 6) + append alpha-trail markdown + validate state-graph transition.
type: skill
---

# /hypothesis-alpha-state

Update alpha state per OMG Essence 2.0:2024 state-graphs.

## Arguments

| Flag | Required | Описание |
|---|---|---|
| `<H-NNN>` | yes | Hypothesis id |
| `--alpha NAME` | yes | One of {stakeholder, opportunity, requirements, software-system, work, team, way-of-working} |
| `--state STATE` | yes | Valid state per alphas.yaml state_graph |
| `--note "<text>"` | no | Reason / context для transition |

## Workflow

1. Locate H-NNN; parse `alphas:` frontmatter
2. Validate `--alpha` in `_schema/alphas.yaml` keys
3. Validate `--state` in alpha's `state_graph` list
4. Validate transition: state must be later или same as previous state in state_graph (no reversion без `--allow-reverse`)
5. Update frontmatter:
   ```yaml
   alphas:
     - alpha: <name>
       state: <new-state>
       # other alphas preserved
   ```
6. Update `updated` к today
7. Append к `hypotheses/alphas/state-graphs/<H-NNN>-alpha-trail.md`:
   ```markdown
   ## YYYY-MM-DD — alpha <name> → <state>
   - Previous: <prev-state>
   - Note: <note>
   ```
8. Append к `hypotheses/_log.md` (1-line summary)
9. Output: confirmation + alpha-trail path

## State-graph reference

Per `hypotheses/_schema/alphas.yaml`:

| Alpha | State sequence |
|---|---|
| stakeholder | recognized → represented → involved → in_agreement → satisfied_for_deployment → satisfied_in_use |
| opportunity | identified → solution_needed → value_established → viable → addressed → benefit_accrued |
| requirements | conceived → bounded → coherent → acceptable → addressed → fulfilled |
| software-system | architecture_selected → demonstrable → usable → ready → operational → retired |
| work | initiated → prepared → started → under_control → concluded → closed |
| team | seeded → formed → collaborating → performing → adjourned |
| way-of-working | principles_established → foundation_established → in_use → in_place → working_well → retired |

## Examples

```bash
/hypothesis-alpha-state H-001 --alpha work --state started \
  --note "Applied meta-method к Education domain — first cycle starting"

/hypothesis-alpha-state H-005 --alpha way-of-working --state in_use \
  --note "Recursive method-as-1st-class-object pattern adopted в daily workflow"
```

## Validation gate

- Alpha + state must be valid per alphas.yaml
- Transition must be monotonic (state index increases) unless `--allow-reverse`
- Default-Deny invalid combinations (R11)

## Cross-refs

- `hypotheses/_schema/alphas.yaml` (7 alphas + state graphs)
- `hypotheses/alphas/_alphas-overview.md` (overview)
- `hypotheses/alphas/state-graphs/` (per-alpha state graph mermaid)
- Левенчук Методология 2025 Гл. 4 (MG4 ⭐⭐⭐) — primary source
