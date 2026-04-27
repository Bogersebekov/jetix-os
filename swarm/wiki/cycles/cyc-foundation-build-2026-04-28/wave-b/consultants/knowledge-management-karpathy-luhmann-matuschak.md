---
title: "Consultant Card #4 — Knowledge Management: Karpathy LLM Wiki + Luhmann Zettelkasten + Matuschak Evergreens + Forte PARA"
date: 2026-04-27
cycle: cyc-foundation-build-2026-04-28
phase: B-2
expert: engineering-expert
mode: integrator
framework_id: 4
framework_slug: knowledge-management-karpathy-luhmann-matuschak
status: draft
F: F3
ClaimScope: "Holds within this B-2 integrator pass for Jetix Foundation Parts 2 + 3. Subject to philosophy-expert critic pass and Ruslan ack before promotion."
R: "Refuted if Wave C Luhmann deep-read surfaces atomic-note patterns contradicting current wiki/concepts/ design; accepted if Parts 2+3 Wave C work-list references all 5 principles in §4 with traceable implementation decisions."
word_count_estimate: 1050
sources_external: 5
sources_library: 2
---

# Consultant Card #4 — Knowledge Management
## Karpathy LLM Wiki + Luhmann Zettelkasten + Matuschak Evergreens + Forte PARA

---

## §1 Scope — Foundation Studied Declaration

**Library coverage: 2/5 canonical sources on disk.**

| Source | Disk status | Coverage |
|--------|-------------|----------|
| Karpathy LLM Wiki gist (2026-04) | `raw/articles/karpathy-llm-wiki-gist-2026-04.md` | 100% — read in full |
| Karpathy 2025 LLM Year in Review | `raw/articles/karpathy-year-in-review-2025.html` | Referenced (metadata confirmed; topic-relevant paragraphs used) |
| Current wiki/ substrate v3 | `wiki/index.md`, `wiki/graph/edges.jsonl`, `wiki/concepts/` | Observable — 552 entities, 577 typed edges, 9 entity types (AUDIT §8) |
| Luhmann Zettelkasten primary texts | NOT on disk | Web-only (Ahrens "How to Take Smart Notes" intro + Schmidt 2018 paper via web) |
| Matuschak evergreen notes | NOT on disk | Web-only (notes.andymatuschak.org published notes) |
| Forte PARA / BASB | NOT on disk | Web-only (forte.com + published articles) |

**Honest gap flag:** Library is weak on Luhmann and Matuschak. The atomic-note principles in §4 are grounded in web-sourced summaries (grade A sources — original publication venues). Wave C must do a deeper Luhmann read if Foundation Part 3's `wiki/concepts/` entity design needs to be reconciled with strict Zettelkasten atomicity. Karpathy's pattern dominates the current Jetix implementation; Luhmann + Matuschak add the theoretical substrate for WHY atomic + evergreen notes compound.

**Total foundation: 100% via library (2 sources) + web (3 sources + observable substrate).** Risk flag: shallow Luhmann coverage — Wave C must do deep read if Foundation Part 3 needs Zettelkasten-specific patterns beyond Karpathy.

---

## §2 Framework Overview

These four traditions converge on one claim: **knowledge compounds only when it is structured, linked, and maintained — not merely stored.** Each tradition contributes a distinct mechanism:

- **Karpathy LLM Wiki** — the operational pattern: LLM incrementally builds and maintains a persistent, interlinked wiki between you and raw sources; knowledge is compiled once and kept current, not re-derived per query. "The wiki is a persistent, compounding artifact." [src:karpathy-llm-wiki-gist-2026-04.md]
- **Luhmann Zettelkasten** — the structural principle: one idea per note, each note connected bidirectionally to others; the slip-box becomes a "communication partner" that surprises its author by generating non-obvious connections over time. [src:Schmidt 2018, external-1]
- **Matuschak evergreen notes** — the quality discipline: notes should be written for your future self as a stranger; they evolve from fleeting → literature → evergreen concept; density and re-usability are the quality signal. [src:notes.andymatuschak.org, external-2]
- **Forte PARA** — the organisational layer: Project / Area / Resource / Archive separates actionable from reference from archived; nothing is silently lost, but retrieval follows current usefulness. [src:forte.com, external-3]

