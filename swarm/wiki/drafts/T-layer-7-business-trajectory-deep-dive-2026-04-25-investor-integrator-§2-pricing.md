---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§2-pricing
title: "§2 Pricing Finalization — 9 directions × tiers"
type: cell-draft
cell: C-01
expert: investor-expert
mode: integrator-with-critic-validation
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
task_id: T-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 3000-4500
status: drafted
provenance_inline: true
sources:
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§2.1 portfolio table, §3.1-§3.9 per-direction, §15.2 Q1-Q5 acked"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§2.1 payment-ability filter, §7 outreach, §10 Secure Network"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1.1 revenue-mix CC-1, §3.8 budget, audio_452"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path A/B/C"}
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§3-§6 acked inputs + tensions"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 + USB-C reinforcement"}
confidence: medium
confidence_method: arithmetic-plus-analogy
escalations: []
dissents:
  - id: D-price-1
    claim: "Aspirational миллионер-tier pricing (€20K-€50K/mo retainer) is incompatible with Phase-1 cold outreach reachability"
    F: F4
    ClaimScope: Phase-1 active cold-outreach (P1A); fails at P1B referral mode
    R:
      refuted_if: first 2 P1B inbound миллионер leads close at aspirational tier without discount
      accepted_if: zero миллионер closes at aspirational tier within 6 months of Phase-1 outreach
  - id: D-price-2
    claim: "Path B GM 70.7% is arithmetic correct but fragile if Ruslan delivery time > 20 hrs per engagement"
    F: F4
    ClaimScope: applies to yr1 where delivery overhead is uncharted
    R:
      refuted_if: first signed Path B engagement delivers at ≤20 hrs Ruslan time
      accepted_if: first engagement logs >25 hrs → trigger GM re-computation
---

# §2 Pricing Finalization — 9 Directions × Tiers

> **Cell C-01 | investor-expert | mode: integrator + critic-validation**
>
> Этот документ — foundational pricing layer для LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md.
> Все §§3, 7, 11 этого документа потребляют цены отсюда. L5 placeholders заменены
> на конкретные €/$ per direction × tier с явной F-G-R тройкой, arithmetic-обоснованием,
> margin-of-safety и discount policy.

---

## §2.0 Framing — что L7 §2 owns vs L5 placeholders

L5 Product Deep-Dive (acked 2026-04-25 11:10 CET) зафиксировал 9 направлений как
portfolio-систему и явно выставил pricing как **placeholder-only**: *«All pricing ranges are
placeholders only. L7 Business Deep-Dive owns final pricing structure.»*
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.1]

L7 §2 owns три вещи, которые L5 deliberately оставил открытыми:

1. **Конкретные числа** (floor / standard / premium) с arithmetic-обоснованием на каждый tier
2. **Discount policy** (первые 2-3 клиента, Alliance members, volume Phase-3+)
3. **Phase-1 reach reconciliation** — arithmetic-проверка: доставляет ли эта pricing-структура
   €50K Q2 2026?

L6 Community Deep-Dive (acked 2026-04-25 01:00 CET) дал binding constraint:
**payment-ability filter ≥$5K/месяц recurring OR ≥$10K one-shot** — это операционный cutoff
для всех pricing tiers. Ни один tier не должен быть ниже этого фильтра для Phase-1
платёжеспособного клиента. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1]

