---
type: task-prompt
created: 2026-04-20
target: claude-code-on-server (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md
estimated-time: 2-4 hours focused synthesis
status: ready-to-execute
stage: Pre-Gap-Analysis Knowledge Base compilation
---

# Task — Compile Left-FPF Knowledge Base

## Context

Ты — Claude Code на сервере Jetix OS. Нужна **unified knowledge base** на
основе:

1. **5 Perplexity deep researches** (R-A до R-E) — ~394 KB combined material
2. **Официальная FPF specification** от Анатолия Левенчука (`raw/external/
   ailev-FPF/FPF-Spec.md`, 62,202 строки, 5.7 MB)

Эти два источника дадут comprehensive reference для последующего:
- Gap Analysis Jetix vs FPF (следующий шаг)
- D6 JETIX-FPF.md writing (позже)
- Long-term Jetix methodology canon

**Вызов:** FPF-Spec.md от Левенчука — **primary source** (author first-hand).
5 researches — **secondary** (third-party compiled сontext). **Triangulate**,
отмечай conflicts, prefer primary where authoritative.

---

## Inputs (read all)

### Primary source (authoritative)

**`raw/external/ailev-FPF/FPF-Spec.md`** (62,202 строки)
- Анатолий Левенчук, March 2026 version
- 11 Parts (A-K) + pattern language
- Holonic Foundation, Advanced Mereology, U.Episteme, DRR, UTS, etc.
- Requires 1M context window для full load (Opus 4.7)

**`raw/external/ailev-FPF/Readme.md`** (384 строки)
- Entry routes + quick-start

**`raw/external/ailev-FPF/ATTRIBUTION.md`**
- License status (no formal license, citation requested)

### Secondary sources (5 Perplexity deep researches, 2026-04-20)

**`raw/research/levenchuk-fpf-research-2026-04-20/`**:
- `R-A-levenchuk-full-body-of-work.md` (~63 KB) — Левенчук as person +
  full corpus: books, courses, evolution 2000-2026
- `R-B-shsm-5-primitives-deep.md` (~99 KB) — 5 примитивов ШСМ deep dive
  (роль / альфа / граф создания / стратегирование / мышление письмом)
- `R-C-17-trans-disciplines-mapping.md` (~95 KB) — full 17 trans-disciplines
  enumeration + hierarchy + relations к 5 примитивам
- `R-D-essence-kernel-shsm-relation.md` (~60 KB) — Essence Kernel + SEMAT
  adaptation → ШСМ evolution
- `R-E-mereology-holon-hierarchy.md` (~78 KB) — mereology theory + Holons
  (Koestler/Wilber/Fine) applied к organizations + AI-agent systems

---

## Deliverable

### File path

`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`

### Size target

**40-80 pages** structured knowledge reference. Could extend если material
truly требует — better complete than compressed.

### Format

Structured Markdown с:
- Clear hierarchy (H1/H2/H3/H4)
- Cross-references к source files (inline)
- Tables для compact reference
- Code blocks для examples / pattern IDs
- Glossary section (Russian + English equivalents)

### Frontmatter

```yaml
---
type: knowledge-base
compiled: 2026-04-20
purpose: Unified reference для Jetix FPF adaptation (Gap Analysis + D6 writing)
sources-primary:
  - raw/external/ailev-FPF/FPF-Spec.md (Anatoly Levenchuk, March 2026)
sources-secondary:
  - raw/research/levenchuk-fpf-research-2026-04-20/R-A через R-E (Perplexity, 2026-04-20)
size: XXK words
status: draft
unblocks:
  - Gap Analysis Jetix vs FPF
  - D6 JETIX-FPF.md writing
---
```

---

## Structure (recommended — adapt if improvement found)

### Section 1 — About this knowledge base (500-700 words)

- Purpose (Jetix FPF derivation)
- Sources overview (primary FPF-Spec + 5 secondary researches)
- Triangulation methodology used
- Anti-hallucination commitments
- How to use this document

### Section 2 — Anatoly Levenchuk — intellectual context (800-1200 words)

Based primarily on R-A, supplemented where FPF-Spec gives his own voice.

- Biographical sketch
- Intellectual lineage (Russian methodological school, Western systems thinking)
- Career arc (2000-2010 IT → 2010-2020 ШСМ → 2020-2026 AI-augmented)
- Current 2026 focus (FPF as latest framework)
- Where his body of work lives (ШСМ courses, books, FPF GitHub repo)

### Section 3 — ШСМ 5 primitives (deep, 2500-3500 words)

Based primarily on R-B, cross-referenced с FPF-Spec patterns где applicable.

One subsection per primitive:
3.1 **РОЛЬ (Role)** — definition, role vs executor, multi-role exec critique
3.2 **АЛЬФА (Alpha)** — definition, past-participle convention, states,
    Alpha vs Work Product vs Entity
3.3 **ГРАФ СОЗДАНИЯ (Creation Graph)** — mereological structure,
    target/creation/supersystem levels
3.4 **СТРАТЕГИРОВАНИЕ (Strategizing)** — event-not-ceremony, invent mode,
    AI limitation
3.5 **МЫШЛЕНИЕ ПИСЬМОМ (Writing-as-Thinking)** — externalization of cognition

For each:
- Primary definition (quote source)
- Cross-reference to relevant FPF-Spec patterns (if any)
- "What it is NOT" protection list
- Application examples
- Common mistakes

### Section 4 — 17 Trans-disciplines structure (2000-3000 words)

Based primarily on R-C.

4.1 Concept of trans-discipline
4.2 Enumeration of 17 (one-paragraph each + hierarchy)
4.3 Hierarchical structure + dependency graph
4.4 Relation к 5 primitives
4.5 Relation к FPF-Spec Parts A-K (if mapping exists)

### Section 5 — FPF-Spec Architecture (4000-6000 words) ⭐ CRITICAL

**Это самая важная section** — первичная дistillation of 62K-line FPF-Spec
для reuse. Digest FPF-Spec thoroughly.

5.1 **FPF at a glance**
- What FPF solves (coordination bottleneck, human/AI teams)
- Entry routes (6 patterns из Readme.md)
- Difference from project methodology (FPF is not shrink-wrapped)

5.2 **Parts overview** — each Part A through K:
- **Part A — Kernel Architecture**: holons, bounded contexts, roles,
  scopes, transformers, time/evolution, measurement/comparability
- **Part B — Aggregation**: Universal Algebra (Γ), Meta-Holon Transitions
- **Part C — CAL**: Sys-CAL, Episteme-CAL, KD-CAL, Compose-CAL
- **Part D — Conflict Topology**: holonic conflicts + resolution
- **Part E — Pattern Authoring + Multi-View Publication**
- **Part F — Bridges + Cross-Linking**
- **Part G — Selection Mechanisms + Comparison**
- **Part H — Glossary** (alphabetical)
- **Part I — Walkthroughs**
- **Part J — Route Explanations**
- **Part K — Extensions**

Per Part: 200-400 words digest + key patterns (A.1, A.14, A.6, B.1, etc.)

5.3 **Key FPF concepts** — deep definitions:
- **Holon** (A.1) — whole-and-part; Entity→Holon
- **Advanced Mereology** (A.14) — ComponentOf, PortionOf, PhaseOf
- **U.System + U.Episteme** (A.6, C.2) — system vs knowledge claim
- **DRR** (Decision Rationale Record) — formalized ADR
- **UTS** (Unstable Term Sheet) — vocabulary discipline
- **Bounded Contexts** — scope boundaries
- **Claim Register** — decomposing mixed boundary text
- **Traditioncard + OperatorCard** — SoTA portfolio
- **Gamma (Γ) operator** — aggregation operator
- **Meta-Holon Transition (MHT)** — emergence + re-identification
- Other core concepts (scan FPF-Spec deep sections)

5.4 **FPF unique commitments** — 9 "big storylines" (per A.0 intro):
- Holonic kernel
- Explicit creativity treatment
- Assurance first-class
- [list all 9 from FPF-Spec]
- Why FPF unique vs other frameworks

### Section 6 — Essence Kernel + SEMAT legacy (1500-2500 words)

Based primarily on R-D.

6.1 Essence Kernel original (SEMAT, OMG standard)
6.2 Levenchuk's adaptation путь: Essence → ШСМ → FPF
6.3 What он kept unchanged / modified / rejected / added
6.4 Alpha concept evolution (Essence alpha → ШСМ alpha → FPF treatment)
6.5 Current FPF relationship к Essence (deprecated? continued reference?)

### Section 7 — Mereology + Holon Hierarchy (2500-3500 words)

Based primarily on R-E, cross-ref с FPF A.1 + A.14.

7.1 **Foundational mereology** (Leśniewski → Lewis → Fine)
7.2 **Koestler holons** + Wilber four-quadrants
7.3 **FPF's mereological treatment** (A.1 Holonic Foundation + A.14
    Advanced Mereology — deep)
