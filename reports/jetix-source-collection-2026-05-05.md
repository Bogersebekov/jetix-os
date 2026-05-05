---
title: Jetix Source Collection — компактная сборка всех источников о Jetix Corp
type: source-collection
created: 2026-05-05
created_by: server CC (claude/jolly-margulis-915d34)
purpose: input для заполнения Документа 1B JETIX-CORPORATION-2026-05-05.md
parent_target: decisions/JETIX-CORPORATION-2026-05-05.md
parent_foundation: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Документ 1A LOCKED v1.0)
total_sources_scanned: ~30 (HIGH/MEDIUM priority pulled; remaining LOW priority indexed in Appendix only)
canonical_locked_count: 11 LOCKED (Workshop, TRM, Vision FUNDAMENTAL, Foundation Parts 1-11, Pillar C, RUSLAN-ACK Bundle 1-5, Wave D, BASE-MGMT 1A)
draft_count: ~7 (Vision-D1, Philosophy-D2, Plan-D3, Architecture-Working, Vision-of-System RUSLAN-LAYER, voice-extract, retrospective)
superseded_count: ~3 (legacy 8-layer architecture; "house" metaphor → workshop; old Mittelstand-only ICP frame)
sources:
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md  # LOCKED
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md  # LOCKED v1.0
  - decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md  # RUSLAN-LAYER (WIP)
  - decisions/JETIX-VISION.md  # D1 Identity Document (draft)
  - decisions/JETIX-PHILOSOPHY.md  # D2 (draft)
  - decisions/JETIX-PLAN.md  # D3 (draft)
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md  # 1A LOCKED v1.0
  - swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md
  - swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md
  - reports/retrospective_2025-05_to_2026-04.md
  - design/JETIX-ARCHITECTURE-WORKING.md  # 8-layer working draft
  - SYSTEM-DESIGN-HUMAN.md  # v1-beta-FINAL 2026-04-18 (root, not in design/)
  - wiki/ideas/jetix-*.md  (10 entries)
  - wiki/concepts/{korporaciya-startup,jetix-open-source-principles,curated-community-access,founder-isolation,digital-sovereignty,value-three-layers}.md
gaps_flagged:
  - swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md  # NOT FOUND (mentioned in 1B sources frontmatter but file absent on filesystem)
  - design/SYSTEM-DESIGN-HUMAN.md  # NOT in design/; actual location is repo root
  - decisions/JETIX-FPF.md  # NOT in decisions/; actual location is design/JETIX-FPF.md
F: F3
G: jetix-source-collection-draft
R: refuted_if_quote_attribution_inaccurate
---

# Jetix Source Collection

> Компактная сборка ключевых тезисов / цитат / фактов о Jetix Corp из всех актуальных источников. Используется как input для Документа 1B JETIX-CORPORATION.
>
> **Принципы экстракции:**
> - Каждый тезис attribution `[src: path:section]`.
> - Компрессия 1-3 предложения; не полный dump.
> - **⚠️ Conflict:** между источниками отмечен явно.
> - **🟡 Possibly stale:** для >3мес или superseded материала.
> - **❌ Outdated frame:** для "Mittelstand DACH 50-500 emp" — Ruslan отверг этот ICP.
> - НЕ дублирует universal Foundation (это в Документе 1A).

---

## 0. Executive Summary

**Что такое Jetix согласно собранным источникам:**

Jetix — это **applied use case Базовой Системы Управления** (Документ 1A). Каркас (Foundation v1.0 LOCKED 2026-04-28: 11 Parts + Pillar A/B/C) — universal. Jetix — конкретная реализация под текущую ситуацию Ruslan'а (Berlin, solo founder, Phase 1 €50K Q2 2026 → trajectory $1T).

**Главные тезисы (через несколько слоёв формулировок):**

1. **Jetix = мастерская для работы с информацией** — canonical metaphor LOCKED 30.04 [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§1]. Заменила старую метафору «дом» из foundation-master-overview-human-2026-04-29 §1.
2. **Jetix = методология + operating system** — методология превращения AI-рычага в cascading-leverage [src: decisions/JETIX-VISION.md:§4]. Методология (база) + OS (overlay) = единый identity.
3. **Jetix = Total Resource Management (TRM)** — управляющая компания нового типа, управляющая 6 ресурсами клиента (финансы / время CEO / аудитория / знания / compute / команда) с mgmt fee + performance fee [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§1].
4. **Jetix = корпорация-стартап** — стартап-аппарат с ответственностью за «сотни тысяч людей и миллионы $»; параллельно развивает другие стартапы [src: wiki/concepts/korporaciya-startup-concept.md:одна-строка].
5. **Jetix = эволюция в 3 фазы:** одна мастерская одного владельца → команда → community мастерских [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6]; в TRM-терминах: сервисная компания → управляющая компания → платформа TRM Network [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.1].

**Главная амбиция:** мировой рекорд по скорости достижения $1T market cap (precedent: XEI / 2 года до $100B) [src: decisions/JETIX-VISION.md:§14]. Это **engineering-faith bet**, не pyramid / hype [src: holding-vision-2026-04-21:Note 5].

**Текущая фаза:** Phase 0/1 transition. €5K на счету (2026-04-21), цель €50K к 30.06.2026 (единственная committed absolute date). Trajectory: €50K → €200K validation → €1M → $100M → $100B → $1T.

---

## 1. Что такое Jetix — все имеющиеся определения

> Собраны все формулировки one-liner и развёрнутых определений из источников. Каждая с attribution.

### 1.1 Workshop / Мастерская (canonical, LOCKED 30.04)

> «Jetix = мастерская для работы с информацией. Мастерская с кучей профессиональных работников и кучей станков/инструментов любого калибра.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§0 TL;DR]

> «Главная фишка — continuous capability expansion: быстро внедряет новые станки/инструменты, работники быстро изучают новое, переиспользует наработки с других направлений.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§0 + §1.2]

> «Вход = информация, выход = информация (другая, переработанная, ценная).»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§0 + §4]

**Verbatim Ruslan (30.04):**
> «Это вот эта система Jetix... это мастерская с кучей профессиональных работников и с кучей станков инструментов любого калибра.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 1]

> «Это мастерская для работы с информацией.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 3]

### 1.2 Methodology + Operating System (D1 Vision, 21.04)

**Tagline:**
> «Jetix — методология превращения AI-рычага в mass-scale cooperation и personal sovereignty.»
> [src: decisions/JETIX-VISION.md:§1 Tagline]

**Verbatim Ruslan voice anchor:**
> «Jetix это методология, ёбаная. Это не просто какая-то программа, ещё что-то, нихуя. Это ёбаный метод, блядь. Понимаешь? Это, сука, уровень повыше.»
> [src: decisions/JETIX-VISION.md:§1, audio_502]

**Elevator pitch:**
> «Jetix — методология и operating system превращения AI-рычага в cascading-leverage (жизнь → проекты → знания → мышление → технологии) для умных, driven, skin-in-game людей. Воплощается в Phase 1 как консалтинг + продюсерский центр для English-speaking infobiz; в Phase 2+ как Secure Network — платформа для профессионалов, cooperating вокруг AI-augmented knowledge work; в Phase 3+ как enterprise-fast холдинг уровня USB-C universal connector в AI-и-бизнес пространстве.»
> [src: decisions/JETIX-VISION.md:§1 elevator pitch]

**Core identity (D8 LOCKED layered identity):** Jetix — один объект с разными лицами per observer + phase.
- Для Ruslan (self): Methodology + OS (всегда)
- Для клиентов: Company / Agency consulting (Phase 1)
- Для партнёров: Network / Platform / Secure Network (Phase 2+)
- Для community: Club Kingsman inside (всегда)
- Для external world: Corporation, "имеет вес" (Phase 2+)
- Phase 3+: USB-C universal connector + Holding
- Phase 4 / 200y horizon: Civilizational infrastructure
[src: decisions/JETIX-VISION.md:§4 Decision 8]

### 1.3 AI-native Operational Corporation (1B skeleton placeholder)

**1B skeleton предлагает one-liner candidate:**
> «Jetix — AI-native operational corporation которая использует Базовую Систему Управления как core infrastructure для предоставления Total Resource Management услуг Mittelstand клиентам в DACH.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§1.1]

**❌ Outdated frame** (см. §7 ниже): "Mittelstand DACH" ICP — Ruslan отверг этот frame; новый ICP = 2 оси × 3 типа участников. One-liner candidate в 1B skeleton требует переформулировки.

### 1.4 Корпорация-стартап (D29 / wiki/concepts)

> «Jetix позиционируется не как фрилансер и не как "ещё один стартап", а как корпорация-стартап: стартап-аппарат с ответственностью за сотни тысяч людей и миллионы $, который параллельно развивает другие стартапы.»
> [src: wiki/concepts/korporaciya-startup-concept.md:суть-в-одной-строке]

> «делает все то же самое что успешные стартапы (V-Work, сериалы типа 'Замри и гори'), но онлайн, ответственно, качественно и быстро.»
> [src: audio_537@26-04-2026, цитировано в korporaciya-startup-concept.md]

> «Jetix будет стартапом, который развивает другие стартапы.»
> [src: audio_537@26-04-2026]

**Свойства:**
- Ответственность как масштаб — не "клиенты", а "сотни тысяч людей и миллионы $".
- Корпорация = качество процессов; стартап = скорость и адаптивность.
- Online-first и автоматизация поддерживают корпоративное качество при стартап-скорости.
- Meta-leverage: помогать другим стартапам = создавать сеть, в которой Jetix — узел.
[src: wiki/concepts/korporaciya-startup-concept.md:ключевые-свойства]

### 1.5 USB-C Universal Connector (Decision 20, Phase 3+)

> «Jetix existing на уровне USB-C в electronics. Универсальный протокол подключения AI-агентов, бизнесов, specialists. Не монополия (USB-C работает с любым vendor), а standards-level interoperability.»
> [src: decisions/JETIX-VISION.md:§5 Phase 3+]

**Verbatim:**
> «Jetix будет настолько охуенен… он будет на уровне вот USB-C существовать.»
> [src: holding-vision-2026-04-21 Note 3, цитировано в JETIX-VISION.md:§14]

### 1.6 Дорога / инфраструктура metaphor (alternative, parallel)

> «Jetix — дорога, люди и бизнесы — разные машины (трактор, Porsche, самолёт). Без дороги машины бесполезны, без машин дорога бесполезна.»
> [src: wiki/ideas/jetix-as-infrastructure-metaphor.md:одна-строка]

**Pitch:** «Мы не ваш конкурент. Мы инфраструктура, на которой вы быстрее.»
[src: wiki/ideas/jetix-as-infrastructure-metaphor.md:приложения]

🟡 **Possibly stale alternative metaphor.** Workshop concept (30.04 LOCKED) — canonical. "Дорога/машины" (16.04) — раннее формулировка, может coexist как parallel framing для partners-as-vehicles dimension.

### 1.7 Foundation для AI-native operational company (8-layer architecture, 18.04)

> «Jetix — это AI-native operational company, где один человек (Ruslan) выполняет 7 функций большого бизнеса через 12 AI-ролей, собранных в 7 слоёв на одном git-репозитории.»
> [src: design/JETIX-ARCHITECTURE-WORKING.md:§4.1]

🟡 **Possibly stale.** 8-layer model (раннее formulation 18.04) предшествует Foundation v1.0 LOCKED 28.04 (11 Parts + Pillars). Концептуально совместимо но vocabulary устарел.

### 1.8 Ruslan «бульдозер для работы с информацией» (proto-canonical, 30.04 утро)

> «первое сейчас еще дописываю вот именно это бульдозер для работы с информацией я его описываю»
> [src: raw/transcripts/audio_582@30-04-2026_18-12-09.txt:L6, цитировано в voice-extract:§1.1.4]

🟡 **Iterational variant**. Audio_582 18:12 — 22 минуты до audio_583 18:34 где finalised «мастерская». Iteration: бульдозер → купол → мастерская (final canonical).
[src: voice-extract-workshop-people-2026-05-01.md:§1.1.4 + §1.9.2]

### 1.9 Сводное определение

**На основе всех формулировок** (NOT yet locked в 1B):

Jetix Corporation — **applied use case** Базовой Системы Управления (Foundation v1.0 LOCKED 28.04). На уровне metaphor: **мастерская для работы с информацией**, специализированная под текущую ситуацию Ruslan'а. На уровне offering: **методология + operating system + Total Resource Management** для smart entrepreneurs. На уровне ambition: **enterprise-fast корпорация-стартап** на trajectory $1T market cap. На уровне идентичности: layered identity — разные лица для clients / partners / community / external observers, единая internal грамматика.

---

## 2. Метафора Мастерской — все материалы

### 2.1 Почему именно мастерская (не дом, не оркестр, не город)

> **Дом:** статичный объект (отвергнут).
> **Оркестр:** один дирижёр + исполнители по нотам — не подходит, у Jetix владелец задаёт направление, агенты = инструменты (отвергнут).
> **Город:** слишком большой (отвергнут).
> **Организм:** слишком биологический (отвергнут).
> **Мастерская:** ✓ потому что (1) что-то делается — постоянный активный процесс; (2) есть мастер + работники + инструменты; (3) есть конкретные deliverables; (4) adaptive — переучивается, ставит новые станки; (5) knowledge accumulates.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§1; foundation-master-overview-human-2026-04-29.md:§1]

🟡 **Note:** старая метафора «дом» из `foundation-master-overview-human-2026-04-29.md §1` LOCKED 28.04, но **superseded 30.04** Workshop concept (см. JETIX-WORKSHOP §9 Action: «заменить на Мастерская / создать v2 файл»).

### 2.2 Главная фишка — continuous adaptability / capability expansion

> «Главный главный прикол в том что эта мастерская довольно быстро может там какие-то новые станки к себе внедрять какие-то новые эти новые инструменты внедрять работники могут быстро что-то новое изучить или наоборот вот эта мастерская может там как-то использовать уже текущие наработки с других направлений.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 2]

**Это adaptability — главный moat.** Конкуренты с фиксированной capability отстают; Jetix эволюционирует с каждым cycle.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§1]

### 2.3 Что такое «информация» в Jetix (NOT строгое CS-определение, функциональное)

«Информация» — это почти всё, что осмысленно попадает в систему:
- Информация о рынке (анализ ниш, конкуренты, opportunities)
- Информация о личном самочувствии (Life-OS, health log, energy)
- Информация о финансах (счета, runway, cash flow)
- Информация о возможностях в мире (партнёрства, новые tech, события)
- Информация «как нужно что-то делать» (методологии, best practices, playbooks)
- Информация-инсайт (новые идеи, синтезы, observations)
- Информация о задачах / целях
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§2]

**Принцип:** у каждого мастера / владельца **свой набор релевантной информации** — у инвестора одно, у психолога другое, у маркетолога третье.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§2 + §5]

### 2.4 Роль владельца — adaptive (5 ролей)

