---
title: Engineering × Optimizer — Pipeline Deltas (Ingest + Retrieval + Offline-LLM)
type: optimization
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: medium
confidence_method: expert-judgment-from-critic-draft-and-tier1
tier: tier-1
produced_by: engineering-optimizer
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md", range: "§1-§3"}
  - {path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md", range: "Parts B/F/G/H"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§3,5,6"}
  - {path: "prompts/km-architecture-research-2026-04-24.md", range: "§1.2/§3.9/§3.10"}
  - {path: ".claude/config/wiki-roots.yaml", range: "full"}
  - {path: ".claude/skills/ingest.md", range: "full"}
  - {path: ".claude/skills/ask.md", range: "full"}
related: []
binding_scope: km-architecture-engineering-optimizer-deltas
mode: optimizer
---

# Engineering × Optimizer — Pipeline Deltas

> **Scope statement.** This optimizer proposes minimal-LOC, invariant-checked
> delta proposals that close the 8 Conformance failures surfaced by
> `engineering × critic` (especially H-3, H-4, H-8) plus the UC-10 escalation
> from `mgmt × critic`. Each delta carries WLNK/MONO/IDEM/COMM/LOC declarations,
> a before/after table, and an (F, ClaimScope, R) triple. Method-change candidates
> are refused with documented rationale. No implementation is written — manifests
> and skill-body patches only.

---

## §1 Delta Proposals (one section per H-N closed)

### Δ1 — Close H-3: Per-Client Isolation Namespace Boundary

**Target:** `.claude/config/wiki-roots.yaml` + enforcement note in
`swarm/lib/shared-protocols.md §5` role-tool-matrix

**Conformance failure being closed:** H-3 — No filesystem-namespace boundary
preventing Client-A's `/ask` from retrieving Client-B's wiki content.
[src: engineering-critic §1 H-3; BIOS-insight §6 "client-isolation mechanics MISSING"]

#### Before (verbatim excerpts)

`.claude/config/wiki-roots.yaml` (lines 10-14):
```yaml
wiki_root_v2: wiki
wiki_root_v3: swarm/wiki
default_root: wiki_root_v3
```
No `clients:` stanza. Single configurable root. All five skills operate against
one `$WIKI_ROOT` value; no per-client binding exists.

`swarm/lib/shared-protocols.md §5` role-tool-matrix: lists tool permissions for
the 6 Phase-A agents; does not name a `WIKI_ROOT_CLIENT_ID` env var or a
session-init assertion step.

#### After (proposed delta — manifest additions only)

`.claude/config/wiki-roots.yaml` — add `clients:` stanza after `default_root:`:

```yaml
# Per-client isolated roots (UC-9 client-isolation, BIOS-insight §6).
# Each key is a client-id slug; value is the path from repo root.
# Phase A: single active client at a time; multi-client requires separate
# repo or OS-level permission scoping per engineering-critic §3 H-3 Alt-A / Alt-B.
clients:
  _template: "clients/{client-id}/swarm/wiki"   # canonical path pattern
  # Populated at client-onboarding time by /ingest-client (Phase B skill).
  # Phase A placeholder: empty map = single-tenant Jetix-internal deployment.

# Session-init enforcement assertion (by-policy, Phase A; by-construction, Phase B).
# When WIKI_ROOT_CLIENT_ID env var is set, all 5 skills MUST resolve $WIKI_ROOT
# to clients.{WIKI_ROOT_CLIENT_ID} above. If client-id not in clients: map,
# skill returns structured error "unknown client-id; register in wiki-roots.yaml first".
client_root_env_var: WIKI_ROOT_CLIENT_ID
client_root_isolation: policy-enforced   # Phase A; Phase B upgrades to OS-level
```

`swarm/lib/shared-protocols.md §5` — add one row to the role-tool-matrix:

```
| WIKI_ROOT resolution | All 5 skills | On every invocation: if $WIKI_ROOT_CLIENT_ID set, assert clients.map[$WIKI_ROOT_CLIENT_ID] exists in wiki-roots.yaml before any Read/Write; else use default_root. |
```

#### Before/After Measurement Table

| Axis | Before | After | Delta | Method |
|---|---|---|---|---|
| LoC in `wiki-roots.yaml` | 45 lines | 58 lines | +13 lines | wc -l |
| LoC in `shared-protocols.md §5` | N (existing rows) | N+1 rows | +1 row | wc -l |
| Client roots declared | 0 | template + empty map (0 active) | structural +1 | count keys |
| Isolation mode | none | policy-enforced Phase A | qualitative | — |
| Skills requiring update | 0 (transparent via env) | 0 (env-var transparent) | 0 | count skill diffs |

#### Invariant Declarations

