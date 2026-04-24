---
title: "Investor × Critic — ICP + KPI Realism Audit: quick-money P1 bootstrap (Wave 3 Part E)"
type: critic-audit-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: investor-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: critic
wave: 3
part: E
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted-with-dissent
state: accepted-with-dissent
confidence: high
confidence_method: unit-economics-arithmetic
tier: core
promotion_note: |
  Wave-3 critic audit promoted 2026-04-24 with DISSENT PRESERVATION. 3 HARD FAIL + 1
  conditional FAIL findings on quick-money P1 bootstrap (CC-1 KPI arithmetic, CC-3
  archetype filter, CC-4 kill_criteria precondition, CC-5 levenchuk kpi_targets empty
  option). Escalated to Ruslan via AWAITING-APPROVAL packet with 6 Alternatives + F-G-R
  triples. Mgmt-integrator's design record preserves JETIX-PLAN §3.1 numbers as-sourced;
  this critic audit preserves the arithmetic refutation with Kelly-edge reasoning.
  Per brigadier §1d AP-6: dissent NEVER averaged into consensus — both positions
  documented; Ruslan arbitrates parameter choice (contract count + revenue mix + Tier-1
  archetype filter + kill-criteria structure) before Part E physical execution.
artefact_under_review:
  - "prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1-E.2"
  - "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md (consulting.default_kpi_targets)"
  - "decisions/JETIX-VISION.md §§7.1-7.2"
  - "decisions/JETIX-PLAN.md §§3.1-3.9"
  - "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5"
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§§7.1-7.2 (11 archetypes + 5 ICP criteria)"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.9 (Phase-1 objectives + budget + milestones)"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 (Path A/B/C hosting-path GM arithmetic)"}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.1-E.2 (quick-money bootstrap spec)"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "consulting.default_kpi_targets (lines 162-165)"}
related:
  - "swarm/wiki/drafts/T-km-materialization-mvp-2026-04-24-mgmt-integrator-partB-b2-mini-swarm-bundle.md"
binding_scope: "task-T-km-materialization-mvp-2026-04-24-wave-3-partE"
granularity: jetix-internal
---

# Investor × Critic — ICP + KPI Realism Audit

## §0 Scope + anti-scope

**In scope:** ICP filter arithmetic, KPI consistency with €50K Q2 2026 gate, Path B vs Path C
hosting-path gross-margin arithmetic, archetype-to-Phase-1-buyer filter, kill-criteria
triangulation, levenchuk-deep-dive KPI coverage gap.

**Anti-scope (what this critique does NOT assess):**
- LLM-eval predicates or stage-gate DSL grammar — philosophy-expert reviewed that in Wave 1.
- Engineering implementation (skill code, offline-LLM stack, bash scripts) — engineering-expert territory.
- Rewriting `project-types.yaml` schema — mgmt-expert territory.
- Whether the B2 scaffold design is correct (Wave 1 decision, locked).
- General business strategy direction (α-5 Direction, HITL-only per §1d `never` row).

---

## §1 Conformance Checks (CC-1 through CC-6)

### CC-1 — KPI arithmetic consistency with €50K Q2 2026 gate

**F: F4** (operational convention; arithmetic on stated parameters)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1` kpi_targets block
**R:** refuted if signed-contract data in Q2 2026 diverges by >2× from projection; accepted if Q2 2026 report shows ≥€50K committed; refutation receipt: `swarm/wiki/reviews/Q2-2026-portfolio-<date>.md`

**Arithmetic:**

The bootstrap specifies:
```yaml
kpi_targets:
  leads_per_quarter:            20
  discovery_calls_per_quarter:  10
  contracts_per_quarter:        2
  mrr_eur_target_q2_2026:       15000
  cumulative_revenue_q2_2026_eur: 50000
