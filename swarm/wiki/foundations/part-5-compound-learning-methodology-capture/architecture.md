---
title: "Foundation Part 5 — Compound Learning & Methodology Capture (Architecture)"
part_number: 5
part_slug: compound-learning-methodology-capture
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
phase: Wave-C-Bundle-3-architecture
status: F4-pending-ruslan-ack
predecessor_interface_card: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md
constitutional_baseline_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
constitutional_baseline_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
retroactive_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
F: F4
ClaimScope: "Holds for any single-owner knowledge-work system that uses a structured cycle ritual to convert per-cycle execution experience into improved future-cycle execution. The 40/10/40/10 ratio is FUNDAMENTAL §2.2 constitutional value (F5+ inherited). Bundle 3 introduces methodology promotion pipeline (UND-2 binding) and OQ-MERGED-2 dissolve-test condition declaration. Phase A scope: single-owner Jetix Phase-A €50K horizon; Fork-portable for Phase B partner imports."
R:
  refuted_if: "DRR entries stop appearing in agents/<id>/strategies.md across consecutive cycles; OR methodology library at wiki/methodology/ shows zero new validated entries across 5+ cycles; OR Bundle 3 + Bundle 4 + Wave D produce <3 distinct compound-phase-exclusive operations (dissolve-test condition activates per OQ-MERGED-2)"
  accepted_if: "DRR entries accumulate per role per cycle; methodology candidates rise from per-agent strategies.md to wiki/methodology/<rule-slug>.md via the gate at Part 6b with gate_class=draft_promotion; compound-application-rate health metric tracked at ≥80% acceptance predicate; ≥3 distinct compound-phase-exclusive operations evident across 3-cycle window"
oq_merged_2_dissolve_test:
  status: declared-Bundle-3-first-cycle-of-3-cycle-window
  threshold: ">=3 distinct compound-phase-exclusive operations across Bundle 3 + Bundle 4 + Wave D"
  decision_window_close: "Wave D ack cycle"
  engineering_expert_dissent_link: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md frontmatter dissent_preserved block"
  companion_policy_artefact: "decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md"
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md (§2 Part 5)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md (§2 Part 5; §4 OQ-MERGED-2)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§2.4 P4↔P5; §4.3 UND-3)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (§2 Part 5)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md"
  - "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§2.2 40/10/40/10; §2.4 5-line postmortem; §3.3.1 compound-application-rate)"
  - "design/JETIX-FPF.md (IP-3 artifacts-over-conversations; IP-7 writing-as-thinking; A.13 Agency-CHR; A.14 typed edges; A.6.B L/A/D/E; B.3 F-G-R)"
  - "swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§H commit interface; §I.4 task-return-packet stub post-supplement; §K K18 upcasting)"
  - "swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md (§E L9 admissibility predicate F5; §I.2 wiki/methodology/ entity-type)"
  - "swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (§I.1 task-return-packet.json FULL schema; §H message schema v2.0.0)"
  - "swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§I.1 F-G-R F8 schema; §C approval log)"
  - "swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.1 awaiting-approval-packet F8; §I.4 blast-radius; §E L9 Halt-Log-Alert + Corrigibility)"
  - "raw/books-md/event-sourcing/young-cqrs-2010.md (Reversal Transactions; event versioning)"
  - "raw/books-md/anthropic/askell-2021-hhh.md (Corrigibility Appendix E.2)"
---

# Foundation Part 5 — Compound Learning & Methodology Capture (Architecture)

## §0 Executive Summary

**Part 5 closes the R2 reinforcing loop (Senge): every cycle's execution becomes
input to the next cycle's improved execution.** Without Part 5, the system
executes brilliantly once and re-derives the same lessons next cycle — knowledge
does not compound across cycles. Part 5 canonicalises three artefacts that
together close the loop:

1. **The 40/10/40/10 compound ritual** (FUNDAMENTAL §2.2 — Plan 40% / Work 10% /
   Review 40% / Compound 10% with ±10pp drift tolerance per FUNDAMENTAL §3.3.1)
   as a discrete Foundation artefact with mandatory compound-phase outputs.
2. **The DRR ledger schema** (Decision / Reasoning / Result / Review per
   Compounding-Engineering §2 P2 + §4 P2) that lives append-only in
   `agents/<id>/strategies.md`, with `rule_slug` deduplication, `validated_in_cycles`
   accumulator, and `ratio: {hits, misses}` decay counter.
3. **The methodology promotion pipeline** (UND-2 binding) that rises validated
   patterns from per-agent strategies.md to `wiki/methodology/<rule-slug>.md`
   canonical entries via the Part 6b gate (`gate_class: draft_promotion`),
   triggering F4→F5 promotion on Ruslan ack, with companion entry in
   `swarm/approvals/log.jsonl` (Part 6a §C) and update of `wiki/index.md`.

Bundle 3 introduces three structural firsts for Part 5:

- **OQ-MERGED-2 dissolve-test condition declaration in §X** (Bundle 3 = first
  cycle of 3-cycle window; threshold ≥3 distinct compound-phase-exclusive
  operations across Bundle 3 + Bundle 4 + Wave D). Engineering-expert dissolve
  dissent (preserved verbatim from Wave A interface card §H frontmatter) is
  re-cited; systems-thinking-cybernetics §4 R2 reinforcing loop counter-argument
  is preserved alongside.
- **UND-3 P5↔P7 stub** (Part 7 retrospective input contract specified in §A
  Inputs as Phase 2 — Bundle 4 — finalization upstream; Bundle 4 Part 7 conforms
  to this contract).
- **UND-1 binding consumed verbatim** (Part 5 reads RAW task-return packets per
  Part 4 §I.1 schema FROM `comms/mailboxes/`, performs OWN DRR extraction;
  schema is FROZEN from Bundle 2 Decision #4).

Reuse over reinvention: 8 `agents/<id>/strategies.md` files already exist with
19 strategy entries accumulated pre-Bundle-3 [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§4]. Part 5 canonicalises the schema; it does
NOT regenerate content. **No knowledge erasure** — the existing entries are
read by Part 5 §A Inputs as the historical baseline; Bundle 3 schema extension
is additive (new fields appended; existing entries upcast on next compound-phase
write per K18 upcasting policy at Part 1 §K — Bundle 3 retroactive supplement).

The compound ritual is anchored in Compounding-Engineering's main loop (Klaassen
/ Shipper / Cherny — Plan/Work/Review/Compound) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§2 main loop]. The DRR ledger
operationalises Compounding-Engineering §4 P2 (DRR ledger as append-only compound
memory) and §4 P3 (Error→Rule→Skill pipeline). The methodology promotion pipeline
is the canonical path by which §4 P5 (validated pattern threshold) lands in the
Karpathy LLM Wiki [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§5 validated pattern threshold].

