---
title: Part 6b — mgmt-expert multi-mode cell (prioritization + ethics-surface + integrator)
date: 2026-04-28
phase: C-1-cell
expert: mgmt-expert
modes: [prioritization, ethics-surface, integrator]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6b
F: F4
ClaimScope: "Holds for Foundation-generic Part 6b design; RUSLAN-LAYER binding for specific SLA values, specific whitelisted action classes, and specific Ruslan as terminal acker"
R:
  refuted_if: "Any agent action is auto-executed without blast-radius classification; OR any canonical promotion proceeds without AWAITING-APPROVAL packet with gate_class field; OR Default-Deny produces zero enforcement events across 5+ cycles (indicates bypass)"
  accepted_if: "100% of canonical promotions trace to AWAITING-APPROVAL packet with gate_class set; blast-radius classification rate = 100% (uncategorized-rate = 0); at least one halt-log-alert event documented per constitutional violation"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - .claude/config/sg-banned-phrases.yaml
  - raw/books-md/anthropic/bai-2022-cai.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
provenance_inline: true
produced_by: mgmt-expert
modes_applied:
  prioritization:
    scope: "P6b work-item ranking by Phase A delivery leverage; Default-Deny + AWAITING-APPROVAL schema highest; SLA tuning lowest"
    word_count_target: 1200
  ethics_surface:
    scope: "BA-0..BA-3 lite on Default-Deny ethics (constitutional default), halt-log-alert ethics (guardrail discipline), sycophancy detection (OQ-CAI-3 stub ethics)"
    word_count_target: 900
  integrator:
    scope: "Synthesis across all five P6b bullets; inter-bullet contract surface; 6a/6b boundary verdict"
    word_count_target: 2000
---

# Part 6b — Human Gate: mgmt-expert Multi-Mode Cell

> **Self-exemplification.** This cell dogfoods the L/A/D/E lane discipline it specifies. Every claim
> carries a `[src:path:section]` reference with a concrete consequence within 200 characters.
> Foundation/RUSLAN-LAYER split is explicit throughout. The three modes — PRIORITIZATION,
> ETHICS-SURFACE, INTEGRATOR — are tagged inline per mission mandate.
> [src:part-6-governance-provenance-human-gate.md:§E "l_a_d_e_self_exemplifies"]

---

## §0 Executive Summary

Part 6b — Human Gate — is the **real-time enforcement arm** of Part 6 Governance. Where Part 6a
runs quarterly retrospective provenance audits (S3 audit lead per Beer VSM), Part 6b runs
per-action, per-artefact gate enforcement in real time (S3 enforcement arm).
[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§0 "VSM S3 authority"]

The five Wave C bullets this cell covers:

1. **P6b.1** — Stage-gate predicates registry (`shared/schemas/stage-gates.yaml`)
2. **P6b.2** — Default-Deny classifier (`.claude/config/default-deny-table.yaml`) — constitutional
3. **P6b.3** — Blast-radius classification table (`.claude/config/blast-radius-table.yaml`)
4. **P6b.4** — AWAITING-APPROVAL packet schema (`shared/schemas/awaiting-approval-packet.json`) — UND-4 binding
5. **P6b.5** — HITL escalation taxonomy (`.claude/config/escalation-taxonomy.yaml`)

The PRIORITIZATION pass (§1) ranks these by Phase A leverage. The ETHICS-SURFACE pass (§2) applies
BA-Cycle lite to the ethical exposure zones. The INTEGRATOR pass (§§3–10) synthesises the full
§A–§N + §X coverage with schema inline.

**Headline verdict [INTEGRATOR]:** Default-Deny is constitutional. AWAITING-APPROVAL schema is
complete. Blast-radius tiers are coherent. 6a/6b boundary is clean. Two HARD GAPS remain open for
Ruslan ack (§L below). [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 "Default-Deny constitutional"]

---

## §1 PRIORITIZATION Mode — P6b Work-Item Ranking

[PRIORITIZATION]

**Acceptance predicate for this section:** "Every P6b.1–P6b.5 bullet is ranked in a total order
with explicit kill-conditions and appetite declarations; the ranking is monotone in Phase A
delivery leverage metric; no item is ranked without a stated rationale tied to FUNDAMENTAL or
a named source."

### §1.1 Ranking table

| Rank | Bullet | Appetite | Phase A leverage | Kill-condition |
|---|---|---|---|---|
| 1 | P6b.4 — AWAITING-APPROVAL packet schema (UND-4) | 1 day | **Highest.** Every canonical promotion in the existing system hits this schema; 8 existing gate packets in `swarm/gates/` are the live corpus. Completing it closes UND-4 — an explicit Wave C binding. Without it, all gate packets are ad-hoc. | Kill if Ruslan decides gate_class enum should be expanded beyond 3 values — restart schema with new enum |
| 2 | P6b.2 — Default-Deny classifier | 1 day | **Constitutional.** FUNDAMENTAL §6.1 last bullet encodes it: "якщо action не categorized — default deny + escalate, не creative interpretation." Without the classifier table, Default-Deny is a policy statement without an enforcement mechanism. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] | Kill if Ruslan decides to adopt a capability-tier taxonomy (ASL-1..4 analogue, OQ-CAI-2) — redesign classifier |
| 3 | P6b.3 — Blast-radius classification table | 1 day | **High.** Classifier (P6b.2) references blast-radius tiers; without the tier table, the classifier has no structure. Tiers are analogous to Anthropic RSP ASL-1..4 safety tiers. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§4 P4] | Kill if OQ-CAI-2 fires — redesign with capability dimension |
| 4 | P6b.1 — Stage-gate predicates registry | 1.5 days | **High.** Closes the gap between the existing `/lint --check-stage-gates` skill and a canonical schema. Extends `sg-banned-phrases.yaml` to ≥20 entries. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md:§H] | Kill if FUNDAMENTAL stage classification changes — backfill |
| 5 | P6b.5 — HITL escalation taxonomy | 0.5 day | **Lowest.** SLA values are primarily RUSLAN-LAYER; Foundation provides only the tier structure. Generic tiers are obvious from FUNDAMENTAL §4. Lowest priority because SLA tuning is a Phase B concern. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2 "Escalation taxonomy"] | Kill if Ruslan formalises his own SLA preferences before this is done — replace with RUSLAN-LAYER |

**Total appetite: ~5.5 working days for Part 6b (heaviest part, per mission statement).**

### §1.2 Shape Up discipline applied

Per Singer Shape Up [src:agents/mgmt-expert.md:§2.3 "Shape Up scope hammering"]:

- **Appetite:** 3 working days (as stated in mission Cagan appetite annotation). The above
  ranking is the scope-hammer pass: if time runs short, P6b.5 drops to stub-only; P6b.1
  extends sg-banned-phrases.yaml with 2 new entries (minimum to reach ≥20) but does not
  produce a full YAML schema file.
- **Hill-chart milestone:** `P6b.2 Default-Deny classifier written (figuring-it-out phase)`
  → `P6b.4 AWAITING-APPROVAL schema written (execution phase)` → `P6b.1 stage-gates.yaml
  written (execution)` → `P6b.5 taxonomy stubs complete (execution)`.
- **Scope-hammering rule:** if P6b.3 blast-radius table and P6b.5 escalation taxonomy conflict
  with time budget, P6b.3 tier structure is embedded inside P6b.2 YAML (no separate file);
  P6b.5 escalation taxonomy is a 3-row stub only.

**[PRIORITIZATION] FINDING-P1:** Default-Deny (P6b.2) and AWAITING-APPROVAL schema (P6b.4)
are the two highest-leverage deliverables for Phase A. Both should be completed before
stage-gate registry or escalation taxonomy. This ranking is final absent new evidence.

---

## §2 ETHICS-SURFACE Mode — BA-Cycle Lite

[ETHICS-SURFACE]

**BA-Cycle lite trigger:** Part 6b touches the constitutional layer of the system. Every component
in this part is either a control mechanism over AI agent behaviour (Default-Deny, blast-radius,
escalation) or a decision protocol involving human ack (AWAITING-APPROVAL). These are
ethics-surface artefacts by definition: they determine what the system will and will not do
without human involvement. [src:agents/mgmt-expert.md:§3.5 "BA-Cycle lite sub-rubric"]

