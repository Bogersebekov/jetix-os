---
title: Candidate Parts Merged — draft 8-14 list (integrator)
date: 2026-04-27
phase: A-1
expert: systems-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
inputs:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/systems-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/investor-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/philosophy-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/cycle-artefact-register.md
confidence: medium
confidence_method: F-G-R-coherence
F: F3
ClaimScope: "Holds within this A-1 integrator pass; subject to philosophy-expert critic pass and Ruslan ack before promotion"
R: "Refuted if philosophy-expert critic finds unresolved Role=Executor violations or Ruslan-specific content surviving after this merge; accepted if all 7 philosophy pressure points clear on next critic pass"
---

# Candidate Parts Merged — Foundation Main Parts (Integrator Draft)

## §1 Synthesis Method

**Starting inventory.** 20 candidate parts arrived from 4 proposing experts (5 from systems, 5 from engineering, 5 from mgmt, 5 from investor). Philosophy-expert contributed 7 constitutional pressure points + 5 named anti-patterns + 4 Ruslan-creep leak risks — no independent part proposals.

**Deduplication rules applied:**

1. **Same function, different name → merge.** Systems Part 3 (Governance & Provenance), engineering Part 5 (Governance & Quality Gates), investor Part 1 (Provenance + Audit-Trail Substrate), and investor Part 5 (Founder Agency Preservation) all describe overlapping enforcement machinery: stage gates, provenance tagging, human ack, audit trail. They were folded into two distinct parts: one for the provenance/audit substrate (passive storage of WHO/WHEN/FROM WHAT — U.Episteme adjacent) and one for the human-gate enforcement mechanism (active enforcement of decision-class authority — U.System). This resolves the PP-2 / PP-5 tension cleanly: the "constraint mechanism" is U.System; the "audit record" is U.Episteme.

2. **Cross-cutting concern vs structural part test (Popper falsifier).** For each candidate, I applied the philosophy-expert Popper test: "If this part did not exist as a separate part, what observable system behaviour would degrade?" Engineering's "System Substrate" fails the test as a standalone *Foundation* part — git/filesystem discipline is a pervasive infrastructure constraint that every other part inherits; it has no independent lifecycle or interface contract beyond "write here." It becomes a cross-cutting discipline (§3 below), not a numbered part. Similarly, mgmt's "Operational Rhythm Layer" — daily/weekly cadence is a scheduling pattern that every other part adheres to, not a part with its own boundary and artifact type distinct from others. Cross-cutting.

3. **UC-gap fill.** Gap categories A.1-A.3 (Strategic Management), F.1-F.2 (AI Augmentation Continuity), G.1-G.2 (Multi-channel Access), K.1-K.3 (CRM/Network Tracking), L.1-L.3 (External Integrations) received no standalone proposals from any expert. Per the brief instruction, each is either absorbed into an existing part with explicit rationale, or proposed as a new part. Results: A.1-A.3 folded into the Governance & Human-Gate part with explicit scope extension; F.1-F.2 folded into the Compound Learning & Methodology part; G.1-G.2 folded into an External Signal Processing part; K.1-K.3 treated as an existing working part (CRM cycle-10) referenced under the Information Lifecycle part; L.1-L.3 proposed as a thin Integrations Interface part (Phase-A stub + Phase-B materialisation).

4. **Philosophy-expert anti-patterns applied.** AP-1 (no agent-names as part names), AP-2 (no flat "Wiki" part), AP-3 (no "AI Augmentation" part), AP-4 (no FUNDAMENTAL-as-parts conflation), AP-5 (no "Operations" catch-all). All 5 anti-patterns triggered at least one rename or split in the candidate list. The merged list uses method/capability names throughout — no executor names, no catch-all containers.

5. **Ruslan-creep gate.** All 4 creep-risk categories (11 archetypes used as defaults, 5-tier bindings with specific agents, USB-C/Korp-Startup framing, DACH/Mittelstand content) were searched in every candidate part's rationale. Where found, the content was either removed (Ruslan-specific) or reclassified as "RUSLAN-LAYER binding over this Foundation part's generic contract."

6. **Resulting count.** After merge: 10 parts. Within the 8-14 target. The count reflects the complexity of the 35 UC spread: fewer than 8 would produce cross-cutting concerns that are too large to have actionable Wave C work-lists; more than 14 would produce micro-parts with insufficient independent lifecycle.

---

## §2 Main Parts List (10 parts)

---

### Part 1 — System State Persistence

**Scope sentence.** The append-only, version-controlled ground truth substrate on which every other part stores its committed state: git repository discipline, declarative configuration, atomic commit format, reversibility primitives, and schema validation.

**U.System or U.Episteme.** U.System — this part produces operational effects (commits, reverts, git log queries); it is not passive knowledge content.

**FUNDAMENTAL UC mapping.**
- H.1 Company-as-Code (primary — this part IS the Company-as-Code implementation)
- H.2 Provenance and audit trail (primary — git history is the provenance chain)
- H.3 Reversibility and safe experimentation (primary — git revert is the mechanism)
- Cross-cutting dependency for all UC categories as the durable storage medium.

**Cross-cutting?** Yes — every other part's state ultimately passes through this substrate. However, unlike a "cross-cutting concern" (which has no interface), this part has a well-defined interface: `git commit [area] verb what (why)`, `git revert`, `git log`, declarative YAML config read. Services-vs-concerns distinction per [engineering-expert.md §3 Ambiguity 2]: this is a *service* (callable interface) not a *concern* (ambient discipline). Other parts call this interface explicitly. [src:engineering-expert.md:§2 Part 1]

**Why a part vs cross-cutting concern.** Every other part depends on it for durability — but it has its own discrete interface, schema, and lifecycle (the git repo itself has integrity checks, backup cadence, restoration drill SLI). Removing it would degrade an observable: every state change becomes unauditable and unrecoverable. Popper falsifier passes. [src:philosophy-expert.md:§1 Falsifiability check]

**FPF anchor.** D25 Company-as-Code; FPF IP-3 Artifacts over conversations (artifacts must be committed files); FPF A.1 WF-A1-1 (single boundary per holon — the boundary of this part is the git repository root).

**D-Lock anchor.** D25 (git-as-system-state, append-only substrate, atomic commits). [src:engineering-expert.md:§3 D25]

**AUDIT artefact mapping.** Entire `git/` repo; `.claude/config/*.yaml` (3 declarative configs); `CLAUDE.md` global rules; `shared/schemas/*.json` (3 JSON schemas); `swarm/lib/shared-protocols.md` (runtime contract referencing commit format). [src:engineering-expert.md:§2 Part 1 AUDIT]

**Originating expert.** Engineering-expert (Part 1: System Substrate). Investor-expert independently flagged D25 as "Lindy substrate" [investor-expert.md:§1 "Where investment compounds"]. Investor's capital-allocation framing is absorbed: the git history is the Foundation's most durable artifact.

**Cycles 3b/10/11 reuse?** Company-as-code discipline is operational per cycle 3b (partD-company-as-code.md); `/company-status` and `/knowledge-diff` skills exist. Do NOT reinvent. [src:cycle-artefact-register.md:§6.2]

---

### Part 2 — Signal Ingestion & Triage

**Scope sentence.** The pipeline that converts external raw signals (voice memo, URL, file, book excerpt, email, clipboard item) into provenance-tagged, anchor-linked draft candidates ready for Knowledge Base promotion — with a mandatory STOP gate requiring human review before any entry becomes canonical.

**U.System or U.Episteme.** U.System — this part runs pipelines (`transcribe → extract → filter → triage`), produces operational effects (draft files, review reports), and enforces the STOP gate. The draft candidates it produces are U.Episteme (passive content), but the pipeline itself is U.System.

**FUNDAMENTAL UC mapping.**
- B.1 Selective inbox with triage filters (primary)
- B.5 Rapid ingestion pipeline and proactive learning (primary)
- G.1 Multi-channel capture (voice, URL, file, clipboard — G-category gap addressed here)
- G.2 Unified capture regardless of modality (multi-channel normalisation into one pipeline format)

**Cross-cutting?** No — directed dependency: receives from external world, writes draft candidates to System State Persistence (Part 1), queues drafts for human review before Knowledge Base (Part 3) promotion.

