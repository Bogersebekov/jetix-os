---
title: Cross-fork audit trail — Phase B architecture deferral
date: 2026-04-28
type: policy
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
status: deferred-phase-b
ack_record: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
authority: Ruslan ack OQ-B1-8 (2026-04-28)
F: F5
ClaimScope: "Holds for Jetix Foundation Phase A. The deferred-Phase-B label is itself constitutional — declares the gap exists rather than silently inheriting ambiguity."
R:
  refuted_if: "A Phase B partner-import scenario surfaces in Phase A that requires synthetic Phase B fixture before partner integration begins"
  accepted_if: "Phase B partner-integration architecture work begins by extending this policy with concrete fixture + reconciliation strategy"
sources:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md §I.1 cross-fork-provenance.json
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md §L P1.1
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/M3-walkthroughs.md Scenario 4
  - decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md §5 OQ-B1-5 + OQ-B1-8
---

# Cross-fork audit trail — Phase B architecture deferral

> **Per Ruslan ack OQ-B1-8 (2026-04-28).** This policy file declares the explicit deferral of cross-fork audit trail materialisation to Phase B. The schema design is complete (Part 1 §I.1); the synthetic Phase B partner test fixture and concrete reconciliation strategies for approval-log merge across forks are deferred.

## What is deferred

1. **Synthetic Phase B partner test fixture.** P1.1 acceptance predicate ("Schema validates against fork-import test fixture") requires a concrete synthetic partner case. Bundle 1 designs the schema fields; Bundle 4 (Part 10 external touchpoints) authors the fixture once partner candidates are identified.

2. **`approvals_reconciliation_strategy` field promotion.** Per OQ-B1-5, this field currently lives in `metadata` open field of `cross-fork-provenance.json`. Phase B work promotes it to top-level with explicit Phase B reconciliation strategies enumerated.

3. **Merge-superset / fork-isolated / merge-conflict-escalate strategies.** Concrete reconciliation algorithms for when partner approval logs are imported back into Jetix. Phase B work — premature for Phase A single-owner scope.

## What is NOT deferred (already in Bundle 1)

- `cross-fork-provenance.json` schema with ≥4 named cross-fork fields (parent_repo_id, parent_commit_hash, fork_id, fork_branch, divergence_point, reconciliation_strategy, audit_trail_continuation, F-G-R-on-imported-claims, IP-1-role-binding-overrides, metadata)
- IP-1 compliance via `role_archetype` Foundation field; executor IDs tagged RUSLAN-LAYER
- M3 Scenario 4 fork-separation walkthrough (Phase B partner imports Foundation generics; replaces RUSLAN-LAYER bindings) — full trace in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/M3-walkthroughs.md`
- Part 6a + Part 6b architecture documents both have explicit §X Foundation vs RUSLAN-LAYER sections covering fork-separation discipline

## Trigger to lift the deferral

Lift the deferred-phase-b label when ANY of the following becomes true:
1. A concrete partner-fork candidate is identified (DACH partner organization, alumni-instance, hypothetical research partner)
2. Phase B engineering backlog opens with capacity for Part 10 external-touchpoints work
3. A Phase A scenario surfaces that requires cross-fork audit reconciliation before Phase B (e.g., research collaboration with shared knowledge base)

When triggered: update this policy file's `status:` from `deferred-phase-b` → `active-phase-b`, author the synthetic fixture, promote `approvals_reconciliation_strategy` to top-level, commit per D25 with `[architecture] Phase B — cross-fork audit reconciliation activated`.

## §X Foundation vs RUSLAN-LAYER

This deferral policy is GENERIC Foundation discipline — the pattern of "declare deferral explicitly rather than silently inherit ambiguity" is a constitutional commitment. Specific deferred items are RUSLAN-LAYER instance-bindings (Jetix mono-repo / DACH ICP context). A Phase B partner inheriting Foundation creates their own `cross-fork-audit-deferred-phase-b.md` with their fork-specific deferred items.
