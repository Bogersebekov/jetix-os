---
type: migration-report
date: 2026-04-16
phase: 2
author: claude-code
status: complete
---
# Отчёт миграции: Phase 2 — Wiki + Agent Memory

Выполнено на сервере 100.99.156.28 по инструкции `prompts/phase2-migration-2026-04-16.md`.
Принцип: additive only, ничего не удалено, ничего не перезаписано.

## Что создано

### Структура `wiki/`

| Путь | Тип | Назначение | Статус |
|------|-----|-----------|--------|
| `wiki/index.md` | index | каталог всех страниц | seed |
| `wiki/log.md` | log | append-only хронология | seed |
| `wiki/overview.md` | doc | обзор архитектуры для людей | seed |
| `wiki/.gitignore` | config | игнор `.obsidian/workspace*` и т.п. | done |
| `wiki/concepts/` | entity dir | концепции, фреймворки | empty |
| `wiki/entities/` | entity dir | люди, компании, продукты | empty |
| `wiki/sources/` | entity dir | карточки источников | empty |
| `wiki/topics/` | entity dir | темы / кластеры | empty |
| `wiki/ideas/` | entity dir | гипотезы | empty |
| `wiki/experiments/` | entity dir | проверки гипотез | empty |
| `wiki/claims/` | entity dir | утверждения | empty |
| `wiki/summaries/` | entity dir | сводки | empty |
| `wiki/foundations/` | entity dir | базовые принципы | empty |
| `wiki/comparisons/` | bonus dir | сохранённые ответы `/ask` | empty |
| `wiki/niches/personal/` | niche | личный домен | README |
| `wiki/niches/business/` | niche | Jetix как бизнес | README |
| `wiki/niches/sales/` | niche | продажи | README |
| `wiki/niches/life/` | niche | здоровье, энергия | README |
| `wiki/niches/tech/` | niche | технологии | README |
| `wiki/niches/meta/` | niche | сама система | README |
| `wiki/graph/edges.jsonl` | data | 9-типовой граф, append-only | empty |
| `wiki/graph/communities.md` | doc | кластеры (из `/build-graph`) | seed |
| `wiki/graph/summaries.md` | doc | HippoRAG summaries | seed |
| `wiki/_templates/*.md` | 9 templates | concept, entity, source, topic, idea, experiment, claim, summary, foundation | done |

### Структура `raw/` (расширение)

Добавлены папки (существующие transcripts/ и voice-memos/ не тронуты):

- `raw/articles/` (new)
- `raw/meetings/` (new)
- `raw/books/` (new)
- `raw/web/` (new, для `/ingest <url>`)
- `raw/README.md` (new, с migration plan)

### Skills (`.claude/skills/`)

| Skill | Путь | Статус |
|-------|------|--------|
| `/ingest` | `.claude/skills/ingest.md.new` | создан под новой структурой; конфликт имён с существующим |
| `/ask` | `.claude/skills/ask.md` | done |
| `/lint` | `.claude/skills/lint.md` | done |
| `/consolidate` | `.claude/skills/consolidate.md` | done |
| `/build-graph` | `.claude/skills/build-graph.md` | done |

⚠️ **Конфликт:** `.claude/skills/ingest.md` уже существовал (старая версия raw → KB).
Новая версия — под wiki-архитектуру — сохранена как `ingest.md.new`.
Требуется ручное решение Руслана: удалить старую, переименовать новую.

### Per-agent memory (12 агентов)

Все 12 агентов получили 4 новых файла/папки. `baseline.md` оставлен как есть (additive).

| Agent | system.md | strategies.md | scratchpad.md | niche/ symlinks |
|-------|:---------:|:-------------:|:-------------:|-----------------|
| manager | ✓ (copy of baseline) | ✓ | ✓ | business, meta |
| personal-assistant | ✓ | ✓ | ✓ | personal, meta |
| system-admin | ✓ | ✓ | ✓ | meta, tech |
| sales-lead | ✓ | ✓ | ✓ | sales, business |
| sales-researcher | ✓ | ✓ | ✓ | sales |
| sales-outreach | ✓ | ✓ | ✓ | sales |
| inbox-processor | ✓ | ✓ | ✓ | meta |
| crazy-agent | ✓ | ✓ | ✓ | meta, tech |
| knowledge-synth | ✓ | ✓ | ✓ | personal, business, sales, life, tech, meta (все 6) |
| strategist | ✓ | ✓ | ✓ | business, personal |
| life-coach | ✓ | ✓ | ✓ | life, personal |
| meta-agent | ✓ | ✓ | ✓ | meta |