| Роль | Что делает |
|---|---|
| **Управляющий** (default, главная) | задаёт стратегию, распределяет ресурсы, определяет направление |
| **Мастер за станком** | сам сидит и делает работу |
| **Исследователь нового станка** | разбирается в новом tool / framework / agent |
| **Фильтр входящей информации** | решает что попадает в систему (Part 2 STOP-gate human ack) |
| **Перенастройщик workflow** | меняет процессы, добавляет hooks, переписывает agent prompts |
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§3]

**Verbatim Ruslan:**
> «Я как вот владелец могу играть вообще разные роли которые я хочу я могу играть как вот такой управляющий этой мастерской но это самая первая важная роль в любом случае но точно также я могу быть одним из мастеров я могу идти разбираться в новом станке я могу за этим станком сидеть работать я могу фильтровать какая информация попадает в станок какая нет я могу рабочие процессы переустанавливать.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 4]

**Cadence + mechanism роли-switch (refinement из voice-extract):**
- Cadence — ~2 hours per role-context switch
- Mechanism — записывать «где ты кто» для quick re-entry
- Trigger — project switch (не mood switch)
[src: voice-extract-workshop-people-2026-05-01.md:§1.1.3, audio_565@27-04-2026_14-41-06]

### 2.5 Input → System → Output — всё информация

**Input:** через **фильтр** (Part 2 STOP-gate) попадают только гипотезы / observations / запросы / сырые данные / идеи. «Всякое дерьмо в систему не попадает.»
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§4 Input]

**Internal:** информация (a) адекватно работает (provenance, F-G-R, structure); (b) переливается между частями (typed edges); (c) не теряется / не засыхает (compound learning); (d) AI не трогает важное / не обосрал (constitutional rules, Default-Deny, Human Gate).
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§4 Internal]

**Output:** информация переработанная — план / инсайт / навык / рабочая программа / готовый deliverable.

| Вход | Что система делает | Выход (тоже информация) |
|---|---|---|
| Гипотезы | анализирует, синтезирует | План действий |
| Сырые данные + контекст | находит паттерны | Новый инсайт |
| «Хочу научиться X» + материалы | структурирует, прорабатывает | Новый навык в голове |
| Specs + cycles | строит, тестирует | Рабочая программа |
| Task | делегирует, координирует | Готовый deliverable |
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§4]

### 2.6 Specialization — каждый мастер свой

> «У каждого мастера / владельца — своя специализация: один — под инвестиции; второй — под психологию; третий — под R&D... Foundation v1.0 — fork-portable. Структура одна. RUSLAN-LAYER (специализация) — заменяема.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§5]

**Master vs non-master entry filter (refinement из voice-extract):**
> «это все описание одного и того же мастер и не мастер профи и не профи… в этого мастера есть опыт есть возможно нужные инструменты есть возможно not понимание и знания как нужно делать какой последовательности… а который не может это не профессионал»
> [src: voice-extract-workshop-people-2026-05-01.md:§1.6.1, audio_583@30-04-2026]

**Demand mechanism (refinement):**
> «профессионалы… любят использовать профессиональные инструменты. И это тоже во всем... один раз попользовавшись качественным инструментом не хочется уже дерьмом каким-то пользоваться»
> [src: voice-extract-workshop-people-2026-05-01.md:§1.6.2, audio_585@30-04-2026]

**Breadth (refinement):**
> «можно быть профессионалом и в выгуле собак, блядь. И можно быть профессионалом в винах… и в готовке и в спорте короче где только где только угодно.»
> [src: voice-extract-workshop-people-2026-05-01.md:§1.6.3, audio_586@30-04-2026]

### 2.7 Эволюция фаз — от одного к community (3 фазы)

**Phase 1 — мастерская одного владельца (текущее)**
- Один владелец + AI агенты = команда мастерской.
- Может делать сложные задачи: исследования, анализ, синтез, generation.
- Накапливает knowledge, специализируется на нише.
- «Это уже довольно охуенная мастерская» (verbatim Ruslan 30.04).
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 1]

**Phase 2 — команда работает с одной системой**
- Несколько человек + AI + одна Jetix-мастерская.
- Workflow тот же (информация-centric).
- Цель командная.
- Система чуть-чуть улучшается под team scenarios.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 2]

**Phase 3 — community мастеров с мастерскими (mega-system)**
- Когда задачи слишком сложные для одной мастерской.
- Мастер берёт **кусок задачи** в свою мастерскую → разбирает → выдаёт **одну качественную деталь**.
- Все детали собираются на верхнем (community) уровне в **finished product**.
- Это тоже информационный flow: получили информацию (часть задачи) → выдали информацию (свой результат).
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 3]

**Verbatim:**
> «Когда уже будет комьюнити таких вот мастеров с своими мастерскими можно будет делать уже мега систему в которой внутри вот эти мастера у которых есть мастерские смогут между собой коммуницировать и работать над уже более сложными проектами задачами для которых одной мастерской даже прям хорошо настроенной но одной мастерской одного человека не хватит.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 13]

**Phase transitions concrete triggers:**
- **Phase 1 → 2 trigger:** «foundation готов» (audio_562@27-04-2026): «Мы сейчас заканчиваем этот фондейшн… это, по сути, уже готовый продукт. Это можно уже давать идти людям.» [src: voice-extract-workshop-people-2026-05-01.md:§1.3.1]
- **Phase 1 → 2 mechanism:** «соло консультант → партнёры приводят», audio_536: «для начала я хочу это вот самостоятельно Как такой бизнес-консультант… попутно Уже сразу накапливать команду… уже эти партнеры За меня другим партнером помогали Будь то финансами Будь то ресурсами» [src: voice-extract:§1.3.2]
- **Phase 3 trigger:** «когда задачи > одной мастерской», audio_576@29-04-2026 [src: voice-extract:§1.3.3]

### 2.8 Visual / View principle — программирование с визуальным редактором

**Аналогия:** код (физическая реальность) + visual view в IDE (концентрированное представление).

Jetix даёт **view** на: дома (недвижимость), людей (CRM), машины (assets), проекты, задачи, ресурсы. **Не смотришь на всё физическое одновременно — это перегрузка.** Смотришь на view, который система собрала.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§7]

**Verbatim:**
> «именно система позволяет вот это посмотреть это как бы конкретно то что есть и удобно этим пользоваться передвигать чтобы не смотреть на все свои дома всех своих людей все свои машины ты отдельно смотришь на вот этот view который тебе дает система и тебе это позволяет удобнее этим всем распространять спряжаться это использовать мастерить.»
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 14]

**Refinement #1: Visual = cognitive offload, не display.**
> «но если ты этим управляешь записывать себе где ты кто просто чтобы тебя быстрее входить в эту роль… просто потому что думать о блять перед глазами записано казалось бы казалось бы но это ебать насколько вообще улучшает дать облегчает.»
> [src: voice-extract:§1.4.1, audio_565@27-04-2026]

**Refinement #2: View dual-direction — internal navigation + external accountability** (public dashboard).
> «сразу же надо будет сделать сайт получается как раз смотрите можете по всем метриком следить за компанией»
> [src: voice-extract:§1.4.2, audio_553@26-04-2026]

### 2.9 Mapping старых cluster names → новые workshop language

| Старая метафора (house) | Новая метафора (workshop) |
|---|---|
| 🏗 Подвал — Substrate (P1 git) | 🏭 Фундамент мастерской — git как основа |
| 🛡 Несущие стены — Governance (P6a/6b) | 🚨 Охрана + правила безопасности — Provenance + Human Gate |
| 📚 Кладовая — Knowledge (P2/P3) | 📋 Приёмная + Склад материалов и чертежей — Triage + Wiki |
| ⚙ Рабочие комнаты — Work (P4/P5/P7) | 🔨 Рабочие столы + Станки + Workflow — Coordination + Compound Learning + Project Lifecycle |
| 🚪 Гостиная и дверь — Interaction (P8/P9/P10) | 📞 Front-office + Радиосвязь — Health + Owner Interaction + External |
| 🎯 Стол стратегии — Strategy (P11/Pillar C) | 🗺 Планировочный стол + Свод правил — Strategic Direction + Principles |
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§10]

### 2.10 Workshop "примеры станков" (детализация из voice-extract)

**Polный набор корпоративного toolkit (audio_565):**
> «полный набор нахуй мега корпорации в одной в одной блять программки в jetix… лучшая research и лучшая блять аналитика up to date… лучшая crm… лучшая блять автоматизация… сбор твоих знаний… ёбаный нож швейцарский нож в виде в мире с Jetix. Это ебаный космический корабль»
> [src: voice-extract:§1.1.2, audio_565@27-04-2026]

**Расширенный список (audio_557):**
> «лучшее блять инвесторы лучшие юристы лучшая блять защита лучше блять токены лучше нахуй автоматизация лучше сука люди лучше блять рестораны лучше переговоры блять лучше возможности»
> [src: voice-extract:§1.2.1, audio_557@26-04-2026]

**Personal-development станки (audio_543):**
> «у нас лучшие психологи помогают тебе себя там раскрыть блять проанализировать… потом лучше нахуй маркетологи себя блять а брендить нахуй о упаковать… лучшее блять трекеры помогают тебе дальше развиваться»
> [src: voice-extract:§1.2.2, audio_543@26-04-2026]

### 2.11 Knowledge accumulation discipline (Workshop infrastructure)

> «сбор твоих знаний сукка сохранения твоих знаний… ничего не будет стоить если это самого первого дня и начала как бы сохранять адекватно потом можно просто будет на блять скопируй сразу… с одной ниши в другую короче перетаскивать»
> [src: voice-extract:§1.8.1, audio_565@27-04-2026]

**Mechanism:** (a) save from day 1; (b) cross-niche portability via copy-and-adapt; (c) base layer for compound learning.

### 2.12 Mafia-style closed-circle Phase 1 trust (refinement)

> «именно для начальной стадии вот джекса что мы все-таки будем действовать больше как мафия то есть мы там собрались какие-то свои ресурсы собрали хорошо бизнес там работа да есть это свободные ресурсы инвестируем»
> [src: voice-extract:§1.9.4, audio_563@27-04-2026]

**Trust structure Phase 1 → Phase 2:** closed-circle mafia-style, **NOT open community**. Phase 3 evolves from this.

### 2.13 Genesis quote — "танк в мастерской" (proto-Workshop, 27.04)

> «сделать что-то в этом в мастерской наверное легче, да, танк в мастерской сделать со всеми инструментами и, блядь, ресурсами, чем это сделать, блядь, на поле битвы, когда тебя, нахуй, 10, блядь, проблем отвлекает»
> [src: voice-extract:§1.1.1, audio_565@27-04-2026]

Workshop = safe controlled environment где можно создать сложный артефакт ("танк") в отличие от хаоса "поля битвы" (real-world execution). Первое explicit использование «мастерская» metaphor ДО canonical 30.04.

---

## 3. TRM — Total Resource Management

### 3.1 Что такое TRM

> «Классические управляющие фонды (BlackRock, Bridgewater, family offices) управляют только одним типом ресурса — деньгами. Между тем у предпринимателя/компании есть как минимум 6 видов исчерпаемых, монетизируемых ресурсов.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§1]

**Тезис:** Jetix управляет всеми шестью одновременно — берёт комиссию (mgmt fee + performance fee) с каждого. Это превращает консалтинговую модель в управляющую компанию нового типа — **Total Resource Management (TRM)**.

### 3.2 6 ресурсов

| # | Ресурс | Что значит |
|---|--------|-----------|
| 1 | 💰 **Финансы** (capital) | Кэш, инвестиции, рабочий капитал |
| 2 | ⏱️ **Время CEO/основателя** (founder time) | Часы внимания первого лица — самый дефицитный ресурс |
| 3 | 📢 **Аудитория** (audience) | Подписчики, контакты, рассылки, репутационный капитал |
| 4 | 📚 **Информация / знания** (knowledge) | Внутренние данные, экспертиза, методологии, накопленный опыт |
| 5 | 💻 **Вычислительные мощности** (compute) | GPU/CPU, AI-инференс, токены, серверная инфраструктура |
| 6 | 🤝 **Команда / человеческий капитал** (talent) | Сотрудники, их время, их компетенции |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§1]

### 3.3 Почему TRM работает именно сейчас (3 волны)

1. **AI-агенты как операционный слой** — раньше управлять временем 10 CEO одновременно было невозможно; AI-агенты позволяют одному управляющему + флоту агентов параллельно держать в голове состояние десятков клиентов. Compute стал ресурсом, который масштабируется и сам становится продуктом.
2. **Mittelstand перегружен** — немецкие средние предприятия завалены AI-внедрением, EU AI Act, кадровым кризисом, наследованием, цифровизацией. Нужен не консультант, а **operator**.
3. **Падающее доверие к консалтингу** — Big 4 продают слайды. Performance-based модель Jetix отвечает на этот запрос. TRM — финальная форма: «мы не просто внедряем, мы управляем твоими ресурсами и делим прибыль».
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§2]

❌ **Outdated frame note:** "Mittelstand перегружен" — Ruslan отверг "Mittelstand DACH" как ICP (см. §7). Сама **аналитическая основа** (любой средний бизнес перегружен AI) остаётся валидной, но не привязывать к DACH географии или manufacturing вертикали.

### 3.4 Уже существующие аналоги (по каждому ресурсу)

> «Ни одна компания не делает всё одновременно, но по каждому отдельному ресурсу есть состоявшийся рынок с понятной экономикой. Это значит, что синтетическая комбинация имеет шанс быть рабочей.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§3 intro]

| Ресурс | Аналоги | Модель | Ключевые игроки |
|---|---|---|---|
| Финансы | Wealth Management, Family Offices | AUM 0.5-2% + 10-20% performance | BlackRock, UBS Wealth, Bridgewater |
| Время CEO | Fractional COO, EOS Integrator, Chief of Staff | Retainer $5-25k/мес + equity | ScaleUpExec, EOS Worldwide, Chief Outsiders (257K компаний на EOS) |
| Аудитория | Talent / Creator Management Agencies | 15-25% revenue share | WME, CAA, UTA, Night Media, Jellysmack, Whalar |
| Информация | Knowledge Mgmt + Holistic Wealth (extended) | Часть holistic financial planning | Mercer, Deloitte HC; **зазор → открытое окно для Jetix** |
| Compute | AI Compute Brokers / GPUaaS | Маржа 15-30% | Together AI, Anyscale, RunPod, Lambda Labs |
| Команда | Talent / HR Outsourcing, Fractional Executives | 15-30% от ФОТ либо markup | Toptal, Andela, ADP, Mercer, Deloitte |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§3.1-§3.6]

### 3.5 Что нет ни у кого (зазор Jetix)

> «Универсальный «total resource manager», который объединяет все шесть ресурсов под одним договором, на одной аналитической платформе, с единой комиссионной моделью. Это белое пятно. Если Jetix туда зайдёт — это новая категория.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§3.7]

### 3.6 Бизнес-модель — Mgmt fee + Performance fee

**A. Management fee (плата за управление, идёт независимо от результата):**
- 0.5-1% годовых от размера ресурса под управлением (для финансов и compute)
- $X тыс./мес фиксированно (для времени CEO)
- 10-15% от monetization revenue (для аудитории)

