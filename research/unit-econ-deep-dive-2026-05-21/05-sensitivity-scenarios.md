---
title: DR-26 Phase 5 — Sensitivity Scenarios + Reinvestment Loop Modeling
date: 2026-05-21
type: research-substrate
parent_prompt: prompts/dr-26-unit-econ-deep-dive-2026-05-21.md
phase: 5
F: F4
G: dr-26-phase-5-sensitivity-scenarios
R: refuted_if_math_model_off_by_>30%_OR_R12_compliance_misjudged_OR_assumptions_undeclared
constitutional_posture: R1 + R6 + R12 + IP-1 STRICT + EP-5 + append-only + R12 paired-frame DISCIPLINE
prose_authored_by: brigadier-scribe (Cloud Cowork — autonomous Phase 5 substrate compile)
language: russian primary
---

# DR-26 Phase 5 — Sensitivity Scenarios + Reinvestment Loop Modeling

> **Цель Phase 5.** Зафиксировать 4 take-rate scenarios (15% / 20-25% / 30% / piecewise gradient) с math model + 5-year sensitivity projections + reinvestment loop dynamics + R12 compliance check per scenario.

---

## §1 Shared assumptions across scenarios

### §1.1 Baseline numerical assumptions

Все 4 scenarios share these baseline placeholders (sensitivity-adjustable):

| Variable | Baseline | Sensitivity range | Rationale |
|---|---|---|---|
| **R** = revenue per member per month | €2000 | €1500-3000 | Workshop + advisory hybrid; Phase 3 §6 cohort-platform comparable (Maven $1000-3000/cohort cycle [src: Maven public pricing 2023-2024]) |
| **Initial cohort size Y1** | 10 members | 5-15 members | Distribution Plan §0.2 Q3 2026 Workshop founding cohort target |
| **Cohort growth multiplier Y2-Y5** | 1.5-2.5× per year | 1.2-3.0× | Compound growth от R-component reinvestment loop (Phase 4 §1.4 illustrative) |
| **Foundation operations cost** | €120K/year (€10K/month) | €80K-200K/year | Ruslan personal compensation + brigadier infrastructure + Foundation overhead; placeholder |
| **Onboarding cost per new member** | €5K | €2K-10K | Workshop materials + mentorship time; scales down via standardisation |
| **Member churn rate annual** | 15% | 5-30% | Cohort attrition; lower if substrate-delivery + R12 paired-frame strong |
| **Mondragón ratio cap** | 5:1 | 3:1-9:1 | Charter-stated; Clan-configurable per H7 / R12 programmable ack |
| **Take rate split** | R=50% / M=25% / O=25% of T | sensitivity-adjustable | Mondragón-style retention pattern |

### §1.2 Critical caveat

These assumptions are placeholders для sensitivity modeling. **Actual values depend on:**

- Phase 1 Workshop pricing decision (Ruslan strategic prose)
- Foundation operations cost reality (Ruslan personal compensation expectations + infrastructure cost)
- Cohort acquisition cost reality (depends on Distribution Plan execution + cascade quality)
- Macro AI/crypto cycle effects (Phase 4 sustainability check)

**Sensitivity tables below should be read as directional, не prescriptive numbers.**

---

## §2 Scenario A — Conservative (15% take rate)

### §2.1 Setup

- **T = 15%**
- **Risk:** low R-1 (R12 paired-frame slippage risk minimal — generous member share)
- **R-component:** 7.5%; M-component: 3.75%; O-component: 3.75%

### §2.2 Year-1 economics

```
Cohort: 10 members × €2000 R × 12 months = €240,000 annual revenue
Member-direct (D = 85%) = €204,000 (€20.4K per member annually)
Institutional take (T = 15%) = €36,000
  R-component (reinvestment) = €18,000
  M-component (matching pool) = €9,000
  O-component (operations) = €9,000
```

**Operations cost €120K/year — Year-1 deficit:**
- O-component available €9K vs €120K need
- **Deficit: €111K**
- Compensated only via external funding (Foundation seed / personal capital / Anthropic / VC) OR Ruslan non-Jetix revenue

### §2.3 5-year projection (Conservative)

