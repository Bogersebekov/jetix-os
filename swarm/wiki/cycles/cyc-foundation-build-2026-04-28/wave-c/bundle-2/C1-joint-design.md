---
title: "C1 Joint Design — Accessor Pipeline Ownership Resolution (Parts 3 + 4)"
date: 2026-04-28
type: joint-design-decision
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
parts_jointly_designed: [3, 4]
status: canonical-pre-ruslan-ack
ruslan_acked_variant: "Variant A — shared infrastructure swarm/lib/ with named owner (acked 2026-04-27 in walkthrough preceding Bundle 2 deep-prompt brief)"
F: F4
ClaimScope: "Resolves dependency-graph C1 BLOCKING contradiction between Part 3 §F Anti-scope (disowns accessor pipeline to Part 4 or shared infra) and Part 4 §B Outputs (does not accept ownership). Holds within Foundation Phase A scope. Phase B forks may re-elect named owner per local needs but the shared-infra location pattern persists."
R:
  refuted_if: "An accessor skill (/ingest, /ask, /consolidate, /build-graph, /lint) develops a lifecycle that cannot be coherently located in swarm/lib/; OR Part 3 begins owning the script lifecycles (writes the .sh/.py logic in wiki/) instead of the content; OR Part 4 begins owning the script lifecycles (writes them under coordination protocol files) instead of the routing"
  accepted_if: "(a) Part 3 §I REFERENCES this document and swarm/lib/README.md without duplicating their content; (b) Part 4 §I REFERENCES this document and swarm/lib/README.md without duplicating; (c) Part 4 swarm/lib/routing-table.yaml lists which roles can invoke which accessor skills via accessor_skills_invocable field; (d) every accessor skill is path-addressable inside swarm/lib/"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§3.1 C1 BLOCKING)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md (§F Anti-scope first bullet — the disowning statement)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md (§F Anti-scope; §H Note for Wave C)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (P3.1 C1 + P4.2 C1)
  - swarm/lib/shared-protocols.md (current shared-infra layer being extended)
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§4.6 boundary enforcement; §6.1 hard rules)
  - design/JETIX-FPF.md (§1.4 A.1 Agency Rule — U.System vs U.Episteme classification; §5.1 IP-1 Role≠Executor; §3.5 A.14 typed edges)
related_artefacts:
  - swarm/lib/README.md (the canonical infra-layer documentation produced as companion to this design decision)
  - swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md (§I REFERENCES this)
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (§I REFERENCES this)
---

# C1 Joint Design — Accessor Pipeline Ownership Resolution

> **Joint design between Parts 3 + 4.** Single coherent answer to the BLOCKING C1 contradiction
> from dependency-graph §3.1: "where do `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`
> live? Who owns them? Who can modify them? How does Part 3 invoke them? How does Part 4 invoke
> them?"

## §1 The contradiction (verbatim from dependency-graph §3.1)

| Side | Position |
|------|----------|
| Part 3 §F Anti-scope | "This part does NOT own the accessor pipeline (U.System) — `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` are U.System accessor services owned by Part 4 (coordination protocol infrastructure) or shared infrastructure." |
| Part 4 §B Outputs | Does not list "wiki accessor pipeline skills" as an output. Does not accept ownership. |
| Net result | Skills currently in limbo. Architectural orphans. BLOCKING for Wave C task assignment. |

This is not a runtime defect — the skills work today (cycle 11 voice pipeline operational; `/lint`
ran cycle 9 and produced `wiki/_lint-report-2026-04-16.md`). It is a structural ownership gap that
would propagate Wave C work as orphan tasks: no Part has obligation to maintain them, and a Phase
B fork has no clear instruction on whether to fork these scripts or treat them as upstream.

## §2 The three candidate variants (Wave A surfaced)

**Variant A — Shared infrastructure `swarm/lib/` with named owner.** Skills live in `swarm/lib/`.
Neither Part 3 nor Part 4 writes the script logic; both invoke through declared interfaces. A
named owner role takes maintenance accountability. Modifications gated by AWAITING-APPROVAL
stage_gate per Part 6b §I.4.

