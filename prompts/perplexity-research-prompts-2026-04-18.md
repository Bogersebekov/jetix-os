---
type: research-prompts-collection
created: 2026-04-18
owner: ruslan
executor: Perplexity Pro DeepMode
purpose: 8 waves deep-research для построения hybrid-фреймворка Jetix
synth-target: raw/research/hybrid-framework-synthesis-2026-04-XX.md
related:
  - notion/3462496333bf811b9658da71783423d5 (Research-план)
---

# 📚 Perplexity Deep-Research Prompts — 8 волн для Jetix hybrid-framework

> **Цель всей серии.** Построить hybrid-фреймворк Jetix: software-foundation (Phase 1) +
> русская школа системного мышления (Phase 1.5) + 6 альтернативных моделей бизнеса
> (Phase 2-7). После всех волн — финальный synthesis → `Jetix framework v1-beta`.
>
> **Как пользоваться.**
> 1. Открыть Perplexity Pro → переключить в **DeepMode** (deep research режим).
> 2. Скопировать промпт одной фазы целиком.
> 3. Вставить → запустить.
> 4. Сохранить результат как `<phase-slug>-deep-research-2026-04-18.md` на Windows
>    или закинуть сразу на сервер через scp в `raw/research/`.
> 5. После всех 8 — единый Claude Code synth'ит hybrid.
>
> **Параллелизм.** Perplexity Pro позволяет запускать несколько одновременно — запускай
> все 8 параллельно в разных вкладках, соберёшь за 30-60 минут вместо 4-5 часов.
>
> **Язык выхода везде — русский.** Non-developer friendly (объяснять термины).

---

## 🌐 Общий контекст (одинаковый для всех промптов)

Каждый промпт уже содержит минимальный контекст Jetix в начале. Если Perplexity попросит
уточнения — используй этот блок (скопируй):

```
Контекст системы Jetix. Solo-operator (я, Руслан, Берлин) строит AI-управляемую operational
company. Текущая инфраструктура: 12 Claude-Code агентов (manager, strategist, sales-lead,
sales-researcher, sales-outreach, knowledge-synth, crazy-agent, meta-agent, personal-assistant,
system-admin, inbox-processor, life-coach), 8 активных проектов (quick-money, research, brand,
community, ai-tools, life-os, engineering-thinking, bets), git-монорепо jetix-os на GitHub,
Ubuntu VPS, Obsidian vault, Notion как legacy workspace. Primary цель — $50K revenue к
30.06.2026. Hypothesis: Jetix строится как hybrid — software-foundation + лучшие практики
других моделей бизнеса (consulting, agency, platform, holding, community, русская школа
системного мышления), интегрированные в новый framework для AI-native operational business.
```

---

# 🧱 PHASE 1 — Software Company (foundation layer)

**Выход:** `software-deep-research-2026-04-18.md` (6000-10000 слов)

```
Мне нужен глубокий research по software development как индустрии и методологии работы.
Контекст: я non-developer, строю AI-управляемую operational company (12 AI-агентов,
solo-operator, цель $50K revenue к 30.06.2026). Гипотеза: практики software development
применимы как OS для построения бизнеса через AI-агентов.

Мне нужен research на 6000-10000 слов на русском языке, структурированный в 4 блока
(ниже), с citation источников, свежими данными 2024-2026, конкретными примерами компаний.

## БЛОК A — Software-индустрия как non-developer её должен понимать

A1. SDLC полный breakdown: Waterfall / V-model / Agile / DevOps / SRE. Когда какая модель
используется, плюсы/минусы, real cases.

A2. Agile на практике: Scrum vs Kanban — отличия, ceremonies, роли, artifacts, когда
какую выбирают. Shape Up (Basecamp) как третья альтернатива.

A3. CI/CD: что конкретно автоматизируется на каждом этапе (build, test, deploy, monitor).
Tools landscape 2026 (Jenkins/GitHub Actions/CircleCI/ArgoCD). Metrics: DORA four keys
(deployment frequency, lead time, MTTR, change failure rate).

A4. Career ladder software engineer: Junior/Mid/Senior/Staff/Principal/Distinguished.
Что решает каждый уровень без escalation? Разница Senior vs Staff vs Principal — реальные
примеры из Google/Stripe/Amazon.

A5. Product Management в software: роль PM, PRD структура (Stripe/Linear/Shopify примеры),
roadmap methodologies, как PRD связан с OKR, разница PRD vs RFC vs 6-pager.

A6. DevOps и SRE: что такое Site Reliability Engineering, SLO/SLI/SLA с примерами, error
budgets, blameless postmortems, toil vs automation balance.

A7. Documentation practices: docs-as-code, Diátaxis framework (tutorial/how-to/reference/
explanation), README structure, ADRs (Architecture Decision Records), runbooks.

A8. Code review culture: зачем, pull request workflow, pair programming vs async review,
как она меняется при AI-coding (Copilot, Cursor, Claude Code).

A9. Retros и postmortems: blameless culture, 5 whys, learning organizations, как превращать
инциденты в systemic improvements.

A10. Technical debt: как измеряют (CodeScene research — 42% времени, 15x дефектов), как
учитывают в roadmap, когда рефакторить vs переписывать. Knight Capital 2012 case как пример
catastrophic debt.

## БЛОК B — Применимость к бизнесу через AI-агентов

B1. Успешные cases "business as software" где продукт не-софт (курсы, community,
consulting-native) — примеры и уроки.

B2. Holacracy (Zappos) — что получилось, что провалилось. Параллели с flat-организацией
AI-агентов.

B3. Amazon 6-pager + 14 leadership principles: как narrative-практики сочетаются с SDLC.
Cases применения.

B4. Как software-компании делают sales/marketing/ops: Salesforce, HubSpot, Stripe — их подход
к go-to-market через призму software-методологий.

B5. Продуктовые стартапы vs agencies — разница моделей, unit economics, scaling patterns.

B6. Software-native consulting: HashiCorp, Vercel, Stripe Atlas — кейсы когда software-
компании параллельно делают consulting-layer. Модели монетизации.

B7. Shape Up (Basecamp) подробно: 6-week cycles, appetite vs estimate, betting table,
hill chart. Почему это работает для small teams.

## БЛОК C — AI-агенты как развитие парадигмы

C1. Multi-agent systems в production 2025-2026: что реально работает (use cases), где
ломается, кто лидеры (OpenAI Swarm, LangChain/LangGraph, CrewAI, AutoGen, Anthropic multi-
agent patterns).

C2. AI as product vs AI as tool — разница в positioning, monetization, support burden.

C3. Cost модели multi-agent vs human teams: real numbers 2026 (tokens per task, $/hour
equivalent, utilization patterns).

C4. Reliability AI-agents в production: как обеспечивается, SRE practices для LLM-систем
(observability, guardrails, hallucination monitoring), real incidents и mitigation.

C5. Career-level metaphor для AI: релевантно или натяжка? Как frontier-компании структурируют
agent hierarchies (examples from Anthropic, OpenAI deployments).

C6. AI-native frameworks построения бизнеса (Gumloop, n8n, Zapier AI, CrewAI ecosystem):
что уже существует, gaps, opportunities.

## БЛОК D — Фильтр: что берём, что адаптируем, что не берём

D1. Какие software-практики переносятся 1:1 на operational business через AI (без изменений)?

D2. Какие требуют адаптации под solo-operator + agents + non-code основа?

D3. Какие не подходят вообще и почему (cargo-cult risks)?

D4. Какие риски слепого копирования software-индустрии в бизнес (ceremony overhead, human
factors игнор, false analogies)?

D5. Как гибридизировать: что из 6 альтернативных моделей бизнеса (classic consulting /
product / agency / holding / community-driven / platform-OS) комбинировать с software-
foundation для максимального leverage? Реальные примеры гибридных моделей.

D6. Что конкретно внедрять на текущих 12 AI-агентах (manager, strategist, sales-lead,
personal-assistant, etc.) и 8 проектах (quick-money, research, brand, community, ai-tools,
life-os, engineering-thinking, bets) на ближайшие 2 недели?

D7. Какой next-action после выбора методологии (= как документировать выбор, как катить
изменения без ломки velocity)?

## ТРЕБОВАНИЯ К RESEARCH

- Русский язык, non-developer friendly (термины объяснять)
- Каждый крупный факт с citation (URL + год источника)
- Свежие данные 2024-2026 предпочтительнее классики
- Конкретные примеры компаний, не абстракции
- В конце — honest conclusions: где гипотеза "Jetix = software company" держится, где
  ломается, что брать для hybrid-модели
- Open questions list для follow-up research'ов (holding / agency / platform / community /
  consulting как отдельные темы)

Выход: один markdown-документ 6000-10000 слов.
```

