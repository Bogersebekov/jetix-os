# Brief: Voice-notes pipeline run + Workshop extraction + structured report

**Run instruction:** server CC, ветка `claude/jolly-margulis-915d34`, Opus 4.7 [1m], `--dangerously-skip-permissions`, **БЕЗ Plan Mode** (нужно реально выполнять). Слово `ultrathink` в тексте триггерит deeper reasoning на extraction quality.

---

## Кто я и кто ты

Я — Ruslan, основатель Jetix OS (Berlin). Phase 1 цель €50K Q2 2026. Solo founder + AI agents. Workshop concept LOCKED 30.04 («Jetix = мастерская для работы с информацией»).

Ты — server CC, обрабатываешь голосовые заметки + extract'ишь из них всё ценное под Workshop тему.

## Что есть на сейчас

**Voice-pipeline state:**
- `raw/voice-memos/` — 62 ogg-файла (15 старых audio_525-539 уже обработаны + 47 новых audio_540-586)
- `raw/transcripts/` — 15 транскриптов (audio_525-539), **новых ещё нет**
- `reports/review_2026-04-26.md` (compact 10.6KB) + `reports/review_2026-04-26-DEEP.md` (DEEP 115KB) — последний обработанный батч (24-26.04)
- `tools/run_pipeline.sh` (1.3KB orchestrator), `tools/transcribe.py` (Groq Whisper), `tools/extract.py`, `tools/filter.py`, `tools/review_report.py`

**Контекст для Workshop extraction:**
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — canonical concept (271 строка, 12 секций)
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` — companion business model (635 строк)
- `memory/MEMORY.md` + `memory/project_jetix_metaphor_dynamic.md` — Workshop frame в памяти

**Текстовые заметки (не через ogg):**
- `raw/voice-memos-text/community-addendum-2026-04-21.md` (18KB)
- `raw/voice-memos-text/holding-vision-2026-04-21.md` (42KB)

## Что от тебя нужно (4 deliverables)

### 1. Pipeline run на новом батче

```bash
bash tools/run_pipeline.sh
```

Что произойдёт:
- `transcribe.py` транскрибирует все ogg без транскрипта (audio_540-586) → `raw/transcripts/`
- `extract.py` пройдётся по новым transcripts → structured items
- `filter.py` сделает dedup + meta-analysis по **ВСЕМ** items (не только новым) — full re-filter
- `review_report.py` сгенерирует `reports/review_2026-05-01.md` (compact) + `reports/review_2026-05-01-DEEP.md` (DEEP) + копию `~/review-latest.md`

**Должно сработать самостоятельно**. Если что-то падает (API rate limit / token blow-up / invalid ogg) — flag explicitly с конкретным error, **не workaround'ируй молча**.

### 2. Workshop angle extraction — ⭐ главный артефакт

**Файл:** `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`

**Inputs:**
- Новый review_2026-05-01-DEEP.md (только что сгенерированный)
- `reports/review_2026-04-26-DEEP.md` (115KB предыдущий — оттуда тоже extract под Workshop)
- `raw/voice-memos-text/holding-vision-2026-04-21.md` + `community-addendum-2026-04-21.md` (текстовые заметки могут содержать Workshop-relevant)
- Workshop concept canonical для context'а — что уже LOCKED

**Структура:**

```markdown
# Workshop Voice-Extract — 2026-05-01

## §0 Что extract'ится
- Источники с датами / number ranges
- Coverage (сколько заметок, какой период)

## §1 Workshop-relevant ideas
Группировка по темам Workshop concept v2 (8 тем из плана дня):
- Adaptable станки — конкретные примеры
- Mapping 12 agents → workshop roles
- Phase transitions concrete triggers
- Visual/View principle deep
- Workshop НЕ-это (anti-patterns)
- Specialization in detail
- Workshop ↔ TRM connection
- Knowledge accumulation mechanism
- (другие темы если всплыли — open category)

Каждая идея в формате:
> «verbatim quote из заметки»
> [source: review_2026-05-01-DEEP.md:LXXX-YYY] OR [source: review_2026-04-26-DEEP.md:LXXX-YYY] OR [source: voice-memos-text/holding-vision-2026-04-21.md:LXXX]
> 
> **Связь с Workshop:** что эта идея даёт (1-2 предложения)
> **Куда:** Workshop concept v2 §X / wiki / concept-supplement / drop

## §2 Люди упомянутые (с relevance к Workshop)
Каждый человек:
- Имя / роль / краткий контекст
- В каких заметках упомянут (citations)
- Связь с Workshop: возможный партнёр / mentor / community-member / inspiration / deferred
- Существующая карточка в `crm/people/` — да/нет (поиск)
- Action: создать карточку / обновить / просто tracking

## §3 Прочее ценное (не Workshop, backlog)
Идеи которые не Workshop, но extract'ить жалко:
- Категория (TRM / Foundation / Tseren / projects / other)
- Quote + citation
- Куда (соответствующее место в repo / wiki / Notion)

## §4 Action items
Конкретные шаги по результату:
- В Workshop concept v2: какие секции добавить + какие quote'ы вшить
- В wiki/: какие концепции `/ingest` (с указанием topic/cluster)
- В crm/people/: какие новые карточки создать (с указанием identity inputs)
- В memory: что critical для будущих CC sessions
- В backlog (см. §3 deliverable 4): какие новые задачи/вопросы добавить
```

**Hard rule extraction:** **source-tag КАЖДОЙ идеи**. Без citation — не пиши. Лучше «не нашёл» чем confabulate. Provenance ≥0.95.

### 3. Structured report по новой пачке

**Файл:** `reports/review_2026-05-01-STRUCTURED.md`

**НЕ атомарный dump** items (это уже в `review_2026-05-01.md` compact + DEEP).

**Структура высокоуровневая:**

```markdown
# Structured Review — 2026-05-01 batch (audio_540-586)

