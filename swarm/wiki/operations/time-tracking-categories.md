---
title: Time Tracking Categories — понятийный аппарат
status: living
created: 2026-05-02
last_updated: 2026-05-02
type: operational_canon
authored_via: AI scribe (verbatim Ruslan dictation)
applies_to:
  - Toggl Track (manual entries)
  - ActivityWatch (auto tracking, computer-only subset)
  - Daily Log Notion (EOD reflection)
phase_1_scope: solo founder, no business yet, no team, no client comms
phase_2_extension: business + team layers (deferred)
---

# Time Tracking Categories — путеводитель

## §0 Цель документа

**Что это:** единый **понятийный аппарат** для time tracking в Jetix OS. Один источник истины — что значит каждая категория, что туда входит / что НЕ входит, как засекать в Toggl и ActivityWatch.

**Зачем:**
- Чтобы каждый раз не путаться («это работа или ебланил?»)
- Чтобы у меня + AI + future agents было одинаковое понимание
- Чтобы tracking pipeline (AW auto + Toggl manual + voice→CC entries) использовали одну схему
- Чтобы report'ы были **сравнимы между собой** — week-to-week, month-to-month
- Чтобы потом легко расширить под бизнес/команду/клиентов

**Принцип living document:** этот файл **evolve'ится**. Если категория слишком широкая / слишком узкая — refine. Если появляется новый класс деятельности (например бизнес, клиенты) — добавляем. Версионируется через git history.

**Как пользоваться:**
- Перед записью в Toggl / при review дня — сверяться с этим документом
- При сомнении («куда отнести?») — читать §3 Boundary cases
- При значимом изменении — update этот файл + log entry в `wiki/log.md` + commit

---

## §1 Top-level направления (8 штук)

Минимальный универсальный набор для Phase 1 (solo founder, no clients, no team):

| # | Направление | Тип | Tracker |
|---|-------------|-----|---------|
| 1 | **Сон** | биологический | Toggl |
| 2 | **Зарядка** | утренний ритуал | Toggl |
| 3 | **Спорт** | физический | Toggl |
| 4 | **Рутина** | бытовое | Toggl |
| 5 | **Deep Work** | продуктивная работа | Toggl + AW |
| 6 | **Гулял** | физическое+социальное движение | Toggl |
| 7 | **Отдых** | intentional восстановление | Toggl + (AW если на компе) |
| 8 | **Ебланил** | бесцельный тупеж | Toggl + AW |

**Всё что в день должно попасть в одну из этих 8.** Если что-то не попадает — это **сигнал** что нужна новая категория или refinement (записать в §6 «открытые вопросы»).

**Phase 2 расширения (отложено, см. §7):**
- **Бизнес** — sales calls, client work, partnership meetings
- **Команда** — менеджмент, 1-on-1s, code review
- **Клиенты** — consulting hours, deliverables

---

## §2 Каждое направление подробно

### §2.1 Сон

**Что это:** время реального сна (от закрытия глаз до пробуждения). Включает «не мог уснуть» как отдельный sub-state.

**Что входит:**
- Полный ночной сон
- Дневной сон / siesta
- «Не мог уснуть» — лёг, но крутился, не спал

**Что НЕ входит:**
- Лежание в кровати с телефоном перед сном (это **Ебланил**)
- Утреннее «ещё 5 минут полежу» с телефоном (Ебланил)
- Подготовка ко сну (это **Рутина**)

**Toggl:**
- Project: `Сон`
- Tags: `глубокий` / `прерывистый` / `не мог уснуть` (опционально)
- Description: free-text если что-то значимое («плохой сон из-за стресса», «yvarse в 3 утра»)

**ActivityWatch:** не применимо (computer выключен).

**Важно:** записывать каждый день, даже если коротко. Это baseline для всего остального.

---

### §2.2 Зарядка

**Что это:** утренний ритуал после пробуждения. **~20 минут.** Тело + день подготовка.

**Что входит:**
- Утренние физические упражнения (растяжка / упражнения / yoga)
- Утренние «задачи на заряд дня» — чай / медитация / set intentions / читать одну страницу

