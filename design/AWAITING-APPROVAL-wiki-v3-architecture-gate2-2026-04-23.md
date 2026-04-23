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
    # Closes critic-gate2 H4 dead-code check: previous version tested
    # `config["default_root"] in config` which is always true (the
    # value of default_root is a key by schema). Correct check is:
    # does the *value pointed to by* default_root resolve to a configured root?
    if config["default_root"] not in {"wiki_root_v2", "wiki_root_v3"}:
        log "ERROR: default_root must be wiki_root_v2 or wiki_root_v3, got {config[default_root]}"
        exit 3
    return config[config["default_root"]]   # config["wiki_root_v2"] or config["wiki_root_v3"]
    # No hard-coded fallback — schema guarantees default_root resolves;
    # if config file is missing/malformed, the YAML parser exits earlier.

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

## DELIVERABLE 8 — Skill Edit Diffs (5 in-scope skills + 3 documented exclusions)

### 8.1 Mandate, scope reconciliation, and edit budget

The prompt §6 D8 mandates concrete edit diffs for "6 skills targeted
(`/ingest`, `/ask`, `/lint`, `/compile`, `/consolidate`, `/build-graph`)."
Sub-agent D §4 audit revealed `/compile` (50 lines) targets legacy
`knowledge-base/`, NOT `wiki/`. Sub-agent D §7 transplant table
recommendation: "drop (or rewrite); Targets legacy knowledge-base/;
supplanted by /ingest + /ask in v2." Sub-agent E §4 confirms `/compile`'s
inclusion in the 6-skill list is inferred (master synthesis §5.10
itself does not name 6).

**Resolution.** This deliverable scopes to **5 in-scope skills** for
`$WIKI_ROOT` parameterisation (`/ingest`, `/ask`, `/lint`,
`/consolidate`, `/build-graph`) and **3 documented exclusions**
(`/search-kb`, `/sweep-notion-bank`, `/compile`). The 6→5 reduction
honours the audit (no point parameterising a skill that doesn't read
`wiki/` at all) and is the cleaner Стадия-D landing. If Ruslan wants
`/compile` rewritten for v3 KB target, escalate as a follow-up
`AWAITING-APPROVAL-compile-v3-rewrite-*.md` after Стадия D ships.

**Edit budget per Sub-agent D §4 audit + ~9-line `$WIKI_ROOT` resolution
preamble per skill:**

| Skill | Total lines (current) | Path-line replacements | Prose tweaks | New `$WIKI_ROOT` preamble | Total per-skill lines changed | Cumulative |
|---|---|---|---|---|---|---|
| /ingest | 135 | 7 | 2 | 9 | 18 | 18 |
| /ask | 116 | 7 | 2 | 9 | 18 | 36 |
| /lint | 103 | 7 | 2 | 9 | 18 | 54 |
| /consolidate | 96 | 8 | 2 | 9 | 19 | 73 |
| /build-graph | 97 | 5 | 2 | 9 | 16 | 89 |

Total: **89 substantive lines changed across 5 files** (matches
Sub-agent D §4.8 estimate of ~85 ± rounding; matches prompt §6 D8 budget).

### 8.2 Shared `$WIKI_ROOT` resolution preamble (inserted into each in-scope skill)

Every in-scope skill receives the following 9-line block immediately
after its frontmatter (before `# Skill: /...`). The preamble is
**identical** across all 5 skills — Стадия D copy-pastes verbatim.

```markdown
> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. The default
> root is `swarm/wiki/` (v3) per D7 `default_root: wiki_root_v3`. To
> target v2, set `WIKI_ROOT=wiki` env var or pass `--wiki-root=v2`.
> Cross-tree edges (v3→v2 only) land in
> `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
```

(Counted as 9 lines including the blank line before `# Skill:`.)

### 8.3 `/ingest` skill diff (`.claude/skills/ingest.md`, 135 lines → +18 = 153 lines)

**Audit baseline:** Sub-agent D §4.1 — 7 substantive `wiki/` paths at
lines 62, 65, 71, 78, 90, 100, 111; 2 prose mentions at lines 3, 15.

**Per-edit table:**

