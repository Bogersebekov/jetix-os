---
title: "MetaPlan V4 — Direction #16: Хакатоны / Соревнования / Экспедиции (портфельный спек)"
date: 2026-05-26
type: phase-report-metaplan-v4
phase: 17
direction: 16
F: F2-F3
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
language: russian
status: draft-report
prose_authored_by: brigadier-scribe (R1 surface — Ruslan authors final integration)
constitutional_posture: R1 surface only + R2 STRICT + R11 + R12 paired-frame STRICT AUTO-FIRE + IP-1 STRICT
auto_paired:
  - influence-ethics-expert (R12 AUTO-FIRE — revenue events)
  - recruitment-dynamics-expert (R12 AUTO-FIRE — event onboarding funnel)
predecessors:
  - decisions/strategic/JETIX-AS-HACKATHON-PLATFORM-2026-05-18.md (primary substrate — operational concept)
  - decisions/strategic/JETIX-WORKSHOP-MASTERY-NETWORK-CONCEPT-2026-05-26.md
  - decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-V2-2026-05-25.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md
  - research/hackathon-deep-2026-05-18/ (5 research phases)
  - swarm/wiki/foundations/principles/architecture.md
r12_notice: Revenue events — Mondragón 5:1 cap + QF distribution + fork-and-leave + sponsorship transparency + no anti-competitive practices
---

# Direction #16 — Хакатоны / Соревнования / Экспедиции: портфельный спек (V4)

## Введение: грань Events и что это направление

Jetix — мега-мастерская мирового уровня. Три грани Foundation: **Мастерская** (ГДЕ — пространство, 8 зон, инфраструктура) · **Мастерство** (ЧТО прокачивают) · **Сеть** (КАК распределено — mesh cells, pooling). Direction #16 «Хакатоны / Соревнования / Экспедиции» — это **грань Events**: Мастерская приводится в движение. Workshop = static substrate; хакатон = operational pattern. Events = **revenue engine + community engine одновременно**.

Одна строка (R1 surface): «Jetix-события — то, где Мастерская оживает: люди приходят незнакомцами, уходят участниками проектов, система зарабатывает, community растёт, R12 сохраняется».

Почему это направление критично. Все остальные Direction'ы описывают потенциал: метод, платформа, видение, правила. Events = актуализация потенциала. Без событий Мастерская — красивая концепция. С событиями — есть участники, есть revenue, есть кейсы, есть рост. «Люди сами будут создавать хакатоны, искать исследования, решать задачи, ездить на экскурсии — всё через Jetix» [src: Ruslan voice 26.05]. Это не один продукт — обширный слой.

**Связи в V4 архитектуре:**
- **#12 Мастерская** — Events = activation mode пространства. За 2 часа незнакомцы становятся командой с проектом [src: text_009 ¶1-2].
- **#13 Мастерство** — Events = delivery vehicle для deliberate practice (хакатон как форсированный apprenticeship — tacit knowledge transfer ускорен).
- **#14 Сеть (Кланы)** — Clan-wars = хакатоны различных ритмов [src: text_009 ¶10]. Соревнования = операционная идентичность клановой системы.
- **#15 Геймификация** — Events = пик engagement-петли. Skill tree visuaization; participation points; leaderboard per event. R12-HIGHEST: meaningful progression, не addictive loop.
- **#8 R12** — Revenue events = зона наивысшего R12-риска. QF distribution + Mondragón 5:1 + fork-and-leave = constitutional baseline для каждого события.

**Sub-areas направления:**
1. Хакатоны (24–72h research-and-build; paid entry + sponsored prizes)
2. Соревнования (между кланами / cohorts / mastery-comparable по темам и уровням)
3. Экспедиции (small group travel — погрузиться в одну нишу глубоко)
4. Research challenges (задача → кланы/индивиды решают → Jetix монетизирует через sponsorship/IP/talent placement)
5. Экскурсии / поездки в города (движение network-участников)
6. Retreats (community bonding, восстановление)
7. Public talks / conferences (visibility + recruitment + revenue)

**Multi-rhythm matrix:**

| Ритм | Длительность | Сложность проекта | Аудитория |
|---|---|---|---|
| День | 1 день | Низкая–средняя (чётко скопированная задача) | Блогеры + general |
| Месяц | 1 месяц | Средняя (спонсорские проекты, интегрированные системы) | Инженеры + партнёры |
| Год | 1 год | Высокая (крупные коллаборации, Master Workshop apprenticeship) | L1-инженеры + Мастера |

GAP статус: create — события ещё не запущены (Q3 2026 target per §7 Activation Gantt). Первый event = day-rhythm, bloggers+sponsor mode, ≤90 дней от ack концепт-документа [src: HP-T1]. R12 paired-frame: авто-пара influence-ethics + recruitment-dynamics fires на каждое revenue event.

> **R1:** все формулировки ниже — варианты/опции. Финальные решения за Ruslan.
> **R11 STRICT:** ниже — спецификации ЧЕГО содержит каждый документ, не сам публичный текст. Цифры — сценарные.
> **IP-1 STRICT:** имена ролей = role-type примеры (T-организатор, T-участник, T-ментор, T-спонсор и т.д.), не конкретные люди.
> **R12 paired-frame STRICT AUTO-FIRE:** каждая секция с revenue / event payouts / onboarding funnel получает явный anti-pattern check.

