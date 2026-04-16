---
name: consolidate
description: "Найти дубликаты в wiki/ и предложить merge. После confirm — объединить, обновить ссылки, залогировать."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill: /consolidate

## Описание

Объединение дубликатов в wiki/. Не мерджит автоматически — всегда confirm от пользователя.

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
  A: wiki/concepts/value-based-pricing.md (4 sources, 120 lines)
  B: wiki/concepts/value-pricing.md (2 sources, 80 lines)

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
   - Обновить `wiki/graph/edges.jsonl`: где `from: B` → `from: A`, где `to: B` → `to: A`
     (дедуп идентичных edges).
   - Обновить `wiki/index.md`: убрать строку B, обновить A.

4. Удалить B:
   - Перед удалением — создать копию в `wiki/_archive/YYYY-MM-DD-B.md` (с комментом "merged into A").
   - Только после успешного копирования.

5. Залогировать в `wiki/log.md` (сверху):

   ```
   ## [YYYY-MM-DD] consolidate | merge | A ← B
   A: wiki/concepts/value-based-pricing.md
   B (archived): wiki/_archive/YYYY-MM-DD-value-pricing.md
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