| Year | Cohort | Revenue | T (15%) | R-comp | M-comp | O-comp | Ops gap | Cumulative gap |
|---|---|---|---|---|---|---|---|---|
| Y1 | 10 | €240K | €36K | €18K | €9K | €9K | -€111K | -€111K |
| Y2 | 15 | €360K | €54K | €27K | €13.5K | €13.5K | -€106.5K | -€217.5K |
| Y3 | 25 | €600K | €90K | €45K | €22.5K | €22.5K | -€97.5K | -€315K |
| Y4 | 40 | €960K | €144K | €72K | €36K | €36K | -€84K | -€399K |
| Y5 | 60 | €1.44M | €216K | €108K | €54K | €54K | -€66K | -€465K |

**Sustainability assessment:** **NEGATIVE** при single baseline ops cost. Foundation operations не покрываются T = 15% даже Y5; cumulative deficit €465K over 5 years.

**Mitigation options для Conservative:**
- External matching pool (Foundation grant / Anthropic / VC funding €100-150K annually)
- Lower ops cost (Ruslan absorbs personal compensation reduction; brigadier infrastructure lean)
- Higher R per member (€3000 instead of €2000; doubles revenue → revenue €480K Y1; ops gap reduces к -€84K Y1)
- Different T split (more O-component, less R/M): T = 15% with O=10%; R=2.5%; M=2.5% — ops gap better but reinvestment slower

### §2.4 Cohort growth model (Conservative)

```
Cohort_Year+1 = Cohort_Year × (1 + reinvestment_capacity_factor − churn_rate)
  where reinvestment_capacity_factor = R-component / (onboarding_cost × current_cohort)
```

Y1: R-comp €18K / €5K per new member = 3.6 new members supportable; growth multiplier ~1.36× minus churn 15% = ~1.2×
Y2: R-comp €27K / €5K = 5.4 new members; growth ~1.3× minus churn = ~1.15× — slowing
**Growth rate decelerates** при flat per-member ops cost; needs onboarding cost reduction OR external matching to break trajectory.

### §2.5 R12 compliance check (Conservative)

- ✅ Reading A (procedural): Charter-stated 15% rate; member-direct 85%
- ✅ Reading B (Mondragón-functional): institutional retention 15% well below Mondragón 60% cap
- ✅ Reading C (outcome-based): substrate-delivery threshold low (member shares 85% direct)
- **Overall: R12-strong.** But Foundation sustainability vulnerability creates pressure to drift extraction patterns (e.g., contact-extraction, data-extraction) — must monitor.

### §2.6 Conservative bottom line

**Pros:** R12-exemplar; member-friendly; lowest extraction perception risk; high reinvestment / direct member ratio
**Cons:** Foundation sustainability deficit; external funding dependency Year 1-5; growth rate slow без external pool
**Best fit:** if external funding (Foundation / VC / Anthropic) secured for Year 1-3 + Workshop pricing scales к €3000/month + Onboarding cost reduces к €2-3K per member

---

## §3 Scenario B — Ruslan-voiced 20-25%

### §3.1 Setup

- **T = 22.5% (midpoint 20-25%)** — represents Ruslan voice anchor
- **Risk:** medium R-1 (R12 paired-frame discipline needed but not strict-extreme)
- **R-component:** 11.25%; M-component: 5.625%; O-component: 5.625%

### §3.2 Year-1 economics

```
Cohort: 10 × €2000 × 12 = €240,000 revenue
Member-direct (D = 77.5%) = €186,000 (€18.6K per member annually)
Institutional take = €54,000
  R-component = €27,000
  M-component = €13,500
  O-component = €13,500
```

**Operations cost €120K — Year-1 deficit:** -€106.5K — comparable к Conservative; not yet sustainable on cohort revenue alone.

### §3.3 5-year projection (Ruslan-voiced)

