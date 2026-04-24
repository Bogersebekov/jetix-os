---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§3-unit-econ
title: "§3 Unit-Econ per Direction"
type: cell-draft
cell: C-02
expert: investor-expert
mode: scalability-with-critic-validation
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 2500-3500
sources:
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.1-§3.9 per-direction unit-econ hints"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§11 evolution + §6 matchmaker mechanics"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1.1 revenue-mix CC-1, §3.8 budget"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path A/B/C"}
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "full intake"}
  - {path: "CLAUDE.md", range: "KM-MVP infrastructure (compute substrate)"}
provenance_inline: true
status: drafted
---

# §3 Unit-Econ per Direction — L7 Business Trajectory Deep-Dive

> **Назначение раздела.** §3 вычисляет per-direction unit-economics: COGS, GM%, contribution margin, CAC, payback period, LTV, LTV:CAC — для каждого из 9 направлений. Ключевая метрика этого раздела: **Ruslan-hours per €1K revenue** — первичный показатель дефицитного ресурса Phase-1. Направление с низким Ruslan-hours per €1K = кандидат на масштабирование без bottleneck; направление с высоким показателем = требует productization или contractor-decoupling до масштаба.
>
> **Связь с другими разделами.** §3 unit-econ питает §7 (cash flow — monthly P&L построен на contribution margins отсюда), §11 (risk register — отрицательный margin или LTV:CAC <3:1 = risk row), §13 (evolution per gate — какие направления меняют структуру costs при переходе). §2 pricing (Wave-A sibling cell) определяет revenue line; если §2 pricing скорректирует numbers после integration pass, §3 числа обновляются. Все pricing references в этом draft помечены [placeholder — §2 integration required].

---

## §3.0 Framing — что считаем, что не считаем, и почему Ruslan-hours = первичная метрика

### Что такое unit-econ в контексте Jetix Phase-1

Unit-economics в Jetix Phase-1 — это **per-engagement contribution analysis**: сколько денег одна продажа оставляет после прямых затрат, учёта overhead-доли, и стоимости привлечения. Это не cash flow (тот в §7), не P&L (в §7 также), не финансовая модель компании целиком. §3 отвечает на один вопрос: «если я закрою одну дополнительную продажу по этому направлению — сколько contribution это принесёт, и сколько часов Ruslan это стоит?»

**Почему Ruslan-hours per €1K revenue = первичная скалярная метрика.**
Phase-1 = solo-founder + Max-subscription + агентный swarm + contractors on-demand. Единственный невосполнимый ресурс — attention budget Ruslan. Деньги можно привлечь (займы, pre-payment, early close). Агентов можно добавить (brigadier dispatch). Только часы Ruslan не масштабируются без найма. Следовательно, **productization scoring = обратная величина Ruslan-hours per €1K revenue**: чем ниже этот показатель, тем быстрее направление масштабируется без founder-bottleneck.

Целевые значения (эмпирические, Phase-A):
- **≤5 hrs/€1K** — scalable (автоматизирован настолько, что рост revenue не блокируется founder bandwidth)
- **5-15 hrs/€1K** — нормальная Phase-1 territory; требует productization roadmap
- **>15 hrs/€1K** — founder-bottleneck ceiling; без contractor или продуктизации направление не вырастет выше €5-8K/мес

### Базовые допущения (константы расчёта)