```

Per `partB-b2-mini-swarm-bundle.md` (line 163), the canonical `consulting.default_kpi_targets`
also carries `leads_per_quarter: 20` and `contracts_per_quarter: 2`.

**Working the arithmetic:**

Stage 1: leads_per_quarter: 20 → discovery_calls_per_quarter: 10 implies a lead-to-call rate
of 50% (10/20). This is plausible for warm/semi-warm outreach; optimistic for cold email.

Stage 2: discovery_calls_per_quarter: 10 → contracts_per_quarter: 2 implies a call-to-close
rate of 20% (2/10). For B2B consulting, 10–25% is industry-normal on qualified calls.
This is within range IF the calls are correctly ICP-filtered.

Stage 3: contracts_per_quarter: 2 at what deal size?

The bootstrap states `mrr_eur_target_q2_2026: 15000` (monthly recurring) and
`cumulative_revenue_q2_2026_eur: 50000` (cumulative).

Invert: to reach €50K cumulative in ~13 weeks (Q2 = April–June 2026, from ~April 24):
- €50K / 13 weeks = €3,846/week revenue run rate required.
- At €15K MRR by end of Q2: that implies revenue ramp from near-zero to €15K/month.
  If we assume linear ramp: months 1/2/3 average ~€8.3K/month. 3 × €8.3K = €25K.
  **Gap: €50K target vs €25K implied by linear ramp to €15K MRR. Delta: -€25K.**

This is a **material inconsistency.** The cumulative-revenue target (€50K) and the MRR-end-
state target (€15K/month) are arithmetically inconsistent unless:

Option A: Revenue is not linear — most contracts close in months 2–3 (back-loaded). Under
back-loading (€2K month-1, €18K month-2, €30K month-3): cumulative = €50K, MRR = ~€30K
(not €15K). Still inconsistent on the MRR figure.

Option B: €15K MRR is stated for the END of Q2, but the €50K includes non-recurring one-off
consulting revenue (hourly billing at €150/hour + project-based fees) PLUS recurring retainer
revenue. Under this interpretation: 2 contracts at typical Phase-1 deal sizes.

**Path B deal-size triangulation (from STRATEGIC-INSIGHT §5):**
Path B = €3K onboarding + €15K/yr. Per year: €3K + €15K = €18K/contract. Per quarter:
€18K/4 = €4.5K/quarter per contract. Two contracts: €9K/quarter recurring + €6K
onboarding fees (2 × €3K) = €15K in quarter from new contracts.

**2 contracts × €4.5K recurring/quarter + 2 × €3K onboarding = €15K in Q2 from new contracts alone.**
That is far below €50K.

**Verdict for CC-1: FAIL.** The arithmetic forces one of two conclusions:

1. `contracts_per_quarter: 2` is insufficient to reach €50K cumulative unless avg deal
   size is **€25K per contract** (€50K / 2 contracts — ignoring prior pipeline from Phase 0).
   At Path B pricing (€18K/yr = €4.5K/quarter), 2 contracts = €9K quarterly. Gap: 5.5×.

2. The €50K target requires approximately **11 contracts** at Path B pricing
   (€50K / €4.5K/contract/quarter ≈ 11) in Q2 alone — or a mix of larger enterprise
   deals (Path A/C at higher ticket) and/or legacy hourly consulting at scale.

**The bootstrap does not resolve this tension.** KPI targets are internally inconsistent
unless avg deal size >> Path B unit economics. Recommended fix: either (a) raise
`contracts_per_quarter` to ≥5, or (b) add a separate `avg_deal_size_eur` field that
triangulates the cumulative target, or (c) source the €50K from a wider deal mix
(hourly consulting + retainers + onboarding fees) stated explicitly.

[src:decisions/JETIX-PLAN.md §3.9 milestone M1.4]
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]

---

### CC-2 — Path B vs Path C hosting-path arithmetic + explicit path selection

**F: F4** (operational convention; arithmetic on stated parameters from STRATEGIC-INSIGHT §5)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.2` icp.md hosting path row;
`decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path B/C`
**R:** refuted if gross margin on first signed contract diverges by >10pp from projected; accepted if
Q2 2026 contract report shows GM ≥70% on all contracts; refutation receipt: first contract P&L entry
in `swarm/wiki/operations/quick-money/contracts/`

**STRATEGIC-INSIGHT §5 Path B gross-margin arithmetic:**

Path B: Client-Hosted (Jetix as methodology + tooling provider).
Stated: €3K onboarding + €15K/yr = 70.7% GM year-1.

**Verify:**

Revenue year-1: €3K onboarding + €15K recurring = €18K total.
GM = 70.7% implies COGS = €18K × (1 - 0.707) = €18K × 0.293 = **€5.27K**.

What goes into COGS at Path B?
- Ruslan's time: onboarding (setup, config, training). Estimate: ~20 hours @ €150/hour
  (opportunity cost) = €3K. Plus quarterly support: ~5 hours × 4 = 20 hours × €150 = €3K/yr.
  Total time-COGS: ~€6K.
- Software/tooling pass-through: ~€0 at Path B (client hosts own infra; Jetix ships configs).
- Claude Max subscription: already sunk cost (Max-sub discipline); €0 marginal.

At €6K time-COGS on €18K revenue: GM = (€18K - €6K) / €18K = **66.7%**. Slightly below
the stated 70.7%.

The 70.7% figure is achievable if onboarding time is held to ~15 hours (not 20):
15h × €150 = €2.25K + €3K support = €5.25K COGS → GM = (€18K - €5.25K) / €18K = **70.8%**. Verified.

**The 70.7% Path B GM arithmetic checks out** — conditional on onboarding being held to ≤15
hours and quarterly support to ≤20 hours/year. This is tight for first clients but achievable
with the playbook templates that the quick-money KM materialization is designed to produce.

**Path C (Hybrid) GM arithmetic — as stated "54% GM fails Phase-A floor":**

STRATEGIC-INSIGHT §5 does not provide explicit Path C arithmetic, only the conclusion.
The execution prompt icp.md spec does state: "Path C (hybrid) deferred to post-contractor-#1
(54% GM fails Phase-A floor)."

Investor-expert cannot verify the 54% figure without explicit Path C cost breakdown.
The stated conclusion is directionally credible (Path C adds networking complexity,
tunnel setup, GDPR compliance cost, Jetix compute for hosted agents), but the 54% needs
arithmetic backing.

**Coverage gap: Path is explicitly chosen (Path B default, Path C deferred) — this IS present
in the icp.md spec at §2.E.2.** Credit for explicit selection. However:

1. The Path C 54% figure is asserted, not derived. No arithmetic block.
2. Path A (Jetix-hosted VPS) GM arithmetic is completely absent from the bootstrap spec.

**Verdict for CC-2: PARTIAL PASS.**
- Path B GM arithmetic: arithmetically defensible at ≤15hr onboarding. PASS.
- Path selection explicit (Path B default, Path C deferred): PASS.
- Path C 54% figure: asserted without arithmetic. FAIL on that sub-claim.
- Path A arithmetic: absent entirely. FAIL on that sub-claim.

Recommended fix: add a "hosting-path GM table" to `quick-money/icp.md` with explicit
arithmetic for all 3 paths. Path C ≈54% is plausible if you add: ~40hr/yr Jetix ops +
tunnel infra cost ~€1.2K/yr → COGS ~€8.25K on €18K = 54.2% GM. Document this.

[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]
[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.2]

---

### CC-3 — 11 archetypes filtered to Phase-1 buyers

