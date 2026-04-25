---
id: T-producer-services-strategy-options-2026-04-25-investor-scalability-economics-pricing
title: "Investor-Expert (scalability) — Hypothesis Economics + Pricing Variants"
type: cell-draft
cell: investor-expert
mode: scalability
cycle_id: cyc-producer-services-strategy-options-2026-04-25
task_id: T-producer-services-strategy-options-2026-04-25
brigadier_cycle: 8
phase: 3
created: 2026-04-25
status: drafted
sections_covered: [§3-hypothesis-economics, §5-pricing-variants]
provenance:
  - decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md lines 319-385 (§2.2 pricing tiers)
  - decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md lines 1149-1216 (§3.2 unit-econ baseline)
  - decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md lines 500-680 (§3.2 offer)
  - swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/intake.md
  - swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/decomposition.md §C2
locks_verified: [D10, D11, D18, D22, D26]
---

# Investor-Expert (scalability) — Hypothesis Economics + Pricing Variants

> Контекст: Phase-1 OPTIONS-PAPER. Этот черновик не предлагает стратегию — он
> генерирует варианты с численной подложкой. Руслан выбирает. Все данные — расчётные
> модели, не верифицированные на реальных клиентах.

---

## §3 Hypothesis Economics — H1..H5

### Baseline L7 §3.2 (обязательный якорь)

Все гипотезы измеряются относительно baseline. [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§3.2]

| Метрика | Baseline L7 §3.2 |
|---|---|
| Avg retainer | €4 000/мес |
| Direct COGS/мес | €1 750 (Ruslan 8 hrs × €150 + contractor 10 hrs × €50 + compute €50) |
| Gross Margin | 56.3% ⚠️ ниже 70% флора |
| Ruslan-hrs/€1K | 2.0 (лучший Phase-1 показатель) |
| CAC (органика) | €4 000 (cold outreach) / €2 500 (case-study path) |
| LTV (6 мес + 50% renewal) | €36 000 |
| LTV:CAC | 6.0:1 (conservative) / 14.4:1 (case-study channel) |
| Payback | 1 мес (prepaid) |
| Phase-1 capacity ceiling | ~4 параллельных клиента при Ruslan 8 hrs/client + 40 hrs/wk бюджет Producer |

**Флоры для каждой гипотезы:**
- GM ≥ 40% (Phase-1 minimum; ниже = флаг, не kill)
- LTV:CAC ≥ 3:1 (minimum viable; ≥ 6:1 = здоровый)
- Ruslan-hrs/€1K ≤ 5.0 (scalability threshold)
- Payback ≤ 3 мес (runway preservation)

**Phase-1 capacity logic.** Ruslan 40 hrs/wk = ~160 hrs/мес. Producer allocation (из intake: "Производство контента 60-80% времени" — [src:reports/review_2026-04-24.md audio_475]). При 70%: 112 hrs/мес для Producer. При 8 hrs/client: **максимум 14 клиентов** теоретически, но с учётом onboarding, QA, коммуникации — реальный Phase-1 потолок **4-5 активных ретейнеров** без contractor. С contractor (10 hrs/client): потолок сдвигается до 6-7.

---

### H1: Specialist YouTube Educators (5K-50K subs; courses + consulting; ~$80-300K/yr)

**Профиль сегмента.** Преподаватель-практик с YouTube-каналом 5K-50K подписчиков. Монетизация: курсы ($500-$3K), consulting ($5K-$20K/проект), возможно Patreon/спонсорство. Годовой доход $80-300K. Производит 1-4 видео/мес, но каждое видео обходится 20-40 hrs собственного времени. Боль: "снимаю редко, потому что производство пожирает время; аудитория растёт медленно".

**Tier fit:** Standard €4-6K/мес — 2 workshop-эквивалента/мес (сессия + разбор Q&A). Pilot €2-3K/мес для первых 1-2 пилотов с case study discount 20-30%.

| Метрика | H1 расчёт | vs Baseline |
|---|---|---|
| Avg retainer | €4 500/мес (Standard mid) | +€500 (лучше baseline) |
| Ruslan hours/client/мес | 10 hrs (video review + voice gate + QA тяжелее для video-heavy) | +2 hrs vs baseline |
| Contractor hours/client/мес | 14 hrs (видеоредактор дороже: €65/hr) | +4 hrs + rate +€15/hr |
| COGS/мес | €1 500 + €910 + €50 = **€2 460** | +€710 vs baseline |
| GM% | (€4 500 - €2 460) / €4 500 = **45.3%** | ⚠️ ниже 56.3% baseline; выше 40% флора |
| Ruslan-hrs/€1K | 10 / 4.5 = **2.2** | ✓ ≤5.0 |
| CAC | Специфика канала: YouTube educators активны в LinkedIn + Twitter/X edu-комьюнити. DM + тематическая статья как демо. 5 hrs Ruslan × €150 / 12% конверсия = **€6 250** (холодный). Case study path: €3 000 | Выше baseline ⚠️ |
| Engagement duration | 8 мес avg (курсники планируют длиннее — привязаны к editorial calendar) | +2 мес vs baseline |
| LTV | €4 500 × 8 × (1 + 50% renewal × 6/8) = €4 500 × 8 × 1.375 = **€49 500** | +€13 500 vs baseline |
| LTV:CAC (cold) | €49 500 / €6 250 = **7.9:1** ✓ | |
| LTV:CAC (case study) | €49 500 / €3 000 = **16.5:1** ✓✓ | |
| Payback | 1 мес (prepaid) | = baseline |
| Phase-1 capacity | 10 hrs Ruslan/client → **max 3-4 клиента** без contractor overflow | Ниже baseline ⚠️ |