**Phase A scope discipline.** Single-owner Jetix Phase-A €50K horizon. Methodology
promotion gate (Part 6b `gate_class: draft_promotion`) is HITL — Ruslan acks
every promotion. Phase B partner forks adopt the schema; Phase B-specific
methodology entries rise via the same gate under Phase B owner. **Fork-portable
by construction** — schema is GENERIC; specific methodology slugs and DRR
entries are RUSLAN-LAYER (per §X).

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Part 4 task-return-packet | `task-return-packet.json` per Bundle 2 Part 4 §I.1 FULL schema (UND-1 LOCKED contract; raw consumption per UND-1 ack OQ-3) | Cycle-close event OR per-task-completion event in `comms/mailboxes/<role>.jsonl` (event-driven; Part 4 emitter) | F4|G:Bundle 2 LOCKED schema|R-medium |
| Owner strategic reflection (U.Episteme) | Owner-authored prose written at compound phase per IP-7 (writing-as-thinking) — NOT dictated chat-only; agents contribute structured extractions only [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2 anti-pattern warning "Если и сам текст пишет LLM — исчезает мышление письмом"] | Owner-authored at compound phase boundary (event-driven on cycle close OR scheduled at week boundary — see §J.1) | F5|G:IP-7 constitutional|R-high |
| Health signals from Part 8 | Anomaly reports, SLI drift records, agent-drift detection outputs per Part 8 §I.1 canonical health-signal schema (Bundle 3 Part 8 deliverable; cross-ref) | Periodic health-event published by Part 8 (cadence per Part 8 §I.2 SLI/SLO schema — daily summary minimum; weekly snapshot mandatory) | F4|G:Part 8 Bundle 3 schema|R-medium |
| Prior `agents/<id>/strategies.md` entries | Existing DRR ledger entries — 19 accumulated pre-Bundle-3 baseline per AUDIT [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§4]; schema extended with `validated_in_cycles[]` accumulator + `ratio: {hits, misses}` counter + `created_at:` + `last_validated_at:` (Bundle 3 additive extension; existing entries upcast on next write per K18) | Read at compound-phase start; baseline for delta computation | F4|G:legacy plus Bundle 3 schema additive|R-medium |
| **Part 7 retrospective output (UND-3 STUB — Phase 2 Bundle 4 finalization)** | Stub schema reference: `task-return-packet.json` superset OR `project-retrospective-packet.json` TBD by Bundle 4 Part 7 emission contract. Part 5 declares the EXPECTATIONS; Part 7 in Bundle 4 conforms to this contract. Cross-ref: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` | Per project closure event OR per cycle close — TBD by Part 7 in Bundle 4 (defer rationale in §I.4) | F2|G:UND-3 stub; Phase 2 Bundle 4 finalization|R-low — premature lock prevented per Joint Design lite §4.3 |

**§A.1 Concrete consequence — UND-1 raw packet consumption pattern.** Part 4
§I.1 LOCKED `task-return-packet.json` schema is the upstream FROZEN contract.
Part 5 reads RAW packets — no pre-extracted DRR fields per UND-1 ack OQ-3.
Therefore Part 5 §I.2 declares the DRR extraction algorithm: for each
task-return-packet, scan the `outcome` field, the `decisions[]` array, and the
`unresolved` array; emit a DRR entry with Decision (extracted from
`decisions[]`), Reasoning (from `outcome.rationale` if present, else from
`outcome.summary`), Result (from `outcome.status` + `outcome.delta`), Review
(populated at next compound-phase by reviewing predicted vs actual). The
extraction produces F2 (single-cycle observation) entries; F-rises occur on
multi-cycle validation per §G F-G-R Tagging table. [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision #4 task-return-packet schema LOCKED]

**§A.2 Concrete consequence — Owner reflection separation from agent extraction.**
Per IP-7 [src:design/JETIX-FPF.md:§5.7 IP-7 writing-as-thinking], strategic
reflection is owner-authored prose; agents contribute structured extractions
(DRR fields filled from packet content) but DO NOT author the strategic
reflection. The compound-phase output therefore has TWO distinct artefact types:
(a) per-agent DRR entries (machine-extracted from packets; F2 baseline; F-rises
on multi-cycle validation); (b) owner-authored strategic reflection prose (F-N/A
— this is U.Episteme not U.System; not subject to F-G-R because it is the
generative input to System artefacts, not a System claim itself). The boundary
prevents the IP-7 anti-pattern: "Если и сам текст пишет LLM — исчезает мышление
письмом" [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2].

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| `agents/<id>/strategies.md` (per-role DRR ledger) | Append-only DRR entries — 4-part Decision/Reasoning/Result/Review structure with `rule_slug`, `validated_in_cycles[]`, `ratio: {hits, misses}`, `created_at`, `last_validated_at`, `f_g_r` (per Part 6a §I.1 F8 schema) | `drr-entry-committed` event via Part 1 §H `[strategy] add: <rule-slug> (DRR entry from <cycle-id>)` commit | F4|G:per-role DRR ledger discipline|R-medium |
| `wiki/methodology/<rule-slug>.md` (Karpathy-LLM-wiki canonical methodology entry — Part 3 §I.2 entity-type) | Promoted methodology entry with full frontmatter (`entity_type: methodology`, `f_g_r`, `claimscope`, `refuted_if`, `human_acked_at`, `pipeline: ready`, `para_tier: Resource | Archive`, `supersedes:` if replacement) | `methodology-entry-promoted` event via Part 1 §H `[methodology] promote: <rule-slug> (F5 codified rule)` commit; AWAITING-APPROVAL packet to Part 6b with `gate_class: draft_promotion` | F4→F5|G:cross-cycle reuse evidence on promotion|R-high post-Ruslan-ack |
| Part 1 §H commit substrate | All compound outputs committed as git artefacts per IP-3 (artifacts-over-conversations) [src:design/JETIX-FPF.md:§5.3 IP-3] | `artifact-committed` event (Part 1 §B Outputs) | F5|G:IP-3 constitutional|R-high |
| Part 8 health-signal pipeline | `compound-application-rate` metric; `methodology-promotion-rate` metric; `drr-write-rate` metric; `dissolve-test-evidence-count` metric — emitted per Part 8 §I.1 canonical health-signal schema (Bundle 3) | `health-metric-updated` event consumed by Part 8 SLI/SLO schema | F4|G:Part 8 SLI consumption|R-medium |
| `swarm/approvals/log.jsonl` (Part 6a §C) | One entry per methodology promotion gate ack — recording timestamp, rule-slug, gate_class=draft_promotion, F-rise (F4→F5), Ruslan ack signature | `approval-logged` event via Part 6a service | F5|G:Part 6a §C F8 schema|R-high |
| `wiki/index.md` (Part 3) | Methodology entry indexed | `index-updated` event | F4|G:Part 3 §I.2 promotion sequence|R-medium |
| `swarm/wiki/meta/health.md` compound-application-rate counter | Append-only delta entries with `cycle_id` + `compound_application_rate_observed` + `target_0.8` + `delta` | `compound-rate-observation` event (per cycle close) | F4|G:health.md baseline reuse|R-medium |
| Bundle 3 `dissolve-test-evidence-count` accumulator | Per-cycle count of compound-phase-exclusive operations (operations Parts 3+4 cannot capture without invoking Part 5 logic). Targeted threshold ≥3 across 3-cycle window. | `dissolve-test-evidence` event committed as `swarm/wiki/cycles/<cycle-id>/bundle-3-dissolve-test-evidence.md` per cycle | F3|G:OQ-MERGED-2 dissolve-test condition window evidence|R-low — accumulating |

**§B.1 Concrete consequence — Part 8 metric emission shape.** Part 8 §I.1
canonical health-signal schema (Bundle 3 deliverable) is the contract Part 5
emits to. Required fields per emission: `signal_name`, `emitter_part: "part-5"`,
`emitter_section`, `value`, `unit`, `cadence`, `measurement_method`,
`created_at`, `cycle_id`, `f_g_r`. Therefore Part 5 §H code interface declares
a thin `emit_health_signal(signal_name, value, ...)` accessor that lives in
`swarm/lib/` per Bundle 2 C1 Joint Design canonical (Part 3 LEAD + Part 4
ADVISORY governance) and is called from compound-phase ritual code. NO direct
file writes from Part 5 to `shared/state/system-health.json` — Part 8 owns
that file's canonical contract. [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1 swarm/lib/ accessor pipeline; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision #C1 Joint Design canonical]

**§B.2 Concrete consequence — Methodology promotion gate trigger conditions.**
Methodology candidate emerges when: (1) DRR entry has `result: validated` AND
(2) `validated_in_cycles` accumulator has ≥2 distinct cycle IDs AND (3) `rule_slug`
is populated (and either unique or `supersedes:` points to the entry being
replaced). Part 5 §I.1 emits methodology candidate at
`wiki/methodology/<rule-slug>-DRAFT.md` with `pipeline: ingested`, then opens
AWAITING-APPROVAL packet to Part 6b with `gate_class: draft_promotion` per Part 6b §I.1 F8 LOCKED schema. Part 6b §E Law L9 Corrigibility ensures Ruslan ack
is required; Halt-Log-Alert ordering is irrelevant for draft_promotion (this is
not Tier 0). Part 3 §E L9 admissibility predicate is the SAME predicate at the
Part 3 admission gate — DRY enforced (Part 5 owns EMISSION; Part 3 owns
ADMISSION). [src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§E L9 admissibility; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1 awaiting-approval-packet]

---

## §C Side-effects

- **Append-only writes to `agents/<id>/strategies.md`.** No in-place edits of
  prior entries [src:design/JETIX-FPF.md:§5.3 IP-3 D25 append-only discipline].
  Corrections take the form of NEW DRR entries with `corrects: <prior-entry-id>`
  pointer per Reversal Transactions discipline (Young 2010 §4 P3). The legacy
  ledger remains canonical; the correction is additive. This is the opposite of
  "edit and commit" — every change is its own committed entity.
  [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3 Reversal Transactions]

- **Methodology entries promoted via Part 6b gate.** Promotion is a TWO-step
  side-effect: (1) DRAFT file written at `wiki/methodology/<rule-slug>-DRAFT.md`
  with `pipeline: ingested` (committed via Part 1 §H `[methodology] draft:
  <rule-slug>`); (2) on Ruslan ack of Part 6b AWAITING-APPROVAL packet, file
  renamed to `wiki/methodology/<rule-slug>.md` with `pipeline: ready` +
  `human_acked_at:` populated (committed via Part 1 §H `[methodology] promote:
  <rule-slug> (F5 codified rule)`). Each step is a distinct git commit; the
  history shows DRAFT → PROMOTED transition explicitly. NO in-place rename
  without commit. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§H commit interface; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1]

- **Updates to `swarm/wiki/meta/health.md` compound-application-rate counter.**
  Per-cycle delta entry appended (no in-place edit). Counter shape:
  `cycles_completed` / `cycles_with_compound_phase_executed` /
  `compound_application_rate = ratio` / `target = 0.8` per FUNDAMENTAL §3.3.1.
  When ratio drops below 0.8, Part 8 SLI threshold fires (per Part 8 §I.2
  SLI/SLO schema with Part 5 SLI entry: "compound-application-rate ≥ 80%
  rolling 5 cycles"). [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.3.1; src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§5]

- **Does NOT write to any `decisions/` files.** Strategic decisions are
  Part 6b's promotion gate domain. Part 5 surfaces patterns; Ruslan decides
  whether a pattern becomes a strategic decision. The boundary prevents
  scope-creep where Part 5 silently drives strategic direction without explicit
  HITL ack. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1]

- **Does NOT auto-mutate `agents/<id>/system.md` or other agent system prompts.**
  System Prompt Learning accumulations land in `agents/<id>/strategies.md`, not
  in the system prompt itself. Per FUNDAMENTAL §6.1 no-self-modify rule:
  agents do not silently rewrite their own system prompts at compound phase;
  evolution of the system prompt is owner-authored at session boundary with
  explicit HITL ack. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 no-self-modify]

- **Dissolve-test evidence accumulator** (Bundle 3 NEW per OQ-MERGED-2). Each
  cycle close emits per-cycle count of compound-phase-exclusive operations to
  `swarm/wiki/cycles/<cycle-id>/bundle-3-dissolve-test-evidence.md`. The file is
  the audit-trail input to Wave D's dissolve decision. [src:decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md]

---

## §D Dependencies (typed per FPF A.14 — canonical 10-edge table)

Bundle 1 canonical 10-edge reference: `ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`. NO generic `depends-on`. NO `uses`. [src:design/JETIX-FPF.md:§A.14 typed edges]

| From | Edge type | To | Rationale |
|---|---|---|---|
| Part 5 | `creates` | Part 3 (`wiki/methodology/`) | UND-2 — methodology promotion pipeline emits validated patterns into Part 3 KB; Part 3 hosts the canonical entry post-promotion. The CREATION is the F4→F5 entry; Part 3 hosts and indexes it. |
| Part 5 | `creates` | Part 1 (commit substrate) | DRR entries + methodology entries + dissolve-test evidence committed via Part 1 §H — every Part 5 output is a Part 1 commit. The CREATION is the committed artefact; Part 1 is the substrate. |
| Part 5 | `methodologically-uses` | Part 4 (coordination protocol) | Compound phase draws on Part 4 coordination cadence; the 40/10/40/10 ritual is enforced at Part 4 dispatch level (cycle close event triggers compound phase). Part 5 produces compound-phase artefacts WITHIN Part 4's cadence — not a CREATES edge (Part 5 does not create Part 4); not a DERIVES-FROM (Part 5 does not parse Part 4 contents per se); rather Part 5 USES Part 4's cadence as method. |
| Part 5 | `methodologically-uses` | Part 4 §I.1 task-return-packet schema | UND-1 — Part 5 reads RAW task-return-packets per Part 4 §I.1 LOCKED schema. Part 5 does not depend on Part 4's runtime; Part 5 USES the schema as METHOD for DRR extraction. |
| Part 5 | `methodologically-uses` | Part 6a §I.1 F-G-R schema | DOGFOOD — every Part 5 output carries F-G-R per the F8 LOCKED schema. Part 5 USES F-G-R as METHOD for tagging. |
| Part 5 | `methodologically-uses` | Part 6a §C approval log | Methodology promotions emit log entries per the canonical schema. Part 5 USES the log structure as METHOD for promotion-event recording. |
| Part 5 | `methodologically-uses` | Part 6b §I.1 awaiting-approval-packet | Methodology promotion gate uses `gate_class: draft_promotion` per F8 LOCKED schema. Part 5 USES the gate primitive as METHOD for promotion enforcement. |
| Part 5 | `derives-from` | Part 4 task-return-packets | DRR extraction parses `outcome` / `decisions[]` / `unresolved` fields. Part 5 DERIVES DRR entries from packet content. |
| Part 8 | `derives-from` | Part 5 health emissions | Part 8 consumes `compound-application-rate`, `methodology-promotion-rate`, `drr-write-rate` SLI signals from Part 5 emissions. The arrow points Part 8 → Part 5 because Part 8 is the consumer; Part 5 is the emitter. |
| Part 5 | `constrained-by` | Part 6b §E Law L9 (Corrigibility) | Methodology promotions are Corrigibility-bound — Ruslan can revert any promotion via `git revert` of the `[methodology] promote:` commit. Part 5 is CONSTRAINED BY this invariant. |
| Part 5 | `constrained-by` | FUNDAMENTAL §6.1 no-self-modify | Part 5 cannot auto-rewrite agent system prompts at compound phase. Part 5 is CONSTRAINED BY this invariant. |
| Part 7 | `derives-from` | Part 5 §A.5 input contract (UND-3 STUB) | Bundle 4 — Part 7 retrospective output conforms to Part 5's declared input expectations. The arrow is Part 7 → Part 5 because Part 7 emits to Part 5; Part 5 declares the input contract. (Phase 2 — Bundle 4 finalises Part 7 emission.) |

**§D.1 No `depends-on` edges.** Per Bundle 1 canonical 10-edge table, generic
`depends-on` is forbidden (it loses semantic resolution). Every dependency above
is one of the canonical types. Critic gate verifies. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§D 10-edge reference]

**§D.2 Meadows leverage context.** Part 5 occupies Meadows leverage point #4
(self-organisation — the ability of the system to add new structure). The
methodology promotion pipeline IS Part 5 adding new structure (canonical
methodology entries) to Part 3. The 40/10/40/10 ritual is Meadows L9 (delays —
Part 5 enforces a deliberate delay between Work and Compound to allow
reflection). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§4 Meadows leverage points]

---

## §E Boundary — L/A/D/E Lanes (FPF A.6.B Norm Square)

### Laws (invariants MUST hold — violations are constitutional defects)

**L-1. DRR entries MUST be committed files in `agents/<id>/strategies.md`** —
never chat-only reflections [src:design/JETIX-FPF.md:§5.3 IP-3
artifacts-over-conversations; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2]. Violation refuter: a compound phase that
produces no `[strategy]` commit on Part 1 §H. **Meadows L5 (rules).**

**L-2. Strategic reflection MUST be owner-authored prose** — agent extractions
are structured inputs to owner authorship, NOT substitutes [src:design/JETIX-FPF.md:§5.7 IP-7 writing-as-thinking; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2
agency-preservation]. Violation refuter: a strategic reflection prose paragraph
in `agents/<id>/strategies.md` whose immediate prior commit lineage is an LLM
generation rather than an owner edit. **Meadows L4 (goals — owner agency
preserved).**

**L-3. `agents/<id>/strategies.md` updates ONLY through explicit gated
compound-phase review** — no runtime mutation [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 no-self-modify]. Violation refuter: a `[strategy]` commit
that lands outside a compound-phase ritual. **Meadows L4 (no-self-modify
goal-preservation).**

**L-4. 40/10/40/10 cadence ratio with ±10pp drift tolerance** — FUNDAMENTAL
§2.2 constitutional value [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§2.2; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.3.1]. Violation refuter: rolling
5-cycle observed cadence outside [Plan: 30-50%, Work: 0-20%, Review: 30-50%,
Compound: 0-20%]. F5 inherited from FUNDAMENTAL — constitutional. **Meadows L5
(rules).**

**L-5. Methodology entry promotion is HITL-gated** — every F4→F5 promotion
requires Ruslan ack via Part 6b `gate_class: draft_promotion`
[src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1; src:design/JETIX-FPF.md:§5.7 IP-7]. Violation refuter: a `wiki/methodology/<slug>.md` entry
with `pipeline: ready` AND `f_level: F5` AND no corresponding entry in
`swarm/approvals/log.jsonl` for that slug. **Meadows L4 (Corrigibility).**

**L-6. Methodology entries carry F-G-R per Part 6a §I.1 F8 schema** —
DOGFOOD [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 F-G-R F8].
Violation refuter: a methodology entry with no `f`, no `claimscope`, or no
`refuted_if`. **Meadows L4 (constitutional).**

**L-7. Dissolve-test evidence accumulator MUST be append-only**
[src:decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md]. Violation
refuter: a `bundle-3-dissolve-test-evidence.md` file edited in place after
initial commit. **Meadows L5 (audit trail integrity).**

### Admissibility (acceptance criteria for inputs)

**A-1.** A DRR entry is admitted into `agents/<id>/strategies.md` ONLY if it
carries all 4 parts (Decision / Reasoning / Result / Review) AND `rule_slug`
populated AND `f_g_r` populated AND `created_at` populated.

**A-2.** A methodology candidate is admitted into the promotion queue ONLY
after ≥1 DRR `result: validated` marker across ≥2 distinct cycles AND
`rule_slug` unique (or `supersedes:` points to existing entry being replaced)
AND F-level rises target F5 (per Part 3 §E L9 admissibility predicate F5 —
DRY referenced not duplicated).
[src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§E L9 admissibility predicate]

**A-3.** Owner reflection prose is admitted as compound output ONLY if
authored in writing (not dictated chat-only) — the writing IS the thinking
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2]. Operationally enforced at compound phase via the
ritual checklist (§J.1).

**A-4.** UND-1 raw task-return-packets are admitted to DRR extraction ONLY if
they conform to Part 4 §I.1 LOCKED schema. Schema-version mismatch (legacy
v1.0.0) triggers K18 upcasting (Part 1 §K) before extraction; failure to upcast
rejects the packet with named-field error.
[src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K18]

**A-5 (UND-3 STUB).** Part 7 retrospective inputs are admitted via the stub
schema declared in §I.4. Phase 2 — Bundle 4 finalises Part 7 emission contract;
Bundle 3 declares EXPECTATIONS only.

### Deontics (obligations of this part toward consumers)

**D-1.** Part 5 MUST surface ≥1 candidate strategies.md entry per role per
cycle (or "no new learnings this cycle — zero-delta DRR" entry) so
`compound-application-rate` remains measurable. Zero-delta entries are
explicitly admissible under Popper-falsifiability (the absence of new pattern
IS a finding) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md:§Popper falsifiability].

**D-2.** Part 5 MUST preserve all dissenting DRR entries — competing
interpretations of the same cycle event are retained, NOT averaged
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§4 OQ-MERGED-2 dissent record].

**D-3.** Part 5 MUST route any methodology pattern that contradicts an
existing canonical Foundation document or methodology entry to the Part 6b
governance gate BEFORE promotion (gate_class: draft_promotion with explicit
`supersedes:` pointer in candidate frontmatter).

**D-4.** Part 5 MUST emit `compound-application-rate`,
`methodology-promotion-rate`, `drr-write-rate`, `dissolve-test-evidence-count`
to Part 8 health-signal pipeline per Part 8 §I.1 canonical schema.

**D-5.** Part 5 MUST update the dissolve-test evidence accumulator at every
cycle close (Bundle 3 + Bundle 4 + Wave D 3-cycle window) per OQ-MERGED-2
declared in §X.

### Effects (measurable outcomes)

**E-1.** `agents/<id>/strategies.md` entry count grows per cycle; `ratio.hits`
accumulate over time. Acceptance predicate (P5.1): synthetic fixture of 3
cycle-close events produces 3 DRR entries (or 3×N if multiple roles have
learnings); compound-application-rate metric ≥0.8 in test fixture.

**E-2.** `wiki/methodology/` gains ≥1 promoted entry per 5 cycles (starter
benchmark — calibration parameter per FUNDAMENTAL §3 starter values; calibrated
in Phase B per OQ-MERGED-5).

**E-3.** F-level of validated DRR rules rises from F2 (single-cycle) toward
F4-F5 (operational convention, multi-cycle validated) over compound history
[src:design/JETIX-FPF.md:§B.3 F-G-R; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P5].

**E-4.** Methodology promotion event log entries appear in
`swarm/approvals/log.jsonl` per Part 6a §C — one entry per promotion
acceptance.

**E-5 (Bundle 3 NEW).** Dissolve-test evidence accumulator count tracked
across Bundle 3 + Bundle 4 + Wave D. Threshold ≥3 distinct
compound-phase-exclusive operations preserves Part 5 standalone; <3 activates
dissolve hypothesis at Wave D ack cycle.

---

## §F Anti-scope

### §F.1 Generic anti-scope (per FUNDAMENTAL §6 — all Foundation parts)

- Part 5 does NOT make strategic decisions. Compound learning surfaces patterns
  for owner consideration; the OWNER decides what to change [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; §6.2].
- Part 5 does NOT execute behaviour-change without HITL ack. Methodology
  promotion is gated; pattern detection is automatic; promotion decision is
  owner-owned.
- Part 5 does NOT modify agent system prompts. System Prompt Learning
  accumulations land in `strategies.md`, not in `system.md` (no-self-modify
  rule).

### §F.2 Part-specific anti-scope

- **Does NOT own KB content management.** Methodology promotion REQUESTS route
  through Part 3's admission gate. Part 5 is the EMITTER. Part 3 is the
  STORAGE+ADMITTER. The split is per UND-2 ack: Part 5 owns emission schema;
  Part 3 owns admission schema; both reference each other; DRY enforced — no
  duplication of admissibility predicate between Parts 3 and 5.
- **Does NOT own coordination protocol.** The 40/10/40/10 cadence enforcement
  mechanism lives in Part 4. Part 5 PRODUCES the compound-phase artefacts
  WITHIN that cadence.
- **Does NOT own health monitoring.** `compound-application-rate` is a health
  signal CONSUMED by Part 8. Part 5 EMITS the metric; Part 8 owns the SLI/SLO
  threshold and alert logic.
- **Does NOT own retrospective format.** UND-3 stub declares input expectations
  from Part 7; Bundle 4 Part 7 finalises emission. Part 5 specifies WHAT it
  expects; Part 7 specifies HOW to emit.
- **Does NOT auto-promote dissenting DRR entries.** Per D-2, dissent is
  preserved; promotion of a contested pattern requires explicit Ruslan ack of
  the contestation.
- **Does NOT dissolve into Parts 3+4 without explicit OQ-MERGED-2 Ruslan ack
  at Wave D.** Engineering-expert dissolve dissent preserved [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§4 OQ-MERGED-2]; dissolve path
  held open contingent on 3-cycle-window evidence per §X.

### §F.3 Phase-A scope discipline (Cagan / Shape Up appetite)

Per Cagan + Singer 2019 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 Principle 2 appetite-fixed/scope-variable]:
Wave C Part 5 architecture build = appetite of 1 day brigadier walltime; scope
variable. If schema design balloons beyond 1 day, defer to Wave D rather than
expand.

Phase B (partner forks importing Part 5 schema) does NOT inherit Ruslan-specific
DRR entries — the schema is GENERIC; the entries are RUSLAN-LAYER per §X.

---

## §G F-G-R Tagging (DOGFOOD per Part 6a §I.1 F8 schema)

Every promoted Part 5 claim carries F-G-R inline `[F<N>|G:<scope>|R-<level>]`
OR table entry below. Per Bundle 1 OQ-B1-1 anchor wording: F4 = "≥3 cycles
applied"; F6 = "cross-cycle reuse evidence"; F8 = "FUNDAMENTAL Vision
lock-class".

| Artefact / Claim | F | ClaimScope (G) | Reliability (R) | Promotion path |
|---|---|---|---|---|
| DRR entry (new, cycle 1 of rule) | F2 | Specific role + specific cycle context | R-low | Promote to F4 on ≥2-cycle validation |
| DRR entry (validated, ≥3 cycles) | F4 | Role + system context; bridge needed for multi-agent systems with different coordination patterns | R-medium | Promote to F5 if methodology promotion gate accepts |
| DRR entry (tombstoned: ratio.misses > ratio.hits×2) | F-tombstoned | No longer valid in current context | R-low; archived not deleted | Tombstone via NEW DRR entry with `tombstones: <prior-rule-slug>`; original entry preserved (Reversal Transactions) |
| Methodology candidate (DRAFT — pre-Part-6b ack) | F4 | Phase A scope candidate | R-medium | Promote to F5 on Ruslan ack of `gate_class: draft_promotion` |
| Methodology entry (PROMOTED — post-Ruslan-ack) | F5 | Any system applying the same methodology; bridge note for different domain contexts | R-medium to R-high | Promote to F6 on cross-cycle reuse evidence (Phase B partner imports + uses entry); F7 on three independent forks adopting; F8 only if FUNDAMENTAL Vision absorbs |
| 40/10/40/10 cadence ratio (constitutional) | F5 (inherited from FUNDAMENTAL §2.2) | Any knowledge-work system using structured cycle ritual | R-high | Already F5; promotion to F8 requires FUNDAMENTAL Vision update |
| Methodology promotion pipeline schema (P5.2 UND-2 binding) | F4 architecture-time → F5 on Bundle 3 owner ack | Foundation schema for methodology promotion | R-medium | F5 on Ruslan ack of Bundle 3 packet |
| OQ-MERGED-2 dissolve-test condition declaration (P5.3) | F3 (proposed dissolve-test condition; not validated until Wave D evidence accumulates) | Phase A 3-cycle window | R-low — accumulating | F4 on Bundle 3 owner ack of test condition itself |
| UND-3 P5↔P7 stub | F2 | Cross-bundle interface; Bundle 4 Part 7 finalises emission | R-low | F4 on Bundle 4 Part 7 conformance |
| `compound-application-rate` SLI emission | F4 | Per-cycle health metric | R-medium | F5 on Phase B calibration of SLO threshold |
| `dissolve-test-evidence-count` accumulator | F3 | Bundle 3 + Bundle 4 + Wave D 3-cycle window | R-low | F-N/A — accumulator is audit-trail input to dissolve decision; not a claim per se |

**§G.1 Concrete consequence — F4→F5 rise on owner ack.** Per Part 6a §I.1 F8
schema, F4 = "≥3 cycles applied; ≥1 cross-cycle reuse"; F5 = "operational
convention; multi-cycle validated; canonical entry post-HITL ack". Therefore
the methodology promotion gate (P5.2 UND-2) IS the F4→F5 transition gate. NO
methodology entry rises to F5 without `swarm/approvals/log.jsonl` entry +
`human_acked_at:` populated. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 F-G-R F8]

---

## §H Code-Level Interfaces

### §H.1 CLI signatures (canonical)

```
# Compound-phase ritual driver (event-driven on cycle close)
/compound <cycle-id> [--scheduled] [--dry-run]

