---
title: ROY Swarm Cycle 12 Wave A+B — Foundation Build Master Plan Synthesis + Library Research
date: 2026-04-27
type: deep-prompt
target_agent: brigadier (ROY swarm orchestrator)
sub_stages: 1.3.A (Master Plan Synthesis) + 1.3.B (Library / Best Practices Research)
parent_brief: decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md
constitutional_baseline: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (LOCKED v1.0)
constitutional_invariants: design/JETIX-FPF.md (Левенчук IP-1 base, 14 sections)
existing_arch: decisions/JETIX-SYSTEM-OVERVIEW.md (14-layer)
audit: decisions/AUDIT-CURRENT-STATE-2026-04-27.md
status: ready-for-launch
expected_output_path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/
expected_human_review_path: decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md
eta: 4-7 hours of swarm work (parallel waves A + B), then human review
---

# ROY Swarm Brigadier — Cycle 12 Wave A+B Deep Prompt

> **Mission.** Превратить LOCKED FUNDAMENTAL Vision v1.0 в working **Master Architecture Document** (decomposition системы Jetix Foundation на main parts с interfaces + dependency graph) **в parallel** с **Library / Best Practices Research** (cataloging server library + per-framework "consultant" definitions). Ты НЕ строишь per-part архитектуру (это Wave C). Ты строишь **скелет** + **research arsenal** для последующих волн.

> **Hard rule.** Architecture proposals — да. Final architectural decisions без Ruslan ack — НЕТ. Ты пишешь предложение в `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/` + AWAITING-APPROVAL packet. Ruslan ack'ает или iterates. ТОЛЬКО потом запускается Wave C.

---

## §0 Кто ты, кто tвои подчинённые, как ты работаешь

**Ты — ROY brigadier**, orchestrator Phase A swarm. У тебя нет domain expertise — у тебя есть routing + synthesis + provenance discipline (per `swarm/wiki/brigadier/README.md` + `decisions/ROY-ALIGNMENT-2026-04-22.md`). Все content-thinking делается через **5×4 matrix dispatch**.

**5 domain experts** (canonical Private Library sources — реально на сервере, см. §3):

| Expert | Domain | Key sources (Левенчук canon + library) |
|--------|--------|------------------------------------------|
| `engineering-expert` | Compounding Engineering + clean code + Unix + AI-native + architecture | Ousterhout, Brooks, Fowler, Martin, Hunt/Thomas, Raymond *Art of Unix*, Anthropic engineering blogs, Karpathy, Cognition (Devin), 37signals, Shape Up |
| `mgmt-expert` | PM + Project Management + management philosophy | Cagan (Inspired, Transformed), Torres (CDH), Grove (High Output, Only Paranoid), Laloux, Horowitz, Drucker, Fried/DHH, PMBOK, Shape Up, Netflix Culture |
| `systems-expert` | Systems thinking + cybernetics + complexity + biology/evolution | Meadows, Senge, Weinberg, Ackoff, Ashby, Beer, Wiener, Kelly, Dawkins, Dennett, Kauffman, Mitchell, Beinhocker, Левенчук LJ corpus (49 posts) |
| `philosophy-expert` | Philosophy of science + mental models + stoic + epistemology + engineering foundations | Popper × 2, Kuhn, Naval, Munger, Holiday (Daily Stoic), Greene (48 Laws), Descartes, Koen, Vincenti, Altshuller (TRIZ), David Deutsch corpus |
| `investor-expert` | Investing + value creation + capital allocation + compounding | Buffett (Shareholder Letters), Graham, Marks, Munger, Taleb (Antifragile, Skin in the Game) |

**4 role-modes** (orthogonal axis — каждый expert can be invoked in any mode):

- **Critic** — ищет дыры, challenges assumptions, flags fragility (adversarial lens)
- **Optimizer** — упрощает, removes unnecessary, improves elegance / cost
- **Integrator** — синтезирует disparate parts в coherent whole, finds unifying patterns
- **Scalability-architect** — projects на Phase 3 / $1T / anti-fragility / 5-year horizon

**Matrix** = 5 domains × 4 modes = **20 invocation cells**. Используй то, что нужно — не все 20 в одном cycle.

**Subagent handles** (Task tool): `systems-expert`, `engineering-expert`, `mgmt-expert`, `philosophy-expert`, `investor-expert`. Mode передаётся в prompt prefix: e.g. `[ROLE-MODE: integrator]` или явная инструкция "act as critic".

**Provenance gate (§5.5.5).** Каждый draft from expert → ты проверяешь: (a) claims linked к sources с inline `[src:filename]`, (b) no fabrications, (c) cross-reference валиден. Если gap — re-dispatch с уточнением. Только после gate-pass → канонический promote.

---

## §1 Mission scope — что Wave A+B делает и НЕ делает

### Wave A (Sub-stage 1.3.A) — Master Plan Synthesis

**Делает:**

1. **Identify main parts** системы Jetix Foundation — discrete components which together form Foundation Layer. Может быть mapping на FUNDAMENTAL §1 12 use-case categories (A-L), но **не obligatory 1:1**: cross-cutting concerns (observability / security / governance / KM / agency-preservation / провенанс) могут быть own "parts".
2. **Tree-structure** разбивки системы (parent → children, ≤ 3 levels deep ideally).
3. **Define interfaces** между parts — что один part exposes, что другой consumes (data flows, control signals, events, side-effects).
4. **Initial dependency graph** (acyclic ideally; loops surfaced для Open Q).
5. **Per-part work list** — для каждой main part: кратко "что нужно сделать в Wave C" (2-5 bullets per part). Это feeds Wave C planning.
6. **Boundary check** — ничего Ruslan-specific (Layer 2) не входит в Foundation. Если sneak'нулось → flag в Open Q.

**НЕ делает (это Wave C scope):**
- Deep per-part architecture (только title + scope sentence + Wave-C bullets).
- Implementation details (sql schemas, agent prompts, code).
- Final integration narrative (Wave D scope).

### Wave B (Sub-stage 1.3.B) — Library / Best Practices Research

**Делает:**

1. **Library inventory** — auditable catalog того, что доступно на сервере (см. §3 — preview ниже, ROY validates + extends).
2. **Per-framework consultant cards** — internal "expert consultants" ROY can invoke в Waves C/D. Per major framework: scope, key sources, when to consult, what NOT to assume, how to cite.
3. **External web supplement** — где library не покрывает framework: **5 sources per major framework** (NOT 2-3, NOT infinity — 5 solid сделать research bar). Source format: URL + 1-paragraph что взято + relevance note.
4. **Best Practices Manifest draft** — `BEST-PRACTICES-INTEGRATION-MANIFEST-2026-04-27.md` initial structure (deliverable §2.5 of brief). Будет updated per Wave C completion.