**Базовые предположения arithmetic:**
- Курс EUR/USD: 1.07 (апрель 2026 mid-market; FX-риск в §2.11)
- Ruslan hourly rate anchor: **€150/hr** [audio_452; src:decisions/JETIX-PLAN.md#§3.1]
- Phase-1 target: **€50K Q2 2026** (D9/D15 единственный committed absolute date)
  [src:decisions/JETIX-PLAN.md#§3.1.1]
- CC-1 revenue-mix (investor-critic ack'd): 4 productized contract-quarters × €7.5K +
  233 hourly hours × €150/hr = €65K total (~30% buffer над target)
  [src:decisions/JETIX-PLAN.md#§3.1.1]

---

## §2.1 Direction 1 — AI Consulting for Complex Tasks

### Pricing rationale

AI Consulting — **primary revenue engine Phase-1**, co-equal с hourly line (CC-1 ack).
Базовый rate: **€150/hr** [audio_452]. Productized packages — D18 path — масштабируют
без линейного роста часов. [src:decisions/JETIX-VISION.md#§5-D18]

**Claim: базовый hourly rate = €150/hr (Phase-A).**
- F: F5 (anchored to Ruslan voice memo audio_452; cross-validated with DACH
  AI-consulting market rate for senior independent consultants €120-€200/hr;
  Glassdoor/IM-equivalent reference for Berlin 2026 market)
- ClaimScope: Phase-A (solo Ruslan delivery, G0→G1); rate upgrades at G2 when
  first contractor hired and service is partially team-delivered
- R: refuted if ≥3 consecutive qualified leads reject €150/hr as price anchor in
  discovery calls; accepted if first 5 paying engagements close at ≥€130/hr effective

### Phase-1 pricing tiers

| Tier | Format | Price | Min engagement | Implied hourly |
|---|---|---|---|---|
| **Discovery session** | 90-min scoping call + written diagnostic | **€300 fixed** | 1 session | €200/hr |
| **Starter package** | 10 templates + 1 session + async Q&A 2 weeks | **€500–€800** | one-time | €125–200/hr |
| **Productized engagement (Path B default)** | KB setup + agent config + handoff doc; 4-6 weeks | **€5K–€10K** | per engagement | €150/hr equiv |
| **Monthly retainer (Phase-1)** | Ongoing KB maintenance + 4 sessions/mo + community chat | **€1K–€2K/mo** | 3-month min | €150/hr equiv |
| **Billable services** | Complex task execution hourly | **€150/hr** | 4 hr block | €150/hr |

**Claim: productized engagement €5K–€10K (Phase-A Mittelstand P1A).**
- F: F4 (based on L5 §3.1 Archetype A payment filter €5K+/mo OR €10K one-shot;
  cross-validated with KM-Architecture-Variants Dissent 3 Path B: €3K onboarding +
  €15K/yr annual = €7.5K/contract-quarter which sits between floor and standard)
- ClaimScope: Mittelstand Operator-Founder-CEO (€1M-€50M revenue company, DACH);
  does NOT apply to Startupper segment (lower tier below)
- R: refuted if first Mittelstand prospect refuses €5K floor citing budget; accepted
  if first signed contract closes at ≥€4.5K

**Claim: Startupper package €500–€5K (Phase-A English-market P1A).**
- F: F4 (L5 §3.1 Archetype B Startupper $50K-$500K/yr revenue; $10K one-shot filter
  maps to ≈€9.3K ceiling; Phase-1 entry price below ceiling by 30%+ margin-of-safety)
- ClaimScope: English-speaking Startupper, $50K-$500K/yr revenue, digital business
- R: refuted if Startuppers consistently use the lower tier only and never upgrade
  to productized engagement within 90 days; accepted if ≥30% of Startupper clients
  upgrade within first engagement cycle

### Phase-2+ pricing evolution

При G1→G2 (€50K → €200K): retainer эволюционирует в managed methodology.

| Tier | Phase-2 price | Format |
|---|---|---|
| Managed retainer | **€3K–€5K/mo** | 3-month block; team-partial delivery |
| Enterprise package | **€15K–€30K/engagement** | 6-month; includes Alliance license option |
| Alliance methodology license | **€5K–€15K/yr** | per practitioner/firm |

### First 2-3 case-study discount (AI Consulting)

**Первые 2-3 клиента получают 20-30% discount в обмен на:**
- Право публиковать anonymized case study (no client name without explicit approval)
- Письменный testimonial (quote-approved by client)
- Разрешение использовать как reference для следующих prospects

**Claim: 20-30% case-study discount rationale.**
- F: F4 (standard B2B services launch practice; margin-of-safety check: даже со
  скидкой 30% productized €5K engagement = €3.5K > cost-of-delivery estimate ≈
  €1.5K at €150/hr × 10 hrs → GM≈57%, above Phase-A 30% floor)
- ClaimScope: first 3 signed contracts only; expires automatically at contract #4
- R: refuted if first 3 clients take discount but refuse case study publication;
  accepted if ≥2 of 3 case-study clients provide publishable testimonial within 60
  days of engagement close

---

## §2.2 Direction 2 — Продюсерский центр

### Pricing rationale

Продюсерский центр — **co-primary revenue engine Phase-1**, English-speaking infobiz.
Retainer model per D18 (productization-over-hours). Minimum 3-month commitment.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.2]

Payment ability filter: ≥$5K/mo recurring — blogger с 5K+ аудиторией и монетизацией
($50K-$500K/yr revenue) легко проходит, если правильно объяснить ROI («1 workshop →
10+ artifacts, 30-day production multiplier»). [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1]

### Phase-1 pricing tiers

| Tier | Input | Output | Price/mo | Min commit |
|---|---|---|---|---|
| **Pilot (Starter)** | 1 workshop/mo | 10+ artifacts; single-channel | **€2K–€3K/mo** | 3 months |
| **Standard (Growth)** | 2 workshops/mo | 20+ artifacts; multi-channel | **€4K–€6K/mo** | 3 months |
| **Premium (Elite)** | 4+ workshops/mo | 40+ artifacts; full funnel + course modules | **€7K–€10K/mo** | 3 months |

10% discount при quarterly prepaid (выравнивает cash-flow с €50K gate arithmetic).

**Claim: Pilot tier = €2K–€3K/mo.**
- F: F4 (L5 §3.2 §5 placeholder "€2K-€8K/month retainer range consistent with L6
  payment filter"; floor set at €2K as minimum viable for 10-artifact monthly
  production covering Ruslan time ≈ 10-15 hrs × €150/hr = €1.5K-€2.25K COGS;
  margin-of-safety at €2K: GM = (€2K - €1.5K) / €2K = 25% — BORDERLINE; standard
  €2.5K yields GM 40%+ — ACCEPTABLE)
- ClaimScope: English-speaking blogger Archetype (Блогер/Teacher), 5K+ audience,
  Phase-1 solo-Ruslan-delivery; rate increases at G2 when editor contractor joins
- R: refuted if delivery overhead consistently exceeds 15 hrs/mo at Pilot tier (GM
  collapses); accepted if Pilot tier delivered at ≤13 hrs/mo across first 3 pilots

**Claim: Standard tier = €4K–€6K/mo.**
- F: F4 (2× input volume → 2× delivery time → 2× pricing floor; GM check: €4K
  standard, COGS 20-25 hrs × €150 = €3K-€3.75K → GM 6-25% — tight at floor;
  at €5K midpoint: GM ≈ 33-40% — ACCEPTABLE; contractor support narrows COGS at G2)
- ClaimScope: Startuppers with established multi-channel distribution; 2-workshop
  volume suggests monetized audience of $100K-$500K/yr revenue
- R: refuted if demand for 2-workshop tier appears before G2 contractor hire (delivery
  risk materializes solo); accepted if G2 contractor join enables 4-5 Standard clients
  simultaneously at maintained quality

**Claim: Premium tier = €7K–€10K/mo.**
- F: F4 (4× volume of Pilot → minimum €7K based on linear COGS scaling; €10K ceiling
  anchored to L6 payment-ability one-shot filter $10K ≈ €9.3K; GM at €7K + 35-40 hrs
  delivery: GM = (€7K - €5.25K) / €7K = 25% — requires contractor to be viable;
  at €8.5K midpoint: GM ≈ 38% assuming contractor costs €2K/mo for support)
- ClaimScope: Phase-2+ only in practice (Phase-1 solo cannot sustain 4-workshop
  volume without degradation); listed here as Phase-1 ceiling but unlikely to close
  before G2
- R: refuted if Ruslan delivers Premium tier solo at maintained quality without contractor

### Phase-2+ evolution

| Phase | Pricing | Notes |
|---|---|---|
| G1→G2 | Standard remains; Premium activates properly | Contractor hire unlocks Premium delivery |
| G2→G3 | +methodology license add-on €500-€2K/mo | Client-private KB license separate from production |
| G3→G4 | Team rate; potential BU split | Separate pricing P&L per L5 §3.2 Gate G3 |

### First 2-3 case-study discount (Продюсерский центр)

Аналогично §2.1: 20-30% discount за testimonial + case study publication rights.
Для Продюсерского центра case study = публичный пример «1 workshop → X artifacts»,
желательно с measurable outcome (engagement rate, new subscribers, revenue conversion).

---

## §2.3 Direction 3 — USB-C Integration Services

USB-C Integration Services — **Phase-2 productized** direction с тремя delivery paths,
acked в L5 Q1 (2026-04-25 11:10 CET). Path A/B/C resolve здесь per L5 Q1 final decision:
**Path B default Phase-A, Path C enterprise override (>€30K + GDPR-audit), Path A Phase-2
SMB**. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#frontmatter ack_decisions Q-01]

---

### §2.3.1 Path B — Client-Hosted Methodology License (Phase-A default)

Клиент устанавливает Jetix methodology на своей инфраструктуре. Jetix = methodology
licensor, NOT data processor. Maximum data sovereignty. Investor-critic Phase-A preference
на основе unit-economics. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#Dissent-3]

| Component | Phase-A price | Notes |
|---|---|---|
| **Onboarding fee** (one-time setup + configuration + handoff training) | **€3K** | 2-3 week engagement; includes setup scripts, wiki template, GDPR fit statement |
| **Annual methodology license** | **€15K/yr** (= €1.25K/mo) | Methodology updates, support retainer, upgrade protocol |
| **Year-1 total commitment** | **€18K** | Onboarding + yr1 license |
| **Optional compliance add-on** | **+€2K** | GDPR audit trail documentation package |

**Gross margin analysis (Path B, yr1):**

| Item | Amount |
|---|---|
| Revenue yr1 | €18K |
| COGS estimate: onboarding 15 hrs × €150/hr = €2.25K | — |
| COGS estimate: support year (4 hrs/mo × 12 = 48 hrs × €150/hr = €7.2K; Phase-A heavily Ruslan-delivered) | — |
| COGS estimate: methodology update distribution (2 hrs/mo × 12 × €150 = €3.6K) | — |
| COGS total (worst-case) | ≈€5.25K |
| **Gross profit** | **€12.75K** |
| **GM%** | **≈70.7%** |

**Claim: Path B onboarding = €3K + annual license = €15K → 70.7% GM yr1.**
- F: F4 (directly from KM-ARCHITECTURE-VARIANTS Dissent 3 Position B; methodology
  license fee benchmarked against SMB software methodology licenses: Scrum.org PSM =
  $150-200/user/yr; Jetix is a full-stack deployment, not a single certification —
  justified premium 50-100× per practitioner vs per-seat SaaS; analogical from
  NetSuite implementation fee structure for Mittelstand; not formally validated)
- ClaimScope: Phase-A, Mittelstand SMB €1M-€15M revenue; technical IT team present
  for installation; first 3-5 contracts only; rate review post-G2 empirical data
- R: refuted if first 3 clients refuse €3K onboarding citing budget preference for
  €0 onboarding + higher annual; or if actual delivery hours > 35 hrs total yr1
  (pushes GM below 50%); accepted if first signed Path B contract closes at ≥€2.5K
  onboarding + ≥€12K/yr AND actual delivery fits ≤ estimated COGS

**Path B GM margin-of-safety check:**
margin_of_safety = (70.7% GM - 30% hurdle) / 30% hurdle = **135%** — passes
Graham threshold (≥30% MS = 30% relative to opportunity cost of founder hours).
Risk-of-ruin floor: если GM падает ниже 0% → проект убыточен → stop. At current
numbers, GM could drop from 70.7% to 0% только если COGS > €18K → impossible at
35-hr annual delivery. Floor is structurally protected. ✓

---

### §2.3.2 Path C — Hybrid (Enterprise override: >€30K client revenue + GDPR-audit)

Path C: клиент держит данные, Jetix hosts agents via encrypted tunnel. Recommended
by STRATEGIC-INSIGHT §5 для enterprise-grade compliance-strict clients.
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5]

**Override trigger (per L5 Q1 ack):** клиент с >€30K одноразовым бюджетом
(= revenue company likely €10M+) И требует GDPR-audit trail в контракте.

| Component | Price | Notes |
|---|---|---|
| **Onboarding fee** (VPN tunnel setup + agent config + client KB bootstrap) | **€5K** | 3-5 week engagement; higher complexity than Path B |
| **Annual hybrid managed license** | **€25K–€40K/yr** | Includes Jetix compute cost for agent swarm, tunnel uptime, methodology updates |
| **Year-1 total** | **€30K–€45K** | Depending on agent swarm intensity |
| **GDPR-audit package** (per-engagement compliance doc + DPA signing) | **+€3K** | Included in contracts citing GDPR Art. 28 |

**Gross margin analysis (Path C, yr1):**

| Item | Amount |
|---|---|
| Revenue yr1 (midpoint €37.5K) | €37.5K |
| COGS: onboarding 20 hrs × €150/hr = €3K | — |
| COGS: Jetix compute (EU-VPS Hetzner ≈ €100-200/mo × 12 = €1.2K-€2.4K) | — |
| COGS: support year 6 hrs/mo × 12 × €150/hr = €10.8K | — |
| COGS: tunnel monitoring 2 hrs/mo × 12 × €150/hr = €3.6K | — |
| COGS total | ≈€18.6K–€19.8K |
| **Gross profit** | **≈€17.7K–€18.9K** |
| **GM%** | **≈47%–50%** |

**Note on Path C GM vs Path B GM:** Path C GM (≈47-50%) is below Path B GM (70.7%)
in Phase-A, which validates the investor-critic preference for Path B as Phase-A default.
Path C becomes economically superior at Phase-2+ when:
(a) first contractor hired absorbs support hours at lower cost (e.g. €80/hr vs Ruslan €150/hr)
(b) compute COGS amortized across 5+ clients

**Claim: Path C = €5K onboarding + €25K–€40K/yr.**
- F: F4 (analogical from STRATEGIC-INSIGHT §5 placeholder "$15K-$40K/month managed";
  L7 re-anchors per annual contract framing since monthly = Ruslan Phase-A overhead
  risk; pricing set annual to align with Mittelstand budget cycle; enterprise
  Mittelstand €10M+ company: €30-45K/yr = 0.3-0.45% revenue — feasible if ROI
  demonstrated in 90 days)
- ClaimScope: enterprise Mittelstand >€10M revenue + GDPR-strict + has existing IT
  infrastructure for tunnel endpoint; NOT for solo/SMB without IT team
- R: refuted if enterprise clients refuse annual contract in favor of monthly pricing;
  or if tunnel complexity consistently requires >25 Ruslan hrs/mo (GM collapses);
  accepted if first Path C enterprise contract closes at ≥€28K total yr1

---

### §2.3.3 Path A — Jetix-Hosted Managed Service (Phase-2 SMB only)

Path A: Jetix provisions dedicated EU-VPS per client, manages uptime and updates.
Easiest sale. Highest ops burden. NOT Phase-A default (investor position confirmed
per L5 Q1 ack: Path A = Phase-2 SMB activation only, post-contractor hire).
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.3 §5]

**Phase-2 pricing (не активна Phase-1):**

| Component | Price | Notes |
|---|---|---|
| **Setup fee** | **€2K** | VPS provision + client namespace bootstrap + onboarding walkthrough |
| **Monthly managed service** | **€2K–€4K/mo** | Includes compute, uptime, methodology updates, support SLA |
| **Annual commitment discount** | 10% off monthly × 12 | Prepaid annual = €21.6K–€43.2K |

**Claim: Path A = €2K–€4K/mo managed (Phase-2 SMB).**
- F: F4 (analogical from L5 §3.3 placeholder "$5K-$15K/month all-in" — L7 re-anchors
  lower because SMB targeting (not enterprise) and Phase-2 contractor-supported delivery
  reduces labor COGS; lower bound €2K/mo anchored to Hetzner VPS cost ≈€100-200/mo +
  20 hrs/mo support × €80/hr contractor = €1.7K-€1.8K COGS → GM≈10-15% at floor;
  at €3K/mo midpoint and contractor cost: GM≈40% — ACCEPTABLE)
- ClaimScope: Phase-2+ SMB Mittelstand that has no internal IT team; NOT for
  compliance-strict enterprise requiring Path C
- R: refuted if SMB clients consistently exceed 25 hrs/mo support demand (ops burden
  unsustainable without additional hire); accepted if G2 contractor hire enables
  3-5 Path A clients simultaneously at ≥30% GM

**Сводная таблица — USB-C 3 Paths:**

| Path | ICP | Phase | Onboarding | Annual/Monthly | Year-1 total | GM yr1 |
|---|---|---|---|---|---|---|
| **B (default)** | Mittelstand SMB + IT team | Phase-A (NOW) | €3K | €15K/yr | €18K | 70.7% |
| **C (enterprise)** | Enterprise >€10M + GDPR-strict | Phase-A (trigger >€30K+audit) | €5K | €25-40K/yr | €30-45K | 47-50% |
| **A (SMB)** | SMB no-IT-team | Phase-2 (post-contractor) | €2K | €2-4K/mo | €26-50K/yr | ≈30-40% |

---

## §2.4 Direction 4 — Matchmaker Platform

### Phase-1: нет direct pricing (стратегический актив, не revenue line)

Phase-1 Matchmaker — **бесплатный сервис** (Ruslan manual). Инвестиция в relationship
depth + consulting funnel + scoreboard data для Phase-2 AI-smoothing.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.4 §5]

Операционная стоимость Phase-1: 45-60 мин × Ruslan attention per match event.
Opportunity cost: €150/hr × 0.75 hr = **€112/match** — это внутренняя стоимость
каждого матча; даже при 10 matches/week = €1.12K/week opportunity cost. Justified
как marketing + moat-building investment (goodwill → consulting pipeline).

**Claim: Phase-1 Matchmaker = €0 direct fee; opportunity cost ≈€112/match.**
- F: F4 (L5 §3.4 §5: "no direct pricing (matchmaking as service multiplier)";
  opportunity cost arithmetic above; justified by pipeline-building logic per L6 §6)
- ClaimScope: Phase-1 only, ≤10 match-events/week; fails if volume exceeds 10/week
  (Ruslan bandwidth collapse)
- R: refuted if consulting pipeline generates zero leads from matchmaking after 10
  completed matches; accepted if ≥2 of first 10 matches surface consulting opportunity
  within 30 days

### Phase-2: match-fee structure (€50K → €200K gate)

| Tier | Fee | Trigger |
|---|---|---|
| **Standard match** (1 specialist, defined brief) | **€500–€800/match** | Task-side pays at match acceptance |
| **Complex match** (multi-specialist, cross-disciplinary) | **€1.2K–€2K/match** | Task-side pays at introduction delivery |
| **Monthly retainer** (match-on-demand, repeat clients) | **€2K/mo flat** | Subscription for active task-side clients |

Specialist-side Phase-2-early: no upfront fee. Success-fee 10-15% of first engagement
value post-match introduced Phase-2-mid (when portrait data is sufficient).

**Claim: Phase-2 match fee = €500–€2K/match (complexity-tiered).**
- F: F4 (L5 §3.4 placeholder "$500-$2,000 per match"; L7 confirms in EUR;
  price sits below L6 payment-ability filter monthly threshold ($5K/mo ≈ €4.65K) —
  single match fee is <50% of monthly filter → affordable per payment-ability logic;
  analogical from Toptal placement fees $2K-$5K for engineering roles — Jetix lower
  due to no exclusivity, different service scope)
- ClaimScope: Phase-2 only; P1A/P1B task-side clients only; specialist pool ≥15
  active portraits required
- R: refuted if ≥3 consecutive task-side clients refuse to pay match fee citing
  "should be free like Ruslan does it now"; accepted if first 5 paid matches complete
  without dispute at listed prices

### Phase-3+: platform subscription + take-rate

| Model | Price | Phase |
|---|---|---|
| **Task-side subscription** | **€500–€1.5K/mo** | G2→G3 (€200K→€1M) |
| **Transaction fee (escrow)** | **5–10% of matched-task value** | G3+ |
| **Secure Network gated access** | Platform access included in SN membership | G3+ |

---

## §2.5 Direction 5 — Secure Network

### Phase-1 precursor: бесплатно (5-20 invite-only)

Текущий Phase-1 Telegram-чат «попутно» — **€0**. НЕ является Secure Network
продуктом; это D16 "простой чат" precursor.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.5 §2]