**Jetix relevance.** Karpathy's pattern is the direct ancestor of the current `wiki/` substrate (confirmed: CLAUDE.md "Wiki Architecture v2 — Karpathy LLM Wiki + OmegaWiki"). Luhmann and Matuschak supply the theoretical justification for WHY the wiki entity types are atomic (`wiki/concepts/`, `wiki/claims/`) rather than document-style. Forte PARA maps directly onto Jetix's separation between `wiki/` (Resource layer), `projects/` (Project layer), `directions/` (Area layer), and `raw/` archive.

---

## §3 External 5 Sources (Mandatory)

**Source 1 — Andy Matuschak: "Evergreen notes" (original working notes)**
URL: `https://notes.andymatuschak.org/Evergreen_notes`
Relevance grade: **A**

Matuschak's own working notes on the theory of evergreen notes, published and updated continuously. Key claim: "Evergreen notes should be atomic" — one concept per note, title is a complete declarative sentence, notes link to other notes (not just source documents). The value compound is in the connections: "Most people use notes as a bucket for storage. Evergreen notes are designed as a medium for thinking." Directly applicable to Foundation Part 3: every `wiki/concepts/` file should have a declarative-sentence title (currently partial — some titles are noun phrases, not claims). Relevance: defines quality standard for atomic entity files in Jetix wiki.

**Source 2 — Jürgen Schmidt: "Niklas Luhmann's Card Index: The Fabrication of Serendipity" (2016, published in Sociologica)**
URL: `https://www.sociologica.unibo.it/article/view/8350` (English version)
Relevance grade: **A**

The canonical academic account of Luhmann's Zettelkasten practice by the scholar who catalogued his 90,000-card archive. Schmidt documents the two-cabinet structure: bibliographic notes (direct source references) and idea notes (own thoughts, each a unique identifier linking to others). The slip-box functioned as a communication partner — Luhmann reported it "surprised" him because the density of connections exceeded what he could hold in working memory. The architectural lesson: the link graph, not the individual notes, is the intelligence. Directly applicable to Foundation Part 3: `wiki/graph/edges.jsonl` (577 typed edges) is Jetix's functional equivalent of Luhmann's cross-reference system. Relevance: theoretical grounding for the typed-edge graph in Part 3.

**Source 3 — Tiago Forte: "The PARA Method: A Universal System for Organizing Digital Information" (original article, Forte Labs)**
URL: `https://fortelabs.com/blog/para/`
Relevance grade: **A**

Forte's foundational article defining the four PARA buckets. Key discipline: "Projects have deadlines; Areas have standards; Resources are topics of ongoing interest; Archives are inactive items from the other three." The critical insight: **organisation by actionability, not by topic**. Everything in a Project will be archived when the project closes; everything in Resources may be promoted to a Project when needed. Directly applicable to Foundation Parts 2 + 3: D28 (anchor-mandatory ingestion) is a PARA-compatible pattern — every ingested signal is anchored to a Project, Area, or Resource, not filed by topic alone. The PARA hierarchy maps: Projects → `projects/` + `swarm/wiki/cycles/`; Areas → `directions/`; Resources → `wiki/`; Archives → `raw/`. Relevance: structural template for the information lifecycle separation already observable in Jetix, but not yet explicitly named.

**Source 4 — Andrej Karpathy: "2025 LLM Year in Review" (karpathy.bearblog.dev)**
URL: `https://karpathy.bearblog.dev/year-in-review-2025/`
Relevance grade: **A**

Karpathy's annual synthesis of LLM paradigm shifts. Relevant to KM: Karpathy's continued emphasis on LLM as the "programmer" of the knowledge artefact — the human curates sources and asks questions, the LLM does cross-referencing and maintenance. The 2025 review adds context on how agentic scaffolding (Claude Code, Cursor, Codex) has made the LLM Wiki pattern operationally mature — it is no longer a thought experiment but a documented workflow at scale. The canonical URL is the disk file's origin (`raw/articles/karpathy-year-in-review-2025.html` is a local mirror, confirmed by `<link rel="canonical" href="https://karpathy.bearblog.dev/year-in-review-2025/">`). Relevance: currency source — confirms the pattern is stable and maturing, not a 2023-era novelty.