**Variant B — Part 4 absorbs ownership.** Part 4 §B Outputs adds "wiki accessor pipeline skills
:: invocable by any consumer :: on-demand"; Part 4 §D adds `creates Part 3` edge. Part 4 owns the
script lifecycles. Drawback: Part 4 becomes both a coordination protocol AND a tooling provider —
mixed responsibility violates IP-2 bounded context.

**Variant C — Part 3 absorbs ownership.** Part 3 §F changes from "does NOT own" to "DOES own".
Part 3 carries both content (U.Episteme) and pipeline scripts (U.System). Drawback: violates
A-1-critic FLAG-MINOR resolution (which already identified this as boundary leak); mixes U.System
and U.Episteme inside one Part.

## §3 Ruslan-acked answer — Variant A

**Acked in 2026-04-27 walkthrough preceding the Bundle 2 deep-prompt brief.** Variant A is
canonical for Foundation Phase A.

### §3.1 Canonical answer (one sentence)

The five accessor skills (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) and any
future accessor pattern at the same level (e.g. `/search-kb`) live as path-addressable scripts
under `swarm/lib/`; **Part 3 (Knowledge Base) is the named LEAD owner** with **Part 4 (Role
Taxonomy & Coordination Protocol) as ADVISORY owner**; modifications require AWAITING-APPROVAL
`gate_class: stage_gate` per Part 6b §I.4 frozen schema; routing of which roles may invoke which
skills lives in Part 4 `swarm/lib/routing-table.yaml` `accessor_skills_invocable:` field.

### §3.2 Why Part 3 lead

Part 3 is the **content substrate** these skills operate on. The KB (`wiki/`) is Part 3 territory
(U.Episteme). Every accessor skill — without exception — reads or writes Part 3-managed content:

| Skill | Touches Part 3 content? |
|-------|------------------------|
| `/ingest` | YES — writes new entity to `wiki/<entity-type>/<slug>.md` after STOP gate ack |
| `/ask` | YES — reads `wiki/index.md` + `wiki/concepts/` + `wiki/sources/`; writes `wiki/comparisons/<query-slug>.md` on `--save` |
| `/consolidate` | YES — merges duplicate entities in `wiki/concepts/` and `wiki/sources/` |
| `/build-graph` | YES — rebuilds `wiki/graph/edges.jsonl` typed-edge graph + `wiki/graph/communities.jsonl` |
| `/lint` | YES — validates `wiki/` frontmatter, edges, citations, PARA-tier tags, methodology promotion predicates |

