# Re-OCR 8 Failed Books — через Claude Code Vision (Max subscription)

**Цель:** 8 scanned PDF книг перечитать напрямую через Claude multimodal (vision),
заменить broken MD в `raw/books-md/`. Использует Max подписку (не API billing).

---

## План

### Точка А (сейчас)
- 8 books сконвертились в broken MD (0-800 слов, OCR fail на scanned)
- Oригиналы PDF лежат локально + в `inbox-reocr.tar.gz` (130 MB архив)
- Max subscription активна на сервере
- У нас на сервере Claude Code уже running cleanup task (deep cleanup meta/philosophy)

### Точка Б (цель)
- 8 books в `raw/books-md/` как clean MD (30-80K слов каждая, grade A)
- Commit + push готов
- Inbox-reocr удалён

### Стратегия
- Read PDF через Claude Code Read tool (встроенная multimodal visual OCR)
- Обрабатываем по **2 книги за batch** чтобы проверить rate limits + качество
- Большие книги (Grove 34MB, Vincenti 18MB, Beer 38MB) — chunked reading (5-10 страниц за раз)
- После каждой книги: commit. Если rate-limit — прерываемся, продолжаем когда reset.

---

## Шаги

### Шаг 1 — локально: upload архив на сервер

На Windows:
```bash
cd /c/Users/49152/Desktop/jetix-os
scp inbox-reocr.tar.gz ruslan@100.99.156.28:~/jetix-os/
```

### Шаг 2 — на сервере: распаковать + запустить Claude

```bash
ssh ruslan@100.99.156.28
tmux new -s reocr
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
tar xzf inbox-reocr.tar.gz
rm inbox-reocr.tar.gz
ls inbox-reocr/
```

Должны быть 6 папок:
- cybernetics/ (beer + wiener)
- mgmt/ (grove + drucker)
- pdm/ (cagan)
- philosophy-science/ (popper)
- engineering-foundations/ (vincenti)
- clean-code/ (brooks)

### Шаг 3 — Paste промпт в Claude Code

```bash
claude --dangerously-skip-permissions
```

Paste промпт из секции ниже.

### Шаг 4 — Detach + wait

`Ctrl+B` потом `D`. Claude работает в фоне 4-8 часов.

### Шаг 5 — Проверка локально

```bash
cd /c/Users/49152/Desktop/jetix-os
git pull origin claude/jolly-margulis-915d34
cat raw/books-md/INDEX.md | grep -iE "beer|wiener|grove|drucker|cagan inspired|popper conj|vincenti|brooks"
```

Увидишь обновлённые grade + word_count.

---

## PROMPT (copy-paste в Claude Code на сервере)

```
Задача: re-OCR 8 scanned PDF книг через твою native multimodal capability
(Read tool reads PDF pages visually). Replace broken MD in raw/books-md/.

### Контекст
- 8 PDFs лежат в ~/jetix-os/inbox-reocr/ (уже распакованы из tar.gz)
- Текущие MD versions в raw/books-md/<subcat>/<slug>.md — broken (0-800 words)
- Max subscription активна — используй как можешь. Если hit rate-limit — 
  save progress, commit, exit. Через 5 часов можешь продолжать.

### Test batch стратегия

НАЧИНАЙ С 2 КНИГ для validation:
1. brooks-mythical-man-month-1995.pdf (clean-code, 10MB) — short, faster
2. cagan-inspired-2ed-2017.pdf (pdm, 9MB) — medium, canonical PM content

Обработай эти 2 → commit + push → ОСТАНОВИСЬ.

После этого user посмотрит результат и решит continue ли оставшиеся 6.

### Workflow per book (repeat для каждой)

1. Open PDF в Read tool
2. Read в chunks по 10 страниц (pages: "1-10", затем "11-20", итд.)
3. Для каждого chunk:
   - Extract clean markdown text (preserve headings structure)
   - Skip page numbers / running headers
   - Preserve sections / subsections
   - Keep tables если есть
   - Math equations — сохраняй как можешь (inline LaTeX $$ если understand,
     иначе textual description)
4. Concatenate chunks в единый MD
5. Add YAML frontmatter:
   ```yaml
   ---
   title: <Real title from book>
   author: <Author name>
   year: <publication year>
   subcategory: <matches folder>
   expert: <from EXPERT_MAP в convert_all.py>
   priority: <from PRIORITY_MAP>
   acquired_date: "2026-04-22"
   converted_date: "2026-04-22"
   converted_via: "claude-vision-max"
   word_count: <count>
   quality_grade: "A"
   source_format: "scanned-pdf"
   tags: [<subcategory>, ...]
   ---
   ```
6. Save в raw/books-md/<subcat>/<slug>.md (overwrite broken version)
7. Commit immediately (чтобы не потерять prog при rate-limit):
   ```
   git add raw/books-md/<subcat>/<slug>.md
   git commit -m "[raw] re-OCR via Claude Vision: <title>"
   ```

### Rate limit handling

- Если получаешь rate limit error → completeи current chunk + commit → exit.
- Не продолжай после rate limit — let user decide continue.

### Quality check after each book

Короткий sanity check:
- Word count reasonable? (30K-200K для книги)
- Headings present (минимум 5)
- Text readable (sample 100 words — понятно о чём)

### После 2 test books

Commit + push + short report:
- Time taken per book
- Word count both books
- Quality grade self-assessment
- Any issues encountered
- Rate limit usage estimate

ОСТАНОВИСЬ. User review results + decide continue.

Поехали. Extended thinking где judgment нужен (math rendering / table structure
decisions). Остальное — bursty execution.
```

---

## ETA

- **Test batch (2 books):** 1-2 часа на сервере
- **Full (8 books):** 4-8 часов, возможно 2 session'а через rate limit reset
- **Твоё active time:** 5 минут (ssh + paste + detach)

## Rate limit концерн

Max 20× subscription = ~800-1000 messages/5 hours.

Книга ~300 страниц chunked по 10 = 30 reads + 30 writes = ~60 tool calls.

8 книг × 60 = 480 calls — **уложимся в одно 5-hour window** на Max 20×.

Но если у тебя Max 5× (на 4× меньше) — делим на 2 sessions, detach между ними.

---

## Мониторинг

Вернуться к tmux и посмотреть progress:
```bash
ssh ruslan@100.99.156.28
tmux a -t reocr
```

Если Claude hit rate limit — увидишь message. Exit tmux (`Ctrl+B D`), reconnect через 5 часов — `tmux a -t reocr` — снова Claude, дай "continue с той книги на которой остановился".