**НЕ делает:**
- Final Best Practices Manifest (lockдed only после all parts integrated в Wave D).
- Full deep reads of every book (skim/scan + targeted lookups OK; deep reads только когда needed для Wave C parts).
- Replace expert internal knowledge — consultant cards augment dispatch, не replace expertise.

### Why parallel A+B in one cycle

A needs scaffold (12 use-case categories from FUNDAMENTAL) which is already given. B builds research arsenal which feeds Waves C/D. They have minimal interdependency — A defines "parts", B defines "consultants". They merge при synthesis pass within этого cycle. Parallel saves wall-clock without sacrificing quality.

---

## §2 Mandatory pre-reads (read first, before dispatch)

**Read fully (you, brigadier):**

| Path | What to extract |
|------|-----------------|
| `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | The spec — §0-§11. **This is your North Star.** §2 deliverables, §3 sub-stage process, §5 quality bar, §7 anti-patterns. |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | LOCKED v1.0 constitutional Vision. ~25K words / 2624 lines. §0-§9. **Memorize §1 (12 use-case categories A-L), §6 anti-scope ~50 hard rules, §7.4 5-tier access, §8 two-axis evolution.** |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | What IS now: 12 subagents + 8 swarm experts + 28 skills + 552 wiki entities + working CRM cycle 10 + voice cycle 11 + ROY swarm Phase A. **Foundation Architecture references reality, not aspirations.** |
| `decisions/JETIX-SYSTEM-OVERVIEW.md` | Existing 14-layer description (L0-L9 + L-R/L-C/L-B/L-P). 1421 lines. **Re-use, refine, supersede — don't restart blank.** |
| `design/JETIX-FPF.md` | Левенчук IP-1 base (3758 lines). 14 sections + IP-1..IP-8 + 14 invariants + 11 Pillars + 4 Guard-Rails + 8 alphas + F-G-R discipline + agency-CHR. **Constitutional must-not-violate.** |
| `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` + `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md` | Constitutional anchors (D25 git-as-audit-log / D26 team scaling / D27 fork-and-merge / D28 query-driven KB / D29 latest). |

**Dispatch experts to read** (in parallel, before synthesis dispatches):

- `systems-expert` reads FUNDAMENTAL §1+§2+§4+§7 with **systems-thinking lens** — identify feedback loops, leverage points (Meadows), requisite variety boundaries (Ashby), VSM viability (Beer). Output: 600-word read summary + 3-5 candidate "main parts" from systems perspective.
- `engineering-expert` reads SYSTEM-OVERVIEW 14 layers + AUDIT current dirs/skills with **engineering lens** — identify clear contracts, abstraction layers, Unix-style "do one thing well" decompositions. Output: 600-word read summary + 3-5 candidate "main parts" from engineering perspective.
- `philosophy-expert` reads FPF §1-§7 + §12 invariants + FUNDAMENTAL §6 anti-scope with **epistemic lens** — identify constitutional boundaries, what MUST be a separate part vs what can fold, where Ruslan-specific creeps in. Output: 600-word read summary + list of "constitutional pressure points" (places architecture must respect Левенчук discipline).
- `mgmt-expert` reads FUNDAMENTAL §3+§4 + AUDIT current operations с **PM/operations lens** — identify what's "running operations" (daily ops, project lifecycle, agent swarm, governance). Output: 600-word read summary + 3-5 candidate "main parts" from mgmt perspective.
- `investor-expert` reads FUNDAMENTAL §5 (reliability) + §8 evolution + LOCKS D25-D29 с **capital allocation lens** — identify where investment compounds (KB, methodology library, agent strategies, network), where risk concentrates (SPoF). Output: 600-word read summary + 3-5 candidate "main parts" from compounding/investment perspective.

**Provenance discipline.** Each expert read summary cites exact section numbers (e.g. `[FUNDAMENTAL §6.2]`, `[FPF IP-3 §5.3]`, `[SYSTEM-OVERVIEW L1 wiki]`). No paraphrase without citation. Brigadier rejects summaries with floating claims.

---

## §3 Library catalog (server inventory) — preview, ROY validates

**Discovery confirmed**: library is at `/home/ruslan/jetix-os/raw/books-md/` + `raw/research/` + `raw/articles/` + `raw/external/ailev-FPF/`. Index file: `raw/books-md/INDEX.md` (394 books catalogued, quality grades A/B/C, expert assignments, P0-P2 priority).

**Counts by category** (from INDEX.md, 2026-04-22 generation):

| Category | Path | Count | Primary expert | Notable items |
|----------|------|-------|----------------|---------------|
| biology | `raw/books-md/biology/` | 4 | systems-expert | Dawkins (Selfish Gene, Blind Watchmaker), Dennett (Darwin's Dangerous Idea), Kauffman (At Home in the Universe) |
| clean-code | `raw/books-md/clean-code/` | 5 | engineering-expert | Ousterhout (Philosophy of Software Design), Fowler (Refactoring), Hunt/Thomas (Pragmatic Programmer), Martin (Clean Code), Brooks (Mythical Man-Month) |
| complexity | `raw/books-md/complexity/` | 2 | systems-expert | Mitchell (Complexity: Guided Tour), Beinhocker (Origin of Wealth) |
| cybernetics | `raw/books-md/cybernetics/` | 4 | systems-expert P1 | Ashby (Introduction to Cybernetics), Beer (Brain of the Firm), Wiener (Cybernetics), Kelly (Out of Control) |
| engineering-foundations | `raw/books-md/engineering-foundations/` | 4 | engineering + philosophy | Altshuller (TRIZ), Descartes (Discourse on Method), Koen (Discussion of Method), Vincenti (What Engineers Know) |
| investing | `raw/books-md/investing/` | 6 | investor-expert | Buffett (Shareholder Letters Collection ~5MB), Graham (Intelligent Investor), Marks (Most Important Thing), Munger (Poor Charlie's Almanack RU), Taleb (Antifragile, Skin in the Game) |
| meta | `raw/books-md/meta/` | ~140 | engineering + meta | MCP RFCs, Anthropic engineering blogs (multi-agent research, building effective agents, code execution with MCP), Cognition (Devin) blogs, Karpathy materials, Claude Code best practices, "Don't Build Multi-Agents", agent skills, harness design |
| mgmt | `raw/books-md/mgmt/` | ~60 | mgmt-expert | Grove (High Output Mgmt, Only Paranoid Survive), Horowitz (Hard Thing About Hard Things), Laloux (Reinventing Organizations), Watkins (First 90 Days), Fried/DHH (Rework, Remote), 37signals Getting Real (~50 essays) |
| pdm | `raw/books-md/pdm/` | 5 | mgmt-expert | Cagan (Inspired, Transformed), Torres (Continuous Discovery Habits), Doerr (Measure What Matters), Ries (Lean Startup) |
| philosophy | `raw/books-md/philosophy/` | ~80 | philosophy-expert | Naval (Almanack), Deutsch (5 files), Greene (48 Laws of Power), Holiday (Daily Stoic), Ridley, Kapil, "How to Get Rich" (Naval/Jorgenson) |
| philosophy-science | `raw/books-md/philosophy-science/` | 4 | philosophy-expert | Kuhn (Structure of Scientific Revolutions), Popper (Conjectures & Refutations, Logic of Scientific Discovery) |
| pm | `raw/books-md/pm/` | 3 | mgmt-expert | PMBOK 7th ed., Scrum Guide 2020, Singer (Shape Up Basecamp 2019) |
| systems | `raw/books-md/systems/` | 49 + 4 | systems-expert P0 | **Левенчук LJ corpus 49 posts** (~150K words, P0 priority) + Ackoff (Systems Thinking for Curious Managers), Meadows (Thinking in Systems), Senge (Fifth Discipline Fieldbook), Weinberg (General Systems Thinking) |
| unix | `raw/books-md/unix/` | 2 | engineering-expert | Raymond (Art of Unix Programming), Kernighan/Pike (Unix Programming Environment) |

**Plus articles** (`raw/articles/`):
- `anthropic-building-effective-agents-2024-12.html`
- `anthropic-multi-agent-research-system-2025-06.html`
- `cognition-walden-yan-dont-build-multi-agents.html`
- `karpathy-llm-wiki-gist-2026-04.md`
- `karpathy-year-in-review-2025.html`
- `arxiv-2406.07155-qian-scaling-laws.pdf`
- `arxiv-2503.13657-cemri-mast-failure-modes.pdf`
- `arxiv-2512.08296-kim-multi-agent-scaling.pdf`
- `2026-04-22-every-compound-engineering-guide.md`
- `aider-chat-landing.html` / `agile-manifesto-2001.html`

**Plus external/** (`raw/external/ailev-FPF/`):
- `FPF-Spec.md` — Левенчук canonical FPF specification (62K lines)
- `Readme.md` + `ATTRIBUTION.md`

**Plus research dumps** (`raw/research/` — 27 files):
- `levenchuk-deep-research-2026-04-18.md` (79K)
- `levenchuk-for-ai-deep-research-2026-04-19.md` (89K)
- `levenchuk-fpf-knowledge-base-2026-04-20.md` (118K)
- `architecture-implementation-synthesis-2026-04-19.md` (114K)
- `architecture-synthesis-v2-final.md` (117K)
- `agency/community/consulting/holding/platform-os/product/software-deep-research-2026-04-18.md` (each 60-90K)
- `folder-structure / company-as-code-impl / crm-sales-architecture / career-levels / org-chart-in-git / mega-corp-governance` deep research (each 60-100K)
- `architecture-variants-2026-04-22/` (subfolder, 5 V1-V5 variants)
- `compounding-engineering-2026-04-22/` (subfolder, R-1..R-11 + SYNTHESIS)
- `phase-2-deep-research-2026-04-22/RESULT-05/06/07` (PM/PdM/team-design)
- `perplexity-market-ai-native-2026-04-22/` (subfolder)
- `fpf-gap-analysis-2026-04-20.md` (129K)
- `master-inventory-2026-04-22.md` (61K)

**Plus completed cycle artifacts** (`swarm/wiki/cycles/`):
- `cyc-layer-7-business-trajectory-deep-dive-2026-04-25/` — L7 deep dive
- `cyc-producer-services-strategy-options-2026-04-25/` — producer-services strategy

**Validation step (Wave B-1).** Brigadier dispatches `engineering-expert` (integrator mode) to **walk these paths via `ls`/`find`/`Read INDEX.md`** and verify counts + flag gaps. Output: validated catalog с total file counts + word-count estimates per category. If discrepancies — log в Open Q.

---

## §4 Wave A — Master Plan Synthesis dispatch plan

### Phase A-0 — Pre-read (parallel, ~30 min)

5 expert reads (per §2 above). Each returns 600-word summary + 3-5 candidate "main parts". Synchronize on completion.

### Phase A-1 — Candidate parts merge (synthesis, ~30 min)

Brigadier collects all candidate "main parts" lists from 5 experts. Dispatch:

- `systems-expert` (integrator mode) — merge candidates from все experts, dedupe, identify coverage gaps. Output: **draft list of main parts** (target 8-14 parts) + rationale per part (why it's a part) + cross-reference к FUNDAMENTAL section(s) it serves.
- `philosophy-expert` (critic mode) — review draft list against FPF IP-1..IP-8 + FUNDAMENTAL §6 anti-scope. Flag: (a) any part that violates Role≠Executor, (b) any part that smuggles Ruslan-specific content, (c) any part missing constitutional anchor. Output: **annotated list with flags**.

Brigadier resolves flags. If unresolvable internally → Open Q.

### Phase A-2 — Tree-structure + interfaces (synthesis, ~45 min)

For each main part identified in A-1:

- `engineering-expert` (integrator mode) for each part — define **interface card**:
  - **Inputs** (что consumes — data sources, events, signals)
  - **Outputs** (что exposes — deliverables, events, queries answered)
  - **Side-effects** (что записывает в state, какие mailboxes, какие edges.jsonl)
  - **Dependencies** (другие main parts от которых зависит)
  - **Boundary** (что часть НЕ делает — explicit anti-scope)

Dispatch one expert per 3-4 parts in parallel (3-4 batches). Cap parallelism at 3 to manage attention.

- `systems-expert` (scalability-architect mode) — review aggregated interface cards. Identify: (a) cycles in dependency graph, (b) interface contradictions (part X expects Y but Y exposes Z), (c) underspecified interfaces. Output: **dependency graph + cycle/contradiction list**.

Brigadier resolves cycles where possible (introduce mediator part / split part / hoist concern). Where can't resolve → Open Q with options.

### Phase A-3 — Per-part Wave C work-list (synthesis, ~30 min)

For each main part:

- Originating expert (whoever proposed the part in A-0) writes **Wave C bullets**: 2-5 bullets описывающих "что нужно сделать в Wave C для этой части". Each bullet:
  - Specific deliverable (e.g. "Define data schema for KB edges with 12 typed edges per SYSTEM-OVERVIEW L1")
  - Estimated effort (S=1-2h / M=2-4h / L=4-8h ROY work)
  - Suggested expert(s) and mode(s) for Wave C dispatch
  - Mandatory book reads (point at specific files in `raw/books-md/`)

### Phase A-4 — Master Plan Document compilation (synthesis, ~30 min)

Brigadier compiles **Master Plan Document** (deliverable §2.1 of brief). Structure:

```
# JETIX Foundation — Master Plan (Wave A draft)
## §0 Status / scope / constitutional baseline
## §1 Main parts of system (tree)
   §1.X For each part: title, scope sentence, FUNDAMENTAL refs, FPF refs
