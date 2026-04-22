---
sources:
  - wiki/ (overview, index, log, _templates/, graph/, sample entries)
  - .claude/skills/ (8 wiki-related)
  - CLAUDE.md Wiki Architecture v2 section
extracted_by: W-3
date: 2026-04-23
scope: current-state audit for Q9 + evidence on Q1/Q2/Q3/Q5/Q6
---

# W-3 extraction — existing wiki v2 infrastructure audit

## A. Current directory structure

Top level of `wiki/`:

```
wiki/
├── overview.md, index.md (186L), log.md (112L)
├── _lint-report-2026-04-16.md, _lint-report-2026-04-16-v2.md
├── _templates/   (9 files: claim, concept, entity, experiment,
│                  foundation, idea, source, summary, topic)
├── concepts/     (8 entries)
├── entities/     (4 entries: jetix, claude-code, github, linux)
├── sources/      (271 entries — dominant)
├── ideas/        (257 entries — dominant)
├── claims/       (5 entries)
├── topics/       (1 entry: system-design-hub)
├── experiments/  (0)
├── summaries/    (0)
├── foundations/  (0)
├── comparisons/  (0 — /ask output loop never triggered yet)
├── niches/       (6 subdirs: personal, business, sales, life, tech, meta;
│                  each has README.md only — symlink targets for agents)
└── graph/
    ├── edges.jsonl     (572 lines, 572 edges)
    ├── communities.md  (4 communities: Life/Business/Tech/Meta)
    └── summaries.md    (GraphRAG text summaries per community)
```

Total entries across entity types: **546** (8+4+271+1+257+5+0+0+0).

## B. Frontmatter schema (per template type)

All 9 templates use YAML frontmatter. Common required fields across ALL types:
`title`, `type`, `niche`, `sources: []`, `related: []`, `tags: [...]`, `created`, `updated`, `confidence`, `pipeline`.

Type-specific fields:
- **source**: `source_kind` (article | book | podcast | video | meeting | voice-memo | transcript | web | paper), `url`, `author`, `captured`, `raw_file`
- **concept**: no extras
- **entity**: `entity_kind` (person | company | product | team | event | place)
- **claim**: `stance` (asserted | supported | contested | refuted)
- **idea**: `status` (raw | evaluated | planned | in-progress | shipped | dropped)
- **experiment**: `status` (planned | running | done | aborted), `started`, `ended`
- **summary**: `scope` (daily | weekly | topic | cluster), `covers: []`
- **foundation**: no extras; defaults `confidence: high`
- **topic**: no extras

Concrete example from `wiki/concepts/collaborative-project-versioning.md` (real entry — also shows observed `topics: [...]` field not in template, added by Notion-sweep):

```yaml
title: "Collaborative project versioning — бизнес-проекты как git-репозиторий"
type: concept
niche: business
sources:
  - raw/notion-ideas/2026-04-16-github-for-business-projects.md
related:
  - ideas/github-for-business-projects.md
  - claims/business-projects-like-code.md
tags: [#type/concept, #topic/collaboration, #topic/platform]
topics: [system-design]
created: 2026-04-16
updated: 2026-04-16
confidence: medium
pipeline: ingested
```

`niche` enum: `personal | business | sales | life | tech | meta | global`.
`pipeline` enum (per overview.md): `raw → ingested → ready`.
`confidence` enum: `low | medium | high`.

## C. Edge model (edges.jsonl)

Shape (inferred from 572 lines, all well-formed JSON):

```json
{"from": "<type>/<slug>.md", "to": "<type>/<slug>.md",
 "type": "<edge-type>", "created": "YYYY-MM-DD", "confidence": "<low|medium|high>"}
```

Paths are relative to `wiki/` root; both `from` and `to` carry the type-subdir prefix.

Observed edge types (FULL enumeration across all 572 edges — not just first 50):

| Type | Count |
|------|-------|
| `derived_from` | 219 |
| `part_of` | 233 |
| `supports` | 84 |
| `extends` | 35 |
| `contradicts` | 1 |
| **Total** | **572** |

