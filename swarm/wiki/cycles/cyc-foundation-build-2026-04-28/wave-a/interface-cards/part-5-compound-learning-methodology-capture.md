---
title: "Interface Card — Part 5: Compound Learning & Methodology Capture"
part_number: 5
part_slug: compound-learning-methodology-capture
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
critic_status: CLEAN
originating_experts: [systems-expert, investor-expert]
FUNDAMENTAL_UC: [C.1, C.2, C.3, F.1, F.2]
FPF_anchors: [IP-3, IP-7, P-10, A.13]
D_lock_anchors: [FUNDAMENTAL §2.2, FUNDAMENTAL §2.4, FUNDAMENTAL §3.3.1]
U_classification: "Dual: DRR entries + methodology patterns = U.Episteme; cycle ritual enforcement = U.System"
F: F4
ClaimScope: "Holds for any knowledge-work system using a structured cycle ritual to convert execution experience into improved future execution; 40/10/40/10 ratio is FUNDAMENTAL §2.2 constitutional value, not Ruslan-specific"
R:
  refuted_if: "DRR entries stop appearing in strategies.md files across consecutive cycles; or methodology library sub-layer within Part 3 shows zero new entries across 5+ cycles (feedback loop stalled)"
  accepted_if: "Per-agent strategies.md files accumulate DRR entries at compound phase; methodology library sub-layer in Part 3 receives promoted patterns from compound phase; compound-application-rate health metric tracked"
dissent_preserved:
  source: "engineering-expert pre-read (Ambiguity 4 in candidate-parts-merged.md §2 Part 5)"
  claim: "Part 5 might dissolve into Parts 3 (KB) and 4 (coordination) without residue — DRR ledger belongs to KB; cycle ritual belongs to coordination protocol"
  F: F2
  ClaimScope: "Held by engineering-expert; contested by systems-expert and investor-expert"
  R:
    refuted_if: "After 3 Wave C cycles the DRR work-list is fully captured by Parts 3+4 with no residual compound-phase-specific artifacts"
    accepted_if: "Compound phase produces distinct artifact types (DRR entries, promoted methodology patterns) not produced by any other part; R2 reinforcing loop is observably distinct from R1"
  integrator_resolution: "Part 5 retained as standalone per A-1-critic-gate.md §4 OQ-MERGED-2. If dissolve condition fires after cycle-50 review, OQ-MERGED-2 dissolve path remains open."
sources:
  - "candidate-parts-merged.md §2 Part 5"
  - "A-1-critic-gate.md §2 Part 5 (verdict: CLEAN) + §4 OQ-MERGED-2"
  - "levenchuk-shsm-fpf.md §4 P2 (IP-3 writing-as-thinking), §4 P5 (F-G-R)"
  - "FUNDAMENTAL §2.2 (40/10/40/10), §2.4, §3.3.1"
  - "design/JETIX-FPF.md §5.7 IP-7, §5.3 IP-3, FPF P-10 Open-Ended Evolution"
  - "AUDIT-CURRENT-STATE-2026-04-27.md §4 (agents/*/strategies.md, swarm/wiki/meta/)"
---

# Interface Card — Part 5: Compound Learning & Methodology Capture

## A. Inputs

| Source | Data shape | Event trigger |
|---|---|---|
| Cycle execution outputs (from all parts) | Structured packets: `summary`, `proposed_writes[]`, `provenance[]`, `confidence`, `escalations[]` | Compound phase trigger (10% of cycle wall-clock; FUNDAMENTAL §2.2) |
| Owner strategic reflection (U.Episteme) | Authored by owner per IP-7: written strategic observation, framed retrospectively | Owner-authored at compound phase; agents contribute structured extractions only [FPF §5.7 IP-7; levenchuk-shsm-fpf.md §4 P2] |
| Health signals from Part 8 | Anomaly reports, SLI drift, agent-drift-detection outputs | Periodic health event; feeds into compound-phase retrospective |
| Prior strategies.md entries | Historical DRR entries per role — accumulated learning baseline | Read at compound phase start; baseline for delta computation |

## B. Outputs