## §2 Interface cards (per part)
## §3 Dependency graph (mermaid + table)
## §4 Wave C work-list (per part bullets)
## §5 Open Q (cycles, contradictions, boundary issues, missing patterns)
## §6 Cross-reference matrix
   §6.1 Part × FUNDAMENTAL §1 use-case category (A-L) — what serves what
   §6.2 Part × FPF invariants (A.1-A.14) — what enforces what
   §6.3 Part × LOCKS (D1-D29) — what anchors what
   §6.4 Part × current AUDIT artefact (existing dir/skill/agent) — what reuses what
## §7 Provenance (sources cited per part)
```

Save to: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`.

### Phase A-5 — Self-verification (synthesis, ~30 min)

Per Master Plan Brief §5 quality criteria + Ruslan's 100% verification ack:

**For each main part, brigadier dispatches:**

1. **Smoke test** — `engineering-expert` (critic mode) attempts minimal implementation walkthrough: "Given current AUDIT state, what's smallest concrete artefact that would implement Wave-C bullet #1 of this part? Does the data flow work end-to-end?" Output: pass/fail per part + concrete obstacles.

2. **Cross-reference** — `philosophy-expert` (critic mode) verifies all FUNDAMENTAL/FPF/LOCKS citations resolve correctly. Output: list of broken/missing citations.

