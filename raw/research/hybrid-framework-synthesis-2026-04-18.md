# Jetix Hybrid Framework: Синтез восьми моделей в одну операционную архитектуру

> **Дата:** 18 апреля 2026
> **Контекст:** Ruslan, solo-operator из Берлина, 12 Claude-Code агентов, цель $50K revenue до 30.06.2026.
> **Базис:** восемь deep-research документов 2026-04-18 (software, Левенчук/ШСМ, platform-OS, community, consulting, product/SaaS, agency, holding).
> **Назначение:** не реферат, а синтетическая архитектура, в которой каждая из моделей занимает строго определённый слой, а противоречия между ними разрешены для конкретного контекста Jetix.

---

## 1. Executive Summary

Jetix в своей текущей форме — не «software company», не «agency», не «consulting», не «platform». Это **восьмислойная архитектура**, в которой каждая классическая бизнес-модель XXI века исполняет строго одну функцию, а критическое конкурентное преимущество рождается именно из того, что эти слои сшиты в один организм одним человеком с помощью двенадцати AI-агентов.

**Ядро гипотезы.** Software company — это не «чем Jetix является», это **операционная система** (foundation layer): Git, CI/CD, Docs-as-code, Diátaxis, prompt-as-code, SRE, blameless postmortems, eval-pipelines для промптов ([software-deep-research, D1 что переносится 1:1](software-deep-research-2026-04-18.md)). Над ней — **cognitive layer** от Левенчука: системное мышление 3.0, FPF, ролевая онтология, альфы с состояниями, граф создания, стратегирование как метод выбора метода ([levenchuk-deep-research, разделы 3–6 и 11](levenchuk-deep-research-2026-04-18.md)). Это не «добавка», это тот слой, который превращает 12 Claude-агентов из набора инструментов в **систему систем** (по Левенчуку — system-of-systems с эмерджентными свойствами).

Над мышлением — три практических слоя, отвечающих за **денежный поток и рост**: agency + productized consulting как pragmatic revenue engine до 30.06.2026 ([agency-deep-research, раздел 10.6](agency-deep-research-2026-04-18.md); [consulting-deep-research, разделы 10.4–10.5](consulting-deep-research-2026-04-18.md)); product/micro-SaaS как параллельный micro-MRR-track ([product-deep-research, разделы 10.1–10.4](product-deep-research-2026-04-18.md)); community layer (Jetix Alliance / Jetix Club) как мембрана между бизнесом и клиентами ([community-deep-research, раздел 9.1 hybrid elite B2B + practitioner](community-deep-research-2026-04-18.md)).

И два слоя-горизонта: **topology layer** (platform) — куда всё это эволюционирует через 18–36 месяцев ([platform-os-deep-research, фазы 1–4](platform-os-deep-research-2026-04-18.md)); и **portfolio layer** (holding) — как капитал, время и внимание перераспределяются между проектами внутри Jetix по Constellation-принципу ([holding-deep-research, раздел 3 и 10.5](holding-deep-research-2026-04-18.md)).

**Почему это работает только вместе, а не по отдельности.** У каждой модели есть своя ловушка, и ровно другая модель её закрывает:

- Чистый software-подход даёт инфраструктуру, но не даёт бизнес-модели — это дыра, которую закрывают agency/consulting слоями.
- Чистый MBB-консалтинг строится на пирамиде младших аналитиков — фатально для solo-operator, потому что у него нет пирамиды ([consulting-deep-research, 10.2](consulting-deep-research-2026-04-18.md)). Решение: заимствовать интеллект (MECE, Pyramid Principle, Issue Tree), но заменить пирамидальный leverage на AI-leverage 1:100 ([consulting-deep-research, 10.3](consulting-deep-research-2026-04-18.md)).
- Чистая agency-модель затягивает в service trap и feast/famine ([agency-deep-research, раздел 8](agency-deep-research-2026-04-18.md)). Решение: продуктизация + community layer + переход к платформенному IP.
- Чистая SaaS-модель требует 6–18 месяцев до первой выручки и часто — VC-денег ([product-deep-research, раздел 8.3](product-deep-research-2026-04-18.md)); для solo это несовместимо с целью $50K до июня.
- Чистая community-модель долго строится и требует 15–25 часов в неделю от founder ([community-deep-research, 9.6](community-deep-research-2026-04-18.md)); без agency-выручки её невозможно финансировать.
- Чистая platform-модель страдает от chicken-and-egg ([platform-os-deep-research, раздел 2](platform-os-deep-research-2026-04-18.md)) — её можно строить, только имея уже community и agency-клиентов как anchor tenants.
- Чистая holding-модель требует капитала, которого у solo нет ([holding-deep-research, раздел 1.3](holding-deep-research-2026-04-18.md)). Но holding-**дисциплина** (ROIC, kill-criteria, separate P&L) применима на любом масштабе и именно она спасает solo от размазывания внимания по 8 проектам.
- Чистый Левенчук без software-инфраструктуры и бизнес-моделей — это «академическая башня» ([levenchuk-deep-research, раздел 10 «слишком абстрактно»](levenchuk-deep-research-2026-04-18.md)). Но software без Левенчука — это CI/CD для прокрастинации: вы можете идеально версионировать промпты, которые решают не ту задачу.

**Главный инсайт синтеза.** В 2026 году AI сместил узкое место со «скорости исполнения» на «качество постановки задачи и приёмки» ([levenchuk-deep-research, раздел 6 «Конференция МИМ-2026»](levenchuk-deep-research-2026-04-18.md)). Это означает, что все восемь моделей сходятся в одной точке: ценность solo-operator с AI — это **judgment** (суждение, framing, acceptance), а не delivery. Agency-модель в этой логике — не «мы делаем работу», а «мы ставим правильный вопрос». Consulting — не «мы анализируем», а «мы применяем MECE к вашей проблеме, пока вы этого не делаете». Platform — не «мы хостим данные», а «мы курируем доверие». Community — не «мы собираем людей», а «мы создаём facilitated peer exchange, где возникает коллективное суждение». Software-foundation — не «код и инфраструктура», а «прослеживаемость решений». Левенчук — «мышление письмом как экзокортекс suggestment».

**Финансовая цель $50K до 30.06.2026 достигается через agency + consulting слои**, с первым micro-SaaS-MRR-экспериментом (Jetix Club Tier 1) как параллельным треком. Community закладывается в Q2 как lead-generation-движок для H2. Platform — H2 2026 как anchor tenant (1–3 Mittelstand-клиента через IHK). Holding-дисциплина — с первого дня как управление вниманием. Этот документ детализирует каждый слой с принципами, применением в Jetix, рисками и метриками, затем разрешает 12 конфликтов между моделями, фиксирует 8 open questions и даёт понедельный migration path.

---

## 2. Foundation Layer: Software Company

### 2.1 Почему software — это фундамент, а не бизнес-модель

Главный сдвиг в понимании Jetix: «Jetix = software company» не означает, что Jetix продаёт software. Это означает, что **управление бизнесом ведётся как управление кодовой базой** ([software-deep-research, Блок B1 Business as Software](software-deep-research-2026-04-18.md)). Это не метафора — это буквальная практика: каждое решение — коммит, каждый процесс — скрипт, каждая роль — модуль, каждый провал — postmortem.

Конкретные практики, которые переносятся 1:1 на solo-operator с 12 Claude-Code агентами:

- **Docs-as-code и Diátaxis.** Вся база знаний Jetix живёт в Git в четырёх формах: tutorials (как учиться новому), how-to guides (как делать конкретную задачу), reference (правила и определения), explanation (почему так устроено) ([software-deep-research, D1](software-deep-research-2026-04-18.md)). Это не «хорошая практика» — это условие того, чтобы 12 агентов работали с общим контекстом без дрейфа.
- **Prompt-as-code.** Промпты агентов версионируются через Semantic Versioning (v1.2.0), а не «latest» ([software-deep-research, C6 и D1](software-deep-research-2026-04-18.md)). Откат промпта занимает 30 секунд вместо часа отладки «почему manager-агент вдруг стал писать по-другому».
- **CI/CD для промптов (eval pipelines).** Перед деплоем новой версии промпта — автоматический прогон на золотом датасете (golden dataset) из 10–50 эталонных кейсов ([software-deep-research, D1](software-deep-research-2026-04-18.md)). Если качество упало > порога — блок мержа.
- **Blameless postmortems.** Если агент «галлюцинировал» — виноват не агент, виновата система: промпт, контекст, guardrails ([software-deep-research, A9 и D1](software-deep-research-2026-04-18.md)). 5 Whys, зафиксированные в Notion/Git.
- **Error Budgets / Hallucination Budgets.** Адаптация SRE-практики: у каждого агента есть бюджет «допустимых ошибок» в неделю. При превышении — система останавливается, промпт переписывается, evals обновляются ([software-deep-research, D2](software-deep-research-2026-04-18.md)).
- **Risk-based routing (AI observability).** Низкий риск (internal queries) — минимальные проверки; средний — ML-классификатор; высокий (финансы, клиентские коммуникации) — трёхслойная валидация + human-in-the-loop ([software-deep-research, C4](software-deep-research-2026-04-18.md)). Инструменты: LangSmith/Langfuse для трейсинга, Braintrust для step-level tracing, Patronus AI для детекции галлюцинаций, Latitude для кластеризации failure patterns.

### 2.2 Что НЕ переносится (cargo-cult для solo)

Критически важно: Scrum, story points, daily standups с агентами, Jira-микроменеджмент, SAFe — всё это **убивает velocity solo-operator** ([software-deep-research, D3–D4](software-deep-research-2026-04-18.md)). Это инструменты координации больших команд, и для одного человека с 12 агентами они — чистый overhead и «Agile theatre». Замена — Shape Up: 2–6 недельные «bets» (ставки), высокоуровневая цель, свобода реализации ([software-deep-research, A3 и D6](software-deep-research-2026-04-18.md)).

### 2.3 Применение в Jetix и метрики слоя

Foundation layer в Jetix должен быть полностью развернут в ближайшие 2 недели (он дешёвый и обратимый, и без него все остальные слои нестабильны):

