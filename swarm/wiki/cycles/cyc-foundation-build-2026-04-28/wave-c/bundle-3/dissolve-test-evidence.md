---
title: "OQ-MERGED-2 Dissolve-Test Evidence — Bundle 3 (Cycle 1 of 3)"
date: 2026-04-28
type: dissolve-test-evidence
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
window_position: 1-of-3
parent_policy: decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md
parent_part_5_section: swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md §X.3 + §J.4
F: F3
ClaimScope: "Bundle 3 cycle compound-phase-exclusive operations evidence accumulator entry. F-rises on Wave D ack cycle when 3-cycle window closes."
R:
  refuted_if: "Items listed below are interpreted differently than declared (e.g. owner judges that Parts 3+4 actually CAN capture them without invoking Part 5 logic — would invalidate the entry)"
  accepted_if: "At Wave D ack cycle, owner reads entries from Bundle 3 + Bundle 4 + Wave D files; counts distinct compound-phase-exclusive operations; applies threshold per parent policy"
para_tier: Area
---

# Dissolve-Test Evidence — Bundle 3 (Cycle 1 of 3)

## §1 Window position

Bundle 3 is the FIRST cycle of the OQ-MERGED-2 3-cycle dissolve-test window.

Window:
1. **Bundle 3** ← THIS FILE (Cycle 1 of 3)
2. Bundle 4 (Cycle 2 of 3) — to be written at Bundle 4 cycle
3. Wave D (Cycle 3 of 3) — to be written at Wave D ack cycle

Window closes at Wave D ack cycle. At that point, accumulator total across
3 files determines:
- ≥3 distinct compound-phase-exclusive operations = **STANDALONE PRESERVED**
- <3 = **DISSOLVE HYPOTHESIS ACTIVATES**

## §2 Cycle 1 (Bundle 3) compound-phase-exclusive operations

Per Part 5 §J.4 ritual + §X.3 starter examples + companion policy §2 scope.

### §2.1 OPERATION 1 — DRR ratio decay tombstoning policy declared