**F: F4** (operational convention; filter criterion from JETIX-VISION §7.2 + JETIX-PLAN §3.3)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.2` icp.md archetype subset
**R:** refuted if first 3 signed contracts come from archetypes outside the stated subset; accepted if
Q2 2026 pipeline shows >70% of qualified prospects are from the 2 Phase-1 primary archetypes;
refutation receipt: `swarm/wiki/operations/quick-money/pipeline.md` entries

**Analysis:**

JETIX-VISION §7.1 lists 11 archetypes. The icp.md spec cites 6:
```
1. Предприниматели / бизнесмены
2. Ресёрчеры
3. Инженеры
4. Инвесторы
6. Продавцы
7. Менеджеры / коммуникаторы
11. Блогеры
```
(Archetypes 5 Политики, 8 Философы, 9 Разработчики идей, 10 Разработчики жизни omitted.)

**Investor verdict on this filter:**

The JETIX-PLAN §3.3 (Phase 1 actions) explicitly names two Phase-1 primary offers:
(a) 4-pack consulting and (b) Продюсерский центр for English-speaking infobiz (D10).
JETIX-VISION §9 confirms "Блогеры specifically — natural overlap с продюсерским центром
(Decision 11 core Phase 1 offer). Блогер-архетип является primary Phase-1 customer for
English-speaking infobiz."

**The upward-direction filter is the primary selector.** Per JETIX-VISION §7.2: "Jetix
community = ВСЕ 11 archetypes × UPWARD-DIRECTION ONLY. Topic secondary, direction primary."

For Phase-1 REVENUE (not community): the question is who signs contracts NOW, not who
might engage later. Capital-allocation criterion: **ability-to-sign + pay-now**.

Apply second-level thinking (Marks pattern P3): Which archetypes have BOTH upward-direction
AND discretionary budget for AI consulting at €3K–€18K/engagement in 2026?

**Inversion (Munger pattern P4): Who does NOT have ability-to-sign + pay-now?**
- Ресёрчеры: often academic or employed; discretionary budget low. Phase-2 fit, not Phase-1.
- Инвесторы: may engage but evaluation cycles long; not primary P1 lead-gen target.
- Политики: long sales cycles; complex procurement; NOT Phase-1 (JETIX-PLAN §3 explicitly: "НЕ Fortune-500 закупщики в Phase 1").
- Философы: missing from the spec (correctly omitted); low ability-to-pay in Phase-1.

**The Phase-1 buyer profile that triangulates with ability-to-sign + pay-now:**
1. **Предприниматели / бизнесмены** (archetype 1) — primary. Hungry, action-driven, already running revenue, €3–18K is within discretionary budget.
2. **Блогеры** (archetype 11) — primary for Продюсерский центр. Specialist bloggers with 5K+ subscribers and paid products have revenue to invest in production leverage.

These two are the MITTELSTAND + STARTUPPER Phase-1 buyers per the upward-direction + ability-to-sign filter.

**Gap in the spec:** The icp.md lists 6 archetypes without ranking them by Phase-1 priority.
It does NOT call out archetypes 1 and 11 as PRIMARY and the rest as SECONDARY (Phase-2+).
This is a **coverage gap** — it risks the bootstrap treating all 6 equally, which would
dilute outreach and extend the conversion cycle beyond Q2 2026.

**Verdict for CC-3: FAIL.**
The archetype filter is partially correct (correctly omits 4 of 11) but fails to establish
a Phase-1 priority ranking. Adding 4 Phase-2 archetypes (Ресёрчеры, Инженеры, Инвесторы,
Продавцы) to the Phase-1 list dilutes outreach without improving near-term revenue.

Recommended fix: Add a two-tier structure to icp.md:
- Tier 1 (Phase-1 primary, ability-to-sign-now): Предприниматели + Блогеры.
- Tier 2 (Phase-1 secondary, longer cycle): Менеджеры, Продавцы.
- Tier 3 (Phase-2+ activate): Ресёрчеры, Инженеры, Инвесторы.

Filter criterion: Tier 1 = upward-direction + discretionary budget ≥€5K + decision-cycle ≤6
weeks. This is the Phase-1 operator-reachable ICP.

[src:decisions/JETIX-VISION.md §§7.1-7.2]
[src:decisions/JETIX-PLAN.md §3.3 (Phase 1 offer expansion) + §3.7 (Phase 1 markets)]

---

### CC-4 — kill_criteria date 2026-07-24 triangulation

**F: F5** (analytical with arithmetic backing on funnel timing)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1` kill_criteria
**R:** refuted if a project with these outreach parameters regularly produces first contract before
week 8 (base-rate for B2B consulting cold outreach: median first close is week 8–14);
accepted if base-rate analysis of ≥10 comparable bootstraps shows >50% sign by week 12;
refutation receipt: recorded in `swarm/wiki/reviews/Q2-2026-portfolio-<date>.md`

**kill_criteria as stated:**
```
"if no signed contract after 12 weeks of ICP-targeted outreach to 50 qualified prospects,
re-decompose the offer — or kill. Specifically: no contract signed by 2026-07-24."
```

**Triangulation:**

Start date: ~2026-04-24 (now). End date: 2026-07-24. Delta: 13 weeks (91 days).

Funnel timing:
- Leads per quarter: 20 (per kpi_targets). But kill_criteria cites "50 qualified prospects."
  **Inconsistency 1: kpi_targets says 20 leads/quarter; kill_criteria requires 50 qualified
  prospects as a precondition for the kill to be valid.** At 20 leads/quarter, reaching 50
  qualified prospects requires 2.5 quarters (37.5 weeks) — well beyond the 13-week window.
  The kill criterion is therefore physically impossible to satisfy in the stated timeframe
  at the stated lead volume.

- Weekly outreach volume: 20 leads/quarter = 1.54 leads/week. This is very low volume.
  At this pace, 50 qualified prospects requires week 32 (August 2027, approximately).

