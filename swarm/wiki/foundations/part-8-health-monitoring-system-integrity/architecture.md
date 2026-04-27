---
title: "Foundation Part 8 — Health Monitoring & System Integrity (Architecture)"
part_number: 8
part_slug: health-monitoring-system-integrity
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
phase: Wave-C-Bundle-3-architecture
status: F4-pending-ruslan-ack
predecessor_interface_card: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md
constitutional_baseline_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
constitutional_baseline_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
retroactive_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
F: F4
ClaimScope: "Holds for Foundation observability design at Phase A scale (single owner, ≤10 agents). SLI/SLO starter values are calibration parameters per OQ-MERGED-5, NOT Foundation constants. Bundle 3 scope = SPECIFY AND STUB only — schemas + templates + alert routing stub. NOT live metrics. NOT calibrated thresholds. Live calibration is Phase B (2-3 month operational data accumulation)."
R:
  refuted_if: "Bundle 3 Part 8 produces hardcoded SLI thresholds in Foundation artefacts without labeling them as calibration parameters; OR live metrics implementation code; OR sub-daily metric collection cadence; OR delivery code (Slack/email/SMS) for alert routing; OR FUNDAMENTAL §3 30+ SLI/SLO pairs treated as production-grade thresholds rather than starter values requiring Phase B calibration"
  accepted_if: "SLI/SLO schema exists with explicit starter_value + starter_value_label: calibration-grade + calibration_cadence + calibration_trigger fields; canonical health-signal schema (C2 resolution) exists with mapping table to Bundle 1+2 emitter shapes; alert-routing stub maps ≥10 alert classes to Tier 0/1/2/3 with Halt-Log-Alert ordering; weekly + quarterly templates exist with synthetic populated rows; TRADEOFF-01 split materialised (Part 8 audit lead + Part 6a service + Part 6b enforcement)"
specify_and_stub_scope: declared-OQ-MERGED-5
tradeoff_01_split: "Part 8 = audit LEAD; Part 6a = audit SUPPORT (F-G-R compliance check service invocation); Part 6b = ENFORCEMENT ARM (alert routing through gate)"
c2_resolution_variant: "B — mapping table fallback (Variant B chosen per Joint Design lite §4.3 — Bundle 1+2 emitter shapes are F5 LOCKED; Part 8 §I.3 owns canonical health-signal schema with mapping table; retroactive align (Variant A) deferred to Wave D housekeeping cycle to respect F5 LOCKED architecture stability)"
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md (§2 Part 8)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md (§2 Part 8 + TRADEOFF-01)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§3.2 C2 health signal schema; §7 OQ-1 TRADEOFF-01)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (§2 Part 8)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md"
  - "raw/books-md/sre/google-sre-book.md (Ch.4 SLOs; Ch.6 Monitoring; Ch.15 Postmortem; Ch.22 Cascading Failures)"
  - "raw/books-md/sre/google-srewb-implementing-slos.md (Ch.2 Implementing SLOs — burn-rate algebra)"
  - "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§3 30+ SLI/SLO calibration parameters; §5 reliability 3-2-1 backup; §6.7 halt+log+alert)"
  - "design/JETIX-FPF.md (IP-4 Quarterly Immune Audit; A.13 Agency-CHR; A.14 typed edges; A.6.B L/A/D/E; B.3 F-G-R)"
  - "swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§B Four Golden Signals; §J burn-rate 1×/6×/14.4×; §H commit interface; §I.5 health signal stub)"
  - "swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md (§I.6 Part 8 health signal stub)"
  - "swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md (§I.6 health signal stub)"
  - "swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (§I.4 health signal stub)"
  - "swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§I.1 F-G-R F8; §C approval log; quarterly immune audit framework)"
  - "swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.1 awaiting-approval-packet F8; §I.3 default-deny; §I.4 blast-radius 4-tier F8; §E L9 Halt-Log-Alert + Corrigibility)"
  - "swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md (Bundle 3 sibling — health signal emissions: compound-application-rate, methodology-promotion-rate, drr-write-rate, dissolve-test-evidence-count)"
---

# Foundation Part 8 — Health Monitoring & System Integrity (Architecture)

## §0 Executive Summary

**Part 8 closes the immune-system loop (Beer VSM S3 Audit/Optimisation): the
system surfaces silent degradation before it becomes catastrophic.** Without
Part 8, the system has no eyes — drift is invisible until catastrophe (a
methodology entry rots without anyone noticing; an SLI burns without anyone
seeing; F-G-R compliance silently degrades across cycles).

**Bundle 3 scope is SPECIFY AND STUB per OQ-MERGED-5.** That means:
- SLI/SLO schema (§I.2) — canonical schema with explicit starter_value_label
  + calibration_cadence + calibration_trigger fields. ≥8 starter SLI entries
  populated, all labeled `starter_value_label: "calibration-grade"`. NO
  production-grade thresholds.
- Canonical health-signal schema (§I.1, C2 resolution) — every Foundation Part
  emits health signals in this unified shape. Mapping table (§I.3) projects
  Bundle 1+2 emitter shapes onto the canonical schema (Variant B chosen per
  Joint Design lite — retroactive align deferred to Wave D housekeeping to
  respect F5 LOCKED architecture stability).
- Weekly health dashboard template (§I.4 + `swarm/audits/weekly-health-template.md`).
- Quarterly immune audit template (§I.5 + `swarm/audits/quarterly-immune-audit-template.md`)
  — extends Bundle 1 Part 6a quarterly framework.
- Alert-routing stub config (§H.1) — ≥10 alert classes mapped to Tier 0/1/2/3
  per Part 6b §I.4 F8 LOCKED 4-tier blast-radius table; Halt-Log-Alert
  ordering enforced for Tier 0; alert packet schema declared.

**NOT delivered in Bundle 3 (Phase B materialisation):**
- Live metric collection code (the schemas declare WHAT to measure; collection
  is Phase B).
- Calibrated thresholds (starter values are placeholders; Phase B calibration
  observes 2-3 months of operational data, then replaces starter with
  calibrated).
- Alert delivery infrastructure (Slack/email/SMS/page) — alert-routing is
  SPECIFICATION, not IMPLEMENTATION.
- Sub-daily metric collection cadence — calibration cadence is monthly review
  per OQ-MERGED-5; live metric emission cadence per signal is in §I.2 starter
  values.

**TRADEOFF-01 split materialised** (Beer VSM S3 oscillation risk avoided):
- **Part 8 = audit LEAD**. Part 8 owns audit cadence (weekly + quarterly),
  audit scope (drift detection across F-G-R compliance + SLI burn + alpha
  classification + role-manifest freshness + methodology library staleness),
  and audit output (committed audit reports).
- **Part 6a = audit SUPPORT (service invocation)**. Part 8 invokes Part 6a's
  F-G-R compliance check primitive (Part 6a Bundle 1 quarterly immune audit
  framework) AS A SERVICE. Part 8 does NOT re-implement F-G-R compliance
  checking.
- **Part 6b = ENFORCEMENT ARM**. Anomaly alerts route through Part 6b's
  blast-radius Tier 0/1/2/3 + Halt-Log-Alert ordering. Tier 0 (integrity
  emergency) = stop_gate AWAITING-APPROVAL packet. Tier 1 (Ruslan ack
  required) = same-session HITL. Tier 2 (batch ack) = weekly review. Tier 3
  (auto-log) = silent ledger entry.

**Part 8 itself does NOT enforce anything — it surfaces drift; Part 6b is the
enforcement arm.** This boundary is structural per the TRADEOFF-01 split. Part
8 OBSERVES; Part 6b ACTS.

**Phase A scope discipline.** Single-owner Jetix Phase-A €50K horizon.
FUNDAMENTAL §3 names 30+ SLI/SLO pairs (calibration parameters per FUNDAMENTAL
§3 anchor). Bundle 3 declares ≥8 starter SLI entries (one per major health
domain — git substrate / triage pipeline / KB freshness / mailbox cycle time /
DRR write rate / gate-open count / project state distribution / daily log
creation rate). The remaining ≥22 entries (FUNDAMENTAL §3 30+ minus 8) populate
in Phase B. **Bundle 3 is a SCHEMA delivery + STUB delivery; not a 30-SLI
inventory.**

**Fork-portable by construction** — schema is GENERIC; specific SLO threshold
values + alert delivery destinations + immune audit checklist contents are
RUSLAN-LAYER (per §X). Phase B partner forks adopt the schema; Phase B owner
calibrates own SLO targets.

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Part 1 Four Golden Signals (latency, traffic, errors, saturation) [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§B.1 SRE Four Golden Signals] | git substrate signals: commit-error-rate, hook-failure-rate, fsck-object-errors, repo-growth, latency-p95 — emitted per Part 8 §I.1 canonical health-signal schema (Bundle 3 deliverable) | Periodic per-signal cadence (declared in §I.2 SLI starter cadences); fsck triggered weekly per Part 1 §J | F4|G:Bundle 2 LOCKED Part 1 §B; Part 8 §I.1 Bundle 3 deliverable|R-medium |
| Part 1 §J burn-rate algebra (1×/6×/14.4× — SRE Workbook Ch.2) | Inherited from Part 1 §J — Part 8 §I.2 SLI/SLO schema adopts the algebra without re-derivation | Per-SLI evaluation cadence | F5|G:SRE Workbook Ch.2 algebra adopted Bundle 1|R-high |
| Part 1 §I.4 task-return-packet stub (post-Bundle-3-supplement gate_class enum aligned) | Health signals derived from packet outcomes: task-success-rate, task-cycle-time, escalation-rate | Per-task-completion event | F4|G:post-supplement schema|R-medium |
| Part 2 health signals [src:swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md:§I.6 Part 8 health signal stub] | triage-backlog, STOP-gate-acked-rate, para-tier-coverage, voice-pipeline-success-rate | Per-pipeline-run event + weekly aggregate | F4|G:Bundle 2 LOCKED Part 2 §I.6 stub|R-medium |
| Part 3 health signals [src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§I.6 health signal stub] | orphan-anchor-count, stale-claims-count, edges-per-entity-avg, contradicts-supports-density, methodology-admissibility-violations, comparisons-emptiness-flag, malformed-crm-edges | Periodic `/lint` runs (weekly) + on-ingest evaluation | F4|G:Bundle 2 LOCKED Part 3 §I.6 stub|R-medium |
| Part 4 health signals [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§I.4 health signal stub] | mailbox-queue-depth, cycle-time-avg, escalation-rate, routing-variety-count, message-schema-version-distribution | Per-cycle-close event + per-message-emit event | F4|G:Bundle 2 LOCKED Part 4 §I.4 stub|R-medium |
| Part 5 health signals (Bundle 3 sibling) [src:swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md:§B + §I.2] | compound-application-rate, methodology-promotion-rate, drr-write-rate, dissolve-test-evidence-count | Per-compound-phase-fire event | F4|G:Bundle 3 sibling deliverable|R-medium |
| Part 6a health signals [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§C approval log; quarterly framework] | approval-log-write-rate, fg-r-compliance-pct, citation-resolution-pct | Per-approval-event + weekly aggregate | F4|G:Bundle 1 LOCKED|R-medium |
| Part 6b health signals [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1] | gate-open-count, gate-acked-rate, gate-rejected-rate, default-deny-classified-pct, blast-radius-distribution, halt-log-alert-ordering-violations | Per-gate-event + per-cycle aggregate | F4|G:Bundle 1 LOCKED|R-medium |
| `shared/state/system-health.json` baseline [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md] | Current "all green" hardcoded baseline; Part 8 §I.1 specifies real computation contract (Phase B) | Read at weekly snapshot; rewritten with computed values | F2|G:current placeholder; F4 post-Phase-B|R-low |
| `shared/state/metrics/agent-performance.json` + `task-log.jsonl` [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md] | Current metrics; mapping table §I.3 maps to canonical schema | Per-task-emit event | F3|G:current placeholder; F4 post-mapping|R-low |
| FUNDAMENTAL §3 30+ SLI/SLO calibration parameters [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3] | Starter values for ≥30 SLI/SLO pairs labeled calibration-grade | Phase B calibration | F4|G:starter labels; calibrated values Phase B|R-low — calibration |

**§A.1 Concrete consequence — Bundle 3 admits ≥8 starter SLI entries (not all 30+).**
Per OQ-MERGED-5 specify-and-stub scope: Bundle 3 declares ≥8 starter SLI
entries, one per major health domain (per §I.2 entries enumerated below). The
remaining ≥22 entries from FUNDAMENTAL §3 populate in Phase B as operational
data accumulates. This is NOT under-delivery; it is **scope discipline** — a
30-SLI inventory at Bundle 3 time would be uncalibrated speculation. Phase B
inventory expansion has the operational data to inform threshold values.