---

## §A — Главный документ «Jetix как events-платформа»

**Что это:** 1-pager + long-form spec. Не лендинг — операционный документ, который определяет, что такое события в Jetix, как они устроены, какой revenue-модели следуют и как R12 сохраняется. Аудитория: T-участники + T-спонсоры + T-организаторы + сам Ruslan.

**Структура 1-pager (≤400 слов):**
- Заголовок + one-liner (R1 surface выше)
- 3 ключевых вопроса: Что такое Jetix-событие / Для кого / Зачем идти
- Multi-rhythm matrix (3 ряда: день/месяц/год)
- Чем НЕ является — 6 пунктов (не конференция с докладчиками и зрителями / не bootcamp с лекционной моделью / не «заплати побольше — получи больше» / не замкнутый клуб инсайдеров / не engagement-trap / не pay-to-play exclusion)
- Как участвовать (entry point: первое событие → первый проект)

**Структура long-form spec (≤3K слов, 7 разделов):**

1. **Почему события — не «дополнение» к платформе.** Events = первичный revenue- и community-engine одновременно. Workshop (статический) без events = потенциал без реализации. Два аспекта ценности: «решить свои проблемы» (практический результат) + «куча возможностей» (network, роли, ментор-связи) [src: text_008 ¶1]. Connectivity speed claim: «за 2 часа в лица в проекты» [src: text_009 ¶1-2]. Precedents: Devpost (~1M users) = project artefact platform; MLH = sponsor-mentor-participant triangle; Kaggle = quality predicate drives participant ROI; YC Hackathons = batch cohort + demo event; g0v/Audrey Tang = civic-tech QF governance.

2. **Event orchestration cycle (A.16 Work-as-process per FPF).** Пять шагов:
   - **Initiate** — спонсор commit + проект surfaced + strategy file shared. Условие входа: sponsor ≥ baseline pool per event type; R12-compliance check before launch.
   - **Match** — участники + менторы + инструменты assigned via FPF protocol. «Прошаренные / крутые first» cohort 1; bloggers + general cohort 2. Matching = ROY swarm routing + человеческий gate.
   - **Solve** — marathon с continuous mentor pairing (TPS pattern). Длительность per ритм-матрице. Deliverable = работающий артефакт, не презентация.
   - **Reward** — QF distribution (Tang+Weyl mechanism; Ethereum substrate acked commit `8a3d800`). Mondragón 5:1 cap на event payouts. Sponsorship pool = transparent per event.
   - **Recurse** — winners feedback к platform improvement. Retention loop: участники следующего события = предыдущие winners + referrals. Target retention Year-1 ≥ 60% [src: HP-T3].

3. **Multi-rhythm экономика (сценарные цифры — не прогнозы).** Day-rhythm: sponsored prize pool + paid entry. Month-rhythm: sponsor project с IP-1 compliance; вознаграждение per QF. Year-rhythm: apprenticeship contract + sponsor grant. Revenue target = scenario (HP-T2: ≥ $30K per event в первые 3 события — falsifiable threshold, not projection). Coordination cost test: HP-T5 sub-linear (≤1.5× at 100 vs 10 participants).

4. **Activation Gantt (Ruslan picks operator semantics).** Q3 2026: first day-rhythm hackathon (bloggers+sponsor mode, Aug–Sep). Q4 2026: second+third day-rhythm + first month-rhythm. 2027+: 10→100→1000→100k participant ramp. «Снежный ком» per text_009 Thread 12: Stage 1 (10 «прошаренных/крутых») → Stage 2 (100, bloggers+sponsor) → Stage 3 (1000, engineers+Workshop) → Stage 4 (100,000, mass audience).

5. **Sub-areas taxonomy.** Семь sub-areas перечислены выше. Операционный приоритет Year-1: хакатоны (day + month rhythm) → research challenges → retreats → экскурсии/поездки. Экспедиции + conferences = Year 2+ при подтверждённой Run-петле.

6. **Чем Events-платформа отличается от конкурентов.** Devpost = project showcase без community engine. MLH = student-only, нет multi-domain. Kaggle = ML-only, нет cross-discipline. YC = equity-based model. Jetix = multi-domain + multi-rhythm + R12 baseline + FPF lingua franca + Workshop substrate + QF prize distribution. Differentiation per HP-T1..T5: empirically testable, не только marketing claims.

7. **R12 events baseline.** Mondragón 5:1 wage ratio на event payouts. QF prize pool distribution per Tang+Weyl. Fork-and-leave: участник выходит из event без штрафа, без «оставить задаток». Sponsorship pool = публично раскрыт до события. Anti-competitive между кланами: нет sabotage patterns; соревнование = developing, не extractive. Полный paired-frame — §J ниже.

---

## §B — Видео: hook + scenes + closing

**Что это:** короткий формат (90–180 сек) для первичного привлечения участников + спонсоров. Не рекламный ролик — demonstration of live event (founder-as-resident-master принцип: показываем работающее, не обещаем будущее).

