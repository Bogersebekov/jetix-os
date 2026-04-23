---
title: "AWAITING-APPROVAL — Swarm Self-Improvement v1, Gate 1 (Hypothesis review)"
type: gate
gate_type: catch-all                      # hypothesis-review is not in §6.1 trigger list; uses 10th catch-all
escalator: brigadier
escalated_at: 2026-04-23
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
deadline: 2026-04-24
state: open
gate_number: 1
of_gates: 2
gate_cost_turns: 3                        # per OPP-06 future policy; applied proactively now
---

# AWAITING-APPROVAL — Gate 1 (Hypothesis review)

## Context

First real swarm cycle (`cyc-swarm-self-improve-v1-2026-04-23`) completed Phase 1 + Phase 2 +
Phase 3. Matrix 5×4 fired **12 cells across 3 modes** (5 critics + 5 optimizers + 2 integrators) —
≥4×≥2 floor satisfied. 47 raw hypotheses were generated, clustered to 19, and assembled into
**Document 1: `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md`**.

**Gate 1 decision:** which clusters should proceed to Phase-5 opportunity drafting?

**Phase-2 matrix output quality summary** (all artefacts under
`swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/`, 12 files / ~6700 lines):

- 5 critics × (≥5 binary Conformance checks + ≥2 Alternatives + Anti-scope): 100% passed format-check
- 5 optimizers × (before/after snapshot + WLNK/MONO/IDEM/COMM/LOC invariants + measurable delta): 100%
- 2 integrators × (dissents[] preserved + provenance ≥10 inputs): 100% + SHIPPABLE-WITH-CAVEATS verdict

**What Ruslan is reading** — Document 1 (§1..§12) is the primary input. This gate file is the
≤1-page summary with the pick-list.

---

## Top-10 hypothesis clusters by combined score

(From Document 1 §1 + §3..§6 tables; full justification in
`swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md` §3.)

| Rank | Cluster | Tier | Dim | Combined | One-liner |
|---|---|---|---|---|---|
| 1 | C-02 / W1 (OPP-01) | T1 | Wiki | 55.6 | Install `swarm/evals/` eval harness — unblocks golden-sets + health counters + PPR recall + skill pass-rate |
| 2 | C-01 / A1+A2+A3 (OPP-02) | T1 | Agents | 42.3 | Wire `UserPromptSubmit` + role-tool-matrix + return-packet verifier hooks |
| 3 | C-03 / M1 (OPP-03) | T1 | Memory | 39.6 | Install `/compound` dual-sink skill (strategies.md + comparisons/) |
| 4 | C-04 / A4 (OPP-04) | T1 | Agents | 28.6 | Add `cell_acceptance_predicate:` as mandatory field in WBS schema |
| 5 | C-06 / W3 (OPP-05) | T1 | Wiki | 26.5 | Add `falsifier:` field to hypothesis/claim frontmatter |
| 6 | C-08 / A6 (OPP-06) | T1 | Agents | 26.1 | Gate-saturation prevention: `open_gates_count` + ack-SLA + pre-open check |
| 7 | C-05 / A5 | T2 | Agents | 22.3 | §7 SPEC stub numbering fix (5 agent files) |
| 8 | C-07 / W4 | T2 | Wiki  | 21.5 | Add `scope_envelope:` + `anti_scope[]` + `dichotomy_tag` blocks |
| 9 | C-13 / W5 | T2 | Wiki  | 18.7 | Add `turn_budget_used/allocated` to cell-return packets |
| 10| C-12 / SK1 | T2 | Skills| 17.5 | Canonicalise α-3 state vocabulary + wire `/promote-draft` |

**Ranks 1-6 are flagged as OPP-01..OPP-06 Tier-1 opportunity candidates** by mgmt × integrator;
Phase-5 drafts them into concrete opportunity-docs with implementation plans.

**Ranks 7-10** are T2 candidates — they improve the swarm but don't unblock downstream clusters.

**Remaining 9 clusters** (C-09, C-10, C-11 + S-01..S-06) are cross-referenced in Document 1 §3..§6.

---

