---
title: Research Deepening — meta-research over adjacent-ideas + recursive deep dives
date: 2026-05-18
type: deep-prompt-meta-research
target: server CC (brigadier mode, autonomous, 3-5h)
trigger: Ruslan ack — углубиться в research-adjacent: что ещё изучить, где gaps, какие hooks worth deepening
parent: research/adjacent-ideas-2026-05-17/ (10 docs + 4 mermaid, commit 298eccc)
language: russian + english (verbatim citations)
parallel_runs: jetix-fpf-describe (ongoing) — НЕ trog'ает vision/jetix-fpf-describe/* namespace
---

# DEEP PROMPT — Research Deepening (meta-research + recursive deep dives)

> **Ты = brigadier** (per `.claude/agents/brigadier.md`, opus). Constitutional: Tier 2 R1/R2/R6/R11 + append-only + no API keys. **ultrathink** ON.

> **PARALLEL RUN.** `jetix-fpf-describe` идёт в соседнем tmux session. НЕ trog'ай `vision/jetix-fpf-describe/*` namespace. Этот run в `research/deepening-2026-05-18/`.

---

## §0 Контекст

Ruslan прочитал `research/adjacent-ideas-2026-05-17/` (10 docs, commit `298eccc`) и нашёл это «очень интересным». Ack: **«пусть для начала соберёт что ещё надо изучить отталкиваясь от этой информации... важно... что может расширить нашу картину либо углубить в какую-то конкретную часть куда надо что может быть полезным»**.

Цель: **расширить research картину + углубиться в конкретные части**. Recursive deepening over existing surface.

---

## §1 2-Phase workflow

### §1.1 Phase 1 — META-RESEARCH PLANNING

Brigadier reads `research/adjacent-ideas-2026-05-17/*` (10 docs + 4 mermaid + cell drafts) + identifies:

1. **Open questions / Q1-QN sections** of each cluster — already surfaced gaps
2. **Hooks** — concepts / people / events worth deeper look (per cluster open questions + brigadier-surfaced)
3. **Gaps** — under-researched areas / sparse-data flags from research-adjacent §6
4. **Cross-cutting themes** — patterns spanning 2+ clusters that warrant focused deep dive
5. **Failure-case deep dives** — pre-mortem opportunities (Xanadu / Cybersyn / Stack Overflow / Praxis / Friend.tech / kibbutz decline / Six Sigma backlash)
6. **Success-case deep dives** — what worked + transferable mechanism (Alexander Pattern Language lineage / Mondragón 68yr / Engelbart H-LAM/T / Karpathy LLM Wiki / TPS tacit→explicit)
7. **Substrate option deep comparisons** — VC vs SBT vs PGP vs Karpathy wiki sigs vs Coordinape (H8 substrate selection blocker)
8. **Methodology lineage deep traces** — SEMAT Essence vs FPF / Cynefin 5-domain vs FPF Foundation Parts / TRIZ pattern hierarchy
9. **People deep profiles** — Top-12 из `08-interesting-people-list.md` — extended bibliography + public channels + recent work + outreach surface (no actual contact)
10. **Cross-domain transfer candidates** — FPF apply к aerospace / biotech / heavy industry / education / cooperative networks

**Phase 1 output:** `research/deepening-2026-05-18/00-DEEPENING-PLAN.md` (~1000 слов) — prioritized list of deepening directions с rationale per direction.

### §1.2 Phase 2 — EXECUTE DEEP DIVES

Per identified direction (target: 10-15 directions; pick most-impactful per F-G-R):