**Структура (спек — не скрипт):**

**Hook (0–10 сек).** Контраст: «Обычная конференция — ты слушаешь. Jetix-хакатон — ты решаешь». Или: визуальный стоп-кадр момента "команда собирается за задачей за первые 2 часа". Вопрос к зрителю задаётся через действие, не риторику.

**Scenes (10–140 сек, 5 сцен):**
1. Initiate — sponsor + project arrival. Момент, когда реальная задача появляется в системе (screencast или narrative).
2. Match — как за 30 минут подбираются команда + ментор + инструменты. FPF lingua franca в действии.
3. Solve — рабочая сцена. Люди работают, а не презентуют. Tacit knowledge transfer visible.
4. Reward — QF distribution moment. Прозрачность: вот пул, вот как он распределён. Mondragón 5:1 = не маркетинг, а факт.
5. Recurse — winner становится ментором следующего события. Community flywheel.

**Closing (140–180 сек).** One-liner + call-to-action конкретный (не «узнай больше», а «первое событие — [дата]; войти → [ссылка]»). R12 disclosure в closing: «QF distribution, fork-and-leave preserved — детали на странице события».

**GAP:** видео создаётся после первого реального события (есть что снимать). Placeholder = animated spec или текстовый storyboard.

---

## §C — Курс: «Как организовать Jetix-хакатон»

**Применимость:** HIGH. Цель — создать T1-организаторов, которые проводят события самостоятельно, соблюдая R12-baseline и FPF. Это масштабирующий механизм: Ruslan не bottleneck организации каждого события.

**Аудитория:** T-организаторы (кланы, спонсоры, партнёры) + Tier-2 community members которые хотят запустить своё событие в рамках Jetix-сети.

**Структура курса (6 модулей):**

**Модуль 1 — Зачем хакатон (а не лекция, не мастер-класс).** Hackathon vs. other formats: почему tacit knowledge transfer > explicit. Precedents: MLH sponsor-mentor-participant triangle; g0v civic model; Kaggle quality predicate. Ключевой вопрос: «Какую задачу ты хочешь решить с участниками?» — не «какой контент дать».

**Модуль 2 — Event orchestration cycle (практика).** Пять шагов Initiate→Match→Solve→Reward→Recurse с чек-листами. Каждый шаг = hands-on задание (не чтение). Deliverable: черновик плана конкретного события.

**Модуль 3 — Работа со спонсорами.** Как формулировать sponsor commitment. QF pool setup. R12-compliance check до launch. Sponsorship deck structure (→ §F шаблон). Anti-pattern: sponsor capture (когда sponsor диктует судейство → нарушение независимости QF).

**Модуль 4 — Matching mechanics.** Как работает participant+mentor matching через FPF. Роль T-организатора vs. ROY swarm routing. Human gate в matching: что автоматизировано, что остаётся за человеком.

**Модуль 5 — R12 baseline для организатора.** Mondragón 5:1 практически. Fork-and-leave: как объяснить участникам, как технически реализовать. QF distribution: как считать, как раскрывать. Anti-competitive rules между командами/кланами. Checkpoint: пройти paired-frame §J перед каждым событием.

**Модуль 6 — После события: recurse loop.** Feedback collection. Winner→mentor pipeline. Как событие улучшает платформу. Retention mechanics (не FOMO-driven — opt-in reminder, не «ты пропустишь», а «следующее событие — вот что будет»).

**Формат:** асинхронный + live Q&A с T-организатором-ветераном (первые организаторы = выпускники первых событий). IP-1: курс не привязан к конкретному ментору — role-type примеры.

---

## §D — Книга

**Применимость:** DEFER → Year 2+. Книга об events-платформе требует прецедентов: реальные события, реальные кейсы, измеренные гипотезы HP-T1..T5. Year 1 = собрать substrate. Year 2 = написать по факту, не по плану.

**Рабочий тезис для будущей книги (R1 surface):** «Как события становятся основным двигателем community и revenue одновременно — опыт построения Jetix events-платформы с нуля до [N] событий». Не «теория хакатонов» — practitioners account.

**Контент-якоря для накопления:**
- Каждое реальное событие = глава-кейс
- HP-T1..T5 результаты = empirical backbone
- QF distribution примеры = financials section
- R12-violations и как они были предотвращены = cautionary examples (честно, не PR)

---

## §E — Инструкции / SOP

**Что это:** набор операционных документов для проведения каждого типа события. Не маркетинг — внутренние инструкции. Аудитория: T-организаторы + ROY swarm (для автоматизируемых частей).

**Документ E1 — Hackathon Hosting Guide (Day-rhythm).** Разделы:
- Pre-event (7 дней): sponsor confirmation + QF pool setup + R12-compliance check + participant outreach (not FOMO) + tool preparation
- Event day: Initiate (0h, sponsor briefing + task sharing) → Match (0–2h, team formation + mentor pairing) → Solve (2–22h, working sessions) → Reward (22–24h, QF distribution + public disclosure)
- Post-event (48ч): feedback forms + recurse loop trigger + retention outreach (opt-in)
- Checklist per шаг: человек-gate vs. automated step marker

