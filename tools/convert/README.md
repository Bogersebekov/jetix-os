# Conversion Pipeline — PDF/EPUB/TXT/HTML → LLM-friendly Markdown

## Quick start (3 команды)

```bash
# 1. Установить зависимости (один раз, 5-10 минут)
bash tools/convert/install.sh

# 2. Запустить full pipeline (4-8 часов автоматом, в фоне)
bash tools/convert/run_all.sh

# 3. Проверить результат
cat raw/books-md/INDEX.md | head -50
```

## Что делает

1. **Triage** — сканирует `raw/books-external/` и разделяет files по типам (text-PDF / scanned-PDF / EPUB / TXT / HTML)
2. **OCR** — для scanned PDFs добавляет text layer (ocrmypdf)
3. **Convert** — каждый file → Markdown в `raw/books-md/<subcategory>/`:
   - PDF → docling (primary) или pymupdf4llm (fallback)
   - EPUB → pandoc
   - HTML → pandoc
   - TXT → copy
4. **Frontmatter** — добавляет YAML metadata (title / subcategory / expert / priority / word_count / etc)
5. **Quality grade** — auto-grades каждый MD: A (clean) / B (minor artifacts) / C (needs reprocess)
6. **Index** — генерирует `raw/books-md/INDEX.md` — каталог всех книг

## Output structure

```
raw/
├── books-external/         # ORIGINALS (PDF/EPUB/TXT) — keep локально
│   ├── unix/
│   ├── clean-code/
│   └── ...
└── books-md/               # CONVERTED Markdown — push в git
    ├── INDEX.md            # каталог
    ├── unix/
    │   └── art-of-unix-programming-raymond-2003.md
    ├── clean-code/
    └── ...
```

## Advanced — отдельные шаги

```bash
# Только triage (без конверсии)
python tools/convert/convert_all.py --step triage

# Только OCR scanned PDFs
python tools/convert/convert_all.py --step ocr

# Только convert
python tools/convert/convert_all.py --step convert --resume

# Только quality check (после ручной проверки/исправления)
python tools/convert/convert_all.py --step quality

# Dry-run (показать что будет делать, без execute)
python tools/convert/convert_all.py --dry-run
```

## Resume mode

Скрипт запущен с `--resume` (default в `run_all.sh`) — **пропускает файлы которые уже конвертированы**. Можно прерывать Ctrl+C и запускать снова.

## Quality grading explained

Каждый MD получает auto-grade в frontmatter:

- **A ✅ Clean** — word count в range, headings есть, no OCR artifacts
- **B ⚠️ Minor artifacts** — page numbers leak / occasional weird breaks / small table issues. Usable.
- **C ❌ Poor** — OCR failed / garbled text / missing content. Нужен re-process.

**Auto-grader проверяет:**
- Word count (1K-500K expected)
- Isolated 'l' как OCR indicator
- Heading presence (3+ if >5K words)
- Non-ASCII/Cyrillic char ratio (< 2%)
- Page-number pollution in text

**Human override:** ставь grade руками в YAML frontmatter если автомат не прав.

## Expert assignment

Каждая книга получает `expert:` в frontmatter — какой Domain-Expert subagent её читает:

| Subcategory | Expert |
|---|---|
| unix / clean-code / engineering-foundations | unix-expert |
| pm / pdm | pm-expert |
| mgmt | mgmt-expert |
| systems / cybernetics / complexity | systems-expert |
| investing | investor-expert |
| meta / biology | meta-expert |
| philosophy / philosophy-science | philosophy-expert |

## Logs

`tools/convert/logs/YYYYMMDD-<step>.log` — все operations логируются.

## Troubleshooting

**`docling` очень медленный**
- Норма для первого run (модели качаются). ~30-60 сек/book.
- Fallback — pymupdf4llm быстрее, автоматом используется если docling fail.

**`ocrmypdf: tesseract not found`**
- Windows: скачай с https://github.com/UB-Mannheim/tesseract/wiki
- После install — добавь в PATH

**`pandoc: command not found`**
- Windows: скачай .msi с https://pandoc.org/installing.html
- Без pandoc — EPUB и HTML конверсия пропускается (PDF/TXT работают)

**Конкретный file конвертируется с ошибками**
- Проверь grade в frontmatter
- Если C — попробуй OCR ещё раз с agressive mode:
  ```bash
  ocrmypdf --force-ocr --deskew --clean-final <path>
  ```
- Или используй marker (тяжелее, но качественнее):
  ```bash
  pip install marker-pdf
  marker_single <file.pdf> --output_format markdown
  ```

## After conversion — commit

```bash
git add raw/books-md/ tools/convert/
git commit -m "[raw] books converted to Markdown — Waves 1-2"
git push origin claude/jolly-margulis-915d34
```

**ORIGINALS (raw/books-external/)** — не пуш в git сразу. Они большие (PDF 3-5MB each × 55 files = ~200MB+). Варианты:
1. Local-only (не push нигде — проще)
2. Git LFS (+$5/mo если >1GB)
3. External backup на диск

Рекомендация — local-only. MD достаточно для роя.

## ETA

Single book: 30-90 сек (docling) / 5-15 сек (pymupdf4llm fallback).
55 books: 4-8 часов wall-clock. Фоном OK.
