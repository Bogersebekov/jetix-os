---
title: Brigadier prompt — rewrite Foundation Master Overview Human через метафору Мастерской
type: brigadier-prompt
created: 2026-05-06
target: server CC + ROY swarm на branch claude/jolly-margulis-915d34
purpose: переписать `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (метафора «дом» 676 строк) под новую canonical метафору «Мастерская» с глубокой grounding в LOCKED documents 1A, 1B и Foundation v1.0
priority: P1 (canonical Foundation-level deliverable)
estimated_effort: 6-12 hours brigadier work через Phases A-D
discipline: Foundation-level path → Default-Deny per Tier 2 rule 2 → AWAITING-APPROVAL packet required
---

# 🔨 BRIGADIER PROMPT — Rewrite Foundation Master Overview Human через Workshop metaphor

## §0 Mission Statement

**Что:** полностью переписать `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (sometimes "human overview", 676 строк, метафора «дом») в новый файл с **canonical метафорой «Мастерская»** (Workshop), описывающий все 11 Foundation Parts + Pillar C через workshop frame.

**Зачем:** существующий human overview использует **superseded** метафору «дом» которая была заменена canonical concept «Мастерская» в LOCKED документах 30.04 (`decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`) и 05.05/06.05 (`decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` Документ 1A LOCKED v1.0 + `decisions/JETIX-CORPORATION-2026-05-05.md` Документ 1B LOCKED v1.0). Human overview должен быть **выровнен** с canonical metaphor.

**Что НЕ делаем:** technical overview (`foundation-master-overview-technical-2026-04-29.md`) — НЕ ТРОГАЕМ. Он остаётся как есть (1590 строк technical reference). Его возможно скорректируют позже отдельной задачей — но НЕ в этом цикле.

**Output:** новый файл `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (или подобное naming с явным `-workshop-` маркером). Old file `foundation-master-overview-human-2026-04-29.md` помечается как `superseded_by:` (НЕ удаляется — append-only discipline).

---

## §1 Sources — что ОБЯЗАТЕЛЬНО прочитать ПЕРЕД написанием

> *Список приоритезирован. Каждый файл — `[src: path]` для будущей attribution.*

### 🔴 PRIMARY canonical sources (must read fully)

#### 1.1 Документ 1A — Базовая Система Управления (LOCKED v1.0)
- **Path:** `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md`
- **Размер:** ~2530 строк
- **Status:** LOCKED v1.0 (git tag `base-management-system-locked-2026-05-05`)
- **Что взять:**
  - §2 Метафора Мастерской — **главный framework** (7 элементов мастерской: фундамент / охрана / склад / станки / мастера / автоматизация / телефон)
  - §2.0 Первый принцип — **«всё есть информация»**
  - §2.4 Адаптивность станков
  - §2.5 Роль владельца (5 ролей: архитектор / арбитр / дегустатор / исполнитель / судья)
  - §3 Принципы (6 принципов: ценность / 4-фаза pipeline / внимание / время / ресурсы / knowledge)
  - §4 Архитектура 11 Foundation Parts + Pillar C — **canonical 6-group structure**
  - §6 Knowledge Accumulation — 3 уровня Wikipedia
  - §0 TL;DR — за один абзац всё

#### 1.2 Документ 1B — Jetix Corporation (LOCKED v1.0)
- **Path:** `decisions/JETIX-CORPORATION-2026-05-05.md`
- **Размер:** ~3845 строк
- **Status:** LOCKED v1.0 (git tag `jetix-corporation-locked-2026-05-06`)
- **Что взять:**
  - §2 Jetix как Мастерская — **расширение метафоры через 3 фазы** (Phase 1 одна → Phase 2 команда → Phase 3 community мастерских)
  - §2.4 Jetix-specific станки
  - §6.7 Авантюра управления (контекст почему адекватные люди в управлении)
  - §11 Синергия / network effects
  - §0 TL;DR

#### 1.3 Foundation Workshop concept LOCKED
- **Path:** `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- **Размер:** 271 строка
- **Status:** LOCKED 30.04
- **Что взять:** ОРИГИНАЛЬНЫЙ canonical Workshop concept — **источник всех формулировок**. Особенно:
  - §1 Почему мастерская
  - §2 Информация
  - §3 Роль владельца
  - §4 Input → System → Output
  - §6 3 фазы эволюции
  - §8 Verbatim Ruslan quotes
  - §10 Mapping старая «дом» metaphor → новая «workshop»