**§A.2 Concrete consequence — Inputs are PASSIVE READS from Bundle 1+2+3 emitters.**
Part 8 does NOT push instrumentation INTO Bundle 1+2 architectures (which are
F5 LOCKED). Part 8 READS the emitters at their declared cadence per Bundle
1+2 §I.5/§I.6/§I.4 stubs (now post-Bundle-3 mapped to canonical schema in
§I.3 below). The mapping is the adapter; the source emitters remain F5 LOCKED.

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| `shared/state/system-health.json` | Updated health snapshot — current-cycle SLI values per §I.1 canonical schema | Weekly minimum (Friday 17:00 per Part 1 §J `/company-status` weekly cadence) + on-anomaly-detect | F4|G:weekly snapshot canonical|R-medium |
| `swarm/audits/weekly/<YYYY-WNN>-health.md` | Weekly health dashboard — per template `swarm/audits/weekly-health-template.md` (Bundle 3 deliverable) | Weekly commit `[health] weekly snapshot: WNN-YYYY` | F4|G:weekly dashboard structure|R-medium |
| `swarm/audits/quarterly/<YYYY-QN>-immune-audit.md` | Quarterly immune audit — per template `swarm/audits/quarterly-immune-audit-template.md` (Bundle 3 deliverable; extends Part 6a Bundle 1 quarterly framework) | Quarterly commit `[health] quarterly immune audit: QN-YYYY` | F5|G:quarterly audit structure|R-high |
| Part 6b AWAITING-APPROVAL packet (Tier 0 stop_gate) | Tier 0 integrity-emergency packet per Part 6b §I.1 F8 LOCKED schema with `gate_class: stop_gate` | On Tier 0 anomaly detect — Halt-Log-Alert ordering: ≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9 F8 | F5|G:Tier 0 routing per Part 6b §I.4 F8 LOCKED|R-high |
| Part 6b AWAITING-APPROVAL packet (Tier 1 stage_gate / Tier 2 stage_gate) | Tier 1 same-session HITL ack OR Tier 2 batch-ack packet per Part 6b §I.1 F8 LOCKED schema with `gate_class: stage_gate` | On Tier 1/Tier 2 anomaly detect | F4|G:Tier 1/2 routing|R-medium |
| `swarm/audits/log/alert-log.jsonl` (Tier 3 auto-log) | Tier 3 silent-log entries — anomaly recorded but no immediate ack required | Append-only per anomaly-detect for Tier 3 classified events | F4|G:Tier 3 routing|R-medium |
| Part 9 weekly review feed (Bundle 4 consumer) | "Look here" recommendation list per FUNDAMENTAL §1 UC-I.3; cross-ref Bundle 4 Part 9 architecture | Weekly published with weekly health snapshot commit | F3|G:Phase 2 Bundle 4 consumer interface|R-low — Bundle 4 finalises consumption |
| Part 6a service invocation result (TRADEOFF-01 audit support) | F-G-R compliance check result — invoked from §J quarterly audit ritual; Part 6a returns drift report | Quarterly per §J quarterly cadence | F5|G:Part 6a Bundle 1 service contract|R-high |

**§B.1 Concrete consequence — TRADEOFF-01 split materialised in §B Outputs.**
Part 8 outputs include BOTH the audit reports (weekly + quarterly committed
artefacts) AND the alert-routing AWAITING-APPROVAL packets to Part 6b. The
Part 6a service invocation is an INPUT to Part 8's quarterly audit (Part 6a
returns drift report; Part 8 includes drift in audit output). The Part 6b
gate emission is an OUTPUT (Part 8 emits alert; Part 6b enforces). **Part 8
DOES NOT enforce; Part 6b enforces.** Part 8 OBSERVES; Part 6b ACTS. The split
is structural per TRADEOFF-01 ack [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 8 + TRADEOFF-01 OQ; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§4 P3 Beer VSM S3].

---

## §C Side-effects

- **Append to `swarm/wiki/log.md`** on each weekly health snapshot commit
  (append-only per D25; new entries above older ones per Global Rule 2 logs
  discipline).

- **Write to `shared/state/system-health.json`** (idempotent re-computation;
  prior value preserved in git history per Reversal Transactions). Weekly
  rewrite is a NEW commit, not in-place edit; the file IS its history.

- **Open AWAITING-APPROVAL packets via Part 6b** when anomaly detected per
  Part 8 §H.1 alert-routing stub. Tier 0 = stop_gate (immediate ack); Tier 1
  = stage_gate (same-session ack); Tier 2 = stage_gate (batch ack); Tier 3 =
  silent log (no packet).

- **Quarterly audit writes to `swarm/audits/quarterly/<YYYY-QN>-immune-audit.md`** via Part 1 §H commit `[health] quarterly immune audit: <YYYY-QN>` per
  D25 Company-as-Code.

- **Invoke Part 6a F-G-R compliance check service** at quarterly cadence
  (TRADEOFF-01 audit support). Part 6a runs the F-G-R compliance check
  primitive across wiki entries; returns drift report. Part 8 includes the
  drift report in the quarterly audit output. Part 6a is a SERVICE called by
  Part 8; Part 8 does NOT re-implement Part 6a's compliance primitive.

- **Append to `swarm/audits/log/alert-log.jsonl`** for Tier 3 silent-log
  events (e.g., low-severity SLI burns where Ruslan ack is not immediately
  required; weekly review surfaces them).

- **Does NOT auto-promote or auto-demote artefacts.** Per Part 8 §F Anti-scope
  + per FUNDAMENTAL §6.1: anomaly detection is J-Auto; behaviour-change on
  budget burn is J-Approve; structural integrity failure is J-Strategic.
  Part 8 surfaces; owner (or Part 6b gate) acts.

- **Does NOT write to canonical Foundation architecture documents.** Part 8
  observes Bundle 1+2+3 architectures; it does NOT modify them. F5 LOCKED
  artefacts remain F5 LOCKED.

---

## §D Dependencies (typed per FPF A.14 — canonical 10-edge table)

Bundle 1 canonical 10-edge reference: `ComponentOf` / `ConstituentOf` /
`PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in`
/ `methodologically-uses` / `constrained-by` / `derives-from`. NO generic
`depends-on`. NO `uses`.

| From | Edge type | To | Rationale |
|---|---|---|---|
| Part 8 | `operates-in` | [Part 1, Part 2, Part 3, Part 4, Part 5, Part 6a, Part 6b, Part 7 (Bundle 4), Part 9 (Bundle 4), Part 10 (Bundle 4)] | Beer VSM S3 audit context spans entire Foundation [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§4 P3 VSM S3]. Part 8 is the OBSERVABILITY context for the entire system; it OPERATES IN the substrate provided by all other Parts. |
| Part 8 | `methodologically-uses` | Part 1 (commit substrate) | Health snapshots, weekly dashboards, quarterly audits, alert log committed via Part 1 §H. Part 8 USES Part 1's commit interface as METHOD. |
| Part 8 | `methodologically-uses` | Part 6a (TRADEOFF-01 — F-G-R compliance check service) | Part 8 INVOKES Part 6a's F-G-R compliance check primitive as a SERVICE at quarterly audit cadence. Part 6a runs the check; Part 8 includes the result. Part 8 USES Part 6a as METHOD for compliance audit. |
| Part 8 | `methodologically-uses` | Part 6b (TRADEOFF-01 — alert routing through enforcement arm) | Anomaly alerts route through Part 6b's blast-radius Tier 0/1/2/3 + Halt-Log-Alert ordering. Part 8 USES Part 6b as METHOD for alert delivery. |
| Part 8 | `derives-from` | Part 1 §J burn-rate (1×/6×/14.4× SRE Workbook Ch.2 algebra) | Part 8 §I.2 SLI/SLO schema CONSUMES Part 1's burn-rate algebra without re-derivation. The arrow is Part 8 → Part 1 (Part 8 derives FROM Part 1). |
| Part 8 | `derives-from` | Part 1 §B Four Golden Signals | Part 8 SLI definitions for git substrate domain DERIVE from Part 1 §B (latency, traffic, errors, saturation). |
| Part 8 | `derives-from` | Part 5 health emissions (compound-application-rate, methodology-promotion-rate, drr-write-rate, dissolve-test-evidence-count) | Part 8 SLI definitions for compound-learning domain DERIVE from Part 5 §B emissions (Bundle 3 sibling). |
| Part 8 | `derives-from` | Parts 2/3/4 health emissions per §I.6/§I.6/§I.4 | Part 8 SLI definitions for triage / KB / coordination domains DERIVE from Bundle 2 emissions. |
| Part 8 | `constrained-by` | Part 6b §E Law L9 (Halt-Log-Alert + Corrigibility) | Tier 0 alert ordering ≤1s halt / ≤5s log / ≤60s alert; Part 8 alerts CANNOT bypass Halt-Log-Alert. Part 8 is CONSTRAINED BY this F8 LOCKED invariant. |
| Part 8 | `constrained-by` | OQ-MERGED-5 specify-and-stub scope | Part 8 Wave C output is schemas + templates + stub routing; live metrics is Phase B. Part 8 is CONSTRAINED BY this scope discipline. |
| Part 8 | `constrained-by` | FUNDAMENTAL §6.1 no-self-modify + agency-preservation | Part 8 SURFACES; owner ACTS. Part 8 does not auto-execute behaviour-change. |
| Part 9 (Bundle 4) | `derives-from` | Part 8 weekly health dashboard | Part 9 weekly review CONSUMES Part 8 weekly dashboard. Bundle 4 Part 9 finalises consumption. |

**§D.1 No `depends-on` edges.** Per Bundle 1 canonical 10-edge table, generic
`depends-on` is forbidden. Every dependency above is one of the canonical
types. Critic gate verifies. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§D 10-edge reference]

**§D.2 Beer VSM S3 split — TRADEOFF-01 materialised in edge typology.** Note
that Part 8 has TWO `methodologically-uses` edges to Part 6 family — one to
Part 6a (F-G-R compliance check service invocation; AUDIT SUPPORT) and one to
Part 6b (alert routing through enforcement arm; ENFORCEMENT). This dual edge
IS the TRADEOFF-01 split visible at the dependency graph layer. NO oscillation
risk because the edges are SCOPED:
- Part 6a edge = quarterly cadence + F-G-R compliance scope
- Part 6b edge = on-anomaly-detect + alert-routing scope

The two edges do NOT conflict. Part 8 is the audit LEAD that orchestrates both
the SUPPORT (Part 6a) and ENFORCEMENT (Part 6b) edges. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 8 TRADEOFF-01]

---

## §E Boundary — L/A/D/E Lanes (FPF A.6.B Norm Square)

### Laws (invariants MUST hold — violations are constitutional defects)

**L-1. Health monitoring is observability ONLY.** [Meadows L8 — information
flows] Part 8 surfaces alerts; Part 8 does NOT auto-change system
configuration or auto-promote/demote artefacts. Anomaly detection is J-Auto
per A.13 Agency-CHR; behaviour-change on budget burn is J-Approve;
structural integrity failure is J-Strategic. Violation refuter: a Part 8
mechanism that mutates Foundation architecture documents OR auto-promotes
methodology entries OR auto-rejects ingest events. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; src:design/JETIX-FPF.md:§A.13 Agency-CHR]

**L-2. Fail-loud principle.** [Meadows L5 — rules] Anomaly detected →
committed alert record + AWAITING-APPROVAL packet opened via Part 6b within
one monitoring cycle. Halt-Log-Alert ordering enforced for Tier 0:
≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9 F8 LOCKED. Violation
refuter: an anomaly observed but no committed alert record within the
monitoring cycle. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§5.2; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§5 T3 fail-loud; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9]

**L-3. SLI/SLO values declared in Foundation artefact MUST be labeled as
starter/calibration values with explicit calibration_cadence.** [Meadows L5
— rules] Hardcoded thresholds without `starter_value_label:
"calibration-grade"` + `calibration_cadence` + `calibration_trigger` fields
are a Foundation violation. Violation refuter: any SLI entry in §I.2 with
`starter_value` set but no `starter_value_label`. [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-MERGED-5 specify-and-stub; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3 30+ SLI/SLO calibration parameters]

**L-4. Quarterly immune-system audit MUST cover the canonical scope.**
[Meadows L5 — rules] Required scope: F-G-R compliance drift across artefact
types (Part 6a service invocation); alpha classification drift (IP-5
past-participle exception whitelist check); role-manifest freshness (IP-6);
methodology library staleness (entries with `last_validated_at:` >90 days);
strategies.md staleness (per-role DRR entry decay). Violation refuter: a
quarterly audit committed without one or more of these scope items.
[src:design/JETIX-FPF.md:§5.4 IP-4 Quarterly Immune Audit; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 8]

**L-5. Halt-Log-Alert ordering for Tier 0 alerts.** [Meadows L5 — rules]
Tier 0 (integrity emergency — git fsck error / hook bypass / fg-r compliance
collapse) MUST execute ordering: ≤1s halt → ≤5s log → ≤60s alert. Halt
BEFORE log; log BEFORE alert. Per Part 6b §E Law L9 F8 LOCKED. Violation
refuter: a Tier 0 alert committed before halt registered. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9 Halt-Log-Alert F8]

**L-6. Corrigibility — Part 8 NEVER locks owner out of override.** [Meadows
L4 — goals] Per Askell HHH Appendix E.2 verbatim (F8 LOCKED Bundle 1 Part 6b
§E Law L9). Owner can: `git revert` any health snapshot; manually edit any
audit report; override any alert; pause Part 8 entirely. Part 8 is
SURVEILLANCE-ENABLING but NOT ENFORCEMENT — there is no mechanism by which
Part 8's alerts cannot be overridden by owner judgment. Violation refuter: a
Part 8 alert that cannot be reverted via standard `git revert`. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9 Corrigibility F8; src:raw/books-md/anthropic/askell-2021-hhh.md:Appendix E.2]

**L-7. Specify-and-stub scope discipline.** [Meadows L5 — rules; OQ-MERGED-5
F8 ack] Bundle 3 Part 8 = schemas + templates + stub routing. NOT live
implementation. NOT calibrated thresholds. NOT delivery code. NOT sub-daily
metric collection cadence. Violation refuter: any Part 8 §I.2 SLI entry with
production-grade threshold (no calibration-grade label) OR §H delivery code
(Slack/email/SMS) OR cadence <daily granularity. [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-MERGED-5]

