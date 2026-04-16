---
type: overview
updated: 2026-04-16
---
# Overview — Jetix OS Wiki

База знаний Jetix OS по модели Karpathy LLM Wiki + OmegaWiki knowledge graph.

## Как устроено

```
raw/            — сырые источники (статьи, транскрипты, заметки)
 ↓ /ingest
wiki/           — обработанная, связанная база знаний
 ├─ concepts/   — концепции (фреймворки, идеи, паттерны)
 ├─ entities/   — сущности (люди, компании, продукты)
 ├─ sources/    — карточки источников
 ├─ topics/     — темы / кластеры
 ├─ ideas/      — гипотезы, что можно сделать
 ├─ experiments/— проверки гипотез
 ├─ claims/     — утверждения с аргументами за/против
 ├─ summaries/  — сводки по темам / периодам
 ├─ foundations/— базовые принципы
 ├─ comparisons/— результаты /ask (сохранённые ответы)
 ├─ niches/     — срезы по доменам (для агентов)
 └─ graph/      — edges.jsonl + communities + summaries
```

## Операции

- `/ingest <path | url>` — поднять источник из raw/ в wiki/
- `/ask <question>` — синтезировать ответ из wiki; сохранить в comparisons/
- `/lint` — проверки здоровья (orphans, stale, broken links, contradictions)
- `/consolidate` — объединить дубликаты
- `/build-graph` — пройти по edges, обновить communities + summaries

## Принципы

1. **Не стираем, накапливаем.** Raw — навсегда. Wiki растёт поверх.
2. **Каждая правка логируется** в `log.md` (дата + тип операции + затронутые файлы).
3. **Все связи в `[[wikilink]]`** — для Obsidian и для `/build-graph`.
4. **9 типов edge** в `graph/edges.jsonl`: extends, contradicts, supports, inspired_by,
   tested_by, invalidates, supersedes, addresses_gap, derived_from.
5. **Niches — это срезы**, не копии. Symlinks из `agents/<id>/niche/` в `wiki/niches/<name>/`.

## Niches

| Niche | Что туда кладётся |
|-------|-------------------|
| `personal` | персональные контакты, привычки, цели |
| `business` | Jetix, клиенты, pricing, offers |
| `sales` | ICP, outreach, возражения, CRM |
| `life` | тренировки, сон, питание, энергия |
| `tech` | инструменты, архитектуры, библиотеки |
| `meta` | система, агенты, собственные процессы |

## Pipeline статусы

`raw` → `ingested` → `ready` — в frontmatter каждой страницы поле `pipeline`.

## Obsidian

Откроется поверх `wiki/` как vault. Структура совместима: flat-каталоги, wikilinks, markdown.
`.obsidian/` появится автоматически — в git он частично игнорируется (см. `wiki/.gitignore`).
