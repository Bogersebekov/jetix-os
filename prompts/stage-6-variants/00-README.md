---
id: stage-6-variants-master-index
title: Stage 6 — 6 Architecture Variants (master index)
date: 2026-04-21
type: master-index
status: ready
priority: P1
stage: 6
depends_on:
  - decisions/JETIX-VISION.md (D1 APPROVED 2026-04-21)
  - decisions/JETIX-PHILOSOPHY.md (D2 APPROVED 2026-04-21)
  - decisions/JETIX-PLAN.md (D3 APPROVED 2026-04-21)
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 APPROVED 2026-04-21)
  - decisions/STAGE-3-APPROVAL.md
  - decisions/STAGE-4-APPROVAL.md
binding: no — index/navigation only (individual prompts are binding directives for architects)
audience:
  - Ruslan (Stage 7 comparative evaluation)
  - 6 parallel Claude Code architect-agents (execution in Stage 6)
---

# Stage 6 — 6 Architecture Variants (master index)

## What this directory contains

Six independent architect-variant prompts + this master index + shared working memory
(`/home/ruslan/jetix-os/tmp/stage6-meta/SHARED-REFERENCE-PACK.md`).

Each prompt instructs a Stage 6 Claude Code architect-agent to generate **one variant** of the
Jetix architecture, answering all 15 architect questions from D4 §10, under a distinct
philosophical lens, producing a comparable 24-section output document. Ruslan reads all 6
variants in Stage 7 and selects one (or composes a hybrid) per the D4 §9 procedure.

**Precedence reminder.** D1 Vision + D2 Philosophy + D3 Plan + 24 locked decisions > D4 Brief >
OME/FPF/ADR reference material > atom registry. No variant may violate any lock, any of the
21 hard constraints (D4 §6 C1–C21), or any of the 16 anti-patterns (D4 §7 AP-1–AP-16) without
disqualification (§8.3).

## Stage 6 context

**Stage sequence (architectural track).**
- Stage 1–2: Knot mapping + tension pre-resolution (24 locks emerged)
- Stage 3: D1 + D2 + D3 written + approved (2026-04-21)
- Stage 4: D4 Architecture Brief written + approved (2026-04-21, 5 passes, academic-grade)
- Stage 5: Prompt-writing (this stage — 6 variant prompts + master index + launchers)
- **Stage 6: 6 architect-agents in parallel produce 6 variants (5–7h each in 6 CC sessions)**
- Stage 7: Ruslan comparative evaluation + selection (pure variant or hybrid composition)
- Stage 8: Implementation plan from selected variant (D5 Architecture Canonical feeds this)
- Stage 9+: Execution

**Why 6 variants, not 1.** Diversity of architectural perspective. A single architect, however
good, collapses to one lens. Six lenses surface design trade-offs that a single pass would leave
implicit. Stage 7 selection may take one pure variant, but more commonly composes a hybrid
per D4 §9 Step D. The variants are not ranked ex-ante; each is optimized for its own character.

**Why these 6 specifically.** The six variants span the design space along two axes:
(i) *complexity stance* (Conservative — minimum deviation / Maximalist — full scaffold) and
(ii) *evolution stance* (top-down designed / emergent / phase-keyed / contrarian). Together
they cover the dominant ways a competent architect might approach the brief, including the
"what if the brief is wrong?" Wildcard.

## 6 variants overview

| # | Variant | Philosophical lens | Signature move | Expected strengths | Expected weaknesses |
|---|---|---|---|---|---|
| 1 | **Conservative** | "Evolve what works, don't rewrite what isn't broken" | Minimum deviation from CLAUDE.md + D6 FPF + OME reference; 11-agent roster as-is | Phase-1 readiness, Locks compliance, Operational simplicity | Innovation, Scale trajectory |
| 2 | **Aggressive Maximalist** | "Build for Phase 3 from Day 1 — pay technical debt upfront, not later" | Full Phase-2/3 capability scaffolded Phase 1 (schemas + role-manifests + spec docs, not runtime) | Scale trajectory, Foundation quality, Innovation | Operational simplicity, Phase-1 cost (must defend €800/mo) |
| 3 | **Aggressive Deep-Tech** | "Correctness through formalism — FPF is the substrate, Jetix is the instance" | Ontology-first: every agent has formal FPF contract, wiki = typed graph, protocols = standards-body drafts | Foundation quality, Universality, Innovation | Operational simplicity, Phase-1 readiness (depth slows shipping) |
| 4 | **Hybrid** | "Right depth at right phase — simplicity Phase 1, richness Phase 2+, maximalism Phase 3+" | Every capability has `activation_trigger` (revenue gate OR MHT transition); phase-keyed complexity | Balance across axes, Scale trajectory, Locks compliance | Distinctive strength (no single 9-10 axis) |
| 5 | **Emergent** | "Design the space of possibilities, not the outcome itself — trellis not cage" | Thin prescribed structure + rich protocols + agent-driven specialization within hub-and-spoke | Operational simplicity, Cost efficiency, Innovation | Scale predictability, Locks compliance tension (must defend) |
| 6 | **Wildcard** | "Orthodox answers produce orthodox results — challenge the question" | 1–3 radical reframes with defense + lock-check + fallback per reframe | Innovation, surfacing blind spots | High variance; highest disqualification risk |