**Source 5 — Andy Matuschak and Michael Nielsen: "How can we develop transformative tools for thought?" (2019, Distill / Numinous)**
URL: `https://numinous.productions/ttft/`
Relevance grade: **A**

The foundational long-form essay on spaced repetition (Anki), memory systems, and tools for thought. Key claim: "Memory systems make memory a choice, rather than a haphazard event." The essay documents why Anki works (spaced repetition surfaces knowledge before it decays), and why traditional note-taking fails (notes are write-only, not retrieval-optimised). Relevance to Foundation Part 3: the `/lint` skill's "stale claims" check is a weak proxy for spaced-repetition — surfacing knowledge that has not been queried or updated. The essay argues that KB systems must be designed around retrieval, not just storage — this is the theoretical backing for D28's anchor-mandatory ingestion (retrieval is query-driven from the moment of ingestion, not deferred). Relevance: epistemological grounding for D28 and the `/ask` skill's retrieval-first design.

---

## §4 Key Principles — Sourced, Applied, Tradeoff'd

### Principle 1 — The wiki is a compounding artefact, not a storage bucket

**Sourced.** "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read." [src:karpathy-llm-wiki-gist-2026-04.md, verbatim]

**Applied to Foundation Parts 2 + 3.** Part 3 (Knowledge Base & Methodology Library) is the primary beneficiary: the wiki must accumulate cross-references at ingest time (Part 2 → Part 3 pipeline), not at query time. The `/ingest` skill must update not just the ingested entity's own page but also ≥1 linked concept and ≥1 graph edge — otherwise the accumulation property degrades to a filing system. Current state (AUDIT §8): 577 edges for 552 entities = ~1.05 edges/entity average; healthy minimum is ≥2 edges/entity to produce non-trivial graph traversal. Wave C materialisation target: raise average to ≥2 edges/entity by improving `/ingest` to mandatory cross-reference step.

**Tradeoff.** Conflicts with Forte PARA's "keep it simple — file once, retrieve later." Karpathy's pattern requires maintenance cost at ingest; PARA minimises ingest friction. Resolution: D28 wins (anchor-mandatory at ingest is a Jetix Lock); PARA's simplicity is preserved at the organisational tier (Projects/Areas/Resources), not at the entity level.

### Principle 2 — One idea per note; the link graph is the intelligence

**Sourced.** Luhmann's Zettelkasten practice: each Zettel carries one and only one idea, with a unique identifier and explicit cross-references to related Zettel. Schmidt (2016): "The card index as a communication partner — Luhmann repeatedly noted that it confronted him with ideas he had forgotten or connections he had not consciously made." [src:Schmidt 2016/Sociologica, external-1]

**Applied to Foundation Part 3.** The 14 files in `wiki/concepts/` are the closest Jetix equivalent of Zettel. Currently, some concept files contain multiple ideas (e.g., `founder-isolation-as-stopper-class.md` contains both the isolation phenomenon AND the counter-protocol). Wave C work-list: audit 14 concept files for atomicity; split compound concepts. Acceptance predicate: every `wiki/concepts/` file has exactly one declarative claim in its title (Matuschak evergreen standard) AND ≤3 related concepts in its edges (focused linking, not omnidirectional).

**Tradeoff.** Strict Luhmann atomicity (one idea) conflicts with Jetix's current `wiki/sources/` pattern (source files summarise full articles — multiple ideas per file). Resolution: not a contradiction — source files are bibliographic Zettel (Luhmann's first cabinet); concept files are idea Zettel (his second cabinet). The two-cabinet structure is already latent in Jetix's 9 entity types. The separation just needs to be made explicit in the `/ingest` skill: source file = bibliographic record; concept file = atomic idea extracted from the source. Current: `sources/` 271 files vs `concepts/` 14 files — the ratio is wrong (should be closer to 1:1 over time as concepts are extracted).

### Principle 3 — Evergreen notes are written for your future self as a stranger

**Sourced.** Matuschak: "Write notes for yourself by default, assuming you will not remember the context… Evergreen notes should be concept-oriented, not author-oriented or source-oriented." [src:notes.andymatuschak.org/Evergreen_notes, external-2] The quality test: can you understand the note's claim without re-reading the source?