**Why a part vs cross-cutting concern.** The voice pipeline is a working, distinct sub-system with its own tool chain (`tools/transcribe.py`, `tools/extract.py`, `tools/filter.py`, `tools/review_report.py`) and its own STOP gate [engineering-expert.md:§1 "Unix-philosophy decompositions"]. The STOP gate is not a convention — it is an architectural enforcement of FUNDAMENTAL §4.2 (AI-augmented, human-in-loop). Removing this part means raw external signals flow directly into the KB without human review, violating the agency-preservation constraint. Popper falsifier: yes — observable degrades. [src:philosophy-expert.md:§1 Falsifiability check]

**FPF anchor.** FPF IP-3 (Artifacts over conversations — every stage output is a committed file); D28 (anchor-mandatory ingestion — `/ingest --anchor=<topic|project|question>` is a required parameter, not optional [philosophy-expert.md:PP-6]); FPF A.1 (permeable but filtered inbound boundary).

**D-Lock anchor.** D28 (query-driven KB filtering — anchor mandatory at ingest boundary); D25 (every committed draft is a git commit). [src:engineering-expert.md:§3 D28]

**AUDIT artefact mapping.** `tools/transcribe.py`, `tools/extract.py`, `tools/filter.py`, `tools/review_report.py`, `tools/run_pipeline.sh`; `inbox/` (raw voice); `raw/transcripts/` (151 files); `/ingest` skill; `inbox-processor` legacy agent; `crm/_scripts/voice_router.py` (cycle-11 wire). [src:engineering-expert.md:§2 Part 3 AUDIT]

**Originating expert.** Engineering-expert (Part 3: Information Lifecycle), systems-expert (Part 1: Information Lifecycle Substrate, partial). G.1-G.2 gap addressed here — no expert proposed a standalone, but the voice pipeline already implements multi-channel capture.

**Cycles 3b/10/11 reuse?** Voice pipeline is operational (cycle 11); `/ingest` skill is operational (cycle 3b). Do NOT reinvent. [src:cycle-artefact-register.md:§6.2]

---

### Part 3 — Knowledge Base & Methodology Library

**Scope sentence.** The dual accumulation layer — the curated, queryable, provenance-linked wiki KB (atomic entity files, typed graph edges, niche slices) and the reusable methodology library (patterns, templates, workflows) — where past work compounds into future leverage through structured query-driven retrieval.

**U.System or U.Episteme.** Dual. The content (wiki entries, methodology patterns, graph edges) is U.Episteme — passive knowledge, transformed only by external actors. The pipeline that writes it (/ingest, /ask, /consolidate, /build-graph) is U.System. Philosophy-expert AP-2 was applied: this is NOT a flat "Wiki" part. [philosophy-expert.md:§3 AP-2] The part's primary identity is U.Episteme; the pipeline sub-system is an accessor service, not the part itself.

**A-1 critic correction (FLAG-MINOR resolved 2026-04-27):** Per FPF §1.4 A.1 Agency Rule, the pipeline sub-system (accessor service) holon-affiliation must be explicit. **The pipeline sub-system is a U.System component; it is operationally owned by Part 4 (coordination protocol infrastructure) where the dispatch / message-schema / hub-and-spoke routing live, OR treated as shared cross-cutting infrastructure invoked by Part 4. It is NOT a dangling U.System component internal to this U.Episteme part.** The A.1 boundary of Part 3 is the `wiki/` directory content layer (the U.Episteme holon); the pipeline that mutates that content lives in the supersystem context, not embedded in Part 3. [src:A-1-critic-gate.md:§6 item 4]

**FUNDAMENTAL UC mapping.**
- B.2 Multi-wiki knowledge storage (primary)
- B.3 Source preservation raw and processed (primary)
- B.4 Synthesis on demand (primary)
- C.2 Skill acquisition under strategic direction (methodology library aspect)
- C.3 Methodology library as first-class artifact (primary for methodology sub-layer)
- F.1 Persistent memory across sessions (F-category gap addressed — the KB IS the cross-session persistent memory; F.2 AI continuity is addressed through agent strategies.md files which are KB-adjacent)

**Cross-cutting?** Partially — KB content is consumed by all other parts (agents reference it, health monitoring queries it, daily ops uses it). But the KB has its own independent lifecycle: ingest → triage → process → store → index → retrieve → synthesize. Its internal compound mechanic (cross-reference density grows, signal quality rises) is self-contained. Not cross-cutting in the service sense; cross-referenced in the content sense. [src:investor-expert.md:§2 Part 2]

**Why a part vs cross-cutting concern.** The KB has its own distinct boundary, access interface (/ask, /lint, /consolidate), and lifecycle that does not reduce to any other part's function. The methodology library sub-layer compounds independently of the wiki's factual content layer — both are U.Episteme but with different access patterns (query-driven retrieval vs pattern-driven prescription [investor-expert.md:§5 Q2]). Removing this part means no persistent cross-session knowledge substrate — all synthesis is ephemeral, all methodology must be rediscovered each cycle. Popper falsifier: yes.

**FPF anchor.** FPF IP-3 (every KB entry is a committed artifact, not a chat output); D28 (anchor-mandatory — `/ingest --anchor=` enforced at Part 2 boundary before content reaches Part 3); FPF A.14 (typed edges in `wiki/graph/edges.jsonl` — `ComponentOf`, `creates`, `derived_from`); FPF A.1 (the wiki content layer is U.Episteme; the access pipeline is U.System — distinct roles per A.1 agency rule [philosophy-expert.md:OQ-PHIL-1]).

**D-Lock anchor.** D28 (query-driven KB, anchor discipline); D27 (fork-and-merge — Part 3 must be forkable with ICP-specific content parameterized, not hardcoded).

**AUDIT artefact mapping.** `wiki/` (552 entities, 577 edges, 9 entity types, 6 niches); `raw/books-md/` (393 books, Private Library); `raw/research/` (27 files); `wiki/graph/edges.jsonl`; `/ask`, `/lint`, `/consolidate`, `/build-graph`, `/search-kb` skills. [src:engineering-expert.md:§2 Part 2 AUDIT]

**Originating expert.** Engineering-expert (Part 2: Knowledge Substrate), systems-expert (Part 1 partial — the R1 reinforcing loop lives here), investor-expert (Part 2: Knowledge Compound Engine). C.3 methodology library consolidation is investor-expert's primary contribution.

**Cycles 3b/10/11 reuse?** A1 Karpathy++ substrate operational (cycle 3b): `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` all exist. Do NOT reinvent. Methodology library as a distinct named sub-layer within the wiki is not yet operationally populated — Wave C materialisation needed. [src:cycle-artefact-register.md:§6.2]

---

### Part 4 — Role Taxonomy & Coordination Protocol

**Scope sentence.** The typed message schema, role-manifest definitions, mailbox routing, escalation taxonomy, and hub-and-spoke dispatch protocol that govern all agent-to-agent and agent-to-owner communication — separating role (method signature, decision-class authority) from executor (agent instance binding) per IP-1.

**U.System or U.Episteme.** Dual with a mandatory IP-1 split. The role manifests (role.md files, method signatures, decision-class authority declarations) are U.Episteme — passive definitions transformed only by the governance gate. The coordination protocol (message routing, mailbox relay, escalation logic, hub-and-spoke dispatch) is U.System — it produces operational effects in real time.

**FUNDAMENTAL UC mapping.**
- E.1 Multi-agent coordination (primary)
- E.2 Agent self-learning and strategy refinement (partial — the DRR discipline lives here as a coordination protocol; the compound learning engine is Part 5)
- E.3 Agent communication discipline (primary — message schema, acting_as field, mailbox routing)

**Cross-cutting?** Partially — coordination infrastructure underlies all other parts' runtime interactions. But the coordination protocol has its own discrete interface (dispatch a task, receive a structured packet per shared-protocols §3) and its own artifacts (role.md files, executor-binding.yaml, message schema YAML, routing table). It is a service, not an ambient concern. [src:engineering-expert.md:§3 Ambiguity 2]

**Why a part vs cross-cutting concern.** Without an explicit coordination protocol, each new agent invents its own communication pattern — this is the canonical fragility cited in MAST failure-modes paper [investor-expert.md:§2 Part 3]. The routing table, message schema, and escalation taxonomy must be declarative artifacts (YAML/JSON), not embedded in system prompts. Philosophy PP-1: this part must NOT name specific agents as constituents — it names roles (coordinator, domain-expert, meta-steward) and the methods they carry. Specific agent bindings (brigadier = Sonnet 4.6, etc.) are RUSLAN-LAYER executor-binding.yaml files. Popper falsifier: yes — without this part, multi-agent coordination degrades to implicit conventions that break at context boundaries (Cognition warning). [src:philosophy-expert.md:PP-1]