**Unit-econ verdict H1:** УСЛОВНЫЙ PASS.
- GM 45.3% > 40% флора ✓ — но ниже baseline, потому что video editing contractor дороже.
- LTV:CAC здоровый при case-study канале ✓.
- Риск: если contractor rate повышается до €80/hr (рынок видеоредакторов) — GM падает до 38% < 40% флора. ФЛАГ: video-heavy segment = contractor cost sensitivity высокая; нужна contractor rate договорённость до масштабирования.
- Phase-1 fix: начинать с audio-first workflow (1-session записи без полного video edit); вводить video tier только после contractor rate зафиксирован.

---

### H2: Newsletter Operators с Paid Tier (Substack/Beehiiv; $5K-$50K MRR)

**Профиль сегмента.** Paid newsletter: $5K-$50K MRR = 100-1000 платных подписчиков × $5-$50/мес. Автор производит 2-4 issue/мес. Боль: "не успеваю конвертировать накопленные идеи в контент; пропускаю публикацию — теряю подписчиков". Высокая дисциплина текстового производства, но часто слабый video/audio layer. Хорошо платят если видят прямую связь retention → production.

**Tier fit:** Pilot €2-3K/мес (text-heavy pipeline, ниже production cost). Newsletter operator может апгрейдиться до Standard если добавляет audio-tier (podcast-version newsletter).

| Метрика | H2 расчёт | vs Baseline |
|---|---|---|
| Avg retainer | €3 000/мес (Pilot tier; text pipeline проще) | -€1 000 vs baseline |
| Ruslan hours/client/мес | 7 hrs (text artifacts легче проверять; меньше QA) | -1 hr vs baseline |
| Contractor hours/client/мес | 8 hrs × €50 = €400 (writing editor, не video; стандартная rate) | -2 hrs vs baseline |
| COGS/мес | €1 050 + €400 + €30 = **€1 480** | -€270 vs baseline |
| GM% | (€3 000 - €1 480) / €3 000 = **50.7%** | ⚠️ ниже 56.3% baseline; выше 40% флора |
| Ruslan-hrs/€1K | 7 / 3.0 = **2.3** | ✓ ≤5.0 |
| CAC | Newsletter авторы кластеризованы в Twitter/X и Substack Notes. Взаимные репосты, рекомендации. 3 hrs Ruslan × €150 / 18% конверсия = **€2 500** | Лучше baseline ✓ |
| Engagement duration | 5 мес avg (newsletter операторы более agile — могут уйти если ROI не быстрый; 3-мес minimum важен) | -1 мес vs baseline |
| LTV | €3 000 × 5 × (1 + 40% renewal × 5/5) = €3 000 × 5 × 1.4 = **€21 000** | -€15 000 vs baseline |
| LTV:CAC | €21 000 / €2 500 = **8.4:1** ✓ | |
| Payback | 1 мес | = baseline |
| Phase-1 capacity | 7 hrs Ruslan/client → **max 5-6 клиентов** | Лучше baseline ✓ |

**Unit-econ verdict H2:** PASS с оговорками.
- GM 50.7% acceptable ✓. LTV:CAC 8.4:1 ✓.
- Но LTV абсолютная низкая (€21K vs €36K baseline) потому что retainer ниже и engagement короче.
- Риск: newsletter операторы чувствительны к outcome — если нет видимого subscriber growth в 60 дней, уходят. Высокий churn risk после 3-мес minimum.
- ФЛАГ: H2 — лучший вариант для быстрого старта (низкий CAC, текстовый pipeline проще для Phase-1), но **не лучший для LTV**. Рекомендация: H2 как entry point + апселл до Standard (добавить audio podcast-версию) = расширяет retainer до €4K+ и LTV до baseline уровня.

---

### H3: Course Creators в Productization Phase (Kajabi/Teachable; cohort + self-serve)

**Профиль сегмента.** Курсный создатель с existing course ($500-$3K продукт), хочет добавить cohort или автоматизировать контентное производство под следующий курс. Revenue $50-$300K/yr. Боль: "нужно постоянно производить контент для аудитории между запусками курса; моя аудитория остывает". Длинный sales cycle, но высокая commitment.

**Tier fit:** Standard €4-6K/мес. Специфика: часто нужен отдельный цикл pre-launch content (heavy), после запуска — maintenance cycle (lighter). Непостоянная нагрузка.