Part 4's accessor obligations are **routing**, not content access — Part 4 needs to declare which
roles invoke which skill (per role's `accessor_skills_invocable:` field in routing-table.yaml),
but the substrate the skill operates on is Part 3's. Per IP-2 bounded context: the owner is the
Part most affected by malformation. Malformed `/ingest` corrupts `wiki/`; Part 3 felt-pain ratio
exceeds Part 4's. Therefore Part 3 leads.

### §3.3 Why Part 4 advisory (not silent)

Part 4 holds advisory ownership for two reasons:

1. **Routing variance:** when a new role enters the system (e.g. a Wave D Part 8 health monitor
   role), Part 4's routing-table.yaml must add an `accessor_skills_invocable:` entry. Part 4
   surfaces the variance to Part 3 advisory; Part 3 acks (or rejects) the addition. Part 4 is the
   noticer.

2. **Cross-cutting hub-and-spoke:** the brigadier (Part 4 territory) is the dispatcher. If a cell
   needs an accessor skill outside its declared `accessor_skills_invocable:` set, the brigadier
   surfaces the gap. Part 4 advisory means: brigadier escalates to Part 3 lead, Part 3 decides.

The advisory role prevents Part 3 from drifting into an isolated maintainer that never hears the
call sites. Part 4 is the call-site witness.

### §3.4 Modification governance

Any change to `swarm/lib/<skill>.{sh,py}` requires:

1. **Proposal:** any role with write access to `swarm/lib/` may propose a change. Proposal is a
   draft commit on a feature branch + AWAITING-APPROVAL packet with `gate_class: stage_gate` per
   Part 6b §I.4 (the schema is FROZEN at F8 per RUSLAN-ACK Bundle 1 Decision #5).
2. **Lead review:** Part 3 lead owner (Ruslan in Phase A; Phase B successor named in
   `executor-binding.yaml`) reviews. Pass = packet acked.
3. **Advisory pass:** Part 4 advisory owner reviews routing implications. If routing-table.yaml
   needs a corresponding update, packet bundles both files.
4. **Promotion:** ack triggers merge to `claude/jolly-margulis-915d34` (or Phase B equivalent).
   `swarm/approvals/log.jsonl` (Part 6a §C) gets the entry.
5. **Audit trail:** every modification carries a `[swarm-lib]` commit prefix per Part 1
   commit-format-tokens.json schema (Bundle 1 §I.2). The token `[swarm-lib]` is added to the
   accepted area enum.

### §3.5 Failure modes — what would refute this answer

The answer is REFUTED (re-litigate via new AWAITING-APPROVAL constitutional packet) if any of:

- An accessor skill develops semantics that **cannot** be coherently located in `swarm/lib/` —
  e.g., a future skill that bridges to external API and would need different security domain.
  In that case: split the skill into a `swarm/lib/<accessor>` shim that calls a separately-located
  external integration script.
- Part 3 begins **writing** the script logic (instead of consuming the script's outputs into
  `wiki/`). The lead-owner role should be governance + interface contract, not implementation.
- Part 4 begins **writing** the script logic (instead of routing dispatchers to invoke the
  scripts). Advisory should be routing surface management, not implementation.
- Phase B fork demonstrates a structural reason to relocate the skills (e.g., partner needs a
  different content substrate). In that case: partner forks `swarm/lib/` per Variant A's
  shared-infra-with-fork pattern; shared structural pattern persists, named owner role re-elected.

## §4 Skill inventory (current state)

| Skill | Path (current) | Status | Brief description |
|-------|----------------|--------|-------------------|
| `/ingest` | `.claude/commands/ingest.md` (skill spec) → invokes per CLAUDE.md voice-notes pipeline | Operational (cycle 11 baseline) | Reads raw signal (URL/PDF/voice/clipboard); produces draft candidate at `inbox/<slug>-DRAFT.md` or `raw/transcripts/<slug>.md` with frontmatter. Bundle 2 P2.2 EXTENDS to enforce `para_tier:` mandatory. |
| `/ask` | `.claude/commands/ask.md` (skill spec) | Operational + Bundle 2 P3.4 EXTENSION | Receives `<question>`; reads `wiki/index.md` + relevant entity files; produces synthesis with inline `[src:...]` citations. **Bundle 2 P3.4: `--save` is DEFAULT** — writes synthesis to `wiki/comparisons/<query-slug>.md`. `--no-save` flag for ephemeral. |
| `/consolidate` | `.claude/commands/consolidate.md` | Operational + `--weekly` flag (KM MVP cycle) | Detects + merges duplicate entities (e.g. two `wiki/concepts/<slug>.md` that should be one). `--weekly` runs auto-merge on items added in last 7 days. |
| `/build-graph` | `.claude/commands/build-graph.md` | Operational + community detection (KM MVP cycle) | Rebuilds `wiki/graph/edges.jsonl` typed-edge graph from per-entity frontmatter. Optionally writes `wiki/graph/communities.jsonl` (Louvain-equivalent community labels). |
| `/lint` | `.claude/commands/lint.md` | Operational + 11 KB health checks + Bundle 1 P1.2 commit-format check (#12) + Bundle 1 P6a.2 citation scanner (specified, Bundle 4 implementation per OQ-B1-2) | Validates `wiki/` frontmatter completeness, edges.jsonl integrity, orphan entities, stale claims, contradicts/supports edge density, anchor compliance. **Bundle 2 extensions: P2.2 PARA-tier check; P3.3 CRM edge validation; P3.4 comparisons emptiness signal.** |

## §5 Invocation contract — which roles invoke which skills

Authoritative source of truth: `swarm/lib/routing-table.yaml` (Part 4 P4.1 deliverable).

This document declares the principle; routing-table.yaml declares the per-role permissions.
Cross-reference rule: every accessor skill MUST appear in at least one role's
`accessor_skills_invocable:` array; every role with `accessor_skills_invocable: [...]` non-empty
MUST list only skills declared in §4 above (no invented skills).

Invocation discipline:

- **Brigadier** (orchestrator): invokes any accessor skill on behalf of a cell IF the cell's
  routing-table entry permits.
- **Owner (Ruslan)**: invokes any accessor skill directly via slash-command (e.g. `/ask "what
  does X mean"` in REPL).
- **Cells (5 ROY experts in critic/optimizer/integrator/scalability modes)**: per role's
  `accessor_skills_invocable:`. Default permit set: `/ask` (read-only synthesis). `/lint` and
  `/build-graph` are typically brigadier-only.
- **Legacy 13 agents** (manager, sales-lead, etc.): invokers per `executor-binding.yaml` entries
  (RUSLAN-LAYER); typical pattern is `/ask` + `/ingest` + their own niche-specific subset.

## §6 Modification governance summary (one-line operational rule)

> Any change to `swarm/lib/<skill>.{sh,py,md}` produces an AWAITING-APPROVAL packet with
> `gate_class: stage_gate`, ack required from Part 3 lead owner before merge; if the change
> touches routing semantics (which roles invoke), Part 4 advisory ack also required.

## §7 Cross-references (DRY enforcement)

Both Part 3 §I and Part 4 §I REFERENCE this document. Neither duplicates content. Specifically:

- **Part 3 §I**: declares accessor pipeline ownership via reference: "Per `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` and `swarm/lib/README.md`: Part 3 is named LEAD owner of the accessor pipeline; modification governance per §3.4 of C1-joint-design.md."

- **Part 4 §I**: declares routing inclusion via reference: "Per `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md`: Part 4 holds ADVISORY ownership; routing variance surfaces via `accessor_skills_invocable:` field per role in `swarm/lib/routing-table.yaml`."

Brigadier critic gate verifies both §I sections REFERENCE; if either §I duplicates the canonical
content, critic-gate auto-rejects with citation `[src:C1-joint-design.md:§7 DRY enforcement]`.

## §8 Provenance chain

Decision lineage:

1. **2026-04-27 (Wave A complete):** dependency-graph.md surfaces C1 as BLOCKING (§3.1).
2. **2026-04-27 evening:** wave-c-worklist.md scopes P3.1 + P4.2 as joint-design pair (BLOCKING for Wave C task assignment).
3. **2026-04-27 walkthrough:** Ruslan reviews variants A/B/C; acks Variant A with named-owner addition (Part 3 lead with Part 4 advisory).
4. **2026-04-28 deep-prompt brief:** Wave C Bundle 2 prompt references the ack (deep-prompt §1.4 C1).
5. **2026-04-28 (this document):** brigadier materializes the canonical answer + companion `swarm/lib/README.md`.

[src:dependency-graph.md:§3.1 C1 BLOCKING; src:wave-c-worklist.md:§2 Part 3 Bullet 1 + §2 Part 4 Bullet 2; src:RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md (Bundle 1 ack carries forward unblocking constitutional context); src:prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md:§1.4 UND-1+UND-4+UND-5+C1; F4|G:Bundle 2 Joint Design canonical answer Foundation Phase A scope|R-medium]

## §9 What Phase B sees

A Phase B partner forking the Foundation imports:

- This document as the **structural pattern** (shared infra `swarm/lib/` with named lead+advisory).
- `swarm/lib/README.md` as the **operational reference** (skill inventory + invocation contract).
- `swarm/lib/routing-table.yaml` as the **routing schema** (the partner replaces specific roles per their fork).

The partner re-elects their named owner role per local needs (e.g., partner's Part 3 successor is
the new lead). The Variant A pattern persists; the specific names rotate per fork. This is the
F.9 Bridge contract for accessor pipeline ownership across forks.

---

*End of C1 Joint Design. Cross-reference: see `swarm/lib/README.md` for operational specifics.*