Notable gap: the overview and `/build-graph` skill define **9 edge types** (`extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, addresses_gap, derived_from`), but only **4 of the 9** appear in data, plus `part_of` (which is NOT in the documented 9 — it was added ad hoc for hub→children during the 2026-04-16 system-design hub creation). So the actual schema has drifted from the documented schema.

Writers: `/ingest` (Step 6 of its spec: append one JSON-per-line), `/build-graph` (Step 3: back-fills missing edges via section-name heuristics), `/ask` (Step 6 when saving to comparisons/). Append-only — `/build-graph` spec: "Никогда не удаляй вручную. Для удаления edge — перегенерируй с нуля."

## D. Skill protocol summary

| Skill | Trigger | Reads | Writes |
|-------|---------|-------|--------|
| **/ingest** | `/ingest <path|url>` | raw file (or WebFetch URL), `_templates/`, existing wiki pages for merge | `wiki/{type}/{slug}.md` (new or merged), `wiki/sources/YYYY-MM-DD-slug.md`, `wiki/graph/edges.jsonl` (append), `wiki/index.md` (add line), `wiki/log.md` (prepend), `wiki/niches/{niche}/README.md`, raw file frontmatter (`pipeline: ingested`, `wiki_page:`) |
| **/ask** | `/ask <вопрос>` | `wiki/index.md` (full), then grep + selective page reads (5–15 pages), optionally `wiki/graph/summaries.md` | Optionally `wiki/comparisons/YYYY-MM-DD-slug.md`, `edges.jsonl`, `index.md`, `log.md` — only if answer is high-value (new cross-page synthesis) |
| **/lint** | `/lint [niche]` | Glob `wiki/**/*.md`, `edges.jsonl`, `index.md` | `wiki/_lint-report-YYYY-MM-DD.md`, `log.md` prepend. Read-only for all other files (explicit rule: "Не удалять / не править другие файлы"). |
| **/compile** | `/compile {topic}` | raw/ files by tags, `knowledge-base/{cluster}/_moc.md` | `knowledge-base/{cluster}/{topic}.md`, updates raw frontmatter `extracted_to:`, updates `_moc.md`. **Targets `knowledge-base/` (legacy), NOT `wiki/` — this is the old pipeline.** |
| **/consolidate** | `/consolidate [type|niche]` | pairwise across `wiki/{type}/*.md` | Merged `wiki/{type}/A.md`, archive `wiki/_archive/YYYY-MM-DD-B.md`, updated `edges.jsonl`, `index.md`, `log.md`. Never acts without `y` confirmation. |
| **/build-graph** | `/build-graph [--edges-only]` | Glob `wiki/**/*.md`, `edges.jsonl` | Appends to `edges.jsonl`, rewrites `wiki/graph/communities.md` and `wiki/graph/summaries.md`, prepends to `log.md` |
| **/search-kb** | `/search-kb {query}` | `knowledge-base/_index.md` → cluster `_moc.md` → `grep -rl tags` → `grep -rl` full-text in `knowledge-base/ raw/` | Nothing — read-only. **Also targets legacy `knowledge-base/`, not `wiki/`.** |
| **/sweep-notion-bank** | `/sweep-notion-bank [--dry-run|--batch-size|--parallel]` | Notion MCP, `wiki/sources/` for dedup by `notion_id` | `raw/notion-ideas-sweep-*.jsonl`, `wiki/ideas/`, `wiki/sources/`, `index.md`, `log.md`. Chains `/build-graph` + `/lint` at end. |

## E. Current retrieval mechanism (Q1)

**No embeddings. No vector DB. No dedicated RAG infra.** Retrieval is pure filesystem + grep.

`/ask` algorithm (direct quote):
> 1. Прочитать `wiki/index.md`. Это главный навигатор. Не гадай — читай целиком.
> 2. Отобрать 5-15 релевантных страниц: сначала по заголовку и one-line summary из index.md. При необходимости — grep по ключевым словам вопроса в `wiki/**/*.md`. Смотри niche… Если есть community summaries (`wiki/graph/summaries.md`) — используй их для быстрого контекста.
> 3. Прочитать отобранные страницы. Полностью. Следи за wikilinks — при необходимости иди глубже (но не более 2 уровней).