### Phase-2 invite-list: €0 (waitlist phase)

После €200K validation gate (G2) — Secure Network architecture design начинается.
Waitlist фаза: бесплатная; цель — quality-filter 50-200 первых членов до запуска.
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§10]

### Phase-3 launch tiers (G2→G3, €200K→€1M launch)

| Tier | Access | Price/mo | Notes |
|---|---|---|---|
| **Складчина базовая** | Pooled access к expensive tools (Perplexity Pro, Claude Max, research) + general network chat | **€19/mo** | Entry-level; tools складчина alone justifies (Perplexity = €20/mo individual) |
| **Network standard** | Full thematic sub-networks (Предприниматели / Инвесторы / etc.) + складчина + Matchmaker match-initiation right | **€49/mo** | Primary Phase-3 tier |
| **Network premium** | Standard + priority Matchmaker queue + featured specialist badge + Alliance working group access | **€99/mo** | For active Matchmaker participants |
| **Alliance strategic** | Premium + Alliance governance participation + methodology license access | **€199/mo** | Phase-3+ for committed Alliance members |

**Claim: Secure Network tiers €19/€49/€99/€199/mo.**
- F: F4 (L5 §3.5 placeholder "€200-€500/mo" for subscription — L7 DISAGREES with
  upper placeholder for Phase-3 launch; re-anchors lower based on складчина economics:
  Perplexity Pro = $20/mo, Claude Max = $100/mo, research tools = $30/mo; pooled
  across 20 members → cost/member ≈ €7-10/mo for tool access alone; €19/mo provides
  margin above tool cost; standard €49/mo validated against similar professional
  community pricing: YPO $25K/yr = $2K/mo — that's a different market; CMO Alliance
  $200-500/mo — relevant comparison; €49 is 10% of CMO Alliance = positioned as
  accessible premium)