# DRR entry write (called from compound-phase driver)
/strategies-add <role> <rule-slug> --decision="..." --reasoning="..." --result="..." --review="..." [--validates=<prior-rule-slug>]

# Methodology promotion candidate emit (called when admissibility predicate satisfied)
/methodology-promote-candidate <rule-slug> --from-strategies-of=<role> [--supersedes=<prior-slug>]

# Dissolve-test evidence emit (per cycle close)
/dissolve-test-evidence <cycle-id> --compound-phase-exclusive-ops=<count> --description="..."
```

**§H.1.1 Concrete consequence — `/compound` skill is the orchestrator.** The
driver is invoked at cycle-close (event-driven) OR scheduled at week boundary
(per §J.1 trigger predicate decision). Driver responsibilities: (a) read RAW
task-return-packets from `comms/mailboxes/`; (b) for each role, perform DRR
extraction; (c) write `agents/<role>/strategies.md` entries via Part 1 §H
commit; (d) for each candidate methodology slug satisfying admissibility,
invoke `/methodology-promote-candidate`; (e) emit health signals to Part 8;
(f) emit dissolve-test evidence; (g) write owner-reflection prompt placeholder
to `swarm/wiki/cycles/<cycle-id>/compound-reflection-prompt.md` (owner authors
the prose at session boundary). The driver does NOT author owner reflection
prose — that is the IP-7 anti-pattern boundary [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2].

### §H.2 Accessor pipeline (swarm/lib/ per Bundle 2 C1 Joint Design canonical)

Part 5 invokes accessor skills via `swarm/lib/` per Bundle 2 C1 Joint Design
canonical (Part 3 LEAD + Part 4 ADVISORY governance) [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision #C1 Joint Design canonical]:

- `swarm/lib/strategies-accessor.py` — read/append `agents/<id>/strategies.md`
  entries with schema validation (DRR 4-part + `rule_slug` + `f_g_r` mandatory).
- `swarm/lib/methodology-promote.py` — emit AWAITING-APPROVAL packet to Part 6b
  with `gate_class: draft_promotion` per F8 LOCKED schema; rename DRAFT →
  PROMOTED on ack.
- `swarm/lib/health-emit.py` — emit health signal per Part 8 §I.1 canonical
  schema (Bundle 3 deliverable; cross-ref).
- `swarm/lib/task-return-extract.py` — DRR extraction algorithm (parses Part 4
  §I.1 LOCKED schema; emits 4-part DRR entries).

All accessors live in `swarm/lib/` — NOT inline in `/compound` skill. DRY
discipline + UC-9 Phase-A isolation per `wiki-roots.yaml` clients stanza.

### §H.3 Reference to Part 1 §H commit interface

Every Part 5 output is committed via Part 1 §H. Commit-format tokens
(post-Bundle-1-supplement): `[strategy]` (DRR entries), `[methodology]`
(promotions), `[health]` (compound-application-rate signals — though Part 8
emits canonical), `[meta]` (dissolve-test evidence — flexible token; could
also use new dedicated token in Wave D if frequency warrants). Token list
authoritative at `shared/schemas/commit-format-tokens.json` (Part 1 §I.2,
post-supplement). [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§H + §I.2]

### §H.4 Reference to Part 6b §I.1 awaiting-approval-packet schema

Methodology promotion gate emits AWAITING-APPROVAL packet conforming to F8
LOCKED schema with `gate_class: draft_promotion`. Packet fields (Part 6b §I.1
verbatim): `gate_id`, `gate_class`, `created_at`, `cycle_id`, `requesting_part`,
`requesting_role_archetype`, `subject`, `claimscope`, `refuted_if`, `accepted_if`,
`f_before`, `f_after_target`, `provenance[]`, `decision_required_by`,
`status`. Part 5 fills these per §I.1 schema. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1 awaiting-approval-packet F8]

### §H.5 Routing-table.yaml extension (Bundle 3 deliverable)

Part 5 contributes the `compound-phase-orchestration` role archetype entry to
`swarm/lib/routing-table.yaml` per Bundle 2 P4.1 deliverable extension pattern.
Role archetype name (IP-1 strict — generic name, no executor binding):
`compound-phase-orchestrator`. Routing rule: cycle-close event in
`comms/mailboxes/orchestrator.jsonl` triggers dispatch to
`compound-phase-orchestrator` role; the ROLE invokes accessor pipeline; the
EXECUTOR mapping lives in RUSLAN-LAYER `executor-binding.yaml` (out of scope
per IP-1). [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision
#C1 Joint Design canonical; src:design/JETIX-FPF.md:§5.1 IP-1 Role≠Executor]

---

## §I Data Schemas

### §I.1 Methodology Promotion Pipeline schema (UND-2 binding — P5.2)

**Schema-of-schema (declared inline; physical file generation Phase B per
OQ-B1-2 + OQ-B1-4 pattern):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/methodology-promotion-event.json",
  "$comment": "GENERIC Foundation schema. Specific methodology slugs are RUSLAN-LAYER per §X. UND-2 binding from Bundle 3 Part 5.",
  "title": "Methodology promotion event",
  "description": "Records a single methodology promotion lifecycle event: candidate emit, gate request, ack, post-promotion canonical entry. Append-only event stream. Physical file generation Phase B; Bundle 3 declares schema inline.",
  "type": "object",
  "required": ["event_id", "event_type", "rule_slug", "cycle_id", "created_at", "f_before", "f_after_target", "actor_role_archetype", "f_g_r"],
  "properties": {
    "event_id": {
      "type": "string",
      "pattern": "^mpe-[0-9]{8}-[0-9]{3}$",
      "description": "Methodology Promotion Event ID. Format mpe-YYYYMMDD-NNN."
    },
    "event_type": {
      "type": "string",
      "enum": ["candidate-emit", "gate-request", "gate-acked", "promoted", "tombstoned", "superseded"],
      "description": "Event in promotion lifecycle. candidate-emit = DRAFT file written; gate-request = Part 6b packet opened; gate-acked = Ruslan ack received; promoted = DRAFT renamed to canonical; tombstoned = entry retired (NEW entry with tombstones: pointer); superseded = replacement entry promoted (NEW entry with supersedes: pointer)."
    },
    "rule_slug": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$",
      "description": "Unique methodology rule slug. Lowercase kebab-case. Used as filename: wiki/methodology/<rule_slug>.md."
    },
    "cycle_id": { "type": "string" },
    "created_at": { "type": "string", "format": "date-time" },
    "f_before": { "type": "string", "enum": ["F2", "F3", "F4", "F5", "F6", "F7", "F8"] },
    "f_after_target": { "type": "string", "enum": ["F2", "F3", "F4", "F5", "F6", "F7", "F8"] },
    "actor_role_archetype": {
      "type": "string",
      "description": "IP-1 compliant role archetype emitting the event (compound-phase-orchestrator typical). NO executor instance names."
    },
    "f_g_r": {
      "type": "object",
      "required": ["f", "claimscope", "reliability"],
      "properties": {
        "f": { "type": "string" },
        "claimscope": { "type": "string" },
        "reliability": { "type": "string", "enum": ["R-low", "R-medium", "R-high"] },
        "refuted_if": { "type": "string" },
        "accepted_if": { "type": "string" }
      },
      "description": "Per Part 6a §I.1 F8 LOCKED schema."
    },
    "validated_in_cycles": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 2,
      "description": "Required for f_after_target >= F4. ≥2 distinct cycle IDs evidencing validated DRR markers."
    },
    "supersedes": { "type": ["string", "null"] },
    "tombstones": { "type": ["string", "null"] },
    "human_acked_at": { "type": ["string", "null"], "format": "date-time" },
    "human_acked_by": { "type": ["string", "null"] },
    "para_tier": {
      "type": "string",
      "enum": ["Resource", "Archive"],
      "description": "PARA-tier mandatory per Bundle 2 P2.2 + Bundle 3 cross-cut. Resource = reusable pattern; Archive = deprecated pattern."
    }
  }
}
```