**B. Performance fee (плата за результат, % от прироста прибыли клиента):**
- 15-25% от incremental profit
- Считается по сравнению с baseline (доход клиента до начала управления, индексированный на рост рынка)
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.1]

### 3.7 Пример расчёта на одном клиенте (TRM-full)

**Клиент:** немецкий Mittelstand, машиностроение, выручка €50M, EBITDA €5M.

❌ **Outdated example frame:** "немецкий Mittelstand машиностроение" — illustration only; Ruslan отверг этот ICP. Числа per-resource остаются валидной calculation methodology.

**Jetix берёт под управление:** €5M AUM (финансы), 8h/нед (время CEO), 12k+3k подписчиков (аудитория), вся внутренняя база, €15k/мес AI-инфра, 3 ключевых человека.

**Годовая выручка Jetix:**

| Уровень | Ресурс | Логика | Сумма |
|---------|--------|--------|-------|
| Mgmt | Финансы €5M × 0.75% | стандарт wealth mgmt | €37.5k |
| Mgmt | Время CEO (fractional COO часть) | €8k × 12 мес | €96k |
| Mgmt | Аудитория | 15% от monetization | €15k |
| Mgmt | Информация | retainer | €36k |
| Mgmt | Compute | 15% маржа на €180k/год | €27k |
| Mgmt | Команда | retainer | €60k |
| **Σ mgmt fee** | | | **€271.5k/год** |
| Performance | 20% от incremental EBITDA (€5M→€7M = +€2M) | | **€400k** |
| **Σ с клиента** | | | **~€670k/год** |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.2]

**Comparison vs traditional consulting:** один TRM-full клиент = эквивалент 5-6 классических консалтинговых проектов.

### 3.8 Масштабирование

- 10 клиентов TRM = €5-7M ARR
- 30 клиентов TRM = €15-20M ARR (территория «AI consulting unicorn» по выручке)
- Recurring revenue + scale с ростом клиента (не Jetix) → valuation мультипликатор 1-3× (консалтинг) → 5-10× (asset mgmt) → 10-20× (платформа)
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.3]

### 3.9 Архитектура — каждый ресурс = отдельный модуль (мини-фонд)

```
JETIX TRM PLATFORM (core) — единая аналитика, dashboard, отчёты, billing
   ↓
[Fin fund | Time fund | Aud fund | Info fund | Comp fund | Team fund]
   ↓
JETIX OS (12 agents, 6 departments) — Operations, Sales, Growth, Support, Leadership
```
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§5]

### 3.10 Варианты реализации (от простого к сложному)

| Вариант | Description | Срок | Условия |
|---------|-------------|------|---------|
| **A — TRM-lite (2 ресурса)** | Финансы + время CEO. «Family office for AI-driven CEOs». Низкий регуляторный барьер. | 6-12 мес | 2-3 клиента |
| **B — TRM-3** | Финансы + время + информация. «AI Chief of Staff as a Service». | 12-18 мес | Близко к Jetix HQ |
| **C — TRM-full** | Все 6 ресурсов. Требует команды 30-50 чел, лицензии BaFin (для финансов). | 3-5 лет | Полная модель |
| **D — TRM Alliance** | Альянс-модель. Jetix управляет общей AI-инфраструктурой и знанием для 5-10 клиентов. **Самый быстрый путь.** | 12-18 мес | Mittelstand AI Alliance polygon |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§6]

### 3.11 Риски TRM (6 main + mitigations)

1. **Регуляторика** (BaFin licensure, KAGB / WpHG, €730k+ капитальные требования) → mitigation: cash flow management + advisory only Phase 1, license горизонт 3-5 лет.
2. **Конфликт интересов** (10 клиентов, конкуренты, insider trading-like risks) → non-compete sectoring (1 клиент на отрасль), Chinese walls.
3. **Концентрационный риск** (€670k/клиент × 5 = -20% на потерю) → долгосрочные контракты 3-5 лет, deeply integrated AI-ops.
4. **Доверие** (никто не отдаст незнакомцу 6 ресурсов сразу) → поэтапный onboarding (1 ресурс / 6 мес → расширение), performance-based.
5. **Operational complexity** (6 несвязанных доменов) → AI-агенты как «множитель компетенций».
6. **Юридическая структура** (договор управления 6 ресурсами одновременно — сложный, неотработанный) → чёткие KPI на старте, baseline measurement, neutral arbitration.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§7]

### 3.12 Land-and-Expand: лестница 6 уровней (€3k → €40-60k/мес)

> «Хочется заходить «снизу» — с маленьких задач/гипотез/частей ресурсов, на которых клиент мало рискует.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.1]

| Уровень | Что | Цена | Срок |
|---------|-----|------|------|
| **L0 — AI-разведчик (Reconnaissance)** | Одна гипотеза / исследование / аналитическая записка | €1.5-5k/задача | 1-2 недели |
| **L1 — AI-аналитический отдел (Outsourced Brain)** | «Команда из 3 аналитиков, которые держат твои интересы» | €3-10k/мес ретейнер | min 6 мес |
| **L2 — Менеджер одного ресурса** | Один из 6 ресурсов под управлением (часто аудитория или информация) | €5-15k/мес mgmt + 20% performance | |
| **L3 — AI Chief of Staff** | «Правая рука» CEO, фильтрует информацию, готовит решения | €10-25k/мес | |
| **L4 — Партнёр по гипотезам / Venture Operator** | Открытие нового бизнеса/направления; revenue share или fee + small equity | €15-30k/мес или equity | |
| **L5 — TRM-full** | Все 6 ресурсов под управлением, deep integration | €30-60k/мес mgmt + 20-25% performance | Только для прошедших L1-L4 |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.2]

**Реалистичная воронка одного клиента:** €3k (M0) → €40k MRR / €480k ARR за 24 мес (M26+).
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.3]

**Sales motion change:**
> «Jetix не продаёт TRM — Jetix продаёт гипотезу за €3k, а потом доращивает клиента до TRM органически.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.4]

### 3.13 AI Brain on Demand (выделенная нить L0-L1 product)

**Идея:** Jetix как **внешний мозг** клиента — для разбора одного вопроса полностью.

**Себестоимость одной гипотезы:** ~$50-200 в compute + 2-4ч человеческого времени.
**Цена клиенту:** €1500-5000.
**Маржа:** 70-90%.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§12.3]

**Зазор Jetix:** между «дешёвый AI без контекста» (Perplexity Pro €20) и «дорогой консалтинг без скорости» (McKinsey €50-150k за 6-12 нед).

**Pricing-варианты:**
1. **Per-question** (€1500-5000 за гипотезу) — низкий барьер, транзакционные отношения
2. **Subscription** («10 гипотез/мес за €5k») — recurring revenue
3. **Personal Analytics Department** (€8-15k/мес unlimited) — high-value
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§12.5]

### 3.14 Что отличает TRM от обычного консалтинга

| Аспект | Классический консалтинг | TRM |
|--------|------------------------|-----|
| Что покупает клиент | Рекомендации, отчёты | Управление ресурсами |
| Кто несёт ответственность за результат | Клиент | Jetix (через performance fee) |
| Модель оплаты | Fixed fee / hourly | Mgmt fee + performance fee |
| Зависимость выручки от успеха клиента | Минимальная | Высокая (растёт с ростом клиента) |
| Скейл | Линейный (нанимаешь людей) | Экспоненциальный (через AI-агентов) |
| Valuation мультипликатор | 1-3× revenue | 5-20× revenue |
| Барьер на выход | Низкий | Очень высокий (deep integration) |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§8]

### 3.15 Главный инсайт TRM

> «Идея TRM — это не «новый продукт» Jetix. Это переопределение того, что значит "консалтинг" в эпоху AI-агентов.»
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§9]

> «Это превращает консалтинг из service business (продажа часов) в asset management business (продажа результата от управляемых активов).»

**Ключевая фраза для позиционирования:**
> «Jetix не консультирует ваш Mittelstand. Jetix управляет вашим Mittelstand-ресурсами — и делит с вами прирост прибыли.»

❌ **Outdated tagline frame:** «ваш Mittelstand» / «Mittelstand-ресурсами» — Ruslan отверг "Mittelstand DACH" frame; новая formulation должна быть domain-agnostic.

---

## 4. Платформа для проектов / partners ecosystem (Phase 2-3)

### 4.1 Workshop Phase 3 — community мастеров

См. §2.7 выше — Phase 3 = network of workshops, каждый мастер берёт кусок, выдаёт качественную деталь, аггрегация на community уровне.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6]

### 4.2 TRM Platform Phase 3 (двусторонняя marketplace)

**Эволюция в 3 фазы:**

| Фаза | Бизнес | Кто работает | Доход | Скейл |
|------|--------|--------------|-------|-------|
| **Фаза 1: Сервисная компания** (2026-2027) | Jetix управляет ресурсами клиентов сам | Ruslan + команда | Mgmt fee + performance fee | Линейный |
| **Фаза 2: Управляющая компания** (2027-2029) | Jetix управляет 30+ клиентами через AI-агентов | Команда 30-50 + флот агентов | Тот же, кратно > клиентов | Сублинейный (агенты дают рычаг) |
| **Фаза 3: Платформа TRM Network** (2029+) | Jetix сводит сторонних управляющих с клиентами | Платформа + рамочный персонал + сеть | **Take rate 15-25%** с обеих сторон | Экспоненциальный (network effects) |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.1]

### 4.3 Сторона А и Сторона B на платформе TRM

**Сторона А: «Управляемые» (Asset Owners) — клиенты с ресурсами:**
- Mittelstand-предприниматели с €10-500M выручки ❌ outdated frame
- Family offices, которые хотят управлять не только деньгами
- Self-made предприниматели с большой аудиторией, недостатком времени
- Корпоративные innovation lab'ы — есть R&D, нет операторов
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.2]

**Сторона B: «Управляющие» (Resource Operators) — профессионалы по конкретному ресурсу:**
- Финансы — independent wealth managers, ex-Goldman / UBS / family office veterans
- Время CEO — fractional COO/Integrators, ex-EOS implementers
- Аудитория — growth marketers, fractional CMO, content operators
- Информация — knowledge managers, BI experts, research analysts
- Compute / AI — ML engineers, AI ops, prompt engineers
- Команда — fractional CHRO, talent operators

**Каждый Operator** приходит со своей экспертизой, инфраструктура (Jetix OS, AI-агенты, KPI dashboard, billing, legal, escrow) — общая. Это даёт Operator 5-10× leverage.

### 4.4 Бизнес-модель платформы

**Take rate с обеих сторон:**

| Источник | Размер | Логика |
|----------|--------|--------|
| **С Operator** | 15-20% от его revenue | Платит за лиды, vetting, infra, brand, billing |
| **С Asset Owner** | €1-5k/мес или 5% от mgmt fee | Платит за curation, dispute resolution, AI tools |
| **С performance fee** | 10-15% override | Платит за то, что платформа повышает шанс успеха |
| **С compute markup** | 20-30% наценка | Своя добавленная стоимость |
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.3]

**Пример экономики при 100 Operators × 3 клиента = 300 контрактов:**
- Средний контракт €200k/год → GMV €60M/год
- Take rate ~25% blended → €15M/год revenue
- Маржа 50-70% → €7.5-10.5M EBITDA
- При 1000 Operators × 3 клиента → GMV €600M, revenue €150M платформы → валуация €1.5-3 млрд (10-20× revenue, marketplace мультипликатор).

### 4.5 Главная угроза — дисинтермедиация (disintermediation)

> «Operator находит на платформе клиента, отрабатывает 3 месяца, потом договаривается работать напрямую — мимо платформы. Все «довольны», кроме Jetix.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.4]

**Чем выше take rate и чем дороже одна сделка — тем сильнее стимул дисинтермедиироваться.** TRM с €200k+ контрактами — самая уязвимая категория.

### 4.6 7 слоёв защиты от дисинтермедиации

1. **Инфраструктурный lock-in** — Jetix OS / HQ как операционная платформа; уйдя, Operator теряет инфра.
2. **Шаринг clients = шаринг рисков** — escrow платежей, юридический контракт, страховка ответственности, dispute resolution.
3. **Performance-based reputation system** — рейтинги, отзывы, performance history — собственность платформы. Уход = потеря track record для следующих клиентов.
4. **AI-leverage недоступен вне платформы** — флот агентов даёт 3-5× продуктивности.
5. **Cross-resource synergy** — на платформе для того же клиента работают ещё 5 Operators; уход одного = потеря синергии.
6. **Контрактные ограничения** — no-circumvention clause (24 мес), психологический барьер.
7. **Низкий take rate (мета-стратегия)** — 25% → стимул уйти; 15% → маленький; 10% → почти нулевой. **Выживают на максимальном GMV × разумный take rate.**
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.5]

**Главный «секрет» работающих маркетплейсов** (Wharton academic):
> «Наиболее эффективная anti-disintermediation стратегия — это не «запрет», а «постоянное добавление ценности». Если платформа реально полезна — уход с неё становится невыгодным даже без юридических запретов.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.6]

### 4.7 Как перейти к платформенной фазе (chicken-and-egg)

**Главная проблема Phase 3:** Operators не приходят без клиентов; клиенты не приходят без Operators. Все известные решения (Uber, Airbnb, Toptal, Catalant) проходили через одну схему: **сначала сервисная компания → набирает первых клиентов и Operators руками → открывается как платформа**.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§15.1]

**Хорошая новость:** именно это Jetix делает в Phase 1-2 → путь к платформе уже встроен в текущую стратегию.

**Critical timing insight:**
> «Все эти компании потратили 5-10 лет в Phase 1+2 прежде, чем перейти в Phase 3. Прыгнуть сразу в платформу не получалось ни у кого. Переход Jetix в платформу не должен случиться раньше 2028-2029.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§16]

**Аналоги-кейсы:**

| Компания | Phase 1 (сервис) | Phase 2 (масштаб) | Phase 3 (платформа) | Текущий статус |
|----------|----------------|------------------|---------------------|----------------|
| **Toptal** | Ручной скаутинг 100 разработчиков | $200M+ ARR through own team | Открытая платформа 3% acceptance rate | $200M+ ARR, $1B+ |
| **Catalant** (ex-HourlyNerd) | Ручной матчинг ex-MBA | Команда менеджеров для проектов | Marketplace 35k+ экспертов, 30% commission | ~$50M ARR |
| **Andela** | Bootcamp + staff aug | Сами растили инженеров | Open marketplace 175k+ | $200M+ ARR, $1.5B |

### 4.8 Уникальная конкурентная позиция Jetix

**3 структурных преимущества:**

1. **Vertical specialization (Mittelstand + AI)** ❌ outdated frame — defensible niche.
2. **AI-native infrastructure** — Toptal/Catalant из 2010-х; Jetix HQ изначально AI-native, на одно поколение технологий впереди.
3. **Resource multidimensionality (TRM-структура)** — все остальные marketplace'ы матчат **один тип отношений** (заказчик ⇄ фрилансер); Jetix матчит **6 типов ресурсов одновременно** = уникальный сетевой эффект.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§17]

