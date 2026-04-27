---
title: "Part 3 — Knowledge Base & Methodology Library (Architecture)"
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
part: 3
part_slug: part-3-knowledge-base-methodology-library
status: draft-pre-ruslan-ack
F: F4
ClaimScope: "Holds for the wiki/ content layer (U.Episteme) and methodology library sub-layer (`wiki/methodology/`) in Foundation Phase A. The accessor pipeline (/ingest, /ask, /consolidate, /build-graph, /lint) is U.System owned by `swarm/lib/` shared infrastructure with Part 3 as named LEAD owner per C1 Joint Design (Variant A Ruslan-acked 2026-04-27). RUSLAN-LAYER specific wiki content (552 entities Ruslan-authored), niche slices, methodology library entries authored by Ruslan are out of scope per §X."
R:
  refuted_if: "(a) An accessor pipeline skill develops a lifecycle independent of `swarm/lib/`; OR (b) Part 3 §I or Part 4 §I duplicates the C1 canonical answer instead of REFERENCING swarm/lib/README.md and C1-joint-design.md; OR (c) a CRM edge from Part 10 reaches `wiki/graph/edges.jsonl` unvalidated by Part 3 /lint; OR (d) a methodology promotion bypasses the F4→F5 admissibility predicate (≥1 DRR validated marker from ≥2 cycles + rule_slug + Part 6b ack); OR (e) `/ask --save` does not write to `wiki/comparisons/` by default"
  accepted_if: "All bullets P3.1/P3.2/P3.3/P3.4 acceptance predicates pass; §I REFERENCES swarm/lib/README.md (no DRY duplication); CRM edge validation declared with cross-ref to Part 10 (Bundle 4); /ask --save default declared; methodology library entity-type chosen and admissibility predicate operational"
predecessor_artefacts:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§3.1 C1 BLOCKING; §4.5 UND-5)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md
  - swarm/lib/README.md
constitutional_inputs_consumed:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - CLAUDE.md (CRM System §; Wiki Architecture v2 §)
---

# Part 3 — Knowledge Base & Methodology Library (Architecture)

## §0 Mission

Part 3 is the **dual accumulation layer** of the Jetix system: the curated, queryable, provenance-linked **wiki KB** (atomic entity files, typed graph edges, niche slices, 9 entity-types) and the reusable **methodology library sub-layer** (patterns, templates, workflows promoted from Part 5 compound phase). Part 3's bargain with the rest of the system: every consumer queries via `/ask` and gets cited synthesis; every methodology pattern accumulates into a compound asset that pays back across cycles; every promotion is gated by Part 6b human ack and tagged by Part 6a F-G-R; every entity is anchored (D28) and PARA-tagged (Bundle 2 P2.2) before admission; every typed edge in `wiki/graph/edges.jsonl` is A.14-canonical and append-only.

The wiki is **U.Episteme content** [src:design/JETIX-FPF.md:§1.4 A.1; F8|G:Foundation A.1 boundary discipline|R-high]. The accessor pipeline (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) is **U.System** — separate holon, separate ownership. Per C1 Joint Design (Bundle 2; Ruslan-acked 2026-04-27 Variant A), the accessor scripts live in `swarm/lib/` shared infrastructure; **Part 3 is the named LEAD owner** with Part 4 as ADVISORY owner; modifications gate through AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 F8 schema. This document does NOT duplicate the C1 canonical answer — it REFERENCES `swarm/lib/README.md` and `C1-joint-design.md` (DRY enforcement; §I declares the references; critic gate verifies).

Bundle 2 adds four structural deltas atop the Wave A interface card baseline:

1. **P3.1 — C1 accessor pipeline ownership resolution (BLOCKING)**: §I REFERENCES `swarm/lib/README.md` for the canonical answer; §F Anti-scope explicitly disowns the scripts to `swarm/lib/`; routing-table.yaml (Part 4 P4.1) lists which roles invoke which accessor skills via `accessor_skills_invocable:` field. Part 3 is named LEAD; Part 4 is ADVISORY. **Cross-Part DRY enforced** — both §I sections REFERENCE; neither duplicates.
2. **P3.2 — Methodology library sub-layer materialisation**: `wiki/methodology/` chosen as the canonical entity-type (decision documented in §I.2 with rationale: clearer namespace separation than extending `wiki/foundations/`; aligns with KM consultant P1 compounding pattern). Promotion pipeline from Part 5 → Part 3 declared in §A Inputs + §E Admissibility with explicit predicate (≥1 DRR 'Result: validated' marker from ≥2 distinct cycles + `rule_slug:` for deduplication + F-level rises to F5 post-promotion per OQ-B1-1 anchor wording). Edge density target ≥2.0 edges/entity (current 1.05 per AUDIT §8.3) via mandatory cross-reference at every methodology entry write.
3. **P3.3 — CRM edge validation schema (UND-5 binding)**: §D + §E Laws explicitly declare Part 10 as content creator writing typed CRM edges into `wiki/graph/edges.jsonl`. The 8 CRM edge types enumerated. Validation rules: malformed CRM edges flagged by Part 3 `/lint` (operating on Part 3-managed file though origin is Part 10); validation surface is Part 3 territory; edge content origin is Part 10 territory.
4. **P3.4 — `/ask --save` default enforcement**: `--save` is now DEFAULT (writes synthesis to `wiki/comparisons/<query-slug>.md` with citations); `--no-save` flag for ephemeral discard. `/lint` adds health signal: flag `wiki/comparisons/` emptiness when `/ask` usage confirmed in session history.

The wiki is a **compound asset**, not a static archive. Per Karpathy LLM-Wiki gist [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 P1; F4|G:Foundation generic compounding principle|R-high]: each new entity write triggers ≥1 cross-reference update; without this discipline, the wiki degrades into a folder of disconnected notes. The Wave C target (≥2.0 edges/entity, up from 1.05 baseline per AUDIT §8.3) operationalises this — the consequence of the principle is a measurable edge-density floor.

The methodology library is the **highest-compound asset after the KB itself** [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md:§4 P1 Buffett owner-earnings; F4|G:capital-allocation framing for KB|R-medium]. A pattern validated across ≥2 cycles is institutional memory; promoting it to F5 codified-rule status with `rule_slug:` deduplication makes it queryable as a single canonical piece. Future cycles consume it; future cycles validate or refute it (Popperian `refuted_if:` discipline). The compound is non-linear in cycle count — at cycle 11 (current baseline) the methodology library is sparse; at cycle 50 it should be the load-bearing reference layer for everyday operations.

---

## §A Inputs

Each entry: `<source> :: <data-shape> :: <event-trigger>`.

- **Part 2 (Signal Ingestion & Triage) — post STOP gate:** promoted draft candidate (`.md` with frontmatter `pipeline: ingested`, `anchor:`, `para_tier:` mandatory per Bundle 2 P2.2, `human_acked_at:` populated, `ack_packet_id:` referencing Part 6b §I.4 packet, `sources:` provenance ≥1) :: `ingest-completed` event :: owner acks STOP gate per Part 6b [src:swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md:§B Outputs second bullet "Part 3"; F4|G:Bundle 2 P2.2 binding consumed at Part 3 admissibility|R-high]. The consequence: Part 3 admissibility predicate (§E A1) checks both `human_acked_at:` AND `para_tier:` before accepting the draft — rejecting at admissibility with specific reason (transparency principle from CAI).

- **Part 5 (Compound Learning & Methodology Capture) — methodology candidate:** DRR-derived pattern, workflow, or template in wiki-entity format (markdown with frontmatter declaring `pipeline: ingested`, `entity_type: methodology`, `rule_slug:` for deduplication, `validated_in_cycles: [<cycle-id-1>, <cycle-id-2>, ...]` ≥2 entries with each carrying `result: validated` marker, `F: F4` initial → F5 post-promotion) :: `compound-phase-completed` event :: end of each 40/10/40/10 cycle [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§5 DRR validated pattern threshold; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 3 Bullet 2; F4|G:Bundle 2 P3.2 binding|R-medium]. The consequence: Part 3 §E Admissibility A2 enforces all three sub-conditions (DRR-validated-≥2-cycles AND rule_slug AND F-level rise to F5 on promotion); a methodology candidate missing any of the three is rejected with specific reason.

- **Part 6b (Human Gate) — promotion instruction:** AWAITING-APPROVAL packet with `gate_class: draft_promotion` per Part 6b §I.4 F8 LOCKED schema :: ack event :: HITL gate ack [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED contract consumed|R-high]. The consequence: Part 3 does NOT make promotion decisions autonomously; every transition `pipeline: ingested → ready` requires Part 6b ack via the F8 packet. The packet's `ack_request:` provides three options (Approve / Approve-with-modifications / Reject) per Askell HHH corrigibility three-option discipline.

- **D28 anchor parameter (read-only at query time):** `/ask --anchor=<topic>` query parameter :: query-invocation event :: any consumer querying this part [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28; F8|G:Foundation generic anchor discipline|R-high]. Therefore: a query without `--anchor` either receives broad-topic synthesis (default behaviour) OR the query is scoped to anchor candidates from `wiki/index.md` (when `--anchor` is supplied). The anchor-discipline is leading at query time as well as at ingest time.