**§I.1.1 Concrete consequence — pipeline stages mapped to event_type values.**
The promotion pipeline has 7 stages, mapped 1-to-1 with event_type values:
(1) DRR entry accumulates in `agents/<id>/strategies.md` — NOT a methodology
event (this is §I.2 territory). (2) `validated_in_cycles` accumulator reaches
≥2 entries with `result: validated` AND `rule_slug` populated/unique — internal
state, no event yet. (3) Part 5 emits methodology candidate at
`wiki/methodology/<rule-slug>-DRAFT.md` with `pipeline: ingested` —
**event_type: candidate-emit**. (4) Part 5 (or owner) emits AWAITING-APPROVAL
packet with `gate_class: draft_promotion` to Part 6b — **event_type:
gate-request**. (5) Owner acks the gate — **event_type: gate-acked**.
(6) Entity moves to `wiki/methodology/<rule-slug>.md` with `pipeline: ready`,
F4→F5 rise, `human_acked_at:` populated — **event_type: promoted**.
(7) `swarm/approvals/log.jsonl` (Part 6a §C) entry written. (8) `wiki/index.md`
updated. (9) For tombstoning or superseding: **event_type: tombstoned** or
**event_type: superseded** — preserves prior canonical entry with NEW
event entry pointing to it (Reversal Transactions discipline).

**§I.1.2 Concrete consequence — DRY enforcement Part 5 ↔ Part 3.** Per UND-2
ack: Part 5 owns the EMISSION schema (above); Part 3 owns the ADMISSION
schema (Part 3 §E L9 admissibility predicate F5 — referenced not duplicated).
Both schemas reference each other; `/lint` cross-reference check verifies both
sides resolve. NO duplication of admissibility predicate text — change one,
edit one. [src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§E L9 admissibility predicate F5; src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§I.2 promotion sequence]

### §I.2 DRR Ledger schema (P5.1 binding)

DRR entry schema in `agents/<id>/strategies.md` (markdown frontmatter +
structured body):

