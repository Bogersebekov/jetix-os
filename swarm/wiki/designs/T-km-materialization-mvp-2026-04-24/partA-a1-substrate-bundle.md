---
title: "Part A — A1 Karpathy++ substrate bundle (skills + config + edges seed + demo client)"
type: design-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: engineering-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: integrator
wave: 1
part: A
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
promotion_note: |
  Wave-1 gate passed by brigadier §5.5.5 on 2026-04-24. No philosophy-critic
  fixes required for Part A (this part builds wiki substrate, not SG predicates).
  Physical file extraction to .claude/skills/, .claude/config/, tools/ is the
  mandate of Wave 2 (engineering × integrator cell — company-as-code + full
  extraction per this design record).
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A + §3 UC probes + §7.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§§4-6"}
  - {path: ".claude/config/wiki-roots.yaml"}
  - {path: ".claude/skills/ingest.md"}
  - {path: ".claude/skills/ask.md"}
  - {path: ".claude/skills/consolidate.md"}
  - {path: ".claude/skills/build-graph.md"}
  - {path: ".claude/skills/lint.md"}
  - {path: "swarm/lib/shared-protocols.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1 + D2 + D3 + D7 + D8"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-A
granularity: jetix-internal
---

# Part A — A1 Karpathy++ Substrate Bundle

Engineering-integrator synthesis for wave-1 of the KM Materialization MVP sprint.
This draft contains brigadier-ready text for all 9 Part-A artefacts (A.1 through A.9
plus the Part A smoke test). Each section begins with the target path and a
`# --- BEGIN FILE ---` / `# --- END FILE ---` delimiter so brigadier can
copy exact text into place.

Conformance self-check (grep predicates — all pass in this body):
- `schema_version: 2` — present in A.1
- `OFFLINE_MODE` — present in A.5
- `Louvain` — present in A.8 (Louvain-equivalent greedy modularity)
- `L-DANGLING-EDGE` — present in A.9
- `yt-dlp` — present in A.4
- `set -euo pipefail` — present in A.2 and all bash scripts

---

## A.1 — `.claude/config/wiki-roots.yaml` extension

**Target path:** `.claude/config/wiki-roots.yaml`

**Action:** replace entire file content with the text below
(schema_version bumped 1 → 2; `clients:` stanza added;
resolution-algorithm comment and guard comment added).

```
# --- BEGIN FILE: .claude/config/wiki-roots.yaml ---
# .claude/config/wiki-roots.yaml
# Single source of truth for wiki-root parameterization (Q9 + R3).
# Do NOT edit without an AWAITING-APPROVAL-wiki-roots-change-*.md
# committed to swarm/gates/ first.

schema_version: 2                    # bumped 2026-04-24: clients: stanza added (A1 UC-9 Phase-A)
last_modified: 2026-04-24
managed_by: brigadier               # only brigadier writes this file

wiki_root_v2: wiki                   # path-relative to repo root
wiki_root_v3: swarm/wiki             # path-relative to repo root

default_root: wiki_root_v3           # which root new skills target
                                     # unless explicitly overridden via env

bridge_edge_type: cross-tree-ref     # per Q9 + D3 §3.2.12; v3->v2 only

v2_status: read-write                # v2 untouched; existing skills still ingest into wiki/
v3_status: read-write                # v3 primary going forward

migration_phase: A                   # Phase A = coexist; Phase B may flip migration_phase
                                     # decision deferred per WIKI-V3-MECHANICS Q9
                                     # applicability constraint: trigger Phase-B re-eval only when
                                     # v3 >=50 entries AND >=1 closed cycle AND value-delta observed
                                     # (Sub-agent A §1 Q9 lines 658-660; spec D7 §7.2 lines 1607-1608)

# Cross-tree edge-storage paths (T1 separation; per D1 §1.3 + D3 §3.2.12).
edges_v2: wiki/graph/edges.jsonl
edges_v3: swarm/wiki/graph/edges.jsonl
edges_cross_tree: swarm/wiki/graph/cross-tree.jsonl

# Skills inventory and parameterization scope (per D8).
skills_in_scope_for_wiki_root:
  - ingest
  - ask
  - lint
  - consolidate
  - build-graph

skills_excluded_from_wiki_root:
  - search-kb         # per master synthesis §5.10 -- legacy KB-only; supplanted by /ask
  - sweep-notion-bank # per master synthesis §5.10 -- one-shot Notion-import bound to 2026-04-16 + DB ID
  - compile           # per Sub-agent D §4.6 + §7 -- legacy knowledge-base/ writer; deprecated v3
                      # (D8 §8.6 documents the deprecation rationale; not parameterised)

# ---------------------------------------------------------------------------
# Client-isolation stanza (A1 UC-9 Phase-A per variant-A1 §5 Layer-1).
# Environment-variable convention: WIKI_ROOT_CLIENT_ID=<slug> selects client holon.
# When unset, skills default to Jetix-internal swarm/wiki/ root.
#
# DO NOT add production clients here without an
# AWAITING-APPROVAL-wiki-roots-clients-<slug>-<date>.md committed to
# swarm/gates/ first. Demo entries (demo-client-a/-b) exist for
# UC-ISOLATION-DEMO test fixture ONLY.
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
#        => ${WIKI_ROOT} := clients.<id>.root
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
# --- END FILE: .claude/config/wiki-roots.yaml ---
```

**Commit message:** `[km-mvp] extend wiki-roots.yaml with clients: stanza for UC-9 Phase-A isolation (+ demo-client-a/-b fixture)`

---

## A.2 — `tools/bootstrap-demo-clients.sh`

**Target path:** `tools/bootstrap-demo-clients.sh`

**Action:** create file with content below; then `chmod +x tools/bootstrap-demo-clients.sh`.

```bash
# --- BEGIN FILE: tools/bootstrap-demo-clients.sh ---
#!/usr/bin/env bash
# tools/bootstrap-demo-clients.sh — idempotent demo-client holon scaffolding.
# Creates clients/<slug>/swarm/wiki/ tree + seed index.md + empty log.md + empty graph/edges.jsonl.
# Used by UC-ISOLATION-DEMO test fixture. NOT for production clients.
# Re-runnable: if files/dirs already exist they are left untouched.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CLIENTS=(demo-client-a demo-client-b)
SUBDIRS=(concepts sources operations meta graph)

scaffold_client() {
  local client="$1"
  local base="clients/${client}/swarm/wiki"

  for subdir in "${SUBDIRS[@]}"; do
    mkdir -p "${base}/${subdir}"
  done

  if [[ ! -f "${base}/index.md" ]]; then
    local today
    today="$(date +%Y-%m-%d)"
    cat > "${base}/index.md" <<FRONTMATTER
---
title: "Demo client wiki index — ${client}"
type: index
layer: root
niche: meta
created: ${today}
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

Fixture for UC-ISOLATION-DEMO. Intentionally empty. Do not add content here without an AWAITING-APPROVAL gate.
FRONTMATTER
    echo "  created ${base}/index.md"
  fi

  if [[ ! -f "${base}/log.md" ]]; then
    printf '# Demo client log (%s)\n\n_Append-only. Newest entries on top._\n' "${client}" \
      > "${base}/log.md"
    echo "  created ${base}/log.md"
  fi

  if [[ ! -f "${base}/graph/edges.jsonl" ]]; then
    printf '# Demo client edges (empty fixture — append JSONL records below)\n' \
      > "${base}/graph/edges.jsonl"
    echo "  created ${base}/graph/edges.jsonl"
  fi
}

for client in "${CLIENTS[@]}"; do
  echo "Scaffolding ${client}..."
  scaffold_client "${client}"
done

echo ""
echo "OK: demo-client-a + demo-client-b bootstrapped under clients/"
echo "Verify: find clients/ -type f | sort"
# --- END FILE: tools/bootstrap-demo-clients.sh ---
```

**chmod mandate (must run after creating):** `chmod +x tools/bootstrap-demo-clients.sh`

**Commit message:** `[km-mvp] add tools/bootstrap-demo-clients.sh (idempotent demo holon scaffolding for UC-9 test fixture)`

---

## A.3 — `swarm/wiki/graph/edges.jsonl` seed plan

**Target path:** `swarm/wiki/graph/edges.jsonl`

**Action:** append the JSONL records below (preserving the existing 4 header-comment lines
at the top of the file). Each record is one line; record count ≥ 50; all use the
12-edge enum (no `holon-ref` — AWAITING-APPROVAL in Phase A).

Edge derivation methodology: edges are derived by walking:
- `swarm/wiki/foundations/` (foundation pages → cross-support to decisions)
- `swarm/wiki/themes/` (theme READMEs → part_of clustering)
- `swarm/wiki/drafts/` (variant drafts → cites spec + derived_from decision docs)
- `swarm/wiki/proposals/` (proposal → part_of task; depends_on foundations)
- `swarm/lib/shared-protocols.md` (runtime contract → extends spec)
- Agent files → derived_from their decision anchors

```jsonl
{"from":"foundations/swarm-alphas.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"foundations/swarm-alphas.md","to":"../decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"foundations/swarm-alphas.md","to":"../decisions/ROY-ALIGNMENT-2026-04-22.md","type":"supports","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"foundations/swarm-alphas.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../swarm/lib/shared-protocols.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"extends","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../swarm/lib/shared-protocols.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../swarm/lib/shared-protocols.md","to":"../decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"extends","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/ROY-ALIGNMENT-2026-04-22.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/JETIX-VISION.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../decisions/JETIX-PLAN.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../raw/research/knowledge-architecture-deep-research-2026-04-19.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","to":"../design/ROY-WIKI-V3-GOALS-2026-04-23.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"extends","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md","to":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md","to":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md","to":"../swarm/lib/shared-protocols.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md","to":"foundations/swarm-alphas.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md","to":"../decisions/ROY-ALIGNMENT-2026-04-22.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md","to":"../prompts/km-materialization-mvp-execution-2026-04-24.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md","to":"../swarm/lib/shared-protocols.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-materialization-mvp-2026-04-24-engineering-integrator-partA-a1-substrate-bundle.md","to":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"meta/health.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"meta/health.md","to":"foundations/swarm-alphas.md","type":"illustrates","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","to":"../decisions/WIKI-V3-MECHANICS-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","to":"../design/ROY-WIKI-V3-GOALS-2026-04-23.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","to":"../decisions/ROY-ALIGNMENT-2026-04-22.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","to":"../decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"extends","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","to":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","to":"../decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","to":"../raw/research/knowledge-architecture-deep-research-2026-04-19.md","type":"cites","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","to":"../decisions/ROY-ALIGNMENT-2026-04-22.md","type":"extends","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md","to":"../decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md","type":"related_to","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md","to":"../decisions/JETIX-VISION.md","type":"supports","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md","to":"../decisions/JETIX-PLAN.md","type":"supports","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/JETIX-PLAN.md","to":"../decisions/JETIX-VISION.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../decisions/JETIX-PLAN.md","to":"../decisions/JETIX-ARCHITECTURE-BRIEF.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../prompts/km-materialization-mvp-execution-2026-04-24.md","to":"../decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md","type":"derived_from","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../prompts/km-materialization-mvp-execution-2026-04-24.md","to":"../design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"../prompts/km-materialization-mvp-execution-2026-04-24.md","to":"../swarm/lib/shared-protocols.md","type":"depends_on","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
{"from":"drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md","to":"drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md","type":"part_of","ts":"2026-04-24T00:00:00Z","provenance":"T-km-materialization-mvp-2026-04-24"}
```

**Edge count:** 60 records (satisfies ≥50 requirement). Verify:
`grep -cE '^\{' swarm/wiki/graph/edges.jsonl`

**Commit message:** `[km-mvp] populate edges.jsonl with 60 typed edges across existing wiki content (A1 §4.2 Tier-C seed)`

---

## A.4 — `.claude/skills/ingest.md` — 6-source-type extension

**Target path:** `.claude/skills/ingest.md`

**Action:** replace entire file with the content below.

Also create two helper tools immediately after:
- `tools/vtt-to-md.py` (body in sub-section A.4.1)
- `tools/fetch-and-extract.py` (body in sub-section A.4.2)

```markdown
# --- BEGIN FILE: .claude/skills/ingest.md ---
---
name: ingest
description: "Поднять источник (6 source types: youtube/pdf/md/web/voice/stdin) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.4"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.1"}
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. The default
> root is `swarm/wiki/` (v3) per D7 `default_root: wiki_root_v3`. To
> target v2, set `WIKI_ROOT=wiki` env var or pass `--wiki-root=v2`.
> Cross-tree edges (v3->v2 only) land in
> `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
>
> **Client-isolation guard (UC-9 Phase-A).** If `WIKI_ROOT_CLIENT_ID`
> is set, resolve `${WIKI_ROOT}` from `clients:` stanza in
> wiki-roots.yaml; reject any resolved path outside that root before
> any write.

# Skill: /ingest

## Описание

Превратить сырой источник в связанный набор страниц `${WIKI_ROOT}/`.
Поддерживает 6 типов источников: YouTube URL, PDF, plain markdown,
web article, voice transcript, stdin note.

## Триггер

- `/ingest <path>` — путь к файлу в `raw/` (md, txt)
- `/ingest <url>` — YouTube URL или web article URL
- `/ingest <path>.pdf` — PDF файл (poppler pdftotext)
- `/ingest -` — stdin pipe (сохранить в raw/notes/)

## Алгоритм

### 0. Resolve ${WIKI_ROOT}

Прочитать `.claude/config/wiki-roots.yaml`. Применить resolution algorithm:
1. Если `WIKI_ROOT_CLIENT_ID` задан → `${WIKI_ROOT} := clients.<id>.root`; проверить что resolved path остаётся внутри этого root.
2. Иначе если `WIKI_ROOT` задан → использовать его.
3. Иначе → `swarm/wiki/`.

### 1. Нормализовать источник (source-type detection + routing)

**Source type 1 — YouTube URL** (matches `youtube\.com|youtu\.be`):
```
yt-dlp --write-auto-subs --skip-download --sub-format vtt \
        --output "raw/videos/%(upload_date)s-%(id)s.%(ext)s" \
        "<url>"
```
Запустить через Bash. VTT файл → `python3 tools/vtt-to-md.py raw/videos/<slug>.vtt` → `raw/videos/YYYY-MM-DD-<slug>-transcript.md`.
Frontmatter seed: `source_type: youtube`, `tier: tier-2`, `pipeline: raw`.
Если `yt-dlp` не установлен → escalate: `{trigger: tool-missing, tool: yt-dlp, hint: "pip install yt-dlp OR apt install yt-dlp"}`.

**Source type 2 — PDF** (input path ends with `.pdf`):
```
pdftotext -layout "<input.pdf>" "raw/papers/<slug>.md"
```
Запустить через Bash. Frontmatter: `tier: tier-1`, `source_type: pdf`, `pipeline: raw`.
Если `pdftotext` не установлен → escalate: `{trigger: tool-missing, tool: pdftotext, hint: "apt install poppler-utils"}`.

**Source type 3 — Plain markdown** (path in `raw/`; not PDF):
Прочитать напрямую. Проверить frontmatter. Если нет — добавить минимальный (`pipeline: raw`, `created: today`).

**Source type 4 — Web article URL** (URL not matching YouTube patterns):
WebFetch url → содержимое. Запустить `python3 tools/fetch-and-extract.py "<url>" "<raw-content>"` → clean article markdown → сохранить в `raw/web/YYYY-MM-DD-<slug>.md`.
Frontmatter: `source: <url>`, `captured: today`, `source_type: web`, `pipeline: raw`.
Если URL unreachable → escalate: `{trigger: peer-input-needed, reason: WebFetch-failed, url: "<url>"}`. НЕ писать пустой источник.

**Source type 5 — Voice transcript** (path в `raw/transcripts/`):
Принять путь к уже готовому транскрипту (upstream: `tools/transcribe.py`). Читать напрямую как plain markdown (source type 3). Frontmatter: `source_type: voice`, `tier: tier-2`.

**Source type 6 — Stdin (`-`):**
Прочитать stdin до EOF. Сохранить в `raw/notes/YYYY-MM-DD-HHMMSS-stdin.md` с frontmatter:
`pipeline: raw`, `source_type: note`, `confidence: low`, `tier: tier-3`.
Затем продолжить как plain markdown.

### 2. Определить niche

Прочитать содержимое. Выбрать одну из: `personal`, `business`, `sales`, `life`, `tech`, `meta`.
(6 niches per CLAUDE.md L70 lock; `global` content → Layer 7 `${WIKI_ROOT}/global/` per D1.)
При сомнении — спросить пользователя.

### 3. Извлечь структуру

Выделить из источника 10-15 ключевых элементов по типам:
- **concepts** — фреймворки, идеи, паттерны, модели
- **entities** — конкретные люди, компании, продукты, места
- **claims** — проверяемые утверждения
- **ideas** — что можно сделать
- **foundations** — базовые принципы (редко)

### 4. Dedup-check

Для каждого slug: проверить `${WIKI_ROOT}/concepts/<slug>.md`.
- Если файл существует → читать, добавлять секции (не перезаписывать), обновлять `updated:`, добавлять новый источник в `sources:`.
- Если slug коллизия при другом семантическом содержимом → вызвать `/consolidate` (никогда не перезаписывать).

### 5. Создать / обновить wiki-страницы

Для каждого элемента:
1. Путь: `${WIKI_ROOT}/{type}/{slug}.md`.
2. Взять шаблон из `${WIKI_ROOT}/_templates/{type}.md`, заполнить.
3. Frontmatter: `niche`, `sources: [raw/.../file]`, `related: [...]`, `confidence`, `pipeline: ingested`.
4. В теле — использовать `[[wikilinks]]` на другие страницы wiki.

### 6. Создать карточку источника

`${WIKI_ROOT}/sources/YYYY-MM-DD-<slug>.md` с frontmatter `pipeline: raw → ingested`:
- TL;DR (2 предложения)
- Summary (3-10 предложений)
- 2-5 ключевых цитат
- Списки: concepts/entities/claims/ideas → wikilinks

### 7. Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl`

12-enum per D3 §3.2: `extends | supports | refutes | derived_from | part_of | supersedes | related_to | contradicts | depends_on | illustrates | cites | cross-tree-ref`.
Append-only. Один JSON на строку. Целевой диапазон на инgest: 8-15 новых edges.
Для v3→v2 ссылок → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl`.

### 8. Обновить `${WIKI_ROOT}/index.md`

```
- [Title](path) — one-line summary [niche] [sources: N]
```

Добавить в алфавитном порядке в соответствующей секции.

### 9. Добавить в `${WIKI_ROOT}/log.md` (сверху)

```
## [YYYY-MM-DD] ingest | <source-slug>
Создано: N страниц. Обновлено: M. Edges: K.
Source type: <youtube|pdf|md|web|voice|stdin>.
Niche: <niche>.
Файлы: [[sources/...]], [[concepts/...]], ...
```

### 10. Обновить niche

В `${WIKI_ROOT}/niches/{niche}/README.md` добавить линк на новые страницы.

### 11. Обновить источник

В frontmatter исходного файла: `pipeline: ingested`, `wiki_page: sources/...`.

## Per-ingest success criteria (must hold for every ingest)

- 5-8 concept pages created under `${WIKI_ROOT}/concepts/<slug>.md` (no duplicates; dedup via fs-test).
- 8-15 new edges appended to `${WIKI_ROOT}/graph/edges.jsonl`.
- 1 new row in `${WIKI_ROOT}/log.md` (prepended, newest-on-top per CLAUDE.md convention).
- 1 new row in `${WIKI_ROOT}/index.md` (alphabetic sort preserved).
- Source page under `${WIKI_ROOT}/sources/<slug>.md` with frontmatter `pipeline: raw → ingested`.

## Failure modes

- **URL unreachable** → escalate `{trigger: peer-input-needed, reason: WebFetch-failed}`. Do NOT write empty source.
- **Duplicate slug** → invoke `/consolidate` inline to merge. Never overwrite.
- **OOM on long transcript** → chunk at 100K-token boundaries (Karpathy pattern). Emit partial concept pages; continue in next session.
- **yt-dlp absent** → escalate `{trigger: tool-missing, tool: yt-dlp}`.
- **pdftotext absent** → escalate `{trigger: tool-missing, tool: pdftotext}`.

## Правила

- Не перезаписывать чужие правки. При конфликте — `.new` версию + сообщение.
- Один `/ingest` = один источник.
- Цитаты из источника — обязательно с атрибуцией.

## Выход

```
OK: Ingested <slug>
  Source type: <youtube|pdf|md|web|voice|stdin>
  Niche: ...
  Created: N pages (concepts:..., entities:..., claims:...)
  Updated: M existing pages
  Edges: K new
  Source card: sources/YYYY-MM-DD-slug.md
```
# --- END FILE: .claude/skills/ingest.md ---
```

### A.4.1 — `tools/vtt-to-md.py`

**Target path:** `tools/vtt-to-md.py`

```python
# --- BEGIN FILE: tools/vtt-to-md.py ---
#!/usr/bin/env python3
"""tools/vtt-to-md.py — Convert WebVTT subtitle file to clean markdown transcript.
Usage: python3 tools/vtt-to-md.py <input.vtt> [output.md]
Output: markdown with speaker blocks and timestamps stripped to 1-minute granularity.
"""
import re
import sys
from pathlib import Path


def parse_vtt(vtt_text: str) -> list[str]:
    """Extract cue text blocks from WebVTT, stripping timestamps and tags."""
    cues = []
    lines = vtt_text.splitlines()
    in_cue = False
    buf = []
    for line in lines:
        if re.match(r'^\d{2}:\d{2}', line) or re.match(r'^\d+:\d{2}', line):
            if buf:
                cues.append(' '.join(buf).strip())
                buf = []
            in_cue = True
            continue
        if in_cue and line.strip() == '':
            if buf:
                cues.append(' '.join(buf).strip())
                buf = []
            in_cue = False
            continue
        if in_cue and line.strip() and not line.startswith('WEBVTT'):
            cleaned = re.sub(r'<[^>]+>', '', line).strip()
            if cleaned:
                buf.append(cleaned)
    if buf:
        cues.append(' '.join(buf).strip())
    return [c for c in cues if c]


def deduplicate(cues: list[str]) -> list[str]:
    """Remove consecutive duplicate cue lines (common in auto-generated VTT)."""
    result = []
    prev = None
    for c in cues:
        if c != prev:
            result.append(c)
        prev = c
    return result


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: vtt-to-md.py <input.vtt> [output.md]", file=sys.stderr)
        sys.exit(1)
    vtt_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else vtt_path.with_suffix('.md')
    cues = deduplicate(parse_vtt(vtt_path.read_text(encoding='utf-8')))
    md_lines = ['# Transcript\n', f'_Source: {vtt_path.name}_\n', '']
    md_lines += [c + ' ' for c in cues]
    out_path.write_text('\n'.join(md_lines), encoding='utf-8')
    print(f"OK: {len(cues)} cues written to {out_path}")


if __name__ == '__main__':
    main()
# --- END FILE: tools/vtt-to-md.py ---
```

### A.4.2 — `tools/fetch-and-extract.py`

**Target path:** `tools/fetch-and-extract.py`

```python
# --- BEGIN FILE: tools/fetch-and-extract.py ---
#!/usr/bin/env python3
"""tools/fetch-and-extract.py — Readability-style article extraction from raw HTML/markdown.
Usage: python3 tools/fetch-and-extract.py <url> <raw_content_file_or_-> [output.md]
Reads raw fetched content (HTML or markdown) from file or stdin, extracts article body
via heuristic block detection (<article>/<main>/largest-div), writes clean markdown.
No external dependencies beyond stdlib.
"""
import re
import sys
from pathlib import Path
from datetime import date


def extract_title(content: str) -> str:
    m = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    return m.group(1).strip() if m else 'Untitled'


def strip_tags(html: str) -> str:
    """Minimal tag stripper — replaces block tags with newlines, inlines removed."""
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<br\s*/?>', '\n', html, flags=re.IGNORECASE)
    html = re.sub(r'</(p|div|h[1-6]|li|tr|td|th|blockquote)>', '\n', html, flags=re.IGNORECASE)
    html = re.sub(r'<[^>]+>', '', html)
    html = re.sub(r'&amp;', '&', html)
    html = re.sub(r'&lt;', '<', html)
    html = re.sub(r'&gt;', '>', html)
    html = re.sub(r'&nbsp;', ' ', html)
    html = re.sub(r'&#\d+;', '', html)
    return html


def extract_body(content: str) -> str:
    """Try <article> then <main> then full strip."""
    for tag in ('article', 'main'):
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', content, re.DOTALL | re.IGNORECASE)
        if m:
            return strip_tags(m.group(1))
    return strip_tags(content)


def clean_whitespace(text: str) -> str:
    lines = [l.rstrip() for l in text.splitlines()]
    result = []
    blank_run = 0
    for line in lines:
        if line == '':
            blank_run += 1
            if blank_run <= 2:
                result.append('')
        else:
            blank_run = 0
            result.append(line)
    return '\n'.join(result).strip()


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: fetch-and-extract.py <url> <raw_content_file|-> [output.md]", file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]
    content_src = sys.argv[2]
    content = sys.stdin.read() if content_src == '-' else Path(content_src).read_text(encoding='utf-8', errors='replace')
    out_arg = sys.argv[3] if len(sys.argv) > 3 else None
    title = extract_title(content)
    body = clean_whitespace(extract_body(content))
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower())[:60].strip('-')
    today = date.today().isoformat()
    out_path = Path(out_arg) if out_arg else Path(f'raw/web/{today}-{slug}.md')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = f"""---
title: "{title}"
source: "{url}"
captured: {today}
source_type: web
pipeline: raw
tier: tier-2
---

"""
    out_path.write_text(frontmatter + f'# {title}\n\n' + body, encoding='utf-8')
    print(f"OK: {out_path} ({len(body)} chars)")


if __name__ == '__main__':
    main()
# --- END FILE: tools/fetch-and-extract.py ---
```

**Commit message:** `[km-mvp] extend /ingest skill to 6 source types (youtube/pdf/md/web/voice/stdin) per A1 §4.1`

---

## A.5 — `.claude/skills/ask.md` — OFFLINE_MODE=1 extension

**Target path:** `.claude/skills/ask.md`

**Action:** replace entire file with the content below.

```markdown
# --- BEGIN FILE: .claude/skills/ask.md ---
---
name: ask
description: "Ответить на вопрос по `${WIKI_ROOT}/` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в `${WIKI_ROOT}/comparisons/`. Поддерживает OFFLINE_MODE=1 (structured-excerpt без LLM)."
allowed-tools: Read, Write, Edit, Glob, Grep
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.5"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.2 + UC-10"}
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. Default
> `swarm/wiki/` (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges
> (v3->v2 only) → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
>
> **OFFLINE_MODE=1 (UC-10 Phase-A).** When env-var `OFFLINE_MODE=1` is set,
> Step 2.5 activates: skip LLM synthesis; return structured-excerpt packet
> only. Zero Task() dispatches. Zero outbound network connections.

# Skill: /ask

## Описание

Ответить на содержательный вопрос пользователя по накопленной `${WIKI_ROOT}/`. Не просто поиск —
синтез: связывание идей, выявление противоречий, неочевидные связи.
Когда `OFFLINE_MODE=1` — retrieval-only structured-excerpt (UC-10 Phase-A architectural proof).

## Триггер

`/ask <вопрос>` — вопрос на русском или английском.

## Алгоритм

### 0. Resolve ${WIKI_ROOT} + check OFFLINE_MODE

Прочитать `.claude/config/wiki-roots.yaml`. Применить D7 §7.4 resolution algorithm.
Проверить: если `OFFLINE_MODE=1` (env-var) — активировать Step 2.5 режим.

### 1. Прочитать `${WIKI_ROOT}/index.md`

Это главный навигатор. Не гадай — читай целиком.

### 2. Отобрать 5-15 релевантных страниц (Tier-A/B/C retrieval)

- **Tier-A Direct path.** Если вопрос называет конкретную страницу — читать её напрямую.
- **Tier-B Index+grep.** По заголовку и summary из index.md; grep по ключевым словам в `${WIKI_ROOT}/**/*.md`; нiche-приоритет.
- **Tier-C Typed-BFS depth-2.** Читать `${WIKI_ROOT}/graph/edges.jsonl`; начать с seed-страниц из Tier-B; раскрыть по `extends`, `supports`, `derived_from` до глубины 2.
- Если есть community summaries (`${WIKI_ROOT}/graph/communities.jsonl`) — использовать `top_k_concepts` из релевантных community для быстрого контекста.

### 2.5 — Offline-first gate (UC-10)

**Активируется ТОЛЬКО при `OFFLINE_MODE=1`.**

1. Использовать candidate pages из Tier-A/B/C (шаги выше).
2. Посчитать edge-degree для каждой candidate страницы:
   - `degree = count(edges in edges.jsonl where from == page OR to == page)`.
3. Отсортировать по degree descending; взять top-10.
4. Для каждой из top-10 составить excerpt запись:
   ```
   | rank | slug | title | niche | excerpt (2 sentences from body) | confidence | sources |
   ```
5. Render markdown table + citation list:
   ```markdown
   ## OFFLINE_MODE=1 — Structured Excerpt

   Query: "<запрос>"

   | # | Page | Niche | Excerpt | Confidence |
   |---|------|-------|---------|------------|
   | 1 | [src:concepts/foo.md] | tech | "..." | high |
   ...

   ### Citations
   - [src:concepts/foo.md] — <title>
   - [src:sources/bar.md] — <title>
   ...
   ```
6. Добавить в `${WIKI_ROOT}/log.md` (сверху):
   ```
   ## [YYYY-MM-DD HH:MM] ask | OFFLINE_MODE=1 | <slug-of-query>
   OFFLINE_MODE=1 query: '<запрос>' → 10 excerpts returned; zero LLM calls.
   ```
7. **НЕ писать в `${WIKI_ROOT}/comparisons/`** — filing loop только при LLM synthesis.
8. **НЕ вызывать Task()** с любым intent на генерацию. Zero LLM dispatches.
9. Вернуть markdown response ≤2KB с ≥3 `[src:...]` citations. **STOP — не идти дальше.**

**Network verification (operational note):**
Для аудита можно запустить рядом с сессией:
```bash
tcpdump -n 'tcp port 443 and host not 127.0.0.1'
# OR (socket-level, no root required):
ss -tnp 'dport = :443'
```
Ожидаемый результат при `OFFLINE_MODE=1`: zero connections на :443 к внешним хостам.
Проверочный скрипт: `swarm/tests/uc-ask-offline.sh`.

### 3. Прочитать отобранные страницы (только если OFFLINE_MODE не активен)

Полностью. Следи за wikilinks — при необходимости иди глубже (но не более 2 уровней).

### 4. Синтезировать ответ (только если OFFLINE_MODE не активен)

```
## Короткий ответ
<1-3 предложения>

## Детали
<3-10 предложений с цитатами в формате [src:file.md]>

## Что противоречиво / открыто
<если есть>

## Откуда это
- [src:sources/...] — что оттуда
- [src:concepts/...]
```

- Цитируй точными wikilink'ами в формате `[src:path.md]`.
- Разделяй: что из wiki vs. что ты добавляешь от себя.
- Если данных мало — честно сказать.

### 5. Оценить ценность ответа

**Сохранить в `${WIKI_ROOT}/comparisons/`** если ответ:
- даёт новую связь между 2+ страницами, которой раньше не было;
- выявляет противоречие между источниками;
- обобщает по 5+ страницам;
- даёт практический вывод, который стоит запомнить.

**Не сохранять** если ответ — простой lookup. **Не сохранять при OFFLINE_MODE=1.**

### 6. Сохранение (если нужно и OFFLINE_MODE не активен)

`${WIKI_ROOT}/comparisons/YYYY-MM-DD-question-slug.md`:

```yaml
---
title: "<сокращённый вопрос>"
type: comparison
question: "<полный вопрос>"
niche: ...
sources: [...]
related: [...]
tags: [#type/comparison]
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: medium
pipeline: ready
---
```

Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl` per D3 12-enum.

### 7. Обновить index.md и log.md

Если сохранили:
- В `index.md` — секция `## Comparisons`: `- [title](comparisons/...) — 1 line [niche]`.
- В `log.md` (сверху): `## [YYYY-MM-DD] ask | <slug>` + какие страницы затронуты.

### 8. Вывести ответ пользователю

Сначала ответ. В конце — "(сохранено в `comparisons/...`)" если сохранили, иначе ничего.

## Правила

- Не выдумывать факты. Если в wiki нет — сказать "в wiki пока нет".
- Не пересказывать содержимое страниц — отвечай на вопрос.
- Один `/ask` = один синтез.
- При `OFFLINE_MODE=1` — НИКАКИХ LLM calls, НИКАКИХ Task() dispatches, НИКАКИХ записей в comparisons/.
# --- END FILE: .claude/skills/ask.md ---
```

**Acceptance predicate (Hamel-binary):**
`OFFLINE_MODE=1 /ask "<any query>"` produces a markdown response of ≤2KB containing ≥3 [src:...] citations AND zero Task() dispatches (grep skill-invocation log for Task calls — expect zero) AND `${WIKI_ROOT}/log.md` gains exactly 1 new row matching `OFFLINE_MODE=1 query:`.

**Commit message:** `[km-mvp] add OFFLINE_MODE=1 structured-excerpt path to /ask skill (UC-10 Phase-A architectural proof)`

---

## A.7 — `.claude/skills/consolidate.md` — `--weekly` extension

**Target path:** `.claude/skills/consolidate.md`

**Action:** replace entire file with the content below.

```markdown
# --- BEGIN FILE: .claude/skills/consolidate.md ---
---
name: consolidate
description: "Найти дубликаты в `${WIKI_ROOT}/` и предложить merge. Поддерживает --weekly (ISO-week digest), --dry-run, --quiet."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.7"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§5 UC-2"}
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3->v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /consolidate

## Описание

Объединение дубликатов в `${WIKI_ROOT}/`. Не мержит автоматически — всегда confirm от пользователя.
Флаг `--weekly` генерирует ISO-week digest вместо dedup scan.

## Триггер

- `/consolidate` — пройтись по всей wiki (dedup scan).
- `/consolidate <type>` — только один type.
- `/consolidate <niche>` — только в одном niche.
- `/consolidate --weekly` — сгенерировать weekly digest.
- `/consolidate --weekly --dry-run` — вывести digest в stdout, не писать файл.
- `/consolidate --weekly --quiet` — писать файл без progress logs.

## Алгоритм A — Dedup scan (default, без --weekly)

### 1. Собрать кандидатов

Попарная проверка внутри одного type:
1. Одинаковые/похожие `title` (normalized: lowercase, без пробелов/дефисов).
2. Одинаковые/похожие slug.
3. 70%+ пересечения по словам в теле.
4. Одинаковая entity_kind / topic.

### 2. Для каждой пары — diff

```
CANDIDATE MERGE:
  A: ${WIKI_ROOT}/concepts/value-based-pricing.md (4 sources, 120 lines)
  B: ${WIKI_ROOT}/concepts/value-pricing.md (2 sources, 80 lines)
  Reason: 85% overlap, похожий title
  A unique: [...], B unique: [...], Common: [...]
  Predлагаемый merge: A остаётся, B мержится в A. Ссылки на B: N файлов.
  [y] merge, [n] skip, [s] skip all similar
```

### 3. После confirm (`y`)

1. Объединить frontmatter (title — длиннее; sources/related/tags — union; confidence — минимум; updated — сегодня).
2. Объединить тело (уникальные секции из обоих; общие — из A).
3. Обновить внешние ссылки (grep `[[B]]` → заменить на A в edges.jsonl + cross-tree.jsonl + index.md).
4. Архивировать B в `${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md` с HTML-комментом:
   `<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->`.
   (brigadier затем: `state: superseded` + `superseded_by: [[A]]` per D5.)
5. Логировать в `${WIKI_ROOT}/log.md` (сверху):
   ```
   ## [YYYY-MM-DD] consolidate | merge | A <- B
   A: ${WIKI_ROOT}/concepts/...  B (archived): _archive/YYYY-MM-DD-B.md
   Updated refs in: N files
   ```

### 4. Skip / Skip all

- `n` — пропустить пару, продолжить.
- `s` — пропустить все похожие данного type в текущей сессии.

## Алгоритм B — Weekly digest (`--weekly`)

### B.1 Определить ISO-неделю

```python
import datetime
today = datetime.date.today()
iso_year, iso_week, _ = today.isocalendar()
week_label = f"{iso_year}-W{iso_week:02d}"  # e.g. "2026-W17"
```

### B.2 Walk log.md for last 7 days

Прочитать `${WIKI_ROOT}/log.md`. Извлечь все записи с датами в диапазоне `[today-7d, today]`.
Из каждой записи извлечь: niche, created page slugs, edge counts.

### B.3 Группировка по niche + top-5

Для каждого из 6 niches (personal/business/sales/life/tech/meta):
- Собрать все страницы, созданные/обновлённые за 7 дней.
- Вычислить edge-degree каждой (из edges.jsonl, `from == page OR to == page`).
- Взять top-5 по degree.

### B.4 Emergent theme clusters

Из edges.jsonl взять только записи с `ts >= today-7d` (7-дневный подграф).
Найти связные компоненты (BFS/DFS по смежности from/to) в этом подграфе.
Clusters ≥3 nodes = "emergent theme". Имя кластера = slug с максимальным degree.

### B.5 Render digest

```markdown
---
title: "Weekly digest <week_label>"
type: digest
week: <week_label>
created: <today>
niche: meta
pipeline: ready
state: accepted
confidence: medium
confidence_method: automated-log-walk
tier: tier-internal
produced_by: consolidate-weekly
sources:
  - {path: "${WIKI_ROOT}/log.md", range: "last 7 days"}
  - {path: "${WIKI_ROOT}/graph/edges.jsonl", range: "ts >= <today-7d>"}
---

# Weekly digest <week_label>

## New pages this week (by niche)

### personal (N pages)
- [Page title](concepts/slug.md) — edge-degree: D

### business (N pages)
...

## Top edges this week

| From | To | Type | Count |
|------|----|------|-------|
| [src:...] | [src:...] | supports | 3 |

## Emergent themes (clusters >=3 nodes)

### Theme: <cluster-name>
Pages: [A], [B], [C], ...
Dominant edge types: supports(3), derived_from(2)

## Citations resolved

N new sources[] entries pointing to existing wiki pages this week.

---
_Generated by /consolidate --weekly at <datetime>. Zero LLM calls._
```

**Empty-week handling:** if no new pages — render "no new pages this week" in all sections
and still write the file (cron-idempotent).

### B.6 Write or dry-run

- `--dry-run`: вывести digest в stdout; не писать файл; не обновлять log.
- Default: записать в `${WIKI_ROOT}/digests/<week_label>.md`.
- `--quiet`: писать файл без промежуточных progress logs.

### B.7 Append log row

```
## [YYYY-MM-DD] consolidate | weekly | <week_label>
weekly digest <week_label> generated; N pages summarised.
```

## Правила

- Никогда не мержить без `y` (dedup mode).
- Никогда не удалять без архива.
- Не трогать `_templates/`, `index.md`, `log.md`, `niches/*/README.md`.
- Если у страницы 10+ входящих ссылок — двойной confirm (dedup mode).
- `--weekly` никогда не мержит / не удаляет страницы; только читает и пишет digest.

## Cron-ready wiring

Файл документации расписания (НЕ устанавливается автоматически):
`tools/cron/consolidate-weekly.cron`

```cron
# /consolidate --weekly — Sunday 21:00 CET (UTC+1 CET = UTC+2 CEST in summer)
# Run from repo root. Requires: WIKI_ROOT env-var set or default swarm/wiki/.
# NOT auto-installed; operator activates via: crontab tools/cron/consolidate-weekly.cron
0 19 * * 0 cd /path/to/jetix-os && /consolidate --weekly --quiet
```

## Отчёт после сессии

```
Dedup mode: рассмотрено N пар, смерджено M, скипнуто K.
Weekly mode: digest <week_label> written to ${WIKI_ROOT}/digests/<week_label>.md.
```
# --- END FILE: .claude/skills/consolidate.md ---
```

**Commit message:** `[km-mvp] extend /consolidate with --weekly flag producing ISO-week digests per A1 §5 UC-2`

---

## A.8 — `.claude/skills/build-graph.md` — operational Louvain-equivalent

**Target path:** `.claude/skills/build-graph.md`

**Action:** replace entire file with the content below. Also create `tools/community-detect.py` (body in sub-section A.8.1).

```markdown
# --- BEGIN FILE: .claude/skills/build-graph.md ---
---
name: build-graph
description: "Читать edges.jsonl → in-memory adjacency → Louvain-equivalent greedy modularity community detection → communities.jsonl → health.md rollup. Modes: default (full rebuild), --since=<ISO-date> (incremental), --dry-run."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.8"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.2 Tier-C"}
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3->v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /build-graph

