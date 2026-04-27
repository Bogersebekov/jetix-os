---
title: Investor-expert pre-read — Foundation main parts (scalability-architect mode)
date: 2026-04-27
phase: A-0
expert: investor-expert
mode: scalability-architect
cycle: cyc-foundation-build-2026-04-28
---

# Investor-expert Pre-read (Capital + Anti-fragility Lens)

## §1 Read summary (~600 words)

### Where investment compounds in Foundation

The capital-allocation lens sees Foundation through a single question: which parts accumulate value over time rather than merely functioning at a point in time? Three compounding loci stand out from the source material.

**Methodology Library (UC-C.3)** is the single highest-compound asset in Foundation. Every reusable pattern, template, and workflow extracted from a completed cycle is Lindy-testable: the longer it survives use without revision, the more weight it earns as canon. [FUNDAMENTAL §1 Category C] explicitly calls methodology a "first-class artifact, not a side-effect." Buffett's logic applies directly — the methodology library is the owner-earnings line of Foundation: each new project that consumes an existing template pays zero marginal acquisition cost; the ROI is unbounded as cycles accumulate. Graham margin-of-safety implication: the Foundation should over-engineer the methodology library storage discipline (provenance, versioning, archival) relative to what feels necessary early on, because the downside of under-engineering it (silent drift, undetected corruption) is not recoverable.

**KB / Wiki Substrate** (UC-B.2, UC-B.3, UC-B.4) compounds through cross-reference density. Karpathy LLM Wiki pattern (cited in [FUNDAMENTAL §2.1]) describes the KB as "provable by answering questions with citations." The investor lens: a KB that cannot cite its own claims is a liability, not an asset — each uncited claim is a hidden contingent liability that surfaces at retrieval time as noise. D28 Query-Driven KB Filtering [D28] is a direct application of via-negativa Taleb principle: do not let the KB fill with high-quality-but-irrelevant material. Signal density compounds; garbage compounds too, but negatively. The `--anchor=<project|topic>` discipline mandated by D28 is a portfolio filter preventing low-conviction positions from accumulating on the balance sheet.

**Agent Strategies Ledger** (UC-E.2, UC-C.1) is the self-improving P&L. Each `strategies.md` per-agent entry is a DRR (Decision/Reasoning/Result/Review) that raises future cycle quality. This is the Karpathy System Prompt Learning pattern [FUNDAMENTAL §2.4]. The investor analog: this is compound interest on operational learning — cycles that do NOT produce a strategies.md entry are the equivalent of spending the dividend rather than reinvesting it.

**Provenance + Audit Trail** (UC-H.2, D25 Company-as-Code [D25]) is the Lindy substrate itself. Git history = the longest-lived artifact in any technology stack (Lindy: git has been the dominant version-control paradigm for 20+ years; everything else in the tool chain turns over faster). Foundation's reliability is anchored by the fact that git is the most antifragile storage format available without external dependency. [FUNDAMENTAL §5.4] identifies "single git repo without backup" as a SPoF — the investor-expert calls this a risk-of-ruin-class fragility and endorses the full 3-2-1 backup doctrine.

### Where risk concentrates (SPoF analysis)

Three SPoF clusters are structurally visible:

1. **Founder-as-single-ack** (UC-H.5, §5.4 of FUNDAMENTAL). All quality gates converge on one person. If the founder is unavailable, capture / persistence / strategic-doc modification all halt. [FUNDAMENTAL §5.4] names this explicitly: "single human (owner) — critical decisions blocked." Risk-of-ruin characterization: not capital risk (no money lost) but runway risk — unacknowledged decisions pile up in queue, then expire or require redecision. The Foundation must encode a "delegation pattern for time-critical decisions during owner absence" as an operational primitive, not as a Phase 2+ improvement.

2. **Single-canonical-writer** (FPF §5.4a, brigadier role). The brigadier is the sole promoter to canonical wiki. This is a deliberate architectural choice per FPF IP-1 (Role ≠ Executor) — and it is also a single point of failure. Marks second-level thinking: what the architecture has already priced in is "this SPoF is acceptable because brigadier is an agent, not a human, and can be respawned." What it has NOT priced in: what happens when the brigadier's strategies.md drifts and produces systematically wrong promotions? The immune system for this is IP-4 FPF-Steward (meta-agent quarterly audit) — but if quarterly is too infrequent for a high-velocity Foundation build cycle, drift accumulates.