| Метрика | H3 расчёт | vs Baseline |
|---|---|---|
| Avg retainer | €5 000/мес (Standard high end; course-creator value = прямой revenue) | +€1 000 vs baseline |
| Ruslan hours/client/мес | 9 hrs (курсные модули требуют структурной проверки) | +1 hr vs baseline |
| Contractor hours/client/мес | 10 hrs × €50 = €500 (mixed editor) | = baseline |
| COGS/мес | €1 350 + €500 + €50 = **€1 900** | +€150 vs baseline |
| GM% | (€5 000 - €1 900) / €5 000 = **62.0%** | ✓ лучше baseline; всё ещё ниже 70% флора |
| Ruslan-hrs/€1K | 9 / 5.0 = **1.8** | ✓ лучший в таблице |
| CAC | Course creators тусуются в niche communities (Kajabi Nation, Skool). Hard to cold-reach; warm through mutual connections или podcast appearances. 6 hrs Ruslan / 10% conv = **€9 000** (cold). Case study / referral: €3 500. | Высокий CAC при cold ⚠️ |
| Engagement duration | 7 мес avg (привязаны к launch cycles; высокий renewal если следующий курс в production) | +1 мес vs baseline |
| LTV | €5 000 × 7 × (1 + 55% renewal × 7/7) = €5 000 × 7 × 1.55 = **€54 250** | +€18 250 vs baseline |
| LTV:CAC (cold) | €54 250 / €9 000 = **6.0:1** ✓ (borderline — только если cold channel) |
| LTV:CAC (warm) | €54 250 / €3 500 = **15.5:1** ✓✓ | |
| Payback | 1 мес | = baseline |
| Phase-1 capacity | 9 hrs Ruslan/client → **max 4 клиента** | = baseline |

**Unit-econ verdict H3:** PASS — лучший GM и LTV среди всех гипотез.
- GM 62.0% — ближайший к 70% флору. LTV абсолютная — самая высокая из H1-H5.
- Риск: CAC cold = €9K — допустим только при warm/referral channel. При холодном старте unit-econ рушится (6:1 LTV:CAC — минимально acceptable; любой churn сдвинет ниже 3:1).
- Риск 2: непостоянная нагрузка — pre-launch месяц = 15+ Ruslan hrs, maintenance месяц = 5 hrs. Неравномерная загрузка contractor. Требует чёткого scope definition в контракте.
- **Сильнейшая гипотеза по unit-econ при warm channel.** При Phase-1 холодном старте — высокий CAC ограничивает.

---

### H4: Podcast Hosts с Deep Guest Expertise (interview format; research + edit heavy)

**Профиль сегмента.** Podcast с 5K-50K слушателями. Монетизация: sponsorships ($2-$10K/эпизод при >10K), Patreon, consulting/coaching. Revenue $50-$200K/yr. Боль: "каждый эпизод = 10+ часов подготовки (research гостя, вопросы, монтаж, shownotes, clips). Я записываю 2 эпизода/мес и выгораю". Pipeline: research → pre-interview brief → interview → edit → shownotes → clips → social.

**Tier fit:** Standard €4-6K/мес. НО: delivery pipeline значительно тяжелее per episode из-за research + video editing clips. Contractor hours выше.

| Метрика | H4 расчёт | vs Baseline |
|---|---|---|
| Avg retainer | €5 000/мес (Standard; podcast value prop = time savings большая) | +€1 000 vs baseline |
| Ruslan hours/client/мес | 12 hrs (research brief review + QA clips + shownotes voice check) | +4 hrs vs baseline ⚠️ |
| Contractor hours/client/мес | 18 hrs × €55 = €990 (podcast editor — выше rate) | +8 hrs + rate ⚠️ |
| COGS/мес | €1 800 + €990 + €60 = **€2 850** | +€1 100 vs baseline |
| GM% | (€5 000 - €2 850) / €5 000 = **43.0%** | ⚠️⚠️ ГРАНИЦА 40% флора |
| Ruslan-hrs/€1K | 12 / 5.0 = **2.4** | ✓ ≤5.0 (но плотнее) |
| CAC | Podcast hosts активны на LinkedIn + Twitter/X + podcast communities. Guesting appearance на чужом podcast = best channel (требует 1-2 episodes как guest первично). 4 hrs prep + 5 hrs Ruslan outreach / 15% conv = **€9 000** (cold). Via podcast community + referral: €4 000. | Высокий CAC ⚠️ |
| Engagement duration | 9 мес avg (подкастеры лояльны если quality hold; editorial calendar-зависимость высокая) | +3 мес vs baseline |
| LTV | €5 000 × 9 × (1 + 60% renewal × 9/9) = €5 000 × 9 × 1.6 = **€72 000** | +€36 000 vs baseline |
| LTV:CAC (cold) | €72 000 / €9 000 = **8.0:1** ✓ | |
| LTV:CAC (referral) | €72 000 / €4 000 = **18.0:1** ✓✓ | |
| Payback | 1 мес | = baseline |
| Phase-1 capacity | 12 hrs Ruslan/client → **max 3 клиента** | Ниже baseline ⚠️ |

**Unit-econ verdict H4:** УСЛОВНЫЙ PASS — с серьёзным предупреждением.
- GM 43.0% — прямо на границе 40% флора. Любой перерасход (guest research сложнее обычного, контрактор дольше монтирует) = GM ниже флора.
- LTV высокая абсолютно, но Phase-1 capacity = 3 клиента (самый низкий).
- ФЛАГ: **H4 не рекомендуется как первый сегмент** из-за низкой GM и высокой COGS sensitivity. Рассматривать только если Ruslan имеет existing тёплую связь с podcast host AND договорённость о contractor rate ≤€50/hr (что маловероятно для podcast editing).
- Альтернативный сценарий: podcast host переходит на audio-only clips (без full video edit) → contractor hours падают до 10 → GM восстанавливается до 52%. Но тогда теряется часть value proposition.

---

### H5: Coaches/Consultants в Productization Phase (1-on-1 → group cohort transition)

