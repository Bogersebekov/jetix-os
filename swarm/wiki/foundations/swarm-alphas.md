---
id: foundation-01HF2K3M5N7P9Q12345678ALPHA
title: Swarm Alphas (5)
type: foundation
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: linted
state: accepted
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources:
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 4"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D5"}
related: []                # topic / foundation hubs deferred — see Phase B activation; was [[foundations/swarm-protocols]] before critic-gate1 H-1 fix
topics: []                 # was [[topics/swarm-architecture-hub]] before critic-gate1 H-1 fix
binding_scope: swarm-wide
supersedes_versions: []
---

# Swarm Alphas — 5 State Machines

This foundation page is the **single source of truth** for the five
alphas that organize all swarm work. Every Task, Artefact,
Strategies-Rule, Cycle, and Direction in Jetix flows through one of
these state machines. Agent prompts under `.claude/agents/` reference
this file by section, never duplicate its contents.

## α-1 Task

**States:** `submitted | intaked | decomposed | dispatched | integrated | gated | approved | compounded | archived | refused | rejected | returned`

**Transitions:**

| from | to | trigger | mover | side-effects |
|---|---|---|---|---|
| submitted | intaked | brigadier reads+classifies | brigadier | `swarm/wiki/tasks/<task-id>/` dir + `open-questions.md` |
| submitted | refused | out-of-scope/malformed | brigadier | `swarm/gates/refused-<task-id>.md` |
| intaked | decomposed | brigadier writes decomposition | brigadier | `swarm/wiki/proposals/<task-id>-decomposition.md` |
| decomposed | dispatched | first Task() invoked | brigadier | log line in `swarm/logs/<cycle-id>.md` |
| dispatched | integrated | all returns received | brigadier | `artefacts/` populated; dissents preserved |
| integrated | gated | brigadier writes AWAITING-APPROVAL | brigadier | `swarm/gates/AWAITING-APPROVAL-<task-id>-<slug>.md` |
| gated | approved | HITL ack parsed | HITL | `swarm/gates/<task-id>-ack.md` appended |
| gated | rejected | HITL rejects | HITL | `swarm/gates/<task-id>-rejection.md` |
| rejected | returned | brigadier composes return note | brigadier | `tasks/<task-id>/decisions/<ts>-returned.md` |
| approved | compounded | brigadier compound-step | brigadier | `agents/<expert>/strategies.md` and/or `meta/agent-improvements/` |
| compounded | archived | brigadier writes cycle-log | brigadier | `decisions/<ts>-archived.md`; log.md entry |

**Acceptance predicates** (filesystem-testable):
- `intaked`: `tasks/<task-id>/open-questions.md` exists; `alpha_state: intaked`
- `decomposed`: `proposals/<task-id>-decomposition.md` with `decomposition:` ≥1 cell
- `dispatched`: ≥1 line `Task(<expert>-<mode>)` for this task-id in `swarm/logs/<cycle-id>.md`
- `integrated`: every decomposition cell has artefact in `artefacts/`
- `gated`: `AWAITING-APPROVAL-<task-id>-*.md` with 4-response template
- `approved`: `<task-id>-ack.md` with `acked: true`
- `compounded`: marker `<ts>-compounded.md` with `task_id: <task-id>`; zero-or-more new strategies entries
- `archived`: `swarm/logs/<cycle-id>/cycle-log.md` exists AND log.md has `task-archived | <task-id>`

```
   submitted ──┬─► intaked ──► decomposed ──► dispatched ──► integrated ──► gated
               │                                                                │
               └─► refused                                                      ├─► approved ──► compounded ──► archived
                                                                                │
                                                                                └─► rejected ──► returned
```

## α-2 Artefact

**States:** `drafted | reviewed | revised | accepted | referenced | superseded | retired | tombstoned` (8 terminal states; spec extends master synthesis with `tombstoned`).

**Transitions** (highlights):

| from | to | trigger | mover |
|---|---|---|---|
| (none) | drafted | cell writes draft | cell (expert-direct drafts/ only) |
| drafted | reviewed | critic returns Conformance Checklist | integrator or critic-mode cell |
| reviewed | revised | producer/integrator edits | producer or integrator |
| revised ↔ reviewed | re-critique loop | critic-mode cell |
| reviewed | accepted | brigadier passes §5.5.5 gate | brigadier |
| accepted | referenced | another accepted artefact consumes this | brigadier |
| accepted | superseded | newer accepted supersedes | brigadier |
| accepted/superseded | retired | EOL identification | brigadier (after meta-agent draft) |
| any (non-drafted) | tombstoned | invalidated OR Ruslan-attested withdrawal | brigadier (via gate-file-ack for Ruslan path) |

**Forbidden:** `drafted → tombstoned` (unpromoted drafts are simply deleted; no archive/tombstone).

**Acceptance predicates** — see spec §5.3 (lines 2047–2056 of `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`).

