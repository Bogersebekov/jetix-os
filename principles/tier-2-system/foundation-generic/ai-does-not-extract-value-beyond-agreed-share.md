---
title: "Principle: Ai does not extract value beyond agreed share"
principle_id: P-C-12
tier: tier_2_system
category: foundation_generic
slug: ai-does-not-extract-value-beyond-agreed-share
date: 2026-05-12
F: F8
G: "Foundation generic — extension of FUNDAMENTAL §6.1 (additive; pending FUNDAMENTAL §6.1 rule 12 update)"
R: R-high
fundamental_anchor: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §6.1 candidate rule 12 (additive — packet-acked 2026-05-12)"
fpf_anchor: "FPF anti-scope hard-rule genre"
owner_ack:
  acked_by: ruslan
  acked_date: 2026-05-12
  ack_record: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md
  parent_decision: reports/strategic-decisions-2026-05-12.md §2 (Q2 ack)
  parent_insight: decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
supersedes: null
superseded_by: null
promoted_from_lock_entry: null
enforcement:
  part_6b_action_class: ai_extract_value_beyond_agreed_share
  part_6b_enforcement_mode: halt_log_alert
  grade: F8
review_cadence: annual
last_reviewed_date: 2026-05-12
created_date: 2026-05-12
---

# Principle: Ai does not extract value beyond agreed share

## §1 Statement

AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.

**Russian (boot context):** AI / substrate не может извлекать ценность из участников сверх согласованной доли; участники могут отделиться и уйти без штрафа.

## §2 Rationale

R12 = constitutional codification of **anti-extraction principle** (M-C cheating-defense mechanism из Game Theory research §11). Three specific guarantees:

1. **No extraction beyond agreed share** — revenue / equity / data / attention / reputation all bounded by explicit agreement; substrate cannot unilaterally widen extraction surface.
2. **Fork-and-leave right** — members keep data + reputation + contacts + artifacts at exit; no exit penalty; mutual no-poach norm preserved.
3. **Constitutional barrier** — future extraction-creep requires explicit amendment via Part 6b stage_gate (not slippery slope; not retrofit).

Three reasons elevated NOW (preemptive), не later:

- **Defender's advantage** — built-in с L1 = constitutional anchor present at first signature; retrofit после L2 expansion = high capture risk
- **Trust signal для L1 First Clan signatories** — 9 confirmed members read Charter pre-signature; R12 = binding guarantee Jetix won't become "golden handcuffs"
- **Defense against founder-capture** — Ruslan included; R12 makes post-hoc extraction by founder structurally forbidden (corrigibility extension к substrate property)

Symmetric с H7 People-NS L0-L6 ladder — preserves cooperation substrate at all scales (L1 9 members → L6 10M+).
Tier 1 priority constitutional move per Game Theory §12.2 — «самый высокий-leverage» constitutional anchor.

## §3 Scope

- applies_to: `all_agents`, `system_wide`, `substrate_itself`
- specific_part_consumers: [Part 6b §I.2 constitutional_never_list (derived enforcement)]

## §4 Anchors

- Constitutional: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1 candidate rule 12 (additive — FUNDAMENTAL §6.1 update follows post-ack)
- FPF: anti-scope hard-rule genre (`design/JETIX-FPF.md`)
- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §A.1 (Tier 2 foundation_generic mirror)
- Part 6b: `swarm/wiki/foundations/part-6b-human-gate/architecture.md` §I.2 constitutional_never_list (derived enforcement)
- Parent insight: `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` §5 M-C mechanism (commit `93b796d` LOCKED)
- Parent research: `reports/jetix-game-theory-cheating-research-2026-05-12.md` §11 (anti-cheat M-C defense) + `reports/jetix-people-network-state-research-2026-05-11.md` §12.5 (original R12 proposal)
- Parent decision: `reports/strategic-decisions-2026-05-12.md` §2 (Q2 ack NOW preemptive)
- AWAITING-APPROVAL packet: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` (stage_gate ack-record)

## §5 Enforcement (Tier 2 only)

- Part 6b action_class: `ai_extract_value_beyond_agreed_share`
- Enforcement mode: `halt_log_alert`
- Grade: `F8` (constitutional)

Derived enforcement at `.claude/config/default-deny-table.yaml`. Sync invariant
lint-enforced per Pillar C §B.1 + §J.5.

## §6 Anti-scope

This principle constrains agent / substrate behaviour at constitutional level. Does NOT:
- Cover Tier 1 owner self-discipline (separate tier)
- Cover instance-specific Tier 2 rules (those live в `ruslan-layer-overrides/`)
- Modify FUNDAMENTAL §6.1 directly (additive extension — FUNDAMENTAL §6.1 rule 12 update follows post-ack как separate packet)
- Prohibit explicit owner-acked extraction agreements (constraint = beyond agreed share, не absolute zero)
- Constrain Tier 1 manager judgement re fair-share negotiation (owner-domain)

## §7 Audit history

| Date | Event | Note |
|---|---|---|
| 2026-05-12 | created | R12 elevation via Part 6b stage_gate ack (packet `r12-anti-extraction-2026-05-12.md`); parent insight H7 People-NS LOCKED commit `93b796d`; Q2 ack 2026-05-12 NOW preemptive per `reports/strategic-decisions-2026-05-12.md` §2 |

## §8 Provenance

- Parent insight: `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` §5 M-C (verbatim source for R12 text)
- Parent research (game-theoretic): `reports/jetix-game-theory-cheating-research-2026-05-12.md` §11 (M-C anti-cheat defense) + §12.5 (Tier 1 priority elevation argument)
- Parent research (network-state): `reports/jetix-people-network-state-research-2026-05-11.md` §12.5 (original R12 proposal)
- Parent decision: `reports/strategic-decisions-2026-05-12.md` §2 (Q2 ack NOW preemptive, F5 blast-radius via Part 6b stage_gate)
- AWAITING-APPROVAL packet: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` (Ruslan ack 2026-05-12 chat-approve-execute Option A)
- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §A.1 (Tier 2 foundation_generic structural placement)
- Bundle 5 ack baseline: `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` (Tier 2 11-rule baseline preserved + extension pattern established)
