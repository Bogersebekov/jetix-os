---
phase: 4
direction: 3
title: "💼 Бизнес — полный портфель artefacts (V4)"
date: 2026-05-26
F: F2-F3
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
language: russian
type: phase-report-metaplan-v4
status: draft-report
---

# Direction #3 💼 Бизнес — портфель artefacts (V4)

## Вступление: Foundation embedding V4

Jetix — мега-мастерская мирового уровня: место, где люди становятся мастерами в эпоху AI, вместе двигают фронтир и не дают системе доить или запирать себя.

Три грани: 🏛️ Мастерская (ГДЕ) · 🎯 Мастерство (ЧТО) · 🌍 Сеть (КАК — mesh + pooling). Direction #3 Бизнес — это операционализация грани Сеть на уровне организационно-правовой формы, экономической модели и governance.

**V4-расширение Foundation embedding.** Три новых элемента расширяют бизнес-модель в V4:

1. **#16 Хакатоны** — первичный revenue engine: events economics заменяют консультационную модель «один клиент — один проект» на pooled-value creation (спонсоры + участники + QF matching pool ≥$30K/event target).
2. **Кланы как организационные под-единицы кооператива** — Mondragón cooperatives-spawning-cooperatives на уровне Jetix: каждый Clan = автономная cooperative-ячейка внутри сети, не филиал, не отдел.
3. **#15 Геймификация** — engagement-механика бизнеса без extraction (R12 HIGHEST): не «игровые трюки для удержания», а координационные механизмы, которые создают ценность для участников, не извлекают её в пользу платформы.

Кооператив — это не «красивая упаковка», это точная форма для мега-мастерской: автономные единицы связаны общими принципами (Mondragón pattern: 81 кооператив, внутренний банк, единая идентичность), каждая ячейка сохраняет суверенитет.

**Ключевые якоря direction #3 (V4):**
- Экономика: 75/25 split (worker/pool) + 5:1 wage-ratio cap + fork-and-leave (30-day notice, без штрафа)
- Хакатоны: sponsor commitments + QF pool ≥$30K/event; events-as-revenue-engine primary model в V4
- Геймификация R12 HIGHEST: engagement без extraction; Schelling coordination + virtual economy mechanics
- R12 четыре action classes: extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt
- Кланы lifecycle: formation / governance / inter-clan / fork-spawn / dissolution; Jetix = «качалка/склад» НЕ контролёр
- Ethereum Phase 2+: Mondragón ratio cap on-chain + QF revenue distribution + exit tokens; per-Clan opt-in
- Governance: Ruslan = единственный стратег; AWAITING-APPROVAL packets на все архитектурные изменения; Stage Gates SG-0..SG-7; Steward role; corrigibility

**GAP этого direction'а (V4):** жанр «create» по-прежнему отсутствует — риск, что Foundation-жаргон вытекает наружу в партнёрские тексты. V4 добавляет специфические переводы для Хакатон-контекста (спонсорские commitments) и Клан-контекста (внешние партнёры спрашивают: «мы форкаем что-то у вас или мы под вами?»).

---

## §V4-delta: Бизнес-модель V4 — три новых слоя

### V4-delta.1 Хакатоны (#16) как primary revenue engine

**Логика смещения.** V3 моделировал Jetix как consulting-кооператив с проектной экономикой. V4 вводит Хакатоны как первичный revenue engine: это не отдельный источник дохода — это смещение центра тяжести.

**Events economics (целевые параметры):**

| Компонент | Параметр | Комментарий |
|---|---|---|
| Sponsor commitments | ≥3 спонсора/event; avg. €5-10K каждый | Validated via discovery call до запуска event |
| QF matching pool | ≥$30K/event (target) | Quadratic Funding — проекты-участники получают matching из pool |
| Participant fees | €200-500/участник × 30-100 участников | Tier: early / standard / corporate |
| Revenue direction | 75/25 split применяется к event revenue | 25% → Jetix infrastructure pool |
| Post-event consulting | Lead-gen из хакатона → consulting pipeline | Конверсия участников в клиентов |

**Почему events меняют модель.** Consulting P2P (один консультант — один клиент) масштабируется линейно. Хакатон — pooled-value event: один event создаёт ценность для 30-100 участников одновременно, привлекает спонсорский капитал, генерирует pipeline для downstream consulting и community. Это квадратичный, не линейный рычаг.

**R12 в events context.** Sponsor деньги входят в QF pool — распределение по QF механике (квадратичное голосование), не по усмотрению организаторов. Это pre-declared distribution: R12 Q3 (non_consensual_distribution) не нарушается, потому что mechanics объявляются до события и участники соглашаются явно.

**Stage Gates для Хакатон-revenue engine:**
- SG-1 для event: ≥3 sponsor commitments confirmed + venue/platform secured
- SG-2 для event: ≥$30K QF pool funded + participant registrations ≥ threshold
- Post-event: revenue distributed per 75/25; leads logged в CRM; Steward audit

### V4-delta.2 Кланы как organizational sub-units кооператива

**Mondragón cooperatives-spawning-cooperatives.** Mondragón — 81 кооператив внутри одной идентичности. Jetix строит то же самое, но через Clan-lifecycle, а не через слияния. Ключевой сдвиг V4: Кланы — не проекты, не команды, не «подразделения». Кланы = автономные cooperative-ячейки внутри сети.

**Lifecycle Клана (V4 EXPANDED):**

```
Formation          → SG-0: Charter написан + R12 прошёл review
Governance setup   → SG-1: первые члены + первый income event
Операционная фаза  → SG-2..SG-4: traction + repeatability + scale
Inter-clan ties    → Edges в wiki/graph/edges.jsonl; optionally shared QF pool
Fork-spawn         → Clan рождает sub-Clan (рекурсивный spawn); родитель = network peer
Dissolution        → 30-day notice → exit tokens → архивация Charter
```

