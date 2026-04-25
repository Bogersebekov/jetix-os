---
id: producer-services-strategy-OPTIONS-2026-04-25
title: "Producer Services — strategy OPTIONS paper (5 hypotheses + market analysis + brigadier proposal)"
type: strategy-options-paper
direction: producer-services
mode: OPTIONS-PAPER
authority: Ruslan-strategist-only
state: drafted-awaiting-ruslan-ack
created: 2026-04-25
cycle_id: cyc-producer-services-strategy-options-2026-04-25
task_id: T-producer-services-strategy-options-2026-04-25
brigadier_cycle: 8
phase: 3
operating_mode: Stage-Gated
hitl_gate: AWAITING-APPROVAL packet at swarm/gates/AWAITING-APPROVAL-producer-services-strategy-options-2026-04-25.md
provenance_inline: true
locks_referenced: [D10, D11, D13, D18, D22, D25, D26, D28]
sources:
  - {path: "swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/intake.md", range: "full"}
  - {path: "swarm/wiki/tasks/T-producer-services-strategy-options-2026-04-25/decomposition.md", range: "full"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.2 lines 500-680"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "§2.2 lines 319-385"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "§3.2 lines 1149-1216"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§3.2 §3.10 lines 310-438"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 D11 §7.1"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1-§3.4 §3.7"}
  - {path: "swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-mgmt-integrator-market-hypotheses-proposal.md", range: "full"}
  - {path: "swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-investor-scalability-economics-pricing.md", range: "full"}
  - {path: "swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-systems-scalability-acquisition-pipeline.md", range: "full"}
  - {path: "swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-philosophy-critic-open-questions-discipline.md", range: "full"}
  - {path: "swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-engineering-integrator-pipeline-feasibility.md", range: "full"}
  - {path: "reports/review_2026-04-24.md", range: "audio_475 + audio_508 (Producer center mandate verbatim)"}
brigadier_top_proposal:
  primary_hypothesis: "H4 Podcast hosts OR H5 Coaches productizing — paired (zero-delta-cluster + best unit-econ)"
  alternative: "H1 Specialist YouTube educators (highest ICP-fit but tech-debt + GM-fragile)"
  acquisition_paths_proposed: "Path 4 Referral (warm) + Path 3 Blogger collaborations + Path 6 Discovery call as conversion layer"
  pricing_floor_proposed: "€5K operational (V1b) — protected GM; case-study discount 20-25% allowed for first 2-3 pilots"
  retainer_format: "3-mo minimum retainer (V4b baseline) + 10% quarterly prepaid (V5a baseline)"
  decision: "PROPOSAL ONLY — Ruslan selects from 5 hypotheses; modifies / hybrid-combines / rejects"
preserved_dissents: 4
open_questions: 9
---

> **FRAMING NOTICE — OPTIONS PAPER, NOT STRATEGY.**
> Этот документ содержит 5 гипотез, рыночный анализ, варианты ценообразования / acquisition / pipeline и **предложение бригадира как один из возможных вариантов для рассмотрения Русланом**. Руслан = единственный стратег. AI / рой / бригадир / ячейки генерируют варианты, собирают данные, surface options. Финальная стратегия = Руслан-выбор / модификация / отклонение.
>
> Per Ruslan 25.04 verbatim: *«я все таки смотрю на продюсерский центр все таки у его как мейн праймери... но вот надо будет еще подробнее разобраться это наверное уже вопрос отдельного рабочего дня но пусть это залупа там накидает какие-то гипотезы не знаю мы потом из них по выбираем посмотрим»*
>
> Per Левенчук + D2 §13: AI does not strategize. Per D11: Producer Services = Phase-1 PRIMARY direction. Phase-3 cycle 8.

---

## §1 TL;DR

**5 гипотез сгенерированы для рассмотрения Русланом** (Phase-1 PRIMARY direction = Продюсерский центр для англоязычного infobiz):

| # | Гипотеза | Brigadier rating (mgmt) | Investor unit-econ rank | Eng feasibility |
|---|---|---|---|---|
| H1 | Specialist YouTube educators (5K-50K subs) | **8/10** | #4 (cond. pass; 45% GM fragile) | YES-WITH-EFFORT (audio-strip gap) |
| H2 | Newsletter operators (Substack/Beehiiv $5K-$50K MRR) | 6/10 | #3 (pass + upsell; €21K LTV low) | **YES** (zero delta) |
| H3 | Course creators productizing (Kajabi/Teachable) | 6/10 | #2 (strong pass *warm only*; €54K LTV) | YES-WITH-EFFORT (export adapter) |
| H4 | Podcast hosts (deep guest expertise) | 7/10 | #5 (cond. pass; 43% GM borderline) | **YES** (native fit) |
| H5 | Coaches/consultants productizing (1-on-1 → group) | 6/10 | **#1** (strong pass; 24.8:1 LTV:CAC referral) | **YES** (native fit) |

**Cross-cell tension surfaced honestly (not averaged into consensus):**
- **mgmt-expert (integrator)** ranks H1 highest by ICP-fit (canonical Блогер archetype, leverage-multiplier story most visually convincing)
- **investor-expert (scalability)** ranks H5 first by unit-econ (best CAC + best LTV:CAC + GM ≈ baseline + native D28 KB-compounding)
- **engineering-expert (integrator)** flags **H2+H4+H5 = zero-delta cluster** (no Phase-1 tooling build needed); H1 + partial H3 = isolated video tech-debt
- **systems-expert (scalability)** notes podcast guesting (Path 2) acquisition mechanism creates **dual leverage** with H4

**Brigadier proposal (one option among several — Ruslan considers and selects):**

Brigadier предлагает рассмотреть пару **H4 (Podcast hosts) + H5 (Coaches productizing)** как Phase-1 starting hypothesis с **H1 (YouTube educators) как conditional-add при наличии тёплого Ruslan-network в YouTube-creator сегменте**. Обоснование: H4+H5 = zero-delta cluster (минимум engineering risk), strong unit-econ, native pipeline fit, акquisition through podcast guesting + referral compounds. H1 имеет наивысший ICP-fit но GM-fragile + video tech-debt; стоит включать только при тёплых контактах.

Acquisition pair proposed: **Path 4 (Referral, warm intros) + Path 3 (Blogger collaborations / first pilot)** + **Path 6 (Discovery call) as conversion layer**.

Pricing floor proposed: **€5K operational** (V1b — protected GM 65%, LTV:CAC robust). Case-study discount 20-25% allowed for first 2-3 pilots → effective €3.75K-€4K (still above €3K experimental floor; GM ≥40%).

**Это предложение, не стратегия.** Руслан выбирает любую из 5 гипотез, любую комбинацию, любые модификации, либо отклоняет starting-point полностью.

**Top-3 unknowns requiring Ruslan ack (full list = 9 Q-PS-XX в §6):**

1. **Q-PS-01:** Какие 1-2 гипотезы тестировать первыми 30-60 дней? — стратегический выбор, brigadier proposes H4+H5, Ruslan decides
2. **Q-PS-02:** Pricing floor €3K экспериментальный или €5K операционный? — risk-tolerance + cash-flow call
3. **Q-PS-06:** Первые 2 target accounts — Ruslan называет из network ИЛИ brigadier surfaces public shortlist? — executive decision

**Out-of-scope (deferred):**
- M&A direction (Phase-2+ per Ruslan 25.04)
- Outreach activation (no DMs sent, no commitments)
- Externally committed pricing (numbers here = internal options only)
- Final strategy (Ruslan strategizes; this is OPTIONS only)

---

## §2 Market Analysis — English-Speaking Infobiz Landscape

> **Important data caveat:** Руслан располагает отдельными рыночными анализами и конкурентными таблицами, которые будут интегрированы в выделенном цикле позже (см. Q-PS-05). Цифры TAM/SAM/SOM ниже — **directional estimates**, основанные на данных репозитория + общесинтетические знания. Не authoritative. Brigadier flags this transparently. [src:swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-mgmt-integrator-market-hypotheses-proposal.md §2.6]