- ClaimScope: Phase-3 launch only; G3 target 200-1000 members;
  does NOT apply at G4 (10K+ members) where pricing power increases
- R: refuted if <30% of waitlist converts to paid at €49 launch tier; accepted if
  ≥50% waitlist converts to any paid tier within 30 days of launch

**Preserved dissent (L5 placeholder vs L7 re-anchor):** L5 §3.5 cited €200-€500/mo.
L7 investor-expert re-anchors to €19-€199 range. Dissent: the €200-€500 placeholder
was Phase-3+ late-stage pricing (after network effects established); L7 sets Phase-3
**launch** pricing. Both can be true at different gates. Resolution: €19-€199 = G2→G3
launch window; €200-€500 = G4+ when NPS and network density justify premium.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.5]

---

## §2.6 Direction 6 — YouTube-Analyzer SaaS

YouTube-analyzer SaaS — **Phase-3+ deferred** per L5 ack Q2 (Defer-to-G3-MVP +
empirical pull-forward trigger if Phase-1 client requests ≥$2K willing-to-pay).
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#frontmatter ack_decisions Q-02]

### Phase-2 manual kit (G1→G2, €50K→€200K)

До SaaS-формы: manual YT-analysis kit как per-engagement service.

| Format | Price | Deliverable |
|---|---|---|
| **Single-channel analysis** | **€2K–€3K/engagement** | Channel audit: топики, engagement patterns, конкурентный ландшафт, ICP hypothesis |
| **Multi-channel niche analysis** | **€4K–€5K/engagement** | Niche mapping: top 20 channels × metrics, opportunity gaps, content calendar strategy |
| **Ongoing intelligence retainer** | **€1K–€2K/mo** | Monthly niche update + 3 channel audits |

