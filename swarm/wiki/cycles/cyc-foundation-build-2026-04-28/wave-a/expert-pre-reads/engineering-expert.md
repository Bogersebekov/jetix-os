---
title: Engineering-expert pre-read — Foundation main parts (integrator mode)
date: 2026-04-27
phase: A-0
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
sources:
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/LOCKS-D29-ADDENDUM-2026-04-26.md
confidence: high
confidence_method: rubric-pass-rate
---

# Engineering-expert Pre-read — Foundation Main Parts

## §1 Read summary

### Contract boundaries — what the engineering lens found

Reading the 14-layer description [SYSTEM-OVERVIEW §L0..§L9] alongside the current-state inventory [AUDIT §1..§12] and then setting both against the FUNDAMENTAL use-case taxonomy [FUNDAMENTAL §1 categories A-L] reveals one dominant engineering observation: **the contract boundaries in SYSTEM-OVERVIEW are drawn along a vertical stack (layers), but the real module boundaries in FUNDAMENTAL are drawn along capabilities (use-case categories)**. These two cuts are not the same, and the mismatch is the single most important engineering pressure point for Wave A decomposition.

**Clear contract boundaries visible now.**
L0 (git-repo + Company-as-Code) and L1 (wiki + Private Library) already have a clean one-way dependency: everything writes TO L0 via git commits; nothing writes FROM L0 back to L1 directly [SYSTEM-OVERVIEW §L0 Interfaces]. This is the Unix-philosophy "data flows one way" pattern applied correctly. L2 (Ingest) writes to L1 but reads from L0 config. L4 (Agent Layer) reads from L0 + L1 + L3, writes to L1 via brigadier. The upward data flow L2→L1→L3→L4 and downward control flow L9→brigadier→L4 are well-separated — two orthogonal flows over the same stack, which is correct [SYSTEM-OVERVIEW §4 diagram].

**Unix-philosophy decompositions — "do one thing well".**
The voice pipeline [AUDIT §6] is a clear example of good Unix decomposition: `transcribe.py` → `extract.py` → `filter.py` → `review_report.py`. Each tool has one job, a defined input format, and a defined output format. The `--resume` flag in `filter.py` and the `.partials/` pattern implement idempotency (a FUNDAMENTAL §5.5 defensive pattern) [AUDIT §6.2]. The CRM system [AUDIT §7] is similarly cleanly bounded: it has its own schema directory, its own scripts, its own test suite, and its own index. Both should be treated as **working atomic parts** — do not refactor them into Foundation architecture without strong justification [deep-prompt §9 anti-pattern 3].

**Abstraction layers — where information hiding belongs.**
Ousterhout's deep-module test: does the implementation complexity sit behind a thin interface? In current state, the wiki subsystem [AUDIT §8] is NOT a deep module. The `/ingest` skill is 9.7K (large surface), `/lint` is 18K (larger), and the wiki spine has 9 entity types + 8 observed edge types exposed to all callers. This is characteristic shallow-module proliferation — many configuration choices leak outward. A Foundation-level KB part should hide the edge-type mechanics and entity-type machinery behind a smaller query surface. The D28 lock [LOCKS-D25-D28 §D28] points exactly at this: "pool-filling driven by anticipated queries" is the principle that the KB interface should be query-shaped, not storage-shaped.

**Module / interface design — Hunt-Thomas DRY and orthogonality.**
The current 28 skills [AUDIT §5] have no explicit dependency declarations between them. `/crm-rebuild-index` rebuilds what `/crm-add` and `/crm-update` modify. `/build-graph` rebuilds edges that `/ingest` writes. These are implicit dependencies — each skill works, but the dependency graph is invisible. A Foundation "Skill/Tool Layer" part needs an explicit interface registry so skills declare what they read and what they write. Without this, adding a new skill risks breaking implicit consumers (AP-ENG-10 — external-dep without failure-mode declaration, applied at the system level rather than code level).

