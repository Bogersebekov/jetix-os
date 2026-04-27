---
title: "Interface Card — Part 6: Governance, Provenance & Human Gate (SUPERSEDED Wave C Bundle 1)"
superseded_by:
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
split_note: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/SPLIT-NOTE-PART-6.md
split_rationale: "Per Ruslan walkthrough OQ-MERGED-1 OVERRIDE 2026-04-27 — split for scale-readiness Phase B/C/D + fork-friendly portable provenance + cadence independence (quarterly Part 6a vs real-time Part 6b)"
historical_note: "This interface card is SUPERSEDED for Wave C / Bundle 1 onward but PRESERVED in the historical record per Reversal Transactions discipline (Young 2010). Future references should use Part 6a or Part 6b explicitly. The Part 6 conceptual cluster persists as the parent role; Part 6a + Part 6b are MemberOf Part 6."
part_number: 6
part_slug: governance-provenance-human-gate
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
critic_status: FLAG-MINOR-RESOLVED
a1_correction_applied: "FPF anchor corrected per A-1-critic-gate.md §6 item 3: executor name 'meta-agent' removed; replaced with generic immune-system function. Specific role assignment (ontological-integrity-steward or equivalent) is RUSLAN-LAYER executor-binding, NOT a Foundation constituent [FPF §5.1 IP-1]."
originating_experts: [engineering-expert, systems-expert, investor-expert]
FUNDAMENTAL_UC: [H.5, A.3, A.4, H.4, I.4]
FPF_anchors: [IP-1, IP-3, IP-4, B.3, A.6.B, A.13, A.14]
D_lock_anchors: [D25, D27, FUNDAMENTAL §4.5, FUNDAMENTAL §4.6, FUNDAMENTAL §6.1, FUNDAMENTAL §6.7]
U_classification: "U.System — enforces constraints, produces gate decisions, writes approval-log entries"
F: F4
ClaimScope: "Holds for all Foundation Parts 1-10 as governance supersystem context; Part 6 operates-in all other parts (not ComponentOf). Specific role assignments to immune-system function are RUSLAN-LAYER bindings."
R:
  refuted_if: "Any agent successfully promotes a draft to canonical state without a Part 6 gate artifact (AWAITING-APPROVAL packet + human ack); OR any Foundation artifact reaches canonical state without F-G-R tags in frontmatter"
  accepted_if: "100% of canonical promotions trace to a Part 6 gate event in audit log; F-G-R compliance audit (periodic, Part 8-triggered) shows zero untagged canonical artifacts"
oq_merged_6_resolution: "Default-Deny classifier for novel/uncategorized actions is a Part 6 primary function per FUNDAMENTAL §6.1 last bullet ('якщо action не categorized — default deny + escalate, не creative interpretation'). Acked per A-1-critic-gate.md §4 OQ-MERGED-6."
l_a_d_e_self_exemplifies: "CRITICAL: this interface card itself must exemplify L/A/D/E lane discipline. Part 6 enforces L/A/D/E on all others; its own card demonstrates what it enforces [A-1-critic-gate.md §2 Part 6 A.6.B note]."
sources:
  - "candidate-parts-merged.md §2 Part 6 (with A-1 correction applied)"
  - "A-1-critic-gate.md §2 Part 6 (FLAG-MINOR resolved) + §4 OQ-MERGED-6"
  - "levenchuk-shsm-fpf.md §4 P5 (F-G-R B.3), §4 P6 (L/A/D/E A.6.B), §4 P1 (IP-1)"
  - "anthropic-constitutional-ai.md §4 P1-P7, §7 (Part 6 application table)"
  - "FUNDAMENTAL §4.5, §4.6, §6.1, §6.2, §6.7"
  - "design/JETIX-FPF.md §5.1 IP-1, §5.3 IP-3, §4.2 B.3, §4.3 A.6.B, §2.1a A.13, §3.5 A.14"
  - "AUDIT-CURRENT-STATE-2026-04-27.md §4 (swarm/awaiting-approval/, decisions/ D1-D29, swarm/gates/)"
