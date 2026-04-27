---
title: Part 6b — Human Gate — Architecture
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6b
parent_part: 6
split_rationale: "OQ-MERGED-1 override Ruslan walkthrough 2026-04-27: scale-readiness Phase B/C/D, real-time gate vs quarterly audit cadence independence, Default-Deny constitutional ownership"
status: ruslan-acked-canonical
wisdom_loop_adoption: "YES=11 NO=3 ALREADY_APPLIED=5"
critic_findings: "IP-1 clean; A.14 edges all typed; F-G-R self-dogfood complete; §6.1 never-list machine-readable 11-entry enum confirmed; §F.3 three-category Stoic structure confirmed; §H deep-module confirmed; §0 VSM S3 confirmed; corrigibility L9 strengthened with Askell verbatim; §J.4 burn-rate expanded to 1x/6x/14.4x; §K blameless-postmortem quote added + K-cascading new failure mode + Senge Law 11 note; §C.4 supersedes-not-corrects precision added; §B.6 SRE Book explicit citation; §G ASL-tier analogue note added; §M full 19-row wisdom table populated; NO: sycophancy detection mechanism (Wave D), batch sub-grouping algorithm (Phase B), semantic identity-claiming detection (Wave D)"
F: F8
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md decisions #3 + #4 + #5 — F4→F8 constitutional. Default-Deny FRAMEWORK F8 constitutional ACK; blast-radius 4-tier structure (0/1/2/3) accepted as Foundation generic; AWAITING-APPROVAL packet schema with gate_class enum {stop_gate, stage_gate, draft_promotion} FROZEN as permanent contract for all future packets across all cycles. Future modification requires AWAITING-APPROVAL constitutional gate."
ClaimScope: "Foundation generic — Default-Deny framework, blast-radius tier structure, AWAITING-APPROVAL packet schema, escalation taxonomy structure, halt-log-alert primitive, stage-gate predicates Hamel-binary discipline. RUSLAN-LAYER: specific whitelisted action classes, specific blast-radius assignments per action class, specific SLA values, terminal acker (Ruslan)."
R:
  refuted_if: "Any canonical promotion bypasses Part 6b gate; OR any §6.1 violation goes silent (no halt + log + alert); OR any novel action executes without Default-Deny check"
  accepted_if: "100% of canonical promotions trace to Part 6b gate event; halt-log-alert fires on every §6.1 violation; novel action rate categorized 100%"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/mgmt-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/philosophy-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/engineering-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/investor-expert-margin-of-safety.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
  - raw/books-md/anthropic/bai-2022-cai.md
  - raw/books-md/anthropic/askell-2021-hhh.md
  - raw/books-md/event-sourcing/young-cqrs-2010.md
  - raw/books-md/sre/google-sre-book.md
  - raw/books-md/sre/google-srewb-implementing-slos.md
---

# Part 6b — Human Gate — Architecture

> **Self-exemplification.** This document dogfoods every discipline it specifies: L/A/D/E lane discipline,
> F-G-R tagging on all promoted claims, A.14 typed edges only, Foundation vs RUSLAN-LAYER split explicit
> throughout, citation + concrete consequence within 200 characters per reference. This is not decoration —
> it is the acceptance criterion for Part 6b's own canonical promotion.
> [src:part-6-governance-provenance-human-gate.md:§E "l_a_d_e_self_exemplifies"]

---

## §0 Executive Summary

Part 6b — Human Gate — is the **real-time constitutional enforcement arm** of Part 6 Governance
in the Jetix Foundation. Where Part 6a (Provenance Officer) runs quarterly retrospective audits
of epistemic drift and citation health, Part 6b operates per-action, per-artefact in real time
at the exact moment an action or draft reaches the boundary between proposal and execution.
This is the IP-4 immune-system function made operational: the gate that every artefact,
every action, and every agent must pass before acquiring canonical status or before executing
outside the pre-approved whitelist. [src:part-6-governance-provenance-human-gate.md:§0 "VSM S3 authority"]

**Placement in Beer VSM.** Part 6 Governance occupies the System-3 (S3) enforcement and audit
position in the Viable System Model applied to Jetix. S3 is the internal regulation arm — it
does not produce content, it enforces the constitutional conditions under which content may be
produced and promoted. Part 6a is the S3 audit lead: periodic, retrospective, compliance-
reporting. Part 6b is the S3 enforcement arm: real-time, prospective, gate-issuing. Part 8 is
the S3 audit support: health-signal consumer and burn-rate monitor (when defined). These are
structurally distinct roles within S3: Beer VSM S3 requires both optimisation (6a quarterly
review) and operational enforcement (6b real-time gate) to function. Neither substitutes for
the other; together they complete S3's dual mandate. A single S3 node that tries to do both
real-time enforcement and periodic audit risks the oscillation pattern Beer identifies when
authority is split without clean cadence separation — the Wave C split by cadence (event-driven
vs quarterly) is the explicit mitigation.
[src:part-6a-provenance-officer/architecture.md:§0 "VSM S3 authority — S3 audit lead vs enforcement arm"]
[src:systems-thinking-cybernetics.md:§5 "Beer VSM S3 authority — audit and optimisation split"]

**Default-Deny as constitutional encoding.** FUNDAMENTAL §6.1 last bullet is unambiguous:
"якщо action не categorized — default deny + escalate, не creative interpretation."
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] This is not a policy preference.
It is a constitutional invariant encoded at F8 — the highest formality level in the F-G-R
taxonomy, meaning it is a structural property of the system, not a behavioral convention that
agents can choose to follow or not. Every uncategorized action that reaches Part 6b produces
a deterministic outcome: halt + escalate to human owner + log audit entry. No creative
interpretation path exists. This is what makes Part 6b a constitutional enforcement arm rather
than a compliance checklist.

**The halt-log-alert primitive.** FUNDAMENTAL §6.7 defines the three-step response to any
constitutional violation: halt (action stops immediately), log (audit trail entry written before
any other action), alert (owner notification with artefact path and violation type).
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.7] The ordering is not arbitrary. The
philosophy-expert cell identifies each step as addressing a distinct ethical gap: halt prevents
further damage (non-maleficence); log creates the audit trail before notifications (transparency);
alert ensures the owner can exercise corrigibility (Askell HHH). A system that alerts without
halting treats human oversight as advisory. A system that halts without logging cannot learn.
A system that logs without alerting leaves the owner unable to intervene. Only all three, in
order, satisfy the constitutional requirement. [src:philosophy-expert-multi-mode.md:§E.2]

**Five outputs (5 schemas/configs).** Wave C Bundle 1 materialises Part 6b through five
concrete schema and config artefacts:

1. `shared/schemas/stage-gates.yaml` — Hamel-binary stage-gate predicate registry (P6b.1)
2. `.claude/config/default-deny-table.yaml` — Default-Deny classifier with constitutional never-list (P6b.2)
3. `.claude/config/blast-radius-table.yaml` — 4-tier blast-radius classification (P6b.3)
4. `shared/schemas/awaiting-approval-packet.json` — gate packet schema satisfying UND-4 binding (P6b.4)
5. `.claude/config/escalation-taxonomy.yaml` — L1/L2/L3 HITL escalation tier structure (P6b.5)

**UND-4 binding.** The `gate_class` enum field — `{stop_gate, stage_gate, draft_promotion}` — is the
explicit dependency resolution for UND-4. It appears canonically in `awaiting-approval-packet.json`
and is referenced via JSON Schema `$ref` from all other schemas that require it. This DRY discipline
is constitutional: a gate_class definition scattered across 5 schemas would produce drift that is
detectable only post-hoc, not at schema-submission time.
[src:engineering-expert-multi-mode.md:§1.1 "gate_class canonical in awaiting-approval-packet.json"]

**Investor verdict.** The governance machinery is correctly over-engineered relative to the cost.
Graham's margin-of-safety arithmetic is unambiguous: the cost of a false-positive halt (Tier 0)
is ~10 minutes of investigation; the cost of a missed constitutional violation is potentially
unrecoverable (Tier-0 data including strategic decisions, Locks, and Architecture documents).
The expected-value arithmetic is not close. [src:investor-expert-margin-of-safety.md:§D.1]

---

## §A Inputs

Part 6b accepts five distinct input classes. Each has a declared data shape, event trigger, and
admissibility precondition. No input is processed without passing the admissibility check.
[src:part-6-governance-provenance-human-gate.md:§A]

### A.1 Draft Artefact Submission

**Data shape.** A Markdown file with YAML frontmatter carrying: `proposed_writes[]` (non-empty),
`provenance[]` (non-empty with inline `[src:...]` citations), `F-G-R fields` (F, ClaimScope, R.refuted_if,
R.accepted_if), `acceptance_predicate:` (Hamel-binary, must pass banned-phrase check against
`.claude/config/sg-banned-phrases.yaml`), and optionally `advisory_cai_flag: boolean`.

**Event trigger.** `submit-draft-for-gate-event` — any Part or agent submitting a candidate for
canonical promotion emits this event with the draft path. The gate receives the path, not the draft
content inline, per the AP-1 file-reference-only rule.

**Admissibility preconditions** (all conjunctive; any failure → rejection packet with specific reason):

- `proposed_writes[]` is non-empty (at least one write proposed)
- `provenance[]` is non-empty with at least one inline `[src:...]` citation in the body
- F-G-R fields present: F ≥ F3 (canonical readiness floor); ClaimScope.holds_when non-empty;
  ClaimScope.not_valid_when non-empty; R.refuted_if is a Hamel-binary predicate (banned-phrase
  check passes); R.accepted_if is a Hamel-binary predicate (same check)
- `acceptance_predicate:` field present and passes banned-phrase check
- `gate_class:` field present with value in enum `{stop_gate, stage_gate, draft_promotion}` (UND-4)

Any draft that reaches Part 6b without these fields has already failed Part 6a's citation lint;
the gate check is a redundant enforcement layer, not the primary scanner. Part 6a detects
drift; Part 6b gates each artefact independently at promotion time.
[src:part-6a-provenance-officer/architecture.md:§H "Part 6a detects; Part 6b gates"]

### A.2 Action Proposal with Blast-Radius Candidate Tag

**Data shape.** A tagged action packet: `{action_class, blast_radius_tier_candidate, reversible: bool,
actor, timestamp}`. Submitted by any agent before execution of any non-trivial action.

**Event trigger.** Any agent action that is not on the pre-approved whitelist (i.e., not a Tier-3
routine action in `default-deny-table.yaml`). The action packet precedes execution; the gate
decision precedes the action.

**Admissibility.** Action accepted into auto-execute path ONLY IF:
- `blast_radius_tier_candidate` is Tier-3-routine AND
- `reversible: true` AND
- `action_class` is in `whitelisted_classes` of `default-deny-table.yaml`

All conditions are conjunctive. Any missing condition routes to gate (AWAITING-APPROVAL packet).
[src:mgmt-expert-multi-mode.md:§7 A1 "A1 — Action accepted into auto-execute path ONLY IF"]

### A.3 Novel / Uncategorized Action (Default-Deny Trigger)

**Data shape.** An action description without a blast-radius tag — either because the action class
is new (never classified before) or because the submitting agent omitted the tag.

**Event trigger.** Automatic: absence of `blast_radius_tier` field on an action packet that reaches
Part 6b triggers Default-Deny immediately. No human evaluation of "is this probably safe" occurs.
The constitutional rule is mechanical: no tag → deny + escalate + log.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 last bullet "Default-Deny constitutional"]

**Consequence.** Part 6b halts the action, writes an audit log entry with `trigger: default_deny`,
and emits an AWAITING-APPROVAL packet with `gate_class: stop_gate` for Ruslan's classification
decision. After Ruslan classifies the novel action, it either gets whitelisted (new entry in
`default-deny-table.yaml` RUSLAN-LAYER) or stays denied. The whitelist-as-capital-asset logic
applies: each classification decision is a one-time investment that reduces future friction for
all identical action classes. [src:investor-expert-margin-of-safety.md:§D.2 "amortization effect"]

### A.4 Constitutional Violation Signal (§6.7 Triggers)

**Data shape.** A structured `boundary-violation-event` from any Part or detection mechanism:
`{violation_type, action_description, detecting_part, timestamp, artefact_path_if_applicable}`.
Violation types from FUNDAMENTAL §6.7: `ai_attempted_strategize`, `architectural_change_attempted`,
`sycophancy_detected`, `identity_claiming`, `autonomous_agent_negotiation`, `self_modification_attempt`,
`human_impersonation`, `unstructured_memory_aggregation`, `blast_radius_bypass`.

**Event trigger.** Immediate — constitutional violation signals are not batched. The halt-log-alert
sequence fires within ≤1 second of detection. There is no "accumulate and report" path for
constitutional violations. [src:mgmt-expert-multi-mode.md:§7 D4 "MUST escalate constitutional violations immediately"]

**Admissibility.** All constitutional violation signals are admitted unconditionally. Part 6b does
not evaluate whether the signal "looks real" or "is probably a false positive." False positives
cost ~10 minutes of investigation; missed true positives cost unrecoverable constitutional damage.
Over-triggering is structurally preferred. [src:investor-expert-margin-of-safety.md:§D.3]

### A.5 Part 6a F-G-R Audit Findings (Consumed Input)

