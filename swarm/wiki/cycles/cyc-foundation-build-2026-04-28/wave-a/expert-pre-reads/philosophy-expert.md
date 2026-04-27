---
title: Philosophy-expert pre-read — Foundation constitutional pressure points (critic mode)
date: 2026-04-27
phase: A-0
expert: philosophy-expert
mode: critic
cycle: cyc-foundation-build-2026-04-28
formality: F2
claim_scope: foundation-decomposition/constitutional-audit
reliability: R-medium
sources:
  - design/JETIX-FPF.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/LOCKS-D29-ADDENDUM-2026-04-26.md
---

# Philosophy-expert Pre-read (Critic Lens)

## §1 Read Summary

### IP-1..IP-8 — what each REALLY means for Foundation decomposition

**IP-1 (Role ≠ Executor strict separation) [FPF §5.1].** The deepest of the 8 principles for Foundation architecture purposes. It does not mean "name your agents properly." It means that any Foundation "part" whose primary function involves agents MUST distinguish between the *role manifest* (method signature, output kinds, decision-class authority) and the *executor binding* (which model instance fills it in which cycle). Concretely: a Foundation part called something like "Agent Swarm Coordination" is not a part at all in Левенчук's sense — it silently conflates the role taxonomy (what roles exist, what methods they carry) with the operational coordinator logic (who is dispatched, how tasks flow). The A.2 Role Taxonomy and F.6 Role Assignment & Enactment Cycle are separate concerns from the coordination protocol. Foundation must honour this split structurally, not only lexically.

**IP-2 (Context is king) [FPF §5.2, A.1.1 U.BoundedContext].** Every Foundation part must declare its bounded context explicitly. Cross-context reuse (e.g., a "CRM" part reused by Life-OS layer) must go through an explicit Bridge (F.9) with a Congruence Level and documented loss. The anti-pattern for Foundation: defining parts at a "universal" granularity that silently assumes Jetix operational context (DACH, Phase 1, 11 agents) while claiming to be generic FUNDAMENTAL. IP-2 is the reason FUNDAMENTAL §0 distinguishes Layer 1 (generic) from Layer 2 (Ruslan-specific). Foundation decomposition must declare: "this part's bounded context is the generic knowledge-worker system, not Jetix-specific."

**IP-3 (Artifacts over conversations) [FPF §5.3].** For Foundation architecture specifically: every Foundation part MUST produce committed file artifacts as its primary output, not ephemeral synthesis that lives only in a session. The Левенчук warning [FPF §5.3 anti-pattern citation, ailev/1769411] is explicit: if the LLM writes the "thinking," writing-as-thinking disappears as cognitive process. For Foundation: the KM part must produce wiki entries and edges.jsonl updates (artifacts), not just "search results." The agent swarm coordination part must produce cycle-log.md entries and provenance trails. IP-3 is not merely operational hygiene — it is what makes the system reconstructable from git history, which is D25's underlying requirement [D25].

**IP-4 (Meta-agent as immune system) [FPF §5.4].** Foundation must include an ontological integrity function — not necessarily a separate "part," but a dedicated responsibility that runs quarterly audits on: alpha/entity/work-product classification drift; past-participle convention; role-manifest structural integrity; F-G-R compliance; A.14 edge-type verification; CHR space integrity. If Foundation decomposes this as a standalone "Governance" part, it must be the bearer of this immune function. If it folds governance into another part, the immune function risks being lost under operational load. The steward role separating trigger [FPF §5.4: 30+ agents OR 1+ human meta-hire OR quarterly audit burden >4h] is a falsifiable threshold Foundation must architect around.

**IP-5 (Explicit alpha state transitions — past-participle discipline) [FPF §5.5, §5.5a].** Foundation must include a lifecycle tracking mechanism where every alpha's state is a past-participle or a whitelisted in-X/under-X compound (with documented semantic justification). A Foundation "Project Management" part that allows states like "qualifying" or "in progress" without whitelisting violates IP-5. The five whitelisted exceptions [FPF §5.5a] are not generic — they are Jetix-specific. A generic Foundation part must declare its own exception list for the archetypes it serves, grounded in the same semantic criterion: "the past-participle sibling would collapse semantically distinct terminal states."

**IP-6 (No role left undefined — 5-block role.md mandatory) [FPF §5.6].** Foundation's role-definition part must enforce the 5-block structure: identity / ontological-positioning / method / production-dependencies / evolution. Any Foundation part that allows role "definitions" outside this structure creates drift. Concretely: a Foundation "Agent Onboarding" part that writes system prompts without a corresponding role.md Block 3 (primary_method + method_description_ref) violates IP-6. The 5-block structure is the anti-pattern prevention mechanism for "Claude Agent #3 as role name" [FPF §5.1 anti-pattern].

