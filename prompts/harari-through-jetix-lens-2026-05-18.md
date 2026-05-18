---
title: Yuval Noah Harari через Jetix lens — deep multi-book research
date: 2026-05-18
type: deep-prompt-author-lens
target: server CC (brigadier mode, autonomous, 2-4h)
trigger: Ruslan ack — Harari books через Jetix lens
parallel_run: text-005-007-blockchain-integration (НЕ trog'ает namespace research/harari-jetix-lens/)
language: russian + english (verbatim citations)
---

# DEEP PROMPT — Harari через Jetix lens

> **Ты = brigadier**. **ultrathink** ON. R1/R2/R6/R11 + append-only + no API keys.

> Parallel run. Namespace: `research/harari-jetix-lens-2026-05-18/`. НЕ trog'ает other namespaces.

---

## §0 Цель

Прогнать **Yuval Noah Harari** book corpus **через Jetix lens** — extract insights / concepts / patterns которые resonate с Jetix vision (особенно text_001-007 cluster + H1-H8 Octagon + virtual tribe + trust mechanism + intellectual augmentation themes).

### §0.1 Harari corpus to cover

| Book | Year | Topic | Jetix relevance prior |
|---|---|---|---|
| **Sapiens: A Brief History of Humankind** | 2011 (en 2014) | Cognitive revolution / shared myths / cooperation across millions | text_005 «миллиарды людей» / virtual tribe / shared meaning |
| **Homo Deus: A Brief History of Tomorrow** | 2015 (en 2016) | Dataism / algorithms / loss of individual / future humanism | H8 trust / R12 anti-extraction / FPF intelligence amplification |
| **21 Lessons for the 21st Century** | 2018 | Current challenges: meaning / community / technology / education | Workshop pattern / education / meaning |
| **Nexus: A Brief History of Information Networks** | 2024 | **Information networks от каменного века до AI** — direct Jetix relevance! | text_002 «новый internet» / text_004 «info-processing instruments» / FPF universal language |
| **Sapienship Foundation publications** | ongoing | Public letters / commentary on AI safety / governance | d/acc adjacency / governance / R12 |

**Priority: Nexus (2024) > Homo Deus > Sapiens > 21 Lessons > Sapienship.**

---

## §1 4-Phase workflow

### Phase 1 — Corpus access + structure (~20 мин)
WebSearch + WebFetch:
- Harari books summaries (Wikipedia / official site / academic reviews)
- Verbatim chapter structures где доступны
- Key claims per book
- Critic responses (Hari has critics — capture diverse views)
- Recent articles / interviews 2024-2026

Save raw extracts в `raw/external/harari-corpus-2026-05-18/`.

### Phase 2 — Per-book Jetix lens distillation (~2h)
Per book separate doc:

```
research/harari-jetix-lens-2026-05-18/
  01-sapiens-jetix-lens.md           # Cognitive revolution + shared myths → virtual tribe / Foundation as shared myth
  02-homo-deus-jetix-lens.md         # Dataism critique → R12 / FPF anti-data-extraction
  03-21-lessons-jetix-lens.md        # Meaning + community + education → Workshop / Self-OS
  04-nexus-jetix-lens.md             # ⭐ Information networks → FPF + Jetix internet layer direct
  05-sapienship-publications-lens.md # AI governance commentary → d/acc adjacency
```

Per doc structure:
- §0 TL;DR (≤200 слов)
- §1 Verbatim Harari quotes (top 10 most relevant)
- §2 Core Harari claims (numbered)
- §3 Jetix lens application (per claim — how this maps к Jetix objects O-01..O-23 / Strategic Insights H1-H8 / vision/* / FPF primitives)
- §4 What Harari shows that Jetix can learn / borrow
- §5 What Harari is critical of (warnings) — does Jetix avoid these?
- §6 Direct mappings к specific Jetix artefacts (cross-refs)
- §7 Open questions (R1 — surface, не decide)
- §8 На человеческом (plain Russian summary)

### Phase 3 — Cross-book synthesis (~30 мин)
Create `research/harari-jetix-lens-2026-05-18/98-CROSS-BOOK-SYNTHESIS.md`:
- Recurring themes across Harari corpus
- Trajectory of his thinking (2011 Sapiens → 2024 Nexus)
- Which Jetix concepts get strongest support from Harari corpus
- Which Jetix concepts Harari might critique
- Synthesis: what we keep / what we adjust / what we reject

### Phase 4 — Master summary + Jetix integration recommendations (~30 мин)
Create `research/harari-jetix-lens-2026-05-18/99-SUMMARY-FOR-RUSLAN.md`:
- ≤1500 слов, 10-min read
- Top-7 actionable insights Harari → Jetix
- Mermaid: Harari corpus mapped к Jetix Octagon (H1-H8)
- Reading order recommendation Ruslan (which Harari book to read first)

---

## §2 Specific themes to track (Harari ↔ Jetix)

**Hash tags для cross-reference:**

- **#shared-myths-cooperation** (Sapiens) → text_002 «новый internet» / Foundation как shared myth
- **#cognitive-revolution** → text_001 trust shift / text_002 FPF as language upgrade
- **#dataism-critique** (Homo Deus) → R12 anti-extraction
- **#useless-class-warning** (Homo Deus) → Workshop counter-mechanism
- **#information-flow-mechanics** (Nexus) → FPF protocol design
- **#truth-vs-order** (Nexus) → F-G-R discipline + AP-6 dissent
- **#story-vs-data** → Workshop human-readable + FPF formal dual versions
- **#decentralized-vs-centralized** → d/acc + Ethereum substrate
- **#meaning-crisis** (21 Lessons) → Workshop mastery vs commodified work
- **#cooperation-at-scale** → text_004 virtual tribe / first clan
- **#AI-alignment-democracy** → governance / Pillar C / R12

---

## §3 Cell dispatch

| Phase | task_shape | Cells |
|---|---|---|
| 1 corpus access | review | brigadier scribe (WebFetch dispatch) |
| 2 per-book lens | design | phil × critic + mgmt × integrator + sys × integrator (per book) |
| 3 cross-book synthesis | design | phil × critic + mgmt × integrator |
| 4 master summary | review | mgmt × integrator + phil × critic |

Plain Russian §8 в каждом doc — eng × scalability + mgmt × integrator (accessible language).

---

## §4 Constitutional posture

- **R1** — surface only; не promote Harari claims as Jetix strategy
- **R2** — `research/harari-jetix-lens-2026-05-18/` namespace; Foundation read-only
- **R6** — provenance per claim (book + chapter + page where extractable; URL + retrieved_date for online sources)
- **R11** — Default-Deny
- **Append-only**
- **EP-5** disclosed
- **NO paid API**

---

## §5 Что НЕ делать

- НЕ purchase books (use Wikipedia + free summaries + reviews + interviews + online excerpts)
- НЕ promote Harari как Jetix authority — он strong-opinion writer с critics
- НЕ оценивать «Harari прав / неправ» — surface neutral; preserve dissent
- НЕ trog'ать другие namespaces
- НЕ create new Strategic Insights (H9+) автоматически — surface candidates если найдёшь

---

## §6 Acceptance criteria

- [ ] 5 per-book lens docs (01-05)
- [ ] 1 cross-book synthesis (98)
- [ ] 1 master summary (99)
- [ ] Plain Russian §8 в каждом doc
- [ ] Provenance per claim (book + chapter where possible)
- [ ] git commits per book + final push

---

## §7 Cost cap

- Daily €10; halt+ask €50
- Expected: <€1 (WebSearch + WebFetch built-in only)

---

## §8 Context files (priority read order)

1. `raw/voice-memos-2026-05-17-batch/text_001-007*.md` — 7 strategic notes baseline
2. `vision/00-MASTER-VISION-PLAN-2026-05-17.md`
3. `research/deepening-2026-05-18/99-SUMMARY-FOR-RUSLAN.md`
4. `decisions/STRATEGIC-INSIGHT-*.md` — H1-H8 Octagon
5. `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md`

---

**Launch:**

```bash
tmux new -s harari-jetix-lens
cd ~/Desktop/jetix-os && git pull --rebase origin main && claude --dangerously-skip-permissions
```

Paste:

```
ultrathink. Прочитай prompts/harari-through-jetix-lens-2026-05-18.md полностью. Ты — brigadier. 4-Phase: corpus access → 5 per-book Jetix-lens docs (Sapiens / Homo Deus / 21 Lessons / Nexus / Sapienship) → cross-book synthesis → master summary. Track 11 themes (#shared-myths / #cognitive-revolution / #dataism / #useless-class / #information-flow / #truth-vs-order / #story-vs-data / #decentralized / #meaning-crisis / #cooperation-at-scale / #AI-alignment). Plain Russian §8 в каждом doc. R1 surface-only. R6 provenance per claim. WebSearch + WebFetch built-in only. Действуй автономно 2-4 часа, commit per book, push origin main в конце.
```

Detach: `Ctrl+B затем D`.
