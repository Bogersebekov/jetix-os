---
title: Engineering × Critic — Wiki v3 Ingest/Retrieval Audit
type: critique
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: expert-judgment-from-tier1-citations
tier: core
produced_by: engineering-critic
sources:
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1/D8/D6/D7"}
  - {path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md", range: "Part A/B/F/G"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§0-§8"}
  - {path: "prompts/km-architecture-research-2026-04-24.md", range: "§1-§3/§6.4/§11"}
  - {path: ".claude/skills/ingest.md", range: "full"}
  - {path: ".claude/skills/ask.md", range: "full"}
related: []
binding_scope: km-architecture-engineering-lens
mode: critic
---

# Engineering × Critic — Wiki v3 Ingest/Retrieval Audit

> **Scope statement.** This critic evaluates the EXISTING wiki v3 ingest/retrieval
> mechanics as a substrate on which KM Layer-A variants will be built. It identifies
> what is provably sufficient, what has gaps, and what is architecturally missing for
> UC-9 (client-isolation) and UC-10 (offline-first inference). It does NOT propose
> variants — that is integrator-mode work. All claims carry F / ClaimScope / R triples.
> Every verdict is binary.

---

## §1 Conformance Checklist (binary)

| # | Check | Verdict | F | ClaimScope | R |
|---|---|---|---|---|---|
| H-1 | Does the existing `/ingest` skill (`.claude/skills/ingest.md`) handle UC-1 video-transcript ingest — producing ≥5 concept pages + ≥8 typed edges + correct niche routing — WITHOUT requiring code change? | **PARTIAL (treated as NO)** | F4 | Jetix Phase-A `swarm/wiki/` v3 with existing skill body as read; fails on the ≥8 typed-edge guarantee | medium |
| H-2 | Does the Q1 4-tier retrieval stack (direct → index+grep → typed-BFS → long-context fallback) as specified in D8 `/ask` skill meet UC-2 weekly-digest ≤180s latency floor at G2 (5,000 pages)? | **NO** | F3 | Jetix Phase-A `swarm/wiki/` v3; G2 = 5,000 pages; knowledge-arch research Part G.2 ground truth | medium |
| H-3 | Does any existing skill or protocol in wiki v3 enforce a filesystem-namespace boundary preventing Client-A's `/ask` from retrieving Client-B's wiki content (UC-9 client-isolation)? | **NO** | F5 | Jetix Phase-A single-tenant deployment; multi-tenant architecture not yet instantiated | high |
| H-4 | Does the Tier-D long-context fallback in `/ask` (Q1 Tier-4) operate without an external LLM API call, satisfying UC-10 offline-first inference? | **NO** | F4 | Applies to Tier-4 synthesis step only (not Tier-1/2/3 filesystem grep); Claude Code Max-plan session required for any LLM synthesis | high |
| H-5 | Does the existing W-5 Two-level CE write-back (W-5: `agents/<expert>/strategies.md` → `swarm/wiki/meta/agent-improvements/`) enforce a static check that prevents `/consolidate` from merging a Cell-A strategies.md entry into a peer expert's strategies via cross-namespace merge? | **NO** | F4 | Phase-A single-repo; no namespace-isolation lint rule for strategies.md entries in `/consolidate` body | medium |
| H-6 | Does `/ingest` produce ≥5 concept pages from a transcript by CONSTRUCTION (enforced by skill body), or only by LLM-best-effort (no count predicate)? | **NO (best-effort only)** | F5 | `/ingest` step 3 says "10-15 ключевых элементов" — target not a hard floor; no exit condition enforcing ≥5 concept-type pages | high |
| H-7 | Does the current D8 `/ask` skill implement typed-BFS over `edges.jsonl` as a distinct algorithmic step (Tier-3), or does it collapse Tier-3 into the grep step? | **NO (Tier-3 is implicit)** | F4 | `/ask` body reads: "при необходимости — grep по ключевым словам + идти глубже по wikilinks (не более 2 уровней)" — this is ad-hoc depth-2 link follow, not a systematic PPR/BFS over the full edges.jsonl graph | medium |
| H-8 | Does the existing skill ecosystem include a dedicated `/ingest-client` or equivalent namespace-isolated ingest path that routes content to a per-client wiki root, satisfying UC-9 by construction? | **NO** | F5 | D8 documents 5 in-scope skills; no per-client variant exists; D7 `wiki-roots.yaml` is single-wiki parameterization, not multi-wiki isolation | high |

