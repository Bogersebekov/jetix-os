---
title: Execution Prompt — Cycle-2 Implementation (OPP-01 + OPP-02 + OPP-04 + HD-01 + HD-02)
date: 2026-04-24
type: execution-prompt
author: Claude Code on server (cycle-1 brigadier handoff to fresh CC executor)
target_executor: A FRESH Claude Code session on this repo (claude/jolly-margulis-915d34)
output: artefacts as specified per Part below; final report at decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-XX.md
estimated_duration: 18-26 active turns across the 5 OPPs + verification + Stage-Gated pause
precedes: T-cycle-2-execution → opens M3 task brief once Part G report acked
defers: M3 solo-vs-matrix experiment (separate task; runs AFTER OPP-01 lands AND HITL ack of report)
upstream_brief: prompts/meta-brief-cycle-2-implementation-2026-04-24.md
authoritative_specs:
  - decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md
  - decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md
  - swarm/lib/shared-protocols.md
  - .claude/agents/brigadier.md
binding_scope: cycle-2 implementation only
state: ready-to-execute
operating_mode: Stage-Gated (AWAITING-APPROVAL pause between Part F verification and Part G report)
---

# Cycle-2 Implementation Execution Prompt

> Read this file end-to-end **before** writing a single byte to the repo. The
> implementation order in §2 is non-negotiable. The Stage-Gated pause in §5
> is non-negotiable. The Max-subscription discipline in §4 is non-negotiable.

---

## §1 Mission + critical framing (read this twice)

You are a fresh Claude Code session opened on the `claude/jolly-margulis-915d34`
branch of the Jetix OS repo. The prior cycle (cyc-swarm-self-improve-v1) closed
with 4 implement-now opportunities (OPP-01, OPP-02, OPP-04, M3) plus 2 HITL
decisions (HD-01, HD-02). Ruslan's Gate-2 ack landed on **2026-04-24** with this
specific shape:

| ID | Decision | What that means for this session |
|---|---|---|
| OPP-04 | APPROVE FIRST (cheapest, true-antifragile) | Implement before everything else (3 turns) |
| OPP-01 | APPROVE (root infra) | Implement second; M3 substrate depends on it |
| OPP-02 | APPROVE (Ruslan overrode "defer" recommendation) | Implement third; honor his decision, do not re-litigate |
| HD-01 | Option C (5-gate, scalability tables updated) | Implement fourth; one nominal-state declaration |
| HD-02 | Option A (N=2 per cycle: 1 structural + 1 measurement) | Implement fifth; protects Ruslan's attention budget |
| M3 | DEFER to separate next task | DO NOT execute in this session |
| OPP-03 / OPP-05 / OPP-06 | Cycle-2 queue (later) | DO NOT touch in this session |

**This implementation session is THE validation moment for Phase A swarm.**
Every OPP you implement shapes whether Cycle-3+ measurements produce signal or
noise. Shallow wiring = broken signal forever. The standing directive is
**1000% depth on each implementation**. There is no "good enough" pass: every
hook script, every schema field, every horizon-table entry is load-bearing for
months of downstream cycles. Optimize for permanence, not for speed.

**What "1000% depth" means concretely:**

1. YAML frontmatter complete on every new `.md` (CLAUDE.md "File Conventions" +
   `.claude/rules/global.md`). No partial frontmatter.
2. Every Bash script: passes `bash -n` + `chmod +x` + `#!/usr/bin/env bash` +
   `set -euo pipefail` + 1-line purpose/invocation comment.
3. Every schema diff to brigadier.md / 5 expert files is shown as BEFORE/AFTER
   block in the commit message, not just inline `Edit()`. Git log = provenance.
4. Every agent-file text-fix leaves surrounding section coherent (no orphaned
   refs, no broken §-numbers, no dangling table cells).
5. Every JSONL skeleton is schema-valid (empty file OK; malformed JSON NOT OK).
6. Every health-counter wire survives 100 cycles without manual intervention.

If you catch yourself thinking "close enough" — stop, re-read the artefact, tighten.

**Disqualifying anti-patterns:** empty `.sh` files; frontmatter missing
id/type/created/pipeline/state; hooks with undefined env var refs without
fallback; `cell_acceptance_predicate:` examples that match the anti-regex;
HD-01 €50K added in some agents but not others (breaks Option-C convergence);
HD-02 rule without health.md counter (unenforced).

Read this section twice. Then proceed to §2.

---

## §2 Scope — implementation order is fixed

**Implement in this exact order:** Part C → Part A → Part B → Part D → Part E.
Then Part F (verification) → AWAITING-APPROVAL pause → Part G (report) on ack.

The order is set by Ruslan's Gate-2 directive: **OPP-04 first** (cheapest +
highest-quality + zero deps), then OPP-01 (root infra), then OPP-02 (depends on
OPP-01 substrate), then HD-01 (touches all 5 agents + brigadier; do after OPPs
so you don't churn agent files mid-OPP-04), then HD-02 (touches brigadier +
health.md only; small).

If you encounter a true cross-Part contradiction (a decision in Part D would
require unwriting work in Part A), STOP and follow the §8 escalation. Do not
silently re-order.

---

### Part C — OPP-04 `cell_acceptance_predicate` (3 turns, FIRST)

**Source spec:** `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md` (655 lines — read §1, §3.1, §3.2, §3.3, §3.4, §8, §9 in full before starting). Cross-reference: OPPORTUNITIES §4.

**Why first:** 3 turns, schema-only, zero upstream deps, true antifragile (gains
value as cell count grows per systems-scalability-01.md §1 + §3 OPP-04 row),
closes root-cause of 8/8 conformance failures from cycle-1 (mgmt-critic-01.md
§2 C-1).

**Physical deliverables:**

#### C.1 — `.claude/agents/brigadier.md` §3.3 schema diff

Read `.claude/agents/brigadier.md:408-435` for the current §3.3 PMBOK WBS
discipline block. The `decomposition:` YAML at lines 418-429 currently has 4
fields per cell: `cell`, `ap_cost`, `ap_budget`, `inputs`, `expected_artefact`.
Add a 5th REQUIRED field `cell_acceptance_predicate:` AFTER `expected_artefact:`
in EACH cell template entry.

**Exact AFTER-state for the schema example** (apply to BOTH cells in the example
block at lines 419-428):

```yaml
decomposition:
  - cell: engineering × critic
    ap_cost: 50000        # estimated tokens
    ap_budget: 75000      # max-turn budget per §8 termination-stack
    inputs: [<file-paths from manifest.yaml>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-critic-<artefact-slug>.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks AND ≥2 Alternatives AND Anti-scope section AND each H-N row carries (F, ClaimScope, R) triple"   # NEW (OPP-04, cycle-2-impl)
  - cell: engineering × integrator
    ap_cost: 30000
    ap_budget: 50000
    inputs: [<paths>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-integrator-<slug>.md
    cell_acceptance_predicate: "Returns ≥3 cross-claim syntheses AND ≥1 D-NN preserved-dissent block AND Structured Output Packet per shared-protocols §3"   # NEW (OPP-04, cycle-2-impl)
```

The two example predicates above are themselves Hamel-binary, 20-200 chars each,
and do NOT match the anti-regex. They are the canonical example for the schema —
treat them as part of the spec.

**Add an inline comment immediately after the `decomposition:` block** explaining
the upgrade path so future-you knows when to migrate to a structured block:

```yaml
# cell_acceptance_predicate: string field is the Phase-A form (OPP-04, cycle-2-impl).
# At €1M horizon, when ≥3 distinct cell predicates per cycle reference swarm/evals/
# or health.md paths, migrate to a structured block:
#   cell_acceptance_predicate:
#     condition: <text>
#     measurement_path: <swarm/evals/... or health.md counter>
#     baseline_required: <true|false>
# Per systems-scalability-01.md §3 OPP-04 MHT event (natural antifragile evolution).
# OPP-05 falsifier: field is a parallel pattern (different LOC target — hypothesis
# artefacts). Do NOT bundle; OPP-05 is Cycle-3+ work.
```

#### C.2 — `.claude/agents/brigadier.md` §4.1 pre-dispatch checklist addition

Find the §4.1 "Task() schema (canonical)" block (starts at line 458). After the
existing schema block, add a "Pre-dispatch checklist" subsection that brigadier
reads before invoking each `Task()`. Per OPP-04 artefact §3.2, the addition is:

```markdown
**Pre-dispatch checklist (brigadier, per cell):**
1. `ap_cost` and `ap_budget` are non-zero integers.
2. `expected_artefact` path is inside `swarm/wiki/drafts/<task-id>-*` glob (write-scope-guard, per OPP-02).
3. `cell_acceptance_predicate` is non-empty string, length 20-200 chars, and does NOT consist solely of "artefact exists" or "file is non-empty" or any artefact-existence variant (anti-regex per /lint check #13). If missing or trivial: REFUSE dispatch with structured return `{status: refused, reason: "cell_acceptance_predicate absent or trivial", ap_code: AP-MGMT-1, cell: <cell-name>}`. (OPP-04, cycle-2-impl)
```