3. **AI-provider dependency** (§5.4 FUNDAMENTAL). Foundation runs on a single AI provider (Anthropic/Claude). [FUNDAMENTAL §5.4] identifies this as a SPoF with "multi-provider abstraction" as the mitigation. The investor lens: this is not a short-term risk-of-ruin (provider outages are brief), but it is a long-horizon fragility — provider pricing changes, capability regression, or policy changes could force emergency re-architecture. The Foundation should encode graceful degradation paths (filesystem-only operation, grep-based retrieval) as first-class capabilities, not afterthoughts.

### Buffett circle-of-competence boundary

Foundation should know deeply: information lifecycle mechanics (capture/triage/storage/retrieval), agent coordination discipline (IP-1 through IP-5), provenance machinery, and health-monitoring patterns. Foundation should delegate to specialists (Wave C): specific AI provider integrations (L-category external integrations), domain-specific CRM schemas (K-category), and business-vertical workflows (RUSLAN-LAYER).

### Marks second-level thinking on Foundation

First-level: "Foundation gives the system a solid base." Second-level: "The market (i.e., the operational reality) has already priced in that the base exists — what it has NOT priced in is the drift discipline. Foundation parts that are well-designed but lack an immune-system (quarterly health checks, integrity linters, strategy-ledger review) will silently degrade." The Foundation's moat is not its initial design; it is its resistance to entropy over time. This means the Self-Preservation + Integrity Layer (UC-I.4) is not a second-order concern — it is the compounding mechanism that makes every other part durable.

### Munger latticework — non-financial disciplines that apply

Biology (Dawkins — Selfish Gene): Foundation parts that can replicate themselves (methodology templates that generate more templates, agent strategies that improve agent strategies) are evolutionarily stable. Parts that cannot self-replicate will require perpetual human maintenance — a fragility. The methodology library and agent strategies ledger are the two "replicating" parts; everything else is scaffolding.

Mathematics (Lindy effect applied): the longer a Foundation invariant (e.g., append-only logs, provenance mandatory, fail-loud) has survived use, the more weight it deserves in the architecture. [D25] Company-as-Code is already Lindy-tested at the industry level (git, plain-text, atomic commits). Design decisions that deviate from Lindy-tested patterns carry a hidden risk premium.

### Taleb antifragile / barbell / via-negativa applied concretely

**Antifragile parts** (gain from disorder): the KB cross-reference graph — each retrieval failure that surfaces an orphan claim is a stress signal that forces a quality improvement. The lint pass (orphan detection, contradiction surfacing) is the antifragile mechanism. The more queries fail, the better the linter is calibrated. This is in contrast to a system that only shows successes. Foundation should be designed so that failures are visible and feed back into improvement, not silently swallowed.

**Barbell structure**: Foundation = safe substrate (append-only, Lindy-tested, provenance-mandatory) + experiments = risky upside (new skill acquisition, new agent patterns, new integrations). The barbell discipline means the safe substrate must be over-engineered relative to the experiment layer. [FUNDAMENTAL §8.5] confirms: constitutional constants (§5 reliability, §4 auto/manual boundaries, §6 anti-scope) are NOT subject to evolution — this is the barbell's safe pole being held fixed.

**Via-negativa** (removal > addition): what to exclude from Foundation? Per [FUNDAMENTAL §6 anti-scope + §8.2 anti-patterns]: engagement metrics as goals, variable rewards, auto-execute of architectural decisions, auto-strategizing. The Foundation's via-negativa list is already written in [FUNDAMENTAL §6] (50+ hard rules). The investor lens adds: every feature proposed for Foundation should pass the test "would removing this make the system fragile?" If yes — include. If removing it is fine — it does not belong in Foundation.

**Lindy discipline**: [FUNDAMENTAL §5.5] defensive patterns (idempotency, atomicity, resumability, append-only, circuit breakers) are all Lindy-tested patterns from distributed systems engineering (Kleppmann). They should be in Foundation at Day 0, not added later.

---

## §2 Candidate "main parts" (3-5)

### Part 1 — Provenance + Audit-Trail Substrate

**One-line scope:** Every artifact produced by Foundation carries a traceable origin chain (who, when, from what source, through which agent), stored in immutable git-backed structures.

**Why it is a part:** This is the Lindy substrate. Without provenance, every other part (KB, methodology library, agent strategies) becomes unverifiable. Loss of provenance = loss of the ability to trust any claim in the system. This is not a feature of other parts — it is a cross-cutting constraint that must be architected as a standalone concern with its own discipline (UC-H.2, UC-B.3, D25 [D25]). Graham margin-of-safety logic: the blast radius of getting provenance wrong is unbounded (silent corruption compounds over cycles); the cost of over-engineering it is bounded (storage, format discipline). Invest more here than feels necessary.