**Профиль сегмента.** B2B или B2C coach/consultant, revenue $100-$500K/yr, хочет перейти от 1-on-1 к cohort или course. Боль: "мои знания в голове; я каждый раз заново объясняю одно и то же; хочу упаковать в программу, но нет времени". Jetix value: упакуем твой IP в артефакты, которые станут основой cohort curriculum. Alignment: D28 query-driven KB — client-private KB = их будущий curriculum asset.

**Tier fit:** Pilot/Standard €3-6K/мес. Специфика: чаще нужна структурированная упаковка (frameworks, templates) больше чем video production.

| Метрика | H5 расчёт | vs Baseline |
|---|---|---|
| Avg retainer | €4 000/мес (Standard low / Pilot high; не video-heavy) | = baseline |
| Ruslan hours/client/мес | 8 hrs (framework review + IP capture; comparable to baseline) | = baseline |
| Contractor hours/client/мес | 9 hrs × €50 = €450 (content strategist/editor; text-heavy) | -1 hr vs baseline |
| COGS/мес | €1 200 + €450 + €40 = **€1 690** | -€60 vs baseline |
| GM% | (€4 000 - €1 690) / €4 000 = **57.8%** | ≈ baseline (57.8% vs 56.3%) |
| Ruslan-hrs/€1K | 8 / 4.0 = **2.0** | = baseline ✓ |
| CAC | Coaches/consultants — LinkedIn-heavy, niche industry events, referral networks. Outbound relateable: "я видел ваш LinkedIn post о переходе к group program — вот как мы помогаем это сделать системно". 4 hrs Ruslan / 20% conv (тёплая ниша) = **€3 000** (outbound). Referral: €1 500. | Лучший CAC из всех гипотез ✓ |
| Engagement duration | 6 мес avg (цикл productization обычно 1 cohort cycle = 3-6 мес; renewal при запуске второго cohort) | = baseline |
| LTV | €4 000 × 6 × (1 + 55% renewal) = €4 000 × 6 × 1.55 = **€37 200** | ≈ baseline |
| LTV:CAC (outbound) | €37 200 / €3 000 = **12.4:1** ✓✓ | |
| LTV:CAC (referral) | €37 200 / €1 500 = **24.8:1** ✓✓✓ | |
| Payback | 1 мес | = baseline |
| Phase-1 capacity | 8 hrs Ruslan/client → **max 4-5 клиентов** | = baseline |

**Unit-econ verdict H5:** STRONG PASS — лучший по сочетанию параметров для Phase-1 old.
- GM 57.8% ≈ baseline ✓. LTV:CAC = лучший среди всех гипотез при referral ✓.
- CAC — самый низкий из всех гипотез (€3 000 outbound, €1 500 referral).
- Alignment с D28 KB-compounding очень высокий: productization = чистое IP-capture.
- Риск: нишевой сегмент — клиенты сложнее идентифицировать без нишевого присутствия Руслана как эксперта по productization. Acquisition требует личного авторитета или рефераллов.

---

### Сводная таблица H1-H5

| Метрика | H1 YouTube Edu | H2 Newsletter | H3 Course Creator | H4 Podcast | H5 Coach/Consultant |
|---|---|---|---|---|---|
| Avg retainer | €4 500 | €3 000 | €5 000 | €5 000 | €4 000 |
| GM% | 45.3% ⚠️ | 50.7% ⚠️ | **62.0%** ✓ | 43.0% ⚠️⚠️ | 57.8% ✓ |
| Ruslan hrs/€1K | 2.2 ✓ | 2.3 ✓ | **1.8** ✓✓ | 2.4 ✓ | 2.0 ✓ |
| CAC (лучший канал) | €3 000 | **€2 500** | €3 500 | €4 000 | **€1 500** |
| LTV | €49 500 | €21 000 | **€54 250** | **€72 000** | €37 200 |
| LTV:CAC (лучший) | 16.5:1 ✓✓ | 8.4:1 ✓ | 15.5:1 ✓✓ | 18.0:1 ✓✓ | **24.8:1** ✓✓✓ |
| Phase-1 capacity | 3-4 | **5-6** | 4 | 3 ⚠️ | 4-5 |
| Payback | 1 мес | 1 мес | 1 мес | 1 мес | 1 мес |
| Unit-econ verdict | COND. PASS | PASS + upsell | STRONG PASS (warm) | COND. PASS ⚠️ | **STRONG PASS** |

**Ранжирование по Phase-1 unit-econ fitness:**

1. **H5 Coach/Consultant** — лучший CAC + хороший GM + полный alignment с D28. Приоритет Phase-1.
2. **H3 Course Creator** — лучший GM и LTV absolute, но высокий CAC при cold. Хорош как вторая линия при warm channel.
3. **H2 Newsletter** — быстрый старт, низкий CAC, но низкий LTV. Стратегически ценен как entry-point с планируемым апселлом.
4. **H1 YouTube Educator** — приемлем при аудио-first workflow; GM под давлением при видео-тяжелом pipeline.
5. **H4 Podcast Host** — GM на грани флора; Phase-1 рекомендация: НЕ приоритетный сегмент без тёплого intro и contractor rate ≤€50.

> Примечание: ранжирование — это unit-econ ранжирование, не стратегический выбор.
> Руслан стратегизирует; investor-expert предоставляет арифметику.

