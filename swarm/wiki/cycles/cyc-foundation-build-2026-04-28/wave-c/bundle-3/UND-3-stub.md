---
title: "UND-3 Stub — Part 5 ↔ Part 7 Cross-Bundle Interface (Bundle 4 finalises Part 7 emission)"
date: 2026-04-28
type: cross-bundle-interface-stub
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
parent_part_5_section: swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md §A.5 + §I.4
parent_oq: UND-3
finalised_in: Bundle 4 (Part 7 architecture) — CONFORMANCE VERIFIED 2026-04-28 via M5 inter-Part lite coherence check
status: finalised-Bundle-4-conformance-verified
F: F4
finalisation_record:
  bundle_4_commit_part_7: "see git log --grep='Bundle 4 — Part 7'"
  schema_option_picked: "Option A — task-return-packet superset (allOf reference); physical file shared/schemas/project-retrospective-packet.json"
  cadence_option_picked: "Option α PRIMARY (per project closure event); Option β SECONDARY (per under-review draft increment)"
  m5_coherence_check_result: "PASS — Part 7 §B project-retrospective-packet schema fields are SUPERSET of Part 5 §A.5 expected fields (project_id, state_transition, appetite_actual_vs_planned, lessons_learned[], dr_r_candidates[]); methodology_promotion_candidates[] added"
  cross_ref_part_5: "swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md §A.5 admissibility A-5"
  cross_ref_part_7: "swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md §B.1 + §I.2"
ClaimScope: "Holds for Part 5 input expectations from Part 7 retrospective output. Bundle 4 Part 7 picks ONE schema-reference path AND ONE cadence path; Bundle 3 declares OPTIONS only."
R:
  refuted_if: "Bundle 4 Part 7 emission contract diverges materially from these expectations and Part 5 cannot consume Part 7 output without re-architecture"
  accepted_if: "Bundle 4 Part 7 emission contract conforms to one of the declared options + cadence; Part 5 admits Part 7 inputs per Part 5 §A.5 admissibility A-5"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md §4.3 UND-3 P7→P5 cadence
  - swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md §A.5 + §I.4
---

# UND-3 Stub — Part 5 ↔ Part 7 Cross-Bundle Interface

## §1 Purpose

UND-3 is the cross-bundle interface between Part 5 (Compound Learning &
Methodology Capture — Bundle 3) and Part 7 (Project Lifecycle Substrate —
Bundle 4). Part 5 expects retrospective input from Part 7 to feed compound
phase DRR extraction at project closure events.

Bundle 3 specifies the INPUT EXPECTATIONS (this stub). Bundle 4 Part 7
finalises the EMISSION contract (which schema, which cadence). Sequential
design without this stub would produce incoherent Part 5 + Part 7 interfaces.

This stub document is the Joint Design lite Phase output (per Bundle 3 deep
prompt §4.3). It lives as a standalone D25 Company-as-Code committed canonical
artefact so it can be referenced from both Part 5 §A.5/§I.4 (Bundle 3) and
future Part 7 §B Outputs (Bundle 4).

## §2 Part 5 Input Expectations from Part 7

Part 7 retrospective output, when consumed by Part 5 at compound phase,
SHOULD provide:

| Field | Type | Purpose |
|---|---|---|
| `project_id` | string | Identifies which project closed (e.g. `quick-money` per CLAUDE.md projects table) |
| `state_transition` | enum | Project state transition that triggered retrospective: `discovery → execution`, `execution → closed-won`, `execution → closed-lost`, `execution → paused`, etc. — matches Part 7 lifecycle states |
| `appetite_actual_vs_planned` | object | Cagan/Shape Up appetite ratio: `{planned_days: <int>, actual_days: <int>, ratio: <float>}`. Ratio >1.0 indicates appetite overrun (signal for next cycle planning) |
| `lessons_learned` | array of structured prose entries | Per-cycle retrospective prose; each entry has `cycle_id`, `prose`, `f_g_r`, `category` (e.g. "estimation", "scope-creep", "tooling-gap") |
| `drr_candidates` | array of DRR-shape entries | Part 7 pre-extracted DRR candidates (Decision/Reasoning/Result/Review structure); Part 5 admits per Part 5 §A.5 admissibility A-5 |
| `metrics_snapshot` | object | Per-project SLI snapshot at closure: `{cycles_completed, methodology_promotions, drr_entries_committed, dissolve_test_evidence_count}` |

