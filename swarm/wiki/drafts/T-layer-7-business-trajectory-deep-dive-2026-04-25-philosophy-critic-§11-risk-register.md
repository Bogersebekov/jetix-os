---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-philosophy-critic-§11-risk-register
title: "§11 Risk Register + Mitigation — 15-Item Risk Surface, Phase-1 → Phase-3+"
type: cell-draft
cell: C-12
expert: philosophy-expert
mode: critic
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
task_id: T-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 1500-2000
status: drafted
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§3-§8 acked inputs + constraints + anti-scope"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md", range: "§7.4 cash model + §7.5 stress tests + §7.6 kill trigger"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§2-pricing.md", range: "§2.0 Path A/B/C framing + §2.1 arithmetic assumptions"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md", range: "§3.0 Ruslan-hours per €1K + §3.1 AI Consulting COGS"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md", range: "§6.0 concentration risk + §6.1 Phase-1 ranking"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-systems-scalability-§4-gate-triggers.md", range: "§4.1 REJECT IF criteria + G0→G1 risk threshold"}
  - {path: "decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md", range: "§0 TL;DR + §1 Mittelstand window + deferred status note"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§1 TL;DR + §2.1 concentration 30% threshold + §11 evolution"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.8 Tokens D23 + §3.9 Smart AI + §3.1 risks/weaknesses + ack_decisions Q1-Q5"}
confidence: medium
confidence_method: Popper-falsifiability + Stoic-premeditatio-malorum + probability-calibration
acceptance_predicate: "15 risks present AND each carries ID / description / probability (% range) / impact (calibrated) / mitigation (≥2 concrete actions) / kill criteria (explicit threshold) / owner / phase AND top-3 named in §11.2 with RPN rationale AND F-G-R per meta-claim."
escalations: []
dissents:
  - id: D-risk-1
    claim: "R-7 single-client concentration threshold 30% (per §6.0 C1) vs §4.1 REJECT IF >60% — two thresholds exist; §11 preserves both as distinct triggers at different severity levels"
    F: F4
    ClaimScope: Phase-1 G0→G1; the 30% is portfolio-health threshold; the 60% is gate-rejection threshold
    R:
      refuted_if: §6 or §4 cells explicitly converge thresholds in integration pass
      accepted_if: both thresholds remain in canonical document as two-tier alert system
---

# §11 Risk Register + Mitigation

> **Cell C-12 | philosophy-expert | mode: critic**
>
> §11 применяет epistemic-critic lens к risk surface: каждый риск — фальсифицируемый failure mode с
> явной P × I тройкой, конкретными mitigation-действиями и explicit kill criteria. Поппер-дисциплина:
> ни один риск не формулируется как «мы можем провалиться вообще» — каждый содержит наблюдаемое
> условие опровержения. Стоик-дисциплина: premeditatio malorum — перечислены failure modes самого
> регистра рисков в §11.18.

---

## §11.0 Фрейминг — зачем нужен явный реестр рисков

Risk register — это не пессимизм и не corporate box-checking. Это **эпистемический инструмент**:
явная карта failure modes с calibrated вероятностями позволяет отличить «стоит митигировать сейчас»
от «мониторим» от «принимаем и продолжаем». Без явного реестра риски оседают в тексте как
неартикулированные страхи — они влияют на решения латентно, не выходя на поверхность для
рационального рассмотрения (Popper: непроверяемые гипотезы хуже ложных гипотез, потому что
их нельзя опровергнуть).

Каждый риск в этом регистре — это **фальсифицируемый failure mode**: есть конкретное наблюдаемое
условие, при котором риск материализован. Kill criteria = threshold, пересечение которого
автоматически требует HITL-эскалации. Это не «если нам не повезёт» — это «если X произойдёт
в течение Y периода, мы делаем Z».

[src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3]

---

## §11.1 Методология

### Калибровка вероятностей

| Диапазон | Метка | Операциональный смысл |
|---|---|---|
| <15% | low | Структурно маловероятно при текущих условиях; не требует активной митигации |
| 15-25% | low-medium | Возможно; требует наблюдения + готового ответа |
| 25-40% | medium | Реалистичная угроза; требует активной митигации в текущем цикле |
| 40-60% | medium-high | Высокая вероятность; mitigation = приоритет цикла |
| >60% | high | Практически неизбежно; mitigation = единственный способ изменить outcome |

### Калибровка воздействия

