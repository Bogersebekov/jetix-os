---
id: voice-memos-step-4-year-plan
title: Step 4 — Year Plan Extraction из ~117 Voice-Memos
date: 2026-04-21
type: prompt
status: ready
depends_on: Step 1 (transcripts ready)
parallel_with: Step 3 (mini-wiki), Step 5 (strategic ideas)
---

# Step 4 — Year Plan Extraction из ~117 Voice-Memos

## Контекст

Voice-memos Ruslan'а содержат плотный слой actionable задач / TODOs / проектов / дедлайнов которые Ruslan надиктовывал по ходу размышлений. Этот слой часто теряется потому что он перемешан со стратегией / философией / случайными размышлениями.

Нужно вытащить именно **actionable year plan layer** — что делать, когда, по каким проектам.

**Это вход для Genesis Document (sequencing + priority directions sections).**

Notion page: https://www.notion.so/3492496333bf813fbbbec5deabcc61a4

## Критическое правило

**Извлечение ПРЯМО ИЗ RAW TRANSCRIPTS**, не из review report и не из mini-wiki. Extracted items можно использовать как дополнительный сигнал, но primary source = .txt транскрипты.

**НЕ читать VOICE-MEMOS-MINI-WIKIPEDIA.md** — этот шаг должен быть independent от Шага 3 чтобы не заражаться его категориями / агрегациями.

## Задача

Извлечь полный year plan из всех ~117 transcripts:
- Actionable TODOs
- Упомянутые проекты
- Дедлайны / временные рамки
- Priority hints
- Последовательность / dependencies
- Resource requirements (время / деньги / люди)

## Input

- `raw/transcripts/*.txt` — ~117 файлов (primary)
- `raw/voice-memos/` — для mtime sorting
- Existing project structures (для context):
  - `alphas/` если есть
  - `directions/` если есть
  - Notion Projects DB ID: `69a3c581-ab33-48d9-9827-ec8a8bb69d14` (reference, можно не fetchить если долго)
  - CLAUDE.md секция "Проекты (8 активных)"

## Алгоритм

### Фаза 1 — Inventory + chunking

1. Список всех transcripts с датами из filename
2. Разбить на chunks по 12-20 transcripts chronologically
3. Подсчитать базовую статистику

### Фаза 2 — Extraction через subagents (parallel batches)

Для каждого chunk — spawn subagent через Task tool:

```
Task: Извлечь year-plan layer из batch transcripts.

Input: [transcript paths]

Для каждого transcript субагент должен найти:

1. TODOS — конкретные actionable tasks:
   - Глагол действия (написать / сделать / запустить / связаться / ...)
   - Object (что именно)
   - Context (почему / в рамках чего)
   - Deadline если упомянут
   - Project mention если упомянут
   - Quote из транскрипта
   
   Example: {
     "action": "написать",
     "object": "Genesis Document часть A (philosophy)",
     "context": "для 6 architect agents",
     "deadline": null,
     "project": "architecture-v3",
     "priority_hint": "P1 (critical)",
     "quote": "...",
     "transcript": "audio_XXX.txt"
   }

2. PROJECT MENTIONS — любые упоминания проектов (existing 8 в CLAUDE.md или новые):
   - Project name
   - What Ruslan said about it (status / next step / concern)
   - Quote

3. DEADLINES / TIMEFRAMES — явные даты / периоды:
   - "к концу месяца" / "через 2 недели" / "Q2" / "30.06.2026"
   - Контекст — deadline для чего

4. PRIORITY SIGNALS — где Ruslan явно маркировал:
   - "срочно" / "важно" / "прям критично" / "можно отложить"

5. DEPENDENCIES — что от чего зависит:
   - "X должно быть готово прежде чем Y"
   - "без Z не стартуем W"

6. RESOURCE MENTIONS:
   - Время (X часов / дней)
   - Деньги (€X)
   - Люди (кого-то нанять / помочь)

Output: JSONL со структурированными TODOs.
```

### Фаза 3 — Aggregation + dedup

После всех subagent runs:

1. **Dedup similar TODOs** — если один и тот же TODO упомянут в 3 транскриптах подряд, merge в один TODO с recurring signal
2. **Categorize by project:**
   - 8 existing projects из CLAUDE.md: quick-money / research / brand / community / ai-tools / life-os / engineering-thinking / bets
   - Новые проекты если Ruslan ввёл
   - Uncategorized (если не ясно)