#### 1.4 ВСЕ 11 Foundation Parts + Pillar C
- **Path:** `swarm/wiki/foundations/part-1-...architecture.md` через `part-11-...architecture.md` + `swarm/wiki/foundations/principles/architecture.md`
- **Total:** ~16,065 строк (см. consolidation report §5 для exact sizes)
- **Что взять:** **§0 Mission** каждой Part + ключевые «Purpose» / «Inputs-Outputs» / «Laws» для **переформулировки в workshop language**.
- **Не нужно:** все Schemas / Sources / F-G-R details (это в technical overview).

#### 1.5 Existing Foundation Master Overview Technical (для context, НЕ для rewriting)
- **Path:** `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md`
- **Размер:** 1590 строк
- **Что взять:** §0 Executive + §1 Vision↔Architecture bridge + §14 cross-cutting. Используется как **structure reference** (как 11 Parts integrate), но **НЕ копируется** stylistically (он technical, мы пишем human).

#### 1.6 Existing Foundation Master Overview Human (то что superseded)
- **Path:** `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md`
- **Размер:** 676 строк
- **Что взять:** **structure reference только** — как организован narrative-style разбор 11 Parts. **НЕ копировать метафору «дом»**. Этот файл будет помечен `superseded_by:` после ship'а нового overview.

#### 1.7 Wave D Integration Report
- **Path:** `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`
- **Размер:** 684 строки
- **Что взять:** §1-§3 для понимания как 11 Parts связаны (52-edge inter-Part graph + 8 system-wide scenarios) — это станет основой §4 Architecture flow в новом overview.

### 🟡 SECONDARY sources (skim для context)

#### 1.8 Workshop deep narrative (если в repo есть)
- **Path:** `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md`
- **Note:** в consolidation report flagged как gap (NOT FOUND в filesystem). Если на самом деле есть — прочитай.