### §2.1 Course creators (Kajabi / Teachable / Mighty Networks ecosystem)

**Профиль сегмента.** Онлайн-преподаватели, монетизирующие экспертизу через платформы: Kajabi (~75K активных создателей), Teachable (~150K создателей с платными учениками), Mighty Networks (community-first + course hybrid, ~10K+ активных). Диапазон выручки $30K-$1M+/год. Наиболее платёжеспособный сегмент creator-экономики для retainer offer. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.10 Teacher archetype]

**TAM/SAM/SOM (directional).**
- **TAM:** ~500K+ монетизированных создателей курсов в EN странах (US + UK + AU + CA). Мировой рынок creator-платформ >$15B (2025).
- **SAM** (≥$5K/мес выручки от курсов): ~50K-80K создателей. ICP — те с production bottleneck.
- **SOM Phase-1:** 5-10 retainer clients = математически negligible vs SAM. Phase-1 задача — найти 1-2 пилотов, не захватить сегмент.

**AI-adoption status.** Ранние последователи / переходный mass adoption. Kajabi запустил нативные AI-инструменты (~2023-24). Создатели курсов вынуждены использовать AI (ChatGPT, Jasper, Descript) под конкурентным давлением. Пропасть: «AI ad hoc» vs «systematized production-pipeline». Jetix позиционируется в этой пропасти.

**Боли (специфика).**
- Curriculum rot через 12-18 месяцев без systematic update
- Launch-effort огромен; ongoing cohort-delivery overhead недооценивается
- 60-80% времени тратится на production [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2 + reports/review_2026-04-24.md audio_475 verbatim]
- Repurposing: workshop → модуль → статья → тред = ручной труд

**Конкуренты в production services.** Платформенно-нативные AI (generic, нет per-client KB); freelance ghostwriters ($1-3K/мес, single-point-of-failure); course-agencies ($5-15K/мес, нет client-private KB); DIY с Claude/Descript (high operator overhead).

**Pricing benchmarks.** High-quality course agencies $5-15K/мес. Niche course producers $2-5K/мес. **Jetix Pilot €2-3K/мес попадает в нижний диапазон серьёзного сегмента; Standard €4-6K/мес конкурентоспособно vs mid-tier agencies.** [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.2]

### §2.2 YouTube educators / Podcasters

**Профиль сегмента.** Специалисты с YouTube-каналами 5K-500K подписчиков (finance, tech, law, healthcare, business strategy, engineering — НЕ lifestyle). Подкастеры с interview-форматом в тех же нишах. Архетип Блогера (D7): возраст 26-45, $80K-$600K/год (реклама + курсы + спонсорство + consulting). [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2 + decisions/JETIX-VISION.md §7.1]

**TAM/SAM/SOM (directional).**
- **TAM YouTube:** ~100K-200K каналов в специалистских EN-нишах с 5K+ подписчиков
- **SAM** (≥$5K/мес выручки + production bottleneck): ~20K-40K каналов
- **TAM Podcasts:** ~50K-100K активных нишевых specialist-подкастов в EN
- **SAM Podcasts** (мontized + bottleneck): ~5K-15K
- **SOM Phase-1:** 1-2 пилота из любой группы

**AI-adoption status.** Tech + finance ниши = ранние последователи (transcription, thumbnails, research). Healthcare / legal / compliance = consрervative из-за accuracy + risk. Подкастеры отстают от YouTube-creators по AI-adoption.

**Боли.**
- **YouTube specialists:** один long-form видео → shorts → статья → тред → newsletter = 20-40 часов ручного труда. Прямое попадание в «1 workshop → 10+ artifacts» promise.
- **Interview podcasters:** research-overhead на гостя + edit + show notes = 4-12 часов на эпизод. Jetix research-pipeline = прямое решение.
- **Distribution clarity:** сильнейшие каналы публикуют регулярно не из-за времени, а из-за production-систем.

**Конкуренты.** Podcast-production companies (podcastmotors, resonate) $2-5K/мес audio-only. Video editing freelancers $1-3K/мес editing-only. Repurposing tools (Repurpose.io) — generic, нет voice preservation.

**Pricing benchmarks.** Podcast production $2-5K/мес; YouTube channel agencies $3-8K/мес mid-tier. **Jetix Pilot €2-3K competitive; Standard €4-6K требует чёткого ROI-narrative (artifacts + compounding KB).** [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.2]

### §2.3 Newsletter operators (Substack / Beehiiv с paid tier)

**Профиль сегмента.** Специализированные newsletter-операторы с платными подписчиками: Substack ($5K-$100K/мес MRR), Beehiiv (SaaS-модель, обычно выше MRR при аналогичном размере аудитории). Архетипы: ex-journalist / отраслевой analyst / опытный практик. Аудитория 5K-100K. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2]

**TAM/SAM/SOM (directional).**
- **TAM:** ~65K+ платных newsletter-операторов (Substack ~50K + Beehiiv ~15K)
- **SAM** (≥$5K/мес MRR): ~5K-10K операторов
- **SOM Phase-1:** один из самых маленьких прямых SOM, но конверсия выше (newsletter-операторы привыкли платить за tools + services)

**AI-adoption status.** Mixed. Substack-нативный editor — basic. Beehiiv интегрировал AI-writing. Высококачественные операторы (≥$100/год с подписчика) **сопротивляются AI-writing из-за voice concerns** — это прямое попадание в Jetix offer (research + structure + repurposing, voice-preserving HITL).

**Боли.** Глубина + частота = оба требуют времени. Операторы с 1 VA: операционный overhead поглощает creative время. Best newsletter content существует только как один артефакт — нет систематического repurposing. Research-overhead 40-60% времени.

**Конкуренты.** Newsletter ghostwriters $1-3K/мес single-author; платформенные AI-tools без strategic layer; VA $500-1.5K/мес low-leverage.

**Pricing benchmarks.** Операторы $10K+ MRR — высокая платёжная способность. Newsletter-production services $1-3K/мес. **Jetix Pilot €2-3K = premium для $10K MRR оператора (10-20% операционных доходов); Standard €4-6K — для операторов $30K+/мес.** Conversion в этом сегменте медленнее, чем YouTube/Course. [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.2]

### §2.4 Coaches / Consultants productizing

**Профиль сегмента.** Индивидуальные practitioners, переходящие от 1-на-1 коучинга / консалтинга к scalable products: групповые когорты, self-serve programs, digital frameworks, memberships. $80K-$500K/год. Возраст 30-50. Нишевой фокус: executive coaching, business strategy, performance, regulated consulting (legal/financial). [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.10 + §3.11]

**TAM/SAM/SOM (directional).**
- **TAM:** ~150K-250K практиков в EN-speaking markets (ICF certified ~60K + неформальные ~90-190K)
- **SAM** (productization-phase + ≥$5K/мес): ~10K-20K практиков
- **SOM Phase-1:** узкий по объёму; пересекается с AI-consulting ICP (Operator/Founder архетип) → cross-sell возможность

**AI-adoption status.** Запаздывает. Большинство ad-hoc (ChatGPT for drafts, Notion AI for notes). **Productization-motion = главный bottleneck** — здесь Jetix value: «твои 1-на-1 сессии = raw production input → pipeline → курс / cohort / Substack / book».

**Боли.**
- «Я знаю что мне нужно создать [курс/книгу/программу], но у меня нет времени»
- 1-на-1 time-cap: коуч на $10K/мес продаёт 60-70 часов/мес; масштабирование требует productization
- IP-extraction bottleneck: знания в головах, преобразование требует systematized process
- Cohort program churn: без хорошего production содержания когорты терпят неудачу

**Конкуренты.** Course-creation consultants $3-10K/проект one-time (нет ongoing). Launch-specialist agencies $10-25K+ за запуск. Ghostwriting + course-production hybrids $3-8K/мес (нет client-private KB). **Ongoing-production-for-coaches практически не существует как категория — это белое пятно.**

**Pricing benchmarks.** Productization consultants $2-8K one-time. **Jetix Pilot €2-3K/мес = конкурентен; frame «трансформация IP → масштабируемый актив» работает.** [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.2]

