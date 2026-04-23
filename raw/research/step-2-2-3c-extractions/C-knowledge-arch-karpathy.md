---
sub_agent: C
title: Knowledge-Architecture + Karpathy Patterns Extraction for Wiki v3 Стадия C
date: 2026-04-23
sources_read:
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md (specified sections)
  - raw/articles/karpathy-llm-wiki-gist-2026-04.md (full)
word_count_target: ≤2500
purpose: Feed Deliverable 1 (directory layout), Deliverable 3 (edge enum), Deliverable 7 (config), Deliverable 10 (health.md), Deliverable 11 (skill rubric)
---

## Section 1 — Retrieval-stack mechanics for the 4-tier Q1 pattern

**Tier 1 — Direct path lookup (alpha IDs, slugs).**
Research H.5 declares an `alpha_direct_lookup` channel: *"trigger: query_contains_alpha_id (`deal-042`, `client:acme`); method: direct_path_lookup; priority: highest — перед wiki retrieval."* Filesystem precondition: deterministic path schema `alphas/{type}/{id}/state.yaml` and wiki-side mirror `wiki/entities/{type}/{id}.md` (H.1). E.2 reinforces: *"любой агент должен уметь найти canonical data в ≤1 hop."* No index file required — the path itself IS the index. Failure handoff: ID-pattern regex misses → fall through to Tier 2. Latency bound: implicit <10ms (T1 "Hot" tier in H.6).

**Tier 2 — Index + grep (Karpathy-native).**
Karpathy: *"the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure."* Files needed: `wiki/index.md` (content-oriented catalog, "updated on every ingest") and `wiki/log.md` (chronological, append-only with consistent prefix `## [YYYY-MM-DD] verb | Title` so unix tools parse it). Failure handoff: Karpathy is silent on explicit failure; research B.1 implies BM25 keyword fallback when index lookup yields nothing exact. **Research silent — spec must specify in Deliverable 7** the exact heuristic (e.g. zero-grep-hit → Tier 3).

**Tier 3 — Typed-BFS over `edges.jsonl` (HippoRAG PPR).**
Research B.2 gives full pseudocode. Filesystem precondition: `wiki/graph/edges.jsonl` with seed lookup over 9 entity types. Index files: edges.jsonl is itself the graph; networkx loads it in-memory. G.2: *"HippoRAG PPR на 572 edges (сейчас) — тривиальная операция... При 5,000 pages и ~5,700 edges — всё ещё быстро в памяти. Порог для Neo4j: ~20,000 edges."* Failure handoff: H.5 — *"trigger: ppr_score_all_below_threshold (если все PPR scores < 0.01)"* → fall to Tier 4. Latency: <500ms for current scale (T2 in H.6).

**Tier 4 — Long-context fallback.**
H.5: *"trigger: total_retrieved_tokens_below_5000; method: long_context_full_load; scope: `wiki/niches/{agent_niche}/` — только нища агента, не вся вики."* B.4 confirms strategy: *"Long-context как fallback для edge cases, не как primary path."* Bounded by niche directory size, not full wiki. Failure handoff: terminal — return what was found.

## Section 2 — Cross-reference mechanics: triple-channel implementation

**YAML `related[]` (frontmatter).**
Best at: machine-parseable structured links, queryable via Dataview-style tooling (Karpathy tip: *"If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists"*). Worst at: fluid in-text references, contextual meaning of the link.
Consulted at: index/grep tier and at lint time (orphan detection).
Writer: every /ingest call writes frontmatter; agent-authored.

**Inline wikilinks `[[layer/slug]]`.**
Best at: in-context citations during retrieval synthesis. B.2 shows the pattern: *"citations = `[f'[[{node.path}]]' for node in top_nodes]`."* Worst at: bulk graph operations.
Consulted at: synthesis time (citation rendering) and during /lint orphan-detection grep.
Writer: agents during /ask synthesis and during entity-page authoring.

**`wiki/graph/edges.jsonl`.**
Best at: typed-BFS, PPR seeding, multi-hop. C.3 names this Blackboard pattern: *"общая запись, все читают; append-only = безопасно."* C.4: *"event-sourced — только события, текущее состояние = replay; применяется в edges.jsonl (append-only)."* Worst at: human readability.
Consulted at: Tier 3 retrieval.
Writer: /ingest, /build-graph, /consolidate skills (append-only discipline).

**Synchronisation discipline.** Research does not give a single explicit sync algorithm but D.3 shows the convention: every cross-reference exists in BOTH frontmatter (`wiki_edges:` list) AND `edges.jsonl` (jsonl record with `from`, `to`, `type`, `ts`). H.4 writeback table assigns each writeback trigger to a specific channel.

