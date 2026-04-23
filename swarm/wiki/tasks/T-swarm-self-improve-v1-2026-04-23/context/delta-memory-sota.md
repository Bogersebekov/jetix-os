---
id: context-delta-memory-sota
title: "Phase 1 δ — Memory SOTA patterns (not yet adopted)"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-delta
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - {path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md", range: "1-828"}
  - {path: "raw/articles/karpathy-llm-wiki-gist-2026-04.md", range: "1-75"}
  - {path: "swarm/lib/shared-protocols.md", range: "233-275"}
  - {path: "swarm/lib/shared-protocols.md", range: "41-105"}
---

## TL;DR

Phase-A Jetix swarm already runs a Karpathy-grade LLM wiki with
pipeline frontmatter, 4-tier retrieval (direct / index-grep /
typed-BFS / niche long-context), and brigadier-gated writes
[swarm/lib/shared-protocols.md:256-270]. Nine SOTA patterns in the
2026-04-19 research corpus are NOT YET adopted and close concrete
retrieval / writeback / context-loading gaps: HippoRAG Personalized
PageRank, HippoRAG-2 passage-integration, HyDE seed-expansion, Mem0
lazy decay + LOCOMO eval, Tiago Forte CODE Distill→Express loop,
MemGPT-style tiered paging, sleep-time consolidation runs, Zettelkasten
folgezettel addressing, Luhmann-style explicit contradiction-flagging,
GraphRAG community summaries. Five are implementable under Phase-A
Max-subscription lock (no vector DB, no paid embeddings, Read/Write/
Grep/Glob/Bash only [swarm/lib/shared-protocols.md:249-254, 270-271]):
PPR-over-edges, HyDE-free-LLM, CODE Distill loops, MemGPT tiers via
context-loading layer-ordering, and Zettelkasten ID discipline. Four
require Phase B (GraphRAG communities, Mem0 prod API, embeddings,
dense retrieval). Expected 2× gains concentrate on Tier-3 BFS recall
and writeback compounding.

## SOTA pattern inventory

| # | Pattern | Source | What it does (1 line) | Phase-A gap it closes | Phase-A feasibility | Confidence |
|---|---------|--------|-----------------------|-----------------------|---------------------|------------|
| 1 | HippoRAG Personalized PageRank over typed KG | NeurIPS 2024 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:31-39] | Seeds from LLM-extracted keywords → PPR associative walk over graph → top-K nodes, multi-hop without embeddings | Tier-3 BFS is currently uniform typed-BFS [swarm/lib/shared-protocols.md:260-264]; no ranking = weaker recall on multi-hop | now (1-sprint hook into existing `graph/edges.jsonl`) | high |
| 2 | HippoRAG-2 deeper passage integration | ICML 2025 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:39] | +7% associativity via online LLM use on top-K passages | Retrieve-and-synthesize re-reads raw nodes without passage re-ranking | 1-sprint (on top of #1) | medium |
| 3 | HyDE hypothetical-page seeding | [raw/research/knowledge-architecture-deep-research-2026-04-19.md:99, 189-191] | LLM drafts a hypothetical wiki page for the query → extract keywords from *it* → better seed nodes | Current Tier-2 index+grep relies on literal keyword match [swarm/lib/shared-protocols.md:260-262] | now (one extra LLM turn) | high |
| 4 | Mem0 lazy decay + LOCOMO eval | arXiv 2504.19413 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:46-47] | Extract/consolidate/retrieve loops; 26% better than baseline, 91% p95 latency cut, >90% token save | No mailbox / strategies.md decay policy; `comms/mailboxes/*.jsonl` grows unbounded | Phase B for API; NOW for the *decay discipline* (locally implementable as a /consolidate sub-step) | medium |
| 5 | Tiago Forte CODE Distill→Express loop | BASB [raw/research/knowledge-architecture-deep-research-2026-04-19.md:74-82, 404-420] | Capture→Organize→Distill→Express; distill = claims→patterns→summaries→foundations | Phase-A has the holonic pipeline `claims→topics→summaries→foundations` [raw/research/knowledge-architecture-deep-research-2026-04-19.md:404-417] but no explicit Distill trigger or Express step | now (skill addition: `/distill`) | high |
| 6 | MemGPT tiered memory paging | arXiv 2310.08560 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:42-43, 709-716] | Agent as OS process, explicit move of data between in-context / hot / warm / cold tiers via interrupts | Shared-protocols §9 defines retrieval tiers but not a *memory* tier contract per agent; context-loading ordering exists only conceptually | now (loader script + layer priorities per H.3 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:591-659]) | high |
| 7 | Karpathy writeback-of-answers | Karpathy gist [raw/articles/karpathy-llm-wiki-gist-2026-04.md:39] | "Good answers can be filed back into the wiki as new pages" — comparisons/ is the landing zone | Phase-A has `/ask` shape but no enforced writeback hook with novelty threshold [raw/research/knowledge-architecture-deep-research-2026-04-19.md:771] | now (provenance-gated comparisons/ write) | high |
| 8 | Zettelkasten folgezettel addressing | Luhmann/Ahrens [raw/research/knowledge-architecture-deep-research-2026-04-19.md:68-72] | Unique hierarchic IDs (1a, 1a1, 1a2) make sibling / branching structure an intrinsic index independent of filesystem | Phase-A uses ULID-like IDs; branching structure carried only by `related[]` edges and directory tree | 1-sprint (ID scheme decision + retrofit script) | low |
| 9 | Luhmann contradiction-partner | [raw/research/knowledge-architecture-deep-research-2026-04-19.md:70] | System flags when a new card contradicts existing; treat wiki as "communication partner that surprises" | `/lint` flags orphans / stale claims [raw/research/knowledge-architecture-deep-research-2026-04-19.md:435-439] but not explicit contradiction surfacing beyond §2 gate [swarm/lib/shared-protocols.md:79-80] | 1-sprint (extend `/lint` check) | medium |
| 10 | GraphRAG community detection | arXiv 2404.16130 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:25-29] | Pre-compute entity communities, per-community summaries, fan-out partial answers → synthesis — serves *global* sensemaking | Phase-A Tier-4 long-context fallback bounded to niche dir [swarm/lib/shared-protocols.md:263-264]; no global summary generation | Phase B only (over-engineering below ~5K pages per [raw/research/knowledge-architecture-deep-research-2026-04-19.md:775]) | high |
| 11 | Sleep-time compute (background consolidation) | implied by `/consolidate` weekly [raw/research/knowledge-architecture-deep-research-2026-04-19.md:428, 736] | Off-cycle cron that synthesizes episodic→semantic when no user load | No scheduled `/consolidate` or `/lint` in Phase-A ritual; only on-demand | now (commit+push ritual extension [swarm/lib/shared-protocols.md:273-274]) | medium |
| 12 | Self-RAG deciding when to retrieve | NeurIPS 2023 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:100] | LLM decides whether retrieval is needed at all | Retrieve-and-synthesize always retrieves; wastes turns on trivial queries | reject — "requires obuchenie of special LLM" [raw/research/knowledge-architecture-deep-research-2026-04-19.md:100] Phase B at most | low |

