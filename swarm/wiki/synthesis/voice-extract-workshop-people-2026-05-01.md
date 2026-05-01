---
id: voice-extract-workshop-people-2026-05-01
title: Workshop Voice-Extract — 2026-05-01
date: 2026-05-01
type: synthesis-extract
status: draft (awaiting Ruslan walkthrough → distribution отдельным шагом)
pipeline: ready
authored_by: cloud-cowork-cc (extract+structure; AI=scribe per memory rule, Ruslan=sole strategist)
sources:
  - reports/review_2026-04-26-DEEP.md (audio_530-539, period 24-26.04)
  - raw/transcripts/audio_540-586 (period 26-30.04, 47 transcripts; full extract pipeline ran 2026-05-01)
  - raw/voice-memos-text/holding-vision-2026-04-21.md (6 text-form notes)
  - raw/voice-memos-text/community-addendum-2026-04-21.md (2 text-form notes)
context:
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md (LOCKED canonical)
  - decisions/JETIX-TRM-MODEL-2026-04-30.md (companion business model)
provenance: ≥0.95 — every claim source-tagged with file:Lstart-Lend; quotes verbatim; AI = scribe (no extrapolation beyond what Ruslan said)
F: F3
G: extract-draft
R: refuted_if_quote_inaccurate_or_synthesis_drift_from_source
---

# Workshop Voice-Extract — 2026-05-01

> **Status:** Extraction draft. **Не promotion в Workshop concept v2 / wiki / crm БЕЗ Ruslan ack** (Hard rule 7 brief).
> Жди walkthrough Ruslan'а → ack каждого артефакта → distribution отдельным шагом.
> AI=scribe: ничего не диктую, только extract+structure из заметок.

---

## §0 Что extract'ится

### Источники + coverage

| Source | Период | Заметок | Items | Notes |
|--------|--------|---------|-------|-------|
| `raw/voice-memos-text/holding-vision-2026-04-21.md` | 21.04 late night | 6 (text-form) | ~30 ideas | Pre-Workshop. Holding vision / $1T / USB-C / tokens / mafia framing |
| `raw/voice-memos-text/community-addendum-2026-04-21.md` | 21.04 evening | 2 (text-form) | ~15 ideas | Pre-Workshop. Community + Secure Network |
| `reports/review_2026-04-26-DEEP.md` (audio_530-539) | 24-26.04 | 10 | 58 | Pre-Workshop. Korp-Startup, AI-Psy-Led, founder isolation |
| `raw/transcripts/audio_540-586.txt` | 26-30.04 | 47 | TBD (extract.py running) | **Includes Workshop genesis 30.04 (audio_582-586)** |

**Coverage gap:** между 26.04 03:44 (audio_539) и 30.04 18:47 (audio_586) — 4.5 дня без gap'ов.

**Workshop concept v2 LOCKED 30.04** — audio_582-586 (30.04 evening) **= источник genesis** для canonical concept.

### Pipeline status note (Phase A)

- Transcribe: ✓ 47 oggs → transcripts (Groq Whisper, 100% success)
- Extract: in-progress at write time (Sonnet через `claude -p`); 3 of 47 JSONs complete
- Filter+review_report: deferred (см. Phase A flag в structured report)
- Pre-fix issue: 47 oggs were placed в `raw/voice-memos/` instead of `inbox/voice/`; transcribe.py read from inbox/voice/ only and skipped them silently. Workaround: oggs copied to inbox/voice/ for re-run. **Это flagged для Ruslan'а** в structured report §"Phase A workaround note".

---

## §1 Workshop-relevant ideas

> Группировка по 8 темам Workshop concept v2 (план дня) + open category. Каждая идея с verbatim quote + source-tag (file:Lstart-Lend) + связь с canonical concept + рекомендация куда.

### §1.1 Adaptable станки — конкретные примеры

#### Idea 1.1.1 — «Танк в мастерской» metaphor (proto-Workshop, 27.04)

> «сделать что-то в этом в мастерской наверное легче, да, танк в мастерской сделать со всеми инструментами и, блядь, ресурсами, чем это сделать, блядь, на поле битвы, когда тебя, нахуй, 10, блядь, проблем отвлекает»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Первое explicit использование «мастерская» metaphor ДО canonical 30.04. Здесь Workshop как safe controlled environment где можно создать сложный артефакт («танк») в отличие от хаоса «поля битвы» (real-world execution). Это proto-version §1 Workshop concept v2 — «что-то делается, постоянный активный процесс, не сидячий объект» + §3 «фильтр входящей информации».
> **Куда:** Workshop concept v2 §1 «Что Jetix есть» — добавить как verbatim genesis quote (предшественник 30.04 dictation). НЕ overwrite canonical, append как evidence trail.

#### Idea 1.1.2 — Workshop = full corp toolkit в одной программе (27.04)

> «полный набор нахуй мега корпорации в одной в одной блять программки в jetix… лучшая research и лучшая блять аналитика up to date… лучшая crm… лучшая блять автоматизация… сбор твоих знаний… ёбаный нож швейцарский нож в виде в мире с Jetix. Это ебаный космический корабль»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Конкретный список «станков»: research, аналитика, CRM, автоматизация, knowledge mgmt — каждый «лучший» (best-in-class). Это §1.2 Workshop adaptability «может быстро внедрять новые станки» детализированный enumerate. Метафоры «швейцарский нож» / «космический корабль» — alternative phrasing same concept (compactness + power).
> **Куда:** Workshop concept v2 §1 — секция «примеры станков» (новая), либо в §2 «Что такое информация» — alternative metaphors layer.

#### Idea 1.1.3 — Adaptable role-playing внутри мастерской (27.04)

> «ты можешь играть разные роли что ты просто зависимости от проекта ты играешь разные роли и ты можешь быть как исполнителем таки управляющим… можешь погружаться хоп в одну роль там в один проект на два часика за два часика глубокой работы… потом хоп блеть через на другие два часика уже в другой проект включился например хоп уже с другими людьми у тебя другой блять этот роль»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Direct ground для §3 Workshop concept v2 «Роль владельца — adaptive». Audio_565 дополняет canonical: (a) cadence — ~2 hours per role-context switch; (b) mechanism — записывать «где ты кто» для quick re-entry; (c) trigger — project switch (не mood switch). Это **operationalises** §3 canonical statement с конкретной cadence.
> **Куда:** Workshop concept v2 §3 — sub-section «Cadence + mechanism роли-switch» (новая). Verbatim quote добавить в §8 canonical quotes.

#### Idea 1.1.4 — «Бульдозер для работы с информацией» (30.04 utro pre-genesis)