#### C.3 — `/lint` check #13 wiring

Read `.claude/skills/lint.md` (if it exists) to understand current check
numbering. If the file does not exist or is shorter than 12 checks, append a
section "Check #13 — cell_acceptance_predicate present in all WBS cells" with
the exact content from OPP-04 artefact §3.3 (lines 213-240 of that file). The
two slugs are:

- **`cell-ap-missing`** — field absent in ≥1 cell row in
  `swarm/wiki/proposals/*-decomposition.md`.
- **`cell-ap-trivial`** — field present but fails `^.{20,200}$` length regex
  OR matches the anti-regex (case-insensitive):
  `^(artefact exists|file is non-empty|file exists|expected_artefact returned|non-empty file|returns output|2[x×]( improvement)?( vs baseline)?$)`.

**Bash one-liner template** to embed in lint.md (target ~25 lines):

For every `swarm/wiki/proposals/*-decomposition.md`:
1. Count `^ *- cell:` (cell count) vs `^ *cell_acceptance_predicate:` (predicate
   count). If preds < cells → emit `FAIL cell-ap-missing` to stderr + `exit 1`.
2. For each predicate value: extract via `sed -E 's/^ *cell_acceptance_predicate: *//; s/^"//; s/"$//'`;
   check length 20-200 (else `FAIL cell-ap-trivial`); check anti-regex
   `^(artefact exists|file is non-empty|file exists|expected_artefact returned|non-empty file|returns output|2[x×])` (case-insensitive; else `FAIL cell-ap-trivial`).
3. Pass-all → `echo "OK"` + `exit 0`.

If `.claude/skills/lint.md` does not exist, create it as a stub with a brief
header explaining its purpose (per CLAUDE.md skill conventions), then add the
check #13 block as the first numbered check. Mark a TODO at the top:
`# TODO(cycle-3+): backfill checks 1..12 from prior /lint design notes`.

#### C.4 — Test fixtures (5 files in `swarm/wiki/tasks/_tests/`)

Create `swarm/wiki/tasks/_tests/` directory if it does not exist. Inside,
create 5 minimal `*-decomposition.md` test files:

| File | Expected check #13 result | Purpose |
|---|---|---|
| `test-ap-pass-1.md` | PASS | 2 cells, both with valid 50-100 char predicates |
| `test-ap-pass-2.md` | PASS | 5 cells, all with valid predicates referencing different artefact types |
| `test-ap-pass-3.md` | PASS | 1 cell with a 195-char predicate (boundary) |
| `test-ap-fail-missing.md` | FAIL `cell-ap-missing` | 3 cells, only 2 have the field |
| `test-ap-fail-trivial.md` | FAIL `cell-ap-trivial` | 2 cells, one predicate is "artefact exists" |

Each file must have full frontmatter:

```yaml
---
id: test-ap-<slug>
type: test-fixture
test_target: lint-check-13
expected_outcome: <pass|fail-missing|fail-trivial>
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Test fixture for /lint check #13 (cell_acceptance_predicate). Created by OPP-04 cycle-2-impl."
---
```

Body content: a minimal `decomposition:` YAML block matching the brigadier §3.3
schema, with the cells configured to produce the expected outcome. Bodies should
be ≤30 lines each.

#### C.5 — Explicit non-deletion declaration (anti-scope)

Add a single comment line in `.claude/agents/brigadier.md` §3.3 (right after
the inline upgrade-path comment from C.1):

```yaml
# OPP-05 (falsifier: field on hypothesis artefacts) is a parallel pattern at a
# DIFFERENT LOC target (swarm/wiki/tasks/<task-id>/artefacts/*.md, not
# swarm/wiki/proposals/*-decomposition.md). Do NOT bundle. OPP-05 lift is trivial
# once OPP-04 lands — clone /lint check #13 → check #14 with `falsifier:` slug.
```

This declaration prevents Cycle-3+ executors from "tidying up" by merging the
two patterns. The LOC separation is the design.

#### C.6 — Verification (Part C internal smoke)

Before committing Part C, run:

```bash
# C-VERIFY-1: schema field present in 2 example cells in brigadier §3.3
test "$(grep -c "cell_acceptance_predicate:" .claude/agents/brigadier.md)" -ge 4
# (4 = 2 example cells × 1 field each in C.1 + 1 in C.2 checklist + 1 in C.5 anti-scope comment)

# C-VERIFY-2: pre-dispatch checklist has the refusal rule
grep -q "AP-MGMT-1" .claude/agents/brigadier.md

# C-VERIFY-3: /lint check #13 file present
test -f .claude/skills/lint.md
grep -q "cell-ap-missing" .claude/skills/lint.md
grep -q "cell-ap-trivial" .claude/skills/lint.md

# C-VERIFY-4: 5 test fixtures
test "$(ls swarm/wiki/tasks/_tests/test-ap-*.md 2>/dev/null | wc -l)" -eq 5

# C-VERIFY-5: All test fixtures have valid frontmatter
for f in swarm/wiki/tasks/_tests/test-ap-*.md; do
  grep -q "^expected_outcome:" "$f" || { echo "FAIL: $f missing expected_outcome"; exit 1; }
done
```

All five must pass. If any fails, fix before commit.

#### C.7 — Commit

```
[cycle-2-impl] OPP-04 cell_acceptance_predicate landed

- brigadier.md §3.3: cell_acceptance_predicate added to WBS schema (string, 20-200 chars)
- brigadier.md §4.1: pre-dispatch checklist with AP-MGMT-1 refusal rule
- .claude/skills/lint.md: /lint check #13 (cell-ap-missing + cell-ap-trivial)
- swarm/wiki/tasks/_tests/: 5 test fixtures (3 pass, 2 fail)
- Anti-scope: OPP-05 falsifier: stays separate (different LOC target)
```

Push immediately after commit.

---

### Part A — OPP-01 `swarm/evals/` eval harness (6-8 turns)

**Source spec:** `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md` (781 lines — treat as authoritative; read §3 directory layout, §3 schema.md, §3 run.sh scaffold, §11 Cycle-1 smoke criteria in full). Cross-reference: OPPORTUNITIES §2.

**Why second:** Root-node infrastructure for FPAR signals; OPP-02 hook layer
needs the JSONL substrate to log enforcement events; M3 (separate task) needs
`swarm/evals/golden/solo-vs-matrix/` substrate.

**Physical deliverables (mapped 1:1 to meta-brief Part A):**

#### A.1 — `swarm/evals/` directory tree

Create the tree exactly as shown in OPP-01 artefact §3 (lines 132-147), adapted
to add the `cells/`, `golden/`, `health-hooks/` subdirs from the meta-brief.
Final tree:

```
swarm/evals/
├── README.md                       # ≥30 lines; usage + integration with OPP-02 + M3 + cycle-close hook
├── schema.md                       # canonical JSONL record schema (per A.2 below)
├── run.sh                          # eval runner; aggregates */results.jsonl; exits 0/1
├── cells/                          # per-cell results (lazy-created; day-1 has 3 seed dirs)
│   ├── systems-critic/
│   │   ├── golden-set.jsonl       # ≥1 seed entry from cycle-1 artefact
│   │   └── results.jsonl          # empty (created by run.sh on first eval)
│   ├── engineering-optimizer/
│   │   ├── golden-set.jsonl
│   │   └── results.jsonl
│   └── systems-integrator/
│       ├── golden-set.jsonl
│       └── results.jsonl
├── golden/
│   └── solo-vs-matrix/             # M3 substrate (empty stub; M3 task fills it)
│       └── README.md               # 5-line stub: "Reserved for M3 solo-vs-matrix experiment. See OPP-M3 spec."
└── health-hooks/                   # bash scripts that update swarm/wiki/meta/health.md
    ├── count-closed-cycles.sh
    ├── count-lint-findings.sh
    └── compute-fpar.sh
```

**README.md content** (≥30 lines, must include):

- Purpose statement: "OPP-01 eval harness — file-JSONL substrate closing Meadows L6 measurement void."
- Directory map (the tree above).
- Q2 single-writer note: "`swarm/evals/` is OUTSIDE `swarm/wiki/` so cells MAY append to their own `cells/<cell-id>/results.jsonl` without violating Q2." Verbatim from OPP-01 §11 Risk 3.
- Max-subscription note: "Pure Bash + Python stdlib only. Zero paid embeddings, zero vector DBs, zero provider API-key references." Verbatim from OPP-01 §10 Locks Honored.
- Integration list: 4 downstream consumers (golden-sets / health.md counters / PPR recall / skill pass-rate) per OPP-01 §1 Pitch.
- 1-line invocation example: `bash swarm/evals/run.sh` (exits 0 on empty corpus).

#### A.2 — `swarm/evals/schema.md` (6 required fields + optional versioned)

Write the schema per OPP-01 artefact §3 lines 154-219. The 6 required fields are
`cell_id`, `test_id`, `cycle_id`, `input_path`, `input_hash`, `expected_output_path`.
Plus required `expected_output_hash` and `acceptance_predicate` from the artefact
(total 8 required to match the artefact spec — meta-brief says "6 required" but
the artefact §3 schema declares 8 required; **honor the artefact**, document the
discrepancy in your Part G report). Optional/versioned: `actual_output_path`,
`pass`, `notes`, `timestamp`.