## Deep dives on top-5 candidates

### 1. HippoRAG PPR over `graph/edges.jsonl`

HippoRAG treats the LLM as neocortex and the typed knowledge graph as
a hippocampus; query keywords seed Personalized PageRank with α=0.85,
producing an associative top-K that outperforms dense baselines by up
to 20% on multi-hop QA at ~10-30× lower cost and 6-13× faster
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:33-38].
The pseudo-code is already spelled in the research
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:104-131]
and maps directly onto Phase-A assets: `swarm/wiki/graph/edges.jsonl`
is the KG; the brigadier's retrieve-and-synthesize is the neocortex.
**Jetix implementation sketch:** add `swarm/lib/retrieve/hipporag.py`
(Bash-invocable; Python stdlib + `networkx` is allowed under §9
Read/Write/Grep/Glob/Bash scope [swarm/lib/shared-protocols.md:270-271]
— `networkx` is pure-Python, no SDK). Wire it as the Tier-3 primitive
replacing raw typed-BFS in shared-protocols §9 [swarm/lib/shared-protocols.md:256-264].
**2× claim / measurable criterion:** Tier-3 recall@20 measured over
the first 100 `/ask` invocations after rollout should rise from the
current typed-BFS baseline to ≥0.80 (the same threshold §9 already
specifies as the Phase-B embedding trigger [swarm/lib/shared-protocols.md:266-268]).
Meeting ≥0.80 via PPR *defers* the Phase-B embedding decision — that
itself is the 2× gain (cost avoided + recall raised).