---

# 🧠 PHASE 1.5 — Анатолий Левенчук / ШСМ (русская школа системного мышления)

**Выход:** `levenchuk-deep-research-2026-04-18.md` (3000-5000 слов)

```
Мне нужен глубокий research по Анатолию Левенчуку и его подходам. Контекст: я строю
AI-управляемую operational company (12 AI-агентов, hybrid-фреймворк на базе software-
practices плюс другие модели бизнеса). Ищу что из наработок Левенчука можно взять для Jetix.

Research на 3000-5000 слов на русском языке, structured:

1. Кто такой Анатолий Левенчук — биография, роль в системном мышлении, связь с ШСМ (Школа
системного менеджмента). Сайт ailev.livejournal.com, ailev.ru — что там, как устроено.

2. Его основные книги в порядке приоритета чтения: "Системное мышление", "Образование для
образованных", "Интеллект-стек", "Системная инженерия" и другие — краткое содержание каждой,
для кого, что даёт. Ссылки на актуальные версии 2024-2026.

3. Ключевые концепции его системного подхода: что такое интеллект-стек, роль-based agency,
continuous learning, дисциплины/практики, системная схема, альфы, evo-agents. Объяснить
non-academic языком.

4. Позиция Левенчука на AI, multi-agent systems, LLM, AI-agents в организациях (2024-2026).
Его публикации и посты на эту тему.

5. Связь его подходов с:
   - Software engineering practices (что он берёт оттуда)
   - Bizdev / organizational design
   - Education / learning
   - System of systems thinking

6. ШСМ (Школа системного менеджмента) — что это за школа, какие курсы, кого готовит, формат
обучения, стоимость, выпускники, community.

7. Где искать свежий контент: YouTube каналы, Telegram каналы, открытые лекции, блог,
рассылки.

8. Применимость к моему кейсу Jetix: что конкретно из Левенчука стоит взять для AI-
управляемой компании. Мои 12 агентов через призму его role-based agency. Hybrid framework
через призму его system of systems. Учебный loop через призму его continuous learning.

9. Критика / ограничения его подхода — где он работает хорошо, где слабо. Альтернативные
точки зрения.

Требования: русский язык, каждый крупный факт с citation URL, свежие данные 2024-2026
предпочтительнее классики, конкретные примеры из его практики, в конце — actionable
takeaways для Jetix (минимум 10 штук).
```

---

# 🏛️ PHASE 2 — Platform-OS Model (самый близкий к Alliance + Marketplace vision)

**Выход:** `platform-os-deep-research-2026-04-18.md` (5000-8000 слов)