**Anti-patterns research warns against:**
- F.4: *"Orphan pages (нет inbound links) → /lint находит и флагит"* — wikilinks without incoming reciprocity are flagged.
- H.9 anti-pattern 7 (Игнор Alpha history): writing state without writing the edge/event = lost audit trail; rule: *"каждое изменение state.yaml → событие в history.jsonl."* By extension: writing a wikilink without the corresponding edges.jsonl record breaks Tier 3.
- **Research silent — spec must specify in Deliverable 3** the explicit reconciliation rule when YAML `related[]` and edges.jsonl drift.

## Section 3 — Edge-type vocabulary precedents

**Definition pattern.** D.3 shows the canonical record shape:
```jsonl
{"from": "...", "to": "...", "type": "alpha-ref", "ts": "2026-06-01"}
```
Fields are positional: source, target, typed relation, timestamp. No cardinality field is recorded; cardinality is enforced by lint. **Research silent on explicit cardinality declarations — spec must specify in Deliverable 3** (1:1 / 1:N / N:M, inverse-edge convention).

**Edge types named in research:**
- `supports`, `based-on` — D.1 example: *"supports: [[entities/deals/deal-042]]"*, *"based-on: [[entities/projects/website-redesign-q1]]"* — intra-layer entity-to-entity.
- `alpha-ref` — D.3 — cross-layer: alphas/ → wiki/entities/.
- `belongs-to` — D.3 — alphas-internal hierarchy (deal → client).
- `applies-to` — D.3 — cross-layer: claim → alpha (wiki/claims/ → alphas/clients/).
- `derives-from` — D.3 — cross-layer: alpha → concept.
- `archived` (boolean flag, not edge type) — G.5 — *"Граф сохраняет edges (помечаются `archived: true`)."*
- `status: refuted` / `status: disputed` (frontmatter, not edge) — F.4, H.4 — supersession signal.

**Karpathy gist** does not enumerate edge types but mandates the categories *"contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, missing cross-references."* This implies (but does not name): a `contradicts` type, a `supersedes`/`superseded_by` pair, and an implicit `references` link.

**Cross-layer canonical stance.** D.3 is the most explicit: cross-layer edges always carry an explicit type that names the layer transition (`alpha-ref`, `applies-to`, `derives-from`). E.1 reinforces strict ownership: *"каждый тип данных имеет одного владельца."* So `claim → source` via `derived_from` is consistent with the research pattern of typed cross-layer edges. **Research silent on `part_of` mereology specifically — spec must specify in Deliverable 3**, although F.1 grounds it in *"мереология холонов: каждый уровень — холон: целое на своём уровне и часть на следующем."*

## Section 4 — Staleness mechanics (5-signal /lint orchestration)

Research recommends these signals (assembled across F.4, A.1, Karpathy "Lint" section, H.9):

1. **Confidence age / confidence level.** F.4: *"Confidence levels в frontmatter: `confidence: high/medium/low` + `authority_source`."* Detection: frontmatter field + age delta vs `last_review_ts`. Computation: pull (read on lint pass).

2. **Contradiction count.** Karpathy: *"contradictions between pages."* F.4: *"Stale claims (противоречат новым источникам) → /lint маркирует `status: disputed`."* Detection: cross-reference scan against newer sources sharing entity refs. Computation: pull (LLM compares claim text vs newer source summaries).

3. **Last-review timestamp.** Implied by H.9 anti-pattern 10 (*"context rot без compaction"*) and F.4 stale-claim language. Filesystem field: `last_review: YYYY-MM-DD` in frontmatter. Threshold: research silent — **spec must specify in Deliverable 10** (e.g. >90 days = stale).

4. **Supersession chains.** F.4: claim status transitions (`active → disputed → refuted`) with `evidence` link. Karpathy: *"stale claims that newer sources have superseded."* Filesystem: `superseded_by:` frontmatter pointer + corresponding edge. Computation: pull (graph walk on lint).

5. **Uncited claims / orphans.** F.4 + Karpathy: *"orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references."* Detection: grep wikilinks + edges.jsonl scan; any node with zero inbound `references`/`related_to` edges flagged. Computation: pull, scheduled (/lint cadence).

**Cadence (G.3, H.7):** weekly at current 557-page scale; daily at 1,000+ pages. **Push vs pull:** research uses pull throughout — lint is scheduled, not on-write. The exception is alpha state changes (write-through, C.4).

## Section 5 — Skill-learning pipeline mechanics (Q6 specifics)