### 2. HyDE seed-expansion (free LLM turns, no API)

HyDE improves retrieval recall when the user query stylistically
differs from corpus documents: the LLM drafts a hypothetical answer,
and that synthetic document's keywords become the seed set
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:189-191].
Under Phase-A Max lock this is free — it is one extra in-session LLM
turn, not a paid API call. **Implementation sketch:** insert a
pre-retrieval stage in the `/ask` skill pipeline (v2 per CLAUDE.md
Wiki Architecture §). Before Tier-2 index+grep
[swarm/lib/shared-protocols.md:260-262], the skill asks the model
"write the wiki page that would answer this" (≤300 tokens), extracts
named entities / concepts, and feeds those as the grep seeds. **2×
claim:** on queries whose literal wording does not appear in any wiki
page title or frontmatter tag (measure: count such queries over 50
samples), HyDE should produce at least one non-zero-score seed ≥2× as
often as literal grep. Criterion: "queries-answered-non-empty" metric
in `swarm/wiki/meta/health.md` rises on HyDE-eligible subset.

### 3. Tiago Forte CODE Distill→Express (skill: `/distill`)

CODE prescribes that captured knowledge must be Distilled (compressed
to core insight) and Expressed (made usable by downstream work) or it
rots [raw/research/knowledge-architecture-deep-research-2026-04-19.md:74-82].
Phase-A already has the Левенчук holonic ladder
`claims → topics → summaries → foundations`
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:404-417]
but no explicit Distill trigger — promotion happens only under
`/consolidate`. **Implementation sketch:** new skill manifest
`/distill <claim-id>` (per D8 skills pattern, brigadier-only write
per §5 `role_tool_matrix` [swarm/lib/shared-protocols.md:145-152]) that
reads a claim page, finds supporting/contradicting edges, and drafts
either a topic or summary page into `drafts/`. The Express step maps
to writeback rule: when a foundation changes, `/distill` emits a
`mode: writing-support` packet per §7 [swarm/lib/shared-protocols.md:181-199]
for downstream agents. **2× claim:** weekly count of promoted
`claims → topics` edges (rebuild edges-jsonl delta) doubles relative
to the `/consolidate`-only baseline. Criterion: `log.md` tallies in
the first 4 weeks.

### 4. MemGPT tiered paging via H.3 context loader

MemGPT reframes the agent as an OS process that pages between fast
context and slow storage [raw/research/knowledge-architecture-deep-research-2026-04-19.md:42-43].
Phase-A has the retrieval 4-tier [swarm/lib/shared-protocols.md:256-264]
but not an explicit *memory* tier per agent. The H.3 loader
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:591-659]
already lists the correct layer ordering: system.md → strategies.md →
task+alpha → HippoRAG → decisions → mailbox → scratchpad, with
compression priority from bottom-up. **Implementation sketch:** add
`swarm/lib/context-loader.md` as a pattern spec (referenced by expert
§7 import-stubs) encoding the 7-layer priority + the compression rule
"auto-compact drops L7→L4, never L1-L3". Enforce via a
PostToolUse-equivalent local gate [swarm/lib/shared-protocols.md:212-213]
that rejects any agent session whose opening prompt lacks L1-L3.
**2× claim:** sessions exceeding ~75% context (auto-compact threshold
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:228-230, 784-785])
retain the ruslan-attested core identity 100% of the time vs the
current "hope it survives" baseline.

### 5. Karpathy writeback loop (comparisons/ with novelty threshold)