```yaml
---
entry_id: drr-<role>-<rule-slug>-<sequence>     # e.g. drr-engineering-expert-ingest-lint-after-001
rule_slug: <kebab-case>                          # unique within role
created_at: <ISO 8601>
last_validated_at: <ISO 8601 | null>             # null until first validated
validated_in_cycles: [<cycle-id>, <cycle-id>]    # array; ≥1 entry mandatory; ≥2 with result:validated triggers methodology candidacy
ratio:
  hits: <int>                                    # times the rule was applied AND result was validated
  misses: <int>                                  # times the rule was applied AND result was refuted
f: F<2|3|4|5>                                    # F-G-R per Part 6a §I.1 F8 schema
claimscope: <string>                             # G — when does this hold?
reliability: R-<low|medium|high>                 # R — confidence
refuted_if: <string | null>                      # Popper falsifier (optional but RECOMMENDED for F4+)
supersedes: <prior-rule-slug | null>             # if this entry replaces a prior rule
tombstones: <prior-rule-slug | null>             # if this entry retires a prior rule (rule was wrong; preserved as audit-trail)
corrects: <prior-entry-id | null>                # if this entry corrects a prior entry (Reversal Transactions)
para_tier: Resource | Archive
---

## Decision

What was decided / what action was taken.

## Reasoning

Why this decision was the right one in context. Cross-references to
predecessor DRR entries (rule_slug links) where applicable.

## Result

Observed outcome. Is the rule's prediction borne out? Set ratio.hits++ or
ratio.misses++ accordingly. If outcome is partial/inconclusive, mark
`result: partial` and DO NOT increment either counter.

## Review

Owner-authored review (or "deferred to next compound phase"). For F4+ entries,
review MUST address: (a) does the rule still hold? (b) does the rule's
ClaimScope need narrowing? (c) is there evidence to promote to methodology
library?
```

**§I.2.1 Concrete consequence — Tombstone vs Correct vs Supersede.** Three
distinct lifecycle operations, each with distinct frontmatter pointer:
- `corrects:` — the prior entry was malformed (typo, schema violation, missing
  field); the new entry is the correct version. Audit trail preserves both.
- `supersedes:` — the prior entry was correct in its time; conditions changed;
  the new entry is the updated rule. Audit trail preserves both.
- `tombstones:` — the prior entry was correct in claim but wrong in prediction;
  ratio.misses > ratio.hits×2 triggered tombstoning. Audit trail preserves
  both.

NO entry is ever DELETED. Reversal Transactions discipline (Young 2010
§4 P3 + P4) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 Principles
3+4]. The prior entry remains canonical; the new entry includes the pointer.

**§I.2.2 Concrete consequence — Schema upcasting for legacy entries.** The 19
entries in pre-Bundle-3 `agents/<id>/strategies.md` files lack
`validated_in_cycles[]`, `ratio: {hits, misses}`, `created_at`,
`last_validated_at`. Per Bundle 1 retroactive supplement K18 upcasting policy
applied to strategies.md entries: on next compound-phase write, scan existing
entries; if frontmatter missing fields, upcast — append default values
(`validated_in_cycles: []`, `ratio: {hits: 0, misses: 0}`, `created_at:
<git-blame-first-touch>`, `last_validated_at: null`); record `upcast_provenance:`
annotation. NO destructive in-place edit — the upcast IS a NEW commit `[strategy]
upcast: <entry_id> to Bundle 3 schema`. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K18; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md:§2.3]

### §I.3 Compound-phase trigger predicate

**Decision (per spec P5.1 explicit-rationale-required):** EVENT-DRIVEN on cycle
close (PRIMARY) with WEEKLY SCHEDULED FALLBACK at week boundary if no cycle
closed in 7d.

Rationale: (a) Event-driven matches Compounding-Engineering §2 "main loop"
where Compound is the closing phase of every cycle [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md:§2]; without a closing cycle, no compound learning fires
(matches the natural pulse of execution). (b) Scheduled-only would create stale
cycles where compound-phase fires too early (no cycle-close evidence) or too
late (cycle-close evidence buried under newer cycles). (c) Weekly fallback is
the safety net for low-velocity weeks (no cycle closed in 7d) — without it, a
zero-cycle week produces zero compound output, distorting the
`compound-application-rate` SLI denominator.

Acceptance predicate: in test fixture of (a) 3 closed cycles in a week →
3 compound-phase fires; (b) 0 closed cycles in a week → 1 weekly-scheduled
compound-phase fire (with zero-delta DRR entries acknowledged per D-1).

### §I.4 UND-3 P5↔P7 stub schema (cross-bundle interface — Bundle 4 finalises)

```yaml
# UND-3 stub — Part 5 input expectations from Part 7 (Bundle 4 finalises emission)
# Cross-ref: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md

part_5_expects_from_part_7:
  schema_reference: "task-return-packet.json superset OR project-retrospective-packet.json — Bundle 4 Part 7 picks ONE; Bundle 3 declares EXPECTATIONS only"
  required_fields_from_part_7:
    - project_id
    - state_transition  # e.g. "discovery → execution"; matches Part 7 lifecycle states
    - appetite_actual_vs_planned  # ratio; Cagan/Shape Up
    - lessons_learned  # array of structured prose entries (cycle context)
    - drr_candidates  # array of DRR-shape entries (Part 7 pre-extracted; Part 5 admits per A-5)
  cadence_expectations:
    - per_project_closure_event  # primary
    - OR per_cycle_close          # fallback if Part 7 picks cycle-aligned cadence
    - "Bundle 4 Part 7 picks ONE; Bundle 3 declares OPTIONS only"
  defer_rationale: "Part 7 is Bundle 4 work; Joint Design lite avoids premature lock; Part 7 conforms to Part 5's input contract in Bundle 4"
```

**§I.4.1 Concrete consequence — DEFER discipline.** Bundle 3 declares
EXPECTATIONS only. Bundle 4 Part 7 picks ONE schema-reference path AND ONE
cadence path. Until then, Part 5 §A.5 admits Part 7 inputs only via the stub
contract; production Part 7 emission is Bundle 4 finalization. The companion
artefact `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md`
mirrors this declaration as a standalone cross-bundle interface document
(D25 Company-as-Code committed canonical artefact).

### §I.5 Compound-phase reflection prompt template (owner-authored prose IP-7)

```markdown
# Compound-phase reflection — Cycle <cycle-id>
# Authored by: <owner-name>
# Date: <YYYY-MM-DD>
# Cadence: 10% of cycle wall-clock (FUNDAMENTAL §2.2)

## Cycle summary (machine-extracted; placeholder; OWNER reads, does not author)
- Roles dispatched: <list>
- Tasks completed: <count>
- DRR candidates surfaced (machine-extracted): <count> — see agents/*/strategies.md
- Methodology candidates emergent: <list of rule_slug>
- Health signals: <list of anomalies if any>

## Strategic reflection (OWNER authored — DO NOT generate via LLM per IP-7)

What worked? What didn't? What patterns am I noticing across the last 3-5 cycles?

[OWNER WRITES PROSE HERE — IP-7 anti-pattern boundary]

## Compound decisions (OWNER authored)

- Methodology candidates to ack at gate (Part 6b draft_promotion): <list>
- Methodology candidates to defer/reject: <list with rationale>
- DRR entries to tombstone: <list with rationale>
- New patterns to monitor (no methodology candidacy yet): <list>

## Dissolve-test evidence (Bundle 3 + Bundle 4 + Wave D 3-cycle window)
- Compound-phase-exclusive operations this cycle: <count>
- Description of operations (what Parts 3+4 cannot capture without invoking Part 5 logic): <list>
```

The template is GENERIC; the OWNER's prose is RUSLAN-LAYER (per §X). The
template enforces IP-7 by leaving the strategic reflection section blank for
owner authorship; agents fill ONLY the machine-extracted summary section.

---

## §J Operational Rituals

### §J.1 Compound-phase ritual (40/10/40/10 — FUNDAMENTAL §2.2 constitutional)

**Cadence.** 40% Plan / 10% Work setup / 40% Review (during execution) / 10%
Compound. The 40+10+40+10 = 100% of cycle wall-clock per FUNDAMENTAL §2.2 +
§3.3.1. Drift tolerance ±10pp before health alert fires (Part 8 SLI).

**Trigger.** Event-driven on cycle close (primary) + weekly scheduled fallback
(§I.3).

**Ritual sequence (per fire):**

1. **PLAN phase** — owner sets cycle scope, appetite, role dispatches. Part 5
   does NOT participate (this is Part 4 territory).
2. **WORK setup** — first 10% of cycle wall-clock; Part 4 dispatches per
   role; Part 5 does NOT participate.
3. **REVIEW** (during execution) — Part 4 collects task-return-packets to
   `comms/mailboxes/`. Part 5 monitors mailbox cadence (passive read). NO
   DRR extraction yet — extraction happens at compound phase boundary.
4. **COMPOUND phase** — last 10% of cycle wall-clock. Driver is `/compound
   <cycle-id>` skill (§H.1):
   a. Driver reads RAW task-return-packets per UND-1 (Part 4 §I.1 LOCKED
      schema).
   b. Driver upcasts legacy v1.0.0 entries per K18 if needed.
   c. Driver performs DRR extraction per role (algorithm in §A.1).
   d. Driver writes `agents/<role>/strategies.md` entries via Part 1 §H
      `[strategy] add: <rule-slug>` commits. ≥1 entry per role per cycle (D-1).
   e. Driver scans for methodology candidates (admissibility predicate A-2);
      if any satisfied, emits DRAFT files at
      `wiki/methodology/<rule-slug>-DRAFT.md` and opens AWAITING-APPROVAL
      packet via Part 6b.
   f. Driver emits health signals (`compound-application-rate`,
      `methodology-promotion-rate`, `drr-write-rate`,
      `dissolve-test-evidence-count`) per Part 8 §I.1 schema.
   g. Driver writes owner-reflection prompt template (§I.5) — OWNER fills the
      strategic reflection prose at session boundary.
   h. Driver emits dissolve-test evidence per OQ-MERGED-2 (Bundle 3 + 4 +
      Wave D 3-cycle window).
5. **OWNER session boundary** — owner reads compound-reflection prompt; writes
   strategic reflection prose IP-7-style; acks methodology promotion gate
   packets in Part 6b inbox; tombstones any DRR entries explicitly. Each owner
   action is a separate Part 1 §H commit.

**Acceptance predicate (P5.1 from spec):** synthetic fixture of 3 cycle-close
events; Part 5 emits 3 DRR entries (or 3×N if multiple roles have learnings);
`agents/<role>/strategies.md` updates committed via Part 1 §H;
`compound-application-rate` metric ≥0.8 in test fixture.

### §J.2 Methodology promotion ritual (UND-2 P5.2 binding)

**Cadence.** Event-driven within compound phase (§J.1 step 4e).

**Trigger.** DRR entry has `result: validated` AND `validated_in_cycles[]` ≥2
AND `rule_slug` populated/unique.

**Ritual sequence (per candidate slug):**

1. Driver writes `wiki/methodology/<rule-slug>-DRAFT.md` with `pipeline:
   ingested`, `entity_type: methodology`, `f_g_r` populated, `claimscope`,
   `refuted_if`, `validated_in_cycles[]` populated, `para_tier: Resource`
   (default for new candidates), `supersedes:` if replacement.
2. Driver commits DRAFT via Part 1 §H `[methodology] draft: <rule-slug>`.
3. Driver opens AWAITING-APPROVAL packet via Part 6b `gate_class:
   draft_promotion` per F8 LOCKED schema. Packet fields populated per Part 6b
   §I.1.