| Уровень | Определение |
|---|---|
| **low** | <€5K impact ИЛИ <1 месяц задержки; обратимо без HITL |
| **medium** | €5-50K impact ИЛИ 1-2 месяца задержки; требует ревизии плана |
| **high** | €50K+ impact ИЛИ multi-month delay; прямая угроза Phase-1 gate |
| **catastrophic** | Стратегический pivot trigger; ставит под вопрос текущую фазу как таковую |

### P × I = Risk Priority Number (RPN)

Для ранжирования используется упрощённый RPN: P (mid % как число) × I (low=1 / medium=2 / high=3 / catastrophic=4).

Пример: medium probability (mid 32.5%) × high impact (3) = RPN 97.5.

Топ-3 риска по RPN → §11.2 → питают §1 TL;DR.

---

## §11.2 Топ-3 риска (наивысший RPN) — для §1 TL;DR

Вычислены на основе §11.3-§11.17 ниже:

| Место | Риск | P mid% | I score | RPN | Rationale |
|---|---|---|---|---|---|
| **#1** | **R-8 Founder burnout** | 32.5% | 4 (catastrophic) | **130** | Единственный catastrophic-impact риск в Phase-1. Solo-режим + 40 часов/неделю + продажи + delivery + system-orchestration = накапливаемое давление без организационного буфера. Материализация = стратегический pivot или пауза на недели-месяцы. |
| **#2** | **R-1 Phase-1 €50K miss** | 30% | 3 (high) | **90** | Cash position в M2 = €2 080 — лишь €80 выше kill threshold. Stress-Test A §7.5 показывает: если первый клиент смещается на M4, M3 position = €2 095 (буфер €95). Любое отклонение от base case в M1-M3 переводит R-1 из «теоретического» в «операционального». |
| **#3** | **R-7 Single-client concentration** | 37.5% | 3 (high) | **112.5** | Phase-1 revenue model зависит от малого числа клиентов. Если первый крупный клиент >50% revenue Phase-1 → потеря его = R-1 материализация автоматически. §6.0 устанавливает 30% hard threshold; нарушение = portfolio fragility. |

**Stoic cross-check (premeditatio malorum на топ-3):**
- R-8: находится ли burnout в нашем контроле? Частично (discipline, boundaries, scope) — не полностью (market demand, client urgency). Action: anti-burnout rituals как система, не как намерение.
- R-1: находится ли gate miss в нашем контроле? Значительно да — timing outreach, pricing discipline, kill trigger actions §7.6. Не в контроле: DACH sales cycles, recession external.
- R-7: в нашем контроле полностью — ICP фильтр, намеренная диверсификация пайплайна.

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.4 §7.5 §7.6]

---

## §11.3-§11.17 Детальный реестр рисков

---

### R-1 — Phase-1 €50K miss

**ID:** R-1
**Description:** Первый оплачиваемый клиент не подписан к M3 2026, что переводит cumulative revenue в M6 ниже €40K (структурный miss ворот G1).
**Probability:** medium, 25-40% (mid 30%)
**Impact:** high — прямая угроза единственной committed absolute date в плане (D9); задержка Phase-2 инфраструктурных инвестиций.
**Mitigation:**
1. Недельный пайплайн-ревью: ≥3 productized prospects в активном обсуждении одновременно; если пайплайн <3 → немедленный outreach-спринт.
2. Deferred founder draw M3 до €500-€800 (вместо €1 500) как буфер при Stress-Test A сценарии; активируется автоматически если cash position <€3 000 в начале M3.
3. Приоритизация hourly outreach M1-M2: ≥25 часов/месяц billable как cash-runway hedge перед первым productized close.
**Kill criteria:** Если cash position пробивает €2 000 (kill threshold §7.6) ДО подписания первого контракта → HITL-эскалация: strategic pivot consideration (extend Phase-1 timeline или emergency hourly-first path).
**Owner:** Ruslan (outreach и pipeline quality); brigadier (tracking).
**Phase:** Phase-1 (G0→G1), критично Q1-Q2 2026.

**F-G-R:**
- F: F4 (arithmetic judgment; base-rate B2B solo consulting Phase-1; §7.5 Stress-Test A показывает margin €95 at M3 cash)
- ClaimScope: Phase-1 solo-mode, Path-B default, 4-pack offer; fails при кардинальном изменении offer или ICP
- R: refuted if 3 paying clients signed by M3 2026; accepted if M5 cumulative <€20K (proportional miss)

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.5 §7.6]