| Invariant | Applies? | Preserved? | Evidence |
|---|---|---|---|
| WLNK | YES | YES | All 5 skills already resolve `$WIKI_ROOT` via D7 §7.4 algorithm; adding `WIKI_ROOT_CLIENT_ID` lookup is an additive branch, not a removal. Existing single-tenant path unchanged. |
| MONO | YES | YES | Client-isolation adds a constraint; it does not remove precision from the existing retrieval path. No regression on single-tenant quality. |
| IDEM | YES | YES | Adding a key to `wiki-roots.yaml` is idempotent; re-adding the same client-id with same path is a no-op (same YAML value). |
| COMM | N/A | — | This delta is a manifest addition; no ordering dependency with adjacent build steps. |
| LOC | PARTIAL | Intentional violation documented | Change touches `wiki-roots.yaml` + `shared-protocols.md §5`. Cross-file, but minimum required for UC-9 enforcement. Per engineering-critic §2 H-3: "LOC violation; this is intentional cross-scope enforcement, not a scope leak." Same rationale preserved. |

**F: F4** (operational convention; single-source, one enforcement point not yet runtime-tested)
**ClaimScope:** Jetix Phase-A single-tenant → single-client deployment; unknown for simultaneous multi-client without Phase-B OS-level isolation upgrade.
**R:** `refuted_if` first real multi-client session shows cross-client read despite `WIKI_ROOT_CLIENT_ID` being set (i.e., a skill ignores the env-var check); `accepted_if` first multi-client test session shows client-A's `/ask` only reads paths under `clients/client-a/swarm/wiki/`.

**Rationale:** The engineering-critic correctly flags that env-var enforcement is process-level, not OS-level. This delta implements the minimum Phase-A version (policy-enforced, by-convention) which closes H-3 at F4 confidence. Phase-B upgrade to Alt-B (OS-level permissions) is a Method decision requiring HITL ack — see §3 Refusal Δ3b below.

---

### Δ2 — Close H-4: Offline Synthesis Path in `/ask` Tier-4

**Target:** `.claude/skills/ask.md` — Step 2 and Step 4 algorithm additions

**Conformance failure being closed:** H-4 — Tier-4 long-context fallback requires
a live LLM call; UC-10 demands offline-first synthesis without cloud APIs.
[src: engineering-critic §1 H-4; BIOS-insight §3 "offline-first AI integration MISSING";
BIOS-insight §6 "Llama/DeepSeek distilled для local inference"]

#### Before (verbatim excerpt)

`.claude/skills/ask.md` Step 2 (lines 33-37):
```
- При необходимости — grep по ключевым словам вопроса в ${WIKI_ROOT}/**/*.md.
- Смотри niche: если вопрос явно про sales — приоритет ${WIKI_ROOT}/niches/sales/...
- Если есть community summaries (${WIKI_ROOT}/graph/summaries.md) — используй их...
  (Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)
```

No `OFFLINE_MODE` branch. Step 4 (Синтезировать ответ) implicitly relies on a
live Claude Code session for LLM-authored prose synthesis. No structured-excerpt
fallback exists.

#### After (proposed delta — skill-body patch)

Add to `.claude/skills/ask.md` Step 2, after the community summaries line:

```
### Offline-mode check (UC-10)

If env var `OFFLINE_MODE=1` is set:
  - Skip Tier-4 LLM long-context synthesis.
  - Proceed with Tiers 1/2/3 (index read + grep + wikilink depth-2 follow)
    to retrieve the top-5 candidate pages.
  - In Step 4 below: produce Structured-Excerpt Synthesis (offline path)
    instead of LLM-authored prose synthesis (online path).
```

Add to `.claude/skills/ask.md` Step 4, as a conditional branch:

```
### Step 4 — Synthesize answer

**Online path (default, OFFLINE_MODE unset or =0):**
  Produce LLM-authored synthesis prose (existing behaviour — unchanged).

**Offline path (OFFLINE_MODE=1, UC-10):**
  Produce Structured-Excerpt Compilation:
  1. For each of the top-5 retrieved pages:
     - Print: page title, one-sentence definition (first non-frontmatter sentence),
       top-3 claims (frontmatter `claims:` field or first 3 bullet points).
  2. Print: "Cross-references:" — list all `related:` frontmatter links across
     the 5 pages (deduped).
  3. Print: "No LLM synthesis in offline mode — review source pages for detail."
  Quality note: offline synthesis quality is lower than online LLM prose.
  This is the stated UC-10 tradeoff (engineering-critic §2 H-4 MONO=applies).
```

#### Before/After Measurement Table

| Axis | Before | After | Delta | Method |
|---|---|---|---|---|
| LoC in `ask.md` | 124 lines | ~155 lines | +31 lines | wc -l estimate |
| LLM calls per `/ask` in offline mode | 1+ (Tier-4 LLM) | 0 (Tier-4 bypassed) | -1 mandatory call | manual count |
| UC-10 satisfaction | NO | YES (degraded-mode, structured excerpt) | structural YES | binary |
| Online path changed | YES (baseline) | NO (unchanged) | 0 delta | diff |
| External deps in offline path | cloud LLM | 0 | -1 dep | grep import |

#### Invariant Declarations