**Документ E2 — Hackathon Hosting Guide (Month-rhythm).** Отличия от Day: extended sponsor project (IP-1 compliance — кто владеет результатом); weekly check-in structure; mid-event mentor rotation; QF pool = staged payout (не единовременно).

**Документ E3 — Expedition Planning SOP.** Small group (5–15 человек) travel. Критерии маршрута: ниша для глубокого изучения + local community connection + доступность для участников. Структура: Pre-expedition brief (1 неделя) → Travel (3–7 дней с daily learning sessions) → Post-expedition synthesis (collective artifact). R12: expedition cost = участники платят напрямую (no margin extraction by Jetix); Jetix revenue = curation fee disclosed + optional sponsor.

**Документ E4 — Inter-Clan Competition Rules.** Competitive frame без anti-competitive sabotage. Правила: равный доступ к ресурсам (tools, mentors, info) на старте; no intel leakage между командами; judge independence от sponsor; QF scoring = community-weighted (не жюри из одного человека). Fork-and-leave clause: клан или участник может выйти mid-competition без penalty (получает partial QF credit за выполненную работу).

**Документ E5 — Public Talk / Conference SOP.** Format: Jetix-talk = not «speaker performs for audience» но «speaker works with audience». Structure: 40% presentation + 40% working session + 20% Q&A. Revenue model: ticket + sponsor table + recording rights. R12: speaker compensation disclosed; no pay-to-speak.

**Документ E6 — Decision trees.** Дерево: «Какой формат выбрать для этой задачи?» → хакатон / соревнование / экспедиция / конференция. Входные переменные: сложность задачи + размер аудитории + revenue target + timeline. Anti-pattern trees: FOMO-marketing → redirect to opt-in narrative; sponsor capture attempt → escalate to R12 gate; participant lock-in attempt → fork-and-leave reminder.

---

## §F — Шаблоны / Templates

**F1 — Event Playbook Template.** Универсальный шаблон для любого события. Секции: Event type / Rhythm / Task definition / Sponsor commitments / QF pool setup / Participant criteria / Mentor roster / Tool stack / Schedule / Reward schema / Recurse plan / R12-compliance checklist. Frontmatter YAML с полями: event_id, rhythm, sponsor, qf_pool_size, r12_check: boolean.

**F2 — Expedition Planning Template.** Секции: Destination + rationale (niche + local connection) / Participant list + roles / Daily schedule template / Learning objectives (not tourist checklist) / Collective artifact spec / Cost breakdown (disclosed) / Jetix curation fee disclosure / Post-expedition publication plan.

**F3 — Inter-Clan Competition Rules Template.** Sections: Task definition / Teams (clan IDs) / Resource parity checklist / Judge independence declaration / QF scoring schema / Fork-and-leave clause (verbatim) / Anti-competitive prohibited actions list / Dispute resolution path.

**F4 — Sponsorship Deck Template (8 слайдов).** 1. Event overview + task 2. Participant profile (role-types, not personal data) 3. Sponsor value proposition (visibility + talent pool + IP placement per IP-1) 4. QF pool structure + Mondragón 5:1 disclosure 5. Timeline 6. R12-compliance statement (sponsor cannot influence judging) 7. Past precedents / comparable events 8. Call to action + terms. R12 note: sponsor deck не обещает эксклюзивных прав на participants; talent placement = opt-in only.

**F5 — QF Distribution Schema.** Tabular: Contributor ID (анонимизированный) / Contribution score / Community vote count / QF weight / Payout amount. Mandatory fields: total_pool, mondragon_cap_ratio (≤5:1), fork_and_leave_reserve (% of pool held for partial exits), public_disclosure_date. Format: JSON + human-readable Markdown summary.

**F6 — Post-Event Retrospective Template.** Sections: What worked / What broke / HP-T1..T5 measurement (per event) / Recurse actions / R12-violations detected (честно) / Next event draft.

---

## §G — Презентация (10–20 слайдов)

**Цель:** events = revenue+community engine; multi-rhythm. Аудитория двойная: потенциальные участники + потенциальные спонсоры (разные версии акцентов, одна база).

**Структура (15 слайдов):**