Use the YAML schema block verbatim from OPP-01 §3 lines 156-219. At the end of
the file, add a Section B header:

```yaml
# Section B — skill manifest fields (Fowler Extract Class shared-consumer)
# This schema also serves as the manifest format for
# swarm/wiki/skills/candidates/<slug>/manifest.md (golden_set_path field).
# One schema; two consumers. Section A (above) covers eval JSONL records;
# Section B (below) covers skill candidate manifests.
#
# Skill manifest fields (additive to Section A):
#   slug:                  string (required)
#   golden_set_path:       string (required) — relative path to swarm/evals/<cell-id>/golden-set.jsonl
#   activation_threshold:  float (default 0.70) — pass-rate floor for promotion
#   min_entries:           int (default 20) — entry-count floor for statistical validity
```

The Section A / Section B split is from OPP-01 §11 Risk 4 ("schema.md shared-
consumer coupling"). Honor it.

#### A.3 — `swarm/evals/run.sh` (≥55 lines, Bash + Python stdlib)

Use the scaffold from OPP-01 artefact §3 lines 222-285 verbatim, with these
specific augmentations:

1. **Add `min_entries: 20` warning logic.** Per OPP-01 §3 line 292-294:
   when total JSONL entries across all cells < 20, emit
   `WARN: golden-set floor not reached (have N, need 20); measurements not yet statistically meaningful`
   to stderr but do NOT fail.

2. **Append-only invariant for results.jsonl** (OPP-01 §3 line 295-296). The
   scaffold already uses `>>` not `>` — verify it stays that way.

3. **Exit code semantics:** `exit 0` on empty corpus (no golden-sets found =
   not a failure, just no work). `exit 0` on all-pass. `exit 1` on any FAIL.
   Smoke test: `bash swarm/evals/run.sh` immediately after creation must
   `echo $?` → `0`.

4. **No `ANTHROPIC_API_KEY` / `GROQ_API_KEY` / etc references.** Per CLAUDE.md
   Max-subscription discipline + shared-protocols §9. `grep -r "API_KEY" swarm/evals/`
   must return zero hits.

After writing, run `bash -n swarm/evals/run.sh` (must pass), `chmod +x swarm/evals/run.sh`,
and `bash swarm/evals/run.sh` (must `exit 0`).

#### A.4 — Per-cell `results.jsonl` skeletons + 3 day-1 golden-set seeds

Create empty `results.jsonl` files in 3 seed cell dirs (`cells/systems-critic/`,
`cells/engineering-optimizer/`, `cells/systems-integrator/`). Empty file is
schema-valid (zero records).

Seed `golden-set.jsonl` with the 3 entries from OPP-01 §3 lines 305-318
verbatim. The hashes will be `<computed-at-install>` placeholders for now; in
this session, **compute real sha256 hashes** for the input/expected_output paths
referenced and substitute them in. Use:

```bash
sha256sum swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md | cut -d' ' -f1
sha256sum swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md | cut -d' ' -f1
# (etc. for all 6 path/hash pairs across the 3 seed entries)
```

If any of those source files do not exist, replace the seed with a different
existing artefact from this cycle (the goal is 3 valid seed records, not
necessarily the exact ones in the spec). Document the substitution in the
Part G report.

#### A.5 — Health-hook scripts (3 files, lint-clean)

**`swarm/evals/health-hooks/count-closed-cycles.sh`** (10-15 lines): walks
`swarm/wiki/tasks/T-*/operations/cycle-*.md`; emits count to stdout. Used by
cycle-close ritual to update `health.md closed_cycles_count`.

**`swarm/evals/health-hooks/count-lint-findings.sh`** (12-18 lines): reads
`swarm/evals/lint-findings.jsonl` (created by `/lint`); counts entries from
most-recent `run_id` group; emits `0` if file absent. Used by cycle-close to
update `health.md lint_findings_count`.

**`swarm/evals/health-hooks/compute-fpar.sh`** (15-25 lines): walks
`swarm/evals/cells/*/results.jsonl`; computes FPAR = `sum(pass=true) /
sum(total)` via Python stdlib JSON parse; emits `0.00` on empty corpus.
Used by cycle-close to update `health.md fpar_log`.

Each script must:
- pass `bash -n` (syntax check)
- have executable bit set (`chmod +x`)
- reference no API keys
- emit a single value to stdout (a number) and zero stderr noise on the empty-corpus path

#### A.6 — Smoke verification (Part A internal)

Before committing Part A, run all 7 OPP-01 SMOKE checks from artefact §11
lines 631-639. Adapted for this implementation:

```bash
# A-SMOKE-1: directory exists
test -d swarm/evals/

# A-SMOKE-2: schema.md exists with ≥20 lines
test "$(wc -l < swarm/evals/schema.md)" -ge 20

# A-SMOKE-3: run.sh exists with ≥55 lines and is executable
test "$(wc -l < swarm/evals/run.sh)" -ge 55
test -x swarm/evals/run.sh

# A-SMOKE-4: ≥3 cell dirs with golden-set.jsonl
test "$(find swarm/evals/cells -name golden-set.jsonl | wc -l)" -ge 3

# A-SMOKE-5: total JSONL entries ≥3 across all golden-sets
total=0
for f in swarm/evals/cells/*/golden-set.jsonl; do
  total=$((total + $(wc -l < "$f")))
done
test "$total" -ge 3

# A-SMOKE-6: bash run.sh exits 0
bash swarm/evals/run.sh; test "$?" -eq 0

# A-SMOKE-7: health-hooks present and lint-clean
for h in count-closed-cycles.sh count-lint-findings.sh compute-fpar.sh; do
  test -x "swarm/evals/health-hooks/$h"
  bash -n "swarm/evals/health-hooks/$h"
done
```

All 7 must pass. If any fails, fix before commit.

#### A.7 — Commit

```
[cycle-2-impl] OPP-01 eval harness infrastructure

- swarm/evals/{README.md, schema.md, run.sh}: file-JSONL substrate (Bash + Python stdlib)
- swarm/evals/cells/{systems-critic, engineering-optimizer, systems-integrator}/: 3 seed dirs with golden-set.jsonl + empty results.jsonl
- swarm/evals/golden/solo-vs-matrix/README.md: M3 substrate stub
- swarm/evals/health-hooks/: 3 scripts (count-closed-cycles, count-lint-findings, compute-fpar)
- All SMOKE-1..SMOKE-7 pass; run.sh exits 0 on empty corpus
- Anti-scope: NO PostToolUse lint hook (OPP-02 owns), NO /compound (OPP-03 Cycle-3+), NO M3 execution
```

Push immediately.

---

### Part B — OPP-02 hook layer (6-12 turns)

**Source spec:** `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md` (725 lines — read §3 sub-components 1/2/3, §3.4 fallback path, §3.5 OPP-01 integration, §8 risk table, §9 effort table in full). Cross-reference: OPPORTUNITIES §3.

**Why third:** Depends on OPP-01 (logs to `swarm/evals/`); enforcement adds
gate-discipline; Ruslan explicitly overrode the "defer" recommendation, so this
is implemented in **log-only mode** for Cycle-2 (warn, exit 0) per meta-brief
Part B item 2-4. Blocking upgrade is a Cycle-3+ decision after OPP-01 health
counters produce signal.

**MANDATORY FIRST STEP (Part B blocker):**

#### B.0 — Hook API availability pre-check

Per OPP-02 artefact §3.0 lines 122-136. Run this verification BEFORE writing
any hook scripts. The result determines whether you implement the hook-native
path (Alternative A) or the Bash-wrapper fallback (Alternative B).

```bash
# Step 1: read current settings.json
cat .claude/settings.json 2>/dev/null || echo "no settings.json"

# Step 2: check for existing hooks key
grep -q "\"hooks\"" .claude/settings.json 2>/dev/null && echo "hooks key present" || echo "hooks key absent"

# Step 3: attempt no-op hook entry validation
# (write a temp settings.json with a UserPromptSubmit no-op; if Claude Code
#  parses it without error on next launch, hook API is available.)
```

**Decision rule:**
- If `.claude/settings.json` already has a `"hooks"` key with `UserPromptSubmit`
  or `PostToolUse` entries → **API available → Alternative A**.
- If you can add a `"hooks"` key without breaking existing config (validate by
  re-reading the file after edit + checking it's still valid JSON via
  `python3 -m json.tool .claude/settings.json`) → **API likely available → Alternative A**.
- If `.claude/settings.json` does not exist OR is structurally fragile (e.g. has
  comments inside JSON, has trailing commas, etc.) → **fallback to Alternative B**.

**Document the verdict explicitly:** Write your verdict to a 1-line entry in
your scratchpad before proceeding. The Part G report MUST include the verdict
+ evidence (which file you read, what you found, why you chose A vs B).

**Default if uncertain:** Choose Alternative B (Bash-wrapper) — it provides
equivalent enforcement semantics for Phase-A sequential dispatch (per OPP-02
§5 Alternative B) and avoids API-availability risk. You can always upgrade to
Alternative A in a later cycle once the hook API is empirically confirmed.

#### B.1 — `.claude/hooks/mode-prefix.sh` (mode-prefix regex check)

Per OPP-02 artefact §3.1 lines 140-184. Path placement: meta-brief says
`.claude/hooks/mode-prefix.sh`, OPP-02 artefact says `swarm/lib/hooks/mode-prefix-validator.sh`.
**Honor the meta-brief path** (`.claude/hooks/mode-prefix.sh`) AND symlink it
from the artefact path:

```bash
mkdir -p .claude/hooks swarm/lib/hooks
# Write the script to .claude/hooks/mode-prefix.sh per spec
# Then:
ln -sf "$(realpath --relative-to=swarm/lib/hooks .claude/hooks/mode-prefix.sh)" swarm/lib/hooks/mode-prefix-validator.sh
```

**Script content** (target 20-28 lines; use OPP-02 §3.1 lines 140-184 spec
verbatim, with these augmentations):

- Read allowlist from `.claude/hooks/mode-prefix-allowlist.txt` (B.7); skip
  validation entirely if `$2` (agent name) matches any line.
- Append events as JSON to `swarm/evals/cells/hook-layer/events.jsonl` (mkdir
  -p the parent first).
- On mismatch: write `result:"warn"` event + stderr WARN message + `exit 0`
  (cycle-2 log-only; cycle-3+ may flip to `exit 1`).
- On match: write `result:"pass"` event + `exit 0`.

Skeleton:

```bash
#!/usr/bin/env bash
set -euo pipefail
PROMPT="${1:-}"; AGENT="${2:-unknown}"
EVENTS_LOG="swarm/evals/cells/hook-layer/events.jsonl"
mkdir -p "$(dirname "$EVENTS_LOG")"
# allowlist short-circuit
grep -qx "$AGENT" .claude/hooks/mode-prefix-allowlist.txt 2>/dev/null && exit 0
first_line=$(echo "$PROMPT" | sed -n '/[^[:space:]]/{p;q;}')
ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
if echo "$first_line" | grep -qE '^mode: (critic|optimizer|integrator|scalability)$'; then
  echo "{\"ts\":\"$ts\",\"component\":\"mode-prefix\",\"result\":\"pass\",\"agent\":\"$AGENT\"}" >> "$EVENTS_LOG"
else
  echo "{\"ts\":\"$ts\",\"component\":\"mode-prefix\",\"result\":\"warn\",\"agent\":\"$AGENT\",\"evidence\":\"$first_line\"}" >> "$EVENTS_LOG"
  echo "[WARN cycle-2 log-only] mode-prefix mismatch agent=$AGENT first_line=$first_line" >&2
fi
exit 0
```

#### B.2 — `.claude/hooks/role-matrix.sh` (role-tool-matrix pre-check)

Per OPP-02 artefact §3.2 lines 188-238 (write-scope-guard). Cycle-2 = log-only.

Path: `.claude/hooks/role-matrix.sh` + symlink at
`swarm/lib/hooks/write-scope-guard.sh`. Target 22-30 lines. Per OPP-02 §3.2
lines 188-238. Augmentations:

- `$ROLE` from `$CLAUDE_AGENT_ROLE` env var or `$1` fallback.
- `$WRITE_PATH` from `$CLAUDE_TOOL_INPUT_PATH` or `$2`.
- `brigadier` role short-circuits to `exit 0` (full write access).
- Empty path or unknown agent file → `exit 0` (pass-through cycle-2).
- Use `bash swarm/lib/hooks/parse-frontmatter-field.sh "$agent_file" "write_scope_glob"` to extract glob.
- Empty glob → log warn + `exit 0` (cycle-2 fail-safe per OPP-02 §8 risk-mitigation row 6).
- Use `shopt -s extglob; case "$WRITE_PATH" in $glob) ...; *) ...; esac` for matching.
- Always `exit 0` in cycle-2 (log-only); cycle-3+ may flip mismatch case to `exit 1`.

#### B.3 — `.claude/hooks/verify-packet.sh` (return-packet verifier)

Per OPP-02 artefact §3.3 lines 242-279. Cycle-2 = log-only. Target 35-50 lines.
4 checks per OPP-02 §3.3:

1. **sources[] non-empty** — `grep -A1 "^sources:" "$DRAFT" | sed -n '2p'`
   must start with `- ` (list item).
2. **confidence_method present** — `grep -qE "^confidence_method:[[:space:]]*\S+" "$DRAFT"`.
3. **type present** — `grep -qE "^type:[[:space:]]*\S+" "$DRAFT"`.
4. **body length + sources combined** — body chars > 500 AND sources empty
   = AP-1 lock violation per meta-brief Part B item 4.

Behavior:
- Filter via `case "$DRAFT" in swarm/wiki/drafts/*) ;; *) exit 0 ;; esac`.
- Collect violations into a Bash array.
- Each violation → JSONL `result:"warn"` event + stderr WARN line + `exit 0`.
- All-pass → `result:"pass"` event + `exit 0`.
- Cycle-2 NEVER exits non-zero; cycle-3+ may flip on AP-1 violations.

#### B.4 — `swarm/lib/hooks/parse-frontmatter-field.sh` (shared helper)

Per OPP-02 §3.2 lines 232-238 (Fowler Extract Function). Target 10-15 lines.
Usage: `parse-frontmatter-field.sh <file> <field-name>`. Extracts single-line
scalar field from YAML frontmatter (between first two `---` markers); strips
surrounding quotes; emits empty string if field absent or multi-line. Use
`awk` with frontmatter-bound counter (`/^---$/ { n++; next }`).

#### B.5 — `.claude/settings.json` updates (Alternative A) OR fallback wrapper (Alternative B)

**If Alternative A (hook API available):**

Read `.claude/settings.json`. Validate via `python3 -m json.tool`. Add a `"hooks"`
key (or augment existing) with two matchers:

- `UserPromptSubmit` matcher `Task` → runs `bash .claude/hooks/mode-prefix.sh "$CLAUDE_USER_PROMPT" "$CLAUDE_AGENT_ROLE"`.
- `PostToolUse` matcher `Write` → runs both `role-matrix.sh` and `verify-packet.sh`
  (in that order).

Preserve all existing keys verbatim — do NOT replace the file, only add entries.
Re-validate after edit; if validation fails, revert and fall back to Alternative B.

**If Alternative B (Bash wrapper, hook API unavailable or risky):**

Write `swarm/lib/hooks/pre-session-check.sh` per OPP-02 artefact §3.4
lines 285-309 verbatim. Then add a single sentence to `.claude/agents/brigadier.md`
§4.2 (find "Mode-prefix mandate" or equivalent line; add after it):

```markdown
**Brigadier MUST run `bash swarm/lib/hooks/pre-session-check.sh` at session start AND `bash .claude/hooks/mode-prefix.sh "<prompt>" "<agent>"` before each Task() dispatch (cycle-2 log-only mode per OPP-02 fallback path).** (cycle-2-impl OPP-02 Alt-B)
```

Document in your Part G report which path you took and why.

#### B.6 — Log substrate dependency on OPP-01

The hook scripts write to `swarm/evals/cells/hook-layer/events.jsonl`. Create the
directory + empty file as part of Part B (OPP-01 only seeded 3 cells; hook-layer
is a 4th):

```bash
mkdir -p swarm/evals/cells/hook-layer
touch swarm/evals/cells/hook-layer/events.jsonl
touch swarm/evals/cells/hook-layer/results.jsonl
```

Also seed `swarm/evals/cells/hook-layer/golden-set.jsonl` with 3 entries per
OPP-02 §3.5 (mode-prefix pass case, role-matrix fail case, verify-packet fail case).

#### B.7 — Allowlist for 5 known legitimate patterns

Per meta-brief Part B item 8. The 5 allowlist agents are already inline in B.1
(`manager`, `personal-assistant`, `system-admin`, `inbox-processor`, `crazy-agent`).
Externalize to `.claude/hooks/mode-prefix-allowlist.txt` for future-tuning:

```
# Cycle-2 OPP-02 mode-prefix allowlist
# One agent name per line; mode-prefix.sh exits 0 immediately for any match.
# Add only AFTER documenting reason in .claude/hooks/allowlist-rationale.md.
manager
personal-assistant
system-admin
inbox-processor
crazy-agent
```

Update B.1 script to read from this file (replace the hard-coded array). Document
the design choice in Part G report.

#### B.8 — Verification (Part B internal)

```bash
# B-VERIFY-1: 3 hook scripts exist + executable + bash -n clean
for h in mode-prefix.sh role-matrix.sh verify-packet.sh; do
  test -x ".claude/hooks/$h"
  bash -n ".claude/hooks/$h"
done

# B-VERIFY-2: shared helper present
test -x swarm/lib/hooks/parse-frontmatter-field.sh
bash -n swarm/lib/hooks/parse-frontmatter-field.sh

# B-VERIFY-3: settings.json valid JSON (Alt-A) OR pre-session-check.sh exists (Alt-B)
python3 -m json.tool .claude/settings.json > /dev/null 2>&1 || test -x swarm/lib/hooks/pre-session-check.sh

# B-VERIFY-4: log substrate created
test -d swarm/evals/cells/hook-layer
test -f swarm/evals/cells/hook-layer/events.jsonl
test "$(wc -l < swarm/evals/cells/hook-layer/golden-set.jsonl)" -ge 3

# B-VERIFY-5: allowlist file present
test -f .claude/hooks/mode-prefix-allowlist.txt
test "$(wc -l < .claude/hooks/mode-prefix-allowlist.txt)" -ge 5

# B-VERIFY-6: smoke-fire each hook once and confirm event log grows
before=$(wc -l < swarm/evals/cells/hook-layer/events.jsonl)
echo "mode: critic" | bash .claude/hooks/mode-prefix.sh "$(cat)" engineering-expert
after=$(wc -l < swarm/evals/cells/hook-layer/events.jsonl)
test "$after" -gt "$before"
```

All 6 must pass.

#### B.9 — Commit

```
[cycle-2-impl] OPP-02 hook layer (log-only mode)

- .claude/hooks/{mode-prefix, role-matrix, verify-packet}.sh: 3 enforcement scripts
- swarm/lib/hooks/parse-frontmatter-field.sh: Fowler Extract Function shared helper
- .claude/settings.json (Alt-A) OR swarm/lib/hooks/pre-session-check.sh (Alt-B): wiring path
- swarm/evals/cells/hook-layer/: events.jsonl + golden-set.jsonl seeded (3 entries)
- .claude/hooks/mode-prefix-allowlist.txt: 5 known legitimate non-matrix agents
- CYCLE-2 mode = log-only (warn + exit 0); blocking upgrade is Cycle-3+ HITL decision
- API verdict: <Alt-A | Alt-B with reason> — see Part G report for evidence
```

Push immediately.

---

### Part D — HD-01 €50K horizon-gate alignment, Option C (1-2 turns)

**Source spec:** OPPORTUNITIES §6 HD-01 Option C + systems-scalability-01.md §6
(5-gate vs 4-gate analysis, Option C verdict).

**Ruslan's directive:** "делай как лучше" → preferred = Option C (5-gate model
with §6.1 tables updated). systems-scalability-01.md §6 explicitly states
Option A/C is more scalability-coherent.