So the retrieval stack is: **index.md as master TOC → grep fallback → niche filter → graph summaries as GraphRAG context → wikilink traversal (max depth 2)**.

`/search-kb` is even simpler and targets the **legacy** `knowledge-base/` tree (not `wiki/`): MOC → `grep -rl "tags:.*{keyword}"` → `grep -rl "{query}"` full-text. Strict order, no semantic layer.

## F. Current cross-reference format (Q3)

Four parallel channels, all used:

1. **Frontmatter `related: [...]`** — list of relative paths (e.g. `ideas/github-for-business-projects.md`). Human-maintained via /ingest.
2. **Frontmatter `sources: [...]`** — raw file path (e.g. `raw/notion-ideas/2026-04-16-github-for-business-projects.md`) — provenance, not navigation.
3. **Inline Obsidian-style wikilinks** in body: `[[concepts/curated-community-access]]` or `[[sources/2026-04-16-slug]]` (often without `.md`). Used in section-based conventions like "## Связи" / "## Расширяет" / "## Поддерживает".
4. **Typed edges** in `wiki/graph/edges.jsonl` — one JSON per line, machine-readable.

Example from `wiki/concepts/collaborative-project-versioning.md`:

```
## Связи
- Расширяет: [[claims/business-projects-like-code]]
- Поддерживает: [[ideas/github-for-business-projects]]
- Связан с: [[concepts/curated-community-access]]
```

`/build-graph` step 3 parses section headers ("## Расширяет" → `extends`, "## Противоречит" → `contradicts`, etc.) to derive edges from the wikilinks inside those sections — i.e. wikilinks + section-name-as-edge-type is the canonical authoring pattern; edges.jsonl is the downstream index.

## G. Current staleness handling (Q5)

Available signals in frontmatter:
- `pipeline: raw | ingested | ready` (only 2 states in active use: `raw`, `ingested`; `ready` reserved, `comparisons/` template sets `ready`).
- `updated: YYYY-MM-DD` (date only).
- `status:` on ideas (`raw | evaluated | planned | in-progress | shipped | dropped`) and experiments.
- `confidence: low | medium | high`.
- `stance:` on claims (`asserted | supported | contested | refuted`).

`/lint` checks (7 total, quoted from skill):
1. Orphan pages — no inbound wikilinks and no edges.jsonl entries.
2. **Stale claims** — only check that touches staleness: `wiki/claims/*.md` where `confidence: low` AND `updated:` older than 60 days.
3. Broken wikilinks.
4. Missing required frontmatter.
5. Contradictions — for every edge `contradicts`, verify both pages exist and mention each other.
6. Missing cross-refs — page A mentioned in 3+ other pages but absent from their `related:`.
7. Index drift — files in wiki/ not in `index.md` and vice versa.

**Conclusion:** staleness handling is thin — only claims get a 60-day `confidence: low` check. No `last_reviewed:` field. No decay. No auto-deprecation. No `supersedes` edge is used (0 in data).

## H. Current skill-addition process (Q6)

**Fully ad-hoc.** No golden-set, no eval harness, no activation gate found. Skills are plain markdown files in `.claude/skills/` with two formats observed:

1. **New-style** (has YAML frontmatter with `name`, `description`, `allowed-tools`) — ingest, ask, lint, consolidate, build-graph, sweep-notion-bank.
2. **Old-style** (no frontmatter, just `# Skill: /name`) — compile, search-kb.

The ingest skill itself carries a comment acknowledging the drift: `⚠️ ВНИМАНИЕ: есть старая версия ingest.md (raw → ingested KB). Этот файл — новая версия под wiki-архитектуру… После ручного ревью Русланом — старую удалить, эту переименовать.`