---

## §2 Acceptance Predicates (per "no" check)

**H-1 — partial on ≥8 typed-edge guarantee:**
Hamel-binary fix: `/ingest` step 6 adds an explicit post-write assertion: `count(edges appended to edges.jsonl for this ingest run) ≥ 8 OR skill returns structured error "insufficient-edges: N found, 8 required, add cross-concept typed links before committing"`.
Invariants: WLNK=applies (downstream `/ask` Tier-3 BFS depends on edges being non-trivially populated; preserving edge count floor protects consumer), MONO=preserve (increasing edge count floor does not regress quality), IDEM=preserve (re-running ingest on same source is idempotent per existing dedup logic), COMM=N/A, LOC=applies (change is ingest-local; does not touch `/ask` or edges consumer logic).

**H-2 — latency floor at G2:**
Hamel-binary fix: `/ask` algorithm acquires a time-budget variable `T_budget = 180s` with explicit timeout on Tier-2 grep step: `grep --timeout=30s $WIKI_ROOT/**/*.md`. Tier-3 BFS is capped at `max_hops=2, max_nodes=50`. Tier-4 long-context fallback is bypassed if Tier-2+3 return ≥5 pages.
Invariants: WLNK=applies (callers of /ask expect a response; timeout preserves liveness), MONO=applies (shorter timeout may reduce recall at G2 — this is a known tradeoff, not a quality regression below the 180s floor), IDEM=preserve, COMM=N/A, LOC=applies (change is /ask-internal).

