---
name: lint
description: "Health check `${WIKI_ROOT}/` (default v3): 11 проверок per Q5 5-signal orchestration + структурные (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift, α-2/α-3 lifecycle, triple-channel cross-refs, Q8 Layer-9 lock, symlink integrity)."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3→v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /lint

## Описание

Проверка целостности `${WIKI_ROOT}/`. Находит проблемы, не чинит автоматически — только отчёт.

## Триггер

`/lint` — без аргументов. Или `/lint <niche>` — для одного niche.

## Проверки

### 1. Orphan pages

Страницы, на которые никто не ссылается (нет входящих `[[links]]` и нет в `${WIKI_ROOT}/graph/edges.jsonl`).

**Grep:** найти упоминания `[[slug]]` или `[slug](path)` в других файлах.

**Исключения:** `index.md`, `log.md`, `overview.md`, `_templates/*`, `niches/*/README.md`,
страницы с `tags: [#status/standalone]`.

### 2. Stale claims

`${WIKI_ROOT}/claims/*.md` где `confidence: low` И `updated:` старше 60 дней от сегодня. **Дополнительно: `${WIKI_ROOT}/foundations/*.md` где `last_reviewed:` старше 365 дней (Q5 §3 + D2 §2.3 foundations re-review).**

### 3. Broken wikilinks

`[[path]]` или `[text](relative-path)` указывающие на несуществующий файл.

### 4. Missing frontmatter

Markdown в `${WIKI_ROOT}/**/*.md` без обязательных полей per D2 §2.2 cross-layer:
`id, title, type, layer, niche, created, last_modified, pipeline, state, confidence, tier, produced_by, sources, related, topics, captured_by, captured_date`.

Исключения: `index.md`, `log.md`, `.gitignore`, `_templates/*` (у них свой frontmatter).

### 5. Contradictions

Для каждой пары (A, B), соединённой edge `contradicts` — проверить, что:
- Обе страницы существуют.
- В обеих упомянута противоположная в секции `## Связи`.

### 6. Missing cross-refs

Страница A упомянута в 3+ других страницах, но её нет в `related:` frontmatter тех страниц.

### 7. Index drift

- Файл есть в `${WIKI_ROOT}/`, но его нет в `index.md` (в соответствующей секции).
- Наоборот: в index.md есть строка, но файла нет.

### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)

Для страниц под `${WIKI_ROOT}/skills/` ИЛИ с `type: skill`:
flag pages with `state ∉ {candidate, learning, active, tombstoned}`
(α-3 4-state lock per D2 §2.4 Layer 8).

Для остальных страниц: flag pages with
`state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}`
(α-2 8-state set per D5 §5.3).

### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)

Каждый inline wikilink матчинг `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]`
(non-matching forms like `[[A]]` or `[[file.md]]` warned as legacy/unparseable,
not errored) MUST появляться в `related[]` AND produce one record in
`${WIKI_ROOT}/graph/edges.jsonl`.

### 10. Q8 Layer-9 lock (per D1 §1.6)

Flag the existence of any file under `${WIKI_ROOT}/insights/{candidates,promoted}/*.md`
(any leaf `.md` write outside `README.md`) when D1 §1.6 boilerplate is in
effect. Per Q8 `phase_a_lock: true`.

### 11. Symlink integrity (per D9 §9.7)

For each `.md` file in `.claude/skills/`:
- if file is a symlink:
  - EMIT "broken symlink" if target doesn't exist
  - EMIT "symlink target outside active/" if not `../../swarm/wiki/skills/active/`
  - EMIT "symlink basename mismatch" if target basename != file basename

## Выход

`${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md`:

```yaml
---
type: lint-report
date: YYYY-MM-DD
checks: 7
---
```

```markdown
# Lint Report — YYYY-MM-DD

## Summary
- Orphans: N
- Stale claims: N
- Broken links: N
- Missing frontmatter: N
- Contradictions issues: N
- Missing cross-refs: N
- Index drift: N (missing in index: X, dangling entries: Y)

## Details

### 1. Orphans
- [[...]] — последний апдейт YYYY-MM-DD
  Hint: добавить в related у ... или удалить

### 2. Stale claims
...

### 3. Broken links
- ${WIKI_ROOT}/concepts/foo.md → [[bar]] (нет такого файла)

...
```

## Правила

- Не удалять / не править другие файлы.
- Только отчёт. Действия — вручную через `/consolidate` или правки.
- Приоритеты: broken links и missing frontmatter — высокий; orphans / stale — средний.
- Добавить запись в `${WIKI_ROOT}/log.md`:
  `## [YYYY-MM-DD] lint | report | issues: N`
