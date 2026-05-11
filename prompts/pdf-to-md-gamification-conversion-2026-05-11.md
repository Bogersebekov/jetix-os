# PDF → MD Conversion — 13 gamification books

> **Создано:** 2026-05-11 afternoon.
> **Задача:** конвертировать 13 PDFs из `raw/papers-pdf/gamification/` в Markdown с extracted images.
> **Gate:** Шаг C gamification mining требует MD format.
> **Wall-clock target:** 30-60 min для всех 13 books.

---

## Команды запуска

```bash
# В новом tmux window:
claude --dangerously-skip-permissions

# Затем paste весь текст ниже под линией ===PROMPT===
```

---

===PROMPT===

Задача: конвертировать 13 PDF books из `raw/papers-pdf/gamification/` в высококачественный Markdown с extracted images. Глубоко, качественно, до конца, на 1000% proработано.

## Источники (13 PDFs, 5007 pages, 86.6 MB total)

```
raw/papers-pdf/gamification/
├── axelrod-evolution-of-cooperation-1984.pdf (231 p, TEXT-OK)
├── castronova-synthetic-worlds-2005.pdf (338 p, TEXT-OK) ⭐ CORE
├── cialdini-influence-ru-1984.pdf (407 p, TEXT-OK, RUSSIAN)
├── csikszentmihalyi-flow-1990.pdf (314 p, TEXT-OK)
├── eyal-hooked-2014.pdf (137 p, TEXT-OK) ⭐ CORE
├── koster-theory-of-fun-2004.pdf (214 p, PARTIAL — image-heavy) ⭐ CORE
├── lehdonvirta-castronova-virtual-economies-2014.pdf (307 p, TEXT-OK)
├── rogers-level-up-2010.pdf (516 p, PARTIAL — game art heavy)
├── rouse-game-design-theory-and-practice-2004.pdf (724 p, TEXT-OK)
├── salen-zimmerman-rules-of-play-2003.pdf (694 p, TEXT-OK — densest)
├── schell-art-of-game-design-lenses.pdf (518 p, TEXT-OK)
├── schelling-strategy-of-conflict-1960.pdf (319 p, TEXT-OK)
└── varoufakis-technofeudalism-2023.pdf (288 p, PARTIAL)
```

## Output дир + структура

```
raw/books-md/gamification/
├── {slug}.md                        # main markdown text
├── {slug}_images/                   # extracted figures / diagrams
│   ├── img-001.png
│   ├── img-002.jpg
│   └── ...
└── {slug}.meta.yaml                 # conversion metadata + audit
```

## Tool selection — choose BEST available

**Priority order:**

1. **`marker-pdf`** (preferred — best MD quality, image extraction, layout preservation, OCR fallback)
   ```bash
   pip install marker-pdf
   ```
   Usage: `marker_single input.pdf output_dir/`

2. **`pymupdf4llm`** (fallback — fast, simpler MD output, images extracted)
   ```bash
   pip install pymupdf4llm
   ```
   Usage: `pymupdf4llm.to_markdown(pdf_path, write_images=True, image_path=...)`

3. **`docling`** (IBM — structured output, accurate layout)
   ```bash
   pip install docling
   ```
   Usage: `DocumentConverter().convert(source).document.export_to_markdown()`

4. **`pdftotext` + `pdfimages`** (last resort baseline — text only + manual image extraction)

**Decision rule:**
- Try marker on 1 sample book (Castronova) first
- If output > 50K chars AND ≥ 10 images extracted → use marker for all
- Else fall back to pymupdf4llm
- If pymupdf4llm also fails → docling
- If all fail → pdftotext baseline + flag in audit

## Script creation

Create `tools/convert_pdfs_to_md.py` (modular, idempotent, skip-if-exists):

```python
#!/usr/bin/env python3
"""
Convert PDFs in raw/papers-pdf/gamification/ to Markdown with extracted images.
Idempotent: skips books already converted (checks output .md + _images/ dir exist).

Usage:
    python3 tools/convert_pdfs_to_md.py [--force] [--book BOOKNAME]

Args:
    --force: overwrite existing MD even if present
    --book BOOKNAME: convert only specific book (filename slug)
"""
# Full implementation:
# 1. Iterate raw/papers-pdf/gamification/*.pdf
# 2. For each, check if {slug}.md exists in raw/books-md/gamification/ — skip unless --force
# 3. Try marker → fallback pymupdf4llm → fallback docling → fallback pdftotext
# 4. Extract images to {slug}_images/ subdir
# 5. Generate .meta.yaml with conversion stats
# 6. Add Tier 2 R6 compliant frontmatter to .md
# 7. Log progress per book + final summary
```

## Per-book frontmatter в .md (per Addendum §3.1)

```yaml
---
title: "<book title>"
author: "<author>"
year: <YYYY>
language: en | ru
source_classifier:
  tier: T1                                # CORE books = T1; bonus textbooks = T2
  type: book
  verifiable_author: true
  year: <YYYY>
  cross_validated: false                  # set true post-domain pass
  primary_source_url_or_path: raw/papers-pdf/gamification/<filename>.pdf
pdf_source: raw/papers-pdf/gamification/<filename>.pdf
md_converted_by: marker | pymupdf4llm | docling | pdftotext
md_conversion_date: 2026-05-11
pages_pdf: <N>
words_md: <N>
images_extracted: <N>
images_dir: raw/books-md/gamification/{slug}_images/
pipeline: ingested
state: draft
F: F4
G: published-source-applied-now
R: R-high
niche: business
secondary_niche: meta
---
```