### §2.5 Specialist-bloggers (deep technical / business / research; 5K+ subs; D22 fit)

**Профиль сегмента.** Узкоспециализированные bloggers с deep domain authority: AI/ML researchers, legal-tech bloggers, fintech analysts, B2B SaaS strategists, industrial engineers. Substack-публикаторы, LinkedIn thought-leaders, независимые сайты с newsletter. 5K-100K аудитория. $50K-$400K/год (sponsorships + consulting + книги + speaking). [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2 + decisions/JETIX-VISION.md §7.1 Блогеры]

**D22 fit.** Этот сегмент — **best-fit по 5-criteria filter** среди 5 сегментов: discipline-driven, anti-fad, adequate, явно upward-direction в expert development.

**TAM/SAM/SOM (directional).**
- **TAM:** ~80K-150K specialist-bloggers с 5K+ аудиторией в EN нишах
- **SAM** (монетизация + bottleneck + ≥$5K/мес multiple streams): ~5K-15K
- **SOM Phase-1:** узкий по объёму, **наивысший по ICP-качеству**

**AI-adoption status.** **Бинарный.** Либо ранние последователи (AI-niche bloggers, tech-forward), либо явно скептичные (academic, compliance, медицинские авторы). **Ключевой insight: те, кто скептичен по AI-writing — самые сильные warm leads** для Jetix, потому что offer = AI-pipeline с HITL voice-preservation, не AI-writing.

**Боли (verbatim source).** «Производство контента 60-80% времени, экспертиза недомонетизирована». [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2 verbatim] Один flagship/мес vs 8-10 derivative/мес = 10× distribution gap. Conversion-gap: best content умирает после первой публикации; systematized repurposing = multiple lifetime value per piece.

**Конкуренты.** **Практически нет прямых конкурентов**, специализирующихся на specialist-bloggers как distinct ICP. Most production-services ориентированы на lifestyle / marketing content, не на domain-deep specialist writing. Это white-space возможность для Jetix.

**Pricing benchmarks.** Рынок фрагментирован. Specialist-ghostwriters для блогов $2-5K/мес. Нет matured production-as-a-service для этого ICP. **Jetix Pilot €2-3K/мес reasonable entry для $100K+/год выручкой.**

### §2.6 Закрытие — флаг для интеграции

**ФЛАГ ДЛЯ Q-PS-05:** Цифры TAM/SAM/SOM выше — directional estimates. Авторитативные данные у Руслана (отдельные рыночные анализы + конкурентные таблицы). Brigadier рекомендует выделенный market-analysis cycle ПОСЛЕ Ruslan hypothesis selection — интеграция тогда = refinement, не discovery. Альтернативный путь: интегрировать СРАЗУ если цифры load-bearing для outreach-decision (Q-PS-05 framing).

---

## §3 Hypothesis Cards H1-H5

> Каждая карточка = **гипотеза для проверки**, не утверждение о стратегии. Brigadier ratings (1-10) = собственная оценка mgmt-expert по данным Phase-A; не «winner verdict». Investor unit-econ rank ниже — отдельный сигнал по unit-арифметике. Ruslan может выбрать любую гипотезу по причинам, недоступным swarm-у (network warmth, личный интерес, timing). [src:philosophy-expert C4 patrol checklist]

---

### H1: Specialist YouTube educators (5K-50K subs, monetized via courses or consulting)

**One-line:** Специалист YouTube-создатель (technical / business / financial) с production-bottleneck на public-display — наиболее визуально убедительная демонстрация Jetix leverage-multiplier; tech-debt в video-pipeline = главная Phase-1 friction.

**Target customer profile:** YouTube channel в нишах AI/ML, B2B SaaS growth, financial independence для HNW, law/legal-tech, performance science. 5K-50K subscribers. Монетизация через курсы ($300-2K) + consulting + sponsorship. $80K-$400K/год выручки. Публикует 1-2 видео/мес вместо 4-8 из-за production-gap (не идей-gap). Иллюстративные профили (не commitments): инди-financial analyst с Substack+YouTube; AI-practitioner с tutorial-каналом.

**Acquisition mechanism:** Podcast guesting (Path 2) + targeted LinkedIn outreach (Path 1) к создателям с явными production-gap signals (нерегулярные посты, аудитория-комментарии «больше частоты пожалуйста»). Secondary: blogger collaborations (Path 3) per JETIX-PLAN §3.4 — pro-bono first case study для visibility. [src:decisions/JETIX-PLAN.md §3.4]

**Production pipeline shape (systems-expert):** Research pass через `/ask(client-KB)` → `transcribe.py` (Groq Whisper) на video audio (требуется prior audio-strip step — engineering tech-debt) → `extract.py` → `filter.py` → script + 3-5 shorts scripts + long-form article + Twitter thread + newsletter issue + course-module stub. **KB depth: heavy (6+ cycles).** **Variety: high.** Bottleneck: shorts video edit + audio-strip automation. Cross-direction: §3.6 YouTube-analyzer (Phase 2+) → editorial calendar; §3.7 Educational → 12+ месяцев KB = course curriculum.

**Pricing tier fit:** Pilot €2-3K/мес initial (1 video/мес → 10+ artifacts). Standard €4-6K/мес при 2 видео/мес multi-channel.

**Phase-1 traction signal (Hamel-binary):** Подписан 3-месячный retainer ≥€2K/мес в течение 60 дней с первого outreach. YES = signed. NO = no signed contracts at 60-day mark.

**Pros:**
- Наивысшая alignment с L5 §3.2 canonical ICP (Блогер archetype) — best-fit по qualitative match [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md §3.2 §3]
- Производственная боль максимальная и наиболее визуально демонстрируема (artifact count = Hamel-binary deliverable)
- D10 EN+US-first нативен (YouTube specialists US-primary)
- Client-private KB (D28) наивысшую ценность здесь: каждое видео обогащает KB → script quality compounds
- Наименьшее acquisition friction: production-gap виден в public-facing publishing cadence

**Cons / risks:**
- **Video editing complexity** — требует contractor (€55-80/hr) или Ruslan video skill, не только voice-pipeline. Production complexity higher than newsletter-only ICP. Eng tech-debt: audio-strip step не автоматизирован [src:engineering-expert C5]
- **Compliance risks** в financial / medical / legal niches → potential Jetix liability exposure → требует explicit contract carve-out
- **Investor flag:** GM 45.3% (above 40% floor but fragile); contractor rate sensitivity high — если video-editor rate растёт до €80/hr, GM падает к 38% (below floor) [src:investor-expert C2]
- **Founder bandwidth:** Phase-1 capacity = 3-4 clients max при 10 hrs Ruslan/client/мес [src:investor-expert C2]
- Conversion-cycle средне-длинный (creator-centric decision-makers независимы)

**Acquisition cost estimate:** ~3-5 hrs Ruslan/lead × €150 = €600 hourly cost; cold conversion 12% → ~€6 250 CAC cold; case-study channel ~€3 000 CAC. [src:investor-expert C2]
**LTV estimate:** Standard €4 500/мес × 8 мес engagement × 1.375 renewal multiplier = **€49 500 LTV** (highest among H1-H5 base, before H4)
**Brigadier rating (mgmt-expert):** **8/10.** Best ICP-fit; main risk = video tech-debt + GM fragility. **Investor unit-econ rank: #4 (cond. pass).** **Eng feasibility: YES-WITH-EFFORT.**
**Empirical test (30-60 days):** Outreach 15-20 YouTube-creators в 2 нишах (AI/tech + B2B SaaS). Метрики: response rate, discovery-call conversion, «да но...» refinement signals. Cost: ~5-8 Ruslan-hours. Zero direct €.

---

### H2: Newsletter operators with paid tier ($5K-$50K MRR, Substack/Beehiiv)

**One-line:** Платные newsletter-операторы — финансово квалифицированные, voice-preservation-skeptical (что конвертируется в warm leads для HITL-pipeline Jetix), pipeline simpler than H1; SAM узкий, conversion cycle медленнее.