## §3 Schema-Reference Options (Bundle 4 Part 7 picks ONE)

**Option A — `task-return-packet.json` superset.** Part 7 retrospective output
extends the Part 4 §I.1 LOCKED `task-return-packet.json` schema with
project-level fields (project_id, state_transition, etc.). Same schema family,
different scope (per-cycle vs per-project).

Pros:
- Reuses existing F4 LOCKED schema; Part 5 already handles the base shape.
- DRY — one schema file with optional project-level fields.

Cons:
- Schema coupling — Part 7's evolution constrained by Part 4's schema.
- Field set per-project may differ enough that "superset" is awkward.

**Option B — `project-retrospective-packet.json` standalone.** Part 7 emits to
a dedicated schema file `shared/schemas/project-retrospective-packet.json`.
Part 5 §A.5 admits via §I.4 stub which references this filename.

Pros:
- Schema independence — Part 7 evolves without coupling to Part 4.
- Cleaner separation of project-scope vs cycle-scope data.

Cons:
- New schema to maintain; Phase B partner forks must adopt both.
- Risk of duplicate field definitions across packet types.

**Bundle 4 Part 7 picks ONE.** Bundle 3 declares OPTIONS only.

## §4 Cadence Options (Bundle 4 Part 7 picks ONE)

**Option α — Per project closure event (PRIMARY recommended).** Part 7 emits
retrospective when project state transitions to terminal state (closed-won /
closed-lost / paused with explicit retrospective trigger). Part 5 consumes at
NEXT compound phase boundary after the emission.

Pros:
- Project-scoped retrospective — natural unit of analysis.
- Aligns with Cagan / Shape Up "after each appetite cycle, review" pattern.

Cons:
- Sparse cadence — projects close infrequently in Phase A; long-running projects
  may not emit retrospective for months.

**Option β — Per cycle close (fallback).** Part 7 emits per-cycle (aligned with
Part 4 cycle-close event) snapshot of all active projects' retrospective
deltas.

Pros:
- Frequent cadence — matches Part 5 compound-phase event-driven trigger.
- No projects "stuck" without retrospective input.

Cons:
- Granularity mismatch — per-cycle snapshot is mostly no-delta for most active
  projects.
- Higher data volume; more events for Part 5 to process.

**Bundle 4 Part 7 picks ONE.** Bundle 3 declares OPTIONS only.

## §5 Defer Rationale

Per Joint Design lite Phase (Bundle 3 deep prompt §4.3): premature lock of
Part 7 emission contract risks incoherent design. Part 7 architecture in
Bundle 4 has access to:
- Bundle 3 Part 5 + Part 8 LOCKED schemas (consumed verbatim).
- Bundle 4 brigadier dispatch insights into project lifecycle specifics.
- Phase B operational data (if any) on appetite-overrun rates.

Therefore Bundle 4 Part 7 picks one Schema-Reference Option AND one Cadence
Option, with rationale citing Bundle 3 + 4 cumulative context. Part 5 §A.5
admissibility A-5 admits Part 7 inputs per the stub contract until Part 7
emission is finalised; production Part 7 emission is Bundle 4 finalization.

## §6 Cross-references

**From Bundle 3 (Part 5 inputs):**
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §A.5 — Part 7 retrospective input declared as Phase 2 Bundle 4 finalization upstream.
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §I.4 — UND-3 stub schema with required fields + cadence options.
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §E A-5 — admissibility A-5 admits Part 7 inputs via stub.
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §D — typed edge `Part 7 derives-from Part 5 §A.5 input contract`.

**From Bundle 4 (future Part 7 outputs):**
- Bundle 4 Part 7 §B Outputs — retrospective emission to Part 5 per the
  selected option.
- Bundle 4 Part 7 §I — schema choice (Option A or B).
- Bundle 4 Part 7 §J — cadence choice (Option α or β).

**From Wave A:**
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` §4.3 UND-3 P7→P5 cadence.

## §7 Status

**Status:** stub-Bundle-3-defer-Bundle-4. F2 (low confidence — premature lock
prevented). F4 on Bundle 4 Part 7 conformance to one of the declared options.

Bundle 3 declares EXPECTATIONS; Bundle 4 Part 7 conforms.
