---
title: Systems-expert pre-read — Foundation main parts (integrator mode)
date: 2026-04-27
phase: A-0
expert: systems-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
sources:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
  - decisions/JETIX-SYSTEM-OVERVIEW.md
confidence: medium
confidence_method: pattern-match
F: F3
ClaimScope: "Holds within scope of inputs read in Phase A-0; scales to candidate-merge pass (A-1); does not claim finality."
R: "Refuted if A-1 synthesis finds that proposed parts have unresolvable dependency cycles or violate FPF A.1 holonic well-formedness; accepted if parts survive philosophy-expert critic pass without constitutional violations."
---

# Systems-expert Pre-read — Foundation Main Parts

## §1 Read summary (~600 words)

The core claim of FUNDAMENTAL is structural: Jetix is an **AI-augmented exocortex** for professional knowledge workers — a brain-extension that amplifies rather than replaces the founder's strategic agency [FUNDAMENTAL §0]. The systems-thinking lens reveals a set of reinforcing and balancing loops embedded in the 35 use cases, and several leverage-point candidates that should shape how the Foundation decomposes into parts.

**Feedback loops observed in the 35 UC:**

Two dominant loops emerge when reading categories A–L together.

*Reinforcing loop R1 — Compound Knowledge Accumulation:* Information enters via inbox/capture [FUNDAMENTAL §2.1, UC-B.1 / UC-B.5], is processed and indexed [FUNDAMENTAL §2.1 stage 4–6], stored in KB [UC-B.2 / UC-B.3], synthesised on demand [UC-B.4], and the synthesis produces new queries that drive more ingestion. Each cycle deposits more KB mass → future synthesis quality improves → owner's cognitive leverage grows → more ambitious projects generate more input. This is an explicit +loop (reinforcing). The Compound Engineering cycle [FUNDAMENTAL §2.2 UC-C.1, 40/10/40/10 ratio] formalises the cadence at which this loop executes.

*Reinforcing loop R2 — Agent Self-Improvement:* Agents execute tasks [UC-E.1], accumulate DRR entries in `strategies.md` [FUNDAMENTAL §2.4], weekly distillation extracts patterns [FUNDAMENTAL §2.4 Layer 2], agent prompts improve, future execution quality improves, more complex tasks become delegatable → agent swarm scope expands. This is a second +loop. Without the Compound phase (10%) this loop degrades to linear [FUNDAMENTAL §2.4 anti-pattern "DRR deferred"].

*Balancing loop B1 — Agency-Preservation Brake:* Every time system complexity grows (R1/R2 feeding back), the constitutional hard rule that agents do NOT strategize and do NOT auto-execute architectural or strategic decisions [FUNDAMENTAL §4.3 / §4.5 / §6.1 / §6.2] applies a damping force. This is the deliberate −loop. Without it, agency erosion occurs (per Левенчук IP-1 [FPF §5 IP-1]).

*Balancing loop B2 — Health Monitoring Correction:* Operational drift (KB staleness, mailbox backlog, SLO budget burn) is detected by health-monitoring [FUNDAMENTAL §3.1–§3.3 / UC-I.1 / UC-H.4], surfaced to the founder, and corrected. This loop's time constant is daily/weekly/monthly checkup cadence [FUNDAMENTAL §2.5]. Without it, degradation accumulates silently — the system's primary failure mode [FUNDAMENTAL §5.2 fail-loud principle].

**Leverage points (Meadows 12-rung):**

The strongest leverage sits at rung L3 (goals/purpose of the system): the "system amplifies founder's strategic agency" goal, enforced through agency-preservation constraints [FUNDAMENTAL §4.3 / §6.2], is what keeps R1+R2 from becoming a runaway system that substitutes for the founder. Removing this constraint would be the fastest way to destroy the system's value.

Next leverage at L4 (rules / information flows): the provenance and audit-trail discipline [FUNDAMENTAL UC-H.2 / §2.1 stages 5–6 / D25 Company-as-Code [SYSTEM-OVERVIEW §3 D25]] is the system's trust substrate. Every other part (KB, agent swarm, daily ops) depends on it being reliable. Degrading provenance degrades all downstream synthesis quality.

Third candidate at L7 (information flow structure): the mandatory anchor discipline [FUNDAMENTAL §2.3 web-research-dump handler / D28 Query-driven KB [SYSTEM-OVERVIEW §3 D28]] controls what enters the KB. This is a leverage point because garbage-in-garbage-out is the primary KB failure mode; the anchor requirement prevents pool-filling driven by availability instead of anticipated queries.