## Preserved dissents (E-5 AP-6, Gate-1 critical)

Five from mgmt × integrator + two from philosophy × integrator. Full (F, ClaimScope, R) triples in
Document 1 §7. Summary only here:

1. **D-01 Yan vs Anthropic paradigm** — unresolvable Phase A; empirical at cycle-5 after OPP-02.
2. **D-02 H-2 NPV vs Kelly** — investor internal dissent; revisit at cycle-5.
3. **D-03 "2× improvement" measurability** — resolved operationally (no T1/T2 uses 2× as AP).
4. **D-04 Distributed orchestration** — Phase-A refusal stands; S-04 T3.
5. **D-05 €50K gate** — HITL-required (see HD-01, deferred to Gate 2).
6. **ADD-D-06 Scoring-weight derivation** — weights unverified empirically; revisit post-Gate-1 via investor × critic.
7. **ADD-D-07 "Partial verification"** — Cycle-1 is smoke-pass; upgrade standard at Cycle-2.

---

## Philosophy × integrator verdict: SHIPPABLE-WITH-CAVEATS

Three caveats brigadier folds into Phase-5 drafting (no action for you here):
- **C-1** Concrete anchors for MP-1 + MP-3 in every Phase-5 opportunity
- **C-2** Every Phase-5 opportunity draft has `anti_scope:` + `dichotomy_tag:`
- **C-3** Cycle-1 smoke-pass explicit; Cycle-2 upgrades to ≥4/7 conformance checks

---

## Options

### Option A — Approve all 6 Tier-1 opportunity candidates (OPP-01..OPP-06)

Proceed to Phase 5. Phase-5 drafts the 6 opportunities as concrete implementation plans. Gate 2
(Phase 6) presents those plans for final pick.

- **Pros:** Maximises material in Phase-5 for your selection. Most information per gate.
- **Cons:** Phase-5 produces 6 opportunity drafts (~500-800 lines total); Phase-6 pick is denser.
- **Risk:** You might prefer to narrow before drafting; that would reduce Phase-5 cost.

### Option B — Approve only OPP-01 + OPP-02 + OPP-04 (the 3 cheapest + most-unblocking)

