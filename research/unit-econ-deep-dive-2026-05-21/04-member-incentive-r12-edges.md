---
title: DR-26 Phase 4 — Member-Incentive Math + R12 Anti-Extraction Edges
date: 2026-05-21
type: research-substrate
parent_prompt: prompts/dr-26-unit-econ-deep-dive-2026-05-21.md
phase: 4
F: F4
G: dr-26-phase-4-member-incentive-r12-edges
R: refuted_if_math_model_off_by_>20%_OR_R12_threshold_misattributed_OR_LOCK_text_modified
constitutional_posture: R1 + R6 + R12 + IP-1 STRICT + EP-5 + append-only + R12 paired-frame DISCIPLINE
prose_authored_by: brigadier-scribe (Cloud Cowork — autonomous Phase 4 substrate compile)
language: russian primary
---

# DR-26 Phase 4 — Member-Incentive Math + R12 Anti-Extraction Edges

> **Цель Phase 4.** Зафиксировать quantitative member-incentive math (per-partner unit econ + ROI first-cohort + cohort-growth compound + break-even) + explicit R12 anti-extraction edge analysis (что считается «extraction beyond agreed share» quantitatively?).

---

## §1 Member-incentive math

### §1.1 Per-partner unit economics — model assumptions

Базовая model assumes Phase 1 Jetix Workshop / Hackathon partnership cohort, simplified:

```
Member = participant в Jetix Workshop / Hackathon cohort
Revenue generated per member per month = R (variable per scenario)
Take rate (institutional retention) = T (variable per scenario)
Member-direct share = D = (1 - T)
```

Model assumptions for baseline:
- R = €1500-3000 per member per month (commercial Workshop / advisory hybrid; rough placeholder)
- T = 0.15 / 0.20 / 0.25 / 0.30 (4 scenarios)
- Operations cost (Ruslan + brigadier + infrastructure) = €5000-15000 per month (rough placeholder)
- First-cohort size: 5-15 (per Distribution Plan §0.2 + audio_686 cascade 150→15→1M)
- Workshop cohort duration: 3-6 months typical cycle

**Caveats:**
- R = placeholder; actual Jetix Phase 1 pricing TBD (workshop fee + advisory fee + Foundation revenue)
- Operations cost = placeholder; Ruslan personal compensation + brigadier infrastructure + Substrate maintenance
- Pricing model not yet locked (per Distribution Plan §5 placeholder fill); Phase 5 sensitivity will vary

### §1.2 Per-member monthly economics — 4 take-rate scenarios

Assume baseline R = €2000 per member per month (mid-range placeholder):

| Scenario | T | D (member direct) | Member monthly share | Institutional share |
|---|---|---|---|---|
| Conservative | 15% | 85% | €1700 | €300 |
| Ruslan-voiced low | 20% | 80% | €1600 | €400 |
| Ruslan-voiced high | 25% | 75% | €1500 | €500 |
| Aggressive | 30% | 70% | €1400 | €600 |

### §1.3 First-cohort joiners ROI calculation

**Setup:** First cohort 10 members; 3-month Workshop cycle; member time investment ~10 hours per week × 13 weeks = 130 hours.

**Member output value (rough proxy):** what they could earn at fully-priced consulting hourly rate (~€50-150 per hour) if not in cohort = €6500-19500 (opportunity cost).

**Member receives from Jetix:**
- Direct: D × R × 3 months = 0.75-0.85 × €2000 × 3 = €4500-5100 (at 25% / 15% T)
- Indirect: cohort substrate access + Foundation lineage + reputation token + future Clan governance voice + skills development + network access

**Member ROI calculation (conservative): break-even if indirect value ≥ opportunity cost − direct payment.**

| T | Direct payment 3 months | Indirect-value-needed-to-break-even (low opportunity cost €6500) | Indirect-value-needed-to-break-even (high opportunity cost €19500) |
|---|---|---|---|
| 15% | €5100 | €1400 minimum indirect value perceived | €14400 minimum indirect value |
| 20% | €4800 | €1700 minimum | €14700 minimum |
| 25% | €4500 | €2000 minimum | €15000 minimum |
| 30% | €4200 | €2300 minimum | €15300 minimum |