---

# Interface Card — Part 6: Governance, Provenance & Human Gate

> **Self-exemplification note.** This card is authored under L/A/D/E lane discipline — the same discipline Part 6 enforces on all other parts. Every claim carries a provenance citation. Every section maps to a lane. The card does not exempt itself from its own standards. [A-1-critic-gate.md §2 Part 6 A.6.B critical note]

## A. Inputs

| Source | Data shape | Event trigger |
|---|---|---|
| Draft artifact from any part | Markdown file with YAML frontmatter: `proposed_writes[]`, `provenance[]`, `confidence`, `F-G-R fields`, `escalations[]` | `submit-draft-for-gate-event` — any part submitting a candidate for canonical promotion |
| Action with blast-radius tag (from any part) | Tagged action packet: blast-radius category (local-only / local-modifying / external-read / external-write / financial / public) per FUNDAMENTAL §4.6 | Any agent action before execution |
| Novel / uncategorized action (from any part) | Action description lacking a blast-radius tag | Default-Deny trigger: escalates immediately rather than proceeding [FUNDAMENTAL §6.1; OQ-MERGED-6 resolved] |
| Constitutional-violation signal | Trigger event from any part: "AI attempted strategize" / "agent attempted architectural decision" / "sycophancy detected" per FUNDAMENTAL §6.7 | Boundary-violation-event |
| Periodic audit request from Part 8 | Health-check trigger: quarterly F-G-R compliance audit across all canonical artifacts | `quarterly-audit-event` |

## B. Outputs

| Consumer | Data shape | Event published |
|---|---|---|
| Human owner (sole decision authority) | AWAITING-APPROVAL packet: structured gate document at `swarm/awaiting-approval/` or `decisions/AWAITING-APPROVAL-*.md` | `gate-submitted-event`; BLOCKED until human ack |
| Canonical artifact store (via Part 1) | Promoted artifact: LOCKED tag applied, canonical path written, git commit via Part 1 [D25] | `artifact-promoted-event` — only after human ack |
| Rejected draft (back to originating part) | Rejection packet: specific failure reason, required corrections, re-submission criteria | `draft-rejected-event` |
| Audit log (Part 1 substrate) | Append-only approval-log entry: artifact path, gate timestamp, human-ack timestamp, F-G-R snapshot at gate time | `audit-log-appended-event` |
| All other parts (broadcast) | F-G-R compliance status: quarterly report of untagged or mistagged canonical artifacts surfaced for correction | `compliance-report-emitted-event` |

## C. Side-effects

- Writes `swarm/awaiting-approval/<cycle>-<slug>.md` — gate packet (BLOCKED state, awaiting human ack) [AUDIT: 8 confirmed gate documents in `swarm/gates/`]
- Writes `decisions/` LOCKED files — canonical decisions after human ack [D25; FUNDAMENTAL §4.5]
- Writes approval-log entry (append-only) — `swarm/logs/cyc-*/cycle-log.md` per promotion event [D25 Company-as-Code]
- Does NOT write wiki canonical content directly — content promotion is triggered by Part 6 gate but executed through Part 3's ingest interface after ack
- Applies LOCKED tag to promoted artifacts — this tag is the measurable enforcement artifact; absence of tag = artifact has not passed gate [candidate-parts-merged.md §2 Part 6]
- Triggers halt-log-alert sequence on constitutional violation: halt = action stops; log = audit trail entry; alert = owner notification [FUNDAMENTAL §6.7; anthropic-constitutional-ai.md §4 P1 RLAIF analogue]

## D. Dependencies (typed per FPF A.14)