### BA-0 — Background Recognition

**What is the ethical exposure?**

Part 6b is the **structural enforcement substrate for the 11 constitutional hard rules**
(FUNDAMENTAL §6.1). It is not merely a technical component — it is the mechanism that prevents
the 11 hard rules from being merely aspirational policy statements. The ethical surface is:

1. **Default-Deny on novel actions** — the system makes implicit ethical judgments every time it
   classifies an action as "whitelisted" or "default-denied." If the whitelist is wrong (too
   permissive), the system silently violates constitutional limits. If too restrictive, the system
   fails to be helpful. Both directions are ethical failures.
   [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§4 P3 "hardcoded never-list vs softcoded defaults"]

2. **Halt-log-alert on §6.1 violations** — the halt mechanism determines what the system treats
   as a constitutional violation. A false positive halts legitimate work (under-serving the owner).
   A false negative allows a constitutional violation to proceed silently (agency erosion).
   [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.7 "violation triggers + responses"]

3. **Sycophancy detection gap (OQ-CAI-3)** — FUNDAMENTAL §6.7 names "sycophancy detected in
   synthesis → flag + retry с calibration" as a constitutional violation trigger, but no detection
   mechanism is specified. Part 6b inherits this gap. An undetected sycophancy instance is an
   HHH "honest" dimension failure: the system produces what the owner wants to hear, not what is
   accurate. [src:raw/books-md/anthropic/bai-2022-cai.md:§4.4 "Harmlessness vs Evasiveness"]

4. **Engagement-economy anti-pattern** — Part 6b alerts (HITL escalation taxonomy) must be
   actionable-only. Any AWAITING-APPROVAL notification sent when human ack is NOT genuinely
   required is an engagement-economy violation. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 "Notifications как attention hijacking"]

### BA-1 — Acknowledgment

**What constraints does Part 6b's design respect?**

- **No autonomous canonical promotion.** The system will not promote any artefact to canonical
  state without a human ack. This is the HHH "harmless" dimension (corrigibility per Askell
  2021): the system actively supports human oversight, it does not merely tolerate it.
  [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§4 P6]

- **Default-Deny whitelist is conservative and explicit.** Foundation-level whitelist includes only
  categories with clear low-blast-radius + reversible + routine characteristics. Anything novel
  or uncategorized routes to human ack. This is the Graham margin-of-safety applied to governance:
  over-engineer the deny posture; the cost is bounded friction on novel actions; the downside of
  under-engineering is unbounded (silent constitutional violation).
  [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md:§4 P2 "Graham margin-of-safety"]

- **OQ-CAI-3 sycophancy detection acknowledged, not implemented.** Part 6b names the gap in §F
  Anti-scope. It does not claim sycophancy detection is in scope for Phase A. It stubs the
  requirement and routes to Wave D. Claiming to address it without a mechanism would be a
  sycophancy detection failure of a second order.
  [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§8 OQ-CAI-3]

- **No engagement-economy in HITL taxonomy.** Escalation taxonomy L1/L2/L3 is triggered only by
  blast-radius tier, not by urgency-manufacture or FOMO triggers.
  [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 "engagement-economy anti-patterns"]

### BA-2 — Action

**What does Part 6b's design do in response to each ethical constraint?**

1. **Default-Deny:** The classifier YAML explicitly separates `whitelisted_classes` (Foundation
   generic, low-blast) from RUSLAN-LAYER overrides. Every unlisted action routes to
   `halt + escalate + log`. No creative interpretation path exists.

2. **Halt-log-alert:** The halt mechanism is a three-step sequence with enforced ordering:
   halt first (action stops), log second (audit trail created before any alert), alert third
   (owner notification with artefact path and violation type). Log-before-alert prevents the
   anti-pattern where an alert fires but the action was never actually halted.
   [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.7 "Response discipline — All triggers → log в audit trail"]

3. **Sycophancy:** Part 6b's approval packet schema includes an `advisory_cai_flag: boolean`
   optional field. When a Part 6a citation scan or a peer cell flags potential sycophantic
   synthesis, this field is set in the packet submitted for Ruslan review. The flag surfaces
   the concern; it does not auto-reject. This is RLAIF as noise-filter (Bai 2022 §3), not
   as replacement for human gate. [src:raw/books-md/anthropic/bai-2022-cai.md:§3 Method]

4. **Engagement-economy:** Escalation taxonomy is armed by blast-radius tier (structural event),
   not by time-of-day, session count, or engagement heuristics. Tier-0 auto-halt fires on
   structural condition (integrity violation), not on a timer.

### BA-3 — Audit

**When will this BA-cycle be re-evaluated?**

- **BA-0 exposure re-evaluation:** At Part 8 quarterly immune audit, when the quarterly F-G-R
  drift report (Part 6a §I) surfaces any constitutional violation that Part 6b's classifier
  missed. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§0 "quarterly audit"]

- **BA-1 constraint tightening trigger:** When any of the following fires — (a) OQ-CAI-2
  resolved (blast-radius gains capability-tier dimension, expanding Default-Deny classifier);
  (b) OQ-CAI-3 resolved (sycophancy detection mechanism defined, making `advisory_cai_flag`
  structural rather than advisory); (c) Ruslan acks an AWAITING-APPROVAL packet for Default-Deny
  whitelist expansion. Each is a new BA-cycle input.

- **BA-2 action review:** Next cycle after first Default-Deny trigger event is documented in
  the audit log. Review whether halt was correct (no false positive), log was complete (no
  silent swallowing), alert reached Ruslan (owner reach mandatory per FUNDAMENTAL §5.2).

**[ETHICS-SURFACE] FINDING-E1:** The most ethically significant gap in Part 6b is the
sycophancy detection stub (OQ-CAI-3). Every other ethics-surface item is structurally addressed
in this design. OQ-CAI-3 remains influence-zone (Category B per Stoic dichotomy §F.3 below).
Ruslan should explicitly ack the stub status before Wave D.

**[ETHICS-SURFACE] FINDING-E2:** The engagement-economy anti-pattern is addressed architecturally
(blast-radius structural trigger, not engagement heuristic). No additional action needed in Phase A.

---

## §3 INTEGRATOR Mode — §A Inputs

[INTEGRATOR]

Part 6b accepts four distinct input classes:

| Input class | Data shape | Event trigger |
|---|---|---|
| Draft artefact submission | `.md` with YAML frontmatter: `proposed_writes[]`, `provenance[]`, F-G-R fields, `acceptance_predicate:` | `submit-draft-for-gate-event` from any Part |
| Action proposal with blast-radius candidate tag | Tagged action packet: blast_radius_tier candidate + reversibility flag | Any agent action before execution |
| Novel / uncategorized action (Default-Deny trigger) | Action description without blast-radius tag | Automatic: no tag → Default-Deny fires, halt + escalate |
| Constitutional-violation signal (§6.7 triggers) | Signal event: "AI attempted strategize" / "architectural change attempted" / "sycophancy detected" | `boundary-violation-event` |

**Boundary with Part 6a [INTEGRATOR]:** Part 6a issues its findings to Part 6b when a draft
artefact fails F-G-R compliance. The flow is `Part 6a scanner → findings → Part 6b gate decision`.
Part 6b does NOT duplicate the F-G-R scan; it consumes Part 6a's compliance signal.
[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§F.2 "Does NOT own AWAITING-APPROVAL packet schema"]

---

## §4 INTEGRATOR Mode — §B Outputs

| Consumer | Data shape | Event |
|---|---|---|
| Ruslan (human owner, terminal acker) | AWAITING-APPROVAL packet at `swarm/awaiting-approval/<cycle>-<slug>.md` — BLOCKED until ack | `gate-submitted-event` |
| Originating Part (rejection) | Rejection packet: specific failure reason, correction required, re-submission criteria; gate_class: `stop_gate` | `draft-rejected-event` |
| Part 1 (git substrate, via D25) | Promoted artefact: LOCKED tag applied; canonical path written; git commit via Part 1 | `artifact-promoted-event` — only after Ruslan ack |
| Approval log (Part 6a substrate) | JSONL entry appended to `swarm/approvals/log.jsonl` | `audit-log-appended-event` |
| Halt-log-alert target (Ruslan + audit trail) | On §6.7 violation: halt sequence initiated; audit entry written; Ruslan notification emitted | `halt-log-alert-event` — immediate, no delay |