Part 5 §I.2.1 declares three Reversal Transactions pointers
(`corrects:` / `supersedes:` / `tombstones:`) for DRR entry lifecycle. The
TOMBSTONE-WHEN-RATIO.MISSES > RATIO.HITS×2 rule (Compounding-Engineering §4
P2 + Wisdom Application Loop adoption #2) is owned by Part 5 — Parts 3+4 do
NOT have per-rule decay counters. Part 3 owns wiki/methodology/ canonical
entries (post-promotion); Part 4 owns coordination cadence; neither owns
the DRR-level decay logic.

**Why exclusive to Part 5:** Parts 3+4 cannot detect rule decay without
per-rule ratio.misses tracking, which requires the DRR ledger schema
(Part 5 §I.2). Even a "compound-phase-as-cadence-step" within Part 4 would
need to invoke Part 5 §I.2 schema to do this.

✅ Counts as 1× compound-phase-exclusive operation.

### §2.2 OPERATION 2 — Cross-cycle methodology candidate emergence detection

Part 5 §I.1 + §J.2 declares the methodology promotion pipeline that detects
candidates emerging across CYCLES (≥2 distinct cycle IDs in
`validated_in_cycles[]`). Part 3 §E L9 admissibility predicate handles the
ADMISSION side (per UND-2 DRY split); Part 5 owns the EMISSION side.

**Why exclusive to Part 5:** Cross-cycle detection requires Part 5's
aggregation across multiple cycle-close events. Parts 3+4 are CYCLE-LOCAL
(Part 4 cycle-close emits packets; Part 3 admits methodology entries one at
a time). Neither has the aggregation-across-cycles primitive.

The R2 reinforcing loop counter-argument is OPERATIONALISED by this
operation: 5-10 cycle delay before compound effect detectable — the
detection requires CROSS-CYCLE state that Part 5 owns.

✅ Counts as 1× compound-phase-exclusive operation.

### §2.3 OPERATION 3 — Owner-reflection prompt generation with IP-7 separation discipline

Part 5 §I.5 reflection template + §A.2 + §E L-2 declare the IP-7 boundary:
machine-extracted summary section (filled by agents) is SEPARATED from
strategic-reflection prose section (owner-authored only; LLM does NOT
generate). This discipline is OWNED by Part 5 — Parts 3+4 can HOST the
prose (Part 3 KB layer) but cannot EMIT THE PROMPT WITH SEPARATION
DISCIPLINE.

**Why exclusive to Part 5:** Parts 3+4 do not own the boundary between
agent-extraction and owner-authorship. Part 3 admits content (regardless
of authorship); Part 4 dispatches roles (agents producing artefacts
machine-style). Without Part 5's IP-7 boundary at compound phase, the
strategic reflection prose risks LLM-generated drift (Levenchuk anti-pattern
"Если и сам текст пишет LLM — исчезает мышление письмом").

✅ Counts as 1× compound-phase-exclusive operation.

### §2.4 OPERATION 4 — Dissolve-test evidence accumulator itself (meta-operation)

Part 5 §J.4 + §X.3 declare the dissolve-test evidence accumulator ritual —
a self-monitoring mechanism for Part 5's continued existence. The
accumulator is metadata ABOUT Part 5's standalone justification; it is
authored at Part 5 §J.4 boundary; Parts 3+4 cannot generate it because
neither knows what counts as "compound-phase-exclusive."

**Why exclusive to Part 5:** This is a self-reflective Part-level operation
— Part 5 enumerates the operations only Part 5 can do. Parts 3+4 have no
need to generate this evidence (they are not on the dissolve-test bubble).

✅ Counts as 1× compound-phase-exclusive operation.

## §3 Bundle 3 cycle accumulator: 4 operations

Cycle 1 of 3 (Bundle 3) contributes **4 distinct compound-phase-exclusive
operations** to the accumulator.

If Bundles 4 + Wave D contribute zero NEW operations (only repeating these
4 same ones), the accumulator at Wave D ack cycle close is still 4 (≥3
threshold met → STANDALONE PRESERVED).

If Bundles 4 + Wave D contribute additional operations, the accumulator
exceeds 4 (also STANDALONE PRESERVED).

For DISSOLVE HYPOTHESIS to activate, owner judgment at Wave D ack cycle
must:
- Reject ≥2 of the 4 operations above as not actually compound-phase-exclusive
  (e.g., owner concludes that DRR ratio decay tombstoning could be hosted
  in Part 3 with a per-rule decay extension)
- AND find no additional compound-phase-exclusive operations in Bundles 4 +
  Wave D

That is a meaningful possibility (the DRR decay logic CAN technically live
in Part 3 if Part 3's schema extends), but the OWNER-JUDGMENT discriminator
is the canonical resolution mechanism per parent policy §2 final paragraph.

## §4 Engineering-expert dissent context

The engineering-expert dissolve dissent (preserved in
`swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` frontmatter
`dissent_preserved` block) claims "Part 5 might dissolve into Parts 3 (KB)
and 4 (coordination) without residue." The 4 operations above SUGGEST that
residue exists at Bundle 3 — DRR decay, cross-cycle aggregation, IP-7
separation discipline, dissolve-test evidence itself. These are PRELIMINARY
findings; Wave D ack cycle owner judgment is the canonical resolution.

## §5 Cross-references

- Parent policy: `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md`
- Part 5 §J.4 dissolve-test evidence ritual: `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §J.4
- Part 5 §X.3 dissolve-test condition declaration: `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §X.3
- Engineering-expert dissent: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` frontmatter `dissent_preserved` block
- Counter-argument: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 R2 reinforcing loop

---

**Bundle 3 (Cycle 1 of 3) accumulator entry committed. Awaits Bundle 4 and
Wave D contributions.**