- **Deep WebSearch + WebFetch** primary sources
- **Verbatim quotes** where extractable
- **F-G-R per claim** (Jetix convention; EP-5 disclosed)
- **Mermaid diagrams** where useful (~1-3 per direction)
- **Cross-refs** к existing material (research-adjacent + Phase 0 + vision/* + H1-H8)
- **Counter-positions / failure modes** preserved per direction (AP-6 dissent)

Output per direction: 1-3 page markdown в `research/deepening-2026-05-18/`.

**Autonomous ack** (in this prompt): Phase 2 запускается автоматически после Phase 1 commit, не останавливается на ack.

---

## §2 Cell dispatch matrix (per direction type)

| Direction type | task_shape | Cells |
|---|---|---|
| People deep profile | review | mgmt × integrator + phil × critic (claim integrity) |
| Substrate technical comparison | design | eng × integrator + sys × scalability |
| Failure-case pre-mortem | review | phil × critic + sys × integrator + mgmt × critic |
| Success-case mechanism extraction | design | eng × integrator + sys × integrator + phil × critic |
| Methodology lineage trace | design | phil × critic + eng × integrator + mgmt × integrator |
| Cross-domain transfer test | review | eng × scalability + investor × scalability + phil × critic |
| Cross-cutting theme synthesis | design | mgmt × integrator + phil × critic + sys × integrator |

Brigadier integrates AP-6 dissent preservation + §5.5.5 provenance gate (6-check) перед каждым canonical write.

---

## §3 Output structure

```
research/deepening-2026-05-18/
  00-DEEPENING-PLAN.md                    # Phase 1 output — prioritized direction list (~1000 слов)
  01-XX-<direction-slug>.md               # Per deepening direction (1-3 pages each)
  ...
  98-CROSS-CUTTING-SYNTHESIS.md           # patterns spanning 3+ directions
  99-SUMMARY-FOR-RUSLAN.md                # ≤1500 слов, 10 min read

research/deepening-2026-05-18/diagrams/
  *.md                                     # ~5-10 mermaid where useful
```

Direction filename pattern: `NN-<type>-<slug>.md` (e.g., `01-people-engelbart-deep.md`, `05-substrate-comparison-vc-sbt-pgp.md`, `08-failure-cybersyn-pre-mortem.md`).

---

## §4 Direction priority hints (R1 — server CC sam picks)

**High-priority hints из 09-positioning + 6 zero-cost actions:**

- **Engelbart H-LAM/T deep mapping** — verbatim 1962 paper sections → exact FPF primitive mapping
- **Alexander Pattern Language → Cunningham → Karpathy lineage** — what survives + why (50-year transfer mechanism)
- **W3C VC v2.0 + SBT + PGP comparison** — technical substrate options для H8 (decision substrate)
- **Xanadu pre-mortem** — exact failure mechanism + Jetix-specific mitigation
- **Cybersyn pre-mortem** — political fragility lesson + distributed substrate design
- **Stack Overflow gamification pre-mortem** — anti-gaming H8 design specifics
- **Buterin d/acc (Nov 2023 + Jan 2025)** — explicit retro + Jetix overlap analysis
- **Karpathy LLM Wiki April 2026** — direct ancestor analysis + delta from Jetix wiki/
- **SEMAT Essence vs FPF** — direct competitive analysis methodology kernel
- **Mondragón 68yr mechanism** — what enables long-run cooperative scale (R12 + governance)
- **TimeBanks 4 principles** — exact R12 positive face mapping
- **Plurality (Tang/Weyl 2024)** — quadratic funding + radical exchange relevance
- **Coordinape + Gitcoin** — production non-money trust mechanisms working today
- **TPS tacit→explicit transfer** — how Toyota distributes opaque knowledge
- **EVE Online 20-year community** — what enables long-form virtual tribe (text_004 reference case)
- **Friend.tech collapse 2024** — financial coordination failure pre-mortem
- **Cross-domain FPF test** — apply FPF к aerospace OR biotech OR education for transfer evidence

**Server CC picks 10-15 directions** based on:
1. Impact for Jetix Phase 0-1 decisions
2. Data availability (WebSearch fruitful)
3. Cross-direction synergy potential

---

## §5 Constitutional posture

- **R1** — surface deepenings / facts, не promote ideas к Jetix strategy. Ruslan picks integration.
- **R2** — `research/` namespace only; Foundation paths read-only.
- **R6** — provenance per claim (URL + retrieved date OR file:line)
- **R11** — Default-Deny.
- **Append-only** — new dir.
- **EP-5** disclosed (F2-F3 grade for research; F4 only if multi-source triangulated).
- **NO external paid APIs** — WebFetch / WebSearch built-in only.

---

## §6 Что НЕ делать

- НЕ create new Strategic Insights / H9 LOCKs
- НЕ trog'ать `vision/jetix-fpf-describe/*` (parallel run)
- НЕ promise outreach к people without Ruslan ack
- НЕ hallucinate facts — «not found» better than fake
- НЕ duplicate research-adjacent docs — extend / deepen / synthesize только
- НЕ оценивать «эта идея лучше Jetix» / «эта хуже» — surface neutral

---

## §7 Quality discipline (per direction)

1. Primary source preferred (WebFetch URL + retrieved_date)
2. Verbatim quotes где fact-load high
3. Multiple sources cross-checked для key claims
4. Conflicting claims → preserve dissent AP-6
5. «Sparse data» / «not found» flags explicit if applicable
6. F-G-R triple per non-trivial claim
7. Mermaid where useful (cool blues palette + color:#1a202c contrast)
8. Cross-refs к existing material mandatory (нет orphan documents)

---

## §8 Failure modes

| Если | Действие |
|---|---|
| Direction yields sparse data | Mark sparse + skip OR pivot к adjacent direction |
| Conflicting sources | Preserve dissent AP-6 |
| Cell disagrees on direction priority | Surface escalation в Phase 1 plan; brigadier picks majority + dissent note |
| Cost cap €50 | NOT triggered — WebSearch + WebFetch built-in = free |
| Time overrun >5h | Surface checkpoint; Ruslan может pause/continue |

---

## §9 Acceptance criteria

- [ ] Phase 1 plan: `00-DEEPENING-PLAN.md` ≤1000 слов с 10-15 prioritized directions
- [ ] Phase 2: 10-15 deepening docs per direction (1-3 pages each)
- [ ] Cross-cutting synthesis: `98-CROSS-CUTTING-SYNTHESIS.md`
- [ ] Summary for Ruslan: `99-SUMMARY-FOR-RUSLAN.md` ≤1500 слов, 10-min read
- [ ] 5-10 mermaid diagrams в diagrams/
- [ ] git commits per Phase 1 + per direction + final push
- [ ] Provenance per claim (R6)
- [ ] Cross-refs к existing material (no orphans)

---

## §10 Context files (priority read order)

1. `research/adjacent-ideas-2026-05-17/00-MASTER-RESEARCH-INDEX.md` — entry
2. `research/adjacent-ideas-2026-05-17/09-jetix-positioning-sharpened.md` — uniqueness claims
3. `research/adjacent-ideas-2026-05-17/08-interesting-people-list.md` — 52 candidates
4. `research/adjacent-ideas-2026-05-17/01-07-*.md` — 7 cluster docs (each §6 = adjacencies, §7 = open questions)
5. `research/adjacent-ideas-2026-05-17/diagrams/*` — 4 visual context aids
6. `vision/00-MASTER-VISION-PLAN-2026-05-17.md` — Jetix vision context
7. `decisions/STRATEGIC-INSIGHT-*.md` — H1-H8 Octagon
8. `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` — Phase 0 14 objects
9. `raw/voice-memos-2026-05-17-batch/text_001-004*.md` — 4 strategic notes baseline

---

**Launch (отдельная tmux session):**

```bash
tmux new -s research-deepening
cd ~/Desktop/jetix-os && git pull --rebase origin main && claude --dangerously-skip-permissions
```

Paste:

```
ultrathink. Прочитай prompts/research-deepening-2026-05-18.md полностью. Ты — brigadier. Параллельный run к jetix-fpf-describe — НЕ trog'ай vision/jetix-fpf-describe/* namespace. 2-phase: Phase 1 meta-research planning (read all 10 research-adjacent docs + identify 10-15 prioritized deepening directions → commit 00-DEEPENING-PLAN.md) → Phase 2 execute deep dives per direction (1-3 page doc each, WebSearch+WebFetch, F-G-R per claim, mermaid where useful, cross-refs mandatory). АВТОНОМНЫЙ ACK — Phase 2 запускается автоматически после Phase 1 commit. R1 surface-only. R6 provenance per claim. R11 Default-Deny. WebSearch + WebFetch built-in only (zero paid API). Действуй автономно 3-5 часов, коммить per Phase + per direction, push origin main в конце.
```

Detach: `Ctrl+B затем D`.