#### 1.9 Voice extract Workshop people
- **Path:** `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
- **Что взять:** verbatim Ruslan quotes про специализацию мастеров / breadth professionals / station tools (audio_565, audio_583, audio_585, audio_586).

#### 1.10 12-month retrospective (для контекста evolution)
- **Path:** `reports/retrospective_2025-05_to_2026-04.md`
- **Что взять:** Phase 1/2/3 trajectory как контекст откуда эта метафора пришла.

### 🔵 NOT sources (explicitly ruled out)

- ❌ `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` — pre-Foundation roadmap (outdated)
- ❌ `wiki/ideas/jetix-as-infrastructure-metaphor.md` — параллельная alternative metaphor (дорога/машины), может coexist но НЕ primary
- ❌ Any `AWAITING-APPROVAL-*` files до Bundle 5 ack (superseded by LOCKED state)

---

## §2 Workshop Metaphor — Ground Rules для Rewrite

> *Эти правила НЕ обсуждаются — они LOCKED в Документе 1A §2 + Workshop Concept. Все формулировки должны соответствовать.*

### 2.1 Главный принцип
**«Всё есть информация».** Мастерская работает **только с информацией** (даже когда управляет реальными ресурсами клиента — она управляет **информацией о ресурсах** + decisions, а не байтами на счёте).

### 2.2 Метафора (canonical, LOCKED)
**Мастерская** = место где работает **мастер** + есть **adaptable станки** + производятся **уникальные артефакты** + **knowledge accumulates** через time.

### 2.3 7 базовых элементов мастерской (canonical)
Каждой Part / Pillar **должен** быть mapped к одному (или нескольким) из этих 7 элементов:

| Элемент | Что |
|---------|-----|
| 🏗️ **Фундамент** | substrate (где живут данные / правила существования) |
| 🛡️ **Охрана** | filter на входе (что впускаем / что отбрасываем) |
| 📦 **Склад** | хранилище материалов и готовых изделий |
| 🔧 **Столы и станки** | adaptable инструменты под конкретные операции |
| 👤 **Мастера** | сам владелец + AI-агенты + помощники |
| 🤖 **Автоматизация** | рутина выполняется без участия мастера |
| 📞 **Телефон** | связь с другими мастерами / мастерскими (внешние интеграции) |

### 2.4 Adaptable станки
Главное свойство мастерской: **станки можно быстро добавлять / удалять / переделывать** под текущую задачу. Не статичная система.

### 2.5 Роль владельца (5 ролей)
- 🏗️ Архитектор
- ⚖️ Арбитр
- 👨‍🍳 Дегустатор
- 🛠️ Исполнитель
- ⚖️ Судья

### 2.6 3 фазы эволюции (canonical)
- Phase 1: одна мастерская одного владельца
- Phase 2: команда работает с одной мастерской
- Phase 3: community мастеров с своими мастерскими (mega-system)

### 2.7 Категорические запреты (НЕ использовать)

| ❌ НЕ использовать | ✅ Вместо этого |
|--------------------|------------------|
| Метафора «дом» (подвал / кладовая / etc.) | Мастерская (фундамент / склад / etc.) |
| «Комнаты» дома | «Цеха» / «зоны» / «отделы» мастерской |
| «Прихожая» | Охрана / ресепшн / приёмка |
| Старая 11-layer business architecture (L0-L7 из JETIX-ARCHITECTURE-WORKING) | 11 Foundation Parts + Pillar C |

### 2.8 Mapping старых cluster names → новые workshop language

> *Источник: `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` §10*

| Cluster (Foundation Parts) | Старая «дом» (NOT to use) | Новая Workshop (use) |
|---------------------------|---------------------------|----------------------|
| Substrate (P1) | 🏗 Подвал | 🏭 **Фундамент мастерской** — git как основа |
| Governance (P6a/6b + Pillar C) | 🛡 Несущие стены | 🚨 **Охрана + правила безопасности** — Provenance + Human Gate |
| Knowledge (P2/P3) | 📚 Кладовая | 📋 **Приёмная + Склад материалов и чертежей** — Triage + Wiki |
| Work (P4/P5/P7) | ⚙ Рабочие комнаты | 🔨 **Рабочие столы + Станки + Workflow** — Coordination + Compound Learning + Project Lifecycle |
| Interaction (P8/P9/P10) | 🚪 Гостиная и дверь | 📞 **Front-office + Радиосвязь** — Health + Owner Interaction + External |
| Strategy (P11/Pillar C) | 🎯 Стол стратегии | 🗺 **Планировочный стол + Свод правил** — Strategic Direction + Principles |

---

## §3 Output Specification — что должно быть в новом overview

### 3.1 Файл и расположение
- **Path:** `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md`
- **Frontmatter:**
  ```yaml
  ---
  title: Foundation Master Overview — Human-readable через метафору Мастерской
  type: synthesis
  status: F4 draft (awaiting Ruslan ack)
  version: 1.0-workshop
  created: 2026-05-06
  brigadier_pass: foundation-overview-human-workshop-2026-05-06
  supersedes: swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md
  related_technical_overview: swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
  related_canonical:
    - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
    - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
    - decisions/JETIX-CORPORATION-2026-05-05.md
  foundation_lock_tag: foundation-architecture-locked-2026-04-28
  audience: smart-human-without-engineering-context (founder / partner / investor / future Jetix member / curious reader)
  ---
  ```

### 3.2 Размер
- **Target:** 800-1500 строк (vs 676 старого человеческого / 1590 technical).
- **Не короче 800:** иначе не покрыты все 11 Parts + Pillar C достаточно глубоко.
- **Не длиннее 1500:** иначе становится reference, не narrative (читается за один присест 30-45 мин).

### 3.3 Структура (recommended)

```markdown
# Foundation v1.0 — Мастерская в одном документе

## §0 Что это в одном абзаце
Один абзац (5-7 предложений). После прочтения: понимаешь 70% сути.

## §1 Метафора Мастерской — почему мы говорим «мастерская»
- Что такое мастерская
- Почему именно она (а не дом / завод / лаборатория / монастырь / etc.)
- 7 базовых элементов мастерской (canonical)
- Adaptable станки как главное свойство
- Роль владельца (5 ролей)
- Главный принцип: «всё есть информация»

## §2 Тур по мастерской — 11 Parts + Pillar C
> Каждой Part / Pillar — отдельная подсекция, описывает что эта Part делает в workshop frame.
> Каждая подсекция: метафора (что это в мастерской) + Что делает + Что хранит/обрабатывает + С кем связана.

### §2.1 🏭 Фундамент мастерской — Part 1 (System State Persistence)
### §2.2 🛡️ Охрана — Part 6a + Part 6b (Provenance Officer + Human Gate)
### §2.3 📋 Приёмная — Part 2 (Signal Ingestion & Triage)
### §2.4 📚 Склад готовых деталей — Part 3 (Knowledge Base & Methodology Library)
### §2.5 👥 Штатное расписание — Part 4 (Role Taxonomy & Coordination Protocol)
### §2.6 🧪 Дневник опыта мастера — Part 5 (Compound Learning & Methodology Capture)
### §2.7 🚧 Большая доска проектов — Part 7 (Project Lifecycle Substrate)
### §2.8 ⚕️ Врач + охранник — Part 8 (Health Monitoring & System Integrity)
### §2.9 💼 Офис владельца — Part 9 (Owner Interaction Scaffold)
### §2.10 📞 Телефонная станция — Part 10 (External Touchpoints & Network Interface)
### §2.11 🎯 Планировочный стол — Part 11 (Strategic Direction Substrate)
### §2.12 📜 Правила дома (на стене) — Pillar C (Principles Substrate)