### 4.9 Wiki/ideas: Platform / Partners ecosystem

**Jetix Agency — лестница ценности:**

| Этап | Сделка | Длительность | Ценность для клиента |
|------|--------|--------------|----------------------|
| 1. Аудит | $1K-5K | 1-2 недели | Уязвимости + возможности |
| 2. Автоматизация | $5K-50K | 1-3 месяца | Внедрённые AI-агенты |
| 3. Стратегический партнёр | retainer / equity | ongoing | Совместная разработка стратегии |
| 4. Со-инвестор / экосистема | equity | долгосрочно | Доступ ко всей сети Jetix |
[src: wiki/ideas/jetix-agency-strategic-ai-partners.md:лестница-ценности]

> «Все компании-клиенты образуют экосистему Jetix — помогают друг другу (matchmaking, lead-share), сотрудничают (joint-products), объединяют отрасли (cross-vertical insights). Jetix владеет методологией, не отдельными контрактами.»
> [src: wiki/ideas/jetix-agency-strategic-ai-partners.md:что-объединяет]

**Investment fund as Jetix component:**
> «Jetix не только консультирует, но и инвестирует в бизнесы партнёров → зарабатывает на росте, а не только на услугах. Партнёры получают и экспертизу, и капитал.»
> [src: wiki/ideas/investment-fund-jetix-component.md:одна-строка + обоснование]

Прецеденты: Atomic, Idealab, eFounders. Phase 2 launch (после €50K validation).

### 4.10 Roy-replication methodology (Decision 21, Phase 3+)

> «Jetix сперва строит свой рой из 10 людей, зарабатывающих $10M-$100M; затем распаковывает методологию как инструмент/систему; затем другие рои emerge в других вертикалях/нишах/странах. Jetix meta-coordinates ecosystem of swarms.»
> [src: decisions/JETIX-VISION.md:§5 Phase 3+]

### 4.11 Token economy (Decision 23, Phase 2 internal / Phase 3+ public)

> «надо будет потом как-то эти токены еще изучить как сделать для jetix токены там валюту и так далее… специалистам тоже но как-то раздавалась чтобы это все было безопасно… для оплаты кита с заделом на будущее что будет своя какая-то экосистема»
> [src: voice-extract:§1.8.3, holding-vision-2026-04-21 Note 6]

**Trigger:** $100K self-earned → token economy exploration starts.
- Phase 2: internal utility (specialist compensation, складчина tokens)
- Phase 3+: limited public layer (alternative-to-IPO liquidity path)
- Design safe + adequate + thoughtful, **explicitly не crypto-pump style**.
[src: decisions/JETIX-VISION.md:§5 Decision 23]

---

## 5. Управляющая компания — что делает Jetix как managing entity

### 5.1 Что значит «управляющая»

**TRM core thesis:**
> «Прибыль клиента растёт, потому что его ресурсы, которые раньше тратились хаотично или не использовались вообще, начинают работать как единый портфель под управлением.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§1]

**Active management vs advisory:**
> «Jetix не просто советы — реальное управление частью ресурсов клиента (с его согласия). Like Berkshire Hathaway но для Mittelstand operations.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§5.1 — 1B skeleton]
❌ outdated frame "Mittelstand operations"; адаптировать к agnostic.

### 5.2 Типы управления (по 6 ресурсам)

См. §3.2 + §3.7 выше. Per resource — разные глубины:

- **Финансы** — cash management, бюджетирование, advisory; investment portfolio только с BaFin license (Phase 3+).
- **Время CEO** — fractional COO/Integrator pattern, освобождение CEO для vision-задач.
- **Аудитория** — управление LinkedIn, рассылками, content monetization.
- **Информация** — knowledge ops: построить и вести KB, оцифровать tribal knowledge.
- **Compute** — управление AI-budget клиента в связке с бизнес-задачами.
- **Команда** — fractional executive ops, кураторство ключевых людей.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.2 пример клиента]

### 5.3 Юридическая структура

🟡 **Possibly stale / open:**
- Phase 1: standard consulting contracts (без Asset Management license).
- Phase 2: extended contracts (multi-resource), not BaFin-licensed.
- Phase 3+: BaFin license (KAGB / WpHG) — capital req €730k+.
- Альтернатива: партнёрство с лицензированной структурой.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§7 Risk 1]

### 5.4 Trust building — как клиент отдаёт управление

**Поэтапный onboarding:**
1. L0 €3k гипотеза → доверие минимально, риск минимален.
2. L1 €5k/мес ретейнер → Jetix становится «memory and analytical layer» клиента.
3. L2 один ресурс → пилот.
4. L3 AI Chief of Staff → доступ к календарю/переписке.
5. L4 venture operator → новый бизнес с CEO как owner.
6. L5 TRM-full → все 6 ресурсов deep integration.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.2]

### 5.5 Анти-паттерны управляющей компании

> «Никто не отдаст управление всеми шестью ресурсами незнакомцу. Это структурная проблема доверия: TRM требует глубокой интеграции, а интеграция требует track record. Прямой путь («заходим на €670k/год сразу») не сработает почти ни на одном клиенте.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.1]

---

## 6. Большая афёра века / Эксперимент

### 6.1 «Самая большая авантюра» framing

**Verbatim Ruslan (21.04 holding-vision):**
> «как раз вот этих авантюристов мы собираем для того чтобы вот триллионную компанию как можно быстрее собрать… инфраструктуру которая должна будет выдержать масштабирование там 1 миллиард до 1 триллиона»
> [src: voice-extract:§1.7.3, raw/voice-memos-text/holding-vision-2026-04-21.md:L38, L56]

**D1 Vision tagline:**
> «Объединить всех авантюристов в самую большую авантюру.»
> [src: decisions/JETIX-VISION.md:§14, audio_401]

**Self-selection через framing:**
> «"Самая большая авантюра века" invitation (Decision 20 aligned) — self-filtering механика. Только человек, self-identifying как авантюрист-с-навыками, отвечает на такой призыв. Passive consumer проходит мимо. Вызов громкий, но adressant узкий. Predator-outside tool: провокативный, но работает как мембрана.»
> [src: decisions/JETIX-VISION.md:§7.2]

### 6.2 $1T trajectory — engineering-faith bet

**Core ambition (D19):**
> «Jetix целится на то, чтобы стать первой… поставить вообще мировой рекорд по достижению капитализации в 1 триллион долларов. Скорость, за которую будет достигнута эта цифра от нуля, от создания компании до триллиона.»
> [src: holding-vision-2026-04-21 Note 5, цитировано decisions/JETIX-VISION.md:§14]

**Precedent to beat:**
> «попытается надавать поебальничку вот XEI, который за два года достиг капитализации в 100 миллиардов»
> [src: holding-vision-2026-04-21 Note 5]

**Civilizational scale:**
> «Jetix… настолько блять будет масштабным, мощным… что это будет, блядь, сопоставимо, сука, с странами какими-то.»
> [src: audio_496, цитировано decisions/JETIX-VISION.md:§14]

### 6.3 Не pyramid / scam — engineering-faith framing

> «Это все должно быть не какая-то там ебаная пирамида или еще что-то, блядь. Нет. А реально адекватные инструменты, наработки, блядь, технологий.»
> [src: holding-vision-2026-04-21 Note 5]

**$1T grounded in:**
- Real tools + adequate методология + adequate team
- Founder commitment («основатель горит, который все свое время, всю свою жизнь вкладывает»)
- Infrastructure-first readiness (Phase 1 architecture carries $1T scale без редизайна)
- Compatible со всеми 18 LOCKED decisions + 6 Stage 2B
[src: decisions/JETIX-VISION.md:§14 Engineering-faith section]

### 6.4 Что именно тестируется (гипотезы Phase 2-3)

- AI-native operational company как новый класс entity (vs traditional consulting / SaaS / agency)
- Total Resource Management as service на 6 ресурсах одновременно (vs single-resource fund)
- Partner ecosystem с roy-replication methodology (vs hire'ы и vertical scaling)
- Workshop community model (Phase 3 mega-system)
- USB-C universal connector для AI-business cooperation (Decision 20)
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§6.2 — 1B skeleton; decisions/JETIX-VISION.md:§5 + §14]

### 6.5 Что если не получится (fallback)

**Honest fallback — что выносим из failed experiment:**
- Накопленный knowledge / методология
- Network of people (через скептический ICP filter)
- Foundation v1.0 — fork-portable infrastructure (other founders могут взять)
- Compound-engineering practices что показали себя
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§6.3 — 1B skeleton, ещё не filled]

### 6.6 Что если получится

**Trajectory:** €50K → €500K → €5M → €50M+ revenue → $100M → $100B → $1T market cap.
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§6.4 — 1B skeleton]

**Что меняется в мире (200-year vision):**
> «Долгосрочная цель Jetix — вклад в создание будущего, где базовые проблемы (голод, болезни, неравенство) решены. Микро-задача: каждый бизнес, который Jetix делает безопаснее и эффективнее через AI, — кирпичик.»
> [src: wiki/ideas/200-year-vision-jetix-humanity.md:одна-строка + обоснование]

**Two leverages:**
1. AI-эффективность — больше выходных продуктов на единицу ресурса.
2. AI-безопасность — снижение системных рисков (cybersec, supply chain, decision quality).

**Founder constitution принцип:**
> «Когда система станет большой, контролировать её напрямую невозможно — поэтому ценности и предохранители закладываются ДО роста.»
> [src: wiki/ideas/founder-responsibility-jetix-constitution.md:одна-строка]

### 6.7 Mafia / закрытое ядро Phase 1

> «именно для начальной стадии вот джекса что мы все-таки будем действовать больше как мафия то есть мы там собрались какие-то свои ресурсы собрали хорошо бизнес там работа да есть это свободные ресурсы инвестируем»
> [src: voice-extract:§1.9.4, audio_563@27-04-2026]

Phase 2 Trust structure — closed-circle mafia-style → Phase 3 evolves to community.

### 6.8 Public company from Day 1 (anti-scam mechanism)

> «джек должен быть публичной компании вести себя как публичная компания чтобы любой аналитик мог проверить посмотреть видеть для все пятна все как управляется»
> [src: voice-extract:§1.9.7, audio_556@26-04-2026]

Trust mechanism для Workshop — public-company-style transparency from Day 1 = anti-pyramid signal. Cross-cuts Visual/View principle (external dashboard).

### 6.9 Cooperation, не extraction

> «пока остальные дурачки целятся на какой-то one-person бизнес, в одиночку какие-то инструменты используют и так далее. Jetix наоборот нацелен на синергию, на сотрудничество, на партнерство»
> [src: voice-extract:§1.5.1, audio_554@26-04-2026]

---

## 7. ICP — концептуальный portrait участников Jetix

> ⚠️ **Critical:** Ruslan **выраженно отверг** «Mittelstand DACH manufacturing 50-500 emp» как ICP. Новый ICP = концептуальный portrait через 2 оси × 3 типа.

### 7.1 Базовый принцип ICP — 2 оси, не география / индустрия

> «Главный портрет участника Jetix:
> **Ось 1: Уровень ресурсов** (финансы, время, знания, network, команда, compute / инструменты).
> **Ось 2: Желание развиваться** (понимание что чего-то не хватает, готовность вкладываться, long-term mindset, готовность учиться + делиться).
>
> Если оба условия есть — потенциальный участник Jetix, **независимо** от индустрии (manufacturing / SaaS / consulting / coaching), географии (DACH / Eastern Europe / global remote), стадии бизнеса (idea / early / scale / mature), размера (1 / 5 / 50 / 500).»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.1 — 1B skeleton]

### 7.2 3 типа участников (по уровню вовлечения)

> Не клиенты vs партнёры — это **спектр**.

#### Тип 1 — Solo Entrepreneurs / Indie Hackers (revenue share %)

**Кто:** один человек строит свой проект / бизнес / practice. Founder / consultant / coach / creator / advisor.

**Что им даёт Jetix:**
- Полный доступ к Базовой Системе как foundation
- Натренированные AI-агенты (12 ролей)
- Adaptable станки (D2 / MCP / Plan Mode / Voice / Time-tracking)
- Compound learning + общая community knowledge
- Cross-collaboration с другими indie через Jetix infrastructure

**Что Jetix получает:**
- **Процент от их revenue / outcome** (revenue share модель)
- Их contributions back в общую систему (новые методологии / инсайты / станки)
- Network growth (приводят клиентов / коллег)

**Пример:** indie consultant с €5-15K/мес practice → Jetix infrastructure → растёт до €30-50K/мес → отдаёт 10-20% revenue share.
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.2 Type 1]

#### Тип 2 — Средний бизнес (mgmt fee + % growth)

**Кто:** компании 5-100+ человек, владелец активно вовлечён, есть ресурсы и желание расти. **Любая индустрия. Любая география.**

**Что им даёт Jetix:**
- Foundation infrastructure для operational layer
- Натренированные AI-агенты под их специфику
- Implementations / customizations adaptable станков
- Periodic strategic консультации / planning sessions
- Cross-pollination с другими бизнесами в Jetix network

**Что Jetix получает:**
- **Процент** (mgmt fee + performance fee на growth metrics)
- Operational data → patterns → улучшение системы для всех
- Case studies / success stories для marketing

**Пример:** small SaaS company €500K ARR → Jetix → €2-5M ARR за 2-3 года → mgmt fee + % growth.
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.2 Type 2]

#### Тип 3 — TRM-делегаторы (полная TRM модель)

**Кто:** люди / компании, готовые **делегировать управление частью своих ресурсов** Jetix — потому что верят, что Jetix управляет лучше, чем они сами.

**Что им даёт Jetix:**
- Активное управление частью их ресурсов (не просто советы)
- Освобождение их focus на то, что они любят / умеют лучше всего
- Compound оптимизация ресурсов через Jetix expertise + AI-augmentation
- Reporting + transparency на всё

**Что Jetix получает:**
- **Mgmt fee + performance fee** (TRM модель в полную силу)
- Глубокую integration → больше data → больше leverage

**Пример:** founder, заработавший €5M exit, не хочет сам управлять wealth + time + знаниями — отдаёт Jetix.
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.2 Type 3]

### 7.3 Общий критерий — у тебя есть **ресурсы** + **желание развиваться**

> «Любой человек или организация у которых есть какие-либо ресурсы (даже минимальные) и есть желание / понимание что развитие нужно — потенциальный участник Jetix.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.3]

### 7.4 Сравнительная таблица 3 типов

| Параметр | Type 1: Solo / Indie | Type 2: Средний бизнес | Type 3: TRM (управление) |
|----------|---------------------|------------------------|--------------------------|
| Размер | 1 человек | 5-100+ чел | Любой (с делегированием) |
| Вовлечённость в систему | Полная (сам использует) | Гибрид (часть команда) | Активная (Jetix manages) |
| Что даёт | Foundation + agents + станки + community | + customizations + strategic | + active management части ресурсов |
| Что получает Jetix | Revenue share % | Mgmt fee + % growth | Mgmt fee + performance fee |
| Глубина integration | Light | Medium | Deep |
| Время до результата | 1-3 мес setup, 6-12 мес leverage | 3-6 мес setup, 12-24 мес leverage | 6-12 мес setup, 24-36 мес transformation |
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.6]

