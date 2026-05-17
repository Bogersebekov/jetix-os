---
title: Voice pipeline 17.05 batch — FPF-lens filter + detailed work plan extraction
date: 2026-05-17 evening
type: deep-prompt
target: server CC (brigadier mode, autonomous, 30-60min)
batch: raw/voice-memos-2026-05-17-batch/ (5 audio, 16.05 13:46 → 17.05 19:49)
trigger: Ruslan request — voice memos обработать через FPF lens после Phase 0 reset
last_batch: 2026-05-16 (commit 2483e09); last timestamp 16.05.2026 12:20:35
language: russian
---

# DEEP PROMPT — Voice batch 17.05 через FPF lens + detailed work plan extraction

> **Ты = brigadier** (per `.claude/agents/brigadier.md`, opus). Multi-agent swarm. Constitutional: Tier 2 R1/R2/R6/R11 + append-only + no API keys.

> **ultrathink — extended thinking ON для всей сессии.**

---

## §0 Контекст

Phase 0 завершён сегодня (commit `f4ed2cf`): 14 объектов Jetix через FPF lens, comparison matrix, kasha cleanup flags, master document для L1. Reference frame теперь stable.

Новый voice batch (5 audio, period 16.05 13:46 → 17.05 19:49) **не обработан** через старый voice pipeline. Ruslan хочет обработать **через новую FPF-lens призму** — то что было до Phase 0 = старая каша, сейчас уже adequate framework.

**Files в `raw/voice-memos-2026-05-17-batch/`:**
- audio_669@16-05-2026_13-46-17.ogg (после Дмитрий call)
- audio_670@16-05-2026_15-00-42.ogg
- audio_671@17-05-2026_01-07-28.ogg (ночное)
- audio_672@17-05-2026_18-59-52.ogg (сегодня вечером — после Phase 0 review)
- audio_673@17-05-2026_19-49-05.ogg (последнее audio)
- **text_001@17-05-2026_22-00.md** — text note: «Trust mechanisms: money vs FPF / open data / role-based». Strategic insight потенциал (high). Pre-Stage-1 = skip Whisper, прямо в Stage 2 extract.

---

## §1 Цель — три параллельных выхода

### §1.1 Jetix track (FPF lens filter)
Что в voice memos mapping'ится на:
- **14 объектов** из `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` (per-object: O-01..O-14)
- **FPF primitives** (U.System / U.Role / U.Method / U.Commitment / etc.) — что Ruslan озвучил из FPF terms
- **L1 outreach** — что относится к Левенчуку / Цэрэну / Дмитрию (любые upcoming моменты сотрудничества)
- **R12 / Hexagon / адаптации** — новые extension surface'нутые

Output: `reports/voice-pipeline-2026-05-17-batch/03-fpf-lens-jetix-track.md`

### §1.2 Detailed work plan track
Любые упомянутые:
- **Конкретные действия / next steps** (что нужно сделать когда)
- **Vision / стратегические повороты** (новые направления)
- **Project / task additions** (что добавить в active work)
- **Blockers / зависимости** (что мешает / от чего ждём)
- **Cleanup actions** (LIVE-FLAG ICP fix? F-grade disclosure? и т.п.)

Output: `reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md` — структурировано по приоритету / timeline

### §1.3 Reflection / Self-OS track
Личное / эмоции / observations о Руслане-человеке (per `inbox/levenchuk-tg-2026-05-17.md` D-1 patterns + Self-OS spec v0):

Output: append-only к `decisions/REFLECTION-INBOX-2026-05-16.md` (продолжение существующего)

---

## §2 Pipeline (через swarm)

### §2.1 Stage 1 — Transcribe (deterministic) — audio only
- Use `tools/transcribe.py` (Groq Whisper API через cc_helper.py headless) OR `whisper.cpp` local (если cost cap)
- Output: `raw/voice-transcripts/audio_669-673-2026-05-17.md` (5 transcripts, Russian)
- **HARD constraint:** transcripts verbatim (Whisper output) — НЕ редактировать содержание, только обертка с timestamps
- **Text note `text_001@17-05-2026_22-00.md`** — skip Whisper, читать verbatim из markdown file (frontmatter `verbatim: true`)

### §2.2 Stage 2 — Extract (FPF-lens dispatch) — для каждого item (5 audio + 1 text = 6 items)
**Brigadier swarm dispatch** (3 cells параллельно на каждый transcript / text note):

| Cell | Mode | Filter task |
|---|---|---|
| `engineering-expert × integrator` | FPF mapping | Найди FPF primitives / Jetix objects (O-01..O-14) упомянутые / производные |
| `mgmt-expert × integrator` | Work plan | Извлеки concrete actions / next steps / vision / blockers |
| `philosophy-expert × critic` | Reflection | Mark items как self-OS / эмоции / observations о Ruslan — НЕ Jetix |

**Special handling для text_001** — Strategic insight potential (high per author hint). Все 3 cells должны treat seriously: предложить Hexagon H8 candidate / route к O-11+O-13+O-14 / surface new direction если соответствует. НЕ dismissing как «just reflection».