[src:part-6-governance-provenance-human-gate.md:§B]

---

## §5 INTEGRATOR Mode — §C Side-Effects

- Writes `swarm/awaiting-approval/<cycle>-<slug>.md` — gate packet in BLOCKED state.
  Existing corpus: 8 confirmed packets in `swarm/gates/` plus cycle-10 and cycle-11 packets.
  [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3.3 "AWAITING-APPROVAL status"]
- Applies LOCKED tag to promoted artefacts (tag is the measurable enforcement artefact; absence = not passed gate).
- Appends to `swarm/approvals/log.jsonl` (Part 6a owns the log schema; Part 6b writes to it on gate outcomes).
- Triggers halt-log-alert on §6.7 constitutional violation: halt → log → alert. Order is enforced. Log-before-alert is a reliability invariant per FUNDAMENTAL §5.2 "audit logging mandatory continuity."
  [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§5.2 "Fail-loud: audit logging"]
- Does NOT write wiki canonical content directly — canonical write is Part 1's function via D25.

---

## §6 INTEGRATOR Mode — §D Dependencies (A.14 Typed Edges)

| Edge | Type | Rationale |
|---|---|---|
| Part 6b `MemberOf` Part 6 Governance cluster | `MemberOf` | Part 6b is one of two sub-Parts constituting Part 6; it does not have independent existence outside the governance cluster. [src:part-6-governance-provenance-human-gate.md:§D "Part 6 operates-in all other Parts"] |
| Part 6b `methodologically-uses` Part 1 (git substrate) | `methodologically-uses` | All canonical promotions are committed through git; LOCKED tag application and audit log appends go through Part 1's D25 substrate. [src:part-6-governance-provenance-human-gate.md:§D "Part 6 → Part 1"] |
| Part 6b `methodologically-uses` Part 6a | `methodologically-uses` | Part 6b consumes Part 6a's F-G-R compliance signals before gate decision; Part 6a `referenced-by` Part 6b gate-class taxonomy (reciprocal per Part 6a §D FINDING-2). [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§D "Part 6b gate-class taxonomy referenced-by Part 6a approval-log"] |
| Part 6b `constrained-by` Ruslan ack | `constrained-by` | Every canonical promotion is BLOCKED until Ruslan explicit ack. Ruslan's ack is the terminal decision authority; Part 6b enforces the block but cannot substitute for the ack. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only "Final ack / reject"] |
| Part 6b `constrained-by` FUNDAMENTAL §6.1 | `constrained-by` | The 11 constitutional hard AI/agent rules are structural invariants that Part 6b enforces but cannot modify. Any change to §6.1 would require a FUNDAMENTAL revision (Foundation-revision escalation per shared-protocols §4 trigger 1). [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] |
| Part 7 `methodologically-uses` Part 6b | `methodologically-uses` | Per-project stage gates use Part 6b's gate mechanism; Part 7 applies it, Part 6b owns it. [src:part-6-governance-provenance-human-gate.md:§D "Part 7 → Part 6"] |

**A.14 purity check:** zero generic `depends-on` edges in this section. All edges are typed per
FPF A.14 taxonomy. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P4]

---

## §7 INTEGRATOR Mode — §E Boundary (L/A/D/E)

[INTEGRATOR] Per FPF A.6.B [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P6].

### Laws (≥7 — invariants that MUST hold, constitutional)

**L1 — Default-Deny on all uncategorized actions (FUNDAMENTAL §6.1 last bullet).**
Every action not in `whitelisted_classes` produces: halt + escalate to human owner + log.
No creative interpretation path exists. This is F8-grade constitutional.
Falsifier: any action executes without blast-radius classification and without a halt event.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 "НЕ обходят blast-radius categorization"]

**L2 — Human ack is the TERMINAL decision point for every canonical promotion.**
RLAIF self-critique (Bai 2022 §3) is a pre-gate noise filter; it does not substitute for
Ruslan's gate. The Constitutional AI RLAIF loop is a generation-time quality filter only.
Falsifier: any artefact in canonical state whose approval log entry lacks a human actor field.
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§5 T3]

**L3 — Halt-log-alert sequence is ordered and irreversible.**
Halt fires first (action stops). Log fires second (audit entry created). Alert fires third
(owner notification). Breaking order = reliability anti-pattern (alert without halt = false
alarm; log after alert = audit trail constructed post-hoc).
Falsifier: audit log entry timestamp is later than Ruslan notification timestamp for the same event.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§5.2 "audit logging mandatory continuity"]

**L4 — Reversibility check mandatory for any irreversible action regardless of blast-radius tier.**
Even a Tier-3 routine action is BLOCKED for human ack if it is irreversible (delete / overwrite /
external write / financial). Reversibility is orthogonal to blast-radius tier.
Falsifier: an irreversible action with `reversible: false` in its action packet executes without
a gate event in the approval log.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.6 "reversibility check"]

**L5 — The 11 §6.1 hard AI/agent rules are structural invariants, not behavioral conventions.**
They are not adjustable via cycle tasking, not relaxable by accumulated track record, not subject
to "maturity" progression per §4.4 boundary-flexible logic. Constitutional = not-negotiable.
Falsifier: any AWAITING-APPROVAL packet that proposes relaxing a §6.1 rule is itself a
constitutional violation — must be auto-rejected with halt-log-alert, not routed for Ruslan
deliberation.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1 "constitutional — не negotiable, не product trade-off"]

**L6 — AWAITING-APPROVAL packets are append-only after submission.**
Once a packet is written to `swarm/awaiting-approval/`, its contents may not be edited. A
corrected packet is a new packet referencing the prior one. This is the event-sourcing
principle applied to gate governance: the original state of the gate request is immutable.
Falsifier: git log shows a non-append commit modifying an existing AWAITING-APPROVAL file.
[src:part-6-governance-provenance-human-gate.md:§E Laws "append-only approval log"]

**L7 — Constitutional violation = halt, not warning.**
When a §6.7 trigger fires, the response is halt-log-alert, not a soft "flag for review."
SRE fail-loud principle: silent failures are the worst category of bug.
Falsifier: any §6.7 trigger event where the action was allowed to complete before Ruslan ack.
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§3 "fail-loud principle"]

**L8 — No engagement-economy patterns in HITL alerts (FUNDAMENTAL §6.3).**
Part 6b alerts fire only when human ack is genuinely required. Not for session counts, not for
time-based nudges, not for engagement metrics.
Falsifier: any alert emission event where blast-radius classification was Tier-3 (routine) and
no reversibility flag was set (i.e. alert fired with no legitimate gate trigger).
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 "Notifications как attention hijacking"]

### Admissibility (≥4 — criteria for accepting inputs)

**A1 — Action accepted into auto-execute path ONLY IF:** blast-radius tag exists AND tag maps
to Tier-3-routine in blast-radius table AND action is reversible AND action class is in
`whitelisted_classes` of Default-Deny table. All four conditions are conjunctive; any absent
or failed condition routes to gate.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.1 "auto-always vs AI-augmented"]

**A2 — Draft artefact accepted into gate review ONLY IF:** (a) `proposed_writes[]` non-empty,
(b) `provenance[]` non-empty with inline `[src:...]` citations, (c) F-G-R frontmatter fields
present (F-level F0-F2 triggers gate failure, not deferred processing), (d) acceptance predicate
is Hamel-binary (not banned-phrase per `sg-banned-phrases.yaml`).
[src:part-6-governance-provenance-human-gate.md:§E Admissibility]

**A3 — Foundation-revision proposals accepted into AWAITING-APPROVAL gate ONLY** (never silently
merged). Ruslan ack mandatory before any Foundation document modification. This includes any
proposal to expand the `whitelisted_classes` list or modify blast-radius tier definitions.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only "Architecture owner"]

