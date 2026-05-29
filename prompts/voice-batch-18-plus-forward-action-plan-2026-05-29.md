---
title: Voice Batch 18 (3 заметки 16:03 29.05) + FORWARD ACTION PLAN (дальнейший план действий чтобы дальше выполнять)
date: 2026-05-29
type: server-cc-autonomous-prompt
prompt_class: voice-batch-quick-plus-forward-action-plan
audio_files:
  - raw/voice-memos/audio_2026-05-29_16-03-21.ogg (~1.3MB)
  - raw/voice-memos/audio_2026-05-29_16-03-26.ogg (~2.6MB)
  - raw/voice-memos/audio_2026-05-29_16-03-29.ogg (~1.0MB)
output_main_doc: decisions/strategic/FORWARD-ACTION-PLAN-2026-05-29.md
output_voice_doc: decisions/strategic/VOICE-BATCH-18-INSIGHTS-2026-05-29.md
output_reports_dir: reports/voice-batch-18-forward-plan-2026-05-29/
F: F2 (voice verbatim) + F3 (synthesis)
G: prompt-voice-batch-18-plus-forward-action-plan-2026-05-29
R: refuted_if_no_transcript_OR_no_3_voice_processed_OR_no_forward_action_plan_OR_LOCK_modified_OR_academic_rant_instead_of_executable_actions_OR_no_concrete_next_steps
constitutional_posture: R1 surface only + R6 verbatim preserve + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only + voice-pipeline DRAFT-only
roy_dispatch_target: brigadier + methodology-engineer + mgmt-expert + philosophy-expert + influence-ethics-expert (R12 paired auto-fire) + systems-expert + investor-expert
language: russian primary
mode: VOICE BATCH QUICK + FORWARD ACTION PLAN (extract insights → executable forward plan чтобы дальше выполнять адекватно)
runtime_target: 2-3h autonomous
audience_primary: Ruslan reads → дальше идёт ВЫПОЛНЯТЬ адекватно (concrete next actions, не очередной анализ)
density_mode: SUBSTANTIVE (НЕ MAX-density — Ruslan explicit: «дальше мы уже пойдём всё выполнять адекватно»; executable > volume)
---

# 🎯 Voice Batch 18 + FORWARD ACTION PLAN

## §0 КРИТИЧНО — что делаем (per Ruslan voice 29.05 ~16:10)

**Ruslan explicit ask:**

> «Вот все три заметки последние. Давай пуш на сервер сразу. Мне давай prompt для клауд кода, что я вытянул. На основе них нам уже дальнейший план составил действия, и дальше мы уже пойдём всё выполнять адекватно.»

### Translation в acceptance criteria

✅ **DO:**
- Process 3 new voice files (16:03:21 / 16:03:26 / 16:03:29)
- Вытянуть ВСЕ инсайты (extract everything — ideas / decisions / questions / hypotheses / actions)
- На их основе + existing substrate → **дальнейший план ДЕЙСТВИЙ** (executable forward plan)
- Концентрация на «что дальше ДЕЛАТЬ» — конкретные шаги, чтобы Ruslan пошёл выполнять адекватно
- Integrate с substrate: ACTION-PLAN-OUTREACH-FOCUS (vчера) + STRATEGIC-REPLAN + сегодняшняя цель (упаковка базовых документов для показа партнёрам)
- Несколько mermaid (3-5: insights map / forward action sequence / dependencies / next 7 days)

❌ **DON'T:**
- НЕ MAX-density блоат (Ruslan downshift — executable не volume)
- НЕ academic «pivot / explore / consider / leverage» rant
- НЕ очередной мета-анализ ситуации (это уже было в batch-17 ACTION-PLAN) — здесь FORWARD план: что РУКАМИ делать
- НЕ premature ranking «что важнее» (R1 surface; Ruslan picks)
- НЕ unsolicited alternatives к выбранным путям
- НЕ trogать Foundation / 4 LOCKED canonical (R2 STRICT)

---

## §1 Substrate (Phase 0 read mandatory)

### Voice files (3 new)

| File | Status |
|---|---|
| `raw/voice-memos/audio_2026-05-29_16-03-21.ogg` | NEW — transcribe + extract |
| `raw/voice-memos/audio_2026-05-29_16-03-26.ogg` | NEW — transcribe + extract |
| `raw/voice-memos/audio_2026-05-29_16-03-29.ogg` | NEW — transcribe + extract |

### Substrate docs (read для context)