3. **Scenario walkthrough** — `mgmt-expert` (integrator mode) traces 3 representative use cases through the part-graph end-to-end:
   - **Use case 1** (Information Lifecycle): "Owner adds voice memo → triage → KB ingestion → retrieval via /ask 3 days later"
   - **Use case 2** (Strategic Management): "Owner makes decision → recorded in UC-A.4 → next month's strategic doc references it → 6 months later anti-recurrence check"
   - **Use case 3** (Agent Swarm Operations): "Brigadier dispatches 3-expert review → drafts collected → provenance gate → canonical promotion"
   Output: trace pass/fail per use case + identified gaps.

Brigadier folds findings into Master Plan §5 Open Q. Re-iterate Phases A-1..A-3 if material defects (>3 broken refs, >1 dependency cycle, any missing critical part).

---

## §5 Wave B — Library / Best Practices Research dispatch plan

### Phase B-0 — Library validation + extension (parallel with A-0, ~30 min)

- `engineering-expert` (integrator mode) — walks `raw/books-md/INDEX.md` + `ls raw/books-md/*/` + `ls raw/research/` + `ls raw/articles/` + `ls raw/external/ailev-FPF/`. Validates §3 catalog above. Lists any items in §3 not on disk + items on disk not in §3. Output: **Library Inventory** (validated, with paths, word counts, quality grades per INDEX.md).
- `mgmt-expert` (integrator mode) — checks `swarm/wiki/cycles/` for prior cycle artefacts that contain reusable methodology snapshots (cycles 6/7/8 + 11). Output: **Cycle Artefact Register**.

### Phase B-1 — Framework taxonomy (synthesis, ~30 min)

Brigadier identifies major frameworks that Foundation Architecture WILL apply. Initial list (ROY can extend):

