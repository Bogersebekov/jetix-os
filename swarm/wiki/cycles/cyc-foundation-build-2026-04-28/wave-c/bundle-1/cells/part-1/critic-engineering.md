---
title: Part 1 — engineering-expert critic gate (Phase E)
date: 2026-04-28
phase: C-1-critic
expert: engineering-expert
mode: critic
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 1
verdict: FLAG-MINOR
sources:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md
F: F4
ClaimScope: "Holds for Part 1 architecture.md as drafted post-Wisdom-Loop, pre-canonical. Does not govern other Foundation Parts."
R:
  refuted_if: "Any finding below is demonstrably incorrect on re-read of the source document"
  accepted_if: "All 7 checks produce verdicts consistent with the evidence quoted below"
---

# Part 1 — engineering-expert critic gate (Phase E)

**Verdict: FLAG-MINOR** — 5 addressable gaps, all fixable in <30 minutes. No Part 6/8 boundary
violations. No broken citations. Contradiction resolutions C1/C2/C4 are visible. One SLO-threshold
labeling gap in §B.1 is the most consequential finding.

---

## §3.1 Conformance Checklist

| check_id | result | evidence |
|---|---|---|
| 1-deep-module | pass | §H declares narrow 6-command public interface against wide internal complexity (git plumbing, schema engine, config resolution). Ousterhout deep-module criterion met. |
| 2-function-purpose | N/A | Not a software file with public functions; the document is an architecture specification. Criterion is not applicable to a markdown artefact. |
| 3-test-integrity | N/A | No test deletions present in this document. |
| 4-premature-abstraction | pass | Abstractions present (cross-fork schema, overflow token, F-G-R tagging) all have ≥3 concrete uses documented or are explicitly tagged as Phase-B stubs with deferred-activation notes. |
| 5-external-dependency | pass | §A declares every external dep (Part 6 gate, cross-fork import, hook, schema validation) with failure-mode declared at the call site. §K backs each with a named failure mode. |
| 6-dry | FLAG | Regex pattern `^\[(area)\] (verb) (subject)( \(why\))?$` appears verbatim in §H.2, §I.2 (comment block), §I.3 (schema_version_history format field), and §L P1.2 — four locations. None of the three latter occurrences references §I.2 as the canonical source. Fowler refactoring analogy: Extract Constant. One canonical regex location; other occurrences reference it. DRY violation count: 1 (minor). |
| 7-tool-eval-acceptance | N/A | This is an architecture document, not a tool-eval.md draft. |
| 8-architecture-pattern | pass | §H declares the deep-module orchestration pattern explicitly with Ousterhout citation and justification. §H.1 ownership note explicitly declares swarm/lib/ as the owner of /company-status, /knowledge-diff, /lint — satisfying the "orchestration pattern named and justified" requirement for an architecture proposal of this type. |

---

## §3.2 Acceptance Predicate (Hamel-binary)

`swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` passes Conformance checks 1
(deep-module), 4 (premature-abstraction), 5 (external-dependency), 8 (architecture-pattern); check 6
(DRY) FLAGS minor regex repetition; checks 2, 3, 7 are N/A for a markdown architecture document; AND
has ≥2 alternatives implicit in §L acceptance predicate status entries (COMPLETE/PARTIALLY
SATISFIED/BLOCKED with alternative paths named); AND has §F.2 explicit anti-scope with 9 specific
exclusion bullets; subject to the 5 gap-fixes enumerated in §§ below.`

---

## §3.3 Alternatives

| # | Alternative | Kill condition |
|---|---|---|
| A | Accept with 5 minor fixes (DRY regex, §B.1 SLI labels, §I.4 required[], 3 missing §K modes) — re-promote same document | Fails if any of the 5 fixes introduces new scope creep or contradicts an existing Foundation artefact |
| B | Re-dispatch engineering × integrator with specific fix list, produce revised draft | Fails if re-dispatch cycle consumes >30 min wall-clock given that all 5 fixes are mechanical edits |
| status-quo | Accept as-is, defer fixes to Wave D | Fails because §B.1 SLI target values in the current form can be misread as Part 1-owned SLO thresholds, creating a Part 8 boundary confusion at Wave C materialisation time |

---

## §3.4 Anti-scope

- Not evaluating priority across Parts — whether Part 1 should be promoted before Part 3 is mgmt × integrator territory.
- Not evaluating capital impact of the backup cost arithmetic in §K K9 — that is investor × critic territory.
- Not adjudicating the OQ-PHIL-PART1-3 `(why)` mandatory/optional dispute — philosophy × critic territory.
- Not authoring a system model for the R2 provenance-drift loop cited in §F — systems × critic territory.
- Not optimizing — this critic pass surfaces failures; follow-up engineering × optimizer dispatches fix proposals.

---

## §3.5 Specific Failures Found

### FINDING-1 — DRY: Regex repeated 4 times (AP-ENG-11 / check 6)

**Location:** §H.2 (pre-commit hook spec comment block, line ~381), §I.2 (canonical regex declaration block
~lines 646-659), §I.3 (schema_version_history.format field ~line 671), §L P1.2 narrative (~line 818).

**Evidence (verbatim):** All four sites reproduce `^\[(area)\] (verb) (subject)( \(why\))?$` as
a literal string without a "see §I.2 for canonical" cross-reference.

**Impact:** If the regex changes (e.g. `(why)` becomes mandatory per OQ-PHIL-PART1-3), an editor must
update 4 locations. The `format:` field in §I.3 schema_version_history YAML is the most dangerous: a
machine parser reading that field as the canonical regex would diverge from the §I.2 canonical block.

**Severity:** Minor — same document, same section cluster. Fixable with one sentence added at each
non-canonical occurrence: "Canonical regex: see §I.2 `shared/schemas/commit-format-tokens.json`
description block."

---

### FINDING-2 — Scope-creep soft violation: §B.1 SLI target column declares Part 8-owned thresholds without "calibration parameter" label

**Location:** §B.1 Four Golden Signals table, column "SLI target", lines ~99-103.

**Evidence (verbatim):**
- `commit-latency-p95` SLI target: `≤3000ms (3 seconds)`
- `hook-failure-rate` SLI target: `SLO ≤ 2% per week (false positives are errors; see K3)`
- `repo-growth-rate-MB-per-day` SLI target: `Target ≤ 10MB/day; alert threshold at Part 8's discretion`

**Part 8 boundary claim (part-8 §E Laws, verbatim):** "SLI/SLO values declared in Foundation artefact
MUST be labeled as starter/calibration values with explicit calibration-cadence field; hardcoded
thresholds without calibration label are a Foundation violation."

**Part 1 anti-scope (§F.2 verbatim):** "NOT SLO thresholds or alert policies. Part 1 emits the Four
Golden Signals (§B.1). Part 8 owns the SLO threshold for each signal, the alert conditions, and the
error-budget burn policy."

**Contradiction:** Part 1 correctly disclaims SLO ownership in §F.2 but §B.1's SLI target column
implicitly asserts concrete threshold values (2%, 3 seconds, 10 MB/day) without labeling them as
"starter/calibration parameters for Part 8 adoption." The §J burn-rate table (hook-failure-rate
6-12%, ≥15% tiers) compounds this: these are calibration-parameter SLO tiers that belong to
Part 8's schema, not Part 1's §J.

**This is NOT a hard Part 8 boundary violation** — §F.2 is explicit and correct. It is a labeling
gap that could cause a Wave C reader to treat Part 1's starter-value table as Part 1-owned SLOs.

**Fix:** Add `(starter value — calibration parameter for Part 8 adoption, not Part 1-owned SLO)`
to each threshold cell in §B.1. Add same label to §J burn-rate table tiers. This is a 3-line edit.

---

### FINDING-3 — Schema completeness gap: `task-return-packet.json` stub missing `required` array (AP-ENG-5 analogue)

**Location:** §I.4, lines ~680-709.

**Evidence:** The JSON Schema stub for `task-return-packet.json` declares `properties` for
`git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class` but has no `required: [...]`
array. JSON Schema draft-07 without a `required` array means all properties are optional.

**Impact:** The `git_commit_hash` field is declared as "FROZEN — not mutable after set" and as
"LOAD-BEARING for Part 5 DRR verification" (§B.2). If the field is not in `required`, a
task-return packet that omits `git_commit_hash` entirely is schema-valid — the load-bearing
constraint is not enforced by the schema.

**Note on design intent:** The stub is declared PARTIAL ("Bundle 3 will author the full
task-return-packet schema"). For a stub, the absence of `required` may be intentional to avoid
premature constraint. However, the document should make this explicit: either add
`"required": ["git_commit_hash"]` as the Part 1-contributed frozen field, or add a `$comment`
noting "required array deferred to Bundle 3 full spec; Part 1 mandates git_commit_hash as
required field."

**Severity:** Minor — schema stub, not yet operational. Fixable with one line.

---

### FINDING-4 — §K failure-mode coverage: 3 latent failure modes not enumerated

**Location:** §K (K1-K14 listed; K15, K16, K17 absent).

#### FINDING-4a — Concurrent commit race condition (K15 candidate)

**Scenario:** Two concurrent `git commit` operations (Phase B multi-agent scenario, or
concurrent Claude Code sessions) can produce a `.git/index.lock` file conflict. Git acquires
a lock on `.git/index` for each commit; a second concurrent attempt fails with "Another git
process seems to be running." This is NOT covered by K1 (partial commit — K1 assumes a
single commit that fails mid-write) and is NOT covered by K2 (schema validation failure —
K2 assumes the hook, not a lock conflict).

