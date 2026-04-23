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
| 11 | (after L17 "Проверки") | (existing 7 checks) | **NEW SECTION:** "### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)" — flag pages with `state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}` (D5 α-2 8-state set). "### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)" — every inline `[[type/slug]]` MUST appear in `related[]` AND produce one record in `${WIKI_ROOT}/graph/edges.jsonl`. "### 10. Q8 Layer-9 lock (per D1 §1.6)" — flag any non-README write under `${WIKI_ROOT}/insights/` when `phase_a_lock: true`. | extends /lint to cover Q5 5-signal + Q3 triple-channel reconciliation + Q8 lock per D2 + D3 |

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
| 8 | L73 | `   - Перед удалением — создать копию в \`wiki/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A").` | `   - Перед удалением — создать копию в \`${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A"). **Установить B's frontmatter \`state: superseded\`, \`superseded_by: [[<A-path>]]\` per α-2 (D5 §5.3).**` | path + α-2 lifecycle integration |
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
| 7 | L62 | `Перезаписать секцию \`## Кластеры\`:` | (no change to this line; nearby line 60: `Обновить \`${WIKI_ROOT}/graph/communities.md\`` replaces `Обновить \`wiki/graph/communities.md\``) | path |
| 8 | L73 | `Обновить \`wiki/graph/summaries.md\`` (or nearby) | `Обновить \`${WIKI_ROOT}/graph/summaries.md\`` | path |
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

- Regex `^[a-z0-9][a-z0-9-]{0,49}$` (kebab-case; ≤50 chars; starts
  with letter or digit; per critic-gate1 H7 kebab-slug discipline).
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

**Step 4 — append migration note** in the v3 canonical file
(`swarm/wiki/skills/active/<slug>.md`):

```markdown
## Migration note

This skill was migrated from a v2 implementation at
`.claude/skills/<slug>_v2.md` (preserved for audit). Original was
deprecated on `<YYYY-MM-DD>` per D9 §9.6. Differences from v2: <one
or two lines>.
```

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


