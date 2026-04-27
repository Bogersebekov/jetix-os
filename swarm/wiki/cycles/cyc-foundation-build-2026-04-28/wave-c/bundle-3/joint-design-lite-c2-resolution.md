---
title: "Joint Design lite — C2 Health Signal Schema Canonicalisation Resolution"
date: 2026-04-28
type: joint-design-lite-resolution
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
parent_oq: C2 (Bundle 1 carry-over contradiction; resolved Bundle 3)
participants: [engineering-expert (integrator-mode), systems-expert (critic-mode VSM S3 + Ashby variety), philosophy-expert (boundary-clarity)]
parent_part_8_section: swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md §I.1 + §I.3
F: F4
ClaimScope: "Holds for Bundle 3 C2 resolution choice (Variant B chosen). Variant A retroactive align deferred to Wave D housekeeping cycle."
R:
  refuted_if: "Wave D housekeeping cycle finds Variant B mapping table is structurally inadequate AND Variant A retroactive align cannot be executed without F-fall on Bundle 1+2 architectures"
  accepted_if: "Bundle 3 ack accepts Variant B as Bundle 3 C2 resolution; Wave D housekeeping cycle has option to apply Variant A as supplement"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md §3.2 C2 health signal schema
  - swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md §I.1 + §I.3
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md §I.5 health signal stub
  - swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md §I.6 health signal stub
  - swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md §I.6 health signal stub
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md §I.4 health signal stub
---

# Joint Design lite — C2 Health Signal Schema Canonicalisation Resolution

## §1 Question

**C2 (Bundle 1 carry-over contradiction):** Bundle 1 + Bundle 2 emitters
declared health signal stubs (Part 1 §I.5; Part 3 §I.6; Part 4 §I.4 — currently
heterogeneous). Bundle 3 Part 8 §I.1 owns the canonical health-signal schema.

**Choice:**

- **Variant A — retroactive align Bundle 1 + 2 emitter shapes to Part 8
  canonical schema** (preferred — DRY).

- **Variant B — Part 8 §I.1 explicitly accepts current heterogeneous shapes
  with a mapping table in §I.3** (fallback if retroactive alignment exceeds
  1h budget OR risks F-fall on F5 LOCKED architectures).

Pick one with rationale per Bundle 3 deep prompt §4.3.

## §2 Deliberation

**Engineering-expert (integrator-mode):**

DRY discipline favours Variant A. Bundle 1+2 emitter §I.5/§I.6/§I.4 stubs
are heterogeneous — different field names, different data types, different
units. A canonical schema in Part 8 §I.1 means the system has TWO authorities
(canonical + per-emitter heterogeneous shapes). DRY violation.

HOWEVER: Bundle 1+2 architectures are F5 LOCKED per RUSLAN-ACK Bundle 1 + 2.
Modifying the §I.5/§I.6/§I.4 sections post-LOCK is a MODIFICATION of F5
artefacts — risks F-fall via re-litigation of acked schemas. The retroactive
supplement pattern (OQ-B2-A) is permissible for SPECIFIC stub corrections
agreed in advance (gate_class enum align; commit-format-tokens; K18 upcasting
— all ≤30 min single commit). Retroactive align of emitter shapes across
Parts 1+2+3+4 is a much larger operation (~4 sections × ~10 fields each =
~40 field projections) and risks F-fall by accident.

**Systems-expert (critic-mode VSM S3 + Ashby variety):**

Beer VSM S3 audit context spans entire Foundation. Part 8 IS the audit
function. The audit function MUST observe heterogeneous emitter outputs
(Ashby requisite variety: monitor must match emitter variety). A mapping
table IS the requisite variety match — adapter pattern from Gang of Four
1994 (clean-code §4 Patterns). The mapping table is NOT a DRY violation — it
is the canonical authority's adapter to Bundle 1+2 emitter variety. The
canonical schema (§I.1) is the SINGLE authority; the mapping table (§I.3) is
the implementation of "how emitter shape X projects onto canonical shape."

Variant B is structurally analogous to a database adapter: the database
schema (§I.1) is canonical; the application's per-table queries (Bundle 1+2
emitters) are different shapes; the adapter (§I.3) projects between them.
This is DRY-respectful at the schema layer.

**Philosophy-expert (boundary-clarity):**