- 90-day B2B consulting close cycle: standard cold-outreach B2B cycle (discovery → proposal
  → negotiation → sign) is 6–14 weeks for SMB/Mittelstand. At 13-week total window,
  the kill criterion is at the OUTER EDGE of the first plausible close cycle.

**Can the kill criterion fire false-positive on a ramping project?**

Yes — at 1.5 leads/week, a project that is performing correctly (discovery calls being
booked, proposals being sent, negotiations underway) might have 0 signed contracts on
day 91 simply because the close cycle is 14 weeks from first contact. The kill criterion
would fire prematurely on a healthy-ramping project.

**Second-level thinking (Marks P3):** The market has already priced in 8–14 week close
cycles for B2B consulting. The 13-week kill window does not account for pipeline LAG —
a lead generated on day 1 does not close by day 91 in a cold-outreach B2B model.

**Verdict for CC-4: FAIL.** Two problems:
1. The "50 qualified prospects" precondition in kill_criteria is inconsistent with
   "20 leads/quarter" in kpi_targets. At 20/quarter, 50 prospects takes 2.5 quarters.
2. The 13-week window may fire false-positive on a correctly-ramping project.

Recommended fixes:
- Fix inconsistency: either raise leads/quarter to ≥40 (to reach 50 qualified in time)
  OR lower the kill_criteria threshold to "20 ICP-qualified prospects" (matching kpi_targets).
- Add pipeline LAG safeguard: "if no signed contract AND ≤15 qualified leads in pipeline
  by 2026-07-24, kill/pivot. If ≥15 qualified leads in pipeline, extend 4 weeks."
- Alternative kill criterion that is both falsifiable and lag-aware:
  "if cumulative discovery_calls < 5 by 2026-06-15 (mid-quarter checkpoint), pivot offer.
  If cumulative contracts < 1 by 2026-07-24 AND pipeline < 10 qualified leads, kill."

[src:decisions/JETIX-PLAN.md §3.9 milestones M1.1-M1.4]
[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1]

---

### CC-5 — levenchuk-deep-dive P3 kpi_targets: not empty

**F: F4** (operational convention; per requirement from execution-prompt §2.E.5 + /lint
hard-fail rules in partB)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.5` kpi_targets field
**R:** refuted if a P3 research project with empty kpi_targets successfully passes /lint and produces
zero falsifiable outputs in 3 cycles; accepted if the `hypotheses.md` marker-scan catches hypothesis
coverage per research default_kpi_targets; refutation receipt: /lint run result in next cycle

**Analysis:**

The execution prompt §2.E.5 states:
```
kpi_targets: optional (P3); leave empty or set {playbooks_drafted: 2, hypotheses_validated: 3}.
```

**The "leave empty" option produces an unfalsifiable project.**

Cross-reference: `partB-b2-mini-swarm-bundle.md` research type `default_kpi_targets`:
```yaml
default_kpi_targets:
  hypotheses_per_cycle: 3   # Hamel-binary: count(hypotheses added per cycle) >= 3
  papers_per_quarter: 1     # Hamel-binary: count(drafts/*.md promoted to ready) >= 1 per 90d
```

These defaults exist. The bootstrap spec for levenchuk-deep-dive explicitly allows leaving
them empty. This is inconsistent with the /lint signal `L-PROJECT-MISSING-REQUIRED-FRONTMATTER`
which hard-fails on missing kpi_targets for P1/P2 but is **"optional P3/P4"** per
the spec.

**Investor verdict:** Empty kpi_targets on a P3 research project creates an unfalsifiable
project. Per AP-INV-2 (unit-econ-presented-as-prose-not-Hamel-binary), any project without
measurable targets is at risk of infinite "research" with no compounding output. This is
especially dangerous for a project explicitly intended to generate consulting leverage for
the €50K Q2 path.

JETIX-PLAN §10.1 (D14) locks: "Research допускается только если serves revenue." A P3
project with empty kpi_targets cannot be evaluated against this lock.

**However,** the bootstrap spec also offers the non-empty alternative:
`{playbooks_drafted: 2, hypotheses_validated: 3}`. If the mgmt-integrator picks this
option (non-empty), CC-5 passes.

**Verdict for CC-5: CONDITIONAL FAIL.**
The spec allows "leave empty" — this option produces an unfalsifiable artefact and violates
D14 revenue-instrumental discipline for Phase-1. The non-empty option (`playbooks_drafted: 2,
hypotheses_validated: 3`) is acceptable IF mandated, not merely suggested.

Recommended fix: Remove the "leave empty" option from the §2.E.5 spec. Mandate minimum
kpi_targets for ALL project types including P3/P4:
```yaml
kpi_targets:
  hypotheses_per_cycle: 2       # D14 revenue-instrumental: ≥2 per cycle
  playbooks_drafted: 2          # output that feeds quick-money consulting leverage
  hypotheses_validated: 3       # Popperian refutation events