**Граница governance: Клан vs Foundation-level.**

| Уровень | Что решает | Что не может изменить |
|---|---|---|
| Clan inner-governance | Операционные правила; внутренние роли; проекты; wage distribution внутри диапазона | R12 четыре action classes; fork-and-leave right; wage cap (только строже, не слабее) |
| Foundation-level (Jetix) | Конституционные принципы; Charter template; R12 enforcement | Операционную автономию Клана |
| Граница-enforcement | Steward мониторит конституционные инварианты; всё остальное — inner-Clan | Конституционный floor enforced; остальное = суверенитет Клана |

**Ценностной floor = триада+R12+уважение.** Три компонента пола, ниже которого Клан не может опуститься:
1. Триада: Мастерская (среда обучения) + Мастерство (методологический IP) + Сеть (mesh-связи без extraction)
2. R12: четыре action classes запрещены без исключений
3. Уважение: anti-cult discipline, 30-day exit без штрафа, данные портируются

**Jetix = «качалка/склад», НЕ контролёр.** Метафора точная:
- «Качалка» = Jetix предоставляет инфраструктуру для роста (методология, governance templates, ROY swarm как ops-машина, QF механику)
- «Склад» = Jetix хранит общий IP pool (wiki/, Charter templates, R12 schemas), к которому Кланы имеют доступ
- НЕ контролёр = Jetix не надстройка, не franchiser, не иерарх; Клан = peer, не дочерняя единица

**Inter-clan координация.** Кланы могут создавать cross-clan QF pools для совместных событий (хакатоны), обмениваться методологическим IP, co-sponsor каждый другой. Координация идёт через network edges, не через иерархию Jetix.

### V4-delta.3 Геймификация (#15) = engagement-механика без extraction (R12 STRICT)

**Разграничение:** Геймификация в контексте Jetix-бизнеса — это не dark patterns удержания (streak mechanics которые создают зависимость, скорбные уведомления, FOMO loops). Это координационные механизмы, которые создают реальную ценность:

| Механика | Как работает | R12 check |
|---|---|---|
| Schelling points | Общие точки координации для inter-clan событий (хакатоны как регулярные Schelling events) | Участие добровольное; extraction = 0 |
| Virtual economy mechanics | Reputation tokens внутри Clan или cross-clan; не конвертируются в деньги без явного согласия | R12 Q3: distribution requires consent |
| Achievement tracks | Мастерство-прогрессия видна участникам; не gamified для удержания, а для recognition | No artificial scarcity; no lock-in |
| QF voting mechanics | Участники Хакатона распределяют matching pool через квадратичное голосование | Mechanics объявлены заранее; R12 compliant |

**influence-ethics-expert auto-pair.** R12 HIGHEST для #15: каждый раз когда gamification-engagement-expert участвует в планировании механик для direction #3, influence-ethics-expert автоматически получает paired task. Отсутствие пары = Halt-Log-Alert F4 ≤5s.

**Платформа = infrastructure provider, не rent-extractor.** Это ключевое бизнес-позиционирование:
- Jetix берёт 25% pool share как infrastructure fee — это agreed share, не extraction
- Платформа не держит данные участников как leverage
- Платформа не создаёт switching costs через технические lock-in механизмы
- Fork-and-leave 30-day notice применяется к Клану целиком, включая его данные и IP

---

## §A. Главный документ «Как устроен Jetix»

### A.1 1-pager (≤500 слов) — спецификация

**Назначение:** первое касание с партнёром, спонсором хакатона, или инвестором. Закрыть вопрос «что это вообще такое» за 2-3 минуты чтения.

**Аудитория:** потенциальные партнёры (будущие члены-основатели), ранние инвесторы (angels, impact funds), корпоративные клиенты и спонсоры хакатонов на разведке.

**Формат:** MD + PDF export, A4, одна страница при стандартном шрифте. Никакого жаргона (нет «AWAITING-APPROVAL», «F-G-R», «brigadier»).

**Структура 1-pager'а (V4):**
1. Одна фраза — что такое Jetix (мега-мастерская + кооператив + события)
2. Проблема — почему AI-эпоха ломает старые модели обучения, работы и extractive platforms
3. Решение — мега-мастерская: место + метод + сеть; события (хакатоны) как engine
4. Как работает экономика — 75/25, потолок 5:1, выход без штрафа; QF для событий (три строки)
5. Кланы — автономные ячейки сети; Jetix = инфраструктура, не иерарх
6. Где сейчас — точка Build, первая когорта O-161 (5-10 основателей), первый хакатон в pipeline
7. Что хотим от читателя — CTA (discovery call / стать спонсором / ознакомиться с Charter)

**Тон:** прямой, без корпоративного пафоса. Язык — такой, чтобы умный незнакомец понял за первое прочтение. V4: добавить «events» в core narrative, потому что Хакатоны — конкретный, осязаемый hook для спонсоров и партнёров.

### A.2 Long-form (≤5K слов) — спецификация

**Назначение:** углублённое знакомство для тех, кто прошёл 1-pager и хочет понять детали перед decision call.

**Аудитория:** серьёзные партнёры-кандидаты, impact-инвесторы с DD-процессом, потенциальные Clan Leads, журналисты/исследователи.

**Формат:** MD + PDF, 8-12 страниц.