**Detection:** `git commit` exits non-zero with error text containing `index.lock`. Recovery:
delete `.git/index.lock` after confirming no other git process is running. HALT policy until
lock is resolved; the failed commit must be retried.

**Phase relevance:** Phase A (single-agent, single-session) makes this rare but not impossible
(two Claude Code tabs simultaneously). Phase B (multi-agent) makes this a systematic risk.

#### FINDING-4b — Disk-full during commit (K16 candidate)

**Scenario:** A `git commit` attempted when the filesystem containing `.git/` is at or near
capacity fails mid-write, leaving a partial object in `.git/objects/`. `git fsck` will
detect this as a dangling or corrupt object. K1 covers partial-commit detection via
`git status`, but K1's recovery path (`git add + git commit` or `git checkout`) assumes
the disk failure has been resolved. Disk-full is a distinct root cause requiring a different
first response: free disk space before attempting any git operation.

**Detection:** `git commit` exit non-zero with error text `"No space left on device"` OR
`git fsck` reporting `dangling blob`. Recovery: (a) free disk space (identify large committed
files; consider LFS migration if voice transcripts are the cause — see §A Admissibility A-4);
(b) run `git fsck --full`; (c) if dangling objects found, run `git gc --prune=now`; (d) retry
commit. HALT ALL CANONICAL WRITES until disk-full is resolved.

#### FINDING-4c — Fork schema drift: `commit-format-tokens.json` diverges between repos (K17 candidate)

**Scenario:** Phase B partner fork adds area tokens to their copy of
`shared/schemas/commit-format-tokens.json` independently. When a cross-fork import is attempted,
the parent's `/lint --check-commit-format` runs against fork commits that use tokens valid in
the fork but not in the parent's schema. The lint run flags every fork commit as malformed. K5
covers fork import collision at the path level; K12 covers token DRY violation within a single
repo; neither covers the cross-fork token-namespace divergence scenario.

**Detection:** Cross-fork import + `/lint --check-commit-format --all` on imported commits
reports high false-positive rate on tokens matching `^[a-z][a-z0-9-]*$` pattern but not in
parent's token list. Recovery: reconcile token lists between repos before import; create a
`token-alignment` record in `cross-fork-provenance.json` metadata field documenting the
diverged tokens. The `metadata` Ashby-overflow field in §I.1 schema is the correct location
for this reconciliation record.

**Severity of all three:** Minor individually; K16 (disk-full) is the most operationally
likely before Phase B. All three are addressable with ≤10-line §K additions.

---

### FINDING-5 — §L P1.1 acceptance predicate: test fixture absence not flagged as HARD GAP equivalent

**Location:** §L P1.1 "Acceptance predicate status: PARTIALLY SATISFIED", lines ~806-812.

**Evidence:** The predicate references "synthetic Phase B partner test fixture" that "NOT YET
EXISTS (Phase B work)." P1.3's equivalent blocked item (K10) is labeled "HARD GAP" and tracked
as a named failure mode (K10). P1.1's test fixture absence is acknowledged but not given the
same "HARD GAP" designation or a Kx failure-mode entry.

**Impact:** Low — the PARTIALLY SATISFIED label is honest. But the absence of a named Kx entry
for "test fixture for cross-fork schema absent" means Part 8 health monitoring has no signal to
track this gap. Without a Kx entry, the gap is invisible to the automated health checks that
will eventually parse §K.

**Fix:** Add a sentence to K5 or add K15/K17 (per Finding-4): "Phase A: no test fixture for
cross-fork schema validation exists — gap label `[PHASE-B-DEFERRED: cross-fork-schema-test-
fixture]`. Visibility: registered as HARD GAP equivalent in §L P1.1."

---

## §3.6 Recommended Changes