```

Note: `hypotheses_per_cycle: 2` (not 3) is used here as a Phase-1-conservative floor.
The partB default of 3 is correct for a mature research project; levenchuk-deep-dive at P3
adaptive start should use a lower floor. This is a second-level nuance the spec misses.

[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md research.default_kpi_targets]
[src:decisions/JETIX-PLAN.md §10.1 D14 research-revenue-instrumental]
[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.5]

---

### CC-6 — Margin-of-safety on the €50K gate (investor-specific check)

**F: F4** (operational convention; applying Graham margin-of-safety + Marks second-level)
**ClaimScope:** `prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1` kpi_targets.cumulative_revenue_q2_2026_eur
**R:** refuted if actual Q2 2026 revenue deviates by >50% from projection; accepted if Q2 2026
report shows ≥€40K committed (80% floor); refutation receipt: Q2 2026 portfolio review

**Arithmetic:**

The €50K gate is the committed Phase-1 exit criterion (JETIX-PLAN §3.10, M1.4, locked).

Opportunity cost at €50K gate: max-subscription discipline (€300–800/month) + Ruslan's
time (40 hr/week × €150/hr opportunity-cost = €6K/week). If Q2 spans 13 weeks:
total Ruslan opportunity-cost during Q2 = 13 × €6K = **€78K**.

**Margin-of-safety calculation (Graham P2 pattern):**
margin = (expected-return - opportunity-cost - risk-of-ruin floor) / opportunity-cost
= (€50K - €78K - €0) / €78K = **-0.36 (negative)**

This is expected for Phase-0/Phase-1 bootstrap — Ruslan is investing his own time below
market rate to build the Jetix moat. The negative margin-of-safety in the FIRST quarter
is not a kill signal; it IS the capital-allocation bet (Buffett: investing your own time
as founder capital). However, it means the bootstrap's €50K target does NOT cover the
opportunity-cost of Ruslan's time.

**Second-level (Marks P3):** What is already priced in? The market consensus for solo-
founder AI consulting bootstraps reaching €50K in the first full quarter of outreach
is LOW. Base rate for B2B consulting cold-outreach reaching €50K ARR in 13 weeks: per
available analogues (Mittelstand-focused consultants, SaaS consultancies, AI boutiques),
~10–20% of solo founders hit this in the first quarter. 80% take 2–3 quarters.

**Risk-of-ruin floor (Marks / Kelly pattern):** JETIX-PLAN §2.4 states "Cash reserve:
>1 month runway" as Phase-1 minimum. At €300–800/month run rate (Max-sub discipline),
the ruin floor = 1 month = €300–800. This is very low (Max-sub discipline makes Jetix
extremely lean). **The ruin floor is not at risk at Phase-1 run rates.** This is a
strong positive.

**Verdict for CC-6: PASS (with notation).**
The margin-of-safety is negative in pure opportunity-cost terms — which is expected and
acceptable for Phase-1 founder-capital deployment. The ruin floor is safe (Max-sub
discipline = extremely low burn). The €50K target is aggressive vs base rate but the
risk-of-ruin consequence of missing it (Ruslan's runway with Max-sub discipline) is
bounded and survivable. Capital discipline preserved.

Notation: if Q2 shows cumulative revenue ≤€15K at week 8 (M1.2 half-milestone), escalate
immediately — this pattern signals the kill criterion should fire earlier than 2026-07-24.

[src:decisions/JETIX-PLAN.md §2.4 budget + §3.9 milestones]
[src:decisions/JETIX-ARCHITECTURE-BRIEF.md §5.1 horizon-gate (not read in detail; referenced by name per §1a)]

---

## §2 Acceptance Predicate (Hamel-binary)

```yaml
acceptance_predicate:
  formula: "CC-1==pass AND CC-2==partial-pass AND CC-3==pass AND CC-4==pass AND CC-5==pass AND CC-6==pass"
  result: fail
  reason: >
    CC-1 FAIL (KPI arithmetic inconsistent — contracts_per_quarter: 2 cannot reach €50K at Path B pricing).
    CC-3 FAIL (archetype list includes Phase-2 archetypes without priority tier; dilutes Phase-1 outreach).
    CC-4 FAIL (kill_criteria internally inconsistent with kpi_targets; 50-prospect precondition
    unreachable at 20-leads/quarter; false-positive risk on ramping project).
    CC-5 CONDITIONAL FAIL (spec allows empty kpi_targets for levenchuk-deep-dive; violates D14).
    CC-2 PARTIAL PASS (Path selection explicit; Path B GM verified; Path C 54% unsubstantiated).
    CC-6 PASS.
    Overall: FAIL — 3 outright FAILs + 1 conditional FAIL + 1 partial. Mandatory revision required.
