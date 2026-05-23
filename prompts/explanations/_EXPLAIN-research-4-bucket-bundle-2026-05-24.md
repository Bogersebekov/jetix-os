---
title: EXPLAIN — 3-Bucket Research Bundle (Propaganda+Recruitment / SOTA / Methodology)
date: 2026-05-23
type: prompt-explanation
prompt_files:
  - prompts/research-propaganda-recruitment-2026-05-24.md
  - prompts/research-sota-2026-05-24.md
  - prompts/research-methodology-2026-05-24.md
audience: Ruslan (R1 pre-launch ack)
language: russian primary
---

# 📋 EXPLAIN — 3-Bucket Research Bundle

## §1 Что у нас есть СЕЙЧАС

- ✅ POINT-B-FOCUSED-WEEK-1 plan locked (Step 1 = Research)
- ✅ Books list создан (`RESEARCH-BOOKS-TO-DOWNLOAD-2026-05-23.md`)
- ✅ Folder structure ready: `raw/external/research-corpus-2026-05-23/{propaganda-recruitment,sota,methodology}/`
- ⏳ Ruslan скачивает books → положит в folders → push → launch 3 prompts

---

## §2 Что делают 3 prompts

**3 parallel deep research prompts** через linzu Jetix:

| Prompt | Phases | Runtime | Cost | Output |
|---|---|---|---|---|
| **propaganda-recruitment** | 9 | 6-10h | <€3 | `RESEARCH-PROPAGANDA-RECRUITMENT-2026-05-24.md` (~15-20K / 10-15 mermaid) |
| **sota** | 8 | 5-8h | <€3 | `RESEARCH-SOTA-2026-05-24.md` (~12-18K / 8-12 mermaid) |
| **methodology** | 9 | 6-10h | <€3 | `RESEARCH-METHODOLOGY-2026-05-24.md` (~18-25K / 10-15 mermaid) |

**Total:** ~17-28h compute, <€9 cost, 3 main deliverables + sub-reports + Summary each.

**Каждый prompt включает Jetix Lens phase** (Phase 7-8 в каждом) — что Jetix может применить + что нельзя (R12 boundary) + extension proposals.

---

## §3 Sequence + parallel strategy

### RAM constraint:
- **propaganda-recruitment** = heavy ROY 500%
- **sota** = medium-heavy
- **methodology** = heavy ROY 500%

⚠️ 3 одновременно = OOM risk (5 параллельных = crash 22.05 precedent).

### Recommended launch sequence

