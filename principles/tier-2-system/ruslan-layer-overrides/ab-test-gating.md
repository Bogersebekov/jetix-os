---
title: "Principle: A B test gating (SCAFFOLD-PENDING-REVIEW)"
principle_id: P-S-04
tier: tier_2_system
category: ruslan_layer_overrides
slug: ab-test-gating
date: 2026-04-28
status: scaffold-pending-review
F: F2
G: "scaffold awaiting Ruslan-driven migration review"
R: R-low
candidate_source:
  path: "CLAUDE.md"
  line_range: "162 (also legacy marker line 191)"
  extracted_2026-04-28: |
    **A/B tests: ALWAYS awaiting_approval, never auto-deploy** — was Global Rule 10
review_status: pending-wave-1.4
created_date: 2026-04-28
---

<!-- WAVE-1-SCAFFOLD: Ruslan reviews this artefact in Wave 1.4 migration step.
DO NOT auto-promote to F4. DO NOT activate referenced enforcement until Ruslan ack.

Candidate source: CLAUDE.md line 162 (also legacy marker line 191)

CANDIDATE TEXT (verbatim from source, awaiting review):

**A/B tests: ALWAYS awaiting_approval, never auto-deploy** — was Global Rule 10

Review actions available in Wave 1.4:
- PROMOTE-AS-IS: minor frontmatter cleanup, content unchanged → F4
- REFACTOR: rewrite §1 statement to fit principle-doc style; preserve intent → F4
- SPLIT: candidate covers multiple principles; split into N files → drafts F2
- MERGE: candidate duplicates another principle → archive this; supersede the other
- ARCHIVE-WITHOUT-MIGRATION: not principle-grade; remove from Pillar C target
- ESCALATE: needs Ruslan clarification before action
-->

# Principle: A B test gating

## §1 Statement

<!-- empty pending Wave 1.4 review; do not author here -->

## §2 Rationale

<!-- empty pending Wave 1.4 review -->

## §3 Scope

- applies_to: `system_wide`  # default; review at Wave 1.4
- specific_part_consumers: []  # populate at review

## §4 Anchors

- Constitutional: <as applicable>
- Lock Entry origin: <as applicable>
- Wave B framework: <as applicable>

## §5 Enforcement (Tier 2 only)

<!-- empty pending Wave 1.4; mode/grade depend on principle severity classification -->

## §6 Anti-scope

<!-- empty pending Wave 1.4 -->

## §7 Audit history

| Date | Event | Note |
|---|---|---|
| 2026-04-28 | scaffolded | Wave 1 mechanical scaffold; pending Ruslan migration review |

## §8 Provenance

- Bundle 5 Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md`
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md`
- CLAUDE.md re-framing decision: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`
- Wave 1 recon: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md` §3
- Original location: CLAUDE.md line 162 (also legacy marker line 191)