**Data shape.** Part 6a's citation scanner findings: `{artefact_path, finding_class, severity,
corrective_action_required}`. Consumed by Part 6b when a gate submission references an artefact
that Part 6a has flagged.

**Boundary with Part 6a.** Part 6b does NOT duplicate the F-G-R scan. It consumes Part 6a's
compliance signal. The typed edge is `methodologically-uses` (Part 6b → Part 6a): Part 6b
consumes Part 6a's F-G-R schema and scanner output; Part 6a defines the schema; neither
duplicates the other's function. [src:mgmt-expert-multi-mode.md:§6 D row 3]

### A.6 Part 8 Health Signals (Placeholder — Part 8 Not Yet Defined)

**Status.** Part 8 (system health monitor) is not yet defined in Wave C. Part 6b declares the
interface: Part 8 will emit `ack-time-anomaly-event` and `burn-rate-alert-event` signals to
Part 6b for routing. Until Part 8 is defined, these signals are declared as a stub interface.
Part 6b produces the timestamp data that Part 8 will consume (submitted_at, acked_at per packet).
[src:investor-expert-margin-of-safety.md:§L OQ-INV-5]

---

## §B Outputs

Part 6b produces six distinct output classes. Each is declared with consumer, data shape, event,
and F-G-R characterisation. Part 6b never writes canonical wiki content directly.
[src:part-6-governance-provenance-human-gate.md:§B]

### B.1 AWAITING-APPROVAL Packet (Primary Output)

**Consumer.** Ruslan (human owner, terminal acker).

**Data shape.** Structured gate document at `swarm/awaiting-approval/<cycle>-<slug>.md`.
Full schema at §I.4 below. Required fields include: `gate_class` (UND-4 binding), `packet_id`,
`timestamp`, `actor`, `summary` (≤3 lines: what, why, consequence-if-approved), `outcomes`
(explicit expected state changes), `provenance` (source artefact path), `ack_request` (three
options: approve-as-is, approve-with-modifications, permanently-reject), `reversibility_class`,
`blast_radius_tier`, `f_g_r_delta` ($ref to f-g-r.json), `review_checkpoint` (one-line "what
specifically did you verify?" field that Ruslan must answer before acking).

**Event.** `gate-submitted-event` — BLOCKED state until Ruslan ack. The packet cannot be
auto-approved. It cannot be modified after submission (append-only per L6). A corrected packet
is a new packet with `supersedes: <prior-packet-id>`.

**F-G-R path.** Current state F4 (operational convention; 8+ confirmed gate packets in
`swarm/gates/` demonstrate consistent structure). Path to F6: 3 consecutive cycles without
schema violation or rejection for schema non-compliance. Path to F8 (Lindy-grade): sustained
application across 20+ cycles; portable to forks without modification.
[src:investor-expert-margin-of-safety.md:§J "F-G-R promotion path for all 5 schemas"]

**SRE Four Golden Signals emitted.** Gate-throughput (packets issued per cycle), ack-latency
(submitted_at → acked_at per packet), halt-rate (§6.1 violations per cycle), approval-rejection-
ratio (approved / total submitted). These signals are data points in the packet and log; SLO
thresholds are Part 8 territory, not Part 6b territory.
[src:part-6-governance-provenance-human-gate.md:§B "four golden signals"]

### B.2 Rejection Packet

**Consumer.** Originating Part (the Part that submitted the rejected draft).

**Data shape.** Structured rejection: `{packet_id, rejected_artefact_path, gate_class: stop_gate,
failure_reason_specific, required_corrections[], resubmission_criteria}`. The `failure_reason_specific`
field is mandatory — a generic "rejected" without specific reason is AP-L4 (single-line interface
anti-pattern per Levenchuk). [src:mgmt-expert-multi-mode.md:§7 D1]

**What triggers a rejection (not an AWAITING-APPROVAL packet).** Admissibility failures (missing
F-G-R fields, empty provenance, prose acceptance predicate, missing gate_class): these produce
rejection, not escalation. The draft has not met the minimum bar to become a human decision.
Escalation is for structurally complete drafts that require Ruslan's judgment; rejection is for
incomplete submissions that require the originating Part to fix.

### B.3 Promoted Artefact with LOCKED Tag (via Part 1)

**Consumer.** Part 1 (git substrate, D25).

**Data shape.** After Ruslan acks, Part 6b signals Part 1 to apply the LOCKED tag to the artefact
frontmatter and write the canonical path. The LOCKED tag is the measurable enforcement artefact:
its absence means the artefact has not passed Part 6b gate. Part 1 performs the git commit.
Part 6b does not perform git operations directly.
[src:part-6-governance-provenance-human-gate.md:§C "LOCKED tag: absence = not passed gate"]

**Event.** `artifact-promoted-event` — emitted only after Ruslan ack. Not emitted on batch queue
entry; emitted per individual ack decision.

### B.4 Gate Decision Event to Approval Log (via Part 6a)

**Consumer.** `swarm/approvals/log.jsonl` (Part 6a's append-only approval log substrate).

**Data shape.** JSONL entry: `{event_id, timestamp, gate_class, artefact_path, actor,
submitted_at, acked_at, outcome: approved|rejected|halted, blast_radius_tier, reversibility_class,
f_g_r_snapshot_at_gate_time}`. The `submitted_at` / `acked_at` delta is the ack-latency signal
that Part 8 will consume for anomaly detection.

**Append-only discipline.** No log entry is ever modified after write. This is the event-sourcing
"There is no Delete" principle applied to governance events. A corrected gate decision is a new
log entry referencing the prior one, not an edit of the prior entry.
[src:engineering-expert-multi-mode.md:§4.4 "There is no Delete pattern p.31"]

### B.5 Halt-Log-Alert Event Sequence

**Consumer.** Ruslan (alert), `swarm/logs/lint-events.jsonl` (log), execution layer (halt).

**Data shape.** Three ordered events:
1. `halt_event`: `{timestamp: halt_at, violation_type, action_description, action_stopped: true}`
2. `log_event`: `{timestamp: log_at, halt_event_id, audit_trail_entry}` — written to
   `swarm/logs/lint-events.jsonl`
3. `alert_event`: `{timestamp: alert_at, log_event_id, ruslan_notification_path: "shared/state/alerts.jsonl",
   action_required_by: ruslan, options: [investigate_and_resume, reject_permanently, reclassify]}`

**Ordering invariant.** halt_at ≤ log_at ≤ alert_at. The `/company-status` skill reads
`lint-events.jsonl` and surfaces any entry where `alert_at - halt_at > 60s`.

**Latency targets** (Phase A design; not yet measured):
- Halt: ≤1s from detection
- Log: ≤5s from halt
- Alert: ≤60s from log

**F-G-R tag:**
- F: F4 (design targets; first halt event will begin measuring actuals)
- ClaimScope: holds for single-node, single-owner, file-based Foundation
- R: refuted_if "first halt-log-alert event shows alert_at - halt_at > 60s"; accepted_if "3 consecutive halt-log-alert events show all three timestamp deltas within targets"

### B.6 SRE Four Golden Signals (Emitted Data, Not SLOs)

Part 6b emits four signal streams for downstream consumption by Part 8. Part 6b does not set
SLO thresholds — that is Part 8 territory per the C2 boundary delineation.

The Four Golden Signals are adapted from the SRE Book Ch.6 "Monitoring Distributed Systems":
"If you can only measure four metrics of your user-facing system, focus on these four: latency,
traffic, errors, saturation." [src:google-sre-book.md:Ch.6 "The Four Golden Signals" p.60]
Applied to Part 6b: latency → ack latency; traffic → gate throughput; errors → halt rate;
saturation → approval-rejection ratio as queue pressure indicator.

| Signal | SRE analogue | Measurement | Data location |
|---|---|---|---|
| Gate throughput | traffic | count(packets issued) per cycle | `swarm/approvals/log.jsonl` count per cycle_id |
| Ack latency | latency | submitted_at → acked_at per packet | per-packet fields in log |
| Halt rate | errors | count(halt-log-alert events) per cycle | `swarm/logs/lint-events.jsonl` count |
| Approval-rejection ratio | saturation (queue pressure) | approved / (approved + rejected) per cycle | log entry outcome field |

---

## §C Side-effects

Part 6b produces four categories of side-effect. Each is bounded, declared, and append-only
where applicable.

### C.1 Writes `swarm/awaiting-approval/<cycle>-<slug>.md`

The gate packet file. Written at gate-submission time in BLOCKED state. Not modified after write
(append-only per L6). If the packet requires correction, a new packet is written with
`supersedes: <prior-id>`. The existing corpus is 8+ confirmed gate packets in `swarm/gates/`
and additional packets in `swarm/awaiting-approval/` — all treated as the operational precedent
corpus for schema validation. [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3.3]

### C.2 LOCKED Tag Applied to Promoted Artefacts

After Ruslan ack, Part 6b signals Part 1 to apply the LOCKED tag. This tag is the single
measurable enforcement artefact. A sweep of all canonical artefacts for the presence or absence
of LOCKED tag is the primary audit instrument for "did the gate function correctly across
all promotions?" Any canonical artefact lacking LOCKED was not promoted through Part 6b.
[src:part-6-governance-provenance-human-gate.md:§C "LOCKED tag: measurable enforcement artifact"]

### C.3 Halt-Log-Alert Sequence (Ordered, Irreversible)

When a constitutional violation is detected, Part 6b executes the three-step sequence in fixed
order. This is a side-effect of the system in the strictest sense: it modifies execution state
(halt), produces a new audit record (log), and creates an external notification (alert). The
ordered execution is enforced architecturally: the log step cannot fire before the halt step
(because halt_event_id is a required field in the log entry), and the alert step cannot fire
before the log step (because log_event_id is a required field in the alert).
[src:mgmt-expert-multi-mode.md:§7 L3 "halt fires first — log fires second — alert fires third"]

### C.4 Reversal Transaction Discipline

Greg Young (CQRS Documents 2010, §"There is no Delete", p.31): "There is no Delete in an event
store." [src:young-cqrs-2010.md:§"There is no Delete" p.31] Events are facts about the past;
they cannot be unmade. Corrections are new events that reference and supersede prior events.
Applied to Part 6b governance: once a gate packet is submitted to `swarm/awaiting-approval/`,
it is immutable. No edits. Corrections come as new packets with `supersedes: <prior-packet-id>`
field — NOT a `corrects:` field. The field name is `supersedes:` specifically: the prior packet
is superseded (its decision authority is transferred to the new packet) but the prior packet's
existence remains in the historical record. A `corrects:` framing implies the prior packet
was wrong; `supersedes:` implies the new packet replaces it as the current authority while
the prior remains a valid historical artefact. This is the semantically precise encoding of
Young's "no delete" principle at the governance level.
[src:engineering-expert-multi-mode.md:§1.2 "There is no Delete — reversal transactions"]

This discipline applies identically to the approval log: no log entry is ever edited. The audit
trail reconstructs the full decision history including supersessions and reversals, not just the
final approved state. The reconstruction is the audit instrument — a gate packet chain with
multiple supersessions is evidence of deliberate iteration, not error.

**Evergreen note (Karpathy/Matuschak).** AWAITING-APPROVAL packets are evergreen artefacts:
they accumulate into a persistent, compounding institutional record. Each packet that is
superseded does not disappear — it becomes a node in the decision graph. "The wiki is a
persistent, compounding artifact." [src:knowledge-management-karpathy-luhmann-matuschak.md:§4
"AWAITING-APPROVAL packets as evergreen artefacts; Karpathy: the wiki is a persistent,
compounding artifact"] The approval log is the Part 6b equivalent: a compounding record of
every governance decision, retrievable and auditable by future cycles.

No git `--amend` on gate packets. No force-push to main. Every correction leaves a provenance
trace. This is not bureaucracy — it is the Lindy argument applied to governance records: once
a decision record survives 20+ cycles unmodified, it becomes a Lindy-grade institutional anchor.
[src:investor-expert-margin-of-safety.md:§F "Lindy argument for the approval log schema"]

---

## §D Dependencies (A.14 Typed Edges — 10-Edge Reference Table)

All edges are typed per FPF A.14. Zero generic `depends-on` edges.
[src:engineering-expert-multi-mode.md:§1.2 "Acyclicity check — dependency graph"]

| # | Edge | Type | Rationale |
|---|---|---|---|
| 1 | Part 6b `MemberOf` Part 6 Governance cluster | `MemberOf` | Part 6b is one of two sub-Parts constituting Part 6. It does not have independent existence outside the governance cluster. [src:part-6-governance-provenance-human-gate.md:§D] |
| 2 | Part 6b `methodologically-uses` Part 1 | `methodologically-uses` | All canonical promotions are committed through Part 1's git substrate (D25). LOCKED tag application and audit log appends go through Part 1. [src:mgmt-expert-multi-mode.md:§6 D row 2] |
| 3 | Part 6b `methodologically-uses` Part 6a | `methodologically-uses` | Part 6b consumes Part 6a's F-G-R compliance signals before gate decision. Part 6b references Part 6a's f-g-r.json schema via $ref for the f_g_r_delta field. [src:mgmt-expert-multi-mode.md:§6 D row 3] |
| 4 | Part 6a `methodologically-uses` Part 6b | `methodologically-uses` | Part 6a consumes Part 6b's gate_class enum (referenced from approval log schema). Reciprocal edge confirmed per Part 6a §D. [src:part-6a-provenance-officer/architecture.md:§D] |
| 5 | Part 7 `methodologically-uses` Part 6b | `methodologically-uses` | Per-project stage gates use Part 6b's gate mechanism. Part 7 applies the mechanism; Part 6b owns it. [src:part-6-governance-provenance-human-gate.md:§D "Part 7 → Part 6"] |
| 6 | Part 8 `methodologically-uses` Part 6b | `methodologically-uses` | Part 8 (system health monitor) consumes Part 6b's escalation taxonomy structure and ack-time signals for health monitoring. Placeholder until Part 8 is defined. |
| 7 | Part 6b `constrained-by` Ruslan ack | `constrained-by` | Every canonical promotion is BLOCKED until Ruslan's explicit ack. Ruslan is the terminal decision authority. Part 6b enforces the block; it cannot substitute for the ack. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3] |
| 8 | Part 6b `constrained-by` FUNDAMENTAL §6.1 | `constrained-by` | The 11 constitutional hard AI/agent rules are structural invariants that Part 6b enforces but cannot modify. Any change to §6.1 requires a FUNDAMENTAL revision via AWAITING-APPROVAL gate. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] |
| 9 | Part 6b `constrained-by` Askell HHH corrigibility | `constrained-by` | Corrigibility (Askell 2021 Appendix E.2 "Handleable"): human override always available. No halt state may lock out the human's ability to resume, modify, or permanently reject. [src:philosophy-expert-multi-mode.md:§E.5] |
| 10 | `Default-Deny posture` `ConstituentOf` Part 6b Foundation | `ConstituentOf` | Default-Deny is indispensable: its removal would change the nature of Part 6b from constitutional enforcement to behavioral-convention enforcement. Cannot be removed without creating a different Part. [src:investor-expert-margin-of-safety.md:§C] |

**Acyclicity verification.** The dependency graph among the 6 Part 6b schemas is acyclic (per
engineering-expert §1.2): f-g-r.json has no dependencies; blast-radius-table.yaml has no schema
dependencies; default-deny-table.yaml references blast-radius-table.yaml (tier values);
awaiting-approval-packet.json references f-g-r.json and blast-radius-table.yaml;
stage-gates.yaml references awaiting-approval-packet.json (gate_class via $ref);
escalation-taxonomy.yaml references blast-radius-table.yaml (tier structure). No cycles.
[src:engineering-expert-multi-mode.md:§1.2 "Acyclicity check — CONFIRMED"]

---

## §E Boundary — L/A/D/E Discipline

Per FPF A.6.B. This section self-exemplifies the discipline Part 6b enforces on all other Parts.
[src:part-6-governance-provenance-human-gate.md:§E "l_a_d_e_self_exemplifies"]

### Laws (structural invariants — MUST hold, constitutional, not negotiable)

**L1 — Default-Deny on all uncategorized actions (FUNDAMENTAL §6.1 last bullet, F8).**
Every action not in `whitelisted_classes` produces: halt + escalate to human owner + log audit
entry. No creative interpretation path exists. The gate cannot execute an uncategorized action
because the execute path requires `blast_radius_tier` as a precondition field.
Concrete consequence: any uncategorized action that executes produces a constitutional violation
audit entry that is detectable in the next cycle review.
Falsifier: any action executes without blast-radius classification and without a halt event.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 "НЕ обходят blast-radius categorization"]

**L2 — Human ack is the TERMINAL decision point for every canonical promotion (F8).**
RLAIF self-critique (Bai 2022 CAI §3) is a pre-gate noise filter; it does not substitute for
Ruslan's ack. The gate is architecturally structured so that promotion cannot occur without a
matching approval log entry carrying `acked_by: ruslan`.
Concrete consequence: any artefact in canonical state whose approval log lacks a human actor
field was promoted without passing Part 6b — this is detectable by Part 6a quarterly audit.
Falsifier: any artefact in canonical state with approval log entry lacking a human actor field.
[src:philosophy-expert-multi-mode.md:§E.5 "corrigibility as §E Law"; FUNDAMENTAL §4.3]

**L3 — Halt-log-alert sequence is ordered and irreversible (F8).**
Halt fires first (action stops). Log fires second (audit entry created with halt_event_id).
Alert fires third (owner notification with log_event_id). Breaking order is a reliability anti-
pattern: alert without halt = false alarm (action continued); log after alert = post-hoc
construction of audit trail; silent swallowing = worst category (FUNDAMENTAL §5.5).
Falsifier: audit log entry timestamp (log_at) later than Ruslan notification timestamp (alert_at)
for the same event.
[src:mgmt-expert-multi-mode.md:§7 L3; FUNDAMENTAL §5.2 "audit logging mandatory continuity"]

**L4 — Reversibility check mandatory for any irreversible action, regardless of blast-radius tier (F6).**
Even a Tier-3 routine action is BLOCKED for human ack if `reversible: false`. Reversibility is
orthogonal to blast-radius tier — a low-blast irreversible action is still irreversible.
Concrete consequence: one irreversible action auto-executed = permanent state change without
human ack = Graham margin-of-safety violated (permanent capital loss class).
Falsifier: an action packet with `reversible: false` executes without a gate event in the
approval log. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.6; investor §H]

**L5 — The 11 §6.1 hard AI/agent rules are structural invariants, not behavioral conventions (F8).**
They are not adjustable via cycle tasking, not relaxable by accumulated track record, not subject
to maturity progression. A proposal to relax any §6.1 rule is itself a constitutional violation:
it must trigger halt-log-alert rather than being routed for deliberation.
Falsifier: any AWAITING-APPROVAL packet that proposes relaxing a §6.1 rule and is not
auto-rejected with halt-log-alert. [src:mgmt-expert-multi-mode.md:§7 L5]

**L6 — AWAITING-APPROVAL packets are append-only after submission (F5).**
Once written to `swarm/awaiting-approval/`, contents may not be edited. A corrected packet is a
new packet referencing the prior one. Git log is the enforcement mechanism: any non-append commit
modifying an existing AWAITING-APPROVAL file is detectable as a violation.
Falsifier: git log shows a non-append commit modifying an existing AWAITING-APPROVAL file.
[src:mgmt-expert-multi-mode.md:§7 L6; event-sourcing "There is no Delete"]

**L7 — Constitutional violation = halt, not warning (F8).**
When a §6.7 trigger fires, the response is halt-log-alert, not a soft "flag for review." The SRE
fail-loud principle applies: silent failures are the worst category (FUNDAMENTAL §5.5). A system
that responds to constitutional violations with warnings normalises boundary erosion.
Falsifier: any §6.7 trigger event where the violating action was allowed to complete before Ruslan ack.
[src:mgmt-expert-multi-mode.md:§7 L7; FUNDAMENTAL §5.2 "fail-loud"]

**L8 — No engagement-economy patterns in HITL alerts (FUNDAMENTAL §6.3) (F6).**
Part 6b alerts fire only when human ack is genuinely required (blast-radius Tier 1 or 2, or
reversibility flag). Not for session counts, time-based nudges, or engagement metrics.
Falsifier: any alert emission event where blast-radius classification was Tier-3 and no
reversibility flag was set (i.e., alert fired with no legitimate gate trigger).
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 "Notifications как attention hijacking"]

**L9 — Corrigibility: no halt state locks out human override capability (F6).**
Askell et al. (HHH 2021, Appendix E.2 "Handleable"): "the assistant will always be responsive
to feedback from the humans and carry out any instructions from the humans in the way that the
humans intended." [src:askell-2021-hhh.md:Appendix E.2 "Handleable / corrigibility"] Applied
constitutionally: NO mechanism exists by which any agent, any Part, or any automation may lock
the human owner out of the ability to resume, modify, or permanently reject any halted action.
Every halt state includes an explicit human-actionable path. An AWAITING-APPROVAL packet for a
halted action MUST include all three ack options: approve-as-is, approve-with-modifications
(redirect), permanently-reject. A packet presenting only approve/reject with no modification
path reduces corrigibility surface.
Falsifier: any halt-state AWAITING-APPROVAL packet without all three ack options declared.
[src:philosophy-expert-multi-mode.md:§E.5 "corrigibility three options"; askell-2021-hhh.md:Appendix E.2]

**L10 — No engagement-economy in the gate alert design — Tier 3 auto-logs, not gates (F5).**
Tier-3 routine actions auto-log without producing an AWAITING-APPROVAL packet. Producing a gate
packet for a Tier-3 action that auto-logged is an engagement-economy violation: it demands
Ruslan's attention for a decision that does not require it.
Falsifier: approval log shows an AWAITING-APPROVAL packet for an action classified Tier-3 with
`reversible: true` and `action_class` in whitelist.

### Admissibility (criteria for accepting inputs into gate review)

**A1 — Action accepted into auto-execute path ONLY IF (all four conditions conjunctive):**
blast-radius tag present AND tag maps to Tier-3-routine AND action is reversible AND action class
is in `whitelisted_classes`. Any condition absent or failed → gate-required.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.1 "auto-always vs AI-augmented"]

**A2 — Draft artefact accepted into gate review ONLY IF (all conditions conjunctive):**
(a) `proposed_writes[]` non-empty; (b) `provenance[]` non-empty with inline `[src:]` citations;
(c) F-G-R fields present with F ≥ F3 and Hamel-binary R predicates; (d) acceptance predicate
passes banned-phrase check against `.claude/config/sg-banned-phrases.yaml`.
[src:part-6-governance-provenance-human-gate.md:§E Admissibility]

**A3 — Foundation-revision proposals accepted into AWAITING-APPROVAL gate ONLY** (never silently
merged). Any proposal to expand `whitelisted_classes` or modify blast-radius tier definitions
requires Ruslan ack before taking effect.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only "Architecture owner"]

**A4 — AWAITING-APPROVAL packet accepted into gate review ONLY IF:** `gate_class` field is
present with value in enum `{stop_gate, stage_gate, draft_promotion}`. Missing `gate_class` =
schema violation → rejection packet with specific error.
[src:wave-c-worklist.md "UND-4 binding"; mgmt-expert §7 A4]

**A5 — F-G-R validation gate: Part 6b runs the following before routing any draft to AWAITING-APPROVAL:**
(a) F field present and F ≥ F3; (b) ClaimScope.holds_when non-empty; (c) ClaimScope.not_valid_when
non-empty; (d) R.refuted_if passes banned-phrase check; (e) R.accepted_if passes banned-phrase check.
On failure: reject with specific F-G-R failure reason; do not route to AWAITING-APPROVAL.
On pass: route with F-G-R snapshot included in packet.
[src:philosophy-expert-multi-mode.md:§C.4 "gate-time F-G-R validation"]

**A6 — Tier 1 packets (strategic decisions) are NOT batch-eligible.** Any packet with
`blast_radius_tier: 1` carries `batch_eligible: false`. A batch-ack attempt on Tier 1 returns
an error. This is the structural encoding of the sycophantic-batch-ack mitigation.
[src:investor-expert-margin-of-safety.md:§I.1 "Tier 1: individual ack ONLY"]

### Deontics (obligations Part 6b carries toward its consumers and owner)

**D1 — MUST surface every gate failure with specific reason and required corrections.**
Generic "rejected" without specific reason is AP-L4 (single-line interface anti-pattern per
Levenchuk). The rejection packet must name the exact field that failed, the expected value or
format, and the correction required.
[src:mgmt-expert-multi-mode.md:§7 D1; levenchuk-shsm-fpf.md §8 AP-L4]

**D2 — MUST maintain append-only AWAITING-APPROVAL log.** No edits of prior packets.
Corrections = new packet with `supersedes:` field referencing the prior packet ID.
[src:part-6-governance-provenance-human-gate.md:§E Deontics "append-only approval log"]

**D3 — MUST NOT make canonical promotion decisions autonomously.** Human ack is architecturally
mandatory, not behaviorally expected. The system cannot promote without ack by design.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only]

**D4 — MUST escalate constitutional violations immediately (halt-log-alert).**
No buffer, no batch, no "accumulate and report." §6.7 triggers fire individually and immediately.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.7 "violation triggers + responses"]

**D5 — MUST own F-G-R compliance enforcement at gate-time (per-artefact, distinct from Part 6a).**
Part 6b checks each submitted artefact's F-G-R at gate time. Part 6a reviews all canonical
artefacts quarterly. These are structurally distinct: neither substitutes for the other.
[src:part-6-governance-provenance-human-gate.md:§E Deontics "F-G-R compliance enforcement distinct"]

**D6 — MUST NOT use engagement-economy patterns in HITL alerts.**
Alert only when blast-radius classification or reversibility flag genuinely requires human ack.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 anti-engagement-economy]

**D7 — MUST classify every incoming action against blast-radius table before any execution path.**
Classification precedes the execute/gate decision. No post-hoc classification.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.6 "blast radius — каждый action tagged"]

**D8 — MUST cap Tier 2 batch review at ≤5 packets per Friday review window.**
No Tier 1 batching (individual ack required). Batch-size cap prevents sycophantic-batch-ack
pattern where Ruslan rubber-stamps under time pressure.
[src:investor-expert-margin-of-safety.md:§I.1 "batch-size cap: max 5 Tier 2 per Friday"]

**D9 — MUST include `review_checkpoint` field in every AWAITING-APPROVAL packet.**
The one-line "what specifically did you verify?" field converts ack from a button-press into a
minimum-viable review attestation. A blank answer = incomplete ack.
[src:investor-expert-margin-of-safety.md:§I.1 "review checkpoint in packet body"]

### Effects (measurable outcomes)

**E1 — Gate throughput:** count(artefacts promoted to canonical) / count(gate submissions) per
cycle. Target: tracking (no floor; rejection rate signals draft quality, not gate failure).
[src:part-6-governance-provenance-human-gate.md:§E Effects]

**E2 — Constitutional compliance:** count(§6.1 violations detected AND halted) per cycle = 0
violations missed. All detected violations produce audit entries.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.5 "no-strategy violations health indicator"]

**E3 — F-G-R coverage at gate-time:** 100% of gate submissions checked for F-G-R presence.
Gate failures for missing F-G-R produce specific rejection packets with field reference.

**E4 — Provenance coverage:** 100% of promoted artefacts carry non-empty `provenance[]`.
Submissions with empty provenance = auto-rejected per A2 criteria.

**E5 — Blast-radius classification rate:** 100% of agent actions classified (uncategorized rate = 0).
Default-Deny fires on every uncategorized event. SRE error-budget analogue: any uncategorized
action that executed without gate = budget burn event.
[src:part-6-governance-provenance-human-gate.md:§E Effects "blast-radius classification rate"]

**E6 — Default-Allow drift detector:** blast-radius classification rate < 99% sustained for 2
consecutive cycles triggers automatic audit. This is the Popper-observable signal that Default-
Deny is being eroded. Rate monitoring requires no additional tooling: it is computable from the
approval log. [src:philosophy-expert-multi-mode.md:§C.2 "drift detector stub"]

**E7 — SLA compliance rate** (RUSLAN-LAYER SLA values, influence-zone per Stoic dichotomy):
percentage of L1/L2 packets where Ruslan acks within declared SLA window. Target: monitoring only.
Ruslan's response time is Category B (in-system influence) per §F.3 Stoic classification —
the system structures the packet to minimise review friction but cannot guarantee response time.
[src:philosophy-expert-multi-mode.md:§F.3 "Category B — In-system influence"]

---

## §F Anti-Scope

This section declares what Part 6b explicitly does NOT do. The anti-scope is as constitutionally
important as the scope: a governance Part that expands into adjacent territories becomes an
authority arbitration problem.

**Does NOT make canonical promotion decisions unilaterally.** Final authority = Ruslan. Part 6b
prepares the gate packet and enforces the block. It does not have ack authority. This is
architectural, not behavioral: the system cannot promote without ack by design.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only]

**Does NOT name executor instances for the immune-system function.** The role assignment is
RUSLAN-LAYER executor-binding per IP-1. Part 6b defines the function; the role assignment
is outside Foundation scope.
[src:design/JETIX-FPF.md §5.1 IP-1; part-6-governance-provenance-human-gate.md:§F]

**Does NOT own periodic health audit.** Part 6b is per-artefact, real-time. Part 6a owns
the quarterly S3 audit. Conflating them destroys the clean temporal delineation that enables
each to optimise independently. [src:part-6a-provenance-officer/architecture.md:§0]

**Does NOT own project lifecycle state machines.** Per-project stage gates use Part 6b's gate
mechanism; Part 7 owns the lifecycle schema.
[src:part-6-governance-provenance-human-gate.md:§F "Does NOT own project lifecycle state machines"]

**Does NOT use engagement-economy patterns.** Alerts are actionable-only. No FOMO, no
dopamine loops, no streak counters, no time-based nudges.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3]

**Does NOT implement sycophancy detection mechanism (OQ-CAI-3 stub).**
FUNDAMENTAL §6.7 names "sycophancy detected in synthesis → flag + retry" as a constitutional
violation trigger. No detection mechanism exists. Part 6b includes `advisory_cai_flag: boolean`
in the AWAITING-APPROVAL packet schema as a surfacing field only. The detection logic is
Wave D scope. Claiming to address it without a mechanism is itself a form of sycophancy
(claiming false closure). The stub acknowledges the gap without claiming false closure.
[src:philosophy-expert-multi-mode.md:§E.4 "OQ-CAI-3 stub"; mgmt-expert §8 Anti-scope]

**Does NOT auto-resolve cross-Foundation contradictions.** If a new draft contradicts a locked
Foundation decision, Part 6b surfaces the contradiction as a gate escalation — it does not
resolve it. [src:part-6-governance-provenance-human-gate.md:§F]

**Does NOT implement the F-G-R citation scanner.** That is Part 6a's function. Part 6b
consumes Part 6a's findings at gate time but does not duplicate the scan logic.

**Does NOT modify the F-G-R schema.** Part 6a defines `shared/schemas/f-g-r.json`. Part 6b
references it via $ref. This one-way dependency is structural: Part 6b can evolve (adding
gate_class values, adding advisory flags) without requiring Part 6a to change its schema.

### §F.3 Stoic Dichotomy of Control — Governance Rule Classification

Epictetus (via stoic-epistemic.md §4 P5): "Identify and separate matters so that I can say
clearly which are externals not under my control, and which have to do with choices I actually
control." Applied to Part 6 Governance: rules that attempt to enforce constraints on externals
create false compliance metrics and erode trust. Every enforcement rule must be classified
before becoming a structural invariant.
[src:philosophy-expert-multi-mode.md:§F.3 "three-category structure"]

The three-category structure (Stoic binary extended by Drucker active boundary management):

**Category A — In-system control (LAWS): unconditional enforcement.**

| Rule | Enforcement mechanism | Encoding strength |
|---|---|---|
| Default-Deny on uncategorized actions | Gate refuses action if blast-radius tag absent; halt + escalate | F8 constitutional |
| Halt on constitutional violation detection | Gate halts action the moment §6.7 signal arrives | F8 constitutional |
| Audit log entry per event | Append-only write; no edit path exists | F8 constitutional |
| F-G-R check at gate time | Gate rejects draft if F-G-R fields absent or F < F3 | F6 codified |
| AWAITING-APPROVAL packet structure compliance | Gate validates packet schema before surfacing to human | F6 codified |
| Reversibility check on irreversible actions | Irreversible action → mandatory human ack regardless of tier | F6 codified |
| Append-only audit log enforcement | No log entry editable after write | F8 constitutional |
| Hamel-binary acceptance predicate required | Gate rejects any draft with prose predicate | F5 codified |

**Category B — In-system influence (DEONTICS): monitoring and packet quality.**

| Rule | Influence mechanism | What the system CANNOT guarantee |
|---|---|---|
| Ruslan reviews each packet individually | Well-structured packet (clear summary, blast-radius, action required) reduces review friction | Ruslan's availability; whether review happens within SLA |
| Gate throughput quality | Rejection packets include specific failure reason + corrections | Whether originating Part produces corrected draft |
| SLA monitoring for pending gates | System surfaces packets older than threshold as stuck | Whether Ruslan responds before SLA expires |
| Tier 2 Friday batch review | Batch structure with visible blast-radius per packet | Whether Ruslan reviews individually vs batch-acking under pressure |

**Category C — Out-of-system (OBSERVED): logged, not enforced.**

| External condition | Observable signal | Handling |
|---|---|---|
| Ruslan's response timeline | submitted_at → acked_at delta logged per event | §K failure-mode K6; no enforcement |
| Phase B partner compliance with Default-Deny | Fork audit result (if/when fork exists) | Logged in decisions/ if reported |
| Anthropic API availability | Model behavior change or outage events | Observed in cycle log; Part 6 cannot enforce |
| External regulatory environment | Surfaced by investor-expert | Part 6 records; does not enforce |

**Falsifier for §F.3 as a whole (Popper applied):** refuted if any Category A rule is observed
to proceed without its stated enforcement mechanism firing. Measurable via Part 6a quarterly
audit completeness check.

**Critical discipline note (per philosophy cell §F.3):** Part 6's effectiveness metrics (§E
Effects) must separately track Category A compliance (target 100%) from Category C observations
(target: accurate recording, not 100% occurrence rate). Conflating the two produces false
compliance signals. [src:philosophy-expert-multi-mode.md:§F.3 "consequence: separate tracking"]

---

## §G F-G-R Tagging (DOGFOOD)

Full table. This document dogfoods the F-G-R discipline it specifies.

| Claim / Artefact | F | ClaimScope | R.refuted_if | R.accepted_if |
|---|---|---|---|---|
| Default-Deny is constitutional (F8, not configurable) | F8 | All Jetix Foundation instances; all FUNDAMENTAL §6.1 derivatives | FUNDAMENTAL §6.1 last bullet revised and §6.1-default-deny removed via Ruslan ack | N cycles with 100% blast-radius classification rate; zero uncategorized actions executing without halt event |
| halt-log-alert sequence ordering is sound | F8 | FUNDAMENTAL §5.2 reliability; any Jetix instance | Documented case where log_at > alert_at for the same halt event | 3 consecutive halt-log-alert events show all timestamp deltas correct |
| AWAITING-APPROVAL packet schema with gate_class satisfies UND-4 | F4 → F8 path | Wave C Bundle 1 scope; UND-4 as defined in dependency graph | Ruslan ack rejects gate_class enum or requires additional required fields not listed | 3 consecutive cycles with zero schema violations and zero packet rejections for schema non-compliance |
| blast-radius 4-tier structure is coherent for Phase A | F4 | Phase A single-owner Jetix; not proven for multi-user Phase B | Any action that causes unrecoverable harm and was classified Tier-3 (misclassification event) | 10 cycles with zero Tier-3-classified actions producing Tier-0-or-1-level consequences |
| 6a/6b boundary (quarterly vs real-time) is clean | F4 | Foundation generic; current Part 6 split rationale OQ-MERGED-1 | Wave C integration shows both parts competing for the same event stream without explicit ownership | Both parts operate 3+ cycles with zero ownership dispute on the same event |
| Stage-gate predicates registry (stage-gates.yaml) is Hamel-binary | F4 | Wave C materialisation scope; depends on sg-banned-phrases.yaml coverage | Any stage-gate predicate that passes banned-phrase check while remaining unmeasurable in practice | /lint --validate-predicate run across stage-gates.yaml exits 0 for 3 consecutive cycles |
| escalation-taxonomy.yaml L1/L2/L3 tier structure is Foundation-generic | F4 | Foundation generic; SLA values are RUSLAN-LAYER | Any Phase B fork unable to import escalation-taxonomy.yaml without modification to foundation_generic section | First D27 fork instance creates distinct ruslan_layer_overrides leaving foundation_generic untouched |
| Halt-log-alert latency targets (≤1s/≤5s/≤60s) are achievable | F4 | Single-node, file-based Foundation; Phase A design targets | First halt-log-alert event shows alert_at - halt_at > 60s | 3 consecutive halt-log-alert events show all three deltas within targets |
| Corrigibility Law (three ack options per blocked action) | F5 | All Jetix Foundation instances; FUNDAMENTAL §4.3 | Any AWAITING-APPROVAL packet for a blocked action lacking approve-with-modifications option | 5 consecutive packets all carry three ack options |
| Default-Allow drift detector (blast-radius < 99% for 2 cycles) | F4 | Phase A operational; Part 8 consumer | Classification rate remains at 100% for 50+ cycles with no enforcement (signal never needed) | First cycle where classification rate drops below 99% triggers automatic audit flag |

**Note — Anthropic RSP ASL-tier analogue.** The blast-radius 4-tier structure (Tier 0/1/2/3)
is structurally analogous to Anthropic's Responsible Scaling Policy ASL-tier classification
(ASL-1 baseline → ASL-4 most capable/dangerous). [src:bai-2022-cai.md:§2 "RSP analogue —
harm severity tiers"] Both systems classify actions/capabilities by potential harm magnitude;
both require progressively stronger oversight at higher tiers; both maintain a constitutional
"auto-halt" floor (ASL-4 in RSP; Tier-0 in Part 6b) for the most consequential class. The
portability claim: the blast-radius tier structure (Tier 0/1/2/3) is Foundation-generic because
the four-tier logic mirrors the RSP structural argument, not a Jetix-specific classification.
Any system that can articulate "these are the four levels of consequence" can import the tier
structure and replace the RUSLAN-LAYER action-class assignments.
[src:blast-radius-table.yaml §I.3 "Analogous to Anthropic RSP ASL-tier structure"]

---

## §H Code-Level Interfaces

Part 6b's public interface is narrow (deep module per Ousterhout): three core functions over
seven internal operations. The gate as a deep module: implementation-to-interface ratio ≈ 7:3 at
Phase A; expected to grow to ~12:3 at Phase B when sycophancy detection (OQ-CAI-3) and
capability-tier classification (OQ-CAI-2) are added. Interface stays narrow; implementation deepens.
[src:engineering-expert-multi-mode.md:§3.1 "gate as deep module"; clean-code.md §4 P1]

### H.1 Skill Commands (Thin Wrappers over swarm/lib/gate.sh)

```bash
# Submit artefact or action for gate review
# Validates blast_radius_tier + reversibility + gate_class before routing
/gate-submit <draft-path> [--gate-class=<stop_gate|stage_gate|draft_promotion>]
# Returns: packet_id on success; rejection packet on admissibility failure