---

## §5 Pricing Tier Hypotheses

### Контекст: L7 §2.2 baseline tiers

[src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§2.2]

| Tier | Scope | Price/мес | Min commit |
|---|---|---|---|
| Pilot (Starter) | 1 workshop/мес → 10+ artifacts | €2K–€3K | 3 мес |
| Standard (Growth) | 2 workshops/мес → 20+ artifacts | €4K–€6K | 3 мес |
| Premium (Elite) | 4+ workshops/мес → 40+ artifacts + full funnel | €7K–€10K | 3 мес |

10% quarterly prepaid discount уже действует в baseline.

**Принцип анализа.** Каждый вариант оценивается по:
- Empirical case — когда именно этот вариант выигрывает
- GM impact — количественно
- CAC impact — качественно
- Phase-1 fit — yes / yes-with-test / no
- Brigadier rating — 1-10 + reasoning

---

### Вариант 1: Floor adjustment €3K experimental vs €5K operational

**Вопрос:** Устанавливать ли нижний порог в €3K (Pilot high end) или в €5K (Standard mid) для Phase-1 retainer?

**Расчёт break-even Ruslan-hrs при каждом флоре:**

При COGS структуре baseline (contractor 10 hrs × €50 + compute €50 = €550 фиксированная часть), Ruslan hours = переменная:

*При €3 000/мес floor:*
- Для GM ≥40%: COGS ≤ €1 800. Ruslan часть ≤ €1 800 - €550 = €1 250 → Ruslan ≤ 8.3 hrs × €150. Break-even = 8.3 hrs/client.
- При 8 hrs (baseline): GM = (€3 000 - €1 750) / €3 000 = **41.7%** — barely above 40% floor.
- При 9 hrs (одна лишняя встреча): GM = (€3 000 - €1 900) / €3 000 = **36.7%** — ниже флора. ⚠️

*При €5 000/мес floor:*
- Для GM ≥40%: COGS ≤ €3 000. Ruslan часть ≤ €3 000 - €550 = €2 450 → Ruslan ≤ 16.3 hrs × €150.
- При 8 hrs (baseline): GM = (€5 000 - €1 750) / €5 000 = **65.0%** — хорошо; приближается к 70%.
- При 12 hrs (сложный клиент): GM = (€5 000 - €2 350) / €5 000 = **53.0%** — acceptable.
- Break-even = 16.3 hrs/client — значительный запас прочности.

**Empirical case для €3K floor:** Снижает acquisition friction для buyers, которые "хотят попробовать" без большого commitment. Ускоряет подписание первых 1-2 пилотов. Даёт возможность case study + testimonial при сниженном риске для клиента. ТОЛЬКО при условии: (a) client fit идеальный, (b) явный апселл-план до Standard на Month 4+, (c) Ruslan-hrs контролируемы ≤8/мес.

**Empirical case для €5K floor:** Защищает GM от Ruslan-hours overflow. Отсекает "трудных клиентов с малым бюджетом" (Marks second-level: кто торгуется до €3K, тот и в delivery будет требовать максимум). Позиционирует как premium service с первого дня. При Phase-1 цели = 4-5 клиентов, даже 3 клиента × €5K = €15K/мес — существенно (vs 3 × €3K = €9K/мес).

**GM impact:** €3K floor = 41.7% GM (fragile). €5K floor = 65.0% GM (robust).

**CAC impact:** €3K floor снижает психологический барьер → конверсия outbound выше (estimate: +30-50%). €5K floor требует более сильного value-prove upfront → либо case study, либо warm referral.

**Phase-1 fit:**
- €3K floor: yes-with-test (только как "пилот на пилот" discount, с планом апселла)
- €5K floor: yes (операционный стандарт)

**Brigadier rating:**
- €3K floor: **5/10** — допустим как исключение для первых 1-2 case studies с 20-30% discount (equivalent €2.4K-€2.1K effective), но НЕ как operational floor. Risk-of-ruin: если 3+ клиентов окажутся на €3K с overflow Ruslan-hours, GM коллапсирует.
- €5K floor: **8/10** — рекомендуется как операционный стандарт с Month 1. Friction выше, но unit-econ защищён. При case study discount: €4.0K effective (20%) = GM 52% — acceptable.

---

### Вариант 2: One-time setup fee + retainer

**Структура:** €3 000 setup fee + €3 000/мес retainer (vs flat €4 000/мес без setup fee).

**GM trajectory — 6-month comparison:**

*Flat €4 000/мес × 6:*
- Total revenue: €24 000
- Total COGS (6 × €1 750): €10 500
- Total GM: €13 500 = **56.3% GM**

*Setup €3 000 + €3 000/мес × 6:*
- Month 0 (setup): Revenue €3 000. Setup COGS: Ruslan 15 hrs × €150 = €2 250 (onboarding, KB bootstrap, pipeline config). GM setup: (€3 000 - €2 250) / €3 000 = **25.0%** ⚠️
- Month 1-6: Revenue €18 000. Monthly COGS (при €3K retainer, меньше delivery): 7 hrs × €150 + 9 hrs × €50 + €40 = €1 540/мес. Total delivery COGS: €9 240.
- Total revenue: €21 000. Total COGS: €11 490. Total GM: €9 510 = **45.3% GM** — хуже flat. ⚠️