Karpathy's central operational claim: "good answers can be filed back
into the wiki as new pages" [raw/articles/karpathy-llm-wiki-gist-2026-04.md:39]
and the research explicitly enumerates it as Jetix writeback pattern
#1 [raw/research/knowledge-architecture-deep-research-2026-04-19.md:425-427].
Without it the wiki stagnates instead of compounding
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:799].
Anti-pattern H.9-#3 warns: naive writeback pollutes with low-quality
content; a novelty threshold is required [raw/research/knowledge-architecture-deep-research-2026-04-19.md:771].
**Implementation sketch:** brigadier post-processes every `/ask` with
an `llm_assess_novelty` check; if score > threshold (tune in
`meta/health.md`), auto-draft `swarm/wiki/comparisons/<slug>.md` into
`drafts/` for §2 gate promotion [swarm/lib/shared-protocols.md:61-83].
Comparisons receive `produced_by: <agent>-writing-support` per §7
lock [swarm/lib/shared-protocols.md:196-203]. **2× claim:**
comparisons/ grows at ≥2× the rate of orphan-rate growth in `/lint`
reports (measure: delta comparisons per week vs delta orphans per week).
Compounding signal: novelty-threshold miss-rate falls over time.

## Retrieval-stack contrast

Current Phase-A 4-tier stack (verbatim §9 [swarm/lib/shared-protocols.md:256-264]):

- Tier 1 — Direct path Read.
- Tier 2 — `index.md` walk + `rg` grep.
- Tier 3 — typed-BFS over `graph/edges.jsonl`, expand via D3 edge types.
- Tier 4 — long-context fallback bounded to current niche dir.

SOTA suggests the Tier-3 primitive is under-powered. The research
claims raw typed-BFS degrades relative to PPR on multi-hop
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:96, 104-131]
and HippoRAG-2 adds passage-level reranking on top
[raw/research/knowledge-architecture-deep-research-2026-04-19.md:39].

Specific Phase-A-compatible improvements to Tier 3:

1. **Replace BFS ranking with PPR scores.** Keep typed-BFS as *graph
   traversal*, but re-rank candidates by PPR over the full
   `edges.jsonl` personalized on LLM-extracted keywords. No new deps
   beyond pure-Python `networkx`; respects §9 prohibition list
   [swarm/lib/shared-protocols.md:249-254].