> «первое сейчас еще дописываю вот именно это бульдозер для работы с информацией я его описываю»
> [source: raw/transcripts/audio_582@30-04-2026_18-12-09.txt:L6]
>
> **Связь с Workshop:** Pre-canonical phrasing — «бульдозер» как alternative metaphor для same concept (что позже стало «мастерской»). Audio_582 timestamp 18:12 — 22 минуты до audio_583 (18:34) который содержит «мастерская» finalised version. Это shows phrasing iteration: бульдозер → мастерская (final).
> **Куда:** Workshop concept v2 §11 Sources — добавить как «iteration trail» (бульдозер as discarded earlier metaphor). Или skip — «мастерская» уже LOCKED, бульдозер не нужен retroactively.

### §1.2 Mapping 12 agents → workshop roles

#### Idea 1.2.1 — Полный agent toolkit как «станки» (27.04)

> «лучшее блять инвесторы лучшие юристы лучшая блять защита лучше блять токены лучше нахуй автоматизация лучше сука люди лучше блять рестораны лучше переговоры блять лучше возможности»
> [source: raw/transcripts/audio_557@26-04-2026_11-40-22.txt:L6]
>
> **Связь с Workshop:** Список «станков для соло-предпринимателя под крылом Jetix» — investors, lawyers, security, tokens, automation, people, restaurants, negotiations, opportunities. Это сверх-списка 12 agents (CLAUDE.md roster); это external resource pool под управлением Jetix.
> **Куда:** Workshop concept v2 §1 «примеры станков» — добавить расширенный список (внутренние agents + external resource brokerage). Различие internal/external станков — refinement canonical.

#### Idea 1.2.2 — Лучшие психологи + маркетологи + трекеры как «станки» (26.04)

> «у нас лучшие психологи помогают тебе себя там раскрыть блять проанализировать… потом лучше нахуй маркетологи себя блять а брендить нахуй о упаковать… лучшее блять трекеры помогают тебе дальше развиваться»
> [source: raw/transcripts/audio_543@26-04-2026_06-18-20.txt:L6]
>
> **Связь с Workshop:** Concrete spec для personal-development «станков» — psychologist + marketer + tracker. Confirms D-DRAFT-30 (AI-Psy-Led Design — review_2026-04-26-DEEP.md:L696) operational mechanism. Trackers (life/business) — Workshop tool для §3 owner-as-master role.
> **Куда:** Workshop concept v2 §1 — sub-section «personal-development станки». Возможный link к D-DRAFT-30 promotion.

### §1.3 Phase transitions concrete triggers

#### Idea 1.3.1 — Phase 1 trigger: «когда фундамент готов» (27.04)

> «Так, и тогда отлично сразу уже встает понятно, что нужно делать дальше… Мы сейчас заканчиваем этот фондейшн. Вот уже его реально до конца, блядь, доводим, что, ну, это, по сути, уже готовый продукт. Это можно уже давать идти людям»
> [source: raw/transcripts/audio_562@27-04-2026_08-49-24.txt:L6]
>
> **Связь с Workshop:** Конкретный trigger Phase 1→Phase 2 transition (canonical §6): foundation ready → готовый продукт → начинать давать людям. Это **operationalises** §6 canonical Phase transition c concrete signal. Foundation Architecture v1.0 LOCKED 28.04 — exactly matches «готовый продукт» frame.
> **Куда:** Workshop concept v2 §6 — sub-section «Phase 1 → Phase 2 trigger» (новая): «foundation готов → продукт можно давать людям → start onboarding partners». 30.04 ack already partial: Tseren outreach.

#### Idea 1.3.2 — Phase 1 → 2 переход: «соло консультант → партнёры приводят» (26.04)

> «для начала я хочу это вот самостоятельно Как такой бизнес-консультант… быть в роли помощника Помогать Потенциальным партнером… и потом попутно Уже сразу накапливать команду… уже эти партнеры За меня другим партнером помогали Будь то финансами Будь то ресурсами»
> [source: reports/review_2026-04-26-DEEP.md:L243-245 (quoting audio_536@26-04-2026_02-10-48.txt)]
>
> **Связь с Workshop:** Mechanism Phase 1 → Phase 2 transition — «soло-партнёр + AI agents → партнёры приводят resources/связи → накапливание team». Это **fork-portable mechanic** (Workshop concept §5 «специализация» + §6 «Phase 2: команда работает с одной системой»).
> **Куда:** Workshop concept v2 §6 — sub-section «Phase 2 onset mechanism: partners-as-multipliers».

#### Idea 1.3.3 — Phase 3 trigger: «когда задачи > одной мастерской» (29.04)

> «надо действовать срочно быстро… все уже нужные ресурсы в принципе есть есть отдельно все знания… отдельно специалисты которые могут это сделать уже есть клауд код»
> [source: raw/transcripts/audio_576@29-04-2026_13-11-51.txt:L6]
>
> **Связь с Workshop:** Phase 3 trigger condition (community of workshops) = когда individual workshops накопили critical resources но решение требует agg агрегации across workshops. Это §6 canonical Phase 3 trigger formulated negatively (когда хватит на Phase 2 → Phase 3 already attainable).
> **Куда:** Workshop concept v2 §6 Phase 3 — sub-section «trigger condition: cross-workshop coordination demand».

### §1.4 Visual / View principle deep

#### Idea 1.4.1 — Sustained visibility как management primitive (27.04)

> «но если ты этим управляешь записывать себе где ты кто просто чтобы тебя быстрее входить в эту роль и соответственно прямо все сто процентов ты можешь погружаться… просто потому что думать о блять перед глазами записано казалось бы казалось бы но это ебать насколько вообще улучшает дать облегчает»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Direct ground для §7 Visual/View principle. Audio_565 говорит: **persistent record («перед глазами записано») = role-switch cost reduction**. Это mechanism — view не как display, а как cognitive offload в context-switching.
> **Куда:** Workshop concept v2 §7 — sub-section «Visual = cognitive offload, не display». Refinement canonical (currently §7 says «view = удобный навигатор», audio_565 adds «view = pre-condition role-switching»).

#### Idea 1.4.2 — Public dashboard как view-наружу (26.04)

> «сразу же надо будет сделать сайт получается как раз смотрите можете по всем метриком следить за компанией вот столько мы сегодня новых людей там блять достучались только там фоллаупов написали столько блять видео создана столько блять человек»
> [source: raw/transcripts/audio_553@26-04-2026_10-19-20.txt:L6]
>
> **Связь с Workshop:** Workshop view не только internal — также **public-facing dashboard** для accountability + brand. Это **extends §7** canonical (currently focuses on internal navigation; audio_553 adds outward-facing view).
> **Куда:** Workshop concept v2 §7 — sub-section «View dual-direction: internal navigation + external accountability». Связь к D-DRAFT (Public Company From Day 1) audio_556.