| Edge | Type | Rationale |
|---|---|---|
| Part 6 `operates-in` all other Parts | `operates-in` | Governance is the supersystem context every other part operates within — NOT ComponentOf any part; it is the constitutional enforcement layer that all parts are subject to [A-1-critic-gate.md §2 Part 6 A.14 note; levenchuk-shsm-fpf.md §4 P4] |
| Part 6 → Part 1 | `methodologically-uses` | All gate decisions are committed through git substrate; audit trail lives in Part 1 [D25; FPF §5.3 IP-3] |
| Part 7 → Part 6 | `methodologically-uses` | Per-project stage gates use Part 6's gate mechanism; Part 7 applies the mechanism, Part 6 owns it [A-1-critic-gate.md §2 Part 7 A.14 note] |
| Part 6 ↔ Part 8 | Dual: Part 6 `constrained-by` Part 8 audit signals; Part 8 `methodologically-uses` Part 6 escalation taxonomy | Part 6 = gate enforcement (real-time, per-artifact); Part 8 = drift audit (periodic, system-wide). Dual-ownership explicitly delineated: not collapsed into one [A-1-critic-gate.md §2 Part 8 B.3 dual-ownership note] |

## E. Boundary — L/A/D/E discipline [FPF §4.3 A.6.B; levenchuk-shsm-fpf.md §4 P6]

**Laws (invariants that MUST hold — constitutional, not negotiable):**
- Human ack is the TERMINAL decision point for every canonical promotion. No AI self-critique loop (Constitutional AI P1 RLAIF) substitutes for it — RLAIF reduces noise before the gate; it does not replace the gate [anthropic-constitutional-ai.md §5 T3; FUNDAMENTAL §4.3 Human-Only].
- The 11 hard AI/agent limits from FUNDAMENTAL §6.1 are encoded as structural invariants in Part 6, not behavioral conventions. Violation = halt-log-alert, not warning [FUNDAMENTAL §6.7; anthropic-constitutional-ai.md §4 P3 hardcoded never-list parallel].
- Every canonical artifact MUST carry F-G-R frontmatter fields (F, ClaimScope, R). Absent F-G-R = gate failure [FPF §4.2 B.3; levenchuk-shsm-fpf.md §4 P5].
- Default-Deny posture on uncategorized actions: if an action lacks a blast-radius tag, the gate issues automatic deny + escalate, never "creative interpretation" [FUNDAMENTAL §6.1 last bullet; FUNDAMENTAL §4.6; OQ-MERGED-6].
- Reversibility check mandatory: any irreversible action (delete / overwrite / external-write / financial) requires explicit human ack regardless of blast-radius category [FUNDAMENTAL §4.6; anthropic-constitutional-ai.md §4 P5; FUNDAMENTAL §5.5 confirmation-for-destructive-ops].
- IP-1 enforcement is a Part 6 quarterly audit function: no executor name in Foundation-level Part definitions. Violations surfaced as immune-system audit finding [A-1-critic-gate.md §2 Part 6 IP-1 note; FPF §5.1 IP-1].

**Admissibility (acceptance criteria for inputs — what the gate accepts):**
- Draft artifact is accepted into gate review only if: (a) `proposed_writes[]` non-empty, (b) `provenance[]` non-empty with inline `[src:...]` citations, (c) F-G-R frontmatter fields present, (d) acceptance predicate is Hamel-binary (not prose) [anthropic-constitutional-ai.md §7 provenance & transparency row; levenchuk-shsm-fpf.md §5 trigger 4].
- Action is accepted into auto-execute path only if blast-radius tag exists AND tag maps to §4.1 auto-always category AND action is reversible [FUNDAMENTAL §4.1, §4.4, §4.6].
- Foundation-revision proposals are accepted into AWAITING-APPROVAL gate only (never silently merged); Ruslan ack mandatory before any Foundation document modification [deep-prompt §8 R4].