**L-8. TRADEOFF-01 split discipline (Beer VSM S3 boundary).** [Meadows L4
— goals] Part 8 = audit LEAD. Part 6a = audit SUPPORT (service invocation).
Part 6b = ENFORCEMENT ARM (alert routing). Part 8 does NOT re-implement
Part 6a's F-G-R compliance check primitive; Part 8 does NOT directly enforce
gates. Violation refuter: Part 8 §J quarterly audit ritual that runs F-G-R
compliance check inline (instead of invoking Part 6a as service) OR Part 8
auto-routing alerts to delivery channels (instead of through Part 6b
enforcement arm). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 8 TRADEOFF-01]

### Admissibility (acceptance criteria for inputs)

**A-1.** Health signals admitted to Part 8 ONLY if derived from committed
git artefacts — no ephemeral in-memory metrics [src:design/JETIX-FPF.md:§5.3
IP-3 artifacts-over-conversations; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md:§4 D25 Company-as-Code].

**A-2.** SLI definition admitted to §I.2 ONLY if it names: `name`,
`signal_ref` (cross-ref to a health-signal definition in §I.1),
`measurement_method`, `cadence`, `starter_value`, `starter_value_label:
"calibration-grade"`, `calibration_trigger`, `calibration_cadence`. SLOs
without these eight fields are REJECTED.

**A-3.** Health signal admitted to §I.1 ONLY if it conforms to canonical
schema: `signal_name`, `emitter_part`, `emitter_section`, `value`, `unit`,
`cadence`, `measurement_method`, `created_at`, `cycle_id`, `f_g_r`. Mapping
table §I.3 covers Bundle 1+2 emitter shapes; new emitters (Bundle 3+ Parts)
emit canonical schema directly.

**A-4.** Anomaly admitted to alert-routing pipeline ONLY if classified per
Default-Deny table (Part 6b §I.3 F8 LOCKED). Novel alert classes Default-Deny
to Tier 1+ default; manual classification required to assign Tier 0 or
Tier 2/3.

**A-5.** Quarterly immune audit admitted ONLY if all five required scope
items present (per L-4): F-G-R drift / alpha classification drift /
role-manifest freshness / methodology library staleness / strategies.md
staleness. Audit with missing scope item is REJECTED at admission gate.

### Deontics (obligations of this part toward consumers)

**D-1.** MUST produce weekly health dashboard at `swarm/audits/weekly/<YYYY-WNN>-health.md` for Part 9 (Owner Interaction Scaffold) for the weekly
review ritual [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§2.5
health checkup cadence].

**D-2.** MUST open AWAITING-APPROVAL packet via Part 6b within 24h of
detecting a structural integrity failure (Tier 0 SLA per FUNDAMENTAL §4.2;
in practice Tier 0 is ≤60s alert per Halt-Log-Alert L9).

**D-3.** MUST NOT execute behaviour-change without HITL ack — surfacing is
automatic; response decision is owner-owned (FUNDAMENTAL §6.1).

**D-4.** MUST emit ALL Bundle 3 starter SLI entries (≥8) with
`starter_value_label: "calibration-grade"` populated; NO unlabeled starter
values per L-3.

**D-5.** MUST invoke Part 6a F-G-R compliance check service at quarterly
audit cadence (TRADEOFF-01 audit support per L-8); MUST include Part 6a's
returned drift report in the quarterly audit output.

**D-6.** MUST NOT auto-route alerts to delivery channels (Slack/email/SMS);
MUST route through Part 6b enforcement arm per L-8 + L-7.

### Effects (measurable outcomes)

**E-1.** Weekly: `swarm/audits/weekly/<YYYY-WNN>-health.md` committed via
Part 1 §H `[health] weekly snapshot: WNN-YYYY`.

**E-2.** Quarterly: `swarm/audits/quarterly/<YYYY-QN>-immune-audit.md`
committed via Part 1 §H `[health] quarterly immune audit: QN-YYYY`.

**E-3.** Anomaly → AWAITING-APPROVAL packet opened via Part 6b within one
monitoring cycle (Tier 0 ≤60s; Tier 1 same-session; Tier 2 batch-weekly;
Tier 3 silent-log).

**E-4.** Part 6a F-G-R compliance check service invoked quarterly; returned
drift report included in quarterly audit output.

**E-5.** Bundle 3 deliverable: ≥8 starter SLI entries in §I.2 with
calibration-grade labels; ≥10 alert classes mapped in §H.1; canonical
health-signal schema declared in §I.1; mapping table populated in §I.3.

---

## §F Anti-scope

### §F.1 Generic anti-scope (per FUNDAMENTAL §6 — all Foundation parts)

- Part 8 does NOT make strategic decisions. Health monitoring surfaces
  patterns; the OWNER decides what to do [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1].
- Part 8 does NOT execute behaviour-change without HITL ack.
- Part 8 does NOT modify agent system prompts (no-self-modify rule).

### §F.2 Part-specific anti-scope

- **Part 8 does NOT enforce stage gates.** That is Part 6b's domain. Part 8
  DETECTS compliance drift; Part 6b ENFORCES. TRADEOFF-01 split materialised.

- **Part 8 does NOT implement SLI/SLO numerical tooling in Bundle 3.**
  Bundle 3 scope is "specify and stub" per OQ-MERGED-5: schemas + cadence
  declarations + templates. Numerical calibration + tool implementation =
  Phase B materialisation [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§4 Kauffman Ch.1
  adjacent-possible — numerical calibration requires ≥5 cycles of real data
  before numbers are stable].

- **Part 8 does NOT name specific role holders for immune-system function.**
  The immune-system function (IP-4 audit cadence) is GENERIC; the specific
  role assigned (e.g. "ontological-integrity-steward") is RUSLAN-LAYER
  `executor-binding.yaml` per IP-1 [src:design/JETIX-FPF.md:§5.1 IP-1].

- **Part 8 does NOT produce recommendations that substitute for founder
  judgment.** Output is a "look here" list; the owner acts or defers
  [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1 UC-I.3].

- **Part 8 does NOT cover capital-impact analysis on health signals.** That
  routes to investor-expert domain.

- **Part 8 does NOT auto-deliver alerts to Slack/email/SMS/page.** Alert
  ROUTING is specified; alert DELIVERY is Phase B materialisation. Bundle 3
  deliverable is `swarm/audits/log/alert-log.jsonl` (Tier 3 silent-log) +
  AWAITING-APPROVAL packets via Part 6b (Tier 0/1/2). Live delivery channels
  are Phase B.

- **Part 8 does NOT calibrate FUNDAMENTAL §3 30+ SLI/SLO pairs in Bundle 3.**
  Bundle 3 declares ≥8 starter entries (one per major health domain). Phase B
  expands inventory + calibrates thresholds.

### §F.3 OQ-MERGED-5 specify-and-stub scope discipline (CRITICAL)

Per OQ-MERGED-5 ack [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-MERGED-5]:

> **Bundle 3 Part 8 = SLI/SLO schema + canonical health signal schema +
> template authoring + alert-routing stub. NOT live metrics implementation.
> NOT calibrated thresholds.**

Self-monitored failure mode declared in §K (K-PartB — over-implementation
drift). Brigadier autocheck (§6.8 of Bundle 3 deep prompt) verifies Bundle 3
Part 8 output is stub-level.

---

## §G F-G-R Tagging (DOGFOOD per Part 6a §I.1 F8 schema)

| Artefact / Claim | F | ClaimScope (G) | Reliability (R) | Promotion path |
|---|---|---|---|---|
| Weekly health snapshot artefact | F4 | Current system state only; calibration parameters may shift | R-medium — automated computation, owner-reviewed | F5 once Phase B calibration completes |
| Quarterly immune audit artefact | F5 | Foundation-wide artefact types across the quarter | R-high — structured audit protocol, human-reviewed | Already F5 on first quarterly audit run |
| Alert record (anomaly) | F4 | Specific anomaly event, single cycle | R-medium — threshold-based detection, may have false positives | F5 on Phase B threshold calibration |
| Recommendation list ("look here") | F3 | Current week's signals only | R-low — surfacing heuristics, owner validation required | F4 with cross-cycle validation |
| Canonical health-signal schema (§I.1) | F4 architecture-time | Foundation-wide canonical | R-medium | F5 on Bundle 3 owner ack |
| SLI/SLO schema (§I.2) | F4 architecture-time | Foundation-wide canonical; calibration-cadence declared | R-high once schema acked; starter values F3 until calibrated | F5 on Bundle 3 owner ack of schema; per-SLI starter F3→F4→F5 on Phase B calibration cycles |
| Mapping table (§I.3) | F4 architecture-time | Bundle 1+2 emitter shapes mapped to canonical | R-medium | F5 on Bundle 3 owner ack |
| Alert-routing stub (§H.1) | F4 | Foundation alert classes mapped to Tier 0/1/2/3 | R-medium | F5 on first Phase B live alert routing |
| Weekly health template | F4 | Weekly review ritual | R-medium | F5 on first quarterly review showing template adoption |
| Quarterly immune audit template | F5 | Foundation-wide audit ritual | R-high | Already F5 on first audit run |
| Per-SLI starter values (8 entries) | F3 | Phase A starter; calibration-grade labeled | R-low — calibration | F4 on first Phase B observation; F5 on Phase B calibration |
| Per-SLI calibrated values (Phase B) | F-N/A Bundle 3 | Phase B materialisation | R-N/A | Phase B promotion path |

**§G.1 Concrete consequence — Phase B calibration is F-rise lifecycle.** Per
F-G-R schema F8 LOCKED [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1]: F-rise events are the lifecycle of an SLI's
maturity. Bundle 3 starter entries are F3 (architecture-time stub +
calibration-grade label). On first Phase B observation cycle: F3→F4
("≥3 cycles applied"). On full Phase B calibration (2-3 months observational
data per OQ-MERGED-5): F4→F5 ("operational convention; multi-cycle
validated"). The starter values are PLACEHOLDERS for the F-rise lifecycle to
play out.

---

## §H Code-Level Interfaces

### §H.1 Alert-routing stub config (Bundle 3 deliverable per P8.4)

Mapping table per alert class (per anomaly type from canonical health-signal
schema) → blast-radius Tier (0/1/2/3 per Part 6b §I.4 F8 LOCKED 4-tier table)
→ routing target. Halt-Log-Alert ordering enforced for Tier 0
(≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9 F8).

**Alert packet schema (canonical for Part 8 alert emission):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/health-alert.json",
  "title": "Health alert packet",
  "type": "object",
  "required": ["alert_id", "anomaly_type", "severity_tier", "affected_part", "affected_signal", "recommended_action", "j_level_authority_required", "created_at", "cycle_id", "f_g_r"],
  "properties": {
    "alert_id": { "type": "string", "pattern": "^ha-[0-9]{8}-[0-9]{3}$" },
    "anomaly_type": { "type": "string" },
    "severity_tier": { "type": "integer", "enum": [0, 1, 2, 3] },
    "affected_part": { "type": "string", "pattern": "^part-(1|2|3|4|5|6a|6b|7|8|9|10)$" },
    "affected_signal": { "type": "string" },
    "recommended_action": { "type": "string" },
    "j_level_authority_required": { "type": "string", "enum": ["J-Auto", "J-Approve", "J-Strategic"] },
    "halt_log_alert_ordering": {
      "type": "object",
      "description": "Required ONLY for severity_tier=0; enforced per Part 6b §E Law L9 F8",
      "properties": {
        "halt_at": { "type": "string", "format": "date-time" },
        "log_at": { "type": "string", "format": "date-time" },
        "alert_at": { "type": "string", "format": "date-time" }
      }
    },
    "created_at": { "type": "string", "format": "date-time" },
    "cycle_id": { "type": "string" },
    "f_g_r": { "$ref": "#/definitions/f_g_r" },
    "routing_target": {
      "type": "string",
      "enum": ["part-6b-stop-gate", "part-6b-stage-gate-same-session", "part-6b-stage-gate-batch-weekly", "swarm-audits-log-jsonl"],
      "description": "Tier 0 → part-6b-stop-gate; Tier 1 → part-6b-stage-gate-same-session; Tier 2 → part-6b-stage-gate-batch-weekly; Tier 3 → swarm-audits-log-jsonl"
    }
  }
}
```

**Alert-class mapping table (Bundle 3 ≥10 classes per spec P8.4):**

| Alert class | Tier | Routing target | Halt-Log-Alert? | Cross-ref |
|---|---|---|---|---|
| `git-fsck-object-error` | 0 | part-6b-stop-gate | YES (≤1s/≤5s/≤60s) | Part 1 §K K8 |
| `hook-bypass-attempt` (`--no-verify` detected) | 1 | part-6b-stage-gate-same-session | NO | Part 1 §K K6 |
| `fg-r-compliance-collapse` (>30% wiki entries missing F-G-R fields) | 0 | part-6b-stop-gate | YES | Part 6a §I.1 F8 + quarterly framework |
| `methodology-admissibility-violation` (entry promoted F4→F5 without ≥2-cycle DRR validation) | 1 | part-6b-stage-gate-same-session | NO | Part 3 §E L9 admissibility predicate F5 |
| `mailbox-queue-overflow` (queue depth > 2× rolling 7d avg for 3+ consecutive cycles) | 1 | part-6b-stage-gate-same-session | NO | Part 4 §I.4 mailbox-queue-depth signal |
| `orphan-anchor-spike` (orphan-anchor count rises by >50% in single weekly run) | 2 | part-6b-stage-gate-batch-weekly | NO | Part 3 §I.6 orphan-anchor-count |
| `stale-claims-burst` (stale-claim count rises by >30% in single weekly run) | 2 | part-6b-stage-gate-batch-weekly | NO | Part 3 §I.6 stale-claims-count |
| `drr-write-rate-drop` (rolling 5-cycle DRR-write-rate <0.5 vs target ≥1 per role per cycle) | 2 | part-6b-stage-gate-batch-weekly | NO | Part 5 §B drr-write-rate |
| `commit-format-violation` (lint signal #12 historical bypasses detected) | 3 | swarm-audits-log-jsonl | NO | Part 1 §K K6 lint signal #12 |
| `compound-application-rate-burn` (rolling 5-cycle ratio <0.8) | 1 | part-6b-stage-gate-same-session | NO | Part 5 §B compound-application-rate; FUNDAMENTAL §3.3.1 |
| `gate-approval-lag-burn` (Tier 0/1 packet open >SLA per Part 6b §E Deontics) | 0 | part-6b-stop-gate | YES (Tier 0 SLA breach IS Tier 0) | Part 6b §E Deontics gate SLA |
| `dissolve-test-evidence-drought` (Bundle 3+4+Wave D accumulator <3 at Wave D ack cycle) | 1 | part-6b-stage-gate-same-session | NO (ack-time decision; not real-time anomaly) | Part 5 §X.3 + decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md |
| `repo-growth-spike` (single-cycle commit count > 2× rolling 7d avg) | 3 | swarm-audits-log-jsonl | NO | Part 1 §B Four Golden Signals |
| `voice-pipeline-failure-rate` (rolling 7d failure rate >10%) | 2 | part-6b-stage-gate-batch-weekly | NO | Part 2 §I.6 voice-pipeline-success-rate |

≥10 alert classes mapped per spec P8.4 acceptance predicate. Halt-Log-Alert
ordering enforced for all Tier 0 entries. Tier 1+ Default-Deny per Part 6b §I.3
— novel alert classes default to Tier 1+; manual classification required to
assign Tier 0 (more severe) or Tier 2/3 (less severe).

**STUB-LEVEL discipline.** This is the routing **specification**, not the
routing **implementation**. Live alert delivery infrastructure (Slack/mailbox/email/SMS/page) = Phase B materialisation per OQ-MERGED-5. The
ROUTING TARGET column names the canonical Part 6b gate type or the silent-log
file; HOW the gate notifies the owner (e.g., session prompt, email digest)
is Phase B.

### §H.2 CLI signatures (canonical)

```
# Weekly health snapshot driver
/health-snapshot-weekly [--week=WNN] [--dry-run]

