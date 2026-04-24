---
title: Deep Execution Prompt — KM Architecture Materialization MVP (A1 full + B2 full + B3-merged + Company-as-Code)
date: 2026-04-24
type: execution-prompt
author: Claude Code on server (writing deep prompt per meta-brief)
target_executor: fresh Claude Code session (7-day Stage-Gated sprint)
input_meta_brief: prompts/meta-brief-km-materialization-mvp-2026-04-24.md
output_this_pass: physical MVP in repo + decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md (≥3000-word execution report)
estimated_duration: ~7 days across 5 Stage-Gated phases (≤20-30h swarm work + 4-6 Ruslan review gates)
precedes: first quick-money P1 project bootstrap → first Mittelstand outreach batch
relates_to:
  - prompts/meta-brief-km-materialization-mvp-2026-04-24.md
  - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md (Ruslan Gate-2 anchor, acked 2026-04-24T21:00:00Z)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
  - decisions/JETIX-VISION.md (D22 ICP for quick-money bootstrap)
  - decisions/JETIX-PLAN.md (D3 Phase 1 €50K Q2 2026)
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 foundation)
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md
  - swarm/lib/shared-protocols.md (9-section runtime contract)
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md
  - .claude/agents/brigadier.md
  - CLAUDE.md
locked_decisions_referenced: [D13, D17, D18, D19, D20, D21, D24, W-5, HD-01, HD-02]
m_class_budget_impact: 1 structural M-task (this materialization); leaves 1 slot open for M3 or companion
quality_bar: 1000% depth — every skill executable, every config declarative, every commit provenance-tight
ruslan_gate_2_decision_verbatim: "A1 full ADOPT + B2 full ADOPT + B3 MERGE INTO B2 as internal mechanic + company-as-code cross-cutting. NO A2 (deferred to first paying client). NO A3 (deferred to 3K+ pages per client). NO B1 (rejected)."
---

# Deep Execution Prompt — KM Architecture Materialization MVP

## §1 Mission + Critical Framing (read three times before starting)

### §1.1 The verbatim mission

You are a fresh Claude Code session on `claude/jolly-margulis-915d34` charged with PHYSICALLY materializing Ruslan's chosen Knowledge-Management + Project-Management architecture MVP over ~7 days. The decision upstream of you is locked:

- **A1 Karpathy++ filesystem-native substrate — ADOPT FULL as wiki substrate.** Lowest cost; ready today; supports UC-9 Phase-A policy-based client isolation + UC-10 structured-citation offline path.
- **B2 Rich mini-swarm — ADOPT FULL as project-management pattern.** Cagan + PMBOK + mini-swarm-of-3 = right shape for serious Jetix projects.
- **B3 Adaptive stage-gates — MERGE INTO B2 as internal mechanic.** Keep the stage-gate predicates (Hamel-binary) + reversibility (`/project-de-morph`) for `bets` / `research` tiers + intra-B2 promotion (`/project-promote`). B3 does NOT survive as a standalone variant; its mechanism becomes optional B2 scaffolding controlled by the `--adaptive` flag.
- **A2 Federated peer holons — DEFERRED.** Trigger: first paying client signed. Not needed at €0 revenue.
- **A3 GraphRAG + HippoRAG hybrid — DEFERRED.** Trigger: 3K+ pages per client. Over-engineering at G1.
- **B1 Thin namespaces — REJECTED.** Not enough structure for Jetix's needs.

The **cross-cutting principle** Ruslan made explicit via voice 2026-04-24:
> *"в режиме GitHub работала — компания как код, знания как код, чтобы это вместе соединить."*

Everything git-versioned. Declarative config under `.claude/config/*.yaml`. Atomic commits with structured messages. Real rollback via `git revert`. Every KB change = commit. This is the operational manifestation of D17 filesystem-SoT + W-5 Two-level CE + knowledge-as-moat.

### §1.2 Why this matters (1000% depth reminder)

**This materialization is THE moment Jetix stops planning and starts compounding.** Every file you create lives for years — wiki entries accumulate into the Private-Library moat, project scaffolds become templates for future clients, the first `quick-money` project bootstrap is the seed for the €50K Q2 2026 trajectory (JETIX-PLAN D3). Shallow wiring = broken KB forever.

**1000% depth. No "good enough".**

- Every skill you write passes `bash -n <skill>.md.lib.sh` syntactic check (if bash helpers exist) AND has executable bit + shebang (`#!/usr/bin/env bash`) + `set -euo pipefail` + 1-line purpose comment at the top + named functions, not inline god-loops.
- Every `*.md` artefact carries YAML frontmatter complete per CLAUDE.md conventions + shared-protocols §2 provenance gate (sources[], produced_by, confidence_method, tier).
- Every config file is declarative, git-versioned, zero Jetix-specific hardcoding (no literal `quick-money` in skill bodies; everything parameterised via config).
- Every test-fixture is reproducible, deterministic, named under `swarm/tests/fixtures/km-mvp/`.
- Every commit has a structured message `[<area>] <verb> <what> (<why>)` and is pushed immediately.

**Ruslan's Gate-2 context (non-negotiable):** 6 variants analyzed across 20-cell matrix dispatch, 3 adopted with specific shapes (A1 full, B2 full, B3 merged into B2), cross-cutting "company-as-code / knowledge-as-code" principle. Honor every choice. Do not re-litigate variant decisions. Do not add A2/A3/B1 elements — they are explicitly deferred or rejected. If you feel tempted to add A2-style federated peer holons because "it would be cleaner" — STOP. It was deferred for a reason (Taleb barbell: no paying client, no substrate). Write what Ruslan acked. Not more.

### §1.3 What you are NOT

- You are NOT a variant researcher. The research is done. Read the variant drafts once, extract specs, move on.
- You are NOT a re-opener of 24 Locks, FPF E-items, W-decisions, or shared-protocols §§1-9. They are sealed.
- You are NOT authorized for paid API calls. Max-subscription discipline absolute. Grep for `ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY` in every file you commit — must return zero hits in body/scripts (may appear only in `unset`-style guards).
- You are NOT touching legacy `wiki/` v2 tree OR the 14 legacy `.claude/agents/*.md` agents (crazy-agent, inbox-processor, knowledge-synth, life-coach, manager, meta-agent, personal-assistant, sales-lead, sales-outreach, sales-researcher, staging-writer, strategist, sweep-worker, system-admin). All new work under `swarm/` + `.claude/skills/` + `.claude/config/` + `.claude/agents/<new-slugs>.md`.
- You are NOT authorized to write to Notion. D17 filesystem-SoT. Ruslan syncs Notion views himself if he chooses.
- You are NOT authorized to execute Part G report writing without an explicit Ruslan ack of the Part F verification packet. Stage-Gated pause is hard.
- You are NOT authorized to `git commit --amend` after push, `git push --force`, or `--no-verify` anywhere.

### §1.4 Quality bar — per-artefact checklist (use before every commit)

Before each commit, walk this list for every changed file:

1. **Path correctness.** Is the file under the canonical tree for its type (`.claude/config/`, `.claude/skills/`, `.claude/agents/`, `swarm/wiki/operations/`, `swarm/wiki/_templates/`, `swarm/tests/fixtures/`, `swarm/lib/`)?
2. **Frontmatter complete** per `swarm/wiki/_templates/<type>.md` (fields: title, type, layer/niche, created, last_modified, pipeline, state, confidence, confidence_method, tier, produced_by, sources[], related[], binding_scope, granularity).
3. **Provenance tight** per shared-protocols §2: sources[] non-empty when pipeline ∈ {compiled, linted, ready}; inline `[src:<path>]` citations present in non-trivial paragraphs.
4. **Edges consistent.** Every `[[wikilink]]` in body has matching `related[]` entry AND `swarm/wiki/graph/edges.jsonl` record.
5. **Shebang + set -euo pipefail** for every bash helper or skill-embedded script.
6. **No hardcoded Jetix-specific paths** in skill code or config. Use `${WIKI_ROOT}` resolution (D7 §7.4) + `.claude/config/*.yaml` for all parameterisation.
7. **No provider API-key references.** Run: `grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' <changed-files>` — expect zero hits in body/script. Only allowed appearance: `unset`-guard lines in operator-side session-start hooks (not committed into skill bodies).
8. **YAML validity.** Run: `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file.yaml>` — exit 0 required.
9. **Commit message structured** per `[<area>] <verb> <what> (<why>)` grammar.

If ANY item fails, stop. Fix. Do not commit broken work.

### §1.5 Operational cadence

- **Working branch:** `claude/jolly-margulis-915d34` (current). No new branch unless explicitly asked.
- **Commit cadence:** per-skill creation or per-logical-unit (not per-file). Target: 15-25 commits across the 7 days.
- **Push cadence:** immediately after each commit. Ruslan peeks at progress via commits; no silent local work.
- **Turn budget:** Max-subscription only. Aim for ~20-30h of swarm turns total. If you hit a wall, write an `AMBIGUITY-*.md` packet (see §11) and escalate, not guess.
- **Escalation signal:** `swarm/gates/AWAITING-APPROVAL-*.md` packet + explicit pause. Between Part F and Part G is a hard pause; all other checkpoints are commit-then-continue.

Re-read §1.1-§1.5 before starting Part A. Then proceed.

---

## §2 Scope — Parts A through G (7-day phased execution)

The 7 days split into 5 functional phases (Parts A/B/C/D/E) + verification (Part F) + report (Part G). **Part D is cross-cutting** — company-as-code / knowledge-as-code discipline applies to every Part; do not treat it as a separate day. It sets the bar for every commit, config, and skill in Parts A/B/C/E.

### §2.A Part A — A1 Karpathy++ substrate (Days 1-2)

**Anchor source:** `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md` §§4-6. Read once before starting.

**Goal of Part A:** make A1 the wiki substrate in day-1 operational state. UC-1 ingest / UC-2 digest / UC-3 solve-with-wiki / UC-9 Phase-A client isolation primitives / UC-10 offline-first structured-citation path all live and testable before Part B begins.

#### A.1 Extend `.claude/config/wiki-roots.yaml` with `clients:` section

**File to modify:** `.claude/config/wiki-roots.yaml` (existing; schema_version 1 at 2026-04-23).

**Add (after existing keys):**

```yaml
# Client-isolation stanza (A1 UC-9 Phase-A per variant-A1 §5 Layer-1).
# Environment-variable convention: WIKI_ROOT_CLIENT_ID=<slug> selects client holon.
# When unset, skills default to Jetix-internal swarm/wiki/ root.
clients:
  # Seed entry — demo client for UC-ISOLATION-DEMO test fixture.
  demo-client-a:
    root: clients/demo-client-a/swarm/wiki/
    methodology_remote: jetix-methodology-repo    # read-only upstream for methodology-push
    granularity: client:demo-client-a
    inference_stack: ollama-mistral-7b-q4         # per Phase-B activation; Phase-A = structured-excerpt
    default_inference_tier: T-Offline
    compliance_classification: gdpr-standard
  demo-client-b:
    root: clients/demo-client-b/swarm/wiki/
    methodology_remote: jetix-methodology-repo
    granularity: client:demo-client-b
    inference_stack: ollama-mistral-7b-q4
    default_inference_tier: T-Offline
    compliance_classification: gdpr-standard

# Resolution algorithm (per D7 §7.4 + A1 §5 UC-9 Layer-1):
#   1. If WIKI_ROOT_CLIENT_ID env-var set AND matches a key in clients:
#        → ${WIKI_ROOT} := clients.<id>.root
#      AND impose `granularity: client:<id>` as default for all new artefacts.
#      AND impose Read-scope restriction: reject any path outside resolved root.
#   2. Else if WIKI_ROOT env-var set: ${WIKI_ROOT} := $WIKI_ROOT (legacy override).
#   3. Else: ${WIKI_ROOT} := wiki_root_v3 (default swarm/wiki/).
#
# Phase-A policy enforcement: Read-scope check is a SKILL responsibility
# (guardrail at skill entry). Phase-B strengthens with OS-level UNIX user
# separation per A2 variant (deferred; trigger = first paying client).

# Seed the demo-client directories so UC-ISOLATION-DEMO has a real target.
# Directory creation is idempotent and performed by tools/bootstrap-demo-clients.sh.
```

**Schema bump:** set `schema_version: 2`, `last_modified: <today>`.

**Guard:** when editing, add inline comment before the `clients:` block:
> *"DO NOT add production clients here without an AWAITING-APPROVAL-wiki-roots-clients-<slug>-<date>.md committed to swarm/gates/ first. Demo entries (demo-client-a/-b) exist for UC-ISOLATION-DEMO test fixture only."*

**Commit message:** `[km-mvp] extend wiki-roots.yaml with clients: stanza for UC-9 Phase-A isolation (+ demo-client-a/-b fixture)`

#### A.2 Bootstrap demo-client directory tree

**File to create:** `tools/bootstrap-demo-clients.sh`

**Purpose:** idempotent creation of `clients/demo-client-a/swarm/wiki/{concepts,sources,operations,meta,graph,index.md,log.md}` and same for `demo-client-b`. Must be re-runnable; if files exist, leave alone.

**Skeleton (executor writes full, under 60 LoC):**

```bash
#!/usr/bin/env bash
# tools/bootstrap-demo-clients.sh — idempotent demo-client holon scaffolding.
# Creates clients/<slug>/swarm/wiki/ tree + seed index.md + empty log.md.
# Used by UC-ISOLATION-DEMO test fixture. NOT for production clients.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

for client in demo-client-a demo-client-b; do
  base="clients/${client}/swarm/wiki"
  for subdir in concepts sources operations meta graph; do
    mkdir -p "${base}/${subdir}"
  done
  if [[ ! -f "${base}/index.md" ]]; then
    cat > "${base}/index.md" <<FM
---
title: "Demo client wiki index — ${client}"
type: index
layer: root
niche: meta
created: $(date +%Y-%m-%d)
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-attested
tier: tier-internal
produced_by: km-mvp-bootstrap
sources: []
related: []
binding_scope: client-${client}-isolation-demo
granularity: client:${client}
---

# Demo client wiki index (${client})

Fixture for UC-ISOLATION-DEMO. Intentionally empty.
FM
  fi
  [[ -f "${base}/log.md" ]] || printf '# Demo client log (%s)\n\n' "$client" > "${base}/log.md"
  [[ -f "${base}/graph/edges.jsonl" ]] || printf '# Demo client edges (empty fixture)\n' > "${base}/graph/edges.jsonl"
done

echo "OK: demo-client-a + demo-client-b bootstrapped at clients/"
```

Make executable: `chmod +x tools/bootstrap-demo-clients.sh`. Run it. Verify tree via `find clients/ -type f -name '*.md' | sort`.

**Commit message:** `[km-mvp] add tools/bootstrap-demo-clients.sh (idempotent demo holon scaffolding for UC-9 test fixture)`

#### A.3 Populate `swarm/wiki/graph/edges.jsonl` with ≥50 real typed edges