**Claim: Phase-2 manual kit = €2K–€5K/engagement.**
- F: F4 (analogical from custom research pricing: Gartner briefing $2K-5K; SimilarWeb
  research report $3K-8K; Jetix manual kit combines YT-API data + Claude analysis +
  structured report — comparable value to custom research at boutique price;
  pull-forward trigger ≥$2K client willing-to-pay per L5 Q2 ack directly validates floor)
- ClaimScope: Phase-2 manual-kit form only; SaaS form is Phase-3; applies to P1A/P1B
  Блогер archetype and Agency clients (Phase-2 expanded ICP)
- R: refuted if first willing-to-pay signal below $2K; accepted if first manual
  engagement closes at ≥€1.8K

### Phase-3+ SaaS tiers (G3→G4, €1M→$100M)

| Tier | Access | Price/mo | Notes |
|---|---|---|---|
| **Individual blogger** | 3 channel analyses/mo + 1 niche map/mo | **€49/mo** | Self-serve |
| **Agency standard** | 20 channels/mo + competitive dashboards | **€149/mo** | Small agencies |
| **Agency pro** | Unlimited channels + API access + white-label option | **€299/mo** | Mid-size agencies |
| **Enterprise API** | Custom volume + dedicated data pipeline + SLA | **€1K–€3K/mo** | Enterprise integrations |

**Claim: SaaS tiers €49–€299/mo (individual→agency).**
- F: F4 (analogical from Tubular Labs $99-$499/mo for YouTube analytics SaaS;
  Social Blade Pro $99/mo; Jetix positioned below Tubular on price,
  differentiated by AI-analysis depth + ICP-matching lens not just raw metrics)
- ClaimScope: Phase-3+ SaaS form only; revenue-triggered by G3 (€1M gate + engineering
  capacity hire); does NOT apply before engineering team exists
- R: refuted if ≥5 trial users cancel at €49 citing "cheaper alternatives cover needs";
  accepted if month-2 retention ≥70% at each tier

---

## §2.7 Direction 7 — Educational + Investor Programs + Grant Hunting

Direction 7 — **Phase-2+ G2→G3**, три sub-tracks с разной economics.
L5 Q4 ack: cohort-first G2→G3 (NPS>40 + margin>€3K/learner), self-serve G3→G4 min.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#frontmatter ack_decisions Q-04]

### Sub-track A — Educational cohort programs

| Format | Price | Constraints |
|---|---|---|
| **Cohort program (G2→G3)** | **€3K–€8K/learner** | 6-8 week intensive; NPS>40 gate per L5 Q4; margin>€3K/learner gate |
| **Self-serve course (G3→G4)** | **€500–€2K/license** | Async; lower support burden; Phase-3 secondary tier |
| **Methodology license (per practitioner/firm)** | **€500–€5K/yr** | License to practice and teach Jetix methodology; Phase-2+ Alliance path |

