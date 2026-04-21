---
id: voice-memos-step-3-mini-wikipedia
title: Step 3 — Mini-Wikipedia по ~117 Voice-Memos
date: 2026-04-21
type: prompt
status: ready
depends_on: Step 1 (transcripts ready)
parallel_with: Step 4 (year plan), Step 5 (strategic ideas)
---

# Step 3 — Mini-Wikipedia по ~117 Voice-Memos

## Контекст

После Шага 1 все ~117 voice-memos транскрибированы. Нужна мета-аналитика — "mini-wikipedia" которая показывает что именно Ruslan обсуждал за весь период, с какой частотой, какие концепции развились, как эволюционировало мышление.

**Это вход для Genesis Document (SYNTHESIS-GOAL bundle).**

Notion page: https://www.notion.so/3492496333bf813fbbbec5deabcc61a4

## Критическое правило

**Извлечение делается ПРЯМО ИЗ RAW TRANSCRIPTS**, не из extracted items и не из review report. Extracted items и review можно использовать как sanity check, но primary source = сами .txt транскрипты. Иначе теряется context (голос / нюансы / эволюция мысли).

## Задача

Построить структурированную mini-wikipedia по всем ~117 transcripts. НЕ суммаризация, а именно **мета-аналитика** с количественными метриками + качественными находками.

## Input

- `raw/transcripts/*.txt` — ~117 файлов (single source of truth)
- `raw/voice-memos/` — для mtime если нужно sorting по датам
- `wiki/index.md` — как reference чтобы помечать "уже в wiki" vs "новое"
- `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md` — как reference (367 цитат уже в harvest, не дублировать атрибуцию)

## Алгоритм

### Фаза 1 — Inventory + chunking

1. Список всех transcripts с их датами (из filename `audio_NNN@DD-MM-YYYY_HH-MM-SS.txt`)
2. Разбить на 6-10 chunks по ~12-20 transcripts каждый (chronologically grouped чтобы evolution видна)
3. Подсчитать базовую статистику:
   - Total transcripts: N
   - Date range: earliest — latest
   - Total words (Russian content)
   - Mean words per transcript

### Фаза 2 — Tagging через subagents (parallel batches)

Для каждого chunk — spawn subagent через Task tool:

```
Task: Извлечь ключевые темы, концепции, entities из batch transcripts.

Input: [transcript paths для этого chunk]

Для каждого transcript субагент должен найти:

1. THEMES (макро-темы) — list of themes with verbatim quote excerpt
   Example: {"theme": "методология как продукт", "quote_excerpt": "...", "transcript": "audio_XXX.txt"}

2. CONCEPTS (конкретные концепции / термины / frameworks) — с определением из голоса
   Example: {"concept": "Jetix Director", "definition_quote": "...", "transcript": "audio_XXX.txt"}

3. ENTITIES mentioned — люди / компании / продукты
   Example: {"entity": "Антон", "role": "ментор", "context_quote": "...", "transcript": "audio_XXX.txt"}

4. INTERESTING CONCEPTS — что-то новое / unusual / ещё не в wiki
   (проверить через grep в wiki/index.md)

5. THOUGHT EVOLUTION signals — где Ruslan меняет / развивает / противоречит себе
   Example: {"before": "...", "after": "...", "transcript": "audio_XXX.txt"}

Output: JSONL структурированный.
```

### Фаза 3 — Aggregation

После всех subagent runs собрать output:

1. **Theme frequency table:**
   - Count mentions per theme across all 117 transcripts
   - Top 30 themes by mention count
   - Для каждой темы — 2-3 representative quotes с transcript attribution

2. **Concept catalog:**
   - Уникальные концепции упомянутые
   - Для каждой — definition (из самых точных quotes)
   - Mention count + transcripts list
   - Mark "new vs wiki" (если НЕ найдено в existing wiki)

3. **Entity index:**
   - Все люди / компании / проекты упомянутые
   - Частота упоминания
   - Role / context

4. **Thought evolution:**
   - Где тема развивается во времени
   - Chronological timeline для top 5 эволюционирующих тем