No formalized lifecycle (propose → eval → activate). No Learning/SPL pipeline. CLAUDE.md lists agent memory layers (`agents/{id}/strategies.md` for "System Prompt Learning накопления"), but there is no skill that consumes or writes to `strategies.md`.

## I. Write-access patterns (Q2)

Writers to `wiki/`:

| File / dir | Writers |
|-----------|---------|
| `wiki/{type}/*.md` | /ingest (new + merge), /consolidate (merge target), /sweep-notion-bank (via /ingest) |
| `wiki/sources/` | /ingest, /sweep-notion-bank |
| `wiki/comparisons/` | /ask only |
| `wiki/index.md` | /ingest, /ask, /consolidate, /sweep-notion-bank (manual append in designated section) |
| `wiki/log.md` | ALL mutating skills (prepend with `## [date] <action>`) |
| `wiki/graph/edges.jsonl` | /ingest, /ask, /build-graph (all append-only) |
| `wiki/graph/communities.md`, `summaries.md` | /build-graph (overwrite) |
| `wiki/_lint-report-*.md` | /lint |
| `wiki/_archive/` | /consolidate |

**No write-serialization / lockfiles.** Append-only for edges.jsonl and log.md is a convention, not enforced. The `/ingest` rule "Не перезаписывать чужие правки. При конфликте — создать `.new` версию" is advisory.

No per-section ownership. No agent-level write routing. Any agent/skill can write to any wiki subdir.

Tools/scripts outside .claude that write to wiki: `tools/_notion_alpha_2_classify_ingest.py` (idempotent bulk import), `tools/stage1_aggregate.py`. One markdown reference in `tools/acquire/MANUAL-ACQUISITION-LIST.md`.

## J. Task-scoping in v2 (Q4)

**No task-scoping mechanism exists.** What exists:

- **Niches (6)** — domain slices (`personal`, `business`, `sales`, `life`, `tech`, `meta`), exposed to agents via symlinks: `agents/<id>/niche/{name} → wiki/niches/{name}/`. Per CLAUDE.md: "у агентов НЕТ изолированной KB. Общая wiki/, каждый агент видит свой срез через niche/ symlinks." Agents with niche symlinks confirmed: sales-lead, sales-researcher, crazy-agent, personal-assistant, life-coach, inbox-processor.
- **`topics:` frontmatter** — ad-hoc tag added during the system-design sweep (65 pages tagged `topics: [system-design]`); `topics/system-design-hub.md` is a navigation hub.
- **Tags** — `#type/...`, `#topic/...`, `#status/...` — used but not a scoping boundary.

No task-ID concept, no ephemeral scratchpads tied to a task, no task-level context frames. Per-agent working memory lives in `agents/{id}/scratchpad.md` and mailboxes — not in wiki/.

## K. Migration / coexistence analysis (Q9)

**Scale of existing wiki/ that would have to move or coexist:**

- **546 entries** across typed subdirs.
- **572 edges** in `edges.jsonl`.
- `index.md` = 186 lines / 1,607 words; `log.md` = 112 lines / 860 words (append-only history — cannot be regenerated).
- 4 community clusters + GraphRAG summaries.
- 6 niche READMEs, each symlinked from 6+ agents. **Agent symlinks pointing into `wiki/niches/*/` will break on move** unless relinked.

**Hardcoded path count (`wiki/` literal in skill prose):**

| Skill | Count of `wiki/` refs | Breaks on move? |
|-------|----------------------|-----------------|
| consolidate.md | 10 | yes |
| ingest.md | 9 | yes |
| ask.md | 9 | yes |
| lint.md | 9 | yes |
| build-graph.md | 7 | yes |
| sweep-notion-bank.md | 7 | yes |
| search-kb.md | 0 | no (targets `knowledge-base/`) |
| compile.md | 0 | no (targets `knowledge-base/`) |

**6 of 8 skills hardcode `wiki/`.** The two that don't reference `wiki/` instead reference the *legacy* `knowledge-base/` tree and would break orthogonally.