| Invariant | Applies? | Preserved? | Evidence |
|---|---|---|---|
| WLNK | YES | YES | Online callers see no change; offline callers gain a structured-excerpt response. No existing contract broken. |
| MONO | YES | APPLIES (known tradeoff) | Offline path quality is monotonically lower than online — this is the stated UC-10 design tradeoff per engineering-critic §2 H-4: "MONO=applies (offline synthesis quality is lower than LLM synthesis — this is the stated UC-10 tradeoff)". Accepted. |
| IDEM | YES | YES | Running `/ask` twice in offline mode on same query produces same structured excerpt (deterministic page selection + same frontmatter content). |
| COMM | N/A | — | The offline/online branch is independent; no ordering dependency with Step 6 (save to comparisons/) or Step 7 (update index/log). |
| LOC | YES | YES | Change is confined to `ask.md` Steps 2 and 4 only. Does not touch `ingest.md`, `wiki-roots.yaml`, `consolidate.md`, `lint.md`, or `build-graph.md`. |

**F: F3** (multi-source: BIOS-insight §3 offline mandate + engineering-critic §2 H-4 Alt-A specification + prompts §3.10 acceptance criteria; not yet runtime-tested)
**ClaimScope:** Holds for Phase-A Tier-1/2/3 retrieval path (filesystem grep + wikilink follow); offline structured-excerpt quality is explicitly lower than LLM synthesis. Full local-LLM path (Alt-B: Llama/DeepSeek distillation) is Phase B — see §3 refusal below.
**R:** `refuted_if` running `/ask "test query" OFFLINE_MODE=1` returns LLM-authored prose (i.e., the branch was not inserted correctly); `accepted_if` running same command returns a structured excerpt of ≤5 pages with no cloud API call observed.

**Rationale (§4.4 heuristics cited):** Boris Cherny "do the simple thing first" — the structured-excerpt offline path is the simplest semantically valid UC-10 response. It avoids the Alt-B complexity (Llama distillation) which would be a Method change requiring HITL. Fowler "Extract Method" pattern: the offline synthesis branch is a named algorithm variant extracted into a conditional, keeping the existing online path unchanged (WLNK preserved).

---

### Δ3 — Close H-8: Per-Client Wiki-Roots Indirection

**Target:** `.claude/config/wiki-roots.yaml` `clients:` stanza (Δ1 above) +
new conceptual path `clients/{client-id}/swarm/wiki/` documented in
`wiki-roots.yaml` comments

**Conformance failure being closed:** H-8 — No per-client ingest path that routes
content to an isolated per-client wiki root by construction.
[src: engineering-critic §1 H-8; engineering-critic §2 H-8 Alt-A fix spec]

#### Before (verbatim excerpt)

`.claude/config/wiki-roots.yaml` (lines 34-44):
```yaml
skills_in_scope_for_wiki_root:
  - ingest
  - ask
  - lint
  - consolidate
  - build-graph
```
All 5 skills share one `$WIKI_ROOT`. No `--client-id` parameter variant. No per-client
subtree path exists in the repo or in the manifest.

#### After (proposed delta — manifest addition)

Δ1 already adds the `clients:` stanza. Δ3 supplements it with the path convention
documentation in `wiki-roots.yaml` comments:

```yaml
# Per-client skill invocation convention (UC-9 + UC-8 isolation, H-8 fix):
# To ingest into a client's isolated wiki, callers set:
#   WIKI_ROOT_CLIENT_ID=<client-id> /ingest <source-path>
# This causes $WIKI_ROOT to resolve to clients.<client-id> above.
#
# Path layout per client (must be provisioned at onboarding time):
#   clients/{client-id}/swarm/wiki/              # wiki root
#   clients/{client-id}/swarm/wiki/index.md
#   clients/{client-id}/swarm/wiki/graph/edges.jsonl
#   clients/{client-id}/swarm/wiki/_templates/   # symlink or copy from swarm/wiki/_templates/
#   clients/{client-id}/swarm/wiki/niches/       # client-scoped niches
#
# The /ingest skill resolves $WIKI_ROOT via D7 §7.4 algorithm;
# no skill-body change is required to support --client-id IF the
# WIKI_ROOT_CLIENT_ID env var is set correctly at invocation.
# Phase B: add /ingest-client as a named skill wrapper that sets the env var
# and validates the client path exists before calling /ingest.
client_path_convention: "clients/{client-id}/swarm/wiki"
client_onboarding_skill: "/ingest-client"   # Phase B; stub only in Phase A
```

#### Before/After Measurement Table

| Axis | Before | After | Delta | Method |
|---|---|---|---|---|
| LoC in `wiki-roots.yaml` | 58 lines (post-Δ1) | ~78 lines | +20 lines | wc -l |
| Per-client path convention documented | NO | YES | qualitative | — |
| Skills requiring code change for `--client-id` | 5 (if flag approach) | 0 (env-var approach) | -5 skill diffs | count |
| Phase-B named skill stub declared | NO | YES (`/ingest-client` named) | +1 stub ref | — |

#### Invariant Declarations

| Invariant | Applies? | Preserved? | Evidence |
|---|---|---|---|
| WLNK | YES | YES | Existing single-tenant path unchanged. Client-specific path is additive. |
| MONO | YES | YES | Per-client roots are monotonically more isolated than the single shared root. No quality regression. |
| IDEM | YES | YES | Writing the same client path convention twice produces the same YAML. |
| COMM | N/A | — | Manifest addition; no ordering dependency. |
| LOC | YES | YES | Change confined to `wiki-roots.yaml` comments + new keys. No skill bodies touched. |