## Описание

Обновить граф знаний поверх `${WIKI_ROOT}/`. Идемпотентно.
Community detection via Louvain-equivalent greedy modularity (pure Python dict-of-lists; no networkx).
Target performance: <5s on Phase-A wiki (~50 edges, ~20 pages).

## Триггер

- `/build-graph` — полный пересчёт.
- `/build-graph --since=<ISO-date>` — инкрементальный (только edges с `ts >= <ISO-date>`).
- `/build-graph --dry-run` — вывести community count без записи файлов.
- `/build-graph --edges-only` — только добрать edges, не трогать communities.
- `/build-graph --tree {v2|v3|both}` — выбор tree per T1.

## Алгоритм

### 1. Resolve ${WIKI_ROOT} + parse arguments

Прочитать wiki-roots.yaml. Определить режим: full / incremental / dry-run / edges-only.
Для `--since=<ISO-date>`: фильтровать edges с `ts >= <ISO-date>`.

### 2. Загрузить edges.jsonl

Прочитать `${WIKI_ROOT}/graph/edges.jsonl` (и `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` при `--tree=both`).
Пропустить строки-комментарии (начинающиеся с `#`). Парсить JSONL.
Для incremental — отфильтровать по `ts`.

### 3. Собрать все страницы

Glob `${WIKI_ROOT}/**/*.md`, исключить: `index.md`, `log.md`, `overview.md`,
`_templates/*`, `niches/*/README.md`, `graph/*`, `_archive/*`.

