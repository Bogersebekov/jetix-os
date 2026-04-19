---
research-id: R3
wave: 1
topic: Левенчук / ШСМ применение к AI-агентам и mega-corporation
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/levenchuk-for-ai-deep-research-2026-04-19.md
priority: P1 (критично — блокирует финализацию L2 Cognitive + role-manifest format)
depends-on: raw/research/levenchuk-deep-research-2026-04-18.md (uже существующий, используется как baseline)
---

# R3 — Левенчук / ШСМ для AI-агентов и mega-corp

## Зачем этот research

L2 Cognitive слой = системное мышление по методологии Анатолия Левенчука /
ШСМ (Школа системного менеджмента). Подтверждены 5 примитивов: роль, альфа,
граф создания, стратегирование, мышление письмом.

Но Левенчук писал про **индивидуальное знание человека**. Jetix нужно применить
это к **AI-агентам** + **mega-corporation**. Это не 1:1 перенос — нужна
adaptation.

Для финализации L2 Cognitive и написания role-manifest format нужно:
- Академически понять 5 примитивов (не поверхностно)
- Понять FPF (First Principles Framework) Левенчука
- Определить что из ШСМ берём / что read-only
- Спроектировать role-manifest format для Jetix
- Спроектировать FPF-lite (3-5 страниц) для Jetix
- Определить метрику «качество framing»

Выход research'а — input для документов `design/JETIX-FPF-LITE.md`,
`design/JETIX-ROLE-MANIFESTS.md`, и части `design/JETIX-ARCHITECTURE-FINAL.md`.

## Как использовать

Скопируй **всё между `=== PROMPT START ===` и `=== PROMPT END ===`** и
вставь в Perplexity Max Computer (собственная вкладка, параллельно R1 и R2).

**Язык prompt:** смешанный русско-английский — Левенчук пишет на русском, ключевые
термины ШСМ тоже на русском. Но запрос academic research допускает и английские
источники (OMG Essence, Peter Naur, AI-agent research).

---

=== PROMPT START ===

Ты — senior research analyst специализирующийся на системной инженерии, онтологическом моделировании и AI-agent architectures. Я прошу тебя провести **глубокий академический research** по теме **применения методологии Анатолия Левенчука (ШСМ, Школа системного менеджмента) к AI-агентам и масштабируемой корпоративной архитектуре**.

Это не «обзор Левенчука» — первичный обзор уже есть. Это **specific adaptation research**: как 5 примитивов ШСМ работают когда исполнитель не человек, а AI-агент, и когда система не индивидуальное знание, а growing mega-corporation.

## Контекст проекта Jetix (1500 слов)

**Кто такой Jetix.** AI-native компания строящаяся одним founder'ом (Ruslan, Берлин) с прицелом на мега-корпорацию. 12+ AI-агентов через Claude Code (Anthropic Opus 4.7). Сервер Hetzner, git monorepo, markdown-based architecture.

**Архитектура Jetix — 7 слоёв + L0:**
- L0 Executive Core: Ruslan + AI-агенты + future human executors через единую role-abstraction
- L1 Foundation: software practices (git, docs-as-code, prompt-as-code)
- **L2 Cognitive (этот research) — Левенчук / ШСМ**
- L3 Product, L4 Delivery (agency+consulting), L5 Membrane (community), L6 Platform, L7 Portfolio

**Ключевой принцип:** Роль ≠ исполнитель. Role-manifest — абстрактная спецификация (целевая система, ключевая альфа, метод, acceptance criteria). Исполнитель (AI или человек) подтаскивается под роль. **Люди = продолжение агентов через ту же самую role-abstraction.**

**Already approved Ruslan'ом на 100% (из нашего synthesis после Phase 1.5 Levenchuk research):**