*Проблема:* setup fee не покрывает реальный onboarding overhead. При честном onboarding (KB bootstrap, pipeline config, first cycle) — Ruslan тратит 12-20 hrs. Если setup fee = €3K и setup COGS = €2.5K, margin с setup = €500. Flat модель лучше.

**Empirical case:** Setup fee полезен если (a) настройка объективно сложная и требует отдельного billing (e.g., Enterprise клиент с нестандартным workflow), (b) Ruslan хочет создать психологическое "инвестиция уже сделана" для retention. При простом Pilot tier setup fee усложняет продажу без пропорциональной выгоды.

**GM impact:** Хуже flat на 6-месячном горизонте при типичном onboarding overhead. Pass if setup fee ≥€5 000 (покрывает реальный overhead + маржа); fail at €3 000.

**CAC impact:** Увеличивает upfront стоимость для клиента → конверсия ниже. Зато фильтрует не-committed buyers.

**Phase-1 fit:** no (хуже unit-econ; усложняет продажу на этапе когда нужна скорость первых подписаний).

**Brigadier rating: 3/10.** Setup fee как отдельная строчка не рекомендуется Phase-1. Альтернатива: включить onboarding cost в Month 1 prepaid (клиент видит одну цифру; Ruslan получает ту же cash).

---

### Вариант 3: Performance Bonus Tier

**Структура:** €3 000/мес base + 5% revenue uplift бонус, capped €2 000/мес (effective ceiling €5 000/мес).

**GM analysis (при базе €3 000 + бонус €1 000 avg):**
- Revenue avg: €4 000/мес (base + avg bonus)
- COGS: €1 750/мес (не меняется — производство одинаковое)
- GM: (€4 000 - €1 750) / €4 000 = **56.3%** ≈ baseline

*Если бонус-месяц = €5 000 (cap):*
- GM: (€5 000 - €1 750) / €5 000 = **65.0%** — хорошо
- Но бонусный месяц не означает больший объём работы → чистый upside

**Empirical case:** Работает если: (a) у клиента есть измеримый revenue metric, напрямую связанный с production output (курсные продажи, email conversions, coaching inquiries через контент), (b) baseline agreement на attribution methodology до старта, (c) клиент имеет revenue ≥$10K/мес (5% бонус значим).

**Риски:**
1. **Attribution dispute**: "Этот рост выручки — от моего контента или от вашего production?" — первая же успешная продажа создаёт спор.
2. **Accounting overhead**: Ruslan должен ежемесячно получать и верифицировать revenue data от клиента. Если клиент не делится честно — не работает.
3. **Misalignment**: Производство хорошего контента ≠ рост revenue (конверсия зависит от offer, pricing, market timing). Ruslan несёт риск за переменные вне его контроля.
4. **Клиент psychology**: "Если base = €3K, значит стандартная работа стоит €3K. Зачем мне платить €5K?" — якорный эффект base снижает perceived value.

**GM impact:** Нейтральный при avg. Положительный при high-performance. Риск: на начальных месяцах пока клиент не measure attribution — фактически работаем за €3K/мес (ниже baseline).

**CAC impact:** Привлекателен для outcomes-oriented buyers; увеличивает конверсию у performance-minded segment.

**Phase-1 fit:** yes-with-test (только для 1 экспериментального клиента с чёткой attribution methodology и минимум 3-мес baseline data у клиента). НЕ как основной pricing format.

**Brigadier rating: 4/10.** Интересная гипотеза, но не для Phase-1 старта. Attribution complexity и misaligned risk слишком высоки без established delivery track record. Рассмотреть как Phase-2 add-on после 6+ месяцев данных по delivery outcomes.

---

### Вариант 4: Productized 4-Week Sprint vs Ongoing Retainer

**Sprint structure:** €8 000–€12 000 all-in за 4 недели, фиксированный scope:
- Week 1: KB bootstrap + client IP capture (2 workshop sessions)
- Week 2: Artifacts batch 1 (12-15 artifacts from 2 sessions)
- Week 3: Artifacts batch 2 + distribution calendar
- Week 4: Review + handoff + "производственный план" на 3 мес

**GM сравнение:**

*Sprint €10 000 (mid-price):*
- Ruslan hours: 25 hrs (intensive 4-week engagement)
- Contractor hours: 20 hrs × €55 = €1 100 (mixed editor)
- Compute: €100
- Total COGS: €3 750 + €1 100 + €100 = **€4 950**
- GM: (€10 000 - €4 950) / €10 000 = **50.5%**

*Sprint €8 000 (low end):*
- GM: (€8 000 - €4 950) / €8 000 = **38.1%** ⚠️ — ниже 40% флора

*Sprint €12 000 (high end):*
- GM: (€12 000 - €4 950) / €12 000 = **58.8%** — лучше

*Retainer €4 000/мес × 6 (baseline):*
- GM: 56.3% (стабильная)

**Ruslan-hrs predictability:** Sprint = известная нагрузка (25 hrs в 4 недели), потом свободно. Retainer = 8 hrs/мес × 6 = 48 hrs распределённо. Sprint создаёт capacity spike, retainer — предсказуемый поток.

**Churn risk:** Sprint = нет churn (фиксированный срок). Retainer = churn risk каждый месяц после 3-мес minimum. Sprint клиент может не продлиться → один-time revenue. Retainer клиент при retention → compound LTV.