**Why fourth:** Touches all 5 expert agent files + brigadier; do AFTER Parts
A/B/C so you don't churn agent files mid-OPP work.

**Physical deliverables:**

#### D.1 — Add €50K gate to brigadier + 4 peer experts

Investor-expert ALREADY has 5 gates (€50K / €200K / €1M / $100M / $1T) — see
`.claude/agents/investor-expert.md:107` and `:301` and `:328`. **DO NOT TOUCH
investor-expert's existing €50K rows.**

For each of the 4 peer experts (engineering / mgmt / systems / philosophy) AND
brigadier, the current state is 4 gates (€200K / €1M / $100M / $1T). Add €50K
as the FIRST gate.

**Per-file edits required:**

**`.claude/agents/engineering-expert.md`:**
- Find `§6.1 BOSC-A-T-X trigger predicates per gate` (search for "BOSC-A-T-X" or "§6.1").
  If §6.1 has a 4-row gate table, add a new row at the TOP for €50K.
- Find any reference to `(€200K / €1M / $100M / $1T)` — replace with
  `(€50K / €200K / €1M / $100M / $1T)`.
- Find the §6 mode predicate line referencing the gates — add €50K.

**`.claude/agents/mgmt-expert.md`:**
- Find `§6.1 BOSC-A-T-X trigger predicates (per horizon gate)` at line ~1114.
- Add €50K row.
- Update §6 predicate at line ~1105 to include €50K.

