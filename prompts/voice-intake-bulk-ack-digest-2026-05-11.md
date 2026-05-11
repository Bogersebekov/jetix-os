# Voice Intake + Bulk-Ack + ФАЗА 4 Prep — Sequenced Pipeline

> **Создано:** 2026-05-11 evening.
> **Назначение:** обработать новые Telegram voice memos (post 30.04 18:47) → bulk-ack combined edges → wiki digest для ФАЗА 4.
> **Особенность:** 6 шагов с **STOP-checkpoints** — CC ждёт Ruslan ack после каждого шага, НЕ ломит всё подряд.
> **Notion parent:** `35c2496333bf81c88389fb2cd0ec90a8` Daily Log 11.05.

---

## Команды запуска

### Шаг 0 — Загрузить voice memos на сервер (Ruslan, PowerShell)

```powershell
$src = "D:\Downloads\Telegram Desktop\ChatExport_2026-05-11\chats\chat_562952475202217\topic_34\voice_messages"
$dst = "C:\Users\49152\Desktop\jetix-os\inbox\voice"
mkdir -Force $dst | Out-Null

$counter = 600
foreach ($f in Get-ChildItem $src -File | Sort-Object LastWriteTime) {
  $ts = $f.LastWriteTime.ToString("dd-MM-yyyy_HH-mm-ss")
  Copy-Item $f.FullName -Destination "$dst\audio_${counter}@${ts}$($f.Extension)" -Force
  $counter++
}

cd C:\Users\49152\Desktop\jetix-os
git stash push -m "pre-pull-voice-batch" wiki/index.md wiki/log.md 2>$null
git pull origin main
git add inbox/voice/
git commit -m "[raw] voice memos Telegram pull batch May — $((Get-ChildItem $dst -File).Count) audio files для Шаг E"
git push origin main
```

### Шаг 0.5 — Pull на сервере (где Antigravity / Claude Code открыт)

```bash
cd ~/jetix-os && git pull origin main
```

### Шаг 0.6 — Запустить CC (если не запущен)

```bash
tmux attach -t pdf-conversion   # or any session
# OR new:
tmux new -s voice-intake
claude --dangerously-skip-permissions
```

### Шаг 0.7 — Paste prompt в CC

```
Прочитай prompts/voice-intake-bulk-ack-digest-2026-05-11.md полностью. Извлеки секцию между маркерами ===PROMPT=== и ===END PROMPT===. Выполни sequence STRICTLY со STOP-checkpoints — после КАЖДОГО Шага ОСТАНАВЛИВАЙСЯ и жди explicit Ruslan ack ПЕРЕД продолжением. GO.
```

---

===PROMPT===

Sequenced voice intake + bulk-ack + ФАЗА 4 prep.

**КРИТИЧНО:** после КАЖДОГО Шага A-E — ОСТАНАВЛИВАЙСЯ + жди explicit Ruslan ack. НЕ продолжай автоматом. Это его decision point на каждом этапе.

## Контекст

- Wiki state: 722 entries / 609 canonical edges / 133 staged gamification edges
- 137 Tier A v3 voice candidates pending (Stage 2A v3 batch 10.05)
- Ruslan upload'ил новые voice memos в `inbox/voice/` (Telegram batch May, post 30.04)
- Цель: incremental processing с Ruslan ack point на каждом этапе

## Pre-flight check

1. `ls inbox/voice/*.ogg inbox/voice/*.mp3 | wc -l` → confirm new audio count
2. `du -sh inbox/voice/` → total size
3. Surface: «Found N new audio files (X MB total) в inbox/voice/. Готовы к Шагу A?»
4. **STOP** — wait Ruslan «GO» before starting Шаг A

---

## ШАГ A — Transcribe + Extract + Summarize (~30-45 min)

```bash
bash tools/run_pipeline.sh
```

Pipeline auto-runs:
- Step 0: sync_context
- Step 1: transcribe.py (Groq Whisper) → `raw/transcripts/audio_NNN@DATE.txt`
- Step 2: extract.py (Claude) → `inbox/processed/extract-items-latest.yaml`
- Step 2b: CRM voice routing (DRAFT-only auto)
- Step 3: summarize.py → `~/summary-latest.md`

Output check:
- Each .ogg → .txt should exist
- extract-items-latest.yaml — valid YAML, items count > 0
- summary-latest.md — readable, mentions top themes

Commit + push:
```
[voice-pipeline] Шаг A done — N memos transcribed + extracted + summarized (May batch)
```

### 🔴 CHECKPOINT A — STOP

Surface to Ruslan:
- Transcribed: N memos (list count + 5 sample slugs)
- Extracted: M structured items
- Summary highlights (top 3 themes from summary-latest.md)
- Status: «Готов к Шагу B (filter + review report) — нужен твой ACK»

**ОСТАНАВЛИВАЙСЯ.** НЕ продолжай. Жди Ruslan «ACK A, продолжай Шаг B» (или corrections).

---

## ШАГ B — Filter + Review Report (~15-20 min)

