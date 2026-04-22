---
id: stage-7-scoring-and-summaries
title: Stage 7 Cross-Audit — Scoring Matrix + Executive Summaries (5 Variants)
date: 2026-04-22
author: server-cc (Opus 4.7 1M, extended-thinking max), independent cross-auditor
audience: Ruslan + Cloud Cowork (Stage 7 selection meeting)
status: ready-for-stage-7
formality: F2
reliability: R-medium
claim-scope: jetix-stage-7-cross-audit
depends_on:
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 §6 / §7 / §8 / §9 / §10)
  - decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md (1699 lines, self=79)
  - decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md (1684 lines, self=76)
  - decisions/variants/JETIX-ARCH-V3-DEEPTECH.md (1809 lines, self≈80)
  - decisions/variants/JETIX-ARCH-V4-HYBRID.md (1608 lines, self=77)
  - decisions/variants/JETIX-ARCH-V5-EMERGENT.md (1499 lines, self=73)
  - decisions/variants/_CRITIC-NOTES.md (V2 Pass-3 stress-tests)
  - 24 Locks: TENSIONS-PRE-RESOLVED.md (1-8) + TENSIONS-RESOLVED.md (9-18) + TENSIONS-RESOLVED-STAGE-2B.md (19-24)
non-goal: NOT a selection. Selection is Ruslan + Cloud Cowork on next step.
---

# Stage 7 Cross-Audit — Scoring + Executive Summaries

> **Role.** Independent cross-auditor (server-cc). NOT author of any variant; no
> self-score conflict. Applies D4 §8.1 rubric + §8.2 weights to all 5 variants;
> compares my scores to author self-scores; flags discrepancies; produces selection-
> ready data. Decision authority remains with Ruslan + Cloud Cowork.

> **Scope.** 5 variants (V1-V5). V6 WILDCARD not delivered — not in scope.

---

## Part 0 — Disqualifier Pass (§8.3, executed first)

Per D4 §9 Step A: eliminate variants violating §6 (C1-C21 hard constraints), exhibiting any
§7 anti-pattern, exceeding €800/mo Phase-1 run-rate without justification, or leaving any of
24 locks uncited.

| # | Variant | C1-C21 mechanism present? | AP-1..16 avoidance? | Phase-1 €/mo (claimed) | 24 locks cited? | Status |
|---|---|---|---|---|---|---|
| V1 | Conservative | Yes — §19 every C with mechanism | Yes — §20 every AP with guard | €350-450 (§9.4) | Yes — Appendix A | **ELIGIBLE** |
| V2 | Maximalist | Yes — §19 every C; *Flag 1: C14 reading on role-manifest layer requires Stage-7 ratification* | Yes — §20 every AP with hook | €320-520 (§9.3) | Yes — body + matrix | **ELIGIBLE** (with C14-reading flag) |
| V3 | Deep-Tech | Yes — §19 every C with FPF primitive + CI check | Yes — §20 every AP; AP-12 explicitly double-treated §20.1 | ≤€500 (§9.5) | Yes — Appendix A | **ELIGIBLE** |
| V4 | Hybrid | Yes — §19 every C invariant-level Phase-1 compliance | Yes — §20 every AP per phase | €300-800 (§9.4); single-provider runtime + multi-provider spec — *Flag 3 needs ratification on AP-11* | Yes — Appendix A | **ELIGIBLE** (with AP-11 reading flag) |
| V5 | Emergent | Yes — §19 every C; *C14 + C17 require argumentation, present in §4.4 + §8.4* | Yes — §20 every AP triple-statement on AP-3/9/10 | ≤€500 (§9.4) | Yes — Appendix B | **ELIGIBLE** (with C14/C17 argumentation flag) |

**No variant disqualified.** All 5 pass to scoring. Three soft flags (V2 C14 reading; V4
AP-11 reading; V5 C14/C17 argumentation) escalated to Part 4 for Stage-7 ratification.

---

## Part 1 — Scoring Matrix (Master Table)

Each cell = my cross-audit score (1-10). `(self: X)` shown when delta ≥2 between
self-score and my score, with one-line reason in Notes. Self-scores I did not adjust
significantly are shown in summary form below the matrix.

### 1.1 Default-weighted matrix (D4 §8.2 weights)

