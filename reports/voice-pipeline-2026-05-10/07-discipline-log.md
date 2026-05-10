---
title: Discipline log — voice pipeline 2026-05-10
type: pipeline-discipline-log
lens: tseren-video-2026-05-10
created: 2026-05-10T05:22:08
output_dir: reports/voice-pipeline-2026-05-10
---

# Discipline log — voice-pipeline 2026-05-10

> Provenance + per-stage pass/fail + self-eval. Append-only artefact.

## Stage 1 — Transcribe (wraps tools/transcribe.py)
**started:** 2026-05-10T03:24:02
- transcripts existing: 0; need transcribing: 47
- transcribe.py exit=0
-     • audio_630@09-05-2026_05-39-09.ogg
-         транскрипт: /home/ruslan/jetix-os/raw/transcripts/audio_630@09-05-2026_05-39-09.txt
-         архив:      /home/ruslan/jetix-os/raw/voice-memos/audio_630@09-05-2026_05-39-09_1778383521.ogg
-     • audio_631@09-05-2026_07-42-38.ogg
-         транскрипт: /home/ruslan/jetix-os/raw/transcripts/audio_631@09-05-2026_07-42-38.txt
-         архив:      /home/ruslan/jetix-os/raw/voice-memos/audio_631@09-05-2026_07-42-38_1778383522.ogg
-     • audio_632@09-05-2026_08-23-51.ogg
-         транскрипт: /home/ruslan/jetix-os/raw/transcripts/audio_632@09-05-2026_08-23-51.txt
-         архив:      /home/ruslan/jetix-os/raw/voice-memos/audio_632@09-05-2026_08-23-51_1778383523.ogg
-     • audio_633@10-05-2026_03-53-44.ogg
-         транскрипт: /home/ruslan/jetix-os/raw/transcripts/audio_633@10-05-2026_03-53-44.txt
-         архив:      /home/ruslan/jetix-os/raw/voice-memos/audio_633@10-05-2026_03-53-44_1778383525.ogg
-   Пропущено (уже есть): 2
-     • audio_528@24-04-2026_02-06-44.ogg
-     • audio_529@24-04-2026_02-48-43.ogg
**stage 1 verdict:** `PASS`
  - transcribed: 47
  - skipped: 0
  - failed: 0
  - dups_cleaned: 47
  - success_rate: 100.0%
**completed:** 2026-05-10T03:25:25

## Stage 2 — Extract + validator (wraps tools/extract.py)
**started:** 2026-05-10T03:25:25
- extractions existing: 0; need: 47
- extract.py exit=0
-     • audio_579@29-04-2026_22-00-03.txt
-     • audio_580@29-04-2026_22-25-32.txt
-     • audio_581@29-04-2026_22-36-20.txt
-     • audio_582@30-04-2026_18-12-09.txt
-     • audio_583@30-04-2026_18-34-21.txt
-     • audio_584@30-04-2026_18-38-18.txt
-     • audio_585@30-04-2026_18-42-10.txt
-     • audio_586@30-04-2026_18-47-54.txt
-   
-   [crm-yaml] jetix-os/inbox/processed/extract-items-latest.yaml: 25 CRM item(s) (11 files с explicit crm_items, 2 fallback)
**stage 2 verdict:** `PASS`
  - memos_extracted: 47
  - total_items: 370
  - empty_memos: 0
  - success_rate: 100.0%
**completed:** 2026-05-10T04:04:43