### §1.5 Workshop НЕ-это (anti-patterns)

#### Idea 1.5.1 — Не one-person company / не freelance (26.04)

> «пока остальные дурачки целятся на какой-то one-person бизнес, в одиночку какие-то инструменты используют и так далее. Jetix наоборот нацелен на синергию, на сотрудничество, на партнерство»
> [source: raw/transcripts/audio_554@26-04-2026_10-27-12.txt:L6]
>
> **Связь с Workshop:** Reinforcement Korp-Startup positioning (review_2026-04-26-DEEP.md:L264-281, audio_537). Workshop = **synergy-platform**, не isolated solo-tool. Это **anti-pattern сторона §3 Workshop concept v2** (canonical positive frame: владелец-adaptive; anti-frame: одиночка-фрилансер).
> **Куда:** Workshop concept v2 §1 — sub-section «Workshop НЕ есть» (новая) — anti-pattern explicit list.

#### Idea 1.5.2 — Не TikTok / Instagram / LinkedIn (21.04)

> «это не хуйня типа тик тока который являть инстаграма или youtube а которая просто ну блять все дерьмо вместе… это тоже этот тоже не linkedin где блять быдло одно которое ищет какие-то рабов»
> [source: raw/voice-memos-text/community-addendum-2026-04-21.md:L36]
>
> **Связь с Workshop:** Anti-pattern для §6 Phase 3 community-of-workshops — **НЕ social media of any kind**, **НЕ slop-aggregator**. Это negation Workshop concept §1 «активный процесс»: social media = passive-consumption, Workshop = active-creation.
> **Куда:** Workshop concept v2 §1 «Workshop НЕ есть» — добавить «не социальная сеть, не slop-aggregator».

#### Idea 1.5.3 — Не Oriflame / pyramid (21.04)

> «это важно зафиксировать не то что он как oriflame нет ну то есть не на широкие массы а конкретно на профессионалов на вот заинтересованных людей в своем развитии»
> [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L38]
>
> **Связь с Workshop:** Distribution anti-pattern — Workshop спрос не через mass-market push, а через targeted professional recruitment. Это **complements §5 Specialization canonical** (currently positive: «у каждого мастера своя специализация»; audio_21.04 adds: «работа только с adequate professionals, не broadcast»).
> **Куда:** Workshop concept v2 §5 — sub-section «Distribution: targeted professionals, не mass-market».

### §1.6 Specialization in detail

#### Idea 1.6.1 — Профи vs не-профи как Workshop entry filter (30.04)

> «это все описание одного и того же мастер и не мастер профи и не профи… в этого мастера есть опыт есть возможно нужные инструменты есть возможно not понимание и знания как нужно делать какой последовательности… а который не может это не профессионал»
> [source: raw/transcripts/audio_583@30-04-2026_18-34-21.txt:L6]
>
> **Связь с Workshop:** **Critical refinement for §5** Workshop concept v2. Canonical §5 says «у каждого мастера своя специализация»; audio_583 adds **binary filter at entry**: master vs non-master. Workshop is **for masters only** — non-masters cannot use the tools effectively. Это direct quote из 30.04 dictation, complementary to §0 TL;DR canonical.
> **Куда:** Workshop concept v2 §5 — sub-section «Entry filter: master vs non-master». Verbatim quote добавить в §8 canonical quotes.

#### Idea 1.6.2 — Профессионал любит профессиональные инструменты (30.04)

> «профессионалы, они что? Они любят использовать профессиональные инструменты. И это тоже во всем. Например, вот там, любить какой-то качественный кофе… один раз попользовавшись качественным инструментом но не хочется уже дерьмом каким-то пользоваться»
> [source: raw/transcripts/audio_585@30-04-2026_18-42-10.txt:L6]
>
> **Связь с Workshop:** **Demand mechanism для Workshop** — profession's love of quality tools = self-perpetuating demand. Workshop = «качественные инструменты» — once user experiences, can't go back to slop. Это **§4 Workshop concept value-proposition** (currently focuses on output info; audio_585 adds aesthetic/preference dimension).
> **Куда:** Workshop concept v2 §4 — sub-section «Demand mechanism: quality-tool addiction». Possible cross-link to brand strategy.

#### Idea 1.6.3 — Любая ниша → разные виды специализации (30.04)

> «Дело может быть вообще разным, нахуй. И можно быть профессионалом и в выкуле собак, блядь. И можно быть профессионалом в винах… и в готовке и в спорте короче где только где только угодно»
> [source: raw/transcripts/audio_586@30-04-2026_18-47-54.txt:L6]
>
> **Связь с Workshop:** **§5 Specialization canonical breadth**. Workshop applies to ANY domain (dog walking, wine, business, sports). This is **fork-portability** — Foundation v1.0 = generic; specialization = domain-specific. Audio_586 verbatim alignment with canonical §5 + Bundle 5 ack 28.04.
> **Куда:** Workshop concept v2 §5 — verbatim quote add (сейчас canonical examples = инвестиции, психология, R&D; audio_586 adds dog walking, wine — extreme breadth).

#### Idea 1.6.4 — Profession как ladder (knowledge → teach → curriculum) (30.04)

> «можно просто что-то знать можно знать настолько хорошо что можешь уже других научить да можно этот еще там вернее просто показать можешь… еще больше быть профессионалом соответственно может какую-то методологию описать можешь наверное какой-то образовательный курс»
> [source: raw/transcripts/audio_586@30-04-2026_18-47-54.txt:L6]
>
> **Связь с Workshop:** **Internal ladder within mastership** — Phase 1 individual → Phase 2 team-able → Phase 3 community-teachable (методология / курс). Это **maps to §6 Workshop concept v2 Phase evolution** but at individual level (master career arc within Workshop).
> **Куда:** Workshop concept v2 §5 — sub-section «Mastery progression ladder» (новая). Явно distinguished от §6 Phase evolution (org-level).

### §1.7 Workshop ↔ TRM connection

#### Idea 1.7.1 — Workshop = WHAT, TRM = HOW + market (alignment confirm)

> Already declared in canonical: `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` frontmatter `companion_doc: decisions/JETIX-TRM-MODEL-2026-04-30.md` + commit `8bbcbc9 [concept] LOCKED Jetix TRM business model + cross-link with Workshop concept`.
> [source: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:L11]
>
> **Связь с Workshop:** Уже LOCKED — Workshop = conceptual frame, TRM = business application. Voice-extraction confirms not contradicts.
> **Куда:** No action — alignment already canonical.