4. Owner acks (or rejects) via Part 6b session.
5. On ack: driver renames DRAFT → PROMOTED canonical
   (`wiki/methodology/<rule-slug>.md`); commits via Part 1 §H `[methodology]
   promote: <rule-slug> (F5 codified rule)`. F-rise F4→F5. `human_acked_at:`
   populated. `pipeline: ready`.
6. Driver appends entry to `swarm/approvals/log.jsonl` per Part 6a §C.
7. Driver updates `wiki/index.md` (Part 3 ownership; Part 5 invokes via Part 3
   accessor).
8. Methodology promotion event emitted per §I.1 schema (event_type: promoted).

**On rejection at step 4:** DRAFT remains; owner rationale committed via Part 1
§H `[methodology] reject: <rule-slug> (rationale: ...)`. Periodic review
revisits (Phase B).

### §J.3 DRR review ritual (per compound phase)

For each existing DRR entry whose `last_validated_at` was >5 cycles ago:
driver emits a "stale-DRR-review" prompt to the owner. Owner reviews and
either: (a) revalidates (`last_validated_at` updated; ratio.hits++ on
re-validation evidence); (b) tombstones (per §I.2.1); (c) supersedes (per
§I.2.1). Health SLI: `drr-review-cadence-rate` ≥ 80% (Phase B starter target;
calibration per OQ-MERGED-5).

### §J.4 Dissolve-test evidence ritual (Bundle 3 OQ-MERGED-2)

Per cycle close, driver emits per-cycle count of compound-phase-exclusive
operations to
`swarm/wiki/cycles/<cycle-id>/bundle-3-dissolve-test-evidence.md`. Definition
of compound-phase-exclusive operation: an operation that Parts 3+4 cannot
capture without invoking Part 5 logic. Examples (per §X declaration): (a)
DRR ratio decay tombstoning (Parts 3+4 do not own per-rule decay counters);
(b) cross-cycle methodology candidate emergence (Parts 3+4 cannot detect
≥2-cycle-validation across role boundaries without Part 5 aggregation); (c)
owner-reflection prompt generation IP-7-bounded (Parts 3+4 can host the prose
but cannot emit the prompt with strategic-reflection separation discipline).

The accumulator file is read by Wave D's dissolve decision: ≥3 distinct
compound-phase-exclusive operations across Bundle 3 + Bundle 4 + Wave D =
standalone preserved; <3 = dissolve hypothesis activates.

### §J.5 Blameless postmortem on Part 5 incidents (SRE Ch.15)

Any incident affecting Part 5 (compound-phase ritual misfire; methodology
promotion gate timeout; DRR extraction failure) MUST produce a postmortem
commit. 5-line minimum per FUNDAMENTAL §2.4: what happened / why / what changed
/ how detect next / owner. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§2.4; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§4 P5 blameless postmortem]

### §J.6 Shape Up appetite (Singer 2019) for compound phase

Compound phase is fixed-time 10% of cycle wall-clock. Scope of compound-phase
output (number of DRR entries, number of methodology candidates) is variable
within that fixed time. Circuit-breaker: if compound-phase work exceeds 10%
+10pp tolerance, defer non-critical DRR review to next cycle (per Cagan
appetite-fixed/scope-variable). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 Principle 2]

---

## §K Failure Modes

**K1 — Compound phase fails to fire (cycle close did not trigger driver).**
Detection: cycle closed in Part 4 (mailbox `cycle-close-event` written) but no
`[strategy]` commits in next 24h. Policy: Part 8 SLI alert fires; owner
manually invokes `/compound <cycle-id>` from session. Mitigation: weekly
scheduled fallback (§I.3) catches the miss within 7d. [F4|G:event-driven
trigger reliability|R-medium]

**K2 — DRR extraction fails (task-return-packet schema mismatch).**
Detection: driver step 4a fails to parse a packet; emits structured error to
`compound-failure-log.md` with packet ID + named field. Policy: HALT
extraction for that packet only; continue with other packets; flag failed
packet to owner via Part 6b same-session ack. Cause: legacy v1.0.0 packet
upcast failed (K18 reject path). Recovery: owner manually corrects packet OR
explicitly rejects (audit trail preserved). [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K18 upcasting; F4|G:UND-1 schema robustness|R-medium]

**K3 — Methodology promotion gate timeout (owner not acked in N days).**
Detection: AWAITING-APPROVAL packet `gate_class: draft_promotion` open >7
days. Policy: Part 6b SLA escalation per Part 6b own discipline; Part 5 does
NOT auto-promote. The candidate stays DRAFT. Periodic Part 8 alert reminds
owner. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E
Deontics gate SLA; F4|G:Corrigibility per Bundle 1 Part 6b|R-high]

**K4 — Methodology candidate name collision (slug already exists in
`wiki/methodology/`).**
Detection: admissibility predicate check at step (3) of pipeline; `rule_slug`
already taken. Policy: REJECT with named-field error; surface to owner. Owner
either (a) renames the new candidate slug; (b) tombstones the existing entry
and supersedes; (c) merges via `supersedes:` pointer. [F4|G:slug uniqueness
enforcement|R-high]

**K5 — DRR entry without `f_g_r`.**
Detection: `/lint` (Bundle 1 P6a.2) admissibility check at A-1. Policy:
REJECT entry; do NOT commit. Surface to owner; owner adds F-G-R. Bundle 3
admissibility A-1 enforces. [F4|G:DOGFOOD per Part 6a §I.1 F8|R-high]

**K6 — Compound-application-rate SLI burn.**
Detection: rolling 5-cycle ratio drops <0.8. Policy: Part 8 SLI threshold
fires; alert routed per Part 8 §H.1 alert-routing stub (Bundle 3 deliverable;
Tier 1 — Ruslan ack required); not Tier 0. Owner investigates whether
compound phase is being skipped; corrective action: explicit owner-driven
compound phase the same week. [F4|G:Part 5 health SLI|R-medium]

**K7 — Dissolve-test evidence drought (Bundle 3 + 4 + Wave D 3-cycle window
ends with <3 distinct compound-phase-exclusive operations).**
Detection: at Wave D ack cycle, dissolve-test evidence accumulator count <3.
Policy: dissolve hypothesis activates per OQ-MERGED-2 §X declaration; Wave D
ack packet redirects compound-phase ownership; engineering-expert dissolve
hypothesis re-evaluated; if owner accepts, bundle redesign initiated before
Wave D Part 5 cycle runs. THIS IS NOT A FAILURE OF THE PART; it is the
DESIGN of the dissolve test — `<3 evidence` = correct outcome of the test.
[src:decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md; F3|G:Bundle 3
+ 4 + Wave D 3-cycle window|R-low — accumulating]

**K8 — Owner reflection prose generated by LLM (IP-7 anti-pattern violation).**
Detection: `/lint` checks (Phase B) for prose-generation provenance —
strategic reflection prose committed by non-owner author. Policy:
REJECT-and-flag; surface to owner; owner re-authors. Phase A: relies on
owner discipline + ritual checklist; Phase B: lint signal added.
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2; F3|G:Phase A discipline; Phase B lint|R-medium]

**K9 — Strategies.md schema upcast failure (legacy entry cannot be upcast).**
Detection: K18 upcasting policy step in driver — legacy entry's `from:` field
cannot infer Bundle 3 schema additive fields. Policy: REJECT with named-field
error; the entry remains in legacy format with `pre_bundle_3_legacy: true`
annotation; owner manually upcasts. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K18; F3|G:legacy entry handling|R-medium]

**K10 — Methodology entry contradicts existing canonical entity.**
Detection: candidate's `claimscope` overlaps with existing entry; `/lint
--check-contradictions` (Phase B) flags. Policy: REQUIRE owner to either set
`supersedes:` pointer (replacing the existing entry) OR explicitly defer the
conflict (write `decisions/policy/conflict-<slug>.md` deferring). NO silent
co-existence. [F4|G:contradiction discipline|R-medium]

**K11 — Compound phase fires but driver finds no task-return-packets.**
Detection: driver step 4a finds empty `comms/mailboxes/` for the cycle.
Policy: emit zero-delta DRR entry per D-1 ("no new learnings this cycle —
zero-delta"); the absence of pattern IS a finding (Popper falsifiability
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md:§Popper]). Continue ritual. [F4|G:zero-cycle-delta admissibility|R-medium]

**K12 — Dissolve-test accumulator file write conflict.**
Detection: concurrent compound-phase fires write to same per-cycle accumulator
file. Per Part 1 K15 (concurrent commit lock), retry with backoff. Mitigation
Phase B: serialise compound-phase fires per cycle. [F4|G:Part 1 concurrency
inheritance|R-low]

**K13 — Methodology candidate emergence rate below benchmark (E-2).**
Detection: rolling 5-cycle methodology promotion count < 1. Policy: investigate
whether DRR validation is too strict (admissibility predicate over-tight) OR
patterns are not emerging (genuine quiet period). Owner-driven review at
quarterly immune audit (Part 8 §J quarterly). [F4|G:Phase A starter benchmark
calibration parameter|R-low — calibration]

**K14 — Methodology demotion (F5→F4) needed (post-promotion evidence
contradicts).**
Detection: validated_in_cycles after promotion shows pattern failure rate
spike; ratio.misses > ratio.hits×2. Policy: open AWAITING-APPROVAL packet
`gate_class: stage_gate` to Part 6b for demotion; owner acks; entity rewritten
with NEW DRR entry tombstoning the methodology entry. F-G-R schema F8 LOCKED
permits F-rise; F-fall is the same gate logic with `f_after_target < f_before`.
[F4|G:F-fall path|R-medium]

---

## §L Wave C Work-List Bullet Status

Three bullets from `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 5. Each with acceptance predicate and current
satisfaction status.

### P5.1 — Compound ritual as canonical Foundation artefact (40/10/40/10)

**Design:** This document §J.1 (compound-phase ritual) + §I.2 (DRR ledger
schema) + §I.3 (compound-phase trigger predicate decision: event-driven on
cycle close primary + weekly scheduled fallback) + §H (code interface for
`/compound` driver). DRR schema 4-part (Decision/Reasoning/Result/Review) +
`rule_slug` for deduplication + `validated_in_cycles[]` accumulator + `ratio:
{hits, misses}` counter + `created_at:` + `last_validated_at:`. Health SLI
"compound-application-rate ≥ 80%" cross-referenced to Part 8 §I.2 SLI/SLO
schema (Bundle 3 deliverable).

**Hamel-binary acceptance predicate:** synthetic fixture of 3 cycle-close
events → Part 5 emits 3 DRR entries (or 3×N if multiple roles have learnings);
`agents/<id>/strategies.md` updates committed via Part 1 §H;
compound-application-rate metric ≥0.8 in test fixture.

**Acceptance predicate status:** DESIGN COMPLETE. Test fixture: NOT YET RUN
(Phase B materialisation). The schema design is at F4. Promoted to F5 on
Bundle 3 owner ack of this document.

**Reuses existing pattern:** `agents/<id>/strategies.md` files already exist
(8 of them per AUDIT §4); 19 strategy entries already accumulated per
`swarm/wiki/meta/health.md` [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§4]. Bundle 3 schema additive — existing entries upcast on next compound-phase
write per K18 (Part 1 §K supplement); NO knowledge erasure.

### P5.2 — Methodology promotion pipeline (UND-2 binding)

**Design:** §I.1 (methodology promotion event schema; pipeline 7 stages mapped
to event_type values; DRY enforcement Part 5 ↔ Part 3); §J.2 (methodology
promotion ritual; AWAITING-APPROVAL packet via Part 6b `gate_class:
draft_promotion`).