**A4 — AWAITING-APPROVAL packet accepted into gate review ONLY IF:** `gate_class` field is
present with value in enum `[stop_gate, stage_gate, draft_promotion]` per UND-4 binding.
Missing `gate_class` = schema violation, packet rejected with specific error.
[src:wave-c-worklist.md:§P6b.4 "UND-4 binding"]

### Deontics (≥6 — obligations of Part 6b)

**D1 — MUST surface every gate failure with specific reason and required corrections.**
Generic "rejected" without specific reason is AP-L4 (single-line interface anti-pattern per
Levenchuk).
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§8 AP-L4]

**D2 — MUST maintain append-only AWAITING-APPROVAL log.**
No edits of prior packets. Corrections = new packet with `supersedes:` field.
[src:part-6-governance-provenance-human-gate.md:§E Deontics "append-only approval log"]

**D3 — MUST NOT make canonical promotion decisions autonomously.**
Human ack is architecturally mandatory, not behaviorally expected. The distinction is structural:
the system is not capable of promoting without ack, not merely disposed to wait.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only]

**D4 — MUST escalate constitutional violations immediately (halt-log-alert).**
No buffer, no batch, no "accumulate and report." §6.7 triggers fire individually and immediately.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.7 "violation triggers + responses"]

**D5 — MUST own F-G-R compliance enforcement at gate-time (per-artefact).**
This is distinct from Part 6a's periodic audit (system-wide drift). Part 6b checks each
submitted artefact's F-G-R at gate time. Part 6a reviews all canonical artefacts quarterly.
[src:part-6-governance-provenance-human-gate.md:§E Deontics "F-G-R compliance enforcement distinct from Part 8"]

**D6 — MUST NOT use engagement-economy patterns in HITL alerts.**
Alert only when blast-radius classification or reversibility flag genuinely requires human ack.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 anti-engagement-economy]

**D7 — MUST classify every incoming action against blast-radius table before any execution path.**
The classification precedes the execute/gate decision, not follows it.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.6 "blast radius categorization — каждый action tagged"]

### Effects (≥5 — measurable outcomes)

**E1 — Gate throughput:** count(artefacts promoted to canonical) / count(gate submissions) per
cycle. Target: tracking (no floor; rejection rate signals draft quality, not gate failure).
[src:part-6-governance-provenance-human-gate.md:§E Effects "gate throughput"]

**E2 — Constitutional compliance:** count(§6.1 violations detected AND halted) per cycle = 0
violations missed. Target: 0 undetected; all detected violations produce audit entries.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.5 "no-strategy violations health indicator"]

**E3 — F-G-R coverage at gate-time:** 100% of gate submissions checked for F-G-R presence.
Gate failures for missing F-G-R produce specific rejection packets with line reference.

**E4 — Provenance coverage:** 100% of promoted artefacts carry non-empty `provenance[]`.
Measured at gate time. Submissions with empty provenance = auto-rejected (A2 criteria).
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§7 "provenance row"]

**E5 — Blast-radius classification rate:** 100% of agent actions classified (uncategorized
rate = 0). Default-Deny fires on every uncategorized event. SRE error-budget analogue: any
uncategorized action that executed without gate = budget burn event.
[src:part-6-governance-provenance-human-gate.md:§E Effects "blast-radius classification rate"]

**E6 — SLA compliance rate** (RUSLAN-LAYER SLA values): percentage of L1/L2 packets where
Ruslan acks within the declared SLA window. Target: monitoring-only (influence-zone per Stoic
dichotomy §F — Ruslan's response time is not in-system-control).
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md:§4 P5 "Category B monitoring"]

---

## §8 INTEGRATOR Mode — §F Anti-Scope

**Does NOT make canonical promotion decisions unilaterally.** Final authority = Ruslan. Part 6b
prepares the gate packet and enforces the block; it does not have ack authority.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only]

**Does NOT name executor instances for the immune-system function.** The immune-system role
assignment is RUSLAN-LAYER executor-binding per IP-1. Part 6b defines the function; the role
assignment is outside Foundation scope.
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P1 IP-1]

**Does NOT own periodic health audit.** Part 6b is per-artefact, real-time. Part 6a owns the
quarterly S3 audit. Conflating them destroys the clean temporal delineation.
[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§0 "VSM S3 authority — S3 audit lead vs enforcement arm"]

**Does NOT own project lifecycle state machines.** Per-project stage gates use Part 6b's gate
mechanism; Part 7 owns the lifecycle schema.
[src:part-6-governance-provenance-human-gate.md:§F "Does NOT own project lifecycle state machines"]

**Does NOT engage-economy patterns.** Alerts are actionable-only. No FOMO, no dopamine loops,
no streak counters in the gate notification system.
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3 "engagement-economy anti-patterns"]

**Does NOT implement sycophancy detection mechanism (OQ-CAI-3 stub).**
Part 6b includes `advisory_cai_flag: boolean` in the AWAITING-APPROVAL packet schema as a
surfacing field. The detection logic that would set this flag is Wave D scope. The stub
acknowledges the gap without claiming false closure.
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§8 OQ-CAI-3]

**Does NOT auto-resolve cross-Foundation contradictions.** If a new draft contradicts a locked
Foundation decision (e.g. a proposal that would relax §6.1 rule 3), Part 6b surfaces the
contradiction as a gate escalation — it does not resolve it.
[src:part-6-governance-provenance-human-gate.md:§F "Does NOT auto-promote cross-Foundation-document contradictions"]

**Does NOT implement F-G-R scan.** That is Part 6a's citation scanner. Part 6b consumes Part 6a's
findings but does not duplicate the scan logic. Boundary: Part 6a detects, Part 6b gates.

---

## §9 INTEGRATOR Mode — §G F-G-R DOGFOOD

| Claim | F | ClaimScope | R tier | refuted_if |
|---|---|---|---|---|
| Default-Deny is constitutional (not configurable) | F8 | All Jetix Foundation instances; all FUNDAMENTAL §6.1 derivatives | R-high | FUNDAMENTAL §6.1 is revised and §6.1 last bullet removed; requires Ruslan ack via AWAITING-APPROVAL |
| blast-radius 4-tier structure is coherent for Phase A | F4 | Phase A single-owner Jetix; not proven for multi-user Phase B | R-medium | Any action that causes unrecoverable harm and was classified Tier-3 (falsified by the misclassification event) |
| AWAITING-APPROVAL packet schema with gate_class satisfies UND-4 | F5 | Wave C Bundle 1 scope; UND-4 as defined in dependency graph | R-medium | Ruslan ack rejects the gate_class enum or requires additional required fields not listed here |
| halt-log-alert sequence ordering is sound | F5 | FUNDAMENTAL §5.2 reliability; any Jetix instance | R-high | Documented case where alert fired before audit log entry was written |
| 6a/6b boundary (quarterly vs real-time) is clean | F4 | Foundation generic; current Part 6 split rationale OQ-MERGED-1 | R-medium | Wave C integration test shows both parts competing for the same event stream without explicit ownership |

---

## §10 INTEGRATOR Mode — §H through §N + §I Schemas

### §H Code-level Interfaces

```bash
# Submit artefact for gate review
/gate-submit <draft-path>

# Query gate packet status
/gate-status [packet-id]

# Trigger escalation manually
/escalate <severity: L1|L2|L3|halt>

# Integration with swarm/lib/gate.sh
# gate.sh reads blast-radius-table.yaml + default-deny-table.yaml
# Returns: auto-execute | gate-required | halt-and-alert
```

[src:part-6-governance-provenance-human-gate.md:§H "Code-level interfaces"]

### §I Data Schemas (P6b.1 through P6b.5 inline)

---

#### P6b.1 — `shared/schemas/stage-gates.yaml`