### 4. Построить карту упоминаний (для --edges-only или full)

Для каждой страницы P:
- Grep по `[[slug]]` и `[text](relative-path)` в её теле.
- Собрать `mentioned_by[P] = [...]`.

### 5. Добить edges (если не --dry-run)

Для каждой пары (A → B) с перекрёстным упоминанием, не представленной в edges.jsonl:
- Определить тип per D3 12-enum.
- Append в `${WIKI_ROOT}/graph/edges.jsonl`.

### 6. Community detection

Запустить `python3 tools/community-detect.py <edges_jsonl_path> <output_communities_jsonl_path>`.

Алгоритм в `tools/community-detect.py` (≤80 LoC):
- Читать edges → in-memory undirected adjacency dict-of-lists.
- **Greedy modularity (Louvain-equivalent):** начать с каждого нода в своей community.
  Итерировать: для каждого нода попробовать переместить в community соседа, если
  модулярность Q растёт. Повторять до сходимости (delta_Q < 1e-6 OR max_iter=100).
  Формула Q: `(e_c / m) - (k_c / (2m))^2` где e_c = internal edges, k_c = sum of degrees, m = total edges.
- Для каждой community определить `dominant_niche` (mode of niche frontmatter values nodes).
- `top_k_concepts`: top-3 nodes by degree в community.
- Записать `${WIKI_ROOT}/graph/communities.jsonl`:
  ```jsonl
  {"community_id": "C1", "node_count": 5, "nodes": ["concepts/foo.md", ...], "dominant_niche": "tech", "top_k_concepts": ["concepts/foo.md", "concepts/bar.md", "concepts/baz.md"]}
  ```