**FUNDAMENTAL UC mapping:** UC-H.1 (Company-as-Code), UC-H.2 (Provenance & audit trail), UC-B.3 (Source preservation raw+processed), cross-cutting to all other categories.

**Investment / risk profile:** Compounds strongly — each new artifact that carries correct provenance raises the retrieval trust of all existing artifacts (dense cross-referencing). Fragility point: if provenance format is inconsistently enforced across different parts (some use inline `[src:...]`, some use frontmatter `sources:`, some use none), the linter cannot catch violations. Enforcement uniformity is the moat.

**Cross-cutting:** Yes — every other part consumes or produces artifacts that require provenance tagging. This part defines the tagging contract.

---

### Part 2 — Knowledge Compound Engine (KB + Methodology Library)

**One-line scope:** The dual accumulation layer — the wiki KB (queryable, cited, cross-referenced) and the methodology library (reusable patterns, templates, workflows) — where past work compounds into future leverage.

**Why it is a part:** These two sub-components share a compounding mechanic that distinguishes them from all other Foundation parts: they accrue value over time, not just at the moment of creation. The KB answers queries; the methodology library answers "how did we do this before?" [FUNDAMENTAL §1 Category C UC-C.3] calls methodology "first-class artifact, not side-effect." [D28] Query-Driven KB Filtering ensures the KB remains signal-dense rather than a garbage-accumulating archive. Via-negativa discipline (Taleb): the KB's moat is enforced by what it refuses to ingest, not just what it accepts. Antifragile mechanic: each `/lint` pass that surfaces contradictions or orphan entries is a stressor that makes the KB stronger.

**FUNDAMENTAL UC mapping:** UC-B.2 (Multi-wiki KB), UC-B.3 (Source preservation), UC-B.4 (Synthesis on demand), UC-B.5 (Rapid ingestion pipeline), UC-C.2 (Skills acquisition), UC-C.3 (Methodology library).

**Investment / risk profile:** Highest long-run ROI of any Foundation part. Fragility point: the methodology library is only antifragile if it has a self-preservation + integrity layer (quarterly archaeology per [FUNDAMENTAL §3.7.6]). Without archaeology, the library accumulates stale entries that degrade retrieval quality. The decay is silent unless the linter is designed to surface it.

**Cross-cutting:** Partially — the KB is consumed by all other parts (agent strategies reference it, health monitoring queries it, daily ops uses it). But it also has a self-contained lifecycle (ingest → triage → process → store → index → retrieve → synthesize) that justifies its own part boundary.

---

### Part 3 — Agent Coordination + Communication Infrastructure

**Why it is a part:** The swarm of agents is only as reliable as its communication protocol. [FUNDAMENTAL §1 Category E, UC-E.3] states all agent communication must be through explicit mailboxes + message schemas + handoff protocols — "no implicit conventions." FPF IP-1 (Role ≠ Executor strict separation, [FPF §5.1]) requires that the role (method signature) be separated from the executor (agent instance). If agent communication infrastructure is not a standalone Foundation part, each new agent will invent its own communication pattern — this is the canonical fragility of multi-agent systems cited in the MAST failure-modes paper (`raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.pdf`).

**One-line scope:** The typed message schema, mailbox routing, escalation taxonomy, and handoff protocols that govern all agent-to-agent and agent-to-owner communication.

**FUNDAMENTAL UC mapping:** UC-E.1 (Multi-agent coordination), UC-E.2 (Agent self-learning), UC-E.3 (Agent communication discipline).

**Investment / risk profile:** Compounds indirectly — as new agents are added, the value of having a correct communication infrastructure grows super-linearly (each new agent must conform to the schema; schema violations are caught immediately rather than silently propagating). SPoF risk: the brigadier (single-canonical-writer) is a bottleneck in this infrastructure — see §1 SPoF analysis. The FPF-Steward quarterly audit (IP-4 [FPF §5.4]) is the immune system for this part.

**Cross-cutting:** Yes — every other part's outputs are routed through this infrastructure.

---

### Part 4 — Health + Integrity Monitor

**One-line scope:** The measurable, automated observability layer — SLI/SLO tracking, KB lint, backup verification, drift detection, and health alert routing — that prevents silent degradation of all other Foundation parts.