**Option A (safest, sequential):**
- Launch 1: methodology (largest scope; gives most)
- Launch 2: propaganda-recruitment (after #1 finishes)
- Launch 3: sota (after #2 finishes)
- Total wall-clock: ~17-28h sequential

**Option B (2-parallel, faster):**
- Wave 1: methodology + sota (parallel — both finish ~6-8h)
- Wave 2: propaganda-recruitment (после Wave 1 finish)
- Total wall-clock: ~12-18h

**Option C (3-parallel, risky):**
- All 3 simultaneously
- Risk: OOM crash → re-launch needed
- Total wall-clock: ~10h if no crash

**Default proposal:** Option B (2-parallel) — best speed/safety tradeoff.

---

## §4 Что берёт каждый prompt на вход

**Common substrate (all 3):**
- Memory rules (max-density + constitutional + research-pool + breadth + fpf-first)
- Existing Jetix substrate (4 LOCKED canonical + 13 Tier A wikis + DR-38/40 main)
- Plan-of-Day 23.05 + Point B Focused Week 1
- Method V2 §J meta-method (для Jetix lens)

**Per-prompt corpus:**
- propaganda: `raw/external/research-corpus-2026-05-23/propaganda-recruitment/`
- sota: `raw/external/research-corpus-2026-05-23/sota/` + Левенчук corpus existing
- methodology: `raw/external/research-corpus-2026-05-23/methodology/` + Левенчук corpus + FPF-Spec

---

## §5 Что получим на выходе (consolidated)

**Per research bucket:**
- Main deliverable (~15-25K consolidated)
- Per-phase reports
- Mermaid INDEX (8-15 diagrams)
- Summary для Ruslan (≤1500w)

**Combined value-add:**
- **Propaganda+Recruitment** → applicable techniques для Welcome-frame + cohort attraction (R12-safe) + EXPLICIT skip-list incompatible
- **SOTA** → как Jetix tracks SoTA + gaps + year-of-update mechanism + partner-facing SOTA claim discipline
- **Methodology** → Jetix positioning внутри methodology tradition (Russian Щедровицкий-Левенчук continuator analysis) + extension proposals back к tradition

---

## §6 К чему ведёт (downstream)

Эти 3 research feed Steps 2-8 в POINT-B-FOCUSED-WEEK-1:

- **Step 2** (Choose ideas + order) — methodology research informs которые idea anchors strongest
- **Step 3** (Запись + упаковка) — propaganda techniques applied для message framing (R12-safe)
- **Step 4** (Видео + сайт) — SOTA framing для credibility + propaganda для virality
- **Step 5** (Notion templates) — methodology research для template structure (methodology-engineering applied)
- **Step 6** (Tool Concept) — propaganda recruitment dynamics для pitch language
- **Step 7** (Testing Дмитрий+Сева) — recruitment patterns для conversion observation
- **Step 8** (Concretные предложения) — все 3 informers + Method V2 §J meta-method

---

## §7 Sequential launch commands

### Launch 1 — Methodology (largest)

```bash
ssh jetix
tmux new -s research-methodology
cd ~/jetix-os && git pull --ff-only
claude --dangerously-skip-permissions -p "$(cat <<'EOF'
Autonomous execution: prompts/research-methodology-2026-05-24.md

9 phases per-phase commit + push в формате [research-methodology] Phase N.
ROY 500%. MAX tokens × 3. Read entire books — Левенчук «Методология» + Polya 
«How to Solve It» + Senge «Fifth Discipline» + Beer «Brain of the Firm» + 
Ashby «Cybernetics» + Polanyi «Personal Knowledge».

Apply §4 §11.0 CRITICAL IMPORTANCE MANDATE FULL.
Phase 6 Russian methodology tradition DEEP (Щедровицкий + ШСМ + ОДИ + Левенчук continuator).
Phase 8 Jetix Lens — concrete positioning + extension proposals.

R6 provenance [src: book author page] per claim. R1 surface only (Ruslan owns positioning).
NO LOCK modifications. SKIP-list integrity. Pool result only.

10-15 mermaid. Final push: Phase 9 main + Summary + diagrams INDEX.
EOF
)"
# Detach: Ctrl-B then D
```

### Launch 2 — SOTA (parallel safe с methodology)

```bash
ssh jetix
tmux new -s research-sota
cd ~/jetix-os && git pull --ff-only
claude --dangerously-skip-permissions -p "$(cat <<'EOF'
Autonomous execution: prompts/research-sota-2026-05-24.md

8 phases per-phase commit + push в формате [research-sota] Phase N.
ROY 500%. MAX tokens × 3.

Apply §4 §11.0 CRITICAL IMPORTANCE MANDATE FULL.
Phase 1 Левенчук's SOTA concept deep decode.
Phase 6 SOTA как operational concept в МИМ (cross-cite Master Qualification article).
Phase 7 Jetix Lens SOTA — existing tracking + gaps + extension proposals.

R6 provenance per claim. R1 surface only. NO LOCK modifications.
SKIP-list integrity. Pool result only.

8-12 mermaid. Final push: Phase 8 main + Summary + diagrams INDEX.
EOF
)"
```

### Launch 3 — Propaganda+Recruitment (AFTER Wave 1 finishes)

```bash
ssh jetix
tmux new -s research-propaganda
cd ~/jetix-os && git pull --ff-only
claude --dangerously-skip-permissions -p "$(cat <<'EOF'
Autonomous execution: prompts/research-propaganda-recruitment-2026-05-24.md

9 phases per-phase commit + push в формате [research-propaganda] Phase N.
ROY 500%. MAX tokens × 3. Read entire books — Bernays «Propaganda» 1928 + 
Cialdini «Influence» + Lippmann «Public Opinion» + Hoffer «True Believer» + 
Lifton «Thought Reform» + Ellul «Propaganda».

Apply §4 §11.0 CRITICAL IMPORTANCE MANDATE FULL.
Phase 7 JETIX LENS — applicable techniques + EXPLICIT R12-incompatible skip-list.
R12 paired-frame STRICT THROUGHOUT — ZERO techniques violating R12.

R6 provenance per claim. R1 surface only. NO LOCK modifications.
SKIP-list integrity. Pool result only.

10-15 mermaid. Final push: Phase 8 main + Summary + diagrams INDEX.
EOF
)"
```

---

## §8 Готов?

После Ruslan скачает books + загрузит в folders + скажет «загрузил» → я push corpus → дам launch commands в правильном порядке.

---

*EXPLAIN closure 2026-05-23. Per `feedback_prompt_explanation_required.md`. 3 prompts bundle.*