**Fowler refactoring smells in current architecture.**
Three smells stand out:
1. **Long method / God object at L4.** The agent layer holds 6 ROY experts + 14 legacy agents + brigadier + the entire 5×4 matrix dispatch logic + 5-layer memory protocol + hub-and-spoke routing grammar [SYSTEM-OVERVIEW §L4]. This is feature envy across multiple responsibilities. Foundation should separate the agent-identity spec (what a role is) from the agent-coordination protocol (how agents talk) from the agent-memory model (how agents remember).
2. **Duplication between L0 and L9.** Git-as-system-state (D25) lives in L0; AWAITING-APPROVAL gates live in L9. But the provenance gate (§5.5.5 in shared-protocols) and the AWAITING-APPROVAL format are both governance artifacts — they should be in ONE part, not split across two layers. The split is arbitrary (one is "infrastructure", one is "governance") but in function they form a single contract: "changes must be auditable and human-acked before promotion."
3. **Feature envy between L1 and L3.** Knowledge storage (L1) and synthesis/compounding (L3) share the wiki — the wiki is simultaneously the store AND the place where synthesis agents write their outputs (strategies.md, insights/). This makes the wiki interface ambiguous: is it a database (L1) or a working scratchpad (L3)? FUNDAMENTAL §1 category B (Information Lifecycle) and category C (Self-Improvement) map to two different use-case categories, suggesting a cleaner split.

**Brooks "no silver bullet" — essential vs accidental complexity.**
Essential complexity in Jetix Foundation: managing the tension between (a) information that needs to flow fast for daily work and (b) decisions that need provenance and human ack before they become canonical. This tension is real — it cannot be optimized away. Every design choice in Foundation either respects this tension (essential) or introduces ceremony that papers over it (accidental). The current 28-lock decision architecture is essential complexity: it costs cognitive load to maintain, but it prevents drift [SYSTEM-OVERVIEW §3]. The current two-wiki situation (wiki v3 + knowledge-base/ in migration) is accidental complexity: it exists because of a historical transition, not because two wikis serve two distinct purposes [AUDIT §1.1 — `wiki/` 589 files, `knowledge-base/` 9 files].

**Karpathy LLM Wiki substrate principles.**
The current wiki [AUDIT §8] has 552 entity files but only 5 claims entries and 0 summaries/foundations/experiments. This means the "queryable / atomic / cite-citation-by-default" principle [FUNDAMENTAL §1 B.2] is not yet operational at scale. The wiki exists as a structure but not yet as a compounding knowledge substrate. Foundation must define what makes an entry "canonical" vs "draft" and must enforce the anchor discipline (D28) so that queries reliably return cited evidence rather than noise.

**Anthropic effective-agents patterns (Orchestrator-Workers / parallelization / routing).**
The 5×4 matrix (5 experts × 4 modes) is an Orchestrator-Workers pattern [SYSTEM-OVERVIEW §L4]. Brigadier holds the orchestration contract; experts hold domain contracts. This is correctly structured. What is missing at Foundation level is an explicit **routing table** that declares: given input type X, which expert and mode combination handles it? Currently this lives implicitly in brigadier's system prompt. A Foundation "Agent Coordination" part should expose this routing table as a declarative artifact so that new experts can be added without modifying brigadier's prompt body.

**Cognition "Don't Build Multi-Agents" warning — context-sharing failure modes.**
The Cognition paper warns that multi-agent failure most commonly occurs at context boundaries — when agent A's output becomes agent B's input, information loss or format mismatch degrades quality faster than single-agent work. In the current state [AUDIT §4.3], most mailboxes are near-empty (7 of 13 have 0 messages). This is not yet a context-sharing problem, but it will become one when agents are active simultaneously. Foundation must define a **message schema contract** (already partially present in `shared/schemas/message.schema.json` [AUDIT §4.5]) as a first-class artifact, not a soft convention.

**AUDIT working pieces — respect these.**
Voice pipeline (cycle 11) works end-to-end on CC headless without ANTHROPIC_API_KEY [AUDIT §6.1]. CRM (cycle 10) has 35 passing unit tests, 10 skills, 8 Python scripts, and idempotent index rebuilds [AUDIT §7]. ROY Phase A has 3 compounded cycles, brigadier strategies with 8+ DRR entries, and 5 per-expert strategies files seeded [AUDIT §3.3]. These are load-bearing. Foundation decomposition must reuse them, not replace them.

---

## §2 Candidate "main parts" (5 candidates)

### Part 1: System Substrate (Git-as-System-State)

**Title.** System Substrate

**One-line scope.** The append-only, version-controlled ground on which every other part stores its state — git repository + declarative configs + atomic commit discipline + reversibility primitives.