1. **Title.** «Jetix Events: Revenue Engine + Community Engine». One-liner.
2. **Проблема.** Конференции = пассивное слушание. Bootcamps = лекционная модель. Hack events без community = высокий churn. Нет платформы с R12 baseline.
3. **Решение.** Workshop (статический substrate) + Events (operational pattern) = Мастерская в движении. Multi-rhythm: day/month/year.
4. **Event orchestration cycle.** 5 шагов: Initiate→Match→Solve→Reward(QF)→Recurse. Визуально (кольцо или flow-диаграмма).
5. **Multi-rhythm matrix.** Таблица 3×4 (ритм / длительность / сложность / аудитория).
6. **Sub-areas taxonomy.** 7 типов событий. Year-1 фокус = хакатоны + research challenges.
7. **Revenue model (сценарный).** QF pool + paid entry + sponsorship. Mondragón 5:1. Не projection — scenario. HP-T2 как falsifiable threshold.
8. **R12 baseline.** 4 правила: 5:1 cap / QF distribution / fork-and-leave / sponsorship transparency. Slide = commitment, не fine print.
9. **Participant journey.** Visitor → Hackathon participant → Winner → Mentor → Organizer. Progression = opt-in, не forced.
10. **Precedents.** Devpost / MLH / Kaggle / g0v. Differentiators: multi-domain + multi-rhythm + R12 + FPF + Workshop substrate.
11. **Activation Gantt (Year 1).** Q3–Q4 2026: first 3 events. 2027+: ramp. Scenario targets.
12. **10→100→1000→100k.** Стадийный рост. Stage 1: «прошаренные/крутые». Stage 4: mass audience. Scenario, not projection.
13. **For sponsors.** Value prop: visibility + talent access + IP placement (opt-in) + R12-compliance = no reputational risk. Sponsor cannot capture judging.
14. **Anti-patterns мы избегаем.** Pay-to-play exclusion / FOMO-driven marketing / sponsor capture / competitive sabotage / fork-prevention. R12 paired-frame enforcement.
15. **Call to action.** Ближайшее событие: [дата Q3 2026]. Join → Sponsor → Organize. Contact.

---

## §H — FAQ (10–30 вопросов)

**Q1. Сколько стоит участие?**
A. Зависит от формата и ритма. Day-rhythm: входной взнос покрывает организационные расходы (размер = disclosed до регистрации). Month/year-rhythm: может быть бесплатным для участников если sponsor pool покрывает. Точные суммы — на странице конкретного события. Нет скрытых платежей.

**Q2. Как распределяются призы?**
A. QF distribution (quadratic funding по Tang+Weyl механизму): взносы community взвешиваются квадратично, что балансирует влияние крупных и малых доноров. Монопольное жюри из одного человека = не применяется. QF schema публикуется до события. Mondragón 5:1 cap: максимальный payout одному участнику ≤ 5× минимального. Детали — §F5 шаблон.

**Q3. Что если я уйду с хакатона до конца?**
A. Fork-and-leave preserved. Можно выйти без штрафа. Если выполненная работа оформлена как artefact — получаешь partial QF credit пропорционально вкладу. Нет «заплатить депозит и потерять».

**Q4. Кто спонсор и что он получает?**
A. Спонсор раскрывается публично до события. Получает: visibility + доступ к talent pool (opt-in only от участников) + IP placement per IP-1 (конкретные условия в договоре, disclosed). Не получает: право влиять на судейство, эксклюзивный доступ к участникам, возможность блокировать fork-and-leave.

**Q5. Могу я организовать своё событие через Jetix?**
A. Да. Tier-1 организаторы проходят курс §C. Клан может организовать свой хакатон (§L). Jetix предоставляет: FPF lingua franca + ROY swarm routing + QF distribution infrastructure + R12-compliance checklist. Jetix не является co-organizer по умолчанию — поддерживающая платформа.

**Q6. Что если два клана конкурируют — это честно?**
A. Правила inter-clan competition = §E4 (resource parity checklist + judge independence + no intel leakage). Клан выйти из соревнования может в любой момент (fork-and-leave). Competitive sabotage = нарушение правил платформы, дисквалификация.

**Q7. Что такое «экспедиция» и чем отличается от туристической поездки?**
A. Экспедиция = small group (5–15 человек), цель = глубокое изучение одной ниши через immersive experience (local community, practitioners, sites). Не tourist schedule. Collective learning artifact создаётся во время. Стоимость = участники платят напрямую за travel/accommodation; Jetix = curation fee (disclosed). Нет margin extraction без disclosure.

**Q8. Что такое «research challenge»?**
A. Конкретная исследовательская задача публикуется (от sponsor или Jetix). Кланы/индивиды решают в заданный срок. Monetization: Jetix получает за постановку задачи (sponsor pays) + talent placement fee (opt-in). IP на решение: определяется в условиях до старта (disclosed).

**Q9. Как работает matching участников и менторов?**
A. Частично автоматизировано через FPF protocol + ROY swarm routing. Человеческий gate: T-организатор подтверждает matching до фиксации. Mentor = opt-in роль, не обязательная. Matching criteria: skill alignment + project needs + mentor availability. Нет принудительного назначения.

**Q10. Есть ли иерархия «кто важнее»?**
A. Нет. Participant, mentor, sponsor = разные roles с разными responsibilities, не статусная иерархия. Progression (Visitor→Master) = opt-in, не обязательная карьера. Fork-and-leave применимо к любой роли.

**Q11. Как Jetix зарабатывает?**
A. Revenue streams: platform fee (% от QF pool, disclosed) + sponsorship origination fee + curation fee for expeditions + course enrollment (§C) + public talk ticket cut. Всё раскрывается до события. Mondragón 5:1 cap применяется к Jetix platform payouts тоже.

**Q12. Что происходит с IP, созданным на хакатоне?**
A. По умолчанию: IP = участники, создавшие артефакт. Если спонсор финансирует с условием IP transfer — это explicit в sponsor agreement, disclosed участникам до регистрации. Участник, не согласный с IP условиями, может не участвовать (fork-and-leave principle).

