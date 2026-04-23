---
title: "AWAITING-APPROVAL — Swarm Self-Improvement v1, Gate 2 (Opportunity approval + HD-01 + HD-02)"
type: gate
gate_type: catch-all
escalator: brigadier
escalated_at: 2026-04-23
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
deadline: 2026-04-24
state: open
gate_number: 2
of_gates: 2
gate_cost_turns: 3
packages_decisions: [HD-01, HD-02]
---

# AWAITING-APPROVAL — Gate 2 (Opportunity approval + 2 HITL decisions)

## Context

**Phase 5 complete.** 4 Phase-5 opportunity drafts produced + 1 scalability-horizon-projection pass.
**Matrix 5×4 FULLY lit this cycle**: all 5 experts × all 4 modes fired (17 cell invocations total).

Document 2 written at `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` (357 lines).
Full opportunity artefacts at `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-*.md` (~3000 lines / ~165KB).

**What Ruslan decides at Gate 2:**
1. Which of the 4 drafted opportunities to commission for implementation.
2. **HD-01** — €50K horizon-gate resolution (blocks eng Bundle-4 + investor Bundle-C).
3. **HD-02** — M-class rate-limiter introduction (blocks OPP-06 full deployment in Cycle-2).
4. For M3 specifically: toy-task selection (T-A moat / T-B unit-econ / T-C horizon).

---

## §1 Drafted opportunities (Ruslan picks subset)

| # | ID | Pitch | Effort | Dependencies | MHT horizon | Antifragile? |
|---|---|---|---|---|---|---|
| 1 | **OPP-01** | `swarm/evals/` file-JSONL eval harness (unblocking root node) | 6–8 turns | none | $100M | schema survives |
| 2 | **OPP-02** | Hook layer: mode-prefix + role-matrix + return-verifier | 6 turns | OPP-01 substrate for event logging | €1M (earliest) | no |
| 3 | **OPP-04** | `cell_acceptance_predicate:` mandatory WBS field | 3 turns | none | €1M (natural upgrade) | **YES** |
| 4 | **M3**    | Solo-brigadier vs 6-cell matrix golden-set baseline | 15 (49–67 upper) | hard block on OPP-01 | €200K | no |

**Dependency lattice (for scheduling):**

```
OPP-01 (eval harness, root)
   ├── OPP-02 (logs events to eval substrate)
   └── M3    (results to eval golden-set dir)
OPP-04 (WBS schema; independent)
```

**Parallelizability.** OPP-01 + OPP-04 can ship in parallel (zero shared LOC). OPP-02 needs OPP-01 substrate. M3 executes AFTER OPP-01 ships.

## §2 HD-01 — Horizon-gate €50K divergence

**Context:** investor-expert agent file declares 5 horizon gates (€50K / €200K / €1M / $100M / $1T); brigadier + 4 peer expert files declare 4 gates (drop €50K). This is a schema drift; scalability-mode outputs across experts will diverge.

### Options

- **Option A:** Add €50K to all 4 peers + brigadier (5 agents converge on 5 gates).
- **Option B:** Remove €50K from investor-expert (5 agents converge on 4 gates).
- **Option C (mgmt × integrator + systems × scalability preferred):** Option A PLUS update each agent's scalability-mode §6.1 table to include a new €50K row. Full schema parity.

### Brigadier recommends: **Option C**

Systems × scalability §6 verdict: **Option C is more scalability-coherent.** Every OPP has a named home gate (€50K). BOSC-A-T-X triggers anchor to Ruslan's current state (pre-€200K). Cross-expert integration risk (investor H-7 concern) is lower. Cost: one nominal state-declaration, no blocking-of-work.

**If Option B is chosen:** Ruslan must explicitly acknowledge that €50K is not a tracked milestone. The investor-expert dissent D-05 notes removing may require adding it back later (WLNK violation from premature removal).

## §3 HD-02 — M-class rate-limiter introduction

**Context:** mgmt-optimizer H-11 proposes a rate-limit on Method-development (M-class) tasks per cycle to prevent self-perpetuating improvement loops from saturating Ruslan's attention budget. (This very cycle is M-class, FYI.)

### Options

- **Option A (mgmt × integrator preferred):** N=2 per cycle. Allows one structural fix + one measurement fix per cycle. Maps to Bundle I + Bundle II cadence.
- **Option B:** N=1 per cycle. Aggressive cap; forces sharper prioritisation.
- **Option C:** No hard cap. Instead add `m_class_cost_turns:` + `m_class_business_value:` fields per M-class task; brigadier rejects failing cost-benefit without a hard cap.