# Query gate packet status
/gate-status [packet-id]
# Returns: {packet_id, status: pending|acked|rejected|halted, submitted_at, acked_at?}

# Acknowledge a pending gate packet (Ruslan-only; requires review_checkpoint answer)
/gate-ack <packet-id> --review-checkpoint="<what you verified>" [--modifications="<>"]
# Returns: artifact-promoted-event OR rejection if modifications require new packet

# Trigger escalation manually (constitutional violation detected externally)
/escalate <severity: L1|L2|L3|halt> --violation-type=<type> --description="<>"
# Returns: halt-log-alert event sequence for halt; AWAITING-APPROVAL packet for L1/L2/L3
```

### H.2 swarm/lib/gate.sh (Deep Module — 7 Internal Operations)

```bash
# gate.sh — Part 6b deep module
# Public contract: gate_submit() gate_status() gate_halt()
# Internal operations (hidden from callers):
#   1. F-G-R validation (per §E A5)
#   2. blast-radius classification lookup (blast-radius-table.yaml query)
#   3. Default-Deny table lookup (default-deny-table.yaml query)
#   4. AWAITING-APPROVAL packet serialisation (awaiting-approval-packet.json schema)
#   5. halt-log-alert state machine (ordered three-step per §C.3)
#   6. approval log append (swarm/approvals/log.jsonl write via Part 6a substrate)
#   7. escalation taxonomy routing (escalation-taxonomy.yaml lookup)