**`.claude/agents/systems-expert.md`:**
- Find `§6.1 BOSC-A-T-X trigger predicates per gate` at line ~1177.
- Add €50K row.
- Update §6 predicate at line ~1175 to include €50K.

**`.claude/agents/philosophy-expert.md`:**
- Find `§6.1 BOSC-A-T-X trigger predicates per horizon gate` at line ~1087.
- Add €50K row.
- Update §6 predicate at line ~1085 to include €50K.

**`.claude/agents/brigadier.md`:**
- Find references to horizon gates in §3 and §5 (line ~398, ~542). Update any
  `(€200K / €1M / $100M / $1T)` to `(€50K / €200K / €1M / $100M / $1T)`.
- If brigadier has its own scalability §6.1 table, add €50K row.

**Canonical €50K row content** (use this verbatim, adapted per expert domain):

For systems-expert §6.1 the row should follow the existing column layout. Read
the current 4-row table first to see the column count and naming. The €50K row
content (template — adjust per-expert language):

```
| €50K | C+S (Composition + Scale) — current state; swarm installs measurement substrate; zero-to-operational transition; consulting-revenue runway from Q2 2026 (Ruslan's single committed absolute date per JETIX-PLAN D3) | Phase Promotion (artefact moves from spec-only to operational) |
```

Per-expert adaptation:
- **engineering**: trigger emphasizes "executor-not-wired closure" (MP-1) +
  enforcement primitives shipping.
- **mgmt**: trigger emphasizes "WBS acceptance gap closed" (C-04 in this cycle).
- **systems**: trigger emphasizes "L6 measurement void closed" (Meadows score 35.0).
- **philosophy**: trigger emphasizes "AP-PHIL-1 falsifier-substrate exists" via
  OPP-01 measurement path (D-03 partial resolution).
- **brigadier**: trigger emphasizes "spec-only → operational" swarm transition.

#### D.2 — Update scalability §6.1 tables in each agent file

Per HD-01 Option C: every OPP / decision now has a NAMED HOME GATE at €50K
(current state) / €200K / €1M / $100M / $1T. The scalability §6.1 table in each
agent file already has rows for the 4 existing gates; add €50K as a new row that
FILLS IN, not replaces.

For systems-expert, the BOSC-A-T-X table at line ~1196 currently has 4 rows.
After your edit it should have 5 rows. The €50K row is the "current state" anchor.

For each expert, also update the §6 predicate string that enumerates the gates
(e.g. systems-expert §6 line 1175, philosophy-expert §6 line 1085, mgmt-expert
§6 line 1105, engineering-expert §6 reference).

**Convergence target:** After D.1 + D.2, all 5 experts + brigadier reference the
same 5-gate set. Verify with:

```bash
# All 5 experts + brigadier mention €50K (Ruslan's first capital gate)
test "$(grep -l '€50K' .claude/agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md | wc -l)" -eq 6
```

#### D.3 — Ruslan rationale comment

In each of the 5 modified agent files (the 4 peer experts + brigadier;
investor-expert already has the €50K so no change), add a single comment line
adjacent to the €50K row in the §6.1 table:

```markdown
<!-- €50K is Ruslan's single committed absolute date (Q2 2026) per JETIX-PLAN D3.
     HD-01 Option C alignment (cycle-2-impl 2026-04-24): every scalability projection
     names a home gate at €50K. -->
```

#### D.4 — S-06 convergence metric verification

If `swarm/wiki/meta/` contains a convergence metric file (e.g.
`swarm/wiki/meta/horizon-convergence.md` or similar), update it to reflect
"5 agents aligned on 5 gates" status. If no such file exists, create
`swarm/wiki/meta/horizon-convergence.md` as a stub:

```markdown
---
id: horizon-convergence
type: meta-metric
created: 2026-04-24
pipeline: ingested
state: drafted
purpose: "Track convergence of horizon-gate references across all 5 expert agents + brigadier per HD-01 Option C."
---

# Horizon Convergence (S-06)

Per HD-01 Option C (Ruslan ack 2026-04-24, cycle-2-impl):

| Agent | €50K | €200K | €1M | $100M | $1T | Convergence |
|---|---|---|---|---|---|---|
| brigadier | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| engineering-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| mgmt-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| systems-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| philosophy-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| investor-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 (was already aligned pre-cycle-2) |

**Status:** S-06 convergence = 6/6 agents on 5/5 gates after cycle-2-impl HD-01 Option C.
```

#### D.5 — Verification (Part D internal)

```bash
# D-VERIFY-1: All 6 agent files reference €50K
test "$(grep -c '€50K' .claude/agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md | grep -v ':0' | wc -l)" -eq 6

# D-VERIFY-2: Investor's existing €50K rows are intact (touch-count in investor-expert.md
#  should be unchanged from pre-cycle-2; you can git diff to confirm zero changes
#  to investor-expert.md if you didn't touch it)
test "$(git diff --stat .claude/agents/investor-expert.md | wc -l)" -eq 0  # OR small if you only added a comment

# D-VERIFY-3: convergence metric file exists
test -f swarm/wiki/meta/horizon-convergence.md
grep -q "5/5" swarm/wiki/meta/horizon-convergence.md
```

#### D.6 — Commit