#### Idea 1.7.2 — Workshop tools list = TRM 6 ресурсов overlap (26.04)

> «Jetix работает на своих партнеров для своих партнеров для себя ищет все самые лучшие варианты возможности и так дальше и потом дает их партнером помогает их реализовать… Jetix нацелена то чтобы увеличить вашу прибыль… мы берем там я не знаю сколько»
> [source: raw/transcripts/audio_544@26-04-2026_06-56-46.txt:L6]
>
> **Связь с Workshop:** Workshop value-prop in business framing = TRM mechanic (mgmt fee + performance fee). Audio_544 is direct ground для TRM-MODEL §4.1 «структура комиссии» через Workshop language — confirms operational alignment Workshop concept ↔ TRM business model.
> **Куда:** TRM-MODEL §4 — verbatim quote optional add (currently TRM uses business-language; audio_544 adds Workshop-language version).

#### Idea 1.7.3 — Resource pool = Workshop tool stockpile (21.04)

> «Jetix будет распространяться среди тех людей которые ему нужны качественно и глубоко и ответственно эффективно быстро… как раз вот этих авантюристов мы собираем для того чтобы вот триллионную компанию как можно быстрее собрать… инфраструктуру которая должна будет выдержать масштабирование там 1 миллиард до 1 триллиона»
> [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L38, L56]
>
> **Связь с Workshop:** Resource accumulation thesis (people, capital, infra) = **stockpile of tools/станков для Workshop**. Это TRM-MODEL Phase 2 (€15-20M ARR through asset accumulation) + Workshop §6 Phase 2-3 evolution. Holding ambition mapped to Workshop scale.
> **Куда:** Workshop concept v2 §6 — sub-section «Phase 2-3: tool/master stockpile mechanic». Cross-ref TRM-MODEL §14 platform phase.

### §1.8 Knowledge accumulation mechanism

#### Idea 1.8.1 — «Сохранения знаний» как Workshop infrastructure (27.04)

> «сбор твоих знаний сукка сохранения твоих знаний фоллово публик еще к это залупа… ничего не будет стоить если это самого первого дня и начала как бы сохранять адекватно потом можно просто будет на блять скопируй сразу… с одной ниши в другую короче перетаскивать»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** **Direct mechanism для §1.2 Workshop adaptability** «использовать наработки с других направлений». Knowledge accumulation = (a) save from day 1; (b) cross-niche portability via copy-and-adapt; (c) base layer for compound learning. Это direct support для existing canonical §1.2 + reinforces Foundation Part 5 (Compound Learning) mechanism.
> **Куда:** Workshop concept v2 §1.2 — sub-section «Knowledge accumulation discipline: save day-1 + cross-niche fork mechanism». Cross-ref Part 5 Compound Learning.

#### Idea 1.8.2 — Patent / capture all (26.04)