```
Мне нужен глубокий research по platform-OS модели в бизнесе. Контекст: я строю Jetix —
AI-управляемую company. Mittelstand AI Alliance — planned членская сеть немецких mid-
market компаний с shared AI-tooling. AI Solutions Marketplace — planned двусторонний рынок
для AI-решений. Обе инициативы — platform-plays. Хочу понять какая именно platform-модель
сработает и какие практики перенимать.

Research на 5000-8000 слов на русском, structured:

## 1. Что такое "платформа" в бизнес-смысле

1.1 Определение platform business: two-sided markets, multi-sided markets, network effects,
cross-side vs same-side effects. Примеры: Stripe, AWS, Apple App Store, GitHub, Airbnb,
Uber, LinkedIn.

1.2 Разница platform vs product vs service — экономика, unit economics, scaling patterns.

1.3 Классификация платформ: exchange platforms, maker platforms, infrastructure platforms,
community platforms, ecosystem platforms.

1.4 Монетизация: transaction fees, subscription tiers, freemium, premium placement, listing
fees, data monetization. Реальные numbers 2024-2026.

## 2. Как платформы строятся (chicken-and-egg problem)

2.1 Cold-start problem: как решали Airbnb (manual supply), Uber (drivers first), Stripe
(developer-first), GitHub (open source community). Подробные кейсы.

2.2 Supply side vs demand side — кого привлекают первым, почему. Андре Хаги "Platform
Revolution" framework.

2.3 Minimum viable ecosystem — сколько нужно поставщиков и потребителей на старте? Примеры.

2.4 Bootstrapping: standalone value (single-player mode до network effects). Как Slack
сначала был просто chat для команды.

## 3. Platform architecture (technical + organizational)

3.1 Core vs periphery: что контролирует платформа, что делегирует экосистеме. Пример: Apple
App Store vs Android.

3.2 API-first design, SDK, developer experience. Stripe, Twilio, Shopify кейсы.

3.3 Governance: rules, quality control, dispute resolution, content moderation. Reddit vs
Discord подходы.

3.4 Economic architecture: кто платит, кто получает, revenue sharing. App Store 30%, Airbnb
3%, Etsy 6.5%.

## 4. Network effects и their mechanics

4.1 Direct network effects (тем больше users — тем лучше для users, пример Telegram).

4.2 Indirect network effects (больше suppliers → больше buyers → больше suppliers, пример
Amazon marketplace).

4.3 Data network effects (больше использования → лучше AI → лучше использование, пример
Tesla FSD, Google Search).

4.4 Local vs global network effects (Uber vs Facebook).

4.5 Negative network effects и как их избегать (Craigslist spam, Airbnb party houses).

## 5. Mittelstand AI Alliance — кейс-применение

5.1 Как устроены profession-based alliances: CPA Alliance, AICPA, SBA-связанные networks.
Какая модель подходит для Mittelstand?

5.2 Shared services alliances: group purchasing organizations (GPO), consortia. Economics +
governance.

5.3 Vertical industry platforms: Veeva для pharma, Procore для construction. Какие уроки?

5.4 B2B vs B2B2C platforms. Where does Mittelstand Alliance fit?

5.5 Trust & data security в B2B platforms — first concerns Mittelstand CFOs. Как решают
Salesforce, SAP, Workday?

## 6. AI Solutions Marketplace — кейс

6.1 AWS Marketplace, Azure Marketplace, Google Cloud Marketplace: структура, curation,
monetization, winners.

6.2 AI-specific marketplaces: Hugging Face, Replicate, OpenAI GPTs store. Working или нет?

6.3 Vertical AI marketplaces (pharma, legal, finance): что уже есть, что работает.

6.4 Quality control в AI marketplace — review processes, certifications, user feedback
loops.

## 7. Platform governance и community

7.1 Role of community managers, evangelists, developer relations. Как Stripe и Twilio
построили DevRel.

7.2 Community-led growth vs product-led growth. Notion, Figma кейсы.

7.3 Toxic platforms avoidance (Reddit moderation, Twitter evolution).

## 8. Riks и downside

8.1 Platform dependency risk (приложения убиты изменением rules: Twitter третьи стороны,
Apple App Store вытеснения).

8.2 Regulatory risk: EU Digital Markets Act, App Store antitrust.

8.3 When NOT to build a platform. Andrew Chen / a16z на эту тему.

## 9. Applicability to Jetix

9.1 Какая platform-модель ближе всего Mittelstand Alliance? Какая AI Marketplace?

9.2 Cold-start strategy для Alliance (10-20 первых членов откуда)?

9.3 Что брать из Stripe / Shopify / AWS для Jetix platform-layer?

9.4 Как hybrid-framework Jetix (software-foundation + platform + community + consulting)
реализуется операционно?

9.5 Risks для Jetix-as-platform + mitigation.

Требования: русский язык, citations 2024-2026, конкретные numbers, 10+ actionable takeaways
для Jetix в конце.
```

---

# 👥 PHASE 3 — Community-Driven Model (для Jetix Club / Alliance membership)

**Выход:** `community-deep-research-2026-04-18.md` (4000-6000 слов)