**F: F3** (structured on engineering-critic §2 H-8 Alt-A fix spec + D7 §7.4 env-var resolution algorithm; Phase-A policy-level only)
**ClaimScope:** Holds for Phase-A single-developer setup with one active client at a time; Phase-B simultaneous multi-client requires OS-level permission scoping (Alt-B) or separate-repo-per-client — both are Method decisions beyond this delta.
**R:** `refuted_if` setting `WIKI_ROOT_CLIENT_ID=test-client` and running `/ingest raw/test.md` writes pages to `swarm/wiki/` instead of `clients/test-client/swarm/wiki/`; `accepted_if` same invocation writes pages correctly to `clients/test-client/swarm/wiki/`.

**Rationale (§4.4 heuristics cited):** Ousterhout deep-module — the env-var indirection keeps the skill interface thin (no new flags) while the implementation (path resolution) handles the per-client routing behind the existing `$WIKI_ROOT` surface. Hunt/Thomas orthogonality: `WIKI_ROOT_CLIENT_ID` is an orthogonal concern from the skill's internal algorithm; setting or unsetting it does not change the skill's correctness, only its routing destination.

---

### Δ4 — Close UC-10 Mgmt Escalation: Offline-First Inference Stack Manifest

**Target:** New file `swarm/lib/inference-stack.yaml` — manifest only, NOT
implementation. Addresses mgmt-critic escalation: "UC-10 engineering architecture
critique → engineering-expert × critic on UC-10 local inference stack per prompts §3.10"

**Conformance failure being closed:** UC-10 "offline-first inference" — no local
LLM stack specified. Combined with Δ2's structured-excerpt offline path for Phase A.
[src: BIOS-insight §3 "offline-first AI integration — Llama/DeepSeek distilled для local inference";
BIOS-insight §6 "Missing: offline-first AI integration"; mgmt-critic §6 UC-10;
prompts §3.10 acceptance criteria]

#### Before

No `swarm/lib/inference-stack.yaml` exists. No inference-stack manifest anywhere in
the Phase-A swarm. The Max-subscription discipline (shared-protocols §9) prohibits
third-party LLM API calls but does not provision a local inference path.

#### After (proposed delta — new manifest file, NOT implementation)

```yaml
# swarm/lib/inference-stack.yaml
# Offline-first local inference stack manifest (UC-10).
# This file declares the target stack for Phase-B implementation.
# Phase A: structured-excerpt synthesis (Δ2 /ask offline path) is the active fallback.
# Phase B: local LLM replaces structured-excerpt synthesis when OFFLINE_MODE=1.
# AWAITING-APPROVAL required before any implementation begins (§1d requires-approval).

schema_version: 1
last_modified: 2026-04-24
managed_by: brigadier
status: manifest-only   # Phase A: declared but not implemented

# --- Stack selection (ordered by Jetix fit) ---

primary_stack:
  name: ollama
  rationale: >
    Pure-Go single binary; no CUDA required for CPU inference; simple REST API
    on localhost; model pull is one command; no Python dependency chain.
    Aligns with D17 Filesystem-SoT (model weights = files on client disk).
  local_api_endpoint: "http://localhost:11434"
  install_footprint: "single binary ~50MB + model weights on client disk"

alternative_stacks:
  - name: llama.cpp
    rationale: "Low-level C++ inference; maximum quantization flexibility; no REST layer out-of-box (add llama.cpp server); ideal for embedding in tooling."
    fit: "high-throughput batch workloads; lower-level than ollama"
  - name: vLLM
    rationale: "High-throughput GPU inference; PagedAttention; best for server with dedicated GPU and concurrent users."
    fit: "Path A Jetix-hosted multi-client; overkill for single-client Phase A"
  - name: LM Studio
    rationale: "GUI wrapper; easy for non-technical client staff; downloads models via UI."
    fit: "Path B client-hosted non-technical; Phase B demo path"

# --- Model defaults (offline-first, client-private) ---

model_defaults:
  primary:
    family: Llama
    model: Llama-3.1-8B-Instruct
    quantization: Q4_K_M
    format: GGUF
    hardware_floor:
      gpu_vram_gb: 8      # minimum for fast inference
      gpu_vram_gb_comfortable: 16  # target floor for production quality
      cpu_ram_gb: 16      # CPU inference fallback (slow but functional)
    rationale: >
      Llama 3.1 8B Q4_K_M is the established baseline for local inference on
      Mittelstand hardware (16GB GPU = mid-range workstation). Q4_K_M balances
      perplexity quality vs quantization loss. Knowledge cutoff compatible with
      2024-2025 Mittelstand AI use cases.
      [src: BIOS-insight §8 recommendation 7 "On-prem distilled LLMs as Mittelstand LLM"]

  alternative_1:
    family: Mistral
    model: Mistral-7B-Instruct-v0.3
    quantization: Q4_K_M
    format: GGUF
    rationale: "Stronger multilingual performance (German/Russian); relevant for DACH Mittelstand. Comparable hardware footprint to Llama 3.1 8B."

  alternative_2:
    family: DeepSeek
    model: DeepSeek-R1-Distill-Llama-8B
    quantization: Q4_K_M
    format: GGUF
    rationale: >
      DeepSeek R1 distilled into Llama 8B architecture; strong reasoning capability
      at 8B scale. Relevant for knowledge synthesis over client-private corpus.
      [src: BIOS-insight §3 "Llama/DeepSeek distilled для local inference"]

# --- Integration with /ask OFFLINE_MODE ---

offline_mode_integration:
  phase_a:
    active: true
    mechanism: structured-excerpt-synthesis   # Δ2 above; no local LLM required
    trigger: "OFFLINE_MODE=1 env var in /ask invocation"

  phase_b:
    active: false   # AWAITING-APPROVAL
    mechanism: local-llm-synthesis
    trigger: "OFFLINE_MODE=1 + LOCAL_LLM_ENDPOINT env var pointing to ollama/llama.cpp"
    skill_changes_required:
      - "/ask Step 4 offline path: replace structured-excerpt with local LLM call to $LOCAL_LLM_ENDPOINT"
      - "/ask Step 2: if LOCAL_LLM_ENDPOINT set, use local LLM for HyDE keyword enhancement"
    acceptance_predicate: >
      /ask "test query" with OFFLINE_MODE=1 and LOCAL_LLM_ENDPOINT=http://localhost:11434
      returns LLM-authored prose without any call to Anthropic/OpenAI endpoints
      AND elapsed time ≤ 120s for a 5-page retrieval on 16GB GPU hardware.

# --- Security note (D13 Open surface / Closed core) ---

security_note: >
  Client model weights live on client infrastructure. Jetix methodology repo
  (swarm/lib/, .claude/skills/) is pushed to client; client data and model
  weights are NEVER pulled back to Jetix. Aligns with D13 + D17 + BIOS-insight §4.
  [src: BIOS-insight §4 "Jetix никогда не становится central server для client data"]
```