| # | Axis (weight) | V1 Con | V2 Max | V3 DT | V4 Hyb | V5 Em | Best | Notes (cross-audit, citations) |
|---|---|---|---|---|---|---|---|---|
| 1 | Phase-1 readiness (20%) | **9** | **6** | **5** | **8** | **6** | V1 | V1 deliberate minimum-delta runs Day 1 (V1 §3.1, §16); V4 forward-compat schemas add ~10% authoring tax (V4 §23.1) acceptable; V3 explicit 2-3wk formalism onramp (V3 §21.1 ax1); V2 ~8 Ruslan-weeks Foundation Day 1 (V2 §18.9); V5 week-1-4 sparse explicitly flagged (V5 §1, §23 R3) — *(self V5: 7, my: 6 — visible-progress deficit)*. |
| 2 | Scale trajectory (15%) | **6** | **9** | **9** | **8** | **7** | V2/V3 | V1 honestly flags 3 subsystems >30% refactor at MHT-2 (V1 §6.2); V2 schema-heavy = activation, not rewrite (V2 §6); V3 parametric ontology over fixed FPF primitives (V3 §6.1, §6.4 table); V4 forward-compat constructively guaranteed but token-B+matchmaker MHT-2 risk (V4 §23.4) — *(self V4: 9, my: 8)*; V5 SI invariants depend on promotion pipeline. |
| 3 | Foundation quality (15%) | **9** | **9** | **10** | **8** | **7** | V3 | V3 only variant with §18.9 10 Foundation Quality Invariants CI-enforceable Day 1; V1 §18 8 elements concrete; V2 8 elements full-fidelity Day 1 (V2 §18); V4 8 elements Day 1 unconditional but spread thinner; V5 trellis = Foundation but enforcement distributed (V5 §21.1 ax3) — author's honest 7. |
| 4 | Locks compliance (18%) | **9** | **8** | **9** | **9** | **7** | V1/V3/V4 | V1 Appendix A all 24 explicit (V1 §19, App A) — *(self: 10, my: 9 — Locks 4/6/9 inherit brief under-operationalization, App A §837)*; V2 §19 + 15 Lock-19 cites but C14 role-manifest-layer reading is contested (V2 §22 Flag 1) — *(self: 9, my: 8)*; V3 every lock with FPF primitive + CI check (V3 §19); V4 Lock-15 cited 6 sections (V4 App A); V5 C14/C17 require explicit argumentation acknowledged (V5 §21.1 ax4). |
| 5 | Universality (10%) | **7** | **8** | **9** | **8** | **8** | V3 | V3 strongest — `jetix-os/` schema-isomorphic to FPF, kit replication §12 validates 3 dry-runs, Hook 5 D-test = 0 hits; V2 base/overlay strict + ≥3 use-case templates Day 1 (V2 §3.3); V4 forward-compat schemas universal by design; V5 emergence-surface clean overlay; V1 Hook 2 D-test from Day 1 plus per-pilot config-overlays (V1 §3, §5.5). |
| 6 | Operational simplicity (10%) | **9** | **5** | **5** | **6** | **8** | V1 | V1 deliberate minimalism — onboarding ≤7d, founder + 1 part-time runs Phase-1 — *(self: 10, my: 9 — no architecture should claim 10/10 op-simp before 2nd-pilot validation)*; V2 surface area large, cognitive load 65% prob (V2 §23 R4); V3 learning cliff 5-7d for 7 hooks + 18 manifests + 4 kit-install + 6 protocols (V3 §21.1 ax6) — *(self: 4.5, my: 5 small lift for self-documenting fpf-manifests)*; V4 ≤7d above 5d soft target; V5 4 blocking hooks + simple bidding — *(self: 9, my: 8 — trellis spec is novel and requires reading)*. |
| 7 | Cost efficiency (gate, 0%) | **PASS** (9) | **PASS** (7) | **PASS** (8) | **PASS** (9) | **PASS** (8) | — | All in band. V1 €350-450 (§9.4); V2 €320-520 multi-provider (§9.3); V3 ≤€500 formalism=filesystem (§9.5); V4 single-provider runtime + spec (§22 Flag 3); V5 Haiku-default ≤€500. Proxy excluded from weighted total per §8.2/§8.3. |
| 8 | Resilience (5%) | **6** | **8** | **7** | **7** | **7** | V2 | V2 multi-provider Day 1 + tier-classified failover + Healthchecks.io (V2 §18.7); V1 multi-provider + git+SSH+Tarsnap, no hot-standby region; V3 §5.3 + §9.1 + §4.8 but crisis playbooks not written Day 1 (V3 §21.1 ax8); V4 phase-keyed — Phase-1 single-provider runtime weaker; V5 distributed enforcement less fault-tolerant to operator fatigue (V5 §21.1 ax8). |
| 9 | Security posture (5%) | **7** | **8** | **8** | **8** | **7** | V2/V3/V4 | V2 4-tier ACL + CP-5 + DPIA + threat model 8+4 Day 1 (V2 §8); V3 typed membrane + CP-5 + orthogonality invariant (V3 §8, §10.2); V4 4-tier ACL + GDPR Art.22 Day 1 + partner-tier runtime at MHT-2 (V4 §8); V1 4-tier via Unix perms + SOPS no novel runtime (V1 §8); V5 hard membrane but emergence-surface adds attack surface (V5 §21.1 ax9). |
| 10 | Innovation (2%) | **4** | **7** | **9** | **6** | **8** | V3 | V3 4 novel primitives — USB-C Phase-1 scaffold + typed-graph wiki + fpf-manifest per agent + orthogonality invariant (V3 §17, §7, §4, §10); V5 capability-capsule + bidding + emergence-triad (V5 §4.2, §11); V2 — *(self: 8, my: 7 — most "innovations" are disciplined application of known patterns; the schema-heavy/runtime-light pattern itself is the novel claim)*; V4 phase-progression-as-architecture is framing, not protocol (V4 §21); V1 4 honest (V1 §21). |
| **TOTAL (weighted /100)** |  | **80.0** | **75.8** | **78.0** | **78.9** | **70.2** | **V1** |  |

**Math (default §8.2; axis 7 excluded per §8.2 0% + §8.3 gate-only).** Sums per row of matrix
weighted by §8.2: V1 = 80.0; V2 = 75.8; V3 = 78.0; V4 = 78.9; V5 = 70.2.

**Hard-floor check (§8, axis < 3 → DQ):** No axis < 5 in any variant. PASS all.

**Self-score vs cross-audit deltas:**

| Variant | Self | Cross-audit | Δ | Note |
|---|---|---|---|---|
| V1 | 79 | **80.0** | +1.0 | Author conservative on §21 |
| V2 | 76.2 | **75.8** | −0.4 | Within rounding |
| V3 | ~80 (78.5-82.5) | **78.0** | −2.0 | Within author range |
| V4 | 77 | **78.9** | +1.9 | Most balanced; cross-axis interaction lifts |
| V5 | 73.2 | **70.2** | −3.0 | Phase-1 7→6, OpSimp 9→8; attributable to visible-progress deficit (V5 §1) |

No Δ ≥ 5 — no major author dishonesty. V5 −3.0 is the largest, sits just below author's stated 73-78 range.

### 1.2 Alternative-Weighting Sub-Table (Lock 19 emphasis)

D4 §8.2 explicitly permits architects to propose alternative weights with Lock citation. Per
**Lock 19 (D19, $1T no-rewrite trajectory)** + **D2 §14 *«Quality cannot be retrofit at $1T scale»***,
two variants (V2 Maximalist §21.2; V3 Deep-Tech §21) propose lifting Scale + Foundation
weights. I formalize the proposal — **NOT to override default, but to surface sensitivity**.