1. Монорепозиторий `jetix-os/` с подкаталогами `prompts/`, `playbooks/`, `agents/`, `clients/`, `evals/`, `postmortems/`.
2. 12 системных промптов агентов вынесены в `prompts/v1/*.md` с семантическим версионированием.
3. Golden datasets по 10 кейсов на агента минимум (sales-lead: 10 квалифицированных лидов с ожидаемым ответом; delivery: 10 типичных клиентских запросов и т.д.).
4. Один eval-скрипт (Python + Anthropic SDK + простой diff), который прогоняет новые промпты против предыдущих.
5. `POSTMORTEMS.md` начинается с сегодняшнего дня — любой сбой агента фиксируется в течение 24 часов.

**Метрики слоя:**
- Prompt version stability: среднее время между rollback < 1 раз в неделю.
- Hallucination budget: < 3 «клиент-видимых» ошибок агента в месяц.
- Docs coverage: 100% внешних клиентских процессов задокументированы в Diátaxis-формате перед сейлзом.
- Eval pass rate: новый промпт мержится только при pass rate ≥ 90% против golden dataset.

**Риски слоя:** over-engineering. Solo-operator может потратить 3 недели на идеальный CI/CD и не сделать ни одного клиентского звонка. Правило: **foundation должен быть построен за 14 дней максимум**, дальше — только клиенты.

---

## 3. Cognitive Layer: Левенчук / ШСМ как операционная система для solo+AI

### 3.1 Роль слоя в архитектуре

Если software — это инфраструктура для артефактов (промпты, код, документация), то cognitive layer — это **инфраструктура для решений**. Это то, что позволяет solo-operator не быть задавленным комбинаторикой: 12 агентов × несколько клиентов × несколько проектов × 7 бизнес-моделей = хаос без системной онтологии.

Левенчук даёт пять практических примитивов, которые решают этот хаос ([levenchuk-deep-research, разделы 3–5 и 10–11](levenchuk-deep-research-2026-04-18.md)):

1. **Ролевая онтология.** Разделение «роль vs агент-исполнитель» ([levenchuk-deep-research, раздел 9 глоссарий и 11 Архитектурные выводы](levenchuk-deep-research-2026-04-18.md)). У Jetix не «12 агентов», у Jetix — **12 ролей**, каждая из которых может быть исполнена Claude Sonnet 4, GPT-5, человеком-фрилансером или сотрудником Ruslanа. Когда Claude 5 выходит — меняется исполнитель, не архитектура.

2. **Альфы с состояниями.** «Клиент» — это альфа с состояниями: `lead → qualified → proposed → negotiating → closed/lost`. «Проект» — альфа: `discovery → audit → pilot → production → retainer`. «Счёт» — альфа: `issued → sent → paid → reconciled` ([levenchuk-deep-research, раздел 11 «Из концепции альф»](levenchuk-deep-research-2026-04-18.md)). Каждый агент отвечает за перевод конкретной альфы из состояния A в состояние B — это формализованная замена «что должен делать агент».

3. **Граф создания.** Кто создаёт что для кого ([levenchuk-deep-research, разделы 4 и 11](levenchuk-deep-research-2026-04-18.md)). Для Jetix это буквально: Ruslan создаёт контекст для Claude Code; Claude Code создаёт код/контент для 12 агентов-ролей; роли создают артефакты для клиента; клиент получает целевую систему (например, «автоматизированный процесс обработки инвойсов»). Каждое звено — потенциальное bottleneck.

4. **Стратегирование как метод выбора метода.** Перед началом любого нового типа работы — ответ на вопрос «каким методом мы это делаем?» ДО запуска агентов ([levenchuk-deep-research, раздел 4 и раздел 11 «Разделите стратегирование и исполнение»](levenchuk-deep-research-2026-04-18.md)). Агенты не стратегируют — это функция оператора. Это прямой антидот к карго-культу и SAFe-ритуалам без смысла ([software-deep-research, D4](software-deep-research-2026-04-18.md)).

5. **Смещение узкого места к постановке и приёмке.** Конференция МИМ-2026 явно зафиксировала: в AI-эпоху узкое место — не исполнение, а framing проблемы и acceptance результата ([levenchuk-deep-research, раздел 6 «Конференция МИМ-2026»](levenchuk-deep-research-2026-04-18.md)). Для Jetix это означает жёсткое правило: **80% ошибок агентов — это плохо поставленные задачи**. Инвестиция в чёткость постановки > инвестиция в «лучшего агента».

### 3.2 FPF и context engineering вместо prompt engineering

Левенчук разрабатывает First Principles Framework (FPF) именно как протокол для работы с AI-агентами: не «инструкция для конкретной задачи», а **«мировоззрение»** (регламент мышления), с которым агент подходит к любой задаче ([levenchuk-deep-research, раздел 6 «FPF как протокол для AI»](levenchuk-deep-research-2026-04-18.md)). Для Jetix это означает, что ключевой артефакт — не «промпт sales-агента», а «онтология продаж Jetix»: что является целевой системой (договор, а не «лид»), кто stakeholders (CFO, IT-Leiter, Geschäftsführer в немецком Konsenskultur — [agency-deep-research, 11.4](agency-deep-research-2026-04-18.md)), какие альфы трекаются, какие состояния допустимы.

### 3.3 Применение в Jetix: от 12 «агентов» к 12 ролям

Каждый из 12 Claude-Code агентов переопределяется как **роль** с явным манифестом:

| Роль | Целевая система роли | Главная альфа | Метод | Acceptance criteria |
|---|---|---|---|---|
| manager | Операционное состояние Jetix | Проект / Сделка | Weekly review, grading | Все альфы в валидных состояниях |
| strategist | Метод работы над типом задачи | Стратегический документ | Стратегирование (выбор метода) | «каким методом делаем» зафиксировано письменно |
| sales-lead | Pipeline | Клиент (`lead → closed`) | MECE-сегментация ICP | ≥ 2 discovery calls/week |
| sales-research | Квалифицированный контакт | Prospect | ICP-скрининг по 100 компаний | ≥ 50 персонализированных контактов/week |
| marketing | Distribution | Контент-единица | LinkedIn-контент, SEO | ≥ 3 немецкоязычных поста/week |
| delivery | Клиентский результат | Deliverable | Productized delivery playbook | On-time rate ≥ 90% |
| analyst | Данные → инсайт | Анализ | MECE, hypothesis-driven | Executive summary на 1 странице |
| ops | Внутренние процессы Jetix | Задача | Shape Up bets | Все SLA соблюдены |
| product | Jetix Club / micro-SaaS | Feature / SKU | PLG activation | PQL → paid conversion tracked |
| research | Внешние знания | Research note | Deep research по промпту | Новый insight в week's log |
| writer | Текст | Документ | Diátaxis (tutorial / how-to / reference / explanation) | Проходит eval на понятность |
| gitops | Версионирование и CI/CD | Commit / PR | Prompt-as-code, evals | Eval pass ≥ 90% перед мержем |

**Это не реорганизация — это переонтологизация.** До этого шага 12 агентов были «набором чатов». После — система ролей с прослеживаемостью и возможностью замены исполнителя ([levenchuk-deep-research, раздел 11 «Архитектурные выводы»](levenchuk-deep-research-2026-04-18.md)).

### 3.4 Мышление письмом как operating principle

Левенчук настаивает: мышление происходит при формулировании текста, не «внутри головы» ([levenchuk-deep-research, раздел 12 и habr.com источник](levenchuk-deep-research-2026-04-18.md)). Для solo-operator с AI это критично в трёх смыслах: (а) тренировка собственного суждения; (б) создание экзокортекса для агентов (они читают то, что вы написали); (в) формирование базы прецедентов для будущего обучения или передачи.

Операционная практика в Jetix: ежедневный рабочий журнал в `decisions/YYYY-MM-DD.md`, еженедельный review в `weekly/YYYY-Www.md`, quarterly letter (даже для себя) в `letters/YYYY-Qn.md` (аналог Mark Leonard / Berkshire — [holding-deep-research, раздел 3.5 и 10.2](holding-deep-research-2026-04-18.md)).

### 3.5 Метрики слоя и риски

**Метрики:**
- Role clarity: для каждой роли существует манифест с целевой системой, альфой, методом, acceptance criteria (12/12 к концу недели 1).
- Strategizing discipline: перед любой новой задачей — запись «каким методом делаем» (≥ 90% cases).
- Written artifacts per week: 7 daily logs + 1 weekly review + 1 FPF-update минимум.

**Риски:**
- Академическая ловушка. Полное освоение ШСМ — ~2 года и 20 курсов ([levenchuk-deep-research, раздел 10 «слишком абстрактно»](levenchuk-deep-research-2026-04-18.md)). Solo с горизонтом до июня должен применять селективно. Правило: брать примитивы (роль/альфа/метод/граф создания), не брать полную онтологическую машинерию (холоны, мереология FPF, интеллект-стек из 17 дисциплин).
- Отсутствие бизнес-моделей. Левенчук почти не касается GTM, юнит-экономики, конверсий ([levenchuk-deep-research, раздел 10](levenchuk-deep-research-2026-04-18.md)). Этот gap закрывается остальными шестью слоями.

---

## 4. Topology Layer: Platform как долгосрочная цель

### 4.1 Почему platform — это топология, а не модель на сегодня

Platform — это форма распределения ценности через multi-sided network ([platform-os-deep-research, раздел 1.1](platform-os-deep-research-2026-04-18.md)). Для solo-operator сегодня это **не** подходящая бизнес-модель: chicken-and-egg problem, MVE (minimum viable ecosystem) требует годы, governance и curation — это full-time-job для команды ([platform-os-deep-research, раздел 2 и 9.5](platform-os-deep-research-2026-04-18.md)). Но platform — это **топологическая цель** на 18–36 месяцев, к которой Jetix готовится уже сегодня тремя конкретными способами.

### 4.2 Три аксиомы, которые применяются сразу

Из [platform-os-deep-research, разделы 9.3–9.4](platform-os-deep-research-2026-04-18.md):

1. **Come for the tool, stay for the network.** Standalone value ДО появления сети. Для Jetix это означает: EU AI Act Compliance Toolkit, Mittelstand AI Readiness Assessment, Jetix-playbooks — это артефакты, которые нужно создать до первого члена Alliance, и которые сами по себе приносят ценность (lead magnet + органическое SEO + доказательство экспертизы).

