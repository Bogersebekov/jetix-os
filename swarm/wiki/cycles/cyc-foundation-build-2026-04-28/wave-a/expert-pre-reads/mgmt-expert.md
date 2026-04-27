---
title: Mgmt-expert pre-read — Foundation main parts (integrator mode)
date: 2026-04-27
phase: A-0
expert: mgmt-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
sources:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
provenance_inline: true
produced_by: mgmt-expert
---

# Mgmt-expert Pre-read — Foundation Main Parts

## §1 Read summary (~600 words)

Through the PM / management-philosophy lens, FUNDAMENTAL describes a system
built for sustained, disciplined output by a professional knowledge worker
who delegates mechanical execution to an agent swarm while retaining
strategic authority. The management-relevant structure that emerges from
reading §1 (categories C, D, E, I, J), §2 (потоки), §3 (health indicators),
and §4 (automation vs manual) is dense. Key patterns follow.

**Cagan empowered-team principle — missions over tasks.**
FUNDAMENTAL explicitly preserves the architect-orbit: "AI не strategize,
владелец = strategize" [FUNDAMENTAL §4.3]. This maps directly to Cagan's
empowered-team discipline: the owner is the missionary who holds the
outcome; agents are subordinate executors who hold the "how". Foundation
must encode this distinction structurally — not as a convention but as an
enforced role-binding (`acting_as` field per [FUNDAMENTAL §3.2.4], Левенчук
IP-1 Role ≠ Executor). Any Foundation part that allows an agent to silently
absorb strategic or architectural authority violates this principle.

**Torres CDH (Continuous Discovery Habits) — opportunity layer.**
UC-C.2 [FUNDAMENTAL §1] requires skill acquisition under strategic
direction, with a 5-stage pipeline: discover sources → ingest → build wiki
sub-area → train agent skills → extract templates [FUNDAMENTAL §2.8]. This
is the CDH opportunity-solution loop applied to system learning: the owner
identifies a capability gap (the "opportunity"), the system ingests
relevant materials (the "solution space"), and the skill crystallises into
a reusable artefact. Foundation needs an explicit **Skill Acquisition
Substrate** to house this pipeline. Currently no dedicated Foundation-level
artefact exists for it [AUDIT §5].

**Grove HOM leverage — attention as ultimate constraint.**
FUNDAMENTAL §2 names "WIP limits + bottleneck awareness (Anderson Kanban +
Goldratt TOC)" as a cross-cutting substrate for all flows [FUNDAMENTAL §2
intro]. The coordinator attention budget cap is an explicit health indicator
(60-80% of cap = healthy; >90% = expand or delegate) [FUNDAMENTAL §3.2.6].
Grove's output-management insight applies directly: the owner's attention
is the bottleneck; Foundation must make that bottleneck visible and
protected. Currently `shared/state/kanban.json` exists [AUDIT §4.4] but
there is no canonical Foundation-level flow that enforces attention-cap
discipline across all project and agent operations simultaneously.

**Laloux Teal — self-management with wholeness.**
UC-C.1 [FUNDAMENTAL §1] describes a compound engineering cycle
(Plan/Work/Review/Compound at 40/10/40/10) where the system improves its
own methodologies each cycle. This is a Teal-adjacent pattern: the system
has an evolutionary purpose (compound leverage) and self-manages its
improvement cadence without centralised top-down direction for each cycle.
The DRR ledger (Decision/Reasoning/Result/Review, append-only per
[FUNDAMENTAL §2.2, §2.4]) is the mechanism. Foundation must encode this
as a first-class cadence substrate — not buried inside individual agent
strategies.

**Drucker effective executive — contribution over effort.**
UC-D.2 [FUNDAMENTAL §1] requires resource budgeting across time, money,
energy, attention, and credits. FUNDAMENTAL §3.8 names deep work hours (≥15h/week)
and leverage ratio (value-creating time / total working time) as health KPIs
[FUNDAMENTAL §3.8.5, §3.8.6]. Drucker's contribution framing demands that
Foundation surface what is being *produced*, not merely what effort is being
expended. The current `shared/state/` has `priorities.json` and
`system-health.json` [AUDIT §4.4] but no unified contribution-tracking
substrate.