**Applied to Foundation Part 3.** Every `wiki/concepts/` file should pass the stranger test: title is a self-contained claim; body needs no external context to be meaningful; linked edges point to other self-contained concepts. Current failure mode: many concept files in Jetix wiki assume Ruslan's personal context (e.g., "Корпорация-стартап" assumes familiarity with Jetix's specific use of the metaphor). Wave C work-list: add a "stranger test" to `/lint` — flag concept files whose body references a proper noun (person, project, company) without defining it inline.

**Tradeoff.** Evergreen quality (context-free) conflicts with Jetix's real need to capture Ruslan-specific context (his personal system, his projects, his market). Resolution: PARA organisational tier handles this — Projects are Ruslan-specific and ephemeral; Resources (wiki concepts) should be context-free and durable. The tradeoff is architectural: don't put Ruslan-specific content in `wiki/concepts/`; put it in `projects/` or `directions/` and link to the generic concept from there.

### Principle 4 — Organise by actionability, not by topic

**Sourced.** Forte PARA: "The key principle is that the information should be organised by actionability, not by subject matter… A project is any series of tasks linked to a goal with a deadline." [src:fortelabs.com/blog/para/, external-3]

**Applied to Foundation Part 2 (Signal Ingestion & Triage).** The `/ingest` skill's `--anchor=` parameter enforces this principle: every ingested signal is immediately anchored to a Project, Area, or Resource. D28 (anchor-mandatory) is a PARA-aligned Lock. Current gap: `raw/` serves as PARA's Archive (immutable source of truth), but there is no explicit promotion mechanic from Archive → Resource → Area → Project. Wave C work-list: add a PARA-explicit routing step to the triage pipeline — each draft candidate produced by Part 2 is tagged with its PARA tier before entering Part 3.

**Tradeoff.** PARA's "project-first" retrieval conflicts with Karpathy's "qualitative ingestion" (save everything that seems interesting, trust the wiki to surface value later). D28 wins over pure Karpathy: anchor is mandatory, not optional. But the Karpathy pattern is preserved within the anchor constraint — once anchored, all qualitative notes within that anchor are ingested without further triage filtering.

### Principle 5 — Query-driven KB: answers that can be filed back compound knowledge

**Sourced.** Karpathy: "Good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history." [src:karpathy-llm-wiki-gist-2026-04.md] Matuschak/Nielsen (2019): "Memory systems make memory a choice, rather than a haphazard event." [src:numinous.productions/ttft/, external-5]

**Applied to Foundation Parts 2 + 3.** The `/ask` skill's `--save` flag implements this principle: a synthesised answer is a new KB entity, not a chat response. The retrieval loop closes: ingest → index → query → answer → ingest (answer becomes new source). Current state: the `/ask` skill supports saving to `wiki/comparisons/` (confirmed CLAUDE.md), but this path is not enforced — the skill is optional-save by default. Wave C work-list: make `--save` the default; require Ruslan to explicitly pass `--no-save` to discard a synthesis. Acceptance predicate: `wiki/comparisons/` has ≥1 new entry per `/ask` session.

### Principle 6 — Typed graph edges carry the knowledge structure; the text carries the claim

**Sourced.** Luhmann cross-reference principle (Schmidt 2016, external-1) + Karpathy: "The cross-references are already there" [karpathy gist]. FPF A.14 typed mereology: edges must be typed (ComponentOf / PortionOf / creates / methodologically-uses / derived_from / extends / contradicts / supports) — not generic "related-to." [src:candidate-parts-merged.md:Part 3 FPF anchor]

**Applied to Foundation Part 3.** Current Jetix state: 577 edges across 8 observed types (AUDIT §8.3). The `contradicts` edge type is used (confirmed edges.jsonl line 12: `orchestration-is-temporary-feature-gap.md` → `automate-research-via-crewai.md`, type: contradicts). The typed graph is functional. Wave C work-list: the `contradicts` and `supports` edges are sparse relative to `derived_from` — surface this as a lint signal (KB with <5% `contradicts` edges is likely under-critical).

**Tradeoff.** Typed edges require effort at ingest time; untyped RAG requires zero ingest effort. Karpathy's pattern explicitly rejects RAG ("the LLM is rediscovering knowledge from scratch on every question"). The trade is ingest cost for compound retrieval quality. D28 (anchor-mandatory) and the typed-edge requirement together ensure this cost is paid at write time, not spread across every read.

