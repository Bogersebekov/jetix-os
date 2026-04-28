---
title: "Foundation Part 9 — Owner Interaction Scaffold (Architecture)"
part_number: 9
part_slug: owner-interaction-scaffold
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
phase: Wave-C-Bundle-4-architecture
status: ruslan-acked-canonical
ruslan_ack_record: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md
ruslan_ack_date: 2026-04-28
predecessor_interface_card: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md
constitutional_baseline_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
constitutional_baseline_bundle_1_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
constitutional_baseline_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
constitutional_baseline_bundle_3: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
applies_c4_fix: "Wave A Part 9 §D used `PhaseOf Part 6` for governance gate dependency; Bundle 4 applies C4 nomenclature fix verbatim (`methodologically-uses Part 6`); brigadier autocheck rejects PhaseOf Part 6 in Part 9"
ip2_single_owner_bounded: "Phase A scope is single-owner (Ruslan, Berlin); attention-budget cap (20 active tasks per Manager rule), 3-tier SLA values (L1 ≤4h same-session, L2 ≤7d batch, L3 immediate auto-log), Russian-primary content patterns are RUSLAN-LAYER values; Foundation generic = the 3-tier STRUCTURE + cap mechanism + schema. F.9 Bridge structural change ≥35% required at >10× scale per Wave A Ashby BOSC-A-T-X analysis."
F: F5
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md decision #1 — F4 → F5. Decision #6 IP-2 single-owner bounded + multi-owner stub fields F5 → F8 LOCKED. Decision #3 C4 nomenclature fix accepted (Part 9 §D edge-table 0 PhaseOf Part 6 entries; methodologically-uses Part 6)."
ClaimScope: "Holds for any single-owner knowledge-work system that needs canonical daily/weekly/monthly interaction shape with attention-budget cap + draft-disposition workflow + 3-tier SLA classification. Bundle 4 introduces daily-log + weekly-review schemas, draft-disposition table (C2 producer side), and 3-tier SLA taxonomy. Phase A scope: single-owner Jetix Phase-A €50K horizon; multi-owner Phase B/C requires F.9 Bridge structural change ≥35%. Fork-portable for Phase B partner imports."
R:
  refuted_if: "A future cycle surfaces an owner interaction shape that cannot be expressed within daily-log/weekly-review/SLA-tier schemas without breaking IP-2 single-owner bounded; OR Part 9 attempts to pre-gate items into Part 6 (per C4 fix `methodologically-uses` not `PhaseOf`); OR weekly review fails to produce draft-disposition table; OR multi-owner case attempted without F.9 Bridge spec"
  accepted_if: "Bundle 4 Part 9 architecture acked; daily-log + weekly-review schemas declared with draft-disposition table; SLA taxonomy declared at .claude/config/sla-taxonomy.yaml; IP-2 declaration explicit in §X with multi-owner stub fields in §I; C4 nomenclature fix applied throughout §D; weekly review surfaces methodology promotion candidates to Part 5"
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (§2 Part 9)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md (§2 Part 9; §6 item 2 IP-2 bounded; §3.4 C4 nomenclature fix)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md (IP-2 + IP-7)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md (Torres CDH weekly cadence)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md (toil < 50%; alert-routing)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md (Naval specific knowledge filter)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md (Forte PARA tier)"
  - "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§2.5 weekly cadence; §2.6 daily ops; §3.2.6 attention-budget cap; §4.2-§4.3 3-tier SLA; §6.2 founder agency)"
  - "design/JETIX-FPF.md (IP-2 bounded context with F.9 Bridge; IP-7 writing-as-thinking; A.6.B L/A/D/E; A.14 typed edges)"
  - "swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§H commit interface)"
  - "swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md (§A weekly review surfaces methodology candidates)"
  - "swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§I.1 F-G-R F8)"
  - "swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.4 awaiting-approval-packet schema F8; §I.3 blast-radius 4-tier; §I.2 default-deny)"
  - "swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md (§I.1 canonical health-signal schema; alert-routing for 3-tier SLA)"
  - "decisions/AUDIT-CURRENT-STATE-2026-04-27.md (daily-log/ baseline)"
  - "raw/books-md/sre/google-sre-book.md (Ch.6 monitoring; Ch.15 postmortems)"
  - "raw/books-md/sre/google-srewb-implementing-slos.md (Ch.2 burn-rate algebra; analogous SLA tiers)"
---

# Foundation Part 9 — Owner Interaction Scaffold (Architecture)

## §0 Executive Summary

**Part 9 closes the owner attention loop.** Every day the owner runs the
system through a canonical interaction shape (morning intent → cycle dispatch
→ afternoon execution → evening reflection committed); every week through a
weekly review with a draft-disposition table; every month through a strategic
reflection. Attention-budget is capped at the Manager rule (20 active tasks
per Phase A — RUSLAN-LAYER value). Items entering the promotion workflow are
classified into a 3-tier SLA taxonomy (L1 strategic same-session / L2 tactical
weekly batch / L3 routine auto-log) — declared canonically as Foundation
artefact at `.claude/config/sla-taxonomy.yaml`.

**Without Part 9, the system has agents but no canonical owner interface.**
Ruslan's attention budget gets shredded by ad-hoc surfacing patterns. Drafts
accumulate without disposition. Weekly retrospection — the Plan/Work/Review/
Compound boundary that Part 5 needs — never happens. Methodology promotion
candidates pile up in agent strategies.md but never surface to wiki/methodology/
because there's no weekly review ritual to lift them. The 3-tier SLA classifies
nothing because no canonical taxonomy exists; gate ack latency drifts toward
worst-case for every item.

Bundle 4 introduces three structural firsts for Part 9:

- **`daily-log.json` + `weekly-review.json` schemas declared (P9.1 + P9.2).**
  The daily-log schema canonicalises the owner's daily working artefact:
  morning intent (today's appetite + 1-3 high-leverage tasks); afternoon
  execution (cycle dispatch summary; surprises); evening reflection (what
  worked; what got dropped; methodology candidates surfaced). The
  weekly-review schema introduces the **draft-disposition table** — the C2
  producer side (Bundle 3 set the consumer side via Part 8 SLI/SLO; Bundle 4
  sets producer side here). Each accumulated draft from the prior week is
  classified `accept | iterate | discard`; rationale prose captured; action
  taken (promotion request, draft revision, archive marker).
- **3-tier SLA taxonomy as Foundation config (P9.3).** Per FUNDAMENTAL §4.2-
  §4.3 + sre-observability §4 P4 toil < 50% + Naval specific-knowledge filter:
  L1 strategic items get same-session ack (≤4h target — RUSLAN-LAYER value);
  L2 tactical batch ack weekly (≤7d target — RUSLAN-LAYER value); L3 routine
  auto-log immediate (RUSLAN-LAYER value). Foundation generic = the 3-tier
  STRUCTURE; specific values are RUSLAN-LAYER overrides.
- **IP-2 single-owner bounded with multi-owner stub fields in §I.** Per
  FUNDAMENTAL §2.6 + Bundle 1 RUSLAN-ACK + FPF IP-2: Part 9 = single-owner
  Phase A scope. Schema fields stub multi-owner extension (commented-out
  `owner_id`, `owners_aggregated`, per-owner sla-taxonomy fork pattern) for
  Phase B F.9 Bridge structural change ≥35% (per Wave A Ashby BOSC-A-T-X
  analysis). NOT IMPLEMENTED in Phase A — declared NOT implemented; Phase B
  work explicit.

**C4 nomenclature fix applied verbatim.** Wave A Part 9 §D used `PhaseOf Part
6` for governance gate dependency. The correct A.14 type is
`methodologically-uses Part 6` — Part 9 USES the gate as a service (per-item
classification + AWAITING-APPROVAL emission); Part 9 is NOT an exclusive
pre-gate phase. Brigadier autocheck verifies §D contains zero `PhaseOf Part 6`
entries [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§3.4
C4].

Reuse over reinvention: `daily-log/` directory exists (1 file currently per
AUDIT); `/plan-day`, `/close-day` skills exist; `shared/state/kanban.json` +
`shared/state/priorities.json` exist [src:CLAUDE.md:Skills + decisions/AUDIT-CURRENT-STATE-2026-04-27.md].
Part 9 **canonicalises** — does NOT reinvent. Schema declarations
operationalise existing convention; the daily-log + weekly-review files
already use this informal shape.

The owner attention loop is anchored in IP-7 writing-as-thinking [src:design/JETIX-FPF.md:§5.7] —
strategic reflection is owner-authored prose; agents contribute structured
extractions only. The 3-tier SLA is anchored in FUNDAMENTAL §4.2-§4.3 [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2].
The weekly review postmortem culture is anchored in Google SRE Book Ch.15
blameless postmortem [src:raw/books-md/sre/google-sre-book.md:Ch.15]. The
Naval specific-knowledge filter (L1 strategic vs L2/L3 delegate-able) is
anchored in stoic-epistemic [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md].

**Phase A scope discipline.** Single-owner Jetix Phase-A €50K horizon. All
SLA tiers calibrated to single-owner reaction time. Attention-budget cap is
RUSLAN-LAYER specific value (20 active tasks); cap mechanism is Foundation.
Phase B partner forks adopt the schema; partner's attention-budget cap and
SLA times are partner's RUSLAN-LAYER (own values per fork's reaction time).

**Fork-portable by construction.** A Phase B partner forks Foundation,
declines RUSLAN-LAYER (specific cap value 20, specific SLA times, Russian-
primary content patterns), keeps the 3-tier SLA structure + schemas + cap
mechanism + draft-disposition table mechanic. F.9 Bridge required if partner
fork later extends to multi-owner within same Jetix instance — daily-log
`owner_id` field uncommented; weekly review `owners_aggregated` field
populated; SLA taxonomy split per-owner via `sla-taxonomy.<owner_id>.yaml`
fork pattern.