Cell drafts: `swarm/wiki/drafts/task-voice-pipeline-2026-05-17-*-audio_NNN.md` + `task-voice-pipeline-2026-05-17-*-text_001.md`

### §2.3 Stage 3 — Brigadier integrate
- 3 параллельных outputs per audio → integrate через AP-6 (dissent preservation если cells disagree)
- §5.5.5 provenance gate (6-check)
- Route to 3 output files §1.1/§1.2/§1.3

### §2.4 Stage 4 — Wiki candidates + cross-refs
- Tier A/B/C classification per existing `wiki-bulk-ack` discipline
- Cross-refs к Phase 0 objects + Phase A+B reports + Foundation Parts
- Output: `reports/voice-pipeline-2026-05-17-batch/05-wiki-candidates.md` (Ruslan ack required перед promotion)

### §2.5 Stage 5 — Master index + checkpoint
- `reports/voice-pipeline-2026-05-17-batch/00-MASTER-INDEX.md` — TOC + summary
- `reports/voice-pipeline-2026-05-17-batch/01-per-note-breakdown.md` — per-audio detailed
- `reports/voice-pipeline-2026-05-17-batch/06-meta-analysis.md` — patterns / themes / red-flags

---

## §3 Что должно быть в каждом output

### §3.1 `03-fpf-lens-jetix-track.md`
| Audio | Timestamp | Jetix object | FPF primitive | Quote | Action item |
|---|---|---|---|---|---|
- Per item: F-G-R triple
- Cross-ref к Phase 0 object number
- Если item не mapping'ится → flag как «possibly new direction»

### §3.2 `04-detailed-work-plan.md`
Структура:
- **Immediate (24-48h)** — что критично сделать
- **Short-term (week)** — этой недели
- **Strategic (month+)** — Phase C / future
- **Blockers** — что мешает
- **Decisions needed** — Ruslan ack требуется
- Plus mermaid: timeline / priority matrix

### §3.3 Reflection append к `decisions/REFLECTION-INBOX-2026-05-16.md`
- Per audio: эмоциональные состояния / patterns / observations
- НЕ Jetix-стратегия (туда §3.1)

---

## §4 Quality / acceptance

- [ ] 5 transcripts created (`raw/voice-transcripts/`)
- [ ] 3 output tracks готовы
- [ ] Per item F-G-R + provenance (audio:timestamp)
- [ ] Dissents preserved per AP-6
- [ ] Brigadier §5.5.5 provenance gate passed before canonical writes
- [ ] Wiki candidates table (Tier A/B/C)
- [ ] Master index + checkpoint
- [ ] git commits per Stage + final push origin main

---

## §5 Что НЕ делать

- НЕ trog'ать Foundation paths без AWAITING-APPROVAL
- НЕ promote wiki candidates автономно (Tier A — Ruslan ack)
- НЕ редактировать verbatim transcripts (только обертка)
- НЕ давать «§РЕКОМЕНДАЦИИ» — surface'инг variants только
- НЕ создавать новые strategic narratives — extract из voice, не authoring
- НЕ обходить cost cap (Groq Whisper ~€0.01/min, 5 audio ~5-15 min total ~€0.10)

---

## §6 Cost cap snapshot

- Daily €10 baseline
- Groq Whisper transcribe: ~€0.10 для 5 audio
- LLM cells (Claude Code Max headless): включено в subscription
- **Estimated total: <€1**

---

## §7 Context files (read first)

- `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` — текущий FPF-lens reference
- `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` — 14 objects table (filter target)
- `reports/voice-pipeline-2026-05-16-batch/00-MASTER-INDEX.md` — last batch output pattern
- `decisions/REFLECTION-INBOX-2026-05-16.md` — existing reflection inbox (append-only target)
- `inbox/levenchuk-tg-2026-05-17.md` — L1 context
- `CLAUDE.md` — pipeline conventions (§Voice-Notes Pipeline)
- `tools/run_pipeline.sh` — existing pipeline (use as reference / building block)

---

## §8 Acceptance criteria для Ruslan ack

В конце Phase + push:
- 5 transcripts visible
- 3 tracks (Jetix-FPF / work-plan / reflection) populated
- Wiki candidates Tier A/B/C table
- Master index ≤500 слов
- Ruslan читает Master + work-plan (5-10 мин) → ack tracks → реальные действия следующим шагом

---

**Launch:**

```bash
tmux new -s voice-17
cd ~/Desktop/jetix-os && git pull --ff-only && claude --dangerously-skip-permissions
```

Paste prompt:
```
ultrathink. Прочитай prompts/voice-pipeline-2026-05-17-fpf-filtered.md полностью. Ты — brigadier Jetix swarm. Обработай 5 audio в raw/voice-memos-2026-05-17-batch/ через FPF lens (Phase 0 14 objects как target) + extract detailed work plan + route reflection items append-only. Three parallel cells per audio (eng-integrator FPF / mgmt-integrator work-plan / phil-critic reflection). §5.5.5 provenance gate перед canonical writes. Brigadier integrates с dissent preservation. R1 + R2 preserved. Действуй автономно 30-60 минут, коммить per stage, push origin main в конце.
```

Detach: `Ctrl+B затем D`.
