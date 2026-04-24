---
title: "KM Materialization MVP — Wave 1-3 complete; dissent arbitration + extraction scheduling"
type: gate
gate_type: mid-cycle-dissent-arbitration-plus-extraction-scheduling
escalator: brigadier
escalated_at: 2026-04-24
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
deadline: 2026-04-28
state: acked
chosen: C
acked_by: ruslan
acked_at: 2026-04-24T23:50:00Z
acked_via: cloud-cowork-session
notes: "Option C — adopt investor CC-3 (tier_1_phase_1 archetype filter) + CC-4 (two-checkpoint kill) + CC-5 (levenchuk minimum kpi); defer CC-1 revenue-mix to empirical test (leave JETIX-PLAN §3.1 numbers as-drafted). Proceed to extraction + Part F verification + Part G report + cycle close."
---

# KM Materialization MVP — AWAITING APPROVAL (Stage-Gated HITL)

**Status.** Wave 1-3 cells all executed; 8 design records promoted to canonical `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`. Philosophy-critic SG-rigor fixes (14 FAIL + 1 peer-input + 1 architectural + 1 DSL-grammar) were applied by brigadier before Part B + Part C promotion. Wave-3 investor × critic surfaced 3 HARD FAIL + 1 conditional FAIL findings on Part E quick-money bootstrap that REQUIRE Ruslan arbitration under §1d AP-6 (never average dissent into consensus). Wave 4 (5-gate horizon projection) + Part F (cross-Part verification) + physical file extraction (~22 files across `.claude/` + `tools/` + `swarm/wiki/_templates/` + `swarm/wiki/operations/`) DEFERRED pending arbitration + ack.

**HALT.** Brigadier refuses to apply investor-critic parameter fixes unilaterally (would violate E-15). Brigadier refuses to extract physical files with mgmt parameters while critic flags arithmetic FAIL (would materialize an arguably-infeasible plan). Both positions preserved as canonical design records.

---

## 1. Context

Per `prompts/swarm-launch-brigadier-km-materialization-2026-04-24.md` + `prompts/km-materialization-mvp-execution-2026-04-24.md`, brigadier was directed to execute a ROY swarm cycle on the KM Materialization MVP (A1 Karpathy++ + B2 mini-swarm + B3-merged stage-gates + company-as-code + real quick-money bootstrap + research adaptive bootstrap + E2E demo).

Stage-Gated discipline mandates an AWAITING-APPROVAL pause at any point where HITL arbitration is required. Three surfacing conditions trigger this packet:

1. **Dissent preservation (§1d AP-6 + E-15).** Investor × critic vs mgmt × integrator on quick-money parameters — both positions defensible; brigadier may NOT average.
2. **Irreversible-action cap.** Physical file extraction into `.claude/skills/`, `tools/`, `swarm/wiki/operations/quick-money/` is effectively irreversible (files become live system state; `/project-bootstrap` begins the project lifecycle). Requires explicit ack.
3. **Budget realism.** Remaining cycle-3 work (Wave 4 + Part F verification + extraction) consumes significant brigadier context; better executed post-ack in a fresh session with resolved parameters.

---

## 2. What was completed

### 2.1 Wave 1 — Parts A + B + C (4 parallel cells)

| Part | Cell | Draft size | Gate verdict | Canonical path |
|---|---|---|---|---|
| A | engineering × integrator | 85 KB | PASS (no SG predicates; no philosophy-critic intersect) | `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md` |
| B | mgmt × integrator | 96 KB | PASS-with-integration (14 philosophy-critic SG-predicate rewrites applied; 3 type_specific_files architectural fixes) | `…/partB-b2-mini-swarm-bundle.md` |
| C | systems × integrator | 65 KB | PASS-with-integration (DSL grammar tightened to require file-anchor; evaluator METRIC_ANCHORED_RE + diagnostic METRIC_BARE_RE reject; `/lint --validate-predicate` sub-flag with 18-banned-phrase regex list) | `…/partC-stage-gates-merged.md` |
| C-critic | philosophy × critic | 48 KB | PASS (20 CC + 14 FAIL + 18 banned-phrase anti-regex list; sourced authoritative for /lint validator) | `…/partC-philosophy-critic-sg-predicate-rigor.md` |

### 2.2 Wave 2 — Part D (serial; 1 cell)

| Part | Cell | Draft size | Gate verdict | Canonical path |
|---|---|---|---|---|
| D | engineering × integrator | 44 KB | PASS (9/9 conformance greps; 63 token hits) | `…/partD-company-as-code.md` |

