---
title: Левенчук Books Inventory — 4 PDF + 1 TXT (top-4 newest editions)
date: 2026-05-20
type: corpus-inventory
trigger: Ruslan downloaded 2026-05-20 для Step 3 distillation
F: F2
G: levenchuk-books-corpus
prose_authored_by: brigadier-scribe (Cloud Cowork)
status: vendored ready for server CC processing
---

# Левенчук Books — Vendored Corpus (2026-05-20)

> 5 файлов (~17 MB) — top-4 newest editions из Левенчук corpus. Ready для Step 3 distillation (PDF→MD + txt CP1251 fix + TOC + cross-link к Jetix substrate).

---

## §1 Files

| # | File | Format | Size | Topic | Cross-link к Jetix |
|---|---|---|---|---|---|
| 1 ⭐⭐ | `Levenchuk_A._Sistemnoe_Myishlenie_2024.a4.pdf` | PDF | 3.55 MB | **Системное мышление 2024 Т1** | K-6 structural twin |
| 2 ⭐⭐ | `Levenchuk_A._Sistemnoe_Myishlenie_202470915633.a4.pdf` | PDF | 4.95 MB | **Системное мышление 2024 Т2** (или другой volume) | K-6 structural twin |
| 3 ⭐⭐ | `Levenchuk_A._Metodologiya_2025.txt` | TXT (**CP1251**) | 1.23 MB | **Методология 2025** | K-6 method + Recursive Engine |
| 4 ⭐ | `Levenchuk_A._Intellekt_Stek_2023.a4.pdf` | PDF | 5.61 MB | **Интеллект-стек 2023** | K-4 12-component anchor |
| 5 | `Levenchuk_A._Injeneriya_Lichnosti.a4.pdf` | PDF | 1.74 MB | **Инженерия личности 2023** | Education Layer + mastery-formula wiki |

**Total: ~17 MB / 4 PDF + 1 TXT.**

---

## §2 Processing requirements

### PDF → MD conversion
- 4 PDF файла (A4 format, типичные learning materials с text + diagrams)
- Tools: **pdftotext** (poppler-utils) для plain text OR **pymupdf** (Python) для structured extract OR **pandoc** (если PDF-source compatible)
- Russian text — нужен UTF-8 output
- Diagrams / mermaid диаграммы / images — лучше игнорировать (or note pages) для quick distillation, не deep OCR

### TXT encoding fix
- `Levenchuk_A._Metodologiya_2025.txt` — **CP1251** (Windows Cyrillic legacy encoding)
- Convert к UTF-8:
  ```bash
  iconv -f WINDOWS-1251 -t UTF-8 input.txt > output.txt
  ```

### TOC + structure
- Extract Table of Contents per книга
- Identify chapter boundaries
- Per-chapter словосочетания short summary

### Cross-link к Jetix substrate (priority)
- К-6 Method-Systems-Thinking deep research (особенно 10 thinkers cited vs Левенчук's lineage)
- 3 K-6 Tier A wikis: method-systems-thinking / jetix-as-exokortex / sense-of-measure-scientific-approach
- К-4 Intellect-12-Component Audit (vs Интеллект-стек 2023 framework)
- Education Layer concept doc + mastery-formula wiki (vs Инженерия личности 2023)
- Левенчук inventory v2 cross-link matrix 189-cell

---

## §3 Что НЕ скачано (missing из 6 newest)

- ❌ Системная инженерия 2022 — defer для отдельной download
- ❌ Системный менеджмент 2023 — defer

(Можно добавить позже если важно.)

---

## §4 Constitutional posture

- **R1 surface.** No Foundation modifications.
- **R2.** New namespace `raw/external/levenchuk-books-2026-05-20/`.
- **R6 provenance.** Per-extract citation [src: book.pdf page N].
- **R11.** Discovery-only; no operational application before Ruslan ack.
- **EP-5 F2.** Extraction = verbatim; commentary = derivative F2-F3.
- **Append-only.** Conversion outputs в new namespace; original PDF + TXT preserved untouched.

---

## §5 Pipeline target output

```
research/levenchuk-books-distillation-2026-05-20/
├── 00-SUMMARY-FOR-RUSLAN.md (entry ≤1000w)
├── 01-sistemnoe-myishlenie-2024-tom-1.md (TOC + chapter highlights)
├── 02-sistemnoe-myishlenie-2024-tom-2.md
├── 03-metodologiya-2025.md
├── 04-intellekt-stek-2023.md
├── 05-injeneriya-lichnosti.md
├── 06-cross-link-к-jetix-substrate.md (matrix: 4 books × Jetix sources)
├── 07-DE-RU-terminology-glossary.md (Левенчук terms cross-cite к 3 K-6 Tier A wikis)
└── diagrams/ — mermaid (corpus overview / cross-link map / chapter heatmap)

raw/external/levenchuk-books-2026-05-20/
└── converted/
    ├── 01-sistemnoe-myishlenie-2024-tom-1.md (full conversion)
    ├── 02-sistemnoe-myishlenie-2024-tom-2.md
    ├── 03-metodologiya-2025.md (CP1251→UTF-8 fixed)
    ├── 04-intellekt-stek-2023.md
    └── 05-injeneriya-lichnosti.md
```

---

*Vendored 2026-05-20. Ready для Step 3 distillation server CC autonomous run.*
