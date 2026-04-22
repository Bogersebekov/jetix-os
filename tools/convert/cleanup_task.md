# Cleanup Task — promo для Claude Code на сервере

## Как запустить

Открой Git Bash или Antigravity terminal.

```
ssh ruslan@100.99.156.28
```

На сервере:

```
tmux new -s cleanup
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

Когда Claude запустится — paste целиком промпт ниже:

---

## PROMPT (copy-paste целиком)

```
Задача: почистить raw/books-md/ от мусора. Быстрая операция (5-10 минут).

ВАЖНО: НЕ удаляй failed books — они есть в списке ниже, их re-OCR будем делать
отдельно. Также НЕ трогай большие книги.

## ПРАВИЛА УДАЛЕНИЯ

### 1. C-grade файлы с word_count < 1000 — УДАЛИТЬ

Это tiny blog pages / navigation artifacts. Примеры:
- philosophy/ Naval short posts (subscribe.md, on-humility.md, etc.)
- meta/ contact.md, careers.md, security.md, data-processing-addendum.md
- cybernetics/ indexphp.md, reviewsphp.md, translationsphp.md

Логика: прочитать YAML frontmatter, check quality_grade=C + word_count<1000,
delete.

### 2. НЕ ТРОГАТЬ — failed books (будем re-OCR отдельно)

Этот список НЕ УДАЛЯТЬ даже если они C-grade + 0 слов:
- raw/books-md/cybernetics/beer-brain-of-the-firm-1972.md
- raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md
- raw/books-md/mgmt/grove-only-paranoid-survive-1996.md
- raw/books-md/mgmt/drucker-effective-executive-2006.md
- raw/books-md/pdm/cagan-inspired-2ed-2017.md
- raw/books-md/philosophy-science/popper-conjectures-and-refutations-1963.md
- raw/books-md/engineering-foundations/vincenti-what-engineers-know-1990.md
- raw/books-md/clean-code/brooks-mythical-man-month-1995.md

Все эти — книги которые failed OCR. Оставь как есть.

### 3. Дубликаты scraped chapters — УДАЛИТЬ

Серверу wget скачал некоторые книги дважды — как PDF и как scraped HTML
(chapter by chapter). Удаляй chapter-dubli, оставляй single PDF version.

Dubli to delete:
- raw/books-md/cybernetics/ch1-a.md, ch1-b.md, ..., ch25-*.md (все chN-X.md files)
  → оставляем только kelly-out-of-control-1994.md (содержит полную книгу)
- raw/books-md/cybernetics/chbibal.md, chbibmz.md, chbibst.md (bibliographies)
- raw/books-md/pm/ NN-chapter-MM.md files (scraped Shape Up chapters)
  → оставляем singer-shape-up-basecamp-2019.md (PDF version)
- raw/books-md/unix/ chapter files (Raymond scraped chapters)
  → оставляем raymond-art-of-unix-programming-2003.md если есть

Проверяй паттерны: ch1-a / ch2-b / 01-chapter / 02-chapter / chapter_N и т.д.
Безопасно — если filename match pattern + в той же подпапке есть соответствующая
книга с нормальным title, удаляй chapter-files.

### 4. Очевидный мусор — УДАЛИТЬ

Также удали если встретишь:
- *.php.md files (wget artifacts)
- index.md / index.html.md / contact.md / careers.md / subscribe.md / rss.md
- Любые файлы title'ом типа "404", "sitemap", "feed", "tag"
- Naval blog artifacts: 'new-blog-and-feed-address.md', 'stories.md',
  'interview-on-entrepreneurship-up-at-gigaom-tv.md'

### 5. Явные duplicates

Если видишь два файла с одинаковым word_count и title в одной папке — удали
меньший / более broken.

Пример: philosophy/how-to-get-rich.md (44197w) и philosophy/rich.md (44197w)
это one and the same Naval "How to Get Rich" — удали короткий (rich.md менее
evocative name).

## WORKFLOW

1. Scan raw/books-md/ recursively
2. Для каждого MD: read frontmatter (python-frontmatter installed уже)
3. Apply rules 1-5
4. Collect delete list, показать preview (first 30 files), confirm with yourself,
   execute delete
5. После delete: regenerate INDEX.md (python tools/convert/convert_all.py --step index)
6. Git commit + push:
   git add raw/books-md/
   git commit -m "[raw] cleanup — removed trash blog pages + chapter duplicates (kept failed books for re-OCR)"
   git push origin claude/jolly-margulis-915d34

## SAFETY

- Before deleting — сохрани список deleted files в raw/books-md/_DELETED-LOG.md
  (один список с path + size + reason per file)
- Этот log commit также
- Если сомневаешься про конкретный файл (is it junk or valuable?) — НЕ удаляй,
  flag в DELETED-LOG как "unclear", но keep

## Отчёт

После завершения:
- Сколько всего удалено
- Per-subcategory breakdown (до / после)
- Какие files flagged as "unclear" (kept but suspicious)
- Новый total count
- INDEX.md regenerated?

Используй extended thinking если нужно для judgment calls (например unclear
files). Иначе — быстрое выполнение.

Поехали.
```

---

## Что произойдёт

Claude Code на сервере:
1. Прочитает `raw/books-md/` весь
2. Применит правила удаления
3. Удалит ~200-220 junk files (philosophy tiny posts / meta navigation / chapter dupes)
4. Сохранит список удалённого в `raw/books-md/_DELETED-LOG.md`
5. Перегенерит INDEX.md
6. Git commit + push

## После завершения (у тебя локально)

```
cd C:\Users\49152\Desktop\jetix-os
git pull origin claude/jolly-margulis-915d34
cat raw/books-md/_DELETED-LOG.md | head -30
cat raw/books-md/INDEX.md | head -50
find raw/books-md -name "*.md" ! -name "INDEX.md" ! -name "_*" | wc -l
```

Увидишь что осталось ~700-800 файлов (vs 1016 до чистки).

## Потом — re-OCR для 7 failed books

Это будет отдельная задача. Сейчас просто чистим. После cleanup ты посмотришь на resulting INDEX, решим что дальше.

---

**Делай:** SSH на сервер → tmux → claude → paste промпт. Detach потом (`Ctrl+B D`). Через 5-10 минут вернись посмотреть что удалилось.
