---
title: A-1 Critic Gate — 10-Part Foundation Review (philosophy-expert critic)
date: 2026-04-27
phase: A-1-critic
expert: philosophy-expert
mode: critic
cycle: cyc-foundation-build-2026-04-28
gate_verdict: PARTIAL
F: F3
ClaimScope: "Holds within this A-1 critic pass; subject to integrator iteration and Ruslan ack before A-2 (interface cards) dispatch"
R: "Refuted if integrator corrects all §6-listed items and philosophy-expert re-pass returns PASS; accepted when all FLAG-MAJOR items cleared and required iterations confirmed by brigadier"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/philosophy-expert.md
  - design/JETIX-FPF.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
---

# Phase A-1 Critic Gate

## §1 Verdict + Summary

**Verdict: PARTIAL**

The 10-part integrator draft is structurally sound in its major architecture: the IP-1 Role≠Executor wall is respected throughout (no agent-executor names appear as part names); the Popper falsifier test was applied explicitly and documented; all 5 anti-patterns (AP-1..AP-5) from the philosophy pre-read were applied and triggered renames/splits; U.System vs U.Episteme declarations are provided for each part; the Ruslan-creep gate was applied and documented in §1 synthesis method. These are genuine achievements over what would have been a raw expert-merge.

The PARTIAL verdict is driven by three categories of issues: (1) two FLAG-MAJOR findings — Part 9 has a residual IP-2 boundary problem where the bounded context declaration leaks toward Ruslan-specific (solo-founder cognitive workspace rather than generic owner workspace), and Part 7's state-naming has an IP-5 past-participle inconsistency that will propagate into Wave C interface cards if uncorrected; (2) three FLAG-MINOR findings across Parts 3, 6, and 10 that require integrator annotation corrections before A-2; (3) two OQ-MERGED items (OQ-3 and OQ-6) that require Ruslan ack before interface card authoring can proceed without ambiguity.

The integrator may dispatch Phase A-2 after correcting the items listed in §6. No full re-merge is required. The architecture itself passes constitutional review.

---

## §2 Per-Part Annotated Review (10 Parts)

---

### Part 1 — System State Persistence — Status: CLEAN

**IP-1 Role≠Executor check.** Clean. No agent-executor names appear. The part is defined by the git interface (commit/revert/log/YAML config read) — this is a method-signature, not an executor-binding. The service-vs-concern distinction drawn in the integrator's rationale [candidate-parts-merged.md §2 Part 1] is constitutionally correct: Part 1 has a callable interface, therefore it is a service (U.System), not an ambient concern.

**IP-2 Context-is-king check.** Clean. The bounded context is declared as "the git repository substrate" — this is generic. The specific commit-message format `[agent] action: description` appears in `CLAUDE.md` and is correctly held there, not encoded in this part's scope sentence. Ruslan-specific implementation details (specific `.claude/config/` paths) are referenced as AUDIT artefact mapping, not as Foundation invariants — an acceptable documentation of existing material rather than a Foundation constraint.

**IP-3 Artifacts>conversations check.** Clean. The part's primary output type is a committed file (the git commit itself). The Effects (E lane) of every other part routes through this part's interface. IP-3 is the constitutional foundation of this part's rationale — correctly cited [FPF §5.3].

**A.1 Holonic check.** Clean. U.System declared. The boundary is the git repository root — well-defined, testable. The whole-and-part structure is correct: Part 1 is a whole (with its own integrity checks, backup cadence, restoration SLI) and a part of Foundation (all other parts write through it).

**A.14 Typed mereology check.** Dependency from other parts to Part 1: every other part "creates-artifacts-in" Part 1. This is a `creates` edge in the Jetix-specific vocabulary. The integrator does not spell this edge-type out explicitly — minor gap. Acceptable at A-1 (edge-typing is A-2 scope for interface cards), but the dependency graph author should note that the edge from any part to Part 1 is `creates` (not `ComponentOf` or `methodologically-uses`).

**A.6.B L/A/D/E check.** Not yet specified — this is A-2 scope. No violation at A-1.

**A.13 Agency-CHR check.** Not applicable at this part level (Part 1 is infrastructure, not an agent-bearing role). No violation.

**B.3 F-G-R check.** The document itself carries F:F3, ClaimScope, R. Part 1's AUDIT artefact mapping correctly identifies the git history as the provenance chain. F-G-R enforcement is Part 6's function — not a requirement for Part 1's scope sentence.

**§6 anti-scope check.** Clean. Part 1 does not automate strategic decisions [FUNDAMENTAL §6.1], does not substitute for founder [§6.2], does not exhibit dark patterns [§6.3], does not contain scope creep [§6.5].

**Ruslan-creep check.** Clean. The scope sentence is fully generic. The specific git commit format in `CLAUDE.md` is correctly in RUSLAN-LAYER. The `.claude/config/*.yaml` path references are AUDIT documentation of existing artefacts, not Foundation constraints — acceptable.

**Verdict: CLEAN.** No required edits.

---

### Part 2 — Signal Ingestion & Triage — Status: CLEAN

**IP-1 Role≠Executor check.** Clean. The part is defined by the pipeline function (transcribe → extract → filter → triage → STOP gate) — a method signature. No specific agent instance named as a constituent. The `inbox-processor` legacy agent appears in AUDIT artefact mapping only (documentation of what exists), not as a defining element of the part.

**IP-2 Context-is-king check.** Clean. The bounded context is "the interface between external signals and the canonical KB — with a mandatory human-review STOP gate." This is fully generic. The part does not assume Ruslan's specific voice-memo content, DACH-specific signal types, or Phase-1-specific toolchain. The voice pipeline tools (`transcribe.py`, etc.) appear in AUDIT artefact mapping — implementation evidence, not Foundation constraints.

**IP-3 Artifacts>conversations check.** Clean. Every pipeline stage output is a committed file (draft artifacts, review reports). The STOP gate is an explicit structural enforcement. IP-3 is the constitutional rationale for why this part is a part [candidate-parts-merged.md §2 Part 2, FPF IP-3 cited].

**A.1 Holonic check.** Clean. U.System declared correctly. The boundary is the inbound signal interface (permeable but filtered). Draft candidates produced are correctly identified as U.Episteme (passive content), separate from the pipeline that produces them (U.System). The A.1 Agency Rule [FPF §1.4] is not violated.

