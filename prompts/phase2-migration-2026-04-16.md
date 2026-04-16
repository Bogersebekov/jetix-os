---
title: "Phase 2 Migration — Karpathy LLM Wiki + OmegaWiki + 5-layer Agent Memory"
date: 2026-04-16
type: claude-code-prompt
status: ready
target: Claude Code на сервере 100.99.156.28 (Antigravity + SSH)
---

# ЗАДАЧА: Phase 2 Migration — Wiki + Agent Memory

**Как использовать:** на сервере `cd ~/jetix-os && git pull && claude`, затем дать Claude Code этот файл через `@prompts/phase2-migration-2026-04-16.md выполни`.

---

## КОНТЕКСТ

Я владелец Jetix OS — мульти-агентной системы (12 агентов, 6 департаментов).
Мы переходим на новую архитектуру памяти и базы знаний, основанную на:

- Karpathy LLM Wiki pattern (raw/ → wiki/ + index.md + log.md, операции ingest/ask/lint)
- OmegaWiki 9 entity types + 9 typed edges (knowledge graph поверх wiki)
- Letta-inspired 5-layer memory для каждого агента

Финальный документ архитектуры: https://www.notion.so/3442496333bf819cb864cf0e04c9de74
Прочитай его через Notion MCP если есть доступ — там полная картина и обоснование решений.

Первоисточники (для понимания принципов, НЕ для исполнения):

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (Karpathy LLM Wiki)
- https://github.com/skyllwt/OmegaWiki (прецедент реализации с 23 skills)
- https://x.com/karpathy/status/1921368644069765486 (System Prompt Learning)
- https://x.com/karpathy/status/1937902205765607626 (Context Engineering)

## ПРИНЦИПЫ РАБОТЫ

1. **Additive only.** Ничего не удаляй и не перезаписывай. Если папка/файл существует — оставь как есть, добавь только недостающее.
2. **Не трогать:** существующий `knowledge-base/`, существующий `raw/` (там уже есть transcripts/ и voice-memos/ — добавь рядом articles/, meetings/, books/, web/), `agents/*.md`, `comms/mailboxes/`, `shared/state/`, `tools/`, `dashboard/`, `_meta/`, `projects/`, `crm/`, `inbox/`, `ideas/`.
3. **Никогда не трогать:** `.env`, `private/`, `~/.ssh/`, `.git/`, `node_modules/`, `config/*.secret.*`.
4. Используй только Read/Write/Edit/Bash/Glob/Grep. Без внешних пакетов.
5. Все Markdown файлы создавай с YAML frontmatter.
6. Конвенции: kebab-case имена, YYYY-MM-DD даты, UTF-8, 2-space indent для JSON/YAML.
7. Язык: контент на русском, ключи/имена файлов на английском.
8. Каждая создаваемая директория получает `.gitkeep` ЛИБО `README.md` со стартовым содержимым.
9. После каждой из 5 фаз — коммит формата `[arch] phase2 stepN: описание`. Не push.

## ЦЕЛЕВАЯ СТРУКТУРА