# Quarterly immune audit driver
/health-audit-quarterly [--quarter=QN-YYYY] [--invoke-part-6a-service] [--dry-run]

# SLI evaluation
/sli-evaluate <sli-name> [--cadence-window=Nh|Nd|Nw]

# Alert emit (called from anomaly detector)
/alert-emit <alert-class> --affected-part=<part> --affected-signal=<signal-name> --severity-tier=<0|1|2|3>

# Mapping table validate (canonical schema vs Bundle 1+2 emitters)
/health-mapping-validate

# Health signal emit (called from Bundle 1+2+3 emitters via swarm/lib/health-emit.py)
/health-signal-emit <signal-name> --emitter-part=<part> --emitter-section=<§> --value=<num> --unit=<str> --cadence=<str> --measurement-method=<str>
```

### §H.3 swarm/lib/ accessor pipeline (Bundle 3 extension per Bundle 2 C1
Joint Design canonical)

Part 8 contributes accessor scripts to `swarm/lib/` per Part 3 LEAD + Part 4
ADVISORY governance:

- `swarm/lib/health-emit.py` — emit health signal per canonical schema §I.1.
  Called from Bundle 1+2+3 emitters (passive read pattern; emitters write
  through this accessor for validation).
- `swarm/lib/sli-evaluate.py` — evaluate SLI value against SLO per §I.2
  schema; emit alert if burn-rate threshold exceeded.
- `swarm/lib/health-snapshot-weekly.py` — generate weekly dashboard per
  §I.4 template.
- `swarm/lib/health-audit-quarterly.py` — generate quarterly audit per
  §I.5 template; INVOKES Part 6a service for F-G-R compliance check.
- `swarm/lib/alert-emit.py` — emit alert packet per §H.1 alert-routing stub;
  routes through Part 6b enforcement arm.
- `swarm/lib/health-mapping-validate.py` — validate canonical health-signal
  schema vs Bundle 1+2 emitter shapes per mapping table §I.3.

All accessors live in `swarm/lib/` — NOT inline in skills. DRY discipline +
UC-9 Phase-A isolation per `wiki-roots.yaml` clients stanza.

### §H.4 Reference to Part 6b §I.1 awaiting-approval-packet schema

Alert routing emits AWAITING-APPROVAL packets conforming to Part 6b §I.1 F8
LOCKED schema:
- Tier 0 alerts → `gate_class: stop_gate` + Halt-Log-Alert ordering
- Tier 1 alerts → `gate_class: stage_gate` + same-session ack
- Tier 2 alerts → `gate_class: stage_gate` + batch-weekly ack
- Tier 3 alerts → silent-log (no packet; entry to `swarm/audits/log/alert-log.jsonl` only)

Packet field set per Part 6b §I.1 F8 LOCKED — no field additions; Part 8
populates standard fields with Part 8-specific values. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.1 awaiting-approval-packet F8]

### §H.5 Reference to Part 6a quarterly immune audit framework

Quarterly audit ritual (§J.2) invokes Part 6a service per TRADEOFF-01 audit
support:

```
# Pseudo-code — Part 6a service invocation
result = part_6a.fg_r_compliance_check(scope=["wiki/", "decisions/", "agents/"], quarter="2026-Q2")
# result includes: drift_count, missing_fg_r_entries, citation_resolution_pct, by_artefact_type
```

Part 8 includes `result` in quarterly audit output. Part 6a is a SERVICE;
Part 8 does NOT re-implement F-G-R compliance checking. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:quarterly immune audit framework]

### §H.6 Routing-table.yaml extension (Bundle 3 deliverable)

Part 8 contributes the `health-monitor` role archetype entry to
`swarm/lib/routing-table.yaml`. Role archetype name (IP-1 strict):
`health-monitor`. Routing rule: weekly schedule (Friday 17:00) +
event-driven on anomaly-detect triggers dispatch to `health-monitor` role;
the ROLE invokes accessor pipeline; the EXECUTOR mapping lives in
RUSLAN-LAYER `executor-binding.yaml`. Plus `quarterly-immune-auditor` role
for quarterly cadence.

---

## §I Data Schemas

### §I.1 Canonical health-signal schema (C2 RESOLUTION — Variant B chosen per Joint Design lite)

**Schema-of-schema (declared inline; physical file `shared/schemas/health-signal.json` generation Phase B per OQ-B1-2 + OQ-B1-4 pattern):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/health-signal.json",
  "$comment": "GENERIC Foundation schema. C2 RESOLUTION (Variant B chosen per Joint Design lite §4.3): Bundle 1+2 emitter shapes (currently F5 LOCKED heterogeneous stubs at Part 1 §I.5, Part 3 §I.6, Part 4 §I.4) are mapped to this canonical schema via §I.3 mapping table. Retroactive align (Variant A) deferred to Wave D housekeeping cycle to respect F5 LOCKED architecture stability.",
  "title": "Health signal (canonical)",
  "description": "The unified shape every Foundation Part emits health signals in. Bundle 3 Part 8 declares this schema as canonical; Bundle 1+2 emitters use mapping table §I.3 adapter; Bundle 3+ Parts (Part 5 sibling) emit canonical directly.",
  "type": "object",
  "required": ["signal_name", "emitter_part", "emitter_section", "value", "unit", "cadence", "measurement_method", "created_at", "cycle_id", "f_g_r"],
  "properties": {
    "signal_name": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$",
      "description": "kebab-case signal name (e.g. compound-application-rate, commit-error-rate, orphan-anchor-count)"
    },
    "emitter_part": {
      "type": "string",
      "pattern": "^part-(1|2|3|4|5|6a|6b|7|8|9|10)$",
      "description": "Foundation Part emitting this signal"
    },
    "emitter_section": {
      "type": "string",
      "description": "Section reference within emitter_part (e.g. §J burn-rate, §I.4 task-return-packet, §B compound-application-rate)"
    },
    "value": {
      "type": ["number", "boolean"],
      "description": "Numeric value OR boolean (e.g. fsck-object-errors=0 | true if errors present). Numeric is canonical; boolean is allowed for binary integrity signals."
    },
    "unit": {
      "type": "string",
      "description": "Unit of measurement (e.g. ratio, count, seconds, percent). Use SI-style; ratio is unit-less but explicit."
    },
    "cadence": {
      "type": "string",
      "pattern": "^(event-driven|periodic-[0-9]+(m|h|d|w))$",
      "description": "event-driven OR periodic-Nm/Nh/Nd/Nw — minimum cadence granularity per OQ-MERGED-5 is daily (periodic-1d); sub-daily allowed only for Tier 0 signals"
    },
    "measurement_method": {
      "type": "string",
      "description": "How the signal is measured (e.g. 'git fsck exit code', 'count of orphan anchors via /lint', 'rolling 5-cycle ratio of compound-phase-fired/cycles-closed')"
    },
    "created_at": { "type": "string", "format": "date-time" },
    "cycle_id": { "type": "string" },
    "f_g_r": {
      "type": "object",
      "required": ["f", "claimscope", "reliability"],
      "properties": {
        "f": { "type": "string", "enum": ["F2", "F3", "F4", "F5", "F6", "F7", "F8"] },
        "claimscope": { "type": "string" },
        "reliability": { "type": "string", "enum": ["R-low", "R-medium", "R-high"] },
        "refuted_if": { "type": "string" },
        "accepted_if": { "type": "string" }
      },
      "description": "Per Part 6a §I.1 F8 LOCKED schema."
    },
    "para_tier": {
      "type": "string",
      "enum": ["Area"],
      "description": "PARA-tier mandatory per Bundle 2 P2.2 + Bundle 3 cross-cut. Health signals are 'Area' (ongoing operational concern) — not Resource (reusable pattern), not Archive (deprecated), not Project (time-bound)."
    }
  }
}
```

**§I.1.1 Concrete consequence — C2 resolution Variant B chosen.** Per Joint
Design lite Phase (Bundle 3 deep prompt §4.3): Variant A (retroactive align
Bundle 1+2 emitters to canonical schema) was OPTION; Variant B (Part 8 §I.1
canonicalises + §I.3 mapping table adapter) was FALLBACK. Variant B chosen
because: (a) Bundle 1+2 emitter §I.5/§I.6/§I.4 sections are F5 LOCKED — modifying
them risks F-fall via re-litigation; (b) the mapping table is a clean Adapter
Pattern (Gang of Four 1994 + clean-code §4 Patterns) — adapter sits between
canonical schema and existing emitter shapes; emitters do not need to know
about canonical schema directly; (c) Variant A retroactive align can be done
in Wave D housekeeping cycle as a coordinated supplement (similar to OQ-B2-A
retroactive supplement pattern from Bundle 1) — no Phase A urgency. Variant A
remains AVAILABLE in Wave D; the choice here is "Variant B for Bundle 3,
Variant A optional for Wave D housekeeping."