**Requisite variety (Ashby):**

The agent swarm [UC-E.1–E.3] must have at least as much variety as the task environment it controls. The 35 UC categories span information management, daily operations, external integrations, strategic governance, agent coordination, health monitoring, and CRM — seven distinct variety dimensions. The current 12-agent roster [CLAUDE.md Agent Roster / SYSTEM-OVERVIEW §L4] provides coverage across these, but a single-layer decomposition of Foundation that collapses these seven dimensions into fewer than five main parts risks under-specification (requisite variety deficit).

**VSM viability (Beer Levels 1–5):**

The 35 UC map naturally onto Beer's VSM:
- Level 1 (Operations): UC-J daily ops, UC-B information lifecycle, UC-K CRM interactions.
- Level 2 (Coordination): UC-E.1 multi-agent coordination, message schema + mailboxes [FUNDAMENTAL §2.2 Work phase / SYSTEM-OVERVIEW §L4].
- Level 3 (Audit/Optimisation): UC-H.4 health monitoring, UC-I.1 periodic checkups, UC-C.1 Compound Engineering.
- Level 4 (Intelligence/Futures): UC-A.1–A.4 strategic management, UC-B.5 rapid ingestion under strategic direction.
- Level 5 (Identity/Policy): UC-H.5 stage-gated approval, Locks D1–D29, anti-scope §6, founder agency-preservation rules.

A Foundation missing an explicit Level-3 sub-system (observability + self-correction) would be VSM-incomplete. This surfaces as a candidate "main part" below.

**Senge 11 laws applicable:**

Law 4 ("the easy way out usually leads back in"): Skipping the provenance discipline to move faster leads to unverifiable KB entries; retrieval quality degrades; founders lose trust in the system and go back to manual work. Foundation must make provenance the easy path, not the hard one [FUNDAMENTAL §5.2 / §2.1 stage 5].

Law 7 ("cause and effect are not closely related in time"): Agent strategy improvements accumulate over months, not cycles. The Compound Engineering cadence [FUNDAMENTAL §2.4] exists precisely because the feedback from DRR to better execution is time-delayed. Foundation must preserve the DRR mechanism even in early phases when payoff is invisible.

**Holonic boundaries (FPF A.1):**

Each main part must be a U.Holon — simultaneously a whole (its own bounded context with a declared boundary) and a part (nested inside the Foundation supersystem) [FPF §1.1 / §12.1]. The inside/outside test [FPF §1.3]: removing the part breaks a core invariant. All five candidate parts below pass this test.

**Adjacent-possible (Kauffman):**

From the current substrate (git-repo + wiki + voice pipeline + 12 agents + CRM [SYSTEM-OVERVIEW §0 TL;DR current state]), the adjacent-possible includes: query-driven retrieval improvement, agent strategy distillation automation, health-metric dashboarding. What is NOT adjacent-possible yet: multi-wiki federation, federated git (D27 Phase 3), token economy. Foundation should target only what is reachable from current substrate, not what requires structural change.

---

## §2 Candidate "main parts" (3-5)

### Part 1 — Information Lifecycle Substrate

**One-line scope:** The pipeline from raw signal capture through storage, indexing, and query-driven retrieval — the system's read/write nervous system.

**Why it's a part:** It owns the R1 reinforcing loop (compound knowledge accumulation). Its boundary is: everything between "external signal arrives" and "synthesised answer leaves" [FUNDAMENTAL §2.1 8-stage flow]. This is the highest-variety sub-system in Foundation; removing it breaks every other part's access to knowledge.
- F: F3 | ClaimScope: holds across all 12 UC categories that produce or consume KB content | R: refuted if synthesis can be grounded without a typed pipeline

**FUNDAMENTAL UC mapping:** B.1–B.5 (information lifecycle) primary; A.2 (strategic doc creation), A.3 (strategic alignment enforcement), C.2 (skill acquisition) depend on it.

**FPF anchor:** FPF A.1 (holonic boundary — permeable, filtered inbound), FPF A.14 (typed edges in `wiki/graph/edges.jsonl` — `ComponentOf`, `creates`, `derived_from`), D28 Query-driven KB [SYSTEM-OVERVIEW §3 D28]. IP-3 (artifacts over conversations) is the constitutional ground for why this pipeline must produce committed files.