[F4|G:Bundle 4 Part 9 architecture — single-owner Phase A; Fork-portable; multi-owner Phase B requires F.9 Bridge|R-medium — pending Ruslan ack]

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Owner-authored daily intent | Owner prose at top of `daily-log/<YYYY-MM-DD>.md` per IP-7 — declares appetite for the day, 1-3 high-leverage tasks, any blocked context | `/plan-day` skill invocation (event-driven on owner action) | F2|G:per-day owner intent|R-low — pre-execution draft |
| Drafts from all other parts | Draft artefacts surfaced by Parts 2/3/5/7/10 — agent-drafted strategic content (project briefs, methodology promotion candidates, KB synthesis outputs, scope-record proposals, retrospective drafts, CRM action proposals) | `draft-ready` event from emitting parts; surfaces in weekly review | F2-F4|G:per-draft|R-varies |
| Health dashboard from Part 8 | Weekly health snapshot per Part 8 §I.1 canonical health-signal schema; SLI deltas; alert routing recommendations | `weekly-health-ready` event from Part 8 | F4|G:Part 8 Bundle 3 LOCKED|R-medium |
| Project status from Part 7 | Project state transitions per Part 7 §B; project-retrospective-packets for closed projects (Bundle 4 UND-3 finalization) | `project-status-update` events from Part 7 | F4-F5|G:per-project|R-medium |
| Methodology promotion candidates from Part 5 | DRR ledger entries with `validated_in_cycles ≥ 2` from `agents/<id>/strategies.md`; surface to weekly review for promotion-disposition | `methodology-candidate-surfaced` event from Part 5 §I.1 | F4|G:Part 5 Bundle 3 LOCKED|R-medium |
| Attention budget state | `shared/state/kanban.json` WIP counts; `shared/state/priorities.json` priority stack; `agents/<id>/scratchpad.md` working memory load | Read at /plan-day OR /close-day OR weekly review invocation | F4|G:operational state|R-medium |
| 3-tier SLA taxonomy config | `.claude/config/sla-taxonomy.yaml` — declared canonical Bundle 4 P9.3 (this part owns) | Read at draft classification time + weekly review SLA-tier review | F5|G:Bundle 4 P9.3 LOCKED|R-high |

**§A.1 Concrete consequence — IP-7 writing-as-thinking enforced at intake.**
Owner-authored daily intent prose is FOUNDATIONAL — agents may draft daily-log
STRUCTURE (frontmatter; section headers) but not the strategic intent text.
The schema (§I.1) declares `morning_intent` field as `owner-authored: true`
predicate; intake validation checks the field's authorship via git blame on
the line range — if blame matches an agent commit (e.g., committed by
`[brigadier]` token), the field is rejected as agent-authored. This prevents
the IP-7 anti-pattern: "Если и сам текст пишет LLM — исчезает мышление
письмом" [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P2].

**§A.2 Concrete consequence — Drafts MUST carry source provenance for intake.**
Drafts admitted to Part 9's draft-disposition table only if accompanied by
`sources:` frontmatter field + ≥1 inline `[src:...]` citation per Part 6a
provenance discipline. Drafts without provenance auto-rejected at intake; the
draft author is notified via `comms/mailboxes/<role>.jsonl` to fix
provenance before re-submitting.

**§A.3 Concrete consequence — Methodology candidate surfacing is event-driven
not poll-based.** Part 5 §I.1 emits methodology-candidate-surfaced events when
`validated_in_cycles ≥ 2` predicate fires. Part 9 weekly review consumes
events from `comms/mailboxes/part-9.jsonl`. NO polling; NO weekly cron query
of strategies.md. This aligns with Bundle 4's broader event-driven cadence
discipline (Part 7 §E).

**§A.4 Concrete consequence — 3-tier SLA classification feeds Part 6b
enforcement at intake time.** Drafts entering Part 9 carry SLA tier metadata
classified per `.claude/config/sla-taxonomy.yaml` event_examples. Part 6b
enforcement reads sla_tier and applies tier-appropriate gate timing: L1 →
same-session ack required (≤4h RUSLAN-LAYER); L2 → Friday batch window (≤7d
RUSLAN-LAYER); L3 → auto-log no gate. This is the operational handoff between
Part 9 (intake classifier) and Part 6b (gate enforcer) — DRY enforced via
shared schema reference (no double-classification logic).

**§A.5 Concrete consequence — Health signals from Part 8 surface in afternoon
execution + weekly review.** Part 8 emits weekly health snapshots via
`comms/mailboxes/part-9.jsonl`. Part 9 reads at /close-day (afternoon
execution surprises field) AND at weekly review composition (sla_tier_review
section + tier_breaches[] populated from Part 8 alerts). The two-stage
consumption (daily for awareness, weekly for action) prevents Part 8 alerts
from drowning out daily flow while ensuring weekly review has full context.

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| `daily-log/<YYYY-MM-DD>.md` | Committed daily working artefact conforming to §I.1 schema (frontmatter + morning intent + afternoon execution + evening reflection sections) | `[daily] plan: <YYYY-MM-DD>` commit at `/plan-day`; `[daily] eod: <YYYY-MM-DD>` commit at `/close-day`; via Part 1 §H | F4|G:per-day artefact|R-medium |
| `weekly-reviews/<YYYY-Wnn>.md` | Committed weekly review artefact conforming to §I.2 schema (frontmatter + draft-disposition table + retrospective + methodology promotion surfacing + SLA-tier review) | `[review] weekly: <YYYY-Wnn>` commit via Part 1 §H | F4|G:per-week artefact|R-medium |
| `monthly-reflections/<YYYY-MM>.md` | Committed monthly reflection artefact (strategic synthesis + compound-learning input — owner-authored per IP-7) | `[review] monthly: <YYYY-MM>` commit | F5|G:owner-authored strategic|R-high |
| Promoted canonical artefacts to Part 6b | `accept`-disposition drafts forwarded with `gate_class: draft_promotion` AWAITING-APPROVAL packets per Part 6b §I.4 F8 schema | `gate-request` event with `gate_class: draft_promotion` | F4→F5|G:Part 6b §I.4 LOCKED|R-high on ack |
| 3-tier SLA gate classifications | Per pending item: L1 / L2 / L3 classification per `.claude/config/sla-taxonomy.yaml`; included in AWAITING-APPROVAL packet metadata | Per-item classification at intake | F4|G:Part 9 owns classification|R-medium |
| Methodology promotion forwarding | `accept`-dispositioned methodology candidates from weekly review forwarded to Part 5 (Part 5 emits to wiki/methodology/<rule-slug>-DRAFT.md and opens Part 6b draft_promotion gate per Part 5 §I.1) | `methodology-promotion-forwarded` event | F4|G:Part 5 §I.1 input|R-medium |
| `shared/state/priorities.json` | Updated priority stack at weekly review close | `priorities-updated` event via Part 1 §H | F4|G:operational state|R-medium |
| `shared/state/kanban.json` | WIP-count updates per intake/promotion/archive (attention-budget enforcement) | `wip-state-changed` event per FUNDAMENTAL §3.2.6 | F4|G:operational state|R-medium |
| Part 8 health-signal pipeline | `daily-log-creation-rate` SLI; `weekly-review-completion-rate` SLI; `draft-clearance-rate` SLI; `l1-sla-compliance-rate` SLI — emitted per Part 8 §I.1 canonical health-signal schema | `health-metric-updated` event | F4|G:Part 8 SLI consumption|R-medium |
| `swarm/wiki/log.md` | Append-only log line per committed review artefact | Per artefact commit | F4|G:audit trail|R-medium |

**§B.1 Concrete consequence — Draft-disposition table is the canonical C2
PRODUCER side.** Bundle 3 set the C2 CONSUMER side via Part 8 SLI/SLO (drafts
accumulate; consumer reads accumulation rate). Bundle 4 Part 9 sets the
PRODUCER side: weekly review classifies each accumulated draft into `accept |
iterate | discard` with rationale + action taken. The C2 contradiction
(producer vs consumer ownership of draft-promotion responsibility — surfaced
in Wave A) is resolved: Part 9 PRODUCES disposition decisions; Part 6b
ENFORCES via `gate_class: draft_promotion` for `accept`-dispositioned items.

**§B.2 Concrete consequence — 3-tier SLA classification is mandatory at
intake.** Every draft entering Part 9 carries an SLA-tier classification
(L1 / L2 / L3) populated at intake. Unclassified drafts default to L2 per
FUNDAMENTAL §4.2 conservative-not-aggressive principle. Classification feeds
into Part 6b enforcement at promotion time (L1 same-session-required; L2
batch-acceptable Friday window; L3 auto-log no gate).

**§B.3 Concrete consequence — Monthly reflection is owner-authored only.**
Per IP-7. Schema field `monthly_reflection_text` carries `owner-authored:
true` predicate; agent contribution = structured extraction of cycle data
populating `cycle_summary[]` array. The strategic prose is Ruslan's. This is
the structural enforcement of FPF IP-7 + FUNDAMENTAL §6.2 founder-agency
preservation.

---

## §C Side-effects

- **Append-only writes to daily-log + weekly-reviews + monthly-reflections.**
  No in-place edits. Corrections via NEW entries with `corrects:` pointer per
  Reversal Transactions discipline (Young 2010).

- **WIP-count updates on intake / promotion / archive.** Per FUNDAMENTAL
  §3.2.6 attention-budget cap. Cap value = 20 (RUSLAN-LAYER); cap mechanism =
  Foundation.

- **AWAITING-APPROVAL emissions for `accept`-dispositioned drafts.** Per
  Part 6b §I.4 F8 schema. `gate_class: draft_promotion` for content drafts;
  `gate_class: stage_gate` for project-related items; `gate_class: stop_gate`
  for items with constitutional implications.

- **SLA-tier classification fed to Part 6b enforcement arm.** L1 →
  same-session ack required (Part 6b SLA L1 — RUSLAN-LAYER value ≤4h);
  L2 → Friday batch ack window (Part 6b SLA L2 — RUSLAN-LAYER value ≤7d);
  L3 → auto-log no gate (Part 6b SLA L3 — RUSLAN-LAYER value immediate).

- **PARA-tier tagging on every artefact.** Daily-log = Area; weekly-review =
  Area; monthly-reflection = Resource. Drafts inherit PARA tier from origin
  part. Per Bundle 2 P2.2 PARA-tier mandatory.

- **Health signal emissions via swarm/lib accessor.** NO direct file writes
  to `shared/state/system-health.json`. Per Bundle 2 C1 Joint Design canonical.

- **NO direct external writes from Part 9.** External actions (Slack
  notifications about pending L1 items, email reminders) flow through Part 10
  RT-2 write-ack adapters, not through Part 9.