**Interpretation:** at 25% T, first-cohort member needs to perceive ≥€2000-15000 worth of indirect value (substrate access + network + reputation + Foundation lineage) per 3-month cohort to feel net-positive ROI. **This is plausible** if substrate is rich + cohort positions member для high-value future opportunities (per Distribution Plan §0.2 1M user cascade KEYSTONE).

**Counter-evidence:** if Workshop produces nothing of indirect value, member only perceives direct payment − opportunity cost = potential net-negative. → critical that substrate + cohort positioning + reputation delivers tangible value beyond direct revenue share.

### §1.4 Compound growth: take rate → community pool → cohort expansion

Per Mondragón pattern + Phase 2 §3 distribution skeleton:

```
Take rate T% = institutional retention
  R component (retention для R&D / Workshop scaling) → fuels cohort expansion
  M component (matching pool QF) → fuels emerging Clan initiatives
  O component (Foundation operations) → fuels Ruslan + brigadier sustainability
```

**Cohort expansion via R-component reinvestment:**

Assume R-component = 50% of institutional take rate (Mondragón pattern); 50% of revenue captured for reinvestment loop.

| Year | Cohort size | Revenue per cohort cycle | T = 25%; R-component | Reinvestment available | Cohort scaling possible |
|---|---|---|---|---|---|
| Year 1 | 10 members | €2000 × 10 × 12 = €240K | €60K institutional; €30K R-component | €30K | scale to 15-20 Year 2 |
| Year 2 | 20 members | €480K | €120K; €60K R-component | €60K | scale to 30-40 Year 3 |
| Year 3 | 50 members | €1.2M | €300K; €150K R-component | €150K | scale to 100 Year 4 |
| Year 4 | 100 members | €2.4M | €600K; €300K R-component | €300K | federation transition possible |

**Note:** This is illustrative; assumes consistent R per member, retention; ignores churn, externals, etc. Actual dynamics will vary substantially.

**Insight:** at 25% take rate × 50% retention component, reinvestment compounds approximately ~2× per year при cohort expansion follows. Aggressive scaling possible.

### §1.5 Break-even analysis

**Break-even definition:** Foundation operations cost (Ruslan + brigadier + infrastructure) covered by O-component of institutional take rate.

Assume operations cost ~€10K/month = €120K/year (placeholder; actually depends on Ruslan personal compensation + AI infrastructure + Foundation overhead).

| T | O-component (assume 5% of revenue) | Revenue needed annually для break-even |
|---|---|---|
| 15% | 5% O-share | €120K / 0.05 = €2.4M annual revenue |
| 20% | 5% O-share | €2.4M |
| 25% | 5% O-share | €2.4M |
| 30% | 5% O-share | €2.4M |

If O-component fixed % of revenue (5%), break-even cohort revenue same across T scenarios.

**Alternative:** O-component sized в absolute terms (€120K/year fixed) — then take rate covers это первым:

| T | Member-direct D | First-priority share goes to: |
|---|---|---|
| 15% | 85% | Operations first (€120K), then R + M from remainder |
| 25% | 75% | More remainder для R + M after operations |
| 30% | 70% | Maximum remainder для R + M |

**Practical implication:** at low T (15%), Foundation operations + reinvestment loop both squeezed simultaneously → fragile sustainability.
At higher T (25-30%), comfortable reinvestment AND operations sustainability.

### §1.6 Self-sustaining cohort threshold

**Threshold definition:** cohort size + revenue per member such that R-component reinvestment ≥ cost of next cohort onboarding (training + materials + scholarship slots).

**Assume:** cohort onboarding cost = €5K per new member (Workshop materials + mentorship + onboarding time).

| T | R-component (assume 50% of T) | Per-member institutional € | New-members-supportable per existing member |
|---|---|---|---|
| 15% | 7.5% | €150 / year per member | 0.03 new member per existing |
| 25% | 12.5% | €250 / year per member | 0.05 new member per existing |
| 30% | 15% | €300 / year per member | 0.06 new member per existing |

