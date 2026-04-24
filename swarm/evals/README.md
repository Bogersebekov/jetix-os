# swarm/evals/ — OPP-01 Eval Harness (Phase-A file-JSONL substrate)

**Purpose:** file-JSONL substrate closing Meadows L6 measurement void (systems-critic-01.md
H-8, score 35.0 — highest-leverage intervention in the 9-hypothesis set). Every balancing
loop in the swarm requires a sensor; this directory is where the sensor data lives.

## Directory map

```
swarm/evals/
├── README.md                       # this file
├── schema.md                       # canonical JSONL record schema (Section A) +
│                                   # skill-candidate manifest fields (Section B)
├── run.sh                          # eval runner; aggregates */results.jsonl;
│                                   # exits 0 on empty corpus or all-pass; 1 on any FAIL
├── cells/                          # per-cell results (lazy-created; day-1 has 3 seed dirs)
│   ├── systems-critic/
│   │   ├── golden-set.jsonl        # ≥1 seed entry from cycle-1 artefacts
│   │   └── results.jsonl           # empty — run.sh appends on first eval
│   ├── engineering-optimizer/
│   │   ├── golden-set.jsonl
│   │   └── results.jsonl
│   └── systems-integrator/
│       ├── golden-set.jsonl
│       └── results.jsonl
├── golden/
│   └── solo-vs-matrix/             # M3 substrate stub — M3 task fills it
│       └── README.md
└── health-hooks/                   # bash scripts that update swarm/wiki/meta/health.md
    ├── count-closed-cycles.sh
    ├── count-lint-findings.sh
    └── compute-fpar.sh
```

## Q2 single-writer note

`swarm/evals/` is OUTSIDE `swarm/wiki/` so cells MAY append to their own
`cells/<cell-id>/results.jsonl` without violating Q2. The single-writer rule
(brigadier sole writer) is scoped to `swarm/wiki/<canonical>/` per shared-protocols §1.
This placement is a LOC (locality) design choice per OPP-01 §11 Risk 3. Cells MUST
NOT write to `swarm/wiki/<canonical>/` directly — that stays Q2-bound.

## Max-subscription note

Pure Bash + Python stdlib only. Zero paid embeddings, zero vector DBs,
zero third-party LLM APIs, zero provider-key references. The literal
provider env-var names are intentionally elided from files under
`swarm/evals/` so that grep over this directory returns zero hits —
making "no provider keys in the eval substrate" mechanically verifiable.
Per OPP-01 §10 Locks Honored + shared-protocols §9 + CLAUDE.md
Max-subscription discipline.

## Downstream consumers (4)

After installation `swarm/evals/` feeds the following (per OPP-01 §1 Pitch):

1. **Golden-sets** — `cells/<cell-id>/golden-set.jsonl` stores accepted
   artefact hashes per cell. Source-of-truth for M3 comparison + future
   quality comparisons.
2. **`meta/health.md` counters** — health-hooks/*.sh compute `fpar_log`,
   `closed_cycles_count`, `lint_findings_count` from JSONL records; brigadier
   or cycle-close ritual invokes.
3. **PPR recall (Phase B)** — δ retrieval Phase-B reads results.jsonl for
   relevance.
4. **Skill pass-rate (α-3 activation)** — D11 Q6 rubric requires
   golden-set.jsonl ≥3 entries + pass-rate ≥ 0.70 across last 5 evals to
   graduate a skill from `candidates` to `learning`.

## 1-line invocation

```bash
bash swarm/evals/run.sh           # exits 0 on empty corpus or all-pass
bash swarm/evals/run.sh --dry-run # no writes to results.jsonl
bash swarm/evals/run.sh --cell systems-critic  # filter to single cell
```

## Integration note — OPP-02 hook-layer events

The hook-layer (OPP-02, cycle-2-impl) writes enforcement events to
`cells/hook-layer/events.jsonl`. That 4th cell directory is created by Part B of
cycle-2-impl and uses the same schema.

## Phase-A scope

- NO PostToolUse lint hook (OPP-02 territory).
- NO `/compound` skill (OPP-03, Cycle-3+).
- NO execution of M3 solo-vs-matrix comparison (separate task after OPP-01 ships).
- NO paid tooling.

## Upgrade path

At €1M (per `systems-scalability-01.md` §3 OPP-01), file-JSONL hits
write-contention under ≥5 concurrent cells. Transport migrates to a
distributed event store; the **schema contract survives**, only the
transport replaces. Phase-A measure: `results.jsonl` append-only;
transport swap is an MHT event, not a failure.
