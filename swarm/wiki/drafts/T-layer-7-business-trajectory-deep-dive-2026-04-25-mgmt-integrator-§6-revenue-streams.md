---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§6-revenue-streams
title: "§6 Revenue Streams Ranking + Portfolio Diversification"
type: cell-draft
cell: C-04
expert: mgmt-expert
mode: integrator
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 1500-2000
sources:
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§2 Portfolio overview + §3.1-§3.9 direction sections + §13 Evolution"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§2.1 Client ICP + §11 Evolution table"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1.1 revenue-mix CC-1 + §5 Phase 2 actions + §6 Phase 3"}
  - {path: "decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md", range: "§3 M&A direction + deferred status note"}
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§3 L6+L5 acked inputs + §4 28 Locks alignment"}
provenance_inline: true
acceptance_test: pass
---

# §6 Revenue Streams Ranking + Portfolio Diversification

> **Cell C-04 — mgmt-expert × integrator.** Этот раздел ранжирует потоки выручки Jetix по фазам (Phase-1, Phase-2, Phase-3+), устанавливает пороги концентрации и описывает диверсификационную логику портфеля в терминах, аналогичных портфельному Sharpe-thinking. Раздел потребляет §2 ценообразования (L7 owner) и §13 evolution из L5 как входные данные — он не пересматривает pricing arithmetic, а использует уже зафиксированные диапазоны как ориентиры структуры потоков. Сноска на §7 cash flow и §11 risk register внутри документа явная.

---

## §6.0 Фрейминг — что такое revenue stream и почему portfolio matters

**Revenue stream** — это дискретный канал поступления денег, идентифицируемый по паре (продукт/услуга × механика оплаты). Два потока от одного клиента — разные revenue streams, если механика оплаты различается (например: retainer-контракт vs success-fee). Понятие stream принципиально отличается от понятия direction (L5 §2): одно направление (например, AI Consulting) может порождать несколько streams (hourly overflow + productized package + retainer).

**Portfolio** — набор активных revenue streams в текущей фазе. Задача портфеля — не максимизировать один поток, а обеспечить устойчивый совокупный доход через баланс коррелированных и антикоррелированных источников. [src:decisions/JETIX-PLAN.md#§1 Plan Overview]

**Concentration risk** — ситуация, при которой один клиент или один stream генерирует долю, достаточную для того, чтобы его потеря угрожала cash-flow всей фазы. Threshold определён в L6 §2.1: **ни один клиент не должен превышать 30% общей фазовой выручки**. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1] Это операционный закон, а не ориентир.

**Claim §6.0-C1:**
- F: F4 (операционная конвенция, закреплённая в L6 ack)
- ClaimScope: действует для Phase-1 solo-operator; применимость к Phase-3+ multi-BU требует уточнения (threshold может быть тоньше)
- R: опровергается, если единственный крупный клиент не уходит в Phase-1 (risk never materalised) — но это ex-post; accepted как architecture constraint a priori

---

## §6.1 Phase-1 (€0 → €50K Q2 2026) — ранжирование потоков

### Первичные потоки (≥40% каждый)