**Cross-cutting?** No — it is a primary structural part, not a cross-cutting concern. Other parts consume its output but do not own its feedback loop.

---

### Part 2 — Agent Coordination & Communication Layer

**One-line scope:** The protocols, roles, message schemas, hub-and-spoke topology, and escalation taxonomy that let multiple specialised agents operate without shared mutable state.

**Why it's a part:** It owns the Level-2 VSM (coordination) function [Beer] and the R2 reinforcing loop (agent self-improvement via strategy accumulation). Its boundary: everything between "coordinator receives a task" and "cells return structured results." Without this part, the multi-agent swarm [UC-E.1–E.3] collapses to single-agent throughput.
- F: F3 | ClaimScope: holds at current 12-agent scale; dynamics change at 50+ agents (Ashby variety budget expands) | R: refuted if all 35 UC can be served by a single agent without coordination protocol

**FUNDAMENTAL UC mapping:** E.1–E.3 (agent swarm) primary; J.1–J.3 (daily ops dispatch) depend on it; H.5 (stage-gated approval) uses its escalation taxonomy.

**FPF anchor:** FPF IP-1 Role≠Executor (role manifests are episteme; agent instances are system bearers) [FPF §1.4 / §12.1]; FPF §12.3 Role-Method-Work alignment; FUNDAMENTAL §2.2 Work phase hub-and-spoke discipline; `acting_as` field mandatory per [FUNDAMENTAL §3.2.4].

**Cross-cutting?** No — it is a structural part. Coordination is not a concern that "pervades" other parts in the way observability does; it is a discrete sub-system with its own boundary.

---

### Part 3 — Governance & Provenance Layer

**One-line scope:** The mechanisms that make every artifact traceable, every decision reversible, and every architectural change human-gated — the system's constitutional enforcement substrate.

**Why it's a part:** It owns the B1 balancing loop (agency-preservation brake) and the B2 balancing loop (health-monitoring correction) at their structural level — stage-gated approval, Locks, audit trail, F-G-R tagging, Default-Deny. The Meadows L3 leverage point (goals of the system — agency preservation) lives here. Removing this part would allow agents to drift toward autonomous decision-making, violating the foundational anti-scope [FUNDAMENTAL §6.1 / §4.5 / FPF IP-1].
- F: F4 | ClaimScope: holds at any scale; this is the Level-5 VSM (identity/policy) function | R: refuted if the system can preserve founder agency through soft conventions alone without structural enforcement

**FUNDAMENTAL UC mapping:** H.1–H.5 (foundation and reliability) primary; A.4 (decisions tracking and governance) feeds the decisions ledger; §4.6 enforcement mechanisms; §6.7 violation triggers.

**FPF anchor:** FPF A.1 WF-A1-1 (single boundary per holon); FPF §12.7 B.3 F-G-R trust calculus; FPF §12.5 Four Guard-Rails (GR-3 Unidirectional Dependency — Core → Tooling acyclic); D25 Company-as-Code [SYSTEM-OVERVIEW §3 D25]; D27 Fork-and-Merge [SYSTEM-OVERVIEW §3 D27].

**Cross-cutting?** This is a boundary case. The concern pervades all other parts (every part must respect provenance, every agent output must be F-G-R tagged). However, the *mechanism* (stage-gate files, Locks, `decisions/` directory, AWAITING-APPROVAL packets) has its own discrete boundary and lifecycle — it is not merely a discipline, it is a structural sub-system. Verdict: **structural part with cross-cutting effect**. Flag for brigadier in Phase A-1.

---

### Part 4 — Health Monitoring & Self-Correction Layer

**One-line scope:** The operational observability substrate — metric collection, SLI/SLO framing, periodic health checkups, anomaly surfacing, and self-preservation integrity checks.

**Why it's a part:** This is the VSM Level-3 (audit/optimisation) function. Without it, both reinforcing loops (R1 and R2) accumulate drift silently — KB staleness, agent strategy misalignment, resource overrun — until failure is catastrophic rather than gradual. Meadows' Senge Law 4 ("the easy way out leads back in") predicts that skipping health monitoring eventually forces a more expensive manual rescue.
- F: F3 | ClaimScope: holds for any system with ≥2 reinforcing loops and time-delayed feedback | R: refuted if empirical evidence shows systems without explicit Level-3 function remain healthy over multi-month operation

**FUNDAMENTAL UC mapping:** I.1–I.4 (continuous health & self-improvement) primary; H.4 (health monitoring & alerting); §3.1–§3.3 all health indicators; §2.5 health checkup flows.