**FPF anchor.** FPF IP-1 Role≠Executor strict separation (role manifests are episteme; agent instances are system bearers [philosophy-expert.md:§1 IP-1]); FPF IP-6 (5-block role.md mandatory per role: identity / ontological-positioning / method / production-dependencies / evolution); FPF IP-8 (F.6 6-step agent onboarding: Locate / Stance / Qualify / Bind / Evidence / Conclude); FPF A.6.B L/A/D/E lane discipline on every interface card.

**D-Lock anchor.** FUNDAMENTAL §3.2.4 (acting_as field mandatory); FUNDAMENTAL §4.6 (boundary enforcement mechanism — Default-Deny at the coordination gate); D26 (hub-and-spoke topology must survive to 50-100 human team).

**AUDIT artefact mapping.** `.claude/agents/brigadier.md` + 5 expert `.md` files (ROY swarm); `agents/*/strategies.md` (8 files); `comms/mailboxes/*.jsonl` (13 channels); `shared/schemas/message.schema.json`; `swarm/lib/shared-protocols.md`; `.claude/hooks/mode-prefix.sh`, `role-matrix.sh`, `verify-packet.sh` (hook layer, cycle 2). [src:engineering-expert.md:§2 Part 4 AUDIT]

**Originating expert.** Engineering-expert (Part 4: Agent Coordination), systems-expert (Part 2: Agent Coordination & Communication Layer), mgmt-expert (Part 4: Agent Swarm Governance Layer), investor-expert (Part 3: Agent Coordination + Communication Infrastructure). All 4 experts independently proposed this as a discrete part — strongest convergence in the candidate list.

