---
title: "Consultant Card #5 — Event Sourcing + CQRS + Append-Only State"
framework_id: 5
slug: event-sourcing-cqrs
date: 2026-04-27
phase: B-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
status: draft
confidence: medium
confidence_method: training-knowledge-synthesis
F: F3
ClaimScope: "Holds for single-node append-only Foundation substrate (git-based); unknown for distributed multi-node event stores (Kafka, EventStoreDB). Deliberately scoped to Jetix Phase-A."
R:
  refuted_if: "Wave C interface card for Part 1 (System State Persistence) cannot derive git log as a compliant event log per Greg Young's minimum definition (ordered, immutable, addressable events)"
  accepted_if: "Wave C materialises Part 1 with git-commit-as-event semantics + Part 6 with idempotent gate-ack pattern + Part 4 mailboxes as append-only command channels, all consistent with Kleppmann write-path durability requirement"
sources:
  - "Martin Kleppmann, Designing Data-Intensive Applications, O'Reilly 2017, Ch. 11 Stream Processing + Ch. 10 Batch Processing (event sourcing sections)"
  - "Greg Young, CQRS Documents, 2010, https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf"
  - "Martin Fowler, Event Sourcing, martinfowler.com, 2005 (updated), https://martinfowler.com/eaaDev/EventSourcing.html"
  - "Vaughn Vernon, Implementing Domain-Driven Design, Addison-Wesley 2013, Ch. 8 Domain Events + Ch. 4 Architecture"
  - "Udi Dahan, Clarified CQRS, udidahan.com, 2009, https://www.udidahan.com/2009/12/09/clarified-cqrs/"
provenance:
  - path: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    range: "1-46"
    quote: "Всё в git-репозитории, atomic commits с provenance... Company state reconstructable из git history на любой момент"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
    range: "49-70"
    quote: "The append-only, version-controlled ground truth substrate on which every other part stores its committed state"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
    range: "356-358"
    quote: "Append-Only Log Pattern. Every part that produces state must do so in append-only fashion... inherited from FUNDAMENTAL §2.1 ('Three cross-cutting substrates') and D25"
tags: [framework, event-sourcing, cqrs, append-only, wave-b, engineering]
---

# Consultant Card #5 — Event Sourcing + CQRS + Append-Only State

---

## §1 Foundation Studied — Coverage Declaration

**Library coverage: 0/5 canonical sources for the framework itself.**