**IP-7 (Writing as thinking) [FPF §5.7].** Foundation must structurally support Ruslan as primary author of strategic artifacts, with agents in support role, not substitution role. The quality criteria are concrete [FPF §5.7]: artifact author discovers something new during writing; text contains ontologically typed objects; text reveals contradictions not visible pre-writing. A Foundation "Knowledge Management" part that automates synthesis without requiring human authorship of strategic documents violates IP-7. The mechanism: every strategic document has a human as primary author; agents contribute structured extractions and alternatives.

**IP-8 (Agents as new participants — F.6 6-step onboarding) [FPF §5.8].** Foundation's agent onboarding sub-function must implement the F.6 6-step cycle: M1 Locate (which bounded context) / M2 Stance (design vs run) / M3 Qualify (holder eligibility) / M4 Bind/Assert (the executor-binding.yaml artifact itself) / M5 Evidence (warm-up task shape) / M6 Conclude (promotion threshold). A Foundation part that skips M3-M4 (qualification + binding) treats agents as tools, not role-filling participants, violating IP-8 in the Левенчук sense.

### Architectural invariants for Foundation decomposition

**A.1 Holonic Foundation [FPF §12.1, §1.1-1.7].** Every Foundation "part" must be a holon — simultaneously a whole with its own boundary AND a part of the larger Foundation. This has a concrete implication that is frequently violated: a "flat" decomposition where parts are merely functional modules without their own lifecycle, state machine, or boundary definition violates A.1. Each Foundation part must declare: (a) its U.Boundary, (b) whether it is primarily U.System (operational, produces effects) or U.Episteme (passive knowledge content, transformed only by external actors), and (c) how it participates in the Nested Holonic Structure [FPF §1.7]. The U.Episteme distinction is critical: wiki entries are U.Episteme (passive); the agent that writes them is U.System. A Foundation part that blurs this (e.g., a "Knowledge part" that simultaneously stores and acts) violates A.1 Agency Rule [FPF §1.4].

**A.14 Typed mereology [FPF §3.5, §12 reference].** Dependency edges between Foundation parts MUST be typed. The 6 canonical A.14 edges (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf) plus the 4 Jetix-specific edges (creates / operates-in / methodologically-uses / constrained-by) are the available vocabulary. A Foundation dependency graph that uses "depends-on" or "uses" as edge labels violates A.14 and makes the dependency semantics unverifiable. Concretely: if Part X "depends on" Part Y, what does that mean? Is X a ComponentOf Y? Does X methodologically-uses Y? The distinction matters for understanding what happens when Y changes or fails.

**A.6.B L/A/D/E lane discipline [FPF §4.3, §12.9].** Every Foundation interface card must split its specification into 4 lanes: Laws (invariants that must hold — not optional), Admissibility (acceptance criteria — what the consuming part expects), Deontics (obligations and permissions — what each side must/may/must-not do), Effects (measurable outcomes — SLAs, deliverable specifications). An interface card that lists only "inputs" and "outputs" without L/A/D/E violates A.6.B. The anti-pattern is conflating obligations (D) with effects (E): "the KM part must produce wiki entries and also the entries must be ≥300 words" — the first is D (obligation), the second is E (measurable outcome). They require different enforcement mechanisms.

**A.13 Agency-CHR [FPF §2.1a, §12 reference, §5.10.4].** Agent autonomy in Foundation is bounded by per-decision-class j_level (J-Auto / J-Approve / J-Strategic). The "AI agents don't strategize" hard rule [FPF §5.10.4, FUNDAMENTAL §6.1] applies universally: no Foundation part may grant agents J-Strategic authority. Foundation's access-control part must encode this as a structural constraint, not a behavioral guideline. Concretely: the Agency-CHR profile dimensions (bmc / ph / mp / per / oc) must be declared per role per decision-class, stored in two locations (policy defaults + executor-binding overrides) [FPF §2.1a canonical schema], and auditable by the immune-system function (IP-4).

**B.3 F-G-R triad [FPF §12.7, §4.2].** Every Foundation artifact must carry F-G-R tags: Formality (F0-F9), claim-Scope (G — the bounded context where the claim holds), Reliability (R-low/medium/high/certified). Foundation's provenance part must enforce this as a structural requirement, not a convention. The practical failure mode: F-G-R exists in the constitutional document but is never applied to wiki entries, strategy drafts, or agent outputs because no Foundation part owns the enforcement mechanism. The FPF-Steward quarterly audit [FPF §5.4] must check F-G-R compliance across all artifact types — this check must be assigned to a specific Foundation part with a specific audit cadence.

### Falsifiability check (Popper P1)