2. **HyDE seeds before Tier-2.** Raise the quality of the seed set
   that feeds Tier 3 (see deep-dive #2).
3. **Alpha-aware filter.** Filter PPR results by the caller's declared
   alpha context [raw/research/knowledge-architecture-deep-research-2026-04-19.md:126-129];
   Phase-A alphas live in the swarm-alphas foundation
   [swarm/wiki/foundations/swarm-alphas.md — present per dir listing].
4. **Passage rerank pass (HippoRAG-2).** After PPR top-K, one cheap
   in-session LLM pass ranks *passages* inside each node. Free under
   Max lock.
5. **Decision for Phase B deferral stays.** §9 already specifies
   embedding re-evaluation when Tier-3 recall < 0.80 over rolling 100
   `/ask` invocations [swarm/lib/shared-protocols.md:266-268]. The
   PPR upgrade is the natural last move before that trigger fires.

Tier 4 remains the escape hatch; GraphRAG community summaries are the
*right* Tier-4 evolution at 5K+ pages but premature now (see caveats).

## Reading comprehension caveats

The research explicitly flags patterns that work only at scale and
should be rejected for Phase A:

- **GraphRAG community detection is over-engineering below 5K
  pages.** Anti-pattern H.9-#5 verbatim: "переинжиниринг с community
  detection при текущем масштабе. PPR уже делает лучше дешевле"
  [raw/research/knowledge-architecture-deep-research-2026-04-19.md:775].
  Swarm wiki graph currently lists 4 files under `swarm/wiki/graph/`
  (directory listing: communities.md, cross-tree.jsonl, edges.jsonl,
  summaries.md). Build out community summaries by hand at first;
  automated detection is Phase B.
- **Vector DBs below 3,000 pages.** Anti-pattern H.9-#6:
  "Дополнительная инфраструктура без выигрыша. HippoRAG PPR
  outperforms dense retrieval на multi-hop без embeddings"
  [raw/research/knowledge-architecture-deep-research-2026-04-19.md:777].
  This matches §9 prohibition list [swarm/lib/shared-protocols.md:249-254].
- **Mem0 production API.** The 26%/91%/>90% numbers are LOCOMO
  benchmark results [raw/research/knowledge-architecture-deep-research-2026-04-19.md:47];
  production track record is called "ограничен (2025 — early adoption)"
  [raw/research/knowledge-architecture-deep-research-2026-04-19.md:47].
  And the API is a paid third-party [swarm/lib/shared-protocols.md:252].
  Phase A can adopt only the *discipline* (lazy decay + consolidation),
  not the service.
- **HippoRAG PPR performance at >10K nodes is unknown.**
  "Production-scale опыт HippoRAG на 10,000+ страниц ограничен"
  [raw/research/knowledge-architecture-deep-research-2026-04-19.md:39]
  and "точный performance threshold HippoRAG PPR при больших графах
  не задокументирован в production — open research question"
  [raw/research/knowledge-architecture-deep-research-2026-04-19.md:457].
  Phase-A swarm is far below that ceiling, so adoption is safe now —
  but do not assume the same decision survives 10K scale.
- **Self-RAG requires trained LLM.** "Требует обучения специального
  LLM" [raw/research/knowledge-architecture-deep-research-2026-04-19.md:100].
  Not Phase A.
- **Karpathy pattern's "surprisingly well" applies at ~100 sources /
  hundreds of pages.** [raw/articles/karpathy-llm-wiki-gist-2026-04.md:47]
  Once >5K pages the index.md-first retrieval degrades; that is the
  natural trigger to re-open the Tier-2/3 trade-off.

## Questions for integrator

1. Does `networkx` (pure-Python, MIT-licensed, no SDK) count as a
   "tool" under §5 `role_tool_matrix` [swarm/lib/shared-protocols.md:145-152],
   or is it a transparent library used via Bash? HippoRAG PPR rollout
   depends on this call.
2. For HyDE's extra LLM turn inside `/ask`: does it count against the
   skill's `maxTurns` budget? If yes, `/ask` manifest needs a turn-count
   bump.
3. Novelty-threshold calibration for the Karpathy writeback loop —
   should it be a global constant in `meta/health.md` or per-niche?
   Research gives no prior.
4. Folgezettel ID retrofit: is the current ULID-style ID a hard
   invariant (Lock 17 or similar), or is a cycle-scoped ID migration
   acceptable? Zettelkasten gain is small if retrofit disruption is
   large.
5. `/distill` skill falls squarely in the expert `writing-support`
   mode per §7 [swarm/lib/shared-protocols.md:181-199] — confirm that
   claim→topic promotion is a brigadier-only write, not expert-direct.
6. Phase-A wiki page count right now: listings under
   `swarm/wiki/foundations/`, `swarm/wiki/graph/` confirm the swarm
   wiki is very early (5 foundation subdirs + swarm-alphas.md + 4
   graph files). Research thresholds (1K, 5K, 10K, 50K) all sit above
   current scale — should scale triggers be ported verbatim or
   re-baselined for the swarm-wiki subtree?

## Provenance

All claims trace to four canonical Phase-A files:

- `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
  Parts A-H (lines 11-828) — primary SOTA corpus.
- `raw/articles/karpathy-llm-wiki-gist-2026-04.md` lines 1-75 —
  Karpathy pattern source.
- `swarm/lib/shared-protocols.md` §9 (lines 233-275) — current
  retrieval-stack contract and Max-subscription lock.
- `swarm/lib/shared-protocols.md` §§1-8 (lines 41-231) — current
  write protocol, provenance gate, and tool-permission matrix against
  which feasibility is graded.

Directory listings (`swarm/wiki/foundations/`, `swarm/wiki/graph/`)
used to confirm Phase-A scale and existing scaffolding; pure
filesystem evidence, no external content extracted.

No inlined source bodies exceed 5 continuous lines. Every numbered
pattern, feasibility judgement, and 2× claim cites at least one
`[path:line-range]` anchor in the corpus.
