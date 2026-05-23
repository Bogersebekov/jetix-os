---
title: Mistral OCR Full Pass — 11 scan books (4536 pages)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 4
ack_source: Ruslan voice 24.05 «все книги в MD + Mistral нехуй делать потом — сейчас»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: mistral-ocr-full-pass
R: refuted_if_lt_10_of_11_books_full_OCR_OR_LOCK_modified
constitutional_posture: R1 surface only + R2 + R6 + R11 + append-only
estimated_runtime: 30-90 min (Mistral OCR API ~1-3 sec/page × 4536 pages)
estimated_cost: ~$5 (Mistral OCR pricing)
language: russian primary
priority: ⭐⭐⭐ PRE-research enhancement — upgrades 11 partial OCR books to full coverage
parent_pipeline_output: reports/research-corpus-pipeline-2026-05-24/phase-3-ocr-log.md
parent_ack: Ruslan voice 24.05 ack-all P1 decisions
ram_constraint: low (API calls, не CPU-bound) — OK parallel с research prompts
---

# 🔬 Mistral OCR Full Pass — 11 Scan Books

> **Trigger:** Ruslan ack-all P1 decisions. Pipeline Phase 3 OCR'd только partial 25 pp каждой (Tesseract free, time-bound). Mistral OCR = full coverage 4536 pages для downstream research prompts depth.

---

## §0 Pre-flight

1. **Memory:** constitutional + research-pool + no-unsolicited + fpf-first
2. **Substrate:**
   - Existing partial OCR MDs (Phase 3 Tesseract output)
   - 11 scan PDFs full text via Mistral OCR API
   - Existing Mistral OCR API integration (per `inbox-reocr-fresh.tar.gz` precedent — check if API key configured)
3. **Mistral OCR endpoint:** `https://api.mistral.ai/v1/ocr` (или similar — check current docs)
4. **API key:** check env / config (per `feedback_no_api_keys.md` — never commit; use existing key пути)

---

## §1 11 Books to OCR (priority order)

| Priority | Book | Pages | Bucket |
|---|---|---|---|
| ⭐⭐⭐ | dilts-delozier-encyclopedia-of-systemic-nlp-2000 | 1724 | nlp |
| ⭐⭐⭐ | goodfellow-deep-learning-2016 | 972 | sota |
| ⭐⭐ | schon-educating-reflective-practitioner-1987 | 384 | methodology |
| ⭐⭐ | hacking-representing-and-intervening-1983 | 306 | sota |
| ⭐ | laudan-progress-and-its-problems-1977 | 264 | sota |
| ⭐ | le-bon-the-crowd-1895 | 262 | propaganda-recruitment |
| ⭐ | bandler-grinder-trance-formations-1981 | 260 | nlp |
| ⭐ | bernays-crystallizing-public-opinion-1923 | 228 | propaganda-recruitment |
| ⭐ | bernays-propaganda-1928 | 158 | propaganda-recruitment |
| ⭐ | freud-group-psychology-1921 | 152 | propaganda-recruitment |
| ⭐ | dijkstra-short-intro-art-of-programming-1969 | 101 | methodology |

**Total: 4536 pages, ~$5 estimated.**

---

## §2 4 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + API key check + tool setup + cost estimate confirm | `reports/mistral-ocr-2026-05-24/phase-0-setup.md` |
| **1** | ⭐⭐⭐ **Mistral OCR full pass** all 11 books (sequential or parallel per API rate limits) | per-PDF `<bookname>-mistral.md` next to existing PDF + Tesseract MD (preserve both для comparison); phase log `01-ocr-log.md` |
| **2** | **Quality replace** — for each book если Mistral output > Tesseract partial coverage AND quality OK → overwrite primary `<bookname>.md` с Mistral version; preserve Tesseract version as `<bookname>-tesseract-partial.md` для audit | phase log `02-replace-log.md` |
| **3** | **Quality report + Summary** + final push | `00-SUMMARY-FOR-RUSLAN.md` (≤500w) с per-book status + final cost + page coverage |

---

## §3 Acceptance criteria

- ✅ 4 phases per-phase commit + push (format `[mistral-ocr] Phase N description`)
- ✅ Min **10 of 11** books full OCR successful
- ✅ Each book получает full-coverage MD (vs Tesseract partial 25 pp)
- ✅ Tesseract partial preserved для comparison/audit
- ✅ Cost actual ≤ $7 (budget $5 + 40% buffer)
- ✅ Per book: page count + char count + token count + quality grade reported
- ✅ R1 surface only — pure conversion; NO content interpretation
- ✅ NO LOCK content modifications
- ✅ Append-only

---

## §4 Operational

- Per-phase commit + push
- API key handling: check env / secret file; NEVER commit
- Russian + English MD output per book language
- R6 provenance per page: `[src: <bookname>.pdf p NNN]` inline где applicable
- Pool result only
- Fallback если Mistral API fails: stay with Tesseract partial (report which failed)

---

## §5 Final push

```bash
git add raw/external/research-corpus-2026-05-23/ inbox/ reports/mistral-ocr-2026-05-24/
git commit -m "[mistral-ocr] Phase 3 Quality report + final push (4 commits / NN/11 books OCR'd / ~\$N cost / NN pages → NN tokens)"
git push origin main
```

---

## §6 What this prompt does NOT do

- ❌ NOT process text PDFs (already done Phase 2 pipeline)
- ❌ NOT modify LOCKED content
- ❌ NOT trigger downstream research prompts
- ❌ NOT analyze book content

---

*Mistral OCR full pass — upgrade partial Tesseract MDs to full Mistral coverage. ~30-90 min / ~$5.*
