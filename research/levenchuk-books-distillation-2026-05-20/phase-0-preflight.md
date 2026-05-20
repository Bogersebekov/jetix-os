---
title: Phase 0 Pre-flight — Левенчук Books Distillation
date: 2026-05-20
type: phase-preflight-log
phase: 0
parent_prompt: prompts/step-3-levenchuk-books-distillation-2026-05-20.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: levenchuk-books-distill
constitutional_posture: R1 + R2 + R6 + R11 + EP-5 + append-only
---

# Phase 0 — Pre-flight Verification

## §1 Input corpus verified (5 files, 16.94 MB)

| # | File | Size (bytes) | Format |
|---|---|---|---|
| 1 | `Levenchuk_A._Sistemnoe_Myishlenie_2024.a4.pdf` | 3,719,520 (3.55 MB) | PDF |
| 2 | `Levenchuk_A._Sistemnoe_Myishlenie_202470915633.a4.pdf` | 5,190,587 (4.95 MB) | PDF |
| 3 | `Levenchuk_A._Metodologiya_2025.txt` | 1,278,058 (1.22 MB) | TXT CP1251 |
| 4 | `Levenchuk_A._Intellekt_Stek_2023.a4.pdf` | 5,879,169 (5.61 MB) | PDF |
| 5 | `Levenchuk_A._Injeneriya_Lichnosti.a4.pdf` | 1,823,443 (1.74 MB) | PDF |

## §2 Tools verified

- `pdftotext` — `/usr/bin/pdftotext` (poppler-utils) ✅
- `iconv` — `/usr/bin/iconv` (libiconv) ✅
- `pymupdf` (fallback) — PyMuPDF 1.27.2.2 (MuPDF 1.x) ✅

## §3 Output namespaces created

- `raw/external/levenchuk-books-2026-05-20/converted/` (5 converted MD target)
- `research/levenchuk-books-distillation-2026-05-20/` (distillation outputs)
- `research/levenchuk-books-distillation-2026-05-20/diagrams/` (3 mermaid target)

## §4 Cross-link target sources verified (read-only)

- `wiki/concepts/method-systems-thinking.md`
- `wiki/concepts/jetix-as-exokortex.md`
- `wiki/concepts/sense-of-measure-scientific-approach.md`
- `research/method-systems-thinking-deep-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
- `research/intellect-12-component-audit-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
- `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/04-cross-link-к-jetix-substrate.md`
- 5 acked concept docs F2 (Hackathon / Recursive Engine / System Merger / Outreach / Education Layer)
- Platform v2 (§6 7-role / §7 values / §20 templates)

## §5 Constitutional checks

- R1 surface: brigadier-scribe authoring (distillation only, no strategic prose)
- R2: no Foundation modifications planned; only new namespaces
- R6: provenance discipline `[src: book.pdf page N]` / `[src: converted/0X-book.md line N]`
- R11: discovery + distillation only; no novel actions
- EP-5 F2: verbatim extraction; commentary F2-F3
- Append-only: original PDF/TXT untouched

## §6 Status

✅ Phase 0 complete. Proceeding to Phase 1 (TXT CP1251 → UTF-8 fix).

*Phase 0 closure 2026-05-20.*