**Target customer profile:** Substack/Beehiiv оператор в нишах B2B analysis, fintech, healthcare strategy, legal/regulatory. 5K-30K subscribers, 500-3K платных. MRR $5K-$50K. Часто ex-journalist / ex-analyst / practitioner-turned-writer. Публикует 1-2× в неделю; research = 60%+ production time. Voice-quality-skeptical → warm lead для HITL-anchored Jetix.

**Acquisition mechanism:** Direct LinkedIn outreach к writers с research-heavy content signals (long-form, links, data-heavy). Secondary: referral от existing consulting network (Jetix AI consulting ICP overlap значителен). DM angle: «research-pipeline для specialist writers — не AI-ghostwriting, а система исследований». [src:decisions/JETIX-PLAN.md §3.3-§3.4]

**Production pipeline shape (systems-expert):** Focused research → thematic brief → KB-anchored context → structure draft → HITL editorial assist (NOT ghostwrite — structural assist) → repurposing: LinkedIn-post + tweet-thread + summary-version. **Менее video-heavy** vs H1: pipeline существенно simpler. Voice pipeline адаптируется для voice-memo → newsletter-structure pattern. **KB depth: medium (3-5 cycles).** **Variety: medium with spikes.** Bottleneck: ingestion speed при reader-feedback. Cross-direction: §3.4 Matchmaker (cross-niche co-production); §3.5 Secure Network (paid community natural upsell).

**Pricing tier fit:** Pilot €2-3K/мес = ~20-30% MRR для $10K-MRR оператора. Высокая relative cost — требует strong ROI narrative. Standard более естественно обоснован при $30K+ MRR.

**Phase-1 traction signal:** Newsletter-оператор закрывает retainer ≥3 мес в течение 75 дней. Hamel-binary YES/NO.

**Pros:**
- **Самый простой pipeline из 5 гипотез** — meньше contractor-dependency (нет video editing) [src:engineering-expert C5: zero-delta]
- Высокий D22 fit (newsletter-операторы по определению upward-direction, adequate, disciplined)
- Платёжная способность задокументирована публично (Substack MRR частично visible)
- **Voice-preservation angle прямо адресует главный скептицизм сегмента** → Jetix дифференцируется
- Cross-sell potential: newsletter → YouTube-channel (операторы с видео-амбициями = H1 upsell)

**Cons / risks:**
- **Conversion-cycle slower:** newsletter-operators тщательно protect voice; trust строится дольше
- **Узкий SAM** (только ~5-10K операторов с ≥$5K MRR в EN) — Phase-1 пространство маленькое
- **LTV абсолютная низкая** (€21 000 vs €36K baseline) — retainer ниже + engagement короче (5 мес avg) [src:investor-expert C2]
- Высокий churn risk после 3-мес minimum (newsletter-operators agile)
- Меньше «wow»-артефактов vs H1 (newsletter additions менее визуально convincing)

**Acquisition cost estimate:** Lower than H1 (simpler channel). ~€2 500 CAC через case-study path. [src:investor-expert C2]
**LTV estimate:** Pilot €3K/мес × 5 мес × 1.4 = **€21 000 LTV** (lowest absolute)
**Brigadier rating:** **6/10.** Strong ICP-fit по D22; узкий SAM + slow conversion снижают Phase-1 priority. **Investor unit-econ rank: #3 (pass + planned upsell).** **Eng feasibility: YES (zero delta).**
**Empirical test (30-60 days):** Outreach 10 newsletter-operators в B2B SaaS / fintech. Test: open + response + «да но...» signals. ~3-5 Ruslan-hours.

---

### H3: Course creators in productization phase (Kajabi/Teachable; coaching → course transition)

**One-line:** Коучи / consulting-practitioners, явно переходящие от 1-на-1 billing к масштабируемым курсам — нишевый сегмент с высоким production-anxiety и чётким moment-of-purchase (productization decision); CAC высокий при cold start.

**Target customer profile:** Individual practitioner (бизнес-коуч, executive коуч, performance specialist) с активными клиентами (≥5 платных), решивший запустить онлайн-курс или групповую когорту в течение 3-6 месяцев. Инфраструктура: Kajabi/Teachable account. $80K-$250K/год, из них 80%+ — hourly или retainer. «Знаю что нужно сделать курс, но не знаю с чего начать production».

**Acquisition mechanism:** LinkedIn outreach к coaches с productization signals («launching course», Kajabi testimonials, «выход из 1-на-1»). Secondary: referral с AI-consulting клиентов (cross-sell). Moment-of-purchase trigger: когда coach решается запустить — высокое intent. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.10 Teacher archetype]

**Production pipeline shape (systems-expert):** Curriculum ingestion (one-time, baseline) — все existing materials → `/ingest(anchor=client, type=curriculum)` → KB structured by модули. Front-loaded investment 5-10 hrs цикл 1. Update cycle: новая лекция → transcribe → extract → update KB. Repurposing: student handouts + social proof + email nurture + course-module gap analysis. **KB depth: heavy (6+ cycles).** **Variety: low-medium (curriculum structured).** Bottleneck: baseline ingestion. Cross-direction: §3.7 Educational direct synergy; §3.3 USB-C Services (course curriculum как first enterprise deployment KB).

**Pricing tier fit:** Standard €4-6K/мес. Можно структурировать setup fee + lower ongoing.

**Phase-1 traction signal:** Course-creator client запускает первую когорту с Jetix curriculum-artifacts в течение 90 дней. Hamel-binary YES/NO.

**Pros:**
- **Чётко определённый moment-of-purchase** = entry trigger без ambiguity
- Cross-sell с AI-consulting (тот же клиент часто оба)
- High D18 alignment: productization-over-hours = client core goal, не только Jetix principle [src:decisions/JETIX-VISION.md §5 D18]
- **Best GM (62.0%)** + best LTV absolute (€54 250) при warm channel [src:investor-expert C2]
- Knowledge-extraction methodology = differentiator

**Cons / risks:**
- **Длиннее pipeline до видимого результата** — первая когорта 4-8 нед с нуля; client-patience risk
- **Высокий cold CAC (€9 000)** — допустим только при warm/referral channel; LTV:CAC 6:1 borderline cold [src:investor-expert C2]
- **Непостоянная нагрузка**: pre-launch месяц = 15+ Ruslan hrs, maintenance = 5 hrs
- Высокий **scope-creep риск** (course-creators склонны расширять scope)
- Нет «существующей аудитории» у некоторых: course-launch без аудитории = product-risk Jetix не fix

**Acquisition cost estimate:** Cold ~€9 000; warm/referral ~€3 500. [src:investor-expert C2]
**LTV estimate:** Standard €5K/мес × 7 мес × 1.55 = **€54 250 LTV** (highest absolute)
**Brigadier rating:** **6/10.** Хороший ICP-fit, но длиннее time-to-first-artifact + scope-creep risk. **Investor unit-econ rank: #2 (strong pass *warm only*).** **Eng feasibility: YES-WITH-EFFORT (export adapter ~2-4h).**
**Empirical test:** 5 productization-mode coaches identified (LinkedIn signals); 2-3 discovery calls. ≥1/5 → serious retainer conversation = valid signal.

---

### H4: Podcast hosts с deep guest expertise (interview-format; research + editing pipeline)