```
Мне нужен глубокий research по community-driven бизнес-моделям. Контекст: Jetix строит
Mittelstand AI Alliance (membership-based сеть немецких компаний) + AI Solutions Community.
Хочу понять как успешные communities строятся и монетизируются, что перенимать.

Research на 4000-6000 слов на русском, structured:

## 1. Community-driven business: определение и примеры

1.1 Что такое community-driven business (CDB) vs community-enabled vs community-around-
product. Иерархия.

1.2 Примеры successful CDB: Indie Hackers (Courtland Allen), Stack Overflow, GitHub, Reddit,
Kickstarter, Patreon. Для каждого — модель монетизации и scale.

1.3 B2B communities: Salesforce Trailblazers, HubSpot Academy, AWS re:Invent, DevOps Enterprise
Summit. Как они связаны с бизнес-моделью parent-компании.

1.4 Professional communities: AICPA (accountants), BNI (networking), YPO (young presidents).
Economics + value propositions.

## 2. Architecture of a community

2.1 Platform choice: Discord vs Slack vs Circle vs Discourse vs custom forum — плюсы/минусы
каждого для B2B.

2.2 Onboarding flows: что делает новичка member'ом (Stripe Atlas, Reforge playbooks).

2.3 Roles & permissions: lurkers, contributors, moderators, leaders. Power laws (1-9-90 rule).

2.4 Rituals & events: weekly calls, monthly meetups, annual conferences. Когда что.

## 3. Monetization models

3.1 Membership fees (YPO, Indie Hackers Plus, FI Network).

3.2 Freemium community + paid premium (Lenny's Newsletter, Rand Fishkin's SparkToro
Community).

3.3 Course / cohort sales via community (ON Deck, Maven, Reforge).

3.4 Sponsor revenue (HackerNews jobs, SaaS newsletters with sponsors).

3.5 Marketplace within community (Indie Hackers Jobs, YC Work List).

3.6 Enterprise services (community-as-channel: от community к B2B sales, HubSpot model).

## 4. Growth playbooks

4.1 Cold-start: founder-led community building (Courtland для Indie Hackers, Pat Flynn для
SPI).

4.2 Content-led: newsletter / podcast / YouTube первые → community потом (Lenny Rachitsky,
First Round Review).

4.3 Event-led: conference / meetup первые → community потом (AWS re:Invent).

4.4 Product-led: product already has users → community forms around (Notion Ambassadors,
Figma Community).

4.5 Partnerships: leverage other communities (AppSumo, Product Hunt).

## 5. Retention & engagement mechanics

5.1 Gamification: badges, reputation, levels (Stack Overflow, Duolingo). Работает или нет?

5.2 Exclusive access drives retention: founder AMAs, beta access, private Slack.

5.3 User-generated content loops: как stimulate UGC (Reddit, Twitter, Medium).

5.4 Conflict resolution & toxicity management: Reddit admin tools, Discord moderation,
community guidelines examples.

## 6. B2B community specifics

6.1 Decision-makers vs practitioners: кто платит, кто использует community. Как serve обе
аудитории.

6.2 Confidentiality tensions: competitors в одном community. Chatham House Rules, private
channels.

6.3 Value measurement: NPS community, ROI metrics для membership.

6.4 Community-to-enterprise pipeline: как community leads в B2B sales.

## 7. Community + AI

7.1 AI tools для community management (moderation, content summaries, member matching).

7.2 AI community members (custom GPTs в Discord, bot-assistants). Ethics and perception.

7.3 AI as community differentiator: Jetix Club как "community с AI embedded".

## 8. Case studies: 5 deep dives

Выбрать 5 максимально релевантных для Jetix и разобрать подробно:
- Indie Hackers (community-first, B2C, creator economy)
- Reforge (B2B learning community + high-ticket courses)
- YPO (elite B2B professional membership)
- Mindvalley (education + community hybrid)
- Bundesverband Mittelschichtiger Unternehmen (если найдёшь немецкий аналог)

Для каждого: founding story, model evolution, current economics, что копировать Jetix.

## 9. Применимость к Jetix Alliance / AI Community

9.1 Какая модель (elite B2B membership à la YPO? Practitioner community à la Indie Hackers?
Hybrid?) подходит Mittelstand Alliance?

9.2 Cold-start для Alliance: 10 первых членов откуда? Что предложить?

9.3 Monetization: membership fees? Shared services? Marketplace cut? Combo?

9.4 Governance: я один основатель или pool founders?

9.5 Scaling: когда нанимать community manager? Когда делегировать модерацию? Когда hire
full-time.

9.6 Риски: what kills B2B communities (dead forum syndrome, 1-9-90 collapse, founder burnout).

Требования: русский, citations 2024-2026, numbers где возможно (members, revenue, churn),
10+ actionable takeaways для Jetix.
```

---

# 💼 PHASE 4 — Classic Consulting (McKinsey / BCG playbook — что НЕ копируем, но понимаем)

**Выход:** `consulting-deep-research-2026-04-18.md` (4000-6000 слов)

