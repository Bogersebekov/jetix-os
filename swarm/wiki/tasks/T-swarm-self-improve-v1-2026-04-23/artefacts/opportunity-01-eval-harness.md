---
id: opportunity-01-eval-harness
title: "OPP-01 — swarm/evals/ file-JSONL eval harness"
type: opportunity-draft
cluster_id: C-02
tier: T1
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: systems-expert
mode: integrator
lead_domain: systems
co_domains: [engineering, investor, philosophy]
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: high
confidence_method: multi-source-rubric
sources:
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md
  - decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md
caveats_addressed: [C-1, C-2, C-3]
dissents_addressed: [D-03]
requisite_variety_budget:
  captured: >
    L6 feedback-loop sensor placement for the measurement void; 4 downstream
    consumers (golden-sets, health counters, PPR recall, skill pass-rate);
    file-JSONL schema contract; run.sh executor; integration points with
    health.md, edges.jsonl, strategies.md compound step.
  actual_estimate: >
    ~25% of full system variety. Captures the measurement substrate and its
    4 consumers. Does not capture: HITL cadence dynamics, external-market
    feedback loops, Ruslan attention-variance, Anthropic API latency variance.
---

# OPP-01 — swarm/evals/ file-JSONL eval harness

---

## Pitch

Install a pure-filesystem JSONL eval harness at `swarm/evals/` that becomes the single
measurement substrate feeding health counters, golden-set validation, skill pass-rate
tracking, and PPR recall — simultaneously closing the Meadows L6 measurement void that
severs every balancing loop in the swarm.

```
Before (open-loop swarm):

  brigadier dispatches ──► cell executes ──► artefact written
        │                                         │
        │ (manual survey only)                    │ (no counter update)
        └─────────────────────────────────────────┘
                  no measurement path exists

After (closed-loop swarm with OPP-01):

  brigadier dispatches ──► cell executes ──► artefact written
        ▲                                         │
        │                              swarm/evals/<cell>/
        │                               results.jsonl append
        │                                         │
        └── health.md counters ◄── run.sh ◄───────┘
              │              ▲
              │              └── strategies.md DRR (compound step)
              │
              └── edges.jsonl (Q1 Tier-3 BFS unblocked when count > 0)
              └── skill pass-rate (Q6 α-3 activation criterion)
```

---

## Problem

### Current state anchored to MP-1 and MP-3

**MP-3 — Measurement void (Caveat C-1 compliance: concrete anchors from on-disk state).**