**One-line:** Interview-подкастеры с domain-depth (B2B, tech, fintech, research) — наиболее **native pipeline fit** + **dual-leverage acquisition** (podcast guesting Ruslan'а одновременно marketing + lead-gen); GM borderline 43%, capacity ceiling низкий (3 clients).

**Target customer profile:** Подкастер с 1K-30K скачиваний/эпизод в EN B2B / specialist нишах. Не entertainment — interview-based с expert guests. 1-4 эпизода/мес. Текущий overhead: 4-12 часов/эпизод (guest research + record + edit + show notes + distribution). Монетизация: sponsorships ($2-10K/эп при >10K), Patreon, consulting, community. $50K-$300K/год.

**Acquisition mechanism:** **Podcast-guesting strategy (Path 2 — dual leverage)** — Ruslan появляется на аналогичных подкастах и органично представляет offer. Secondary: LinkedIn outreach + referral. [src:decisions/JETIX-PLAN.md §3.4 + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3.2 channel: «Podcast guesting»]

**Production pipeline shape (systems-expert + engineering):** Pre-guest research packet (KB-based + web research) → interview structure brief → recording facilitation (optional) → `transcribe.py` (native baseline case) → episode edit support → show notes + summaries → repurposing: clip-selection brief + newsletter-insert + LinkedIn post per episode. **KB depth: medium-heavy (4-6 cycles).** **Variety: very high.** Bottleneck: transcription throughput at scale. **Engineering: native fit, zero delta** [src:engineering-expert C5]. Cross-direction: §3.1 Consulting (podcast host с enterprise audience → cross-sell); §3.4 Matchmaker (host + guest из Secure Network = co-production).

**Pricing tier fit:** Standard €4-6K/мес при 2 эп/мес. Math: €5K / 2 эп = €2.5K/эпизод (плюс KB compounding). Легко обоснован vs traditional podcast-production ($1-3K/эп market).

**Phase-1 traction signal:** Подкаст-клиент подписывает ≥3-мес retainer в течение 60 дней + публикует ≥2 эпизода с Jetix research-packets. Hamel-binary по обоим.

**Pros:**
- **Acquisition через podcast-guesting = dual leverage** (Ruslan строит аудиторию + lead-gen одновременно) [src:systems-expert C3 Pair A reinforcing loop]
- **Engineering native fit** (audio-pipeline = baseline case; zero tooling delta) [src:engineering-expert C5]
- Guest-research pipeline = наиболее **algorithmic из всех гипотез** (repeatable, low creative variance)
- **Highest absolute LTV (€72 000)** при longest engagement (9 мес avg) + 60% renewal [src:investor-expert C2]
- Strong D28 KB-compounding: каждый гость обогащает client KB; KB-depth = competitive asset

**Cons / risks:**
- **GM 43.0% — на границе 40% floor** [⚠️ INVESTOR FLAG] — любой перерасход (research сложнее, contractor дольше монтирует) = ниже floor [src:investor-expert C2]
- **Phase-1 capacity = 3 clients** (lowest) при 12 hrs Ruslan/client/мес
- **Lower SAM** vs H1 (well-monetized specialist podcasters реже YouTube-creators)
- **Conversion-cycle средний:** podcast-hosts осторожны в делегировании guest-selection / research (editorial brand)
- Меньше «wow»-артефактов (show notes + clips менее визуально впечатляюще vs H1)
- Investor recommends: **рассматривать только при warm intro AND contractor rate ≤€50/hr** (что маловероятно для podcast editing)

**Acquisition cost estimate:** Подкаст-guesting reduces effective cost; via community + referral ~€4 000 CAC. [src:investor-expert C2]
**LTV estimate:** Standard €5K × 9 мес × 1.6 = **€72 000 LTV** (highest absolute)
**Brigadier rating:** **7/10.** Strong fit с acquisition mechanism + pipeline simplicity. SAM-size limit Phase-1. **Investor unit-econ rank: #5 (cond. pass + GM warning).** **Eng feasibility: YES (native).**
**Empirical test:** Ruslan появляется на 2-3 relevant podcasts; в post-episode conversations тестирует production-offer naturalistically. Reaction = signal. ~10-15 hrs.

---

### H5: Coaches / consultants productizing knowledge-product (1-on-1 → group cohort transition)

**One-line:** Consulting-practitioners, выстраивающие cohort/membership на базе IP — **highest LTV:CAC + best CAC + native pipeline + strong D28 fit**; longest sales-cycle + highest scope-creep risk.

**Target customer profile:** Independent consultant с 5+ платными клиентами и конкретным frameworks-based IP (не generic coaching). $150K-$400K/год, 70%+ hourly. Хочет запустить cohort ($5-15K/участник, 10-20 участников), membership ($50-300/мес) или signature program. Jetix value: превратить existing 1-на-1 методологии в производимый curriculum + community-content.

**Acquisition mechanism:** LinkedIn search по сигналам «launching group program» / «cohort» / «mastermind formation». **Referral из AI-consulting ICP (Operator/Founder archetype overlap значителен).** Discovery-call как TOF per JETIX-VISION §9 4-pack. [src:investor-expert C2: best CAC at €1 500 referral / €3 000 outbound]

**Production pipeline shape (systems-expert + engineering):** **Privacy layer (specific to H5)** — coaching recordings требуют client-permission + anonymization before ingestion. Pre-processing step: anonymize → sanitized transcript → `/ingest`. Framework extraction → recurring themes → methodology pattern KB-items. Script production: framework posts + LinkedIn series + workshop outline + email sequence. Productization support via `/ask` gap analysis. **KB depth: heavy (6+ cycles).** **Variety: medium + privacy overhead.** Bottleneck: privacy pre-processing (manual Phase-1) [src:systems-expert C3]. **Engineering: native fit (Zoom audio extraction trivial).** Cross-direction: §3.1 AI Consulting (cross-sell); §3.5 Secure Network (anchor-expert role); §3.3 USB-C Services (productization journey = USB-C live case).

**Pricing tier fit:** Pilot/Standard €3-6K/мес.

**Phase-1 traction signal:** Client запускает первую когорту с Jetix curriculum-artifacts в течение 90 дней. Hamel-binary YES/NO.

**Pros:**
- **Investor unit-econ rank #1** — highest LTV:CAC (24.8:1 referral / 12.4:1 outbound), best CAC (€1 500 referral / €3 000 outbound), GM ≈ baseline (57.8%) [src:investor-expert C2]
- **Engineering native fit** (zero delta to minor) [src:engineering-expert C5]
- **Highest D18 alignment**: productization-over-hours = core client goal
- **Cross-sell с AI-consulting natural** (Operator/Founder archetype overlap)
- **Native D28 query-driven KB fit** (productization = clean IP-capture)
- IP-library compound: client-private KB при успешной cohort = premium long-term retainer lock-in

**Cons / risks:**
- **Highest scope-creep risk** из всех гипотез — требует жёстких scope-gates в контракте
- **Длиннее time-to-result** (видимый успех cohort launch = 6-12 нед; client-patience risk)
- **Market-validation gap:** если cohort productization fails по marketing причинам, Jetix не rescue → blame risk
- **Privacy pre-processing manual** Phase-1 (anonymization не automated в текущей infrastructure) → +30-60 мин/цикл [src:systems-expert C3 dissent]
- **Overlap с H3** (оба productization-journey) — разница в entry point (H3 = course-platform natives; H5 = consulting practitioners)
- Acquisition требует личного авторитета или referrals (нишевой identification)

**Acquisition cost estimate:** ~€1 500 referral / €3 000 outbound (best of all hypotheses). [src:investor-expert C2]
**LTV estimate:** €4K/мес × 6 мес × 1.55 = **€37 200 LTV**
**Brigadier rating:** **6/10.** Highest LTV:CAC потенциал; longest sales+delivery cycle. **Investor unit-econ rank: #1 (strong pass).** **Eng feasibility: YES (native to minor).**
**Empirical test:** 3-5 discovery calls с consultants в productization-mode. ≥2/5 явный интерес к production-retainer = valid signal. ~5-8 hrs.

---

### Сводная таблица гипотез

| # | Гипотеза | mgmt rating | Investor rank | Eng feasibility | GM | LTV | Best CAC | Phase-1 capacity |
|---|---|---|---|---|---|---|---|---|
| H1 | YouTube educators | **8/10** | #4 cond. | YES-WITH-EFFORT | 45.3% ⚠️ | €49 500 | €3 000 | 3-4 |
| H2 | Newsletter ops | 6/10 | #3 pass | **YES** | 50.7% ⚠️ | €21 000 | **€2 500** | **5-6** |
| H3 | Course creators | 6/10 | #2 strong (warm) | YES-WITH-EFFORT | **62.0%** ✓ | **€54 250** | €3 500 | 4 |
| H4 | Podcast hosts | 7/10 | #5 cond. | **YES** | 43.0% ⚠️⚠️ | **€72 000** | €4 000 | 3 ⚠️ |
| H5 | Coaches productizing | 6/10 | **#1 strong** | **YES** | 57.8% ✓ | €37 200 | **€1 500** | 4-5 |

**Cross-cell tension (preserved, NOT averaged):**
- mgmt-expert: H1 highest by ICP-fit + visibility + leverage-multiplier story
- investor-expert: H5 #1 by unit-econ; H4 has best LTV but GM borderline
- engineering-expert: zero-delta cluster = H2 + H4 + H5; isolated tech-debt = H1
- systems-expert: H4 acquisition (podcast guesting) = dual-leverage; H5 best CAC (referral)

---

## §4 Acquisition Path Variants — 6 Paths

> Все 6 путей — варианты для рассмотрения. Phase-1 capacity = ~2 параллельных пути max (D26 solo trajectory). Per Senge 11 laws: heavy cold outreach генерирует **«cure worse than disease»** риск — деградирует production capacity (60-80% Ruslan-time should be production per audio_475). [src:systems-expert C3]

| # | Path | € cost | Ruslan-hrs/wk | Time-to-first-signed | Conversion hypothesis | Feedback loop | Meadows leverage | Ashby variety | Phase-1 fit |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Cold outreach (LinkedIn/email)** | ~€0 | 5-8 | 6-12 нед | 200→20→5→1-2 (0.5-1%) | Balancing (−); reputation decay | L11 (params, weak) | Сжимает | Yes-with-test |
| 2 | **Podcast guesting** | ~€0-500 | 3-5 | 8-16 нед (nonlinear) | 10 pitches → 2 episodes → 5-15 inbound → 1 signed/6mo | **Reinforcing (+); compound** | **L8 (info flows)** | Adds | **Yes** |
| 3 | **Blogger collaborations** | €0-1000 | 8-12 (period of) | 4-8 нед | 5-8 pitches → 2-3 pilots → 1-2 retainer (50-70% pilot→retainer) | **Reinforcing (+); referrals** | **L7 (strengthening loops)** | Adds | **Yes** |
| 4 | **Referral (warm intros)** | €0 | 1-3 | 4-8 нед | 20 contacts → 5-8 conv → 3-5 intros → 2-3 calls → 1-2 signed (20-30%) | Reinforcing (+) but bounded | L9 (delays) | Сжимает | **Yes** |
| 5 | **Content marketing (case studies)** | €0-200/mo | 3-6 | 12-24 нед | 10K reads → 100 engaged → 10 subscribers → 3-5 inbound/qtr → 0.5-1 signed/qtr | Reinforcing (+) long delay | L8 + L7 | Neutral | Yes-with-test |
| 6 | **Discovery call funnel (TOF)** | €0 | 2-4 | 2-4 нед (от trigger) | 10 calls → 3-5 qualified → 2-3 offers → 1-2 signed (20-30%) | Balancing standalone (−); reinforcing in composition (+) | L10 (stock structure) | Сжимает (intentional) | **Yes (conversion layer)** |

### Composition analysis (which paths reinforce, which compete)

**Composing pair A: Path 2 (Podcasts) + Path 5 (Content marketing).** Self-reinforcing — podcast эпизод поставляет material → Jetix производит artifacts через собственный pipeline → publishes как case study → case study attracts next podcast invitations. **Pipeline самодемонстрация:** Jetix производит собственный контент собственным pipeline.

**Composing pair B: Path 3 (Collaborations) + Path 6 (Discovery call).** Blogger-collaboration creates first warm leads + trust (L7); discovery call converts to retainer (L10). Без conversion mechanism (Path 6) collaborations create visibility без revenue.

**Composing triple C: Path 4 (Referral) + Path 3 (Collaborations) + Path 6 (Discovery call).** Optimal Phase-1 composition с минимумом Ruslan-hrs. Total load: ~12-18 hrs/wk vs 15-22 hrs/wk при добавлении Path 1 или 5.

**Competing pair: Path 1 (Cold outreach) vs Paths 2/3 (Podcasts/Collaborations).** Cold outreach 5-8 hrs/wk vs Podcasts 3-5 hrs/wk не могут одновременно выполняться на достаточном качестве при 6-8 hrs/day Jetix budget [src:decisions/JETIX-PLAN.md §3.8]. **Senge risk:** heavy cold outreach degrades production capacity → leverage-multiplier value prop становится не demonstrable.

### 3 рекомендуемых композиции (proposed for consideration — Ruslan picks)

**Variant 1 (conservative, minimum Ruslan-hours):** Path 4 (referral) + Path 3 (collaborations, 1 pilot) + Path 6 (discovery call). Total: ~14-18 hrs/wk. Time-to-first-signed: 4-8 weeks via referral.

**Variant 2 (compound-oriented):** Path 3 (collaborations) + Path 2 (podcasts) + Path 6 (discovery call). Slower start, builds long-term reinforcing loops. Total: ~14-20 hrs/wk. Time-to-first-signed: 10-14 нед.

**Variant 3 (hybrid sequential):** Path 4 (referral, sprint 2-4 нед) → Path 3 (collaborations once first result) → Path 2 (podcasts once first case). Sequential activation = minimal simultaneous load.

[src:systems-expert C3 §4 systems synthesis]

---

## §5 Pricing Tier Hypotheses

> L7 §2.2 baseline: Pilot €2-3K / Standard €4-6K / Premium €7-10K; 3-mo min commitment; 10% quarterly prepaid discount. [src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2.2]

### Сводная таблица вариантов (10 variants evaluated)

| Variant | GM impact | CAC impact | Phase-1 fit | Brigadier rating |
|---|---|---|---|---|
| V1a: €3K experimental floor | 41.7% ⚠️ fragile | Конверсия выше | yes-with-test (case study only) | 5/10 |
| **V1b: €5K operational floor** | **65.0% ✓✓** | Friction higher | **yes (operational standard)** | **8/10** |
| V2: Setup fee (€3K) + retainer (€3K) | 45.3% ⚠️ worse than flat | Lower entry barrier | no Phase-1 (worse unit-econ) | 3/10 |
| V3: Performance bonus (5% revenue uplift) | Нейтральный avg | Outcomes buyers attract | yes-with-test (1 experiment) | 4/10 |
| V4a: Productized Sprint €10K | 50.5% | Lower commitment | yes-with-test (retainer on-ramp) | 6/10 |
| **V4b: Retainer (baseline)** | **56.3% ✓** | Standard | **yes (primary)** | **9/10** |
| **V5a: 10% prepaid (baseline)** | 53.8% | Standard | **yes** | **8/10** |
| V5b: 15% prepaid | 48.5% | Better adoption | yes-with-test (first 2-3) | 6/10 |
| V5c: 20% prepaid | 45.3% ⚠️ | Best adoption | no | 3/10 |
| V6: 1-month trial +30% premium | 66.3% (trial mo) | Converts resistant | yes-with-test (selective; ≥34% conv-to-retainer required) | 6/10 |

[src:investor-expert C2 §5 detailed analysis]

### Investor recommendation (proposal — arithmetic only, not strategy)

**Operational standard Phase-1 (maximizes GM + revenue predictability):**
- **Floor: €5K** (Standard tier) для open outbound — **V1b**
- **10% quarterly prepaid discount** (V5a baseline preserve)
- **3-mo minimum commitment** (preserve baseline)
- **Retainer (V4b)** as primary format, не sprint

**Exceptions allowed для первых 2-3 клиентов:**
- Case study discount 20-25% → effective €3 750-€4 000 (above €3K floor; GM ≥40%)
- 15% prepaid (V5b) допустим для cash flow bootstrap
- 1-month trial (V6) при risk-averse buyer с explicit «trial → retainer» framing

**Variants to test (NOT all simultaneously):**
- Один Sprint €10K (V4a) как acquisition experiment (measure: conversion-to-retainer %)
- Один performance-bonus experiment (V3) при candidate с clear attribution methodology
- **Не тестировать setup fee (V2)** — unit-econ хуже без upside

### Pricing dissents preserved

**D-PS-3 (3-mo vs 1-mo retainer minimum):** Investor recommends 3-mo by default; но философ-эксперт сохраняет dissent — 1-mo может снижать first-close friction в cold start. Q-PS-09 адресует Ruslan напрямую. [src:philosophy-expert C4 D-PS-3]

---

## §6 Open Questions for Ruslan (9 Q-PS-XX — All Require ACK)

> Каждый вопрос явно маркирован **[RUSLAN ACK REQUIRED]**. Brigadier предоставляет framing-факторы, не предзаданные ответы. AI does not strategize per Левенчук + D2 §13. [src:philosophy-expert C4 §6]

### Q-PS-01: Какие 1-2 гипотезы тестировать первыми 30-60 дней?
**[RUSLAN ACK REQUIRED]**

Brigadier proposal в §7: H4+H5 paired primary; H1 conditional-add при warm network. Это предложение, не директива.

**Факторы для взвешивания:**
- **Тепло сети** — есть ли у Руслана уже знакомые в нужном сегменте? Тёплый контакт → CAC ≈ 0
- **Скорость сигнала** — какой сегмент даёт самый быстрый «да/нет/не сейчас»?
- **Контентный интерес Руслана** — voice-preservation gate возможен только при genuine interest
- **D10 совместимость** — гипотеза должна работать в EN сегменте
- **Unit-econ** — investor-expert ранжирование (H5 > H3 warm > H2 > H1 > H4); Ruslan может выбрать вне ранжирования по network/interest factors

### Q-PS-02: Pricing floor — €3K experimental or €5K operational?
**[RUSLAN ACK REQUIRED]**

- **€3K floor:** GM ~25% при 8 hrs Ruslan; снижает first-close friction. Допустим как «pilot pilot» discount, не operational floor. Если 3+ клиентов окажутся на €3K с Ruslan-hours overflow, GM коллапсирует.
- **€5K floor (investor recommendation):** GM 65%; LTV:CAC robust; повышает acquisition friction → требует case study OR warm referral channels.
- **Гибрид:** Первый pilot €3K «экспериментальная цена, ревью 3 мес»; остальные €5K.

### Q-PS-03: Acquisition path — какие 2 пути запустить параллельно?
**[RUSLAN ACK REQUIRED]**

Systems-expert предлагает 3 композиции (см. §4): Conservative (4+3+6), Compound (3+2+6), Hybrid sequential (4→3→2). Phase-1 capacity = ~2 paths max.

**Ключевой Ruslan-вопрос:** какие пути уже есть в нетворке прямо сейчас? Выбор без учёта текущего состояния = ошибка.

### Q-PS-04: Voice-preservation gate — manual every cycle или sample-based?
**[RUSLAN ACK REQUIRED]**

- **Manual every batch (Phase-1 baseline):** absolute voice protection; throttles capacity at 3+ clients
- **Sample-based at scale:** требует ≥10 batches manual + formalized voice-checklist + Ruslan устанавливает % выборки
- **Hybrid:** manual для новых artifact types; sample для repeating patterns

**Brigadier discipline:** quality bar = только Ruslan устанавливает. Sample-based не «optimization» — это trade-off с прямым impact на Ruslan brand. Ни один agent не вправе recommend это как default. [src:philosophy-expert C4 D-PS-4]

### Q-PS-05: Existing Ruslan market analyses + competitor tables — when integrate?
**[RUSLAN ACK REQUIRED]**

- **Integrate next cycle (after hypothesis selected):** market analysis обогащает выбранную hypothesis card точными данными
- **Integrate after first pilot signed (empirical-first):** real signal важнее предварительного анализа
- **Integrate now if numbers load-bearing for first outreach decision**

§2 TAM/SAM/SOM здесь — directional. Cadence call = Ruslan picks.

### Q-PS-06: First 2 target accounts — Ruslan provides from network OR brigadier surfaces from public?
**[RUSLAN ACK REQUIRED]**

- **Ruslan-network (warm):** CAC ≈ 0, conversion higher; ограничен размер network
- **Brigadier surfaces longlist** из публичных данных по D22 criteria; higher CAC; scalable; **финальный выбор + контакт = только Ruslan**
- Hard rule: brigadier НЕ pre-selects target accounts. Executive decision.

### Q-PS-07: DACH-параллель — opportunistic or actively-rejected?
**[RUSLAN ACK REQUIRED — LOAD-BEARING DISSENT D-PS-1]**

D10 = EN+US first lock; «opportunistic» требует Ruslan-толкования:
- **A. Actively-rejected:** Phase-2 deferred; ноль Ruslan-hours на DACH
- **B. Opportunistic-passive:** если DACH-блогер сам приходит → evaluate per D22; не initiate
- **C. Opportunistic-active:** 10% Phase-1 ресурсов на DACH-pilot параллельно

**Load-bearing:** влияет на ICP scope в §3 hypothesis cards. Brigadier не интерпретирует locks самостоятельно.

### Q-PS-08: Workshop format standard — audio-only or video?
**[RUSLAN ACK REQUIRED — LOAD-BEARING DISSENT D-PS-2]**

- **Audio-only (Phase-1 default):** voice pipeline native; minimum tooling complexity; нет shorts/reels
- **Video standard:** unlocks shorts/reels Elite tier; требует tooling delta (engineering tech-debt per H1)
- **Client-choice:** maximum flexibility; increases internal process variability; Phase-1 risky

**Load-bearing:** меняет pricing tier structure + H1 hypothesis viability. [src:engineering-expert C5 video tech-debt]

### Q-PS-09: Retainer minimum — 3-mo standard or 1-mo experimental?
**[RUSLAN ACK REQUIRED — LOAD-BEARING DISSENT D-PS-3]**

- **3-mo minimum (baseline):** revenue predictability €50K gate; LTV:CAC 6:1 holds
- **1-mo experimental:** lower friction first engagement; 3× client volume needed for same revenue
- **Hybrid:** 1-mo pilot + auto-conversion to 3-mo at renewal

**Cash-flow impact direct:** 2 clients × €3K × 3 = €18K к gate. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md §10 Q5]