```
Мне нужен глубокий research по classic management consulting модели. Контекст: Jetix сейчас
имеет consulting-linию (quick-money проект), но эволюционирует к platform-модели. Хочу
понять playbook McKinsey / BCG / Bain / Deloitte / Accenture — что брать для текущего
consulting-layer'а и что явно НЕ брать потому что это обеспечивает leverage только через
человеко-часы.

Research на 4000-6000 слов на русском, structured:

## 1. Что такое management consulting

1.1 Определение consulting vs advisory vs implementation. Категории: strategy, operations,
IT, HR, finance, turnaround, transaction services.

1.2 Big 3 (MBB — McKinsey, BCG, Bain) vs Big 4 (Deloitte, PwC, EY, KPMG) vs boutique
consultancies. Разница в позиционировании, клиентах, ценообразовании.

1.3 Типичный клиент management consulting: Fortune 500 CEO, PE fund partner, government
agency, central bank. Почему они платят $500-2000/час за консультации.

1.4 Размер рынка 2024: глобальный consulting market ~$900B. Top 10 firms по revenue.

## 2. Business model economics

2.1 Pyramid model: 1 partner → 2-4 managers → 10-20 consultants → 40-80 analysts. Почему
так устроено (margin mechanics).

2.2 Utilization rates: targets 70-80% billable hours. Что это значит для consultants.

2.3 Leverage ratio: сколько analysts на 1 partner. McKinsey ~1:10, Accenture ~1:30.

2.4 Pricing models: time-and-materials, fixed-fee, outcome-based, retainer, subscription
(rare). Расчёт rates (bill rate = cost × multiple, multiple обычно 3-5x).

2.5 Margins: top-tier MBB ~20-30% operating margin, Big 4 ~12-18%, boutiques варьируются.

## 3. The MBB playbook

3.1 Problem-solving method: MECE framework, hypothesis-driven, issue trees, 80/20 principle.
Как это работает end-to-end.

3.2 Case interviews: что такое, почему именно так нанимают, paralleль с отбором в Jetix
agents.

3.3 Communication: Pyramid Principle (Barbara Minto), структура deck'ов, executive summary,
"so what" test.

3.4 Data analysis: back-of-the-envelope estimations, market sizing, financial modeling,
benchmarking.

3.5 Client management: partner-as-rainmaker, client as relationship, upsell / cross-sell,
"land and expand" strategy.

## 4. McKinsey, BCG, Bain — differentiation

4.1 McKinsey: strategy + C-suite relationships, "Firm" culture, alumni network.

4.2 BCG: intellectual differentiation (growth-share matrix, experience curve), knowledge-
leveraged.

4.3 Bain: results-focused, PE-facing, Net Promoter Score как внутренняя метрика.

4.4 Каждый — свои proprietary frameworks, publications, thought leadership (HBR articles,
books).

## 5. How consulting firms scale

5.1 Partner-track model: up-or-out, 7-10 лет до partnership. Вести культуру.

5.2 Global expansion: Office network, regional partners, practice areas.

5.3 Practice areas: industry practices (financial services, healthcare, technology) +
functional (strategy, operations, digital).

5.4 Knowledge management: KM systems, case repositories, expert networks.

5.5 Talent pipeline: ivy-league / top-MBA recruiting, on-cycle summer programs.

## 6. Digital & AI transformation of consulting

6.1 McKinsey QuantumBlack, BCG Gamma, Bain Advanced Analytics — AI практики big 3.

6.2 Generative AI 2024-2026: как firms используют для research, deliverables, code. Что
это делает с pyramid-модели.

6.3 Threats: boutique AI consultancies, former-MBB alumni starting AI shops, client in-
housing.

6.4 New pricing models в AI era: value-based, outcome-based, productized services.

## 7. Criticism and limitations

7.1 Critique of consulting: "When McKinsey Comes to Town" (Bogdanich/Forsythe 2022), conflicts
of interest, regulatory capture cases (opioid consulting, tobacco).

7.2 Structural issue: consulting sells "smart junior talent" from top universities, charges
10x their cost to client — ethical and value debates.

7.3 Low leverage for consultant: pure human-hours business, no equity multiplier. Why consultants
exit to industry / PE / startups.

7.4 Client side complaints: dependence, rising costs, lack of implementation follow-through.

## 8. Productized consulting (hybrid models)

8.1 Productized services: fixed-scope, fixed-price consulting (Bench Accounting, MarketerHire).

8.2 Subscription consulting: Boardroom (B2B ops), Growth Natives (SaaS ops).

8.3 AI-augmented consulting: solo consultants with AI leverage (Dan Shipper's Every, Alex
Lieberman's Smart Nonsense).

8.4 Community-based consulting: consultant pools (Toptal, Catalant, A.Team).

## 9. Mittelstand-specific consulting landscape

9.1 Big firms в DACH: Roland Berger, zeb, Atreus, Horvath & Partners. Кого обслуживают.

9.2 Mittelstand-specialists: BBE Handelsberatung, Enomic, Rittal Schaltschrank (industrial).

9.3 Немецкие культурные особенности: trust, long-term relationships, conservatism, handshake-
based deals.

9.4 Цены: Tagessätze (daily rates) 1500-3000 EUR для senior consultants, 3000-5000 EUR для
partners.

## 10. Applicability to Jetix

10.1 Что брать из MBB playbook для Jetix consulting-layer'а (quick-money проект):
- Problem-solving methodology (MECE, hypothesis-driven)
- Communication (Pyramid Principle)
- Client relationship management
- Delivery discipline

10.2 Что НЕ брать (не копируем):
- Pyramid / utilization model (у меня agents не people)
- Up-or-out culture
- Partner-track rainmaker model
- Ivy-league recruiting
- Billable hours economics

10.3 Как AI-agents меняют consulting economics для solo-operator: leverage ratio effective
может быть 1:100 с agents, vs 1:10 с humans у McKinsey.

10.4 Gibrid для Jetix: consulting as rev-gen + platform as scale + community as network.
Где consulting сидит в hybrid-framework?

10.5 Actionable next-steps для quick-money проекта (first paying client до 30.06.2026):
конкретно какие MBB-практики внедрять, какие игнорировать.

Требования: русский, citations 2024-2026, DACH-специфика где релевантно, 10+ actionable
takeaways, честная критика где consulting — плохая модель для solo-AI-operator.
```

---

# 📦 PHASE 5 — Product Company (SaaS-first: Notion / Linear / Stripe)

**Выход:** `product-deep-research-2026-04-18.md` (4000-6000 слов)