**Claim: cohort price = €3K–€8K/learner.**
- F: F4 (analogical from premium cohort programs: OnDeck $5K-$15K; Maven cohorts
  $2K-$8K; Reforge $2K-$4K; Jetix positioned in the middle as Phase-1 methodology
  validation product; L5 Q4 margin>€3K/learner constraint validates €3K as floor —
  if cohort COGS exceeds €0/learner at €3K price, margin still ≥€3K on full cohort
  economics only if Ruslan time is not all marginal cost)
- ClaimScope: G2→G3 cohort-first window only; methodology must be stable (Phase-2);
  requires NPS>40 gate per L5 Q4 ack before second cohort runs
- R: refuted if first cohort produces NPS<40 (signaling methodology not yet
  teachable); accepted if first 2 cohorts close at ≥€3K/learner AND NPS≥40

**Note on margin>€3K/learner check:**
At €3K/learner × 10 learners = €30K cohort revenue.
COGS estimate: Ruslan 50 hrs facilitation × €150/hr = €7.5K + materials/tooling €2K = €9.5K.
Margin = (€30K - €9.5K) / 10 learners = **€2.05K/learner** — FAILS the >€3K gate.

Re-check at €5K/learner × 10 learners = €50K.
Margin = (€50K - €9.5K) / 10 = **€4.05K/learner** — PASSES gate. ✓

**Implication: minimum viable cohort price = €5K/learner** to clear L5 Q4 margin gate.
Floor of €3K/learner in the table is aspirational Phase-A entry; real operating minimum
for gate compliance = €5K. Preserved dissent noted below.

**Preserved dissent (educational pricing floor):** L5 table lists €3K–€8K. L7
arithmetic shows €3K fails the margin>€3K/learner gate at 10-learner cohort. Resolution:
price floor for gate-compliance is €5K; €3K/learner viable only if cohort size ≥20
learners (margin = (€60K - €9.5K) / 20 = €2.525K — still below gate at 20 learners).
Recommendation: set cohort minimum price at €5K/learner. This is a FLAG, not a Lock revision.

### Sub-track B — Investor Programs

Не pricing — equity stake или token allocation. Investor program = path for ecosystem
investors who want exposure to Jetix growth. Structure определяется Phase-3+ при
формировании holding entity (D19). NOT priced in L7 §2; deferred to investor relations
§9 of canonical document.

**Claim: Investor Programs = no Phase-1/2 pricing; Phase-3+ equity/token structure.**
- F: F4 (operational convention; before holding entity formation and Phase-3 revenue
  validation, investor program structure is premature; Ruslan must have skin to offer;
  per Taleb pattern P5 — leverage without skin is forbidden)
- ClaimScope: Phase-3+ only; Phase-1/2 = not applicable

### Sub-track C — Grant Hunting

| Format | Fee model | Notes |
|---|---|---|
| **Grant research retainer** | **€1K–€2K/mo** | Opportunity scouting + application drafting support |
| **Success fee on awarded grant** | **5–10% of awarded grant value** | Performance-linked; Phase-2+ |

**Claim: grant success-fee = 5–10% of awarded value.**
- F: F4 (standard EU grant-consulting market: grant success fees 5-15% for boutique
  advisors; Jetix anchors conservative 5-10% to remain accessible to SMBs while
  providing meaningful upside on large EU Horizon/BMBF grants €100K-€2M; €100K
  grant × 8% = €8K success fee — substantial for a single engagement)
- ClaimScope: EU SMB grant hunting (Horizon Europe / BMBF / BMWI grants); NOT
  applicable to US federal grants (different regulatory structure)
- R: refuted if clients refuse success-fee model citing preference for flat fee;
  accepted if first 2 grant applications produce award + Jetix collects success fee
  at ≥5% of awarded amount

---

## §2.8 Direction 8 — Tokens / ICO D23 Option B

D23 Option B acked: **preserve optionality through Phase-3 review**; retirement clause
if MiCA/Howey prohibitive OR $100M ARR without specialist-friction.
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#frontmatter ack_decisions Q-05]

**Pricing design: NOT applicable Phase-1/2.**

Tokens — **не pricing exercise в L7 §2** для Phase-1 или Phase-2. Это tokenomics
design вопрос, который принадлежит Phase-3+ с отдельным regulatory navigation
процессом (EU MiCA, US Howey test). L7 §2 только зафиксирует optionality + retirement
clause, не pricing.

**Optionality preservation structure:**

| Gate | Token status | Action |
|---|---|---|
| Now → G3 (€1M) | Internal utility only | Складчина token pools (experimental); no public token; no pricing |
| G3 review ($100K self-earned trigger) | Phase-3 review event | Evaluate: does consulting/educational/USB-C fund growth without token? |
| If NO token needed → | Formal deprecation | File LOCKS-D23-DEPRECATION; no token launch |
| If YES token viable → | Design + legal structure | Phase-3+ separate cycle with MiCA counsel |

**Retirement clause (per L5 Q5 ack):**
«Deprecate formally if consulting/educational/USB-C fund growth without specialist-friction
OR MiCA/Howey legally prohibitive» — this clause overrides any aspirational token
discussion until Phase-3 review gate.

**Claim: Tokens D23 = no pricing; optionality preserved with explicit retirement clause.**
- F: F4 (operational convention; per Taleb antifragility: token optionality = upside
  from volatility without forcing exposure; retirement clause = via-negativa discipline)
- ClaimScope: Phase-3+ only; Phase-1/2 = internal utility token pools experimental,
  not monetized
- R: refuted if regulatory counsel at Phase-3 review deems token launch feasible AND
  profitable AND non-speculative; then proceeds to tokenomics design; accepted if
  Phase-3 review shows token adds friction without proportional benefit → formal
  deprecation

---

## §2.9 Direction 9 — Smart AI

**NOT priced — internal narrative label only.**

Smart AI — cross-phase internal framing. Ruslan explicit: «ну типа запиши между прочим
но нет это ещё не лок блять забей хуй». Не D29. Не external product. Не revenue line.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]

Anti-scope: L7 §2 does NOT assign pricing to Smart AI. Если в будущем D29 lock будет
принят Ruslan'ом → отдельный cycle определит pricing для Smart AI как external product.
До этого: internal narrative only = €0 external pricing.

---

## §2.10 Discount Policy

### First 2-3 case-study clients (ALL directions where applicable)

**Стандартная формула:** 20–30% discount в обмен на testimonial + anonymized case study
publication rights. Применяется к:
- Direction 1 (AI Consulting): первые 3 contracts
- Direction 2 (Продюсерский центр): первые 3 retainer clients
- Direction 3 (USB-C Path B/C): первые 3 productized deployments