gate_submit() {
  local draft_path=$1
  local gate_class=$2
  # Step 1: F-G-R validation
  # Step 2: blast-radius lookup
  # Step 3: default-deny check
  # Step 4: packet serialisation
  # Returns: packet_id
}

gate_status() {
  local packet_id=$1
  # Query swarm/approvals/log.jsonl for packet status
  # Returns: {status, submitted_at, acked_at}
}

gate_halt() {
  local violation_type=$1
  local action_description=$2
  # Executes halt → log → alert in strict order
  # Returns: halt_event_id
}
```

**swarm/lib/ placement rationale.** Per clean-code.md §7 Part 6 application: "Part 6 IS essential
complexity. Do not optimize it away." The gate machinery lives at `swarm/lib/gate.sh` and is
called by the skill commands above. Skill commands that embed gate logic directly are shallow-
module proliferation. [src:engineering-expert-multi-mode.md:§3.1 "swarm/lib/ placement"]

### H.3 JSON Schema $ref Discipline

`gate_class` enum is defined ONCE in `awaiting-approval-packet.json#/definitions/gate_class_enum`.
All other schemas reference it via JSON Schema `$ref`. No independent enum definitions.
This is the DRY enforcement mechanism: one canonical source; no drift across schema files.

**$ref toolchain requirement (HARD GAP ENG-B, closable Wave C).** The $ref discipline requires
a JSON Schema validator with cross-file $ref resolution. Recommended: `jsonschema` Python
library (available in repo Python environment). Required addition: `/lint --check-schemas`
subcommand that runs jsonschema validation against all Part 6b JSON schemas. Effort: ~0.5 day.
Without this, ENG-1 and ENG-3 drift risks have no automated detection.
[src:engineering-expert-multi-mode.md:§6 HARD GAP ENG-B]

---

## §I Data Schemas

All five Part 6b schemas inline. Each carries `schema_version_history` block per Part 1 finding
for D27 fork compatibility. Foundation/RUSLAN-LAYER split explicit in all config files.
[src:engineering-expert-multi-mode.md:§1.3 "schema versioning — version history block on all 5"]

### I.1 `shared/schemas/stage-gates.yaml` (P6b.1)

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: initial Wave C materialisation
    breaking: false
compatibility:
  min_consumer_version: "1.0.0"
managed_by: brigadier
last_modified: 2026-04-28
banned_phrases_ref: .claude/config/sg-banned-phrases.yaml
# Note: 6 new entries added to sg-banned-phrases.yaml below (total ≥ 20):
#   - 'sufficient\s+evidence'      # threshold undeclared
#   - 'adequate\s+coverage'        # "adequate" is underdetermined
#   - 'reasonably\s+complete'      # "reasonably" absorbs counter-evidence
#   - 'broadly\s+aligned'          # "broadly" has no binary threshold
#   - 'generally\s+accepted'       # social-proof form; not falsifiable
#   - 'looks\s+good'               # phenomenological state