| Consumer | Data shape | Event published |
|---|---|---|
| Per-role strategies.md files (U.Episteme) | 4-part DRR entries: Decision / Reasoning / Result / Review; `ratio: {hits, misses}` counters per rule [candidate-parts-merged.md §2 Part 5 FPF anchor] | `drr-entry-committed-event` via Part 1 |
| Part 3 (Knowledge Base & Methodology Library) | Promoted methodology patterns: templates, workflow schemas, validated heuristics — committed wiki entries with typed edges | `methodology-entry-promoted-event` |
| Part 1 (System State Persistence) | All compound outputs committed as git artifacts [FPF §5.3 IP-3] | `artifact-committed-event` |
| Part 8 (Health Monitoring) | Compound-application-rate metric update; strategies.md growth delta [FUNDAMENTAL §3.3.1 health indicator] | `health-metric-updated-event` |

## C. Side-effects

- Writes to `agents/<role>/strategies.md` — append-only DRR entries; no in-place edits of prior entries [D25 append-only discipline]
- Promotes validated patterns to `wiki/` methodology library sub-layer via Part 3 interface — each promotion is a git commit through Part 1 [IP-3]
- Updates `swarm/wiki/meta/health.md` compound-application-rate counter
- Does NOT write to any canonical decisions/ files — that is Part 6's promotion gate

## D. Dependencies (typed per FPF A.14)

| Edge | Type | Rationale |
|---|---|---|
| Part 5 → Part 3 | `creates` | Compound outputs create methodology library entries in the KB [A-1-critic-gate.md §2 Part 5 A.14 note] |
| Part 5 → Part 1 | `creates` | DRR entries and all compound artifacts are committed through git substrate [FPF §5.3 IP-3] |
| Part 5 → Part 4 | `methodologically-uses` | Compound phase draws on the coordination protocol cycle structure (40/10/40/10 cadence is enforced at Part 4 dispatch level; Part 5 produces the compound phase artifacts within that cadence) |
| Part 8 → Part 5 | `derives-from` | Health anomaly signals inform the retrospective lens at compound phase [candidate-parts-merged.md §2 Part 5 A.14 partial] |

## E. Boundary — L/A/D/E discipline [FPF §4.3 A.6.B]

**Laws (invariants that MUST hold):**
- DRR entries MUST be committed files in strategies.md — never chat-only reflections [FPF §5.3 IP-3; levenchuk-shsm-fpf.md §4 P2; candidate-parts-merged.md §2 Part 5].
- Strategic reflection MUST be owner-authored; agent extractions are structured inputs to owner authorship, not substitutes [FPF §5.7 IP-7; FUNDAMENTAL §6.2 agency-preservation].
- Agent strategies.md files update ONLY through explicit gated compound-phase review — no runtime mutation [FUNDAMENTAL §6.1 no-self-modify rule].
- 40/10/40/10 cadence ratio is FUNDAMENTAL §2.2 constitutional value — drift tolerance ±10pp before health alert fires [FUNDAMENTAL §3.3.1].

**Admissibility (acceptance criteria for inputs):**
- A DRR entry is accepted into strategies.md only if it carries all 4 parts (Decision / Reasoning / Result / Review) and a `rule_slug` for deduplication.
- A methodology pattern is accepted into Part 3 promotion queue only after ≥1 DRR "Result: validated" marker across ≥2 cycles (F-level uplift from F2→F3+).
- Owner reflection is accepted as compound output only when authored in writing (not dictated chat only); the writing IS the thinking [levenchuk-shsm-fpf.md §4 P2 anti-pattern warning: "Если и сам текст пишет LLM — исчезает мышление письмом"].

**Deontics (obligations of this part toward consumers):**
- Part 5 MUST surface one candidate strategies.md entry per role per cycle (even if the entry is "no new learnings this cycle — zero-delta DRR") so compound-application-rate remains measurable.
- Part 5 MUST preserve all dissenting DRR entries — competing interpretations of the same cycle event are retained, not averaged [A-1-critic-gate.md §4 OQ-MERGED-2 dissent record].
- Part 5 MUST route any methodology pattern that contradicts an existing Foundation document to Part 6 governance gate before promotion [Part 6 interface].