```bash
bash tools/run_filter.sh
```

Auto-runs:
- filter.py — dedup + meta-analysis (Claude)
- review_report.py → `reports/review_2026-05-11-may-batch.md`

Output: review report с:
- Top themes (5-10)
- Surprising findings (3-5)
- Recurring concepts
- Priority/tier estimates per item
- Skipped items (with reason)

Commit + push:
```
[voice-pipeline] Шаг B done — review report May batch, N items filtered, top themes surfaced
```

### 🔴 CHECKPOINT B — STOP

Surface to Ruslan:
- Total items processed: M
- Skipped: K (with reasons categorized)
- Top 5 surprising findings (verbatim from report)
- New themes vs existing wiki: list which themes already covered, which are NEW
- Status: «Готов к Шагу C (LLM rerank → wiki candidates) — нужен твой ACK»

**ОСТАНАВЛИВАЙСЯ.** Жди Ruslan «ACK B, продолжай Шаг C» (или «скипни memo X» / «продолжай с тем что есть»).

---

## ШАГ C — Stage 5 LLM Rerank → Wiki Candidates (~20-30 min)

```bash
python3 -m tools.wiki_integration._rerun_stage5_may_batch
```
(если script не существует — adapt из `_rerun_stage5_v3.py` для new batch input path; same methodology: BM25 prefilter top-10 + Claude Sonnet 4.6 LLM rerank batch=8, thresholds A≥0.85 / B≥0.60).

Output: `reports/voice-pipeline-2026-05-11-may-batch/04-wiki-candidates.md` + `.json` sidecar.

Format: same as Stage 2A v3 (Tier A/B/C tables per item with memo refs, score, rationale).

Quality check:
- match-rate (A+B) sane (40-65% expected)
- fallback to BM25 rate < 5%
- 0 contradicts к 6 Hexagon insights

Commit + push:
```
[voice-pipeline] Шаг C done — Stage 5 LLM rerank May batch, Tier A N / B M / C K (match-rate X%)
```

### 🔴 CHECKPOINT C — STOP

Surface to Ruslan:
- Tier breakdown (A/B/C counts)
- Match rate vs Stage 2A v3 baseline (60.1%)
- Top 10 Tier A candidates (verbatim — strongest semantic matches)
- Top 3 anti-pattern surfaces (если есть)
- Status: «Готов к Шагу D (Combined Bulk-Ack) — нужен твой ACK»

**ОСТАНАВЛИВАЙСЯ.** Жди Ruslan «ACK C, продолжай Шаг D» (или «подправь эти 2 candidates» / «скипни этот»).

---

## ШАГ D — Combined Tier A Bulk-Ack (~30-40 min)

3 батча вместе → canonical `edges.jsonl`:
1. **137 Tier A v3 voice** (Stage 2A v3 10.05)
2. **M Tier A new** (May batch — per Шаг C)
3. **133 gamification staged** (Шаг C done) — per Decision 4 staged ready для canonical promotion

Sequence:
```
/wiki-bulk-ack --tier A --version v3 --dry-run                    # preview batch 1
# wait ack
/wiki-bulk-ack --tier A --version v3                              # execute batch 1

/wiki-bulk-ack --tier A --batch may-2026 --dry-run                # preview batch 2
# wait ack
/wiki-bulk-ack --tier A --batch may-2026                          # execute batch 2

/wiki-bulk-ack --batch gamification --tier A,B,C --dry-run        # preview batch 3
                --staged-file wiki/graph/edges-gamification-pending-2026-05-11.jsonl
# wait ack
/wiki-bulk-ack --batch gamification --tier A,B,C                  # execute batch 3
                --staged-file wiki/graph/edges-gamification-pending-2026-05-11.jsonl
```

Result: `edges.jsonl` 609 → ~880-930 canonical (dedup applies).

Commit + push:
```
[wiki] Шаг D Combined Tier A bulk-ack done — voice v3 (137) + may-batch (M) + gamification staged (133) → edges.jsonl X→Y
```

### 🔴 CHECKPOINT D — STOP

Surface to Ruslan:
- Edges before: 609
- Edges after: Y (delta +Z)
- Per-batch breakdown (voice v3 acked / may-batch acked / gamification staged promoted)
- Dedup events (если есть)
- Constitutional check: 0 contradicts к Hexagon
- Status: «Готов к Шагу E (Wiki digest для ФАЗА 4) — нужен твой ACK»

**ОСТАНАВЛИВАЙСЯ.** Жди Ruslan «ACK D, продолжай Шаг E» (или «откати batch X» — git revert).

---

## ШАГ E — Wiki Digest для ФАЗА 4 (~15-30 min)

Build: `reports/phase-4-wiki-digest-2026-05-11.md`

Структура digest:

§1 6 Realm entity stubs (current state, verbatim из `wiki/concepts/jetix-realm/e1-persona.md ... e6-seasons.md`)

§2 Top 20 converged questions из Шаг D Question Mining
- per Q: short text + best variant (highest confidence)
- short rationale + ≥2 wiki refs