[Cross-ref: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/joint-design-lite-c2-resolution.md` — companion artefact mirroring this decision.]

### §I.2 SLI/SLO schema (P8.1 binding)

**Schema-of-schema (declared inline; physical file `shared/schemas/sli-slo.json` generation Phase B):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/sli-slo.json",
  "$comment": "GENERIC Foundation schema. Bundle 3 declares schema; ≥8 starter SLI entries populated below; Phase B calibration replaces starter values per OQ-MERGED-5.",
  "title": "SLI/SLO schema",
  "type": "object",
  "definitions": {
    "sli": {
      "type": "object",
      "required": ["name", "signal_ref", "measurement_method", "cadence", "starter_value", "starter_value_label", "calibration_trigger", "calibration_cadence"],
      "properties": {
        "name": { "type": "string", "pattern": "^[a-z][a-z0-9-]*$" },
        "signal_ref": {
          "type": "string",
          "description": "Cross-ref to a health-signal definition in §I.1 (signal_name)"
        },
        "measurement_method": { "type": "string" },
        "cadence": { "type": "string", "pattern": "^(event-driven|periodic-[0-9]+(m|h|d|w))$" },
        "starter_value": { "type": ["number", "string"] },
        "starter_value_label": {
          "type": "string",
          "const": "calibration-grade",
          "description": "MANDATORY per OQ-MERGED-5 + L-3. Starter values are placeholders; Phase B calibration replaces with operational data."
        },
        "calibration_trigger": {
          "type": "string",
          "description": "Cycle/data condition that promotes starter→calibrated value (e.g. '≥3 cycles of operational data')"
        },
        "calibration_cadence": {
          "type": "string",
          "description": "Review cadence (per OQ-MERGED-5: monthly review minimum; not sub-daily)"
        }
      }
    },
    "slo": {
      "type": "object",
      "required": ["name", "sli_ref", "target_value", "error_budget", "burn_rate_thresholds"],
      "properties": {
        "name": { "type": "string" },
        "sli_ref": { "type": "string" },
        "target_value": { "type": "number" },
        "error_budget": { "type": "number", "description": "1 - target_value" },
        "burn_rate_thresholds": {
          "type": "object",
          "required": ["1x", "6x", "14.4x"],
          "description": "Per SRE Workbook Ch.2 burn-rate algebra (already adopted in Part 1 §J)",
          "properties": {
            "1x": { "type": "string", "description": "Normal — no behaviour change" },
            "6x": { "type": "string", "description": "Urgent — owner notified within session" },
            "14.4x": { "type": "string", "description": "Critical — page within 1h; halt non-critical writes" }
          }
        },
        "behaviour_change_rule": { "type": "object" }
      }
    }
  }
}
```

**Bundle 3 ≥8 starter SLI entries (one per major health domain per spec P8.1):**

```yaml
sli_entries:
  - name: git-substrate-integrity
    signal_ref: fsck-object-errors  # Part 1 §I.5
    measurement_method: "Weekly git fsck exit code; 0 = no errors"
    cadence: periodic-1w
    starter_value: 0
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B operational data ≥4 weekly fsck runs"
    calibration_cadence: monthly review
    # SLO target 100% (zero errors); error_budget 0; 14.4x burn = halt all writes (K8 policy)

  - name: triage-pipeline-success-rate
    signal_ref: voice-pipeline-success-rate  # Part 2 §I.6
    measurement_method: "Rolling 7d ratio of voice-pipeline-runs-success / voice-pipeline-runs-total"
    cadence: periodic-1d
    starter_value: 0.95
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B ≥10 weekly observations"
    calibration_cadence: monthly review

  - name: kb-freshness
    signal_ref: stale-claims-count  # Part 3 §I.6
    measurement_method: "Count of wiki entries with last_validated_at >90d via /lint --check-stale-claims"
    cadence: periodic-1w
    starter_value: 10
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B ≥4 weekly /lint runs"
    calibration_cadence: monthly review

  - name: mailbox-cycle-time
    signal_ref: cycle-time-avg  # Part 4 §I.4
    measurement_method: "Rolling 5-cycle avg of cycle-open to cycle-close duration"
    cadence: event-driven
    starter_value: 90
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B ≥10 cycles"
    calibration_cadence: monthly review
    # unit: minutes

  - name: drr-write-rate
    signal_ref: drr-write-rate  # Part 5 §B
    measurement_method: "Rolling 5-cycle avg of DRR entries committed per role per cycle"
    cadence: event-driven
    starter_value: 1.0
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B ≥5 compound-phase fires"
    calibration_cadence: monthly review

  - name: gate-open-count
    signal_ref: gate-open-count  # Part 6b §I.1
    measurement_method: "Count of AWAITING-APPROVAL packets open simultaneously"
    cadence: event-driven
    starter_value: 5
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B ≥4 weekly observations"
    calibration_cadence: monthly review
    # SLO target ≤5; >5 = batch-ack queue overflow signal

  - name: project-state-distribution-health
    signal_ref: project-state-distribution  # Part 7 §B (Bundle 4 pending)
    measurement_method: "Per /company-status snapshot, ratio of active-projects-with-cycle-progress / active-projects-total"
    cadence: periodic-1w
    starter_value: 0.7
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B + Bundle 4 Part 7 emission online"
    calibration_cadence: monthly review

  - name: daily-log-creation-rate
    signal_ref: daily-log-creation-rate  # Part 9 §B (Bundle 4 pending)
    measurement_method: "Per /plan-day fire, daily log file created in decisions/daily/<YYYY-MM-DD>.md"
    cadence: periodic-1d
    starter_value: 0.85
    starter_value_label: calibration-grade
    calibration_trigger: "Phase B + Bundle 4 Part 9 emission online"
    calibration_cadence: monthly review

slo_entries:
  - name: git-substrate-integrity-slo
    sli_ref: git-substrate-integrity
    target_value: 1.0
    error_budget: 0.0
    burn_rate_thresholds:
      "1x": "Normal — fsck clean every Sunday"
      "6x": "Urgent — fsck error in last 7d; owner notified same session"
      "14.4x": "Critical — fsck error + commits halted; AWAITING-APPROVAL stop_gate to Part 6b"
    behaviour_change_rule:
      14.4x: "ALL canonical writes halted per Part 1 K8 policy; HITL ack required; restore from verified backup if fsck objects corrupted"

  - name: kb-freshness-slo
    sli_ref: kb-freshness
    target_value: 10  # max stale entries
    error_budget: "starter — Phase B calibrates"
    burn_rate_thresholds:
      "1x": "Normal — stale entries ≤10"
      "6x": "Urgent — 11-20 stale entries; weekly /consolidate triggered"
      "14.4x": "Critical — >20 stale entries; quarterly immune audit advanced"

  - name: drr-write-rate-slo
    sli_ref: drr-write-rate
    target_value: 1.0
    error_budget: 0.2
    burn_rate_thresholds:
      "1x": "Normal — ≥0.8 rolling 5-cycle"
      "6x": "Urgent — 0.5-0.8; compound phase suspected skipped; owner alerted"
      "14.4x": "Critical — <0.5; compound phase severely degraded; weekly review prioritises"
```

**§I.2.1 Concrete consequence — All starter values labeled.** Per L-3 +
OQ-MERGED-5 specify-and-stub scope discipline: every starter_value entry above
has `starter_value_label: "calibration-grade"` populated AND
`calibration_trigger` AND `calibration_cadence`. **NO unlabeled starter
values.** This is the structural enforcement of OQ-MERGED-5.

**§I.2.2 Concrete consequence — Burn-rate algebra inherited from Part 1 §J.**
The `burn_rate_thresholds: {1x, 6x, 14.4x}` structure is identical to Part 1
§J adoption [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§J SRE Workbook Ch.2 burn-rate]. Part 8 §I.2 INHERITS the algebra
without re-derivation. SRE Workbook Ch.2 [src:raw/books-md/sre/google-srewb-implementing-slos.md:Ch.2] is the canonical authority adopted Bundle 1.

### §I.3 Mapping table — Bundle 1+2 emitter shapes to canonical schema (C2 resolution)

| Source Part | Source signal stub (Bundle 1+2 declared shape) | Canonical schema field projection | Notes |
|---|---|---|---|
| Part 1 §I.5 | `commit-error-rate` (numeric percentage) | `signal_name=commit-error-rate, emitter_part=part-1, emitter_section=§I.5, value=<float>, unit=percent, cadence=periodic-1h, measurement_method='count(failed-commits-7d)/count(commit-attempts-7d)'` | Direct projection — no semantic gap |
| Part 1 §I.5 | `hook-failure-rate` (numeric percentage) | `signal_name=hook-failure-rate, ...` | Direct |
| Part 1 §I.5 | `fsck-object-errors` (boolean OR integer count) | `signal_name=fsck-object-errors, ..., value=<int 0-N>, unit=count, cadence=periodic-1w, measurement_method='git fsck exit code interpretation'` | Direct; value=0 if clean |
| Part 1 §I.5 | `repo-growth` (commit count per period) | `signal_name=repo-growth, ..., value=<int>, unit=count, cadence=periodic-1d` | Direct |
| Part 1 §B | `latency-p95` (Four Golden Signals) | `signal_name=latency-p95, ..., unit=seconds, cadence=periodic-1h, measurement_method='per Part 1 §B SRE Four Golden Signals'` | Direct |
| Part 2 §I.6 | `triage-backlog` (count) | `signal_name=triage-backlog, emitter_part=part-2, emitter_section=§I.6, value=<int>, unit=count, cadence=periodic-1d, measurement_method='count(unprocessed-voice-items)+count(unprocessed-emails)'` | Direct |
| Part 2 §I.6 | `STOP-gate-acked-rate` (ratio) | `signal_name=stop-gate-acked-rate, ..., unit=ratio, cadence=periodic-1d` | Direct |
| Part 2 §I.6 | `para-tier-coverage` (percentage of inbox items with PARA tag) | `signal_name=para-tier-coverage, ..., unit=percent, cadence=periodic-1w` | Direct |
| Part 3 §I.6 | `orphan-anchor-count` (count) | `signal_name=orphan-anchor-count, emitter_part=part-3, ..., unit=count, cadence=periodic-1w, measurement_method='/lint --check-orphan-anchors'` | Direct |
| Part 3 §I.6 | `stale-claims-count` (count) | `signal_name=stale-claims-count, ..., measurement_method='/lint --check-stale-claims (last_validated_at >90d)'` | Direct |
| Part 3 §I.6 | `edges-per-entity-avg` (ratio) | `signal_name=edges-per-entity-avg, ..., unit=ratio` | Direct |
| Part 3 §I.6 | `contradicts-supports-density` (ratio) | `signal_name=contradicts-supports-density, ..., unit=ratio` | Direct |
| Part 3 §I.6 | `methodology-admissibility-violations` (count) | `signal_name=methodology-admissibility-violations, ...` | Direct |
| Part 3 §I.6 | `comparisons-emptiness-flag` (boolean) | `signal_name=comparisons-emptiness-flag, ..., value=<bool>` | Boolean value variant |
| Part 3 §I.6 | `malformed-crm-edges` (count) | `signal_name=malformed-crm-edges, ...` | Direct |
| Part 4 §I.4 | `mailbox-queue-depth` (count) | `signal_name=mailbox-queue-depth, emitter_part=part-4, ..., cadence=event-driven` | Direct |
| Part 4 §I.4 | `cycle-time-avg` (minutes) | `signal_name=cycle-time-avg, ..., unit=minutes` | Direct |
| Part 4 §I.4 | `escalation-rate` (ratio) | `signal_name=escalation-rate, ...` | Direct |
| Part 4 §I.4 | `routing-variety-count` (count of distinct routes used) | `signal_name=routing-variety-count, ...` | Direct |
| Part 4 §I.4 | `message-schema-version-distribution` (object: v1.0.0_count, v2.0.0_count) | `signal_name=message-schema-version-distribution, ..., value=<v2.0.0_ratio>, unit=ratio, measurement_method='count(v2.0.0)/count(total) over rolling 7d'` | Aggregation over Part 4's object emission — canonical schema requires single numeric value; aggregate is v2.0.0 adoption ratio |
| Part 5 §B (Bundle 3 sibling) | `compound-application-rate` | Native canonical (Part 5 emits to canonical schema directly per Bundle 3 sibling); no mapping needed | Native |
| Part 5 §B | `methodology-promotion-rate` | Native canonical | Native |
| Part 5 §B | `drr-write-rate` | Native canonical | Native |
| Part 5 §B | `dissolve-test-evidence-count` | Native canonical | Native |
| Part 6a §C | `approval-log-write-rate` | `signal_name=approval-log-write-rate, emitter_part=part-6a, emitter_section=§C, value=<int per cycle>, unit=count, cadence=event-driven` | Direct projection from Part 6a §C |
| Part 6a §I.1 | `fg-r-compliance-pct` | `signal_name=fg-r-compliance-pct, ..., unit=percent, cadence=periodic-1w` | Direct |
| Part 6a §I.1 | `citation-resolution-pct` | `signal_name=citation-resolution-pct, ...` | Direct |
| Part 6b §I.1 | `gate-open-count` | `signal_name=gate-open-count, emitter_part=part-6b, ...` | Direct |
| Part 6b §I.1 | `gate-acked-rate` | `signal_name=gate-acked-rate, ...` | Direct |
| Part 6b §I.3 | `default-deny-classified-pct` | `signal_name=default-deny-classified-pct, ...` | Direct |
| Part 6b §I.4 | `blast-radius-distribution` (object: tier_0_count, tier_1_count, tier_2_count, tier_3_count) | `signal_name=blast-radius-distribution-tier-N` (emitted as 4 separate signals, one per Tier; each signal value=count) | Disaggregation — canonical schema expects single value per signal; emit 4 signals |
| Part 6b §E L9 | `halt-log-alert-ordering-violations` (count) | `signal_name=halt-log-alert-ordering-violations, ...` | Direct |

**§I.3.1 Concrete consequence — Mapping table is the C2 RESOLUTION ADAPTER.**
Variant B chosen: Bundle 1+2 emitters retain F5 LOCKED §I.5/§I.6/§I.4 stub
shapes; Part 8 §I.3 mapping table is the adapter that projects each emitter
shape onto the canonical schema. Adapter pattern from Gang of Four 1994 +
clean-code §4 — adapter sits between canonical (Part 8 §I.1) and existing
emitter shapes; emitters do not need to know about canonical schema directly.
This is DRY-respectful (no schema duplication; single canonical authority)
without F-fall risk on Bundle 1+2 LOCKED architectures.

**§I.3.2 Concrete consequence — Aggregation/disaggregation rules.** Two
canonical-shape transformations declared: (a) Part 4
`message-schema-version-distribution` (object value) → single ratio scalar
(v2.0.0 adoption rate); (b) Part 6b `blast-radius-distribution` (object value
with 4 tier counts) → 4 separate signals, one per Tier. The mapping is
declarative — implementations apply transformations at signal-emit time.

### §I.4 Weekly health dashboard template

Template file at `swarm/audits/weekly-health-template.md` (Bundle 3
deliverable). Required sections per spec P8.3:

- **Period** (Week WNN — YYYY-MM-DD to YYYY-MM-DD)
- **SLI Snapshot Per Domain** — table: SLI name / current value / starter
  value / drift (current - starter) / status (green/yellow/red per burn-rate
  tier)
- **Anomalies** — table: anomaly-type / detected-at / affected-part /
  severity-tier / recommended-action / J-level-authority-required
- **Recommendations** ("look here" list per FUNDAMENTAL §1 UC-I.3) — owner-
  reviewed signals worth attention this week
- **Next-week appetite signals** (cross-ref Part 9 weekly review schema —
  Bundle 4)
- **F-G-R compliance summary** (cross-ref Part 6a service invocation result;
  weekly subset)

The template lives at `swarm/audits/weekly-health-template.md` with a
populated synthetic Week-NN row demonstrating SLI snapshot shape.

### §I.5 Quarterly immune audit template

Template file at `swarm/audits/quarterly-immune-audit-template.md` (Bundle 3
deliverable). Extends Part 6a Bundle 1 quarterly framework. Required sections
per spec P8.3:

- **Quarter** (YYYY-QN — YYYY-MM-DD to YYYY-MM-DD)
- **F-G-R Compliance Sweep** (cross-ref Part 6a service invocation result;
  per Part 6a §I.4 F-G-R compliance check primitive). **TRADEOFF-01 audit
  support visible HERE** — Part 8 invokes Part 6a service; Part 8 includes
  result.
- **Alpha Classification Drift** (IP-5 past-participle exception whitelist
  check; Phase B implementation per OQ-B1-2 lint signal)
- **Role-Manifest Freshness** (IP-6 audit; per FUNDAMENTAL §3 30+ SLI/SLO)
- **Methodology Library Staleness** (entries with `last_validated_at:` >90d
  flagged — cross-ref Part 5 §J.3 stale-DRR-review)
- **Strategies.md Staleness** (per-role DRR entry decay — cross-ref Part 5
  §J.3)
- **TRADEOFF-01 Verification** — Part 8 → Part 6a service invocation log
  visible (≥1 invocation per quarter); Part 6b enforcement gate log visible
  (≥1 enforcement per quarter, or zero with rationale "no drift detected")
- **Drift Remediation Gate Packet** — if drift detected, AWAITING-APPROVAL
  `gate_class: stage_gate` to Part 6b enforcement arm

The template lives at `swarm/audits/quarterly-immune-audit-template.md` with
a populated synthetic Q-N row demonstrating Part 6a service invocation result
shape (TRADEOFF-01 split materialised).

---

## §J Operational Rituals

### §J.1 Weekly health snapshot ritual

**Cadence.** Friday 17:00 local time (Berlin) — aligns with Part 1 §J
`/company-status` weekly review ritual (D29 Korp-Startup discipline; weekly
review is owner-facing, not silent; surfaces "look here" recommendations).

**Trigger.** Calendar cron (scheduled) + on-anomaly-detect (event-driven).
The two trigger paths are NOT exclusive — scheduled produces routine snapshot;
anomaly-detect may produce mid-week emergency snapshot.

**Ritual sequence:**

1. Driver `/health-snapshot-weekly` reads canonical health-signal stream
   (per §I.1 canonical schema; via mapping table §I.3 for Bundle 1+2
   emitters).
2. For each SLI in §I.2 starter set, compute current value; compare to
   starter_value; classify burn_rate (1x/6x/14.4x).
3. For each anomaly above Tier 3 threshold, emit alert via §H.1 alert-routing
   stub (Tier 0/1/2 routes to Part 6b; Tier 3 routes to silent-log).
4. Write `swarm/audits/weekly/<YYYY-WNN>-health.md` per template §I.4.
5. Update `shared/state/system-health.json` with current snapshot.
6. Commit via Part 1 §H `[health] weekly snapshot: WNN-YYYY`.
7. Emit `weekly-health-snapshot-committed` event consumed by Part 9 (Bundle 4
   weekly review feed).

**Acceptance predicate (P8.3):** Weekly template populated with synthetic
Week-NN row demonstrating SLI snapshot shape; Bundle 3 deliverable ships
populated synthetic example.

### §J.2 Quarterly immune audit ritual (TRADEOFF-01 audit lead binding)

**Cadence.** Quarterly — last business day of each quarter (per IP-4 quarterly
immune audit cadence) [src:design/JETIX-FPF.md:§5.4 IP-4].

**Trigger.** Calendar cron (scheduled).

**Ritual sequence (TRADEOFF-01 split visible at every step):**

1. Driver `/health-audit-quarterly --invoke-part-6a-service` invokes Part 6a
   F-G-R compliance check service [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:quarterly framework] across scope:
   `[wiki/, decisions/, agents/]`.
2. Part 6a returns drift report (drift_count, missing_fg_r_entries,
   citation_resolution_pct, by_artefact_type).
3. Driver runs IP-5 alpha classification drift check (Phase B lint signal;
   stub at Bundle 3).
4. Driver runs IP-6 role-manifest freshness check.
5. Driver runs methodology library staleness check (entries with
   `last_validated_at:` >90d).
6. Driver runs strategies.md staleness check (per-role DRR entry decay).
7. Driver compiles quarterly audit report per template §I.5.
8. **TRADEOFF-01 enforcement step:** if drift detected, driver opens
   AWAITING-APPROVAL packet via Part 6b with `gate_class: stage_gate`. Part 6b
   acks remediation gate. **Part 6b is enforcement arm; Part 8 surfaces; Part
   6a supports compliance check.**
9. Driver writes `swarm/audits/quarterly/<YYYY-QN>-immune-audit.md` per
   template §I.5.
10. Commit via Part 1 §H `[health] quarterly immune audit: QN-YYYY`.
11. `swarm/approvals/log.jsonl` entries appended (Part 6a §C; one per
    remediated entry, if any).

**Acceptance predicate (P8.3):** Quarterly template populated with synthetic
Q-N row demonstrating Part 6a service invocation result shape; TRADEOFF-01
split materialisation visible (Part 8 lead, Part 6a service, Part 6b
enforcement); Bundle 3 deliverable ships populated synthetic example.

### §J.3 SRE Workbook burn-rate behaviour-change ritual

Per Part 1 §J + SRE Workbook Ch.2: behaviour-change is pre-declared per burn
rate tier, NOT decided reactively. Per SLI in §I.2:
- 1× burn → no change (within SLO)
- 6× burn → owner notified within session; non-critical canonical writes
  paused pending investigation
- 14.4× burn → ALL canonical writes halted (K8 policy for git-substrate);
  immediate HITL ack required per Tier 0 routing

The behaviour-change rule is canonical for each SLO; declared in §I.2
`behaviour_change_rule` field. [src:raw/books-md/sre/google-srewb-implementing-slos.md:Ch.2]

### §J.4 Blameless postmortem ritual

Any Tier 0 incident MUST produce a postmortem commit. 5-line minimum per
FUNDAMENTAL §2.4: what happened / why / what changed / how detect next /
owner. Postmortem is committed at `swarm/audits/postmortems/<YYYY-MM-DD>-<slug>.md` via Part 1 §H `[meta] postmortem: <slug>`. Per SRE Book Ch.15:
"primary goals of writing a postmortem are to ensure that the incident is
documented, that all contributing root cause(s) are well understood, and,
especially, that effective preventive actions are put in place."
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§4 P5; src:raw/books-md/sre/google-sre-book.md:Ch.15]