**Shape Up (Singer) — fixed-time variable-scope discipline.**
FUNDAMENTAL §4.4 [FUNDAMENTAL §4.4] describes "boundary-flexible" tasks
that shift between manual and AI-augmented as confidence accumulates. Shape
Up's appetite framing (fixed time, hammered scope) is the natural
implementation model for this. Every project cycle should carry an explicit
appetite; scope hammering is the operational response to overrun.
Currently project skills exist (`project-bootstrap`, `project-review`, etc.
[AUDIT §5]) but the appetite / scope-hammer discipline is not enforced at
Foundation level.

**Daily / weekly / monthly / quarterly cadence (Plan-Work-Review-Compound).**
FUNDAMENTAL §2 documents all four cadences explicitly [FUNDAMENTAL §2.2
compound / §2.5 health checkups / §2.6 daily ops]. The 40/10/40/10
ratio is a named constitutional value. Foundation must encode each cadence
as a distinct operational layer with named artefacts (Daily Log per UC-J.1,
weekly review per UC-J.3, monthly Operations Review per §3.3.3, quarterly
architectural review per §3.5.4) [FUNDAMENTAL §3.3, §3.5].

**Stage gates and 3-tier approval SLA.**
FUNDAMENTAL §4.2 (AI-augmented) and §4.3 (human-only) name the approval
taxonomy [FUNDAMENTAL §4.2, §4.3]. UC-H.5 requires quality gates
(stage-gated approval) as a Foundation principle [FUNDAMENTAL §1 UC-H.5].
Cycle-2 implementation demonstrated this pattern in the swarm: OPP-04
added `cell_acceptance_predicate` as a required YAML field enforced by
`/lint` check #13 [CYCLE-2 §G.1]. Foundation must generalise this into a
reusable governance substrate.

**WIP limits + bottleneck awareness.**
Anderson Kanban WIP limits and Goldratt TOC are named as cross-cutting
substrates [FUNDAMENTAL §2 intro]. The concrete health indicator is:
coordinator active task count sustained 60-80% of cap is healthy; >90% for
>24h triggers capacity expansion [FUNDAMENTAL §3.2.6]. AUDIT confirms
`kanban.json` exists [AUDIT §4.4] but is not enforced at Foundation level
across agents.

**Cycle pattern — Compound Engineering.**
FUNDAMENTAL §3.3 enumerates cycle health indicators: ratio drift (40/10/40/10
±10pp), cycle completion rate (70-90%), review depth (≥200 words + ≥1
explicit decision per monthly review), compound application rate (≥60% of
high-confidence insights integrated within 2 cycles) [FUNDAMENTAL §3.3.1-§3.3.4].
D26 Team 50-100 [D26] confirms this pattern must survive to enterprise
scale — the cycle cadence is not a solo-founder quirk; it is the operating
model of the company at scale.

---

## §2 Candidate "main parts" (3-5)

### Part 1 — Cycle Operations Substrate

**Scope sentence.** The bounded execution unit that encodes
Plan/Work/Review/Compound at 40/10/40/10, with intake, decomposition,
dispatch, integration, gate, compound, and archive as typed stages with
named artefacts and acceptance predicates per stage.

**Why it's a part.** Without a canonical cycle definition, every agent
and every project invents its own cadence. The cycle is the primary unit
of output management (Grove HOM) and self-improvement (Compound Engineering).
It is not a project artefact; it is the operating rhythm that makes all
other parts coherent. FUNDAMENTAL names it as the cross-cutting structural
discipline in §2 [FUNDAMENTAL §2 intro] and §3.3 [FUNDAMENTAL §3.3]. The
Cycle-2 implementation report demonstrates the cycle pattern in practice
[CYCLE-2 §G.1-§G.5].

**FUNDAMENTAL UC mapping.** UC-C.1 (self-improvement / compound engineering)
+ UC-H.5 (quality gates / stage-gated approval) + UC-D.1 (project lifecycle
management) — the cycle is the unifying execution primitive across all three.

