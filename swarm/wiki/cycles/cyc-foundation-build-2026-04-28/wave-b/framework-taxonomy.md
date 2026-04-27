---
title: Framework Taxonomy — Wave B-1 (brigadier confirmed initial list)
date: 2026-04-27
phase: B-1
expert: brigadier
mode: routing
cycle: cyc-foundation-build-2026-04-28
status: initial-confirmed (extensible by ROY up to 17 total per §5 Phase B-1 cap)
---

# Framework Taxonomy — Wave B-1

> Brigadier confirms initial 14-framework list per deep-prompt §5 Phase B-1. ROY may add up to 3 more (cap 17 total) if Phase A-0 expert pre-reads surface gaps. Each framework gets a consultant card in Phase B-2 with §1 Scope declaring foundation-studied coverage as `[X]/[Y]` per Ruslan emphasis 27.04 evening.

---

## §1 Confirmed 14 frameworks (initial)

| # | Framework | Why relevant to Foundation | Primary expert | Library evidence | External 5-sources needed? |
|---|-----------|----------------------------|----------------|------------------|----------------------------|
| 1 | **Левенчук ШСМ + FPF** | Constitutional baseline (FPF §1-§14, IP-1..IP-8, 14 invariants, agency-CHR, F-G-R, A.14 typed mereology, A.6.B L/A/D/E lanes, F.6 6-step cycle). 100% MUST be FULL CORPUS — 49 LJ posts not sampled (per Ruslan emphasis 27.04). | systems-expert + philosophy-expert (joint) | `design/JETIX-FPF.md` (3758 lines), `raw/external/ailev-FPF/FPF-Spec.md` (62K lines), `raw/research/levenchuk-{deep-research,for-ai,fpf-knowledge-base}*` (~286K words combined), `raw/books-md/systems/` (49 numbered LJ posts, P0 priority) | Yes — 5 sources for `levenchuk-public-materials` (recent posts not in disk corpus, FPF upstream changelog) |
| 2 | **Systems thinking + cybernetics** | Decomposition discipline (Meadows leverage points), requisite variety (Ashby), VSM viability (Beer System 1-5), evolutionary purpose (Senge + Kelly). Foundation parts must respect feedback-loop mapping. | systems-expert | `raw/books-md/systems/` (Meadows, Senge, Weinberg, Ackoff), `raw/books-md/cybernetics/` (Ashby, Beer, Wiener, Kelly), `raw/books-md/complexity/` (Mitchell, Beinhocker), `raw/books-md/biology/` (Dawkins, Dennett, Kauffman) | Yes — 5 sources (Donella Meadows Institute, Beer's archive, contemporary VSM applications) |
| 3 | **Multi-agent architecture** | Swarm coordination (brigadier role), agent communication protocols, MCP, context management. Foundation Cat E (Agent Swarm Operations) MUST integrate state-of-art patterns. | engineering-expert | `raw/books-md/meta/` (Anthropic blogs: building-effective-agents, multi-agent-research-system, code-execution-with-MCP), Cognition Don't-Build-Multi-Agents, MCP RFCs, `raw/articles/karpathy-llm-wiki-gist-2026-04.md`, `raw/articles/arxiv-2406.07155-qian-scaling-laws.pdf`, `raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.pdf`, `raw/articles/arxiv-2512.08296-kim-multi-agent-scaling.pdf` | Yes — 5 sources (recent MAST literature, LangGraph/CrewAI architecture papers, agent-skill papers) |
| 4 | **Knowledge management — Karpathy LLM Wiki + Luhmann Zettelkasten + Matuschak evergreens + Forte PARA** | Foundation Cat B (Information Lifecycle) substrate. Query-driven KB per D28; provenance per FPF. | engineering-expert + systems-expert (joint) | `raw/articles/karpathy-llm-wiki-gist-2026-04.md`, current `wiki/` substrate v3 (552 entities + 9 types + 8 edge types). NO direct Luhmann or Matuschak books on disk → external 5-sources mandatory | Yes — 5 sources (Andy Matuschak working notes, Luhmann/Schmidt history, Forte BASB framework) |
| 5 | **Event sourcing + CQRS + append-only state** | Git-as-audit-log per D25; mailboxes; edges.jsonl; idempotent skills; recoverability. Foundation Cat H reliability. | engineering-expert | `raw/books-md/clean-code/` (Fowler tangentially via Refactoring) — NO Kleppmann directly on disk → external 5-sources mandatory | Yes — 5 sources (Kleppmann DDIA chapter excerpts, Greg Young CQRS, Fowler Event Sourcing, Vaughn Vernon DDD) |
| 6 | **Site Reliability Engineering — Google SRE + Honeycomb observability** | Foundation Cat H §5 reliability + Cat I health checkups. SLI/SLO/error budgets, observability, failure injection. | engineering-expert + systems-expert (joint) | NO direct SRE Book on disk → external 5-sources mandatory | Yes — 5 sources (Google SRE Book chapters, Honeycomb engineering blog, Charity Majors observability writings) |
| 7 | **Compounding Engineering** | Self-improving system discipline (D2 architect-orbit + ROY strategies.md compound effect). Foundation Cat C (Self-Improvement & Learning) substrate. | engineering-expert | `raw/research/compounding-engineering-2026-04-22/` (R-1..R-11 + SYNTHESIS), `raw/articles/2026-04-22-every-compound-engineering-guide.md`, Anthropic engineering blogs in `raw/books-md/meta/` | Optional — solid library coverage; 0-2 sources max if gap |
| 8 | **Product management — Cagan + Torres + Ries + Shape Up** | Foundation Cat D (Project & Resource Mgmt) + Cat J (Daily Operations). Discovery / delivery / fixed-time variable-scope. | mgmt-expert | `raw/books-md/pdm/` (Cagan x2, Torres CDH, Doerr OKRs, Ries Lean Startup), `raw/books-md/pm/` (PMBOK, Scrum, Singer Shape Up), `raw/research/phase-2-deep-research-2026-04-22/RESULT-05/06/07` | Optional — strong library; 0-2 sources |
| 9 | **Stoic + epistemic discipline — Popper + Kuhn + Naval + Holiday + Munger latticework** | Falsifiability, paradigm awareness, agency-preservation philosophical grounding. Foundation §5 reliability + §6 anti-scope philosophical anchors. | philosophy-expert | `raw/books-md/philosophy-science/` (Kuhn, Popper x2), `raw/books-md/philosophy/` (Naval, Holiday, Greene, Deutsch), `raw/books-md/investing/` (Munger Poor Charlie's), `raw/books-md/engineering-foundations/` (Descartes, Koen, Vincenti) | Optional — strong library; 0-2 sources |
| 10 | **Capital allocation + anti-fragility — Buffett + Munger + Marks + Taleb** | Foundation §5 reliability anti-fragility + Cat H provenance/audit + long-term compounding investment in KB / methodology / network. | investor-expert | `raw/books-md/investing/` (Buffett Letters ~5MB, Graham, Marks, Munger RU, Taleb Antifragile + Skin in the Game) | Optional — strong library; 0-2 sources |
| 11 | **Unix philosophy** | Compose-via-pipes, do-one-thing-well, plain-text formats, programmability, KISS. Foundation §4 automation discipline + every part interface clean contract. | engineering-expert | `raw/books-md/unix/` (Raymond Art of Unix Programming, Kernighan/Pike Unix Programming Environment) | Optional — solid library; 0-2 sources |
| 12 | **Clean code / software architecture — Ousterhout + Fowler + Hunt-Thomas + Martin + Brooks** | Foundation L0 Company-as-Code skills + agent-prompts module discipline + abstraction layers. | engineering-expert | `raw/books-md/clean-code/` (Ousterhout, Fowler Refactoring, Hunt/Thomas Pragmatic, Martin Clean Code, Brooks MMM) | Optional — solid library; 0-2 sources |
| 13 | **Anthropic Constitutional AI / agent safety** | Constitutional limits in agent design (anti-scope §6.1 hard rules implementation pattern). | philosophy-expert | Anthropic engineering blogs in `raw/books-md/meta/` (Constitutional AI methodology references) | Yes — 5 sources mandatory (Anthropic Constitutional AI paper, Helpful-Harmless-Honest framework, RLHF & RLAIF refinements) |
| 14 | **Mereology + ontology — FPF A.14 typed edges** | Typed dependency edges (ComponentOf vs PortionOf vs creates vs methodologically-uses) — NOT generic "depends-on". Foundation interface cards § Dependencies must be typed. | philosophy-expert + systems-expert (joint) | FPF + LJ Левенчук posts (covered in #1); academic mereology (Leśniewski → Lewis → Fine) NOT on disk | Yes — 5 sources (Leśniewski mereology primer, David Lewis Parts of Classes, Kit Fine variable-embodiments, contemporary applied mereology) |

---

## §2 Frameworks ROY may add (cap +3, total ≤17)

If Phase A-0 expert pre-reads surface gaps, ROY may add UP TO 3 frameworks. Candidate watch-list:

- **Domain-Driven Design (Eric Evans + Vaughn Vernon)** — bounded contexts overlap with FPF IP-2; could be standalone framework if engineering-expert pre-read shows distinct value beyond Левенчук
- **Conway's Law / Software architecture as social structure** — relevant for D26 Team 50-100 + agent-org alignment
- **Toyota Production System / Lean** — flow / waste / continuous improvement; potentially overlaps with Compounding Engineering #7
- **Cynefin (Snowden) — complex/complicated/clear/chaotic** — decision-making under different complexity regimes; overlaps with Systems thinking #2 + Stoic #9

Default: **add only if expert pre-read explicitly justifies why none of the 14 confirmed frameworks cover the gap**.

---

## §3 100% framework foundation studied — coverage method per consultant card

Per Ruslan emphasis 27.04 evening: every consultant card §1 Scope MUST declare:
- `Foundation studied: [X]/[Y] canonical sources (Z%)`
- Where coverage <100% — explicit reason (e.g., "Levenchuk: studied 49/49 LJ posts + FPF 14 sections = 100% / D28 reflection deferred to Wave C per scope")

**Левенчук framework (#1) is the priority canon — FULL 49 LJ posts must be consulted, not sampled.** This is Ruslan's explicit emphasis 27.04: "Левенчук 49 posts (P0 priority) — FULL corpus consulted для Levenchuk consultant card, не sampled."

For frameworks with NO library coverage (#4 KM-Luhmann/Matuschak, #5 Event-sourcing-Kleppmann, #6 SRE, #13 Anthropic Constitutional AI, #14 Mereology) — explicit "100% web-based foundation, 5 sources" with quality grade A relevance per source.

---

## §4 Cargo-cult sharper detection (Ruslan emphasis #3)

Each consultant card §4 Key Principles MUST contain — per principle:
- **Sourced** — exact quote or paraphrase + citation
- **Applied** — specific Foundation context (which Wave A main part / which decision / what changes if applied vs not)
- **Tradeoff'ed** — explicit reasoning if conflicts with another framework's principle

Reject from Wave B-2 batch: cards with vague principles like "Apply systems thinking to architecture" — re-dispatch with explicit "give me the 1-paragraph application example linking to a Wave A main-part candidate".

---

## §5 Conflicts surface proactively (Ruslan emphasis #4)

Where 2 frameworks suggest different patterns, log to Open Q with TRADEOFF analysis. Examples:
- **Левенчук Role≠Executor (IP-1)** vs **CrewAI agent personification** — IP-1 wins per FPF constitutional, but tradeoff is documented
- **Anthropic "Don't Build Multi-Agents" (Cognition)** vs **Anthropic "Multi-agent research system" effective patterns** — these are nuanced; brigadier surfaces both with context-dependence
- **Karpathy LLM Wiki "answer questions with citations"** vs **Anthropic Constitutional AI hard refusals** — both apply different layers (KB vs guardrail); not direct conflict but worth documenting
- **Buffett circle-of-competence** vs **Taleb antifragile via-negativa** — both endorse "less is more" but for different reasons (epistemic humility vs error-resilience); cards must document
- **D28 Query-driven KB filtering (selective)** vs **Karpathy "ingest qualitative KB"** — conflict resolved by D28 (Jetix-specific anchor mandate)

NO silent compromise. Surface to Manifest §4 Conflict Resolution Rules.

---

## §6 Output paths

- 14 consultant cards → `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/<framework-slug>.md`
- External sources register → `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/external-sources-register.md`
- Manifest draft → `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md`

Slug convention: `<framework-slug>` ∈ {levenchuk-shsm-fpf, systems-thinking-cybernetics, multi-agent-architecture, knowledge-management-karpathy-luhmann-matuschak, event-sourcing-cqrs, sre-observability, compounding-engineering, product-management-cagan-shape-up, stoic-epistemic, capital-allocation-antifragility, unix-philosophy, clean-code, anthropic-constitutional-ai, mereology-typed-edges}.

---

*Brigadier confirmation. Awaiting Phase A-0 pre-reads to validate framework gaps before Wave B-2 dispatch.*