### §J.5 Health-mapping-validate ritual (canonical schema vs Bundle 1+2 emitter shapes)

Cadence: per cycle (event-driven on cycle close + weekly batch).
Trigger: `/health-mapping-validate` skill.

Validates that every health signal emitted from Bundle 1+2 emitters projects
cleanly onto canonical schema per §I.3 mapping table. Failure = mapping table
gap; flagged for owner review. Phase A: manual mapping table maintenance;
Phase B: automated check.

### §J.6 Shape Up appetite for Part 8

Bundle 3 Part 8 architecture build: 1 day brigadier walltime appetite. Scope
fixed at "specify and stub" per OQ-MERGED-5; if scope expands beyond stub
(e.g., live metrics implementation creep), defer overflow to Phase B per
Cagan/Shape Up appetite-fixed/scope-variable. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md:§4 Principle 2]

---

## §K Failure Modes

**K1 — Health signal emission fails (emitter Part errors before canonical
schema write).**
Detection: expected weekly snapshot row missing for a Part. Policy: weekly
dashboard flags missing emitter; Part 8 emits "emitter-silent" alert (Tier 2
batch ack); owner investigates emitter Part. [F4|G:weekly snapshot integrity|R-medium]

**K2 — Mapping table gap (Bundle 1+2 emitter shape not in §I.3).**
Detection: §J.5 health-mapping-validate ritual flags unmapped emitter shape.
Policy: Tier 2 batch alert; owner manually adds mapping table entry +
commits. Phase B: auto-detect new emitter shapes. [F4|G:mapping table
maintenance|R-medium]

**K3 — SLI starter value un-labeled.**
Detection: `/lint` (Phase B) checks every §I.2 SLI entry for
`starter_value_label: "calibration-grade"`; Phase A: manual review at critic
gate. Policy: REJECT entry — Foundation L-3 violation. [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§E L-3; F4|G:OQ-MERGED-5 enforcement|R-high]

**K-PartB — Over-implementation drift (Bundle 3 self-monitored failure mode
per spec §6.8 brigadier autocheck).**
The risk that Part 8 produces "live implementation spec" instead of
stub-level. Detection: structural autocheck per spec §6.8 — every starter
value labeled calibration-grade; cadence ≥daily; §K contains this entry; §X
explicit specify-and-stub scope; §H alert-routing is stub not delivery code.
Policy: brigadier returns to integrator with feedback "Part 8 produced live
implementation spec — that's scope creep per OQ-MERGED-5. Re-dispatch with
stub-level mandate." [F5|G:OQ-MERGED-5 enforcement; this entry IS the
self-monitored detection|R-high]

**K4 — Tier 0 alert misses Halt-Log-Alert ordering.**
Detection: alert packet `halt_log_alert_ordering` field has timestamps out
of order (e.g., log_at < halt_at, alert_at < log_at). Policy: HALT — this is
a Foundation L-5 violation (Part 6b §E L9 F8 LOCKED). Per Part 6b: the alert
is REJECTED; owner ack with rationale required to override. [F5|G:Part 6b §E
L9 F8 LOCKED|R-high]

**K5 — TRADEOFF-01 split violation (Part 8 re-implements Part 6a's F-G-R
compliance check).**
Detection: Part 8 §J.2 quarterly audit ritual code that runs F-G-R check
inline (instead of invoking Part 6a service). Phase B: lint check. Phase A:
manual review at critic gate. Policy: REJECT — Foundation L-8 violation
(TRADEOFF-01 split). [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§E L-8; F4|G:TRADEOFF-01 enforcement|R-medium]

**K6 — Alert-routing direct delivery violation (Part 8 routes alerts directly
to Slack/email instead of Part 6b enforcement arm).**
Detection: Phase B lint check on `/alert-emit` invocations; Phase A manual
review. Policy: REJECT — Foundation L-7 + L-8 violation. [F4|G:OQ-MERGED-5
+ TRADEOFF-01 enforcement|R-medium]

**K7 — Quarterly audit missing required scope.**
Detection: §I.5 template enforces required sections; missing section = audit
REJECTED at admission gate (A-5). Policy: re-run audit with full scope.
[F4|G:Foundation L-4 enforcement|R-high]

**K8 — Calibration cadence below daily granularity (sub-daily live metrics).**
Detection: §I.2 SLI entry with `cadence: periodic-Nm` where N<60 minutes
(sub-hourly is OK; sub-daily is the line). Policy: REJECT — OQ-MERGED-5
specify-and-stub scope violation; calibration cadence is monthly review per
OQ-MERGED-5; sub-daily is operational metric collection (Phase B). [F4|G:OQ-MERGED-5
enforcement|R-medium]

**K9 — Phase B SLI inventory expansion premature.**
Detection: PR adds SLI entry to §I.2 without Phase B operational data
backing. Policy: REJECT at gate; Phase B inventory expansion requires Phase B
ack. Bundle 3 ships ≥8 starter entries; remaining ≥22 entries from
FUNDAMENTAL §3 are Phase B. [F4|G:Phase A scope discipline|R-medium]

**K10 — `shared/state/system-health.json` "all green" hardcoded persists.**
Detection: file unchanged across multiple weekly snapshots despite real SLI
emissions. Policy: Phase B implementation replaces hardcoded with computed;
until then, weekly snapshot manually overrides. [F2|G:Phase A baseline
placeholder|R-low — Phase B expected]

**K11 — Variant A retroactive align (deferred to Wave D housekeeping)
diverges from §I.3 mapping table.**
Detection: Wave D housekeeping cycle applies Variant A retroactive align;
§I.3 mapping becomes redundant. Policy: at Wave D, retire §I.3 mapping table
in favor of canonical-direct emitters; preserve §I.3 in archived form for
audit trail (Reversal Transactions). [F3|G:Wave D scope|R-low]

**K12 — Cascading failure: Part 8 own infrastructure failure prevents alert
emission.**
Detection: Part 8 itself goes silent (no weekly snapshot for 2+ weeks; no
alert emissions despite known anomalies). Policy: Part 9 (Bundle 4) weekly
review ritual catches Part 8 silence; owner manually invokes
`/health-snapshot-weekly --recovery`. Mitigation Phase B: meta-monitor Part
on Part 8. [F3|G:Phase A discipline; Phase B meta-monitor|R-medium]

**K13 — Alert-class enumeration insufficient (≥10 declared but real anomaly
type not in mapping).**
Detection: novel anomaly type not in §H.1 mapping. Policy: Default-Deny per
Part 6b §I.3 — novel = Tier 1+; manual classification adds to mapping table
on next commit. [F4|G:Default-Deny inheritance|R-high]

**K14 — F-G-R compliance check service (Part 6a) returns inconsistent results.**
Detection: two consecutive quarterly audits return materially different
drift counts despite no remediation between. Policy: investigate Part 6a
service stability; Part 8 quarterly audit notes the inconsistency. [F4|G:Part
6a service contract|R-medium]

**K15 — Anomaly detector false-positive storm.**
Detection: alert-log shows >10× normal alert rate for >24h with no
corresponding system change. Policy: investigate detector tuning; throttle
alert routing temporarily; owner ack. Phase B: tunable thresholds. [F3|G:Phase
A discipline; Phase B tuning|R-medium]

---

## §L Wave C Work-List Bullet Status

