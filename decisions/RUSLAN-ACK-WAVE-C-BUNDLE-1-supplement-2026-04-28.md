---
title: RUSLAN-ACK Wave C Bundle 1 — Retroactive Supplement (OQ-B2-A applied)
date: 2026-04-28
type: ruslan-ack-supplement
parent_record: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
parent_packet: decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md
applied_at_cycle: cyc-foundation-build-2026-04-28
applied_at_bundle: 3 (cycle start, Phase 0)
trigger: OQ-B2-A from Bundle 2 ack record (decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md §2)
status: applied
---

# RUSLAN-ACK Wave C Bundle 1 — Retroactive Supplement

## §1 Purpose

This supplement records the three retroactive corrections to Bundle 1 Foundation
artefacts triggered by OQ-B2-A (raised at Bundle 2 ack 2026-04-28). The corrections
were applied at Bundle 3 cycle start (Phase 0) per the Bundle 3 deep-prompt §4.0
BLOCKING gate before substantive Part 5 / Part 8 dispatch.

The parent ack record (`decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`)
remains canonical for the Bundle 1 acknowledgement. This supplement extends it
with the retroactive corrections; it does not supersede the parent record.

## §2 Retroactive corrections applied

### §2.1 Part 1 §I.4 stub `gate_class` enum aligned to Part 6b §I.4 F8 LOCKED

**Before:** `enum: ["autonomous", "requires-approval", "hitl-required"]` (stale,
pre-Bundle-1 nomenclature predating the F8 locked gate-class taxonomy).

**After:** `enum: ["stop_gate", "stage_gate", "draft_promotion"]` (Part 6b §I.4
F8 LOCKED awaiting-approval-packet.json `gate_class` enum — single source of
truth canonicalised in Bundle 1).

Rationale: Bundle 1 §I.4 of Part 1 declared a STUB schema for the
task-return-packet that included a `gate_class` field; the stub used a
pre-canonical enum. Bundle 1 Part 6b §I.4 then locked the gate-class taxonomy at
F8 with a different enum vocabulary. Bundle 2 review surfaced the divergence as
OQ-B2-A. Resolution: align the stub to the F8 LOCKED Part 6b enum verbatim;
field description cross-references Part 6b §I.4 as canonical authority.

Edit location: `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`
§I.4 `task-return-packet.json` stub.

### §2.2 Part 1 §I.2 commit-format-tokens.json — `swarm-lib`, `health`, `methodology` tokens added

**Before:** RUSLAN-LAYER token list did not include `swarm-lib`, `health`,
`methodology`. Bundle 2 commits used `[swarm-lib]` informally despite the token
not being in the authoritative list (lint signal would have flagged).

**After:** `swarm-lib` token added (canonicalises Bundle 2 C1 Joint Design accessor
pipeline area — `swarm/lib/` houses accessor skills + routing-table.yaml +
executor-binding.yaml under Part 3 LEAD + Part 4 ADVISORY governance).
Additionally, `health` token added (Part 8 Bundle 3 health snapshot commits) and
`methodology` token added (Part 5 Bundle 3 methodology promotion commits) — these
are forward-looking additions for Bundle 3 substantive work, anticipated by
OQ-B2-D Bundle 2 ack canonicalisation discipline.

Rationale: per OQ-B2-D ack: tokens informally used must be canonicalised. The
authoritative list at §I.2 is the single source of truth for the pre-commit
hook + `/lint --check-commit-format`; deferring canonicalisation creates lint
false-positives when Bundle 3 ships.

Edit location: `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`
§I.2 RUSLAN-LAYER token list block.

### §2.3 Part 1 §K K18 — Legacy v1.0.0 message upcasting failure mode added

**Before:** No failure mode covering pre-cutover message schema v1.0.0 ingestion.

**After:** New failure mode entry K18 — Legacy v1.0.0 message upcasting. Detects
`schema_version: "1.0.0"` on ingest; attempts upcast to v2.0.0 (Bundle 2 LOCKED
schema with `acting_as:` mandatory); rejects with named-field error if upcast
cannot be inferred from `from:` field. Append `upcast_provenance:` annotation on
successful upcast. NO silent acceptance.

Rationale: per Bundle 2 Decision #6 (message schema v2.0.0 BREAKING change), Part 1
commit substrate may receive legacy messages in operational use (reprocessing
archived packets, replaying pre-cutover mailbox contents). Without explicit
upcasting policy, silent malformed acceptance corrupts the audit trail (Young 2010
§4 P4 event-versioning principle). K18 closes the gap.

**Numbering note:** the OQ-B2-A spec (2026-04-28) named this failure mode "K15"
but pre-existing K15/K16/K17 entries already occupied those slots (concurrent
commit `.git/index.lock` / disk-full / cross-fork token drift). To preserve
numbering uniqueness while honouring spec substantive content verbatim, the new
failure mode is filed at K18. The substantive content (legacy v1.0.0 upcasting
policy + named-field error reject + `upcast_provenance:` annotation) matches the
spec exactly.

Edit location: `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`
§K Failure Modes (between K17 and K14 — K14 is at end as PHASE-B-DEFERRED).

## §3 Single commit landed

Commit message:

```
[architecture] Bundle 1 retroactive supplement — Part 1 §I.4 gate_class enum + commit-format-tokens.json [swarm-lib] token + K18 upcasting (per OQ-B2-A + OQ-B2-D RUSLAN-ACK Bundle 2)
```

Branch: `claude/jolly-margulis-915d34`.

## §4 Constitutional consequences

- Bundle 1 §I.4 stub now constitutionally aligned with Part 6b F8 LOCKED gate-class
  taxonomy. Bundle 3 Part 5 methodology promotion (`gate_class: draft_promotion`)
  + Part 8 Tier 0 health-integrity events (`gate_class: stop_gate`) consume the
  enum verbatim with no further re-litigation.
- Commit-format-tokens.json now canonical for `swarm-lib` (Bundle 2 accessor area),
  `health` (Bundle 3 Part 8 area), `methodology` (Bundle 3 Part 5 area).
  Pre-commit hook + `/lint --check-commit-format` accept these as valid `[area]`
  prefixes from this commit forward.
- K18 closes the message schema v1.0.0 → v2.0.0 cutover policy gap. Operational
  ingest of pre-cutover messages now has a declared failure-mode policy with a
  Hamel-binary acceptance predicate.

## §5 OQ-B2-A status

Status: **CLOSED — applied at Bundle 3 cycle start (Phase 0) before substantive
Part 5 / Part 8 dispatch.**

## §6 No re-ack required

These corrections are "fix-the-stub" supplements within the F-G-R contract
already acked at Bundle 1 (F8 schemas are immutable; F5 stub schemas can be
extended with corrections-as-new-entries per Reversal Transactions discipline).
The Bundle 1 F-G-R promotions in the parent ack record (§3 of
`RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`) remain in effect.

Bundle 3 substantive work proceeds with these corrections as F4 stable inputs.
