---
name: ingest
description: "Поднять источник (6 source types: youtube/pdf/md/web/voice/stdin) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.1"}
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. The default
> root is `swarm/wiki/` (v3) per D7 `default_root: wiki_root_v3`. To
> target v2, set `WIKI_ROOT=wiki` env var or pass `--wiki-root=v2`.
> Cross-tree edges (v3->v2 only) land in
> `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
>
> **Client-isolation guard (UC-9 Phase-A).** If `WIKI_ROOT_CLIENT_ID`
> is set, resolve `${WIKI_ROOT}` from `clients:` stanza in
> wiki-roots.yaml; reject any resolved path outside that root before
> any write.

# Skill: /ingest

## Описание

Превратить сырой источник в связанный набор страниц `${WIKI_ROOT}/`.
Поддерживает 6 типов источников: YouTube URL, PDF, plain markdown,
web article, voice transcript, stdin note.

## Триггер

- `/ingest <path>` — путь к файлу в `raw/` (md, txt)
- `/ingest <url>` — YouTube URL или web article URL
- `/ingest <path>.pdf` — PDF файл (poppler pdftotext)
- `/ingest -` — stdin pipe (сохранить в raw/notes/)

## Алгоритм

### 0. Resolve ${WIKI_ROOT}

Прочитать `.claude/config/wiki-roots.yaml`. Применить resolution algorithm:
1. Если `WIKI_ROOT_CLIENT_ID` задан → `${WIKI_ROOT} := clients.<id>.root`; проверить что resolved path остаётся внутри этого root.
2. Иначе если `WIKI_ROOT` задан → использовать его.
3. Иначе → `swarm/wiki/`.

### 1. Нормализовать источник (source-type detection + routing)

**Source type 1 — YouTube URL** (matches `youtube\.com|youtu\.be`):
```
yt-dlp --write-auto-subs --skip-download --sub-format vtt \
        --output "raw/videos/%(upload_date)s-%(id)s.%(ext)s" \
        "<url>"
```
Запустить через Bash. VTT файл → `python3 tools/vtt-to-md.py raw/videos/<slug>.vtt` → `raw/videos/YYYY-MM-DD-<slug>-transcript.md`.
Frontmatter seed: `source_type: youtube`, `tier: tier-2`, `pipeline: raw`.
Если `yt-dlp` не установлен → escalate: `{trigger: tool-missing, tool: yt-dlp, hint: "pip install yt-dlp OR apt install yt-dlp"}`.

**Source type 2 — PDF** (input path ends with `.pdf`):
```
pdftotext -layout "<input.pdf>" "raw/papers/<slug>.md"
```
Запустить через Bash. Frontmatter: `tier: tier-1`, `source_type: pdf`, `pipeline: raw`.
Если `pdftotext` не установлен → escalate: `{trigger: tool-missing, tool: pdftotext, hint: "apt install poppler-utils"}`.

**Source type 3 — Plain markdown** (path in `raw/`; not PDF):
Прочитать напрямую. Проверить frontmatter. Если нет — добавить минимальный (`pipeline: raw`, `created: today`).

**Source type 4 — Web article URL** (URL not matching YouTube patterns):
WebFetch url → содержимое. Запустить `python3 tools/fetch-and-extract.py "<url>" "<raw-content>"` → clean article markdown → сохранить в `raw/web/YYYY-MM-DD-<slug>.md`.
Frontmatter: `source: <url>`, `captured: today`, `source_type: web`, `pipeline: raw`.
Если URL unreachable → escalate: `{trigger: peer-input-needed, reason: WebFetch-failed, url: "<url>"}`. НЕ писать пустой источник.

**Source type 5 — Voice transcript** (path в `raw/transcripts/`):
Принять путь к уже готовому транскрипту (upstream: `tools/transcribe.py`). Читать напрямую как plain markdown (source type 3). Frontmatter: `source_type: voice`, `tier: tier-2`.

**Source type 6 — Stdin (`-`):**
Прочитать stdin до EOF. Сохранить в `raw/notes/YYYY-MM-DD-HHMMSS-stdin.md` с frontmatter:
`pipeline: raw`, `source_type: note`, `confidence: low`, `tier: tier-3`.
Затем продолжить как plain markdown.

### 2. Определить niche

Прочитать содержимое. Выбрать одну из: `personal`, `business`, `sales`, `life`, `tech`, `meta`.
(6 niches per CLAUDE.md L70 lock; `global` content → Layer 7 `${WIKI_ROOT}/global/` per D1.)
При сомнении — спросить пользователя.

### 3. Извлечь структуру

Выделить из источника 10-15 ключевых элементов по типам:
- **concepts** — фреймворки, идеи, паттерны, модели
- **entities** — конкретные люди, компании, продукты, места
- **claims** — проверяемые утверждения
- **ideas** — что можно сделать
- **foundations** — базовые принципы (редко)

### 4. Dedup-check

Для каждого slug: проверить `${WIKI_ROOT}/concepts/<slug>.md`.
- Если файл существует → читать, добавлять секции (не перезаписывать), обновлять `updated:`, добавлять новый источник в `sources:`.
- Если slug коллизия при другом семантическом содержимом → вызвать `/consolidate` (никогда не перезаписывать).

### 5. Создать / обновить wiki-страницы

Для каждого элемента:
1. Путь: `${WIKI_ROOT}/{type}/{slug}.md`.
2. Взять шаблон из `${WIKI_ROOT}/_templates/{type}.md`, заполнить.
3. Frontmatter: `niche`, `sources: [raw/.../file]`, `related: [...]`, `confidence`, `pipeline: ingested`.
4. В теле — использовать `[[wikilinks]]` на другие страницы wiki.

### 6. Создать карточку источника

`${WIKI_ROOT}/sources/YYYY-MM-DD-<slug>.md` с frontmatter `pipeline: raw → ingested`:
- TL;DR (2 предложения)
- Summary (3-10 предложений)
- 2-5 ключевых цитат
- Списки: concepts/entities/claims/ideas → wikilinks

### 7. Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl`