**Alt weights:** Phase-1 → 15% (from 20%); Scale → 20% (from 15%); Foundation → 18% (from 15%);
Locks → 15% (from 18%); others unchanged. Sum = 100%. Citation: **Lock 19 + D2 §14**.

| Variant | Default total | **Alt-weighted total (Lock 19 emphasis)** | Rank shift |
|---|---|---|---|
| V1 Conservative | 80.0 | **78.5** | 1st → 3rd |
| V2 Maximalist | 75.8 | **77.6** | 4th → 4th |
| V3 Deep-Tech | 78.0 | **80.3** | 3rd → **1st** |
| V4 Hybrid | 78.9 | **78.6** | 2nd → 2nd |
| V5 Emergent | 70.2 | **70.7** | 5th → 5th |

**Critical reading.** The default-weighting winner is **V1 Conservative (80.0)**. The Lock-19-
emphasis winner is **V3 Deep-Tech (80.3)**. **V4 Hybrid is stable at 2nd under both** (78.9 / 78.6).

This is the most consequential output of Part 1: **the choice of weighting determines the
nominal winner**. Stage 7 must explicitly decide whether the canonical §8.2 weights or a
Lock-19-justified reweight governs the selection. See Part 4 Q1.

---

## Part 2 — Executive Summaries (5 × ~400-600 words)

### V1 Conservative

**Self-score:** 79/100 (banked from 82.8) | **My weighted score:** 80.0/100 | **Status:** ELIGIBLE

**Thesis (1 sentence).** Minimum-delta evolution of the current `~/jetix-os/` repo into
explicit `jetix-os/` + `jetix-company/` factorization, with Foundation built uncompromisingly
Day 1 and every Phase-2/3 capability deferred to spec-only stubs — *evolve what works,
don't rewrite what isn't broken* (V1 §1).

**Top 3 strengths.**
1. **Phase-1 ships fastest** (axis 1 = 9). Manual matchmaker + design-only USB-C/token + static-
   site content stack means Day-1-to-€50K runway is shortest among 5 variants (V1 §3.1, §11.1, §17.1).
2. **Operational simplicity is genuinely 9** — solo founder + 1 part-time assistant operates
   Phase-1 from Day 1; new pilot cold-start ≤7 days (V1 §16.2).
3. **Locks compliance close to ceiling** (axis 4 = 9). §19 maps every C1-C21 to mechanism;
   Appendix A cites all 24 locks with primary location; pre-commit hooks enforce at commit
   time, not at audit time (V1 §3.3, §8.2, §16.5).

**Top 3 weaknesses/risks.**
1. **Scale trajectory honestly 6.** V1 §6.2 admits 3 subsystems exceed 30% LOC refactor target at
   Phase-2b (matchmaker, USB-C, token). Risk 1 (V1 §23.1) prices €30K-€60K Phase-2a refactor budget
   as engineering insurance — Ruslan must accept this cheque.
2. **Innovation 4** is a deliberate floor. V1 §22 explicitly notes USB-C runtime readiness
   "might matter Phase-2b if competitor-variant ships first" — strategic exposure window.
3. **Matchmaker founder-dependency risk** (V1 §23.5). Manual ICP review at >10 prospects/week
   strands Ruslan as bottleneck. Mitigation = Phase-1 day-45 partial automation.

**Phase-1 cost estimate:** €350-450/mo realistic, €300-800 envelope (V1 §9.4). Headroom for cache + reserve provider standby.

**Phase-3 scalability:** 6/10 — Phase-2a/2b refactor budget needed for matchmaker engine, USB-C runtime, token ledger, dashboard v2; 3 subsystems >30% rewrite (V1 §6.2).

**Critical assumptions** (if false → variant breaks).
- *Phase-2a refactor budget €30K-€60K is actually available* — if cash-flow-stressed at €200K, deferred subsystems pile up.
- *Competitor doesn't ship USB-C protocol Phase-1* — strategic exposure (V1 §23.2). 25% probability per author estimate.
- *Manual matchmaker scales to ≤10 prospects/week* — V1 §23.5 risk if Phase-1 outreach outperforms plan.

**Non-negotiable elements** (must survive in any hybrid).
- **Hook 1 asymmetric Jetix→Life-OS reference ban + Hook 2 D-test on `base/` subtree** (V1 §3.3, C9 / AP-5).
- **Compute-ledger hard-block at €800/mo** (V1 §9.3-9.4, C2).
- **`tools/icp_score.py` as first-class hard-gate** (V1 §11.5, C20) — direction-of-life axis as schema field.
- **§19 C1-C21 compliance matrix discipline** (V1 §19) — every constraint has named compliance mechanism.

**Red flags** (what lowered my score).
- Self-10 on Operational simplicity is unverifiable until 2nd pilot — adjusted to 9.
- Self-10 on Locks compliance treats Appendix A citation = full operationalization; brief itself flags Locks 4/6/9 as under-operationalized (D4 App A note §837). Adjusted to 9.

**Locks compatibility.** ✅ All 24 (App A); ✅ all 21 C with mechanism (§19); ✅ all 16 AP with guard (§20). Soft drift-risk: AP-5 under "minimum-delta instinct" — guard = D-test Hook 2 Day 1 (V1 §20).

---

### V2 Aggressive-Maximalist

**Self-score:** 76.2/100 | **My weighted score:** 75.8/100 | **Status:** ELIGIBLE (with C14-reading flag, Part 4 Q2)

**Thesis (1 sentence).** Schema-heavy / runtime-light: every Phase-2/3 capability gets a designed home in Phase-1 (directory, schema, role-manifest, spec) but only the 11 canonical agents burn compute — *capabilities not scaffolded in the founding architecture accumulate as retrofitting debt that compounds exponentially at each revenue gate* (V2 §1).

