---
id: stage-3-synthesize-readme
title: Stage 3 Synthesize — Master Index (3 parallel writers)
date: 2026-04-21
type: prompt-index
status: ready
---

# Stage 3 Synthesize — Master Index

## Контекст

После Stage 1 (Untangle → 3626 atoms), Stage 2 (Resolve → 18 locked decisions), и Stage 2B (Holding Vision integration → 6 additional locked decisions 19-24), **критический путь разблокирован**. Всего **24 locked decisions**. Время писать 3 фундаментальных документа через 3 параллельных Claude Code sessions на сервере.

**✅ Stage 3 ready to launch:** все 24 decisions LOCKED (including $1T trajectory, USB-C positioning, Matchmaker/Roy, ICP refinement, Token economy Option B, Open-source research).

**Триада:** D1 Vision (кто мы) → D2 Philosophy (как мы думаем) → D3 Plan (что мы делаем и когда). Mutually reinforcing.

**Notion page:** https://www.notion.so/3492496333bf812e8b62cbc61338ce06

---

## Три prompt файла

| # | Prompt | Document | Size target | ETA |
|---|---|---|---|---|
| 1 | [01-d1-vision-writer.md](01-d1-vision-writer.md) | JETIX-VISION.md | 15-25 pages | 4-5h |
| 2 | [02-d2-philosophy-writer.md](02-d2-philosophy-writer.md) | JETIX-PHILOSOPHY.md | 25-40 pages | 5-6h |
| 3 | [03-d3-plan-writer.md](03-d3-plan-writer.md) | JETIX-PLAN.md | 15-25 pages | 4-5h |

---

## Как параллелизация работает

### 3 CC sessions (разные)

Ruslan запускает 3 отдельные Claude Code sessions на сервере. Каждый получает один из промптов.

### Shared inputs

Все 3 writers читают **идентичный набор binding inputs**:

1. `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md` — 3626 atoms
2. `raw/research/architecture-variants-2026-04-22/KNOT-MAP.md` — navigation
3. `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` — 8 locked decisions
4. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` — ещё 10 locked decisions
5. **`raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md`** — 6 LOCKED decisions (19-24: Holding-scale $1T / USB-C / Matchmaker+Roy / ICP refinement / Tokens Option B / Open-source research).
6. **`raw/voice-memos-text/holding-vision-2026-04-21.md`** — 6 text voice-notes (PRIMARY source of Decisions 19-24, preserved Ruslan voice)
7. **`raw/research/architecture-variants-2026-04-22/HOLDING-VISION-SYNTHESIS.md`** — synthesis of 6 notes + 8 categorized insight groups + top 20 quotes + compatibility report
8. `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md` — 367 voice quotes
9. `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md` — cross-analysis (§5 top 50 quotes)
10. `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-COMMUNITY-ADDENDUM.md` — §7 top 15 quotes
11. `raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md` — inspiration (не binding)
12. `CLAUDE.md` — current configuration

**24 locked decisions OVERRIDE any conflicting atoms** (8 Pre-Stage-1 + 10 Stage 2 + 6 Stage 2B). Writers use locks as truth when atoms disagree.

### Independent writes

Каждый writer пишет **свой** файл:
- D1 writer → `decisions/JETIX-VISION.md`
- D2 writer → `decisions/JETIX-PHILOSOPHY.md`
- D3 writer → `decisions/JETIX-PLAN.md`

НЕ конфликт на данных (разные файлы). Но git concurrent push требует `git pull --rebase` перед каждым push.

### Multi-pass architecture

Каждый writer делает **3 passes**:

**Pass 1 — Skeleton:**
- Read all mandatory inputs
- Build section structure согласно document spec
- Insert anchor quotes from 65 top quotes (50 digest + 15 addendum)
- Rough content per section

**Pass 2 — Flesh:**
- Expand narrative между anchor quotes
- Add nuances, edge cases, per-archetype angles (D1) / mental models (D2) / phase detail (D3)
- Cross-check against 18 locked decisions
- Preserve Ruslan voice verbatim в цитатах

**Pass 3 — Coherence:**
- Read own siblings (D1 reads D2+D3 siblings after their Pass 2, etc)
- Flag any cross-document contradictions в stdout для Ruslan review
- Voice consistency check
- Final polish

### Subagents внутри каждого writer

Writers могут использовать subagents через Task tool для:
- Parallel section drafting (10 sections параллельно)
- Atom filtering (find all atoms с dimension=X)
- Quote selection (find top 20 quotes matching section)

Это ускоряет каждый writer с 8-10h до 4-5h.

---

## Output structure

```
decisions/
├── JETIX-VISION.md           ← D1 output
├── JETIX-PHILOSOPHY.md       ← D2 output
└── JETIX-PLAN.md             ← D3 output
```

Каждый с YAML frontmatter:
```yaml
---
id: jetix-vision | jetix-philosophy | jetix-plan
title: <full title>
date: 2026-04-21
type: vision | philosophy | plan
status: draft (pending Ruslan review)
binding: yes — foundational document
sources: [all 9 inputs listed above]
related_to: [other two D documents]
stage: 3 of 4
next: Stage 4 compress → D4 Architecture-Brief → Stage 6 6 architects
---
```

---

## Binding rules (non-negotiable)

1. **24 locked decisions override atoms** (18 confirmed + 6 Stage 2B once approved). Any contradiction — locks win.
2. **Preserve Ruslan voice verbatim** в direct quotes. Мат в цитатах сохраняется.
3. **Attribution обязательна** — каждый quote имеет transcript / wiki reference.
4. **OME-ARCHITECTURE-REFERENCE.md — inspiration, НЕ binding.** Writers integrate patterns where resonates, don't copy slavishly.
5. **Non-contradicting** — D1, D2, D3 внутренне consistent + между собой не противоречат (Pass 3 coherence check).
6. **Size targets в диапазоне** — слишком короткий = не deep enough; слишком длинный = bloat.
7. **Multi-pass обязательно** — первый draft никогда не финальный.

---

## После Stage 3

Ruslan reviews 3 drafts → approves / requests adjustments → Stage 4 starts (compress в D4 Architecture-Brief).

Stage 4 = 1 CC session compresses D1+D2+D3 в ~5000 слов binding input для 6 architects (Stage 6).
