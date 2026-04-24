---
id: test-ap-pass-2
type: test-fixture
test_target: lint-check-13
expected_outcome: pass
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). Five cells, all with valid predicates referencing different artefact types. Created by OPP-04 cycle-2-impl."
---

# Fixture — PASS case 2 (5 cells, diverse artefact types)

```yaml
task_id: task-test-ap-pass-2
decomposed_at: 2026-04-24
shape: combined-design-review
chat_or_decompose: decompose
decomposition:
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [swarm/lib/shared-protocols.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-2-engineering-critic.md
    cell_acceptance_predicate: "Returns ≥5 Conformance Checks AND each check cites a canonical engineering pattern"
  - cell: systems × scalability
    ap_cost: 40000
    ap_budget: 60000
    inputs: [decisions/JETIX-ARCHITECTURE-BRIEF.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-2-systems-scalability.md
    cell_acceptance_predicate: "BOSC-A-T-X first-trigger named per gate AND MHT event per gate AND Janus degraded-mode spec"
  - cell: mgmt × integrator
    ap_cost: 30000
    ap_budget: 50000
    inputs: [swarm/wiki/drafts/task-test-ap-pass-2-engineering-critic.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-2-mgmt-integrator.md
    cell_acceptance_predicate: "Dissents preserved with (F, ClaimScope, R) AND opportunity ranking matrix present"
  - cell: philosophy × critic
    ap_cost: 35000
    ap_budget: 55000
    inputs: [swarm/wiki/drafts/task-test-ap-pass-2-engineering-critic.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-2-philosophy-critic.md
    cell_acceptance_predicate: "Every claim carries F-level plus ClaimScope plus falsifier condition"
  - cell: investor × optimizer
    ap_cost: 25000
    ap_budget: 45000
    inputs: [swarm/wiki/drafts/task-test-ap-pass-2-mgmt-integrator.md]
    expected_artefact: swarm/wiki/drafts/task-test-ap-pass-2-investor-optimizer.md
    cell_acceptance_predicate: "Before/after snapshot table AND Kelly score computed for each proposed hypothesis"
```