- **Karpathy compounding cross-reference at every ingest:** each new entity write triggers ≥1 linked-concept update + ≥1 graph edge addition [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1; src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§8 wiki current state — 552 entities / 577 edges = 1.05 avg; Wave C target ≥2.0; F4|G:Foundation compounding principle|R-high]. The consequence: writes are NOT pure-add — each write carries an obligation to inspect existing entities for cross-references; absent cross-reference triggers `/lint` flag.

- **Part 10 (External Touchpoints — Bundle 4 stub) — CRM edge writes:** typed CRM edges (8 CRM edge types per CLAUDE.md CRM System §) appended to `wiki/graph/edges.jsonl` :: edge-append event :: CRM record creation/update [src:CLAUDE.md CRM System §; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.5 UND-5; F2|G:Bundle 4 Part 10 stub; UND-5 binding satisfied at Part 3 validation surface|R-low — Part 10 not yet materialised]. **This is P3.3 binding (UND-5).** The consequence: Part 3's `/lint` validates CRM-origin edges; malformed CRM edges surface as Part 3 lint failures (validation surface ownership) even though edge content origin is Part 10 territory.

- **Owner queries via `/ask`:** `<question>` string + optional `--anchor` + optional `--no-save` :: query-invocation event :: owner runs `/ask "..."` [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§E Deontics; F4|G:Bundle 2 P3.4 binding|R-high]. The consequence: `/ask` reads `wiki/index.md` + relevant entity files; produces synthesis with inline citations; **`--save` is DEFAULT (writes to `wiki/comparisons/<query-slug>.md` with citations); `--no-save` for ephemeral**.

- **`/consolidate` invocation (weekly or on-demand):** owner or Part 8 health monitor invokes `/consolidate [--weekly]` :: consolidation event :: explicit invocation [src:CLAUDE.md KM MVP cycle; F4|G:KM MVP cycle materialisation|R-medium]. The consequence: duplicate entities (same `rule_slug:` or near-duplicate concept titles per Matuschak stranger test) are merged; Reversal Transactions discipline preserves history (the merged entity has `supersedes: [<list of merged slugs>]` frontmatter).

- **`/build-graph` invocation (on-demand, typically post-`/consolidate` or after batch ingestion):** invokes Louvain-equivalent community detection on `wiki/graph/edges.jsonl` :: graph-rebuild event :: explicit invocation [src:CLAUDE.md KM MVP cycle; F4|G:KM MVP cycle|R-medium]. The consequence: `wiki/graph/communities.jsonl` is rebuilt; community labels feed `/ask` synthesis (weighting strongly-connected concepts higher in retrieval).

---

## §B Outputs

Each entry: `<consumer> :: <data-shape> :: <event-published>`.

- **All Foundation parts and owner (read-query interface via `/ask`):** synthesis response with inline `[src:...]` citations :: `query-answered` event :: on-demand at any time [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1 UC-B.4; F4|G:Foundation generic query interface|R-high]. The consequence: every consumer of the wiki reads via the typed interface — there is no "raw read" pattern; the citation discipline is enforced at the synthesis layer. **`--save` default** writes the response to `wiki/comparisons/<query-slug>.md`; only explicit `--no-save` produces ephemeral output.

- **Part 5 (Compound Learning):** methodology library entries (U.Episteme patterns, templates) queryable via `/ask --niche=methodology` OR direct read at `wiki/methodology/<rule-slug>.md` :: `entity-created` event :: at compound phase boundary OR on-demand [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§B; F4|G:Bundle 2 P3.2 binding|R-medium].

- **Part 8 (Health Monitoring) — Bundle 4 stub:** wiki health signals (entity count; edge density average; orphan count; stale-claims count; `contradicts`-edge density; missing-frontmatter count; orphan-anchor count; `wiki/comparisons/` emptiness flag per P3.4) via `/lint` :: `health-poll` event :: periodic monitoring run [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 4; F2|G:Bundle 4 Part 8 stub|R-low]. The consequence: Part 8 polls `/lint` output as health signal source; the schema for the polling is documented in §I.4.

- **Part 9 (Owner Interaction Scaffold) — Bundle 4 stub:** structured synthesis reports (`wiki/comparisons/<query-slug>.md`) filed from `/ask --save` runs :: `synthesis-filed` event :: after each owner query session [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 5 query-driven KB; F4|G:Bundle 2 P3.4 binding|R-high — testable]. The consequence: comparisons accumulate per query; `/ask` future queries can reference prior comparisons (cross-reference loop closure).