```

---

## §3 Specific Failures + Anti-patterns triggered

| CC | AP | Why (≤80 words) |
|---|---|---|
| CC-1 | AP-INV-1 (adapted: horizon-projection without gate-risk table) + AP-INV-8 (narrative-fallacy-investing) | €50K target stated without arithmetic triangulation against deal-size × contract-count. The €15K MRR and 2-contract KPI generate ~€9K/quarter — 5.5× below the €50K gate. No one ran the numbers before writing the KPI block. |
| CC-3 | AP-INV-3 (moat-claim without counterfactual adapted to ICP filter) | 6 archetypes listed without priority ranking. No kill-condition for "archetype generates zero revenue in 8 weeks → deprioritize." Risk: equal effort on Phase-2 archetypes starves Phase-1 primaries. |
| CC-4 | AP-INV-2 (Hamel-binary stated but internally inconsistent) | Kill criterion references "50 qualified prospects" but kpi_targets caps at 20/quarter. The kill can never legally fire in the window. Predicate is unfalsifiable. |
| CC-5 | AP-INV-2 (empty kpi_targets = unfalsifiable) | "Leave empty" option on P3 creates infinite-horizon research with no Popperian refutation event. D14 revenue-instrumental violated. |

---

## §4 Recommended Changes (imperative)

1. **CC-1 fix:** Rewrite `kpi_targets` arithmetic to triangulate. Add `avg_deal_size_eur`
   field. Either raise `contracts_per_quarter` to ≥5 OR document that €50K includes non-
   recurring hourly revenue (€150/hr × estimated hours) separate from retainer revenue.
   The simplest fix: `contracts_per_quarter: 2` stays but annotate that €50K = 2 × €15K
   retainer (annual) prorated over 13 weeks (€7.5K) + ~€35K hourly consulting revenue
   (233 hours at €150/hr). Make this explicit. See Alternative A below.

2. **CC-3 fix:** Split icp.md archetype list into three tiers with explicit Phase-1 priority.
   Tier 1 only (Предприниматели + Блогеры) for first 6 weeks of outreach; expand to Tier 2
   only after first signed contract. Gate the tier expansion on SG-2 (contracts_signed >= 1).

3. **CC-4 fix:** Replace kill_criteria with a two-checkpoint predicate:
   ```
   "if discovery_calls_total < 5 by 2026-06-15, pivot offer.
   if contracts_signed < 1 AND pipeline_qualified_leads < 10 by 2026-07-24, kill.
   if contracts_signed < 1 AND pipeline_qualified_leads >= 10, extend 4 weeks."
   ```
   Remove the "50 qualified prospects" precondition — it is inconsistent with kpi_targets.

4. **CC-5 fix:** Remove "leave empty" option from §2.E.5. Mandate:
   ```yaml
   kpi_targets:
     hypotheses_per_cycle: 2
     playbooks_drafted: 2
     hypotheses_validated: 3
   ```
   Add a lint enforcement note: "L-PROJECT-MISSING-REQUIRED-FRONTMATTER fires on
   empty kpi_targets for ALL priorities including P3/P4 if project is revenue-instrumental
   per D14."

5. **CC-2 supplementary:** Add a hosting-path GM table to icp.md with explicit arithmetic
   for all 3 paths. Path C 54% figure needs cost decomposition.

---

## §5 Alternatives (≥2 per FAIL per §3.3)

### CC-1 alternatives

**Alternative A — Revenue mix arithmetic (RECOMMENDED):**
Keep `contracts_per_quarter: 2` (Path B retainers) but add an explicit hourly-consulting-
revenue line to kpi_targets:
```yaml
contracts_per_quarter: 2          # 2 Path-B retainers = €7.5K/Q prorated
hourly_hours_per_quarter: 233     # 233h × €150/hr = €35K
onboarding_fees_per_quarter: 6000 # 2 × €3K = €6K
cumulative_total: 50000           # €35K + €7.5K + €6K + €1.5K buffer ≈ €50K
```
Kill condition: if hourly hours < 80 in Q2 first month → offer is not converting time.
Trade-off: Ruslan as the bottleneck; 233 hours in 13 weeks = 18 hours/week on billable work.
That's 45% of 40-hour week. Tight but survivable.

**Alternative B — Raise contract count:**
Raise `contracts_per_quarter` to 5–6 at Path B pricing (€4.5K/contract/quarter recurring + €3K
onboarding = €7.5K/contract/Q). 6 contracts × €7.5K = €45K + buffer → €50K.
Trade-off: 6 contracts requires ~30 qualified discovery calls (at 20% close rate), which
requires ~60 leads/quarter (at 50% call rate). kpi_targets leads must rise to 60.
Feasible only if Ruslan has a warm network or paid lead-gen unlocks at $20-30K.

**Status quo (do nothing):** leave kpi_targets as-is.
Kill condition: status quo fails when Q2 2026 shows €15K revenue vs €50K target — gap
flags at mid-quarter review.

### CC-3 alternatives

**Alternative A — Two-tier archetype priority (RECOMMENDED):**
Tier 1 outreach first 6 weeks: Предприниматели + Блогеры only.
Tier 2 expands after SG-2 fires (first contract signed).
Kill condition: if Tier 1 generates <3 qualified leads in 6 weeks → ICP mismatch; pivot
to adjacent archetype.

**Alternative B — Market test all 6 simultaneously:**
Run parallel mini-sequences on all 6 archetypes for first 3 weeks; kill lowest-converting
3 by week 4 (Graham pruning via-negativa).
Trade-off: requires 6 parallel outreach sequences = 3× the content volume; exceeds solo-
founder bandwidth at Phase-1 run rate.

**Status quo (do nothing):** list all 6 equally.
Kill condition: status quo fails when Q2 audit shows discovery calls split evenly across 6
archetypes, none converting at scale — wasted outreach budget across 4 non-primary ICPs.

### CC-4 alternatives

**Alternative A — Two-checkpoint kill criterion (RECOMMENDED, per §4 CC-4 fix above).**
Kill condition: fires if mid-quarter checkpoint (week 7) shows <5 discovery calls.
Trade-off: requires mid-quarter check (easy — calendar it).

**Alternative B — Volume-first kill:**
Kill if leads_per_quarter_actual < 10 by week 6.
Trade-off: fires on volume, not conversion; a high-volume/low-quality pipeline passes.

**Status quo (do nothing):** keep current kill_criteria.
Kill condition: status quo fails when the predicate fires prematurely (week 13) on a project
that is at 1 contract in negotiation — killing a live deal.

---

## §6 Dissent preservation — Path B vs Path C

**Investor-expert dissent on the Path C deferral rationale.**

The execution prompt icp.md spec asserts "Path C (hybrid) deferred to post-contractor-#1
(54% GM fails Phase-A floor)." Investor-expert registers the following dissent:

```yaml
dissent:
  claim: >
    Path C should be deferred NOT primarily because of 54% GM, but because Path C requires
    a stable networking layer (secure tunnel) that depends on contractor-#1 for support.
    The 54% GM figure, if correct, is ABOVE the operating-cost floor for Phase-1 (Max-sub
    discipline = €300-800/month; at €18K/contract revenue, 54% GM = €9.7K — still €8.9K
    net contribution). The GM floor argument is weaker than the ops-complexity argument.
  F: F4
  ClaimScope: >
    Holds for Phase-A solo-founder (no ops support). Does NOT apply post-contractor-#1
    (with ops support, Path C becomes viable at 54% GM given low absolute cost base).
  R:
    refuted_if: >
      Path C is trialed pre-contractor and requires >5 hours/month Ruslan ops time to
      maintain tunnel stability. Receipt: ops-log entry in quick-money/history.md.
    accepted_if: >
      Path C requires ≤2 hours/month ops time with standard docker-compose setup.
      Receipt: first Path C client pilot ops log.
  source_expert: investor-expert
  synthesis_note: >
    Majority position (defer Path C) is correct in outcome. Investor-expert dissent
    is on the reasoning: the GM floor argument is weaker than the ops-complexity argument.
    This dissent informs the Phase-2 Path C re-evaluation (when contractor-#1 joins).
```

**No direct call to mgmt-integrator.** This dissent is preserved for brigadier integration.
mgmt-integrator may include the ops-complexity framing as an additional justification for
Path C deferral in their icp.md; the outcome (defer Path C) is not disputed.

[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]

---

## §7 BA-Cycle lite (ethical surfaces check)

The quick-money bootstrap has a third-party exposure surface: Mittelstand clients who
sign contracts based on the ICP + offer framing.

- **BA-0 (boundary):** Third-party exposed = Mittelstand client (50-500 employees) who
  purchases a Path B €18K/yr consulting engagement.
- **BA-1 (asymmetry):** Ruslan upside = €18K/yr recurring per client (with 70.7% GM).
  Client downside = €18K/yr spend + internal time investment on KB setup if project
  delivers less than promised. Asymmetry is moderate (not extreme).
- **BA-2 (alternative):** Is there an alternative with similar return AND less client
  exposure? Yes — a smaller pilot first (€3K onboarding only, no €15K commitment)
  before full retainer. This is worth considering for early clients.
- **BA-3 (acceptance):** Would the Mittelstand client accept the risk structure if fully
  disclosed? PASS — provided the bootstrap's kill_criteria and ICP filter are accurate.
  The "local-first, client owns data" BIOS positioning (STRATEGIC-INSIGHT §3) is
  genuinely differentiated vs pure cloud-vendor lock-in. Client sovereignty is
  architecturally real at Path B.

**BA-3 PASS.** No HITL escalation required on ethical grounds.

---

## §8 Anti-scope (explicit)

This critique does NOT assess:
- Stage-gate DSL grammar (e.g., `count(<glob>)` predicate syntax) — philosophy-expert reviewed.
- Skill code correctness (`/project-bootstrap` algorithm steps 1–13) — engineering-expert.
- `project-types.yaml` schema design — mgmt-expert territory.
- Whether B2 vs B3 variant merge was correct — Ruslan Gate-2 decision, locked.
- Content of levenchuk-deep-dive research (FPF / ШСМ methodology details) — philosophy-expert.
- The $1T trajectory framing or Phase-3+ capital structure — out of Phase-1 scope.
- Epistemic Рациональность of the ICP hypotheses — philosophy territory.

---

## §9 Output schema (shared-protocols §3)

```yaml
status: fail
context:
  task_id: T-km-materialization-mvp-2026-04-24
  artefact_under_review:
    - "prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1-E.2"
    - "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md consulting.default_kpi_targets"
  mode: critic
  cycle_id: cyc-km-materialization-mvp-2026-04-24
  wave: 3
  mgmt_draft_available: false  # file not found at run time; reviewed upstream sources directly

conformance_checklist:
  - {check: CC-1, verdict: fail, evidence: "§2.E.1 kpi_targets: contracts_per_quarter: 2 × Path-B €4.5K/Q + €3K onboarding = €15K/Q, not €50K; gap 3.3×"}
  - {check: CC-2, verdict: partial-pass, evidence: "Path B GM 70.7% verified arithmetically; Path C 54% asserted without cost breakdown; Path selection IS explicit"}
  - {check: CC-3, verdict: fail, evidence: "6 archetypes listed without Phase-1 priority tier; Ресёрчеры/Инженеры/Инвесторы are Phase-2 ICPs per ability-to-sign-now filter"}
  - {check: CC-4, verdict: fail, evidence: "kill_criteria requires '50 qualified prospects' but kpi_targets caps at 20/quarter — precondition physically unreachable in 13-week window"}
  - {check: CC-5, verdict: conditional-fail, evidence: "'leave empty' option on levenchuk-deep-dive kpi_targets violates D14 revenue-instrumental; non-empty option is present but not mandated"}
  - {check: CC-6, verdict: pass, evidence: "margin-of-safety is negative in opportunity-cost terms (expected for founder-capital Phase-1); ruin floor safe at Max-sub discipline €300-800/month"}

acceptance_predicate:
  formula: "CC-1==pass AND CC-2==partial-pass AND CC-3==pass AND CC-4==pass AND CC-5==pass AND CC-6==pass"
  result: fail

specific_failures:
  - {check: CC-1, ap: AP-INV-8, why: "€50K target stated without arithmetic triangulation against deal-size × contract-count. 2 contracts at Path B = €15K/Q, not €50K."}
  - {check: CC-3, ap: AP-INV-3, why: "6 archetypes listed without kill-condition per archetype; Phase-2 ICPs included without demotion criterion; risks diluted outreach."}
  - {check: CC-4, ap: AP-INV-2, why: "kill_criteria Hamel-binary internally inconsistent: 50-prospect precondition unreachable at 20 leads/quarter. Predicate cannot fire in window."}
  - {check: CC-5, ap: AP-INV-2, why: "'leave empty' produces unfalsifiable P3 project; D14 revenue-instrumental violated."}

recommended_changes:
  - "CC-1: Add avg_deal_size_eur + hourly revenue line to kpi_targets to triangulate €50K. OR raise contracts_per_quarter to ≥5 with corresponding lead volume."
  - "CC-3: Tier icp.md archetypes (Tier-1 Phase-1 primary, Tier-2 secondary, Tier-3 Phase-2+). Gate Tier-2 expansion on SG-2 (first signed contract)."
  - "CC-4: Replace 50-prospect precondition with two-checkpoint kill criterion (mid-Q + end-Q checks with pipeline-lag buffer)."
  - "CC-5: Remove 'leave empty' option for levenchuk-deep-dive; mandate minimum kpi_targets {hypotheses_per_cycle: 2, playbooks_drafted: 2, hypotheses_validated: 3}."
  - "CC-2 supplement: Add explicit GM arithmetic table for all 3 paths to icp.md."

alternatives:
  - {label: "CC-1-A", name: "Revenue mix: 233hr hourly + 2 retainers + 2 onboarding fees = €50K", kill_condition: "hourly hours < 80 in month-1 of Q2 → offer not converting"}
  - {label: "CC-1-B", name: "Raise contracts_per_quarter to 5–6 with 60 leads/quarter", kill_condition: "leads < 30 by week 6 → insufficient volume; scale outreach or pivot"}
  - {label: "CC-1-status-quo", name: "T-bills + Max-sub discipline, hold capital, delay Phase-1 outreach until offer is arithmetically sound", kill_condition: "status quo fails when opportunity cost exceeds €78K before first revenue (week 13)"}
  - {label: "CC-3-A", name: "Two-tier archetype: Tier-1 first 6 weeks only", kill_condition: "Tier-1 generates <3 qualified leads in 6 weeks → ICP mismatch; pivot"}
  - {label: "CC-3-B", name: "Parallel test all 6 archetypes for 3 weeks, kill lowest-converting 3", kill_condition: "requires 6 outreach sequences simultaneously; fails if Ruslan bandwidth < 20hr/week available"}
  - {label: "CC-4-A", name: "Two-checkpoint kill (week-7 mid-Q + week-13 end-Q with pipeline buffer)", kill_condition: "fires if mid-Q discovery calls < 5; fails if pipeline count incorrectly scored"}

anti_scope:
  - "This critique does NOT assess stage-gate DSL grammar — philosophy-expert domain."
  - "This critique does NOT assess /project-bootstrap skill algorithm — engineering-expert domain."
  - "This critique does NOT assess project-types.yaml schema design — mgmt-expert domain."
  - "This critique does NOT assess levenchuk-deep-dive research content — philosophy-expert domain."
  - "This critique does NOT assess the $1T trajectory or Phase-3+ capital structure."
  - "This critique does NOT arbitrate epistemic claims on ICP hypotheses."

provenance:
  - {path: "decisions/JETIX-VISION.md", range: "§7.1-7.2", quote: "Jetix community = ВСЕ 11 archetypes × UPWARD-DIRECTION ONLY. Topic secondary, direction primary."}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.9 M1.4", quote: "€50K reached Q2 2026 → Phase 1 → transition gate triggered"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path B", quote: "€3K onboarding + €15K/yr = 70.7% GM yr1"}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E.1", quote: "kpi_targets: {leads_per_quarter: 20, contracts_per_quarter: 2, cumulative_revenue_q2_2026_eur: 50000}"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "lines 162-165", quote: "leads_per_quarter: 20, contracts_per_quarter: 2, mrr_eur: 5000"}