**Разделы (V4-extended):**
1. Thesis — почему мы строим именно так (Mondragón + deep-tech + методологический IP + events-as-engine)
2. Что такое мега-мастерская — три грани операционально (Мастерская / Мастерство / Сеть)
3. Экономическая модель — 75/25 split, 5:1 cap, social fund 10%, QF matching, events economics (хакатоны ≥$30K/event target), triple-role
4. Кланы — lifecycle (formation → dissolution), граница governance, Jetix как «качалка/склад»
5. Governance — Stage Gates, Steward role, один стратег на Phase A; corrigibility; как система не запирает
6. Хакатоны как revenue engine — events economics, sponsor mechanics, QF pool, downstream pipeline
7. Геймификация без extraction — R12-compliant engagement mechanics; Schelling coordination
8. R12 anti-extraction — восемь вопросов (plain language, без кода)
9. AI как операционная машина — ROY swarm что делает, что не делает; corrigibility
10. Lifecycle — Build / Run / Scale / Mature, где сейчас, что разблокирует следующий этап
11. Ethereum Phase 2+ — programmable enforcement, per-Clan opt-in, exit tokens
12. Как присоединиться — Charter, discovery call, стать спонсором хакатона, запустить Clan

**Ключевой принцип:** Foundation-жаргон переводится. «AWAITING-APPROVAL packet» → «решения с архитектурным влиянием требуют явного одобрения основателя». «Halt-Log-Alert» → «при нарушении конституционных принципов система останавливается и сигнализирует». «Клан» → в тексте объяснить как «автономная мастерская-ячейка внутри сети».

---

## §B. Видео

**Hook (0-10 сек):** Один вопрос в лоб — «Вы когда-нибудь работали в компании, где правила придумывают наверху, а платят внизу?» Пауза. «Мы строим что-то другое.»

**Сцены (V4-extended):**

1. (10-40 сек) Проблема — AI меняет рынок труда и создаёт новое extraction: платформы собирают данные, удерживают пользователей, берут 30-40% без реальной ценности. Старые компании реагируют старыми инструментами.
2. (40-90 сек) Jetix как мега-мастерская — три грани (место / метод / сеть); аналогия с ремесленной гильдией, обновлённой для AI-эпохи. Кланы как autonomous cells.
3. (90-150 сек) События как engine — Хакатоны: 30-100 участников, спонсоры, QF pool. Не просто «тусовка» — это способ создать ценность для многих одновременно и распределить её честно. QF механика объясняется на пальцах.
4. (150-210 сек) Кооперативная экономика — 75/25, потолок 5:1, можно уйти через 30 дней без штрафа. Jetix = «качалка/склад», не franchiser.
5. (210-250 сек) Governance — Stage Gate (просто: идея → валидация → запуск → масштаб); Steward как роль; геймификация — engagement без manipulation.
6. (250-270 сек) Где сейчас, что строим, кого ищем — партнёры, Clan Leads, спонсоры первого хакатона.

**Closing:** «Если вы хотите строить что-то серьёзное, участвовать в событиях где правила честные, и не отдавать 100% плодов вверх — посмотрите Charter.» [ссылка]

**Аудитория:** потенциальные члены-основатели (25-45 лет, tech/consulting/education background), impact-инвесторы, корпоративные спонсоры, журналисты Future of Work темы.

**Длина:** 3-4 минуты. Формат: screen + talking head Ruslan. Субтитры обязательны (EN + RU). V4: добавить визуальный момент для QF pool mechanics — это конкретный и наглядный hook для спонсоров.

---

## §C. Курс — спецификация модулей

**Название (рабочее):** «Компания как кооператив в эпоху событий: строим Jetix изнутри»

**Аудитория:** будущие основатели собственных кланов / кооперативов; участники Workshop и Хакатонов, дошедшие до уровня «хочу строить, а не только учиться».

**Формат:** 7 модулей × 3-4 урока, асинхронный; финал — живая группа с Ruslan.

**Skeleton модулей (V4):**

- M1: Почему кооператив — не charity и не хипстерство. Mondragón 81 кооператив как proof of concept. Три failure modes классической компании vs кооперативная структура.
- M2: Экономическая модель Jetix. 75/25 split — откуда цифра. 5:1 wage cap — математика и мотивация. Social fund 10% — зачем. Fork-and-leave — механика и психология выхода.
- M3: Хакатоны как revenue engine. Events economics: sponsor commitments, QF pool, participant fees, downstream pipeline. Как организовать event с QF-распределением. R12 в events context.
- M4: Кланы — lifecycle и governance. Formation → dissolution. Граница Clan vs Foundation governance. Jetix = «качалка/склад». Spawn pattern: рождение sub-Clan. Inter-clan координация без иерархии.
- M5: Governance без диктатуры. Stage Gates как инструмент роста. Steward role. Решение vs стратегия. Геймификация: engagement без extraction — R12 HIGHEST discipline.
- M6: R12 на практике. Восемь вопросов anti-extraction. Как проверить любое решение. Кейсы: events, Clan spawn, wage decisions.
- M7: Phase 2+ горизонт. Ethereum programmable governance. QF matching on-chain. Network State spawn. Как форкнуть Jetix-модель под свой Clan.

**Каждый модуль:** теория (видео ≤20 мин) + практика (worksheet / шаблон) + обсуждение (async forum или live).

---

## §D. Книга — спецификация глав

**Рабочее название:** «Компания-кооператив в эпоху AI: архитектура, которую не сломают»

**Аудитория:** предприниматели, консультанты, исследователи будущего организаций. Не учебник — манифест с практикой.

**Skeleton глав (V4-extended):**