7.4 **Organizational applications** (Sociocracy 3.0, Holacracy, Teal orgs)
7.5 **AI agent systems** (multi-agent systems + LLM ensembles as mereology)
7.6 **Beyond Левенчук's "lightweight"** — Kit Fine, constructor theory,
    category theory — when applicable

### Section 8 — Intersections, conflicts, convergence (1500-2500 words)

**Critical section — triangulation results:**

8.1 **Where all sources agree** — core concepts all sources endorse
8.2 **Where FPF has evolved past older ШСМ sources** — R-B may describe
    older version that FPF-Spec now refines
8.3 **Where sources conflict** — flag explicitly, prefer FPF primary
8.4 **Gaps** — what researches missed that FPF-Spec covers
8.5 **Counter-gaps** — what researches cover that FPF-Spec doesn't
    (e.g., Левенчук biographical from R-A not in FPF-Spec)

### Section 9 — Terminology glossary (reference)

Complete glossary: Russian term → English term → definition → source.
Include все terms from all sources. Critical for D6 writing + cross-refs.

### Section 10 — Recommended reading / learning order

Based on all sources, propose optimal learning path for:
- **Total beginner** к Левенчук methodology
- **Practitioner with Essence background** (e.g., software engineer)
- **Jetix-specific adapter** (our use case)