**Deontics (obligations of Part 6 toward consumers and owner):**
- Part 6 MUST surface every gate failure with specific failure reason and required corrections — not a generic "rejected" [levenchuk-shsm-fpf.md §8 AP-L4 single-line-interface anti-pattern].
- Part 6 MUST maintain an append-only approval log — no edits of prior log entries [D25; FUNDAMENTAL §5.5 append-only].
- Part 6 MUST NOT make canonical promotion decisions autonomously — human ack is architecturally mandatory, not behaviorally expected [FUNDAMENTAL §4.3; anthropic-constitutional-ai.md §4 P6 transparency/corrigibility].
- Part 6 MUST escalate constitutional violations immediately (halt-log-alert sequence) — no silent swallowing [FUNDAMENTAL §6.7; FUNDAMENTAL §5.5 no-silent-error-swallowing].
- Part 6 MUST own F-G-R compliance enforcement (gate-time, per-artifact) as distinct from Part 8's periodic audit (system-wide drift) — the delineation must be explicit in Wave C interface cards for both parts [A-1-critic-gate.md §2 Part 8 B.3 dual-ownership].

**Effects (measurable outcomes):**
- Gate throughput: count(artifacts promoted to canonical) / count(gate submissions) per cycle — baseline metric. Rejection rate signals draft quality [FUNDAMENTAL §3 health indicators].
- Constitutional compliance: count(§6.1 violations detected + halted) per cycle = 0 target [FUNDAMENTAL §3.2.5 no-strategy-violations health indicator].
- F-G-R coverage: (canonical artifacts with F-G-R tags) / (total canonical artifacts) = 100% target [B.3; F-G-R compliance enforcement gap: Wave C materialisation task per candidate-parts-merged.md §2 Part 6].
- Provenance coverage: (canonical artifacts with non-empty provenance[]) / (total canonical artifacts) = 100% target [D25; anthropic-constitutional-ai.md §7 provenance row].
- Blast-radius classification rate: (actions with blast-radius tag) / (total agent actions) = 100% target; uncategorized rate = 0 [OQ-MERGED-6; FUNDAMENTAL §4.6].

## F. Anti-scope

- **Does NOT make canonical promotion decisions unilaterally.** Final authority = human owner. Part 6 prepares the gate packet and enforces the process; it does not have authority to promote [FUNDAMENTAL §4.3; anthropic-constitutional-ai.md §4 P6; FUNDAMENTAL §6.2 agency-preservation — 10 rules].
- **Does NOT name specific agents (executor instances) as role-fillers for the immune-system function.** The immune-system function (IP-4, quarterly ontological-integrity audit) is Part 6's function; the role assigned to fill it is a RUSLAN-LAYER executor-binding, not a Foundation-level constituent [FPF §5.1 IP-1; A-1-critic-gate.md §6 item 3 FLAG-MINOR resolved].
- **Does NOT own periodic health monitoring.** Part 6 = per-artifact gate enforcement (real-time). Part 8 = system-wide drift audit (periodic). These are structurally distinct; conflating them creates dual-ownership without clear accountability [A-1-critic-gate.md §2 Part 8 B.3 dual-ownership note].
- **Does NOT own project lifecycle state machines.** Per-project stage gates use Part 6's gate mechanism (methodologically-uses); Part 7 owns the lifecycle schema [A-1-critic-gate.md §2 Part 7].
- **Does NOT engage-economy patterns.** Part 6 alerts are actionable-only: AWAITING-APPROVAL notifications fire when human decision is genuinely required; no FOMO triggers, no engagement-metric notifications [FUNDAMENTAL §6.3 anti-engagement-economy].
- **Does NOT implement sycophancy-detection mechanism (yet).** FUNDAMENTAL §6.7 names "sycophancy detected in synthesis → flag + retry" as a trigger, but no detection mechanism is specified. This is OQ-CAI-3 (Wave C gap) [anthropic-constitutional-ai.md §8 OQ-CAI-3].
- **Does NOT auto-promote cross-Foundation-document contradictions.** If a new draft contradicts an accepted Foundation document, Part 6 surfaces the contradiction as an escalation — it does not resolve it autonomously [deep-prompt §8 R4; levenchuk-shsm-fpf.md §5 trigger 4].

