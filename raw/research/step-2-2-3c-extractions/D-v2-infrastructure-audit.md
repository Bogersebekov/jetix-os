---
sub_agent: D
title: v2 Infrastructure Audit for Wiki v3 Стадия C
date: 2026-04-23
sources_read:
  - wiki/_templates/{source,concept,entity,claim,idea,topic,experiment,summary,foundation}.md
  - wiki/graph/edges.jsonl, communities.md, summaries.md
  - wiki/{overview,index,log}.md
  - .claude/skills/{ingest,ask,lint,compile,consolidate,build-graph,search-kb,sweep-notion-bank}.md
  - CLAUDE.md
  - .claude/rules/global.md
word_count_target: ≤2500
purpose: Feed Deliverable 4 (templates), Deliverable 3 (edge enum grounding), Deliverable 8 (skill diffs)
---

# v2 Infrastructure Audit — Wiki v3 Стадия C

## Section 1 — Per-template audit (9 templates)

**Common core frontmatter (all 9 templates):** `title` (string, req), `type` (literal, req), `niche` (enum: personal/business/sales/life/tech/meta/global, req), `sources: []` (list, req), `related: []` (list, req), `tags: [#type/X, #status/active]` (list, req), `created` (date, req), `updated` (date, req), `confidence` (enum low/medium/high, req), `pipeline` (enum raw/ingested/ready, req). Below — only deltas from this core.

### 1.1 source.md
- Path: `wiki/_templates/source.md`, lines: 42
- Extra fields: `source_kind` (enum: article\|book\|podcast\|video\|meeting\|voice-memo\|transcript\|web\|paper, req), `url` (string, opt, ""), `author` (string, opt, ""), `captured` (date, req), `raw_file` (string, req).
- Body: TL;DR, Summary, Ключевые цитаты, Что извлекли, Мета, Сырое.
- Lint: convention sources[] non-empty + niche valid enum.
- Deadweight: Мета секция (язык/длина/качество) часто пустая.

### 1.2 concept.md
- Path: `wiki/_templates/concept.md`, lines: 35. No extra fields. Default confidence: medium.
- Body: Суть в одной строке, Определение, Ключевые свойства, Применимость, Связи, Источники.
- "Связи" sub-bullets pre-typed (Расширяет/Противоречит/Поддерживает) — maps to edge enum.

### 1.3 entity.md
- Path: `wiki/_templates/entity.md`, lines: 37. Extra: `entity_kind` (enum: person\|company\|product\|team\|event\|place, req).
- Body: Кто/что это, Контекст, Факты, Связи, История взаимодействий, Источники.

### 1.4 claim.md
- Path: `wiki/_templates/claim.md`, lines: 36. Extra: `stance` (enum: asserted\|supported\|contested\|refuted, req).
- Body: Точная формулировка, Контекст, Аргументы за, Аргументы против, Что опровергнуло бы это утверждение, Связи.
- Lint: has FALSIFIER section — important. `/lint` flags low-confidence stale claims (>60d).

### 1.5 idea.md
- Path: `wiki/_templates/idea.md`, lines: 39. Extra: `status` (enum: raw\|evaluated\|planned\|in-progress\|shipped\|dropped, req). Default confidence: low.
- Body: Одна строка, Обоснование, Предполагаемый эффект, Что уже известно/проверено, Следующий шаг, Связи, Источники.

### 1.6 topic.md
- Path: `wiki/_templates/topic.md`, lines: 33. No extra fields.
- Body: Зачем эта тема, Основные концепции, Ключевые сущности, Открытые вопросы, Смежные темы, Источники. Plays "hub" role (e.g. `system-design-hub.md`).

### 1.7 experiment.md
- Path: `wiki/_templates/experiment.md`, lines: 44. Extra: `status` (planned\|running\|done\|aborted), `started` (date), `ended` (nullable date).
- Body: Гипотеза, Дизайн (IV/DV/control/duration), Что делаем, Результат, Выводы, Связи, Источники.