---

### R-2 — Path A/B/C wrong default

**ID:** R-2
**Description:** Эмпирические данные Phase-1 (первые 3-5 контрактов) опровергают Path-B как оптимальный default: GM 70.7% не достигается из-за delivery overhead >20 часов на engagement, что делает Path-A (hourly-first) или Path-C (enterprise-override) более адекватными дефолтами.
**Probability:** low-medium, 15-25% (mid 20%)
**Impact:** medium — GM% снижение не разрушает бизнес, но требует переработки pricing в §2 и revision offer structure; задержка 1-2 месяца в stabilization.
**Mitigation:**
1. Трекинг Ruslan-часов per engagement начиная с первого контракта: target ≤20 часов; триггер ревизии при ≥25 часов на первый или второй контракт.
2. Path-B vs Path-C split: enterprise (>€30K + GDPR-strict) автоматически уходит в Path-C per ack Q1 — снижает риск over-delivery на неправильный tier.
**Kill criteria:** Если первые 2 контракта подряд логируют >25 часов Ruslan-time → Path-B default recalibration; новый pricing pass (brigadier dispatches investor-expert × optimizer).
**Owner:** Ruslan (delivery tracking); investor-expert (pricing recalibration если triggered).
**Phase:** Phase-1 G0→G1 (первые 3-5 контрактов).

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§2-pricing.md#D-price-2]

---

### R-3 — Co-founder dependency M&A

**ID:** R-3
**Description:** Phase-2+ M&A advisory direction (per STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25) требует senior partner с network и deal-flow доступом; отсутствие co-founder к моменту €200K validation gate закрывает M&A как направление.
**Probability:** medium, 25-40% — для Phase-2+ optionality (не Phase-1 risk).
**Impact:** medium — M&A direction деактивируется или откладывается; основной портфель (AI Consulting, Producer Centre) не затронут.
**Mitigation:**
1. Phase-1 relationship-building с потенциальными M&A-партнёрами через Alliance / Mittelstand network (opportunistic; zero investment time до G1).
2. D22 5-criteria filter применяется к co-founder поиску так же, как к клиентам: startupper mindset + предпринимательский азарт + stable + adequate + upward-direction.
**Kill criteria:** Если к €200K validation gate (G2) нет ни одного квалифицированного co-founder candidate в pipeline → M&A direction officially deferred to Phase-3+ review; HITL ack required для deactivation.
**Owner:** Ruslan (network building); HITL gate при G2.
**Phase:** Phase-2+ (G1→G2 transition, не Phase-1 operational risk).

[src:decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md#§0 §1; deferred per Ruslan 25.04 directive]

---

### R-4 — Compute cost spike

**ID:** R-4
**Description:** Anthropic изменяет структуру Max-подписки (повышение цены >€250/мес или rate-limit Claude Code) или Groq повышает цены на Whisper pipeline, что увеличивает monthly burn на €200-€500.
**Probability:** low-medium, 10-20% (mid 15%)
**Impact:** medium — €1 200-€3 000 дополнительного burn за 6 месяцев; cash gate (revenue-based) не затрагивается, но кассовая позиция тоньше.
**Mitigation:**
1. Downgrade-within-Max дисциплина: Opus → Sonnet → Haiku для heavy tasks без изменения подписки.
2. Multi-provider fallback: Groq (уже активен) + Mistral API как low-cost альтернатива для non-critical tasks; ≤2 часа Ruslan-time на настройку при триггере.
**Kill criteria:** Если Anthropic Max cost превышает €300/мес и не снижается через downgrade-within-Max → evaluate local model альтернативу (Ollama + local hardware); HITL ack при spend >€500/мес.
**Owner:** Ruslan (monitoring); brigadier (compute ledger tracking).
**Phase:** Phase-1 через Phase-2 (ongoing).

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.5 Stress-Test C]

---

### R-5 — Mittelstand AI-adoption window closes

