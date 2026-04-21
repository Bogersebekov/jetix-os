---
id: unprocessed-notes-inventory
title: Unprocessed Notes Inventory для Genesis Document
date: 2026-04-21
type: inventory-report
status: raw
pipeline: raw
related:
  - raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md
purpose: |
  Inventory unprocessed заметок (voice-notes / transcripts / reports / extracted)
  перед harvest для Genesis Document bundle (SYNTHESIS-GOAL, Шаг 1 Architecture v3).
---

# Unprocessed Notes Inventory — 2026-04-21

## Summary
- **Total unprocessed pipeline artifacts**: **320 files** (106 voice-memos + 106 transcripts + 106 extractions + 2 filtered batches + 2 review reports that were never distributed to wiki)
- **Oldest** (by recording date in filename): `audio_390@08-04-2026_02-45-30.ogg` — voice recorded **2026-04-08 02:45** (server mtime 2026-04-15)
- **Newest**: `audio_494@18-04-2026_16-08-52.ogg` — voice recorded **2026-04-18 16:08** (last mtime in pipeline 2026-04-18 16:47 for transcripts, 16:52 for extractions, 17:14 for review)
- **Recording span**: 11 days (2026-04-08 → 2026-04-18). **Gap since last recording: 3 days** (2026-04-18 to today 2026-04-21).
- **Total size**: **~82 MB** (voice-memos 80 MB OGG + transcripts 652 KB + extractions ~870 KB + reports 484 KB)

