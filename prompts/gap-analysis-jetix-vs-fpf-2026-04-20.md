---
type: task-prompt
created: 2026-04-20
target: claude-code-on-server (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: raw/research/fpf-gap-analysis-2026-04-20.md
estimated-time: 2-4 hours intensive analysis
status: ready-to-execute
stage: Post-KB-compilation, Pre-D6-writing
prerequisite: raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md must exist
---

# Task — Gap Analysis: Jetix Architecture vs Левенчук FPF

## Context

Ты — Claude Code на сервере Jetix OS. Только что завершена compilation
unified Knowledge Base (Левенчук + FPF + 5 researches). Теперь нужно
**critical gap analysis**: сравнить утверждённую Jetix архитектуру с
каноническим FPF от Анатолия Левенчука и найти:

1. Что Jetix уже хорошо покрыл
2. Что Jetix missed (patterns из FPF которые стоит add / consider)
3. Где Jetix divergeует от FPF — и stands ли rationale
4. Что Jetix добавил novel (innovations beyond FPF canon)
5. Specific recommended changes к Jetix ADR / D9 draft

Это **critical decision point** перед writing D6. Цель: либо confirm
что current Jetix architecture robust vs FPF canon, либо flag
recommended improvements которые Ruslan может одобрить/отвергнуть.

---

## Inputs

### Primary inputs (must-read fully, in this order)

1. **`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`** (~2456
   строк, ~15K слов) — compiled unified KB (primary + 5 researches
   triangulated). Это твой main reference.

2. **`raw/external/ailev-FPF/FPF-Spec.md`** (62,202 строки, 5.7 MB) —
   **original primary source от Левенчука**. KB — digest; когда нужно
   deep detail по specific FPF pattern — возвращайся сюда. Loaded в 1M
   context window.

3. **`decisions/2026-04-19-architecture-v2-approval.md`** (~30+ pages)
   — утверждённая Jetix архитектура. Все 11 overrides + 50+ decisions
   из Stage 3 review. **Основной Jetix reference.**

4. **`decisions/2026-04-20-jetix-architecture-final-DRAFT.md`** (980
   строк, ~25-30 pages) — D9 draft v0.5, clean consolidation ADR.
   Более structured view Jetix architecture.

### Secondary inputs (reference as needed)

5. **`raw/research/architecture-synthesis-v2-final.md`** (1621 строка)
   — v2 synthesis, original (pre-Ruslan-overrides). Полезно для
   understanding intent если нужен context.

6. **`raw/external/ailev-FPF/Readme.md`** — FPF entry routes + quick-start.

---

## Deliverable

### File path

`raw/research/fpf-gap-analysis-2026-04-20.md`

### Size target

**30-50 pages** structured analysis. Depth > brevity — каждая "recommended
change" должна быть fully justified.

### Frontmatter

```yaml
---
type: gap-analysis
created: 2026-04-20
purpose: Critical comparison Jetix architecture vs Левенчук FPF canon
inputs:
  - raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md (primary reference)
  - raw/external/ailev-FPF/FPF-Spec.md (primary source 62K lines)
  - decisions/2026-04-19-architecture-v2-approval.md (Jetix ADR approved)
  - decisions/2026-04-20-jetix-architecture-final-DRAFT.md (D9 draft v0.5)
analyst: claude-opus-4-7
decision-maker-target: ruslan (reviews and approves/rejects recommendations)
unblocks:
  - Potential ADR Chunk 8 "Post-FPF-discovery additions"
  - D6 JETIX-FPF.md writing (enriched с FPF alignment)
---
```

---

## Structure (recommended — adapt if justified)

### Section 1 — Executive summary (500-800 words)

- One-paragraph Jetix architecture overview (as currently stands)
- One-paragraph FPF canon overview
- Top 5 strongest alignments Jetix↔FPF
- Top 5 critical gaps Jetix should address
- Overall alignment score (0-100 scale with rationale)
- Bottom line: "Jetix is X% aligned with FPF; recommended Y specific changes"

### Section 2 — Jetix Architecture Snapshot (1500-2000 words)

**Purpose:** Distill Jetix current state в form comparable с FPF patterns.

Cover:
- **8 Core Principles** (P1-P8) — short re-statement
- **Reference vs Operational split** — what's material Phase 1 vs later
- **15 folders Phase 1** — purpose per folder
- **8 alphas + state machines** — naming conventions
- **18 role-manifests** — 5 Ruslan sub-roles + 11 agents + 2 stubs
- **FPF (internal, renamed from Lite)** — Ruslan's decision: full depth
- **Portfolio of Directions model** — 8-я alpha + 8-й principle
- **DACH + US + RU unified funnel** — market scope
- **Resource accounting** — Capital + Compute + Deep Hours + Attention
  Budget + Ecosystem
- **11 Overrides vs v2 synthesizer** — what changed

### Section 3 — Pattern-by-pattern mapping (8000-12000 words) ⭐ CRITICAL

**Это самая важная section.** Systematic mapping FPF patterns к Jetix
architecture.

Format: **Table + narrative per major cluster.**

Structure per Part of FPF-Spec:

```markdown
#### Part A — Kernel Architecture (Jetix coverage)

| Pattern ID | FPF Pattern Name | Jetix Coverage | Status | Notes |
|-----------|-----------------|---------------|--------|-------|
| A.1 | Holonic Foundation | Partial (Model D + 8 alphas) | 🟡 | Jetix имеет implicit holon hierarchy но не formal Holon type |
| A.1.1 | Entity → Holon bridge | Not covered | ❌ | Could strengthen alpha model |
| A.6 | Boundary Unpacking | Covered (role out_of_scope) | ✅ | Via role-manifest out_of_scope blocks |
| A.6.H | Wholeness Unpacking (RPR-WHOLE) | Not covered | ❌ | Consider adding |
| A.14 | Advanced Mereology (ComponentOf, PortionOf, PhaseOf) | Partial (3-level mereological graph) | 🟡 | Ruslan override expanded; may need formal part-of types |
| ... | ... | ... | ... | ... |
```

**Iterate через все 11 Parts (Preface + A-K)**:
- Preface / A.0 — big storylines
- Part A — Kernel Architecture (~25-40 patterns)
- Part B — Aggregation
- Part C — CAL (Sys/Episteme/KD/Compose)
- Part D — Conflict Topology
- Part E — Pattern Authoring + Multi-View Publication
- Part F — Bridges + Cross-Linking
- Part G — Selection Mechanisms + Comparison
- Part H — Glossary
- Part I — Walkthroughs
- Part J — Route Explanations
- Part K — Extensions

**Status codes:**
- ✅ **Fully covered** — Jetix имеет equivalent pattern explicit
- 🟡 **Partially covered** — concept present но не formal / named
- ❌ **Not covered** — missing в Jetix, consider add
- ⭐ **Jetix-specific** — Jetix added beyond FPF

**Critical FPF patterns to verify** (deep dive на эти):
- A.1 Holonic Foundation (basic holon type)
- A.6 Boundary Unpacking + A.6.H Wholeness + A.6.P Overloaded Quality
- A.7 Strict Distinction (Object ≠ Description ≠ Carrier)
- A.14 Advanced Mereology (ComponentOf/PortionOf/PhaseOf/AspectOf)
- A.15 / A.15.2 / A.15.3 — responsibility/method/plan/actual separation
- A.16 — partly-said / language-state discovery
- A.17-A.19 — lawful comparison / selection
- B.1 Universal Algebra of Aggregation (Γ operator)
- B.2 Meta-Holon Transition (emergence)
- B.5 RoleEnactment family
- C.2.1 U.Episteme — knowledge representation
- C.13 Compose-CAL (Constructional Mereology)
- D.3 Holonic Conflict Topology
- E.9 DRR (Decision Rationale Record) — formalized ADR
- E.17 Multi-View Publication Kit (MVPK)
- F.9 Bridges + CL (Cross-Linking)
- F.11 Method/work vocabulary alignment
- F.17 UTS (Unstable Term Sheet)
- G.0 — G.5 Selection/Comparison family

### Section 4 — Jetix divergences (judgments) (2000-3000 words)

Где Jetix intentionally diverges from FPF canon. For each:

- **Divergence:** What Jetix does differently
- **FPF canonical position:** What FPF-Spec says (with pattern ID quote)
- **Jetix rationale:** Why Jetix chose divergent path
- **Risk assessment:** Does divergence cost ontological integrity?
- **Verdict:** Keep divergence / Revisit / Align with FPF

**Candidates для assessment:**

- **FPF name** — Jetix использует "FPF" как designation для **Jetix-specific
  adaptation**; Левенчук использует "FPF" для canonical framework. Collision
  risk. Should Jetix rename? (e.g., "JPF — Jetix Philosophy Framework" или
  "Jetix FPF adaptation")
- **5 primitives vs 11 Pillars** — Jetix использует old "5 primitives"
  наряду с FPF 11 Pillars. Дублирование?
- **8-я alpha "Direction"** — Jetix innovation. Does FPF-Spec have
  equivalent Portfolio-of-Directions pattern?
- **Past-participle convention strict** — Jetix применяет everywhere.
  FPF may have более nuanced position.
- **Model D Nested Hierarchy** — Jetix uses Russian "Model D" terminology.
  Does FPF use similar or different? Is "Model D" derived from FPF?
- **Role-manifest 5-block structure** — compare с FPF role patterns
  (B.5 RoleEnactment, A.15.1 responsibility vocabulary).

### Section 5 — Jetix innovations (beyond FPF) (1500-2000 words)

**What Jetix has that FPF-Spec does NOT.** Это **positive** — Jetix
adds value к canonical framework.

Document each innovation:

- **Innovation:** What Jetix added
- **Origin:** Where in ADR/D9 was this decided (chunk reference)
- **FPF gap:** Why FPF-Spec doesn't have это
- **Potential contribution back:** Could this inform future FPF versions?

**Known candidates:**

- **Portfolio of Directions as 8-й principle** — holding pattern beyond
  FPF project-alignment focus
- **Capital + Compute + Deep Hours + Attention Budget + Ecosystem**
  resource accounting framework — FPF doesn't address resource typology
- **AI-native specifics** — 18 role-manifests optimized for AI agents
- **DACH-specific compliance integration** — GDPR + EU AI Act + BDSG
  explicit handling
- **7+7 day rollout operational plan** — FPF is general; Jetix specific
- **FPF-Steward sub-role** — R12 override; FPF mentions stewarding in
  context but not formal role
- **Life-OS / Jetix physical separation** — meta-organizational
  decision FPF doesn't address

### Section 6 — Recommended changes к Jetix (2000-4000 words) ⭐ CRITICAL

**Каждая recommendation должна быть actionable + prioritized.**

Format per recommendation:

```markdown
#### Rec-NN: [Short title]

**Priority:** P1 (critical) / P2 (valuable) / P3 (nice-to-have)

**FPF basis:** Which FPF pattern(s) support this. Quote FPF-Spec if
relevant.

**Current Jetix state:** What ADR currently says.

**Proposed change:** Specific modification к ADR / D9 draft / D6.

**Rationale:** Why this improves Jetix.

**Cost:** Time estimate Phase 1.

**Risk of not doing:** What breaks if we skip.

**Dependencies:** Which other recs это enables / requires.
```

**Expected 10-30 recommendations across priorities.**

### Section 7 — Open questions for Ruslan review (1000-1500 words)

Items requiring **judgment-level decision** by Ruslan. Format:

```markdown
#### OQ-NN: [Question]

**Context:** Background + why it matters.

**Options:**
- A. [Option with implications]
- B. [Option with implications]
- C. [Option with implications]

**Claude recommendation:** [My pick + rationale]

**Impact:** What changes based on answer.
```

**Expected 5-15 open questions.**

### Section 8 — Next steps (300-500 words)

Clear recommendation:

1. **Ruslan review** этого gap analysis (time estimate ~60-90 min)
2. **Decisions** per recommendation (accept / reject / defer)
3. **ADR Chunk 8** — update ADR с accepted changes
4. **Potentially D9 draft v0.6** regeneration
5. **THEN** D6 JETIX-FPF.md writing (enriched)

---

## Quality requirements

### Rigour

- **Every claim backed by source citation** — либо FPF-Spec pattern ID
  + line number, либо Jetix ADR section, либо KB section X.Y.
- **Anti-hallucination** — если pattern не verified в actual file,
  flag explicitly
- **Triangulation** — where KB and FPF-Spec disagree, prefer FPF-Spec,
  note conflict

### Balance

- **Not sycophantic pro-FPF** — Jetix может reasonably diverge
- **Not defensive about Jetix** — если FPF clearly better approach, say so
- **Evidence-based** — opinions clearly marked; facts cited

### Actionability

- Every recommendation should be **implementable** (not vague "consider X")
- Every change should have **cost estimate** (hours or effort)
- Every question should have **clear options** (не open-ended)

### Length

- Don't pad; don't compress. Length matches content depth.
- 30-50 pages range is guide; could be 25 or 60 if material justifies

---

## Process

### Step 1 — Read KB thoroughly (~45-60 min)

KB is digest; read it first to build mental model of FPF canon.

Note:
- All 11 sections
- Especially Section 5 (FPF Architecture) + Section 8 (Intersections)
- Glossary (Section 9) — terminology
- Open questions (Section 11) — what KB compiler flagged as uncertain

### Step 2 — Read Jetix ADR + D9 draft (~30-45 min)

Get full Jetix architecture in head. Note all 11 overrides, все 8
principles, 15 folders, 18 roles, etc.

### Step 3 — Scan FPF-Spec для specific patterns (~60-90 min)

With KB + Jetix в голове — scan FPF-Spec section-by-section для
pattern-by-pattern mapping. Use Grep для specific pattern IDs when
needed.

Use Extended Thinking aggressively.

### Step 4 — Write gap analysis (~90-180 min)

Sections 1-8 в order. Focus Extended Thinking on:
- Section 3 pattern-by-pattern mapping (most critical)
- Section 6 recommendations (actionable)
- Section 7 open questions (decisions matter)

### Step 5 — Self-review (~30-45 min)

Check:
- All FPF Parts covered в Section 3 mapping?
- Recommendations prioritized + actionable?
- Open questions have clear options?
- Cost estimates realistic?
- Citation fidelity (pattern IDs correct)?

### Step 6 — Commit + push

```
[research] Gap Analysis: Jetix architecture vs Левенчук FPF canon

Critical comparison:
- Pattern-by-pattern mapping FPF 11 Parts vs Jetix ADR + D9 draft
- Jetix divergences assessment (intentional vs unaddressed)
- Jetix innovations documented (Portfolio, Resource Accounting, AI-native)
- ~N prioritized recommendations (P1/P2/P3)
- ~M open questions для Ruslan judgment

Overall alignment: X% (N strong alignments / M gaps / K innovations).

Unblocks:
- Ruslan review + ADR Chunk 8 updates
- D9 draft v0.6 regeneration (if substantive changes)
- D6 JETIX-FPF.md writing (enriched)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

Push to `claude/jolly-margulis-915d34`.

### Step 7 — Report

Output brief report:
- File path + size
- Alignment score (X/100)
- Top 3 strongest matches
- Top 3 critical gaps
- Number of recommendations per priority
- Number of open questions
- Commit SHA

---

## Configuration

- **Model:** Claude Opus 4.7 (1M context) — mandatory для loading FPF-Spec + ADR + KB together
- **Mode:** Extended thinking enabled, maximum budget
- **Temperature:** 0.3-0.4 (consistency > creativity for analytical work)
- **Tool usage:** Primarily Read + Grep (FPF-Spec pattern lookup) + Write

---

## Important notes

1. **KB is digest, FPF-Spec is authority.** When KB says something, verify
   in FPF-Spec if material to recommendation.

2. **Don't recommend changes that add burden without commensurate value.**
   Ruslan has €50K Q2 deadline + 18 role-manifests + full FPF writing
   already committed. New Phase 1 work needs strong justification.

3. **Identify "cheap adoptions"** — FPF patterns that Jetix can adopt с
   minimal cost (e.g., just renaming conventions).

4. **Identify "expensive divergences"** — places Jetix intentionally
   diverged but might be wrong in hindsight.

5. **Respect Russian + English balance** — FPF-Spec mostly English с
   Russian terms; Jetix ADR mostly Russian с English technical terms.
   Use both thoughtfully.

6. **Output language:** Russian primary (Jetix convention per OT2), but
   FPF patterns quoted in original English с Russian explanation.

7. **Neutral stance.** Don't champion FPF; don't defend Jetix. Report
   honestly.

---

## Success criteria

- [ ] All 4 primary inputs read fully (KB, FPF-Spec, ADR, D9 draft)
- [ ] All 11 FPF-Spec Parts mapped в Section 3
- [ ] Section 3 table has 100+ rows (pattern-by-pattern)
- [ ] 10-30 recommendations в Section 6 (prioritized P1/P2/P3)
- [ ] 5-15 open questions в Section 7 (с options + recommendation)
- [ ] Overall alignment score justified with evidence
- [ ] Commit + push successful
- [ ] Report generated

После этого analysis — Ruslan reviews + decides per recommendation.
Далее either ADR update (Chunk 8) или directly D6 writing.

---

**END OF TASK PROMPT**