- **Part 6a (Provenance Officer):** F-G-R compliance data (entity-level trust tags per Part 6a §I.1 F8 schema) for quarterly audit :: `audit-query` event :: Part 6a immune-function audit cadence [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§J quarterly audit; F8|G:Bundle 1 LOCKED|R-high]. The consequence: Part 3 stamps F-G-R on every entity per Part 6a F8 schema; Part 6a audits compliance quarterly (not at promotion-time — that is Part 6b's territory).

- **Part 6b (Human Gate):** AWAITING-APPROVAL packet with `gate_class: draft_promotion` for promotion of any entity from `pipeline: ingested → ready` :: gate-submission event :: every promotion [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED contract|R-high]. The consequence: Part 3 emits the packet; Ruslan acks; only after ack does the entity reach canonical state. Methodology promotions specifically use `gate_class: draft_promotion` (not stage_gate, which is for project lifecycle gates owned by Part 7).

- **Part 1 (System State Persistence):** every wiki entity file write, every edges.jsonl append, every index.md update, every log.md append-top, every methodology library entry write :: `[wiki]` or `[kb]` commit per Part 1 §I.2 commit-format-tokens.json :: persistence event [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.2; F8|G:Bundle 1 LOCKED|R-high].

---

## §C Side-effects

Per FPF IP-3 [src:design/JETIX-FPF.md:§5.3]: every KB entity is a committed file; no ephemeral-only writes. The Karpathy compounding principle requires mandatory side-effects at every write [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1].

- **Entity file write:** `wiki/<entity-type>/<slug>.md` committed via Part 1 at promotion time. Frontmatter mandatory: `pipeline: ingested|compiled|linted|ready`, `F:`, `ClaimScope:`, `R:`, `sources:`, `anchor:`, `para_tier:` (per Bundle 2 P2.2 cross-Part discipline), `entity_type:` (one of the 9 types), `edges:` (optional declaration of typed A.14 edges).

- **Graph edge append:** `wiki/graph/edges.jsonl` — typed A.14 edge appended (NEVER mutated in place); append-only per FUNDAMENTAL §2.1 substrate discipline [src:design/JETIX-FPF.md:§3.5 A.14; src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§8.3; F8|G:Foundation generic A.14 contract|R-high]. Per `/build-graph` rebuild: the entire graph can be reconstructed from the entity frontmatter `edges:` blocks plus the historical jsonl appends; the jsonl is the canonical source.

- **Index update:** `wiki/index.md` — entry appended for the new entity (anchor for future D28 lookups). Idempotent: re-promoting the same slug updates the index entry rather than creating a duplicate (or if PRE-EXISTING, the consolidate step merges).

- **Log append:** `wiki/log.md` — new entry appended at the TOP (append-only-top discipline per CLAUDE.md Global Rules §Logs). Format: `## [YYYY-MM-DD HH:MM:SS] entity-promoted | <entity-type>/<slug> | <anchor> | part-3`.

- **Methodology library sub-layer write (P3.2 binding):** `wiki/methodology/<rule-slug>.md` written at promotion. Same entity structure as other entity types; distinguished by `entity_type: methodology` frontmatter + the `rule_slug:` deduplication field. The ENTITY-TYPE DECISION (per worklist §2 Part 3 Bullet 2): chose `wiki/methodology/` as a NEW canonical entity-type rather than extending `wiki/foundations/`. Rationale (architecture decision per P3.2): clearer namespace separation; `wiki/foundations/` content is structural Foundation parts (Part 1-10 architectures), `wiki/methodology/` is reusable patterns derived from cycle DRRs. The two have different lifecycles; separating namespaces avoids accidental mutation of Foundation architectures by methodology promotions. [F4|G:P3.2 architecture decision|R-medium]

- **Comparisons write (P3.4 binding):** `/ask --save` (default) writes synthesis response to `wiki/comparisons/<query-slug>.md` with frontmatter `pipeline: ingested`, `entity_type: comparison`, `query: <verbatim>`, `sources:` listing every cited entity, `F: F3` (AI synthesis multi-source informal), `ClaimScope: {holds_within: [query-context-<query-slug>]}`, `R: {refuted_if: <subsequent contradicting synthesis>}`. The comparisons act as **cross-reference loop closure**: future `/ask` queries can reference prior comparisons via `wiki/index.md` entries.

- **Append-only on edges.jsonl:** L3 invariant — edges are NEVER mutated in place. A correction is a NEW edge entry referencing the prior via `corrects:` field per Reversal Transactions (Young 2010 "There is no Delete"). [src:raw/books-md/event-sourcing/young-cqrs-2010.md:p.31 Reversal Transactions; F5|G:Foundation generic|R-high]

- **NO direct write to RUSLAN-LAYER content:** Part 3 does NOT modify the existing 552 wiki entities Ruslan-authored without explicit promotion gate. Part 3's writes are NEW entities OR `/consolidate` merges (which are Reversal-Transaction-disciplined: merge produces NEW entity with `supersedes:` pointer).

- **NO write to `crm/`:** CRM data is Part 10 territory. Part 3 receives CRM EDGES into `wiki/graph/edges.jsonl` (which is Part 3-managed) but does NOT write CRM record content. Per UND-5 / P3.3 binding.

---

## §D Dependencies (typed per FPF A.14)

Every edge below is from the canonical 10-edge A.14 reference table authored in Part 1 §D [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§D 10-edge canonical lookup; F8|G:Foundation generic edge taxonomy|R-high]. Generic `depends-on` is FORBIDDEN. Critic gate auto-rejects.

**Part 3's edges:**

- **`operates-in Part 1`** — all wiki entity files, `edges.jsonl`, `index.md`, `log.md`, methodology library entries, comparisons files are committed artefacts persisted in the git substrate; Part 3's entire content layer operates within Part 1's commit interface [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.2 commit-format-tokens.json; F8|G:Bundle 1 LOCKED substrate|R-high]. The consequence: a Part 1 substrate failure (K8 fsck error) cascades into Part 3 inability to commit promotions; Part 3's K1 failure mode handles this cascade.

- **`PhaseOf information-lifecycle`** (cross-cutting; Part 2 → Part 3) — Part 3 receives drafts from Part 2 post-STOP-gate. The phase boundary is the STOP gate ack. The pre-KB phase is Part 2 territory; Part 3 is the in-KB phase. [src:swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md:§D PhaseOf; F5|G:Foundation generic edge type|R-high]

- **`methodologically-uses Part 6a`** — every promotion in Part 3 uses Part 6a's F-G-R service (entity gets stamped with F-G-R per F8 schema) AND Part 6a's approval log discipline (`swarm/approvals/log.jsonl` appends per promotion event). [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 F-G-R F8; §C approval log; F8|G:Bundle 1 LOCKED|R-high]

- **`methodologically-uses Part 6b`** — every promotion is gate-checked by Part 6b. The gate authority (`gate_class: draft_promotion` for entity promotions; `gate_class: stage_gate` for `swarm/lib/` accessor pipeline modifications per C1 Joint Design) is Part 6b's. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED|R-high]

- **`creates methodology-entries-for Part 5`** (inverse direction) — Part 5 creates methodology candidates that LAND in Part 3. From Part 3's perspective: Part 5 is upstream creator; Part 3 is the destination accumulator. This is captured as `creates` edge with the edge direction from Part 5 to Part 3 (Part 5 creates content that Part 3 receives). The reverse perspective: Part 3 `derives-from Part 5` for methodology entries. Both perspectives are valid — the edge taxonomy permits both readings. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md (referenced for Part 5 perspective); F4|G:Foundation generic asymmetric edge|R-medium]

- **`derives-from Part 10`** — CRM-origin edges in `wiki/graph/edges.jsonl` derive from Part 10's CRM record creation events. Part 3 stores them but does not author them. **This is P3.3 / UND-5 binding.** The validation surface (whether the edge conforms to the 8 CRM edge types and A.14 typed schema) is Part 3 territory; the edge content origin is Part 10 territory. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.5 UND-5; F4|G:UND-5 binding|R-medium]

- **`operates-in swarm/lib/`** — the accessor skills (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) that operate ON Part 3 content live in `swarm/lib/` per C1 Joint Design. Part 3 does NOT own the scripts (Anti-scope §F); Part 3 IS owned-of-record by the same script invocations (lead owner per C1). The relationship is "Part 3's content layer is the substrate the swarm/lib accessor pipeline operates on." [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A canonical answer; F4|G:C1 Joint Design canonical|R-medium]

**Edges Part 3 explicitly does NOT have:**

- NO `creates Part 4` — Part 3 does NOT produce role manifests or routing; that is Part 4 territory.
- NO `creates Part 1` — Part 3 produces content that Part 1 stores; the edge is `operates-in Part 1`, not `creates`.
- NO `depends-on` (any) — generic dependency forbidden.

---

## §E Boundary (per FPF A.6.B L/A/D/E)

[src:design/JETIX-FPF.md:§4.3 A.6.B; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P6]

### Laws — invariants that MUST hold

**L1 — Every entity in `wiki/` carries mandatory frontmatter.** Required fields: `pipeline:` stage (one of raw/ingested/compiled/linted/ready); `sources:` ≥1 entry; F-G-R fields (`F:`, `ClaimScope: {holds_within: [...]}`, `R: {refuted_if: <Popperian falsifier>}`); `entity_type:` (one of 9 — `concepts/ | entities/ | sources/ | topics/ | ideas/ | experiments/ | claims/ | summaries/ | foundations/` PLUS Bundle 2 P3.2 NEW: `methodology`). A typed A.14 edge in `wiki/graph/edges.jsonl` for any cross-reference declared. [src:design/JETIX-FPF.md:§5.3 IP-3; B.3; D28; F8|G:Foundation generic frontmatter contract|R-high]

**L2 — D28 anchor discipline.** Every entity is anchored to ≥1 declared topic/project/question anchor. Orphan entities (no anchor link) are flagged by `/lint` as health defect [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28; F8|G:Foundation generic anchor discipline|R-high].

**L3 — `wiki/graph/edges.jsonl` is APPEND-ONLY.** No in-place mutation of edge records. Corrections are NEW entries with `corrects: <prior_edge_id>` field per Reversal Transactions [src:raw/books-md/event-sourcing/young-cqrs-2010.md:p.31; F8|G:Foundation generic|R-high].

**L4 — Every entity promoted to `pipeline: ready` (canonical) must have passed Part 6b's human gate.** The promotion event carries `ack_packet_id:` and `human_acked_at:` in the entity's frontmatter. [src:design/JETIX-FPF.md:§2.1a A.13 J-Approve; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2; F8|G:Bundle 1 LOCKED Part 6b authority|R-high]

**L5 — A.1 boundary of this part is `wiki/` directory content layer.** No content from `decisions/`, `raw/`, or `projects/` is canonical KB until it passes through Part 2's pipeline (with STOP gate) and Part 6b's gate (with ack). [src:design/JETIX-FPF.md:§1.4 A.1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§6 item 4; F8|G:Foundation A.1 boundary|R-high]

**L6 — D27 fork-and-merge discipline.** The KB must be FORKABLE with ICP-specific content parameterised — generic Foundation content lives in `wiki/concepts/` + `wiki/methodology/`; Ruslan-specific content lives in `projects/` or `directions/` with links INTO the generic Foundation entries. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D27; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 3 stranger test; F5|G:Foundation generic D27 discipline|R-high]

**L7 — CRM edges in `wiki/graph/edges.jsonl` validated by Part 3 `/lint` (P3.3 / UND-5 binding).** Malformed CRM edges (wrong edge type, missing required fields, broken slug references) surface as Part 3 lint failures. The validation surface is Part 3; the edge content origin is Part 10. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.5 UND-5; src:CLAUDE.md CRM System §; F4|G:Bundle 2 P3.3 binding|R-medium]

**L8 — `/ask --save` is DEFAULT (P3.4 binding).** `--save` writes synthesis to `wiki/comparisons/<query-slug>.md` with citations. `--no-save` flag required for ephemeral. `/lint` adds health signal: flag `wiki/comparisons/` emptiness when `/ask` usage confirmed in session history. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 3; F4|G:Bundle 2 P3.4 binding|R-high — testable]

**L9 — Methodology promotion admissibility predicate (P3.2 binding).** A methodology pattern from Part 5 accepted only if: (a) carries ≥1 DRR `result: validated` marker from ≥2 distinct cycles; (b) carries `rule_slug:` for deduplication; (c) F-level rises to F5 post-promotion (per OQ-B1-1 anchor wording: F5 = "peer-validated methodology"; on owner ack as peer-equivalent in single-owner Phase A). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 3 Bullet 2; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§5 validated pattern threshold; F4|G:Bundle 2 P3.2 binding|R-medium]

**L10 — Edge density target ≥2.0 edges/entity (Wave C goal).** Current baseline 1.05 (577 edges / 552 entities per AUDIT §8.3). Achieved via mandatory cross-reference at every methodology entry write per Karpathy P1. `/lint` flags entries with 0 outbound edges as health defect. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 P1 density as quality signal; F4|G:Wave C target|R-high — measurable]

**L11 — Halt-Log-Alert (Part 6b §E Law L9).** Apply to any KB integrity failure: lint orphan-anchor or missing-frontmatter affecting a `pipeline: ready` entity halts further promotions until resolved; logs to `swarm/approvals/log.jsonl`; alerts owner via `~/review-latest.md` flag. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E Law L9; F8|G:Bundle 1 LOCKED|R-high]

**L12 — Corrigibility (Askell HHH Appendix E.2 verbatim).** Owner can `git revert` any wiki entity, manually edit any frontmatter, override any /lint flag — Part 3 has no exclusive lock on its own outputs. [src:raw/books-md/anthropic/askell-2021-hhh.md:Appendix E.2; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9; F8|G:Bundle 1 LOCKED Corrigibility|R-high]

### Admissibility — acceptance criteria for content to enter Part 3