5. **Co-occurrence matrix:**
   - Какие темы встречаются вместе (top pairs)
   - Это намёк на natural clusters

6. **New concepts (top 10-15):**
   - Концепции которых НЕ было в wiki harvest (367 цитат) и NOT в existing wiki pages
   - С direct quotes
   - Flag для manual review

### Фаза 4 — Output document

Создать `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md` со следующей структурой:

```markdown
---
id: voice-memos-mini-wikipedia
title: Mini-Wikipedia по ~117 Voice-Memos (meta-analysis)
date: 2026-04-21
type: meta-analysis
status: ready
sources:
  - raw/transcripts/ (~117 файлов)
purpose: |
  Meta-аналитика всех voice-memos для input в Genesis Document
  (SYNTHESIS-GOAL bundle, Architecture v3).
---

# Mini-Wikipedia по ~117 Voice-Memos

## 1. Meta-Stats
- Total transcripts: N
- Date range: YYYY-MM-DD — YYYY-MM-DD
- Total words: ~N
- Mean words/transcript: N
- Oldest theme cluster: ...
- Newest theme cluster: ...

## 2. Top 30 Themes (by mention count)

| # | Theme | Mentions | First seen | Last seen | Representative quote |
|---|-------|----------|------------|-----------|----------------------|
| 1 | ...   | 45       | YYYY-MM-DD | YYYY-MM-DD | "...[src:audio_XXX]" |
...

## 3. Concept Catalog

### 3.1 Concepts в existing wiki
(с дополнительными refinements из voice-memos)

### 3.2 NEW Concepts (не было в wiki)
- **Concept name** — definition (quote)
  - Mention count: N
  - Source transcripts: [...]
  - Proposed wiki placement: concepts/slug.md

## 4. Entity Index
(люди / компании / проекты)

| Entity | Role | Mentions | Key context |
|--------|------|----------|-------------|

## 5. Thought Evolution (top 5 эволюционирующих тем)

### 5.1 Theme: "[название]"
- Timeline:
  - [date]: stance #1 (quote)
  - [date]: stance #2 (quote)
  - [date]: current synthesis (quote)
- Observation: [как развитие произошло]

## 6. Co-occurrence (natural clusters)

Top theme-pair co-occurrences (2+ transcripts):
- "theme A" + "theme B" — N transcripts
- ...

Этот раздел — намёк на natural clustering, полезен для 7 dimensions.

## 7. Дайджест для Genesis Document

### Dimensions impact
Как эти voice-memos питают 7 dimensions Genesis:
- База (universal OS): [key contributions]
- Jetix-life: [key contributions]
- Jetix-company: [key contributions]
- Community: [key contributions] ← ожидается много
- Money path: [key contributions]
- Relationships: [key contributions] ← ожидается много
- Philosophy: [key contributions]

### Surprises / tensions
- Что неожиданного нашлось
- Где voice-memos противоречат existing wiki
- Где усиливают

## 8. Provenance Index

Full list: transcripts → themes mapping
(compact table)
```

### Фаза 5 — Commit

```bash
git add raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md
git commit -m "[research] Mini-wikipedia по ~117 voice-memos для Genesis Document"
git push origin claude/jolly-margulis-915d34
```

## Ограничения

- **Primary source = .txt transcripts**. Не читать extracted items как primary.
- **Preserve Ruslan voice** — direct quotes с attribution.
- **НЕ интерпретировать** — только факты (theme mentioned N times) + quotes.
- **НЕ дублировать wiki harvest** — если тема уже в harvest с N цитатами, упомянуть это ("тема А также в harvest") и focus на новые voice-memo quotes.
- **Количественные метрики честные** — если считаешь mentions, используй consistent definition (e.g., "mention" = тема явно обсуждается в абзаце).
- **ETA:** 2-4 часа.

## Deliverable (stdout summary)

```
# Mini-Wikipedia Generation Complete

- File: raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md
- Size: X lines / Y KB
- Transcripts analyzed: N
- Themes identified: N
- Concepts catalogued: N (X new vs wiki)
- Entities indexed: N
- Thought evolution chains: N
- Top co-occurrence pairs: N
- Commit hash: abc1234
```