## Tier assignment (per Addendum §1.1-§1.2)

**Tier 1 (R-high, anchor-eligible)** — primary academic + foundational:
- Castronova Synthetic Worlds (T1)
- Lehdonvirta-Castronova Virtual Economies (T1)
- Csikszentmihalyi Flow (T1)
- Axelrod Evolution of Cooperation (T1)
- Schelling Strategy of Conflict (T1)
- Cialdini Influence (T1, language: ru)
- Eyal Hooked (T1)
- Koster Theory of Fun (T1)
- Varoufakis Technofeudalism (T1)

**Tier 2 (R-medium, supportive textbooks)** — practitioner experience:
- Schell Art of Game Design (T2 textbook)
- Salen-Zimmerman Rules of Play (T2 textbook)
- Rouse Game Design Theory & Practice (T2 textbook)
- Rogers Level Up! (T2 practical guide)

## Quality validation per book

После каждой конверсии — auto-validate:

1. **Word count check:** > 5000 words (sanity — book has content)
2. **Headers detected:** at least 5 h1/h2/h3 in MD (chapter structure)
3. **Image count:** record actual extracted vs PDF native image references
4. **Encoding:** UTF-8 valid; for Cialdini RU — Cyrillic chars preserved
5. **Reading order:** spot-check first 200 chars matches PDF page 1

Если quality fail для book — **DO NOT skip silently.** Surface в final report, mark `pipeline: raw` (не `ingested`) + reason.

## Special handling

### Cialdini RU
- Russian text preserve as-is — НЕ переводить
- `language: ru` в frontmatter
- `prose_in: russian` для downstream filtering

### Koster (PARTIAL — image-heavy)
- Книга comic-style с большим числом иллюстраций
- Image extraction CRITICAL — там visual explanations
- Если marker не достаёт images — попробуй pymupdf4llm с verbose extraction
- Acceptable: 100+ images extracted

### Rogers Level Up (PARTIAL — game art)
- Колорные иллюстрации игровых концептов
- Images extraction nice-to-have, не critical (text меньше depend on images)

### Varoufakis (PARTIAL)
- Likely combination of text + some inline visualizations
- Standard conversion OK

## Run sequence

### 1. Install tools (one-time setup)
```bash
pip install marker-pdf pymupdf4llm docling 2>&1 | tail -5
```

### 2. Test on 1 sample (Castronova) — verify quality before mass run
```bash
python3 tools/convert_pdfs_to_md.py --book castronova-synthetic-worlds-2005
ls -la raw/books-md/gamification/castronova-synthetic-worlds-2005*
wc -l raw/books-md/gamification/castronova-synthetic-worlds-2005.md
head -100 raw/books-md/gamification/castronova-synthetic-worlds-2005.md
```

### 3. Verify sample quality
- Word count > 50K (Castronova ~338 p × ~250 words/p = ~85K expected)
- Images extracted (try Castronova — academic book usually has tables/charts)
- Frontmatter correct
- Markdown well-formed (no parser errors)

### 4. If sample OK → mass convert all 12 остальных
```bash
python3 tools/convert_pdfs_to_md.py
```

### 5. Final summary report
Создать `reports/pdf-to-md-conversion-2026-05-11.md`:
- Per-book: tool used / pages → words / images extracted / quality verdict
- Total: 13 books / pages / words / images / disk usage MB
- Failed books (if any) + reason
- Wall-clock per book

### 6. Commit + push
```bash
git add raw/books-md/gamification/ tools/convert_pdfs_to_md.py reports/pdf-to-md-conversion-2026-05-11.md
git commit -m "[raw-md] 13 gamification books converted PDF → MD with images — marker/pymupdf4llm — full text + figures + Tier 2 R6 frontmatter"
git push origin main
```

## Hard constraints

- **Constitutional posture:** F2 blast-radius, append-only к raw/books-md/, NO writes к canonical (Foundation / decisions / principles / .claude/config)
- **AI = scribe rule** (Tier 2 R1) — конвертация = scribe action, не strategic
- **NO API keys в commits** — pre-commit grep `ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY` raw/books-md/ → 0 hits required
- **Idempotent re-run** — script может быть запущен снова без duplicates
- **NO touching `raw/papers-pdf/` originals** — append-only к `raw/books-md/`
- **Language preserve** — Russian text НЕ переводить; English стays English

## Quality target — глубоко, на 1000%

- 13/13 books конвертированы
- ≥ 90% TEXT-OK preserved (per pdftext baseline pre-vs-post)
- Images extracted с reasonable count (academic ~50-200, illustrated ~100-500)
- Frontmatter complete per Addendum §3.1
- Validation pass на каждой book
- Failed books surface explicitly (NOT silently skipped)

## Final report формат

Когда done — дай в чат:
- Tool used (marker primary?)
- Per-book table: pages → words → images → tier → status
- Total stats
- Disk usage raw/books-md/gamification/ (MB)
- Failed books (если есть) + plan
- Next step: «PDF→MD conversion done — N/13 OK, ready для Шаг C gamification mining trigger»

После твоего report — я ack + триггерну Шаг C («Шаг C: starts brigadier dispatch — gamification deep wiki mining»).

Wall-clock budget: 30-60 min total. Если > 90 min — checkpoint + ask Ruslan продолжать.

GO.

===END PROMPT===
