---
title: Step 3 Левенчук Books Distillation — 4 PDF + 1 TXT → MD + cross-link к Jetix substrate
date: 2026-05-20
type: autonomous-execution-prompt
phase_count: 8
parent_explain: prompts/explanations/_EXPLAIN-step-3-levenchuk-books-distillation-2026-05-20.md
parent_plan: daily-logs/_PLAN-OF-DAY-2026-05-20.md
input_corpus: raw/external/levenchuk-books-2026-05-20/
output_namespace: research/levenchuk-books-distillation-2026-05-20/ + raw/external/levenchuk-books-2026-05-20/converted/
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: levenchuk-books-distill
R: refuted_if_encoding_misfixed_OR_cross_link_misattributed_OR_LOCK_content_modified
constitutional_posture: R1 + R2 + R6 + R11 + EP-5 + append-only + Russian-primary
estimated_runtime: 90-120 min autonomous
estimated_cost: <€2
language: russian primary
---

# Step 3 Левенчук Books Distillation — Prompt

> **Trigger:** Ruslan 2026-05-20 — «обработай это всё на сервере, push в один, всё в md переведи». Per-phase commit + push. NOT plan mode — execute autonomously on launch.

---

## §0 Pre-flight (mandatory)

ПЕРЕД Phase 0 прочитай:
1. **EXPLAIN:** `prompts/explanations/_EXPLAIN-step-3-levenchuk-books-distillation-2026-05-20.md`
2. **INVENTORY:** `raw/external/levenchuk-books-2026-05-20/00-INVENTORY.md`
3. **Memory rules:**
   - `feedback_iwe_chat_rejected.md` — Aisystant chat REJECTED (только text materials)
   - `feedback_fpf_lens_first.md` — FPF lens Phase 0 mandatory
   - `feedback_breadth_not_selection.md` — surface highlights, не «top 3 best chapters» selection
   - `feedback_no_unsolicited_alternatives.md` — distillation execution не recommendations
4. **Cross-link target:**
   - `wiki/concepts/method-systems-thinking.md` + `jetix-as-exokortex.md` + `sense-of-measure-scientific-approach.md` (3 K-6 Tier A wikis)
   - `research/method-systems-thinking-deep-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
   - `research/intellect-12-component-audit-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
   - `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/04-cross-link-к-jetix-substrate.md`

---

## §1 Phase 0 — Pre-flight (5m)

**Output:** `research/levenchuk-books-distillation-2026-05-20/phase-0-preflight.md`

### Steps
1. Verify 5 files в `raw/external/levenchuk-books-2026-05-20/`
2. Check available tools:
   ```bash
   which pdftotext  # poppler-utils
   which iconv      # libiconv
   python3 -c "import fitz; print(fitz.__doc__[:50])"  # pymupdf fallback
   ```
3. Mkdir output namespace:
   ```bash
   mkdir -p raw/external/levenchuk-books-2026-05-20/converted/
   mkdir -p research/levenchuk-books-distillation-2026-05-20/diagrams/
   ```

Commit: `[step-3-lev] Phase 0 pre-flight + tools check`

---

## §2 Phase 1 — TXT Encoding Fix Методология 2025 (5-10m)

**Output:** `raw/external/levenchuk-books-2026-05-20/converted/03-metodologiya-2025.md`

### Steps
1. Convert CP1251 → UTF-8:
   ```bash
   iconv -f WINDOWS-1251 -t UTF-8 \
     raw/external/levenchuk-books-2026-05-20/Levenchuk_A._Metodologiya_2025.txt \
     > raw/external/levenchuk-books-2026-05-20/converted/03-metodologiya-2025.md
   ```
2. Add MD header frontmatter:
   ```markdown
   ---
   title: Методология 2025
   author: Анатолий Левенчук
   year: 2025
   source: Levenchuk_A._Metodologiya_2025.txt (CP1251→UTF-8 converted 2026-05-20)
   pages: ~826 (per Ridero info)
   ---
   ```
3. Sanity check — first 500 chars должны быть readable русский:
   ```bash
   head -c 1500 raw/external/levenchuk-books-2026-05-20/converted/03-metodologiya-2025.md
   ```

Commit: `[step-3-lev] Phase 1 Методология 2025 CP1251→UTF-8 converted`

---

## §3 Phase 2 — PDF → MD Conversion 4 Books (15-20m)

**Outputs:**
- `raw/external/levenchuk-books-2026-05-20/converted/01-sistemnoe-myishlenie-2024-tom-1.md`
- `raw/external/levenchuk-books-2026-05-20/converted/02-sistemnoe-myishlenie-2024-tom-2.md`
- `raw/external/levenchuk-books-2026-05-20/converted/04-intellekt-stek-2023.md`
- `raw/external/levenchuk-books-2026-05-20/converted/05-injeneriya-lichnosti.md`