**Why it is a part:** Munger inversion applied: "how does Foundation fail?" Answer — silently. KB orphan ratio drifts above 5%, agent strategies stop being written, backup is not verified, strategic docs drift from locked decisions. Each of these failures is invisible unless there is a dedicated monitoring function. [FUNDAMENTAL §3] defines the full SLI/SLO framework and [FUNDAMENTAL §5.4] identifies the SPoFs that the monitor must watch. This is the "immune system" of Foundation — analogous to FPF IP-4 FPF-Steward role but applied to the entire system health, not just ontological integrity. Without a health monitor, Foundation is fragile (a system that only works when things go well, collapses silently when they do not). With a health monitor, Foundation is antifragile — failures surface as inputs that improve the next cycle.

**FUNDAMENTAL UC mapping:** UC-H.4 (Health monitoring & alerting), UC-I.1 (Periodic system health checkups), UC-I.4 (System self-preservation & integrity checks), UC-I.3 (Recommendation engine).

**Investment / risk profile:** Does not directly compound value but prevents compounded decay. The ROI is negative-space: you do not see the value until a failure would have occurred and did not. Graham margin-of-safety framing: the cost of under-investing in health monitoring is unbounded (silent corruption, undetected drift, data loss); the cost of over-investing is bounded (storage, compute, attention). Invest more here than feels necessary at day zero.

**Cross-cutting:** Yes — monitors all other parts' outputs and health indicators.

---

### Part 5 — Founder Agency Preservation Layer (Quality Gates + Human-in-Loop)

**One-line scope:** The explicit stage-gate mechanisms, escalation taxonomy, and HITL (human-in-loop) protocols that ensure the founder remains the sole locus of authority over architectural, strategic, and irreversible decisions.

**Why it is a part:** [FUNDAMENTAL §4] defines the auto/manual boundary with a Default Deny principle — if a task is not categorized as automatable, human ack is required. [FUNDAMENTAL §4.5] lists 12 hard "never automate" rules. [FPF §5.5 IP-5] requires explicit past-participle state transitions for all alphas — the gate IS the state transition. This is the anti-fragility against the most dangerous failure mode in any AI-augmented system: agency erosion (the founder stops being the acting subject and becomes the object that things happen to). [FUNDAMENTAL §6.2] dedicates a full section to this: "Система НЕ подменяет founder." Taleb skin-in-the-game: only the party bearing consequences (the founder) should hold final authority. The quality gate is the architectural enforcement of this principle.

**FUNDAMENTAL UC mapping:** UC-H.5 (Quality gates / stage-gated approval), UC-A.4 (Decisions tracking & recall), UC-A.3 (Strategic alignment enforcement), §4.3 (Human-only tasks), §4.5 (Anti-patterns never automate).

**Investment / risk profile:** This part does not compound in the positive direction but prevents the highest-magnitude negative compounding: agency erosion is irreversible at the point it becomes culturally normalized. Once the system routinely makes architectural or strategic decisions without HITL, reversing that pattern requires re-establishing trust — expensive and slow. Barbell logic: this part is the safe pole of the barbell; it must be over-engineered relative to the automation layer.

**Cross-cutting:** Yes — every other part's significant outputs pass through quality gates before promotion to canonical state.

---

## §3 Capital allocation pressure points

**D25 Company-as-Code [D25] = the Lindy substrate.** Git history is the most durable artifact format available. Every other technology in the Foundation stack (agent implementations, search indexes, dashboard tools) will turn over faster than git. This means Foundation's long-term compounding is disproportionately anchored to the quality of its git discipline: atomic commits with provenance, structured commit messages `[area] verb what (why)`, no hardcoded paths. The capital allocation implication: spend disproportionately on getting the git discipline right at Day 0 rather than on features that will be refactored in Wave C.

**D27 Fork-and-merge [D27] = ecosystem-level value distribution.** The long-horizon capital thesis for Foundation is that it becomes an upstream canonical that other instances (roy-replication per D21) fork and contribute improvements back to. This is the network-effects model: each contributor improves the canonical for all. The Foundation architecture must be designed from Day 0 as forkable — no hardcoded Ruslan-specific paths, no RUSLAN-LAYER content inside Foundation parts (per [FUNDAMENTAL §0 two-layer principle] and [FUNDAMENTAL §8.3 horizontal axis constraints]). If Foundation accumulates Ruslan-specific content, the fork-and-merge value distribution mechanism is broken before it starts.