### 7.5 ICP Pains / triggers для входа в Jetix

- «Я делаю всё сам и не хватает капасити» (solo founders → Type 1)
- «Бизнес растёт, но всё медленнее чем хочется, не понимаю где затыки» (mid-size → Type 2)
- «У меня есть деньги / время / связи но не знаю как их максимально использовать» (Type 3)
- «Я хочу учиться у людей с похожими амбициями но более продвинутых» (любой Type)
- «Я устал управлять всем сам, хочу делегировать operationally а не просто tactically» (Type 3)
- «AI / новые tools меняют game, я не могу один это все integrate» (любой Type)
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.4]

### 7.6 НЕ наш ICP — explicitly

- ❌ Люди которые **не хотят меняться** / "у меня и так всё хорошо"
- ❌ Те кто ждут **готовое решение под ключ без вовлечения** (Jetix = сотрудничество, не assembly line)
- ❌ Покупатели **самой дешёвой опции** (мы не competitor SaaS подписок)
- ❌ Те у кого **нет вообще ресурсов** (для start даже Type 1 нужно минимум €X финансов или Y времени)
- ❌ Краткосрочный mindset (Jetix даёт результаты в 6-36 мес, не 1-3)
- ❌ Не разделяют ценности из Pillar C
[src: decisions/JETIX-CORPORATION-2026-05-05.md:§7.5]

### 7.7 ❌ OUTDATED ICP frame (Mittelstand DACH)

🟡 **Possibly stale frame** — широко представлен в источниках:

**TRM-MODEL §4.2** illustrative client: «немецкий Mittelstand, машиностроение, выручка €50M, EBITDA €5M.»
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.2]

**TRM-MODEL §17 vertical specialization:** «Vertical specialization (Mittelstand + AI). Узкая ниша = глубокое понимание клиентов = лучше матчинг = выше LTV.»
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§17]

**TRM-MODEL §18 positioning phrase:**
> «Jetix не консультирует ваш Mittelstand. Jetix управляет вашим Mittelstand-ресурсами — и делит с вами прирост прибыли.»
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§18]

**1B skeleton frontmatter INCLUDES list:**
> «ICP (Mittelstand DACH 50-500 emp manufacturing)»
[src: decisions/JETIX-CORPORATION-2026-05-05.md:frontmatter line 37]

⚠️ **Conflict:** 1B skeleton frontmatter INCLUDES «Mittelstand DACH» ICP, BUT §7 body of 1B skeleton **rejects this frame** explicitly («НЕ привязывайся к Mittelstand DACH»). When заполняем 1B — frontmatter line 37 нужно обновить consistent с §7 body.

### 7.8 Старые ICP archetypes (10 + 1 архетипов из D1 Vision, 21.04)

**11 архетипов (Decision 7 union + Stage 3 addition):**
1. Предприниматели / бизнесмены
2. Ресёрчеры
3. Инженеры
4. Инвесторы
5. Политики
6. Продавцы
7. Менеджеры / коммуникаторы
8. Философы
9. Разработчики идей
10. Разработчики жизни
11. **Блогеры** (Stage 3 addition 2026-04-21) — 5K+ подписчиков + реальная глубокая экспертиза в своей нише
[src: decisions/JETIX-VISION.md:§7.1]

**ICP Qualitative Filter (Decision 22) — 5 критериев:**
1. **Startupper mindset** — builder's instinct, proactive, creates rather than consumes
2. **Предпринимательский азарт** — entrepreneurial game-drive (skilled player, не gambler)
3. **Stable** — reliable, disciplined, не volatile
4. **Adequate** — common sense, no delusion, anti-bullshit detector
5. **Upward-direction** — actively develops self + среду

**Direction-of-life axis (NEW dimension):**
> «прикол в том что темы это не по темам а по направлению жизни короче вот в чем штука что темы они как-то расходятся… вправо влево получается по горизонтали а по вертикали это вверх вниз нахуй это направление вверх направление к жизни или направление вниз там к смерти блять тупежу»
> [src: decisions/JETIX-VISION.md:§7.2, holding-vision-2026-04-21 Note 2]

**Jetix community = ВСЕ 11 archetypes × UPWARD-DIRECTION ONLY.** Topic — secondary, direction — primary.

🟡 **Reconciliation needed:** D1 Vision (21.04) 11 архетипов × 5 critical filter — это **complementary** к 1B skeleton 3-types axis. 11 архетипов distribute через 3 типа (Solo Type 1 / mid-business Type 2 / TRM Type 3). 5 critical filter (Startupper / Azart / Stable / Adequate / Upward) применим ко всем 3 типам.

### 7.9 NOT target — анти-аудитория

- Mass-market consumer base (*«не oriflame»*)
- Мотивационный circle (Tony Robbins passive audience)
- Философский retreat (passive reflection без action)
- Superficial networking (LinkedIn-style transactional)
- Attention-economy consumers
[src: decisions/JETIX-VISION.md:§7.2 NOT target]

**Anti-Oriflame quote:**
> «это важно зафиксировать не то что он как oriflame нет ну то есть не на широкие массы а конкретно на профессионалов на вот заинтересованных людей в своем развитии»
> [src: voice-extract:§1.5.3, raw/voice-memos-text/holding-vision-2026-04-21.md:L38]

**Anti-LinkedIn / TikTok / Instagram quote:**
> «это не хуйня типа тик тока который являть инстаграма или youtube а которая просто ну блять все дерьмо вместе… это тоже этот тоже не linkedin где блять быдло одно которое ищет какие-то рабов»
> [src: voice-extract:§1.5.2, raw/voice-memos-text/community-addendum-2026-04-21.md:L36]

### 7.10 Master vs non-master entry filter (refinement)

> «это все описание одного и того же мастер и не мастер профи и не профи… в этого мастера есть опыт есть возможно нужные инструменты есть возможно not понимание и знания как нужно делать какой последовательности… а который не может это не профессионал»
> [src: voice-extract:§1.6.1, audio_583@30-04-2026]

**Workshop = for masters only — non-masters cannot use the tools effectively.** Это критический ICP filter (Phase 1+).

---

## 8. Видение 1 / 3 / 10 лет

### 8.1 Через 1 год (середина 2027)

**1B skeleton placeholder:**
> «€50K achieved → €100-300K ARR / 3-5 клиентов / 1-2 партнёра / Foundation v2.0 / first methodology publish.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§8.1]

**TRM-MODEL Phase 1 numbers:**
- 5-10 клиентов на TRM-lite / 6 уровнях лестницы
- Один клиент при honest TRM-lite delivery = €10-50k/год; full L5 = €670k/год
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§4.3 + §11.3]

### 8.2 Через 3 года (2029)

**1B skeleton placeholder:**
> «€1-5M ARR / 15-30 клиентов / 5-10 партнёров / community 50-200 people / признание в DACH consulting space.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§8.2]
❌ outdated frame "DACH consulting space" — нужно перевести в agnostic.

**TRM-MODEL Phase 2:**
- 30+ клиентов в TRM-управлении → €15-20M ARR
- Команда 30-50 чел + флот агентов
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.1]

### 8.3 Через 10 лет (2036)

**1B skeleton placeholder:**
> «€50M+ ARR / категория «AI-native operational corp» признана / multi-region / patents / Trust ecosystem.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§8.3]

**TRM-MODEL Phase 3 (платформа):**
- 1000 Operators × 3 клиента = €600M GMV → €150M revenue платформы
- Валуация €1.5-3 млрд (10-20× revenue marketplace мультипликатор)
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.3]

### 8.4 Через 10 лет — экспериментальный сценарий ($1T)

**D19 LOCKED:**
> «мы строим нахуй ван хандрит биллиан» ($100B scale) → world-record по достижению $1T market cap.
> [src: holding-vision-2026-04-21 Note 4 + Note 5]

**Trajectory benchmarks:**
- XEI precedent: 2 years to $100B market cap (to be beaten)
- Phase sequencing: $20-30K → €50K Q2 2026 → €200K validation → €1M → $100M → $100B → $1T
[src: decisions/JETIX-PLAN.md:§1 Plan Overview]

**Civilizational infrastructure:**
> «Jetix настолько будет масштабным, мощным… что это будет сопоставимо, сука, с странами какими-то.»
> [src: decisions/JETIX-VISION.md:§14, audio_496]

### 8.5 Phase transitions — 3 фазы Workshop + 3 фазы TRM

**Workshop frame:**
- Phase 1: одна мастерская одного человека (текущее)
- Phase 2: команда работает с одной системой
- Phase 3: community of workshops (mega-system)

**TRM-MODEL frame:**
- Phase 1 (2026-2027): сервисная компания
- Phase 2 (2027-2029): управляющая компания
- Phase 3 (2029+): двусторонняя платформа TRM Network

**Cross-mapping:** Workshop Phase 1 = TRM Phase 1; Workshop Phase 2 ≈ TRM Phase 2 (но Workshop emphasizes one-system; TRM emphasizes 30+ клиентов через AI scale); Workshop Phase 3 (community) ≈ TRM Phase 3 (platform).

### 8.6 200-year vision

> «Долгосрочная цель Jetix — вклад в создание будущего, где базовые проблемы (голод, болезни, неравенство) решены.»
> [src: wiki/ideas/200-year-vision-jetix-humanity.md]

> «Мы строим не компанию, а инфраструктуру для мира, в котором хочется жить через 200 лет.»

**Smysl, который переживёт основателя.** Связано с founder responsibility / constitution (закладывать ценности до роста).

### 8.7 Phase 1 capability state (текущий)

**Из retrospective 2025-05_to_2026-04:**
- Foundation v1.0 LOCKED 28.04 (11 Parts + Pillar A/B/C)
- Workshop concept LOCKED 30.04
- TRM model LOCKED 30.04
- Plan Mode pilot 30.04
- Peak month April 2026: 702h total, 150h Deep Work
- Phase 3 trajectory: «строить систему которая будет генерить ценность долго» (стратегия + leverage)
[src: reports/retrospective_2025-05_to_2026-04.md:§Phase 3 + insights]

**12-month transformation:**
- Phase 1 (Jul-Sep 2025): Lead Gen Agency
- Phase 2 (Oct 2025 - Feb 2026): Mindset / Values / Books
- Phase 3 (Mar-Apr 2026): AI breakthrough + Active Jetix Build

**Insight #3 (retrospective):**
> «AI-breakthrough был ПОДГОТОВЛЕННЫМ. Если бы AI пришёл в Phase 1 (Jul 2025) — ты бы использовал его на ускорение outreach, и заработал бы $5K. Но потому что он пришёл в Phase 3 (Feb 2026, после Phase 2 mind-training) — ты строишь Jetix OS на $50K → trajectory $1T. Phase 2 не была «потерянным временем». Это был invest в leverage.»
> [src: reports/retrospective_2025-05_to_2026-04.md:§Insight #3]

---

## 9. Roadmap к €50K — Q2 2026

### 9.1 Phase 0 → Phase 1 transition (текущее)

**Current starting point (2026-04-21):** $5K на счету; transitioning из existing work; Phase 0 цель = $20-30K self-funded.
[src: decisions/JETIX-PLAN.md:§2 Phase 0]

**Phase 0 actions — top priorities:**
1. Закрыть основной слой архитектуры Notion (AI-1) — unlock'ает всю communication / execution layer
2. **Описать ICP подробно** (QM-1) — D22 5 критериев + direction-of-life axis ✓ (см. §7 выше)
3. Зафиксировать позиционирование (BR-1) — pain-primary + opportunity-secondary, USB-C / enterprise-fast framing
4. Сайт + 2 видео RU/EN + трафик на сайт (QM-13, QM-14)
5. Описать роль + focus 3-4 месяца (QM-7) — role clarity unlock'ает execution
6. Setup Claude Code полный workflow (AI-4, AI-5)
7. Open Stripe business + начать юр инфра setup (QM-9) — GmbH actual open triggers at $20-30K
[src: decisions/JETIX-PLAN.md:§2.2]

### 9.2 Phase 1 — Foundation ($20-30K → €50K Q2 2026)

**Q2 2026 finish line: €50K committed revenue** (D9 / D15). **Это единственная committed absolute date в плане.**
[src: decisions/JETIX-PLAN.md:§3]

### 9.3 Revenue-mix decomposition (€50K target)

⚠️ **Critical migration note 2026-04-24** (KM-Mat-MVP investor CC-1):

| Line | Volume | Price | Revenue Q1+Q2 2026 |
|------|--------|-------|--------------------|
| Productized contracts (Path-B) | 4 contract-quarters (2 contracts × 2 Q) | €7.5K per contract-Q | €30 000 |
| Hourly consulting (4-pack «конкретная помощь» + discovery) | 233 hours | €150/hr | €35 000 |
| **Total (gate: €50K)** | | | **€65 000 (~30% margin)** |

**Implication:** 4-pack `услуги` / `конкретная помощь` line — **first-class revenue channel** (~54% of Phase-1 target). Without hourly capacity, €50K gate fails.

Operator guidance: ≥20 hours/week of hourly-available capacity across Q1 + Q2 2026 alongside structured outreach for 2 contracts/quarter.
[src: decisions/JETIX-PLAN.md:§3.1.1]

### 9.4 Phase 1 actions

**Infrastructure:**
- GmbH setup (€1000-1500) — DE legal home
- Stripe business + optimal payment method
- Basic legal: contracts, NDA templates
- Agent contracts formalized
[src: decisions/JETIX-PLAN.md:§3.2]

**Offer expansion:**
- **Продюсерский центр pilot** — 1-2 first clients (англоязычный инфобиз)
- Consulting scale — 5-10 active clients (€150/час baseline, productized packages)
- 4-pack offer fully live (сессия / 10 шаблонов / чат попутно / услуги)
- $1000 experiment — agent система, publicly measured outcome
- 10-template lead-magnet consolidated
[src: decisions/JETIX-PLAN.md:§3.3]

**Content:**
- Full site launch (deeply packaged)
- Weekly videos + blog posts
- Podcast appearances 1-2/мес
- Blogger collaborations start (TOF max)
[src: decisions/JETIX-PLAN.md:§3.4]

**Community (Phase 1 simple):**
- Telegram group OR Discord (invite-based)
- 5-20 members face-to-face
- No formal mechanics
- Tool-sharing seed (Perplexity / Claude Code pool)
[src: decisions/JETIX-PLAN.md:§3.5]

### 9.5 Phase 1 markets

- **English + US primary** (infobiz ниша)
- **UK / international English** secondary
- **DE** — GmbH legal home, **НЕ primary sales market** в Phase 1
[src: decisions/JETIX-PLAN.md:§3.7]

🟡 **Possibly stale / contradiction:** D1 Vision (21.04) и Phase 1 plan (21.04) emphasize English + US Phase 1 markets; TRM-MODEL (30.04) implies Mittelstand DACH primary. ⚠️ **Conflict + outdated**: TRM "Mittelstand" framing is illustrative, not committed market; Phase 1 actual market = English/US infobiz blogers + indie hackers + smart entrepreneurs (per ICP §7). When заполняем 1B Phase 1 plan — clarify markets agnostic + de-emphasize Mittelstand.

### 9.6 Phase 1 milestones

| ID | Marker | Trigger |
|---|---|---|
| M1.1 | Продюсерский центр first deal signed | Product-market signal |
| M1.2 | €20K (Phase 1 half) | Momentum check |
| M1.3 | €35K | Acceleration |
| M1.4 | €50K reached Q2 2026 | **Phase 1 → transition gate triggered** |
[src: decisions/JETIX-PLAN.md:§3.9]

### 9.7 Phase 1 exit criteria

- ✅ €50K revenue reached by Q2 2026
- ✅ Продюсерский центр running — at least 2-3 paying clients
- ✅ Consulting portfolio диверсифицирован
- ✅ Community чат active (>5 regular members)
- ✅ Content pipeline operational (weekly cadence)
- ✅ $1000 experiment outcome documented publicly
[src: decisions/JETIX-PLAN.md:§3.10]

**Anchor quotes:**
> «150 евро × 4 часа = 600 кэшфлоу» [audio_452] — юнит-экономика первой платной услуги.
> «переключиться в режим бизнеса, охоты, сфокусированного поиска денег» [audio_503]

### 9.8 Revenue-gated unlocks (D15) — фазовая mechanics

| Checkpoint | Unlocks |
|---|---|
| $20-30K self-earned | GmbH, Stripe, $1000 experiment, basic legal |
| €50K Q2 2026 | Продюсерский центр scaling, patent process *prep* |
| €200K validation | Patents EU, first 1-2 hires, Secure Network build starts |
| €200K → €1M | Team 5-10, revenue-share partnerships, token economy internal |
| €1M+ | 10+ team, Fortune 500 conversations, holding structure formalized, roy-replication |
[src: decisions/JETIX-PLAN.md:§1 Revenue-gated unlocks]

### 9.9 Tactical / strategic sequencing

> «тактически прибыль, стратегически польза»
> [src: audio_503, цитировано decisions/JETIX-VISION.md:§14]

Phase 1 tactical revenue (consulting €50K) ⊂ Phase 3+ strategic contribution ($1T + civilizational). **No conflict — phase sequencing.** Engineering-faith means: faith expressed through resource allocation, не affirmations; tactical profit Day 1 буквально funds the strategic contribution Day N.

### 9.10 Tseren Tserenov — first concrete Phase 2 partnership target

**Phase 1 → 2 first transition trigger** identified:
> «созваниваюсь с этим царином цариновым… мы берем как-то с тыкуем скорее всего вот эту мое видение плюс их как-то наработки… мы это для делаем адекватно потом я беру это все вот упаковываю сайт»
> [src: voice-extract:§2.1, audio_582@30-04-2026]

Tseren = first non-AI human partnership for Workshop scale-up. Workshop §6 Phase 2 onset.

---

## 10. Синергия / network effects

### 10.1 Cross-resource synergy в TRM

**5 Operators on same client:**
> «Один Operator управляет финансами клиента. На платформе для того же клиента работают ещё 5 Operators (время, аудитория, информация, compute, команда). Все они обмениваются контекстом через платформу. Уход одного из них = потеря синергии для клиента (он этого Operator потеряет первым). Это специфическое преимущество TRM-структуры — оно отсутствует у Toptal/Catalant.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§14.5 Layer 5]