**Insight:** even at 30% take rate, reinvestment per-member only supports ~6% new-member growth annually if onboarding cost €5K each. → Cohort growth via reinvestment is **gradual**, не explosive.

**Counter-evidence:** if onboarding cost lower (€2K per new member, more standardised materials), growth rate doubles. If external matching pool achievable (Optimism-style sequencer-fee-funded analogue), growth uncapped.

**Conclusion:** sustainable cohort growth via reinvestment is feasible at 20-30% take rate; explosive growth requires external matching pool OR lowering per-member onboarding cost.

---

## §2 R12 anti-extraction edges (quantitative threshold analysis)

### §2.1 R12 verbatim text (LOCKED 2026-05-12)

Per `principles/tier-2-system/foundation-generic/ai-does-not-extract-value-beyond-agreed-share.md` LOCKED:

> «AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

**Russian (CLAUDE.md §4.1 inline):**

> «AI / substrate не может извлекать ценность из участников сверх согласованной доли; участники могут отделиться и уйти без штрафа.»

### §2.2 «Agreed share» — quantitative interpretation

«Agreed share» implies **explicit member ack** of revenue split + take rate + reinvestment loop. Operational interpretation:

1. **Charter-stated take rate** = canonical baseline; member acks Charter before joining Clan
2. **Any take rate change post-ack** requires re-ack + opt-out window (fork-and-leave right preserved)
3. **Smart contract (Phase 2+ Option D Hybrid)** enforces immutable distribution params per round; upgrade requires multi-sig + time-lock + DAO quorum (per R12 programmable ack §4)

**Quantitative «agreed share»:** the take rate published in Clan Charter at member signup = legal-binding baseline.

### §2.3 «Beyond agreed share» — operational definition

| Action | R12 violation? |
|---|---|
| Foundation increases take rate с 25% to 30% без member re-ack | ✅ YES — extraction beyond agreed share |
| Foundation reduces reinvestment loop share to operations-only без member ack | ✅ YES — reinvestment loop implied in agreed share |
| Member exits с reputation history preserved + treasury share + no penalty | ❌ NO — R12-compliant exit |
| Foundation collects data from member activity без disclosure / consent | ✅ YES — data extraction beyond agreed share |
| Foundation routes member contacts / leads к external (non-Jetix) commercial activity | ✅ YES — contact-extraction beyond agreed share |
| Take rate ≤ Charter baseline + transparent reinvestment loop articulation | ❌ NO — within agreed share |

### §2.4 Quantitative R12 boundary thresholds — three readings

Per memory `feedback_constitutional.md` + Левенчук distillation §2.7 systemic ethics cross-link, three plausible readings:

**Reading A — Strict procedural (binding text):**
> «R12 violation = any deviation from explicit Charter-stated revenue split without re-ack.»
- 25% Charter-stated → 25% only is compliant; 25.01% is violation
- Pros: bright-line; constitutionally clean
- Cons: rigid; doesn't accommodate Phase-gradient (15%→20%→25%) without explicit per-phase re-ack

**Reading B — Functional Mondragón-ratio:**
> «R12 violation = wage-payout ratio exceeds Mondragón cap (5:1 default) OR institutional retention exceeds Mondragón threshold (~60-70%).»
- Allows take rate variance up to functional cap (Mondragón 60% institutional)
- Pros: room для Phase gradient; cooperative-aligned
- Cons: subjective threshold; needs explicit calibration

**Reading C — Outcome-based:**
> «R12 violation = if member ROI net-negative across reasonable indirect-value assessment, regardless of take rate %.»
- Take rate could be 0% but still violate R12 if substrate non-functional
- Take rate could be 30% but R12-compliant if substrate delivers commensurate value
- Pros: substantive; outcome-driven
- Cons: hard to enforce programmatically; subject to interpretation

### §2.5 Recommended hybrid reading для Jetix

**Combined operationalisation (recommended; subject to Ruslan ack):**