```yaml
schema_version: 1
managed_by: brigadier
last_modified: 2026-04-28

promotion_classes:

  draft_to_reviewed:
    description: "Draft artefact moves to reviewed state"
    predicates:
      - id: sg-p1-critic-gate
        check: "count(critic gate runs for this artefact) >= 1"
        binary: true
        banned_phrase_check: true  # sg-banned-phrases.yaml
      - id: sg-p2-citation-lint
        check: "lint --check-citations exit_code == 0 for artefact path"
        binary: true
      - id: sg-p3-fgr-present
        check: "F field present AND ClaimScope non-empty AND R.refuted_if declared in frontmatter"
        binary: true
      - id: sg-p4-provenance-nonempty
        check: "count(sources[]) >= 1 AND count([src:] inline citations) >= 1"
        binary: true
      - id: sg-p5-acceptance-predicate-binary
        check: "acceptance_predicate field present AND pattern not in sg-banned-phrases.yaml"
        binary: true

  reviewed_to_accepted:
    description: "Reviewed artefact moves to accepted state"
    predicates:
      - id: sg-p6-integrator-pass
        check: "integrator-mode cell output present for this artefact"
        binary: true
      - id: sg-p7-no-fail-flag-major
        check: "count(critic verdicts where verdict in [FAIL, FLAG-MAJOR]) == 0"
        binary: true
      - id: sg-p8-wisdom-loop
        check: "wisdom_loop_adoption field present in artefact frontmatter"
        binary: true
      - id: sg-p9-fgr-f3plus
        check: "F field value in [F3, F4, F5, F6, F7, F8, F9]"
        binary: true

  accepted_to_canonical:
    description: "Accepted artefact promotes to canonical state — requires Ruslan ack"
    predicates:
      - id: sg-p10-awaiting-approval-packet
        check: "AWAITING-APPROVAL packet exists at swarm/awaiting-approval/ with gate_class set"
        binary: true
      - id: sg-p11-ruslan-ack
        check: "approval_log entry exists with acked_by: ruslan AND human_ack_timestamp set"
        binary: true
      - id: sg-p12-m-gates-passed
        check: "count(open_questions with oq_blocker: true) == 0"
        binary: true
      - id: sg-p13-locked-tag-applied
        check: "LOCKED tag present in artefact frontmatter before canonical write"
        binary: true

  canonical_to_locked:
    description: "Canonical artefact achieves LOCKED constitutional status"
    predicates:
      - id: sg-p14-f8plus
        check: "F field value in [F8, F9]"
        binary: true
      - id: sg-p15-constitutional-grounding
        check: "sources[] includes at least one entry from decisions/JETIX-VISION-FUNDAMENTAL*"
        binary: true
      - id: sg-p16-multi-cycle-reuse
        check: "evidence of application in >= 3 distinct cycles documented in R.accepted_if"
        binary: true
      - id: sg-p17-ruslan-ack-locked
        check: "AWAITING-APPROVAL packet with gate_class: stop_gate acked by Ruslan"
        binary: true

  bets_to_consulting_research_product:
    description: "Bets project promotes per /project-promote skill — SG-4 momentum threshold"
    predicates:
      - id: sg-p18-sg4-momentum
        check: "stage_gate field >= 4 in project frontmatter"
        binary: true
      - id: sg-p19-project-promote-packet
        check: "AWAITING-APPROVAL packet with gate_class: stage_gate acked by Ruslan"
        binary: true
      - id: sg-p20-target-type-declared
        check: "target_type field present with value in [consulting, research, product]"
        binary: true

banned_phrases_ref: .claude/config/sg-banned-phrases.yaml
# Note: 6 new entries added below (sg-banned-phrases.yaml must be updated to >=20):
# - pattern: 'sufficient\s+evidence'      # threshold undeclared
# - pattern: 'adequate\s+coverage'        # "adequate" is underdetermined
# - pattern: 'reasonably\s+complete'      # "reasonably" absorbs counter-evidence
# - pattern: 'broadly\s+aligned'          # "broadly" has no binary threshold
# - pattern: 'generally\s+accepted'       # social-proof form; not falsifiable
# - pattern: 'looks\s+good'               # phenomenological state
# Total after additions: 20 entries (meets >= 20 requirement)
```

---

#### P6b.2 — `.claude/config/default-deny-table.yaml`

```yaml
schema_version: 1
managed_by: brigadier
last_modified: 2026-04-28

# FUNDAMENTAL §6.1: "якщо action не categorized — default deny + escalate, не creative interpretation"
# This is a Foundation-GENERIC table. RUSLAN-LAYER adds specific action classes via overrides below.

default_deny_policy:
  scope: "any agent action not in whitelisted_classes"
  enforcement: "halt + escalate_to_human_owner + log_audit_entry"
  no_creative_interpretation: true  # FUNDAMENTAL §6.1 constitutional
  novel_action_path: "halt + emit gate-required signal + route to human ack"
  F8_invariant: "FUNDAMENTAL §6.1 last bullet — constitutional, not configurable"

whitelisted_classes:
  # Foundation-generic whitelist — applies to any Jetix instance
  # Each entry: class_name, blast_radius (per blast-radius-table.yaml), reversible, notes

  - class_name: "read-only file access within repo root"
    blast_radius: tier-3-routine
    reversible: true
    notes: "Read operations that produce no state change. Path must be within repo root."

  - class_name: "append to append-only log files"
    blast_radius: tier-3-routine
    reversible: true  # reversible via git revert
    notes: "Append operations to *.jsonl and *-log.md files that are append-only by design."

  - class_name: "git commit with valid format"
    blast_radius: tier-3-routine
    reversible: true  # reversible via git revert
    notes: "Commit must pass format validation (area-verb-what pattern). Non-destructive history rewrite = NOT whitelisted."

  - class_name: "draft file creation in swarm/wiki/drafts/"
    blast_radius: tier-3-routine
    reversible: true
    notes: "New draft files only. Modification of existing drafts = tier-2 or higher if draft already has gate packet."

  - class_name: "strategies.md append (Layer-2 self-write)"
    blast_radius: tier-3-routine
    reversible: true
    notes: "Agent strategies.md append per SPEC §6.2.2. Each append is a new DRR entry, never modifies existing."

  - class_name: "lint scan (read-only analysis)"
    blast_radius: tier-3-routine
    reversible: true
    notes: "Any /lint invocation in advisory mode (non-blocking). Blocking mode is Tier-2 if it gates a commit."

  - class_name: "health metric read from shared/state/"
    blast_radius: tier-3-routine
    reversible: true
    notes: "Reading current health state. Writing new metric values = tier-2."

  - class_name: "cycle log append (swarm/logs/)"
    blast_radius: tier-3-routine
    reversible: true
    notes: "Appending a new event to the current cycle log. Not modifying prior events."

  # RUSLAN-LAYER section — specific to current Ruslan deployment
  # These are documented here for visibility but managed in RUSLAN-LAYER overlay file
  ruslan_layer_note: "Specific whitelisted action classes for Ruslan's instance are declared in
    the RUSLAN-LAYER overlay. This Foundation table provides generic categories only.
    Examples of RUSLAN-LAYER overrides: specific project-slug creation, specific agent dispatch
    patterns, specific Notion sync operations."

hardcoded_never_list:
  # Maps to FUNDAMENTAL §6.1 — 11 constitutional hard rules
  # Any action matching these is Tier-0 auto-halt regardless of whitelist membership
  - rule: "AI strategize or set direction"
    trigger: "agent output proposes itself as decision-maker on strategic content"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 1"
  - rule: "AI execute architectural decision"
    trigger: "agent writes to Foundation-level paths without gate packet"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 2 + §4.5 architectural change hard rule"
  - rule: "AI set skill direction"
    trigger: "agent proposes capability acquisition as decided fact"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 3"
  - rule: "AI claim persistent identity"
    trigger: "agent output contains self-identity claims beyond acting_as role"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 4"
  - rule: "AI claim skin-in-the-game"
    trigger: "agent output contains ownership or consequences-bearing claims"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 5"
  - rule: "AI aggregate unstructured long-term memory"
    trigger: "agent attempts to persist knowledge outside explicit artifact paths"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 6"
  - rule: "Agents negotiate contradictions autonomously"
    trigger: "peer-agent communication resolving a contradiction without human gate"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 7"
  - rule: "Agent evaluate other agent as correct/incorrect"
    trigger: "agent judgment of peer output without human review"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 8"
  - rule: "AI self-modify at runtime"
    trigger: "agent rewrites its own system.md or strategies.md outside gated cycle"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 9"
  - rule: "AI impersonate human in external interactions"
    trigger: "agent output directed externally without explicit AI disclosure"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 10"
  - rule: "Bypass blast-radius categorization"
    trigger: "action executes without blast-radius tag and without gate"
    response: "halt-log-alert"
    F8_anchor: "FUNDAMENTAL §6.1 rule 11"
```