**FPF anchor:** FPF §12.1 (holonic trinity — U.System operational integrity); FPF P-7 (Pragmatic Utility — falsification rewarded, i.e., health failures must be surfaced not suppressed); FUNDAMENTAL §5.2 fail-loud principle; SLI/SLO/error-budget framing [FUNDAMENTAL §2 three cross-cutting substrates].

**Cross-cutting?** Yes and no. The concern (every part should be observed) is cross-cutting. But the mechanism (health-checkup pipeline, metric aggregation, anomaly alerting, `decisions/weekly/` and `decisions/quarterly/` outputs) is a distinct functional unit with its own input/output boundary. Same verdict as Part 3: **structural part with cross-cutting effect**. Flag for brigadier.

---

### Part 5 — Compound Learning & Self-Improvement Engine

**One-line scope:** The structured cycle (Plan/Work/Review/Compound 40/10/40/10) and its associated artefacts (DRR ledger, `strategies.md` per agent, methodology library, skill-acquisition pipeline) that convert execution experience into improved future execution.

**Why it's a part:** This is where the R2 loop executes structurally. The Kauffman adjacent-possible framing makes this concrete: only capabilities adjacent to current state are reachable. This part governs the rate at which adjacency expands — it is the system's growth engine. Without it, Foundation is a static toolbox, not a compounding OS.
- F: F3 | ClaimScope: holds under the assumption that knowledge-work compound effects are real (Karpathy System Prompt Learning empirical ground); breaks down if execution cycles are one-shot with no reuse | R: refuted if DRR entries fail to produce detectable improvement in agent output quality over 10+ cycles (measurable via feedback-loop-hit-rate KPI)

**FUNDAMENTAL UC mapping:** C.1–C.3 (self-improvement & learning) primary; §2.2 Compound phase (10%); §2.4 self-improvement flows; §2.8 skill-acquisition pipeline.

**FPF anchor:** FPF §12.4 P-10 (Open-Ended Evolution — every entity expected to evolve indefinitely); FPF §12.3 Role-Method-Work alignment (Work records feed the learning); IP-3 Artifacts over conversations (DRR must be committed files, not chat reflections).

**Cross-cutting?** No — this is a structural part with its own bounded process (weekly distillation, monthly synthesis, quarterly architectural review) and its own artefact types (DRR entries, methodology library). Other parts execute within cycles; this part is what turns cycles into compounding.

---

## §3 Constitutional pressure points

**IP-1 Role≠Executor for agent-related parts:**
Parts 2 and 5 both involve agents. The constitutional constraint [FPF §1.4 / §12.1 / FUNDAMENTAL §6.1] is that role manifests (episteme) are passive — only the founder or an explicitly-bound U.System instance can change them. This means Part 2 (Agent Coordination) must be designed so that communication schemas, role definitions, and escalation taxonomy live as committed files (`executors/*.yaml`, `role.md`, message schema YAMLs) that agents READ but do not WRITE at runtime. Part 5 (Compound Learning) must gate `strategies.md` updates through the Compound phase ritual, not auto-update at runtime. Any architecture where agents self-modify their own roles without a gated cycle violates IP-1.

**D25 Company-as-Code git-as-substrate:**
All five parts produce artefacts. Every artefact must land in a committed file with atomic provenance [SYSTEM-OVERVIEW §L0 / FUNDAMENTAL UC-H.1]. This rules out any design where parts communicate through in-memory shared state, database rows, or Notion-only records without filesystem mirrors. Specifically: Part 1 (Information Lifecycle) must commit raw events to `events.jsonl` and derived entries to `wiki/`; Part 3 (Governance) must produce gate files in `decisions/` as committed artifacts, not as approval states stored only in a UI.

**D28 Query-driven KB filtering:**
Part 1 (Information Lifecycle Substrate) must enforce anchor-mandatory ingestion [SYSTEM-OVERVIEW §3 D28 / FUNDAMENTAL §2.3 web-research-dump handler]. This is a constitutional constraint on Part 1's input boundary: no item enters the KB without a declared anticipatory query. The boundary-enforcement mechanism for this constraint belongs in Part 3 (Governance & Provenance) — the audit trail that verifies anchor presence is a governance function, not an information-lifecycle function. This creates a dependency: Part 1 → depends on → Part 3 for anchor-presence enforcement.