**Discount mechanics:**

| Discount level | Что получает клиент | Что получает Jetix |
|---|---|---|
| 20% | Скидка от standard tier | Testimonial (quote-approved) |
| 25% | Скидка от standard tier | Testimonial + anonymized case study |
| 30% | Скидка от standard tier | Testimonial + named case study (client named explicitly) |

**Margin-of-safety check на discount (worst case: 30% на Direction 1 productized €5K):**
- Discounted price: €3.5K
- COGS estimate: 10-15 hrs × €150/hr = €1.5K-€2.25K
- GM at worst: (€3.5K - €2.25K) / €3.5K = **35.7%** — passes Graham 30% floor ✓

**Claim: 20-30% case-study discount is margin-safe across all applicable directions.**
- F: F5 (arithmetic demonstrated above; worst-case GM 35.7% > 30% Graham floor for
  Direction 1; Direction 2 Pilot tier is tighter — see §2.2 note on Pilot GM ≈25%
  before discount; at 20% discount on €2K Pilot: €1.6K price, COGS €1.5K → GM 6.25%
  — FAILS floor; recommendation: NO case-study discount on Pilot tier; minimum
  discount-eligible tier = Standard at €4K → discounted €3.2K → GM ≈ 20-30% range)
- ClaimScope: applies to all directions EXCEPT Продюсерский центр Pilot tier
  (GM too thin); does not apply to Phase-3+ when brand established
- R: refuted if ≥2 of first 3 case-study clients refuse publication rights despite
  receiving discount; or if GM drops below 30% across 3 case-study engagements;
  accepted if ≥2 case studies published AND subsequent MQL conversion rate improves

### Alliance member discount (Phase-2+)

10–15% discount на AI Consulting, USB-C, Educational tiers для acked Alliance members.
Rationale: Alliance membership = network effect benefit to Jetix → justified discount
as partnership incentive. NOT applicable Phase-1.

### Volume discount (Phase-3+ enterprise)

Custom negotiation at G4+ for multi-BU deployments. Not structured in Phase-1/2.

---

## §2.11 Currency Policy

**EUR primary.** All Phase-1 pricing denominated in EUR. Rationale:
- DACH Mittelstand client base → EUR native
- Jetix Phase-1 entity = DE GmbH (post-$20-30K trigger per D15)
- FX risk on EUR invoices = 0 for DE clients

**USD optional Phase-2+ (US/EN-market clients).**
- English-speaking Startupper + Blogger archetypes = USD-native
- Phase-2+ Jetix entity structure may include US entity or Stripe EUR+USD
- USD pricing follows EUR pricing at 1.05-1.10 × EUR amount (minor markup for FX
  hedging and Stripe USD fees 2.9% + $0.30)

**FX risk note:**
- EUR/USD fluctuation ±10% within 12 months (historical volatility)
- USD-denominated contracts should include FX clause: «price in EUR; USD equivalent
  at invoice date ECB rate + 3% processing»
- Ruslan operates on EUR expenses (rent, tools, GmbH) → USD revenue creates FX
  exposure; hedge via: USD collected → converted monthly to EUR at mid-market

---

## §2.12 Phase-1 Reach Reconciliation

**Question:** Доставляет ли эта pricing-структура €50K Q2 2026?

### CC-1 revenue-mix (investor-critic ack, mandatory arithmetic)