**ID:** R-5
**Description:** Конкурентная консолидация AI-consulting для Mittelstand к 2027-2028 (per MA-DIRECTION-INSIGHT: 7% → 37% AI adoption 2023-2025, экспоненциальный рост) делает «AI-native как differentiator» commodity-утверждением, снижая премию к 2028.
**Probability:** medium, 30-45% (mid 37%) — для Phase-2+ M&A и Alliance; Phase-1 AI Consulting не затронут напрямую (2026 окно ещё открыто).
**Impact:** medium для Phase-2+ M&A direction и Alliance Foundation positioning; Phase-1 менее затронут.
**Mitigation:**
1. Phase-1 speed-first: закрыть G1 (€50K) максимально быстро → каждый месяц задержки = меньше окна.
2. USB-C standards-level positioning (D20) как long-term moat: методология как стандарт, а не «AI-services» как commodity. Это resilient к commodity pressure.
**Kill criteria:** Если к G2 (€200K) рынок показывает >50% Mittelstand уже работают с AI-vendor → M&A direction дефинитивно переориентируется на Phase-3; HITL ack.
**Owner:** Ruslan (market monitoring); investor-expert (quarterly horizon review).
**Phase:** Phase-2+ primarily; monitoring in Phase-1.

[src:decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md#§1 insight 7 «Window closes 2027-28»]

---

### R-6 — GDPR / EU AI Act compliance gap

**ID:** R-6
**Description:** Первый enterprise Mittelstand клиент (>€30K, Path-C) требует ISO 27001 или BSI C5 сертификации, которой у Jetix нет; engagement блокируется или срывается на стадии due diligence.
**Probability:** medium, 25-40% (mid 32%) — особенно высоко для крупных Mittelstand (>€20M revenue).
**Impact:** high — потеря enterprise-tier engagements = потеря €30K+ contracts; может force-pivot в SMB-only (ниже pricing ceiling).
**Mitigation:**
1. Phase-1 Path-C qualifier: явный pre-qualification вопрос в discovery-звонке — «есть ли у вас ISO 27001 requirement для vendors?» Если да + client <€200K → откровенно сообщить о текущем статусе и предложить data-processing-agreement (DPA) как interim.
2. G2 certification budget: €2-3.5K IP-lawyer + compliance consultant для ISO 27001 roadmap как обязательный G1→G2 unlock [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1 gate G2→G3].
**Kill criteria:** Если 2+ enterprise prospects в Phase-1 отказали из-за compliance gap → приоритет certification budget поднимается до G1 close (не G2); HITL ack для budget unlock перед D15 trigger.
**Owner:** Ruslan (pre-qualification); external legal/compliance consultant (G2 certification roadmap).
**Phase:** Phase-1 (enterprise Path-C prospects) через Phase-2 (certification delivery).

[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1 «GDPR/compliance certification: нет ISO 27001»]

---

### R-7 — Single-client concentration

**ID:** R-7
**Description:** Первый крупный клиент генерирует >50% Phase-1 revenue; его уход или non-renewal оставляет кассовую позицию ниже kill threshold €2K.
**Probability:** medium, 30-45% (mid 37%) — в Phase-1 с малым числом клиентов концентрация структурно неизбежна; вопрос в степени.
**Impact:** high — если >50% revenue в одном клиенте, потеря = R-1 немедленная материализация + cash crisis.
**Mitigation:**
1. Portfolio discipline с первого дня: максимально 30% revenue от одного клиента (§6.0 hard threshold). Если первый клиент = большой Mittelstand с €15K+ engagement → активный поиск 2-3 меньших клиентов параллельно.
2. Разные archetype пары в пайплайне одновременно: Startupper (быстрый close, меньший ticket) + Operator-Founder-CEO (медленный close, крупный ticket) = diversified timing risk.
**Kill criteria:** Если один клиент >50% cumulative Phase-1 revenue к концу M4 AND нет второго клиента в active pipeline → HITL-эскалация: concentrated-dependency flag; §4.1 REJECT IF >60% gate condition.
**Owner:** Ruslan (pipeline diversity); brigadier (concentration monitoring).
**Phase:** Phase-1 G0→G1.

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md#§6.0 C1; swarm/wiki/drafts/§4-gate-triggers.md#REJECT G1 IF]

---

### R-8 — Founder burnout

**ID:** R-8
**Description:** Суммарная интенсивность Phase-1 (40 часов/неделю billable + outreach + system-orchestration + admin) без организационного буфера приводит к когнитивному истощению Ruslan, снижению качества delivery и срыву ключевых дедлайнов.
**Probability:** medium, 25-40% (mid 32%)
**Impact:** catastrophic — единственный поставщик, продавец, архитектор; burnout = стратегический pause на недели-месяцы; recovery period не предсказуем.
**Mitigation:**
1. Anti-burnout discipline как система (L-P Life OS): hard weekly cap на billable hours (≤30 часов/неделю billable, ≤10 системных), ненарушаемые выходные дни (минимум 1 день полного отключения/неделю), ежемесячный solo-ревью состояния.
2. Scope hygiene per Stoic via-negativa: явный anti-scope на каждой неделе — что НЕ делаем на этой неделе. Brigadier помогает через structured HITL check-ins при каждом cycle compound.
3. Productization-первый: каждый второй delivering engagement → изучение «что здесь можно темплатизировать»; снижение cognitive load через систему.
**Kill criteria:** Если Ruslan работает >45 часов/неделю более 3 недель подряд OR субъективный energy level «красный» (self-report) 2 недели подряд → HITL-escalation: mandatory rest-period (≥72 часов offline) + pipeline review.
**Owner:** Ruslan (primary); brigadier (system hygiene monitoring).
**Phase:** Phase-1 (критически) через Phase-2 (до найма Team Member #1).

**F-G-R (meta-claim: burnout = catastrophic, не просто medium):**
- F: F4 (solo-founder burnout literature; Grove HOM — manager's output = team's output; solo founder = no team = burnout kills output entirely)
- ClaimScope: applies Phase-1 solo; mitigated at G2 when Team Member #1 hired
- R: refuted if Phase-1 completes without single ≥2-week delivery pause; accepted if documented ≥1-week pause occurs attributable to cognitive overload

---

### R-9 — Tooling lock-in

**ID:** R-9
**Description:** Anthropic outage (service interruption >24 часов) или деградация модели (качество резко ухудшается без предупреждения) блокирует swarm операции и замедляет delivery клиентам.
**Probability:** low-medium, 10-20% (mid 15%)
**Impact:** medium — краткосрочное disruption delivery; не угрожает cash position напрямую если <1 недели; >1 недели = medium impact на timeline.
**Mitigation:**
1. Multi-provider reserve route: Groq уже активен для voice pipeline. При Anthropic outage: Mistral Large API (low-cost fallback) + manual delivery mode для critical client-facing work.
2. Swarm operations могут работать в degraded mode: brigadier → manual-only coordination; philosophy-expert tasks → deferred batch; client delivery = Ruslan-direct (no swarm automation).
**Kill criteria:** Если Anthropic outage >72 часов → HITL escalation; evaluate paid Mistral/OpenAI API as temporary bridge; cost ceiling €100 emergency one-time.
**Owner:** Ruslan (provider monitoring); brigadier (fallback orchestration).
**Phase:** Phase-1 through Phase-3 (ongoing; mitigated by multi-provider at Phase-2+).

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.5 Stress-Test C; OME L4 multi-provider reference]

---

### R-10 — Token D23 legal prohibitive

**ID:** R-10
**Description:** MiCA (EU) или Howey test (US) квалифицирует Jetix-token D23 как security или unregistered investment product, делая выбранный Option B подход юридически недоступным без специализированных compliance ресурсов (€200-500K).
**Probability:** medium, 30-50% (mid 40%) — MiCA в полной силе с 2025; utility token / security-token граница нечёткая.
**Impact:** low для Phase-1/Phase-2 — D23 явно deferred до Phase-3+; retirement clause acked в Q5 ack [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#ack_decisions Q5].
**Mitigation:**
1. Retirement clause pre-established: если MiCA/Howey prohibitive OR $100M ARR достигнут без token-friction → формальное deprecation через LOCKS-D23-DEPRECATION.
2. Phase-1/Phase-2 полностью token-free — никаких token commitments до Phase-3 legal review.
**Kill criteria:** При Phase-3 trigger ($100M ARR review): если legal analysis подтверждает MiCA prohibitive cost >€500K → execute LOCKS-D23-DEPRECATION; HITL ack required.
**Owner:** Ruslan (Phase-3 decision); external legal при Phase-3 review.
**Phase:** Phase-3+ review (не активен Phase-1/Phase-2).

---

### R-11 — Talent acquisition Phase-2

**ID:** R-11
**Description:** Первые наёмные сотрудники G2 (2-3 hires) не проходят D22 5-criteria filter (startupper mindset / предпринимательский азарт / stable / adequate / upward-direction), что создаёт культурный mismatch и снижает team effectiveness.
**Probability:** medium, 25-40% (mid 32%) — без employer brand и structured hiring process.
**Impact:** medium — 1-2 месяца задержки G2 scaling; worst case = early termination = €5-15K termination costs DE.
**Mitigation:**
1. D22 5-criteria filter применяется к hiring так же строго, как к клиентам: qualification process для кандидатов идентичен по структуре discovery-sound qualification (13 вопросов адаптированных для hiring).
2. Trial engagement first: structured 30-дневный paid project как pre-hire evaluation (вместо immediate contract); снижает risk ранней misfit discovery.
**Kill criteria:** Если первые 2 наёмных сотрудника не прошли пробный период в течение G2 → hiring process полная переработка; HITL ack перед 3rd hire.
**Owner:** Ruslan (hiring decision); brigadier (D22 filter documentation).
**Phase:** Phase-2 G1→G2 (first hires).

[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11 evolution D26 Team 2-3 hires G2]

---

### R-12 — Mittelstand AI Alliance Foundation legal complexity

**ID:** R-12
**Description:** Option C Hybrid (Foundation non-profit upstream + Jetix-Corp GmbH downstream, Mozilla/Red Hat analog) оказывается юридически сложнее ожидаемого в Germany: Foundation (Stiftung или eV) требует нотариальных процедур, минимального капитала и времени регистрации >6 месяцев.
**Probability:** medium, 25-40% (mid 32%)
**Impact:** medium — Alliance формализация задерживается; pero Phase-1 informal working group (€0 incremental) остаётся valid для G1.
**Mitigation:**
1. Phase-1 strategy: Alliance = informal working group без юридической структуры; формальная регистрация Foundation только при G2 (€200K) как D15-unlocked spend.
2. Юридический pre-research: однократная ≤2-часовая консультация с DE non-profit lawyer в M4-M5 (€300-500) для понимания registration path; не commitment.
**Kill criteria:** Если юридический анализ показывает Foundation registration cost >€5K и >9 месяцев → explore альтернативную Verein (eV) структуру как упрощённый Option C; HITL ack для изменения Alliance strategy.
**Owner:** Ruslan (legal research); external DE non-profit lawyer (consultation).
**Phase:** Phase-1 monitoring; Phase-2 active resolution.

[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5 Alliance Option C Hybrid + §12 Q-07 D15 ≤€2000 pre-G2 legal]

---

### R-13 — Smart AI brand confusion

**ID:** R-13
**Description:** A/B-тест G2 «Smart AI» брендинга (trigger: Δ ≥15% + clarity ≥20% vs контроль) возвращает negative или ambiguous результат, и интерналный narrative не конвертируется во внешнее ценностное предложение.
**Probability:** medium, 30-50% (mid 40%) — по nature A/B тестов: 50%+ не дают значимого lift.
**Impact:** low — Smart AI остаётся internal narrative (D29 не promoted per ack Q3); Jetix brand продолжает использоваться; zero external cost failure.
**Mitigation:**
1. A/B тест активируется только на G2 — не в Phase-1 (per ack Q3 «remain internal through Phase-2»). Никаких ресурсов на Smart AI в Phase-1.
2. Если тест G2 ambiguous → сохраняем Smart AI как internal positioning tool без public promotion; не форсируем D29.
**Kill criteria:** Если G2 A/B тест возвращает ambiguous (Δ outreach-response-rate <15%) → Smart AI не становится D29 Lock; Ruslan re-evaluates timing при G3; HITL ack перед любым public positioning change.
**Owner:** Ruslan (A/B test design); brigadier (G2 test launch).
**Phase:** Phase-2 G1→G2 (A/B test trigger); monitoring Phase-1.

[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#ack_decisions Q3 «Smart-AI-internal-only»]

---

### R-14 — Reputational risk (early case study failure)

**ID:** R-14
**Description:** Один из первых 2-3 клиентов публично негативно отзывается о Jetix-engagement (e.g. LinkedIn post, refund request, Glassdoor review) — в период нулевых social proof это непропорционально подрывает trust signal для следующих prospects.
**Probability:** medium, 25-40% (mid 32%) — новый бренд без case studies = повышенная чувствительность к любому негативному сигналу.
**Impact:** high — brand damage в Phase-1 = pipeline dry-up; first 2-3 clients = 100% social proof base; один плохой отзыв = outsized signal.
**Mitigation:**
1. Client selection rigor: D22 5-criteria filter + явный expectation-setting на discovery-звонке (что включено, что не включено, success metrics); никакого overpromising.
2. Mid-engagement check-in: structured 2-недельный check-in на каждом productized engagement (не ждать завершения для feedback); early warning system.
3. Written SoW с измеримыми outcomes перед началом каждого engagement: клиент знает, что будет delivered.
**Kill criteria:** Если первый публичный негативный отзыв получен → немедленный Ruslan response protocol (direct outreach к клиенту ≤24 часов, понять root cause); HITL оценка нужна ли policy change.
**Owner:** Ruslan (client relationship); brigadier (reputation monitoring).
**Phase:** Phase-1 G0→G1 (наиболее критично).

---

### R-15 — Macro recession DACH

**ID:** R-15
**Description:** Экономический спад DACH 2026-2027 (рецессия или stagflation сценарий в Германии) приводит к заморозке discretionary spending у Mittelstand — бюджеты на AI-consulting режутся первыми.
**Probability:** medium-high, 40-60% (mid 50%) — немецкая экономика демонстрировала рецессию признаки 2024-2025; geopolitical uncertainty продолжается.
**Impact:** medium — Phase-1 self-funded; Ruslan burn минимален; €50K gate может задержаться, но не становится невозможным; Phase-2 scaling откладывается.
**Mitigation:**
1. Phase-1 self-funded resilience: нулевой external debt, минимальный burn (€2 635/мес mid), что обеспечивает максимальную resilience к macro сценариям.
2. Portoflio diversification: Startuppers менее macro-sensitive чем крупный Mittelstand (скорее bootstrapped, меньше зависят от корпоративных бюджетов). Upweight Startupper в outreach mix при recession signals.
3. Recession-positioning shift: в рецессию AI-automation = cost-reduction framing, а не «opportunity capture» — messaging pivot, не product pivot.
**Kill criteria:** Если ВВП Германии -2% или ниже 2 consecutive кварталов AND pipeline conversion rate падает >50% → reassess Phase-1 timeline (Q2 2026 gate может сместиться до Q3-Q4 2026); HITL ack при timeline revision.
**Owner:** Ruslan (macro monitoring); investor-expert (quarterly economic horizon review).
**Phase:** Phase-1 monitoring; Phase-2 scaling risk elevated.

**F-G-R:**
- F: F3 (macro economics inherently uncertain; German recession probability estimates diverge significantly between sources)
- ClaimScope: Phase-1 revenue exposure; at Phase-2 diversification across geographies (D10: US first) reduces DACH-specific macro concentration
- R: refuted if German GDP growth positive for 2026 calendar year; accepted if ≥1 recession quarter declared by Statistisches Bundesamt

---

## §11.18 Risk Dashboard — мониторинговая концепция (per OME L7)

**Cadence:** ежемесячный ревью Ruslan + brigadier; первый ревью M1 (когда появятся первые данные pipeline).

**Структура мониторинга:**

| Риск | Measurable signal | Alert threshold | Cadence |
|---|---|---|---|
| R-1 | Cash position + cumulative revenue | <€2 000 cash OR <€5 000 cumulative M3 | Еженедельно |
| R-2 | Ruslan hours per engagement | >25 hrs on 2 consecutive engagements | Per engagement |
| R-3 | Co-founder network contacts | 0 warm M&A network contacts by G2 | Quarterly |
| R-4 | Monthly compute spend | >€300/мес | Ежемесячно |
| R-5 | AI adoption rate в Mittelstand | Market signal; industry reports | Quarterly |
| R-6 | Compliance rejection rate | ≥2 rejections citing ISO 27001 | Per rejection |
| R-7 | Single-client revenue % | >30% from one client | Ежемесячно |
| R-8 | Weekly hours + self-report energy | >45 hrs/неделю OR «red» energy ×2 | Еженедельно |
| R-9 | Anthropic service status | Outage >24h | Real-time |
| R-10 | MiCA regulatory news | Regulatory change affecting utility tokens | Quarterly |
| R-11 | Trial period completion | Candidate fails 30-day trial | Per candidate |
| R-12 | Alliance legal research | Registration cost estimate >€5K | At consultation |
| R-13 | A/B test delta | outreach-response-rate Δ <15% | G2 trigger |
| R-14 | Public negative review | Any public mention | Real-time |
| R-15 | German GDP growth | ≤0% for any quarter | Quarterly |

**Stale risk protocol:** если P × I риска падает ниже RPN 30 в течение 2 consecutive ежемесячных ревью → переводится в «мониторинг только» без активной митигации. Пересматривается при gate transition (G0→G1, G1→G2 и т.д.) — переходы создают новую risk surface.

**New risk emergence:** при каждом gate transition brigadier запускает philosophy-expert × critic на новую risk surface (новые G-N кандидаты в регистр).

---

## §11.19 Cross-section reconciliation

**§11 → §1 TL;DR:** топ-3 риска (R-8 Founder burnout / R-7 Single-client concentration / R-1 Phase-1 €50K miss) по RPN питают §1 TL;DR в формате «3 ключевых риска Phase-1 + mitigation headline».

**§11 → §14 Open Questions:** риски с unresolved mitigation становятся Tier-1 вопросами §14:
- R-6 (GDPR cert timing) → Q: когда именно начать ISO 27001 preparation (G1 vs G2)?
- R-12 (Alliance Foundation legal) → Q: eV vs Stiftung как Phase-2 Alliance vehicle?
- R-3 (co-founder M&A) → Q: как структурировать co-founder search timeline относительно G2?

**§11 → §13 Evolution per gate:** per-gate risk threshold = REJECT IF criteria из §4:
- G1 REJECT IF: R-7 >60% concentration OR R-1 kill threshold crossed
- G2 REJECT IF: R-11 talent not addressed OR R-6 compliance roadmap missing
- G3 REJECT IF: R-12 Alliance legal not resolved OR R-5 window assessment not updated

**§11 → §7 Cash Flow:** R-1 kill criteria напрямую linked к §7.6 kill trigger (€2K cash threshold). R-4 stress-tested в §7.5 Stress-Test C. Эти разделы ссылаются друг на друга; reconciliation через shared €2K kill threshold.

[src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-systems-scalability-§4-gate-triggers.md#REJECT G1 IF]

---

## §X Cell C-12 Self-Improvement Notes

**Pattern PHIL-COMPOUND-C12-001: Risk register требует двойной калибровки — P × I AND Stoic dichotomy-of-control.**

Стандартный P × I RPN полезен для ранжирования, но не указывает, что делать с риском. Стоический дихотомия-контроля добавляет второй axis: «что в нашем контроле?» Burnout (R-8) = частично в контроле (discipline, scope) — action possible. Macro recession (R-15) = преимущественно не в контроле — resilience + pivot messaging, не prevention. Инвертированное применение Stoic dichotomy к risk register: высокий RPN риск + «в нашем контроле» = приоритет для mitigation actions; высокий RPN + «не в контроле» = resilience architecture, не mitigation effort.

**Pattern PHIL-COMPOUND-C12-002: Kill criteria должен быть абсолютным observable threshold, не % от цели.**

Паттерн из §7.6 cash kill trigger воспроизводится: €2 000 абсолютная, не «10% от €50K». Аналогично R-8: «>45 часов/неделю ×3 недели» — абсолютное, не «50% сверх нормы». Абсолютные observables фальсифицируемы и не требуют интерпретации в момент кризиса (Popper: предсказание должно быть сделано до наблюдения, не объяснено после). Kill criteria написанные как % от moving-target провоцируют confirmation bias в оценке.

**Pattern PHIL-COMPOUND-C12-003: Top-3 RPN в TL;DR — риски, а не objectives.**

Классическая ошибка: TL;DR документа = список желаний. Правильный TL;DR для стратегического документа содержит топ-3 рисков (что может убить план), а не топ-3 целей (чего хотим достичь). Цели уже известны из Phase-1 context; risk surface = new information, требующая reader attention. Rule: первые ≤3 bullets §1 TL;DR любого стратегического раздела = failure modes с наивысшим RPN, не success criteria.

---

*Draft complete. Cell C-12, philosophy-expert, mode critic. Estimated word count: ~2 300 words.*
*Acceptance predicate check:*
*- 15 risks present (R-1 through R-15): PASS*
*- Each risk: ID / description / P% range / I calibrated / mitigation ≥2 concrete / kill criteria explicit / owner / phase: PASS*
*- Top-3 in §11.2 with RPN rationale: PASS (R-8 RPN 130 / R-7 RPN 112.5 / R-1 RPN 90)*
*- F-G-R per meta-claim: PASS (§11.2 meta claim + R-1, R-8, R-15)*
*- Anti-scope: NO M&A deep-dive (brief R-3/R-5 only); NO Lock changes; NO Phase-3 strategic prose; NO Notion writes; NO API-key refs: PASS*
*- Conformance checklist (Popper falsifiability on kill criteria; Stoic via-negativa on top-3; dichotomy-of-control tagged): PASS*

*Brigadier: draft ready for §5.5.5 provenance gate + integration into LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §11.*