## §3 Как мастерская работает — потоки информации
> 2-3 потока (input → processing → output) end-to-end через несколько Parts.
> Один пример конкретный: voice note → ingestion → wiki → decision → action.

## §4 3 фазы эволюции мастерской
- Phase 1: одна мастерская одного владельца (текущее состояние)
- Phase 2: команда + одна мастерская
- Phase 3: community мастеров с мастерскими

## §5 Как использовать — для разных ролей
- Если ты founder/owner — что делать
- Если ты исследователь — что изучить
- Если ты потенциальный партнёр — что понять
- Если ты curious reader — за 5 минут общая картина

## §6 Связанные документы
- Technical overview (полная reference)
- Документ 1A (universal foundation)
- Документ 1B (Jetix Corp applied)
- Workshop concept LOCKED (origin)
```

### 3.4 Стилистика
- **Русский язык** (как существующий human overview)
- **Narrative-driven**, не reference-driven
- **Метафорично, образно** — но **не overdone** (метафора служит understanding, не self-purpose)
- **Verbatim quotes Ruslan'а** где они органично ложатся (из Workshop concept §8 и voice-extract)
- **Чем отличается от technical:**
  - Technical: F-G-R citations + verifiable claims + provenance dense
  - Human: narrative + visceral metaphors + smooth flow + minimal citations (только если quote)
- **Цель:** human-readable за 30-45 минут, после прочтения — visceral понимание Foundation v1.0.

### 3.5 НЕ копировать стилистику старого human overview
Старый foundation-master-overview-human-2026-04-29.md — **помечен superseded**. Stylistic patterns которые НЕ переносить:
- Метафоры «дом» / «комнаты» / «подвал»
- Любые формулировки которые противоречат canonical Workshop concept

---

## §4 Process — Phases A через D (brigadier discipline)

### Phase A — Draft (4-6 hours)
**Brigadier responsibility:** read all primary sources (§1.1-§1.7), synthesize в новый overview file.

**Key activities:**
1. Read 1A §2 (Метафора Мастерской) — **главный source** of metaphor formulations
2. Read Workshop concept §1-§10 — verbatim canonical quotes
3. Read each of 11 Parts §0 Mission + Pillar C §0 — extract Purpose
4. Read 1B §2 — для контекста 3 фаз эволюции
5. **Map** каждую Part к workshop frame через canonical mapping (§2.8 этого prompt)
6. Write narrative-style §0-§6 в Output Spec (§3.3)

**Output Phase A:** `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` v0.1 draft.

### Phase B — Critic review (2-3 hours)
**Brigadier dispatches critic role:**

**Critic checks:**
1. ✅ Все 11 Parts + Pillar C покрыты?
2. ✅ Метафора consistent (нет ли утечек «дом» формулировок)?
3. ✅ Соответствует canonical Workshop concept (Документ 1A §2 + WORKSHOP-CONCEPT)?
4. ✅ 7 базовых элементов мастерской упомянуты явно?
5. ✅ 3 фазы эволюции описаны?
6. ✅ Pillar C как cross-cutting sub-system, НЕ как Part?
7. ✅ Размер 800-1500 строк?
8. ✅ Audience-appropriate (smart-human-without-engineering)?
9. ✅ Verbatim quotes используются органично (не overdone)?
10. ✅ Cross-references на canonical sources корректны?

**Если ❌ — return to Phase A iteration.**

**Output Phase B:** v0.2 draft + critic findings memo `swarm/wiki/cycles/cyc-foundation-overview-human-workshop-2026-05-06/critic-findings.md`.

### Phase C — AWAITING-APPROVAL packet (30-60 min)
**Brigadier создаёт ack packet:**

**File:** `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md`

**Содержит:**
- Summary что было сделано (rewrite human overview через workshop metaphor)
- Diff vs old: старая «дом» metaphor → новая «workshop»
- Coverage check (все 11 Parts + Pillar C — да/нет)
- Quality assessment (critic findings resolved или нет)
- Risk assessment (constitutional violations / discipline gaps)
- Action requested: Ruslan ack для:
  - Promote v0.2 → v1.0 LOCKED
  - Mark old `foundation-master-overview-human-2026-04-29.md` as `superseded_by:`
  - Update `swarm/wiki/index.md` + `swarm/wiki/log.md`
  - Update CLAUDE.md `## Foundation Architecture v1.0 (LOCKED)` секцию (если в Variant D consensus был добавить cross-link)