## G. F-G-R tagging [FPF §4.2 B.3; anthropic-constitutional-ai.md §7 provenance & transparency row]

| Artifact | F | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| AWAITING-APPROVAL gate packet | F4 — operational convention (gate structure consistent cycles 1-11) | All Foundation parts; gate structure is generic | R-medium (gate content reliability depends on draft quality; gate process reliability = R-high) |
| LOCKED canonical decision (D-series) | F6 — codified rule + ≥3 successful applications (D1-D29 operational) | Full Foundation scope; bridge required for fork instances per D27 | R-high (constitutional anchor; human-acked) |
| Approval-log entry | F5 — codified audit record | Foundation-level audit trail | R-high (append-only; not editable post-write) |
| F-G-R compliance report (quarterly) | F4 — operational convention (audit cadence pending Wave C materialisation) | All canonical artifacts at audit time | R-medium until automated scanner implemented (Wave C gap) |
| Blast-radius classification (per action) | F4-F5 depending on category maturity | Actions within current Foundation scope; novel action categories start at F2 | R-medium; grows to R-high as classification table stabilises across cycles |
| Constitutional violation halt-log-alert | F5 — codified rule (FUNDAMENTAL §6.7 hardcoded) | All Jetix Foundation instances | R-high (constitutional; not softcoded) |

## H. Originating expert + critic flags + OQ notes

- **Originating experts:** Engineering-expert (Part 5: Governance & Quality Gates), systems-expert (Part 3: Governance & Provenance), investor-expert (Part 5: Founder Agency Preservation + Part 1: Provenance Audit-Trail). Merged per Popper test: both provenance substrate and human gate serve the single invariant "no canonical change without auditable human-acked record" [candidate-parts-merged.md §2 Part 6 rationale].
- **A-1 critic verdict: FLAG-MINOR resolved.** Correction applied in frontmatter and §H above: "meta-agent" executor name removed from FPF anchor; replaced with "immune-system function (ontological-integrity-steward role or equivalent); specific role assignment is RUSLAN-LAYER executor-binding" [A-1-critic-gate.md §6 item 3].
- **OQ-MERGED-6 resolved:** Default-Deny classifier for novel/uncategorized actions is a Part 6 primary function — encoded in §E Laws lane and §B Outputs (Default-Deny trigger) above [A-1-critic-gate.md §4 OQ-MERGED-6; FUNDAMENTAL §6.1 last bullet].
- **Constitutional AI alignment:** Part 6 is the structural enforcement substrate for Constitutional AI principles in Jetix. Full mapping in `anthropic-constitutional-ai.md §7 Part 6 application table` — 7 Constitutional AI concepts mapped to Part 6 mechanisms.
- **Wave C primary gap:** F-G-R compliance enforcement is NOT yet a systematic Part 6-owned function. Current state: F-G-R tags exist in some artifacts but no automated scan + exception-to-HITL routing exists. Wave C task: build F-G-R compliance checker as a Part 6 service with automated scan + exception routing [candidate-parts-merged.md §2 Part 6 Cycles reuse note; anthropic-constitutional-ai.md §7 key implication].
- **AUDIT existing artefacts to reuse:** `swarm/awaiting-approval/cycle-*.md`; `swarm/gates/AWAITING-APPROVAL-*` (8 confirmed); `decisions/` (D1-D29 LOCKED); `swarm/logs/cyc-*/cycle-log.md`; `.claude/config/sg-banned-phrases.yaml` (18 banned-phrase entries); `/lint --check-stage-gates --validate-predicate` [AUDIT §4; candidate-parts-merged.md §2 Part 6 AUDIT mapping].