**D28 Query-Driven KB Filtering [D28] = portfolio discipline applied to information.** "Pool first but filling driven by anticipated queries" is the KB equivalent of a conviction-based portfolio: only ingest what serves an active anchor. The anti-pattern (greedy ingestion because "the book is good") is the information equivalent of buying a stock because "the company is good" without a thesis. Foundation must encode the anchor requirement in the `/ingest` skill at the architectural level, not as a best-practice note.

**D29 Korp-Startup [D29] = narrative discipline constraining scope creep.** The founder operates as the CEO of a corporation-in-formation, not as a freelancer building tools. This has a direct Foundation architecture implication: Foundation must be built to corporate-grade reliability standards (§5.1 Tier 0 data = "cannot lose ever" [FUNDAMENTAL §5.1]) from Day 0, not deferred to Phase 2. The risk: building Foundation to "good enough for solo" means re-architecting under load in Phase 2 — the most expensive form of technical debt.

**Anti-scope §6 (via-negativa applied to architecture) [FUNDAMENTAL §6].** Foundation refuses to become: a marketplace (L-category integrations are Foundation infrastructure, not marketplace features), a social network (community management is RUSLAN-LAYER), a payment processor (handled by Stripe externally), or an engagement-optimization engine (no engagement metrics as goals). The 50+ hard rules in §6 are the via-negativa list that keeps Foundation lean. Every proposed Foundation feature should be checked against this list first. Features that are not forbidden but are not essential to any UC-A through UC-L should default to "defer to RUSLAN-LAYER."

---

## §4 SPoF + anti-fragility audit

### SPoF 1 — Founder as single human approval point

**Location:** [FUNDAMENTAL §5.4, §4.3, §4.5, UC-H.5 quality gates]. Every significant artifact requires founder ack. If founder is unavailable (illness, travel, cognitive overload), all quality gates queue.

**Current state:** No documented delegation pattern for time-critical decisions during owner absence. [FUNDAMENTAL §5.4] identifies this as a SPoF and proposes "documented decision authority delegation for time-critical things" — but this is listed as a mitigation to implement, not as an existing mechanism.

**Proposed Foundation architecture response:** Foundation must include an explicit "owner-unavailable protocol" as a first-class artifact (not a Phase 2 improvement). Minimal version: a `decisions/policy/owner-absence-protocol.md` that declares which decision classes can be deferred (all strategic), which can be delegated to agent + queued for ack (L1/L2 substantive), and which must halt (L0 contractual + lock modifications). The protocol is an insurance policy — low cost to write, unbounded cost if missing during a real absence event.

### SPoF 2 — KB integrity without automated repair

**Location:** [FUNDAMENTAL UC-I.4, §3.7.1, §5.2]. KB integrity checks (orphan ratio, contradiction count, provenance link completeness) are defined as health indicators but their enforcement is lint-pass based — not continuously enforced.

**Risk:** Silent corruption accumulates between lint passes. A busy cycle that skips the weekly lint pass leaves an unknown drift window. The self-preservation mechanism (UC-I.4) says "auto-repair where safe; escalate where judgment required" — but if the auto-repair tooling is not yet built, the fallback is manual repair, which is slow and founder-attention-intensive.

**Proposed Foundation architecture response:** The health monitor part (Part 4 above) must run a daily lightweight lint pass (orphan count, frontmatter schema compliance, provenance link sample check) as an automated always-on process, not just as a weekly ritual. Failures should be loud (alert to coordinator inbox) not silent. This is the antifragile mechanism: every lint failure is a signal that improves the next cycle's schema discipline.

### SPoF 3 — Agent strategy drift (the immune system gap)

**Location:** [FPF §5.4 IP-4, UC-E.2, FUNDAMENTAL §2.4 compound engineering]. Agent strategies accumulate in per-agent `strategies.md` files. The FPF-Steward quarterly audit checks for ontological integrity — but agent strategy drift (agents developing systematically wrong patterns) could go undetected between quarterly audits.

**Risk:** If an agent's strategies.md accumulates three or four DRR entries that reinforce an incorrect pattern (e.g., brigadier consistently routing a class of tasks to the wrong expert), the pattern compounds negatively across cycles before the quarterly audit catches it.

**Proposed Foundation architecture response:** The monthly health checkup (per [FUNDAMENTAL §2.5] monthly checkup) should include a "strategies.md freshness and coherence check" — not deep audit, but: (a) has each active agent produced at least one DRR entry in the last 30 days?, (b) do the last 3 DRR entries for each agent show positive trajectory? The FPF-Steward quarterly audit is the deep pass; the monthly check is the early-warning signal.

### SPoF 4 — Methodology library decay (no archaeology discipline)