**Why it's a part.**
Ousterhout: this is a deep module. The interface is extremely thin (git commit / git revert / git log / YAML config read). The implementation is the entire git history + config resolution + schema validation. Every other part consumes this interface identically — it does not need to know how git works internally. Raymond Unix principle: it is a single tool that does one thing (persistent, auditable, reversible state) and does it through a composable interface (git CLI). It has a hard contract boundary: EVERYTHING writes to System Substrate; System Substrate writes nothing back to any part directly. [D25; SYSTEM-OVERVIEW §L0; FUNDAMENTAL UC-H.1, UC-H.2, UC-H.3]

**FUNDAMENTAL UC mapping.** H.1 (Company-as-Code), H.2 (Provenance & audit trail), H.3 (Reversibility & safe experimentation), cross-cutting for all categories as the storage medium.

**AUDIT artefact mapping.** `git/` (entire repo), `.claude/config/*.yaml` (3 declarative configs), `CLAUDE.md` rules, `shared/schemas/` (3 JSON schemas), `swarm/lib/shared-protocols.md`.

**Cross-cutting?** Yes — every other part depends on this one for durability.

---

### Part 2: Knowledge Substrate (Query-driven KB + Private Library)

**Title.** Knowledge Substrate

**One-line scope.** The curated, queryable, provenance-linked store of knowledge — wiki entity files + typed graph edges + Private Library + query-anchor filtering (D28) — serving read-queries to all other parts.

**Why it's a part.**
This is the "do one thing well" part: store and retrieve knowledge. It is distinct from INGESTING knowledge (Part 3) and SYNTHESIZING knowledge (Part 4). The interface is: write an entity file with frontmatter + body + edges; query with `/ask --niche=X`; lint with `/lint`. Internal machinery (9 entity types, 8+ edge types, community detection) hides behind this surface. Brooks: the complexity of the type system and edge machinery is ESSENTIAL complexity (it makes queries reliable); the accidental complexity is the two-wiki situation (wiki v3 + knowledge-base/ in migration) which Foundation should close. D28 anchor discipline is the core contract: no ingestion without a declared query-relevance anchor. [D28; SYSTEM-OVERVIEW §L1; FUNDAMENTAL UC-B.2, UC-B.3, UC-F.1]

**FUNDAMENTAL UC mapping.** B.2 (Multi-wiki knowledge storage), B.3 (Source preservation), B.4 (Synthesis on demand), F.1 (Persistent memory across sessions).

**AUDIT artefact mapping.** `wiki/` (552 entities, 577 edges, 9 entity types, 6 niches), `raw/books-md/` (393 books), `raw/research/` (27 files), `wiki/graph/edges.jsonl`, `/ask`, `/lint`, `/consolidate`, `/build-graph`, `/search-kb`.

**Cross-cutting?** No — it is a distinct layer with well-defined read/write interfaces. It receives from Part 3 (Ingest) and serves Part 4 (Synthesis) and Part 5 (Agent Coordination).

---

### Part 3: Information Lifecycle (Ingest & Signal Processing)

**Title.** Information Lifecycle

**One-line scope.** The pipeline that converts external raw signals (voice, URL, file, book excerpt, chat) into provenance-linked, anchor-tagged draft entries ready for Knowledge Substrate promotion.

**Why it's a part.**
Unix philosophy: this is a composable pipeline (`transcribe → extract → filter → triage → ingest`), not a monolith. Each stage has a defined input format and defined output format. The STOP gate (human review before promotion) is a hard contract boundary: nothing from this part goes to Part 2 without passing through the STOP gate. This is the correct implementation of FUNDAMENTAL §4.2 (AI-augmented, human-in-loop). The voice pipeline in its current state already implements this contract cleanly [AUDIT §6]. The `/ingest` skill is the public interface of this part; the `tools/*.py` pipeline is its deep implementation. D28 anchor requirement is enforced at THIS part's input gate, not at the KB. [D28; SYSTEM-OVERVIEW §L2; FUNDAMENTAL UC-B.1, UC-B.5, §2.1 information flow]

**FUNDAMENTAL UC mapping.** B.1 (Selective inbox with filters), B.5 (Rapid ingestion pipeline / proactive learning).

**AUDIT artefact mapping.** `tools/transcribe.py`, `tools/extract.py`, `tools/filter.py`, `tools/review_report.py`, `tools/run_pipeline.sh`, `inbox/` (raw voice), `raw/transcripts/` (151 files), `/ingest` skill, `inbox-processor` legacy agent.