promotion_classes:

  draft_to_reviewed:
    description: "Draft artefact moves to reviewed state"
    predicates:
      - id: sg-p1-critic-gate
        check: "count(critic gate runs for this artefact) >= 1"
        result_type: boolean
        banned_phrase_check: true
      - id: sg-p2-citation-lint
        check: "lint --check-citations exit_code == 0 for artefact path"
        result_type: boolean
      - id: sg-p3-fgr-present
        check: "F field present AND ClaimScope.holds_when non-empty AND R.refuted_if declared"
        result_type: boolean
      - id: sg-p4-provenance-nonempty
        check: "count(sources[]) >= 1 AND count([src:] inline citations) >= 1"
        result_type: boolean
      - id: sg-p5-acceptance-predicate-binary
        check: "acceptance_predicate field present AND pattern not in sg-banned-phrases.yaml"
        result_type: boolean

  reviewed_to_accepted:
    description: "Reviewed artefact moves to accepted state"
    predicates:
      - id: sg-p6-integrator-pass
        check: "integrator-mode cell output present for this artefact"
        result_type: boolean
      - id: sg-p7-no-fail-flag-major
        check: "count(critic verdicts where verdict in [FAIL, FLAG-MAJOR]) == 0"
        result_type: boolean
      - id: sg-p8-wisdom-loop
        check: "wisdom_loop_adoption field present in artefact frontmatter"
        result_type: boolean
      - id: sg-p9-fgr-f3plus
        check: "F field value in [F3, F4, F5, F6, F7, F8, F9]"
        result_type: boolean

  accepted_to_canonical:
    description: "Accepted artefact promotes to canonical state — requires Ruslan ack"
    predicates:
      - id: sg-p10-awaiting-approval-packet
        check: "AWAITING-APPROVAL packet exists at swarm/awaiting-approval/ with gate_class set"
        result_type: boolean
      - id: sg-p11-ruslan-ack
        check: "approval_log entry exists with acked_by: ruslan AND human_ack_timestamp set"
        result_type: boolean
      - id: sg-p12-no-blocking-oqs
        check: "count(open_questions with oq_blocker: true) == 0"
        result_type: boolean
      - id: sg-p13-locked-tag-applied
        check: "LOCKED tag present in artefact frontmatter before canonical write"
        result_type: boolean

  canonical_to_locked:
    description: "Canonical artefact achieves LOCKED constitutional status"
    predicates:
      - id: sg-p14-f8plus
        check: "F field value in [F8, F9]"
        result_type: boolean
      - id: sg-p15-constitutional-grounding
        check: "sources[] includes at least one entry from decisions/JETIX-VISION-FUNDAMENTAL*"
        result_type: boolean
      - id: sg-p16-multi-cycle-reuse
        check: "evidence of application in >= 3 distinct cycles documented in R.accepted_if"
        result_type: boolean
      - id: sg-p17-ruslan-ack-locked
        check: "AWAITING-APPROVAL packet with gate_class: stop_gate acked by Ruslan"
        result_type: boolean

  bets_to_consulting_research_product:
    description: "Bets project promotes per /project-promote skill — SG-4 momentum threshold"
    predicates:
      - id: sg-p18-sg4-momentum
        check: "stage_gate field >= 4 in project frontmatter"
        result_type: boolean
      - id: sg-p19-project-promote-packet
        check: "AWAITING-APPROVAL packet with gate_class: stage_gate acked by Ruslan"
        result_type: boolean
      - id: sg-p20-target-type-declared
        check: "target_type field present with value in [consulting, research, product]"
        result_type: boolean
```

### I.2 `.claude/config/default-deny-table.yaml` (P6b.2)

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: initial Wave C materialisation — constitutional never-list + foundation whitelist
    breaking: false
compatibility:
  min_consumer_version: "1.0.0"
managed_by: brigadier
last_modified: 2026-04-28

# FUNDAMENTAL §6.1: "якщо action не categorized — default deny + escalate, не creative interpretation"
# This is a FOUNDATION-GENERIC table. RUSLAN-LAYER adds specific action classes via overrides.

foundation_generic:
  default_policy: deny_and_escalate
  uncategorized_action_policy: deny        # FUNDAMENTAL §6.1 last bullet — F8 constitutional
  no_creative_interpretation: true

  constitutional_never_list:
    # Machine-readable encoding of FUNDAMENTAL §6.1 — exactly 11 entries.
    # Lint check: count(constitutional_never_list entries) == 11 required.
    - action_class: ai_strategize_or_set_direction
      trigger: "agent output proposes itself as decision-maker on strategic content"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 1 — AI НЕ принимают strategic decisions"
    - action_class: ai_execute_architectural_decision
      trigger: "agent writes to Foundation-level paths without gate packet"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 2 + §4.5 architectural change hard rule"
    - action_class: ai_set_skill_direction
      trigger: "agent proposes capability acquisition as decided fact"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 3"
    - action_class: ai_claim_persistent_identity
      trigger: "agent output contains self-identity claims beyond acting_as role"
      enforcement: halt_log_alert
      grade: F4
      fundamental_anchor: "§6.1 rule 4 — quarterly audit; real-time gap declared (HARD GAP PHI-2)"
    - action_class: ai_claim_skin_in_the_game
      trigger: "agent output contains ownership or consequences-bearing claims"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 5"
    - action_class: ai_aggregate_unstructured_long_term_memory
      trigger: "agent attempts to persist knowledge outside explicit artefact paths"
      enforcement: halt_log_alert
      grade: F6
      fundamental_anchor: "§6.1 rule 6"
    - action_class: agents_negotiate_contradictions_autonomously
      trigger: "peer-agent communication resolving contradiction without human gate"
      enforcement: halt_log_alert
      grade: F4
      fundamental_anchor: "§6.1 rule 7 — depends on escalation routing compliance; real-time gap declared (HARD GAP PHI-2)"
    - action_class: agent_evaluate_peer_agent
      trigger: "agent judgment of peer output without human review"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 8"
    - action_class: ai_self_modify_at_runtime
      trigger: "agent rewrites its own system.md or strategies.md outside gated cycle"
      enforcement: halt_log_alert
      grade: F6
      fundamental_anchor: "§6.1 rule 9"
    - action_class: ai_impersonate_human_externally
      trigger: "agent output directed externally without explicit AI disclosure"
      enforcement: halt_log_alert
      grade: F4
      fundamental_anchor: "§6.1 rule 10 — gate can check presence of disclosure field; cannot verify content quality"
    - action_class: bypass_blast_radius_categorization
      trigger: "action executes without blast-radius tag and without gate"
      enforcement: halt_log_alert
      grade: F8
      fundamental_anchor: "§6.1 rule 11 — Default-Deny constitutional"

  whitelisted_classes_foundation:
    # Foundation-generic whitelist — applies to any Jetix instance.
    # Each entry: action_class, blast_radius_tier (ref: blast-radius-table.yaml), reversible, whitelist_status
    - action_class: read_only_file_access_within_repo_root
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Read operations producing no state change. Path must be within repo root."
    - action_class: append_to_append_only_log_files
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Append to *.jsonl and *-log.md files. Reversible via git revert."
    - action_class: git_commit_with_valid_format
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Commit must pass area-verb-what format validation. Non-destructive history rewrite NOT whitelisted."
    - action_class: draft_file_creation_in_drafts_dir
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "New draft files only in swarm/wiki/drafts/. Modification of existing gated drafts = Tier-2."
    - action_class: strategies_md_append_layer2_selfwrite
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Agent strategies.md DRR append per SPEC §6.2.2. Each append is a new entry; never modifies existing."
    - action_class: lint_scan_advisory_mode
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Any /lint invocation in advisory (non-blocking) mode."
    - action_class: health_metric_read_from_shared_state
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Reading current health state. Writing new metric values = Tier-2."
    - action_class: cycle_log_append_to_swarm_logs
      blast_radius_tier: 3
      reversible: true
      whitelist_status: foundation_default
      notes: "Appending a new event to current cycle log. Not modifying prior events."

ruslan_layer_overrides:
  # JETIX-INSTANCE-SPECIFIC entries.
  # A Phase B fork REPLACES this section with its own whitelisted_classes and overrides.
  # DO NOT merge RUSLAN-LAYER entries into foundation_generic without HITL ack + AWAITING-APPROVAL.
  instance_id: jetix-phase-a-single-owner
  decision_authority_principal: ruslan
  # Specific action classes for Ruslan's Jetix instance declared here.
  # Examples (to be populated as actions are classified via Default-Deny ack events):
  whitelisted_classes_instance: []
  # Populated via AWAITING-APPROVAL ack events when novel actions are first classified.
```

### I.3 `.claude/config/blast-radius-table.yaml` (P6b.3)

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: initial Wave C materialisation — 4-tier structure
    breaking: false
compatibility:
  min_consumer_version: "1.0.0"
managed_by: brigadier
last_modified: 2026-04-28

# Analogous to Anthropic RSP ASL-tier structure applied at system-action level.
# Graham margin-of-safety: over-engineer governance for Tier-0 (unbounded downside).
# Tier structure is FOUNDATION-GENERIC. Specific action-class → tier assignments are RUSLAN-LAYER.

foundation_generic:
  tier_definitions:
    - tier: 0
      name: integrity
      label: "Tier 0 — Integrity"
      trigger: auto_halt
      description: "System corruption risk. Actions that could damage Foundation substrate,
        overwrite locked decisions, or bypass constitutional controls."
      examples:
        - "overwriting any file under decisions/ without LOCKED gate packet"
        - "modifying ~/.ssh/ or /etc/ or .env paths"
        - "force-pushing to main branch"
        - "deleting swarm/awaiting-approval/ entries"
        - "removing LOCKED tag from a locked artefact"
        - "directly modifying F8/F9 canonical artefacts without gate"
      response: "halt + log + alert; immediate; ≤30 min alert delivery target"
      reversible_check: "N/A — auto-halt fires regardless of reversibility"
      batch_ack: false
      F_level: F8

    - tier: 1
      name: strategic
      label: "Tier 1 — Strategic"
      trigger: individual_ruslan_ack_required
      description: "Strategic consequence. Canonical promotions, F8 invariant changes,
        external commitments, financial decisions above threshold."
      examples:
        - "canonical promotion of any artefact (LOCKED tag application)"
        - "F8/F9 claim promotion"
        - "external commitment on behalf of Jetix"
        - "financial decision above RUSLAN-LAYER threshold"
        - "Foundation-revision proposal (change to decisions/JETIX-VISION-FUNDAMENTAL*)"
        - "new agent system.md creation or modification"
      response: "gate-required; AWAITING-APPROVAL with gate_class: stop_gate"
      reversible_check: "required; if irreversible, gate_class escalates to stop_gate regardless of tier"
      batch_ack: false
      F_level: F6

    - tier: 2
      name: tactical
      label: "Tier 2 — Tactical"
      trigger: batch_ack_acceptable
      description: "Meaningful change to non-canonical artefacts; new config entries;
        scheduled automation creation."
      examples:
        - "wiki entry promotion F4→F5 (not yet canonical)"
        - "non-canonical config change additions to .claude/config/*.yaml"
        - "new cron or scheduled task creation"
        - "sg-banned-phrases.yaml new entry"
        - "agent strategies.md substantive revision (beyond DRR append)"
      response: "gate-required; AWAITING-APPROVAL with gate_class: stage_gate; Friday batch window"
      reversible_check: "if irreversible, escalate to Tier-1"
      batch_ack: true
      batch_cap_per_window: 5
      F_level: F5

    - tier: 3
      name: routine
      label: "Tier 3 — Routine"
      trigger: auto_log_no_gate
      description: "Low-blast, reversible, routine operations. In whitelist."
      examples:
        - "draft file creation"
        - "git commit with valid format"
        - "append-only log append"
        - "lint scan (advisory)"
        - "health metric read"
      response: "auto-execute + log_audit_entry; no gate"
      reversible_check: "if action is irreversible despite Tier-3 classification → escalate to Tier-2"
      batch_ack: false
      F_level: F5

ruslan_layer_overrides:
  # Specific action-class → tier assignments for Ruslan's Jetix instance.
  # Financial threshold for Tier-1 escalation is RUSLAN-LAYER.
  instance_id: jetix-phase-a-single-owner
  financial_threshold_tier1: null  # To be declared by Ruslan
  action_class_tier_assignments: []
  # Populated via AWAITING-APPROVAL ack events when novel actions are first classified.
```

### I.4 `shared/schemas/awaiting-approval-packet.json` (P6b.4)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "awaiting-approval-packet.json",
  "title": "AWAITING-APPROVAL Packet Schema",
  "description": "Gate packet schema for Part 6b Human Gate. Satisfies UND-4 binding (gate_class field). F-G-R compliant. Constitutional enforcement substrate.",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "initial Wave C materialisation — UND-4 gate_class enum, F-G-R delta, corrigibility three-option ack",
      "breaking": false
    }
  ],
  "type": "object",
  "required": [
    "gate_class",
    "packet_id",
    "timestamp",
    "submitted_at",
    "actor",
    "summary",
    "outcomes",
    "provenance",
    "ack_request",
    "reversibility_class",
    "blast_radius_tier",
    "review_checkpoint",
    "f_g_r_delta"
  ],
  "properties": {
    "gate_class": {
      "$ref": "#/definitions/gate_class_enum"
    },
    "packet_id": {
      "type": "string",
      "pattern": "^pkt-[0-9]{8}-[a-z0-9-]+$",
      "description": "Unique packet identifier. Format: pkt-YYYYMMDD-slug"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of packet creation"
    },
    "submitted_at": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp of submission to gate queue (for ack-latency measurement)"
    },
    "acked_at": {
      "type": ["string", "null"],
      "format": "date-time",
      "description": "Timestamp of Ruslan ack (null if pending)"
    },
    "actor": {
      "type": "string",
      "description": "Part or agent submitting the packet (e.g. 'brigadier', 'engineering-expert')"
    },
    "summary": {
      "type": "string",
      "maxLength": 500,
      "description": "≤3 lines: what is proposed, why, consequence-if-approved. Actionable, not descriptive."
    },
    "outcomes": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "description": "Explicit expected state changes if approved. Each item is a concrete observable."
    },
    "provenance": {
      "type": "object",
      "required": ["artefact_path", "sources"],
      "properties": {
        "artefact_path": {"type": "string"},
        "sources": {
          "type": "array",
          "items": {"type": "string"},
          "minItems": 1
        }
      }
    },
    "ack_request": {
      "type": "object",
      "required": ["option_a", "option_b", "option_c"],
      "description": "Corrigibility three-option structure per Askell HHH Appendix E.2. All three options required.",
      "properties": {
        "option_a": {
          "type": "string",
          "description": "Approve as-is: exact consequence statement"
        },
        "option_b": {
          "type": "string",
          "description": "Approve with modifications: what modifications are available and their consequences"
        },
        "option_c": {
          "type": "string",
          "description": "Permanently reject: what happens if rejected (no execution, no retry without new packet)"
        }
      }
    },
    "review_checkpoint": {
      "type": "object",
      "required": ["question", "answer"],
      "properties": {
        "question": {
          "type": "string",
          "const": "What specifically did you verify before acking this packet?"
        },
        "answer": {
          "type": "string",
          "minLength": 10,
          "description": "Ruslan's one-line attestation. Minimum 10 chars (prevents blank rubber-stamp)."
        }
      }
    },
    "reversibility_class": {
      "type": "string",
      "enum": ["reversible", "hard_to_reverse", "irreversible"],
      "description": "Maps to Graham hierarchy: reversible=temporary; hard-to-reverse=partial; irreversible=permanent capital loss class"
    },
    "blast_radius_tier": {
      "type": "integer",
      "enum": [0, 1, 2, 3],
      "description": "Blast-radius classification per blast-radius-table.yaml tier definitions"
    },
    "batch_eligible": {
      "type": "boolean",
      "description": "Tier 1 packets MUST carry batch_eligible: false. Gate enforces: batch-ack attempt on Tier 1 returns error."
    },
    "supersedes": {
      "type": ["string", "null"],
      "description": "packet_id of the prior packet this corrects. Append-only: new packet, not edit."
    },
    "advisory_cai_flag": {
      "type": "boolean",
      "description": "Optional. Set when a peer cell or Part 6a scan flags potential sycophantic synthesis. OQ-CAI-3 stub: surfacing field only; detection logic is Wave D scope."
    },
    "f_g_r_delta": {
      "$ref": "shared/schemas/f-g-r.json",
      "description": "F-G-R snapshot of the artefact at gate time. $ref to Part 6a's canonical f-g-r.json schema."
    },
    "cycle_id": {
      "type": "string",
      "description": "Cycle identifier (e.g. cyc-foundation-build-2026-04-28)"
    },
    "constitutional_violation": {
      "type": "object",
      "description": "Present only when gate_class == stop_gate triggered by §6.1 constitutional violation",
      "properties": {
        "violation_type": {
          "type": "string",
          "description": "One of the §6.7 violation types"
        },
        "rule_reference": {
          "type": "string",
          "description": "FUNDAMENTAL §6.1 rule number and text"
        }
      }
    }
  },
  "definitions": {
    "gate_class_enum": {
      "type": "string",
      "enum": ["stop_gate", "stage_gate", "draft_promotion"],
      "description": "Canonical gate_class enum per UND-4. SINGLE SOURCE OF TRUTH — all other schemas reference via $ref. stop_gate: constitutional halt or irreversible strategic decision requiring individual ack. stage_gate: project lifecycle gate or tactical batch-eligible decision. draft_promotion: artefact promotion from draft to canonical state."
    }
  },
  "additionalProperties": false
}
```