### 1.8 summary.md
- Path: `wiki/_templates/summary.md`, lines: 36. Extra: `scope` (daily\|weekly\|topic\|cluster), `covers: []` (list).
- Body: TL;DR, Ключевые выводы, Что изменилось/появилось, Что ещё открыто, Входные страницы, Источники. Currently summaries live in `wiki/graph/summaries.md`, not as individual files.

### 1.9 foundation.md
- Path: `wiki/_templates/foundation.md`, lines: 34. Default confidence: high.
- Body: Принцип, Почему принимается, Что из этого следует, Когда сомневаться, Связи, Источники. Almost-axiomatic statements.

**Common pattern:** all bodies minimal (~5-7 sections), all use `[[wikilinks]]` for cross-refs, all terminate with "Источники".

## Section 2 — `edges.jsonl` audit

- **Total lines/edges:** 572
- **Live edge-type vocabulary (count desc):**
  - `part_of`: 233
  - `derived_from`: 219
  - `supports`: 84
  - `extends`: 35
  - `contradicts`: 1
- **Average metadata per edge:** 5 fields per record (`from`, `to`, `type`, `created`, `confidence`). No edges carry extra metadata.
- **Malformed/ad-hoc:** none observed in head/tail samples — all records are well-formed JSON with consistent shape.
- **Unsanctioned edge types:** `part_of` is heavily used (233) but is **NOT** in the v2 declared enum (overview.md line 42-43 lists 9 types: `extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, addresses_gap, derived_from`). `part_of` was introduced ad-hoc by the system-design-hub creation (log.md line 37) and has become dominant. This is a **drift-from-spec** finding.
- **Mapping to v3 12-type planned enum:**
  - `derived_from` (219), `supports` (84), `extends` (35), `contradicts` (1) — likely transplant as-is.
  - `part_of` (233) — needs explicit acceptance into v3 enum (it's the dominant edge — dropping breaks the topic-hub pattern). Likely renames to `part_of` or `belongs_to` in v3.
  - `inspired_by`, `tested_by`, `invalidates`, `supersedes`, `addresses_gap` — declared but **zero usage** in real data. v3 should decide: keep as planned vocabulary, or drop unused.
  - 7 of v3's hypothetical 12 types are net-new and have no v2 baseline — clean greenfield.

## Section 3 — Wiki conventions worth preserving

### overview.md (64 lines)
Structure: TL;DR → Как устроено (tree diagram) → Операции (5 skills) → Принципы (5) → Niches (table) → Pipeline статусы → Obsidian.
**For v3 swarm/wiki/overview.md:** replicate the tree-diagram format and "Принципы" numbered list. The Obsidian compatibility note is an underrated v2 asset (flat dirs + wikilinks = vault-compatible).

### index.md (186 lines)
**TOC mechanism:** Topical sections by entity type (`## Concepts`, `## Entities`, `## Sources`, …), alphabetical within section. Format: `- [Title](path) — one-line summary [niche] [sources: N]`. Auto-updated by `/ingest` (skill step 7). Header frontmatter: `type: index`, `updated: YYYY-MM-DD`. No hash/checksum mechanism — drift detected by `/lint` check #7.

### log.md (112 lines)
**Append-only chronology, NEW ENTRIES ON TOP** (rule global.md §"Логи"). Pattern: `## [YYYY-MM-DD] <skill-name> | <action> | <key-metrics>` followed by 2-5 lines of detail. No date-grouped headers — one entry per operation. Rotation rule: >30 entries → archive (CLAUDE.md §"Правила" #7).

## Section 4 — Skill-by-skill audit

### 4.1 /ingest (135 lines)
- Path: `.claude/skills/ingest.md`
- Purpose: Raw source → wiki/ pages + index + log + edges.
- Hard-coded `wiki/` references (line numbers): 3, 15, 62, 65, 71, 78, 90, 100, 111.
- Read surfaces: `raw/**`, `wiki/_templates/{type}.md`, `wiki/graph/edges.jsonl` (existence check), existing `wiki/{type}/{slug}.md` for merge.
- Write surfaces: `raw/web/YYYY-MM-DD-slug.md`, `wiki/{type}/{slug}.md`, `wiki/sources/...`, `wiki/graph/edges.jsonl` (append), `wiki/index.md`, `wiki/log.md`, `wiki/niches/{niche}/README.md`.
- Lines that change for `$WIKI_ROOT` parameterization: **62, 65, 71, 78, 90, 100, 111** (7 substantive replacements; 3, 15 are description-only prose).

### 4.2 /ask (116 lines)
- Path: `.claude/skills/ask.md`
- Purpose: Q&A over wiki with synthesis + optional comparison-card filing.
- Hard-coded `wiki/` references: 3, 11, 20, 27, 28, 29, 60, 71, 100.
- Read surfaces: `wiki/index.md`, `wiki/**/*.md`, `wiki/niches/sales/`, `wiki/graph/summaries.md`.
- Write surfaces: `wiki/comparisons/YYYY-MM-DD-question-slug.md`, `wiki/graph/edges.jsonl` (append), `wiki/index.md`, `wiki/log.md`.
- Lines that change for `$WIKI_ROOT`: **20, 27, 28, 29, 60, 71, 100** (7 lines; 3 and 11 are prose).

### 4.3 /lint (103 lines)
- Path: `.claude/skills/lint.md`
- Purpose: 7-check health report (orphans, stale claims, broken links, missing FM, contradictions, missing cross-refs, index drift).
- Hard-coded `wiki/` references: 3, 11, 21, 30, 38, 55, 60, 92, 102.
- Read surfaces: `wiki/**/*.md`, `wiki/graph/edges.jsonl`, `wiki/index.md`.
- Write surfaces: `wiki/_lint-report-YYYY-MM-DD.md`, `wiki/log.md`.
- Lines that change: **21, 30, 38, 55, 60, 92, 102** (7 substantive; 3, 11 prose).

### 4.4 /consolidate (96 lines)
- Path: `.claude/skills/consolidate.md`
- Purpose: Detect & merge duplicates with confirm-loop, archive losers.
- Hard-coded `wiki/` references: 3, 11, 36, 37, 68, 70, 73, 76, 80, 81.
- Read surfaces: `wiki/{type}/*.md` (all entity types), `wiki/graph/edges.jsonl`, `wiki/index.md`.
- Write surfaces: surviving page (edited), `wiki/_archive/YYYY-MM-DD-B.md`, `wiki/graph/edges.jsonl` (rewritten), `wiki/index.md`, `wiki/log.md`.
- Lines that change: **36, 37, 68, 70, 73, 76, 80, 81** (8 substantive; 3, 11 prose).

### 4.5 /build-graph (97 lines)
- Path: `.claude/skills/build-graph.md`
- Purpose: Walk wiki, append missing edges, recompute communities + summaries.
- Hard-coded `wiki/` references: 3, 11, 22, 33, 62, 73, 86.
- Read surfaces: `wiki/**/*.md` (excluding index/log/overview/templates/niches READMEs/graph/_archive/_lint-report), `wiki/graph/edges.jsonl`.
- Write surfaces: `wiki/graph/edges.jsonl` (append), `wiki/graph/communities.md` (rewrite), `wiki/graph/summaries.md` (rewrite), `wiki/log.md`.
- Lines that change: **22, 33, 62, 73, 86** (5 substantive; 3, 11 prose).

### 4.6 /compile (50 lines)
- Path: `.claude/skills/compile.md`
- Purpose: Synthesize multiple ingested raw-files into one KB article (LEGACY — references `knowledge-base/`, NOT `wiki/`).
- Hard-coded `wiki/` references: **NONE** (uses `knowledge-base/` and `raw/`).
- Read surfaces: `raw/` (frontmatter tags), `knowledge-base/{cluster}/_moc.md`.
- Write surfaces: `knowledge-base/{cluster}/{topic}.md`, raw frontmatter (`extracted_to:`), `knowledge-base/{cluster}/_moc.md`.
- Status: legacy/pre-v2. **No parameterization needed for v3 wiki path** — but the skill itself is orthogonal to the wiki/ pipeline and may need v3-specific decision (deprecate? rewrite for $WIKI_ROOT?).

### 4.7 /search-kb (38 lines)
- Path: `.claude/skills/search-kb.md`
- Purpose: KB lookup (MOC → tags → full-text).
- Hard-coded `wiki/` references: **NONE** (references `knowledge-base/` only).
- Read surfaces: `knowledge-base/_index.md`, `knowledge-base/{cluster}/_moc.md`, `knowledge-base/`, `raw/`.
- Write surfaces: none.
- **Out-of-scope per master synthesis §5.10 — confirmed exclusion.** Legacy skill targeting old KB; doesn't touch wiki/. No v3 parameterization needed.

### 4.8 /sweep-notion-bank (110 lines)
- Path: `.claude/skills/sweep-notion-bank.md`
- Purpose: Mass-import Notion Bank of Ideas into wiki/ via parallel sub-agents.
- Hard-coded `wiki/` references: 5, 16, 29, 51, 72, 73, 77.
- Read surfaces: Notion MCP, `raw/notion-ideas-sweep-2026-04-16.jsonl`, `wiki/sources/` (dedup grep).
- Write surfaces: `raw/notion-ideas/`, `wiki/ideas/`, `wiki/sources/`, `wiki/index.md`, `wiki/log.md`.
- **Out-of-scope per master synthesis §5.10 — confirmed exclusion.** This is a one-shot Notion-import script bound to specific date 2026-04-16 + specific Notion DB ID (bf0e9a11-…). Re-running for v3 swarm would require full rewrite, not parameterization. Lines that *would* change if forced: 29, 51, 72, 73, 77 (5 lines).

**Total skill edit budget if parameterizing 5 in-scope skills (ingest, ask, lint, consolidate, build-graph):** 7+7+7+8+5 = **34 substantive line replacements** + ~5 prose-description tweaks = ~40 lines. (Master synthesis estimate of ~85 lines includes likely added `$WIKI_ROOT` declaration blocks/header comments per skill, ~9 lines × 5 skills = 45 lines, totalling ~85.)

## Section 5 — CLAUDE.md "Wiki Architecture v2" section

Located at lines **61-90**. Quoted verbatim (key clauses):
- Line 63: `**Главный KB:** wiki/ (не knowledge-base/ — тот в миграции, см. MIGRATION.md).`
- Lines 65-72: Структура — `wiki/index.md`, `wiki/log.md`, 9 entity types listed, `comparisons/`, `niches/` (6 срезов), `graph/edges.jsonl` (typed, 9 types), `_templates/`.
- Lines 74-79: 5 skills — `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`.
- Lines 81-86: Per-agent memory 5 layers — system.md, strategies.md, scratchpad.md, niche/ (symlinks), comms mailbox.
- Line 88: **Принцип: у агентов НЕТ изолированной KB. Общая wiki/, каждый агент видит свой срез через niche/ symlinks.**
- Line 90: Legacy `knowledge-base/` reference + MIGRATION.md pointer.

**Carry into v3 docs:** the "structure tree", "5 skills", "5-layer per-agent memory", and the niche-symlinks principle are core architectural choices that must survive v3. The **9-entity-types** list and **9-edge-types** list will both change in v3 (per master synthesis: 12 edges, possibly different entities). **Replace:** the literal `wiki/` path becomes `swarm/wiki/` (or `$WIKI_ROOT`). The "5 skills" list grows (or stays — depends on Стадия C decisions). The Karpathy + OmegaWiki framing should stay.

## Section 6 — `.claude/rules/global.md` audit

Inherited as-is for v3:
- **Файлы (lines 9-11):** YAML frontmatter mandatory (except README), check-before-create, kebab-case + YYYY-MM-DD. Universal.
- **Логи (lines 14-16):** Append-only, new-on-top, rotate >30 entries to archive/. Already governs `wiki/log.md`; will govern `swarm/wiki/log.md` identically.
- **Безопасность (lines 30-32):** ssh/etc/.env/private/ untouchable. Universal.
- **Язык/стиль (lines 35-37):** Russian primary, direct, ask-don't-assume. Universal.
- **Git (lines 25-27):** Format `[area] description`; v3 may add new area tags (e.g. `[swarm]`, `[wiki-v3]`).

Need v3-specific equivalent:
- **Knowledge Base (lines 19-22):** Currently mandates `_moc.md` first → tags grep → full-text grep. This search order is **legacy** (targets `knowledge-base/`, not `wiki/`). v3 needs an updated KB-search rule: `index.md` → community summaries → niche → grep — matching the v2 `/ask` behaviour (skill ask.md lines 20-27).

## Section 7 — Top transplant-vs-modify recommendations

| v2 asset | recommendation | rationale |
|---|---|---|
| 9 entity templates (source/concept/entity/claim/idea/topic/experiment/summary/foundation) | **transplant as-is** with `niche` enum updated for v3 | Frontmatter shape is solid; type-specific discriminators are well-thought-out. Bodies are minimal and language-localized. |
| `pipeline` field (raw/ingested/ready) | **modify** | v3 will likely have different lifecycle stages; CLAUDE.md mentions `raw→ingested→compiled→linted→ready` (5 states) but templates only use 2-3. Reconcile. |
| `confidence` field (low/medium/high) | **transplant as-is** | Used by `/lint` stale-claim check; portable. |
| `niche` enum (7 values: personal/business/sales/life/tech/meta/global) | **unsure-flag-for-orchestrator** | v3 swarm topology may collapse or expand niches. Architectural decision needed. |
| Edge-type vocabulary (declared 9, actual 5 used) | **modify** | Drop 5 unused (`inspired_by/tested_by/invalidates/supersedes/addresses_gap`); promote `part_of` to first-class; expand to 12 per v3 spec. Migration script needed for 572 existing edges (mostly straightforward — only `contradicts` is rare). |
| `edges.jsonl` schema (5 fields: from/to/type/created/confidence) | **transplant as-is** | Clean shape, well-honoured across 572 records. |
| `wiki/index.md` topical-section format | **transplant as-is** | Auto-generated by `/ingest`, format is clean. May add v3 sections per new entity types. |
| `wiki/log.md` append-on-top + rotation rule | **transplant as-is** | Universally applicable. |
| `wiki/overview.md` structure (tree + principles + niches) | **transplant as-is** with path/enum updates | Strong reference doc; v3 needs equivalent at `swarm/wiki/overview.md`. |
| `wiki/graph/communities.md` & `summaries.md` | **transplant as-is** | Format works for GraphRAG-style context injection in `/ask`. |
| `comparisons/` filing loop in `/ask` | **transplant as-is** | Bonus pattern that captures synthesis value. |
| `niches/` symlink mechanism | **transplant as-is** | Core to "shared KB, per-agent slice" principle. |
| `/ingest` skill | **modify** (parameterize `$WIKI_ROOT`) | 7 lines change. |
| `/ask` skill | **modify** (parameterize `$WIKI_ROOT`) | 7 lines change. |
| `/lint` skill | **modify** (parameterize `$WIKI_ROOT` + add new v3 checks?) | 7 lines minimum. |
| `/consolidate` skill | **modify** (parameterize `$WIKI_ROOT`) | 8 lines change. |
| `/build-graph` skill | **modify** (parameterize `$WIKI_ROOT` + update edge-type detection regex for v3 12 types) | 5 path lines + section-4 logic block. |
| `/compile` skill | **drop** (or rewrite) | Targets legacy `knowledge-base/`; supplanted by `/ingest` + `/ask` in v2. |
| `/search-kb` skill | **drop** (per master synthesis §5.10 exclusion) | Legacy; supplanted by `/ask` index-first lookup. |
| `/sweep-notion-bank` skill | **drop** (per master synthesis §5.10 exclusion) | One-shot Notion-import bound to 2026-04-16 sweep. |
| CLAUDE.md "Wiki Architecture v2" section | **modify** | Replace path/enum specifics; keep structural/principle parts. |
| `.claude/rules/global.md` Files/Logs/Security/Style sections | **transplant as-is** | Universal. |
| `.claude/rules/global.md` Knowledge Base section | **modify** | Currently MOC-first (legacy); rewrite for v3 index→summaries→niche→grep. |

---

**Audit complete.** No changes proposed beyond the recommendation table — decisions belong to Стадия C orchestrator.