**H-3 — UC-9 client-isolation missing:**
Hamel-binary fix: `wiki-roots.yaml` gains a `clients:` map with per-client root entries; `$WIKI_ROOT_CLIENT_{ID}` env var is set at session init; `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph` all assert `$WIKI_ROOT_CLIENT_ID` matches the target root before any Read/Write. Fix must be BY CONSTRUCTION (directory enforcement), not by policy comment.
Invariants: WLNK=applies (all callers of `/ask` must see only their client's pages — contract broken today if multi-tenant), MONO=preserve, IDEM=preserve, COMM=N/A, LOC=NO (touches all 5 skills — LOC violation; this is intentional cross-scope enforcement, not a scope leak; it is the minimum change required).

**H-4 — UC-10 offline-first synthesis:**
Hamel-binary fix: `/ask` Tier-4 is redesigned to produce a locally-rendered plaintext synthesis from retrieved pages WITHOUT an LLM call when `OFFLINE_MODE=1` env var is set. The synthesis is a structured excerpt compilation (top-5 pages, their definitions, their key claims) rather than LLM-authored prose. LLM synthesis remains the default online path; offline synthesis is the UC-10 fallback.
Invariants: WLNK=applies (UC-10 clients depend on synthesis working offline), MONO=applies (offline synthesis quality is lower than LLM synthesis — this is the stated UC-10 tradeoff), IDEM=preserve, COMM=N/A, LOC=applies (change is /ask Tier-4 only).

**H-5 — strategies.md cross-namespace merge protection:**
Hamel-binary fix: `/consolidate` adds a pre-merge guard: `if source_path contains "agents/" AND source_path contains "strategies.md": REJECT with "strategies.md files are per-expert personal memory; use swarm/wiki/meta/agent-improvements/ for cross-agent promotion"`.
Invariants: WLNK=preserve (strategies.md is per-expert per D6 §6.6.3), MONO=preserve, IDEM=preserve, COMM=N/A, LOC=applies.

**H-6 — concept count not enforced by construction:**
Hamel-binary fix: `/ingest` step 3 adds a post-extraction count gate: `concept_pages = [x for x in extracted if x.type == "concept"]; if len(concept_pages) < 5: log WARNING "Only N concept pages extracted — re-run step 3 with broader extraction or proceed with N (user decision)"`.
Invariants: WLNK=applies (UC-1 requires ≥5 concept pages for downstream training corpus), MONO=preserve, IDEM=preserve, COMM=N/A, LOC=applies.

**H-7 — Tier-3 BFS is implicit, not systematic:**
Hamel-binary fix: `/ask` step 2 adds an explicit Tier-3 algorithm: after Tier-2 grep returns candidate pages, extract their `related[]` and `edges.jsonl` entries, expand to depth-2 neighbor pages, score by PPR-approximation (edge-weighted frequency count as a proxy for full PPR). Return top-20 combined candidates.
Invariants: WLNK=applies (Tier-3 is the retrieval layer Q1 specifies for multi-hop queries), MONO=preserve (more systematic BFS improves precision), IDEM=preserve, COMM=N/A, LOC=applies.

**H-8 — no per-client wiki isolation path:**
Hamel-binary fix: new skill `/ingest-client --client-id=<id>` that sets `WIKI_ROOT=$WIKI_ROOT_CLIENTS/<id>` and enforces the isolated ingest path. Alternatively, extend `/ingest` with `--client-id=<id>` flag that routes to a per-client subtree. Either fix requires a parallel `/ask --client-id=<id>` enforcement.
Invariants: WLNK=applies (multi-tenant clients are isolated consumers), MONO=preserve, IDEM=preserve, COMM=N/A, LOC=NO (systemic change — same rationale as H-3).

---

## §3 Alternatives (≥2 per "no")

**H-1 alternatives:**
- Alt-A: Add count gate inside existing `/ingest` step 3 (Wave-A extension — modify existing skill). Simple, maintains single-skill surface. Kill condition: fails if an input source genuinely yields fewer than 5 distinct concepts (e.g., a 2-page memo); gate becomes an annoying false-positive blocker.
- Alt-B: Add a new post-ingest skill `/ingest-verify` that re-reads the newly written pages and asserts the count predicate (Wave-B — separate verification step). Cleaner separation, more robust. Kill condition: adds an extra invocation cost per ingest; brigadier must chain two skills for every ingest.

**H-2 alternatives:**
- Alt-A: Enforce `T_budget=180s` per `/ask` execution by adding explicit grep-timeout and hop limits to the existing skill body. Low-cost. Kill condition: at G2 (5,000 pages) even a 30s grep per step may fail on slow storage; assumes filesystem grep is fast enough (true for local SSD, unknown for NFS/remote).
- Alt-B: Pre-build a per-niche BM25-style inverted index at `/build-graph` time (written to `swarm/wiki/graph/index-<niche>.json`) so Tier-2 grep is replaced by index-lookup. Kill condition: index build time grows with wiki size; adds write surface; Phase-A Max-subscription constraint limits this to a pure filesystem implementation of BM25.

**H-3 alternatives:**
- Alt-A: Extend `wiki-roots.yaml` with a `clients:` map and enforce client-scoped roots in all 5 skills via env-var check at startup. Builds on existing D7 parameterization. Kill condition: env-var enforcement is process-level, not OS-level; a bug in the skill body could still read across roots. Requires auditing all Read/Write calls in all 5 skills for compliance.
- Alt-B: Separate filesystem trees under `clients/<client-id>/wiki/` with OS-level directory permissions set at deployment time. By-construction isolation. Kill condition: requires deployment automation that Jetix does not yet have; Phase-A is single-developer; OS permissions are not managed by the skill ecosystem today.

**H-4 alternatives:**
- Alt-A: `/ask` Tier-4 gains `OFFLINE_MODE=1` flag producing structured-excerpt synthesis without LLM. Online path unchanged. Kill condition: offline synthesis quality is significantly lower; clients may not accept it as the same product.
- Alt-B: Pre-build locally-distilled Llama/DeepSeek inference (UC-10 mandate from BIOS-insight §6) that replaces Claude Code synthesis for client-private paths. Kill condition: requires distillation infrastructure not present in Phase A; this is a Phase-B/C build, not an ingest/retrieval fix.

**H-5 alternatives:**
- Alt-A: Add a pre-merge guard in `/consolidate` that rejects any merge target containing `agents/` path prefix. Low-cost, specific to the known failure mode. Kill condition: guard is a heuristic; if strategies.md is moved to a different path, it breaks.
- Alt-B: `/consolidate` is prohibited from touching any path matching `agents/<expert>/strategies.md` by a `/lint` rule added to its own startup self-check (analogous to D6 §6.6 permission self-check). More robust. Kill condition: adds complexity to `/consolidate` startup; must be maintained when per-agent paths change.

**H-6 alternatives:**
- Alt-A: Hard count gate inside `/ingest` step 3 with user-decision escape hatch ("proceed with N?" prompt). Kill condition: interactive prompt breaks headless/automated ingest runs.
- Alt-B: Soft warning in `/ingest` output (log WARN "N < 5 concept pages") without blocking; brigadier reads the warning in the structured return and decides to re-invoke or accept. Kill condition: brigadier may silently accept subthreshold output without re-invoking; UC-1 acceptance criteria not met.

**H-7 alternatives:**
- Alt-A: Explicit Tier-3 BFS step added to `/ask` step 2, using `edges.jsonl` as the graph source, capped at depth-2/max-20-nodes. No new infrastructure. Kill condition: at G2 (5,000 pages, ~5,700 edges per knowledge-arch §G.2), depth-2 BFS may surface up to 400 candidate nodes; filtering to 20 requires a scoring function not currently in the skill body.
- Alt-B: Implement a full HippoRAG PPR retrieval step using `edges.jsonl` as the knowledge graph and query keywords as seed nodes (per knowledge-arch §B.2 pseudocode). Produces ranked retrieval. Kill condition: PPR requires computing PageRank iteratively; Phase-A constraint is filesystem+Claude Code tools only — no networkx available without Bash+pip; PPR must be approximated in pure Claude Code logic.

**H-8 alternatives:**
- Alt-A: Extend D7 `wiki-roots.yaml` with `clients:` map + per-client `WIKI_ROOT` env; extend all 5 skills with `--client-id` flag. Incremental extension of existing architecture. Kill condition: same as H-3 Alt-A — env-var enforcement is not OS-level isolation.
- Alt-B: Separate Git repositories per client, each with their own `swarm/wiki/` tree. Jetix methodology is pushed as a versioned Git submodule or template. By-construction isolation at the repo level. Kill condition: multiple repos dramatically increase operational complexity for Phase A single-developer setup; brigadier would need to manage cross-repo coordination.

---

## §4 Anti-scope

- **NOT proposing Layer-A variants.** That is integrator-mode work. This critic produces gap analysis only.
- **NOT touching legacy `wiki/` v2 or the 14 legacy agents** under `.claude/agents/` (not in the Phase-A roster). All references are to `swarm/wiki/` v3.
- **NOT proposing implementation.** The acceptance predicates in §2 name what a fix would look like; the selection of which fix to implement is for Ruslan + brigadier.
- **NOT proposing Tier-4 book reads.** All citations are from Phase-A Tier-1 sources (decisions/, design/, raw/research/, prompts/). No corpus read triggered.
- **NOT evaluating Layer-B project-mgmt mechanics.** Scope is UC-1..UC-10 against wiki v3 ingest/retrieval substrate only.
- **NOT re-opening 24 Locks, FPF E-items, W-decisions, or shared-protocols 9 sections.** Those are locked inputs.
- **NOT proposing paid APIs, vector DBs, or paid embeddings.** All fix proposals use filesystem + grep + skill-body logic only (D6 §6.10 Max-subscription discipline).
- **NOT evaluating the capital impact of the gaps.** That is investor-expert territory.

---

## §5 UC-1..UC-10 Baseline Coverage Assessment

**UC-1 — Video Ingest (ingestion pipeline that learns):**
PARTIAL. `/ingest` exists and routes to `swarm/wiki/` v3 with correct frontmatter (D2). However: (a) no hard floor on ≥5 concept pages (H-6 NO); (b) no hard floor on ≥8 typed edges (H-1 PARTIAL); (c) niche routing for the systems-expert theme wiki (`themes/systems/`) is not explicitly wired in the skill body — step 2 assigns a single niche but does not differentiate between entity-spine location (`concepts/`) and theme-wiki location (`themes/systems/concepts/`); (d) "new knowledge alert" for weekly digest is not produced by ingest itself — it depends on `/build-graph` or `/lint` being run separately.
F: F4 | ClaimScope: Jetix Phase-A single-user session, skill body as-read 2026-04-24 | R: medium

**UC-2 — Weekly Digest Query:**
PARTIAL. `/ask` produces a retrieval+synthesis flow, but: (a) no dedicated weekly-digest aggregator skill exists; (b) no mechanism writes "new pages this week" signal to `meta/health.md` after each ingest; (c) Tier-3 BFS is implicit not systematic (H-7 NO); (d) 180s latency floor at G2 is unproven (H-2 NO). A human-driven `/ask "что нового за неделю?"` works today at G1 (557 pages) but has no structural guarantee at G2+.
F: F4 | ClaimScope: Jetix Phase-A G1 scale | R: medium

**UC-3 — Deep Problem Synthesis:**
PARTIAL. `/ask` + depth-2 wikilink following handles single-session synthesis. Gaps: no systematic multi-hop Tier-3 BFS (H-7); no HyDE enhancement (knowledge-arch §B.5 identifies this as a known improvement for domain-specific queries); at G2+, precision degrades without PPR or community summaries.
F: F3 | ClaimScope: Jetix Phase-A G1, single-session | R: medium

**UC-4 — Skill Activation (agent uses wiki to bootstrap a new skill):**
PASS at G1. Q6 skill pipeline (`skills/{candidates,learning,active,usage}/`) is specified in D1 + D11. `/lint` check #10 enforces the Q8 Phase-A lock on `insights/`. Agent reads from `swarm/wiki/skills/active/` + associated `swarm/wiki/themes/<expert>/` pages via niche symlinks. No structural gap identified for single-tenant use.
F: F4 | ClaimScope: Jetix Phase-A single-tenant | R: medium

**UC-5 — Client Onboarding (new client gets a bootstrapped project-wiki):**
FAIL at the architecture level for multi-client. The D1 tree has no per-client namespace. D7 `wiki-roots.yaml` has one default root. H-3 and H-8 are both NO. For single Jetix internal use (Ruslan onboarding a new Jetix project), UC-5 works via Layer-6 `operations/<project-slug>/`. For client-facing deployment, the substrate does not support it.
F: F5 | ClaimScope: multi-client deployment; single-tenant Jetix internal PASS | R: high

**UC-6 — Cross-Project Knowledge Leverage:**
PARTIAL. Layer-7 `global/compound-rules/` + `meta/agent-improvements/` exist as the designated write-back target. W-5 Two-level CE write-back defines the protocol in principle. However: no skill currently implements the `agents/<expert>/strategies.md → swarm/wiki/global/compound-rules/` promotion step; that promotion is brigadier-manual per D6 §6.2. No cross-project edge type exists beyond `layer-ref` and `derived_from` in D3.
F: F4 | ClaimScope: Jetix Phase-A, brigadier-manual promotion | R: medium

**UC-7 — Contradiction Detection and Resolution:**
PARTIAL. `/lint` Q5 signal #4 detects `contradicts`+`invalidates` edge integrity. D3 §3.2.2 requires bidirectional `contradicts` edges. `/build-graph` detects them. However: no automated claim-stance-downgrade trigger (`asserted → contested when contradiction_count > 0`) exists in the skill body. Contradiction detection is passive (lint reports it) not active (skill updates stance).
F: F4 | ClaimScope: Jetix Phase-A, passive detection | R: medium

**UC-8 — Scale (wiki grows from 557 to 5K to 50K pages):**
PARTIAL at G1, FAIL at G2+. Knowledge-arch §G.1-G.3 specifies: G2 (5K pages) needs namespace sharding + periodic `/consolidate` daily + BM25 sparse index; G3 (50K pages) needs hybrid BM25+dense+PPR+Neo4j. None of these exist in the current skill ecosystem. D8 skills are G1-tuned. H-2 NO.
F: F3 | ClaimScope: knowledge-arch §G.1-G.3 research ground truth; Jetix current G1 | R: medium

**UC-9 — Client Isolation (two simultaneous Jetix clients cannot observe each other's KB):**
FAIL. By construction NO exists (H-3 NO, H-8 NO). The current substrate is single-tenant. Directory namespacing for multi-client is absent. D7 `wiki-roots.yaml` provides single-wiki parameterization, not client-isolation. The BIOS-insight §6 explicitly lists "client-isolation mechanics" as MISSING for client-facing production. This is a strategic failure mode per the brief's disqualification criteria.
F: F5 | ClaimScope: multi-tenant Jetix client deployment | R: high

**UC-10 — Offline-First Inference (client AI archivist works disconnected from cloud LLMs):**
FAIL. By construction NO exists (H-4 NO). Every synthesis step in `/ask` depends on a live Claude Code session (Claude Code Max plan = cloud LLM). Tier-4 long-context fallback is still an LLM call. The locally-distilled Llama/DeepSeek path named in BIOS-insight §3 does not exist in the current skill ecosystem. This is a strategic failure mode per the brief's disqualification criteria.
F: F5 | ClaimScope: client-private offline inference path | R: high

---

## §6 UC-9 + UC-10 Architectural Feasibility Flag

**Existing substrate can prove UC-9 (client-isolation) by construction: NO.**

Reason: The v3 wiki substrate is single-tenant by design. The `$WIKI_ROOT` parameterization in D7 provides a single configurable root, not a per-client isolated namespace. There is no mechanism in any of the 5 skills that binds a session to exactly one client's subtree and rejects reads/writes to any other. The `wiki-roots.yaml` has no `clients:` map. No OS-level or process-level enforcement of cross-client boundary exists. The BIOS-insight §6 explicitly lists "client-isolation mechanics" as missing for client-facing production. The gap is STRUCTURAL: adding client-isolation requires extending D7, extending all 5 skills with client-id enforcement, and adding a deployment step that provisions per-client roots. This is not fixable by a policy note; it requires architectural extension.
F: F5 | ClaimScope: multi-tenant Jetix client deployment scenario | R: high

**Existing substrate can prove UC-10 (offline-first inference) by construction: NO.**

Reason: Every retrieval tier in `/ask` that produces synthesized prose depends on a Claude Code session with an active Claude Sonnet/Opus connection. Tier-1/2/3 (filesystem grep + BFS) are offline-capable for page RETRIEVAL, but Tier-4 (long-context synthesis) and the final synthesis step (step 4 of `/ask`) both require LLM inference. The "offline" path that the BIOS-insight §3 mandates — locally-distilled Llama/DeepSeek/Mistral answering questions about client-private data while network-disconnected — is not present in any current skill body or in D8. The Max-subscription discipline (D6 §6.10) actively prohibits third-party API calls, but does not provision a local-inference path. The gap is ARCHITECTURAL: providing offline synthesis requires either (a) a local LLM inference layer (Phase B/C build) or (b) a degraded-mode structured-excerpt synthesis (no LLM) per the H-4 Alt-A fix.

**How these flags drive integrator's variant generation:**

Any Layer-A variant that does not address H-3, H-4, H-8 simultaneously is disqualified per the brief §1.2 + §1.3. The integrator must generate variants where UC-9 and UC-10 are proven BY CONSTRUCTION at the variant's architectural level — not as optional add-ons. The three most architecturally distinct paths the integrator has to work with are:
(a) Single shared wiki with per-client namespace enforcement via `wiki-roots.yaml` extension (Dir-level isolation, policy-enforced at skill startup),
(b) Per-client Git repository with Jetix methodology as a versioned template (Repo-level isolation, by-construction),
(c) Per-client isolated filesystem tree with OS-level directory permissions + offline inference via a locally-distilled LLM (Hardware-level isolation, by-construction).
Path (a) passes UC-9 by policy, not by construction — barely acceptable per the brief. Paths (b) and (c) pass by construction.
F: F4 | ClaimScope: KM architecture variant design space given current substrate gaps | R: medium

---

## §7 Provenance

- [src-1] `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D8 §8.3: `/ingest` step 6 edge enum, step 3 extraction target. Direct evidence for H-1, H-6, H-7 verdicts.
- [src-2] `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D7 §7.2: `wiki-roots.yaml` single `default_root` field, no `clients:` map. Direct evidence for H-3, H-8 verdicts.
- [src-3] `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D6 §6.10: "All retrieval Phase A is filesystem + ripgrep + typed-BFS per Q1 + Sub-agent C §1." Evidence for H-4 verdict (no local LLM inference path in Max-subscription discipline).
- [src-4] `raw/research/knowledge-architecture-deep-research-2026-04-19.md` Part G §G.2: "HippoRAG PPR на 572 edges (сейчас) — тривиальная операция. При 5,000 pages и ~5,700 edges — всё ещё быстро в памяти." Evidence for H-2 verdict (latency unproven, not guaranteed at G2).
- [src-5] `raw/research/knowledge-architecture-deep-research-2026-04-19.md` Part B §B.2: HippoRAG PPR pseudocode showing keyword-extraction → seed-nodes → PPR ranking. Evidence for H-7 verdict (current `/ask` implements informal depth-2 link following, not PPR).
- [src-6] `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` §6: "Missing для client-facing production: Client-isolation mechanics — how exactly we spawn per-client wiki/agents without cross-contamination." Direct evidence for H-3, H-8 verdicts and UC-9 fail.
- [src-7] `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` §3: "Offline-first AI integration — Llama/DeepSeek distilled для local inference." Direct evidence for H-4 verdict and UC-10 fail.
- [src-8] `prompts/km-architecture-research-2026-04-24.md` §1.2 point 7: "Every variant MUST architecturally prove UC-9 (client-isolation) and UC-10 (offline-first inference) — by construction, not by policy." Binding quality bar for §6 flags.
- [src-9] `.claude/skills/ingest.md` step 3: "10-15 ключевых элементов" (best-effort, no hard floor). Direct evidence for H-6 verdict.
- [src-10] `.claude/skills/ask.md` step 2: "grep по ключевым словам... идти глубже (не более 2 уровней)" — no mention of `edges.jsonl` BFS as a distinct step. Direct evidence for H-7 verdict.
- [src-11] `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D8 §8.4 L29 note: "(Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)" Evidence that Tier-4 is LLM-dependent and H-4 is NO.
- [src-12] `raw/research/knowledge-architecture-deep-research-2026-04-19.md` Part F §F.2: "Three writeback mechanisms: explicit writeback (/ask → comparisons/), agent-triggered, scheduled consolidation." Evidence for UC-6 PARTIAL (no automated strategies.md → global/compound-rules/ promotion).