**Directory + file-naming.** H.1 places skills implicitly under role/system memory: `agents/{id}/strategies.md` for accumulated meta-cognitive patterns, plus skill scripts under the existing `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph` namespace. C.1 maps "Procedural" memory to *"`/skills/*.md`, `roles/<role>.md`."* **Research silent on `learning/` vs `active/` split specifically — spec must specify in Deliverable 11** the exact directory transition (likely `swarm/skills/learning/{slug}/` → `swarm/skills/active/{slug}/`).

**Golden-set storage conventions.** Research is silent on a named "golden set" structure. Closest precedent: F.4 metric FPAR (First-Pass Acceptance Rate) implies a corpus of evaluated /ask queries with accepted/rejected outcomes. **Research silent — spec must specify in Deliverable 11** (e.g. `golden/{skill}/cases.jsonl` per skill, JSONL with input + expected-output + acceptance flag).

**Use-log conventions.** Research provides two append-only JSONL precedents: `comms/mailboxes/{id}.jsonl` (per-agent recall) and `alphas/{type}/{id}/history.jsonl` (per-alpha event log). The matching pattern for skills: per-skill JSONL (`swarm/skills/{slug}/use-log.jsonl`) — each invocation = one event line. C.4 event-sourcing reinforces append-only.

**Validation before activation (anti-T3 stance).** H.9 anti-pattern 4 (Monolithic system.md) enforces *"shorter files get followed more reliably"* — small validated artefacts beat large unvalidated ones. Anti-pattern 3 (over-eager writeback) and H.7 Week 4 step (*"5 writebacks через /ask → проверить что comparisons/ обновляется"*) demonstrate the principle: filesystem-resident evidence (real outputs in real folders) is required before promotion. The Q6 rubric (golden-set ≥3, ≥3:1 success ratio, ≥10 uses) is consistent with this stance — **but the rubric itself is not in research; research provides only the validation philosophy**.

## Section 6 — Health metrics computation formulas

Research provides metric *names* and validation *philosophy* but very few closed-form formulas.