- Введение: Почему старая модель компании устарела (AI + extraction-economy + winner-takes-all + platform rent)
- Гл. 1: Мега-мастерская как форма. Три грани. История гильдий и почему она возвращается.
- Гл. 2: Mondragón как proof. 81 кооператив, Caja Laboral, 85-90% retention. Что работает, что нет (cross-border scalability gap, programmable enforcement gap).
- Гл. 3: Экономика справедливости. 75/25 split. 5:1 wage-ratio cap. Triple-role. Events economics: QF pool как fair distribution mechanism.
- Гл. 4: Кланы — autonomous cells. Lifecycle. Jetix = «качалка/склад». Spawn. Inter-clan. Dissolution. Ценностной floor.
- Гл. 5: Хакатоны как движок. Events economics. Sponsor mechanics. QF. Downstream pipeline. Почему events = квадратичный, не линейный рычаг.
- Гл. 6: Геймификация без manipulation. R12-compliant engagement. Schelling coordination. Virtual economy mechanics. Разница между value-creating mechanics и dark patterns.
- Гл. 7: R12 — конституция против extraction. Восемь вопросов. Четыре запрещённых класса. Fork-and-leave как главная защита.
- Гл. 8: Governance без диктатуры. Stage Gates. Steward role. Стратегия vs операция.
- Гл. 9: AI как операционная машина. ROY swarm. Corrigibility на практике.
- Гл. 10: Запуск первой когорты. Charter v1. Onboarding. Anti-cult дисциплина.
- Гл. 11: Масштабирование кланов. Spawn pattern. Network State как горизонт. Ethereum Phase 2+.
- Заключение: Что значит «двигать фронтир» не дав системе запереть тебя — и не запирая других.

---

## §E. Инструкции/SOP — governance procedures

**Назначение:** операционный справочник для Steward, Ruslan и будущих Clan Leads. Внутренний документ.

**Структура SOP-пакета (V4-extended):**

### E.1 Как принимается решение (Decision Flow)

```
Входящее решение
├── Операционное (затрагивает один проект, обратимо, не меняет принципы)
│   └── Ответственный Lead или Ruslan → логируется → исполняется
├── Events-operational (хакатон: venue, спонсор онбординг, QF pool setup)
│   └── Ответственный Event Lead → R12 QF-check → логируется → исполняется
├── Clan governance (inner-Clan operationaly; не нарушает конституционный floor)
│   └── Clan Lead → inner-Clan process → логируется в Clan governance log
├── Архитектурное (изменение Foundation, principles/, schemas/, routing-table)
│   └── AWAITING-APPROVAL packet → Ruslan ack → LOCKED → исполняется
├── Стратегическое (direction, vision, resource allocation)
│   └── Только Ruslan → логируется как R1 decision → производный контент отмечается
└── Конституционное нарушение (R12 action class detected)
    └── HALT → log.jsonl → Ruslan alert → разбор
```

### E.2 Stage Gates (SG-0..SG-7) — операционная механика

| Gate | Название | Predicate-пример | Что разблокирует |
|------|----------|-----------------|-----------------|
| SG-0 | Idea validated | Ruslan ack + problem statement written | Scaffold проекта |
| SG-1 | First signal | ≥3 leads / ≥1 paid session / ≥1 sponsor confirmed / ≥1 partnership MOU | Полный scaffold |
| SG-2 | Traction | Revenue ≥ threshold OR cohort ≥ N OR event QF pool ≥ $30K | Operational budget |
| SG-3 | Repeatability | ≥3 successful cycles (sessions / events / Clan spawns) | Process documentation |
| SG-4 | Promote / Scale | Stable revenue + team ≥ core-group | Phase transition |
| SG-5 | Legal entity | Registered coop entity | Formal contracts |
| SG-6 | Charter ratified | Charter v1 signed by first cohort | Full member rights |
| SG-7 | Ethereum on-chain | Smart-contract deployed + audited | R12 programmable enforcement |

**de-morph:** откат через `/project-de-morph --rollback-to=SG-N`. Логируется. Данные предыдущих gates сохраняются.

**Anti-patterns SG:** предсказание вместо predicate запрещено; автопромотирование без Ruslan ack запрещено; retroactive gate-firing запрещён без explicit AWAITING-APPROVAL.

### E.3 AWAITING-APPROVAL — когда и как

Пакет открывается для: изменений Foundation paths; routing-table; R12-классов; любого действия из default-deny-table без explicit ack.

V4 дополнение: изменение QF pool mechanics, изменение sponsor share в events economics, изменение Clan конституционного floor — все требуют AWAITING-APPROVAL.

Структура пакета: gate_type / blast_radius / proposed_change / reversibility / Ruslan_ack_required.

После ack — исполняется, логируется в swarm/approvals/log.jsonl.

### E.4 Steward role — responsibilities (V4)

- Мониторинг R12: каждое распределение дохода (включая events QF) запускает 8-вопросный чеклист
- Stage Gate audit: еженедельно `/lint --check-stage-gates`
- Clan floor monitoring: при регистрации нового Клана — проверка, что Charter не нарушает ценностной floor
- Gamification audit: при внедрении новой engagement-механики — paired check с influence-ethics-expert
- Anti-cult discipline: давление на выход, нарушение 30-day notice, lock-in через virtual economy
- Escalation to Ruslan: при любом нарушении конституционных принципов — немедленно

**Anti-patterns Steward:** не стратег; не цензор операционных решений; при масштабировании → rotating Steward panel.

---

## §F. Шаблоны / Templates

### F.1 Charter draft schema (V4)

```yaml
charter_version: "1.0"
clan_name: ""
founding_date: ""
mission_statement: ""

economics:
  worker_share: 75
  pool_share: 25
  wage_ratio_cap: "5:1"
  social_fund_pct: 10
  exit_notice_days: 30
  exit_penalty: none
  events_qf_pool_participation: optional  # per-event opt-in для QF

governance:
  strategist: "ruslan"  # Phase A; updatable at SG-4+
  decision_classes: [operational, events_operational, clan_governance, architectural, strategic, constitutional]
  stage_gates_active: true
  steward_role: true
  corrigibility: "owner-ack-authority-final"
  jetix_role: "infrastructure_provider"  # не иерарх

r12_declaration:
  anti_extraction_classes:
    - extraction_beyond_share
    - wage_ratio_violation
    - non_consensual_distribution
    - fork_prevention_attempt
  enforcement_phase_1: "charter-text-consent"
  enforcement_phase_2: "ethereum-on-chain"
  gamification_r12_highest: true  # engagement mechanics require paired influence-ethics check

clan_lifecycle:
  formation: "SG-0 charter_written + r12_review_passed"
  autonomy: "inner_clan_governance_sovereign_above_floor"
  jetix_relation: "network_peer_not_subsidiary"
  fork_spawn: "allowed_any_time_above_floor"
  dissolution: "30_day_notice_data_portability_exit_token"

member_rights:
  fork_and_leave: true
  exit_notice_days: 30
  data_portability: true
  vote_weight: "1-member-1-vote"

member_obligations:
  participation_minimum: ""
  knowledge_contribution: ""
  anti_cult_discipline: true
```

