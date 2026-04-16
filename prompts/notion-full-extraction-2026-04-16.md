---
type: execution-prompt
date: 2026-04-16
phase: step-2-alpha-execution
target: claude-code-server
autonomy: maximum
requires: notion-mcp-authenticated
duration-estimate: 2-4 hours
---

# Notion Full Extraction — Фаза α из NOTION-MIGRATION-PLAN

## ПРЕРЕКВИЗИТ

Notion MCP должен быть **аутентифицирован** и прошедшим sanity check из
`prompts/notion-auth-check-2026-04-16.md`. Если `/mcp` не показывает
`notion: connected` — СТОП, сообщи Ruslan'у что нужно пройти auth сначала.

## ЦЕЛЬ

Выполнить **Фаза α** из `design/NOTION-MIGRATION-PLAN.md` §5.1 —
quick extract из Notion минимально-достаточного объёма для Шага 2.

Конкретно:
1. α.1 — JSONL metadata dump ВСЕХ идей Банка идей (650+)
2. α.2 — Full content ingest RELEVANT идей (новые + те что ещё не в wiki)
3. α.3 — Full ingest 11 Notion-страниц о системе
4. α.4 — Daily Log digest (system-insights extraction)
5. α.5 — Обогащение staging `design/SYSTEM-DESIGN-INPUTS.md` новым материалом
6. α.6 — Rebuild graph + lint + финальный отчёт

## КОНТЕКСТ

