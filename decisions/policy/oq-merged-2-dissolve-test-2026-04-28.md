---
title: "Policy — OQ-MERGED-2 Dissolve-Test Condition (Part 5 Standalone Preservation)"
date: 2026-04-28
type: policy
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
status: declared-Bundle-3-first-cycle-of-3-cycle-window
mirrors_section: swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md §X.3
companion_to: swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md
F: F3
ClaimScope: "Holds for the Bundle 3 + Bundle 4 + Wave D 3-cycle window. After Wave D ack cycle, this policy resolves: either Part 5 is preserved standalone (≥3 evidence) or dissolves into Parts 3+4 (<3 evidence)."
R:
  refuted_if: "Wave D ack cycle accumulator count is interpreted differently than declared here (e.g. owner accepts <3 as sufficient or rejects ≥3 as insufficient — would require explicit Ruslan ack of the policy override)"
  accepted_if: "Wave D ack cycle reads accumulator count from per-cycle dissolve-test-evidence files and applies the threshold per this policy"
applies_per_part: 5
authoritative_artefacts:
  - swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md (canonical Part 5 architecture)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md (Wave A interface card with engineering-expert dissent record)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md §4 (OQ-MERGED-2 origin)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md §2.4 (P4↔P5 R2 reinforcing loop note)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md §4 R2 reinforcing loop counter-argument
---

# Policy — OQ-MERGED-2 Dissolve-Test Condition (Part 5 Standalone Preservation)

## §1 Origin

OQ-MERGED-2 was surfaced at Wave A critic gate
(`swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md`
§4) as a CLEAN-with-dissent condition for Part 5 (Compound Learning &
Methodology Capture). Engineering-expert pre-read claimed Part 5 might
dissolve into Parts 3 (KB) and 4 (coordination) without residue. Integrator
retained Part 5 standalone per Wave A consensus, with explicit dissolve path
held open contingent on multi-cycle evidence.

Bundle 3 (Wave C, Parts 5 + 8) is the FIRST cycle of the 3-cycle dissolve-test
window. The window closes at Wave D ack cycle.

This policy file is a D25 Company-as-Code committed canonical artefact that
mirrors `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §X.3 dissolve-test condition declaration. It exists as a
standalone file so it can be referenced from `decisions/policy/`-aware skills
without needing to fetch the full architecture document.

## §2 Dissolve-Test Condition (verbatim)

> "If Bundle 3 + Bundle 4 + Wave D show <3 distinct compound-phase-exclusive
> operations (operations Parts 3+4 cannot capture without invoking Part 5
> logic), dissolve hypothesis activates and Wave D ack cycle decides whether
> Part 5 dissolves into Parts 3+4."

**Threshold (numerical):**

- ≥3 distinct compound-phase-exclusive operations across the 3-cycle window
  = STANDALONE PRESERVED.
- <3 = DISSOLVE HYPOTHESIS ACTIVATES at Wave D ack cycle.

**Scope of "compound-phase-exclusive operation":**

An operation that Parts 3+4 cannot capture without invoking Part 5 logic.
Examples (Part 5 §J.4 declaration):
- DRR ratio decay tombstoning (Parts 3+4 do not own per-rule decay counters);
- cross-cycle methodology candidate emergence (Parts 3+4 cannot detect ≥2-cycle
  validation across role boundaries without Part 5 aggregation);
- owner-reflection prompt generation IP-7-bounded (Parts 3+4 can host the
  prose but cannot emit the prompt with strategic-reflection separation
  discipline).

**The judgment of "what counts as compound-phase-exclusive" is owner-authored
at Wave D ack cycle.** The accumulator file collects candidates; the owner
adjudicates. The criteria above are starter examples; Wave D may extend or
narrow them with explicit rationale.

## §3 Engineering-Expert Dissent (preserved)

> *Engineering-expert pre-read claim:* "Part 5 might dissolve into Parts 3
> (KB) and 4 (coordination) without residue — DRR ledger belongs to KB; cycle
> ritual belongs to coordination protocol."

Reference: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` frontmatter
`dissent_preserved` block.

The dissent is NOT averaged or silenced. It is held open contingent on the
3-cycle window evidence accumulator. If Wave D ack cycle accumulator <3
distinct compound-phase-exclusive operations, the dissent is VINDICATED —
dissolve path activates.

Engineering-expert specific refuted_if / accepted_if (from the interface card
frontmatter):

- **refuted_if:** "After 3 Wave C cycles the DRR work-list is fully captured
  by Parts 3+4 with no residual compound-phase-specific artifacts"
- **accepted_if:** "Compound phase produces distinct artifact types (DRR
  entries, promoted methodology patterns) not produced by any other part;
  R2 reinforcing loop is observably distinct from R1"

## §4 Systems-Thinking-Cybernetics R2 Counter-Argument (preserved alongside)