| Year | Cohort | Revenue | T (22.5%) | R-comp | M-comp | O-comp | Ops gap | Cumulative gap |
|---|---|---|---|---|---|---|---|---|
| Y1 | 10 | €240K | €54K | €27K | €13.5K | €13.5K | -€106.5K | -€106.5K |
| Y2 | 18 | €432K | €97.2K | €48.6K | €24.3K | €24.3K | -€95.7K | -€202.2K |
| Y3 | 35 | €840K | €189K | €94.5K | €47.25K | €47.25K | -€72.75K | -€274.95K |
| Y4 | 70 | €1.68M | €378K | €189K | €94.5K | €94.5K | -€25.5K | -€300.45K |
| Y5 | 130 | €3.12M | €702K | €351K | €175.5K | €175.5K | **+€55.5K** | -€244.95K |

**Sustainability assessment:** Foundation operations cross break-even в Y5 (€175.5K O-comp vs €120K ops cost); cumulative deficit ~€245K over 5 years — substantially lower than Conservative -€465K.

**Cohort growth model:** with R-comp €27K Y1 / €48.6K Y2 etc., growth multipliers 1.5-2.0× achievable; cohort scales from 10 → 130 by Y5 (vs Conservative 10 → 60).

### §3.4 R12 compliance check (Ruslan-voiced)

- ✅ Reading A (procedural): Charter-stated 20-25%; member acks 77.5% direct
- ✅ Reading B (Mondragón-functional): 22.5% institutional retention vs Mondragón 60% cap = well within
- ✅ Reading C (outcome-based): substrate-delivery threshold moderate; verifiable at substrate-quality-audit Phase
- **Overall: R12-compliant** with paired-frame discipline normal (Reading C key — substrate must deliver value commensurate с extraction)

### §3.5 Ruslan-voiced bottom line

**Pros:** Sustainability achievable в 5 years; balanced reinvestment + operations; matches voice anchor; R12-compliant с moderate discipline
**Cons:** Year 1-4 deficit still requires external supplement (~€275K cumulative through Y4); cohort growth contingent on Phase 1 + Distribution Plan execution quality
**Best fit:** Charter-stated baseline; substrate-delivery + R12 paired-frame discipline ensured; external matching pool 2-3 years; default operational hypothesis

---

## §4 Scenario C — Aggressive (30%)

### §4.1 Setup

- **T = 30%**
- **Risk:** high R-1 (R12 paired-frame slippage risk + perception extraction-heavy at first-touch)
- **R-component:** 15%; M-component: 7.5%; O-component: 7.5%

### §4.2 Year-1 economics

```
Cohort: 10 × €2000 × 12 = €240,000 revenue
Member-direct (D = 70%) = €168,000 (€16.8K per member annually)
Institutional take = €72,000
  R-component = €36,000
  M-component = €18,000
  O-component = €18,000
```

**Operations cost €120K — Year-1 deficit:** -€102K — only marginally better than Conservative.

### §4.3 5-year projection (Aggressive)

| Year | Cohort | Revenue | T (30%) | R-comp | M-comp | O-comp | Ops gap | Cumulative gap |
|---|---|---|---|---|---|---|---|---|
| Y1 | 10 | €240K | €72K | €36K | €18K | €18K | -€102K | -€102K |
| Y2 | 22 | €528K | €158.4K | €79.2K | €39.6K | €39.6K | -€80.4K | -€182.4K |
| Y3 | 50 | €1.2M | €360K | €180K | €90K | €90K | -€30K | -€212.4K |
| Y4 | 110 | €2.64M | €792K | €396K | €198K | €198K | **+€78K** | -€134.4K |
| Y5 | 230 | €5.52M | €1.656M | €828K | €414K | €414K | **+€294K** | +€159.6K |

**Sustainability assessment:** Foundation operations break-even Year 4; **cumulative positive Year 5** at +€160K; aggressive scaling supported via heavy R-component reinvestment.

**Cohort growth model:** with R-comp scaling fast (€36K Y1 → €396K Y4), growth multipliers 2.0-2.5× achievable; cohort 10 → 230 by Y5.

### §4.4 R12 compliance check (Aggressive)

- ⚠️ Reading A (procedural): Charter-stated 30%; member acks 70% direct — operationally compliant if Charter explicit
- ⚠️ Reading B (Mondragón-functional): 30% institutional retention vs Mondragón 60% cap = within range; education-platform-comparable (Coursera 50%) more relaxed
- ⚠️ Reading C (outcome-based): substrate-delivery threshold **HIGH** — must verify member receives substantial indirect value; first-touch perception risk material
- **Overall: R12-compliant IF Charter discipline + strict substrate-delivery + R12 paired-frame in outreach language.** Margin for slippage narrow; ethical-surface review (KA-07 pattern) recommended pre-Phase-1 launch.