**Anti-scope §6 — no agents strategize, no founder substitution:**
All five parts must respect the hard rule that agents do not strategize [FUNDAMENTAL §6.1] and the system does not substitute for the founder [FUNDAMENTAL §6.2]. Concretely:
- Part 2 (Agent Coordination) must route strategic escalations to HITL, not to another agent.
- Part 5 (Compound Learning) must gate monthly/quarterly synthesis through founder-written reflection [FUNDAMENTAL §2.4 Layer 2/3 quality gates] — the system can propose patterns, but writing-as-thinking is non-delegatable.
- Part 3 (Governance) must preserve the Default-Deny posture [FUNDAMENTAL §4.6] — any new action type that is not categorised defaults to human-ack-required, not silent execution.

**Founder agency-preservation §6.2:**
This is the L3 leverage point (Meadows) — the goal of the system. It must not be compromised in the pursuit of automation efficiency. Specifically: boundary-flexible tasks [FUNDAMENTAL §4.4] can shift from manual to AI-augmented as the system matures, but the shift mechanism itself (explicit re-evaluation trigger, founder ack) must be part of Part 3 (Governance). The anti-pattern is "drift by convenience" — automation expanding without explicit approval.

---

## §4 Open questions for brigadier

**OQ-SYS-1 — Part 3 and Part 4 cross-cutting vs structural:**
The systems lens identifies both Governance & Provenance (Part 3) and Health Monitoring (Part 4) as structural parts with cross-cutting effect. Engineering-expert may decompose these differently — as concerns that pervade all parts rather than as discrete parts themselves. Brigadier should surface this tension in the A-1 merge: if philosophy-expert's critic pass flags these as IP-2 context violations (global state assumptions) rather than bounded sub-systems, they may need to be redesigned as Aspect-Of (FPF A.14 AspectOf) relations rather than ComponentOf parts.

**OQ-SYS-2 — Daily Operations (UC-J) and CRM (UC-K) placement:**
FUNDAMENTAL categories J (daily ops) and K (CRM) are not represented as standalone main parts in this reading. The systems lens absorbs them into Part 1 (daily-log artefacts feed the information lifecycle) and Part 2 (CRM interactions route through coordination layer). This may be incorrect: if J and K have distinct feedback loops (they do — UC-J has a daily bookending rhythm, UC-K has a relationship-tier cadence) they may warrant a "Daily Operations & Relationship Tracking" part. Request: mgmt-expert pre-read should clarify whether UC-J and UC-K have enough operational distinctness to warrant separate decomposition.

**OQ-SYS-3 — External Integrations (UC-L) boundary:**
Category L [FUNDAMENTAL UC-L.1–L.3] describes an Integration Hub with read-only intelligence trackers and write-access action coordinators. The systems lens notes this is a **permeable boundary** sub-system [FPF §1.3] — it mediates all external signal flows. It was not proposed as a separate main part because it is adjacent-possible only at Phase 2+ (most integrations require external API connectivity not established in Phase A). However, if engineering-expert identifies a distinct interface contract (integration adapter pattern) it may deserve its own part. Flag for A-1 synthesis.

**OQ-SYS-4 — Feedback-loop-hit-rate KPI for the Compound Learning part:**
Part 5 (Compound Learning Engine) has a proposed acceptance predicate tied to feedback-loop-hit-rate KPI. This KPI is defined in the systems-expert memory [agents/systems-expert strategies.md] but is not yet materialised in FUNDAMENTAL. Brigadier should surface to Ruslan: does the Foundation include the KPI definitions themselves as artefacts (a monitoring schema within Part 4), or are KPIs defined per-agent and aggregated by Part 4? The answer affects the interface card between Part 4 (Health Monitoring) and Part 5 (Compound Learning).

**OQ-SYS-5 — VSM Level-3 materialisation gate:**
The health-monitoring part (Part 4) corresponds to Beer VSM Level-3. FUNDAMENTAL describes it through periodic checkup cadences [§2.5] and health indicators [§3]. However, the SYSTEM-OVERVIEW current state note [§0 TL;DR] confirms that L5-L9 are spec'd but not executed, and that health dashboarding is not yet operational. Brigadier should flag: does Phase A Foundation work materialise Part 4 as an operational sub-system, or only as a specification? The adjacent-possible constraint (Kauffman) suggests materialising only what is reachable from current substrate at Phase A; full health dashboarding may belong to Wave C delivery gates rather than Foundation specification.