**Top 3 strengths.**
1. **Scale trajectory 9.** Schema-heavy means scale = activation, not rewrite. §6 per-subsystem scale-path + sharding-keys + LOC-refactor budget concrete (V2 §6.1, §6.4). Lock-19 cited 15 times (V2 critic notes stress-test 4) — variance well-defended.
2. **Foundation quality 9.** All 8 §4 Foundation elements at full fidelity Day 1 (V2 §18). Wiki 9 entity types + atoms registry + 8 Alphas + typed edges Day 1 (V2 §7).
3. **Innovation 7.** USB-C Phase-1 protocol scaffold + role-manifest layer as C14-compliant scale vector + escalation-trace audit loop (V2 §17, §4.6, §15.6).

**Top 3 weaknesses/risks.**
1. **Phase-1 readiness 6.** Foundation investment Day 1 ≈ 8 Ruslan-weeks (V2 §18.9). Surface area genuinely large; scaffold-rot risk if revenue is slow >12 months (V2 §23 R3, ~45% probability).
2. **Operational simplicity 5.** Cognitive-load risk 65% probability (V2 §23 R4). Mitigations (top-level README, `jetix tree` CLI, `wiki/foundations/what-runs-phase-1.md`) are good but don't eliminate.
3. **C14 reading risk** — *if Stage 7 reads C14 as forbidding any named role-manifest beyond 11* (including `executor: ruslan` or `executor: null`), Maximalist pattern is invalid and variant disqualified (V2 §22 Flag 1). High decision-leverage on Stage 7 ratification.

**Phase-1 cost estimate:** €320-520/mo steady-state, P99 €650/mo (V2 §9.3). €800 ceiling defended via compute-ledger hard-block (V2 §9.4).

**Phase-3 scalability:** 9/10 — Phase-3 role-manifests, federation namespace, token state machine, USB-C taxonomy + verification harness all scaffolded Day 1; activation = publication, not invention (V2 §1).

**Critical assumptions** (if false → variant breaks).
- *Stage 7 ratifies C14 reading as runtime-only constraint* (V2 §22 Flag 1) — if not, full pattern collapses.
- *Revenue grows fast enough that scaffold-rot doesn't dominate* (~6-12 months to €50K assumed in V2 §24).
- *Ruslan's cognitive load is bearable Phase 1* — high-probability risk (V2 §23 R4).

**Non-negotiable elements** (must survive in any hybrid).
- **Multi-provider Day 1 at compute-contract layer** (V2 §5, §9, §18.7) — AP-11 by construction; Conservative explicitly endorses keeping this in hybrid composition (V1 §22 / V2-critic §"Delta vs Conservative").
- **Wiki full 9 entity types + atoms + F-G-R + 8 Alphas + typed edges Day 1** (V2 §7) — retrofitting entity taxonomy across 10⁴ claims is the Lock-19 disaster.
- **USB-C protocol layer complete spec Day 1** (V2 §17) — V3 Deep-Tech also has this; composable to any other variant.
- **Dashboard v1 + v2 + v3 schema scaffolded Day 1** (V2 §14) — schema roy-level-compatible without migration.

**Red flags** (what lowered my score).
- Self-9 on Locks lowered to 8 — C14 reading flag (V2 §22 Flag 1) creates real DQ risk pending ratification.
- Self-8 on Innovation lowered to 7 — most "innovations" are scale/disciplined application of known patterns; schema-heavy/runtime-light pattern *itself* is the novel claim, but several listed primitives (multi-provider, F-G-R, dashboard) are brief-mandated baselines.

**Locks compatibility.** ✅ All 24 cited (§19); 15 Lock-19 cites. ⚠️ Tension with **C14** (§22 Flag 1) — author's reading consistent with D4 §4.1 but Stage-7 ratification required. ✅ €800/mo gate defended at instrumentation level (V2 §9.3-9.4).

---

### V3 Aggressive Deep-Tech

**Self-score:** ~80/100 (range 78.5-82.5) | **My weighted score:** 78.0/100 (default) / **80.3/100 (Lock-19 alt-weighted)** | **Status:** ELIGIBLE

**Thesis (1 sentence).** FPF as **generative substrate, not name-dropped canon**: every folder, agent contract, wiki edge, protocol message derives from an FPF primitive at line-level traceability, with `jetix-os/` schema-isomorphic to FPF and `jetix-company/` as the first instance — *correctness through formalism — FPF is the substrate, Jetix is the instance* (V3 §1, §2).

**Top 3 strengths.**
1. **Foundation quality 10.** Only variant with §18.9 10 Foundation Quality Invariants CI-enforceable Day 1. Every C1-C21 has a CI check, not a vague "we comply" (V3 §19, §18.9). Strongest Foundation evidence in 5-variant set.
2. **Universality 9.** Parametric ontology over fixed FPF primitives ⇒ 50th roy = same primitives = $1T-scale = same primitives. Scale invariants (V3 §6.1) make "no rewrite, ever" a derivation, not a promise.
3. **Innovation 9.** Four novel primitives all defended in §17, §7, §4, §10: USB-C Phase-1 scaffold (2 reference protocols + verification harness), typed-graph wiki (9 entities × 10 typed edges), fpf-manifest per agent (machine-verifiable), orthogonality invariant on token economy.

**Top 3 weaknesses/risks.**
1. **Phase-1 readiness 5.** Honest. 2-3 week formalism-onramp before consulting pipeline ships at full velocity (V3 §21.1 axis 1). USB-C Phase-1 scaffold adds ~40h architect time.
2. **Operational simplicity 5.** Learning cliff is real. New pilot reading 7 hooks + 18 manifests + 4 kit-install + 6 protocols needs 5-7 days vs 1-2 for V1 (V3 §21.1 ax6). Mitigation = self-documenting fpf-manifests.
3. **AP-12 risk explicitly self-flagged HIGH** (V3 §20 + §20.1). Deep-Tech's natural gravity is toward FPF internals — could spend Phase-1 attention on civilizational research instead of consulting close. Mitigations binding (15% Ruslan-hours cap; formalism subordinate to revenue) but discipline cost is real.