**Что НЕ входит:**
- Душ / умывание (Рутина)
- Завтрак (Рутина)
- Полная тренировка ≥45 мин (Спорт)
- Прогулка (Гулял)

**Toggl:**
- Project: `Зарядка`
- Tags: `тело` / `день-prep` (опционально)
- Description: что делал («15 мин растяжка + чай + 5 мин планирование»)

**ActivityWatch:** не применимо (offline ritual).

---

### §2.3 Спорт

**Что это:** **intentional physical training**. Не walking, не зарядка.

**Что входит:**
- Спортзал
- Бег / интервальные
- Полная тренировка дома ≥45 мин
- Велосипед как тренировка (не дорога в магазин)
- Боевые / йога как class

**Что НЕ входит:**
- Утренняя зарядка (Зарядка)
- Гуляние (Гулял)
- Walking как способ перемещения (Рутина / часть другого направления)

**Toggl:**
- Project: `Спорт`
- Tags: тип (`бег` / `зал` / `йога` / `cardio` / `домашка`)
- Description: что делал, intensity если хочется

**ActivityWatch:** не применимо.

---

### §2.4 Рутина

**Что это:** **бытовое необходимое для жизни**, не двигающее проекты вперёд. Зонтик-категория с sub-themes.

**Что входит:**
- Еда (готовка / магазин / готовая еда / ресторан)
- Магазин (продукты / non-food)
- Уборка дома
- Стирка
- Доктор (зубной / обычный / любой медицинский)
- Hygiene routines (душ / самочувствие)
- Коммунальные дела (банк, документы, бюрократия)
- «Прочая поебота» — anything mandatory but не deep work

**Что НЕ входит:**
- Сон (Сон)
- Зарядка (Зарядка)
- Прогулка ради прогулки (Гулял)
- Спорт (Спорт)
- Eating while working (это часть Deep Work / другой деятельности)

**Toggl:**
- Project: `Рутина`
- Tags (для sub-themes): `еда` / `магазин` / `уборка` / `доктор` / `документы` / `другое`
- Description: что именно («магаз+еда» / «уборка кухни 30мин» / «зубной»)

**ActivityWatch:** не применимо в основном (offline). Если документы / банк через computer — может попасть в AW под uncategorized → manual cleanup в Toggl.

**Multi-task allowed:** «магаз+еда» как один Toggl entry с двумя tags — нормально.

---

### §2.5 Deep Work ⭐ (расширение из «New info or thinking»)

**Что это:** **продуктивная мыслительная / творческая работа** двигающая проекты / систему вперёд. Здесь раньше всё попадало под «New info or thinking», теперь разбито на 6 sub-directions.

**Что входит (любая из 6 sub-directions):**

#### DW.RES — Research / получение новой информации
- Чтение книг / статей / docs по теме
- Изучение видео / курсов
- Интервью с экспертом ради information gathering
- Исследование рынка / конкурентов

#### DW.OBR — Обработка / синтез / поток инсайтов
- Размышление над проблемой
- Синтез существующих знаний в новый view
- «Поток инсайтов», философские размышления, систематизация
- Critical reading (когда не просто читаешь а переваривайshь)
- Mapping concepts, drawing connections