The Foundation decomposition is itself a set of claims. Each claim ("Part X is a necessary part of Foundation") must be falsifiable. The falsifier for a proposed Foundation part: "If this part did not exist as a separate part, what observable system behavior would degrade?" If no observable degrades — the part is not a part in the mereological sense, it is a concern that belongs inside another part. This test should be applied to every candidate part in Phase A-1.

### Paradigm awareness (Kuhn P2)

FUNDAMENTAL was authored drawing on multiple research programmes simultaneously: Левенчук ШСМ / FPF (its own paradigm with specific ontology), multi-agent architecture research (Anthropic, Cognition, arxiv — their own paradigm with different vocabulary), Karpathy LLM Wiki (yet another paradigm for KM). These paradigms use the same words for different concepts: "role" in Левенчук means method-signature + interest + mastery; "role" in multi-agent architecture often means "agent persona." Foundation decomposition that silently mixes these paradigms will produce interface cards that appear coherent but are semantically inconsistent across the boundary. Each Foundation part must declare which paradigm's vocabulary it uses, and Bridges must be explicit at cross-paradigm boundaries.

### Engineering knowledge categories (Vincenti P7)

Foundation content spans at least 4 Vincenti categories: fundamental design concepts (the holonic structure, the role/executor split), criteria and specifications (F-G-R tagging, L/A/D/E lanes, past-participle states), theoretical tools (A.14 mereology, B.3 F-G-R calculus, A.13 Agency-CHR), and practical considerations (git commit conventions, mailbox protocols, context budget management). Foundation parts that mix these categories silently will produce interface cards where enforcement mechanisms are undefined — you cannot test compliance with a "fundamental design concept" the same way you test compliance with a "specification."

---

## §2 Constitutional Pressure Points

### PP-1 — Role≠Executor wall: agents are not parts

**What:** [FPF §5.1 IP-1] Role is a method signature and interest. Executor is an instance binding. Any Foundation decomposition that names an agent (coordinator, brigadier, meta-agent) as a constituent part rather than a role-filling-executor violates IP-1.

**Why non-negotiable:** FPF A.1 agency rule [FPF §1.4] states behavioral roles attach ONLY to U.System bearers; U.Episteme is passive. If a Foundation "part" is defined as "the brigadier agent does X," the part's behavior is tied to a specific executor instance. When the executor changes (model upgrade, role rebinding), the Foundation part appears to change identity. This is the Левенчук "Claude Agent #3 as role name" anti-pattern [FPF §5.1] operationalised at the architectural level.

**Where typically violated:** "Agent Swarm" as a Foundation part, where the part's description lists which agents do what, rather than which roles carry which methods under which decision-class authority. "Coordination layer" defined as "brigadier coordinates" rather than "hub-and-spoke role-coordination method, filled by the coordinator role instance."

**What architecture must do:** Foundation parts that involve agents must separate (a) the role taxonomy sub-part (what roles exist, what methods they carry, what decision-class authority they have) from (b) the operational coordination sub-part (how tasks are dispatched, how mailboxes route messages, how escalations trigger). The executor-binding.yaml mechanism [FPF §5.8.1] must be a concrete deliverable of the role-taxonomy sub-part, not an afterthought. Role rebinding (e.g., replacing Sonnet 4.6 brigadier with Opus brigadier) must require only an executor-binding.yaml change, not a Foundation architecture change.

### PP-2 — IP-2 Context-is-king: Foundation ≠ Jetix-specific

**What:** [FPF §5.2, FUNDAMENTAL §0] Foundation is generic (Layer 1). Every Foundation part must function for a generic knowledge worker, not only for Ruslan-as-DACH-AI-consultant.

**Why non-negotiable:** FUNDAMENTAL explicitly states [FUNDAMENTAL §0]: "Если завтра Ruslan уйдёт в другую нишу → меняется только RUSLAN-LAYER, FUNDAMENTAL остаётся." A Foundation part that references DACH, Mittelstand, €50K, 11 specific archetypes, or Ruslan's specific role sub-manifests is in RUSLAN-LAYER territory, not Foundation. IP-2's U.BoundedContext [FPF §5.2] requires explicit context declaration — "this part holds in: generic-professional-knowledge-worker context; NOT in: Jetix-DACH-Phase-1 specific context."

**Where typically violated:** The 5-tier access control model [FUNDAMENTAL §7.4] is described generically (T0-Founder / T1-trusted-agents / etc.) — this is Foundation-eligible. But if the interface card for an "Access Control" part references specific agent IDs (sales-lead, brigadier) rather than generic role-tier bindings, it has leaked into RUSLAN-LAYER. The 11 archetypes [FUNDAMENTAL §7.1.1] are presented as generic — they are Foundation-eligible as a taxonomy. But if a "CRM" Foundation part encodes Mittelstand-specific ICP scoring, it has leaked. The Agency-CHR policy template [FPF §2.1a] is generic — Foundation-eligible. The specific CHR values for Jetix's 11 agents are RUSLAN-LAYER.