### Section 11 — Open questions / uncertainties

Flag things that need Ruslan review OR next-wave research:
- Terms seen в only one source (verify or discard?)
- Apparent contradictions between sources (which to trust?)
- FPF concepts that may not apply к solo-founder context
- Etc.

---

## Quality requirements

### Source fidelity

- **Direct quotes** где FPF-Spec gives authoritative definition — use
  quotation с citation
- **Preserve Russian terms** с English transliteration везде
- **Cite specific FPF-Spec pattern IDs** (A.1, B.1.3, C.2.1, etc.) — not
  vague references
- **Cite specific research files** (R-A section X.Y) для secondary sources

### Anti-hallucination

- If information appears in only one source и contradicts another — flag
  explicitly, don't silently pick
- If a term / concept mentioned but not defined anywhere → flag, don't
  guess
- If FPF-Spec pattern referenced не findable в actual FPF-Spec → note
  as "пattern ID not verified in source"

### Precision over comprehensiveness

- **Don't pad.** Empty words detract.
- **If section is shorter because material thin — accept it.**
- **If section is longer because material deep — accept это.**
- Target ranges are guides, not requirements.

### Primary > Secondary где conflict

FPF-Spec (Левенчук first-hand) > Perplexity research (third-party compile).
Flag conflicts explicitly.

---

## Process

### Step 1 — Read all inputs (~60-90 min)

Use Opus 4.7 1M context to load everything:

1. `raw/external/ailev-FPF/Readme.md` (start — overview, entry routes)
2. `raw/external/ailev-FPF/ATTRIBUTION.md` (usage scope understanding)
3. `raw/research/levenchuk-fpf-research-2026-04-20/R-A` (biographical)
4. `raw/research/levenchuk-fpf-research-2026-04-20/R-B` (5 primitives)
5. `raw/research/levenchuk-fpf-research-2026-04-20/R-C` (17 trans-disciplines)
6. `raw/research/levenchuk-fpf-research-2026-04-20/R-D` (Essence Kernel)
7. `raw/research/levenchuk-fpf-research-2026-04-20/R-E` (mereology + holons)
8. `raw/external/ailev-FPF/FPF-Spec.md` (**62K lines — primary source,
   читай полностью в context window**)

