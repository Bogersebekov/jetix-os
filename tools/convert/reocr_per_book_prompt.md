# Per-Book Re-OCR Prompt (Claude Vision via Max)

**Контекст:** обрабатываем по **одной книге за раз** через Claude Vision.
User вручную кладёт "fresh" версии PDFs в `inbox-reocr-fresh/` на сервере
(после улучшения / alternative scan source). Claude обрабатывает ровно одну,
отчитывается, ждёт next.

---

## Setup (один раз)

На сервере:

```
ssh ruslan@100.99.156.28
mkdir -p ~/jetix-os/inbox-reocr-fresh
# Сюда ты будешь класть fresh PDFs через scp с Windows
```

---

## Per-book workflow

### Шаг 1 — локально upload PDF на сервер

Put fresh PDF в temp folder на Windows, например:
`D:\Downloads\fresh-books\cagan-inspired-v2.pdf`

SCP на сервер в inbox-reocr-fresh:

```
scp D:/Downloads/fresh-books/cagan-inspired-v2.pdf ruslan@100.99.156.28:~/jetix-os/inbox-reocr-fresh/
```

### Шаг 2 — SSH на сервер, tmux, Claude

```
ssh ruslan@100.99.156.28
tmux new -s perbook  # или tmux a -t perbook если есть
cd ~/jetix-os
git pull
unset ANTHROPIC_API_KEY
claude --dangerously-skip-permissions
```

### Шаг 3 — Paste prompt

```
Per-book re-OCR через Max subscription (Claude Vision).

BOOK: <paste filename, e.g. cagan-inspired-v2.pdf>
SUBCATEGORY: <paste subcat, e.g. pdm>
TARGET SLUG: <paste slug, e.g. cagan-inspired-2ed-2017>

### Workflow

1. PDF лежит в: ~/jetix-os/inbox-reocr-fresh/<BOOK>
2. Check page count: python3 -c "from pypdf import PdfReader; print(len(PdfReader('~/jetix-os/inbox-reocr-fresh/<BOOK>').pages))"
3. Check text layer: python3 -c "from pypdf import PdfReader; r=PdfReader('~/jetix-os/inbox-reocr-fresh/<BOOK>'); print(sum(len(p.extract_text().split()) for p in r.pages[:3])//3, 'words/page avg')"

### Если text layer >100 words/page avg → pymupdf extract:
python3 << EOF
import pymupdf4llm
md = pymupdf4llm.to_markdown('~/jetix-os/inbox-reocr-fresh/<BOOK>')
with open('/tmp/<TARGET-SLUG>.md', 'w') as f: f.write(md)
print('written', len(md), 'chars')
EOF

### Если text layer <50 words/page → Claude Vision chunks:

Для каждого 10-page chunk:
- Read tool с pages: "1-10" (затем "11-20", etc.)
- Extract clean markdown text, preserve structure (headings / paragraphs / lists)
- Skip page numbers / running headers
- Save chunk to /tmp/<TARGET-SLUG>-chunk-NN.md
- Если chunk blocked by content filter → log в raw/books-md/_FILTER-BLOCKED.md `<target-slug>: pages X-Y blocked` → skip chunk → continue с pages X+10 to X+20
- ≥5 chunks подряд blocked → abort book → log "<target-slug>: multiple chunks blocked, needs Google Docs / iLovePDF OCR preprocessing"

После всех chunks:
- Concatenate all successful chunks в один MD
- Add YAML frontmatter:
```yaml
---
title: <Real book title>
author: <Author name>
year: <Publication year>
subcategory: <SUBCATEGORY>
expert: <from EXPERT_MAP>
priority: <from PRIORITY_MAP>
acquired_date: "2026-04-22"
converted_date: "<today>"
converted_via: "claude-vision-max"
source_format: "scanned-pdf"
word_count: <count>
quality_grade: "A"
tags: [<SUBCATEGORY>, ...]
---

<book content>
```
- Save to raw/books-md/<SUBCATEGORY>/<TARGET-SLUG>.md (OVERWRITE broken)

### Commit + push

git add raw/books-md/<SUBCATEGORY>/<TARGET-SLUG>.md raw/books-md/_FILTER-BLOCKED.md
git commit -m "[raw] re-OCR <Book title> via Claude Vision per-book"
git push origin claude/jolly-margulis-915d34

### Cleanup

rm ~/jetix-os/inbox-reocr-fresh/<BOOK>
rm /tmp/<TARGET-SLUG>-chunk-*.md /tmp/<TARGET-SLUG>.md 2>/dev/null

### Отчёт

После завершения — короткий отчёт:
- Total pages processed / blocked / skipped
- Word count final
- Quality grade (auto)
- Time taken
- Path к MD файлу
- Ready for next book signal

### Правила

- **Read tool только** — НЕ anthropic.Client / API / Python с Anthropic SDK
- **Max subscription** — всё идёт через unset ANTHROPIC_API_KEY env
- **Per-book atomic** — commit + push после этой книги, не вместе с другими
- **Auto, no confirmations** — dangerously-skip-permissions ON
- **Content filter skip chunk, не book** (≥5 chunks blocked = skip book)

Go.
```

### Шаг 4 — Wait + Review

Claude делает одну книгу → отчёт → ждёт. Ты видишь output в tmux → либо give next book prompt, либо exit tmux.

### Шаг 5 — Next book (повторить с Шага 1)

Upload следующий PDF → SCP → paste new prompt с новыми BOOK/SUBCATEGORY/TARGET SLUG.

---

## Template для paste в Claude (одна книга)

```
Per-book re-OCR:

BOOK: <filename.pdf>
SUBCATEGORY: <subcat>
TARGET SLUG: <slug>

Workflow как в tools/convert/reocr_per_book_prompt.md. 
Read tool only, Max subscription, chunks 10 pages,
content filter skip chunk continue book,
abort if ≥5 chunks blocked, commit + push после готовности,
отчёт + wait for next book.

Go.
```

---

## Subcategory → Expert + Priority map (reference для frontmatter)

| SUBCATEGORY | expert | priority |
|---|---|---|
| unix | unix-expert | P1 |
| clean-code | unix-expert | P1 |
| pm | pm-expert | P1 |
| pdm | pm-expert | P1 |
| mgmt | mgmt-expert | P1 |
| systems | systems-expert | P0 |
| cybernetics | systems-expert | P1 |
| complexity | systems-expert | P2 |
| investing | investor-expert | P2 |
| meta | meta-expert | P2 |
| biology | meta-expert | P1 |
| philosophy | philosophy-expert | P1 |
| philosophy-science | philosophy-expert | P1 |
| engineering-foundations | unix-expert | P1 |

---

## Remaining 5 books (для подстановки в prompt)

| BOOK | SUBCATEGORY | TARGET SLUG |
|---|---|---|
| cagan-inspired-v2.pdf | pdm | cagan-inspired-2ed-2017 |
| popper-conjectures-v2.pdf | philosophy-science | popper-conjectures-and-refutations-1963 |
| wiener-cybernetics-v2.pdf | cybernetics | wiener-cybernetics-2ed-1961 |
| grove-paranoid-v2.pdf | mgmt | grove-only-paranoid-survive-1996 |
| beer-brain-v2.pdf | cybernetics | beer-brain-of-the-firm-1972 |

(Префикс `-v2` если ты загружаешь improved versions, иначе без суффикса.)
