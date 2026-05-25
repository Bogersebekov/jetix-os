---
title: Phase 1 — Расширенный reference-scan публичных архитектур (Western + Chinese + cooperative + research + methodology)
date: 2026-05-25
type: phase-report
phase: 1
parent_prompt: prompts/jetix-public-docs-metaplan-v2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: prompt-jetix-public-docs-metaplan-v2-phase-1
constitutional_posture: R1 surface only + R6 + R11; F3 reference general knowledge (NO new external research)
language: russian primary
status: pool — reference baseline for v2 directions; NO auto-promotion
---

# 🏛️ Phase 1 — Как устроены публичные архитектуры у других (расширенный scan)

> **Что это.** v1 Phase 1 смотрел на 7 западных референсов. v2 расширяет до **5 кластеров**:
> Западный tech (7) · Китайские гиганты (8 — NEW) · кооперативы / anti-extraction (4) ·
> deep-tech / research (4) · методология / образование (4). Итого **27 референсов**.
>
> **Угол тот же:** сколько разделов верхнего уровня · по какой логике разбито · narrative flow
> (с чего вход) · public vs gated · длина · что украсть. **F3 — общие знания, без нового external
> research** (per §6 промпта). Цель — variant D в Phase 2 опирается на проверенные паттерны, а
> Vision/Master Plan (Phase 5) — на лучшие манифест-жанры.

---

## §1 КЛАСТЕР 1 — Западный tech (7)

### 🟢 Anthropic — «исследования → продукт → ответственность → компания»
- **Top-level (~5-6):** Research · Claude · API/Developers · Safety/Policy · Company · Careers.
- **Логика:** по **зрелости отношений** — сначала «во что верим» (Research + Core Views), потом «что потрогать» (Claude/API), потом «как держим безопасно» (RSP/ASL), в конце «кто мы».
- **Narrative flow:** миссия → продукт → безопасность → команда. Safety вынесена в топ как часть оффера, не спрятана.
- **Public vs gated:** почти всё public (papers, RSP, Core Views); gated — только API-ключи + enterprise-контакт.
- **Украсть для Jetix:** **принципы/safety в топ** = прямая модель для R12-обещания как публичного якоря. «Core Views» = шаблон для нашего Vision/Values документа.

### ⚡ Tesla — «продукт впереди, миссия отдельным манифестом»
- **Top-level (~4-5):** Vehicles/Models · Energy · Charging · Discover · Shop.
- **Логика:** по **линейкам продукта**, не по аудитории. Миссия живёт отдельным жанром — публичный **«Master Plan» (Part 1/2/3, теперь Part Deux/Master Plan 3)**, редкий формат «вот наша долгосрочная стратегия открыто, на годы вперёд».
- **Narrative flow:** продукт сразу → манифест опционально для тех, кто хочет «зачем».
- **Public vs gated:** всё public; конфигуратор/заказ — мягкий gate (нужен аккаунт).
- **Украсть (ГЛАВНОЕ для v2):** **публичный Master Plan как отдельный жанр** — короткий, нумерованный по частям, написанный от первого лица, обещающий конкретные вехи. Это прямой шаблон для нашей полки #11 (Vision/Master Plan standalone). Tesla открыла патенты → ↔ наш D-13 open-surface/closed-core.

### 🍎 Apple — «по продуктовым линиям + витрина отделена от глубины»
- **Top-level (~6-7):** Mac · iPhone · iPad · Watch · Services · Support · Store.
- **Логика:** по **продуктовым семействам**; единый brand-язык поверх всего; глубина (tech specs, HIG, developer docs) уходит на под-уровни и в отдельный поддомен (developer.apple.com).
- **Narrative flow:** витрина-эмоция сверху → tech specs по клику → developer/API в отдельной зоне «для своих».
- **Public vs gated:** маркетинг public; developer-глубина — отдельный слой («для тех, кто ищет», не gated).
- **Украсть:** **слой глубины отделён от витрины** — прямой аргумент за двери variant D (любопытный видит эмоцию, методолог проваливается в спеки). HIG (Human Interface Guidelines) как публичный standalone = шаблон для нашего Rules/Method-канона.