**Cycles 3b/10/11 reuse?** ROY swarm 6-agent system operational; hook layer operational (log-only mode, cycle 2); shared-protocols.md runtime contract exists. The canonical "routing table as declarative artifact" (not embedded in brigadier's system prompt) is NOT yet operational — Wave C materialisation needed. [src:cycle-artefact-register.md:§6.2]

---

### Part 5 — Compound Learning & Methodology Capture

**Scope sentence.** The structured cycle ritual (Plan/Work/Review/Compound at 40/10/40/10) and its associated artifacts (DRR ledger, per-agent strategies.md, methodology library entries) that convert execution experience into improved future execution — the system's self-improvement engine.

**U.System or U.Episteme.** Dual. The DRR entries and methodology patterns are U.Episteme (accumulated knowledge, passive). The cycle ritual enforcement mechanism (compound phase trigger, DRR write obligation, strategies.md update gate) is U.System (procedural, produces effects).

**FUNDAMENTAL UC mapping.**
- C.1 Self-improvement and compound engineering cycle (primary)
- C.2 Skill acquisition under strategic direction (methodology entries include new skill templates)
- C.3 Methodology library as first-class artifact (methodology capture is the compound output that flows into Part 3)
- F.1 Persistent memory across sessions (the strategies.md per-agent files ARE the agent's persistent memory [investor-expert.md:§1 "Agent Strategies Ledger"])
- F.2 AI augmentation continuity (agent self-improvement over cycles is how AI augmentation quality persists and grows; F-category gap addressed here)

**Cross-cutting?** No — this is a structural part with its own bounded process (40/10/40/10 cadence, weekly distillation, monthly synthesis) and its own artifact types (DRR entries, methodology library entries, strategies.md files). Other parts execute within cycles; this part is what turns cycles into compounding. [src:systems-expert.md:§2 Part 5]

**Why a part vs cross-cutting concern.** The compound learning engine has a distinct operational phase (the Compound 10%) that produces specific artifacts (DRR entries in strategies.md, methodology patterns promoted to Part 3) that no other part produces. Without it, both reinforcing loops (R1 knowledge accumulation, R2 agent self-improvement) operate without a conversion mechanism — they accumulate execution but not learning. Senge Law 7: cause and effect are not closely related in time; the DRR mechanism exists precisely because feedback from execution to improvement is time-delayed [systems-expert.md:§1 Senge laws]. Popper falsifier: yes — without this part, DRR entries stop appearing in strategies.md, feedback-loop-hit-rate trends down, agent output quality plateaus. [src:systems-expert.md:§2 Part 5]

**FPF anchor.** FPF IP-7 (Writing as thinking — founder authors strategic reflection; agents contribute structured extractions; compound step must preserve human-authored reflection [philosophy-expert.md:§1 IP-7]); FPF P-10 Open-Ended Evolution (every entity expected to evolve indefinitely — this part is the mechanism); FPF IP-3 (DRR must be committed files, not chat reflections).

**D-Lock anchor.** FUNDAMENTAL §2.2 (Compound Engineering 40/10/40/10 constitutional value); FUNDAMENTAL §3.3.1 (ratio health indicators — 40/10/40/10 ±10pp drift tolerance); FUNDAMENTAL §2.4 (self-improvement flows, Layer-1/2/3 quality gates).

**AUDIT artefact mapping.** `agents/*/strategies.md` (8 files — 19 strategy entries per health.md); `swarm/wiki/meta/health.md` (cycle counter, compound-application-rate); `swarm/wiki/meta/agent-improvements/` (improvement proposals); `swarm/evals/` (eval harness, cycle 1 seeded, 3/20 cells). [src:engineering-expert.md:§2 Part 4 partial; systems-expert.md:§2 Part 5]

**Originating expert.** Systems-expert (Part 5: Compound Learning & Self-Improvement Engine). Investor-expert independently argued this is the highest-compound asset after KB [investor-expert.md:§1 "Agent Strategies Ledger"]. Mgmt-expert's "Cycle Operations Substrate" (Part 1) partially overlaps — the overlap is resolved by separating the *cycle ritual protocol* (here, in Part 5) from the *per-project lifecycle scaffolding* (Part 7 below).

**Cycles 3b/10/11 reuse?** Per-agent strategies.md files are seeded and accumulating. The compound learning ritual itself is operational at the swarm level (brigadier DRR pattern validated cycles 1-11). The methodology library sub-layer within Part 3 is not yet consistently populated from compound outputs — Wave C materialisation needed. [src:cycle-artefact-register.md:§5 Pattern 9]

---

### Part 6 — Governance, Provenance & Human Gate

**Scope sentence.** The stage-gate enforcement mechanism, provenance-tagging schema, F-G-R trust-calculus discipline, approval-log, and HITL escalation taxonomy that ensure every significant artifact passes human ack before canonical promotion, and every claim is traceable to a source — the system's constitutional enforcement substrate.

**U.System or U.Episteme.** U.System — this part enforces constraints (stage-gate checks, provenance verification, blast-radius classification, J-level decision routing) and produces operational effects (AWAITING-APPROVAL packets, promotion or rejection of drafts, audit log entries).

**FUNDAMENTAL UC mapping.**
- H.5 Quality gates and stage-gated approval (primary)
- A.3 Strategic alignment enforcement (A-category gap: this part enforces alignment via audit trail that confirms decisions reference locked constitutional documents)
- A.4 Decisions tracking, recall, and governance (A-category gap: the decisions ledger — `decisions/` directory — is owned and enforced by this part)
- H.4 Health monitoring and alerting (partial — alert routing goes through this part's escalation taxonomy before reaching Part 8)
- I.4 System self-preservation and integrity checks (partial — the stage-gate IS the self-preservation mechanism for canonical state)

**Cross-cutting?** Yes — every other part's significant outputs route through this part to become canonical. But it has its own discrete interface (`submit_draft → gate_packet → human_ack → promote_to_canonical`) and its own artifacts (AWAITING-APPROVAL files, approval-log entries, LOCKED tags). Service, not ambient discipline. The enforcement mechanism (gate files, Locks, `decisions/` directory) has its own boundary and lifecycle — it is a structural sub-system with cross-cutting effect, not merely a concern. [src:systems-expert.md:§2 Part 3 "boundary case"]

**Why a part vs cross-cutting concern.** Philosophy PP-4 (anti-scope §6.1 agents-don't-strategize must be architecture-enforced, not behavioral) and PP-7 (founder-agency-preservation: system suggests, founder decides) both demand a structural enforcement part. Removing this part means the agency-preservation constraint degrades to a behavioral convention — agents can silently promote to canonical. FUNDAMENTAL §6.7 specifies: "AI попытался strategize → halt + log + alert founder." This halt-and-alert mechanism requires a structural owner. Popper falsifier: yes — without this part, canonical state is reachable without human ack, and agency erosion accumulates. [src:philosophy-expert.md:PP-4, PP-7]

**FPF anchor.** FPF IP-4 (immune-system function — the ontological integrity audit function is a primary function of this part; **the specific role assigned to fill this function (e.g., "ontological-integrity-steward role" or RUSLAN-LAYER named role) is an executor-binding, NOT a Foundation-level constituent**); FPF B.3 F-G-R triad enforcement (every artifact carries F-G-R tags; this part owns the compliance check [philosophy-expert.md:OQ-PHIL-5]); FPF A.13 Agency-CHR (J-level decision matrix encoded as structural invariant, not behavioral guideline); FPF A.6.B L/A/D/E lanes on every interface card produced by this part.

**A-1 critic correction (FLAG-MINOR resolved 2026-04-27):** Per FPF §5.1 IP-1 + pre-read PP-1, original anchor cited "meta-agent" — that's an executor name. Corrected to immune-system function with explicit RUSLAN-LAYER deferral for the role-assignment. [src:A-1-critic-gate.md:§6 item 3]

**D-Lock anchor.** D25 (Company-as-Code — every state change is a git commit with provenance; this part enforces the commit-as-state-change rule across all other parts); D27 (Fork-and-merge — the LOCKED tag and approved canonical state must be forkable with clear extension points); FUNDAMENTAL §4.5 (12 "never automate" hard rules — this part enforces the boundary); FUNDAMENTAL §4.6 (Default-Deny posture).

**AUDIT artefact mapping.** `swarm/awaiting-approval/cycle-*.md`; `swarm/gates/AWAITING-APPROVAL-*` (8 confirmed gate documents); `swarm/logs/cyc-*/cycle-log.md`; `decisions/` (D1-D29 LOCKED files); `swarm/gates/`; `/company-status`, `/knowledge-diff`, `/lint --check-stage-gates --validate-predicate`; `.claude/config/sg-banned-phrases.yaml` (18 banned-phrase entries). [src:engineering-expert.md:§2 Part 5 AUDIT; cycle-artefact-register.md:§4]

**Originating expert.** Engineering-expert (Part 5: Governance & Quality Gates), systems-expert (Part 3: Governance & Provenance Layer), investor-expert (Part 5: Founder Agency Preservation Layer), investor-expert (Part 1: Provenance + Audit-Trail Substrate). Merged into one part per Popper test — both "provenance substrate" and "human gate" serve the same invariant ("no canonical change without an auditable, human-acked record") and separating them would create a coordination problem between the two parts on every promotion event.

**Cycles 3b/10/11 reuse?** Stage-gate pattern operational (10/10 cycles, Pattern 1); company-as-code `/company-status` and `/knowledge-diff` skills operational (cycle 3b). F-G-R compliance enforcement is NOT yet a systematic Part-owned function — flagging as Wave C gap. [src:cycle-artefact-register.md:§5 Pattern 1]

---

### Part 7 — Project Lifecycle Substrate

**Scope sentence.** The typed scaffolding for creating, staging, tracking, reviewing, and archiving work items (projects, tasks, cycles) — from brief to closure — with stage-gate acceptance predicates, appetite declarations, scope records, and resource tracking per project type.

**U.System or U.Episteme.** U.System — this part manages state transitions (`drafted` → `staged` → `activated` → `under-review` → `closed` / `archived`), enforces acceptance predicates per gate, and produces operational effects (project scaffold files, stage-gate evaluation results, archive records).

**A-1 critic correction (FLAG-MAJOR resolved 2026-04-27):** Per FPF §5.5 IP-5 past-participle discipline, original scope listed `active` (adjective) and `review` (gerund/noun) — both non-compliant. Corrected to `activated` (past-participle) and `under-review` (whitelisted in-X/under-X exception per FPF §5.5a — semantic justification: `under-review` = active review window with decision pending; `reviewed` would imply review concluded, which is properly the closed/archived state). Add to `decisions/policy/past-participle-exceptions.md` whitelist when materialized in Wave C. [src:A-1-critic-gate.md:§6 item 1]

**FUNDAMENTAL UC mapping.**
- D.1 Unified project lifecycle management across all project types (primary)
- D.2 Resource budgeting and monitoring per project (primary)
- H.5 Quality gates (partial — per-project stage gates use the same gate mechanism owned by Part 6)

**Cross-cutting?** Partially — project artifacts are consumed by Part 8 (Health Monitoring) for status aggregation and by Part 5 (Compound Learning) for retrospective DRR input. But the project lifecycle has its own distinct state machine (brief → milestones → tasks → review → closure) that no other part owns. It is a managed entity, not a concern.

**Why a part vs cross-cutting concern.** FUNDAMENTAL UC-D.1 requires unified project lifecycle management across all project types — a cross-project schema with acceptance predicates enforced per stage gate. Mgmt-expert noted that while the skills exist (`project-bootstrap`, `project-review`, etc.), the Foundation-level schema for "what a project is" with enforced stage-gate sequences is not yet canonical [mgmt-expert.md:§2 Part 3]. D26 mandates the schema survives to 50-100 humans. Popper falsifier: yes — without this part, project lifecycle governance degrades to per-project conventions, stage gates are unenforced, appetite discipline disappears.

**FPF anchor.** FPF IP-5 (explicit alpha state transitions in past-participle or whitelisted form — project states must be past-participles: `scoped`, `staged`, `active`, `reviewed`, `closed`, `archived`); FPF A.6.B L/A/D/E lanes per project type; FUNDAMENTAL §4.4 (boundary-flexible tasks — project scope is the explicit appetite declaration per Shape Up).

**D-Lock anchor.** D26 (team 50-100 — project lifecycle must scale without architectural redesign); FUNDAMENTAL §3.3 (cycle completion rate health indicators: 70-90% target).

**AUDIT artefact mapping.** `projects/` directory; `.claude/config/project-types.yaml`; `swarm/wiki/_templates/project-*/` (4 template trees); `project-bootstrap`, `project-review`, `project-archive`, `project-de-morph`, `project-promote` skills. [src:mgmt-expert.md:§2 Part 3 AUDIT]

**Originating expert.** Mgmt-expert (Part 3: Project Lifecycle Substrate). Systems-expert's OQ-SYS-2 questioned whether UC-J and UC-K warrant separate decomposition — resolved here: UC-J (daily ops bookending rhythm) maps to Part 9 (Owner Interaction Scaffold), not to this part; UC-K (CRM relationship tracking) maps to Part 10 (External Touchpoints & CRM).

**Cycles 3b/10/11 reuse?** B2 mini-swarm skills operational (cycle 3b): `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote`. B3 stage-gate DSL operational (`tools/stage-gate-eval.py`). Do NOT reinvent. The Foundation-level acceptance-predicate enforcement schema per project type needs Wave C canonicalisation. [src:cycle-artefact-register.md:§6.2]

---

### Part 8 — Health Monitoring & System Integrity

**Scope sentence.** The operational observability substrate — SLI/SLO definition, metric collection, anomaly surfacing, backup verification, agent-drift detection, methodology-freshness tracking, and periodic self-preservation integrity checks — that makes silent degradation visible before it becomes catastrophic.

**U.System or U.Episteme.** U.System — this part collects signals, evaluates thresholds, surfaces alerts, and triggers behavior-change rules when error budget burns. The health dashboard files it produces are U.Episteme (passive records), but the monitoring mechanism itself is U.System.

**FUNDAMENTAL UC mapping.**
- I.1 Periodic system health checkups — weekly, monthly, yearly (primary)
- I.2 Owner self-reflection prompts (partial — health checkup surfaces reflection triggers)
- I.3 Recommendation engine — structured recommendations from health signals (primary)
- I.4 System self-preservation and integrity checks (primary)
- H.4 Health monitoring and alerting (primary)

**Cross-cutting?** Yes — health signals are consumed across all layers. But the mechanism (health-checkup pipeline, metric aggregation, anomaly alerting, `decisions/weekly/` and `decisions/quarterly/` outputs) is a distinct functional unit with its own input/output boundary and its own artifact type (health dashboard, SLI/SLO registry, alert record). Same verdict as systems-expert §2 Part 4: structural part with cross-cutting effect. [src:systems-expert.md:§2 Part 4]

**Why a part vs cross-cutting concern.** Engineering-expert argued health monitoring is a cross-cutting concern deserving a "thin dedicated layer" rather than a heavyweight part [engineering-expert.md:§4 Ambiguity 5]. Systems-expert argued it is VSM Level-3 (Audit/Optimisation) — a distinct functional unit. Resolution in favor of standalone part, for two reasons: (1) Investor-expert's Munger inversion clinches it — "how does Foundation fail?" The answer is silently, through undetected drift [investor-expert.md:§1 Marks second-level thinking]. A cross-cutting concern without an owner will not be maintained. (2) Popper falsifier: without an owned health monitoring part, SLI/SLO definitions have no enforcing mechanism, drift accumulates silently, and the fail-loud principle [FUNDAMENTAL §5.2] is violated in practice even if asserted in principle. [src:investor-expert.md:§2 Part 4]

**FPF anchor.** FPF P-7 (Pragmatic Utility — failures must be surfaced and visible, not suppressed); FPF IP-4 (immune-system function — the quarterly audit on alpha classification drift and F-G-R compliance is a primary function of this part, NOT of a separately named "FPF-Steward" which is a RUSLAN-LAYER role binding [philosophy-expert.md:§4 Leak risk 4]); FUNDAMENTAL §5.2 fail-loud principle; FUNDAMENTAL §3 (30+ SLI/SLO pairs across 8 health domains).

**D-Lock anchor.** FUNDAMENTAL §3.1-§3.8 (all health indicators and SLI/SLO definitions); FUNDAMENTAL §5.3-§5.4 (backup 3-2-1 rule, SPoF mitigation); FUNDAMENTAL §2.5 (health checkup cadence — daily lightweight, weekly structured, monthly deep, quarterly immune-system).

**AUDIT artefact mapping.** `shared/state/system-health.json`; `shared/state/metrics/agent-performance.json`; `/lint` skill (11 KB health checks); `/company-status` skill; `swarm/evals/` harness (seeded, cycle 1). [src:mgmt-expert.md:§2 Part 5 AUDIT]

**Originating expert.** Systems-expert (Part 4: Health Monitoring & Self-Correction Layer), mgmt-expert (Part 5: Operational Health Monitoring Layer), investor-expert (Part 4: Health + Integrity Monitor). All 3 independently proposed; strong convergence. Engineering-expert was the outlier (cross-cutting-only position).

**Cycles 3b/10/11 reuse?** `shared/state/system-health.json` exists but reports "all green" with no canonical computation mechanism. `/lint` and `/company-status` are disconnected tools. A unified Foundation-level health schema with declared SLI/SLO values and behavior-change rules is NOT yet operational — primary Wave C gap for this part. [src:mgmt-expert.md:§2 Part 5]

---

### Part 9 — Owner Interaction Scaffold

**Scope sentence.** The structured interface between the system and its human owner — daily working page creation, draft-to-canonical promotion workflow, weekly and monthly review rituals, attention-budget cap enforcement, and the 3-tier approval SLA taxonomy — ensuring the owner's cognitive load is bounded and their interaction with the system is structured.

**U.System or U.Episteme.** U.System — this part manages state transitions in the owner's daily workflow (draft → pending-review → promoted/archived), enforces the attention cap, and produces operational effects (daily log entries, weekly review pages, monthly reflection prompts).

**FUNDAMENTAL UC mapping.**
- J.1 Daily working page and EOD ritual (primary)
- J.2 Draft capture and promotion workflow (primary)
- J.3 Weekly draft review (primary)
- I.1 Periodic health checkups — weekly and monthly cadence (partial — the cadence scaffold is here; the SLI computation is Part 8)
- I.2 Owner self-reflection prompts (primary — structured prompts are part of the review rituals)
- A.1 Strategic management — weekly and monthly touchpoints (A-category gap: the owner's weekly review IS the strategic management touchpoint; strategic doc creation and quarterly architectural review live here)
- A.2 Strategic document creation and maintenance (A-category gap: the draft → promote workflow is how strategic documents are created and updated)

**Cross-cutting?** Yes — this part consumes outputs from all other parts (agent drafts, project status, KB freshness, health alerts) and produces the owner's daily and weekly decision record. But it has its own discrete lifecycle (daily-log file, weekly-review file, monthly-reflection file) and its own artifact schema. Not merely ambient; it has a defined interface for other parts to push content to it (the "daily summary" surface). [src:mgmt-expert.md:§2 Part 2]

**Why a part vs cross-cutting concern.** Mgmt-expert OQ-MGMT-2 asked whether operational rhythm is a part or cross-cutting. Resolution: it is a part, for the following reason: the owner's daily workflow has a distinct artifact schema (daily-log frontmatter, weekly-review structure, monthly-reflection format) and a distinct state machine (plan → work → review → compound) that no other part owns. Folding this into every other part's lifecycle would mean each part defines its own "how does the owner interact here?" — producing incoherent interaction patterns. A unified "owner interaction scaffold" provides a single coherent interface. PP-7 (founder-agency-preservation) grounds this: the system's primary obligation is to scaffold the owner's agency, not to replace it. This part is the primary expression of that obligation. [src:philosophy-expert.md:PP-7]

**FPF anchor.** FPF IP-7 (Writing as thinking — the owner authors strategic documents; agents provide structured extractions; the interaction scaffold must preserve this asymmetry); FPF IP-2 (Context-is-king — **this part's bounded context is a single-owner professional knowledge-worker system; bridge required (F.9, FPF §5.2 U.BoundedContext) when instantiated in multi-owner or team systems**).

**A-1 critic correction (FLAG-MAJOR resolved 2026-04-27):** Per FPF §5.2 IP-2 + A.1.1 U.BoundedContext, original anchor read "the owner's cognitive workspace" — Ruslan-framing risk per pre-read §4 Leak risk 3. Corrected to explicit bounded-context declaration: single-owner professional knowledge-worker system. The "in a solo-founder system" rationale below is now an explicit bounded context declaration, not a universal claim. F.9 Bridge mechanism required for multi-owner/team instantiations (e.g., Phase 3+ Mittelstand AI Alliance use, RUSLAN-LAYER deployment beyond Ruslan). [src:A-1-critic-gate.md:§6 item 2]

**D-Lock anchor.** FUNDAMENTAL §2.6 (daily ops flow — daily-log creation, EOD ritual, inbox processing); FUNDAMENTAL §2.5 (health checkup cadence — weekly/monthly/quarterly); FUNDAMENTAL §4.2-§4.3 (human-only tasks enumeration; 3-tier approval SLA L1/L2/L3 [mgmt-expert.md:§3 "3-tier approval SLA"]).

**AUDIT artefact mapping.** `daily-log/` directory (exists, 1 file); `shared/state/kanban.json`; `/plan-day`, `/close-day` skills; `shared/state/priorities.json`. [src:mgmt-expert.md:§2 Part 2 AUDIT]

**Originating expert.** Mgmt-expert (Part 2: Operational Rhythm Layer). A.1-A.3 UC gap (Strategic Management) absorbed here with scope extension — no expert proposed standalone strategic management part; the mgmt-expert rhythm layer is the correct home because weekly/monthly reviews ARE the strategic touchpoints in a solo-founder system.

**Cycles 3b/10/11 reuse?** `/plan-day` and `/close-day` skills exist. `daily-log/` directory exists but minimally populated. Foundation-level schema for daily log artifacts, weekly review cadence, and the 3-tier approval SLA taxonomy is NOT yet canonical — Wave C materialisation needed. [src:mgmt-expert.md:§2 Part 2]

---

### Part 10 — External Touchpoints & Network Interface

**Scope sentence.** The typed interface layer for all external relationship and integration surfaces — the CRM/contact network (relationship lifecycle tracking, communication history, ICP-generic pipeline), the external integration adapter pattern (read-only intelligence trackers, write-ack action coordinators), and the multi-channel output routing (voice, text, webhook delivery).

**U.System or U.Episteme.** U.System — this part manages relationship state transitions (contact lifecycle), routes external inputs to Part 2 (Signal Ingestion), and coordinates outbound actions through write-ack gates.

**FUNDAMENTAL UC mapping.**
- K.1 Contact and relationship lifecycle management (primary — K-category gap addressed)
- K.2 Communication history and context (primary — CRM §11 append-only history)
- K.3 Network-effect tracking and relationship mapping (primary — CRM graph, edge types)
- L.1 External service read integration — intelligence trackers (primary — L-category gap addressed)
- L.2 External service write integration — action coordinators with ack (primary)
- L.3 Multi-channel access and output routing (partial — G.1-G.2 capture side is Part 2; delivery side is here; L-category gap addressed)
- G.2 Unified output delivery regardless of modality

**Cross-cutting?** No — this part has a directed boundary: inbound external signals route to Part 2 (Signal Ingestion); outbound relationship actions and integration calls route OUT through this part's write-ack gates. It does not pervade other parts' internal logic.

**Why a part vs cross-cutting concern.** CRM cycle-10 already demonstrated this is a bounded sub-system with its own schema, scripts, tests, and index — a deep module per Ousterhout test [engineering-expert.md:§1 "AUDIT working pieces"]. L.1-L.3 external integrations are explicitly out-of-scope for Phase A (most require external API connectivity not yet established) per systems-expert OQ-SYS-3, but must appear in Foundation's part decomposition so Wave C knows where to anchor them. This part is therefore partially a Phase-A stub (relationship tracking is operational; external integrations are a Phase-B/C materialisation surface). Popper falsifier: yes — without this part, K and L categories are unanchored in Foundation, CRM is an orphan sub-system, and external integration discipline has no home.

**FPF anchor.** FPF IP-2 (Context-is-king — the CRM's bounded context is explicitly relationship-management for the generic knowledge-worker owner; DACH-specific ICP bindings are RUSLAN-LAYER); FPF A.14 typed edges for CRM-to-wiki graph (8 CRM edge types per CLAUDE.md CRM System section); FPF A.1 (relationship records are U.Episteme; the CRM pipeline managing state transitions is U.System).

**D-Lock anchor.** D17 (Filesystem = SoT — CRM records are filesystem-first; Notion is a view [FUNDAMENTAL UC-L.1-L.2 "read-only intelligence trackers"]); D27 (CRM schema must be forkable with ICP parameters externalized from Foundation); **FUNDAMENTAL §6.4 (privacy and data ethics — CRM is the only Foundation part that explicitly stores data about third parties; therefore generic privacy principles apply structurally: consent-respected, forget-request compliance, sensitive-info encrypted at rest, cross-context awareness, NO inference of protected characteristics — religion / sexuality / health / political views)**.

**A-1 critic correction (FLAG-MINOR resolved 2026-04-27):** Per FUNDAMENTAL §6.4 + pre-read PP-7, original D-Lock anchors omitted §6.4 privacy reference. Required because Part 10 is the structural home of third-party data; without explicit citation, Wave C interface card may omit privacy architecture. [src:A-1-critic-gate.md:§6 item 5]

**AUDIT artefact mapping.** `crm/` tree (24 source files); `crm/_schema/` (frontmatter / roles / statuses / strategy-hooks YAMLs); `crm/_scripts/crm.py`; 10 `/crm-*` skills; 35 unit tests; `crm/log.md`; `crm/_scripts/voice_router.py` (cycle-11 wire). [src:CLAUDE.md:CRM System section]

**Originating expert.** Engineering-expert noted CRM (cycle 10) as existing working part [engineering-expert.md:§4 Ambiguity 3]. No expert proposed a standalone K or L part. K.1-K.3, L.1-L.3 gap addressed here by combining CRM (operational) with the external integrations stub (Phase-B).

**Cycles 3b/10/11 reuse?** CRM cycle-10 fully operational. Voice-to-CRM wire (cycle 11) operational. Do NOT reinvent. External integration adapter pattern is NOT yet operational — Wave C stub needed. [src:cycle-artefact-register.md:§6.2]

---

## §3 Cross-cutting Concerns (Not Parts)

The following candidates were proposed as parts by at least one expert but resolved to cross-cutting disciplines that every part adheres to. They are named here to prevent them from being re-introduced as parts in Wave C.

**1. Git/Filesystem Discipline (Company-as-Code D25).** Engineering-expert proposed "System Substrate" as a standalone part. Resolution: git discipline is a pervasive infrastructure constraint (all 10 parts commit their state through the same git interface) but does not have an independent lifecycle or artifact type beyond "write to this repo." It is enforced via Part 6 (Governance & Human Gate) and the commit conventions declared in `CLAUDE.md`. Not a part — a discipline. Every Foundation interface card's Effects (E lane) must declare the git-commit artifact that corresponds to each state change. [src:engineering-expert.md:§3 Ambiguity 2]

**2. Provenance Tagging (F-G-R and inline [src:...]).** Investor-expert proposed "Provenance + Audit-Trail Substrate" as a standalone part. Engineering-expert echoed this. Resolution per OQ-PHIL-2: provenance is a cross-cutting discipline embedded in every other part's Effects (E lane) specification. The tagging format (`[src:path#section]`, frontmatter `sources:`, F-G-R fields) is universal. Part 6 (Governance) owns the compliance enforcement and audit; Part 1 (System State Persistence) owns the durable storage. Making provenance a separate part would create an unhelpful hub that every other part routes through for tagging — instead, every part's interface card includes a mandatory provenance section. [src:philosophy-expert.md:OQ-PHIL-2]

**3. Operational Rhythm / Cadence (40/10/40/10).** Mgmt-expert proposed "Operational Rhythm Layer" as a standalone part. Resolution: the 40/10/40/10 cadence is a scheduling pattern that every part adheres to, not a module with its own data. The cycle ritual is owned by Part 5 (Compound Learning); the owner's daily/weekly interaction with the rhythm is owned by Part 9 (Owner Interaction Scaffold); the health signals from the cadence are owned by Part 8 (Health Monitoring). The cadence itself is a cross-cutting temporal discipline. [src:mgmt-expert.md:OQ-MGMT-2]

**4. Append-Only Log Pattern.** Every part that produces state must do so in append-only fashion (mailboxes, log.md, strategies.md, edges.jsonl, approval-log). This is an architectural invariant inherited from FUNDAMENTAL §2.1 ("Three cross-cutting substrates") and D25. It is not a part — it is a write discipline that every part's interface card declares in its Deontics (D lane): "MUST append; MUST NOT mutate existing records." [src:engineering-expert.md:§3 "Append-only substrate"]

**5. IP-1 Role≠Executor Discipline.** Philosophy PP-1 is a constitutional discipline that every part involving agents must respect — separating role manifests (U.Episteme) from executor bindings (RUSLAN-LAYER). This is enforced through Part 4 (Role Taxonomy & Coordination Protocol) structurally and through Part 6 (Governance) as an audit check. Not a standalone part — a constitutional constraint woven into every agent-involving part's interface card. [src:philosophy-expert.md:PP-1]

---

## §4 Mapping to Existing 14-Layer SYSTEM-OVERVIEW

Quick mapping of 10 Foundation parts to the 14 layers (L0-L9 + L-R/L-C/L-B/L-P) from `decisions/JETIX-SYSTEM-OVERVIEW.md`. Foundation does not restart from blank — it supersedes / consolidates / reframes.

| Foundation Part | Maps to SYSTEM-OVERVIEW Layer(s) | Relationship |
|---|---|---|
| Part 1 — System State Persistence | L0 (Foundation Layer — git, configs, schemas) | Supersedes: Foundation gives L0 its own interface card and Wave-C work-list. L0 description remains valid. |
| Part 2 — Signal Ingestion & Triage | L2 (Knowledge Ingest Layer) | Supersedes and clarifies: Part 2 gives L2 explicit STOP gate + D28 anchor enforcement as structural requirements (not soft conventions). |
| Part 3 — Knowledge Base & Methodology Library | L1 (Knowledge Base Layer) + L3 (Synthesis/Compound Layer, partial) | Consolidates: L1 (wiki KB) + the methodology library sub-layer from L3. Clarifies that L3's compounding function is split: methodology-capture goes to Part 3; compound ritual goes to Part 5; synthesis query goes to Part 3 via /ask. |
| Part 4 — Role Taxonomy & Coordination Protocol | L4 (Agent Layer, partial) | Refines: extracts the protocol/schema sub-system from L4's God-object (per engineering-expert AP-ENG [engineering-expert.md:§1 "Fowler refactoring smells" — L4 God object]). L4 becomes the executor-layer; Part 4 is the protocol-layer. |
| Part 5 — Compound Learning & Methodology Capture | L3 (Synthesis/Compound Layer, partial) + Layer-2 memory (strategies.md) | Refines: extracts the compound-ritual sub-system from L3. L3 dissolves into Part 3 (KB/methodology) and Part 5 (compound engine). [src:engineering-expert.md:§4 Ambiguity 4] |
| Part 6 — Governance, Provenance & Human Gate | L9 (Governance Layer) + L0 (partial — git provenance) | Consolidates: unifies L0 git-as-provenance with L9 AWAITING-APPROVAL gates into one part. Eliminates the artificial split between infrastructure-provenance and governance-gates. [src:engineering-expert.md:§1 "Fowler smells" duplication L0/L9] |
| Part 7 — Project Lifecycle Substrate | L8 (Project Layer, if exists) | New: SYSTEM-OVERVIEW does not have an explicit project lifecycle layer. Part 7 is a Foundation addition not present in the 14-layer model. Motivated by UC-D.1 and D26. |
| Part 8 — Health Monitoring & System Integrity | L5-L6 partial (Resource + Compute cross-cutting concerns) + L9 (partial) | New: health monitoring as an owned part is not in SYSTEM-OVERVIEW. It is currently distributed across L3 (strategies), L4 (agent metrics), L9 (governance gates). Part 8 consolidates these. |
| Part 9 — Owner Interaction Scaffold | L7 (Daily Operations Layer) | Supersedes and clarifies: gives L7 an explicit owner-interaction interface schema, approval SLA taxonomy, and UC-A/J mapping. |
| Part 10 — External Touchpoints & Network Interface | L-R (Resource cross-cutting, partial) + implicit CRM layer | New: CRM and external integrations are not explicit layers in SYSTEM-OVERVIEW. Part 10 surfaces them as a Foundation part. |

**Summary of divergence from SYSTEM-OVERVIEW.** Foundation parts are 10 capability-boundary decompositions vs 14 vertical-stack layers. Key changes: (a) L3 dissolved into Parts 3 and 5; (b) L0 and L9 consolidated into Part 6; (c) Part 7 (Project Lifecycle) and Part 8 (Health Monitoring) are new additions not in the 14-layer model; (d) Part 10 (External Touchpoints) surfaces CRM and integrations that were implicit in SYSTEM-OVERVIEW. The 14-layer model remains valid as an implementation-view description; the 10-part Foundation is the capability-boundary decomposition that the 14-layer model implements. [src:engineering-expert.md:§4 Ambiguity 1]

---

## §5 Coverage Matrix — Foundation Parts × FUNDAMENTAL UC Categories A-L

| Part | A | B | C | D | E | F | G | H | I | J | K | L |
|------|---|---|---|---|---|---|---|---|---|---|---|---|
| Part 1 — System State Persistence | | | | | | | | H.1 H.2 H.3 | | | | |
| Part 2 — Signal Ingestion & Triage | | B.1 B.5 | | | | | G.1 G.2 | | | | | |
| Part 3 — KB & Methodology Library | | B.2 B.3 B.4 | C.2 C.3 | | | F.1 F.2 | | | | | | |
| Part 4 — Role Taxonomy & Coordination | | | | | E.1 E.2 E.3 | | | | | | | |
| Part 5 — Compound Learning | | | C.1 C.2 C.3 | | E.2 | F.1 F.2 | | | | | | |
| Part 6 — Governance & Human Gate | A.3 A.4 | | | | | | | H.4 H.5 | I.4 | | | |
| Part 7 — Project Lifecycle | | | | D.1 D.2 | | | | H.5 | | | | |
| Part 8 — Health Monitoring | | | | | | | | H.4 | I.1 I.2 I.3 I.4 | | | |
| Part 9 — Owner Interaction Scaffold | A.1 A.2 A.3 | | | | | | | | I.1 I.2 | J.1 J.2 J.3 | | |
| Part 10 — External Touchpoints | | | | | | | G.2 | | | | K.1 K.2 K.3 | L.1 L.2 L.3 |

**Coverage check — every UC category must map to at least one part:**

| Category | Status | Parts |
|---|---|---|
| A — Strategic Management | Covered | Parts 6, 9 |
| B — Information Lifecycle | Covered | Parts 2, 3 |
| C — Self-Improvement & Learning | Covered | Parts 3, 5 |
| D — Project & Resource Management | Covered | Part 7 |
| E — Agent Swarm Operations | Covered | Part 4 |
| F — AI Augmentation Continuity | Covered | Parts 3, 5 |
| G — Multi-channel Access | Covered | Parts 2, 10 |
| H — Foundation & Reliability | Covered | Parts 1, 6, 7, 8 |
| I — Continuous Health & Self-Improvement | Covered | Parts 6, 8, 9 |
| J — Daily Operations | Covered | Part 9 |
| K — CRM / Network Tracking | Covered | Part 10 |
| L — External Integrations | Covered | Part 10 |

**No orphan UC categories detected.** All 12 FUNDAMENTAL categories A-L map to at least one part. ✓

---

## §6 Open Questions for Brigadier

**OQ-MERGED-1 (from OQ-PHIL-2, investor Q2): Provenance as cross-cutting vs standalone.**
This integration resolves provenance as cross-cutting (§3 item 2). If the philosophy-expert critic pass disagrees and argues Part 6 is too large (conflating human-gate enforcement with F-G-R tagging into one part), the split would be: Part 6a = F-G-R tagging schema + provenance audit (U.Episteme-adjacent); Part 6b = human-gate enforcement + AWAITING-APPROVAL mechanism (U.System). This would push the count to 11 parts — still within range. Ruslan ack needed if split is preferred over consolidated.

**OQ-MERGED-2 (from engineering-expert Ambiguity 4): Compound Learning Engine vs Protocol within Agent Coordination.**
Engineering-expert argued the compound learning ritual dissolves across Parts 2, 4, and 6 rather than being a standalone part. This integration preserves Part 5 as standalone, grounded in the R2 reinforcing loop (distinct from Part 4's coordination function) and the Kauffman adjacent-possible growth mechanic (Part 5 is what expands what's adjacent-possible, not Part 4 which merely coordinates the current adjacent-possible). If brigadier finds Part 5's Wave-C work-list collapses into Parts 3 and 4 without residue, it can be dissolved. Surface to Ruslan.

**OQ-MERGED-3 (from investor Q5): Fork-and-merge separation surface.**
Part 10 (External Touchpoints) is the highest-risk part for Ruslan-specific content leaking into Foundation — CRM pipeline stages, ICP scoring weights, outreach templates. The fork-separation checklist (per investor Q5) should be a Wave A or Wave C deliverable. Recommendation: include a per-part "fork-separation declaration" in each Wave C interface card (what is parameterized for RUSLAN-LAYER vs what is Foundation-invariant). Ruslan ack on whether this is Wave A scope (add to MASTER-PLAN-DRAFT §5 Open Q) or Wave C scope (add to each interface card template).

**OQ-MERGED-4 (from mgmt OQ-MGMT-1): Product management / continuous discovery at Foundation level.**
Torres CDH (opportunity-solution loop) and continuous discovery are NOT represented in the 10-part decomposition. The integration resolves this as RUSLAN-LAYER (ICP-specific opportunity framing). However, if a generic "Discovery Substrate" (opportunity → solution tree discipline without specific ICP content) belongs in Foundation, it would likely sit inside Part 9 (Owner Interaction Scaffold) as a sub-function — the weekly strategic review is the natural home. Ruslan ack needed: is a generic discovery/CDH sub-function in Part 9 in scope for Foundation?

**OQ-MERGED-5 (from systems OQ-SYS-5): Health Monitoring materialisation gate.**
Systems-expert flagged that SYSTEM-OVERVIEW's L5-L9 are spec'd but not operational. Part 8 (Health Monitoring) has no existing operational substrate beyond `system-health.json` (reports "all green" with no computation mechanism) and disconnected lint/company-status tools. Wave C materialisation of Part 8 may be Phase-B scope (after Foundation spec is complete) rather than immediate Wave C. Brigadier should flag in MASTER-PLAN-DRAFT §5 Open Q: is Part 8 a "specify and stub" Wave C task, or a "specify and implement" Wave C task?

**OQ-MERGED-6 (from investor Q1 + OQ-PHIL-4): Blast-radius categorization — Foundation primitive or RUSLAN-LAYER?**
The J-level decision matrix (J-Auto / J-Approve / J-Strategic) lives in Part 6. OQ-PHIL-4 asks whether Foundation needs an explicit "blast-radius classification" sub-function for novel/unclassified actions. The integration recommends yes — this sub-function belongs in Part 6 as a "Default-Deny classifier" that maps novel actions to J-Strategic pending explicit categorization. Whether the founder-absence delegation protocol (investor Q1) belongs in Foundation or RUSLAN-LAYER: recommend Foundation defines the protocol template and decision-class taxonomy; RUSLAN-LAYER fills specific delegation targets. Ruslan ack on both.

**OQ-MERGED-7: U.System vs U.Episteme full declaration.**
OQ-PHIL-1 asks whether Foundation should enumerate which candidate parts are U.System vs U.Episteme vs dual, or leave this to Wave C per-part architecture. This integration provides a declaration for each of the 10 parts (see §2 above). If the philosophy-expert critic pass finds any declaration incorrect or insufficiently precise, the affected part's Wave C interface card must correct it before Phase A-2 (interface cards). Ruslan ack: is the U.System/U.Episteme declaration in this document sufficient for Phase A-2, or does it require an additional philosophy-expert critic pass before A-2 proceeds?

---

## §7 Provenance

All claims in this document trace to the following sources. Format: `[<expert-pre-read>:§N]` or `[<source-doc>:§Y]`.

| Claim / decision | Source |
|---|---|
| 20 candidate parts from 4 experts | brigadier convergence summary (in dispatch brief) |
| Popper falsifier test as deduplication criterion | [philosophy-expert.md:§1 Falsifiability check] |
| AP-1 through AP-5 anti-patterns applied | [philosophy-expert.md:§3 Candidate Main Parts Anti-patterns] |
| PP-1 through PP-7 pressure points applied | [philosophy-expert.md:§2 Constitutional Pressure Points] |
| Ruslan-creep leak risks applied | [philosophy-expert.md:§4 Where Ruslan-specific Creep is Likely] |
| Part 1 (System State Persistence) | [engineering-expert.md:§2 Part 1]; [investor-expert.md:§1 D25 "Lindy substrate"] |
| Part 2 (Signal Ingestion & Triage) | [engineering-expert.md:§2 Part 3]; [systems-expert.md:§2 Part 1 partial] |
| Part 3 (KB & Methodology Library) | [engineering-expert.md:§2 Part 2]; [systems-expert.md:§2 Part 1]; [investor-expert.md:§2 Part 2] |
| Part 4 (Role Taxonomy & Coordination Protocol) | [engineering-expert.md:§2 Part 4]; [systems-expert.md:§2 Part 2]; [mgmt-expert.md:§2 Part 4]; [investor-expert.md:§2 Part 3] |
| Part 5 (Compound Learning & Methodology Capture) | [systems-expert.md:§2 Part 5]; [investor-expert.md:§1 "Agent Strategies Ledger"] |
| Part 6 (Governance, Provenance & Human Gate) | [engineering-expert.md:§2 Part 5]; [systems-expert.md:§2 Part 3]; [investor-expert.md:§2 Part 1, Part 5]; [philosophy-expert.md:PP-4, PP-5, PP-7, OQ-PHIL-2] |
| Part 7 (Project Lifecycle Substrate) | [mgmt-expert.md:§2 Part 3] |
| Part 8 (Health Monitoring & System Integrity) | [systems-expert.md:§2 Part 4]; [mgmt-expert.md:§2 Part 5]; [investor-expert.md:§2 Part 4] |
| Part 9 (Owner Interaction Scaffold) | [mgmt-expert.md:§2 Part 2]; UC A.1-A.3 gap resolution |
| Part 10 (External Touchpoints & Network Interface) | [engineering-expert.md:§4 Ambiguity 3]; UC K.1-K.3, L.1-L.3, G.2 gap resolution; [CLAUDE.md:CRM System section] |
| Cross-cutting concern: git discipline | [engineering-expert.md:§3 Ambiguity 2]; [philosophy-expert.md:PP-5 D25] |
| Cross-cutting concern: provenance tagging | [philosophy-expert.md:OQ-PHIL-2]; [investor-expert.md:§2 Part 1] |
| Cross-cutting concern: operational rhythm | [mgmt-expert.md:OQ-MGMT-2] |
| Cross-cutting concern: append-only log pattern | [engineering-expert.md:§3 "Append-only substrate"]; [FUNDAMENTAL §2.1] |
| Cross-cutting concern: IP-1 Role≠Executor discipline | [philosophy-expert.md:PP-1]; [FPF §5.1 IP-1] |
| SYSTEM-OVERVIEW mapping — L3 dissolved | [engineering-expert.md:§4 Ambiguity 4] |
| SYSTEM-OVERVIEW mapping — L0/L9 consolidated | [engineering-expert.md:§1 "Fowler refactoring smells"] |
| G.1-G.2 gap addressed in Part 2 | no expert proposed standalone; systems-expert OQ-SYS-3 flagged L-category as adjacent-possible only at Phase 2+ |
| F.1-F.2 gap addressed in Parts 3, 5 | no expert proposed standalone; resolved through strategies.md (Part 5) + KB persistent memory (Part 3) |
| A.1-A.3 gap addressed in Parts 6, 9 | no expert proposed standalone; resolved through governance audit trail (Part 6) + owner interaction scaffold (Part 9) |
| K.1-K.3 gap addressed in Part 10 | [engineering-expert.md:§4 Ambiguity 3]; CRM cycle-10 operational |
| L.1-L.3 gap addressed in Part 10 | no expert proposed standalone; Part 10 is Phase-A stub for L-category |
| U.System vs U.Episteme declarations per part | [philosophy-expert.md:OQ-PHIL-1]; [FPF §1.4 A.1 agency rule] |
| Cycle artefact reuse declarations | [cycle-artefact-register.md:§6.2] |
| 14-layer divergence analysis | [engineering-expert.md:§4 Ambiguity 1] |
| VSM Level-3 → Part 8 mapping | [systems-expert.md:§1 VSM viability] |
| R1/R2 loop placement | [systems-expert.md:§1 Feedback loops] |
| Senge Law 7 → Part 5 rationale | [systems-expert.md:§1 Senge laws] |
| Kauffman adjacent-possible → Part 5 rationale | [systems-expert.md:§1 Adjacent-possible] |
| Munger inversion → Part 8 rationale | [investor-expert.md:§1 Marks second-level thinking] |
| Barbell structure — safe substrate + experiments | [investor-expert.md:§1 Taleb barbell] |
| Via-negativa: FUNDAMENTAL §6 anti-scope 50+ rules | [investor-expert.md:§1 Via-negativa]; [FUNDAMENTAL §6] |
| D26 Team 50-100 scaling constraint | [mgmt-expert.md:§3 D26 "Team 50-100"] |
| 3-tier approval SLA (L1/L2/L3) placement in Part 9 | [mgmt-expert.md:§3 "3-tier approval SLA"] |
| Karpathy LLM Wiki substrate principles | [engineering-expert.md:§1 "Karpathy LLM Wiki substrate"] |

---

*Dissents preserved:*

```yaml
dissents:
  - source: engineering-expert × integrator (§4 Ambiguity 4)
    claim: "Compound Learning Engine (Part 5) should dissolve across Parts 3 and 4 rather than exist as standalone"
    F: F3
    ClaimScope: "Holds if the compound ritual's primary product is KB entries and protocol updates with no distinct ritual artifact type"
    R: "Refuted if Wave C interface card work confirms DRR ledger and strategies.md files are not naturally owned by Part 3 or Part 4; accepted if Wave C dissolves Part 5 without residue"
  - source: engineering-expert × integrator (§4 Ambiguity 5)
    claim: "Health monitoring is a cross-cutting concern deserving a thin dedicated layer, not a heavyweight standalone part"
    F: F3
    ClaimScope: "Holds if the SLI/SLO schema and health artifact type are lightweight enough to be embedded in every other part's Effects spec"
    R: "Refuted if Wave C reveals health monitoring requires its own compound lifecycle (daily lint → weekly checkup → monthly deep review → quarterly immune audit) that cannot be distributed without losing ownership"
```