**What architecture must do:** Every Foundation part interface card must pass a boundary heuristic [deep-prompt §8 R3]: "Would a professional knowledge worker in a different domain (researcher, investor, politician, engineer per FUNDAMENTAL §7.1.1) also need this part?" If yes — Foundation. If only Ruslan — RUSLAN-LAYER. Brigadier must enforce this as a gate in Phase A-1.

### PP-3 — A.14 typed mereology: no flat "depends-on" dependency graph

**What:** [FPF §3.5, A.14] Dependencies between Foundation parts must be typed with specific A.14 edge types, not generic "depends-on."

**Why non-negotiable:** The mereology-edge-types semantic firewall [FPF §3.5, decisions/policy/mereology-edge-types.md] exists because different edge types have different change-propagation semantics. If Part X is ComponentOf Part Y, removing X breaks Y's structural integrity. If X methodologically-uses Y, X can swap Y for an equivalent method without structural breakage. If X operates-in Y (Part X is a supersystem context for Y), then Y is operationally dependent on X's existence. A flat "depends-on" graph obscures which kind of dependency it is, making the dependency graph unactionable for resilience planning or phased implementation.

**Where typically violated:** The typical Foundation dependency graph lists "Information Lifecycle depends on Knowledge Management" without specifying: does IL ComponentOf KM? Does IL methodologically-use KM's indexing function? Does IL operate-in KM as a supersystem? These have different implications for what gets built first, what can fail gracefully, and what is a hard architectural coupling vs a soft methodological dependency.

**What architecture must do:** The dependency graph in Phase A-2 must use only A.14 canonical + Jetix-specific typed edges (the 10-edge vocabulary from FPF §3.5). Every edge in the graph carries an edge-type label. The mereology-edge-types.md anti-pattern guide [FPF §3.5 reference] must be consulted before each edge is drawn. The systems-expert (scalability-architect mode) dependency graph review in Phase A-2 must check for unlabeled "depends-on" edges.

### PP-4 — Anti-scope §6.1 agents-don't-strategize: must be architecture-enforced, not behavioral

**What:** [FUNDAMENTAL §6.1, FPF §5.10.4] Agents do not make strategic decisions, architectural decisions, or skill-direction decisions. This is a constitutional hard rule, not a best-practice guideline.

**Why non-negotiable:** FUNDAMENTAL §6.7 specifies: "AI попытался strategize → halt + log + alert founder." This is not "AI should not strategize" — it is "if AI strategizes, halt the entire action." Foundation's access-control / governance part must implement this as a mechanism (J-Strategic decision-class = founder-only, enforced at message-schema level via the acting_as field), not as a convention. The Левенчук grounding [FPF §5.10.4]: "No identity / no commitment / no long-term memory / no skin-in-game" — these are the reasons why agents cannot strategize, and they are permanent properties of AI systems, not Phase-1 limitations. The mechanism must therefore be permanent, not provisional.

**Where typically violated:** A "Strategy Support" Foundation part that allows agents to produce "strategic recommendations" without specifying that (a) these are J-Approve outputs requiring founder ack, and (b) the distinction between "variant generation" (J-Auto) and "method selection" (J-Strategic) is enforced at the access-control level. The pattern: agents producing AWAITING-APPROVAL packets is correct (proposing, not deciding). Agents auto-merging to canonical without ack violates the rule.

**What architecture must do:** Foundation's governance / access-control part must encode the J-level decision matrix as a structural invariant. Every agent role manifest must enumerate decision-classes with explicit J-levels. The message schema must carry acting_as field (already specified in FPF §5.9a). The hook-enforcement layer (Hook 4, pre-commit checks) must be part of Foundation, not a Phase-1 implementation detail. FUNDAMENTAL §6.7 trigger-response discipline must be a concrete Foundation deliverable.

### PP-5 — D25 Company-as-Code: every state change = git commit

**What:** [D25] All Jetix state — including Foundation architecture evolution — lives in git. Reconstructability from git history is a hard requirement. No state change without a commit.

**Why non-negotiable:** D25 makes explicit [D25]: "Company state reconstructable из git history на любой момент." This is both an operational requirement (recovery from git history) and an epistemic one (provenance of every decision). Foundation must architect around this: the provenance/audit-trail part must treat git history as the primary source of truth, not a secondary log. D25 combined with FUNDAMENTAL §5 (reliability / backup / append-only) creates a specific architectural constraint: Foundation must not include any state storage mechanism that is not git-backed or git-replicated.

**Where typically violated:** Wiki state stored only in filesystem without git commit discipline. Agent strategies.md updated in-session without commit. Approval log entries created but not committed. The failure mode: a session ends, state exists on disk but not in git, recovery from git history is incomplete.