## Stage 3 — Filter + frequency annotation (wraps tools/filter.py)
**started:** 2026-05-10T04:04:43
- filter.py exit=0
-     • Инфраструктурный долг: нет документа 'Кто я' (упоминается в контексте, не утверждён) и нет 'листа философии' / 'во что врезаюсь зубами' — три разных артефакта одного семейства, имеет смысл объединить в одну систему повседневных якорей в Life OS
-     • Дублирующих с принятыми решениями нет — ни одна заметка не повторяет уже зафиксированное решение из контекста (всё новое)
-     • OnlyFans-кластер (audio_625) — изолированный backlog, безопасно отложить; не трогать пока не валидирован основной путь
-     • Самонаблюдение про ночное состояние записи (audio_629) поднят priority до high — это критический guardrail на принятие решения об увольнении
-     • Самый горячий actionable-трек этой партии: подготовка предложения Церину (айтемы 24-29, 31) — concrete next step для Быстрых денег P1, требует немедленной материализации в текстовый документ.
-     • Концепция 'мировые рекорды' (айтем 29) — потенциально новый нарратив бренда, ещё не зафиксированный в принятых решениях контекста; требует решения owner: фиксируем как часть позиционирования или нет.
-     • Кластер 'Мастерская как платформа' (айтемы 13-23) — крупная стратегическая идея на стыке Life OS и Бренд; не для срочного движения, но требует решения owner о приоритете проекта (P3 Life OS текущий).
-     • Каскад оферов + ежедневный аутрич (айтемы 3, 4, 9, 10) — операциональная процедура для Быстрых денег, нуждается в фиксации как SOP-документ (айтем 8 уже это формулирует как задачу).
-     • Метапринцип 'письменная подготовка перед устным выходом' (айтемы 28, 30, 33, 34) — повторяющийся сигнал; стоит зафиксировать как Tier-1 принцип в personal workflow.
-     • Контакт 'Церин' — добавить в CRM как `crm/people/cerin-DRAFT.md` со статусом draft_from_voice (per voice-pipeline DRAFT-only discipline).
- filter output: batch_2026-05-10.json
**stage 3 verdict:** `PASS`
  - items_in: 1635
  - items_out: 1627
  - dedup_ratio: 0.5%
  - annotated_path: reports/voice-pipeline-2026-05-10/_filtered-annotated.json
**completed:** 2026-05-10T05:22:07

## Stage 4 — Per-note breakdown
**started:** 2026-05-10T05:22:07
**stage 4 verdict:** `PASS`
  - memos_with_sections: 47
  - nothing_extractable: 0
  - items_summarized: 137
  - verbatim_quotes: 0
  - size_kb: 71.7
**completed:** 2026-05-10T05:22:07

## Stage 5 — Wiki candidates extraction
**started:** 2026-05-10T05:22:07
**stage 5 verdict:** `PARTIAL`
  - total: 1285
  - match_to_existing: 0
  - propose_new: 1285
  - match_rate: 0.0%
  - size_kb: 54.8
**completed:** 2026-05-10T05:22:08

## Stage 6 — Current-lens filter (lens=tseren-video-2026-05-10)
**started:** 2026-05-10T05:22:08
**stage 6 verdict:** `PASS`
  - items_scored: 1627
  - items_above_threshold: 48
  - items_in_top_n: 20
  - threshold: 0.6
  - size_kb: 14.9
**completed:** 2026-05-10T05:22:08

## Stage 7 — Multi-output assembly
**started:** 2026-05-10T05:22:08
**stage 7 verdict:** `PASS`
  - files_written: 4
  - total_size_kb: 277.9
**completed:** 2026-05-10T05:22:08

## Self-evaluation (PLAN.md §4 quality criteria)
- **All 47 memos transcribed (≥95%):** ✅ PASS — 47/47 = 100%
- **Every memo has §-section in 01-per-note-breakdown.md:** ✅ PASS — 47/47 sections; nothing-extractable=0
- **Wiki candidates ≥30% match-to-existing OR <10 candidates:** ❌ FAIL — match_rate=0% (0 match / 1285 propose)
- **Top-N items have provenance + score breakdown:** ✅ PASS — top-N count: 20 (above threshold: 48)
- **No silent merges to wiki/:** ✅ PASS — verified by `git diff --stat origin/main -- 'wiki/**'` (zero changes)
- **Append-only — existing review_*.md preserved:** ✅ PASS — no modifications to reports/review_2026-04-* / review_2026-05-01-*
- **Every file ≤150 KB; total ≤500 KB:** ✅ PASS — see file inventory in 00-MASTER-INDEX.md
- **07-discipline-log.md captures honest pass/fail:** ✅ PASS — this very file is the artefact