**AUDIT artefact mapping.** `swarm/wiki/cycles/cyc-*` directories (existing
cycle artefact pattern) [AUDIT §3.3]; `swarm/logs/`, `swarm/awaiting-approval/`
[AUDIT §1.1]; `swarm/evals/` eval harness (OPP-01, cycle-2) [CYCLE-2 §G.2];
`.claude/hooks/` hook layer (OPP-02) [CYCLE-2 §G.3]. The skeleton exists;
the canonical definition of "what a cycle is" at Foundation level does not.

**Cross-cutting?** Yes — every other main part emits or consumes cycle
artefacts. The cycle substrate is the coordination backbone.

---

### Part 2 — Operational Rhythm Layer

**Scope sentence.** The daily/weekly/monthly/quarterly cadence infrastructure:
Daily Log creation and EOD ritual (UC-J.1), draft capture and promotion
workflow (UC-J.2), weekly draft review (UC-J.3), monthly Operations Review,
and quarterly architectural review — each with named artefacts, completion
KPIs, and WIP-limit enforcement.

**Why it's a part.** Operational rhythm is distinct from the Cycle
Operations Substrate (Part 1): Part 1 is the agent-swarm execution unit;
Part 2 is the owner-system daily co-work rhythm. FUNDAMENTAL devotes an
entire flow section to it (§2.6 daily ops, §2.5 health checkups)
[FUNDAMENTAL §2.5, §2.6] and names 5 daily-ops health indicators
[FUNDAMENTAL §3.5.1-§3.5.5]. Without this layer, the owner has no
structured way to interact with the system daily — the swarm operates but
the human-system interface has no cadence scaffold.

Shape Up's appetite discipline plugs in here: each day's planning page
declares the day's appetite; weekly review is the scope-hammer moment;
monthly review is the strategy-alignment check. Grove's high-leverage
activities (quarterly architectural review, monthly methodology synthesis)
are the high-leverage anchors of this layer.

**FUNDAMENTAL UC mapping.** UC-J.1 (daily working page) + UC-J.2 (draft
→ promote → archive) + UC-J.3 (weekly draft review) + UC-I.1 (periodic
health checkups weekly/monthly/yearly) + UC-I.2 (owner self-reflection
prompts).

**AUDIT artefact mapping.** `daily-log/` directory (exists but minimally
populated, 1 file) [AUDIT §1.1]; `shared/state/kanban.json` [AUDIT §4.4];
`skills/plan-day`, `skills/close-day` [AUDIT §5]; `decisions/weekly/`
(referenced in FUNDAMENTAL but not yet present in AUDIT). The skills exist;
the Foundation-level schema for daily log artefacts and weekly review
cadence does not.

**Cross-cutting?** Yes — this layer consumes outputs from all other parts
(agent drafts, project status, KB freshness) and produces the owner's
daily and weekly decision record.

---

### Part 3 — Project Lifecycle Substrate

**Scope sentence.** The typed scaffolding for creating, staging, tracking,
reviewing, and archiving projects — from brief to closure — with
stage-gate acceptance predicates, appetite declarations, scope
records, and resource tracking per project.

**Why it's a part.** FUNDAMENTAL UC-D.1 requires unified project lifecycle
management across all project types [FUNDAMENTAL §1 UC-D.1]. This is
currently partially implemented through `project-bootstrap`, `project-review`,
`project-archive`, `project-de-morph`, and `project-promote` skills
[AUDIT §5.1] and the KM Materialization MVP (cycle 4). However, these
skills are execution tools; the underlying Foundation-level schema for
"what a project is" (brief → milestones → tasks → status → closure) with
acceptance predicates enforced per stage gate is not yet a canonical
Foundation artefact. Cagan's vision-strategy-tactics three-layer split
applies here: projects must be placed at the right layer (tactical milestone
vs strategic direction) to prevent layer mixing [FUNDAMENTAL §2.2 Phase-3
BA-cycle reference].

D26 [D26] mandates that the project lifecycle must survive to 50-100 humans:
the schema must be team-ready, not solo-founder-specific. The existing
4-type template system (`consulting / research / product / bets`) provides
a start but lacks the Foundation-level stage-gate enforcement layer.

**FUNDAMENTAL UC mapping.** UC-D.1 (project lifecycle management) +
UC-D.2 (resource budgeting and monitoring) + UC-H.5 (quality gates).