### F.2 Stage Gate checklist (per gate)

```markdown
## SG-[N] Checklist — [Gate Name]

- [ ] Predicate defined (binary: yes/no)
- [ ] Predicate measured (source: [file/metric])
- [ ] Predicate = true
- [ ] Ruslan ack received (date: )
- [ ] Spawned paths created (list: )
- [ ] Logged to stage-gate-fires-YYYY-MM-DD.md
- [ ] No banned phrases in predicate (/lint --validate-predicate: PASS)
- [ ] Events-specific: QF pool mechanics declared pre-event [N/A if not event]
- [ ] Clan-specific: constitutional floor checked [N/A if not Clan]
```

### F.3 Governance log entry schema

```jsonl
{"date": "YYYY-MM-DD", "type": "stage_gate|awaiting_approval|r12_check|steward_audit|clan_floor_check|gamification_paired_check", "gate_id": "SG-N", "actor": "ruslan|steward|brigadier", "result": "fired|ack|violation|pass", "note": ""}
```

### F.4 R12 8-вопросный чеклист (для Steward)

1. Получает ли каждый член свою согласованную долю (75/25)?
2. Превышает ли разница max/min зарплат 5:1?
3. Есть ли распределение дохода без явного согласия членов (включая QF pool)?
4. Создаёт ли решение барьер для выхода (технический / финансовый / социальный / психологический)?
5. Блокирует ли это решение возможность форка?
6. Получает ли платформа / AI-система / спонсор ценность сверх согласованной доли?
7. Изменяет ли решение условия задним числом без ретроактивного согласия?
8. Если смарт-контракт Phase 2+ существовал бы — это решение прошло бы его логику?

**V4 дополнение — вопрос 9 (events-specific, не конституционный, но recommended):**
Объявлены ли QF mechanics участникам до события, с явным согласием до регистрации?

---

## §G. Презентация — 10-20 слайдов

**Аудитория:** партнёры / инвесторы / корпоративные спонсоры на discovery call или конференции.

**Skeleton слайдов (V4):**

| # | Заголовок | Содержание |
|---|-----------|------------|
| 1 | Jetix | R1 one-liner + визуал три грани + «events engine» |
| 2 | Проблема | AI меняет рынок; extractive platforms; старые модели не работают |
| 3 | Почему кооператив | Mondragón proof + три failure modes классической компании |
| 4 | Мега-мастерская | Мастерская / Мастерство / Сеть — операционально |
| 5 | Хакатоны как engine | Events economics: sponsor ≥€5-10K/sponsor × 3 + QF pool ≥$30K; downstream pipeline |
| 6 | Кланы | Lifecycle; Jetix = «качалка/склад»; spawn pattern; network peer, не иерарх |
| 7 | Экономика | 75/25 + 5:1 cap + social fund; QF mechanics визуально |
| 8 | Fork-and-leave | 30 дней, без штрафа; почему это делает систему лучше |
| 9 | Геймификация без extraction | R12 HIGHEST; Schelling coordination; что ≠ dark patterns |
| 10 | Governance | Stage Gates визуально; Steward; один стратег |
| 11 | AI как операционная машина | ROY swarm — что делает, что не делает |
| 12 | R12 anti-extraction | 4 запрещённых класса; 8 вопросов (plain language) |
| 13 | Lifecycle | Build → Run → Scale → Mature; точка A сейчас |
| 14 | Ethereum Phase 2+ | Triple-role token; programmable enforcement; per-Clan opt-in |
| 15 | Команда | Ruslan + первая когорта |
| 16 | Компаративы | Mondragón / RaidGuild / Equal Exchange / ETHGlobal / Devfolio |
| 17 | Что ищем | Партнёры-основатели / инвесторы / спонсоры хакатонов / Clan Leads |
| 18 | Следующий шаг | Charter / discovery call / Q&A |

**Дизайн-принципы:** минималистично, данные > украшения, каждый слайд = одна идея. V4: слайд 5 (Хакатоны) — самый конкретный и осязаемый для спонсорской аудитории; приоритизировать его визуально.

---

## §H. FAQ — честные ответы

### H.1 Базовые вопросы (аудитория: незнакомые)

**Q1: Вы кооператив или компания?**
Мы строим кооператив. Юридического лица пока нет (Stage Gate SG-5 ещё не достигнут). Charter v1 — текстовое соглашение об обязательствах, предшествующее юридическому оформлению. Это честнее, чем зарегистрировать LLC и называть её кооперативом.

**Q2: Кто решает в Jetix?**
На текущем этапе (Build) стратегические решения принимает Ruslan. Операционные — распределены между Lead'ами. Переход к более распределённому governance через Stage Gates при достижении Scale. Не «потому что Ruslan хочет власти» — потому что рассредоточенный контроль до traction убивает стартапы.

**Q3: Как вы защищаете от диктатуры основателя?**
Четыре уровня: (1) Charter запрещает R12 action classes; (2) Steward мониторит; (3) fork-and-leave 30 дней без штрафа; (4) Phase 2+ — Ethereum on-chain, ни Ruslan не может изменить параметры без смарт-контракта.

