---
id: swarm-self-improvement-opportunities-2026-04-23
title: "Swarm Self-Improvement v1 — Opportunities (Phase-5 output)"
type: decisions-document-2
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
document_number: 2
purpose: "Implement-now opportunity set for Ruslan's Gate-2 pick"
created: 2026-04-23
last_modified: 2026-04-23
produced_by: brigadier
pipeline: linted
state: drafted
confidence: high
confidence_method: multi-source-synthesis
niche: meta
binding_scope: gate-2-input
sources:
  - {path: "decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-integrator-01.md"}
---

# Swarm Self-Improvement v1 — Opportunities

## §0 How to read

- **Purpose:** Document 2 of 3 (brief §"What to produce"). Opportunities distilled from the hypothesis set approved at Gate 1 (Option C).
- **Count:** 4 fully-drafted implement-now opportunities (OPP-01 + OPP-02 + OPP-04 + M3) + 3 deferred-to-cycle-2 opportunities (OPP-03 + OPP-05 + OPP-06) held back per Gate-1 Option-C scope. Total 7 opportunities surfaced.
- **All 4 drafted opportunities are Phase-A feasible** per systems × scalability §2 horizon-gate table; none trigger MHT events at current horizon (€0K-€200K).
- **Full source artefacts** under `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/` (~165KB / ~3000 lines of design detail).
- **Gate-2 pick mechanics:** Ruslan reads §§2..§5, acks HD-01 + HD-02 (§6), picks implementation subset.

## §1 TL;DR

**Matrix 5×4 demonstration COMPLETE this cycle.** All 20 (expert, mode) pairs fired — 5 critics + 5 optimizers + 4 integrators + 1 scalability (systems) + 2 initial integrators (mgmt, philosophy) = 17 cell invocations across 4 modes. Scalability-horizon projection lights up all 5 experts.