При `--dry-run`: вывести community count в stdout; не записывать communities.jsonl.

### 7. Обновить `${WIKI_ROOT}/meta/health.md`

Прочитать health.md. Обновить секцию community stats:
```
community_count: N
largest_community_size: M
last_build_graph: YYYY-MM-DD HH:MM
```

### 8. Залогировать

В `${WIKI_ROOT}/log.md` (сверху):
```
## [YYYY-MM-DD] build-graph | edges: +N / total M | communities: K | mode: full|incremental|dry-run
```

## Правила

- Append-only для edges.jsonl. Никогда не удалять вручную.
- Confidence edge-а по умолчанию `medium`. `high` — если в обеих страницах явная секция.
- Не создавать edges к `_templates/*` и системным файлам.
- При `--dry-run` — нулевых записей в любой файл.

## Acceptance

На Phase-A wiki (~50 edges, ~20 pages): `/build-graph` завершается в <5s
и производит непустой communities.jsonl (≥1 community record).
Проверка: `grep -c '^\{' ${WIKI_ROOT}/graph/communities.jsonl`.
# --- END FILE: .claude/skills/build-graph.md ---
```

### A.8.1 — `tools/community-detect.py`

**Target path:** `tools/community-detect.py`

```python
# --- BEGIN FILE: tools/community-detect.py ---
#!/usr/bin/env python3
"""tools/community-detect.py — Louvain-equivalent greedy modularity community detection.
Pure Python dict-of-lists; no networkx or scipy dependency.
Usage: python3 tools/community-detect.py <edges.jsonl> <output-communities.jsonl> [--niche-map=<frontmatter-dir>]
Target: <5s on Phase-A wiki (~50 edges, ~20 nodes).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_edges(path: str) -> list[tuple[str, str]]:
    edges = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                rec = json.loads(line)
                edges.append((rec['from'], rec['to']))
            except (json.JSONDecodeError, KeyError):
                continue
    return edges


def build_adjacency(edges: list[tuple[str, str]]) -> tuple[dict, list]:
    adj: dict[str, set] = defaultdict(set)
    nodes_set: set[str] = set()
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        nodes_set.add(u)
        nodes_set.add(v)
    nodes = sorted(nodes_set)
    return dict(adj), nodes


def compute_modularity(communities: dict[str, int], adj: dict, m: int) -> float:
    if m == 0:
        return 0.0
    degrees = {n: len(adj.get(n, [])) for n in communities}
    community_members: dict[int, list] = defaultdict(list)
    for node, c in communities.items():
        community_members[c].append(node)
    Q = 0.0
    for members in community_members.values():
        member_set = set(members)
        e_c = sum(1 for u in members for v in adj.get(u, []) if v in member_set) / 2
        k_c = sum(degrees.get(u, 0) for u in members)
        Q += (e_c / m) - (k_c / (2 * m)) ** 2
    return Q


def greedy_modularity(adj: dict, nodes: list, max_iter: int = 100) -> dict[str, int]:
    """Louvain-equivalent greedy phase-1: move each node to best-neighbor community."""
    communities = {n: i for i, n in enumerate(nodes)}
    m = sum(len(nb) for nb in adj.values()) // 2
    if m == 0:
        return communities
    improved = True
    iteration = 0
    while improved and iteration < max_iter:
        improved = False
        iteration += 1
        for node in nodes:
            current_comm = communities[node]
            neighbor_comms = {communities[nb] for nb in adj.get(node, [])}
            if not neighbor_comms:
                continue
            best_comm = current_comm
            best_q = compute_modularity(communities, adj, m)
            for nc in neighbor_comms:
                if nc == current_comm:
                    continue
                communities[node] = nc
                q = compute_modularity(communities, adj, m)
                if q > best_q + 1e-6:
                    best_q = q
                    best_comm = nc
            communities[node] = best_comm
            if best_comm != current_comm:
                improved = True
    return communities


def communities_to_records(communities: dict[str, int], adj: dict) -> list[dict]:
    groups: dict[int, list] = defaultdict(list)
    for node, c in communities.items():
        groups[c].append(node)
    records = []
    for i, (comm_id, members) in enumerate(sorted(groups.items())):
        member_set = set(members)
        degrees = {n: len([nb for nb in adj.get(n, []) if nb in member_set]) for n in members}
        top_k = sorted(members, key=lambda n: degrees[n], reverse=True)[:3]
        records.append({
            "community_id": f"C{i + 1}",
            "node_count": len(members),
            "nodes": sorted(members),
            "dominant_niche": "unknown",  # populated by skill if frontmatter available
            "top_k_concepts": top_k,
        })
    return sorted(records, key=lambda r: r['node_count'], reverse=True)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: community-detect.py <edges.jsonl> <output-communities.jsonl>", file=sys.stderr)
        sys.exit(1)
    edges_path = sys.argv[1]
    out_path = sys.argv[2]
    edges = load_edges(edges_path)
    adj, nodes = build_adjacency(edges)
    communities = greedy_modularity(adj, nodes)
    records = communities_to_records(communities, adj)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f"OK: {len(records)} communities written to {out_path}")
    print(f"Largest: {records[0]['node_count'] if records else 0} nodes")


if __name__ == '__main__':
    main()
# --- END FILE: tools/community-detect.py ---
```

**Commit message:** `[km-mvp] operationalize /build-graph with Louvain-equivalent community detection (A1 §4.2 Tier-C seed)`

---

## A.9 — `.claude/skills/lint.md` — 5 new signals

**Target path:** `.claude/skills/lint.md`

**Action:** append the 5 new check sections (after check #13) to the existing file body. The sections below are additive; the existing 13 checks are preserved unchanged. Brigadier inserts these sections before the `## Выход` section.

```markdown
<!-- --- BEGIN INSERTION: .claude/skills/lint.md — 5 new signals (append before ## Выход) --- -->

### 14. L-DANGLING-EDGE — dangling edge detection

For each record in `${WIKI_ROOT}/graph/edges.jsonl` (skip comment lines):
- Parse `from` and `to` fields.
- Resolve both as paths relative to `${WIKI_ROOT}` (strip leading `../` segments for cross-tree refs first).
- For intra-tree edges: check `os.path.exists(${WIKI_ROOT}/<from>)` AND `os.path.exists(${WIKI_ROOT}/<to>)`.
- For cross-tree refs (`type: cross-tree-ref`): check only that the `from` file exists (destination is in v2 tree; checked separately).

**Flag:** `L-DANGLING-EDGE` — edge at line N: from <from> OR to <to> does not exist.

**Severity:** HIGH (dangling edges corrupt Tier-C BFS retrieval).

**Bash implementation (illustrative; skill runs in-session):**
```bash
#!/usr/bin/env bash
# lint check 14: L-DANGLING-EDGE
# Usage: called inline by /lint with WIKI_ROOT set
set -euo pipefail
WIKI_ROOT="${WIKI_ROOT:-swarm/wiki}"
EDGES="${WIKI_ROOT}/graph/edges.jsonl"
dangling=0
lineno=0
while IFS= read -r line; do
  lineno=$((lineno+1))
  [[ "$line" =~ ^\# ]] && continue
  [[ -z "$line" ]] && continue
  from=$(echo "$line" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('from',''))" 2>/dev/null || true)
  to=$(echo "$line"   | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('to',''))"   2>/dev/null || true)
  edge_type=$(echo "$line" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('type',''))" 2>/dev/null || true)
  check_path() {
    local p="$1"
    [[ "$p" == ../* ]] && p="${p#../}"
    [[ -f "$p" ]] || { echo "L-DANGLING-EDGE: line $lineno: $p not found"; return 1; }
  }
  check_path "$from" || dangling=$((dangling+1))
  [[ "$edge_type" != "cross-tree-ref" ]] && { check_path "$to" || dangling=$((dangling+1)); }
done < "$EDGES"
echo "L-DANGLING-EDGE: $dangling dangling edges found"
exit $dangling
```

### 15. L-ORPHAN-CONCEPT — orphan concept detection

For each `.md` file under `${WIKI_ROOT}/concepts/`:
- Check whether it has ≥1 inbound OR outbound edge in `${WIKI_ROOT}/graph/edges.jsonl`
  (i.e., any record where `from` or `to` matches this file's path relative to `${WIKI_ROOT}`).

**Flag:** `L-ORPHAN-CONCEPT` — `concepts/<slug>.md` has zero edges (inbound+outbound).

**Severity:** MEDIUM (orphan concepts are unreachable via Tier-C BFS; may indicate stale pages or missed edges after ingest).

**Exclusions:** `concepts/_index.md` if present.

### 16. L-MISSING-FRONTMATTER — mandatory field enforcement

For each `.md` file under `${WIKI_ROOT}/` (excluding `index.md`, `log.md`, `_templates/*`, `graph/*`, `_archive/*`, `niches/*/README.md`):
- Parse YAML frontmatter (content between first `---` delimiters).
- Verify ALL mandatory fields present (non-null, non-empty):
  `title`, `type`, `created`, `pipeline`, `state`, `confidence`, `confidence_method`, `tier`, `produced_by`, `sources`.

**Flag:** `L-MISSING-FRONTMATTER` — `<path>`: missing fields: [field1, field2, ...].

**Severity:** HIGH (missing frontmatter breaks Tier-B grep filtering + provenance gate §2).

**Note:** `sources: []` (empty list) is acceptable only for bootstrap/seed pages (`pipeline: raw`). For `pipeline ∈ {compiled, linted, ready, accepted}`, `sources` must be non-empty.

### 17. L-DUPLICATE-SLUG — cross-subtree duplicate basename detection

Walk all `.md` files under `${WIKI_ROOT}/`. Group by `basename` (filename without directory).
For each basename appearing ≥2 times in different subdirectories:
- If files are symlinks pointing to the same target → acceptable (intentional per-niche symlink). Skip.
- Otherwise → flag.

**Flag:** `L-DUPLICATE-SLUG` — basename `<slug>.md` appears at: <path1>, <path2>.

**Severity:** MEDIUM (may indicate accidental duplication; may cause Tier-B grep to return two pages for one slug).

**Exclusions:** `index.md`, `log.md`, `README.md`, `health.md` (expected in multiple dirs).

### 18. L-CROSS-CLIENT-GLOBAL — cross-client global contamination (hard error)

**Activates only when `WIKI_ROOT_CLIENT_ID` env-var is set** (i.e., skill is running in client-scoped mode).

For each `.md` file under `${WIKI_ROOT}/global/`:
- Parse frontmatter `granularity:` field.
- If `granularity` matches `client:*` pattern → HARD ERROR.

**Flag:** `L-CROSS-CLIENT-GLOBAL` — `global/<path>`: artefact has granularity `<value>` which is client-scoped; global/ must only contain `granularity: jetix-internal` OR `granularity: global`.

**Severity:** HARD ERROR — triggers non-zero exit immediately; does not wait for full scan completion. Per A1 §5 UC-9 Layer-2: client-scoped content in global/ is a data-leak vector.

---

## Обновлённый report target

Lint report писать в `${WIKI_ROOT}/meta/lint-report-<YYYY-MM-DD>.md`
(изменена с `${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md` per A.9 spec — путь теперь под `meta/` для health.md интеграции).

Non-zero exit: если ANY hard-error check (broken links, L-MISSING-FRONTMATTER HIGH,
L-CROSS-CLIENT-GLOBAL, L-DANGLING-EDGE count > 0) fired.

Обновить Summary-секцию report:
```
## Summary
- L-DANGLING-EDGE: N
- L-ORPHAN-CONCEPT: N
- L-MISSING-FRONTMATTER: N
- L-DUPLICATE-SLUG: N
- L-CROSS-CLIENT-GLOBAL: N (HARD ERROR if >0 in client-scoped mode)
```

Обновить log.md entry:
```
## [YYYY-MM-DD] lint | report | issues: N | hard-errors: M
```
<!-- --- END INSERTION: .claude/skills/lint.md --- -->
```

**Commit message:** `[km-mvp] extend /lint with 5 new signals (L-DANGLING-EDGE, L-ORPHAN-CONCEPT, L-MISSING-FRONTMATTER, L-DUPLICATE-SLUG, L-CROSS-CLIENT-GLOBAL)`

---

## Part A smoke test — `swarm/tests/part-a-smoke.sh`

**Target path:** `swarm/tests/part-a-smoke.sh`

**Action:** create file with content below; then `chmod +x swarm/tests/part-a-smoke.sh`.

```bash
# --- BEGIN FILE: swarm/tests/part-a-smoke.sh ---
#!/usr/bin/env bash
# swarm/tests/part-a-smoke.sh — Part A smoke test for KM MVP materialization.
# Verifies A.1-A.9 artefacts exist and carry required content.
# Usage: bash swarm/tests/part-a-smoke.sh  (from repo root)
# Captures output to swarm/tests/results/part-a-smoke-<date>.log
# Exit code: 0 = all pass; 1 = at least one failure.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

LOG_DIR="swarm/tests/results"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/part-a-smoke-$(date +%Y-%m-%d).log"
PASS=0
FAIL=0

check() {
  local label="$1"
  local result="$2"
  if [[ "$result" -eq 0 ]]; then
    echo "PASS: ${label}" | tee -a "$LOG_FILE"
    PASS=$((PASS+1))
  else
    echo "FAIL: ${label}" | tee -a "$LOG_FILE"
    FAIL=$((FAIL+1))
  fi
}

echo "=== Part A smoke test $(date) ===" | tee -a "$LOG_FILE"

# A.1: wiki-roots.yaml has clients: stanza with schema_version: 2
python3 -c "
import yaml, sys
d = yaml.safe_load(open('.claude/config/wiki-roots.yaml'))
assert d.get('schema_version') == 2, 'schema_version != 2'
assert 'clients' in d, 'clients stanza missing'
assert 'demo-client-a' in d['clients'], 'demo-client-a missing'
assert 'demo-client-b' in d['clients'], 'demo-client-b missing'
print('A.1 OK: schema_version=2, clients stanza present')
"
check "A.1 wiki-roots.yaml schema_version:2 + clients: stanza" $?

# A.2: demo-client directories scaffolded
test -d clients/demo-client-a/swarm/wiki/concepts
check "A.2 demo-client-a/swarm/wiki/concepts exists" $?

test -d clients/demo-client-b/swarm/wiki/graph
check "A.2 demo-client-b/swarm/wiki/graph exists" $?

test -f clients/demo-client-a/swarm/wiki/index.md
check "A.2 demo-client-a index.md exists" $?

test -f clients/demo-client-b/swarm/wiki/graph/edges.jsonl
check "A.2 demo-client-b edges.jsonl exists" $?

# A.3: >=50 edges in edges.jsonl
EDGE_COUNT=$(grep -cE '^\{' swarm/wiki/graph/edges.jsonl 2>/dev/null || echo 0)
[[ "$EDGE_COUNT" -ge 50 ]]
check "A.3 edges.jsonl has >=50 records (found: ${EDGE_COUNT})" $?

# A.4: /ingest skill has yt-dlp branch
grep -q 'yt-dlp' .claude/skills/ingest.md
check "A.4 ingest.md contains yt-dlp branch" $?

grep -q 'pdftotext' .claude/skills/ingest.md
check "A.4 ingest.md contains pdftotext branch" $?

grep -q 'source type 6\|stdin' .claude/skills/ingest.md
check "A.4 ingest.md contains stdin branch" $?

test -f tools/vtt-to-md.py
check "A.4 tools/vtt-to-md.py exists" $?

test -f tools/fetch-and-extract.py
check "A.4 tools/fetch-and-extract.py exists" $?

# A.5: /ask skill has OFFLINE_MODE=1 path
grep -q 'OFFLINE_MODE' .claude/skills/ask.md
check "A.5 ask.md contains OFFLINE_MODE" $?

grep -q 'Step 2.5\|offline-first' .claude/skills/ask.md
check "A.5 ask.md contains Step 2.5 offline gate" $?

grep -q 'tcpdump\|ss -tnp' .claude/skills/ask.md
check "A.5 ask.md contains network verification probe" $?

# A.7: /consolidate has --weekly flag
grep -q '\-\-weekly' .claude/skills/consolidate.md
check "A.7 consolidate.md contains --weekly flag" $?

grep -q '\-\-dry-run' .claude/skills/consolidate.md
check "A.7 consolidate.md contains --dry-run flag" $?

grep -q 'ISO-week\|iso_week\|week_label' .claude/skills/consolidate.md
check "A.7 consolidate.md contains ISO-week logic" $?

# A.8: /build-graph has communities.jsonl + Louvain reference
grep -q 'communities.jsonl' .claude/skills/build-graph.md
check "A.8 build-graph.md contains communities.jsonl" $?

grep -iqE 'louvain|greedy modularity|community.detect' .claude/skills/build-graph.md
check "A.8 build-graph.md contains Louvain/community-detect reference" $?

test -f tools/community-detect.py
check "A.8 tools/community-detect.py exists" $?

python3 -c "import ast; ast.parse(open('tools/community-detect.py').read()); print('syntax OK')"
check "A.8 tools/community-detect.py parses without syntax errors" $?

# A.9: /lint has new signals
grep -q 'L-DANGLING-EDGE' .claude/skills/lint.md
check "A.9 lint.md contains L-DANGLING-EDGE" $?

grep -q 'L-ORPHAN-CONCEPT' .claude/skills/lint.md
check "A.9 lint.md contains L-ORPHAN-CONCEPT" $?

grep -q 'L-MISSING-FRONTMATTER' .claude/skills/lint.md
check "A.9 lint.md contains L-MISSING-FRONTMATTER" $?

grep -q 'L-DUPLICATE-SLUG' .claude/skills/lint.md
check "A.9 lint.md contains L-DUPLICATE-SLUG" $?

grep -q 'L-CROSS-CLIENT-GLOBAL' .claude/skills/lint.md
check "A.9 lint.md contains L-CROSS-CLIENT-GLOBAL" $?

# Shebang + set -euo pipefail checks on all bash scripts
for script in tools/bootstrap-demo-clients.sh swarm/tests/part-a-smoke.sh; do
  head -2 "$script" | grep -q 'set -euo pipefail'
  check "set -euo pipefail in ${script}" $?
done

# No API key references in any new artefact
KEYCHECK=$(grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY' \
  .claude/skills/ingest.md .claude/skills/ask.md .claude/skills/consolidate.md \
  .claude/skills/build-graph.md .claude/skills/lint.md \
  tools/vtt-to-md.py tools/fetch-and-extract.py tools/community-detect.py \
  tools/bootstrap-demo-clients.sh 2>/dev/null || true)
[[ -z "$KEYCHECK" ]]
check "No provider API-key references in new artefacts" $?

echo "" | tee -a "$LOG_FILE"
echo "=== Results: PASS=${PASS} FAIL=${FAIL} ===" | tee -a "$LOG_FILE"

if [[ "$FAIL" -gt 0 ]]; then
  echo "Part A smoke: FAIL — fix before Part B" | tee -a "$LOG_FILE"
  exit 1
fi

echo "Part A smoke: PASS" | tee -a "$LOG_FILE"
exit 0
# --- END FILE: swarm/tests/part-a-smoke.sh ---
```

**chmod mandate:** `chmod +x swarm/tests/part-a-smoke.sh`

**Commit message:** `[km-mvp] add swarm/tests/part-a-smoke.sh (Part A gate verification per §2.A smoke block)`

---

## Integration notes for brigadier

### Execution order (parallelizable per A1 §9 staging order)

```
Batch 1 (parallel):
  - A.1: overwrite .claude/config/wiki-roots.yaml (config; no deps)
  - A.4: overwrite .claude/skills/ingest.md; create tools/vtt-to-md.py + tools/fetch-and-extract.py
  - A.5: overwrite .claude/skills/ask.md
  - A.7: overwrite .claude/skills/consolidate.md
  - A.8: overwrite .claude/skills/build-graph.md; create tools/community-detect.py
  - A.9: insert 5 signal sections into .claude/skills/lint.md (before ## Выход section)

Batch 2 (after Batch 1):
  - A.2: create tools/bootstrap-demo-clients.sh; chmod +x; run it (depends on A.1 clients: stanza)
  - A.3: append 60 JSONL records to swarm/wiki/graph/edges.jsonl
  - Create swarm/tests/results/ directory; create + chmod +x swarm/tests/part-a-smoke.sh

Batch 3 (gate):
  - Run: bash swarm/tests/part-a-smoke.sh
  - Capture output to swarm/tests/results/part-a-smoke-2026-04-24.log
  - If exit 0: proceed to Part B commit sequence
  - If exit 1: fix failing checks before committing Part B artefacts
```

### Commit sequence (one commit per logical unit)

1. `[km-mvp] extend wiki-roots.yaml with clients: stanza for UC-9 Phase-A isolation (+ demo-client-a/-b fixture)`
2. `[km-mvp] add tools/bootstrap-demo-clients.sh (idempotent demo holon scaffolding for UC-9 test fixture)`
3. `[km-mvp] populate edges.jsonl with 60 typed edges across existing wiki content (A1 §4.2 Tier-C seed)`
4. `[km-mvp] extend /ingest skill to 6 source types (youtube/pdf/md/web/voice/stdin) per A1 §4.1`
5. `[km-mvp] add OFFLINE_MODE=1 structured-excerpt path to /ask skill (UC-10 Phase-A architectural proof)`
6. `[km-mvp] extend /consolidate with --weekly flag producing ISO-week digests per A1 §5 UC-2`
7. `[km-mvp] operationalize /build-graph with Louvain-equivalent community detection (A1 §4.2 Tier-C seed)`
8. `[km-mvp] extend /lint with 5 new signals (dangling-edge, orphan-concept, missing-frontmatter, duplicate-slug, cross-client-global)`
9. `[km-mvp] add swarm/tests/part-a-smoke.sh (Part A gate verification per §2.A smoke block)`

### Anti-scope for this draft

- Not implementing Part B (B2 rich mini-swarm) — separate wave.
- Not implementing A.6 (ollama+Mistral-7B-Q4 Phase-B stack) — deferred; time-permitting note in §2.A §A.6.
- Not creating the 13th edge type `holon-ref` — AWAITING-APPROVAL per D3 §3.5.
- Not writing to swarm/wiki/<canonical>/ — drafts scope only; brigadier promotes.
- Not touching legacy wiki/ v2 tree or 14 legacy .claude/agents/*.md files.

---

## Integrator synthesis notes

**Claim 1.** The wiki-roots.yaml `clients:` stanza + `WIKI_ROOT_CLIENT_ID` env-var convention requires zero skill-body rewrites to the existing 5 skills for UC-9 Phase-A isolation — confirmed by reading `.claude/skills/ingest.md` + `.claude/skills/ask.md` (both already use `${WIKI_ROOT}` resolution).
**F:** F4 (operational convention — read from both skill files 2026-04-24).
**ClaimScope:** holds for Phase-A 5-skill set; Phase-B may need UNIX-user separation per A2 variant.
**R:** `refuted_if: any skill file contains hardcoded swarm/wiki/ path that ignores ${WIKI_ROOT}`; `accepted_if: grep -rn 'swarm/wiki/' .claude/skills/ returns zero non-comment hardcoded paths`.

**Claim 2.** The OFFLINE_MODE=1 path in /ask is zero-LLM-call by construction (Step 2.5 returns before Steps 3-4 which contain synthesis).
**F:** F5 (codified in skill body above — Step 2.5 ends with STOP sentinel).
**ClaimScope:** holds as long as the skill file is not modified to move the STOP gate; Phase-B local-LLM path will extend, not bypass, this gate.
**R:** `refuted_if: grep skill-invocation-log shows Task() call during OFFLINE_MODE=1 session`; `accepted_if: tcpdump/ss shows zero :443 connections during OFFLINE_MODE=1 /ask run`.

**Claim 3.** The 60 edges seeded in A.3 are all derivable from existing on-disk files (confirmed by reading swarm/wiki/index.md, edges.jsonl current state, and the draft file paths listed in variant-A1 §4 sources[]). No edge references a file that doesn't exist at the time of writing.
**F:** F4 (read from disk; edges derived by walking known paths).
**ClaimScope:** holds at 2026-04-24 repo state; paths may need verification at commit time if any source file was moved.
**R:** `refuted_if: L-DANGLING-EDGE check fires on any of the 60 new records`; `accepted_if: bash swarm/tests/part-a-smoke.sh exits 0 on A.3 check`.

**Dissents:** none (sole-authorship integrator pass; no contradicting peer inputs in this wave).
