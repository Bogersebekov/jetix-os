---
title: "Interface Card — Part 4: Role Taxonomy & Coordination Protocol"
part_number: 4
part_slug: role-taxonomy-coordination-protocol
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
critic_status: CLEAN
originating_experts: [engineering-expert, systems-expert, mgmt-expert, investor-expert]
FUNDAMENTAL_UC: [E.1, E.2, E.3]
FPF_anchors: [IP-1, IP-2, IP-6, IP-8, A.6.B, A.13]
D_lock_anchors: [FUNDAMENTAL §3.2.4, FUNDAMENTAL §4.6, D26]
U_classification: "Dual: role manifests = U.Episteme; coordination protocol = U.System"
F: F4
ClaimScope: "Holds for any multi-agent system using hub-and-spoke topology with role-based communication; RUSLAN-LAYER executor-binding.yaml provides specific agent bindings"
R:
  refuted_if: "Any Foundation Part 4 interface card names a specific agent executor (e.g., a model name or instance ID) as a constituent, violating IP-1"
  accepted_if: "All coordination protocol interfaces are expressed as role-method signatures; executor bindings live exclusively in RUSLAN-LAYER executor-binding.yaml; F.6 onboarding block is mandatory in executor-binding.yaml"
sources:
  - "candidate-parts-merged.md §2 Part 4"
  - "A-1-critic-gate.md §2 Part 4 (verdict: CLEAN)"
  - "levenchuk-shsm-fpf.md §4 P1 (IP-1), §4 P6 (L/A/D/E), §4 P7 (F.6)"
  - "FUNDAMENTAL §3.2.4, §4.6, §6.1"
  - "design/JETIX-FPF.md §5.1 IP-1, §5.6 IP-6, §5.8 IP-8, §4.3 A.6.B, §2.1a A.13"
  - "AUDIT-CURRENT-STATE-2026-04-27.md §4 (agents/ 20 dirs, comms/mailboxes, swarm/lib/shared-protocols.md)"
---

# Interface Card — Part 4: Role Taxonomy & Coordination Protocol

## A. Inputs

| Source | Data shape | Event trigger |
|---|---|---|
| Role-manifest files (U.Episteme) | `role.md` per role — 5-block structure per IP-6: identity / ontological-positioning / method / production-dependencies / evolution | Written once at Foundation build; updated only via governance gate (Part 6) |
| Executor-binding registry (RUSLAN-LAYER) | `executor-binding.yaml` per role-instance binding — includes M1-M6 F.6 onboarding block mandatory | Updated when executor changes (model swap, agent replacement, role reassignment) |
| Inbound message from any part | `message.schema.json` — `acting_as:` field mandatory [FUNDAMENTAL §3.2.4]; `task_id`, `mode:`, `inputs[]`, `expected_return_path` | Per-dispatch event |
| Escalation signal from any part | Structured escalation packet: `trigger`, `evidence`, `routing` | When any part reaches a J-level boundary it cannot self-resolve [A.13 Agency-CHR] |

## B. Outputs

| Consumer | Data shape | Event published |
|---|---|---|
| Any executing role-instance | Dispatch packet conforming to message schema + routed to correct mailbox `comms/mailboxes/<role>.jsonl` | `task-dispatched-event` |
| Part 6 (Governance) | Escalation packet when J-Strategic or J-Approve boundary hit; routing table updates require governance gate | `escalation-submitted-event` |
| Part 5 (Compound Learning) | DRR coordination patterns from cycle retrospective — structured extraction, not authored by agents | `compound-phase-extract-event` |
| Part 1 (System State Persistence) | Committed role-manifest artifacts, executor-binding.yaml, routing table YAML, message schema YAML | `artifact-committed-event` |

## C. Side-effects

- Mailbox write: `comms/mailboxes/<role>.jsonl` — appended per dispatch [D25 Company-as-Code; IP-3]
- Routing table: `swarm/lib/shared-protocols.md` runtime contract + declarative routing YAML (Wave C materialisation gap — currently embedded in system prompts, not declarative) [candidate-parts-merged.md §2 Part 4]
- Executor-binding registry: RUSLAN-LAYER `executor-binding.yaml` — NOT a Foundation artifact; binding is RUSLAN-LAYER parameterisation over the Foundation role archetype [FPF §5.1 IP-1; levenchuk-shsm-fpf.md §4 P1]
- Audit log entry per escalation routed [Part 6 interface]

## D. Dependencies (typed per FPF A.14)

| Edge | Type | Rationale |
|---|---|---|
| Part 4 → Part 1 | `creates` | Every role-manifest, executor-binding.yaml, message schema commit routes through Part 1 git substrate [FPF §5.3 IP-3] |
| Part 4 → Part 6 | `methodologically-uses` | Governance gate owns compliance audit on role-manifests (IP-1 quarterly audit); Part 4 applies governance protocol, does not own it [A-1-critic-gate.md §2 Part 4 A.14 note] |
| Part 4 → Part 5 | `creates` | Coordination cycle events feed DRR extraction in compound phase [candidate-parts-merged.md §2 Part 5 E.2] |

## E. Boundary — L/A/D/E discipline [FPF §4.3 A.6.B; levenchuk-shsm-fpf.md §4 P6]