### §4.5 Aggressive risks (R-1 + R12 edge)

1. **First-touch perception:** «extraction-heavy» reading при cold outreach if substrate-delivery + reinvestment loop articulation not visible immediately
2. **Mondragón ratio cap implications:** if max-payout / min-payout spread exceeds 5:1 default cap due to large founders-equity-like concentration, programmatic R12 violation Phase 2+ (R12 programmable Option D Hybrid)
3. **Competitive comparison:** Maven 10% — Jetix 30% = 3× extraction premium; perceptual risk if Jetix substrate not 3× superior to standard cohort platform
4. **Audit cadence:** quarterly R12 ethical-surface review needed (vs annual at lower T)

### §4.6 Aggressive bottom line

**Pros:** Fastest sustainability + biggest reinvestment + aggressive scaling capability; cumulative positive Y5; aligned with consulting-style markup industry norm
**Cons:** Strict R12 discipline required; perception risk first-touch; ethical-surface audit needed quarterly; Mondragón ratio cap edge cases possible; narrower margin for slippage
**Best fit:** if Workshop / Hackathon substrate delivers value clearly 3-5× standard cohort platform AND Foundation lineage / network access verifiable + AND if external matching pool less achievable

---

## §5 Scenario D — Piecewise Gradient

### §5.1 Setup

- **Y1 T = 15%** (Conservative; first cohort gentle on-ramp)
- **Y2-Y3 T = 20%** (steady-state; majority cohort phase)
- **Y4-Y5 T = 25%** (scale phase; federation transition)

OR alternative gradient:
- **Y1-Y2 T = 25%** (Foundation-building phase; reinvestment-heavy)
- **Y3-Y4 T = 20%** (steady-state)
- **Y5+ T = 15%** (post-scale federation efficiency; lower extraction sustainable due to volume)

### §5.2 Year-1 economics (variant A: 15% Y1 → 25% Y5)

Year-by-year piecewise:

| Year | T | Cohort | Revenue | T | R-comp | M-comp | O-comp | Ops gap | Cumulative gap |
|---|---|---|---|---|---|---|---|---|---|
| Y1 | 15% | 10 | €240K | €36K | €18K | €9K | €9K | -€111K | -€111K |
| Y2 | 20% | 15 | €360K | €72K | €36K | €18K | €18K | -€102K | -€213K |
| Y3 | 20% | 25 | €600K | €120K | €60K | €30K | €30K | -€90K | -€303K |
| Y4 | 25% | 45 | €1.08M | €270K | €135K | €67.5K | €67.5K | -€52.5K | -€355.5K |
| Y5 | 25% | 80 | €1.92M | €480K | €240K | €120K | €120K | €0K (break-even) | -€355.5K |

**Sustainability assessment:** Y5 break-even on operations; cumulative deficit ~€355K over 5 years; cohort scale 10 → 80 (slower than Aggressive).

### §5.3 Year-1 economics (variant B: 25% Y1 → 15% Y5)

| Year | T | Cohort | Revenue | T | R-comp | M-comp | O-comp | Ops gap | Cumulative gap |
|---|---|---|---|---|---|---|---|---|---|
| Y1 | 25% | 10 | €240K | €60K | €30K | €15K | €15K | -€105K | -€105K |
| Y2 | 25% | 20 | €480K | €120K | €60K | €30K | €30K | -€90K | -€195K |
| Y3 | 20% | 40 | €960K | €192K | €96K | €48K | €48K | -€72K | -€267K |
| Y4 | 20% | 75 | €1.8M | €360K | €180K | €90K | €90K | -€30K | -€297K |
| Y5 | 15% | 140 | €3.36M | €504K | €252K | €126K | €126K | **+€6K** | -€291K |

**Sustainability assessment:** Y5 marginal positive; cumulative deficit ~€291K; cohort scale 10 → 140 (faster than variant A due to higher Y1-Y2 R-comp).

