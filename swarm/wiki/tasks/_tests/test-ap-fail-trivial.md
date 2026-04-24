---
id: test-ap-fail-trivial
type: test-fixture
test_target: lint-check-13
expected_outcome: fail-trivial
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). Two cells, one carries a trivial artefact-existence predicate — must trigger cell-ap-trivial slug. Created by OPP-04 cycle-2-impl."
---

# Fixture — FAIL case cell-ap-trivial (anti-regex match)

```yaml
task_id: task-test-ap-fail-trivial
decomposed_at: 2026-04-24
shape: review
chat_or_decompose: decompose
decomposition:
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [swarm/lib/shared-protocols.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-fail-trivial-engineering-critic.md
    cell_acceptance_predicate: "artefact exists"
  - cell: mgmt × critic
    ap_cost: 30000
    ap_budget: 50000
    inputs: [.claude/agents/brigadier.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-fail-trivial-mgmt-critic.md
    cell_acceptance_predicate: "Each H-N row carries falsifier AND (F, ClaimScope, R) triple per claim"
```