**Q4: Что значит 75/25?**
75% от revenue проекта/сессии/события — тому, кто создал ценность (worker). 25% — в общий pool (инфраструктура, social fund, рост). «Ruslan берёт 25%» — нет, это pool системы.

**Q5: Что значит fork-and-leave?**
30-day notice. Без штрафа. Данные портируются. Опционально: берёшь Charter template и строишь свой Clan. Jetix и новый Clan остаются в network как peers.

**Q6: Что такое Клан в Jetix?**
Автономная cooperative-ячейка внутри сети. Свой Charter, свои проекты, своя governance — в рамках ценностного floor (R12 + fork-and-leave + уважение). Jetix предоставляет инфраструктуру, не командует.

### H.2 Более сложные вопросы (аудитория: серьёзные партнёры)

**Q7: Хакатоны — почему это revenue engine, а не просто маркетинг?**
Events economics: спонсоры платят €5-15K за exposure к целевой аудитории; участники платят €200-500 за доступ к методологии, нетворку и QF механике; QF pool ≥$30K создаёт реальные гранты для проектов. Downstream: участники конвертируются в consulting клиентов и Clan Leads. Это создаёт ценность для всех участников, а не только для организатора.

**Q8: Что такое QF pool и зачем он спонсорам?**
Quadratic Funding — механика распределения matching money: каждый участник голосует своими деньгами, matching усиливает проекты с широкой поддержкой (не только богатые вкладчики). Спонсорам: их деньги идут не «в маркетинг организатора», а напрямую в проекты участников. Это осязаемый social impact vs слепое спонсорство конференции.

**Q9: Геймификация — это не манипуляция?**
В Jetix — нет. R12 HIGHEST гарантирует: каждая engagement-механика (репутационные токены, хакатон scoring, achievement tracks) проходит paired-check с influence-ethics-expert. Dark patterns (FOMO loops, streak mechanics с зависимостью, scarcity manipulation) — запрещены на конституционном уровне. Геймификация = координационные механизмы, не ловушки удержания.

**Q10: Как Клан соотносится с Jetix — он под вами или отдельно?**
Отдельно, но в сети. Аналогия точная: Mondragón и каждый из его 81 кооперативов. Jetix = shared infrastructure + constitutional floor. Клан = autonomous peer. Jetix не берёт процент с Клана сверх agreed infrastructure fee, не имеет права блокировать Клан, не держит данные Клана.

**Q11: Почему AI — операционная машина, а не стратег?**
Потому что стратегия требует skin-in-the-game, которого у AI нет. Агенты surfac'ят варианты, помогают исполнять. Ruslan — единственный стратег. Это архитектурный принцип: компании, где AI принимает стратегические решения, создают systems без ответственности.

**Q12: Ethereum Phase 2+ — обязательно для Клана?**
Per-Clan opt-in. Базовая защита (Charter текст + Steward + fork-and-leave) работает без блокчейна. Phase 2+ добавляет programmable enforcement: смарт-контракт, который ни основатель, ни Clan Lead не может обойти.

**Q13: Как мне стать спонсором хакатона?**
Discovery call с Ruslan → обсуждаем цели (talent pipeline? brand visibility? social impact?) → confirmed commitment (минимальный порог) → ваши деньги в QF pool → получаете exposure + impact report после события.

**Q14: Как запустить свой Клан через Jetix?**
(1) Discovery call — понять fit; (2) Charter review — адаптировать template под свой Clan; (3) R12 review Steward или Ruslan; (4) SG-0 predicate: Charter написан + R12 passed → Clan autonomous; (5) Edge в network graph. Jetix = peer с этого момента.

---

## §I. Worked examples (IP-1 STRICT — без executor names)

### Example 1: Новый партнёр проходит onboarding

Ситуация: Анна, эксперт по организационному дизайну, узнала о Jetix, хочет присоединиться и возможно запустить Clan по своей специальности.

Процесс:
1. Discovery call (Ruslan + Анна): fit, Charter, экономика, роль Клана
2. Анна читает Charter — вопросы по R12, QF mechanics, Clan lifecycle
3. Ruslan открывает O-161 onboarding entry (операционное — AWAITING-APPROVAL не нужен)
4. Первый проект Анны: консультация → 75/25 применяется с первого дня
5. SG-1 предикат: cohort +1; если ≥5 → gate может сработать
6. Анна опционально: запускает Clan «Org Design Collective» → SG-0 Clan Charter написан + R12 passed → autonomous

### Example 2: Организация первого хакатона

Ситуация: Jetix планирует первый хакатон — «AI Tools for Cooperatives».

Процесс:
1. Ruslan ack'ует концепцию — R1 strategic decision logged
2. Event Lead (из ROY swarm dispatch) готовит events economics proposal: 3 sponsors × €7K + participant fees 50 × €300 = €36.5K gross
3. QF pool target: ≥$30K → sponsor €21K + Jetix contribution → declared pre-event
4. SG-1 event: ≥3 sponsors confirmed → fire; Ruslan ack
5. QF mechanics объявлены участникам до регистрации: R12 Q3 passed (consent pre-event)
6. Steward: R12 audit post-event → 75/25 applied → governance log entry
7. Downstream: 12 из 50 участников → CRM leads; 2 → discovery call; 1 → Clan spawn

### Example 3: Запрос на изменение wage cap

Ситуация: Clan Lead предлагает поднять cap с 5:1 до 8:1 для senior специалиста.

Процесс:
1. Clan Lead пишет предложение → brigadier роутит к mgmt-expert + investor-expert
2. Эксперты surfac'ят варианты (8:1 / 6:1 с sunset clause / raise floor instead of cap)
3. AWAITING-APPROVAL packet: wage_ratio_violation = конституционный класс
4. Ruslan получает пакет → ack или reject
5. Если ack: Charter обновляется; Steward уведомлён; Clan может применить

