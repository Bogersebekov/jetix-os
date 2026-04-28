---
title: "Lock D-28 — Query-driven KB filtering (SCAFFOLD-PENDING-REVIEW)"
type: lock-entry
version: 1.0
status: scaffold-pending-review
cadence: append-only
owner: ruslan-plus-agent
audience: internal
F: F2
G: "scaffold awaiting Ruslan-driven migration review"
R: R-low
last_updated: 2026-04-28
lock_id: D-28
slug: query-driven-kb-filtering
candidate_source:
  path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md"
  section: "§D28"
review_status: pending-wave-1.4
created_date: 2026-04-28
references:
  foundation_parts:
    - Part 6b governance gate
    - Part 1 system state persistence
    - Part 8 health monitor
    - Part 11 strategic direction substrate
  fpf_anchors:
    - "FPF B.3 trust calculus"
    - "FPF IP-3 artifacts-over-conversations"
  parent_strategic_docs:
    - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
related_locks: []  # populate at Wave 1.4
---

<!-- WAVE-1-SCAFFOLD: Ruslan reviews this Lock in Wave 1.4 migration step.
DO NOT promote to F4 until ack.

Source: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28
Extracted candidate (verbatim from source / synthesized from recon):

Pool first, BUT pool-filling driven by anticipated queries, query second. `/ingest --anchor=<…>` mandatory; KB filling not greedy accumulation but query-driven curation.

Migration actions available in Wave 1.4:
- PROMOTE-AS-IS: copy candidate to §1-§7; minor cleanup → F4
- REFACTOR: reorganize candidate to fit 7-section discipline → F4
- SPLIT: candidate is multi-Lock; split into D-28-a, D-28-b → scaffold
- ARCHIVE: not actually a Lock (might be Direction, Insight, or operational note)
- SUPERSEDE-WITH-NEW: write new Lock; mark this superseded
- ESCALATE: needs clarification
-->

# Lock D-28 — Query-driven KB filtering

## §1 What is locked

<!-- empty pending Wave 1.4 review -->

## §2 Why this is irreversible

<!-- empty pending Wave 1.4 -->

## §3 Scope of what this Lock covers

<!-- empty pending -->

## §4 Downstream artifacts depending on this Lock

<!-- empty pending -->

## §5 Reversal predicate

<!-- empty pending -->

## §6 Anti-scope

<!-- empty pending -->

## §7 Provenance + sources

- Bundle 5 Pillar A architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md`
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md`
- Original location: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28
- Wave 1 recon: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md` §1
- Scaffolded: 2026-04-28