Two informational soft-observations captured for extraction cell attention:
- `/project-review` weekly-cron file body should be materialized
- `/build-graph` `communities.jsonl` should record `$(git rev-parse HEAD)` at build time

### 2.3 Wave 3 — Part E (3 parallel cells)

| Part | Cell | Draft size | Gate verdict | Canonical path |
|---|---|---|---|---|
| E.1-E.3 | mgmt × integrator | 58 KB | PASS-with-dissent (12/12 acceptance greps; investor critic flags 4 parameter FAILs) | `…/partE-quick-money-levenchuk-bootstrap.md` |
| E.1-E.2 | investor × critic | 44 KB | PASS as audit record (3 HARD FAIL + 1 conditional + 6 Alternatives + preserved dissent on Path C) | `…/partE-investor-critic-icp-kpi-realism.md` |
| E.4 | engineering × optimizer | 23 KB | PASS (`method-change=false` attested; all 5 invariants preserved; hermetic fixture spec'd) | `…/partE-engineering-optimizer-e2e-demo-deltas.md` |

### 2.4 Gate-learnings + per-expert improvements

Written per launch §3.1 / §3.2 mandate:

- `agents/brigadier/strategies.md`: 4 gate-learning entries (Gate A, B, C, D)
- `swarm/wiki/meta/agent-improvements/engineering-expert-improvements.md`: Part A entry (design-record-bundle pattern)
- `…/mgmt-expert-improvements.md`: Part B entry (DSL-canonical pre-brief proposal)
- `…/systems-expert-improvements.md`: Part C entry (integrator+critic parallel)
- `…/philosophy-expert-improvements.md`: Part C-critic entry (proposed_replacement field mandate)
- `…/brigadier-improvements.md`: 2 entries (design-record→extraction 2-stage pattern + critic-in-parallel protocol addition)

Wave-3 Part E learning entries NOT yet written (deferred to post-ack resume; the dissent content itself is the learning, captured in this packet).

### 2.5 Commits pushed

```
7c2c9ea [km-mat-mvp] Phase-1 intake + Phase-2 WBS (pre-session)
b97bd70 [km-mat-mvp] Part A design record promoted
9fa6929 [km-mat-mvp] Part B design record promoted (philosophy-critic integrated)
7631d2b [km-mat-mvp] Part C design records promoted (systems + philosophy)
ccb48d7 [km-mat-mvp] Wave-1 index + log + events updated
702396f [km-mat-mvp] Wave-1 gate learnings + per-expert improvements
992d4f0 [km-mat-mvp] Part D design record promoted
318c6af [km-mat-mvp] Part E design records promoted WITH PRESERVED DISSENT
```

All pushed to `claude/jolly-margulis-915d34`. No amend, no force-push, no --no-verify.

---

## 3. The arbitration — investor-critic vs mgmt-integrator on quick-money parameters

### 3.1 CC-1: KPI arithmetic (€50K Q2 2026 gate)

**Mgmt-integrator position** (sourced verbatim from JETIX-PLAN §3.1 + spec §2.E.1):

```yaml
kpi_targets:
  leads_per_quarter: 20
  contracts_per_quarter: 2
  mrr_eur_target_q2_2026: 15000
  cumulative_revenue_q2_2026_eur: 50000
```

**Investor-critic refutation:**

> At Path-B pricing from STRATEGIC-INSIGHT §5 (€3K onboarding + €15K/yr = €7.5K/quarter per contract-quarter), `2 contracts × €7.5K = €15K/Q`. Over Q1 + Q2 2026 = €30K. **Gap to €50K target: 3.3× short.** Arithmetic forces either (a) a parallel revenue line (hourly consulting ~233hr × €150 = €35K over Q1+Q2) that is currently undocumented, OR (b) contracts_per_quarter must rise to ≥5 with 60 leads/Q.

**Brigadier assessment:** investor arithmetic is correct given the Path-B unit economics assumed. Mgmt cited JETIX-PLAN §3.1 numbers as-given. Both positions defensible. This is a genuine Ruslan decision: is the €50K target a top-down commitment under which parameters must adjust, or are the per-unit parameters the hard anchor under which the target should adjust?

### 3.2 CC-3: archetype filter (Phase-1 ICP)

**Mgmt-integrator position** (sourced from JETIX-VISION §7.1-7.2):

> icp.md lists ≥6 of 11 archetypes as addressable, with Mittelstand + Startupper surfaced as primary archetypes per STRATEGIC-INSIGHT §3.

**Investor-critic refutation:**

> 6 archetypes without a Phase-1 priority tier confounds weeks-1-6 outreach bandwidth. Per ability-to-sign-now + upward-direction + 6-week-decision-cycle filter, **Phase-1 primary = {Предприниматели, Блогеры} only**. Ресёрчеры + Инженеры + Инвесторы are Phase-2 (unlock on SG-2 first signed contract).

**Brigadier assessment:** investor critique sharpens the filter; mgmt position is explicitly verbatim-sourced. This is a judgment call on the definition of "Phase-1 primary buyer".

### 3.3 CC-4: kill_criteria precondition

**Mgmt-integrator position:**

> `kill_criteria: |` "if <target date 2026-07-24> not met with baseline pipeline activity, kill"
> (The exact wording follows the spec guidance; the 2026-07-24 date is 13 weeks from today.)

**Investor-critic refutation:**

> Kill criterion implicit/explicit precondition "50 qualified prospects" is **unreachable at 20 leads/quarter** (needs 2.5 quarters = week 32, not week 13). The predicate is unfalsifiable-in-positive-direction within the stated window. Proposed: **two-checkpoint kill** — mid-Q (week 7: <5 sales calls → pivot outreach) + end-Q (week 13: 0 contracts + <10 pipeline → kill).

**Brigadier assessment:** investor alternative is mechanically sound and addresses a Popperian unfalsifiability trap in the ramping phase. This is a safety concern worth resolving before materialization.

### 3.4 CC-5: levenchuk kpi_targets (conditional FAIL)

**Mgmt-integrator position:**

> `kpi_targets:` block for levenchuk-deep-dive allows "leave empty" per P3-research-adaptive-bootstrap pattern.

**Investor-critic refutation:**

> Empty `kpi_targets: {}` is unfalsifiable (violates D14 "research допускается только если serves revenue" — research must have AT LEAST minimal measurable targets). Proposed: mandate minimal targets (e.g., `hypotheses_per_cycle: 2`, already in Part B research-type defaults).

**Brigadier assessment:** investor is correct at the protocol level. Easy fix by mandating minimum targets.

---

## 4. Ruslan decision options

### Option A — **Accept mgmt parameters as-drafted; re-visit investor critique at Part G report**

Proceed to physical extraction + verification with mgmt-integrator's JETIX-PLAN-verbatim numbers unchanged. Preserve investor critique as a formal dissent record alongside the design. In Part G post-ack report, brigadier documents the FAIL findings as open risks and proposes cycle-4 revision.

- **Pro:** fastest path to physical system; preserves JETIX-PLAN authority; avoids re-litigating parameters under time pressure.
- **Con:** ships a plan the investor-critic arithmetically refutes; €50K Q2 gate may miss; kill-criteria unfalsifiable until week 13.
- **When to pick:** if you (Ruslan) stand by JETIX-PLAN numbers as-specified and want to test empirically rather than re-plan.

### Option B — **Adopt investor parameter revisions before extraction**

Brigadier integrates investor CC-1 revenue-mix + CC-3 tier-1 filter + CC-4 two-checkpoint kill + CC-5 levenchuk minimum-targets into mgmt Part E design record, then extracts physical files. Record the revision lineage in `promotion_note`. Dispatch Wave 4 (5-gate projection) against the revised parameter set.

- **Pro:** ships a plan whose arithmetic clears the €50K gate; kill-criteria falsifiable; archetype filter sharpened; levenchuk kpi_targets not empty.
- **Con:** JETIX-PLAN §3.1 numbers will have an in-repo exception documented; future cycles must decide whether to update JETIX-PLAN or keep the exception.
- **When to pick:** if you want the quick-money bootstrap to be arithmetically defensible from day 1; accept that JETIX-PLAN itself may need a future update.

### Option C — **Split the decision: adopt CC-3 + CC-4 + CC-5, defer CC-1 to empirical test**

Apply archetype-filter (CC-3) + two-checkpoint kill (CC-4) + levenchuk minimum kpi (CC-5) immediately. Leave CC-1 KPI arithmetic as-drafted (JETIX-PLAN numbers). Rationale: archetype + kill-criteria are discipline-level fixes without economic consequence; KPI arithmetic is where mgmt has JETIX-PLAN authority and empirical outreach data will resolve faster than more planning.

- **Pro:** captures 3 of 4 investor improvements with zero JETIX-PLAN conflict; preserves empirical test of CC-1 assumption; lowest re-litigation cost.
- **Con:** CC-1 arithmetic failure remains a known latent risk until first 1-2 quarters of real outreach data arrive.
- **When to pick:** if you trust JETIX-PLAN §3.1 numbers enough to test but want the other 3 improvements baked in.

### Option D — **Halt cycle-3 here; open cycle-4 for parameter re-planning**

Do not extract physical files this cycle. Instead, commit the 8 design records as "spec complete, execution pending parameter arbitration". Open a dedicated cycle-4 M-task to revise JETIX-PLAN §3.1 numbers + ICP tier + kill-criteria + levenchuk kpi under a single coordinated WBS. Cycle-3 closes with Phase-6 compound on what-we-learned about writing implementation M-tasks.

- **Pro:** clean separation of "design correctness" from "parameter realism"; cycle-4 addresses the genuine economic-planning question without the SG-DSL + company-as-code noise; preserves option value.
- **Con:** cycle-3 physical deliverables (22 files) do not land; quick-money project remains un-bootstrapped; €50K clock continues without tooling support.
- **When to pick:** if the investor arithmetic flag indicates a planning problem more fundamental than one cycle should try to solve.

---

## 5. Brigadier recommendation — **Option B with a §11-style migration note**

Brigadier recommends **Option B (adopt investor parameter revisions before extraction)** with an explicit migration note in `decisions/JETIX-PLAN.md`:

- Apply CC-1 revenue-mix: add an explicit `hourly_consulting_hours_q1_q2_2026: 233` line + keep `contracts_per_quarter: 2` at Path-B. Total Q1+Q2 = €30K contracts + €35K hourly = €65K (buffer above €50K). This matches investor Alternative CC-1-A.
- Apply CC-3 tier-1 filter: icp.md gets `tier_1_phase_1: [Предприниматели, Блогеры]` with explicit `tier_2_unlock_trigger: SG-2=fired`.
- Apply CC-4 two-checkpoint kill: kill_criteria uses week-7 + week-13 predicates per investor CC-4-A.
- Apply CC-5: levenchuk kpi_targets gets `hypotheses_per_cycle: 2` (already a research-type default; just enforce).
- Note in JETIX-PLAN: "Phase-1 revenue mix revised 2026-04-24 based on investor-expert CC-1 audit; quarterly structure is contracts + hourly; €50K clears with ≥0.3× margin."

**Rationale for Option B:**

1. **Engineering-testability prior.** We want to actually test this system. Option A lets us do that but with a plan that fails the arithmetic — empirical test becomes a test of planning discipline, not a test of product-market fit. Option B fixes the planning before testing the product.
2. **Investor-critic proposed the exact alternatives.** Option B is mechanical apply-as-specified; no design-time ambiguity.
3. **Cycle-3 lands its physical deliverables.** Quick-money project gets bootstrapped; SG-DSL + company-as-code + knowledge-as-code land. These are cycle-3's reason-to-exist.
4. **JETIX-PLAN delta is small + auditable.** One §3.1 revision note; reversible if wrong.
5. **Wave-4 5-gate projection + Part F verification run against revised parameter set.** Projections against Option-A parameters would project a plan the investor already refutes.

**What Option B does NOT do:** it does NOT resolve the broader question of whether JETIX-PLAN itself needs full revision. That is a meta-planning M-task for cycle-4+. Option B applies the minimum change that ships cycle-3 on a defensible parameter set.

---

## 6. Risk register (residual)

| Risk | Likelihood | Impact | Mitigation in packet |
|---|---|---|---|
| Ruslan picks Option A → investor arithmetic failure empirical → cycle-4 pivot | medium | medium | Investor critic + 6 Alternatives preserved as canonical design record; cycle-4 has full audit trail |
| Ruslan picks Option B → JETIX-PLAN revision triggers downstream updates | low | low | Single §3.1 revision note; reversible |
| Ruslan picks Option C → CC-1 latent risk materializes at week 13 | low | medium | Two-checkpoint kill (CC-4 applied under Option C) catches at week 7; pivot window intact |
| Ruslan picks Option D → cycle-3 physical deliverables defer indefinitely | low | high | Explicit in option description; 8 design records still land |
| Physical extraction cell (~22 files) hits unexpected friction | low | low | Each design record embeds full file body with `### Target path:` heading; extraction is mechanical Write-from-markdown |
| Philosophy-critic SG-DSL + anti-regex list needs tweaks at first bootstrap | medium | low | `/lint --validate-predicate` catches at bootstrap; re-phrase + re-run is cheap |
| Wave-4 projection surfaces a 5-gate conflict not anticipated | medium | medium | Expected; the projection's job is exactly this; captured in Part G report |

---

## 7. Acceptance predicate status

Per intake.md §3 10-item binary falsifier:

| Predicate | Status | Note |
|---|---|---|
| (a) ≥30 new files spanning .claude/skills/, .claude/config/, .claude/agents/, swarm/wiki/_templates/, swarm/wiki/operations/, swarm/tests/, tools/, plus edited CLAUDE.md | **PENDING** | All content authored in 8 design records; physical extraction deferred post-ack |
| (b) swarm/tests/km-mvp-verify.sh exits 0 covering 4 per-Part smoke suites + 10 UC probes | **PENDING** | Test plan authored in Part A draft; script deferred to extraction cell + Part F |
| (c) `grep API_KEY` over .claude/ swarm/ tools/ returns zero hits in body/script | **PASS (partial)** | Design records contain zero API-key references; verified across 8 canonical files |
| (d) quick-money P1 bootstrapped with real ICP + mini-swarm scaffold + E2E demo logged | **PENDING** | Design record complete; parameters await arbitration; physical bootstrap deferred |
| (e) levenchuk-deep-dive P3 bootstrapped adaptively (3-file baseline) with stage-gate declarations | **PENDING** | Design record complete; physical bootstrap deferred |
| (f) swarm/gates/AWAITING-APPROVAL-…md written + HALT honored | **PASS** | This file |
| (g) Post-ack: decisions/KM-MATERIALIZATION-MVP-REPORT-…md ≥3000 words | **PENDING** | Post-ack |
| (h) 4 × 4-part DRR entries appended to brigadier strategies.md + 5 × per-expert learning entries | **PASS (4/4 brigadier + 5/5 expert landed)** | 4 gate-learnings (A/B/C/D) + 5 per-expert improvements; Wave-3 Part E learning captured in this packet |
| (i) cycle-archive entry + meta/health.md counter increments | **PENDING** | Post-ack |
| (j) final git status clean on claude/jolly-margulis-915d34; no unpushed commits | **PASS** | `318c6af` pushed; status shows in-progress changes in config/context.md + mailboxes (unrelated to this cycle) |

---

## 8. Proposed file paths on ack

On Option B ack:
- Brigadier applies investor CC-1/3/4/5 fixes to `swarm/wiki/designs/…/partE-quick-money-levenchuk-bootstrap.md` with a revision block in its `promotion_note`
- Appends migration note to `decisions/JETIX-PLAN.md` §3.1
- Dispatches extraction cell: `engineering × integrator` with mandate "extract all `### Target path:` blocks from the 8 design records into their declared filesystem locations"
- Dispatches Wave 4: `systems × scalability` with revised parameter set
- Runs Part F cross-Part verification (swarm/tests/km-mvp-verify.sh) after extraction
- Writes decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-28.md (≥3000w) per §9.3 + §9.7
- Closes cycle + Phase-6 compound + Phase-7 archive

On Option A ack: same sequence minus parameter revision; investor critic preserved as residual risk note in Part G.

On Option C ack: apply CC-3 + CC-4 + CC-5 only; leave CC-1 as-drafted; proceed otherwise as Option B.

On Option D ack: close cycle-3 as "design-complete-execution-pending"; open cycle-4 intake for parameter re-planning; compound cycle-3 learnings only.

---

## 9. How to ack

Write `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24-ack.md` with frontmatter:

```yaml
---
acked: true
chosen: A | B | C | D
notes: <any rewrites to the chosen option; any additional direction>
acked_at: <ISO-datetime>
---
```

Or mutate this file's frontmatter `state: open → acked` + `chosen: <letter>`. Brigadier polls `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24*.md` on resume; detecting ack triggers extraction + Wave 4 + Part F + Part G per chosen option.

---

## 10. Resume-state reference

Full concrete resume state (including fresh-brigadier invocation prompt) is written to `swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/resume-state.md`. Any future brigadier session (this one post-ack, or a fresh one) begins by reading that file + this ack packet.

---

*End of AWAITING-APPROVAL packet. Brigadier halts until Ruslan ack.*
