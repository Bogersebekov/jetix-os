---
name: ingest
description: "Поднять источник из raw/ (или по URL) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. The default
> root is `swarm/wiki/` (v3) per D7 `default_root: wiki_root_v3`. To
> target v2, set `WIKI_ROOT=wiki` env var or pass `--wiki-root=v2`.
> Cross-tree edges (v3→v2 only) land in
> `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /ingest

⚠️ ВНИМАНИЕ: есть старая версия `ingest.md` (raw → ingested KB). Этот файл — новая версия
под wiki-архитектуру (Karpathy LLM Wiki + OmegaWiki). После ручного ревью Русланом —
старую удалить, эту переименовать в `ingest.md`.

## Описание

Превратить сырой источник (файл в `raw/` или URL) в связанный набор страниц `${WIKI_ROOT}/`.

## Триггер

- `/ingest <path>` — путь к файлу в `raw/` (md, txt, pdf-резюме)
- `/ingest <url>` — сначала скачать через WebFetch, положить в `raw/web/YYYY-MM-DD-slug.md`

## Алгоритм

### 1. Нормализовать источник

**Если URL:**
- WebFetch → получить содержимое и заголовок.
- Определить дату: сегодня в формате `YYYY-MM-DD`.
- Slug из заголовка: lowercase, `-`, ASCII, max 60.
- Сохранить в `raw/web/YYYY-MM-DD-slug.md` с frontmatter:

  ```yaml
  ---
  title: "..."
  source: "<url>"
  captured: YYYY-MM-DD
  pipeline: raw
  ---
  ```

**Если путь в `raw/`:** прочитать напрямую. Проверить frontmatter. Если нет — добавить минимальный.

### 2. Определить niche

Прочитать содержимое. Выбрать одну из: `personal`, `business`, `sales`, `life`, `tech`, `meta`. (6 niches per CLAUDE.md L70 lock; `global` content lives в Layer 7 `${WIKI_ROOT}/global/` per D1.)
Если сомнения — спросить пользователя.

### 3. Извлечь структуру

Выделить из источника 10-15 ключевых элементов по типам:

- **concepts** — фреймворки, идеи, паттерны, модели
- **entities** — конкретные люди, компании, продукты, места
- **claims** — проверяемые утверждения
- **ideas** — что можно сделать
- **foundations** — базовые принципы (редко)

### 4. Создать / обновить wiki-страницы

Для каждого элемента:

1. Построить путь: `${WIKI_ROOT}/{type}/{slug}.md`.
2. Если файл существует → читать, добавлять секции (не перезаписывать), обновлять `updated:`,
   добавлять новый источник в `sources:`.
3. Если нет → взять шаблон из `${WIKI_ROOT}/_templates/{type}.md`, заполнить.
4. Frontmatter: `niche`, `sources: [raw/.../file]`, `related: [...]`, `confidence`, `pipeline: ingested`.
5. В теле — использовать `[[wikilinks]]` на другие страницы wiki.

### 5. Создать карточку источника

`${WIKI_ROOT}/sources/YYYY-MM-DD-slug.md` по шаблону `source.md`:

- TL;DR (2 предложения)
- Summary (3-10 предложений)
- 2-5 ключевых цитат
- Списки: какие concepts/entities/claims/ideas извлечены → wikilinks

### 6. Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl` (v3 intra-tree)

Для v3→v2 ссылок — `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` (D3 §3.2.12 + T1).

Append-only. Один JSON на строку. **12 типов per D3 §3.2** (9 intra-layer + 3 cross-layer):
`extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of, alpha-ref, layer-ref, cross-tree-ref`.
(`addresses_gap` dropped per critic-gate1 H4 of the wiki-v3 spec.)

Пример:

```json
{"from": "concepts/value-based-pricing.md", "to": "entities/vladislav.md", "type": "derived_from", "created": "2026-04-16", "confidence": "high"}
```

### 7. Обновить `${WIKI_ROOT}/index.md`

Для каждой новой / существенно изменённой страницы:

```
- [Title](path) — one-line summary [niche] [sources: N]
```

Добавить в соответствующую секцию (Concepts, Entities, …), алфавитно.

### 8. Добавить в `${WIKI_ROOT}/log.md` (сверху)

```
## [YYYY-MM-DD] ingest | <source-slug>
Создано: N страниц. Обновлено: M. Edges: K.
Niche: <niche>.
Файлы: [[sources/...]], [[concepts/...]], ...
```

### 9. Обновить niche

В `${WIKI_ROOT}/niches/{niche}/README.md` в секцию `## Pages` добавить линк на новые страницы. (Niche enum: 6 values per CLAUDE.md L70 lock — `personal/business/sales/life/tech/meta`; `global` removed per critic-gate1 S3.)

### 10. Обновить источник

В frontmatter исходного файла: `pipeline: ingested`, добавить `wiki_page: sources/...`.

## Правила

- Не перезаписывать чужие правки. При конфликте — создать `.new` версию, сообщить.
- Один `/ingest` = один источник. Несколько — отдельными вызовами.
- Если источник большой — не пытаться вместить всё. Лучше несколько `concept`-страниц.
- Цитаты из источника — обязательно с атрибуцией.

## Выход

Короткий отчёт в чат:

```
✅ Ingested: <slug>
  Niche: ...
  Created: N pages (concepts:..., entities:..., claims:...)
  Updated: M existing pages
  Edges: K new
  Source card: sources/YYYY-MM-DD-slug.md
```