### Steps per PDF

**Primary tool — pdftotext (poppler-utils):**
```bash
pdftotext -layout -enc UTF-8 \
  raw/external/levenchuk-books-2026-05-20/Levenchuk_A._Sistemnoe_Myishlenie_2024.a4.pdf \
  raw/external/levenchuk-books-2026-05-20/converted/01-sistemnoe-myishlenie-2024-tom-1.md
```

**Fallback if pdftotext fails / poor quality — pymupdf (Python):**
```python
import fitz
doc = fitz.open("input.pdf")
text = ""
for page_num, page in enumerate(doc):
    text += f"\n\n--- Page {page_num+1} ---\n\n"
    text += page.get_text()
with open("output.md", "w", encoding="utf-8") as f:
    f.write(text)
```

### Per converted MD — add header
```markdown
---
title: <Book title>
author: Анатолий Левенчук
year: <year>
source: <original PDF filename>
pages: <page count>
conversion_tool: pdftotext / pymupdf
conversion_date: 2026-05-20
---
```

### Quality check per book
- First 1000 chars Russian readable?
- Layout preserved roughly (chapters / subheadings detectable)?
- Special chars / diagrams marked or skipped cleanly?

### Mapping which PDF = which Tom (Системное мышление)
- `Levenchuk_A._Sistemnoe_Myishlenie_2024.a4.pdf` (3.55 MB, no suffix) → check first page → Tom 1 OR Tom 2 (likely smaller = Tom 1)
- `Levenchuk_A._Sistemnoe_Myishlenie_202470915633.a4.pdf` (4.95 MB, has number suffix) → likely Tom 2

Если first-page check показывает иначе — swap labels.

Commit: `[step-3-lev] Phase 2 PDF→MD 4 books converted`

---

## §4 Phase 3 — TOC Extract + Chapter Boundaries (10-15m)

**Output:** Per-book section в distillation directory + chapter index в overview.

### Steps per book
1. Read converted MD
2. Identify TOC markers (typically «Оглавление» / «Содержание» section)
3. Extract chapter list with page numbers (if visible)
4. Identify chapter boundary markers (typically «Глава N» / Chapter headings via formatting)
5. Output structured TOC к `research/levenchuk-books-distillation-2026-05-20/0N-<book>-toc-highlights.md` Section §1

### Output structure per book
```markdown
---
title: Системное мышление 2024 Том 1 — TOC + Highlights
---

## §1 Table of Contents

| # | Глава | Страница (если visible) |
|---|---|---|
| 1 | <chapter name> | <page> |
| ... | ... | ... |

## §2 Chapter Boundaries (markers detected)
- Глава 1: pages X-Y (offset in converted MD: line Z)
- ...

## §3 Key sections highlight (Phase 4 result here)
[...]

## §4 Cross-link к Jetix substrate (Phase 5 result)
[...]
```

Commit: `[step-3-lev] Phase 3 TOC + chapter boundaries 5 books`

---

## §5 Phase 4 — Key Chapter Highlights (20-30m)

**Goal:** Per book — surface 3-5 key chapters + brief 200-300w summary per chapter. **NOT deep analysis** (this is для future FPF deep phase). Just surfacing for cross-link mapping.

### Per book

1. Pick 3-5 chapters per книга based on:
   - Cross-link relevance к Jetix substrate (K-6 / K-4 / Education Layer / Recursive Engine)
   - TOC clear strategic importance (introduction / conclusion / key methodology)
   - Length (longer chapters often = core)
2. Per chapter — 200-300w summary in Russian:
   - Что обсуждает (1-2 sentences)
   - Ключевые termы / concepts (verbatim Левенчук terms preserved)
   - Cross-cite к Jetix substrate если obvious overlap (defer detailed matrix к Phase 5)
3. Add к per-book MD §3

### Output format per highlight
```markdown
### §3.1 Глава 4 — Метод системного мышления

[200-300w summary]

**Ключевые термы Левенчука:** виды деятельности / системные уровни / стейкхолдер / альфы.

**Predicted overlap (Phase 5 confirms):** K-6 Method components #1-#5 / O-75 Pre-existing Partnership frame / Recursive Engine concept doc.

[src: 01-sistemnoe-myishlenie-2024-tom-1.md chapter 4 lines NN-MM]
```

Commit: `[step-3-lev] Phase 4 key chapter highlights 5 books × 3-5 chapters`

---

