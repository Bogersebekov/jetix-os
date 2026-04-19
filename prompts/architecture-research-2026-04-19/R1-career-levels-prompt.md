---
research-id: R1
wave: 1
topic: Corporate career levels, делегирование, decision-rights на всех масштабах
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/career-levels-deep-research-2026-04-19.md
priority: P1 (критично — блокирует финализацию L0 Executive Core)
---

# R1 — Corporate career levels, делегирование, phase transitions

## Зачем этот research

Jetix проектируется как AI-native mega-corporation с scale-up-first design.
Сейчас 12 AI-ролей + Ruslan как strategic-management. В будущем: human
executors + C-level + divisions. Всё через единую **role-abstraction**
(роль-manifest — абстрактная спецификация, исполнитель-человек или AI
подтаскивается под роль).

Для финализации **L0 Executive Core** нужно академически понять:

- Как устроены уровни (junior → senior → staff → principal → C-level) в разных
  типах корпораций
- Как работают decision-rights на каждом уровне
- Как работает делегирование
- Как компании проходят **phase transitions** (solo → 5 → 50 → 500 people)
- Что меняется с появлением AI-агентов в структуре

Выход research'а — input для документа
`design/JETIX-CAREER-LEVELS.md` (финальный чистовик).

## Как использовать

Скопируй **всё между `=== PROMPT START ===` и `=== PROMPT END ===`** ниже и
вставь в Perplexity Max Computer. Запусти в собственной вкладке (не смешивай с
другими research'ами).

---

=== PROMPT START ===

Ты — senior research analyst. Я прошу тебя провести **глубокий академический research** по теме корпоративных уровней ролей, делегирования и phase transitions в организациях, с прямым практическим выходом на специфический use case — AI-native mega-corporation с одним основателем и 12+ AI-агентами, масштабируемая к team + C-level.

## Контекст проекта Jetix (2000 слов)

**Кто такой Jetix.** Jetix — операционная система для AI-native компании, построенная одним основателем (Ruslan, Берлин) с целью вырасти в крупную корпорацию. Текущий стек: GitHub monorepo, сервер Hetzner, центральный Claude Code (Anthropic Opus 4.7 1M context) выполняющий задачи через переключение system prompt между ролями. Уже есть: 557-страничная knowledge base (wiki/), 8 активных проектов, 15 canonical templates, voice-memos pipeline.

**Ключевой принцип — Jetix ≠ one-person company.** Хотя сейчас технически один человек + AI-агенты, архитектура закладывается **с Day 1 под mega-corporation**. Инструмент (Jetix OS) задумывается как система управления большой корпорацией, а не helper для solo-operator. Количество ролей (сейчас условно 12) — **переменная, не константа**: масштабируется до 30 / 100 / 200 по мере роста сложности цели.

**Три типа исполнителей работают через единую role-abstraction:**
1. **Ruslan** — strategic-management role (для начала). Judgment, framing, acceptance критических решений, внешние стратегические отношения. Сама по себе роль, не «надсистема».
2. **Claude Code AI-агенты** — сейчас условно 12 ролей, scale до сотен.
3. **Human executors** (future team) — sales people, project managers, C-level, ops. Будут подтаскиваться под абстрактные role-manifest'ы. Их задачи, описания, артефакты живут в той же git-системе что и для AI.

**Ключевой принцип:** **Роль ≠ исполнитель**. Role-manifest — абстрактная спецификация (целевая система, ключевая альфа-lifecycle-entity, метод, acceptance criteria). Исполнитель (человек или агент) подтаскивается под роль. **Люди = продолжение агентов, не отдельная категория.**

**Текущие 12 ролей (baseline для дальнейшего дизайна):**

| Роль | Текущий уровень | Целевая система | Главная альфа |
|------|---------|-----------------|---------------|
| strategic-management (Ruslan) | — | Стратегическая картина Jetix | Стратегические решения |
| manager | Staff | Операционное состояние Jetix | Проект / Сделка |
| strategist | Principal | Метод работы над типом задачи | Стратегический документ |
| sales-lead | Senior | Pipeline | Клиент (lead → closed) |
| sales-research | Junior | Квалифицированный контакт | Prospect |
| sales-outreach | Junior | Distribution | Контент / сообщение |
| delivery | Senior | Клиентский результат | Deliverable |
| analyst | Senior | Данные → инсайт | Анализ |
| knowledge-synth | Senior | Cross-domain synthesis | Research note |
| life-coach | Senior | Personal health / energy (живёт в Life-OS, не в Jetix) | Личная энергия |
| meta-agent | Staff | Cross-cutting QA | Audit findings |
| inbox-processor | Junior | Information triage | Inbox items |
| crazy-agent | Hackathon | Disruption / creative | Creative output |
| personal-assistant | Junior | Productivity | Quick tasks |
| system-admin | Mid | Инфраструктура | Infra health |

**Архитектура Jetix OS — 7 слоёв + L0 Core** (уже утверждено):
- L0 Executive Core: Ruslan + AI-агенты + future human team
- L1 Foundation: Git + CI/CD + Docs-as-code + prompt-as-code + SRE
- L2 Cognitive: Системное мышление Анатолия Левенчука / ШСМ
- L3 Product: Micro-SaaS, productized services, Jetix Club tiers
- L4 Delivery: Agency + Consulting hybrid (primary Q2 2026 revenue engine)
- L5 Membrane: Community (Alliance + Club + newsletter)
- L6 Topology: Platform (horizon 18-36 мес)
- L7 Portfolio: Holding discipline (attention + capital + hours allocation)

**Target market:** Немецкий Mittelstand (manufacturing / services 50-500 сотрудников, €10-500M revenue). Цель Q2 2026: €50K revenue до 30.06.2026. Сейчас 0 клиентов, 0 revenue.

**Типы ресурсов для allocation (ключевой концепт):** в отличие от инвесторов (Buffett/Leonard распределяют только капитал), Jetix L7 отслеживает **три ресурса одновременно**: капитал + часы + внимание. Эволюция scope: Phase 1 (solo — свои ресурсы) → Phase 2 (team — свои + team ресурсы) → Phase 3 (mega-corp — full portfolio управления). Дополнительно Jetix **orchestrates ресурсы экосистемы** (внимание клиентов, время партнёров, капитал ecosystem-участников) — это уникальное competitive advantage.

**Ключевое требование к архитектуре:** Scale-up-first design. При **10x росте** (капитала / часов / людей / проектов / ролей) система должна справиться **без rebuild**, только расширением scope. Это не опция, это обязательное требование к дизайну.

**Что нам нужно от этого research:** академически понять career levels и orgdesign patterns во всех релевантных индустриях, чтобы построить role-manifest framework и career ladder для Jetix, который работает на всех phase transitions.

## Основной research-запрос

Проведи **глубокий академический research** по следующим темам. Каждая тема — обязательный раздел в финальном отчёте.

### Часть A — Career ladders в software industry (FAANG + startups + mid-size)

1. **Полный IC-track:** junior → mid → senior → staff → principal → distinguished engineer / fellow. Для каждого уровня детально опиши:
   - Scope работы (task-level / feature-level / multi-team / org-wide / industry-wide)
   - Decision-rights (что может решить без escalation)
   - Impact ожидания (per quarter / per year)
   - Time-in-role baseline (сколько обычно сидят на уровне)
   - Что отличает от следующего уровня
   - Concrete examples из Google, Meta, Amazon, Netflix, Microsoft

2. **Management track:** tech lead → engineering manager → director → VP engineering → CTO. То же самое как для IC.

3. **Dual-ladder companies (IC ↔ management)** — как работает переход, сохранение compensation, когда выбирают track. Примеры.

4. **Specialist tracks** (SRE, security, ML, data) — чем отличаются от generic SWE ladder. Где senior SRE vs senior SWE по impact.

5. **Startup-specific** — как ladder отличается у early-stage startup (10-50 человек) от mature org. Why founder-led titles misleading.

Источники для раздела A: Will Larson «Staff Engineer» (2021) и «Elegant Puzzle», Camille Fournier «The Manager's Path» (2017), Michael Lopp (Rands in Repose) articles, levels.fyi data, Tanya Reilly «The Staff Engineer's Path» (2022). HBR articles on software org design. Google SRE book for engineering ladder examples.

### Часть B — Consulting ladders (MBB) + German Mittelstand patterns

1. **MBB ladder:** Business Analyst / Associate → Consultant → Engagement Manager → Associate Principal → Principal → Partner → Senior Partner. Time-in-role. Utilization rates. Billing rates. Up-or-out policy. Decision-rights. Impact expectations.

2. **Big4 ladder** (Deloitte / PwC / EY / KPMG) — отличия от MBB.

3. **Boutique consulting** (Roland Berger в Германии, Simon-Kucher) — specifics.

4. **German Mittelstand hierarchy:** Geselle → Meister → Teamleiter → Abteilungsleiter → Bereichsleiter → Geschäftsführer. Relatively flat org. Family-business patterns. Konsenskultur.

5. **IHK / VDMA / Handwerkskammer** — как Mittelstand структурирует internal roles. References, публикации.

Источники: Ethan Rasiel «The McKinsey Way» и «The McKinsey Mind», Marc Cosentino «Case in Point», Vault Guide to Consulting, McKinsey / BCG / Bain careers pages, Roland Berger publications. Fraunhofer Institute Mittelstand research. IHK publications on Führungsstrukturen im Mittelstand. VDMA reports on manufacturing organization.

### Часть C — C-level executive structure evolution

1. **Полный C-suite:** CEO / COO / CFO / CTO / CMO / CSO / CPO / CHRO / CDO / CIO / CCO — функциональные boundaries каждого. Для каждого:
   - Когда компания заводит (by company size / revenue / industry)
   - Main KPIs
   - Reporting structure (who reports to whom)
   - Overlap areas with other C-levels

2. **C-level timing** — в какой момент growth (10 ppl / 50 / 200 / 500 / 1000+) каждая позиция появляется. Исследования на этот счёт.

3. **Founder → CEO transition** — когда founder выходит из CEO role, nанимает professional CEO. Примеры (Google: Page→Schmidt→Pichai, Airbnb: Chesky остаётся). Research на founder-mode vs manager-mode.

4. **Chief of Staff role** — что это, когда нужен, обязанности. Как используется в мега-корпорациях и startups.

5. **Fractional C-level** — модель (Part-time CFO / CMO / COO). Когда применяется. Как работает.

Источники: Ben Horowitz «The Hard Thing About Hard Things» (2014), Keith Rabois «Founder-led sales», a16z Executive Briefing, Harvard Business Review articles on C-suite, The Board Member's Guide by NACD, TheCFOAcademy resources. Paul Graham essays on founder mode (2024).

### Часть D — Decision-rights frameworks

1. **RACI matrix** — Responsible / Accountable / Consulted / Informed. Как применяется. Когда ломается.

2. **Bezos 2-way vs 1-way doors** — reversible vs irreversible decisions. Как escalation rules строятся вокруг этого.

3. **DARE framework** (Decide / Agree / Recommend / Endorse / perform-work).

4. **Intel / Grove approach** — Andy Grove's High Output Management decision types.

5. **Stripe / Patrick Collison approach** к decision-rights (public info).

6. **Holacracy circles** — как decision-rights распределены в Holacracy-based org.

7. **Escalation paths** — паттерны когда задача поднимается вверх по ladder. Anti-pattern: everything escalates.

Источники: Andrew Grove «High Output Management» (1983), Keith Rabois / a16z Executive School, Amazon shareholder letters (Bezos на 2-way doors), Holacracy Constitution (holacracy.org/constitution). Stripe blog on org design. Paul Graham «Founder Mode» (2024).

### Часть E — Делегирование patterns

1. **Basic delegation framework** — Stephen Covey 6 levels of delegation. Practical examples.

2. **Jeff Bezos «Singular focus» / «Two-pizza teams»** — как ограничение размера команды меняет delegation.

3. **Spotify squad model** — squads / tribes / chapters / guilds. Как делегирование работает в matrix structure.

4. **Autonomy-Alignment matrix** (Henrik Kniberg / Spotify) — почему autonomy без alignment ведёт к хаосу.

5. **Scaled delegation patterns** — как корпорации на 10,000+ человек решают problem of knowing. Gartner research, McKinsey research.

6. **Mission Command** (military delegation philosophy, based on Prussian model) — adopted by Amazon и others. Как apply в non-military org.

7. **Micromanagement anti-patterns** — classic research. Why managers over-delegate vs under-delegate.

Источники: Covey «7 Habits of Highly Effective People», Fred Kofman «Conscious Business», McKinsey Quarterly on delegation (multiple articles), The Economist articles on Mission Command. Prussian military history references for original Auftragstaktik.

### Часть F — AI-augmentation of career ladders

1. **Как AI меняет junior work.** Research 2023-2026: survey на изменение scope junior-developer роли. Stack Overflow 2024 Developer Survey. GitHub Copilot impact studies.

2. **Что остаётся человеку.** Academic research на AI complementarity. McKinsey Global Institute reports 2024-2025. MIT / Stanford research on AI-human teams.

3. **AI-native companies** — публичные примеры структуры:
   - Anthropic (blog posts, research)
   - Cursor (по blog interviews team)
   - Lovable (по Y Combinator interviews)
   - OpenAI internal team descriptions (public info)
   - Replicate (blog)
   - DeepSeek (industry reports)

4. **Hybrid human+AI org patterns** — research 2024-2026 на how companies structure teams where AI does majority of work.

5. **Career paths transformation** — что значит быть «senior» когда AI делает большую часть execution. Как меняется compensation.

6. **AI как «teammate» vs «tool»** — academic discussion 2023-2025.

Источники: Erik Brynjolfsson et al. на Stanford HAI, McKinsey Global Institute «The State of AI 2024», Sequoia Capital analysis, Anthropic blog (anthropic.com/research), Patrick Collison interviews on AI org design. MIT Sloan Management Review articles 2024-2025.

### Часть G — Практическая рекомендация для Jetix

**Это самая важная часть.** Подвяжи весь предыдущий research к конкретному Jetix-контексту и дай actionable рекомендации:

1. **Финальный career ladder Jetix** — уровни, переходы, time-in-role, decision-rights. Mapping текущих 12 ролей + future team + C-level slots на полный ladder.

2. **Role-manifest format recommendation** — что должно быть в role-manifest файле (формат .md или .yaml). Minimum viable fields + optional extensions. Examples из consulting / software / mega-corp.

3. **Decision-rights matrix** — таблица: какой уровень какие decisions может делать без escalation. Apply к Jetix-specific decisions (accept client, fire client, change price, launch new SKU, hire, fire и т.д.).

4. **Phase transitions roadmap** — когда Jetix (growing) должен:
   - Добавить первого human hire (какую роль, при каких метриках)
   - Добавить C-level (какого, когда)
   - Разделить Ruslan strategic-management role (когда, на что)
   - Добавить divisions (по каким критериям)

5. **Escalation protocol Jetix** — signals когда задача должна подняться вверх. Anti-patterns чего избегать.

6. **Human-AI boundary recommendations** — что делает AI, что человек, как переопределяется с релизом новых моделей. Где единственный точный ответ «точно человек» vs «точно AI» vs «зависит».

7. **10-year view** — как Jetix org выглядит в 2035 если всё идёт по плану. Гипотетическая структура.

## Format требования

- **Объём:** 5000-10000 слов (академическая глубина, не поверхностный обзор)
- **Format:** Markdown с явными частями A-G
- **Citations:** каждый ключевой факт с прямой ссылкой на источник. Предпочтительно — прямые URL на оригинальные материалы (книга, paper, blog post, conference talk). Inline format `[автор год](url)` или `[title](url)`.
- **Tables** где релевантно (например, comparison ladders между индустриями)
- **Honest about uncertainty** — где данных нет или противоречия, явно указать «мало данных» или «противоречивые results in literature», не fabricate
- **Non-generic** — не «senior отличается от junior большим опытом», а конкретные обязанности / decisions / KPI
- **Actionable for Jetix** — Part G должна быть действительно практичная для solo-founder + 12+ AI-agents вырастающего в mega-corp

## Anti-patterns (чего НЕ делать)

- ❌ Поверхностный обзор без citations
- ❌ Только одна индустрия (только software) — нужен cross-industry view
- ❌ Без Part G — without practical recommendations research бесполезен
- ❌ Копипаст из один ChatGPT-like source — нужны primary sources
- ❌ Игнор специфики Jetix (solo + AI + scale-up-first)
- ❌ Игнор German Mittelstand specifics (это наш target market)

## Критерий успеха

Research считается успешным если на его основе я могу:
1. Написать `design/JETIX-CAREER-LEVELS.md` (финальный чистовик для репозитория)
2. Создать role-manifest template
3. Построить decision-rights matrix для Jetix current state
4. Зафиксировать phase transition triggers для scale-up

Вперёд. Приступай к research. Работай тщательно, академично, цитируй всё. Не торопись.

=== PROMPT END ===

---

## Notes для Ruslan

**Время запуска:** ожидай 30-90 минут работы Computer. Можно поставить и идти делать R2 в параллельной вкладке.

**Что делать если результат слабый:**
- Если citations недостаточно — запроси follow-up с «expand citations, add more primary sources»
- Если Part G слишком generic — запроси «make Part G more Jetix-specific, use our context»
- Если не хватает German Mittelstand — запроси отдельный follow-up только на эту часть

**После получения файла:**
- Сохрани как `raw/research/career-levels-deep-research-2026-04-19.md`
- На сервер через `scp` или GitHub commit
- Сообщи Claude Code — начнём синтез после Wave 1 complete