**Key fact**: voice-memos pipeline ран all the way through (transcribe → extract → filter → review), но final step **distribute → wiki/** was NOT executed. `tools/distribute.py` is archived (per CLAUDE.md) — so **nothing from these 106 memos has landed in wiki/sources/** (verified: 0 `audio_*` files в wiki/sources/). The entire harvest sits in `reports/review_2026-04-18.md` waiting for manual review.

---

## По локациям

### raw/voice-memos/
- **Count**: 106 (.ogg)
- **Size**: 80 MB
- **Date range**: 2026-04-08 02:45 → 2026-04-18 16:08 (by filename timestamp)
- **Mtime range**: 2026-04-15 20:28 (oldest batch fetched) → 2026-04-18 16:38 (latest)
- **Sample last 3**:
  - `audio_494@18-04-2026_16-08-52.ogg`
  - `audio_493@18-04-2026_15-59-17.ogg`
  - `audio_492@18-04-2026_15-56-54.ogg`

### raw/transcripts/
- **Count**: 106 (.txt, Whisper-large-v3 ru)
- **Size**: 652 KB
- **Mtime range**: 2026-04-15 20:36 → 2026-04-18 16:47
- **1:1 coverage**: каждый .ogg имеет .txt
- **Sample last 3**:
  - `audio_494@18-04-2026_16-08-52.txt`
  - `audio_493@18-04-2026_15-59-17.txt`
  - `audio_492@18-04-2026_15-56-54.txt`

### inbox/processed/extractions/
- **Count**: 106 (.json — structured items по tesponse из Claude Sonnet 4, model `claude-sonnet-4-20250514`)
- **Mtime range**: 2026-04-15 21:00 → 2026-04-18 16:52
- **1:1 coverage**: каждый transcript → JSON extraction
- **Sample**: `audio_494@18-04-2026_16-08-52.json` (items: tasks, visions, принципы, etc.)

### inbox/processed/filtered/
- **Count**: 2 batch files + 2 error logs
- **Files (full list)**:
  - `batch_2026-04-15.json` — aggregated/deduped batch (generated 2026-04-15, from early subset)
  - `batch_2026-04-18.json` — aggregated/deduped batch (generated 2026-04-18 17:13, **from all 106 extractions**, model `claude-opus-4-7`)
  - `raw_error_20260418_165656_199523.txt`
  - `raw_error_20260418_165841_072752.txt` [?] — two filter errors; не блокирующие, но warrant a look if re-running filter

### reports/review_*.md (NOT distributed — distribution архивирована)
- **Count**: 2
- **Full list**:
  - `review_2026-04-15.md` — 56 lines, 10 KB. Early voice-memos run. Mtime 2026-04-15 20:56.
  - `review_2026-04-18.md` — 507 lines, **156 KB. MAIN artifact. Distills 473 items from 106 voice-memos into: 131 tasks / 64 strategic hypotheses / 52 vision items / 51 principles / 45 insights / 34 personal observations / 31 decisions / 31 ideas / 24 project ideas / 7 open questions / 2 contacts / 1 resource.** Mtime 2026-04-18 17:14.
- **Status**: Neither distributed to wiki/ (tools/distribute.py архивирован per CLAUDE.md).

### reports/ (не-review файлы — session artifacts, NOT voice-memo distributions)
Каталогизированы для контекста (не считаются в "unprocessed voice-memo" count):
- `summary_2026-04-15.md` (89 KB) — voice-memos summary (same pipeline as review_2026-04-15) — **тоже вероятно недистрибьютирован** [?]
- Остальные (architecture-inventory, arch-migration, ideas-import*, notion-alpha*, stage-A-pipeline-closure, step3/step4-closure, system-design-inputs-collection, tech-doc-*, voice-memos-audit) — session artifacts (инфраструктурные отчёты, не контент для wiki).

### Other raw/ subdirs (для полноты, не unprocessed)
- `raw/notion-ideas/` — 259 файлов, все `2026-04-16-*.md`. **Уже ingest'нуты** в wiki/ideas/ (257 из 259 migrated — 2 dup merged).
- `raw/notion-pages/` — 11 Notion system pages, уже отражены в wiki/sources/ (α.3 ingest).
- `raw/external/ailev-FPF/` — 3 файла (ATTRIBUTION.md, FPF-Spec.md, Readme.md) — external research (Levenchuk FPF). Не personal notes, но уже отражены в `raw/research/levenchuk-fpf-research-2026-04-20/`.
- `raw/research/*.md` — 22 .md файла + поддиректории. Это **output research** (deep-research artifacts), не raw notes. Pipeline frontmatter нет. Не включены в "unprocessed".
- `raw/notion-daily-log-dump-2026-04-16.jsonl` + `raw/notion-daily-log-insights-2026-04-16.md` — Notion daily log (processed already в 2026-04-16 ingest).
- `raw/articles/`, `raw/books/`, `raw/meetings/`, `raw/web/`, `raw/imports/` — **все пустые**.
- `inbox/archive/`, `inbox/articles/`, `inbox/chats/`, `inbox/text/`, `inbox/voice/` — **все пустые**.
- `raw/transcripts/audio_2026-04-15_22-27-47.txt` — немного отличается от паттерна `audio_NNN@DD-MM-YYYY` — это одиночный hand-recorded файл из 2026-04-15, но всё равно в pipeline.

---

## Contextually relevant (community / winners / объединение / relationships)

### Pattern matches (grep с контекстом)

**"winner" (English)**: 0 файлов. Ruslan не использует английское слово в transcripts.

**"объедин*"** (unification/uniting): **11 transcripts**. Самые прямые совпадения Jetix-тематики:

- `audio_470@17-04-2026_04-44-55.txt`: «миллионы реально миллионы и так вот значит первое что **jetix может их там как-то объединить** ну или как то вот…»
- `audio_465@16-04-2026_08-02-50.txt`: «…у которых есть вот подход такой глубокий к изучению информации и **объединение их с другими такими людьми** обучение…»
- `audio_460@15-04-2026_16-59-49.txt`: «нужна помощь и так дальше их можно при помощи искусственного интеллекта как-то **объединить хоть немного**…»
- `audio_430@13-04-2026_04-55-09.txt`: «…ну и снова-таки даже людей вот это **объединять между собой**, это тоже вообще…»
- `audio_414@11-04-2026_02-08-27.txt`: «…потом их вместе **объединяешь**, там как-то на этой технологии читаешь…»
- Остальные 6 (audio_394, 401, 403, 408, 413, 422) — тот же куст идей про объединение людей/направлений/экспертизы.

**"авантюрист"**: 1 transcript — `audio_478@17-04-2026_06-26-38.txt` — эхо идеи `unite-adventurers-biggest-adventure` из wiki.

**"движени*"** (movement): 10 transcripts, но many are false positives (`продвижение` / `передвижение`). Clean matches:
- `audio_488@18-04-2026_04-27-18.txt`: «развитием сука компании…продвижением этой компании…» (развитие корпорации)
- `audio_480@17-04-2026_06-55-08.txt`: «продвижение развития этой корпорации вот jetix я как раз этим и собираемся…»

**"комьюнити/community"**: 0 direct matches (Ruslan использует русское «сообщество», «клан», «семья» — см. wiki harvest).

**"партн[её]р"**: ~10 transcripts. Наиболее сильные:
- `audio_397@09-04-2026_04-37-43.txt`: «…ты себе и клиентов, и **партнеров**, блядь, и тиммейта вытащишь как-то одновременно…» — AI-помощник как сборщик network.
- `audio_438@14-04-2026_11-09-17.txt`: «…делиться с моими **партнерами**, с моим кланом…» и «…одно с упором на **партнерство**, другое на продажу, я как бизнес-консультант…» — прямая community + sales dimension.
- `audio_457@15-04-2026_07-38-09.txt`: «…много-миллиардной компании прямо с тысячами **партнеров** умных сильных…» — vision scale.
- `audio_456@15-04-2026_04-06-44.txt`: «…людей из сообщества и клиентов и **партнеров**…» — social fabric для Jetix.
- `audio_425@13-04-2026_04-06-05.txt`: «…спарринг **партнер** адекватные…помощник, люди которые в тебя верят, спарринг партнер, учитель, команда, соревнования, конкуренты…» — целая "окружающая среда".

**Winners-adjacent Russian** (победител/успешн): 4 transcripts (audio_409, 426, 434, 476).

### Flag для Ruslan
Тема «Jetix объединяет winners» в transcripts присутствует **densely** — минимум **11+ voice-memos** содержат прямые формулировки про unification людей через Jetix (audio_394/401/403/408/413/414/422/430/460/465/470) плюс **~10 про партнёрство/сообщество/клан** (audio_397/425/438/456/457). **Это core community dimension отсутствует в текущем wiki harvest** (367 цитат из 281 wiki-файла), потому что ни одно из них ещё не дистрибьютировано.

---

## Top 5 newest unprocessed (by recording time)

### 1. `audio_494@18-04-2026_16-08-52.ogg` — 2026-04-18 16:08
**Preview (200 char)**: «так сразу на будущее вот приложение типа task rabbit почему тоже и балла будет начищена поднейшим в ближайшие года 3 4 просто люди приходят выполнять какую-то работу так еще получаются это 40 50 евро там…»
**Тема**: TaskRabbit будет заменён роботами; взять их методологию платформы для Jetix.

### 2. `audio_493@18-04-2026_15-59-17.ogg` — 2026-04-18 15:59
**Preview**: «И как раз за счет подхода к бизнесу, как к написанию кода и к качественному подходу написания кода, и в целом за счет качественного подхода к работе над бизнесом и так далее, у нас должно будет получиться следующим образом, что мы прям все лучшие практики…»
**Тема**: Бизнес-как-код, сразу на уровне best-practices настроить процессы; затем подтягивать людей под структуру; спидран до компании зарабатывающей $100K/мес.

### 3. `audio_492@18-04-2026_15-56-54.ogg` — 2026-04-18 15:56
**Preview**: «В стратегический документ записываем то, что у нас амбиции стать одной из worldwide компаний, как раз по производству софтов и по работе в целом с ключевыми предприятиями и людьми…»
**Тема**: Стратег-документ: worldwide company, средний бизнес → enterprise, $100K/мес sub-цель, автоматизировать всё что можно, до конца года.

### 4. `audio_491@18-04-2026_08-47-30.ogg` — 2026-04-18 08:47
**Preview**: «элементарно мы можем еду точно так же как и код записывать но и как-то сохранять разные варианты блюд и так далее и потом возможно ними делиться их шерить…»
**Тема**: Еда-как-код (versioning рецептов), авто-кухни, мегафабрики по цене электричества, white-label / франшиза модель как универсальный pattern.

### 5. `audio_490@18-04-2026_07-46-59.ogg` — 2026-04-18 07:46
**Preview**: «так тогда команда и в целом обработка каких-то запросов и идей она обязательно должна иметь короче человека и стадию когда они такие так что-то за хуйня нам надо в 10 раз больше или чё так или чё так блять неэффективно нам надо в 10 раз еще блять эффективней…»
**Тема**: Элон-Маск "10× approach", изучить его последние наработки и внедрить в workflow; one-million-one-person company через агентов.

---

## Rekomendations для Ruslan (сугубо observational, не предписание)

- **Единственный критический slug**: все 106 voice-memos (2026-04-08 → 2026-04-18) осели в `reports/review_2026-04-18.md` (156 KB, 473 структурированных items) и НЕ интегрированы в wiki/. Это источник №1 недостающего community/unification dimension для Genesis Document.
- **Gap since last recording: 3 days** (последняя запись 2026-04-18 16:08, сегодня 2026-04-21). Новые голосовые за 19/20/21 апреля ещё не записаны или не зафетчены в `raw/voice-memos/`.
- **Contextually relevant сейчас**: минимум **11 transcripts с прямыми формулировками про Jetix-объединение** + **10 про партнёрство/клан** + `review_2026-04-18.md` как aggregated distillation. Это ~20+ files worth harvesting selectively для community dimension.
- `batch_2026-04-18.json` (в `inbox/processed/filtered/`) — **уже готовый дедуплицированный массив** по всем 106 voice-memos (Opus 4.7 processed). Может быть efficient input для selective harvest вместо 106 raw transcripts.
- **2 raw_error_2026-04-18** в filtered/ [?] — два error-логи от filter.py; warrant a quick look, но не блокирующие.
- **summary_2026-04-15.md** (89 KB) [?] — potentially тоже unprocessed distribution artifact early batch; pair with review_2026-04-15.

---

*Read-only inventory. No files moved. No ingest performed. No commits.*
