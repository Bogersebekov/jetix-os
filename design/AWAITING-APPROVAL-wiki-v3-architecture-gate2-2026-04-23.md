---
title: Wiki v3 Architecture Spec — Gate 2 (Deliverables 7–12, operational integration)
date: 2026-04-23
status: AWAITING-APPROVAL
gate: 2-of-2
covers_deliverables: [7, 8, 9, 10, 11, 12]
upstream_gate: design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md  # D1–D6 approved
upstream:
  - decisions/WIKI-V3-MECHANICS-2026-04-23.md     # Q1..Q9 + R1..R8 + T1..T5
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md        # W-1..W-12
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  - design/ROY-BUILD-LOGIC-2026-04-23.md
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
extractions:
  - raw/research/step-2-2-3c-extractions/A-mechanics-goals-buildlogic.md
  - raw/research/step-2-2-3c-extractions/B-fpf-alphas-protocols.md
  - raw/research/step-2-2-3c-extractions/C-knowledge-arch-karpathy.md
  - raw/research/step-2-2-3c-extractions/D-v2-infrastructure-audit.md
  - raw/research/step-2-2-3c-extractions/E-master-synthesis-matrix.md
written_by: Claude Code on server (Opus 4.7, 1M context, Стадия C orchestrator)
branch: claude/jolly-margulis-915d34
---

# WIKI v3 ARCHITECTURE SPEC — GATE 2 (DELIVERABLES 7–12)

> **TL;DR** — This is the **operational integration surface**: the
> parameterization config that lets v2 and v3 coexist (D7), the diffs
> that wire the existing v2 skills to read `$WIKI_ROOT` (D8), the
> symlink convention that makes promoted skills active (D9), the
> health.md dashboard that surfaces FPAR / cycle / cross-theme
> metrics (D10), the Q6 activation-vs-validation rubric (D11), and
> the T5 strategies-trio collapse migration (D12).
>
> Gate 1 (D1–D6, ROY-approved) is the structural skeleton. Gate 2
> turns that skeleton into a **live, instrumented system** Стадия D
> can boot and operate.
>
> All citations preserve the W/Q/R/T/Lock provenance discipline of
> Gate 1. No locked decision is re-opened. No Tier 4 (393 books, web)
> is consulted.

---

## DELIVERABLE 7 — `.claude/config/wiki-roots.yaml` (Parameterization Config)

### 7.1 Mandate

Per Q9 (coexist + parameterize) and R3 (locked: v2 untouched, v3
added, `$WIKI_ROOT` indirection mandatory), this deliverable specifies
the full content of `.claude/config/wiki-roots.yaml` and the
`$WIKI_ROOT` resolution algorithm the 5 in-scope skills run at
startup. The file is the single source of truth for which wiki tree a
skill targets.

### 7.2 File content (Стадия D writes verbatim)

```yaml
# .claude/config/wiki-roots.yaml
# Single source of truth for wiki-root parameterization (Q9 + R3).
# Do NOT edit without an AWAITING-APPROVAL-wiki-roots-change-*.md
# committed to swarm/gates/ first.

schema_version: 1                    # bump when adding/removing keys
last_modified: 2026-04-23
managed_by: brigadier               # only brigadier writes this file

wiki_root_v2: wiki                   # path-relative to repo root
wiki_root_v3: swarm/wiki             # path-relative to repo root

default_root: wiki_root_v3           # which root new skills target
                                     # unless explicitly overridden via env

bridge_edge_type: cross-tree-ref     # per Q9 + D3 §3.2.12; v3→v2 only

v2_status: read-write                # v2 untouched; existing skills still ingest into wiki/
v3_status: read-write                # v3 primary going forward

migration_phase: A                   # Phase A = coexist; Phase B may flip migration_phase
                                     # decision deferred per WIKI-V3-MECHANICS Q9
                                     # applicability constraint (Sub-agent A §1 Q9
                                     # L658–660): trigger Phase-B re-eval only when
                                     # v3 ≥50 entries AND ≥1 closed cycle AND value-delta observed

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
  - search-kb        # per master synthesis §5.10 — legacy KB-only; supplanted by /ask
  - sweep-notion-bank # per master synthesis §5.10 — one-shot Notion-import bound to 2026-04-16 + DB ID
  - compile          # per Sub-agent D §4.6 + §7 — legacy knowledge-base/ writer; deprecated v3
                     # (D8 §8.6 documents the deprecation rationale; not parameterised)
```

### 7.3 Per-key annotation table