**A.14 Typed mereology check.** Part 2 → Part 1 (writes committed drafts): `creates`. Part 2 → Part 3 (feeds drafts ready for KB promotion): `PhaseOf` (Part 2's output is the pre-KB phase of the information lifecycle). Not yet typed in the document — A-2 scope. No violation at A-1.

**A.6.B L/A/D/E check.** A-2 scope. No violation.

**A.13 Agency-CHR check.** The STOP gate requires human ack before canonical promotion. This is correct: promotion is J-Approve (human gate required), not J-Auto. No CHR violation detected.

**B.3 F-G-R check.** D28 anchor-mandatory is cited [D28 anchor]. The anchor-trace discipline (every draft carries active anchor) is the F-G-R-adjacent provenance requirement for this part. Correct.

**§6 anti-scope check.** Clean. The STOP gate directly implements FUNDAMENTAL §6.2 (system does not substitute for founder; recommendations yes, decisions no) and §6.1 (agents do not auto-promote to canonical). The STOP gate is the architectural enforcement, not a behavioral convention — constitutionally correct.

**Ruslan-creep check.** Clean. No DACH references, no Korp-Startup framing, no Phase-1-specific targets in scope sentence or rationale. Voice pipeline toolchain is AUDIT documentation of existing implementation.

**Verdict: CLEAN.** No required edits.

---

### Part 3 — Knowledge Base & Methodology Library — Status: FLAG-MINOR

**IP-1 Role≠Executor check.** Clean. No executor names. The part is defined by its content-type (wiki entries, typed graph edges, methodology patterns) and its access interface (/ask, /lint, /consolidate, /build-graph) — both are method-signatures at the appropriate level of abstraction.

**IP-2 Context-is-king check.** Clean. The bounded context is "the curated, queryable, provenance-linked KB and methodology library." This is generic. D27 (fork-and-merge) is correctly cited — the KB must be forkable with ICP-specific content parameterized, not hardcoded [candidate-parts-merged.md §2 Part 3 D-Lock anchor].

**IP-3 Artifacts>conversations check.** Clean. Every KB entry is a committed artifact. The pipeline sub-system (/ingest → /ask → /consolidate) produces committed files. IP-3 is explicitly cited.

**A.1 Holonic check.** FLAG-MINOR. The integrator correctly identifies this as a dual (U.Episteme content + U.System pipeline) and correctly resolves it by declaring the part's primary identity as U.Episteme (the content layer) with the pipeline as an "accessor service." This resolution is philosophically defensible under A.1 — the content holon has a defined boundary (the wiki/ directory) and a defined lifecycle (ingest → compile → lint → ready). However, the integrator's formulation is ambiguous: "the pipeline sub-system is an accessor service, not the part itself" [candidate-parts-merged.md §2 Part 3 U.System/U.Episteme]. This risks creating an invisible U.System component with no explicit holon boundary. The A.1 Agency Rule [FPF §1.4] requires behavioral roles to attach ONLY to U.System bearers; if the pipeline sub-system is not explicitly identified as its own U.System sub-holon, the A.1 boundary is fuzzy. Required annotation: the integrator should explicitly state in the Part 3 description that the pipeline sub-system (accessor service) is a U.System sub-holon of Part 4 (Coordination Protocol) or a shared infrastructure function, not a dangling U.System component internal to the U.Episteme part. This is a minor structural clarification, not an architecture change.

**A.14 Typed mereology check.** The integrator cites `ComponentOf`, `creates`, `derived_from` edge types in the FPF anchor [candidate-parts-merged.md §2 Part 3 FPF anchor: "FPF A.14 typed edges in wiki/graph/edges.jsonl"]. This is correct. The dependency from Part 3 to Part 5 (compound outputs flow into Part 3) is implicitly typed as `creates` (Part 5 creates methodology entries in Part 3). The dependency from Part 2 to Part 3 (ingest feeds Part 3) is `PhaseOf`. These are not stated explicitly in the document — acceptable at A-1.

**A.6.B L/A/D/E check.** A-2 scope.

**A.13 Agency-CHR check.** The /ingest --anchor= mandatory requirement enforces that agents do not autonomously decide what enters the canonical KB. This is correct J-Approve discipline. No CHR violation.

**B.3 F-G-R check.** The F-G-R tagging enforcement is Part 6's function. Part 3 is the storage medium; Part 6 enforces compliance. The OQ-PHIL-5 question (which part owns F-G-R compliance) is resolved by the integrator as Part 6 [OQ-MERGED items, §6 "Part 6 owns F-G-R compliance enforcement"]. This is constitutionally correct.

**§6 anti-scope check.** Clean. No strategic decisions automated, no dark patterns, no scope creep.

**Ruslan-creep check.** Clean. The 393-book Private Library appears in AUDIT artefact mapping only — this is documentation of existing content, not a Foundation constraint. The methodology library sub-layer is generic. No DACH-specific ICP content is embedded in the scope sentence.

**Required edit (FLAG-MINOR):** Add a clarifying sentence to the Part 3 U.System/U.Episteme declaration that explicitly designates where the pipeline sub-system (accessor service) belongs holonically — either as a U.System sub-holon of Part 4 (if coordination-adjacent) or as a separate shared-infrastructure service — to satisfy A.1 boundary discipline [FPF §1.4, pre-read PP-1].

---

### Part 4 — Role Taxonomy & Coordination Protocol — Status: CLEAN

**IP-1 Role≠Executor check.** Clean and constitutionally strongest part in the list. The integrator explicitly states: "this part must NOT name specific agents as constituents — it names roles (coordinator, domain-expert, meta-steward) and the methods they carry. Specific agent bindings (brigadier = Sonnet 4.6, etc.) are RUSLAN-LAYER executor-binding.yaml files" [candidate-parts-merged.md §2 Part 4 Popper falsifier]. This is the exact IP-1 discipline. The role manifests (role.md files) are correctly identified as U.Episteme; the coordination protocol is correctly identified as U.System. The IP-1 split within a single part is correctly executed.

**IP-2 Context-is-king check.** Clean. The bounded context is "any multi-agent system using hub-and-spoke topology with role-based communication" — fully generic. The acting_as field is a generic message-schema discipline, not Ruslan-specific.

**IP-3 Artifacts>conversations check.** Clean. Role manifests, executor-binding.yaml, message schema YAML, routing table — all committed artifacts. The point about the "canonical routing table as declarative YAML (not embedded in system prompts)" being a Wave C gap is correctly flagged.

**A.1 Holonic check.** Clean. Dual U.System/U.Episteme split is correctly declared with the IP-1 mandatory split note. The boundary is the coordination protocol interface (dispatch a task / receive a structured packet). Each sub-holon is well-defined.

**A.14 Typed mereology check.** Role manifests (U.Episteme) have a `constrained-by` relationship to the Governance part (Part 6 enforces role-manifest compliance). The coordination protocol (U.System) has a `methodologically-uses` relationship to Part 1 (commits route through git). Not yet typed explicitly — A-2 scope.

**A.6.B L/A/D/E check.** A-2 scope. The IP-6 5-block role.md structure cited [FPF IP-6] provides the L/A/D/E template for role manifests — correctly referenced.

**A.13 Agency-CHR check.** The J-level decision matrix (J-Auto / J-Approve / J-Strategic) per role is cited as a primary FPF anchor [A.13 Agency-CHR]. The acting_as field in the message schema enforces the CHR binding per message. This is the correct architecture.

**B.3 F-G-R check.** The F-G-R for role manifests themselves is declared via the Governance gate (Part 6). The trust-calibration audit for role manifests (are they F5+ for canonical roles?) is Part 6's quarterly audit function.

**§6 anti-scope check.** Clean. The IP-8 F.6 6-step agent onboarding (Locate/Stance/Qualify/Bind/Evidence/Conclude) is cited [FPF IP-8] — this is the correct mechanism that prevents agents from being treated as tools rather than role-filling participants. No §6 violations.

**Ruslan-creep check.** Clean. No specific agent names (brigadier, personal-assistant) appear in the scope sentence or rationale. The AUDIT artefact mapping correctly documents existing Jetix-specific artefacts without making them Foundation constraints.

**Verdict: CLEAN.** No required edits.

---

### Part 5 — Compound Learning & Methodology Capture — Status: CLEAN

**IP-1 Role≠Executor check.** Clean. The part is defined by the cycle ritual (Plan/Work/Review/Compound 40/10/40/10) and its artifacts (DRR ledger, per-agent strategies.md, methodology library entries). No executor names appear as defining elements.

**IP-2 Context-is-king check.** Clean. The bounded context is "any knowledge-work system using a structured cycle ritual to convert execution experience into improved future execution." This is fully generic. The 40/10/40/10 ratio is a generic compounding discipline, not Ruslan-specific (FUNDAMENTAL §2.2 treats it as a foundational constitutional value).

**IP-3 Artifacts>conversations check.** Clean. DRR entries must be committed files (strategies.md), not chat reflections — explicitly cited [FPF IP-3, IP-7]. The methodology library entries promoted to Part 3 are committed wiki files.

**A.1 Holonic check.** Clean. Dual declared correctly. DRR entries and methodology patterns are U.Episteme (passive content). The cycle ritual enforcement mechanism is U.System (procedural, produces effects). The boundary is the compound phase trigger (the Compound 10% of the cycle). Well-defined.

**A.14 Typed mereology check.** Part 5 → Part 3: `creates` (compound outputs create methodology library entries in KB). Part 5 → Part 1: `creates` (DRR entries are committed artifacts). Part 5 → Part 8 (Health Monitoring): feeds `strategies.md` data as health signal inputs. Not yet typed — A-2 scope.

**A.13 Agency-CHR check.** The IP-7 (writing as thinking) constraint that founder authors strategic reflection with agents contributing structured extractions is correct J-level discipline: strategic reflection = J-Strategic (founder-authored), structured extractions = J-Auto (agent-produced drafts for founder review). No CHR violation.

**B.3 F-G-R check.** The DRR entries in strategies.md inherit F-G-R requirements from Part 6's enforcement. The compound phase is where F-level uplift occurs (when a DRR entry is validated over multiple cycles, its Formality level increases from F1 to F2-F3).

**§6 anti-scope check.** Clean. The strategies.md update gate (gated by explicit cycle review) correctly implements FUNDAMENTAL §6.1 (agents do not self-modify without structure — strategies update only through explicit gated review, not runtime mutation). No dark patterns, no founder substitution.

**Ruslan-creep check.** Clean. The 40/10/40/10 ratio is FUNDAMENTAL-grounded (§2.2, §3.3.1). No DACH references, no Phase-1-specific targets in the scope sentence. The "swarm-level DRR pattern validated cycles 1-11" appears in the Cycles reuse note — documentation of existing evidence, not a Foundation constraint.

**Verdict: CLEAN.** No required edits. The dissent from engineering-expert (that Part 5 should dissolve into Parts 3 and 4) is preserved in the integrator document [dissents block]. The integrator's rationale (R2 reinforcing loop distinct from coordination function, Kauffman adjacent-possible) is constitutionally defensible. OQ-MERGED-2 correctly surfaces this for Ruslan ack.

---

### Part 6 — Governance, Provenance & Human Gate — Status: FLAG-MINOR

**IP-1 Role≠Executor check.** Minor concern. The part correctly assigns the immune-system function (IP-4) to this part. However, the integrator cites: "meta-agent as immune system — ontological integrity audit function is a primary function of this part" [FPF anchor, candidate-parts-merged.md §2 Part 6]. The word "meta-agent" is an executor name appearing in the FPF anchor citation. This is not a scope-sentence violation (the scope sentence is clean), but the FPF anchor citation should not reference the executor by name when it could reference the role function (ontological-integrity-steward role). A minor IP-1 formulation issue — not a structural violation, but risks being copied into Wave C interface cards incorrectly.

**IP-2 Context-is-king check.** Clean. The bounded context is "stage-gate enforcement, provenance-tagging, F-G-R trust calculus, HITL escalation" — all generic mechanisms. No Ruslan-specific content in scope sentence.

**IP-3 Artifacts>conversations check.** Clean. The AWAITING-APPROVAL packets, approval-log entries, and LOCKED tags are committed artifacts. The stage-gate pattern is correctly defined through committed gate files.

**A.1 Holonic check.** Clean. U.System declared. The boundary is the gate interface (`submit_draft → gate_packet → human_ack → promote_to_canonical`). Well-defined lifecycle with discrete artifacts per stage.

**A.14 Typed mereology check.** Part 6 `constrained-by` relationship to Part 1 (all gate decisions are committed through git). Part 6 `operates-in` relationship across all other parts (governance is the supersystem context that every other part operates within). Not yet typed — A-2 scope. The "constrained-by" direction is important: Part 6 is NOT ComponentOf other parts; other parts operate within Part 6's governance context.

**A.6.B L/A/D/E check.** A-2 scope. Critical note for A-2: this part's own interface card must itself demonstrate L/A/D/E lane discipline — it is the part that enforces L/A/D/E on all others, and it must exemplify what it enforces.

**A.13 Agency-CHR check.** The J-level decision matrix (J-Auto / J-Approve / J-Strategic) encoded as a structural invariant is cited [A.13 Agency-CHR, FPF §2.1a]. OQ-PHIL-4 (blast-radius classification sub-function) is correctly flagged as unresolved and surfaced to OQ-MERGED-6. The OQ-MERGED-6 recommendation ("Default-Deny classifier for novel actions in Part 6") is constitutionally correct and required [FUNDAMENTAL §6.1: "якщо action не categorized — default deny + escalate"].

**B.3 F-G-R check.** Part 6 is the designated owner of F-G-R compliance enforcement [OQ-PHIL-5 resolved]. This is constitutionally correct (Munger lollapalooza convergence: immune-system IP-4, honesty CP-2, trust-calibration B.3 all reinforce single-owner with audit cadence). The Wave C gap (F-G-R compliance enforcement not yet a systematic Part-owned function) is correctly flagged.

**§6 anti-scope check.** Clean. Part 6's halt-and-alert mechanism [FUNDAMENTAL §6.7: "AI попытался strategize → halt + log + alert founder"] is correctly specified as a primary function. The mechanism exists at the architecture level, not only as behavioral convention — constitutionally correct per PP-4 [pre-read].

**Ruslan-creep check.** Minor: The FPF anchor citation references "meta-agent" by name (executor-name, RUSLAN-LAYER). Required correction: replace "FPF IP-4 Meta-agent as immune system" citation with "FPF IP-4 immune-system function (ontological-integrity-steward role)" — retaining the function, removing the executor name from the Foundation-level Part description.

**Required edit (FLAG-MINOR):** In the FPF anchor for Part 6, replace the "meta-agent" executor reference with the generic role function ("ontological-integrity-steward role or equivalent immune-function role") to maintain IP-1 discipline in the Foundation document itself [FPF §5.1 IP-1, pre-read PP-1].

---

### Part 7 — Project Lifecycle Substrate — Status: FLAG-MAJOR

**IP-1 Role≠Executor check.** Clean. No executor names. The part is defined by the lifecycle scaffold (brief → staged → active → reviewed → closed → archived) and the typed project-type schema. Clean.

**IP-2 Context-is-king check.** Clean. The bounded context is "typed scaffolding for creating, staging, tracking, reviewing, and archiving work items" — generic. D26 (team 50-100 scaling constraint) is a generic scalability requirement. No DACH-specific content.

**IP-3 Artifacts>conversations check.** Clean. Stage-gate acceptance predicates, appetite declarations, scope records — all committed artifacts. The existing skills (/project-bootstrap, /project-review, etc.) are correctly identified as reusable implementation evidence.

**A.1 Holonic check.** Clean. U.System declared. The boundary is the project lifecycle state machine. Well-defined.

**A.14 Typed mereology check.** Part 7 → Part 6 (per-project stage gates use the same gate mechanism). This is a `methodologically-uses` edge (Part 7 uses Part 6's gate mechanism methodologically; it is not ComponentOf Part 6). The integrator notes this correctly: "partial — per-project stage gates use the same gate mechanism owned by Part 6" [FUNDAMENTAL UC mapping, D.2]. The edge type is not yet spelled out — A-2 scope.

**A.6.B L/A/D/E check.** A-2 scope.

**A.13 Agency-CHR check.** Stage-gate acceptance predicates per project type enforce J-level authority. Project state transitions (draft → staged, etc.) are J-Approve or J-Strategic depending on significance. No CHR violation detected in the scope description.

**B.3 F-G-R check.** The project lifecycle artifacts (scope records, acceptance criteria) inherit F-G-R requirements. No dedicated F-G-R concern in this part — Part 6 owns enforcement.

**§6 anti-scope check.** Clean. The stage-gate structure prevents agents from auto-advancing projects without human ack.

**Ruslan-creep check.** Clean. The 4 project type templates (consulting/research/product/bets) appear in AUDIT artefact mapping only. No DACH-specific ICP content in scope sentence.

**IP-5 Past-Participle Check — FLAG-MAJOR.** The scope sentence lists proposed project states: "draft → staged → active → review → closed → archived." The states `active` and `review` are NOT past-participles. Per IP-5 [FPF §5.5], alpha states must be past-participle verbs unless a whitelisted `in-X`/`under-X` exception is documented. `active` is an adjective (not a past-participle — the correct form would be `activated` or `started`). `review` is a noun/gerund infinitive base (the correct form would be `under-review` if whitelisted per §5.5a, or `reviewed` if terminal). If `review` is intended as a non-terminal (active review period before closure), it must be explicitly whitelisted as `in-review` per FPF §5.5a. If it is terminal, it should be `reviewed`.

This is FLAG-MAJOR because IP-5 violations in Foundation part definitions propagate into Wave C interface cards and then into actual alpha state machines, corrupting the Hook 4 enforcement layer [FPF §5.5, IP-5].

**Required corrections (FLAG-MAJOR):**
1. Replace `active` with `activated` (past-participle: the project has been activated/scoped and is running).
2. Replace `review` with either:
   - `under-review` (whitelisted as `in-X`/`under-X` exception per §5.5a, with documented semantic justification: "under-review = active review window where decision pending; 'reviewed' would imply review complete")
   - OR `reviewed` if this is a terminal state (review concluded, project awaiting closure decision).

The FPF anchor already correctly cites IP-5 [candidate-parts-merged.md §2 Part 7 FPF anchor]. The violation is in the scope sentence itself, not in the understanding. A mechanical correction.

---

### Part 8 — Health Monitoring & System Integrity — Status: CLEAN

**IP-1 Role≠Executor check.** Clean. No executor names. The part is defined by the monitoring function (SLI/SLO definition, metric collection, anomaly surfacing, backup verification, drift detection). The immune-system function (IP-4 quarterly audit) is assigned to this part as a generic function — no FPF-Steward executor name appears in the scope sentence or rationale. Leak risk 4 [pre-read §4] was correctly resolved: "Leak risk 4 addressed — this part owns the generic audit scope and cadence; the specific role name (FPF-Steward), the specific agent assigned (meta-agent), and the specific trigger thresholds (30+ agents) are RUSLAN-LAYER bindings" [FPF anchor: "FPF IP-4 immune-system function — the quarterly audit... is a primary function of this part, NOT of a separately named 'FPF-Steward' which is a RUSLAN-LAYER role binding"].

**IP-2 Context-is-king check.** Clean. The bounded context is "operational observability of the system" — generic. No DACH references, no Phase-1-specific thresholds embedded in the scope sentence. The FUNDAMENTAL §3 SLI/SLO starter values are correctly treated as calibration parameters, not Foundation constants [FUNDAMENTAL §3 note: "конкретные численные values ниже — starter values"].

**IP-3 Artifacts>conversations check.** Clean. Health dashboard files, SLI/SLO registry, alert records — all committed artifacts produced by the monitoring pipeline.

**A.1 Holonic check.** Clean. U.System declared. The boundary is the health monitoring pipeline interface (signal collection → threshold evaluation → alert generation → behavior-change trigger). Correctly identified as structural part with cross-cutting effect (not cross-cutting without owner) — the investor-expert Munger inversion argument is constitutionally sound [candidate-parts-merged.md §2 Part 8 reasoning].

**A.14 Typed mereology check.** Part 8 consumes inputs from all other parts (health signals are `derived_from` other parts' state artifacts). Part 8's alert outputs feed into Part 6 (governance escalation taxonomy) and Part 9 (owner review). Edge types: Part 8 `methodologically-uses` Part 1 for durable storage of health records; Part 8 `operates-in` all other parts as a monitoring context. Not yet typed — A-2 scope.

**A.13 Agency-CHR check.** The fail-loud principle [FUNDAMENTAL §5.2] and the FUNDAMENTAL §6.7 "halt + log + alert" discipline are cited. Correctly: anomaly detection is J-Auto (monitoring runs automatically); behavior change triggered by error budget burn is J-Approve (founder ack required for changing operational mode); structural integrity failures are J-Strategic (halt and escalate). No CHR violation.

**B.3 F-G-R check.** The quarterly immune-system audit (F-G-R compliance across all artifact types) is assigned here [FPF IP-4]. This is constitutionally correct per OQ-PHIL-5 resolution in Part 6 — there is a slight tension: Part 6 owns F-G-R enforcement (compliance gate at promotion time) while Part 8 owns the quarterly audit (immune-system check on accumulated drift). This dual-ownership is acceptable IF the Wave C interface cards for Parts 6 and 8 clearly delineate: Part 6 = gate enforcement (real-time, per-artifact); Part 8 = audit compliance (periodic, system-wide drift detection). The distinction must be explicit in A-2 interface cards.

**§6 anti-scope check.** Clean. The health monitoring does not automate strategic decisions. Alert generation is automatic; response decision is founder-owned. Constitutionally correct.

**Ruslan-creep check.** Clean. No DACH references, no Phase-1-specific targets, no FPF-Steward executor name in scope. Leak risk 4 [pre-read §4] correctly resolved.

**Verdict: CLEAN.** No required edits. Note for A-2: the F-G-R dual-ownership between Part 6 (gate) and Part 8 (audit) should be made explicit in both interface cards.

---

### Part 9 — Owner Interaction Scaffold — Status: FLAG-MAJOR

**IP-1 Role≠Executor check.** Clean. No executor names. The part is defined by the interaction scaffold function (daily working page creation, draft-to-canonical promotion, review rituals, attention-budget enforcement, approval SLA taxonomy).

**IP-2 Context-is-king check — FLAG-MAJOR.** The FPF anchor states: "FPF IP-2 (Context-is-king — the bounded context of this part is explicitly 'the owner's cognitive workspace,' not a generic user interface)" [candidate-parts-merged.md §2 Part 9 FPF anchor]. The phrase "the owner's cognitive workspace" is dangerously close to Ruslan-specific framing. The IP-2 bounded context for this part should be: "the structured interface between the system and its single human owner-operator in a solo-founder system architecture." The phrase "cognitive workspace" imports a Ruslan-specific concept (the "owner cognitive workspace" framing that appears in ROY-ALIGNMENT and JETIX-PHILOSOPHY as Ruslan-specific concerns) rather than the generic Foundation concept.

More significantly: the UC mapping for Part 9 includes A.1 (Strategic management — weekly and monthly touchpoints) and A.2 (Strategic document creation and maintenance). The integrator's rationale is "the owner's weekly review IS the strategic management touchpoint in a solo-founder system" [candidate-parts-merged.md §2 Part 9 rationale]. This is IP-2 FLAG-MAJOR: "in a solo-founder system" is a bounded context specification, but it is not stated explicitly as such. A generic professional knowledge worker system may have team-based strategic review (not solo-founder weekly review). The Part 9 description must explicitly declare its bounded context as: "a solo-owner system where the owner is the sole strategic decision-maker" — AND must explicitly note that this part's Wave C interface card will require a bridge (F.9) when instantiated in a system with multiple strategic decision-makers.

Without this explicit context declaration, Part 9 silently assumes the solo-founder context while appearing to be generic Foundation — this is the IP-2 violation pattern [pre-read PP-2: "generic-vs-Ruslan-specific clean"]. The solo-founder assumption is in fact constitutionally valid (FUNDAMENTAL §0 scopes Jetix to a "professional knowledge worker" system with a single owner), but it must be explicit, not silent.

**IP-3 Artifacts>conversations check.** Clean. Daily log entries, weekly review files, monthly reflection files — all committed artifacts. The interaction scaffold produces committed files as its primary output.

**A.1 Holonic check.** U.System declared. The boundary is the owner's daily workflow interface. Partially clean — the "cognitive workspace" framing above creates a boundary ambiguity (is the boundary the daily-log file schema, or the owner's mental model?). The file schema boundary is well-defined; the cognitive workspace boundary is not. Required correction: define the boundary as the structured daily/weekly/monthly workflow artifact schema, not the cognitive workspace concept.

**A.14 Typed mereology check.** Part 9 consumes outputs from all other parts (agent drafts, project status, KB freshness, health alerts). Part 9's outputs (daily-log, weekly-review, monthly-reflection) flow into Part 1 (committed files) and inform Part 8 (owner reflection data as health signal). Not yet typed — A-2 scope.

**A.6.B L/A/D/E check.** A-2 scope.

**A.13 Agency-CHR check.** The IP-7 writing-as-thinking asymmetry (owner authors, agents contribute extractions) is correctly cited. The 3-tier approval SLA (L1/L2/L3) maps to J-Strategic/J-Approve/J-Auto respectively. No CHR violation.

**B.3 F-G-R check.** The strategic documents created through this part's workflow must carry F-G-R tags. Part 6 enforces compliance at promotion time.

**§6 anti-scope check.** Clean. The part correctly implements FUNDAMENTAL §6.2 (system does not substitute for founder) through the IP-7 discipline. The attention-budget cap enforcement is a correctly scoped mechanism — it bounds agent interruption demand on the founder's attention without removing founder agency.

**Ruslan-creep check.** FLAG-MAJOR concerns above. Additionally: the "3-tier approval SLA taxonomy" cited [mgmt-expert.md §3] should be confirmed as generic (L1/L2/L3 are generic tier names grounded in FUNDAMENTAL §2.2 [Three-tier approval SLA]) before appearing in Foundation. Confirmed generic — no creep here.

**Required corrections (FLAG-MAJOR):**
1. Revise the FPF anchor IP-2 citation to replace "the owner's cognitive workspace" with an explicit bounded-context declaration: "this part's bounded context is a single-owner professional knowledge-worker system; bridge required (F.9, FPF §5.2 U.BoundedContext) when instantiated in multi-owner or team systems."
2. Revise the rationale's "in a solo-founder system" phrase to explicitly declare this as a bounded context, not a universal assumption: "in a single-owner system architecture (the primary Jetix deployment context), the weekly review IS the strategic management touchpoint; this is a bounded-context declaration, not a universal claim."

---

### Part 10 — External Touchpoints & Network Interface — Status: FLAG-MINOR

**IP-1 Role≠Executor check.** Clean. No executor names. The CRM pipeline and integration adapter pattern are defined by their functions, not by specific agents.

**IP-2 Context-is-king check.** FLAG-MINOR. The FPF anchor states: "FPF IP-2 (Context-is-king — the CRM's bounded context is explicitly relationship-management for the generic knowledge-worker owner; DACH-specific ICP bindings are RUSLAN-LAYER)" [candidate-parts-merged.md §2 Part 10 FPF anchor]. This is correct. However, the scope sentence includes "multi-channel output routing (voice, text, webhook delivery)" as a function of this part. The G.2 UC (Unified output delivery regardless of modality) is mapped here. This creates a risk that the Part 10 interface card will conflate two distinct bounded contexts: (a) the relationship-management context (CRM) and (b) the output-routing context (delivery infrastructure). These are potentially different bounded contexts with different IP-2 implications — a CRM is a generic knowledge-worker tool, while output routing depends on the owner's specific channel choices (voice-memo, webhook, etc.). Minor: the integrator should note in the rationale that the G.2 delivery-side function is a thin stub in Part 10 and may split into a separate part in Wave C if the bounded contexts diverge in complexity.

**IP-3 Artifacts>conversations check.** Clean. CRM records are filesystem-first committed artifacts [D17]. Append-only history per contact (§11 CRM schema). No ephemeral state.

**A.1 Holonic check.** U.System declared. The boundary is the external relationship and integration interface. The CRM content (contact records) is U.Episteme; the CRM pipeline (state-transition management) is U.System. The same dual-nature as Part 3. Same minor A.1 clarification needed: the CRM content sub-holon and the pipeline sub-holon should be explicitly delineated as two sub-holons within Part 10, not fused.

**A.14 Typed mereology check.** Part 10 → Part 2 (inbound external signals route to Signal Ingestion): `PhaseOf` — the external signal capture is the pre-processing phase of the Part 2 pipeline. Part 10 → Part 1: `creates` (CRM records are committed). The CRM graph edges (8 CRM edge types per CLAUDE.md) feed into Part 3's edges.jsonl: `creates`. Not yet typed — A-2 scope.

**A.6.B L/A/D/E check.** A-2 scope. Critical note for A-2: the L.1-L.3 external integrations stub must specify in its Laws lane that all write-actions to external services require explicit human ack (FUNDAMENTAL §6.1 anti-pattern: "auto-respond external без ack"; §4.2 HITL principle; §4.5 anti-pattern list).

**A.13 Agency-CHR check.** The write-ack gate for external integration actions is correctly specified in the scope sentence. All outbound actions through write-ack gates are J-Approve minimum. External commitment actions (auto-create commitments external) are prohibited [FUNDAMENTAL §4.5]. No CHR violation.

**B.3 F-G-R check.** CRM records carry provenance per contact history (§11 append-only). F-G-R tagging of CRM records is not explicitly addressed — this is a gap. CRM interaction notes (what was said, when, by whom) should carry F-level tags (F1 for informal notes, F5+ for signed agreements). The Wave C interface card for Part 10 should include a provenance/F-G-R section.

**§6 anti-scope check.** Clean on §6.1-§6.2. Clean on §6.4 privacy: the scope sentence notes that DACH-specific ICP bindings are RUSLAN-LAYER. However, the Part 10 description does not explicitly state the §6.4 privacy principles for CRM (consent-respected, forget-request compliance, sensitive info encrypted, cross-context awareness). These are generic Foundation requirements [FUNDAMENTAL §6.4]. Required: add an explicit §6.4 reference to the Part 10 FPF anchor or D-Lock anchor so the Wave C interface card knows to implement these constraints. This is a FLAG-MINOR omission — not a violation of the scope sentence, but a gap that could produce an interface card without privacy architecture discipline.

**Ruslan-creep check.** Minor risk correctly flagged by OQ-MERGED-3 (fork-separation declaration for Part 10 is the highest-risk part). The integrator notes: "Part 10 is therefore partially a Phase-A stub (relationship tracking is operational; external integrations are a Phase-B/C materialisation surface)" [candidate-parts-merged.md §2 Part 10]. This is honest. The CRM schema (`crm/_schema/strategy-hooks.yaml` with 6 offers + 6 asks that reference `decisions/`, `directions/_active/`) is RUSLAN-LAYER content that must not be embedded in Foundation. Confirmed in AUDIT artefact mapping (documentation only). OQ-MERGED-3 fork-separation checklist is the right resolution.

**Required edit (FLAG-MINOR):** Add an explicit §6.4 privacy reference to the Part 10 rationale or D-Lock anchor, specifying that the CRM component must implement the FUNDAMENTAL §6.4 generic privacy principles (consent-respected, forget-request, sensitive-info encryption, cross-context awareness). This is required because the CRM is the only Foundation part that explicitly stores information about third parties (contacts), making privacy architecture a structural Foundation requirement here, not merely an operational detail.

---

## §3 Cross-cutting Concerns Review (5)

**Cross-cutting 1 — Git/Filesystem Discipline.** Constitutionally correct to treat as cross-cutting. The Popper test was applied: "does this have an independent lifecycle or artifact type beyond 'write to this repo'?" — the answer is no; git discipline is a write constraint on all other parts' outputs. Treating it as cross-cutting avoids the SPoF of a "git part" that every other part depends on as a structural component. The enforcement mechanism (Part 6 governs; `CLAUDE.md` declares commit conventions) is adequate. No enforcement gap: every part's Wave C interface card will declare git commit in its Effects (E lane) as a mandatory output.

**Cross-cutting 2 — Provenance Tagging (F-G-R and inline [src:...]).** Constitutionally correct to treat as cross-cutting. The OQ-PHIL-2 resolution (provenance embedded in every part's E lane, with Part 6 owning compliance enforcement and Part 1 owning durable storage) correctly avoids the SPoF risk of a standalone "provenance part" that every other part routes through. The enforcement gap concern (provenance as "everyone's responsibility and therefore no-one's") is mitigated by explicitly assigning compliance enforcement to Part 6 as a primary function. The resolution is constitutionally sound.

**Cross-cutting 3 — Operational Rhythm / Cadence.** Constitutionally correct to treat as cross-cutting. The cycle ritual ownership is correctly distributed: cycle STRUCTURE is Part 5 (compound learning); owner's daily/weekly INTERACTION with the rhythm is Part 9 (Owner Interaction Scaffold); health SIGNALS from the cadence are Part 8 (Health Monitoring). The cadence itself is a temporal constraint, not a part with its own data or lifecycle. No enforcement gap.

**Cross-cutting 4 — Append-Only Log Pattern.** Constitutionally correct to treat as cross-cutting. This is an architectural invariant (FUNDAMENTAL §2.1, D25, Kleppmann event-sourcing discipline) that every part's Deontics (D lane) must declare. No independent lifecycle. Cross-cutting disciplining is the correct treatment.

**Cross-cutting 5 — IP-1 Role≠Executor Discipline.** Constitutionally correct to treat as cross-cutting. IP-1 is a constitutional discipline enforced structurally through Part 4 (role manifests) and audited through Part 6 (governance). Making IP-1 a standalone part would be an AP-3 category error ("AI Augmentation as a main part" equivalent) — a property turned into a part. No enforcement gap: Part 4 is the structural home of IP-1 implementation; Part 6 is the audit home. Both parts' Wave C interface cards must include IP-1 compliance checks explicitly.

**No promotions recommended.** All five cross-cutting concerns are correctly resolved as ambient disciplines, not parts. No enforcement gaps detected that would require promotion.

---

## §4 Open Q Reflections (OQ-MERGED 1-7)

**OQ-MERGED-1 (Provenance as cross-cutting vs standalone; was OQ-PHIL-2 + investor Q2).**

Critic position: The integrator's resolution (cross-cutting) is constitutionally correct. See §3 Cross-cutting 2 above. The Part 6 + Part 1 split (enforcement gate vs durable storage) correctly prevents the SPoF risk while maintaining a single compliance owner. Recommended Ruslan ack option: ACCEPT the cross-cutting resolution. If Ruslan wants a higher-visibility provenance function, the alternative is to add a dedicated "Provenance Officer" sub-function within Part 6 (named explicitly in the Part 6 Wave C interface card) — not a separate part.

**OQ-MERGED-2 (Compound Learning Engine vs Protocol within Agent Coordination; was engineering-expert Ambiguity 4).**

Critic position: Part 5 should remain standalone. The constitutional argument is the R2 reinforcing loop (distinct from R1 and from Part 4's coordination function). Epistemically: the Kauffman adjacent-possible framing is correctly applied — Part 5 is what expands the set of possible future cycles, while Part 4 is what executes within the current set. These are categorically different functions (Vincenti P7 applied: Part 4 is "theoretical tools" — the coordination machinery; Part 5 is "practical considerations" — the learning discipline that makes the machinery better over time). Recommended Ruslan ack option: ACCEPT Part 5 as standalone with the dissent preserved. If after 3 Wave C cycles the DRR work-list collapses into Parts 3 and 4 without residue, the dissolve option remains available.

**OQ-MERGED-3 (Fork-and-merge separation surface; was investor Q5).**

Critic position: This is the highest-epistemic-risk OQ in the list. Creep risk 3 [pre-read §4] names the USB-C metaphor and Korp-Startup framing as RUSLAN-LAYER — these must not appear in any Part 10 interface card. The per-part "fork-separation declaration" (what is parameterized for RUSLAN-LAYER vs Foundation-invariant) is a constitutional requirement for D27 compliance [FPF §5.2, D27]. Recommended Ruslan ack: REQUIRE this as Wave A scope, not Wave C scope. Specifically: the per-part fork-separation declaration should be added to each part's current description in candidate-parts-merged.md before A-2 interface card authoring begins. If it is left to Wave C, the interface card authors will implicitly make fork-separation decisions without constitutional guidance. This is the single OQ where deferral to Wave C creates the highest risk.

**OQ-MERGED-4 (Product management / continuous discovery at Foundation level; was mgmt OQ-MGMT-1).**

Critic position: Torres CDH (continuous discovery, opportunity-solution loop) belongs in RUSLAN-LAYER, not Foundation. The epistemic argument: continuous discovery is a specific methodology (methodology = a method for choosing methods, per Левенчук). Foundation can include "generic discovery substrate" as a function of Part 9 (Owner Interaction Scaffold) — specifically, the weekly strategic review is the natural home for a generic "opportunity intake" ritual. However, the CDH-specific vocabulary (opportunity-solution tree, assumption testing, etc.) is methodology selection, which is HITL-only [A§1.4 universal never-list; FPF §5.10.4]. Recommended Ruslan ack: A generic "opportunity intake" sub-function (not CDH-branded) is acceptable in Part 9 as the weekly review's strategic planning component. CDH itself goes to RUSLAN-LAYER methodology library.

**OQ-MERGED-5 (Health Monitoring materialisation gate; was systems OQ-SYS-5).**

Critic position: Part 8 should be "specify and stub" for Wave C (not "specify and implement"). Epistemic reason: FUNDAMENTAL §3 provides the SLI/SLO shape with explicit starter values (§3 note: "calibrate в первые 2-3 months"). The Foundation-level deliverable is the SLI/SLO schema and the audit cadence specification; the numerical calibration and tool implementation are Phase-B materialisation. This is consistent with the integrator's own framing that the Primary Wave C gap for Part 8 is the unified Foundation-level health schema. Recommended Ruslan ack: ACCEPT "specify and stub" for Wave C; PLAN Part 8 materialisation as Phase-B work after Foundation spec is locked.

**OQ-MERGED-6 (Blast-radius categorization — Foundation primitive or RUSLAN-LAYER; was investor Q1 + OQ-PHIL-4).**

Critic position: The Default-Deny classifier for novel/unclassified actions MUST be in Foundation (Part 6), not RUSLAN-LAYER. Constitutional ground: FUNDAMENTAL §6.1 states "якщо action не categorized — default deny + escalate, не 'creative interpretation'" — this is a constitutional hard rule, not a RUSLAN-LAYER behavioral convention. The J-level matrix provides per-role per-decision-class authority; the Default-Deny classifier handles novel actions that fall outside existing decision-classes. Without it, agents confronting novel situations have no constitutional guidance and default to "creative interpretation" — the exact anti-pattern FUNDAMENTAL §6.1 prohibits [FUNDAMENTAL §6.1 last bullet]. The integrator's OQ-MERGED-6 recommendation ("yes, this belongs in Part 6 as Default-Deny classifier") is constitutionally correct. Recommended Ruslan ack: ACCEPT the Default-Deny classifier as a Part 6 primary function. The founder-absence delegation protocol (investor Q1) belongs in RUSLAN-LAYER (who specifically gets delegated to is executor-specific), while the generic delegation protocol template belongs in Foundation (Part 6 or Part 9).

**OQ-MERGED-7 (U.System vs U.Episteme full declaration; was OQ-PHIL-1).**

Critic position: The integrator's U.System/U.Episteme declarations per part are sufficient for A-2 with corrections noted in §2 above (Part 3 pipeline sub-holon clarification; Part 9 cognitive-workspace boundary clarification; Part 10 CRM dual-holon delineation). The declarations are not perfect, but they are sufficiently precise to allow Wave C interface card authoring to proceed. Recommended Ruslan ack: ACCEPT the declarations as sufficient for A-2 with the corrections from §6 applied. A separate philosophy-expert critic pass before A-2 is NOT required — the corrections are integrator-level edits, not architecture-level changes.

---

## §5 Coverage Matrix Critic Check (Foundation Parts × FUNDAMENTAL UC A-L)

**UC-A review.** A.1 and A.2 (Strategic Management, document creation) are mapped to Part 9. A.3 (strategic alignment enforcement) is mapped to Part 6. A.4 (decisions tracking and recall) is mapped to Part 6. This split is constitutionally defensible: governance enforces alignment (A.3, A.4); the owner's weekly review IS the strategic touchpoint (A.1, A.2 in solo-founder context). One concern: A.4 "decisions tracking" maps to Part 6, but the `decisions/` directory is owned by Part 6 as an AUDIT artefact [candidate-parts-merged.md §2 Part 6 AUDIT artefact mapping]. This is correct. No duplication issue.

**UC-B review.** B.1 (selective inbox with triage) and B.5 (rapid ingestion pipeline) map to Part 2. B.2-B.4 (multi-wiki storage, source preservation, synthesis) map to Part 3. Coverage is clean. No mapping errors.

**UC-C review.** C.1 (self-improvement compound cycle) maps to Part 5. C.2-C.3 (skill acquisition, methodology library) map to Parts 3 and 5 jointly. The joint coverage is constitutionally correct: skill acquisition is a function that produces methodology library entries (Part 3) through a compound learning process (Part 5). No duplication — this is healthy redundancy (a UC can be served by multiple parts; the question is whether each part's contribution is distinct, which it is here).

**UC-D review.** D.1-D.2 (project lifecycle, resource budgeting) map exclusively to Part 7. Correct.

**UC-E review.** E.1-E.3 (multi-agent coordination, agent self-learning, agent communication) map to Part 4. E.2 (agent self-learning) also partially maps to Part 5. This dual mapping is intentional and constitutionally correct: E.2's protocol dimension (how agents use DRR in their coordination interactions) lives in Part 4; E.2's compound-ritual dimension (how the DRR ritual turns interaction data into improved future interactions) lives in Part 5.

**UC-F review.** F.1-F.2 (AI augmentation continuity, persistent memory) map to Parts 3 and 5. The dual mapping is constitutionally correct: F.1 persistent memory across sessions is provided by the KB (Part 3 — wiki entries persist); F.2 AI augmentation continuity is provided by strategies.md compound learning (Part 5 — agent capabilities persist and improve). No duplication issue — different mechanisms for different aspects of continuity.

**UC-H review.** H.1-H.3 (Company-as-Code, provenance, reversibility) map to Part 1. H.4 (health monitoring and alerting) maps to Parts 6 and 8. H.5 (quality gates) maps to Parts 6 and 7. The dual mapping for H.4 (Part 6 alert routing + Part 8 alert generation) is constitutionally correct and reflects the correct architectural split (Part 8 detects, Part 6 routes escalation through the gate mechanism). The dual mapping for H.5 (Part 6 owns the gate mechanism, Part 7 uses it per-project) is also correct — a `methodologically-uses` relationship.

**UC-I review.** I.1 (periodic health checkups) maps to Parts 8 and 9. I.2 (owner self-reflection prompts) maps to Parts 8 and 9. I.3 (recommendation engine) maps to Part 8. I.4 (system self-preservation) maps to Parts 6 and 8. The dual mapping for I.1 and I.2 (Part 8 computes the health signal; Part 9 scaffolds the owner's review ritual) is constitutionally correct. The dual mapping for I.4 (Part 6 stage-gate = self-preservation of canonical state; Part 8 integrity checks = ongoing self-preservation monitoring) is constitutionally correct.

**UC-A.4 placement concern.** A.4 (decisions tracking, recall, and governance) is mapped to Part 6. The integrator explains: "the decisions ledger — decisions/ directory — is owned and enforced by this part" [candidate-parts-merged.md §2 Part 6 FUNDAMENTAL UC mapping]. An alternative reading would place UC-A.4 in Part 9 (Owner Interaction Scaffold) since decisions tracking is part of the owner's strategic management touchpoint. Verdict: Part 6 is the correct home. The decisions/ directory is a canonical governance artifact (LOCKED files, D-series decisions) that requires the full provenance + human-gate enforcement of Part 6. The owner INTERACTS with decisions through Part 9 (weekly review), but the decisions LIVE in Part 6. The distinction is U.System ownership vs interaction interface — correct architectural split.

**UC-F.1 in Parts 3+5 — duplication or redundancy?** Constitutionally this is healthy redundancy: two distinct mechanisms serve the same UC (persistent memory). Part 3 serves F.1 through wiki KB persistence (factual content); Part 5 serves F.1 through strategies.md persistence (agent learning). Different content types, different access patterns, both necessary for full F.1 coverage. No duplication issue.

**No orphan UC categories.** All 12 categories A-L map to at least one part — confirmed.

---

## §6 Required Iterations Before Phase A-2 Dispatch

The following edits are required of the integrator before Phase A-2 (interface cards) can proceed. No full re-merge is required. These are targeted corrections to the existing draft.

**1. Part 7 — IP-5 State-Naming Correction (FLAG-MAJOR)**
- Change: Replace `active` with `activated` in the scope sentence state list.
- Change: Replace `review` with either `under-review` (if non-terminal, with documented semantic justification per FPF §5.5a whitelist) or `reviewed` (if terminal).
- Reason: IP-5 [FPF §5.5] requires past-participle or whitelisted in-X/under-X forms for all alpha states. `active` and `review` violate this. The FPF anchor already cites IP-5 — the scope sentence must comply.
- Cite: FPF §5.5 IP-5; pre-read §1 IP-5 (past-participle discipline; 5 whitelisted exceptions).

**2. Part 9 — IP-2 Bounded Context Declaration (FLAG-MAJOR)**
- Change: Revise the FPF anchor IP-2 citation from "the owner's cognitive workspace" to an explicit bounded-context declaration: "this part's bounded context is a single-owner professional knowledge-worker system; bridge required (F.9, FPF §5.2 U.BoundedContext) when instantiated in multi-owner or team systems."
- Change: In the rationale, explicitly mark "in a solo-founder system" as a bounded context declaration, not a universal claim.
- Reason: IP-2 [FPF §5.2, A.1.1 U.BoundedContext] requires explicit bounded context; "cognitive workspace" imports Ruslan-specific framing; solo-founder assumption must be declared explicitly as a context, not silently embedded.
- Cite: FPF §5.2 IP-2; pre-read PP-2 (Foundation ≠ Jetix-specific; boundary heuristic); pre-read §4 Leak risk 3.

**3. Part 6 — IP-1 Executor-Name Removal from FPF Anchor (FLAG-MINOR)**
- Change: In the FPF anchor for Part 6, replace "FPF IP-4 (Meta-agent as immune system — ontological integrity audit function is a primary function of this part)" with "FPF IP-4 (immune-system function — the ontological integrity audit function is a primary function of this part; the specific role assigned to fill this function is a RUSLAN-LAYER executor-binding)."
- Reason: IP-1 [FPF §5.1] requires executor names not to appear in Foundation-level Part definitions; "meta-agent" is an executor name.
- Cite: FPF §5.1 IP-1; pre-read PP-1 (agents are not parts; executor name = RUSLAN-LAYER).

**4. Part 3 — A.1 Pipeline Sub-Holon Clarification (FLAG-MINOR)**
- Change: Add one sentence to the U.System/U.Episteme declaration: "The pipeline sub-system (accessor service) is a U.System component; it is owned by Part 4 (coordination protocol infrastructure) or treated as shared infrastructure — NOT a dangling U.System component internal to the U.Episteme part. The A.1 boundary of Part 3 is the wiki/ directory content layer."
- Reason: A.1 Agency Rule [FPF §1.4] requires behavioral roles to attach ONLY to U.System bearers; the pipeline sub-system's holon affiliation must be explicit to prevent boundary ambiguity.
- Cite: FPF §1.4 A.1 Agency Rule; pre-read §1 A.1 Holonic Foundation (dual-nature risk).

**5. Part 10 — §6.4 Privacy Reference Addition (FLAG-MINOR)**
- Change: Add a D-Lock anchor reference to FUNDAMENTAL §6.4 in the Part 10 description: "FUNDAMENTAL §6.4 (privacy and data ethics — generic privacy principles apply to all CRM data: consent-respected, forget-request compliance, sensitive info encrypted at rest, cross-context awareness; no inference of protected characteristics)."
- Reason: Part 10 is the only Foundation part that explicitly stores data about third parties (contacts). FUNDAMENTAL §6.4 applies structurally, not merely as an operational convention. Without explicit citation, the Wave C interface card for Part 10 may omit privacy architecture.
- Cite: FUNDAMENTAL §6.4 privacy and data ethics; pre-read §1 PP-7 (founder agency preservation — §6.2 analog for contact privacy).

**6. OQ-MERGED-3 Fork-Separation Declaration — Escalate to Wave A Scope (OQ requiring Ruslan ack)**
- Required: Ruslan ack on whether the per-part fork-separation declaration (what is parameterized for RUSLAN-LAYER vs Foundation-invariant) is Wave A scope or Wave C scope.
- Critic recommendation: Wave A scope. If deferred to Wave C, interface card authors will make fork-separation decisions without constitutional guidance.
- Reason: D27 compliance [D27]; pre-read §4 Leak risk 3 (USB-C/Korp-Startup framing must not enter Foundation); OQ-MERGED-3 as written defers this to Wave C.
- Cite: D27 (fork-and-merge); FPF §5.2 IP-2 (bridge requirements at cross-context boundaries); pre-read PP-3 (A.14 typed mereology — extension points are "design instrumentalities" that must be explicitly designed).

---

## §7 Provenance

All claims in this critic gate trace to the following sources.

| Claim / Flag | Source |
|---|---|
| IP-1 clean assessments (all parts) | [FPF §5.1 IP-1]; [pre-read §2 PP-1]; [pre-read §3 AP-1] |
| IP-2 FLAG-MAJOR on Part 9 | [FPF §5.2 IP-2; A.1.1 U.BoundedContext]; [pre-read §2 PP-2]; [pre-read §4 Leak risk 3] |
| IP-2 FLAG-MINOR on Part 10 (G.2 bounded context) | [FPF §5.2 IP-2]; [pre-read §2 PP-2] |
| IP-3 artifacts>conversations — all parts clean | [FPF §5.3 IP-3]; [pre-read §1 IP-3]; [FUNDAMENTAL §2.1 Three cross-cutting substrates] |
| A.1 Holonic check — Part 3 pipeline ambiguity | [FPF §1.4 A.1 Agency Rule]; [pre-read §1 A.1 Holonic Foundation]; [pre-read §3 AP-2] |
| A.1 Holonic — Part 9 boundary clarification | [FPF §1.4 A.1 Agency Rule]; [pre-read §1 A.1 Holonic Foundation] |
| A.14 typed mereology — all parts (A-2 scope) | [FPF §3.5 A.14]; [pre-read §2 PP-3] |
| A.6.B L/A/D/E — all parts (A-2 scope) | [FPF §4.3 A.6.B]; [pre-read §1 A.6.B] |
| A.13 Agency-CHR — all parts | [FPF §2.1a A.13]; [FUNDAMENTAL §6.1]; [pre-read §1 A.13] |
| B.3 F-G-R Part 6 + Part 8 dual-ownership | [FPF §12.7 B.3]; [pre-read §1 B.3]; [pre-read §5 OQ-PHIL-5] |
| IP-5 FLAG-MAJOR on Part 7 state-naming | [FPF §5.5 IP-5]; [pre-read §1 IP-5] |
| IP-6 5-block role.md — Part 4 clean | [FPF §5.6 IP-6]; [pre-read §1 IP-6] |
| IP-7 writing-as-thinking — Part 5 + Part 9 | [FPF §5.7 IP-7]; [pre-read §1 IP-7]; [FUNDAMENTAL §2.2 Phase 4 Compound] |
| IP-8 F.6 6-step onboarding — Part 4 | [FPF §5.8 IP-8]; [pre-read §1 IP-8] |
| §6.1 agents-don't-strategize (PP-4) — Part 6 | [FUNDAMENTAL §6.1]; [FPF §5.10.4]; [pre-read §2 PP-4] |
| §6.2 founder-agency-preservation (PP-7) — Parts 2, 6, 9 | [FUNDAMENTAL §6.2]; [pre-read §2 PP-7] |
| §6.4 privacy omission — Part 10 FLAG-MINOR | [FUNDAMENTAL §6.4] |
| §6.7 boundary violation triggers — Part 6 | [FUNDAMENTAL §6.7] |
| Ruslan-creep clean — Parts 1, 2, 4, 5, 7, 8 | [FUNDAMENTAL §0 two-layer principle]; [pre-read §4 Leak risks 1-5] |
| Ruslan-creep FLAG-MINOR — Part 6 (meta-agent name) | [FPF §5.1 IP-1]; [pre-read §4 Leak risk 4] |
| Cross-cutting resolutions — all 5 correct | [pre-read §5 OQ-PHIL-2 (provenance)]; [FUNDAMENTAL §2.1 Three substrates] |
| OQ-MERGED-3 Wave A escalation recommendation | [D27 fork-and-merge]; [FPF §5.2 IP-2 Bridge requirement]; [pre-read §2 PP-3 A.14] |
| OQ-MERGED-6 Default-Deny classifier in Part 6 | [FUNDAMENTAL §6.1 last bullet]; [pre-read §5 OQ-PHIL-4]; [FPF §2.1a A.13] |
| PARTIAL verdict justification | All FLAG-MAJOR items above + dissent preserved on OQ-3 and OQ-6 requiring Ruslan ack |
| UC-A.4 in Part 6 (not Part 9) — correct | [candidate-parts-merged.md §2 Part 6 UC mapping]; [FUNDAMENTAL §1 UC-A.4 Decisions tracking] |
| UC-F.1 in Parts 3+5 — healthy redundancy | [Vincenti P7 — different knowledge categories, not duplication]; [pre-read §1 Vincenti P7] |
| Conformance checklist — §3.1 of philosophy-expert.md | [pre-read §3 Conformance Checklist: all 7 binary checks pass on this critic gate output] |