#### Before/After Measurement Table

| Axis | Before | After | Delta | Method |
|---|---|---|---|---|
| Local inference stack documented | NO | YES (manifest) | +1 manifest file | count |
| LoC in new file | 0 | ~110 lines | +110 lines | wc -l |
| Phase-A offline capability | structured-excerpt (Δ2) | structured-excerpt (Δ2) + stack declared | +stack declaration | qualitative |
| Phase-B implementation scope | undefined | named (ollama + Llama 3.1 8B Q4_K_M) | scope defined | qualitative |
| Paid API dependencies | 0 (Max-subscription) | 0 | 0 delta | grep |

#### Invariant Declarations

| Invariant | Applies? | Preserved? | Evidence |
|---|---|---|---|
| WLNK | YES | YES | Manifest is a new file with no existing consumers; no existing workflow link broken. |
| MONO | YES | YES | Adding a manifest does not reduce capability; it only adds documentation for Phase-B implementation scope. |
| IDEM | YES | YES | Writing this manifest twice produces the same YAML content. |
| COMM | N/A | — | Manifest file; no ordering dependency with other build steps. |
| LOC | YES | YES | New file in `swarm/lib/`; does not touch skills, wiki-roots, or shared-protocols. |

**F: F3** (multi-source: BIOS-insight §3/§6/§8 + prompts §3.10 UC-10 acceptance criteria + mgmt-critic escalation; hardware floor from industry consensus on Q4_K_M inference)
**ClaimScope:** Stack selection (ollama + Llama 3.1 8B Q4_K_M) holds for Mittelstand single-server deployment with 16GB GPU / 16GB CPU RAM floor. Simultaneous-user high-throughput deployment may prefer vLLM (Path A Jetix-hosted). German-language query performance may prefer Mistral 7B alternative.
**R:** `refuted_if` first Phase-B integration test shows Llama 3.1 8B Q4_K_M produces unacceptable synthesis quality on German-language client queries (then switch to Mistral 7B alt); `accepted_if` Phase-B acceptance predicate above passes on target hardware.

**Rationale (§4.4 heuristics cited):** Boris Cherny "do the simple thing first" — ollama single binary is simpler than vLLM or a custom llama.cpp server setup. Poppendieck waste elimination: the manifest declares the stack without building it, eliminating premature implementation waste in Phase A. The Phase-B implementation gate (AWAITING-APPROVAL) is explicitly preserved.

---

## §2 Pre-Cache vs On-Demand Tradeoff Matrix

This matrix covers the retrieval-side deltas and their latency/storage implications.
Applies to all clients using the Δ1/Δ3 per-client wiki-roots pattern.