```
[cycle-2-impl] HD-01 €50K gate propagated to all agents

- engineering-expert.md, mgmt-expert.md, systems-expert.md, philosophy-expert.md, brigadier.md: €50K added as first horizon gate
- investor-expert.md: untouched (already had 5 gates)
- §6.1 BOSC-A-T-X tables updated in 4 peer experts + brigadier
- swarm/wiki/meta/horizon-convergence.md: S-06 metric (6/6 agents on 5/5 gates)
- Ruslan rationale comment: €50K is Q2 2026 single committed absolute date (JETIX-PLAN D3)
- HD-01 Option C per Ruslan ack 2026-04-24
```

Push immediately.

---

### Part E — HD-02 M-class rate limiter, Option A N=2 (1-2 turns)

**Source spec:** OPPORTUNITIES §6 HD-02 Option A.

**Why fifth:** Touches brigadier.md + health.md only; small surface; protects
Ruslan's attention budget across all future cycles.

**Physical deliverables:**

#### E.1 — Rate-limiter rule in `.claude/agents/brigadier.md`

Add a new subsection in §3.3 (PMBOK WBS) or as a §3.6 / §6 sub-rule.
Recommended placement: end of §3.3, after the `risk_register:` block.

```markdown
### §3.3.1 M-class rate limiter (HD-02 Option A, cycle-2-impl 2026-04-24)

Per cycle, brigadier MAY dispatch a MAXIMUM of **2 Method-class (M) tasks** —
specifically, **1 structural fix + 1 measurement fix** per cycle. Any 3rd+
M-class decomposition is REFUSED with structured return:

```yaml
status: refused
reason: "M-class rate limit hit (2/2 per cycle); queue this task for next cycle"
ap_code: AP-MGMT-RATE-LIMIT-M
overflow_log: swarm/wiki/operations/<cycle>/m-class-overflow.md
```

**Classification rule:** every decomposition cell must carry `class: M | B | O`
(Method / Business / Operational). Rate-limit applies ONLY to `class: M`.

- **M (Method):** changes how the swarm operates. Examples: hook layer,
  schema fields, lint checks, gate semantics, agent prompt edits.
- **B (Business):** capital-deploying or revenue-generating. Examples: pricing
  proposals, client deliverables, moat analyses for live offers.
- **O (Operational):** day-to-day execution. Examples: outreach drafts, daily
  logs, status reports, voice-memo triage.

**Why N=2 (Ruslan ack 2026-04-24, HD-02 Option A):** 1 structural + 1 measurement
fix per cycle protects Ruslan's attention budget. Self-perpetuating improvement
loops would otherwise saturate the gate-ack queue.

**Counter:** brigadier maintains `m_class_dispatched_this_cycle: N/2` in
`swarm/wiki/meta/health.md`. Reset to `0/2` at cycle-open.

**Failure mode:** When the M-limit is hit mid-cycle, the third+ M-class task is
queued for next cycle via append to `swarm/wiki/operations/<cycle-id>/m-class-overflow.md`
and an explicit log entry in `swarm/wiki/log.md`:

`## [<date>] m-class-overflow | <cycle-id> | <task-brief> | brigadier`
```

#### E.2 — Add `class:` field to WBS schema example

Edit the §3.3 `decomposition:` block (already touched in Part C). Add a new
field `class: M | B | O` after `cell:` in each example. Updated example:

```yaml
decomposition:
  - cell: engineering × critic
    class: M                            # NEW (HD-02 Option A, cycle-2-impl)
    ap_cost: 50000
    ap_budget: 75000
    inputs: [<file-paths from manifest.yaml>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-critic-<artefact-slug>.md
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks AND ≥2 Alternatives AND Anti-scope section AND each H-N row carries (F, ClaimScope, R) triple"
  - cell: engineering × integrator
    class: M
    ap_cost: 30000
    ap_budget: 50000
    inputs: [<paths>]
    expected_artefact: swarm/wiki/drafts/<task-id>-engineering-integrator-<slug>.md
    cell_acceptance_predicate: "Returns ≥3 cross-claim syntheses AND ≥1 D-NN preserved-dissent block AND Structured Output Packet per shared-protocols §3"
```

#### E.3 — Counter in `swarm/wiki/meta/health.md`

Read current `swarm/wiki/meta/health.md`. Add a new field/row to the counters
block:

```yaml
m_class_dispatched_this_cycle: 0   # /2 — HD-02 Option A rate limit (cycle-2-impl 2026-04-24)
m_class_overflow_total: 0          # cumulative across all cycles
```

If health.md is structured as a markdown table, add as a new row. If it's pure
YAML, add as new keys. Honor the existing structure.

#### E.4 — Failure mode doc

Create stub directory + readme for overflow handling:

```bash
mkdir -p swarm/wiki/operations
```

Add to `.claude/agents/brigadier.md` a new short section §6.4 (or appropriate
adjacent location near §6 HITL escalation rules):

```markdown
### §6.4 M-class overflow handling (HD-02, cycle-2-impl)

When a 3rd+ M-class decomposition is requested in a single cycle:

1. Reject the decomposition with `AP-MGMT-RATE-LIMIT-M` per §3.3.1.
2. Append to `swarm/wiki/operations/<cycle-id>/m-class-overflow.md`:
   ```
   ## <ISO-timestamp> | <task-brief-id> | <one-line description>
   ```
3. Append to `swarm/wiki/log.md`:
   `## [<date>] m-class-overflow | <cycle-id> | <task-brief> | brigadier`
4. Increment `m_class_overflow_total` in `swarm/wiki/meta/health.md`.
5. Surface to Ruslan in the next AWAITING-APPROVAL packet body.
```

#### E.5 — Verification (Part E internal)

```bash
# E-VERIFY-1: rate-limiter rule present in brigadier.md
grep -q "AP-MGMT-RATE-LIMIT-M" .claude/agents/brigadier.md
grep -q "m_class_dispatched_this_cycle" .claude/agents/brigadier.md

# E-VERIFY-2: counter present in health.md
grep -q "m_class_dispatched_this_cycle" swarm/wiki/meta/health.md

# E-VERIFY-3: class field in WBS example
grep -q "class: M" .claude/agents/brigadier.md

# E-VERIFY-4: overflow handling section
grep -q "§6.4 M-class overflow" .claude/agents/brigadier.md
test -d swarm/wiki/operations
```

All 4 must pass.

#### E.6 — Commit

```
[cycle-2-impl] HD-02 M-class rate limiter N=2 in brigadier

- brigadier.md §3.3.1: rate-limiter rule (max 2 M-class per cycle: 1 structural + 1 measurement)
- brigadier.md §3.3 WBS schema: class: M | B | O field added to cell template
- brigadier.md §6.4: overflow handling procedure (queue + log + counter increment)
- swarm/wiki/meta/health.md: m_class_dispatched_this_cycle + m_class_overflow_total counters
- HD-02 Option A per Ruslan ack 2026-04-24
- Anti-scope: NO automatic M-task generation, NO cost-accounting field (Option C)
```

Push immediately.

---

### Part F — Bootstrap verification (MANDATORY GATE before AWAITING-APPROVAL)

After Parts A-E are committed and pushed, run all 7 meta-brief Part F checks
plus the per-Part internal smoke checks one more time as a regression sweep.

#### F.1 — Cross-Part verification matrix

Run the following 7 checks in order. Each must produce the expected output. Fail
ANY = STOP, write `decisions/AMBIGUITY-cycle-2-implementation-2026-04-24.md`,
escalate per §8.

```bash
# F-CHECK-1: swarm/evals/ has 6 expected items (per meta-brief Part F item 1)
ls swarm/evals/ | sort
# Expected: README.md, schema.md, run.sh, cells, golden, health-hooks (6 items)

# F-CHECK-2: bash swarm/evals/run.sh exits 0 on (now-seeded) corpus
bash swarm/evals/run.sh; echo "exit=$?"
# Expected: exit=0

# F-CHECK-3: .claude/hooks/*.sh all exist + bash -n + executable
for h in .claude/hooks/*.sh; do
  test -x "$h" || { echo "FAIL: $h not executable"; exit 1; }
  bash -n "$h" || { echo "FAIL: $h syntax error"; exit 1; }
done
echo "all hooks OK"

# F-CHECK-4: cell_acceptance_predicate appears ≥2 times in brigadier.md (schema + example)
test "$(grep -c 'cell_acceptance_predicate' .claude/agents/brigadier.md)" -ge 2
echo "OPP-04 schema field present"

# F-CHECK-5: €50K appears in all 6 agent files (HD-01 Option C convergence)
hits=$(grep -lE '€50K' .claude/agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md | wc -l)
test "$hits" -eq 6
echo "HD-01 6/6 convergence"

# F-CHECK-6: m_class_dispatched_this_cycle in both brigadier + health.md
grep -q "m_class_dispatched_this_cycle" .claude/agents/brigadier.md
grep -q "m_class_dispatched_this_cycle" swarm/wiki/meta/health.md
echo "HD-02 counter wired"

# F-CHECK-7: /lint check #13 reports correctly on 5 test fixtures
# (run the inline Bash one-liner from C.3 against each fixture; expect:
#   test-ap-pass-{1,2,3} → exit 0
#   test-ap-fail-{missing,trivial} → exit 1)
for f in swarm/wiki/tasks/_tests/test-ap-pass-*.md; do
  # Run check #13 logic against just this file (adapt the loop)
  # ... pass expected
  :
done
for f in swarm/wiki/tasks/_tests/test-ap-fail-*.md; do
  # ... fail expected
  :
done
```

If F-CHECK-7 is too tedious to reproduce inline, write a `swarm/evals/run-check-13.sh`
helper that takes a single decomposition file as argument and exits 0/1 per the
check #13 spec. Run it against each of the 5 fixtures; record results.

#### F.2 — AWAITING-APPROVAL packet

After all 7 F-checks pass, write `swarm/gates/AWAITING-APPROVAL-cycle-2-implementation-2026-04-24.md`
following the shared-protocols §4 packet shape. Required frontmatter: `title,
type: gate, gate_type: implementation-review, escalator: cycle-2-impl-executor,
escalated_at: <ISO>, task_id, cycle_id, state: open`. Required body sections
(in this order):

- **Context** — brief: all 5 items implemented per this prompt; 7/7 F-CHECK
  passed; awaiting ack before Part G report.
- **Verification log** — paste F-CHECK-1..7 outputs verbatim.
- **Hook API verdict** — state Alt-A or Alt-B with evidence (from Part B B.0).
- **Per-part summary** — compact; one bullet per Part with files touched +
  commit hash.
- **Options** — A (approve all → Part G), B (approve subset → revert specified
  + re-pause), C (reject → open AMBIGUITY packet + halt).
- **Recommendation** — Option A; all Hamel-binary predicates satisfied.
- **Risk** — Low; all commits reversible via `git revert`; hooks in cycle-2
  log-only mode = zero blocking risk.
- **How Ruslan acks** — either write `<id>-ack.md` (`acked: true`, `chosen: A`)
  OR mutate this file's frontmatter (`state: acked`, `chosen: A`).

Commit + push the AWAITING-APPROVAL packet:

```
[cycle-2-impl] Part F verification passed; awaiting Ruslan ack

All 7 F-CHECK-1..F-CHECK-7 pass. AWAITING-APPROVAL-cycle-2-implementation-2026-04-24.md
opened at swarm/gates/. Stage-Gated pause until ack.
```

**STOP HERE.** Do not write Part G report until Ruslan acks. The Stage-Gated
contract is non-negotiable.

---

### Part G — Deep execution report (≥2000 words, ONLY after Ruslan ack)

After Ruslan acks the AWAITING-APPROVAL packet (Option A), write
`decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md` (or `-XX` if file
collision; this prompt assumes 2026-04-24 but adjust the date suffix to the
actual ack-receipt date if it differs).

**Mandatory sections (no shortcuts; ≥2000 words across them):**

- **G.1 Per-part summary** — for each of Parts A-E: what was implemented (file
  paths + counts), how verified (which F-CHECK / per-Part smoke proved it),
  commit hash, 1-line commit message.
- **G.2 Hook API pre-check verdict** — Alt-A or Alt-B; evidence (files read,
  output of B.0 step 3); risks accepted; cycle-3+ upgrade path if Alt-B.
- **G.3 Tradeoffs encountered** — for each spec ambiguity (e.g. schema field
  count 6 vs 8, hook script path `.claude/hooks/` vs `swarm/lib/hooks/`):
  ambiguity, decision, why (cite artefact paragraph), alternative reading.
- **G.4 Emergent issues** — surprises during execution; honest doubts about
  whether implementation matches OPP spirit (e.g. "Alt-B fallback discipline
  fragile under brigadier time pressure — Cycle-3+ must monitor").
- **G.5 Verification matrix** — table: Check / Expected / Actual / Pass? /
  Evidence (command + output). Cover all F-CHECK-1..7 + per-Part smoke checks
  (C.6, A.6, B.8, D.5, E.5).
- **G.6 Lessons for Cycle-3** — 3-5 concrete points. Examples of required
  depth:
  - "Hook script path canonical decision needs to land in shared-protocols.md
    before Cycle-3 OPP-03; symlink bridge introduces drift risk."
  - "M-class classification (M/B/O) is purely textual; Cycle-3 should consider
    auto-classification via task-shape heuristic in brigadier §3.0."
  - "OPP-04 length budget 20-200 chars selected pre-empirically; Cycle-5
    should review actual predicate length distribution to recalibrate."
  - "OPP-01 health-hooks assume cycle-close ritual that doesn't yet exist as
    a skill; Cycle-3 should formalize `/cycle-close` skill."
- **G.7 Next-step recommendations** — in priority order:
  1. M3 solo-vs-matrix experiment on OPP-01 substrate (recommended task T-B
     unit-econ arithmetic per OPPORTUNITIES §5 "most conservative test").
  2. Cycle-3 task brief drafting (OPP-03 `/compound`, OPP-05 `falsifier:`,
     OPP-06 gate-discipline per OPPORTUNITIES §7).
  3. Draft `.claude/skills/cycle-close.md` to encapsulate health-hook invocation.
- **G.8 Anti-scope honored** — explicit list: M3 NOT executed; OPP-03/05/06
  NOT touched; investor-expert €50K rows NOT modified; legacy 14 agents NOT
  touched; v2 `wiki/` NOT touched; no provider API keys referenced.

#### G.9 — Commit Part G

```
[cycle-2-impl] Part G execution report

decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-XX.md (≥2000 words):
- Per-part summary with commit hashes
- Hook API verdict (Alt-A or Alt-B with evidence)
- Tradeoffs + spec-ambiguity decisions documented
- Verification matrix (all F-CHECKs + per-Part smoke checks)
- Lessons for Cycle-3 (3-5 points)
- Next-step recommendations (M3 first; cycle-3 task brief drafting)
```

Push immediately.

---

## §3 Artefact sources to read in full BEFORE starting

You MUST read these files end-to-end before writing a single byte of
implementation. Set aside 30-45 minutes of reading time.

| # | Path | Why you must read |
|---|---|---|
| 1 | `prompts/meta-brief-cycle-2-implementation-2026-04-24.md` | Ruslan's directive; the spec for THIS prompt |
| 2 | `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` (398 lines) | Approved opportunity set; §2/§3/§4/§6 are most relevant |
| 3 | `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` (355 lines) | Upstream context (cluster IDs, tier rankings, dissents) |
| 4 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md` (781 lines) | Authoritative spec for Part A |
| 5 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md` (725 lines) | Authoritative spec for Part B; §3.0 API check, §3.4 fallback, §8 risk table |
| 6 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md` (655 lines) | Authoritative spec for Part C; §3.1/§3.2/§3.3/§3.4 critical |
| 7 | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md` (~677 lines) | Horizon-gate context for Part D HD-01 + scalability §6 verdict |
| 8 | `swarm/lib/shared-protocols.md` (275 lines, 9-section runtime contract) | §1 wiki write protocol, §3 schema, §4 HITL, §5 tool perms, §9 Max-sub |
| 9 | `swarm/wiki/operations/T-swarm-self-improve-v1-2026-04-23/cycle-01.md` (if exists) | Cycle-1 close log (provenance for Part G report) |
| 10 | `.claude/agents/brigadier.md` (1005 lines) | §3.3 WBS schema (Parts C + E), §4.1 dispatch (Part C C.2), §6 HITL (Part E E.4) |
| 11 | All 5 expert agent files (`engineering-expert.md`, `mgmt-expert.md`, `systems-expert.md`, `philosophy-expert.md`, `investor-expert.md`) | §6.1 BOSC-A-T-X tables for HD-01 Part D |
| 12 | `CLAUDE.md` (project root) | File conventions, Wiki Pipeline, Skill list, project rules |
| 13 | `.claude/rules/global.md` | Global rules (logs append-only, frontmatter mandatory, etc.) |

If any of these files do not exist or have moved, document in your Part G report
and use the closest equivalent.

---

## §4 Locked decisions to honor (NON-NEGOTIABLE)

All 24 D-locks (D1-D24) from the prior cycle are in force. Specifically:

- **D17** — Filesystem = SoT. Every change committed to git; Notion reflects,
  does not originate. NO Notion writes from this session.
- **D11** — Продюсерский центр parallel revenue stream is unaffected by this
  Method-class work; this swarm work generates no revenue directly.
- **D19** — $1T trajectory; Part D HD-01 must include all 5 gates (€50K +
  €200K + €1M + $100M + $1T) in every scalability table after the change.
- **W-5** — Two-level Compounding Engineering; OPP-01 eval harness IS the
  Level-2 substrate.
- **Q2** — Single-writer brigadier rule applies to `swarm/wiki/<canonical>/`
  only; `swarm/evals/` is OUTSIDE `swarm/wiki/` so cells MAY append directly
  to `swarm/evals/cells/<cell-id>/results.jsonl` without violation.
- **Max-subscription discipline** (shared-protocols §9): zero paid embeddings,
  zero vector DBs, zero third-party LLM API calls, zero provider key references
  in any committed file.

Plus W-1..W-12 (wiki goals), 8 R-items + 5 T-resolutions (wiki mechanics),
FPF E-1..E-18, full shared-protocols.md 9-section contract.

**Legacy coexistence:** 14 legacy agents listed in CLAUDE.md (manager,
personal-assistant, system-admin, sales-lead, sales-researcher, sales-outreach,
inbox-processor, crazy-agent, knowledge-synth, strategist, life-coach,
meta-agent, plus staging-writer + sweep-worker) are **untouched**. v2 `wiki/`
directory is **untouched**. All new work goes into `swarm/` + the 6 swarm
agents only (brigadier + 5 experts).

**No editing of existing investor-expert.md €50K rows.** They are already correct.

---

## §5 Operating mode — Stage-Gated (NON-NEGOTIABLE)

**Per ROY-ALIGNMENT default + Ruslan's standing directive:** this implementation
runs in **Stage-Gated** mode. Full-Auto is NOT authorized.

The pause point is between **Part F (verification)** and **Part G (deep
execution report)**. Specifically:

1. Implement Parts C → A → B → D → E (each with its own commit + push).
2. Run Part F verification matrix (7 cross-Part checks).
3. Write `swarm/gates/AWAITING-APPROVAL-cycle-2-implementation-2026-04-24.md`.
4. Commit + push the AWAITING-APPROVAL packet.
5. **STOP. Do not start Part G.** Wait for Ruslan ack.
6. On ack (file `<id>-ack.md` with `chosen: A`, OR frontmatter `state: acked`):
   write Part G report.
7. Commit + push Part G report.
8. Done.

If you finish all of Parts A-E + F and the AWAITING-APPROVAL packet, that is
the **end of your active session**. Do not preemptively draft Part G in your
scratchpad. Do not "get a head start." The pause is the contract. Ruslan reads
the packet; you wait.

If Ruslan acks with Option B (approve subset, roll back the rest), revert the
specified parts via `git revert <commit-hash>` (NOT `git reset --hard` — keep
history) and re-write the AWAITING-APPROVAL packet with the new state.

If Ruslan acks with Option C (reject all), open
`decisions/AMBIGUITY-cycle-2-implementation-2026-04-24.md` documenting the
rejection reason and HALT until further direction.

---

## §6 Commit cadence (per shared-protocols §1 + meta-brief)

**Incremental commits per Part. NOT one monolithic commit.** The exact
sequence (each followed by `git push`):

1. `[cycle-2-impl] OPP-04 cell_acceptance_predicate landed`
2. `[cycle-2-impl] OPP-01 eval harness infrastructure`
3. `[cycle-2-impl] OPP-02 hook layer (log-only mode)`
4. `[cycle-2-impl] HD-01 €50K gate propagated to all agents`
5. `[cycle-2-impl] HD-02 M-class rate limiter N=2 in brigadier`
6. `[cycle-2-impl] Part F verification passed; awaiting Ruslan ack`
7. `[cycle-2-impl] Part G execution report` (only AFTER ack)

Each commit message MUST follow the body shape shown in the per-Part `Commit`
sub-section (file list + ≤8 bullets summary). Do not collapse multiple Parts
into one commit even if they appear "related." The git log is part of the
provenance chain Cycle-3+ executors will consult.

**Push after each commit.** Branch: `claude/jolly-margulis-915d34`. No
force-push. No `--no-verify`. If pre-commit hooks fail, fix the underlying
issue and create a new commit (do NOT amend per the global Git Safety Protocol).

---

## §7 Definition of done

This session is COMPLETE when ALL of the following hold:

1. ✓ Parts C, A, B, D, E each have a clean commit + push to
   `claude/jolly-margulis-915d34`.
2. ✓ Part F's 7 cross-Part verification checks all return success.
3. ✓ `swarm/gates/AWAITING-APPROVAL-cycle-2-implementation-2026-04-24.md`
   exists, is committed, pushed, and includes the verification log.
4. ✓ Part G `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-XX.md` (≥2000
   words) exists, is committed, pushed — but only AFTER Ruslan's Option-A ack.
5. ✓ All Bash scripts pass `bash -n`, have executable bits, use proper shebangs,
   reference no API keys.
6. ✓ All YAML frontmatter is complete on every new `.md` file (id, type,
   created, pipeline, state minimum).
7. ✓ The 7 specific verification criteria from meta-brief Part F are explicitly
   documented as passed in the Part G report verification matrix.
8. ✓ git status is clean (all changes committed).
9. ✓ The cycle-2 log entry exists at `swarm/wiki/log.md` (or appropriate log
   file per shared-protocols §1).

If any criterion fails when you think you're done, you are NOT done. Re-do.

---

## §8 Escalation (when to STOP and escalate)

**Stop and escalate via `prompts/AMBIGUITY-cycle-2-implementation-2026-04-24.md`
in any of the following cases:**

1. **Spec contradictions** between OPPORTUNITIES §X and the corresponding
   artefact §Y. Example: meta-brief Part B item 5 says
   "shared helper goes at `swarm/lib/hooks/parse-frontmatter-field.sh`" while
   OPP-02 §3.2 also references the same path — these align, no escalation
   needed. But if you find OPP-04 §3.1 saying "string field" while a follow-up
   citation in mgmt-integrator-01.md says "structured block required" without
   reconciliation, that's an escalation trigger.

2. **OPP-01 substrate dependency on OPP-02 hook logging is unclear** — meta-brief
   Part B item 7 says "Log substrate = writes events to `swarm/evals/`
   (OPP-01 substrate; hard dependency)". If you find that OPP-01's `swarm/evals/`
   layout does not have a clear placement for `cells/hook-layer/`, document the
   ambiguity and choose the most conservative interpretation (place under
   `swarm/evals/cells/hook-layer/` matching the OPP-01 cell-dir convention).
   This is documented in B.6 above; you should NOT need to escalate here.

3. **HD-02 class tag location ambiguity** — meta-brief Part E item 2 says
   "Classification rule for M-class — brigadier must tag each decomposed cell
   with `class: M | B | O`". If you find that the class field belongs in the
   manifest.yaml (per brigadier §3.0 task intake) rather than in the WBS
   §3.3 decomposition, escalate. (The recommended placement in E.2 is in the
   §3.3 cell template; if that is incompatible with existing brigadier
   discipline, raise it.)

4. **Hook API verdict produces an unsafe state** — if `.claude/settings.json`
   contains existing hook entries that conflict with the OPP-02 entries, and
   you cannot resolve cleanly via additive merging, escalate.

5. **Any commit fails pre-commit hooks** — do NOT bypass. Investigate the
   underlying issue. If you cannot resolve in 2 turns, escalate.

6. **Any verification check (F.1 or per-Part) returns unexpected result** —
   investigate first (did you mis-implement?). If you re-do and still fail,
   escalate.

**Escalation packet shape:**

```markdown
---
title: Ambiguity packet — Cycle-2 Implementation
type: ambiguity
created: <ISO-timestamp>
escalator: cycle-2-impl-executor
state: open
---

# Ambiguity Encountered

## Context
<which Part you were on; what step>

## The contradiction / ambiguity
<exact quote from spec A; exact quote from spec B; why they conflict>

## What I would do if I had to choose
<your best guess + rationale>

## What I'm doing instead
HALT pending Ruslan resolution.

## Files written so far in this Part
<list>

## Files NOT written that this Part requires
<list>
```

Commit + push the ambiguity packet:

```
[cycle-2-impl] AMBIGUITY: <one-line summary>
```

Then HALT. Do not proceed to next Part. Do not guess.

---

## §9 Quick-reference cheat sheet (pin this to your scratchpad)

```
ORDER:        Part C (OPP-04) → Part A (OPP-01) → Part B (OPP-02) → Part D (HD-01) → Part E (HD-02)
PAUSE:        Between Part F (verification) and Part G (report). Stage-Gated.
COMMITS:      7 total (5 Part commits + 1 verification + 1 report)
BRANCH:       claude/jolly-margulis-915d34 (no force-push, no --no-verify)
LANGUAGE:     RU for content if creating wiki pages; EN for code/config/log entries
KEY DON'Ts:
              - DO NOT execute M3 (separate next task)
              - DO NOT touch OPP-03 / OPP-05 / OPP-06 (Cycle-3+ queue)
              - DO NOT modify investor-expert.md €50K rows (already correct)
              - DO NOT touch v2 wiki/ or 14 legacy agents
              - DO NOT reference any provider API key in any committed file
              - DO NOT skip the AWAITING-APPROVAL pause
              - DO NOT collapse Part commits into one
              - DO NOT amend commits (create new ones if pre-commit hook fails)
              - DO NOT preemptively draft Part G before Ruslan ack
KEY DOs:
              - DO `unset ANTHROPIC_API_KEY` before launching (Max-sub discipline)
              - DO read all 13 §3 sources end-to-end FIRST
              - DO run per-Part internal smoke checks before each commit
              - DO push after each commit
              - DO honor the artefact wording when meta-brief and artefact differ
                (and document in Part G report)
              - DO escalate via AMBIGUITY packet on any spec contradiction
```

---

---

*End of execution prompt. Estimated 18-26 active turns across 5 Parts +
verification + Stage-Gated pause + report. ~28 files touched. Max-sub
discipline throughout.*