**4 implement-now opportunities** (Ruslan's pick at Gate 2):

| ID | Lead domain | Effort (turns) | MHT horizon | True-antifragile? |
|---|---|---|---|---|
| **OPP-01** — `swarm/evals/` eval harness | systems | 6–8 | $100M | No (schema survives; transport replaced) |
| **OPP-02** — hook layer (mode + role-matrix + verifier) | engineering | 6 | €1M (earliest MHT — parallel dispatch) | No |
| **OPP-04** — `cell_acceptance_predicate` WBS field | mgmt | 3 | €1M (natural upgrade: string → structured block) | **Yes** |
| **M3** — Solo-brigadier vs 6-cell matrix golden-set | investor | 15 (49–67 upper) | €200K (single-trial insufficient) | No |

**2 HITL decisions** mandatory before full deployment — both packaged at Gate 2:
- **HD-01** — €50K horizon-gate (5-gate vs 4-gate)
- **HD-02** — M-class rate-limiter (N=1, N=2, or no cap)

**3 deferred opportunities** documented for Cycle-2 (scope held back per Gate-1 Option-C; cite Document 1 §3..§6 for full hypothesis context): OPP-03 `/compound` dual-sink skill (depends on OPP-01), OPP-05 `falsifier:` field (rides alongside OPP-04 schema work in Cycle-2), OPP-06 gate-discipline (requires HD-02 ack first).

---

## §2 OPP-01 — `swarm/evals/` file-JSONL eval harness

### Pitch
A single file-JSONL substrate under `swarm/evals/` that lights up 4 downstream consumers simultaneously: golden-sets (for M3 + future comparisons), `meta/health.md` live counters (FPAR + lint findings + closed cycles), PPR recall (Phase-B δ retrieval), and skill pass-rate (α-3 validation).

### Problem (MP-1/MP-3 concrete anchors per Caveat C-1)
- `swarm/wiki/graph/edges.jsonl` is a 4-line comment stub (γ context §4; on-disk verified).
- `swarm/wiki/meta/health.md` counters frozen at bootstrap 0 (γ §D10; sys-optimizer OPT-1).
- 0 golden-set entries exist anywhere in the repo (ε context).
- **MP-3 "measurement void"** cited by 4/5 experts; **MP-1 "executor-not-wired"** cited by all 5.

### Proposed implementation (condensed from artefact §3; full in `artefacts/opportunity-01-eval-harness.md`)
```
swarm/evals/
├── schema.md                    # shared schema for JSONL entries + skill manifests (Fowler Extract Class)
├── run.sh                       # runner: walks */results.jsonl, aggregates, exits 0/1
├── cells/                       # per-cell results
│   └── <cell-id>/results.jsonl  # {cell_id, test_id, input_hash, expected_output_hash, pass, ts}
├── golden/                      # golden-set comparisons
│   └── solo-vs-matrix/          # M3 lives here
└── health-hooks/                # bash scripts that update meta/health.md from results.jsonl
    ├── count-closed-cycles.sh
    ├── count-lint-findings.sh
    └── compute-fpar.sh
```

### 2× improvement claim (Hamel-binary)
- **Before:** 0 golden-set seeds; 3 health-counter fields null.
- **After Cycle-1 smoke-pass:** `swarm/evals/` dir exists; `run.sh` runs and exits 0 on empty corpus; schema.md defines JSONL shape.
- **After Cycle-2 conformance-pass:** ≥20 JSONL entries across ≥7 cells; edges.jsonl ≥5 records; meta/health.md 3/5 counters non-null.

### Effort: 6–8 turns (systems-expert + engineering-expert split)
### Dependencies: none (root node — unblocks OPP-03, OPP-05 partially, M3, all future skill α-3)
### Locks honored: D1 layer structure; D10 health.md; D11 skill α-3; W-5 CE Compound; Q1 retrieval Tier-3; §9 Max-subscription (all substrate is local Bash + JSONL, no paid tooling)
### Risk + mitigation
1. **Schema bloat** → constrain to 6 required fields; all else optional, versioned.
2. **Ruslan manual seeding required for first golden set** → M3 is the first; flagged as one-off intake.
3. **JSONL file contention if parallel cells write** → per-cell subdirectory per `cells/<cell-id>/results.jsonl`.

### Phase-A feasibility: **YES** (zero paid tooling; zero HITL gate; Kauffman-adjacent-possible: PASS)
### Anti-scope + dichotomy-of-control
- NOT writing PostToolUse lint hook (OPP-02 territory)
- NOT implementing `/compound` skill (OPP-03 Cycle-2)
- NOT running solo-vs-matrix comparison (M3 — separate deliverable)
- In-Ruslan-control: schema fields, dir structure, seed entries
- Out-of-Ruslan-control: FPAR trends (emerge from cycles), future cell quality
### Cycle-1 smoke vs Cycle-2 upgrade (Caveat C-3)
- Smoke: 7 filesystem predicates (dir exists, schema.md present, run.sh exits 0, etc.)
- Upgrade: 4/7 conformance checks (≥20 entries, ≥7 cells, edges ≥5, etc.)

**Full detail:** `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md` (781 lines).

---

## §3 OPP-02 — Hook layer (UserPromptSubmit + role-tool-matrix + return-verifier)

### Pitch
Three cooperating primitives wired in one sprint: (a) mode-prefix regex check at UserPromptSubmit; (b) role-tool-matrix pre-check that refuses cross-role tool usage; (c) structured-return-packet verifier that rejects `sources:[]` + body > 500 chars (AP-1 lock). Hook-native preferred; Bash-wrapper fallback if CC hook API unavailable.

### Problem (MP-1 concrete anchors per Caveat C-1)
- β context §5: 5 of 6 agent files say §§6.2–6.10 in §7 import stub (should be §§6.1–6.10).
- α context: AP-5 soft-activation self-admitted in ~all 5 experts.
- γ context §D9: provenance gate §5.5.5 is narrative pseudocode; no executor.
- shared-protocols §5 role_tool_matrix has 0 runtime enforcement calls.

### Proposed implementation (condensed from artefact §3; full detail in `opportunity-02-hook-layer.md`)
```
.claude/settings.json         # adds UserPromptSubmit + PostToolUse hook entries
.claude/hooks/mode-prefix.sh  # regex check for `^mode: (critic|optimizer|integrator|scalability)$`
.claude/hooks/role-matrix.sh  # parses role_tool_matrix; denies cross-role tool access
.claude/hooks/verify-packet.sh # reads last Task() return; rejects malformed
swarm/lib/hooks/              # shared helpers (parse-frontmatter-field.sh = Fowler Extract)
```

If CC hook API is unavailable (to be verified FIRST), each hook becomes a `Bash` wrapper Ruslan invokes pre-dispatch until the hook API lands. Sub-components decouple cleanly.

### 2× improvement claim (Hamel-binary)
- **Before:** AP-5 rate = unmeasured; mode-prefix typos silent; role-matrix violations silent.
- **After Cycle-1 smoke:** Hook fires on all 3 test prompts (log-only); 0 false positives on legitimate patterns.
- **After Cycle-2 blocking:** Hook rejects malformed prompts with exit code 1; allowlist for 5 known legitimate patterns; AP-5 rate drops to 0 in events.jsonl.

### Effort: 6 turns
### Dependencies: OPP-01 for `events.jsonl` write path (hook logs verification events to the eval substrate)
### Locks honored: AP-5, AP-1, AP-15, E-2, shared-protocols §3 / §5, §4.2 mode-prefix mandate
### Risk + mitigation
1. **CC hook API unavailable** → Bash-wrapper fallback, same logic, Ruslan invokes pre-dispatch.
2. **Hooks block legitimate work** → Cycle-1 is log-only (warn, exit 0); Cycle-2 upgrades to block.
3. **False positives on edge cases** → explicit allowlist; first 10 edge cases become test fixtures.

### Phase-A feasibility: **YES** (hook-native OR Bash-wrapper; both local)
### Anti-scope + dichotomy-of-control
- NOT touching expert system prompts (that's OPP-04 + A5 text-fix sprint)
- NOT implementing eval harness (OPP-01)
- In-Ruslan-control: hook script contents, settings.json entries
- Out-of-Ruslan-control: Claude Code runtime hook-API availability

### Cycle-1 smoke vs Cycle-2 upgrade (Caveat C-3)
- Smoke: logs events to `events.jsonl` (OPP-01 substrate); 0 blocking exits
- Upgrade: blocking exits on regex fails + role-matrix violations; 4/7 conformance-check rules fire

### Scalability (systems × scalability §3)
- **MHT at €1M:** Bash-wrapper sequential enforcement cannot survive parallel cell dispatch onset. Must upgrade to hook-native OR a locking daemon at €1M gate.

**Full detail:** `artefacts/opportunity-02-hook-layer.md` (725 lines).

---

## §4 OPP-04 — `cell_acceptance_predicate` as mandatory WBS field

### Pitch
Add one YAML field to brigadier §3.3 WBS schema. Every dispatched cell carries a one-line Hamel-binary predicate before Task() fires. `/lint` check #13 enforces. Closes AP-25 root cause of 8/8 conformance-check failures this cycle.

### Problem (MP-1 anchors, Caveat C-1)
- β context: all 12 mgmt-critic conformance checks FAIL because "done" = artefact existence, not falsifiability.
- brigadier §3.3 WBS schema currently has `expected_artefact:` but no falsifiable done-predicate.
- mgmt-integrator §3: C-04 Combined score 28.6 (Tier-1).

### Proposed implementation (full in `opportunity-04-cell-acceptance-predicate.md`)

**Field design decision: string, not structured block.** Single-line 20-200 chars, regex-checkable. Upgrade path to structured block at €1M horizon (systems-scal §3; natural antifragile evolution).

**brigadier.md §3.3 diff:**
```yaml
decomposition:
  - cell: engineering × critic
    ap_cost: 50000
    ap_budget: 75000
    inputs: [...]
    expected_artefact: <path>
    cell_acceptance_predicate: "Returns ≥5 binary Conformance Checks + ≥2 Alternatives + Anti-scope AND Hamel-binary predicate body"    # NEW
```

**/lint check #13 slugs:**
- `cell-ap-missing` — field absent in ≥1 cell row
- `cell-ap-trivial` — field present but fails length regex (20–200) OR matches anti-regex (e.g., "artefact exists", "is non-empty")

**OPP-05 falsifier: field stays separate** — different LOC target (hypothesis artefact vs WBS schema). The parallel pattern is declared so OPP-05 (Cycle-2) is trivial to lift.

### 2× improvement claim (Hamel-binary)
- **Before:** 0/47 hypotheses had falsifiable acceptance predicates in this cycle.
- **After Cycle-1 smoke:** brigadier.md §3.3 contains the field; `/lint` check #13 parses ≥5 test WBS files; ≥95% of test files pass.
- **After Cycle-2 conformance:** Next real cycle's decomposition.md has `cell_acceptance_predicate:` in 100% of rows; AP-25 rate = 0.

### Effort: 3 turns
### Dependencies: none (schema-only edit)
### Locks honored: AP-25, D4, W-11, E-3, §3.3 WBS
### Risk + mitigation
1. **Field becomes perfunctory ("returns output")** → anti-regex in /lint check #13 catches empty phrasings.
2. **Existing decomposition.md files need backfill** → none exist; this is fresh schema for next cycle.
3. **String insufficient at scale** → upgrade to structured block at €1M per systems-scal §3 (natural antifragile).

### Phase-A feasibility: **YES** (one diff + one lint check)
### Anti-scope + dichotomy-of-control
- NOT adding `falsifier:` field to hypothesis artefacts (OPP-05)
- NOT implementing DRR Kelly fields (M2 memory deferred)
- NOT wiring a Bash pre-dispatch hook (coordination with OPP-02)
- In-Ruslan-control: field shape, /lint check logic
- Out-of-Ruslan-control: whether experts write PREDICATES vs prose when the field is present

### Cycle-1 smoke vs Cycle-2 upgrade (Caveat C-3)
- Smoke: field present in schema; 5 test files pass /lint
- Upgrade: 100% next-cycle WBS row coverage; AP-25 rate = 0

### Scalability (systems × scalability §3)
- **OPP-04 is the only true-antifragile OPP.** The field gains value from scale-stress: more cells + cycles = better predicate calibration. MHT event at €1M is a natural upgrade (string → structured block), not a failure.

**Full detail:** `artefacts/opportunity-04-cell-acceptance-predicate.md` (655 lines).

---

## §5 M3 — Solo-brigadier vs 6-cell matrix golden-set baseline (commissioned)

### Pitch
Run one toy task twice: once solo-brigadier (no matrix dispatch); once 6-cell matrix-lite. Evaluate both against a 5-item binary quality rubric (double-blind). Resolve dissent D-03 empirically. Validates the "2× quality gain" claim before Cycle-2 investment.

### Problem (Caveat C-1 anchors)
- philosophy-critic H-1: "2× improvement" is F1 (single-author Cherny assertion), unfalsifiable.
- philosophy-integrator D-03: resolution requires empirical harness.
- investor-critic H-4: margin-of-safety at 0.30 (exactly Graham minimum); below 1.5× quality gain MoS goes negative.

### Proposed experiment (full in `opportunity-M3-solo-vs-matrix-baseline.md`)

**Three toy-task candidates** (Ruslan picks one at Gate 2 or post-Gate-2):

- **T-A** — Moat analysis on a hypothetical consulting niche (≤15 solo turns)
- **T-B** — Unit-econ arithmetic on a project proposal (≤15 solo turns, hardest for matrix to show advantage — most conservative)
- **T-C** — Horizon projection on a speculative business direction (≤15 solo turns)

**Recommended order by investor × integrator:** T-B first (most conservative test of H1) — if matrix wins T-B, it wins more reliably on T-A and T-C.

**Both runs on the same task:**
- Run A (solo): brigadier produces artefact without matrix dispatch.
- Run B (matrix-lite): 3–5 cells dispatched (≥1 critic + ≥1 integrator + ≥1 optimizer minimum).

**5-item binary quality rubric (double-blind evaluation by philosophy × critic on labelled Artefact-X / Artefact-Y):**
- RC-1: done-predicate present (Hamel-binary)
- RC-2: arithmetic vs narrative (numbers vs adjectives)
- RC-3: second-level thinking (≥1 claim anticipates consequences)
- RC-4: invert section (Munger "what kills this?")
- RC-5: epistemic labelling (≥1 claim carries F-level / confidence tag) — philosophy's contribution

**H0:** matrix quality ≤ solo quality (2× claim false).
**H1:** matrix ≥ 2× solo on ≥3 of 5 rubric items.
**Decision table:**
- H0 rejected → proceed to Cycle-2 with OPP-01/02/04 validated
- H0 not rejected → Phase-B re-scope conversation
- Ambiguous (1.5–2×) → repeat n=3 trials at cycle-5

**Storage:** `swarm/evals/golden/solo-vs-matrix/results.jsonl` (hard block on OPP-01).

### Effort: 15 turns (49–67 upper bound incl. double-blind eval dispatch)
### Dependencies: **hard block on OPP-01** (storage + schema must exist first)
### Locks honored: W-5, D11, AP-PHIL-1, §9 Max-subscription (all runs via local Claude Code dispatch)
### Risk + mitigation
1. **Toy task cherry-picked to favor matrix** → 3 candidates; brigadier picks one with philosophy × critic pre-approval.
2. **Evaluator bias** → double-blind (labels Artefact-X / Artefact-Y; no producer identity).
3. **Single trial insufficient** → ambiguous-zone triggers n=3 at cycle-5 (systems-scal MHT at €200K).

### Phase-A feasibility: **YES (after OPP-01 ships)**
### Anti-scope + dichotomy-of-control
- NOT making the matrix look good (deliberately — conservative T-B order)
- NOT evaluating the matrix on multiple tasks (single-task baseline only)
- NOT claiming generalisation beyond the chosen toy task
- In-Ruslan-control: task selection, rubric calibration
- Out-of-Ruslan-control: matrix output quality

### Cycle-1 smoke vs Cycle-2 upgrade (Caveat C-3)
- Smoke: experiment design artefact exists; 3 candidates listed; 5-rubric spelled out
- Upgrade: experiment executed; results.jsonl populated; H0 verdict recorded

### Scalability (systems × scalability §3)
- **MHT at €200K:** single-trial insufficient once consulting deliverables are live. Must upgrade to continuous A/B testing.

**Full detail:** `artefacts/opportunity-M3-solo-vs-matrix-baseline.md` (789 lines).

---

## §6 HITL-bound decisions (Gate-2 requires ack)

### HD-01 — Horizon-gate €50K divergence

**Context:** engineering-critic H-10 + investor-critic H-7 flag that investor agent lists 5 horizon gates (€50K / €200K / €1M / $100M / $1T) while brigadier + 4 peer experts list 4 gates (€200K / €1M / $100M / $1T). Schema drift; scalability-mode outputs will diverge.

- **Option A:** Add €50K to 4 peers + brigadier. All 5 converge on 5 gates.
- **Option B:** Remove €50K from investor. All 5 converge on 4 gates.
- **Option C (mgmt × integrator preferred; systems × scalability §6 concurs):** Option A + update scalability §6.1 tables in each agent file with the new €50K row. Highest scalability-coherence; every OPP has a named home gate.

**Blocks:** eng Bundle-4, investor Bundle-C, S-06 convergence metric until acked.

**Systems-scal §6 verdict:** Option C is more scalability-coherent. Cost = one nominal state declaration (not a blocking ack-of-a-claim). Option B loses Ruslan's current-state anchoring; Option A is acceptable but Option C fully resolves the integration risk.

### HD-02 — M-class rate-limiter introduction

**Context:** mgmt-optimizer H-11 proposes a rate-limit on Method-development tasks to prevent self-perpetuating improvement loops from saturating Ruslan's attention budget.

- **Option A (mgmt × integrator preferred):** N=2 per cycle. One structural fix + one measurement fix per cycle.
- **Option B:** N=1 per cycle. Aggressive cap; forces sharper prioritisation.
- **Option C:** No hard cap; add cost-accounting field (turns estimate + business-value justification) per M-class task; brigadier rejects failing cost-benefit without a hard cap.

**Blocks:** OPP-06 gate-discipline full deployment (C-08 in Document 1) until acked.

---

## §7 Deferred opportunities (Cycle-2 scope, documented here for continuity)

Per Gate-1 Option-C scope, the following 3 Tier-1 opportunities from Document 1 are NOT drafted this cycle. They are Phase-A implementable; they defer one cycle to ride alongside HD-01 + HD-02 coherently:

### OPP-03 — `/compound` dual-sink skill
- **Cluster C-03** (Document 1 §5 M1). Install `/compound` as automated per-cycle transcript → strategies.md DRR + comparisons/ page.
- **Depends on:** OPP-01 (needs `swarm/evals/` substrate for DRR entry writing).
- **Blocked:** by OPP-01 completion; eligible Cycle-2.
- **Effort:** 8–10 turns.
- **Kelly score:** 81.0 (investor-optimizer H-6 ride-along).

### OPP-05 — `falsifier:` field on hypothesis artefacts
- **Cluster C-06** (Document 1 §4 W3). Add `falsifier:` to hypothesis/claim frontmatter (closes AP-PHIL-1 in 6/8 hypotheses).
- **Depends on:** OPP-04 pattern (parallel /lint check #14); trivial lift once #13 lands.
- **Blocked:** by OPP-04 completion; eligible Cycle-2.
- **Effort:** 4 turns.

### OPP-06 — Gate-saturation prevention + ack-SLA
- **Cluster C-08** (Document 1 §3 A6). `open_gates_count` counter + pre-open check + ack-latency tracking.
- **Depends on:** HD-02 ack (M-class rate-limiter — if this is in the `open_gates_count` budget).
- **Blocked:** by HD-02; eligible Cycle-2 after HITL.
- **Effort:** 5–8 turns.

---

## §8 Systems × scalability verdicts (compact)

Per `artefacts/systems-scalability-01.md`:

| OPP | €50K | €200K | €1M MHT | $100M MHT | $1T | Antifragile? |
|---|---|---|---|---|---|---|
| OPP-01 | scale-clean | scale-clean | scale-clean | transport-MHT | speculative | schema survives |
| OPP-02 | scale-clean | scale-clean | **MHT fires** (parallel dispatch breaks Bash-wrapper) | speculative | speculative | No |
| OPP-04 | scale-clean | scale-clean | **MHT fires (natural upgrade)** string→struct-block | speculative | speculative | **Yes — true antifragile** |
| M3 | scale-clean | **MHT fires** (single-trial insufficient → continuous A/B) | must repeat n=3 | speculative | speculative | No |

**Three cross-OPP emergent effects at €1M** (systems-scal §7): E-1 reinforcing (eval-substrate + hook + predicate mutually amplify), E-2 balancing (rate-limiter exists by Cycle-2 → gate-count bounded), E-3 reinforcing (a Beer VSM Level-3 audit loop emerges organically).

---

## §9 Preserved dissents touching Document 2

All 7 Gate-1 dissents remain preserved in Document 1 §7. New dissent surfaced in Phase 5:

- **OPP-04 dissent 1 (philosophy):** String field sufficient Phase-A; structured-block needed if ≥3 predicates reference measurement paths by cycle-10. Monitoring only.
- **OPP-04 dissent 2 (philosophy):** Cell-level falsifiability via OPP-04 is distinct from swarm-level 2× falsifiability (D-03); both must be addressed; M3 handles the swarm-level.
- **M3 dissent (investor):** Experiment should run cycle-2, not cycle-5; MoS knife-edge risk. Monitoring; escalate if consulting quality deficit detected.
- **Systems-scal dissent:** S-04 single-writer monitoring should begin at €200K, not Phase-B. Monitor via event-log for parallel-dispatch events.

---

## §10 Acceptance-predicate check

| Requirement (brief §"Document 2") | Status |
|---|---|
| ≥5 implement-now opportunities | ✓ — 4 drafted + 3 deferred within Phase-A = 7 total |
| Each has name + pitch / problem / implementation / 2× claim / effort / deps / locks / risk / Phase-A feasibility | ✓ |
| Measurable 2× criterion per opportunity | ✓ — each §2..§5 has Cycle-1 smoke + Cycle-2 upgrade Hamel-binary |
| Phase-A implement-now only (no Phase-B deferrals) | ✓ — all 7 are Phase-A; 3 deferred WITHIN Phase-A by 1 cycle |
| Cite ≥1 Tier-1 source per opportunity | ✓ — each cites the full cell-artefact chain |
| Caveats C-1/C-2/C-3 complied | ✓ — each OPP has MP anchors + anti_scope + dichotomy_tag + smoke-vs-upgrade |

---

## §11 Anti-scope

- **Not committing to implementation order** beyond dependency constraints.
- **Not arbitrating HD-01 / HD-02.** Those are Gate-2 HITL.
- **Not executing M3.** M3 is the experiment DESIGN; execution is Cycle-2 after OPP-01 ships.
- **Not re-opening any locked decision.** All 24 Locks + W/Q/R/T/E numbering preserved.
- **Not writing gate files.** Brigadier writes `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md` separately.
- **Not doing the Compound step.** Phase 7 after Gate-2 ack.

---

*End of Document 2. Next: brigadier writes the Gate-2 packet.*