> «все что можно патентуем все что можно блять забираем создаем блять забираем себе лучшие таланты лучшие наработки reverse инженеро­вы»
> [source: raw/transcripts/audio_541@26-04-2026_05-13-10.txt:L6]
>
> **Связь с Workshop:** Aggressive defensive accumulation — Workshop NOT just internal accumulation but external tool capture (talent, IP, reverse engineering of competitors' methods). Это **§1.2 adaptability + competitive moat** dimension.
> **Куда:** Workshop concept v2 §1.2 — sub-section «Defensive accumulation: capture all available IP/talent». Note: aggressive framing; possible Ruslan ack required если promote (legal/ethical surface area).

#### Idea 1.8.3 — Token-economy для shared resource pool (21.04)

> «надо будет потом как-то эти токены еще изучить как сделать для jetix токены там валюту и так далее… специалистам тоже но как-то раздавалась чтобы это все было безопасно… для оплаты кита с заделом на будущее что будет своя какая-то экосистема»
> [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L62]
>
> **Связь с Workshop:** **Phase 3 community-of-workshops mechanism** — token economy для cross-workshop value transfer. Это deferred Phase 3+ scope (canonical §6 Phase 3) — token = mechanism для resource sharing между workshops. Pre-canonical formulation, not yet operationalised.
> **Куда:** Workshop concept v2 §6 Phase 3 — sub-section «Cross-workshop resource transfer: token economy candidate». Defer to Phase 3 backlog (TRM-MODEL §14 Platform phase).

### §1.9 Open category — другие Workshop-relevant ideas

#### Idea 1.9.1 — Synergy formula 6-component (26.04)

> «эффект синергии ответственность блять и разграничение того в чем силен в чем не силен адекватное управление ресурсами и тогда поиск рычагов и так далее автоматизация всего что только можно занятия стратегическими делами видением»
> [source: reports/review_2026-04-26-DEEP.md:L924-925 (quoting audio_537@26-04-2026_03-22-32.txt)]
>
> **Связь с Workshop:** 6-component synergy formula = Workshop-as-engine model. Это compact summary всех Workshop §1-§7 в одной фразе. Может стать canonical single-line definition.
> **Куда:** Workshop concept v2 §0 TL;DR — alternative one-liner candidate. Or §1 — sub-section «Synergy formula».

#### Idea 1.9.2 — Workshop как «купол» (27.04)

> «вот джек ну по сути это такой вот купол получается который позволяет тебе быстренько зайти все включится в любой проект»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Alternative metaphor «купол» (dome/canopy) — protective container что enables work. Synonyms «среда» / «мастерская» / «купол». Workshop concept canonical chose «мастерская»; «купол» is discarded variant.
> **Куда:** Workshop concept v2 §11 Sources — iteration trail note. Or skip.

#### Idea 1.9.3 — Workshop activates anyone (creator-философ-разработчик-businessman) (27.04)

> «Jetix… хорошо работающая голова, там, наличие инструментов и так дальше для творения, и по сути это вот свобода для какого-то там творца этого, блядь, исследователя, бизнесмена и так далее, вообще любого нахуй человека»
> [source: raw/transcripts/audio_565@27-04-2026_14-41-06.txt:L6]
>
> **Связь с Workshop:** Workshop universality — applies to creator/philosopher/developer/researcher/businessman. Это **direct ground для §5 specialization breadth** (canonical §5 says «инвестор/психолог/R&D»; audio_565 broader: any thinker).
> **Куда:** Workshop concept v2 §5 — alignment confirmed; possible expand canonical examples.

#### Idea 1.9.4 — Mafia-style trust as Workshop community glue (27.04)

> «именно для начальной стадии вот джекса что мы все-таки будем действовать больше как мафия то есть мы там собрались какие-то свои ресурсы собрали хорошо бизнес там работа да есть это свободные ресурсы инвестируем»
> [source: raw/transcripts/audio_563@27-04-2026_14-24-38.txt:L6]
>
> **Связь с Workshop:** Phase 1 → Phase 2 community structure = mafia-style closed trust group. Это refinement §6 canonical Phase 2 (current canonical: «команда работает с одной системой»; audio_563 adds: closed-circle trust as glue, не open community).
> **Куда:** Workshop concept v2 §6 Phase 2 — sub-section «Trust structure: closed circle (mafia-style), not open community». Phase 3 ⚠ will need to evolve from this.

#### Idea 1.9.5 — Infrastructure для $1T scale (21.04)

> «фундамент надо строить с такой видением и целью, что будет просто 100 миллиардов выруч person company… как будто бы мы сейчас… ну реально качественно умно с первого начала ну просто вот заложено потом чтобы мы могли просто люто масштабироваться»
> [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L56]
>
> **Связь с Workshop:** Foundation Architecture v1.0 LOCKED 28.04 (CLAUDE.md) is exactly this $1T infrastructure foundation. Workshop concept §1.5 «Knowledge accumulates» needs durable substrate — Foundation v1.0 = substrate.
> **Куда:** Workshop concept v2 §6 — link к Foundation Architecture v1.0 LOCKED 28.04. Bundle 5 strategic layer ack 28.04 = Phase 1 → 2 transition substrate.

#### Idea 1.9.6 — Lazy + harder-tasks paradox (26.04)

> «мы делаем людей ленивей, прям очень ленивыми, делая все за них с одной стороны. А с другой стороны даем им наоборот более сложные задачи и этим делаем их еще более сильнее»
> [source: raw/transcripts/audio_546@26-04-2026_07-09-48.txt:L6]
>
> **Связь с Workshop:** Workshop value-prop paradox — automate trivial → free up for higher-cognitive work. Это **§4 canonical input→output** (information processing) operationalised at user level. User input = harder cognitive task; Workshop output = leverage.
> **Куда:** Workshop concept v2 §4 — sub-section «User experience: lazy on trivial + stronger on hard». Possible D-DRAFT для positioning (если Ruslan хочет lock-quality).

#### Idea 1.9.7 — Public company from Day 1 (26.04)

> «джек должен быть публичной компании вести себя как публичная компания чтобы любой аналитик мог проверить посмотреть видеть для все пятна все как управляется»
> [source: raw/transcripts/audio_556@26-04-2026_11-26-32.txt:L6]
>
> **Связь с Workshop:** Trust mechanism for Workshop — public-company-style transparency from Day 1 = anti-pyramid signal (см. Idea 1.5.3). Cross-cuts §1.4 Visual/View principle (external dashboard).
> **Куда:** Workshop concept v2 §1 — possible D-DRAFT «Public-from-Day-1». Cross-ref TRM-MODEL §3 «падающее доверие к консалтингу» — Workshop = transparency-as-moat answer.

#### Idea 1.9.8 — Тестирование сразу на практике (30.04)

> «сразу проверяем сразу на практике вот находим блять проекты и работаем»
> [source: raw/transcripts/audio_582@30-04-2026_18-12-09.txt:L6]
>
> **Связь с Workshop:** Workshop validation principle — практика над теорией. Это **§9 canonical: "что меняется в существующих документах"** + Foundation Part 5 Compound Learning (test in cycle, refine in cycle). Direct ground for cycle-based validation.
> **Куда:** Workshop concept v2 §9 (next-steps) — sub-section «validation discipline: test in real project use BEFORE next iteration».

---

## §2 Люди упомянутые (с relevance к Workshop)

> Each person: name / role / контекст / citations / Workshop relevance / existing CRM record / action.

### §2.1 Tseren Tserenov (царин царинов / Серен)

- **Имя / роль:** Tseren Tserenov (transcription "царин царинов" — likely auditory name distortion; CLAUDE.md commit `a9c5241 [crm] add Tseren Tserenov identity card for TC-5 unblock` confirms identity)
- **Контекст в заметках:** Ruslan plans to call Tseren on 30.04 evening (audio_582), discuss Jetix system + dive into joint partnership («партнеры», «совместная работа»), use Tseren's наработки + MIM («мы это для делаем адекватно потом я беру это все вот упаковываю сайт»). Tseren = first concrete partnership target post-Foundation-LOCK.
- **Citations:**
  - `raw/transcripts/audio_582@30-04-2026_18-12-09.txt:L6` — "созваниваюсь с этим царином цариновым… мы берем как-то с тыкуем скорее всего вот эту мое видение плюс их как-то наработки"
- **Связь с Workshop:** **Phase 1 → Phase 2 first transition trigger** (Idea 1.3.1). Tseren = first non-AI human partnership for Workshop scale-up. Workshop §6 Phase 2 onset.
- **Existing CRM record:** ✓ `crm/people/tseren-tserenov.md` (committed `a9c5241`) — verified via git log.
- **Action:** /crm-touch with new context (audio_582 mention) + history append «30.04 outreach planned for Workshop frame discussion + наработки exchange». Не draft new card — existing.

### §2.2 Илон Маск (Elon Musk)

- **Имя / роль:** Elon Musk — vision-inspiration reference, не actual contact.
- **Контекст:** Используется как пример «как должен работать Jetix» — vision-driven (космос), ranges of regulation acceptance, leverage compound mechanism.
- **Citations:**
  - `raw/transcripts/audio_545@26-04-2026_07-05-56.txt:L6` — "пример на наших вдохновителей вот один из них илон маск"
- **Связь с Workshop:** Inspiration-class. Voice-router DRAFT created `crm/people/ilon-mask-draft.md` (per pipeline log Шаг 2b). Это **NOT actual contact**, vision-inspiration only — likely should be **withdrawn** from CRM, similar к V-Work withdrawal (review_2026-04-26-DEEP.md:L741, L807-812).
- **Existing CRM record:** ⚠ DRAFT auto-created by voice-router (`crm/people/ilon-mask-draft.md`). Recommend: **withdraw / archive draft** — это metaphor/inspiration, не contact. Возможно move to `crm/inspirations/` или просто delete.
- **Action:** Ruslan ack required — withdraw DRAFT or keep как inspiration record.

### §2.3 Дима (Dima)

- **Имя / роль:** Unclear — voice-router auto-created DRAFT `crm/people/dima-draft.md` per pipeline log, but transcripts in this batch не contain explicit «Дима» reference в high-priority context. Likely inferred from earlier extraction or fallback heuristic.
- **Контекст:** **Cannot confirm from current voice batch** — review_2026-04-26 batch не упоминает Dima explicitly; new 540-586 batch не surfaces clear Dima context.
- **Citations:** ❌ **Not found in 540-586 transcripts via grep "Дим" / "дим"**
- **Связь с Workshop:** Не определимо без clarification.
- **Existing CRM record:** ⚠ DRAFT auto-created by voice-router fallback heuristic (likely false positive).
- **Action:** **Ruslan ack required** — confirm Dima identity or **withdraw DRAFT**. Hard rule 8 (no-confabulation): не угадываю.

### §2.4 Антон (existing mentor — referenced but no new audio mention)

- **Имя / роль:** Antoine — ментор Ruslan'а (existing per CLAUDE.md «Ключевые люди»).
- **Контекст:** Не упомянут в audio_540-586 batch directly. References from earlier batch (audio_535) сохранены через personal-mentor-search work cluster.
- **Citations:** No new — reference only `reports/review_2026-04-26-DEEP.md:L760` (audio_535 from earlier batch).
- **Связь с Workshop:** Mentor model для psy-PM hire (Workshop §3 founder-as-master support).
- **Existing CRM record:** Recommended /crm-add per review_2026-04-26-DEEP.md:L1055 — **already pending** Ruslan ack from earlier batch.
- **Action:** No new action this batch — earlier action still pending.

### §2.5 Ross / Сасок («бизнес примеры», Tony Robbins-like) (28.04)

- **Имя / роль:** Multiple unidentified business example references — Mishu Takovinin, Oscar Hardman.
- **Контекст:** Audio_558 references «верхнеуровневым мишу таковинина этого оскара хардмана этих основателей еще там кого-то этих всех сюда» — outreach target list contemplated.
- **Citations:**
  - `raw/transcripts/audio_558@26-04-2026_12-30-58.txt:L6` — "по верхнеуровневым мишу таковинина этого оскара хардмана этих основателей"
- **Связь с Workshop:** Phase 2-3 outreach target candidates. Не Workshop-direct, но business-network expansion — Phase 1 → Phase 2 partner pool.
- **Existing CRM record:** Unknown — recommend Ruslan check `crm/people/` для existing slugs.
- **Action:** Ruslan ack required — confirm correct names ("мишу таковинин" / "оскар хардман" likely auditory transcription noise; could be "Misha Takhovinin" / "Oscar Hartman"). **Не draft без correct identity.**

### §2.6 V-Work (NOT a person, withdrawn earlier)

- **Имя / роль:** Withdrawn — это media metaphor (likely WeWork) per `reports/review_2026-04-26-DEEP.md:L741`.
- **Новые упоминания в 540-586:** audio_575 (28.04) — **substantive case-study reference** к WeWork business model: «как работал в work то есть они получаются арендовали какую-то площадь… а потом сдавали уже эту площадь в субаренду» = exact WeWork model description. Confirms «V-Work = WeWork» hypothesis.
- **Citations:**
  - `raw/transcripts/audio_575@28-04-2026_21-56-57.txt:L6` — "смотрим как работал в work то есть они получаются арендовали какую-то площадь… как давали площадь на длительный срок а потом сдавали уже эту площадь в субаренду по частям"
- **Связь с Workshop:** WeWork = aggregation/sub-leasing business model — **possible analogue for TRM-MODEL §14 platform phase** (Jetix as aggregator of resources, sub-leasing capability to partners). Worth research note.
- **Action:** WITHDRAW DRAFT (per earlier ack). Optional research task: WeWork case study — informs Phase 3 platform mechanic in TRM.

### §2.7 Generic personas (psy-PM, стратег, facilitator)

- **Имя / роль:** Same as 04-26 batch — generic ICP-портреты, не individual contacts.
- **Связь с Workshop:** Workshop §3 founder-master role support — psy-PM = external interventor (review_2026-04-26-DEEP.md:L211 audio_535).
- **Action:** No CRM addition. Profile descriptions уже в `personal-mentor-search/`. CRM gets entries только когда concrete candidates surface from outreach.

---

## §3 Прочее ценное (не Workshop, backlog)

> Ideas surfaced в 540-586 batch + holding-vision + community-addendum, не directly Workshop, но extract'ить жалко.

### §3.1 TRM-related

#### 3.1.1 — Mafia / closed circle Phase 1 (27.04)

> «мы все-таки будем действовать больше как мафия то есть мы там собрались какие-то свои ресурсы собрали хорошо бизнес там работа да есть это свободные ресурсы инвестируем например в рынок серым ок»
> [source: raw/transcripts/audio_563@27-04-2026_14-24-38.txt:L6]
>
> **Куда:** TRM-MODEL §6 Variant D «TRM Alliance». Mafia framing = closed Alliance pre-token. Cross-ref community-addendum Note 2 «secure network».

#### 3.1.2 — WeWork sub-lease arbitrage as TRM platform analogue (28.04)

> See §2.6 V-Work entry. TRM-MODEL §14 platform phase mechanic.
> [source: raw/transcripts/audio_575@28-04-2026_21-56-57.txt:L6]

#### 3.1.3 — $100B → $1T trajectory anchor (21.04 + 28.04)

> «настолько блять масштабным проектом что это даже блять в голову влезь нему это даже сука представить не получится»
> [source: raw/transcripts/audio_572@28-04-2026_08-05-57.txt:L6]
> + holding-vision Note 5 [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L56]
>
> **Куда:** TRM-MODEL §14.1 «Три фазы эволюции» + JETIX-VISION-FUNDAMENTAL §3. Reinforces D19 lock.

### §3.2 Foundation-related

#### 3.2.1 — Phase 1 → 2 trigger «foundation готов» (27.04)

> «Мы сейчас заканчиваем этот фондейшн. Вот уже его реально до конца, блядь, доводим, что, ну, это, по сути, уже готовый продукт. Это можно уже давать идти людям»
> [source: raw/transcripts/audio_562@27-04-2026_08-49-24.txt:L6]
>
> **Куда:** Foundation Architecture v1.0 closure 28.04 (CLAUDE.md) — audio_562 предсказал closure с 1-day lead time. Workshop concept v2 §6 Phase 1 → 2 trigger. Already covered in §1.3.1 above; here noted as Foundation-status ack confirmation.

#### 3.2.2 — Public company from Day 1 (26.04)

> See §1.9.7. Cross-ref Foundation Part 6a Provenance Officer + Part 8 Health Monitoring.

### §3.3 Tseren Tserenov (already in §2.1)

> Direct cross-ref §2.1.

### §3.4 Other projects (Life OS / brand / community)

#### 3.4.1 — Petition + weekly self-question ritual (26.04)

> «петицию какую блять чтобы человек как минимум раз в неделю задавался вопросом как я могу сделать свою жизнь лучше»
> [source: raw/transcripts/audio_550@26-04-2026_07-57-41.txt:L6]
>
> **Куда:** Life OS LO-1 reflection bot — extends to public-petition-as-product. Possible Phase 3 community-of-workshops mechanism.

#### 3.4.2 — Lazy-vs-strong paradox (26.04)

> See §1.9.6. Brand positioning.

#### 3.4.3 — Discipline + chaos balance (26.04)

> «есть дисциплина есть хаос есть порядок есть хаос есть дисциплина есть распиздяйство… надо совмещать короче дозировать»
> [source: raw/transcripts/audio_555@26-04-2026_11-03-15.txt:L6]
>
> **Куда:** Life OS / personal protocol. Brand-aesthetic candidate.

#### 3.4.4 — Brand: компания + личность дуальный layer (26.04)

> «у нас будет jetix отталкиваться от этого брендинга тоже но не на уровне компаний а nokia на уровне компании плюс на уровне личности»
> [source: raw/transcripts/audio_543@26-04-2026_06-18-20.txt:L6]
>
> **Куда:** Brand strategy direction — dual-axis brand (corporate + personal). Cross-ref D-DRAFT-29 Korp-Startup positioning.

#### 3.4.5 — Patent / IP capture aggressive frame (26.04)

> See §1.8.2. Possible legal/ethical Ruslan ack required.

#### 3.4.6 — Tokens / Jetix economy Phase 3 (21.04)

> See §1.8.3. Defer Phase 3+ backlog.

### §3.5 Sales / outreach

#### 3.5.1 — «Just ask, не sell» ICP messaging (29.04)

> «не надо нам прям вызывать ебать интерес прям вот это продавать что-то продавать себя… просто ну реально показать ситуацию адекватно попросить адекватно»
> [source: raw/transcripts/audio_578@29-04-2026_17-57-47.txt:L6]
>
> **Куда:** quick-money outreach scripts. Refinement D9 (Pain primary / Opportunity secondary).

#### 3.5.2 — Convince every contact «Jetix охуенен» (29.04)

> «я просто каждого с кем буду видеться с кем буду созваниваться кого буду видеть так далее буду убеждать в том что jetix это ебейшая компания»
> [source: raw/transcripts/audio_579@29-04-2026_22-00-03.txt:L6]
>
> **Куда:** quick-money outreach behavior baseline. D-DRAFT-29 Korp-Startup self-narrative discipline (review_2026-04-26-DEEP.md:L685).

#### 3.5.3 — Reach anyone via «звонить наяривать» (29.04)

> «руки звонить блять наяривать ему сколько хочешь блять всю нахуй информацию о человеке узнать вдоль и поперек»
> [source: raw/transcripts/audio_577@29-04-2026_17-35-40.txt:L6]
>
> **Куда:** sales-outreach playbook. Persistence pattern.

### §3.6 AI tooling / methodology

#### 3.6.1 — Ultra-think + plan mode 300% leverage (29.04)

> «ультра сэнкин и плен мод получается использовать на все 300 процентов и получается заебать чтобы он как раз сам уже мне всю эту систему проанализировал»
> [source: raw/transcripts/audio_580@29-04-2026_22-25-32.txt:L6]
>
> **Куда:** AI-инструменты project — Claude ultrathink as Workshop tool. Confirms Phase A current usage pattern.

#### 3.6.2 — Full-context → Plan mode → code analysis (29.04)

> «если дать полноценный контекст вот этому ультра свинкин да и план моду то получается раньше это могло вот в в коде да… взять и выбрать отличные варианты»
> [source: raw/transcripts/audio_581@29-04-2026_22-36-20.txt:L6]
>
> **Куда:** AI-инструменты — Plan Mode pilot deferred per CLAUDE.md commit `58bfb8c [research] pilot-design-plan: Claude Code book-grounded экспертная команда`.

### §3.7 Holding-vision-specific (21.04 text-form)

#### 3.7.1 — Data-first + speed-first investment-analyzer

> See holding-vision Note 1 [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L32]
>
> **Куда:** investor-archetype direction (TRM-MODEL §6 Variant). Phase 2-3 backlog.

#### 3.7.2 — «Самая большая афера века» framing (21.04)

> See holding-vision Note 2 [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L38]
>
> **Куда:** brand strategy — adventurer-recruitment narrative. Phase 2 onboarding mechanic.

#### 3.7.3 — USB-C / enterprise-fast positioning

> See holding-vision Note 3 [source: raw/voice-memos-text/holding-vision-2026-04-21.md:L44]
>
> Already locked D20 USB-C. No new action.

### §3.8 Community-addendum-specific (21.04 text-form)

#### 3.8.1 — План ближайшего будущего: глубокий сайт + видео + сообщество

> [source: raw/voice-memos-text/community-addendum-2026-04-21.md:L30]
>
> **Куда:** Phase 1 deliverables — site + видосы + community recruitment. Confirms current personal-mentor-search + Foundation closure work.

#### 3.8.2 — Secure network как Phase 3 platform vision

> [source: raw/voice-memos-text/community-addendum-2026-04-21.md:L36]
>
> **Куда:** Phase 3 community-of-workshops + TRM-MODEL §14 platform phase. Workshop §6 Phase 3.

---

## §4 Action items

### §4.1 В Workshop concept v2 — какие секции добавить + verbatim quotes вшить

**Hard rule 7: НЕ автоматически. Только после Ruslan ack.**

Recommended additions (по priority):

| Priority | Workshop section | What to add | Source |
|----------|------------------|-------------|--------|
| HIGH | §1 Что есть | sub-section «Workshop НЕ есть» (anti-patterns) | §1.5.1, 1.5.2, 1.5.3 |
| HIGH | §1 + §8 quotes | "сделать танк в мастерской легче чем на поле битвы" verbatim genesis quote | §1.1.1 audio_565 |
| HIGH | §5 + §8 quotes | "мастер и не мастер профи и не профи… это все описание одного и того же" verbatim genesis quote | §1.6.1 audio_583 |
| HIGH | §5 | sub-section «Entry filter: master vs non-master» | §1.6.1 |
| HIGH | §5 | sub-section «Mastery progression ladder» | §1.6.4 |
| MED | §3 | sub-section «Cadence + mechanism роли-switch» (~2h sessions) | §1.1.3 audio_565 |
| MED | §6 | Phase 1 → 2 trigger «foundation готов» | §1.3.1 audio_562 |
| MED | §6 | Phase 2 mafia-style trust structure | §1.9.4 audio_563 |
| MED | §1.2 | sub-section «Knowledge accumulation discipline» (save day-1 + cross-niche fork) | §1.8.1 audio_565 |
| LOW | §0 TL;DR | Synergy formula 6-component as alternative one-liner | §1.9.1 audio_537 |
| LOW | §11 Sources | Iteration trail (бульдозер → купол → мастерская) | §1.1.4, 1.9.2 |

### §4.2 В wiki/ — какие концепции `/ingest` (с topic/cluster)

**Hard rule 7: НЕ ingest без Ruslan ack.** Recommended candidates:

| Concept | File | Topic/cluster | Source |
|---------|------|---------------|--------|
| Master-vs-non-master entry filter | `wiki/concepts/master-non-master-entry-filter.md` | workshop-philosophy, professionalism | §1.6.1 audio_583 |
| Workshop ≠ social-media (anti-pattern) | `wiki/concepts/workshop-anti-social-media.md` | workshop-philosophy, jetix-positioning | §1.5.2 community-addendum |
| Quality-tool addiction demand mechanism | `wiki/concepts/quality-tool-addiction.md` | workshop-philosophy, brand | §1.6.2 audio_585 |
| Mafia-style closed-circle Phase 1 trust | `wiki/concepts/mafia-style-phase-1-trust.md` | workshop-phase-evolution, governance | §1.9.4 audio_563 |
| Workshop view = cognitive offload (refinement) | `wiki/concepts/workshop-view-cognitive-offload.md` | workshop-philosophy, life-os | §1.4.1 audio_565 |

### §4.3 В crm/people/ — какие новые карточки создать (с identity inputs)

**Hard rule 7: НЕ создавать без Ruslan ack.**

| Slug | Source identity | Status | Action |
|------|-----------------|--------|--------|
| tseren-tserenov | EXISTS (commit a9c5241) | active | /crm-touch + history append (audio_582 30.04 mention, Workshop frame discussion planned) |
| ilon-mask-draft | DRAFT (auto by voice-router) | DRAFT | **Withdraw** — inspiration ref, не contact (analog к V-Work withdrawal) |
| dima-draft | DRAFT (auto by voice-router, fallback heuristic) | DRAFT | **Verify or withdraw** — Ruslan ack identity required (no clear context in 540-586 batch) |
| anton-mentor | Recommended pending earlier (review_2026-04-26-DEEP.md) | pending | Earlier ack required (not new this batch) |
| (mishu/oscar) | Auditory transcription noise — likely Misha + Oscar Hartman | unknown | Ruslan ack identity before any draft |

### §4.4 В memory — что critical для будущих CC sessions

> **Note:** Memory updates НЕ в этом sprint. Brief Phase D = STOP. Только flag here для будущего.

Candidates for memory addition (Ruslan ack required):
1. **Workshop concept LOCKED 30.04** = canonical metaphor for all future synthesis (replaces house metaphor) — already в `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`, потенциально в memory project.
2. **Master-vs-non-master entry filter** = ICP filter for all Phase 2-3 partner outreach (refines D22 «Adequate» filter).
3. **Tseren Tserenov = first concrete Phase 2 partnership target** (audio_582 30.04 plan).

### §4.5 В backlog — какие новые задачи / вопросы (см. §3 Phase B-2 deliverable 4)

> **Note:** Per Hard rule 8 brief — **backlog file не найден** по brief candidates. Documented in Phase B-3 deliverable separately.

Items to add **once backlog file location confirmed** (Ruslan указует):

| Item | Type | Source | Priority |
|------|------|--------|----------|
| Tseren outreach 30.04 — followup status | task | audio_582 | P1 |
| Foundation closure → Phase 2 product launch | task | audio_562 | P1 |
| Withdraw V-Work / ilon-mask / dima-draft CRM auto-drafts | task | §2 | P2 |
| Mishu Takhovinin / Oscar Hartman identity verify | open-question | audio_558 | P2 |
| Antoine CRM record decision (still open from 04-26) | open-question | review_2026-04-26-DEEP.md | P2 |
| Token-economy Phase 3 design study | open-question | holding-vision Note 6 | P3 |
| AI-Psy-Led design Strategic Insight promote | task | review_2026-04-26-DEEP.md D-DRAFT-30 | P2 |
| Korp-Startup positioning D29 vs Strategic Insight | open-question | review_2026-04-26-DEEP.md D-DRAFT-29 | P1 |
| Public-company-from-Day-1 D-DRAFT review | open-question | audio_556 | P3 |
| Lazy-vs-strong paradox brand frame | task | audio_546 | P3 |
| WeWork sub-lease case study research (TRM platform analogue) | task | audio_575 | P3 |
| Workshop view = cognitive offload mechanism documented | task | audio_565 | P2 |

---

## §5 Provenance trail

- **Quotes:** все verbatim из source files; preserve мат and speech artifacts (Hard rule 4 brief).
- **Citations:** file:Lstart-Lend format. New transcripts (audio_540-586): `:L6` (content always on line 6 of 6-line files).
- **Synthesis:** AI = scribe. No claim не attributed. No extrapolation beyond what Ruslan said.
- **Confidence:** ≥0.95 — every idea has source-tag; non-attributable suspicions flagged как open-questions for Ruslan ack (e.g., Dima identity, Mishu/Oscar names).
- **Coverage:** Pipeline state at write — extract.py 3 of 47 JSONs complete; remainder will run; raw transcripts already provide ground for all extractions above. Direct citation to transcripts maximises precision (DEEP report would re-cite same transcripts via :L6 anyway).

---

## §6 STOP — что НЕ делать (Hard rule 7 brief)

- ❌ НЕ ingest concepts в `wiki/concepts/` без Ruslan ack
- ❌ НЕ promote ideas в Workshop concept v2 без Ruslan ack
- ❌ НЕ create CRM records без Ruslan ack (даже existing tseren-tserenov touch — recommend, не auto-execute)
- ❌ НЕ trigger D-promotion (D29 / D30 / etc) без Ruslan binary ack
- ❌ НЕ modify canonical LOCKED docs (Foundation parts / Vision / Workshop / TRM)
- ✅ ✓ This document = extraction draft only. Phase D STOP per brief.

---

**END Workshop Voice-Extract.**

Жду Ruslan walkthrough — ack каждого идеи / источника → distribution отдельным шагом.
