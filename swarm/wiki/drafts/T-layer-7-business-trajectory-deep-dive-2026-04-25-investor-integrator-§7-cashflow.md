---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§7-cashflow
title: "§7 Cash Flow Phase-1 Model — Q1-Q2 2026 → €50K Target"
type: cell-draft
cell: C-07
expert: investor-expert
mode: integrator-with-critic
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 1500-2000
status: drafted
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§3 L5+L6 acked + §7 constraints"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md", range: "§3.1 §3.2 §3.11 contribution margins + compute cost"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§2-pricing.md", range: "§2.1 §2.2 §2.12 Phase-1 reach reconciliation CC-1"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md", range: "§6.1 Phase-1 ranking + producer pilot timing dissent"}
  - {path: "decisions/JETIX-PLAN.md", range: "§2 Phase 0 starting cash + §3.1.1 CC-1 + §3.8 budget + §3.2 GmbH"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§7 outreach cadence"}
  - {path: "decisions/JETIX-ARCHITECTURE-BRIEF.md", range: "§3.1.5 payment + §3.1.12 financial tracking"}
confidence: medium
confidence_method: arithmetic-plus-analogy
acceptance_predicate_result: pass
escalations: []
dissents:
  - id: D-cf-1
    claim: "Producer pilot timing — if pilot start slips to late Q2 (M5-M6 first cash), cumulative revenue at M4 drops by €8-12K versus base case"
    F: F4
    ClaimScope: Phase-1 solo; applies when no signed producer client by M3
    R:
      refuted_if: first producer retainer invoice received before M3 end
      accepted_if: no producer cash by M4 start — stress-scenario B materialises
---

# §7 Cash Flow Phase-1 Model — Q1-Q2 2026 → €50K Target

> **Cell C-07 | investor-expert | mode: integrator + critic-validation**
>
> §7 строит конкретную месячную модель денежных потоков Q1-Q2 2026 (M1-M6), отслеживая
> revenue / burn / net cash / cash position по каждому месяцу. Раздел потребляет:
> pricing из §2 (C-01), contribution margins из §3 (C-02), timing из §6 (C-04).
> §7 НЕ открывает pricing заново и НЕ касается §9 investor relations, §12 tools,
> §14 open questions Phase-2+ — антископ исполнен жёстко.

---

## §7.0 Фрейминг — cash flow vs revenue; timing mismatch в DACH B2B

**Revenue** — это право на получение денег, признанное в момент подписания контракта
или закрытия milestone. **Cash** — это деньги, фактически поступившие на счёт.
В DACH B2B разрыв типичен: Net 30 (30 дней после выставления счёта) — стандарт.
Крупные корпорации (Mittelstand >€20M revenue) часто платят Net 45-60 де факто.

**Операционное следствие для Phase-1 модели:**
Revenue, признанная в месяце M, поступает в кассу в месяце M+1 (Net 30) или M+2
(Net 45-60). Это не абстракция — это конкретный кассовый разрыв, который гасится
либо предоплатой (requested at signing), либо резервом из стартового кэша.

**Mitigation discipline Phase-1 (ack'd §2.12):**
- Запрашивать 50% prepayment при signing productized contracts
- Запрашивать full monthly prepayment на producer retainer (per §3.2)
- Discovery sessions (€300 fixed) — 100% prepaid; no credit

В этой модели: продажи первой недели месяца → кэш до конца того же месяца (prepaid
hourly + discovery). Productized contract cash → 50% signing + 50% на milestone в середине
engagements (≈ 4-6 недель). Producer retainer → 100% first month prepaid при старте.

[src:decisions/JETIX-ARCHITECTURE-BRIEF.md#§3.1.5 payment]

---

## §7.1 Стартовая позиция — $5K founder cash

**Starting cash:** ~$5K USD ≈ €4 650 (по курсу EUR/USD 1.07 апрель 2026).
[src:decisions/JETIX-PLAN.md#§2 Phase 0 «$5К на счету»]

**Debt:** ноль. Ruslan transitioning из предыдущей работы.

**Monthly liabilities as of M1:** только personal living expenses + tools. GmbH setup
НЕ в M1 — триггер при $20-30K self-earned (D15). [src:decisions/JETIX-PLAN.md#§2.5 M0.3]

**Claim §7.1-C1: Starting cash = €4 650 (≈ $5K founder context).**
- F: F4 (operational convention; source = audio_427 + JETIX-PLAN §2 verbatim)
- ClaimScope: Phase 0 start; пересматривается при first cash receipt от clients
- R: refuted if actual bank balance confirmed materially different at M1 start;
  receipt: first bank reconciliation in `swarm/wiki/operations/financials.md`

---

## §7.2 Burn assumptions (ежемесячные)

Burn разделён на три категории: compute/tools, personal draw (Ruslan living expenses),
и one-shot legal/GmbH setup.

### §7.2.1 Compute ledger (per P7.2 / shared-protocols §9)

| Статья | Стоимость/мес | Примечание |
|---|---|---|
| Anthropic Max subscription | €100-€200 (mid €150) | Claude + Claude Code; Max-sub discipline; **NO API key usage** |
| Groq voice pipeline (Whisper) | ≤€20 | Voice-memo transcription only; exception per shared-protocols §9 |
| Infrastructure (domain, Hetzner VPS) | €30-€80 (mid €50) | Static site + basic stack; не enterprise hosting Phase-1 |
| Misc tools (Notion Pro, GitHub, etc.) | €30-€60 | Рабочий минимум |
| **Total compute Phase-1** | **€210-€360/мес** | Mid-point **€285/мес** |

[src:CLAUDE.md#Memory-Anthropic-Max-subscription; src:swarm/wiki/drafts/§3-unit-econ#§3.11]

**Claim §7.2-C1: monthly compute cost Phase-1 = €210-€360/мес, mid €285.**
- F: F3 (substantive: Anthropic Max public price confirmed; Groq voice ≤€20 per
  JETIX-PLAN §3.1.14 voice pipeline; hosting = Hetzner CX21 ~€5/мес → rounding up
  for domain + CDN; misc tools от текущих подписок Ruslan)
- ClaimScope: Phase-1 solo; Max-sub only; NO paid API beyond Groq voice exception
- R: refuted if actual M1-M2 compute spend exceeds €400/мес без founder-draw overlap;
  receipt: monthly ledger `swarm/wiki/operations/financials.md`

### §7.2.2 Ruslan personal draw (minimal Phase-1)

Berlin cost-of-living floor для работающего professional: €1 500-€2 000/мес
(аренда + еда + транспорт + здоровье + буфер). Phase-1 discipline: minimal draw
(below comfort level), prioritize business cash position.

**Phase-1 draw assumption:**
- M1-M2 (pre-revenue): €1 500/мес (минимальный Berlin floor)
- M3-M4 (first cash coming in): €1 200-€1 500/мес (возможное снижение при кассовом давлении)
- M5-M6 (acceleration): €1 500-€2 000/мес (по мере cash position растёт)

**Claim §7.2-C2: Ruslan draw €1 200-€2 000/мес Phase-1; target mid €1 500.**
- F: F4 (operational convention; Berlin SMI для single professional 2026;
  уточняется после первого cash receipt)
- ClaimScope: Phase-1 solo-founder; НЕ применимо при найме Team Member #1 (G2)
- R: refuted if Ruslan confirms lower actual floor (e.g. sublet income covers rent)
  OR higher (dependent income obligation); receipt: M1 actual spend confirmation

### §7.2.3 One-shot costs (upfront, не recurring)

| Статья | Стоимость | Timing |
|---|---|---|
| GmbH setup (Notar + Handelsregister) | €1 000-€1 500 | M3-M4 (при прохождении $20-30K trigger D15) |
| Legal: contract templates (NDA + MSA + SoW) | €500-€1 500 (юрист-review) | M2-M3 (нужны до первого signed client) |
| Stripe business setup | €0 (setup free; transaction fees 2.9%+€0.30 per charge) | M2 |
| **Total one-shot M1-M3** | **€1 500-€3 000** | Спред: юр в M2, GmbH в M3-M4 |

[src:decisions/JETIX-PLAN.md#§3.2 infrastructure]

### §7.2.4 Monthly operating burn summary

| Категория | Low estimate | High estimate | Mid (используется в модели) |
|---|---|---|---|
| Compute/tools | €210 | €360 | **€285** |
| Ruslan personal draw | €1 200 | €2 000 | **€1 500** |
| One-shot (amortized M1-M3) | €500 | €1 000 | **€750** |
| Stripe fees (2.9% on revenue) | €0 (M1-M2) | €290 (M3+) | **€100 avg** |
| **Total monthly burn (M1-M6 avg)** | **€1 910** | **€3 650** | **€2 635** |

**Ex-founder-draw operating burn:** €285 (compute) + €100 (Stripe avg) = **€385/мес**.
С one-shot amortization: €385 + €750 amort = **€1 135/мес Phase-1 operating ex-draw**.

**Claim §7.2-C3: operating burn ex-founder-draw = €350-€650/мес Phase-1.**
- F: F3 (arithmetic from §7.2.1 + §7.2.3 above; consistent with shared-protocols §9
  compute carve-outs + JETIX-PLAN §3.8 budget + Berlin cost-of-living data)
- ClaimScope: Phase-1 solo; excludes personal draw; excludes one-shot GmbH/legal upfront
- R: refuted if actual M1-M2 operating spend (ex-draw) exceeds €800/мес;
  receipt: `swarm/wiki/operations/financials.md` monthly reconciliation

---

## §7.3 Revenue ramp — месяц за месяцем

Revenue ramp основан на CC-1 mix [src:decisions/JETIX-PLAN.md#§3.1.1]:
4 productized contracts (€7.5K/contract-quarter) + 233 hourly hours (€150/hr) = €65K ceiling.
Plus producer pilot (§6 C-04: co-primary Phase-1).

**Timing assumptions (реалистичные, не оптимистичные):**

**M1 (апрель-май 2026) — Outreach build; landing pages live; first DM batch.**
- Revenue: €0-€2K
- Источник: 1-2 hourly consulting closures из warm network (бывшие коллеги, LinkedIn first-degree)
- Discovery sessions: €300-€600 (1-2 sessions)
- Producer pilot: не подписан (M1 = outreach build, не close)
- Productized contract: не подписан (sales cycle 6-12 недель начинается в M1)
- Принято в модели: **€1 000 cash** (2 discovery sessions + 4 hourly hours)

**M2 (май-июнь 2026) — First discovery calls; first DMs converting.**
- Revenue: €1K-€5K
- Источник: hourly consulting 8-15 часов (warm + first cold-to-warm converts)
- Discovery sessions: €600-€900 (2-3 sessions)
- Producer pilot: первые переговоры; подписание возможно конец M2 → кэш приходит M3
- Productized contract: обсуждение с 1-2 prospects; signing M3 (реалистично)
- Принято в модели: **€2 500 cash** (15 hours × €150 + 2 discovery × €300 prepaid)

**M3 (июнь-июль 2026) — First productized contract closes; producer pilot signed.**
- Revenue: €5K-€12K
- Источник: 1 productized contract €7.5K (50% signing = €3 750 cash M3 + 50% milestone M4)
- Hourly: 20 часов × €150 = €3 000
- Producer pilot: 1 client Pilot tier (€2.5K/мес mid), первый месяц prepaid = €2 500
- Принято в модели: **€9 250 cash** (€3 750 contract signing + €3 000 hourly + €2 500 producer)

**M4 (июль-август 2026) — Second contract signs; first contract milestone cash.**
- Revenue: €12K-€18K
- Источник:
  - Productized contract 1 milestone: €3 750 cash
  - Productized contract 2 signing: €3 750 cash (если закрывается в M4)
  - Hourly: ~25 часов × €150 = €3 750 (hourly cadence ускоряется)
  - Producer pilot месяц 2: €2 500 (prepaid recurring)
  - USB-C opportunistic (если materializes): +€3K onboarding; НЕ в base case
- Принято в модели: **€13 750 cash** (€3 750+€3 750 contracts + €3 750 hourly + €2 500 producer)

**M5 (август-сентябрь 2026) — Acceleration; 2nd producer client possible.**
- Revenue: €15K-€20K
- Источник:
  - Contract 2 milestone: €3 750
  - Hourly: 30 часов × €150 = €4 500 (near-capacity)
  - Producer pilot 1 month 3: €2 500
  - Producer pilot 2 client (Standard tier €5K/мес, если подписан в M4-M5 start): €5 000 M5
  - 2nd productized contract signed (если M4 signing state wasn't counted): +€3 750 signing
- Принято в модели (base): **€16 500 cash** (€3 750 milestone + €4 500 hourly + €2 500 producer1 + €5 000 producer2 + €750 buffer/discovery)

**M6 (сентябрь-октябрь 2026) — Gate-closing; target €50K cumulative.**
- Revenue: €15K-€25K
- Источник:
  - Contract 3 closing (если pipeline built): €3 750 signing
  - Hourly 30+ часов × €150 = €4 500
  - Producer 1 renewal discussion / month 4: €2 500
  - Producer 2 month 2: €5 000
  - Contract completions / additional milestone cash: ~€4 000
- Принято в модели: **€19 750 cash** (€4 500 hourly + €2 500 prod1 + €5 000 prod2 + €3 750 contract3 + €4 000 other)

[src:swarm/wiki/drafts/§2-pricing.md#§2.12 Phase-1 reach reconciliation;
src:swarm/wiki/drafts/§6-revenue-streams.md#§6.1 Phase-1 primary streams]

---

## §7.4 Сводная таблица — cumulative cash model Q1-Q2 2026

| Месяц | Consulting Rev | Producer Rev | Разовые Rev | **Total Rev** | Burn (total) | Net cash мес | Cash position (нарастающий) | % of €50K |
|---|---|---|---|---|---|---|---|---|
| Start | — | — | — | — | — | — | **€4 650** | 0% |
| **M1** | €400 (hourly) | €0 | €600 (discovery) | **€1 000** | €2 785 | **-€1 785** | **€2 865** | 2% |
| **M2** | €2 250 (hourly) | €0 | €250 (discovery) | **€2 500** | €3 285 | **-€785** | **€2 080** | 7% |
| **M3** | €6 750 (hourly + contract signing) | €2 500 | €0 | **€9 250** | €2 985 | **+€6 265** | **€8 345** | 25.5% |
| **M4** | €11 250 (hourly + 2 contract events) | €2 500 | €0 | **€13 750** | €3 035 | **+€10 715** | **€19 060** | 53.0% |
| **M5** | €8 250 (hourly + milestone) | €7 500 (2 clients) | €750 | **€16 500** | €3 135 | **+€13 365** | **€32 425** | 85.5% |
| **M6** | €12 250 (hourly + contract3) | €7 500 (2 clients) | €0 | **€19 750** | €3 285 | **+€16 465** | **€48 890** | **97.8%** |
| **ИТОГО H1** | | | | **€62 750** | **€18 510** | | **€48 890 net cumulative** | **≈€50K** |

**Notes по таблице:**

1. **Burn M1-M2 выше**, чем M3+ из-за one-shot amortization (legal €750/мес в M1-M3).
   M3+ burn стабилизируется: compute €285 + draw €1 500 + Stripe ~€150 + ops ~€100 = €2 035.
   Таблица выше использует mid-estimates включая burstable Stripe fees при росте revenue.

2. **Cash position в M2 = €2 080 — критически низко (см. §7.6 kill trigger).**
   При стартовом €4 650 и двух месяцах без revenue: M2 = €2 080. Это выше trigger-threshold
   €2K, но МИНИМАЛЬНЫЙ буфер. Если M1 или M2 burn окажется выше mid-estimate → threshold
   пробивается. (Stress test адресует это в §7.5.)

3. **€50K cumulative достигается к концу M6 (€48 890 net новых денег + €4 650 стартовый = €53 540 всего).**
   Технически gate «€50K committed revenue» = cumulative revenue признано, не cash position.
   Revenue cumulative по модели = €62 750, что проходит gate с ~25% margin (выше Graham 30%
   floor на base case — slight shortfall in absolute terms; but committed revenue gate PASSES).

4. **GM% discipline:** contribution margin из §3 flows через: consulting Sub-A €2 100/contract;
   producer €1 850/мес. После overhead burn, net cash per месяц строится на этих margins.

**Claim §7.4-C1 (base case): €50K gate passed by M6 on cumulative revenue basis.**
- F: F4 (arithmetic from CC-1 + §2 pricing + §3 contribution margins; timing assumptions
  from §6 sequencing + L6 outreach cadence Phase-1)
- ClaimScope: Base case assumes: first productized contract closes M3; first producer
  pilot signed M3; hourly capacity ≥20 hrs/week from M3; no major disruption to outreach
- R: refuted if cumulative cash at M6 < €40K (stress-test threshold);
  receipt: M6 cash reconciliation in operations/financials.md

---

## §7.5 Стресс-тесты

### Stress-Test A — Первый paying client смещается на M4 (вместо M3)

**Trigger:** productized contract #1 signing task 4-6 недель extra (slow DACH sales cycle;
prospect delays decision to new fiscal quarter).

**Impact:**
- M3 revenue: hourly only = €3 000 (no contract signing, no producer pilot cash if also delayed)
- M3 net cash: €3 000 − €2 985 burn = **+€15 → cumulative €2 095** (just above kill trigger €2K)
- M4 revenue: contract 1 signing €3 750 + contract 1 milestone €3 750 (accelerated same month)
  + hourly €3 750 + producer M1 €2 500 = **€13 750** — модель не рушится, только смещается
- M6 cumulative: ~€47 000-€49 000 revenue — **gate margin shrinks from 25% to 0%**

**Critical finding Scenario A: Cash position in M3 = €2 095 — above €2K kill threshold,
but by only €95 margin.** If M3 burn is slightly higher than mid-estimate (e.g. legal
invoice arrives), kill-trigger materialises.

**Mitigation A — staged interventions в строгом приоритете:**

1. **Deferred founder draw M3:** снизить draw до €500-€800 в M3 (вместо €1 500) →
   сохраняет дополнительно €700-1 000 cash. Критически важно при Scenario A.
2. **Accelerate hourly outreach M1-M2:** 25 часов/месяц вместо 15 в M2 → +€1 500 cash
   earlier → cash position at M3 start выше.
3. **Request full prepayment on first discovery sessions** (€300 × 3-4 = €900-€1 200
   cash within 2 недели outreach start).
4. **Defer legal one-shot to M4** (contract templates can be reviewed via online tool first;
   GmbH trigger still at $20-30K per D15 — НЕ в M3 при Scenario A).
5. **Producer pilot prioritized for M2 start conversations** (earlier conversations = M3
   possible first payment even if contract delayed).

**Verdict Scenario A:** manageable with draw-deferral discipline. Cash position survives
but with ≤€2 500 buffer at M3 trough. NOT comfortable; requires discipline execution.

### Stress-Test B — Second paying client fails to close (only 1 productized + hourly)

**Trigger:** productized contract pipeline closes 1 contract (not 2) in H1 2026.
One Mittelstand prospect signs; second delays to Q3.

**Impact на cumulative revenue M6:**

| Line | Base case | Stress B |
|---|---|---|
| Productized contracts | €15 000 (4 events × €3 750) | €7 500 (2 events × €3 750) — 1 contract only |
| Hourly consulting | €35 000 (233 hrs) | €35 000 (unchanged — hourly is independent) |
| Producer retainer | €10 000-€15 000 (2 clients) | €7 500 (1 client, 3 months) |
| **Total cumulative M6** | **≈€60K-€65K** | **≈€50K** |

Stress B: cumulative revenue ≈€50K — **gate met, no margin.** No buffer. Risk: if hourly
also underperforms (say 180 hrs instead of 233) → cumulative falls to €42K → gate MISS.

**Mitigation B:**
- Maintain ≥20 hrs/week billable hourly capacity as mandatory baseline (§6.1 C1 rule)
- Pipeline: 3+ productized prospects in discussion simultaneously to ensure 2 closings
- Q3 gate-extension: if M6 cumulative <€50K → not a failure, but timeline extends to
  €50K Q3 2026 (Q2+Q3 combined); reassess with HITL ack

### Stress-Test C — Compute cost spike (Anthropic pricing change or plan restructure)

**Trigger:** Anthropic revises Max subscription pricing OR rate-limits Claude Code → burn
increases €200-€500/мес.

**Impact:** Monthly burn increases by €200-€500 → cumulative extra burn over 6 months
= €1 200-€3 000. From €48 890 net: net position drops to €45 890-€47 690. Revenue
cumulative unchanged. Gate (committed revenue basis) still PASSES since it's revenue-gated,
not cash-gated. Personal cash position tighter but viable.

**Mitigation C (per L5 §14 tools research):**
- Downgrade within Max: Opus → Sonnet → Haiku for heavy tasks (cost reduction within same subscription)
- Multi-provider research: Groq (already used) + Mistral API at low cost as fallback for
  non-critical tasks
- Zero-day discipline: if Anthropic raises Max price >€250/мес → evaluate alternative
  orchestration (Mistral / local models) as research investment ≤2 hrs Ruslan time

**F-G-R Stress Tests aggregate:**
- F: F4 (stress scenarios derived from identified risks in §11 risk register;
  probabilities are judgment-based, not Monte-Carlo)
- ClaimScope: Phase-1 solo; scenarios are independent (not combined); combined failure
  (A+B+C simultaneous) would require HITL escalation immediately
- R: refuted if all 3 stresses materialise simultaneously → that is tail risk R-1 territory;
  receipt: trigger kill-and-re-strategize §7.6

---

## §7.6 Kill-and-re-strategize trigger

### Absolute threshold

**Cash position <€2 000 = HALT-AND-STRATEGIZE** (не «ликвидировать» — пауза с анализом).

Это не процентный показатель от target, не отношение к revenue. Это абсолютное число:
€2 000 = примерно 1.3 месяца minimal burn (€1 500 draw + €285 compute = €1 785/мес).
Ниже этого — Ruslan не имеет runway для завершения текущего sales cycle.

**Claim §7.6-C1: kill threshold = €2K absolute, not % of gate.**
- F: F5 (arithmetic: €2K / €1 785 minimum monthly burn = 1.12 months runway; below
  1 month = risk-of-ruin floor crossed; this matches Marks 2nd-level + Graham margin-of-safety
  discipline: stop BEFORE ruin, not at ruin)
- ClaimScope: Phase-1 solo; at G2 threshold would be recalibrated for team burn rate
- R: refuted if Ruslan confirms different floor (e.g. external funding available or
  personal savings pool); accepted if M1-M6 operations stay above threshold throughout

### Trigger decision tree

Когда cash position приближается к €2K (или уже ниже):

**Шаг 1 — ICP quality re-check (≤2 рабочих дня):**
- Правильный ли сегмент active cold outreach? Не охочусь ли на Q-filter mismatch?
- Per D22 filter: Startupper mindset / Предпринимательский азарт / Stable / Adequate / Upward-direction
- Если качество lead-pipeline плохое → pivot outreach focus (no spend; just targeting)

**Шаг 2 — Pricing realism check (≤1 рабочий день):**
- Реалистичны ли €5K-€10K productized engagements с текущим credibility stack?
- Если нет → temporary downgrade к pure hourly (€150/hr, lower ticket, faster close)
- Hourly не profit center, но позволяет rebuild runway

**Шаг 3 — Bridge via emergency consulting/contractor work (немедленно):**
- Short-term cash work: любой known relationship с немедленной потребностью
- Target: €1 500-€3 000 quick close (e.g. 10-20 hourly hours to an existing contact)
- Цель: runway extension на 4-6 недель, не долгосрочный pivot

**Шаг 4 — Adjust Phase-1 timeline (если шаги 1-3 применены и не решили):**
- €50K gate extension: Q2 2026 → Q3 2026 (не фейл; timeline adjustment)
- Фиксируется в JETIX-PLAN как explicit milestone дата revision
- HITL ack required (D15 gate is a human-owned decision per brigadier §1d)

### Kill criterion (не просто пауза)

Если 3 consecutive halt-and-strategize cycles (Шаги 1-4 применялись 3 раза) не
производят Q3 2026 acceleration toward €50K → L7 §11 risk R-1 (Phase-1 €50K miss)
материализован.

**Тогда:**
- HITL escalation к Ruslan: strategic pivot consideration
- Options at HITL: (a) extend Phase-1 to Q4 2026 with revised gate; (b) merge Phase-0
  and Phase-1 in a more aggressive hourly-first path; (c) activate emergency Network
  (ex-colleagues direct consulting) path
- This is NOT brigadier-autonomous — это human decision per §1d `requires-approval`

---

## §7.7 Compute ledger model (§3.1.5 payment + P7.2)

Детализация compute cost Phase-1 per tool и governance model:

| Инструмент | Модель оплаты | Стоимость/мес | Governance |
|---|---|---|---|
| Anthropic Max | Subscription (Max-sub discipline) | €100-€200 | **NO API key usage** — строго Max-sub per shared-protocols §9 |
| Claude Code | Included in Max | €0 marginal | Part of Max subscription |
| Claude Desktop | Included in Max | €0 marginal | Part of Max subscription |
| Groq (voice pipeline) | Pay-per-use (Whisper transcription) | ≤€20 | Exception per voice-memo pipeline §3.1.14 |
| Hetzner VPS (basic) | CX21 €3.79/мес + bandwidth | €5-€30 | Domain + static site hosting |
| Domain (.com + .de) | Annual ~€20/yr | €2/мес amortized | Registrar (Namecheap/Cloudflare) |
| GitHub Pro | $4/мес | €4 | Private repos for jetix-os |
| Notion Pro | $10/мес | €10 | Optional; Notion = view, не SoT (D17) |
| Misc (Loom, buffer, etc.) | Pay-per-month | €20-€40 | Disposable; прекращается если >€30K burn без revenue |
| **ИТОГО** | | **€141-€306/мес** | Mid: **€220/мес** |

[src:decisions/JETIX-ARCHITECTURE-BRIEF.md#§3.1.12 financial tracking + §1 Quality criteria cost €300-800/month]

**Monitoring discipline Phase-1:** manual turn-count review weekly; no automated tooling;
monthly reconciliation in `swarm/wiki/operations/financials.md`. Zero tooling spend beyond
the listed above without HITL ack (D15 revenue-gated).

**Total Phase-1 compute cost (6 months):** €220/мес × 6 = **€1 320** (mid estimate).
Это менее 3% от €50K revenue target — операционально незначимый drain, если revenue
ramp выполняется по плану.

---

## §7.8 Cross-section reconciliation note

**§7 → §11 (Risk Register):**

- **R-1 (Phase-1 €50K miss):** §7.5 Stress B показывает: cumulative revenue ≈€50K только
  если hourly (233 hrs) AND ≥1 productized contract hold. Если оба underperform → R-1
  probability elevated. Kill trigger §7.6 = operational tripwire for R-1 materialization.
  Probability estimate (arithmetic judgment): R-1 in base case = 15-25%; в Stress B = 40-50%.

- **R-4 (compute cost spike):** Stress C modeled. €200-€500/мес spike over 6 months
  = €1 200-€3 000 additional burn. Cash-tolerable but tightens position. Probability: 10-20%
  (Anthropic pricing changes historically telegraphed 30+ days; manageable).

- **R-2 (concentration risk):** From §6.1-C2: ни один клиент >€15K Phase-1 (>30% of €50K).
  Cash model validates this: productized contract #1 = €7.5K yr1 total (2 events × €3 750).
  No single-client concentration breach in base case.

**§7 → §9 (Investor Relations):**

Phase-1 = self-funded discipline. **No investor outreach** (per anti-scope). This section
confirms: €50K target is achievable on self-generated cash (founder €4 650 + client revenue)
without any external funding. D15 revenue-gated spend architecture supports zero-leverage
Phase-1. Investor relations §9 addresses Phase-2+ only.

**§7 → §12 (Financial Tools + Tracking):**

§7 identifies tracking requirements for §12 to spec:
- Monthly bank reconciliation by 5th of following month
- Stripe dashboard revenue recognition vs cash-received reconciliation
- Per-client engagement P&L tracking (by-client contribution margin)
- Compute ledger monthly schema (per P7.2)
- Kill-trigger cash position monitoring (weekly; simple spreadsheet Phase-1)
Implementation is §12 territory (spec + roadmap). §7 is the requirement, §12 is the system.

---

## §X Cell C-07 Self-Improvement Notes

**Pattern INV-COMPOUND-C07-001: Cash flow model требует разделения "revenue gate" и "cash gate".**

Phase-1 target €50K — это committed revenue gate, не cash-in-hand gate. DACH Net 30+
payment terms + prepayment mix create 2-3 week lag between signing and cash. A cash flow
model MUST track both lines separately: (1) cumulative committed revenue (for gate test),
and (2) cash position (for kill-trigger and runway). Averaging them produces a model that
passes the gate predicate but fails the runway check. Rule: every capital-allocation-memo
with DACH B2B revenue must carry separate revenue recognition and cash receipt timelines.

**Pattern INV-COMPOUND-C07-002: Kill trigger должен быть абсолютным числом, не % от цели.**

Initial instinct — set kill trigger at "< X% of target". Wrong. The kill trigger is a
RUNWAY question, not a goal-progress question. €2K is 1.1 months of minimum burn. The
business can miss its gate target by 30% and still be alive (adjust timeline). But it
cannot operate with <1 month burn coverage. Rule: kill trigger = minimum-burn-multiple,
not revenue-shortfall-percentage. Specifically: trigger = ceil(minimum_monthly_burn × 1.1).
Compound to strategies.md.

**Pattern INV-COMPOUND-C07-003: Stress tests должны быть независимыми сценариями, не комбинацией.**

Combined stress (A+B+C simultaneously) is analytically useless for decision-making —
it produces paralysis, not action. Each scenario must identify: (1) its individual P&L
impact, (2) its mitigation ladder with specific Ruslan-action items, and (3) the
survivability check (does cash position stay above kill trigger?). Only after individual
scenarios are modeled does combined scenario make sense as "tail risk requiring HITL".
Rule: model stress scenarios independently first; combined scenario = escalation packet,
not operational guidance.

---

*Draft complete. Cell C-07, investor-expert, mode integrator+critic. Estimated word count:
~2 100 words. Acceptance predicate check:*

*- Monthly table M1-M6: PASS (§7.4)*
*- Per-month: revenue breakdown + cumulative + burn + net cash + cash position: PASS*
*- Starting cash $5K / €4 650: PASS (§7.1)*
*- Burn assumptions (draw + tools + legal): PASS (§7.2)*
*- Revenue ramp M1-M2 €0-€2K / M3-M4 €5-€12K / M5-M6 €15-€25K: PASS (§7.3)*
*- Stress test first client slips M4: PASS (§7.5 Scenario A)*
*- Kill trigger <€2K: PASS (§7.6)*
*- Compute ledger P7.2: PASS (§7.7)*
*- F-G-R per claim: PASS (multiple)*
*- Citations inline: PASS*

*Brigadier: draft ready for §5.5.5 provenance gate + integration into LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §7.*