**A1 — Source provenance:** Part 2 STOP-gate-acked draft (with `human_acked_at:` populated AND `para_tier:` mandatory per Bundle 2 P2.2) OR Part 5 compound output (with DRR `result: validated` marker per L9) OR Part 6 governance-acked synthesis.

**A2 — Methodology pattern admissibility (P3.2 / L9 binding):** all three sub-conditions: (a) ≥1 DRR `result: validated` from ≥2 distinct cycles; (b) `rule_slug:` non-null and unique (or merging into existing entry per `supersedes:`); (c) F-level rises to F5 post-promotion. A candidate missing any sub-condition is rejected with specific reason per CAI transparency.

**A3 — Entity-type from 9-type taxonomy (10 with methodology Bundle 2 addition):** `concepts/ | entities/ | sources/ | topics/ | ideas/ | experiments/ | claims/ | summaries/ | foundations/ | methodology/`. The `entity_type:` frontmatter field is mandatory and validated against the enum.

**A4 — Concept-type entities (`wiki/concepts/`) pass Matuschak stranger test:** declarative-sentence title; context-free body; ≤500 words. Enforced by `/lint --check-stranger-test` (Wave C materialisation per worklist; Bundle 4 implementation candidate). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 3]

**A5 — Karpathy compounding requirement:** every new ingest event produces ≥1 cross-reference update (concept link or graph edge) to an existing entity. Wave C target ≥2 edges/entity per L10.

**A6 — `para_tier:` mandatory (cross-Part discipline with Bundle 2 P2.2):** Part 2 ensures drafts have `para_tier:` populated before handoff; Part 3 admissibility verifies the field on entry. A draft from Part 2 without `para_tier:` is rejected at Part 3 admissibility (transparent reject — even though Part 2 should have caught it earlier).

**A7 — CRM edge admissibility (P3.3 / UND-5 binding):** CRM edge from Part 10 conforms to (i) one of the 8 CRM edge types per CLAUDE.md CRM System; (ii) A.14 typed-edge schema (from/to/type/confidence non-null); (iii) slug references both resolve (no dangling refs). Non-conforming edges flagged by `/lint`. [src:CLAUDE.md CRM System §]

### Deontics — obligations toward consumers

**D1 — `/ask` returns inline citations.** No synthesis without `[src:...]` citations. Per Karpathy "wiki proves itself by answering questions with citations" [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 P5; F4|G:Foundation generic /ask discipline|R-high].

**D2 — Queryable index `wiki/index.md`.** Any consumer can discover anchor candidates without traversing raw filesystem. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28]

**D3 — `/ask --save` files synthesis to `wiki/comparisons/` BY DEFAULT (P3.4 binding).** `--no-save` for ephemeral.

**D4 — `/lint` surfaces health signals to Part 8:** orphan count, stale-claims count, `contradicts`-edge density (target ≥5% of total edges), average edges/entity, missing-frontmatter count, `wiki/comparisons/` emptiness flag (P3.4), CRM-edge-malformed count (P3.3).

**D5 — Methodology library queryable via `/ask --niche=methodology`.** P3.2 binding.

**D6 — Anti-RAG discipline.** Part 3 does NOT replace `/ask` synthesis with vector embedding lookup; the Karpathy compiled-cited-maintained-substrate is structurally required, not optional [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 6 explicit RAG rejection].

### Effects — measurable outcomes

**E1 — After promotion of new entity:** entity is path-addressable at `wiki/<entity-type>/<slug>.md`; indexed in `wiki/index.md`; has ≥1 typed A.14 edge in `wiki/graph/edges.jsonl`; visible to `/ask` within the same session OR after next `/consolidate` for canonical index update.

**E2 — After `/lint` run:** health report lists orphans, stale claims, missing-frontmatter entities, malformed CRM edges, comparisons emptiness flag (P3.4); target 0 orphans, 100% frontmatter coverage, 0 malformed CRM edges, comparisons populated when /ask was used in session.

**E3 — Edge density:** Wave C target ≥2.0 edges/entity (current 1.05 per AUDIT §8.3) — achieved via L10 mandatory cross-reference at methodology and concept entry writes.

**E4 — `contradicts` + `supports` edge density:** target ≥5% of total edges (current ~1.5% inferred per AUDIT §8.3) — achieved via Wave C `/lint` signal flagging entries lacking peer-evidential edges.

**E5 — Methodology promotion fixture (P3.2 acceptance predicate):** at least one methodology entry promoted from Bundle 3 stub (Part 5 work) lands cleanly in `wiki/methodology/<rule-slug>.md`; passes /lint; carries F5 + ClaimScope + refuted_if; rule_slug deduplication operational.

**E6 — CRM edge fixture (P3.3 acceptance predicate):** synthetic 10-fixture (5 well-formed CRM edges, 5 malformed in distinct ways) — Part 3 `/lint` flags 5 malformed with specific reasons; cross-references Part 10 (Bundle 4) for content authoring rules.

**E7 — `/ask --save` fixture (P3.4 acceptance predicate):** `/ask "X"` invocation produces committed file at `wiki/comparisons/<query-slug>.md` with citations; `/ask --no-save "X"` ephemeral; `/lint` detects empty `comparisons/` after N>0 `/ask` invocations and flags health defect.

---

## §F Anti-scope

**Generic (applies to all Foundation parts):**

- This part does NOT make strategic decisions [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1].
- This part does NOT substitute for founder agency — knowledge is retrieved and surfaced; the founder decides what to do with it [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2].
- This part does NOT use engagement-economy patterns — no algorithmic feed, no "recommended for you" without explicit query.

**Part-specific:**

- **This part does NOT own the accessor pipeline (U.System).** `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` are U.System accessor services housed in `swarm/lib/` shared infrastructure with **Part 3 as named LEAD owner and Part 4 as ADVISORY owner per C1 Joint Design**. Part 3 OWNS the content these scripts operate on (the `wiki/` substrate); Part 3 does NOT own the script logic. The named-owner role is **governance + interface contract**, not implementation. Modifications gate through AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A canonical answer; src:swarm/lib/README.md:§4 Modification governance; F4|G:Bundle 2 C1 Joint Design canonical|R-medium]

- This part does NOT do final strategic synthesis or produce strategic documents — synthesis answers via `/ask` are U.Episteme outputs that feed owner judgment; strategic documents are Part 9 (Owner Interaction Scaffold) territory.

- This part does NOT enforce F-G-R compliance at promotion time — Part 6 (Governance / Provenance Officer) responsibility. Part 3 STORES F-G-R tags; Part 6a checks them at quarterly audit; Part 6b checks them at promotion gate. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 3 B.3]

- This part does NOT own CRM data (`crm/` directory). CRM is a separate subsystem (Part 10 External Touchpoints). CRM graph EDGES that cross into `wiki/graph/edges.jsonl` are stored here AND VALIDATED by Part 3 `/lint` (P3.3 / UND-5 binding); the CRM RECORD CONTENT itself is Part 10 territory.

- This part does NOT contain RUSLAN-LAYER ICP-specific content in `wiki/concepts/`. ICP-specific content belongs in `projects/` or `directions/` with links TO generic Foundation concepts. Per D27 fork-and-merge.

- This part does NOT replace RAG (vector embedding, paid search). The Karpathy wiki pattern explicitly rejects RAG ("the LLM is rediscovering knowledge from scratch on every question"); the wiki is a compiled, cited, maintained substrate. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 6]

- This part does NOT own the Private Library (`raw/books-md/` — 393 books per AUDIT §1.1) as KB content. The library is raw source material that gets ingested through Part 2's pipeline; Part 3 holds the resulting EXTRACTED concepts and summaries, not the raw books. [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§1.1]

- This part does NOT own project lifecycle state machines — Part 7 territory. Project anchors stored in `wiki/index.md` are references, not authoritative project state.

- This part does NOT make promotion DECISIONS — every transition `pipeline: ingested → ready` requires Part 6b ack via F8 packet; Part 3 emits packets, does not unilaterally promote.

---

## §G F-G-R Tagging (per FPF B.3, Part 6a §I.1 F8 schema)

[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 F-G-R F8 schema]