---

## §D Dependencies (typed per FPF A.14)

**C4 NOMENCLATURE FIX APPLIED VERBATIM** per Wave A dependency-graph §3.4 +
brigadier autocheck §6.8: every Part 6 / Part 6a / Part 6b reference uses
`methodologically-uses` not `PhaseOf`. Part 9 USES the gate as service; Part
9 is NOT an exclusive pre-gate phase.

| Dep | Edge type | Target | Rationale |
|---|---|---|---|
| D-1 | `creates` | **Part 1** | All daily/weekly/monthly artefacts committed via Part 1 §H. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§H] |
| D-2 | `methodologically-uses` | **Part 6b** | C4 FIX applied. `accept`-dispositioned drafts forwarded to Part 6b with `gate_class: draft_promotion`. Part 9 USES gate; not pre-gate phase. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4] |
| D-3 | `methodologically-uses` | **Part 6a** | F-G-R per Part 6a §I.1 F8 schema on every emitted artefact. Approval-log entries written per Part 6a §C on each gate ack. C4 FIX applied. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 + §C] |
| D-4 | `methodologically-uses` | **Part 5** | Weekly review surfaces methodology promotion candidates from `agents/<id>/strategies.md`. Monthly reflection feeds Part 5 compound-learning input (S4 environment scanning per VSM). [src:swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md:§A] |
| D-5 | `operates-in` | **Part 8** | Owner reflection data (attention-budget utilisation, daily-log creation rate, weekly review completion rate) are health signals that Part 8 monitors. [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§I.1] |
| D-6 | `methodologically-uses` | **Part 7** | Weekly review consumes Part 7 project status updates + project-retrospective-packets for closed projects (Bundle 4 UND-3 finalization). [src:swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md:§B] |
| D-7 | `methodologically-uses` | **Part 4** | Cycle dispatch context surfaces in afternoon execution section of daily-log. [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.1] |
| D-8 | `constrained-by` | **FPF IP-2** | Single-owner bounded context; F.9 Bridge structural change ≥35% required at >10× scale per Wave A Ashby BOSC-A-T-X analysis. [src:design/JETIX-FPF.md:§5.2] |
| D-9 | `constrained-by` | **FPF IP-7** | Writing-as-thinking — owner authors strategic content; agents contribute structured extractions only. [src:design/JETIX-FPF.md:§5.7] |
| D-10 | `constrained-by` | **FUNDAMENTAL §3.2.6** | Attention-budget cap discipline; cap mechanism is Foundation; cap value 20 is RUSLAN-LAYER. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.6] |
| D-11 | `constrained-by` | **FUNDAMENTAL §4.2-§4.3** | 3-tier SLA structure constitutional (L1/L2/L3); specific times RUSLAN-LAYER. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2] |
| D-12 | `constrained-by` | **FUNDAMENTAL §6.2** | Founder agency preservation — strategic decisions owner-only. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2] |

**Brigadier autocheck verifies §D contains zero `PhaseOf Part 6`,
`PhaseOf Part 6a`, `PhaseOf Part 6b` entries** per §6.8 autocheck procedure.
Grep returns 0 hits → C4 FIX confirmed applied.

---

## §E Boundary (FPF A.6.B L/A/D/E)

### E.1 Laws (invariants that MUST hold)

**L1 — IP-7 writing-as-thinking asymmetry.** Owner authors strategic and
reflective content; agents contribute structured extractions only. Schema
fields with `owner-authored: true` predicate (morning_intent, evening
reflection, monthly_reflection_text) checked at intake via git blame.

**L2 — Attention-budget cap is hard Law.** No agent or automation may add
items to the owner's active queue beyond the declared WIP limit (20 active
tasks — RUSLAN-LAYER value) without explicit owner ack. Default-Deny applies:
attempt to exceed cap → AWAITING-APPROVAL `gate_class: stop_gate` per Part 6b.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.6]

**L3 — 3-tier SLA classification mandatory.** Every item entering the
promotion workflow carries L1/L2/L3 classification. Unclassified items default
to L2 (conservative).

**L4 — F.9 Bridge documentation REQUIRED at multi-owner activation.** Any
deployment in a multi-owner context (1 owner → 2+ owners within same Jetix
instance) MUST produce F.9 Bridge specification per FPF §5.2 BEFORE Part 9
functions are exposed to additional human owners. Phase A operates single-
owner until partner-onboarding signal sustained ≥2 weeks.

**L5 — IP-2 single-owner Phase A bounded.** Schema `owner_id` field declared
but COMMENTED OUT in Phase A schema (NOT implemented; Phase B work). Default
owner = Ruslan; no per-owner aggregation logic in Phase A.

**L6 — Draft provenance mandatory at intake.** No drafts admitted without
`sources:` frontmatter + ≥1 inline `[src:...]` citation per Part 6a
provenance discipline.

**L7 — Append-only daily/weekly/monthly artefacts.** No in-place edits.
Corrections via NEW entries with `corrects:` pointer per Reversal Transactions
discipline (Young 2010).

**L8 — Halt-Log-Alert ordering for Tier 0 events.** Attention-cap-exceedance
attempt fires Halt-Log-Alert per Part 6b §E L9 (≤1s halt / ≤5s log / ≤60s
alert).

**L9 — C4 nomenclature fix.** Part 9 USES Part 6 gate as service via
`methodologically-uses` edge; Part 9 is NOT exclusive pre-gate phase.
Brigadier autocheck rejects `PhaseOf Part 6` in §D.

**L10 — Weekly review surfaces methodology promotion candidates.** Per Part 5
§A consumption contract: Part 9 weekly review reads `agents/<id>/strategies.md`
entries with `validated_in_cycles ≥ 2` predicate AND classifies each
candidate `accept | iterate | discard`. `accept` triggers Part 5 §I.1
draft promotion → wiki/methodology/<rule-slug>-DRAFT.md + Part 6b
`gate_class: draft_promotion`.

### E.2 Admissibility (acceptance criteria for inputs)

**A-1.** Daily working artefact admitted only if schema-conformant: date
header in YYYY-MM-DD format, morning_intent section non-empty (owner-authored
predicate), afternoon_execution section structurally present, para_tier:
Area declared, owner: ruslan declared, f_g_r populated.

**A-2.** Drafts from other parts admitted only with `sources:` frontmatter +
≥1 inline `[src:...]` citation. Provenance-free drafts auto-rejected with
notification to draft author.

**A-3.** Promotion requests admitted only if SLA-tier classification declared
(L1/L2/L3 enum value).

**A-4.** Weekly review admitted only if it contains: draft-disposition table
with header columns (Draft path / Created / Status / Disposition / Rationale
/ Action taken); ≥1 draft entry classified; methodology candidate surfacing
(may be empty if no candidates ≥2 cycles); SLA-tier review section.

**A-5.** Monthly reflection admitted only if `monthly_reflection_text` is
owner-authored (git blame check); cycle_summary[] array auto-populated by
agent extraction.

**A-6.** Attention-budget intake check: WIP count + new item count ≤ cap
(20 RUSLAN-LAYER); else reject + emit AWAITING-APPROVAL `gate_class:
stop_gate` per Part 6b.

**A-7.** SLA tier classification at draft intake admissibility: every draft
entering Part 9 carries `sla_tier` metadata (L1/L2/L3 enum). Drafts without
sla_tier classification default to L2 per FUNDAMENTAL §4.2 conservative-not-
aggressive principle.

**A-8.** Methodology candidate surfacing admissibility: only candidates with
`validated_in_cycles ≥ 2` predicate per Part 5 §I.1 admitted into
`methodology_candidates_surfaced[]` array. Candidates with 1 cycle remain in
strategies.md ledger; do NOT surface to weekly review.

**A-9.** Draft-disposition entry admissibility: every entry MUST have non-empty
`disposition` enum value (accept | iterate | discard) AND `rationale` prose ≥
30 chars AND `action_taken` prose ≥ 10 chars. Stripped fields rejected at
weekly review commit.

**A-10.** Multi-owner accidental activation admissibility: schema field
`owner_id` cannot be activated (uncommented + populated) without
`design/F-9-Bridge-multi-owner-spec.md` file present. Pre-commit hook enforces.

### E.3 Deontics (obligations toward consumers)

**D-1.** MUST produce a weekly review artefact within 7 days of the prior one;
absence triggers a health alert to Part 8 (weekly cadence SLI per FUNDAMENTAL
§2.5).

**D-2.** MUST forward all L1-classified items to Part 6b gate WITHIN the same
session (L1 = external commitment or Lock modification — no batching per
FUNDAMENTAL §4.2 L1 SLA: same-session immediate).

**D-3.** MUST NOT auto-promote any item to canonical without owner ack
(FUNDAMENTAL §6.2 founder-agency; §4.5 anti-patterns).

**D-4.** MUST preserve full text of archived drafts (archive ≠ delete;
searchable with provenance per FUNDAMENTAL §1 UC-J.2).

**D-5.** MUST emit health signals via `swarm/lib/emit_health_signal()` accessor;
NO direct writes to `shared/state/system-health.json` (Bundle 2 C1 Joint
Design canonical).

**D-6.** MUST surface Part 5 methodology promotion candidates at every weekly
review (Part 9 reads Part 5 strategies.md; Part 9 classifies; Part 9 forwards
`accept` to Part 5 §I.1 promotion logic).

### E.4 Effects (measurable outcomes)

**E-1.** Daily-log creation rate ≥5 per working week (FUNDAMENTAL §3.5
indicative target). SLI tracked via Part 8.

**E-2.** Weekly review completion rate 1 per calendar week (FUNDAMENTAL §2.5
weekly checkup cadence).

**E-3.** Draft clearance rate ≤20 open drafts at any weekly review point
(WIP limit enforcement).

**E-4.** L1 SLA compliance 100% — every L1-classified item gated within
same-session. SLO target: 100%; deviation fires Part 8 alert per Part 9 §I.3.

**E-5.** L2 SLA compliance 95% — items batched within Friday window. SLO
target Phase B calibration.

**E-6.** L3 SLA compliance 100% — auto-log immediate. SLO target Phase B
calibration.

**E-7.** Draft-disposition coverage 100% — every accumulated draft from prior
week receives accept|iterate|discard disposition at weekly review.