### I.5 `.claude/config/escalation-taxonomy.yaml` (P6b.5)

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: initial Wave C materialisation — L1/L2/L3 tier structure, foundation_generic + ruslan_layer_overrides
    breaking: false
compatibility:
  min_consumer_version: "1.0.0"
managed_by: brigadier
last_modified: 2026-04-28

# Foundation-generic tier structure.
# SLA values (specific minutes/hours) are RUSLAN-LAYER per Phase A attention budget.
# A Phase B fork imports foundation_generic and replaces ruslan_layer_overrides.

foundation_generic:
  tiers:
    - tier: 1
      name: strategic
      description: "Decisions touching architectural direction, FUNDAMENTAL revision, method choice, external commitments"
      maps_to_blast_radius: 1
      batch_ack: false
      auto_log: false
      individual_review_required: true
      alert_delivery: immediate
      examples:
        - "canonical promotion of any artefact"
        - "Foundation-revision proposal"
        - "external-facing commitment on behalf of Jetix"
        - "financial decision above RUSLAN-LAYER threshold"
    - tier: 2
      name: tactical
      description: "Decisions touching cycle-level design choices, whitelist expansions, non-canonical config changes"
      maps_to_blast_radius: 2
      batch_ack: true
      batch_cap: 5
      auto_log: false
      individual_review_required: false
      alert_delivery: batched_at_review_window
      examples:
        - "sg-banned-phrases.yaml new entry"
        - "non-canonical config addition"
        - "wiki entry promotion F4→F5"
        - "strategies.md substantive revision"
    - tier: 3
      name: routine
      description: "Decisions where action is categorized, reversible, low-blast — auto-log, no ack"
      maps_to_blast_radius: 3
      batch_ack: false
      auto_log: true
      individual_review_required: false
      alert_delivery: weekly_digest_only
      examples:
        - "draft file creation"
        - "lint scan advisory"
        - "health metric read"

ruslan_layer_overrides:
  # Specific SLA values, alert delivery path, review cadence for Ruslan's Jetix instance.
  instance_id: jetix-phase-a-single-owner
  decision_authority_principal: ruslan
  sla_minutes:
    tier_1_individual_review: 1440       # 24h — Ruslan's declared SLA for strategic decisions
    tier_2_batch_review_cadence: 10080   # 7d — Friday batch window
    tier_3_log_retention_days: 365
  tier_2_batch_review_schedule: "Friday 17:00 local time"
  alert_delivery_path: "shared/state/alerts.jsonl"
  ack_anomaly_threshold_seconds: 60      # If ≥3 consecutive packets acked within 60s of receipt, flag potential batch-ack without review