---

## §7 Brigadier Proposal — Proposal-Language Only

> **Это предложение, не стратегия.** Руслан рассматривает, выбирает гипотезу(и), модифицирует pricing / acquisition / timeline или полностью отклоняет starting-point. Brigadier НЕ принимает решение. Final selection emerges from Ruslan ack/modify/select cycle, NOT from brigadier. [src:philosophy-expert C4 patrol checklist; intake.md §2 hard rule 1]

На основании §2 market-analysis + §3 hypothesis cards + §4 acquisition paths + §5 pricing variants + cross-cell tension surfaced in §1 TL;DR, brigadier **предлагает рассмотреть** следующий starting-point как **один из возможных вариантов** для рассмотрения Русланом:

**Primary hypothesis pair (предложение):** **H4 (Podcast hosts) + H5 (Coaches productizing)** — paired starting hypothesis.

*Обоснование (one-sentence each):*
- **H4 reasoning:** podcast guesting acquisition mechanism = dual leverage (Ruslan audience-building + lead-gen одновременно); engineering native fit (zero-delta); highest absolute LTV €72K [src:investor-expert C2; systems-expert C3 Pair A]
- **H5 reasoning:** **investor-expert unit-econ rank #1** (LTV:CAC 24.8:1 referral, best CAC €1.5K, GM ≈ baseline); engineering native; cross-sell с AI-consulting natural; native D28 KB-compounding [src:investor-expert C2]

