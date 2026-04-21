---
id: voice-memos-processing-2026-04-21-readme
title: Voice-Memos Processing Prompts — Master Index
date: 2026-04-21
type: prompt-index
status: ready
---

# Voice-Memos Processing — Master Index

## Контекст

Ruslan добавил 11 новых voice-memos (audio_495...505, 18-20 апреля 2026) к существующим ~106, итого ~117 файлов в `raw/voice-memos/`.

Цель: обработать всё, получить 3 сводных артефакта (mini-wikipedia / year plan / strategic ideas), свести в digest для ревью Ruslan'а, чтобы дальше питать Genesis Document (SYNTHESIS-GOAL bundle) для Jetix Architecture v3.

**Notion page:** https://www.notion.so/3492496333bf813fbbbec5deabcc61a4

## Критическое правило (НЕ НАРУШАТЬ)

**Шаги 3, 4, 5 (mini-wikipedia / year plan / strategic ideas) извлекаются ВСЕ НАПРЯМУЮ ИЗ RAW DATA** (транскрипты + extracted items), НЕ из обработанной mini-wikipedia. Иначе теряется контекст.

Реализация: каждый шаг делегируется отдельному subagent с full context всех ~117 транскриптов.

## Порядок запуска

| Шаг | Prompt | Depends on | Parallel? |
|-----|--------|------------|-----------|
| 1 | (уже выдан отдельно) pipeline прогон | raw OGG | нет |
| 2 | [01-auto-ingest-wiki.md](01-auto-ingest-wiki.md) | Шаг 1 | нет |
| 3 | [02-mini-wikipedia.md](02-mini-wikipedia.md) | Шаг 1 (transcripts ready) | ✅ может параллельно с 4, 5 |
| 4 | [03-year-plan.md](03-year-plan.md) | Шаг 1 (transcripts ready) | ✅ может параллельно с 3, 5 |
| 5 | [04-strategic-ideas.md](04-strategic-ideas.md) | Шаг 1 (transcripts ready) | ✅ может параллельно с 3, 4 |
| 6 | [05-digest-merge.md](05-digest-merge.md) | Шаги 3, 4, 5 | нет (финальное merge) |

**Рекомендация по исполнению:** Шаги 3, 4, 5 запустить параллельно через Task tool (три subagent в одном message) — сэкономит время и каждый subagent получит свой clean context.

## Input (единый источник для всех шагов)

- `raw/voice-memos/` — ~117 OGG файлов
- `raw/transcripts/` — ~117 .txt транскриптов (после Шага 1)
- `raw/extracted/` или аналог — structured items (после Шага 1)
- `reports/review_*.md` — review reports (как reference, НЕ primary)

## Output (итого)

После всех шагов должны появиться:

- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md`
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md`
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md`
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md` ← финальный для Ruslan review
- Обновлённый `wiki/` с новыми concepts / ideas / entities / foundations страницами

## Общие ограничения (применимы ко всем шагам)

- **НЕ** редактировать существующие файлы transcripts / extracted (они immutable raw).
- **НЕ** запускать `tools/distribute.py` — он архивирован сознательно (Claude-выводы не должны попадать в KB без ревью Ruslan'а). Wiki ingest из Шага 2 делается по другому workflow через /ingest skill.
- **НЕ** писать интерпретации от себя — только то что реально сказано в транскриптах. Сохранять прямые цитаты Ruslan voice где возможно.
- **Commit + push** в конце каждого шага.
- **Branch:** `claude/jolly-margulis-915d34` (или соответствующая working branch).
- **Все deliverables имеют YAML frontmatter** (id / title / date / type / sources).
- **Язык контента:** русский (voice Ruslan) с английскими tags/structure.