**E-8.** Methodology promotion candidates surfaced 100% of strategies.md
entries with `validated_in_cycles ≥ 2` predicate.

**E-9.** Attention-budget utilisation reported in monthly reflection (peaks,
average, distribution across project types).

**E-10.** Methodology promotion candidate-to-DRAFT-emission rate ≥80% — at
least 80% of `weekly_disposition: accept` candidates result in committed
wiki/methodology/<rule-slug>-DRAFT.md within ≤7d of weekly review commit.
Below-threshold over 3 consecutive weeklies surfaces as Part 8 alert.

**E-11.** Draft-disposition latency: weekly review compose → disposition
classification of all accumulated drafts ≤2h synchronous owner time. SLO target
phase B calibration; Phase A indicative target.

**E-12.** SLA compliance reporting in every weekly review — `sla_tier_review`
section populated with l1_compliance_pct + l2_compliance_pct + l3_compliance_pct
+ tier_breaches[] array. Coverage target: 100% of weekly reviews include
sla_tier_review section.

**E-13.** Daily-log → weekly-review aggregation latency: weekly review composes
within ≤3h of trigger event (Friday EOD OR Sunday SOD per owner pick). SLO
target Phase B calibration.

### E.5 Effects extension — multi-owner Phase B activation predicates

Phase B activation requires the following effects to manifest BEFORE F.9 Bridge
spec is opened:
- **Sustained partner-onboarding signal**: ≥2 weeks of operational evidence
  with 2+ distinct human owners interacting with the system.
- **F.9 Bridge file present**: `design/F-9-Bridge-multi-owner-spec.md` lives;
  pre-commit hook verifies before allowing schema field activation.
- **Per-owner SLA calibration**: `sla-taxonomy.<owner_id>.yaml` files declared
  per owner; consistent structure (mirrors Foundation generic).

These are NOT Phase A effects but are declared here to make Phase B activation
auditable.

---

## §F Anti-scope

- Part 9 does NOT make strategic decisions — it scaffolds owner's strategic
  engagement; owner decides (FUNDAMENTAL §6.1 + §6.2).
- Part 9 does NOT own the gate mechanism — Part 6b owns AWAITING-APPROVAL
  enforcement; Part 9 classifies SLA tier and forwards.
- Part 9 does NOT substitute for founder agency — Part 9 IS the primary
  expression of the system's obligation to SCAFFOLD founder agency (PP-7 per
  Wave A A-1-critic-gate.md §2 Part 9).
- Part 9 does NOT define strategic document content (UC-A.2 strategic document
  creation assistance is triggered from weekly review BUT authored by owner per
  IP-7; agent contribution = structured extraction only).
- Part 9 does NOT cover CRM or external relationship management (Part 10).
- Part 9 does NOT run project execution — it surfaces project status for owner
  review; project execution lives in Part 7.
- Part 9 does NOT apply universally to multi-owner systems without F.9 Bridge
  specification (IP-2 bounded; solo-owner is explicit Phase A scope, not silent
  default).
- Part 9 is NOT a Torres CDH (Continuous Discovery Habits) implementation. CDH
  is RUSLAN-LAYER methodology library content; Foundation encodes only the
  generic "opportunity intake" sub-function within weekly review (OQ-MERGED-4
  resolution).
- Part 9 cadence is event-driven for daily artefacts (per /plan-day OR /close-
  day skill invocation event). Weekly + monthly cadences ARE periodic but the
  trigger is event-driven (Friday end-of-week skill invocation OR Sunday start-
  of-next-week — owner picks). This is NOT a contradiction with Bundle 4 OQ-5
  cadence-event-driven discipline because Part 9 does NOT gate state
  transitions on the calendar; the calendar is the trigger event-source for
  the owner's reflection action, not a transition gate.

---

## §G F-G-R Tagging

| Artefact emitted by Part 9 | F | G (ClaimScope) | R |
|---|---|---|---|
| Daily working page (intake draft) | F2 | That calendar day; mixes planning + exploration | R-low — pre-EOD draft |
| Daily working page (post-EOD commit) | F4 | That calendar day; owner-acked end-of-day | R-medium |
| Weekly review artefact | F4 | Current week; single-owner Phase A context | R-medium — covers all active parts; owner-reviewed |
| Monthly reflection artefact | F5 | Trailing month; strategic scope | R-high — owner-authored strategic; compound-learning input |
| Draft-disposition table entry (accept) | F4 | Single draft, single weekly review | R-medium — pending Part 6b ack |
| Draft-disposition table entry (iterate) | F3 | Single draft, single weekly review | R-low — explicit deferral |
| Draft-disposition table entry (discard) | F4 | Single draft, single weekly review | R-medium — explicit closure |
| Promoted canonical artefact (post-Part 6b ack) | F5 | Artefact's own claim scope | R-high — Part 6b gate passed; human ack recorded |
| L1/L2/L3 SLA classification | F4 | Single item, single session | R-medium — heuristic per `.claude/config/sla-taxonomy.yaml`; correctible by owner |
| Methodology promotion forwarded entry | F4 | Single rule_slug; classified accept | R-medium — pending Part 5 §I.1 + Part 6b draft_promotion ack |

---

## §H Code-level Interfaces

### H.1 `swarm/lib/owner_interaction_intake.py` (Phase B; specify-and-stub Phase A)

```python
def intake_draft(
    draft_path: str,
    origin_part: Literal["part-2", "part-3", "part-5", "part-7", "part-10"],
    sla_tier: Optional[Literal["L1", "L2", "L3"]] = None,
) -> dict:
    """
    Validate draft has sources: frontmatter + ≥1 inline [src:...] citation.
    If sla_tier not provided, classify via `.claude/config/sla-taxonomy.yaml`
    heuristic (default L2 if uncertain). Check WIP cap (kanban.json + new
    item count ≤ 20). Append to draft queue.

    Returns: {
      "intake_committed": bool,
      "sla_tier_assigned": str,
      "wip_count_post_intake": int,
      "rejection_reason": str | None
    }
    """
```

### H.2 `swarm/lib/owner_weekly_review.py` (Phase B; specify-and-stub)

```python
def compose_weekly_review(week_id: str) -> dict:
    """
    Aggregate accumulated drafts since last weekly review; populate
    draft-disposition table skeleton (owner classifies). Read agents/<id>/
    strategies.md for methodology candidates with validated_in_cycles ≥ 2;
    populate methodology_candidates_surfaced[] array. Compute SLA-tier
    review summary. Compose weekly-review artefact at weekly-reviews/<week_id>.md.

    Returns: {
      "weekly_review_path": str,
      "draft_count": int,
      "methodology_candidate_count": int,
      "sla_tier_breakdown": dict
    }
    """
```

### H.3 `swarm/lib/owner_attention_budget.py` (Phase B; specify-and-stub)

```python
def check_attention_budget(intake_count: int = 1) -> dict:
    """
    Read shared/state/kanban.json WIP count; check if WIP + intake_count > 20
    (RUSLAN-LAYER cap). If exceeded, return {"cap_exceeded": True, "current_wip":
    int, "cap": int} and emit AWAITING-APPROVAL gate_class: stop_gate per
    Part 6b. If within cap, return {"cap_exceeded": False, "current_wip": int}.

    Returns: {"cap_exceeded": bool, "current_wip": int, "cap": int,
              "stop_gate_packet_id": str | None}
    """
```

### H.4 `swarm/lib/owner_methodology_forwarding.py` (Phase B; specify-and-stub)

```python
def forward_methodology_candidate(
    rule_slug: str,
    disposition: Literal["accept", "iterate", "discard"],
    rationale: str,
) -> dict:
    """
    On disposition=accept: emit methodology-promotion-forwarded event to
    comms/mailboxes/part-5.jsonl. Part 5 §I.1 logic creates wiki/methodology/
    <rule-slug>-DRAFT.md with pipeline: ingested + opens Part 6b
    AWAITING-APPROVAL gate_class: draft_promotion.

    On disposition=iterate: append revision_note to agents/<id>/strategies.md
    entry; rule_slug remains in candidate state.

    On disposition=discard: mark strategies.md entry with
    `dispositioned_discard: <weekly-review-id>` field; rule_slug archived.

    Returns: {"forward_committed": bool, "part_5_packet_id": str | None}
    """
```

**§H.5 Phase A operational baseline.** These 4 interfaces are Phase B
materialisation surface. Phase A operates via existing `/plan-day`, `/close-
day` skills [src:CLAUDE.md:Skills]. The interfaces declare Foundation-level
shape for Phase B partner imports + scripted automation.

---

## §I Data Schemas