### Brigadier recommends: **Option A** (N=2)

**Reasoning:** N=1 is too restrictive for current Phase-A where compounding improvements are genuinely valuable. N=2 pairs one structural + one measurement fix per cycle — matches the scope pattern emerging from this very cycle (OPP-01 measurement + OPP-02 structural + OPP-04 structural would violate N=2 which is why OPP-04 is bundled with OPP-01 by ultra-low-effort, effectively a one-item-plus-free-rider). Option C preserves flexibility but adds per-M-class-task overhead that compounds over cycles.

## §4 M3 toy-task selection

If M3 is approved, pick one of three candidate toy tasks:

- **T-A Moat analysis** — on a hypothetical consulting niche
- **T-B Unit-econ arithmetic** — on a project proposal (**recommended by investor × integrator**: most conservative test of H1; hardest for matrix to show advantage; highest information-per-turn)
- **T-C Horizon projection** — on a speculative business direction

**Brigadier suggests T-B** per investor's reasoning. Ruslan may pick differently if preference for demonstrating matrix value on real-deliverable-type pattern (then T-C).

---

## Options summary (composite ack format below)

Each ack chooses (a) opportunity set, (b) HD-01 option, (c) HD-02 option, (d) M3 toy-task (if M3 approved).

### Option Alpha (full scope, maximalist) — brigadier ALT

Ship all 4 opportunities in Cycle-2. HD-01 C. HD-02 A. M3 toy-task T-B.

- **Effort Cycle-2:** 30–40 turns (4 opportunities + 2 HITL integrations)
- **Pros:** Maximum compounding Cycle-2; every Gate-1-approved item delivers
- **Cons:** Highest Cycle-2 load; if any OPP rejects at §5.6 gate twice, Cycle-2 stalls

### Option Beta (lean scope, fastest) — brigadier PRIMARY

Ship OPP-01 + OPP-04 + M3 in Cycle-2; defer OPP-02 one more cycle for hook-API clarity. HD-01 C. HD-02 A. M3 toy-task T-B.

- **Effort Cycle-2:** 24–32 turns
- **Pros:** All deliveries have clear Phase-A feasibility TODAY (no dependency on Claude Code hook-API availability question). D-03 gets resolved. Cycle-3 decides OPP-02 with more info.
- **Cons:** OPP-02 deferral delays AP-5 enforcement; MP-1 meta-pattern persists one more cycle.

### Option Gamma (structural-first, M3 last) — brigadier RISK-MITIGATED