**Conditional add: H1 (YouTube educators)** if Ruslan имеет тёплый network в YouTube creator сегменте OR клиентский запрос приходит первым. H1 наивысший ICP-fit (mgmt-expert rating 8/10) но GM-fragile + video tech-debt → не recommended cold.

**Acquisition path (proposal):** **Composition Variant 1 (conservative)** — Path 4 (Referral, warm intros, 1-3 hrs/wk) + Path 3 (Blogger collaborations, 8-12 hrs/wk during pilot) + Path 6 (Discovery call as conversion layer, 2-4 hrs/wk). Total load ~14-18 hrs/wk; time-to-first-signed 4-8 weeks via referral; minimum Senge «cure-worse-than-disease» risk vs Path 1.

**Pricing tier (proposal):** **V1b €5K operational floor** + V4b retainer + V5a 10% prepaid (all baseline). Case-study discount 20-25% allowed для первых 2-3 пилотов → effective €3.75-€4K (above €3K floor; GM ≥40%). 3-mo minimum.

**First 30-day test (proposal):**
1. Identify 5-10 contacts from Ruslan-network в H4 (podcast hosts) + H5 (coaches productizing)
2. Run 3-5 discovery calls (Path 6) — measure: response rate to outreach + qualified-lead conversion + «what would actually close you?» refinement signal
3. Parallel: Ruslan pitches на 1-2 relevant podcasts (Path 2 dual-leverage; bootstrap H4 acquisition)
4. Goal at 30 days: ≥1 серьёзный retainer conversation (signed letter of intent OR active negotiation)