### Phase D — LOCK + Ship (15 min after Ruslan ack)
**Action sequence:**
1. Update frontmatter: `status: LOCKED v1.0`
2. Old human overview frontmatter: добавить `superseded_by: <new path>`
3. Update `swarm/wiki/index.md` — добавить новый, пометить старый
4. Update `swarm/wiki/log.md` (append-only)
5. Git commit: `[foundation] human overview rewrite через workshop metaphor — LOCKED v1.0`
6. Git tag: `foundation-overview-human-workshop-locked-2026-05-XX` (date Ruslan ack)
7. Git push origin HEAD:main + push tag

---

## §5 Constitutional discipline (Pillar C compliance)

### Tier 2 Rules применимые
- **Rule 2:** AI does NOT execute architectural changes without gate. Этот rewrite касается Foundation-level synthesis → **обязателен Human Gate (Phase C ack)**.
- **Rule 4:** AI does NOT claim personal identity (только `acting_as` role). Brigadier prompt — это `acting_as` orchestration role.
- **Rule 6:** AI does NOT aggregate unstructured long-term memory. Все aggregations должны иметь explicit provenance.
- **Rule 11:** No actions without blast-radius classification + Default-Deny.

### Blast radius classification
- **Этого rewrite:** STRUCTURAL F8 (новый canonical synthesis document, replaces existing).
- **Approval level required:** Ruslan explicit ack (через AWAITING-APPROVAL packet, Phase C).

### Append-only discipline
**НЕ удалять** старый `foundation-master-overview-human-2026-04-29.md`. Mark `superseded_by:` — **history preserved**.

### Provenance requirements
- Каждый ключевой claim в новом overview должен быть **traceable** к canonical source (1A / 1B / Workshop concept / 11 Parts / etc.)
- Citations не обязательно inline (это human overview, не technical), но **frontmatter должен указать all sources used**
- Если что-то добавлено creative beyond canonical — **flag** в Phase C critic findings

---

## §6 Success Criteria (Phase D ship)

После ship — выполнены ВСЕ:

- ✅ Файл `foundation-master-overview-human-workshop-2026-05-06.md` существует, ~800-1500 строк
- ✅ Все 11 Parts + Pillar C описаны через workshop frame
- ✅ Метафора consistent throughout (zero «дом» references)
- ✅ Soответствует canonical Workshop concept LOCKED 30.04
- ✅ Соответствует Документу 1A §2 (Метафора Мастерской) и §4 (11 Parts архитектура)
- ✅ Соответствует Документу 1B §2 (3 фазы эволюции)
- ✅ Old human overview помечен `superseded_by:`
- ✅ Index + Log updated
- ✅ Ruslan ack received (через Phase C AWAITING-APPROVAL packet)
- ✅ Git tag pushed
- ✅ Commit on main

---

## §7 Estimated Effort

- Phase A (Draft): 4-6 hours
- Phase B (Critic): 2-3 hours
- Phase C (Ack packet): 30-60 min
- Phase D (Ship): 15 min after ack
- **Total brigadier time:** 7-10 hours
- **Total Ruslan time:** ~30-60 min (read + review + ack)
- **Wall-clock realistic:** 1-2 days если Ruslan available; 2-4 days if async

---

## §8 ВАЖНО — что НЕ делаем в этом цикле

> *Чтобы scope не разъехался.*

- ❌ **НЕ переписываем technical overview** — он остаётся как есть (ПОЛНОСТЬЮ).
- ❌ **НЕ создаём one-pager <300 строк** — это отдельный future task (Variant D step 3 из consolidation report).
- ❌ **НЕ обновляем CLAUDE.md cross-link** — это отдельный mini-task с own ack packet.
- ❌ **НЕ touchаем 11 Parts architecture.md files** — они LOCKED, immutable через append-only.
- ❌ **НЕ обновляем Wave 1 Strategic Layer scaffolding** — это deferred work, не часть этого цикла.

---

## §9 Запуск

```bash
# Команда запустить server CC без permissions
cd ~/jetix-os && git pull origin main && claude --dangerously-skip-permissions
```

Затем в чате CC:

> Прочитай и выполни автономно файл `prompts/foundation-overview-human-workshop-rewrite-brigadier-2026-05-06.md`. Это brigadier prompt для rewrite Foundation Master Overview Human через метафору Мастерской. Все sources / output spec / process / discipline — внутри файла. Поехали.

---

**Estimated total wall-clock for ship:** 1-2 days.

**Next deliverable:** `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` LOCKED v1.0.