**Cross-cutting?** No — it has a directed dependency: receives from the external world, writes to System Substrate (git commit) and queues draft candidates for Knowledge Substrate.

---

### Part 4: Agent Coordination (Swarm Protocol + Memory Model)

**Title.** Agent Coordination

**One-line scope.** The protocol layer governing how agents communicate, how roles are bound to executors, how memory persists across sessions, and how the orchestrator dispatches and integrates work.

**Why it's a part.**
This is where the Cognition warning applies most directly. Agent coordination is the deepest module in the system — its interface is thin (dispatch a task, receive a structured packet), but its implementation is the entire 5×4 matrix, hub-and-spoke routing, 5-layer memory model, provenance gate, and HITL escalation taxonomy. Fowler smell: in current state this is a God object (brigadier's 64K system prompt + 6 expert prompts at 74-98K each) [AUDIT §4.2]. Foundation decomposition should extract the PROTOCOL (message schema, routing rules, escalation taxonomy) as a separate artifact from the AGENT DEFINITIONS (role specs). IP-1 Левенчук: Role ≠ Executor — this is the exact architectural separation this part enforces. The routing table, message schema, and escalation taxonomy should be declarative artifacts (YAML/JSON), not embedded in prose system prompts. [SYSTEM-OVERVIEW §L4; FUNDAMENTAL UC-E.1, UC-E.2, UC-E.3; FUNDAMENTAL §6.1 AI/Agents anti-scope]

**FUNDAMENTAL UC mapping.** E.1 (Multi-agent coordination), E.2 (Agent self-learning / strategy refinement), E.3 (Agent communication discipline).

**AUDIT artefact mapping.** `.claude/agents/brigadier.md` + 5 expert .md files, `agents/*/strategies.md` (8 files), `comms/mailboxes/*.jsonl` (13 channels), `shared/schemas/message.schema.json`, `swarm/lib/shared-protocols.md`, `swarm/wiki/meta/agent-improvements/`.

**Cross-cutting?** Partially — this part coordinates all other parts at runtime, but is itself a distinct capability (coordination). It depends on System Substrate (for its own persistence) and Knowledge Substrate (for agent memory reads).

---

### Part 5: Governance & Quality Gates (Provenance + Approval Discipline)

**Title.** Governance & Quality Gates

**One-line scope.** The stage-gate + provenance enforcement mechanism that ensures every significant artifact passes human ack before promotion to canonical state, and every claim is traceable to a source.

**Why it's a part.**
This is the most dangerous part to leave implicit. Currently it is split between L0 (git commits = provenance) and L9 (AWAITING-APPROVAL gates) in the 14-layer model [SYSTEM-OVERVIEW §L0, §L9]. Engineering lens: these two mechanisms are serving the same invariant — "no canonical change without an auditable, human-acked record." Unifying them into one part gives a single contract surface: everything that wants to become canonical must pass through Governance. The interface of this part is: `submit_draft(artifact) → gate_packet → human_ack → promote_to_canonical`. Its deep implementation is the provenance check (§5.5.5), the AWAITING-APPROVAL format, the LOCKED tag, and the git commit conventions (D25). This part cross-references UC-H.4 (health monitoring) and UC-H.5 (quality gates) directly. [D25; D27; SYSTEM-OVERVIEW §L9; FUNDAMENTAL UC-A.3, UC-H.5, UC-I.4; FUNDAMENTAL §4.2, §4.3]

**FUNDAMENTAL UC mapping.** A.3 (Strategic alignment enforcement), A.4 (Decisions tracking, recall & governance), H.5 (Quality gates / stage-gated approval), I.4 (System self-preservation & integrity checks).

**AUDIT artefact mapping.** `swarm/awaiting-approval/cycle-*.md` files, `swarm/logs/cyc-*/cycle-log.md`, `decisions/` (D1-D29 LOCKED files), `swarm/gates/`, `/company-status`, `/knowledge-diff`, `/lint --check-stage-gates --validate-predicate`, `.claude/config/sg-banned-phrases.yaml`.

**Cross-cutting?** Yes — every other part eventually routes artifacts through Governance to become canonical. It is a cross-cutting concern but with a well-defined interface, not ambient logic.

---

## §3 Engineering pressure points

### D25 Company-as-Code — git as system substrate

Every Foundation part that writes state MUST write through git commits with the `[area] verb what (why)` format. This is not just a convention — it is the recovery mechanism. If any part writes state outside git (in-memory only, or via Notion-first), it violates D25 and creates an unrecoverable state gap. Engineering implication: Part 1 (System Substrate) must be the single writer to canonical state. All other parts submit to Part 5 (Governance), which submits to Part 1. This gives a single write path for auditability. [D25; SYSTEM-OVERVIEW §L0 Boundaries]

### D28 Query-driven KB filtering — anchor mandatory at /ingest

D28 is NOT just a UX guideline — it is an architectural constraint on Part 3 (Information Lifecycle). The anchor must be validated at the ingest boundary, not at the KB boundary. If Part 3 accepts unanchored content, Part 2 (Knowledge Substrate) becomes a dump. The current `/lint` check #14 ("every wiki entry must have a link to at least one anchor") is a lagging indicator — it catches violations after they enter. Foundation design should enforce this as a leading constraint: Part 3's `/ingest` skill REJECTS input without a declared anchor, returning an error, not a warning. [D28; LOCKS-D25-D28 §D28; AUDIT §5.1 ingest skill]

### D17 Filesystem = SoT, Notion = view

Notion must never appear in the write path of any Foundation part. It is a read-display layer only. Any Foundation part that proposes a Notion write as part of its normal flow has violated D17. The integration layer (FUNDAMENTAL category L) is explicitly scoped to "read-only intelligence trackers" and "action coordinators with write-ack" — Notion would fall into read-only category. The only exception is manual operator sync after human ack (e.g., AWAITING-APPROVAL packet published to Notion after Ruslan reviews filesystem version). [D17; SYSTEM-OVERVIEW §L0 Boundaries; FUNDAMENTAL UC-L.1, UC-L.2]

### IP-3 Artifacts > conversations — every agent output is a file

This is the hardest discipline to enforce. An agent that returns a useful analysis in a chat turn but does not write it to disk has produced zero compounding value. Foundation must define for each part: what is the artifact shape? Where does it land? What frontmatter is required? The current system has 2,736 .md files [AUDIT §1.3] but only 5 claims entries in the wiki [AUDIT §8.1] — most knowledge is living in `decisions/` and `raw/research/` as flat prose, not in queryable wiki form. Foundation should designate specific paths as "canonical homes" for each artifact type.

### Existing skills (28) and agent inventory — no duplication

The 28 skills are load-bearing. Any Foundation part that proposes a NEW mechanism that duplicates an existing skill without retiring the old one adds accidental complexity (Brooks). Specifically: `search-kb` and `compile` are flagged as deprecated in favor of `/ask` [AUDIT §5.1]. Foundation decomposition should resolve this explicitly — either retire them or acknowledge they remain for backward compatibility with a sunset plan. Engineering position: retire them at Foundation wave, use `/ask` as the unified query interface.

### FUNDAMENTAL §6.1 AI agent constitutional anti-scope — no architectural autonomy

FUNDAMENTAL §6.1 is explicit: agents do NOT make architectural decisions [FUNDAMENTAL §6.1 "НЕ принимают architectural decisions"]. This means that Foundation parts' interface cards (Wave A-2) must declare which decisions are human-gated vs agent-executable. The boundary rule from engineering: any decision that changes a part's INTERFACE (adds/removes/renames a public function or data contract) is architectural and requires human ack. Any decision that changes only a part's IMPLEMENTATION (refactors internal logic while preserving the interface) is agent-executable. This maps cleanly to Ousterhout's module boundary definition.

### Append-only substrate — state is events, not mutations

FUNDAMENTAL §2.1 establishes append-only as the first cross-cutting substrate principle [FUNDAMENTAL §2.1 "Three cross-cutting substrates"]. This has direct engineering implications: `edges.jsonl` (already append-only, 577 edges [AUDIT §8.3]), `wiki/log.md` (append-only, 128 lines), `agents/*/strategies.md` (append-only DRR entries) — these patterns are correct and must be preserved across all Foundation parts. Any Foundation part that proposes an in-place mutation of a log or history file violates this invariant.

---

## §4 Open questions for brigadier

### Ambiguity 1: 14-layer vertical vs 12-category horizontal cuts

SYSTEM-OVERVIEW uses 14 vertical layers (L0-L9 + 4 cross-cutting). FUNDAMENTAL uses 12 horizontal use-case categories (A-L). These are NOT the same decomposition. A vertical layer can contain multiple use-case categories (L4 Agent Layer serves UC-E.1, UC-E.2, UC-E.3 from category E; but also UC-C.1, UC-C.2 from category C because agents are what executes self-improvement). A horizontal use-case category can span multiple layers (UC-A.4 Decisions tracking spans L0/git commits + L1/wiki entries + L9/AWAITING-APPROVAL + L3/compound step DRR entries). The 5 candidate parts I propose above are neither the 14-layer cut nor the 12-category cut — they are a third decomposition: **capability boundaries with clean contracts**. Brigadier needs to surface this three-way tension to Ruslan as Open Q for Wave A-1 merge.

### Ambiguity 2: Cross-cutting parts vs cross-cutting layers

SYSTEM-OVERVIEW already has 4 cross-cutting layers (L-R Resource, L-C Compute, L-B Brand, L-P Life OS). Two of my proposed 5 parts (Part 1 System Substrate and Part 5 Governance) are also cross-cutting in the sense that every other part depends on them. But they are NOT the same as SYSTEM-OVERVIEW's cross-cutting layers — those cut across all L0-L9 vertically; mine cut across all capabilities horizontally. The distinction: SYSTEM-OVERVIEW's cross-cutting layers are CONCERNS (resource management is a concern that every layer has); my cross-cutting parts are SERVICES (governance is a service that every part calls). Services have interfaces; concerns do not. This distinction matters for dependency graph construction in Phase A-2.

### Ambiguity 3: AUDIT shows CRM cycle 10 and voice pipeline cycle 11 as working tech — where do they fit?

CRM [AUDIT §7] is not one of my 5 candidate parts. It is a concrete instantiation of FUNDAMENTAL category K (Communication & Network Tracking). At Foundation level, K maps to a "Relationship Tracking" capability that CRM implements. Should Foundation decompose to include "Relationship Tracking" as a 6th part? Or should CRM be referenced as an existing implementation of a Foundation-level interface defined within "Information Lifecycle" (Part 3)?

Engineering position: CRM has its own schema, scripts, tests, and index — it is already a deep module with a thin skill interface (10 skills). It should be referenced as a WORKING IMPLEMENTATION of the Foundation "Relationship Tracking" contract, not reimplemented. The open question is whether "Relationship Tracking" warrants its own main part or is a sub-part of "Information Lifecycle."

### Ambiguity 4: Synthesis / Compounding Engineering — standalone part or protocol within Agent Coordination?

SYSTEM-OVERVIEW gives Synthesis its own layer (L3). FUNDAMENTAL §2.2 defines the Plan/Work/Review/Compound 40/10/40/10 cycle as a cross-cutting protocol, not a separate capability. Engineering lens: the Compounding Engineering cycle is a PROTOCOL that runs over all other parts — not a module with its own data. The `/compile`, `/ask`, `/consolidate` skills are query-and-synthesis capabilities that belong in Part 2 (Knowledge Substrate) as its synthesis interface. The DRR ledger discipline belongs in Part 4 (Agent Coordination) as each agent's self-learning mechanism. The brigadier compound step belongs in Part 5 (Governance) as the cycle-close artifact. Engineering position: L3 should be DISSOLVED across other parts, not made a standalone Foundation part. But this contradicts SYSTEM-OVERVIEW §L3 — brigadier needs to surface this as a candidate cycle for Phase A-1 philosophy-expert critic review.

### Ambiguity 5: Where does the health monitoring layer live?

FUNDAMENTAL category I (Continuous Health & Self-Improvement) maps to UC-I.1 through UC-I.4. Health monitoring reads from all parts (KB integrity, agent queue depth, cycle velocity, resource burn) but writes to Part 5 (Governance, as alerts → AWAITING-APPROVAL when thresholds breach). Should health monitoring be a standalone Foundation part (a "System Observability" part)? Or is it a cross-cutting protocol like Compounding Engineering? SYSTEM-OVERVIEW doesn't give health monitoring its own layer — it is distributed across L3 (strategies), L4 (agent metrics), L9 (governance gates). Engineering position: health monitoring is a cross-cutting concern that deserves a THIN dedicated layer with its own artifact type (health dashboard + lint report), but should NOT be a heavyweight main part. Surface to brigadier for Phase A-1 decision.
