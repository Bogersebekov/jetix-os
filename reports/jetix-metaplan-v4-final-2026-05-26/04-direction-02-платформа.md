---
title: "MetaPlan V4 — Direction #2: Платформа (Personal OS / Team OS / Universal Business OS + AI Tools + ROY Swarm)"
date: 2026-05-26
type: phase-report-metaplan-v4
phase: 3
direction: 2
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
F: F2-F3
language: russian
status: draft-report
source_substrate:
  - decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md
  - decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
  - decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md
  - decisions/strategic/JETIX-WORKSHOP-MASTERY-NETWORK-CONCEPT-2026-05-26.md
  - decisions/strategic/OUTREACH-CONTENT-OUTCOMES-CTAS-2026-05-24.md
  - decisions/strategic/CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md
prose_authored_by: brigadier-scribe (claude-sonnet-4-6)
constitutional_posture: R1 surface only + R2 STRICT + R11 specs-only + R12 paired-frame STRICT + IP-1 STRICT
v4_delta: true
new_directions_integrated: [15-геймификация, 16-хакатоны]
---

# Direction #2 — Платформа

## Введение: мега-мастерская и станки на стене

Jetix — мега-мастерская мирового уровня: место, где люди становятся мастерами в эпоху AI, вместе двигают фронтир и не дают системе доить или запирать себя (R1, oneliner).

Три грани системы: **Мастерская** (ГДЕ — физическое или цифровое пространство с зонами и инструментами), **Мастерство** (ЧТО прокачивают — навыки, методология, практики), **Сеть** (КАК распределено — mesh-кооператив, pooling, Mondragón-экономика). Направление «Платформа» — это конкретная реализация грани **Мастерской** в части **инструментов на стене**: каждый инструмент, шаблон, OS-слой — это «станок». Его можно улучшить, заменить, поставить новый: «предложил → сообщество оценило → встал на полку с твоим именем». Инструменты не закрытые — fork-friendly, не lock-in.

Платформа Jetix — три Notion-слоя (Personal Core / Team Collaboration / Universal Business Foundation) плюс AI Tools mega-page плюс ROY swarm (17 агентов). Три слоя работают независимо (STANDALONE), соединяются через fast-connect opt-in — не лестница, а три отдельных станка. AI-стратификация O-182 встроена как базовый принцип: AI делает рутину (захват, сортировка, транскрипция, суммари, граф), человек — фронтир (решения, стратегия, ценностные суждения, работа с непонятным).

Маховик платформы живёт в трёх режимах — Build / Run / Scale (PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25). Сейчас: Build, средняя часть. Substrate готов. Наружу ещё не вышел. Видео A — блокер всего.

**V4-расширение.** В MetaPlan V4 платформа получает два новых «потребителя» — Direction #15 Геймификация (engagement-слой: Life Pulse dashboard, Habits, skill trees, achievement system) и Direction #16 Хакатоны (events-engine: stack baseline = Cloud Cowork + FPF + ROY swarm + AI Tools). Оба движка строятся поверх Platform как substrate. Это означает, что архитектура трёх слоёв больше не только «OS для одного человека или команды» — она теперь несёт нагрузку массового engagement-слоя и событийного движка. Этот сдвиг фиксируется в §V4-delta ниже.

---

## §V4-delta — V4-интеграция: Платформа как основа новых движков

### Платформа как технический substrate для Direction #15 (Геймификация)

Direction #15 Геймификация — engagement-слой, статус R12 HIGHEST (highest risk of extraction). Все компоненты геймификации (Life Pulse dashboard, Habits tracking, skill trees, achievement system, XP/badge mechanics) строятся как **слои поверх Platform**, а не как самостоятельные изолированные системы. Это не техническое решение архитектора — это ограничение substrate: данные прокачки участников живут в Platform-трекинге, не в проприетарной базе геймификационного движка.

**Почему это критично для R12.** Если статистика прокачки строится на изолированной геймификационной БД без Platform-backing, то при выходе участника его история прокачки теряется или становится инструментом удержания («твои достижения останутся здесь»). Это `fork_prevention_attempt` — HALT ≤5s. Platform-backing гарантирует, что участник уходит с полной историей своего роста.

**Технические точки интеграции (спецификация):**

| Геймификация-компонент | Platform-основа | Слой |
|---|---|---|
| Life Pulse dashboard | Daily Log DB (Layer 1) + Projects DB | Personal Core |
| Habits tracking | Daily Log (Habit relation) + Goals DB | Personal Core |
| Skill trees | Skills Exchange DB (Layer 2) + Knowledge Library (Layer 3) | Team + Business |
| Achievement system | Contribution Log (Layer 2 overlay) | Team overlay |
| XP / progress metrics | Project DB + Toggl sync | Layer 1/3 |
| Leaderboard (опц.) | Roles DB aggregated view | Layer 2 overlay |
| Badge system | Contribution-credit field (append-only) | Layer 2 overlay |

Детальная архитектура геймификационных механик — в Direction #15. Здесь фиксируется только: **Platform tracking = authoritative source. Геймификация = derived view, не источник.**

**R12 constraint для геймификации на Platform.** Любой achievement или badge, создаваемый геймификационным движком, должен быть fork-exportable в 30-day window. Achievement система не может быть механизмом удержания. `fork_prevention_attempt` в геймификации — отдельный класс нарушений, проверяется R12-автоматом.

### Платформа как технический substrate для Direction #16 (Хакатоны)

Direction #16 Хакатоны — events-engine, revenue + community flywheel. Stack baseline хакатона: Cloud Cowork (пространство/координация) + FPF (Foundation Protocol Framework — методологический scaffold) + ROY swarm (17 агентов, multi-angle поддержка участников) + AI Tools (20 инструментов в 4 кластерах). Этот stack означает, что **Platform = инфраструктура хакатона**, а не только инструмент для индивидуального участника.

**«За 2 часа: из лиц — в проекты».** Ключевая обещанная функция хакатона. Platform реализует её через:
1. Layer 2 Generic — быстрый онбординг команды: Roles DB (создать за 15 мин), Skills Exchange (каждый вводит offer/ask за 5 мин), Charter consent (подписать за 10 мин).
2. Layer 3 subset — базовый бизнес-scaffold за 30 мин: Strategy + Projects + People (три базы из 12 группы).
3. ROY swarm — brigadier доступен всем участникам хакатона (командный режим): задаёшь вопрос → multi-angle ответ → не теряешь время на поиск информации.

**Stack integration map (спецификация):**

| Хакатон-нужда | Platform-элемент | Время |
|---|---|---|
| Командный онбординг | Layer 2 Generic fork | 30 мин |
| Роли и договорённости | Roles DB + Charter consent | 20 мин |
| Проектный scaffold | Layer 3 subset (Strategy/Projects/People) | 30 мин |
| AI-помощь по ходу | ROY swarm через brigadier | on-demand |
| AI Tools инструменты | AI Tools companion (20 tools, 4 кластера) | on-demand |
| Трекинг прогресса | Projects DB + Daily Log (хакатон-режим) | on-demand |
| Post-hackathon follow-up | CRM touch (Layer 1 Contacts → CRM) | 15 мин |

**QF-совместимость (Quadratic Funding).** Direction #16 включает QF как механизм распределения revenue. Platform обеспечивает прозрачность через Layer 2 Jetix overlay: Group Finance DB + Decision Log. QF-результаты фиксируются как Decision Log entry с R12-аудитом.

**Multi-rhythm хакатонов.** Direction #16 предполагает три ритма событий: micro (2-4 часа), standard (1-2 дня), marathon (3-5 дней). Platform scaffold разной глубины для каждого ритма:
- Micro: только Layer 2 Generic (Roles + Skills Exchange)
- Standard: Layer 2 Generic + Layer 3 subset
- Marathon: полный stack (Layer 1 + Layer 2 + Layer 3 + ROY swarm)