```
jetix-os/
├── CLAUDE.md                           # уже есть, НЕ трогать (обновим отдельно)
├── raw/                                # РАСШИРИТЬ (уже есть transcripts/, voice-memos/)
│   ├── articles/                       # NEW
│   ├── transcripts/                    # УЖЕ ЕСТЬ — не трогать
│   ├── voice-memos/                    # УЖЕ ЕСТЬ — не трогать
│   ├── meetings/                       # NEW
│   ├── books/                          # NEW
│   ├── web/                            # NEW
│   └── README.md                       # создать если нет
│
├── wiki/                               # ПОЛНОСТЬЮ НОВАЯ
│   ├── index.md
│   ├── log.md
│   ├── overview.md
│   │
│   ├── concepts/                       # Entity 1
│   ├── entities/                       # Entity 2
│   ├── sources/                        # Entity 3
│   ├── topics/                         # Entity 4
│   ├── ideas/                          # Entity 5
│   ├── experiments/                    # Entity 6
│   ├── claims/                         # Entity 7
│   ├── summaries/                      # Entity 8
│   ├── foundations/                    # Entity 9
│   ├── comparisons/                    # bonus: filing loop от /ask
│   │
│   ├── niches/                         # domain slices
│   │   ├── personal/
│   │   ├── business/
│   │   ├── sales/
│   │   ├── life/
│   │   ├── tech/
│   │   └── meta/
│   │
│   ├── graph/                          # GraphRAG/HippoRAG слой
│   │   ├── edges.jsonl
│   │   ├── communities.md
│   │   └── summaries.md
│   │
│   └── _templates/                     # 9 шаблонов по entity types
│       ├── concept.md
│       ├── entity.md
│       ├── source.md
│       ├── topic.md
│       ├── idea.md
│       ├── experiment.md
│       ├── claim.md
│       ├── summary.md
│       └── foundation.md
│
├── agents/                             # УЖЕ ЕСТЬ — РАСШИРЯЕМ каждого
│   └── {agent-id}/                     # если есть только {agent-id}.md файл —
│       │                               # создай папку и перенеси в system.md
│       ├── system.md                   # Core memory
│       ├── strategies.md               # System prompt learning
│       ├── scratchpad.md               # Working memory
│       └── niche/                      # symlinks в wiki/niches/{dept}/
│
└── .claude/
    └── skills/                         # НОВЫЕ user-invocable skills
        ├── ingest.md
        ├── ask.md
        ├── lint.md
        ├── consolidate.md
        └── build-graph.md
```

## FRONTMATTER СХЕМА (для всех wiki страниц)

Используй в `_templates/`:

```yaml
---
title: "Название страницы"
type: concept | entity | source | topic | idea | experiment | claim | summary | foundation | comparison
niche: personal | business | sales | life | tech | meta | global
sources: [raw/articles/2026-04-16-example.md, ...]
related: [concepts/example.md, entities/another.md]
tags: [#topic/ai, #status/active]
created: 2026-04-16
updated: 2026-04-16
confidence: high | medium | low
pipeline: raw | ingested | ready
---
```

## GRAPH EDGES СХЕМА

`wiki/graph/edges.jsonl` — append-only, один JSON на строку:

```json
{"from": "concepts/value-based-pricing.md", "to": "entities/vladislav.md", "type": "derived_from", "created": "2026-04-16", "confidence": "high"}
```

9 edge types: `extends`, `contradicts`, `supports`, `inspired_by`, `tested_by`, `invalidates`, `supersedes`, `addresses_gap`, `derived_from`

## SKILLS — СПЕЦИФИКАЦИЯ

Каждый skill — Markdown файл в `.claude/skills/` с frontmatter `name`, `description`, `allowed-tools`. В теле — пошаговая инструкция для агента.

### `/ingest <path-or-url>`

1. Если URL — скачай в `raw/web/YYYY-MM-DD-slug.md` (WebFetch).
2. Если путь в raw/ — читаем оттуда.
3. Извлеки entities, concepts, claims — создай/обнови 10-15 страниц в wiki/.
4. Создай `wiki/sources/YYYY-MM-DD-slug.md` с summary и cross-refs.
5. Добавь edges в `wiki/graph/edges.jsonl`.
6. Обнови `wiki/index.md` (строка под соответствующей категорией).
7. Добавь в `wiki/log.md` запись `## [YYYY-MM-DD] ingest | source-slug` + что тронули.
8. Определи niche — добавь symlink в `wiki/niches/{niche}/`.

### `/ask <question>`

1. Прочитай `wiki/index.md` полностью.
2. Отбери 5-15 наиболее релевантных страниц.
3. Прочитай их, синтезируй ответ с цитатами в формате `[[file.md]]`.
4. Если ответ ценный (новая связь / противоречие / обобщение / неочевидный вывод) — сохрани в `wiki/comparisons/YYYY-MM-DD-question-slug.md` и обнови index + log.
5. Выведи ответ пользователю.

### `/lint`

Health check. 7 проверок:

1. Orphan pages (есть файл, нет ссылок).
2. Stale claims (confidence=low и updated > 60 дней).
3. Broken wikilinks.
4. Missing frontmatter.
5. Contradictions (через edge `contradicts`).
6. Missing cross-refs (упомянут 3+ раз, нет в `related`).
7. Index drift (файл есть, в index.md нет).