**Phase-1 cost estimate:** ≤€500/mo (V3 §9.5). Formalism = filesystem + schema validation + 7 hooks; zero runtime cost beyond GitHub free tier.

**Phase-3 scalability:** 9/10 — at $1T, formal verification on token state machine + matchmaker contract kernel = tooling-migration >30% (V3 §21.1 ax2); otherwise scale = instance addition over fixed primitives.

**Critical assumptions** (if false → variant breaks).
- *15% Ruslan-hours cap on `[formalism]` actually holds* (V3 §20.1 mitigation). Toggl-tagged enforcement; >15% × 2 weeks triggers strategic escalation.
- *Q2 €15K consulting close is achievable WITH 2-3wk formalism onramp* (V3 §23.1 R1, 25% probability of miss).
- *Self-documenting fpf-manifests work as advertised for 2nd pilot* (V3 §23.2 residual). If not, hybrid pivot per §22.3.

**Non-negotiable elements** (must survive in any hybrid).
- **§17 USB-C Phase-1 scaffold (2 reference protocols + verification harness)** (V3 §17) — author's own §24.3 marks this as cheapest strategic win (~40h, €0 runtime). Composable into V4-style hybrid.
- **§4 fpf-manifest per agent** (V3 §4.2) — JSON-Schema validator in CI, machine-verifiable `acting_as` enforcement; ~90 min Day-1 / 18 agents.
- **§7 typed-graph wiki (9 entity × 10 edge types)** (V3 §7) — moderate cost (2-3d retro-tagging); enables A.14 mereology queries.
- **§18.9 10 Foundation Quality Invariants** (V3 §18.9) — these are the machine-checkable version of *«главный актив»*; should land in selected variant regardless.

**Red flags** (what lowered my score).
- Self ~80 (range 78.5-82.5); my 78.0 sits within range — no significant flag.
- AP-12 self-flagged HIGH risk + Ruslan default preference §9 ("Foundation > feature count" supports V3, but "Phase-1 readiness" preference works against) — V3 itself explicitly addresses this collision (§22.3) and proposes hybrid candidate.

**Locks compatibility.** ✅ All 24 cited w/ FPF primitive + CI check (§19). ⚠️ **Lock 14** residual AP-12 risk (V3 §21.1 ax4, 1pt deducted). ⚠️ **Contrarian #1** (§22.1) advances USB-C Phase-1 scaffold vs D4 Q15 — Phase-1 = internal RFC, not standards submission; Stage-7 ratification recommended.

---

### V4 Hybrid (Phase-Keyed Complexity)

**Self-score:** 77/100 (banked from 80.4) | **My weighted score:** 78.9/100 | **Status:** ELIGIBLE (with AP-11 reading flag, Part 4 Q4)

**Thesis (1 sentence).** Phase-progression IS the architecture: every non-Foundation capability carries an explicit `activation_trigger` field pinned to a Lock-15 revenue gate ($20-30K / €50K / €200K / €1M / €1M+) or a B.2 MHT transition (MHT-1/2/3/4) — *right depth at right phase — simplicity Phase 1, richness Phase 2+, maximalism Phase 3+* (V4 §1).

