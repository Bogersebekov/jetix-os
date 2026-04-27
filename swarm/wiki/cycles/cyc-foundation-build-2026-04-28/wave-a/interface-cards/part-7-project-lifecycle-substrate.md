---
title: "Interface Card — Part 7: Project Lifecycle Substrate"
part: 7
slug: project-lifecycle-substrate
phase: A-2
cycle: cyc-foundation-build-2026-04-28
expert: engineering-expert
mode: integrator
date: 2026-04-27
originating_expert: mgmt-expert
critic_flags_applied:
  - "FLAG-MAJOR resolved: IP-5 state-naming corrected (activated, under-review) per FPF §5.5 + A-1-critic-gate.md §6 item 1"
F: F4
ClaimScope: "Holds for single-owner professional knowledge-worker system; D26 Team 50-100 scaling constraint applies (schema must be team-ready without architectural redesign)"
R: "Refuted if Wave C interface card produces alpha states that are not past-participle or whitelisted under-X forms; accepted if state machine validates against IP-5 in Wave C review"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
---

# Interface Card — Part 7: Project Lifecycle Substrate

**Scope sentence.** The typed scaffolding for creating, staging, tracking,
reviewing, and archiving work items (projects, tasks, cycles) — from brief to
closure — with stage-gate acceptance predicates, appetite declarations, scope
records, and resource tracking per project type.

**U.System.** State-machine owner: manages transitions `drafted` → `staged` →
`activated` → `under-review` → `closed` / `archived`.

> IP-5 correction applied [A-1-critic-gate.md §6 item 1]: `active` → `activated`
> (past-participle, FPF §5.5); `review` → `under-review` (whitelisted under-X
> exception per FPF §5.5a — semantic justification: under-review = active review
> window with decision pending; `reviewed` would imply review concluded).
> Whitelist entry to be recorded in `decisions/policy/past-participle-exceptions.md`
> during Wave C materialisation.

---

## A. Inputs