**What architecture must do:** Foundation's information-lifecycle part must enforce commit-as-state-change as a structural rule, not a convention. Every Foundation part that produces state (wiki entries, alpha state transitions, approval log entries, strategy learning entries) must have a corresponding commit as part of its "Effects" (E lane) specification. The Company-as-Code principle [D25] means the /ingest --anchor= pattern [D28] must be implemented as part of Foundation's KM part, not a future enhancement.

### PP-6 — D28 query-driven KB: /ingest --anchor mandatory, not optional

**What:** [D28] KB ingestion is query-driven (anchor-tagged), not greedy. Every wiki entry must trace to at least one active anchor (project / topic / question). Unanchored entries are garbage-collection candidates.

**Why non-negotiable:** D28 changes the architecture of the KM part: it is not a "collect everything good" system, it is a "collect what serves active queries" system. This has a concrete implication for the Foundation KM part's interface card: the /ingest skill must expose --anchor= as a mandatory parameter, not optional. The /lint check must include anchor-trace verification [D28 implications]. A Foundation KM part designed without this constraint will drift into a "high-quality landfill" — large volume, low signal-to-noise, slow retrieval.

**Where typically violated:** A Foundation KM part that says "wiki stores all ingested knowledge" without the anchor-filtering mechanism. Or a KM part that includes --anchor= as "optional metadata" rather than a required parameter with lint enforcement.

**What architecture must do:** Foundation KM part must declare in its interface card: inputs carry declared relevance anchor (active project / topic / question from a query-registry); outputs carry anchor trace in frontmatter; /lint check enforces anchor-trace presence. The query-registry (what anchors are currently active) must be a Foundation artifact, not an implicit mental model in Ruslan's head.

### PP-7 — FUNDAMENTAL §6.2 founder-agency-preservation: system suggests, founder decides

**What:** [FUNDAMENTAL §6.2] The system does not substitute for founder agency. Recommendations yes, decisions no. The system does not evaluate the founder, does not know "what is best" in personal matters, does not generate values or meaning, does not assume consent.

**Why non-negotiable:** FUNDAMENTAL §6.2 is not a UX concern — it is an architectural constraint that determines which Foundation parts can be fully automated and which require a founder-ack gate. Any Foundation part whose function involves an action that "materially influences owner decisions or perceptions" (CP-5 L2 tier, FPF §4.5.1) requires a human approval gate. Foundation must include this gate as a structural mechanism, not a behavioral convention. The failure mode is agency erosion: system gradually takes over more decision-making because no explicit gate enforces the boundary.

**Where typically violated:** A "Self-Improvement" Foundation part that automatically updates strategies.md and promotes methodology changes without founder ack. Or a "Health Monitor" part that automatically changes system configuration when anomalies are detected. The AWAITING-APPROVAL packet pattern (used by the ROY swarm) is the correct Foundation primitive: propose, not decide.

**What architecture must do:** Foundation must include an explicit human-gate mechanism as a structural part (not folded into "operations"). This gate must be invoked by any Foundation function that crosses the L2-Substantive threshold [FPF §4.5.1]. The gate must produce an audit trail per the approval-log schema [FPF §4.5.4].

---

## §3 Candidate "Main Parts" Anti-patterns

The following anti-patterns are observed patterns that will likely appear in Phase A-1 when candidate parts from 5 experts are merged. Brigadier should watch for these.

### AP-1 — "Agent" as a main part (IP-1 violation)

Naming a main part after an agent instance (e.g., "Brigadier Layer," "ROY Swarm," "11 Agents Subsystem") conflates executor with role. The part should be named after the FUNCTION (method) the role performs, not the executor that fills it. Correct formulation: "Multi-Agent Coordination" or "Role Orchestration" — then the interface card specifies what roles exist, what methods they carry, what decision-class authority they hold, and how role-binding (executor-binding.yaml) is managed. The specific agents (Sonnet 4.6 brigadier, Haiku personal-assistant) are RUSLAN-LAYER content [FPF §5.1, FUNDAMENTAL §0]. Test: "If Jetix switched from Claude to GPT-5 agents, would this part still exist as defined?" If yes — the part is genuinely Foundation-level. If the part's definition would need rewriting — it leaked executor details.

### AP-2 — "Wiki" as a flat main part (A.1 violation)