**Location:** [FUNDAMENTAL §3.7.6 "Methodology archaeology"]. The methodology library is the highest-compound asset but has no automated decay detection. [FUNDAMENTAL §3.7.6] specifies quarterly archaeology (≥ 80% of entries either current or explicitly archived). But there is no alarm if the archaeology does not happen — it is calendar-driven, not trigger-driven.

**Risk:** Methodology entries become stale references that are retrieved but no longer applicable. Agents cite a methodology pattern that has been superseded. The damage is subtle — incorrect guidance applied with confidence.

**Proposed Foundation architecture response:** The health monitor (Part 4) should maintain a methodology-entry freshness index: for each entry, when was it last validated as current? Entries older than N cycles without validation should be flagged as "archaeology-required" in the weekly review surface. This converts a quarterly calendar ritual into a trigger-driven discipline — methodology archaeology fires when entries become stale, not on a fixed date.

### SPoF 5 — Backup without verified restore

**Location:** [FUNDAMENTAL §5.3, §3.7.2]. Backup hierarchy is specified (3-2-1 rule, RTO/RPO per tier). Restoration drills are required quarterly. But "backup exists" and "restore actually works" are different states. If the quarterly restoration drill is missed (founder unavailable, high-velocity cycle in progress), the backup is untested.

**Proposed Foundation architecture response:** Foundation must encode the restoration drill as a forced-ack protocol, not a calendar reminder. The health monitor should track "last verified restoration" as a first-class SLI. If last verified restore is > 60 days, the health dashboard surfaces this as a yellow alert (not just a metric). If > 90 days, it surfaces as red. The distinction between "backup exists" and "restore verified" should be explicit in two separate health indicators, not collapsed into one.

---

## §5 Open questions for brigadier

**Q1 — Founder-absence protocol: Foundation scope or RUSLAN-LAYER?**
The investor-expert argues this is Foundation scope (a generic professional knowledge worker using any Jetix instance could be temporarily unavailable). But the specific delegation rules (which roles receive delegated authority) will be Ruslan-specific. How to split: Foundation defines the protocol template and the decision-class taxonomy; RUSLAN-LAYER fills the specific delegation targets. Ruslan ack needed on whether this split is accepted.

**Q2 — Methodology library as part of KB part or as standalone part?**
The investor-expert proposes combining KB and methodology library as "Knowledge Compound Engine" (Part 2) because they share the compounding mechanic. But there is an argument for separating them: KB is query-driven (retrieve on demand), methodology library is pattern-driven (prescribe a repeatable approach). If the Wave C interface cards reveal these have different data schemas and different query patterns, the consolidation may be premature. Ruslan (or brigadier via A-1 synthesis) should validate this boundary before Wave C dispatch.

**Q3 — Health monitor cadence: daily lightweight vs weekly full vs quarterly deep?**
Investor-expert proposes three tiers: daily automated lightweight (orphan count, schema compliance sample), weekly structured (per [FUNDAMENTAL §2.5]), quarterly deep (FPF-Steward). But daily automated lint requires tooling that may not exist until Wave C or Wave D. Can the daily lightweight pass be implemented as a Git hook (pre-commit) rather than a scheduled agent task? This changes the implementation path significantly. Engineering-expert input needed.

**Q4 — Risk-of-ruin floor for Foundation build itself?**
The Foundation build (Waves A through E) is itself a capital allocation decision. Current phase: ROY swarm cycles with human ack at each wave boundary. The investor-expert observes: if Wave C parts are designed in isolation and integration failures are discovered only in Wave D, the rework cost is high. Propose: each Wave C part should include a "minimum integration smoke test" (can this part's output be consumed by at least one other part?) before promotion to AWAITING-APPROVAL. This is the Foundation-build's own margin-of-safety discipline. Ruslan ack on whether this gate is added to Wave C dispatch template.

**Q5 — D27 fork-and-merge governance: timing for first merge-back protocol?**
[D27] defers the merge-back governance decision to Phase 2+ (€200K valid'd) or earlier. From a capital lens: the longer Foundation accumulates Ruslan-specific content without a clear delineation of what is "Foundation-upstreamable" vs "RUSLAN-LAYER-only," the harder the eventual extraction will be. Propose: Wave A MASTER-PLAN-DRAFT includes a "fork-separation checklist" (per part: is this part forkable as-is? what would need to be parameterized for a different owner?). Not implementing the governance yet — just making the extraction surface visible. Ruslan ack on whether this is Wave A scope or Wave D scope.