### §I.1 `shared/schemas/daily-log.json` (P9.1)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/daily-log.json",
  "$comment": "GENERIC Foundation schema. Per IP-2 single-owner Phase A: owner_id field commented out (Phase B materialization). Specific owner value (ruslan) and content-language patterns are RUSLAN-LAYER. Schema structure is Foundation-generic.",
  "title": "Daily working artefact",
  "description": "Schema for canonical owner daily-log artefacts per Wave C Bundle 4 Part 9 architecture. IP-7 writing-as-thinking enforced via owner-authored predicate on strategic prose fields.",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "initial Wave C Bundle 4 P9.1 — frontmatter + 3 sections (morning intent, afternoon execution, evening reflection); IP-7 owner-authored predicate; PARA tier mandatory; multi-owner stub field commented out",
      "breaking": false
    }
  ],
  "type": "object",
  "required": [
    "schema_version",
    "date",
    "owner",
    "projects_touched",
    "decisions_made",
    "ack_events",
    "attention_budget_used",
    "para_tier",
    "f_g_r"
  ],
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "date": { "type": "string", "format": "date" },
    "owner": {
      "type": "string",
      "description": "Single-owner Phase A. Default ruslan (RUSLAN-LAYER). Schema field is Foundation-generic."
    },
    "// PHASE-B owner_id": "Phase B multi-owner extension: replace `owner` string with `owner_id` enum derived from per-fork owners.yaml. Currently commented out — NOT IMPLEMENTED; Phase B F.9 Bridge work.",
    "projects_touched": {
      "type": "array",
      "items": { "type": "string", "pattern": "^[a-z][a-z0-9-]*$" },
      "description": "Project slugs touched today (ref Part 7 project schema)."
    },
    "decisions_made": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["decision_id", "decision_summary", "projects_touched", "rationale"],
        "properties": {
          "decision_id": { "type": "string", "pattern": "^dec-[0-9]{8}-[a-z0-9-]+$" },
          "decision_summary": { "type": "string", "minLength": 30 },
          "projects_touched": { "type": "array", "items": { "type": "string" } },
          "rationale": { "type": "string", "minLength": 30 }
        }
      },
      "description": "Owner-authored decisions made today. IP-7 — owner authors rationale prose."
    },
    "ack_events": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["packet_id", "gate_class", "action_taken"],
        "properties": {
          "packet_id": { "type": "string" },
          "gate_class": { "type": "string", "enum": ["stop_gate", "stage_gate", "draft_promotion"] },
          "action_taken": { "type": "string" }
        }
      },
      "description": "Today's AWAITING-APPROVAL ack events. References Part 6b §I.4 LOCKED schema gate_class enum."
    },
    "attention_budget_used": {
      "type": "object",
      "required": ["tasks_started", "tasks_completed", "tasks_paused"],
      "properties": {
        "tasks_started": { "type": "integer", "minimum": 0 },
        "tasks_completed": { "type": "integer", "minimum": 0 },
        "tasks_paused": { "type": "integer", "minimum": 0 }
      }
    },
    "para_tier": { "type": "string", "enum": ["Project", "Area", "Resource", "Archive"], "default": "Area" },
    "f_g_r": { "$ref": "shared/schemas/f-g-r.json" },
    "morning_intent": {
      "type": "object",
      "required": ["appetite", "high_leverage_tasks", "owner_authored"],
      "properties": {
        "appetite": { "type": "string", "minLength": 10 },
        "high_leverage_tasks": {
          "type": "array",
          "items": { "type": "string", "minLength": 10 },
          "minItems": 1, "maxItems": 3
        },
        "owner_authored": { "type": "boolean", "const": true, "description": "Predicate — must be owner-authored per IP-7. Validated via git blame at commit time." }
      }
    },
    "afternoon_execution": {
      "type": "object",
      "properties": {
        "cycle_dispatch_summary": { "type": "string" },
        "surprises": { "type": "array", "items": { "type": "string" } }
      }
    },
    "evening_reflection": {
      "type": "object",
      "required": ["what_worked", "what_dropped", "methodology_candidates_surfaced", "owner_authored"],
      "properties": {
        "what_worked": { "type": "string" },
        "what_dropped": { "type": "string" },
        "methodology_candidates_surfaced": { "type": "array", "items": { "type": "string", "pattern": "^[a-z][a-z0-9-]+$" } },
        "owner_authored": { "type": "boolean", "const": true, "description": "Predicate — must be owner-authored per IP-7." }
      }
    }
  },
  "additionalProperties": false
}
```

[F4|G:Bundle 4 P9.1 daily-log schema|R-medium]

### §I.2 `shared/schemas/weekly-review.json` (P9.2 — with draft-disposition table)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/weekly-review.json",
  "$comment": "GENERIC Foundation schema. C2 PRODUCER side via draft-disposition table. Multi-owner stub field commented out (Phase B). Bundle 4 P9.2.",
  "title": "Weekly review artefact",
  "description": "Schema for canonical owner weekly-review artefacts per Wave C Bundle 4 Part 9. Draft-disposition table is C2 PRODUCER side (Bundle 3 set CONSUMER side via Part 8 SLI/SLO). Methodology promotion surfacing per Part 5 §A.",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "initial Wave C Bundle 4 P9.2 — frontmatter + draft-disposition table + retrospective + methodology promotion surfacing + SLA-tier review; multi-owner stub field commented out",
      "breaking": false
    }
  ],
  "type": "object",
  "required": [
    "schema_version",
    "week",
    "period_start",
    "period_end",
    "daily_logs_referenced",
    "projects_touched",
    "draft_disposition_table",
    "methodology_candidates_surfaced",
    "attention_budget_summary",
    "appetite_actual_vs_planned",
    "sla_tier_review",
    "para_tier",
    "f_g_r"
  ],
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "week": { "type": "string", "pattern": "^[0-9]{4}-W[0-9]{2}$", "description": "ISO week ID (e.g. 2026-W18)." },
    "period_start": { "type": "string", "format": "date" },
    "period_end": { "type": "string", "format": "date" },
    "// PHASE-B owners_aggregated": "Phase B multi-owner extension: array of owner_ids whose daily-logs aggregate into this weekly review. Currently commented out — NOT IMPLEMENTED; Phase B F.9 Bridge work.",
    "daily_logs_referenced": {
      "type": "array",
      "items": { "type": "string", "format": "date" },
      "minItems": 1
    },
    "projects_touched": { "type": "array", "items": { "type": "string", "pattern": "^[a-z][a-z0-9-]*$" } },
    "draft_disposition_table": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["draft_path", "created", "status", "disposition", "rationale", "action_taken"],
        "properties": {
          "draft_path": { "type": "string", "description": "Path to the draft artefact." },
          "created": { "type": "string", "format": "date" },
          "status": { "type": "string", "enum": ["draft", "iterating", "ready"] },
          "disposition": { "type": "string", "enum": ["accept", "iterate", "discard"] },
          "rationale": { "type": "string", "minLength": 30 },
          "action_taken": { "type": "string", "minLength": 10, "description": "Concrete action: 'promotion request emitted via Part 6b draft_promotion gate'; 'iterate — revision note appended'; 'discard — archived to drafts/archive/'." }
        }
      },
      "description": "C2 PRODUCER side. Each accumulated draft from prior week receives accept|iterate|discard disposition. Drives Part 6b enforcement at promotion time."
    },
    "methodology_candidates_surfaced": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["rule_slug", "evidence_count"],
        "properties": {
          "rule_slug": { "type": "string", "pattern": "^[a-z][a-z0-9-]+$" },
          "evidence_count": { "type": "integer", "minimum": 2 },
          "validated_in_cycles": { "type": "array", "items": { "type": "string", "pattern": "^cyc-[a-z0-9-]+$" } },
          "weekly_disposition": { "type": "string", "enum": ["accept", "iterate", "discard"] }
        }
      },
      "description": "Methodology candidates surfaced from agents/<id>/strategies.md with validated_in_cycles ≥ 2. Owner classifies disposition; accept → forwarded to Part 5 §I.1."
    },
    "attention_budget_summary": {
      "type": "object",
      "properties": {
        "avg_used": { "type": "number" },
        "peaks": { "type": "array", "items": { "type": "object", "properties": { "date": { "type": "string", "format": "date" }, "wip_count": { "type": "integer" } } } }
      }
    },
    "appetite_actual_vs_planned": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["project_slug", "planned_weeks", "actual_weeks_to_date", "delta_pct"],
        "properties": {
          "project_slug": { "type": "string" },
          "planned_weeks": { "type": "integer" },
          "actual_weeks_to_date": { "type": "integer" },
          "delta_pct": { "type": "number" }
        }
      },
      "description": "Per Part 7 §I.1 appetite tracking. Surfaces overrun projects for re-shape OR archive decision."
    },
    "sla_tier_review": {
      "type": "object",
      "properties": {
        "l1_compliance_pct": { "type": "number" },
        "l2_compliance_pct": { "type": "number" },
        "l3_compliance_pct": { "type": "number" },
        "tier_breaches": { "type": "array", "items": { "type": "object", "properties": { "tier": { "type": "string" }, "item_id": { "type": "string" }, "delta": { "type": "string" } } } }
      }
    },
    "weekly_retrospective": {
      "type": "object",
      "required": ["what_worked", "what_blocked", "what_dropped", "next_week_appetite", "methodology_candidates_surfaced", "owner_authored"],
      "properties": {
        "what_worked": { "type": "string" },
        "what_blocked": { "type": "string" },
        "what_dropped": { "type": "string" },
        "next_week_appetite": { "type": "string" },
        "methodology_candidates_surfaced": { "type": "array", "items": { "type": "string" } },
        "owner_authored": { "type": "boolean", "const": true }
      }
    },
    "para_tier": { "type": "string", "enum": ["Area", "Resource"], "default": "Area" },
    "f_g_r": { "$ref": "shared/schemas/f-g-r.json" }
  },
  "additionalProperties": false
}
```

[F4|G:Bundle 4 P9.2 weekly-review schema|R-medium]

### §I.3 `.claude/config/sla-taxonomy.yaml` (P9.3 — 3-tier SLA Foundation artefact)

Companion file declared inline below; physical file generation per Bundle 4
deliverable §8.3:

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: "initial Wave C Bundle 4 P9.3 — 3-tier SLA taxonomy Foundation artefact (L1/L2/L3); RUSLAN-LAYER override pattern for specific time values"
    breaking: false
managed_by: brigadier
last_modified: 2026-04-28

# Foundation-generic 3-tier SLA structure per FUNDAMENTAL §4.2-§4.3.
# Specific time values are RUSLAN-LAYER overrides (declared at instance deployment).
# Cross-references: Part 6b §I.3 blast-radius 4-tier table; Part 9 §J.