**Effects (measurable outcomes):**
- strategies.md entry count grows per cycle; ratio.hits accumulate over time [FUNDAMENTAL §3.3.1 compound-application-rate health indicator].
- Methodology library sub-layer in Part 3 gains ≥1 promoted pattern per 5 cycles (starter benchmark; calibrated in Wave C).
- F-level of validated DRR rules rises from F2 (single-cycle observation) toward F4-F5 (operational convention, multi-cycle validated) over compound history [FPF §4.2 B.3; levenchuk-shsm-fpf.md §4 P5].

## F. Anti-scope

- **Does NOT produce strategic decisions** — compound learning surfaces patterns for the owner's consideration; the owner decides what to change [FUNDAMENTAL §6.1; FUNDAMENTAL §6.2].
- **Does NOT own KB content management** — methodology promotion requests route through Part 3's ingest interface; Part 5 is the producer, Part 3 is the storage layer.
- **Does NOT own coordination protocol** — the 40/10/40/10 cadence enforcement mechanism lives in Part 4; Part 5 produces the compound-phase artifacts within that cadence.
- **Does NOT own health monitoring** — compound-application-rate is a health signal consumed by Part 8; Part 5 emits the metric, Part 8 owns the SLI/SLO threshold and alert logic.
- **Does NOT dissolve into Parts 3+4 without explicit OQ-MERGED-2 Ruslan ack** — dissent from engineering-expert preserved; dissolve path is held open contingent on cycle-50 evidence [A-1-critic-gate.md §4 OQ-MERGED-2].

## G. F-G-R tagging [FPF §4.2 B.3]

| Artifact | F | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| DRR entry (new, cycle 1 of rule) | F2 — single-cycle observation | Specific role + specific cycle context | R-low |
| DRR entry (validated, 3+ cycles) | F4 — operational convention | Role + system context; bridge needed for multi-agent systems with different coordination patterns | R-medium |
| DRR entry (tombstoned: ratio.misses > ratio.hits × 2) | F-tombstoned | No longer valid in current context | R-low; archived not deleted |
| Methodology pattern (promoted to Part 3) | F4→F5 on promotion (requires ≥2-cycle DRR validation) | Any system applying the same methodology; note bridge (F.9) for different domain contexts | R-medium to R-high |
| 40/10/40/10 cadence ratio | F5 — codified in FUNDAMENTAL §2.2 | Any knowledge-work system using structured cycle ritual | R-high (constitutional) |

## H. Originating expert + critic flags + dissent record

- **Originating experts:** Systems-expert (Part 5: Compound Learning & Self-Improvement Engine); investor-expert independently flagged as highest-compound asset after KB [candidate-parts-merged.md §2 Part 5].
- **A-1 critic verdict: CLEAN** [A-1-critic-gate.md §2 Part 5]. No required edits.
- **Dissent preserved (engineering-expert):** Engineering-expert proposed Part 5 dissolves into Parts 3+4. Integrator retained Part 5 standalone per OQ-MERGED-2 rationale (R2 reinforcing loop distinct from R1; Kauffman adjacent-possible: Part 5 expands what future cycles can do, Part 4 executes within current capability set; Vincenti P7: these are categorically different knowledge functions). Dissent is NOT averaged — it is held open as OQ-MERGED-2 for Ruslan ack, with dissolve condition explicitly stated above in §H frontmatter.
- **AUDIT existing artefacts to reuse:** `agents/*/strategies.md` (8 files — 19 strategy entries per health.md); `swarm/wiki/meta/health.md` (cycle counter, compound-application-rate); `swarm/wiki/meta/agent-improvements/`; `swarm/evals/` harness (seeded cycle 1, 3/20 cells) [AUDIT §4; candidate-parts-merged.md §2 Part 5 AUDIT mapping].
- **Wave C primary gap:** Methodology library sub-layer within Part 3 is not yet consistently populated from compound outputs. Wave C task: define promotion pipeline from strategies.md validated entries → wiki/methodology/ entries with typed edges and F-G-R frontmatter [candidate-parts-merged.md §2 Part 5 Cycles reuse note].