**Current state:** `swarm/wiki/graph/edges.jsonl` has 4 lines (all comments; empty bootstrap).

**Goal:** emit ≥50 typed edges emerging from existing wiki content across the 9 layers. This proves the graph is real, not a stub. These edges drive `/build-graph` community detection in A.7.

**Edge schema (per D3 §§3.2.1-3.2.11):**

```jsonl
{"from": "<from-path-relative-to-wiki-root>", "to": "<to-path-or-slug>", "type": "<edge-type>", "ts": "<ISO8601>", "provenance": "<task-id-or-skill>"}
```

**12-edge enum (D3):** `extends | supports | refutes | derived_from | part_of | supersedes | related_to | contradicts | depends_on | illustrates | cites | cross-tree-ref`. Plus `holon-ref` is AWAITING-APPROVAL (DO NOT emit in Phase A).

**Execution approach:** walk existing `swarm/wiki/foundations/`, `swarm/wiki/themes/`, `swarm/wiki/drafts/`, `swarm/wiki/proposals/` directories. For each page, emit:

- `extends` edges from drafts to their canonical parents (e.g., variant drafts → ROY-WIKI-V3 spec D1).
- `supports` edges from foundations to decision docs.
- `derived_from` edges from wiki/brigadier/ Level-2 entries to source cells.
- `cites` edges from each variant draft to its ≥8 Tier-1 sources.
- `part_of` edges clustering sibling pages under the same theme/niche.

**Writing mechanics:** append to `swarm/wiki/graph/edges.jsonl`, one JSONL record per line, preserving the existing 4 header-comment lines. Target: exactly ≥50 new edge records (count via `grep -cE '^\{' swarm/wiki/graph/edges.jsonl`).

**Commit message:** `[km-mvp] populate edges.jsonl with 50+ typed edges across existing wiki content (A1 §4.2 Tier-C seed)`

#### A.4 Upgrade `.claude/skills/ingest.md` for multi-source ingest

**Current state:** `ingest.md` exists (146 LoC) and resolves `${WIKI_ROOT}` per D7. It handles `raw/` paths and URLs.

**Extensions required (per A1 §4.1 six source types):**

1. **YouTube URL branch.** When input matches `youtube\.com|youtu\.be`, pipe through `yt-dlp --write-auto-subs --skip-download --sub-format vtt` → `tools/vtt-to-md.py` (write this helper; ≤30 LoC) → save to `raw/videos/YYYY-MM-DD-<slug>-transcript.md` → proceed as a normal markdown ingest. Emit `--source-type=youtube` frontmatter marker.
2. **PDF branch.** When input is `.pdf`, use `pdftotext` (poppler-utils) → `raw/papers/<slug>.md` with frontmatter `tier: tier-1`. If `pdftotext` absent, escalate (do not silently fail).
3. **Plain markdown branch.** Existing behaviour preserved.
4. **Web article branch.** WebFetch exists (existing path); add `readability`-style content extraction via `tools/fetch-and-extract.py` (new helper, ~40 LoC wrapping `WebFetch` output with regex for `<article>` / `<main>` block).
5. **Voice/audio branch.** Already handled upstream via `tools/transcribe.py` (CLAUDE.md voice-pipeline). `/ingest` accepts the transcript markdown; no new logic in skill.
6. **Telegram/inline note branch.** Accept stdin via `-` argument: `/ingest -`. Save to `raw/notes/YYYY-MM-DD-HHMMSS-stdin.md` with minimal frontmatter (`F: F2 / R: low`), then proceed.

**Per-ingest success criteria (MUST hold for each ingest):**

- 5-8 concept pages created under `${WIKI_ROOT}/concepts/<slug>.md` (no duplicates; dedup-check via `ls ${WIKI_ROOT}/concepts/<slug>.md`).
- 8-15 new edges appended to `${WIKI_ROOT}/graph/edges.jsonl`.
- 1 new row in `${WIKI_ROOT}/log.md` (prepended; append-only newest-on-top per CLAUDE.md convention).
- 1 new row in `${WIKI_ROOT}/index.md` (alphabetic sort preserved).
- Source page under `${WIKI_ROOT}/sources/<slug>.md` with frontmatter `pipeline: raw → ingested`, full `sources[]` triple.

**Failure modes (must handle):**

- URL unreachable → escalate as `peer-input-needed` with `WebFetch-failed` trigger. Do NOT silently write an empty source.
- Duplicate slug → call `/consolidate` inline to merge; never overwrite.
- OOM on long transcript → chunk at 100K-token boundaries (existing Karpathy pattern).

**Commit message:** `[km-mvp] extend /ingest skill to 6 source types (youtube/pdf/md/web/voice/stdin) per A1 §4.1`

#### A.5 Add `OFFLINE_MODE=1` to `.claude/skills/ask.md`

**Current state:** `ask.md` exists (123 LoC), resolves `${WIKI_ROOT}`, implements Q1 4-tier retrieval.

**Extension required (per A1 §4.2 Tier-D offline-first + UC-10):**

Add a Step 2.5 and Step 4-branch that activate when `OFFLINE_MODE=1` is set:

```
### Step 2.5 — Offline-first gate (UC-10)

If OFFLINE_MODE=1:
  1. Skip any LLM synthesis call (do NOT dispatch Task() with generation intent).
  2. After Tiers A/B/C produce candidate pages, assemble a STRUCTURED-EXCERPT packet:
     - Top-10 candidate pages sorted by edge-degree (most inbound edges first)
     - For each: {slug, title, niche, 2-sentence excerpt from body, frontmatter.confidence, cites=[related[]]}
     - Render as markdown table + citation list.
  3. Return the packet. Do NOT write to ${WIKI_ROOT}/comparisons/ (filing loop
     is LLM-synthesis-only; offline mode is retrieval-only).
  4. Append a log entry: "OFFLINE_MODE=1 query: '<query>' → 10 excerpts returned; zero LLM calls."

Network verification: zero outbound TCP on :443 during OFFLINE_MODE=1 execution.
This is auditable via `tcpdump -n 'tcp port 443 and host not 127.0.0.1'` run
alongside the query session. See tests/km-mvp/uc-ask-offline.sh for the probe.
```

**Acceptance:** `OFFLINE_MODE=1 /ask "<any query>"` produces a markdown response of ≤2KB containing ≥3 `[src:...]` citations and zero Task() dispatches (grep the skill invocation log).

**Commit message:** `[km-mvp] add OFFLINE_MODE=1 structured-excerpt path to /ask skill (UC-10 Phase-A architectural proof)`

#### A.6 (Optional — time-permitting only) Document ollama + Mistral-7B-Q4 stack

**File to create:** `swarm/lib/offline-llm/README.md`

**Content (write if Part A.1-A.5 leave ≥2h budget on Day 2; otherwise defer with explicit note):**

```markdown
---
title: Offline-LLM stack — ollama + Mistral-7B-Q4 (Phase-B activation)
type: infra-doc
...
---

# Offline-LLM stack

## Status: Phase-B activation (trigger = first paying client)

Documented here for reference; NOT installed in Phase-A (MVP).
Phase-A uses the OFFLINE_MODE=1 structured-excerpt path (retrieval-only).

## Default model: Mistral 7B Q4_K_M

- License: Apache 2.0 (cleanest for Mittelstand commercial)
- VRAM floor: 8GB
- Latency: 3-6s p95 for 500-token synthesis
- Source: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF

## Runtime: ollama

- Install: see ollama.ai (not scripted here; client-owned infra Phase-B).
- Model pull: `ollama pull mistral:7b-instruct-q4_K_M`
- API: `curl http://127.0.0.1:11434/api/generate -d '{...}'`

## `/ask --local-llm` path (NOT YET IMPLEMENTED)

When activated:
1. Replace the Tier-D LLM call with an HTTP POST to the local ollama endpoint.
2. All other Tier-A/B/C retrieval unchanged.
3. Network verification: only loopback TCP on :11434; zero outbound.

## Alternative: Llama 3.1-8B-Q4_K_M

- License: Llama Community (≤700M MAU compliance)
- VRAM floor: 16GB
- Pending resolution: 20-query DACH golden-set eval per Dissent D-2.
```

Commit only if written: `[km-mvp] document offline-LLM stack (ollama + Mistral-7B-Q4) as Phase-B activation reference`

#### A.7 `/consolidate --weekly` skill

**File to extend:** `.claude/skills/consolidate.md`

**Current state:** 101 LoC; handles dedup merge.

**Extension required:** add `--weekly` flag that generates `${WIKI_ROOT}/digests/<ISO-week>.md`.

**Algorithm:**

```
1. Parse ISO week number from today (date +%V).
2. Walk ${WIKI_ROOT}/log.md for entries in the last 7 calendar days.
3. Group entries by niche (6 niches per CLAUDE.md: personal/business/sales/life/tech/meta).
4. For each niche: top-5 pages ranked by |inbound_edges in past 7d|.
5. Compute emergent themes: run lightweight edge-clustering on last-7d edge subset.
   (Cluster = connected component with ≥3 nodes in the 7d subgraph.)
6. Render digest with sections:
   - "## New pages this week (by niche)"
   - "## Top-edges this week"
   - "## Emergent themes (clusters ≥3 nodes)"
   - "## Citations resolved" (count of new sources[] entries pointing to existing pages)
7. Write to ${WIKI_ROOT}/digests/<YYYY-Www>.md with frontmatter.
8. Append 1 row to ${WIKI_ROOT}/log.md: "weekly digest <Www> generated; N pages summarised."
```

**Cron-ready wiring:** the skill must accept `--dry-run` (print digest to stdout, no write) AND `--quiet` (suppress progress logs). Schedule target: Sunday 21:00 CET via operator cron; executor writes `tools/cron/consolidate-weekly.cron` as documentation, not installed.

**Empty-week handling:** if no new pages, render "no new pages this week" and still write the file (cron-idempotent).

**Commit message:** `[km-mvp] extend /consolidate with --weekly flag producing ISO-week digests per A1 §5 UC-2`

#### A.8 `/build-graph` operational

**File to verify/extend:** `.claude/skills/build-graph.md`

**Current state:** 107 LoC; skeleton exists per D8.

**Required functionality:**

- Read `${WIKI_ROOT}/graph/edges.jsonl`.
- Build an in-memory adjacency list (no networkx dependency in Phase A; pure Python dict-of-lists).
- Detect communities via simple Louvain-equivalent greedy modularity (write `tools/community-detect.py` ≤80 LoC).
- Write `${WIKI_ROOT}/graph/communities.jsonl` — one JSONL record per community: `{community_id, node_count, nodes: [slug,...], dominant_niche, top-k-concepts: [...]}`.
- Update `${WIKI_ROOT}/meta/health.md` with `community_count` + `largest_community_size` rollup.

**Invocation modes:**

- `/build-graph` (default): full rebuild.
- `/build-graph --since=<ISO-date>`: incremental — only edges added after `<date>`.
- `/build-graph --dry-run`: report community count without writing.

**Acceptance:** on Phase-A wiki (~50 edges, ~20 pages), `/build-graph` completes in <5s and produces a non-empty communities.jsonl.

**Commit message:** `[km-mvp] operationalize /build-graph with Louvain-equivalent community detection (A1 §4.2 Tier-C seed)`

#### A.9 Extend `/lint`

**File to extend:** `.claude/skills/lint.md` (197 LoC existing).

**Extensions required:**

1. **L-DANGLING-EDGE.** For each edge in edges.jsonl, verify both `from` and `to` resolve to existing files under `${WIKI_ROOT}`. Report any dangling edge with source line number.
2. **L-ORPHAN-CONCEPT.** For each `.md` under `${WIKI_ROOT}/concepts/`, check it has ≥1 inbound OR outbound edge. Orphans listed.
3. **L-MISSING-FRONTMATTER.** For each `.md` under `${WIKI_ROOT}/`, verify frontmatter parses AND contains the mandatory field set (title, type, created, pipeline, state, confidence, confidence_method, tier, produced_by, sources).
4. **L-DUPLICATE-SLUG.** Detect two `.md` files under `${WIKI_ROOT}/` with same basename in different subtrees. Flag unless intentional (e.g., per-niche symlinks).
5. **L-CROSS-CLIENT-GLOBAL.** If `WIKI_ROOT_CLIENT_ID` is set and any artefact under `${WIKI_ROOT}/global/` has `granularity: client:*`, flag as hard error.

Report written to `${WIKI_ROOT}/meta/lint-report-<YYYY-MM-DD>.md` + non-zero exit code if any hard errors.

**Commit message:** `[km-mvp] extend /lint with 5 new signals (dangling-edge, orphan-concept, missing-frontmatter, duplicate-slug, cross-client-global)`

**Part A verification (before moving to Part B):**

Run this smoke script and capture output to `swarm/tests/results/part-a-smoke-<date>.log`:

```bash
#!/usr/bin/env bash
set -euo pipefail

# A.1-A.2: config + demo dirs exist
python3 -c "import yaml; d=yaml.safe_load(open('.claude/config/wiki-roots.yaml')); assert 'clients' in d; assert 'demo-client-a' in d['clients']" && echo "A.1 ✓"
[[ -d clients/demo-client-a/swarm/wiki/concepts ]] && echo "A.2 ✓"

# A.3: ≥50 edges
count=$(grep -cE '^\{' swarm/wiki/graph/edges.jsonl)
[[ $count -ge 50 ]] && echo "A.3 ✓ ($count edges)"

# A.4-A.5: skills present with new features
grep -q 'OFFLINE_MODE' .claude/skills/ask.md && echo "A.5 ✓"
grep -q 'youtube\|yt-dlp' .claude/skills/ingest.md && echo "A.4 ✓"

# A.7: /consolidate --weekly flag
grep -q '\-\-weekly' .claude/skills/consolidate.md && echo "A.7 ✓"

# A.8: /build-graph + communities.jsonl
grep -q 'communities.jsonl' .claude/skills/build-graph.md && echo "A.8 ✓"

# A.9: lint signals
grep -q 'L-DANGLING-EDGE\|L-ORPHAN-CONCEPT' .claude/skills/lint.md && echo "A.9 ✓"

echo "Part A smoke: PASS"
```

If any line fails — fix before Part B. No exceptions.

---

### §2.B Part B — B2 Rich mini-swarm (Days 3-5)

**Anchor source:** `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md` §§4-6. Read once.

**Goal of Part B:** `/project-bootstrap` + mini-swarm spawning + per-project frontmatter discipline + weekly project review operational. UC-PROJECT-CONSULTING works end-to-end.

#### B.1 Create `.claude/config/project-types.yaml`

**New file:** `.claude/config/project-types.yaml`

**Purpose:** declarative templates for 4 project types. Zero Jetix-specific hardcoding — paths, default experts, required fields are all config-driven. New project types added here, not in skill code.

**Content (full; executor writes verbatim):**

```yaml
---
# .claude/config/project-types.yaml
# Declarative templates for /project-bootstrap skill. Edited here, not in skill code.
# Schema v1.