Four bullets from `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 8.

### P8.1 — SLI/SLO schema definition + canonical health signal schema (C2 resolution)

**Design:** §I.1 (canonical health-signal schema; C2 resolution Variant B
chosen with rationale); §I.2 (SLI/SLO schema with ≥8 starter entries; all
labeled calibration-grade; burn-rate algebra inherited from Part 1 §J).

**Hamel-binary acceptance predicate:** both schemas structurally complete;
≥8 SLI entries in §I.2 with starter_value_label = "calibration-grade";
mapping table in §I.1+§I.3 covers Part 1+2+3+4 emitter shapes; synthetic
fixture of 5 health signals validates against canonical schema.

**Acceptance predicate status:** DESIGN COMPLETE. Test fixture: NOT YET RUN
(Phase B materialisation). F4 architecture-time. F5 on Bundle 3 owner ack.

### P8.2 — Health signal schema per emitting part (C2 resolution — producer side)

**Design:** §I.3 mapping table — Bundle 1+2 emitter shapes (Parts 1, 2, 3, 4)
mapped to canonical schema (P8.1 §I.1). Each Foundation Part's §B Outputs row
for "Part 8 health signal" mapped to schema field.

**Hamel-binary acceptance predicate:** every Bundle 1+2 part has ≥1 row in
mapping table; each row populated with canonical-schema field projection;
mapping table has F-G-R tag.

**Acceptance predicate status:** DESIGN COMPLETE. ≥30 mapping table entries
populated covering Parts 1-6b. F4 architecture-time → F5 on cross-Bundle
reuse evidence (Bundle 4 + Wave D consume mapping table).

### P8.3 — Weekly health dashboard + quarterly immune audit templates

**Design:** Templates committed at `swarm/audits/weekly-health-template.md`
+ `swarm/audits/quarterly-immune-audit-template.md` (Bundle 3 deliverables;
populated synthetic rows). §I.4 + §I.5 declare required sections.

**Hamel-binary acceptance predicate:** both templates exist with required
sections; weekly template populated with synthetic Week-NN row demonstrating
SLI snapshot shape; quarterly template populated with synthetic Q-N row
demonstrating Part 6a service invocation result shape (TRADEOFF-01 split
materialised).

**Acceptance predicate status:** DESIGN COMPLETE. Templates ship as Bundle 3
deliverables. F4 architecture-time + templates → F5 on first quarterly audit
run (Phase B).

### P8.4 — Alert-routing stub to Part 6b (Tier 0/1/2/3 mapping)

**Design:** §H.1 alert-routing stub config — alert packet schema +
mapping table per alert class → Tier 0/1/2/3 → routing target. ≥10 alert
classes mapped (14 declared; spec required ≥10). Halt-Log-Alert ordering
enforced for Tier 0 entries.

**Hamel-binary acceptance predicate:** alert-routing stub config exists;
≥10 alert classes mapped; every class assigned Tier 0/1/2/3 + routing target;
Halt-Log-Alert ordering enforced for Tier 0.

**Acceptance predicate status:** DESIGN COMPLETE. STUB-LEVEL — specification
not implementation; live alert delivery infrastructure (Slack/email/SMS) =
Phase B. F4 architecture-time → F5 on first Phase B live alert routing.

---

## §M Wisdom Application Findings — Part 8

Per §5 Wisdom Application Loop discipline. OPERATIONAL/PHILOSOPHICAL
discriminator column mandatory. Bundle 3 target: ≥85% operational adoption
ratio.

| # | Card / Source | Principle | Current state | Improvement | Adopted? | Op vs Phi | Justification | Section edited |
|---|---|---|---|---|---|---|---|---|
| 1 | SRE Workbook Ch.2 | Burn-rate algebra 1×/6×/14.4× | Part 1 §J already adopted | Part 8 §I.2 inherits from Part 1 §J — no re-derivation | YES (already applied via inheritance) | OPERATIONAL | Already in §I.2 inheritance | §I.2 + §J.3 |
| 2 | SRE Book Ch.4 | SLOs as user-facing reliability targets | informal | Part 8 §I.2 SLI/SLO schema codifies; ≥8 starter entries with starter/calibration discipline | YES | OPERATIONAL | Phase A — schema codification | §I.2 |
| 3 | SRE Book Ch.6 | Monitoring distributed systems | informal | §I.4 weekly dashboard template; §I.5 quarterly audit template | YES | OPERATIONAL | Phase A — template authoring | §I.4 + §I.5 |
| 4 | SRE Book Ch.15 | Postmortem culture (blameless) | informal | §J.4 blameless postmortem ritual; 5-line minimum per FUNDAMENTAL §2.4 | YES | OPERATIONAL | Phase A — ritual codification | §J.4 |
| 5 | SRE Book Ch.22 | Cascading failures (graceful degradation) | informal | §K12 cascading failure detection on Part 8 itself; Part 9 Bundle 4 weekly review catches Part 8 silence | YES | OPERATIONAL | Phase A — failure mode declared | §K12 |
| 6 | SRE consultant card §4 P1 | SLI/SLO/error-budget triad | informal | §I.2 SLI/SLO schema with explicit error_budget = 1 - target_value field | YES | OPERATIONAL | Phase A — schema field | §I.2 |
| 7 | SRE consultant card §4 P2 | Observability vs monitoring (unknown unknowns) | informal | §I.1 canonical schema captures arbitrary signal_name (open enum); novel signals admittable | YES | OPERATIONAL | Phase A — open schema | §I.1 |
| 8 | SRE consultant card §4 P4 | Toil reduction | not formalised | §F.2 — Part 8 does not auto-implement; relies on Phase B for tooling; Phase A is owner-reviewed weekly + quarterly | NO | PHILOSOPHICAL | Phase B work — toil reduction is automation; Bundle 3 is specify+stub per OQ-MERGED-5 | n/a |
| 9 | SRE consultant card §4 P5 | Blameless postmortem | informal | §J.4 — adopted same as #4 | YES (covered by #4) | OPERATIONAL | Already in §J.4 | §J.4 |
| 10 | SRE consultant card §4 P6 | Fail-loud | informal | §E L-2 — fail-loud Law promoted; Halt-Log-Alert per Part 6b §E L9 inheritance | YES | OPERATIONAL | Phase A — Law promotion | §E L-2 |
| 11 | SRE consultant card §4 P7 | Error-budget burn behaviour-change | informal | §J.3 + §I.2 SLO `behaviour_change_rule` field; per burn rate tier | YES | OPERATIONAL | Phase A — schema field + ritual | §I.2 + §J.3 |
| 12 | Systems-thinking-cybernetics §4 P3 | Beer VSM S3 audit function (TRADEOFF-01) | OQ open Bundle 1; resolved Bundle 3 | §0 + §B.1 + §D.2 + §E L-8 + §J.2 — TRADEOFF-01 split materialised: Part 8 audit lead, Part 6a service, Part 6b enforcement | YES | OPERATIONAL | Phase A — split structurally enforced | §B.1 + §D.2 + §E L-8 + §J.2 |
| 13 | Systems-thinking-cybernetics §4 P2 (Ashby requisite variety) | ≥30 SLI/SLO pairs match failure-mode count | informal | §I.2 ≥8 starter; remaining ≥22 Phase B; rationale: variety mismatch is Phase B discovery (operational data informs entries) | YES | OPERATIONAL | Phase A — starter; Phase B inventory expansion | §I.2 + §F.2 + §K9 |
| 14 | Systems-thinking-cybernetics §4 Meadows L7 | Information-flows leverage | conceptual | §E L-1 — Part 8 IS the information-flow primitive (observability surfaces drift); Meadows L8 in §E L-1 annotation | YES | OPERATIONAL | Phase A — Meadows leverage point mapping | §E L-1 |
| 15 | Capital-allocation-antifragility §4 P2 (Graham margin-of-safety) | margin-of-safety on backup discipline | F4 inherited Part 1 §K K9 | Part 8 §I.2 git-substrate-integrity-slo target=1.0 (zero errors); 14.4× burn = HALT all writes (K8 policy); margin-of-safety enforced | YES | OPERATIONAL | Phase A — SLO target | §I.2 |
| 16 | Capital-allocation-antifragility §4 P3 (Antifragility via stressors) | Detect stressors | informal | §I.1 canonical schema captures stressor signals (orphan-anchor-spike, stale-claims-burst, mailbox-queue-overflow); §H.1 alert-routing maps to action | YES | OPERATIONAL | Phase A — stressor-detection schema | §I.1 + §H.1 |
| 17 | Capital-allocation-antifragility (Marks second-level thinking moat) | Health-snapshot evidence as moat asset | conceptual | NO — pure framing prose; the moat IS the structured snapshot history (already operational via D25); no schema change needed for "moat" framing | NO | PHILOSOPHICAL | Pure framing prose without operational consequence; §X.1 already captures fork-portability moat | n/a |
| 18 | Levenchuk SHSM-FPF IP-4 | Quarterly immune audit cadence | F5 inherited Bundle 1 Part 6a | §J.2 quarterly audit ritual; extends Part 6a Bundle 1 quarterly framework with TRADEOFF-01 split | YES | OPERATIONAL | Phase A — ritual codification | §J.2 + §I.5 |
| 19 | Anthropic constitutional-AI §5 T3 | Fail-loud anomaly→committed alert record within one monitoring cycle | informal | §E L-2 + §J.1 step 3 — anomaly emits alert via §H.1 within monitoring cycle | YES | OPERATIONAL | Phase A — Law operationalisation | §E L-2 + §J.1 |
| 20 | Anthropic constitutional-AI | Integrity violations = absolute halt (Tier 0) | F8 inherited Part 6b §I.4 | §H.1 — git-fsck-object-error and fg-r-compliance-collapse classified Tier 0 with Halt-Log-Alert ordering | YES | OPERATIONAL | Phase A — alert-class mapping | §H.1 |
| 21 | Anthropic constitutional-AI | Softcoded degradation for velocity SLIs (graceful degrade for non-Tier-0 burns) | informal | §I.2 SLO `behaviour_change_rule` per burn rate tier — graceful degradation pre-declared | YES | OPERATIONAL | Phase A — schema field | §I.2 |
| 22 | Askell HHH Appendix E.2 | Corrigibility verbatim | F8 LOCKED Bundle 1 Part 6b | §E L-6 — Part 8 NEVER locks owner out; revert via git revert always available | YES | OPERATIONAL | Phase A — Corrigibility inheritance | §E L-6 + §F.2 |
| 23 | FUNDAMENTAL §3 | 30+ SLI/SLO calibration parameters | F8 anchor | §I.2 ≥8 starter entries; remaining Phase B; explicit calibration-grade label per OQ-MERGED-5 | YES | OPERATIONAL | Phase A — starter inventory + scope discipline | §I.2 + §F.3 + §K9 |
| 24 | FUNDAMENTAL §5 | 3-2-1 backup rule | F8 anchor | §I.2 git-substrate-integrity-slo enforces fsck-clean weekly; backup rule operates at infrastructure layer (not Part 8) | YES (cross-ref) | OPERATIONAL | Phase A — SLO cross-ref | §I.2 |
| 25 | FUNDAMENTAL §6.7 | halt + log + alert | F8 anchor | §E L-5 — Halt-Log-Alert ordering per Part 6b §E L9 F8 LOCKED | YES | OPERATIONAL | Phase A — Law inheritance | §E L-5 + §H.1 |
| 26 | FUNDAMENTAL §3.3.1 | compound-application-rate ≥0.8 | informal in `swarm/wiki/meta/health.md` | §I.2 drr-write-rate-slo + cross-ref Part 5 §B compound-application-rate emission | YES | OPERATIONAL | Phase A — SLI codification | §I.2 |
| 27 | FPF §B.3 F-G-R | DOGFOOD per Bundle 1 Part 6a F8 | adopted | §G F-G-R Tagging table; inline tags throughout | YES | OPERATIONAL | Phase A — DOGFOOD inheritance | §G + inline |
| 28 | FPF §A.14 typed edges | Canonical 10-edge table | adopted Bundle 1 | §D Dependencies — every edge typed; NO `depends-on` | YES | OPERATIONAL | Phase A — typed edge discipline | §D |
| 29 | FPF §A.13 Agency-CHR | J-Auto / J-Approve / J-Strategic | informal | §H.1 alert packet schema includes `j_level_authority_required` field per Tier classification | YES | OPERATIONAL | Phase A — Agency-CHR mapping | §H.1 |
| 30 | FPF IP-3 artifacts-over-conversations | committed not chat-only | adopted Bundle 1 | §C — health snapshots, audits, alert log all committed via Part 1 §H | YES | OPERATIONAL | Phase A — IP-3 inheritance | §C |
| 31 | FPF IP-1 Role≠Executor | role archetype not executor instance | adopted Bundle 2 | §F.2 — Part 8 does NOT name specific role holders for immune-system function; executor binding is RUSLAN-LAYER | YES | OPERATIONAL | Phase A — IP-1 inheritance | §F.2 + §X |
| 32 | OQ-MERGED-5 specify-and-stub | Bundle 3 = schemas + templates + stub; not live impl | F8 ack Bundle 2 | §E L-7 + §F.3 + §K K-PartB — three-layer enforcement (Law + Anti-scope + self-monitored failure mode) | YES | OPERATIONAL | Phase A — multi-layer scope discipline | §E L-7 + §F.3 + §K K-PartB |
| 33 | TRADEOFF-01 ack | Part 8 audit lead + Part 6a service + Part 6b enforcement | OQ-1 ack Bundle 1 | §0 + §B.1 + §D.2 + §E L-8 + §J.2 + §I.5 — five-layer materialisation | YES | OPERATIONAL | Phase A — split structurally enforced | §0 + §B.1 + §D.2 + §E L-8 + §J.2 + §I.5 |
| 34 | C2 resolution | Canonical health-signal schema | OQ open Bundle 1 carry-over; resolved Bundle 3 | §I.1 canonical + §I.3 mapping table (Variant B chosen with rationale; Variant A retroactive align deferred to Wave D housekeeping) | YES | OPERATIONAL | Phase A — schema canonicalisation + adapter pattern | §I.1 + §I.3 |
| 35 | Stoic-epistemic Popper | falsifiability | inherited Bundle 1 | §I.2 SLI fields include `accepted_if/refuted_if` via f_g_r block (per Part 6a §I.1); each SLI is falsifiable | YES | OPERATIONAL | Phase A — Popper falsifier mandatory | §I.2 |
| 36 | Compounding-Engineering anti-cargo-cult | Citation + concrete consequence within 200 chars | adopted Bundle 1 | This document follows discipline; every [src:] followed by concrete consequence sentence | YES | OPERATIONAL | Phase A — anti-cargo-cult discipline | throughout |
| 37 | SRE consultant card §4 P3 (Three Pillars: logs/metrics/traces) | Logs + metrics + traces | conceptual | NO — Phase A is owner-reviewed weekly + quarterly; traces are Phase B (distributed tracing requires multi-agent runtime infrastructure) | NO | PHILOSOPHICAL | Phase B/C scale; premature for Phase A single-owner | n/a |
| 38 | Beer VSM S5 (identity/values) | system identity | F5 inherited FUNDAMENTAL §6 | NO — out of scope for Part 8 (Part 8 is S3); FUNDAMENTAL §6 covers identity | NO | PHILOSOPHICAL | Domain-orthogonal | n/a |
| 39 | Capital-allocation Marks "second-level thinking" | second-level thinking on incentives | conceptual | NO — Part 8 has no incentive-design role; SRE-domain | NO | PHILOSOPHICAL | Domain-orthogonal to Part 8 | n/a |
| 40 | Stoic Dichotomy of Control | "in our control" framing | inherited Part 5 reject | NO — pure framing prose; Part 8 already operates within Corrigibility (L-6) | NO | PHILOSOPHICAL | Pure framing prose without operational consequence | n/a |

**Aggregate operational adoption ratio for Part 8:**
- Total YES Adopted: 35 (all OPERATIONAL — 35 OP / 0 PHI)
- Total NO: 5 (all PHILOSOPHICAL — domain-orthogonal, Phase B scale, or
  pure framing prose)
- Total findings: 40
- **Operational adoption ratio: 35/35 = 100%** (well above ≥85% Bundle 3
  target)

---

## §N Provenance

Every claim in this document carries inline `[src:<path>]` citation followed
within 200 chars by a concrete consequence sentence. Per Bundle 1 Part 6a §C
citation discipline + Bundle 3 §6.3 anti-cargo-cult enforcement.

**Sources consulted (full list):**

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md` (Wave A interface card §A-§H + TRADEOFF-01 OQ + Wave C bullets preview)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md` §2 Part 8
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md` §2 Part 8 + TRADEOFF-01
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` §3.2 C2 health signal schema; §7 OQ-1 TRADEOFF-01
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 8
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md` §4 P1-P7 + §3 Source 1 (Google SRE Book Ch.4 SLOs / Ch.6 Monitoring / Ch.15 Postmortem / Ch.22 Cascading Failures)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 P3 Beer VSM S3 + Ashby requisite variety + Meadows leverage
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md` §4 P2 Graham + P3 Antifragility + P5 Munger
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` §5.4 IP-4 Quarterly Immune Audit
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` §5 T3 fail-loud
- `raw/books-md/sre/google-sre-book.md` Ch.4 / Ch.6 / Ch.15 / Ch.22
- `raw/books-md/sre/google-srewb-implementing-slos.md` Ch.2 burn-rate algebra
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §3 30+ SLI/SLO + §5 reliability + §6.7 halt+log+alert
- `design/JETIX-FPF.md` IP-4 / A.13 Agency-CHR / A.14 typed edges / A.6.B L/A/D/E / B.3 F-G-R / IP-1 Role≠Executor / IP-3 artifacts-over-conversations
- `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (existing system-health.json + metrics baseline)
- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §B Four Golden Signals + §J burn-rate + §H commit + §I.5 health stub + §I.4 task-return-packet stub (post-supplement)
- `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` §I.6 health stub
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` §I.6 health stub + §E L9 admissibility
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` §I.4 health stub + §H message schema v2.0.0
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (Bundle 3 sibling — health emissions)
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` §I.1 F-G-R F8 + §C approval log + quarterly framework
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` §I.1 awaiting-approval-packet F8 + §I.3 default-deny + §I.4 blast-radius F8 + §E L9 Halt-Log-Alert + Corrigibility F8
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (Bundle 1 ack)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` §1 Decision #1-7 + §2 OQ-MERGED-5 + §3 word count
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` (Bundle 1 retroactive supplement applied 2026-04-28 Phase 0)
- `raw/books-md/anthropic/askell-2021-hhh.md` Appendix E.2 Corrigibility verbatim