**Empirical case для Sprint:** Buyers, которые боятся долгосрочного commitment. "Давайте сначала попробуем 4 недели". Хорошо как acquisition mechanism (lower commitment, faster decision). Risk: без renewal pipeline Sprint = одноразовая транзакция, не business.

**Empirical case для Retainer:** Compound LTV. Client-private KB compounds с каждым циклом — retention incentivizes client (их KB дорожает). Revenue predictability для €50K gate arithmetic.

**GM impact:** Sprint €10K = 50.5% (немного хуже baseline). Sprint €12K = 58.8% (сравнимо). Sprint €8K = 38.1% — below floor.
Retainer = 56.3% (стабильная, compounding).

**CAC impact:** Sprint снижает CAC через lower barrier to entry. Но если не переходит в retainer — CAC amortization плохая (один sprint = разовая выручка / CAC ≥ 1:1 LTV:CAC при cold channel).

**Phase-1 fit:**
- Sprint: yes-with-test (как on-ramp к retainer, ценообразование €10K+, с explicit conversion plan в retainer на Month 5)
- Retainer: yes (основной format)

**Brigadier rating:**
- Sprint: **6/10** — полезен как acquisition pathway "try before you commit" при ценообразовании ≥€10K. НО: должен иметь explicit retainer conversion pitch (Sprint Week 4 = "вот ваш производственный план на 3 мес — хотите, чтобы мы его реализовали?").
- Retainer (baseline): **9/10** — основной format; защищает KPI €50K gate через predictable revenue.

---

### Вариант 5: Quarterly Prepaid Discount — 10% vs 15-20%

**Текущий baseline:** 10% discount при quarterly prepaid (3 мес upfront). [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§2.2]

**Анализ: стоит ли поднять до 15-20%?**

*При €4 000/мес standard, 15% quarterly discount:*
- Quarterly revenue: €4 000 × 3 × 0.85 = **€10 200** (vs €12 000 без discount)
- Effective monthly: €3 400
- GM при €3 400/мес: (€3 400 - €1 750) / €3 400 = **48.5%** — ниже baseline 56.3%

*При 20% quarterly discount:*
- Effective monthly: €3 200
- GM: (€3 200 - €1 750) / €3 200 = **45.3%** — падает к H1 уровню ⚠️

*Что получает Ruslan за скидку?*
- Cash flow certainty (€12 000 upfront vs €4K/мес) — важно для €50K gate arithmetic
- Zero churn risk на 3 мес — избегает re-acquisition cost
- Negotiating leverage с contractor (guaranteed work = возможно rate снижение)

*Opportunity cost скидки:*
- При 15% discount: потеряно €1 800 за квартал (vs no discount). Если replaced by new client = €1 800 opportunity cost acceptable только если CAC нового клиента > €1 800. CAC baseline = €4 000 — значит СОХРАНИТЬ клиента на квартальном prepaid ВЫГОДНЕЕ чем найти нового.
- При 20% discount: потеряно €2 400 за квартал. Аналогично — всё равно выгоднее чем CAC €4 000.

**Empirical case для 15%:** Buyers с cash flow volatility (независимые creators с irregular income) — скидка 15% даёт им reason to commit upfront. При Phase-1 цели = cash flow certainty для €50K gate, 15% discount aggressive но defensible.

**Empirical case для оставить 10%:** 10% = достаточно psychological incentive; увеличение до 15-20% компрессирует GM без пропорционального увеличения prepaid adoption rate. Если 10% уже конвертирует 50%+ клиентов в prepaid — нет смысла давать больше.

**GM impact:**
- 10% discount: GM = 53.8% (от базовой €4K)
- 15% discount: GM = 48.5%
- 20% discount: GM = 45.3% ⚠️

**Phase-1 fit:** 10% = yes (baseline). 15% = yes-with-test (для первых 2-3 клиентов как incentive). 20% = no (компрессирует GM ниже приемлемого без достаточного benefit).

**Brigadier rating:**
- 10% (baseline): **8/10** — сохранить как стандарт
- 15%: **6/10** — допустим как temporary incentive для первых 2-3 клиентов Phase-1 для cash flow bootstrap
- 20%: **3/10** — нет. GM ниже 46% не оправдан для retainer service.

---

### Вариант 6: Tiered Minimum Commitment — 3-мес стандарт vs 1-мес trial + premium

**Структура:** 1-месячный пробный период с +30% pricing premium (risk-adjusted pricing для клиента).

*При €4 000/мес Standard + 30% = €5 200/мес для 1-мес trial:*
- GM: (€5 200 - €1 750) / €5 200 = **66.3%** — лучший GM из всех вариантов ✓
- Если конвертируется в 3-мес стандарт после: total 4-мес revenue = €5 200 + €4 000 × 3 = **€17 200**

*Vs стандарт 3-мес minimum €4 000/мес:*
- Total 3-мес revenue = €12 000

*Если trial не конвертируется (client уходит после 1 мес):*
- Revenue = €5 200. COGS = €1 750. GM = €3 450.
- CAC already spent = €2 500-4 000.
- LTV:CAC = €5 200 / €4 000 = **1.3:1** ⚠️ — ниже 3:1 минимума при холодном CAC.

**Расчёт break-even conversion rate:**