schema_version: 1
last_modified: 2026-04-XX
managed_by: brigadier

# Every project type declares:
#   - baseline_files: always created (5 files baseline per B2)
#   - type_specific_files: created when --type=<this> selected
#   - default_experts: 2 experts for the mini-swarm (P1/P2 only)
#   - required_frontmatter_fields: /lint hard-fails if missing
#   - default_stage_gates: merged B3 mechanic (optional per --adaptive)
#   - default_kpi_targets: Hamel-binary targets for P1/P2

baseline_files:
  - _moc.md               # rich frontmatter + Cagan problem + Hamel kill-criteria
  - context.md            # current project state snapshot
  - history.md            # append-only events (newest-on-top)
  - decisions.md          # 4-part DRR entries per FPF E-9
  - open-questions.md     # pending Ruslan decisions

required_frontmatter_fields:
  # Every project _moc.md MUST have these. /lint fails on missing.
  - problem_statement     # Cagan; prose; non-empty
  - kill_criteria         # Hamel-binary; prose; non-empty
  - kpi_targets           # measurable; required on P1/P2; optional P3/P4
  - project_type          # enum: consulting | research | product | bets
  - priority              # enum: P1 | P2 | P3 | P4
  - state                 # enum: active | paused | pivoted | tombstoned | killed
  - pmbok_phase           # enum: Initiated | Planned | Executing | Monitoring | Closed
  - granularity           # jetix-internal | client:<slug>

types:
  consulting:
    type_specific_files:
      - icp.md                        # Ideal Customer Profile (per D22)
      - pipeline.md                   # lead → prospect → qualified → closed stages
      - leads/                        # directory for per-lead pages
      - offline-inference-spec.md     # per-project UC-10 spec
    default_experts:
      - mgmt-expert
      - sales-researcher
    default_stage_gates:
      SG-1: "count(leads/*.md) >= 3"
      SG-2: "contract_signed_count >= 1"
      SG-3: "count(hypothesis_refuted) >= 1"
      SG-4: "cycle_count >= 5 AND active_tasks_avg >= 5"
      SG-5: "client_revenue_recurring_eur_per_month >= 1000"
    default_kpi_targets:
      leads_per_quarter: 20
      contracts_per_quarter: 2
      mrr_eur: 5000

  research:
    type_specific_files:
      - hypotheses.md                 # Popperian falsifiable claims
      - sources.md                    # cited sources by tier
      - drafts/                       # work-in-progress artefacts
    default_experts:
      - systems-expert
      - philosophy-expert
    default_stage_gates:
      SG-rd-1: "count(hypotheses.md:supported) >= 2"
      SG-rd-2: "count(hypothesis_refuted) >= 1"
      SG-rd-3: "count(drafts/*.md) >= 1"
      SG-4: "cycle_count >= 5 AND active_tasks_avg >= 5"
    default_kpi_targets:
      hypotheses_per_cycle: 3
      papers_per_quarter: 1

  product:
    type_specific_files:
      - problem-explored.md
      - solution-hypothesis.md
      - validation.md
      - roadmap.md
    default_experts:
      - engineering-expert
      - philosophy-expert
    default_stage_gates:
      SG-p-1: "count(validation_runs) >= 3"
      SG-p-2: "release_count >= 1"
      SG-4: "cycle_count >= 5 AND active_tasks_avg >= 5"
    default_kpi_targets:
      validation_cycles: 5
      releases_per_quarter: 1

  bets:
    # Adaptive starting scaffold (B3 mechanic). 3-file minimum; extends on SG firings.
    type_specific_files: []           # empty at bootstrap; auto-spawn on SG
    default_experts:
      - investor-expert
      - philosophy-expert
    default_stage_gates:
      SG-0: "cycle_count >= 3"
      SG-1: "count(leads/*.md) >= 3"
      SG-2: "contract_signed_count >= 1 OR hypothesis_validated >= 1"
      SG-4: "cycle_count >= 5 AND active_tasks_avg >= 5"
    default_kpi_targets: {}
    adaptive: true                     # default: bets start with --adaptive

# Promotion rules (B3 merged into B2 per Ruslan Gate-2).
# When an adaptive project hits SG-4, it may be promoted to a full B2 scaffold.
promotion_rules:
  - trigger: "state=active AND SG-4=fired AND type=bets"
    action: "eligible for /project-promote <slug> to type=consulting|research|product"
  - trigger: "SG-1=fired AND type=bets"
    action: "auto-spawn leads/ + pipeline.md (template: consulting)"
```

**Commit message:** `[km-mvp] add project-types.yaml declarative templates (4 types + stage-gates + promotion rules)`

#### B.2 Author `.claude/skills/project-bootstrap.md`

**New skill file:** `.claude/skills/project-bootstrap.md`

**Invocation:**
```
/project-bootstrap <slug> <priority> --type=<consulting|research|product|bets> [--client=<client-id>] [--adaptive]
```

**Behaviour:**

1. Validate `<slug>` kebab-case + unique under target operations dir (reject if exists).
2. Validate `<priority>` ∈ {P1,P2,P3,P4}; `<type>` ∈ project-types.yaml enum; `<client-id>` ∈ wiki-roots.yaml.clients (if passed).
3. Resolve target directory:
   - No `--client`: `swarm/wiki/operations/<slug>/`
   - `--client=<id>`: `clients/<id>/swarm/wiki/operations/<slug>/`
4. Load `project-types.yaml` → pull baseline_files + type_specific_files + required_frontmatter_fields + default_experts + default_stage_gates + default_kpi_targets.
5. Prompt interactively for required frontmatter fields:
   - `problem_statement:` (Cagan; non-empty)
   - `kill_criteria:` (Hamel-binary; non-empty)
   - `kpi_targets:` (required on P1/P2; optional otherwise)
6. Generate `_moc.md` with full frontmatter + body template referencing the theme-wiki (`swarm/wiki/themes/<auto-detected-theme>/README.md`).
7. Generate each of baseline_files + type_specific_files from template stubs under `swarm/wiki/_templates/project-<type>/`.
8. If `--adaptive` flag OR type=bets: skip type_specific_files, include only baseline + empty stage-gates block.
9. For P1/P2: spawn mini-swarm. Create `agents/<slug>-brigadier.md` (template from `.claude/agents/project-brigadier.md` — see B.4). Wire 2 default_experts from config.
10. Append to `${WIKI_ROOT}/log.md`: `project-bootstrap <slug> <priority> --type=<type> (+mini-swarm=<yes|no>)`.
11. Append row to `${WIKI_ROOT}/index.md` under `## Projects`.
12. Increment `${WIKI_ROOT}/meta/health.md` `project_count` + (if P1/P2) `mini_swarm_count`.
13. Commit atomically: all files in one git commit.

**Reject-on-missing-required behaviour:**

If the operator leaves `problem_statement` or `kill_criteria` empty, `/lint` on the bootstrap output will fail. The skill SHOULD fail the bootstrap atomically (roll back created files) OR leave the scaffold in place with a `state: draft-incomplete` marker — executor picks one approach consistently. Recommended: leave in place with `state: draft-incomplete`; Ruslan completes the fields later; next `/lint` run passes once complete.

**Wall-clock target:** <90 seconds of skill execution time (file writes in parallel where independent); Ruslan fills frontmatter in ≤25 min → total ≤30 min UC-5 target per B2 §4.1.

**Commit message:** `[km-mvp] add /project-bootstrap skill (4 types + mini-swarm spawn + client namespacing per B2 §4.1)`

#### B.3 Author project-scaffold templates under `swarm/wiki/_templates/`

**New files** (one template dir per project_type):

- `swarm/wiki/_templates/project-consulting/` — 9 template stubs: `_moc.md`, `context.md`, `history.md`, `decisions.md`, `open-questions.md`, `icp.md`, `pipeline.md`, `leads/.gitkeep`, `offline-inference-spec.md`.
- `swarm/wiki/_templates/project-research/` — 8 stubs: baseline 5 + `hypotheses.md`, `sources.md`, `drafts/.gitkeep`.
- `swarm/wiki/_templates/project-product/` — 9 stubs: baseline 5 + `problem-explored.md`, `solution-hypothesis.md`, `validation.md`, `roadmap.md`.
- `swarm/wiki/_templates/project-bets/` — 5 stubs (baseline only; minimal adaptive start).

**Template structure — `_moc.md` stub (common across types, with type-specific frontmatter markers):**

```markdown
---
title: "{{PROJECT_TITLE}}"
type: topic
layer: 6
niche: "{{AUTO_NICHE}}"
project_type: "{{PROJECT_TYPE}}"
priority: "{{PRIORITY}}"
state: active
pmbok_phase: Initiated
problem_statement: |
  {{FILL_IN — Cagan: describe the problem being solved in terms customer understands.
  One paragraph. Non-empty required.}}
kill_criteria: |
  {{FILL_IN — Hamel-binary: specific measurable condition that ends the project.
  Example: "if no signed contract after 12 weeks of outreach, kill."}}
kpi_targets:
  {{FILL_IN_FOR_P1_P2 — e.g., leads_per_quarter: 20, mrr_eur: 5000}}
stage_gates:
  {{FROM_PROJECT_TYPES_YAML — copied from project-types.yaml.types.<type>.default_stage_gates}}
granularity: "{{GRANULARITY}}"
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.{{PROJECT_TYPE}}"}
related:
  - "swarm/wiki/themes/{{AUTO_THEME}}/README.md"
binding_scope: "project-{{SLUG}}"
---

# {{PROJECT_TITLE}} — Map of Content

## Problem
{{FROM_FRONTMATTER.problem_statement}}

## Kill criteria
{{FROM_FRONTMATTER.kill_criteria}}

## Current focus
{{FILL_IN — 2-3 sentences.}}

## KPIs
{{FROM_FRONTMATTER.kpi_targets}}

## Stage gates declared
{{FROM_FRONTMATTER.stage_gates}}

## Related themes
- [[{{AUTO_THEME}}]]

## Active leads / hypotheses / validations
<!-- Populated as type_specific_files accumulate. -->
```

**Commit message:** `[km-mvp] add 4 project-scaffold template dirs under swarm/wiki/_templates/project-<type>/`

#### B.4 Author `.claude/agents/project-brigadier.md`

**New agent file:** `.claude/agents/project-brigadier.md` (template; instantiated per-project by `/project-bootstrap`).

**Purpose:** mini-swarm coordinator scoped to a single project's `operations/<slug>/` subtree. Derives from canonical brigadier but with tighter budget + narrower scope.

**Structure (derived from `.claude/agents/brigadier.md` with deltas):**

```markdown
---
name: project-brigadier
description: |
  Mini-swarm orchestrator for a single Jetix project. Scoped to operations/<slug>/
  subtree (or clients/<client>/.../operations/<slug>/ when per-client). Dispatches 2
  default experts from project-types.yaml. Budget: ≤7 active tasks (vs canonical
  brigadier's ≤20; no attention competition). Instantiated per-project by
  /project-bootstrap; per-project manifest at agents/<slug>-brigadier.md.
model: opus
tools: [Read, Write, Edit, Bash, Grep, Glob, Task]
granularity: project-scoped
owner: ruslan
created: {{TODAY}}
primary_alpha: task
secondary_alphas: [cycle, artefact]
domains: [project-task-decomposition, project-mini-swarm-dispatch, project-integration]
active_task_limit: 7                  # vs canonical brigadier's 20
scope_subtree: "operations/{{SLUG}}/" # hard write-scope
default_experts: {{FROM_PROJECT_TYPES_YAML}}
sole_writer_of: "operations/{{SLUG}}/"
---

# Project-brigadier — {{SLUG}}

## §1 Scope

- **Scope:** `operations/{{SLUG}}/` subtree only. May READ anything under ${WIKI_ROOT}; may WRITE only within scope.
- **Budget:** ≤7 active tasks at any time. Hard ratchet via meta/health.md.
- **Escalation to canonical brigadier:** cross-project promotion; method change; contradiction with canonical foundations; budget overrun.

## §2 Responsibilities

Every cycle for this project:
1. Read `operations/{{SLUG}}/_moc.md` + `history.md` + `open-questions.md`.
2. Decompose next task per canonical brigadier §3 (Decompose-or-Chat gate).
3. Dispatch 1-2 of default_experts via Task(); integrate returns per canonical §5.
4. Append to `history.md` (append-only; newest-on-top).
5. Write 4-part DRR entries to `decisions.md`.
6. Run `/lint --project={{SLUG}}` before weekly digest.

## §3 Mini-swarm dispatch

- Two default experts per project_type (sourced from project-types.yaml):
  {{LIST_DEFAULT_EXPERTS}}
- On-demand experts: escalate `peer-input-needed` to canonical brigadier.

## §4 Strategies memory (Level-1 per W-5)

- Personal memory: `agents/{{SLUG}}-brigadier/strategies.md` (scaffold at bootstrap).
- Promotion to `swarm/wiki/global/compound-rules/` only after α-3 validated
  (≥10 uses + 3:1 ✓/✗) + canonical brigadier attestation.

## §5 Stage-gate interaction (B3 merged into B2)

- Read _moc.md stage_gates: declarations.
- When /lint --check-stage-gates fires an SG:
  1. Verify scaffold extension per project-types.yaml.promotion_rules.
  2. Execute auto-spawn (or HITL-gate if configured).
  3. Append to history.md: "SG-<N> fired at <ts>; spawned <paths>."
  4. Notify canonical brigadier via escalation.

## §6 Output contract

- Commit frequency: per-logical-unit (not per-file).
- Commit message: `[<slug>] <verb> <what>`.
- Never --amend, --no-verify, force-push.

## §7 Import stubs (shared-protocols)

Import by reference:
- §1 Wiki-write protocol
- §2 Provenance gate
- §3 Structured Task() return schema
- §4 HITL escalation rules
- §5 Tool-permission self-check
- §6 Cross-cell-reference protocol
- §7 mode: writing-support
- §8 Verb dictionary
- §9 Max-subscription + retrieval stack

All apply verbatim within project-brigadier scope.
```

**Commit message:** `[km-mvp] add .claude/agents/project-brigadier.md template (instantiated per-project; ≤7 active tasks, scoped write)`

#### B.5 Create `agents/<project-slug>-brigadier/strategies.md` scaffold on bootstrap

**Behaviour of `/project-bootstrap`:** at the end of successful P1/P2 bootstrap, create `agents/<slug>-brigadier/strategies.md` as an empty scaffold:

```markdown
---
title: "Strategies — {{SLUG}}-brigadier"
type: personal-memory
layer: 2
owner: "{{SLUG}}-brigadier"
created: "{{TODAY}}"
last_modified: "{{TODAY}}"
pipeline: drafted
state: active
confidence: medium
confidence_method: scaffold
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related: []
binding_scope: "project-{{SLUG}}"
---

# Strategies — {{SLUG}}-brigadier

<!-- W-5 Level-1 personal memory. 4-part DRR entries appended here by
     project-brigadier. Promotion to Level-2 (wiki/meta/agent-improvements/)
     requires canonical brigadier attestation + ≥10 uses + 3:1 ✓/✗. -->

## Cycle-1 (placeholder)

No entries yet. First entry appended after first integration.
```