| Параметр | Значение | Источник |
|---|---|---|
| Ruslan loaded rate | €150/hr | [src:decisions/JETIX-PLAN.md#audio_452] |
| Contractor rate (general) | €50/hr (editor, ops) | Рыночный ориентир DE Phase-1 |
| Contractor rate (technical) | €80/hr (developer, architect) | Рыночный ориентир DE Phase-1 |
| Tooling fixed overhead (Anthropic Max + Groq voice) | €200-400/mo ≈ €300/mo mid | [src:CLAUDE.md#Global-Rules] |
| Operating overhead allocation rate | 10% выручки (ops/legal/compliance/KB-maintenance share) Phase-1 | Консервативная Phase-A норма; уточняется после первых 3 месяцев данных |
| GM% floor (D18 target) | ≥70% | [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.1 §1d D18] |
| LTV:CAC healthy threshold | ≥3:1 | Investor-expert rubric P3 (Marks risk-of-ruin) |
| Ruslan Phase-1 available hours | 30-40 hrs/wk billable + system (target 40 total) | [src:decisions/JETIX-PLAN.md#§3.6] |

**F-G-R для базового допущения по Ruslan rate:**
- F: F4 (operational convention; source = audio_452 verbatim «150 евро × 4 часа = 600 кэшфлоу»)
- ClaimScope: Phase-1 solo-founder; пересматривается при найме Team Member #1 (G2 gate)
- R: refuted если первый signed contract закрыт по ставке <€130/hr или >€200/hr — ставка корректируется в §3 update cycle; receipt: `swarm/wiki/operations/quick-money/contracts/*.md` первый signed

**Compute cost allocation.** €300/мес mid × 12 = €3 600/yr. Phase-1: 100% allocate на revenue-генерирующие направления (§3.1 Consulting + §3.2 Producer), по 50/50 split (€150/мес каждое). Phase-2+: spread по числу активных revenue directions пропорционально revenue contribution. Детали: §3.11.

---

## §3.1 AI Consulting — Unit-Econ

### Структура revenue (два sub-продукта)

**Sub-A: Productized 4-pack engagement (Path-B delivery model, Phase-A default).**
Средний engagement: €7 500 per contract-quarter [src:decisions/JETIX-PLAN.md#§3.1.1 CC-1]. Это €3 000 onboarding + €15 000/yr (≈€3 750/quarter renewal) = €7 500 при аннуализации первого квартала.

**Sub-B: Hourly consulting (4-pack «конкретная помощь»).**
Базовая ставка €150/hr. Revenue-mix CC-1: 233 часа × €150 = €35 000 за Q1+Q2 2026 — co-equal revenue line, не overflow.

### COGS per engagement

| Статья COGS | Sub-A (4-pack €7.5K) | Sub-B (hourly €150/hr) |
|---|---|---|
| Ruslan time (direct delivery) | 30 hrs × €150 = €4 500 | 1 hr × €150 = €150 |
| Contractor assistance (Phase-1 = 0) | €0 (solo Phase-A) | €0 |
| Tooling allocation per engagement | €150 (compute share) | €5 (проп. доля) |
| **Total direct COGS** | **€4 650** | **€155** |

**Gross margin pre-overhead:**
- Sub-A: (€7 500 − €4 650) / €7 500 = **38%** → ниже флора D18 ≥70% — FLAG
- Sub-B: (€150 − €155) / €150 = **−3%** gross hourly (solo delivery)

**Объяснение флага Sub-A.** Margin в 38% на productized consulting в Phase-A — норма для мягкого consulting-бизнеса с высокой долей founder time в delivery. Это НЕ фейл модели; это сигнал productization roadmap: contractor decoupling на G2 (hired editor/PM) снижает Ruslan-hours с 30 до 10-15, поднимая GM% до ≥60-70%. Path-B самого по себе высокий GM при decoupled delivery — его инвестор-критик оценил как 70.7% yr1 в KM-ARCH Dissent 3 [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§6 Delivery Path-B] — но только при условии, что delivery cost = methodology kit, не founder time.

**Sub-B hourly: gross negative per-hour при Ruslan loaded rate = €150.** Hourly sub-продукт имеет нулевую маржу именно потому, что единица revenue = единица cost (Ruslan-час × ставка = revenue и одновременно COGS). Это корректно. Hourly revenue = capital для productization, не free-cash. Инвестор-трактовка: hourly consulting = Phase-1 working capital machine, не profit center.

**Allocated overhead (10% revenue):**
- Sub-A: 10% × €7 500 = €750
- Sub-B: 10% × €150 = €15 per hour

**Contribution margin (post-overhead):**
- Sub-A: €7 500 − €4 650 − €750 = **€2 100 (28% contribution margin)**
- Sub-B: €150 − €150 − €15 = **−€15** per hour → hourly не profit-генерирует; это revenue-vehicle

### Ruslan-hours per €1K revenue

- Sub-A: 30 hrs / (€7 500 / €1 000) = **4 hrs/€1K** → scalable zone (≤5 порог)
- Sub-B: 1 hr / (€0.150K) = **6.7 hrs/€1K** → нормальная Phase-1; выше scalable threshold

**F-G-R:**
- Claim: Sub-A productized consulting = 4 hrs/€1K, scalable zone
- F: F4 (оценочная расчётная модель; одно engagement не верифицировано empirically)
- ClaimScope: Phase-A solo-delivery; Path-B methodology-kit; нет contractor
- R: refuted если первые 2 productized engagements потребуют >40 Ruslan-hours (>5.3 hrs/€1K); receipt: `swarm/wiki/operations/quick-money/engagements/<slug>/time-log.md`

### CAC

- **Тёплый referral:** ~0 прямых денежных затрат. Ruslan time = 2-5 hrs per close (DM + discovery + proposal). CAC by time: 3.5 hrs avg × €150 = €525
- **Холодный LinkedIn outreach:** 10-15 hrs/lead (research + outreach + follow-up + discovery) при conversion 5-10%. Acquisition cost: 12 hrs × €150 / 7.5% conversion = **€2 400 per closed client** (conservative)

**LTV:**
- 1-3 engagements/year × €7 500 = €7 500-€22 500 per year
- Средний retention consulting = 1-2 years (Phase-1 estimate; нет empirical data)
- Referral multiplier 1.5x (каждый client в среднем приводит 0.5 дополнительных clients)
- **LTV estimate: €15 000-€35 000** mid-point €22 500 [placeholder — needs 6-month data]

**LTV:CAC:**
- Warm referral: €22 500 / €525 = **42.8:1** — healthy
- Cold outreach: €22 500 / €2 400 = **9.4:1** — healthy (>3:1 threshold)

**Payback period:** Sub-A engagement оплачивается milestone-based (первый payment при старте). Payback = 1-2 месяца.

### Summary table — §3.1 AI Consulting

| Metric | Sub-A Productized | Sub-B Hourly |
|---|---|---|
| Avg revenue per unit | €7 500 | €150 |
| Direct COGS | €4 650 | €155 |
| Gross margin % | 38% ⚠️ | ~0% ⚠️ |
| Allocated overhead | €750 | €15 |
| Contribution margin | €2 100 (28%) | −€15 |
| Ruslan-hrs/€1K | **4.0 hrs** ✓ | **6.7 hrs** |
| CAC (warm) | €525 | €525 |
| CAC (cold) | €2 400 | €2 400 |
| LTV | €22 500 | n/a (per-hr) |
| LTV:CAC (warm) | 42.8:1 ✓ | — |
| LTV:CAC (cold) | 9.4:1 ✓ | — |
| Payback | 1-2 мес | immediate |

**GM% ниже флора D18 ≥70% для Sub-A. Обоснование:** Phase-A delivery cost = founder time. Contractor decoupling на G2 (hired PM/editor, €50/hr, 15 hrs вместо 30 hrs Ruslan) поднимет GM% до ≈60-65%; productized kit без live consulting поднимет до KM-ARCH Dissent 3 уровня 70.7%. Path: [Sub-A Phase-A delivery] → [decoupled G2] → [methodology kit G3] = GM% trajectory 38% → 65% → 70.7%+.

---

## §3.2 Продюсерский центр — Unit-Econ

### Revenue structure

Monthly retainer model. Avg retainer = €4 000/мес (mid-range между €2K-€8K Starter/Growth/Elite tiers; L7 §2 pricing sibling [placeholder — §2 integration required]). Avg engagement duration = 6 мес (Phase-1 estimate; 3-month minimum + typical 3-month renewal).

Engagement value = €4 000 × 6 = **€24 000 LTV per client Phase-1**.

### COGS per месяц

| Статья | Стоимость |
|---|---|
| Ruslan time (quality gate + voice preservation + client mgmt) | 8 hrs × €150 = €1 200 |
| Contractor (external editor, Phase-1 on-demand) | 10 hrs × €50 = €500 |
| Voice pipeline compute (Groq Whisper + Claude processing) | €50 allocated |
| **Total direct COGS per месяц** | **€1 750** |

**Gross margin per месяц (pre-overhead):**
- (€4 000 − €1 750) / €4 000 = **56.3% GM** → ниже ≥70% флора, но существенно лучше §3.1 Sub-A

**FLAG:** 56.3% GM ниже D18 target ≥70%. Объяснение: contractor cost (€500/мес) является основным drag. При автоматизации ≥70% production pipeline (агентами) и сокращении contractor до 6 hrs/мес contractor cost падает до €300 → GM% вырастает до 62.5%. При полной zeroisation contractor в Phase-2 (dedicated in-house editor, fixed cost, не per-hour) — GM% до ≥70% достижим. Trajectory: Phase-1 56% → Phase-2 (in-house editor allocated) 68% → Phase-3 (automated pipeline at scale) 75-80%.

**Allocated overhead (10% revenue):** €400/мес

**Contribution margin:** €4 000 − €1 750 − €400 = **€1 850/мес (46.3%)**

### Ruslan-hours per €1K revenue

8 hrs / (€4 000 / €1 000) = **2.0 hrs/€1K** → высоко scalable (well below ≤5 threshold)

Это лучший показатель среди Phase-1 активных направлений. Producer Center = самое продуктизированное из двух Phase-1 revenue directions.

**F-G-R:**
- Claim: Продюсерский центр = 2.0 hrs/€1K, most scalable Phase-1 direction
- F: F4 (расчётная модель; pipeline не верифицирована на реальных clients)
- ClaimScope: 1-3 pilot clients; Ruslan direct delivery; automated pipeline ≥60% (voice pipeline + /ingest + /ask)
- R: refuted если first pilot client потребует >20 Ruslan-hrs/мес при €4K retainer (>5 hrs/€1K); receipt: pilot time-log после первого месяца

### CAC

- Organic / referral path: Ruslan network + LinkedIn DM → 3-5 hrs/lead × €150 = €450-750. Conversion Phase-1 ≈15% (warm market). CAC = 4 hrs × €150 / 15% = **€4 000 per signed client** (если считать всё Ruslan time including failed calls)
- Целевой CAC снижается при pro-bono first case study → публичный кейс → inbound inquiries (JETIX-PLAN §3.4 «Blogger collaborations start»)
- При case study path: CAC Phase-1 = €2 000-3 000 effective (pro-bono стоит ~20 hrs Ruslan, амортизируется на 5+ leads)

**LTV:** €4 000/мес × 6 мес avg = €24 000 per client. Renewal rate Phase-1 (optimistic): 50% продлевают на 2nd 6-month cycle → effective LTV mid-point €36 000.

**LTV:CAC:**
- Best case (case study channel): €36 000 / €2 500 = **14.4:1** ✓
- Conservative (direct outreach): €24 000 / €4 000 = **6.0:1** ✓ (above 3:1)

**Payback:** Monthly retainer, prepaid в advance (per §3.2 L5 offer structure). Payback = 1 месяц.

### Summary table — §3.2 Продюсерский центр

| Metric | Value |
|---|---|
| Avg monthly revenue | €4 000 |
| Direct COGS/мес | €1 750 |
| Gross margin % | 56.3% ⚠️ (below 70% floor) |
| Allocated overhead/мес | €400 |
| Contribution margin/мес | €1 850 (46.3%) |
| Ruslan-hrs/€1K | **2.0 hrs** ✓ (best Phase-1) |
| CAC (organic+case study) | €2 500 |
| CAC (cold outreach) | €4 000 |
| LTV (avg 6-мес + renewal) | €36 000 |
| LTV:CAC (conservative) | 6.0:1 ✓ |
| Payback | 1 мес |

---

## §3.3 USB-C Integration Services — Unit-Econ

**Phase-A delivery model: Path-B (client-hosted methodology license).** Ack'd per L5 Q1 resolution [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#Q1-ack]. Path-B unit-econ = investor-critic KM-ARCH Dissent 3 70.7% GM yr1. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#Dissent-3 Position-B]

### Revenue structure (Path-B)

- Onboarding fee: €3 000 (one-time setup + methodology kit delivery + remote consulting during installation)
- Annual support retainer: €15 000/yr (quarterly check-ins + methodology version updates + support SLA)
- Year-1 combined: €3 000 + €15 000 = **€18 000**
- Year-2+: €15 000/yr renewal

### COGS yr1 (Path-B)

| Статья | Cost |
|---|---|
| Onboarding: Ruslan setup consulting | 8 hrs × €150 = €1 200 |
| Onboarding: compliance template preparation (GDPR fit statement, EU AI Act paragraph) | €500 (one-time write, amortized after 3rd client = €167 marginal) |
| Annual support: Ruslan time | 1 hr/мес × 12 × €150 = €1 800 |
| Annual support: methodology updates | 2 hrs/yr × €150 = €300 |
| Tooling allocation (compute, hosting docs) | €150/yr |
| **Total yr1 COGS** | **€3 950** |

**Gross margin yr1 (pre-overhead):**
- (€18 000 − €3 950) / €18 000 = **78.1% GM** → выше D18 флора ≥70% ✓

**Allocated overhead (10% revenue yr1):** €1 800

**Contribution margin yr1:** €18 000 − €3 950 − €1 800 = **€12 250 (68.1%)**

Это лучший contribution margin в абсолютном выражении среди всех Phase-A directions, несмотря на то что направление активируется G1→G2 (post-€50K).

**GM% yr2+:** (€15 000 − €2 100) / €15 000 = **86.0%** (COGS yr2 = только support hours + tooling, без onboarding amortization)

**F-G-R для 78.1% GM yr1:**
- F: F4 (substantive arithmetic; основан на KM-ARCH Dissent 3 investor projection 70.7% + уточнение COGS breakdown в этом расчёте)
- ClaimScope: Phase-A first 3-5 contracts; solo-Ruslan delivery; Path-B; без ISO 27001 сертификации (которая добавит €30-80K fixed cost при G2 gate)
- R: refuted если первые 2 deployments дают GM% <60% после полного COGS accounting (includin allocated overhead); receipt: `swarm/wiki/operations/clients/<slug>/financials.md`

### Ruslan-hours per €1K revenue (yr1)

Total Ruslan hours yr1: 8 (onboarding) + 12 (annual support × 1 hr/мес) + 2 (updates) = **22 hrs/yr**
Revenue yr1: €18 000

22 hrs / 18 = **1.2 hrs/€1K** → highly scalable zone (best ratio of all directions)

Это ниже уровня Продюсерского центра и является лучшим productization score в портфеле. Однако: Phase-1 volume = 1-2 clients (не productized yet). На масштабе 10+ clients Phase-2, ratio сохраняется или улучшается.

### CAC

- Warm referral (из consulting engagement к USB-C upsell): 3-5 hrs Ruslan (discovery → proposal). CAC = 4 hrs × €150 = **€600** (essentially free given consulting relationship)
- Cold Mittelstand outreach: 15-20 hrs/lead × €150 / 8% conversion = **€3 750-€4 700 per signed client** (sales cycle 6-12 недель Mittelstand)
- Target CAC structure: majority via consulting upsell path (warm), minority cold

**LTV:** 3-5 yr retention × €15 000/yr renewal = **€45 000-€75 000**. Mid-point €60 000.

**LTV:CAC:**
- Via consulting upsell: €60 000 / €600 = **100:1** (exceptional; near-zero acquisition cost)
- Cold outreach: €60 000 / €4 200 = **14.3:1** ✓

**Payback:** onboarding fee €3 000 received upfront. Payback = immediate on onboarding; retainer revenue from month 1.

### Summary table — §3.3 USB-C Integration Services

| Metric | Value |
|---|---|
| Revenue yr1 (Path-B) | €18 000 |
| Direct COGS yr1 | €3 950 |
| Gross margin % yr1 | **78.1% ✓** (above 70% floor) |
| Allocated overhead yr1 | €1 800 |
| Contribution margin yr1 | €12 250 (68.1%) |
| GM% yr2 (renewal only) | 86.0% ✓ |
| Ruslan-hrs/€1K (yr1) | **1.2 hrs** ✓ (best in portfolio) |
| CAC (consulting upsell) | €600 |
| CAC (cold) | €4 200 |
| LTV | €60 000 |
| LTV:CAC (upsell) | 100:1 ✓ |
| LTV:CAC (cold) | 14.3:1 ✓ |
| Payback | Immediate (upfront onboarding fee) |

---

## §3.4 Matchmaker Platform — Unit-Econ

Matchmaker проходит через 3 cadence-фазы с принципиально разной unit-econ на каждой. Все три анализируются отдельно.

### Phase-1: Manual Ruslan (G0→G1, €0→€50K)

**Revenue:** Zero прямых revenue. Matchmaker на Phase-1 = **network-building investment**, не profit center.

**Opportunity cost (economic COGS):** 5-10 hrs/мес Ruslan × €150 = €750-€1 500/мес economic cost. Это не денежный отток, но это forgone billable consulting revenue.

**Strategic ROI:** Каждый match создаёт relationship capital в specialist network. 1 good match ≈ 1-2 inbound consulting referrals за 12-18 мес. Если inbound consulting LTV = €22 500 (§3.1) и 10% leads конвертируются через Matchmaker channel → effective ROI of Matchmaker time = €22 500 × 10% / (€1 125 opportunity cost avg) ≈ **2:1 ROI** on time invested.

**Ruslan-hours per €1K revenue:** N/A Phase-1 (нет revenue line). Трактовать как customer acquisition investment, not separate direction.

### Phase-2: AI-Smoothed (G1→G2, €50K→€200K)

**Revenue model:** success-fee €500-€2 000 per match (mid-point €1 250); 10-20 matches/мес при AI-smoothed pipeline.

**COGS per match:**
- Ruslan review: 1 hr × €150 = €150
- Agent processing (compute): €10-20 per match
- **Total COGS per match: €170**

**GM% per match:** (€1 250 − €170) / €1 250 = **86.4%** ✓ (well above 70% floor)

**Ruslan-hrs/€1K:** 1 hr / (€1 250 / €1 000) = **0.8 hrs/€1K** → highest scalability ratio of any revenue-generating mode

**CAC:** Organic (aus consulting network); effectively €0 monetary — Ruslan time 2-3 hrs per specialist recruited into network. Network liquidity = # of active specialists × # of active task buyers; CAC per match ~ €0 once network reaches tipping point.

**LTV:** Platform (not per-match) — as network grows, Matchmaker LTV = sum of all future match fees. Estimate Year-2 platform: 20 matches/мес × €1 250 × 12 = €300 000 ARR with minimal marginal cost.

**LTV:CAC:** Network-effect business; at scale LTV:CAC → very high (100:1+). Phase-2 estimate: 5:1 minimum.

### Phase-3+: Platform (G2→G3, €1M→$100M)

**Revenue model:** take-rate 5-10% on matched-task value. Avg task value €5 000 → fee €250-€500 (mid €375). At 100 matches/мес: €37 500/мес = **€450K ARR**.

**COGS:** platform infrastructure (hosting, engineering amortized) ~20-30% at maturity → **GM% 70-80%** at scale.

**Summary table — §3.4 Matchmaker per Phase**

| Phase | Revenue model | GM% | Ruslan-hrs/€1K | LTV:CAC |
|---|---|---|---|---|
| Phase-1 (manual) | €0 direct | N/A | N/A (investment) | N/A |
| Phase-2 (AI-smoothed) | €1 250/match success-fee | 86.4% ✓ | 0.8 hrs ✓ | ≥5:1 ✓ |
| Phase-3+ (platform take-rate) | 5-10% task value | 70-80% ✓ | <0.5 hrs ✓ | 100:1+ ✓ |

---

## §3.5 Secure Network — Unit-Econ

**Phase activation:** G1→G2 architecture design; G2→G3 launch. Phase-1 = invite-list building (zero revenue). Unit-econ анализируется за Phase-2 (post-launch) state.

### Revenue structure (post-G2 launch)

Subscription tiers (placeholder; §2 owns final pricing):
- **Tier 1 (Basic):** €19/мес — access + складчина pool participation
- **Tier 2 (Active):** €49/мес — tools access + sub-networks + matchmaker priority
- **Tier 3 (Core):** €99/мес — full stack + 1:1 Ruslan session/quarter
- **Tier 4 (Elite):** €199/мес — enterprise access + custom onboarding

**Blended ARPU estimate (membership mix 60%/25%/10%/5%):**
60% × €19 + 25% × €49 + 10% × €99 + 5% × €199 = €11.4 + €12.3 + €9.9 + €10 = **€43.6/мес ARPU** [placeholder]

### COGS per member per месяц

| Статья | Cost |
|---|---|
| Platform hosting allocation | €2/member (Telegram-primary Phase-2 = near €0; Phase-3 dedicated = €2) |
| Moderation / curation (Ruslan + community managers) | 0.1 hrs × €50 = €5/member |
| Складчина tool-pool subsidy | €3/member avg |
| Content / events production | €2/member |
| **Total COGS/member/мес** | **€12** |

**GM% per member:** (€43.6 − €12) / €43.6 = **72.5%** ✓ (above 70% floor, marginally)

**Allocated overhead (10%):** €4.36/member

**Contribution margin:** €43.6 − €12 − €4.36 = **€27.2/member/мес (62.4%)**

**FLAG: GM% 72.5% marginal above floor.** При росте платформы (более дорогая инфраструктура Phase-3) COGS/member может вырасти до €15 → GM% падает до 65.6%. Мониторинг: engineering-expert должен держать hosting cost/member в envelope €2-3 на протяжении G2→G3.

### Ruslan-hours per €1K revenue

Community management Phase-2: ~20 hrs/мес Ruslan (curation + sessions + moderation oversight).
Revenue at 100 members × €43.6 ARPU = €4 360/мес.
20 hrs / 4.36 = **4.6 hrs/€1K** → borderline scalable; improves sharply при делегировании community management hired CM на G3.

### CAC

- Organic / referral: invite-only from consulting + producer clients. CAC ≈ €0 monetary; Ruslan time 1-2 hrs per recruited member = €150-300.
- Referral discount механизм (per L5 §3.5 описание): -20% первого месяца за referral → incentivizes viral growth без cash CAC.
- **CAC estimate: €200 (Ruslan time) + €10 (referral discount cost)**

**LTV:** avg €43.6/мес × 18 мес avg retention = **€785/member**

**LTV:CAC:** €785 / €210 = **3.7:1** ✓ (above 3:1 floor, but tight)

**Payback:** Monthly subscription, prepaid. Payback = 5 месяцев (€200 CAC / €43.6 ARPU).

**FLAG: LTV:CAC 3.7:1 — barely above floor.** Это требует удержания retention >18 мес. Если churn растёт → LTV падает → LTV:CAC может уйти ниже 3:1. Мoniтoринг: 6-month retention cohort review после launch.

### Summary table — §3.5 Secure Network

| Metric | Value |
|---|---|
| ARPU blended | €43.6/мес |
| COGS/member/мес | €12 |
| Gross margin % | 72.5% ✓ (marginal) |
| Allocated overhead | €4.36/member |
| Contribution margin | €27.2/member/мес (62.4%) |
| Ruslan-hrs/€1K | 4.6 hrs (Phase-2); improves G3 |
| CAC | €210 |
| LTV (18 мес avg) | €785 |
| LTV:CAC | **3.7:1 ⚠️** (borderline) |
| Payback | 5 мес |

---

## §3.6 YouTube-Analyzer SaaS — Unit-Econ

**Phase:** G3→G4 деferred (Phase-3+). Phase-1/Phase-2 = N/A as SaaS. Phase-2 preparatory: manual YouTube analysis kit (€2K-€5K per engagement = consulting delivery).

### Phase-2: Manual Kit (G2 preparatory)

**Revenue per engagement:** €3 500 mid-point (between €2K-€5K).
**COGS:** 4-8 hrs Ruslan × €150 + agent processing €50 = €650-€1 250. Mid: €950.
**GM%:** (€3 500 − €950) / €3 500 = **72.9%** ✓
**Ruslan-hrs/€1K:** 6 hrs / 3.5 = **1.7 hrs/€1K** → scalable ✓

### Phase-3: SaaS (G3→G4)

Avg seat: €99/мес (blended tiers €49/€99/€299). At 500 seats (G3 launch milestone): €49 500/мес ARR.

**COGS SaaS:**
- YouTube API quotas + data pipeline: €0.05/query × 10K queries/мес = €500
- Hosting + infrastructure: €800/мес (G3 scale)
- Customer success + support: €2 000/мес (dedicated 0.5 FTE)
- **Total COGS: €3 300/мес at 500 seats**
- COGS/seat: €6.6/мес

**GM% SaaS at 500 seats:** (€49 500 − €3 300) / €49 500 = **93.3%** → excellent, Phase-3 target
**CAC SaaS:** content marketing + product-led growth → €200-500/seat. Payback: 2-5 мес.
**LTV SaaS:** €99 × 24 мес avg = €2 376. LTV:CAC = €2 376 / €350 = **6.8:1** ✓

**Ruslan-hrs/€1K (SaaS Phase-3):** nearly 0 (SaaS is self-serve; Ruslan role = strategic direction only). <0.2 hrs/€1K → best-in-portfolio when live.

### Summary — §3.6 YouTube-Analyzer

| Phase | Revenue model | GM% | Ruslan-hrs/€1K | LTV:CAC |
|---|---|---|---|---|
| Phase-2 manual kit | €3 500/engagement | 72.9% ✓ | 1.7 hrs ✓ | N/A (one-off) |
| Phase-3 SaaS | €99/мес avg seat | 93.3% ✓ | <0.2 hrs ✓ | 6.8:1 ✓ |

---

## §3.7 Educational + Investor Programs + Grant Hunting — Unit-Econ

Три sub-трека с различной unit-econ структурой.

### Sub-A: Cohort-first (G2→G3 activation, per L5 Q4 ack)

**Revenue per cohort:** 10 learners × €5 000 avg cohort fee = **€50 000 per cohort**
[placeholder; §2 owns final pricing; per L5 ack Q4 «NPS>40 + margin>€3K/learner»]

**COGS per cohort:**
| Статья | Cost |
|---|---|
| Ruslan instruction | 30 hrs × €150 = €4 500 |
| Platform (Teachable / Notion / custom) | €1 000 per cohort |
| Materials production (slides, exercises, recordings) | €500 first run; €0 repeat |
| **Total COGS** | **€5 500 first cohort / €5 000 repeat** |

**GM% first cohort:** (€50 000 − €5 500) / €50 000 = **89.0%** ✓ (excellent; matches L5 ack Q4 «margin>€3K/learner» → actual €4 450/learner)

**Allocated overhead (10%):** €5 000

**Contribution margin per cohort:** €50 000 − €5 500 − €5 000 = **€39 500 (79.0%)**

**Ruslan-hrs/€1K:** 30 hrs / 50 = **0.6 hrs/€1K** → best cohort metric in portfolio

**CAC cohort:** audience-first via consulting brand → €0 monetary; Ruslan time 5 hrs per learner enrolled (outreach + qualification). Effective CAC = 5 hrs × €150 / 10 learners = **€750 per cohort place**.

**LTV cohort learner:** €5 000 (cohort) + €2 000 avg upsell (mentoring / self-serve follow-on) = **€7 000**.

**LTV:CAC:** €7 000 / €750 = **9.3:1** ✓

### Sub-B: Self-Serve (G3→G4, min per L5 Q4 ack)

Revenue per seat: **€1 000 avg** (between €500 basic course and €2 000 premium).
COGS: platform €50/seat (hosting + delivery) + Ruslan time €50 (async Q&A). Total COGS: €100/seat.
**GM%:** (€1 000 − €100) / €1 000 = **90.0%** ✓
**Ruslan-hrs/€1K:** 0.3 hrs → highly scalable
CAC: content marketing / inbound → €100-200/seat. LTV = €1 000. LTV:CAC = 5-10:1 ✓

### Sub-C: Grant Hunting

Success-fee 5-10% × grant size. EU innovation grants: €100K-€1M typical.
Revenue range per success: **€5 000-€100 000**.
COGS: 20-100 hrs Ruslan (research + application writing + partner coordination) × €150 = €3 000-€15 000.
**GM%:** (€52 500 mid − €9 000 mid) / €52 500 = **82.9%** mid-case. High variance.
**Ruslan-hrs/€1K mid:** 60 hrs / 52.5 = **1.1 hrs/€1K** — but variance wide; best case 0.3, worst case 5.0.

FLAG: Grant hunting — **высокий variance, длинный payback (3-12 мес cycle)**. Treat as R&D allocation, not reliable revenue line. Maximum 10-15% Ruslan time budget Phase-2.

### Summary table — §3.7 Educational

| Sub-track | Revenue per unit | GM% | Ruslan-hrs/€1K | LTV:CAC |
|---|---|---|---|---|
| Cohort (10 learners) | €50 000 | **89.0% ✓** | 0.6 hrs ✓ | 9.3:1 ✓ |
| Self-serve (per seat) | €1 000 | **90.0% ✓** | 0.3 hrs ✓ | 5-10:1 ✓ |
| Grant hunting (avg success) | €52 500 mid | 82.9% ✓ (high var) | 1.1 hrs avg | N/A |

---

## §3.8 Tokens / ICO D23 — Unit-Econ

**N/A — Phase-1 and Phase-2.** D23 Option B установил explicit $100K self-earned trigger для Phase-2 internal utility, Phase-3+ public layer. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.8 + D23 ack Q5]

Unit-econ analysis для Tokens не проводится в этом разделе по следующим основаниям:
1. **Pre-revenue:** в Phase-1/2 токен-экономика не генерирует прямого revenue → unit-econ не применимо
2. **Regulatory uncertainty:** MiCA (EU) и Howey test (US) делают любую unit-econ модель conditional на юридическую структуру, которая будет определена в Phase-3 cycle
3. **Tokenomics ≠ unit-econ:** pricing power токена определяется network effects + regulatory framework, не COGS/margin структурой. L7 §2 (pricing sibling) также defers tokens

**Retirement clause preserved:** если consulting + educational + USB-C генерируют $100M ARR без specialist-friction → D23 deprecation acked per L5 Q5. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3 L5 acked]

**F-G-R для N/A статуса:**
- F: F5 (аналитический; D23 explicit defer trigger + regulatory analysis)
- ClaimScope: Phase-1 and Phase-2 only; Phase-3 unit-econ cycle re-opens when trigger fires
- R: re-open unit-econ analysis when $100K self-earned AND initial regulatory counsel obtained; receipt: `swarm/wiki/tasks/T-tokens-unit-econ-phase-3-<date>/`

---

## §3.9 Smart AI — Unit-Econ

**N/A — нет unit-econ по дизайну.** Smart AI = внутренний нарративный label для всего портфеля, не внешний продукт и не D29 lock. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.1 Direction 9]

Ruslan explicit: «ну типа запиши между прочим но нет это ещё не лок блять забей хуй» [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]. Нет pricing, нет revenue line → unit-econ N/A.

Роль Smart AI в контексте §3: это **positioning narrative**, который влияет на **CAC других направлений** (Matchmaker, Consulting, Producer center) через брендинг-дифференциацию. Влияние косвенное: более сильный narrative → выше conversion rate → ниже effective CAC. Но это не измеримая unit-econ до Phase-2 A/B теста (Δ ≥15% outreach response rate + clarity ≥20% per L5 Q3 trigger criteria).

---

## §3.10 Cross-Direction Ruslan-Hours Rationing

### Available capacity

Phase-1: 30-40 hrs/нед total Ruslan. Allocation:
- Billable delivery (consulting + producer): 20-25 hrs/нед
- Outreach + sales: 5-8 hrs/нед
- System building / agents / infra: 5-8 hrs/нед
- Admin / finance / legal: 2-3 hrs/нед

**Ceiling:** €50K gate arithmetic из CC-1 [src:decisions/JETIX-PLAN.md#§3.1.1]: 233 hourly consulting hours over Q1+Q2 = ~9 hrs/нед + 4 productized engagements (30 hrs each) = 60 hrs total over 2 quarters = ~2.3 hrs/нед. Total Phase-1 delivery load: ~11 hrs/нед minimum delivery-only. Production center: 8 hrs/мес = 2 hrs/нед.

### Productization scoring (Ruslan-hours per €1K revenue, ranked)

| Rank | Direction | Hrs/€1K | Scalability |
|---|---|---|---|
| 1 | USB-C Integration Services (Path-B) | 1.2 hrs | ✓✓ Highly scalable |
| 2 | Educational (Cohort) | 0.6 hrs | ✓✓ Best-in-class |
| 3 | Educational (Self-serve) | 0.3 hrs | ✓✓ Best-in-class |
| 4 | Matchmaker Phase-2 (AI-smoothed) | 0.8 hrs | ✓✓ Highest scalability |
| 5 | Продюсерский центр | 2.0 hrs | ✓✓ Scalable |
| 6 | YouTube-Analyzer (manual kit) | 1.7 hrs | ✓ Scalable |
| 7 | AI Consulting (productized 4-pack) | 4.0 hrs | ✓ Borderline |
| 8 | AI Consulting (hourly) | 6.7 hrs | — Normal Phase-1 |
| 9 | Secure Network (Phase-2) | 4.6 hrs | — Borderline (improves G3) |
| 10 | Grant Hunting | ~1.1 hrs avg | ⚠️ High variance |

**Ключевой вывод: USB-C + Educational + Matchmaker Phase-2 — наиболее scalable направления по productization score.** Они максимизируют revenue per Ruslan-час. Consultion (hourly) + Secure Network — наиболее founder-intensive Phase-1. Это подтверждает D18 roadmap: приоритизировать productization consulting → USB-C / Educational upsell.

**Allocation heuristic Phase-1:**
- Maximize billable consulting hours (hourly = working capital for productization)
- Maximize productized engagement pipeline (4-pack)
- Guard 2-3 hrs/нед для Matchmaker relationship building (low cost, high network leverage)
- Producer center: 8 hrs/мес Ruslan floor (minimum to run 1-2 pilot clients)
- USB-C: 22 hrs/yr per client (negligible weekly impact)

---

## §3.11 Compute Cost Allocation

**Fixed cost:** Anthropic Max subscription + Groq voice processing = €200-400/мес, mid-point **€300/мес = €3 600/yr**.

**Phase-1 allocation (2 active revenue directions):**
- §3.1 AI Consulting: €150/мес (50%)
- §3.2 Продюсерский центр: €150/мес (50%)
- Rationale: оба равно revenue-primary Phase-1; consulting использует agents для research + KB; producer использует voice pipeline + agents для production

**Phase-2 allocation (4-5 active directions):**
- Allocate proportionally to revenue contribution:
  - Consulting 35% → €105
  - Producer 25% → €75
  - USB-C 20% → €60
  - Matchmaker 10% → €30
  - Secure Network 10% → €30

**Impact on GM% per direction:**
- §3.1 Sub-A: tooling COGS €150/мес ÷ ~2 engagements/мес = €75/engagement → влияние на GM% незначительное (<1% shift)
- §3.2: tooling COGS €150/мес ÷ 2 producer clients = €75/client/мес → уже включено в COGS §3.2 (€50/мес там) → minor rounding

**Compute cost allocated and documented.** Не является значимым margin driver на Phase-1 scale; становится операционно заметным при Phase-3+ масштабе (если monthly compute превысит €2K → переосмыслить allocation модель).

---

## §3.12 Cross-Section Reconciliation Note

### Связь с §2 (Pricing)

Все revenue figures в §3 являются **placeholders привязанными к §2 sibling cell** (pricing cell, Wave-A). При integration pass:
- Если §2 скорректирует productized consulting engagement price (например, с €7 500 до €10 000) → §3.1 GM% Sub-A вырастет с 38% до 50%
- Если §2 установит producer retainer avg ≥€5 000 (вместо €4 000 mid) → §3.2 GM% вырастет с 56% до ≥60%
- USB-C Path-B: §2 pricing sibling должен confirm €3 000 onboarding + €15 000/yr или сдвинуть; §3.3 пересчитывается

**Integration flag:** §3 unit-econ не финализирован до §2 integration pass. Brigadier должен обеспечить sequential integration pass §2 → §3 reconciliation перед canon promotion.

### Связь с §7 (Cash Flow)

- **Contribution margins из §3 → monthly P&L в §7**: §3.1 Sub-A: €2 100/contract × 2 contracts/мес = €4 200/мес contribution; §3.2: €1 850/client × 2 clients = €3 700/мес. Phase-1 monthly contribution (consulting + producer) ≈ €7 900 против overhead €300 compute + €1 000 est fixed ops = **≈€6 600 net/мес Phase-1 at capacity**
- CAC cash outflow из §3 → cash flow timing в §7 (CAC = pre-revenue period; payback aligned к retainer/engagement cash receipt)

### Связь с §11 (Risk Register)

Из §3 следуют risk rows для §11:
1. **GM% below floor on Consulting Sub-A (38%):** risk = если прайс не вырастет или productization не случится на G2 → margin compression при scale → RISK-UNIT-ECON-001
2. **LTV:CAC Secure Network borderline (3.7:1):** risk = churn >6 мес avg → LTV:CAC <3:1 → RISK-UNIT-ECON-002
3. **Hourly consulting negative contribution (−€15/hr overhead allocated):** risk = high hourly volume without productization → gross revenue up but contribution flat → RISK-UNIT-ECON-003
4. **Ruslan-hours ceiling (40 hrs/нед):** risk = если consulting + producer + USB-C + Matchmaker sum hours exceed ceiling → quality degradation → RISK-UNIT-ECON-004

---

## §X Cell C-02 Self-Improvement Notes

Паттерны для compound в `agents/investor-expert/strategies.md`:

**Pattern INV-COMPOUND-001: Ruslan-hours per €1K = первичная productization scoring метрика.**

Threshold scheme: ≤5 hrs/€1K = scalable (автоматизация достаточна для growth без founder-bottleneck); 5-15 hrs/€1K = нормальная Phase-1 (productization roadmap needed); >15 hrs/€1K = founder-bottleneck ceiling (либо contractor decoupling, либо deprioritization). Эта трёхзонная схема должна войти в шаблон каждого capital-allocation-memo как mandatory metric. Без этого числа memo не проходит C1 critic check на owner-earnings уровне для solo-founder businesses.

**Pattern INV-COMPOUND-002: GM% ниже D18 флора (≥70%) не автоматически = fail; требует trajectory justification.**

Consulting Sub-A на Phase-A имеет 38% GM, но это объяснимо founder-heavy delivery. Инвестор-критик не должен flat-reject такой memo — он должен запросить trajectory к ≥70% GM с explicit gate-trigger. Правило: GM% < флора → обязательно присутствует "Trajectory to GM floor: [Phase] [Gate] [Mechanism]" section в memo. Без trajectory — fail C2.

**Pattern INV-COMPOUND-003: LTV:CAC < 4:1 при borderline = early warning, не kill-condition Phase-1.**

Secure Network 3.7:1 — это warning, не rejection. Phase-1 borderline LTV:CAC может быть ОК если retention data отсутствует (нет empirical base rate); должен стать kill-condition только после 2 cohort cycles дают <3:1 empirically. Правило: для pre-revenue directions LTV:CAC < 3:1 threshold применяется только после первых 2 empirical cohorts, не на model estimate.