OPP-01 eval harness (substrate), OPP-02 hooks (AP-5/AP-1 lock), OPP-04 cell-level AP
(schema fix). Skip OPP-03 `/compound` (depends on OPP-01), OPP-05 falsifier field (can ride along in OPP-04's schema work), OPP-06 gate discipline (requires HD-02 HITL which is a Phase-6 gate).

- **Pros:** 3 opportunities = lean Phase-5; each has zero dependency on the others.
- **Cons:** OPP-03 compounding loop is one of the two "real" Compounding-Engineering pieces — deferring it weakens the CE claim. OPP-06 gate discipline protects your attention budget.
- **Risk:** Narrower set delays compounding benefit by 1 cycle.

### Option C — Approve top-3 + ask brigadier for a "solo-brigadier vs matrix" baseline as M3

Approve OPP-01, OPP-02, OPP-04 AND explicitly commission the golden-set comparison
(M3 / S-05 / inv-H4: solo-brigadier vs 6-cell matrix on a toy task) as an additional Phase-5
deliverable. Validates the 2-3× quality claim before further swarm investment.

- **Pros:** Empirically grounds D-03 ("2× claim unfalsifiable today"). Cheapest first investor-grade
  ROI check. Supports the philosophy × integrator verdict directly.
- **Cons:** Adds Phase-5 scope (~3 turns extra). Delays OPP-03/05/06 by one cycle.
- **Risk:** If the comparison shows <1.5× quality gain, the investor margin-of-safety goes negative,
  which could trigger re-scoping at Phase-B.

### Option D — Redirect

Provide alternate direction: e.g., "I only want OPP-02 + OPP-04 this cycle", or "defer entire
self-improvement; ship consulting first", or any other custom scope. State it in `notes:` and
brigadier re-issues Phase-5 accordingly.

---

## Recommendation

**brigadier preferred: Option C** (top-3 + baseline comparison).

**Reasoning:** Four weighted factors converge here.

1. **Philosophy × integrator flagged D-03** ("2× improvement" unfalsifiable) as the single most
   upstream epistemic issue. Option C closes it before Phase-B.
2. **Investor × optimizer put Kelly score 90.0 on H-6 DRR fields + 81.0 on H-1 unit-econ** — both
   ride along in OPP-04 schema work. Bundle these with the baseline comparison = highest capital
   efficiency Phase A.
3. **OPP-06 gate discipline depends on HD-02** (M-class rate-limiter ack). That's a Gate-2
   decision. Option A puts OPP-06 in Phase-5 drafting but it will block at Gate 2 on HD-02 anyway —
   Option C pre-empts that friction by deferring OPP-06 to the next cycle where HD-02 can ship
   alongside it coherently.
4. **Cycle-1 is definitionally smoke-pass** (ADD-D-07). Loading it with 6 opportunities is
   maximalist; Cycle-2 with 3 validated opportunities + the solo-vs-matrix comparison data gives
   better compounding inputs for Cycle-3 decisions.

**If you disagree with the prioritisation, Option A is the safe default** — you see all 6 drafts
and pick at Gate 2.

---

## Risk

- **Option A risk:** Phase-5 produces more than strictly necessary; ~6-10 extra turns Phase-5, most
  drafts land anyway. Low material risk.
- **Option B risk:** OPP-03 deferral leaves the Compounding-Engineering claim thin for another
  cycle. Low tangible risk; high narrative cost.
- **Option C risk:** If the baseline comparison yields <1.5× quality gain, the Phase-B investor
  thesis requires re-scoping. This is actually a feature (investor-grade discipline), not a bug —
  but if you'd rather not trigger that re-scope conversation now, choose A or B.
- **Option D risk:** Depends on your redirect content.

---

## Proposed file paths (written on ack, per chosen option)

**All options write:**
- Phase-5 updates to `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/` (opportunity drafts)
- `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` (Document 2)
- `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md` (Gate 2 packet)

**Option A adds:** drafts for OPP-01..OPP-06 (6 files).
**Option B adds:** drafts for OPP-01, OPP-02, OPP-04 only (3 files).
**Option C adds:** same 3 as B + `artefacts/golden-set-solo-vs-matrix-01.md` + small run under
`swarm/evals/golden/solo-vs-matrix/*.jsonl`.
**Option D adds:** per your redirect.

---

## How Ruslan acks

Ack via either:
(a) Reply inline with `ack A` / `ack B` / `ack C` / `ack D — <notes>`.
(b) Append `swarm/gates/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23-ack.md` with
    frontmatter `acked: true`, `chosen: <A|B|C|D>`, `notes: <optional>`.
(c) Mutate this file's frontmatter `state: acked` + `chosen: <letter>`.

On ack detection, brigadier:
1. Moves α-1 `gated → approved`.
2. Proceeds to Phase 5 with the chosen opportunity set.
3. Writes Document 2 and Gate-2 packet.
4. Pauses again at Gate 2 (HD-01 + HD-02 + opportunity picks).

---

## Provenance

- Document 1: `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md`
- Master synthesis artefact: `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md`
- Meta-sanity: `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-integrator-01.md`
- All 10 cell artefacts + 6 context extractions under `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/`
- Cycle events: `swarm/logs/cyc-swarm-self-improve-v1-2026-04-23/events.md`
- Strategies accretion (Layer-2 self-writes): 4 agents updated
  - `agents/engineering-expert/strategies.md`
  - `agents/mgmt-expert/strategies.md`
  - `agents/systems-expert/strategies.md`
  - `agents/investor-expert/strategies.md`
  - (philosophy-expert and brigadier strategies writes happen at Phase-7 Compound step)

---

## Open observation for operator

**Max-sub discipline note.** Shell env shows `ANTHROPIC_API_KEY` / `GROQ_API_KEY` present at session
start. brigadier did NOT invoke either (all expert work is via Claude Code's subscription-bound
Task dispatch; file operations only). Per shared-protocols §9, the operator's SessionStart hook
should unset these; flagging only — no blocking.
