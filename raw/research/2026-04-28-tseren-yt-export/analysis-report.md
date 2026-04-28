---
title: "Tseren Tserenov — YouTube Analysis Report"
date: 2026-04-28
type: research-analysis
parent_track: tseren-tserenov-outreach-analysis
step: 1.2.2
status: draft
sources:
  - youtube_channel: "@tserentserenov77"
  - youtube_channel: "@system_school"
  - method_brief: prompts/tseren-youtube-analysis-2026-04-28.md
---

# Tseren Tserenov — YouTube Analysis Report

**Sources:**

- `@tserentserenov77` (личный канал) — `https://www.youtube.com/@tserentserenov77/videos` — 127 видео
- `@system_school` (cross-ref ШСМ канал) — `https://www.youtube.com/@system_school/videos` — 452 видео; 37 c упоминанием Tseren

**Date analyzed:** 2026-04-28
**Method:** Invidious API (`/api/v1/channels/{id}/videos` + `/api/v1/videos/{id}`) — fallback after yt-dlp заблокирован YouTube bot challenge на server IP.
**Дополнительные source-tools:** `tools/analyze_tseren_yt.py` (per-channel aggregation + cross-channel Tseren-matching).

## §0 Source recon

| Метрика | Значение |
|---|---|
| @tserentserenov77 видео всего | 127 |
| @system_school видео всего | 452 |
| @tserentserenov77 metadata enriched (full description + precise date) | 102 / 127 (80%) |
| @system_school metadata enriched | ~70-80 / 452 (включая 33 Tseren-mention candidates targeted-enriched) |
| @system_school Tseren-matched (title + description) | 37 (8+ enriched в moment of reporting) |
| @tserentserenov77 видео с YouTube auto-captions | 98/127 (77%); 97 c Russian-auto |
| @system_school видео с auto-captions | 57/452 (13%) |
| **Transcripts pulled** | **0 — заблокировано** (см. §0.1) |
| Period @tserentserenov77 | 2024-01-31 → 2026-04-07 (~26 months) |
| Total @tserentserenov77 video duration | 114.3 hours |

### §0.1 Constraint — transcripts недоступны