**Q13. Как R12 защищает меня как участника?**
A. R12 anti-extraction: Jetix не может извлекать ценность сверх agreed share (disclosed platform fee). 5:1 cap = у Jetix нет стимула забирать больше чем cap позволяет. Fork-and-leave = ты не заперт. QF = твой голос в распределении призов математически защищён от whale capture.

**Q14. Что если событие не соберёт участников?**
A. HP-T1 threshold: если первый хакатон не состоится в 90 дней после ack → operational-VAPOR signal (не катастрофа, но честный индикатор). Sponsor pool refunded по условиям договора. Участники уведомлены заранее. Нет «деньги не возвращаются».

**Q15. Можно ли участвовать удалённо?**
A. Year 1: primary remote-first (Workshop = виртуальный). Physical events = только при подтверждённой Run-петле (anti-WeWork принцип). Экспедиции = по определению physical. Remote participation для хакатонов = full support через Cloud Cowork + FPF + ROY swarm tools.

**Q16. Что такое «ритм» события и зачем три разных?**
A. Разные задачи требуют разных временных горизонтов. Day: чётко скопированные, быстро проверяемые гипотезы. Month: интегрированные системы, где нужно iteration + mentor feedback cycle. Year: deep apprenticeship, продуктовые разработки, research программы. Участник выбирает ритм по своим целям и доступному времени.

**Q17. Как стать ментором?**
A. Mentor = opt-in роль. Путь: участвовал в нескольких событиях → заявился как ментор → T-организатор approve (skill fit + commitment check). Ментор получает: visibility + community connection + potential QF mentor bonus (disclosed per event). Нет «купить роль ментора».

**Q18. Что если спонсор попытается повлиять на результаты?**
A. Sponsor independence clause = обязательная часть sponsor agreement (§F4 шаблон). При попытке влияния: T-организатор эскалирует per decision tree §E6. QF mechanism = математически защищён от sponsor override. Публичное раскрытие: если sponsor попытка зафиксирована → disclosure. Sponsor exit без event cancellation = возможна при обеспечении replacement pool.

**Q19. Проводятся ли события только по AI-тематике?**
A. Нет. Jetix = multi-domain по Workshop concept (8 зон). Хакатоны могут быть: AI + engineering + design + research + civic-tech + creative + methodology. Clan-wars = тематика per Clan Charter. Единственное требование к задаче: решаемая, falsifiable, meaningful.