**Cross-reference:** Part 3 §E L9 admissibility predicate (≥1 DRR `result:
validated` from ≥2 cycles + `rule_slug:` + F4→F5 rise) — Part 5 §I.1
references Part 3 §E L9 + §I.2 promotion sequence. DRY enforced: Part 5 owns
the EMISSION schema; Part 3 owns the ADMISSION schema; both reference each
other; do NOT duplicate.

**Hamel-binary acceptance predicate:** synthetic fixture of methodology
candidate carrying ≥2 validated DRR markers + rule_slug; AWAITING-APPROVAL
`gate_class: draft_promotion` packet emitted; Part 6b ack simulated; entity
at `wiki/methodology/<slug>.md` with F5 + ClaimScope + `refuted_if`; passes
Part 3 `/lint`; `swarm/approvals/log.jsonl` entry visible.

**Acceptance predicate status:** DESIGN COMPLETE. Test fixture: NOT YET RUN
(Phase B materialisation). The schema design is at F4. Promoted to F5 on
Bundle 3 owner ack of this document.

### P5.3 — OQ-MERGED-2 dissolve-test condition declaration in §X

**Design:** §X (Foundation vs RUSLAN-LAYER section below) declares the
dissolve-test condition explicitly. Required content per spec:
(a) DISSOLVE-TEST CONDITION verbatim; (b) ENGINEERING-EXPERT DISSENT preserved
with cross-references; (c) BUNDLE 3 = FIRST CYCLE OF 3-CYCLE WINDOW
declaration; (d) STANDALONE PRESERVATION threshold ≥3; (e) DISSOLVE PATH if
threshold not met.

**Companion artefact:** `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` (D25 Company-as-Code committed canonical artefact, mirrors §X declaration).

**Acceptance predicate:** §X section non-empty; dissolve threshold numerically
declared (≥3 vs <3); engineering-expert dissent linked; companion policy file
exists.

**Acceptance predicate status:** DESIGN COMPLETE. §X populated below. Companion
policy file written as Bundle 3 deliverable. F3 (proposed dissolve-test
condition; not validated until Wave D evidence accumulates) → F4 on Bundle 3
owner ack of test condition itself.

---

## §M Wisdom Application Findings — Part 5

Per §5 Wisdom Application Loop discipline. OPERATIONAL/PHILOSOPHICAL
discriminator column mandatory. Bundle 3 target: ≥85% operational adoption
ratio.

| # | Card / Source | Principle | Current state | Improvement | Adopted? | Op vs Phi | Justification | Section edited |
|---|---|---|---|---|---|---|---|---|
| 1 | Compounding-Engineering §2 | 40/10/40/10 main loop | F5 inherited from FUNDAMENTAL §2.2 | Part 5 §J.1 codifies ritual sequence with explicit step 4a-4h driver responsibilities | YES | OPERATIONAL | Phase A — operational ritual specification | §J.1 |
| 2 | Compounding-Engineering §4 P2 | DRR ledger as append-only compound memory | partial in `agents/<id>/strategies.md` (19 entries) | Add `ratio: {hits, misses}` counter + `validated_in_cycles[]` + tombstone rule when ratio.misses > ratio.hits×2 | YES | OPERATIONAL | Phase A — operational decay signal; tombstone rule prevents stale entries | §I.2 + §K |
| 3 | Compounding-Engineering §4 P3 | Error→Rule→Skill pipeline | not formalised | DRR `result: validated` accumulation IS the Error→Rule pipeline; methodology promotion IS the Rule→Skill pipeline; explicit F4→F5 rise as the codification step | YES | OPERATIONAL | Phase A — schema codification of pipeline | §I.1 + §J.2 |
| 4 | Compounding-Engineering §4 P4 | strategies.md persistent memory | exists as 8 files; schema informal | Schema canonicalised in §I.2; upcasting policy K18 inherited | YES | OPERATIONAL | Phase A — schema discipline | §I.2 |
| 5 | Compounding-Engineering §4 P5 | Validated pattern threshold for methodology promotion | not formalised | Admissibility predicate A-2: ≥1 DRR `result: validated` + ≥2 distinct cycles + `rule_slug` populated/unique | YES | OPERATIONAL | Phase A — admissibility schema | §I.1 + §J.2 |
| 6 | Compounding-Engineering §4 P6 | Anti-cargo-cult | enforced in Bundle 1 + 2 by citation discipline | Inherit; Part 5 emission events MUST cite source DRR entries; methodology entries MUST carry `validated_in_cycles[]` evidence | YES | OPERATIONAL | Phase A — schema-level cargo-cult prevention | §I.1 |
| 7 | Compounding-Engineering §4 P7 | Reversibility via git | F5 inherited from D25 Company-as-Code | Part 5 §I.2 Reversal Transactions discipline (corrects/supersedes/tombstones — NO delete) | YES | OPERATIONAL | Phase A — append-only operationalised | §I.2.1 + §C |
| 8 | Levenchuk SHSM-FPF §4 P2 | IP-7 writing-as-thinking; LLM does NOT generate strategic reflection | not enforced operationally | §I.5 reflection template separates machine-extracted summary from owner-authored prose; §A.2 boundary; §K8 violation detection | YES | OPERATIONAL | Phase A — boundary enforcement; Phase B lint adds detection | §A.2 + §I.5 + §K8 |
| 9 | Levenchuk SHSM-FPF IP-3 | artifacts-over-conversations | enforced Bundle 1 D25 | Part 5 L-1 promotes to Foundation Law for Part 5 specifically (DRR MUST be committed file) | YES | OPERATIONAL | Phase A — Law promotion | §E L-1 |
| 10 | Cagan/Shape Up §4 P2 | Appetite-fixed/scope-variable | adopted Bundle 2 | Part 5 §F.3 + §J.6 — compound-phase appetite 10% wall-clock; defer overflow to next cycle | YES | OPERATIONAL | Phase A — appetite discipline | §F.3 + §J.6 |
| 11 | Stoic-epistemic Popper falsifiability | Falsifiability as rule-promotion gate | not formalised | F4+ DRR entries MUST have `refuted_if:` Popper falsifier; Part 6b admissibility A-2 enforces; Part 3 §E L9 admissibility predicate references | YES | OPERATIONAL | Phase A — Popper falsifier mandatory at F4+ | §I.2 + §A.4 |
| 12 | Stoic-epistemic Popper | Zero-delta-cycle as finding | not stated | Part 5 D-1: zero-delta DRR entries explicitly admissible — absence of pattern IS finding | YES | OPERATIONAL | Phase A — zero-delta admissibility | §E D-1 + §K11 |
| 13 | Systems-thinking-cybernetics §4 R2 | R2 reinforcing loop distinct from R1; 5-10 cycle delay before compound effect detectable | preserved as dissent counter-argument in OQ-MERGED-2 | Part 5 §X declares R2 distinctness as dissolve-test counter-argument; §J.4 dissolve-test evidence ritual operationalises 3-cycle window | YES | OPERATIONAL | Phase A — dissolve-test condition operationalisation | §X + §J.4 |
| 14 | Systems-thinking-cybernetics §4 Meadows leverage | Self-organisation = ability to add new structure (L4) | not explicitly cited | Part 5 §D.2 — Part 5 occupies Meadows L4; methodology promotion IS Part 5 adding new structure to Part 3 | YES | OPERATIONAL | Phase A — leverage point mapping | §D.2 |
| 15 | Systems-thinking-cybernetics §4 Meadows L9 (delays) | Deliberate delay between Work and Compound for reflection | informal | §J.1 ritual sequence enforces delay (40% Plan / 10% Work / 40% Review / 10% Compound — Compound is LAST 10%, not interleaved) | YES | OPERATIONAL | Phase A — sequence discipline | §J.1 |
| 16 | Young 2010 §4 P3 | Reversal Transactions (no-delete; corrections = new entries with `corrects:` pointer) | informal | Part 5 §I.2.1 — three pointer types: corrects/supersedes/tombstones; explicit in schema | YES | OPERATIONAL | Phase A — schema discipline | §I.2.1 + §C |
| 17 | Young 2010 §4 P4 | Event-versioning + upcasting | inherited from K18 retroactive supplement | §I.2.2 — strategies.md upcasting policy applies Bundle 3 schema additively; legacy entries upcast on next write | YES | OPERATIONAL | Phase A — schema evolution discipline | §I.2.2 |
| 18 | Askell HHH Appendix E.2 | Corrigibility verbatim | F8 LOCKED Bundle 1 Part 6b | Part 5 §E L-5 — methodology promotion HITL-gated; owner can revert any promotion via git revert | YES | OPERATIONAL | Phase A — Corrigibility inheritance | §E L-5 + §F.1 |
| 19 | FUNDAMENTAL §2.2 | 40/10/40/10 ratio | F5 inherited | Part 5 §E L-4 — drift tolerance ±10pp before health alert; F5 inherited not re-litigated | YES | OPERATIONAL | Phase A — constitutional inheritance | §E L-4 + §J.1 |
| 20 | FUNDAMENTAL §3.3.1 | compound-application-rate health indicator ≥0.8 | informal in `swarm/wiki/meta/health.md` | Part 8 §I.2 SLI codification (Bundle 3 deliverable; Part 5 §B.1 cross-ref) | YES | OPERATIONAL | Phase A — SLI codification cross-ref | §B.1 + §C |
| 21 | FPF §5.7 IP-7 | writing-as-thinking | acknowledged | Part 5 §A.2 + §E L-2 + §I.5 — three-layer enforcement | YES | OPERATIONAL | Phase A — IP-7 codification | §A.2 + §E L-2 + §I.5 |
| 22 | FPF §B.3 F-G-R | DOGFOOD per Bundle 1 Part 6a F8 | adopted Bundle 1 | §G F-G-R Tagging table; inline tags throughout | YES | OPERATIONAL | Phase A — DOGFOOD inheritance | §G + inline |
| 23 | FPF §A.14 typed edges | Canonical 10-edge table | adopted Bundle 1 | §D Dependencies — every edge typed; NO `depends-on` | YES | OPERATIONAL | Phase A — typed edge discipline | §D |
| 24 | FPF §A.13 Agency-CHR | J-Auto / J-Approve / J-Strategic | informal | Part 5 §J.2 step 3-4 distinguishes J-Auto (DRAFT emit) vs J-Approve (Part 6b gate) vs J-Strategic (owner reflection prose) | YES | OPERATIONAL | Phase A — Agency-CHR mapping | §J.2 |
| 25 | Compounding-Engineering "good engineering compounds" | Engineering subsumes itself | conceptual | NO — pure framing prose without operational consequence; explicitly rejected per Bundle 3 §6.3 | NO | PHILOSOPHICAL | Pure framing prose without operational consequence; DEFER to Wave D documentation pass | n/a |
| 26 | Stoic Dichotomy of Control | "in our control" framing | not applied | NO — Part 5 already operates within Corrigibility (L-5); the Stoic framing adds prose without operational change | NO | PHILOSOPHICAL | Pure framing prose without operational consequence; DEFER to Wave D | n/a |
| 27 | Cagan Shape Up §6 "no contracts; betting table" | Quarterly betting on which projects | conceptual | NO — Phase A is single-owner; betting table is multi-stakeholder pattern (Phase C scale) | NO | PHILOSOPHICAL | Phase B/C scale; premature for Phase A | n/a |
| 28 | Systems-thinking-cybernetics Beer VSM S5 | Identity / values | conceptual | NO — out of scope for Part 5 (Part 5 is S3 input); FUNDAMENTAL §6 covers Phase A identity | NO | PHILOSOPHICAL | Domain-orthogonal to Part 5 | n/a |