Всего symlinks: **24** (по одному на пару agent × niche). Все создались без fallback'ов.

## Что НЕ сделано и почему

- **knowledge-base/ миграция** — отложена, план в `MIGRATION.md`. Делается постепенно через `/ingest`.
- **voice-memos/ → wiki** — ожидают transcribe через существующий `tools/transcribe.py`, затем `/ingest`.
- **Obsidian vault init** — делает Руслан вручную (открывает `wiki/` как vault).
- **CLAUDE.md обновления** — требуют ручного решения (что оставить, что переписать под новую структуру). Не тронут.
- **Перенос `baseline.md` → `system.md`** — сделана копия, не переименование. Если хочется canonical — нужно вручную решить, какой файл оставить.
- **Старый `.claude/skills/ingest.md`** — не удалён. Новый под именем `ingest.md.new`. Руслан решает.

## Проверка безопасности

- [x] `.env` не тронут
- [x] `private/` не тронут
- [x] `.git/` не тронут
- [x] `knowledge-base/` не тронут
- [x] `_meta/`, `tools/`, `dashboard/`, `projects/`, `crm/`, `inbox/`, `ideas/` не тронуты
- [x] `agents/{id}/baseline.md` оставлены на месте (копии в `system.md`)
- [x] Существующие `.claude/skills/` не перезаписаны (новый ingest как `.new`)
- [x] `raw/transcripts/`, `raw/voice-memos/`, `raw/imports/`, `raw/research/` не тронуты

## Открытые вопросы для Руслана

1. **`baseline.md` vs `system.md`.** Сейчас обе существуют с одинаковым содержимым.
   Выбрать единый источник правды — и удалить вторую (либо оставить baseline как snapshot,
   а system — как рабочую версию).
2. **`.claude/skills/ingest.md` vs `ingest.md.new`.** Поведение сильно разное (старое —
   raw→KB, новое — raw→wiki). Какое оставить? Можно сосуществовать, если переименовать
   одну из команд (например `/ingest-kb`).
3. **Миграция `knowledge-base/`.** Начинаем прямо сейчас или дождаться обкатки skills
   на 2-3 внешних источниках?
4. **Obsidian vault — где открываем?** Только `wiki/` или шире (весь `jetix-os/`)?
   Если шире — нужен корневой `.obsidian/` в `.gitignore`.
5. **Niche `global`.** Сейчас его нет как папки (только в enum у frontmatter).
   Создать `wiki/niches/global/` или оставить как логический label?

## Статистика

- Git коммитов: **5** (step1 → step5)
- Создано файлов в wiki/: **24** (index/log/overview + 9 templates + 6 niche READMEs + 3 graph + .gitignore + 10 .gitkeep)
- Создано папок в wiki/: **19** (9 entity + comparisons + 6 niches + graph + _templates + wiki root)
- Создано файлов в raw/: **5** (README + 4 .gitkeep)
- Создано skill-файлов: **5** (4 новых + 1 `.new`)
- Создано файлов в agents/: **48** (12 × 4: system.md, strategies.md, scratchpad.md, niche/README.md)
- Создано symlinks: **24** (по манифесту agent → niches)
- Создано корневых файлов: **2** (MIGRATION.md, этот отчёт)

## Next steps (Phase 3)

1. **Руслан:** открыть `wiki/` как Obsidian vault, проверить рендеринг wikilinks и frontmatter.
2. **Руслан:** решить вопросы выше (особенно 1 и 2).
3. **Первый живой `/ingest`** — взять одну статью из `knowledge-base/ai-consulting/` и прогнать
   через новый skill. Убедиться, что index/log/edges обновляются.
4. После **3-5 успешных `/ingest`** — прогнать `/lint` и посмотреть отчёт.
5. После **10+ страниц в wiki/** — `/build-graph`, посмотреть на первые communities.
6. **Update CLAUDE.md** — добавить секцию "Wiki pipeline v2" с новыми skills.
7. **Phase 3 следующие фичи:**
   - Хук в `/close-day`, который пишет summary дня в `wiki/summaries/`.
   - Интеграция `inbox-processor` — после обработки inbox делать `/ingest` в wiki.
   - Миграция активных стратегий из `baseline.md` агентов в `strategies.md`.