Naming "Wiki" as a single main part ignores its internal holonic structure. The wiki has at minimum 4 distinct sub-holons with different lifecycles: (a) hot working layer (scratchpads, drafts, cycle artifacts — frequently mutated, short retention); (b) cold archive (compiled, linted, ready — stable, long retention); (c) topic-wikis / project-wikis (per-direction KB slices); (d) niche slices (per-agent symlinked views). These are NOT the same part — they have different F-G-R requirements, different access patterns, different backup/recovery needs (Tier 0 vs Tier 2 [FUNDAMENTAL §5.1]), and different anchor-trace requirements [D28]. A flat "Wiki" part will produce an interface card that mixes these concerns and prevents clear ownership. A.1 requires each part to have exactly one U.Boundary and a defined role (U.System vs U.Episteme). "Wiki" has both — the content is U.Episteme, the pipeline that writes it is U.System.

### AP-3 — "AI Augmentation" as a main part (anti-scope risk + scope creep)

"AI Augmentation" as a Foundation part is a category error. Augmentation is a property (how the system enhances founder cognitive capacity — FUNDAMENTAL §0 main principle), not a part with its own boundary, lifecycle, and interface contract. If it appears as a candidate part, it is probably a container for multiple concerns: agent orchestration (belongs in coordination), synthesis capabilities (belongs in KM), and the human-gate mechanism (belongs in governance). A part named "AI Augmentation" will produce an interface card that cannot be falsified (see Popper test in §1) — what observable would be absent if this "part" were removed? Likely nothing, because its functions live elsewhere. This is also a scope-creep risk: "AI Augmentation" as a part tends to absorb features that would otherwise be flagged for architectural review [FUNDAMENTAL §6.5].

### AP-4 — "Foundation Build" conflated with "FUNDAMENTAL document" (paradigm conflation P2)

This anti-pattern is already flagged in the deep-prompt [deep-prompt §9 item 13] but bears epistemic emphasis: FUNDAMENTAL is a locked constitutional Vision document (what the system must do, must not do, what it is). Foundation is a Layer 1 architecture (how the system is decomposed into parts that fulfill the Vision). Treating FUNDAMENTAL sections as Foundation parts (e.g., "§1 Use Cases A-L are the 12 Foundation parts") conflates the Vision with the Architecture. The 12 use-case categories (A-L) are requirements specification, not part decomposition. Foundation parts are the architectural units that together FULFILL those requirements. They may not map 1:1 to FUNDAMENTAL §1 categories — cross-cutting concerns (provenance, observability, governance, agency-preservation) may each serve multiple use-case categories simultaneously. The Vincenti distinction [Vincenti P7] matters here: FUNDAMENTAL §1 is "criteria and specifications" (Vincenti category 2); Foundation parts are "fundamental design concepts" (Vincenti category 1) — different knowledge types, different validation methods.

### AP-5 — "Operations" as a catch-all part (Locality violation — LOC)

A single "Operations" part that contains daily ops, agent swarm coordination, project lifecycle, and health monitoring violates LOC — the locality invariant that a part should stay within its epistemic territory and not blur into adjacent concerns. The failure mode: the "Operations" part's interface card becomes so broad that it has no meaningful boundary, and the dependency graph shows all other parts depending on Operations for everything. In FPF terms [FPF §12.3, A.15 Role-Method-Work Alignment]: plan vs reality must not be conflated, and U.Work (actual records) must be distinguished from U.WorkPlan (planning artifacts). A catch-all "Operations" part will mix U.Work (what happened — git history, approval logs, alpha state transitions) with U.WorkPlan (what is planned — cycle plans, sprint backlogs) without the firewall A.15 requires.

---

## §4 Where Ruslan-specific Creep is Likely

Per FUNDAMENTAL §0 and deep-prompt §8 R3: Foundation must be generic. The following areas are high-risk for Ruslan-specific content leaking into Foundation parts.

### Leak risk 1 — 11 archetypes: generic taxonomy vs Ruslan-specific context

The 11 archetypes [FUNDAMENTAL §7.1.1] ARE generic — they describe what kind of knowledge worker might use a Jetix instance (Startupper / Entrepreneur / Researcher / Engineer / Investor / Politician / Seller / Manager / Philosopher / Life-Developer / Blogger). These are Foundation-eligible as a user taxonomy for a CRM or access-control part. HOWEVER: any Foundation part that assumes the specific archetype mix for this Jetix instance (Ruslan is primarily Entrepreneur + Startupper + Manager) has leaked into RUSLAN-LAYER. Concretely: a Foundation CRM part that pre-configures pipeline stages for "DACH Mittelstand AI consulting" has leaked. A Foundation CRM part that provides a generic relationship-lifecycle state machine (per Alpha 1 Client in FPF §6.3.1) with configurable ICP parameters is Foundation-eligible.

### Leak risk 2 — 5-tier access model: generic structure vs Jetix-specific bindings

