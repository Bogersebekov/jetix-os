---
type: task-prompt
stage: A (main orchestrator)
created: 2026-04-20
target: claude-code-on-server (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: design/JETIX-FPF.md v1 (30-40 pages)
uses: Task tool for spawning 3 FPF Scholar subagents + 1 Verifier subagent
estimated-time: 3-5 hours
status: ready-to-execute
---

# Stage A — D6 JETIX-FPF v1 Writing (Multi-Agent Orchestrator)

## Context

Ты — Claude Code на сервере Jetix OS. Тебе поручена **самая важная
работа Stage 4** — написание **D6 JETIX-FPF.md** — constitutional
документа онтологии Jetix.

**Это не обычное writing task.** Это **foundation** всего Jetix:
- Все 18 role-manifests читают D6 как primary reference
- Все agent system.md загружают full text D6 (OT5 override)
- D6 — основа для D1 (Architecture Final), D3 (Role Manifests), D5
  (Knowledge Architecture), D7 (Career Levels), D8 (Instructions)
- **Это sacred text Jetix methodology**

**Quality requirement:** **1000% depth, max Левенчук fidelity, zero
hallucinations, zero context loss.** Никакие compromises.

**Your strategy:** multi-agent orchestration. Ты — оркестратор. Spawn
**3 FPF Scholar subagents parallel** через Task tool — каждый deep
reads specific FPF Parts (Parts A-B / C-E / F-K). После integration —
spawn 1 Verifier subagent для cross-validation.

---

## Primary inputs (read at start)

### Jetix contextual (must-read fully):

1. **`decisions/gap-analysis-review-decisions-2026-04-20.md`** — **primary reference** для 60+ accepted decisions (5 Gaps + 22 Recs + 11 OQs + 9 Innovations, ~9K tokens)
2. **`decisions/2026-04-19-architecture-v2-approval.md`** — ADR Chunks 1-8 approved (1989 строк, ~40K tokens)
3. **`decisions/2026-04-20-jetix-architecture-final-DRAFT.md`** — D9 v0.6 clean consolidation (1880 строк, ~38K tokens)
4. **`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`** — compiled KB (2456 строк, ~50K tokens)
5. **`raw/research/fpf-gap-analysis-2026-04-20.md`** — Gap Analysis (2486 строк, ~50K tokens)

### FPF supporting (reference, загружаешь selectively):

6. **`raw/external/ailev-FPF/FPF-Spec.md`** — 62,202 строк, 5.7 MB primary source. **NE загружай целиком** — это 1.24M tokens, exceeds window. Subagents делают focused reads per Part.
7. **`raw/external/ailev-FPF/Readme.md`** — entry routes (384 строк, ~8K tokens)
8. **`raw/external/ailev-FPF/ATTRIBUTION.md`** — citation requirements

### Left research materials (reference):

9. **`raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md`**
10. **`raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md`**
11. **`raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md`**
12. **`raw/research/levenchuk-fpf-research-2026-04-20/R-D-essence-kernel-shsm-relation.md`**
13. **`raw/research/levenchuk-fpf-research-2026-04-20/R-E-mereology-holon-hierarchy.md`**

---

## Deliverable — D6 JETIX-FPF.md v1

### File path
`design/JETIX-FPF.md`

### Size target
30-40 pages (v1 может slightly exceed — это ok для depth).

### Format
T-02 Oxide RFD template стиль, но адаптированный для constitutional document.

### Frontmatter

```yaml
---
id: JETIX-FPF
title: Jetix First Principles Framework — Constitutional Document
subtitle: Jetix-specific adaptation of First Principles Framework (FPF) by Anatoly Levenchuk
date: 2026-04-20
version: v1.0
state: draft
based-on:
  - FPF-Spec.md (Anatoly Levenchuk, March 2026 version, raw/external/ailev-FPF/)
  - Knowledge Base compilation (raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md)
  - ADR Chunks 1-8 approved (decisions/2026-04-19-architecture-v2-approval.md)
  - D9 Draft v0.6 (decisions/2026-04-20-jetix-architecture-final-DRAFT.md)
  - Gap Analysis 60+ decisions (decisions/gap-analysis-review-decisions-2026-04-20.md)
  - 5 Perplexity researches (raw/research/levenchuk-fpf-research-2026-04-20/)
attribution: >
  JETIX-FPF — Jetix-specific adaptation of First Principles Framework (FPF)
  by Anatoly Levenchuk (https://github.com/ailev/FPF). Upstream repo has
  no formal license; citation explicitly requested and provided.
  Internal Jetix use с adaptation.
lang: [ru, en]
scope: internal-only (per OT5 + OQ-09 A)
status: draft (unblocks Stage 4 D1/D2/D3/D4/D5/D7/D8 writing)
---
```

### Structure — 11 sections minimum

**ВАЖНО:** Below — **suggested structure**. Ты можешь adapt / reorder / extend
если improvement found. Но **все 11 sections должны иметь coverage.**

#### Section 1 — Target System (Jetix as holon)
~2-3 pages
- Jetix определение как holon
- Jetix как part-of Life-OS supersystem (lightweight mereology)
- L0-L7 7-layer architecture (Reference) vs 4-layer materialized (Operational)
- Nested Holonic Structure (OQ-06 B — FPF A.1 + A.14 canonical terminology)
- Connection к FPF A.1 Holonic Foundation + A.14 Advanced Mereology

#### Section 2 — Stakeholders
~2 pages
- Ruslan (primary executor, 5 atomic sub-roles)
- 11 Claude agents
- Future human hires (Phase 2a+)
- Advisory board (Anton, Vladislav, Rodion)
- Clients (DACH Mittelstand primary + US + RU secondary)
- Ecosystem Phase 3 (11 categories detailed)

#### Section 3 — Creation Graph (full 3-level mereological, MC3 override)
~4-5 pages (это большая section, includes typed edges per Rec-05)
- **Level 1 Target systems:** client-relationship, deal-opportunity, product-SKU, content-item, member-engagement, hypothesis, way-of-working, direction
- **Level 2 Creation systems:** 5 Ruslan sub-roles + 11 agent roles + 2 Phase 2a stubs + methodologies + processes
- **Level 3 Supersystems:** Jetix-Sales-Function, Jetix-Revenue-Engine, Jetix-Delivery-Function, Jetix-Ecosystem (Phase 3 hooks)
- **A.14 typed mereological edges** (Rec-05): ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf + Jetix-specific (creates / operates-in / methodologically-uses / constrained-by / fills)
- Reference к separate artifact `wiki/foundations/jetix-creation-graph.md`

#### Section 4 — Client Principles
~1-2 pages
- Respect / honesty / no-surprise
- DACH Konsenskultur alignment
- Mittelstand-specific engagement patterns

#### Section 5 — Internal Principles (8 principles + ШСМ 5 primitives)
~4-5 pages (deep section)

Eight internal principles (expanded to reflect all Chunk 8 adoptions):

1. **Role ≠ Executor strict separation** (P2 + A.2 Role Taxonomy FPF)
2. **Context is king** (agent reasoning must be context-grounded)
3. **Artifacts over conversations** (document the output)
4. **Meta-agent as immune system** (FPF-Steward sub-role, quarterly audit)
5. **Explicit alpha state transitions** (past-participle strict, MC6 + Hook 4)
6. **No role left undefined** (5-block role.md mandatory)
7. **Writing as thinking** (Левенчук's writing-as-thinking primitive)
8. **Agents as new participants of master class** (Левенчук Part 3 — onboarding required, not prompt loading)

Plus explicit forbidden: **dynamic role-switching by agent at task-time** (founder exception: Ruslan multi-role-binding).

**Cross-reference** к FPF Parts A (Roles), B (Reasoning), E (Constitution 11 Pillars).

#### Section 6 — 8 True Alphas (with A.14 typed mereology)
~3-4 pages
- **Client / Project / Deal / Content Item / Hypothesis / Member / Way of Working / Direction** (8-я alpha, Jetix innovation)
- **Past-participle state machines** для каждого (cite MC6 Hook 4)
- **Reclassified (NOT alphas):** Invoice (work product) / SKU (entity) / Postmortem (work product) / Research Note (work product of Knowledge)
- Cross-reference к SEMAT Essence Kernel legacy (R-D research)
- Cross-reference к FPF patterns A.2.5 U.RoleStateGraph, A.6 boundary discipline

#### Section 7 — Ritual Cadence + Strategizing as Event
~2-3 pages
- **4 rituals Phase 1** (Daily 30min / Weekly Friday 60min / Monthly last Friday 2h / Quarterly 1 day)
- **B.4 Canonical Evolution Loop mapping** (Rec-14): Observe / Reflect / Decide / Act per ritual cadence
- **Strategizing as trigger-driven event, NOT scheduled** (Левенчук §1.4 #1)
- **F.11 Method Quartet Harmonisation** (Rec-18): monthly per-direction check

#### Section 8 — U-Types Full (Deep Левенчук treatment)
~4-5 pages (deep section — "max depth" commitment)

**НЕ "Lite" 6 U-Types.** Full Левенчук treatment:
- U.System (Jetix как system; holons nested)
- U.Role (Jetix 18 role-manifests)
- U.Method (methodologies применяемые)
- U.Stakeholder (11 Ecosystem categories)
- U.Objective (quarterly attention-themes; direction goals)
- U.Decision (ADR + DRR records)
- U.Practice (ritual practices + protocols)
- U.Case (case studies — per Gap 3 CHR applications)
- U.Knowledge (wiki/ cross-cutting knowledge)
- U.Artifact (deliverables — role.md / binding.yaml / direction.md etc.)
- U.Holon (holonic structure нестинг)
- U.Episteme (FPF C.2.1 knowledge claims, epistemes)
- (Plus any additional U-Types applicable per FPF-Spec Parts exploration)

**LEX-BUNDLE 4-register naming** (per Gap 4 UTS + Rec-12): tech / plain / legacy / mnemonic per U-Type.

#### Section 9 — "What ШСМ is NOT" (protection section, expanded)
~2-3 pages
- ШСМ роль ≠ software class
- ШСМ alpha ≠ database table
- ШСМ creation graph ≠ workflow
- ШСМ strategizing ≠ planning meeting
- ШСМ thinking-by-writing ≠ documentation generation
- **Plus extensions:** FPF Holon ≠ software component; FPF Holon ≠ microservice; FPF Holon ≠ Kubernetes pod; etc.
- **Plus Jetix-specific:** "FPF" canonical (Левенчук's) ≠ JETIX-FPF (our adaptation — рandomization namespace clear)

#### Section 10 — Mereology + Holon Hierarchy (full, not lightweight)
~4-5 pages (deep — Левенчук excluded но Ruslan override MC3 full depth)

**Goes beyond "lightweight":**
- Leśniewski classical extensional mereology
- Lewis / Varzi mereological systems
- Kit Fine granular mereology (acknowledged, applicable где useful)
- Koestler holons + Wilber four-quadrants
- Mella / Jantsch organizational holons
- **Jetix holon hierarchy fully documented** (Ruslan / roles / agents / alphas / directions / Jetix / Life-OS supersystem)
- **A.14 typed mereology edges applied** (ComponentOf / PortionOf / PhaseOf / MemberOf / AspectOf / ConstituentOf)
- **Compose-CAL foundation** (C.13 — foundations для future composition)

Reference separate artifact `wiki/foundations/holon-hierarchy.md` (to be written Phase 1 post-D6).

#### Section 11 — 17 Trans-disciplines reference (или 16 per current FPF)
~3-4 pages

**Per R-C research findings** (may be 16, не 17 в current FPF — verify):
- Enumerate ~16-17 trans-disciplines Левенчук stack
- Hierarchy / dependencies
- Relation к 5 primitives (which underpin which)
- Relation к FPF-Spec Parts A-K
- **Jetix-specific subset:** which trans-disciplines Jetix practitioners (Ruslan + agents + future hires) need к master

Reference separate artifacts:
- `wiki/foundations/shsm-primitives.md` (5 primitives deep reference)
- `wiki/foundations/trans-disciplines.md` (17 disciplines full reference — to be written Phase 1)

#### Section 12 — Full FPF Architectural Invariants (deep Левенчук)
~2-3 pages

**Ruslan max-depth stance:** не excluded "full FPF architectural invariants".
List all invariants FPF-Spec declares:
- Holonic trinity (U.Entity → U.Holon → {U.System, U.Episteme})
- Transformer Quartet (A.3)
- Role-Method-Work alignment (A.15)
- 11 Pillars (E.2) + 4 Guard-Rails (E.5)
- Γ Universal Algebra (B.1)
- F-G-R Trust Calculus (B.3)
- CSLC Characteristic Spaces (A.17-21)
- Boundary Discipline L/A/D/E (A.6.B)

Each invariant: statement + Jetix implementation mapping.

#### Section 13 — Constructor/Category Theory Applications (where applicable)
~2 pages

**Per Ruslan max-depth:** не excluded "constructor/category theory".
Selectively apply where useful:
- Category theory — morphisms between epistemes (A.6.2 U.EffectFreeEpistemicMorphing)
- Constructor theory — Creation Graph depth (Deutsch/Marletto application points)
- Keep pragmatic — apply только где реально enables better reasoning

#### Section 14 — References + Cross-docs
~1 page
- Citations (FPF-Spec pattern IDs + line numbers)
- Cross-references к other Jetix documents (D1-D9, Constitution.md)
- Primary source acknowledgment (Anatoly Levenchuk, ailev/FPF)

### Total expected: **~40-50 pages** v1 (может slight overflow — depth >brevity).

---

## Process — Orchestration via Task tool subagents

### Step 1 — Read primary Jetix contextual inputs (~45-60 min)

Load all 5 primary Jetix contextual inputs (items 1-5 above). Build mental
model of Jetix architecture + all decisions + FPF alignment goals.

**Use Extended Thinking aggressively.**

### Step 2 — Spawn 3 FPF Scholar subagents в parallel (~2-3 hours)

Use Task tool с following configuration:

**Subagent Task 1 — "FPF Parts A-B Scholar":**

```
Prompt:
You are a focused FPF Scholar subagent. Your exclusive task:

1. Read raw/external/ailev-FPF/FPF-Spec.md Part A (Kernel Architecture) and 
   Part B (Aggregation + Trust + Reasoning cycles).
2. Extract key patterns with line numbers + exact definitions.
3. Pay special attention к:
   - A.1 Holonic Foundation
   - A.2 Role Taxonomy (+ A.2.1-A.2.9)
   - A.3 Transformer Quartet
   - A.6.* Boundary Discipline cluster (B/C/0/P/Q/A/H)
   - A.7 Strict Distinction
   - A.13 Agency
   - A.14 Advanced Mereology
   - A.15 Role-Method-Work
   - A.16 Language-State
   - A.17-A.21 Characteristic Space
   - B.1 Γ Universal Algebra
   - B.2 MHT Meta-Holon Transition
   - B.3 F-G-R Trust Calculus
   - B.4 Canonical Evolution Loop
   - B.5 Canonical Reasoning Cycle

Output (return to main session):
- Per-pattern structured notes:
  - Pattern ID + line number
  - Exact definition (quote or paraphrase)
  - Key relations to other patterns
  - Application hints for Jetix
- Critical dependencies / prerequisite patterns
- ~20K tokens structured notes

Tools: Read (FPF-Spec.md с line ranges), Grep (for specific pattern IDs).
Extended thinking on.
```

**Subagent Task 2 — "FPF Parts C-E Scholar":**

```
Prompt:
You are a focused FPF Scholar subagent. Your exclusive task:

1. Read FPF-Spec.md Part C (Kernel Extensions/CALs), Part D (Ethics),
   Part E (FPF Constitution + Authoring).
2. Extract patterns with line numbers + definitions.
3. Pay attention к:
   - C.2.1 U.Episteme
   - C.11 Decsn-CAL + C.12 ADR-Kind
   - C.13 Compose-CAL (Constructional Mereology)
   - C.18 NQD-CAL + C.19 E/E-LOG
   - C.22 Problem-CHR TaskSignature
   - D.5 Bias-Audit & Ethical Assurance
   - E.1 Vision + Mission
   - E.2 Eleven Pillars
   - E.5 Four Guard-Rails
   - E.5.1 DevOps Lexical Firewall
   - E.9 DRR (Decision Rationale Record)
   - E.10 LEX-BUNDLE
   - E.17 Multi-View Publication Kit (MVPK)
   - E.18 Transduction Graph Architecture
   - E.19 Pattern Authoring Discipline
   - E.20 Mechanism Introduction Protocol

Same output format: structured notes per pattern, ~20K tokens.
```

**Subagent Task 3 — "FPF Parts F-K Scholar":**

```
Prompt:
You are a focused FPF Scholar subagent. Your exclusive task:

1. Read FPF-Spec.md Part F (Unification), Part G (SoTA), Part H (Glossary),
   Part I (Walkthroughs), Parts J-K (Navigation/Extensions).
2. Extract patterns.
3. Pay attention к:
   - F.6 Role Assignment & Enactment Cycle
   - F.9 Bridges + CL (Congruence Level)
   - F.11 Method Quartet Harmonisation
   - F.17 UTS (Unified Term Sheet)
   - F.18 Cross-cultural patterns (если exist)
   - G.0 Frame Standard
   - G.1 CG-Frame Generator
   - G.2 SoTA Harvester
   - G.5 Multi-Method Dispatcher
   - H.1 Alphabetic Glossary
   - Any novel patterns в I-K

Same output format: structured notes per pattern, ~15-20K tokens.
```

**Важно:** 3 subagents run **parallel**. Main awaits all 3 выходов.

### Step 3 — Integrate subagent outputs + write D6 v1 (~2-3 hours)

After 3 subagents complete, main has:
- Jetix context (Step 1, ~300K tokens)
- 3 FPF digests (Steps 2 subagents, ~55K tokens combined)
- Output budget: 40-60K tokens (30-40 pages D6)

**Write D6 JETIX-FPF.md v1** following Structure above (Sections 1-14).

**Writing principles:**

1. **Russian primary**, English FPF citations verbatim
2. **Cite FPF pattern IDs** (e.g., "A.1 Holonic Foundation defines..." not vague references)
3. **Include line numbers** для direct quotes FPF-Spec (via subagent structured notes)
4. **Preserve Ruslan voice** где applicable (quotes из tracking file)
5. **Engineering-grade prose** — no fluff, dense content
6. **Past-participle convention strict** (MC6)
7. **Full depth** — Ruslan said "max Левенчук, no compromises" — deliver this
8. **Every Gap Analysis adoption integrated** explicitly (see below)

### Step 4 — Gap Analysis integrations checklist

Verify D6 v1 explicitly includes:

- [ ] **Gap 1 Boundary Discipline (A.6.*)** — Section 5 internal principles + Section 14 references
- [ ] **Gap 2 Trust F-G-R (B.3)** — Section 5 + Section 12 invariants
- [ ] **Gap 3 Characteristic Space (A.17-21)** — Section 12 invariants + hints за practical application
- [ ] **Gap 4 UTS (F.17)** + **LEX-BUNDLE (E.10)** — Section 8 U-Types Full с 4-register naming + reference к wiki/foundations/jetix-uts.md
- [ ] **Gap 5 Multi-View (E.17)** — Section 14 references (template implementation deferred к practice)
- [ ] **Rec-03 Bias-Audit (D.5)** — Section 12 invariants + reference к decisions/policy/bias-audit-cycle.md
- [ ] **Rec-05 A.14 typed mereology** — Section 3 Creation Graph explicitly types edges
- [ ] **Rec-06 B.2 MHT** — Section 7 Ritual Cadence или Section 14 references
- [ ] **Rec-08 Agency-CHR (A.13)** — Section 5 principles
- [ ] **Rec-14 B.4 Evolution Loop** — Section 7
- [ ] **Rec-18 F.11 Method Harmonisation** — Section 7
- [ ] **Все 9 Jetix innovations acknowledged** — Section 6 (Portfolio Direction alpha) + Section 5 (FPF-Steward etc.)

### Step 5 — Spawn Verifier subagent (~30-45 min)

Use Task tool:

**Subagent Task 4 — "D6 Cross-Reference Verifier":**

```
Prompt:
You are a D6 Cross-Reference Verifier subagent. Your exclusive task:

1. Read design/JETIX-FPF.md v1 (just written).
2. Для every FPF pattern ID cited (A.1, A.6.B, B.3, etc.):
   - Verify pattern exists in raw/external/ailev-FPF/FPF-Spec.md (Grep or Read)
   - Verify cited line number (if provided) matches actual content
   - Flag any mismatch or hallucinated patterns
3. Verify Russian/English terminology consistency.
4. Verify past-participle convention applied.
5. Check completeness vs Gap Analysis adoptions checklist (from Step 4 Main session).

Output (return to main):
- Verification report:
  - Patterns verified ✅ (count + sample)
  - Patterns flagged ⚠️ (specific issues + corrections)
  - Patterns invalid ❌ (hallucinated — remove or fix)
  - Completeness check results
  - Recommended fixes для main session
- ~5-10K tokens report

Tools: Read, Grep.
```

### Step 6 — Apply verification fixes (~30 min)

Main applies verifier recommendations → D6 v1 finalized.

### Step 7 — Commit + push

```
git add design/JETIX-FPF.md
git commit -m "[design] D6 JETIX-FPF v1 written — Hybrid Ultimate Stage A complete

Multi-agent orchestration:
- 3 FPF Scholar subagents (Parts A-B / C-E / F-K) parallel reading
- Main integrated subagent outputs + Jetix contextual (ADR/D9/gap analysis/KB/researches)
- Verifier subagent cross-validated citations

Content:
- 14 sections (Target System / Stakeholders / Creation Graph / Client Principles /
  8 Internal Principles / 8 True Alphas / Rituals / U-Types Full / What ШСМ is NOT /
  Mereology+Holons / 17 Trans-disciplines / FPF Invariants / Constructor/Category /
  References)
- 30-40 pages, max Левенчук depth
- All 22 Gap Analysis adoptions integrated
- Past-participle strict
- All FPF pattern IDs verified

Unblocks Stage B — 4 parallel perspective reviews.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin claude/jolly-margulis-915d34
```

### Step 8 — Report

Output:
- File path + line count
- Sections written (14) — high-level summary per section
- Subagent performance (tokens returned, time taken)
- Verifier findings summary (patterns verified, issues fixed)
- Gap Analysis adoptions checklist results
- Open items flagged для Stage B reviewers
- Commit SHA

---

## Configuration

- **Model:** Claude Opus 4.7 (1M context) — mandatory
- **Mode:** Extended thinking enabled, **max budget**
- **Temperature:** 0.3-0.4 (consistency > creativity для structural work)
- **Tool usage:** Read (inputs), Task (subagents), Write (D6), Grep (pattern verification), Bash (commit + push)

---

## Critical constraints

1. **Context window management:** не load full FPF-Spec.md в main session (1.24M tokens exceeds window). Subagents handle focused FPF-Spec reads.

2. **No hallucinations:** every FPF pattern ID cited must be verified в FPF-Spec via Grep/Read. Если не verified — flag + remove.

3. **Preserve depth:** Ruslan explicitly said "1000% depth, max Левенчук, no compromises". Err на stronger depth если ambiguous.

4. **Russian-primary voice:** sections написаны на Russian; English FPF citations verbatim.

5. **Past-participle strict:** все state mentions в past-participle.

6. **Cross-reference existing Jetix artifacts:** reference ADR, D9, Gap Analysis с precise paths.

7. **Internal-only stance:** D6 marked scope: internal-only (per OT5 + OQ-09 A). No publishing hints.

---

## Success criteria

- [ ] All 5 primary Jetix inputs read fully
- [ ] 3 FPF Scholar subagents spawned + outputs received
- [ ] Verifier subagent confirmed citations
- [ ] D6 v1 file written (30-40 pages)
- [ ] All 14 sections present
- [ ] All 22 Gap Analysis adoptions integrated
- [ ] All FPF pattern IDs verified (~80+ citations)
- [ ] Russian primary + English citations consistent
- [ ] Past-participle convention strict
- [ ] Commit + push successful
- [ ] Report generated с metrics

**После Stage A done — D6 v1 готов к Stage B (4 parallel perspective reviews).**

---

**END OF STAGE A TASK PROMPT**
