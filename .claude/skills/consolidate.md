---
name: consolidate
description: "Найти дубликаты в `${WIKI_ROOT}/` и предложить merge. После confirm — объединить, обновить ссылки, залогировать."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3→v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /consolidate

## Описание

Объединение дубликатов в `${WIKI_ROOT}/`. Не мерджит автоматически — всегда confirm от пользователя.

## Триггер

- `/consolidate` — пройтись по всей wiki.
- `/consolidate <type>` — только concepts / entities / claims / …
- `/consolidate <niche>` — только в одном niche.

## Алгоритм

### 1. Собрать кандидатов

Попарная проверка внутри одного type:

1. Одинаковые/похожие `title` (normalized: lowercase, без пробелов/дефисов).
2. Одинаковые/похожие slug (файловое имя).
3. 70%+ пересечения по словам в теле (грубая оценка: shared word count / min word count).
4. Одинаковая entity_kind (для entities) или topic (для claims).

### 2. Для каждой пары — diff

Показать пользователю:

```
CANDIDATE MERGE:
  A: ${WIKI_ROOT}/concepts/value-based-pricing.md (4 sources, 120 lines)
  B: ${WIKI_ROOT}/concepts/value-pricing.md (2 sources, 80 lines)

  Reason: 85% overlap, похожий title

  A unique: [...секции которых нет в B...]
  B unique: [...]
  Common: [...]

  Predлагаемый merge: A остаётся, B мержится в A.
  Ссылки на B будут обновлены на A: N файлов.

  [y] merge, [n] skip, [s] skip all similar
```

### 3. После confirm (`y`)

1. Объединить frontmatter:
   - `title` — более развёрнутый.
   - `sources` — union.
   - `related` — union.
   - `tags` — union.
   - `updated` — сегодня.
   - `confidence` — минимум из двух.

2. Объединить тело:
   - Сохранить все уникальные секции.
   - Общие — из A (первый).
   - Если в B есть больше цитат / деталей — перенести.

3. Обновить все внешние ссылки:
   - Grep `[[B]]`, `[[B.md]]`, `[path/to/B](...)` → заменить на путь к A.
   - Обновить `${WIKI_ROOT}/graph/edges.jsonl`: где `from: B` → `from: A`, где `to: B` → `to: A` (дедуп идентичных edges). **Также пройти по `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` для v3-сторонних ссылок на B.**
   - Обновить `${WIKI_ROOT}/index.md`: убрать строку B, обновить A.

4. Удалить B:
   - Перед удалением — создать копию в `${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md` (с комментом "merged into A"). **Per critic-gate2 SS3: this skill runs as expert (D6 §6.6.3 role_tool_matrix) and CANNOT mutate canonical α-2 `state` field — that requires brigadier per Q2/D6 §6.2. /consolidate writes the `_archive/` copy with the original frontmatter unchanged + appends an HTML comment `<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->`. The brigadier subsequently transitions α-2 `state: superseded` + `superseded_by: [[<A-path>]]` per D5 §5.3 movers (separate commit).**
   - Только после успешного копирования.

5. Залогировать в `${WIKI_ROOT}/log.md` (сверху):

   ```
   ## [YYYY-MM-DD] consolidate | merge | A ← B
   A: ${WIKI_ROOT}/concepts/value-based-pricing.md
   B (archived): ${WIKI_ROOT}/_archive/YYYY-MM-DD-value-pricing.md
   Updated refs in: N files
   ```

### 4. Skip / Skip all

- `n` — пропустить пару, продолжить.
- `s` — пропустить все похожие (по этому же type) в текущей сессии.

## Правила

- Никогда не мержить без `y`.
- Никогда не удалять без архива.
- Не трогать `_templates/`, `index.md`, `log.md`, `niches/*/README.md`.
- Если у страницы 10+ входящих ссылок — двойной confirm.
- Отчёт после сессии: сколько пар рассмотрено, сколько смерджено, сколько скипнуто.