Что не происходит: Clan Lead не решает самостоятельно. AI не «рекомендует» итоговый вариант.

### Example 4: Clan spawn

Ситуация: Михаил, ранний участник, хочет запустить отдельный Clan на основе Jetix-модели — «DevCooper».

Процесс:
1. Михаил уведомляет Ruslan и Steward — 30-day notice (если он выходит из текущего Clan)
2. Steward R12 exit check: нет штрафов, данные портируются
3. Михаил получает Charter template (§F.1)
4. Адаптирует под DevCooper: wage cap оставляет 5:1, добавляет tech-specific governance rules
5. Steward review: конституционный floor OK → SG-0 DevCooper passed
6. DevCooper автономен; Jetix = network peer
7. Edge: `{from: jetix, to: devcooper, type: spawned, date: YYYY-MM-DD}`
8. DevCooper может co-sponsor следующий хакатон как network partner

### Example 5: Gamification механика — paired check

Ситуация: mgmt-expert предлагает ввести «streak mechanics» для участников курса — streak потери при пропуске сессий.

Процесс:
1. Proposal попадает к brigadier
2. Автоматически: gamification-engagement-expert dispatched + influence-ethics-expert paired (R12 HIGHEST)
3. influence-ethics-expert: streak mechanics с потерями = dark pattern; создаёт anxiety-based retention, не value-based
4. Вывод: не соответствует R12 anti-extraction (psychological lock-in = fork_prevention_attempt через soft coercion)
5. Альтернатива: achievement recognition (positive streak, без потерь); proposal revised
6. Ruslan finalize: одобряет revised mechanics
7. Logged: gamification_paired_check PASS для revised version

### Example 6: Stage Gate SG-4 и promote

Ситуация: проект quick-money (P1) достигает stable revenue + cohort ≥ core-group.

Процесс:
1. `/lint --check-stage-gates` выявляет SG-4 predicate = true
2. brigadier готовит promote proposal → Ruslan ack
3. Проект переходит в Scale phase
4. `/project-promote quick-money` — scaffold масштабируется
5. SG-5/SG-6 становятся активными (legal entity + Charter ratified)

---

## §J. R12 paired-frame check

### J.1 8 вопросов — governance edition (V4)

Каждое governance-решение в direction #3:

1. **Share integrity:** все члены получают согласованную долю (75/25)? Events QF pool — mechanics declared?
2. **Wage ratio:** wage cap 5:1 соблюдается? Предложение не нарушает?
3. **Consent:** изменение дохода / QF / распределения — с явного согласия?
4. **Exit freedom:** создаёт ли решение барьер выхода (технический / финансовый / социальный / psychological via gamification)?
5. **Fork freedom:** позволяет ли решение создать Clan fork? Запирает ли оно членов?
6. **Substrate extraction:** получает ли платформа / AI / спонсор ценность сверх agreed share?
7. **Retroactivity:** изменяет ли условия задним числом без consent?
8. **Phase 2+ compatibility:** если смарт-контракт существовал бы — решение прошло бы его логику?

### J.2 Governance anti-patterns (V4-extended)

| Anti-pattern | Признак | Защита |
|---|---|---|
| Founder lock-in | Основатель блокирует выход или форк | fork-and-leave 30d; exit token Phase 2+ |
| Strategic capture | AI «предлагает» стратегию; owner соглашается без критической оценки | Ruslan = sole strategist; AI = surface only |
| Gate inflation | Stage Gates расширяются без ack | AWAITING-APPROVAL на изменение gate schema |
| Steward overreach | Steward блокирует операционные без конституционного основания | Steward = конституционный монитор, не менеджер |
| Silent distribution | Revenue идёт в фонд без Charter basis | R12 Q3 + Steward audit |
| Wage drift | cap ростёт через «исключения» | Charter explicit cap + SG-5 enforcement |
| Cult dynamics | Давление «не уходить»; социальная стоимость выхода | Anti-cult discipline + 30-day notice |
| AI autonomy creep | Агент принимает архитектурные решения | Default-deny + AWAITING-APPROVAL + Halt-Log-Alert |
| Gamification lock-in | Engagement mechanics создают psychological dependency | R12 HIGHEST; influence-ethics paired check |
| Clan subordination | Jetix ведёт себя как franchiser | Charter: Jetix = infrastructure provider, not controller |
| Sponsor extraction | Sponsor получает data/control сверх agreed exposure | R12 Q6; QF pool pre-declared; sponsor contract explicit |
| QF manipulation | Pool mechanics меняются post-announcement | QF mechanics locked pre-event; AWAITING-APPROVAL на change |

### J.3 Corrigibility в governance контексте (V4)

- Ruslan может отменить любое Stage Gate решение через AWAITING-APPROVAL
- Члены могут форкнуться в любой момент — system-level corrigibility
- Кланы могут выйти из network — это тоже corrigibility
- Геймификация: участник всегда может отключить engagement tracking без penalty
- Ethereum Phase 2+ не блокирует Ruslan из системы контроля — per-Clan opt-in, not mandatory

---

## §K. AI tooling integration

**ROY swarm как операционная машина для Бизнес-direction (V4)**

Governance — не область, где AI стратегизирует. Но AI снижает операционную нагрузку.

### K.1 Что делает swarm в direction #3 (V4)