The T0-T4 access model [FUNDAMENTAL §7.4] is generic Foundation content (T0 Founder / T1 Trusted Agents / T2 Specialised Agents / T3 Inner Stakeholders / T4 Outer). The tier structure itself is Foundation. HOWEVER: binding specific agents to specific tiers (brigadier = T1, personal-assistant = T2) is RUSLAN-LAYER (Jetix-specific). A Foundation "Access Control" part should define the tier model and the enforcement mechanisms (role-based, scoped tokens, time-bounded, audit-trailed, revocable, compartmentalised [FUNDAMENTAL §7.4]) without naming specific agents. The specific agent-to-tier bindings go in the RUSLAN-LAYER executor-binding.yaml files [FPF §5.8.1].

### Leak risk 3 — USB-C metaphor, Korp-Startup (D29), DACH, Phase-1-specific targets

USB-C metaphor [D20 reinforcement in D25-D28 addendum] and Korp-Startup framing [D29] are explicitly Ruslan-specific self-narrative and positioning elements. They are RUSLAN-LAYER. Any Foundation part whose rationale cites "Jetix becoming the USB-C standard" or "Korp-Startup self-narrative" has leaked. Foundation's rationale for parts must be generic knowledge worker system architecture, not Jetix competitive positioning. Similarly: €50K Phase-1 targets [cited in FPF §5.4a cost analysis], DACH legal framework references (GDPR Art. 37, HGB §257), and EU AI Act compliance specifics are RUSLAN-LAYER. Foundation can include a generic "Compliance and Governance" part with generic regulatory-framework hooks — but binding those hooks to specific EU regulations happens in RUSLAN-LAYER.

### Leak risk 4 — FPF-Steward as specific role vs immune-function as generic concern

The FPF-Steward [FPF §5.4] is a Jetix-specific role sub-designation within the meta-agent. As a specific named role, it is RUSLAN-LAYER. HOWEVER: the function it performs (ontological integrity audit, alpha classification sanity, past-participle convention enforcement, F-G-R compliance check, A.14 edge-type verification) is a generic Foundation concern — any Jetix instance needs an immune system function. Foundation should include an "Ontological Integrity" or "System Health" part with the generic audit scope and cadence. The specific role name (FPF-Steward), the specific agent assigned to it (meta-agent), and the specific Jetix-phase trigger thresholds (30+ agents, etc.) are RUSLAN-LAYER bindings.

### Leak risk 5 — Company-as-code D25 infrastructure: generic principle vs Jetix-specific implementation

D25 [D25] is a universal principle (git-backed state, atomic commits, declarative configs). The principle is Foundation-eligible. The specific implementation (`.claude/config/*.yaml` paths, specific Jetix commit message format `[agent] action: description`) is RUSLAN-LAYER. Foundation should define: "state changes are git-backed; configuration is declarative YAML; every state change has a commit with provenance metadata." The specific conventions for Jetix's own git repo are RUSLAN-LAYER overlays on that Foundation specification.

---

## §5 Open Questions for Brigadier

The following items are under-determined from the epistemic / FPF / FUNDAMENTAL perspective and require Ruslan ack before Wave A can proceed without ambiguity. They are not blocking Wave A-0 pre-reads, but they are blocking Phase A-1 parts-merge if left open.

**OQ-PHIL-1: U.System vs U.Episteme split in Foundation — which parts are operational holons vs knowledge holons?**

FPF A.1 agency rule [FPF §1.4] states behavioral roles attach ONLY to U.System bearers; U.Episteme is passive. Foundation must declare for each proposed part whether it is primarily U.System (produces operational effects, can bear behavioral roles) or U.Episteme (stores knowledge, transformed only by external actors). Some candidates are clearly U.System (agent coordination, human gate mechanism, access control). Some are clearly U.Episteme (wiki content, strategy documents). Some appear dual (KM part — is it the content or the pipeline?). Without this declaration, the dependency graph cannot correctly type edges (creates is U.System → U.Episteme; ComponentOf operates between U.System holons). Question for Ruslan: should Foundation explicitly enumerate which candidate parts are U.System vs U.Episteme vs dual, or is this detail left to Wave C per-part architecture?

**OQ-PHIL-2: Provenance / audit-trail as cross-cutting concern vs standalone part**

B.3 F-G-R trust calculus [FPF §12.7], D25 company-as-code [D25], and FUNDAMENTAL §5 (reliability / audit logging) all require provenance tracking across all Foundation parts. Question: is "Provenance and Audit Trail" a standalone Foundation part with its own interface card, or is it a cross-cutting concern embedded in every other part's Effects (E lane) specification? If standalone — every other part has a methodologically-uses edge to it. If cross-cutting — every other part's interface card must include a provenance section. The choice affects the dependency graph topology significantly. This is a genuine architectural decision, not a detail: standalone creates a potential SPoF [FUNDAMENTAL §5.4], while cross-cutting creates implementation complexity without a clear owner.

**OQ-PHIL-3: How does Fork-and-merge D27 affect Foundation part boundaries?**