2. **Anchor tenant сначала.** Один крупный Mittelstand-игрок (≥ 500 сотрудников, оборот €100M+) как founding member с governance-ролью. Логотип + кейс = доказательство легитимности ([platform-os-deep-research, 9.2](platform-os-deep-research-2026-04-18.md)). Канал к anchor: IHK (Industrie- und Handelskammer), VDMA, Bitkom — это подтверждается и в community-research ([community-deep-research, 9.2](community-deep-research-2026-04-18.md)) и в agency-research ([agency-deep-research, 10.6](agency-deep-research-2026-04-18.md)).

3. **Local network effects достаточно.** Не надо глобально — надо доминировать в DACH (как Uber сначала в одном городе) ([platform-os-deep-research, 10 takeaway 9](platform-os-deep-research-2026-04-18.md)). Bavaria → BaWü → Германия → DACH. Это радикально снижает требования к supply/demand liquidity.

### 4.3 Как это связывает слои

Platform в Jetix — это не отдельный бизнес, это **форма, которую принимают остальные слои через 18–36 месяцев**:

- Community layer (Jetix Alliance) становится membership-tier платформы.
- Agency layer даёт compliance-certification и co-sell mechanics с vendors ([platform-os-deep-research, 9.3 «Из AWS»](platform-os-deep-research-2026-04-18.md)).
- Product layer (Jetix Club, micro-SaaS) становится SDK/API-first tooling ([platform-os-deep-research, 9.3 «Из Stripe»](platform-os-deep-research-2026-04-18.md)).
- Holding layer отвечает за capital allocation между верхними слоями.
- Software foundation обеспечивает trust architecture (GDPR, ZDR, EU-only infrastructure) — что для немецкого Mittelstand-CFO читается на front page, а не в footer ([platform-os-deep-research, 10 takeaway 4](platform-os-deep-research-2026-04-18.md)).

### 4.4 Что конкретно строится в Q2 2026 (подготовка к платформе)

- **EU AI Act Compliance Kit** как стандалонный артефакт: чек-лист, шаблон DPA, GDPR-brief для Mittelstand, готовые ответы для IT-Leiter. Публикуется бесплатно, служит lead magnet.
- **Mittelstand AI Readiness Assessment** как productized consulting (€5K — [consulting-deep-research, 10.5](consulting-deep-research-2026-04-18.md)), одновременно — прото-платформенная оценка ([platform-os-deep-research, 9.3 «Из Hugging Face: freemium → enterprise»](platform-os-deep-research-2026-04-18.md)).
- **180-day change notice policy** зафиксирована в документации с первого дня ([platform-os-deep-research, 10 takeaway 10](platform-os-deep-research-2026-04-18.md)).
- **Data network effects** — каждое взаимодействие с клиентом/Alliance-членом (с их согласия и анонимно) обогащает Jetix Mittelstand AI Benchmark dataset ([platform-os-deep-research, 10 takeaway 8](platform-os-deep-research-2026-04-18.md)). Через 2 года — уникальный data moat.

### 4.5 Метрики и риски

**Метрики слоя (12–36 месяцев):**
- Alliance MRR (membership fees).
- Marketplace GMV + take rate (0% → 10–15% по мере роста).
- NPS anchor tenants.
- Benchmark dataset coverage (компании/use cases).

**Риски:**
- Слишком ранний запуск marketplace без MVE → прийдёт demand и уйдёт разочарованным ([platform-os-deep-research, 10 takeaway 11](platform-os-deep-research-2026-04-18.md)).
- Big platform competition (SAP, Microsoft, Deutsche Telekom AI strategy). Mitigation: hyper-focus на Mittelstand-нишу, personal relationships, community moat ([platform-os-deep-research, 9.5](platform-os-deep-research-2026-04-18.md)).
- Founder burnout при попытке запустить platform одновременно с agency-revenue. Mitigation: strict sequencing — Alliance до Marketplace, Marketplace не ранее 30 Alliance members.

---

## 5. Community Layer: Jetix Alliance / Jetix Club как мембрана

### 5.1 Роль: мембрана между Jetix и рынком

Community в Jetix — это не отдельный бизнес («мы делаем community»), а **мембрана** между delivery-слоем и клиентской базой. Она выполняет три функции одновременно:

1. **Retention** — превращает одноразовых клиентов в долгосрочные отношения.
2. **Referral** — peer-to-peer рекомендации, которые работают в B2B DACH-контексте сильнее любой рекламы ([community-deep-research, 9.2 и 9.6](community-deep-research-2026-04-18.md)).
3. **Insight loop** — источник живых problem statements для определения новых productized services и eventual платформенных features.

### 5.2 Двухуровневая структура

Синтез community-research и product-research приводит к одной конкретной конфигурации ([community-deep-research, 9.1](community-deep-research-2026-04-18.md); [product-deep-research, 10.1 Вектор B](product-deep-research-2026-04-18.md)):

**Уровень 1 — Jetix Alliance (Elite B2B, YPO-inspired).**
- ICP: CEO / Geschäftsführer Mittelstand DACH (€10M–€500M выручки), принимают решения по AI.
- Forum Groups: 6–8 CEO из non-competing отраслей, ежемесячные video calls, ежеквартальные physical meetups, Chatham House Rules.
- Membership fee: €3,000–€5,000/год.
- Core value: confidential peer exchange + vendor vetting + deal flow + curated benchmarks.
- Платформа: Slack corporate + Notion knowledge base.

**Уровень 2 — Jetix Club (Practitioner / Reforge-inspired).**
- ICP: CTO, Head of Digital, AI Project Managers из тех же компаний + DACH-solo-предприниматели (расширенная аудитория).
- Membership fee: Tier 1 «Insider» €29/mo, Tier 2 «Accelerator» €99/mo, Tier 3 «VIP» €299/mo ([product-deep-research, 10.1 Вектор B](product-deep-research-2026-04-18.md)).
- Value: AI implementation templates, tool reviews, cohort-based training, monthly workshop, community forum.
- Платформа: Circle (knowledge-base orientation) + Discord для async.

**Уровень 3 — Public funnel (free).**
- Немецкоязычный AI-newsletter weekly → аудитория → конверсия в платные уровни.
- LinkedIn-присутствие (Ruslan как авторитет «AI для Mittelstand»).
- Ежегодный Mittelstand AI Summit (в перспективе — H2 2026).

### 5.3 Critical conflict resolved: long runway vs fast cashflow

Здесь **прямое противоречие** между community-research и agency-research:

- Community-модель требует 3–6 месяцев контент-first-подготовки до первой платной продажи ([community-deep-research, 9.2 «LinkedIn content first»](community-deep-research-2026-04-18.md)).
- Agency-модель требует €50K к 30.06.2026 через активный outreach уже в мае ([agency-deep-research, 10.6](agency-deep-research-2026-04-18.md)).

**Разрешение.** Community запускается **параллельно** agency, но с разными целями по фазам:
- Q2 2026 (май–июнь): Jetix Club Tier 1 как low-risk пробная продажа для DACH-solo-предпринимателей (не Mittelstand-CEO) — это быстрый тест продукта, €29/mo × 20–30 early adopters = €580–870/mo микровыручка плюс аудитория.
- Jetix Alliance запускается только после первого agency-клиента, потому что этот первый клиент становится anchor tenant и founding member с 50% скидкой навсегда ([community-deep-research, 9.2 «Founding Member offer»](community-deep-research-2026-04-18.md)).
- Public newsletter стартует немедленно (неделя 1) — это медленный актив, но без него не построится ни Alliance, ни SaaS-distribution.

### 5.4 Operating principles

Из [community-deep-research, раздел 9.6 и Заключение takeaways 1, 3, 5, 8, 13](community-deep-research-2026-04-18.md):

- **Forum Groups как core unit**, который нельзя автоматизировать. 6–8 CEO в non-competing группах, founder facilitation.
- **Chatham House Rules как founding charter** — подписывается при вступлении. Без confidentiality немецкие CEO не делятся реальными проблемами.
- **Concierge matchmaking** первый год — personal introductions между членами. Это создаёт ранний WOM.
- **Quarterly ROI report** каждому члену: «благодаря Alliance вы: сэкономили X на vendor vetting, получили intro к Y» — единственный способ обосновать ежегодный renewal для DACH-покупателей.
- **AI operational layer как differentiator vs IHK/VDMA.** AI-powered onboarding, summarization, member matching — это то, что отличает Jetix Alliance от обычной Handelskammer.

### 5.5 Метрики и риски

**Метрики:**
- Alliance: MRR, churn (< 15% annual), NPS ≥ 50, deal flow через Alliance (target Year 1: €2M+ в сделках между членами или с Jetix).
- Club: активация (% членов, сделавших 3+ действий в первые 30 дней), weekly active members (WAM), Tier upgrade rate.
- Public: newsletter subscribers, open rate ≥ 35%, click-through ≥ 5%.

**Риски:**
- Dead Forum Syndrome ([community-deep-research, 9.6](community-deep-research-2026-04-18.md)). Решение: seeded content от founder + weekly «что нового» thread + curated member spotlights.
- Founder burnout (15–25 часов/week на community — цена, которую невозможно делегировать на старте — [community-deep-research, 9.6 и Takeaway 15](community-deep-research-2026-04-18.md)).
- Confidentiality breach — один случай разрушает trust навсегда. Mitigation: формальный NDA-лайт документ.
- Competitor dilution в Alliance — проверка applications на competitive conflicts.

---

## 6. Delivery Layer: Agency + Consulting Hybrid — pragmatic revenue engine

### 6.1 Почему именно гибрид

Agency и consulting — формально разные модели, но для solo-operator с AI они **сливаются в один оффер** ([agency-deep-research, 1.3](agency-deep-research-2026-04-18.md)). В классическом мире consulting продаёт «что делать» (strategy), agency — «как сделать» (implementation). Для Jetix грань стирается: AI-Readiness Audit — это consulting deliverable ([consulting-deep-research, 10.5](consulting-deep-research-2026-04-18.md)), но дальше клиент подписывается не на «часы на внедрение», а на доступ к AI-агентам ([consulting-deep-research, 10.4 и 11.3](consulting-deep-research-2026-04-18.md)) — что ближе к agency-retainer.

