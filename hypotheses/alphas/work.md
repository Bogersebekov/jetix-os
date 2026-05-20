---
alpha: work
date: 2026-05-20
F: F2
G: hypotheses-alpha-machinery
R: low
source: "OMG Essence 2.0:2024 + Левенчук Методология 2025 Гл. 4"
---

# Alpha: Work

## Purpose
Activity being undertaken — the cycle / sprint / phase performing the hypothesis test.

## State graph
```
initiated → prepared → started → under_control → concluded → closed
```

## State definitions

| State | Meaning |
|---|---|
| **initiated** | Work request / hypothesis test acknowledged; backlog item |
| **prepared** | Method clear; resources allocated; ready to start |
| **started** | Actual work began |
| **under_control** | Predictable progress; on track |
| **concluded** | Work completed (outcome obtained — confirmed/refuted) |
| **closed** | Closure formal — outcome logged, learning extracted, archived |

## Jetix application

- Hypothesis status=active → work in {initiated, prepared}
- Hypothesis status=testing → work in {started, under_control}
- Hypothesis status=confirmed/refuted → work in {concluded, closed}
- Hypothesis status=paused → work special state — `under_control` paused

## Example transition

```
2026-05-20 — work → initiated: H-001 added to backlog
2026-05-20 — work → prepared: test_method documented
2026-05-25 — work → started: pilot к Education domain begun
2026-06-15 — work → under_control: regular cadence; 2 of 3 domains complete
2026-09-XX — work → concluded: all 3 domains tested; result documented
2026-09-XX — work → closed: /hypothesis-close called; learning extracted
```

## Cross-refs

- Schema: `_schema/alphas.yaml`
- State-graph: `state-graphs/work-state-graph.md`
- Overview: `_alphas-overview.md`