#### B.6 Author `.claude/skills/project-review.md`

**New skill:** `.claude/skills/project-review.md`

**Invocation:** `/project-review <slug>` — produces weekly digest per project.

**Scheduling intent:** Monday 08:00 CET cron; executor documents in `tools/cron/project-review-weekly.cron`.

**Output format** (written to `${WIKI_ROOT}/operations/<slug>/weekly-<ISO-week>.md`):

```markdown
---
title: "Weekly review — <slug> — <YYYY-Www>"
type: weekly-digest
project: <slug>
...
---

# Weekly review — <slug>

## Light signal: 🟢 | 🟡 | 🔴
{{RULE: 🟢 if progress since last week AND no open-blockers with age > 7d;
        🟡 if some blockers age 3-7d OR flat progress;
        🔴 if blocker age > 7d OR state=paused > 14d OR kill-criteria approaching.}}

## Progress since last review
- <extracted from history.md entries in last 7d>

## Open blockers
- <from open-questions.md with age annotation>

## Stage-gate status
- SG-1: <fired | pending — predicate=... current value=...>
- SG-2: ...

## KPI vs targets
{{from _moc.md kpi_targets vs current values in context.md or pipeline.md}}

## Next cycle
{{top 3 active tasks; from project-brigadier active-task list}}
```

**Commit message:** `[km-mvp] add /project-review skill for weekly per-project digest (Mon 08:00 CET cron)`

#### B.7 Author `.claude/skills/project-archive.md`

**New skill:** `.claude/skills/project-archive.md`

**Invocation:** `/project-archive <slug> --reason=<killed|closed|pivoted>`

**Behaviour:**
1. Validate slug exists under current `${WIKI_ROOT}/operations/`.
2. Move (git mv) `operations/<slug>/` → `operations/_archived/<slug>/`.
3. Update `_moc.md` frontmatter: `state: <reason>`, append `archived_at: <ISO8601>`, `archived_reason: <reason>`.
4. Append to `history.md`: `project archived — reason: <reason>.`
5. If mini-swarm exists: tear down (`rm -rf agents/<slug>-brigadier/`; git rm).
6. Decrement `meta/health.md` project_count + mini_swarm_count.
7. Append `${WIKI_ROOT}/log.md` row.
8. Commit: `[km-mvp] archive project <slug> (reason: <reason>)`.

**Reversibility:** `_archived/` retains full history; re-activating requires manual `/project-unarchive` (Phase-B work; not in this MVP).

#### B.8 Extend `/lint` for required-frontmatter enforcement

Add to `/lint` a signal `L-PROJECT-MISSING-REQUIRED-FRONTMATTER`:

- For each `_moc.md` under `${WIKI_ROOT}/operations/` (and `clients/*/swarm/wiki/operations/`):
  - Verify every field in `project-types.yaml.required_frontmatter_fields` is present AND non-empty.
  - Hard-fail on missing `problem_statement` or `kill_criteria`.
  - Hard-fail on missing `kpi_targets` for P1/P2 projects.
  - Warn on missing `pmbok_phase`.

**Commit message:** `[km-mvp] extend /lint with L-PROJECT-MISSING-REQUIRED-FRONTMATTER (enforces Cagan+Hamel discipline)`

**Part B verification smoke** (capture to `swarm/tests/results/part-b-smoke-<date>.log`):

```bash
#!/usr/bin/env bash
set -euo pipefail

# B.1: project-types.yaml present and valid
python3 -c "import yaml; d=yaml.safe_load(open('.claude/config/project-types.yaml')); assert 'types' in d; assert set(d['types']) >= {'consulting','research','product','bets'}" && echo "B.1 ✓"

# B.2: /project-bootstrap skill
[[ -f .claude/skills/project-bootstrap.md ]] && grep -q 'project-types.yaml' .claude/skills/project-bootstrap.md && echo "B.2 ✓"

# B.3: templates exist
for t in consulting research product bets; do
  [[ -f swarm/wiki/_templates/project-$t/_moc.md ]] || { echo "B.3 FAIL ($t template)"; exit 1; }
done
echo "B.3 ✓"

# B.4: project-brigadier template
[[ -f .claude/agents/project-brigadier.md ]] && echo "B.4 ✓"

# B.6-B.7: review + archive skills
[[ -f .claude/skills/project-review.md ]] && [[ -f .claude/skills/project-archive.md ]] && echo "B.6/B.7 ✓"

# B.8: lint extension
grep -q 'L-PROJECT-MISSING-REQUIRED-FRONTMATTER' .claude/skills/lint.md && echo "B.8 ✓"

echo "Part B smoke: PASS"
```

---

### §2.C Part C — B3 stage-gate mechanic merged into B2 (Day 5)

**Anchor source:** `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md` §4.2-§4.9.

**Goal of Part C:** stage-gate predicates evaluate daily; fire auto-spawn; philosophy-critic gates new predicates; reversibility via `/project-de-morph`; promotion via `/project-promote`. The B3 mechanic is FOLDED into B2 — no standalone B3 skill.

#### C.1 `_moc.md` frontmatter supports `stage_gates:` block

Verify the `_moc.md` template from B.3 already carries `stage_gates:` section. Also verify it supports per-SG status annotations (when SG fires):

```yaml
stage_gates:
  SG-1:
    predicate: "count(leads/*.md) >= 3"
    state: pending           # pending | fired
    declared_at: 2026-04-25
    fired_at: null           # set when fires
    spawned_paths: []        # filled on fire
  SG-2: ...
```

#### C.2 `/lint --check-stage-gates` daily cron

Extend `.claude/skills/lint.md` with `--check-stage-gates` flag:

Algorithm:
1. For each `_moc.md` under `${WIKI_ROOT}/operations/`:
   - Load `stage_gates:` block.
   - For each SG where `state: pending`:
     - Evaluate the predicate DSL against current scaffold + history.
     - If TRUE: call auto-spawn logic (C.3), update state to `fired`, set `fired_at`, populate `spawned_paths`.
     - If FALSE: do nothing.
2. Log fires to `${WIKI_ROOT}/meta/stage-gate-fires-<YYYY-MM-DD>.md`.
3. Surface in next weekly digest.

**Predicate DSL (simple, deterministic, offline):**

- `count(<glob>) >= N` — file-count check
- `count(<glob>:<marker>) >= N` — count files containing marker (grep -c)
- `<metric> >= <value>` — read from `context.md` or `pipeline.md` key (YAML front + body parse)
- `cycle_count >= N AND active_tasks_avg >= M` — compound predicates via `AND` / `OR`

Write `tools/stage-gate-eval.py` (~120 LoC) implementing the DSL. Test with `swarm/tests/fixtures/stage-gates/` containing mocked scaffolds.

**Commit message:** `[km-mvp] add /lint --check-stage-gates with Hamel-binary predicate DSL evaluator`

#### C.3 Auto-spawn protocol

When SG fires per `project-types.yaml.promotion_rules`:

Example (bets project, SG-1 fires):
1. Load the `action` field: `"auto-spawn leads/ + pipeline.md (template: consulting)"`.
2. Copy `swarm/wiki/_templates/project-consulting/leads/.gitkeep` + `pipeline.md` into the project subtree.
3. Append `history.md`: `SG-1 fired; spawned leads/ + pipeline.md (via project-types.yaml promotion_rules).`
4. Update `_moc.md` stage_gates entry with `spawned_paths: [leads/, pipeline.md]`.
5. Commit: `[<slug>] SG-1 fired — auto-spawn leads/ + pipeline.md (per bets promotion rule)`.

If auto-spawn would overwrite existing files: STOP, escalate `peer-input-needed`.

#### C.4 `/project-de-morph` reversibility skill

**New skill:** `.claude/skills/project-de-morph.md`

**Invocation:** `/project-de-morph <slug> --rollback-to=<SG-N>`

**Behaviour:**
1. Load `<slug>`'s `_moc.md` stage_gates.
2. For every SG with `stage_gate_number > N` and `state: fired`:
   - Read `spawned_paths` list.
   - `git rm -rf` each spawned path (use git mv to `_archived/` if path contains user-written content; pure scaffolds are safe to rm).
   - Set SG state back to `pending`; clear `fired_at` and `spawned_paths`.
3. Append `history.md`: `de-morph: rolled back to SG-<N>; removed <paths>.`
4. Commit atomically: `[<slug>] de-morph rollback to SG-<N>`.

**Guard:** `/project-de-morph` requires HITL ack if any spawned path contains ≥50 lines of user-authored content (i.e., not pure scaffold). Escalate via AWAITING-APPROVAL packet.

**Commit message:** `[km-mvp] add /project-de-morph skill (SG reversibility; B3 mechanic per variant §4.9)`

#### C.5 `/project-promote` skill

**New skill:** `.claude/skills/project-promote.md`