### §5.4 R12 compliance check (Piecewise)

- ✅ Reading A (procedural): if Charter publishes piecewise gradient explicitly at member signup → compliant; if Foundation adjusts post-hoc → violation
- ✅ Reading B (Mondragón-functional): all variants within Mondragón 60% institutional cap
- ✅ Reading C (outcome-based): substrate-delivery threshold scales with T per phase
- **Overall: R12-compliant IF Charter discipline upfront** stating gradient explicitly; opt-out window 30 days at each gradient transition (per Phase 4 §2.5 recommendation)

### §5.5 Piecewise bottom line

**Pros:** Adaptive к phase needs; signals Foundation commitment to lower extraction at scale; matches cooperative federation efficiency expectation; balances first-cohort sustainability с long-term R12-strength
**Cons:** Complex к communicate; member must understand gradient + opt-out rights; not as fast scaling as flat Aggressive; planning + Charter discipline overhead
**Best fit:** if Ruslan wants explicit signal of «Foundation-building Phase 1 → efficiency Phase 4 → lower extraction at scale» trajectory; signals commitment к Mondragón institutional R&D pattern

---

## §6 Sensitivity analysis — R per member variation

If baseline R = €2000 changes к €1500 or €3000, all 4 scenarios shift:

### §6.1 Sensitivity table — Ruslan-voiced (T = 22.5%) Y5 numbers

| R per member | Y5 cohort | Y5 revenue | Y5 T | Y5 O-comp | Y5 Ops gap |
|---|---|---|---|---|---|
| €1500 | 130 | €2.34M | €526.5K | €131.6K | +€11.6K (marginal positive) |
| **€2000 (baseline)** | 130 | €3.12M | €702K | €175.5K | **+€55.5K (positive)** |
| €3000 | 130 | €4.68M | €1.053M | €263.25K | +€143.25K (strong positive) |

**Insight:** Workshop pricing strongly affects sustainability arrival timing. €1500/month — marginal Y5; €3000/month — comfortable Y5.

### §6.2 Sensitivity — Cohort growth multiplier variation

If growth multiplier averages 1.3× annually vs 2.0× baseline:

| Multiplier | Y5 cohort | Y5 revenue | Y5 T (22.5%) | Y5 Ops gap |
|---|---|---|---|---|
| 1.3× | 30 | €720K | €162K | **-€80K** (still deficit) |
| **2.0× (baseline)** | 130 | €3.12M | €702K | +€55.5K |
| 2.5× | 245 | €5.88M | €1.323M | +€210.7K |

**Insight:** Cohort growth dynamics critical; sub-2× multiplier prevents Y5 sustainability в Ruslan-voiced scenario.

### §6.3 Sensitivity — Operations cost variation

If ops cost differs от €120K/year baseline:

| Ops cost | Ruslan-voiced Y5 Ops gap | Aggressive Y5 Ops gap |
|---|---|---|
| €80K | +€95.5K | +€334K |
| **€120K (baseline)** | +€55.5K | +€294K |
| €200K | -€24.5K | +€214K |

**Insight:** Lean operations material для earlier sustainability; €200K ops requires Aggressive-level T to comfortably sustain Y5.

---

## §7 Cross-scenario summary matrix

| Scenario | T | Y5 cohort | Cumulative 5y gap | Sustainability Y5 | R12 discipline level | Speed of scaling |
|---|---|---|---|---|---|---|
| **A Conservative** | 15% | 60 | -€465K | Negative | Low | Slow |
| **B Ruslan-voiced** | 22.5% | 130 | -€245K | Positive | Normal | Medium |
| **C Aggressive** | 30% | 230 | +€160K | Strong positive | Strict | Fast |
| **D Piecewise (15→25%)** | gradient | 80 | -€356K | Break-even | Charter-strict | Slow-Medium |
| **D Piecewise (25→15%)** | gradient | 140 | -€291K | Marginal positive | Charter-strict | Medium-Fast |

---

## §8 Reinvestment loop dynamics — qualitative observations

### §8.1 Loop properties

```
Take rate T → R-component (50% of T per skeleton) → Workshop scaling fund
                                                        ↓
                                                  more cohort members
                                                        ↓
                                                  more revenue (R × cohort)
                                                        ↓
                                                  more R-component compounding
```