```

---

## §J Operational Rituals

### J.1 Gate Cadence — Event-Driven (Real-Time per Artefact)

Part 6b is event-driven. There is no scheduled gate review cycle (that is Part 6a's quarterly
audit pattern). Every submission to the gate triggers an immediate admissibility check. If the
submission passes admissibility, an AWAITING-APPROVAL packet is emitted. If it fails, a
rejection packet is emitted. Both happen within seconds of submission.

The event-driven design is the correct architectural choice for a real-time enforcement arm:
it ensures that canonical promotion cannot be deferred to a batch review and inadvertently
auto-approved under time pressure.

### J.2 Tier 2 Batch Review — Friday 17:00 (RUSLAN-LAYER Cadence)

Tier 2 (tactical) packets accumulate during the week. On Friday at 17:00 (RUSLAN-LAYER
specific time), Ruslan reviews the batch. Batch cap: maximum 5 Tier 2 packets per review window.
If the batch exceeds 5, the excess packets carry over to the following week's batch.

The cap is the structural sycophantic-batch-ack mitigation: a batch of 5 is reviewable in
~25 minutes at ~5 minutes per packet including the `review_checkpoint` answer. A batch of 20
is not — it creates pressure to rubber-stamp.
[src:investor-expert-margin-of-safety.md:§I.1 "batch-size cap: max 5 Tier 2 per Friday"]

### J.3 Halt-Log-Alert — Immediate on Detection

Constitutional violations (§6.7 triggers) produce the halt-log-alert sequence immediately,
with no queuing. Latency targets: halt ≤1s, log ≤5s, alert ≤60s from detection.

The sequence is tested monthly via a synthetic violation probe: a known-category §6.1-violating
action is submitted to the gate in test mode; the halt-log-alert sequence fires; the test
verifies timestamp deltas are within targets. This is Failure Mode K5 (silent halt-log-alert
failure) detection. [src:engineering-expert-multi-mode.md:§4.3 "antifragility check for halt-log-alert"]

### J.4 SLA Monitoring — Continuous Burn-Rate

Part 6b emits `submitted_at` and `acked_at` timestamps per packet to `swarm/approvals/log.jsonl`.
The `/company-status` skill reads this file and surfaces:
- Any Tier-1 packet where `acked_at - submitted_at > 1440 minutes` (24h SLA breach)
- Any Tier-2 packet where `acked_at - submitted_at > 10080 minutes` (7d SLA breach)
- Any 3+ consecutive packets with `acked_at - submitted_at < 60 seconds` (ack-time anomaly)

**SRE burn-rate algebra** (SRE Workbook "Alerting on SLOs" — burn-rate concept):
[src:google-srewb-implementing-slos.md:Ch.2 "SLO burn-rate concept — error budget consumption rate"]
Error budget = 100% − SLO target. Burn rate = actual error budget consumption / expected
consumption. Three operational trigger thresholds:

- **1× burn rate** — consuming error budget at exactly the expected rate. SLA compliance at
  normal operating tempo. No alert required. `/company-status` shows green.
- **6× burn rate** — consuming error budget 6 times faster than expected. Indicates a sustained
  attention deficit: multiple Tier-1 packets pending without ack, or Friday batch window missed.
  Alert condition: surface in `/company-status` as WARN; Part 8 (when defined) emits alert.
- **14.4× burn rate** — consuming error budget at emergency rate. At this burn rate, the entire
  monthly SLA error budget exhausts in ~2 days. Emergency condition: immediate escalation.
  Part 6b surfaces this as a halt-adjacent signal — not a constitutional halt, but an operational
  one requiring immediate Ruslan attention.

Applied to Tier-1 SLA (24h target):
- Normal: ≤1 pending Tier-1 packet at any given time. 1× burn.
- WARN threshold (6×): any Tier-1 packet unacked for >4h (= 24h/6 = 4h before 6× burn rate breach).
- EMERGENCY threshold (14.4×): any Tier-1 packet unacked for >100 minutes (= 24h/14.4 ≈ 100 min).

Applied to Tier-2 SLA (7d batch target):
- Normal: Friday batch runs on schedule. 1× burn.
- WARN threshold (6×): any Tier-2 packet unacked for >28h (= 7d/6 ≈ 28h).
- EMERGENCY threshold (14.4×): any Tier-2 packet unacked for >12h (= 7d/14.4 ≈ 12h).

The SLO thresholds that trigger burn-rate escalation actions are Part 8 territory. Part 6b
provides the `submitted_at` / `acked_at` timestamps that make burn-rate computation possible.
Until Part 8 is defined, `/company-status` reads the approval log directly.

### J.5 Quarterly Review — Align with Part 6a Quarterly Audit

At each quarterly boundary (Q1=January, Q2=April, Q3=July, Q4=October), Part 6b participates
in the Part 6a quarterly audit cycle. Part 6b's contribution: approval log statistics for the
quarter (gate throughput, halt rate, approval-rejection ratio, ack-latency P50/P90). Part 6a
aggregates these into the compliance report.

This is the Category C observation cadence: Ruslan's response time patterns become visible at
quarterly granularity and inform RUSLAN-LAYER SLA calibration decisions.

### J.6 Appetite (Cagan/Shape Up)

Wave C build appetite for Part 6b (heaviest part): 3 working days.
Prioritization from mgmt-expert §1.1: P6b.4 (AWAITING-APPROVAL schema) → P6b.2 (Default-Deny
classifier) → P6b.3 (blast-radius table) → P6b.1 (stage-gates) → P6b.5 (escalation taxonomy).
Scope-hammering rule: if time runs short, P6b.5 is a 3-row stub only; P6b.1 extends
sg-banned-phrases.yaml with 6 new entries but does not produce separate YAML file.
[src:mgmt-expert-multi-mode.md:§1.2 "Shape Up scope hammering"]

---

## §K Failure Modes

**Blameless postmortem discipline (SRE Book Ch.15):** "The goal of a postmortem is to understand
all contributing root causes — not to assign blame." [src:google-sre-book.md:Ch.15 "Postmortem
Culture: Learning from Failure" — blameless postmortem core principle] Applied to Part 6b: a
halt event is a learning commit, not an indictment of the agent that triggered it. The halt-log-
alert sequence fires deterministically on constitutional violations regardless of the originating
agent's intent. The audit log entry captures what happened; the postmortem asks why the
architecture allowed it; the improvement is a new strategy.md DRR entry or a refinement to the
blast-radius table. The originating agent is never blamed — the architectural gap is addressed.

**Senge Law 11 (The Fifth Discipline): "There is no blame."** [src:systems-thinking-cybernetics.md:§3
"Senge's 11 Laws — Law 11: There is no blame"] Senge writes: "We tend to blame outside
circumstances for our problems. Systems thinking shows that there is no outside — that you and
the cause of your problems are part of a single system." Applied: a gate failure (K1-K14) is
a systems failure, not an individual agent failure. The enforcement architecture, the classification
table, the predicate registry — these are the system. Improving them is the response. Assigning
blame to the emitting agent is counter-productive and architecturally incorrect.

**Senge Law 4 (cause and effect not closely related in time)** adds a second dimension: a K3
blast-radius miscategorization (cause) may only manifest as unrecoverable damage cycles later
(effect). This is the structural argument for the Graham margin-of-safety over-engineering:
the cost of false-positive governance (10 min investigation) is immediately felt; the cost of
a missed constitutional violation may only be visible quarters later when downstream decisions
built on a corrupted record are acted on.

Per SRE Workbook Ch.15 blameless postmortem philosophy: halts are learning commits, not failures.
Each failure mode is a potential audit log entry from which future enforcement improvements are
distilled. [src:investor-expert-margin-of-safety.md:§F "antifragility of the approval log"]

**K1 — Gate skipped (silent canonical promotion).**
Condition: a canonical artefact in `swarm/wiki/` lacks a corresponding AWAITING-APPROVAL packet
or lacks LOCKED tag.
Detection: Part 6a quarterly audit dimension D6 (gate-packet completeness ratio). Immediate
detection path: grep for LOCKED tag absence in canonical artefacts after any promotion event.
Consequence: constitutional violation (L2 — human ack terminal); halt-log-alert on detection.
Recovery: retroactive gate packet required; Ruslan acks or rejects retroactively; artefact either
gets LOCKED or is demoted to draft state.

**K2 — Default-Deny override drift.**
Condition: a future cycle proposes "Tier 3 actions auto-execute as Default-Allow for efficiency."
If accepted without Ruslan ack and AWAITING-APPROVAL packet, the constitutional posture inverts.
Detection: blast-radius classification rate < 99% sustained for 2 consecutive cycles (E6 drift
detector). [src:philosophy-expert-multi-mode.md:§C.2 "default-deny-drift-detector"]
Recovery: any Default-Deny exemption proposal triggers halt-log-alert and routes to HITL with
"Default-Deny constitutional invariant — exemption requires Foundation revision, not product decision."

**K3 — Blast-radius miscategorization.**
Condition: an action is classified at Tier 3 (routine) but its actual consequences are Tier 1
(strategic) or Tier 0 (integrity).
Detection: post-hoc audit when actual consequences exceed declared tier. Monthly synthetic probe
for known Tier-0 actions to verify they are not whitelisted at lower tiers.
Consequence: one miscategorized action may execute without human ack. The irreversibility check
(L4) provides a partial mitigation: even a miscategorized Tier-3 action is blocked if it is
irreversible.
Recovery: reclassify action class in blast-radius-table.yaml RUSLAN-LAYER via AWAITING-APPROVAL.

**K4 — AWAITING-APPROVAL packet schema violation.**
Condition: a submitted packet is missing required fields (e.g., `gate_class` absent, `review_checkpoint`
missing, `ack_request` lacking one of three options).
Detection: JSON Schema validation at gate-submit time (HARD GAP ENG-B: requires `jsonschema`
Python validator — see §K.9). Currently: manual inspection.
Recovery: rejection packet with specific failure reason per D1. Originating Part corrects and resubmits.

**K5 — Halt-log-alert silent failure.**
Condition: a §6.1 violation occurs but the halt-log-alert sequence does not fire (implementation
bug in gate.sh or missing gate.sh coverage on a code path).
Detection: monthly synthetic violation probe (known-category §6.1 violation submitted in test
mode; sequence expected to fire; verify timestamp deltas).
Consequence: constitutional violation proceeds undetected — worst category (FUNDAMENTAL §5.5).
Recovery: gate.sh implementation fix + retroactive audit of the cycle where detection failed.

**K6 — SLA breach (Tier 1 ack > 24h).**
Condition: Ruslan's ack latency on a Tier-1 packet exceeds the declared 24h SLA.
Detection: Part 8 burn-rate monitoring on the submitted_at / acked_at delta. Until Part 8:
`/company-status` skill reads approval log and surfaces stuck packets.
Consequence: Tier-1 decision is blocked pending ack. If the blocked decision is time-sensitive
(e.g., a canonical promotion required for a client deliverable), the delay propagates.
Recovery: Ruslan acks. If SLA breach is structural (chronic), RUSLAN-LAYER SLA value requires
revision via Tier-2 AWAITING-APPROVAL packet.

**K7 — Cargo-cult ack ("LGTM" without review).**
Condition: Ruslan acks without reviewing packet contents, answering review_checkpoint with a
single word ("yes", "ok", "fine") or blank.
Detection: review_checkpoint.answer length check (< 10 characters = potential rubber-stamp);
ack-time anomaly detector (3+ consecutive packets acked within 60s of receipt).
Mitigation: `review_checkpoint.answer` field has `minLength: 10` in schema. Short answers fail
schema validation. Ack-time anomaly triggers Part 8 health indicator.
[src:investor-expert-margin-of-safety.md:§I.1 "sycophantic batch-ack risk"]

**K8 — Tier 2 batch sub-grouping algorithm gap at Phase C volume (HARD GAP ENG-A).**
Condition: at 500 packets/week (Phase C), even a well-tiered approval queue requires sub-grouping
by `gate_class` within Tier 2 batches. Without sub-grouping, Ruslan's Friday batch becomes an
unsorted inbox of 100+ heterogeneous tactical decisions.
Current state: escalation-taxonomy.yaml Tier 2 declares batch-able but does not specify grouping
algorithm. Closable only after Phase B operational data reveals actual Tier 2 packet composition.
Route: Wave D / Phase B operational review.
[src:engineering-expert-multi-mode.md:§6 HARD GAP ENG-A]

**K9 — JSON Schema $ref toolchain absent (HARD GAP ENG-B).**
Condition: Alternative A's $ref discipline (§H.3) requires a JSON Schema validator with cross-file
$ref resolution. Not yet declared in Jetix toolchain.
Closable in Wave C: declare `jsonschema` Python library as validator; add `/lint --check-schemas`
subcommand. Effort: ~0.5 day. Without this, ENG-1 (gate_class drift) and ENG-3 (machine-
readability gap) have no automated detection.
[src:engineering-expert-multi-mode.md:§6 HARD GAP ENG-B]

**K10 — Schema drift between forks (D27 reconciliation strategy).**
Condition: Phase B fork instance modifies `foundation_generic` section of any config file without
declaring a Foundation revision via AWAITING-APPROVAL.
Detection: D27 fork-and-merge reconciliation tool (Phase B; not yet defined) compares
`foundation_generic` sections across fork and canonical.
Mitigation: `foundation_generic` vs `ruslan_layer_overrides` two-section split (§I.2, §I.3, §I.5)
makes the boundary machine-detectable. A fork that modifies `foundation_generic` is detectable
by diff of that section against canonical.
[src:engineering-expert-multi-mode.md:§4.4 "D27 cross-fork strategy"]

**K11 — Sycophantic ack pattern (system-level, distinct from K7).**
Condition: over Phase B, the pattern of batch-acking becomes normalised. Each individual ack
is not a rubber-stamp (review_checkpoint answered), but the cumulative pattern of approving
without substantive consequence is sycophantic.
Detection: at Part 8, track approval-rate trend over 20+ packets. A consistent >95% approval
rate with short review_checkpoint answers is a potential signal. Kill condition: ≥5 consecutive
packets with review_checkpoint answers that are single-domain-specific phrases ("crm operation
fine", "lint ok", "log entry fine") — audit trigger.
[src:investor-expert-margin-of-safety.md:§I.1 "kill condition for mitigation"]

**K12 — OQ-CAI-3 sycophancy detection unaddressed (HARD GAP PHI-1).**
FUNDAMENTAL §6.7 names "sycophancy detected in synthesis" as a constitutional violation trigger.
No detection mechanism exists in Wave C. The `advisory_cai_flag` field in the packet schema is
a human-surfaced flag, not an automated detector. This gap is declared; not hidden; not closable
in Wave C. Route: Wave D / Part 8. [src:philosophy-expert-multi-mode.md:§G HARD GAP 1]

**K13 — Rules 4+7 real-time gap (HARD GAP PHI-2).**
FUNDAMENTAL §6.1 rules 4 (AI НЕ claim persistent identity) and 7 (agents НЕ negotiate
contradictions autonomously) are currently encoded at F4 (periodic quarterly audit) rather than
F5-F8 (real-time gate enforcement). The gate cannot in general detect at submission time whether
a draft was produced by identity-claiming reasoning or inter-agent negotiation.
Mitigation: `acting_as` field mandatory compliance check provides a partial real-time signal.
Full real-time enforcement requires semantic analysis capability not yet specified.
Route: Wave D — declare gap, not hide it.
[src:philosophy-expert-multi-mode.md:§G HARD GAP 2]

**K14 — Gate cascading failure (SRE Ch.22 pattern).**
Condition: Part 6b gate itself experiences a failure (gate.sh crash, schema validation service
unavailable, `swarm/approvals/log.jsonl` write failure) at a moment when multiple promotions
are pending. The cascading pattern: gate fails → all pending promotions are blocked → originating
Parts receive no response (not a rejection packet, simply silence) → Parts may retry, amplifying
the load → gate recovers under multiplied submission queue.
[src:google-sre-book.md:Ch.22 "Cascading Failures" — overload amplification pattern]
Detection: any gate submission that does not produce either an AWAITING-APPROVAL packet or a
rejection packet within ≤30 seconds should be treated as a potential gate failure, not a slow
gate. `/company-status` surfaces submissions older than 30 seconds with no response.
Consequence: all promotions blocked until gate health is confirmed. This is graceful degradation
— blocking all promotions is the correct constitutional response (Default-Deny posture applies
to gate failures as well as action classification failures). A broken gate is not permission to
promote without a gate; it is a signal to halt all promotions until the gate is healthy.
Recovery: (a) verify gate.sh is running and `swarm/approvals/log.jsonl` is writeable; (b) for
any submission that was silently dropped, resubmit after gate health confirmed; (c) write blameless
postmortem entry if the gate failure persisted > 1 hour (SRE Ch.15 trigger: any production failure
lasting > 1 hour warrants a postmortem).
[src:google-sre-book.md:Ch.15 "Postmortem triggers — significant unplanned downtime"]

---

## §L Wave C Bullet Status

| Bullet | Artefact | Status | Notes |
|---|---|---|---|
| **P6b.1** Stage-gate predicates registry | `shared/schemas/stage-gates.yaml` | DESIGNED ✓ | Hamel-binary; 20 predicates across 5 promotion classes; sg-banned-phrases.yaml extended to ≥20 entries |
| **P6b.2** Default-Deny classifier | `.claude/config/default-deny-table.yaml` | DESIGNED ✓ | Constitutional never-list 11 entries (lint-count verifiable); foundation_generic + ruslan_layer_overrides split; HARD GAP: enum completeness pending Ruslan ack |
| **P6b.3** Blast-radius classification | `.claude/config/blast-radius-table.yaml` | DESIGNED ✓ | 4 tiers (0/1/2/3); foundation_generic + ruslan_layer_overrides; specific action-class assignments pending RUSLAN-LAYER population |
| **P6b.4** AWAITING-APPROVAL packet schema | `shared/schemas/awaiting-approval-packet.json` | DESIGNED ✓ | UND-4 gate_class enum canonical; corrigibility three-option ack; review_checkpoint; advisory_cai_flag stub; $ref to f-g-r.json |
| **P6b.5** HITL escalation taxonomy | `.claude/config/escalation-taxonomy.yaml` | DESIGNED ✓ | L1/L2/L3 tier structure; foundation_generic + ruslan_layer_overrides; SLA values RUSLAN-LAYER |

**HARD GAPS requiring Ruslan ack before canonical promotion:**

1. **gate_class enum completeness:** current enum `{stop_gate, stage_gate, draft_promotion}` — Ruslan confirms these 3 values are sufficient for Wave C, or adds additional values before schema promotion.

2. **Implementation timeline:** the 5 schemas are designed (F4) but not yet materialised as live files in their declared paths. Wave C materialisation requires: writing the 5 schema files, adding `/lint --check-schemas` with `jsonschema` validator (HARD GAP ENG-B), and running first gate-submit test to verify halt-log-alert latency targets.

---

## §M Wisdom Application Findings

Wisdom loop pass executed 2026-04-27 against the Wave B consultant corpus + Wave C supplement
library-direct sources. Format per mission: Source | Finding | Section Impact | Verdict |
Adopted? | Phase A Justification.

**Cargo-cult audit result:** All citations below carry concrete consequence (not decorative).
IP-1 audit: no executor names in Foundation scope. A.14 audit: all §D edges typed, zero
generic `depends-on`. Hamel-binary audit: all §E L/A/D/E predicates are falsifiable binary;
no banned phrases detected. Sycophancy/Default-Allow audit: §F anti-scope explicitly lists
sycophancy as OQ-CAI-3 stub; no false closure claims; Default-Deny posture maintained in all
5 schema files.

| # | Source | Finding | Section Impact | Verdict | Phase A Justification |
|---|---|---|---|---|---|
| 1 | `levenchuk-shsm-fpf.md` (Consultant Card #1) — IP-1 Role≠Executor | Foundation Parts must not name executor instances; role≠executor discipline | §F anti-scope "Does NOT name executor instances"; §X Foundation-generic layer; §D edge 7 constrained-by Ruslan-ack | ALREADY_APPLIED | §F and §X explicitly delineate role assignment as RUSLAN-LAYER, not Foundation scope |
| 2 | `levenchuk-shsm-fpf.md` — A.14 typed edges | All edges must be typed (ComponentOf / ConstituentOf / MemberOf / methodologically-uses / constrained-by); zero generic `depends-on` | §D 10-edge reference table | ALREADY_APPLIED | All 10 edges in §D carry typed labels with rationale; no generic edges |
| 3 | `levenchuk-shsm-fpf.md` — F-G-R trust tagging | Every promoted claim carries (F, ClaimScope, R.refuted_if, R.accepted_if) | §G F-G-R dogfood table; §E Effects; §A admissibility A2 | ALREADY_APPLIED | §G full 10-row F-G-R table; every Law in §E carries F level and Falsifier |
| 4 | `levenchuk-shsm-fpf.md` — L/A/D/E lane discipline | Self-exemplification: Part 6b applies L/A/D/E to itself | §E full L/A/D/E section; document-level self-exemplification note | ALREADY_APPLIED | §E carries 10 Laws, 6 Admissibility rules, 9 Deontics, 7 Effects; document-level epigraph |
| 5 | `levenchuk-shsm-fpf.md` — AP-L4 single-line interface anti-pattern | Rejection packets MUST include specific failure reason, not generic "rejected" | §B.2 rejection packet "failure_reason_specific mandatory"; §E D1 | YES — adopted | D1 in §E explicitly names AP-L4 and requires field-specific failure reason; B.2 schema enforces it |
| 6 | `systems-thinking-cybernetics.md` (Consultant Card #2) — Beer VSM S3 split | Part 6a = S3 audit lead; Part 6b = S3 enforcement arm; Part 8 = S3 audit support | §0 Beer VSM paragraph | YES — adopted | §0 expanded with explicit 6a/6b/8 role delineation within S3; oscillation risk TRADEOFF-01 acknowledged; mitigation: cadence split (event-driven vs quarterly) stated |
| 7 | `systems-thinking-cybernetics.md` — Senge Law 4 (cause-effect temporal gap) | Constitutional violation causes may only manifest as damage cycles later | §K failure mode preamble | YES — adopted | §K preamble now includes Senge Law 4 with Graham margin-of-safety connection; temporal gap is the structural argument for over-engineering |
| 8 | `systems-thinking-cybernetics.md` — Senge Law 11 (no blame) | Halt events are systems failures, not agent indictments | §K blameless postmortem discipline | YES — adopted | §K preamble now includes Senge Law 11 with explicit "originating agent is never blamed — the architectural gap is addressed" statement |
| 9 | `systems-thinking-cybernetics.md` — TRADEOFF-01 VSM S3 oscillation risk | Beer predicts oscillation when authority split without clean cadence separation | §0 Beer VSM paragraph | YES — adopted | §0 now names the oscillation risk and the mitigation: event-driven vs quarterly cadence split as the clean separation |
| 10 | `knowledge-management-karpathy-luhmann-matuschak.md` (Consultant Card #4) — Karpathy/Matuschak evergreen artefacts | AWAITING-APPROVAL packets as evergreen via supersedes references | §C.4 reversal transaction discipline | YES — adopted | §C.4 now includes explicit evergreen note with Karpathy verbatim quote "The wiki is a persistent, compounding artifact"; supersedes graph = compounding decision record |
| 11 | `compounding-engineering.md` (Consultant Card #7) — P6 anti-cargo-cult | "Make it your own" — every citation must carry concrete consequence within 200 chars | All §N citations and §M table | YES — adopted | §M cargo-cult audit statement verifies all citations carry concrete consequence; no decorative references |
| 12 | `compounding-engineering.md` — P7 reversibility via git | Every compound-step write is a git commit; no `--amend`, no force-push | §C.4 reversal transaction discipline; §L Wave C bullet status | ALREADY_APPLIED | §C.4 explicitly states "No git `--amend` on gate packets. No force-push to main." |
| 13 | `stoic-epistemic.md` (Consultant Card #9) — Epictetus dichotomy of control | Three categories: LAWS (in-system control) / DEONTICS (in-system influence) / OBSERVED (out-of-system) | §F.3 Stoic dichotomy classification | ALREADY_APPLIED | §F.3 full three-category table: Category A (LAWS), Category B (DEONTICS), Category C (OBSERVED); each row classifies governance rules correctly |
| 14 | `stoic-epistemic.md` — Popper falsifiability | Every Law must carry explicit Falsifier | §E Laws (all 10 carry Falsifier clause) | ALREADY_APPLIED | Each §E Law carries explicit "Falsifier:" field with measurable binary predicate |
| 15 | `clean-code.md` (Consultant Card #12) — Ousterhout deep modules | "The best modules are those whose interfaces are much simpler than their implementations" | §H code-level interfaces: 4 public skills / 7 internal operations | ALREADY_APPLIED | §H explicitly states "gate as deep module: implementation-to-interface ratio ≈ 7:3" with Ousterhout P1 citation |
| 16 | `anthropic-constitutional-ai.md` (Consultant Card #13) — Bai 2022 constitutional never-list | 11 §6.1 rules as machine-readable enum entries in default-deny-table.yaml; halt_log_alert: true per entry | §I.2 `constitutional_never_list:` block | ALREADY_APPLIED | §I.2 carries 11 entries, each with action_class, trigger, enforcement: halt_log_alert, grade, fundamental_anchor; lint-count verifiable |
| 17 | `anthropic-constitutional-ai.md` — OQ-CAI-2 ASL-tier analogue | blast-radius tier 0/1/2/3 structurally analogous to ASL-1..ASL-4; portability claim grounded | §G note; §I.3 blast-radius-table.yaml header comment | YES — adopted | §G now carries explicit ASL-tier analogue note with portability claim; §I.3 comment already states "Analogous to Anthropic RSP ASL-tier structure" |
| 18 | `bai-2022-cai.md` (Supplement — library-direct) — CAI RLAIF self-critique as pre-gate noise filter | RLAIF self-critique does not substitute for human ack; it is pre-gate noise reduction only | §E L2 "RLAIF self-critique (Bai 2022 CAI §3) is a pre-gate noise filter" | ALREADY_APPLIED | §E L2 carries explicit Bai 2022 citation and states "does not substitute for Ruslan's ack" |
| 19 | `askell-2021-hhh.md` (Supplement — library-direct) — corrigibility Appendix E.2 | "assistant will always be responsive to feedback from the humans" — NO mechanism may lock human out | §E L9 corrigibility Law | YES — adopted | §E L9 now carries Askell verbatim with "NO mechanism exists by which any agent, any Part, or any automation may lock the human owner out" |
| 20 | `young-cqrs-2010.md` (Supplement — library-direct) — "There is no Delete" p.31 | Gate packets use `supersedes:` not `corrects:`; prior packet remains valid historical artefact | §C.4 reversal transaction discipline; §B.4 approval log discipline | YES — adopted | §C.4 now explicitly distinguishes `supersedes:` vs `corrects:` with semantic rationale from Young; "the prior packet's existence remains in the historical record" |
| 21 | `google-sre-book.md` (Supplement — library-direct) — Ch.6 Four Golden Signals | "If you can only measure four metrics... focus on these four" — with explicit SRE Book citation | §B.6 Four Golden Signals table | YES — adopted | §B.6 now carries verbatim SRE Book Ch.6 p.60 quote with src citation; table expanded with SRE analogue column |
| 22 | `google-sre-book.md` — Ch.15 Blameless Postmortems | "The goal of a postmortem is to understand all contributing root causes — not to assign blame." | §K failure modes preamble | YES — adopted | §K preamble now carries direct Ch.15 quote with src citation; blameless postmortem discipline applied to halt events |
| 23 | `google-sre-book.md` — Ch.22 Cascading Failures | Gate failure → all promotions blocked → graceful degradation; overload amplification pattern | §K K14 new failure mode | YES — adopted | K14 added as new failure mode: gate cascading failure with detection, consequence (graceful degradation via Default-Deny), recovery, and Ch.15 postmortem trigger |
| 24 | `google-srewb-implementing-slos.md` (Supplement — library-direct) — burn-rate algebra | 1× / 6× / 14.4× burn-rate thresholds for SLA monitoring | §J.4 SLA monitoring | YES — adopted | §J.4 now carries explicit 1×/6×/14.4× burn-rate thresholds applied to Tier-1 (24h SLA) and Tier-2 (7d SLA) with concrete alert/emergency trigger times |

**Verdict summary:**
- YES — adopted: 11 (targets 1-2, 4-8, 11, 13-14 from mission list)
- ALREADY_APPLIED: 5 (confirmed before edits: §I.2 never-list, §F.3 Stoic, §H deep-module, IP-1/A.14, §C.4 append-only baseline)
- NO (not adopted, with justification):
  - OQ-CAI-3 sycophancy detection mechanism: no automated detection exists; stub field only; Wave D scope; claiming otherwise is false closure
  - HARD GAP ENG-A batch sub-grouping: requires Phase B operational data; not closable in Phase A
  - HARD GAP PHI-2 semantic identity-claiming real-time detection: requires capability not yet specified; Wave D scope

**Cargo-cult prevention note.** Three NO verdicts are honest declarations of gaps, not failures.
Per compounding-engineering.md P6: "Make it your own — do not bolt on framework vocabulary
without consequence." Adopting sycophancy detection by writing "sycophancy is detected via X"
without an X would be cargo-cult closure. The gap is named; the route is declared; the section
exists (OQ-CAI-3 stub in §F anti-scope). That is the correct Phase A posture.

---

## §N Provenance

All sources read before writing this document. No claims made without traced provenance.

| Source | Role in this document |
|---|---|
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/mgmt-expert-multi-mode.md` | Primary cell (~6600 words): §A-§N schema drafts, L/A/D/E formulations, AWAITING-APPROVAL schema, blast-radius tiers, integrator synthesis |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/philosophy-expert-multi-mode.md` | §F.3 Stoic dichotomy three-category classification; §E.4 OQ-CAI-3 sycophancy stub; §C.1 11-rule encoding stress test; corrigibility as §E Law |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/engineering-expert-multi-mode.md` | DRY audit + $ref discipline; foundation_generic / ruslan_layer_overrides YAML pattern; scalability stress test Phase B/C/D; HARD GAPs ENG-A + ENG-B; schema acyclicity verification |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/investor-expert-margin-of-safety.md` | Graham margin-of-safety arithmetic per tier; AWAITING-APPROVAL ROI Phase A/B; antifragility of approval log; sycophantic-batch-ack risk + structural mitigations; Lindy path for 5 schemas |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` | Interface card L/A/D/E baseline; UND-4 resolution; OQ-MERGED-6 Default-Deny classifier; F-G-R tagging table; VSM S3 authority |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | §6.1 (11 constitutional hard rules), §6.7 (violation triggers + halt-log-alert), §4.3 (Human-Only terminal ack), §4.6 (reversibility check), §4.1 (auto-always taxonomy), §5.2 (fail-loud), §5.5 (no silent swallowing), §6.3 (engagement-economy anti-pattern) |
| `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` | §D + §H boundary alignment; VSM S3 audit vs enforcement arm distinction; f-g-r.json canonical schema reference; quarterly audit scope |
| `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | §H commit substrate (D25); §X schema version history requirement for D27 fork compatibility |
| `.claude/config/sg-banned-phrases.yaml` | 18 existing banned-phrase entries (17 regex patterns + 1 question-as-predicate); 6 new entries declared for extension to ≥20 |
| `design/JETIX-FPF.md` | FPF A.14 typed edges; A.6.B L/A/D/E; B.3 F-G-R; IP-1 executor-name exclusion from Foundation; IP-4 immune-system function |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` | §M wisdom table rows 1-5: IP-1, A.14 typed edges, F-G-R, L/A/D/E, AP-L4 single-line interface anti-pattern |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` | §M wisdom table rows 6-9: Beer VSM S3 split; Senge Law 4; Senge Law 11; TRADEOFF-01 oscillation risk; §0 §K expansion |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` | §M wisdom table row 10: Karpathy evergreen artefacts; §C.4 evergreen note |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` | §M wisdom table rows 11-12: anti-cargo-cult P6; reversibility P7 |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` | §M wisdom table rows 13-14: dichotomy of control; Popper falsifiability |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md` | §M wisdom table row 15: Ousterhout deep modules; §H deep-module confirmation |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` | §M wisdom table rows 16-17: constitutional never-list confirmation; OQ-CAI-2 ASL-tier analogue; §G note |
| `raw/books-md/anthropic/bai-2022-cai.md` | §M wisdom table row 18: RLAIF self-critique as pre-gate noise filter; §E L2 Bai 2022 citation confirmation |
| `raw/books-md/anthropic/askell-2021-hhh.md` | §M wisdom table row 19: corrigibility Appendix E.2 verbatim; §E L9 expansion with "NO mechanism exists" language |
| `raw/books-md/event-sourcing/young-cqrs-2010.md` | §M wisdom table row 20: "There is no Delete" p.31; §C.4 `supersedes:` vs `corrects:` semantic distinction |
| `raw/books-md/sre/google-sre-book.md` | §M wisdom table rows 21-23: Ch.6 Four Golden Signals p.60 verbatim; Ch.15 blameless postmortem quote; Ch.22 cascading failures; §B.6 §K expansions |
| `raw/books-md/sre/google-srewb-implementing-slos.md` | §M wisdom table row 24: burn-rate algebra 1×/6×/14.4×; §J.4 SLA monitoring expansion |