**Laws (invariants that MUST hold):**
- IP-1 strict: role manifests (U.Episteme archetypes) are NEVER the same artifact as executor bindings (RUSLAN-LAYER). No executor name appears in any Foundation Part 4 artifact [FPF §5.1 IP-1].
- `acting_as:` field is mandatory in every message; absent = message rejected at coordination gate [FUNDAMENTAL §3.2.4].
- J-level decision matrix is architecturally encoded, not behaviorally assumed: J-Auto / J-Approve / J-Strategic per role per decision-class [A.13 Agency-CHR; FPF §2.1a].
- All novel or uncategorized actions escalate; no "creative interpretation" [FUNDAMENTAL §6.1 last bullet; FUNDAMENTAL §4.6].

**Admissibility (acceptance criteria for inputs):**
- A role-manifest is accepted into Foundation only after IP-6 5-block completeness check (all 5 blocks populated) [FPF §5.6 IP-6].
- An executor-binding.yaml is activated only after F.6 six-step onboarding (M1-M6 all populated, M3 Qualify reviewer pass confirmed) [FPF §5.8 IP-8; levenchuk-shsm-fpf.md §4 P7].
- An inbound message is accepted only if `acting_as:` matches a registered role-manifest name.

**Deontics (obligations of this part toward consumers):**
- Part 4 MUST maintain a canonical role-manifest registry (declarative YAML, not embedded in system prompts) — Wave C materialisation task [candidate-parts-merged.md §2 Part 4].
- Part 4 MUST route escalations within one cycle turn; no silent absorption of escalation signals.
- Part 4 MUST expose a routing table legible to all parts without requiring reading any individual agent system prompt.

**Effects (measurable outcomes):**
- Successful dispatch: structured packet delivered to target mailbox, verifiable via `comms/mailboxes/<role>.jsonl` append.
- Cycle completion: all dispatched tasks returned with structured packets; open task count = 0 at cycle close.
- Role-manifest health: IP-1 compliance rate = 100% (no executor names in Foundation role definitions) — audited quarterly by Part 6 / Part 8 [FUNDAMENTAL §3.2.5].

## F. Anti-scope

- **Does NOT name specific executor instances** as Foundation constituents. Specific bindings (which model, which agent file) are RUSLAN-LAYER executor-binding.yaml [FPF §5.1 IP-1; levenchuk-shsm-fpf.md §8 AP-L1].
- **Does NOT strategize** — routing and dispatch are procedural; method selection is HITL-only [FUNDAMENTAL §6.1; FPF §5.10.4].
- **Does NOT own F-G-R compliance enforcement** — that is Part 6's function; Part 4 embeds F-G-R tags on dispatched artifacts but does not audit compliance [A-1-critic-gate.md §2 Part 4 B.3 note].
- **Does NOT own project lifecycle state machines** — that is Part 7; Part 4 dispatches tasks within cycles, not projects.
- **Does NOT allow agents to negotiate contradictions autonomously** — all unresolved inter-agent contradictions escalate to human gate [FUNDAMENTAL §6.1; A.13 Agency-CHR].

## G. F-G-R tagging [FPF §4.2 B.3; levenchuk-shsm-fpf.md §4 P5]

| Artifact | F | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Role-manifest (role.md per role) | F5 — codified rule in Foundation | Any multi-agent system using hub-and-spoke + IP-1 discipline | R-medium until F.6 M6 promotion threshold met; R-high after |
| Executor-binding.yaml | F4 — operational convention (RUSLAN-LAYER) | Specific to one deployed instance; bridge required for multi-owner context (F.9) | R-medium; updated per M3 Qualify re-run on executor change |
| Message schema YAML | F5 — codified rule; `acting_as:` mandatory per FUNDAMENTAL §3.2.4 | Any Jetix instance | R-high (constitutional; not softcoded) |
| Dispatch packet | F3 — multi-source informal (task brief + mode prefix + input paths) | Single cycle turn | R-low to R-medium; reliability grows with cycle history in strategies.md |
| Routing table YAML (Wave C) | F5 target (currently F2 — embedded in system prompts) | Full Foundation scope | R-low until materialised as declarative YAML artifact |

## H. Originating expert + critic flags

- **Originating experts:** Engineering-expert (Part 4: Agent Coordination), systems-expert (Part 2: Agent Coordination & Communication Layer), mgmt-expert (Part 4: Agent Swarm Governance Layer), investor-expert (Part 3: Agent Coordination Infrastructure) — strongest convergence in candidate list (4/5 experts independently proposed) [candidate-parts-merged.md §2 Part 4].
- **A-1 critic verdict: CLEAN** [A-1-critic-gate.md §2 Part 4]. No required edits.
- **Note for Wave C:** Primary materialisation gap is the routing table as declarative YAML artifact (not embedded in system prompts). Wave C task: extract routing logic from system prompt files into `swarm/lib/routing-table.yaml` with typed role entries + J-level authority declarations per role [candidate-parts-merged.md §2 Part 4 AUDIT artefact mapping].
- **AUDIT existing artefacts to reuse:** `.claude/agents/brigadier.md` + 5 ROY expert `.md` files; `agents/*/strategies.md` (8 files); `comms/mailboxes/*.jsonl` (13 channels); `shared/schemas/message.schema.json`; `swarm/lib/shared-protocols.md`; hook layer (mode-prefix.sh, role-matrix.sh, verify-packet.sh) [AUDIT §4].