- `projects/<slug>/brief.md` :: project-create-event (owner or agent draft)
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §1 UC-D.1-D.2` :: constitutional scope shape
- `.claude/config/project-types.yaml` :: typed project schema (consulting / research / product / bets)
- `swarm/wiki/_templates/project-*/` :: per-type stub files (4 template trees)
- Stage-gate acceptance signals from Part 6 (Governance, Provenance & Human Gate) :: gate-ack events

## B. Outputs

- `projects/<slug>/` directory tree with stage-gate artefacts per accepted type
- Stage-gate evaluation results (pass / fail / pending) per transition
- Archive records for closed/archived projects with provenance preserved
- Resource-budget summary per project (time / appetite / scope delta) → consumed by Part 8 (Health Monitoring) as health signals
- Per-project scope-record files consumed by Part 9 (Owner Interaction Scaffold) for weekly review

## C. Side-effects

- git commit `[project] staged: <slug> (brief accepted, appetite declared)` per Part 1
- git commit `[project] activated: <slug> (stage-gate <N> acked by owner)` per Part 1
- Append to `swarm/wiki/log.md` on every state transition (append-only, Part 5 compound audit trail)
- Write accepted predicates to project artefact frontmatter (`stage: activated`, `acceptance_predicate:` field)
- Feed project status to `shared/state/kanban.json` (WIP-limit enforcement per FUNDAMENTAL §3.2.6)

## D. Dependencies (typed per FPF A.14)

- `methodologically-uses` **Part 6** — per-project stage gates reuse Part 6's gate mechanism (the gate mechanism is owned by Part 6; Part 7 invokes it per-project). [candidate-parts-merged.md §2 Part 7; A-1-critic-gate.md §2 Part 7 A.14]
- `creates` **Part 1** — all project artefacts are committed files (FPF IP-3; D25)
- `PhaseOf` **Part 5** — project retrospective DRR input feeds compound learning at cycle close

## E. Boundary (FPF A.6.B L/A/D/E)

**Laws (invariants that MUST hold):**
- Every project state transition must be a past-participle or whitelisted under-X form per FPF §5.5 IP-5
- Every stage-gate transition requires a committed gate artefact (AWAITING-APPROVAL or equivalent) per Part 6 discipline; no silent promotion [FUNDAMENTAL §4.5]
- Appetite declaration is mandatory at `staged` state; projects without declared appetite cannot transition to `activated` [mgmt-expert.md §1 Shape Up discipline; FUNDAMENTAL §4.4]
- D26 compliance: all schema fields must be team-addressable (single named accountable per deliverable, not "the team owns it") [D26; mgmt-expert.md §3]

**Admissibility (acceptance criteria for inputs):**
- Project brief accepted only if it declares: type (consulting / research / product / bets), appetite, scope boundary, and at least one Hamel-binary acceptance predicate
- Stage-gate evaluation inputs must include the corresponding Foundation acceptance predicate; predicate-free evaluations are rejected [FUNDAMENTAL §4.5; CYCLE-2 §G.1 OPP-04]

**Deontics (obligations toward consumers):**
- MUST surface project status to Part 8 (Health Monitoring) at minimum weekly cadence (cycle completion rate SLI: 70-90% target per FUNDAMENTAL §3.3)
- MUST append every state transition to `swarm/wiki/log.md` before returning (append-only per FUNDAMENTAL §2.1 cross-cutting substrate)
- MUST NOT auto-advance project state without human ack (FUNDAMENTAL §6.1; Part 6 gate required)

**Effects (measurable outcomes):**
- Project scaffold exists in `projects/<slug>/` within one work session of brief acceptance
- Stage-gate acceptance predicate evaluated and committed within 24h of owner ack submission (L2 SLA per FUNDAMENTAL §4.2)
- Archive record with full provenance trail committed on `closed` or `archived` transition

## F. Anti-scope

- Part 7 does NOT author strategic decisions — project scope is whatever the owner declares in the brief; agents can draft scopes but owner acks (FUNDAMENTAL §6.1, §6.2)
- Part 7 does NOT own the gate mechanism — Part 6 (Governance) owns AWAITING-APPROVAL gate logic; Part 7 calls the gate per-project [A-1-critic-gate.md §2 Part 7]
- Part 7 does NOT track contacts or external relationships (Part 10 — External Touchpoints)
- Part 7 does NOT run health monitoring — it produces health-signal inputs for Part 8; Part 8 evaluates them
- Part 7 does NOT encode RUSLAN-LAYER project types (4 templates are AUDIT documentation; the generic schema is Foundation; specific ICP-content per project template is RUSLAN-LAYER) [D27; candidate-parts-merged.md §2 Part 7 Ruslan-creep check]
- Part 7 does NOT substitute for founder resource-allocation decisions (D.2 resource budgeting surfaces resource data; owner decides allocation)

## G. F-G-R Tagging

| Artefact emitted | F | G (ClaimScope) | R |
|---|---|---|---|
| Project brief draft | F2 | Single project scope | low — draft, owner-unacked |
| Staged project artefact (appetite declared) | F4 | This project's lifecycle only | medium — owner-acked appetite |
| Activated project artefact (gate passed) | F5 | This project, current cycle | high — human gate passed per Part 6 |
| Archive record | F5 | Permanent audit trail | high — immutable after archive commit |
| Stage-gate evaluation result | F4 | This project stage | medium — based on declared predicate |

## H. Originating Expert + Critic Flags

**Originating expert.** Mgmt-expert (Part 3: Project Lifecycle Substrate). [candidate-parts-merged.md §1 §2 Part 7]

**Critic flags applied:**
- FLAG-MAJOR (IP-5 state-naming): `active` → `activated`; `review` → `under-review` (whitelisted). Correction applied in scope sentence and state machine above. [A-1-critic-gate.md §6 item 1; FPF §5.5 IP-5]

**D26 constraint (wave A surface).** The project schema must be designed for 50-100 humans from the start — not solo-founder-specific. Concretely: single named accountable per deliverable; escalation path declared per project type; no hardcoded "Ruslan does X" in schema. Wave C materialisation must include a D26 compliance check per project type template. [D26; mgmt-expert.md §3]

**Wave C bullets (preview).**
- Define canonical Foundation-level project schema YAML (acceptance-predicate fields, appetite, state machine, accountable field) — M effort; engineering-expert integrator + mgmt-expert integrator
- Canonicalise IP-5 past-participle exception whitelist (`decisions/policy/past-participle-exceptions.md`) — S effort; philosophy-expert critic
- Wire project state transitions to Part 6 gate mechanism (AWAITING-APPROVAL per transition) — M effort; engineering-expert integrator
- Validate D26 compliance of all 4 project type templates — S effort; mgmt-expert critic
