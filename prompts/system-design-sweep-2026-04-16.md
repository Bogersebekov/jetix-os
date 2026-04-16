---
type: execution-prompt
date: 2026-04-16
phase: step-2-inputs-collection
target: claude-code-server
autonomy: maximum
---

# Sweep & Staging для Шага 2 SYSTEM-DESIGN-HUMAN.md

## Вступление для исполнителя (Claude Code на сервере 100.99.156.28)

Ты — Claude Code. Выполняешь длительную (2-4 часа) автономную задачу по сбору
материала под Шаг 2 строительства Jetix OS. Ruslan не будет сидеть рядом и
подтверждать каждый шаг. Действуй.

### Модель

Предпочтительно **Opus 4.6** или **Sonnet 4.6**. НЕ Haiku. Подписка Max —
токены не экономим.

### Режим работы

- **Autonomous.** Не спрашивай подтверждений. Все действия в рамках локального
  репо + Notion MCP + git — безопасны, Ruslan дал явный карт-бланш.
- **Safelist tools:** Read, Write, Edit, Bash (только внутри `~/jetix-os/`), Grep,
  Glob, Task (для sub-agents), mcp__notion-*, git (через Bash).
- **Запрещено:** WebFetch, WebSearch — вообще. Нам не нужна внешняя инфа, только
  то что уже в Notion/git/локалке.
- **Parallelism encouraged.** Spawn 3-5 sub-agents параллельно через Task tool
  где это имеет смысл. Если 529 → foreground fallback.

### Коммиты

Commit после каждой фазы. Формат: `[inputs] фаза N: <что> (+ N численно)`.
Push в `origin/main` после фаз 3, 6, 9.

### При ошибке

1. `git add -A && git commit -m "[inputs] SAFE-SAVE: stopped in фаза X"`
2. `git push origin main`
3. Запиши состояние в `agents/system-admin/scratchpad.md` (что сделано, где упал, что нужно).
4. Верни короткий error-отчёт в чат.

---

## ЦЕЛЬ

Собрать ВСЮ релевантную информацию о системе управления проектами / философии
работы / Jetix OS из всех источников Notion + wiki → и структурировать её в
одном staging-файле `design/SYSTEM-DESIGN-INPUTS.md`, откуда Ruslan будет
диктовать в `SYSTEM-DESIGN-HUMAN.md`.

**Ты НЕ пишешь SYSTEM-DESIGN-HUMAN.md.** Ты готовишь inputs для него.

---

## ОБЯЗАТЕЛЬНОЕ ЧТЕНИЕ ПЕРЕД СТАРТОМ

1. `SYSTEM-DESIGN-HUMAN.md` — главный целевой документ (279 строк, 6 частей)
2. `ARCHITECTURE-CURRENT.md` — snapshot системы из Шага 1
3. `reports/architecture-inventory-2026-04-16.md` — 3 находки + 3 gap'а
4. `CLAUDE.md` — roster 12 агентов, правила, Notion IDs
5. `MIGRATION.md`
6. `wiki/index.md` + `wiki/log.md`
7. `reports/ideas-import-2026-04-16.md` + `reports/ideas-import-batch2-2026-04-16.md`
8. `.claude/agents/sweep-worker.md` — subagent которого будешь spawn'ить
9. `.claude/agents/staging-writer.md` — subagent для финальной компиляции
10. `.claude/skills/sweep-notion-bank.md` — новый skill
11. Notion: Манифест (`3442496333bf818184a1fbc3108b38cb`),
    Архитектура Memory+KB Karpathy+ (`3442496333bf819cb864cf0e04c9de74`),
    План работ 2026-04-16 (`3442496333bf813b9187c4c7a6eace04`).

После прочтения — **кратко в чат** (5-7 строк): что понял про цель, сколько
ожидаешь идей в Банке, главный output.

---

## КРИТЕРИИ РЕЛЕВАНТНОСТИ (используй во всей работе)

### RELEVANT (помечай `topics: [system-design]`)

Идея касается ХОТЯ БЫ ОДНОГО из:

- Управление проектами, система жизни, система управления временем, Notion-методология
- Ритуалы: morning/evening pipeline, weekly/monthly analysis, retrospectives, reviews
- Pipeline рабочего дня (утро → работа → вечер)
- Daily Log структура, формат страницы дня, типы дней (fokus/recovery/orientation)
- Toggl трекинг, Obsidian vault, dashboard (Command Center)
- Потоки информации: inbox, processed, archive, raw → wiki
- Типы чатов с AI (1 чат = 1 тема), правила работы с AI
- Многоагентные системы: оркестрация, делегирование, hub-and-spoke, департаменты
- Агенты: роли, коммуникация, memory (Core/Working/Archival/Recall), strategies
- System Prompt Learning, накопление опыта агентов
- Memory frameworks: Letta / Mem0 / Zep
- Knowledge base, wiki, Karpathy LLM Wiki, OmegaWiki
- GraphRAG, HippoRAG, vector RAG vs wiki
- Context engineering: Write / Select / Compress / Isolate
- ICP Jetix, бизнес-модель Jetix, видение Jetix
- 5-year / 10-year / 200-year vision, North Star
- Open-source premium, community как продукт, клуб-маркетинг, Revenue Share
- Jetix Corporation (1000 pros, 100K agents)
- Философия работы: engineering faith, think-do feedback loop,
  writing as telepathy, engineering thinking
- Жизненный цикл сущностей: idea → claim → experiment → validated;
  inbox → processed → archive; prospect → lead → customer
- Focus theory (5+AI+1), beast mode, charged vs chill
- Любая информация которая описывает "как ДОЛЖНА работать система Jetix OS"

### IRRELEVANT (не импортировать, оставить в Notion)

Касается ТОЛЬКО:

- Конкретного здоровья/еды/спорта **БЕЗ** привязки к принципу/ритуалу системы
- Личных мемуаров, эмоциональных заметок без системного вывода
- Внешних новостей, пассивных наблюдений
- Конкретного контента без принципа ("прочитал книгу X, понравилось")
- Случайных покупок, планов отдыха без системной связки

### UNCLEAR

Сомнительно — не уверен RELEVANT или IRRELEVANT. В bucket для ручного ревью.
Оптимально UNCLEAR не больше 10-20 % от всего пула.

---

## ФАЗЫ РАБОТЫ

### Фаза 1 — Prep (5-10 мин)

1. `git status` → чисто. Если нет — stop, report.
2. `git pull origin main`.
3. Прочитай обязательное чтение (выше).
4. Проверь что:
   - `.claude/agents/sweep-worker.md` существует
   - `.claude/agents/staging-writer.md` существует
   - `.claude/skills/sweep-notion-bank.md` существует
5. Выведи в чат: "Ready. Понял цель: ... . Ожидаю ~N идей в Банке. Стартую Фазу 2."

### Фаза 2 — Sweep Банка идей (30-60 мин)

Вызови skill `/sweep-notion-bank` (см. `.claude/skills/sweep-notion-bank.md`).

Это выполнит:
- pagination query всего Bank of Ideas
- dedup против wiki/sources/
- spawn 4 параллельных sweep-worker через Task
- dry-run-like классификация, затем import RELEVANT

Ожидаемый результат: ~100-200 RELEVANT новых импортировано,
~300-400 IRRELEVANT помечено, ~30-70 UNCLEAR. Новые ~120+ идей в wiki.

Коммит: `[inputs] фаза 2: sweep Банка идей (N relevant of M)`.
Push.

### Фаза 3 — Ingest Notion-страниц о системе (20-40 мин)

Последовательно (не параллельно — их мало) прогони `/ingest` на каждой из
11 Notion-страниц. Используй `mcp__notion-fetch` → сохрани dump в
`raw/notion-pages/{slug}-2026-04-16.md` → запусти ingest-алгоритм как в
`.claude/skills/ingest.md`, создай source + ideas/concepts/claims по содержимому.

Все — `topics: [system-design]`.

| ID | Slug |
|----|------|
| 3442496333bf818184a1fbc3108b38cb | manifest-system-building |
| 3442496333bf819cb864cf0e04c9de74 | architecture-memory-kb-karpathy |
| 3322496333bf8161b6d3ea789d039356 | command-center |
| 3342496333bf8150a87ece4cfacab815 | pipeline-rabochego-dnia |
| 3342496333bf814a88e1d0699d1d469d | analiz-nedeli |
| 3342496333bf814db239c8bfc55aacb2 | tipy-chatov-ai-rules |
| 3342496333bf81fa9950cbb53bd0e8f5 | potoki-informatsii |
| 33c2496333bf81f3a360e0e90a05265b | format-stranitsy-dnia |
| 3322496333bf8184b31bc985a93222d7 | life-os |
| 32c2496333bf81e8807cd490f9d17872 | research-hub |
| 3372496333bf8125a72cd7352124b5ee | icp-page |

Коммит: `[inputs] фаза 3: ingest 11 Notion-страниц о системе`.
**Push main.**

### Фаза 4 — Daily Log scan (20-40 мин)