## §6 Phase 5 — Cross-link Matrix 4 Books × 8 Jetix Sources (15-20m)

**Output:** `research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md`

### 8 Jetix substrate sources

1. **K-6 Method-Systems-Thinking** (research + 3 Tier A wikis) — **HIGHEST priority** cross-link
2. **K-4 Intellect-12-Component Audit** — для Интеллект-стек 2023 book особенно
3. **5 acked concept docs F2** (Hackathon / Recursive / System Merger / Outreach / Education Layer)
4. **Platform v2** (§6 7-role / §7 values / §20 templates)
5. **Левенчук inventory v2** (189-cell cross-link matrix existing)
6. **Sprint-Synthesis-v2 Doc 4** (Master Packaging Step 6)
7. **9 existing Tier A wikis** (особенно K-6: method / exokortex / sense-of-measure)
8. **3 NEW Tier A wikis batch-7** (partnership / mastery / persistence)

### Matrix structure

```markdown
## §1 Books × Sources Cross-link Matrix

|              | K-6 method | K-4 intellect | 5 concept docs | Platform v2 | Lev inv v2 | SS-v2 Doc 4 | 9+3 wikis |
|--------------|------------|---------------|----------------|-------------|------------|-------------|-----------|
| СМ 2024 Т1   | ✅ deep    | 🟢 medium     | 🟢            | 🟢          | ✅         | 🟢          | ✅        |
| СМ 2024 Т2   | ✅ deep    | 🟡            | 🟢            | 🟢          | ✅         | 🟢          | ✅        |
| Методология  | ✅ deep    | 🟡            | ✅ Recursive   | 🟢          | ✅         | 🟢          | ✅ method |
| Интеллект-стек | 🟢       | ✅ deep        | 🟢 Education   | 🟢 §7       | ✅         | 🟢          | 🟢        |
| Инженерия личности | 🟢   | 🟢            | ✅ Education   | 🟢 §6       | 🟢         | 🟢          | ✅ mastery |
```

### Per-cell narrative
- Identify specific chapter / concept в book + specific section / claim в Jetix source
- Note depth (verbatim mention / structural parallel / gap-to-fill)
- Surface 5-10 most interesting overlaps for next FPF deep phase

Commit: `[step-3-lev] Phase 5 cross-link matrix 4 books × 8 sources`

---

## §7 Phase 6 — DE-RU Terminology Glossary (10-15m)

**Output:** `research/levenchuk-books-distillation-2026-05-20/07-DE-RU-terminology-glossary.md`

### Goal
Extract Левенчук method terminology (Russian primary) + cross-cite к 3 K-6 Tier A wikis. Bridge between Левенчук's vocabulary и Jetix's substrate.

### Format

```markdown
## §1 Core Methodology Terms (Левенчук corpus)

### Системное мышление (Systems Thinking)
- **Левенчук definition:** [verbatim] (СМ 2024 Т1 Глава X)
- **Jetix cross-cite:** `wiki/concepts/method-systems-thinking.md` §1 — K-6 31 components mirror this structurally
- **Notes:** Левенчук acks 10 thinkers; K-6 wiki cites same set + adds Hofstadter; Левенчук = 11th thinker candidate

### Стейкхолдер (Stakeholder)
- **Левенчук definition:** [verbatim]
- **Jetix cross-cite:** Platform v2 §6 22 Tier-1 stakeholder list / Pre-existing Partnership wiki §3 stakeholder positioning

[... 30-50 entries minimum across all 5 books ...]

## §2 Cross-cite priorities (top 10 для outreach pitch usage)

[10 terms ranked by usefulness в KA-01 Левенчук pitch context]
```

Commit: `[step-3-lev] Phase 6 DE-RU terminology glossary ~30-50 entries`

---

## §8 Phase 7 — Summary + Daily Log + Push (10m)

**Outputs:**
- `research/levenchuk-books-distillation-2026-05-20/00-SUMMARY-FOR-RUSLAN.md` (≤1000w)
- 3 mermaid diagrams в `diagrams/`
- `daily-logs/_DAILY-LOG-2026-05-20.md` §APPEND step-3 execution log

### Summary structure (≤1000w)