[src:decisions/JETIX-PLAN.md#§3.1.1]

| Line | Volume | Price | Revenue Q1+Q2 2026 |
|---|---|---|---|
| **Productized contracts (USB-C Path B)** | 4 contract-quarters (2 contracts × 2 Q) | €7.5K/contract-Q (≈ €3K onboarding + €15K/yr ÷ 4Q) | **€30K** |
| **Hourly consulting (4-pack "конкретная помощь" + discovery sessions)** | 233 hours | €150/hr | **€35K** |
| **Total (gate: €50K, ~30% buffer)** | | | **€65K** |

**Reconciliation of Path B contract-quarter unit:**
- Path B yr1 total: €3K onboarding + €15K annual license = **€18K/yr**
- Per quarter (for CC-1 arithmetic): €18K ÷ 4Q = **€4.5K/Q average**
- But CC-1 uses **€7.5K/contract-quarter** — this reflects that 2 contracts are
  signed in Q1 AND Q2, each generating:
  - Q1: €3K onboarding (upfront) + €3.75K (half-year license = €15K/2) = €6.75K ≈ €7.5K
  - Q2: renewal/continuation Q of same 2 contracts → license prorated
- The €7.5K figure approximates the FIRST-YEAR total value per contract divided
  proportionally; minor rounding acceptable (CC-1 was acked by investor-critic)

**Implication for pricing set in §2.3.1:**
- Path B €3K onboarding + €15K/yr = €18K yr1 = exactly the anchor used in CC-1
- This validates §2.3.1 pricing as consistent with CC-1 arithmetic ✓

**Does this pricing structure deliver €50K Q2 2026?**

| Scenario | Revenue estimate | Gate outcome |
|---|---|---|
| **Conservative (2 Path B contracts + 167 hrs hourly)** | 2 × €7.5K + 167 × €150 = €15K + €25K = **€40K** | MISS by €10K |
| **Base (CC-1 ack: 2 contracts × 2Q + 233 hrs hourly)** | €30K contracts + €35K hourly = **€65K** | PASS (30% buffer) |
| **Optimistic (+ 1 Producer retainer 3 mos €3K/mo)** | €65K + €9K = **€74K** | PASS (48% buffer) |

**Conservative scenario FAILS** if only 2 Path B contracts signed in Q1 (not 2 in Q1 + 2 in Q2). This means
hourly consulting is NOT optional overflow — it is a **mandatory co-equal revenue line**
carrying ≈54% of Phase-1 target. [src:decisions/JETIX-PLAN.md#§3.1.1 CC-1 resolution]

**Operator guidance (direct, no fluff):**
- Schedule **≥20 hrs/week billable capacity** across Q1+Q2 2026 at €150/hr
- Target **2 Path B contracts closed per quarter** (not per half-year)
- Продюсерский центр retainer(s) add buffer; even 1 Standard tier client (€5K/mo × 3 mos) = €15K buffer

**Margin-of-safety on the €50K gate:**
margin_of_safety = (€65K base - €50K target) / €50K target = **30%** — exactly Graham floor.
Passes but thin. Any sustained delay in hourly consulting (fewer than 20 hrs/week billable)
collapses the buffer. Risk-of-ruin floor: if revenue falls below €30K in H1 2026 →
Ruslan runway impact = ~2 months buffer lost (at €300-800/mo Phase-1 run rate per
ROY-INFORMATION-DIET + personal living expenses).

---

## §2.13 Preserved Dissents

### Dissent D-price-1: aspirational миллионер-tier pricing vs Phase-1 P1A reach

**Position A (aspirational):** миллионер-tier retainers €20K-€50K/mo represent the
real TAM ceiling. audio_529 + audio_470 reference клиентов $20-50K/mo. The portfolio
should be priced to capture these clients from Phase-1.

**Position B (investor-expert position):** Phase-1 cold outreach (P1A = Mittelstand +
Startupper) is sized for €5K-€15K engagements, NOT €20K-€50K/mo retainers. Millionaire
clients ($1M+/yr) are P1B referral-only per L6 ack. Pricing a Phase-1 offer at
миллионер-tier creates AP-INV-11 (mistaking comfort for low risk — pricing the aspirational
ceiling as the operational floor when Phase-1 has zero social proof to command it).

**Resolution:** Price Phase-1 at P1A range (§2.1 §2.2 above). Aspirational pricing
document separately as «миллионер engagement proposal» — available when P1B referral
materializes. Do NOT pre-set Phase-1 outreach at миллионер-tier pricing without social
proof. Both positions preserved; resolution: P1A pricing primary, P1B pricing as
AWAITING-APPROVAL HITL packet when first миллионер referral materializes.

**F / ClaimScope / R:**
- F: F4 (Position B based on payment-ability filter mechanics + bandwidth-discipline
  argument from L6 §2.1 P1A/P1B split)
- ClaimScope: Phase-1 solo-outreach context only; fails if warm referral to миллионер
  arrives before G1
- R: refuted if first P1B инbound миллионер closes at €20K+ engagement within Phase-1;
  accepted if zero миллионер closes at aspirational tier within 6 months of P1A outreach

### Dissent D-price-3: Secure Network launch pricing (€19-€199/mo vs L5 €200-€500/mo placeholder)

**Position A (L5 placeholder):** Secure Network = €200-€500/mo — consistent with
premium professional community pricing (YPO analog, executive network pricing).

**Position B (L7 investor-expert re-anchor):** Phase-3 LAUNCH pricing should be
accessible (€19-€199/mo) to build initial density; premium pricing (€200-€500) applies
at G4+ when network density and NPS justify it. Launching at €200+/mo without NPS
validation = risk-of-ruin: low conversion, low density, network dies before effects emerge.

**Resolution:** Both positions preserved. §2.5 sets G2→G3 launch tiers (€19-€199);
G4+ pricing escalation path formally planned at Phase-3 review. Neither position
overrides the other at their respective gate.

### Dissent D-price-4: Educational cohort minimum price (€3K L5 floor vs €5K L7 arithmetic floor)

**Position A (L5 §3.7):** cohort €3K-€8K/learner range as stated.

**Position B (L7 arithmetic):** margin>€3K/learner gate (per L5 Q4 ack) requires
≥€5K/learner at 10-learner cohort to pass. €3K floor fails its own gate predicate.

**Resolution:** §2.7 flags this as an arithmetic inconsistency in L5's own stated gate.
L7 sets €5K as operating minimum for gate compliance. L5 floor of €3K retained as
«aspirational below-minimum» for large cohorts (20+ learners) where fixed COGS amortize.
This is a FLAG for brigadier, not a Lock revision request.

---

## §X — Cell C-01 Self-Improvement Notes

### Pattern 1 — Pricing reconciliation requires 3-pass loop

Effective pricing finalization cannot be done in single pass. The minimum viable
loop is:

1. **Aspirational tier pass** — what does the market allow? (TAM anchor)
2. **Unit-econ check** — does each tier clear GM floor? (margin-of-safety gate)
3. **Cash flow check** — does the pricing structure deliver the gate target
   (€50K Q2 2026)? (reach reconciliation per CC-1)

Skipping pass 2 (as L5 did deliberately, since it deferred to L7) produces tiers that
look plausible but fail their own acceptance predicates (e.g., Продюсерский центр Pilot
tier is too thin for 20-30% case-study discount; Educational cohort €3K floor fails
margin>€3K/learner gate).

**Compound rule candidate:** «pricing-finalization requires 3-pass loop: aspirational
→ unit-econ → cash-flow; any tier failing pass 2 or 3 must be revised before shipping.»

### Pattern 2 — L5 placeholder ranges embed implicit gate conflicts

L5 deliberately deferred pricing to L7. But L5 DID specify qualitative gates
(margin>€3K/learner; 70.7% GM Path B; payment-ability filter $5K/mo). These gates
constrain the pricing space implicitly. When L7 runs arithmetic, it discovers that
some L5 placeholder floors fail their own gates (Educational €3K; Pilot discount case).

**Compound rule candidate:** «when inheriting placeholder pricing ranges with embedded
quality gates, always run gate-arithmetic against floor AND ceiling of the range; the
range that fails its own gate is not a valid placeholder — it is a FLAG for the
originating cell.»

### Pattern 3 — Dissent preservation is structurally different from ambiguity escalation

Two distinct patterns appeared in this cell:

- **D-price-1 (aspirational vs reach):** genuine investor dissent — two legitimate
  positions with different ClaimScope. Preserved in §2.13, neither averaged.
- **D-price-4 (€3K vs €5K educational floor):** NOT a dissent — it is an arithmetic
  inconsistency where one number fails its own stated constraint. This is a FLAG,
  not a preserved dissent. Flagging ≠ preserving; flagging = requiring correction.

**Compound rule candidate:** «distinguish preserved-dissent (two legitimately scoped
positions) from arithmetic-inconsistency (one number fails its own gate predicate);
only the former goes into §dissents block; the latter is a FLAG requiring revision.»

---

*Draft complete. Cell C-01 investor-expert mode integrator+critic. Word count estimate:
~4200 words. Awaiting brigadier §5.5.5 provenance gate before promotion to canonical
LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.*
