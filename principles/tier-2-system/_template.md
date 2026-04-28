---
title: "Principle: <slug-readable>"
principle_id: P-<C|S>-<NN>
tier: tier_2_system
category: foundation_generic | ruslan_layer_overrides
slug: <kebab-slug>
date: <YYYY-MM-DD>
F: F4 | F5 | F8
G: "<group-scope description>"
R: R-medium | R-medium-high | R-high
fundamental_anchor: <required for foundation_generic; refs FUNDAMENTAL §6.1 rule N>
fpf_anchor: <optional>
owner_ack:
  acked_by: ruslan
  acked_date: <YYYY-MM-DD>
supersedes: <prior-path-or-null>
superseded_by: <path-or-null>
promoted_from_lock_entry: <path-or-null>
enforcement:
  part_6b_action_class: <e.g., ai_strategize_or_set_direction>
  part_6b_enforcement_mode: halt_log_alert | advisory | default_deny
  grade: F4 | F5 | F8
review_cadence: quarterly | annual
last_reviewed_date: <YYYY-MM-DD>
created_date: <YYYY-MM-DD>
---

# Principle: <Title>

## §1 Statement
<concise declarative statement>

## §2 Rationale
<why; what it prevents / enables>

## §3 Scope
<applies_to: all_agents | system_wide | specific_role_archetypes | specific_part_consumers>

## §4 Anchors
- Constitutional: <FUNDAMENTAL § ref>
- FPF: <FPF § ref>
- Wave B framework: <consultant card refs>
- Lock Entry origin: <if promoted from Lock Entry>

## §5 Enforcement
- Part 6b action_class: <ref>
- Mode: <halt_log_alert | advisory | default_deny>
- Grade: <F4 / F5 / F8>

## §6 Anti-scope
<what this does NOT cover>

## §7 Audit history

| Date | Event | Note |
|---|---|---|
| <YYYY-MM-DD> | created | <note> |

## §8 Provenance
- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md`
- Template: `principles/tier-2-system/_template.md`