| change | ap_code_addressed | estimated_effort |
|---|---|---|
| Add "canonical regex: see §I.2" reference at §H.2, §I.3, §L P1.2 occurrences of the regex | AP-ENG-11 DRY | small (3 in-place sentence additions) |
| Add `(starter value — calibration parameter for Part 8 adoption, not Part 1-owned SLO)` label to each §B.1 SLI target cell and §J burn-rate tiers | FINDING-2 scope-creep label | small (6 cell edits) |
| Add `"required": ["git_commit_hash"]` OR `$comment` noting Bundle 3 defers required array, to §I.4 task-return-packet.json stub | FINDING-3 schema completeness | small (1-2 line addition) |
| Add K15 (concurrent commit lock conflict), K16 (disk-full), K17 (fork schema drift) entries to §K | FINDING-4 failure-mode exhaustiveness | small (3 × ~8 lines each) |
| Add HARD GAP label and cross-reference to §L P1.1 test fixture absence | FINDING-5 visibility | small (1 sentence) |

---

## §3.7 Contradiction Resolutions Visibility

| Contradiction | Resolved in document? | Evidence |
|---|---|---|
| C1 — shared infra `swarm/lib/` ownership | YES — VISIBLE | §H.1 CLI signatures explicitly: "Owner: swarm/lib/ shared infra (NOT Part 1-owned; Part 1 owns the Law guaranteeing offline)" for /company-status, /knowledge-diff, /lint |
| C2 — Part 8 owns health-signal schema | PARTIALLY RESOLVED — labeling gap | §F.2 anti-scope explicitly disclaims SLO ownership. §B.1 correctly emits signals. Gap: §B.1 SLI target column values are not labeled as "starter/calibration parameters for Part 8 adoption" — see FINDING-2 |
| C4 — PhaseOf → methodologically-uses for governance edges | YES — VISIBLE | §D.2 uses `methodologically-uses` for Part 6 → Part 1 edge with explicit rationale; §D preamble lists `methodologically-uses` in the 10-edge reference table with correct definition |

---

## §3.8 A.14 Edge-Type Audit (Check 4)

Scanned §D Dependencies for prohibited terms. Result:

- `depends-on`: not found outside the prohibition declaration in §D preamble
- `uses` (bare): not found
- `calls` / `reads` / `writes` / `triggers` / `needs`: not found in §D

All edges in §D.2 use valid A.14 types: `operates-in`, `methodologically-uses`, `constrained-by`.
The `AspectOf` mention is correctly flagged as "pending philosophy-expert validation" and not
declared as a current edge. A.14 compliance is CLEAN.

---

## §3.9 Wave C Acceptance Predicate Machine-Checkability

| Predicate | Machine-runnable? | Blocker if any |
|---|---|---|
| P1.1 — "Schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain" | NO — Phase B dependency | Test fixture does not exist. Hamel-binary form is correct; the predicate is well-formed but non-executable in Phase A. Gap acknowledged in document. |
| P1.2 — "Lint run on last 50 commits produces 0 false positives AND flags any malformed commit" | YES in principle; BLOCKED by implementation | `pre-commit-format.sh` and `/lint --check-commit-format` are designed but not yet written as implemented files. Once implemented, predicate is a valid bash one-liner. |
| P1.3 — "Test exits 0 when run against both skills; exits non-zero with specific syscall name" | YES in principle; BLOCKED by K10 | `unshare -n` availability on production server unconfirmed. HARD GAP correctly declared. |

All three predicates are Hamel-binary. None are prose predicates. The document correctly labels
each with its satisfaction status.

---

## Verdict Summary

**FLAG-MINOR** — 5 gaps, all mechanical, all fixable in <30 minutes:

1. DRY: regex repeated in 4 locations without cross-reference to §I.2 canonical source
2. SLI label: §B.1 SLI target values and §J burn-rate tiers need "calibration parameter / starter
   value for Part 8 adoption" labels to honour Part 8 boundary and Part 1's own §F.2 anti-scope
3. Schema: `task-return-packet.json` stub missing `required` array for the load-bearing
   `git_commit_hash` field
4. §K: 3 latent failure modes absent (concurrent commit lock, disk-full, fork schema drift)
5. §L P1.1: test fixture absence not given HARD GAP designation or Kx tracking entry

**No FAIL conditions triggered:**
- Zero scope-creep violations: §F.2 explicitly disclaims SLO ownership; the §B.1 labeling gap
  is a presentation issue, not a structural Part 8 boundary violation
- Zero broken citations: all `[src:...]` references point to real paths within the cycle or
  decisions/ tree
- Zero A.14 bare-dependency violations: §D is clean

**Contradiction resolutions visible:**
- C1 (swarm/lib ownership): RESOLVED, VISIBLE in §H.1
- C2 (Part 8 health-signal schema): PARTIALLY RESOLVED — §F.2 correct; §B.1 needs labeling fix
- C4 (PhaseOf → methodologically-uses): RESOLVED, VISIBLE in §D.2