foundation_generic:
  tier_definitions:
    - tier: L1
      name: strategic
      label: "L1 — Strategic"
      description: "External commitment OR Lock modification OR canonical promotion OR financial decision above RUSLAN-LAYER threshold."
      target_latency_phase_a: "ruslan-layer-override"  # RUSLAN-LAYER value
      target_latency_default_recommendation: "≤4h same-session"
      blast_radius_typical: 1  # Tier 1 — Strategic per Part 6b §I.3
      gate_class_typical: "stop_gate"
      event_examples_foundation_generic:
        - "stage-gate ack on AWAITING-APPROVAL packets per FUNDAMENTAL §4.2-§4.3 human-only tasks"
        - "external commitment write-ack via Part 10 RT-2 adapter"
        - "Foundation revision proposal (change to decisions/JETIX-VISION-FUNDAMENTAL*)"
        - "F8 invariant change"
      requires_synchronous_owner: true
      batch_eligible: false

    - tier: L2
      name: tactical
      label: "L2 — Tactical"
      description: "Meaningful change to non-canonical artefacts; new config entries; routine policy edits; low-severity gate decisions."
      target_latency_phase_a: "ruslan-layer-override"
      target_latency_default_recommendation: "≤7d batch (Friday window)"
      blast_radius_typical: 2  # Tier 2 — Tactical per Part 6b §I.3
      gate_class_typical: "stage_gate"
      event_examples_foundation_generic:
        - "wiki entry promotion F4→F5 (not yet canonical)"
        - "agent strategies.md substantive revision (beyond DRR append)"
        - "non-canonical config change additions to .claude/config/*.yaml"
        - "draft-disposition: accept on weekly review"
      requires_synchronous_owner: false
      batch_eligible: true
      batch_window: "weekly-friday"

    - tier: L3
      name: routine
      label: "L3 — Routine"
      description: "Low-blast, reversible, routine operations. In whitelist. Auto-log no gate."
      target_latency_phase_a: "ruslan-layer-override"
      target_latency_default_recommendation: "immediate (auto-log to audit)"
      blast_radius_typical: 3  # Tier 3 — Routine per Part 6b §I.3
      gate_class_typical: null  # No gate
      event_examples_foundation_generic:
        - "read-only intelligence ingest via Part 10 RT-1 adapter"
        - "CRM event log append"
        - "daily-log commit via /plan-day or /close-day"
        - "lint scan advisory (no enforcement)"
        - "git commit with valid format token"
      requires_synchronous_owner: false
      batch_eligible: false
      auto_log: true

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  l1_target_latency: "≤4h same-session"
  l2_target_latency: "≤7d Friday batch window"
  l3_target_latency: "immediate auto-log"
  # Phase B partner forks override per fork's reaction time profile.
  # Multi-owner Phase B/C requires per-owner sla-taxonomy.<owner_id>.yaml fork pattern (NOT IMPLEMENTED Phase A).

# PHASE-B per-owner overrides supported via sla-taxonomy.<owner_id>.yaml fork pattern.
# NOT IMPLEMENTED Phase A; F.9 Bridge structural change ≥35% required at multi-owner activation.
```

[F4|G:Bundle 4 P9.3 SLA taxonomy|R-medium]

### §I.4 Multi-owner stub fields (NOT IMPLEMENTED; Phase B F.9 Bridge work)

Per IP-2 single-owner Phase A bounded + brigadier autocheck §6.8: Bundle 4 §I
declares multi-owner stub fields explicitly NOT IMPLEMENTED. Schema fields
commented out. Activation requires F.9 Bridge structural change ≥35% per Wave
A Ashby BOSC-A-T-X analysis.

| Stub field | File | Phase A status | Phase B activation requirement |
|---|---|---|---|
| `owner_id` (replaces `owner` string with enum) | daily-log.json | COMMENTED OUT | Per-fork `owners.yaml` enumeration; F.9 Bridge spec |
| `owners_aggregated[]` (multi-owner weekly review) | weekly-review.json | COMMENTED OUT | Multi-owner aggregation logic + per-owner attention budget |
| `sla-taxonomy.<owner_id>.yaml` fork pattern | .claude/config/ | NOT IMPLEMENTED | Per-owner SLA calibration; F.9 Bridge spec |
| `attention_budget_per_owner` | shared/state/kanban.json | DEFAULTS TO 20 (single-owner Phase A) | Per-owner cap value override |
| `multi-owner-conflict-resolution-policy` | new config | NOT DECLARED | F.9 Bridge spec mandates resolution policy |

Brigadier autocheck verifies: Phase A schema files contain stub field
references in commented-out form OR `// PHASE-B:` annotated lines; Phase B
activation requires F.9 Bridge document under
`design/F-9-Bridge-multi-owner-spec.md` (NOT YET CREATED).

### §I.5 Cross-Part schemas REFERENCED (not duplicated)

| Schema | Owner | Part 9 consumption |
|---|---|---|
| `awaiting-approval-packet.json` | Part 6b §I.4 (Bundle 1 LOCKED) | Draft-disposition `accept` items emit packets per this schema with `gate_class: draft_promotion` |
| `f-g-r.json` | Part 6a §I.1 (Bundle 1 LOCKED) | Every Part 9 emitted artefact carries f_g_r per this schema |
| `health-signal-schema.json` | Part 8 §I.1 (Bundle 3 LOCKED) | Part 9 health emissions conform |
| `task-return-packet.json` | Part 4 §I.1 (Bundle 2 LOCKED) | Cycle dispatch context referenced in afternoon-execution section |
| `project-retrospective-packet.json` | Part 7 §I.2 (Bundle 4 LOCKED) | Weekly review consumes for closed projects |
| `cross-fork-provenance.json` | Part 1 §I.1 (Bundle 1 + Bundle 4 supplement) | Phase B partner fork imports Part 9 schemas |

DRY enforced — schemas are NOT duplicated here.

---

## §J Operational Rituals

### J.1 Daily ritual

1. **Morning** (`/plan-day` skill invocation): owner authors morning_intent
   prose (appetite + 1-3 high-leverage tasks); agent populates frontmatter
   skeleton. Commit `[daily] plan: <YYYY-MM-DD>` via Part 1 §H.

2. **Afternoon** (cycle dispatch via Part 4): cycle_dispatch_summary populated
   by brigadier extraction from cycle task-return-packets. Surprises
   field captures unexpected events.

3. **Evening** (`/close-day` skill invocation): owner authors evening_reflection
   prose (what worked, what dropped, methodology candidates surfaced). Commit
   `[daily] eod: <YYYY-MM-DD>` via Part 1 §H.

### J.2 Weekly ritual (event-driven on Friday EOD OR Sunday SOD per owner pick)

1. Aggregate daily-logs since last weekly review.
2. Read `agents/<id>/strategies.md` for methodology candidates with
   `validated_in_cycles ≥ 2` predicate.
3. Compose draft-disposition table — one entry per accumulated draft from
   prior week. Owner classifies each: accept | iterate | discard.
4. Owner authors weekly_retrospective prose (5 questions: what worked / what
   blocked / what dropped / next-week appetite / methodology candidates).
5. SLA-tier review: compute compliance percentages; surface tier breaches.
6. For each accept-disposition methodology candidate: emit forward event to
   Part 5 §I.1 (Part 5 creates wiki/methodology/<rule-slug>-DRAFT.md and
   opens Part 6b draft_promotion gate per its own §I.1 logic).
7. For each accept-disposition draft: emit AWAITING-APPROVAL `gate_class:
   draft_promotion` packet to Part 6b for canonical promotion.
8. Commit `[review] weekly: <YYYY-Wnn>` via Part 1 §H.

### J.3 Monthly ritual (event-driven on month-end)

1. Aggregate weekly reviews from the trailing month.
2. Owner authors monthly_reflection_text prose (strategic synthesis +
   compound-learning input). IP-7 enforced.
3. Cycle_summary[] array auto-populated by agent extraction from weekly
   reviews + per-cycle task-return-packets.
4. Attention-budget utilisation report generated.
5. Commit `[review] monthly: <YYYY-MM>` via Part 1 §H.

### J.4 SLA-tier classification ritual

For every draft entering Part 9 intake:
1. Read `.claude/config/sla-taxonomy.yaml` event_examples per tier.
2. Match draft origin + draft type against examples; assign tier (L1/L2/L3).
3. If no clear match, default to L2 (conservative per FUNDAMENTAL §4.2).
4. Tag draft frontmatter with `sla_tier: <L1|L2|L3>`.
5. On promotion, Part 6b enforcement reads sla_tier and applies appropriate
   ack window (L1 same-session; L2 Friday batch; L3 auto-log).

### J.5 Attention-budget cap enforcement ritual

1. On every draft intake: check WIP count + new item count vs cap (20
   RUSLAN-LAYER).
2. If exceeded: emit AWAITING-APPROVAL `gate_class: stop_gate` to Ruslan;
   reject intake until ack.
3. Cap exceedance event logged to `swarm/wiki/log.md` (audit trail).

### J.6 Health-emission ritual

At each daily-log commit, weekly-review commit, monthly-reflection commit,
and on draft-disposition events, Part 9 calls
`swarm/lib/emit_health_signal()` with:
- `daily-log-creation-rate` (per /plan-day or /close-day commit);
- `weekly-review-completion-rate` (per weekly review commit);
- `draft-clearance-rate` (count of dispositioned drafts at weekly review);
- `l1-sla-compliance-rate` / `l2-sla-compliance-rate` / `l3-sla-compliance-rate`
  (per weekly review SLA tier review);
- `attention-budget-utilisation` (per intake event).

Health emissions conform to Part 8 §I.1 canonical health-signal schema.

### J.7-pre Commit-message format conventions for Part 9 events

All Part 9 emissions use these area tokens (per Part 1 §I.2 commit-format-tokens.json):

| Event | Commit-message pattern | Example |
|---|---|---|
| /plan-day morning intent commit | `[daily] plan: <YYYY-MM-DD>` | `[daily] plan: 2026-04-28` |
| /close-day evening reflection commit | `[daily] eod: <YYYY-MM-DD>` | `[daily] eod: 2026-04-28` |
| Weekly review commit | `[review] weekly: <YYYY-Wnn>` | `[review] weekly: 2026-W18` |
| Monthly reflection commit | `[review] monthly: <YYYY-MM>` | `[review] monthly: 2026-04` |
| Draft-disposition forwarding | `[review] forward: <draft-slug> (disposition=accept, gate=draft_promotion)` | `[review] forward: cyc-foundation-build-2026-04-28-bundle-4 (disposition=accept, gate=draft_promotion)` |
| Methodology candidate forward | `[methodology] candidate-forward: <rule-slug> (Part 5 §I.1)` | `[methodology] candidate-forward: shape-up-appetite-constraint (Part 5 §I.1)` |
| Priorities update | `[review] priorities: <YYYY-Wnn> (priority stack updated)` | `[review] priorities: 2026-W18 (priority stack updated)` |

Pre-commit hook (`pre-commit-format.sh`) verifies the area token exists in
Part 1 §I.2 commit-format-tokens.json schema; pattern conformance is best-
effort (no enforcement at Phase A).

### J.7 Methodology promotion forwarding ritual

Per weekly review:
1. Read `agents/<id>/strategies.md` for entries with `validated_in_cycles ≥ 2`.
2. Surface each entry in `methodology_candidates_surfaced[]` array.
3. Owner classifies disposition (accept | iterate | discard).
4. For accept: emit `methodology-promotion-forwarded` event to
   `comms/mailboxes/part-5.jsonl`. Part 5 §I.1 admits + creates DRAFT entry +
   opens Part 6b gate per its own logic.