```
Мне нужен глубокий research по SaaS product company модели. Контекст: Jetix может эволюционировать
частью в SaaS-продукты (AI Solutions Marketplace как productized services, Jetix Club
membership как SaaS tier). Хочу понять лучшие SaaS-практики 2024-2026 и что адаптировать.

Research на 4000-6000 слов на русском, structured:

## 1. SaaS business model fundamentals

1.1 Определение SaaS vs традиционный software. Recurring revenue, subscription economics.

1.2 SaaS metrics trifecta: MRR/ARR, churn (gross vs net), CAC vs LTV ratio, payback period.
Benchmarks 2024-2026.

1.3 T2D3 growth trajectory (Triple-Triple-Double-Double-Double): почему это benchmark
unicorn-путь.

1.4 Rule of 40: growth rate + operating margin ≥ 40% как индикатор healthy SaaS.

1.5 Go-to-market motions: product-led (Notion, Figma) vs sales-led (Salesforce) vs hybrid
(HubSpot).

## 2. Product-led growth (PLG) — deep dive

2.1 Core principles: self-serve onboarding, freemium / free trial, activation metrics,
viral loops.

2.2 Notion case: pivot from collab tool to workspace platform, community-driven growth,
template marketplace.

2.3 Figma case: browser-based collab как дифференциатор, design systems as platform.

2.4 Linear case: opinionated design for high-performing teams, dev-first positioning, pricing
transparency.

2.5 Metrics: time-to-value, PQLs (product-qualified leads), expansion revenue.

## 3. SaaS architecture and operations

3.1 Multi-tenancy: shared infrastructure vs isolated (dedicated). Trade-offs.

3.2 Data isolation для enterprise clients: первый вопрос CFO Mittelstand.

3.3 SLO/SLA/uptime: 99.9% (three nines) vs 99.99% (four nines) — cost implications.

3.4 Support tiers: community support, standard (email 24h), premium (Slack Connect),
enterprise (dedicated CSM).

3.5 Security compliance: SOC 2 Type II, ISO 27001, GDPR, HIPAA, FedRAMP. Cost and timeline.

## 4. Pricing strategies

4.1 Models: per-seat, per-usage, tiered features, outcome-based, hybrid.

4.2 Notion pricing evolution: от freemium к team/business/enterprise.

4.3 Usage-based pricing (Snowflake, Twilio, Stripe): plus/minus, когда работает.

4.4 Value metric selection: что считать (seats? queries? revenue processed?).

4.5 Pricing page anatomy: 3-plan structure, feature matrix, FAQ, social proof.

## 5. Customer success & expansion

5.1 Negative churn mechanics: expansion revenue > churn. How top SaaS (Slack, Snowflake)
achieve 120%+ NRR.

5.2 Customer success as a discipline: roles, playbooks, segmentation (SMB / mid-market /
enterprise).

5.3 Onboarding as product: first 30 days, activation metrics, milestone celebrations.

5.4 Power user identification: who drives expansion? How to activate them.

## 6. Marketing for SaaS

6.1 Content marketing: SEO, blog, newsletters, YouTube. HubSpot playbook.

6.2 Community marketing: Notion Ambassadors, Figma Config conference.

6.3 Partnerships: integrations, tech alliances, reseller programs.

6.4 Paid acquisition: Google Ads, LinkedIn, podcast sponsorships, review sites (G2, Capterra).

6.5 SaaStr / SaaStock / ProductHunt — где SaaS Founders nertworking.

## 7. Sales motions for SaaS

7.1 PLG + sales-assist: self-serve для SMB, sales-assist для mid-market, sales-led для enterprise.

7.2 Sales team structure: SDR (outbound) → AE (closer) → CSM (retention / expansion).

7.3 Sales tools stack: Salesforce / HubSpot CRM, Outreach / SalesLoft, Gong, ZoomInfo.

7.4 Enterprise sales cycle: 3-12 месяцев, procurement process, legal reviews, pilot projects.

## 8. Fundraising and capital

8.1 SaaS funding stages: pre-seed ($500K-$2M), seed ($2-5M), Series A ($10-20M), Series B
($30-50M), beyond.

8.2 Revenue-based financing (Pipe, Capchase, Clearco) as alternative.

8.3 Bootstrap vs VC: Notion early-VC vs Basecamp bootstrap. Economics implications.

8.4 Metrics VCs smotрят: ARR, growth rate, CAC payback, LTV/CAC, logo retention.

## 9. AI native SaaS 2025-2026

9.1 How AI changes SaaS economics: inference cost (variable) vs traditional SaaS (mostly fixed).

9.2 Pricing shifts: от per-seat к usage-based из-за AI costs.

9.3 New categories: AI copilots, agent platforms, AI-native verticals (legal AI, healthcare AI).

9.4 Companies to watch 2026: Cursor, Harvey AI, Perplexity, Anthropic Claude for Work.

## 10. Applicability to Jetix

10.1 Может ли Jetix parts become SaaS?
- AI Solutions Marketplace как productized consulting (fixed-scope fixed-price)
- Jetix Club membership как SaaS tier
- Mittelstand Alliance как SaaS platform (shared services tier)

10.2 Какие SaaS-практики перенимать сразу для solo-operator + AI-agents:
- Metrics discipline (MRR/churn/LTV даже для early-stage)
- Self-serve onboarding principles
- Productized service delivery
- Community marketing

10.3 Что не копировать (не SaaS-native):
- VC-growth trajectory (bootstrap fit)
- Enterprise sales machine (без team не масштабируется)
- Multi-seat licensing (solo-operator сложно)

10.4 Hybrid roadmap: Jetix consulting-layer → productized services → SaaS community → platform.
Timeline и milestones.

Требования: русский, citations 2024-2026, DACH-специфика для Mittelstand where relevant,
10+ actionable takeaways для Jetix.
```

---

# 🏭 PHASE 6 — Agency Model (pragmatic revenue engine)

**Выход:** `agency-deep-research-2026-04-18.md` (4000-5000 слов)