**Phase-1 Revenue Mix (ack'd CC-1 per KM-Mat-MVP investor audit):**

| Stream | Объём | Цена | Выручка Q1+Q2 |
|---|---|---|---|
| Productized contracts (Path-B) | 4 contract-quarters (2 × 2Q) | €7 500/contract-quarter | €30 000 |
| Hourly consulting (4-pack "конкретная помощь" + discovery) | 233 часа | €150/час [audio_452] | €35 000 |
| **Итого (gate: €50K)** | | | **€65 000 (~30% margin)** |

[src:decisions/JETIX-PLAN.md#§3.1.1]

**AI Consulting (productized contracts + hourly overflow) — ~100% Phase-1 cash-flow в узком смысле.** Подробнее: productized sub-stream даёт €30K (~46% от €65K ceiling), hourly sub-stream — €35K (~54%). Оба принадлежат одному направлению (Direction 1 — AI Consulting), но имеют разные mechanics и разный операционный риск:

- **Productized contracts (Path-B default per L5 Q1 ack):** GM 70.7% [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#frontmatter brigadier_top5_ack_recommendations]. Риск: медленный sales cycle (6–12 недель). Защита: если 2 контракта/квартал не закрываются, весь €30K plan рушится — hourly становится критическим.
- **Hourly consulting:** более ликвидный, быстрее конвертируется из discovery-звонков. Риск: hours-ceiling (Ruslan — единственный deliverer; физически ограничен ~20 часов/неделю billable). [src:decisions/JETIX-PLAN.md#§3.1.1 implication: ≥20 hours/week]

**Продюсерский центр (pilot) — co-primary, внутри Phase-1 ceiling.** Pilot format: 1-2 клиента × retainer €4K/мес × 6 мес ≈ €24K потенциал. Перекрывается с consulting ICP (Блогер + Startupper — один outreach motion приводит к обоим). [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1 Sub-prioritization] Важно: Продюсерский центр **входит** в общий €65K ceiling как вторая активная линия — не добавляется к ней. При расчёте доли в портфеле нужно рассматривать суммарно.

**Claim §6.1-C1 (Phase-1 primary streams):**
- F: F4 (операционная конвенция, закреплённая в CC-1 ack)
- ClaimScope: действует для Phase-1 Q1+Q2 2026 solo-operator; не действует без ≥20 часов/неделю billable capacity
- R: опровергается, если productized contract pipeline < 2/квартал AND hourly < 15 часов/неделю устойчиво → €50K gate не достигается

### Вторичные потоки (5–20% Phase-1)

**Matchmaker incidental:** €0 прямого revenue в Phase-1. Функция: leverage для acquisition consulting-клиентов (Ruslan вручную коннектирует людей → trust building → referrals → consulting leads). [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.5 P1B opportunistic referral] Считается secondary lever, не revenue stream в Phase-1.

**USB-C early-access (P1B opportunistic):** первый клиент возможен как opportunistic, не как планируемый target. Path-B unit economics при случайном первом клиенте: €3K-€10K/мес engagement. Не включается в €65K baseline — учитывается как upside buffer.

**Hourly overflow (уже в primary):** почасовые discovery-сессии уже захвачены в основном hourly-stream. Дублирования нет.

### Concentration thresholds — Phase-1

**Правило №1 (L6 §2.1 verbatim):** ни один клиент > 30% общей Phase-1 выручки. При target €50K это означает: ни один клиент > €15K суммарно за Phase-1. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1]

**Следствие (количественное):** при средней величине контракта ~€7.5K/квартал (Path-B), минимальный «безопасный» портфель требует ≥4-5 активных клиентов. Один productized contract + остальное hourly = 1 клиент potentially >30% → структурный риск концентрации. Решение: диверсифицировать hourly across 3-5 clients, а не одним большим engagement.

**Правило №2 (mgmt-inferred от структуры):** ни один direction > 70% выручки в Phase-1. Поскольку оба primary (consulting + producer) активны с P1A outreach, target — 45-55% balance между ними. Если producer pilot не стартует в Q1 → consulting = 100% → direction-concentration risk.

**Claim §6.1-C2 (concentration thresholds):**
- F: F4 (L6 §2.1 ack'd + mgmt-inferred arithmetic)
- ClaimScope: Phase-1 solo-operator €50K gate; threshold 30% = hard rule из L6
- R: опровергается только если Ruslan явно пересматривает L6 §2.1 в HITL-гейте; принят как binding constraint

---

## §6.2 Phase-2 (€50K → €200K → €1M) — ранжирование потоков

### Gate 1 (€50K → €200K) — validation window

**Primary: AI Consulting (declining %)** остаётся крупнейшим stream, но его доля снижается по мере появления новых потоков. Consulting эволюционирует: hourly → retainer → productized managed service (D18 productization path). [src:decisions/JETIX-PLAN.md#§4.1]

**Primary: Продюсерский центр (growing %)** становится main revenue driver начала Phase-2 ([src:decisions/JETIX-PLAN.md#§5.5]): productized fully (D18). 1-2 → 3-5 retainer clients at €4K-€8K/мес = €12K-€40K/мес ceiling. По мере появления hire #1 (sales) продажи ускоряются.

**Новые streams, запускаемые в Phase-2:**

| Stream | Механика | Примерный размер (placeholder) | Gate |
|---|---|---|---|
| Subscription — Secure Network складчина | Subscriptions €200-€500/мес × growing membership | Starts post-G3 (€1M) — BUILIDING at G2 | G2→G3 architecture design, G3 launch |
| Path A/B/C USB-C contracts | Retainer €3K-€20K/мес per Path | First client G1→G2 transition opportunistic; productized at G2 | G1→G2 |
| Educational cohort | €50K per cohort (€3K-€8K × 15-20 learners), 1-2 cohorts/quarter at G2→G3 | Target: €50K/cohort × 2/quarter = €100K/quarter | G2→G3 (NPS>40 + margin>€3K/learner gate) |
| Matchmaker AI-smoothed fees | €500-€2K per match | Small but growing; Phase-2 product form at G2 | G1→G2 AI-smoothed |

[src:decisions/JETIX-PLAN.md#§5.5; decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.5; swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3]

**Важная оговорка — Secure Network:** согласно L5 §2.5 и JETIX-PLAN §4.4, Secure Network build starts после €200K validation gate. Subscribe revenue появляется **только post-G3** (€1M). В окне G2 (€50K-€200K) это invite-list, не revenue stream. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.5 P1B]

### Concentration thresholds — Phase-2

- Ни один клиент > 25% total Phase-2 revenue
- Ни один direction > 50% total revenue к G2 (€200K)
- Ни один direction > 40% total revenue к G3 (€1M)

По мере появления educational cohort + matchmaker fees + USB-C contracts, consulting+producer как пара должна опуститься ниже 50% совокупной выручки к концу Phase-2.

**Claim §6.2-C1 (Phase-2 new streams onboarding):**
- F: F3 (паттерн наблюдаемый в аналогичных consulting-to-platform transitions; не верифицирован на Jetix Phase-1 данных)
- ClaimScope: Phase-2 solo→managed-team; holds for consulting-motion с productization (D18); NOT valid для pure-SaaS transition (другая динамика)
- R: опровергается, если educational cohort NPS<40 или margin<€3K/learner после первых 2 cohorts — тогда cohort revenue stream не масштабируется и должен быть tombstone'd per §3.10 Q4 ack

---

## §6.3 Phase-3+ ($1M → $100M → $1T) — ранжирование потоков

На этом горизонте портфель трансформируется: services-heavy → methodology+subscription+asset-driven.

### Первичные потоки Phase-3+

**Methodology licensing royalties (D27 Fork-and-Merge):** Practitioners (co-consultants, roys) платят за лицензию методологии и участие в Alliance ecosystem. Два ценовых уровня: practitioner €500-€5K/год; co-consultant network revenue-share (% от их выручки, generated через Jetix methodology). D27 fork-and-merge governance: лучшие форки возвращают улучшения upstream → методология улучшается за счёт сети. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.7 Educational + Licensing]

**Secure Network subscription (membership tiers):** Post-G3 launch: €200-€500/мес basic; premium tiers выше. При 1000-5000 members (G4 cardinality per L6 §11): €200K-€2.5M/мес subscription ceiling. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11 Evolution table G4]

**USB-C standard-layer (Alliance dues + Path A managed hosting):** Alliance membership dues (Foundation operating fees); Path A managed hosting subscriptions (enterprise clients, recurring €5K-€20K/мес). По мере роста Alliance — сетевой эффект увеличивает и базу, и ARPU. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.3 USB-C §5 Offer structure]

**Educational license tier:** Methodology repo v1 (Apache 2.0 free → commercial license tier); certified consultant program (Phase-3+, G3→G4); institutional educational licenses (€500-€5K/год). По оценке: 12+ paid cohorts до запуска certification per §3.7 Q5. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.7]

### Вторичные / опциональные потоки Phase-3+

**Token economy (D23 Option B) — IF launched:**  
Per Ruslan Q5 ack (2026-04-25): preserve optionality; retirement clause triggers if consulting/educational/USB-C fund growth without specialist-friction AND MiCA/Howey legally prohibitive. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3] Если токен запущен: ecosystem service payments denominated in JCU; specialist compensation; складчина tool-pooling внутри Secure Network. Активация: Phase-3 ($100K self-earned internal utility trigger); public layer Phase-3+ ($100M). НЕ автоматический — retirement clause явный. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.8]

**Claim §6.3-C1 (Token optionality):**
- F: F3 (conditional on regulatory clarity + self-funded growth + specialist-friction materialization)
- ClaimScope: Phase-3+; NOT valid for Phase-1/2; conditional on D23 retirement clause NOT firing
- R: опровергается (token retired), если consulting+educational+USB-C достигают $100M ARR без specialist-compensation friction → D23 deprecation per LOCKS-D23-DEPRECATION

**Holding investment returns (D11 + D19):** Equity в roys; Kelly portfolio multi-roy. Phase-3+ по мере формирования holding structure. [src:decisions/JETIX-PLAN.md#§6 Phase 3] Механика: investment-fund philosophy (D11) — Ruslan allocates capital в roys (подтверждённые методологические ответвления); holding returns — dividends/equity appreciation. Timeline: $1M gate (Phase-3 start) → holding structure formalized per JETIX-PLAN §6.

**M&A Advisory (Phase-2+ optionality — brief mention only):**  
Per Ruslan 25.04 directive: деferred to Phase-2+; NOT Phase-1 priority. [src:decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md#deferred-status-note] Если активирован при €200K validation AND co-founder secured: success-fees €1-2M per Mittelstand mid-market deal (€30-50M EV × 2-4%). Bimodal revenue profile: **€1-2M если mandate closes; €0 если retainer-only без close**. Dedicated deep-dive cycle when Ruslan re-prioritizes.

**Claim §6.3-C2 (M&A optionality):**
- F: F2 (единственный источник — Wall Street research + Ruslan brief verbatim 25.04; no Phase-1 data)
- ClaimScope: Phase-2+ only if co-founder secured + DACH geography active; NOT Phase-1
- R: опровергается (M&A retired), если 6-18 месячный sales cycle делает M&A несовместимым с Phase-2 cash-flow runway; принят как upside optionality item

---

## §6.4 Diversification Logic — Portfolio Sharpe-Equivalent

Классический Sharpe ratio максимизирует return при заданной волатильности. В отсутствие достаточной Phase-1 статистики прямой расчёт невозможен, но структурная логика применима: **какие потоки коррелируют (падают одновременно), а какие антикоррелируют (стабильны в рецессию)**.

### Correlation matrix (качественная)

**Группа A — проциклические (B2B AI services demand):**
- AI Consulting (productized + hourly)
- Продюсерский центр retainers
- USB-C Integration Services contracts (Path A/B/C)

Корреляция: все три привязаны к discretionary B2B spend. В рецессию Mittelstand сокращает consultancy бюджеты первыми. DACH recession risk 2026-27 (R-15 risk, L7 §11 owner) — прямо ударяет по этой группе. Одновременное снижение всех трёх создаёт worst-case cash-flow gap.

**Группа B — мягко-коррелированные (resilient, но не immune):**
- Educational cohort (demand shifts в рецессию: люди переобучаются)
- Subscription Secure Network (низкий ticket = meньше churn в рецессию чем enterprise contracts)

Эти два потока устойчивы к мягким рецессиям. В глубокой рецессии discretionary learning тоже сжимается, но позже и менее драматично чем B2B services.

**Группа C — антициклические (lagging или counter-cyclical):**
- Methodology licensing royalties (once launched: инфраструктурный тип revenue — платят, пока используют методологию; перестают только при bankcruptcy или смене стека)
- Holding investment returns (диверсифицированы по рояльным портфелям; если Kelly-disciplined — не коррелируют с DACH SMB cycle напрямую)

**Группа D — некоррелированные (own cycle):**
- Token economy (IF launched): crypto market имеет собственный цикл, не коррелирующий с DACH SMB recession. Может быть positive в рецессию (риск-аппетит к альтернативным активам) или negative (risk-off). Не управляемая корреляция — чистая некоррелированность.

**Claim §6.4-C1 (diversification analysis):**
- F: F3 (структурная аналогия с известными паттернами B2B services + SaaS; не эмпирические данные Jetix)
- ClaimScope: holds для DACH market context + solo-founder Phase-1/2; NOT valid для US market где B2B spend менее cyclical чем в Германии
- R: опровергается, если Phase-1 empirical data покажет, что consulting churn в DACH recession < 20% (тогда группа A более stable чем структурно ожидается)

### Diversification targets per phase

| Phase | % Anti-cyclic streams в портфеле | Почему |
|---|---|---|
| Phase-1 | ~0% (no anti-cyclic streams operational yet) | Вынужденно: subscription/licensing не запущены |
| Phase-2 (G2) | 15-25% (subscription early + educational) | Первые anti-cyclic streams появляются |
| Phase-3 (G3) | ≥30% (subscription + educational + licensing early) | Трёхпотоковая база |
| Phase-3+ | ≥40% (full anti-cyclic portfolio operational) | Целевой уровень устойчивости |

**Главный вывод Phase-1/2:** Jetix вынужден оставаться проциклическим на ранних фазах — нет выбора. Единственная защита = **клиентская диверсификация** (concentration threshold <30% per client) и **geographic diversification** (English+US primary, DACH secondary — рецессии не синхронны). [src:decisions/JETIX-PLAN.md#§1 Geographic rollout]

---

## §6.5 Concentration Risk Thresholds per Phase

| Metric | Phase-1 | Phase-2 | Phase-3 | Phase-3+ |
|---|---|---|---|---|
| Single client max | <30% total revenue | <25% total revenue | <15% total revenue | <10% total revenue |
| Single direction max | <70% (consulting+producer pair jointly active) | <50% к G2; <40% к G3 | <35% | <30% |
| Single roy (Phase-3+) | n/a | n/a | <30% roy portfolio | <20% |
| Single stream max (Phase-3+) | n/a | n/a | <35% | <30% |

[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1 single-client >30% threshold; decisions/JETIX-PLAN.md#§3.10 exit criteria "portfolio diversified"]

**Phase-3+ balance target:** methodology + subscription + token (if active) + roy returns — равномерное распределение между Группами A, B, C per §6.4.

**Операционное следствие Phase-1:** если к M1.2 (€20K) все деньги получены от одного клиента → триггер для немедленной диверсификации outreach. Это не просто бизнес-риск — это нарушение concentration threshold, который является **acceptance condition** Phase-1 exit criteria.

---

## §6.6 Phase-1 → Phase-2: Sequencing — как новые потоки onboard'ятся

Новые revenue streams не должны разбавлять Phase-1 capacity. Sequencing следует из D15 (revenue-gated spend) и D18 (productization path):

**Шаг 1 — Secure Network invite-list (G1, €50K):** Не revenue stream — pre-enrollment. Первые 5-20 high-quality contacts. Zero spend. Build в Phase-1 = нет. Revenue = нет. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§2.5]

**Шаг 2 — USB-C first client (G1→G2 transition):** Path A/B/C первый contract opportunistic (P1B). Не планируемый outreach target — появляется если consulting engagement естественно растёт до managed-methodology scope. Unlock trigger: первый контракт >€30K+GDPR-audit (Path-C override per L5 Q1). [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3 L5 acked inputs]

**Шаг 3 — Matchmaker AI-smoothed (G1→G2):** При первом hire (sales), Ruslan передаёт manual matchmaking на AI-smoothed layer. Fees начинают появляться но остаются небольшими (€500-€2K/match). Net-new stream, не замена consulting.

**Шаг 4 — Educational cohort первый (G2→G3):** ТОЛЬКО после Secure Network architecture design завершена. Первый paid cohort = методология достаточно стабильна для обучения. Acceptance gate: NPS>40 + margin>€3K/learner. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3]

**Шаг 5 — Secure Network subscription launch (G3, €1M):** Первые subscription revenues. Это архитектурный gate — не раньше €200K validation (D15) и не раньше первого cohort validated. [src:decisions/JETIX-PLAN.md#§5.2]

**Главный принцип sequencing:** каждый новый stream открывается только после того, как предыдущая ступень валидирована и не требует Ruslan'ского full-attention. Иначе — AP-MGMT-4 (scope creep) и риск срыва Phase-1 €50K target.

**Claim §6.6-C1 (sequencing protection):**
- F: F4 (operational convention per D15 revenue-gated + D18 productization path; закреплено в Locks)
- ClaimScope: Phase-1 solo-operator; NOT valid при наличии 5+ team (тогда parallel streams не создают одиночного bottleneck)
- R: опровергается, если появляется inbound demand на новый stream (например клиент сам просит educational content) → тогда opportunistic открытие допустимо, НО requires explicit Ruslan ack (scope gate)

---

## §6.7 Cross-Section Reconciliation Note

**Dependences on/from other §§ L7:**

- **→ §3 Unit Economics:** pricing arithmetic для каждого stream (hourly €150/hr, Path-B €7.5K/quarter, cohort €50K, subscription €200-€500/мес) является ВХОДОМ из §2 Pricing + §3 Unit Econ. Если §2/§3 изменят ranges → доли портфеля в §6 обновляются пропорционально. Mgmt не пересматривает pricing — consumption only.
- **→ §7 Cash Flow:** Phase-1 cash flow model (monthly Q1-Q2 2026) потребляет revenue-stream timing из §6 (какой stream когда начинает генерировать cash). Разрыв: subscription revenue появляется only post-G3 → в Phase-1 cash model она = €0.
- **→ §11 Risk Register:** concentration risk thresholds (§6.5) питают §11 risk register напрямую: single-client >30% = explicit risk entry. DACH recession (R-15) = demand shock на Группу A (§6.4) = quantified cash-flow impact в §11.
- **→ §13 Evolution Master:** ranking shares per gate (G1→G5) в §13 должны совпадать с §6 фазовой логикой. Если §13 даёт другой ranking order → conflict flag для brigadier.

---

## §X Cell C-04 Self-Improvement Notes

**Pattern 1 — Concentration threshold → minimum client count formula:**

Phase-1 single-client threshold 30% при target €50K = max €15K per client. При средней величине engagement (Path-B hourly mix: ~€7-10K per client over Phase-1) минимальный безопасный N = ceiling(1/0.30) = **4 clients**. Универсальная формула: N_min = ceiling(1/threshold). При threshold 25% (Phase-2): N_min = 4; при threshold 15% (Phase-3): N_min = 7. Это прямой KPI для outreach velocity: если N_active < N_min → concentration risk.

**Pattern 2 — Anti-cyclic stream onboarding lag:**

Subscription + licensing = anti-cyclic, но оба требуют 12-24 месяцев build time ПОСЛЕ revenue gate. Если DACH recession приходит в 2026-27 (R-15), Jetix встречает её с проциклическим портфелем даже если Phase-1 выполнена. Вывод: anti-cyclic streams не "страховка на Phase-1" — они страховка на Phase-3. Единственная Phase-1/2 защита от recession = geographic diversification (US demand vs DACH demand не синхронны) + клиентская диверсификация (N_min).

**Pattern 3 — Bimodal stream risk:**

M&A success-fees и token revenues — bimodal: либо крупный event (€1-2M сделка; token utility launch), либо €0. Bimodal streams нельзя включать в cash-flow baseline — только в upside scenario. Правило: baseline cash model = только predictable streams (retainer + hourly + subscription + licensing). Bimodal streams входят в "upside sensitivity" расчёт §7, не в base case.

---

## Provenance

| Source | Range | Relevance |
|---|---|---|
| decisions/JETIX-PLAN.md | §3.1.1 CC-1 + §5.5 Phase 2 streams + §6 Phase 3 | Revenue-mix decomposition + Phase-2 action plan + Phase-3 holding structure |
| decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md | §2.1 Portfolio table + §2.5 Revenue priority classification + §3.1-§3.8 direction sections | Direction-level offer structures + P1A/P1B classification + Phase activation gates |
| decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md | §2.1 single-client >30% threshold + §11 Evolution table | Concentration threshold binding constraint + membership cardinality per gate |
| decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md | §3 M&A as Phase-2+ optionality + deferred-status verbatim | M&A brief mention rationale + bimodal revenue profile |
| swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md | §3 L6+L5 acked inputs + M&A directive | Binding constraints list; L5 Q1-Q5 ack status; M&A treatment instruction |

---

*Drafted by mgmt-expert (mode: integrator), Cell C-04, cycle cyc-layer-7-business-trajectory-deep-dive-2026-04-25. Status: drafted. Word count: ~1850 words body. Acceptance predicate: PASS — Phase-1/2/3+ rankings present; concentration thresholds per phase declared; diversification correlation analysis present; F-ClaimScope-R per major claim; anti-scope complied (no M&A deep-dive; no unit-econ depth; no Notion writes; no implementation tools; 28 Locks not reopened). Brigadier: this draft is ready for §5.5.5 provenance gate check and integration into LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §6.*