5. For iterate: append revision_note to strategies.md entry; remains
   candidate state.
6. For discard: mark strategies.md entry with
   `dispositioned_discard: <weekly-review-id>` field.

---

### J.8 Phase B partner fork import ritual

When a Phase B partner forks Foundation:
1. Partner imports `shared/schemas/daily-log.json` + `shared/schemas/weekly-review.json`
   + `.claude/config/sla-taxonomy.yaml` (Foundation generic structure).
2. Partner DECLINES Foundation's RUSLAN-LAYER (specific cap value 20, specific
   SLA times, Russian-primary content patterns).
3. Partner populates own RUSLAN-LAYER values for partner's reaction-time
   profile.
4. Reconciliation_strategy applied per `cross-fork-provenance.json` D27
   promotion (Bundle 4 supplement 2):
   - `parent-wins` for IP-7 owner-authored predicate, IP-2 single-owner bounded
     invariant, 3-tier SLA structure, attention-budget cap mechanism.
   - `fork-wins` for cap value override, SLA time overrides, content-language
     patterns, owner identifier.
   - `manual-merge` for cross-cutting changes (e.g., new tier beyond L1/L2/L3).
5. If partner activates multi-owner case within fork (1 owner → 2+ owners
   within partner's instance): F.9 Bridge spec REQUIRED before schema field
   activation.

### J.9 OQ-MERGED-2 dissolve-test evidence (Bundle 4 = Cycle 2 of 3)

Part 9's contribution to dissolve-test evidence (per OQ-MERGED-2): weekly
review methodology candidate surfacing is an operation that ONLY Part 5
compound-phase logic can consume coherently (Part 3 KB MOC, Part 4 routing
table cannot extract methodology promotion candidates from agents/<id>/
strategies.md without invoking Part 5 §I.1 admissibility predicate). Each
weekly review with `methodology_candidates_surfaced` non-empty counts as 1
distinct dissolve-test evidence entry.

---

## §K Failure Modes

| ID | Failure | Detection | Response |
|---|---|---|---|
| K1 | Daily-log gap — working day with no daily-log commit | Part 8 `daily-log-creation-rate` SLI breach; alert routes via Part 9 §I.3 L2 tier | Investigate; surface in next weekly review; not a Tier 0 failure (single missed day acceptable) |
| K2 | Weekly review gap — calendar week with no weekly review commit | Part 8 `weekly-review-completion-rate` SLI breach (target 1/week); alert routes L1 (Tier 1 Strategic) | Halt new draft intake until weekly review committed (forces compound-loop fed) |
| K3 | Attention-cap exceedance attempt — agent attempts to add item beyond WIP=20 cap | swarm/lib/owner_attention_budget.check_attention_budget() rejects | Emit AWAITING-APPROVAL gate_class: stop_gate; require Ruslan ack to override |
| K4 | IP-7 violation — strategic prose authored by agent (git blame check fails) | Pre-commit hook / lint check on owner-authored predicate fields | Reject commit; require owner-authored prose |
| K5 | Provenance-free draft intake — draft submitted without sources: frontmatter | Part 9 H.1 intake_draft() rejects; notification to author | Author appends sources + re-submits |
| K6 | SLA tier mis-classification — L1 item batched as L2 (escapes same-session ack) | Part 8 alert when L1 item ack delay exceeds tier_definitions.l1_target_latency | Brigadier audit; reclassify; emit retrospective AWAITING-APPROVAL |
| K7 | Draft-disposition gap — accumulated drafts without disposition at weekly review | Part 9 weekly review schema validation: disposition coverage 100% required | Brigadier autocheck rejects; require disposition before weekly review commit |
| K8 | Methodology candidate surfacing miss — strategies.md entry with validated_in_cycles ≥ 2 not surfaced | Part 5 §I.1 emit-vs-Part-9-consume mismatch; Part 8 SLI on rate | Brigadier audit; manual surfacing; investigate why event missed |
| K9 | C4 nomenclature drift — `PhaseOf Part 6` reintroduced in §D | Brigadier autocheck §6.8; pre-commit hook on Part 9 architecture commits | Reject commit; restore `methodologically-uses Part 6` |
| K10 | Multi-owner accidental activation — owner_id field uncommented without F.9 Bridge spec | Pre-commit hook: if daily-log.json schema activates owner_id, requires F.9 Bridge spec presence | Reject commit; require F.9 Bridge spec at design/F-9-Bridge-multi-owner-spec.md |
| K11 | Draft archive deletion — archived draft hard-deleted | Pre-commit hook on drafts/archive/ paths; D-4 deontic violation | Reject commit; archive ≠ delete (FUNDAMENTAL §1 UC-J.2) |
| K12 | PARA-tier missing — daily-log/weekly-review without para_tier | Schema validation; pre-commit hook | Reject commit; require para_tier field |
| K13 | Monthly reflection automation — `monthly_reflection_text` populated by agent | Git blame on field's line range; agent commit detected | Halt-Log-Alert; revoke and require owner-authored prose |
| K14 | Appetite-overrun review skipped — projects with overrun not surfaced in weekly review appetite_actual_vs_planned | Schema validation; cross-check with Part 7 project records | Brigadier audit; force surfacing |
| K15 | Methodology candidate disposition drift — `weekly_disposition: accept` but no Part 5 forward emitted | Part 5 §A.5 ingestion absent for the candidate; Part 8 SLI on rate | Brigadier audit; manual forward emission |
| K16 | Daily-log frontmatter drift — required fields stripped on commit (e.g., para_tier removed) | Schema validation pre-commit hook; /lint --check-frontmatter Phase B | Reject commit; restore required fields |
| K17 | Weekly review draft-disposition skip — `iterate` disposition with no revision_note appended | Schema validation; weekly review commit hook | Reject commit; require revision_note for iterate disposition |
| K18 | SLA tier override silent — RUSLAN-LAYER override drift (e.g., L1 target_latency relaxed beyond Foundation default) | Pre-commit hook on `.claude/config/sla-taxonomy.yaml` ruslan_layer_overrides; AWAITING-APPROVAL `gate_class: stage_gate` required for overrides | Reject commit; require AWAITING-APPROVAL ack |
| K19 | F.9 Bridge spec missing at multi-owner activation — schema field activated without F-9 Bridge file | Pre-commit hook checks `design/F-9-Bridge-multi-owner-spec.md` exists before allowing daily-log.json schema activation of owner_id | Reject commit; require F-9 Bridge spec landing |
| K20 | Weekly-review draft-disposition coverage <100% — accumulated drafts not all dispositioned | Schema validation: count(draft_disposition_table[]) >= count(accumulated_drafts) | Reject commit; require coverage |

---

## §L Wave C Worklist Bullet Status

| Bullet | Status | Acceptance predicate | Evidence |
|---|---|---|---|
| **P9.1** Daily-log artefact schema | ✅ DONE | Schema structurally complete; ≥1 synthetic fixture; commit via Part 1 §H; PARA-tier tagged; IP-7 owner-authored predicate enforced | §I.1 + §J.1 ritual + §K K4 |
| **P9.2** Weekly review artefact schema with draft-disposition table (C2 producer side) | ✅ DONE | Schema structurally complete; draft-disposition table per fixture; methodology promotion surfaced via fixture | §I.2 + §J.2 ritual + §B.1 |
| **P9.3** 3-tier SLA taxonomy as canonical Foundation artefact | ✅ DONE | File at `.claude/config/sla-taxonomy.yaml`; 3 tiers declared; cross-ref Part 6b | §I.3 inline; physical file Phase F deliverable §8.3 |
| **C4 nomenclature fix** | ✅ DONE | §D every Part 6 reference uses `methodologically-uses` not `PhaseOf`; brigadier autocheck PASS | §D D-2 + D-3 + L9 + brigadier autocheck §6.8 |
| **IP-2 single-owner bounded** | ✅ DONE | §X declares single-owner Phase A; multi-owner stub fields §I (NOT implemented; Phase B F.9 Bridge); §6.8 autocheck PASS | §X + §I.4 stub fields |

---

## §M Wisdom Application Findings — Part 9

| Card / Source | Principle | Current state pre-loop | Improvement | Adopted? | Op vs Phi | Justification | Section edited |
|---|---|---|---|---|---|---|---|
| #1 Levenchuk SHSM-FPF | IP-7 writing-as-thinking — owner authors strategic prose | Wave A surfaced; not enforced | Add `owner_authored: true` predicate field on morning_intent + evening_reflection + monthly_reflection_text + weekly_retrospective; pre-commit git blame check (§A.1 + §K K4) | YES | OPERATIONAL | Phase A — schema field + pre-commit hook; structural enforcement of IP-7 anti-pattern | §I.1 + §I.2 + §A.1 + §K K4 + K13 |
| #2 Levenchuk SHSM-FPF | IP-2 single-owner bounded with F.9 Bridge | Wave A surfaced; not encoded structurally | Add §X declaration + §I.4 multi-owner stub fields with NOT IMPLEMENTED markers; §J.2 weekly review aggregates single-owner only; brigadier autocheck §6.8 | YES | OPERATIONAL | Phase A — fork-separation invariant + structural Phase B activation requirement | §X + §I.4 |
| #3 PM-Cagan-ShapeUp | Torres CDH continuous discovery — weekly customer touchpoint slot | Implicit | Add §F anti-scope: Torres CDH is RUSLAN-LAYER methodology library content; Foundation encodes only generic "opportunity intake" sub-function within weekly review (per Wave A OQ-MERGED-4) | YES | OPERATIONAL | Phase A — boundary declaration prevents Foundation creep | §F |
| #4 Stoic-Epistemic | Naval specific knowledge filter — L1 strategic (specific) vs L2/L3 (delegate-able) | Implicit in 3-tier SLA | Map L1 = strategic (specific knowledge); L2/L3 = delegate-able; declare in §I.3 sla-taxonomy.yaml event_examples | YES | OPERATIONAL | Phase A — explicit mapping clarifies tier semantics for classification ritual | §I.3 + §J.4 |
| #5 SRE-Observability | Toil < 50% of owner time | Implicit attention-budget cap | Add E-9 effect: attention-budget utilisation reported in monthly reflection (peaks, average, distribution) | YES | OPERATIONAL | Phase A — measurable outcome supports SLO-tracking | §E E-9 |
| #6 SRE-Observability | Blameless postmortem (Ch.15) | Implicit weekly retrospective | Map weekly_retrospective fields to postmortem culture (what worked / what blocked / what dropped — owner-authored, not finger-pointing) | YES (lite) | OPERATIONAL | Phase A — structural framing influences ritual content | §I.2 weekly_retrospective |
| #7 SRE-Implementing-SLOs | Burn-rate algebra for SLA tiers | Implicit | Add §I.3 sla-taxonomy.yaml inline structure analogous to burn-rate tiers (L1 = fast burn alert; L2 = medium; L3 = slow auto-log) | YES (lite) | OPERATIONAL | Phase A — analogous SLA tier structure inherits SRE-WB §2 algebra | §I.3 |
| #8 Knowledge-Mgmt-Forte-PARA | PARA tagging | Bundle 2 P2.2 mandatory | Daily-log = Area; weekly-review = Area; monthly-reflection = Resource; drafts inherit from origin | YES | OPERATIONAL | Phase A — schema field; cross-bundle consistency | §I.1 + §I.2 + §C |
| #9 Stoic-Epistemic | Dichotomy-of-control | Implicit | Add framing prose to §F about owner-control of strategic; agents-control-of-extraction. Declined as PHILOSOPHICAL framing without operational consequence | NO | PHILOSOPHICAL | Pure framing prose; no schema field / no failure mode / no SLO. DEFER to Wave D documentation pass | n/a |
| #10 Compounding-Engineering | Plan/Work/Review/Compound main loop — Part 9 owns Plan + Review boundaries | Implicit | Map daily-log = Plan + Work boundary; weekly-review = Review + Compound boundary (forwards to Part 5) | YES | OPERATIONAL | Phase A — explicit cross-reference makes the loop auditable | §J.1 + §J.2 |
| #11 FPF A.14 typed edges | Typed dependency edges | Wave A used `PhaseOf Part 6` (incorrect) | Apply C4 nomenclature fix verbatim — `methodologically-uses Part 6` per Wave A dependency-graph §3.4; brigadier autocheck §6.8 | YES | OPERATIONAL | Phase A — typed-edge discipline + C4 fix | §D + §L9 |
| #12 FUNDAMENTAL §3.2.6 | Attention-budget cap | Bundle 1 baseline | Add §E L2 hard Law + §K K3 detection + §J.5 enforcement ritual | YES | OPERATIONAL | Phase A — operationalises constitutional anchor | §E L2 + §K K3 + §J.5 |
| #13 FUNDAMENTAL §4.2-§4.3 | 3-tier SLA structure | Constitutional | Canonicalise as `.claude/config/sla-taxonomy.yaml` Foundation artefact with RUSLAN-LAYER override pattern | YES | OPERATIONAL | Phase A — Foundation artefact materialised; fork-portable | §I.3 |

**Aggregate adoption:** 12 YES (10 OPERATIONAL + 2 lite OPERATIONAL) / 1 NO
(PHILOSOPHICAL deferred). **Operational ratio: 12/12 = 100%** (lite OPERATIONAL
counted as OPERATIONAL since it changes ritual structure). Bundle 4 ≥85% target
MET.

[F4|G:Wisdom Loop applied to Part 9|R-medium]

---

## §N Provenance

**Constitutional baseline:**
- Bundle 1 LOCKED parts: Part 1 (§H commit interface), Part 6a (§I.1 F-G-R F8),
  Part 6b (§I.4 awaiting-approval-packet F8 + §I.3 blast-radius 4-tier).
- Bundle 2 LOCKED parts: Part 4 (§I.1 task-return-packet — afternoon execution
  reference).
- Bundle 3 LOCKED parts: Part 5 (§A weekly review surfaces methodology
  candidates), Part 8 (§I.1 canonical health-signal schema).
- Bundle 4 LOCKED parts (this bundle): Part 7 (§B project-retrospective-packet
  consumed in weekly review), Part 10 (§F C3 Phase A external; §I CRM data
  model — weekly review surfaces stuck contacts via /crm-stuck).

**RUSLAN-ACK records:**
- Bundle 1 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md].
- Bundle 1 supplement [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md].
- Bundle 2 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md].
- Bundle 3 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md].