```
Мне нужен глубокий research по agency business model. Контекст: Jetix в краткосрочной
перспективе (2026) может работать частично как AI-agency — брать клиентов на custom AI-
проекты. Хочу понять agency playbook 2024-2026, особенно AI-focused agencies, чтобы
грамотно построить этот revenue stream без sacrificing долгосрочный platform-path.

Research на 4000-5000 слов на русском, structured:

## 1. Agency business model fundamentals

1.1 Что такое agency: service firm, billing на time-and-materials или fixed-price,
project-based delivery.

1.2 Types of agencies: digital marketing, advertising, creative, brand, web/app development,
consulting boutiques.

1.3 Agency vs consulting: overlap (strategy) и differences (implementation focus, creative
output).

1.4 Agency vs product company: recurring revenue (product) vs project revenue (agency).

## 2. Agency economics

2.1 Billing models: hourly rates, project fees, retainers, performance-based.

2.2 Typical rates 2024-2026: junior $75-150/hr, mid $150-250/hr, senior $250-400/hr,
boutique specialty $500+/hr.

2.3 Utilization targets: 60-75% billable для sustainable agency.

2.4 Margin structure: ~40% cost of labor, ~30% overhead, ~30% profit in healthy agency.

2.5 Revenue concentration risk: одному клиенту >25% revenue — red flag.

## 3. Positioning and niching

3.1 Horizontal vs vertical agency: broad generalist vs vertical specialist. Почему niching
обычно winning (higher rates, shorter sales cycle).

3.2 Specialization axes: by client type (SaaS, e-commerce, D2C), by service (SEO, brand,
AI implementation), by geography, by deliverable.

3.3 Examples of successful niched agencies: 10up (WordPress for enterprise), Lumos (design
for fintech), Foundation (content for B2B SaaS).

## 4. Lead generation and sales

4.1 Inbound tactics: SEO content, case studies, podcasts, conference speaking.

4.2 Outbound tactics: cold email (Lemlist playbooks), LinkedIn outreach, referral partnerships.

4.3 Pipeline management: typical sales cycle 30-90 days для mid-market agency client.

4.4 Pricing conversation: avoiding race to bottom, value-based pricing vs hourly.

4.5 Win rates: 20-30% typical для qualified leads.

## 5. Delivery and operations

5.1 Project management: Scrum-style sprints, milestone-based, или waterfall. Когда что.

5.2 Client communication: weekly standups, monthly deliverables reviews, slack channels.

5.3 Scope management: change orders, scope creep prevention, contracts structure.

5.4 Quality assurance: peer reviews, QA checklists, client satisfaction surveys.

5.5 Documentation: for client handoff, for internal knowledge base.

## 6. Team structure and scaling

6.1 Early-stage: founder + 1-3 contractors. Lean economics.

6.2 Mid-stage: core team + project-based specialists network.

6.3 Established: 10-50 FTE, departments (strategy, design, dev, accounts).

6.4 Freelancer network model: Toptal, A.Team, Catalant — pros/cons for solo.

6.5 AI-augmented agency: solo operator + AI agents achieving what 5-10 person agency does.

## 7. AI-focused agencies 2024-2026

7.1 New breed: AI implementation agencies, prompt engineering shops, AI transformation
consultants.

7.2 Service offerings: custom GPT setup, workflow automation (n8n, Make), custom AI apps
(LangChain, Anthropic), training programs.

7.3 Pricing: custom AI implementation $25-75K, retainers $10-25K/mo, training workshops
$5-15K.

7.4 Client profiles: mid-market companies without in-house AI expertise, looking for
competitive advantage.

7.5 Examples (US/EU): 10Clouds AI division, Deeper Insights, Fractal Analytics. В DACH —
what exists?

## 8. Common pitfalls

8.1 The service trap: high revenue but no equity / IP, no multiplier.

8.2 Founder burnout: every project requires founder time, no scaling.

8.3 Client concentration risk: losing one big client = agency collapse.

8.4 Race to bottom on price: competing on hourly rates.

8.5 Lack of recurring revenue: feast or famine cycles.

## 9. Productizing agency services

9.1 Shift from custom to productized: Fixed scope, fixed price, fixed timeline.

9.2 Examples: Designjoy (unlimited design $4995/mo), ManyPixels, DesignCrowd.

9.3 AI-productized services possibilities: AI audit ($5K), Custom agent build ($25K),
AI workshop ($15K).

9.4 Transition path: custom agency → hybrid → fully productized.

## 10. Applicability to Jetix

10.1 Жизнеспособна ли agency-модель для Jetix quick-money проекта в 2026?
- Positioning: "AI-transformation для Mittelstand"
- Services: audit, implementation, training, retainer support
- Pricing: based on Mittelstand budgets (conservative — 10-50K EUR range)

10.2 How AI agents change the economics:
- Solo operator с AI может deliver проекты, требующие team of 5-10
- Leverage через agents = higher margin для агентства уровня
- Productization proceeds быстрее

10.3 Какие agency-practices внедрить:
- Lead generation (SEO, LinkedIn, podcast)
- Delivery discipline (milestones, QA)
- Client management (weekly updates)
- Scope management (contracts, change orders)

10.4 Какие НЕ внедрять:
- Hourly billing (это low-leverage)
- Large team structure
- Geographic offices
- Generalist positioning

10.5 Hybrid path: agency-revenue today, platform-income later. Timeline milestones.

10.6 Конкретный next-action для quick-money проекта (first 3 paying clients): lead sources,
offer structure, pricing.

Требования: русский, citations 2024-2026, DACH-специфика для Mittelstand, 10+ actionable
takeaways, честная картина pitfalls.
```

---

# 🏦 PHASE 7 — Holding / Portfolio Company (Berkshire, Tinybird model)

**Выход:** `holding-deep-research-2026-04-18.md` (3000-5000 слов)