12-enum per D3 §3.2: `extends | supports | refutes | derived_from | part_of | supersedes | related_to | contradicts | depends_on | illustrates | cites | cross-tree-ref`.
Append-only. Один JSON на строку. Целевой диапазон на инgest: 8-15 новых edges.
Для v3→v2 ссылок → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl`.

### 8. Обновить `${WIKI_ROOT}/index.md`

```
- [Title](path) — one-line summary [niche] [sources: N]
```

Добавить в алфавитном порядке в соответствующей секции.

### 9. Добавить в `${WIKI_ROOT}/log.md` (сверху)

```
## [YYYY-MM-DD] ingest | <source-slug>
Создано: N страниц. Обновлено: M. Edges: K.
Source type: <youtube|pdf|md|web|voice|stdin>.
Niche: <niche>.
Файлы: [[sources/...]], [[concepts/...]], ...
```

### 10. Обновить niche

В `${WIKI_ROOT}/niches/{niche}/README.md` добавить линк на новые страницы.

### 11. Обновить источник

В frontmatter исходного файла: `pipeline: ingested`, `wiki_page: sources/...`.

## Per-ingest success criteria (must hold for every ingest)

- 5-8 concept pages created under `${WIKI_ROOT}/concepts/<slug>.md` (no duplicates; dedup via fs-test).
- 8-15 new edges appended to `${WIKI_ROOT}/graph/edges.jsonl`.
- 1 new row in `${WIKI_ROOT}/log.md` (prepended, newest-on-top per CLAUDE.md convention).
- 1 new row in `${WIKI_ROOT}/index.md` (alphabetic sort preserved).
- Source page under `${WIKI_ROOT}/sources/<slug>.md` with frontmatter `pipeline: raw → ingested`.

## Failure modes

- **URL unreachable** → escalate `{trigger: peer-input-needed, reason: WebFetch-failed}`. Do NOT write empty source.
- **Duplicate slug** → invoke `/consolidate` inline to merge. Never overwrite.
- **OOM on long transcript** → chunk at 100K-token boundaries (Karpathy pattern). Emit partial concept pages; continue in next session.
- **yt-dlp absent** → escalate `{trigger: tool-missing, tool: yt-dlp}`.
- **pdftotext absent** → escalate `{trigger: tool-missing, tool: pdftotext}`.

## Правила

- Не перезаписывать чужие правки. При конфликте — `.new` версию + сообщение.
- Один `/ingest` = один источник.
- Цитаты из источника — обязательно с атрибуцией.

## Выход

```
OK: Ingested <slug>
  Source type: <youtube|pdf|md|web|voice|stdin>
  Niche: ...
  Created: N pages (concepts:..., entities:..., claims:...)
  Updated: M existing pages
  Edges: K new
  Source card: sources/YYYY-MM-DD-slug.md
```