**AUDIT artefact mapping.** `projects/` directory [AUDIT §1.1];
`.claude/config/project-types.yaml` [AUDIT §5]; `swarm/wiki/_templates/project-*/`
[AUDIT §5]; `project-bootstrap / project-review / project-archive / project-de-morph /
project-promote` skills [AUDIT §5.1]. Schema + templates exist; Foundation-level
acceptance-predicate enforcement and stage-gate sequencing are not canonical.

**Cross-cutting?** Partially — project artefacts are consumed by the
Operational Rhythm Layer (weekly review) and the Cycle Operations Substrate
(cycle decomposition). Not fully cross-cutting; primarily a managed entity.

---

### Part 4 — Agent Swarm Governance Layer

**Scope sentence.** The role-binding, communication-discipline, escalation-taxonomy,
WIP-limit, and HITL-gate infrastructure that keeps the agent swarm operating
within Левенчук discipline: acting_as enforcement, mailbox schemas, hub-and-spoke
routing, approval SLA tiers, and the attention-budget cap on the coordinator.

**Why it's a part.** FUNDAMENTAL UC-E.1, UC-E.2, UC-E.3 [FUNDAMENTAL §1]
define multi-agent coordination, agent self-learning, and agent communication
discipline as three distinct requirements. FUNDAMENTAL §2.3 names the
agent communication flow as a typed protocol [FUNDAMENTAL §2.3]. The health
indicators for agent swarm (§3.2.1-§3.2.6) include: mailbox cycle time,
queue depth, escalation rate (healthy 10-25%), Левенчук compliance via
`acting_as` field (target 100%), no-strategy violations (0 per quarter),
and coordinator attention budget (60-80% of cap) [FUNDAMENTAL §3.2].

Without this part as a named Foundation component, the discipline is
convention — enforced by individual agent system prompts but not by a
canonical governance substrate. The cycle-2 hook layer (OPP-02) begins
to materialise this [CYCLE-2 §G.3] but remains log-only. Foundation
must make this enforcement canonical.

D26 [D26] implies the swarm must scale from 1 coordinator + 6 agents today
to a 50-100 human + agent hybrid team: the hub-and-spoke governance
model must survive that scaling without redesign.

**FUNDAMENTAL UC mapping.** UC-E.1 (multi-agent coordination) + UC-E.2
(agent self-learning / strategy refinement) + UC-E.3 (agent communication
discipline) + UC-H.5 (quality gates / approval flow) + §4.6 (boundary
enforcement mechanism) [FUNDAMENTAL §4.6].

**AUDIT artefact mapping.** `comms/mailboxes/*.jsonl` (13 JSONL channels)
[AUDIT §4.3]; `shared/schemas/message.schema.json` [AUDIT §4.5];
`.claude/hooks/` (mode-prefix.sh, role-matrix.sh, verify-packet.sh,
OPP-02) [CYCLE-2 §G.3]; `swarm/lib/shared-protocols.md` (runtime
contract for ROY swarm); `shared/state/kanban.json` [AUDIT §4.4].
The message schema and hook layer exist; the canonical Foundation
governance document (what the swarm governance layer IS, what
invariants it enforces, how it scales) does not exist as a Foundation artefact.

**Cross-cutting?** Yes — this part's invariants (role-binding, escalation
taxonomy, WIP limits) apply to every other part. It is a constitutional
substrate for all agent-swarm interactions.

---

### Part 5 — Operational Health Monitoring Layer

**Scope sentence.** The SLI/SLO/error-budget substrate that makes system
health observable: health indicators per domain (KB, agents, cycles,
self-improvement, daily ops, CRM, resources), alert thresholds,
behaviour-change rules when error budget burns, and periodic
self-preservation integrity checks.

**Why it's a part.** FUNDAMENTAL §3 devotes ~30 SLI/SLO pairs across 8
health domains [FUNDAMENTAL §3.1-§3.8]. UC-I.1 (periodic health checkups),
UC-I.3 (recommendation engine), and UC-I.4 (system self-preservation)
[FUNDAMENTAL §1] are use cases whose implementation requires a canonical
observability substrate. Without this substrate, health is subjective
("it feels good") and issues surface late.

