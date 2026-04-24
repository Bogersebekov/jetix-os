---
name: "levenchuk-deep-dive-brigadier"
description: |
  STUB — P3 project. No mini-swarm spawned at bootstrap per /project-bootstrap §8
  algorithm (P3/P4: no mini-swarm; expert dispatch via canonical brigadier on-demand).
  This file is a routing stub only. If project reaches SG-4 momentum threshold
  and HITL promotes to P2, /project-bootstrap --promote will instantiate a real
  mini-swarm agent. Until then: canonical brigadier dispatches systems-expert +
  philosophy-expert on-demand per open-questions.md items.
model: sonnet
tools: [Read, Write, Edit, Grep, Glob]
granularity: project-scoped
owner: ruslan
created: "2026-04-24"
last_modified: "2026-04-24"
primary_alpha: task
secondary_alphas: [cycle, artefact]
domains: [project-task-routing-stub]
active_task_limit: 0
scope_subtree: "operations/levenchuk-deep-dive/"
default_experts:
  - systems-expert
  - philosophy-expert
sole_writer_of: "operations/levenchuk-deep-dive/"
stub: true
stub_reason: "P3 project; mini-swarm requires P1/P2. Upgrade path: HITL acks SG-4 + /project-promote."
---

# Project-Brigadier Stub — levenchuk-deep-dive

P3 research project. No active mini-swarm per `/project-bootstrap §8`
(P3/P4 projects → no mini-swarm spawned).

## Routing for on-demand expert dispatch

When Ruslan or canonical brigadier needs work done on this project:
1. Canonical brigadier reads `operations/levenchuk-deep-dive/_moc.md` + `open-questions.md`.
2. Dispatches `systems-expert × <mode>` OR `philosophy-expert × <mode>` on-demand.
3. Outputs land under `operations/levenchuk-deep-dive/drafts/<id>-<mode>-<slug>.md`.

Default experts (from project-types.yaml research type):
- **systems-expert** — feedback loops, system archetypes, Левенчук ШСМ primary reader
- **philosophy-expert** — Popperian hypothesis critique, epistemic audit, first-principles reset

## Upgrade path (P3 → P2 promotion)

If SG-4 fires (`context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`):
1. Canonical brigadier emits escalations[]{trigger: sg-promotion-eligible, sg: SG-4, project: levenchuk-deep-dive}.
2. HITL (Ruslan) acks: promote to P2 via `/project-promote levenchuk-deep-dive --to=P2`.
3. Mini-swarm instantiated: real `levenchuk-deep-dive-brigadier.md` replaces this stub.
4. This stub file is archived to `agents/levenchuk-deep-dive-brigadier/stub-archived-<date>.md`.

## Write scope

`operations/levenchuk-deep-dive/` subtree only.
Canonical brigadier is sole commit authority.