3. **Timeline construction:**
   - Grouping по timeframe (now / Phase 1 Q2 / Phase 2 / long-term)
4. **Priority ranking:**
   - P1 (explicit "critical" / "important" signals)
   - P2 (implicit priority)
   - P3 (nice-to-have)
5. **Dependencies graph:**
   - X blocks Y
   - Y requires Z

### Фаза 4 — Output document

Создать `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md`:

```markdown
---
id: voice-memos-year-plan
title: Year Plan из ~117 Voice-Memos (extracted)
date: 2026-04-21
type: plan-extraction
status: ready
sources:
  - raw/transcripts/ (~117 файлов)
purpose: |
  Actionable year-plan extracted напрямую из voice-memos.
  Input для Genesis Document (sequencing + priority directions).
---

# Year Plan из ~117 Voice-Memos

## 1. Meta-Stats
- Total TODOs extracted: N
- After dedup: N unique
- With explicit deadline: N
- With project assignment: N (breakdown по проектам)

## 2. TODOs по проектам

### 2.1 quick-money (P1)
| # | Action | Deadline | Priority | Quote / Source |
|---|--------|----------|----------|----------------|
| 1 | ...    | 2026-06-30 | P1 | "..." [src:audio_XXX] |
...

### 2.2 research (P2)
...

### 2.3 brand (P2)
...

### 2.4 community (P3)
...

### 2.5 ai-tools (P2)
...

### 2.6 life-os (P3)
...

### 2.7 engineering-thinking (P3)
...

### 2.8 bets (P4 paused)
...

### 2.9 NEW projects (если Ruslan ввёл)
...

### 2.10 Uncategorized
(TODOs без clear project assignment — нужно classification manually)

## 3. Timeline View

### 3.1 NOW / эта неделя (2026-04-21 ... 2026-04-27)
- TODO list

### 3.2 Phase 1 Q2 push (→ 2026-06-30, €50K target)
- TODO list grouped by project

### 3.3 Phase 2 (post €50K → €200K gate)
- TODO list

### 3.4 Long-term
- TODO list

## 4. Priority Distribution
- P1 (critical): N TODOs
- P2 (important): N TODOs
- P3 (nice-to-have): N TODOs
- P4 (paused/future): N TODOs

## 5. Dependencies Graph

```
blockers:
- X blocks Y
- ...
```

## 6. Resource Budget Extractions

### 6.1 Time
- Total estimated hours (если extract возможен): N
- By project

### 6.2 Money
- Упомянутые бюджеты / инвестиции

### 6.3 People
- Кого нужно нанять / привлечь
- Кого упомянул как партнёра / helper

## 7. Conflicts / Tensions в plan

Где TODOs конфликтуют друг с другом:
- "сделать X быстро" vs "сделать X глубоко"
- Resource overallocation
- Timeline conflicts

## 8. Surprises

Что в plan оказалось неожиданным:
- TODO которые Ruslan упомянул много раз но до сих пор не сделал
- Проекты про которые Ruslan говорит в voice-memos но которых нет в CLAUDE.md "Проекты"
- Дедлайны которые уже прошли

## 9. Provenance Index
(compact table: TODO → transcript source)
```

### Фаза 5 — Commit

```bash
git add raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md
git commit -m "[research] Year plan extraction из ~117 voice-memos"
git push origin claude/jolly-margulis-915d34
```

## Ограничения

- **Primary source = .txt transcripts**, не review report.
- **НЕ inventить TODOs** — только те которые реально сказаны.
- **НЕ генерировать TODOs на основе анализа темы** — только те которые сформулированы глаголом действия в речи.
- **Quote attribution обязательна** для каждого TODO.
- **Conservative dedup** — если not sure что это тот же TODO, сохрани оба.
- **ETA:** 2-3 часа.

## Deliverable (stdout summary)

```
# Year Plan Extraction Complete

- File: raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md
- Size: X lines / Y KB
- Transcripts analyzed: N
- TODOs extracted raw: N
- After dedup: N unique
- P1 / P2 / P3 / P4 breakdown
- Deadlines with dates: N
- New projects mentioned (not in CLAUDE.md): N
- Conflicts detected: N
- Commit hash: abc1234
```