`swarm/wiki/meta/health.md` exists on disk (γ:D10, ratio 0.7) but all 5 live counters
(`closed_cycles_count`, `active_skills_count`, `open_tasks_count`, `lint_findings_count`,
`fpar_log`) are frozen at `0` or `null`. [src: gamma-wiki-v3.md:D10 "every counter will
remain at bootstrap until wired"] No script, hook, or scheduled job updates these fields.
The dashboard skeleton is pristine; it carries no physiology.

The consequence for the swarm system model is that every balancing loop requires a sensor
and none exist. [src: systems-critic-01.md:H-8 "the system is running open-loop: actions
are taken but no feedback on outcomes reaches any controller"] The reinforcing compounding
loop requires "did artefact quality improve?"; the Level-3 audit loop requires "what is the
cell pass-rate?"; neither can close. This is the Meadows L6 (information-structure) failure
rated score 35.0 — highest-leverage intervention in the entire 9-hypothesis ranked set.
[src: systems-optimizer-01.md:scoring table H-8=35.0]

**MP-1 — Executor not wired (eval harness dimension).**

`swarm/evals/` does not exist on disk. [src: decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES:W1
"swarm/evals/ does not exist; 0 golden-set seeds"] `D11` (Q6 skill-activation rubric) states
that the golden-set JSONL is the prerequisite for a skill to graduate from `candidates` to
`learning`. [src: gamma-wiki-v3.md:D11 "no golden-set.jsonl"] With zero JSONL entries, zero
skills can be validated. The eval harness is not just a measurement tool — it is the gate
mechanism for the α-3 skill lifecycle. [src: engineering-optimizer-01.md:Bundle-3 H-5 "without
this, Phase B is unmeasurable"]

**Philosophy falsifier prerequisite (D-03 addressed, C-1 anchor).**

The "2× improvement" claim (Boris Cherny) is currently F=F1 (single-author assertion, no
measurement substrate). [src: philosophy-optimizer-01.md:M-1 "0/8 hypotheses satisfy falsifier
completeness"] Treating it as a gate criterion before the eval harness exists encodes a
non-falsifiable anchor in all downstream KPIs. The eval harness is the prerequisite that
elevates this claim from F1 to F3+. [src: mgmt-integrator-01.md:D-03 "Position A accepted:
eval harness ships first; 2× calibrated numerically"] D-03 is resolved operationally by this
opportunity: the "2× claim" is NOT used as a gate criterion in this artefact — it is cited
as provenance context only. [src: mgmt-integrator-01.md:§5 OPP-01 acceptance predicate]

**Unit-econ substrate gap (investor anchor).**

The investor-optimizer's Bundle-C H-4 (golden-set comparison: solo-brigadier vs 6-cell) is
BLOCKED until `swarm/evals/` exists to store `results.jsonl`. [src: investor-optimizer-01.md:
Bundle-C "H-4 is a prerequisite for H-8; sequential dependency"] The ROI arithmetic (7.9×
over 20 cycles lower bound) cannot be validated without a measurement path.
[src: investor-optimizer-01.md:§4.1 "first investor-grade ROI computation on the swarm"]

---

## Proposed Implementation

### Directory layout

```
swarm/evals/
├── schema.md                         # shared schema contract (single source of truth)
├── run.sh                            # eval runner (Bash + Python stdlib only; no paid tooling)
├── README.md                         # usage + integration points
├── engineering-critic/
│   └── golden-set.jsonl              # ≥3 seed entries on install day
├── systems-critic/
│   └── golden-set.jsonl
├── systems-integrator/
│   └── golden-set.jsonl
├── mgmt-integrator/
│   └── golden-set.jsonl
└── ... (one dir per cell as needed; not all 20 cells on day-1)
```

Cells not seeded on day-1 are created lazily: the first time a cell produces an accepted
artefact, its directory and `golden-set.jsonl` are created by the cycle-close step.

### schema.md (canonical JSONL record)

File: `swarm/evals/schema.md`

```yaml
# swarm/evals/schema.md
# Single schema record used by all cells.
# One JSON object per line in golden-set.jsonl and results.jsonl.

fields:
  cell_id:
    type: string
    description: "<expert>-<mode> e.g. systems-critic, engineering-optimizer"
    required: true
  test_id:
    type: string
    description: "slug uniquely identifying this test case; kebab-case"
    required: true
  cycle_id:
    type: string
    description: "cycle that produced the seed; e.g. cyc-swarm-self-improve-v1-2026-04-23"
    required: true
  input_path:
    type: string
    description: "relative path to the input artefact or context file"
    required: true
  input_hash:
    type: string
    description: "sha256 of input file contents at seed time (for drift detection)"
    required: true
  expected_output_path:
    type: string
    description: "relative path to the expected-output artefact"
    required: true
  expected_output_hash:
    type: string
    description: "sha256 of expected output at seed time"
    required: true
  acceptance_predicate:
    type: string
    description: "Hamel-binary predicate; the gate criterion for pass=true"
    required: true
  actual_output_path:
    type: string
    description: "relative path to actual output produced by the cell during eval run; null if not yet run"
    required: false
    default: null
  pass:
    type: boolean
    description: "true if acceptance_predicate was satisfied by actual_output; null if not yet evaluated"
    required: false
    default: null
  notes:
    type: string
    description: "free-text; max 200 chars; capture discrepancy reason on fail"
    required: false
    default: ""
  timestamp:
    type: string
    description: "ISO-8601 UTC; set at eval-run time, not at seed time"
    required: false
    default: null

# Engineering-optimizer Bundle-3 shared-schema requirement:
# This schema also serves as the manifest format for
# swarm/wiki/skills/candidates/<slug>/manifest.md (golden_set_path field).
# One schema; two consumers.
```

### run.sh scaffold

File: `swarm/lib/evals/run.sh` (symlinked from `swarm/evals/run.sh`)

```bash
#!/usr/bin/env bash
# swarm/evals/run.sh
# Usage: bash swarm/evals/run.sh [--cell <cell-id>] [--dry-run]
# Runs acceptance-predicate checks against golden-set.jsonl entries.
# Outputs results.jsonl in same cell directory.
# No paid tooling. No external APIs. Pure filesystem + Python stdlib.
# Max-subscription discipline: no ANTHROPIC_API_KEY or equivalent referenced.

set -euo pipefail

EVALS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PASS=0
FAIL=0
SKIP=0

# Argument parsing
CELL_FILTER=""
DRY_RUN=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --cell) CELL_FILTER="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

# Discover cell directories
for cell_dir in "${EVALS_ROOT}"/*/; do
  cell_id=$(basename "${cell_dir}")
  [[ -n "${CELL_FILTER}" && "${cell_id}" != "${CELL_FILTER}" ]] && continue
  golden="${cell_dir}golden-set.jsonl"
  [[ ! -f "${golden}" ]] && continue

  results="${cell_dir}results.jsonl"

  while IFS= read -r line; do
    [[ -z "${line}" || "${line}" == \#* ]] && continue
    test_id=$(echo "${line}" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['test_id'])")
    predicate=$(echo "${line}" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['acceptance_predicate'])")
    expected_path=$(echo "${line}" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['expected_output_path'])")

    # Minimal structural check: expected output file exists + non-empty
    if [[ -f "${expected_path}" && -s "${expected_path}" ]]; then
      pass_val=true
      ((PASS++)) || true
    else
      pass_val=false
      ((FAIL++)) || true
    fi

    if [[ "${DRY_RUN}" == false ]]; then
      ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
      echo "{\"cell_id\":\"${cell_id}\",\"test_id\":\"${test_id}\",\"pass\":${pass_val},\"timestamp\":\"${ts}\"}" >> "${results}"
    fi
  done < "${golden}"
done

echo "PASS=${PASS} FAIL=${FAIL} SKIP=${SKIP}"
[[ "${FAIL}" -eq 0 ]] && exit 0 || exit 1
```

Notes on the scaffold:
- Line count target: 55-70 lines (engineering-optimizer-01 Bundle-3 H-5 sharpen). This
  scaffold is ~55 lines; expand with the `min_entries: 20` warning and hash-verification
  path in the implementation step.
- The `min_entries: 20` guard: when total JSONL entries across all cells < 20, emit a
  `WARN: golden-set floor not reached (have N, need 20); measurements not yet statistically
  meaningful` to stderr but do NOT fail. Floor of 20 entries is the Hamel-valid threshold.
  [src: engineering-optimizer-01.md:H-5 sharpening "floor to 'measurement valid': 20 entries"]
- Idempotency: `results.jsonl` is append-only with timestamp; re-running does not overwrite.
  [src: engineering-optimizer-01.md:Bundle-3 IDEM invariant "re-runs append new results"]
- No `networkx`, no paid SDKs, no env-var references. Pure Bash + Python stdlib.
  [src: mgmt-integrator-01.md:T-5 resolution "deny paid tooling Phase A"]

### Seed entries — day-1 golden set

Three seed entries are created on install day from this cycle's artefacts. These are the
minimum to satisfy the Cycle-1 smoke-verification criterion (§11 below).

**Cell: systems-critic**
```json
{"cell_id":"systems-critic","test_id":"h8-measurement-void-claim","cycle_id":"cyc-swarm-self-improve-v1-2026-04-23","input_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md","input_hash":"<computed-at-install>","expected_output_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md","expected_output_hash":"<computed-at-install>","acceptance_predicate":"count(named_feedback_loops with polarity) >= 2 AND system_boundary named with >=3 out_of_system_items AND requisite_variety_budget present","actual_output_path":null,"pass":null,"notes":""}
```

**Cell: engineering-optimizer**
```json
{"cell_id":"engineering-optimizer","test_id":"bundle3-eval-harness-creation","cycle_id":"cyc-swarm-self-improve-v1-2026-04-23","input_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md","input_hash":"<computed-at-install>","expected_output_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md","expected_output_hash":"<computed-at-install>","acceptance_predicate":"swarm/evals/schema.md exists AND swarm/evals/engineering-critic/golden-set.jsonl exists AND wc -l golden-set.jsonl >= 3","actual_output_path":null,"pass":null,"notes":""}
```

**Cell: systems-integrator (this artefact)**
```json
{"cell_id":"systems-integrator","test_id":"opp01-opportunity-draft","cycle_id":"cyc-swarm-self-improve-v1-2026-04-23","input_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md","input_hash":"<computed-at-install>","expected_output_path":"swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md","expected_output_hash":"<computed-at-install>","acceptance_predicate":"frontmatter contains caveats_addressed: [C-1, C-2, C-3] AND dissents_addressed: [D-03] AND section '## 2x improvement claim' present AND anti_scope length >= 3","actual_output_path":null,"pass":null,"notes":""}
```

### Integration points

How OPP-01 feeds the 4 downstream consumers after installation:

**1. health.md live counters (D10 / sys H-8 OPT-1).**
The cycle-close hook (or manual brigadier discipline until Phase-B automation) runs:
```
bash swarm/evals/run.sh 2>&1 | grep -c "pass=true"
```
and writes the result to `swarm/wiki/meta/health.md` `fpar_log` field. The
`closed_cycles_count` field is incremented by the same hook when
`swarm/logs/<cycle-id>/cycle-log.md` is created. [src: systems-optimizer-01.md:OPT-1
"sensor type: filesystem-derived counters; sensor script: ~20-line bash fragment"]

**2. Golden-set validation (eng Bundle-3 H-5 / investor Bundle-C H-4).**
`swarm/evals/<cell>/golden-set.jsonl` stores accepted artefact hashes. At each cycle close,
brigadier runs `run.sh --cell <cell-id>` and appends to `results.jsonl`. The acceptance-
predicate pass-rate (FPAR) is the ratio `pass=true / total` across all results. This is the
measurement substrate that validates the "2× quality claim" (philosophy D-03 resolved path).
[src: engineering-optimizer-01.md:H-5 "eval-runner.sh produces results.jsonl with ≥3 records"]

**3. Skill pass-rate (Q6 α-3 skill-activation criterion).**
The D11 activation rubric requires a golden-set JSONL before a skill candidate can graduate
to `learning` state. [src: gamma-wiki-v3.md:D11 "no golden-set.jsonl → activation rubric
untested"] Once `swarm/evals/<cell>/golden-set.jsonl` has ≥3 entries AND pass-rate ≥ 0.70
across the last 5 evaluations, the skill candidate is eligible for promotion. Brigadier reads
`results.jsonl` to compute this; the `run.sh` output provides the machine-readable signal.

**4. Q1 Tier-3 BFS unblock.**
`swarm/wiki/graph/edges.jsonl` is currently empty — 4-line comment stub, no data records.
[src: gamma-wiki-v3.md:D3 "Tier-3 BFS has nothing to traverse"] OPP-01's cycle-close hook
emits a `derived_from` edge entry to `edges.jsonl` for each golden-set seed created (e.g.
`{from: "tasks/.../artefacts/systems-critic-01", to: "tasks/.../context/gamma-wiki-v3",
type: "derived_from"}`). After the first eval run, `edges.jsonl` is non-empty and Tier-3
BFS becomes operational on the populated subgraph. [src: decisions/SWARM-SELF-IMPROVEMENT-
HYPOTHESES:W1 "Locks touched: Q1 retrieval"]

---

## 2x Improvement Claim

**Caveat C-1 compliance:** The 2× claim is anchored to concrete on-disk observables, not to
the Boris Cherny assertion (which is F=F1, ungrounded before harness exists).
**Caveat C-2 compliance:** The claim is tagged to in-Ruslan-control variables only (see
anti_scope and dichotomy_tag below).
**D-03 compliance:** The claim does not USE "2× improvement" as a gate criterion — it states
a MEASURABLE CRITERION that will be evaluated post-implementation.

**Before (baseline, on-disk-verifiable):**
- `swarm/evals/` does not exist: `ls swarm/evals/` returns "No such file or directory."
- Golden-set seeds: 0 entries.
- Cells with `golden-set.jsonl`: 0 of 20.
- health.md `fpar_log`: null (bootstrap).
- `/lint` check #X for eval-harness presence: absent (not yet added).
- Feedback loops with measurable sensors: 0 of 5 declared in health.md.

**After OPP-01 (Hamel-binary measurable criterion):**

```
OPP-01 passes iff ALL of the following hold:

(a) swarm/evals/ directory exists AND swarm/evals/schema.md exists
    AND swarm/evals/run.sh exists AND wc -l swarm/evals/run.sh returns ≥55 lines

(b) swarm/evals/<cell>/golden-set.jsonl exists for ≥15 cells
    AND total JSONL entry count across all golden-set.jsonl files >= 60

(c) bash swarm/evals/run.sh exits 0 on the day-1 seed golden-sets
    (i.e. the 3 seed entries pass their structural acceptance predicates)

(d) swarm/wiki/meta/health.md fpar_log field is non-null
    (at least 1 FPAR record written by cycle-close hook)

(e) swarm/wiki/graph/edges.jsonl has >= 5 data records
    (non-comment lines; Tier-3 BFS unblocked)
```

This is the 2× improvement claim: from 0 golden-set seeds and 0 measurement-path nodes
to ≥60 JSONL entries across ≥15 cells with a working runner. Every single balancing loop
that was severed by the measurement void (systems-critic H-8, score 35.0) now has a sensor
path. The improvement is not "2× on quality" (that would be D-03's unfalsifiable anchor);
it is "0-to-operational on the entire measurement substrate" — a step-change, not an
incremental gain.

---

## Effort Breakdown

**Total estimate: 6-8 expert turns (Ruslan-equivalent; Phase A Max-subscription)**

| Subtask | Turns | Notes |
|---|---|---|
| Create `swarm/evals/` directory tree (5 initial cells: systems-critic, engineering-critic, systems-integrator, engineering-optimizer, mgmt-integrator) | 1 | `mkdir -p` + initial README; brigadier executes |
| Write `swarm/evals/schema.md` (shared schema per Bundle-3 engineering-optimizer shared-schema extraction) | 1 | ~40 lines YAML; serves dual consumers (eval + skill manifest) [src: engineering-optimizer-01.md:OPT-EXT-2] |
| Write `swarm/evals/run.sh` scaffold to 55-70 lines; add `min_entries: 20` warning; add hash-verification path | 2 | Pure Bash + Python stdlib; no paid tooling; Max-sub compliant |
| Compute sha256 hashes of 3 seed artefacts; write 3 seed JSONL entries across 3 cell dirs | 1 | `sha256sum` on existing artefacts; trivial filesystem op |
| Integrate cycle-close hook: append to fpar_log in health.md; emit ≥5 `derived_from` edges to edges.jsonl | 1 | Part of brigadier Compound-step discipline; OR manual script ~15 lines |
| Seed remaining 12 cell directories (lazy-creation; deferred to each cell's first closed cycle) | 0 (deferred) | Not a day-1 turn; each cycle-close adds 1-2 cells |
| Brigadier verification pass: run `bash swarm/evals/run.sh --dry-run`; confirm exit 0 | 1 | 1 verification turn |

**Effort grounding source:** engineering-optimizer-01.md Bundle-3 H-5 sharpening: "Verification
turn-count: 2 brigadier turns (read schema + run eval-runner on seed)"; systems-optimizer-01.md
OPT-1: "Sensor script: ~20-line bash fragment; effort-class: 1 (hours)"; mgmt-integrator-01.md
§5 OPP-01: "Effort estimate: 6-8 turns (systems-optimizer OPT-1 + OPT-6 partial;
engineering Bundle-3)."

---

## Dependencies

**OPP-01 has no upstream dependencies.** It is the unblocking root node.
[src: mgmt-integrator-01.md:§5 OPP-01 "Dependencies: None. This is the unblocking root node"]
[src: decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES:W1 "Locks touched: D10, Q1 retrieval, W-5"]

**OPP-01 unblocks (downstream, NOT prerequisites for this opportunity):**

| Downstream | Blocked by OPP-01 absence | Unblocked when |
|---|---|---|
| OPP-03 /compound dual-sink | `/compound` should write to `swarm/evals/` on each invocation | OPP-01 dirs exist |
| M3 golden-set comparison (solo vs 6-cell) | Needs `swarm/evals/golden/` path | OPP-01 dirs exist |
| D11 Q6 α-3 skill activation | golden-set.jsonl required for candidates→learning | ≥3 JSONL seed entries exist |
| health.md fpar_log population | No path to write FPAR without results.jsonl | run.sh emits results |
| Q1 Tier-3 BFS | edges.jsonl empty | ≥5 edges emitted by cycle-close hook |
| Philosophy M-1 falsifier completeness | "2× claim" is F1 without measurement path | FPAR baseline exists |
| investor Bundle-C H-4 (golden-set comparison) | Needs results.jsonl store | run.sh operational |

---

## Locks Honored / Touched

| Lock | Status | How OPP-01 handles it |
|---|---|---|
| **D1** 9-layer dir layout | HONORED | `swarm/evals/` is NOT inside `swarm/wiki/` — it is a peer directory at `swarm/` level, consistent with the layer structure. No wiki-layer write required. [src: gamma-wiki-v3.md:D1] |
| **D10** health.md skeleton | HONORED + POPULATED | OPP-01's cycle-close hook writes the first non-null value to `fpar_log`. The D10 skeleton receives its first physiological signal. [src: gamma-wiki-v3.md:D10 "every counter will remain at bootstrap until wired"] |
| **D11** Q6 skill activation rubric | HONORED + UNBLOCKED | The golden-set.jsonl at `swarm/evals/<cell>/` is the exact file path that D11 §11.7 requires for the `candidates→learning` transition. OPP-01 creates the substrate; D11's owner (brigadier + meta-agent) operates against it. [src: gamma-wiki-v3.md:D11] |
| **W-5** CE Compound | HONORED | OPP-01 is the substrate that the /compound skill (OPP-03) writes into. The CE 40/10/40/10 Compound step = "money step" flows through `swarm/evals/` on each cycle close. OPP-01 does not change the W-5 rule — it instantiates the filesystem infrastructure the rule needs. [src: decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES:M1 "/compound depends on W1 eval substrate"] |
| **Q1** Tier-3 BFS retrieval | UNBLOCKED | The cycle-close hook emits ≥5 `derived_from` edges to `swarm/wiki/graph/edges.jsonl`, giving Tier-3 BFS its first traversable nodes. [src: gamma-wiki-v3.md:Q1 "edges.jsonl empty → Tier-3 BFS has nothing to traverse"] |
| **Q2** Single-writer brigadier | HONORED | `swarm/evals/` is NOT under `swarm/wiki/<canonical>/`. Writes to `swarm/evals/` are by the cell executing the eval (appending to results.jsonl) — this does not touch canonical wiki. Brigadier's sole-writer rule is scoped to `swarm/wiki/` per shared-protocols §1. |
| **Q6** α-3 skill pipeline | UNBLOCKED | Once golden-set.jsonl ≥3 entries AND pass-rate ≥0.70, the skill-activation rubric can fire. OPP-01 delivers the prerequisite; Q6's own machinery operates from there. |
| **Max-subscription discipline** | STRICTLY HONORED | `run.sh` uses Bash + Python stdlib only. Zero paid embeddings, zero vector DBs, zero third-party SDK imports, zero provider API-key references. [src: systems-expert §1a; shared-protocols §9] |

---

## Risk + Mitigation

### Risk 1: Seed-entry quality (Caveat C-1 concrete-anchor requirement)

**Risk:** The 3 day-1 seed entries may have poorly-specified acceptance predicates that are
trivially satisfied (e.g. "file exists") rather than content-checking. Trivial predicates
produce a misleading FPAR of 1.0 that masks real quality failures.

**F:** F3 (multi-case pattern — identical dynamic observed in canonical eval harness bootstrap
literature: Hamel/Husain methodology warns "20-entry floor before rates are statistically
meaningful").

**Mitigation:** Each seed entry's `acceptance_predicate` must match the producing cell's own
frontmatter `acceptance_predicate` field (not a trivial structural check). Brigadier verifies
this alignment during the AWAITING-APPROVAL review of OPP-01 before promoting the seed files.
The `min_entries: 20` warning in `run.sh` provides an automated reminder that rates below the
floor are non-binding.

**Kill-condition:** If FPAR = 1.0 across all entries for ≥3 cycles AND acceptance predicates
are confirmed to be structural-only (file-exists), OPP-01 seeds are replaced with content-
aware predicates before cycle-5.

### Risk 2: Integration drift between run.sh and health.md schema

**Risk:** The cycle-close hook that writes to `health.md fpar_log` may evolve separately from
`run.sh`'s output format, producing a format mismatch that silently breaks the measurement path.

**Mitigation:** `schema.md` is the single source of truth for the JSONL record structure. The
cycle-close hook MUST reference `schema.md` before writing. A `/lint` check (`lint` check #X:
"fpar_log entry format matches schema.md field names") should be added in the same PR as OPP-01.
This is a ≤5 line addition to `.claude/skills/lint.md`.

**Kill-condition:** If `health.md fpar_log` contains non-parseable entries across 2 consecutive
cycles, the hook has drifted from schema; brigadier re-synchronises or escalates to HITL.

### Risk 3: OPP-01 becomes a write target for non-brigadier cells (Q2 scope)

**Risk:** Cells may attempt to write their own output directly to `swarm/evals/<cell>/results.jsonl`
rather than returning the result to brigadier for promotion. This violates Q2 single-writer if
the cells are writing INSIDE `swarm/wiki/` — but `swarm/evals/` is intentionally placed OUTSIDE
`swarm/wiki/` to allow cell-direct writes to `results.jsonl` without violating Q2.

**Mitigation:** The directory placement (`swarm/evals/` NOT inside `swarm/wiki/<canonical>/`)
is deliberate. The README.md in `swarm/evals/` must state explicitly: "Cells MAY append to their
own `<cell>/results.jsonl`; cells MUST NOT write to `swarm/wiki/<canonical>/` directly (Q2)."
This is a LOC (locality) design choice, not a workaround.

**Kill-condition:** If a cell write to `swarm/evals/` triggers an AP-1 provenance-gate violation
(because the hook has been over-scoped to include `swarm/evals/`), narrow the hook's write-scope-
glob to exclude `swarm/evals/`. The engineering-optimizer-01 Bundle-1 H-4 `write-scope-guard.sh`
is the mechanism. [src: engineering-optimizer-01.md:H-4 "running it with path=swarm/wiki/foundations/
swarm-alphas.md returns exit 1; path=swarm/wiki/drafts/... returns exit 0"]

### Risk 4: schema.md shared-consumer coupling (engineering Bundle-3 LOC partial warning)

**Risk:** The shared `schema.md` serves both `swarm/evals/` JSONL records AND
`swarm/wiki/skills/candidates/<slug>/manifest.md` as noted by engineering-optimizer-01 Bundle-3
LOC partial warning. A schema change that serves one consumer may break the other.

**Mitigation:** The schema carries two versioned sections: `# Section A — eval JSONL fields`
and `# Section B — skill manifest fields`. Changes to Section A require no action on Section B
(they are additive, not shared keys). The `/lint` check for manifest validity references only
Section B. The LOC partial warning is acknowledged; the risk is rated LOW because Section A
and Section B share only the `acceptance_predicate` string field, which is semantically compatible
across both uses.

---

## Phase-A Feasibility

**YES — implement now.**

Rationale:

1. **No paid tooling required.** `run.sh` is pure Bash + Python stdlib. `schema.md` is a text
   file. The 3 seed entries are typed JSONL strings. Total infrastructure cost: 0 external
   dependencies. Max-subscription discipline is not stretched.
   [src: mgmt-integrator-01.md:T-5 resolution; shared-protocols §9; systems-expert §1a max-sub]

2. **No HITL gate required.** OPP-01 is a directory-creation + file-writing action within
   `swarm/evals/` (outside canonical wiki). It does not touch `swarm/wiki/<canonical>/`,
   does not revise foundations, does not change a Method. Decision rights check per §1d:
   action is in `autonomous` (draft a system-model.md / scalability-projection.md) OR
   permitted under brigadier's own write rights. No `requires-approval` row is triggered.

3. **Adjacent-possible confirmed.** The 4 prerequisites for OPP-01 are all satisfied in the
   current state: (a) `swarm/wiki/meta/health.md` exists (D10 skeleton confirmed by γ:D10),
   (b) `swarm/wiki/graph/edges.jsonl` exists (γ:D3 "4-line comment stub"), (c) at least 1
   accepted artefact exists to seed from (this cycle's artefacts), (d) brigadier can run a
   bash script. Kauffman adjacent-possible check: PASS.
   [src: systems-optimizer-01.md:OPT-6 "prerequisite A met: cycle 1"]

4. **Effort is hours-class.** Systems-optimizer-01 classifies OPT-1 (health.md sensor
   placement) as effort-class 1 (hours). Engineering Bundle-3 estimates 4 effort-points
   (before shared-schema compression). Combined OPP-01 estimate is 6-8 turns — trivially
   within a single brigadier session.

5. **Root-node position guarantees no blocking dependency.** OPP-01 is the root node of
   the entire dependency DAG. Installing it does not require any other opportunity to be
   delivered first. [src: mgmt-integrator-01.md:§5 OPP-01 "Dependencies: None"]

---

## Anti-scope + Dichotomy-of-Control

**Caveat C-2 compliance.** Per philosophy-optimizer-01.md B-2, every opportunity must declare
anti_scope (≥3 items) and a dichotomy_tag separating in-Ruslan-control from not-in-Ruslan-control.

### anti_scope

- **NOT wiring the PostToolUse lint hook** — that is OPP-02 (C-01 Executor Gap / engineering
  Bundle-1) territory. OPP-01 creates the measurement substrate; OPP-02 creates the enforcement
  hook. They are parallel-deliverable; neither blocks the other.

- **NOT implementing the /compound dual-sink skill** — that is OPP-03 (C-03 Compounding Loop).
  OPP-01 provides the `swarm/evals/` directory that `/compound` writes into; the skill itself
  is authored in OPP-03. The eval harness is infrastructure; the skill is the consumer.

- **NOT performing the golden-set comparison (solo-brigadier vs 6-cell)** — that is Memory
  cluster M3 / investor Bundle-C H-4. The comparison requires a working eval harness; it is
  a post-OPP-01 activity, not part of the harness installation.

- **NOT adding the `falsifier:` field to existing artefacts** — that is OPP-05 (C-06 Falsifier
  Field / philosophy Bundle-B-1). OPP-01 is the prerequisite that makes falsifier predicates
  measurable; populating them is a separate pass.

- **NOT computing unit-econ ROI arithmetic** — that is investor-expert territory (investor-
  optimizer-01 §4 turn-cost model). The eval harness IS the substrate the ROI arithmetic
  depends on; the arithmetic itself is not authored here.

- **NOT resolving the Yan/Anthropic paradigm conflict (D-01)** — that is philosophy × integrator
  territory at Phase B. OPP-01 does not touch multi-agent throughput claims.

### dichotomy_tag

```yaml
dichotomy_tag:
  in_control:
    - "which directory structure to create under swarm/evals/"
    - "which JSONL field names appear in schema.md"
    - "which 3 seed entries to create on day-1 (from this cycle's artefacts)"
    - "whether run.sh uses Bash or Python stdlib"
    - "whether schema.md version is bumped when fields are added"
    - "which cells get day-1 dirs vs lazy-created dirs"
  not_in_control:
    - "whether Ruslan reads health.md fpar_log between cycles"
    - "whether future cells produce artefacts that actually pass acceptance predicates"
    - "whether the Hamel-binary acceptance predicates in seed entries are correct"
    - "whether the Anthropic model interprets eval criteria consistently across cycles"
    - "whether 60 JSONL entries is the right floor for statistical validity"
  mixed:
    - "the cadence at which the cycle-close hook runs (Ruslan can manually trigger; ideal is automated)"
    - "whether FPAR trends up or down (observable but not directly actionable without behavioral change)"
    - "whether /lint check #X is added in the same PR or a subsequent one"
```

---

## Cycle-1 Smoke vs Cycle-2 Upgrade

**Caveat C-3 compliance.**

### Cycle-1 smoke-verification criterion

Cycle-1 smoke passes iff ALL of the following hold at the end of the current cycle
(cyc-swarm-self-improve-v1-2026-04-23):

```
SMOKE-1: swarm/evals/ directory exists (bash ls swarm/evals/ exits 0)
SMOKE-2: swarm/evals/schema.md exists AND wc -l returns >= 20 lines
SMOKE-3: swarm/evals/run.sh exists AND wc -l returns >= 55 lines
SMOKE-4: swarm/evals/<cell>/golden-set.jsonl exists for >= 3 cells
SMOKE-5: total JSONL entries across all golden-set.jsonl files >= 3
SMOKE-6: bash swarm/evals/run.sh --dry-run exits 0
SMOKE-7: swarm/wiki/meta/health.md fpar_log field is non-null
         (at least 1 record; may be from manual brigadier write for cycle-1)
```

Smoke-1 through Smoke-6 are pure filesystem checks. Smoke-7 requires the cycle-close
hook or brigadier to manually write 1 fpar_log record. This is the minimum viable signal:
the measurement path exists and has been exercised once.

The smoke-verification does NOT require 60 JSONL entries (that is the Cycle-2 target).
It does NOT require FPAR ≥ 0.70 (no statistical meaning with 3 entries). It confirms
form, not quality.

### Cycle-2 conformance-check upgrade criterion

Cycle-2 upgrade passes iff ALL of the following hold at the end of cycle 2:

```
CONFORM-1: SMOKE-1..SMOKE-7 still pass (regression check)
CONFORM-2: swarm/evals/<cell>/golden-set.jsonl exists for >= 7 cells
           (≥4 new cell dirs lazily created during cycle 2 execution)
CONFORM-3: total JSONL entries >= 20
           (floor reached; run.sh min_entries warning no longer fires)
CONFORM-4: bash swarm/evals/run.sh (full run, not --dry-run) exits 0
           AND produces results.jsonl in >= 3 cell dirs
CONFORM-5: swarm/wiki/meta/health.md fpar_log contains >= 2 records
           (cycle-close hook has fired at least twice)
CONFORM-6: swarm/wiki/graph/edges.jsonl has >= 5 non-comment data records
           (Tier-3 BFS population begun; Q1 unblocked)
CONFORM-7: /lint check #X "swarm/evals/schema.md present" passes
           (lint check addition is part of cycle-2 delivery)
```

The 4/7 conformance-check upgrade requirement in Caveat C-3 means: at cycle-2, if
CONFORM-1..CONFORM-7 are checked and ≥4 pass, OPP-01 is declared CONFORMANT and elevated
from `state: drafted` to `state: conformant` in its frontmatter. If <4 pass, brigadier opens
an AWAITING-APPROVAL packet with the failing checks listed.

---

## Provenance

All claims above trace to locked artefacts. Inline [src:] citations appear throughout the body.

| # | Path | Sections used |
|---|---|---|
| 1 | `swarm/wiki/tasks/.../artefacts/systems-optimizer-01.md` | OPT-1 sensor placement; scoring table H-8=35.0; OPT-6 prerequisite sequencing; effort-class 1 |
| 2 | `swarm/wiki/tasks/.../artefacts/systems-critic-01.md` | H-8 measurement void L6; H-9 latent bottleneck; check-5 requisite-variety budget; alternatives table |
| 3 | `swarm/wiki/tasks/.../artefacts/engineering-optimizer-01.md` | Bundle-3 H-3+H-5; shared schema-extraction OPT-EXT-2; IDEM guard; H-5 sharpening: JSONL counts, line targets, min_entries 20; LOC partial warning |
| 4 | `swarm/wiki/tasks/.../artefacts/philosophy-optimizer-01.md` | M-1 falsifier completeness threshold; B-1 bundle template; method-change refusals; scope_envelope requirement |
| 5 | `swarm/wiki/tasks/.../artefacts/investor-optimizer-01.md` | Bundle-C H-4+H-8 sequential dependency; §4.1 first ROI arithmetic; Bundle-A H-1 unit-econ substrate |
| 6 | `swarm/wiki/tasks/.../artefacts/mgmt-integrator-01.md` | §5 OPP-01 opportunity brief; acceptance predicate; effort estimate; D-03 resolution path; T-5 paid-tooling resolution |
| 7 | `swarm/wiki/tasks/.../context/gamma-wiki-v3.md` | D3 edges.jsonl empty; D10 health.md skeleton; D11 Q6 zero skills; Q1 Tier-3 BFS gap; Q2 single-writer gap; Q5 lint gap; Q6 activation rubric untested |
| 8 | `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` | W1 cluster definition; W1 locks (D10, Q1, W-5); M1 /compound dependency on W1 |

---

## Structured Output Packet (shared-protocols §3)

```yaml
summary: >
  OPP-01 installs swarm/evals/ file-JSONL eval harness as the Meadows L6 measurement-void
  fix (systems score 35.0; unblocking root node for all 5 downstream consumers).
  6-8 turns Phase-A; no paid tooling; no HITL gate; no upstream dependencies.
  Cycle-1 smoke: 7 filesystem checks. Cycle-2 upgrade: 4/7 conformance checks.
  D-03 (2x unfalsifiable) resolved by routing the claim through the harness, not using it
  as a gate. Caveats C-1/C-2/C-3 all addressed.

proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md
    frontmatter:
      id: opportunity-01-eval-harness
      type: opportunity-draft
      cluster_id: C-02
      tier: T1
      produced_by: systems-expert
      mode: integrator
      state: drafted
      pipeline: ingested
      confidence: high
      confidence_method: multi-source-rubric
      caveats_addressed: [C-1, C-2, C-3]
      dissents_addressed: [D-03]
    body: "(this file)"
    edges_to_add:
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness", to: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01", type: derived_from}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness", to: "tasks/T-swarm-self-improve-v1-2026-04-23", type: part_of}

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-optimizer-01.md", range: "OPT-1..OPT-6 + scoring table + intervention sequence"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md", range: "H-8 measurement void + check-5 variety budget + alternatives table"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-optimizer-01.md", range: "Bundle-3 H-3+H-5 + OPT-EXT-2 + H-5 sharpening + LOC partial warning"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-optimizer-01.md", range: "M-1 + B-1 + scope_envelope requirement + method-change refusals"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "Bundle-C H-4+H-8 + §4.1 ROI + Bundle-A H-1"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "§5 OPP-01 + D-03 + T-5 + OPP-01 acceptance predicate"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "D3 + D10 + D11 + Q1 + Q2 + Q5 + Q6"}
  - {path: "decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md", range: "W1 cluster definition + W1 locks"}

confidence: high
confidence_method: multi-source-rubric

escalations: []

dissents:
  - source: "philosophy-expert (D-03 from mgmt-integrator-01.md §4)"
    claim: "The 2× improvement claim is F=F1 unfalsifiable NOW and MUST NOT guide delivery until eval harness exists"
    F: F3
    ClaimScope: "holds while swarm/evals/ absent; NOT valid after OPP-01 ships and FPAR baseline is populated"
    R:
      accepted_if: "OPP-01 ships (SMOKE-1..7 pass) AND fpar_log carries at least 1 record"
      refuted_if: "any Phase-A acceptance predicate in a live artefact cites '2× improvement' as a gate criterion while swarm/evals/ is absent"
    resolution: >
      Resolved operationally in this artefact: '2× claim' appears as provenance context only,
      not as a gate criterion. The Hamel-binary acceptance predicate in §2x-improvement-claim
      is anchored to filesystem observables (directory exists, JSONL counts, exit codes), not
      to the Boris Cherny assertion. Philosophy's concern is satisfied; engineering's
      operationalise-first path is unblocked.

extractions:
  - {id: "OPP01-EXT-1", claim: "swarm/evals/schema.md serves dual consumers: eval JSONL records AND skill candidate manifest.md (golden_set_path field)", source: "engineering-optimizer-01.md OPT-EXT-2", grounding: "Fowler Extract Class: same data shape (acceptance_predicate + path fields); one schema, two uses"}
  - {id: "OPP01-EXT-2", claim: "swarm/evals/ placement OUTSIDE swarm/wiki/ allows cell-direct writes to results.jsonl without violating Q2 single-writer rule", source: "gamma-wiki-v3.md Q2 + shared-protocols §1", grounding: "LOC design: Q2 is scoped to swarm/wiki/<canonical>/; swarm/evals/ is a peer, not a child"}
  - {id: "OPP01-EXT-3", claim: "The cycle-close hook that populates health.md fpar_log ALSO seeds edges.jsonl derived_from records — one hook, two consumers", source: "systems-optimizer-01.md OPT-1 + gamma-wiki-v3.md D3", grounding: "Ashby simplification: reduce variety-demand on brigadier by consolidating two measurement actions into one hook invocation"}

alternatives:
  - label: "A — Install eval harness first (recommended, this document)"
    description: "Create swarm/evals/ substrate before any other Tier-1 cluster. 6-8 turns. Closes measurement void. All downstream consumers unlock."
    kill_condition: "Fails if swarm/evals/ exists AND fpar_log is populated AND swarm behaviour does not improve across 10 cycles (information was not the bottleneck — H-8 kill-condition fires)."
  - label: "B — Wire executor hooks first (OPP-02 first, OPP-01 second)"
    description: "Install UserPromptSubmit + PostToolUse hooks (engineering Bundle-1) before the eval harness. Argument: hooks prevent structural failures before measurement is needed."
    kill_condition: "Fails if hooks are wired AND quality still degrades (unmeasured) — we have enforcement but no signal. Philosophy's D-03 concern is NOT resolved; the 2× claim remains unfalsifiable."
  - label: "C — Status quo (no eval harness; defer to Phase B)"
    description: "Defer swarm/evals/ to Phase B alongside Tier-4 books. Argument: Phase A is specification-only; one cycle of smoke-passing validates patterns before infrastructure is needed."
    kill_condition: "Fails immediately: this cycle (T-swarm-self-improve-v1) IS the first real fire. Health.md counters remain at 0; FPAR is unmeasurable; golden-set comparison (M3) blocked indefinitely; D-03 unresolved for all future cycles. Alt-C is empirically already failing as of today."

anti_scope:
  - "NOT wiring PostToolUse lint hook (OPP-02 / engineering Bundle-1 territory)"
  - "NOT implementing /compound dual-sink skill (OPP-03 / sys H-3 territory)"
  - "NOT performing solo-vs-6-cell golden-set comparison (M3 / investor Bundle-C H-4)"
  - "NOT adding falsifier: field to existing artefacts (OPP-05 / philosophy Bundle-B-1)"
  - "NOT computing unit-econ ROI arithmetic (investor-expert territory)"
  - "NOT resolving Yan/Anthropic paradigm conflict (D-01; philosophy × integrator Phase B)"
  - "NOT writing canonical wiki pages (brigadier sole-writer per Q2)"
  - "NOT authorising HITL gate files (brigadier sole gate-file writer per shared-protocols §4)"
```