Currently `shared/state/system-health.json` exists [AUDIT §4.4] and reports
"all green" — but there is no canonical mechanism for computing the health
signals or triggering behaviour-change on budget burn. The `/lint` skill
covers 11 KB health checks [AUDIT §5.1] and `company-status` provides a
git-native snapshot [AUDIT §5.1], but these are disconnected tools, not a
unified Foundation-level health layer.

Drucker's time-as-alpha lens demands this part: without visibility into
where owner attention is going (deep work hours, WIP cap utilization,
leverage ratio), Foundation cannot protect the owner's primary resource
[FUNDAMENTAL §3.8.1-§3.8.6].

**FUNDAMENTAL UC mapping.** UC-I.1 (periodic system health checkups) +
UC-I.2 (owner self-reflection prompts) + UC-I.3 (recommendation engine) +
UC-I.4 (system self-preservation and integrity checks) + UC-H.4 (health
monitoring and alerting).

**AUDIT artefact mapping.** `shared/state/system-health.json` [AUDIT §4.4];
`shared/state/metrics/agent-performance.json` [AUDIT §4.4]; `/lint` skill
[AUDIT §5.1]; `/company-status` skill [AUDIT §5.1]; `swarm/evals/` harness
[CYCLE-2 §G.2]. Components exist but are not unified under a canonical
Foundation health schema with declared SLI/SLO values and behaviour-change
rules.

**Cross-cutting?** Yes — health signals are consumed across all layers
(daily planning, weekly review, cycle compound, project gating). This part
is an observability spine for Foundation.

---

## §3 Mgmt pressure points

The following operational discipline constraints must be respected by
Foundation main-part design. They are non-negotiable inputs from the PM
lens.

**D26 Team 50-100 — system must scale to 50-100 humans [D26].**
Every Foundation part must be designed with a hub-and-spoke governance
topology that admits team members beyond the founder. Concretely:
- Part 3 (Project Lifecycle) must support multi-owner projects where a
  single accountability per deliverable is named (not "the team owns it").
- Part 4 (Agent Swarm Governance) must anticipate the hub-and-spoke scaling
  path: subagent → dept lead → coordinator — not skip-level dispatch.
- Any Foundation artefact that bakes in "Ruslan does this" implicitly
  violates D26 and crosses into RUSLAN-LAYER.

**3-tier approval SLA (L1 contractual / L2 substantive / L3 cosmetic) [FUNDAMENTAL §4.2, §4.5].**
The HITL gate taxonomy must be explicit in Foundation governance (Part 4).
L1 = any external commitment, financial outlay, or Lock modification
(requires immediate human ack); L2 = significant artefact promotion,
strategic alignment change (requires human review within 24h); L3 =
formatting, cosmetic, reversible (batch-ackable). Without this taxonomy
in Foundation, the approval discipline degrades to "ask every time" (bottleneck)
or "never ask" (agency erosion).

**WIP limit on coordinator attention budget [FUNDAMENTAL §3.2.6].**
The Foundation health monitoring layer (Part 5) must declare and enforce
the coordinator attention cap (max ≤N active tasks). The current
`shared/state/kanban.json` holds this state [AUDIT §4.4] but no health
monitor enforces the cap. Foundation design must name where the cap
enforcement lives and how it surfaces to the coordinator.

**Hub-and-spoke: subagents report to dept lead, not coordinator [FUNDAMENTAL §2.3, CLAUDE.md Global Rule 8].**
Agent Swarm Governance (Part 4) must encode hub-and-spoke as an
architectural invariant, not a convention. The escalation rate SLI
(10-25% healthy) [FUNDAMENTAL §3.2.3] is the signal; the hub-and-spoke
topology is the mechanism. Any Foundation design that allows skip-level
dispatch (subagent → coordinator, bypassing dept lead) violates this.

**Daily Log + Draft → Promote → Archive workflow (UC-J) [FUNDAMENTAL §1 UC-J.1-J.3].**
The Operational Rhythm Layer (Part 2) must encode the three-stage draft
lifecycle as typed state transitions with named artefacts: draft (created
in daily working page), pending-review (in drafts queue), and terminal
(promoted to canonical OR archived with provenance). Without this explicit
lifecycle, drafts accumulate as information graveyard [FUNDAMENTAL §2.6
anti-patterns].

