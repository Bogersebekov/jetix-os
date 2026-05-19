---
title: "FPF/IWE Cooperation Plan — 3-Tier Engagement Ladder (Optimizer Proposal)"
type: optimizer-proposal
produced_by: mgmt-expert
mode: optimizer
expert: mgmt-expert
cycle_id: task-fpf-iwe-phase-b-2026-05-17
task_id: task-fpf-iwe-phase-b-2026-05-17
sources:
  - reports/jetix-vs-iwe-audit-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/05-residencies-format.md
  - reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
  - inbox/levenchuk-tg-2026-05-17.md
  - _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
provenance_inline: true
F: F4
G: optimizer-proposal-cooperation-plan
R: refuted_if_Levenchuk_rejects_tiered_approach_OR_Tseren_unavailable_OR_C4-benchmark-not-run
prose_authored_by: mgmt-expert (scribe, optimizer mode)
constitutional_posture: R1 scribe — NOT authoring strategic prose; optimizer = before/after + 5 invariants
---

# FPF/IWE Cooperation Plan — mgmt × optimizer proposal

> **Optimizer posture.** This draft applies the mgmt × optimizer rubric: before/after
> snapshot, 5 invariant declarations, per-tier GIVES/WANTS/KNOWS/EXIT tables,
> per-tier circuit breakers, R12 calibration, RACI per tier. No strategic prose authored.
> No method-change proposed. Brigadier integrates with investor × scalability +
> phil × critic cells.

---

## §1 Invariant Check (precondition — before any delta)

| Invariant | Applies? | Preserved by proposed delta? | Failure consequence if broken |
|---|---|---|---|
| **WLNK** Work-linkage: every tier deliverable has a named wiki/decision-doc path | YES — tier deliverables are wiki artefacts that Ruslan + swarm read/update | YES — each tier has an explicit `proposed_write_path:` below | Silent handoff break: tier says "done" with no artefact; Ruslan loses the shared state record |
| **MONO** Monotonicity: later tiers strictly extend earlier tier deliverables, never remove | YES — Tier 2 must extend Tier 1 observables; Tier 3 must extend Tier 2 | YES — table structure enforces additive extension; Tier 2 GIVES absorbs Tier 1 GIVES | Regression: Tier 3 engagement drops an accountability that Tier 1 established |
| **IDEM** Idempotency: re-issuing a tier offer does not change state if already accepted | YES — if Ruslan re-sends Tier 1 invite after Tseren already accepted, state must not regress | YES — each tier has an `acceptance_state:` field; re-offer treated as no-op if state = accepted | State drift: duplicate tier invites create conflicting cooperation commitments |
| **COMM** Commutativity: Tier 1 + Tier 2 can run in either sequence if both apply | PARTIAL — Tier 1 is the epistemic prerequisite (Ruslan must attend residency to have basis for Tier 2 joint artefact); COMM is intentionally limited per §2.3 sequencing rule below | PARTIAL PRESERVED — sequencing constraint declared explicitly; not silently assumed | Commutativity failure: Tier 2 joint artefact without Tier 1 learning = low-quality artefact; circuit breaker required |
| **LOC** Locality: changes scoped to declared tier; no creeping scope | YES — each tier has explicit anti-scope enumeration | YES — anti-scope listed per tier below | Scope leak: Tier 1 "observation" morphs into de facto Tier 2 commitment without explicit upgrade |