| Retrieval mechanic | Pre-cache cost | On-demand latency | Storage cost | Recommendation | Relevant delta |
|---|---|---|---|---|---|
| **index.md full read (Tier-1)** | Zero (index is always current) | O(1) per read — single file | Grows linearly with wiki size; ~1 line per page | No pre-cache needed at G1 (557 pages → ~2KB index). Pre-cache at G2 (5K pages → ~20KB). | Δ2 / Δ3 (same per client) |
| **grep Tier-2 (full wiki)** | Zero | O(N·L) where N=pages, L=avg lines. At G1: ~2-5s. At G2: 30-60s without index. | No storage — live scan | Pre-build per-niche BM25 index at G2+ (engineering-critic §3 H-2 Alt-B). For Phase A (G1): on-demand grep is sufficient. | Δ2 (OFFLINE_MODE affects Tier-4 only; Tier-2 grep always on-demand) |
| **edges.jsonl BFS Tier-3** | Zero (edges.jsonl always current) | O(E·d) where E=edges, d=max_depth. At G1 (572 edges, depth-2): ~50ms in-memory. At G2 (~5700 edges): ~500ms. | Grows linearly; currently ~57KB. At G2: ~570KB. | On-demand at G1-G2. Pre-compute community summaries at G3 (50K pages). [src: knowledge-arch §G.2] | Δ2 improves Tier-3 by making BFS explicit (H-7 complement) |
| **Structured-excerpt synthesis (Tier-4 offline, Δ2)** | Zero (no pre-build; reads live pages) | O(5) page reads = ~5 × avg_page_read_time ≈ 1-3s total. No LLM call. | No additional storage | Preferred for offline path. Latency floor well inside 180s budget even at G2. | Δ2 |
| **LLM synthesis (Tier-4 online, existing)** | Zero (no pre-cache) | Network + inference: 5-30s for Sonnet. Counts against 180s budget if combined with slow Tier-2 grep. | No storage | Online default; combine with Tier-2 grep timeout (engineering-critic §2 H-2 fix: `T_budget=180s`) to stay within budget. | Not a Δ in this optimizer pass (H-2 fix is a separate delta not proposed here — insufficient baseline measurements for LOC) |
| **Local LLM synthesis (Tier-4 Phase-B, Δ4 manifest)** | Model weights: Llama 3.1 8B Q4_K_M ≈ 4.7GB on disk. One-time download. | Inference: 8-15 tokens/s on 16GB GPU → 200-token answer ≈ 15-25s. Within 180s budget. | 4.7GB per client installation (model weights). Per-client storage cost. | Preferred for Phase-B offline path over structured-excerpt quality-wise. | Δ4 (Phase-B manifest) |

**Key tradeoff summary:** For Phase A (G1, offline mode), structured-excerpt synthesis (Δ2) costs 0 storage overhead and 1-3s latency — significantly better than the 180s budget. For Phase B (G2+, full local LLM), the 4.7GB per-client model weight cost is the primary constraint; for Mittelstand single-server deployment this is acceptable. GraphRAG community summaries (pre-cache) become cost-effective only at G3 (50K pages) per knowledge-arch §G.1.

F: F4 (operational convention from knowledge-arch §G.1-§G.3 scaling analysis + known inference benchmarks for Q4_K_M)
ClaimScope: G1-G2 Jetix Phase-A single-tenant; G3 projections are forward-looking.
R: medium

---

## §3 Refusals (Method-Change Candidates)

The following candidates from the engineering-critic's §3 Alternatives were
considered for delta proposals and REFUSED as Method-changes per §4.3 (E-4
hard refusal).

### Refusal R-1: OS-Level Permission Scoping (H-3 Alt-B / H-4 Alt-B in critic)

**Proposed:** Enforce client-isolation via OS-level `chmod`/`chown` directory
permissions with a per-client OS user account.

**Refused because:** This changes the **Method** of isolation from filesystem-path
parameterization (current D17 Filesystem-SoT method, which operates within a single
OS user context) to OS-level user/permission management. It requires:
- Deployment automation that does not exist in Phase A
- OS user provisioning outside the skill ecosystem
- Infrastructure changes external to the swarm's tool set (Bash + file tools)

This is a deployment-infrastructure Method decision. It requires HITL ack and
architect-level design beyond the optimizer's scope wall.

**Escalation:** `escalations[]{trigger: method-change, candidates: ["H-3 Alt-B OS-level isolation", "H-8 Alt-B OS-level isolation"], route: "integrator or HITL — deployment infrastructure method"}`.

### Refusal R-2: Separate-Git-Repository-Per-Client (H-8 Alt-B / mgmt-critic H-4 Alt-A)

**Proposed:** Each client gets a full fork of `jetix-os/` in a separate private
Git repository. By-construction isolation at repo level.

**Refused because:** This changes the **Method** of code/methodology distribution
from single-repo-parameterized to multi-repo-forked. It introduces:
- A cross-repo methodology update fan-out problem (engineering-critic §3 H-8 Alt-B kill-condition)
- A new orchestration requirement (brigadier must manage multiple git remotes)
- A packaging methodology question (how does Jetix methodology ship as a versioned update without client data?)

All three sub-questions are Method decisions requiring HITL ack. The optimizer
cannot resolve them by patching `wiki-roots.yaml`.

**Escalation:** `escalations[]{trigger: method-change, candidate: "per-repo client isolation", route: "integrator — three-path (A/B/C) from BIOS-insight §5 must be surfaced as a variant-level decision, not a parameter delta"}`.

### Refusal R-3: Full HippoRAG PPR Implementation (H-7 Alt-B)

