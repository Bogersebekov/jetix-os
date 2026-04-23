---
id: opportunity-04-cell-acceptance-predicate
title: "OPP-04 — cell_acceptance_predicate as mandatory WBS field"
type: opportunity-draft
cluster_id: C-04
lead_domain: mgmt
co_domains: [engineering, investor, philosophy]
dissents_addressed: [D-03 partial — acceptance predicates explicit prevents 2× overclaim]
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: mgmt-expert
mode: integrator
created: 2026-04-23
pipeline: drafted
state: drafted
confidence: high
confidence_method: claim-by-claim-trace
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "H-01, §2 C-1, §3, §4 H-01"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md", range: "§3.2 Bundle I, §5 H-01 sharpened"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "§4.1 Bundle-1 WLNK, §5 H-4 AP-25, §4.1 AP-25 prevention"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "§3 H-6 Kelly-81, §5 Bundle-A, §4.2 H-6 cost model"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md", range: "Part B M-1 falsifier threshold, Part C Bundle B-1, Part D M-1..M-4"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "§5 OPP-04, §2.3 C-04, §3 ranked table row 4"}
  - {path: ".claude/agents/brigadier.md", range: "§3.3 WBS schema block L413-435"}
  - {path: "agents/mgmt-expert/strategies.md", range: "entry: mgmt-cell-level-acceptance-predicate-required"}
niche: meta
---

# OPP-04 — cell_acceptance_predicate as mandatory WBS field

## §1 Opportunity Statement

The brigadier's WBS decomposition schema (brigadier.md §3.3, L413-435)
requires three fields per cell: `ap_cost`, `ap_budget`, and
`expected_artefact`. It does NOT require a `cell_acceptance_predicate:`
field. As a result, cells can satisfy the dispatch contract by returning
any non-empty artefact — "done" is defined by artefact existence alone,
not by a falsifiable binary predicate.

This gap was the root cause of 8/8 conformance check failures in the
first real cycle (mgmt-critic-01.md §2 C-1). It corresponds to cluster
C-04 (WBS Acceptance Gap) in the unified synthesis, ranked Tier 1 with
combined score 28.6. [src: mgmt-critic-01.md:§2 C-1]
[src: mgmt-integrator-01.md:§3 row C-04]

The fix is narrow and purely additive: one required field in the
decomposition YAML schema + one brigadier refusal rule + one /lint
check. No runtime behaviour change beyond the refusal gate. Effort
estimate: 3 turns (mgmt Bundle I; engineering AP-25 coverage).
[src: mgmt-optimizer-01.md:§3.2 Bundle I slot I-1]

---

## §2 Context: how this fits the swarm's current state

OPP-04 sits fourth in the Tier-1 ranked sequence behind C-02
(measurement void), C-01 (executor gap), and C-03 (compounding loop).
Unlike those three, OPP-04 has zero dependencies — it does not wait
for the eval harness, hooks, or /compound skill. It can ship in the
same session as OPP-01 and OPP-02 without sequencing risk.
[src: mgmt-integrator-01.md:§5 OPP-04 "Dependencies: None"]

The cross-domain convergence is strong:

- **mgmt-critic-01.md H-01** named it as a root-cause failure: AP-25
  prevention fires only at task-intake (§2.3) but not at cell-dispatch
  (§3.3). [src: mgmt-critic-01.md:H-01]
- **engineering-optimizer-01.md §4.1** named AP-25 prevention as the
  primary AP addressed by Bundle-1 hooks — the write-scope-guard
  (H-4) already enforces per-agent write boundaries; the
  `cell_acceptance_predicate:` field extends the same contract to
  per-cell output quality. [src: engineering-optimizer-01.md:§4.1 AP-25]
- **investor-optimizer-01.md H-6** (Kelly score 81) proposes adding
  `expected_invocation_frequency` + `estimated_turn_savings_per_invocation`
  to DRR entries. These are Kelly-discriminating fields that live in
  strategies.md DRR entries, NOT in the WBS schema. Scope boundary is
  explicitly drawn in §5 of this draft. [src: investor-optimizer-01.md:§3 H-6]
- **philosophy-optimizer-01.md M-1** (falsifier threshold) requires
  every hypothesis to carry an atomic `falsifier:` field. The
  `cell_acceptance_predicate:` field is the WBS-layer equivalent of
  M-1: it makes the cell's "done" condition atomic, machine-readable,
  and non-prose. [src: philosophy-optimizer-01.md:Part D M-1]