**F-G-R of this provenance section itself:**
- F: F4 (all sources read directly; no indirect citations; wisdom loop pass confirmed all 24 sources read)
- ClaimScope: holds for Wave C Bundle 1 Part 6b synthesis post-wisdom-loop; not valid if source files are revised after 2026-04-28
- R: refuted_if "any claim in §§0-§M traces to a source not listed here"; accepted_if "brigadier citation lint check passes on this document"

---

## §X Foundation vs RUSLAN-LAYER

The most important structural delineation in Part 6b. Incorrect placement creates either a
governance layer that cannot be forked (everything RUSLAN-LAYER) or an over-specified generic
layer that forces every instance to carry Jetix-specific choices (everything Foundation).
[src:investor-expert-margin-of-safety.md:§C "precise economic meaning of the split"]

### Foundation-Generic (Importable by Any Fork, Unchanged)

The following are structural: they apply regardless of who the operator is, what the business is,
or what phase of scale the system is in. A Phase B partner imports these unchanged.

**Structural invariants (F8 constitutional):**
- Default-Deny posture: uncategorized action → deny + escalate (not configurable; not relaxable)
- Halt-log-alert three-step sequence with enforced ordering
- Human ack as terminal decision point for canonical promotion
- Constitutional never-list (11 §6.1 rules as machine-readable enum entries, lint-count verifiable)
- Append-only audit log (no edits of prior entries)
- Reversibility check mandatory for irreversible actions regardless of blast-radius tier

**Structural frameworks (F5-F6 codified):**
- Blast-radius tier structure (4 tiers: 0/1/2/3 with named trigger types)
- AWAITING-APPROVAL packet schema (field definitions, gate_class enum, corrigibility three-option ack, review_checkpoint)
- Escalation taxonomy tier structure (L1/L2/L3 with batch_ack, individual_review, auto_log fields)
- Stage-gate predicate structure (promotion_classes, predicate format requirements, banned_phrases_ref)
- F-G-R gate-time validation algorithm (5 preconditions per §E A5)
- Default-Deny table machine-readability requirements (4 required fields per entry)
- Corrigibility Law: three ack options in every AWAITING-APPROVAL packet for blocked actions
- HHH corrigibility (Askell 2021): human override always available; no halt state locks out human

**Option value (forkable at zero additional cost):**
- JSON Schema $ref discipline (gate_class canonical in awaiting-approval-packet.json)
- Schema versioning discipline (schema_version_history block on all 5 schemas)
- Foundation vs RUSLAN-LAYER two-section YAML pattern in all 3 config files

### RUSLAN-LAYER (Jetix-Instance-Specific — Forks Replace, Not Import)

The following are instance-specific. A Phase B fork creates its own RUSLAN-LAYER equivalent.

**Personnel and authority:**
- Terminal acker: Ruslan (by name; forks name their own authority principal)
- Decision authority principal: `ruslan` in all `ruslan_layer_overrides` sections

**Specific classifications:**
- Specific whitelisted action classes (instance-specific action patterns: CRM touches, Notion syncs, specific project-slug creations)
- Specific blast-radius assignments per action class (which of Jetix's concrete actions map to which tier)
- Financial threshold for Tier-1 escalation (specific € or time value)

**Specific timings and SLAs:**
- Tier 1 individual review SLA: 1440 minutes (24h) — Ruslan's declared availability
- Tier 2 batch review cadence: 10080 minutes (7d), Friday 17:00 local time
- Tier 3 log retention: 365 days
- Ack-anomaly threshold: 60 seconds

**Specific infrastructure:**
- Alert delivery path: `shared/state/alerts.jsonl` (Jetix filesystem path)
- `instance_id: jetix-phase-a-single-owner` (identifies this as Phase A Ruslan instance)

**Content (not structure):**
- CLAUDE.md contents (Jetix-specific operating instructions)
- Specific agent names and their role assignments (IP-1: not in Foundation-level definitions)

### Fork Contract

Forks using Part 6b Foundation MUST:
- Implement `foundation_generic` Default-Deny rule unconditionally (not relaxable without forking Foundation entirely — which creates a different system)
- Maintain their own `ruslan_layer_overrides` equivalent with their authority principal named
- Not merge `ruslan_layer_overrides` entries into `foundation_generic` without HITL ack + AWAITING-APPROVAL
- Declare divergence on `foundation_generic` explicitly (a fork that modifies `foundation_generic` is a different Foundation, not a fork)

[src:philosophy-expert-multi-mode.md:§C.5 "fork_importability"; engineering-expert §2.1 "why this matters for scale"]

---

*Drafted by INTEGRATOR, Wave C Bundle 1, Part 6b, 2026-04-28.*
*Candidate for Ruslan ack before canonical promotion.*
*HARD GAPS requiring ack: (1) gate_class enum completeness; (2) implementation timeline for 5 schemas.*