**Invocation:** `/project-promote <slug>` (one-line command Ruslan ack'd at Gate-2)

**Behaviour:**
1. Validate slug exists AND current `project_type: bets` AND `SG-4: fired`.
2. Prompt operator for target type (consulting | research | product).
3. Apply diff: add type_specific_files from target template; update `project_type:` in `_moc.md`; re-evaluate `required_frontmatter_fields` (may prompt for new fields).
4. Append `history.md`: `promoted from bets → <target-type> at <ts>.`
5. Commit: `[<slug>] promote bets → <target-type> (SG-4 fired; criteria met)`.

**Guard:** promotion is one-way (no demote). If promotion wrong, `/project-archive` + re-bootstrap.

**Commit message:** `[km-mvp] add /project-promote skill (B3 → B2 promotion at SG-4 + mini-swarm criteria)`

#### C.6 philosophy-expert gate on new SG predicates

**Policy (not a separate skill; enforced by `/project-bootstrap` and any custom SG addition):**

When a new SG predicate is declared (default from project-types.yaml OR custom in `_moc.md`):
1. Parse predicate via DSL.
2. Invoke philosophy-expert critic mode via `Task(philosophy-expert × critic, mode: sg-validation, predicate: <raw>, context: <project>)`.
3. Expect return `{verdict: hamel-binary | ambiguous | non-binary, rationale: <text>}`.
4. If `non-binary` or `ambiguous`: reject predicate; require re-phrase.
5. Log validation result alongside SG declaration in `_moc.md` (field: `sg_validation: {...}`).

This prevents predicate drift (per variant-B3 §4.2 + Ruslan's Gate-2 concern about B3 predicate rigor).

**Commit message:** `[km-mvp] require philosophy-expert critic validation on every new SG predicate (Hamel-binary gate per Gate-2)`

---

### §2.D Part D — Company-as-code / Knowledge-as-code enforcement (cross-cutting, all days)

**This is not a separate Part-day** — it's the bar every commit in Parts A/B/C/E must clear. Checklist applied continuously:

#### D.1 Structured commit messages

Every commit message follows `[<area>] <verb> <what> (<why>)`:
- `<area>` ∈ {km-mvp, ingest, ask, lint, consolidate, build-graph, project-bootstrap, project-review, project-de-morph, project-promote, project-archive, agents, config, templates, tests, tools, docs}.
- `<verb>` ∈ {add, extend, fix, refactor, wire, document, remove, archive}.
- `<what>` = concrete file or subsystem.
- `<why>` = one-line rationale referencing Gate-2, a variant-draft section, or a UC.

Example: `[km-mvp] extend /ingest skill to 6 source types (A1 §4.1: UC-1 multi-source ingest)`.

**Enforcement:** executor self-audits before each commit. If unsure, look at `git log --oneline | head -20` style examples.

#### D.2 Declarative config discipline

- `.claude/config/*.yaml` are the only source-of-truth for structural parameters.
- No hardcoded paths in skill code. Every skill opens config via the existing wiki-roots resolution pattern.
- New config files must include `schema_version:`, `last_modified:`, `managed_by:` keys.

#### D.3 Clean git provenance

- `git log --follow <file>` must produce a clean linear provenance for any new file.
- No force-push. No `--amend` after push. No `--no-verify`. No secret rewrites.
- If a commit is wrong, make a new commit with `revert` or a corrective edit. Never rewrite history.

#### D.4 `/company-status` skill

**New skill:** `.claude/skills/company-status.md`

**Purpose:** produce compact git-based system snapshot — all from filesystem + git, zero external deps.

**Output format:**

```
Jetix company-status — <YYYY-MM-DD HH:MM CET>

Active projects: <N> (P1=<a> P2=<b> P3=<c> P4=<d>)
Active clients:  <N> (<slug-list>)
Mini-swarms:     <N> active
Open SGs:        <N> (pending) / <M> (fired this week)

Ingest activity (last 7d):
  - <N> pages ingested (<breakdown-by-source-type>)
  - <M> new edges
  - <K> new concepts

Wiki health:
  - pages total:        <N>
  - edges total:        <N>
  - communities:        <N>
  - dangling edges:     <N>
  - orphan concepts:    <N>
  - lint errors:        <N> (hard) / <M> (warnings)

Git:
  - branch:             <name>
  - commits last 7d:    <N>
  - unpushed:           <N>
```

Derive every field from local reads (`git log`, file walks, JSONL counts, meta/health.md) — zero network.

**Commit message:** `[km-mvp] add /company-status skill (git-native system snapshot, zero external deps)`

#### D.5 `/knowledge-diff` skill

**New skill:** `.claude/skills/knowledge-diff.md`

**Invocation:** `/knowledge-diff <from-date> <to-date>`

**Behaviour:**
1. `git log --since=<from> --until=<to> -- swarm/wiki/concepts/ swarm/wiki/foundations/ swarm/wiki/themes/` → list of commits touching wiki.
2. For each: `git show --name-status <sha>` → classify Added/Modified/Deleted.
3. Aggregate by niche, by type.
4. Output markdown report: "Between <from> and <to>: +N concepts, ~M concepts, -K concepts; top-5 by edit volume; delta in edges.jsonl."

**Commit message:** `[km-mvp] add /knowledge-diff skill (git-log based delta between two dates)`

#### D.6 Update `CLAUDE.md` post-materialization

At the end of Part E, extend `CLAUDE.md` with a new section:

```markdown
## KM MVP (2026-04-<XX>) — what changed

- New skills: /project-bootstrap, /project-review, /project-archive, /project-de-morph,
  /project-promote, /company-status, /knowledge-diff
- Extended skills: /ingest (6 source types), /ask (OFFLINE_MODE=1),
  /consolidate (--weekly), /build-graph (communities.jsonl), /lint (5 new signals + stage-gates)
- New config: .claude/config/project-types.yaml (4 project types declarative)
- New agent template: .claude/agents/project-brigadier.md (instantiated per-P1/P2 project)
- Wiki-roots.yaml extended: clients: stanza for UC-9 Phase-A isolation
- Templates added: swarm/wiki/_templates/project-<type>/ (4 types)
- Company-as-code principle: every KB change = structured git commit; config-driven;
  git-native rollback via git revert.

## KM MVP quick ops

- Bootstrap new project: /project-bootstrap <slug> <P1|P2|P3|P4> --type=<consulting|research|product|bets> [--client=<id>] [--adaptive]
- Weekly review: /project-review <slug> OR /company-status (aggregate)
- Offline-first query: OFFLINE_MODE=1 /ask "<query>"
- Bet promotion: /project-promote <slug> (after SG-4 fired)
- Rollback stage gates: /project-de-morph <slug> --rollback-to=SG-<N>
```

**Commit message:** `[km-mvp] update CLAUDE.md with KM MVP skills + conventions`

---

### §2.E Part E — Apply MVP to real Jetix work (Days 6-7)

**Goal of Part E:** prove the new infrastructure on REAL Jetix content. Two projects bootstrapped, one end-to-end ingest+ask demo, weekly digest generated. The `quick-money` bootstrap is the seed for the €50K Q2 2026 trajectory (JETIX-PLAN D3).

#### E.1 Bootstrap `quick-money` project (P1, type=consulting)

Invocation:
```
unset ANTHROPIC_API_KEY OPENAI_API_KEY GROQ_API_KEY  # Max-sub discipline
/project-bootstrap quick-money P1 --type=consulting
```

**Fill in `_moc.md` frontmatter (executor pulls from authoritative Jetix sources):**

- `problem_statement:` derive from `decisions/JETIX-PLAN.md §3.1 Phase-1-objectives`. One-paragraph Cagan frame: "Mittelstand DACH companies (50-500 employees) are AI-curious but paralyzed by privacy/compliance/vendor-lock-in fears. They need local-first, client-private AI consulting from an operator who speaks their language and delivers working systems — not slideware — within 6-12 weeks. Jetix provides consulting + productized playbook templates so each engagement converts trapped internal knowledge into operational AI leverage."
- `kill_criteria:` Hamel-binary: "if no signed contract after 12 weeks of ICP-targeted outreach to 50 qualified prospects, re-decompose the offer — or kill. Specifically: no contract signed by 2026-07-24."
- `kpi_targets:` per D3: `{leads_per_quarter: 20, discovery_calls_per_quarter: 10, contracts_per_quarter: 2, mrr_eur_target_q2_2026: 15000, cumulative_revenue_q2_2026_eur: 50000}`.
- `granularity: jetix-internal` (quick-money is Jetix's own bootstrap engagement, not per-client yet).

#### E.2 Populate `quick-money/icp.md` from JETIX-VISION D22

Pull verbatim from `decisions/JETIX-VISION.md` §7.1 (11 archetypes) + §7.2 (5 ICP criteria). Structure:

```markdown
---
title: "Quick-money ICP"
type: icp
project: quick-money
source: "decisions/JETIX-VISION.md §§7.1-7.2"
...
---

# Quick-money ICP — Ideal Customer Profile

## 5 qualitative criteria (D22)

1. **Startupper mindset** — builder's instinct; proactive; creates rather than consumes.
2. **Предпринимательский азарт** — entrepreneurial game-drive; skill-based risk enjoyment.
3. **Stable** — reliable, disciplined, non-volatile; survives long trajectories without burn-out.
4. **Adequate** — common sense; no delusion; anti-bullshit detector on self first.
5. **Upward-direction** — active self-development + environment-development (vs degradation).

## 11 archetypes (subset relevant to quick-money consulting Phase-1)

[Cite the ones most likely to buy consulting in Phase 1:]
1. Предприниматели / бизнесмены — hungry, action-driven, seek AI leverage for scale.
2. Ресёрчеры — depth-seekers, want structured thinking + AI enhancement.
3. Инженеры — system builders, productivity multiplier seekers.
4. Инвесторы — pattern seekers, resource-allocation frameworks.
6. Продавцы — conversion specialists, AI sales infrastructure.
7. Менеджеры / коммуникаторы — orchestrators, process effectiveness.
11. Блогеры — specialist content creators (primary Phase-1 overlap with producer center).

## Market scope (per JETIX-PLAN D3 §3.7)

- EN — primary sales market (English-speaking infobiz, specialist blogers).
- DACH — secondary: DE (GmbH legal home, NOT primary Phase-1 sales), AT, CH.
- Language sequence: EN primary messaging; DE follows for DACH leads.

## Hosting path (per STRATEGIC-INSIGHT §5 × investor-optimizer Δ-H3)

- **Path B default for first 1-3 clients:** €3K onboarding + €15K/yr recurring
  → 70.7% GM year-1 (clears 70% floor).
- Path C (hybrid) deferred to post-contractor-#1 (54% GM fails Phase-A floor).
- Path A (Jetix-hosted VPS) knife-edge; used for low-touch SMB only.

## Offer shape (Phase-1 anchor)

4-pack: consulting session + 10 playbook templates + light community access
+ concrete help on one prioritized deliverable. €150/hour baseline; scale via
productization not hourly rate. Phase-1 offer mirrors JETIX-PLAN §3.3.

## Upward-direction filter

All 11 archetypes × UPWARD-DIRECTION ONLY. Topic secondary; direction primary.
```

Commit: `[quick-money] populate icp.md from JETIX-VISION D22 (5 criteria + 11 archetypes)`.

#### E.3 Spawn mini-swarm for `quick-money`

Verify `/project-bootstrap` created:
- `.claude/agents/quick-money-brigadier.md` from project-brigadier template.
- `agents/quick-money-brigadier/strategies.md` scaffold.
- Mini-swarm experts: mgmt-expert + sales-researcher (per project-types.yaml consulting default).

Test the mini-swarm is reachable:
```bash
# smoke test
grep -l 'quick-money' .claude/agents/quick-money-brigadier.md && echo "mini-swarm ✓"
```

#### E.4 End-to-end ingest+ask demo

1. Pick a real reference article on Mittelstand AI. Executor may fetch via:
   ```
   /ingest https://www.bitkom.org/Bitkom/Publikationen/... (or similar reference article)
   ```
   OR if no URL fetched, use a local markdown file under `raw/articles/` as the seed.

2. Verify ingest output: 5-8 new concept pages under `swarm/wiki/concepts/`; 8-15 new edges; log row; index row.

3. Fire the ask:
   ```
   /ask "как применить [concept-extracted-above] к quick-money ICP"
   ```
   Expect synthesized answer with ≥3 `[src:...]` citations and 1 comparison written to `swarm/wiki/comparisons/<YYYY-MM-DD>-<slug>.md`.

4. Write the insight to `quick-money/history.md`:
   ```markdown
   ## 2026-04-<XX> — first end-to-end demo
   Ingested: <article-title> (<source>).
   Queried: "как применить <concept> к quick-money ICP".
   Answer cited: <3 pages>.
   Key insight: <1-2 sentences actionable for Mittelstand outreach>.
   ```

Commit: `[quick-money] first end-to-end ingest+ask demo — <concept-slug> insight logged to history.md`.

#### E.5 Bootstrap `levenchuk-deep-dive` research project (adaptive)

Invocation:
```
/project-bootstrap levenchuk-deep-dive P3 --type=research --adaptive
```

Fill in:
- `problem_statement:` "Extract operational leverage from Левенчук ШСМ + FPF E-1..E-18 methodology into reusable systems-thinking playbooks Jetix can cite in consulting engagements + publish as open research per D24."
- `kill_criteria:` "If after 3 cycles no hypothesis is validated AND no playbook draft produced, pause (not kill — research-tier has longer tolerance)."
- `kpi_targets:` optional (P3); leave empty or set `{playbooks_drafted: 2, hypotheses_validated: 3}`.
- Default experts: systems-expert + philosophy-expert.
- Stage-gates: 3-file minimal start (baseline only); stage-gates from research template.

Verify adaptive bootstrap: 3 files (`_moc.md`, `history.md`, `open-questions.md`) + NO type_specific_files yet. SG declarations present in `_moc.md`.

Commit: `[levenchuk-deep-dive] bootstrap P3 research project adaptively (3-file minimal start)`.

#### E.6 First weekly digest run

Invocation:
```
/consolidate --weekly
```

Expect output at `swarm/wiki/digests/<YYYY-Www>.md` containing:
- New pages this week (by niche)
- Top-edges this week
- Emergent themes (clusters)
- Citations resolved

If digest is near-empty (thin wiki early on), that's OK — the skill must still produce a file with "no new pages this week" and the expected empty-state rendering.

Commit: `[km-mvp] first weekly digest generated via /consolidate --weekly (<Www>)`.

**Part E verification smoke:**

```bash
#!/usr/bin/env bash
set -euo pipefail

# E.1: quick-money exists with required frontmatter
[[ -f swarm/wiki/operations/quick-money/_moc.md ]] && echo "E.1 ✓"
grep -q '^problem_statement' swarm/wiki/operations/quick-money/_moc.md || { echo "E.1 FAIL: problem_statement missing"; exit 1; }
grep -q '^kill_criteria' swarm/wiki/operations/quick-money/_moc.md || { echo "E.1 FAIL: kill_criteria missing"; exit 1; }

# E.2: icp.md populated with D22
grep -qi 'Startupper\|archetype' swarm/wiki/operations/quick-money/icp.md && echo "E.2 ✓"

# E.3: mini-swarm present
[[ -f .claude/agents/quick-money-brigadier.md ]] && [[ -d agents/quick-money-brigadier ]] && echo "E.3 ✓"

# E.4: history.md has a demo entry
grep -q 'end-to-end demo\|insight' swarm/wiki/operations/quick-money/history.md && echo "E.4 ✓"

# E.5: levenchuk-deep-dive minimal
[[ -f swarm/wiki/operations/levenchuk-deep-dive/_moc.md ]] && \
  [[ ! -f swarm/wiki/operations/levenchuk-deep-dive/hypotheses.md ]] && \
  echo "E.5 ✓ (3-file minimal start verified)"

# E.6: weekly digest exists
ls swarm/wiki/digests/*.md | head -1 && echo "E.6 ✓"

echo "Part E smoke: PASS"
```

---

### §2.F Part F — Verification + Stage-Gated Pause

**Goal of Part F:** produce a comprehensive verification matrix covering every Part A-E deliverable + integration tests covering UC-1..UC-10 (per §3 below). Write the AWAITING-APPROVAL packet. Halt for Ruslan review. No autonomous progression to Part G.

**Master verification script:** `swarm/tests/km-mvp-verify.sh`

```bash
#!/usr/bin/env bash
# swarm/tests/km-mvp-verify.sh — master verification matrix.
# Runs every Part A-E smoke + 10 UC integration probes.
# Outputs: swarm/tests/results/verify-<date>.log + exit 0 on full pass.

set -euo pipefail

# Max-sub discipline guard
for var in ANTHROPIC_API_KEY OPENAI_API_KEY GROQ_API_KEY COHERE_API_KEY; do
  if [[ -n "${!var:-}" ]]; then
    echo "FAIL: $var is set — violates Max-sub discipline"
    exit 1
  fi
done

bash swarm/tests/part-a-smoke.sh
bash swarm/tests/part-b-smoke.sh
bash swarm/tests/part-c-smoke.sh
bash swarm/tests/part-e-smoke.sh

# UC integration probes (§3 below)
bash swarm/tests/uc-ingest-1.sh
bash swarm/tests/uc-ask-1.sh
bash swarm/tests/uc-ask-offline.sh
bash swarm/tests/uc-digest.sh
bash swarm/tests/uc-project-consulting.sh
bash swarm/tests/uc-project-adaptive.sh
bash swarm/tests/uc-reverse.sh
bash swarm/tests/uc-review.sh
bash swarm/tests/uc-isolation-demo.sh
bash swarm/tests/uc-company-status.sh

echo "========================================"
echo "KM MVP verify: ALL PASS"
echo "========================================"
```

Per-UC probe files written under `swarm/tests/` (see §3 for individual specs).

**AWAITING-APPROVAL packet:** `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md`

Template:

```markdown
---
title: "AWAITING-APPROVAL — KM Materialization MVP — 2026-04-<XX>"
type: gate
gate_type: materialization-mvp-verification
escalator: brigadier
escalated_at: <ISO8601>
task_id: T-km-materialization-mvp-2026-04-<XX>
cycle_id: cyc-km-materialization-2026-04-<XX>
deadline: "review within 48h"
state: open
---

# KM Materialization MVP — Gate for Part G authorization

## Context

7-day sprint completed Parts A-E per execution prompt
`prompts/km-materialization-mvp-execution-2026-04-24.md`. All Part A-E
smoke tests + 10 UC integration probes PASS.

Summary of what built:
- Part A (A1 substrate): <N> files; <M> LoC; wiki-roots.yaml clients:
  stanza + 6 skills extended + 50+ edges + /ingest multi-source
  + /ask offline + /consolidate weekly + /build-graph communities
  + /lint 5 signals.
- Part B (B2 mini-swarm): project-types.yaml + /project-bootstrap 4 types
  + project-brigadier template + 4 scaffold template dirs + /project-review
  + /project-archive + /lint required-frontmatter.
- Part C (B3 merged): stage_gates in _moc.md + /lint --check-stage-gates
  + DSL evaluator + /project-de-morph + /project-promote + philosophy gate.
- Part D (company-as-code): structured commits + /company-status
  + /knowledge-diff + CLAUDE.md updated.
- Part E (real work): quick-money P1 bootstrap + icp.md from D22
  + mini-swarm live + end-to-end demo + levenchuk-deep-dive adaptive
  + first weekly digest.

Commit count this sprint: <N> (target was 15-25).
LoC added: <M> across <K> new files + <L> modified.

## Verification matrix

[Attach link to verify-<date>.log with all ✓ lines.]

Every UC from §3 has a per-UC probe file; all exit 0.

## Pen-test results (UC-9 + UC-10)

- UC-ISOLATION-DEMO: attempted cross-client read from demo-client-a context
  into demo-client-b — denied at skill-layer (wiki-roots.yaml resolution
  + Phase-A policy check). Phase-B OS-level strengthening deferred to A2
  activation.
- UC-ASK-OFFLINE: OFFLINE_MODE=1 session verified via tcpdump probe; zero
  outbound TCP on :443 during 10-query run.

## Options for Ruslan

(a) ACCEPT — authorize Part G report writing. Executor proceeds to:
    (1) write decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md (≥3000 words).
    (2) compound step: append 4-part DRR rules to agents/brigadier/strategies.md.
    (3) cycle-archive entry + agent-improvements entries for 5 experts.
    Optional: specify focus areas in Part G report (e.g., "expand on
    adaptive bootstrap learnings" or "call out any spec ambiguities
    resolved during execution").

(b) MODIFY — request specific re-verification or scaffold changes.
    Examples:
    - "Re-run UC-ISOLATION-DEMO with additional pen-test: prompt-injection
      targeting /ask to cross client boundaries."
    - "Swap default_experts for consulting: use philosophy-expert as second
      default instead of sales-researcher."
    Executor acts on specified deltas + re-verifies + returns to gate.

(c) REJECT — pause materialization. Reason required. Executor writes
    remediation plan + re-enters after Ruslan guidance.

(d) EXPAND — request additional UC coverage before Part G.
    Examples: "Add UC-CROSS-PROJECT: promote a pattern from quick-money
    history.md to compound-rules via meta-agent sweep."

## Risk

- If Part G is skipped and cycle not archived, next sprint loses compound
  step (W-5 Level-2 promotion window).
- If verify pass is accepted but contains regression undetected by probes,
  quick-money bootstrap may inherit the bug.

## How to ack

- Reply `(a) accept` + optional focus, OR
- Edit this file's frontmatter: `state: acked`, `chosen: <letter>`, `notes: <text>`,
  OR
- Write `<this-file>-ack.md` with `{acked: true, chosen: <letter>, notes}`.
```

**Pause behaviour:** after writing this packet + pushing, the executor STOPS. No further writes until Ruslan ack detected. Check for ack every session startup; do not poll continuously.

---

### §2.G Part G — Execution Report + Compound Step (after Ruslan ack only)

**Goal of Part G:** produce `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md` (≥3000 words); compound learnings; close cycle.

#### G.1 Report structure (≥3000 words total)

Required sections with per-section word floors:

1. **§0 TL;DR** (≥100 words). 3 paragraphs: what built, what verified, what next.
2. **§1 Part-by-part summary** (≥300 words per Part A/B/C/D/E — 1500 total minimum). For each:
   - What built (files + skills list with LoC).
   - Where (paths).
   - How verified (UC list + results).
   - Adaptations (any place spec was ambiguous; how resolved).
3. **§2 Emergent insights / surprises** (≥300 words). What executor learned that ISN'T in the variant drafts or the meta-brief. Could be:
   - Predicate DSL edge cases.
   - Config-driven discipline ratifying specific patterns.
   - Unexpected coupling between Parts B and C.
   - Quality-bar friction points.
4. **§3 Quick-money first bootstrap results** (≥400 words). Detailed review of:
   - `_moc.md` problem_statement quality (Cagan fit).
   - `icp.md` how well D22 content mapped.
   - Mini-swarm first dispatch (what mgmt-expert × critic said about ICP).
   - End-to-end demo: ingest → ask → insight. What was the concept? What was the insight? Is it real or theatre?
5. **§4 Levenchuk research adaptive bootstrap results** (≥250 words). Similar review.
6. **§5 Verification matrix** (≥200 words + table). Table: UC | probe | PASS/FAIL | evidence-path.
7. **§6 Lessons for next cycle** (≥250 words). Concrete lessons feeding back into:
   - `agents/brigadier/strategies.md` (Level-1 DRR entries).
   - `swarm/wiki/meta/agent-improvements/<expert>-<date>.md` (per-expert Level-2 candidates).
8. **§7 Recommended next M-class tasks** (≥200 words). Top-3 with rationale + rough sizing. Likely candidates:
   - M3 solo-vs-matrix measurement task (HD-02 companion slot).
   - A2 trigger-check infrastructure (health.md + first-paying-client detector).
   - First client outreach kickoff (B-class, not M-class).
9. **§8 Open questions for Ruslan** (≥100 words). Anything surfaced during execution that needs his call.

#### G.2 Compound step — 4-part DRR rules to `agents/brigadier/strategies.md`

Append to `agents/brigadier/strategies.md` 4-part DRR entries per philosophy-optimizer canonical template (80 words/part minimum):

For each of: (a) decomposing a physical-materialization task into Parts A-G; (b) stage-gated commit cadence during a multi-day sprint; (c) config-first discipline avoiding skill-code hardcoding; (d) Cagan-problem + Hamel-kill-criteria enforcement via lint:

```markdown
## DRR — <rule-slug> (<YYYY-MM-DD>)

**Context (≥80w):** <when this rule applied>

**Decision (≥80w):** <what the rule prescribes>

**Alternatives considered (≥80w):** <what else was on the table and why rejected>

**Review checkpoint (≥80w):** <how to tell if this rule stops working + when to revisit>

[F: F4 / ClaimScope: <scope> / R: <high|medium> / refuted_if: <specific signal>]
```

#### G.3 Agent-improvements entries for each of 5 experts

Write `swarm/wiki/meta/agent-improvements/<expert>-2026-04-<XX>.md` (one per: engineering / mgmt / systems / philosophy / investor). Each entry ≥200 words covering what that expert's lens taught about the KM-MVP materialization. Examples:

- **engineering-expert:** clean 5-skill extension pattern; LoC discipline; config-first decomposes ambiguity.
- **mgmt-expert:** Cagan-problem-statement as hard frontmatter field — prevents scope drift; project-types.yaml as right level of abstraction.
- **systems-expert:** stage-gate predicate DSL as Ashby requisite variety; `/project-de-morph` preserving reversibility as feedback-loop safeguard.
- **philosophy-expert:** Hamel-binary predicate validation as Popperian refutability gate; 4-part DRR as compound-engineering hygiene.
- **investor-expert:** quick-money bootstrap validates Path B €3K+€15K 70.7% GM thesis; next verification at first-signed-contract.

#### G.4 Cycle-archive entry

Create `swarm/wiki/tasks/T-km-materialization-mvp-2026-04-<XX>/` with:
- `decisions/<date>-final-consolidation.md` (summary).
- `artefacts/` (links to all committed skills/configs/templates).
- `events.md` (appended throughout the sprint; finalize here).

#### G.5 Final commit + push

Commit: `[km-mvp] close cycle — Part G report + compound + agent-improvements + archive`.

Push. End of sprint.

---

## §3 Use-cases that MUST work end-to-end before Part F

For each UC, the executor writes `swarm/tests/<uc-slug>.sh` as a reproducible probe. Every probe exits 0 on pass; all probes run together via the master verify script (§2.F).

### UC-INGEST-1 — Multi-source ingest

**Given:** a YouTube URL (or a local transcript markdown if YouTube fetch blocked).

**When:** `/ingest <url>` runs.

**Then (all must hold):**
- ≥5 and ≤10 new concept pages under `swarm/wiki/concepts/`.
- ≥8 and ≤20 new edges in `swarm/wiki/graph/edges.jsonl`.
- 1 new row in `swarm/wiki/log.md` (prepended).
- 1 new row in `swarm/wiki/index.md`.
- Source page under `swarm/wiki/sources/<slug>.md` with full frontmatter + pipeline transition `raw → ingested`.

**Probe (`swarm/tests/uc-ingest-1.sh`):**

```bash
#!/usr/bin/env bash
set -euo pipefail
before_concepts=$(find swarm/wiki/concepts -name '*.md' | wc -l)
before_edges=$(grep -cE '^\{' swarm/wiki/graph/edges.jsonl)

# Use a local transcript fixture to be hermetic
FIXTURE="swarm/tests/fixtures/km-mvp/meadows-leverage-points-transcript.md"
[[ -f "$FIXTURE" ]] || { echo "UC-INGEST-1 FAIL: fixture missing"; exit 1; }

# /ingest invocation (as documented in skill — executor picks real invocation)
# For hermetic test: copy fixture to raw/ then invoke ingest
cp "$FIXTURE" raw/transcripts/

# Placeholder — actual skill invocation handled by executor's runtime
# In verification, executor performs the ingest and this probe validates the result
after_concepts=$(find swarm/wiki/concepts -name '*.md' | wc -l)
after_edges=$(grep -cE '^\{' swarm/wiki/graph/edges.jsonl)

delta_concepts=$((after_concepts - before_concepts))
delta_edges=$((after_edges - before_edges))

[[ $delta_concepts -ge 5 && $delta_concepts -le 10 ]] || { echo "UC-INGEST-1 FAIL: concepts Δ=$delta_concepts"; exit 1; }
[[ $delta_edges -ge 8 && $delta_edges -le 20 ]] || { echo "UC-INGEST-1 FAIL: edges Δ=$delta_edges"; exit 1; }

echo "UC-INGEST-1 PASS (Δconcepts=$delta_concepts, Δedges=$delta_edges)"
```

### UC-ASK-1 — Solve with wiki + insight write-back

**Given:** wiki with recent Meadows / systems-thinking concepts ingested.

**When:** `/ask "how does systems-thinking apply to Mittelstand outreach"` runs (cloud mode — i.e., without OFFLINE_MODE=1).

**Then:**
- Synthesized answer ≥200 words.
- ≥3 `[src:...]` citations in answer.
- 1 new file under `swarm/wiki/comparisons/` (filing loop).
- 1 new row in `wiki/insights/` or equivalent insight-capture path.

### UC-ASK-OFFLINE — Offline-first retrieval

**Given:** same wiki state.

**When:** `OFFLINE_MODE=1 /ask "<query>"` runs.

**Then:**
- Top-10 structured excerpts returned.
- Zero Task() dispatch (grep skill-invocation log).
- Zero outbound TCP on :443 during execution (executor runs `tcpdump` alongside; writes result to `swarm/tests/results/uc-ask-offline-tcpdump.log`).

**Probe:**
```bash
#!/usr/bin/env bash
set -euo pipefail
# Start tcpdump in background
sudo tcpdump -n 'tcp port 443 and not host 127.0.0.1' -c 1 > /tmp/offline-probe.log 2>&1 &
TCPD=$!
sleep 1

OFFLINE_MODE=1 # invoke /ask here per executor runtime
# (Executor runs the query; this probe validates result)

sleep 2
kill $TCPD 2>/dev/null || true
wait $TCPD 2>/dev/null || true

# Expect tcpdump captured zero packets (file should be small/empty)
if grep -q 'IP.*443' /tmp/offline-probe.log; then
  echo "UC-ASK-OFFLINE FAIL: outbound TCP :443 detected"
  exit 1
fi
echo "UC-ASK-OFFLINE PASS (zero outbound :443)"
```

Note: `tcpdump` requires sudo; if executor lacks sudo, substitute with `ss -t state established '( dport = :443 )'` polled before/during/after — same intent.

### UC-DIGEST — Weekly consolidation

**Given:** wiki with activity in past 7 days.

**When:** `/consolidate --weekly` runs.

**Then:**
- `swarm/wiki/digests/<YYYY-Www>.md` created.
- File contains sections: "New pages", "Top-edges", "Emergent themes", "Citations resolved".
- Empty-week case: file still created with explicit "no new pages this week" marker.

### UC-PROJECT-CONSULTING — Full consulting bootstrap

**Given:** project-types.yaml with consulting type; no existing `test-consulting-001` project.

**When:** `/project-bootstrap test-consulting-001 P1 --type=consulting` runs + operator fills in problem_statement/kill_criteria/kpi_targets.

**Then:**
- Exactly 9 files created under `swarm/wiki/operations/test-consulting-001/`.
- `.claude/agents/test-consulting-001-brigadier.md` created.
- `agents/test-consulting-001-brigadier/strategies.md` scaffold created.
- `/lint` on the project passes (all required frontmatter present).
- Mini-swarm default experts (mgmt-expert + sales-researcher) declared in project-brigadier manifest.

**Reject case:** re-run `/project-bootstrap test-consulting-001 P1 --type=consulting` and leave `problem_statement` empty — `/lint` flags `L-PROJECT-MISSING-REQUIRED-FRONTMATTER` hard error.

Cleanup: `/project-archive test-consulting-001 --reason=closed` after probe to keep repo clean.

### UC-PROJECT-ADAPTIVE — Adaptive bootstrap + SG fire

**Given:** project-types.yaml bets type; no existing `test-bet-001`.

**When:** `/project-bootstrap test-bet-001 P4 --type=bets --adaptive`.

**Then:**
- 3 files created (baseline only): `_moc.md`, `history.md`, `open-questions.md`.
- NO type_specific_files.
- `_moc.md` contains 4-5 stage-gate declarations per bets template.
- No mini-swarm spawned (P4; SG-4 not yet fired).

**Second step (simulate SG-1 firing):**
- Create 3 test lead files: `touch swarm/wiki/operations/test-bet-001/leads/{lead-a,lead-b,lead-c}.md` (requires scaffolding `leads/` dir first — this is what SG-1 auto-spawns).

Wait — in the strict probe, the operator creates the lead files WITHOUT `leads/` dir to simulate pre-SG-1 state; then `/lint --check-stage-gates` detects the predicate evaluation. Structure carefully:

Revised probe sequence:
1. Bootstrap `test-bet-001` adaptive → 3 files, no leads/ dir, SG-1 declared pending.
2. Create `swarm/wiki/operations/test-bet-001/leads/` dir + 3 test lead files manually via `mkdir + touch` (this is what SG-1 expects to find).
3. Run `/lint --check-stage-gates` on the project.
4. Verify: SG-1 fires → `pipeline.md` auto-spawned (per promotion_rules) → `_moc.md` SG-1 state becomes `fired`.

### UC-REVERSE — Stage-gate rollback

**Given:** `test-bet-001` with SG-1 fired and `pipeline.md` spawned.

**When:** `/project-de-morph test-bet-001 --rollback-to=SG-0` runs.

**Then:**
- `pipeline.md` removed (git rm).
- `_moc.md` SG-1 state back to `pending`; `fired_at` cleared; `spawned_paths` cleared.
- `history.md` has new entry: "de-morph rollback to SG-0; removed pipeline.md".

### UC-REVIEW — Weekly per-project digest

**Given:** `quick-money` project bootstrapped with history entries in past 7 days.

**When:** `/project-review quick-money` runs.

**Then:**
- `swarm/wiki/operations/quick-money/weekly-<Www>.md` created.
- Contains: traffic-light signal (🟢🟡🔴), progress list, open blockers, stage-gate status, KPI vs targets.

### UC-ISOLATION-DEMO — Client isolation

**Given:** demo-client-a and demo-client-b seeded under `clients/`.

**When:** agent with `WIKI_ROOT_CLIENT_ID=demo-client-a` attempts to read `clients/demo-client-b/swarm/wiki/concepts/anything.md`.

**Then (three layers — all must deny):**
1. **Config-level:** `wiki-roots.yaml` resolution produces `${WIKI_ROOT}=clients/demo-client-a/swarm/wiki/`; any read outside this root is flagged by the skill's Read-scope check.
2. **Filesystem-level (Phase-A approximation):** if the skill bypasses its own check and the operator directly invokes Read with absolute path, there is no OS-level denial in Phase-A (that is A2 Phase-B work; deferred). The probe documents this gap explicitly: Phase-A isolation is policy+config, not by-construction.
3. **Frontmatter-level:** any artefact written with `granularity: client:demo-client-a` into `swarm/wiki/global/` triggers `L-CROSS-CLIENT-GLOBAL` hard error.

**Probe:** `swarm/tests/uc-isolation-demo.sh` runs audit script:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Layer 1: resolution check
export WIKI_ROOT_CLIENT_ID=demo-client-a
# Run any skill that does resolution; check stdout reports resolved root = clients/demo-client-a/swarm/wiki/
# (implementation-specific — executor wires a --resolve-check flag)

# Layer 3: cross-client global-write rejection
# Create a test artefact in swarm/wiki/global/ with granularity: client:demo-client-a
mkdir -p swarm/wiki/global
cat > swarm/wiki/global/test-cross-client-violation.md <<EOF
---
title: test
granularity: client:demo-client-a
---
body
EOF

# Run /lint; expect L-CROSS-CLIENT-GLOBAL hard error (non-zero exit)
if /lint swarm/wiki/global/test-cross-client-violation.md 2>&1 | grep -q 'L-CROSS-CLIENT-GLOBAL'; then
  echo "UC-ISOLATION-DEMO Layer-3 PASS"
  rm swarm/wiki/global/test-cross-client-violation.md
else
  echo "UC-ISOLATION-DEMO Layer-3 FAIL"
  exit 1
fi

unset WIKI_ROOT_CLIENT_ID
echo "UC-ISOLATION-DEMO PASS (Phase-A: Layer-1 config + Layer-3 frontmatter; Layer-2 OS deferred to A2)"
```

The explicit documentation of Phase-A gap (vs Phase-B by-construction) preserves Dissent D-1 (engineering vs systems on Phase-A isolation).

### UC-COMPANY-STATUS — System snapshot

**Given:** repo state after all previous UCs.

**When:** `/company-status` runs.

**Then:**
- Output contains all 10+ expected lines (active projects, clients, mini-swarms, open SGs, ingest activity, wiki health, git status).
- Every field derived from local reads (zero network).
- Output ≤80 lines total (compact).

---

## §4 Artefact sources executor MUST read (treat as authoritative)

Before writing any code, the executor reads (in order of priority):

1. **`prompts/meta-brief-km-materialization-mvp-2026-04-24.md`** — the short brief that produced this deep prompt. Authority anchor.
2. **`decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md`** — Ruslan Gate-2 decision document; acked 2026-04-24T21:00:00Z. Read §§1-2-11-12-13 verbatim; skim §§3-10 for variant specs.
3. **`swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md`** — A1 implementation spec. Read §§4-6 verbatim (mechanics + UCs + UC-9/UC-10 co-located proof).
4. **`swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md`** — B2 implementation spec. Read §§4-6.
5. **`swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md`** — B3 mechanic spec. Read §§4.2-4.9 (stage-gates + de-morph + promotion).
6. **`decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`** — local-first / client-private positioning rationale. §§3-5.
7. **`decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md`** — Pillars 2+3 context. §§1-2.
8. **`decisions/JETIX-VISION.md`** — D22 ICP (§§7.1-7.2) for quick-money bootstrap.
9. **`decisions/JETIX-PLAN.md`** — D3 Phase-1 €50K Q2 2026 targets (§§3.1-3.9). Used verbatim in quick-money `_moc.md` kpi_targets.
10. **`decisions/JETIX-ARCHITECTURE-BRIEF.md`** — D4 foundation + 24 Locks + FPF E-items. §§2 and 4.
11. **`swarm/lib/shared-protocols.md`** — 9-section runtime contract. ALL sections. Every new skill imports this via §7 stub.
12. **`design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`** — wiki v3 layout spec. §§D1 (9-layer), D2 (frontmatter), D3 (12-edge enum), D7 (`$WIKI_ROOT` resolution), D8 (5 in-scope skills).
13. **`.claude/agents/brigadier.md`** — canonical brigadier template. Used as parent for `project-brigadier.md`.
14. **`CLAUDE.md`** — project conventions. §§ Wiki Architecture v2, Voice-Notes Pipeline, Конвенции, Правила.
15. **`.claude/rules/global.md`** — global rules (frontmatter, logs, KB, git, security, language).

Do not treat any document not on this list as authoritative for THIS sprint. If the executor feels need for another source (e.g., original Левенчук ШСМ text), note it in the ambiguity file (§11) and proceed with what's available.

---

## §5 Locked decisions honored (non-negotiable)

The following decisions are LOCKED and the executor MUST honor them verbatim:

- **D13 Open surface / Closed core.** Templates + methodology published (`swarm/wiki/_templates/` + skill docs); client-KB stays closed (per-client `clients/<slug>/swarm/wiki/` tree).
- **D17 Filesystem = Single Source of Truth.** Notion is optional view only. Zero Notion writes from executor.
- **D18 Productization over hours.** `/project-bootstrap` IS productization of Jetix's project-spawning know-how — a skill, not a slide.
- **D19 $1T trajectory.** Architecture must not preclude G2-G5 migration paths. A2 deferred (not impossible). A3 deferred (not impossible).
- **D20 USB-C positioning.** Wiki works with any underlying LLM (OpenAI / Anthropic / Llama / DeepSeek) via `$LLM_BACKEND` abstraction. No skill hardcodes a provider.
- **D21 Matchmaker + roy-replication.** Mini-swarms are "baby roys"; each P1/P2 project gets its own project-brigadier + 2 experts.
- **D24 Open-source research.** Research-type projects may be published externally; consulting/product stay closed.
- **W-5 Two-level Compounding Engineering.** Level-1 per-expert strategies.md; Level-2 promotion to `wiki/meta/agent-improvements/` after ≥10 uses + 3:1 ✓/✗. Compound DRR at Part G.
- **HD-01 €50K gate** referenced in project `kpi_targets` where applicable (quick-money specifically).
- **HD-02 N=2 M-class budget.** This materialization = 1 M-slot. Leaves 1 slot for M3 or emergency structural fix. Do NOT execute M3 in this sprint.
- **24 Locks + W-1..W-12 + FPF E-1..E-18 + shared-protocols 9 sections** unchanged.
- **Legacy coexistence.** 14 legacy `.claude/agents/*.md` and v2 `wiki/` untouched. All new work under `swarm/` + `.claude/skills/` + `.claude/config/` + `.claude/agents/<new-name>.md`.
- **Max-subscription discipline.** `unset ANTHROPIC_API_KEY OPENAI_API_KEY GROQ_API_KEY COHERE_API_KEY` before every launch. No paid API calls anywhere in the repo. Grep-verifiable.
- **No amend, no --no-verify, no force-push.**
- **Branch:** `claude/jolly-margulis-915d34`.

If any of the above feels wrong in the middle of execution: STOP. Write an ambiguity packet (§11). Do not unilaterally override.

---

## §6 Commit cadence + message grammar

### §6.1 Cadence

- **Per-skill creation or per-logical-unit** (not per-file).
- **Target:** 15-25 commits across the 7 days.
- **Push immediately after each commit.** No silent local work.

Approximate distribution:
- Part A (Days 1-2): ~6-8 commits (config + demo-dir + edges + 4 skill extensions + lint).
- Part B (Days 3-5): ~5-7 commits (config + bootstrap + 4 templates + project-brigadier + review + archive + lint).
- Part C (Day 5): ~3-4 commits (lint --check-stage-gates + DSL + de-morph + promote + phil gate).
- Part D (cross-cutting): ~2-3 commits (company-status + knowledge-diff + CLAUDE.md update).
- Part E (Days 6-7): ~4-5 commits (quick-money bootstrap + icp population + mini-swarm + demo + levenchuk + weekly digest).
- Part F (verification): ~1-2 commits (test scripts + AWAITING-APPROVAL packet).
- Part G (post-ack): ~1-2 commits (report + compound + archive + cleanup).

Total expected: ~22-31 commits. Within the 15-25 target range modulo the B2+B3 split.

### §6.2 Message grammar

`[<area>] <verb> <what> (<why>)`

- `<area>` ∈ {km-mvp, ingest, ask, lint, consolidate, build-graph, project-bootstrap, project-review, project-de-morph, project-promote, project-archive, project-types, agents, config, templates, tests, tools, docs, quick-money, levenchuk-deep-dive}.
- `<verb>` ∈ {add, extend, fix, refactor, wire, document, remove, archive, populate, bootstrap, promote}.
- `<what>` = concrete file or subsystem.
- `<why>` = one-line rationale: Gate-2 anchor / variant-draft section / UC reference.

### §6.3 Forbidden

- No `git commit --amend` after push.
- No `git push --force` or `git push --force-with-lease`.
- No `git commit --no-verify`.
- No signing-bypass.
- No rewriting history.

### §6.4 When a pre-commit hook fails

1. Do NOT `--amend`. The commit did not happen.
2. Fix the underlying issue (usually lint or frontmatter).
3. Re-stage (`git add <files>`).
4. Create a NEW commit.

---

## §7 Verification protocol

### §7.1 Per-Part smoke

Each of Parts A, B, C, E has a dedicated smoke script (see each §2.X subsection for the full bash snippet). Smoke scripts live under `swarm/tests/part-<letter>-smoke.sh`.

### §7.2 Per-UC integration probe

Each of 10 UCs (§3) has a dedicated probe under `swarm/tests/uc-<slug>.sh`. Each probe exits 0 on pass with a single line `<UC-name> PASS (<evidence-summary>)`. Each probe is idempotent: running it twice produces the same pass/fail.

### §7.3 Master verifier

`swarm/tests/km-mvp-verify.sh` chains all smokes + probes. Output captured to `swarm/tests/results/verify-<date>.log`.

### §7.4 Grep audits (run before AWAITING-APPROVAL)

1. No provider API keys:
   ```
   grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' \
     .claude/ swarm/ tools/ 2>/dev/null | grep -v 'unset\|\.md:#' | grep -v 'README\|docs/'
   ```
   Expect zero hits.

2. No hardcoded Jetix paths in skill code:
   ```
   grep -rEn 'swarm/wiki/operations/quick-money|operations/quick-money' \
     .claude/skills/ 2>/dev/null
   ```
   Expect zero hits. `quick-money` is data, not code.

3. Frontmatter coverage:
   ```
   for f in $(find swarm/wiki -name '*.md' -newer .claude/config/project-types.yaml); do
     head -1 "$f" | grep -q '^---$' || { echo "missing frontmatter: $f"; exit 1; }
   done
   ```

4. Schema version bumps:
   ```
   grep 'schema_version' .claude/config/wiki-roots.yaml .claude/config/project-types.yaml
   ```
   Expect both files declare it.

### §7.5 Verification matrix required in AWAITING-APPROVAL

The AWAITING-APPROVAL packet MUST contain the verification matrix as a markdown table:

```
| UC / Part | Probe | Status | Evidence |
|---|---|---|---|
| Part A smoke | part-a-smoke.sh | PASS | <log path> |
| Part B smoke | part-b-smoke.sh | PASS | <log path> |
| Part C smoke | part-c-smoke.sh | PASS | <log path> |
| Part E smoke | part-e-smoke.sh | PASS | <log path> |
| UC-INGEST-1 | uc-ingest-1.sh | PASS | <log path> |
| UC-ASK-1 | uc-ask-1.sh | PASS | <log path> |
| UC-ASK-OFFLINE | uc-ask-offline.sh | PASS | <tcpdump log path> |
| UC-DIGEST | uc-digest.sh | PASS | <digest file path> |
| UC-PROJECT-CONSULTING | uc-project-consulting.sh | PASS | <log> |
| UC-PROJECT-ADAPTIVE | uc-project-adaptive.sh | PASS | <log> |
| UC-REVERSE | uc-reverse.sh | PASS | <log> |
| UC-REVIEW | uc-review.sh | PASS | <log> |
| UC-ISOLATION-DEMO | uc-isolation-demo.sh | PASS | <log> |
| UC-COMPANY-STATUS | uc-company-status.sh | PASS | <output> |
```

All rows PASS or the packet is not submitted — the executor fixes first.

### §7.6 Regression discipline

If any probe starts FAILing during execution of later parts (regression), the executor STOPS, fixes, re-runs, and commits the fix before continuing. Do not leave broken probes "for later".

---

## §8 Stage-Gated pause spec (between Part F and Part G)

### §8.1 What triggers the pause

The pause triggers at the end of Part F — specifically after:
1. All smokes + probes PASS.
2. Grep audits clean.
3. `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md` written + committed + pushed.

### §8.2 What the pause means

- **Full-Auto NOT authorized for Part G.** Part G writes the execution report, which is a persistent artefact feeding next cycle's compound step. It must be reviewed.
- Executor writes NO further files until Ruslan ack detected.
- Executor MUST NOT anticipate Part G by pre-drafting the report. No "shadow writes".

### §8.3 How ack is detected

Any one of:

1. A new file `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>-ack.md` with frontmatter `{acked: true, chosen: <letter>, notes?}`.
2. Direct edit to the gate file's frontmatter: `state: acked` + `chosen: <letter>` + `notes: <text>`.
3. An explicit resume prompt in the next session: "Ruslan acked (a) — proceed to Part G."

On detection, executor logs the ack info to `swarm/wiki/tasks/T-km-materialization-mvp-.../events.md` and begins Part G.

### §8.4 What if Ruslan picks (b) MODIFY

Executor:
1. Reads the modification request.
2. Implements the specified delta.
3. Re-runs the verification matrix.
4. Writes a new AWAITING-APPROVAL packet (same filename + `-round-2` suffix).
5. Re-enters pause.

### §8.5 What if Ruslan picks (c) REJECT

Executor:
1. Writes remediation plan to `swarm/wiki/tasks/.../remediation-<date>.md`.
2. Does NOT modify any committed artefacts without further explicit direction.
3. Waits for Ruslan follow-up.

### §8.6 Intra-sprint checkpoint (NOT a pause)

Between Part E completion and Part F verification: brief checkpoint — executor writes a 1-paragraph status line to `swarm/wiki/tasks/T-km-materialization-mvp-.../events.md` and commits. This is a commit-then-continue, NOT a HITL pause.

### §8.7 No Full-Auto for Ruslan-facing artefacts

Anything Ruslan reads in isolation (Part G report, AWAITING-APPROVAL packet, outreach drafts for clients) is HITL-gated. Executor MAY prepare drafts under `swarm/wiki/drafts/` with `state: drafted` but MUST NOT promote to `decisions/` or ship externally without explicit ack.

---

## §9 Part G report format (≥3000 words; fires only after Ruslan ack)

### §9.1 Required file

`decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md`

### §9.2 Required frontmatter

```yaml
---
title: "KM Materialization MVP — Execution Report"
date: 2026-04-<XX>
type: execution-report
state: approved
task_id: T-km-materialization-mvp-2026-04-<XX>
cycle_id: cyc-km-materialization-2026-04-<XX>
acked_by: ruslan
acked_at: <ISO>
produced_by: km-mvp-executor
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md"}
  - {path: "swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md"}
  - {path: "swarm/tests/results/verify-<date>.log"}
related:
  - "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md"
  - "prompts/meta-brief-km-materialization-mvp-2026-04-24.md"
tier: core
binding_scope: km-materialization-mvp-cycle-3
word_count_approx: <filled at close>
---
```

### §9.3 Required sections (per §2.G.1 with word floors)

See §2.G.1 above for each section's word floor. Total ≥3000 words.

### §9.4 Required artifacts referenced

- Verification log path.
- All AWAITING-APPROVAL packet paths (round-1, round-2, etc., if modifications).
- Paths to each new skill, config file, and template directory.
- Pull-request / commit SHA list for the sprint (from `git log --oneline`).

### §9.5 Next M-class candidates (§7 of report) — guidance

Executor recommends top-3 next M-class tasks with sizing. Likely candidates:

1. **M3 solo-vs-matrix measurement task.** HD-02 companion slot open. Goal: empirical measure of whether 5×4 matrix dispatch outperforms single-expert on a fixed benchmark.
2. **A2 trigger-check infrastructure.** Health.md `first_paying_client_detector` auto-trigger + gate packet template for A2 activation. Size: S-M (1-2 days).
3. **First Mittelstand outreach batch.** B-class not M-class — but high-priority follow-up. Uses quick-money mini-swarm + icp.md + pipeline.md. Size: S (0.5-1 day).

### §9.6 Compound step checklist

At end of Part G:
- [ ] 4 x 4-part DRR entries appended to `agents/brigadier/strategies.md` (≥320w each).
- [ ] 5 x agent-improvements entries written under `swarm/wiki/meta/agent-improvements/` (≥200w each).
- [ ] Cycle-archive entry at `swarm/wiki/tasks/T-km-materialization-mvp-2026-04-<XX>/`.
- [ ] `meta/health.md` updated: `cycles_closed += 1`, `compound_rules_added: <count>`, `agent_improvements_promoted: <count>`.
- [ ] Final commit with message `[km-mvp] close cycle — Part G report + compound + archive` pushed.

### §9.7 End-of-sprint attestation

Final paragraph of Part G report:

> "I attest that: all 20/20 matrix cells from the Gate-2 variant analysis informed this execution; all 10 UCs verified PASS; zero provider API keys committed; zero legacy `wiki/` v2 or 14-legacy-agent writes; Max-sub discipline maintained; A2/A3/B1 NOT implemented per Gate-2 anti-scope; stage-gated pause honored between Part F and Part G. — km-mvp-executor, 2026-04-<XX>."

---

## §10 Anti-scope (verbatim from meta-brief §9 + enforced)

The executor MUST NOT:

- **Implement A2 Federated peer holons.** Deferred. Trigger: first paying client signed. Demo-client-a/-b exist ONLY for UC-9 probe; they are not production clients and carry no per-client agent instances, no per-client git repos, no per-client UNIX users. Phase-A is policy+config; Phase-B is A2.
- **Implement A3 GraphRAG / HippoRAG / PPR / community summaries at the SLM level.** Deferred. Trigger: 3K+ pages per client. `/build-graph` in this sprint does simple Louvain community detection for the communities.jsonl artefact; it does NOT precompute community summaries or run any LLM cron.
- **Implement B1 Thin namespaces as a standalone skill or config.** Rejected. Do not create B1-style `/project-bootstrap-thin`.
- **Promote variant drafts out of `swarm/wiki/drafts/`.** The 6 variant drafts stay as reference. MVP is a fresh implementation synthesizing A1 + B2 + B3-merged per variant specs; drafts are not "promoted" to canonical.
- **Touch legacy trees.** No writes to v2 `wiki/`, 14 legacy agents, or v1 `knowledge-base/` (which is in migration per MIGRATION.md). Touching these breaks the Q9+R3 coexistence lock.
- **Write to Notion.** D17 filesystem-SoT. Ruslan updates Notion if he chooses.
- **Execute M3 solo-vs-matrix.** HD-02 companion slot stays open. M3 is a separate cycle.
- **Hardcode Jetix-specific paths or project slugs in skill code.** Everything parameterised via `.claude/config/*.yaml`.
- **Reference provider API keys in any committed file.** Grep-test zero hits.
- **Adopt "good enough" attitude.** If any UC fails before Part F, fix. No shipping broken work.
- **Write `docs/` markdown or README.md files unless explicitly required by the task.** Project-level README.md exists; updates are allowed only if touching the new KM MVP subsystems (e.g., CLAUDE.md section per D.6).
- **Use emojis in committed files** unless user explicitly requests (they didn't). Traffic-light signals (🟢🟡🔴) in `/project-review` output ARE authorized because they're requested in §2.B.6 spec.

---

## §11 Escalation (ambiguity handling during execution)

### §11.1 When to escalate vs proceed

Escalate (write ambiguity packet) when:

- **Contradictions between variant drafts.** E.g., B2 draft assumes A2 substrate; the Gate-2 decision reshapes B2 atop A1-only. If executor finds a conflict in specs that isn't explicitly resolved in the meta-brief, escalate.
- **Ambiguity on stage-gate predicate DSL.** If the default SG predicate set from project-types.yaml doesn't fit a real bootstrap (e.g., research-type SG-rd-1 requires a field that isn't in the baseline template), escalate.
- **Uncertainty on mini-swarm agent file format.** Template inherits from `.claude/agents/brigadier.md`; if a concrete field is unclear (e.g., `split_trigger` semantics for project-brigadier), escalate.
- **How to merge B3 adaptive mechanic into B2 without doubling complexity.** If during Part C the executor finds a case where B3 semantics clash with B2 (e.g., stage-gate firing on a project that's already past SG-4), escalate.
- **Pen-test result unexpected.** E.g., if UC-ISOLATION-DEMO Layer-3 passes for the wrong reason (lint flagged a different signal), escalate.
- **Max-sub turn budget approaching ceiling.** If executor senses the sprint exceeding ~30h, escalate to Ruslan with status + options (defer Part E.5 Levenchuk, defer Part A.6 ollama docs, etc.).

Do NOT escalate for:

- Routine scaffolding choices (e.g., whether `leads/` uses `.gitkeep` or `README.md` as placeholder — pick one and be consistent).
- Minor wording in templates (use your judgment; don't over-document trivialities).
- Commit-message `<why>` phrasing (pick one; don't agonize).

### §11.2 Ambiguity packet format

`prompts/AMBIGUITY-km-materialization-<topic-slug>-<date>.md`

```markdown
---
title: "Ambiguity — <topic> — <date>"
type: ambiguity-packet
task_id: T-km-materialization-mvp-2026-04-<XX>
escalator: km-mvp-executor
escalated_at: <ISO>
state: open
---

# Ambiguity: <topic>

## Context
<where in the sprint this arose>

## Conflict
<what spec-A says vs what spec-B says>

## Options
(a) <option-A> — <tradeoff>
(b) <option-B> — <tradeoff>
(c) defer until Ruslan guidance

## Impact on critical path
<how this blocks or does not block Parts A/B/C/E>

## Recommendation
<executor's best guess if forced to decide>

## How to ack
Same as AWAITING-APPROVAL gate ack mechanism.
```

Commit + push the ambiguity packet. Do not modify the ambiguous area until resolved. Continue with unblocked parts of the sprint if possible.

### §11.3 Specific pre-identified ambiguities (flagged in meta-brief §12)

The meta-brief pre-flagged 4 ambiguity classes. For each, the executor's recommended default (use unless Ruslan signals otherwise):

1. **B2 draft assumes A2 substrate.** Default: implement B2 atop A1. Per-client paths use `clients/<slug>/swarm/wiki/operations/<project>/` WHERE `--client=<slug>` is passed; absent client, use `swarm/wiki/operations/<project>/` (Jetix-internal). The 13th `holon-ref` edge is NOT added (A2 territory).

2. **Stage-gate predicate DSL ambiguity.** Default: simple predicate grammar per §2.C.2 — `count(<glob>)`, `count(<glob>:<marker>)`, `<metric> >= <N>`, compound `AND/OR`. If a specific SG needs a richer predicate (e.g., regex match on history.md content), write `tools/stage-gate-eval.py` to support it with clear docstring. Escalate only if the richer predicate class can't be expressed deterministically.

3. **Project-brigadier manifest format.** Default: copy `.claude/agents/brigadier.md` headers; replace name, scope, budget; keep §7 shared-protocol import stubs verbatim. Drop sections irrelevant to project scope (e.g., §1c Graph-of-Creation — project-brigadier inherits from canonical).

4. **B3 + B2 merge clash.** Default: B3 mechanic is an OPTIONAL layer on B2, activated via `--adaptive` flag. A project CAN start as full B2 (all type_specific_files at bootstrap) OR as adaptive (baseline only + stage-gates). If both modes clash (e.g., `--type=consulting --adaptive` — conflicts because consulting has 4 type_specific_files and --adaptive says start minimal), default behaviour: --adaptive wins → start with baseline only + consulting stage_gates declared → type_specific_files auto-spawn as SGs fire. Document this in `/project-bootstrap` skill body.

---

## §12 Definition of Done

### §12.1 Parts A-E Done

- [ ] All smokes PASS (A/B/C/E).
- [ ] All 10 UCs PASS.
- [ ] All grep audits clean.
- [ ] All new skills have executable-bit + shebang + `set -euo pipefail`.
- [ ] All new `.md` artefacts have complete frontmatter + provenance gate satisfied.
- [ ] All new config files have `schema_version` + `last_modified` + `managed_by`.
- [ ] `quick-money` P1 project bootstrapped with real Jetix content.
- [ ] `levenchuk-deep-dive` P3 research project bootstrapped adaptively.
- [ ] First weekly digest generated.
- [ ] End-to-end ingest+ask demo logged to `quick-money/history.md`.
- [ ] Commits count between 15 and 31 (target: 22).
- [ ] All commits pushed.

### §12.2 Part F Done

- [ ] Master verify script written + runs green.
- [ ] AWAITING-APPROVAL packet written with verification matrix table.
- [ ] Packet committed + pushed.
- [ ] Executor halted (no further writes until ack).

### §12.3 Part G Done (after ack)

- [ ] Report written (≥3000 words, all required sections + word floors).
- [ ] 4 x 4-part DRR entries appended to `agents/brigadier/strategies.md`.
- [ ] 5 x agent-improvements entries written.
- [ ] Cycle-archive entry created.
- [ ] `meta/health.md` updated.
- [ ] Final commit + push.
- [ ] Attestation paragraph present at end of report.

### §12.4 Overall sprint Done

- [ ] `git status` clean on `claude/jolly-margulis-915d34`.
- [ ] No unpushed commits.
- [ ] No unresolved ambiguity packets.
- [ ] Report visible at `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md`.
- [ ] Summary line posted (session final message): "KM MVP sprint complete: <N> commits, <M> skills, <K> UCs verified, quick-money P1 live, report at decisions/KM-MATERIALIZATION-MVP-REPORT-<date>.md."

---

## §13 Executor-facing cheat sheet (one-pager)

> Keep this section open in a side window during the sprint.

### ORDER

1. Part A Day 1-2 — A1 substrate: wiki-roots clients: + demo-client dirs + edges + 5 skill extensions (ingest multi-src, ask offline, consolidate weekly, build-graph, lint 5 signals).
2. Part B Day 3-5 — B2: project-types.yaml + /project-bootstrap + project-brigadier template + 4 scaffold templates + /project-review + /project-archive + /lint required-frontmatter.
3. Part C Day 5 — B3 merged: /lint --check-stage-gates + DSL + /project-de-morph + /project-promote + philosophy SG-validation gate.
4. Part D (cross-cutting) — company-as-code: structured commits + /company-status + /knowledge-diff + CLAUDE.md update.
5. Part E Day 6-7 — real work: quick-money P1 + icp from D22 + mini-swarm + ingest+ask demo + levenchuk adaptive + weekly digest.
6. Part F — master verify + AWAITING-APPROVAL. HALT.
7. Part G (after ack) — ≥3000w report + compound DRR + 5 agent-improvements + cycle-archive.

### KEY DON'TS

- Don't implement A2 (federated peer holons). Deferred.
- Don't implement A3 (GraphRAG / HippoRAG community summaries at LLM level). Deferred.
- Don't implement B1 (thin namespaces). Rejected.
- Don't touch v2 `wiki/` or 14 legacy agents.
- Don't write to Notion.
- Don't execute M3 solo-vs-matrix.
- Don't hardcode Jetix paths in skill code. Config-driven only.
- Don't commit provider API keys. Grep-zero.
- Don't `--amend`, `--no-verify`, force-push.
- Don't skip the Stage-Gated pause between Part F and Part G.
- Don't ship broken UCs. Fix before advance.

### KEY DOS

- Do `unset ANTHROPIC_API_KEY OPENAI_API_KEY GROQ_API_KEY COHERE_API_KEY` at session start.
- Do read §4 sources before coding.
- Do `set -euo pipefail` + shebang + executable-bit on every bash helper.
- Do complete frontmatter + provenance-gate pass on every `.md`.
- Do structured commit messages: `[<area>] <verb> <what> (<why>)`.
- Do push after every commit.
- Do write per-UC probes under `swarm/tests/`.
- Do escalate ambiguities via packet in §11.2 format — do not guess on structural decisions.
- Do honor Ruslan Gate-2 verbatim: A1 full + B2 full + B3 merged + company-as-code.
- Do treat 1000% depth as the bar. No corners cut.

### COMMITS target

- 15-25 (target 22). Distribution approximate: A=6-8, B=5-7, C=3-4, D=2-3, E=4-5, F=1-2, G=1-2.

### ESCALATION path

- Structural ambiguity → `prompts/AMBIGUITY-km-materialization-<topic>-<date>.md`.
- UC fail not fixable in-session → AWAITING-APPROVAL packet with round-N suffix.
- Max-sub budget approaching ceiling → status message + options to Ruslan.
- Contradiction with 24 Locks / FPF / shared-protocols → STOP. Do not proceed.

### DAILY RHYTHM (suggestion)

- **Day 1 (Part A.1-A.4):** config + demo dirs + edges + /ingest extensions. 3 commits.
- **Day 2 (Part A.5-A.9):** /ask offline + /consolidate weekly + /build-graph + /lint. 3 commits.
- **Day 3 (Part B.1-B.3):** project-types.yaml + /project-bootstrap + 4 templates. 3 commits.
- **Day 4 (Part B.4-B.8):** project-brigadier + review + archive + lint. 4 commits.
- **Day 5 (Part C.1-C.6):** stage-gates + DSL + de-morph + promote + phil gate + Part D cross-cutting. 5 commits.
- **Day 6 (Part E.1-E.4):** quick-money + icp + mini-swarm + demo. 3 commits.
- **Day 7 (Part E.5-E.6 + Part F):** levenchuk + weekly digest + verify + AWAITING-APPROVAL. 3 commits. HALT.
- **Day ??? (post-ack): Part G** — report + compound + archive. 2 commits.

### ONE-LINER TO LAUNCH THE NEXT SESSION

```
cd /home/ruslan/jetix-os && git checkout claude/jolly-margulis-915d34 && git pull && \
  unset ANTHROPIC_API_KEY OPENAI_API_KEY GROQ_API_KEY COHERE_API_KEY && \
  echo "Read prompts/km-materialization-mvp-execution-2026-04-24.md; execute Parts A-G."
```

---

*End of execution prompt. Next session: read this file §§1-13, then §4 sources, then start Part A.1.*