Beyond skills, `wiki/` is referenced by: `tools/_notion_alpha_2_classify_ingest.py`, `tools/stage1_aggregate.py`, `tools/acquire/MANUAL-ACQUISITION-LIST.md`, and numerous `agents/*/scratchpad.md` + `agents/*/niche/README.md` files (10+). Also CLAUDE.md itself documents `wiki/` as the canonical root.

Additionally: `edges.jsonl` stores `<type>/<slug>.md` paths **without** a `wiki/` prefix — so the edges file itself is location-agnostic and would survive a move if skills and path joins are updated. Same for wikilinks in bodies (`[[concepts/foo]]`).

**What would BREAK if `wiki/` is moved to `swarm/wiki/`:**
1. All 6 skills that hardcode `wiki/` paths — every step references `wiki/` directly (no variable).
2. Agent niche symlinks (6 niches × N agents = ~10+ symlinks) need retargeting.
3. `index.md` path conventions (e.g. `[[concepts/...]]` are relative to wiki root — fine; but `[raw](../../raw/...)` back-links from sources encode depth — would break if depth changes).
4. 2 tools under `/tools/`.
5. CLAUDE.md "Wiki Architecture v2" section and its examples.
6. Lint reports are dated + cumulative — fine to leave (historical).

**What can be shared cleanly between v2 `wiki/` and v3 `swarm/wiki/`:**
- **Templates** — all 9 `_templates/` are path-agnostic content; reusable as-is or copied.
- **Edge model** — `{from, to, type, created, confidence}` is type-subdir-relative; the schema itself is portable. Edge-type enum (9 declared, 4+1 observed) is reusable.
- **Skill logic** — if skills are parameterized by `$WIKI_ROOT` or a config file, all 6 can point at either tree. Current skills are markdown specs (not code), so parameterization = editing prose.
- **Frontmatter schema** — path-agnostic; identical across trees is desirable.
- **Community detection + GraphRAG flow** in `/build-graph` — logic is generic.
- **niche concept** — could extend to v3 or be replaced by task-scoping.

**Rough cost-of-change estimate (lines edited, not files):**
- **Migrate (move `wiki/` → `swarm/wiki/`):** ~51 skill-prose edits (sum of hardcoded `wiki/` counts, ignoring search-kb/compile), ~10 symlink retargets, ~3 tool edits, ~20 lines in CLAUDE.md, wiki/overview.md rewrite. Total: **~85–100 targeted line edits + 1 directory move + symlink fix-ups.** Data itself (546 files + edges.jsonl) moves byte-identical.
- **Coexist (add `swarm/wiki/` alongside):** 0 edits to existing skills (they keep writing to `wiki/`), but every new v3 skill must be `swarm/wiki/`-aware; plus a decision layer on *which* tree to write for each concept. Risk: drift between trees, duplicate entries, unclear authority. Net: fewer immediate edits, more long-term divergence risk.
- **Parameterize (single skill set, `$WIKI_ROOT` variable):** ~51 skill-prose edits to replace literal `wiki/` with variable reference + a config file. Matches migrate effort, but gives optional dual-tree. Feasible because skills are markdown prose consumed by Claude, not compiled code.

Empty directories with 0 entries (`experiments/`, `summaries/`, `foundations/`, `comparisons/`) are cost-free to migrate.

## L. Unknowns / questions raised

1. Schema drift: `part_of` edge type (233 edges, 40% of data) is undocumented in overview/build-graph; was it added ad-hoc for the system-design hub and should become formal v9-type #10?
2. Two skill formats coexist (new frontmatter-style and old plain-header). Is the old `/compile` + `/search-kb` pair being retired? Ingest.md carries a note implying an older sibling needs removal.
3. `comparisons/` is empty — /ask save-loop has never fired. Is the heuristic too strict, or has /ask not been invoked on valuable-enough questions?
4. `foundations/`, `experiments/`, `summaries/` all 0 — indicates ingest almost always lands as `idea/source/concept`; the richer entity types are unused.
5. Index drift already at 30 in last lint report — /ingest index-update step seems to be skipped in bulk imports (Notion sweep).
6. No `last_reviewed:` or decay field — staleness story is claim-only.