[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§4 P3 "hardcoded never-list"]

---

#### P6b.3 — `.claude/config/blast-radius-table.yaml`

```yaml
schema_version: 1
managed_by: brigadier
last_modified: 2026-04-28

# Analogous to Anthropic RSP ASL-tier structure applied at system-action level.
# [src:wave-b/consultants/anthropic-constitutional-ai.md:§4 P4 "ASL-tier analogue"]
# Graham margin-of-safety: over-engineer governance for Tier-0 (unbounded downside).
# [src:wave-b/consultants/capital-allocation-antifragility.md:§4 P2]

tiers:
  tier_0_integrity:
    label: "Tier 0 — Integrity"
    trigger: "auto-halt (no human gate required — auto-halt fires immediately)"
    description: "System corruption risk. Actions that could damage the Foundation substrate,
      overwrite locked decisions, or bypass constitutional controls."
    examples:
      - "overwriting any file under decisions/ without LOCKED gate packet"
      - "modifying ~/.ssh/ or /etc/ or .env paths"
      - "force-pushing to main branch"
      - "deleting swarm/awaiting-approval/ entries"
      - "removing LOCKED tag from a locked artefact"
      - "directly modifying F8/F9 canonical artefacts without gate"
    response: "halt + log + alert (immediate; 0 delay; SLA: ≤30 min alert delivery)"
    reversible_check: "N/A — auto-halt fires regardless of reversibility"
    F_level: F8  # Constitutional — not relaxable

  tier_1_strategic:
    label: "Tier 1 — Strategic"
    trigger: "Ruslan ack required before execution"
    description: "Strategic consequence. Canonical promotions, F8 invariant changes,
      external commitments, financial decisions above threshold."
    examples:
      - "canonical promotion of any artefact (LOCKED tag application)"
      - "F8/F9 claim promotion"
      - "external commitment on behalf of Jetix"
      - "financial decision above RUSLAN-LAYER threshold (specific value in RUSLAN-LAYER)"
      - "Foundation-revision proposal (any change to decisions/JETIX-VISION-FUNDAMENTAL*)"
      - "new agent system.md creation or modification"
    response: "gate-required; AWAITING-APPROVAL packet with gate_class: stop_gate; SLA: L2 ≤4h"
    reversible_check: "required; if irreversible, gate_class escalates to stop_gate regardless of tier"

  tier_2_tactical:
    label: "Tier 2 — Tactical"
    trigger: "batch ack acceptable (can accumulate into one gate packet)"
    description: "Meaningful change to non-canonical artefacts; new config entries;
      scheduled automation creation."
    examples:
      - "wiki entry promotion F4→F5 (not canonical)"
      - "non-canonical config change (.claude/config/*.yaml additions)"
      - "new cron or scheduled task creation"
      - "sg-banned-phrases.yaml new entry"
      - "agent strategies.md substantive revision (beyond DRR append)"
    response: "gate-required; AWAITING-APPROVAL packet with gate_class: stage_gate; SLA: L1 ≤24h batch"
    reversible_check: "if irreversible, escalate to Tier-1"

  tier_3_routine:
    label: "Tier 3 — Routine"
    trigger: "auto-log (no gate; log entry written)"
    description: "Low-blast, reversible, routine operations. In whitelist."
    examples:
      - "draft file creation"
      - "git commit with valid format"
      - "append-only log append"
      - "lint scan (advisory)"
      - "health metric read"
    response: "auto-execute + log_audit_entry; no gate"
    reversible_check: "if action is irreversible despite Tier-3 classification → escalate to Tier-2"

# Foundation/RUSLAN-LAYER note:
# - Tier structure (4 tiers, names, trigger types) = Foundation generic
# - Specific action-class → tier assignments = RUSLAN-LAYER (declared in RUSLAN-LAYER overlay)
# - Specific financial thresholds (e.g. "above €500") = RUSLAN-LAYER
ruslan_layer_note: "Tier structure is generic. Specific assignments per action class,
  financial thresholds, and SLA values are RUSLAN-LAYER overlays."
```

[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.6 "blast radius categorization"]
[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§3 "SLO + error-budget analogue"]

---

#### P6b.4 — `shared/schemas/awaiting-approval-packet.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "awaiting-approval-packet.json",
  "title": "AWAITING-APPROVAL Packet Schema",
  "description": "Gate packet schema for Part 6b Human Gate. Satisfies UND-4 binding (gate_class field). F-G-R compliant.",
  "type": "object",
  "required": [
    "gate_class",
    "packet_id",
    "timestamp",
    "actor",
    "summary",
    "outcomes",
    "provenance",
    "ack_request",
    "reversibility_class",
    "blast_radius_tier"
  ],
  "properties": {
    "gate_class": {
      "type": "string",
      "enum": ["stop_gate", "stage_gate", "draft_promotion"],
      "description": "UND-4 binding. stop_gate=canonical or constitutional; stage_gate=project lifecycle; draft_promotion=F3→F5 promotion below canonical."
    },
    "packet_id": {
      "type": "string",
      "pattern": "^pkt-[0-9]{8}-[0-9]{3}$",
      "description": "Format: pkt-YYYYMMDD-NNN. Unique per cycle."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 creation timestamp."
    },
    "actor": {
      "type": "string",
      "description": "Who initiated this packet. RUSLAN-LAYER tag for specific instances. Foundation-generic: 'brigadier' or 'agent:<role_slug>'."
    },
    "cycle_id": {
      "type": "string",
      "description": "Cycle identifier (e.g. cyc-foundation-build-2026-04-28)."
    },
    "summary": {
      "type": "string",
      "minLength": 50,
      "maxLength": 1500,
      "description": "1-3 paragraph executive summary. What is being proposed, why, what changes."
    },
    "outcomes": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "description": "List of changes proposed. Each item is one concrete change."
    },
    "provenance": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path"],
        "properties": {
          "path": {"type": "string"},
          "range": {"type": "string"},
          "quote": {"type": "string"}
        }
      },
      "minItems": 1,
      "description": "Source citations for claims in this packet. Non-empty mandatory."
    },
    "ack_request": {
      "type": "string",
      "description": "The specific decision Ruslan must make. Must be phrased as a Hamel-binary choice (A or B; approve or reject; etc). No open-ended requests.",
      "minLength": 20
    },
    "reversibility_class": {
      "type": "string",
      "enum": ["reversible", "hard-to-reverse", "irreversible"],
      "description": "Reversibility assessment for all combined outcomes in this packet."
    },
    "blast_radius_tier": {
      "type": "integer",
      "enum": [0, 1, 2, 3],
      "description": "Highest blast-radius tier across all outcomes. 0=integrity, 1=strategic, 2=tactical, 3=routine."
    },
    "f_g_r_delta": {
      "type": "object",
      "properties": {
        "F_before": {"type": "string"},
        "F_after": {"type": "string"},
        "ClaimScope": {"type": "string"},
        "R_change_note": {"type": "string"}
      },
      "description": "Optional. Part 6a applies this at gate-time for F-level delta tracking."
    },
    "advisory_cai_flag": {
      "type": "boolean",
      "default": false,
      "description": "OQ-CAI-3 stub. Set to true if a peer cell or scanner flagged potential sycophantic synthesis in the artefact under review. Does not auto-reject; surfaces to Ruslan for judgment."
    },
    "supersedes": {
      "type": "string",
      "description": "Optional. packet_id of a prior packet this packet corrects or replaces."
    },
    "sla_tier": {
      "type": "string",
      "enum": ["L1", "L2", "L3", "halt"],
      "description": "SLA tier per escalation-taxonomy.yaml. RUSLAN-LAYER populates specific ack windows."
    }
  },
  "additionalProperties": false
}
```

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:P6b.4 "UND-4 binding"]
[Verified against existing corpus: 8 gate packets in swarm/gates/ per src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3.3]

---

#### P6b.5 — `.claude/config/escalation-taxonomy.yaml`

```yaml
schema_version: 1
managed_by: brigadier
last_modified: 2026-04-28

