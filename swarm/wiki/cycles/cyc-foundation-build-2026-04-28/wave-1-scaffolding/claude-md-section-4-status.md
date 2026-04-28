---
title: "Wave 1 — CLAUDE.md §4 Pillar C Section Status Note"
date: 2026-04-28
type: cycle-decision-note
parent_cycle: cyc-foundation-build-2026-04-28
phase: wave-1-scaffolding-phase-b
F: F2
G: "Wave 1 status note documenting CLAUDE.md §4 deferral decision"
R: R-low
---

# §0 Mission

Document Wave 1 Phase B decision на CLAUDE.md §4 Pillar C section per recon §5.1
`unclear_claude_md_section_4` flag.

# §1 Brief intent vs current state

Brief §3.6 specified APPENDING a placeholder version of `§4 Pillar C Principles —
Boot Context` section с note «PHASE A NOTE (Wave 1): This section is PLACEHOLDER.
Tier 2 inline content populated when Wave 1.4 migration review completes per-file.
Until then, existing scattered Global Rules / Правила remain authoritative.»

Current state of CLAUDE.md (читано 2026-04-28 13:00 CET): §4 Pillar C Principles
section ALREADY EXISTS at lines ~130-180, populated с актуальным content per
Bundle 5 ack 2026-04-28 (same date as this Wave 1):

- §4.1 Tier 2 Constitutional — 11 hard rules in bullet list, citing FUNDAMENTAL §6.1 rule N
- §4.2 Tier 2 Instance-specific — 8 RUSLAN-LAYER bullet entries
- §4.3 Tier 1 Reference — pointer
- §4.4 Sync Discipline — lint check description

# §2 Decision

**No modification to CLAUDE.md performed in Wave 1 Phase B.** Rationale:

1. **Architectural change without gate.** Modifying CLAUDE.md §4 (a Foundation-level config file consumed at every Claude Code session boot) constitutes an architectural change. Per FUNDAMENTAL §6.1 rule 2 (mirrored in Pillar C `ai-does-not-execute-architectural-decision.md` + Part 6b §I.2 constitutional_never_list `ai_execute_architectural_decision`), such changes require AWAITING-APPROVAL packet via Part 6b stage_gate. Wave 1 brigadier-mechanical scaffolding does NOT carry that ack authority.

2. **Default-Deny.** Per FUNDAMENTAL §6.1 rule 11 (Pillar C `bypass-blast-radius-categorization-forbidden.md` + Part 6b constitutional_never_list `bypass_blast_radius_categorization`): when ambiguity surfaces, Default-Deny + escalate. Brief §3.6 + brief §1.1 mention APPEND but §4 already exists — ambiguity → Default-Deny.

3. **Brief §6 constraint.** Brief §6 explicit: «При неоднозначности — flag в recon.md `unclear_<area>` section, do NOT decide; Ruslan reviews.» Recon §5.1 carries the flag.

# §3 Two interpretations for Ruslan disposition

| Option | Action | Rationale |
|---|---|---|
| **A — Replace with placeholder** | Edit existing CLAUDE.md §4 → brief §3.6 placeholder text. Migration content реверсируется к scaffold-pending state. | Consistent с Wave 1 mantra «scaffolds-not-migrations». Wave 1.4 then re-populates per-file. Cost: temporary regression of currently-populated §4 to placeholder until Wave 1.4 finishes. |
| **B — Keep as-is** | No modification. Existing populated §4 satisfies brief intent (boot-context inline content available). | Bundle 5 ack already populated content на same day. Wave 1 brief written without checking that §4 was already populated. Effective intent already realised. Cost: brief §3.6 placeholder language not literally present. |

**Default proposed: Option B (keep as-is).**

Reason: existing §4 content в CLAUDE.md mirrors канонические foundation_generic
files в `principles/tier-2-system/foundation-generic/` (those just got created in
Wave 1 Phase B Pillar C batch), so the sync invariant
`/lint --check-claude-md-sync` (Phase B materialization) will work over them
correctly. Reverting to placeholder would create temporary drift that Wave 1.4
would have to undo anyway.

# §4 Ruslan ack required

Ruslan should pick A or B explicitly во время Wave 1.4 entry review. AWAITING-APPROVAL
packet at `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md` carries
this question.

# §5 Provenance

- Wave 1 brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md` §3.6 + §1.1
- Wave 1 recon: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md` §5.1 unclear flag
- CLAUDE.md re-framing decision: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`
- Bundle 5 ack: `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md`