Итоговая формула: **Consulting даёт framing и intellectual credibility (MBB-интеллект), Agency даёт delivery-дисциплину и recurring revenue**. AI-leverage 1:100 делает это маржинально невозможным для традиционных игроков ([consulting-deep-research, 10.3](consulting-deep-research-2026-04-18.md)).

### 6.2 Productized SKUs (конкретный оффер Jetix)

Синтез [agency-deep-research, 10.1](agency-deep-research-2026-04-18.md) и [consulting-deep-research, 10.5–10.6](consulting-deep-research-2026-04-18.md):

| SKU | Формат | Цена | Длительность | Deliverable |
|---|---|---|---|---|
| AI Readiness Audit | Productized consulting | €5,000–€8,000 | 2 недели | 25-стр. PDF + 10-слайдовый executive summary + ROI calculation |
| Quick Win Automation | Implementation project | €10,000–€15,000 | 4 недели | 1 production-ready process (invoice, HR, customer routing) |
| Custom Agent Build | Implementation project | €25,000–€40,000 | 8–12 недель | Кастомный multi-agent workflow + документация |
| Operations Retainer | Monthly recurring | €3,000–€5,000/mo | ongoing | SLA-backed operations + monthly reviews |

**Три уровня цен (Good-Better-Best)** — классический Simon-Kucher приём ([consulting-deep-research, 11.4](consulting-deep-research-2026-04-18.md)), плюс немецкая Tagessätze-логика: €5K audit = ~2.5–3 дня сеньор-эксперта, что вписывается в approval limit CEO Mittelstand без совета директоров ([consulting-deep-research, 10.6](consulting-deep-research-2026-04-18.md)).

### 6.3 MBB intellectual toolkit (украсть) + AI leverage (заменить)

Из [consulting-deep-research, 10.1–10.3](consulting-deep-research-2026-04-18.md) — четыре интеллектуальных инструмента, которые Ruslan должен освоить и применять через AI-агентов:

1. **MECE + hypothesis-driven problem solving** → делегируется на уровне промпта: не «найди проблемы», а «проверь гипотезу X в ветке Y дерева проблем».
2. **Pyramid Principle (Barbara Minto)** → Ruslan пишет верхушку (главный тезис), AI пишет низ (аргументация, данные).
3. **80/20 rule** → жёсткое правило: клиент видит только те 20%, которые дают 80% результата.
4. **Delivery discipline** → SOW с жёстким in-scope/out-of-scope, acceptance criteria, change order process ([consulting-deep-research, 11.2](consulting-deep-research-2026-04-18.md)).

**Что НЕ копировать ни из agency, ни из consulting:**
- Hourly billing ([agency-deep-research, 10.4 и 11.1](agency-deep-research-2026-04-18.md); [consulting-deep-research, 10.2](consulting-deep-research-2026-04-18.md)). Value-based / fixed-price only. При AI-leverage hourly делает тебя беднее.
- Большая команда fallacy. Jetix leverage = кремний, не углерод ([consulting-deep-research, 10.2](consulting-deep-research-2026-04-18.md)).
- «Boil the ocean» research. Сузить перед расширением ([consulting-deep-research, 10.2](consulting-deep-research-2026-04-18.md)).

### 6.4 Sales conversation structure (DACH-специфичная)

Из [agency-deep-research, 11.3 и 11.4](agency-deep-research-2026-04-18.md), синтезируя с [consulting-deep-research, 10.6](consulting-deep-research-2026-04-18.md):

1. **Diagnose, не pitch.** Вопросы: «Какие процессы съедают больше всего времени у вашей команды? Где теряете деньги на ручной работе?»
2. **Anchor budget early.** «Проекты подобного масштаба обычно €25–50K. Это бюджет, с которым мы можем работать?» — отсекает неплатёжеспособных.
3. **Propose AI Audit как Trojan Horse.** €5K, 2 недели, «стоимость audit идёт в зачёт основного проекта».
4. **Немецкий Konsenskultur.** Готовиться к 6–12-недельному sales cycle, к участию IT-Leiter + CFO + Geschäftsführer одновременно ([agency-deep-research, 11.4](agency-deep-research-2026-04-18.md)).
5. **DSGVO как differentiator.** «Данные на серверах в ЕС, DPA готов, ZDR с LLM-провайдерами» — выносится в front page.
6. **Субсидии (go-digital, ZIM) как sales argument** ([agency-deep-research, 10.3 и 11.1](agency-deep-research-2026-04-18.md)).

### 6.5 Unit economics для Jetix

Из [agency-deep-research, 10.2](agency-deep-research-2026-04-18.md) и [consulting-deep-research, 10.3](consulting-deep-research-2026-04-18.md):

| Параметр | Традиционный agency | Jetix (solo + 12 agents) |
|---|---|---|
| Проект €25,000 | 2–3 разработчика × 4 недели | 1 человек × 2 недели |
| Gross margin | 40–50% (≈€10–12K) | 75–80% (≈€19–20K) |
| Параллельных проектов | 2–3 | 4–6 |
| Effective hourly rate | €100–200 | €1,000–1,500 |
| Ежемесячный потенциал | €50–80K | €80–150K при full pipeline |

**€50K до 30.06.2026 достижимы** через 2–3 audits (€10–20K), 1 Quick Win (€10–15K) и 1 начальный retainer (€3–5K) — реалистичный pipeline при outreach с мая ([agency-deep-research, 10.6](agency-deep-research-2026-04-18.md)).

### 6.6 Метрики и риски

**Метрики:**
- Weekly outreach volume ≥ 50 персонализированных LinkedIn-контактов ([agency-deep-research, 11.7](agency-deep-research-2026-04-18.md)).
- Discovery calls/week ≥ 2–3.
- Proposal win rate 25–35% для qualified leads.
- Gross margin per project ≥ 70%.
- Revenue concentration < 50% одного клиента на старте; план снижения к < 25% ([agency-deep-research, 11.7](agency-deep-research-2026-04-18.md)).
- Effective hourly rate ≥ €500/hr.
- Project on-time delivery ≥ 90%.
- Retainer conversion rate (project → retainer) ≥ 30%.

**Риски:**
- Service trap / scale trap ([agency-deep-research, 8.1](agency-deep-research-2026-04-18.md)). Mitigation: каждый проект производит переиспользуемые компоненты (промпты, workflows), которые станут кирпичами платформы ([agency-deep-research, 10.5](agency-deep-research-2026-04-18.md)).
- Feast/famine cycle ([agency-deep-research, 8.5](agency-deep-research-2026-04-18.md)). Mitigation: pipeline as habit — 5 часов/week на outreach ВНЕ зависимости от текущей загрузки.
- Scope creep. Mitigation: SOW + change order process с первого проекта ([consulting-deep-research, 11.2](consulting-deep-research-2026-04-18.md)).
- Founder burnout. Mitigation: AI-leverage, time boxes, чёткое разделение «оператор vs исполнитель» по Левенчуку.

---

## 7. Portfolio Layer: Holding-дисциплина на масштабе solo

### 7.1 Что из Constellation переносится на solo, а что нет

Buffett / Berkshire требует капитала, которого у solo нет ([holding-deep-research, раздел 2 и 10.1](holding-deep-research-2026-04-18.md)). Но **Constellation Software под Mark Leonard** — это другое: small-deal discipline, radical decentralization, MECE-scenarios для каждой acquisition, ROIC as единственный metric ([holding-deep-research, 3.1–3.5](holding-deep-research-2026-04-18.md)). Это философия, не размер капитала, и она **прямо применяется** к solo-operator с 8 параллельными проектами.

Прямой перенос в Jetix ([holding-deep-research, 10.1–10.2, 10.7](holding-deep-research-2026-04-18.md)):

1. **Project grading.** Каждый из N активных проектов Jetix — `active / stable / zombie / archive`. Честно, еженедельно, в одной Notion-таблице.
2. **Kill criteria.** Zombie-проект живёт максимум 4 недели после grading; потом kill.
3. **Separate P&L per project.** MRR, monthly cost (tools + tokens + время × $rate), IRR проекта.
4. **Hurdle rate ≥ 25% IRR.** Новый проект запускается только если ожидается ≥ 25% IRR в 12 месяцев ([holding-deep-research, 10.2 пункт 4](holding-deep-research-2026-04-18.md)).
5. **Quarterly letters.** Даже для себя. Честно о том, что работает и что нет ([holding-deep-research, 10.2 пункт 5](holding-deep-research-2026-04-18.md)).
6. **Owner earnings, не revenue.** MRR − hosting − AI tokens − (время × $rate) = real profit. Если time-cost убивает маржу — это zombie, даже если MRR растёт.

### 7.2 Portfolio-thinking для solo: Pieter Levels, Rob Walling, Andrew Wilkinson

Три solo-моделей из [holding-deep-research, раздел 6](holding-deep-research-2026-04-18.md):

- **Pieter Levels** — канонический solo-portfolio, много экспериментов, распределение внимания по power law ([holding-deep-research, 6.1](holding-deep-research-2026-04-18.md)).
- **Rob Walling / Stair Step Approach** ([holding-deep-research, 6.3](holding-deep-research-2026-04-18.md)) — step 1: один продукт на чужой платформе; step 2: свой продукт на своём домене; step 3: real SaaS. Для Jetix это значит: не пытайся сразу на step 3.
- **Andrew Wilkinson / Tiny** ([holding-deep-research, 4.1](holding-deep-research-2026-04-18.md)) — «Berkshire for internet companies», но без VC, без debt, только cash-on-cash. Вопрос Wilkinson: «enough?» — дисциплинирующий анти-growth-obsession.

### 7.3 Third layer unlocks second layer

Ключевой синтетический insight из [holding-deep-research, 10.5](holding-deep-research-2026-04-18.md): без holding-дисциплины platform layer и community layer становятся реактивными, а не стратегическими. Если нет kill-criteria — Ruslan будет тащить зомби-проект в Alliance «на всякий случай». Если нет hurdle rate — новые productized SKUs плодятся без фильтра.

Holding layer — это **функция капитал-аллокации между слоями**. Он отвечает на вопрос «сколько часов/денег/внимания в этом квартале идёт на agency vs community vs product?»