| # | Line range | Before (current) | After (v3) | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` resolution at skill entry |
| 2 | L3 (frontmatter description) | `description: "Поднять источник из raw/ (или по URL) в wiki/: распарсить, создать entity-страницы, обновить index/log/edges."` | `description: "Поднять источник из raw/ (или по URL) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"` | prose alignment — surfaces parameterisation in the skill description |
| 3 | L15 (description body) | `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц wiki/.` | `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц \`${WIKI_ROOT}/\`.` | prose alignment |
| 4 | L62 | `1. Построить путь: \`wiki/{type}/{slug}.md\`.` | `1. Построить путь: \`${WIKI_ROOT}/{type}/{slug}.md\`.` | path parameterisation |
| 5 | L65 | `3. Если нет → взять шаблон из \`wiki/_templates/{type}.md\`, заполнить.` | `3. Если нет → взять шаблон из \`${WIKI_ROOT}/_templates/{type}.md\`, заполнить.` | path parameterisation |
| 6 | L71 | `\`wiki/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:` | `\`${WIKI_ROOT}/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:` | path parameterisation |
| 7 | L78 | `### 6. Добавить edges в \`wiki/graph/edges.jsonl\`` | `### 6. Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` (v3 intra-tree). Для v3→v2 ссылок — `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` (D3 §3.2.12 + T1).` | path parameterisation + cross-tree extension |
| 8 | L80–L82 (edge type list) | `Append-only. Один JSON на строку. 9 типов: \`extends\`, \`contradicts\`, \`supports\`, \`inspired_by\`, \`tested_by\`, \`invalidates\`, \`supersedes\`, \`addresses_gap\`, \`derived_from\`.` | `Append-only. Один JSON на строку. **12 типов per D3 §3.2** (10 intra-layer + 3 cross-layer): \`extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of, alpha-ref, layer-ref, cross-tree-ref\`. (\`addresses_gap\` dropped per critic-gate1 H4.)` | edge enum alignment with D3 |
| 9 | L90 | `### 7. Обновить \`wiki/index.md\`` | `### 7. Обновить \`${WIKI_ROOT}/index.md\`` | path parameterisation |
| 10 | L100 | `### 8. Добавить в \`wiki/log.md\` (сверху)` | `### 8. Добавить в \`${WIKI_ROOT}/log.md\` (сверху)` | path parameterisation |
| 11 | L111 | `В \`wiki/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы.` | `В \`${WIKI_ROOT}/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы. (Niche enum: 6 values per CLAUDE.md L70 lock — \`personal/business/sales/life/tech/meta\`; \`global\` removed per critic-gate1 S3.)` | path parameterisation + niche-enum correction (also fixes L45 implicit reference) |
| 12 | L45 (niche enum) | `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`, \`global\`.` | `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`. (6 niches per CLAUDE.md L70 lock; \`global\` content lives in Layer 7 \`${WIKI_ROOT}/global/\` per D1.)` | niche enum alignment |

**Net edits:** 11 line edits (12 numbered above; #1 is insertion-only,
not replacement). Combined with the 9-line preamble, the file grows
~15 lines net (some prose lines lengthen, no lines deleted).

**Behaviour after edit.** /ingest reads `.claude/config/wiki-roots.yaml`
at startup, resolves `$WIKI_ROOT` to `swarm/wiki/` by default, writes
all entity pages and updates index/log/edges under that root. Edge
types align with D3 12-enum.

**Test plan.** (1) `unset WIKI_ROOT && /ingest raw/articles/foo.md` →
expect `swarm/wiki/sources/<…>.md` written. (2) `WIKI_ROOT=wiki
/ingest raw/articles/foo.md` → expect `wiki/sources/<…>.md` written
(v2 backward-compat). (3) `/ingest raw/v3-test.md` should add an edge
to `swarm/wiki/graph/edges.jsonl` (not v2 `wiki/graph/edges.jsonl`).

### 8.4 `/ask` skill diff (`.claude/skills/ask.md`, 116 lines → +18 = 134 lines)

**Audit baseline:** Sub-agent D §4.2 — 7 substantive paths at L20, 27,
28, 29, 60, 71, 100; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` resolution |
| 2 | L3 | `description: "Ответить на вопрос по wiki/: подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в comparisons/."` | `description: "Ответить на вопрос по \`${WIKI_ROOT}/\` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в \`${WIKI_ROOT}/comparisons/\`."` | prose alignment |
| 3 | L11 | `Ответить на содержательный вопрос пользователя по накопленной wiki/.` | `Ответить на содержательный вопрос пользователя по накопленной \`${WIKI_ROOT}/\`.` | prose |
| 4 | L20 | `### 1. Прочитать \`wiki/index.md\`` | `### 1. Прочитать \`${WIKI_ROOT}/index.md\`` | path |
| 5 | L27 | `- При необходимости — grep по ключевым словам вопроса в \`wiki/**/*.md\`.` | `- При необходимости — grep по ключевым словам вопроса в \`${WIKI_ROOT}/**/*.md\`.` | path |
| 6 | L28 | `- Смотри niche: если вопрос явно про sales — приоритет \`wiki/niches/sales/\` и страниц с \`niche: sales\`.` | `- Смотри niche: если вопрос явно про sales — приоритет \`${WIKI_ROOT}/niches/sales/\` и страниц с \`niche: sales\`.` | path |
| 7 | L29 | `- Если есть community summaries (\`wiki/graph/summaries.md\`) — используй их для быстрого контекста.` | `- Если есть community summaries (\`${WIKI_ROOT}/graph/summaries.md\`) — используй их для быстрого контекста. (Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)` | path + Q1 Tier-4 alignment |
| 8 | L60 | `**Сохранить в \`wiki/comparisons/\`** если ответ:` | `**Сохранить в \`${WIKI_ROOT}/comparisons/\`** если ответ:` | path |
| 9 | L71 | `\`wiki/comparisons/YYYY-MM-DD-question-slug.md\`:` | `\`${WIKI_ROOT}/comparisons/YYYY-MM-DD-question-slug.md\`:` | path |
| 10 | L100 | `Добавить edges в \`wiki/graph/edges.jsonl\`.` | `Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` per D3 12-enum. Cross-tree refs (v3→v2) → \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` per T1.` | path + cross-tree |

**Net edits:** 9 line edits + 9-line preamble = 18 lines changed.

**Behaviour after edit.** /ask reads `$WIKI_ROOT/index.md` first
(Karpathy Tier-2), then `$WIKI_ROOT/niches/<niche>/`, then
typed-BFS over `$WIKI_ROOT/graph/edges.jsonl` (Q1 Tier-3), then
long-context fallback bounded to niche dir (Q1 Tier-4). Comparisons
and edges land in the right tree.

**Test plan.** (1) Default-root: `/ask "что такое 4-tier retrieval"` →
reads `swarm/wiki/index.md` first; comparisons land in
`swarm/wiki/comparisons/`. (2) `WIKI_ROOT=wiki /ask "что такое
4-tier retrieval"` → reads `wiki/index.md`; comparisons land in
`wiki/comparisons/`.

### 8.5 `/lint` skill diff (`.claude/skills/lint.md`, 103 lines → +18 = 121 lines)

**Audit baseline:** Sub-agent D §4.3 — 7 substantive paths at L21, 30,
38, 55, 60, 92, 102; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Health check wiki/: 7 проверок..."` | `description: "Health check \`${WIKI_ROOT}/\` (default v3): 5-signal /lint orchestration per Q5 + structural checks (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift)."` | prose + Q5 5-signal alignment |
| 3 | L11 | `Проверка целостности wiki/.` | `Проверка целостности \`${WIKI_ROOT}/\`.` | prose |
| 4 | L21 | `Страницы, на которые никто не ссылается (нет входящих \`[[links]]\` и нет в \`wiki/graph/edges.jsonl\`).` | `Страницы, на которые никто не ссылается (нет входящих \`[[links]]\` и нет в \`${WIKI_ROOT}/graph/edges.jsonl\`).` | path |
| 5 | L30 | `\`wiki/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня.` | `\`${WIKI_ROOT}/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня. **Дополнительно: \`${WIKI_ROOT}/foundations/*.md\` где \`last_reviewed:\` старше 365 дней (Q5 §3 + D2 §2.3 foundations re-review).**` | path + Q5 §3 365-day re-review for foundations |
| 6 | L38 | `Markdown в \`wiki/**/*.md\` без обязательных полей: \`title\`, \`type\`, \`niche\`, \`created\`, \`updated\`, \`pipeline\`.` | `Markdown в \`${WIKI_ROOT}/**/*.md\` без обязательных полей per D2 §2.2 cross-layer table: \`id, title, type, layer, niche, created, last_modified, pipeline, state, confidence, tier, produced_by, sources, related, topics, captured_by, captured_date\`.` | path + full D2 cross-layer field list |
| 7 | L55 | `- Файл есть в wiki/, но его нет в \`index.md\` (в соответствующей секции).` | `- Файл есть в \`${WIKI_ROOT}/\`, но его нет в \`index.md\` (в соответствующей секции).` | path |
| 8 | L60 | `\`wiki/_lint-report-YYYY-MM-DD.md\`:` | `\`${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md\`:` | path |
| 9 | L92 | `- wiki/concepts/foo.md → [[bar]] (нет такого файла)` | `- ${WIKI_ROOT}/concepts/foo.md → [[bar]] (нет такого файла)` | path (in example) |
| 10 | L102 | `- Добавить запись в \`wiki/log.md\`:` | `- Добавить запись в \`${WIKI_ROOT}/log.md\`:` | path |
| 11 | (after L17 "Проверки") | (existing 7 checks) | **NEW SECTION:** "### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)" — for skill pages (path under `${WIKI_ROOT}/skills/` OR `type: skill`): flag pages with `state ∉ {candidate, learning, active, tombstoned}` (α-3 4-state lock per critic-gate1 S2 + D2 §2.4). For all other pages: flag pages with `state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}` (α-2 8-state set). Branching closes critic-gate2 M3. "### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)" — every inline wikilink matching the regex `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]` (closes critic-gate2 H5; non-matching forms like `[[A]]` or `[[file.md]]` are **warned** as legacy/unparseable, not errored) MUST appear in `related[]` AND produce one record in `${WIKI_ROOT}/graph/edges.jsonl`. "### 10. Q8 Layer-9 lock (per D1 §1.6)" — flag the existence of any file under `${WIKI_ROOT}/insights/{candidates,promoted}/*.md` (i.e. any leaf `.md` write outside `README.md`) when D1 §1.6 boilerplate is in effect (closes critic-gate2 H6 by testing file-presence rather than a frontmatter field that D1 §1.6 didn't define). | extends /lint to cover Q5 5-signal + Q3 triple-channel reconciliation + Q8 lock per D2 + D3 |

**Net edits:** 10 line edits + new sections (~15 lines) + 9-line
preamble = ~34 lines added/changed. Slightly above the audit's
estimate because /lint absorbs the Q5 5-signal and triple-channel
enforcement. Acceptable inflation; the alternative is a separate
/lint-v3 skill which would violate the parameterisation principle.

**Behaviour after edit.** /lint runs the original 7 v2 checks +
3 new v3 checks (α-2/α-3 lifecycle, triple-channel consistency, Q8
lock). Reports land in `$WIKI_ROOT/_lint-report-<date>.md`.

**Test plan.** (1) Default-root: `/lint` → walks `swarm/wiki/`,
emits report at `swarm/wiki/_lint-report-2026-04-23.md`. (2) Set up
a draft page with `[[concepts/foo]]` body wikilink but missing
`related[]`/edges entry; expect /lint to flag it under check #9. (3)
Try writing `swarm/wiki/insights/candidates/test.md` with
`phase_a_lock: true` → expect /lint to reject under check #10.

### 8.6 `/consolidate` skill diff (`.claude/skills/consolidate.md`, 96 lines → +19 = 115 lines)

**Audit baseline:** Sub-agent D §4.4 — 8 substantive paths at L36, 37,
68, 70, 73, 76, 80, 81; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Найти дубликаты в wiki/ и предложить merge..."` | `description: "Найти дубликаты в \`${WIKI_ROOT}/\` (default v3) и предложить merge..."` | prose |
| 3 | L11 | `Объединение дубликатов в wiki/.` | `Объединение дубликатов в \`${WIKI_ROOT}/\`.` | prose |
| 4 | L36 | `  A: wiki/concepts/value-based-pricing.md (4 sources, 120 lines)` | `  A: ${WIKI_ROOT}/concepts/value-based-pricing.md (4 sources, 120 lines)` | path (in example) |
| 5 | L37 | `  B: wiki/concepts/value-pricing.md (2 sources, 80 lines)` | `  B: ${WIKI_ROOT}/concepts/value-pricing.md (2 sources, 80 lines)` | path (in example) |
| 6 | L68 | `   - Обновить \`wiki/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\`` | `   - Обновить \`${WIKI_ROOT}/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\`. **Также пройти по \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` для v3-сторонних ссылок на B.**` | path + cross-tree handling per T1 |
| 7 | L70 | `   - Обновить \`wiki/index.md\`: убрать строку B, обновить A.` | `   - Обновить \`${WIKI_ROOT}/index.md\`: убрать строку B, обновить A.` | path |
| 8 | L73 | `   - Перед удалением — создать копию в \`wiki/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A").` | `   - Перед удалением — создать копию в \`${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A"). **Per critic-gate2 SS3: this skill runs as expert (D6 §6.6.3 role_tool_matrix) and CANNOT mutate canonical α-2 `state` field — that requires brigadier per Q2/D6 §6.2. /consolidate writes the `_archive/` copy with the original frontmatter unchanged + appends an HTML comment `<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->`. The brigadier subsequently transitions α-2 `state: superseded` + `superseded_by: [[<A-path>]]` per D5 §5.3 movers (separate commit).**` | path + α-2 ownership clarification (closes critic-gate2 SS3) |
| 9 | L76 | `5. Залогировать в \`wiki/log.md\` (сверху):` | `5. Залогировать в \`${WIKI_ROOT}/log.md\` (сверху):` | path |
| 10 | L80 | `   A: wiki/concepts/value-based-pricing.md` | `   A: ${WIKI_ROOT}/concepts/value-based-pricing.md` | path (in example) |
| 11 | L81 | `   B (archived): wiki/_archive/YYYY-MM-DD-value-pricing.md` | `   B (archived): ${WIKI_ROOT}/_archive/YYYY-MM-DD-value-pricing.md` | path (in example) |

**Net edits:** 10 line edits + 9-line preamble = 19 lines changed.

**Behaviour after edit.** /consolidate operates within `$WIKI_ROOT`,
moves losers to `$WIKI_ROOT/_archive/`, sets α-2 state correctly,
and updates BOTH `edges.jsonl` AND `cross-tree.jsonl` (the latter
when the loser had inbound v3→v2 cross-refs).

**Test plan.** (1) Set up duplicate `swarm/wiki/concepts/foo.md` and
`swarm/wiki/concepts/foo-v2.md`; run `/consolidate` → on `y`,
loser moves to `swarm/wiki/_archive/`, frontmatter shows `state:
superseded` + `superseded_by:`. (2) If a v3→v2 cross-tree-ref pointed
at the loser, verify the cross-tree.jsonl record is rewritten to
point at the survivor.

### 8.7 `/build-graph` skill diff (`.claude/skills/build-graph.md`, 97 lines → +16 = 113 lines)

**Audit baseline:** Sub-agent D §4.5 — 5 substantive paths at L22, 33,
62, 73, 86; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Пройти по wiki/, добить недостающие edges в edges.jsonl, пересчитать communities + summaries."` | `description: "Пройти по \`${WIKI_ROOT}/\` (default v3), добить недостающие edges в edges.jsonl per D3 12-enum, пересчитать communities + summaries. Поддерживает \`--tree {v2|v3|both}\` per T1."` | prose + tree-flag |
| 3 | L11 | `Обновить граф знаний поверх wiki/.` | `Обновить граф знаний поверх \`${WIKI_ROOT}/\`.` | prose |
| 4 | L22 | `Glob \`wiki/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`.` | `Glob \`${WIKI_ROOT}/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`. **При \`--tree=both\`: повторить glob для v2 \`wiki/**/*.md\` и v3 \`swarm/wiki/**/*.md\`; cross-tree-ref edges (D3 §3.2.12) пишутся в \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.**` | path + tree-flag impl |
| 5 | L33 | `Прочитать \`wiki/graph/edges.jsonl\` в память (set по \`(from, to, type)\`).` | `Прочитать \`${WIKI_ROOT}/graph/edges.jsonl\` в память (set по \`(from, to, type)\`). При \`--tree=both\` — также \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.` | path + tree-flag |
| 6 | L37–L46 (edge type detection) | (current section-header → 9 v2 types) | **Update to D3 12-enum:** "Расширяет/Extends → \`extends\`. Противоречит/Contradicts → \`contradicts\` (запись BIDIRECTIONAL — обе стороны записать). Поддерживает/Supports → \`supports\`. Вдохновлён/Inspired by → \`inspired_by\`. Тестируется/Tested by → \`tested_by\`. Опровергает/Invalidates → \`invalidates\`. Заменяет/Supersedes → \`supersedes\`. Часть/Part of → \`part_of\` (FORMALIZED per Q3). Иначе (упоминание сущности) → \`derived_from\`. Cross-layer (5×4 matrix→alpha tracker) → \`alpha-ref\`. Cross-layer (theme → global pattern) → \`layer-ref\`. v3→v2 link → \`cross-tree-ref\` (запись в cross-tree.jsonl, не edges.jsonl). **Снят: \`addresses_gap\` per critic-gate1 H4.**" | edge enum alignment with D3; bidirectional contradicts; cross-tree separation |
| 7 | L62 | `### 5. Обновить \`wiki/graph/communities.md\`` | `### 5. Обновить \`${WIKI_ROOT}/graph/communities.md\`` | path (corrected per critic-gate2 SS2 — L62 is the actual communities line, not L60) |
| 8 | L73 | `### 6. Обновить \`wiki/graph/summaries.md\`` | `### 6. Обновить \`${WIKI_ROOT}/graph/summaries.md\`` | path |
| 9 | L86 | `В \`wiki/log.md\` (сверху):` | `В \`${WIKI_ROOT}/log.md\` (сверху):` | path |

**Net edits:** 5 path replacements + edge-type-detection rewrite (~10
lines) + 9-line preamble = ~24 lines changed (slightly above audit's 16).
The /build-graph extension absorbs D3's 12-enum migration and T1
cross-tree separation — both load-bearing for Q5 staleness signal #4
(contradiction-edge integrity) and Q1 Tier-3 retrieval.

**Behaviour after edit.** /build-graph walks `$WIKI_ROOT/`, detects
edge types per the D3 12-enum (with bidirectional `contradicts`),
writes intra-tree edges to `$WIKI_ROOT/graph/edges.jsonl`, writes
cross-tree edges to `$WIKI_ROOT_V3/graph/cross-tree.jsonl` (when
`--tree=both`), recomputes communities + summaries.

**Test plan.** (1) Default-root: `/build-graph` → walks
`swarm/wiki/`, emits edges to `swarm/wiki/graph/edges.jsonl`. (2)
`/build-graph --tree=both` → walks both trees; cross-tree-refs land
in `swarm/wiki/graph/cross-tree.jsonl`. (3) Verify a `contradicts`
edge written from page A to B also has the inverse B→A record.

### 8.8 Documented exclusions (3 skills NOT parameterised)

#### 8.8.1 `/search-kb` (38 lines) — **out of scope**

- **Path:** `.claude/skills/search-kb.md`.
- **Audit (Sub-agent D §4.7):** zero `wiki/` references; targets
  `knowledge-base/_index.md`, `knowledge-base/{cluster}/_moc.md`,
  `knowledge-base/`, `raw/`. Legacy KB lookup.
- **Exclusion source:** master synthesis §5.10 explicitly excludes
  `/search-kb` from wiki skills (per prompt §6 D8).
- **Disposition:** keep as-is for legacy use. Supplanted by `/ask`
  Tier-1/2 retrieval per Q1. No `$WIKI_ROOT` parameterisation
  required because the skill never touches `wiki/` or `swarm/wiki/`.
- **Future option (Phase B):** deprecate when `knowledge-base/`
  migration completes (per CLAUDE.md MIGRATION.md note); not in
  Phase A scope.

#### 8.8.2 `/sweep-notion-bank` (110 lines) — **out of scope**

- **Path:** `.claude/skills/sweep-notion-bank.md`.
- **Audit (Sub-agent D §4.8):** 5 substantive `wiki/` references at
  L29, 51, 72, 73, 77; one-shot Notion-import bound to specific date
  (2026-04-16) and specific Notion DB ID (bf0e9a11-0e6f-4717-9ae5-…).
- **Exclusion source:** master synthesis §5.10 explicitly excludes
  per prompt §6 D8.
- **Disposition:** keep as-is. Re-running for v3 would require full
  rewrite (different DB, different sweep date), not just
  parameterisation. If Ruslan later needs a v3 Notion sweep, escalate
  as `AWAITING-APPROVAL-sweep-notion-bank-v3-*.md`.

#### 8.8.3 `/compile` (50 lines) — **deprecated, out of scope**

- **Path:** `.claude/skills/compile.md`.
- **Audit (Sub-agent D §4.6):** zero `wiki/` references; targets
  `knowledge-base/{cluster}/_moc.md` and `knowledge-base/{cluster}/{topic}.md`.
  Legacy pre-v2 skill that synthesises raw → KB-article.
- **Exclusion source:** Sub-agent D §7 transplant table:
  "drop (or rewrite); Targets legacy knowledge-base/; supplanted by
  `/ingest` + `/ask` in v2."
- **Disposition:** **deprecate.** Emit a Phase-A deprecation note in
  `swarm/wiki/log.md` at Стадия D bootstrap:
  `## [2026-04-XX] deprecate | /compile | superseded by /ingest + /ask
  per Sub-agent D §7 + D8 §8.6.3`. The skill file is retained
  (kept for knowledge-base/ legacy use until `MIGRATION.md` finalises)
  but is not part of the v3 wiki-skill set.

### 8.9 Total edit budget verification

| Skill | Lines edited | Lines added (preamble) | Total per-skill | Cumulative |
|---|---|---|---|---|
| /ingest | 11 (incl. niche fix) | 9 | 20 | 20 |
| /ask | 9 | 9 | 18 | 38 |
| /lint | 10 + new sections (~15) | 9 | 34 | 72 |
| /consolidate | 10 | 9 | 19 | 91 |
| /build-graph | 5 + edge rewrite (~10) | 9 | 24 | 115 |

**Total: ~115 lines** (above prompt's ~85 estimate; the inflation
comes from /lint's Q5 5-signal absorption and /build-graph's D3
12-enum detection rewrite — both load-bearing semantic upgrades, not
optional polish). If Ruslan prefers a strict ~85-line budget, defer
the /lint Q5 5-signal extensions to a follow-up
`AWAITING-APPROVAL-lint-q5-extension-*.md`.

### 8.10 Compatibility matrix

| Locked item | D8 honours by … |
|---|---|
| Q9 + R3 (coexist + parameterize) | Every in-scope skill consumes `$WIKI_ROOT` from D7; defaults to v3 root; v2 still accessible via env/flag. |
| T1 (cross-tree separation) | /ingest, /consolidate, /build-graph all write cross-tree-ref records to `cross-tree.jsonl` (not `edges.jsonl`). |
| D3 (12-edge enum) | /ingest L80–L82 + /build-graph L37–L46 carry the D3 12-type vocabulary; `addresses_gap` dropped per critic-gate1 H4; bidirectional `contradicts`. |
| Q1 4-tier retrieval | /ask preamble + L29 long-context fallback bounded to niche dir. |
| Q5 5-signal /lint | /lint extended with α-2/α-3 lifecycle check + triple-channel consistency + Q8 Phase-A lock. |
| Q8 Layer-9 lock | /lint check #10 rejects writes under `insights/` when `phase_a_lock: true`. |
| Master synthesis §5.10 (skills inventory) | 5 in-scope skills match §5.10.2; 3 exclusions documented with source. |
| Max-subscription (D6 §6.10) | All edits are filesystem-only; no SDK, no embeddings, no third-party APIs. |
| Sub-agent D §4 audit + §7 transplant table | Per-skill edits match audit line numbers (cross-checked against actual file reads); /compile deprecation per D §7. |
| Critic-gate1 H4 (drop addresses_gap) | /ingest + /build-graph edge-type lists updated. |
| Critic-gate1 S3 (niche enum 6 not 7) | /ingest L45 niche-enum line corrected. |

---

## DELIVERABLE 9 — `.claude/skills/` Symlink Convention for v3 `active/<slug>.md`

### 9.1 Mandate

Per Q6 skill-learning pipeline + W-9 (skills first-class), when a skill
candidate is promoted from `swarm/wiki/skills/learning/<slug>/` to
`swarm/wiki/skills/active/<slug>.md`, the canonical content lives at
the v3 wiki path; Claude Code's runtime expects `.claude/skills/<slug>.md`
to be a real file (or a symlink resolving to one). This deliverable
specifies the **symlink convention** that bridges the two — the lifecycle
hooks integrated with α-3 transitions (D5 §5.4) and the lint signal
that surfaces broken symlinks.

### 9.2 Symlink rule (canonical form)

```
.claude/skills/<slug>.md  →  ../../swarm/wiki/skills/active/<slug>.md
```

**Relative path** (not absolute) for two reasons:

1. **Roy-replication discipline** (master synthesis §5.8.3 + Sub-agent
   E §8): "no hard-coded `/home/ruslan/*` paths." Absolute symlinks
   break when the repo is checked out elsewhere (e.g. on Ruslan's
   laptop, on a CI runner).
2. **Repo portability:** the relative target resolves correctly
   regardless of the absolute repo root.

`<slug>` is the same kebab-slug used as the file basename (D2 §2.4
`skill_slug` field) — one and only one canonical naming.

### 9.3 Filename normalisation

The `skill_slug` MUST satisfy:

- Regex `^[a-z0-9-]{1,60}$` — the body half of D2 §2.2 `id` regex
  (`^[a-z]+-[a-z0-9-]{1,60}$` where `[a-z]+-` is the type-prefix and
  `[a-z0-9-]{1,60}$` is the slug body). For skills the type-prefix is
  always `skill-`, so the `id` is `skill-<slug>` and the `<slug>`
  portion conforms to the body regex (closes critic-gate2 H1
  inconsistency with D2 §2.2 `id` format).
- Unique across `.claude/skills/` (no collision with v2 file names).
- Match the basename of `swarm/wiki/skills/active/<slug>.md` exactly.

Slug derivation rules:

- Single-word: lowercase as-is (`focus` → `focus`).
- Multi-word: hyphen-separated lowercase (`Build Graph` → `build-graph`).
- No spaces, no underscores, no uppercase, no extension in the slug
  itself (`.md` is always appended at file path resolution, never
  inside the slug).

### 9.4 Symlink creation step (α-3 `learning → validated` transition)

Triggered by D11 §11.4 activation predicate. Brigadier executes (per
D6 §6.2 single-writer rule):

```bash
# Pre-flight checks (brigadier verifies before symlink creation)
test -f swarm/wiki/skills/active/<slug>.md  || exit "no canonical"
test ! -e .claude/skills/<slug>.md          || exit "name collision; see §9.6"

# Create symlink (atomic via ln -s)
ln -s ../../swarm/wiki/skills/active/<slug>.md .claude/skills/<slug>.md

# Verify
readlink .claude/skills/<slug>.md         # should print "../../swarm/wiki/skills/active/<slug>.md"
test -f .claude/skills/<slug>.md          || exit "broken symlink"
```

This step is part of the brigadier's α-3 `active → validated`
transition mover (D5 §5.4). It is committed in the same commit as the
file move from `swarm/wiki/skills/learning/<slug>/manifest.md` to
`swarm/wiki/skills/active/<slug>.md` (commit message format per D6
§6.2.4).

### 9.5 Symlink removal step (α-3 `validated → tombstoned` transition)

Triggered by D11 §11.5 retirement / tombstoning predicates. Brigadier
executes:

```bash
# Pre-flight check
test -L .claude/skills/<slug>.md          || exit "not a symlink (or absent)"

# Remove symlink (file at canonical path is preserved by the α-3 mover; see D5 §5.4)
rm .claude/skills/<slug>.md

# Move canonical to _archive/ per α-3 tombstone transition
mv swarm/wiki/skills/active/<slug>.md \
   swarm/wiki/_archive/skills/<slug>.md
```

The skill's content file is **not deleted** (anti-pattern Sub-agent C
§8 #9: "never delete, only archive"). The symlink IS deleted because
Claude Code only registers active skills via the `.claude/skills/`
directory.

Note: per critic-gate1 S2 fix, α-3 has only 4 states
(proposed/active/validated/tombstoned). There is no separate `retired`
state requiring a different removal path; graceful supersession also
goes through tombstone (with a `supersedes:` edge from the successor
skill, per D3 §3.2.7).

### 9.6 Conflict handling — v2 skill collides with v3 promotion

The v2 `.claude/skills/` directory contains pre-v3 skills (per
Sub-agent D §4 audit: ingest, ask, lint, compile, consolidate,
build-graph, search-kb, sweep-notion-bank — 8 files; plus `close-day`,
`focus`, `plan-day` directories). When a v3 skill candidate's slug
collides with a v2 file:

**Step 1 — detect.** Brigadier checks: `test -e .claude/skills/<slug>.md`.
If true → collision.

**Step 2 — preserve v2.** Move the v2 file:

```bash
mv .claude/skills/<slug>.md  .claude/skills/<slug>_v2.md
```

The `_v2` suffix is the marker of a deprecated v2 skill retained for
audit. `/lint` flags `_v2`-suffixed files as deprecated (informational
only; not an error).

**Step 3 — create v3 symlink.** Per §9.4.

**Step 4 — record migration in frontmatter** of the v3 canonical file
(`swarm/wiki/skills/active/<slug>.md`). Per critic-gate2 H7 (D4
templates have no `## Migration note` body section schema), the
migration record lives in frontmatter, not body:

```yaml
migrated_from: .claude/skills/<slug>_v2.md      # path to preserved v2 file
migration_date: <YYYY-MM-DD>
migration_note: <one-line summary of v2→v3 differences>
```

`/lint` (per D8 §8.5 #4 missing-frontmatter) accepts `migrated_from`,
`migration_date`, `migration_note` as optional fields when present.

The 5 in-scope D8 skills (`/ingest`, `/ask`, `/lint`, `/consolidate`,
`/build-graph`) are NOT promoted via the v3 candidate→learning→active
pipeline — they were already v2 skills, parameterised in place per
D8 (their `.claude/skills/<slug>.md` files remain regular files, not
symlinks). Only **new** v3-born skills go through D9 promotion.

### 9.7 Audit signals — how `/lint` detects broken symlinks

`/lint` (per D8 §8.5 extension) gains a sub-check inside check #1
(structural):

```
For each .md file in .claude/skills/:
  if file is a symlink:
    target := readlink(file)
    if not file_exists(target):
      EMIT "broken symlink: .claude/skills/<slug>.md → <target>"
    if not target.startswith("../../swarm/wiki/skills/active/"):
      EMIT "symlink target outside active/: .claude/skills/<slug>.md → <target>"
    if not target.endswith("/<basename(file)>"):
      EMIT "symlink basename mismatch: .claude/skills/<slug>.md → <target>"
```

This catches three failure modes:

- Brigadier removed canonical without removing symlink (`broken symlink`).
- Symlink mistakenly points to `learning/` or `_archive/` (target
  outside `active/`).
- Slug rename happened on canonical without updating symlink
  (`basename mismatch`).

### 9.8 Worked example — full skill lifecycle

A new v3-born skill `query-pricing-models` proceeds:

1. **proposed** (α-3 entry). Compound step writes:
   `swarm/wiki/skills/candidates/query-pricing-models/manifest.md`.
   No symlink yet.

2. **active** (α-3 `learning`; spec alias). Brigadier moves
   `manifest.md` to `swarm/wiki/skills/learning/query-pricing-models/manifest.md`,
   creates `golden-set.jsonl` (per D11). Brigadier appends use events
   to `swarm/wiki/skills/usage/query-pricing-models.jsonl`.
   No symlink yet.

3. **validated** (α-3; D11 activation predicate satisfied). Brigadier:
   - Moves canonical: `mv swarm/wiki/skills/learning/query-pricing-models/manifest.md
     swarm/wiki/skills/active/query-pricing-models.md`.
   - Pre-flight (no v2 collision; new slug).
   - Creates symlink: `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md
     .claude/skills/query-pricing-models.md`.
   - Updates `swarm/wiki/log.md` (per D6 §6.2.4 commit format).
   - Single commit covers all the above.

4. **tombstoned** (α-3; ratio drops <1:1 per D11 §11.5). Brigadier:
   - Removes symlink: `rm .claude/skills/query-pricing-models.md`.
   - Archives canonical: `mv swarm/wiki/skills/active/query-pricing-models.md
     swarm/wiki/_archive/skills/query-pricing-models.md`.
   - Records `tombstoned_by:` in the archived file's frontmatter.
   - Updates `swarm/wiki/log.md`.

### 9.9 Compatibility matrix

| Locked item | D9 honours by … |
|---|---|
| Q6 (skill-learning pipeline) | symlink lifecycle integrated with α-3 transitions per D5 §5.4. |
| W-9 (skills first-class) | active skills are first-class wiki entries at `swarm/wiki/skills/active/`; `.claude/skills/` is a symlink registry. |
| §5.5.5 provenance gate (D6 §6.3) | symlink creation deferred to brigadier per single-writer Q2; α-3 transition predicates verified before symlink. |
| Master synthesis §5.8.3 (Roy-replication) | relative symlinks (no absolute paths). |
| Sub-agent C §8 #9 (never-delete-only-archive) | `tombstoned` skills moved to `_archive/`, not `rm`-ed. |
| Critic-gate1 H7 (kebab-slug discipline) | §9.3 enforces kebab-slug regex; matches D2 `skill_slug` field. |
| Critic-gate1 S2 (α-3 4-state lock) | §9.5 acknowledges no `retired` state; supersession routes through `tombstoned` + `supersedes:` edge per D3 §3.2.7. |
| D8 §8.5 (`/lint` skill diffs) | §9.7 audit checks integrated into /lint check #1 structural. |

---

## DELIVERABLE 10 — `swarm/wiki/meta/health.md` Skeleton

### 10.1 Mandate

Per Q5 (5-signal /lint) + W-12 (1000% depth) + Q8 (Layer-9 trigger
metrics) + critic-gate1 H1/M10 (forward-reference fix), this
deliverable specifies the **initial content** of `swarm/wiki/meta/health.md`
as the swarm's self-monitoring dashboard. The file contains 8
sections, each with: definition, computation formula, source data,
threshold for alerting, and a structured-log scaffold for time-series
records.

### 10.2 File content (Стадия D writes verbatim)

**Singleton frontmatter exemption (closes critic-gate2 H2 + H3).** This
file (`swarm/wiki/meta/health.md`) is a **singleton dashboard** with
its own dedicated frontmatter schema, exempt from D2 §2.2 cross-layer
table extras-rejection. The 5 live-counter fields below
(`closed_cycles_count`, `active_skills_count`, `cross_theme_refs_count`,
`tombstone_rate_weekly`, `fpar_swarm_wide`) are dashboard-specific and
mutated by `/lint` + meta-agent per §10.8. Field types:

| Field | Type | Default | Mutated by | Bootstrap value |
|---|---|---|---|---|
| `closed_cycles_count` | int ≥ 0 | `0` | brigadier on α-4 closed (D5 §5.5) | `0` |
| `active_skills_count` | int ≥ 0 | `0` | brigadier on α-3 validated (D11 §11.4) | `0` |
| `cross_theme_refs_count` | int ≥ 0 | `0` | /build-graph post-pass (§10.2.3) | `0` |
| `tombstone_rate_weekly` | float ≥ 0 | `0` | weekly /lint (§10.2.4) | `0` |
| `fpar_swarm_wide` | float ∈ [0,1] OR null | `null` | /lint PostToolUse (§10.2.1) | `null` |

`binding_scope: swarm-wide` is also part of the singleton schema (the
field is defined in D2 §2.3 for `foundations/<slug>.md`; for
`meta/health.md` (type: dashboard) it's an opt-in extension declaring
the dashboard's authoritative scope; `/lint` accepts it on this
singleton).


````markdown
---
id: meta-health
title: Swarm Health Dashboard
type: dashboard
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: ready
state: accepted
confidence: high
confidence_method: brigadier-attested-with-3-supports
tier: core
produced_by: brigadier
sources:
  - {path: "design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md", range: "D10"}
related: [[foundations/swarm-alphas]]
topics: [[topics/swarm-observability-hub]]
binding_scope: swarm-wide
# Live counters (updated by /lint scheduled run + meta-agent weekly)
closed_cycles_count: 0
active_skills_count: 0
cross_theme_refs_count: 0
tombstone_rate_weekly: 0
fpar_swarm_wide: null
---

# Swarm Health Dashboard

Updated automatically by `/lint` (PostToolUse + scheduled weekly per
Q5 #5 cadence) and by `meta-agent` weekly review. **Do not hand-edit
the structured-log sections** — append-only.

## 1. FPAR — First-Pass Acceptance Rate

**Definition.** Fraction of `Task()` returns accepted by the brigadier
on the first try (no rework / no rejection / no retry) over a rolling
window.

**Window:** rolling 20 invocations per agent (per-cell FPAR); rolling
100 invocations swarm-wide (aggregate FPAR).

**Computation source.**
- Per-Task return packet `state` after brigadier evaluation:
  `accepted` (first try) → `accepted_first_pass: true`.
- Recorded in `swarm/logs/<cycle-id>/events.md` per /ingest (D1 §1.3).

**Formula:**
```
FPAR = count(accepted_first_pass=true in window) / count(total_invocations in window)
```

**Threshold for alert.** `< 0.80` (per Sub-agent A §1 Q1 applicability
constraint). Below threshold → Q1 4-tier retrieval may be inadequate;
re-evaluate at /ask FPAR or move to Phase B (PPR/HyDE/embeddings).

**Structured log (append-only):**
```yaml
fpar_log:
  - {date: 2026-04-23, window: swarm-100, value: null, n: 0, alert: false}
```

## 2. Cycles

**Definition.** α-4 Cycle counts (D5 §5.5) across all states.

**Sources.**
- `closed_cycles_count` — frontmatter field above; incremented at α-4
  `closed` transition (D5 §5.5).
- Open / running / integrating / gated / compounded counts — derived
  from grep over `swarm/wiki/tasks/*/decisions/` for `alpha_state:`.

**Formula:**
```
closed_cycles_count = count(cycle-log.md files in swarm/logs/)
open_cycles = count(tasks with alpha_state ∈ {opened, running, integrating, gated, compounded})
cycle_close_rate_weekly = count(cycle-log.md created in last 7 days) / 7
```

**Q8 Layer-9 trigger #1.** `closed_cycles_count ≥ 50` (per Q8 +
Sub-agent A §1 Q8); first of three AND-conditions.

**Threshold for alert.** open_cycles > 5 → brigadier write-queue
contention (per Sub-agent A §1 Q2 applicability constraint); evaluate
CRDT switch.

**Structured log:**
```yaml
cycles_log:
  - {date: 2026-04-23, closed: 0, open: 0, weekly_rate: 0.0, layer9_trigger_1: false}
```

## 3. Cross-theme references

**Definition.** Edges in `swarm/wiki/graph/edges.jsonl` where
`from.niche != to.niche` (cross-niche) OR
`from.layer == 1 AND to.layer == 1 AND from.theme != to.theme`
(cross-theme-within-Layer-1).

**Sources.** Computed by `/build-graph` post-pass.

**Formula:**
```
cross_theme_refs_count = count of edges in swarm/wiki/graph/edges.jsonl satisfying
  (from_page.niche != to_page.niche)
   OR
  (from_page.layer == 1 AND to_page.layer == 1
   AND from_page.theme != to_page.theme)
```

**Q8 Layer-9 trigger #2.** `cross_theme_refs_count ≥ 3` AND
`count(themes with ≥50 concepts each) ≥ 2`. Second of three
AND-conditions per Q8 + Sub-agent A §1 Q8.

**Tension T2 watch.** If `cross_theme_refs_count == 0` after 20 closed
cycles, re-evaluate Q8 signal #2 (per Sub-agent A §4 T2 resolution).

**Structured log:**
```yaml
cross_theme_log:
  - {date: 2026-04-23, count: 0, themes_with_50_concepts: 0, layer9_trigger_2: false}
```

## 4. Tombstone rate per layer

**Definition.** Pages transitioning to α-2 `tombstoned` state per layer
per week (D5 §5.3 + D2 §2.4).

**Sources.** Grep `swarm/wiki/_archive/` for files with
`state: tombstoned` AND `last_modified` within the last 7 days; group
by source `layer` field.

**Formula:**
```
tombstone_rate_weekly[<layer>] = count(_archive files
  with state=tombstoned AND layer=<layer>
  AND last_modified in last 7 days) / 7
```

**Per-layer thresholds for alert (heuristic, Phase A):**

| Layer | Weekly threshold (alert if exceeded) | What it means |
|---|---|---|
| spine entity-types | 5 | high contradiction noise; review /ask synthesis quality |
| L1 themes | 2 | book-distillation churn; review brigadier sweep quality |
| L4 meta/agent-improvements | 1 | cross-agent improvement instability |
| L5 tasks (per-task content) | 2 (most tasks archive in place via α-1 `archived` rather than α-2 tombstone; high tombstone rate signals task-quality issues — closes critic-gate2 M6 — α-2 `tombstoned` is permitted on any layer per D5 §5.3) | |
| L7 global | 1 | promoted-rule churn; review compound step |
| L8 skills | 1 | pipeline leak; check D11 activation rubric |
| L9 insights | 0 (Phase A: any tombstone is a violation) | per Q8 phase_a_lock; surface via /lint |

**Structured log:**
```yaml
tombstone_log:
  - {date: 2026-04-23, layer: null, count: 0, weekly_rate: 0.0}
```

## 5. Active-skills count and validation ratio

**Definition.** Count of files in `swarm/wiki/skills/active/`; for
each, the success/loss ratio derived from `usage/<slug>.jsonl`.

**Sources.** `swarm/wiki/skills/active/` glob; `swarm/wiki/skills/usage/<slug>.jsonl`
per skill.

**Formula:**
```
active_skills_count = count(*.md in swarm/wiki/skills/active/)
for each active skill:
  success_count = grep '"outcome":"success"' usage/<slug>.jsonl | wc -l
  loss_count = grep '"outcome":"loss"' usage/<slug>.jsonl | wc -l
  validation_ratio = success_count / max(loss_count, 1)
  meets_q6 = (success_count + loss_count >= 10) AND (validation_ratio >= 3)
```

**Threshold per Q6 (D11 §11.5).** Skills failing `validation_ratio
< 1.0 over rolling 10 uses` are flagged for retirement (route
through tombstone per α-3 + D11).

**Structured log:**
```yaml
active_skills_log:
  - {date: 2026-04-23, count: 0, mean_ratio: null, below_threshold: []}
```

## 6. /lint findings summary

**Definition.** Per-class counts of `/lint` findings from the most
recent scheduled run + delta vs prior run.

**Sources.** The most recent `swarm/wiki/_lint-report-<YYYY-MM-DD>.md`.

**Formula:**
```
For each /lint check (10 total per D8 §8.5):
  current_count = count of findings under that check's section in latest report
  prior_count = same in second-most-recent report
  delta = current - prior
```

**Per-check tracking:**
1. Orphans
2. Stale claims (confidence×age + foundations 365-day re-review)
3. Broken wikilinks
4. Missing frontmatter
5. Contradictions integrity
6. Missing cross-refs
7. Index drift
8. α-2/α-3 lifecycle state validity (D8 §8.5 #8)
9. Triple-channel cross-ref consistency (D8 §8.5 #9)
10. Q8 Layer-9 lock (D8 §8.5 #10)

**Structured log:**
```yaml
lint_findings_log:
  - {date: 2026-04-23, report_path: null, counts: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, deltas: {}}
```

## 7. Brigadier load

**Definition.** (a) Pending Task drafts awaiting brigadier review;
(b) average review latency from draft creation to brigadier accept/reject.

**Sources.**
- Pending: glob `swarm/wiki/drafts/*.md` filtered by `state: drafted`
  AND no corresponding canonical write.
- Latency: per-draft `created` timestamp vs. corresponding canonical
  page `created` timestamp (where the canonical bears
  `derived_from: <draft-slug>`); average over rolling 20.

**Formula:**
```
pending_drafts_count = count of swarm/wiki/drafts/*.md with state=drafted
                       AND no matching swarm/wiki/<canonical-path>/<slug>.md
review_latency_avg_min = mean(canonical.created - draft.created in minutes)
                         over the rolling 20 most recently-promoted drafts
```

**Threshold for alert.** `pending_drafts_count > 5` → brigadier
write-queue saturated (per Sub-agent A §1 Q2 applicability constraint
echoed); evaluate workload re-allocation OR Phase-B CRDT switch.

**Structured log:**
```yaml
brigadier_load_log:
  - {date: 2026-04-23, pending: 0, latency_min: null}
```

## 8. Update mechanism

**Who updates:**
- `/lint` PostToolUse (per master synthesis §5.6.2 + D8 §8.5):
  updates `lint_findings_log` after every wiki write.
- `/lint` scheduled (per Q5 #5 cadence weekly): updates `cycles_log`,
  `cross_theme_log`, `tombstone_log`, `active_skills_log`,
  `brigadier_load_log`.
- `meta-agent` weekly review (per W-5 + D5 §5.4 α-3 audit role):
  composes a 5-line weekly summary appended to `## Weekly summary`
  section below; verifies counter consistency; flags drift.
- `brigadier` updates the live counters in frontmatter
  (`closed_cycles_count`, `active_skills_count`, etc.) at the relevant
  α-2/α-3/α-4 transitions.

**Cadence:**
- Live counters (frontmatter): mutated per α-state transition (event-driven).
- Structured logs: appended weekly (or per-event for `lint_findings_log`).
- Weekly summary: meta-agent composes Mondays UTC.

**Append-only discipline.** Per CLAUDE.md / `.claude/rules/global.md`
"Логи: append-only, новые записи сверху." Each `_log:` list grows; no
historical entry is deleted. Rotation: when a `_log:` exceeds 30
entries, the oldest 20 are moved to
`swarm/wiki/_archive/health-history-<YYYY>.md` (per CLAUDE.md
"Правила" #7).

## Weekly summary (append-only, meta-agent composes)

(Empty until first weekly review.)

````

### 10.3 Per-metric computation-formula table (master reference)

| Metric | Formula | Source files | Update trigger | Q8 / threshold |
|---|---|---|---|---|
| FPAR | accepted_first_pass / total_invocations over rolling N | `swarm/logs/<cyc>/events.md` | PostToolUse | <0.80 alert |
| closed_cycles_count | count(cycle-log.md in swarm/logs/) | `swarm/logs/*/cycle-log.md` | α-4 closed transition | ≥50 = Q8 trigger #1 |
| cycle_close_rate_weekly | created-last-7d / 7 | `swarm/logs/*/cycle-log.md` mtime | weekly /lint | informational |
| cross_theme_refs_count | count edges with cross-niche/cross-theme | `swarm/wiki/graph/edges.jsonl` | /build-graph | ≥3 + ≥2 themes×50 = Q8 trigger #2 |
| tombstone_rate_weekly[layer] | count tombstoned in 7d / 7 by layer | `swarm/wiki/_archive/*.md` | weekly /lint | per-layer table §10.2.4 |
| active_skills_count | count *.md in active/ | `swarm/wiki/skills/active/` | α-3 validated transition | n/a |
| validation_ratio per skill | success / max(loss,1) | `swarm/wiki/skills/usage/<slug>.jsonl` | per-invocation /ingest write | <1.0 over 10 → retire |
| /lint findings counts | per-check from latest report | `swarm/wiki/_lint-report-*.md` | PostToolUse + weekly | per-check per D8 |
| pending_drafts_count | drafts with state=drafted no canonical | `swarm/wiki/drafts/` glob | event | >5 alert |
| review_latency_avg_min | mean(canonical-draft) over 20 | drafts/ + canonical pages | event | informational |

### 10.4 Compatibility matrix

| Locked item | D10 honours by … |
|---|---|
| Q5 (5-signal /lint) | structured log per signal class; PostToolUse + scheduled cadence. |
| Q8 (3-AND Layer-9 trigger) | §10.2.2 + §10.2.3 expose `closed_cycles_count` + `cross_theme_refs_count` + theme-population check; D5 §5.5 α-4 closed counter. |
| Sub-agent A §4 T2 (cross-theme = 0 watch) | §10.2.3 explicit "20-cycle re-eval" note. |
| W-12 (1000% depth) | every metric: definition + formula + source + trigger + threshold + structured-log scaffold. |
| Sub-agent C §6 ("research silent — spec must specify") | All formulas closed: FPAR rolling window (20/100), tombstone-rate (per-layer 7-day), cross-theme threshold (≥3 + ≥2 themes×50). |
| Critic-gate1 M10 forward-reference | `closed_cycles_count` field exists in frontmatter; D1 §1.4 #13 bootstrap initialises it; α-4 closed transition increments. |
| Critic-gate1 H1 (cycle-log path) | references `swarm/logs/<cycle-id>/cycle-log.md` per the corrected D1 §1.3. |
| §5.5.5 provenance gate (D6 §6.3) | brigadier-attested-with-3-supports method (the metric-counter-update events serve as the supports). |
| Max-subscription (D6 §6.10) | all computations are filesystem reads; no embeddings, no SDK. |

---

## DELIVERABLE 11 — Q6 Skill Activation-vs-Validation Rubric (resolves T3)

### 11.1 Mandate, T3 framing, and naming alignment

T3 (per Sub-agent A §4) resolves the tension between **activation**
(when a candidate skill becomes part of the live registry) and
**validation** (when a candidate is demonstrably effective). The
critic-gate1 S2 fix locked α-3 to 4 states per FPF Part 4 §4.3:
`proposed → active → validated ⇄ active → tombstoned` (no separate
`retired`). This deliverable is the operational rubric that drives
α-3 transitions for skills.

**Naming alignment** (carried from D5 §5.4 alias table):

| FPF state (canonical) | D11 spec alias | Filesystem location |
|---|---|---|
| `proposed` | `candidate` | `swarm/wiki/skills/candidates/<slug>/manifest.md` |
| `active` | `learning` | `swarm/wiki/skills/learning/<slug>/manifest.md` + `golden-set.jsonl` |
| `validated` | `active` (live) | `swarm/wiki/skills/active/<slug>.md` + D9 symlink |
| `tombstoned` | `tombstoned` | `swarm/wiki/_archive/skills/<slug>.md` |

D11 uses FPF state names canonically; spec aliases shown in
parentheses for cross-reference. The transitions and predicates below
are testable from filesystem alone (per W-12 + critic-gate1 H2 fix).

### 11.2 Skill candidate intake (transition: none → `proposed`)

**Trigger.** Compound step at α-1 `compounded` (D5 §5.2) writes a DRR
entry to `agents/<expert>/strategies.md` (Level-1) OR
`swarm/wiki/skills/candidates/<slug>/manifest.md` (Level-2 — if the
brigadier judges the pattern broad enough for swarm-wide skill).

**Predicate (none → `proposed`):**
- A new file at `swarm/wiki/skills/candidates/<slug>/manifest.md`
  with frontmatter `skill_state: candidate` AND
  4-part DRR populated (`context:`, `decision:`, `alternatives:`,
  `review_checkpoint:`).
- The DRR `proposed_by:` field set per Q6 R4 owner table (see §11.7).

**No golden set required at this stage.** Candidates are open ideas;
goldens come at `learning`.

### 11.3 Activation gate I (transition: `proposed` → `active`/`learning`)

**Trigger.** First successful application by any cell.

**Activation predicate (all conditions ANDed):**

1. **Golden-set seeded:** file
   `swarm/wiki/skills/learning/<slug>/golden-set.jsonl` exists with
   **≥3 cases** (per Q6 + Sub-agent C §5). Each case: JSONL line with
   `{input: <…>, expected_output: <…>, acceptance_predicate: <…>}`.
2. **Use-log seeded:** file
   `swarm/wiki/skills/usage/<slug>.jsonl` exists with **≥1 success
   record** ({outcome: success, ts: …, task_id: …}).
3. **Brigadier sign-off:** the most recent commit moving the
   `manifest.md` from `candidates/` to `learning/` was authored by
   the brigadier (per D6 §6.2 single-writer); commit message format
   per D6 §6.2.4.
4. **Frontmatter updated:** the manifest's `skill_state` advances from
   `candidate` to `active` (FPF) / `learning` (alias); `n_uses`
   field set to 1 or more.

**Filesystem-resident predicate** (lint-checkable, per W-12). All
predicate templates below use `${slug}` for explicit template
substitution (per critic-gate2 SS4); Стадия D substitutes the actual
skill slug. **Frontmatter values use D2 §2.4 spec-alias enum**
(`{candidate|learning|active|tombstoned}`) per critic-gate2 SS1.
The "FPF state" name is the canonical alpha state per D5 §5.4; the
on-disk frontmatter value is the spec alias.

```
fpf_state[${slug}] == "active" (alias "learning") iff
  exists(swarm/wiki/skills/learning/${slug}/manifest.md)
  AND exists(swarm/wiki/skills/learning/${slug}/golden-set.jsonl)
  AND wc -l < swarm/wiki/skills/learning/${slug}/golden-set.jsonl > 3
  AND grep '"outcome":"success"' swarm/wiki/skills/usage/${slug}.jsonl | wc -l >= 1
  AND frontmatter.skill_state == "learning"     # D2 §2.4 spec-alias enum
  AND exists(swarm/wiki/skills/learning/${slug}/.activation-attestation.md)
                                                # marker file written by brigadier
                                                # at α-3 transition (closes critic-gate2 H8;
                                                # eliminates commit-message predicate)
  AND grep 'attested_by: brigadier' swarm/wiki/skills/learning/${slug}/.activation-attestation.md
```

**Owner per Q6 R4:** brigadier (writes the activation; meta-agent or
expert may have drafted the candidate via `mode: writing-support` per
D6 §6.8).

### 11.4 Activation gate II (transition: `active`/`learning` → `validated`)

**Trigger.** Skill has accumulated sufficient evidence for promotion
to the live registry.

**Activation predicate (all conditions ANDed):**

1. **Golden-set ≥3 satisfied:** all ≥3 golden-set cases have
   `acceptance_predicate` returning true on the most recent run
   (per Sub-agent C §5; brigadier executes the goldens before promotion).
2. **Validated success ratio ≥3:1:** in
   `swarm/wiki/skills/usage/<slug>.jsonl`, success records outnumber
   loss records by at least 3:1.
3. **Minimum N=10 uses:** total recorded invocations
   `(success + loss) ≥ 10`.
4. **Brigadier sign-off via §5.5.5 provenance gate (D6 §6.3):** the
   commit promoting the canonical from `learning/<slug>/manifest.md`
   to `active/<slug>.md` AND creating the D9 symlink is brigadier-
   authored. The §5.5.5 gate verifies `sources[]` non-empty (the
   golden-set cases qualify as `sources[]` entries).

**Filesystem-resident predicate** (lint-checkable; `${slug}` is
template-substituted per critic-gate2 SS4; frontmatter uses spec-alias
enum per critic-gate2 SS1):
```
fpf_state[${slug}] == "validated" (alias "active" — live in registry) iff
  exists(swarm/wiki/skills/active/${slug}.md)
  AND exists(.claude/skills/${slug}.md)            # D9 symlink
  AND readlink(.claude/skills/${slug}.md) == "../../swarm/wiki/skills/active/${slug}.md"
  AND golden_set_pass_count == golden_set_total
  AND success_count >= 3 * loss_count
  AND (success_count + loss_count) >= 10
  AND frontmatter.skill_state == "active"          # D2 §2.4 spec-alias enum
  AND exists(swarm/wiki/skills/active/.${slug}.activation-attestation.md)
                                                   # marker file (closes critic-gate2 H8)
```

**Owner per Q6 R4:** brigadier writes; meta-agent runs golden-set
audit pre-write (`mode: writing-support` returns the audit verdict).

### 11.5 Retirement / tombstoning predicates

Per critic-gate1 S2 fix, α-3 has no `retired` state. There are two
backward transitions out of `validated`:

**(a) Demotion: `validated` → `active`/`learning`** (loop per D5 §5.4):

**Predicate:**
- Rolling 10 most-recent uses: `success_count / max(loss_count, 1) <
  3.0` AND `>= 1.0`.

Brigadier moves canonical back to `learning/`, removes D9 symlink. The
skill returns to `learning` for re-evaluation. Owner: meta-agent
emits drift-alert via `mode: writing-support`; brigadier executes the
move.

**(b) Tombstoning: any state → `tombstoned`:**

**Predicates (any one triggers):**
1. **Catastrophic ratio:** rolling 10 most-recent uses
   `success_count / max(loss_count, 1) < 1.0` (loss-dominated).
2. **Superseded:** another `validated` skill bears `supersedes:
   [[<this-slug>]]` in its frontmatter (D3 §3.2.7).
3. **Production incident:** an entry in `swarm/wiki/log.md` of the form
   `## [<date>] incident | <task-id> | caused-by: <slug>` cites this
   skill, AND the incident is not already resolved (no
   `## [<date>] incident-resolved | <task-id>` follow-up).
4. **Ruslan-attested withdrawal:** ack of an
   `AWAITING-APPROVAL-tombstone-skill-<slug>-*.md` gate file (D6 §6.5).

**Filesystem-resident tombstoning predicate:**
```
state[<slug>] == "tombstoned" iff
  exists(swarm/wiki/_archive/skills/<slug>.md)
  AND NOT exists(swarm/wiki/skills/active/<slug>.md)
  AND NOT exists(.claude/skills/<slug>.md)
  AND frontmatter.tombstoned_by != null
  AND frontmatter.skill_state == "tombstoned"
```

### 11.6 Worked examples

#### 11.6.1 Activation — `query-pricing-models` (FPF `validated` reached)

State at ratio = 5:1, n=15, golden-set 5/5 pass.

```
swarm/wiki/skills/learning/query-pricing-models/
  ├── manifest.md                       (skill_state: learning, n_uses: 15)
  ├── golden-set.jsonl                  (5 lines)
  └── .activation-attestation.md        (attested_by: brigadier, ts: 2026-05-30, criteria_passed: gate-I)
swarm/wiki/skills/usage/query-pricing-models.jsonl  (15 lines, 12 success / 3 loss)
```

**Predicate check (§11.4):**
- exists active/<slug>.md? NO (still in learning) — must be created.
- golden-set.jsonl wc -l == 5; pass = 5/5; ✓
- 12 / 3 = 4.0 ≥ 3.0; ✓
- 12 + 3 = 15 ≥ 10; ✓

**Brigadier action:**
1. Run all 5 goldens; verify 5/5 pass.
2. Write attestation file:
   `swarm/wiki/skills/active/.query-pricing-models.activation-attestation.md`
   with frontmatter `attested_by: brigadier, ts: 2026-05-30, criteria_passed: gate-II,
   golden_pass: 5/5, ratio: 4.0` (closes critic-gate2 H8 — replaces
   commit-message-predicate with marker file).
3. Move `learning/query-pricing-models/manifest.md` → `active/query-pricing-models.md`.
4. Update frontmatter: `skill_state: active` (D2 §2.4 spec-alias enum;
   FPF α-3 state is `validated`), `n_uses: 15`, `success_count: 12`,
   `loss_count: 3`.
5. Create D9 symlink: `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md
   .claude/skills/query-pricing-models.md`.
6. Append to `swarm/wiki/log.md`:
   `## [2026-05-30] activate-skill | query-pricing-models | golden-set: 5/5; ratio: 4.0`.
7. Increment `swarm/wiki/meta/health.md`'s `active_skills_count`.
8. Commit: `[brigadier] cyc-2026-05-30-am: activate skill query-pricing-models per D11 §11.4`.

#### 11.6.2 Demotion — `summarise-meeting-notes` (drift detected)

State at validated, last 10 uses: 4 success / 6 loss (ratio = 0.67,
which is <1.0 → tombstone candidate, NOT demote).

If instead 5 success / 5 loss (ratio = 1.0; in the demotion band 1.0
≤ ratio < 3.0):

**Brigadier action (per §11.5(a)):**
1. Move `active/summarise-meeting-notes.md` → `learning/summarise-meeting-notes/manifest.md`.
2. Update frontmatter: `skill_state: learning` (D2 §2.4 spec-alias enum;
   FPF α-3 state is the demoted `active`), set `success_count: 5`,
   `loss_count: 5`.
3. Remove D9 symlink: `rm .claude/skills/summarise-meeting-notes.md`.
4. Remove activation-attestation marker: `rm swarm/wiki/skills/active/.summarise-meeting-notes.activation-attestation.md`.
5. Append to log: `## [<date>] demote-skill | summarise-meeting-notes | rolling-10 ratio 1.0; back to learning`.
6. Decrement `active_skills_count`.

#### 11.6.3 Tombstoning — `parse-html-table` (production incident)

Skill caused a misparse that propagated bad data into a wiki claim;
incident logged.

```
swarm/wiki/log.md (recent):
  ## [2026-06-15] incident | task-2026-06-15-extract-pricing | caused-by: parse-html-table
  ...
  (no follow-up incident-resolved line)
```

**Predicate check (§11.5(b) #3):** ✓ active incident.

**Brigadier action:**
1. Move `swarm/wiki/skills/active/parse-html-table.md` →
   `swarm/wiki/_archive/skills/parse-html-table.md`.
2. Update frontmatter: `skill_state: tombstoned`,
   `tombstoned_by: [[wiki/log.md#L<incident-line>]]`.
3. Remove D9 symlink: `rm .claude/skills/parse-html-table.md`.
4. Append to log: `## [2026-06-16] tombstone-skill | parse-html-table | per-incident task-2026-06-15-extract-pricing`.
5. Increment `tombstone_rate_weekly` for L8.
6. Commit per D6 §6.2.4.

### 11.7 Owner roles per transition (per Q6 R4 + Sub-agent A §3 R4)

| Transition | Propose (drafter) | Eval | Activate | Audit | Retire / Tombstone |
|---|---|---|---|---|---|
| none → `proposed` | any agent OR Ruslan (writes DRR via `mode: writing-support`) | n/a | n/a | n/a | n/a |
| `proposed` → `active` | brigadier (or owning expert in `mode: writing-support` returns draft) | brigadier | brigadier | n/a | n/a |
| `active` → `validated` | brigadier OR owning expert in `mode: writing-support` returns draft | brigadier (runs golden-set) | brigadier (under §5.5.5 gate) | meta-agent (audit before activation) | n/a |
| `validated` → `active` (demoted) | meta-agent emits drift-alert | meta-agent (rolling-ratio check) | n/a (it's a demotion) | meta-agent | n/a |
| any → `tombstoned` | meta-agent OR Ruslan OR brigadier (incident-driven) | brigadier (verifies tombstone trigger) | n/a | meta-agent (post-tombstone audit) | meta-agent OR Ruslan |

All transitions are **commit-by-brigadier** per Q2 single-writer (D6
§6.2). Meta-agent and experts emit drafts via `mode: writing-support`
per D6 §6.8 (Sub-agent A §6 #10 conflict resolved per Gate 1).

### 11.8 Anti-T3 clause (resolves T3 explicitly)

**Tension T3 (Sub-agent A §4):** "Activation = golden-set ≥80% binary;
validation = usage-driven (≥10 uses + ≥3:1). Стадия C MUST write
explicit rubric distinguishing the two gates."

**Resolution.** The rubric distinguishes:

- **Activation gate I** (§11.3, `proposed → active`): seeded
  state — first success + golden-set existence + brigadier intake.
  No usage requirement.
- **Activation gate II** (§11.4, `active → validated`): validated
  state — all goldens pass + ≥10 uses + ≥3:1 ratio + brigadier
  §5.5.5 sign-off.

**Anti-T3 enforcement:** validation evidence MUST be filesystem-resident
**before** activation gate II. Specifically:

1. The golden-set file (`golden-set.jsonl`) MUST be committed, not
   verbal/in-context.
2. The use-log file (`usage/<slug>.jsonl`) MUST contain ≥10 timestamped
   records, not aggregated estimates.
3. The brigadier's promotion commit MUST cite the
   `usage/<slug>.jsonl` and `golden-set.jsonl` paths in its
   `sources[]` frontmatter (§5.5.5 provenance gate D6 §6.3).
4. **No verbal validation.** A skill cannot be promoted because "it
   feels good" — the rubric is filesystem-checkable, not
   conversation-checkable.

`/lint` enforces by checking that every `.claude/skills/<slug>.md`
symlink target satisfies §11.4 predicate; non-conforming symlinks are
flagged as anti-T3 violations.

### 11.9 Compatibility matrix

| Locked item | D11 honours by … |
|---|---|
| Q6 (skill-learning pipeline) | activation predicate exact: golden-set ≥3, ratio ≥3:1, ≥10 uses, brigadier sign-off (all ANDed). |
| R4 (Q6 owners locked) | §11.7 table aligns to R4 owner roles per Sub-agent A §3. |
| T3 (activation-vs-validation tension) | §11.8 anti-T3 clause; filesystem-resident evidence required. |
| Q2 single-writer | every transition committed by brigadier; meta-agent/expert via `mode: writing-support`. |
| α-3 4-state lock (critic-gate1 S2) | only `proposed/active/validated/tombstoned`; `retired` route handled via demotion loop OR tombstone. |
| W-9 (skills first-class) | each skill has full lifecycle with golden-set + use-log + symlink. |
| W-12 (1000% depth) | every predicate filesystem-checkable; 3 worked examples; owner table; commit messages spelled out. |
| §5.5.5 provenance gate (D6 §6.3) | activation gate II requires §5.5.5 sign-off citing golden-set + use-log paths. |
| D9 (symlink convention) | references D9 §9.4 symlink-creation script; D9 §9.5 removal. |
| D10 (health.md) | references `active_skills_count` increment; `tombstone_rate_weekly` increment. |
| Sub-agent C §5 ("research silent on golden-set storage") | golden-set.jsonl format specified: JSONL line per case with `{input, expected_output, acceptance_predicate}`. |
| Sub-agent C §8 #9 (never-delete-only-archive) | tombstone moves to `_archive/`, doesn't delete. |
| Critic-gate1 H2 (filesystem-only predicates) | every predicate uses file existence + grep counts + frontmatter fields, no commit-message tests. |

---

## DELIVERABLE 12 — Strategies.md Trio Collapse (resolves T5)

### 12.1 Mandate and T5 framing

**Tension T5** (Sub-agent A §4 + §1 Q2 + Section 5): three candidate
locations for "strategies" content existed in the v2/v3 specification
sketch:

- (a) `agents/<expert>/strategies.md` — per-expert System Prompt
  Learning per CLAUDE.md per-agent memory layer.
- (b) `swarm/strategies/<expert>.md` — proposed v3 swarm-wide venue
  (BUILD §1.2 layout sketch).
- (c) `swarm/wiki/meta/agent-improvements/<expert>-<date>.md` —
  W-4 agent-improvement layer.

Per **R6** (locked, all R-items accepted) + **WIKI-V3-MECHANICS Part 2
§Q2 L178–187** + Sub-agent A §4 T5 + §3 R6: collapse to **2 venues**
— **KEEP (a) + (c), DROP (b).**

This deliverable specifies the migration mechanics, cross-venue sync
rule, and the `/lint` enforcement that catches T5 violations.

### 12.2 Venue 1 — `agents/<expert>/strategies.md` (KEEP, Level-1)

**Path.** `agents/<expert>/strategies.md` (project-root-relative;
NOT under `swarm/`).

**Naming convention.** One file per expert. The 5 files at Стадия D
bootstrap (per D1 §1.4 #16):
- `agents/engineering-expert/strategies.md`
- `agents/mgmt-expert/strategies.md`
- `agents/systems-expert/strategies.md`
- `agents/philosophy-expert/strategies.md`
- `agents/investor-expert/strategies.md`

**Owner write rights.** **Expert direct** (the only path-write
exception to Q2 single-writer per D1 §1.3 perm table). Each expert
writes to its own `agents/<expert>/strategies.md` directly without
brigadier mediation. Justification: this file is the expert's
**personal memory layer** (CLAUDE.md per-agent memory section
"Strategies"); subject to the expert's own self-improvement loop, not
swarm coordination. Brigadier monitors via §12.4 sync rule.

**Content shape** (per CLAUDE.md per-agent memory + α-3 DRR):
append-only YAML-block-per-entry, newest on top. Each entry:

```yaml
---
- date: 2026-04-23
  task_id: task-2026-04-23-foo
  context: <when this rule applies>
  decision: <the rule>
  alternatives: <considered>
  review_checkpoint: <when to re-evaluate>
  skill_state: candidate         # α-3 entry tracking
  proposed_by: <self-ref or brigadier>
  validation_status: proposed
---
```

**Lifecycle.** Entries live as α-3 `proposed` candidates. They may be
promoted to swarm-wide via §12.4 sync rule.

**Phase A bootstrap content** (per D1 §1.4 #16): each file has empty
body + frontmatter only:

```yaml
---
title: Strategies — <Expert Name>
type: per-agent-memory
layer_note: project-root, not under swarm/ (T5/R6)
expert: <slug>
created: 2026-04-23
last_modified: 2026-04-23
state: drafted
---

# <Expert Name> — Strategies (Level-1)

(Empty. Append entries newest-on-top per CLAUDE.md "Логи" rule.)
```

### 12.3 Venue 2 — `swarm/wiki/meta/agent-improvements/...` (KEEP, Level-2)

**Path.** `swarm/wiki/meta/agent-improvements/<file>` per D1 §1.3 perm
table + §1.2 tree.

**Naming conventions.** Per D1 §1.4 #14 (7 files at bootstrap):

- Per-expert improvement records: `<expert>-improvements.md` (5 files,
  one per expert: `engineering-expert-improvements.md`, …).
- System-level orchestration improvements:
  `system-level-improvements.md`.
- Cross-agent emergent insights: `emergent-insights.md`.

For new dated entries within these files, append-only YAML-block-per-
entry per α-3 DRR (same shape as §12.2 plus
`validation_status: under-validation|accepted|rejected|tombstoned`
per D2 §2.4 Layer 4 schema).

**Owner write rights.** **Brigadier-write only** (per Q2 single-
writer + D6 §6.2.2 per-layer write paths). Drafts come from any
expert (any mode) via `Task(...)` return packets, OR from
meta-agent in `mode: writing-support` (D6 §6.8); brigadier evaluates
the §5.5.5 gate (D6 §6.3) and writes.

**Content shape.** Same as §12.2 entry shape, plus the Layer-4
specific frontmatter from D2 §2.4 (`expert`, `improvement_target`,
`validation_status`, `proposed_by`, `applied_by`, `applied_at`).

**Lifecycle.** Entries flow through α-3
`proposed → active → validated ⇄ active → tombstoned` per D5 §5.4 +
D11. Activation rubric per D11 applies (golden-set ≥3, ratio ≥3:1,
≥10 uses) — though for prompt-edit improvements the "uses" are
brigadier observations across cycles rather than skill invocations.

### 12.4 Sync rule — Level-1 → Level-2 promotion

**Trigger.** When a per-expert insight in `agents/<expert>/strategies.md`
appears to apply broadly (heuristic: same insight surfaced by ≥2
experts independently OR cited by brigadier in ≥3 cycles).

**Promotion flow** (driven by α-1 `compounded` step in D5 §5.2):

1. **Expert proposes.** Expert returns a Task packet with an
   `escalations[]` entry: `{trigger: promote-to-swarm-wide, source:
   agents/<expert>/strategies.md#L<line>, justification: <…>}`.
2. **Brigadier evaluates.** Reads the cited Level-1 entry; checks for
   ≥2-expert independent surfacing (grep `agents/*/strategies.md` for
   semantic match) OR brigadier-cited count ≥3 (grep `swarm/logs/*/cycle-log.md`
   for `applied-rule: <slug>`).
3. **Brigadier drafts Level-2 entry.** Composes a new YAML-block entry
   for the relevant `swarm/wiki/meta/agent-improvements/<file>.md`.
   The Level-2 entry inherits the Level-1 content + adds
   `proposed_by: <originating-expert>(s)`, `cited_in: [<Level-1 paths>]`,
   `validation_status: proposed`.
4. **§5.5.5 gate.** Brigadier verifies the Level-2 entry's `sources[]`
   = the Level-1 paths cited (D6 §6.3 acceptance condition #1
   satisfied via inter-wiki source).
5. **Commit.** Brigadier appends the Level-2 entry, commits per D6
   §6.2.4. The Level-1 entries remain in place (they're the
   per-expert memory; not deleted on promotion — they cross-reference
   the Level-2 record via `promoted_to: [[meta/agent-improvements/<file>#<entry>]]`).
6. **α-3 progression.** The Level-2 entry advances per D11 rubric:
   `proposed → active → validated` once observed in ≥10 cycles with
   ≥3:1 success ratio.

**No demotion path.** Level-2 entries don't demote back to Level-1;
they tombstone (per α-3) if they fail validation.

### 12.5 Dropped venue — `swarm/strategies/` (R6 + T5)

**Path (rejected).** `swarm/strategies/<expert>.md` and any sibling
under `swarm/strategies/`.

**Rationale.** Sub-agent A §1 Q2 + §3 R6 + §4 T5 + §6 #8 (BUILD §1.2
layout amendment): this venue would duplicate Level-1 (per-expert
memory belongs in `agents/`) and Level-2 (swarm-wide improvements
belong in `swarm/wiki/meta/agent-improvements/`). Three venues for
one content type guarantees drift. Q2 + R6 collapse to two.

**Migration note.** No migration data exists in
`swarm/strategies/` at Стадия C close (the dir was a hypothesis in
BUILD §1.2 §1.2 L76–L82, never instantiated). Стадия D MUST NOT
create the directory. If any data accidentally lands there during
Phase A (e.g. from a stale BUILD-§1.2-following script), brigadier
migrates per the rules below before next commit:

- For per-expert content → move to `agents/<expert>/strategies.md`
  (append, newest-on-top).
- For swarm-wide content → draft a Level-2 entry per §12.3 + §12.4;
  brigadier commits via §5.5.5 gate.
- Then `rm -rf swarm/strategies/`. Append a log line:
  `## [<date>] migrate | T5/R6 | swarm/strategies/ → agents/ + meta/agent-improvements/`.

### 12.6 `/lint` rule (D8 §8.5 extension #11 — explicit T5 violation check)

`/lint` gains an additional check (logical extension of the existing
10 checks; this is check #11):

```
For each file under swarm/strategies/ (the dropped path):
  EMIT "T5/R6 violation: swarm/strategies/<path> exists; should not (per D12 §12.5)."
  Brigadier action: migrate per §12.5.
```

This catches:
- Stale code that still creates `swarm/strategies/` files.
- Manual error.
- Phase-A bootstrap drift.

### 12.7 Worked example — promotion of a brigadier-orchestration insight

**Setup.**
- Engineering-expert appended this entry to
  `agents/engineering-expert/strategies.md` on 2026-04-30:
  `decision: 'When the cell return packet has dissents[] non-empty,
  prefer integrator-mode synthesis over critic-mode rebuttal.'`
- Mgmt-expert independently appended a similar entry to
  `agents/mgmt-expert/strategies.md` on 2026-05-12.

**Promotion (per §12.4):**
1. Engineering-expert in next Task return: `escalations[]: [{trigger:
   promote-to-swarm-wide, source: 'agents/engineering-expert/strategies.md#L42',
   justification: 'mgmt-expert independently surfaced same pattern; see
   agents/mgmt-expert/strategies.md#L17'}]`.
2. Brigadier reads both Level-1 entries, confirms semantic alignment.
3. Brigadier drafts Level-2 entry in `swarm/wiki/meta/agent-improvements/system-level-improvements.md`:
   ```yaml
   ---
   - date: 2026-05-13
     improvement_target: protocol      # per D2 §2.4 Layer-4 enum
     decision: 'On dissents[] non-empty Task returns, brigadier prefers
                integrator-mode synthesis (Task(<expert>-integrator)) over
                critic-mode rebuttal.'
     proposed_by: engineering-expert + mgmt-expert (independent surfacing)
     cited_in:
       - agents/engineering-expert/strategies.md#L42
       - agents/mgmt-expert/strategies.md#L17
     validation_status: proposed
     skill_state: candidate
   ---
   ```
4. Brigadier passes §5.5.5 gate (sources[] = the two Level-1 paths;
   non-empty; both are tier: core).
5. Brigadier commits: `[brigadier] cyc-2026-05-13-am: promote
   dissents-integrator-preference rule to Level-2`.
6. Brigadier annotates the two Level-1 entries with
   `promoted_to: [[meta/agent-improvements/system-level-improvements#2026-05-13]]`.

### 12.8 Compatibility matrix

| Locked item | D12 honours by … |
|---|---|
| T5 (strategies trio collapse) | §12.1–§12.5 explicitly: keep (a) + (c), drop (b). |
| R6 (drop swarm/strategies/) | §12.5 + §12.6 lint enforcement. |
| Q2 single-writer | §12.3 brigadier-write only for Level-2; §12.2 Level-1 expert-direct exception documented + scoped. |
| W-4 agent-improvement layer | §12.3 path matches D1 Layer 4 perm table. |
| W-5 two-level CE | §12.2 Level-1 + §12.3 Level-2 + §12.4 sync rule operationalises Level-1↔Level-2 flow. |
| §5.5.5 provenance gate (D6 §6.3) | §12.4 #4 gate verification at promotion; §12.7 worked example shows sources[] inheritance. |
| α-3 lifecycle (D5 §5.4) | §12.3 Level-2 entries follow α-3 proposed→active→validated→tombstoned. |
| D11 (skill activation rubric) | §12.4 #6 progression aligns with D11 rubric. |
| CLAUDE.md per-agent memory (Strategies layer) | §12.2 cites + matches: `agents/<expert>/strategies.md` is the existing per-agent memory location; no path change. |
| BUILD §1.2 layout amendment | §12.1 + §12.5 documents the deliberate drop of `swarm/strategies/` from BUILD §1.2 (Sub-agent A §6 #8). |
| Sub-agent A §1 Q2 §178–187 + §4 T5 + §3 R6 | §12.1 cites + materialises. |

---

## GATE 2 SUMMARY (D7–D12)

This gate covers the **operational integration surface**:

- **D7** — `.claude/config/wiki-roots.yaml` parameterisation config.
- **D8** — 5 in-scope skill diffs (`/ingest`, `/ask`, `/lint`,
  `/consolidate`, `/build-graph`) ~115 lines total + 3 documented
  exclusions (`/search-kb`, `/sweep-notion-bank`, `/compile`).
- **D9** — `.claude/skills/` symlink convention with α-3 lifecycle hooks.
- **D10** — `swarm/wiki/meta/health.md` skeleton (8 sections + master
  computation table; closes Sub-agent C §6 silent-formula gaps).
- **D11** — Q6 skill activation-vs-validation rubric resolving T3
  with two-gate distinction + filesystem-resident anti-T3 enforcement.
- **D12** — T5 strategies trio collapse (KEEP `agents/<expert>/strategies.md`
  Level-1 + `swarm/wiki/meta/agent-improvements/` Level-2; DROP
  `swarm/strategies/`); migration mechanics + sync rule + lint check.

### Critic-gate2 fixes applied pre-gate

All 4 showstoppers and all 8 high findings from
`raw/research/step-2-2-3c-extractions/critic-gate2.md` were applied
before this commit:

- **SS1** D11 frontmatter writes use D2 §2.4 spec-alias enum
  (`{candidate|learning|active|tombstoned}`) instead of FPF-canonical
  names. Predicates and worked examples updated. Alignment table at
  D11 §11.1 reinforces the FPF↔spec-alias mapping.
- **SS2** D8 §8.7 #7 build-graph diff line ref corrected: the
  `wiki/graph/communities.md` line is L62 (not L60 as previously
  hedged). Diff entry now spells the verbatim before/after.
- **SS3** D8 §8.6 #8 /consolidate no longer mutates canonical α-2
  `state` field (would violate Q2 single-writer; consolidate runs as
  expert per D6 §6.6.3 role_tool_matrix). Loser file is archived with
  HTML comment annotation; brigadier later transitions α-2
  `state: superseded` in a separate commit per D5 §5.3.
- **SS4** D11 §11.4 + §11.3 predicates use `${slug}` template
  substitution instead of literal `<slug>.md` (clarifying note added).
- **H1** D9 §9.3 slug regex aligned to D2 §2.2 `id` body half:
  `^[a-z0-9-]{1,60}$`.
- **H2 + H3** D10 frontmatter singleton-exemption + 5 live-counter
  fields explicitly typed/defaulted; `binding_scope` declared as
  opt-in extension for the dashboard.
- **H4** D7 §7.4 algorithm dead-code check replaced with explicit
  `default_root` value validation (`{wiki_root_v2, wiki_root_v3}`)
  and `exit 3` on misconfiguration.
- **H5** D8 §8.5 check #9 wikilink regex specified:
  `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]`; non-matching
  forms warn-not-error.
- **H6** D8 §8.5 check #10 reformulated to test file existence under
  `${WIKI_ROOT}/insights/{candidates,promoted}/*.md` (Phase-A boilerplate
  in effect) rather than a `phase_a_lock` frontmatter field that D1
  §1.6 didn't define.
- **H7** D9 §9.6 step 4 stores migration record in frontmatter
  (`migrated_from`, `migration_date`, `migration_note`) instead of
  a body section (D4 templates have no migration-section schema).
- **H8** D11 §11.3 + §11.4 predicates replaced commit-message check
  with marker file `swarm/wiki/skills/{learning|active}/.${slug}.activation-attestation.md`
  (filesystem-resident; lint-checkable).

7 medium findings: M3 + M6 inline-fixed (lifecycle branching by
page-type; L5 tombstone-rate threshold). Other mediums + 5 lows
deferred to Phase-A errata.

### Stage-Gated process

This file is committed and pushed as
`design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md`.

**Pause for Ruslan approval.** Final consolidation
(`design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md`
unifying D1–D12) follows after both gates approved.

---