- `decisions/strategic/ACTION-PLAN-OUTREACH-FOCUS-2026-05-28.md` (vчера — situation + documents filtered + action queue + outreach plan) ⭐ KEY
- `decisions/strategic/VOICE-BATCH-17-INSIGHTS-2026-05-28.md` (batch-17 insights)
- `decisions/strategic/STRATEGIC-REPLAN-2026-05-28.md` (re-plan)
- `decisions/strategic/VOICE-BATCH-16-INSIGHTS-2026-05-28.md`
- `daily-logs/_PLAN-OF-DAY-2026-05-29.md` (сегодняшняя цель: упаковка базовых документов для показа партнёрам — НЕ продажа, НЕ launch)
- `decisions/strategic/JETIX-METAPLAN-V4-FINAL-2026-05-26.md` (16 directions canonical)
- `decisions/strategic/JETIX-WORKSHOP-MASTERY-NETWORK-CONCEPT-2026-05-26.md` (Foundation metaphor)
- `decisions/strategic/LETTER-TO-TSEREN-RESPONSE-2026-05-26.md` (Tseren letter draft pending)
- `crm/` (180+ contacts — для outreach/partner mapping)

### Сегодняшний контекст (день 29.05)

День = **упаковка структуры базовых документов** для показа партнёрам/помощникам (НЕ продажа, НЕ launch). Forward action plan должен включать этот goal как primary thread + integrate новые инсайты из 3 заметок.

---

## §2 Phases (sequential, commit per phase, push at end)

### Phase 0 — Substrate read + FPF lens
- Read all substrate (§1)
- FPF lens: forward план = gap между state-now → target (партнёр-ready упаковка + outreach launch); actions = что закрывает gap
- Commit: `[voice-batch-18] Phase 0 substrate read + FPF lens`

### Phase 1 — Transcribe 3 voice
- `tools/transcribe.py` (Groq Whisper)
- Output: `raw/transcripts/audio_2026-05-29_16-03-*.txt`
- Commit: `[voice-batch-18] Phase 1 transcripts (3 voice 16:03)`

### Phase 2 — Extract ВСЕ insights + themes
- Per voice: structured items (idea / decision / question / hypothesis / action) — вытянуть ВСЁ
- CC headless (no Anthropic API key)
- Theme clustering
- Output: `reports/voice-batch-18-forward-plan-2026-05-29/01-extracted-items.md`
- Commit: `[voice-batch-18] Phase 2 extracted items + themes`

### Phase 3 — Dedup + R12 paired check + integrate substrate
- Dedup vs batch-12..17
- R12 paired-frame STRICT (influence-ethics auto-fire if propaganda/recruitment/nlp/gamification)
- Merge с ACTION-PLAN + STRATEGIC-REPLAN — combined forward picture
- Output: `reports/.../02-dedup-r12-integrated.md`
- Commit: `[voice-batch-18] Phase 3 dedup R12 + substrate integrated`

### Phase 4 — FORWARD ACTION PLAN (executable, что РУКАМИ делать)
**Tone:** «делай X, потом Y, для этого нужно Z». Конкретные actions, не анализ.

**Содержимое:**
- **Что нового дали 3 заметки** (delta — что изменилось / добавилось к плану)
- **Forward action sequence** — ordered list конкретных действий (что делать дальше, по порядку):
  - Per action: `[#] действие — кто (Ruslan / Cloud Cowork / Server CC) — est. time — что разблокирует — dependency`
  - Ordered by: что нужно сделать ПЕРВЫМ чтобы двигаться (unlock-first)
- **Интеграция с сегодняшней целью** (упаковка базовых документов для партнёров): какие actions относятся к packaging, какие к outreach, какие к остальному
- **Что НЕ делаем сейчас** (defer — чтобы не распыляться)

Output: `reports/.../03-forward-action-plan.md` (≤4000 слов)
Commit: `[voice-batch-18] Phase 4 forward action plan (executable)`

### Phase 5 — Базовые документы для партнёров (refine из сегодняшней цели)
- На основе инсайтов batch-18 + ACTION-PLAN documents-filtered: какие базовые документы нужны для показа партнёрам
- Per документ: что показывает / формат / статус substrate / est. time упаковки / writer (Ruslan-prose vs swarm-draft)
- Reading path для партнёра (с чего начать → куда углубиться)
- Output: `reports/.../04-partner-base-documents.md`
- Commit: `[voice-batch-18] Phase 5 partner base documents structure`

### Phase 6 — Mermaid suite (3-5 dense)
1. **Insights map** (batch-18 items → directions)
2. **Forward action sequence** (ordered actions + dependencies)
3. **Partner package structure** (документы + reading path)
4. **Next 7 days timeline** (Gantt-style)
5. (optional) **What unlocks what** (dependency graph)