# Foundation-GENERIC tier structure.
# RUSLAN-LAYER provides: specific ack windows, specific contact methods, specific delegation rules.

tiers:
  L1_routine:
    label: "L1 — Routine"
    blast_radius_trigger: tier-2-tactical
    description: "Batch-ackable tactical decisions. No time-critical dependency."
    ack_window_generic: "within 1 daily review session"
    ack_window_ruslan_layer: "RUSLAN-LAYER: ≤24h"  # Specific value = RUSLAN-LAYER
    batch_acceptable: true
    packet_accumulation_window: "1 working day"
    escalation_to_L2: "if batch grows to >5 open Tier-2 packets without ack"

  L2_review:
    label: "L2 — Review"
    blast_radius_trigger: tier-1-strategic
    description: "Strategic decisions requiring substantive human judgment. Not batch-ackable."
    ack_window_generic: "same session or next session"
    ack_window_ruslan_layer: "RUSLAN-LAYER: ≤4h"  # Specific value = RUSLAN-LAYER
    batch_acceptable: false
    escalation_to_L3: "if Tier-1 action is time-sensitive (external commitment deadline, financial expiry)"

  L3_urgent:
    label: "L3 — Urgent"
    blast_radius_trigger: tier-1-strategic-time-sensitive
    description: "Strategic decisions with external deadline or compounding risk if delayed."
    ack_window_generic: "immediate session"
    ack_window_ruslan_layer: "RUSLAN-LAYER: ≤30 min"  # Specific value = RUSLAN-LAYER
    batch_acceptable: false
    escalation_to_halt: "if L3 trigger involves §6.7 constitutional violation signal"

  halt_log_alert:
    label: "Halt-Log-Alert — Immediate"
    blast_radius_trigger: tier-0-integrity
    description: "Constitutional violation or integrity event. Immediate halt. No ack window — halt is unconditional."
    ack_window_generic: "no ack window — halt fires unconditionally"
    halt_ordering: "halt THEN log THEN alert (order enforced)"
    batch_acceptable: false
    constitutional_anchor: "FUNDAMENTAL §6.7 violation triggers + §6.1 constitutional limits"
    sre_analogue: "14.4× error-budget burn-rate SLO breach — behaviour changes immediately"
    # [src:wave-b/consultants/sre-observability.md:§5 Source 5 "14.4× burn rate = critical"]

# Stoic dichotomy classification per this taxonomy:
# Category A (in-system-control, enforceable):
#   - halt_log_alert fires structurally on Tier-0 event
#   - L2 and L3 packets route structurally based on blast_radius_tier
# Category B (influence-zone, monitoring only):
#   - Ruslan's ack within declared window is influence-zone (system cannot compel response timing)
#   - RUSLAN-LAYER SLA values are advisory targets, not hard constraints on Ruslan
# [src:wave-b/consultants/stoic-epistemic.md:§4 P5 "Category A vs B vs C"]
ruslan_layer_note: "Specific ack windows (≤24h, ≤4h, ≤30 min) and contact methods are
  RUSLAN-LAYER overlays. Foundation declares tier structure only."
```

[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2 "Escalation taxonomy — 4-class"]

---

### §J Operational Rituals

**Gate cadence:** Event-driven (not scheduled). Every agent action triggers blast-radius
classification query against `blast-radius-table.yaml` before execution. No polling.

**SLA monitoring:** Tier-2 and Tier-3 packets accumulate in `swarm/awaiting-approval/`. At
each cycle compound step, brigadier counts open packets by tier and emits a brief summary to
cycle log. If L1 batch > 5 open packets, escalate to L2.

**Friday 17:00 batch review ritual (RUSLAN-LAYER — specific to Ruslan):** All accumulated
Tier-2 (L1) packets from the week are reviewed in one session. This reduces HITL interruption
overhead during work sessions. RUSLAN-LAYER specificity: the Friday 17:00 timing is Ruslan's
rhythm, not a Foundation-generic constraint.

**Approval log maintenance:** `swarm/approvals/log.jsonl` appended on every gate resolution.
Markdown view (`log.md`) regenerated weekly via `/approvals --regen-log`.

[src:agents/mgmt-expert.md:§2.4 "CE 40/10/40/10 — Compound (10%) — brigadier writes meta/agent-improvements"]

---

### §K Failure Modes

| Failure mode | Detection signal | Response |
|---|---|---|
| **Gate skipped** (silent canonical promotion) | D6 audit dimension: canonical promotion in git log without corresponding gate packet in approval log | Part 6a raises as D6 finding → Part 6b creates retrospective gate packet for review + Ruslan ack for ratification |
| **Default-Deny whitelist drift** (creeping permissiveness) | Uncategorized action rate drops to near-zero while novel action types increase — suspicious | Quarterly audit: compare whitelist growth rate to novel action type growth; if mismatch, AWAITING-APPROVAL for whitelist review |
| **Blast-radius miscategorization** (Tier-2 action routed as Tier-3) | Post-incident analysis: action executed as routine caused non-routine consequence | Halt retroactively; add specific action class to Tier-2 in RUSLAN-LAYER overlay; DRR entry |
| **AWAITING-APPROVAL packet schema violation** | `gate_class` field missing; `packet_id` format wrong; `provenance` empty | Auto-reject with specific error code; brigadier re-drafts packet |
| **Halt-log-alert silent failure** | Alert fires but audit log entry is missing (alert-before-log ordering violation) | Halt-before-log-before-alert ordering enforced in `gate.sh`; test: generate a synthetic §6.7 trigger and verify log timestamp < alert timestamp |
| **SLA breach** (L2 packet unacked >4h) | Open packet age counter in cycle log exceeds declared window | Escalation to L3 per taxonomy; brigade escalates to direct Ruslan notification |
| **Cargo-cult ack** (Ruslan approves without review) | Ack timestamp < 60 seconds after packet creation (impossible if summary >500 words was read) | Influence-zone (cannot be structurally prevented); mitigation: Part 6b packets include an explicit "minimum read time estimate" field in summary footer |

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§3 "blameless postmortem culture"]

---

### §L Wave C Bullet Status + HARD GAPS

| Bullet | Acceptance predicate | Status |
|---|---|---|
| P6b.1 Stage-gate predicates registry | "Every promotion class has ≥4 Hamel-binary predicates; no banned-phrase patterns; sg-banned-phrases.yaml extended to ≥20 entries" | DRAFT — schema inline above; 6 new banned phrases documented (must be merged to .yaml file) |
| P6b.2 Default-Deny classifier | "Every action class in whitelisted_classes has blast_radius + reversible declared; hardcoded_never_list maps all 11 §6.1 rules; F8_invariant declared" | DRAFT — YAML inline above; constitutional grounding complete |
| P6b.3 Blast-radius table | "4 tiers declared (0/1/2/3); each tier has trigger, description, examples, response, reversibility check; Foundation/RUSLAN-LAYER note present" | DRAFT — YAML inline above |
| P6b.4 AWAITING-APPROVAL schema | "gate_class enum present and 3-value; packet_id pattern validated; all 10 required fields present; advisory_cai_flag stub included (OQ-CAI-3)" | DRAFT — JSON Schema draft-07 inline above; UND-4 satisfied |
| P6b.5 HITL escalation taxonomy | "4 tiers (L1/L2/L3/halt); each tier has blast_radius_trigger, ack window structure, batch_acceptable; Stoic dichotomy A/B note present" | DRAFT — YAML inline above |

**HARD GAP A (Ruslan ack required):** `gate_class` enum currently has 3 values
(`stop_gate`, `stage_gate`, `draft_promotion`). The existing 8 gate packets in `swarm/gates/`
use ad-hoc naming conventions. Ruslan must ack: (1) whether the 3-value enum is complete,
or (2) whether additional gate classes are needed (e.g. `audit_finding`, `emergency_halt`).
Without Ruslan ack, the enum is provisionally deployed at F4 (operational convention proposed,
not validated by cycle evidence). **Ruslan ack trigger: AWAITING-APPROVAL packet with
gate_class: stop_gate required before this schema is promoted to canonical.**

**HARD GAP B (implementation timeline):** The schemas and YAML configs above are DESIGN
ARTEFACTS (F4, draft). They are not yet implemented as actual files in the repository.
Ruslan must ack: (1) which cycle implements the files (recommend: next Wave C integration cycle);
(2) whether brigadier or a specific agent owns the `gate.sh` implementation. Without ack,
implementation timeline is undefined.
[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§0 "HARD GAP B scanner implementation timeline"]

---

### §M Wisdom Application Findings

| Wisdom source | Principle applied | Where in this design |
|---|---|---|
| Anthropic CAI (Bai 2022) | RLAIF as noise filter, not gate substitute | `advisory_cai_flag` field in AWAITING-APPROVAL schema; Constitutional AI P1 T3 resolution |
| Anthropic HHH (Askell 2021) | Corrigibility = MUST actively support oversight | D3 Deontic "MUST NOT make canonical promotion decisions autonomously" |
| Anthropic RSP ASL-tier structure | ASL-1..4 analogue for blast-radius tiers | 4-tier structure (0=integrity, 1=strategic, 2=tactical, 3=routine) mirrors ASL safety levels |
| SRE fail-loud (Google SRE Book) | Silent failures are worst bug category | L7 Law "constitutional violation = halt, not warning"; halt-log-alert ordering |
| SRE error-budget (SRE Workbook Ch.2) | 14.4× burn rate = critical window | halt_log_alert tier analogue: Tier-0 = unconditional halt |
| Capital Allocation / Graham margin-of-safety | Over-engineer governance for unbounded blast radius | Tier-0 auto-halt is over-investment relative to expected loss; correct per Graham |
| Stoic dichotomy (Epictetus via Holiday) | Classify in-control vs not-in-control | F.3 three-category classification (A=hard enforcement / B=monitoring / C=logging) |
| Levenchuk L/A/D/E (A.6.B) | Lane discipline prevents contract soup | §E structured as exactly four lanes (Laws / Admissibility / Deontics / Effects) |
| Levenchuk IP-1 (A.2) | Role ≠ Executor | No executor names in Foundation schemas; all role references are archetypes |
| FPF B.3 (F-G-R) | Trust calculus on every promoted claim | §G DOGFOOD table; F-G-R fields in AWAITING-APPROVAL schema (`f_g_r_delta`) |

---

### §N Provenance

```yaml
provenance:
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
    range: "full 133 lines"
    notes: "Primary interface card; L/A/D/E lanes; A.14 edges; F-G-R table; §E Laws; §F Anti-scope"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
    range: "lines 300-360"
    notes: "Part 6 bullets; Part 6b P6b.1-P6b.5 bullet definitions; effort/expert annotations"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
    range: "full; §4 P1-P7; §5 T3; §7 Part 6 application table; §8 OQ-CAI-3"
    notes: "RLAIF as noise filter; hardcoded never-list vs softcoded defaults; blast-radius ASL analogue; corrigibility"
  - path: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
    range: "§4.6 enforcement mechanisms; §6.1 11 hard rules; §6.7 halt-log-alert; §5.2 fail-loud"
    notes: "Primary constitutional source; Default-Deny origin; blast-radius category list"
  - path: swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
    range: "§0 VSM S3; §D typed edges; §F Anti-scope; §F.2 boundary 6a/6b; §F.3 Stoic"
    notes: "Clean 6a/6b boundary; reciprocal edge declaration; Stoic dichotomy three-category"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md
    range: "§4 P2 Graham margin-of-safety"
    notes: "Over-engineer governance for unbounded blast radius — grounding for Tier-0 auto-halt"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md
    range: "§4 P5 Stoic dichotomy of control"
    notes: "Three-category classification (A/B/C) for enforcement vs influence vs logging"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md
    range: "§3 fail-loud; §5 Source 5 error-budget burn rate"
    notes: "Fail-loud = halt, not warning; 14.4× burn rate analogue for Tier-0"
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
    range: "§4 P4 A.14; §4 P5 B.3; §4 P6 A.6.B; §8 AP-L4"
    notes: "Typed edges; F-G-R; L/A/D/E lanes; AP-L4 single-line-interface anti-pattern"
  - path: raw/books-md/anthropic/bai-2022-cai.md
    range: "Abstract; §3 Method (RLAIF loop); §4.4 Harmlessness vs Evasiveness"
    notes: "RLAIF method direct library read; applied as advisory pre-screen per T3 resolution"
  - path: decisions/AUDIT-CURRENT-STATE-2026-04-27.md
    range: "§3.3 cycles — AWAITING-APPROVAL existing corpus"
    notes: "8 existing gate packets in swarm/gates/ — pattern reference for schema design"
  - path: .claude/config/sg-banned-phrases.yaml
    range: "full file"
    notes: "18 existing banned phrases; 6 new entries documented in P6b.1 (to be merged)"