| Key | Type | Allowed values | Behaviour at load time | Which skills read |
|---|---|---|---|---|
| `schema_version` | int | `1` (bump on schema change) | parsers reject unknown versions | all |
| `last_modified` | iso-date | valid ISO date | informational only | all |
| `managed_by` | string | `brigadier` | informational; surfaced by /lint when this file's writer differs | all |
| `wiki_root_v2` | string (path) | a path relative to repo root that resolves to a directory | becomes `$WIKI_ROOT_V2` env var | all D8 skills (read-only legacy access) |
| `wiki_root_v3` | string (path) | a path relative to repo root that resolves to a directory | becomes `$WIKI_ROOT_V3` env var | all D8 skills |
| `default_root` | enum | `wiki_root_v2` or `wiki_root_v3` | resolves to `$WIKI_ROOT` per the algorithm in §7.4 | all D8 skills |
| `bridge_edge_type` | string (D3 enum) | one of D3 edge types | drives `cross-tree.jsonl` write target type | /ingest, /build-graph |
| `v2_status` | enum | `read-only` or `read-write` | when `read-only`, /ingest into v2 is rejected | /ingest, /consolidate |
| `v3_status` | enum | `read-only` or `read-write` | parallel | /ingest, /consolidate |
| `migration_phase` | enum | `A` or `B` | informational; bumps trigger Phase-B re-evaluation | meta-agent, brigadier |
| `edges_v2`, `edges_v3`, `edges_cross_tree` | string (path) | resolved paths | /build-graph picks the file by `--tree` flag (T1 separation) | /build-graph, /ingest |
| `skills_in_scope_for_wiki_root` | list of strings | each must match an existing skill in `.claude/skills/` | drives D8 diff scope | meta-agent (lint check) |
| `skills_excluded_from_wiki_root` | list of strings | each must match an existing skill | each must have a documented exclusion rationale (D8 §8.6) | meta-agent (lint check) |

### 7.4 `$WIKI_ROOT` resolution algorithm

The 5 in-scope skills (D8) run this exact algorithm at startup, before
any Read/Write to `wiki/` or `swarm/wiki/`:

```
# pseudo-code (executed by every D8 skill at startup)
fn resolve_wiki_root(skill_invocation):
    config := read_yaml(".claude/config/wiki-roots.yaml")

    # Precedence (highest first):
    # 1. Per-invocation env override — `WIKI_ROOT=...` in shell env at skill launch
    # 2. Per-skill flag override — `--wiki-root=v2|v3` on the command line
    # 3. Config default — `default_root` key resolves to `wiki_root_v2` or `wiki_root_v3`
    # 4. Hard-coded fallback — "swarm/wiki" (matches D1 v3 root)

    if env("WIKI_ROOT") is set:
        return env("WIKI_ROOT")
    if cli_flag("--wiki-root") in {"v2", "v3"}:
        return config["wiki_root_" + cli_flag_value]
    if config["default_root"] in config:
        return config[config["default_root"]]
    return "swarm/wiki"   # hard-coded last-resort fallback

fn assert_root_writable(root, skill_name):
    # Honour v2_status / v3_status read-only flags
    status_key := if root == config["wiki_root_v2"] then "v2_status" else "v3_status"
    if config[status_key] == "read-only" and skill_writes_to_wiki(skill_name):
        log "Refusing to write to {root}: {status_key} = read-only"
        exit 2
```

The algorithm is **stateless** (re-runs at every skill invocation; no
caching between sessions). This honours the Max-subscription discipline
(D6 §6.10 — no SDK calls; pure filesystem read).

### 7.5 Worked example (Стадия D verification)

After Стадия D writes the file, a brigadier session running `/ingest`
sees:

```bash
$ unset WIKI_ROOT          # no env override
$ cd ~/jetix-os
$ # /ingest internally calls resolve_wiki_root() → reads default_root → "wiki_root_v3" → "swarm/wiki"
$ # → /ingest writes to swarm/wiki/sources/<...>.md
```

Backwards-compatibility test:

```bash
$ WIKI_ROOT=wiki /ingest raw/articles/foo.md   # explicit v2 ingest
$ # → /ingest writes to wiki/sources/<...>.md
```

Per-flag test:

```bash
$ /ingest --wiki-root=v2 raw/articles/foo.md   # explicit v2 via flag
$ # → /ingest writes to wiki/sources/<...>.md
```

### 7.6 Compatibility matrix

| Locked item | D7 honours by … |
|---|---|
| Q9 coexist + parameterize | `wiki_root_v2` + `wiki_root_v3` both present; `default_root` controls new behaviour. |
| R3 v2 untouched, v3 added | `v2_status: read-write` keeps v2 ingestible (per Sub-agent A §1 Q9 — v2 ingestion not frozen); `default_root: wiki_root_v3` routes new content to v3. |
| T1 cross-tree separation | `edges_cross_tree` path explicitly distinct from `edges_v2`/`edges_v3`. |
| Sub-agent A §1 Q9 applicability constraint | `migration_phase: A` documented; Phase-B re-eval trigger noted. |
| Master synthesis §5.10 6-skill inferred set | `skills_in_scope_for_wiki_root` lists 5 (`ingest/ask/lint/consolidate/build-graph`) per D's audit; `skills_excluded` lists 3 with rationale (search-kb / sweep-notion-bank explicit per §5.10; compile per D's §4.6 deprecation). Total 5 in-scope, not 6 — see D8 §8.1 reconciliation. |
| Max-subscription (D6 §6.10) | resolution algorithm is pure filesystem read; no API calls; no embeddings. |
| 24-Lock 17 (Filesystem = SoT) | this file lives at `.claude/config/wiki-roots.yaml`; filesystem is the source of truth. |

---