**Use Extended Thinking aggressively** during reads — build full mental
model before writing.

### Step 2 — Outline (~15-20 min)

Write detailed outline section-by-section. Verify:
- Каждое major concept из любого source — has home в outline
- Triangulation analysis planned где sources cover same topic
- Glossary covers all Russian + English terms

### Step 3 — Write document (~90-180 min)

Sections 1-11 в order. Use Extended Thinking для:
- Section 5 (FPF architecture digest — most complex)
- Section 8 (intersections/conflicts analysis)
- Decision moments where sources conflict

### Step 4 — Self-review pass (~30-45 min)

Read full draft. Check:
- **Coverage:** все inputs reflected?
- **Citations:** pattern IDs verified? research section references correct?
- **Triangulation:** FPF primary honored where conflict?
- **Glossary completeness**
- **Length range achieved** (40-80 pages)

### Step 5 — Commit + push

Commit message:

```
[research] Levenchuk+FPF unified knowledge base (pre-Gap-Analysis compilation)

Compiled from:
- raw/external/ailev-FPF/FPF-Spec.md (primary, 62K lines, Левенчук March 2026)
- raw/research/levenchuk-fpf-research-2026-04-20/ (5 Perplexity researches)

11 sections covering: Левенчук intellectual context / 5 ШСМ primitives /
17 trans-disciplines / FPF-Spec architecture (Parts A-K) / Essence Kernel
evolution / mereology + holons / triangulation + conflicts / glossary.

Unblocks: Gap Analysis Jetix vs FPF (next task).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

Push to `claude/jolly-margulis-915d34` branch.

### Step 6 — Report

Output short report:
- File path + line count
- Sections written list
- Major FPF-Spec insights что materially affect Jetix architecture
- Open questions / flagged items (if any)
- Commit SHA

---

## Configuration

- **Model:** Claude Opus 4.7 (1M context) — mandatory для reading 62K-line FPF-Spec
- **Mode:** Extended thinking enabled, max budget
- **Temperature:** default (0.3-0.4)
- **Tool usage:** primarily Read + Write. Minimal Bash.

---

## Important notes

1. **FPF-Spec.md является primary source.** Если research заявляет
   что-то про ШСМ что FPF-Spec refines или расширяет — honor FPF-Spec.

2. **Research R-B (5 primitives)** потенциально describes older ШСМ
   version. FPF-Spec может have evolved beyond that. Flag evolutions.

3. **17 trans-disciplines** — R-C может be best source (FPF-Spec focuses
   on kernel + patterns, не on курса curriculum).

4. **Биографический материал R-A** — not в FPF-Spec; preserve from research.

5. **Mereology depth** — R-E + A.14 FPF-Spec → both substantial, blend
   insights carefully.

6. **Don't replicate FPF-Spec in its entirety.** Digest: capture essential
   concepts, не full spec. Knowledge Base = reference, not copy.

7. **Russian-first где Левенчук использует Russian.** English translations
   в глоссарии, но Russian primary в concept definitions.

---

## Success criteria

- [ ] All 6 input files read fully (ATTRIBUTION + Readme + FPF-Spec + R-A-E)
- [ ] 11 sections written
- [ ] 40-80 pages length
- [ ] FPF-Spec primary source respected (conflicts flagged, not silently
      resolved)
- [ ] Glossary complete
- [ ] Commit + push successful
- [ ] Open questions / uncertainties flagged
- [ ] Report generated

После этой compilation — следующий task будет **Gap Analysis Jetix
architecture vs FPF** используя:
- Knowledge Base (this output)
- FPF-Spec.md (primary)
- Jetix ADR + D9 draft

---

**END OF TASK PROMPT**