**Reinvestment loop is positive-feedback** при growth multiplier > onboarding-cost-per-new-member / R-component-per-existing-member. At base case, this requires:

```
growth_factor > onboarding_cost / R_per_existing_member
            = €5K / R-per-existing-member
```

At T=25% (Ruslan-voiced), R-component = €250 per existing member annually; growth_factor needed = 20 (impossible).
At T=25% with R = €3000/month per member → R per member = €9000 annually × 0.5 R-component / T = €1125 R-comp per member; growth_factor needed = €5K/€1125 = 4.4 (still high).

**Implication:** Reinvestment loop alone insufficient для cohort doubling annually unless onboarding cost reduces substantially (standardisation Phase 3+).

### §8.2 External matching amplifier

Per Optimism RetroPGF analogue (Phase 1 §5):

- If external matching pool ~€100K annually achievable (Anthropic / Foundation grant), loop accelerates: equivalent к doubling R-component
- Strategy: Phase 2 (Year 2-3) actively pursue external matching; reduces Foundation-only reinvestment dependency

### §8.3 Cohort attrition impact

15% annual churn baseline; if churn drops к 5% (substrate-delivery excellent), growth multiplier increases ~10%; if churn rises к 30% (substrate-delivery weak), growth multiplier decreases ~15%.

**Substrate-delivery quality is THE primary lever for cohort retention and reinvestment loop velocity.**

---

## §9 R12 paired-frame language per scenario (preview для Phase 6 memo)

Per Distribution Plan §4.5 pre-send checklist + R12 paired-frame STRICT:

| Scenario | Paired-frame language recommendation |
|---|---|
| **Conservative 15%** | «15% Foundation institutional share + 85% direct cohort distribution + 7.5% Workshop reinvestment loop + 3.75% matching pool + 3.75% operations» — emphasizes member-friendly extraction; needs external funding language |
| **Ruslan-voiced 20-25%** | «20-25% Foundation institutional share funds Workshop scaling + matching pool + operations; cohort retains 75-80% direct; Mondragón-style 50% reinvestment loop» — balanced articulation |
| **Aggressive 30%** | «30% Foundation institutional share — 15% reinvestment loop (Workshop scaling), 7.5% matching pool (community Clan initiatives), 7.5% operations» — must articulate reinvestment loop SUBSTANTIALLY in any first-touch language; demonstrate value delivery |
| **Piecewise (25→15%)** | «25% Year 1-2 Foundation-building → 20% Year 3-4 steady-state → 15% Year 5+ federation scale; Charter-stated gradient; 30-day opt-out at each transition» — explicit trajectory language |

---

## §10 Closure Phase 5

4 scenarios analysed с math model + 5-year projection + R12 compliance check + sensitivity tables (R per member, cohort growth, ops cost). Cross-scenario summary: Conservative R12-strong but sustainability-fragile; Ruslan-voiced 20-25% balanced; Aggressive 30% sustainable+ fast but R12-discipline strict; Piecewise gradient adaptive с Charter discipline.

**Working hypothesis для Phase 6 recommendation:**
- **Default operational hypothesis:** Ruslan-voiced 22.5% midpoint (Scenario B) — balanced sustainability + R12-compliant + matches voice anchor + most-feasible-default
- **Alternative if R12-purity prioritised:** Piecewise 25→15% (Scenario D variant) — explicit gradient signaling cooperative-federation efficiency commitment + opt-out window discipline
- **Alternative if speed prioritised:** Aggressive 30% (Scenario C) — fastest sustainability + scaling but requires strict R12 paired-frame + substrate-delivery + ethical-surface audit cadence
- **NOT recommended:** Conservative 15% — sustainability deficit dependency on external funding too fragile Y1-Y3

**Commit:** `[dr-26] Phase 5 sensitivity scenarios + reinvestment modeling`

---

*Phase 5 closure 2026-05-21. F4 / G: dr-26-phase-5-sensitivity-scenarios / R: refuted_if_math_model_off_by_>30%_OR_R12_compliance_misjudged_OR_assumptions_undeclared.*