Each ≥10 nodes, dense, light theme.
Output: `reports/.../diagrams/FP-1..FP-5.mmd` + INDEX
Commit: `[voice-batch-18] Phase 6 mermaid suite FP-1..FP-5`

### Phase 7 — Main doc + INSIGHTS + SUMMARY + INDEX + final push

**Main doc** `decisions/strategic/FORWARD-ACTION-PLAN-2026-05-29.md` (≤7000 слов):
- §0 TL;DR (60s — что нового из заметок, top 3 actions, что делаем сегодня)
- §1 Что дали 3 заметки (insights delta, ≤1200w)
- §2 Forward action sequence (executable, ordered, ≤2000w)
- §3 Базовые документы для партнёров (structure + reading path, ≤1500w)
- §4 Mermaid suite (3-5 inline/linked)
- §5 R1 decisions surface (≤8 — только то что Ruslan must ack для движения; pool discipline)
- §6 Cross-refs

**VOICE-BATCH-18-INSIGHTS** `decisions/strategic/VOICE-BATCH-18-INSIGHTS-2026-05-29.md`:
- Standard voice-batch format (batch-14..17 pattern), O-N items, R12 check, cross-batch dedup

**SUMMARY** `reports/.../00-SUMMARY-FOR-RUSLAN.md` (≤1000w human Russian, factual):
- 3 things: что нового / что делаем дальше (top actions) / какие документы упаковываем
- 1 mermaid overview

**INDEX** `reports/.../INDEX.md`

Commit: `[voice-batch-18] Phase 7 Main + INSIGHTS + SUMMARY + INDEX (final)`
**FINAL PUSH:** `git push origin main`

---

## §3 Operational rules

### Constitutional (STRICT)
- R1 surface only · R2 STRICT (Foundation / 4 LOCKED untouched) · R6 provenance per claim · R11 Default-Deny · R12 paired-frame auto-fire · IP-1 STRICT · append-only · voice-DRAFT-only (wiki/CRM proposals DRAFT, no auto-promote)

### NO MAX-density (overridden — Ruslan explicit downshift)
- «дальше мы уже пойдём всё выполнять адекватно» = executable focus, не volume
- Substantive depth в actions + partner docs; ≤7000w main, ≤1000w SUMMARY

### Git
- Commit per phase (8 commits: Phase 0-7); push only Phase 7 final
- NO `--no-verify` / `--force` / `--amend`
- Format: `[voice-batch-18] Phase N <description>`

### tmux session: `voice-batch-18-forward-plan-2026-05-29`

---

## §4 К чему ведёт

После Phase 7 push:
1. Cloud Cowork pull → surface SUMMARY ≤1000w + top actions
2. Ruslan reads → picks top action → **идёт ВЫПОЛНЯТЬ** (упаковка документов OR Tseren send OR outreach)
3. Forward план = executable roadmap на ближайшие дни
4. Foundation substrate untouched (R2 LOCK)
5. Pool result — NO auto-launch consequent

---

## §5 Acceptance criteria (self-check перед final push)

✅ 3 voice transcribed + ВСЕ insights extracted
✅ FORWARD-ACTION-PLAN-2026-05-29.md (≤7000w, executable не анализ)
✅ VOICE-BATCH-18-INSIGHTS-2026-05-29.md (standard format)
✅ Partner base documents structure (Phase 5)
✅ 6-7 phase reports + SUMMARY ≤1000w (human Russian factual)
✅ 3-5 mermaid FP-1..FP-N (dense)
✅ Forward actions ORDERED + executable (кто / time / unlock / dependency)
✅ R12 paired-frame applied
✅ R2 LOCK preserved
✅ Pool result discipline
✅ NO academic language / NO unsolicited alternatives
✅ Final push origin/main

---

*Prompt closure 2026-05-29. Voice-batch-18 (3 заметки 16:03) + FORWARD ACTION PLAN. Mode: substantive не MAX-density (Ruslan explicit downshift «пойдём выполнять адекватно»). Goal: вытянуть ВСЕ инсайты → executable forward action plan (что РУКАМИ делать, ordered, unlock-first) + базовые документы для партнёров (today's goal) + 3-5 mermaid. R1 surface; R2 STRICT; R12 paired-frame STRICT; pool result. After finish — Cloud Cowork surfaces SUMMARY, Ruslan picks top action, идёт ВЫПОЛНЯТЬ.*