**Decision criteria (proposed continue / pivot / kill at 60 days):**
- **Continue H4+H5:** ≥1 signed retainer (≥3-mo, ≥€3.75K/mo effective with case-study discount) by day 60
- **Pivot to H1:** if YouTube creator inbound emerges OR Ruslan тёплый contact materializes AND H4+H5 outreach not converting (≤0.5 discovery calls/week)
- **Add H2 parallel:** if discovery calls reveal newsletter operators in network overlap (cross-sell potential)
- **Kill H3 Phase-1:** if no Ruslan-time available after H4+H5 active; defer H3 до Phase-2 с contractor

**Это предложение, не стратегия.** Ruslan рассматривает §1-§6, выбирает hypothesis(es), modifies pricing / acquisition path / timeline / decision criteria, OR rejects starting-point полностью. Brigadier does NOT decide. Final strategy emerges from Ruslan-only.

---

## §8 What This Document Does NOT Do (Anti-Scope)

- ❌ **NOT a final strategy** — Ruslan picks one of 5 hypotheses (or hybrid combination) or rejects entirely. Brigadier proposal in §7 = one option among several.
- ❌ **NOT a commitment to specific clients** — first 2 candidate accounts surfaced for Ruslan-decision (Q-PS-06). Brigadier does NOT pre-select target accounts.
- ❌ **NOT pricing committed externally** — all numbers internal options only. No public commitments. €5K vs €3K floor remains open until Q-PS-02 ack.
- ❌ **NOT a launch plan** — Phase 4 outreach activates only after Ruslan ack + per-direction strategic doc finalized. This document does NOT authorize outreach.
- ❌ **NOT M&A direction in scope** — Phase-2+ deferred per Ruslan 25.04.
- ❌ **NOT Notion writes / external publication** — internal swarm doc only.
- ❌ **NOT Ruslan voice-preservation gate overridden** — manual HITL Phase-1 default until Q-PS-04 ack. Sample-based is option, not recommendation.
- ❌ **NOT D10 EN+US lock revised** — DACH = opportunistic per Q-PS-07 interpretation only; D10 remains lock.
- ❌ **NOT AI-strategist mode activated** — Левенчук hard rule + D2 §13: AI does not strategize. This is OPTIONS PAPER. Ruslan strategizes.

---

## §9 Preserved Dissents (NOT averaged into consensus)

**D-PS-1 — English-only vs DACH bilingual.** Position A: D10 EN+US first, period. Position B: DACH specialist-blogger underserved, less competition; warm DACH contacts may have higher opportunity cost than focus dilution. **Empirical resolution:** if DACH contact emerges organically in 60 days → evaluate per D22; if not → D10 stands. **Q-PS-07 addresses Ruslan.**

**D-PS-2 — Audio-only vs video format standard.** Position A: audio-only Phase-1 simplicity (voice pipeline native; less tooling complexity). Position B: video unlocks shorts/reels for H1 ICP value-prop. **Empirical resolution:** first 2-3 pilots test both formats. **Q-PS-08 addresses Ruslan.**

**D-PS-3 — 3-mo vs 1-mo retainer minimum.** Position A: 3-mo revenue predictability + LTV:CAC 6:1 holds. Position B: 1-mo lowers first-engagement friction at cold start. **Empirical resolution:** first prospect negotiation gives signal — if prospect resists 3-mo, that's data. **Q-PS-09 addresses Ruslan.**

**D-PS-4 — Manual voice-gate vs sample-based.** Position A: manual every batch = canonical Phase-1 quality bar. Position B: sample-based at scale 3+ pilots = practical capacity-management. **Empirical resolution:** ≥10 manual batches with formalized voice-checklist required before sample question opens. **Q-PS-04 addresses Ruslan.**

**D-PS-5 (added by brigadier integration) — H1-vs-H5 cell-disagreement.** Position A (mgmt-expert): H1 highest by ICP-fit + leverage-multiplier story. Position B (investor-expert): H5 highest by unit-econ + best CAC. **Empirical resolution:** Ruslan selects based on network warmth + cash needs (Q-PS-01). Brigadier preserved both positions in §1 TL;DR + §7 proposal-with-conditional.

[src:philosophy-expert C4 dissent preservation]

---

## §10 Provenance (full chain)

```yaml
authoritative_sources:
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.2 lines 500-680",
     use: "Producer canonical: ICP, pipeline (research → script → footage → edit → repurpose), offer structure, open questions Q1-Q5"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "§2.2 lines 319-385",
     use: "Pricing tiers Pilot €2-3K / Standard €4-6K / Premium €7-10K; 3-mo min; 10% prepaid"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "§3.2 lines 1149-1216",
     use: "Unit-econ baseline: GM 56.3%, Ruslan-hrs/€1K = 2.0, LTV €36K, LTV:CAC 6:1"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§3.2 lines 310-322",
     use: "Блогер archetype: pain points, channels (LinkedIn / Referral / Podcast), message pattern"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§3.10 lines 425-438",
     use: "Teacher archetype: educator productization fit"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 D11 + §7.1 Блогеры",
     use: "D11 Producer mandate; archetype 11 criteria"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1-§3.4 §3.7",
     use: "Phase-1 actions: Producer pilot 1-2 first clients; Blogger collaborations start; D10 EN+US"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 / D26 / D27 / D28",
     use: "Company-as-code; team trajectory; fork-merge; query-driven KB"}
  - {path: "reports/review_2026-04-24.md", range: "audio_475 audio_508",
     use: "Producer center mandate verbatim; 60-80% production time data point"}
  - {path: "CLAUDE.md", range: "voice pipeline + KM MVP ops",
     use: "transcribe.py / extract.py / filter.py substrate; /ingest multi-format; /ask query-driven"}

cell_drafts:
  - swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-mgmt-integrator-market-hypotheses-proposal.md
  - swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-investor-scalability-economics-pricing.md
  - swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-systems-scalability-acquisition-pipeline.md
  - swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-philosophy-critic-open-questions-discipline.md
  - swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-engineering-integrator-pipeline-feasibility.md

confidence: medium
confidence_method: structured-rubric + canonical-source-trace + cross-cell triangulation
note: >
  TAM/SAM/SOM directional only — Ruslan holds authoritative market analyses (Q-PS-05).
  Unit-econ Phase-1 estimates — modeling, not pilot-verified.
  Brigadier proposal in §7 = one option; preservation of cell dissent is intentional.
```

---

## §11 What Happens Next

1. Brigadier writes `swarm/gates/AWAITING-APPROVAL-producer-services-strategy-options-2026-04-25.md` (1-line per hypothesis + 9 Q-PS-XX surfaced + brigadier proposal as proposal)
2. **HALT.** Brigadier does NOT proceed.
3. Ruslan reviews this OPTIONS paper.
4. Ruslan ack/modify/reject via gate file (any of: select hypothesis(es), modify pricing/acquisition/timeline, hybrid combination, reject entirely, request rewrite).
5. Final strategy doc emerges from Ruslan-only decision in subsequent cycle.

**Full-Auto NOT authorized.** Stage-Gated halt mandatory per intake §8 + D2 §13.

---

*End of OPTIONS paper. Brigadier integration discipline verified per philosophy-expert C4 patrol checklist (§7-discipline). Final selection authority = Ruslan-only.*
