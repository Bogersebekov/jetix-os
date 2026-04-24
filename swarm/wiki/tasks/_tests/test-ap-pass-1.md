---
id: test-ap-pass-1
type: test-fixture
test_target: lint-check-13
expected_outcome: pass
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). Two cells, both with valid 50-100 char predicates. Created by OPP-04 cycle-2-impl."
---

# Fixture — PASS case 1 (2 cells, valid predicates)

```yaml
task_id: task-test-ap-pass-1
decomposed_at: 2026-04-24
shape: review
chat_or_decompose: decompose
decomposition:
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [swarm/lib/shared-protocols.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-1-engineering-critic.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks plus ≥2 Alternatives plus Anti-scope section"
  - cell: mgmt × critic
    ap_cost: 30000
    ap_budget: 50000
    inputs: [.claude/agents/brigadier.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-1-mgmt-critic.md
    cell_acceptance_predicate: "Each H-N hypothesis row carries falsifier plus (F, ClaimScope, R) triple"
```