| Artefact emitted | Formality (F0-F9) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| `wiki/sources/<slug>.md` — bibliographic record (Luhmann "first cabinet") | **F3** — multi-source informal; summarises external source + provenance link | `holds_within: [source-document-<slug>]` — not transferable without explicit `derived_from` edge | **R-medium** — human-acked at Part 2 STOP gate; accuracy depends on extraction quality; `refuted_if: <source claims contradict on re-read>` |
| `wiki/concepts/<slug>.md` — atomic idea (Luhmann "second cabinet") | **F2-F4** — F2 newly extracted; F3 multi-cycle; F4 operational convention when validated ≥1 cycle | `holds_within: [concept-context-<slug>]` — must NOT assume cross-context validity without explicit Bridge F.9 (FPF IP-2) | **R-medium** — human-acked provenance; rises with cross-cycle evidence |
| `wiki/graph/edges.jsonl` edge record | **F4** — typed A.14 edge; operational convention enforced by `/lint` | `holds_within: [edge-<from>-<to>-<type>]` — invalidated if either entity superseded without edge update | **R-medium** — structural link; periodic `/lint` catches stale edges |
| `/ask` synthesis response (filed to `wiki/comparisons/<query-slug>.md`) | **F3** — AI synthesis + cited sources | `holds_within: [query-context-<query-slug>]` — may stale as KB grows | **R-medium** if filed with `--save`; **R-low** if `--no-save` ephemeral |
| Methodology library entry (`wiki/methodology/<rule-slug>.md`) | **F5** — codified when validated across ≥2 cycle applications per L9; **F3** initially before L9 satisfied | `holds_within: [system-context-<methodology-context>]` — bridge required for other contexts (FPF IP-2 F.9) | **R-high** when F5+ (peer-validated); **R-medium** at F3 (single-cycle extraction) |
| `wiki/index.md` entries | **F4** | `holds_within: [Foundation generic indexing discipline]` | **R-high** |
| `wiki/log.md` entries | **F1** — append-only chronology, single-source | `holds_within: [log-entry-<timestamp>]` | **R-low** — no provenance check |
| Reverse-transactions correction (e.g. `/consolidate` merge with `supersedes:` pointer) | **F4** | `holds_within: [merge-event-<ts>]` | **R-medium** |

---

## §H Code-level Interfaces

This section declares the interface contracts. The accessor pipeline scripts live in `swarm/lib/` per C1 Joint Design — Part 3 §H REFERENCES `swarm/lib/README.md` for skill inventory and invocation contract; does NOT duplicate.

### §H.1 Accessor pipeline invocation contract

Per C1 Joint Design, the accessor pipeline (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) lives in `swarm/lib/`. Part 3 invokes through the declared interfaces. The skill specs live at `.claude/commands/<name>.md` (Phase A spec-driven; Phase B may move into `.sh`/`.py` for deterministic execution).

**Invocation patterns:**

```bash
# Query
/ask "<question>" [--anchor=<topic>] [--save (default) | --no-save] [--niche=methodology]

# Consolidate duplicates
/consolidate [--weekly]

# Rebuild graph
/build-graph [--with-communities]

# Lint health check
/lint [--check-para-tier] [--check-citations] [--check-stranger-test] [--check-crm-edges] [--check-methodology-admissibility] [--check-comparisons-emptiness] [--all]

# Ingest (Part 2 territory primarily; cross-listed here for completeness)
/ingest <signal-source> --anchor=<topic> [--para-tier=<value>] [--new-anchor]
```

The full skill inventory + per-role permission map lives in `swarm/lib/README.md` §3 + `swarm/lib/routing-table.yaml` (Part 4 P4.1). Part 3 §H REFERENCES; does NOT duplicate.

### §H.2 Wiki entity write interface

Pseudocode for the wiki entity write operation (executed at promotion after Part 6b ack):

```
function write_wiki_entity(draft, entity_type, ack_packet_id):
  # Validate admissibility per §E A1-A7
  if not has_human_acked_at(draft) or not has_para_tier(draft):
    return reject(reason="missing acked_at OR para_tier")
  if entity_type not in NINE_TYPES_PLUS_METHODOLOGY:
    return reject(reason="invalid entity_type")
  if entity_type == "concept" and not passes_stranger_test(draft):
    return reject(reason="fails Matuschak stranger test")
  if entity_type == "methodology" and not passes_l9_admissibility(draft):
    return reject(reason="missing DRR-validated-≥2-cycles OR rule_slug OR F5-rise")
  # Write entity file
  path = f"wiki/{entity_type_dir(entity_type)}/{slug}.md"
  write_with_frontmatter(path, draft, F=stamp_f_level(entity_type, draft))
  # Append index, log, edges
  append_index(path, anchor=draft.anchor)
  append_log(path)
  for edge in draft.edges:
    append_edge_jsonl(edge)
  # Commit via Part 1
  git_commit(message=f"[wiki] add {entity_type}/{slug} (anchor: {draft.anchor})")
  return success
```

**The K-class failure modes** map to the rejection branches (K2 missing-frontmatter, K3 stranger-test-fail, K4 methodology-admissibility-fail, K5 invalid-entity-type, etc.) per §K.

### §H.3 CRM edge validation function (P3.3 binding)

```
function validate_crm_edge(edge):
  if edge.type not in EIGHT_CRM_EDGE_TYPES:
    return flag(severity=defect, reason=f"invalid CRM edge type: {edge.type}")
  if not is_valid_a14_typed_edge(edge):
    return flag(severity=defect, reason="malformed A.14 typed-edge structure")
  if not slug_resolves(edge.from) or not slug_resolves(edge.to):
    return flag(severity=defect, reason=f"dangling slug ref: {edge.from} or {edge.to}")
  return accept

EIGHT_CRM_EDGE_TYPES = [
  "client_of",       # contact is/was a client of org
  "partner_of",      # contact/org is a partnership relationship
  "advisor_of",      # contact advises org or person
  "mentor_of",       # contact mentors person
  "hire_of",         # person was/is a hire
  "vendor_of",       # contact/org is vendor
  "competitor_of",   # contact/org is competitor
  "friend_of"        # personal-network edge
]
```

The 8 CRM edge types are enumerated per CLAUDE.md CRM System § (and aligned with `crm/_schema/edge-types.yaml` if such file exists; otherwise this enumeration is the canonical source until the CRM schema is materialised in Bundle 4 Part 10). [src:CLAUDE.md CRM System §; F4|G:Bundle 2 P3.3 binding|R-medium]

### §H.4 `/lint` signal extensions for Bundle 2

Bundle 1 Part 6a P6a.2 specified `/lint --check-citations` (deferred to Bundle 4 implementation per OQ-B1-2). Bundle 2 adds:

- `--check-para-tier` (P2.2 binding) — flags canonical entries lacking `para_tier:` frontmatter field
- `--check-crm-edges` (P3.3 binding) — flags malformed CRM edges per §H.3 validation function
- `--check-methodology-admissibility` (P3.2 binding) — flags `wiki/methodology/<slug>.md` lacking `validated_in_cycles:` ≥2 entries OR missing `rule_slug:`
- `--check-comparisons-emptiness` (P3.4 binding) — flags `wiki/comparisons/` emptiness when /ask usage confirmed in current session log
- `--check-edge-density` (L10 target) — flags entities with 0 outbound edges; aggregates avg edges/entity and reports vs ≥2.0 target
- `--check-stranger-test` (Wave C target; Bundle 4 implementation candidate) — flags `wiki/concepts/` entries with non-declarative-sentence titles, context-dependent body, or >500 words

The `/lint --all` invocation runs all signals + Bundle 1 #12 (commit-format check). Phase A: advisory output. Phase B: pre-commit hook blocking (per Bundle 1 K6 hook bypass discipline).

### §H.5 `/ask --save` default behaviour (P3.4 binding)

```
function ask_query(question, anchor=None, save=True, niche=None):
  candidates = retrieve_relevant_entities(question, anchor=anchor, niche=niche)
  synthesis = synthesize_with_citations(question, candidates)
  if save:
    slug = query_slug_from(question)
    path = f"wiki/comparisons/{slug}.md"
    write_with_frontmatter(path, synthesis, F=F3, entity_type="comparison",
                            sources=[c.path for c in candidates])
    git_commit(f"[wiki] file synthesis to comparisons/{slug}")
  return synthesis
```

The default is `save=True`. `--no-save` flips to ephemeral. `/lint --check-comparisons-emptiness` flags violations of the default behaviour (e.g., session log shows /ask invocations but `wiki/comparisons/` empty → likely indicates someone overrode the default; surfaces as health signal for owner attention).

---

## §I Data Schemas

### §I.1 Wiki entity frontmatter schema

The canonical entity frontmatter contract for `wiki/<entity-type>/<slug>.md`:

```yaml
---
pipeline: ingested|compiled|linted|ready
entity_type: concept | entity | source | topic | idea | experiment | claim | summary | foundation | methodology   # 10 types (Bundle 2 added methodology)
sources: [<path-or-URL>, ...]   # ≥1; raw provenance
anchor: <topic|project|question>   # D28 mandatory
para_tier: Project | Area | Resource | Archive   # cross-Part with P2.2
human_acked_at: <ISO 8601 | null>   # null pre-ack
ack_packet_id: <pkt-YYYYMMDD-slug | null>
F: F0..F9
ClaimScope:
  holds_within: [<scope-token>, ...]
R:
  refuted_if: <Popperian falsifier sentence>
  decay_after: <ISO 8601 | null>   # B.3.4 evidence decay (optional)
edges:
  - {from: <slug>, to: <slug>, type: <A.14 edge type>, confidence: <low|medium|high>}
# methodology-only fields (when entity_type == methodology):
rule_slug: <unique-slug-for-deduplication>
validated_in_cycles:
  - {cycle_id: <id>, result: validated|refuted, drr_path: <path>}
  - {cycle_id: <id>, result: validated|refuted, drr_path: <path>}
# comparison-only fields (when entity_type == comparison from /ask --save):
query: <verbatim>
---
```

### §I.2 Methodology library structure (P3.2 binding)

**Architecture decision:** chose `wiki/methodology/` as a NEW canonical entity-type. Rationale (per worklist §2 Part 3 Bullet 2 architecture decision):