### 7.4 Jetix Holdings BV/OÜ (H2 2026)

Долгосрочно — Estonian OÜ или Netherlands BV как holding-entity ([holding-deep-research, 10.3](holding-deep-research-2026-04-18.md)), с top-3 проектами как subsidiaries. Первая acquisition — H2 2026 на Acquire.com: профитный AI/micro-SaaS за $30–80K с $1.5–3K/mo MRR ([holding-deep-research, 10.3](holding-deep-research-2026-04-18.md)). Применение MECE 4-scenario analysis перед покупкой, 25%+ IRR target.

**No debt, no leverage** — Thrasio cautionary tale ([holding-deep-research, 5.1 и 10.7 пункт 2](holding-deep-research-2026-04-18.md)). All-equity acquisitions, cash-only.

### 7.5 Метрики и риски

**Метрики:**
- Количество проектов по grade: active / stable / zombie / archive (target: ≤ 2 zombie в любой момент).
- IRR per project (actual vs projected после 12 месяцев).
- Portfolio ROIC (combined).
- Hours allocation discipline: Toggl-reports ежемесячно — где реально ушло время vs где должно было.
- Kill rate: 1–2 kills per quarter нормально и здоровé.

**Риски:**
- Over-diversification («размазывание»). Mitigation: power law — 80% времени на top-2 проекта.
- Premature hire. Решение: community manager только при 150+ Alliance members или €300K+ ARR ([community-deep-research, 9.5](community-deep-research-2026-04-18.md)).
- Ложная экономия в owner-earnings. Если не трекать время через Toggl — все проекты «выглядят profitable». Mitigation: 30 дней жёсткого time-tracking в Q2 для baseline.

---

## 8. Product Layer: Micro-SaaS параллельно service-бизнесу

### 8.1 Почему micro-SaaS — а не enterprise SaaS

Enterprise SaaS требует 6–18 месяцев до первого клиента, минимум 3–5 человек команды (SDR/AE/CSM), SOC 2 Type II ($50–120K first year) — фатально для solo с целью $50K до июня ([product-deep-research, 10.3 и 8.3](product-deep-research-2026-04-18.md)). Но **micro-SaaS** — это другой вид: $5K–50K MRR, solo или 1–3 contractors, 30% CAGR индустрия ([product-deep-research, раздел 9 и Заключение](product-deep-research-2026-04-18.md)).

Примеры 2024–2026: Cursor $2B ARR с 150 сотрудниками, Lovable $400M ARR с 146 сотрудниками, Manus $100M ARR как agent platform pivot ([product-deep-research, 9.4](product-deep-research-2026-04-18.md)) — доказывают, что AI-native SaaS ломает старые per-employee-revenue бенчмарки.

### 8.2 Три вектора для Jetix

Синтез [product-deep-research, 10.1](product-deep-research-2026-04-18.md):

- **Вектор A (primary): Productized services with subscription layer.** 3 fixed-price SKU (€500–5K) + Operations Retainer (€3–5K/mo). При 10–15 клиентах/месяц = €15–22.5K MRR. Это НЕ классический SaaS, но SaaS-подобная экономика. Запускается за 2–4 недели. Это тот же слой, что и agency (раздел 6), просто с другой упаковкой.
- **Вектор B (secondary): Jetix Club как SaaS membership.** €29/mo Tier 1, €99/mo Tier 2, €299/mo Tier 3. При 50/20/5 членов — €4,925/mo ([product-deep-research, 10.1 Вектор B](product-deep-research-2026-04-18.md)). Это **тот же слой, что и community**, просто с PLG-механикой и Stripe-billing.
- **Вектор C (horizon 2027+): Mittelstand Alliance as SaaS platform.** Beyond solo без anchor clients. Запускается только если H2 2026 дал 3+ pilot Mittelstand-клиентов с pre-committed интересом.

### 8.3 SaaS practices to adopt немедленно

Из [product-deep-research, 10.2](product-deep-research-2026-04-18.md), но с фильтром для solo:

1. **MRR/churn/LTV с первого платящего клиента.** Простая Notion-таблица: Date | Client | ARPU | Status | Churn reason.
2. **Self-serve onboarding.** Welcome email Day 0, value email Day 3, check-in Day 7. Activation checklist.
3. **Stripe Billing + annual payment option (15% discount).** Cash flow + retention.
4. **Cal.com + Notion workspace template** для каждого клиента.
5. **GDPR-first positioning** как competitive advantage vs US SaaS.
6. **Single-player mode** (PLG-принцип): клиент получает ценность ДО появления сети.
7. **Rule of 40 мышление** с ранней стадии: growth rate + profit margin ≥ 40.

### 8.4 Что НЕ копировать (solo-filter)

- T2D3 growth trajectory — burn-funded machine, не для bootstrap ([product-deep-research, 10.3](product-deep-research-2026-04-18.md)).
- Enterprise sales SDR/AE/CSM — требует команды $500K+/year.
- Per-seat licensing as primary model — требует viral growth или active sales.
- SOC 2 Type II в Year 1 — $50–120K, нерелевантно до $100K ARR.

### 8.5 Consulting → Productized → Micro-SaaS bridge

Из [product-deep-research, 10.4 и 10.5 takeaway 12](product-deep-research-2026-04-18.md) и [consulting-deep-research, 11.3](consulting-deep-research-2026-04-18.md):

Классическая механика solo-operator 2024–2025: consulting первые 3 месяца → MVP на 6-й → $1K MRR на 8-й → $10K MRR на 12-й. Для Jetix:

- Q2 2026: consulting/agency даёт $50K cash-cushion.
- Q3 2026: Jetix Club Tier 1 Launch (результат 6 месяцев newsletter/content).
- Q4 2026: первый пилот — auto-generated AI compliance check или кастомный agent template как standalone Stripe-платный продукт.
- 2027: Tier 2/3 growth, один из productized SKUs превращается в standalone SaaS.

### 8.6 Метрики и риски

**Метрики:**
- MRR per tier, total MRR.
- Monthly churn rate (target < 5% для Tier 1, < 2% для Tier 2/3).
- Rule of 40 score (growth + margin).
- Activation rate (% new members completing onboarding checklist in 30 days).
- Expansion revenue (% revenue from tier upgrades и retainer-conversions).

**Риски:**
- Distraction from revenue-generating agency. Mitigation: product-layer — это не primary focus в Q2, это параллельный backburner.
- Churn if community not active ([product-deep-research, 10.1 Вектор B risk](product-deep-research-2026-04-18.md)). Mitigation: weekly async Loom updates, structured challenges, member spotlights.
- Pricing confidence — не занижать ([product-deep-research, 10.5 takeaway 11](product-deep-research-2026-04-18.md)).

---

## 9. Integration: как 8 слоёв работают вместе

### 9.1 Архитектурная диаграмма в тексте

```
┌──────────────────────────────────────────────────────────────┐
│ Layer 7: PORTFOLIO (Holding discipline)                      │
│ Capital allocation: time × money × attention across layers   │
│ Primitives: grading, kill-criteria, ROIC, hurdle rate        │
├──────────────────────────────────────────────────────────────┤
│ Layer 6: TOPOLOGY (Platform, horizon 18-36m)                 │
│ Alliance → Marketplace → Data network effects → Ecosystem    │
│ Primitives: anchor tenant, take rate, GMV, multi-sided       │
├──────────────────────────────────────────────────────────────┤
│ Layer 5: MEMBRANE (Community)                                │
│ Jetix Alliance (Elite B2B) + Jetix Club (Practitioner)       │
│ Primitives: forum groups, Chatham House, ROI reports         │
├──────────────────────────────────────────────────────────────┤
│ Layer 4: DELIVERY (Agency + Consulting hybrid) ← PRIMARY $   │
│ Productized SKUs: Audit / Quick Win / Custom / Retainer      │
│ Primitives: MECE, Pyramid, SOW, value-based pricing          │
├──────────────────────────────────────────────────────────────┤
│ Layer 3: PRODUCT (Micro-SaaS parallel track)                 │
│ Jetix Club tiers, productized services with Stripe billing   │
│ Primitives: MRR, churn, activation, Rule of 40               │
├──────────────────────────────────────────────────────────────┤
│ Layer 2: COGNITIVE (Левенчук / ШСМ)                          │
│ Roles vs agents, alphas, graph of creation, strategizing     │
│ Primitives: FPF, role-manifests, alpha-state-tracking        │
├──────────────────────────────────────────────────────────────┤
│ Layer 1: FOUNDATION (Software company practices)             │
│ Git, CI/CD, Diátaxis, prompt-as-code, SRE, postmortems       │
│ Primitives: versioning, eval pipelines, risk-based routing   │
└──────────────────────────────────────────────────────────────┘
```

Слой 0 (не нарисован, потому что он пронизывает все): Ruslan + 12 Claude-Code role-агентов как **исполнительное ядро**.

### 9.2 Dataflow: как сигналы текут между слоями

**От низа вверх (operational signals):**
- Foundation (L1) → Cognitive (L2): postmortem выявляет плохую постановку задачи → апдейт FPF / role-manifest.
- Cognitive (L2) → Delivery (L4): новый метод (например, изменение sales-conversation structure по MBB Pyramid Principle) → обновление playbook в `delivery/`.
- Delivery (L4) → Product (L3): переиспользуемый компонент (промпт для AI Audit) → кандидат на productized SKU.
- Delivery (L4) → Membrane (L5): довольный клиент → приглашение в Alliance как founding member.
- Product (L3) + Membrane (L5) → Topology (L6): критическая масса членов + vendors → platform MVE.
- Все слои → Portfolio (L7): P&L, IRR, time-spent-tracking.

**Сверху вниз (strategic signals):**
- Portfolio (L7) → Все: kill-criteria, hurdle rate, capital allocation.
- Topology (L6) → Delivery (L4): требования к anchor tenant формируют ICP для agency.
- Membrane (L5) → Delivery (L4): запросы от Alliance CEO становятся новыми audit-темами.
- Membrane (L5) → Product (L3): запросы от Jetix Club становятся новыми tier-features.
- Cognitive (L2) → Foundation (L1): «каким методом работаем» определяет структуру папок, eval-критериев, CI-тестов.

### 9.3 Распределение 12 Claude-Code агентов по слоям