The boundary question: where does Part 8 own canonical schema vs where do
Bundle 1+2 emitters own their stub shapes? Variant A ERASES the boundary —
Part 8's schema becomes the sole authority; Bundle 1+2 emitters lose their
stub-level independence. Variant B PRESERVES the boundary — Bundle 1+2
emitters retain their F5 LOCKED stubs; Part 8 owns the canonical adapter.

For Phase A (single owner; ≤10 agents; not yet at fork-and-merge complexity),
Variant B is the cleaner boundary: Bundle 1+2 architectures are CANONICAL in
their own right; Part 8 is the audit context that adapts to them.

**For Phase B+ (multi-fork, distributed observability), Variant A retroactive
align would be more efficient** because the adapter table layer becomes
redundant when emitters all output canonical-direct. But Phase B is Phase B;
Bundle 3 is Phase A; the right scope is Variant B with Variant A as Wave D
housekeeping option.

## §3 Resolution: Variant B chosen for Bundle 3

**Decision:** Variant B (mapping table in §I.3 of Part 8 architecture).

**Rationale:**

1. **F5 LOCKED preservation.** Bundle 1+2 architectures are RUSLAN-ACK
   constitutional baselines per RUSLAN-ACK Bundle 1 + 2 §3 (F-promotions
   table). Modifying their §I.5/§I.6/§I.4 sections post-LOCK risks F-fall
   via re-litigation. Variant B respects this LOCK status.

2. **Adapter pattern is DRY-respectful.** §I.3 mapping table is the canonical
   authority's adapter to heterogeneous emitter shapes. Single authority
   (§I.1); single adapter location (§I.3); no schema duplication.

3. **Phase A scope discipline.** Retroactive align of ~40 field projections
   across Parts 1+2+3+4 exceeds the 1h budget specified in Bundle 3 deep
   prompt §4.3 fallback condition. Variant B fits within the Joint Design
   lite Phase 1h budget.

4. **Variant A remains AVAILABLE for Wave D housekeeping.** The retroactive
   align operation is not foreclosed — it is DEFERRED to a Wave D
   coordination cycle where it can be executed as a coordinated supplement
   (similar to OQ-B2-A retroactive supplement pattern from Bundle 1 →
   Bundle 3 cycle).

5. **Phase B fork-portability is preserved.** A Phase B partner forking
   Jetix can adopt: (a) the canonical health-signal schema (Part 8 §I.1) as
   the universal authority; (b) the mapping table pattern (Part 8 §I.3) as
   a generic adapter mechanism; (c) optionally apply Variant A retroactive
   align if their fork's emitter shapes already conform to canonical.

## §4 Open Question — Variant A as Wave D housekeeping option

OQ-B3-P8-1 (registered in Part 8 §Y): Variant A retroactive align deferred
to Wave D housekeeping cycle. Confirm Wave D scope accepts this housekeeping
commit.

This OQ does NOT block Bundle 3 ack. Variant B is functional; Variant A is
optional optimization for Wave D.

## §5 Materialisation in Part 8 architecture

- **§I.1 canonical health-signal schema** — declared inline (physical file
  generation Phase B per OQ-B1-2 + OQ-B1-4 pattern).
- **§I.3 mapping table** — populated with ≥30 entries covering Parts 1+2+3+4+5+6a+6b emitter shapes (per Bundle 3 spec P8.2 acceptance predicate).
  Aggregation/disaggregation rules declared for object-valued emitters.
- **§K11 failure mode** — declared: "Variant A retroactive align (deferred
  to Wave D housekeeping) diverges from §I.3 mapping table. Detection: Wave
  D housekeeping cycle applies Variant A retroactive align; §I.3 mapping
  becomes redundant. Policy: at Wave D, retire §I.3 mapping table in favor
  of canonical-direct emitters; preserve §I.3 in archived form for audit
  trail (Reversal Transactions). [F3|G:Wave D scope|R-low]"

## §6 Decision provenance

This decision was made within the Joint Design lite Phase per Bundle 3 deep
prompt §4.3. Direct-write mode (subagent stall fallback per §10.12 of deep
prompt). Deliberation captured above; resolution materialised in Part 8
architecture §I.1 + §I.3 + §K11.

The companion artefact is committed at:
- This file: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/joint-design-lite-c2-resolution.md`

Cross-ref companion:
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` (Joint Design lite UND-3 deliverable)