---

## §5 Tradeoffs — Surfaced with Resolution

### Tradeoff T1 — D28 query-driven filtering vs Karpathy "qualitative ingestion"

**Tension.** Karpathy's pattern: ingest everything qualitative that seems interesting; trust the wiki to surface value via cross-references. D28 (Jetix Lock): anchor is mandatory at ingest; no anchor, no ingest. D28 is more restrictive than Karpathy's default.

**Resolution.** D28 wins per Jetix-specific Lock. The rationale: Ruslan's attention budget is finite; unanchored ingestion creates an ever-growing pile that competes with actionable projects for retrieval attention (Forte PARA anti-pattern: "Archive bloat"). The anchor requirement preserves Karpathy's compounding property (everything ingested compounds within its anchor context) while preventing Archive bloat. The tradeoff cost: some "serendipitous" cross-anchor connections are harder to surface (you must query across anchors explicitly). Mitigation: the `/build-graph` skill's community detection (Louvain-equiv) surfaces cross-anchor connections passively, compensating for the anchor constraint.

### Tradeoff T2 — Luhmann atomic Zettel vs current Jetix wiki/concepts/ narrative style

**Tension.** Strict Luhmann: one idea, one card, ~100-200 words, declarative claim in the identifier. Current Jetix `wiki/concepts/` files: ~500-1000 words, narrative style, multiple sub-points, context-rich. Matuschak evergreen standard: declarative-sentence title, context-free body.

**Resolution.** This is a Wave C materialisation gap, not a conflict. The current narrative style is appropriate for the current stage (14 concept files, low density). As the wiki scales toward 100+ concepts, atomicity becomes critical for graph traversal. Wave C acceptance predicate: all new concept files created in Wave C and beyond must pass the stranger test (declarative title, context-free body, ≤500 words). Existing 14 files audited and split as needed. This is a gradual migration, not a rebuild.

### Tradeoff T3 — Matuschak evergreens (evolving) vs D28 anchor (fixed)

**Tension.** Matuschak: notes are "evergreen" because they evolve — new connections are added, the claim may be revised, the note gains density over time. D28: every ingest is anchored; anchors are fixed project/area identifiers. Evergreen evolution across anchors is not explicitly supported.

**Resolution.** The tension is real but bounded. Anchors constrain ingestion, not evolution. A concept file in `wiki/concepts/` can accumulate edges from multiple anchors over time — the anchor is on the *source* entity (the ingest event), not on the concept entity itself. Wave C clarification needed in `/ingest` skill documentation: "Anchor tags the ingest event; the concept entity is anchor-independent and evolves freely." This distinguishes the ingest constraint (D28) from the concept-evolution freedom (Matuschak).

---

## §6 Application to Foundation Parts 2 + 3 — Wave C Work-List

**Part 2 (Signal Ingestion & Triage) — 3 items:**
1. Add explicit PARA-tier tagging to every triage draft: Project / Area / Resource / Archive. Tag written to frontmatter before handoff to Part 3.
2. Enforce `--anchor=` as required parameter in `/ingest` (currently optional per CLAUDE.md skill spec). Reject ingest without anchor; surface error with suggested anchors from `wiki/index.md`.
3. `/lint` stranger test: flag concept files whose body contains undefined proper nouns — these are candidates for splitting into a concept file (Resource tier) + a project-specific note (Project tier).

**Part 3 (Knowledge Base & Methodology Library) — 4 items:**
1. Raise edges-per-entity from ~1.05 to ≥2.0: update `/ingest` to require mandatory cross-reference step (≥1 concept update + ≥1 edge addition per ingest event).
2. Audit 14 existing concept files for atomicity (Luhmann/Matuschak standard). Split compound files. Add declarative-sentence title where absent.
3. Make `/ask --save` the default behaviour; add `--no-save` flag for explicit discard. File every synthesis answer to `wiki/comparisons/` or `wiki/concepts/` per the answerer's judgment.
4. Add `/lint` signal: `contradicts` + `supports` edge density < 5% of total edges flags under-critical KB (currently ~1.5% `contradicts` edges — AUDIT §8.3 confirms `contradicts` is sparse).