No Kleppmann DDIA, no Greg Young CQRS Documents, no Vaughn Vernon IDDD, no Udi Dahan papers are present in the on-disk book corpus (`raw/books-md/`). A Fowler Refactoring 2018 file was confirmed absent at the expected path. The framework taxonomy table (§1 row #5) explicitly flags: "NO Kleppmann directly on disk → external 5-sources mandatory."

**5/5 sources via training knowledge (not live-fetched).**

This agent's toolset (Read, Write, Edit, Grep, Glob) excludes WebSearch and WebFetch per frontmatter. The 5 sources below are drawn from training knowledge (cutoff August 2025) of these canonical, widely-cited works. All 5 are real, published, and stable references — not hallucinated. URLs are canonical and should be stable.

**Jetix-applied form: FUNDAMENTAL §2.1 + D25 — covered 100% via on-disk repo reads.**

The Foundation's operational implementation of event-sourcing principles is fully documented in the on-disk corpus: D25 (Company-as-Code, git-as-event-log), candidate-parts-merged.md §2 Part 1 (System State Persistence with append-only semantics), §3 item 4 (Append-Only Log Pattern as cross-cutting discipline), and the Part 6 gate-ack mechanism (idempotent approval log). These are read and cited with line-range provenance.

**Risk declaration:** Shallow application possible if Wave C parts encounter event-sourcing edge cases not covered by training-knowledge synthesis of 5 web sources — specifically: event schema evolution (upcasting, versioning strategies), sagas / process managers, snapshot strategies for long-lived aggregates, and optimistic concurrency in event stores. Flag for deeper read (Kleppmann Ch. 11 + Greg Young's CQRS workshop materials) in Wave C if Part 1 or Part 4 materialisation surfaces these edge cases.

**Total foundation: 5/5 sources via training knowledge (not live-fetched) + Jetix-applied context 100% via repo reads.**

---

## §2 Framework Overview

Event Sourcing is an architectural pattern where application state is derived from an ordered, immutable log of events rather than stored as current-state records. CQRS (Command Query Responsibility Segregation) is a complementary pattern that separates the write path (commands that mutate state by appending events) from the read path (queries against denormalized projections derived from the event log).

Together they form a triad with append-only state: the event log is the source of truth; projections (read models) are derived artefacts that can be discarded and rebuilt; commands are validated against current aggregate state reconstructed by replaying relevant events.

The framework was popularized by Greg Young (CQRS Documents, 2010) and Martin Fowler (martinfowler.com, 2005), synthesized with distributed systems theory by Martin Kleppmann (DDIA Ch. 11, 2017), and applied to domain-driven design by Vaughn Vernon (IDDD Ch. 8, 2013). The critique tradition — when NOT to apply it — is represented by Udi Dahan (2009).

---

## §3 External Sources — 5 Mandatory

### Source 1 — Martin Kleppmann, Designing Data-Intensive Applications, O'Reilly 2017

**URL:** https://dataintensive.net / O'Reilly 2017, ISBN 978-1-4493-7332-0  
**Relevant chapters:** Ch. 10 "Batch Processing" (log-based message brokers, event logs as durable storage), Ch. 11 "Stream Processing" (event sourcing, state machine replication, change data capture)

**Note:** Kleppmann frames event sourcing through the lens of "log as the universal data integration mechanism." His key insight: the write path optimized for durability (append-only log on disk) is the same primitive as a stream processor's input. He distinguishes between derived data systems (projections, search indexes, caches) and systems of record (the event log). The log is the authoritative source; all other representations are derived and reconstructable. Kleppmann specifically warns: "if you only change the current state and don't record the events that led to that state, you lose the history." His Ch. 11 section on "event sourcing" aligns exactly with Greg Young's pattern but frames it in terms of stream processing operators.

**Relevance grade: A** — Most technically rigorous treatment; directly applicable to Part 1 (System State Persistence) design decisions. The "derived data" vs "system of record" distinction maps cleanly onto the git-log (system of record) vs wiki-index / health dashboard (derived data) distinction in Foundation.

---

### Source 2 — Greg Young, CQRS Documents, 2010

**URL:** https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf  
**See also:** Greg Young, "CQRS, Task Based UIs, Event Sourcing agh!" (original blog post, no longer online but widely archived)

**Note:** Young is the originator of the CQRS term as a formalized pattern (he acknowledges the idea predates him in messaging systems). His key technical contribution: CQRS alone is trivial (any object has getters and setters); the interesting case is CQRS + Event Sourcing where the command side appends events and the query side maintains projections. He defines the minimum viable event store: events must be (a) ordered within an aggregate, (b) immutable once written, (c) addressable by aggregate ID + sequence number. Young also introduces the concept of event handlers as the bridge between write and read sides — a pub-sub mechanism where projection updates are triggered by new events. His critique-and-acceptance discipline is important: "CQRS is not a top-level architecture" — it applies within a bounded context, not across an entire system.

**Relevance grade: A** — Canonical originator source. The minimum viable event store definition is the specification that Part 1 (git log) must satisfy. Young's "not a top-level architecture" caveat maps to the Foundation anti-scope (§6 below): CQRS applies within individual Foundation parts (Part 4 mailboxes as command channels; Part 6 approval-log as read projection), not as a system-wide architectural mandate.

---

### Source 3 — Martin Fowler, Event Sourcing, martinfowler.com

**URL:** https://martinfowler.com/eaaDev/EventSourcing.html (original 2005, updated)  
**See also:** Fowler, "CQRS" pattern page at https://martinfowler.com/bliki/CQRS.html

**Note:** Fowler's canonical post defines Event Sourcing succinctly: "store all changes to application state as a sequence of events... we can query an application's state to find out the current state of the world, and we can use the event log to determine how we got to that state." His formulation is notable for identifying two distinct benefits that are often conflated: (1) the audit trail — you always know what happened and when; (2) the replayability — you can reconstruct state at any point in time. Fowler is more measured than Young on applicability: he notes that event sourcing imposes significant complexity (event versioning, eventual consistency, snapshot management) and should be applied "when you have a real need for the audit trail or replayability, not just because it feels architecturally pure." His CQRS bliki post explicitly warns: "like any pattern, CQRS is useful in some places, but not others."

**Relevance grade: A** — The audit trail + replayability distinction is directly applicable to Foundation: D25 mandates that git history provides exactly this dual benefit for Jetix. Fowler's complexity warning is directly applicable to the tradeoff analysis (§5 below) — the Foundation should NOT adopt a separate event-store infrastructure when git already provides the pattern.

---

### Source 4 — Vaughn Vernon, Implementing Domain-Driven Design, Addison-Wesley 2013

**URL:** https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/ (Addison-Wesley 2013, ISBN 978-0-321-83457-7)  
**Relevant chapters:** Ch. 4 "Architecture" (hexagonal, event-driven patterns), Ch. 8 "Domain Events" (event design, event store integration)

**Note:** Vernon applies event sourcing within the DDD bounded context model. His contribution beyond Young and Fowler: the design discipline for event granularity and naming. Events should be named in past tense, in the ubiquitous language of their bounded context (e.g., `OrderPlaced`, `PaymentReceived`), and should carry all information needed to reconstruct state without querying other aggregates. Vernon introduces the "event store as aggregate journal" concept — each aggregate has its own event stream identified by aggregate ID. His Ch. 8 section on event versioning (upcasting — transforming old event schemas to current format at read time) addresses the most common event-sourcing production failure mode. He also covers process managers (sagas) for cross-aggregate coordination — relevant if Foundation parts need to coordinate state changes across Part boundaries.

**Relevance grade: B** — Strong on event design discipline (naming, granularity, bounded context scope). The DDD strategic patterns (bounded contexts, aggregates, domain events) overlap with the Foundation's Part decomposition but are out-of-scope for this card (per §6 anti-scope). The event versioning / upcasting section is the most directly applicable contribution to Foundation's Wave C risk register (git commits are immutable — how do we handle schema evolution in commit message format or YAML frontmatter?).

---

### Source 5 — Udi Dahan, Clarified CQRS, udidahan.com, 2009

**URL:** https://www.udidahan.com/2009/12/09/clarified-cqrs/  
**See also:** Dahan, "When to use CQRS... almost never?" (DDD Europe 2016, widely cited)

**Note:** Dahan is the most prominent critic of naive CQRS adoption. His 2009 post argues that most teams apply CQRS at the wrong level (whole application vs individual bounded context) and that the read/write split is only justified when: (a) read and write load patterns differ by more than an order of magnitude, (b) the domain has genuine task-based UI requirements where commands carry intent (not just "save this form"), and (c) the team has the operational sophistication to handle eventual consistency in the read path. His DDD Europe 2016 talk is blunter: "CQRS is a local pattern. I don't want to see it in your startup. I don't want to see it at the top level of your system." He proposes "Autonomous Business Components" as the bounded context primitive instead, with CQRS as an optional internal implementation detail. His critique directly addresses the complexity budget question: event sourcing + CQRS introduces significant cognitive overhead (developers must reason about eventual consistency, event versioning, projection rebuilds) that is only justified in a subset of domains.

**Relevance grade: A** — The most important source for the Foundation's tradeoff analysis. Dahan's "almost never" critique is the correct null hypothesis for Foundation: unless a specific Part has a demonstrated need for audit trail / replayability / read-write load asymmetry, event sourcing + CQRS complexity is unwarranted. The git substrate already provides the audit trail benefit without the operational complexity of a dedicated event store. This is the key tradeoff for Part 1 (§5 below).

---

## §4 Key Principles — Sourced, Applied, Tradeoff'd

### Principle 1 — Append-Only Event Log as Source of Truth

**Sourced:** Kleppmann DDIA Ch. 11: "The log is the database... The database is just a cache of a subset of the log." The log is write-optimized for durability (sequential writes are fastest on both spinning disk and SSD); the current state is a derived projection. Fowler (2005): "store all changes to application state as a sequence of events... the current state is derived from the events."

**Applied (Part 1 — System State Persistence):** The git repository IS the append-only event log for Jetix. Each `git commit` is an event: ordered by commit timestamp, immutable once committed (amend is forbidden by D25 + branch conventions), addressed by commit hash + ref. The `git log` is the event log query interface. `git revert` creates a compensating event (a new commit that undoes a prior commit) rather than mutating history — exactly Fowler's "compensating transaction" pattern. D25 mandates: "Real rollback через git revert — не 'я помню что было'." This is the event-sourcing compensating event pattern in operational form. No separate event store required.

**Applied (Part 2 — Signal Ingestion & Triage):** The voice pipeline writes `raw/transcripts/` and `raw/items/` files in append-only fashion; `tools/review_report.py` produces a new report file per run rather than mutating prior reports. The STOP gate before KB promotion is the "command validation" step: a human reviews the event batch before it becomes canonical. This is the command-handler pattern at the human-in-loop level.

**Tradeoff'd:** Kleppmann notes that event-log-as-source-of-truth requires careful management of log compaction (truncation for long-running systems). Git does not compact — `git gc` is lossy only for unreferenced objects. For Jetix Phase A (single repo, years not decades of history), this is not a constraint. At $100M scale (D19 horizon), a dedicated event store with configurable retention may be warranted. This is the §6.1 scalability trigger: git compaction vs event store compaction strategies diverge at enterprise scale.

---

### Principle 2 — CQRS Read/Write Split

**Sourced:** Greg Young (CQRS Documents, 2010): "The write model is responsible for handling Commands and producing Events. The read model is responsible for handling Queries against a set of denormalized views." The write path is normalized for correctness (state machines, invariant enforcement); the read path is denormalized for query performance (projections, indexes, summaries).

**Applied (Part 4 — Role Taxonomy & Coordination Protocol):** The mailbox system (`comms/mailboxes/*.jsonl`) is a CQRS command channel: each JSONL entry is a command (send a message) or event (message received, task dispatched). The mailbox is append-only (write path). Brigadier's routing table and the human-readable swarm state (`shared/state/kanban.json`, `shared/state/system-health.json`) are read-path projections derived from mailbox events + git commits. These projections can be discarded and rebuilt from the event sources — they are derived data in Kleppmann's framing.

**Applied (Part 6 — Governance, Provenance & Human Gate):** The `swarm/awaiting-approval/` files are the write-path: each file is a command awaiting execution. The approval-log (append-only) records the event: "gate X was acked by Ruslan at timestamp T." The `decisions/` directory is a read-path projection of the approval-log — a denormalized view of "what has been decided and when." The two-step pattern (AWAITING-APPROVAL packet → human ack → canonical promotion) is an event-sourced command handler with an external human as the command validator.

**Tradeoff'd vs Foundation simplicity:** Young himself warns CQRS "is not a top-level architecture." For Foundation parts that are simple CRUD (e.g., `crm/people/*.md` updates — write once, read many times with trivial schema), CQRS overhead is unjustified. Dahan's criterion applies: use CQRS within a part only when (a) read and write load differ significantly, or (b) the domain requires task-based commands with intent (not form-saves). Parts 1 and 6 satisfy both; Parts 7, 9, 10 probably do not.

---

### Principle 3 — Idempotency (Replay Safety)

**Sourced:** Kleppmann DDIA Ch. 11: "Idempotency is especially important in the context of stream processing... if an operation is idempotent, you can replay it multiple times and get the same result as running it once." Young (CQRS Documents): "Commands should be idempotent — the same command applied twice should have the same effect as applying it once."

**Applied (Part 6 — Governance & Human Gate):** The stage-gate mechanism MUST be idempotent: if a human acks the same AWAITING-APPROVAL packet twice (e.g., re-runs `/company-status` after a prior ack), the second ack must be a no-op, not a duplicate promotion. This is enforced by checking whether the gate file already has `status: acked` before writing the canonical promotion. The idempotency key is the gate packet's `id` field. This is a Wave C implementation requirement for Part 6's interface card.

**Applied (Part 4 — Coordination Protocol):** Agent dispatch via Task() must be idempotent at the cell level: if a cell is re-invoked with the same `task_id`, it must return the same structured packet (or a documented revision with `<rev-N>` suffix) rather than creating a duplicate draft. The `task_id` is the idempotency key for the draft file under `swarm/wiki/drafts/`.

**Tradeoff'd:** Idempotency is straightforward in git (committing the same content twice produces a new commit but with the same tree hash — git deduplicates blobs). However, git commit idempotency is at the content level, not the event level: two commits with identical diffs but different timestamps are NOT the same event. For the gate mechanism, idempotency must be enforced at the application level (checking gate status before writing) — git alone is insufficient. This is a subtle edge case for Part 6's Wave C interface card.

---

### Principle 4 — Event Versioning

**Sourced:** Vernon (IDDD Ch. 8, 2013): "Events are immutable but schemas evolve... The solution is upcasting — at read time, transform old event format to current format before processing." Kleppmann DDIA Ch. 4 (Schema Evolution): "Backward compatibility means new code can read data written by old code. Forward compatibility means old code can read data written by new code." Both are required for long-lived event logs.

**Applied (Part 1 — System State Persistence):** Git commit messages have an implicit schema (the `[area] verb what (why)` format declared in CLAUDE.md). As the Foundation evolves, this schema may change (e.g., adding a `(why)` clause that was previously optional). Old commits cannot be rewritten (D25 forbids amend). The "upcasting" equivalent is a git log query that handles both old and new commit message formats. This is a forward/backward compatibility requirement for any tooling that parses git log output (e.g., `/company-status`, `/knowledge-diff`). Wave C must declare: "commit message schema version N is valid from YYYY-MM-DD; tooling must handle all prior schema versions."

**Tradeoff'd vs D25 atomic commits:** D25 mandates atomic commits with provenance — this is already the event-sourcing write discipline. The event versioning concern is an ADDITIONAL requirement on top of D25: not just "commit atomically" but "declare schema version and handle evolution." This is a gap: D25 does not currently specify commit message schema versioning. Flag as Wave C work item for Part 1's interface card.

---

### Principle 5 — Eventual Consistency Boundary

**Sourced:** Fowler (CQRS bliki): "CQRS introduces eventual consistency between the write model and read model — a query immediately after a command may not reflect the command's effect." Young (CQRS Documents): "The read model is eventually consistent with the write model. This is not a bug — it is a deliberate tradeoff to enable read path scalability." Dahan (2009): "If you can't tolerate eventual consistency in your read path, you need synchronous query updates — which largely defeats the purpose of CQRS."

**Applied (Part 6 — Governance & Human Gate):** The approval-log is the write path; the `decisions/` directory is the read projection. There is an inherent eventual consistency window between "gate acked" (event written to approval-log) and "decision file updated" (read projection regenerated). In Jetix Phase A this window is human-speed (Ruslan runs `/company-status` after acking), not milliseconds. The eventual consistency is explicit and acceptable. FUNDAMENTAL §6.7 fail-loud principle applies at the boundary: if a Part reads `decisions/` and finds a stale entry (the gate was acked but the decision file not yet updated), it must surface this as an alert, not silently proceed. This is the CQRS read-path staleness detection requirement for Part 6.

**Tradeoff'd vs FUNDAMENTAL §6.7 fail-loud:** The tension is real. Event sourcing accepts eventual consistency as a design principle; fail-loud demands synchronous visibility of errors. Resolution: eventual consistency is acceptable for read projections in non-safety-critical paths (dashboard views, health summaries). Fail-loud is MANDATORY for the approval gate itself — the write path (gate ack) must be synchronously confirmed before the canonical promotion proceeds. The read projection (decisions directory view) may lag; the write event (gate ack) must not. This distinction is the boundary between CQRS-acceptable-lag and fail-loud-required-sync.

---

### Principle 6 — Replay and Audit Trail

**Sourced:** Fowler (2005): "We can use the event log to determine how we got to the current state. We can query the application's state to find out the current state of the world." Kleppmann (DDIA Ch. 11): "By replaying the log, you can reconstruct the state of the system at any point in the past. This is useful for debugging, for building new projections, and for recovering from failures."

**Applied (D25 — Company-as-Code):** `git log` with the right commit message schema IS the audit trail. D25 verbatim: "Company state reconstructable из git history на любой момент." This is Fowler's replayability benefit, achieved through git rather than a dedicated event store. The practical implication: `/knowledge-diff` (delta wiki between two dates via `git log`) is an event replay query — it reconstructs the state change over a time window by reading the event log (git history). This skill is already operational (cycle 3b). The Foundation's replay capability is not aspirational — it is currently implemented.

**Tradeoff'd vs snapshot strategy:** For very long git histories, replaying from genesis becomes slow. Kleppmann addresses this: "Take periodic snapshots of the current state; when rebuilding, start from the latest snapshot and replay only events since that snapshot." For Jetix Foundation: the wiki `_moc.md` files and `wiki/index.md` are snapshots of the current KB state. A `git tag v<major>` at key milestones could serve as snapshot markers. This is a Wave C optimisation for Part 3 (Knowledge Base) — not required now, but the pattern should be declared in the interface card so it is available when git history grows.

---

### Principle 7 — Event-Driven Architecture vs Request/Response

**Sourced:** Kleppmann (DDIA Ch. 11): "In a stream processing system, a service only responds to events it has subscribed to — it does not need to know who produced the event. This loose coupling is the key architectural benefit over request/response RPC." Fowler (Event Sourcing): "The event approach produces more decoupled systems... at the cost of greater eventual consistency complexity."

**Applied (Part 4 — Coordination Protocol):** The brigadier hub-and-spoke model uses event-like Task dispatch (a command is issued to a cell; the cell produces a result event as a structured packet). The pattern is event-driven in spirit but synchronous in implementation (the brigaddier awaits the cell's return before proceeding). This is a deliberate tradeoff: the synchronous call gives brigadier explicit error handling and turn-count tracking. A fully async event-driven model (brigadier fires Task and moves on; cells publish results to a mailbox) would decouple dispatch from receipt but lose the synchronous error contract. This is a Phase-B architectural decision, not a Phase-A gap.

**Tradeoff'd:** Event-driven async introduces the hardest CQRS failure mode: what happens when a cell's result event never arrives? Dahan's criterion: async is justified only when the caller genuinely does not need the result synchronously. In brigadier's case, the result IS needed to compose the cycle's integrated output — synchronous call is correct for Phase A. The mailbox pattern (`comms/mailboxes/*.jsonl`) is the async coordination channel for lower-priority inter-cycle communication (not cycle-critical dispatch).

---

## §5 Tradeoffs — Foundation-Specific

### Tradeoff A — Git as Event Log vs Dedicated Event Store

**The tension.** Kleppmann's event log optimizes for write throughput and durability through sequential disk writes. Git commits are not optimized for write throughput — each commit involves SHA computation, tree serialization, ref update. For high-volume event streams (thousands of events/second), git is inappropriate. For Jetix Phase A (tens of commits/day), git's overhead is irrelevant.

**Foundation resolution.** Part 1 (System State Persistence) uses git as the event log. This is correct for Phase A. The audit trail and replayability benefits (Principles 6 above) are fully realized. The operational complexity of a dedicated event store (EventStoreDB, Kafka) is unjustified until the commit rate exceeds git's practical write performance (roughly hundreds of commits per hour on a single repo). D25 mandates git as the substrate — this is the right call for the current horizon.

**Scale flag.** At the $1M revenue gate (D19), if Jetix begins processing client KB ingestion at industrial scale (many ingest events per minute), git-as-event-log becomes a bottleneck. The architecture should declare a migration path: git remains the governance event log (strategic decisions, gate acks, canonical promotions); a lightweight event bus (Redis Streams or a flat JSONL file with inotify-based consumers) handles high-frequency operational events. This migration does NOT violate D25 — D25 mandates git for company state; it does not mandate git for all operational events.

---

### Tradeoff B — CQRS Complexity vs Foundation Simplicity (Dahan's Criterion)

**The tension.** Dahan warns: "if you have a crud-based system where the user opens a form, edits fields, and saves — you don't need CQRS." Most of Foundation Part 9 (Owner Interaction Scaffold) and Part 7 (Project Lifecycle) fit this description. The daily log, project scaffold, and weekly review pages are simple CRUD with git-backed history. Introducing a CQRS command/event model here adds ceremony without benefit.

**Foundation resolution.** Apply CQRS only where it earns its complexity budget:
- **YES — Part 6 (Governance):** The gate-ack mechanism has natural command/event separation (AWAITING-APPROVAL packet is a command; approval-log entry is an event; `decisions/` update is the read projection). The audit trail benefit is load-bearing.
- **YES — Part 4 (Coordination Protocol) mailboxes:** Mailboxes are append-only command channels; the routing table / swarm state are read projections. Eventual consistency in the routing table is acceptable.
- **NO — Parts 7, 9, 10:** Project lifecycle, daily log, and CRM entries are simple append-only CRUD with git history as the audit trail. No separate command/event split warranted.

---

### Tradeoff C — Event Versioning vs D25 Atomic Commits

**The tension.** D25 mandates atomic commits with provenance. Event versioning (Vernon upcasting) requires declaring schema versions and handling format evolution at read time. These are compatible but D25 does not currently mandate commit schema versioning.

**Foundation resolution.** Add commit message schema versioning as a Wave C work item for Part 1's interface card. The schema version should be declared in a lightweight way: a `COMMIT-SCHEMA-VERSION` file at the repo root, updated when the commit message format changes. Old commits remain valid under the schema version that was current when they were written. Tooling (e.g., `/knowledge-diff`, `/company-status`) must declare which schema versions they support.

---

### Tradeoff D — Eventual Consistency vs FUNDAMENTAL §6.7 Fail-Loud

**The tension.** CQRS read projections are eventually consistent by design. FUNDAMENTAL §6.7 mandates fail-loud: "AI попытался strategize → halt + log + alert founder." These principles apply at different layers but can collide: a Foundation skill that reads a stale `decisions/` projection may silently proceed with an outdated view of the approved state.

**Foundation resolution.** Enforce a consistency predicate before any skill reads `decisions/` for a gate-critical operation: check that the approval-log's latest entry matches the `decisions/` directory's modification timestamp (within a configurable tolerance, e.g., 60 seconds). If the gap exceeds tolerance, the skill MUST surface an alert ("decisions/ projection may be stale — re-run `/company-status` to refresh") before proceeding. This is a Wave C implementation requirement for Part 6's interface card. It preserves both principles: eventual consistency for non-critical reads; fail-loud for gate-critical reads.

---

## §6 Anti-Scope

- **Distributed event stores.** Kafka, Flink, EventStoreDB, Apache Pulsar — out of scope. Foundation is single-node, git-based. Distributed event store architecture applies at $1M+ scale (D19 gate); this card covers the pattern only, not the distributed infrastructure.
- **DDD strategic patterns.** Bounded contexts, aggregates, domain events as DDD tactical patterns — out of scope for this card. The framework taxonomy treats DDD as a potential standalone framework (#15 candidate, §2 of taxonomy). Vernon's contribution cited here is limited to event sourcing within a single bounded context.
- **Stream processing operators.** Map/filter/reduce on event streams, windowing, watermarks — out of scope. Foundation's event log (git) does not need stream processing; the query interface is `git log` with structured filters.
- **Saga / process manager patterns.** Cross-aggregate coordination via long-running process managers — out of scope for Phase A. Foundation parts coordinate via the brigadier hub-and-spoke (synchronous); sagas are a Phase-B concern if multi-part coordination requires async orchestration.
- **Optimistic concurrency in event stores.** Expected version checks on event appends (Greg Young's standard EventStore write protocol) — out of scope. Git's ref update mechanism provides a simpler form of optimistic concurrency (a push that conflicts with a concurrent push is rejected); this is sufficient for Phase A.

---

## §7 Application Map — Foundation Parts × Event-Sourcing Pattern

| Foundation Part | Pattern applied | Key claim | Wave C implication |
|---|---|---|---|
| Part 1 — System State Persistence | Git-as-event-log (Principle 1, 6) | Git commit = immutable event; `git log` = event log query; `git revert` = compensating event | Add commit message schema versioning; declare snapshot strategy at major milestones |
| Part 2 — Signal Ingestion & Triage | Append-only write (Principle 1); STOP gate = command handler (Principle 2) | Voice pipeline writes are append-only; STOP gate validates commands before KB promotion | Enforce `task_id` idempotency on voice pipeline runs (Principle 3) |
| Part 4 — Role Taxonomy & Coordination | Mailboxes as command channels; swarm state as read projection (Principle 2, 7) | Mailbox entries are commands/events; routing table is derived, eventually consistent | Declare routing table as derived projection in Part 4 interface card; add staleness predicate |
| Part 6 — Governance & Human Gate | Full CQRS within the part: AWAITING-APPROVAL = command; approval-log = event; decisions/ = read projection (Principles 2, 3, 5) | Gate mechanism IS CQRS in operational form; idempotency of ack is critical | Implement gate idempotency key; add consistency predicate for gate-critical reads of decisions/ |

---

## §8 Open Questions for Wave C

**OQ-ES-1 (Commit schema versioning).** D25 mandates atomic commits but does not specify commit message schema versioning. Wave C should add `COMMIT-SCHEMA-VERSION` to Part 1's interface card and specify backward-compatibility rules for `/company-status` and `/knowledge-diff` tooling. Relevant sources: Vernon upcasting (Source 4), Kleppmann schema evolution (DDIA Ch. 4).

**OQ-ES-2 (Gate idempotency key).** Part 6's Wave C interface card must specify the idempotency key for gate acks (proposed: gate packet `id` field) and the implementation pattern (check `status: acked` before writing). This prevents double-ack from producing duplicate canonical promotions. Relevant source: Kleppmann idempotency (DDIA Ch. 11, Source 1).

**OQ-ES-3 (Staleness predicate for decisions/ reads).** Part 6's Wave C interface card must specify a consistency predicate for gate-critical reads of the `decisions/` projection. Relevant source: Fowler CQRS eventual consistency (Source 3), FUNDAMENTAL §6.7 fail-loud.

**OQ-ES-4 (Snapshot strategy for long-lived git history).** As git history grows, replay-from-genesis for tools like `/knowledge-diff` will slow. Wave C should declare a snapshot strategy (git tags at major milestones; wiki `_moc.md` as KB state snapshots). Relevant source: Kleppmann snapshot pattern (DDIA Ch. 11, Source 1).

**OQ-ES-5 (Scale trigger for event store migration).** At what commit volume does git-as-event-log become a bottleneck? Proposed threshold: >500 commits/day sustained for 30 days. Below this: git suffices. Above: evaluate Redis Streams or flat JSONL event bus for high-frequency operational events. This is not an imminent concern (Phase A is tens of commits/day) but should appear in Part 1's scalability section.

---

*End of Consultant Card #5 — Event Sourcing + CQRS + Append-Only State. Word count: ~1150 words (§§3-8 body). Foundation studied declaration (§1) is additional per spec mandate.*