```
Мне нужен глубокий research по holding / portfolio company моделям. Контекст: Jetix имеет
8 активных проектов + planned Alliance + Marketplace. Это по сути portfolio-structure. Хочу
понять как портфельные компании управляются, капитал allocated, risks diversified. Особо
интересуют AI-era holdings и solo-operator portfolio-thinking.

Research на 3000-5000 слов на русском, structured:

## 1. Holding company basics

1.1 Определение: operational holding vs financial holding vs pass-through holding.

1.2 Иконические examples: Berkshire Hathaway (Buffett), IAC (Diller), SoftBank (Son),
Constellation Software (Leonard), Danaher.

1.3 Economic rationale: diversification, capital reallocation, conglomerate discount/premium.

1.4 Corporate structure: parent company, subsidiaries, cross-holdings, tax optimization.

## 2. Buffett / Berkshire model

2.1 Key principles: circle of competence, long-term hold, moat analysis, owner earnings.

2.2 Capital allocation: let subsidiaries operate independently, sweep cash up to HQ, deploy
opportunistically.

2.3 Culture: "decentralized operations, centralized capital". Sub-CEOs have autonomy.

2.4 Size implications: Berkshire has $1T+ market cap — works at scale, not for solo.

## 3. Constellation Software model (smaller, more relevant)

3.1 Mark Leonard's playbook: acquire vertical market software (VMS) companies, hold forever.

3.2 Unit economics: small VMS businesses ($5-50M revenue), high customer retention, sticky.

3.3 Acquisition math: pay ~1x revenue for mature VMS, apply Constellation operating system,
cash-flow grows.

3.4 Decentralization: 6 operating groups, within each — hundreds of companies. Autonomy +
metrics accountability.

3.5 Communication culture: quarterly letters, no road shows, no analyst days.

## 4. Operator-investor hybrids (Tinybird, Koch, Fairfax)

4.1 Tinybird founder: Founder as allocator of capital across bets, stay operator-involved.

4.2 Koch Industries (private): $125B revenue, 130K employees, owned by Koch family. Extreme
decentralization + market-based management (Charles Koch's framework).

4.3 Fairfax Financial (Prem Watsa): insurance cash flow funds investments.

4.4 Lessons: operator discipline + investor capital allocation mindset = strong results.

## 5. Modern portfolio plays (2020+)

5.1 Rollup strategies: Thrasio (Amazon aggregator), Perch, Acquco — buy-and-hold e-commerce
brands.

5.2 Lifestyle rollups: StackCommerce (content brands), Morning Brew (newsletters acquired by
Insider).

5.3 AI-era rollups: possibility of AI-tool acquirers doing similar plays.

5.4 Micro-PE (Search Funds, ETA): 1-2 person team buy small profitable company, run it.

## 6. Solo-operator portfolio-thinking

6.1 Indie Hackers / Pieter Levels style: one founder, multiple products generating cash flow
(Nomad List, RemoteOK, Photo AI).

6.2 Portfolio approach for solo: why it works (different products, different customers,
diversification), why it fails (attention fragmentation, context switching).

6.3 Key skill: ruthless focus + strong operational rhythm + AI leverage.

6.4 Examples: Kevin Rose's network (Oak, Digg, etc.), Sam Parr (HubSpot acquired MFM, then
new ventures).

## 7. Portfolio management framework

7.1 Grading projects: active / stable / zombie / archive. Kill-criteria for each.

7.2 Capital (time / money / attention) allocation: not equal, based on expected value + strategic
importance.

7.3 Synergies vs independence: portfolio companies что share? (Brand, audience, infrastructure,
talent).

7.4 Cross-pollination: insights from one project informing others. Dangerous groupthink
avoided.

7.5 Exit readiness: каждый проект должен быть sellable или sustainable independently.

## 8. Governance и reporting

8.1 Monthly / quarterly reviews: что сморят portfolio owner/operator.

8.2 Financial transparency: P&L per project, cash flow, runway.

8.3 Strategic reviews: annual, 3-year plans, pivot decisions.

8.4 Founder-CEO relationship (if company has separate CEOs).

## 9. AI-era opportunities

9.1 AI tools consolidation: buy struggling AI startups at fraction of cost, revitalize.

9.2 AI-powered portfolio companies (each runs lean with AI agents vs large teams).

9.3 New categories: AI-augmented holding companies, portfolio of AI agents themselves.

9.4 Constellation-style playbook applied to AI vertical SaaS.

## 10. Applicability to Jetix

10.1 Is Jetix a holding company по сути?
- 8 проектов разной nature (consulting, product, community, content)
- One founder-operator
- Shared infrastructure (jetix-os, 12 agents, Notion/GitHub)
- Cash flow differently (quick-money generates, ai-tools maybe future)

10.2 Какие portfolio-practices перенимать сейчас:
- Kill-criterion per project (из implementation plan уже есть)
- Budget-hours per project (tracked)
- Quarterly portfolio reviews
- Capital allocation discipline

10.3 Long-term: может ли Jetix evolve в AI-portfolio holding?
- Acquire struggling AI tools / communities
- Apply Jetix operating system к каждому
- Consolidate under hybrid-framework

10.4 Текущий фокус: из 8 проектов — что живое? Что зомби? Что драйвить? Honest analysis
через portfolio-lens.

10.5 Integration: holding-thinking как третий слой hybrid-framework (software-foundation +
platform-topology + holding-allocation).

10.6 Actionable next-steps: какие portfolio-practices внедрять на ближайшие 2 недели.

Требования: русский, citations 2024-2026, solo-operator focus (Berkshire scale irrelevant,
Constellation / Levels / Koch relevant), 10+ actionable takeaways для Jetix portfolio
management.
```

---

# 📊 После всех 8 волн — Synthesis стратегия

Когда все 8 research-документов получены и лежат в `raw/research/`:

1. **Прочитай каждый свежим глазом** — отметь 5-10 самых важных takeaways из каждого
   (рядом с доком или в мини-отчёте).

2. **Запусти Claude Code synth** на сервере с промптом:

```
Прочитай все 8 research-документов в raw/research/*.md (software, levenchuk, platform,
community, consulting, product, agency, holding). Синтезируй в raw/research/hybrid-
framework-synthesis-2026-04-XX.md единое предложение "Jetix framework v1-beta" со структурой:

- Executive summary (что это, одной страницей)
- Foundation layer (software-practices — что берём 1:1)
- Cognitive layer (Левенчук / системное мышление — как мыслим)
- Topology layer (platform model — как устроена архитектура Alliance / Marketplace)
- Community layer (как строим Jetix Club membership)
- Delivery layer (agency + consulting practices — как работаем с клиентами)
- Portfolio layer (holding thinking — как управляем 8+ проектами)
- Product layer (SaaS practices — для productized offerings)
- Integration: как слои склеиваются в единую систему
- Conflicts resolved: где исследования противоречили и как мы решили
- Open questions: что требует дополнительного research
- Migration path: из текущего состояния Jetix в framework v1-beta (с датами)

На русском, 8000-15000 слов, каждый тезис с ссылкой на source research-документ (path:line
или section title).
```

3. **Прочитай synthesis** — это вход для Шага 2 methodology.

4. **Возвращаешься на [🧪 Шаг 2](https://www.notion.so/3462496333bf810da2cffc210c304f21)**
   → утверждаем методологию → decisions/ доку.

---

## 🎯 Итоговый порядок действий

| # | Фаза | Время (Perplexity) | Параллель? |
|---|------|--------------------|-----------|
| 1 | Software company | 15-25 мин | Да |
| 1.5 | Левенчук / ШСМ | 10-15 мин | Да |
| 2 | Platform-OS | 15-20 мин | Да |
| 3 | Community-driven | 10-15 мин | Да |
| 4 | Consulting MBB | 10-15 мин | Да |
| 5 | Product SaaS | 10-15 мин | Да |
| 6 | Agency | 10-15 мин | Да |
| 7 | Holding | 10-15 мин | Да |

**С параллельным запуском** — 20-30 минут wallclock (ограничено самым медленным).
Без параллельности — 90-130 минут.

После — synth ещё 10-15 минут Claude Code на сервере.

**К концу дня у нас есть**: 8 deep-research + 1 hybrid-framework synthesis + заготовка для
Шага 2 methodology.

---

*Prompts collection v1-2026-04-18. Составлено для Ruslan для массового запуска через Perplexity
Pro DeepMode. Обновляй этот файл по мере получения результатов — добавляй в конец каждого
промпта "**результат:** path/to/*.md" чтобы не потерять связки.*