D27 [D27] says Jetix is a canonical upstream; instances can fork and adapt. Foundation must be forkable. This has a concrete implication: Foundation parts must have clear extension points (where a RUSLAN-LAYER fork can add configuration without modifying Foundation code). Question: should Foundation interface cards explicitly declare "extension points" (where a downstream fork may inject RUSLAN-LAYER configuration) vs "invariants" (what a fork may not change without losing Foundation compatibility)? Without this, D27's fork-and-merge architecture is aspirational rather than operational. The Vincenti distinction [Vincenti P7] applies: extension points are "design instrumentalities" (category 6) — they must be explicitly designed, not discovered by forks through trial and error.

**OQ-PHIL-4: Blast-radius categorization as a Foundation primitive**

FUNDAMENTAL §6.1 [FUNDAMENTAL §6.1] states: "якщо action не categorized — default deny + escalate, не 'creative interpretation'." This implies Foundation must include a blast-radius categorization mechanism — before any agent action, the action must be classified against a taxonomy that maps to J-level authority. This is more than the J-level decision matrix (which is per-role per-decision-class). It is a real-time classification of any novel action that does not match an existing decision-class. Question: should Foundation include an explicit "Blast-radius Classification" sub-function within the governance/access-control part? Or is the J-level matrix sufficient (any unclassified action defaults to J-Strategic = founder-only)? The FPF A.13 Agency-CHR [FPF §2.1a] supports per-task-family specialization, but does not explicitly address novel/unclassified actions.

**OQ-PHIL-5: F-G-R enforcement ownership — which Foundation part owns the trust-calibration audit?**

F-G-R tagging is required on every agent output, every ADR, every client deliverable [FPF §12.7, §4.2]. The FPF-Steward quarterly audit includes F-G-R compliance checks [FPF §5.4]. Question: which Foundation part owns F-G-R compliance enforcement? Options: (a) Governance/Health part — owns the quarterly audit and blocks promotion of non-tagged artifacts; (b) Provenance part — owns F-G-R as a structural tag requirement embedded in every artifact schema; (c) distributed — every Foundation part enforces its own F-G-R discipline. Option (c) is the most common failure pattern: F-G-R is "everyone's responsibility" and therefore no-one's. The Munger lollapalooza check [Munger P4] applied here: multiple mental models (immune-system IP-4, honesty CP-2, trust-calibration B.3) all reinforce that a single owner with a specific audit cadence is necessary. Recommendation to brigadier: assign F-G-R compliance enforcement to a single Foundation part as a primary function (not a secondary concern).

---

## Conformance Checklist (§3.1 critic mode)

| Check | Result | Evidence |
|-------|--------|----------|
| Falsifier-named (Popper) | pass | Every pressure point states what observable would indicate violation; every anti-pattern states its observable signal |
| Paradigm-named on shift (Kuhn) | pass | §1 explicitly names Левенчук / multi-agent / Karpathy paradigm mix; IP-2 requires Bridges at cross-paradigm boundaries |
| Mental-model + applicable-conditions (Munger) | pass | Popper P1, Kuhn P2, Munger P4, Vincenti P7, Stoic PP-5 all cited with specific applicable conditions |
| Method declares what it is NOT (via-negativa) | pass | §3 anti-patterns list what Foundation parts must NOT be; §4 lists where Ruslan-specific content must NOT enter Foundation |
| Dichotomy-of-control for meta-decisions | pass | PP-4 (agents-don't-strategize) and PP-7 (founder-agency-preservation) both declare which variables are in-founder-control vs not |
| Fallacy-named-when-named | pass | No fallacies invoked by name; where logical errors described, they are named as specific anti-patterns with observable signals |
| Meta-claim grounded in object-level | pass | Every IP is grounded in at least one concrete Jetix operational example (executor-binding.yaml, acting_as field, /ingest --anchor=, approval-log schema) |

**Acceptance predicate:** "All 7 pressure points carry a citation to FPF §X, FUNDAMENTAL §Y, or LOCKS D-Z; all 5 anti-patterns name an observable signal by which they would be detected in Phase A-1; all 5 Ruslan-specific leak risks name a specific document section or artifact type that marks the RUSLAN-LAYER boundary."

**Anti-scope of this pre-read:**
- This pre-read does NOT propose main Foundation parts — that is systems-expert and engineering-expert scope for Phase A-1.
- This pre-read does NOT assess capital or investment implications — investor-expert scope.
- This pre-read does NOT produce system feedback loops or leverage-point maps — systems-expert scope.
- This pre-read does NOT produce code review or implementation specifications — engineering-expert scope.
- This pre-read does NOT select the method for Foundation decomposition — that is Ruslan's strategizing authority [FPF §5.10.4].