### Кланы: каждый клан получает Platform-инстанс

В V4 кланы (lifecycle из Direction #14 Network) получают расширенное описание: Jetix = «качалка/склад» для кланов. Ценностной floor = триада (принципы Мастерства) + R12 (анти-экстракция) + уважение (respect minimum). Это означает, что каждый клан, входящий в сеть Jetix, получает:

**Что даёт «качалка/склад»:**
- Notion templates-пакет: Layer 1 Personal Core для каждого участника + Layer 2 Generic для команды + Layer 3 опц.
- AI tooling пакет: доступ к AI Tools mega-page + ROY swarm в командном режиме
- Методологический scaffold: FPF + workshop-методология (Direction #1 Workshop)
- R12 Steward: клан получает R12-watchdog (может быть участник клана, прошедший обучение)

**Что клан берёт сам (STANDALONE):**
- Конкретный состав ролей — клан решает
- Экономика распределения — клан решает в рамках Mondragón 5:1 cap
- Брендинг и название — клан решает
- Внешние инструменты — клан добавляет поверх Platform-baseline

**R12-floor для клана:**
Клан может кастомизировать Platform под себя при условии: не нарушает четыре action classes (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt). Любое нарушение — Steward HALT ≤5s, эскалация к Jetix Network Steward.

**Fork-and-leave для клана:**
Клан как единица может покинуть сеть Jetix, забрав полный Platform-инстанс (все Notion DB, все шаблоны, все данные команды). 30-day window. Никакого lock-in через Platform. Это не опция — это архитектурное требование: если Platform технически не позволяет клану уйти, это `fork_prevention_attempt` на системном уровне.

---

## §A — Главный документ

### 1-pager (≤500 слов) — спецификация

**Аудитория.** Первичная: методологи-партнёры T1 (Maxim/Oleg/Левенчук), тестеры-гуманитарии T3 (Дмитрий, Сева) — Build. Вторичная: любой founder, специалист, команда, которые хотят систему управления знаниями + работой без vendor lock-in. V4-дополнение: организаторы хакатонов, клан-лидеры, участники геймификационных когорт.

**Формат.** MD-файл + Notion-страница (вложена в Command Center) + возможно скриншоты трёх слоёв. Объём: ≤500 слов, одна страница Notion при стандартном шрифте.

**Разделы 1-pager:**
1. Что это за система (одна фраза-концепт: три станка, не лестница)
2. Три слоя — таблица: Layer 1 Personal Core / Layer 2 Team Collaboration / Layer 3 Universal Business Foundation. На каждый: кому, за сколько настроить, standalone-статус.
3. Companion: AI Tools & Lifehacks (что добавляет, 20 инструментов в 4 кластерах)
4. Как начать (3 шага: выбери слой → форкни шаблон → пройди onboarding-чеклист)
5. R12-гарантии (fork-and-leave, 30-day window, Mondragón cap — одной строкой)
6. V4-добавление: одна строка «Platform = основа хакатонов (#16) и геймификации (#15) — детально в соответствующих разделах»

### Long-form doc (≤5K) — спецификация

**Разделы:**
- §0 TL;DR + что такое STANDALONE и зачем это важно
- §1 Три слоя: архитектура, чем отличаются, когда брать каждый
- §2 Layer 1 Personal Core — Daily Log, Projects, Ideas, Contacts, Hypotheses, Goals, Finance, Strategic под-раздел, Weekly/Monthly ревью шаблоны. Схема полей (минимум → что добавить потом)
- §3 Layer 2 Team Collaboration — часть A Generic (Roles, Skills Exchange, Charter, Skill Briefing, Group Finance, Decision Log) + часть B Jetix overlay (10 ролей, 4 класса R12, 4 шаблона монетизации, Steward). Отдельно — Brand pattern для внешних команд.
- §4 Layer 3 Universal Business Foundation — 12 групп баз (Strategy / Finance / People / Projects / KM / Knowledge Library / Brand / Sales / Ops / Templates / Substrate / System), Vision/Goals страницы, Executive Briefing как главный артефакт
- §5 AI Tools companion: 4 кластера (захват / обработка / создание / анализ), таблица «что для какого слоя»
- §6 Fast-connect opt-in — как соединить слои, когда нужно
- §7 R12 дисциплина — где живёт (только Jetix overlay, generic нейтральна)
- §8 Onboarding-чеклист на каждый слой
- §9 Fork-пути: использовать Jetix overlay как есть / взять generic / сделать свой Brand pattern
- §10 Решения за пользователем (IP-1: роли ≠ исполнители, конфиг — за человеком)
- §11 V4-добавление: Platform как substrate для #15 и #16 — обзор точек интеграции
- §12 V4-добавление: Клан-инстанс — что входит в Platform-пакет для клана

---

## §B — Видео (5–15 мин)

**Аудитория.** Build-акторы: методологи, гуманитарии-тестеры, founders, которые устали от хаоса в Notion. Не для массы — для первых 5–20 человек.

**Hook (0–45 сек).** Визуальный контраст: стандартный перегруженный Notion-воркспейс с 50 полями vs три чистых пустых шаблона на экране. Вопрос: «сколько раз ты начинал систему и бросал через неделю?» Ответ без слов — показать три кнопки «Fork Layer 1», «Fork Layer 2», «Fork Layer 3».

**Сцена 1 (1–3 мин). Проблема.** Демо экрана: открываем типичный «продуктивность-воркспейс» с 7 связанными базами. Показываем: открыл → испугался → закрыл. Голос за кадром: «если шаблон сложнее задачи — он не помогает, он мешает».

**Сцена 2 (3–7 мин). Три слоя в действии.** Демо экрана: форкаем Layer 1 Personal Core. Показываем Daily Log (одна запись — 3 поля). Проекты (4 поля). Contacts. «Встал и работает за 30 минут». Переходим к Layer 2: показываем онбординг команды из 3 человек, Roles DB, Skills Exchange, Charter consent. Layer 3: Executive Briefing — весь бизнес на одной странице.

**Сцена 3 (7–10 мин). AI Tools + ROY.** Демо: voice pipeline (надиктовал → транскрибировано → структурировано → попало в Daily Log DRAFT, жду моего ревью). CRM touch через голос. ROY swarm: задаю вопрос → 17 экспертов дают multi-angle ответ. Явно показываем: «AI делает рутину — транскрипция, сортировка, граф. Решения — ты.»

**Сцена 4 (10–12 мин). Fork-friendly + R12.** Показываем: Layer 2 Jetix overlay → кнопка «Fork для своей команды». Объясняем: «никакого lock-in — берёшь generic без Jetix-терминов, делаешь своё. Выйти можно в 30 дней с твоей долей истории.»

**Сцена 4b (V4-добавление, 1–2 мин опц.).** Короткий анонс: «Это же основа хакатонов — за 2 часа из лиц в проекты. И engagement-система для прокачки навыков в геймификации живёт здесь же, в Platform tracking». Не демонстрировать детально — только обозначить связь, отослать к соответствующим направлениям.

**Closing (12–14 мин).** Ссылка на шаблоны (Notion-ссылки). Призыв: «выбери один слой, форкни, используй 7 дней, напиши нам что не сработало.» Явный стоп-сигнал: «не навязываем — если не зашло, просто скажи».

**Substrate.** Notion-шаблоны (три слоя), screen recording, голосовой комментарий, mermaid-диаграммы из NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2.

---

## §C — Курс

**Применимость: да.** Курс — это «как настроить и использовать платформу от нуля до системной работы».

**Формат.** Notion-страница со встроенными видео (5–7 мин каждый модуль) + текстовые инструкции + чеклисты. Проходится асинхронно. Опциональные live-сессии для Layer 2 (Team Collaboration требует живого онбординга).

**Skeleton модулей:**

| Модуль | Outcome | Материалы | Упражнение | Оценка |
|---|---|---|---|---|
| M0 Ориентация | Понять три слоя, выбрать свой стартовый | 1-pager + видео §B | Анкета «какой ты?» → рекомендация | Auto: выбор слоя зафиксирован |
| M1 Layer 1 Personal Core | Настроена личная система за 30 мин | Видео-демо Layer 1 + онбординг-чеклист | Завести Daily Log на 3 дня подряд | Ручной check: 3 записи есть |
| M2 Layer 1 Advanced | Подключить Weekly Review + Goals + Finance | Инструкции §2 long-form + шаблон ревью | Провести Weekly Review по шаблону | Ручной check: ревью заполнено |
| M3 Layer 2 Generic | Настроить командный воркспейс (Generic baseline) | Видео-демо Layer 2A + онбординг 5 шагов | Создать Roles DB + Skills Exchange для своей команды | Проверка: 3+ роли заведены, Charter consent подписан |
| M4 Layer 2 Jetix overlay | Понять монетизацию + R12 + Steward | Инструкции Layer 2B + R12 8 вопросов | Пройти R12-чеклист для своего проекта | Ручной check: 8 вопросов пройдены |
| M5 Layer 3 Universal Business | Видеть весь бизнес с одной страницы | Видео-демо Layer 3 + Executive Briefing | Настроить Executive Briefing: 4 ядерных раздела | Ручной: briefing заполнен |
| M6 AI Tools companion | Освоить 3–5 инструментов из 20 | AI-TOOLS-LIFEHACKS-MEGA-PAGE + live demo | Запустить voice pipeline один раз | Ручной: summary-latest.md создан |
| M7 ROY Swarm intro | Понять как задавать задачи рою | Видео-демо brigadier + примеры | Задать один вопрос через brigadier | Ручной: ответ получен, осмыслен |
| M8 Fast-connect opt-in | Связать нужные слои без страха | Инструкции fast-connect §6 | Сделать linked view из Layer 1 в Layer 3 | Ручной: view работает |
| M9 (V4) Platform + Геймификация | Понять как Habits/skill trees строятся поверх Platform | Ссылка на Direction #15 курс + схема интеграции | Связать Daily Log с Habit tracking | Ручной: habit entry создан |
| M10 (V4) Platform + Хакатон | Настроить командный scaffold за 2 часа | SOP-4 (ниже) + Layer 2 hackathon-mode | Провести мини-хакатон (2ч, 3+ чел.) | Ручной: Roles + Charter + Projects — все три готовы |

---

## §D — Книга

**Применимость: да, фаза Run/Scale.** В Build — рано. Пишем skeleton сейчас для проектирования.

**Формат.** Электронная книга (PDF + Notion-страница) или серия long-form статей, которые потом сшиваются. Русский primary, английская версия — перевод в Scale.

**Skeleton глав:**

| Глава | Тезис | Под-тезисы (3–4) | Формат |
|---|---|---|---|
| Предисловие | Почему системы управления знаниями умирают за неделю | Слишком сложно / не fit / нет петли обратной связи / нет защиты от эксплуатации | Narrative |
| Гл.1 Три станка | Personal / Team / Business — три независимых инструмента, не лестница | STANDALONE принцип / когда брать каждый / fast-connect как опция | Концепт + примеры |
| Гл.2 Personal Core | Личная система за 30 мин — минимум, который работает | Daily Log discipline / Projects как async tracker / Contacts без CRM-ада / Goals без стресса | How-to + антипаттерны |
| Гл.3 Team Collaboration | Честная команда: роли, навыки, деньги | Roles DB зачем / Skills Exchange не найм / Charter consent / Mondragón 5:1 | Концепт + кейс (IP-1) |
| Гл.4 Universal Business | Founder видит весь бизнес с одной страницы | Executive Briefing / 12 групп баз / Hypotheses as first-class / Vision/Goals как документ | How-to + примеры |
| Гл.5 AI как инструмент, не замена | O-182: AI делает рутину, человек идёт на фронтир | voice pipeline / ROY swarm multi-angle / что AI не делает (стратегию) / DRAFT-only discipline | Концепт + workflow |
| Гл.6 Fork-friendly системы | Как строить инструменты, из которых не страшно уходить | R12 anti-patterns / 30-day exit / fork protocol / вклад с именем автора | Принципы + чеклист |
| Гл.7 Маховик | Build → Run → Scale: кто крутит | Три режима в деталях / антиловушки каждого / R12-риск растёт с системой / защита быстрее роста | Стратегия (R1 surface) |
| Гл.8 (V4) Платформа как база сообщества | Кланы, хакатоны, геймификация строятся поверх трёх слоёв | Клан-инстанс / хакатон-stack / skill trees на Platform / QF-прозрачность через Layer 2 | Интеграция-глава |
| Заключение | Мастерская продолжается | Поставить свой станок / community / что дальше | Призыв к действию |

---

## §E — Инструкции / SOP

### SOP-1: Форк и настройка Layer 1 Personal Core

**Шаги:**
1. Открыть Notion → найти шаблон Layer 1 Personal Core (ссылка в Notion Command Center)
2. Нажать «Duplicate» → переименовать «[Имя] Personal OS»
3. Открыть Daily Log DB → создать первую запись: Date, What I did (1–3 строки), Energy (1–5), Notes (опц.)
4. Открыть Projects DB → добавить 1–3 текущих проекта: Name, Status, Next action
5. Contacts DB → добавить 3–5 ключевых людей
6. Пройти Weekly Review шаблон по воскресеньям (≤20 мин)
7. Включить fast-connect к Layer 2 или 3 ТОЛЬКО если нужно (по умолчанию — нет)

**Decision tree.** Нужна командная работа? → Layer 2. Нужен бизнес-overview? → Layer 3. Не уверен? → Стартуй с Layer 1, добавь остальное потом.

**Антипаттерны:**
- Создал все 12 баз в первый день → не заполнял ни одну → бросил. Контр: только Daily Log + Projects первую неделю.
- Подключил все три слоя сразу → запутался в relation'ах → стресс. Контр: STANDALONE, fast-connect — только когда нужно.
- Добавил 20 полей в Daily Log «на всякий случай» → заполнять лень. Контр: минимум (Date + What + Energy).

**Troubleshooting:**
- «Не понимаю куда класть X» → у каждой базы есть Description (раскрыть sidebar). Если всё ещё не ясно → пиши в чат сообщества.
- «Шаблон ревью не открывается» → убедись что дублировал страницу целиком, не только DB.

### SOP-2: Онбординг команды в Layer 2 (Generic baseline)

**Шаги:**
1. Один человек (Facilitator) дублирует Layer 2 Generic template
2. Заполнить Roles DB: имя роли (абстрактно), ответственности, кто сейчас
3. Заполнить Skills Exchange: каждый участник вводит 3 навыка (offer) + 3 запроса (ask)
4. Charter consent: все участники читают и подписывают текст согласия (минимум: fork-and-leave, 30-day window, Mondragón если финансы)
5. Настроить Skill Briefing шаблон для встреч
6. Неделя 1: провести 1 встречу по шаблону Skill Briefing

**Антипаттерны:**
- Подключили Jetix overlay сразу, без понимания → путаница с терминами (Steward, R12). Контр: сначала Generic, overlay — когда нужна монетизация.
- Charter не читали, просто нажали «согласен» → нет реального consent. Контр: 30 мин на чтение вслух.
- Facilitator единственный, кто понимает систему → bottleneck. Контр: обучить 2-го человека SOP-2 за первую неделю.

### SOP-3: Запуск AI voice pipeline

**Шаги:**
1. Записать голосовой файл (OGG/MP3/M4A) → положить в `inbox/voice/`
2. Запустить `bash tools/run_pipeline.sh`
3. Дождаться `~/summary-latest.md`
4. СТОП. Прочитать отчёт.
5. Принять решения: что идёт в Daily Log, что в CRM, что в Ideas, что выбросить
6. Промоция вручную (voice DRAFT-only — никаких авто-перезаписей прода)

**Антипаттерны:**
- Запустил pipeline → не читал → всё автоматически попало в прод. Нарушение voice-DRAFT discipline. Контр: СТОП после шага 3 — это конституционное правило.
- Забыл положить файл в правильную папку → pipeline не подхватил. Контр: алиас в shell `alias vi='cp $1 ~/jetix-os/inbox/voice/'`.

### SOP-4 (V4): Быстрый хакатон-онбординг (2 часа — из лиц в проекты)

**Контекст.** Layer 2 Generic в хакатон-режиме. Применяется для Direction #16 events. Stack: Cloud Cowork + Platform (Layer 2 + Layer 3 subset) + ROY swarm + AI Tools.

**Шаги:**

*Блок 1 (0–30 мин): Знакомство + роли*
1. Facilitator дублирует Layer 2 Generic hackathon-шаблон (заранее подготовленный форк с упрощёнными базами)
2. Все участники добавляют себя в Roles DB: имя роли (что делает здесь) + 1 offer + 1 ask
3. Skills Exchange: каждый вводит 3 навыка (2 мин на человека)
4. Быстрая Charter: упрощённая версия (3 пункта: scope / exit / no-extraction) — читают вслух, подписывают

*Блок 2 (30–60 мин): Проект scaffold*
5. Форкнуть Layer 3 subset (Strategy + Projects + People — 3 базы из 12)
6. Заполнить Projects: 1 главный проект с Name + Goal + Owner + Deadline
7. Strategy: 1-строчный Mission + 3 гипотезы (что проверяем за хакатон)
8. People: все участники внесены с ролью

*Блок 3 (60–90 мин): AI Tools + ROY*
9. Открыть AI Tools companion → выбрать 2-3 инструмента из кластера «Создание»
10. Задать brigadier вопрос: «какие риски у нашего подхода?» → multi-angle ответ (5 мин)
11. Зафиксировать ответы ROY в Hypotheses DB как открытые гипотезы

*Блок 4 (90–120 мин): Работа по проекту*
12. Команда работает по своему плану
13. Daily Log в хакатон-режиме: update каждые 30 мин (What we did + What's next)

*Post-hackathon (15 мин после финала):*
14. CRM touch для каждого участника (если CRM интегрирован) через Layer 1 Contacts → CRM
15. Decision Log: зафиксировать 3 главных решения хакатона
16. Экспорт: каждый участник получает форк своей части (STANDALONE гарантия)

**Антипаттерны хакатон-онбординга:**
- Попытка настроить полный Layer 1/2/3 за 2 часа → не успели, всё бросили. Контр: только Layer 2 Generic + Layer 3 subset (3 базы).
- Charter пропустили «нет времени» → конфликт по exit в конце. Контр: упрощённый Charter (3 пункта) входит в первые 30 мин обязательно.
- ROY swarm использовали как оракул («что нам делать?») → R1-нарушение. Контр: формулировать как «какие варианты» или «какие риски».

---

## §F — Шаблоны / Templates

### Notion DB schemas (спецификация, не sample content)

**Layer 1 Personal Core — базы:**

| База | Поля (минимум) | Тип | Опциональные расширения |
|---|---|---|---|
| Daily Log | Date (date), What I did (text), Energy (select 1–5), Notes (text) | Page template | Tags, Project relation, ActivityWatch link |
| Projects | Name (title), Status (select: active/paused/done), Next action (text) | DB | Priority, Due date, Owner |
| Ideas | Title, Source (select: own/voice/reading), Status (draft/active/parked) | DB | Category, Project relation, Confidence |
| Contacts | Name, Context (text), Last touch (date) | DB | Role, Pipeline status, Tags |
| Hypotheses | Statement (title), Confidence (select: low/med/high), Status (open/confirmed/refuted) | DB | Evidence (text), Related project |
| Goals | Title, Horizon (Q/Y/3Y), Status (active/paused/done) | DB | Metrics, Sub-goals |
| Finance (опц.) | Date, Amount, Category, Direction (in/out) | DB | Project, Notes |

**Layer 2 Team Collaboration (Generic) — базы:**

| База | Поля (минимум) | Тип |
|---|---|---|
| Roles | Role name (title), Responsibilities (text), Current holder (person/text) | DB |
| Skills Exchange | Skill name, Person, Type (offer/ask), Status (active/done) | DB |
| Charter | Text (page), Signed by (multi-select), Date signed | Page |
| Skill Briefing | Meeting date, Participants, Agenda, Decisions, Action items | Template |
| Group Finance (опц.) | Amount, Category, Direction, Timestamp | DB |
| Decision Log | Decision (title), Date, Rationale, Who decided | DB |

**Layer 2 Jetix overlay (дополнительные поля/базы):**

| Добавляет | Что это | R12 scope |
|---|---|---|
| Roles с R12-категориями | 10 Jetix ролей: Inv-Capital / Inv-Time / Contributor / Learner и др. | HIGH (Mondragón cap per категории) |
| 4 шаблона монетизации | M1–M4: Standard / Asymmetric / IP-leverage / Anti-fork-prevention | Каждый проходит 8-Q checklist |
| R12 Audit Log | extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt | AUTO-HALT на нарушение |
| Steward role | Watchdog: ловит нарушения ≤5s | Rotateable, не permanent founder |

**Layer 3 Universal Business Foundation — 12 групп баз (минимальная схема):**

Strategy (Title, Type, Period) · Finance (Amount, Category, Direction, Date) · People (Name, Role, Status) · Projects (Name, Status, Stage, Owner) · Sales/CRM (Contact, Status, Last touch) · KM (Title, Type, Pipeline status) · Knowledge Library (Title, Source, Format) · Brand (Asset name, Type, Status) · Ops (Process name, Owner, SOP-link) · Templates (Name, Type, Link) · Substrate (Title, Category, Reference) · System (Config name, Path, Status)

**MD-шаблоны (filesystem-side):**
- `_templates/daily-log-entry.md` — frontmatter + 4 поля
- `_templates/weekly-review.md` — 6 вопросов (что сделал / что не сделал / энергия / открытие недели / следующий фокус / R12-check для команды)
- `_templates/charter-consent.md` — 6 секций: scope / roles / economics / exit / R12 / signatures
- `_templates/charter-hackathon-mini.md` (V4-NEW) — упрощённая версия для хакатонов: 3 секции (scope / exit / no-extraction), ≤1 страница, подписание за 5 мин
- `_templates/hackathon-daily-log.md` (V4-NEW) — хакатон-режим Daily Log: Date + Block + What we did + What's next + Blockers, обновляется каждые 30 мин

**V4-NEW Platform-форматы (связаны с Direction #15):**

| Формат | Описание | Основа | Детали |
|---|---|---|---|
| Dashboard template | Life Pulse / engagement-view поверх Daily Log | Layer 1 Daily Log DB | Детально в Direction #15 |
| Achievement log | Contribution-credit + badge track | Layer 2 overlay (append-only) | Детально в Direction #15 |
| Skill tree view | Linked view: Skills Exchange + Knowledge Library + Goals | Layer 2 + Layer 3 | Детально в Direction #15 |
| Habit tracking template | Daily Log extension: Habit field + streak counter | Layer 1 Daily Log | Детально в Direction #15 |

Все четыре V4-NEW формата — это **Platform-views поверх существующих баз**, не новые standalone базы. Platform tracking = authoritative, геймификация = derived.

---

## §G — Презентация (10–20 слайдов)

**Формат.** Slide deck (Notion slides или PDF). Для discovery-звонков с T1/T3 партнёрами.

| Слайд | Headline | 3 bullets | Visual concept |
|---|---|---|---|
| 1 | Jetix Platform: три станка на стене | Standalone / Fork-friendly / AI-усиленные | Mermaid: три блока (L1/L2/L3) без стрелок между ними |
| 2 | Зачем три станка, а не один | Каждый работает сам / не нужно всё сразу / соединяй когда нужно | Было: лестница → Стало: три независимых иконки |
| 3 | Layer 1: Personal Core | Daily Log за 30 мин / Goals + Hypotheses / Weekly Review | Скриншот или mermaid схемы DB |
| 4 | Что AI делает здесь | Voice → Daily Log DRAFT / Groq Whisper транскрипт / человек ревьюит | Flow-диаграмма: voice → DRAFT → ты → прод |
| 5 | Layer 2: Team Collaboration | Roles + Skills Exchange / Charter consent / Честная монетизация | Скриншот Roles DB + Charter |
| 6 | R12 в Layer 2 Jetix overlay | Mondragón 5:1 cap / Fork-and-leave 30-day / 4 класса нарушений | Таблица: 4 action classes → реакция (HALT) |
| 7 | Layer 3: Universal Business | 12 групп баз / Executive Briefing / Весь бизнес с одной страницы | Схема 12 групп |
| 8 | AI Tools companion — 4 кластера | Захват (voice/telegram/OCR) / Обработка (extract/wiki/CRM) / Создание (mermaid/synthesis) / Анализ (ROY swarm/hypothesis) | 4-кластерная таблица |
| 9 | ROY Swarm — 17 агентов | Brigadier-маршрутизатор / 5 original + 8 book-driven / R12 auto-pair | Граф: brigadier → expert nodes |
| 10 | O-182: AI стратификация | AI = рутина (транскрипция/сортировка/граф) / Человек = фронтир (решения/непонятное/стратегия) / Никакой авто-записи без ревью | Ось: рутина ← → фронтир |
| 11 | Build → Run → Scale маховик | Build: основатель solo / Run: петля обратной связи / Scale: система крутится сама | PL-1 mermaid (адаптация) |
| 12 | Кто нужен сейчас (Build) | T1 методологи: проверить метод / T3 тестеры: пройти систему / R12-мост: проверить Charter | Таблица T1/T2/T3/T4 по этапам |
| 13 | Экономика (честная) | 75/25 split / Mondragón 5:1 wage cap / Fork-and-leave: proportional share + history без штрафа | Схема split |
| 14 | Как стать партнёром-методологом | Проверить метод → со-создать курс → вести когорту → спавнить клан | Lifecycle T1 партнёра |
| 15 | Как поставить свой станок | Предложи → сообщество оценило → встал на полку с твоим именем / Fork-able / Твой contribution-credit | Метафора: пустая стена → станок с именем |
| 16 | 8 вопросов перед любым касанием | Цена ≤ польза? / Конкретно? / По ступени? / Не доим? / Не запираем? / Нет манипуляции? / Стоп-сигнал готов? / Канал уместен? | Чеклист список |
| 17 | V4: Platform = основа #15 и #16 | Геймификация строится поверх Platform / Хакатоны: за 2ч из лиц в проекты / Кланы получают Platform-инстанс | Схема: L1+L2+L3 → #15 → #16 → Кланы |
| 18 | Что НЕ делаем сейчас | Не массовые адвокаты (Run/Scale) / Не курс end-to-end (Run) / Не смарт-контракты (Scale) / Не рассылаем без видео | Red X list |
| 19 | Следующий шаг | Выбери один слой → форкни → 7 дней → обратная связь | CTA slide |

---

## §H — FAQ (10–30 вопросов)

1. **Зачем три слоя, а не один Notion-шаблон?** Каждый слой решает разную задачу. Лестница из всех слоёв сразу = перегрузка. STANDALONE — выбрал свой, остальное добавляешь когда дорастёшь. Подробно: §1 long-form.

2. **Нужно ли разворачивать Layer 1 чтобы использовать Layer 2?** Нет. Layer 2 работает один. У членов команды могут быть свои Notion, Obsidian, вообще ничего. Layer 2 — это «как нам работать вместе», не «какой у тебя личный OS».

3. **Что такое STANDALONE на практике?** Ни одна база в default-схеме не ссылается на существование другого слоя. Связи (relations к чужим базам) появляются только если ты включил fast-connect opt-in. По умолчанию — замкнутый граф.

4. **Сколько полей в каждой базе?** Минимум: 3–4 поля. Всё сложное вынесено в sidebar «что можно добавить потом». Принцип: лучше 3 поля, которые заполняются каждый день, чем 20 полей, которые заполнились один раз.

5. **Что такое Jetix overlay для Layer 2, и обязательно ли его брать?** Нет. Generic baseline нейтральный. Jetix overlay — это пример применения (RUSLAN-LAYER per IP-1): 10 конкретных ролей, R12-дисциплина, 4 шаблона монетизации, Steward. Можешь взять overlay целиком, взять как образец для своего, или вообще не брать.

6. **Что такое Mondragón 5:1?** Потолок разрыва между самой высокой и самой низкой компенсацией в кооперативе. Если самый «дешёвый» участник получает X, самый «дорогой» — максимум 5X. Живёт только в Jetix overlay. Generic-слои нейтральны.

7. **Что такое fork-and-leave?** Право уйти из системы/команды в течение 30 дней, забрав свою пропорциональную долю treasury + историю без штрафа. Называется первым при онбординге. `fork_prevention_attempt` — любая механика, которая делает уход трудным → HALT.

8. **Что AI делает в этой системе, а что нет?** AI делает рутину: транскрипция голоса, структурирование записей, заполнение DRAFT, multi-angle анализ (ROY swarm), граф связей. AI НЕ делает: стратегические решения, выбор направления, оценку партнёров, написание Charter — это человек (R1 + O-182).

9. **Что такое ROY swarm и зачем он мне?** 17 агентов-экспертов (brigadier + 5 ROY + 8 book-driven + 4 sub-brigadier). Даёшь задачу brigadier'у, он маршрутизирует к нужным экспертам, получаешь multi-perspective ответ. Ни один агент не принимает решений за тебя — они surface'ят варианты, ты выбираешь.

10. **Голосовой pipeline — безопасно ли, что AI читает мои заметки?** Voice-DRAFT discipline: pipeline создаёт только DRAFT-файлы, ничего не записывает в прод без твоего ревью. Это конституционное правило системы. Никаких API-ключей в открытых файлах. Подробно: voice-DRAFT discipline в Global Rules.

11. **Как поставить свой «станок»?** Предложи инструмент или шаблон → сообщество оценивает → если полезен, встаёт на «стену» с твоим именем (contribution-credit). Fork-able: другие могут взять и адаптировать. R12-check: инструмент не должен создавать lock-in.

12. **Что такое Executive Briefing в Layer 3?** Страница-агрегатор: весь бизнес с одной точки зрения. Подтягивает из 12 групп баз самое важное. Обновляется вручную (не авто) — так владелец сохраняет связь с реальностью. Главный артефакт Layer 3.

13. **Можно ли использовать Layer 3 не в Notion?** Архитектура описана как Notion-схема, но принцип работает в любом инструменте (Obsidian, Airtable, Excel). Главное — 12 групп баз и Executive Briefing как структура.

14. **Где живут AI Tools companion в системе?** Отдельная companion-страница (не слой). 20 инструментов в 4 кластерах. Reference, не кнопка: ничего не запускается автоматически. Привязывается к любому слою. Подробно: AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.

15. **Build → Run → Scale — где мы сейчас?** Build, средняя часть (26.05.2026). Substrate готов, наружу не вышел. Видео A — блокер. Первые тестеры (Дмитрий) уже в процессе. Подробно: PLATFORM-LIFECYCLE-STAGES-PLAN §3.

16. **Зачем нужен T1 методолог, если система уже готова?** Чтобы проверить метод на ком-то кроме создателя. Методолог — не клиент и не инвестор, а человек, который «прогоняет систему на себе и говорит где она ломается». Run без T1-validation — риск методологического дрейфа.

17. **Что такое Charter и зачем он нужен?** Текст-согласие: scope + роли + экономика + exit + R12-дисциплина + подписи. Живёт в Layer 2 Jetix overlay. В Run — текст-согласие. В Scale — legal-документ с возможным смарт-контрактом. Проверяется R12-экспертом перед началом работы.

18. **Как работает fast-connect между слоями?** Linked database views (окно, не копия). Например: Daily Log из Layer 1 подтягивает Executive Briefing из Layer 3 через relation. Оба слоя остаются независимыми — удалил один, другой не ломается. Включается вручную (opt-in, не дефолт).

19. **Что значит «инструмент с твоим именем на полке»?** Contribution-credit: если ты предложил и развил инструмент/шаблон, используемый сообществом — твоё имя (или alias, по желанию) привязано к нему навсегда (append-only). Fork не удаляет attribution.

20. **Если мне не нужна вся система Jetix — могу взять только шаблоны?** Да. Generic части (Layer 1 / Layer 2 generic / Layer 3 base) не содержат Jetix-терминов, работают как нейтральные инструменты для любого человека или команды. Jetix overlay — отдельный fork-able template, opt-in.

21. **(V4) Как связаны геймификация и Platform? Это два разных Notion-воркспейса?** Нет. Геймификация (Direction #15) — это views и derived-слои поверх Platform баз. Habit tracking — это Daily Log extension. Skill trees — это linked view поверх Skills Exchange + Knowledge Library. Никакого отдельного «геймификационного воркспейса». Platform tracking = authoritative source.

22. **(V4) Как Platform помогает на хакатоне?** Stack: Layer 2 Generic (Roles + Charter) за 30 мин + Layer 3 subset (Projects) за 30 мин + ROY swarm on-demand. Итого: «из лиц в проекты» за 2 часа. Детально: SOP-4 выше.

23. **(V4) Что клан получает от Platform при входе в сеть Jetix?** Notion-пакет: Layer 1 template для каждого + Layer 2 Generic для команды + Layer 3 опционально. AI tooling: доступ к AI Tools + ROY swarm командный режим. Методологический scaffold (FPF). R12 Steward. Полный STANDALONE: клан может уйти с полным инстансом в 30 дней.

24. **(V4) Достижения из геймификации можно забрать при выходе из клана?** Да. Это требование архитектуры, не опция. Achievement system строится на Platform contribution-credit (append-only). Fork-and-leave включает полную историю достижений. `fork_prevention_attempt` через achievement lock-in → HALT.

25. **(V4) QF (Quadratic Funding) в хакатонах — где это в Platform?** QF-результаты фиксируются в Layer 2 Jetix overlay: Group Finance DB + Decision Log. Прозрачность = Platform-record. Само QF-распределение — логика Direction #16 (events-engine), Platform предоставляет audit trail.

---

## §I — Worked Examples (3–5)

*(IP-1 STRICT: все имена — ролевые типы, не назначенные исполнители. Финальный выбор конкретных людей за Ruslan.)*

### Пример 1 — Гуманитарий-тестер (тип: «Дмитрий-trial»)

**Контекст (роль).** Гуманитарий, не технарь. Много источников, мало структуры. Хочет порядок в задачах и идеях. Нет команды. Нет бизнеса.

**Стартовый слой.** Layer 1 Personal Core.

**Сессия 1 (30 мин).** Форкнул Layer 1 → Daily Log: создал запись «первая неделя». Projects: добавил 3 текущих дела. Contacts: 5 человек. «Зашло — не страшно».

**Сессия 2 (через неделю).** Weekly Review по шаблону. Обнаружил: Projects Status не заполнял. Упростил — убрал Status из привычки, оставил только Name + Next action.

**Что AI помогло.** Надиктовал идеи в голос → `run_pipeline.sh` → summary-latest → ты скопировал нужное в Ideas DB. Сэкономил 20 мин ручной работы.

**Обратная связь.** «Weekly Review — слишком длинный, 6 вопросов много для начала». Правка шаблона: оставить 3 вопроса в baseline, 6 — в sidebar «продвинутое».

### Пример 2 — Методолог-партнёр T1 (тип: «Maxim/Oleg»)

**Контекст (роль).** Эксперт с методологическим опытом. Интерес: посмотреть как Jetix-метод устроен изнутри, возможно со-создать курс-модуль.

**Стартовые слои.** Layer 2 Jetix overlay (методология Jetix) + Layer 1 (опционально свой).

**Взаимодействие.** Получает Charter текст → читает 30 мин → задаёт 3 вопроса о монетизации → Ruslan отвечает → подписывает Charter consent → онбординг в Layer 2 Jetix overlay.

**Что видит.** Roles DB с 10 типами ролей. Понимает: «я — тип Inv-Time». Skills Exchange: предлагает «методологический ревью курса». R12 Audit Log: видит прозрачность экономики.

**Результат теста.** «Mondragón ratio — хорошо, но нужно объяснение почему 5:1, а не 3:1 или 10:1». Правка: добавить footnote в Charter с ссылкой на Mondragón-историю.

### Пример 3 — Founder-одиночка (тип: стартап/агентство)

**Контекст (роль).** Основатель агентства (5 человек). Хочет видеть весь бизнес в одном месте. Личная система уже есть (не Notion). Команда работает через мессенджеры.

**Стартовый слой.** Layer 3 Universal Business Foundation (standalone, без Layer 1/2).

**Сессия (2 часа).** Форкнул Layer 3 → настроил 4 ядерных раздела (Strategy, Finance, Projects, People) → заполнил Executive Briefing → «вижу бизнес».

**Что AI помогло.** ROY swarm: задал вопрос «где у меня самый слабый процесс?» → brigadier маршрутизировал к mgmt-expert + systems-expert → получил multi-angle ответ за 5 мин вместо часа рефлексии.

**Обратная связь.** «Executive Briefing — хочу обновлять автоматически». Ответ: в текущей архитектуре обновление вручную (human-in-the-loop по конституции). Auto-update → только через явный opt-in в Scale.

### Пример 4 (V4) — Хакатон-команда (тип: 4 человека, смешанный профиль)

**Контекст (роль).** Четыре человека: условно один с техническим бэкграундом, один с гуманитарным, один с бизнес-опытом, один новичок. Хакатон Direction #16: 6-часовой формат (micro-standard).

**Слои.** Layer 2 Generic (hackathon-fork) + Layer 3 subset (Projects + Strategy).

**Ход (по SOP-4):**
- 00:00–00:30: Onboarding. Facilitator форкнул hackathon-шаблон. Все внесли роли (кто чем занимается) + 2 offer/ask. Charter-mini: 3 пункта, подписали. «Понятно кто что делает».
- 00:30–01:00: Project scaffold. Projects DB: 1 проект (Name + Goal + Milestone + Owner). Strategy: 1-строчный mission + 3 гипотезы. People: все занесены.
- 01:00–01:30: ROY swarm. Вопрос brigadier: «у нас гипотеза X, какие у неё слабые места?» → philosophy-expert + systems-expert + investor-expert → 3 угла. Команда скорректировала гипотезу 2.
- 01:30–06:00: Работа. Daily Log update каждый час (3 поля: что сделали / что дальше / blocker).
- 06:00–06:15: Закрытие. Decision Log: 3 решения. Каждый форкает себе Layer 2-часть со своей историей.

**Что сработало.** Charter-mini за 5 мин — не пропустили, не перегрузились. ROY swarm в 01:00 — получили острый feedback за 5 мин без ментора.

**Что не сработало (обратная связь).** Daily Log update каждый час — забыли обновить в 03:00 и 04:00 (deep work блок). Правка SOP-4: daily log update обязательно только в start + end хакатон-блока, промежуточные — рекомендуемые.

---

## §J — R12 Paired-Frame Check

### 8 вопросов для платформы Jetix

*Применяется перед каждым касанием партнёра (T1/T2/T3/T4) и перед каждым обновлением системы.*

| # | Вопрос | Применение к Платформе |
|---|---|---|
| 1 | Цена ≤ польза? | Онбординг ≤30 мин (Layer 1) / 1 день (Layer 2 generic) / 2ч (Layer 3). Если дольше — шаблон слишком сложный. |
| 2 | Конкретно? | Каждое касание — конкретный слой, конкретная задача. Не «посмотри на систему вообще». |
| 3 | Соразмерно отношениям? | Тестеру T3 не суём Layer 2 Jetix overlay с R12-терминами в первую встречу. |
| 4 | По ступени? | Layer 1 → Layer 2 → Layer 3. Не наоборот. Jetix overlay — только после Generic baseline. |
| 5 | Канал уместен? | Discovery-звонок (не email-рассылка) для T1/T3 Build. |
| 6 | Не доим / не запираем? | Fork-and-leave прописан явно. Инструменты fork-friendly. Contribution-credit append-only. |
| 7 | Нет манипуляции? | Никакого FOMO («только 3 места осталось»). Никаких клятв верности. Выход называется первым. |
| 8 | Стоп-сигнал готов? | Каждый онбординг содержит явный off-ramp: «если не зашло — просто скажи». |

### V4-дополнение к R12-check: специфика для #15 и #16

**Для геймификации (#15) на Platform:**
- Достижения fork-exportable? Achievement lock-in = `fork_prevention_attempt` HALT.
- Геймификационные механики не создают dependency (FOMO-badges, streak manipulation)? → influence-ethics-expert auto-pair ОБЯЗАТЕЛЕН для любого геймификационного компонента на Platform.
- Platform tracking = authoritative? Если геймификация хранит прогресс только у себя → R12 violation.

**Для хакатонов (#16) на Platform:**
- QF-распределение прозрачно через Platform Decision Log? Непрозрачное QF = `non_consensual_distribution` риск.
- Post-hackathon: у каждого участника есть fork его части? Если нет → `fork_prevention_attempt`.
- ROY swarm использовался как советник, не оракул? Если команда «делала что сказал AI» → R1-нарушение (фиксируется в Decision Log).

### Антипаттерны (lock-in vs fork-friendly)

| Антипаттерн (lock-in) | Fork-friendly контр |
|---|---|
| Инструмент работает только внутри Jetix-подписки | Все шаблоны — standalone Notion duplicates, нет платного wall |
| Charter требует «эксклюзивности» — нельзя использовать другие системы | Charter = согласие на принципы, не эксклюзивный контракт |
| Contribution history удаляется при выходе | Append-only: история остаётся, attribution не снимается |
| Сложно найти кнопку «Выйти» | Fork-and-leave называется на Day 5 (до подписи Charter), 30-day window явный |
| AI-инструменты работают только с проприетарным API-ключом | Max-подписка Claude Code headless, DRAFT-only, никаких авто-перезаписей |
| Шаблон монетизации не объясняет split | Каждый из 4 шаблонов монетизации: явный % + 8-Q check до SG-2 |
| `fork_prevention_attempt` в языке документов | R12 Audit Log ловит `fork_prevention_attempt` → HALT ≤5s |
| Steward = постоянная роль основателя | Steward rotateable. Основатель = один из многих в Scale. |
| (V4) Achievement badges хранятся только в геймификационном движке | Platform tracking = authoritative, achievement exportable в 30-day window |
| (V4) Хакатон-команда не получает форк своих данных после события | SOP-4 шаг 16: каждый участник получает форк своей части обязательно |

### R12-риск по этапам платформы

- **Build (сейчас) — низкий.** Денег нет. Единственный риск: присвоить методологический вклад T1. Лечение: явные credits в документах.
- **Run — средний.** Деньги потекли. Главные риски: выжать аудиторию T2/T3, lock-in через Charter. Защита: Steward HALT ≤5s, Mondragón 5:1 на каждом шаблоне монетизации, fork-and-leave на каждой выплате. V4-добавление: геймификационные механики входят в Run → influence-ethics-expert auto-pair обязателен для любого gamification-деплоя.
- **Scale — высокий.** Массовая динамика, риск секты. Защита механическая: смарт-контракты (4 класса нарушений), Steward per clan, анти-секта-дисциплина (нет клятв верности, выход называется первым, нет фигуры спасителя). V4-добавление: сотни кланов на Platform → каждый клан-инстанс должен быть технически exportable. QF-распределение через хакатоны становится системным механизмом → требует смарт-контракт backing в Scale.

**Сквозной закон:** защита растёт быстрее системы. Если система масштабируется быстрее защиты → секта или корпорация с диктатором на Scale.

---

## §K — AI Tooling Integration

### Что AI делает vs что человек (O-182)

| Задача | AI | Человек |
|---|---|---|
| Транскрипция голоса | Groq Whisper (`whisper-large-v3`) авто | — |
| Структурирование транскрипта | `extract.py` → Claude headless → DRAFT | Ревью DRAFT, решение что куда |
| CRM voice routing | `voice_router.py` → DRAFT-контакт | Промоция из DRAFT в прод |
| OCR PDF/книг | `mistral_ocr.py` / `convert_pdfs_to_md.py` → Markdown | Выбор что включить в corpus |
| Wiki ingest | `/ingest` → страницы + log + edges | Решение о канонизации |
| Multi-angle анализ | ROY swarm (17 агентов) → варианты | Выбор варианта, стратегическое решение |
| Hypothesis tracking | `/hypothesis-*` skills → structured entries | Оценка confidence, решение validate/refute |
| Mermaid диаграммы | Claude Code headless → готовая диаграмма | Постановка задачи, ревью схемы |
| Toggl sync | `toggl_sync.py` → отчёт | Решение что трекать |
| Executive Briefing | Не авто | Человек обновляет вручную (human-in-the-loop) |
| Charter разработка | Не авто | Человек пишет и проверяет |
| Выбор партнёров | R1: нет, варианты только | Ruslan = единственный стратег |
| (V4) Habit streak tracking | Daily Log view (derived) → визуализация | Решение что трекать как habit |
| (V4) Skill tree generation | Skills Exchange + KL → linked view scaffold | Человек решает что включить в свой tree |
| (V4) QF calculation | Не авто — логика Direction #16 | Человек верифицирует QF-результаты |
| (V4) Achievement badge issue | Platform contribution-credit → derived badge | Человек решает критерии badge |

### Готовые workflows (спецификация)

**WF-1: Voice → Daily Log**
```
Голос → inbox/voice/ → run_pipeline.sh → summary-latest.md → СТОП → ревью → ручная промоция → Daily Log
```
Промпт для extract.py: «Структурируй следующий транскрипт в список: что сделано / что запланировано / идеи / CRM-касания / задачи. Формат: YAML. Не интерпретируй стратегически.»

**WF-2: ROY swarm — platform question**
```
Ruslan → brigadier: "вопрос о Layer 2 монетизации" → dispatch → mgmt-expert + investor-expert + influence-ethics-expert (R12 auto-pair) → multi-angle ответ → ты выбираешь
```
Антипаттерн: не задавать brigadier вопрос «что мне делать?» — это R1-нарушение. Правильно: «какие варианты есть для X?»

**WF-3: Wiki ingest — новый источник знаний**
```
Источник (URL / PDF / голос) → /ingest → wiki-страница + log + edges → frontmatter pipeline: raw → ingested → compiled → linted → ready → решение о канонизации
```

**WF-4: CRM partner touch**
```
Звонок / переписка → voice заметка → CRM voice router → DRAFT-контакт → ревью → /crm-touch → обновление последнего касания → /crm-stuck (если >14d без touch)
```

**WF-5 (V4): Хакатон-ROY dispatch**
```
Хакатон-команда → brigadier: "у нас гипотеза X — какие риски?" → dispatch (philosophy / systems / investor) + influence-ethics-expert (если касается engagement) → multi-angle → команда фиксирует в Decision Log → человек принимает решение
```
Антипаттерн: ROY использован как оракул («AI сказал делать X → делаем X») → Decision Log должен фиксировать «решение принял [Role], ROY = input». Если этого нет → R1-риск.

**WF-6 (V4): Platform → Геймификация-tracking**
```
Участник заполняет Daily Log (стандартный workflow) → геймификационный движок (#15) читает Daily Log как Platform-source → derived view (habit streak / XP / achievement) → НЕ обратная запись в Platform без explicit user action
```
Критично: геймификация = derived view, не write-back. Автоматическая запись геймификации в Platform-базы без явного action пользователя = нарушение voice-DRAFT discipline паттерна (для геймификации — «engagement-DRAFT discipline»).

---

## §L — Partner-Extension Hook

### Fork protocol (спецификация)

Партнёр хочет поставить свой «станок» в Мастерскую — инструмент, шаблон, OS-слой. Протокол:

**Шаг 1. Предложение (PROPOSE).** Партнёр описывает инструмент: что делает, для кого, как работает, R12-совместимость (8 вопросов пройдены? нет lock-in?). Формат: MD-файл в `proposals/tools/`.

**Шаг 2. Оценка сообщества (EVALUATE).** 3+ участника тестируют инструмент. Обратная связь: 1 неделя минимум. R12-проверка: influence-ethics-expert (если инструмент касается монетизации/рекрутинга/геймификации) авто-firing.

**Шаг 3. Размещение (PLACE).** Если прошёл — инструмент встаёт на «стену» (добавляется в AI-TOOLS-MEGA-PAGE или Notion-шаблоны) с attribution автора: `contribution-by: [имя/alias]`, `date: YYYY-MM-DD`. Append-only.

**Шаг 4. Поддержка (MAINTAIN).** Автор отвечает на вопросы первые 30 дней. После — community ownership. Автор может форкнуть «свою версию» если хочет развивать отдельно.

### Extension points платформы

| Extension point | Что можно добавить | Ограничения |
|---|---|---|
| Layer 1 Personal Core | Новые шаблоны ревью / дополнительные DB (habits, health, reading) | STANDALONE не ломать; минимум полей в baseline |
| Layer 2 Generic | Новые типы ролей / шаблоны встреч / процессы | Generic = нейтральный; Jetix-терминология только в overlay |
| Layer 2 Jetix overlay | Новые роли-типы / шаблоны монетизации / R12 enforcement rules | R12 STRICT; каждый шаблон монетизации — 8-Q check; influence-ethics-expert auto-fire |
| Layer 3 Universal Business | Новые группы баз (макс 16) / Executive Briefing sections | Нейтральность; любой бизнес-тип |
| AI Tools companion | Новые инструменты в кластеры | Voice-DRAFT discipline; no API keys in open files; DRAFT-only |
| ROY swarm | Новый book-driven expert (MAX-8 ack per batch) | IP-1: роль ≠ executor; R12 auto-pair для influence-смежных |
| (V4) Геймификация-слой | Dashboard / achievement / skill-tree views поверх Platform баз | Platform tracking = authoritative; геймификация = derived; no write-back без user action; influence-ethics-expert auto-pair ОБЯЗАТЕЛЕН |
| (V4) Хакатон-шаблоны | Hackathon-mode форки Layer 2/3 | SOP-4 compliance; post-hackathon fork для каждого участника обязателен |

### Contribution guidelines

- Каждый инструмент — отдельный file с YAML frontmatter: `title`, `date`, `contribution-by`, `type`, `R12-checked: true/false`
- Attribution append-only: имя автора не удаляется при форке (только добавляется `forked-by`)
- Fork-and-leave из contribution: автор может убрать своё имя из активного использования, но fork-история сохраняется
- R12 compliance checklist (8 вопросов) обязателен для любого инструмента, касающегося монетизации, рекрутинга, gamification
- (V4) Для геймификационных extension: дополнительный engagement-DRAFT discipline check (производный от voice-DRAFT: геймификация = derived view, не write-back без user action)

### R12 compliance для партнёра-разработчика

Партнёр, создающий инструмент/шаблон для платформы, проходит R12-check перед размещением:

```
extraction_beyond_share → нет (инструмент не извлекает больше agreed share)?
wage_ratio_violation → нет (если инструмент связан с компенсацией — 5:1 cap соблюдён)?
non_consensual_distribution → нет (распределение только с явным согласием всех участников)?
fork_prevention_attempt → нет (нет механик, которые делают выход трудным)?
```

Все четыре «нет» → инструмент допускается на «стену». Хоть один «да» → на доработку или HALT.

**(V4) Дополнительный check для геймификационных инструментов:**
```
achievement_lock_in → нет (achievements exportable, не привязаны только к Jetix-движку)?
engagement_manipulation → нет (нет streak-FOMO, nag-badges, pressure mechanics)?
platform_write_back_without_consent → нет (геймификация не пишет в Platform-базы без явного user action)?
```

Все три «нет» → геймификационный инструмент проходит. influence-ethics-expert финальная проверка перед размещением.

---

## Closing

Direction #2 Платформа — инфраструктурный хребет всей Мастерской. В V4 этот хребет несёт существенно большую нагрузку: не только Personal/Team/Business OS для отдельных пользователей и команд, но и технический substrate для двух новых движков — геймификации (#15) и хакатонов (#16), плюс Platform-инстанс для каждого клана в Сети (#14).

Три слоя (Personal/Team/Business OS) + AI Tools + ROY Swarm — это по-прежнему не монолит, а набор независимых инструментов-станков. Fork-friendly принцип встроен на уровне архитектуры: STANDALONE, fast-connect opt-in, fork-and-leave 30-day, contribution-credit append-only. V4-расширение не меняет этот принцип — оно его нагружает дополнительными требованиями (engagement-DRAFT discipline для геймификации; post-hackathon fork для хакатонов; клан-инстанс как exportable unit).

Текущая позиция: Build, средняя часть. Substrate готов (17 агентов, 3-слойная Notion-архитектура v2, AI Tools 20 инструментов, voice pipeline). Наружу не вышел — видео A блокер. Первый тестер Layer 1 запущен. Следующий шаг — видео A → тестеры → обратная связь → правки → выход из Build.

R12-защита в этом направлении растёт с каждым этапом (Build → Run → Scale), и она должна опережать рост системы. С V4-расширением на хакатоны и геймификацию ставки выросли: influence-based механики (#15) имеют R12 HIGHEST риск, хакатоны (#16) вводят QF-распределение как системный механизм. Четыре action classes (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt) плюс V4-геймификационные три класса (achievement_lock_in / engagement_manipulation / platform_write_back_without_consent) — это конкретные триггеры HALT, не абстракция.

*F2-F3 derivative. Интегрирован существующий substrate без нового ресёрча. R1 surface only — Ruslan принимает решения. R12 paired-frame STRICT. IP-1 STRICT (все имена — ролевые типы). NO auto-launch. NO Foundation modifications.*