Для trial to be unit-econ positive при cold CAC €4 000:
- LTV должен быть ≥ €12 000 (3:1 minimum) при 1-мес trial
- Если trial конвертируется в 6-мес retainer: LTV = €5 200 + €4 000 × 5 = **€25 200** → LTV:CAC = 6.3:1 ✓
- Break-even conversion rate: LTV trial × conv% + LTV (конверсии не случилось) × (1 - conv%) ≥ €12 000
- Если trial non-convert LTV = €5 200, convert LTV = €25 200: conv% ≥ (€12 000 - €5 200) / (€25 200 - €5 200) = 34%

Т.е. trial модель unit-econ positive если ≥34% trialing clients конвертируются в full retainer. Phase-1 estimate: неизвестно — нет данных. Предположение: если это вынужденный вариант для risk-averse buyer, конверсия 30-50% — реалистично.

**Empirical case:** Risk-averse buyers с высоким CAC (те, кого сложно закрыть на 3-мес commitment). "Покажите мне, что это работает, прежде чем я дам commitment". Полезен для premium segment (H3 Course Creator) где CAC высокий и buyers careful.

**GM impact:** Trial-месяц = лучший GM (66.3%). Если конвертируется — хорошо. Если нет — CAC не amortized.

**CAC impact:** Снижает barrier → конверсия outbound выше. Но если conversion-to-retainer <34% — unit-econ отрицательный.

**Phase-1 fit:** yes-with-test (для 1-2 случаев с высокорелевантными buyers, где без trial они точно не подпишут).

**Brigadier rating: 6/10.** Полезен как тактический инструмент для конкретных buyers. НЕ как стандарт. Риск: если все клиенты ведут переговоры через trial, операционная предсказуемость снижается.

---

### Сводная таблица вариантов ценообразования

| Вариант | GM impact | CAC impact | Phase-1 fit | Brigadier rating |
|---|---|---|---|---|
| V1a: €3K floor | 41.7% ⚠️ (fragile) | Конверсия выше | yes-with-test (case study only) | 5/10 |
| V1b: €5K floor | 65.0% ✓✓ | Friction выше | yes (operational standard) | **8/10** |
| V2: Setup fee + retainer | 45.3% ⚠️ (worse) | Lower entry | no (Phase-1) | 3/10 |
| V3: Performance bonus | Нейтральный avg | Outcomes buyers | yes-with-test (1 experiment) | 4/10 |
| V4a: Sprint €10K | 50.5% | Lower commitment | yes-with-test (retainer on-ramp) | 6/10 |
| V4b: Retainer (baseline) | 56.3% ✓ | Standard | yes | **9/10** |
| V5a: 10% prepaid (baseline) | 53.8% | Standard | yes | **8/10** |
| V5b: 15% prepaid | 48.5% | Better adoption | yes-with-test (first 2-3) | 6/10 |
| V5c: 20% prepaid | 45.3% ⚠️ | Best adoption | no | 3/10 |
| V6: 1-мес trial +30% | 66.3% (trial мес) | Converts resistant | yes-with-test (selective) | 6/10 |

### Investor recommendation (не стратегия — арифметика):

**Операционный стандарт Phase-1 (максимизирует GM + predictability):**
- Floor: €5K (Standard tier) для открытого outbound
- 10% quarterly prepaid discount (сохранить baseline)
- 3-мес minimum commitment (сохранить baseline)
- Retainer (не sprint) как primary format

**Exceptions-table для первых 2-3 клиентов:**
- Case study discount 20-25% допустим → effective €3 200-3 750 (выше €3K floor, GM ≥40%)
- 15% prepaid допустим для cash flow bootstrap
- 1-мес trial при risk-averse buyer если conversion intent высокий (explicit "trial → retainer" framing)

**Варианты к тесту в Phase-1 (не запускать все одновременно):**
- Один Sprint €10K как acquisition experiment (measure: conversion to retainer %)
- Один performance bonus experiment при identified кандидате с чёткой attribution model
- Не тестировать setup fee — unit-econ хуже без upside

---

## Escalations

```yaml
escalations: []
dissents:
  - claim: "H4 Podcast Host может быть жизнеспособным при audio-only workflow"
    F: F4 (расчётная; не верифицирована)
    ClaimScope: только если contractor hours ≤10 и rate ≤€50/hr
    R: refuted если первый podcast client потребует full video edit → GM ниже 40%;
       accepted если первые 3 месяца audio-only delivery и GM ≥45%
  - claim: "V3 Performance Bonus требует pilot данных перед scale"
    F: F4 (operational convention)
    ClaimScope: Phase-1 только при existing revenue track record клиента
    R: refuted если attribution methodology agreed in writing перед старт;
       accepted если 3-мес baseline data available при signing
```

## Provenance

- [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§2.2] — L7 pricing tiers (lines 319-385)
- [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§3.2] — L7 unit-econ baseline (lines 1149-1216)
- [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.2] — L5 offer structure (lines 500-680)
- [src:swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/intake.md] — task mandate + constraints
- [src:swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/decomposition.md#C2] — cell assignment

## Confidence

```yaml
confidence: medium
confidence_method: arithmetic
note: >
  Все расчёты — модельные, на основе L7 §3.2 baseline + экстраполяции на специфику
  сегмента. CAC estimates — аналоговые (нет реальных данных по conversion rates).
  Engagement duration — Phase-1 предположения (нет pilot data). Единица данных,
  которая изменит модель наиболее сильно: первый реальный client time-log.
```