Каждый агент (роль в терминах Левенчука) имеет primary layer и secondary layers:

| Роль | Primary layer | Secondary layers | Ключевая альфа |
|---|---|---|---|
| manager | L7 Portfolio | L2 Cognitive, L4 Delivery | Портфельная allocation |
| strategist | L2 Cognitive | L7 Portfolio, L6 Topology | Метод работы над типом задачи |
| sales-lead | L4 Delivery | L5 Membrane | Клиент (lead → closed) |
| sales-research | L4 Delivery | L6 Topology | Prospect / ICP |
| marketing | L5 Membrane | L3 Product, L4 Delivery | Контент-единица |
| delivery | L4 Delivery | L1 Foundation | Deliverable |
| analyst | L4 Delivery | L2 Cognitive, L7 Portfolio | Анализ |
| ops | L1 Foundation | L7 Portfolio | Задача / SLA |
| product | L3 Product | L6 Topology, L5 Membrane | Feature / SKU |
| research | L2 Cognitive | L6 Topology, L5 Membrane | External knowledge note |
| writer | L1 Foundation | L2 Cognitive, L5 Membrane | Документ |
| gitops | L1 Foundation | L2 Cognitive | Commit / PR |

**Ключевое наблюдение.** Ни один агент не живёт в одном слое. Это означает, что role-manifests должны явно описывать связь с primary и secondary слоями, иначе агент дрейфует. Это применение «графа создания» ([levenchuk-deep-research, раздел 4](levenchuk-deep-research-2026-04-18.md)): каждый агент создаёт артефакты для других агентов/слоёв.

### 9.4 Rituals: как слои синхронизируются во времени

- **Daily** (15 минут): Ruslan читает digest от manager-роли — альфы, которые поменяли состояние за сутки; решения, которые требуют human-in-the-loop (высокий риск по risk-based routing — [software-deep-research, C4](software-deep-research-2026-04-18.md)).
- **Weekly** (2 часа, воскресенье): Shape Up-style review ([software-deep-research, A3](software-deep-research-2026-04-18.md)). Что побеждает? Что зомби? Одно «next bet» на следующую неделю. Запись в `weekly/`.
- **Monthly** (4 часа, 1-е число): Kill check по каждому zombie ([holding-deep-research, 10.2 пункт 9](holding-deep-research-2026-04-18.md)). P&L update. Quarterly letter draft (накопление).
- **Quarterly** (8 часов): Quarterly letter публикуется — для себя в Q2, публично с Q3 ([holding-deep-research, 10.7 пункт 7](holding-deep-research-2026-04-18.md)). Strategy-review: что меняется в sequencing слоёв.
- **Annually** (2 дня): 3-year review в стиле Leonard. Stress-test всей архитектуры.

### 9.5 The Jetix Flywheel (как слои усиливают друг друга)

```
Agency/Consulting project (L4)
    → reusable prompt/workflow → Product SKU (L3)
    → satisfied client → Alliance founding member (L5)
    → peer referral → next Agency project (L4)
    → data (anonymized) → Mittelstand Benchmark (L6)
    → credibility → anchor tenant for Platform (L6)
    → cash flow → investment in new project via holding (L7)
    → Portfolio grading shifts focus back to L4
```

Это flywheel работает только если ВСЕ слои присутствуют одновременно. Один слой отсутствует — колесо буксует. Если нет L1 (software foundation) — агенты дрейфуют, и клиент получает нестабильный deliverable. Если нет L2 (cognitive) — Ruslan задавлен комбинаторикой и решает не ту задачу. Если нет L4 (delivery) — нет cashflow, и все остальные слои финансируются из кармана. Если нет L5 (membrane) — agency превращается в feast/famine lottery без retention ([agency-deep-research, 8.5](agency-deep-research-2026-04-18.md)). Если нет L7 (portfolio) — внимание размазывается по zombies и хорошие проекты голодают.

### 9.6 Две интеграционные практики, которых нет ни в одном source-документе

**Практика A: Layer-tagged decisions.** Каждое решение в `decisions/YYYY-MM-DD.md` получает теги `L1 L2 L4` — показывая, на какие слои это решение влияет. Через месяц анализ тегов показывает, где реально тратится когнитивное внимание vs где должно. Это применение holding-мышления ([holding-deep-research, 7.2 capital allocation](holding-deep-research-2026-04-18.md)) к attention allocation, что особенно критично для solo.

**Практика B: Cross-layer post-mortem.** Любой провал агента (L1) обязательно анализируется через призму L2 (была ли задача правильно поставлена?), L4 (был ли корректный SOW?) и L7 (стоило ли вообще этот проект брать?). Это превращает технический инцидент в стратегический сигнал, и именно так Levenchuk's «узкое место в постановке» операционализируется ([levenchuk-deep-research, раздел 11 «Смещение узкого места»](levenchuk-deep-research-2026-04-18.md)).

### 9.7 Почему именно 8 слоёв, а не 5 или 12

На каждый слой — одна специфическая функция, которую не выполняет никто другой:

- L1 отвечает на «как не потерять артефакты».
- L2 отвечает на «какой метод мы применяем».
- L3 отвечает на «как сделать повторяющуюся выручку без human labor».
- L4 отвечает на «откуда деньги сейчас».
- L5 отвечает на «кто наши союзники».
- L6 отвечает на «куда это эволюционирует».
- L7 отвечает на «куда направлено внимание».
- Слой 0 (Ruslan + 12 агентов) отвечает на «кто это исполняет».

Объединение слоёв (например, L3+L4 в один «revenue layer») уничтожает их различие: productized service (L4) и micro-SaaS membership (L3) требуют принципиально разной дисциплины (SOW/delivery vs MRR/churn/activation). Разделение даёт ясность о том, какие метрики в каждом слое критичны.

---

## 10. Conflicts Resolved

Ниже — 12 конкретных противоречий между исходными моделями и их разрешение для контекста Jetix.

**Conflict 1. SaaS VC-scale vs Wilkinson no-VC solo.**
- Source conflict: [product-deep-research, 8.3 bootstrap vs VC](product-deep-research-2026-04-18.md) vs [holding-deep-research, 4.1 Tiny no-debt](holding-deep-research-2026-04-18.md).
- Resolution: **bootstrap + selective RBF**. Solo-operator идёт Wilkinson-путём (all-equity, cash-only) для foundation/community/holding слоёв. Product layer может взять Revenue-Based Financing (Capchase / EU-equivalent) при достижении $5K+ MRR для ускорения growth без dilution ([product-deep-research, 8.2](product-deep-research-2026-04-18.md)). VC отвергается как opt-in, не как принцип.

**Conflict 2. MBB pyramid leverage vs solo AI leverage.**
- Source conflict: [consulting-deep-research, 2.1 Pyramid model](consulting-deep-research-2026-04-18.md) vs [consulting-deep-research, 10.3 AI-leverage 1:100](consulting-deep-research-2026-04-18.md).
- Resolution: **intellectual pyramid без human pyramid**. Ruslan — как Engagement Manager MBB. 12 AI-агентов — как команда из 5 junior-analysts + 2 associates + 1 consultant. Но без payroll, без up-or-out, без bench-cost. MECE/Pyramid/Issue Tree используются буквально, но на уровне промптов агентов.

**Conflict 3. Community long runway (3–6 мес) vs Agency fast cashflow (до июня).**
- Source conflict: [community-deep-research, 9.2 LinkedIn content first 3-6 months](community-deep-research-2026-04-18.md) vs [agency-deep-research, 10.6 €50K до 30.06.2026](agency-deep-research-2026-04-18.md).
- Resolution: **параллельные треки с разными целями**. Agency outreach — primary track в Q2 с eжедневным LinkedIn. Jetix Club Tier 1 запускается в Q2 как micro-test продукта, не как primary community-play. Alliance запускается ПОСЛЕ первого agency-клиента (он становится founding member). Newsletter стартует неделей 1 и накапливает аудиторию медленно.

**Conflict 4. Scrum/Agile ceremonies vs Shape Up async.**
- Source conflict: [software-deep-research, A3 и D3](software-deep-research-2026-04-18.md) vs SAFe-критика [software-deep-research, D4](software-deep-research-2026-04-18.md).
- Resolution: **Shape Up для Jetix, Scrum отвергнут полностью**. 2–6-недельные bets, высокоуровневая цель, свобода реализации агентами. Никаких daily standups с AI.

**Conflict 5. Левенчук онтологическая глубина vs solo speed-execution.**
- Source conflict: [levenchuk-deep-research, раздел 10 «где слишком абстрактно»](levenchuk-deep-research-2026-04-18.md) vs agency Q2 urgency.
- Resolution: **селективное применение 5 примитивов** (роль, альфа, граф создания, стратегирование, мышление письмом). Остальная ШСМ-машинерия (холоны, полный интеллект-стек, FPF-мереология) — read-only, не применяется.

**Conflict 6. Platform chicken-and-egg vs anchor tenant strategy.**
- Source conflict: [platform-os-deep-research, раздел 2 chicken-and-egg](platform-os-deep-research-2026-04-18.md).
- Resolution: **не строить platform в Q2**. Строить standalone tools (EU AI Act Kit, Readiness Assessment) + Alliance через agency-клиентов. Platform — H2 2026 только при наличии 3+ Alliance members и 2+ agency-retainer-клиентов.

**Conflict 7. Hourly billing agency (traditional) vs value-based (AI-leverage).**
- Source conflict: [agency-deep-research, 2.1 billing models](agency-deep-research-2026-04-18.md) vs [agency-deep-research, 10.4 не копировать hourly](agency-deep-research-2026-04-18.md).
- Resolution: **value-based / fixed-price ONLY**. Hourly запрещён. Если клиент просит hourly — конвертировать в day rate (Tagessätze) или отказаться. При AI-leverage hourly — самоубийство.

**Conflict 8. Generalist positioning vs niching.**
- Source conflict: «AI для всех» vs [agency-deep-research, 10.1 нишевый positioning](agency-deep-research-2026-04-18.md).
- Resolution: **жёсткая ниша с Q2 2026**. «AI-трансформация для немецкого Mittelstand производственного сектора, 50–500 сотрудников». Одна вертикаль, один ICP. Расширение — после 10 клиентов в нише.