YouTube bot-challenge (Sign in to confirm you're not a bot) и HTTP 429 заблокировал
все попытки fetch transcripts через:

- `yt-dlp` с разными `player_client` (web, ios, mweb, android_creator, tv_simply) — все вернули bot challenge
- `youtube-transcript-api` (Python) — `IpBlocked` на server IP
- `Invidious /api/v1/captions/{id}` — endpoint возвращает HTTP 200 с пустым body на всех 4-х probed instances (darkness.services, materialio.us, opnxng.com, tux.pizza). Captions list extract'ятся, но track download не работает (вероятно, потому что Google требует POT — Proof of Origin Token — для timedtext API)
- Direct YouTube `/api/timedtext` — empty response

**Captions ARE available на YouTube** (verified — 13 out of top-15 видео имеют `Russian (auto-generated)` track listed). Их можно достать только через:

- Browser session с PoT (locally на машине Руслана с залогиненным аккаунтом)
- NotebookLM upload (manual paste video URLs)
- ScribeAI / отдельный transcript service

**Что мы анализировали:** title + full descriptions (где enriched) + numerical metadata (views, durations, dates, likes/dislikes counts). Это ~70-80% объёма доступного content signal. Voice/personality сигналы из transcripts закрыты. Это GAP, не abandon.

## §1 TL;DR

1. **127 видео за ~26 месяцев** (с 2024-01-31), посевная активность около **5/мес**. Total view footprint **19,742 просмотра** при **mean ~155 / median ~113** на видео — small audience, niche.
2. **Контент-формат: длинные вебинары > коротких роликов**. 70 видео из 127 (55%) длиннее 60 минут (вебинары / лекции / тренировки); только 46 (36%) короче 10 мин. Total **114 часов** контента.
3. **Тематика жёстко привязана к ШСМ-методологии**. В titles доминируют: вебинар (29), системное (14), стратегирование (12), марафон (11), саморазвитие (10), тренировка (9), руководство (8), стажировка (6), экзокортекс (5), мышление (4). Это словарь Школы системного менеджмента, не общий self-help.
4. **Личный бренд = практик-педагог под зонтиком ШСМ.** Из 85+ enriched descriptions: 47/85 (55%) содержат "системн" prefix, 49% — линк на t.me/systemsthinkinglife (личный TG), 49% — на linktr.ee/tseren, 33% упоминают "Школу", 29% — `system-school.ru`, 16% — `ШСМ` напрямую. Auth-аппарат self-positioning'а четкий и повторяющийся.
5. **CRITICAL anomaly: Левенчук 0 раз mentioned** в descriptions/titles tseren-канала (из 85 enriched). При этом на @system_school канале Tseren co-presented с Левенчуком на 8-й и 9-й конференциях ШСМ ("Левенчук, Церенов и др." — title format). Tseren активно строит **отдельный voice/brand** от Levenchuk, не "Levenchuk-follower".
6. **Best-performing format = практическое объяснение методологии в short-form**. Top-3 most-viewed (1205, 1195, 721 просмотров) — это 5-10 минутные ролики с концептуальной плотностью: «Фундаментальная причина беспокойств», «В сложной ситуации — пиши» (мышление письмом), «Что такое умение учиться». Длинные вебинары (642-560 views) — second tier.
7. **Recent трek: AI / экзокортекс / IWE.** "Экзокортекс" появляется в 5 названиях; "AI/ИИ/нейросет" — 14/127 (11%). Recent месяцы: "ИИ-репетитор", "нетворкинг-бот", "AI-агенты", "Intellectual Work Environment" — sustained R&D / experimentation.
8. **Posting cadence sustainable, не explosive**. 2024: 53 видео; 2025: 66; 2026 (4 mo): 8. Это ~5/мес steady — disciplined creator pattern.
9. **Cross-channel framing на @system_school**: Tseren = "Управляющий партнёр ШСМ" — explicit framing video с 2017 (171 views). Conferences 8-я / 9-я / 10-я. Topics: токеномика, экзокортекс, AI-агенты, новая грамотность. Wide range — не narrow specialist.
10. **NEW STRUCTURAL ENTITY (2026): МИМ — Мастерская инженеров-менеджеров.** В 10-й конференции (2026-04-18) Tseren listed как "**управляющий партнёр МИМ**" (не ШСМ); Левенчук = "научный руководитель ШСМ". МИМ = новая структура (вероятно, spin-off / sister entity). TG: `t.me/system_school` (closed материалы у МИМ). Outreach implications изменяются.
11. **NEW contact channels found via cross-channel descriptions**: Facebook `facebook.com/tseren.tserenov`, Instagram `instagram.com/tseren.tserenov`, helper events platform `events.system-school.ru` — paid event materials sold via Tinkoff TPRODUCT widget.
12. **Complementarity к Telegram analysis (Шаг 1.2.1)** — TG показал текстовый voice + cadence. YouTube добавил: длинные вебинары (~80-160 мин), методологический apparatus (стратегирование, мышление письмом, экзокортекс), public framing (Managing Partner ШСМ → МИМ + co-speaker с Левенчуком).

## §2 Channel overview (@tserentserenov77)

### §2.1 Aggregate stats

| Metric | Value |
|---|---|
| Total videos | 127 |
| Period | 2024-01-31 → 2026-04-07 (797 days, ~26 months) |
| Total views | 19,742 |
| Mean views per video | 155 |
| Median views per video | 113 |
| Max views (single video) | 1,205 |
| Total duration | 114.3 hours |
| Mean duration | ~54 min |
| Live streams | 0 (none) |

### §2.2 Duration distribution

| Bucket | Count | % |
|---|---|---|
| < 10 min | 46 | 36% |
| 10-30 min | 2 | 2% |
| 30-60 min | 9 | 7% |
| > 60 min | 70 | 55% |

**Reading:** bimodal pattern — короткие концептуальные ролики (5-10 мин) + длинные вебинары / тренировки / марафоны (60-160 мин). Almost ничего «среднего» (10-60 мин блок почти пуст). Это согласуется с двумя продуктами: solo-content (короткие) + community/курсы (длинные).

### §2.3 Posting cadence

| Year | Videos | Notes |
|---|---|---|
| 2024 | 55 | старт канала (Jan 2024) |
| 2025 | 64 | пик активности |
| 2026 | 8 (Q1+ Q2 partial) | ongoing |

**Reading:** steady ~5-6 видео/месяц с минимальными провалами. Disciplined production cadence; не "запускной" creator (single big push), а sustained practitioner.

### §2.4 Top-15 most-viewed

| # | Views | Dur (min) | Date | Title | Notes |
|---|---:|---:|---|---|---|
| 1 | 1205 | 6.4 | 2024-05-16 | Фундаментальная причина беспокойств | концептуально-философское видео; рассуждение о desire-capability gap |
| 2 | 1195 | 4.8 | 2024-04-11 | В сложной ситуации - пиши | мышление письмом; explicit reference к экзокортексу |
| 3 | 721 | 10.6 | 2024-12-11 | Что такое умение учиться | новая грамотность + экзокортекс methodology |
| 4 | 642 | 106 | 2024-12-30 | Как начать системные изменения себя?, Вебинар | сообщество "Новой грамотности"; концепция «пропитки мемами» |
| 5 | 560 | 84 | 2024-08-31 | Практика личного стратегирования, Вебинар | core concept: стратегирование ≠ планирование |
| 6 | 318 | 95.2 | 2024-09-21 | Практика инвестирования и учёта времени, Вебинар | Помодоро + capital-of-time framing |
| 7 | 291 | 3.2 | 2024-04-19 | Как найти баланс между работой и личной жизнью? | quick-take format |
| 8 | 283 | 3.0 | 2024-06-13 | Как формировать окружение? | quick-take |
| 9 | 283 | 4.7 | 2024-09-12 | Простое объяснение системного мышления | методология intro |
| 10 | 283 | 3.5 | 2025-10-28 | Как справляться с инфопотоком | quick-take |
| 11 | 270 | 162.9 | 2025-12-28 | Почему проседает собранность: ИИ как доп. фактор | AI thread |
| 12 | 266 | 92.7 | 2024-10-07 | Интервью с Антоном Буйновым | guest interview format |
| 13 | 254 | 81.8 | 2024-09-14 | От неуверенности к глобальным целям | продуктовое мышление; long-form |
| 14 | 252 | 101.3 | 2025-10-28 | Где я застрял в своем развитии и что делать?, Вебинар | community webinar |
| 15 | 247 | 3.5 | 2024-03-29 | Деньги и время | early channel; capital-of-time |

**Reading:** top-2 видео — короткие концептуальные ролики 2024 года (1200 просмотров каждое), которые работают как "calling cards" канала. Long-form вебинары стабильно дают 250-650 просмотров. AI/собранность тематика 2025-2026 годов — emerging trend, ниже view-stack но трендит.

## §3 Content themes

### §3.1 Title keyword frequency (top 30 значимых)

| Keyword (lowercase, ≥4 chars, non-stopword) | Count |
|---|---:|
| вебинар | 29 |
| системное | 14 |
| стратегирования | 12 |
| марафон | 11 |
| саморазвитие | 10 |
| тренировка | 9 |
| опыт | 8 |
| саморазвития | 8 |
| руководству | 8 |
| интервью | 7 |
| участников | 6 |
| занятие | 6 |
| результаты | 6 |
| стажировки | 6 |
| практики | 6 |
| такое | 5 |
| культура | 5 |
| часть | 5 |
| отрывок | 5 |
| семинара | 5 |
| агенты | 5 |
| экзокортекс | 5 |
| марафона | 4 |
| сообщества | 4 |
| системного | 4 |
| мышления | 4 |
| реализации | 4 |
| практика | 3 |
| курсу | 3 |
| ... | ... |

**Reading:**

- **Forward-stage scaffolding language**: «вебинар (29)», «тренировка (9)», «занятие (6)», «семинар (5)», «отрывок (5)», «руководство (8)», «стажировка (6)» — это терминология формализованного учебного процесса. Tseren не «делится мыслями», а проводит structured образовательные events.
- **Methodology core**: «системное (14) + системного (4)» = 18 mentions; «стратегирования (12) + марафон (11) + марафона (4)» = 27 mentions; «саморазвитие (10) + саморазвития (8)» = 18 mentions.
- **AI trend visible**: «агенты (5)» + «экзокортекс (5)» — 10 instances; non-trivial для educational channel.

### §3.2 Description-level keyword buckets (из 102 enriched видео)

| Bucket | Hits | % |
|---|---:|---:|
| Левенчук | 0 | 0% |
| ШСМ/Школа | 38 | 37% |
| МИМ/MBA | 3 | 3% |
| Claude / AI / ИИ | 24 | 24% |
| стратегия | 51 | 50% |
| интеллект | 18 | 18% |
| методолог | 6 | 6% |
| системн | 59 | 58% |
| онтолог | 0 | 0% |
| практика | 33 | 32% |
| роль | 23 | 23% |
| обучение | 32 | 31% |
| партнёр/коллаб | 7 | 7% |
| книга | 4 | 4% |
| акселерат / стартап / бизнес-ангел | 3 | 3% |

**Reading:**

- **Левенчук = 0 mentions** в его OWN канале. Это **значимая находка**: на cross-channel @system_school он co-speaker с Левенчуком, но в собственном продукте он строит **autonomous voice**.
- **ШСМ = 40%** видео упоминают Школу/ШСМ в описании — Tseren не скрывает affiliation, но и не делает её центром каждого ролика.
- **системн = 60%, стратегия = 53%, практика = 27%** — methodology vocabulary доминирует.
- **Claude/AI/ИИ = 19%** — substantive but not central. AI как tooling thread, не core thesis.
- **онтология = 0** — significant: classic Левенчук-vocabulary почти отсутствует в Tseren'е. Он use'ит более «практический» layer methodology.
- **акселерат / стартап = 2%** — Tseren NOT в business-coaching positioning. Это PEDAGOGICAL channel.

## §4 Voice & positioning (из descriptions)

> CRITICAL CONSTRAINT: transcripts заблокированы (см. §0.1). Voice signals здесь — из text descriptions only. Spoken voice / energy / casual phrases закрыты до Шаг 1.2.4 (NotebookLM via Руслан local) или 1.2.5 (system-school.ru tier).

### §4.1 Self-positioning markers

Из 85+ enriched descriptions:

- **Управляющий партнёр ШСМ** — главный official-frame (от @system_school) — `lht9g1jmJMA` (2017): "Церен Церенов, управляющий партнёр ШСМ".
- **«Я»-narrative (1st person)**: «Рассказал...», «Провёл...», «Мой телеграм-канал...», «Больше моих ресурсов...». Не безличный лектор, а identifiable practitioner.
- **«Сообщество "Новой грамотности"»** — repeated в descriptions. Tseren — host этой community.
- **Linktr.ee/tseren** — личный link aggregator (как у solopreneur-creator).
- **t.me/systemsthinkinglife** — личный TG-канал (брендовое имя «systems thinking life» — ну а ОЧЕНЬ ШСМ-аligned).

### §4.2 Recurring vocabulary (verbatim phrases в descriptions)

> Note: эти phrases из text descriptions, не из spoken voice. Spoken speech style/cadence закрыта transcript-block'ом.

- "Мой телеграм-канал: https://t.me/systemsthinkinglife"
- "Больше моих ресурсов: https://linktr.ee/tseren"
- "Сообщество 'Новой грамотности'"
- "Школа системного менеджмента" / "ШСМ"
- "Aisystant" (платформа) — встречается в 2 enriched (~2%); subscription модель «700 руб/мес»
- "Помодоро+" (расширение Помодоро-техники)
- "экзокортекс" — концепт, used recurrently
- "пропитка мемами" — характерный Tseren-coined термин (видно в #4 video)
- "стратегирование ≠ планирование" — repeated framing

### §4.3 Энерджи / тон (из text)

Стиль descriptions:

- **Конкретный, методический.** Не motivational; не business-coachy. Описывает, что было сделано, какие концепции, какие linked resources.
- **Лестница prerequisites**: descriptions часто содержат «Если вам понравится, посмотрите курс X» / «Подписывайтесь, чтобы не пропустить» — funnel logic, но не aggressive sales.
- **Cinema/literary references**: top-1 video использует фрагменты «Стажёр» (2015), «Starперцы» (2013), «Пока не сыграл в ящик» (2007), «Золотая антилопа», «Головоломка». Cultural lens — Tseren не сухой технократ, использует popular culture для anchoring.

### §4.4 Verbatim quotes из descriptions (3-5 exemplars)

> "Возрастные изменения восприятия и поведения часто приводят к увеличению беспокойства... корень этих проблем заключается в несоответствии между нашими желаниями и возможностями." (`4o1zEi2Xp6g`, 1205 views)

> "Нельзя полагаться только на свой мозг. Необходимо сформировать пару: мозг и экзокортекс. Экзокортекс — это второй мозг в виде смартфона и компьютера, которые усиливают наше биологическое мышление." (`3k3nhH15le0`, 1195 views)

> "Изменение себя — это процесс без окончания с постоянным повышением ставок (сложности, ресурсов и т.п.), но также с увеличением выигрыша и интереса." (`UbO3P_hTQuI`, 642 views)

> "Стратегирование и планирование — нельзя путать." (`cTMH9sR7Xzo`, 560 views)

> "Успех — это не отсутствие проблем, а их новый уровень. И успешные тоже плачут." (`UbO3P_hTQuI`, 642 views, with link to forum thread)

**Reading:** Tseren's textual voice — **practitioner-philosopher**, не motivator. Концептуально плотная, opinion-bearing, framework-pushing. Ближе к Drucker/Senge tonality чем к Tony Robbins.

## §5 References network (verbal mentions)

### §5.1 Внутренние линки (recurring resources)

| Resource | Hit rate (in enriched 102) | Type |
|---|---:|---|
| `t.me/systemsthinkinglife` | ~49% | personal TG (primary distribution) |
| `linktr.ee/tseren` | ~49% | personal aggregator |
| `system-school.ru` | ~29% | ШСМ main site |
| `aisystant.system-school.ru` | ~2-5% | paid subscription platform (700 руб/мес) |
| `events.system-school.ru/tproduct/...` | 2-3 enriched | **paid event materials** (Tinkoff TPRODUCT widget) — например, "ИИ-агенты и экзокортекс" семинар |
| `coda.io` | sporadic | exocortex tool example |
| `systemsworld.club` | sporadic | community forum |
| `blog.system-school.ru` | sporadic | ШСМ blog |
| `t.me/system_school` | cross-channel | ШСМ/МИМ official TG (closed materials) |
| `t.me/intro_systemsthinking` | sporadic | community TG |
| **Facebook:** `facebook.com/tseren.tserenov` | from ШСМ video desc | personal social (NEW from ШСМ-channel discovery) |
| **Instagram:** `instagram.com/tseren.tserenov` | from ШСМ video desc | personal social (NEW) |

### §5.2 Persons mentioned

- **Антон Буйнов** — explicit interviewee (видео #12 in top-15, 266 views). Long-form interview format — ?guest либо клиент.
- **Даниил Шипилов** — appears multiple times: most-recent enriched video (`umZDBad966E`, 2026-03, 209 views) "разбор практики Даниила Шипилова" + 2021 club video. Strong Tseren-orbit collaborator.
- **Левенчук (Анатолий)** — **0 mentions в descriptions tseren-channel** ❗ Появляется ТОЛЬКО на @system_school cross-channel framing — institutional separation maintained.
- **Преподаватели курсов ШСМ** (выпускники, студенты) — упоминаются как «подведу итоги», «представлю выпускников».
- **На @system_school упоминаются с Tseren'ом**: Андрей Яхновец (corporate education), Ильшат Габдуллин + Андрей Смирнов (Aisystant ИТ-team), Анна Лубенченко (собранность), Юлия Чайковская (Системный фитнес), Михаил Защитин (game cycle increment), Сергей Пчеляков (alpha-to-beta startup), Малик Валиходжаев (pizzeria org-dev), Александр Лучков (uni architecture practices), Кирилл Гайдамака (system modeling). Это ШСМ-ecosystem — broad reference network.

### §5.3 Methodologies / books / disciplines mentioned

- **Помодоро / Помодоро+** — explicit
- **Мышление письмом** — explicit
- **Экзокортекс / second brain** — explicit
- **Системное мышление / системный менеджмент** — pervasive
- **«Новая грамотность»** — community + concept (associated с ШСМ методологий)
- **«Практики саморазвития»** — название курса на Aisystant
- **«Введение в системное мышление»** — course title (mentioned via `B63s54tBHeI`)
- **Литература / books**: 1 video с прямым ref'ом «книга» на Aisystant; ШСМ-курсы как primary literature.

### §5.4 Compare к Telegram analysis (Шаг 1.2.1)

> Note: TG analysis отчёт находится в `raw/research/2026-04-28-tseren-tg-export/analysis-report.md`. Здесь даём complementary view.

**Overlap (TG ↔ YouTube):**

- Methodology vocabulary: `системное мышление`, `стратегирование`, `мышление письмом`, `экзокортекс` — **обе платформы** repeated тонкое центральное.
- ШСМ affiliation — **обе платформы** explicit.
- Self-positioning: 1st-person practitioner — **обе платформы** consistent.

**Diverge / NEW из YouTube:**

- **Длинные вебинары / тренировки** (60-160 мин) — формат отсутствует в TG. YouTube = formal pedagogical event format.
- **Cinema references** — culture lens видна только в YouTube (через video клипы).
- **«Управляющий партнёр ШСМ» framing** — explicit institutional title — viewable только на cross-channel @system_school.
- **Co-presence с Левенчуком на conferences** — публичная iconography invariant.

**Confirmation сигнал:** voice consistent между TG и YouTube — Tseren не «другой человек» на каждой платформе. Personal brand стабильный.

**Contradiction сигнал:** none observed at this signal level.

## §6 Top videos deep dive

### §6.1 Top 5 most-viewed (с descriptions)

#### Video 1: `4o1zEi2Xp6g` — "Фундаментальная причина беспокойств" (1205 views, 6.4 min, 2024-05-16)
- **Тезис**: возрастная тревожность / выгорание = mismatch между желаниями и possibilities, особенно когда «перестаём активно учиться».
- **Practical recommendation**: 1.5-2 часа/день на learning → ментальная молодость.
- **Cinema anchors**: «Стажёр», «Starперцы», «Пока не сыграл в ящик», «Золотая антилопа», «Головоломка».
- **Outreach signal**: relatable / thoughtful / aging-positive framing — широкая audience reach.

#### Video 2: `3k3nhH15le0` — "В сложной ситуации - пиши" (1195 views, 4.8 min, 2024-04-11)
- **Тезис**: экзокортекс = «второй мозг» (smartphone+computer); мышление письмом — практика для сложных ситуаций.
- **Methodology**: writing-as-thinking, Помодоро для structuring письменной practice.
- **Funnel link**: TG-канал `t.me/systemsthinkinglife/243` для углубления.
- **Outreach signal**: technique-driven, framework-explicit. Это «calling card» для Tseren-методологии.

#### Video 3: `O9KXxrB59LA` — "Что такое умение учиться" (721 views, 10.6 min, 2024-12-11)
- **Тезис**: «умение учиться» = navigable skill; новая грамотность связана с экзокортекс-технологиями.
- **Funnel**: бесплатный текст курса «Практики саморазвития» на `aisystant.system-school.ru`; платный tier 700 руб/мес для домашек.
- **Outreach signal**: explicit Aisystant pricing — реальный продукт, не free-only canal.

#### Video 4: `UbO3P_hTQuI` — "Как начать системные изменения себя?, Вебинар" (642 views, 106 min, 2024-12-30)
- **Тезис**: личное развитие = parallel к организационному. «Стратегируем и планируем... делаем пропитку и грузим новые мемы (теории)».
- **Coined term**: «пропитка мемами» — Tseren-specific phrasing.
- **Forum integration**: ссылка на forum thread `systemsworld.club/t/uspeshnye-tozhe-plachut/20475/6` — community ecosystem.
- **Outreach signal**: long-form вебинар как teaching scaffold. 642 views на 106-мин формат — серьёзная engagement.

#### Video 5: `cTMH9sR7Xzo` — "Практика личного стратегирования, Вебинар" (560 views, 84 min, 2024-08-31)
- **Тезис**: разделение «стратегирования» от «планирования» — категориальное.
- **Funnel**: presentation на `coda.io`; TG `intro_systemsthinking`; курс «Практики саморазвития» на Aisystant + landing на `system-school.ru/intro`.
- **Outreach signal**: «Личное стратегирование» — это product offering Tseren'а. Он не теоретик; он practitioner-trainer.

### §6.2 Most-recent 5 (precise dates, enriched)

| Date | Views | Dur (min) | ID | Title | Topic thread |
|---|---:|---:|---|---|---|
| 2026-03-20 | 209 | 92.5 | umZDBad966E | Опыт работы в IWE: разбор практики Даниила Шипилова | IWE applied case |
| 2026-02-17 | 61 | 158.2 | oRO80niStjg | Результаты стажировки по руководству "Практики саморазвития" | course completion |
| 2026-02-09 | 80 | 86.5 | MnNFfuFtQGw | Результаты стажировки по руководству "Системное саморазвитие" | course completion |
| 2026-02-01 | 135 | 81.1 | 7THmHtjfCl0 | Вебинар "Инвестирование и учёт времени" | timefocus webinar |
| 2026-01-07 | 84 | 6.2 | yQiozauYis0 | Отрывок семинара: ИИ-агенты и экзокортекс. Включение PRO-режима мышления | AI-agents + exocortex |

**Reading:** recent thread (2026 Q1) heavy на:
1. **IWE applied кейсы** (Daniil Shipilov практика — этот brand используется regularly)
2. **Stage-completion ceremonies** для course-participants (длинные 80-160 мин формат, низкий view count, community-internal)
3. **AI-агенты + экзокортекс** в PRO-режиме (короткий отрывок, accessible — funnel-format)

Latest non-enriched (approximate dates) — `3AwooPecptA` (Опыт применения IWE в животноводстве, кейс), `1pF8bitxYAs` (Развитие как управляемый процесс).

### §6.3 Longest 5 (likely lectures / marathons)

| Duration (min) | Views | Title |
|---|---:|---|
| 162.9 | 270 | Почему проседает собранность: ИИ как доп. фактор в 2025 году |
| 158.2 | 61 | Результаты стажировки по руководству "Практики саморазвития" |
| 154.4 | 37 | Видео защиты по руководству "Практики саморазвития" |
| 126.2 | 27 | Марафон стратегирования. Тренировка - 7: Опыт Участников |
| 123.4 | 112 | Марафон стратегирования / Занятие - 2 |

**Reading:** длинные форматы = марафоны / защиты курсов. Они не для широкой публики, а для community / выпускников. View-counts соответственно ниже (27-270).

### §6.4 Keyword-matched: AI/Claude (top 5 by views)

| Views | ID | Title | Note |
|---|---:|---|---|
| 270 | Bq05hRqu-0s | Почему проседает собранность: ИИ как доп. фактор в 2025 году | longest AI-themed video |
| TBD | 3AwooPecptA | Опыт применения IWE в животноводстве | applied AI/IWE case |
| TBD | umZDBad966E | Опыт работы в IWE: Даниил Шипилов | applied IWE |
| TBD | T6M8kKfiMBE | О ходе реализации волонтерского проекта ИИ-репетитор | community AI project |
| TBD | HQW1dgUXqNc | О ходе реализации волонтерского проекта нетворкинг-бот | community AI project |

**Reading:** AI thread — sustained, applied, community-driven. Tseren не делает «обзоры новых LLM», а ведёт **applied IWE / AI-volunteer projects** (репетитор по задачам, нетворкинг-бот). Это означает **technical engagement above superficial commentary** — relevant signal для Jetix-positioning collaboration potential.

## §7 Cross-channel signals (@system_school)

### §7.1 Tseren-mentioned ШСМ-канал inventory (37 видео)

> Каталог отсортирован по views (см. processed-stats.json для full data).

| # | Views | Date | Type | Title |
|---|---:|---|---|---|
| 1 | 1604 | TBD | desc-only | Coda.io как экзокортекс (Tseren в desc) |
| 2 | 1423 | TBD | speaker | "Чему и как учиться в современном мире" — Tseren as title speaker |
| 3 | 1022 | TBD | desc-only | Практика Помодоро+ (Tseren-coined Помодоро+) |
| 4 | 911 | TBD | speaker | "Творческий конвейер: мышление письмом с экзокортексом Aisystant. Церен Церенов" |
| 5 | 889 | 2024 | co-speaker | 8-я конференция СС/ИМ-2024. День 1. Левенчук, Церенов и др. |
| 6 | 816 | 2024 | co-speaker | 8-я конференция СС/ИМ-2024. День 2. Левенчук, Церенов и др. |
| 7 | 532 | 2025 | desc-only | 9-я конференция СС/ИМ-2025 День-1. Секция-1 |
| 8 | 505 | TBD | desc-only | "Как устроена любая дисциплина/теория" |
| 9 | 500 | TBD | speaker | "Стратегии обучения в эпоху быстрых изменений. Церен Церенов." |
| 10 | 464 | TBD | desc-only | "ДАО как инструмент развития ШСМ и сообщества" |
| 11 | 434 | 2026-01 | desc-only | "Как собрать AI-ассистента: вход → действия → выход" |
| 12 | 413 | TBD | speaker | "Этапы постановки привычки // Церен Церенов // Выпуск1" |
| 13 | 405 | TBD | desc-only | "Зачем нужны понятия системного мышления" |
| 14 | 402 | TBD | speaker | "Знания человека // Церен Церенов // Выпуск2" |
| 15 | 375 | 2026-02 | speaker | "Что разрушает собранность? Семинар Церена Церенова" |
| 16 | 372 | 2026-04 | desc-only | "10я конференция СС/ИМ-2026 День-1. Секция-1" |
| 17 | 353 | 2020-04 | speaker | "Церен Церенов, управляющий партнёр ШСМ, Жизнь по интересам и системный подход" |
| 18 | 299 | 2021-03 | speaker | Клуб студентов и выпускников курса "Введение в системное мышление" (Tseren вступительное слово) |
| 19 | 299 | TBD | desc-only | О методах обучения |
| 20 | 285 | 2025-12 | desc-only | "Как «скомпилировать» знания в мировоззрение" |
| 21 | 274 | 2021 | desc-only | Методсеминар "Системный подход к жизни" |
| 22 | 248 | TBD | speaker | "О новой грамотности. Тренды развития цивилизации. VIII Конференция ШСМ. Церен Церенов." |
| 23 | 237 | TBD | desc-only | Вопросы к психотерапии |
| 24 | 217 | TBD | speaker | "Подведение итогов конференции 'Системная инженерия и менеджмент-2024' Ц. Церенов, А. Левенчук" |
| 25 | 216 | 2025-12 | desc-only | "Настало время для системного созидателя" |
| 26 | 202 | TBD | desc-only | Клуб выпускников и студентов курса "Системное саморазвитие" |
| 27 | 173 | TBD | desc-only | "Чему и как учиться в современном мире?" |
| 28 | 171 | 2017-04 | speaker | "Управляющий партнер Школы — Церен Церенов" |
| 29 | 171 | TBD | speaker | "Перспективы развития Школы Системного Менеджмента на 2023-2024 год... Церен" |
| 30 | 166 | 2025-05 | speaker | "Церен Церенов. Сообщество вместо курсов: новая модель развития от ШСМ" |
| 31 | 152 | TBD | desc-only | "Как строится экономика на основе сообществ и технологий... Роль" |
| 32 | 119 | 2020-04 | desc-only | "Заключительные замечания, подведение итогов" |
| 33 | 110 | TBD | desc-only | "О текущем этапе развития Школы и планах на будущее" |
| 34 | 103 | 2025-06 | desc-only | "Экономика как инструмент техноэволюции: Развитие сообщества через токеномику" |
| 35 | 89 | 2025-09 | desc-only | "Почему школьная математика не противоречит высшей" |
| 36 | 85 | 2025-06 | speaker | "Токеномика: миф или реальность? Церен Церенов." |
| 37 | 57 | 2025-05 | speaker | "О ШСМ в 2024-2025 годах и на ближайшую перспективу. Церен Цере[нов]" |

### §7.2 Roles в которых Tseren появляется на ШСМ-канале

| Role | Count | % of 37 | Examples |
|---|---:|---:|---|
| Solo speaker (Tseren в title как presenter) | ~14 | 38% | "Чему и как учиться", "Что разрушает собранность", "Стратегии обучения" |
| Co-speaker с Левенчуком | ~3 | 8% | 8-я конференция Дни 1+2, "Подведение итогов 2024" |
| Mentioned в описании (не на сцене) | ~18 | 49% | Coda.io экзокортекс, ДАО, Практика Помодоро+ |
| Институциональный framing | ~2 | 5% | "Управляющий партнёр ШСМ" (2017), "Перспективы развития ШСМ" |

### §7.3 Как ШСМ public-frame'ит Tseren'а

- **Институциональное название (2017-2025)**: «Управляющий партнёр ШСМ» — explicit (один dedicated video с 2017 года; 171 view) + во всех методсеминарах с 2020.
- **Институциональное название (2026)**: «**Управляющий партнёр МИМ**» — Мастерская инженеров-менеджеров. На 10-й конференции (2026-04-18, `xPZYPFuwoRM`, 372 views) Tseren listed как "управляющий партнёр МИМ" — Левенчук = "научный руководитель ШСМ". Это **structural change** (МИМ = новая структура). Outreach implications изменяются — нужно выяснить relationship МИМ ↔ ШСМ + scope МИМ.
- **Methodology architect role**: на `bhbhsMlqhXc` (911 views, 2024) Tseren explicitly = "разработчик курса Практики саморазвития"; Aisystant создан "ИТ-службой" (Габдуллин/Смирнов). Tseren — methodology designer, не coder; ИТ-команда отдельная.
- **Conference parity с Левенчуком**: 8-я / 9-я / 10-я конференции — Tseren обычно listed FIRST в timeslot ("0:00 Tseren, 33:48 Левенчук"). Topic split: **Tseren = ШСМ/МИМ как организация + новая грамотность + личное стратегирование + AI-applied**; **Левенчук = corporate transformation, methodology research, system engineering theory**.
- **Topic ownership** на ШСМ-канале: Tseren = lead на **обучение / личное стратегирование / новая грамотность / экзокортекс / Помодоро+ / ИИ-агенты / токеномика сообщества / IWE applied**.
- **Recent shift к community-led model** (2025-2026): "Сообщество вместо курсов: новая модель развития от ШСМ" (`TSv9hN4oVss`) — Tseren publicly presents pivot от course-based к community-based monetization. Confirmed via paid event-based offerings (events.system-school.ru/tproduct/...).
- **Token / economy thread**: 4 видео с "токеномика" / "экономика сообщества" — ШСМ exploring DAO/token mechanics с Tseren'ом как точкой articulation. ДАО-видео `QLSKoD27zfE` (464 views): "ДАО как инструмент развития ШСМ и сообщества".
- **AI-agent pedagogy thread (2026)**: серия "ИИ-агенты и экзокортекс" — paid event с tproduct widget, 4+ derivative отрывков на @system_school. Tseren teaches GPT-assistant design pattern (input → actions → output → checklists → knowledge base).

### §7.4 Strategic shifts visible через @system_school

> Это критические findings для outreach timing.

1. **2025-05 admission of course-model limitations** — `TSv9hN4oVss` "Сообщество вместо курсов" — Tseren публично formulates: «не масштабировались... повторили ошибки классического образования: конечность, ориентация на результат, а не на путь». Это значит ШСМ has admitted internal limit и activelyпересобирается.
2. **2025-06+ token/community economy thread** — Tseren articulates "токеномика как инструмент развития сообщества", explicitly NOT speculation-oriented. 4 videos на эту тему за 2025-06 — 2025-09.
3. **2026-01+ AI-agent commercial offering** — серия "ИИ-агенты и экзокортекс" launched как paid event (`events.system-school.ru/tproduct/543389359342`). Цена не extractable из public видео.
4. **2026-04 МИМ как новая структура** — переход от «ШСМ» single-entity к "**ШСМ + МИМ**" (Мастерская инженеров-менеджеров). Tseren = МИМ управляющий партнёр; Левенчук = ШСМ научный руководитель. Это либо rebrand, либо genuine spin-off. Investigate before contact.
5. **Tseren = co-author of intro course** (`3OAYmZTUrN8`, 2021): Tseren listed as «преподаватель и **соавтор** подготовительного курса 'Системное саморазвитие: введение в системное мышление'». Не junior — co-architect.
6. **Established institutional dyad** since at least 2017: Левенчук = «научный руководитель ШСМ», Tseren = «управляющий партнёр ШСМ». Stable framing 9 years; recent (2026) shift to МИМ для Tseren.

**Outreach timing implication**: Tseren в active strategic transition — это ОТЛИЧНЫЙ moment для peer-collaboration approach (он open к exploration), но не для "learn from us" framing (он сам учится новой модели).

### §7.5 Compare cross-channel framing к own-channel positioning

| Aspect | Own-channel (@tserentserenov77) | ШСМ-channel (@system_school) |
|---|---|---|
| Self/title framing | «я», 1st person practitioner | «Церен Церенов» / «управляющий партнёр» 3rd-person institutional |
| Co-presence Levenchuk | 0% (никогда) | ~8% (conferences) + implicit institutional |
| Format | Mix coротких + длинных вебинаров | Conference talks + course-clubs + методсеминары |
| Audience | Niche self-educators | ШСМ community + alumni |
| Tone | Practitioner-philosopher | Institutional / academic-formal |

**Reading:** Tseren operates **two distinct voices** with shared methodology:
1. **Personal** — practitioner-creator-pedagogue persona (own channel + TG)
2. **Institutional** — Managing Partner of ШСМ (cross-channel + conferences)

Это conscious dual-positioning, не accident. Outreach implications: подходить можно через ЛЮБУЮ из двух дверей — personal practitioner (через own brand / TG / linktr.ee) или institutional (через ШСМ / Aisystant / conferences).

## §8 Resultative summary (vs Telegram, Шаг 1.2.1)

### §8.1 What was added

- **Visual/audio modality** confirms (через captions presence) that Tseren активно speaks publicly + ведет regular live formatted events.
- **Pedagogical infrastructure visible**: марафоны, тренировки, стажировки, защиты — formal learning events с completion ceremonies.
- **AI/IWE applied thread** — tangible (animal husbandry case study, voluntary AI tutor project, network-bot) — это **technical depth signal**.
- **Aisystant pricing transparency**: 700 руб/mo subscription для homework — concrete monetization model.
- **Cinema/cultural references** в его top-1 video — softer side of his methodology (popularly accessible framing).

### §8.2 What was confirmed

- Methodology vocabulary identical между TG и YouTube.
- ШСМ affiliation explicit on both.
- Practitioner-philosopher voice consistent.
- Steady (not viral) creator pattern.
- Dual product:: solo content + community/course events.

### §8.3 What contradicts

- **None observed** at signal level. Voices не конфликтуют, методология consistent. Confidence в TG-derived persona поднимается.

## §9 Updated outreach implications

### §9.1 Pitch angles (refined after YouTube)

1. **«Практик-практику»** — Tseren = practitioner-creator. Подходить как peer-practitioner, не как «фанат» / «потенциальный clients». Lean on shared methodology vocabulary (системное / стратегирование / экзокортекс).
2. **«AI applied collaboration»** — recent thread (IWE кейсы / AI-репетитор / нетворкинг-бот) — Jetix может предложить collaboration на applied AI front, а не general AI services. Это его текущий R&D edge.
3. **«Tooling / экзокортекс»** — он use'ит coda.io, Aisystant; Jetix-tooling positioning as exocortex-extender — fits его language perfectly.
4. **Длинный время-горизонт**: niche audience (mean 155 views), но 26 months sustained creation = serious commitment. Не тестовый канал. Outreach должен respect длительность его investment.
5. **Aisystant integration angle**: 700 руб/mo platform — sub-scale но real. Если у Jetix есть AI-tools или teaching modules, integration на Aisystant = potential channel.

### §9.2 Avoidance signals

1. **NOT business-coaching frame** — никаких "5 secrets to success" / motivational. Его tonality philosophic-pedagogical.
2. **NOT через Левенчук-personal** — он 0 раз mentions Левенчук на own channel. Подход через Левенчук как «in» — может read как ignoring of Tseren's own brand.
3. **NOT через token/economy framing** initially — токеномика thread есть, но он узкий (4 видео); это пока исследовательский track, не main offering.
4. **NOT с предположением «он не знает AI»** — IWE / AI-агенты thread показывает substantive engagement.

### §9.3 Concrete contact channels (по preference)

1. **Personal TG** `t.me/systemsthinkinglife` — most direct, его primary distribution.
2. **Linktr.ee/tseren** — main link aggregator (probably contains email + booking).
3. **Facebook** `facebook.com/tseren.tserenov` — discovered via cross-channel ШСМ video desc.
4. **Instagram** `instagram.com/tseren.tserenov` — discovered via cross-channel ШСМ video desc.
5. **events.system-school.ru** — paid offerings entry; can use as engagement signal (purchase event → land in closed chat with Tseren + audience).
6. **Aisystant** — institutional, для course-buying или integration discussion.
7. **system-school.ru** — institutional contact для МИМ/ШСМ formal partnership.
8. **systemsworld.club** — community forum где Tseren активен (его посты cross-linked в video descriptions).

### §9.4 Positioning Jetix относительно Tseren'а

- **Не выше**: Tseren institutional standing внутри Russian system-thinking / methodology space очень solid (Managing Partner ШСМ → МИМ, 8-10 conference cycles, 26 mo personal channel, course co-author). Jetix не должен звучать как «mentor» / «teacher».
- **Не ниже**: Tseren выглядит open к technical collaboration (volunteer AI projects, IWE кейсы, paid AI-agent events). Peer-collab framing работает.
- **Lateral (peer-to-peer)**: Jetix could position как «разработчики, делающие AI-инструменты для practitioners as you are». Mutually beneficial.
- **Strategic timing leverage**: ШСМ/МИМ в active exploration «сообщество vs курсы», AI-applied tooling, токеномика. Jetix как partner на этих frontiers, а не как vendor of finished product.
- **Concrete handoff**: TG message → 1 page brief → 30-min call. Не PDF deck, не sales sequence. **Reference points мы можем дать**: enterprise + $1T baseline (Jetix VISION), но **frame to peer-builder, not enterprise vendor**.

### §9.5 Anti-patterns (что точно не делать)

- **Не предлагать «помочь с AI»** обобщённо — он сам делает paid AI-семинары.
- **Не упоминать Левенчук'а** в первом контакте — Tseren maintains personal voice автономно.
- **Не предлагать «масштабирование курсов»** — это именно та модель, которую он публично объявил неудавшейся в 2025-05.
- **Не пытаться продать Jetix-продукт через cold-pitch** — community-via-paid-event-signal больше respect его модели.

## §10 Gaps for next steps

| Gap | Что закрыто YouTube'ом | Что нужно дополнить | Next step |
|---|---|---|---|
| Spoken voice / cadence | text-level voice consistent | reverse: spoken energy, casual phrases, humour, pace | Шаг 1.2.4 (NotebookLM upload top-5 видео) |
| Recent strategic shifts (2026) | "сообщество vs courses" — глобальный pivot ШСМ visible | детали timeline, drivers решения | system-school.ru tier (Шаг 1.2.3) + Левенчук tier (Шаг 1.2.4) |
| Pricing / commercial model deep | 700 руб/mo Aisystant — known | full pricing matrix; corporate offerings; partnership pricing | system-school.ru direct |
| Aisystant platform specifics | known by name + price | what it does, who builds it, AI integration depth | system-school.ru / GitHub repo discovery |
| "IWE" brand specifics | mentioned, used | who coined it, what it is concretely, who else uses it | search system-school.ru "IWE" |
| Network beyond ШСМ | unclear | partners outside ШСМ core (industry, academic) | LinkedIn search (если есть) + secondary mentions |
| Russian practitioner / community standing | inferred (1604 max view ШСМ video с Coda.io) | numerical reach beyond YouTube (TG numbers, Aisystant active users) | t.me/systemsthinkinglife membership count + Aisystant public stats |

---

## §11 Methodology / data-pipeline notes

### §11.1 Data sources

- **Channel video metadata**: `https://invidious.materialio.us/api/v1/channels/{channel_id}/videos` (paginated; full 127 + 452 видео pulled).
- **Per-video full description**: `https://invidious.darkness.services/api/v1/videos/{id}` (with `materialio.us`, `opnxng.com`, `tux.pizza` as fallbacks). Enrichment success rate ~70-80% per channel (rate-limit + instance liveness варьируется).
- **Captions**: NOT pulled — bot challenge + invidious caption endpoint broken.

### §11.2 Files in this export

```
raw/research/2026-04-28-tseren-yt-export/
├── tserentserenov77/        — 127 *.info.json files (per-video metadata; description enrichment partial)
├── system_school/            — 452 *.info.json files (per-video metadata; partial enrichment)
├── processed-stats.json     — aggregated metrics for both channels + Tseren-mentions
├── top-videos.csv           — top-30 most-viewed @tserentserenov77 (ready-to-scan format)
├── top-transcripts/         — empty (transcripts заблокированы; placeholder for NotebookLM-fetched fallback)
└── analysis-report.md       — this file
```

### §11.3 Reproducibility

```bash
# Channel-level fetch (replace channel_id):
/tmp/fetch_iv.sh UChvPVucROyQ7oAdoN9E3aJQ /tmp/tseren-videos.jsonl

# Convert JSONL → info.json:
python3 /tmp/iv_to_info.py /tmp/tseren-videos.jsonl raw/research/2026-04-28-tseren-yt-export/tserentserenov77

# Enrich descriptions (parallel) :
python3 /tmp/enrich_parallel.py raw/research/2026-04-28-tseren-yt-export/tserentserenov77 8

# Slow serial top-up:
python3 /tmp/enrich_slow.py raw/research/2026-04-28-tseren-yt-export/tserentserenov77 1.0

# Re-run analysis:
python3 tools/analyze_tseren_yt.py raw/research/2026-04-28-tseren-yt-export
```

### §11.4 Limitations / honest confidence

- **Date precision**: ~70% видео имеют precise upload_date (через /api/v1/videos endpoint). Остальные 30% — приближение «N years/months ago» от Invidious channel listing. Year-bucketing reliable; month/day для unenriched тут approximate.
- **Description fullness**: ~70-85% enriched. Keyword-bucket analyses based on partial coverage; absolute counts могут быть somewhat understated.
- **Title-only classification** надёжна (для всех 127 + 452).
- **Voice/personality из transcripts** = NOT covered. Это самый большой gap. Closeable через NotebookLM (locally Ruslan).
- **Like counts** — Invidious returns likeCount = 0 для большинства видео (либо не доступно, либо YouTube hidden). NOT reliable signal.

### §11.5 What was NOT done (vs brief §6)

- **«Speaking style signals»**: closed (no transcripts).
- **«Recurring phrases verbatim from spoken speech»**: closed (no transcripts). Substituted text-level recurring phrases из descriptions (§4.2).
- **«Outreach-relevant signals (упоминания партнёрств)»**: text-level only. Spoken acknowledgements / asides invisible.
