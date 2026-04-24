---
id: test-ap-fail-missing
type: test-fixture
test_target: lint-check-13
expected_outcome: fail-missing
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). Three cells, only two carry the field — must trigger cell-ap-missing slug. Created by OPP-04 cycle-2-impl."
---

# Fixture — FAIL case cell-ap-missing (3 cells, 2 fields)

```yaml
task_id: task-test-ap-fail-missing
decomposed_at: 2026-04-24
shape: review
chat_or_decompose: decompose
decomposition:
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [swarm/lib/shared-protocols.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-fail-missing-engineering-critic.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks AND ≥2 Alternatives AND Anti-scope present"
  - cell: mgmt × critic
    ap_cost: 30000
    ap_budget: 50000
    inputs: [.claude/agents/brigadier.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-fail-missing-mgmt-critic.md
    cell_acceptance_predicate: "Each H-N row carries falsifier AND (F, ClaimScope, R) triple per claim"
  - cell: systems × critic
    ap_cost: 35000
    ap_budget: 55000
    inputs: [.claude/agents/brigadier.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-fail-missing-systems-critic.md
    # NOTE: cell_acceptance_predicate intentionally absent — expected to trigger cell-ap-missing slug.
```