§3 Top 10 diverged questions из Шаг D
- per Q: short text + variants spread summary
- explicit «нужен Ruslan strategize» flag

§4 8 surprising findings (5 Шаг D + 3 Шаг C)
- verbatim from run reports

§5 9 anti-pattern claims (must avoid в Realm design)
- list with rationale + wiki refs

§6 Cross-domain synthesis (key insight clusters)
- from `wiki/summaries/gamification-cross-domain-synthesis-2026-05-11.md`

§7 May batch new insights (top themes which are NEW vs existing wiki)
- highlight what May batch surfaced that wasn't in Шаг C/D output

§8 Canonical anchor excerpts
- Strategic Insight Gamified Platform §4.2 (6 entities canonical)
- Document 1B 8 faces + Партнёр/Клиент/Работник tiers
- Workshop concept (5 owner roles)
- TRM model (6 resources × L0-L5)

§9 Open items requiring Ruslan strategize в ФАЗА 4
- Top 5 most-critical decisions

Цель digest: ОДНА concentrated reference doc с которой Ruslan начнёт писать FINAL Realm spec в ФАЗА 4. Минимум 2000 строк / max 5000 — comprehensive но focused.

Commit + push:
```
[phase-4-prep] Шаг E done — Wiki digest для Ruslan-words FINAL Realm spec (§1-9, X строк)
```

### 🔴 CHECKPOINT E — STOP

Surface to Ruslan:
- Digest path: `reports/phase-4-wiki-digest-2026-05-11.md`
- Total lines / sections covered
- 3 most-critical open items (что в digest §9)
- Status: «Digest готов. Открывай в Antigravity / Obsidian / GitHub. Чи­тай — потом ФАЗА 4 (Ruslan-words FINAL spec).»

**ОСТАНАВЛИВАЙСЯ.** Жди Ruslan «ACK E, я читаю digest». ФАЗА F = Ruslan strategizes, AI=scribe only.

---

## Constitutional Posture

- **F2 blast-radius** на Шаги A-E (voice pipeline + bulk-ack + reports/)
- **AI = scribe** (Tier 2 R1) — даже в Шаге E digest = factual extraction, NO strategic prose
- **Tier 2 R2** — NO writes к Foundation / principles / .claude/config / shared/schemas / CLAUDE.md / decisions/ во время Шагов A-E
- **Tier 2 R6** — provenance preserved (memo refs + audio IDs + commit SHAs)
- **Tier 2 R7** — 0 contradicts edges к 6 Hexagon insights (halt-log-alert если попытка)
- **Append-only** к wiki/ + reports/ + raw/transcripts/ + edges.jsonl
- **Halt-log-alert** при violations (write к forbidden path / contradicts к Hexagon / etc.)

## Hard Stops

- Wall-clock > 4h всё шаги вместе → auto-pause + checkpoint
- Stage 5 LLM rerank confidence:low > 25% → PAUSE (quality drop)
- Bulk-ack без dry-run OK → ABORT
- ANY contradicts edge к Hexagon → halt-log-alert
- Skip ЛЮБОЙ STOP-checkpoint без Ruslan ack → halt-log-alert (constitutional violation)

## Wall-clock Estimate

| Шаг | Target | Notes |
|---|---|---|
| A Transcribe+Extract | 30-45 min | depends on count |
| B Filter+Review | 15-20 min | quick |
| C Stage 5 rerank | 20-30 min | LLM-bound |
| D Bulk-ack | 30-40 min | 3 batches |
| E Digest | 15-30 min | concentrated write |
| **Total active** | **~2-2.5h** | + Ruslan review time между checkpoints |

**Ruslan review time:** variable — потенциально 10-30 min per checkpoint (5 checkpoints = 50-150 min). Возможно растянется на полдня-сутки calendar time с реальными breaks.

## Background Mode

- Шаги A, B, C, D, E работают в background (CC processing) — не блокирует chat
- НО CC останавливается на каждом STOP-checkpoint и явно ждёт Ruslan ack
- Telegram push для catastrophic halt only (non-recoverable)

## Commit Pattern

Каждый Шаг — отдельный commit с pattern `[voice-pipeline] Шаг X done — <details>` или `[wiki] Шаг D ack'd — <details>`.

## Final Hand-back (after CHECKPOINT E ack)

Surface to Ruslan:
- 5 commits SHAs (Шаги A-E)
- GitHub URL digest
- Total stats: memos processed / candidates / edges / digest lines
- Next: ФАЗА 4 — Ruslan reads digest + writes FINAL Realm spec в `decisions/JETIX-REALM-FINAL-SPEC-2026-05-11.md` (prose_authored_by: ruslan, F: F5, status: LOCKED после ack)

After ФАЗА 4 — ФАЗА 5 (wiki cross-verify) + ФАЗА 6 (видео Цэрэну).

Constitutional preserved. AI = scribe. Ruslan = sole strategist.

GO. Жгу с STOP-checkpoints до конца.

===END PROMPT===