### 10.2 Knowledge accumulates у всей сети

**Compound learning effect не только у Jetix:**
> «у нас лучшая блять research и лучшая блять аналитика up to date»
> [src: voice-extract:§1.1.2 audio_565]

> «сбор твоих знаний… с одной ниши в другую короче перетаскивать»
> [src: voice-extract:§1.8.1 audio_565 — Knowledge accumulation discipline]

### 10.3 Clients ↔ Partners interactions

**Jetix Agency ecosystem:**
> «Все компании-клиенты образуют экосистему Jetix — помогают друг другу (matchmaking, lead-share), сотрудничают (joint-products), объединяют отрасли (cross-vertical insights).»
> [src: wiki/ideas/jetix-agency-strategic-ai-partners.md:что-объединяет]

**Partnership-Matchmaker (Decision 21):**
> «Jetix матчит complex tasks с specialists, AI-agents смазывают coordination, качественно/быстро/адекватно фиксируются контракты и touch-points. Network effects: накапливаются контакты, specialists постепенно transition внутрь Jetix.»
> [src: decisions/JETIX-VISION.md:§5 Phase 2+]

### 10.4 Network effects — почему ценность растёт нелинейно

**3 структурных преимущества TRM:**
1. **Vertical specialization** — узкая ниша = глубокое понимание клиентов = лучше матчинг = выше LTV.
2. **AI-native infrastructure** — на одно поколение технологий впереди Toptal/Catalant.
3. **Resource multidimensionality (TRM-структура)** — все остальные marketplace'ы матчат **один тип отношений** (заказчик ⇄ фрилансер); Jetix матчит **6 типов ресурсов одновременно** = уникальный сетевой эффект.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§17]

### 10.5 Coalitionary thinking — объединение

> «Объединить всех авантюристов в самую большую авантюру»
> [src: audio_401, цитировано decisions/JETIX-VISION.md:§14]

> «Капитализм → коммунизм на высоких уровнях»
> [src: audio_495]

> «Jetix должна быть самой пиздатой корпорацией, но при этом за счет того, что она работает с другими самыми пиздатыми компаниями, людьми, корпорациями. Они свою пиздатость, уникальность подчеркивают, и Jetix за счет этого свою тоже уникальность.»
> [src: audio_488, цитировано decisions/JETIX-VISION.md:§4]

### 10.6 Open Source / Linux-style philosophy

**Three principles:**
1. **Revenue Share** — партнёры сохраняют свои ресурсы и навыки, даже если Jetix распадётся (антифрагильность).
2. **Прозрачность подхода** — методы / фреймворки / ошибки документируются и делятся (Karpathy LLM Wiki pattern).
3. **Платформа, не клуб** — масштаб за счёт притягивания, а не gatekeeping-а.
[src: wiki/concepts/jetix-open-source-principles.md]

> «Jetix мог бы забирать до 70% прибыли партнёра за счёт экосистемы, инструментов и знаний. Мы этого не делаем — потому что верим, что устойчивее платформа, в которой каждый участник сохраняет свою силу. Если завтра Jetix исчезнет, ваши ресурсы, контакты и навыки останутся у вас. Это закреплено контрактно.»
> [src: wiki/ideas/revenue-share-jetix-philosophy.md:pitch-абзац]

### 10.7 Mafia-style closed Phase 1 → community Phase 3

**Phase 1 trust structure (mafia-style):**
> «именно для начальной стадии вот джекса что мы все-таки будем действовать больше как мафия»
> [src: voice-extract:§1.9.4, audio_563]

**Phase 3 evolution:**
- Не open community с самого начала (anti-Discord, anti-LinkedIn)
- Closed Kingsman-inside trust (D1 layered identity §4)
- Phase 3 evolves: community of workshops с инфраструктурой координации между мастерскими
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 3]

### 10.8 Curated community access

> «Ценность сообщества определяется не массовостью, а качеством отобранных участников.»
> [src: wiki/concepts/curated-community-access.md:одна-строка]

**Прецеденты:** Apache Software Foundation, Linux Kernel maintainers, Y Combinator, Inner Circle, Founders Fund.

**Quality-gating:**
- Входной фильтр — адекватность, релевантность, готовность контрибьютить.
- Доверие по умолчанию внутри сообщества: каждого проверили.
- Участник не просто потребляет, а вносит вклад.
- Репутация и вклад — валюта внутри.
[src: wiki/concepts/curated-community-access.md:ключевые-свойства]

### 10.9 Synergy formula 6-component (alternative one-liner candidate)

> «эффект синергии ответственность блять и разграничение того в чем силен в чем не силен адекватное управление ресурсами и тогда поиск рычагов и так далее автоматизация всего что только можно занятия стратегическими делами видением»
> [src: voice-extract:§1.9.1, audio_537@26-04-2026]

6-component synergy formula = Workshop-as-engine model. Compact summary всех Workshop §1-§7 в одной фразе.

---

## 11. Anti-patterns Jetix Corp (что мы НЕ есть)

### 11.1 НЕ classic consulting firm (vs McKinsey / Big 4)

> «Они deliver reports, Jetix deliver методологию + ongoing productized workflows.»
> [src: decisions/JETIX-VISION.md:§10]

**Verbatim:**
> «мы не целимся на какое-то консалтинговое агентство… Jetix эта сеть которая позволяет консультантам и бизнесу адекватно и в реальном времени сотрудничать… под ней работают McKinsey и там еще какие-то остальные могут продолжать под ней работать»
> [src: audio_464, decisions/JETIX-VISION.md:§10]

**Jetix = networks-layer над consulting world, не compete-layer с McKinsey.**

### 11.2 НЕ AI стартап с продуктом

> «Они delivery AI-tools (chatbots, automations, dashboards). Jetix delivery методологию AI-leverage — как AI применяется, не что AI делает.»
> [src: decisions/JETIX-VISION.md:§10]

**Аналогия Westinghouse / Ford:**
- AI = электричество
- Методология = завод
- Исполнители = электрики
[src: wiki/analogiya-s-elektrichestvom.md, цитировано в decisions/JETIX-VISION.md:§10]

> «Vs SaaS / продукт-tech-startup narrative. D8 methodology, не product. Jetix не строит «ещё один инструмент» — строит способ применения инструментов.»
> [src: decisions/JETIX-VISION.md:§6]

### 11.3 НЕ holding company classic (vs BlackRock)

**TRM-MODEL §3.7 + §17:**
> «Универсальный «total resource manager», который объединяет все шесть ресурсов. Это белое пятно. Berkshire Hathaway но для Mittelstand operations.»
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§3.7]
❌ outdated frame "Mittelstand operations"

**1B skeleton placeholder:**
> «НЕ управляющая компания типа BlackRock. Не управляем investment portfolio. Управляем operational resources.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§12.5]

### 11.4 НЕ accelerator / incubator

> «Не тренинг для founders. Мы реальный operational partner.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:§12.4]

### 11.5 НЕ LinkedIn / TikTok / Instagram / YouTube

> «Vs LinkedIn: Jetix — не LinkedIn где быдло одно которое ищет каких-то рабов. Secure Network Phase 2+ = quality-gated alternative, ICP-filtered membership, anti-attention-economy stance.»
> [src: voice-extract:§1.5.2 + decisions/JETIX-VISION.md:§10]

> «Vs TikTok / Instagram / YouTube: attention extraction vs attention preservation. Jetix нацелена наоборот на сохранение внимания на усиление ускорение своих партнёров.»
> [src: holding-vision-2026-04-21 Note 2, decisions/JETIX-VISION.md:§10]

### 11.6 НЕ Notion / Obsidian / Roam

> «Они personal-OS tools, Jetix — методология, которая может use эти tools (integrates). Focus — human operator + AI-agent coordination, не note-taking.»
> [src: decisions/JETIX-VISION.md:§10]

### 11.7 НЕ One-Person-Company / One-Million-Company

> «Я не конкурирую с этим… One Million Company ещё что-то, нет. Или One Person Company. Нет у нас тут большая компания.»
> [src: holding-vision-2026-04-21 Note 3, decisions/JETIX-VISION.md:§10]

**Jetix = corporation tier (enterprise-fast), не solopreneur aesthetic.** Scale — международный, world-wide, мультимиллиарды выручки.

### 11.8 НЕ pyramid / scam / Oriflame / speculative hype

> «Это все должно быть не какая-то там ебаная пирамида или еще что-то. Нет. А реально адекватные инструменты, наработки, технологий.»
> [src: holding-vision-2026-04-21 Note 5]

> «не на широкие массы а конкретно на профессионалов»
> [src: holding-vision-2026-04-21 Note 2]

### 11.9 НЕ hour-billing-only consulting trap

> «D18 productization path — часы = entry, масштаб через шаблоны/фреймворки/пакеты, не через увеличение часов.»
> [src: decisions/JETIX-VISION.md:§6]

### 11.10 НЕ enterprise C-Level focus в Phase 1

> «Hard Rule: Phase 1 ICP — smart entrepreneurs + English-speaking infobiz, не Fortune-500 закупщики (они активируются Phase 3+).»
> [src: decisions/JETIX-VISION.md:§6]

### 11.11 НЕ pure open-source platform

> «D3 closed outside / D13 closed core. Open — только для inside + research-layer Phase 2+ (D24).»
> [src: decisions/JETIX-VISION.md:§6]

### 11.12 НЕ pure think-tank / philosophical retreat

> «Revenue + action первичны (D14 research = revenue-instrumental Phase 1). Философия и research-direction — Phase 2+ только.»
> [src: decisions/JETIX-VISION.md:§6]

### 11.13 НЕ mass-market consumer

> «Не Tony Robbins motivational circle, не философский retreat без action, не superficial networking, не attention-economy consumers.»
> [src: decisions/JETIX-VISION.md:§7.2 NOT target]

### 11.14 НЕ social media of any kind

> «это не хуйня типа тик тока который являть инстаграма или youtube а которая просто ну блять все дерьмо вместе»
> [src: voice-extract:§1.5.2, raw/voice-memos-text/community-addendum-2026-04-21.md:L36]

Workshop §1 «активный процесс»: social media = passive-consumption, Workshop = active-creation.

### 11.15 НЕ equity-based investor pitches в Phase 1

> «Skin-in-game (self-funded $20-30K earned) + D15 revenue-gated unlocks. Инвесторы приходят в Phase 2+ с validation.»
> [src: decisions/JETIX-VISION.md:§6]

### 11.16 НЕ slop-aggregator / low-quality content

См. §11.5 + §11.14. Jetix Workshop = quality-only, anti-slop.

### 11.17 НЕ research ради «великих дел» в Phase 1

> «D14 revenue-instrumental only. 200-year vision informs architecture decisions, но Phase 1 execution — только то, что serves near-term revenue.»
> [src: decisions/JETIX-VISION.md:§6]

### 11.18 НЕ public dispute с конкурентами / not aggression at people

> «Workshop НЕ есть = не predator agressive at people, but predator-outside framing tool для self-selection invitation»
> [src: decisions/JETIX-VISION.md:§4 D1 LOCKED Gentleman-inside / Predator-outside]

⚠️ **Subtle nuance:** "predator outside" — это **tone of self-selection invitation** ("самая большая авантюра века") + tone of competition response (kill McKinsey market share, не аdхоminem). НЕ aggression at clients, partners, members.

---

## 12. Connections с Базовой Системой (Документ 1A)

### 12.1 Базовая Система = каркас; Jetix Corp = applied use case

**1A LOCKED v1.0 2026-05-05:**
> «Базовая Система Управления — это архитектурный каркас персональной мастерской (метафора), которую любой амбициозный человек может построить под себя для управления своей жизнью, ресурсами, проектами и накопления опыта.»
> [src: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md:§0 TL;DR]