1. **Charter publishes explicit take rate** (Reading A binding text discipline) at member signup
2. **Charter publishes Mondragón ratio cap** (Reading B; 5:1 default; Clan-configurable) — institutional vs member-direct share ratio bounded
3. **Charter publishes reinvestment loop articulation** (Reading C; explicit «what reinvestment does and member-benefit pathway») — substrate substance committed
4. **Any change to (1)+(2)+(3) requires re-ack + 30-day opt-out window** (R12 fork-and-leave protection)
5. **Smart contract Phase 2+ enforces (1)+(2)** programmatically (per R12 programmable Option D Hybrid)
6. **R12 ethical-surface review** (KA-07 pattern) audits (3) substrate-deliverable health on quarterly basis

### §2.6 Edge case — Phase gradient take rate

Per Phase 2 §4.3 piecewise gradient hypothesis:

> 25% Phase 1 → 20% Phase 2-3 → 15% Phase 4-5

**R12 lens:** if gradient explicitly Charter-stated at member signup (e.g., «Clan operates 25% take rate Year 1; expected к decrease to 15% by Year 5 as scale efficiency improves»), member acks gradient → no R12 violation.

If gradient NOT Charter-stated и Foundation adjusts post-hoc → violation.

**Operational implication:** Charter language MUST publish gradient if planned, or commit к flat rate per period.

### §2.7 Edge case — 30%+ take rate

**At 30% take rate:**
- Mondragón institutional pattern was ~60% institutional / 40% member; 30% is between Mondragón institutional and middle-cooperative band → **not constitutionally precluded**
- Education-platform comparable (Coursera 50%, Udemy 37-63%) → 30% is **moderate** by education-platform standard
- Member-direct share = 70% → still majority direct; cohort-platform-comparable bounds (Maven 10% take → 90% direct; Coursera 50% take → 50% direct)

**R12 assessment at 30%:**
- Reading A: compliant if Charter-stated at signup
- Reading B: Mondragón cap (60% institutional) significantly above 30%; well within cooperative band; compliant
- Reading C: substrate-delivery question; if Workshop / Hackathon / Foundation delivers commensurate value, compliant

**Conclusion:** 30% take rate is **not categorically R12-violating** if (1) Charter-stated + (2) reinvestment loop articulated + (3) substrate delivers value commensurate с extraction. **Risk:** at 30%, R12 paired-frame discipline must be strict в outreach language; «extraction-beyond-agreed-share» perception risk higher than at 15-25% range.

### §2.8 Edge case — variable take rate per audience tier

Per Phase 2 §3.4 cooperative ownership stake (per Clan / per member) and per Distribution Plan §3 audience tiers (Tier-1 / L1 / L2 / L3) — could Jetix charge different take rates per audience type?

**Scenarios:**
- Tier-1 named partners: low take rate (15%); high-leverage individuals; Foundation-building
- L1 engineers Workshop founding cohort: moderate (20-25%); main revenue source
- L2 amplifier community: low or zero (community pool funded externally; per Optimism RetroPGF pattern)
- L3 institutional clients: high (30-50% consulting-style markup; institutional-budget audience)

**R12 lens:** variable take rate per audience tier OK if **transparently Charter-stated** + **member-class-aware** (each member acks specific tier rate). However:

- **Risk:** drift к «two-tier extraction» pattern (Mondragón Eroski peripheral-contractor caveat) — must clearly distinguish R12-protected member-class from R12-different non-member arrangement
- **Mitigation:** Clan Charter explicitly defines who is «member» vs «non-member»; only members protected by R12; non-members operate under explicit contract terms separately

### §2.9 4 R12 RUSLAN-LAYER action classes (per programmable ack §4)

Per `.claude/config/default-deny-table.yaml` RUSLAN-LAYER overlay extension (acked 2026-05-18):

| Action class | Default-Deny trigger | Phase 4 quantitative interpretation |
|---|---|---|
| `extraction_beyond_share` | Agent attempts charge beyond Charter-stated take rate OR captures non-revenue value (data / contacts / IP) beyond agreed scope | Programmatic block when take_rate_charged > Charter.take_rate; off-chain auditable via revenue logs |
| `wage_ratio_violation` | Payout spread exceeds Mondragón ratio cap (5:1 default) | Programmatic block when max_payout > min_payout × ratio_param |
| `non_consensual_distribution` | Foundation distributes revenue without DAO quorum + ratio cap check | Programmatic gate за per-round distribution event |
| `fork_prevention_attempt` | Foundation refuses or penalizes member exit (R12 fork-and-leave protection) | Programmatic check on exit event; treasury share automatic; no penalty |