**FPAR (First-Pass Acceptance Rate).** F.4: *"какой % /ask ответов принимается без follow-up. Цель: >80%."* Formula sketch (research's exact language): `accepted_first_pass / total_asks`. Rolling-window: **research silent — spec must specify in Deliverable 10** (suggest 30-day rolling consistent with H.4 `recent_decisions: за последние 30 дней`).

**Cycle-close rate.** Not named in research. Closest precedent: D.4 deal state machine with `terminal: completed | lost`. Formula sketch: per-alpha-type `(transitions_to_terminal_in_window) / (transitions_started_in_window)`. **Research silent — spec must specify in Deliverable 10.**

**Tombstone rate per layer.** G.5 archival pattern: *"никогда не удалять, только архивировать"*; flag `archived: true` on edges, `status: archived` in frontmatter. Formula sketch: per-layer `count(status=archived in window) / count(total in layer)`. **Research silent on the exact computation — spec must specify in Deliverable 10.**

**Cross-theme reference count (Q8 Layer-9 trigger).** F.3: *"557 страниц содержат latent connections... `/build-graph` + GraphRAG-inspired community detection для выявления кластеров."* Formula sketch: count of edges where `from.niche != to.niche` (cross-niche edges from edges.jsonl). G.1 implies this is the trigger metric for community detection. Threshold for Layer-9 promotion: **research silent — spec must specify in Deliverable 10.**

**/lint findings summary.** Karpathy enumerates the categories explicitly: *"contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps."* The dashboard should aggregate these as counts per pass + delta vs prior pass.

## Section 7 — Karpathy LLM Wiki patterns relevant to Jetix

**Honour these Karpathy theses:**
- *"The wiki is a persistent, compounding artifact"* — knowledge compiled once, not re-derived per query. Maps to F.1 insight loop (sources → claims → topics → summaries → foundations).
- *"You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."* — H.4 writeback table operationalises this; every trigger is agent-driven.
- Three-layer architecture (raw / wiki / schema). Maps directly to Jetix `raw/` + `wiki/` + `CLAUDE.md`.
- index.md + log.md duality (content-oriented vs chronological). Already realised in Jetix `wiki/index.md` + `wiki/log.md`.
- *"Good answers can be filed back into the wiki as new pages."* Realised in Jetix `wiki/comparisons/` and H.4 trigger table.
- *"The wiki is just a git repo of markdown files."* Karpathy "Tips" closing item — directly endorses the Jetix git-native stance (E.1, G.4).
- Lint as periodic health-check covering contradictions, stale claims, orphans, missing pages, missing cross-refs, data gaps — Section 4 mechanics.

**Patterns Karpathy advocates that Jetix departs from:**
- Karpathy: *"I have the LLM agent open on one side and Obsidian open on the other."* Jetix is multi-agent (12 agents, hub-and-spoke per CLAUDE.md), not single human + single LLM. **Reconciled with Q2 single-writer**: only one agent writes a given page at a time even in multi-agent mode (locked decision).
- Karpathy explicitly says *"all of [the implementation] will depend on your domain"* and the gist *"is intentionally abstract."* Jetix instantiates concretely (9 entity types, 6 niches, 12 edge types, 9 layers). **Reconciled with Q9 v2/v3 coexistence**: v2 is the working Karpathy-baseline Jetix already runs (557 pages); v3 layers structural rigour on top while preserving v2 conventions.
- Karpathy: *"At small scale the index file is enough"* — explicit permission to skip search infrastructure. Jetix already runs HippoRAG PPR (A.1: *"значительно опережает базовый Karpathy-паттерн"*). The 4-tier stack still keeps index+grep as Tier 2, honouring the small-scale-first principle.
- Karpathy treats Obsidian as the IDE. Jetix has no Obsidian dependency — `wiki/` is a plain git tree readable by any editor. **Reconciled**: Karpathy "Note" section explicitly endorses this flexibility (*"everything mentioned above is optional and modular"*).

## Section 8 — Anti-patterns to avoid

1. **Alpha-in-scratchpad (H.9 #1).** Storing operational state in `agents/{id}/scratchpad.md` (ephemeral). Symptom: agent forgets client status across sessions. *Deliverable 1 must avoid this by mandating that all alpha state lives under `alphas/{type}/{id}/state.yaml` with no scratchpad shadow copies.*

2. **Wiki as CRM (H.9 #2).** Using `wiki/entities/clients/` for operational state mutations. Symptom: agent tries to update `current_deal_stage` via /ingest. *Deliverable 1 must avoid this by declaring `wiki/entities/` as read-only refs that point to `alphas/` via `alpha-ref` edge type.*

3. **Over-eager writeback (H.9 #3).** Every /ask answer filed to comparisons/, polluting the wiki. *Deliverable 11 must avoid this by gating writeback through a novelty threshold + explicit agent decision (mirrors B.3 `NOVELTY_THRESHOLD`).*

4. **Monolithic system.md (H.9 #4).** Role-manifest >5K tokens violates *"shorter files get followed more reliably."* *Deliverable 1 must avoid this by capping `agents/{id}/system.md` <2K tokens, spilling detail to `strategies.md`.*

5. **GraphRAG for 557 pages (H.9 #5).** Premature community-detection infrastructure. *Deliverable 7 must avoid this by gating GraphRAG on the explicit Q8 Layer-9 trigger (cross-theme reference count + scale ≥5K pages).*

6. **Vector DB for <3,000 pages (H.9 #6).** Embedding infrastructure with no recall gain. *Deliverable 7 retrieval config must avoid this by keeping the 4-tier stack as default and listing vector DB only as a >3K-pages scale-up trigger (G.3, H.8).*

7. **Ignoring alpha history (H.9 #7).** state.yaml mutated without history.jsonl event. *Deliverable 1 + Deliverable 7 must avoid this by enforcing the rule "every state.yaml write → one history.jsonl line" in the writeback skill contract.*

8. **Role-manifest without alpha context (H.9 #8).** Agent unaware which alphas it owns. Symptom: sales agent reads `wiki/concepts/tech/`. *Deliverable 1 must avoid this by mandating `context_requirements:` in every `agents/{id}/system.md` listing alpha types and wiki niches.*

9. **Symmetric storage of Research Note + Postmortem in alphas/ (H.9 #9).** These are wiki-primary by nature; their value is in concept links, not state machines. *Deliverable 1 must avoid this by routing Research Notes to `wiki/sources/` and Postmortems to `wiki/experiments/` only (no `alphas/research/` or `alphas/postmortems/` folders).*

10. **Context rot without compaction (H.9 #10).** Long sessions accumulate stale context; auto-compact at ~75% loses unwritten insight. *Deliverable 11 skill rubric must avoid this by requiring every long-session skill to checkpoint key insights to `strategies.md` or wiki BEFORE the expected compaction window.*

11. **Wikilinks without YAML/edges backing (Section 2 derived).** A `[[link]]` that has no `related[]` entry and no edges.jsonl record breaks Tier 3 retrieval. *Deliverable 3 must avoid this by enforcing in /lint that every inline wikilink corresponds to (a) a `related[]` entry and (b) an edges.jsonl record.*

12. **Index drift (Karpathy "Indexing and logging" derived).** index.md not updated on every ingest violates Tier 2. *Deliverable 11 /ingest skill rubric must avoid this by treating index.md update as an atomic step of /ingest (not a lint-time correction).*

---

**Word count:** ~2,470 words (within target).