| Задача | Кто из ROY | Что делает |
|---|---|---|
| Stage Gate monitoring | brigadier + mgmt-expert | Еженедельный `/lint --check-stage-gates` |
| R12 audit | mgmt-expert + investor-expert | 8-вопросный checklist на каждое распределение |
| Events economics analysis | investor-expert + systems-expert | Моделирование events P&L; QF pool sizing |
| Gamification paired check | gamification-engagement-expert + influence-ethics-expert | R12 HIGHEST paired; каждая новая mechanics |
| Clan floor monitoring | systems-expert + mgmt-expert | При spawn нового Клана — конституционный floor check |
| AWAITING-APPROVAL drafting | brigadier | Структура пакета; Ruslan заполняет стратегическую часть |
| Charter monitoring | systems-expert | Внутренняя согласованность Charter при изменениях |
| Governance log | brigadier | Все gate events в governance log (append-only) |
| Partner onboarding support | mgmt-expert + philosophy-expert | Материалы к discovery call; не решает об onboarding |
| Sponsor outreach support | mgmt-expert + quick-money-brigadier | Events pipeline; discovery call materials |

### K.2 Что swarm НЕ делает (IP-1 STRICT)

- Не принимает стратегических решений о governance или events
- Не решает, кого принять в O-161 или кому одобрить Clan spawn
- Не изменяет Charter без AWAITING-APPROVAL + Ruslan ack
- Не выбирает между вариантами wage cap
- Не открывает AWAITING-APPROVAL на конституционные изменения автономно
- Не меняет QF pool mechanics после их объявления

### K.3 Hub-and-spoke в governance context

Все governance tasks роутятся через brigadier. Эксперты не общаются напрямую. Результат — task-return-packet с вариантами к Ruslan. Ruslan = финальный decision-maker.

Attention budget: max 20 активных governance tasks (RUSLAN-LAYER cap). При переполнении — brigadier логирует overflow, не создаёт новых задач.

---

## §L. Partner-extension hook — как партнёр форкает governance-модель под свой Clan

**Mondragón spawn pattern V4:** каждый Clan = автономная cooperative-ячейка с собственным Charter, связанная с Jetix общими принципами (не иерархией). Хакатоны — точка входа для потенциальных Clan Leads: участник видит модель в action и решает строить своё.

### L.1 Что форкается

Партнёр берёт:
- Charter template (§F.1) и адаптирует под свой Clan
- Stage Gate schema (SG-0..SG-7) — может добавлять gates, не убирать конституционные
- R12 8-вопросный checklist — обязателен; extension допускается
- Governance log schema — стандартный формат для совместимости
- Events playbook (опционально) — если Clan планирует собственные хакатоны; берёт QF mechanics template

### L.2 Что остаётся неизменным (конституционная инвариантность)

- R12 четыре action classes — нельзя убрать из Charter
- fork-and-leave 30-day notice — нельзя ужесточить (можно ослабить)
- wage ratio cap — можно сделать строже (3:1), не слабее без явного обоснования
- Corrigibility принцип — Clan Lead не может lock out членов
- Gamification: если Clan вводит engagement mechanics — influence-ethics paired check обязателен (R12 HIGHEST)

### L.3 Ethereum Phase 2+ spawn

Per-Clan opt-in: Clan разворачивает свой смарт-контракт (fork от Jetix base contract). Параметры: 75/25 split (configurable), 5:1 cap (configurable вниз, не вверх), exit token mechanics, QF pool address (если Clan организует events).

### L.4 Процесс spawn (V4)

1. Clan Lead (участник хакатона / бывший член / внешний партнёр) → discovery call
2. Clan Lead адаптирует Charter template → R12 review (Steward или Ruslan)
3. Clan ставит SG-0: «Charter написан + R12 passed»
4. После SG-0 — Clan автономен; Jetix = network peer, не иерарх
5. Edge: `{from: jetix, to: clan-slug, type: spawned, date: YYYY-MM-DD}`
6. Inter-clan optin: Clan может co-sponsor следующий хакатон, участвовать в cross-clan QF pool
7. Dissolution path: Clan Lead уведомляет Jetix (30-day notice); данные портируются; Charter archived

---

## Закрывающий раздел: зачем этот портфель именно сейчас

Direction #3 Бизнес — самый сложный из 16 directions V4, потому что у него тройная задача: (1) объяснить внешнему миру (партнёры/инвесторы/спонсоры), (2) обеспечить внутренний порядок (governance), (3) V4-new: масштабировать через Кланы и события без потери конституционного floor.

**V4 смещение центра тяжести.** В V3 Бизнес-direction был ориентирован на консультационную модель + governance документы. В V4 первичный revenue engine — Хакатоны (#16): они одновременно генерируют доход (events economics), создают Clan pipeline (участники → Clan Leads), тестируют геймификацию в реальном контексте (R12 HIGHEST), и строят спонсорскую базу. Это не «добавление ещё одного revenue stream» — это смена организующей логики.

**Кланы как масштабирование без иерархии.** V4 даёт Jetix способ расти не через найм и не через franchising, а через Clan spawn: каждый новый Clan = автономная cooperative-ячейка, которая усиливает сеть, не создавая управленческую нагрузку на центр. Jetix = «качалка/склад»: предоставляет инфраструктуру, берёт только agreed share, не контролирует.

**Геймификация (R12 HIGHEST) = новый риск и новый инструмент.** V4 явно включает геймификацию как engagement-механику бизнеса. Это риск: gamification плохо сделанная = extraction через psychological lock-in. Поэтому influence-ethics-expert auto-pair обязателен (Halt-Log-Alert при отсутствии пары). Правильно сделанная геймификация — Schelling coordination + QF mechanics + achievement recognition — создаёт реальную координационную ценность.

**GAP «create» остаётся критическим.** До публикации Charter v1 и 1-pager'а (§A.1) Jetix существует как внутренняя система без внешнего лица. В V4 это особенно острo: спонсоры хакатонов хотят видеть конкретный документ («что мы спонсируем»), потенциальные Clan Leads хотят понять «что мы форкаем». Charter v1 + 1-pager = максимальный рычаг.

**Следующий шаг:** Charter v1 текст + 1-pager (§A.1) + Events economics one-pager для спонсоров (§V4-delta.1) = три документа, которые разблокируют partnership, инвестиции, первую когорту и первый хакатон одновременно.