## Executive summary (≤200 слов)
Что главное в этом батче. Не атомы — общая картина.

## Основные темы (3-7)
По убыванию частоты / важности. Каждая:
- Название темы
- Что говорилось (выжимка ≤100 слов)
- Citations на atom items в DEEP review
- Связь с текущими canonical docs (Workshop / TRM / Foundation)

## Вопросы (raised in this batch)
Open / unresolved questions из заметок:
- Q: вопрос
- Source: где задан (audio_NNN line range)
- Status: open / has-thought / answered (если в позднейшей заметке решён)

## Задачи (actionable items)
- T: задача
- Source
- Priority guess: P1/P2/P3 (на основе тональности заметки)
- Project: какой проект (quick-money / research / brand / community / ai-tools / life-os / engineering-thinking / bets)

## Решения (если в заметках было «решил X / отказался от Y»)
- D: решение
- Source
- Дата effective

## References
- Atomic dump: `reports/review_2026-05-01-DEEP.md`
- Compact: `reports/review_2026-05-01.md`
- Workshop extract: `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
```

### 4. Update backlog задач/вопросов

**Что найти:** existing backlog file. Кандидаты:
- `swarm/wiki/topics/backlog-*.md`
- `swarm/wiki/topics/open-questions-*.md`
- `swarm/wiki/topics/pending-tasks-*.md`
- `decisions/operational/stoppers-*.md`
- В Notion (Daily Log open questions sections)

**Если файл не найден** — flag explicitly, **не создавай новый** (Ruslan скажет где).

**Если найден:**
- Merge новых вопросов/задач из §3 deliverable 3 (этого batch'а)
- Mark deprecated/resolved если в новых заметках есть closure
- Update file in-place + log entry в `wiki/log.md` (append top)
- Source-tag: каждая новая запись с citation на audio_NNN

## Hard rules

1. **ultrathink** для extraction quality — не cargo-cult «прочитал, написал что попало»
2. **AI = scribe для strategic** — extract+structure, **НЕ диктуй** что Workshop ДОЛЖЕН быть. Только что Ruslan сказал в заметках.
3. **Source-tagging обязателен** — каждый клейм с pointer (file:Lstart-Lend). Confabulate = fail.
4. **Russian primary** prose, English code/configs, мат preserve в quotes из заметок.
5. **Beta-first** — достаточно-хороший v1, не perfectionism. Скорость > полировка.
6. **No solo-founder downgrade** — baseline enterprise + $1T trajectory.
7. **НЕ promote ideas в wiki / Workshop concept v2 / crm БЕЗ Ruslan ack** — extraction только, distribution отдельный шаг по Ruslan ack.
8. **No-confabulation** на missing — если backlog file не найден, flag explicitly. Если quote не точен — не парафразируй, дай file:line ref.
9. **Token budget** — если pipeline + extraction суммарно >700K main context — split на 2 sessions (pipeline run done, fresh session для extraction).

## Workflow

1. **Phase A — Pipeline run** (auto, не требует input)
   - `bash tools/run_pipeline.sh`
   - Verify outputs: `ls reports/review_2026-05-01*` + `ls raw/transcripts/audio_5{4,5,6,7,8}*`

2. **Phase B — 3 extraction артефакта параллельно**
   - Workshop extract → `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
   - Structured report → `reports/review_2026-05-01-STRUCTURED.md`
   - Backlog update → `<found backlog file>` + log entry
   - Each commit отдельно для clean history

3. **Phase C — Commit + push**
   ```
   [voice] pipeline run 2026-05-01: audio_540-586 transcripts + extract + filter + review
   [voice] workshop extract from 2026-04-26 + 2026-05-01 voice batches
   [voice] structured review 2026-05-01 — themes/questions/tasks/decisions
   [voice] backlog update from 2026-05-01 batch
   ```

4. **Phase D — STOP**
   - **НЕ** distribute extracted ideas в wiki / Workshop concept / crm
   - **НЕ** ingest /ingest без Ruslan ack
   - Жди Ruslan walkthrough на 3 артефакта → ack каждого → потом distribution отдельным шагом

## Inputs (pre-load)

- `CLAUDE.md` (auto)
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- `decisions/JETIX-TRM-MODEL-2026-04-30.md`
- `memory/MEMORY.md` + `memory/project_jetix_metaphor_dynamic.md`
- `reports/review_2026-04-26-DEEP.md` (115KB) — источник дополнительной выжимки
- `raw/voice-memos-text/holding-vision-2026-04-21.md`
- `raw/voice-memos-text/community-addendum-2026-04-21.md`
- (после Phase A) `reports/review_2026-05-01-DEEP.md` — главный input для extraction

## Out of scope (НЕ делай)

- Не переписывай Workshop concept v2 (Ruslan диктует отдельно, AI=scribe)
- Не promote / `/ingest` в wiki без ack
- Не trogai canonical docs LOCKED (Foundation Parts / Vision / Workshop / TRM)
- Не пиши Plan Mode pilot артефакты (pilot отложен)
- Не genericize в «best practices for voice-note processing» — это операционная задача, не методология

## Формат финального отчёта в чат

После Phase C — короткий summary (≤300 слов) в чат:
- Сколько заметок обработано (X transcripts new)
- Сколько Workshop-relevant ideas extracted
- Сколько людей упомянуто (с краткими names list)
- Какой backlog file нашёл / не нашёл
- Top 3 «aha-moments» из batch'а (что surprised тебя при extraction)
- Open questions Ruslan'у (если есть)

---

ready? Начинай Phase A. Когда pipeline закончит — Phase B параллельно. ultrathink на extraction quality.
