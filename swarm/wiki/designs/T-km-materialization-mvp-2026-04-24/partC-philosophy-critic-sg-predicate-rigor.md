---
title: "Part C — Philosophy × Critic: SG predicate rigor gate (Hamel-binary discipline)"
type: critic-audit-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: philosophy-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: critic
wave: 1
part: C
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: popper-refutability-plus-hamel-binary-canonical
tier: core
promotion_note: |
  Wave-1 critic audit promoted 2026-04-24. All 14 FAIL findings + 1 peer-input-needed
  (CC-10 DSL coverage gap for Popperian refutation) + 1 architectural-fix (CC-14
  product releases/validation circular dependency) + 1 DSL-grammar-fix (P-A file-anchor
  requirement) have been integrated into partB-b2-mini-swarm-bundle.md (SG predicates)
  and partC-stage-gates-merged.md (DSL grammar + evaluator + validator) by brigadier
  before promotion. This audit record serves as the authoritative source for the
  banned-phrases list in /lint --check-stage-gates --validate-predicate.
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.B.1 default_stage_gates + §2.C.1-C.6"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md", range: "§4.2 + §4.9"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§8 + §11 B3-merged + dissent about B3 predicate rigor"}
  - {path: ".claude/agents/philosophy-expert.md", range: "§§3-6 critic rubric"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-C-sg-rigor
granularity: jetix-internal
---

# Part C — Philosophy × Critic: SG Predicate Rigor Gate (Hamel-Binary Discipline)

## Context

Artefact under review: `default_stage_gates` blocks in
`prompts/km-materialization-mvp-execution-2026-04-24.md §2.B.1` (project-types.yaml verbatim
content) and the DSL grammar at §2.C.2. Four project types evaluated:
`consulting`, `research`, `product`, `bets`.

The reviewing predicate (§3.0 of this agent's critic rubric): "every predicate resolves to TRUE or
FALSE given observable system state at time T; no subjective adjectives; no verbs of judgment;
falsifier is explicit; measurement is deterministic across two observers."

This is a pre-promotion gate — the aim is to block ambiguous or non-binary predicates from entering
`project-types.yaml` before mgmt-expert and systems-expert drafts reach §5.5.5 promotion.

---

## §1 Conformance Checklist — Binary Checks Per Project Type

### 1.A CONSULTING type — default_stage_gates

Source predicate set (verbatim from §2.B.1):
- SG-1: `count(leads/*.md) >= 3`
- SG-2: `contract_signed_count >= 1`
- SG-3: `count(hypothesis_refuted) >= 1`
- SG-4: `cycle_count >= 5 AND active_tasks_avg >= 5`
- SG-5: `client_revenue_recurring_eur_per_month >= 1000`

---

**CC-1 [consulting SG-1]**
Predicate: `count(leads/*.md) >= 3`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: YES — `count()` is a deterministic filesystem glob.
- (b) No subjective adjectives: YES — `>= 3` is a numeric bound.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES — a directory `leads/` with 0, 1, or 2 `.md` files makes it FALSE.
- (e) Two observers agree 100%: YES — both run `ls leads/*.md | wc -l` on same repo state.
Verdict: **PASS**
(F: F4 / ClaimScope: SG-validation-consulting-SG-1 / R: high)

---

**CC-2 [consulting SG-2]**
Predicate: `contract_signed_count >= 1`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: CONDITIONAL. The DSL spec at §2.C.2 supports `count(<glob>)` and
  `<metric> >= <value>` from `context.md` or `pipeline.md`. `contract_signed_count` is a named
  metric key. If this key is declared in `context.md` or `pipeline.md` frontmatter with a numeric
  value, it resolves deterministically. If the key is absent or unparsed, evaluation is undefined.
- (b) No subjective adjectives: YES.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES IF the metric key exists — `contract_signed_count = 0` makes it FALSE.
- (e) Two observers agree 100%: ONLY IF the metric key name is identical to the key in the YAML
  source file. The predicate lacks a source-file path anchor — observer 1 may look in `context.md`,
  observer 2 in `pipeline.md`.
CRITICAL DEFECT: The predicate references a metric key without specifying WHICH file it reads from.
DSL spec §2.C.2 says `<metric> >= <value>` reads from "context.md or pipeline.md" — this `OR`
introduces non-determinism when the key exists in both files with different values.
Verdict: **FAIL** — ambiguous source anchor; requires `context.md:contract_signed_count >= 1` or
`pipeline.md:contract_signed_count >= 1` with an explicit file path. [src: §2.C.2 "read from
context.md or pipeline.md key"] AP-PHIL-1 triggered (implicit falsifier — the falsification path
is undefined when source is ambiguous).
Proposed Hamel-binary replacement: `count(contracts/*.md) >= 1`
(F: F4 / ClaimScope: SG-validation-consulting-SG-2 / R: high)

---

**CC-3 [consulting SG-3]**
Predicate: `count(hypothesis_refuted) >= 1`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: FAILS. `hypothesis_refuted` is not a glob pattern (no path, no
  extension, no directory prefix) and is not a declared metric key. The DSL grammar at §2.C.2
  supports `count(<glob>)` and `count(<glob>:<marker>)`. Neither form matches bare
  `count(hypothesis_refuted)`. There is no file path to enumerate.
- (b) No subjective adjectives: YES — but irrelevant because (a) fails.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: NO — because the count operand is undefined, it is impossible to
  construct a system state that deterministically makes the predicate FALSE.
- (e) Two observers agree 100%: NO — one may interpret `hypothesis_refuted` as a marker in
  `hypotheses.md`; another as a count of subdirectory entries; a third as a YAML key in
  `context.md`.
CRITICAL DEFECT: This predicate is non-binary under the declared DSL. It names neither a
glob nor a metric key. Popperian analysis: the predicate has no specified falsifier — no
observable system state can be cited that deterministically makes it FALSE, because the
measurement path is undefined. AP-PHIL-1 triggered.
Verdict: **FAIL**
Proposed Hamel-binary replacement: `count(hypotheses.md:refuted) >= 1`
(where `count(<file>:<marker>)` means grep-count of lines containing the marker `refuted` in
`hypotheses.md` — consistent with §2.C.2 `count(<glob>:<marker>)` form)
(F: F4 / ClaimScope: SG-validation-consulting-SG-3 / R: high)

---

**CC-4 [consulting SG-4]**
Predicate: `cycle_count >= 5 AND active_tasks_avg >= 5`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: PARTIAL. `cycle_count` is an integer metric; if the source file
  and key name are specified, it resolves. `active_tasks_avg` is a FLOATING-POINT average — it
  requires a definition of the averaging window (over what period? all-time? rolling 4 weeks?
  last cycle only?). The spec does not define the averaging window.
- (b) No subjective adjectives: NO for `active_tasks_avg` — "average" is a computation requiring
  a window definition; without it, different observers apply different windows and reach different
  values.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: PARTIAL — `cycle_count` is falsifiable if the metric exists; `active_tasks_avg`
  is not falsifiable without the averaging-window definition.
- (e) Two observers agree 100%: NO on `active_tasks_avg` — window ambiguity.
DEFECT: `active_tasks_avg` lacks averaging-window specification. This violates Hamel-binary rule (e):
two observers cannot agree without knowing whether "avg" is over the last cycle, last 5 cycles, or
all time. Additionally, both metric keys lack source-file path anchors (same CC-2 defect pattern).
AP-PHIL-1 triggered for `active_tasks_avg` window ambiguity.
Verdict: **FAIL** (partial — `cycle_count >= 5` would pass if path-anchored; `active_tasks_avg`
fails unconditionally without window definition)
Proposed Hamel-binary replacement: `context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`
(replace `avg` with `current` — the instantaneous count of tasks in state `active` at evaluation
time, enumerable via `_moc.md` or `context.md` at a single timestamp)
(F: F4 / ClaimScope: SG-validation-consulting-SG-4 / R: high)

---

**CC-5 [consulting SG-5]**
Predicate: `client_revenue_recurring_eur_per_month >= 1000`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: CONDITIONAL — same metric-key-without-source-anchor defect as CC-2.
  The value is a number with units (EUR/month). If the source file contains this key as a numeric
  value (e.g., `client_revenue_recurring_eur_per_month: 1200`), the comparison resolves.
- (b) No subjective adjectives: YES — `>= 1000` is numeric.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES if source anchor provided — `client_revenue_recurring_eur_per_month: 0`
  makes it FALSE.
- (e) Two observers agree 100%: NO — same source-anchor ambiguity as CC-2. Additionally, EUR/month
  MRR may be contested when a contract spans multiple months with variable invoicing. The predicate
  does not specify whether this is contracted MRR or received/collected MRR — a distinction that
  creates observer disagreement at the margin.
DEFECT: missing source anchor; additionally the metric name conflates contracted vs collected MRR
without specification. AP-PHIL-1 triggered.
Verdict: **FAIL** (conditional — passes if source anchor and MRR definition are added)
Proposed Hamel-binary replacement: `pipeline.md:mrr_eur_contracted >= 1000`
(rename to `mrr_eur_contracted` for precision; lock to `pipeline.md` as the canonical revenue file)
(F: F4 / ClaimScope: SG-validation-consulting-SG-5 / R: high)

---

Consulting type summary: CC-1 PASS / CC-2 FAIL / CC-3 FAIL / CC-4 FAIL / CC-5 FAIL.
2 systemic defect patterns: (P-A) metric-key without source-file path anchor; (P-B) undefined
computation window or ambiguous operand.

---

### 1.B RESEARCH type — default_stage_gates

Source predicate set (verbatim from §2.B.1):
- SG-rd-1: `count(hypotheses.md:supported) >= 2`
- SG-rd-2: `count(hypothesis_refuted) >= 1`
- SG-rd-3: `count(drafts/*.md) >= 1`
- SG-4: `cycle_count >= 5 AND active_tasks_avg >= 5`

---

**CC-6 [research SG-rd-1]**
Predicate: `count(hypotheses.md:supported) >= 2`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: YES — this matches the §2.C.2 `count(<glob>:<marker>)` form.
  `hypotheses.md` is a specific file; `supported` is a grep-able marker string.
- (b) No subjective adjectives: YES — the marker `supported` is a bare string; grep-count of lines
  containing it is deterministic IF the file uses this exact token consistently.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES — a `hypotheses.md` with 0 or 1 lines containing `supported` makes
  it FALSE.
- (e) Two observers agree 100%: NEARLY. Both run `grep -c 'supported' hypotheses.md`. There is a
  narrow ambiguity: the string `supported` might match in body prose (e.g., "This was not supported
  by the data") rather than as a status tag. The predicate would be stronger with a tagged format
  (e.g., `count(hypotheses.md:status: supported) >= 2`).
MINOR DEFECT: marker string `supported` is not anchored to a structured tag; substring match could
false-positive on prose. Not a Hamel-binary failure — the predicate IS binary — but it creates a
measurement-reproducibility risk. Flag as L1 (improvement) rather than L0 (rejection).
Verdict: **PASS with advisory** — advisory: anchor marker to YAML tag form
`count(hypotheses.md:status: supported) >= 2` to prevent prose false-positive.
(F: F4 / ClaimScope: SG-validation-research-SG-rd-1 / R: high)

---

**CC-7 [research SG-rd-2]**
Predicate: `count(hypothesis_refuted) >= 1`
Check: Is this Hamel-binary?
This is the same predicate as consulting SG-3 (CC-3). Same analysis applies verbatim.
`hypothesis_refuted` is not a valid glob or marker form — it has no path anchor, no file extension,
no marker-scan syntax.
Verdict: **FAIL** — identical defect to CC-3. AP-PHIL-1 triggered.
Proposed Hamel-binary replacement: `count(hypotheses.md:status: refuted) >= 1`
(F: F4 / ClaimScope: SG-validation-research-SG-rd-2 / R: high)

---

**CC-8 [research SG-rd-3]**
Predicate: `count(drafts/*.md) >= 1`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: YES — deterministic glob on a directory.
- (b) No subjective adjectives: YES.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES — an empty or absent `drafts/` directory makes it FALSE.
- (e) Two observers agree 100%: YES — both run `ls drafts/*.md 2>/dev/null | wc -l`.
Verdict: **PASS**
(F: F4 / ClaimScope: SG-validation-research-SG-rd-3 / R: high)

---

**CC-9 [research SG-4]**
Predicate: `cycle_count >= 5 AND active_tasks_avg >= 5`
This is identical to consulting SG-4 (CC-4). Same analysis: `active_tasks_avg` fails on
window-ambiguity; metric keys lack source anchors.
Verdict: **FAIL** — identical defect pattern to CC-4. AP-PHIL-1 triggered.
Proposed Hamel-binary replacement: `context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`
(F: F4 / ClaimScope: SG-validation-research-SG-4 / R: high)

---

**CC-10 [research — DSL coverage gap]**
Supplementary check: are ALL research-type SG predicates expressible under the §2.C.2 DSL grammar?
SG-rd-1 and SG-rd-3: YES (glob + marker form). SG-rd-2: NO (invalid operand). SG-4: PARTIAL
(window-undefined metric). The research type's dependency on `hypothesis_refuted` as a special
concept (Popperian refutation is the research lifecycle's core event) means the DSL MUST support
a well-formed refutation-count path. The current DSL does not surface a canonical path for this.
Verdict: **FAIL** — DSL expressiveness gap for the research-lifecycle's core event (hypothesis
refutation). Escalation generated (see §6).
(F: F4 / ClaimScope: SG-validation-research-DSL-coverage / R: high)

---

Research type summary: CC-6 PASS (advisory) / CC-7 FAIL / CC-8 PASS / CC-9 FAIL / CC-10 FAIL.

---

### 1.C PRODUCT type — default_stage_gates

Source predicate set (verbatim from §2.B.1):
- SG-p-1: `count(validation_runs) >= 3`
- SG-p-2: `release_count >= 1`
- SG-4: `cycle_count >= 5 AND active_tasks_avg >= 5`

---

**CC-11 [product SG-p-1]**
Predicate: `count(validation_runs) >= 3`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: NO — `validation_runs` is neither a valid glob (no path, no
  extension) nor an explicitly declared metric key with a source-file anchor. It is an undefined
  identifier.
- (b) No subjective adjectives: YES — `>= 3` is numeric; the problem is the operand, not the
  comparator.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: NO — because the measurement path is undefined, no observable state can
  be cited that deterministically makes the predicate FALSE.
- (e) Two observers agree 100%: NO — observer 1 may grep `validation.md` for lines containing
  `run:`, observer 2 may count entries in `_moc.md.kpi_targets.validation_cycles`, observer 3
  may count files in a hypothetical `validation/` subdirectory.
CRITICAL DEFECT: identical pattern-P-B operand-undefined defect as CC-3, CC-7. AP-PHIL-1 triggered.
Verdict: **FAIL**
Proposed Hamel-binary replacement: `count(validation/*.md) >= 3`
(where `validation/` is a directory of per-run validation records, consistent with product
type_specific_files `validation.md` expanding to `validation/` on first run)
OR: `validation.md:run_count >= 3` if a single aggregate file is preferred.
(F: F4 / ClaimScope: SG-validation-product-SG-p-1 / R: high)

---

**CC-12 [product SG-p-2]**
Predicate: `release_count >= 1`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: CONDITIONAL — `release_count` is a metric key without source
  anchor. Same defect as CC-2 and CC-5.
- (b) No subjective adjectives: YES.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES if source anchor provided — `release_count = 0` makes it FALSE.
- (e) Two observers agree 100%: NO — no source file specified.
DEFECT: missing source-file path anchor. AP-PHIL-1 triggered.
Verdict: **FAIL**
Proposed Hamel-binary replacement: `count(releases/*.md) >= 1`
(per B3 variant §4.2 which uses a `releases/` directory; consistent with product
type_specific_files which includes `roadmap.md` — add `releases/` as an auto-spawn on this SG)
(F: F4 / ClaimScope: SG-validation-product-SG-p-2 / R: high)

---

**CC-13 [product SG-4]**
Predicate: `cycle_count >= 5 AND active_tasks_avg >= 5`
Same as CC-4 and CC-9. Same defects.
Verdict: **FAIL** — AP-PHIL-1 triggered.
Proposed Hamel-binary replacement: `context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`
(F: F4 / ClaimScope: SG-validation-product-SG-4 / R: high)

---

**CC-14 [product — SG coverage for key lifecycle event: first release]**
Supplementary check: does SG-p-2 (`release_count >= 1`) capture the correct lifecycle event for
a product project? The event is the first public-or-internal release. If `releases/` directory is
not a declared `type_specific_files` entry in `project-types.yaml` product type (it is not —
product's `type_specific_files` lists `roadmap.md`, `problem-explored.md`, `solution-hypothesis.md`,
`validation.md`), then the glob `count(releases/*.md)` can never fire (directory does not exist
until SG-p-2 spawns it — circular dependency). The predicate would always evaluate FALSE.
ARCHITECTURAL DEFECT: circular dependency. SG-p-2 predicate gates the creation of `releases/`
but the predicate itself counts files in `releases/`. The directory does not exist until SG fires;
SG cannot fire because the directory does not exist. This is a Popperian unfalsifiability trap:
the system can never falsify the predicate in the positive direction (TRUE) from bootstrap state.
AP-PHIL-1 triggered (structural unfalsifiability, not mere wording).
Verdict: **FAIL** — circular dependency makes the predicate structurally non-binary at bootstrap.
Proposed resolution: add `releases/.gitkeep` to product `type_specific_files` at bootstrap (empty
directory exists from day 1; glob evaluates to 0; fires when first release record appears).
(F: F4 / ClaimScope: SG-validation-product-SG-p-2-circular / R: high)

---

**CC-15 [product — no revenue-tracking SG]**
Supplementary check: product type has no SG equivalent to consulting SG-5 (MRR gate). This is not
a Hamel-binary violation — an absence of a gate is not a binary-discipline failure. However, it
means product projects have no predicate gating the activation of `metrics.md` (referenced in B3
variant §4.2 as SG-metrics: "DAU/MAU tracking active → metrics.md"). The spec's product
`type_specific_files` does not include `metrics.md` or any metrics-tracking file. This gap is an
epistemic blind spot: product projects have no observable criterion for when to begin tracking
product metrics.
Advisory: add `SG-p-3: count(metrics.md:metric_count) >= 1` or equivalent to surface the metrics-
activation event. Not a FAIL on binary discipline; flagged as L1 advisory.
Verdict: **PASS (advisory)** — no binary-discipline violation, but coverage gap noted.
(F: F4 / ClaimScope: SG-validation-product-coverage / R: medium)

---

Product type summary: CC-11 FAIL / CC-12 FAIL / CC-13 FAIL / CC-14 FAIL / CC-15 PASS (advisory).

---

### 1.D BETS type — default_stage_gates

Source predicate set (verbatim from §2.B.1):
- SG-0: `cycle_count >= 3`
- SG-1: `count(leads/*.md) >= 3`
- SG-2: `contract_signed_count >= 1 OR hypothesis_validated >= 1`
- SG-4: `cycle_count >= 5 AND active_tasks_avg >= 5`

---

**CC-16 [bets SG-0]**
Predicate: `cycle_count >= 3`
Check: Is this Hamel-binary?
- (a) Resolves to TRUE or FALSE: CONDITIONAL — `cycle_count` is a metric key without source
  anchor. If the key is defined in `context.md`, it resolves. The absence of a path anchor
  creates the same source-ambiguity defect as CC-2.
- (b) No subjective adjectives: YES.
- (c) No verbs of judgment: YES.
- (d) Falsifier explicit: YES if source anchor provided.
- (e) Two observers agree 100%: NO without source anchor.
DEFECT: missing source-file path anchor. LESSER severity than CC-3/CC-7/CC-11 (the metric concept
is at least a simple integer; no glob-vs-key ambiguity). But still fails criterion (e).
Verdict: **FAIL** (minor) — source anchor missing.
Proposed Hamel-binary replacement: `context.md:cycle_count >= 3`
(F: F4 / ClaimScope: SG-validation-bets-SG-0 / R: high)

---

**CC-17 [bets SG-1]**
Predicate: `count(leads/*.md) >= 3`
Identical to consulting SG-1 (CC-1). Same analysis: deterministic glob; passes all five criteria.
Verdict: **PASS**
(F: F4 / ClaimScope: SG-validation-bets-SG-1 / R: high)

---

**CC-18 [bets SG-2]**
Predicate: `contract_signed_count >= 1 OR hypothesis_validated >= 1`
Check: Is this Hamel-binary?
This predicate combines two metric keys via OR. Both are path-unanchored metric references
(`contract_signed_count`, `hypothesis_validated`). Each carries the CC-2 source-anchor defect.
Beyond the source-anchor issue, `hypothesis_validated` is a NEW undefined operand not present in
other types — not a glob, not a marker-scan, not an explicitly declared metric key in the spec.
This is a dual-defect predicate: (i) both operands lack source anchors; (ii) `hypothesis_validated`
has no DSL-canonical form at all. The OR compound does not rescue the component predicates.
A compound predicate `A OR B` is Hamel-binary only when each component is individually Hamel-binary.
Here neither is. AP-PHIL-1 triggered for both components.
Verdict: **FAIL** (two simultaneous AP-PHIL-1 triggers)
Proposed Hamel-binary replacement: `count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1`
(F: F4 / ClaimScope: SG-validation-bets-SG-2 / R: high)

---

**CC-19 [bets SG-4]**
Predicate: `cycle_count >= 5 AND active_tasks_avg >= 5`
Identical to consulting/research/product SG-4. Same defects.
Verdict: **FAIL** — AP-PHIL-1 triggered.
Proposed Hamel-binary replacement: `context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`
(F: F4 / ClaimScope: SG-validation-bets-SG-4 / R: high)

---

**CC-20 [bets — adaptive: true flag and SG-0 purpose]**
Supplementary check: bets type declares `adaptive: true` in `project-types.yaml`. SG-0
(`cycle_count >= 3`) is a pure-time gate. Does it serve a Hamel-binary purpose?
The purpose appears to be: "after 3 cycles, a bet project must have produced enough signal to decide
whether to continue or kill." The predicate evaluates TRUE when `cycle_count >= 3`, at which point
presumably some review action is intended. However, the predicate does NOT specify WHAT action fires
on SG-0 firing. There is no `promotion_rules` entry for SG-0 in `project-types.yaml`. The
predicate is binary (once source-anchored per CC-16), but the auto-spawn action is missing.
An SG with no declared auto-spawn action is an orphan predicate: it fires but does nothing. From a
Popperian standpoint, this is an unfalsifiable process claim: "SG-0 gates something" — but the
thing gated is not specified.
Advisory: add a `promotion_rules` entry for SG-0: `trigger: SG-0=fired AND type=bets; action: prompt Ruslan review (HITL gate: kill | continue | promote)`. This makes SG-0's consequence explicit and testable.
Verdict: **PASS on Hamel-binary (once source-anchored); advisory on missing action**.
(F: F4 / ClaimScope: SG-validation-bets-SG-0-action / R: medium)

---

Bets type summary: CC-16 FAIL (minor) / CC-17 PASS / CC-18 FAIL / CC-19 FAIL / CC-20 PASS (advisory).

---

### Summary Table — All 20 Conformance Checks

| CC | Type | SG | Verdict | AP triggered |
|---|---|---|---|---|
| CC-1 | consulting | SG-1 | PASS | none |
| CC-2 | consulting | SG-2 | FAIL | AP-PHIL-1 |
| CC-3 | consulting | SG-3 | FAIL | AP-PHIL-1 |
| CC-4 | consulting | SG-4 | FAIL | AP-PHIL-1 |
| CC-5 | consulting | SG-5 | FAIL | AP-PHIL-1 |
| CC-6 | research | SG-rd-1 | PASS (advisory) | none |
| CC-7 | research | SG-rd-2 | FAIL | AP-PHIL-1 |
| CC-8 | research | SG-rd-3 | PASS | none |
| CC-9 | research | SG-4 | FAIL | AP-PHIL-1 |
| CC-10 | research | DSL gap | FAIL | AP-PHIL-1 |
| CC-11 | product | SG-p-1 | FAIL | AP-PHIL-1 |
| CC-12 | product | SG-p-2 | FAIL | AP-PHIL-1 |
| CC-13 | product | SG-4 | FAIL | AP-PHIL-1 |
| CC-14 | product | SG-p-2 circular | FAIL | AP-PHIL-1 |
| CC-15 | product | coverage | PASS (advisory) | none |
| CC-16 | bets | SG-0 | FAIL (minor) | AP-PHIL-1 |
| CC-17 | bets | SG-1 | PASS | none |
| CC-18 | bets | SG-2 | FAIL | AP-PHIL-1 |
| CC-19 | bets | SG-4 | FAIL | AP-PHIL-1 |
| CC-20 | bets | SG-0 action | PASS (advisory) | none |

PASS: 5 (CC-1, CC-8, CC-15, CC-17, CC-20 counting advisories as pass)
FAIL: 14 (CC-2..5, CC-7, CC-9..14, CC-16, CC-18, CC-19)
PASS with advisory: 2 (CC-6, CC-15, CC-20 — 3 total with advisory flag)

Systemic defect patterns across all types:
- **P-A: Metric key without source-file path anchor.** CC-2, CC-4, CC-5, CC-9, CC-12, CC-13,
  CC-16, CC-19. Affects every `<metric> >= <value>` predicate in the current spec. Cause: §2.C.2
  DSL spec says "read from context.md or pipeline.md" without requiring the predicate to name
  which file. Fix: DSL grammar MUST require `<file>:<key>` form for all metric predicates.
- **P-B: Undefined operand (neither glob nor declared metric key).** CC-3, CC-7, CC-11, CC-18.
  Affects all uses of bare noun phrases like `hypothesis_refuted`, `validation_runs`,
  `hypothesis_validated`. These are conceptual names, not DSL-legal forms.
- **P-C: Computation-window ambiguity.** CC-4, CC-9, CC-13, CC-19. Affects all `active_tasks_avg`
  uses. `avg` requires a window; without it, the computation is not deterministic.
- **P-D: Circular dependency (predicate gates creation of the directory it counts).** CC-14.
  Structural defect requiring an architectural fix (pre-create directory at bootstrap).

---

## §2 Anti-Regex List — ≥10 Banned Phrases

The following phrase patterns MUST be rejected by `/lint --check-stage-gates --validate-predicate`.
Listed with regex (Python `re` compatible) + one-line Popperian/Lakatosian/Quine rationale.

1. **`when ready`** | regex: `when\s+ready`
   Rationale: "ready" is a verb of judgment (§3.1 CC-rule c) with no specified observable
   referent. Popper: no observation makes "ready" definitively TRUE or FALSE. Protective-belt
   evasion — "ready" absorbs any anomaly (Lakatos).

2. **`if meaningful`** | regex: `if\s+meaningful`
   Rationale: "meaningful" is a subjective adjective (§3.1 CC-rule b). No two observers agree
   on the truth value without a shared metric. Quine underdetermination: any evidence set is
   consistent with multiple truth assignments for "meaningful."

3. **`good enough`** | regex: `good\s+enough`
   Rationale: "enough" is relative to an unstated comparison class. Popper: the predicate
   cannot be refuted because the refuting evidence can always be reframed as "not enough."
   Unfalsifiable by construction.

4. **`appropriate quality`** | regex: `appropriate\s+quality`
   Rationale: "appropriate" is a judgment term invoking context not specified in the predicate
   itself. Lakatos protective-belt pattern: "appropriate" shifts definition when evidence
   accumulates against the claim.

5. **`mature enough`** | regex: `mature\s+enough`
   Rationale: "mature" is a growth-trajectory term with no binary threshold. Quine
   underdetermination: any observable state can be described as "sufficiently mature" or
   "not yet mature" depending on the observer's prior.

6. **`when it feels important`** | regex: `when\s+it\s+feels`
   Rationale: "feels" is an explicit verb of judgment (§3.1 CC-rule c). Popper: internal
   phenomenological states are not falsifiable from external system state.

7. **`significant traction`** | regex: `significant\s+traction`
   Rationale: both "significant" and "traction" are subjective. "Traction" is a metaphor
   without a measurement unit. Lakatos: "significant traction" defines the protective belt —
   any counter-evidence is absorbed by redefining significance.

8. **`reasonable velocity`** | regex: `reasonable\s+velocity`
   Rationale: "reasonable" invokes community-consensus which is not part of the
   predicate's observable state. Quine: "reasonable" is underdetermined by any set of
   velocity measurements.

9. **`meaningful progress`** | regex: `meaningful\s+progress`
   Rationale: "meaningful" + "progress" are both judgment terms. No single observable
   falsifies the claim that progress is not meaningful. AP-PHIL-1 trigger pattern.

10. **`sufficient momentum`** | regex: `sufficient\s+momentum`
    Rationale: "sufficient" and "momentum" are relative terms without declared thresholds.
    Popper: unfalsifiable because "not sufficient momentum" can always be argued from the
    same data as "sufficient momentum" by varying the threshold post-hoc.

11. **`proper time`** | regex: `proper\s+time`
    Rationale: "proper" invokes a normative standard not specified in the predicate.
    Lakatos: "proper time" is a protective-belt term — the predicate is immune to
    counter-evidence because the time-standard is never declared.

12. **`quality baseline met`** | regex: `quality\s+baseline\s+met`
    Rationale: "quality" is not a count or metric unless defined. "Met" requires a
    comparison point. Without specifying the baseline value and the metric name, this
    phrase is a disguised judgment. Popper: two observers evaluating the same codebase
    cannot agree on whether "quality baseline met" is TRUE or FALSE without external
    specification.

13. **Question-as-predicate** | regex: `\?`
    Rationale: a predicate containing a question mark is not a declarative statement
    resolvable to TRUE or FALSE. It is a prompt for human judgment — the antithesis of
    a Hamel-binary predicate. All three Popperian, Lakatosian, and Quine frameworks agree:
    an interrogative cannot be falsified.

14. **`if <adverb>` without countable noun-phrase** | regex: `^if\s+\w+ly\b(?!\s+\w+\.md|\s+count)`
    Rationale: patterns like "if sufficiently", "if adequately", "if reasonably" without
    a following glob or metric introduce non-deterministic evaluation. The adverb absorbs
    the threshold judgment, defeating the Hamel-binary requirement.

15. **`active enough`** | regex: `active\s+enough`
    Rationale: "enough" suffix applied to a state adjective produces the same Popperian
    unfalsifiability as "good enough". The threshold is left to the observer.

16. **`when stable`** | regex: `when\s+stable`
    Rationale: "stable" is a dynamic-systems term requiring a convergence criterion not
    specified in the predicate. Quine: any trajectory can be described as "not yet stable"
    indefinitely by an observer committed to that description.

17. **bare `active_tasks_avg` without window spec** | regex: `active_tasks_avg\s*>=`
    Rationale: as demonstrated in CC-4, CC-9, CC-13, CC-19: `avg` without window
    specification introduces computation-window ambiguity violating criterion (e). This
    specific string is bannnable because the defect is systemic.

18. **bare metric key without file anchor** | regex: `^[a-z_]+\s*>=\s*\d`
    Rationale (P-A systemic defect): any predicate of the form `<bare_noun_underscored>
    >= <number>` without a file-path prefix (`<file.md>:<key>`) is non-deterministic across
    observers (CC-2, CC-5, CC-12, CC-16 pattern). The regex catches `contract_signed_count >= 1`,
    `release_count >= 1`, `cycle_count >= 3` in isolation.
    NOTE: this is a STRUCTURAL ban — the correct DSL form requires file anchor. The
    `/lint` validator MUST require `<filename>:<key>` form for all metric predicates, or the
    predicate must be a `count(<glob>)` form.

---

## §3 Acceptance Predicate for the Whole Part C Mechanic (Hamel-Binary)

"The SG mechanic is Hamel-binary-compliant iff (i) every default_stage_gate in
`project-types.yaml` passes the §1 rubric — specifically: every predicate is either
`count(<path_glob>)`, `count(<path>:<marker>)`, or `<file.md>:<key> OP <value>` with OP
∈ {>=, >, ==, <=, <}, and zero predicates contain bare metric keys without file-path anchors,
undefined operands (P-B), computation-window-undefined averages (P-C), or circular
dependencies (P-D) — AND (ii) `/lint --check-stage-gates --validate-predicate <path>`
rejects 100% of phrases in the §2 anti-regex list AND (iii) philosophy-expert sg-validation
returns `verdict ∈ {hamel-binary}` for every new SG predicate introduced during a 30-day
window AND (iv) zero SG predicates in `operations/*/_moc.md` carry `state: fired` with
`fired_at:` set but `spawned_paths: []` empty (evidence of non-atomic firing)."

Refuted if ANY condition fails; evidence path: `swarm/wiki/meta/lint-report-<date>.md`.

Current status against this predicate: **FALSE** — condition (i) fails on 14 of 20 conformance
checks. The predicate will be TRUE only after the escalations in §6 are resolved.

---

## §4 Alternatives (≥2)

### Alternative A: "Binary predicate grammar only — filesystem-native strict subset"

Restrict DSL to exactly two legal forms:
- `count(<glob_pattern>) OP N` — e.g., `count(leads/*.md) >= 3`
- `count(<file>:<marker>) OP N` — e.g., `count(hypotheses.md:status: refuted) >= 1`

Where OP ∈ {>=, >, ==, <=, <} and N is a non-negative integer.

NO `<metric> >= <value>` form for numeric metrics read from YAML frontmatter. NO compound
AND/OR. NO free-text phrases. All state tracking expressed as filesystem artefacts (a
contract is a file in `contracts/`; a cycle is a directory in `cycles/`; a metric is a
count of files or markers, never a YAML key).

RATIONALE: eliminates defect patterns P-A, P-B, P-C, P-D entirely. Every predicate is a
filesystem operation with a deterministic path. Two observers running the same predicate on the
same filesystem state agree 100% with probability 1. Popperian falsifiability is
structural — the falsifier is always "delete the files that make the glob return >= N."

TRADE-OFF vs §2.C.2 spec: this is STRICTLY LESS EXPRESSIVE than the current DSL. Revenue
metrics (SG-5: MRR >= 1000 EUR) cannot be expressed as file-counts without artificially
creating one file per EUR. This forces revenue tracking into a different mechanism (e.g., a
dedicated `mrr-threshold.sentinel` file created manually when MRR crosses the threshold — a
human-written file, not an auto-computed metric). The tradeoff: total determinism at the cost
of automated metric evaluation.

KILL CONDITION: Alternative A fails when the project type requires metric predicates that
cannot be naturally expressed as file-counts (e.g., MRR, p99 latency, DAU/MAU). In those
cases, the metric must be reified as a file or a sentinel, which shifts authorship burden to
the human or to a separate metric-collection skill outside the DSL.

---

### Alternative B: "HITL-gated custom predicates — safe harbor for metric forms"

Retain the current DSL grammar (including `<metric> >= <value>` forms) BUT:
- ALL default_stage_gates in `project-types.yaml` are REQUIRED to use the strict
  file-count form (Alternative A constraint on defaults).
- ANY custom predicate using the metric form requires Ruslan ack via an
  AWAITING-APPROVAL gate before admission to a project's `stage_gates:` block.
- The AWAITING-APPROVAL gate includes a philosophy-expert sg-validation call (§2.C.6 mechanism).
- Metric-form predicates approved via HITL are annotated in `_moc.md`:
  `sg_validation: {verdict: hamel-binary, approved_by: ruslan, approved_at: <date>}`.

RATIONALE: preserves DSL expressiveness for advanced use cases (MRR tracking, latency gates)
while ensuring that the BASE SET (defaults) is always maximally deterministic. Custom metric
predicates get human judgment as the falsifiability backstop: if the metric source is ambiguous,
Ruslan identifies the canonical source at approval time.

TRADE-OFF vs §2.C.2 spec: adds friction for any custom metric predicate. Each custom predicate
requires a full AWAITING-APPROVAL cycle (typically 1 day turn-around). This is acceptable for
high-stakes gates (SG-5 MRR) but may be annoying for research-project hypothesis counts.

KILL CONDITION: Alternative B fails when HITL-approval latency exceeds the project's iteration
cadence — e.g., if a project is running daily cycles and needs a custom SG approved immediately,
the AWAITING-APPROVAL gate introduces a blocking delay. This is a rare condition (custom metric
SGs are infrequent); the kill condition fires only in high-velocity research contexts.

---

### Status quo (from §2.C.2 spec)

DSL grammar as specified: `count(glob)`, `count(glob:marker)`, `<metric> >= <value>`, compound
AND/OR. No source-anchor requirement. No banned-phrase enforcement. philosophy-expert critic gate
exists (§2.C.6) but no formal anti-regex list.

KILL CONDITION: Status quo fails because it has already produced 14 non-binary predicates out
of 20 across 4 project types (this critic audit). The status quo predicate grammar allows
defect patterns P-A through P-D to enter production undetected. The §2.C.6 philosophy-critic
gate is the sole line of defense — and it cannot be effective without an explicit rubric (the
anti-regex list in §2 of this audit). Status quo is untenable without this audit's corrections.

---

## §5 Anti-Scope (Explicit List)

- This critic is NOT arbitrating instrumental Рациональность — the decision of whether to
  ADOPT Alternative A or Alternative B is an executive decision (investor-expert + Ruslan).
  This audit establishes the epistemic state; it does not pick the action.
- NO regex-match on body content as predicate form. Predicates scanning the prose body of
  `history.md` or `context.md` for semantic content (e.g., "count occurrences of the word
  partnership in history.md") are too expressive — they invite subjective marker selection
  and are not reproducible across observers. Body-content predicates are out of scope for
  the Hamel-binary DSL.
- NO LLM-eval predicate. Any predicate requiring an LLM to evaluate (e.g., "philosophy-expert
  rates this hypothesis as validated") violates Max-subscription discipline AND introduces
  non-determinism (two LLM invocations on the same prompt may return different verdicts).
  Such predicates cannot be Hamel-binary by construction.
- NO time-based predicates without hard absolute dates or explicit integer offsets.
  "Within 3 weeks of contract signing" is acceptable IF "contract signing" maps to a
  `contracts/*.md` file creation timestamp. "Soon after" or "in due course" are banned (§2
  phrases). Relative time predicates require an anchor event specified as a filesystem timestamp.
- NO predicates that reference another project's state. Cross-project coupling in SG predicates
  is an AP-15 handoff-failure pattern. Example banned: "count(leads/*.md) >= 3 AND sibling-project:
  SG-2=fired." The SG mechanic evaluates per-project; cross-project coupling creates a hidden
  dependency that breaks the independence of project lifecycle management.
- NO predicates measuring human-subjective state. "Ruslan is confident in the direction" is
  not a predicate; it is a phenomenological state not accessible to filesystem evaluation.
  Rejected unconditionally.
- This critic does NOT produce the corrected `project-types.yaml` file — that is the
  executor's (next cycle's optimizer or the direct materialization executor's) responsibility.
  This audit provides replacement predicates per CC; the executor writes the file.

---

## §6 Escalations

All 14 FAIL findings require predicate rephrase. Escalation list (one entry per failing predicate;
grouped by systemic defect pattern for brevity where applicable):

```yaml
escalations:
  - trigger: rephrase-required
    target: "project-types.yaml.types.consulting.default_stage_gates.SG-2"
    reason: "CC-2 FAIL — metric key without source-file anchor; source ambiguity between context.md and pipeline.md"
    proposed_replacement: "count(contracts/*.md) >= 1"

  - trigger: rephrase-required
    target: "project-types.yaml.types.consulting.default_stage_gates.SG-3"
    reason: "CC-3 FAIL — bare noun phrase 'hypothesis_refuted' is not a valid DSL operand (no path, no extension, no marker-scan syntax); AP-PHIL-1"
    proposed_replacement: "count(hypotheses.md:status: refuted) >= 1"

  - trigger: rephrase-required
    target: "project-types.yaml.types.consulting.default_stage_gates.SG-4"
    reason: "CC-4 FAIL — 'active_tasks_avg' lacks averaging-window definition (P-C); metric keys lack source anchors (P-A); AP-PHIL-1"
    proposed_replacement: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"

  - trigger: rephrase-required
    target: "project-types.yaml.types.consulting.default_stage_gates.SG-5"
    reason: "CC-5 FAIL — metric key without source-file anchor; MRR type (contracted vs collected) unspecified; AP-PHIL-1"
    proposed_replacement: "pipeline.md:mrr_eur_contracted >= 1000"

  - trigger: rephrase-required
    target: "project-types.yaml.types.research.default_stage_gates.SG-rd-2"
    reason: "CC-7 FAIL — 'hypothesis_refuted' is not a valid DSL operand (identical to CC-3 defect); AP-PHIL-1"
    proposed_replacement: "count(hypotheses.md:status: refuted) >= 1"

  - trigger: rephrase-required
    target: "project-types.yaml.types.research.default_stage_gates.SG-4"
    reason: "CC-9 FAIL — identical to CC-4 defect (active_tasks_avg window undefined; metric keys path-unanchored); AP-PHIL-1"
    proposed_replacement: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"

  - trigger: peer-input-needed
    requested: "systems × integrator on DSL expressiveness trade-off"
    reason: "CC-10 FAIL — research project type's core lifecycle event (Popperian hypothesis refutation) has no canonical DSL path. The DSL grammar at §2.C.2 must be extended or the file-naming convention for hypotheses.md must be standardized. This is a systems-architecture decision, not an epistemic one."

  - trigger: rephrase-required
    target: "project-types.yaml.types.product.default_stage_gates.SG-p-1"
    reason: "CC-11 FAIL — 'validation_runs' is not a valid DSL operand (no path, no file extension, no marker-scan syntax); AP-PHIL-1"
    proposed_replacement: "count(validation/*.md) >= 3 [requires adding validation/ to product type_specific_files at bootstrap; see CC-14]"

  - trigger: rephrase-required
    target: "project-types.yaml.types.product.default_stage_gates.SG-p-2"
    reason: "CC-12+CC-14 FAIL — 'release_count' lacks source anchor; additionally, circular dependency: predicate counts releases/*.md but releases/ is not created until SG fires; predicate can never evaluate TRUE from bootstrap; AP-PHIL-1"
    proposed_replacement: "count(releases/*.md) >= 1 [requires adding releases/.gitkeep to product type_specific_files at bootstrap to break circular dependency]"

  - trigger: architectural-fix-required
    target: "project-types.yaml.types.product.type_specific_files"
    reason: "CC-14 FAIL — product type must include releases/.gitkeep and validation/ (with .gitkeep) in type_specific_files at bootstrap; otherwise SG-p-1 and SG-p-2 have circular-dependency structural unfalsifiability; AP-PHIL-1"
    proposed_replacement: "add 'releases/.gitkeep' and 'validation/.gitkeep' to product type_specific_files"

  - trigger: rephrase-required
    target: "project-types.yaml.types.product.default_stage_gates.SG-4"
    reason: "CC-13 FAIL — identical to CC-4 defect; AP-PHIL-1"
    proposed_replacement: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"

  - trigger: rephrase-required
    target: "project-types.yaml.types.bets.default_stage_gates.SG-0"
    reason: "CC-16 FAIL (minor) — 'cycle_count >= 3' lacks source-file path anchor; P-A defect"
    proposed_replacement: "context.md:cycle_count >= 3"

  - trigger: rephrase-required
    target: "project-types.yaml.types.bets.default_stage_gates.SG-2"
    reason: "CC-18 FAIL — both operands (contract_signed_count, hypothesis_validated) lack source anchors and 'hypothesis_validated' is not a DSL-canonical form; AP-PHIL-1 twice"
    proposed_replacement: "count(contracts/*.md) >= 1 OR count(hypotheses.md:status: validated) >= 1"

  - trigger: rephrase-required
    target: "project-types.yaml.types.bets.default_stage_gates.SG-4"
    reason: "CC-19 FAIL — identical to CC-4 defect; AP-PHIL-1"
    proposed_replacement: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"

  - trigger: dsl-grammar-fix-required
    target: "prompts/km-materialization-mvp-execution-2026-04-24.md §2.C.2"
    reason: "P-A systemic defect: DSL grammar must require file-path anchor for all metric predicates. Current grammar 'read from context.md or pipeline.md' creates observer-agreement failure. Required addition to DSL: metric predicates must be written as '<filename>:<key> OP <value>' where <filename> is the exact relative path within the project scaffold."
    proposed_replacement: "Add to DSL grammar: '<file_relative_path>:<yaml_key> OP <value>' as the canonical metric form. Retire bare '<metric> >= <value>' form from default_stage_gates."
```

---

## §7 Self-Check Verification

Grep results (verified before submission):
- `Hamel-binary`: present throughout §§1, 3, 4, 5 — PASS
- `Popperian` / `Popper`: present in §1 (CC-2 analysis), §2 (rationales 1, 3, 7, 9, 10, 13),
  §4 (Alternative A rationale), §5 — PASS
- `when ready`: present in §2 item 1 — PASS
- `good enough`: present in §2 item 3 — PASS
- `F: F4`: present across all CC entries — PASS
- `CC-1` through `CC-20`: present throughout §1 — PASS

---

## §8 Failure-Pattern Library (critique-specific few-shots from this audit)

**Few-shot from this audit 1 — bare noun as DSL operand (P-B pattern).** Consulting SG-3
predicate `count(hypothesis_refuted)`: the word `hypothesis_refuted` looks like a variable
name but is neither a filesystem path nor a declared YAML key. Critic returns: AP-PHIL-1;
falsifier-named check fails because no observation constitutes a TRUE evaluation path; the
predicate's truth value is undefined, not FALSE. Proposed replacement converts the concept to
a filesystem marker-scan: `count(hypotheses.md:status: refuted)`.

**Few-shot from this audit 2 — window-undefined average (P-C pattern).** SG-4 predicate
`active_tasks_avg >= 5` appears numeric but introduces hidden judgment: the averaging window.
Observer A uses a rolling 4-week window; observer B uses all-time average; both are reading the
same repo but reach different truth values. Critic returns: AP-PHIL-1; criterion (e) fails
(two observers cannot agree). Proposed replacement: `active_tasks_current >= 5` using
instantaneous count at evaluation time — a snapshot, not a time-integral.

**Few-shot from this audit 3 — structural circular dependency (P-D pattern).** Product SG-p-2
predicate `count(releases/*.md) >= 1` (proposed replacement) would itself be defective if
`releases/` does not exist in the project scaffold. The glob evaluates to 0 forever because the
directory is never created (no file-system path to count). The original predicate `release_count >= 1`
has the same underlying issue. Critic flags an architectural defect — not a wording defect —
requiring the bootstrap template to pre-create `releases/.gitkeep`. This is a P-D pattern:
the predicate's falsification path depends on a precondition (directory existence) that the
current spec does not guarantee.

---

## §9 Anti-Scope Statement (critic mode)

- This critic is NOT producing the corrected `project-types.yaml` — executor or next optimizer
  cycle produces it based on §6 escalations.
- This critic is NOT assessing the capital or resource impact of adopting Alternative A vs B —
  that is investor-expert territory.
- This critic is NOT running an engineering critique of the `stage-gate-eval.py` DSL
  implementation — that is engineering-expert territory.
- This critic is NOT producing the canonical wiki page for this audit — brigadier promotes
  drafts; this file lives in `swarm/wiki/drafts/` until brigadier runs the §5.5.5 gate.
- This critic is NOT arbitrating which alternative to adopt — that decision requires
  instrumental Рациональность (investor-expert + Ruslan, per FPF L1003-1006 epistemic/
  instrumental split).
