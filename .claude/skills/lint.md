---
name: lint
description: "Health check wiki/: 7 проверок (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift). Пишет отчёт."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill: /lint

## Описание

Проверка целостности wiki/. Находит проблемы, не чинит автоматически — только отчёт.

## Триггер

`/lint` — без аргументов. Или `/lint <niche>` — для одного niche.

## Проверки

### 1. Orphan pages

Страницы, на которые никто не ссылается (нет входящих `[[links]]` и нет в `wiki/graph/edges.jsonl`).

**Grep:** найти упоминания `[[slug]]` или `[slug](path)` в других файлах.

**Исключения:** `index.md`, `log.md`, `overview.md`, `_templates/*`, `niches/*/README.md`,
страницы с `tags: [#status/standalone]`.

### 2. Stale claims

`wiki/claims/*.md` где `confidence: low` И `updated:` старше 60 дней от сегодня.

### 3. Broken wikilinks

`[[path]]` или `[text](relative-path)` указывающие на несуществующий файл.

### 4. Missing frontmatter

Markdown в `wiki/**/*.md` без обязательных полей:
`title`, `type`, `niche`, `created`, `updated`, `pipeline`.

Исключения: `index.md`, `log.md`, `.gitignore`, `_templates/*` (у них свой frontmatter).

### 5. Contradictions

Для каждой пары (A, B), соединённой edge `contradicts` — проверить, что:
- Обе страницы существуют.
- В обеих упомянута противоположная в секции `## Связи`.

### 6. Missing cross-refs

Страница A упомянута в 3+ других страницах, но её нет в `related:` frontmatter тех страниц.

### 7. Index drift

- Файл есть в wiki/, но его нет в `index.md` (в соответствующей секции).
- Наоборот: в index.md есть строка, но файла нет.

## Выход

`wiki/_lint-report-YYYY-MM-DD.md`:

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
- wiki/concepts/foo.md → [[bar]] (нет такого файла)

...
```

## Правила

- Не удалять / не править другие файлы.
- Только отчёт. Действия — вручную через `/consolidate` или правки.
- Приоритеты: broken links и missing frontmatter — высокий; orphans / stale — средний.
- Добавить запись в `wiki/log.md`:
  `## [YYYY-MM-DD] lint | report | issues: N`