```
   (none) ──► drafted ──► reviewed ⇄ revised
                            │
                            ▼
                         accepted ──► referenced
                            │
                            ├──► superseded ──► retired
                            │
                            └──► tombstoned (invalidated/withdrawn)
```

## α-3 Strategies-Rule (4 states, FPF-canonical)

| FPF state | Spec alias | Definition |
|---|---|---|
| proposed | candidate | 4-part DRR submitted |
| active | learning | ≥1 successful use; under golden-set eval |
| validated | active | ✓/✗ ≥ 3:1 over ≥10 uses; live skill registry |
| tombstoned | tombstoned | ratio <1:1 cumulative OR Ruslan-retire OR incident OR superseded |

**Canonical = FPF names.** Wiki, /lint, /build-graph all use FPF names.

**Transitions:**

| from | to | trigger | mover |
|---|---|---|---|
| (none) | proposed | brigadier compound writes DRR | brigadier |
| proposed | active | first successful cell-use | brigadier (records in usage/<slug>.jsonl) |
| active | validated | golden-set ≥3 + ≥10 uses + ✓/✗ ≥3:1 (D11) | brigadier (after meta-agent audit-via-task) |
| validated | active (demoted) | ratio drops to 1:1 ≤ r < 3:1 over rolling 10 | meta-agent-via-task → brigadier writes |
| any | tombstoned | <1:1 cumulative OR Ruslan retire OR incident OR superseded | brigadier |

```
   (none) ──► proposed ──► active ⇄ validated
                              │         │
                              └────► tombstoned ◄────┘
```

## α-4 Cycle

**States:** `opened | running | integrating | gated | compounded | closed | tombstoned`.

**Spec alias map:** open→opened; mid-cycle→running+integrating; closing→gated+compounded; closed→closed.

**Transitions:** see spec §5.5 (lines 2201–2209). Key: α-4 `closed` count is the authoritative metric for Q8 Layer-9 trigger #1 (≥50 closed cycles).

**Acceptance predicates** — `closed`: `swarm/logs/<cycle-id>/cycle-log.md` exists with frontmatter `summary:` (≥1 line) and `open_questions:` (≥1 line); `closed_cycles_count` in `meta/health.md` incremented.

```
   opened ──► running ──► integrating ──► gated ──► compounded ──► closed
                                                                     │
                                                                     └──► tombstoned (rare)
```

## α-5 Direction (human-owned, Phase A lightweight)

**States:** `hypothesized | under-validation | validated | activated | scaled | plateaued | invalidated | dropped | archived`. Pivot branches: `under-validation → hypothesized`; `invalidated → hypothesized`.

**Movers:** human/strategic-management for hypothesized+activated; brigadier tracks state; experts contribute evidence artefacts. **AI agents do NOT move α-5** beyond tracking.

**Phase A vs B:** Phase A = state-enum-only, flat list in this α-5 section; no machine validator required. Phase B defers NQD-CAL+E/E-LOG+BLP formalization per FPF Part 10.6.

**HITL discipline:** any α-5 state change is HITL-only (AWAITING-APPROVAL file).

```
   hypothesized ──► under-validation ──► validated ──► activated ──► scaled
        ▲                  │                                            │
        └──── pivot ───────┘                                            ▼
                                                                    plateaued
                                                                        │
                                                            invalidated ┴── dropped ──► archived
```

## §5.7 — Cross-alpha integrations summary matrix

| | α-1 Task | α-2 Artefact | α-3 Strategies | α-4 Cycle | α-5 Direction |
|---|---|---|---|---|---|
| α-1 | self | creates instances dispatched→integrated | emits at compounded | inhabits α-4 (1:1) | task may target direction (info) |
| α-2 | created during α-1 | self | strategies cite α-2 artefacts | exists inside α-4 | direction evidence is α-2 |
| α-3 | emitted at α-1 compounded | strategies cite α-2 | self | activation/retirement triggered by cycle aggregates | strategies may inform direction |
| α-4 | contains 1× α-1 | hosts α-2 from running→compounded | drives α-3 validated | self | cycle counts feed direction validation |
| α-5 | n/a (HITL) | direction evidence is α-2 | n/a | spans multiple α-4 | self |

## Movers reference

- **brigadier** — sole writer for α-1, α-2 (post-drafted), α-3, α-4 transitions to wiki canonical.
- **HITL (Ruslan)** — sole mover for α-5 transitions; sole authoriser for `gated → approved/rejected` (α-1) and α-2 `tombstoned` via attested withdrawal.
- **expert cells** — write α-2 `drafted` only (in `swarm/wiki/drafts/`); return critic/integrator/optimizer/scalability outputs that drive α-2 `drafted → reviewed → revised → accepted` via brigadier integration.
- **meta-agent (via Task)** — composes α-3 demotion proposals and weekly health summaries; never writes canonical wiki directly.