- `wiki/foundations/` is structural Foundation parts (Part 1-10 architectures); extending it with methodology entries would conflate two different lifecycles (architecture is Lock-managed; methodology is cycle-validated).
- `wiki/methodology/` is namespace-clean: every entry is a reusable pattern derived from cycle DRRs.
- The `entity_type: methodology` frontmatter field makes the type queryable via `/ask --niche=methodology`.

**Admissibility predicate (L9 binding):** repeated for clarity:

```yaml
# A methodology candidate is admitted ONLY if all three:
- validated_in_cycles: list with ≥2 distinct entries each carrying result: validated
- rule_slug: non-null and either unique OR carries supersedes pointer for deduplication
- F: F4 initial → F5 post-promotion (per OQ-B1-1 anchor wording: F5 = "peer-validated methodology")
```

**Promotion sequence:**

1. Part 5 compound phase produces a methodology candidate at `wiki/methodology/<rule-slug>-DRAFT.md` with `pipeline: ingested`.
2. Candidate accumulates `validated_in_cycles` entries across cycles.
3. When predicate is satisfied, brigadier (or owner) emits AWAITING-APPROVAL `gate_class: draft_promotion` packet to Part 6b.
4. Owner acks; entity file moved to `wiki/methodology/<rule-slug>.md` with `pipeline: ready`, F-level promoted F4→F5, `human_acked_at:` populated.
5. `swarm/approvals/log.jsonl` (Part 6a §C) gets the entry.
6. `wiki/index.md` updated.

### §I.3 CRM edge validation schema (P3.3 / UND-5 binding)

CRM edges in `wiki/graph/edges.jsonl` MUST conform to:

```json
{
  "from": "<slug-of-from-entity>",
  "to": "<slug-of-to-entity>",
  "type": "client_of | partner_of | advisor_of | mentor_of | hire_of | vendor_of | competitor_of | friend_of",
  "confidence": "low | medium | high",
  "origin": "part-10",
  "edge_id": "<unique-id>",
  "created_at": "<ISO 8601>",
  "corrects": "<prior_edge_id | null>"
}
```

Validation by `/lint --check-crm-edges` per §H.3.

**Cross-reference to Part 10 (Bundle 4):** the CRM record content authoring rules (which slug naming, which confidence levels, which from/to entities) are Part 10 territory. Part 3 validates the SHAPE only; Part 10 owns the CONTENT.

### §I.4 Accessor pipeline ownership — REFERENCE to swarm/lib/README.md (P3.1 / C1 binding)

**Per C1 Joint Design (Bundle 2; Ruslan-acked 2026-04-27 Variant A):**

- Accessor pipeline scripts (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) live in `swarm/lib/` shared infrastructure.
- **Part 3 is named LEAD owner**; Part 4 is ADVISORY owner.
- Modification governance: AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 F8 LOCKED schema.
- Routing of which roles invoke which skills lives in `swarm/lib/routing-table.yaml` `accessor_skills_invocable:` field per role (Part 4 P4.1 deliverable).

**This section REFERENCES `swarm/lib/README.md` and `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` for the canonical answer.** Per DRY enforcement, this document does NOT duplicate the content; it CROSS-REFERENCES.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A canonical answer; src:swarm/lib/README.md:§3 skill inventory + §4 modification governance + §5 invocation contract; F4|G:Bundle 2 C1 Joint Design canonical|R-medium]

### §I.5 `wiki/comparisons/` schema (P3.4 binding)

Frontmatter:

```yaml
---
pipeline: ingested
entity_type: comparison
query: <verbatim question>
asked_at: <ISO 8601>
sources: [<entity-path>, ...]
F: F3
ClaimScope:
  holds_within: [query-context-<query-slug>]
R:
  refuted_if: <subsequent contradicting synthesis filed to comparisons/>
  decay_after: <ISO 8601 = asked_at + 90d>   # comparisons stale after 90d unless re-validated
para_tier: Resource   # comparisons are RESOURCE tier by default
anchor: <auto-derived from query keywords or 'general-query'>
---
```

`/lint --check-comparisons-emptiness` flags `wiki/comparisons/` empty when session log indicates /ask was invoked.

### §I.6 Health signal schema for Part 8 consumption (Bundle 4 stub)

Per dependency-graph §3.2 C2 (health signal schema mismatch — Wave C reconciliation needed):

```yaml
# /lint output schema (consumed by Part 8 Bundle 4)
wiki_health:
  entity_count: <int>
  edge_count: <int>
  edges_per_entity_avg: <float>
  edges_per_entity_target: 2.0   # L10 Wave C target
  orphan_anchors: [<list>]
  stale_claims: [<list with decay_after passed>]
  contradicts_supports_density: <float>   # target ≥0.05
  missing_frontmatter: [<list>]
  malformed_crm_edges: [<list>]
  comparisons_emptiness_flag: <bool>
  methodology_admissibility_violations: [<list>]
```

Part 8 Bundle 4 will consume this schema as its input contract for KB health signals.

---

## §J Operational Rituals

| Ritual | Cadence | Trigger | Responsible | Expected output | Notes |
|---|---|---|---|---|---|
| Ingest cross-reference (per entity write) | Per write event | New entity creation | `/ingest` script + `/build-graph` post-pass | ≥1 typed A.14 edge appended to edges.jsonl + ≥1 cross-ref to existing entity | L10 binding; Karpathy P1 |
| `/lint` weekly health audit | Weekly (Sunday morning) | Calendar cron + on-demand | `/lint --all` | Health report per §I.6 schema | Phase A advisory; Phase B blocking |
| `/consolidate --weekly` | Weekly | Calendar cron | `/consolidate` | Merged duplicates with `supersedes:` pointers | KM MVP cycle |
| `/build-graph` | On-demand (typically post-/consolidate or after batch ingestion) | Owner invocation | `/build-graph` | Rebuilt edges.jsonl + communities.jsonl | KM MVP cycle |
| Methodology promotion (per cycle) | At compound phase boundary | Cycle close | brigadier OR owner | AWAITING-APPROVAL packet to Part 6b for `gate_class: draft_promotion` | P3.2 binding |
| `/ask --save` default operation | Per query | Owner or any consumer query | `/ask` | Synthesis filed to `wiki/comparisons/<query-slug>.md` | P3.4 binding |
| Quarterly KB immune audit | Quarterly | Part 6a immune-function cadence | Part 6a (consumes Part 3 F-G-R compliance data) | Audit report at `swarm/audits/<quarter>/p3-kb-coverage.md` | Bundle 1 framework |

**SRE Workbook burn-rate algebra applied to KB edge-density SLO:**

| Burn rate | Part 3 observable | Required behaviour change |
|-----------|-------------------|---------------------------|
| **1×** | edges/entity ≥2.0; orphan-anchor count = 0; comparisons populated | No change |
| **6×** | edges/entity 1.5-2.0 OR orphan count 5-15 OR stale-claim count >10 | Cross-reference push: brigadier dispatches mgmt × integrator on backlog |
| **14.4×** | edges/entity <1.5 OR orphan count >15 OR L4 violation (canonical without ack) | Halt new promotions; owner ack required to resume; AWAITING-APPROVAL escalation packet |

**Evergreen note discipline:** this Part 3 architecture document IS evergreen per Karpathy / Matuschak. Updates land via new commits referencing prior commits, never via archive-then-replace.

**Compounding Engineering DRR ledger:** every cycle close produces a DRR (Decision-Result-Reflection) entry that may surface a methodology candidate. The candidate accumulates `validated_in_cycles` entries until L9 admissibility is satisfied, then promotes.

---

## §K Failure Modes

Apply Halt-Log-Alert L11 (≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9).

**K1 — Substrate cascade (Part 1 K8 fsck blocks Part 3 commits).** Detection: git commit fails. Policy: HALT promotions; LOG; ALERT. Recovery: resolve Part 1 K8.

**K2 — Missing frontmatter on promotion candidate.** Detection: write_wiki_entity admissibility check fails. Policy: REJECT with specific missing-field list; transparent error per CAI.

**K3 — Stranger-test fail on concept entity.** Detection: A4 admissibility check fails. Policy: REJECT; suggest title + body refactor.

**K4 — Methodology admissibility fail (L9 violation).** Detection: missing DRR-validated-≥2-cycles OR missing rule_slug OR F-level mismatch. Policy: REJECT; suggest accumulation cycle (wait for next cycle DRR).

**K5 — Malformed CRM edge (P3.3 / UND-5).** Detection: `/lint --check-crm-edges` flags. Policy: FLAG (severity=defect); cross-ref Part 10 (Bundle 4) for remediation; do NOT remove the malformed edge (Reversal Transactions — corrected by NEW edge with corrects: pointer).

**K6 — `/ask --save` default bypass (L8 violation).** Detection: `/lint --check-comparisons-emptiness` flags. Policy: FLAG; surface to owner; investigate whether `/ask` was used with `--no-save` (legitimate) or default behaviour broke.

**K7 — Edge density below target (L10 violation).** Detection: `/lint --check-edge-density` reports avg < 2.0 OR entity with 0 edges. Policy: FLAG; brigadier dispatches mgmt × integrator on cross-reference backlog.