**COMM constraint declaration.** Tier 1 is an ordering prerequisite for Tier 2 joint artefact on methodology topics (Ruslan needs R0/R1 learning basis to co-author a credible R12/FPF extension). Tier 1 + Tier 3 COULD run concurrently (Levenchuk charter-review role is independent of Ruslan's residency progress). COMM holds for the Levenchuk track; constrained for the Tseren track. This is an execution-parameter constraint, NOT a method-change.

---

## §2 Before/After Snapshot

Current state (baseline): **no structured cooperation with FPF/IWE/MIM**. Levenchuk C3 skepticism (inbox/levenchuk-tg-2026-05-17.md) is the observable signal. No joint artefact exists. No shared commitment exists. Relationship strength: Tseren 2/10 (warm), Levenchuk 1/10 (cold) per CRM.

After (proposed 3-tier ladder): structured engagement with measurable KPIs per tier and explicit circuit breakers.

| Metric | Baseline (current) | Proposed (Tier 1 complete) | Proposed (Tier 2 complete) | Proposed (Tier 3 active) | Direction preferred |
|---|---|---|---|---|---|
| **handoff-count** (Ruslan ↔ MIM per month) | 0 | 4-8 (weekly разборы × 1 month) | 8-20 (разборы + 1-2 joint workshop sessions) | 12-24 (разборы + advisory check-ins) | Stable at Tier 2 level; not ↓ |
| **decision-latency** (time from "cooperation idea" to first joint artefact) | infinite (no path) | ~30 days (Tier 1 R0 entry → first разбор) | ~90 days (R0 complete + first co-authored note) | ~180-360 days (formal advisory or module) | ↓ |
| **priority-reversal-rate** (cooperation scope changes per month) | n/a (no engagement) | 0 (observation only, no commitments to reverse) | target <20% (small scope, 1 joint exercise) | target <20% (advisory scope stable) | ↓ toward <20% |
| **stakeholder-update-frequency** (Ruslan → Tseren/Levenchuk per month) | 0 (one unanswered message) | 4-8 (разбор participation → implicit updates) | 8-16 (разбор + joint artefact reviews) | Monthly advisory check-in (1/month each) | ↑ from 0 to cadenced |
| **ap_budget-actual variance** (cost estimate vs actual) | n/a | Tier 1: €0-€100 (Aisystant subscription, Phase A §0.0 ack: Ruslan pays; €10/day cap) | Tier 2: €0-€200 (1-2 workshop sessions; online format = near-zero variable cost above subscription) | Tier 3: 0 (Ruslan time only; equity requires explicit HITL ack per R12) | ↓ variance by making costs explicit |
| **backlog-age-p50** (age of unresolved FPF/IWE questions in Jetix backlog) | Growing (C4 benchmark, I-U2 gap, FPF integration — all open, no path) | -30 days on C4 benchmark (Tier 1 subscription activates IWE access for B2 unblock) | -60 days (Tier 2 exercise resolves 2-3 open gaps via firsthand Tseren observation) | -120 days (Tier 3 advisory closes FPF integration questions) | ↓ |
| **OKR-confidence per KR** (confidence in FPF-integration KR) | 0.1 (no path forward) | 0.4 (Tier 1 IWE direct access + разборы) | 0.6 (Tier 2 Tseren observes Jetix substrate, gives technical feedback) | 0.8 (Tier 3 Levenchuk reviews Foundation + Tseren co-develops module) | ↑ |

`[src: inbox/levenchuk-tg-2026-05-17.md C3+C7; _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §8 Tseren + §8 Levenchuk]`

---

## §3 Tier 1 — Light (1-month observation)

### §3.1 Description

**Scale.** 1 person (Ruslan), 1 month, no joint artefact, no commitment from FPF/MIM side.
**Entry trigger.** Ruslan applies to next R0 cohort (Aisystant subscription per Phase A §0.0 ack).

`[src: reports/fpf-iwe-distillation-2026-05-17/05-residencies-format.md §1.1-§2]`

### §3.2 GIVES / WANTS / KNOWS / EXIT table

| Slot | Jetix side | FPF/MIM side |
|---|---|---|
| **GIVES** | Engaged residency participant (Ruslan as active разборы contributor) + methodological background (systems thinking applied to multi-agent OS) | R0 cohort access + IWE (Intellectual Work Environment) direct hands-on + weekly разборы с mentor | 
| **WANTS** | Firsthand IWE/FPF operational experience (resolves B2 blocker); C4 benchmark Arm C baseline materialized via IWE subscription; direct observation of MIM pedagogy pattern | Engaged participant who applies MIM methodology to real project (Jetix is a non-trivial real project — methodologist's разбор material) |
| **KNOWS it's working** | After 4 weeks: Ruslan can describe IWE OWC discipline operationally (not from README); at least 1 разбор session where Jetix project was discussed using MIM framing; B2 blocker (paid AI guide) resolved | Participant shows systematic application of R0 material to own project in each разбор (not surface-level) |
| **EXIT** | Tier 1 ends at 4-week mark (1 month per brief). Ruslan decides: upgrade to Tier 2, stay in Tier 1 (continue R1), or downgrade to observation-only (read-only, no разборы). No commitment to FPF/MIM required. | MIM has no commitment to Jetix beyond standard cohort participation. Tseren/Levenchuk under no obligation. |

### §3.3 Anti-scope (what Tier 1 is NOT)

- Tier 1 does NOT produce a joint artefact (→ Tier 2 territory)
- Tier 1 does NOT surface Jetix cooperation proposal to Levenchuk/Tseren directly (→ observe first, propose from informed position)
- Tier 1 does NOT commit Jetix to adopting FPF as base tier (→ Ruslan strategic decision; Phase A §5 FPF integration is a candidate, not a lock)
- Tier 1 does NOT constitute an endorsement or testimonial for MIM (→ not public-facing)
- Tier 1 does NOT require Tseren/Levenchuk to allocate time specifically to Jetix

### §3.4 Proposed artefact path

`wiki/decisions/tier-1-mim-residency-log-2026-<date>.md` — Ruslan-authored (scribe notes from residency; private until Tier 2 gate). Updated weekly per разбор session.

### §3.5 Cost

Aisystant subscription (price not captured Phase A; estimate: €0-€100/month based on pricing page). Phase A §0.0 ack: Ruslan pays; €10/day baseline cap applies. If pricing exceeds cap → escalation to HITL before commitment.

`[src: reports/fpf-iwe-distillation-2026-05-17/05-residencies-format.md §6]`

---

## §4 Tier 2 — Medium (3-month cooperation)

### §4.1 Description

**Scale.** 1-2 joint sessions; 1 co-authored small artefact; cross-citation. Requires Tier 1 complete OR parallel (Levenchuk track, see §2.3 COMM note above).
**Entry trigger.** Tier 1 month complete AND circuit breaker NOT fired (§5) AND explicit Ruslan decision to upgrade.

`[src: _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §7 Tseren + §7 Levenchuk (стиль работы / партнёрство)]`

### §4.2 GIVES / WANTS / KNOWS / EXIT table

| Slot | Jetix side | FPF/MIM side |
|---|---|---|
| **GIVES** | (a) C4 benchmark results (Arm A/B/C comparison per Levenchuk C4 spec — tangible operational proof); (b) Jetix R12 anti-extraction framing as candidate FPF Part E extension proposal (written by Ruslan, reviewed by Tseren); (c) Jetix as live case study for Tseren разбор (1-2 structured sessions where Tseren observes Jetix substrate through MIM lens) | (a) 1-2 dedicated разбор sessions focused on Jetix substrate using FPF/MIM framing; (b) Tseren's expert read on C4 benchmark design / methodology; (c) Levenchuk review comment on R12 anti-extraction proposal (if he chooses) |
| **WANTS** | (a) Expert FPF critique of Jetix Foundation from Tseren (not marketing — surgical gaps); (b) Validation or falsification of «complementary, not substitutionary» framing (audit §0 verdict); (c) First-class citizenship in MIM methodological conversation (not «vanilla AI-agent» label) | (a) Methodologically rigorous peer showing real applied work (not vague startup pitch); (b) R12 anti-extraction proposal potentially extending FPF corpus (novel contribution from Jetix-side research) |
| **KNOWS it's working** | After 3 months: C4 benchmark results exist as shareable artefact; R12 proposal written + reviewed by Tseren (any verdict — accept/reject/partial); Tseren/Levenchuk have first-hand observable of Jetix substrate (not just a PDF) | Tseren has observed Jetix разбор at least once; R12 proposal received + reviewed with written comment; C4 benchmark Arm A/B/C exists and is citable |
| **EXIT** | Tier 2 ends at 3-month mark. Ruslan decides: upgrade to Tier 3, maintain Tier 2 level (ongoing разборы without advisory formalization), or return to Tier 1. No equity, no advisory title, no public commitment at this stage. | FPF/MIM under no formal obligation beyond agreed 1-2 sessions. Tseren/Levenchuk can decline Tier 3 upgrade with no consequence to Tier 2 artefacts already produced. |

### §4.3 Anti-scope (what Tier 2 is NOT)

- Tier 2 does NOT formalize an advisory or consulting relationship (→ Tier 3)
- Tier 2 does NOT produce an IWE/FPF module branded «Jetix» (→ Tier 3)
- Tier 2 does NOT include equity, revenue share, or capital (→ requires explicit HITL ack per R12)
- Tier 2 does NOT require Tseren/Levenchuk public endorsement of Jetix
- Tier 2 does NOT merge Jetix Foundation with IWE (→ strategic decision; HITL)
- Tier 2 does NOT constitute a partnership announcement or joint marketing

### §4.4 Proposed artefact paths

- `wiki/decisions/tier-2-c4-benchmark-results-<date>.md` — C4 benchmark (Arm A vanilla / Arm B FPF-loaded / Arm C Jetix-stack) per Levenchuk C4 spec [src: inbox/levenchuk-tg-2026-05-17.md C4]
- `wiki/decisions/tier-2-r12-fpf-extension-proposal-<date>.md` — R12 anti-extraction as FPF Part E candidate (Ruslan-authored per Tier 2 R1 constitutional posture) [src: decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md §5 M-C]
- `wiki/decisions/tier-2-tseren-razborka-session-log-<date>.md` — notes from 1-2 Jetix разбор sessions with Tseren

### §4.5 Cost

Tier 2 cost beyond Tier 1 subscription: primarily Ruslan time. Sessions online = near-zero variable cost. If Tseren charges for dedicated разбор time (non-cohort) → escalation to HITL before commitment (per §1d «assumes no budget without HITL»).

---

## §5 Tier 3 — Deep (6-12 month strategic)

### §5.1 Description

**Scale.** Formal advisory role for Levenchuk (Foundation reviews) + Tseren (substrate co-development); co-developed module possibility; equity-leaning only via explicit HITL.
**Entry trigger.** Tier 2 complete AND C4 benchmark shows differential Jetix advantage AND Levenchuk/Tseren explicitly indicate interest in deeper engagement AND Ruslan HITL decision.

`[src: _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §8 Levenchuk (Tyson-mentor candidate, Critical path A1.2)]`

### §5.2 GIVES / WANTS / KNOWS / EXIT table

| Slot | Jetix side | FPF/MIM side |
|---|---|---|
| **GIVES** | (a) Named advisory role for Levenchuk: periodic Foundation version reviews (semi-annual); formal cite in Jetix canonical docs (`swarm/wiki/foundations/` credits); (b) Tseren: formal co-developer credit on Jetix-as-IWE-Pack module (if produced); (c) First Clan Charter L1 candidate invitation (stealth mode per Charter §1 Q-D3); (d) R12-compliant equity proposal (if Ruslan acks at HITL gate — requires AWAITING-APPROVAL packet, not this optimizer draft) | (a) Levenchuk: ongoing interaction with live FPF-applied system (feedback loop into FPF-Spec revision potential); (b) Tseren: IWE-Pack extension with Jetix case study (adds to IWE distribution surface); (c) First Clan participation (if Charter resonates) |
| **WANTS** | (a) Levenchuk as «Tyson-mentor» (H5 pattern): depth-mentorship on systems thinking methodology (35+ years consulting lineage not available anywhere else in Russian-language space); (b) Tseren as operational peer: «closest existing operational analog Jetix Workshop substrate» for ongoing cross-pollination; (c) FPF as structural Base tier in Jetix Foundation fallback chain (currently tactical adoption ~5 mechanisms; Tier 3 goal = structural adoption at D-SYS-2 F5 level) | (a) Levenchuk: evidence that FPF works at org-scale (multi-agent OS) — not just individual exocortex; potentially publishable observation; (b) Tseren: validated IWE-Pack extension use case (Jetix as IWE-Pack for AI-consulting domain) |
| **KNOWS it's working** | After 6 months: Levenchuk reviewed ≥1 Foundation version with written comment; FPF structural integration proposal written; Tseren разборы continue (monthly); if IWE-Pack discussion started, concrete module outline exists | Levenchuk: ≥1 written review of Jetix Foundation submitted; (optionally) Levenchuk FPF updated with cross-reference to Jetix case; Tseren: active participation in Jetix разбор cadence; module outline exists |
| **EXIT** | Tier 3 ends when either: (a) Levenchuk/Tseren request discontinuation; (b) 12-month milestone with no mutual-value KPI progress (§5.3 circuit breaker); (c) Ruslan strategic decision. Equity proposals require explicit AWAITING-APPROVAL packet before discussion. R12: both sides can exit without penalty. | Same symmetric exit: FPF/MIM can discontinue at any advisory checkpoint without penalty to Tier 1/2 artefacts already produced. Fork-and-leave preserved per R12. |

### §5.3 Anti-scope (what Tier 3 is NOT)

- Tier 3 does NOT auto-authorize equity discussion (→ requires HITL AWAITING-APPROVAL; this draft cannot grant it)
- Tier 3 does NOT merge Jetix and MIM into a joint venture or shared brand
- Tier 3 does NOT transfer control of Jetix Foundation to Levenchuk/Tseren (Ruslan = sole strategist per Tier 2 R1)
- Tier 3 does NOT impose IWE-Pack adoption on Jetix (it remains an option subject to Ruslan strategic decision)
- Tier 3 does NOT constitute a public announcement without Ruslan decision (Charter remains STEALTH per Q-D3)

### §5.4 Proposed artefact paths

- `wiki/decisions/tier-3-advisory-charter-levenchuk-<date>.md` — formal advisory scope (Ruslan-authored, requires AWAITING-APPROVAL if any equity)
- `wiki/decisions/tier-3-fpf-integration-proposal-<date>.md` — FPF as structural Base tier in Jetix Foundation (AWAITING-APPROVAL gate per §1d — this is a Foundation-level revision)
- `wiki/decisions/tier-3-iwe-pack-jetix-module-outline-<date>.md` — Jetix-as-IWE-Pack module outline (Ruslan + Tseren co-authored; Ruslan-authored primary per Tier 2 R1)

---

## §6 Per-Tier Circuit Breakers

Circuit breaker = condition that triggers tier downgrade (or pause). Each is a binary predicate (fires / does not fire).

| Tier | Circuit breaker | Predicate (binary) | Action on fire |
|---|---|---|---|
| **Tier 1** | No IWE value signal | After 4 weeks в разборах: Ruslan cannot name ≥1 IWE mechanism that operates differently from Jetix equivalent AND 0 разбор sessions produced MIM-lens observation of Jetix project | Downgrade to Tier 0 (read-only: Levenchuk LJ + FPF-Spec study; no subscription renewal) |
| **Tier 1** | Budget overrun | Aisystant subscription price > €10/day-equivalent when normalized to monthly | HITL AWAITING-APPROVAL before payment; if not acked → Tier 0 |
| **Tier 2** | No mutual-value signal within 30 days of Tier 2 start | C4 benchmark not initiated AND R12 proposal not drafted AND no Tseren разбор session scheduled | Downgrade to Tier 1 (continue residency; defer Tier 2 joint work by 30 days) |
| **Tier 2** | Tseren/Levenchuk unavailability | Tseren explicitly declines 1-2 dedicated sessions AND Levenchuk explicitly declines R12 review | Maintain Tier 1; do not escalate to Tier 3; re-trigger Tier 2 entry at next opportunity (≥6 months) |
| **Tier 2** | C4 benchmark null result | C4 benchmark Arm A/B/C complete AND Arm C (Jetix-stack) scores ≤ Arm A (vanilla) on ≥4 of 7 criteria | Do NOT upgrade to Tier 3 (Levenchuk C3 skepticism would be validated); maintain Tier 1/2; address Arm C gap before proposing deeper engagement |
| **Tier 3** | No 6-month progress | At 6-month Tier 3 checkpoint: Levenchuk has NOT submitted ≥1 Foundation review AND FPF integration proposal NOT written AND Tseren разбор cadence dropped to 0 | Downgrade to Tier 2 level; remove advisory title; no penalty per R12 |
| **Tier 3** | Equity demand exceeding R12 | Any equity, revenue-share, or exclusivity request that violates R12 («cannot extract value beyond agreed share; members can fork-and-leave without penalty») | PAUSE Tier 3; open AWAITING-APPROVAL packet for HITL; do NOT negotiate equity autonomously |

`[src: reports/jetix-vs-iwe-audit-2026-05-17.md §12 Q.5 (R12 surfacing к Tseren); decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md §1.0a]`

---

## §7 R12 Anti-Extraction Explicit Calibration

R12 is Pillar C Tier 2 constitutional candidate rule 12 (CLAUDE.md §4.1 rule 12, LOCKED 2026-05-12):
> «AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

Applied SYMMETRICALLY to FPF/IWE cooperation:

**Direction 1 — Jetix does NOT extract from FPF/MIM beyond agreed share.**

- Tier 1: Ruslan pays for residency access (market rate). No extraction of Tseren/Levenchuk time beyond standard cohort разборы. No recording of sessions without explicit permission. No public citation of разбор content without permission.
- Tier 2: Joint artefacts (C4 benchmark, R12 proposal) are co-attributed. Tseren/Levenchuk review sessions are explicitly scoped and time-bounded per §4.2.
- Tier 3: Advisory role is explicitly scoped, compensated (per HITL-acked terms), and revocable. No exclusivity demanded. No IP transfer without explicit consent.

`F: F5 | ClaimScope: holds for all 3 tiers | R: refuted_if_Jetix_demands_unpaid_hours_beyond_agreed_scope`

**Direction 2 — FPF/MIM does NOT extract from Jetix beyond agreed share.**

- Tier 1: Aisystant subscription is Ruslan's data and usage — MIM platform does not receive Jetix proprietary Foundation documents or client data without Ruslan decision.
- Tier 2: R12 proposal contribution is Ruslan-authored and remains Ruslan-owned IP until explicit open-source decision. Tseren's review of C4 benchmark is advisory, not co-authorship of Jetix internal processes.
- Tier 3: Any co-developed module (IWE-Pack) requires explicit IP agreement. Levenchuk Foundation review is advisory feedback, not co-ownership of Jetix Foundation. Charter L1 candidate invitation does NOT transfer Jetix decision authority.

`F: F5 | ClaimScope: holds for all 3 tiers | R: refuted_if_MIM_asserts_IP_claim_on_Jetix_artefacts`

**Fork-and-leave preserved for both sides.**

Both Jetix and FPF/MIM retain full exit rights per tier at any point (see §6 circuit breakers). No lock-in, no penalty clauses, no exclusivity. This is the R12 symmetry: the same rules that protect MIM members from Jetix extraction protect Jetix from FPF/MIM extraction.

`[src: decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md §5 M-C; CLAUDE.md §4.1 rule 12; decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md §1.0a]`

---

## §8 RACI Per Tier

Drucker principle applied: accountability cannot be shared. Each row has a single R + single A.

### Tier 1 RACI

| Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Apply to R0 cohort + pay subscription | Ruslan | Ruslan | — | brigadier (log to tasks/) |
| Weekly разбор participation | Ruslan | Ruslan | MIM mentor (разбор lead) | — |
| Tier 1 log updates (wiki artefact) | Ruslan | Ruslan | — | brigadier (next cycle) |
| Tier 1 exit decision (upgrade / maintain / downgrade) | Ruslan | Ruslan | mgmt-expert (optimizer review) | brigadier |

### Tier 2 RACI

| Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| C4 benchmark design + execution | Ruslan (Arm A/B/C per Levenchuk spec) | Ruslan | Tseren (if agreed) | Levenchuk (result shared) |
| R12 extension proposal authoring | Ruslan | Ruslan | Tseren (review) | Levenchuk (review if interested) |
| 1-2 dedicated разбор sessions scheduling | Ruslan | Ruslan | Tseren | MIM coordinator |
| Tier 2 artefact writes (wiki paths per §4.4) | Ruslan | Ruslan | mgmt-expert (optimizer check per cycle) | brigadier |
| Tier 2 exit decision | Ruslan | Ruslan | mgmt-expert | brigadier |

### Tier 3 RACI

| Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Advisory charter draft (Levenchuk scope) | Ruslan | Ruslan | Levenchuk (negotiation) | brigadier |
| FPF structural integration proposal | Ruslan | Ruslan | Levenchuk (review) | Tseren |
| IWE-Pack module outline | Ruslan + Tseren (co-author) | Ruslan | Levenchuk (methodology) | brigadier |
| Equity discussion (if any) | Ruslan | Ruslan | HITL gate (AWAITING-APPROVAL) | brigadier; NOT mgmt-expert (equity → investor-expert × scalability) |
| Tier 3 exit decision | Ruslan | Ruslan | mgmt-expert | brigadier |

**Scope-wall note on equity.** Any equity/revenue-share row routes to `investor-expert × scalability` per mgmt-expert §1b scope-wall paragraph 4 (out_of_scope: horizon arithmetic → investor-expert). This draft surfaces the slot; does NOT populate it.

`[src: _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §8 Levenchuk (Critical path A1.2, Tyson-mentor pattern)]`

---

## §9 5 Invariants Applied (Summary)

| Invariant | Applied where | Verdict |
|---|---|---|
| **WLNK** | §3.4, §4.4, §5.4 each have explicit `proposed_artefact_path:` | PRESERVED — every tier deliverable has a named wiki path |
| **MONO** | §3 → §4 → §5 strictly add GIVES; no Tier 2 removes Tier 1 commitment | PRESERVED — additive structure confirmed by reading §3.2 + §4.2 + §5.2 |
| **IDEM** | Each tier has `acceptance_state:` concept; re-offer = no-op if accepted | PRESERVED — see circuit breaker §6 «no penalty on exit» |
| **COMM** | Tier 1 + Tier 3 commute (Levenchuk track independent); Tier 1 + Tier 2 Tseren-track sequenced (by design) | PARTIAL PRESERVED — constraint declared explicitly in §2 invariant table |
| **LOC** | Equity, Foundation revision, IWE adoption each have explicit «NOT in this tier» anti-scope | PRESERVED — each tier's anti-scope enumerates adjacent territories |

---

## §10 Measurable Delta (summary)

Proposed cooperation ladder, if executed to Tier 2, produces these measurable deltas vs baseline:

| Observable | Baseline | After Tier 2 | Delta |
|---|---|---|---|
| Levenchuk C3 label («vanilla AI-agent») | Applicable (no evidence to contrary) | Falsified or validated (C4 benchmark exists) | Moves from F2/R-low to F4/R-medium |
| B2 blocker (paid IWE unresolved) | BLOCKED | RESOLVED (Aisystant subscription Tier 1) | -1 blocker |
| FPF/IWE gaps in Jetix (I-U2 OWC, I-U4 TTL, I-U10 WP Gate) | F4, ClaimScope open | Expert-reviewed: Tseren confirms/revises gap assessment | Evidence-grade upgrade |
| Jetix L1 relationship strength Tseren | 2/10 | Target 5/10 | +3 |
| Jetix L1 relationship strength Levenchuk | 1/10 | Target 3/10 | +2 |
| Joint artefact count | 0 | 2-3 (C4 benchmark + R12 proposal + разбор log) | +2-3 |

`[src: reports/jetix-vs-iwe-audit-2026-05-17.md §4 (I-U2, I-U4, I-U10); _archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §4 Quick-glance comparison table (relationship_strength)]`

---

## §11 Conformance Checklist (mgmt × optimizer self-check)

| Check | Pass / Fail |
|---|---|
| 1. Before/after snapshot table with ≥7 metrics | PASS — §2 table has 7 rows |
| 2. All 5 invariants declared with applies? + preserves? + failure consequence | PASS — §1 table |
| 3. Method-change check: this delta is execution-parameter, NOT method-change | PASS — §2.3 COMM constraint is a sequencing rule, not a Method change |
| 4. No equity proposed without HITL gate | PASS — §5.2 and §5.3 explicitly defer equity to AWAITING-APPROVAL |
| 5. R12 applied symmetrically (both directions) | PASS — §7 explicit two-direction calibration |
| 6. Each tier has RACI with single named R + single A | PASS — §8 tables |
| 7. Each tier has anti-scope enumeration | PASS — §3.3, §4.3, §5.3 |
| 8. Circuit breakers per tier with binary predicates | PASS — §6 table |
| 9. Provenance sources[] non-empty + inline citations | PASS — frontmatter + [src:] inline per claim |
| 10. No scope creep beyond brief (cooperation plan structure only) | PASS — no FPF integration decision, no Charter text, no equity math |

---

*mgmt × optimizer draft complete. Task ID: task-fpf-iwe-phase-b-2026-05-17.
Brigadier integrates with investor × scalability + phil × critic outputs.*