**1B relationship:**
> «Базовая Система = каркас (универсальный для любого мастера). Jetix Corp = специфическая реализация этого каркаса под конкретный бизнес-кейс.»
> [src: decisions/JETIX-CORPORATION-2026-05-05.md:reading-guide]

### 12.2 Foundation v1.0 LOCKED 2026-04-28 — 11 Parts + Pillars

> Этот раздел НЕ дублирует — Foundation Parts описаны полностью в Документе 1A разделе 4 / 5. Здесь только Jetix-specific notes.

**11 LOCKED Foundation parts:**
- Part 1 — System State Persistence (git substrate)
- Part 2 — Signal Ingestion & Triage (STOP-gate prихожая)
- Part 3 — Knowledge Base & Methodology Library
- Part 4 — Role Taxonomy & Coordination Protocol
- Part 5 — Compound Learning & Methodology Capture
- Part 6a — Provenance Officer (квартальный аудит)
- Part 6b — Human Gate (real-time страж)
- Part 7 — Project Lifecycle Substrate
- Part 8 — Health Monitoring & System Integrity
- Part 9 — Owner Interaction Scaffold
- Part 10 — External Touchpoints & Network Interface
- Part 11 — Strategic Direction Substrate (Pillar A)
[src: CLAUDE.md / Foundation Architecture v1.0 LOCKED + foundation-master-overview-human-2026-04-29.md]

### 12.3 Pillar A / B / C — Strategic Layer (LOCKED Bundle 5, 28.04)

- **Pillar A (Strategic Direction Substrate)** — system-wide direction; 6 strategic-doc types (Lock Entry / North Star / Strategic Insight / Direction Card / Phase Plan / Strategic Reflection); UC-A.1/A.2/A.3/A.4 hosting; Decisions DB
- **Pillar B (Bundle 5 supplement to Part 7)** — project-strategy slot; project-level стратегия
- **Pillar C (Foundation sub-system)** — two-tier (Tier 1 manager + Tier 2 system); foundation_generic + ruslan_layer_overrides; canonical source для Part 6b constitutional_never_list
[src: CLAUDE.md / Foundation Architecture v1.0 LOCKED]

### 12.4 Какие Jetix-specific дополнения поверх Foundation

**RUSLAN-LAYER overlay** (Layer 2 of 2 per Bundle 5 ack 28.04):

- DACH location ❌ (outdated frame; agnostic geographic)
- AI consulting domain ❌ (broader: AI-leverage methodology generic)
- Phase 1 €50K target ✓
- 11 archetypes ✓ (D1 Vision)
- Korp-Startup positioning ✓ (D29)
- Top Lists Partner Factory (выделено в JETIX-VISION-OF-SYSTEM RUSLAN-LAYER)
- Tseren Tserenov first partnership target ✓
- Mentor search (Phase 0 unblock — founder isolation as stopper)
- Voice-pipeline DRAFT-only discipline
- Manager attention budget 20 active tasks
- Hub-and-spoke routing
- A/B test awaiting_approval mandatory
- Filesystem source of truth
- API keys NEVER в файлах
- Russian content / English code
[src: decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md:RUSLAN-LAYER frame; CLAUDE.md §4.2]

**Note:** Foundation v1.0 — fork-portable. Завтра другой owner с другой нишей возьмёт Foundation, заменит RUSLAN-LAYER на medical-researcher-LAYER (или любую другую) — поедет дальше.
[src: foundation-master-overview-human-2026-04-29.md:final paragraph]

### 12.5 Hard rules / Constitutional principles (Pillar C Tier 2)

**11 hard rules — Foundation generic** (zercalo FUNDAMENTAL §6.1):

1. AI **не** принимает стратегических решений
2. AI **не** делает архитектурных изменений без ворот
3. AI **не** определяет направление skill-acquisition
4. AI **не** претендует на персональную identity (только `acting_as` роль)
5. AI **не** претендует на skin-in-the-game / собственность / последствия
6. AI **не** аккумулирует unstructured long-term память
7. Агенты **не** разрешают противоречия автономно (только через human gate)
8. Агент **не** оценивает другого агента без human review
9. AI **не** self-modify в runtime
10. AI **не** имитирует человека снаружи без disclosure
11. **Никаких** действий без blast-radius classification + Default-Deny
[src: foundation-master-overview-human-2026-04-29.md:§3 Tier 2; CLAUDE.md §4.1]

**Зеркало:** `.claude/config/default-deny-table.yaml` constitutional_never_list, который Part 6b использует для каждого runtime-check. Lint следит, что зеркало не разъезжается с canonical.

### 12.6 Founder isolation as stopper class (Phase 0 critical)

> «Solo-founder без external counterpart (mentor / strategist / PM / partner-in-thinking) деградирует quality of strategic decisions через blind spots + group-of-one effect; это **класс операционных blockers**, не разовая ситуация.»
> [src: wiki/concepts/founder-isolation-as-stopper-class.md]

**Operationalisation для Jetix:**
- Active workstream: `swarm/wiki/operations/quick-money/personal-mentor-search/`
- Approach: «сотрудничество first, paid only if mutual fit»
- 3 типа параллельно (Type 1 Mentor / Type 2 Facilitator / Type 3 Consultant)
- Cap €500 на ВСЁ
- Long-term resolution: D26 Team 50-100 Phase 2+ scaling

**Anti-pattern:** перешёл в isolation; skin-in-game preserved; готовы платить если нужно, но не отчаянно.

### 12.7 IP-1 Role≠Executor

**FPF IP-1 + Bundle 1 D-1 anti-conflation:**
> «Foundation роли = U.Episteme abstract role-types (manager, strategist, sales-lead, etc.); executor bindings (specific agents like `claude-opus`, `sonnet-4-6`) = RUSLAN-LAYER per `shared/schemas/executor-binding.yaml.template`. Foundation parts MUST NOT name executor instances.»
> [src: CLAUDE.md §Critical Tier-2 Principles]

**Practical:** Если завтра ты переедешь на другую модель — роль останется, executor поменяется.
[src: foundation-master-overview-human-2026-04-29.md:§Part 4]

### 12.8 Foundation as $1T scale infrastructure

> «фундамент надо строить с такой видением и целью, что будет просто 100 миллиардов выручка person company… как будто бы мы сейчас… ну реально качественно умно с первого начала ну просто вот заложено потом чтобы мы могли просто люто масштабироваться»
> [src: holding-vision-2026-04-21 Note 5]

> «Foundation Architecture v1.0 LOCKED 28.04 (CLAUDE.md) is exactly this $1T infrastructure foundation. Workshop concept §1.5 «Knowledge accumulates» needs durable substrate — Foundation v1.0 = substrate.»
> [src: voice-extract:§1.9.5]

**Engineering principle:** Phase 1 architecture carries $1T scale без редизайна. Infrastructure-from-Day-1 (Decision 19).
[src: decisions/JETIX-VISION.md:§14]

### 12.9 Что Jetix добавляет к Foundation специфически