**Wave A:**
- Interface card [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md].
- Worklist §2 P9 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md].
- Critic gate §6 item 2 IP-2 + §3.4 C4 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md].
- Dependency graph §3.4 C4 nomenclature fix [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md].

**Wave B consultants:**
- levenchuk-shsm-fpf.md (IP-2 + IP-7) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md].
- product-management-cagan-shape-up.md (Torres CDH) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md].
- sre-observability.md (toil < 50%; postmortem) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md].
- stoic-epistemic.md (Naval specific knowledge) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md].
- knowledge-management-karpathy-luhmann-matuschak.md (PARA) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md].

**Library-direct supplement:**
- Google SRE Book Ch.6 + Ch.15 [src:raw/books-md/sre/google-sre-book.md].
- Google SRE Workbook Ch.2 burn-rate algebra [src:raw/books-md/sre/google-srewb-implementing-slos.md].

**FUNDAMENTAL anchors:**
- §2.5 weekly cadence; §2.6 daily ops; §3.2.6 attention-budget cap; §4.2-§4.3
  3-tier SLA; §6.2 founder agency [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md].

**FPF:**
- IP-2 bounded context with F.9 Bridge (§5.2); IP-7 writing-as-thinking (§5.7);
  A.6.B L/A/D/E; A.14 typed edges [src:design/JETIX-FPF.md].

**Existing operational baseline:**
- `daily-log/` directory (1 file currently per AUDIT) [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md].
- `/plan-day`, `/close-day` skills [src:CLAUDE.md:Skills].
- `shared/state/kanban.json`, `shared/state/priorities.json`.

---

## §X Foundation vs RUSLAN-LAYER (FINAL CLOSURE per OQ-MERGED-3)

### Foundation generic (transferable to any single-owner knowledge-work fork)

| Category | Foundation invariant |
|---|---|
| Daily-log schema structure | YAML frontmatter + 3 sections (morning intent / afternoon execution / evening reflection); IP-7 owner-authored predicate enforcement |
| Weekly review schema structure | YAML frontmatter + draft-disposition table + retrospective + methodology promotion surfacing + SLA-tier review |
| Monthly reflection schema structure | YAML frontmatter + cycle_summary + monthly_reflection_text (owner-authored) |
| 3-tier SLA structure | L1 strategic / L2 tactical / L3 routine; structural ordering; mapping to blast-radius tiers |
| Attention-budget cap mechanism | WIP cap + intake check + Halt-Log-Alert on exceedance + AWAITING-APPROVAL gate_class: stop_gate enforcement |
| Draft-disposition table mechanic | accept | iterate | discard classification + rationale + action_taken; C2 PRODUCER side |
| Methodology candidate surfacing logic | Part 5 strategies.md `validated_in_cycles ≥ 2` predicate; weekly classification; forward to Part 5 §I.1 on accept |
| PARA tier discipline | Daily-log = Area; weekly-review = Area; monthly-reflection = Resource |
| IP-7 owner-authored predicate | Schema-level field with git blame validation; structural anti-pattern enforcement |
| Schema files | `daily-log.json`, `weekly-review.json` (Phase B physical generation per OQ-MERGED-5 specify-and-stub) |
| Config file | `.claude/config/sla-taxonomy.yaml` Foundation generic structure |
| Cadence rule for daily | Event-driven on /plan-day OR /close-day skill invocation |
| Cadence rule for weekly | Event-driven on Friday EOD OR Sunday SOD per owner pick (calendar trigger, not gating) |
| C4 nomenclature | Part 9 `methodologically-uses Part 6` (NOT `PhaseOf Part 6`) — per Wave A dependency-graph §3.4 |

### RUSLAN-LAYER (Ruslan's Jetix Phase A specific bindings)

| Category | RUSLAN-LAYER value |
|---|---|
| Specific owner | `ruslan` (Berlin, Germany) |
| Specific attention-budget cap value | 20 (per Manager rule — RUSLAN-LAYER specific value) |
| Specific L1 SLA time | ≤4h same-session (RUSLAN-LAYER override) |
| Specific L2 SLA time | ≤7d Friday batch window (RUSLAN-LAYER override) |
| Specific L3 SLA time | immediate auto-log (RUSLAN-LAYER override) |
| Russian-primary content patterns | All Ruslan's daily-log + weekly-review prose in Russian primary; English/German for tooling and cross-cultural references |
| Specific morning-intent template | Ruslan-specific structure for high-leverage tasks (Russian phrasing patterns) |
| Specific weekly review timing | Ruslan picks Friday EOD (RUSLAN-LAYER value); other instances pick differently |
| Specific monthly reflection scope | Ruslan's strategic context — Berlin-based AI consultancy; DACH market focus |
| Specific draft-disposition rationales | Ruslan's domain-specific rationales (consulting / AI tools / DACH market context) |

**F.9 Bridge requirement (per FPF §5.2 IP-2 + Wave A Ashby BOSC-A-T-X analysis).**
Phase A is bounded to single-owner Jetix. Multi-owner Phase B/C requires
**structural change ≥35%** per Ashby variety analysis: 1 owner → 2+ owners
within same Jetix instance triggers F.9 Bridge structural change. Concretely:
- Daily-log schema requires `owner_id` field (currently commented out); per-
  owner aggregation logic.
- Weekly review requires `owners_aggregated[]` field; per-owner
  draft-disposition + per-owner methodology candidate surfacing.
- SLA taxonomy requires per-owner calibration via `sla-taxonomy.<owner_id>.yaml`
  fork pattern.
- Attention-budget cap becomes per-owner.

**Phase B activation event**: sustained partner onboarding signal (1 owner →
2+ owners with >2 weeks operational evidence); F.9 Bridge work scoped at that
point; Phase A operates SINGLE-OWNER until that event.

**F.9 Bridge file MANDATORY before activation**: `design/F-9-Bridge-multi-owner-spec.md`
(NOT YET CREATED; pre-commit hook on schema file activation rejects until
this file lives).

[F4|G:Bundle 4 Part 9 §X final closure|R-medium — pending Ruslan ack]

---

*End of Part 9 architecture document.*