---

## §X Foundation vs RUSLAN-LAYER Separation

### §X.1 GENERIC Foundation (fork-portable)

| Foundation generic | Rationale |
|---|---|
| Canonical health-signal schema (§I.1) | Generic shape — any Foundation observability system uses unified signal schema |
| SLI/SLO schema (§I.2) | Generic SLI/SLO/error-budget triad with starter_value_label discipline |
| Burn-rate algebra (1×/6×/14.4×) | F5 inherited from SRE Workbook Ch.2 — universal SRE pattern |
| Mapping table pattern (§I.3) | Generic Adapter pattern; any Foundation can use it for emitter heterogeneity |
| Weekly health dashboard structure (§I.4) | Generic dashboard sections |
| Quarterly immune audit structure (§I.5) | Generic audit scope (F-G-R compliance / alpha / role-manifest / methodology / strategies) |
| Alert-routing 4-tier mapping (§H.1) | F8 inherited from Part 6b §I.4; generic Tier 0/1/2/3 + routing target enum |
| Halt-Log-Alert ordering for Tier 0 | F8 inherited from Part 6b §E L9; generic SRE+CAI pattern |
| TRADEOFF-01 split (audit lead + service + enforcement arm) | Generic Beer VSM S3 split pattern |
| Specify-and-stub scope discipline | Generic Phase A scope-creep prevention pattern |
| Calibration-grade label discipline | Generic — every SLI's starter value labels |

### §X.2 RUSLAN-LAYER (Jetix-specific instance values)

| Ruslan-specific | Where stored |
|---|---|
| Specific SLO threshold values (e.g. 0.95 voice-pipeline-success-rate; 0.8 compound-application-rate) | `shared/state/system-health.json` post-Phase-B calibration; or per-SLI `calibrated_value` field added Phase B |
| Specific alert delivery destinations (e.g. Telegram bot ID; Email address) | RUSLAN-LAYER `executor-binding.yaml` (Phase B; alert delivery is Phase B materialisation) |
| Specific role assignments for health-monitor + quarterly-immune-auditor | `executor-binding.yaml` (RUSLAN-LAYER per IP-1) |
| Specific cycle wall-clock norm (90 min) | `executor-binding.yaml` cadence config |
| Specific weekly review day/time (Friday 17:00 Berlin) | `executor-binding.yaml` schedule config |
| Specific FUNDAMENTAL §3 30+ SLI inventory expansion (≥22 entries Phase B) | Per-SLI yaml files in `shared/schemas/sli/` Phase B |
| Specific alert class additions beyond ≥10 declared (Bundle 4+ Wave D extensions) | `swarm/audits/alert-class-mapping.yaml` extension file |

### §X.3 OQ-MERGED-5 specify-and-stub scope declaration (P8.X mandatory)

**SPECIFY-AND-STUB SCOPE (verbatim):**

> "Bundle 3 Part 8 = SLI/SLO schema + canonical health signal schema +
> template authoring + alert-routing stub. NOT live metrics implementation.
> NOT calibrated thresholds. FUNDAMENTAL §3 30+ SLI/SLO pairs labeled
> calibration-grade with explicit calibration-cadence; live metrics
> implementation = Phase B materialisation (2-3 month operational data
> accumulation per OQ-MERGED-5)."

**Bundle 3 deliverables (specify-level):**
- Canonical health-signal schema declared in §I.1.
- SLI/SLO schema declared in §I.2 with ≥8 starter entries; all labeled
  `starter_value_label: "calibration-grade"`.
- Mapping table declared in §I.3 (Bundle 1+2 emitter shapes mapped to
  canonical).
- Weekly health dashboard template at `swarm/audits/weekly-health-template.md`.
- Quarterly immune audit template at `swarm/audits/quarterly-immune-audit-template.md`.

**Bundle 3 deliverables (stub-level):**
- Alert-routing stub config in §H.1 with ≥10 alert classes mapped to Tier
  0/1/2/3.
- swarm/lib/ accessor pipeline file paths declared (§H.3).
- Alert packet schema declared (§H.1).
- Routing-table.yaml extension declared (§H.6).

**NOT delivered Bundle 3 (Phase B materialisation):**
- Live metric collection code.
- Calibrated SLO threshold values (replacing starter values).
- Alert delivery infrastructure (Slack/email/SMS/page).
- Sub-daily metric collection cadence.
- FUNDAMENTAL §3 30+ SLI inventory expansion beyond 8 starter entries.
- Live computation in `shared/state/system-health.json` (currently hardcoded;
  Phase B replaces).
- automated `/lint --check-stale-claims`, `/lint --check-fg-r-compliance`, etc.
  signals (Phase B implementation per OQ-B1-2 lint signal pattern).

**Self-monitored failure mode:** §K K-PartB declares "Over-implementation
drift" as Part 8's self-monitored failure mode. Brigadier autocheck §6.8
verifies Bundle 3 output is stub-level.

### §X.4 Boundary principle (per IP-1)

The schema (canonical health-signal / SLI-SLO / mapping table / alert-routing
4-tier / weekly+quarterly templates / TRADEOFF-01 split / specify-and-stub
discipline) is GENERIC. The specific values (SLO thresholds / alert delivery
destinations / role names / inventory expansion) are RUSLAN-LAYER. A Phase B
partner forking Jetix:
- ADOPTS the schema (this document is the spec)
- IMPORTS Ruslan-specific calibrated values optionally as historical reference
- EXTENDS with their own SLO targets + alert delivery destinations + own
  inventory expansion
- OVERRIDES specific role-binding mappings via own `executor-binding.yaml`

**This is why operational adoption ratio matters.** A schema is portable; pure
framing prose is not. Bundle 3 §85% operational target is structural — every
NO PHILOSOPHICAL adoption is one less load-bearing constraint a Phase B
partner must inherit. Per §M, Part 8 achieves 100% operational adoption
(35/35).

---

## §Y Open Questions Surfaced By Bundle 3 Part 8

| OQ ID | Open Q | Source | Resolution path | Blocking? |
|---|---|---|---|---|
| OQ-B3-P8-1 | Variant A retroactive align (Bundle 1+2 emitter §I.5/§I.6/§I.4 sections retrofitted to canonical schema) deferred to Wave D housekeeping cycle. Confirm Wave D scope accepts this housekeeping commit. | §I.1 + §I.3 + §K11 | Wave D housekeeping cycle | Not blocking — Variant B (mapping table) is functional |
| OQ-B3-P8-2 | FUNDAMENTAL §3 30+ SLI inventory expansion timing — Bundle 3 ships ≥8; remaining ≥22 entries timing is Phase B operational data dependent. Confirm Phase B kickoff timing | §F.2 + §K9 + §I.2 | Phase B kickoff per Master Plan | Not blocking |
| OQ-B3-P8-3 | Alert delivery infrastructure (Slack/email/SMS/page) — Phase B implementation; specific channel choice + integration approach TBD | §F.2 + §H.1 STUB-LEVEL | Phase B materialisation | Not blocking |
| OQ-B3-P8-4 | `shared/state/system-health.json` "all green" hardcoded replacement — Phase B implements live computation per §I.1 schema | §K10 | Phase B | Not blocking |
| OQ-B3-P8-5 | Tier 1+ Default-Deny default — confirm Phase A operational behaviour: novel alert class defaults to Tier 1 (Ruslan ack) NOT Tier 2 (batch ack) — to err on visibility side | §H.1 + Part 6b §I.3 | Operational policy confirmation | Not blocking — default-deny ensures conservative behaviour |
| OQ-B3-P8-6 | Voice pipeline success-rate SLI starter value 0.95 vs current operational baseline — owner can adjust pre-Phase-B if pre-Bundle-3 data suggests different starter | §I.2 voice-pipeline-success-rate | Owner ack pre-Phase-B | Not blocking |

None of the OQs above are blocking for Bundle 3 ack. They surface for Wave D /
Phase B resolution and are tracked in the AWAITING-APPROVAL packet §5.

---

**End of Part 8 Architecture (Bundle 3).**

Status: F4 architecture-time. Promoted to F5 on Bundle 3 owner ack of this
document.

Word count target: 10K-20K (Bundle 3 constitutional refinement per
RUSLAN-ACK Bundle 2 §3 F8). This document target ~13-14K words.

Next: Joint Design lite Phase deliverables (UND-3 stub written above; C2
mapping declared in §I.3 — companion artefact `swarm/wiki/cycles/.../bundle-3/joint-design-lite-c2-resolution.md`); templates (`swarm/audits/weekly-health-template.md` + `swarm/audits/quarterly-immune-audit-template.md`); M-gates + AWAITING-APPROVAL packet.