**Conflict 9. Shared infrastructure (Constellation synergies) vs separate P&L.**
- Source conflict: [holding-deep-research, 7.3 synergies vs independence](holding-deep-research-2026-04-18.md).
- Resolution: **shared infrastructure (Jetix OS, 12 role-agents, prompts, Git, Notion), separate P&L**. Как Constellation: один operating system, но каждый subsidiary имеет свои финансы ([holding-deep-research, 10.7 пункт 11](holding-deep-research-2026-04-18.md)).

**Conflict 10. SaaS per-seat pricing vs solo productized fixed-price.**
- Source conflict: [product-deep-research, 4.1 pricing models](product-deep-research-2026-04-18.md) vs [product-deep-research, 10.3 не копировать per-seat](product-deep-research-2026-04-18.md).
- Resolution: **fixed-price SKU для services**, **flat monthly tier для Club membership**. Per-seat отвергается как primary model на solo-стадии (требует viral growth или active sales, оба невозможны без команды).

**Conflict 11. Community freemium vs no-freemium первый год.**
- Source conflict: [platform-os-deep-research, 9.3 Hugging Face freemium](platform-os-deep-research-2026-04-18.md) vs [community-deep-research, 9.3 и Takeaway 9](community-deep-research-2026-04-18.md).
- Resolution: **no freemium в Alliance (elite B2B), freemium (newsletter) в public funnel**. Alliance с первого дня платная (€3–5K/год), иначе dilution качества. Public newsletter бесплатный — это distribution, не community.

**Conflict 12. McKinsey Big-firm methodology vs Roland Berger operational / Simon-Kucher pricing.**
- Source conflict: [consulting-deep-research, разделы 4 и 11.4](consulting-deep-research-2026-04-18.md).
- Resolution: **для DACH-рынка — Roland Berger + Simon-Kucher > McKinsey**. «Operations» продаётся в DACH лучше, чем «strategy». Позиционирование Jetix: «инструмент радикального сокращения Opex», не «disruptive GenAI synergy». Pricing: Simon-Kucher Good-Better-Best + anchoring.

---

### 10.13 Meta-разрешение: почему конфликты вообще возникают

12 конфликтов выше — не случайность. Они все проистекают из двух фундаментальных смещений, которые AI внёс в бизнес-архитектуру:

**Смещение 1: leverage-источник.** В XX веке leverage строился на человеческой пирамиде (MBB leverage 1:10, Accenture 1:30). В 2026 году для solo-operator он строится на AI-агентах (1:100 по расчёту [consulting-deep-research, 10.3](consulting-deep-research-2026-04-18.md)). Это меняет все практики, построенные вокруг «human hours as input»: hourly billing, payroll management, utilization rate, up-or-out, bench management. Все эти практики в source-документах появляются в форме «классический подход vs AI-разворот», и во всех случаях правильный ответ — AI-разворот.

**Смещение 2: bottleneck-позиция.** В классических моделях bottleneck — в execution speed (сколько строк кода/слайдов/звонков в день). В AI-эпохе bottleneck — в framing и acceptance ([levenchuk-deep-research, раздел 6 и 11](levenchuk-deep-research-2026-04-18.md)). Это меняет смысл Scrum/Agile-ритуалов (они решают execution-bottleneck, которого больше нет), Agile story points (агенты работают минуты), sales pipeline metrics (важнее qualified leads, чем объём outreach).

Все 12 конфликтов разрешаются применением этих двух линз: любой source-принцип, который предполагает human-pyramid leverage или execution-bottleneck — отвергается или переинтерпретируется. Любой source-принцип, который фокусируется на framing, курации, trust и дисциплине суждения — усиливается.

---

## 11. Open Questions

Восемь вопросов, на которые восемь research-документов ответа не дают, и которые критичны для Jetix:

1. **Как измерять «качество постановки задачи» для AI-агентов?** Если узкое место теперь на framing ([levenchuk-deep-research, раздел 6](levenchuk-deep-research-2026-04-18.md)), то нужна метрика — иначе нельзя оптимизировать. Кандидат: % задач, завершённых с первого прогона без rework. Но baseline не установлен ни в одном документе. Требуется собственный бенчмарк Jetix за Q2 2026.

2. **Точный порог Alliance-членов для найма community manager.** Research говорит «~100–150 членов» ([community-deep-research, 9.5](community-deep-research-2026-04-18.md)), но это эвристика из US/EO/YPO данных. Для немецкого Mittelstand-кейса с AI-differentiator — возможно, порог иной. Требуется empirical test в Q3–Q4 2026.

3. **Сколько проектов одновременно — реальный потолок для solo + 12 AI-агентов?** Research даёт 4–6 параллельных agency-проектов ([agency-deep-research, 10.2](agency-deep-research-2026-04-18.md)), но это extrapolation. Какой реальный cap с учётом community time (15–25 час/неделю) + content + ops? Нужно протестировать в Q3 2026 (2 клиента → 4 клиента → burnout-check).

4. **Когда запускать первый hire/contractor и в какую роль.** Research даёт разные ответы: agency — VA/developer в «Phase 2» ([product-deep-research, 10.4](product-deep-research-2026-04-18.md)); community — community manager при €300K+ ARR ([community-deep-research, 9.5](community-deep-research-2026-04-18.md)); holding — first hire CEO самого большого проекта в 2027 H1 ([holding-deep-research, 10.3](holding-deep-research-2026-04-18.md)). Consistent answer отсутствует. Требуется решение Ruslan-specific с учётом личных burnout-триггеров.

5. **Реальный конверсионный коэффициент LinkedIn outreach → discovery call → paid client в DACH в 2026.** Research даёт 4–6% outreach → call → 25–35% proposal win rate ([agency-deep-research, 11.7](agency-deep-research-2026-04-18.md)), но эти числа из US/UK sources. Немецкий конверсионный коэффициент для AI-agency может быть 0.5–2× от US (Konsenskultur удлиняет cycle, но повышает close rate при prequalification). Собственные данные Jetix после 200 контактов будут ground truth.

6. **Как правильно атрибутировать revenue между слоями в holding-modeling.** Если клиент пришёл через Alliance (L5), купил audit (L4), стал Club member (L3) и дал data для Benchmark (L6) — как делится P&L? Без правильной атрибуции holding-grading искажён. Требуется собственный фреймворк, research пока даёт только примеры Constellation/Danaher для single-product units.

7. **Регуляторный риск EU AI Act для Jetix-клиентов в 2026–2027.** Research упоминает ([platform-os-deep-research, 9.5](platform-os-deep-research-2026-04-18.md)) compliance-as-product, но конкретные требования для Mittelstand-внедрений (high-risk vs limited-risk категории AI-систем) — moving target. Нужна live консультация с EU AI Act юристом в Q2.

8. **Каков реальный TAM DACH-Mittelstand для AI-agency?** Research даёт разрозненные данные: $24B немецкий SaaS market ([product-deep-research, источник 46](product-deep-research-2026-04-18.md)), Mittelstand cuts AI investments in 2025 ([agency-deep-research, 11.1 и источник 18](agency-deep-research-2026-04-18.md)). Но top-down vs bottom-up TAM для productized AI-services (€5K–50K engagements) не посчитан. Нужен собственный расчёт через IHK-статистику в Q2.

---

## 12. Migration Path для Jetix: до 30.06.2026 и дальше

### 12.1 Q2 2026 — понедельный план до $50K

**Week 1 (22–28 апреля 2026): Foundation + Cognitive set-up.**
- Мон–Вт: Монорепозиторий `jetix-os/` развёрнут. 12 role-manifests (роль, целевая система, альфа, метод, acceptance criteria) написаны и закоммичены. Prompt-as-code: v1.0.0 для каждого агента.
- Ср: Golden datasets по 10 кейсов на 4 критичных роли (sales-lead, delivery, analyst, writer). Eval-скрипт работает.
- Чт: FPF-lite документ написан (3–5 страниц): целевая система Jetix, stakeholders, граф создания, принципы работы с клиентами.
- Пт: Первый weekly review. Toggl установлен, time-tracking начат. Quarterly letter Q2 draft начат.
- Метрика недели: все 12 role-manifests существуют, eval pipeline работает, time-tracking активен.

**Week 2 (29 апреля – 5 мая): Positioning + assets.**
- Landing page на немецком: `jetix.de/mittelstand-ai` или эквивалент. Productized SKU-прайс-лист: AI Readiness Audit €5,000 / Quick Win Automation €12,000 / Custom Agent Build €30,000 / Operations Retainer €3,500/mo.
- EU AI Act Compliance Kit (lead magnet) опубликован.
- LinkedIn Ruslan: переписан profile, 3 поста на немецком о AI для Mittelstand (practical use cases с ROI).
- ICP-список: 200 компаний DACH manufacturing SMB 50–500 employees, €10–100M revenue.
- Первый newsletter opt-in на landing page.
- Метрика недели: landing live, 200 ICP identified, 3 LinkedIn posts published, Newsletter #0 (positioning) отправлен.

**Week 3 (6–12 мая): Outreach launch.**
- 50 персонализированных LinkedIn-сообщений Geschäftsführer/IT-Leiter.
- 3–5 warm-email sequences к personal network.
- Референсные запросы: IHK/VDMA знакомые.
- 3 поста на немецком в LinkedIn (один case-study-style, один technical, один opinion).
- Метрика недели: 50 outreach, 3 LinkedIn posts, ≥ 2 discovery calls booked.

**Week 4 (13–19 мая): First discovery cycle.**
- 2–3 discovery calls проведены.
- 1–2 AI Audit proposals отправлены.
- Jetix Club Tier 1 landing page soft-launch (€29/mo). Первые 5 invites в personal network.
- Quarterly letter Q1 draft завершён (ретроспектива).
- Метрика недели: ≥ 2 discovery, ≥ 1 audit proposal sent, Club first 3–5 paying members.

**Week 5 (20–26 мая): First sale.**
- 50 outreach.
- 3+ discovery calls.
- Target: закрыть first AI Audit (€5–8K).
- Newsletter #1 публичный (аудитория ~50–100 подписчиков из org-network).
- Метрика недели: **first paid client = foundation для Alliance anchor**.