1. `mcp__notion-query-database-view` на `collection://30a24963-33bf-8005-817a-000beb10bcd4` — все записи.
2. Для каждой записи выгрузи Reflection, Insights, Deviation, Adjustment, Key Action.
3. Отфильтруй: только строки про систему (не про личные дела без системной связки).
4. Собери в один digest `raw/notion-daily-log-insights-2026-04-16.md` —
   структура:
   ```
   # Daily Log Insights — system-design digest
   
   ## [YYYY-MM-DD] — {Day Type}
   - Key Action: {...}
   - Insight: {...} — [DailyLog YYYY-MM-DD]
   - Reflection: {...}
   
   ## [YYYY-MM-DD] — ...
   ...
   ```
5. Прогони `/ingest raw/notion-daily-log-insights-2026-04-16.md` →
   создастся source card + выделятся ideas/concepts по секциям.

Коммит: `[inputs] фаза 4: Daily Log insights digest (N dates)`.

### Фаза 5 — Теггинг существующих 60 идей (15-30 мин)

1. `ls wiki/ideas/*.md` — 60 файлов.
2. Для каждого: Read frontmatter + first 20 lines body. Классифицируй
   (RELEVANT / IRRELEVANT / UNCLEAR) по критериям.
3. Для RELEVANT — Edit frontmatter: добавь или расширь `topics:` массив значением
   `system-design`. Ничего больше не меняй.
4. Параллельно можешь spawn'ить 2-3 Task для блоков по 20 идей.

Коммит: `[inputs] фаза 5: tag N of 60 existing ideas`.

### Фаза 6 — wiki/topics/system-design-hub.md (15 мин)

1. Grep всех файлов с `topics: [system-design]` → список новых + existing.
2. Создай `wiki/topics/system-design-hub.md` по шаблону `wiki/_templates/topic.md`:
   - Title: "System Design — Управление проектами, философия работы"
   - Summary: 2 параграфа
   - 6 секций (одна на часть SYSTEM-DESIGN-HUMAN.md) с wikilinks на relevant items
   - niche: meta
   - topics: [system-design]
3. Update `wiki/index.md` — добавить этот topic.
4. `/build-graph` — rebuild communities.

Коммит: `[inputs] фаза 6: system-design-hub topic + graph rebuild`.
**Push main.**

### Фаза 7 — Staging skeleton (5 мин)

Создай `design/SYSTEM-DESIGN-INPUTS.md` с frontmatter + 6 placeholder-секций:

```markdown
---
type: design-inputs
status: draft-staging
feeds: SYSTEM-DESIGN-HUMAN.md
author: claude-code-server
created: 2026-04-16
updated: 2026-04-16
stats:
  sources_scanned: {N}
  relevant_ingested: {N}
  total_wiki_pages_with_system-design_tag: {N}
---

# SYSTEM-DESIGN-INPUTS — выжимки под 6 частей SYSTEM-DESIGN-HUMAN.md

## Inputs для Части 1. Видение / Стратегия
_(staging-writer 1 работает)_

## Inputs для Части 2. Пользователи / Роли
_(staging-writer 2 работает)_

## Inputs для Части 3. Потоки информации
_(staging-writer 3 работает)_

## Inputs для Части 4. Действия / Триггеры
_(staging-writer 4 работает)_

## Inputs для Части 5. Состояния / Жизненный цикл
_(staging-writer 5 работает)_

## Inputs для Части 6. Открытые вопросы (сквозные)
_(staging-writer 6 работает)_

## Приложение A. Отбраковка (IRRELEVANT) — только счётчики
- Всего помечено IRRELEVANT: {N}
- По главным причинам: {breakdown}

## Приложение B. UNCLEAR для ручного ревью Ruslan
{list}

## Приложение C. Что НЕ обработано
- knowledge-base/ legacy — см. MIGRATION.md
- voice-memos — требуют транскрибации
```

Коммит: `[inputs] фаза 7: staging skeleton created`.

### Фаза 8 — Заполнение 6 частей staging через sub-agents (40-80 мин)

