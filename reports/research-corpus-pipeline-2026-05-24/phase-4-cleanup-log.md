---
title: Phase 4 — Quality Cleanup Log
date: 2026-05-24
phase: 4/7
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
constitutional_posture: R1 surface
---

# Phase 4 — Quality Cleanup Log

## §4.1 Method

Conservative cleanup applied to all Phase 2 + Phase 3 MDs (those with `extraction_method:` in frontmatter):

1. **Strip page-number lines** — regex `^\s*\d{1,4}\s*$`
2. **Join hyphenated line breaks** — regex `(\w)-\n(\w)` → `\1\2`
3. **Strip trailing whitespace** per line
4. **Collapse 4+ blank lines → 2**
5. **Preserve YAML frontmatter intact** — append cleanup metadata only

## §4.2 Scope decision: light-touch over aggressive

NOT removed (too risky for varied formats):
- Recurring header/footer lines (could remove real chapter titles)
- Multi-line ToC artifacts
- OCR ligature recovery (psm 6 output is usually clean enough)

Rationale: Per R1 surface only mandate + append-only discipline. Tokens saved by aggressive cleanup do not offset risk of removing real content.

## §4.3 Pass 1 results (text MDs from Phase 2)

| Metric | Value |
|---|---|
| MDs processed | 69 (66 text Phase 2 + 3 _unknown text + 3 voice-memos with extraction_method field — incidental scope) |
| Chars before | 48,616,789 |
| Chars after | 48,346,232 |
| Saved | 270,557 (0.6%) |

### Notable cleanup wins
- **le-bon-the-crowd-1895.md** — 15.0% saved (Google Books header noise; will be re-OCR'd in Phase 3)
- **axelrod-evolution-of-cooperation-1984.md** — 3.4% saved
- **rogers-level-up-2010.md** — 2.5% saved
- **robbins-unlimited-power-1986.md** — 2.4% saved
- **chalmers-what-is-this-thing-called-science-1976.md** — 2.2% saved

Most MDs saved <1% (text PDFs typically had minimal page-number noise).

## §4.4 Pass 2 (OCR MDs from Phase 3) — pending Phase 3 completion

Will re-run cleanup script on OCR MDs after Phase 3 completes. OCR output has more page-number noise (Tesseract often catches them) so expected higher savings.

## §4.5 Phase 4 conclusion (Pass 1)

Conservative cleanup applied to 69 text MDs. 0.6% chars saved. No content loss risk. Pass 2 (OCR MDs) deferred to post-Phase-3.

Frontmatter cleanup-metadata appended:
```yaml
phase4_cleaned: true
phase4_chars_before: <int>
phase4_chars_after: <int>
phase4_saved_pct: <float>
```