**Week 6 (27 мая – 2 июня): Delivery discipline test.**
- Audit delivery: week 1. Применение MECE + Pyramid Principle + AI-leverage.
- 50 outreach продолжается.
- Первое post-mortem по delivery process.
- Метрика недели: audit on-track, 2+ discovery calls, pipeline ≥ €30K.

**Week 7 (3–9 июня): Audit deliver + upsell.**
- Audit sdano → immediately Quick Win Automation proposal.
- Case study draft начат (anonymized).
- Club: 5–10 paying members.
- Метрика недели: First audit NPS ≥ 8, upsell proposal sent.

**Week 8 (10–16 июня): Scale pipeline.**
- 2-е Audit начато (закрыто в Week 6–7).
- 1st Retainer negotiation.
- LinkedIn: еженедельный ритм (3 posts/week).
- Метрика недели: pipeline value ≥ €50K, MRR ≥ €500 (Club).

**Week 9 (17–23 июня): Delivery week.**
- 2-е Audit делается, первый Retainer подписывается.
- Quarterly letter Q2 draft close to publishing.
- Метрика недели: Active revenue run-rate ≥ €40K Q2.

**Week 10 (24–30 июня): Close Q2.**
- Revenue total check: target €50K.
- Quarterly letter Q2 published (внутренне).
- Q3 planning: community kick-off (Alliance first 3 invites to first clients), micro-SaaS track roadmap.
- Метрика недели: **€50K revenue достигнуты или зафиксирован gap-plan**.

### 12.2 Q3–Q4 2026 (H2): community + продуктизация

**Июль:**
- Jetix Alliance launch с 3–5 founding members (из первых agency-клиентов с 50% скидкой навсегда). Первая Forum Group setup.
- Публичный Quarterly letter Q2.
- Club growth: target 20 paying members across Tier 1/2.
- Agency pipeline: 3 active projects.

**Август:**
- First Alliance Forum Group meeting.
- Second productized SKU: «AI Compliance Mini-Audit» за €2,500 — lower-barrier entry, upsell-ready.
- Newsletter: 300+ subscribers.

**Сентябрь:**
- Post-mortem по первым 6 месяцам. Serious strategy review.
- Toggl-данные — первый honest IRR calculation per project.
- Kill decision для любых zombie-проектов в personal portfolio.

**Октябрь:**
- Jetix Alliance: 10 members target. First "Mittelstand AI Summit" (soft, 30 attendees).
- Acquire.com browsing начат (holding preparation).
- First Mittelstand pilot для platform-proto-product (shared AI tool для 2–3 Alliance members).

**Ноябрь:**
- Acquire.com: первый shortlist 10 targets ($30–80K micro-SaaS с $1.5–3K MRR, 25%+ IRR проекта).
- Revenue run-rate: €10–15K MRR агентский + Club/Alliance MRR.

**Декабрь:**
- Первая acquisition (если подходящий target и IRR подтверждается).
- Jetix Holdings BV/OÜ setup (legal entity).
- Quarterly letter Q4: публичная версия.
- Год закрывается: €150–250K revenue total, foundation для 2027 есть.

### 12.3 2027 — масштабирование

**Q1 2027:**
- Second acquisition — если first идёт по плану; если нет — post-mortem + адаптация thesis.
- First hire: community manager или developer-contractor, в зависимости от bottleneck.
- Alliance: 20+ members. Curated AI Solutions Marketplace preparation (20 verified vendors shortlist).

**Q2 2027:**
- Marketplace soft-launch: 10 vendors, 0% take rate initially ([platform-os-deep-research, 9.3](platform-os-deep-research-2026-04-18.md)).
- Mittelstand AI Benchmark Report first annual edition (monetizable research product).
- Agency: 5–8 concurrent clients, но с тренжом к снижению custom-work и росту productized-share.

**Q3 2027:**
- Marketplace: 20 vendors, 10% take rate introduction с 180-day notice.
- Alliance: 30+ members. Second Forum Group запущена.
- Holding: 3–4 projects (Jetix core + 1–2 acquisitions + Alliance).

**Q4 2027:**
- Target: €500K–€1M combined ARR (agency + Alliance + marketplace + holding).
- Potential: первый real employee (не contractor), CEO для одного из subsidiaries или Chief of Staff.
- Review: надо ли привлекать RBF (Calm Company Fund, TinySeed equivalent в EU) для ускорения roll-up стратегии.

### 12.4 Ключевые quarterly milestones (кратко)

| Квартал | Revenue | Alliance | Club | Acquisitions | Team |
|---|---|---|---|---|---|
| Q2 2026 | €50K total | 0 (prep) | 5–10 | 0 | solo |
| Q3 2026 | €30K/quarter | 3–5 | 20 | 0 | solo |
| Q4 2026 | €50K/quarter | 10 | 30–40 | 1 small | solo + 1 contractor |
| Q1 2027 | €75K/quarter | 15 | 50 | 2 | solo + 2 contractors |
| Q2 2027 | €100K/quarter | 20 | 70–80 | 2 | solo + 2 contractors + CM |
| Q4 2027 | €150K/quarter | 30+ | 100+ | 3 | solo + team of 4 |

### 12.5 Triggers for strategy pivot

Migration path работает при условиях. Если хоть одно не выполняется — пересмотр:

- Q2 revenue < €30K к 30.06.2026 → reframe позиционирования (ниша слишком узкая или слишком широкая), либо pivot к более агрессивному outreach-каналу (cold email campaigns, partnerships с немецкими accountants).
- > 50% revenue от одного клиента в любой момент → forced diversification, даже ценой growth.
- Alliance churn > 25% annual в Year 1 → recheck value proposition и Forum Group facilitation.
- Любой hallucination budget breach > 2 раза в месяц → остановка нового onboarding, fix foundation.
- Toggl-данные показывают < 30% времени на revenue-generating activity → kill zombies, restructure.

---

### 12.6 Роль каждого слоя в Q2 2026 (сжато)

Чтобы миграционный путь не выродился в «занимаюсь всем сразу», в Q2 2026 каждый слой имеет строго одну функцию:

- **L1 Foundation:** построен за 2 недели, дальше только поддержание (без over-engineering).
- **L2 Cognitive:** 5 примитивов Levenchuk (роль, альфа, граф создания, стратегирование, мышление письмом) внедрены и живут.
- **L3 Product:** один minimum вектор (Jetix Club Tier 1) — маленький эксперимент, не главный фокус.
- **L4 Delivery:** главный трек — весь revenue к 30.06.2026 идёт отсюда.
- **L5 Membrane:** ньюслеттер стартует, Alliance — подготовка (не запуск в Q2).
- **L6 Topology:** только standalone assets (EU AI Act Kit, Readiness Assessment).
- **L7 Portfolio:** введено grading + time tracking, еженедельные review.

Все это даёт в сумме ~60 часов/неделю solo-загрузки (на грани, но и достижимо без burnout при AI-leverage).

---

## Заключение: Jetix как новый тип компании

Hybrid framework — это не «ещё одна бизнес-модель». Это утверждение, что в 2026 году grenзы между software company, consulting firm, agency, product company, community business, platform и holding — стёрты для solo-operator с 12 AI-агентами. Все они сосуществуют внутри одной личности, одного Git-репозитория, одной онтологии ролей. Ruslan — одновременно Engagement Manager McKinsey-style (L4 Delivery), системный инженер в духе Левенчука (L2 Cognitive), community host как у Sam Parr / Hampton (L5 Membrane), portfolio manager по Leonard / Constellation (L7), SRE-оператор (L1 Foundation), platform architect как у Stripe early days (L6), и product owner micro-SaaS как у Pieter Levels (L3).

Это стало возможно только потому, что AI снял требование human pyramid для интеллектуального leverage. И ровно поэтому требует **новой дисциплины** — той, которую предлагает Левенчук: разделить роль и агента, явно моделировать граф создания, стратегировать перед планированием, инвестировать в framing больше, чем в execution.

$50K до 30.06.2026 — это первая точка проверки этой гипотезы. Если достигается — hybrid framework валидирован и становится репродуцируемым паттерном для других solo-operators. Если нет — предсказуемая точка pivot в раздел 12.5.

Финальный тест фреймворка — не деньги, а воспроизводимость. Если Ruslan через 12 месяцев может написать документ, показать его другому solo-operator и получить от него работающую Jetix-подобную структуру — синтез сработал.

### Пять синтетических тезисов, которых нет ни в одном источнике

1. **Software foundation + Levenchuk cognitive — это не два слоя, а два окончания одного континуума.** Software версионирует артефакты (что сказано), Levenchuk версионирует методы (как думаем). Prompt-as-code и FPF — это один и тот же принцип на двух слоях абстракции.

2. **Agency и Community — это два конца одной трубы.** Первый agency-клиент — первый член Alliance. Первый член Alliance — first-referral source для второго agency-клиента. Это разрешает long-runway-vs-fast-cashflow конфликт не через компромисс, а через взаимное питание.

3. **Holding-дисциплина на масштабе solo — это attention allocation, а не capital allocation.** Buffett/Leonard распределяют капитал, solo-operator распределяет внимание. Метрики те же (ROIC, IRR, kill-criteria), но вход — часы, а не доллары. Это делает Constellation-принципы кратно доступнее для solo, чем кажется на первый взгляд.

4. **Platform — это не цель, это форма, в которую сами собой эволюционируют agency + community через два года.** Если Jetix правильно делает agency + community, то на 36-м месяце проснётся фактической platform: Alliance члены + vendors + benchmark data + compliance certification уже сформируют экосистему. «Strategировать platform» с нуля как цель — classic mistake. Стратегировать секвенсирование — правильный путь.

5. **12 Claude-Code агентов — не инструмент, а организационная структура.** Ролевая онтология Левенчука в сочетании с software org-chart-архитектурой ([software-deep-research, C5](software-deep-research-2026-04-18.md)) превращает 12 агентов в компактную скалируемую org. Это первая в истории company виды, где org chart рисуется не в HR-системе, а в Git-репозитории. И это делает company принципиально иным объектом аудита, рефакторинга и передачи, чем любая classic company.

---

*Документ подготовлен: Jetix Synthesis | 18 апреля 2026*
*Источники: 8 deep-research документов 2026-04-18, all cited inline via relative paths*