**Параллельно** spawn 6 `staging-writer` sub-agents через Task tool,
по одному на часть (1-6). Каждый:
- читает `.claude/agents/staging-writer.md` (свой role prompt)
- получает от тебя: номер части (1-6)
- сам делает grep/read по `wiki/` с `topics: [system-design]`
- записывает секцию в `design/SYSTEM-DESIGN-INPUTS.md` через Edit
  (замена placeholder'а)
- возвращает короткий отчёт

Если 529 → run sequentially (one part at a time).

После того как все 6 вернулись — проверь целостность staging-файла
(нет placeholder'ов осталось).

Коммит: `[inputs] фаза 8: staging parts 1-6 filled (N chars total)`.

### Фаза 9 — Финальный отчёт + push (10 мин)

Создай `reports/system-design-inputs-collection-2026-04-16.md`:

```markdown
---
type: collection-report
date: 2026-04-16
phase: step-2-inputs
author: claude-code
status: complete
---

# System Design Inputs — Collection Report (2026-04-16)

## Сводка

- Всего идей в Notion Bank: {N}
- Уже импортированные до sweep (60): прошлось через тег-классификацию, RELEVANT: {N}
- Новые из sweep:
  - RELEVANT ingested: {N}
  - IRRELEVANT: {N}
  - UNCLEAR: {N}
- Notion-страниц о системе ingested: 11/11 (или {N} с ошибками)
- Daily Log записей обработано: {N} дат, insights извлечено: {N}
- wiki/ сейчас: {N} страниц (+{delta} vs старт)
- wiki/graph/edges.jsonl: {M} edges (+{delta})
- Communities после /build-graph: {K}
- Lint: broken links {N}, orphans {N}

## Главные выходы

| Файл | Размер | Описание |
|------|--------|----------|
| wiki/topics/system-design-hub.md | {N} строк | навигационный узел |
| design/SYSTEM-DESIGN-INPUTS.md | {N} строк | staging для Ruslan |

## 3 insight'а которые обнаружил

1. ...
2. ...
3. ...

## UNCLEAR для ручного ревью Ruslan

- {id1} — {title} — {почему сомнение}
- ...

## Commits

- {SHA1} фаза 2 sweep
- {SHA2} фаза 3 pages
- {SHA3} фаза 4 daily-log
- {SHA4} фаза 5 tag
- {SHA5} фаза 6 hub + graph
- {SHA6} фаза 7 skeleton
- {SHA7} фаза 8 staging parts
- {SHA8} этот отчёт

## Время

- Старт: HH:MM
- Финиш: HH:MM
- Duration: {часы}

## Следующий шаг

Ruslan открывает `design/SYSTEM-DESIGN-INPUTS.md` как второе панно в Antigravity
(split view рядом с `SYSTEM-DESIGN-HUMAN.md`), читает, возвращается в чат
с Claude Code (main, локально Windows) и диктует Часть 1 SYSTEM-DESIGN-HUMAN.md.
```

Коммит: `[inputs] фаза 9: final report + push`.
**Push main.**

### Фаза 10 — Отчёт в чат

Финальный ответ (не более 40 строк):
- Total ideas scanned / RELEVANT / IRRELEVANT / UNCLEAR
- Главные выходы (2 файла)
- 3 insight'а
- Список UNCLEAR (до 10 штук)
- Время
- Ссылка на коммиты и финальный отчёт
- "Ruslan может начинать диктовку Части 1 в SYSTEM-DESIGN-HUMAN.md".

---

## ПРАВИЛА БЕЗОПАСНОСТИ (кратко)

- ✅ Можно: Read/Write/Edit внутри `~/jetix-os/`, Bash внутри `~/jetix-os/`,
  Grep, Glob, Task (spawn sub-agents), mcp__notion-*, git (pull/add/commit/push
  на origin main).
- ❌ Нельзя: WebFetch, WebSearch, rm -rf, git push --force, git rebase,
  trash в `.env`, `private/`, `~/.ssh/`, `dashboard/`, `config/*.secret.*`,
  `knowledge-base/`, force push в main.
- ❌ Нельзя: спрашивать подтверждений.
- ⚠️ Notion MCP SPOF: если отваливается — SAFE-SAVE (commit+push) + report.

---

## DEPENDENCIES

Должны существовать в репо на момент запуска:

- `SYSTEM-DESIGN-HUMAN.md` ✓ (есть, 279 строк)
- `ARCHITECTURE-CURRENT.md` ✓ (есть, 332 строки)
- `.claude/agents/sweep-worker.md` ✓
- `.claude/agents/staging-writer.md` ✓
- `.claude/skills/sweep-notion-bank.md` ✓
- `wiki/_templates/` — 9 шаблонов ✓
- Notion MCP активен
- git remote origin = https://github.com/Bogersebekov/jetix-os.git

Проверь `ls` перед стартом.

---

## SUCCESS CRITERIA

- [ ] `wiki/topics/system-design-hub.md` существует и содержит 6 секций с
      wikilinks на все relevant items
- [ ] `design/SYSTEM-DESIGN-INPUTS.md` существует, 6 частей заполнены,
      placeholder'ов не осталось
- [ ] Attribution на каждом тезисе staging-файла
- [ ] `reports/system-design-inputs-collection-2026-04-16.md` существует
- [ ] 8-9 коммитов в main, все запушены в origin
- [ ] Размер wiki увеличен минимум на 50+ страниц
- [ ] `/lint` не показывает критичных broken links
- [ ] Отчёт в чат содержит 3 insight'а + UNCLEAR list

После выполнения — тишина. Ruslan прочитает staging и вернётся к диктовке.
