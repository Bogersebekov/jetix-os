# swarm/evals/schema.md

Canonical schema contract used by:

- `swarm/evals/cells/<cell-id>/golden-set.jsonl` — seed entries.
- `swarm/evals/cells/<cell-id>/results.jsonl` — per-run output (append-only).
- `swarm/evals/cells/hook-layer/events.jsonl` — OPP-02 enforcement events (same pattern; extra `component` field).

One JSON object per line. No trailing commas. No pretty-printed blocks.

---

# Section A — eval JSONL record fields

Per OPP-01 artefact §3 (lines 156-219 verbatim, with the full 8-field
required set as in the authoritative spec — meta-brief's "6 required
fields" is a short summary; the artefact declares 8 required).

```yaml
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
```

**min_entries floor:** run.sh emits `WARN: golden-set floor not reached
(have N, need 20)` when total JSONL entries across all cells < 20 (per
OPP-01 §3 line 292-294). 20 is the Hamel-valid threshold for pass-rate
measurements to be statistically meaningful.

**Append-only invariant:** `results.jsonl` uses `>>` not `>`; re-running
never overwrites, always appends with fresh timestamp.

---

# Section B — skill manifest fields (Fowler Extract Class shared-consumer)

This schema also serves as the manifest format for
`swarm/wiki/skills/candidates/<slug>/manifest.md` (`golden_set_path` field).
One schema; two consumers. Section A (above) covers eval JSONL records;
Section B (below) covers skill candidate manifests per engineering-optimizer-01
OPT-EXT-2 (Fowler Extract Class).

Skill manifest fields (additive to Section A):

```yaml
skill_manifest_fields:
  slug:
    type: string
    required: true
    description: "kebab-case skill slug; matches manifest.md parent dir"
  golden_set_path:
    type: string
    required: true
    description: "relative path to swarm/evals/cells/<cell-id>/golden-set.jsonl"
  activation_threshold:
    type: float
    required: false
    default: 0.70
    description: "pass-rate floor for promotion from candidate → learning per D11 §11.5"
  min_entries:
    type: int
    required: false
    default: 20
    description: "entry-count floor for statistical validity; aligns with Section A min_entries"
```

**Section-A / Section-B split rationale:** per OPP-01 §11 Risk 4
("schema.md shared-consumer coupling"). Changes to Section A are
additive JSONL fields and do NOT require action on Section B.
The `/lint` check for manifest validity references only Section B.
The two sections share the `acceptance_predicate` string field semantically.

---

# Versioning

Schema versioning is done via section-level additive only. Breaking
changes (renaming or removing required fields) require a new top-level
section (Section C) with migration note. Current version: **v1.0
(cycle-2-impl 2026-04-24, cycle-1 smoke baseline).**