> *Counter-argument:* "Part 5 is the R2 reinforcing loop substrate (5-10 cycle
> delay before compound effect detectable). Parts 3+4 own R1 (current-cycle
> execution). Dissolving Part 5 into Parts 3+4 collapses R1 and R2 into a
> single loop — losing the R1/R2 phase distinction. Kauffman adjacent-possible:
> Part 5 expands what FUTURE cycles can do (methodology library accumulation);
> Part 4 executes within CURRENT capability set. These are categorically
> different knowledge functions per Vincenti P7."

Reference: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 R2 reinforcing loop
counter-argument.

This counter-argument is preserved BESIDE the engineering-expert dissent — both
are inputs to Wave D ack judgment; neither pre-resolves the test condition.

## §5 Bundle 3 = First Cycle of 3-Cycle Window

Bundle 3 is the FIRST cycle of the dissolve-test window. The window closes at
Wave D ack cycle. The accumulator is per-cycle:

| Cycle | Accumulator file | Status |
|---|---|---|
| Bundle 3 (cyc-foundation-build-2026-04-28 Wave C) | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/dissolve-test-evidence.md` | Bundle 3 ack — accumulator written by Part 5 §J.4 |
| Bundle 4 (cyc-foundation-build-2026-04-28 Wave C continuation OR next cycle) | TBD per Bundle 4 cycle structure | Awaits Bundle 4 |
| Wave D (final ack cycle) | TBD per Wave D cycle structure | Awaits Wave D |

Total accumulator across 3 cycles: SUM of distinct compound-phase-exclusive
operations from each.

## §6 Standalone Preservation Threshold

≥3 distinct compound-phase-exclusive operations across Bundle 3 + Bundle 4 +
Wave D = Part 5 STANDS as canonical Foundation Part. Architecture document at
`swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` remains canonical with `pipeline: ready`. F-G-R for Part 5 architecture
holds at F5 (or higher per accumulated cross-cycle reuse evidence).

## §7 Dissolve Path (if threshold not met)

If Wave D ack cycle accumulator count <3 distinct compound-phase-exclusive
operations:

1. **Wave D ack packet redirects compound-phase ownership.** Ack packet
   includes explicit `dissolve_path_activated: true` field with rationale
   citing accumulator count.

2. **Engineering-expert dissolve hypothesis re-evaluated.** Owner reviews the
   dissent (§3) + counter-argument (§4) + accumulator evidence (§5). Owner
   judgment.

3. **If owner accepts dissolve, bundle redesign initiated BEFORE Wave D Part 5
   cycle runs:**
   - DRR ledger schema migrates to Part 3 §I.X (new sub-section under
     methodology library — DRR-as-pre-methodology-history).
   - Compound-phase ritual cadence migrates to Part 4 §J.X (new sub-section
     under coordination protocol — compound-phase as cadence step).
   - All historical strategies.md entries preserved (no deletion); migration
     commit `[strategy] migrate: legacy DRR entries to Part 3 methodology
     history (Wave D dissolve)` per IP-3 + Reversal Transactions discipline.
   - OQ-MERGED-2 closes.
   - Part 5 architecture document moves to
     `swarm/wiki/foundations/_archived/part-5-compound-learning-methodology-capture/architecture.md` with `pipeline: archived` frontmatter.
   - `wiki/index.md` updated.
   - `swarm/approvals/log.jsonl` entry recording the dissolve event with
     timestamp, actor (Wave D ack cycle owner), F-fall to F-archived.

4. **If owner rejects dissolve despite <3 accumulator** (owner judgment that
   the test threshold itself was wrong): explicit Ruslan ack of policy
   override required; this policy file gets a `superseded_by:` pointer to a
   NEW policy entry recording the override rationale.

## §8 Reversibility (Corrigibility)

This policy is reversible. Per Bundle 1 Part 6b §E Law L9 (Corrigibility,
Askell HHH Appendix E.2 verbatim), Ruslan can:
- Override the threshold (≥3 vs <3) at any time via NEW policy commit
- Revert dissolve activation via `git revert` of the dissolve commit
- Manually adjudicate accumulator count interpretation
- Decide that "compound-phase-exclusive" judgment differs from §2 starter
  examples

The policy is FORK-PORTABLE: Phase B partner forks adopt the dissolve-test
mechanism (3-cycle window threshold) but apply their own accumulator count
and own judgment.

## §9 Cross-references

- Canonical declaration in Part 5 architecture: `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` §X.3
- Origin: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md` §4 OQ-MERGED-2
- Engineering-expert dissent: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` frontmatter `dissent_preserved` block
- Counter-argument: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` §4 R2 reinforcing loop
- Accumulator: `swarm/wiki/cycles/<cycle-id>/bundle-3-dissolve-test-evidence.md` (per cycle)
- Bundle 3 ack: `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-28.md` (this Bundle's packet)

---

**Status:** declared-Bundle-3-first-cycle-of-3-cycle-window. F3 (proposed
dissolve-test condition; not validated until Wave D evidence accumulates) →
F4 on Bundle 3 owner ack of test condition itself.