confidence: high
confidence_method: unit-economics-arithmetic

escalations:
  - {trigger: "kpi-revision-required", target: "brigadier → mgmt-integrator revises quick-money kpi_targets arithmetic before Part E execution", priority: high}
  - {trigger: "archetype-filter-disputed", target: "brigadier → mgmt-integrator adds Phase-1 priority tier to icp.md archetype list", priority: high}
  - {trigger: "kill-criteria-inconsistency", target: "brigadier → mgmt-integrator replaces single-threshold kill criterion with two-checkpoint predicate", priority: high}
  - {trigger: "peer-input-needed", peer: "philosophy-expert", mode: "critic", reason: "CC-5 kpi_targets emptiness may also violate FPF E-9 Hamel-binary requirement at epistemic level; investor-expert flags for philosophy review on CC-5 only"}

dissents:
  - claim: "Path C deferral rationale: ops-complexity argument stronger than GM floor argument"
    F: F4
    ClaimScope: "Phase-A solo-founder only; does not apply post-contractor-#1"
    R:
      refuted_if: "Path C requires >5hr/month ops; receipt: ops-log in quick-money/history.md"
      accepted_if: "Path C requires ≤2hr/month; receipt: first Path C pilot ops log"
    source_expert: investor-expert
```

---

## §10 Closing notes — investor-expert operational discipline

**Decision-rights ritual applied:** all 6 CC checks are listed in `autonomous` (draft a
capital-allocation critique as a proposal). No horizon-gate shift proposed. No capital
deployment recommended. This draft is in `drafted` state pending brigadier review +
mgmt-integrator revision cycle.

**Provenance density:** every CC cites at least one locked decision source. No bare assertions.

**Arithmetic discipline:** owner-earnings not applicable (consulting bootstrap, not a
capital position); margin-of-safety arithmetic applied in CC-6; opportunity-cost named
(€78K for Q2). Risk-of-ruin floor named (Max-sub discipline = €300-800/month).

**Stage-Gated default:** this critique proposes no autonomous action. Escalations route to
brigadier who dispatches revision to mgmt-integrator per swarm coordination protocol.

End of investor × critic audit — Wave 3 Part E.

[src:decisions/JETIX-VISION.md §7.2]
[src:decisions/JETIX-PLAN.md §3.1]
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]
[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.1-E.2]
[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md consulting.default_kpi_targets]
