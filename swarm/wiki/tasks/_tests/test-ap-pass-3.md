---
id: test-ap-pass-3
type: test-fixture
test_target: lint-check-13
expected_outcome: pass
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). One cell with a 195-char predicate (upper boundary test). Created by OPP-04 cycle-2-impl."
---

# Fixture — PASS case 3 (1 cell, 195-char boundary predicate)

```yaml
task_id: task-test-ap-pass-3
decomposed_at: 2026-04-24
shape: scale-project
chat_or_decompose: decompose
decomposition:
  - cell: systems × scalability
    ap_cost: 45000
    ap_budget: 70000
    inputs: [swarm/wiki/meta/health.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-3-systems-scalability.md
    cell_acceptance_predicate: "BOSC-A-T-X trigger named per gate AND MHT event per gate AND Janus spec for both S-A and INT excess AND recovery binary AND antifragility check AND ≤30 percent refactor claim stated per 10x gate"
```