1. **Ролевая онтология** (роль ≠ агент-исполнитель). Когда выходит Claude 5 — меняется исполнитель, не архитектура.
2. **Альфы с состояниями** — lifecycle-entities. Клиент: lead → qualified → proposed → negotiating → closed/lost. Проект: discovery → audit → pilot → production → retainer. Счёт: issued → sent → paid → reconciled.
3. **Граф создания** — explicit dependency map кто кому что создаёт. Для Jetix: Ruslan создаёт контекст для Claude Code → Claude создаёт код/контент для 12 ролей → роли создают артефакты для клиента → клиент получает целевую систему.
4. **Стратегирование** = метод выбора метода. Перед любой новой задачей — ответ на «каким методом делаем?» ДО запуска агентов. Агенты не стратегируют.
5. **Мышление письмом** — daily log, weekly review, quarterly letter как экзокортекс для Ruslan + агентов (они читают то, что написано).

**Ключевой инсайт:** в AI-эпоху узкое место — не execution, а **framing (постановка задачи) и acceptance**. 80% ошибок агентов = плохо поставленные задачи. Инвестиция в чёткость постановки > инвестиция в «лучшего агента».

**Что из ШСМ берём selectively (правило Ruslan'а):** 5 примитивов — yes. Полная ШСМ-машинерия (холоны, мереология FPF, интеллект-стек из 17 дисциплин) — read-only, не применяется. Левенчук сам пишет что полное освоение ~2 года и 20 курсов — для solo с дедлайном impractical.

**Текущие 12 ролей (будем переписывать как role-manifests):**

| Роль | Целевая система | Главная альфа | Метод (baseline) |
|------|-----------------|---------------|-------------------|
| strategic-management | Стратегическая картина Jetix | Стратегические решения | Strategic writing + framing |
| manager | Операционное состояние | Проект / Сделка | Weekly review, grading |
| strategist | Метод работы над типом задачи | Стратегический документ | Стратегирование |
| sales-lead | Pipeline | Клиент (lead → closed) | MECE ICP segmentation |
| sales-research | Квалифицированный контакт | Prospect | ICP screening |
| sales-outreach | Distribution | Контент / сообщение | LinkedIn content |
| delivery | Клиентский результат | Deliverable | Productized delivery |
| analyst | Данные → инсайт | Анализ | MECE, hypothesis-driven |
| knowledge-synth | Cross-domain synthesis | Research note | Deep research |
| meta-agent | Cross-cutting QA | Audit findings | Policy check |
| inbox-processor | Information triage | Inbox items | Classification |
| crazy-agent | Disruption / creative | Creative output | Divergent thinking |
| personal-assistant | Productivity | Quick tasks | Fast execution |
| system-admin | Infrastructure | Infra health | DevOps |

**Важное уточнение — mega-corporation.** Не solo. Закладываем сейчас: human executors + C-level + divisions. Все через role-abstraction. Phase 1 (solo) → Phase 2 (team) → Phase 3 (mega-corp). 10x scale-up без rebuild.

**Разделение Life-OS / Jetix (nested hierarchy):** Life-OS = root (жизнь founder'а). Jetix = один из проектов Life-OS. Left-coach агент живёт в Life-OS, не в Jetix. Но *роль* «life-coach» существует и в Jetix (для будущих employees) — та же role-abstraction в разных scopes.

## Основной research-запрос

Проведи **глубокий академический research** по следующим темам. Каждая — обязательный раздел финального отчёта.

### Часть A — 5 примитивов ШСМ: deep-dive

Для каждого примитива — детальное academic explanation (а не блогерское).

#### A.1 Ролевая онтология Левенчука

- Origin в ШСМ / OMG Essence standard
- Формальное определение: что есть «роль» в системной инженерии
- Разделение: role vs person vs agent vs organizational unit
- Notation и formal models (если есть)
- Примеры в software engineering (Scrum roles, RACI, etc)
- Как Левенчук conceptualизует в «Системном мышлении» книге
- Critics: где ролевая онтология ломается

Источники: «Системное мышление 2020» Левенчук (книга), OMG Essence specification (semat.org), ШСМ курсы (system-school.ru), ailev.livejournal.com.

#### A.2 Альфы с состояниями

- OMG Essence Alpha concept detailed
- Что такое alpha vs entity vs object
- State machines для альф
- Standard alphas (Stakeholders, Requirements, Software System, Team, Way of Working, Work, Opportunity)
- Как Левенчук adaptирует Essence для non-software domains
- Примеры alphas в бизнес-контексте (клиент, сделка, счёт)

Источники: OMG Essence 1.2 specification (omg.org/spec/Essence), Semat Kernel и extensions, Pekka Abrahamsson et al. «Essence - Kernel and Language» book.

#### A.3 Граф создания

- Formal definition из ШСМ
- Difference from value stream / dependency graph / ownership map
- Mereology и holon концепты (связь с FPF)
- Visual notation
- Examples в organizational design
- Как Левенчук применяет в «Интеллект-стеке»

#### A.4 Стратегирование (strategizing)

- Определение Левенчука: метод выбора метода
- Difference from planning / strategy / tactic
- Когда применяется (перед началом нового типа работы)
- Formal model (если есть)
- Практика: как выглядит «стратегирование session» для конкретной задачи

#### A.5 Мышление письмом (thinking by writing)

- Левенчук на эту тему в «Образовании для образованных»
- Neuroscience research (Peter Naur «Programming as Theory Building» 1985, Gilbert Ryle exocortex, Andy Clark extended mind)
- Daily journaling best practices (Morning Pages, Bullet Journal, Cal Newport Deep Work)
- Corporate adaptation (Amazon 6-pager, Bezos memos)
- AI-augmented writing (Notion AI, Obsidian AI)

### Часть B — FPF (First Principles Framework) Левенчука: full explanation

1. Что такое FPF в разработке Левенчука. Timeline развития concept.

2. Как связан с интеллект-стеком (17 дисциплин).

3. Холоны и мереология — детальное explanation.

4. Как FPF является «протоколом для AI-агентов» (цитата из Левенчук 2024-2025 публикаций на ailev.livejournal.com).

5. Conference МИМ-2026 (Системные сборки и Онтологические сборки) — main insights, особенно про AI и узкое место во framing.

6. Critics: где FPF overkill, где mandatory.

7. Что из полной FPF подходит для **Jetix FPF-lite** (3-5 страниц):
   - Целевая система Jetix
   - Stakeholders
   - Граф создания (основные звенья)
   - Принципы работы с клиентами
   - Принципы работы internal (founder ↔ agents ↔ executors)
   - НЕ включать: holons hierarchy, 17 disciplines, full mereology

Источники: Левенчук statji на ailev.livejournal.com (2023-2026), видео лекции ШСМ. OMG Essence, Peter Naur «Programming as theory building», Andy Clark «Natural-Born Cyborgs».

### Часть C — Role-manifest format: спецификация для Jetix

Это practical часть, на выходе — **полный draft formal spec** для Jetix role-manifest files.

Consider что включить в role-manifest (обосновать каждое поле):

1. **Identity block:**
   - name (slug)
   - display-name
   - version (SemVer)
   - layer (L0-L7)

2. **Ontological block:**
   - target-system (целевая система роли)
   - primary-alpha (главная lifecycle-entity роль управляет)
   - secondary-alphas (второстепенные)
   - acceptance-criteria (когда считается что альфа успешно перешла состояние)

3. **Method block:**
   - method (какой метод применяется)
   - anti-methods (что НЕ использовать)
   - golden-examples (ссылки на 10 эталонных completed tasks)

4. **Graph-of-creation block:**
   - consumes-from (какие роли или sources предоставляют input)
   - produces-for (какие роли или external consumers получают output)
   - artefacts-produced (какие типы файлов создаются, куда, по каким templates)

5. **Seniority block:**
   - level (junior / mid / senior / staff / principal)
   - decision-rights (what можно решить без escalation)
   - escalation-trigger (когда эскалировать)

6. **Implementation block (для AI):**
   - current-executor (e.g. "claude-sonnet-4.6")
   - prompt-file (path to v1.md)
   - eval-dataset (path to golden dataset)
   - tools-allowed (list of MCP tools available)

7. **Implementation block (для human executors):**
   - hired-person (nullable)
   - onboarding-path
   - reporting-to
   - performance-kpis

8. **Evolution block:**
   - created-at
   - last-updated
   - historical-versions (git log reference)
   - expected-evolution (notes on future changes)

Format: YAML frontmatter + Markdown body? Или pure YAML? Или dual (manifest.yaml + system.md)?

Examples из existing practice: как GitLab handbook описывает roles, как Holacracy Constitution, как Essence standard.

### Часть D — Alpha set для Jetix: полная спецификация

Составь **complete alpha set** для Jetix бизнеса с lifecycle states.

Обязательные альфы (based on synthesis):

1. **Клиент (Client)** — lead → qualified → proposed → negotiating → closed-won / closed-lost → churned
2. **Проект (Project)** — scoped → kicked-off → in-progress → delivery → closed → follow-up
3. **Сделка / Контракт (Deal/Contract)** — draft → signed → active → completed / cancelled
4. **Счёт (Invoice)** — issued → sent → paid → reconciled / disputed
5. **Content Item** — draft → in-review → approved → published → retired
6. **Hypothesis** — formulated → active → validating → validated / invalidated → implemented
7. **SKU / Product** — idea → prototype → launched → active → deprecated
8. **Member (Alliance / Club)** — applied → invited → active → at-risk → churned
9. **Research note** — started → draft → completed → integrated into wiki
10. **Postmortem** — incident → draft → reviewed → action-items → closed

Для каждой альфы:
- Complete state diagram
- Valid transitions (не только forward, иногда backward)
- Который агент / роль отвечает за каждый transition
- Artefact template для каждого state (e.g., Deal state "draft" = draft-contract template T-XX)
- Events (what happens on transition)

Это **core operational ontology Jetix**. Больше альф может быть, но эти 10 — обязательные.

### Часть E — Ritual design (стратегирование, writing to think)

1. **Стратегирование ritual для Jetix:**
   - Когда применяется (before new project / new SKU / new role / major decision)
   - Format (1-page document in `strategizing/YYYY-MM-DD-<slug>.md`)
   - Structure: context → method alternatives → chosen method → why → expected outputs
   - Кто владеет (strategic-management role = Ruslan сейчас)
   - Integration с L7 Portfolio (strategizing output влияет на attention allocation)

2. **Thinking-by-writing rituals для Jetix:**
   - Daily log (`daily-log/YYYY-MM-DD.md`) — free-form morning / structured evening
   - Weekly review (`weekly/YYYY-Www.md`) — Shape Up-style
   - Monthly letter draft accumulation (for quarterly letter)
   - Quarterly letter (`letters/YYYY-Qn.md`) — published for self first, Alliance later

3. **How agents participate in writing rituals:**
   - Agent-generated draft vs human-written
   - Review cycles
   - When agent is author vs editor vs critic

### Часть F — AI-specific adaptation (что меняется vs Левенчук original)

Левенчук writes про human cognition. Что изменяется когда исполнитель AI:

1. **Agents don't have inner life** — no emotions, no tacit knowledge, no intuition. Everything must be explicit.

2. **Agents don't learn between sessions** (без retraining). Каждый session — с нуля кроме что в context.

3. **Context engineering замест prompt engineering** — per Левенчук 2024+. What this means concretely.

4. **Role-манифест как «мировоззрение» (FPF-like)** — не инструкция на задачу, а worldview.

5. **Meta-cognitive abilities** — people can stop and reflect; agents нужно явно включать reflection steps.

6. **Multiple agents на одной роли** (Claude + GPT-5 на одну роль для cross-check) — какой pattern.

7. **What translates 1:1** vs **what needs adaptation** vs **what needs invention** in Jetix context.

Источники: AI-agent research papers 2024-2026 (arxiv.org), Anthropic research on constitutional AI, Peter Naur revisited for AI context, ШСМ writings 2024-2026 на AI.

### Часть G — Mega-corporation scale adaptation

Левенчук writes for individual knowledge worker. How 5 primitives scale:

1. **Роли at scale 10 → 100 → 1000 executors:**
   - Как role-manifest разделяется когда scope слишком big
   - Multi-executor per role
   - Role inheritance (sub-role inherits from parent role)

2. **Альфы at scale:**
   - Hundreds of concurrent client alphas
   - Database vs file-based tracking
   - Automated state transition triggers

3. **Граф создания at mega-corp:**
   - Thousands of edges
   - Visualization challenges
   - Automated map maintenance

4. **Стратегирование at scale:**
   - Strategic decisions escalation to C-level
   - Delegation of strategizing к senior levels

5. **Writing rituals at scale:**
   - Quarterly letters as tradition (Berkshire Hathaway, Constellation Software)
   - All-hands documents
   - Decision records for multiple teams

### Часть H — Практические выходы для Jetix

**Самая важная часть.** Actionable выход, который становится input для чистовиков.

1. **FPF-lite Jetix (полный draft 3-5 страниц):**
   - Целевая система Jetix (1 параграф)
   - Stakeholders (список + описание каждого)
   - Граф создания (основные звенья)
   - Принципы работы с клиентами (5-7 bullets)
   - Принципы работы internal (founder ↔ agents ↔ executors)
   - Critical alphas (список 10)
   - Ritual cadence (daily / weekly / monthly / quarterly)

2. **Role-manifest template (полный YAML+markdown spec):**
   - With все fields из Части C
   - Example filled out for `sales-lead` role

3. **Стратегирование template:**
   - When to trigger
   - What sections
   - Example: стратегирование для «как запустить первый AI Audit»

4. **Метрика «качество framing»:**
   - Proposed metric (например: % задач completed с первого прогона без rework / % framing-errors in postmortems)
   - How to measure
   - Baseline / target

5. **Migration plan:**
   - Как перевести 12 существующих агентов в role-manifest format
   - Order (который первый)
   - Сколько времени на каждый

6. **Anti-patterns specific Jetix:**
   - Чего не делать при применении ШСМ (не утонуть в онтологии, не брать полный интеллект-стек)
   - Когда переход от FPF-lite к fuller FPF становится оправдан

## Format требования

- **Объём:** 5000-10000 слов
- **Format:** Markdown с явными частями A-H
- **Citations:** максимум первичных источников (книги Левенчука, Essence standard, peer-reviewed papers). URLs прямые.
- **Russian + English sources** — оба. Книги Левенчука на русском, academic papers на английском.
- **Tables** где релевантно (alpha states, role-manifest fields comparison)
- **Code blocks** для YAML examples, markdown templates
- **Actionable** — Part H должна быть really implementable

## Anti-patterns (чего НЕ делать)

- ❌ Поверхностный обзор — «роль это то что выполняют» без formal definition
- ❌ Не игнорировать OMG Essence (это основа alphas, не only Левенчук)
- ❌ Только русские источники или только английские — нужна обе сторона
- ❌ Без Part H (practical output для Jetix)
- ❌ Over-academize — не утонуть в Левенчук exegesis (helpful but not the goal)
- ❌ Ignoring mega-corp scale requirement (всё думаем с прицелом на 10x scale)

## Критерий успеха

Research считается успешным если на его основе я могу:
1. Написать `design/JETIX-FPF-LITE.md` (3-5 страниц финальная онтология)
2. Написать `design/JETIX-ROLE-MANIFESTS.md` (полная спецификация + template + 12 filled examples)
3. Написать `design/JETIX-ALPHA-SET.md` (10 core alphas with state machines)
4. Запустить стратегирование ritual для first real Jetix task
5. Определить и начать измерять метрику «качество framing»

Приступай. Работай тщательно, academically, cite everything. Не поверхностно.

=== PROMPT END ===

---

## Notes для Ruslan

**Время запуска:** 30-90 минут. Параллельно с R1 и R2 в отдельной вкладке.

**Источники для attention:**
- Книги Левенчука — должны быть upstream source
- ailev.livejournal.com — его блог, много свежих постов 2024-2026
- system-school.ru — ШСМ курсы
- OMG Essence specification (это источник alphas, важно)
- Peter Naur «Programming as Theory Building» — classic paper, цитируется Левенчуком

**Что делать если результат слабый:**
- Если Part H generic — «make Part H Jetix-specific with our actual 12 roles, not abstract»
- Если only book-summary без original research — «add Perplexity analysis of Левенчук 2024-2026 recent posts»
- Если no concrete role-manifest template — «provide full YAML spec + filled example»

**После получения файла:**
- Сохрани как `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md`
- На сервер
- После Wave 1 complete — synthesis + переход к Wave 2
