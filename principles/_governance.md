---
title: "Principles Governance — Foundation generic"
date: 2026-04-28
type: principles-governance
F: F5
G: "Foundation generic governance per Pillar C §I.4 (Bundle 5 LOCKED)"
R: R-high
owner_ack:
  acked_by: ruslan
  acked_date: 2026-04-28
  ack_record: decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md
created_date: 2026-04-28
---

# Principles Governance

> **Source.** Verbatim copy of `swarm/wiki/foundations/principles/architecture.md` §I.4
> Foundation generic governance discipline. Pillar C F5 LOCKED 2026-04-28.

## §1 Authoring authority

- **Tier 1 + Tier 2 ruslan_layer_overrides:** owner-authored only per FUNDAMENTAL §6.2
- **Tier 2 foundation_generic:** mirrors FUNDAMENTAL §6.1; no direct authoring (revised via stop_gate flow)

## §2 Supersession discipline

- Append-only via `supersedes:` refs (per Young Reversal Transactions)
- **Tier 1 + Tier 2 ruslan_layer_overrides:** stage_gate (per Part 6b)
- **Tier 2 foundation_generic:** stop_gate (constitutional event — de facto FUNDAMENTAL §6.1 revision)

## §3 Audit cadence

- **Tier 1:** monthly review (Part 9 surface)
- **Tier 2 ruslan_layer_overrides:** quarterly review (Pillar A Strategic Reflection cadence)
- **Tier 2 foundation_generic:** annual constitutional review

## §4 Sync invariants

- Pillar C Tier 2 foundation_generic ↔ Part 6b `.claude/config/default-deny-table.yaml` constitutional_never_list (count + hash match — lint enforced)
- Pillar C Tier 2 ↔ CLAUDE.md §4 inline (hash match — lint enforced)
- Lint failure = fail-loud per FUNDAMENTAL §5.5

## §5 Lock-to-principle promotion

- Pillar A Lock Entry promotion → Pillar C `principle-candidate` event (per Part 11 §C.2)
- Owner reviews tier categorization (Tier 1 / Tier 2 foundation_generic / Tier 2 ruslan_layer_overrides / Lock-only)
- Authored as principle file with `promoted_from_lock_entry:` ref
- Tier 2 foundation_generic promotion = constitutional event (stop_gate + simultaneous FUNDAMENTAL §6.1 revision flow)

## §6 Provenance

- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §I.4
- Bundle 5 ack: `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md`
- CLAUDE.md re-framing: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`
