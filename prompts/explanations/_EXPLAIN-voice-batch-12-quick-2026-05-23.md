---
title: EXPLAIN — Voice Batch-12 QUICK prompt
date: 2026-05-23
type: prompt-explanation
prompt_file: prompts/voice-batch-12-quick-2026-05-23.md
audience: Ruslan (R1 pre-launch ack)
language: russian primary
---

# 📋 EXPLAIN — Voice Batch-12 QUICK

## §1 Что у нас есть СЕЙЧАС

- ✅ 3 audio files copied + renamed в `raw/voice-memos-2026-05-23-batch/`:
  - `audio_729@23-05-2026_18-50-30.ogg` (210K)
  - `audio_730@23-05-2026_18-50-35.ogg` (1.4M)
  - `audio_731@23-05-2026_18-50-40.ogg` (1.8M)
- Total ~3.4 MB / ~14-17 min audio
- Last processed: audio_728 (batch-11 closure)
- Точка А prompt running на сервере
- Точка Б prompt waiting на Точку А

---

## §2 Что делает этот prompt

**6 phases server CC autonomous** (1-2h LIGHT / <€1 / per-phase commit + push):
- Transcribe via Groq Whisper
- Per-audio 5-cell + FPF lens decode
- Extract 3-5 key ideas per audio (9-15 total)
- Surface pool candidates (Tier B / DR / Hypothesis)
- Surface wiki promotion suggestions
- Prepare integration note для Точка Б

**Mode: QUICK** — НЕ full 17-lens cross-analysis batch (тот = 6-10h). Speed > depth.

→ выдаёт integration-ready substrate для Точки Б Phase 6 + Plan-of-Day Шаг 3 brainstorm

---

## §3 Что берёт на вход

| Input | Откуда |
|---|---|
| 3 audio files | `raw/voice-memos-2026-05-23-batch/audio_729..731@*.ogg` |
| Last processed reference | audio_728 batch-11 |
| Pool current state | Tier B 73 / DR 38 / Hypothesis 33 |
| 13 LOCKED items preservation list | Substrate |
| Plan-of-Day 23.05 | `daily-logs/_PLAN-OF-DAY-2026-05-23.md` (context) |
| REFLECTION-INBOX recent | §APPEND-batch-10 + 11 |
| Memory rules | constitutional + research-pool + breadth + fpf-first + no-unsolicited |

---

## §4 Что обрабатывает (6 phases)

0. Pre-flight + inventory check
1. Transcribe 3 audio (Groq Whisper)
2. Per-audio 5-cell + FPF lens decode (verbatim + decode)
3. Key ideas extraction + pool candidates surface (3-5 per audio)
4. Wiki promotion candidates inventory (D12-* ack queue)
5. Point B integration note + Summary + final push

---

## §5 Что получим на выходе

| File | Что внутри |
|---|---|
| 3 transcripts | `raw/voice-transcripts/audio_729+.txt` |
| 3 per-audio MDs | `raw/voice-memos-2026-05-23-batch/audio_729+@*.md` |
| `01-per-note-breakdown.md` | 5-cell per audio = 15 datapoints |
| `02-key-ideas-pool-candidates.md` | 9-15 key ideas + suggested pool destinations |
| `03-wiki-promotion-candidates.md` | Wiki promotion suggestions (Tier A NEW / §APPEND existing / Tier B only) |
| `04-point-b-integration-note.md` | Note для Точка Б Phase 6 |
| `00-SUMMARY-FOR-RUSLAN.md` | ≤500w summary |
| REFLECTION-INBOX §APPEND-batch-12-quick | D12-* ack queue |

---

## §6 К чему ведёт

- **Feeds Точка Б Phase 6** — новые ideas integrated в Near Target description когда Точка Б runs
- **Feeds Plan-of-Day Шаг 3 Brainstorm directions** — новые idea seeds для direction generation
- **Pool additions** — Tier B / DR / Hypothesis pools обновлены
- **Wiki promotion D12-* ack queue** — surface для potential next-batch decisions
- **Continuity** — sequence audio_728 → 729-731 preserved

---

## §7 Mermaid flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
flowchart TB
    Audio[3 audio files<br/>audio_729-731<br/>~3.4 MB / ~14-17 min]
    Audio --> P1[Phase 1: Transcribe<br/>Groq Whisper]
    P1 --> P2[Phase 2: 5-cell + FPF lens decode<br/>per audio]
    P2 --> P3[Phase 3: Key ideas extraction<br/>3-5 per audio = 9-15 total]
    P3 --> P4[Phase 4: Wiki promotion<br/>candidates inventory]
    P4 --> P5[Phase 5: Point B integration note<br/>+ Summary + push]

    P5 --> Pool[Pool updates<br/>Tier B / DR / Hypothesis]
    P5 --> WikiQ[D12-* ack queue<br/>wiki promotion candidates]
    P5 --> PointB[Точка Б Phase 6<br/>integration ready]
    P5 --> Plan3[Plan-of-Day Шаг 3<br/>Brainstorm seeds]

    style P3 fill:#ffd6d6
    style PointB fill:#d6f0d6
    style Plan3 fill:#fff8d5
```

---

## §8 Дополнительные notes

- ⚠️ **NOT full batch-12 deep** — этот = QUICK; full deep можно сделать later если решишь
- ✅ Light prompt → OK parallel с Точка А (если ещё running) ИЛИ standalone
- ✅ Cost <€1 / 1-2h
- ✅ Per-phase commit = resumable
- ✅ Pool result only — никаких auto-promotion / auto-launch

---

## §9 Готов к launch?

После ack «погнали batch-12 quick» → дам launch command.

---

*EXPLAIN closure 2026-05-23. Per `feedback_prompt_explanation_required.md`.*