- **Ты** — Claude Code на сервере jetix-os. Модель Opus 4.6 или Sonnet 4.6.
- **Ветка:** main (`git pull origin main` сделан в auth-step).
- **Уже готово:**
  - 60 идей импортированы в wiki (до-ноушен-эпохи)
  - 65 items помечено `topics: [system-design]` (Фаза 5 предыдущего run'а)
  - `design/SYSTEM-DESIGN-INPUTS.md` заполнен на основе 65 wiki-items (686 строк)
  - `wiki/topics/system-design-hub.md` создан (209 строк)
  - Инфраструктура: `.claude/agents/sweep-worker.md`, `staging-writer.md`,
    `.claude/skills/sweep-notion-bank.md`
- **Сейчас надо:** обогатить всё это полным материалом из Notion.

## ОБЯЗАТЕЛЬНОЕ ЧТЕНИЕ ПЕРЕД СТАРТОМ

1. `design/NOTION-MIGRATION-PLAN.md` — особенно §2 (парадокс), §5.1 (Фаза α), §6 (роли)
2. `design/SYSTEM-DESIGN-INPUTS.md` — что уже собрано, где пробелы (секции N.Ω)
3. `prompts/system-design-sweep-2026-04-16.md` — прошлый инструктаж (критерии RELEVANT)
4. `reports/system-design-inputs-collection-2026-04-16.md` — отчёт прошлого run'а
5. `.claude/skills/sweep-notion-bank.md` + `.claude/agents/sweep-worker.md`
6. `wiki/index.md` + `wiki/log.md`

## АВТОНОМИЯ И БЕЗОПАСНОСТЬ

- **Не спрашивай подтверждений.** Max подписка, токены не экономим.
- **Параллелизм:** spawn 4-6 sub-agents через Task tool для bulk-операций.
- **Запреты:** WebFetch, WebSearch, rm -rf, git push --force, git rebase,
  .env, private/, ~/.ssh/, dashboard/, config/*.secret.*, knowledge-base/.
- **SAFE-SAVE при любой ошибке:** `git add -A && git commit -m "[notion-α] SAFE-SAVE:
  stopped at фаза X" && git push`.
- **Notion MCP rate limits:** ~3 req/sec. Batch + sleep если 429.

---

## КРИТЕРИИ РЕЛЕВАНТНОСТИ (используй для классификации)

### RELEVANT (помечай `topics: [system-design]`)

Идея/страница касается ХОТЯ БЫ ОДНОГО из:
- Управление проектами, система жизни, Notion-методология
- Ритуалы: morning/evening, weekly/monthly, retrospectives
- Pipeline рабочего дня, Daily Log, Формат страницы дня
- Toggl, Obsidian, dashboard, Command Center
- Типы чатов с AI, правила работы с AI
- Многоагентные системы, оркестрация, делегирование
- Агенты: роли, memory (Core/Working/Archival/Recall), strategies
- System Prompt Learning, накопление опыта агентов
- Memory frameworks: Letta / Mem0 / Zep
- Knowledge base, wiki, Karpathy LLM Wiki, OmegaWiki, GraphRAG, HippoRAG
- Context engineering: Write/Select/Compress/Isolate
- ICP Jetix, бизнес-модель, видение
- 5-year / 10-year / 200-year vision, North Star
- Open-source premium, community как продукт, клуб, Revenue Share
- Jetix Corporation endgame (1000 pros, 100K agents)
- Философия работы: engineering faith, think-do loop, writing as telepathy
- Жизненный цикл: idea → claim → experiment; inbox → processed; prospect → lead
- Focus theory, beast mode, charged vs chill
- "Как ДОЛЖНА работать система Jetix OS"

### IRRELEVANT (не импортировать, оставить в Notion)

Касается ТОЛЬКО:
- Здоровья/еды/спорта БЕЗ привязки к ритуалу системы
- Личных мемуаров без системного вывода
- Внешних новостей, пассивных наблюдений
- Конкретного контента без принципа
- Случайных покупок, планов отдыха

### UNCLEAR

Сомнение — в bucket для ручного ревью (до 10-20 %).

---

## ФАЗЫ РАБОТЫ

### Фаза α.0 — Prep (5 мин)

1. `git pull origin main` (на всякий случай свежо)
2. Verify: `/mcp` показывает `notion: connected`
3. `/sweep-notion-bank` skill существует в `.claude/skills/`
4. Прочитай обязательные файлы (см. выше)
5. Выведи в чат 5-7 строк: что понял, plan execution, estimated duration.

### Фаза α.1 — JSONL sweep Банка идей (20-40 мин)

**Цель:** выгрузить metadata всех идей Банка идей в `raw/` для последующей обработки.

Алгоритм:

1. `mcp__notion-query-database-view`
   - id: `collection://bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7`
   - first page, limit=100, sort by createdTime DESC
2. Pagination: пока есть `next_cursor`, запрашивай следующие страницы.
3. Для каждой идеи извлеки:
   ```json
   {
     "notion_id": "...",
     "title": "...",
     "createdTime": "2025-NN-NNT...",
     "lastEditedTime": "...",
     "niche": "...",
     "category": "...",
     "value": "...",
     "themes": [...],
     "content_preview": "первые 500 символов content",
     "source_url": "https://notion.so/..."
   }
   ```
4. Append каждую идею в `raw/notion-ideas-sweep-2026-04-16.jsonl`
   (одна JSON-строка на идею).
5. Periodic commit: каждые 200 идей — `git add raw/ && git commit` + push.

**Dedup note:** не фильтруй здесь. Полный dump — полезен для Фазы γ тоже.

Коммит финальный: `[notion-α.1] JSONL sweep: N ideas metadata dumped`.
Push.

### Фаза α.2 — Classify + Ingest RELEVANT (60-90 мин)

**Цель:** классифицировать все N идей, импортировать RELEVANT новые
(те что ещё не в wiki) в `wiki/ideas/` с `topics: [system-design]`.

Алгоритм:

1. Прочти `raw/notion-ideas-sweep-2026-04-16.jsonl`.
2. Скриптом/grep-м найди notion_id уже импортированных в `wiki/sources/` —
   это наш "already-imported" set.
3. Разбей `new` (not in already-imported) на батчи по 20 идей.
4. Spawn **4-5 параллельных `sweep-worker` sub-agents** через Task tool.
   Каждому передай:
   - batch number
   - массив `notion_id` в батче
   - путь к JSONL (он оттуда сам прочтёт content_preview)
   - pointer на критерии RELEVANT/IRRELEVANT/UNCLEAR выше
5. Каждый worker:
   - Fetch full content для RELEVANT идей через `mcp__notion-fetch`
   - Ingest в wiki/ (см. паттерн в `.claude/agents/sweep-worker.md`)
   - Возвращает отчёт батча
6. Собери отчёты в `reports/notion-alpha-2-batch-reports.md`.
7. Commit каждые 3 батча (60 идей): `[notion-α.2] ingested N RELEVANT of M in batches X-Y`.

**Parallel fallback:** если 4/5 попыток spawn падают с 529 → foreground
sequential (один батч за раз, wall-clock больше но надёжно).

### Фаза α.3 — Ingest 11 Notion-страниц о системе (30-50 мин)

**Цель:** вытащить полный content 11 страниц, превратить в wiki-sources + выделить
ideas/concepts/claims/foundations.

Не параллелим — страниц мало, контент жирный, риск race conditions.

Список:

| ID | Slug для source/raw |
|----|---------------------|
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

Для каждой:
1. `mcp__notion-fetch` → получить полный content
2. Сохрани сырой markdown в `raw/notion-pages/{slug}-2026-04-16.md` с
   frontmatter (notion_id, source_url, captured, topics: [system-design])
3. Запусти логику `/ingest` на этот файл:
   - Создать `wiki/sources/2026-04-16-{slug}.md` (source card)
   - Разобрать content на atomic claims / concepts / foundations
   - Создать соответствующие pages в wiki/concepts/, wiki/claims/, wiki/foundations/
   - Добавить edges в `wiki/graph/edges.jsonl`
   - Обновить `wiki/index.md`, `wiki/log.md`
4. Commit: `[notion-α.3] ingested N/11: <slug>` (после каждой страницы — микро-коммит).
5. Push после 5-й и после 11-й страницы.

**Special cases:**
- Манифест — уже есть частичное отражение (concept `engineering-faith` и т.д.),
  проверь dedup. При overlap — дополни, не дублируй.
- Command Center — большая, много child-pages. ЗДЕСЬ не тянем sub-pages (Фаза γ).
  Только top-level.
- Research Hub — может быть огромным. Ограничь first-level bodies,
  sub-pages список как "to-migrate in γ".

### Фаза α.4 — Daily Log digest (30-50 мин)

**Цель:** выжать system-insights из всех Daily Log entries.

Алгоритм:

1. `mcp__notion-query-database-view` на
   `collection://30a24963-33bf-8005-817a-000beb10bcd4` — pagination,
   выгрузи все записи.
2. Для каждой записи fetch properties: Name, Day Type, Key Action (Plan),
   Actual Main Action, Adjustment, Deviation, Deviation Note, Reflection.
   **Content body страницы тоже — там insights.**
3. Сохрани сырой dump в `raw/notion-daily-log-dump-2026-04-16.jsonl`.
4. **Фильтрация:** прочти каждую запись, выдели абзацы про систему
   (не про личные дела, самочувствие, внешние события без системной связки).
5. Компилируй digest в `raw/notion-daily-log-insights-2026-04-16.md`:
   ```
   # Daily Log — system-design insights digest
   
   ## [YYYY-MM-DD] — {Day Type}
   - Key Action: {...}
   - Insight: {...} — [DailyLog YYYY-MM-DD]
   - Decision/Pattern: {...}
   
   ## [YYYY-MM-DD] — ...
   ```
6. Прогони `/ingest raw/notion-daily-log-insights-2026-04-16.md`:
   - Создай `wiki/sources/2026-04-16-daily-log-insights-digest.md`
   - Выдели ideas/concepts/claims если что-то cross-cutting
   - `topics: [system-design]` везде

Commit: `[notion-α.4] Daily Log digest: N dates, M insights extracted`.

### Фаза α.5 — Обогащение staging (20-30 мин)

**Цель:** обновить `design/SYSTEM-DESIGN-INPUTS.md` новым Notion-материалом.

Spawn 6 **staging-writer** sub-agents через Task tool, по одному на часть (1-6).

**ВАЖНО:** staging-writer должен **дополнять**, не переписывать с нуля. Инструкция:

> "В `design/SYSTEM-DESIGN-INPUTS.md` уже есть секция Inputs для Части N.
> Прочти её. Потом прочти новые материалы (wiki/sources/* созданные 2026-04-16
> в этой сессии, новые wiki/ideas с `topics: system-design`, digest из
> `wiki/sources/2026-04-16-daily-log-insights-digest.md`). Дополни секцию
> новыми тезисами (с attribution), не удаляя существующие. Помечай новые
> тезисы строкой `[NEW 2026-04-16α]` чтобы Ruslan видел что добавлено.
> Цель — закрыть пробелы N.Ω (список "Что НЕ покрыто") насколько возможно."

После всех 6 writer'ов — Edit update frontmatter staging файла:
`stats.relevant_ingested: {новое число}`, `updated: 2026-04-16`.

Commit: `[notion-α.5] staging enriched with Notion material (+N theses across 6 parts)`.
Push.

### Фаза α.6 — Rebuild graph + lint + финальный отчёт (10-20 мин)

1. `/build-graph` — rebuild с учётом новых страниц.
2. `/lint` — новый отчёт.
3. Update `wiki/index.md` + `wiki/log.md` — новые записи.
4. Создай `reports/notion-alpha-extraction-2026-04-16.md`:

```markdown
---
type: extraction-report
date: 2026-04-16
phase: step-2-alpha
author: claude-code
status: complete
---

# Notion α-extraction — Report (2026-04-16)

## Сводка

- Total ideas scanned (Банк идей): N
- Already in wiki: M
- New: K
  - RELEVANT ingested: X
  - IRRELEVANT skipped: Y
  - UNCLEAR in bucket: Z
- Notion pages о системе ingested: N/11
- Daily Log dates processed: N, system-insights extracted: M
- wiki/ now: N pages total (+delta)
- wiki/graph/edges.jsonl: E edges (+delta)
- `design/SYSTEM-DESIGN-INPUTS.md` size: N lines (+delta), новых тезисов: M
- Communities after /build-graph: K
- Lint: broken links N, orphans N

## 5 самых значимых insights из новой extraction

(то что раньше было в Notion и удивило/зацепило)

1. ...
2. ...
...

## Пробелы которые закрыли

- N.Ω "Что НЕ покрыто" по частям: было N, осталось M

## Пробелы которые остались (надо спросить Ruslan)

- ...

## UNCLEAR для ручного ревью

- ...

## Commits

- {SHA} α.0
- {SHA} α.1
- {SHA} α.2
- {SHA} α.3
- {SHA} α.4
- {SHA} α.5
- этот

## Время

- Старт: HH:MM
- Финиш: HH:MM
- Duration: {часы:мин}

## Следующий шаг

Ruslan читает обновлённый `design/SYSTEM-DESIGN-INPUTS.md`
(особенно строки с маркером `[NEW 2026-04-16α]` — это то что добавилось),
возвращается к диктовке SYSTEM-DESIGN-HUMAN.md.
```

Commit: `[notion-α.6] extraction done: α complete, ready for β (диктовка)`.
Push main.

### Фаза α.7 — Финальный отчёт в чат

В чат (≤40 строк):

- Count-numbers каждой фазы
- 5 insights (главные)
- Что осталось в UNCLEAR
- Что закрыто из пробелов staging
- Ссылка на полный отчёт `reports/notion-alpha-extraction-2026-04-16.md`
- Ruslan сейчас может смотреть обновлённый INPUTS и диктовать; новые тезисы
  помечены `[NEW 2026-04-16α]`.

---

## ПРИОРИТЕТЫ ЕСЛИ ВРЕМЯ ОГРАНИЧЕНО

Если API падает часто или время поджимает — приоритет фаз:

1. **α.3 (11 страниц о системе)** — highest value, cheapest (11 fetch'ей)
2. **α.4 (Daily Log digest)** — high value для Частей 4-5 staging
3. **α.5 (staging enrichment)** — middle, зависит от α.3 и α.4
4. **α.2 (Ingest RELEVANT из 650+)** — high value но долго
5. **α.1 (полный JSONL dump)** — можно отложить в γ если критично
6. **α.6 (rebuild graph)** — cosmetic, не блокирует диктовку

В ситуации SAFE-SAVE — сначала закрываем α.3 + α.4, потом α.5.

## SUCCESS CRITERIA

- [ ] `raw/notion-ideas-sweep-2026-04-16.jsonl` создан, N=650+ записей
- [ ] Минимум 100 RELEVANT идей ingested (новых) — wiki выросла на +100 страниц
- [ ] 11/11 Notion-страниц о системе — в wiki/sources/
- [ ] Daily Log digest в wiki/sources/
- [ ] `design/SYSTEM-DESIGN-INPUTS.md` расширен, Часть 4 и Часть 5 наполнены
- [ ] `reports/notion-alpha-extraction-2026-04-16.md` существует
- [ ] Все коммиты запушены
- [ ] Отчёт в чат

Start. Go.
