---
title: "§6 Matchmaker Mechanics — Phase-by-Phase Coordination Architecture"
type: systems-integrator
produced_by: systems-expert
mode: integrator
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-06
section_ref: "§6 Matchmaker Mechanics"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
word_count_target: "≥1500 words"
confidence: high
confidence_method: F-G-R-coherence
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§1 acceptance predicate §6 section spec"}
  - {path: "decisions/JETIX-VISION.md", range: "D21 matchmaker + roy-replication; §13 phase timeline"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md", range: "§2.6 matchmaker; §6 gate evolution"}
  - {path: "raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md", range: "Voice 2 — matchmaker narrative verbatim"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md", range: "§2.2 Partner ICP"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md", range: "§5.3 Option C; §5.X recommendation; D21 roy-replication"}
investor_peer_input: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md (referenced — concrete KPI targets per gate will reside there)"
locks_cited: [D13, D15, D21, D22, D27]
acceptance_predicate: "count(phases) == 3 AND each_phase >= 400 words AND migration_triggers_named AND KPI_table_present AND systems_lens_applied (Beer_VSM + Senge_limits_to_growth + Meadows_leverage) AND ruslan_voice2_cited_verbatim AND count(F-G-R-tagged_claims) >= 3 AND dissents present"
anti_scope:
  - "NO §10 Secure Network architecture (sibling cell; reference digital portraits as input only)"
  - "NO §5 Alliance governance (sibling cell; referenced as context)"
  - NO Notion writes
  - NO provider-key env-var references
  - "NO Task() invocations (cross-cell forbidden per shared-protocols §6)"
---

# §6 Matchmaker Mechanics — Phase-by-Phase Coordination Architecture

> Этот раздел — один из 13 разделов финального документа `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md`.
> Он отвечает на вопрос: «как именно Jetix соединяет людей с задачами — сейчас, через год, и через пять лет?»
> Matchmaker — не фича. Это **центральный механизм ценности Alliance** для каждого участника.

---

## Системный фрейм: matchmaker как System-3 координатор

Прежде чем переходить к операционным деталям, полезно назвать, чем matchmaker является с точки зрения систем. В терминологии VSM (Beer, Stafford, «Brain of the Firm», book-as-frame), Alliance — это **жизнеспособная система**. У неё пять уровней. System-1 — это сами участники (специалисты, решающие задачи). System-2 — протоколы координации между ними. **System-3 — это matchmaker**: именно он осуществляет audit/optimisation-функцию, обеспечивая, что задача попадает к правильному специалисту, а не просто к ближайшему знакомому.

System-4 (intelligence/futures) — это трекинг того, какие задачи Alliance не умеет решать сейчас, но должен уметь в будущем. System-5 (identity/policy) — это Ruslan + методология Jetix: что Alliance в принципе делает и кем является.

Без работающего System-3 Alliance деградирует в общий чат, где каждый сам ищет помощь хаотично. С работающим System-3 Alliance становится infrastructure для cooperation, которая самоусиливается с каждым новым участником.

Критически важна вот эта VSM-диагностика: **на всех трёх фазах matchmaker остаётся System-3**. Меняется только то, насколько этот уровень населён: в фазе 1 System-3 = один человек (Ruslan), в фазе 2 System-3 = AI-агент с цифровыми портретами, в фазе 3 System-3 = формальный matching-портал с bid-механикой и escrow. VSM-структура остаётся идентичной; меняется её variety (в смысле Ashby). Именно это и есть правильная динамика масштабирования: сохранение структуры при росте разнообразия.

[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md#§5.3-VSM]

---

## §6.1 Phase 1 — Ручной режим: Ruslan матчит лично

### Механика «одного человека»

В голосовом сообщении (Voice 2, 2026-04-24) Ruslan описывает текущую версию matchmaker дословно:

> *«просто соединяется — надо какой-то сложный клиент, другому подрядчик — AI-агентами смазывается, происходит быстрее, качественнее, адекватнее, плюс фиксируется всё адекватно тоже. И вот так вот понемногу нарастают контакты — сперва ну то есть просто вот людям помогаем, помогаем, потом это нарастает мясом. Мы до стратегии тоже упоминаем что потихоньку в специалисты начинают работать с нами, переходят к нам.»*

[src:raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md#Voice2]

Ruslan формулирует это максимально просто: *«я могу уже сейчас делать одному»*. Это одновременно и сила Phase 1 (скорость запуска, нулевые транзакционные издержки), и её системный предел (один человек как System-3 — Ashby: variety контроллера не может превышать variety системы; при росте Alliance variety matchmaker начнёт отставать).

**Процесс в Phase 1 выглядит так:**

1. **Задача приземляется в поле зрения Ruslan'а.** Источники: прямое обращение клиента, сигнал в Telegram-чате Alliance, разговор на звонке, наблюдение за болями в Community. Никакого формального «тикета» — пока это неформальные каналы.

2. **Ruslan сканирует сеть ментально.** Он знает лично всех 5–20 участников Phase-1 Alliance. «Кто из них закрывал похожую задачу? У кого есть свободное время? Кто релевантен по архетипу?» — весь этот скоринг происходит в голове основателя. Это быстро (секунды), но непрозрачно и невоспроизводимо без Ruslan'а.

3. **Инициация соединения.** Форматы: Telegram-введение («Привет обоим, вот задача, вот специалист — разберитесь»), email intro (более формально, для клиентов-корпоратов), WhatsApp-сообщение. Текущей стандартной шаблонной формы нет — Phase-1 action: создать три типовых шаблона введения (Telegram / Email / WhatsApp) с понятным контекстом задачи, именами сторон, ожидаемым next step.

4. **Трекинг результата.** Сейчас — нулевой. Нет формального «этот матч произошёл, вот его статус». Ruslan помнит устно. Phase-1 minimal viable tracking: простая таблица (Airtable / Notion / даже markdown) с полями: дата матча, стороны, задача, статус (initiated / meeting held / delivered / fell through).

**Метрики в Phase 1 (цели для первого скорборда):**

| Метрика | Определение | Ориентир Phase 1 |
|---|---|---|
| Connections attempted | количество попыток матча в месяц | 5–10/мес (предел внимания одного основателя) |
| Acceptance rate | % матчей где обе стороны согласились встретиться | цель ≥70% (тёплая сеть даёт высокий acceptance) |
| Conversion to deliverable | % встреч которые привели к реальной сдаче работы | цель ≥40% (не каждая встреча — сделка) |
| NPS (обе стороны) | Net Promoter Score: рекомендовали бы матч? | цель ≥8/10 |

Конкретные числа по воротам G1–G5 будут дополнены из `swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md` (investor-expert peer-input draft).

**Системный предел Phase 1 — Senge «Limits to Growth» (Fifth Discipline, book-as-frame):**

Классический системный архетип: рост Alliance создаёт нарастающую нагрузку на matchmaker-ресурс (внимание Ruslan'а). До некоторого порога система растёт. Затем нагрузка превышает возможности балансирующего ресурса — рост замедляется и качество матчей падает. Если не ввести дополнительный ресурс (AI-агент, протокол, платформу), система достигает своего структурного потолка. Конкретный порог Phase 1: **~10 connection-событий/неделю**. При превышении этого уровня Ruslan-как-System-3 не успевает обрабатывать входящий поток без деградации качества введений.

[src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#Claim3]

**Failure modes Phase 1:**

- **Scattered network.** Связи не структурированы — нет портретов, нет тегов, нет searchable базы. Ruslan может не вспомнить нужного специалиста потому что не встречался с ним 2 месяца.
- **Weak follow-through.** Без трекинга Ruslan не знает, дошёл ли матч до доставки. Невидимые провалы — хуже, чем видимые.
- **No scoreboard.** Нет данных о том, какие типы задач система закрывает хорошо, какие — плохо. Нет основания для улучшения.
- **Single point of failure.** Если Ruslan занят, болен или в отпуске — matchmaking полностью останавливается. VSM: System-3 = одна нода без резервного маршрута.

**Leverage point Phase 1 (Meadows L5 — информационные потоки):** самое важное изменение, которое можно сделать прямо сейчас с минимальными ресурсами — **начать фиксировать каждый матч**. Не строить платформу, не нанимать агента — просто ввести скорборд. Это переводит matchmaker из «невидимого процесса в голове основателя» в «видимую обратную связь». Без этой информации система не может улучшаться. С ней — даже ручной процесс начинает самоулучшаться через обучение Ruslan'а на собственных паттернах.

```
Claim §6.1:
  claim: "Phase-1 manual matchmaker bottleneck fires at ~10 connection-events/week — это структурный
          предел одного основателя как System-3 VSM без AI-augmentation"
  F: F4  # operational convention; Senge Limits-to-Growth archetype + VSM L3 bandwidth reasoning
  ClaimScope: "holds for Ruslan-as-sole-matchmaker at current Alliance size (≤20 members);
               NOT valid past ~30 members where network scan becomes cognitively unmanageable
               regardless of hours invested"
  R: "refuted if matchmaker volume stays below 10/week even at 50+ Alliance members —
      would imply demand-side constraint, not supply-side;
      accepted when weekly connection-event log shows consistent friction at 10+/week"
```

---

## §6.2 Phase 2 — AI-Smoothed Coordination: агенты помогают коммуникации

### Механизм

Переход в Phase 2 (G1→G2, €50K–€200K gate, с проектированием начиная с G1) означает: **matchmaker-агент (L4) появляется как System-3 помощник**, но Ruslan остаётся на финальном утверждении.

Два ключевых пре-условия фазы 2:

1. **Цифровые портреты существуют** (Phase-2 design, §10 Secure Network — sibling cell). Без структурированных machine-readable профилей участников AI-агент не может предложить кандидатов — у него нет входных данных. Matchmaker Phase-2 потребляет digital portraits как топливо; архитектура самих портретов — в sibling cell §10.

2. **Скорборд фазы 1 накоплен** (как минимум 30–50 матчей с данными). Агент не стартует из ниоткуда — он обучается на том, какие матчи сработали, какие — нет. Без этого исторического сигнала рекомендации агента будут хуже ручных Ruslan'овских.

**Цикл работы в Phase 2:**

1. **Задача приземляется** — через формализованный intake (Telegram-бот, форма в Secure Network, или прямое сообщение Ruslan'у). Задача структурируется: тип (tech / content / strategy / research / legal и др.), срочность, требуемые навыки, бюджет-диапазон.

2. **Matchmaker-агент L4 предлагает топ-3–5 кандидатов** из базы цифровых портретов. Скоринг по четырём осям:
   - **Skill fit** — теги портрета совпадают с тегами задачи
   - **Availability** — портрет содержит заявленные доступные часы/неделю
   - **Past collaboration** — есть ли история совместной работы с задающим (warm vs cold match)
   - **Archetype fit** — архетип участника (из 11 JETIX-VISION §7.1) совпадает с типом задачи

3. **Ruslan просматривает предложение** — человек-в-петле (HITL). Одобряет, корректирует, отклоняет. Это не автономное решение агента — Ruslan остаётся на финале. D13 принцип: агент = open surface (видит портреты, предлагает кандидатов); закрытое ядро (тонкости отношений, нюансы репутации, стратегический выбор кого куда ставить) — у Ruslan'а.

4. **Агент готовит введение** — шаблонное письмо / Telegram-сообщение с контекстом задачи, профилями сторон, предлагаемым next step (например, «15-минутный call в течение 48 часов»).

5. **Агент координирует scheduling** — предлагает временные слоты, напоминает сторонам. Это экономит Ruslan'у 20–30 минут на каждый матч, что при 20 матчах/месяц = 7–10 часов/мес возвращённого architect-orbit времени.

6. **Агент создаёт shared workspace** (если задача перешла в стадию работы) — структурированный канал / папка / документ где стороны могут координироваться. Агент фиксирует статус, апдейты, завершение.

7. **Агент обновляет портреты** по результатам матча — добавляет к профилям запись «работал с X над типом задачи Y, статус: delivered/fell through». Это обратная связь, которая улучшает следующий скоринг.

**Метрики Phase 2:**

| Метрика | Определение | Цель Phase 2 |
|---|---|---|
| Match-rate | % задач где агент предложил принятого кандидата | ≥60% (investor peer-input даст точные числа) |
| Completion-rate | % принятых матчей где работа была сдана | ≥50% |
| NPS обеих сторон | раздельно: task-poster + specialist | ≥8/10 для обоих |
| Time-to-first-meeting | среднее время от intake задачи до первой встречи сторон | ≤72 часа |
| Ruslan-hours-freed | часов в месяц возвращённых из matchmaking в architect-orbit | ≥6 часов/мес |

Инвестор-эксперт дополнит числа в `swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md`.

**VSM-диагностика Phase 2:** агент занимает System-2/System-3 позицию совместно с Ruslan'ом. Ruslan остаётся на System-5 (policy/identity) и System-4 (intelligence — что за задачи Alliance не умеет решать?). System-3 теперь не одна нода, а human + AI система: Ruslan одобряет, агент исполняет. Это **повышение requisite variety (Ashby)**: контроллер-система теперь имеет больший variety чем один человек, что позволяет обрабатывать больший variety задач без деградации.

**Senge «Shifting the Burden» — ключевой риск Phase 2:**

Системный архетип: когда AI-агент начинает хорошо справляться с matchmaking, возникает соблазн **не развивать навык Ruslan'а** как человека-матчмейкера, а перекладывать всё больше на агента. Симптом: Ruslan перестаёт лично знакомиться с новыми Alliance-участниками, полагаясь на «агент разберётся». Последствие — деградация человеческой сети: агент знает портреты, но не знает отношений, контекста, недавних событий в жизни участников. Качество матчей снижается незаметно, потому что метрики показывают технический success (meeting scheduled) но не поведенческий (match felt right, trust was built).

Противоядие: **Ruslan продолжает лично встречаться с каждым новым Alliance-членом** в Phase 2 (не дольше 30 минут, достаточно для «почувствовать человека»). Агент — coordination tool, не relationship replacement.

```
Claim §6.2:
  claim: "AI-смазка matchmaker Phase 2 высвобождает ≥6 часов/мес Ruslan'а при 20+ match-event/мес,
          при условии что цифровые портреты структурированы и Phase-1 scoreboard накоплен"
  F: F3  # multi-case pattern: AI-assisted coordination tools in B2B marketplaces show 30-50%
         # coordination-overhead reduction; applied here at conservative 6h/mo estimate
  ClaimScope: "holds for Alliance size 20–100 active members with structured digital portraits;
               NOT valid if portraits are unstructured prose (agent cannot score);
               NOT valid if Ruslan-HITL approval time exceeds 5 min/match (bottleneck shifts)"
  R: "refuted if Phase-2 Ruslan-hours-freed metric stays below 4h/mo after 3 months of AI-matchmaker
      operation — would imply friction in human-HITL loop or poor portrait quality;
      accepted when rolling 3-month average of time-to-first-meeting ≤72 hours AND
      completion-rate ≥50%"
```

---

## §6.3 Phase 2+ → Phase 3 — Platform Mode: формальный matching-портал

### MVP спецификация

Порог перехода в Platform Mode: **Alliance >100 активных участников + ≥30 connection-событий/месяц** (подробнее в §6.4 ниже). При таком масштабе HITL-Ruslan как финальный одобритель становится новым узким местом: система имеет достаточную variety задач и участников, что её нельзя обрабатывать через единую личность-фильтр.

Platform Mode — это **публичный (для участников Alliance) интерфейс** с формализованными механиками:

**1. Поиск по портретам (Search over portraits)**

Участник Alliance публикует задачу через структурированную форму: тип, навыки, бюджет-диапазон, срочность, формат сотрудничества (разовый / retainer / проект). Платформа показывает ранжированный список специалистов, прошедших D22 ICP-фильтр, с историей реализованных матчей (reputation score). Просмотр портретов — только для верифицированных Alliance-членов, не публичный (D13 Closed core).

**2. Структурированный posting задач (Structured task posting)**

Стандартизированная карточка задачи: не свободный текст, а форма с полями. Это требование Alliance-Board (если выбран Option C Foundation из §5 — sibling cell): стандарт карточки задачи — один из первых методологических продуктов, которые Foundation публикует. Польза: агенты могут автоматически парсить карточки, портреты автоматически сопоставляются с требованиями без ручного скоринга.

**3. Bid-механика**

Для задач с открытым исполнителем (не персонализированным введением): специалисты могут «поднять руку» (bid) на задачу. Task-poster видит пул кандидатов, их reputation score, прошлые проекты. Выбирает — или получает рекомендацию от агента.

Важное ограничение: **AI-агент предлагает, человек финально выбирает**. Это не автономный рынок где алгоритм распределяет задачи. Phase 3 — human-final-decision, AI-assisted. Это соответствует D22 адекватности и cultural gravity Jetix: «умные люди, которые сами принимают решения, используя лучшие инструменты», не «роботы распределяют работу».

**4. Escrow**

Оплата задачи блокируется платформой при старте, высвобождается при acceptance task-poster'ом (или по таймауту с dispute-resolution). Escrow критичен для снижения transaction risk при работе между малознакомыми участниками Alliance. Phase 1 и 2 работают на доверии (люди лично знают Ruslan'а — это гарантия); Phase 3 escrow заменяет эту персональную гарантию институциональным механизмом.

**5. Reputation scoring**

Каждый completed матч генерирует NPS-запрос с обеих сторон. Оценки агрегируются в публичный (внутри Alliance) reputation score. Score влияет на ранжирование в поиске. Важно: score не является единственным фильтром — D22 5-критерийный ICP-фильтр предшествует любому reputation score. Человек, не прошедший D22, не попадает в Alliance вне зависимости от потенциального reputation.

**6. Интеграция с Secure Network sub-channels по архетипам**

Platform matchmaker не существует в изоляции — он интегрирован с Telegram-субсетями (Phase 2) / платформенными каналами (Phase 3) по архетипам. Когда задача требует «ресёрчера с опытом в fintech» — агент уведомляет ресёрч-субсеть, не весь Alliance. Это снижает signal-to-noise для каждого участника (они не видят нерелевантные задачи) и ускоряет нахождение кандидата.

**VSM в Phase 3:** к этому моменту System-3 (matchmaker) превращается в структурированную функцию с собственным staff (platform team), governance (match quality audit), и метриками. System-4 (intelligence) включает мониторинг: какие категории задач Alliance закрывает хорошо, какие — нет, где нужны новые специалисты. Это становится входом для Alliance onboarding stратегии (кого именно рекрутировать в Alliance следующими).

```
Claim §6.3:
  claim: "Platform-mode matchmaker (Phase 3) с escrow + reputation score + structured posting
          позволяет Alliance function без Ruslan-HITL на каждом матче,
          сохраняя human-final-decision архитектуру"
  F: F3  # multi-case pattern: Toptal, Lemon.io, YC Works — similar matching-platform mechanics
         # show viable operation without founder-HITL at 100+ specialists, 30+ monthly matches
  ClaimScope: "holds after Alliance achieves 100+ active vetted members;
               NOT valid if Alliance quality-gate (D22) is poorly enforced —
               escrow/reputation cannot substitute for community curation;
               holds for task types <€50K budget; very large engagements may require Ruslan return"
  R: "refuted if platform match-rate falls below Phase-2 match-rate after 6 months of platform operation
      (would imply platform friction exceeds human-coordination benefits);
      accepted when Phase-3 monthly match-events consistently ≥30 AND NPS both sides ≥8/10
      WITHOUT Ruslan involvement in individual matches"
```

---

## §6.4 Migration Triggers — когда переходить между фазами

Чёткие триггеры критичны, чтобы не перейти слишком рано (overpowered infrastructure without sufficient volume) и не слишком поздно (Ruslan-bottleneck сдерживает Alliance growth).

### Trigger 1: Manual → AI-Smoothed

**Сигнал:** matchmaking volume стабильно превышает 10 connection-events/неделю ИЛИ Ruslan субъективно чувствует cognitive overhead (не успевает думать о новых клиентах — занят введениями).

**Системная интерпретация (Meadows L6 — структура информационных потоков):** когда ручной matchmaker не успевает обрабатывать поток — это сигнал, что System-3 variety ниже variety входящих задач (Ashby). Leverage point: не нанять больше людей для ручного матчинга (L12 — параметр, слабый), а изменить информационную структуру (цифровые портреты + агент — L6, сильнее).

**Gate:** этот триггер соответствует G1→G2 gate (€50K выручки). Дизайн AI-смазки начинается при G1, реализация идёт в G1→G2 window. Конкретное: не ждать пока сломается — проектировать заранее, чтобы переход был без кризиса.

**Предварительные условия перехода:**
- Цифровые портреты для ≥15 Alliance-участников готовы (Phase-2+ design из §10 sibling cell)
- Phase-1 scoreboard накоплен: ≥30 матчей с данными
- Matchmaker-агент L4 написан, протестирован на исторических данных
- Ruslan провёл 1 full cycle (end-to-end) с агентом-помощником до «передачи рулей»

### Trigger 2: AI-Smoothed → Platform

**Сигнал:** Alliance >100 активных членов + ≥30 connection-events/мес стабильно (не пик, а baseline) + Ruslan-HITL approval создаёт очередь ≥3 дней на матч.

**Системная интерпретация:** при Alliance >100 участников количество потенциальных матчей растёт как N² (сеть Меткалфа). Даже AI-смазанный HITL не успевает. System-3 требует не «больше AI», а **формализации governance matchmaking** — это и есть переход в Platform Mode.

**Gate:** соответствует G2→G3 (€200K → €1M). Formalization unlock per D21.

**Revenue gates соответствие (D21 + §13 JETIX-VISION):**

| Gate | Revenue | Matchmaker Phase | Ключевое изменение |
|---|---|---|---|
| G1 | €0–€50K | Manual (Ruslan) | Скорборд введён; шаблоны созданы |
| G2 | €50K–€200K | AI-smooth design begins | Портреты проектируются; агент в разработке |
| G3 | €200K–€1M | AI-smooth production | Агент в работе; HITL Ruslan финально одобряет |
| G4 | €1M–$100M | Platform launches | Search + bid + escrow + reputation live |
| G5 | $100M+ | International scale | Cross-niche meta-coordination; multi-language |

[src:decisions/JETIX-VISION.md#§13]

---

## §6.5 KPI per Gate — целевые показатели

Конкретные числа (targets per gate G1–G5) будут дополнены из investor-expert peer-input draft (`swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md`). Ниже — структура KPI-фрейма; числа будут интегрированы в финальный документ.

| KPI | G1 (Manual) | G2 (AI-design) | G3 (AI-prod) | G4 (Platform) | G5 (Scale) |
|---|---|---|---|---|---|
| Match rate (attempted → conversation) | track/establish baseline | baseline known | ≥60% (investor to confirm) | ≥65% | ≥70% |
| Completion rate (conversation → delivered) | track/establish | baseline known | ≥45% | ≥50% | ≥55% |
| NPS task-poster | track | baseline | ≥8.0 | ≥8.5 | ≥9.0 |
| NPS specialist | track | baseline | ≥8.0 | ≥8.5 | ≥9.0 |
| Time-to-first-meeting | ad hoc | ad hoc | ≤72h | ≤48h | ≤24h |
| Ruslan-hours/match | 45–60 min | 30 min | 5–10 min (HITL) | ~0 (platform) | 0 |
| Monthly match-events | 5–10 | 10–20 | 20–30 | 30–100 | 100+ |

**Ключевой системный KPI, не отражённый в таблице:** «Network density» — % активных участников Alliance, участвовавших в хотя бы 1 матче за последние 90 дней. Если density низкая (< 30%), Alliance деградирует в пассивный список контактов, не в живую экосистему. Matchmaker — **основной инструмент поддержания density**.

---

## §6.6 Системные риски и leverage points

### Риск 1: Senge Law 2 — «Чем сильнее давишь, тем сильнее система давит в ответ»

Если matchmaker становится обязательным каналом для **всех** взаимодействий внутри Alliance (принудительный централизованный роутинг), участники начнут обходить систему напрямую. Это особенно вероятно среди архетипов «Предприниматели» (они не любят излишний bureaucracy). Обратная связь: чем больше давления на использование платформы → тем больше informal bypasses → тем меньше данных в системе → тем хуже reputation score → тем менее ценна платформа.

**Leverage point (Meadows L9 — delays в information loops):** matchmaker должен снижать транзакционные издержки, а не добавлять их. Это значит: использование платформы должно быть **быстрее, чем прямой DM**. Если это не так — платформа не нужна. Метрика: «удобнее ли постить задачу в платформе, чем писать Ruslan'у напрямую?» — это бинарный acceptance test.

### Риск 2: D13 информационная безопасность

Цифровые портреты содержат чувствительные данные: навыки, доступность, прошлые проекты. Alliance-participants ожидают, что эти данные не утекут за пределы Alliance. D13 (Closed core / Open surface): портреты = closed core, никогда не публичны, никогда не в поиске за пределами Alliance membrane.

**Leverage point (Meadows L5 — information gaps):** при онбординге каждого участника Alliance необходимо явно коммуницировать: «ваш портрет виден только верифицированным Alliance-членам, прошедшим D22». Это не просто юридический disclosure — это культурный контракт, который снижает friction онбординга.

### Риск 3: Reputation gaming

При наличии reputation score появляется incentive для artificial inflation — договариваться о взаимных положительных оценках, не отражающих реальное качество. Это разрушает information quality системы.

**Leverage point (Meadows L4 — структура self-organization):** reputation должен быть multi-dimensional (не один score) и частично верифицируем (deliverable artifacts linked to reputation entry). Сложнее игровыми манипуляциями надуть 3D-профиль с прикреплёнными артефактами, чем одну цифру.

---

## §6.7 F-G-R синтез ключевых claims

```yaml
claims:
  - claim: "Matchmaker = System-3 VSM-функция Alliance на всех фазах;
            масштабируется variety контроллера (manual → AI → platform), не структурой"
    F: F4
    ClaimScope: "holds for Alliance as viable system per Beer VSM;
                 assumes Alliance maintains System-5 identity (Ruslan + Jetix methodology)
                 and System-4 intelligence (tracking unmet task types) coherently"
    R: "refuted if Alliance VSM-structure analysis shows matchmaker operating at System-1
        (task execution) rather than System-3 (coordination audit) in practice;
        accepted if quarterly VSM review confirms matchmaker retains System-3 position"

  - claim: "Migration trigger Manual→AI-smooth: 10 connection-events/week является
            requisite-variety threshold для Ruslan-as-sole-matchmaker"
    F: F4
    ClaimScope: "holds assuming Ruslan invests 45-60 min per match (introduction + tracking);
                 40h/week Ruslan total; architect-orbit obligations claim ~20h/week;
                 remaining 20h/week for matchmaking = ~10 matches/week ceiling"
    R: "refuted if Ruslan systematizes manual matchmaking to <30min/match
        (would push threshold to ~15-20/week);
        accepted if connection-event log shows consistent friction starting at 8-10/week"

  - claim: "Senge 'Shifting the Burden' risk: AI-smooth matchmaker может стать
            permanent crutch, атрофируя human relationship-building Ruslan'а"
    F: F3
    ClaimScope: "holds if Ruslan stops personal onboarding meetings with new Alliance members;
                 risk amplifies as Alliance grows past 50 members (Ruslan no longer knows
                 everyone personally — AI portrait is only data he has);
                 less applicable if Alliance stays below 30 members"
    R: "refuted if Ruslan maintains ≥1 personal onboarding call per new Alliance member
        regardless of AI-matchmaker activity (counter-measure preserved);
        accepted as confirmed risk when match quality metrics start declining 3+ months
        after AI-smooth activation without corresponding explanation in data quality"
```

---

## §6.8 Preserved Dissents

### Dissent 1: Ruslan-as-bottleneck vs Platform-timing tension

**Source:** системный анализ VS голос Ruslan'а (Voice 2).

**Claim A (Ruslan-in-system):** Ruslan явно говорит «я могу уже сейчас делать одному» — это сильный signal что Phase-1 manual mode не является проблемой в его восприятии. Он видит matchmaker как organic growth: «нарастают контакты, помогаем, потом это нарастает мясом». Это bottom-up growth model, а не engineered-platform.

- F: F5 (прямая verbatim цитата первичного источника)
- ClaimScope: «holds as Ruslan's intent for Phase-1; uncertain for Phase-2 when volume grows»
- R: «refuted if Ruslan explicitly requests platform before 10-match/week threshold»

**Claim B (системный анализ):** Senge «Limits to Growth» предсказывает, что без явного trigger для перехода система будет «работать» дольше, чем оптимально — основатель адаптируется, сокращает качество матчей незаметно для себя, воспринимает деградацию как «нормально», пока не произойдёт видимый сбой. Trigger 10 match/week должен быть явным и заранее согласованным, не retroactive.

- F: F3 (Senge Law 1: «сегодняшние проблемы — вчерашние решения»; pattern применим)
- ClaimScope: «holds for single-founder systems with cognitive load constraints; less applicable if Ruslan deliberately builds slack capacity»
- R: «refuted if Ruslan operates at 15+ matches/week without quality degradation for 3 months»

**Оба тезиса сохранены.** Рекомендуемый тест: зафиксировать тригерный порог (10 match/week) как явный checkpoint в Phase-2 planning, чтобы переход был плановым, не кризисным.

### Dissent 2: Senge «Shifting the Burden» — AI-smooth как crutch

**Source:** integrator self-dissent (per shared-protocols §5.3).

**Claim (риск):** если Phase-2 AI-smooth matchmaker работает хорошо, у Ruslan'а появляется рациональный incentive НЕ инвестировать время в личные отношения с Alliance-членами — агент справляется. Краткосрочно это правильно (высвобождает время). Долгосрочно это атрофирует ту самую relationship-layer, которая делает Alliance уникальным vs безликого B2B-marketplace. Alliance становится похожим на Upwork с красивым брендингом — и теряет главное differentiator.

- F: F3 (Senge Law 4: «легкий путь обычно ведёт обратно»; применимо к automation-as-crutch паттерну)
- ClaimScope: «holds если Alliance-culture не защищает human-relationship norm явно; менее применимо если Alliance governance содержит explicit norm «Ruslan meets every new member»»
- R: «refuted if Alliance membership survey shows ≥80% participants feel personally known by Ruslan after 6 months of Phase-2 AI-matchmaker;
     accepted if same survey shows <50% — тогда Shifting-the-Burden подтверждён»

**Рекомендованное разрешение:** зафиксировать как Alliance-norm (не только как Ruslan-wish): каждый новый Alliance-participant получает 30-минутный personal onboarding call с Ruslan (или, в Phase-3+, с назначенным Alliance-coordinator). AI-агент не заменяет этот звонок — он облегчает всё остальное.

---

*End of §6 Matchmaker Mechanics. Cell C-06 complete. Ожидает brigadier integration gate.*