**Plan-Work-Review-Compound 40/10/40/10 at week-level [FUNDAMENTAL §3.3.1].**
The Cycle Operations Substrate (Part 1) must enforce the 40/10/40/10
ratio as a health KPI with declared drift tolerance (±10 percentage points)
and a behaviour-change rule when drift exceeds threshold (e.g., if Review
collapses to <20%, trigger protected review block before new work dispatches).
This ratio is a constitutional value [FUNDAMENTAL §2 intro and §3.3.1].

**Periodic health checkups (UC-I.1 weekly/monthly/yearly) [FUNDAMENTAL §1 UC-I.1].**
Health Monitoring Layer (Part 5) must distinguish cadence-based checkups
(automated, scheduled) from trigger-based checkups (method exhaustion,
resource inflection, safety event) [FUNDAMENTAL §2.5]. Foundation design
must name the trigger taxonomy and the escalation path for each trigger
type. The current system has no canonical trigger registry.

---

## §4 Open questions for brigadier

**OQ-MGMT-1: PM type disambiguation.**
FUNDAMENTAL describes three distinct management concerns that could each
be a Foundation part or could fold into each other:
- *Product management* (what to build, discovery, opportunity-solution)
- *Project management* (how to deliver, scope, timeline, stage gates)
- *Operations management* (daily rhythm, cadence, health monitoring)

The current Part 1-5 candidate decomposition treats these as:
Part 1 = project management (cycle), Part 2 = operations management
(daily/weekly/monthly rhythm), Part 3 = project lifecycle (project mgmt
substrate), Part 4 = governance (swarm ops), Part 5 = health (ops
monitoring). Product management in the Torres CDH sense (continuous
discovery, opportunity → solution tree, weekly customer touch) is NOT
explicitly named as a Foundation part — it was excluded as it would require
Ruslan-specific ICP context. **Question for brigadier:** Is product
management at Foundation level out of scope (RUSLAN-LAYER), or should
Foundation include a generic "Discovery Substrate" that encodes the
opportunity → solution discipline without specific ICP content?

**OQ-MGMT-2: Operational rhythm as part vs cross-cutting.**
Part 2 (Operational Rhythm Layer) is a named main part in this pre-read.
But it could be argued that daily/weekly/monthly cadence is a *pattern*
cross-cutting all other parts rather than a discrete structural part with
its own boundary. An alternative decomposition would fold the cadence
discipline into each part's own lifecycle (Cycle Operations Substrate
owns cycle-level cadence; Project Lifecycle owns project-level review
cadence; Health Monitoring owns health-checkup cadence). **Question for
brigadier:** Should Operational Rhythm be an independent Foundation part
(with its own artefacts and interface), or should cadence discipline be
distributed as a cross-cutting concern?

**OQ-MGMT-3: D26 scale — design for 50-100 today or include scale-evolution mechanics?**
D26 [D26] locks Jetix target as 50-100 humans. Foundation main parts need
to be designed so they do not require architectural redesign at that scale.
Two options:
- (A) Design each part for 50-100 from day one (heavier schema, more
  governance ceremony from the start)
- (B) Design each part for current solo-founder state WITH named
  scale-evolution mechanics (e.g., "when Part 4 reaches N agents, the
  hub-and-spoke topology must be formalised as X")
Option B aligns with Shape Up's appetite discipline (current appetite) and
the FUNDAMENTAL §4.4 boundary-flexible pattern. **Question for brigadier:**
Which option is the constitutional default for Foundation part design?

**OQ-MGMT-4: Approval SLA tiers — where do they live in the Foundation?**
The 3-tier approval SLA (L1/L2/L3) is implied by FUNDAMENTAL §4 but not
named as an explicit construct. It could live in:
- Part 4 (Agent Swarm Governance Layer) as a governance artefact
- Part 1 (Cycle Operations Substrate) as a gate-type taxonomy
- Part 5 (Health Monitoring Layer) as a compliance signal
The placement affects which Foundation part owns the SLA schema and which
parts consume it. **Question for brigadier:** Where should approval SLA
tiers be canonically defined at Foundation level?