## Shared inputs (read by all 6 architects)

Every variant architect MUST read, in full, the same binding input set:

1. `decisions/JETIX-VISION.md` (D1 APPROVED 2026-04-21)
2. `decisions/JETIX-PHILOSOPHY.md` (D2 APPROVED 2026-04-21)
3. `decisions/JETIX-PLAN.md` (D3 APPROVED 2026-04-21)
4. `decisions/JETIX-ARCHITECTURE-BRIEF.md` (D4 APPROVED 2026-04-21 — **critical, 15 questions here**)
5. `decisions/STAGE-3-APPROVAL.md`
6. `decisions/STAGE-4-APPROVAL.md`
7. `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (locks D1–D8)
8. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (locks D9–D18 / T1–T10)
9. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (locks D19–D24)
10. `raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md` (inspiration)
11. `design/JETIX-FPF.md` (D6 constitutional ontology)
12. `decisions/2026-04-19-architecture-v2-approval.md` (ADR Chunks 1-8)
13. `CLAUDE.md` (current agent config)

Plus the working-memory reference pack (distilled binding items): `tmp/stage6-meta/SHARED-REFERENCE-PACK.md`.

**Precedence rule for conflicts.** D1+D2+D3+24 locks > D4 Brief > OME/FPF/ADR > atoms. Any
contradiction ⇒ higher-precedence wins; lower artifact silently drops. Brief elevates certain
items to hard constraints (§6); those inherit brief precedence tier.

## 15 architect questions (all 6 must answer all 15)

1. **Q1** — Repository structure (base / overlay separation)
2. **Q2** — Agent roster reconciliation (11 canonical + 5 Ruslan sub-roles + 2 Phase-2a stubs)
3. **Q3** — Integration points inventory (Stripe / Wise / Claude / Notion / Telegram / etc. + fallback)
4. **Q4** — Scaling mechanism ($0 → $1T without rewrite; 10× at each gate ≤30% LOC refactor)
5. **Q5** — Data architecture (wiki 9 entity types + atoms + provenance + F-G-R)
6. **Q6** — Privacy / security membrane (tier ACL + GDPR Art.22 + EU AI Act)
7. **Q7** — API architecture (multi-provider + compute-ledger + €300–800/mo Phase 1 band)
8. **Q8** — Token economy Option B (Phase 2 internal / Phase 3+ limited public)
9. **Q9** — Matchmaker algorithm (4 modules: algorithm / quality-gate / contract-fixation / metrics)
10. **Q10** — Roy-replication formalization (methodology-as-system kit export)
11. **Q11** — Content pipeline TOF/mid/deep (frame-tag + archetype-keyed rendering)
12. **Q12** — Dashboard implementation (v1 Phase 1 / v2 Phase 2+ / v3 Phase 3+)
13. **Q13** — Escalation routing (6 non-delegatable + 4-class FPF + CP-5 gate)
14. **Q14** — Onboarding architecture (2nd pilot ≤7 days cold-start)
15. **Q15** — USB-C protocol layer (Jetix-defined standards + verification harness)

**Interdependency clusters** (D4 §10 summary):
- **Cluster A (Structural):** Q1 ↔ Q2 ↔ Q14
- **Cluster B (Scale + Data + API):** Q4 ↔ Q5 ↔ Q7 ↔ Q12
- **Cluster C (Membrane + Economy):** Q6 ↔ Q8 ↔ Q13
- **Cluster D (Ecosystem):** Q9 ↔ Q10 ↔ Q15 ↔ Q14
- **Cross-cluster:** Q11 (content) touches A/B/C; Q3 (integrations) touches A/B/C

Variants are scored on consistency across clusters (Stage 7 criterion).

## 24-section output structure (identical across all 6)

Each variant deliverable (`decisions/variants/JETIX-ARCH-V{N}-{NAME}.md`) contains the **same 24
sections in the same order**, so Stage 7 comparison is literal side-by-side. This is critical —
one variant that shuffles section order cannot be compared without manual restructuring.

1. Executive Summary (1 page)
2. Variant Character Statement (1 page)
3. Answer to Q1: Repository layout (3–5 pages, ASCII diagrams)
4. Answer to Q2: Agent roster (3–5 pages)
5. Answer to Q3: Integration points (2–3 pages)
6. Answer to Q4: Scaling mechanism (3–5 pages)
7. Answer to Q5: Data architecture (3–4 pages)
8. Answer to Q6: Privacy/security membrane (2–3 pages)
9. Answer to Q7: API architecture (2–3 pages)
10. Answer to Q8: Token economy Option B (2–3 pages)
11. Answer to Q9: Matchmaker algorithm (3–4 pages)
12. Answer to Q10: Roy-replication packaging (2–3 pages)
13. Answer to Q11: Content pipeline (2–3 pages)
14. Answer to Q12: Dashboard implementation (2–3 pages)
15. Answer to Q13: Escalation routing (2–3 pages)
16. Answer to Q14: Onboarding architecture (2–3 pages)
17. Answer to Q15: USB-C protocol layer (3–5 pages)
18. Foundation Layer Specification (5–7 pages, per D4 §4 eight elements)
19. Hard Constraints Compliance Matrix (1–2 pages — table 21 C-constraints × variant compliance)
20. Anti-Patterns Avoidance Statement (1–2 pages — all 16 AP × confirmed avoidance)
21. Self-Scoring on D4 §8 Quality Axes (1–2 pages — honest self-score on 10 axes)
22. Variant Contrarian Claims (0.5–2 pages; Wildcard variant uses full 2 pages, others brief)
23. Risk Profile (1–2 pages — top 5 failure modes + mitigation)
24. Selection Case for Ruslan (1 page — "why pick me")

**Size target per deliverable:** 40–60 pages / 8000–12000 words.

## How parallelization works

Six independent Claude Code sessions, one per variant. Each session is launched in its own
tmux window on Ruslan's remote host (`ruslan@100.99.156.28`) using `--dangerously-skip-permissions`
mode. All six sessions operate on the same git branch (`claude/jolly-margulis-915d34`) and the
same filesystem; each writes its own file under `decisions/variants/JETIX-ARCH-V{N}-{NAME}.md`,
so write-contention is minimal. Each session independently rebases before committing to absorb
other variants' intermediate pushes.

Expected wall-clock: 5–7 hours per variant with sub-subagents in each session (one CC spawning
4 parallel cluster subagents during Pass 2). Total wall-clock for all 6: 5–7 hours (parallel,
not serial). Ruslan monitors progress via tmux attach or Notion updates.

**Prep step (one CC, one-time before launching 6).** See `LAUNCHERS-STAGE-6.md` for the
one-liner that fetches + merges + lists the prompt directory to confirm readiness.

## Output directory structure (where variants land)

```
decisions/variants/
├── JETIX-ARCH-V1-CONSERVATIVE.md
├── JETIX-ARCH-V2-MAXIMALIST.md
├── JETIX-ARCH-V3-DEEPTECH.md
├── JETIX-ARCH-V4-HYBRID.md
├── JETIX-ARCH-V5-EMERGENT.md
└── JETIX-ARCH-V6-WILDCARD.md
```

Each file ~40–60 pages / 8000–12000 words / 24 sections identical order. Filenames are
uppercase for visual distinction from other `decisions/` artefacts.

## Stage 7 evaluation approach

Ruslan + meta-agent apply D4 §9 Step A–F procedure:

- **Step A — Hard-disqualifier pass.** Any §6 C-constraint violated or any §7 AP present ⇒
  variant discarded pre-scoring. (Wildcard variant highest risk here; its §22 must defend
  every reframe against 24 locks + 21 C + 16 AP.)
- **Step B — Quantified scoring.** Each variant self-scored on §8.1 ten axes with §8.2
  weights; Ruslan + meta-agent cross-audit honesty of self-score. Total out of 100.
- **Step C — Trade-off review.** Top 2–3 by total; Ruslan weighs which axes matter most
  for current phase position + risk appetite. Default preference (Stage-3 stated):
  Phase-1 readiness + Foundation quality > Innovation.
- **Step D — Hybrid-option clause.** Ruslan may compose hybrid pulling best elements from
  multiple variants. Required: per-element traceability + constraint-compatibility check +
  Design Rationale Record (DRR per FPF §E.9).
- **Step E — Backup plan.** If all variants inadequate: Stage 6 re-run with refined brief,
  OR commit to best-available and book Phase-1.5 refactor window.
- **Step F — Final lock.** Selected variant (pure or hybrid) = D5 Architecture Canonical.

## Quality evaluation axes (D4 §8.1, weights §8.2)

| # | Axis | Weight |
|---|---|---|
| 1 | Phase-1 readiness | 20% |
| 2 | Scale trajectory | 15% |
| 3 | Foundation quality | 15% |
| 4 | Locks compliance | 18% |
| 5 | Universality | 10% |
| 6 | Operational simplicity | 10% |
| 7 | Cost efficiency | 0% (gate-based disqualifier §8.3) |
| 8 | Resilience | 5% |
| 9 | Security posture | 5% |
| 10 | Innovation | 2% |

Hard floor: any axis < 3 disqualifies variant. Hard disqualifiers (§8.3):
- Any §6 C-constraint violated
- Any §7 AP present
- Section 10 question not addressed
- Any lock uncited (axis 4 ≤3)
- Phase-1 run rate > €800/mo without justification

## Ruslan's stated preferences (Stage-3 — subject to Stage-7 override)

- Foundation quality > feature count
- Scale-readiness > short-term ergonomics
- Universality > Jetix-specific shortcuts
- Enterprise-fast (robust + adequate + fast) > solopreneur ergonomics
- Locks compliance absolute (no trade-off)

## Notion page reference

Stage 6 progress tracked at:
https://www.notion.so/3492496333bf812e8b62cbc61338ce06

Each architect appends a status line when complete; Ruslan reads at Stage 7 entry.

## Operational rules for architect-agents (common to all 6)

1. **Read full binding input list before writing.** No guessing at brief content.
2. **Multi-pass writing mandatory.** Pass 1 skeleton (section headers + key claim per section),
   Pass 2 flesh (8000–12000 words, subagents for parallelism), Pass 3 coherence-critic
   (self-critique, cross-check 15 questions + 24 locks + 21 C + 16 AP).
3. **Citations.** Every lock referenced by ID (D1–D24 or D4 §6 CX or D4 §10 QX). No paraphrase
   of locks without citation. Quote Ruslan's voice where relevant (from D1/D2/D3/D4).
4. **F-G-R frontmatter.** Variant deliverable has F-G-R tags in YAML (formality: F2, reliability:
   R-high, claim-scope: jetix-stage-6-variant-{N}).
5. **Own file only.** Write only to `decisions/variants/JETIX-ARCH-V{N}-{NAME}.md`. Do not edit
   other variants, CLAUDE.md, or any approved D-doc.
6. **Rebase before push.** `git pull --rebase origin claude/jolly-margulis-915d34` before commit.
7. **Notion append at completion.** Single status line.
8. **Stdout summary at end.** Fixed format per variant prompt's Section 8.

## ETA

- Per variant: 5–7 hours (with 4 parallel subagents in Pass 2)
- All 6 in parallel: 5–7 hours total wall-clock
- Stage 7 Ruslan evaluation: 3–5 hours reading + 1–2 hours decision = 4–7 hours total
- Stage 5 prompt-writing (this): 3–4.5 hours with subagents

## Anti-patterns for architects (common)

- Don't skip the coherence-critic pass
- Don't invent locks or brief sections
- Don't skip any of 15 questions
- Don't drift into implementation plan (Stage 8 does that)
- Don't echo D4 verbatim — synthesize in your variant's voice
- Don't copy other variants — yours is distinct by design
- Don't inflate self-score — honesty is the Stage-7 credibility signal

## After Stage 6

Stage 7 (Ruslan):
1. Read all 6 variants (~1 hour each, possibly parallel with meta-agent)
2. Apply §9 Step A–F procedure
3. Commit D5 Architecture Canonical (selected pure variant or composed hybrid)
4. Unblock Stage 8 implementation plan

---

*END OF 00-README — Stage 6 master index*