Ship OPP-01 + OPP-02 + OPP-04 in Cycle-2; M3 in Cycle-3 (run against OPP-01's actual data). HD-01 C. HD-02 A.

- **Effort Cycle-2:** 15–20 turns
- **Pros:** Cycle-2 is pure infrastructure. M3 runs against a fleshed-out eval substrate (≥20 JSONL entries populated naturally), not an empty one. Experiment has more signal.
- **Cons:** Defers D-03 resolution by 1 cycle; MoS knife-edge concern per investor.

### Option Delta (Redirect)

Your custom scope. State it in `notes:` and brigadier re-issues.

---

## Recommendation

**Brigadier preferred: Option Beta** (OPP-01 + OPP-04 + M3; defer OPP-02; HD-01 C; HD-02 A; M3 T-B).

**Reasoning:**

1. OPP-02 has a **structurally unclarified dependency** on Claude Code hook API availability. It's drafted with a Bash-wrapper fallback, but shipping a fallback IS a method choice with long-term consequences. Better to verify API availability in a 5-minute investigation AND decide hook-native-or-wrapper on data, not on speculation.
2. OPP-01 + OPP-04 + M3 are all zero-API-dependency. Ship what's unambiguously ship-ready.
3. M3 in Cycle-2 (not Cycle-3) closes D-03 empirically per your Gate-1 Option-C ack intent. Matches your reasoning: "close the epistemic issue before Cycle-2 investment grows."
4. HD-01 C is the scalability-coherent choice — aligns with investor's €50K grounding AND preserves cross-expert parity.
5. HD-02 A (N=2) protects your attention without over-restricting.
6. M3 T-B is the tightest conservative test; investor's recommendation AND brigadier's pattern-match.

**If OPP-02 is high-priority for you,** Option Alpha is the correct full-send.
**If you want maximum Cycle-2 efficiency,** Option Gamma gives the richest M3 data.

## Risk

- **Option Alpha risk:** OPP-02 hook-API investigation could reveal unworkable-without-fallback scenario; Bash-wrapper becomes permanent, not interim. Affordable but has long-term cost.
- **Option Beta risk (brigadier preferred):** OPP-02 deferral leaves MP-1 meta-pattern executor-unwired for one more cycle. Observable in AP-5 event rate in Cycle-2 logs.
- **Option Gamma risk:** M3 Cycle-3 delay widens the D-03 open-dissent window; 2-cycle gap means decisions made on partial data. Tolerable if Cycle-2 is genuinely infrastructure-pure.
- **Option Delta:** Depends on your scope.

## Proposed file paths (on ack)

**All options write:**
- `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/decisions/<ts>-gate2-ack.md`
- Phase 7 Compound outputs: DRR entries across `agents/<expert>/strategies.md` (Layer-1) + `swarm/wiki/meta/agent-improvements/<target>-improvements.md` (Layer-2, brigadier is sole writer per Q2)
- Phase 8 cycle log: `swarm/wiki/operations/T-swarm-self-improve-v1-2026-04-23/cycle-01.md`

**HD-01 writes** (on Option C):
- Edits to `.claude/agents/{engineering,mgmt,systems,philosophy,investor}-expert.md` §6.1 tables + brigadier.md where horizon-gates are listed (1-line table row addition each)

**HD-02 writes** (on Option A):
- Edit to `.claude/agents/brigadier.md` §2.2 intake gate — add M-class rate-limit check

**M3 writes** (if approved):
- Task file for Cycle-2: `tasks/T-m3-solo-vs-matrix-<YYYY-MM-DD>.md`
- Toy-task spec: `swarm/wiki/tasks/<T-m3>/context/toy-task-spec.md`

## How Ruslan acks

Inline is easiest:
```
ack <Alpha|Beta|Gamma|Delta> — HD-01 <A|B|C> — HD-02 <A|B|C> — M3 <T-A|T-B|T-C|defer>
```

Example: `ack Beta — HD-01 C — HD-02 A — M3 T-B`

Or filesystem:
- Append `swarm/gates/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23-ack.md` with
  `acked: true`, `chosen: Beta|Alpha|Gamma|Delta`, `hd_01: <letter>`, `hd_02: <letter>`, `m3: <letter|defer>`, `notes: <optional>`
- Or mutate this file's frontmatter `state: acked` + set `chosen:` field.

On ack: brigadier:
1. Moves α-1 `gated → approved`.
2. Runs **Phase 7 Compound step** — writes strategies.md accretions across agents (Layer-1) + meta/agent-improvements entries (Layer-2).
3. Runs **Phase 8 cycle closure** — writes cycle-01.md, commits, halts.
4. Cycle-2 starts separately (new task, new brief from Ruslan).

---

## Provenance

- Document 2: `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md`
- Full opportunity artefacts (5):
  - `artefacts/opportunity-01-eval-harness.md` (781 L)
  - `artefacts/opportunity-02-hook-layer.md` (725 L)
  - `artefacts/opportunity-04-cell-acceptance-predicate.md` (655 L)
  - `artefacts/opportunity-M3-solo-vs-matrix-baseline.md` (789 L)
  - `artefacts/systems-scalability-01.md` (scalability projections)
- Phase-2 integration: `artefacts/mgmt-integrator-01.md`, `artefacts/philosophy-integrator-01.md`
- Document 1 (Gate 1): `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md`
- Cycle events: `swarm/logs/cyc-swarm-self-improve-v1-2026-04-23/events.md`

---

## Matrix 5×4 demonstration verification

| Expert | critic | optimizer | integrator | scalability |
|---|---|---|---|---|
| engineering | ✓ Round 1 | ✓ Round 2 | ✓ Phase 5 (OPP-02) | — |
| mgmt | ✓ Round 1 | ✓ Round 2 | ✓ Round 3 + Phase 5 (OPP-04) | — |
| systems | ✓ Round 1 | ✓ Round 2 | ✓ Phase 5 (OPP-01) | ✓ Phase 5 (horizon projection) |
| philosophy | ✓ Round 1 | ✓ Round 2 | ✓ Round 3 (meta-sanity) | — |
| investor | ✓ Round 1 | ✓ Round 2 | ✓ Phase 5 (M3) | — |

**5 critics + 5 optimizers + 6 integrator invocations + 1 scalability = 17 total cell dispatches across 4 modes. ≥4×≥2 floor overwhelmed; matrix demonstration complete.** Scalability remains a single-expert firing (systems); Phase-B will extend this.