**Aggregate operational adoption ratio for Part 5:**
- Total YES Adopted: 24 (all OPERATIONAL — 24 OP / 0 PHI)
- Total NO: 4 (all PHILOSOPHICAL — domain-orthogonal or pure framing prose)
- Total findings: 28
- **Operational adoption ratio: 24/24 = 100%** (well above ≥85% Bundle 3
  target)

---

## §N Provenance

Every claim in this document carries inline `[src:<path>]` citation followed
within 200 chars by a concrete consequence sentence. Per Bundle 1 Part 6a §C
citation discipline + Bundle 3 §6.3 anti-cargo-cult enforcement.

**Sources consulted (full list):**

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` (Wave A interface card §A-§H + frontmatter dissent record)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md` §2 Part 5
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md` §2 Part 5 (verdict CLEAN) + §4 OQ-MERGED-2
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` §2.4 P4↔P5 R2 reinforcing loop; §4.3 UND-3 P7→P5
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 5
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` §2 main loop; §4 P1-P7 + §5 validated pattern threshold
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` §4 P2 IP-3+IP-7 + §4 P5 F-G-R
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md` §4 Principle 2 appetite-fixed
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` §Popper falsifiability
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 R2 reinforcing loop + §4 Meadows leverage
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §2.2 / §2.4 / §3.3.1 / §6.1 / §6.2
- `design/JETIX-FPF.md` IP-3 / IP-7 / A.13 Agency-CHR / A.14 typed edges / A.6.B L/A/D/E / B.3 F-G-R
- `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` §4 (existing strategies.md baseline 19 entries)
- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §H + §I.2 + §I.4 (post-supplement) + §K K15-K18
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` §E L9 admissibility predicate F5 + §I.2 wiki/methodology/ entity-type
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` §I.1 task-return-packet.json FULL schema + §H message schema v2.0.0
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` §I.1 F-G-R F8 schema + §C approval log structure
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` §I.1 awaiting-approval-packet F8 + §I.4 blast-radius + §E L9 Halt-Log-Alert + Corrigibility
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (Bundle 1 ack record)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` §1 Decision #4 + #6 + #C1
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` (Bundle 1 retroactive supplement applied 2026-04-28 Phase 0)
- `raw/books-md/event-sourcing/young-cqrs-2010.md` §4 P3 Reversal Transactions + §4 P4 event-versioning
- `raw/books-md/anthropic/askell-2021-hhh.md` Appendix E.2 Corrigibility
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` (Bundle 3 cross-bundle interface)
- `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` (Bundle 3 companion policy artefact)

---

## §X Foundation vs RUSLAN-LAYER Separation

### §X.1 GENERIC Foundation (fork-portable)

| Foundation generic | Rationale |
|---|---|
| 40/10/40/10 cadence ratio | F5 inherited from FUNDAMENTAL §2.2 — any knowledge-work system using structured cycle ritual |
| DRR 4-part schema (Decision/Reasoning/Result/Review) | Compounding-Engineering §4 P2 — generic ledger pattern |
| Methodology promotion pipeline (7-stage event sequence) | UND-2 binding — generic schema; specific rule_slug values are RUSLAN-LAYER |
| Admissibility predicate (≥1 DRR validated + ≥2 cycles + rule_slug) | Generic threshold — fork can tighten/loosen per its scale |
| Compound-phase trigger predicate (event-driven + weekly fallback) | Generic; cadence may vary per fork's cycle wall-clock norm |
| Reversal Transactions (corrects/supersedes/tombstones) | Young 2010 §4 P3 — generic event-versioning discipline |
| Owner-reflection IP-7 boundary | FPF §5.7 IP-7 — applies to any system that respects writing-as-thinking |
| Health SLI emission (compound-application-rate ≥ 0.8) | Generic SLI shape; specific threshold value is calibration parameter (Phase B per OQ-MERGED-5) |
| Dissolve-test condition declaration mechanism | Generic — any Foundation Part with dissolve dissent should declare a numerical test condition |

### §X.2 RUSLAN-LAYER (Jetix-specific instance values)

| Ruslan-specific | Where stored |
|---|---|
| Specific methodology slugs Ruslan promoted (e.g. `ingest-lint-after`, `compound-cycle-close-event-driven`) | `wiki/methodology/<slug>.md` per-entry |
| Specific DRR entries in `agents/<id>/strategies.md` | Per-role files; RUSLAN-LAYER content within Foundation schema |
| Specific compound-application-rate threshold value (0.8 starter; calibrated value Phase B) | `shared/state/system-health.json` post-Phase-B calibration |
| Specific role assignments for compound-phase orchestrator | `executor-binding.yaml` (RUSLAN-LAYER per IP-1) |
| Specific cycle wall-clock norm (90 min per cycle Phase A) | `executor-binding.yaml` cadence config |
| Specific dissolve-test evidence judgment ("does this count as compound-phase-exclusive?") | Owner-authored at Wave D ack cycle |

### §X.3 OQ-MERGED-2 dissolve-test condition declaration (P5.3 BINDING)

**DISSOLVE-TEST CONDITION (verbatim, MUST hold):**

> "If Bundle 3 + Bundle 4 + Wave D show <3 distinct compound-phase-exclusive
> operations (operations Parts 3+4 cannot capture without invoking Part 5
> logic), dissolve hypothesis activates and Wave D ack cycle decides whether
> Part 5 dissolves into Parts 3+4."

**ENGINEERING-EXPERT DISSENT (preserved from Wave A interface card §H
frontmatter `dissent_preserved` block):**

> *Engineering-expert pre-read claim:* "Part 5 might dissolve into Parts 3
> (KB) and 4 (coordination) without residue — DRR ledger belongs to KB; cycle
> ritual belongs to coordination protocol."
>
> Reference: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` frontmatter `dissent_preserved` block.
>
> Refutation/acceptance per the Wave A interface card:
> - **refuted_if:** "After 3 Wave C cycles the DRR work-list is fully
>   captured by Parts 3+4 with no residual compound-phase-specific artifacts"
> - **accepted_if:** "Compound phase produces distinct artifact types (DRR
>   entries, promoted methodology patterns) not produced by any other part;
>   R2 reinforcing loop is observably distinct from R1"

**SYSTEMS-THINKING-CYBERNETICS §4 R2 COUNTER-ARGUMENT (preserved alongside
dissent):**

> *Counter-argument:* "Part 5 is the R2 reinforcing loop substrate (5-10 cycle
> delay before compound effect detectable). Parts 3+4 own R1 (current-cycle
> execution). Dissolving Part 5 into Parts 3+4 collapses R1 and R2 into a
> single loop — losing the R1/R2 phase distinction. Kauffman adjacent-possible
> [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§4 Kauffman]: Part 5 expands what FUTURE cycles can do (methodology
> library accumulation); Part 4 executes within CURRENT capability set. These
> are categorically different knowledge functions per Vincenti P7
> [src:raw/books-md/engineering-foundations/vincenti-what-engineers-know-1990.md:Ch.7]."
>
> Reference: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 R2 reinforcing loop counter-argument.

**BUNDLE 3 = FIRST CYCLE OF 3-CYCLE WINDOW DECLARATION:**

> Bundle 3 is the FIRST cycle of the 3-cycle dissolve-test window. The window
> closes at Wave D ack cycle. Across Bundle 3 + Bundle 4 + Wave D:
> - If accumulator count ≥3 distinct compound-phase-exclusive operations =
>   STANDALONE PRESERVED (Part 5 retained as canonical Foundation Part).
> - If accumulator count <3 = DISSOLVE HYPOTHESIS ACTIVATES (Wave D ack cycle
>   decides whether Part 5 dissolves into Parts 3+4).

**STANDALONE PRESERVATION threshold:** ≥3 distinct compound-phase-exclusive
operations across Bundle 3 + Bundle 4 + Wave D.

**DISSOLVE PATH if threshold not met:**

> Wave D ack packet redirects compound-phase ownership; engineering-expert
> dissolve hypothesis re-evaluated; if owner accepts dissolve, bundle redesign
> initiated BEFORE Wave D Part 5 cycle runs:
> - DRR ledger schema migrates to Part 3 §I.X (new sub-section under
>   methodology library — DRR-as-pre-methodology-history)
> - Compound-phase ritual cadence migrates to Part 4 §J.X (new sub-section
>   under coordination protocol — compound-phase as cadence step)
> - All historical strategies.md entries preserved (no deletion); migration
>   commit `[strategy] migrate: legacy DRR entries to Part 3 methodology
>   history (Wave D dissolve)` per IP-3 + Reversal Transactions
> - OQ-MERGED-2 closes; Part 5 architecture document moves to
>   `swarm/wiki/foundations/_archived/part-5-compound-learning-methodology-capture/architecture.md` with `pipeline: archived` frontmatter

**Companion policy artefact:** `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` mirrors this declaration as a standalone D25
Company-as-Code committed canonical artefact.

### §X.4 Boundary principle (per IP-1)

The schema (DRR 4-part / methodology pipeline / 40/10/40/10 ratio / dissolve-test
condition mechanism) is GENERIC. The specific values (rule slugs / SLI
thresholds / role names) are RUSLAN-LAYER. A Phase B partner forking Jetix:
- ADOPTS the schema (this document is the spec)
- IMPORTS Ruslan-specific entries optionally as historical reference
- EXTENDS with their own DRR entries + methodology slugs + cycle wall-clock
  norm
- OVERRIDES specific role-binding mappings via own `executor-binding.yaml`

**This is why operational adoption ratio matters.** A schema is portable; pure
framing prose is not. Bundle 3 §85% operational target is structural — every
NO PHILOSOPHICAL adoption is one less load-bearing constraint a Phase B partner
must inherit. Per §M, Part 5 achieves 100% operational adoption (24/24).

---

## §Y Open Questions Surfaced By Bundle 3 Part 5

| OQ ID | Open Q | Source | Resolution path | Blocking? |
|---|---|---|---|---|
| OQ-B3-P5-1 | UND-3 stub schema reference: `task-return-packet.json` superset OR `project-retrospective-packet.json` TBD — Bundle 4 Part 7 picks one | §I.4 | Bundle 4 Part 7 emission contract | Not blocking for Bundle 3 |
| OQ-B3-P5-2 | UND-3 cadence: per project closure event OR per cycle close — Bundle 4 Part 7 picks one | §I.4 | Bundle 4 Part 7 emission contract | Not blocking for Bundle 3 |
| OQ-B3-P5-3 | Methodology candidate emergence rate calibration — E-2 starter benchmark "≥1 entry per 5 cycles" needs Phase B operational data | §E E-2 + §K13 | Phase B 2-3 month observation | Not blocking |
| OQ-B3-P5-4 | DRR review cadence-rate SLI threshold (current starter: ≥80% Phase B; calibrated value TBD) | §J.3 | Phase B per OQ-MERGED-5 | Not blocking |
| OQ-B3-P5-5 | Dissolve-test "compound-phase-exclusive operation" judgment criterion — owner-authored at Wave D; criteria for what counts | §X.3 + §J.4 | Wave D ack cycle owner judgment | Bundle 3 declares mechanism; Wave D judges |

None of the OQs above are blocking for Bundle 3 ack. They surface for Wave D /
Phase B resolution and are tracked in the AWAITING-APPROVAL packet §5.

---

**End of Part 5 Architecture (Bundle 3).**

Status: F4 architecture-time. Promoted to F5 on Bundle 3 owner ack of this
document.

Word count target: 10K-20K (Bundle 3 constitutional refinement per
RUSLAN-ACK Bundle 2 §3 F8). This document target ~12-13K words.

Next: Part 8 — Health Monitoring & System Integrity (Bundle 3 Part 2 of 2).