**K8 — Orphan anchor (L2 violation).** Detection: entity in `wiki/` but no anchor entry in `wiki/index.md`. Policy: FLAG; auto-fix at next `/consolidate` if anchor recoverable from frontmatter; manual ack if anchor missing entirely.

**K9 — Stale claim (B.3.4 evidence decay).** Detection: `decay_after:` past current date. Policy: FLAG; brigadier dispatches philosophy × critic to re-validate or refute.

**K10 — Edges.jsonl in-place mutation attempt (L3 violation).** Detection: `git diff` shows mutation of existing line in edges.jsonl. Policy: BLOCK at pre-commit hook; require new edge with `corrects:` pointer per Reversal Transactions.

**K11 — RAG-style retrieval introduced.** Detection: `/ask` implementation diverges from compiled-cited-substrate pattern (e.g., introduces vector embeddings). Policy: REFUSE per L6 / D6 anti-RAG discipline; constitutional violation.

**K12 — Methodology rule_slug collision.** Detection: two methodology entries claim same rule_slug. Policy: HALT promotion of second; trigger `/consolidate` review; merge via Reversal Transactions.

**K13 — Comparisons file accumulation without `decay_after:` enforcement.** Detection: `wiki/comparisons/` count > N (RUSLAN-LAYER threshold) AND >50% have `decay_after:` past date. Policy: FLAG; surface for `/consolidate --weekly` to merge stale comparisons.

**K14 — CRM edge from Part 10 with dangling slug.** Detection: edge.from or edge.to slug does not resolve. Policy: FLAG with specific slug; cross-ref Part 10 for content authoring fix.

**K15 — Cross-fork CRM edge namespace conflict (Phase B).** Detection: CRM edges from forked instance reference slugs not in parent KB. Policy: defer per cross-fork-audit-deferred-phase-b.md (OQ-B1-8).

---

## §L Wave C Worklist Bullet Status

### Bullet P3.1 — C1 ACCESSOR PIPELINE OWNERSHIP RESOLUTION (BLOCKING — Joint Design with Part 4) ✅ ADDRESSED

**Acceptance predicate:** every accessor skill is path-addressable in `swarm/lib/`; routing-table.yaml (Part 4 P4.1) lists which roles invoke which accessor skills; Part 3 §F Anti-scope explicitly disowns the scripts.

**Status:** §F Anti-scope first part-specific bullet declares Part 3 does NOT own the accessor pipeline; Part 3 is named LEAD with Part 4 ADVISORY per C1 Joint Design Variant A. §I.4 REFERENCES `swarm/lib/README.md` and `C1-joint-design.md` (DRY enforced; no duplication). §H.1 declares invocation contract referencing `swarm/lib/README.md` §3 skill inventory.

**F-G-R:** F4 operational convention (canonical post-Ruslan-ack), `holds_within: [Foundation generic + Bundle 2 C1 canonical]`, R-medium until reuse evidence accumulates.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md; src:swarm/lib/README.md]

### Bullet P3.2 — Methodology library sub-layer materialisation ✅ ADDRESSED

**Acceptance predicate:** at least one methodology entry promoted from Bundle 3 stub (Part 5 work) lands cleanly in `wiki/methodology/<rule-slug>.md`; passes /lint; carries F5 + ClaimScope + refuted_if.

**Status:** §I.2 declares architecture decision `wiki/methodology/` as NEW canonical entity-type. §E L9 declares admissibility predicate (DRR-validated-≥2-cycles + rule_slug + F5 rise). §I.1 entity frontmatter schema includes methodology-specific fields (rule_slug, validated_in_cycles). §H.4 `/lint --check-methodology-admissibility` declared. §J ritual declares promotion sequence at compound phase boundary.

**F-G-R:** F4 architecture; methodology entries themselves F5 post-promotion. `holds_within: [Foundation generic methodology library]`, R-medium.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 3 Bullet 2; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§5 + KM P1]

### Bullet P3.3 — CRM edge validation schema (UND-5 binding) ✅ ADDRESSED

**Acceptance predicate:** synthetic 10-fixture (5 well-formed CRM edges, 5 malformed in distinct ways) — Part 3 `/lint` flags 5 malformed with specific reasons; cross-references Part 10 (Bundle 4) for content authoring rules.

**Status:** §D `derives-from Part 10` edge declared. §E L7 declares Part 3 `/lint` validates CRM-origin edges. §I.3 declares CRM edge validation schema with 8 edge types enumerated. §H.3 declares validation function pseudocode. §K K5 declares failure mode with cross-ref to Part 10. §H.4 `/lint --check-crm-edges` declared.

**F-G-R:** F4 operational convention, `holds_within: [Foundation generic CRM edge type taxonomy; specific edge instances RUSLAN-LAYER]`, R-medium.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.5 UND-5; src:CLAUDE.md CRM System §]

### Bullet P3.4 — `/ask --save` default enforcement ✅ ADDRESSED

**Acceptance predicate:** `/ask "X"` produces committed file at `wiki/comparisons/<query-slug>.md` with citations; `/ask --no-save "X"` ephemeral; `/lint` detects empty `comparisons/` after N>0 `/ask` invocations and flags as health defect.

**Status:** §E L8 declares `--save` is DEFAULT. §H.5 declares pseudocode with default save=True. §I.5 declares comparisons schema. §H.4 `/lint --check-comparisons-emptiness` declared. §K K6 declares failure mode for default-bypass.

**F-G-R:** F4 operational convention, `holds_within: [Foundation generic /ask discipline]`, R-high (testable).

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§E Deontics; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 3]

---

## §M Wisdom Application Findings

[Per Bundle 2 deep-prompt §5. Operational target ≥60% per Ruslan feedback after Bundle 1.]

| # | Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| 1 | KM-Karpathy P1 (compounding) | "Each new note triggers ≥1 cross-reference; without this wiki does not compound" | Implicit in Wave A; Wave C target 1.05→2.0 edges/entity | L10 mandatory cross-reference at every entity write; `/lint --check-edge-density` flag | YES | **OPERATIONAL** | Bundle 2 P3.2 binding; testable | §E L10 + §H.4 + §J ritual |
| 2 | KM-Karpathy P2 (atomicity / one idea per note) | "Concept files: one idea each; intelligence is in the link graph" | Wave A interface card declares stranger test in §E Admissibility | A4 admissibility predicate; §H validation pseudocode; `/lint --check-stranger-test` (Bundle 4 candidate) | YES | OPERATIONAL | Foundation generic atomicity | §E A4 + §H.4 |
| 3 | KM-Karpathy P3 (Matuschak stranger test) | "Declarative title; context-free body; ≤500 words" | Already in Wave A | Reinforced in §E A4; `/lint --check-stranger-test` for enforcement | YES | OPERATIONAL (reinforcing) | Concept-quality discipline at admissibility | §E A4 + §H.4 |
| 4 | KM-Karpathy P4 (Forte PARA) | "Organise by actionability — Project/Area/Resource/Archive" | Bundle 2 P2.2 in Part 2 | Cross-Part discipline at Part 3 admissibility (A6); rejection at Part 3 if Part 2 missed | YES | **OPERATIONAL** | Cross-Part PARA discipline closure | §E A6 |
| 5 | KM-Karpathy P5 (query-driven KB) | "/ask --save filing as default" | Bundle 2 P3.4 binding | L8 declared; §H.5 pseudocode; `/lint --check-comparisons-emptiness` | YES | **OPERATIONAL** | Bundle 2 P3.4 binding; testable | §E L8 + §H.5 + §I.5 |
| 6 | KM-Karpathy P6 (typed graph edges A.14) | "Edges typed; generic depends-on forbidden" | Already enforced via Part 1 §D | Reinforced in §D entire section; L3 append-only edges | YES | OPERATIONAL (reinforcing) | A.14 dogfood | §D entire + §E L3 |
| 7 | Levenchuk-SHSM-FPF IP-2 (bounded context) | "Each holon's context is bounded; cross-context bridge required" | Wave A applied | F-G-R `holds_within:` bounded scope per §G; Bridge via F.9 for cross-context | YES | OPERATIONAL (reinforcing) | F-G-R discipline at concept entries | §G + §I.1 |
| 8 | Levenchuk-SHSM-FPF A.14 typed mereology | "Typed edges canonical" | Already enforced | Reinforced via Part 1 §D 10-edge canonical reference | YES | OPERATIONAL (reinforcing) | A.14 dogfood | §D |
| 9 | Levenchuk-SHSM-FPF F-G-R B.3 | "Every promoted claim carries F-G-R triple" | Bundle 1 Part 6a F8 schema | DOGFOOD throughout §G + §I.1 | YES | OPERATIONAL (reinforcing) | Bundle 1 framework consumed | §G + §I.1 |
| 10 | Compounding-Engineering §5 (DRR → methodology promotion) | "Patterns validated across cycles promote to F5 codified" | Wave A interface card mentioned; not operationalised | L9 admissibility predicate (DRR validated ≥2 cycles + rule_slug + F5 rise); §I.2 promotion sequence | YES | **OPERATIONAL** | Bundle 2 P3.2 binding; load-bearing for compound asset | §E L9 + §I.2 |
| 11 | Clean-Code Ousterhout (deep modules) | "Each module is a deep module: simple interface, rich behaviour; atomic units" | Atomicity already enforced via Matuschak P3 | No new operational consequence; concept-file discipline already covers it | NO | OPERATIONAL deferred | Already-applied via P3 stranger test; no additional delta | n/a |
| 12 | Mereology-Typed-Edges (canonical) | "10-edge taxonomy from Part 1 §D as reference" | Already in Bundle 1 | DOGFOOD throughout §D | YES | OPERATIONAL (reinforcing) | Cross-Part dogfood | §D |
| 13 | SystemsThink-Cybernetics (Meadows L7 info-flows) | "/lint as L7 leverage point" | Implicit | Declared in §H.4 + §J ritual; Bundle 2 extension signals (P2.2/P3.2/P3.3/P3.4) | YES | **OPERATIONAL** | L7 info-flow leverage materialised | §H.4 + §J |
| 14 | SystemsThink-Cybernetics (Beer pipeline as feedback loop) | "Wiki health signals feed Part 8 monitoring" | Phase B / Bundle 4 stub | §I.6 health signal schema declared; Part 8 consumer | YES | OPERATIONAL (Phase B stub) | Schema declared as Foundation generic | §I.6 |
| 15 | Investor capital-allocation (KB as compound asset) | "Methodology library is highest-compound asset after KB itself" | Implicit | §0 frames methodology library as compound asset; capital-allocation lens | YES | PHILOSOPHICAL (justified — informs RUSLAN-LAYER attention budget for methodology promotion cadence) | Phase B/C concrete need: methodology promotion priority | §0 |
| 16 | Investor (Buffett owner-earnings analogy) | "Owner-earnings of KB = future cycles' velocity gain from methodology library" | Implicit | Single-sentence acknowledgement in §0 | NO | PHILOSOPHICAL | Pure framing; no operational delta | n/a |
| 17 | Stoic — Dichotomy of Control | "Distinguish in-control from not-in-control" | Bundle 1 applied at Part 1 | Not adopted at Part 3 — pure framing prose; defer to Wave D doc pass | NO | PHILOSOPHICAL | Defer per Bundle 2 operational bias | n/a |
| 18 | Anthropic-CAI (transparency on rejection) | "Rejection includes specific reason" | Already in Wave A (§E rejects with reason) | Reinforced in §K rejection branches; transparent error per CAI | YES | OPERATIONAL (reinforcing) | Transparency at rejection boundary | §K K2-K7 |
| 19 | Bai 2022 CAI (constitutional anchors) | "Hardcoded never-list as enum" | Bundle 1 Part 6b §I.3 enum | Cross-Part dogfood: Part 3 enforces never-list at promotion (e.g., Notion writes refused per L5 cross-ref) | YES | OPERATIONAL (cross-Part) | Bundle 1 framework consumed | §F + §K K11 |
| 20 | Young 2010 CQRS Reversal Transactions | "There is no Delete; corrections are NEW events with corrects: pointer" | Already enforced via L3 append-only | DOGFOOD via L3 + K10 + `/consolidate` merge with supersedes pointer | YES | OPERATIONAL (reinforcing) | Reversal Transactions discipline | §E L3 + §C + §K K10 |
| 21 | Karpathy LLM-Wiki gist (specific) | "Wiki proves itself by answering questions with citations; rejects RAG" | Already in Wave A | D6 anti-RAG discipline; D1 `/ask` returns inline citations | YES | OPERATIONAL (reinforcing) | Anti-RAG structural | §E D1 + D6 + §F |
| 22 | KM consultant §6 Part 3 item 4 (`/lint` health signals) | "Surface orphan, stale, contradicts/supports density to Part 8" | Wave A mentioned | §I.6 health signal schema; §H.4 `/lint --all` aggregates | YES | OPERATIONAL | Schema for Part 8 consumer declared | §I.6 + §H.4 |
| 23 | KM consultant §6 Part 3 item 1 (Karpathy proof of itself) | "Wiki accumulates validated entries — methodology library demonstrates this" | Wave A baseline | §0 frames methodology library as load-bearing reference layer at cycle 50 | YES | PHILOSOPHICAL (justified — methodology promotion priority is operational consequence) | Phase B/C cycle horizon | §0 |
| 24 | Lindy effect (long-lived) | "Wiki at cycle 11 baseline operational" | Operational since cycle 3b | No operational delta; pure framing | NO | PHILOSOPHICAL | Defer per Bundle 2 operational bias | n/a |

**Aggregate count:** 24 rows; 19 YES Adopted (operational: 16, philosophical: 3) + 5 NO (deferred / philosophical-without-justification / already-applied).

**Operational ratio of YES Adopted:** 16 / 19 = **84%** — exceeds Bundle 2 target of ≥60%.

**No fabricated YES entries** — every YES references a specific section edit verifiable by line trace.

---

## §N Provenance

**Sources consulted:** see frontmatter `sources:` and inline `[src:...]` citations throughout. Citation discipline: every cite within 200 chars of consequence sentence per Bundle 1 P6a.2 anti-cargo-cult discipline.

**Cross-Part cross-references:**

- Part 1 §D 10-edge A.14 canonical lookup (consumed throughout §D).
- Part 1 §I.2 commit-format-tokens.json (consumed at §B Part 1 outputs).
- Part 6a §I.1 F-G-R F8 schema (consumed at §G + §I.1).
- Part 6a §C citation discipline + approval log (consumed at §B + §J).
- Part 6b §I.4 awaiting-approval-packet F8 with gate_class enum [stop_gate, stage_gate, draft_promotion] (consumed at §A + §B for promotion gates).
- Part 6b §I.2 stage-gates (consumed at C1 modification governance via swarm/lib/README.md reference).
- Part 6b §E Law L9 Halt-Log-Alert + Corrigibility (consumed at §E L11 + L12).
- Part 2 §B (consumed at §A first input — STOP-gate-acked draft).
- C1 Joint Design + swarm/lib/README.md (consumed at §F + §I.4 + §H.1).

**Commits on `claude/jolly-margulis-915d34`:** appended at Phase F finalize.

---

## §X Foundation vs RUSLAN-LAYER Fork-Separation

### Foundation generic (any Phase B partner imports)

- **Wiki entity-type taxonomy** — 10 types (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations/methodology) per §I.1.
- **A.14 typed-edge schema** — canonical 10-edge table from Part 1 §D + 8 CRM edge types (P3.3 / UND-5 binding).
- **F-G-R frontmatter contract** — per Bundle 1 Part 6a §I.1 F8 schema; consumed throughout §G + §I.1.
- **Methodology library admissibility predicate (L9 / P3.2 binding)** — DRR-validated-≥2-cycles + rule_slug + F5 rise.
- **`/ask --save` default behaviour (P3.4 binding)** — semantic contract, not the implementation.
- **`/lint` health signal taxonomy** — 6 Bundle 2 signals (para-tier, citations, stranger-test, crm-edges, methodology-admissibility, comparisons-emptiness) + 11 Bundle 1 signals + 1 commit-format = 18 signals total.
- **`wiki/comparisons/` schema (P3.4)** — entity-type and frontmatter contract.
- **C1 Joint Design canonical answer pattern** — `swarm/lib/` shared infra with named lead+advisory per Variant A.

### RUSLAN-LAYER (specific to Ruslan's Jetix instance)

- **552 wiki entities Ruslan-authored** (current baseline per AUDIT §8) — per-entity content is Ruslan's IP.
- **6 niche slices** in `wiki/niches/<slice>` (personal, business, sales, life, tech, meta) — Ruslan's specific niche labels and contents.
- **Specific methodology library entries Ruslan-authored** post-Bundle-2 — the `wiki/methodology/<rule-slug>.md` content per his cycle DRRs.
- **D28 anchor registry contents** — specific projects/topics Ruslan has declared in `wiki/index.md` and `projects/`.
- **CRM record content** — Part 10 territory (Bundle 4); Part 3 stores edges, not content.
- **`wiki/comparisons/` accumulation** — Ruslan's specific queries and synthesised comparisons.
- **`/lint` threshold values** — specific edge-density target if Ruslan deviates from 2.0; specific comparisons-count threshold per K13.

### Phase B fork sees

A Phase B partner forking Foundation:

1. **Imports** Foundation generic taxonomy + A.14 schema + admissibility predicates + accessor pipeline (per `swarm/lib/`).
2. **Imports** the 18 `/lint` signals as health monitoring contract.
3. **Replaces** RUSLAN-LAYER content (entities, niche slices, methodology entries, D28 anchors, comparisons).
4. **Extends** the methodology library per their own cycle DRRs.
5. **Cross-fork reconciliation** per Bundle 1 P1.1 cross-fork-provenance.json (deferred to Phase B per OQ-B1-8).

The C1 Joint Design canonical answer (Variant A) is structural pattern; the partner re-elects their named lead/advisory roles per their fork's `executor-binding.yaml`.

---

*End of Part 3 — Knowledge Base & Methodology Library architecture. Status: draft-pre-ruslan-ack. F4 → F5 on Ruslan ack of Bundle 2 packet. Cross-references: C1-joint-design.md + swarm/lib/README.md (Bundle 2); Bundle 1 LOCKED Parts 1/6a/6b architectures; Part 2 architecture (Bundle 2 sibling); Wave A interface card (superseded for Wave C onward but preserved historically).*
