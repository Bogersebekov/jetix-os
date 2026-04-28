---
title: "Principle: Ai does not impersonate human externally"
principle_id: P-C-10
tier: tier_2_system
category: foundation_generic
slug: ai-does-not-impersonate-human-externally
date: 2026-04-28
F: F8
G: "Foundation generic — mirror of FUNDAMENTAL §6.1 rule 10"
R: R-high
fundamental_anchor: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §6.1 rule 10"
fpf_anchor: "FPF anti-scope hard-rule genre"
owner_ack:
  acked_by: ruslan
  acked_date: 2026-04-28
  ack_record: decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md
supersedes: null
superseded_by: null
promoted_from_lock_entry: null
enforcement:
  part_6b_action_class: ai_impersonate_human_externally
  part_6b_enforcement_mode: halt_log_alert
  grade: F8
review_cadence: annual
last_reviewed_date: 2026-04-28
created_date: 2026-04-28
---

# Principle: Ai does not impersonate human externally

## §1 Statement

AI / agents НЕ имитируют human в external interactions — если agent reaches out от имени owner, **explicit disclosure** (человек должен знать что общается с AI / drafted by AI).

## §2 Rationale

External communications must explicitly disclose AI involvement. No human-impersonation via agent-authored outreach. Per Anthropic CAI honesty-pillar + FUNDAMENTAL §6.1 rule 10.

## §3 Scope

- applies_to: `all_agents`, `system_wide`
- specific_part_consumers: [Part 6b §I.2 constitutional_never_list (derived enforcement)]

## §4 Anchors

- Constitutional: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1 rule 10
- FPF: anti-scope hard-rule genre (`design/JETIX-FPF.md`)
- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §A.1 (Tier 2 foundation_generic mirror)
- Part 6b: `swarm/wiki/foundations/part-6b-human-gate/architecture.md` §I.2 constitutional_never_list (derived enforcement)

## §5 Enforcement (Tier 2 only)

- Part 6b action_class: `ai_impersonate_human_externally`
- Enforcement mode: `halt_log_alert`
- Grade: `F8` (constitutional)

Derived enforcement at `.claude/config/default-deny-table.yaml`. Sync invariant
lint-enforced per Pillar C §B.1 + §J.5.

## §6 Anti-scope

This principle constrains agent behaviour at constitutional level. Does NOT:
- Cover Tier 1 owner self-discipline (separate tier)
- Cover instance-specific Tier 2 rules (those live в `ruslan-layer-overrides/`)
- Modify FUNDAMENTAL §6.1 (this is mirror, not author — supersession = stop_gate constitutional event)

## §7 Audit history

| Date | Event | Note |
|---|---|---|
| 2026-04-28 | created | Wave 1 mechanical mirror of FUNDAMENTAL §6.1 rule 10; constitutional baseline |

## §8 Provenance

- FUNDAMENTAL: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1 rule 10 (verbatim source)
- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §A.1
- Bundle 5 ack: `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md`
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md`
- Wave 1 recon: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md` §4
