---
id: proposal-T-swarm-self-improve-v1-decomposition
title: WBS — Swarm Self-Improvement v1
type: proposal
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
decomposed_at: 2026-04-23
shape: combined-design-review-scale-project
chat_or_decompose: decompose
produced_by: brigadier
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: linted
state: drafted
confidence: medium
confidence_method: rubric-based
tier: operational
sources:
  - {path: "tasks/T-swarm-self-improve-v1-2026-04-23.md", range: "§Phase 1..§Phase 8"}
  - {path: ".claude/agents/brigadier.md", range: "§3.1..§3.5, §4.1..§4.6"}
  - {path: "swarm/lib/shared-protocols.md", range: "§3, §4"}
---

# WBS — Swarm Self-Improvement v1

## Decompose-or-Chat gate verdict

Per brigadier §3.0 (E-17) — all four predicates fire:
1. Complexity > simple: ≥6 domain lenses required across agents / wiki / memory / skills.
2. Adversarial review required: critic-mode over 6 current agent files demanded.
3. Horizon projection required: 2× quality claim requires scalability check on top opportunities.
4. Multi-domain synthesis required: integrator mode across engineering + mgmt + systems + philosophy + investor.

**Decision: decompose.**

## Shape classification

`design + review + scale-project` combined. Union of defaults (capped at 20 cells).

## Cell roster (target, excluding Phase-1 read sub-agents which are NOT matrix cells)

| # | Cell                         | Phase | ap_budget (turns) | inputs                                           | expected artefact                                              |
|---|------------------------------|-------|-------------------|--------------------------------------------------|----------------------------------------------------------------|
| 1 | engineering × critic         | 2 R1  | 80                | context/α+β+γ+δ+ε+ζ extracts + 6 agent files     | artefacts/engineering-critic-01.md                             |
| 2 | mgmt × critic                | 2 R1  | 80                | same                                             | artefacts/mgmt-critic-01.md                                    |
| 3 | systems × critic             | 2 R1  | 80                | same                                             | artefacts/systems-critic-01.md                                 |
| 4 | philosophy × critic          | 2 R1  | 80                | same                                             | artefacts/philosophy-critic-01.md                              |
| 5 | investor × critic            | 2 R1  | 80                | same                                             | artefacts/investor-critic-01.md                                |
| 6 | engineering × optimizer      | 2 R2  | 70                | context/ + artefacts/engineering-critic-01.md    | artefacts/engineering-optimizer-01.md                          |
| 7 | mgmt × optimizer             | 2 R2  | 70                | context/ + mgmt-critic-01.md                     | artefacts/mgmt-optimizer-01.md                                 |
| 8 | systems × optimizer          | 2 R2  | 70                | context/ + systems-critic-01.md                  | artefacts/systems-optimizer-01.md                              |
| 9 | philosophy × optimizer       | 2 R2  | 70                | context/ + philosophy-critic-01.md               | artefacts/philosophy-optimizer-01.md                           |
| 10| investor × optimizer         | 2 R2  | 70                | context/ + investor-critic-01.md                 | artefacts/investor-optimizer-01.md                             |
| 11| mgmt × integrator            | 2 R3  | 90                | all 10 R1+R2 artefacts                           | artefacts/mgmt-integrator-01.md (hypothesis synthesis)         |
| 12| philosophy × integrator      | 2 R3  | 60                | integrator-01.md                                 | artefacts/philosophy-integrator-01.md (epistemic meta-sanity)  |
| 13| systems × scalability        | 5     | 50 (post-Gate-1)  | Document-2 top opportunities                     | artefacts/systems-scalability-01.md (optional pass)            |

**Matrix 5×4 coverage.** 13 cells × 4 modes (critic, optimizer, integrator, scalability) —
exceeds ≥4×≥2 floor. 5 experts × 3 modes core (critic/optimizer/integrator) + 1 expert ×
scalability = full matrix demonstration.

## ap_cost budget totals

- Phase 1 sub-agents (read-only, outside matrix): 6 × ~120 turns = 720 turns (context/ writes).
- Phase 2 matrix cells (1..12): ~900 turns.
- Phase 3 brigadier synthesis: ~150 turns.
- Phase 4 gate write: ~40 turns.
- Phase 5 drafting (+ opt. cell 13): ~250 turns.
- Phase 6 gate write: ~40 turns.
- Phase 7 compound: ~200 turns.
- Phase 8 closure: ~80 turns.

Total wall-clock budget estimate: ~2500 turns. Well under any per-day 200-turn brigadier
soft cap when counted per-invocation (each sub-agent runs in its own Task context).

## Risk register

| risk                                                                                  | likelihood | impact | mitigation                                                                                   |
|---------------------------------------------------------------------------------------|------------|--------|----------------------------------------------------------------------------------------------|
| Sub-agents inline source bodies in returned summaries (AP-1)                          | medium     | medium | Brief explicitly forbids inlining > 50 lines; require disk-path citation                     |
| Critics return "looks good" (AP-2)                                                    | medium     | medium | Brief requires ≥5 binary Conformance-Checklist items; reject otherwise                       |
| Optimizers masquerade method-change as optimization (AP-3)                            | low        | high   | Brief states: optimizer touches execution parameters only; method change → integrator/HITL   |
| Integrator averages dissent (AP-6)                                                    | medium     | high   | Brief requires `dissents[]` explicit per E-5 with (F, ClaimScope, R)                         |
| Cell invokes peer cell directly                                                       | low        | high   | Cells lack Task tool by role matrix; /lint check for `Task(` in draft bodies                 |
| Cycle exceeds 2× budget without HITL                                                  | low        | medium | Per-cell ap_budget + brigadier aggregate watch; §6 gate-trigger #4                           |
| Hypothesis count < 25 at Phase 3                                                      | low        | medium | 5 critics × 5 optimizers × 2 integrators across 4 dimensions → ≥40 raw hypotheses expected   |
| Provenance gate fails > 2× on same draft                                              | low        | medium | §5.6 retry-limit; escalate per §1d                                                           |
| ANTHROPIC/GROQ env vars not unset at session start (Max-sub discipline)               | confirmed  | low    | Flag to operator at Gate 1; brigadier itself invokes no paid APIs; see open-question at G1   |

## Dependency order

- Phase 1 (6 sub-agents) → parallel, all independent.
- Phase 2 R1 (5 critics) → parallel, depend on Phase 1 artefacts.
- Phase 2 R2 (5 optimizers) → parallel, each depends on its same-expert R1 critic.
- Phase 2 R3 (2 integrators) → serial: `mgmt × integrator` first; if inconsistency surfaces,
  `philosophy × integrator` as meta-sanity pass per §5.3 case 4.
- Phase 3 → brigadier serial.
- Phase 4 → gate; pause.
- Phase 5 → cell 13 optional, parallel with brigadier drafting.
- Phase 6 → gate; pause.
- Phase 7 → brigadier serial (compound writes).
- Phase 8 → brigadier serial (cycle log).