> На уровне metaphor: Workshop specialization — каждый мастер строит мастерскую под свою нишу.
> На уровне offering: TRM 6 ресурсов модель + Producer Center + Land-and-Expand 6 уровней.
> На уровне ICP: 2 оси × 3 типа участников (см. §7).
> На уровне ambition: $1T trajectory + 200-year civilizational infrastructure vision.
> На уровне identity: Layered identity (D8) — 8 разных лиц per observer / phase.
> На уровне values: Open Source / Linux philosophy + Revenue Share contract + Curated Community Access.
> На уровне governance: Korp-Startup positioning (responsibility-as-scale).
> На уровне sales motion: «гипотеза за €3k → TRM-full €40-60k/мес» (land-and-expand).
> На уровне brand: Gentleman inside / Predator outside grammar.
[src: synthesis from JETIX-WORKSHOP-CONCEPT + JETIX-TRM-MODEL + JETIX-VISION + wiki/concepts/* + voice-extract]

### 12.10 Foundation Build Master Plan reference

**Foundation Architecture v1.0 LOCKED tag:** `foundation-architecture-locked-2026-04-28`.

**8 RUSLAN-ACK records** (Bundle 1-5 + Wave D + Strategic Layer):
- Bundle 1 (Parts 1/2/4/6a) + supplement 1 + supplement 2
- Bundle 2 (Parts 3/5/6b)
- Bundle 3 (Parts 8/10)
- Bundle 4 (Parts 7/9)
- Wave D Integration Pass — Coverage 55/55; Inter-Part 98.1%; M3 8/8; STANDALONE PRESERVED 2.2× margin
- Bundle 5 Strategic Layer Foundation — Pillar A/B/C structural placement + CLAUDE.md HYBRID + FUNDAMENTAL hierarchy Option 2
[src: CLAUDE.md / Foundation Architecture v1.0 (LOCKED) section]

---

## 📎 Appendix — Список просканированных источников

### A. Decisions (canonical LOCKED docs + drafts)

#### A.1 LOCKED canonical (HIGH priority pulled)

| File | Status | Date | What it covers |
|------|--------|------|----------------|
| `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` | LOCKED canonical | 2026-04-30 | Workshop metaphor v2; supersedes house metaphor; verbatim Ruslan dictation |
| `decisions/JETIX-TRM-MODEL-2026-04-30.md` | Черновик-концепция April 2026 | 2026-04-30 | Total Resource Management — 6 ресурсов, fees, lestnitsa 6 уровней, Phase 3 platform |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | LOCKED v1.0 | 2026-04-27 | 35 use cases × 12 categories, generic sector-agnostic Layer 1 |
| `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | LOCKED v1.0 (Документ 1A) | 2026-05-05 | Universal foundation; что есть Базовая Система; 11 problems analysis |
| `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-{1,1-supp,1-supp-2,2,3,4}-2026-04-28.md` | LOCKED ack | 2026-04-28 | Foundation Bundle 1-4 ack records |
| `decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md` | LOCKED | 2026-04-28 | Wave D coverage 55/55 |
| `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` | LOCKED | 2026-04-28 | Strategic Layer Pillar A/B/C placement |
| `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | LOCKED brief | 2026-04-27 | Foundation Build Master Plan |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | LOCKED audit | 2026-04-27 | Current state audit pre-Foundation build |

#### A.2 Drafts / WIP / Stage 3 outputs

| File | Status | Date | What it covers |
|------|--------|------|----------------|
| `decisions/JETIX-CORPORATION-2026-05-05.md` | SKELETON v0.1 (the target!) | 2026-05-05 | 1B skeleton with 12 sections to fill |
| `decisions/JETIX-VISION.md` | D1 draft | 2026-04-21 | Identity Document — 24 LOCKED decisions, 11 archetypes, 5 ICP filter, $1T trajectory, layered identity |
| `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` | RUSLAN-LAYER WIP | 2026-04-27 | Layer 2 overlay — current Ruslan situation |
| `decisions/JETIX-PHILOSOPHY.md` | D2 draft | 2026-04-21 | Philosophy and reasoning (parallel to D1, не прочитан полностью) |
| `decisions/JETIX-PLAN.md` | D3 draft | 2026-04-21 | Execution plan по фазам, €50K Q2 2026 roadmap |
| `decisions/JETIX-ARCHITECTURE-BRIEF.md` | D4 brief | ~2026-04-21 | Compressed technical архитектура (не прочитан) |
| `decisions/JETIX-PLAN.md §3.1.1` | Migration note 2026-04-24 | 2026-04-24 | Revenue-mix decomposition: contracts €30K + hourly €35K = €65K target |

#### A.3 Other decisions (LOW priority — not pulled, indexed only)

| File | Date | Theme |
|------|------|-------|
| `decisions/JETIX-PHILOSOPHY.md` | 2026-04-21 | D2 Philosophy 983 lines |
| `decisions/JETIX-SYSTEM-OVERVIEW.md` | 2026-04-24 | 14 layers SYSTEM-OVERVIEW |
| `decisions/JETIX-ARCHITECTURE-BRIEF.md` | 2026-04-21 | D4 brief |
| `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` | 2026-04-22 | Master synthesis 185K |
| `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` | 2026-04-24 | Foundation → Execution master plan |
| `decisions/STRATEGIC-INSIGHT-{AI-PSY-LED-DESIGN,ARBITRAGE-TRAFFIC-DIRECTION,JETIX-AI-BIOS-MOMENT,MA-DIRECTION}-2026-04-24/25/26.md` | 2026-04-24 to 26 | 4 Strategic Insights |
| `decisions/LAYER-{5,6,7}-{PRODUCT-DIRECTIONS,COMMUNITY,BUSINESS-TRAJECTORY}-DEEP-DIVE.md` | 2026-04-24/25 | 3 Layer deep dives (large files) |
| `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | 2026-04-24 | Strategic horizon vision |
| `decisions/SWARM-SELF-IMPROVEMENT-{HYPOTHESES,OPPORTUNITIES}-2026-04-23.md` | 2026-04-23 | Swarm self-improvement |
| `decisions/ROY-{AGENTS-BUILT,ALIGNMENT,INFORMATION-DIET}-2026-04-22/23.md` | 2026-04-22/23 | ROY swarm decisions |
| `decisions/LOCKS-D{25-D28,D29}-ADDENDUM-2026-04-{24,26}.md` | 2026-04-24/26 | Decision locks addenda |
| `decisions/AWAITING-APPROVAL-*` (~10 files) | 2026-04-22 to 28 | Stage gates awaiting approval (most ack'd already) |

### B. Wiki entries

#### B.1 Wiki/ideas (HIGH priority — all 10 jetix-* read)

| File | Date | Theme |
|------|------|-------|
| `wiki/ideas/200-year-vision-jetix-humanity.md` | 2026-04-16 | Civilizational 200y vision |
| `wiki/ideas/founder-responsibility-jetix-constitution.md` | 2026-04-16 | Constitutional principles |
| `wiki/ideas/investment-fund-jetix-component.md` | 2026-04-16 | Phase 2 fund component |
| `wiki/ideas/jetix-agency-strategic-ai-partners.md` | 2026-04-16 | 4-step ladder of value (Audit → Equity) |
| `wiki/ideas/jetix-as-infrastructure-metaphor.md` | 2026-04-16 | Дорога/машины metaphor |
| `wiki/ideas/jetix-corporation-1000-pros-100k-agents.md` | 2026-04-16 | North Star — 1000+ профи + 100K agents |
| `wiki/ideas/jetix-open-source-philosophy.md` | 2026-04-16 | Linux-style 3 principles |
| `wiki/ideas/merchants-analogy-jetix-unifies-via-ai.md` | 2026-04-16 | Historical analogy |
| `wiki/ideas/open-source-premium-jetix-model.md` | 2026-04-16 | Open kernel + Premium |
| `wiki/ideas/revenue-share-jetix-philosophy.md` | 2026-04-16 | Revenue share principle (could take 70%, doesn't) |

#### B.2 Wiki/concepts (HIGH priority — all 6 read)

| File | Date | Theme |
|------|------|-------|
| `wiki/concepts/korporaciya-startup-concept.md` | 2026-04-26 | Корпорация-стартап D29 positioning |
| `wiki/concepts/jetix-open-source-principles.md` | 2026-04-16 | Three open-source principles |
| `wiki/concepts/curated-community-access.md` | 2026-04-16 | Quality-gated community |
| `wiki/concepts/founder-isolation-as-stopper-class.md` | 2026-04-26 | Founder isolation operational blocker |
| `wiki/concepts/digital-sovereignty.md` | 2026-04-16 | Digital sovereignty positioning |
| `wiki/concepts/value-three-layers.md` | 2026-04-16 | Ценить-знать-делать |

#### B.3 Wiki/foundations (LOW priority — universal Foundation; не pulled per anti-duplication rule)

Содержание Foundation Parts 1-11 + Pillars A/B/C — описано в Документе 1A; **НЕ дублируется** здесь.

### C. Design docs

| File | Status | Date | What it covers |
|------|--------|------|----------------|
| `design/JETIX-FPF.md` (NOT in decisions/) | Constitutional spec | 3758 lines | FPF-Steward governed; IP-1/IP-2/IP-3/IP-7 + A.6.B + A.14 + B.3 (LOW priority — referenced in CLAUDE.md) |
| `design/JETIX-ARCHITECTURE-WORKING.md` | working-draft | 2026-04-18 | 8-layer architecture working draft, post-research synthesis (PARTIAL pull, §4 8-layer model 🟡 superseded by Foundation v1.0 11 Parts) |
| `SYSTEM-DESIGN-HUMAN.md` (root, NOT design/) | v1-beta-FINAL | 2026-04-18 | Целевая система Jetix OS на человеческом языке; primary-goal $50K Q2 2026 (PARTIAL pull) |
| `design/SYSTEM-DESIGN-TECH.md` | v1-beta | 2026-04-18 | Technical synthesis (LOW priority) |
| `design/SYSTEM-DESIGN-TECH-SUMMARY.md` | v1-beta-FINAL | 2026-04-18 | 15-min executive summary (LOW priority) |
| `design/SYSTEM-DESIGN-INPUTS.md` | inputs | 2026-04-18 | Шпаргалка с тезисами (LOW priority) |
| `design/ARCHITECTURE-TARGET.md` | reference | 2026-04-18 | Current vs v1-beta vs v1-final vs v2 (LOW priority) |
| `design/IMPLEMENTATION-PLAN-2026-04-18.md` | plan | 2026-04-18 | Action plan Шагов 3-6 (LOW priority) |
| `design/JETIX-FPF.md` | constitutional | various | LOW priority (3758 lines; constitutional ref via CLAUDE.md) |

### D. Synthesis files (server CC outputs)

| File | Date | Theme |
|------|------|-------|
| `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md` | 2026-05-01 | Workshop voice-extraction draft (47 transcripts), 9 sub-sections + 4 action types |
| `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` | 2026-04-29 | Human-readable Foundation overview, 11 Parts narrative |
| `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` | 2026-04-29 | Technical overview (1590 lines, LOW priority — too long) |
| `swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md` | 2026-04-30 | Plan Mode + ultrathink pilot design (PARTIAL pull) |
| `swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md` | 2026-05-02 | Claude Code OS analysis (LOW priority) |
| `swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md` | 2026-05-02 | Malware partnership analysis (LOW priority) |
| `swarm/wiki/synthesis/foundation-visuals-2026-04-30/` | 2026-04-30 | Visual diagrams (D2, multiple files) |

🟡 **GAP FLAGGED:** `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` — **NOT FOUND**. Файл упомянут в `decisions/JETIX-CORPORATION-2026-05-05.md` frontmatter sources, но физически отсутствует. Либо не создан, либо удалён, либо path mistype. См. также pilot-design-plan-2026-04-30.md:L28 — там тот же файл flagged как «NOT FOUND (find подтвердил отсутствие)».

### E. Raw research (LOW priority — all listed, not pulled)

#### E.1 Hybrid framework synthesis (entry point)
- `raw/research/hybrid-framework-synthesis-2026-04-18.md` — 8-layer synthesis (101K)
🟡 superseded by Foundation v1.0 (28.04)

#### E.2 8 Phase deep-research files (18-19.04)
- `software-deep-research-2026-04-18.md`
- `levenchuk-deep-research-2026-04-18.md`
- `levenchuk-fpf-research-2026-04-20/`
- `platform-os-deep-research-2026-04-18.md`
- `community-deep-research-2026-04-18.md`
- `consulting-deep-research-2026-04-18.md`
- `product-deep-research-2026-04-18.md`
- `agency-deep-research-2026-04-18.md`
- `holding-deep-research-2026-04-18.md`

#### E.3 Architecture variants & extractions (April 18-22)
- `architecture-implementation-synthesis-2026-04-19.md`
- `architecture-synthesis-v2-final.md`
- `architecture-variants-2026-04-22/` (TENSIONS-PRE-RESOLVED, TENSIONS-RESOLVED, TENSIONS-RESOLVED-STAGE-2B, ATOM-REGISTRY, KNOT-MAP, OME-ARCHITECTURE-REFERENCE, VOICE-MEMOS-FULL-DIGEST, VOICE-MEMOS-COMMUNITY-ADDENDUM, VOICE-MEMOS-YEAR-PLAN, HOLDING-VISION-SYNTHESIS)

#### E.4 Specialized research
- `agency-deep-research-2026-04-18.md`, `antivirus-kaspersky-research.md`, `braginsky-antivirus-modeling.md`, `career-levels-deep-research-2026-04-19.md`, `claude-code-os-course-2026-05-02-transcript.md`, `company-as-code-impl-deep-research-2026-04-19.md`, `compounding-engineering-2026-04-22/`, `crm-sales-architecture-deep-research-2026-04-19.md`, `folder-structure-deep-research-2026-04-19.md`, `fpf-gap-analysis-2026-04-20.md`, `jetix-life-separation-deep-research-2026-04-19.md`, `knowledge-architecture-deep-research-2026-04-19.md`, `master-inventory-2026-04-22.md`, `mega-corp-governance-deep-research-2026-04-19.md`, `org-chart-in-git-deep-research-2026-04-19.md`, `perplexity-market-ai-native-2026-04-22/`, `phase-2-deep-research-2026-04-22/`, `2026-04-25-arbitrage-traffic-deep-dive.md`, `2026-04-25-wall-street-ma-deep-dive.md`, `2026-04-28-tseren-tg-export/`, `2026-04-28-tseren-yt-export/`, `2026-04-29-wiki-roy-compounding/`, `d6-reviews/`, `step-2-1-extractions/`, `step-2-2-2-extractions/`, `step-2-2-3b-extractions/`, `step-2-2-3c-extractions/`, `step-2-2-4-extractions/`, `stage2-review/`, `2026-04-24-bios-clone-wars-jetix-ai-parallel.md`

#### E.5 Voice memos (text form, primary anchor source)
- `raw/voice-memos-text/holding-vision-2026-04-21.md` — 6 notes, $1T / USB-C / tokens / mafia framing
- `raw/voice-memos-text/community-addendum-2026-04-21.md` — 2 notes, Community + Secure Network
- `raw/transcripts/audio_530-586` — 47 transcripts (period 24-30.04), Workshop genesis 30.04 (audio_582-586)

### F. Reports (HIGH+MED priority pulled)

| File | Date | Theme |
|------|------|-------|
| `reports/retrospective_2025-05_to_2026-04.md` | 2026-05-03 | 12 months Phase 1/2/3 trajectory ✓ pulled |
| `reports/review_2026-04-26-DEEP.md` | 2026-04-26 | DEEP review of audio_530-539 (LOW priority — covered in voice-extract) |
| `reports/review_2026-05-01.md` | 2026-05-01 | Latest weekly review (LOW priority) |
| `reports/review_2026-05-01-STRUCTURED.md` | 2026-05-01 | Structured review (LOW priority) |
| `reports/review_2026-05-01-BACKLOG-FLAG.md` | 2026-05-01 | Backlog flag (LOW priority) |
| `reports/notion-alpha-extraction-2026-04-16.md` | 2026-04-16 | Notion extraction (LOW priority) |
| `reports/architecture-inventory-2026-04-16.md` | 2026-04-16 | Architecture inventory (LOW priority) |
| `reports/activity_2026-05-03.md` | 2026-05-03 | Recent activity (LOW priority) |

### G. Foundations (Foundation Parts canonical — Документ 1A)

> **NOT pulled (per anti-duplication rule).** Каждая Part architecture.md — описана в Документе 1A разделе 4. Здесь только index.

- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`
- `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md`
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md`
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md`
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md`
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md`
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md`
- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` + `bundle-5-supplement-pillar-b.md`
- `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md`
- `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md`
- `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md`
- `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md`
- `swarm/wiki/foundations/principles/architecture.md` (Pillar C)
- `swarm/wiki/foundations/{engineering,investing,mgmt,philosophy,systems}/` (5 expert lenses, LOW priority — not pulled)

### H. Notion pages (LOW priority — referenced but not fetched)

| ID | Page |
|----|------|
| 3322496333bf8161b6d3ea789d039356 | Command Center |
| 30a24963-33bf-8005-817a-000beb10bcd4 | Daily Log DB |
| 69a3c581-ab33-48d9-9827-ec8a8bb69d14 | Projects DB |
| 89c2ac5e-797e-4bff-bd53-4316026f8094 | Journal of Chats |
| bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7 | Банк идей |
| 3372496333bf8125a72cd7352124b5ee | ICP Page |
| 32c2496333bf81e8807cd490f9d17872 | Research Hub |
| 3322496333bf8184b31bc985a93222d7 | Life OS |
| 3522496333bf817f836edb0c0a25b28e | Workshop concept LOCKED (Notion mirror) |
| 3522496333bf8107b5dae9e000846747 | TRM model LOCKED (Notion mirror) |
| 3542496333bf81cb9e15d7b49410db73 | Гипотеза abstraction levels CPU/Memory |
| 34e2496333bf816cb421c263beec172f | Jetix Vision Fundamental |

🟡 **Per Pillar C TIER-2 RUSLAN-LAYER §4.2:** «Filesystem = source of truth; Notion = view (not authoritative).» Notion mirror docs не pulled — filesystem canonical.

### I. CLAUDE.md / Configuration (HIGH priority — included in boot context)

- `CLAUDE.md` — Master Configuration (auto-loaded по boot)
- `.claude/rules/global.md` — Global rules
- `.claude/config/default-deny-table.yaml` — Pillar C constitutional_never_list
- `.claude/config/project-types.yaml` — KM MVP project templates

### J. Notable wiki/sources (raw notion-ideas) — LOW priority

`wiki/sources/2026-04-16-jetix-*.md` — raw source files for wiki/ideas/ entries. NOT pulled (already represented в curated wiki/ideas).

---

## 📊 Closing Summary

**Источники отсканированы:** ~30 HIGH/MEDIUM priority pulled deeply; ~120+ LOW priority indexed only in Appendix.

**Distribution:**
- **11 LOCKED canonical** (Workshop, TRM, Vision FUNDAMENTAL, Foundation Parts 1-11, Pillar C, RUSLAN-ACK Bundle 1-5, Wave D, BASE-MGMT 1A, Foundation Build Master Plan Brief, AUDIT-CURRENT-STATE)
- **~7 drafts / WIP** (Vision-D1, Philosophy-D2, Plan-D3, Architecture-Working, Vision-of-System RUSLAN-LAYER, voice-extract, retrospective)
- **~3 superseded / outdated** (legacy 8-layer architecture; «house» metaphor → workshop; «Mittelstand DACH» ICP frame)

**3-5 main findings:**
1. **Workshop = canonical Jetix metaphor** (LOCKED 30.04) и заменяет «дом» из foundation-master-overview. Verbatim Ruslan dictation 30.04 evening — primary anchor для §2 в 1B.
2. **TRM business model — комплексная**: 6 ресурсов, mgmt + performance fee, лестница 6 уровней (€3k → €40-60k/мес), 3 фазы эволюции (Phase 1 service / Phase 2 management / Phase 3 platform). Phase 3 marketplace = $1.5-3B valuation если 1000 Operators × 3 клиента.
3. **ICP — Ruslan отверг "Mittelstand DACH"**, заменив на 2 оси (ресурсы + желание развиваться) × 3 типа (Solo/Indie revenue share / mid-business mgmt+%growth / TRM-делегаторы full TRM). Старые 11 archetypes + 5 critical filter (Startupper/Azart/Stable/Adequate/Upward) **complementary**, не conflicting — distribute across 3 типа.
4. **Foundation v1.0 — fork-portable infrastructure** (LOCKED 28.04). Jetix Corp = applied use case; Jetix-specific = RUSLAN-LAYER overlay. **$1T scale baked in от Day 1.**
5. **Phase 1 €50K Q2 2026** = единственная committed absolute date. Revenue mix: €30K productized contracts + €35K hourly = €65K target (~30% margin). Hourly NOT optional — 233h/Q1+Q2 mandatory.

**Conflicts / противоречия обнаружены:**
- ⚠️ **1B skeleton frontmatter line 37 "Mittelstand DACH 50-500 emp" CONTRADICTS §7 body** (which explicitly rejects Mittelstand frame). Frontmatter нужно обновить.
- ⚠️ **Phase 1 markets:** D1/D3 (21.04) emphasize English+US infobiz; TRM-MODEL (30.04) implies Mittelstand DACH primary. TRM Mittelstand = illustrative (не committed market).
- ⚠️ **Workshop Phase 2 vs TRM Phase 2:** Workshop emphasizes "одна система"; TRM emphasizes 30+ клиентов через AI-агентов scale. Concepts complementary но vocabulary collision.
- ⚠️ **Layered identity** (D1 8 faces) vs **3 типа участников** (1B) — different facets, нужна reconciliation в §1 1B.

**Gaps (нет материалов в текущей базе):**
- 🟡 `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` — **MISSING** (referenced в 1B frontmatter + pilot-design-plan, физически отсутствует).
- 🟡 §6.3 «Что если не получится» (1B) — minimal material; нужно дописать explicit fallback section.
- 🟡 §10.1-10.3 (1B) Synergy / network effects — material есть, но нужна кристаллизация в business-prose form (vs voice-extract dispersed).
- 🟡 §9.1 (1B) Q2 2026 €50K — concrete plan present (JETIX-PLAN.md §3), но нужна compression to ≤500 words for partner audience.
- 🟡 «Большая афёра века» framing присутствует в 21.04 voice; в 30.04+ docs отходит. Нужно решить — preserve как brand framing или сместить акцент в engineering-faith / TRM categorization.

**Готовность к использованию для заполнения 1B:** **HIGH.** Документ покрывает все 12 секций 1B skeleton + appendix sources. Cloud Cowork CC может опираться на этот файл вместо чтения 50+ scattered docs. Рекомендуемая sequence заполнения 1B по разделам: §1 (definition) → §2 (Workshop) → §3 (TRM) → §7 (ICP — critical Mittelstand frontmatter fix) → §6 (afera) → §11 (anti-patterns) → §4-5 (platform/managing) → §8 (vision 1/3/10) → §9 (€50K roadmap) → §10 (synergy) → §12 (1A connections) → §0 TL;DR (last).

---

**END Jetix Source Collection.**