Выход: `wiki/_lint-report-YYYY-MM-DD.md`.

### `/consolidate`

Merge дубликатов. Найти страницы с похожими title/содержанием → предложить merge → после confirm человеком выполнить. Записать в log.

### `/build-graph`

1. Пройтись по всем `wiki/**/*.md`.
2. Для каждой пары (A, B) с перекрёстным упоминанием — убедиться что есть edge в `edges.jsonl`.
3. Простая community detection (density локальных групп; fallback — группировка по niche/topic).
4. Обновить `communities.md` и `summaries.md`.

## PER-AGENT MEMORY — 12 АГЕНТОВ

Манифест agent → niches:

| Agent | Niches |
|-------|--------|
| manager | meta + business |
| personal-assistant | personal + meta |
| system-admin | meta + tech |
| sales-lead | sales + business |
| sales-researcher | sales |
| sales-outreach | sales |
| inbox-processor | meta |
| crazy-agent | meta + tech |
| knowledge-synth | все 6 (доступ ко всему) |
| strategist | business + personal |
| life-coach | life + personal |
| meta-agent | meta |

Для каждого агента:

1. Проверь `agents/{agent-id}.md` или `agents/{agent-id}/`.
2. Если файл — создай папку, перенеси в `system.md`.
3. Если папка — добавь недостающие файлы.
4. Создай:
   - `system.md` — Core memory (тот же system prompt)
   - `strategies.md`:

     ```markdown
     ---
     agent: {agent-id}
     type: strategies
     created: 2026-04-16
     ---
     # Стратегии {agent-id}

     Формат: "Когда встречаю X — делаю Y, потому что Z".
     Добавляй новые стратегии после каждой сложной задачи.

     ## 2026-04-16 (initial)
     - (пусто, накапливаем с опытом)
     ```

   - `scratchpad.md`:

     ```markdown
     ---
     agent: {agent-id}
     type: scratchpad
     updated: 2026-04-16
     ---
     # Scratchpad {agent-id}

     Текущая задача: —
     Промежуточные заметки: —
     ```

   - `niche/` — папка с `README.md` + symlinks:
     `ln -s ../../../wiki/niches/{niche} ./niche/{niche}`

Если symlink не создаётся (ошибка ОС) — вместо него `niche/{niche}.md` с одной строкой `→ ../../../wiki/niches/{niche}/`.

## INDEX.MD — СТАРТОВОЕ СОДЕРЖИМОЕ

```markdown
---
type: index
updated: 2026-04-16
---
# Index — Jetix OS Wiki

Каталог всех страниц. Обновляется при каждом /ingest.
Формат: `- [Title](path) — one-line summary [niche] [sources: N]`

## Concepts
(empty)

## Entities
(empty)

## Sources
(empty)

## Topics
(empty)

## Ideas
(empty)

## Experiments
(empty)

## Claims
(empty)

## Summaries
(empty)

## Foundations
(empty)

## Comparisons
(empty)
```

## LOG.MD — СТАРТОВОЕ СОДЕРЖИМОЕ

```markdown
---
type: log
updated: 2026-04-16
---
# Log — Jetix OS Wiki

Append-only хронология. Новые записи сверху.

## [2026-04-16] init | wiki-structure-created
Создана базовая структура wiki/: index.md, log.md, 9 entity type папок, niches/, graph/, _templates/.
```

## OBSIDIAN СОВМЕСТИМОСТЬ

Ruslan подключит Obsidian vault к `wiki/` позднее. Требования:

1. Не создавай `wiki/.obsidian/` — Obsidian сделает сам.
2. Все cross-refs в страницах — формат `[[relative/path/to/file]]`.
3. Создай `wiki/.gitignore`:

   ```
   .obsidian/workspace*
   .obsidian/cache
   .obsidian/appearance.json
   ```

4. Простые имена файлов без спец-символов.

## МИГРАЦИЯ СТАРОГО KNOWLEDGE-BASE (НЕ СЕЙЧАС)

НЕ мигрируй `knowledge-base/` сейчас. Вместо этого:

1. В `raw/README.md` — секция "Migration plan".
2. В корневом `MIGRATION.md` — план со статусами:
   - [ ] knowledge-base/ → wiki/ via /ingest
   - [ ] raw/transcripts/ существующие → wiki/ via /ingest
   - [ ] raw/voice-memos/ → сначала transcribe через tools/, потом /ingest
   - [ ] Notion pages → ручной экспорт (позже)
3. Старую структуру НЕ удаляй.

## ОТЧЁТ — ОБЯЗАТЕЛЬНЫЙ

Создай `reports/arch-migration-2026-04-16.md` и выведи его содержимое в чат. Формат:

```markdown
---
type: migration-report
date: 2026-04-16
phase: 2
---
# Отчёт миграции: Phase 2 — Wiki + Agent Memory

## Что создано

### Структура wiki/
(таблица: путь / тип / размер / статус)

### Структура raw/ (расширение)
(какие папки добавлены)

### Skills
- [x] .claude/skills/ingest.md
- [x] .claude/skills/ask.md
- [x] .claude/skills/lint.md
- [x] .claude/skills/consolidate.md
- [x] .claude/skills/build-graph.md

### Per-agent memory (12 агентов)
(таблица: agent / system.md / strategies.md / scratchpad.md / niche/ symlinks + какие niches)

## Что НЕ сделано и почему
- knowledge-base/ миграция — отложено, план в MIGRATION.md
- voice-memos — ожидают transcribe
- Obsidian vault init — делает Ruslan вручную
- CLAUDE.md обновления — требуют ручного решения

## Проверка безопасности
- [x] .env не тронут
- [x] private/ не тронут
- [x] knowledge-base/ не тронут
- [x] agents/*.md перенесены (не удалены) — список

## Открытые вопросы для Ruslan
1. ...
2. ...

## Статистика
- Создано файлов: N
- Создано папок: N
- Создано symlinks: N
- Git коммитов: N

## Next steps (Phase 3)
1. Ruslan: открыть Obsidian vault на wiki/
2. Первый /ingest на реальном источнике
3. После 3-5 успешных ingest — /lint
4. После 10+ страниц — /build-graph
```

## GIT КОММИТЫ (по фазам)

1. `[arch] phase2 step1: raw/ expansion + wiki/ skeleton + templates`
2. `[arch] phase2 step2: index.md + log.md + niches/ + graph/`
3. `[arch] phase2 step3: skills (ingest, ask, lint, consolidate, build-graph)`
4. `[arch] phase2 step4: per-agent memory structure (12 agents)`
5. `[arch] phase2 step5: migration plan + report`

НЕ пушить. Ruslan решит сам.

## ПОРЯДОК ИСПОЛНЕНИЯ

1. Прочитай структуру проекта (`ls -la`, `ls agents/`, `ls raw/`).
2. Построй план в TodoWrite на 5 шагов.
3. Step 1 → коммит.
4. Step 2 → коммит.
5. Step 3 → коммит.
6. Step 4 → коммит.
7. Step 5 → генерируй отчёт, финальный коммит.
8. Выведи отчёт в чат.

## КРАЙНИЕ СЛУЧАИ

- `agents/{agent-id}.md` нет → создай папку и `system.md` с `# TODO: system prompt`.
- Symlink не создаётся → создай `niche/{niche}.md` с указателем на путь.
- Конфликт имён → не перезаписывай, создай `.new` версию, сообщи в отчёте.
- `raw/` уже есть с transcripts/ и voice-memos/ → не трогай их, просто добавь недостающие подпапки.

## ЧТО НЕ ДЕЛАТЬ

- Не трогать `knowledge-base/`, `_meta/`, `tools/`, `dashboard/`, `private/`, `.env`, `projects/`, `crm/`, `inbox/`, `ideas/`.
- Не удалять `agents/{agent-id}.md` без переноса в `system.md`.
- Не пушить в git.
- Не устанавливать пакеты.
- Не трогать корневой `CLAUDE.md` (обновим после отчёта).
- Не запускать `/ingest`, `/ask` и т.д. сам — только создай skills, тестирование отдельно.

Работаем.