```markdown
# Summary for Ruslan — Левенчук Books Distillation (2026-05-20)

## §0 TL;DR (≤200w)
- 4 PDF + 1 TXT → 5 MD converted (~17 MB → ~12-15 MB text)
- Per-book TOC + 3-5 chapter highlights surface
- Cross-link matrix 5 books × 8 Jetix sources
- DE-RU terminology glossary ~30-50 entries
- Top finding: [пример: К-6 Method 31 components совпадают structurally с Системное мышление 2024 главой N]

## §1 Что прочитал брат (5 books scope)
[Per-book brief]

## §2 Что сделано автономно (8 commits)
[Phase counts + files created]

## §3 Top 5 cross-link findings ⭐
[Most interesting overlaps for next FPF deep phase]

## §4 5 GAPS detected (Левенчук coverage где Jetix отсутствует)
[Where Левенчук deep but Jetix substrate empty — opportunity для cross-cite в pitches]

## §5 Top-10 terminology bridges (для KA-01 Левенчук pitch usage)
[Direct verbatim Левенчук terms + Jetix counterpart wiki/concept]

## §6 What's next (per PLAN-OF-DAY)
- Step 4 Distribution Plan уже launched / завершён (cross-link)
- Future deep FPF research phase ready (substrate enriched 4 books)
- KA-01 Левенчук pitch — usable verbatim quotes + book references

## §7 Files map для drill-down
[Paths]

## §8 Cost + runtime
~90-120 min / <€2 / 8 commits
```

### 3 mermaid diagrams

1. `01-corpus-overview.md` — graph 4 books + 1 txt с per-book topic
2. `02-cross-link-к-substrate.md` — 4 books × 8 Jetix sources heatmap
3. `03-chapter-priority-heatmap.md` — per-chapter importance для будущего deep FPF

### Daily Log §APPEND

```markdown
## §N §APPEND-step-3-levenchuk-books-distill (2026-05-20)
- 5 files processed (4 PDF + 1 TXT)
- Total converted text: ~12-15 MB
- 5 per-book MDs + cross-link matrix + terminology glossary + Summary
- Substrate ready для future deep FPF research phase
- Cost: <€2; runtime ~XX min
```

### Final push

```bash
git add raw/external/levenchuk-books-2026-05-20/converted/ research/levenchuk-books-distillation-2026-05-20/ daily-logs/_DAILY-LOG-2026-05-20.md
git commit -m "[step-3-lev] Phase 7 Summary + Daily Log §APPEND + final push"
git push origin main
```

Final echo:
```
DONE Phase 7 — 8 commits / N files / 3 mermaid / 4 PDF + 1 TXT processed / cross-link matrix done / DE-RU glossary ~30-50 entries / cost ~€X / runtime ~Y min
```

---

## §9 Operational rules

- **Per-phase commit + push** (mandatory)
- **NO Foundation modifications** — only new namespaces
- **NO Tier A wiki auto-promotion** from book content (Ruslan acks separately)
- **NO deep philosophical analysis** — это future FPF deep phase
- **Russian primary** в всех outputs (Левенчук verbatim quotes preserved)
- **R6 provenance** — `[src: book.pdf page N]` или `[src: converted/0X-book.md line N]`
- **PDF conversion quality check** per book Phase 2 (sanity test first 1500 chars)
- **Fallback discipline** — pdftotext fail → pymupdf; pymupdf fail → log + skip + flag

---

## §10 If blocked

- pdftotext not available → use pymupdf
- pymupdf import fails → install `pip install pymupdf` first (or use `python3 -m pip`)
- iconv missing → use Python `codecs.open(..., encoding='cp1251')` → write utf-8
- Single book corruption → log + skip + continue 4 others
- TOC extraction unclear → fallback к keyword search «Глава [0-9]» + manual structure
- Cross-link cell uncertain → mark 🟡 partial + brief reason

---

## §11 Trigger для launch

Ruslan в Claude Code на сервере (VS Code Remote SSH tmux session) paste'aет:

```
ultrathink. Прочитай prompts/step-3-levenchuk-books-distillation-2026-05-20.md и prompts/explanations/_EXPLAIN-step-3-levenchuk-books-distillation-2026-05-20.md и raw/external/levenchuk-books-2026-05-20/00-INVENTORY.md. Выполни все 8 phases автономно, per-phase commit + push origin main, final push в конце. Ruslan acked launch — «обработай это всё на сервере, push в один, всё в md переведи». 4 PDF + 1 TXT (Методология 2025 CP1251→UTF-8). Output: 5 converted MD + 5 per-book highlights + cross-link matrix 5 books × 8 Jetix sources + DE-RU terminology glossary ~30-50 entries + Summary. ~90-120 min, <€2. NOT deep philosophical analysis (это future FPF deep phase). Russian primary. R1+R2+R6+R11+EP-5+append-only preserved. Не пауза, не вопросы.
```

---

*Prompt closure 2026-05-20. Per memory `feedback_prompt_explanation_required.md` + `feedback_cowork_can_push.md` — EXPLAIN written; Ruslan acked execute autonomously.*