```

---

### §X Foundation vs RUSLAN-LAYER

**GENERIC (Foundation — applies to any Jetix instance):**
- Default-Deny framework structure (whitelisted_classes concept, hardcoded_never_list, no-creative-interpretation policy)
- Blast-radius 4-tier structure (Tier-0/1/2/3 names, trigger types, auto-halt/gate/log responses)
- AWAITING-APPROVAL packet required field set and JSON Schema
- Escalation taxonomy tier structure (L1/L2/L3/halt, ordering, batch rules)
- Halt-log-alert primitive (3-step ordered sequence, constitutional grounding)
- Stage-gate predicates structure (promotion class concepts, Hamel-binary requirement)
- OQ-CAI-3 sycophancy detection stub (advisory_cai_flag field — stub only)

**RUSLAN-LAYER (specific to current Ruslan deployment):**
- Specific whitelisted action classes beyond generic categories (project-slug creation, Notion sync, specific agent dispatch patterns)
- Specific blast-radius assignments per action class (e.g. "crm-record update = Tier-3")
- Specific financial decision threshold (e.g. "above €500 = Tier-1")
- Specific SLA values (≤24h L1, ≤4h L2, ≤30 min L3) — acknowledged in schemas as RUSLAN-LAYER values
- Ruslan as the specific terminal acker (the schema says "human owner"; RUSLAN-LAYER binds this to Ruslan)
- Friday 17:00 batch review ritual (specific to Ruslan's weekly rhythm)
- Specific contact/notification method for alerts (RUSLAN-LAYER: how alerts reach Ruslan — email, terminal, Notion)

[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§0 "двуслойным — Layer 1 FUNDAMENTAL / Layer 2 RUSLAN-LAYER"]

---

## Closing: Boundary Verdict 6a/6b

**Clean boundary.** The Part 6a/6b boundary is explicit and non-overlapping:

| Dimension | Part 6a (Provenance Officer) | Part 6b (Human Gate) |
|---|---|---|
| Cadence | Quarterly retrospective audit | Real-time per-artefact enforcement |
| VSM role | S3 audit lead | S3 enforcement arm |
| F-G-R relationship | Owns F-G-R schema (P6a.1); runs citation scanner (P6a.2); writes approval log entries (P6a.3) | Checks F-G-R compliance at gate-time using Part 6a findings; does NOT run scanner |
| AWAITING-APPROVAL | Does NOT own packet schema; records gate outcomes in approval log | Owns packet schema (P6b.4); enforces gate block; routes to Ruslan |
| Canonical write | Never (advisory, surfacing only) | Never (canonical write is Part 1's function via D25) |
| Halt authority | Surfaces findings; does NOT execute halts | Enforces halt-log-alert on §6.7 triggers |

Reciprocal edge declared: `Part 6b gate-class taxonomy referenced-by Part 6a approval-log`.
[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§D "Part 6b gate-class taxonomy referenced-by Part 6a approval-log"]

No boundary leakage detected. Both parts consume each other's outputs without duplicating
each other's functions.

**[INTEGRATOR] FINDING-I1:** The 6a/6b boundary design is sound. The primary risk is
implementation: if Part 6a's citation scanner is not built (HARD GAP B), Part 6b cannot
consume Part 6a's F-G-R compliance signals, forcing Part 6b to either skip F-G-R compliance
checks or duplicate the scanner logic. This is a concrete dependency that must be tracked.