**Proposed:** Implement full Personalized PageRank on `edges.jsonl` inside
`/ask` Tier-3 as a proper iterative algorithm.

**Refused because:** Phase-A constraint (`ask.md` allowed-tools: `Read, Write, Edit, Glob, Grep` — no `Bash`). Full PPR requires iterative floating-point computation over a graph matrix. Without Bash or a Python runner, this cannot be implemented inside the skill body as a pure Claude Code tool sequence. A proper PPR implementation requires either a Bash script (tool not available in `/ask`) or a dedicated graph-computation helper — a Method change in the retrieval architecture.

The explicit depth-2 BFS improvement (H-7 Alt-A — engineering-critic §2 H-7 fix) IS implementable without Bash and is NOT refused; it is noted here as a complementary delta addressable in a follow-up optimizer pass with a proper baseline measurement. It was not included in this pass because the brief's acceptance predicate covers H-3 + H-4 + H-8 + UC-10 specifically; H-7 is a lower-priority follow-on.

**Escalation:** `escalations[]{trigger: method-change, candidate: "full PPR in Phase-A Bash-free skill", route: "integrator — H-7 Alt-A (explicit depth-2 BFS) is the within-method fix; H-7 Alt-B requires Bash tool unlock or a separate graph-computation agent"}`.

---

## §4 Coverage Matrix (Deltas vs Conformance Failures)

| H-N from critic | Δ closing it | Refused? | Coverage |
|---|---|---|---|
| H-1 (≥8 typed-edge guarantee in `/ingest`) | Not in this optimizer pass — H-1 is a `/ingest` step 6 count gate; insufficient baseline measurement for LOC invariant on step 6 alone. Follow-up pass needed with edge-count baseline from a representative ingest run. | No refusal | Deferred |
| H-2 (latency floor at G2 for `/ask`) | Not in this optimizer pass — H-2 requires a `T_budget=180s` timeout and hop-limit in `/ask` step 2. Deferred: insufficient baseline measurements (no timing data from real G2 run). LOC invariant UNCLEAR without observed grep latency. | No refusal | Deferred |
| **H-3** (client-isolation namespace) | **Δ1** (wiki-roots.yaml `clients:` stanza + shared-protocols §5 assertion row) | No | Closed (Phase A policy; Phase B by-construction requires R-1 method-change HITL) |
| **H-4** (offline synthesis path) | **Δ2** (`/ask` offline structured-excerpt branch) | No | Closed (Phase A degraded-mode; Phase B local LLM via Δ4 manifest) |
| H-5 (strategies.md cross-namespace merge) | Not in this optimizer pass — H-5 is a `/consolidate` pre-merge guard; the brief's acceptance predicate targets H-3/H-4/H-8/UC-10. Separate optimizer pass needed. | No refusal | Deferred |
| H-6 (concept count not enforced) | Not in this optimizer pass — brief acceptance predicate targets H-3/H-4/H-8/UC-10. Follow-up pass needed. | No refusal | Deferred |
| H-7 (Tier-3 BFS implicit) | Not in this optimizer pass — see Refusal R-3 (Alt-B PPR refused; Alt-A depth-2 BFS deferred to follow-up pass). | R-3 (method-change on Alt-B only) | Deferred (Alt-A) |
| **H-8** (no per-client wiki-roots indirection) | **Δ3** (wiki-roots.yaml path convention + Phase-B `/ingest-client` stub) | No | Closed (convention documented; Phase B skill wrapper deferred) |
| **UC-10** (offline-first inference stack) | **Δ2** (Phase-A structured-excerpt path) + **Δ4** (`swarm/lib/inference-stack.yaml` manifest) | No (Phase-B implementation gated AWAITING-APPROVAL) | Closed at Phase-A level; Phase-B implementation requires HITL ack |

**Acceptance predicate result:** The Hamel-binary predicate from the brief — "Returns ingest+retrieval+offline-LLM delta proposals each with WLNK/MONO/IDEM/COMM/LOC declared AND before/after table AND refuses on method-change with documented rationale AND covers H-3 + H-4 + H-8 AND each delta carries (F, ClaimScope, R) triple" — is met by Δ1 (H-3), Δ2 (H-4), Δ3 (H-8), Δ4 (UC-10), with R-1/R-2/R-3 as method-change refusals and H-1/H-2/H-5/H-6/H-7 deferred with documented rationale.

---

## §5 Anti-Scope

- **NOT proposing Layer-A or Layer-B variants.** That is integrator-mode work. This optimizer proposes parameter-level deltas to existing skills and manifests only.
- **NOT touching legacy `wiki/` v2 or the 14 legacy agents** under `.claude/agents/` (untouched per Phase-A locks D17 + Q9 coexist).
- **NOT proposing paid APIs, vector DBs, or non-Max-subscription infrastructure.** All proposed deltas use filesystem + env-vars + YAML manifests + existing skill tool sets. [src: shared-protocols §9; prompts §1.3]
- **NOT proposing capital expenditure.** The 16GB GPU hardware floor in Δ4 is named as a planning datum, not a purchase recommendation. Capital allocation is investor-expert territory.
- **NOT implementing H-1/H-2/H-5/H-6/H-7 fixes.** Insufficient baseline measurements for those deltas to satisfy the §4.1 invariant-check row (especially LOC) without observed runtime data. Deferred to follow-up optimizer pass with explicit baseline numbers.
- **NOT proposing full PPR.** Refused as method-change (R-3). The explicit depth-2 BFS delta (H-7 Alt-A) is recommended as a follow-on task for a subsequent `engineering × optimizer` pass.
- **NOT authoring system-models.** The feedback-loop implications of client-isolated wikis on the dev-cycle (e.g., per-client methodology sync latency) are systems-expert territory. This optimizer surfaces the engineering mechanics; systems-expert models the feedback dynamics.