**Top 3 strengths.**
1. **Most balanced profile** — no axis < 6 in cross-audit. **Stable rank 2nd under both weighting schemes** (78.9 default; 78.6 alt-weighted). Hybrid is the variant that doesn't lose under reweighting.
2. **Locks compliance 9** — Lock-15 baked into architecture as `activation_trigger` first-class field (V4 §1, §6.2, App A — Lock 15 cited 6 sections). Revenue-gating IS the design.
3. **Scale trajectory 8 (close to V2/V3's 9).** Forward-compat schemas + MHT reification ⇒ 0 schema breaks across 4 MHT transitions; ≤30% LOC refactor constructively guaranteed (V4 §6, §7.2-7.3).

**Top 3 weaknesses/risks.**
1. **No single axis at 9-10 (cross-audit).** Risk 23.3 self-acknowledged: "*lacks distinctive strength on any single axis*" — perceptible as "safe but unremarkable" in head-to-head Stage-7 against a strong peer.
2. **Phase-2b rewrite cost at MHT-2 underestimated** (V4 §23.4) — token-B + matchmaker activations heaviest; scope creep could break 30% target. Mitigation = MHT-2 scope-freeze first 3 months.
3. **MHT-1 trigger discipline** (V4 §23.2) — if revenue stalls 6+ months, capabilities queue up; activation becomes a scramble or out-of-gate violation. Discipline is cultural, architecture only enforces hard gates on spend.

**Phase-1 cost estimate:** €300-800/mo envelope (V4 §9.4); single-provider runtime + multi-provider spec — *requires Stage 7 ratification on AP-11 reading* (V4 §22 Flag 3).

**Phase-3 scalability:** 8/10 — phase-progression constructive guarantee; MHT-4 federation = 4-conjunct trigger w/ regulatory-compliance review (V4 §22 Flag 4 + §23.5).

**Critical assumptions** (if false → variant breaks).
- *Stage 7 accepts AP-11 reading: single-provider runtime + multi-provider spec = AP-11 compliant* (V4 §22 Flag 3).
- *MHT-1 fires within 12 months* — if revenue plateaus, capabilities queue up (V4 §23.2).
- *MHT-2 scope-freeze discipline holds* (V4 §23.4) — without it, token-B + matchmaker exceed 30% LOC target.

**Non-negotiable elements** (must survive in any hybrid).
- **`activation_trigger` first-class design field** (V4 §1, §6.2) — should be the schema convention regardless of which base variant wins; it's a discipline that any variant benefits from.
- **MHT-1/2/3/4 as named architectural events with `decisions/mht-{N}-{date}.md`** (V4 §3.4-3.7, §18.4) — formalizes B.2 supervisor-subholon feedback loop.
- **Forward-compatible wiki frontmatter Day 1** (V4 §7.2) — token-B / roy-kit / USB-C fields present empty Day 1 ⇒ 0 schema breaks at MHT.
- **`finance/revenue-gates.yaml` state-machine blocking above-tier spend Day 1** (V4 §19 C2).

**Red flags** (what lowered my score below — actually self-score was lower).
- My cross-audit lifts V4 from self-77 to 78.9 — author conservatism on Innovation (self 6 → my 6) and OpSimp (self 6 → my 6) is internally consistent but cross-axis interaction (Locks 9 + Scale 8 + Phase-1 8) compounds favourably under §8.2 weights.
- Honest deduction on Scale (9 → 8): MHT-2 token-B + matchmaker risk per §23.4 is real.

**Locks compatibility.** ✅ All 24 (App A); Lock-15 cited 6× = revenue-gate backbone. ✅ §19 — every C1-C21 invariant-level Day 1; runtime activation phase-keys but invariant (schema, ACL, hooks) Day 1. ⚠️ **Flag 3** — AP-11 reading on single-provider runtime needs Stage-7 ratification.

---

### V5 Emergent (Trellis-Not-Cage)

**Self-score:** 73.2/100 (range 73-78) | **My weighted score:** 70.2/100 | **Status:** ELIGIBLE (with C14/C17 argumentation flag, Part 4 Q5)

**Thesis (1 sentence).** Design the *space of possibilities*, not the result: hard `core/` trellis (FPF contracts, membrane, escalation, hub-and-spoke, revenue-gates) + `emergence-surface/` (claims, capability-bids, routing-traces, protocol-candidates, co-citation-graph) where patterns crystallize before promotion — *trellis, not cage* (V5 §1, §2).

**Top 3 strengths.**
1. **Operational simplicity 8 (close to V1's 9).** Less prescribed structure ⇒ less to maintain. 4 blocking hooks vs 7 in V3. 18 manifests + simple bidding-protocol (V5 §3.3, §4.2).
2. **Innovation 8.** Self-organizing paradigm for solo-operator is genuinely novel: capability-capsule + bidding-protocol + decentralized-write/centralized-consolidation wiki + emergence-triad discipline (V5 §4, §7, §11).
3. **Universality 8.** `emergence-surface/` is the cleanest overlay pattern — base-layer Jetix-term-free per Hook 5; kit-replication is harvested overlay (V5 §3.2, §12).

**Top 3 weaknesses/risks.**
1. **Phase-1 readiness 6 (cross-audit; self 7).** Week-1-4 visible-progress deficit explicitly flagged (V5 §1, §23 R3 — 60% probability). Foundation-only investment looks like "nothing happened" to external observers.
2. **Convergence failure risk 30%** (V5 §23 R1) — if patterns don't stabilize after week 6 (promotion-rate <1/wk), meta-agent escalates and Ruslan must tighten threshold or add structure-param.
3. **Locks compliance 7** — C14 (capsule bidding could become de-facto 12th agent) + C17 (membrane could soften) require explicit argumentation, present (V5 §4.4, §8.4) but reader strict on compliance may push back. **Largest cross-audit deduction** in the 5-variant set.

**Phase-1 cost estimate:** ≤€500/mo (V5 §9.4); Haiku-default + Sonnet-on-demand keeps under €800 with margin.

**Phase-3 scalability:** 7/10 — SI invariants (V5 §6.2) + structural-parameters-tighten thesis; less mechanically guaranteed than V3/V4, depends on promotion pipeline.

**Critical assumptions** (if false → variant breaks).
- *Promotion pipeline crystallizes patterns within 6 weeks* (V5 §23 R1). If not, Ruslan must intervene; if persistent 60d, hybrid pivot.
- *Capability-capsule bidding does not drift to de-facto 12th agent* (V5 §23 R2 — DISQUALIFIER if materialised). Mitigation = hard bid-gate at step-3 + monthly audit.
- *Ruslan tolerates "sparse weeks 1-4"* externally (investors / partners may read "emergent" = "ad hoc" — V5 §23 R7).

**Non-negotiable elements** (must survive in any hybrid).
- **§4 capability-capsule + §11 bidding-protocol** (V5 §4.2-4.5, §11.1-11.5) — V5 §24 names this composable to any other variant; adds rich task-routing to Conservative or Hybrid base.
- **§14 emergent signal set (7 viewpoints E-1..E-7)** (V5 §14.1) — these ARE the trellis dashboard; useful as additive instrumentation to any variant.
- **§17 USB-C harvesting pipeline** (V5 §17.2) — alternative to V3 Deep-Tech "drafted Day 1" approach; "harvested, not speculated".
- **§22.3 capability-capsule as overlay (not roster expansion)** — D6 §2.2 11 agents preserved; capsules add metadata.

**Red flags** (what lowered my score).
- Self 7 Phase-1 readiness adjusted to 6 — week-1-4 visible-progress deficit is more material than self-acknowledged (V5 §1 itself names this as "острейший риск").
- Self 9 OpSimp adjusted to 8 — trellis-spec is novel and onboarding requires reading; promised simplicity has familiarity overhead.
- Self 73 (range 73-78); my 70.2 sits just below the floor — attributable above-mentioned axis adjustments.

**Locks compatibility.** ✅ All 24 (App B), each ≥2 sections. ⚠️ **C14 + C17 require explicit argumentation** (V5 §4.4, §8.4) — present + signal-instrumented (E-4, E-7), but reader-strict on compliance may push back. ⚠️ **Contrarian #3** — capsule overlay-adds to canonical 11 ("extension not change"); Stage-7 ratification recommended.

---

## Part 3 — Cross-Variant Analysis

### 3.1 Orthogonal pairs vs near-duplicates

- **Orthogonal pair 1 (Phase-1 ↔ Scale):** V1 (P1=9, Sc=6) ↔ V2/V3 (P1=5-6, Sc=9). V4 = literal interpolation.
- **Orthogonal pair 2 (Foundation ↔ OpSimp):** V3 (F=10, OS=5) ↔ V5 (F=7, OS=8). V3 buys depth with cliff; V5 buys simplicity with sparseness.
- **Near-duplicates:** V2 + V3 share 5 axis values (Scale=9, Foundation=9-10, Innov=7-9, Univ=8-9, P1=5-6). Differentiator: V3 = formal substrate (FPF derivation, CI invariants); V2 = scaffolded surface (designed-dormant manifests). Stage 7 picks one as anchor + harvests from other.
- **Genuinely distinctive:** V4 (`activation_trigger` field) and V5 (capsule + bidding) are not substitutable for any peer.

### 3.2 Hybrid composability

| Base | Composable add-ons | Mutually exclusive with |
|---|---|---|
| **V1** | +V3 §17 USB-C scaffold (V3 §24.3) +V3 §4 fpf-manifests +V5 §4 capsule +V5 §14 signal set | V2 full role-manifest layer; V3 full §7 typed-graph wiki |
| **V2** | +V3 §18.9 Foundation Quality Invariants +V4 `activation_trigger` field (formalizes dormant-folder discipline) | V5 emergence-surface (philosophical conflict) |
| **V3** | +V4 `activation_trigger` +V5 §14 signal set | V1 minimum-delta (philosophical conflict) |
| **V4** | +V3 §17/§4/§18.9 +V5 §4/§14 | None — by design |
| **V5** | +V3 §17 USB-C harvesting +V4 `activation_trigger` | V2 designed-dormant scaffolding |

**Key observation.** **V4 + V3 §17/§4/§18.9 + V5 §4/§14** = a "5-variant maximalist composition" pulling best Phase-1-affordable elements from 4 variants without §6 violation. Estimated 81-83 weighted (Part 4 Q7). Strongest hybrid candidate if no single variant dominates Stage 7 selection.

### 3.3 Lock-driven filter — most polarizing locks

1. **Lock 19 ($1T no-rewrite)** is THE polarizing lock. V2/V3 = Day-1 binding (scaffold / derive); V1 = Phase-2b refactor-budget (defer with quantified cost); V4 = `activation_trigger` discipline (defer with constructive guarantee); V5 = structural-parameters-tighten (defer to promotion pipeline). **Lock 19 weighting → ranking** (Part 1 §1.2: V1 default → V3 alt-weighted).
2. **Lock 23 (Token Option B):** V3 formal orthogonality invariant (§10.2) > V2 full state-machine + 5-event audit Day 1 (§10) > V4 forward-compat field-absence (§10.4) > V1 spec-only + Hook 6 regex-reject (§10.5) ≈ V5 carves OUT of emergence (§10.1). Decision: spec-only (V1, V5) or runtime-ready dormant scaffold (V2, V3, V4)?
3. **Lock 20 (USB-C):** V2/V3 = Phase-1 scaffold (2 protocols + harness); V4 = schema stubs only; V1 = spec-doc; V5 = harvesting pipeline (no Phase-1 protocols). Decision: is Phase-1 USB-C signal competitive-strategic or unnecessary?

### 3.4 €50K Q2 feasibility ranking

Top-3 by Phase-1 shipability (axis 1 + axis 6 weighted):
1. **V1** — minimum-delta, ships Day 1. P(€50K Q2) highest.
2. **V4** — ~10% authoring tax; phase-keyed runtime keeps surface small. High.
3. **V5** — runs Day 1 but visible-progress sparse weeks 1-4; consulting pipeline active in `jetix-company/sales/` (V5 §3.1). Moderate-high.

V2/V3 trade Phase-1 velocity for Phase-3 readiness — explicit in their thesis sentences.

### 3.5 Swarm-pattern readiness — capsule + bidding as overlay layer

If Ruslan wants V5's bidding WITHOUT V5's full philosophy:

- **V4 = BEST overlay host.** Forward-compat schemas accept capsule fields; `activation_trigger` aligns with capsule activation cadence. ~40h + zero schema break.
- **V1 = GOOD.** V5 §24 explicitly composable. ~60h (fewer schema hooks).
- **V3 = NEUTRAL.** fpf-manifests already do machine-verifiable role-decl; capsule extends. ~80h.
- **V2 = HOSTILE.** Maximalist pre-declares specialization at design-time; emergent specialization conflicts.
- **V5 = native.**

**Recommendation:** swarm-pattern need → V4 + V5 §4/§11/§14 overlay (lowest friction); V3 + V5 §4 if Foundation depth paramount.

---

## Part 4 — Flagged Questions for Ruslan (Stage 7 decisions)

Each: context (1 sentence) + tradeoff + what it opens/closes.

### Q1. Default §8.2 weights or Lock-19 emphasis governs selection?

**Context.** Default → V1 wins (80.0); Lock-19 emphasis (Scale 20% / Foundation 18% / Phase-1 15% / Locks 15%) → V3 wins (80.3). V4 stable 2nd under both (78.9 / 78.6).
**Tradeoff.** Default honors §9 stated preference ("Phase-1 + Foundation > Innovation"); alt honors *«Quality cannot be retrofit at $1T scale»* (D2 §14).
**Opens/closes.** Determines nominal winner. V4 acceptable under either ⇒ weighting non-binding if Hybrid acceptable.

### Q2. C14 reading — runtime-only or runtime+spec count?

**Context.** V2 Maximalist depends on reading C14 as runtime-only (11 mailbox agents) while permitting role-manifest layer = 23 designed roles. Author argues consistent with D4 §4.1 (5 Ruslan sub-roles + 2 stubs explicitly allowed). V2 §22 Flag 1.
**Tradeoff.** Strict reading (runtime+spec count) → V2 DQ; V3 (18 manifests), V4 (18), V5 (18) also affected. Permissive → all valid.
**Opens/closes.** Strict reading kills V2 standalone (still composable); permissive legitimizes schema-heavy/runtime-light across hybrids.

### Q3. AP-12 tolerance — V3 Deep-Tech ~2-3wk formalism onramp + 15% Ruslan-hours cap acceptable?

**Context.** V3 §20.1 self-flags AP-12 HIGH; mitigations binding (15% cap, formalism subordinate to revenue). Risk = 25% Q2 €15K close slips 60d (V3 §23 R1).
**Tradeoff.** Investment buys Foundation 10 / Universality 9 / Innovation 9 / defensible Lock-19 derivation.
**Opens/closes.** Yes → V3 standalone viable. No → V3 §17/§4/§18.9 components composable to V4 (V3 §24.3).

### Q4. AP-11 reading — single-provider runtime + multi-provider spec satisfies AP-11?

**Context.** V4 §22 Flag 3 — Hybrid runs single-provider runtime Phase 1 (multi-provider spec only) to stay in €800 budget. V2/V3 ship multi-provider runtime Day 1.
**Tradeoff.** Spec-enough → V4 +€100-200/mo headroom. Runtime-required → V4 +€100-150/mo or DQ.
**Opens/closes.** Strict reading raises V4 Phase-1 cost; lenient reading lowers V2/V3 cost-efficiency advantage.

### Q5. V5 Emergent C14/C17 argumentation — accept "capsule extends, never replaces" + "membrane non-emergent"?

**Context.** V5 §4.4 + §8.4 argue C14/C17 preserved by overlay-pattern. Author acknowledges argumentation needed (V5 §21.1 ax4).
**Tradeoff.** Accept → V5 standalone viable. Reject → V5 reduced to overlay component for V4 (V5 §24 hybrid candidacy).
**Opens/closes.** Determines whether V5 stays as 5-variant alternative or becomes V4-overlay.

### Q6. USB-C Phase-1 scaffold — competitive-strategic signal worth ~40h Day 1?

**Context.** D4 Q15 schedules Phase-3+ for standards-body submission. V2/V3 ship Phase-1 scaffold (2 reference protocols + verification harness, ~40h, €0 runtime). V1 spec-doc only; V4 schema stubs; V5 harvesting pipeline (no Phase-1 protocols).
**Tradeoff.** Phase-1 scaffold = Phase-2a enterprise-credibility signal vs ~40h Phase-1 maintenance cost; competitive exposure 25% per V1 §23.2.
**Opens/closes.** Want → V3 / V2 / V4+V3§17 overlay. Don't want → V1 / V4 / V5 viable.

### Q7. Pure variant or hybrid composition?

**Context.** D4 §9 Step D allows hybrid. Part 3 §3.2 maps "V4 + V3 §17/§4/§18.9 + V5 §4/§14" as defensible composition pulling best Phase-1-affordable elements from 4 variants.
**Tradeoff.** Pure → cleaner narrative, faster Stage-8 start. Hybrid → estimated 81-83 weighted, requires DRR per composed element + §9D constraint recheck.
**Opens/closes.** Determines Stage-8 integration scope.

### Q8. V2 cognitive-load tolerance — 65% probability of Phase-1 overload acceptable?

**Context.** V2 §23 R4 self-flags 65% prob; mitigations (`_status.md`, `jetix tree` CLI, README, `what-runs-phase-1.md`).
**Tradeoff.** Tolerable → V2 standalone (Phase-2a transition smoother). Intolerable → V2 hybridized, dormant-surface −30% (V2-critic delta-vs-Conservative).
**Opens/closes.** Determines V2 standalone vs. component-only contribution.

### Q9. Scaffold-rot tolerance — V2 (45% over 2-3y slow-revenue) + V3 (25% €50K slip) both assume <12mo to €50K. Confident?

**Context.** V2 §23 R3 + V3 §23 R1 both depend on revenue arriving fast enough to validate scaffolding.
**Tradeoff.** Confident <12mo → V2/V3 risks acceptable. Uncertain >12mo → V1 (minimum-delta) or V4 (phase-keyed budget protection) preferred.
**Opens/closes.** Cash-runway certainty determines variant tier viability.

### Q10. Cloud Cowork narrative-signal weight — which Stage-7 story matters externally?

**Context.** V1 = "discipline"; V2 = "build for $1T from Day 1"; V3 = "standards-readiness / FOAF-grade"; V4 = "phase-progression elegance"; V5 = "self-organization for solo-operator". Different signals to investors / partners / smart-audience (D12).
**Tradeoff.** V3 most defensible to FOAF / standards-body reviewer (V3 §24.4); V1 most defensible to operational-discipline auditor.
**Opens/closes.** Loops back to Q1 weighting — Cloud Cowork voice may adjust §8.2 weights or shift hybrid composition.

---

## Provenance & Self-Review

**Inputs (Pass 1).** D4 (842 ln) + V1-V5 (1499-1809 ln) + _CRITIC-NOTES (143) + D4 §2 lock summary; TENSIONS-* spot-read for contrarian-claim validation.

**Self-review checklist.**
- ✅ Part 0 disqualifier executed first; no DQ; 3 soft flags → Part 4 Q2/Q4/Q5.
- ✅ Only D4 §8.1 axes used (10); no invented axes.
- ✅ No new Locks / anti-patterns / principles introduced.
- ✅ No selection made; Part 4 surfaces decisions only.
- ✅ Cross-audit honest: V5 −3.0 largest Δ, attributable to Phase-1 7→6 per author's own §1 + §23 R3.
- ✅ Honest weakness floors: V3 axis-1 = 5; V2/V5 axis-1 = 6; V2/V3 axis-6 = 5.

**Caveats.** Single cross-auditor (server-cc). Citation discipline spot-checked ~10/variant; no fabrication but full audit not performed. "Best" column = per-axis only.

---

*END STAGE-7 CROSS-AUDIT — Ready for Ruslan + Cloud Cowork Stage-7 selection meeting.*