**All 4 carry F4-F5 blast-radius** per programmable ack §4; halt_log_alert enforcement; smart contract Phase 2+ enables programmatic enforcement.

---

## §3 Cross-cutting member-incentive vs R12 trade-off

### §3.1 Sustainability vs Anti-extraction tension (Phase 1 §8.2)

Phase 1 cross-cutting observed: low take rate (0-10%) = R12-strong but sustainability-fragile; high retention (Mondragón 60%) = sustainable but requires institutional discipline.

**Jetix Phase 1 specific:** Foundation operations cost (Ruslan + brigadier + infrastructure) substantial при scale 5-15 founding cohort; cannot achieve 0% take rate Phase 1 без external matching. Realistically take rate must be ≥10% Phase 1.

### §3.2 Member ROI vs Foundation Sustainability matrix

```
                  | Member ROI > opportunity cost | Member ROI < opportunity cost
------------------|-------------------------------|--------------------------------
Found. sustainable| ✅ Equilibrium                | ⚠️ Substrate-delivery problem
Found. unsustain. | ⚠️ Donation pattern (R12 risk)| ❌ Failure mode
```

**Sweet spot:** Foundation sustainable + Member ROI net-positive across reasonable indirect-value assessment.

### §3.3 Three operational pillars (synthesised from §1 + §2)

For any take rate T to be R12-compliant operationally:

1. **Charter publishes T explicitly** at member signup
2. **Substrate delivers indirect value ≥ member opportunity cost − direct payment** (substantive R12 Reading C)
3. **Reinvestment loop articulated + measurable** (R12 paired-frame: extraction-paired-with-value-return)

**At 15% T:** substrate-delivery threshold low (member shares 85% direct); R12-relaxed; sustainability-fragile.
**At 25% T:** substrate-delivery threshold moderate; R12-discipline normal; sustainability-comfortable.
**At 30% T:** substrate-delivery threshold high; R12-discipline strict; sustainability-strong.

---

## §4 Open questions for Phase 5 sensitivity

1. **What is realistic R per member?** Phase 5 will model €1500 / €2000 / €3000 sensitivity.
2. **Operations cost trajectory:** as cohort scales, does ops cost remain ~€120K/year или scales? Phase 5 will model.
3. **External matching pool achievability:** when (Phase 2? 3? 4?) does Optimism-style funding become viable?
4. **Cohort onboarding cost:** how Workshop materials standardisation reduces per-member onboarding cost over time?
5. **Member churn rate:** at what take rate / substrate-delivery quality does churn become acceptable (<10% annual)?

---

## §5 Closure Phase 4

Member-incentive math compiled с per-member monthly economics + first-cohort ROI calculation + compound growth via reinvestment + break-even analysis + self-sustaining cohort threshold. R12 anti-extraction edges explored с 3 readings (procedural / Mondragón-functional / outcome-based); recommended hybrid operationalisation. Quantitative thresholds для 4 RUSLAN-LAYER action classes documented. Edge cases (Phase gradient / 30%+ / per-audience variable) analysed.

**Working conclusion для Phase 5:** Jetix Phase 1 take rate likely in 15-30% range; R12-compliance achievable at all 4 scenarios IF Charter discipline + substrate-delivery + reinvestment loop articulation in place. **Sustainability skew higher (20-25%) preferred; R12-strictness skew lower (15%); equilibrium likely 20-25% with explicit Mondragón ratio cap.**

**Commit:** `[dr-26] Phase 4 member-incentive math + R12 edges`

---

*Phase 4 closure 2026-05-21. F4 / G: dr-26-phase-4-member-incentive-r12-edges / R: refuted_if_math_model_off_by_>20%_OR_R12_threshold_misattributed_OR_LOCK_text_modified.*
