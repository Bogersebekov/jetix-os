---
alpha: requirements
date: 2026-05-20
F: F2
G: hypotheses-alpha-machinery
R: low
source: "OMG Essence 2.0:2024 + Левенчук Методология 2025 Гл. 4"
---

# Alpha: Requirements

## Purpose
What outcome must achieve — explicit articulation of acceptance criteria.

## State graph
```
conceived → bounded → coherent → acceptable → addressed → fulfilled
```

## State definitions

| State | Meaning |
|---|---|
| **conceived** | Idea of requirements existing; raw |
| **bounded** | Scope explicitly defined — what's in/out |
| **coherent** | Requirements together don't contradict — internally consistent |
| **acceptable** | Stakeholders accept the requirement set |
| **addressed** | Solution covers requirements; implementation progressing |
| **fulfilled** | All requirements met; closure can occur |

## Jetix application

Для hypothesis substrate, requirements = success/refutation criteria + scope:
- Hypothesis `success_criteria` + `refutation_criteria` = requirement set
- `test_scope` = bounded state
- Pre-test: typically **bounded** (test_method documented)
- Mid-test: **coherent** (criteria don't contradict observations)
- Post-test confirmed: **fulfilled**

## Example transition

```
2026-05-20 — requirements → conceived: «meta-method should work cross-domain»
2026-05-21 — requirements → bounded: scope = Education + Personal-dev + Pitch domains
2026-05-22 — requirements → coherent: success criteria don't conflict across domains
2026-XX-XX — requirements → fulfilled: 3-domain replication complete
```

## Cross-refs

- Schema: `_schema/alphas.yaml`
- State-graph: `state-graphs/requirements-state-graph.md`
- Overview: `_alphas-overview.md`