### 🔵 OpenAI — «research / product / safety / company + Charter якорь»
- **Top-level (~4-5):** Research · Products (ChatGPT/API) · Safety · Company · Pricing.
- **Логика:** зеркало Anthropic — по **функциональным блокам**. **Charter** (про миссию AGI, «broadly distributed benefits») — отдельный якорный конституционный документ.
- **Narrative flow:** research → продукт → safety → кто мы; Charter как «конституция» в Company.
- **Public vs gated:** research/Charter public; API/pricing — мягкий gate.
- **Украсть:** **Charter как отдельный публичный якорь** — у нас Charter рычажный (8/12 сущностей). Можно сделать публичным «конституционным» документом отношений (≈ наша полка #8 R12-обещание + #10 Ценности).

### 💳 Stripe — «по продукту И по роли/задаче + docs как оффер»
- **Top-level (~5-6):** Products · Solutions (по индустрии/задаче) · Developers (docs) · Resources · Pricing · Company.
- **Логика:** двойная — **по продуктам** И **по решениям-под-задачу** (Solutions = «ты кто и что хочешь»); developer-docs — мощный отдельный столп (главное конкурентное преимущество).
- **Narrative flow:** «что у нас есть» (Products) ИЛИ «реши мою задачу» (Solutions) → developers ныряют в docs → pricing → company.
- **Public vs gated:** docs/pricing полностью public (стратегия: открытая дока продаёт); аккаунт — gate на дашборд.
- **Украсть (ГЛАВНОЕ для variant D):** **двойной вход** — «по продукту» ИЛИ «по своей роли». Это и есть гибрид D (полки A × двери C). Открытые docs/шаблоны = наши Notion-шаблоны как публичный актив.

### 🟦 Microsoft — «по аудитории-сегменту, не по технологии»
- **Top-level (~5-6):** For home / For business / For developers/IT · Products (Microsoft 365 / Azure / Windows / Gaming) · Industries · Support.
- **Логика:** **по сегменту покупателя** (home / business / dev) поверх продуктов. Огромный масштаб скрыт за чистым сегментным верхним уровнем; Azure/Learn — отдельные глубинные миры.
- **Narrative flow:** «ты кто» (home/business/dev) → продукты под тебя → глубина (Learn / docs).
- **Украсть:** **сегментный вход маскирует масштаб** — урок: даже при 94 документах верхний уровень держим ≤6, сегментируем по «ты кто» (наши 3 двери). Microsoft Learn = шаблон образовательной полки #7.

### 🔴 Google / Alphabet — «холдинг: бренды отдельны, research/safety отдельным крылом»
- **Top-level (Alphabet):** About · Investors · How we're committed (responsibility) · отдельные сайты per компания (Google / DeepMind / Waymo / Verily).
- **Логика:** **холдинговая** — Alphabet = тонкий зонтик, каждый бренд = свой полный сайт. DeepMind держит собственную research/safety архитектуру отдельно.
- **Narrative flow:** зонтик-about → проваливаешься в конкретный бренд.
- **Украсть:** **холдинговый паттерн** прямо мапится на наш D-19 (holding-scale 1T ambition) + Network State / кланы (полка #11 Vision): Jetix-зонтик + кланы как под-бренды со своими страницами. Подтверждает: на Scale мы = Alphabet-like зонтик, не монолит.

---

## §2 КЛАСТЕР 2 — Китайские гиганты (8) — NEW v2

> **Зачем китайцы (per Ruslan voice «может китая компании»).** Западные = по продукту / по
> воронке доверия. Китайские дают **другой паттерн: super-app + многослойная империя + единая
> экосистема-lock-in**. Часть из этого — анти-урок (lock-in = ровно то, что R12 запрещает),
> часть — позитивный урок про экосистемную плотность и единый вход.

### 🟧 Alibaba — «многослойная империя, разные сущности под зонтиком»
- **Структура:** Taobao/Tmall (commerce) · Alibaba Cloud · Cainiao (logistics) · Ant/Alipay (finance, отделена) · DAMO Academy (research) · AliExpress (international).
- **Логика:** **по бизнес-вертикалям как полу-автономным компаниям** под холдингом. Каждая вертикаль = своя экосистема; объединены идентичностью + платёжным слоем.
- **Narrative flow:** на корп-сайте — «business segments» как равные блоки; пользователь же входит через конкретный сервис.
- **Украсть:** **многослойная империя** = прямой референс для нашего Бизнес-направления (#3) на Scale: кооператив-зонтик + автономные кланы-вертикали. DAMO Academy = research-крыло отдельным брендом (≈ наш open-source research D-24).
- **Анти-урок:** Ant/Alipay показывает риск, когда финслой запирает пользователя в экосистеме — R12 paired-frame: мы делаем платёжно-долевой слой **с fork-and-leave**, не с lock-in.

### 🟦 Tencent — «единый ID (WeChat) как ОС, всё остальное навешано»
- **Структура:** WeChat/Weixin (super-app ОС) · Games (крупнейший в мире) · Tencent Cloud · FinTech · Music/Video.
- **Логика:** **super-app как операционная система жизни** — один ID, внутри mini-programs от всех. Не «разделы сайта», а «слои одного входа».
- **Украсть (важно для Платформы #2):** **WeChat = идея Personal/Team OS как единый вход**, внутри которого всё. Наш Personal OS → Team OS → кланы = тот же паттерн «один OS, внутри слои», но **open/fork-friendly** вместо закрытого.
- **Анти-урок:** WeChat = тотальный lock-in (выйти = потерять всю жизнь). Наш R12 fork-and-leave = осознанная противоположность. **Paired-frame обязателен:** super-app плотность хороша, тотальный lock-in — нет.

### 🎵 ByteDance — «multi-brand content, алгоритм как ядро, бренды наружу разные»
- **Структура:** Douyin (CN) / TikTok (global) / Lark (enterprise productivity) / Toutiao (news) / CapCut / Pico (VR).
- **Логика:** **одно алгоритмическое ядро рекомендаций → много отдельных брендов под аудитории/гео**. Корп-сайт ByteDance минимален; бренды живут своей жизнью.
- **Narrative flow:** пользователь почти не знает «ByteDance» — знает TikTok. Корпорация невидима, бренды видимы.
- **Украсть:** **невидимая корпорация + видимые бренды** ↔ наш Network State (#11): Jetix-substrate невидим, кланы видимы. Lark = шаблон Team OS (productivity для команд).
- **Анти-урок:** алгоритм-движок оптимизирует на удержание-любой-ценой → ровно то, против чего gamification-engagement-expert + influence-ethics R12 ставят paired-frame. Мы используем engagement-паттерны **с обещанием не манипулировать** (R12 вопрос 7).

### 📡 Huawei — «диверсифицированный hardware/services + жёсткий B2B/B2C split»
- **Структура:** Consumer (phones/devices) · Carrier (telecom infra) · Enterprise · Cloud · отдельно — HarmonyOS как платформа.
- **Логика:** **по типу клиента** (consumer / carrier / enterprise) поверх продуктов; HarmonyOS = ставка на собственную ОС-экосистему после санкций.
- **Украсть:** **B2C / B2B чёткий split** = урок для нас: Workshop-users (масса) vs Team OS (организации) — разные двери, разный язык. HarmonyOS-после-санкций = пример «строим свой стек, чтобы не зависеть» ↔ наш filesystem-source-of-truth (D-17) + own-substrate.

### 📱 Xiaomi — «IoT-экосистема + lifestyle brand, "appliances" вокруг ядра»
- **Структура:** Smartphones (ядро) · AIoT (умный дом — сотни устройств партнёров) · Lifestyle (Mijia) · EV (новое).
- **Логика:** **ядро-телефон + экосистема "appliances"** вокруг (партнёрские устройства под единым app/brand). «Ecosystem chain» — Xiaomi инвестирует в стартапы, те делают устройства под зонтик.
- **Украсть (ГЛАВНОЕ — мапится на AI-электрификацию):** Xiaomi «ecosystem chain» = **прямой референс нашей метафоры "appliances + electricians"** (AI-электрификация, направление видения #4). Ядро (метод/платформа) + партнёрские «приборы» (клановые продукты) под зонтиком. Партнёрская инвест-модель ↔ наш investor-role в triple-role.

### 🚁 DJI — «single deep-domain mastery, глубина вместо ширины»
- **Структура:** узко — Drones (consumer/pro/enterprise/agriculture) · Stabilizers (Osmo/Ronin) · поддержка.
- **Логика:** **одна доменная вертикаль, доведённая до мирового доминирования** (~70% рынка дронов). Не империя — глубина. Сайт построен по сценариям использования (creators / enterprise / agriculture).
- **Украсть:** **глубина одного домена бьёт ширину** — урок для Build-этапа: лучше один метод-канон, доведённый до совершенства (как DJI дрон), чем 11 поверхностных направлений. На Build = DJI-mode (фокус метод+платформа), на Scale = Alibaba-mode (империя).

### 🛒 Pinduoduo — «social commerce, рост через приглашение (viral mechanics)»
- **Структура:** commerce-app с team-buying / group-buy + Duoduo Farm (геймификация) + agriculture supply chain.
- **Логика:** **рост через социальное приглашение** — дешевле, если зовёшь друзей (team purchase). Виральность встроена в механику покупки.
- **Украсть (с осторожностью):** **referral встроен в ценность** ↔ наш promoter-role (3-я роль партнёра, 10% bonus 12 мес). PDD доказывает: реферал работает, если приносит **реальную пользу приглашённому**, а не просто extraction.
- **Анти-урок (R12 КРИТИЧНО):** PDD критиковали за тёмные паттерны (фейк-таймеры, бесконечные приглашения = манипуляция). Это **ровно R12 вопрос 7** (нет фейк-срочности / MLM / культа). Promoter-role у нас = **с paired-frame**: приглашение качественное, бонус за пользу, не за объём, fork-and-leave у приглашённого.

### 🔎 Baidu — «search → AI-ставка (Apollo автономия + Ernie LLM)»
- **Структура:** Search/Feed (ядро) · AI Cloud · Apollo (autonomous driving open platform) · Ernie (LLM).
- **Логика:** **legacy-ядро (search) финансирует AI-ставку**; Apollo = открытая платформа автономного вождения (open-source-ish для экосистемы).
- **Украсть:** **Apollo open-platform** = референс open-surface (D-13): открыть платформенный слой, чтобы экосистема строила поверх, монетизировать сервисы. ↔ наш open-source research/platform на Phase 2+ (D-24).

---

## §3 КЛАСТЕР 3 — Кооперативы / anti-extraction (4)

### 🤝 Mondragón ⭐ (главный кооп-референс) — «about → опыт → сектора → знание»
- **Top-level (~4-5):** About us (кто мы / принципы) · Cooperative experience (членство/governance) · Sectors/Business areas · Knowledge (University/research) · Contact.
- **Логика:** по **сущностям кооператива** — отдельно принципы и ценности, отдельно «кооперативный опыт» (10 принципов, 1-член-1-голос, social fund 10%, потолок 5:1), отдельно бизнес-сектора, отдельно образовательное крыло (Mondragón University).
- **Narrative flow:** **ценности/принципы впереди** → как работает (членство, governance) → что делаем (сектора) → как учим (университет).
- **Public vs gated:** принципы и модель — public; членские документы (agreement, capital accounts) — для членов.
- **Украсть (ГЛАВНОЕ):** **кооп-принципы + модель денег публичны и впереди; членский Charter — за порогом вступления**. Прямой каркас разделения «публичное R12-обещание (#8) / членский Charter (gated)». Mondragón University = валидация образовательного крыла (#7) как равной сущности.

### 🏪 John Lewis Partnership — «about → Partnership (Constitution) → бренды»
- **Top-level (~3-4):** About us · Our Partnership (Constitution + employee-ownership) · Our brands · Careers/News.
- **Логика:** **«Partnership» вынесена в отдельный топ-раздел** — публичная Constitution (принципы, «happiness of all members through worthwhile employment»), records совета, bonus policy.
- **Public vs gated:** Constitution полностью public — часть бренда «мы партнёрство».
- **Украсть:** **публичная Constitution = часть идентичности**, не юридический мелкий шрифт. Наш Charter может быть публичным манифестом отношений (полка #8 + #3 Бизнес). «Happiness of all members» = тон для наших Values (#10).

### 🌱 Equal Exchange — «values-first fair-trade кооператив»
- **Структура:** Our Story / Our Model (worker-owned) · Products · Our Impact (fair trade chain) · Resources/Education.
- **Логика:** **ценности впереди продукта** — сначала «как мы устроены и почему» (worker-owned, fair trade), потом что покупать. Прозрачность цепочки = маркетинг.
- **Украсть:** **прозрачность как оффер** — Equal Exchange публикует, кому и сколько платит фермерам. ↔ наш 75/25 split публикуется в Charter (R12). Урок: **финансовая прозрачность модели (не отчётности) = доверие**, прямо в публичный набор.

### 🏕️ REI Co-op — «членство как идентичность + co-op как маркетинг»
- **Структура:** Shop · Membership (co-op dividend) · Classes/Adventures · Co-op Journal (stewardship/values) · Impact.
- **Логика:** **членство = центр** (платишь $30 раз, член навсегда, годовой dividend 10% покупок). Co-op Journal = values/контент-крыло.
- **Public vs gated:** всё public; членство — мягкий платный gate с явной выгодой (dividend).
- **Украсть:** **членство с явной возвращаемой выгодой** (dividend) ↔ наш investor-role (treasury dividend) + cohort-membership. REI показывает: кооп-членство можно сделать **простым и привлекательным наружу**, не «закрытым клубом». Урок против анти-паттерна «секта-tier клуб».

---

## §4 КЛАСТЕР 4 — Deep-tech / research / capital (4)

### 🧠 DeepMind — «research-first, safety встроена, papers как актив»
- **Top-level:** Research · Technologies (AlphaFold/Gemini/etc.) · Safety & Responsibility · About · Blog/Publications.
- **Логика:** **по research-направлениям + флагманские "Alpha" проекты**; safety = отдельный равный раздел; публикации (Nature papers) = главный публичный актив.
- **Украсть:** **papers/research как публичный актив + safety равным разделом**. ↔ наш open-source research (D-24) + 5 research-deeps как curated публичные ссылки (но не raw — DOCS-CLASSIFICATION анти-паттерн).

### 🔷 Cohere / Mistral — «research-org lean structure»
- **Структура:** Products (models) · Research · Docs · Pricing · Company. Минималистично, dev-first.
- **Логика:** **lean — модели + docs + research**, без лишних разделов. Mistral добавляет «open weights» как идентичность (open-source как позиционирование).
- **Украсть:** **lean-структура для раннего этапа** — урок для Build: не нужно 11 полок сразу; Mistral на старте = 5 разделов. **Open weights как позиционирование** ↔ наш D-13 open-surface. Подтверждает Wave-sequencing (Phase 9): начать с lean-набора.

### 💰 Berkshire Hathaway — «годовое письмо как жанр, минимум сайта»
- **Структура:** почти нет сайта (намеренно архаичный) · главный актив = **annual shareholder letter** (Buffett, длинное, личное, образовательное).
- **Логика:** **один длинный личный документ важнее всего сайта**. Письмо учит принципам инвестирования, объясняет решения, признаёт ошибки. Жанр «откровенный длинный разговор с партнёрами».
- **Украсть (важно для Vision/Values):** **годовое письмо-манифест от первого лица** = шаблон для нашего Vision (#11) и Strategic Reflection. Тон «честно, лично, образовательно, признаём ошибки» = anti-hype, прямо под наш стиль plain-Russian. Минимализм сайта = урок против over-engineering навигации.

### 🚀 Y Combinator — «founder-facing playbook, образование как воронка»
- **Структура:** Apply · Library/Startup School (огромный образовательный контент) · Companies · Blog (essays) · About.
- **Логика:** **образовательный контент = воронка отбора**. Startup School / Library = бесплатные знания, которые привлекают и фильтруют основателей. Эссе (PG) = идентичность.
- **Украсть (ГЛАВНОЕ для Образования #7 + воронки):** **бесплатное образование = воронка партнёров** ↔ наша модель «ступени 1-4 бесплатно → ступень 5 платно». YC доказывает: дай ценность бесплатно, лучшие сами квалифицируются и придут. Эссе-формат = шаблон Method-канона.

---

## §5 КЛАСТЕР 5 — Методология / образование (4)

### 🎓 МИМ Левенчука (Школа системного менеджмента) ⭐ — прямой домен-референс
- **Структура (публичный сайт):** О школе · Курсы (catalog по уровням) · Программы/треки · Преподаватели · Блог/материалы · Поступление.
- **Логика:** **по курсам и трекам обучения** (системное мышление → системная инженерия → системный менеджмент → личное развитие). Метод-канон («Методология», «Системное мышление») = публичные учебники.
- **Украсть (КРИТИЧНО — это наш ближайший конкурент/партнёр):** **публичный метод-канон + курсы по трекам** = модель образовательной полки #7 + метод-полки #1. Урок дифференциации: МИМ силён в каноне, слабее в mass-scaling + AI-augmentation + кооп-экономике. **Наш Метод (#1) обязан явно позиционироваться рядом** (Method V2 §11/§13: Левенчук-foundation + ROY swarm + R12 + exocortex). IP-1: Левенчук/Цэрэн = T1/T2 примеры партнёрства, не назначения.

### 📚 Khan Academy — «по предметам + mastery learning, всё бесплатно»
- **Структура:** Courses (по предметам/классам) · Subjects · For teachers/parents/learners (роли) · About/Mission.
- **Логика:** **по предметам × по ролям** (learner / teacher / parent); mastery-based progression; миссия «free world-class education» впереди.
- **Украсть:** **mastery progression + роли-двери** ↔ наши 7 ступеней (mastery) + 3 двери. Миссия-впереди + полностью бесплатное ядро = тон для #7 Образование.

### 🎒 Coursera / edX — «catalog + about + for business/campus»
- **Структура:** Explore (catalog по темам/степеням) · For Business / For Campus / For Government (B2B двери) · Degrees · About.
- **Логика:** **catalog-first + сегментные B2B-двери**. Каталог = ядро; B2B (Business/Campus) = монетизация.
- **Украсть:** **catalog + B2B-сегментные двери** ↔ Workshop catalog + Team OS (B2B). Урок: образовательный каталог масштабируется как catalog, партнёрства — как отдельные B2B-двери.

---

## §6 Сводка паттернов (что повторяется по 5 кластерам)

| Паттерн | У кого | Урок для Jetix v2 |
|---|---|---|
| **3-6 разделов верхнего уровня** | почти у всех (искл. China super-apps) | даже при 94 доках верхний уровень ≤6 видимых; 11 полок — это бэкенд, не витрина |
| **Принципы/safety/values впереди** | Anthropic, OpenAI, Mondragón, John Lewis, Equal Exchange | R12-обещание (#8) + Ценности (#10) + Vision (#11) — в топ |
| **Манифест/Master Plan/письмо как жанр** | Tesla, OpenAI Charter, Berkshire letter | Vision standalone (#11) = Tesla Master Plan + Berkshire-тон |
| **Витрина отделена от глубины** | Apple, Microsoft, DJI, Stripe | 3 двери variant D (любопытный / кандидат / методолог) |
| **Двойной вход (продукт И роль)** | Stripe, Microsoft, Khan | гибрид D = полки × двери |
| **Членское/governance за порогом, публичны принципы** | Mondragón, John Lewis, REI | публичное R12-обещание ≠ членский Charter (gated) |
| **Бесплатное образование = воронка** | Y Combinator, Khan, Coursera | ступени 1-4 бесплатно → ступень 5 платно |
| **Невидимая корпорация + видимые бренды** | ByteDance, Alphabet, Xiaomi-chain | Network State / кланы (#11): substrate невидим, кланы видимы |
| **Экосистема "ядро + appliances"** | Xiaomi, Tencent, Alibaba | AI-электрификация (#4) + Платформа (#2): ядро + клановые приборы |
| **Финансовая прозрачность модели = доверие** | Equal Exchange, Mondragón, REI | публикуем 75/25 + 5:1 (модель, НЕ отчётность) |

### Анти-уроки (China-кластер — paired-frame R12)
| Анти-паттерн | У кого | Наш контр-ход |
|---|---|---|
| **Тотальный lock-in экосистемы** | WeChat, Alipay | fork-and-leave + 30-day opt-out (R12) |
| **Алгоритм оптимизирует удержание любой ценой** | ByteDance/TikTok | engagement-паттерны + обещание не манипулировать (R12 вопрос 7) |
| **Тёмные паттерны в реферале** | Pinduoduo | promoter-bonus за качество/пользу, не за объём |

---

## §7 Что Phase 1 даёт следующим фазам

- **Phase 2 (variant D):** двойной вход (Stripe/Microsoft) + витрина-vs-глубина (Apple/DJI) = каркас полки×двери×маршрут.
- **Phase 3 (Rules):** HIG (Apple) + Constitution (John Lewis) = жанры для свода правил.
- **Phase 4 (Values):** Core Views (Anthropic) + Equal Exchange values-first + REI/Mondragón = шаблоны ценностей.
- **Phase 5 (Vision/Master Plan):** Tesla Master Plan (нумерованные части) + OpenAI Charter + Berkshire letter (тон) = жанр манифеста.
- **Phase 6 (skeletons):** Mistral/Cohere lean = объём для раннего этапа; Khan mastery = образование.
- **Phase 9 (roadmap):** DJI-mode (Build фокус) → Alibaba/Alphabet-mode (Scale империя/холдинг).

---

*Phase 1 closure. 27 референсов в 5 кластерах: Западный tech (Anthropic/Tesla/Apple/OpenAI/Stripe/
Microsoft/Google) · Китайские 8 (Alibaba/Tencent/ByteDance/Huawei/Xiaomi/DJI/Pinduoduo/Baidu, с
anti-уроками R12) · кооперативы (Mondragón/John Lewis/Equal Exchange/REI) · deep-tech/capital
(DeepMind/Cohere-Mistral/Berkshire/YC) · методология/образование (МИМ-Левенчук/Khan/Coursera-edX).
10 повторяющихся паттернов + 3 China anti-урока (paired-frame). F3 general knowledge, NO new
external research. R1 surface. IP-1 (Левенчук/Цэрэн = примеры).*