**Q20. Как события связаны с прогрессией Мастерства?**
A. Каждое событие = точка в skill tree (#15 Геймификация). Participation point + artifact quality = milestone. Winner = значимый milestone, не исчерпывающий путь. Progression opt-in: можно участвовать без accumulation goal.

---

## §I — Worked Examples (3–5)

> **R11 STRICT:** примеры ниже — иллюстративные scenarios, не планы с конкретными числами. Цифры = сценарные.

**Example I1 — Первый bloggers+sponsor day-hackathon (Q3 2026, day-rhythm).**
Задача: T-спонсор (AI-инструмент компания) хочет community validation своего продукта. Jetix initiate: task definition «протестировать продукт на реальной задаче за 24 часа и предложить 3 улучшения». QF pool = [сценарный размер]. Participant cohort = bloggers + «прошаренные» first-event. Match: 5–10 команд × 3–5 человек + ментор pool 3 человека. Solve: 24h с 3 mentor check-ins. Reward: QF distribution публично. Recurse: 2 из 5 winning participants возвращаются как менторы на следующем событии. HP-T1 validated (event состоялся); HP-T2 measurement: сравниваем с $30K threshold; HP-T3 start: tracking retention.

**Example I2 — Cross-clan expedition (Year 2 scenario).**
Два клана с разными специализациями (пример: T-методологи + T-инженеры) едут на 5-дней expedition в город с сильной local tech community. Daily structure: morning = local practitioner session (1.5h) + afternoon = cross-clan working session на shared задаче + evening = synthesis + social. Collective artifact: comparative analysis + tooling recommendations. Cost: disclosed curation fee Jetix + direct participant travel. R12: Jetix не извлекает margin на travel (transparent). Fork-and-leave: участник может улететь раньше без clan penalty.

**Example I3 — Month-rhythm sponsor project per IP-1.**
T-спонсор (research org) финансирует 1-месячный hackathon на конкретную исследовательскую задачу. IP conditions: disclosed pre-registration («результаты становятся open-source; sponsor получает co-author credit + first-use right в течение 6 месяцев»). Teams = 3 кланоподобные группы × 5–8 человек. Monthly rhythm: week 1 = orientation + matching; weeks 2–3 = solve; week 4 = synthesis + QF distribution. Mentor rotation: каждые 10 дней ментор меняется (не monopoly mentorship). Recurse: artifact публикуется в Wiki, sponsor report отправляется, top contributors → invited to next research challenge.

**Example I4 — Research challenge без физического события.**
Задача публикуется онлайн: «Найти лучшую методологию X за 30 дней». Индивиды + кланы участвуют асинхронно. QF community vote в конце: каждый participant может поддержать несколько submissions. Mondragón 5:1: максимальный payout = [5× min payout]. IP: submissions open-source по умолчанию; opt-out возможен (но тогда не участвует в QF). Jetix revenue: sponsorship origination fee + talent placement (opt-in, disclosed).

**Example I5 — Public talk / conference mini-format.**
Формат «Jetix talk» на 50–100 человек. 3 speaker-practitioners + 2 working sessions. Ticket: [сценарная цена]. Speaker compensation: disclosed (% от ticket revenue per QF formula). Sponsor table: optional, R12-compliant (no judging influence). Post-event: recording → paid access OR open-access (Ruslan picks per event). Recurse: attendees invited to next hackathon с early-access slot.

---

## §J — R12 Paired-Frame Check (8 вопросов, influence-ethics + recruitment-dynamics AUTO-FIRE)

> **R12 AUTO-FIRE note.** Этот раздел присутствует в каждом events-документе. influence-ethics-expert и recruitment-dynamics-expert = обязательные receivers каждый раз, когда любой events-docs создаётся или обновляется. Missing pair = Halt-Log-Alert F4 ≤5s per Part 6b §I.2.

**J1. Mondragón 5:1 cap соблюдается?**
CHECK: в каждом QF distribution schema поле `mondragon_cap_ratio` ≤ 5. Jetix platform fee + max payout к min payout в рамках 5:1. Если нет → STOP, пересчитать перед публикацией.
ANTI-PATTERN: «победитель получает всё» (winner-takes-all) = нарушение 5:1. Решение: QF quadratic weighting автоматически предотвращает это при правильной реализации.

**J2. Sponsorship transparency соблюдается?**
CHECK: sponsor identity + pool size + IP conditions + platform fee раскрыты до регистрации. Нет скрытых spons agreements.
ANTI-PATTERN: «секретный спонсор» (анонимный финансист, влияющий на задачу). Решение: anonymity permitted только если спонсор не имеет влияния на задачу + pool + judging. Если влияние есть — full disclosure обязательна.

**J3. Anti-competitive between clans/cohorts?**
CHECK: соревновательные условия создают развивающую конкуренцию, не destructive. Resource parity checklist выполнен. No intel leakage mechanism. Judge independence declaration подписана.
ANTI-PATTERN: клан нанимает T-инсайдера для sabotage конкурентов; спонсор фаворизирует один клан; «информационная асимметрия» созданная организатором.

**J4. Fork-and-leave preserved из event?**
CHECK: explicit fork-and-leave clause в event registration terms. Partial QF credit mechanism задокументирован. Нет deposit/penalty.
ANTI-PATTERN: «невозможно уйти без потери взноса»; «клан несёт штраф за уход участника»; «уход = public shaming».

**J5. QF revenue distribution per Tang+Weyl?**
CHECK: QF schema документирована и published перед event. Community vote counted quadratically (не one-person-one-vote, не plutocratic). Smart contract или auditable spreadsheet.
ANTI-PATTERN: жюри из одного человека решает призы; sponsor оверрайдит QF; «я решаю кто победил» без прозрачного механизма.

**J6. FOMO-driven event marketing?**
INFLUENCE-ETHICS CHECK: маркетинг событий не должен создавать искусственную срочность («только 3 места осталось — это неправда»), fear-of-missing-out narratives («все успешные люди будут там»), или social pressure («твои знакомые уже зарегистрировались»).
ДОПУСТИМО: честные дедлайны (регистрация закрывается в [дату] — потому что нужно matching успеть провести) + информативные reminder (opt-in, не blast).

**J7. Pay-to-play exclusion?**
RECRUITMENT-DYNAMICS CHECK: система отбора участников не создаёт financial exclusion. Если платный entry — есть scholarship/access mechanism для qualified participants без средств (disclosed и реальный, не маркетинговый). Клан membership не требует дорогой entry fee для участия в событиях.
ANTI-PATTERN: «только члены премиум-клана могут участвовать»; «вступительный взнос = $5K за доступ к первому хакатону».

**J8. Recruitment funnel не манипулятивный?**
RECRUITMENT-DYNAMICS CHECK: события используются для community building, не как recruitment funnel с manipulation tactics. Нет cult-onboarding («мы особенные, остальные не понимают»), информационной изоляции («не слушай что говорят снаружи о нас»), или commitment escalation (маленькие обязательства → невозможно уйти).
ДОПУСТИМО: честный advocacy («нам нравится что мы делаем, вот почему — ты судишь сам»), community warmth (welcomeness, не love-bombing), retention через quality (не через psychological lock-in).

---

## §K — AI Tooling Integration

**Принцип:** AI = event orchestration (matching / mentor-pairing / logistics рутина). Человек = judging / mentorship / connection. Per O-182: AI fills coordination overhead, человек сохраняет decision authority на meaningful choices. FPF onboarding = lingua franca для всех участников.

**K1 — Participant + Mentor Matching.**
ROY swarm routing: participant profiles → engineer-expert / methodology-engineer / etc. peer-matching. Inputs: self-declared skills + past artifacts + event history. Output: ranked match suggestions (не автоматическое назначение). Human gate: T-организатор confirm. Система не знает «лучший ментор» — она surfacing candidates, человек решает.

**K2 — Logistics Automation.**
Automation candidates (safe to automate): calendar invites + resource allocation (cloud access, tool permissions) + QF distribution calculation + post-event feedback form distribution + reminder emails (opt-in only).
NOT automated: judging / mentorship quality assessment / sponsor negotiations / participant disputes / fork-and-leave processing (человек должен видеть каждый exit).

**K3 — FPF Onboarding.**
FPF (72K строк vendored) = lingua franca для всех участников. Onboarding через FPF: T-участник получает event-scoped FPF primer (≤2 часа onboarding). FPF defines: work contracts / promise structures / role definitions / artefact contracts. «За 2 часа в лица в проекты» [src: text_009] = FPF onboarding делает это возможным.

**K4 — ROY Swarm Event Support.**
brigadier = dispatcher для event-related tasks. engineering-expert = technical tool setup. mgmt-expert = PM для event timeline. systems-expert = coordination overhead monitoring (HP-T5 sub-linear check). investor-expert = sponsor economics check (QF pool sizing). influence-ethics-expert + recruitment-dynamics-expert = R12 paired-frame AUTO-FIRE на каждом revenue event.

**K5 — Post-Event Analytics.**
Metrics collected: participation rate + retention rate (HP-T3) + QF distribution spread (Gini coefficient as health signal) + mentor satisfaction (opt-in survey) + sponsor ROI (per agreed metrics). Analytics = Jetix internal, не surveillance. Participants see их own data. Aggregate trends = platform improvement substrate (Recurse loop).

---

## §L — Partner-Extension Hook

**L1 — T2 Sponsor хостит event через Jetix.**
Процесс: sponsor заявляет событие (task + pool + IP conditions) → Jetix R12-compliance review (3-5 рабочих дней) → если compliant → Jetix provides infrastructure (FPF + matching + QF distribution) → sponsor maintains event identity but on Jetix R12 rails. Revenue split: disclosed (platform fee % per event type). Sponsor cannot: override QF / enforce non-fork-and-leave / hide identity. «Jetix R12-certified event» = brand mark для compliant sponsor events.

**L2 — Клан организует свой хакатон (Layer 3-4).**
Clan Charter (LOCKED 2026-05-12) включает «clan-warfare-mode» — кланы могут организовывать inter-clan или intra-clan события. Процесс: клан заявляет событие через brigadier → mgmt-expert проверяет R12-compliance → если OK → клан получает Jetix event infrastructure + can invite external participants. Ключевое: R12 baseline не negotiable даже для internal clan events. Клан не может создать «закрытое мероприятие с pay-to-play exclusion».

**L3 — Layer 4: Participant как organizer.**
Progression path: Participant → Winner → Mentor → Organizer (§H Q9 описывает путь ментора; organizer = extended form). Organizer tier = прошёл курс §C + организовал ≥1 successful event + R12-compliance record. Layer 4 = bottom of funnel становится top: participants создают новые events, расширяя Jetix events calendar без Ruslan bottleneck.

**L4 — R12-compliance для partner events.**
Checklist из 8 пунктов §J = mandatory для всех partner events. «Jetix R12-certified» = все 8 J-checks passed + QF schema submitted + fork-and-leave clause verified. Partner events без certification = not listed on Jetix platform (но существуют независимо — нет fork-prevention). Certification = opt-in benefit (visibility + infrastructure), не forced gate.

---

## Заключение: Events как операционализация Vision

Direction #16 — не дополнительный revenue stream поверх существующей платформы. Это точка, где Мастерская (Workshop static substrate) становится живой. Без событий: infrastructure есть, людей нет, revenue нет, community нет. С событиями: infrastructure наполняется людьми, задачами, проектами, деньгами — и возвращает обратно через Recurse loop.

«Люди сами будут создавать хакатоны, искать исследования, решать задачи, ездить на экскурсии — всё через Jetix» [src: Ruslan voice 26.05] — это описывает Layer 3-4 зрелости. Layer 1 = Ruslan создаёт первый хакатон. Layer 2 = T-организаторы создают по курсу. Layer 3 = кланы создают inter-clan. Layer 4 = participants становятся organizers.

HP-T1..T5 = empirical backbone. Не marketing claims — falsifiable thresholds. Если HP-T1 не выполняется (первый хакатон ≤ 90 дней от ack) → operational-VAPOR signal. Если HP-T4 не выполняется (R12 extraction emerges) → Stop, fix, re-launch. Events = самый честный feedback loop для всей Jetix Vision.

> **R1 reminder:** этот спек — варианты. Ruslan авторизует финальную форму каждого документа.
> **R2 STRICT:** Foundation v1.0 LOCKED сохранён. Никаких Foundation-path writes без AWAITING-APPROVAL packet.
> **R12 paired-frame:** §J = обязательный checkpoint перед каждым revenue event. influence-ethics + recruitment-dynamics AUTO-FIRED.

---

*Direction #16 портфельный спек — brigadier-scribe, R1 surface. R2 + R11 + R12 STRICT + IP-1 preserved. 2026-05-26.*