#### DW.SOZD — Создание / производство
- Написание документов / синтезов
- Создание презентаций / видео
- Coding / building
- Email / message draft (важных, не chat'tov)
- Schemas / diagrams creation

#### DW.UCH — Учёба
- Structured learning (course / textbook chapter / tutorial)
- Deliberate practice (skill drills)
- Note-taking от полезного источника

#### DW.PODG — Подготовка
- Подготовка к важному событию (видео / звонок / встреча)
- Сбор материалов для следующего шага
- Pre-call research, agenda preparation

#### DW.KOM — Коммуникация (work-related, deep)
*Пока не активна (нет бизнеса / команды). Будущее direction.*
- Meaningful work conversations (mentor, partner, collaborator)
- Async deep correspondence (важные emails / review comments)
- НЕ пустые сообщения / chit-chat (это Ебланил)

**Что НЕ входит:**
- YouTube ради entertainment (Ебланил)
- Социальные сети (Ебланил / Социальные)
- Просто чтение новостей (Ебланил если без цели)
- Mindless scrolling docs (Ебланил)

**Toggl:**
- Project: `Deep Work`
- Tags (для sub-direction): `RES` / `OBR` / `SOZD` / `UCH` / `PODG` / `KOM`
- Tags (для project context): `Jetix` / `Tseren` / `TRM` / `Workshop` / etc. (project / theme)
- Description: что именно делал — verbatim («разбор гипотез malware partnership через призму бизнеса, поток инсайтов»)

**ActivityWatch (AW Categories):**
- Mapping: AW «Deep work» category → Antigravity / Cursor / Code / Notion / Miro / Terminal / Obsidian
- AW «Research» category → GitHub / docs / Anthropic / Wikipedia / academic — может быть **subset DW.RES**
- AW не различает DW sub-directions (она видит только app+URL). **Toggl остаётся source of truth для sub-direction.** AW — поддерживает overall «deep work time» metric.

**Многозадачность:** часто DW работа — это смесь sub-directions (RES → OBR → SOZD за один час). В Toggl ставить **dominant** sub-direction + другие как secondary tags. Description описывает все.

---

### §2.6 Гулял

**Что это:** **физическое движение outdoor** + потенциально социальное (с кем-то / один). Не спорт, не routine errand.

**Что входит:**
- Прогулка одному (медитативная)
- «Гулял с бро по Берлину»
- Walking park / nature
- Длинная прогулка после еды

**Что НЕ входит:**
- Walking в магазин (Рутина)
- Walking как тренировка fast pace (Спорт)
- Утренняя короткая прогулка как ritual (Зарядка если ~20мин)

**Toggl:**
- Project: `Гулял`
- Tags: `один` / `с кем-то` (опционально)
- Description: с кем / куда («с бро по центру», «один Tiergarten»)

**ActivityWatch:** не применимо.

---

### §2.7 Отдых

**Что это:** **intentional restoration**. Сознательно отдыхаешь чтобы восстановиться. **Не тупеж.**

**Что входит:**
- Лежание с пустой головой (intentional)
- Медитация
- Ванна
- Listen music осознанно
- Nice book (художка)
- Серьёзный фильм (не фоновый сериальчик-тупеж)
- Conscious break перед next task
- Quality time с близким человеком (intentional, не ради чего-то)

**Что НЕ входит:**
- YouTube без цели (Ебланил)
- Скроллинг социалок (Ебланил)
- «Лёг отдохнуть и взял телефон» — теперь это Ебланил

**Boundary case с Ебланил (§3):** часто пересекается. Critical question: **«я выбрал это сейчас и оно меня восстанавливает?»** YES → Отдых. NO / автопилот → Ебланил.

**Toggl:**
- Project: `Отдых`
- Tags: `активный` (book / fiлм с фокусом) / `пассивный` (lying / медитация)
- Description: что именно

**ActivityWatch:**
- Если на компе (фильм через VLC, art browsing) — попадёт в AW. Опциональная категория «Rest» в AW можно создать.
- Если оффлайн — нет AW data.

---

### §2.8 Ебланил ⚠️

**Что это:** **бесцельный тупеж / ерунда / time без прогресса.** Нужно честно фиксировать.

**Definition:** «занимался чем-то без какой-то конкретной цели, и это **не дало прогресса в ключевых проектах**, и это не intentional restoration».

**Что входит:**
- YouTube ради того чтобы YouTube
- Социалки scrolling (Twitter / Instagram / Reddit)
- Сериальчик-тупеж (не фокусированный фильм-Отдых)
- Долгие пустые разговоры на непонятные темы
- «Втык в телефон» / «втыкал в сериальчик»
- «Хотел ебаться, втыкал в телефон»
- «Просто ждал пока обработается» — если в это время бесцельно листал
- «Тупеж» в любых формах
- «В молоке, надулся» states — если не intentional rest

**Что НЕ входит:**
- Intentional rest with focus (Отдых)
- Necessary household task (Рутина)
- Deep work even if frustrating (Deep Work)

**Honest test:** **«Это меня продвинуло хоть где-то? Или это intentional restoration? Или это просто тупо время прошло?»** Если последнее — Ебланил.

**Toggl:**
- Project: `Ебланил`
- Tags: `соцсети` / `youtube` / `втык в телефон` / `пустые разговоры` / `тупеж` / `другое`
- Description: что именно («YouTube random 2ч», «втыкал в Telegram»)

**ActivityWatch:**
- Mapping: AW «Off-topic» → YouTube / Netflix / Twitch / Spotify (when not background work)
- Mapping: AW «Social» → Twitter / Instagram / Facebook / TikTok / Reddit
- AW даст metric «время в off-topic apps», но не различает Отдых vs Ебланил **— Ruslan честно классифицирует в Toggl**.

**Зачем фиксировать:** чтобы видеть **honest** baseline. Если ебланил много — сигнал к коррекции (energy / boredom / avoidance pattern). Не для самоnasilия.

---

## §3 Boundary cases (где путаюсь)

### Boundary 1: Отдых vs Ебланил
**Distinguishing question:** «Я выбрал это сознательно для восстановления?»
- Yes + восстанавливает → **Отдых**
- No / автопилот / просто тупо время прошло → **Ебланил**
- Mixed («сначала отдых, потом залип») → split в Toggl на 2 entries

### Boundary 2: Гулял vs Рутина (walk to магазин)
- Walking to/from магазин когда основная цель — купить → **Рутина** (с tag `магазин`)
- Walking чтобы прогуляться, по пути зашёл в магазин → **Гулял**

### Boundary 3: Зарядка vs Спорт
- ~20 мин morning ritual → **Зарядка**
- ≥45 мин intentional training → **Спорт**

### Boundary 4: Рутина vs Deep Work (документы / банк)
- Routine paperwork (taxes, bills) → **Рутина** (tag `документы`)
- Strategic doc work (Jetix tax planning) → **Deep Work** DW.SOZD

### Boundary 5: Deep Work + еда одновременно
- Если ел обед пока работал — **Deep Work** (продолжение). Eating является background.
- Если break ради еды + не работаешь → **Рутина** (`еда`)

### Boundary 6: Поток инсайтов vs Ебланил
- Productive thinking, mind on важной теме → **Deep Work** DW.OBR
- Mind drifting, no тема → **Ебланил** (или **Отдых** if intentional)

### Boundary 7: Звонки / разговоры
- Work meaningful (mentor / partner / business) → **Deep Work** DW.KOM (когда активно)
- Family / close friend (важное отношение) → **Отдых** (quality time)
- Random chat / пустые разговоры → **Ебланил**

---

## §4 Deep Work — как улучшить и развить дальше

**Phase 1 baseline (сейчас):** 6 sub-directions (RES / OBR / SOZD / UCH / PODG / KOM).

**Предложения для evolution:**

### 4.1 Energy state tag
Добавить tag отражающий **energy / focus state**:
- `flow` — был в потоке (rare, valuable)
- `шёл` — обычный workflow
- `тяжело` — продирался
- `туман` — не фокусировал, ушёл в Ебланил/Отдых

Это даст **2D view:** что × как. Можно увидеть что DW.SOZD редко в `flow` → причина refactor подхода.

### 4.2 Project / theme tag (важно)
Каждый DW entry должен иметь **project tag**:
- `Jetix-foundation` / `Jetix-workshop` / `Jetix-TRM` / `Jetix-pipeline` / `Tseren` / `Mittelstand` / etc.

Когда придёт бизнес — projects расширятся (`client-X` / `partnership-Y`).

### 4.3 Output tag (опционально)
Что произвёл за этот DW slot:
- `доc` (документ создан / updated)
- `решение` (decision made)
- `understand` (gained understanding without artifact)
- `gap` (закрыл gap в понимании)
- `nothing` (потерял время в DW labels)

Поможет видеть **DW with output vs DW without** — если много `nothing`, сигнал к approach review.

### 4.4 Future: BIKE method phase tag (per Nate Herk course)
- `phase-1-training-wheels` (manual, watching mistakes)
- `phase-2-guided` (automation drafts, я review)
- `phase-3-watched` (autonomous + alerts)
- `phase-4-handsoff`

Поможет видеть progression of automation maturity.

### 4.5 Будущее: «cognitive load» tag
- `low` (typing established knowledge)
- `medium` (новая комбинация)
- `high` (synthesize across domains)

Поможет energy budgeting — высокая cognitive load работа должна быть в peak energy hours.

**Sequence для evolution:** сначала освоить базовые 6 sub-directions хорошо в течение 2-4 недель. Потом добавлять tag по одному (energy → output → BIKE phase) — не всё сразу.

---

## §5 Mapping в trackers

### §5.1 Toggl structure

**Projects (8 шт):**
1. Сон
2. Зарядка
3. Спорт
4. Рутина
5. Deep Work
6. Гулял
7. Отдых
8. Ебланил

**Цвета (suggestion):**
- 🌙 Сон — dark blue
- ⚡ Зарядка — yellow
- 💪 Спорт — purple
- 🛒 Рутина — light blue
- 🧠 Deep Work — green
- 🚶 Гулял — orange
- 😌 Отдых — grey
- ⚠️ Ебланил — red / brown

**Tags (universal набор):**

*Sub-direction tags для Deep Work:*
- `RES` (Research)
- `OBR` (Обработка)
- `SOZD` (Создание)
- `UCH` (Учёба)
- `PODG` (Подготовка)
- `KOM` (Коммуникация — пока не активно)

*Theme / project tags:*
- `Jetix` (umbrella)
- `Jetix-foundation` / `Jetix-workshop` / `Jetix-TRM` / `Jetix-pipeline` / `Jetix-malware-analysis` / `Jetix-time-tracking`
- `Tseren` (specific outreach project)
- *(будущее: `client-X` / `partnership-Y`)*

*Sub-tags для Рутина:*
- `еда` / `магазин` / `уборка` / `доктор` / `документы` / `другое`

*Sub-tags для Ебланил:*
- `соцсети` / `youtube` / `втык-в-телефон` / `пустые-разговоры` / `тупеж` / `другое`

*Sub-tags для Сон:*
- `глубокий` / `прерывистый` / `не-мог-уснуть`

*Sub-tags для Спорт:*
- `бег` / `зал` / `йога` / `cardio` / `домашка`

*Sub-tags для Отдых:*
- `активный` / `пассивный`

**Description (свободный):** verbatim что делал. Можно русский / мат / specifics.

### §5.2 ActivityWatch categories (regex rules)

ActivityWatch видит только computer activity. Mapping = subset.

**Категории и regex (web UI [http://localhost:5600/#/settings](http://localhost:5600/#/settings)):**

| Категория | Regex (apps + URLs) | Mapping → Toggl |
|-----------|---------------------|-----------------|
| **Deep Work** | `claude\|antigravity\|cursor\|code\.exe\|notion\|miro\|terminal\|powershell\|git bash\|mingw\|obsidian` | Deep Work (любой sub-direction) |
| **Research** | `github\.com\|stackoverflow\|anthropic\.com\|docs\.\|wikipedia\|developer\.\|arxiv` | Deep Work — DW.RES (часто) |
| **Communication** | `telegram\|discord\|slack\|outlook\|gmail\|whatsapp\|mail\.google` | Deep Work DW.KOM (work) ИЛИ Ебланил (chat random) — manual classification в Toggl |
| **Off-topic** | `youtube\.com\|netflix\|spotify\|twitch\|tiktok\|instagram` | Ебланил ИЛИ Отдых (manual) |
| **Social** | `twitter\.com\|x\.com\|facebook\|reddit\.com` | Ебланил (almost always) |
| **AFK** | (auto-detected by aw-watcher-afk) | Сон / Зарядка / Спорт / Рутина / Гулял / Отдых (offline) |

**Важное правило:** AW даёт **objective baseline** (computer time). Toggl даёт **subjective intent** (что я считал deep work vs ebлан). Reports compare both — расхождение = useful insight.

### §5.3 Daily Log Notion structure

В EOD section Daily Log entry в Notion:

```markdown
## ⏱️ Time tracking summary

- **Сон:** 7h 30m (хорошо)
- **Зарядка:** 0m ⚠️ (пропустил)
- **Спорт:** 0m
- **Рутина:** 1h 20m
- **Deep Work:** 5h 40m
  - DW.OBR: 2h 30m (Jetix-malware-analysis)
  - DW.SOZD: 2h 10m (Jetix-time-tracking)
  - DW.RES: 1h (Jetix-workshop reading)
- **Гулял:** 30m
- **Отдых:** 1h
- **Ебланил:** 1h 40m (втык в телефон + youtube)

## 📊 ActivityWatch
- Total active: 6h 20m
- Top apps: Antigravity (3h), Chrome (1h 30m), Telegram (40m)
- AFK: 2h 25m (аligned с Гулял + Отдых + Рутина)

## 🤔 Reflection
*(free text — что заметил сегодня, что менять)*
```

---

## §6 Открытые вопросы / refine этот документ

(Заполняется по мере использования. Если что-то не fit'ит в 8 категорий — записать сюда.)

1. *(пример)* «Если я слушаю audiobook пока готовлю еду — это Рутина+DW.RES одновременно?» → решение: dominant Рутина + tag `+audiobook` в description.

---

## §7 Phase 2 extension (отложено)

Когда придёт **бизнес / команда / клиенты** — добавим следующие top-level направления:

### Phase 2 candidate categories
- **Бизнес** — sales activities, proposals, contracts, pricing decisions
- **Команда** — менеджмент, 1-on-1s, code review, hiring
- **Клиенты** — direct delivery hours per client, retainer time

### Phase 2 changes к existing
- Deep Work DW.KOM активируется (work conversations)
- Project tags расширяются (`client-{name}` / `partnership-{name}`)
- Возможна 9-я категория «Operational management» если много admin

**Триггер для Phase 2 extension:** появление первого retainer client / hiring первого человека в команду / оформление GmbH.

**Не делать сейчас.** Простота важнее.

---

## §8 Workflow использования этого документа

### При записи в Toggl (manual, Path A)
1. Открыть Toggl Track
2. Start timer (или log past entry)
3. Выбрать **Project** (один из 8)
4. Добавить **Tags** (sub-direction если DW + theme + специфика)
5. Description: словами что делал
6. Stop когда finished

### При использовании Wispr Flow + CC (Path B, после Phase 3 implementation)
1. В Wispr Flow надиктовать («работал 9-12 над Workshop concept v2, потом обед, 13:30-15 outreach Tseren»)
2. Paste text в Cloud Cowork chat (или server CC)
3. CC parses by **этому документу** + создаёт Toggl entries + updates Daily Log
4. Confirm в чате

### При сомнении («куда отнести?»)
1. Читать §3 Boundary cases
2. Если не покрыто — записать в §6 Открытые вопросы + классифицировать на ощупь
3. Update document при значимом insight

### При EOD review
1. Открыть Toggl daily summary
2. Compare с ActivityWatch report (`reports/activity_YYYY-MM-DD.md`)
3. Записать summary в Daily Log Notion (§5.3 format)
4. Reflect: что пошло good / что bad / что менять завтра

---

## §9 Связь с canonical Jetix concepts

- **TRM model** (`decisions/JETIX-TRM-MODEL-2026-04-30.md`) — TRM управляет «временем CEO» как 1 из 6 ресурсов. Этот document = operationalization того ресурса для self-application.
- **Workshop concept** (`decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`) — каждое направление = разная роль мастера / разный «цех» мастерской.
- **Phase 3 vision** (Jetix manages time of clients): когда self-tracking стабилен 4+ недели → этот документ становится **template для clients** (с их кастомизацией).

## §10 Sources / changelog

- **2026-05-02:** initial creation. Verbatim Ruslan dictation. 8 направлений + Deep Work с 6 sub-directions + boundary cases + mapping в Toggl/AW/Daily Log.
- *(future entries here)*
