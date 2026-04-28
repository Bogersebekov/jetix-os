---
title: "RUSLAN-ACK Wave C Bundle 1 supplement 2 — cross-fork-provenance.json approvals_reconciliation_strategy field promotion top-level (per OQ-B1-5)"
date: 2026-04-28
type: ruslan-ack-supplement
parent_ack: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
parent_ack_supplement_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
triggered_by: Bundle 4 Part 10 §I.1 + AWAITING-APPROVAL Bundle 4
status: awaiting-ruslan-ack-with-bundle-4
F: F4
ClaimScope: "Holds for Part 1 §I.1 cross-fork-provenance.json schema. Promotes approvals_reconciliation_strategy from metadata open field to top-level required field with 5 declared enum strategies. END-OF-CYCLE single-commit retroactive correction analogous to OQ-B2-A pattern (inverted timing: substantive Bundle 4 work establishes promotion need; supplement record commits at cycle end after all 3 architecture documents land + AWAITING-APPROVAL packet drafted)."
R:
  refuted_if: "Bundle 4 Part 10 §I.1 references the 5 strategies but Part 1 §I.1 does not contain the top-level field; OR partner-fork-import scenario fails because cross-fork-provenance.json schema rejects approvals_reconciliation_strategy population at top-level"
  accepted_if: "Part 1 §I.1 schema includes approvals_reconciliation_strategy as top-level required enum field; Part 10 §I.1 references resolve cleanly; cross-fork-provenance.json fork import scenario validates"
sources:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§I.1)
  - swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md (§I.1 + §J.6)
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md (OQ-B1-5)
---

# RUSLAN-ACK Wave C Bundle 1 supplement 2

> **Constitutional supplement record.** Bundle 4 Part 10 §I.1 declared 5
> reconciliation strategies (parent-wins / fork-wins / manual-merge /
> decline-import / pending-review). This requires that
> `approvals_reconciliation_strategy` be a TOP-LEVEL field in Part 1 §I.1
> `cross-fork-provenance.json` schema, not buried in the `metadata` open
> field. This file documents the retroactive correction to Bundle 1.
>
> Analogous to OQ-B2-A pattern (Bundle 1 retroactive supplement 1, committed
> 2026-04-28 hash `ca38be3`), but **inverted timing**: substantive Bundle 4
> work (Part 10 §I.1 declaring 5 strategies operationally) established the
> promotion need; supplement record commits at end of Bundle 4 cycle (Phase
> H per deep prompt §4.5) AFTER all 3 architecture documents land + Bundle 4
> AWAITING-APPROVAL packet drafted.

## §1 Retroactive correction per OQ-B1-5 (applied 2026-04-28 at Bundle 4 cycle end)

### §1.1 Schema field promoted

- **From**: `metadata.approvals_reconciliation_strategy` (open extension
  field per Bundle 1 §I.1 v1.0.0; Ashby variety-gap compliance)
- **To**: `approvals_reconciliation_strategy` (top-level required field per
  Bundle 4 supplement 2 v1.1.0)

### §1.2 5 reconciliation strategies declared

| Strategy | Semantic | Used for |
|---|---|---|
| `parent-wins` | Foundation parent ack supersedes fork's local ack | Foundation invariants (privacy + corrigibility + Halt-Log-Alert ordering + 5 reconciliation strategies enum) |
| `fork-wins` | Fork's local ack supersedes Foundation parent | RUSLAN-LAYER ICP-specific values when partner has different ICP |
| `manual-merge` | HITL Ruslan + partner pair-resolve via AWAITING-APPROVAL `gate_class: stage_gate` | Cross-cutting changes affecting both Foundation + RUSLAN-LAYER |
| `decline-import` | Fork explicitly declines Foundation's ack | Foundation patterns inappropriate for fork's domain |
| `pending-review` | Fork holds ack for next sync window | Default state pre-resolution |

### §1.3 Schema version bump

Part 1 §I.1 cross-fork-provenance.json schema version: `1.0.0 → 1.1.0`.

`schema_version_history` block entry added:

```yaml
- version: "1.1.0"
  effective_from: "2026-04-28"
  changelog: "Bundle 4 retroactive supplement 2 — approvals_reconciliation_strategy promoted from metadata open field to top-level required field with 5 declared strategies. Per OQ-B1-5 RUSLAN-ACK Bundle 1 + Bundle 4 §I.1 operational declaration."
  notes: "Records prior to v1.1.0 with approvals_reconciliation_strategy in metadata.* are upcast on next read per K18 upcasting policy. Cross-reference Part 10 §I.1."
  breaking: false
  supersedes: "v1.0.0 metadata.approvals_reconciliation_strategy field"
```

K18 upcasting policy (Bundle 1 supplement 1) ensures backward compatibility:
records prior to v1.1.0 with `approvals_reconciliation_strategy` in
`metadata.*` are upcast to top-level on next read.

### §1.4 Cross-references

- Bundle 4 Part 10 §I.1 (operational declaration; consumer side).
- Bundle 4 Part 10 §J.6 (Phase B partner fork import ritual exercises 5
  strategies).
- Bundle 4 Part 10 §X.3 (F.9 Bridge requirement section references reconciliation
  application per scenario).
- Bundle 4 M3 Walkthroughs Scenario 4 (fork-separation Phase B import — exercises
  all 5 strategies via alex-dach-consulting fork).
- Bundle 1 §I.1 Part 1 schema declaration (now updated v1.0.0 → v1.1.0).
- Bundle 1 RUSLAN-ACK Decision #6 Corrigibility (preserved by privacy +
  reconciliation invariants — `parent-wins` for these).

### §1.5 Constitutional implication

This is a NON-BREAKING schema evolution per `breaking: false` flag. Existing
Phase A use of cross-fork-provenance.json (which has 0 partner-fork imports
since Phase A is single-owner — no actual records exist yet) is unaffected.
Phase B partner-fork imports use v1.1.0+ schema with top-level field.

The promotion is FOUNDATION-LEVEL declarative. Reconciliation actions remain
PHASE B work (no Phase A reconciliation events since Phase A is single-owner
with no partner fork).

## §2 Commit details

- **Commit message**: `[architecture] Bundle 1 retroactive supplement 2 —
  cross-fork-provenance.json approvals_reconciliation_strategy field
  promotion top-level (per OQ-B1-5 RUSLAN-ACK Bundle 1)`
- **Commit hash**: TBD (committed at Phase H end-of-cycle).
- **Branch**: `claude/jolly-margulis-915d34`.
- **Files modified**: `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (§I.1 schema declaration).
- **Files created**: `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md` (this file).

## §3 Ack request

Ruslan acks Bundle 4 AWAITING-APPROVAL packet at
`decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-28.md` confirming
this supplement is accepted as constitutional correction.

After Ruslan ack:
- This file's `status: awaiting-ruslan-ack-with-bundle-4` updates to
  `status: ruslan-acked-canonical`.
- Part 1 §I.1 schema v1.1.0 becomes F8 LOCKED.
- Bundle 4 Wave C closure achieved → Wave D integration pass dispatch
  (separate cycle).