| # | Framework | Why relevant | Library evidence |
|---|-----------|--------------|------------------|
| 1 | **Левенчук ШСМ + FPF** | Constitutional baseline (FPF §1-§14, IP-1..IP-8, 14 invariants, agency-CHR) | `design/JETIX-FPF.md`, `raw/external/ailev-FPF/FPF-Spec.md`, `raw/research/levenchuk-{deep-research,for-ai,fpf-knowledge-base}*`, `raw/books-md/systems/` (49 LJ posts) |
| 2 | **Systems thinking + cybernetics** | Decomposition discipline, leverage points, requisite variety, VSM | Meadows, Senge, Weinberg, Ackoff, Ashby, Beer, Wiener |
| 3 | **Multi-agent architecture** | Swarm coordination, brigadier role, agent communication protocols | Anthropic blogs, Cognition (Don't Build Multi-Agents), arxiv MAST/scaling-laws/multi-agent-scaling, MCP RFCs, Karpathy LLM Wiki gist |
| 4 | **Knowledge management (Karpathy LLM Wiki + Luhmann + Matuschak)** | Query-driven KB, atomicity, provenance, edge-typed graph | `raw/articles/karpathy-llm-wiki-gist-2026-04.md`, current `wiki/` substrate, INDEX.md (no direct Matuschak/Luhmann books — pull external 5 sources) |
| 5 | **Event sourcing / CQRS / append-only state** (Kleppmann, Fowler) | Git-as-audit, mailboxes, edges.jsonl, idempotent skills, recoverability | Fowler (Refactoring) tangent only; need external 5 sources |
| 6 | **Site Reliability Engineering** (Google SRE, Honeycomb) | SLI/SLO/error budgets, observability, failure injection | No direct library; external 5 sources |
| 7 | **Compounding Engineering** | Self-improving system discipline, atomic commits with provenance, methodology library | `raw/research/compounding-engineering-2026-04-22/R-1..R-11+SYNTHESIS`, Anthropic blogs |
| 8 | **Product management (Cagan/Torres/Ries) + Shape Up** | Project lifecycle, discovery, deliveries, fixed-time/flex-scope | Cagan x2, Torres, Ries, Singer (Shape Up) |
| 9 | **Stoic + epistemic discipline** (Popper, Kuhn, Naval, Holiday) | Falsifiability, paradigm awareness, agency-preservation philosophical grounding | Popper x2, Kuhn, Naval, Holiday, Greene |
| 10 | **Capital allocation + anti-fragility** (Buffett, Munger, Marks, Taleb) | Resource allocation discipline, long-term compounding, SPoF avoidance | Buffett, Graham, Marks, Munger, Taleb x2 |
| 11 | **Unix philosophy** (Raymond) | Compose-via-pipes, do-one-thing-well, plain-text formats, programmability | Raymond, Kernighan/Pike |
| 12 | **Clean code / software architecture** (Ousterhout, Fowler, Hunt/Thomas, Martin, Brooks) | Module discipline, abstraction, complexity management | All 5 in `clean-code/` |
| 13 | **Anthropic Constitutional AI / agent safety** | Constitutional limits in agent design (anti-scope hard rules implementation) | Anthropic engineering blogs in `raw/books-md/meta/`, external 5 sources |
| 14 | **Mereology + ontology** (FPF A.14) | Typed edges (ComponentOf vs PortionOf), creates relations, no flat composition | FPF + LJ Левенчук posts |

ROY may add up to 3 frameworks if domain experts surface them in pre-reads. Cap at 17 total to keep cycle bounded.

### Phase B-2 — Consultant cards (parallel batches, ~90 min)

Per framework, dispatch the closest domain expert (from the table) in **integrator mode**. Each expert writes a **Consultant Card** (~600-1000 words) with structure:

```
# Consultant Card — <framework name>

## §1 Scope
What this consultant covers + 1-line tagline

## §2 Canonical sources (library)
- 5-12 paths in `raw/books-md/`, `raw/research/`, `raw/articles/`, or `raw/external/`
- Each: 1-line "what it teaches"

## §3 External 5 sources
5 web URLs with 1-paragraph note + relevance tag.
Source format: `[Title](URL) — Author, Year. <100-word note. <Relevance: A/B/C>`
  Relevance A = directly applicable to Jetix Foundation
  Relevance B = useful background, indirectly applicable
  Relevance C = context-only, cite if challenged

## §4 Key principles (3-7)
Each principle: 1-paragraph + sourced quote/paraphrase + how-it-applies-to-Foundation

## §5 When to consult (triggers)
List 3-7 situations during Wave C/D where this consultant should be invoked
(e.g. "When designing data-flow between agents, consult Левенчук for IP-1 Role≠Executor compliance")

## §6 What this consultant does NOT cover
Anti-scope. Where to redirect (point to other consultants).

## §7 Citation discipline
Format for inline citations from this framework
(e.g. `[FPF §5.1 IP-1]`, `[Meadows ch.6 leverage-points]`, `[Anthropic-multi-agent-2025-06]`)

## §8 Failure modes (anti-patterns)
3-5 ways this framework gets misapplied + how to detect
```

**External 5-sources rule (Ruslan ack):** for each framework where library doesn't fully cover, expert MUST find exactly **5 external sources** (URLs + notes). NOT 2-3, NOT infinite. 5 = solid coverage discipline.

**Web research method:** experts use `web_search` if available; if not, expert proposes search queries + Brigadier dispatches `general-purpose` agent to fetch. Source quality bar: peer-reviewed paper / official docs / Anthropic-Cognition-Karpathy-tier blog / canonical book chapter / standards body (W3C/IETF/ISO). Reject Medium-tier rehashes, listicles, AI-generated SEO.

**Output location:** `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/<framework-slug>.md`

### Phase B-3 — Best Practices Manifest draft (synthesis, ~30 min)

Brigadier compiles **Manifest draft** (deliverable §2.5 of brief). Structure:

```
# JETIX Foundation — Best Practices Integration Manifest (Wave B draft)

## §0 Status: DRAFT — finalised в Wave D
## §1 Frameworks integrated (catalog of consultant cards)
   For each: name, primary expert, file path, status
## §2 Per-framework integration plan
   For each framework: where in Foundation it's applied (Wave C parts × framework matrix)
## §3 Provenance discipline
   Citation format conventions, how to check, how to lint
## §4 Conflict resolution rules
   When 2 frameworks suggest different patterns: how to decide (per FPF §4.5 human gate, per LOCKS hierarchy)
## §5 Anti-cargo-cult discipline
   Per Master Plan Brief §5: "NOT mention book → done. YES principles deeply applied."
   Concrete examples of cargo-cult vs deep integration.
## §6 Open Q
   Frameworks not yet covered, conflicts unresolved, consultant cards needing iteration
```

Save to: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md`.

---

## §6 Verification protocol — 100% качественно (Ruslan ack)

Per Ruslan's directive: каждая Wave-A part и каждая Wave-B consultant card verified through **all 3 methods**:

### M1 — Smoke test (where applicable)

For each main part (Wave A): `engineering-expert` (critic mode) walks through "what's the minimal artefact that demonstrates this part exists in current state?" If part is "Information Lifecycle", smoke test = `ls wiki/`, count files, verify graph/edges.jsonl exists, run `/lint` if available. **Output: pass / fail / N-A** per part + reasoning.

For each consultant card (Wave B): `engineering-expert` (critic mode) tests one principle from §4 of card by attempting to apply it to a Phase-A-1 candidate part. **Output: usable / unclear / wrong**.

### M2 — Cross-reference

For each main part: `philosophy-expert` (critic mode) verifies all citations (FUNDAMENTAL §X, FPF IP-Y, LOCKS D-Z, source paths) actually resolve. Method: open the cited file, find the cited section, verify quote/paraphrase fidelity. **Output: list of (part, citation, resolved?)**.

For each consultant card: `philosophy-expert` verifies external 5 sources are reachable + cite-able + relevance-tagged correctly.

### M3 — Scenario walkthrough

3 representative scenarios traced through proposed architecture (per §4 Phase A-5 above, plus 1 extra for Wave B):

- **Scenario W (Wave-B-specific)**: "Wave C task — design agent communication protocol. Which consultants invoked, what principles applied, where do they conflict?" — `mgmt-expert` (integrator mode) traces. **Output: clear path / ambiguous / conflicts**.

**Verification gate.** Brigadier collects all M1/M2/M3 outputs + computes coverage:
- M1 coverage = (parts smoke-tested) / (total parts) → must be ≥ 90%
- M2 coverage = (citations resolved) / (total citations) → must be 100%
- M3 coverage = (scenarios passed) / (total scenarios) = 4/4 → must be 100%

If gate fails: log defects in Open Q + iterate the affected phase. Do NOT advance to AWAITING-APPROVAL packet with broken citations или failed scenarios.

---

## §7 AWAITING-APPROVAL packet structure (cycle 12 Wave A output)

Brigadier writes packet to: `decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md`

```
---
title: AWAITING APPROVAL — Foundation Build Wave A+B (Master Plan + Library Research)
date: 2026-04-28
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
waves_covered: A, B
deliverables:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/<N>.md (× 14-17)
status: ready-for-Ruslan-review
estimated_review_time: 60-90 min Ruslan
next_action: Ruslan ack / iterate / specific-flag → Wave C launch
---

# AWAITING APPROVAL — Cycle 12 Wave A + Wave B

## §1 What was done (one paragraph executive summary)

## §2 Wave A summary
   §2.1 Main parts identified (count + list with 1-line each)
   §2.2 Interface cards (count, integrity score)
   §2.3 Dependency graph (key features: cycles? bottlenecks? mediators?)
   §2.4 Verification results (M1/M2/M3 scores per part)

## §3 Wave B summary
   §3.1 Library inventory (validated counts vs §3 catalog)
   §3.2 Frameworks taxonomy (count + list)
   §3.3 Consultant cards (count, completeness)
   §3.4 External sources (total count, distribution per framework, quality grades)

## §4 Open Q — items needing Ruslan decision
   For each: question, options (3 max with tradeoffs), recommendation + reasoning, blocking-Wave-C? (Y/N)

## §5 Defects / known limitations
   What didn't pass M1/M2/M3 gate, what's iterated, what's deferred

## §6 Strategy learnings (compound effect)
   What worked, what didn't, what ROY tooling was missing
   → Entries для `swarm/wiki/agents/<expert>/strategies.md`

## §7 ETA + cadence proposal for Wave C
   Estimated cycles needed (2-3 cycles for ~10-14 parts bundled)
   Suggested bundle composition (group related parts together)
   First Wave C cycle proposed scope

## §8 Cross-references
   Source for every claim в этом packet
```

**Brevity discipline.** Packet itself ≤ 5K words. Detail lives in deliverables. Ruslan reads packet → opens deliverables for sections he flags. Don't dump full deliverables into packet.

---

## §8 Quality discipline — 5 hard rules

### R1 — Левенчук discipline applied deeply, not formally

**NOT** "Левенчук says X, therefore we do X."
**YES** "Per FPF IP-1 §5.1, Role ≠ Executor; therefore in Foundation main-part 'Agent Swarm', we separate `role` (method signature, capability spec) from `holder` (agent-instance executing in this cycle); concrete consequence: agent prompts are tied to role-manifest not to agent-name; rebinding requires explicit `executor-binding.yaml` change per FPF §5.8.1; this prevents Role drift when we replace Sonnet with Opus or change brigadier to a different LLM."

Apply to FPF specifically:
- IP-1 (Role ≠ Executor) — separate method/role from instance/holder in any agent decomposition
- IP-2 (Context King) — every part has explicit bounded context, no global state assumptions
- IP-3 (Artifacts > conversations) — every Wave deliverable is a committed file, not a chat
- A.1 (Holonic Trinity) — parts are whole-and-part; no flat decomposition; respect U.System / U.Episteme distinction
- A.6.B (L/A/D/E lanes) — every interface card splits Laws (invariants must hold) / Admissibility (acceptance criteria) / Deontics (obligations) / Effects (measurable outcomes)
- A.14 (Typed mereology) — dependency edges are typed (ComponentOf / creates / methodologically-uses / NOT generic "depends-on")
- F-G-R discipline — every claim tagged Formality (F0-F9) / scope-G / Reliability (R-low/medium/high). No bare assertions.
- 5 ШСМ concepts (§5.10) — Роль, Альфа, Граф создания, Стратегирование, Мышление письмом — used precisely, not as metaphors

### R2 — Best practices REALLY integrated

For each consultant card §4 (key principles), the principle must be:
- **Sourced** with exact quote or paraphrase + cite
- **Applied** to specific Foundation context (which part, which decision, what changes if we apply / don't apply)
- **Tradeoff'ed** if conflicts with another framework (explicit reasoning)

Reject from Wave B: cards with vague principles like "Apply systems thinking to architecture" without concrete application example.

### R3 — No Ruslan-specific content (Foundation Layer only)

If during Wave A any expert proposes a part that:
- References Mittelstand, DACH, AI Alliance, €50K targets, Ruslan archetypes, USB-C metaphor, Smart AI label, Korp-Startup, Layer-7-Business specifics, ICP details
- Names specific stakeholders (apart from generic "founder", "owner", "stakeholder T-tier")
- Embeds specific KPIs / revenue gates / phase numbers (G1-G5)

→ Brigadier flags + reroutes. Foundation layer is generic / sector-agnostic / re-useable for hypothetical future fork users. Ruslan-specific content goes to RUSLAN-LAYER (deferred to post-Foundation work, see brief §0).

**Boundary heuristic:** would another professional knowledge worker (different domain) also need this? If yes → Foundation. If only Ruslan → RUSLAN-LAYER.

### R4 — No architectural decisions без Ruslan ack

You propose. Ruslan decides. Specifically:
- "Main parts list" = **proposal**, Ruslan accepts / modifies / adds
- "Dependency graph" = **proposal**, Ruslan validates
- "Interface cards" = **proposal**, Ruslan ack'ает structure
- "Consultant cards" = **research output**, Ruslan ack'ает relevance/completeness

Никаких `git commit` to canonical paths без Ruslan ack. Drafts under `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/` are fine. Promotion to `decisions/` или canonical wiki — only after Ruslan's signature on the AWAITING-APPROVAL packet.

### R5 — Provenance mandatory + audit-trail

Every claim → cite. No paraphrase without source path. Format:
- For library books: `[<author>-<book>-<year>:<chapter>]` e.g. `[ousterhout-philosophy-of-software-design-2ed-2021:ch5]`
- For research dumps: `[research/<file>:§<section>]` e.g. `[research/levenchuk-deep-research-2026-04-18:§3]`
- For internal docs: `[FUNDAMENTAL §6.2]`, `[FPF IP-1 §5.1]`, `[SYSTEM-OVERVIEW L1]`, `[D27]`, `[AUDIT §3]`
- For external URLs (Wave B only): `[<author>-<short-title>-<year>](URL)`

Brigadier rejects expert outputs missing inline citations. Re-dispatch with explicit "every claim must carry [src:...]".

---

## §9 Anti-patterns (what NOT to do)

| # | Anti-pattern | Detection | Resolution |
|---|--------------|-----------|------------|
| 1 | **Cargo-cult Левенчук** ("we did Левенчук" because we mentioned IP-1) | Citation present but no concrete Foundation application | Re-dispatch: explain HOW it changes Foundation design |
| 2 | **Ruslan-specific creep** (DACH / Mittelstand / specific archetypes / revenue gates leak into Foundation parts) | Phase A-1 critic check by philosophy-expert | Flag → move to RUSLAN-LAYER backlog |
| 3 | **Premature optimization** (proposing "better" architecture for things that already work in current AUDIT — like CRM cycle 10 or voice cycle 11) | Compare against AUDIT §6 working pieces | Default: re-use what works; refactor only if FUNDAMENTAL §6 anti-scope is violated |
| 4 | **Architecture drift from FUNDAMENTAL** (part exists for own sake, not serving §1 use cases) | §6.1 cross-reference matrix — any part not mapping to A-L? | Either justify cross-cutting necessity OR cut |
| 5 | **Best-practices-as-decoration** (consultant card lists 7 principles but none applied in Wave A interface cards) | M3 scenario walkthrough fails to invoke principles | Re-iterate Wave-A part design with principle in scope |
| 6 | **Loss of provenance** (claim with no citation) | M2 cross-reference fails | Re-dispatch expert with explicit citation requirement |
| 7 | **Dependency cycles silently accepted** (graph has cycles but mediator part not introduced) | A-2 scalability-architect output shows cycle | Either introduce mediator part / hoist concern OR Open Q with options |
| 8 | **Conflict resolution by silence** (2 frameworks disagree, expert picks one without surfacing) | Cross-framework principles in Manifest §4 missing reasoning | Surface to Open Q with explicit tradeoff |
| 9 | **Skipping verification** ("looks reasonable") | M1/M2/M3 coverage < threshold | Run gate — do not promote to AWAITING-APPROVAL |
| 10 | **Infinite scope** (Wave A starts producing per-part deep architecture) | Document length per part > 500 words in MASTER-PLAN-DRAFT.md | Compress to scope sentence + Wave-C bullets only; deep architecture is Wave C scope |
| 11 | **Skipping library** (relying on web research when relevant book is on disk) | External-source-count > library-source-count for a framework | Re-dispatch with explicit "use library first, web only for gaps" |
| 12 | **Web research overflow** (>5 sources per framework) | Wave B-2 source list per card | Trim to top 5 by relevance grade A |
| 13 | **Confusing Foundation with FUNDAMENTAL document** | "We're building FUNDAMENTAL" in deliverable | FUNDAMENTAL is constitutional Vision (LOCKED). Foundation is Layer 1 architecture (current work). Use precise language. |

---

## §10 Coordination + cadence

### Within cycle 12 Wave A+B:

- Phases A-0, B-0 run **parallel** (60 min wall-clock).
- Phase A-1 needs A-0 outputs; Phase B-1 needs B-0 outputs. Run parallel after pre-reads.
- Phase A-2 (interfaces) and B-2 (consultant cards) run **parallel** with each other after A-1 / B-1 complete.
- Phase A-3, A-4 sequential; A-5 + B-3 parallel.
- Then verification gate (synchronization point).
- Then AWAITING-APPROVAL packet.

**Wall-clock target:** 4-7 hours total ROY work (depending on parallelism actually achieved + expert availability).

### Sub-stage cadence (Ruslan ack between sub-stages — Ruslan directive)

After this cycle 12 Wave A+B completes + Ruslan ack:
- **Wave C** (per-part deep work) launches in **bundles** (recommend 3-5 related parts per cycle, NOT one-by-one). Bundle composition decided by brigadier in Wave A §7 ETA proposal.
- Each Wave C cycle has its OWN AWAITING-APPROVAL packet → Ruslan ack → next cycle.
- Wave D (integration pass) waits until all Wave C cycles done + acked.
- Wave E = Ruslan final review + LOCKED tag.

**Quality gates preserved.** No auto-chain. No skip-ack. Each AWAITING-APPROVAL packet is its own decision point.

### Strategy learning (compound effect — §8 of brief)

Per cycle, ROY appends to per-expert `strategies.md` in `swarm/wiki/agents/<expert>/`:
- What dispatch patterns worked
- What re-dispatches were needed (and why)
- What library lookups paid off
- What anti-pattern detections caught issues early
- Tooling gaps surfaced (e.g. "ROY needs a `/lint-citations` skill")

Brigadier compiles cross-cutting learnings into `swarm/wiki/brigadier/how-to-decompose-tasks/foundation-build-cycle-12-learnings.md` (per §8 brief). These compound into faster / better Wave C cycles.

---

## §11 Output deliverables checklist

After cycle 12 Wave A+B completion, the following must exist:

**In `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/`:**

- [ ] `wave-a/MASTER-PLAN-DRAFT.md` (per §4 structure, ~3-6K words)
- [ ] `wave-a/expert-pre-reads/` (5 files, 600-word each: systems / engineering / philosophy / mgmt / investor)
- [ ] `wave-a/interface-cards/` (one .md per main part, 200-400 words each)
- [ ] `wave-a/dependency-graph.md` (mermaid + adjacency table + cycle analysis)
- [ ] `wave-a/verification-report.md` (M1/M2/M3 results, ≥90% coverage)
- [ ] `wave-b/MANIFEST-DRAFT.md` (per §5 structure, ~3-5K words)
- [ ] `wave-b/library-inventory.md` (validated catalog with counts/paths/grades)
- [ ] `wave-b/consultants/<framework-slug>.md` × 14-17 (per §5 Phase B-2 structure, 600-1000 words each)
- [ ] `wave-b/external-sources-register.md` (all 70-85 web URLs, 5/framework × 14-17, with quality grades)
- [ ] `cycle-12-wave-a-history.md` (chronological log of all dispatches with timestamps + outputs)

**In `decisions/`:**

- [ ] `AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md` (per §7 structure, ≤ 5K words)

**In `swarm/wiki/agents/<expert>/strategies.md`:**

- [ ] Append per-expert learning entries (5 files, 1-2 entries each)

**In `swarm/wiki/brigadier/how-to-decompose-tasks/`:**

- [ ] `foundation-build-cycle-12-learnings.md` (cross-cutting brigadier learnings)

**In `swarm/wiki/log.md`:**

- [ ] Append cycle 12 Wave A+B entry (start, end, deliverable links, Ruslan-ack-pending status)

---

## §12 ETA estimate

| Phase | Wall-clock | Critical path? |
|-------|------------|---------------|
| Pre-reads (A-0 + B-0 parallel) | 30-45 min | Yes |
| A-1 candidate merge + B-1 framework taxonomy | 30-45 min | Yes |
| A-2 interfaces (3 batches × parallel 3) + B-2 consultant cards (parallel batches) | 90-120 min | Yes |
| A-3 Wave-C bullets + A-4 Master Plan compile | 45-60 min | Yes |
| A-5 verification + B-3 Manifest draft | 45-75 min | Yes |
| AWAITING-APPROVAL packet write | 30 min | Yes |
| **Total** | **4-7 hours** | |

**Iteration buffer.** If verification gate fails, add +2-3 hours. ROY may pause + send Ruslan a brief status update if iteration extends >8 hours total — Ruslan can decide to bump quality bar или ship with documented defects.

---

## §13 Open Q — questions for Ruslan clarification BEFORE launch

These are listed for human review **before** brigadier starts. If Ruslan answers any of these in pre-launch chat, brigadier folds answer into operating constraints. If left open, brigadier proceeds with default (per `[default: ...]` annotation) and surfaces in §4 of AWAITING-APPROVAL packet.

1. **Cycle directory naming convention.** Brief §3 says "cycle 12 wave A". Should cycle dir be `cyc-foundation-build-2026-04-28/` or `cycle-12-foundation-build-2026-04-28/` or follow existing pattern from `swarm/wiki/cycles/cyc-layer-7-business-trajectory-deep-dive-2026-04-25/`? **[default: `cyc-foundation-build-2026-04-28/` to match existing cyc-* pattern]**

2. **Notion sync expectations.** Should AWAITING-APPROVAL packet trigger Notion page creation (per current habit) or remain filesystem-only until Ruslan promotes? **[default: filesystem-only; Notion sync after Ruslan ack]**

3. **Daily Log integration.** Should this cycle have a Daily Log entry per existing convention? **[default: yes, brief entry pointing at AWAITING-APPROVAL]**

4. **Web research authorization.** Wave B-2 needs web fetches for ~70-85 URLs (5/framework × 14-17). Are external HTTP calls authorized in this run? **[default: yes — Ruslan's brief §6 explicitly references external web research]**

5. **Bundle size for Wave C** — recommendation in brief §9 says "bundle related parts" (3-5 per cycle). Brigadier proposes bundle composition in §7 of AWAITING-APPROVAL packet. **[default: group by cross-cutting theme — info-lifecycle parts together, agent-coordination parts together, governance parts together]**. NOT this cycle's scope; just preview.

6. **Library books deep reads in Wave A?** Master Plan Brief §3 Sub-stage 1.3.B says experts catalog the library + build consultants — but don't deep-read every book. Confirm: deep reads are Wave C scope when specific part needs them, not Wave A. **[default: yes, confirm — deep reads deferred]**

7. **Sub-agent budget per cycle.** Project-types.yaml convention is ≤7 active tasks for mini-swarms. Canonical brigadier ≤20. This is canonical brigadier (Foundation work). **[default: ≤20 cap, but parallelize in batches of 3-5 for attention manageability]**

8. **Existing cycle 12 wave A directory if exists?** ROY-AGENTS-BUILT-2026-04-23 mentions cycle 12 phase A as "ROY-built" status. Confirm there's no prior Foundation-build artefact under `swarm/wiki/cycles/` we'd overwrite. **[default: scan first, halt if conflict]**

---

## §14 Key references — quick lookup table

| Need | Path |
|------|------|
| Master Plan Brief (this work's spec) | `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` |
| Constitutional Vision | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` |
| Current state | `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` |
| FPF (Левенчук constitutional base) | `design/JETIX-FPF.md` |
| Existing 14-layer description | `decisions/JETIX-SYSTEM-OVERVIEW.md` |
| Locks D1-D29 | `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md`, `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`, `decisions/JETIX-PHILOSOPHY.md` (D2), `decisions/JETIX-VISION.md`, `decisions/JETIX-PLAN.md` |
| ROY alignment | `decisions/ROY-ALIGNMENT-2026-04-22.md` |
| ROY agents built | `decisions/ROY-AGENTS-BUILT-2026-04-23.md` |
| Brigadier README | `swarm/wiki/brigadier/README.md` |
| Library INDEX | `raw/books-md/INDEX.md` |
| Левенчук canon | `raw/external/ailev-FPF/FPF-Spec.md` |
| Левенчук LJ corpus | `raw/books-md/systems/*` (49 numbered files) |
| Research dumps | `raw/research/*` (27 files) |
| Articles | `raw/articles/*` (12 files including arxiv PDFs) |
| Prior cycle artefacts | `swarm/wiki/cycles/cyc-layer-7-business-trajectory-deep-dive-2026-04-25/`, `swarm/wiki/cycles/cyc-producer-services-strategy-options-2026-04-25/` |

---

## §15 Final operating instructions

1. **Read all 6 mandatory pre-reads (§2) IN FULL before any dispatch.** This is non-negotiable.
2. **Validate library catalog (§3) before Wave B-1.** Don't assume the preview is exhaustive.
3. **Run Phases A-0 + B-0 first (parallel), in 60-min wall-clock.** Synchronize on completion before A-1 / B-1.
4. **Apply §8 hard rules R1-R5 to every dispatched output.** Reject + re-dispatch on violation.
5. **100% verification per §6 M1/M2/M3.** No advancing to AWAITING-APPROVAL with broken citations or failed scenarios.
6. **Cap document length per §9 anti-pattern 10.** Wave A document ≤ 6K words. Wave B Manifest ≤ 5K. Consultant cards 600-1000 each. AWAITING-APPROVAL ≤ 5K.
7. **Surface to Open Q anything you can't internally resolve.** Don't compromise silently.
8. **Compound learning per §10.** Append per-expert strategies + brigadier learnings.
9. **AWAITING-APPROVAL packet is the deliverable handle for Ruslan.** Make it readable in 60-90 min.
10. **STOP after AWAITING-APPROVAL packet writte. Do NOT auto-chain Wave C.** Wait for Ruslan ack.

---

**End of deep prompt.** Brigadier: confirm receipt by writing first entry to `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/cycle-12-wave-a-history.md` ("Cycle launched <UTC timestamp> per `prompts/foundation-build-cycle-12-wave-a-deep-prompt-2026-04-27.md`"). Then begin §2 mandatory pre-reads. Quality > speed. Provenance > volume. Ruslan-ack > brigadier-confidence.

Поехали.