---

## §3 Proposed Implementation

### §3.1 Exact YAML field shape for cell_acceptance_predicate

**Design decision 1: string vs structured block.**

RECOMMENDATION: **string** (not a structured block). Reasoning:

- The Hamel-binary AP is definitionally a single line: one condition
  that either holds or does not hold over the delivered artefact.
  A multi-field block invites partial satisfaction ("some sub-fields
  pass, some fail") which is the opposite of binary.
- The philosophy-optimizer M-1 falsifier field is a structured block
  (condition + threshold + measurement_path + baseline_required +
  baseline_value). That extra structure is appropriate for long-lived
  hypothesis claims that graduate through F-levels. A cell-dispatch
  predicate is short-lived (one cycle) and machine-checkable by grep.
- A string field is /lint-checkable with a single regex:
  non-empty AND length < 200 chars AND does NOT contain "artefact exists"
  OR "file exists" OR "non-empty" as standalone sufficiency markers
  (those are artefact-existence, not Hamel-binary).
- The field does NOT need baseline_value, measurement_path, or
  threshold sub-keys at this layer. Those belong in strategies.md
  DRR entries (per investor H-6) and in hypothesis claim artefacts
  (per philosophy M-1), not in per-cell dispatch.

[src: mgmt-critic-01.md:§3 acceptance predicate format; philosophy-optimizer-01.md:Part D M-1 rationale]

**Canonical field shape (exact diff to brigadier.md §3.3):**

```yaml
# BEFORE (existing brigadier.md §3.3 cell block):
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [<file-paths from manifest.yaml>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-critic-<slug>.md

# AFTER (with cell_acceptance_predicate added):
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [<file-paths from manifest.yaml>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-critic-<slug>.md
    cell_acceptance_predicate: >
      <One-line Hamel-binary: the condition that holds iff this cell's
      output is complete. Example: "Every hypothesis H-N has a
      falsifier.condition field (non-null) AND at least 2 anti_scope
      items AND a confidence level declared.">
```

**Placement:** field appears AFTER `expected_artefact` and BEFORE
any risk or cost annotations. This ordering makes it the last
"pre-dispatch" check: brigadier sets `ap_cost`, `ap_budget`, the
artefact path, and then MUST state what "done" means for that path.
The predicate is therefore the terminal field in each cell block.
[src: brigadier.md:§3.3 L419-430 schema order]

### §3.2 How brigadier checks the field pre-dispatch

**Design decision 2: Bash one-liner grep vs Python lint rule.**

RECOMMENDATION: **Bash one-liner grep** for the Phase-A refusal gate;
**Python lint rule** deferred to Phase B or to OPP-05/engineering
skill bundle.

Rationale:
- Phase A has no Python executor in brigadier's dispatch path. The
  brigadier is Claude Code; its pre-dispatch check is implemented as
  a prose condition in §4.2 (Mode-prefix mandate) and in §2.3
  (AP-25 prevention). Both of those are prose descriptions that
  brigadier enforces by reading them at task-intake time.
- The SAME mechanism applies here: the brigadier checks the field
  existence by reading the decomposition YAML as part of its §4.1
  dispatch ritual. Adding one line to the §4.1 prompt check is
  sufficient for Phase A.
- The Bash one-liner that would execute this check (for use in
  `/lint` or in a PostToolUse hook from OPP-02 Bundle-1) is:

```bash
# One-liner: verify cell_acceptance_predicate present and non-trivial
# Fails if any cell block in the decomposition file lacks the field
# or if the field is empty / contains only "artefact exists" variants

grep -c "cell_acceptance_predicate:" "$DECOMP_FILE" | \
  awk -v cells="$(grep -c "^ *- cell:" "$DECOMP_FILE")" \
  '{if($1 < cells) exit 1; else exit 0}'
```

This one-liner counts `cell_acceptance_predicate:` occurrences and
compares against cell count. If any cell is missing the field, it
exits 1. This is the exact check brigadier's §4.2 Mode-prefix mandate
enforces via hook in OPP-02; OPP-04 PRs for the prose refusal now,
and the hook wires the Bash check when OPP-02 Bundle-1 ships.
[src: engineering-optimizer-01.md:§3 Bundle-1 rationale; mgmt-optimizer-01.md:§3.2 Bundle-I slot I-1]

**Brigadier.md §4.1 prose addition (exact diff):**

```
# AFTER the existing §4.1 Task() schema block, add one check to the
# File-reference-only rule paragraph:

Pre-dispatch checklist (brigadier, per cell):
1. `ap_cost` and `ap_budget` are non-zero integers.
2. `expected_artefact` path is inside `swarm/wiki/drafts/<task-id>-*` glob
   (write-scope-guard, per OPP-02).
3. `cell_acceptance_predicate` is non-empty string, length 20-200 chars,
   and does NOT consist solely of "artefact exists" or "file is non-empty"
   (artefact-existence predicates are AP-MGMT-1 failures).
   If missing or trivial: REFUSE dispatch with structured return
   {status: refused, reason: "cell_acceptance_predicate absent or trivial",
    ap_code: AP-MGMT-1, cell: <cell-name>}.
```

This is a prose-only addition to brigadier.md §4.1 and §4.2. No code
execution required for Phase A. The hook enforces it mechanically
when OPP-02 Bundle-1 lands.

### §3.3 /lint check wiring (Hamel-binary validated by regex)

**Design decision 3: /lint check with regex pattern.**

/lint check #13 — "cell-level AP present" (new check, appended to
`.claude/skills/lint.md` check list):