---

## §6 UC-10 Offline-LLM Stack Manifest Sketch

Δ4 above contains the full manifest. Summary for quick reference:

- **Phase A (active now):** Structured-excerpt synthesis (Δ2 `/ask` offline path). No local LLM required. Latency: 1-3s. Quality: lower than LLM prose. Trigger: `OFFLINE_MODE=1`.
- **Phase B (AWAITING-APPROVAL):** Local LLM via ollama (primary stack). Model: Llama 3.1-8B-Instruct Q4_K_M GGUF. Hardware floor: 16GB GPU / 16GB CPU RAM. Alternates: Mistral 7B Q4_K_M (better German), DeepSeek-R1-Distill-Llama-8B Q4_K_M (better reasoning). Inference: 8-15 tok/s → ~15-25s for 200-token answer on target hardware.
- **Integration trigger:** `OFFLINE_MODE=1` + `LOCAL_LLM_ENDPOINT=http://localhost:11434` env vars in `/ask` invocation.
- **Security:** Model weights live on client disk; Jetix methodology repo is pushed to client; no client data or weights pulled back to Jetix. Directly implements BIOS-insight §3 + §4 + D13 + D17.

---

## §7 F-G-R Summary Per Delta

| Delta | F | ClaimScope | R |
|---|---|---|---|
| Δ1 — H-3 isolation namespace | F4 | Phase-A policy-enforced; Phase-B by-construction requires HITL | medium — refuted if skill ignores WIKI_ROOT_CLIENT_ID |
| Δ2 — H-4 offline synthesis | F3 | Phase-A structured-excerpt path; Phase-B local LLM per Δ4 | medium — refuted if OFFLINE_MODE=1 still calls cloud LLM |
| Δ3 — H-8 per-client indirection | F3 | Phase-A convention; multi-client simultaneous requires method-change | medium — refuted if env-var routing writes to wrong wiki root |
| Δ4 — UC-10 inference stack | F3 | Mittelstand 16GB GPU floor; German-language may prefer Mistral alt | medium — refuted if Phase-B acceptance predicate fails on target hardware |
| R-1 — OS-level isolation (refused) | — | Method-change; HITL required | N/A |
| R-2 — Per-repo per-client (refused) | — | Method-change; integrator variant decision | N/A |
| R-3 — Full PPR (refused) | — | Method-change for Phase-A Bash-free skill | N/A |

---

## §8 Provenance

All claims in this optimizer draft trace to the following Tier-1 in-repo sources.
No Tier-4 book reads performed in Phase A. No paid API calls.

| # | Path | Range | Key claim supported |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md` | §1 H-3/H-4/H-8; §2 H-3/H-4/H-8 fixes; §3 H-3/H-8 alternatives | All four delta targets; invariant declarations sourced from critic's §2 Hamel-binary fixes |
| P-2 | `.claude/config/wiki-roots.yaml` | full (45 lines) | Before-state for Δ1 and Δ3; schema_version, managed_by, skills_in_scope fields |
| P-3 | `.claude/skills/ingest.md` | Steps 3, 6, algorithm | Before-state for H-1/H-6 context; $WIKI_ROOT resolution pattern confirming Δ1/Δ3 env-var approach |
| P-4 | `.claude/skills/ask.md` | Steps 2, 4 (lines 33-37, 44-59) | Before-state for Δ2; exact text of Step 2 community-summaries line and Step 4 synthesis algorithm |
| P-5 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §3 (local-first client-private KB); §5 Path A/B/C; §6 (built vs missing); §8 rec 7 | Δ4 inference stack motivation; client-data-stays-on-client-disk invariant; ollama/Llama/DeepSeek selection |
| P-6 | `raw/research/knowledge-architecture-deep-research-2026-04-19.md` | Part B §B.2 (HippoRAG PPR pseudocode); Part G §G.1-§G.3 (scale milestones); Part H §H.5 (retrieval pipeline YAML) | §2 pre-cache tradeoff matrix; G1/G2/G3 thresholds; R-3 PPR refusal grounding |
| P-7 | `prompts/km-architecture-research-2026-04-24.md` | §1.2 point 7 (local-first mandate); §3.9 UC-9; §3.10 UC-10 | Δ1/Δ3 isolation mandate; Δ2/Δ4 offline-first mandate; disqualifying anti-patterns list |
| P-8 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md` | §6 UC-10 escalation (lines 352-370) | Δ4 UC-10 escalation routing; mgmt-critic's "offline-inference-spec.md" gap flag |
