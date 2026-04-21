---
id: voice-memos-step-2-auto-ingest
title: Step 2 — Auto-Ingest Voice-Memos в Wiki
date: 2026-04-21
type: prompt
status: ready
depends_on: Step 1 (pipeline прогон завершён)
---

# Step 2 — Auto-Ingest ~117 Voice-Memos в Wiki

## Контекст

После Шага 1 все ~117 voice-memos транскрибированы (в `raw/transcripts/`), extract.py прогнан (structured items), filter.py сделал дедуп и review report готов.

Теперь нужно автоматически разложить содержимое по wiki/ — без ручного distribute, но и без тупого копирования всего подряд. Нужна интеллигентная классификация с preservation контекста.

Notion page для контекста: https://www.notion.so/3492496333bf813fbbbec5deabcc61a4

## Задача

Провести intelligent auto-ingest всех transcripts + extracted items в wiki/ через существующий /ingest workflow + агентную классификацию.

## Input

- `raw/transcripts/*.txt` — ~117 файлов
- `raw/extracted/*.jsonl` или аналог — structured items из extract.py
- `reports/review_2026-04-21.md` (или свежий) — review report с дедупликацией
- `wiki/index.md` — существующий каталог (для avoid duplicates)
- `wiki/_templates/` — шаблоны entity types

## Алгоритм

### Фаза 1 — Prep

1. Прочитать `reports/review_2026-04-21.md` (или самый свежий) — там уже de-duplicated items
2. Прочитать `wiki/index.md` — список существующих страниц чтобы избежать duplicates
3. Прочитать `wiki/_templates/` чтобы знать формат каждого типа entity

### Фаза 2 — Классификация через subagent batch

**Батчи по 10-15 transcripts.** Для каждого батча — spawn subagent через Task tool:

```
Task: Классифицировать items из batch transcripts для wiki ingest.

Input:
- Transcripts: [paths]
- Existing wiki pages: [index excerpt]

Для каждого content item в batch classifier должен определить:

1. Entity type (из 9):
   - concepts/ — концепции, термины, frameworks
   - ideas/ — идеи, proposals, hypotheses (формат "что если...")
   - entities/ — люди, компании, проекты
   - sources/ — источники (книги, статьи, видео упомянутые)
   - topics/ — большие темы (собирают концепции)
   - foundations/ — философия, миссия, values
   - experiments/ — эксперименты (гипотеза + тест)
   - claims/ — утверждения с evidence
   - summaries/ — саммари

2. Действие:
   - CREATE_NEW — если в wiki нет похожей страницы → создать новую
   - UPDATE_EXISTING — если есть похожая → добавить новые инсайты + provenance
   - SKIP — если уже полностью покрыто или trivial

3. Target path: `wiki/{type}/{slug}.md`

4. Content для wiki страницы:
   - YAML frontmatter (id, title, date, type, sources: [transcript_path], tags, related)
   - Prose body с direct quotes из transcript где возможно
   - Provenance: [src:audio_XXX@DATE_TIME.txt:line_XX]

Output: JSONL со строками {transcript: path, item_id: X, action: ..., target: ..., content_preview: ...}
```

### Фаза 3 — Применение изменений

После классификации всех батчей:

1. **CREATE_NEW** — создать файлы в `wiki/{type}/`
   - Проверить что slug не конфликтует (grep по index.md)
   - Использовать template из `wiki/_templates/`
   - YAML frontmatter обязателен
2. **UPDATE_EXISTING** — добавить новые инсайты + новые sources в frontmatter
   - НЕ переписывать существующий контент
   - Append-only в prose body с меткой [2026-04-21 from audio_XXX]
3. **SKIP** — пропустить
4. Обновить `wiki/index.md` — добавить новые страницы
5. Обновить `wiki/log.md` — append-only запись о batch ingest (новое СВЕРХУ)
6. Обновить `wiki/graph/edges.jsonl` — typed edges для новых связей

### Фаза 4 — Verification

1. `tools/lint-frontmatter.py` (или аналог) — проверить все новые страницы
2. Grep для orphans (страницы без incoming edges)
3. Подсчитать статистику: X created / Y updated / Z skipped
4. Убедиться что `wiki/index.md` не сломан

### Фаза 5 — Commit

```bash
git add wiki/
git commit -m "[wiki] Auto-ingest ~117 voice-memos (495-505 + backlog) для Genesis Document"
git push origin claude/jolly-margulis-915d34
```

## Deliverable (stdout report)

```
# Auto-Ingest Report — 2026-04-21

## Статистика
- Transcripts processed: N
- Items classified: N
- Created: X pages (breakdown by type)
- Updated: Y pages
- Skipped: Z items
- New edges: N
- Total wiki growth: before → after page count

## По entity types
- concepts/: +X новых / Y обновлённых
- ideas/: +X / Y
- entities/: +X / Y
- (остальные типы)

## Topics density (top 10 most-touched topics)
- Topic name — N transcripts mentioning

## Commit hash + push confirmation

## Warnings / issues
- Любые дубликаты которые classifier не смог решить автоматом
- Любые orphan pages после ingest
- Файлы где unclear type (flagged for manual review)
```

## Ограничения

- **НЕ** запускать `tools/distribute.py` — он архивирован.
- **НЕ** редактировать transcripts / extracted — они immutable.
- **НЕ** создавать wiki страницу если item trivial (односложная задача, timestamp-only mention) — SKIP.
- **НЕ** переводить русский контент Ruslan'а на английский — preserve voice.
- **Provenance обязателен** — каждая новая / обновлённая wiki страница должна иметь source reference на конкретный transcript.
- **ETA:** 1-3 часа в зависимости от количества unique items.

## Если что-то идёт не так

- Если classifier subagent на какой-то батч даёт <50% confident results → stop, report проблему, не пытайся workaround'ом.
- Если wiki/index.md становится слишком большим (>500 строк) — flag для consolidation run.
- Если много UPDATE_EXISTING конфликтов — stop, запросить guidance.