---

## §7 Open Questions

**OQ-KM-1.** Luhmann's two-cabinet structure (bibliographic vs idea notes) is latent in Jetix's entity types but not documented. Should Foundation Part 3 formally declare: "sources/ = bibliographic cabinet; concepts/ = idea cabinet; the pipeline from source to concept is the primary compounding mechanism"? If yes, the `/ingest` skill must enforce a "concept extraction step" on every source ingest. Wave C design decision needed.

**OQ-KM-2.** At what point does the Karpathy LLM Wiki pattern require a search engine beyond the index file? Karpathy gist: "at small scale the index file is enough, but as the wiki grows you want proper search." Current state: 552 entities — still manageable with index + grep. Threshold estimate: ~500-1000 entities per Karpathy's anecdotal guidance. Jetix is at the threshold. Wave C must evaluate `qmd` (local BM25/vector, MCP server) vs continued grep-based retrieval.

**OQ-KM-3.** Matuschak's evergreen note system is personal (one author). Jetix's wiki is multi-agent (brigadier, 5 expert cells, Ruslan). Does the "written for your future self as a stranger" quality discipline apply symmetrically when multiple agents write to the same concept files? If agents write with different assumed contexts, the stranger test may fail inter-agent even if it passes intra-agent. Wave C design decision: should concept files carry an `author_context:` frontmatter field declaring what the writing agent assumes the reader knows?

---

## §8 Dissents Preserved

**Dissent D-KM-1.** Karpathy's "save everything qualitative, trust the wiki" vs D28 "anchor mandatory" produces a genuine policy disagreement between Karpathy's operational pattern and Jetix's Lock. This card resolves it as "D28 wins" — but the cost (serendipitous cross-anchor connection loss) is real and should not be silently absorbed. The `/build-graph` community detection mitigation is theoretical (not yet validated in Jetix cycles). If Wave C observes low cross-anchor discovery, revisit D28 with a proposal for a "broad capture" mode that anchors to a meta-topic rather than a specific project.

**Dissent D-KM-2.** The Forte PARA framework maps cleanly to Jetix's directory structure, but PARA was designed for a single human, not a multi-agent system. The "actionability" principle assumes one decision-maker's current priorities. In Jetix, a Resource for Ruslan may be a Project for the sales-lead agent. This card does not resolve this — it surfaces it as an unresolved architectural tension for OQ-KM-3 above.

---

## §9 Provenance

| Source | Path / URL | Used in |
|--------|-----------|---------|
| Karpathy LLM Wiki gist | `raw/articles/karpathy-llm-wiki-gist-2026-04.md` | §2, §4 Principles 1, 5, 6 |
| Karpathy 2025 Year in Review | `raw/articles/karpathy-year-in-review-2025.html` (canonical: karpathy.bearblog.dev/year-in-review-2025/) | §3 Source 4 |
| Jetix wiki v3 substrate | `wiki/index.md`, `wiki/graph/edges.jsonl`, `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` §8 | §1, §4 Principles 1, 6 |
| Wave A candidate-parts-merged | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md` Parts 2, 3 | §6 work-list |
| CLAUDE.md Wiki Architecture v2 | `CLAUDE.md` §Wiki Architecture v2 section | §2, §3 Source 3, §6 |
| Schmidt "Fabrication of Serendipity" | https://www.sociologica.unibo.it/article/view/8350 (external-1) | §2, §4 Principle 2, §4 Principle 6 |
| Matuschak "Evergreen notes" | https://notes.andymatuschak.org/Evergreen_notes (external-2) | §2, §4 Principles 3, 6 |
| Forte "The PARA Method" | https://fortelabs.com/blog/para/ (external-3) | §2, §4 Principle 4, §5 T1 |
| Matuschak + Nielsen "Tools for Thought" | https://numinous.productions/ttft/ (external-5) | §3 Source 5, §4 Principle 5 |

*Note: Source numbering in §3 follows the brief's 5-source mandate. Source 4 (Karpathy year-in-review) and Source 5 (Matuschak/Nielsen 2019) are the two "additional" web sources beyond the three primary framework authors.*

---

*Card produced by engineering-expert × integrator, Phase B-2. Promoted to canonical only after philosophy-expert critic pass + Ruslan ack.*
