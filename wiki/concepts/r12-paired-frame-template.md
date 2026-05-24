---
title: "R12 Paired-Frame Template (CRITICAL F8)"
type: concept
niche: meta
agents: [influence-ethics-expert, propaganda-expert, recruitment-dynamics-expert, nlp-expert, gamification-engagement-expert]
sources:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md
  - swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md
  - swarm/wiki/foundations/principles/architecture.md
related:
  - concepts/hhh-triad-checklist.md
  - concepts/consent-boundary-protocol.md
  - concepts/mondragon-wage-ratio.md
tags: [#type/concept, #topic/r12, #topic/influence-ethics, #status/F8]
topics: [r12-enforcement, paired-frame, anti-extraction]
created: 2026-05-24
updated: 2026-05-24
confidence: high
pipeline: ingested
F: F8
G: jetix-shared
R12_paired_frame: this-IS-the-template
---

# R12 Paired-Frame Template — CRITICAL (F8)

## Суть в одной строке

Canonical 6-element annotation attached к любой influence-tactic surface для R12 enforcement (Tier 2 R12 + RUSLAN-LAYER 4 extraction action classes).

## Определение

R12 paired-frame template = mandatory annotation, прикреплённое к каждой influence-tactic surface (propaganda / recruitment / NLP / gamification). Состоит из 6 элементов:

1. **Technique description** — что именно делает приём
2. **Defensive counter** — как защититься от приёма
3. **Abuse-mode flag** — когда приём становится манипулятивным
4. **Consent precondition** — какое consent нужно для operational use
5. **Anti-extraction guarantee** — приём не используется для extraction beyond agreed share
6. **Fork-and-leave clause** (если cohort-relevant) — penalty-free exit preserved

## Authority

Этот шаблон operationalizes:
- **Tier 2 R12 LOCKED 2026-05-12** — no extraction beyond agreed share
- **RUSLAN-LAYER 4 action classes** в `.claude/config/default-deny-table.yaml`:
  - `extraction_beyond_share`
  - `wage_ratio_violation`
  - `non_consensual_distribution`
  - `fork_prevention_attempt`
- **Halt-Log-Alert F4 ≤5s** на missing pairing — emit к `swarm/approvals/log.jsonl` per Part 6b §I.2

## Применимость

- **Mandatory attachment** на каждый влияющий приём, surfaced любым из 4 agents (propaganda / recruitment / nlp / gamification)
- **influence-ethics-expert = enforcement cell** — auto-pair receiver direction
- **brigadier VETO authority** — если pairing missing, halt-log-alert + re-dispatch

## Связи

- Pair с: [[concepts/hhh-triad-checklist]] (Askell HHH alignment check)
- Pair с: [[concepts/consent-boundary-protocol]] (consent operationalization)
- Pair с: [[concepts/mondragon-wage-ratio]] (anti-extraction substrate)

## Источники

- [src: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §6.1 rule 12 + candidate]
- [src: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md LOCKED text]
- [src: swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md Option D Hybrid Ruslan ack]
- [src: swarm/wiki/foundations/principles/architecture.md Pillar C Tier 2 foundation_generic rule 12]
- [src: reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md §5.3.A23 CRITICAL F8]