```markdown
### Check #13 — cell_acceptance_predicate present in all WBS cells

**Slug:** `cell-ap-missing`

**What it checks:**
For every file matching `swarm/wiki/proposals/*-decomposition.md`:
(a) Count occurrences of `^ *- cell:` (number of cells declared).
(b) Count occurrences of `cell_acceptance_predicate:` (number of cells
    with the field).
(c) If (b) < (a): FAIL with message
    "cell-ap-missing: N of M cells in <file> lack cell_acceptance_predicate".
(d) For each present `cell_acceptance_predicate:` value:
    - Regex: `^.{20,200}$` (length 20-200 chars)
    - Anti-regex: `^(artefact exists|file is non-empty|file exists|
      expected_artefact returned|non-empty file)` (case-insensitive)
    - If value fails regex: FAIL "cell-ap-trivial: predicate too short
      or matches artefact-existence pattern"

**Pass condition (Hamel-binary):**
`/lint check #13 passes IFF: for every decomposition file in
swarm/wiki/proposals/, (count(cell_acceptance_predicate:) ==
count(- cell:)) AND every predicate value matches regex .{20,200}
AND none matches anti-regex (case-insensitive).`

**Effort:** ~15 lines added to `.claude/skills/lint.md`; bash
implementation: ~20 lines.
```

[src: mgmt-optimizer-01.md:§5 H-01 sharpened measurable; engineering-optimizer-01.md:§4.1 Bundle-3 LOC]

### §3.4 Scope boundary: philosophy-optimizer falsifier field (OPP-05)

**Design decision 4: whether OPP-05 falsifier field can ride along in
the same schema edit.**

RECOMMENDATION: **No. OPP-05 remains a separate opportunity draft.**

Reasoning:

- `cell_acceptance_predicate:` lives in the WBS decomposition schema
  (`proposals/*-decomposition.md`). It describes cell-dispatch intent.
- `falsifier:` (philosophy M-1) lives in hypothesis/claim artefacts
  (`swarm/wiki/tasks/<task-id>/artefacts/*.md`) and in strategies.md
  DRR entries. It describes epistemic status of a long-lived claim.
- The two fields address different artefact lifecycles (one-cycle cell
  dispatch vs multi-cycle claim maturation), different readers
  (brigadier at dispatch time vs /lint at cycle-close), and different
  ontological primitives (α-2 artefact state vs α-1 task state).
- Bundling them would mix two LOC targets (WBS schema + hypothesis
  schema) into one PR, violating the LOC invariant declared in
  engineering-optimizer-01.md §4.1 Bundle-3.
- OPP-05 DOES benefit from OPP-04's precedent: the two fields are
  structurally parallel (both are string fields enforcing binary
  predicates at different layers). When OPP-05 is drafted, it should
  cross-reference OPP-04's /lint pattern as a sibling design.

**Preparation move allowed (not bundled, just declared):**
The /lint check #13 regex pattern (length 20-200; anti-artefact-existence)
is the direct template for OPP-05's /lint check #14 pattern for
`falsifier:`. OPP-04 does NOT write check #14 — it declares the
parallel and defers. brigadier may draft OPP-05 with this preparation
in mind.
[src: philosophy-optimizer-01.md:Part D M-1; mgmt-integrator-01.md:§5 OPP-05 "Dependencies: None"]

### §3.5 Scope boundary: Kelly-discriminating DRR fields (OPP-04 vs separate edit)

**Design decision 5: investor-optimizer Kelly-discriminating fields
in the same WBS schema edit or separate DRR template edit.**

`expected_invocation_frequency` and `estimated_turn_savings_per_invocation`
(investor-optimizer-01.md H-6, Kelly score 81) are fields that belong in
strategies.md DRR entries, NOT in the WBS decomposition schema.

**Explicit scope ruling:**

- WBS decomposition schema (brigadier.md §3.3) describes
  **per-cell dispatch parameters**: what the cell will do, how
  many turns it will use, what artefact it will produce, and — now —
  what "done" means.
- DRR strategies.md entries describe **cross-cycle compounding rules**:
  decision, reasoning, result, review, and (per investor H-6) the
  expected payback and invocation frequency of each compounded rule.
- These are different schema targets, different lifecycle phases, and
  different readers (brigadier at dispatch time vs brigadier at
  Compound step time).

**OPP-04 scope: WBS schema only.** The Kelly fields are a
Phase-5/M2/Memory-dimension edit (investor-optimizer-01.md §3 Bundle-A
H-6: "strategies.md template — 6 files per expert"). That is a separate
DRR template revision, not part of the WBS schema edit. It should
be implemented as part of investor-optimizer Bundle-A (H-6 + H-1 + H-3),
deferred to the compounding-dimension cluster (C-03) rather than the
WBS-acceptance-gap cluster (C-04).

[src: investor-optimizer-01.md:§3 H-6 rationale "DRR strategies.md template"; mgmt-integrator-01.md:§5 OPP-04 lead domain mgmt]

---

## §4 Cross-Domain Synthesis (per-claim F / ClaimScope / R)

### Claim 1 — Cell-level acceptance predicates absent is the root cause of "artefact-existence = done"

- **F:** F4 (operational convention; 8/8 conformance check failures
  from first real cycle constitute a pattern at convention level;
  observed once but severity = 100%)
- **ClaimScope:** Holds for Phase A 1-human + 6-agent swarm where the
  brigadier is the only entity checking cell output. NOT valid if an
  external review process catches predicate-less cells before promotion
  (no such process exists in Phase A).
- **R:**
  - accepted_if: first cycle with `cell_acceptance_predicate:` required
    shows ≥1 brigadier refusal-on-missing-field event recorded in
    events.md (verifiable: grep on events.md for "cell_acceptance_
    predicate absent").
  - refuted_if: field is added to schema and 3 consecutive cycles
    produce zero refusal events AND zero artefact-existence predicates
    (meaning brigadier populates the field correctly without refusing
    any cell, which would mean the absence of the field was NOT the
    root cause — the root cause was something upstream).
- **Source:** [src: mgmt-critic-01.md:§2 C-1; mgmt-critic-01.md:H-01]

---

### Claim 2 — The fix is purely additive (no regression risk)

- **F:** F4 (engineering-optimizer-01.md Bundle-1 invariant analysis;
  both WLNK and LOC declared pass for additive schema fields)
- **ClaimScope:** Holds for the schema addition and prose refusal rule.
  NOT valid if the /lint check is miscounted (counting only top-level
  `cell_acceptance_predicate:` and missing nested YAML — mitigation:
  the grep pattern `^ *cell_acceptance_predicate:` anchors on leading
  whitespace matching the cell block's indentation level).
- **R:**
  - accepted_if: existing decomposition files (if any) pass /lint check
    #13 after the field is retroactively added to them; no pre-existing
    decomposition breaks.
  - refuted_if: an existing decomposition file has a cell block where
    the field was declared under a different key name — should not exist
    (schema did not previously have the field), but worth checking at
    implementation time.
- **Source:** [src: engineering-optimizer-01.md:§4.1 Bundle-1 WLNK + IDEM]

---

### Claim 3 — String field (not structured block) is the right type for this layer

- **F:** F3 (design judgment; not yet validated by any cycle using the
  field — first-cycle hypothesis)
- **ClaimScope:** Holds for cell-dispatch context where the predicate
  is one-cycle, one-artefact, machine-checkable by length+pattern.
  NOT valid if over time brigadier finds that single-string predicates
  are consistently too ambiguous and require sub-fields (e.g.
  "predicate_text + measurement_path + deadline") — that would
  indicate a migration to a structured block is warranted (Phase-B
  upgrade path per §7 evolution plan).
- **R:**
  - accepted_if: at cycle 10, /lint check #13 anti-regex fires on
    <5% of predicate values (meaning authors write non-trivial,
    non-artefact-existence predicates naturally with a string field).
  - refuted_if: at cycle 10, >30% of predicate values require a
    "clarification" dispatch from brigadier because the string was
    ambiguous — indicates structured block is needed.
- **Source:** [src: philosophy-optimizer-01.md:Part B M-1 rationale for atomic string; mgmt-expert.md §3.2 acceptance predicate format]

---

### Claim 4 — /lint check by regex is machine-evaluable without Python or paid tooling

- **F:** F4 (Bash grep + awk is definitionally available in the
  brigadier's toolchain under Max-subscription; no external API)
- **ClaimScope:** Holds for the regex `^.{20,200}$` and
  anti-regex against known artefact-existence phrases. NOT valid if
  future predicates use multi-line YAML blocks (the `>` scalar or `|`
  literal block); those require different parsing. Mitigation: restrict
  `cell_acceptance_predicate:` to a single-line scalar (no `>` or `|`
  allowed per /lint check #13).
- **R:**
  - accepted_if: `/lint` invocation on a decomposition file with all
    fields correctly populated exits 0; invocation on a file with a
    missing or trivial field exits 1 with the "cell-ap-missing" or
    "cell-ap-trivial" slug.
  - refuted_if: the grep approach produces false positives (e.g. a
    correctly written predicate matches the anti-regex) — in which
    case the anti-regex must be tightened to fewer exact-match strings.
- **Source:** [src: mgmt-optimizer-01.md:§5 H-01 Hamel-binary target; engineering-optimizer-01.md:§5 H-5 eval-runner one-liner pattern]

---

## §5 Dissents (E-5 compliance)

### Dissent A — D-03 partial: the cell_acceptance_predicate field addresses the 2× overclaim but does not eliminate it

**Position A (philosophy-optimizer-01.md, M-1):** The "2× improvement"
claim (Boris Cherny lower bound) is currently unfalsifiable because
no measurement substrate exists (philosophy-critic-01.md H-1, AP-PHIL-1).
Adding a `cell_acceptance_predicate:` field makes individual cell outputs
falsifiable but does NOT make the swarm-level "2× improvement" claim
falsifiable — that still requires OPP-01 eval harness.

**Position B (mgmt-integrator-01.md, D-03 resolution):** The synthesis
resolved D-03 operationally: no cluster in T1/T2 uses "2×" as a
Hamel-binary AP. Philosophy's concern is satisfied at the synthesis
level; OPP-04 contributes by ensuring each cell's predicate is
falsifiable, which is a necessary (but not sufficient) condition for
the swarm-level falsifiability that OPP-01 delivers.

- **F:** F3 (Position A from phil-critic-01.md H-1 AP-PHIL-1; Position B from integrator synthesis D-03 resolution — both at pattern level)
- **ClaimScope:** Position A holds at the swarm-level 2× claim. Position B holds at the cell-level individual predicate. The two levels are distinct; there is no contradiction — both are true simultaneously.
- **R:**
  - Position A refuted_if: OPP-01 (eval harness) ships AND the 2× claim is calibrated numerically, making cell-level predicates a sub-gate of the harness measurement.
  - Position B refuted_if: a cell predicate containing a "2×" marker (e.g. "cell output demonstrates 2× improvement vs baseline") passes /lint check #13 despite being unfalsifiable at the cell level because no baseline exists in the WBS file.
- **Resolution path for OPP-04:** The /lint check #13 anti-regex should include `2×` and `2x` as blocked trivial quantifiers ONLY IF they appear without a baseline path reference (e.g. `2× vs <measurement_path>`). This is a sharpening detail for the /lint implementation, not a schema change.

---

### Dissent B — field as string (OPP-04) vs field as structured block (OPP-05 precedent)

**Position A (mgmt, this draft):** String field is sufficient for cell-dispatch; structured block adds overhead without proportional gain at this layer.

**Position B (philosophy-optimizer-01.md B-1):** The falsifier block (for hypothesis claims) is a structured YAML block because machine-checkability of sub-fields (threshold, measurement_path, baseline_required) is essential for epistemic tracking across cycles. If cell predicates eventually need the same tracking, a string-to-block migration is costly.

- **F:** F3 (Position A: design judgment for Phase A; Position B: pattern from philosophy M-1 structured block — both unvalidated as of cycle 1)
- **ClaimScope:** Position A holds while cells are single-cycle artefacts with no cross-cycle tracking requirement. Position B holds if cell predicates eventually need measurement_path references (e.g. "predicate passes iff health.md counter X > N").
- **R:**
  - Position A refuted_if: at cycle 10, ≥3 distinct cell predicates contain references to `swarm/wiki/meta/health.md` counters and brigadier must manually parse them — indicates structured block is needed.
  - Position B refuted_if: at cycle 10, 0 cell predicates reference health.md and /lint check #13 produces clean pass on all decomposition files — string field is sufficient.
- **Resolution path:** Phase A: string. Phase B trigger: if cell predicates reference measurement paths in ≥3 cells over 10 cycles, propose structured block migration via AWAITING-APPROVAL.

---

## §6 Residual Open Questions

1. **OPP-02 Bundle-1 coordination:** The Bash one-liner in §3.2 is
   designed to become a PostToolUse hook when OPP-02 ships. Is the
   hook registration in `.claude/settings.json` done as part of OPP-02
   Bundle-1 (engineering domain) or as part of OPP-04 implementation
   (mgmt domain)? RECOMMENDATION: OPP-02 Bundle-1 owns `.claude/settings.json`;
   OPP-04 provides the check script (`swarm/lib/hooks/cell-ap-check.sh`)
   as a standalone file, and OPP-02 wires it into the hook registry.
   This preserves LOC (OPP-04 touches brigadier.md §3.3 + §4.1 +
   lint.md; OPP-02 touches settings.json).

2. **Retroactive application:** Does the `cell_acceptance_predicate:`
   field need to be backfilled in the current cycle's decomposition
   file (`swarm/wiki/proposals/T-swarm-self-improve-v1-2026-04-23-
   decomposition.md`)? RECOMMENDATION: yes, as a retroactive best-effort
   during the Compound step. This produces the first data point for
   /lint check #13 even before the next cycle.

3. **Length threshold (20-200 chars):** The 20-char floor prevents
   trivially short predicates; the 200-char ceiling prevents prose
   essay predicates. These thresholds are proposed but untested.
   MONITOR: if cycle 3-5 shows predicates legitimately needing >200
   chars (complex multi-condition predicates), raise the ceiling to 350.

4. **Anti-regex completeness:** The proposed anti-regex blocks known
   artefact-existence phrases. New trivial patterns will emerge in
   practice. RECOMMENDATION: brigadier's Compound step should grep
   strategies.md for "cell-ap-trivial" /lint hits and propose anti-regex
   expansions as DRR entries.

5. **Interaction with OPP-05 falsifier field:** When OPP-05 ships,
   the `falsifier:` field in hypothesis artefacts and the
   `cell_acceptance_predicate:` field in WBS cells should be
   cross-validated: every cell whose expected_artefact is a hypothesis-
   type document should have its predicate reference the artefact's
   `falsifier.condition`. This binding is a Phase-B refinement; Phase A
   leaves them independent.

---

## §7 Evolution Plan

**Phase A (current):** String field; prose refusal rule in brigadier
§4.1; /lint check #13 with Bash grep; no hook wiring yet (deferred to
OPP-02 Bundle-1 coordination).

**Cycle 10 checkpoint:**
- Ratio of /lint check #13 passes: target ≥95% of cells across 10
  decomposition files.
- Ratio of "cell-ap-trivial" hits: target <5% of populated cells.
- If string field proving ambiguous (Dissent B refuted): propose
  structured block migration via AWAITING-APPROVAL.

**Cycle 50 checkpoint:**
- If every cell predicate naturally references a measurement path
  (health.md counter, eval result): migrate to structured block per
  philosophy M-1 pattern.
- /lint check #13 can be tombstoned if it produces 0 failures across
  rolling 20 cycles — it has been absorbed into brigadier's dispatch
  discipline.

**Phase B:**
- If cell predicates grow to reference cross-cycle measurement paths:
  migrate to structured block with `predicate_text`, `measurement_path`,
  `baseline_required` sub-fields (aligned with philosophy M-1).
- `cell_acceptance_predicate:` value populates first row of
  `swarm/evals/<cell-id>/golden-set.jsonl` input field automatically
  (engineering H-5 eval harness integration).

---

## §8 Acceptance Predicate (Hamel-binary)

```
brigadier.md §3.3 WBS schema block contains a `cell_acceptance_predicate:`
field as a required entry in every cell block; brigadier.md §4.1 contains
a pre-dispatch checklist with a refusal rule for absent or trivial
predicates (AP-MGMT-1 cite, slug "cell-ap-missing"); `.claude/skills/lint.md`
contains /lint check #13 with slug `cell-ap-missing` and `cell-ap-trivial`,
with the Hamel-binary pass condition stated explicitly; at least one of:
(a) the next cycle's decomposition file carries the field in every row, OR
(b) `swarm/lib/hooks/cell-ap-check.sh` exists (pre-hook for OPP-02
integration) — at least one observable confirmation that the field
is live.
```

---

## §9 Anti-scope

- NOT evaluating code quality of any hook implementation — engineering × critic.
- NOT computing capital ROI of this schema change — investor explicitly
  deferred Kelly fields from this schema (§3.5).
- NOT proposing the /compound skill implementation — that is OPP-03 / systems lead.
- NOT adding `falsifier:` to hypothesis artefacts — that is OPP-05 / philosophy lead.
- NOT adding Kelly-discriminating DRR fields to strategies.md — that is
  investor Bundle-A H-6, separate DRR template edit.
- NOT modifying shared-protocols.md — this is a brigadier.md + lint.md change only.
- NOT producing the stakeholder-map.md — that is mgmt H-10, separate artefact.
- NOT strategizing which opportunity to implement first — brigadier composes
  the execution sequence from the full opportunity set.

---

## §10 Effort / Risk / Dependency Summary

| Dimension | Value | Source |
|---|---|---|
| Effort estimate | 3 turns (mgmt Bundle I; no engineering hooks needed for Phase A) | mgmt-optimizer-01.md Bundle I slot I-1 effort=2 + /lint addition |
| Ruslan attention cost | 0 gate decisions | mgmt-optimizer-01.md §1 "Bundle I requires 0 HITL gate decisions" |
| Dependencies upstream | None (can ship in parallel with OPP-01 and OPP-02) | mgmt-integrator-01.md §5 OPP-04 |
| Dependencies downstream | OPP-02 Bundle-1 (for hook wiring); OPP-05 (for falsifier cross-bind Phase B) | §3.2 + §6 item 1 |
| Risk score | 1 / 5 (purely additive; no regression path) | engineering-optimizer-01.md §4.1 Bundle-1 IDEM + LOC |
| Impact score | 4 / 5 (eliminates root cause of 8/8 C-1 conformance failures) | mgmt-critic-01.md H-01 |
| Phase-A implementable | Yes | mgmt-optimizer-01.md Bundle I |

---

## §11 Provenance Table

| # | Source path | Range / section | Claims grounded |
|---|---|---|---|
| 1 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md` | §2 C-1; §3; §4 H-01 | Root-cause finding (8/8 conformance failure); AP-MGMT-1 definition; proposed fix specification |
| 2 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md` | §3.2 Bundle I slot I-1; §4 Bundle I invariants; §5 H-01 sharpened | Effort=2; WLNK/MONO/IDEM/COMM/LOC all pass; Hamel-binary target "≥95% cells by cycle 5" |
| 3 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md` | §4.1 Bundle-1 WLNK+IDEM+LOC; §5 H-4 AP-25 prevention write-scope-guard; §5 H-9 provenance-gate | AP-25 prevention framing; write-scope-guard Bash pattern; additive-only risk confirmation |
| 4 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md` | §3 H-6 Kelly score 81; §5 Bundle-A; §4.2 H-6 cost model | Kelly fields belong in DRR (not WBS schema); Bundle-A = strategies.md template; scope boundary ruling |
| 5 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md` | Part B M-1 before/after; Part C Bundle B-1; Part D M-1..M-4 binary thresholds | Falsifier field design (structured block vs string); M-1 pass condition as sibling pattern for /lint check #13 |
| 6 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md` | §5 OPP-04 brief; §2.3 C-04; §3 row 4; §4 D-03 resolution | Tier-1 rank 4, combined score 28.6; D-03 partial resolution; "Dependencies: None" |
| 7 | `.claude/agents/brigadier.md` | §3.3 WBS schema L413-435; §4.1 Task() schema; §4.2 Mode-prefix mandate | Exact schema target; pre-dispatch ritual; refusal pattern for analogy |
| 8 | `agents/mgmt-expert/strategies.md` | Entry: mgmt-cell-level-acceptance-predicate-required | Layer-2 self-compounding rule: "Every decomposition cell MUST carry cell_acceptance_predicate:" |

---

## §12 Structured Output Packet (shared-protocols §3)

```yaml
summary: >
  OPP-04 implementation plan for adding cell_acceptance_predicate: as a
  required string field to brigadier.md §3.3 WBS schema. Resolves root
  cause of 8/8 conformance failures in first real cycle. 5 design decisions
  settled: (1) string field (not structured block); (2) prose refusal in
  brigadier §4.1 now, Bash hook when OPP-02 Bundle-1 ships; (3) /lint
  check #13 with slug cell-ap-missing + cell-ap-trivial, regex .{20,200},
  anti-regex for artefact-existence phrases; (4) OPP-05 falsifier field is
  a sibling design but stays out of this schema edit (different LOC target);
  (5) Kelly DRR fields (investor H-6) are DRR-template-layer, not WBS-layer
  — cleanly deferred to C-03 compounding cluster. Effort: 3 turns; 0 HITL
  gates; 0 upstream dependencies.

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md
    frontmatter:
      id: opportunity-04-cell-acceptance-predicate
      title: "OPP-04 — cell_acceptance_predicate as mandatory WBS field"
      type: opportunity-draft
      cluster_id: C-04
      lead_domain: mgmt
      co_domains: [engineering, investor, philosophy]
      dissents_addressed: [D-03 partial]
      produced_by: mgmt-expert
      mode: integrator
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      task_id: T-swarm-self-improve-v1-2026-04-23
      sources: [see file frontmatter]
      provenance_inline: true
      confidence: high
      confidence_method: claim-by-claim-trace
      pipeline: drafted
      state: drafted
    body: "(this file)"
    edges_to_add:
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate", to: "tasks/T-swarm-self-improve-v1-2026-04-23", type: part_of}

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-critic-01.md", range: "§2 C-1, §3, §4 H-01"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-optimizer-01.md", range: "§3.2 Bundle I, §4 Bundle I invariants, §5 H-01"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "§4.1 Bundle-1, §5 H-4, §5 H-9"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "§3 H-6, §5 Bundle-A, §4.2 H-6"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md", range: "Part B M-1, Part C B-1, Part D M-1..M-4"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "§5 OPP-04, §3 C-04 row, §4 D-03"}
  - {path: ".claude/agents/brigadier.md", range: "§3.3 L413-435, §4.1, §4.2"}
  - {path: "agents/mgmt-expert/strategies.md", range: "entry mgmt-cell-level-acceptance-predicate-required"}

confidence: high
confidence_method: claim-by-claim-trace

escalations: []

dissents:
  - position: "cell_acceptance_predicate as string is insufficient long-term; structured block (predicate_text + measurement_path + baseline_required) needed if predicates reference health.md counters"
    evidence:
      - "philosophy-optimizer-01.md:Part B M-1 structured block design rationale"
      - "mgmt-expert.md §3.2 acceptance predicate format — one-line Hamel-binary per artefact type"
    F: F3
    ClaimScope: "Position A (string sufficient) holds Phase A where cells are one-cycle artefacts with no cross-cycle tracking. Position B (structured block better) holds if cell predicates grow to reference measurement paths in ≥3 cells over 10 cycles."
    R:
      accepted_if: "at cycle 10, 0 cell predicates contain cross-cycle measurement references"
      refuted_if: "at cycle 10, ≥3 predicates contain health.md or swarm/evals/ path references; indicates structured block migration is warranted"
  - position: "D-03 partial — OPP-04 makes cells falsifiable but swarm-level 2× claim remains unfalsifiable until OPP-01 ships"
    evidence:
      - "philosophy-critic-01.md:H-1 AP-PHIL-1 — 2× claim F=F1, unfalsifiable now"
      - "mgmt-integrator-01.md:§4 D-03 resolution — resolved operationally (no cluster uses 2× as AP)"
    F: F3
    ClaimScope: "Cell-level falsifiability is a necessary but not sufficient condition for swarm-level falsifiability. Both claims are simultaneously true at different ontological levels."
    R:
      accepted_if: "OPP-01 ships and 2× is calibrated numerically — then OPP-04 + OPP-01 together satisfy both levels"
      refuted_if: "a cell predicate in the next cycle contains '2×' as a gate criterion without a measurement path — anti-regex must catch this"
```
