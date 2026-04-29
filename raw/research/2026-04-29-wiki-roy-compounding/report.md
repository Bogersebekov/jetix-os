---
title: "Wiki / ROY swarm / Compounding Engineering — фактическое состояние repo на 2026-04-29"
date: 2026-04-29
type: research-brief
audience: ruslan (Tseren outreach video, шаг 4 §1.5)
branch: claude/jolly-margulis-915d34
purpose: точные формулировки для раздела «Как я делал систему» — без приближений
---

# §1 — «70 книжек» / Knowledge Ingestion

## §1.1 Where + what (где лежит, сколько реально)

**Реальное число — НЕ 70, а 402** (после двух cleanup-проходов).

- Канонический каталог: `/home/ruslan/jetix-os/raw/books-md/INDEX.md` — 402 книг,
  сгенерирован 2026-04-27 06:56 (cleanup-проходы 22.04).
- На диске сейчас 403 `.md` файла под `raw/books-md/` (402 книги + INDEX +
  сервисные `_DELETED-LOG.md` / `_DELETED-LOG-DEEP.md` / `_FILTER-BLOCKED.md`;
  плюс `processed/` с 2 raw_error stubs).
- Распределены по 14 подкатегориям-папкам:
  - `anthropic/` (2), `biology/` (4), `clean-code/` (5), `complexity/` (2),
    `cybernetics/` (4), `engineering-foundations/` (4), `event-sourcing/` (1),
    `investing/` (6), `meta/` (140 — Anthropic / Cognition / Karpathy блоги +
    MCP RFCs), `mgmt/` (96 — включая 87 chapter-файлов 37signals "Getting Real" +
    9 книг), `pdm/` (5), `philosophy/` (66), `philosophy-science/` (4),
    `pm/` (3), `sre/` (?), `systems/` (~50), `unix/` (?).

**До cleanup было гораздо больше:**
- `_DELETED-LOG.md` 2026-04-22: удалено 578 файлов (rule3 chapter-dupe 283;
  rule1 C-grade tiny 233; rule4 wget url-artifact 22; rule3 known-fragment 10;
  rule5 content-dup 7; rule4 numeric-stub 5; rule4 trash-filename 18). Самый
  большой урон — `cybernetics/` 158→4, `philosophy/` 263→69, `pm/` 27→3,
  `systems/` 79→50.
- `_DELETED-LOG-DEEP.md`: deep multi-agent substance review убил ещё 47 файлов
  из `meta/` (184→140) и `philosophy/` (69→66).

**Оригинальные PDF/EPUB источники в repo НЕ хранятся.** Папка
`/home/ruslan/jetix-os/raw/books/` содержит только `.gitkeep`. Конверсия делалась
из локального `inbox/` через rsync→Tailscale→сервер, исходники потом удалялись
(см. `tools/convert/README.md` "Шаг 5 — rm -rf inbox").

## §1.2 How processed (chunking / summaries / etc.)

**Не RAG. Не chunking. Не embeddings. Не vector store.**

Pipeline (`tools/convert/`):
1. **PDF / EPUB → Markdown через docling** (см. frontmatter каждой книги:
   `converted_via: docling`). Альтернатива OCR: `mistral_ocr.py` +
   `marker_reocr.sh` для книг где docling не справился (есть
   `reocr_per_book_prompt.md`, `reocr_task.md`).
2. **Frontmatter generation** (`tools/convert/gen_metadata.py`) — добавляет к
   каждому файлу YAML с полями: `acquired_date`, `converted_date`,
   `converted_via`, `expert` (= какому из ROY экспертов принадлежит:
   `engineering-expert` / `mgmt-expert` / `systems-expert` / `philosophy-expert`
   / `investor-expert` / `meta-expert`), `priority` (P1/P2),
   `quality_flags`, `quality_grade` (A/B/C), `slug`, `subcategory`, `tags`,
   `title`, `word_count`.
3. **Quality grading**:
   - **A** = clean (большинство файлов)
   - **B** = minor artifacts (page_pollution, OCR ghosts)
   - **C** = needs reprocess (stub-короткие <1000 слов, повреждённый OCR)
4. **Cleanup в 2 прохода** (`tools/convert/scan_cleanup.py` + `execute_cleanup.py`
   + `execute_deep_cleanup.py`) — деление на 12 batches под deep multi-agent
   review (`tools/convert/deep-cleanup-batches/` + `deep-cleanup-verdicts/`).
5. **INDEX.md regeneration** — финальная таблица 14 подкатегорий × строки книг
   с grade / words / expert / priority / path.

**Никакого summarization / chunking / extraction в knowledge-graph не было.**
Файл — это весь текст книги в Markdown с минимальной разметкой (`<!-- page N -->`
маркеры, `# Chapter` заголовки). Целые тексты, до 813 869 слов на файл (Buffett
Shareholder Letters Collection).

## §1.3 Storage format

**Markdown с YAML frontmatter, plain-text, grep-friendly.**

Пример (`raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md`):

```yaml
---
acquired_date: '2026-04-22'
converted_date: '2026-04-27'
converted_via: docling
expert: systems-expert
priority: P1
quality_flags:
- page_pollution (117)
quality_grade: B
slug: wiener-cybernetics-2ed-1961
subcategory: cybernetics
tags: [cybernetics]
title: Wiener Cybernetics 2Ed 1961
word_count: 88579
---
<!-- page 1 -->
# Preface to the Second Edition
…
```

- **Никаких `.json` / `.jsonl` / `.parquet` / vector DB.**
- **Никаких embeddings.** Это явный constitutional-выбор: «Max-subscription
  discipline — zero `ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY` strings»
  (`decisions/ROY-AGENTS-BUILT-2026-04-23.md` §Max-subscription discipline).
  Vector DB / paid embeddings = paid API → запрещено в Phase A.
- Артефакты cleanup'а: `tools/convert/triage-report.json` (метаданные cleanup'а);
  `tools/convert/logs/20260427-*.log` (6 логов: convert, frontmatter, index,
  main, ocr, quality, triage).

## §1.4 Accessibility now (доступно ли агентам сейчас)

**Доступно — но НЕ через RAG / embeddings. Через прямое file-чтение по path с
inline-цитированием.**

Механизм:
1. **Library inventory** для каждого ROY-эксперта зашит в его `system.md`
   (frontmatter поле `expert:` в книгах = таргет-эксперт). Например все 5 книг в
   `clean-code/` → `engineering-expert`. Все 6 книг в `investing/` →
   `investor-expert`. И т.д.
2. **Доступ через `Read` tool по absolute path** + diapason строк:
   `Read raw/books-md/clean-code/ousterhout-philosophy-of-software-design-2ed-2021.md
   lines 355-600`.
3. **Inline citation pattern в drafts/canonical:**
   `[src:raw/books-md/clean-code/ousterhout-philosophy-of-software-design-2ed-2021.md
   lines 355-600]` — это обязательный provenance gate (`swarm/lib/shared-protocols.md`
   §2: «Provenance present. sources[] non-empty AND each path resolves to one of:
   sources/* / Tier-1 file / (incident_file, commit_hash) / (verbatim, line-range)»).
4. **Foundation Build cycle 12 (Wave B-2) — реальный пример использования:**
   14 consultant cards в `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/`
   каждая цитирует книги по line-range. `clean-code.md` цитирует Ousterhout
   lines 355-600, Hunt-Thomas lines 1180-1300, Martin lines 97-150, Brooks
   lines 27-129. Цитаты verbatim.
5. **`/ingest` skill для книг НЕ применялся.** `/ingest` (`.claude/skills/ingest.md`)
   рассчитан на 6 source types (YouTube / PDF / md / web / voice / stdin) с
   созданием entity-страниц в `swarm/wiki/`. Книги остались как raw archive — не
   были подняты в wiki/ как entities. Это явное design decision (см.
   `unix-philosophy.md` consultant card §"SPOT": «The 393-book library is
   `raw/books-md/` — not duplicated into `wiki/` entries until the `/ingest`
   skill transforms and attributes them»).

**Итог §1:** библиотека работает как **lookup-каталог**. Эксперт знает «свои»
книги по `expert:` frontmatter, читает нужные диапазоны при работе над
конкретной задачей, цитирует с line-range. Это retrieval-friendly, grep-friendly,
provenance-friendly паттерн — но это НЕ RAG и НЕ pre-computed knowledge graph.
Cycle-12 Wave-B продемонстрировал, что подход работает: 14 consultant cards
с STRONG/MODERATE library coverage написаны по этой схеме за один день.

## §1.5 Sources

- `/home/ruslan/jetix-os/raw/books-md/INDEX.md` — каталог 402 книг
- `/home/ruslan/jetix-os/raw/books-md/_DELETED-LOG.md` — cleanup-проход 1 (578 deleted)
- `/home/ruslan/jetix-os/raw/books-md/_DELETED-LOG-DEEP.md` — cleanup-проход 2 (47 deleted)
- `/home/ruslan/jetix-os/raw/books-md/_FILTER-BLOCKED.md`
- `/home/ruslan/jetix-os/tools/convert/README.md` — pipeline architecture
- `/home/ruslan/jetix-os/tools/convert/convert_all.py`, `gen_metadata.py`,
  `scan_cleanup.py`, `execute_cleanup.py`, `execute_deep_cleanup.py`,
  `mistral_ocr.py`, `marker_reocr.sh`
- `/home/ruslan/jetix-os/tools/convert/triage-report.json`
- `/home/ruslan/jetix-os/tools/convert/logs/20260427-*.log` (6 файлов)
- `/home/ruslan/jetix-os/tools/convert/deep-cleanup-batches/`,
  `deep-cleanup-verdicts/`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/library-inventory.md`
  — validated catalog по INDEX.md
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md`
  — пример consultant card с line-range citations
- `/home/ruslan/jetix-os/.claude/skills/ingest.md` — `/ingest` НЕ применялся к книгам
- Sample book: `/home/ruslan/jetix-os/raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md`

---

# §2 — ROY Swarm

## §2.1 Human-readable (30-second elevator pitch)

ROY — это **6-агентный swarm под Claude Code**, построенный 2026-04-23 (closure
запись `decisions/ROY-AGENTS-BUILT-2026-04-23.md`). Архитектура — 1 brigadier
(оркестратор без доменной экспертизы) + 5 domain experts (engineering / mgmt /
systems / philosophy / investor). Уникальная фишка — **matrix 5×4**: каждый
эксперт может быть вызван в одном из 4 role-modes (critic / optimizer /
integrator / scalability-architect), что даёт 20 «invocation cells».

**Как Ruslan ставит задачу → как доходит до выполнения:**
1. Ruslan пишет задачу в Claude Code (или brigadier подхватывает из
   `prompts/<step>-deep-prompt-<date>.md` / `decisions/AWAITING-APPROVAL-*.md`).
2. **Brigadier** (`.claude/agents/brigadier.md`, ~1005 строк) декомпозирует
   задачу через PMBOK/Cagan/Grove/Drucker линзы, выбирает task-shape (design /
   review / optimize / scale-project / combined), мапит на cells через
   `swarm/lib/routing-table.yaml`.
3. **Wave-A dispatch** — параллельный `Task()` invocation по 4-7 экспертов
   одновременно с указанием role-mode и full context. Каждый эксперт пишет
   draft в `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md`.
4. **§5.5.5 Provenance gate** (см. `swarm/lib/shared-protocols.md` §2) —
   brigadier валидирует каждый draft: sources[] non-empty, inline `[src:...]`
   citations, edge consistency, tier coherence.
5. **Integration** — brigadier либо принимает draft, либо назначает critic
   role-mode другому эксперту, либо escalates к Ruslan через
   `swarm/gates/AWAITING-APPROVAL-<id>-<date>.md` packet (Stage-Gated).
6. **Ruslan ack** в форме `decisions/RUSLAN-ACK-<id>.md` — финальная
   точка-печать. После этого brigadier promotes draft → canonical wiki, обновляет
   `swarm/wiki/index.md`, `log.md`, `graph/edges.jsonl`.
7. **Compound step** — каждый эксперт записывает DRR (Decision/Reasoning/Result/
   Review) в `agents/<id>/strategies.md`. Brigadier пишет cross-agent
   improvements в `swarm/wiki/meta/agent-improvements/`.

**Чем отличается от legacy 12-агентов** (manager / knowledge-synth / sales-lead
/ life-coach / meta-agent / personal-assistant / sales-researcher /
sales-outreach / crazy-agent / inbox-processor / system-admin / strategist):

- **Legacy 12** — продуктово-операционные агенты (Sonnet/Haiku), отдел-based
  (MGMT / OPS / Sales / Brain / Life / Meta), routing через `manager.md` hub-
  and-spoke. Продолжают работать как **operational layer** для воспроизводимых
  процессов (CRM, daily/evening pipeline, voice-pipeline, sales outreach).
- **ROY 6** — построен поверх как **architecture / strategy layer** для
  knowledge-work cycles (Foundation build, deep-dives, synthesis). Brigadier
  делегирует domain experts; никто не пересекается с операционкой.
- **Status:** оба активны и сосуществуют. Из 19 файлов в `.claude/agents/` —
  6 ROY (brigadier + 5 experts) + 14 legacy + 3 mini-swarm brigadiers
  (`project-brigadier.md`, `quick-money-brigadier.md`,
  `levenchuk-deep-dive-brigadier.md`) + 2 worker (`staging-writer.md`,
  `sweep-worker.md`). Phase-A правило явное: «14 legacy untouched» (`ROY-AGENTS-BUILT-2026-04-23.md`).

## §2.2 Architecture technical

**Где код / конфиги:**
- **Agent system prompts:** `.claude/agents/{brigadier,engineering-expert,
  mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md`. Размеры:
  brigadier 1005 строк, engineering 989, mgmt 1530, systems 1562, philosophy
  1462, investor 1529. Total 8077 строк system-prompt'а. Frontmatter с
  `model: opus`, `tools: [Read, Write, Edit, Bash, Grep, Glob, Task]`,
  `granularity: jetix-shared`, `primary_alpha: task`.
- **Per-agent memory tree** (Karpathy 5-layer):
  - `agents/<id>/system.md` — Layer 1 Core (manager только; для ROY system
    prompt живёт в `.claude/agents/<id>.md`)
  - `agents/<id>/strategies.md` — Layer 2 System Prompt Learning (DRR ledger)
  - `agents/<id>/scratchpad.md` — Layer 3 working memory (некоторые agents)
  - `agents/<id>/niche/` — Layer 4 symlinks в `wiki/niches/` (per-agent slice)
  - `agents/<id>/versions/` — historical snapshots
  - 19 strategies.md files на 2026-04-29 (по одному на каждого agent + 3
    mini-swarm brigadiers).
- **Shared protocols / runtime contract:** `swarm/lib/shared-protocols.md`
  (9 секций: wiki-write / provenance / schema / HITL / tool-permission /
  cross-cell / writing-support / verb-dictionary / Max-sub+retrieval). Каждый
  agent reads этот файл при каждом Task invocation per his §7 import-stub.
- **Routing canonical:** `swarm/lib/routing-table.yaml` — declarative cell
  dispatch, task-shape → default_cells / optional_cells / forbidden_cells.
- **Wiki v3:** `swarm/wiki/` — 53 directories, 9 entity types
  (concepts/entities/sources/topics/claims/ideas/experiments/summaries/
  foundations), 12 edge types, 6 niches (personal/business/sales/life/tech/meta),
  + `_templates/`, `graph/edges.jsonl`, `index.md`, `log.md`, `meta/health.md`.
  Сейчас 382 .md файла в `swarm/wiki/`.
- **HITL gates:** `swarm/gates/AWAITING-APPROVAL-*.md` packets; 8 RUSLAN-ACK
  records закрытых per Foundation Build (`decisions/RUSLAN-ACK-WAVE-*-2026-04-28.md`).

**Orchestrator → workers — НЕ message bus, НЕ IPC.** Brigadier вызывает
экспертов **через нативный Claude Code `Task()` tool** (subagent invocation).
Возврат — структурированный YAML packet (см. shared-protocols §3): `summary` /
`proposed_writes[]` / `provenance[]` / `confidence` / `confidence_method` /
`escalations[]` / `dissents[]`. Brigadier — **sole_writer** в canonical
`swarm/wiki/`. Cells пишут только в `swarm/wiki/drafts/`. State-storage =
filesystem (git как audit trail; commit pattern `[<agent>] <cycle>: <description>`).

**Как ROY использует knowledge bases:**
- **Wiki v3 (`swarm/wiki/`)** — primary KB. Brigadier — sole writer; все cells
  читают через 4-tier retrieval (direct path → index+grep → typed-BFS over
  `graph/edges.jsonl` → bounded long-context fallback). Embeddings deferred к
  Phase B (re-evaluate когда FPAR < 0.80).
- **Books library (`raw/books-md/`)** — read-only reference, разделена по
  `expert:` frontmatter (см. §1.4). Никогда не дублируется в wiki entries.
- **Decisions / design / prompts / raw** — Tier-1 sources, цитируются по path
  в provenance gate.
- **Foundation v1.0** (10 LOCKED parts + Strategic Layer) — constitutional
  baseline; ROY читает per-cycle.

**ROY vs legacy 12 — coexistence:**

| Layer | Agents | Trigger |
|---|---|---|
| **ROY (Phase A)** | brigadier + 5 experts | knowledge-work cycles: deep-dives, Foundation build, layer synthesis, strategy options-papers |
| **Legacy 12** | manager + 11 dept agents | operational cycles: morning/evening pipeline, voice→KB ingest, CRM updates, sales outreach, daily-log |
| **Mini-swarm brigadiers** | project-brigadier, quick-money-brigadier, levenchuk-deep-dive-brigadier | per-project scoped (≤7 active tasks vs canonical brigadier ≤20); instantiated by `/project-bootstrap` |
| **Workers** | staging-writer, sweep-worker | batch operations (e.g., Notion Bank sweep, system-design staging) |

Legacy 12 = active. ROY 6 = active. Не conflict — разные слои.

## §2.3 ROY vs 12 legacy agents

**Сосуществование, не замена.** Status confirmed in `decisions/ROY-AGENTS-BUILT-2026-04-23.md`
§"Untouched in Phase A": «14 legacy agents under `.claude/agents/` (crazy-agent,
inbox-processor, knowledge-synth, life-coach, manager, meta-agent,
personal-assistant, sales-lead, sales-outreach, sales-researcher, staging-writer,
strategist, sweep-worker, system-admin) [и] v2 `wiki/` tree (read-write coexists
per Q9; v2↔v3 bridge is `cross-tree-ref` edge type only)».

Modelling tier: legacy агенты на Sonnet 4.6 / Haiku 4.5; ROY эксперты на Opus 4.7 (1M).

**Phase B будущее (не реализовано):** ROY эксперты «ингестят Tier-4 closed-core
book corpus (per-expert reading lists в §1b / §9 каждого expert) и переписывают
эти 6 файлов как v2 of itself. Phase B activation is HITL-gated; no auto-fire»
(`ROY-AGENTS-BUILT-2026-04-23.md`). На 2026-04-29 Phase B НЕ активирован.

## §2.4 Sources

- `/home/ruslan/jetix-os/decisions/ROY-AGENTS-BUILT-2026-04-23.md` — closure запись Phase A
- `/home/ruslan/jetix-os/decisions/ROY-ALIGNMENT-2026-04-22.md` — 5×4 matrix alignment
- `/home/ruslan/jetix-os/decisions/ROY-INFORMATION-DIET.md`
- `/home/ruslan/jetix-os/design/ROY-BUILD-LOGIC-2026-04-23.md`
- `/home/ruslan/jetix-os/design/ROY-WIKI-V3-GOALS-2026-04-23.md`
- `/home/ruslan/jetix-os/design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
- `/home/ruslan/jetix-os/decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
- `/home/ruslan/jetix-os/decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
- `/home/ruslan/jetix-os/.claude/agents/brigadier.md` (1005 строк)
- `/home/ruslan/jetix-os/.claude/agents/engineering-expert.md` (989)
- `/home/ruslan/jetix-os/.claude/agents/mgmt-expert.md` (1530)
- `/home/ruslan/jetix-os/.claude/agents/systems-expert.md` (1562)
- `/home/ruslan/jetix-os/.claude/agents/philosophy-expert.md` (1462)
- `/home/ruslan/jetix-os/.claude/agents/investor-expert.md` (1529)
- `/home/ruslan/jetix-os/.claude/agents/{project,quick-money,levenchuk-deep-dive}-brigadier.md`
- `/home/ruslan/jetix-os/.claude/agents/manager.md` (legacy hub)
- `/home/ruslan/jetix-os/swarm/lib/shared-protocols.md` — runtime contract D6
- `/home/ruslan/jetix-os/swarm/lib/routing-table.yaml` — Ashby variety ≥20 dispatch
- `/home/ruslan/jetix-os/swarm/wiki/overview.md` — Wiki v3 overview
- `/home/ruslan/jetix-os/swarm/wiki/index.md` — index
- `/home/ruslan/jetix-os/swarm/wiki/foundations/swarm-alphas.md` — α-1..α-5 state machines
- `/home/ruslan/jetix-os/agents/brigadier/strategies.md` (296 строк, 8 cycles closed)
- `/home/ruslan/jetix-os/agents/{engineering,mgmt,systems,philosophy,investor}-expert/strategies.md`

---

# §3 — Compounding Engineering

## §3.1 Implementation status (real / methodology / mixed)

**Mixed — концептуальная база external + structurally embedded в Foundation v1.0
+ operationally работает через 8 закрытых cycles, но НЕ как полностью
автономный Plan→Work→Review→Compound loop с self-modifying tools (как у Cora).**

- **External concept origin:** Kieran Klaassen / Every Inc. / building Cora email
  assistant. Popularised Dan Shipper. Endorsed Boris Cherny (Anthropic / Claude
  Code PM). Canonical статья:
  `raw/articles/2026-04-22-every-compound-engineering-guide.md`.
- **Research bundle в repo:** `raw/research/compounding-engineering-2026-04-22/`
  — 11 Perplexity research outputs R-1..R-11 + `SYNTHESIS-DEEP-CE-vs-JETIX.md`
  (~1018KB total). Wave-1 этой синтезы определила: **«CE-loop (discipline)
  substantive; CE-swarm (topology) provisional scaffolding»** (Walden Yan
  «Don't Build Multi-Agents» + Kim et al. arXiv:2512.08296 aggregate
  −3.5% multi-agent vs single-agent + MAST 14 failure modes — все сходятся, что
  multi-agent parallel code writing — marketing обёртка вокруг substantive loop'а).
- **Adopted as Foundation Part 5:**
  `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md`
  (LOCKED 2026-04-28). Это первое-принципное theoretical embedding CE в Jetix.
  3 канонических артефакта Part 5:
  1. **40/10/40/10 cycle ritual** (FUNDAMENTAL §2.2 — Plan 40% / Work 10% /
     Review 40% / Compound 10% с ±10pp drift tolerance) как обязательная
     дисциплина для всех cycles.
  2. **DRR ledger schema** (Decision / Reasoning / Result / Review per
     Compounding-Engineering §2 P2) — append-only в `agents/<id>/strategies.md`
     с `rule_slug` deduplication, `validated_in_cycles` accumulator, `ratio:
     {hits, misses}` decay counter.
  3. **Methodology promotion pipeline** (UND-2 binding) — validated patterns
     поднимаются from per-agent strategies.md → `wiki/methodology/<rule-slug>.md`
     через Part 6b gate (`gate_class: draft_promotion`); F4→F5 promotion на
     Ruslan ack; companion entry in `swarm/approvals/log.jsonl`; update
     `wiki/index.md`.

**Not implemented as full Cora-style auto-rewriting:**
- В Cora-loop tool description self-rewrite по cycle outputs (Anthropic case:
  −40% completion time). У Jetix этого пока нет — `agent system.md` self-modify
  явно ЗАПРЕЩЕНО в Tier-2 Constitutional rule 9 («AI does NOT self-modify at
  runtime»). System.md edits должны быть «gated cycle outputs» через HITL.
- Methodology promotion pipeline существует as Foundation, но `wiki/methodology/`
  на 2026-04-29 ещё не наполнен реальными rules — Part 5 проходит «dissolve-test
  condition» (OQ-MERGED-2: ≥3 distinct compound-phase-exclusive operations
  across Bundle 3 + 4 + Wave D — verdict: STANDALONE PRESERVED at 6.5 cumulative
  vs 3 threshold = 2.2× margin).

## §3.2 Cycle mechanics

**Реальный реализованный cycle pattern (видимый по `agents/brigadier/strategies.md`,
296 строк, 8 closed DRR-entries):**

```
Phase 1: Intake / WBS
  - read AWAITING-APPROVAL packet или prompt
  - decompose into task-shape (design / review / optimize / etc.)
  - map task-shape → cells via routing-table.yaml

Phase 2: Wave-A Parallel Dispatch
  - single message с N parallel Task() invocations
  - каждая Task имеет mode: critic|optimizer|integrator|scalability|writing-support
  - cells пишут drafts в swarm/wiki/drafts/

Phase 3: Wave-B/C (если нужно) — peer-input или synthesis cells

Phase 4: Brigadier Integration
  - Bash-concatenation drafts с awk frontmatter-strip
  - reconciliations pass (cross-section number, lock audit, F-G-R triple, provenance)
  - §1 TL;DR + §16 Integration Notes brigadier-self без expert dispatch

Phase 5: Provenance Gate (§5.5.5)
  - sources[] non-empty
  - inline [src:...] consistency
  - edge enum compliance
  - tier coherence
  - foundation conditions (если type=foundation)

Phase 6: AWAITING-APPROVAL packet → swarm/gates/

Phase 7: HITL — Ruslan ack via decisions/RUSLAN-ACK-*.md

Phase 8: Compound — DRR в strategies.md + cross-agent improvements + git push
```

**8 closed cycles на 2026-04-29 (per `agents/brigadier/strategies.md`):**
- cyc-1..cyc-7 — pre-foundation cycles (T-jetix-system-overview, T-km-materialization-mvp,
  T-layer-5/6/7-deep-dive, T-swarm-self-improve-v1)
- cyc-8 — `cyc-producer-services-strategy-options-2026-04-25` (PHASE 3 first
  cycle; OPTIONS-PAPER mode introduced; first cycle где AI explicitly does NOT
  strategize)
- cyc-12 — `cyc-foundation-build-2026-04-28` (LARGEST cycle; multi-wave; см. §3.3)

«Проверки» и «тесты» в repo:
- **Provenance gate** (`swarm/lib/shared-protocols.md` §2 — 6 binary-pass
  conditions)
- **Critic gates** (gate1 + gate2 в Шаге 2.2.4 — 0 showstoppers, 3+9+7 high/
  medium/low findings disposed)
- **§5.5.5 verification predicates** (Phase A bootstrap — 10 mechanical
  predicates ALL PASS, `raw/research/step-2-2-4-extractions/part-d-verification.md`)
- **M-D gates** в Wave D Integration Pass (M-D-1..M-D-6 — Coverage 55/55,
  Inter-Part contracts 52 edges 98.1%, 8 system-wide scenarios, 35 UC mapping
  31+4 stub, 62 anti-scope items 100% structurally enforced, 38 OQ catalogue
  routing — `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`)
- **F-G-R provenance triples** (Formality F2-F8 / Group-scope / Reliability
  R-low to R-high per `f-g-r.json` schema) — promoted на Part 6a
- **`/lint` skill** (5 signals: dangling-edge, orphan-concept, missing-frontmatter,
  duplicate-slug, cross-client-global) + flags `--check-stage-gates` /
  `--validate-predicate` / `--check-claude-md-sync`
- **dissolve-test verdict** на OQ-MERGED-2 в Wave D — STANDALONE PRESERVED
  margin 2.2× threshold

Это формальные **verification gates**, не unit tests. Кода-тестов в repo
почти нет (исключение — `tools/convert/test_e2e_no_api.py`, `crm/_tests/` 37
unittest-ов).

## §3.3 Foundation v1.0 application + iteration history

**Cycle: `cyc-foundation-build-2026-04-28`** — самый большой и формальный cycle
в repo. Применил 40/10/40/10 на macro-уровне (мульти-wave) и DRR на per-bundle
уровне.

**Iteration history (chronological, per `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/cycle-12-wave-a-history.md`
+ git log):**

| Wave | Date | Output | Что делалось |
|---|---|---|---|
| **Wave A — Master Plan Synthesis** | 2026-04-27 03:00-04:20Z | `MASTER-PLAN-DRAFT` + 5 expert pre-reads + 10 interface-cards | Phase A-0 (5 cells parallel) → A-1 integrator → A-2 (10 interface cards) → A-3 Wave-C work-list → A-4 master-plan → A-5 verification gate |
| **Wave B — Library Research** | 2026-04-27 same window | 14 consultant cards + library-inventory + framework-taxonomy + cycle-artefact-register | Phase B-0 library validation → B-2 batches 1+2+3 (14 cards parallel) → B-3 MANIFEST-DRAFT |
| **Wave C — Architecture (4 bundles)** | 2026-04-28 | 10 LOCKED Foundation parts | Bundle 1 (Parts 1/2/4/6a) → Bundle 2 (Parts 3/5/6b) → Bundle 3 (Parts 8/10) → Bundle 4 (Parts 7/9). Каждый bundle: cells per part → critic gate → Ruslan ack → next bundle. |
| **Wave D — Integration Pass** | 2026-04-28 | INTEGRATION-REPORT (5009 words) — 6 M-D gates PASS | Coverage matrix 55/55 cells (5 cross-cuts × 11 parts); Inter-Part contracts 52 edges (51 verified); 8 system-wide scenarios; 35 UC mapping; 62 anti-scope items 100% structurally enforced; OQ catalogue 38 items routed |
| **Bundle 5 Strategic Layer** | 2026-04-28 | Part 11 + `principles/` Pillar C | Pillar A (strategic direction substrate) + Pillar B (project strategy slot) + Pillar C (principles tree two-tier) |
| **Wave E LOCKED tag** | 2026-04-28 | `foundation-architecture-locked-2026-04-28` git tag | Final closure tag |
| **Wave 1 Mechanical Scaffolding** | 2026-04-28 | 40 артефактов (29 Lock scaffolds + 4 Insight scaffolds + 4 schemas + 4 configs + 8 lint stubs + 33-entry decisions DB index) | Скелет Pillar C tree + supporting infra |

**8 RUSLAN-ACK records закрыты** (gates между waves/bundles):
1. `RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` — Parts 1/2/4/6a baseline
2. `RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` — retroactive constitutional pattern
3. `RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md`
4. `RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` — Parts 3/5/6b
5. `RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md` — Parts 8/10
6. `RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md` — Parts 7/9
7. `RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md` — Coverage 55/55; Inter-Part 98.1%
8. `RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` — Pillar A/B/C placement
+ предыдущие на Шаге 2.2.4 (gate1 + gate2 для ROY swarm).

**Сколько итераций было:** Foundation Build один cycle (cyc-12), но **внутри 5
последовательных waves + 4 wave-C bundles + Strategic Layer extension + Wave 1
scaffolding = ~10 iteration-pass'ов** с Ruslan ack между каждым.

Plus ROY swarm itself был построен в отдельном cycle (Шаг 2.2.4, 2026-04-23) с
2 critic-gates (gate1 + gate2) и 2 Ruslan acks. Plus 8 pre-Foundation cycles
накопления patterns.

## §3.4 Sources

- `/home/ruslan/jetix-os/raw/articles/2026-04-22-every-compound-engineering-guide.md` — Klaassen canonical
- `/home/ruslan/jetix-os/raw/research/compounding-engineering-2026-04-22/R-1..R-11.md` (11 файлов)
- `/home/ruslan/jetix-os/raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md`
- `/home/ruslan/jetix-os/swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` — Foundation Part 5
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` — Consultant Card #7
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/cycle-12-wave-a-history.md` — chronological history (434 строки)
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` — Wave D 5009w
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/{D-0..D-6}-*.md` (7 phase artefacts)
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/SUMMARY.md`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-{1,2,3,4}/`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-C-BUNDLE-{1,2,3,4}-2026-04-28.md` (4 acks)
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement{,-2}-2026-04-28.md` (2 supplements)
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-STRATEGIC-LAYER-{TEMPLATES,PHASE-1-BASELINE}-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md`
- `/home/ruslan/jetix-os/decisions/AUDIT-CURRENT-STATE-2026-04-27.md`
- `/home/ruslan/jetix-os/agents/brigadier/strategies.md` — 296 строк, 8 closed DRR-cycles
- `/home/ruslan/jetix-os/.claude/skills/lint.md` — verification skill

---

# §4 — Master Sources List

**§1 Knowledge ingestion:**
- `/home/ruslan/jetix-os/raw/books-md/INDEX.md`
- `/home/ruslan/jetix-os/raw/books-md/_DELETED-LOG.md`
- `/home/ruslan/jetix-os/raw/books-md/_DELETED-LOG-DEEP.md`
- `/home/ruslan/jetix-os/raw/books-md/_FILTER-BLOCKED.md`
- `/home/ruslan/jetix-os/raw/books-md/<14 категорий>/<402 .md>`
- `/home/ruslan/jetix-os/raw/books/` (пустая, .gitkeep)
- `/home/ruslan/jetix-os/tools/convert/README.md`
- `/home/ruslan/jetix-os/tools/convert/{convert_all,gen_metadata,scan_cleanup,execute_cleanup,execute_deep_cleanup,mistral_ocr}.py`
- `/home/ruslan/jetix-os/tools/convert/marker_reocr.sh`
- `/home/ruslan/jetix-os/tools/convert/triage-report.json`
- `/home/ruslan/jetix-os/tools/convert/logs/20260427-{convert,frontmatter,index,main,ocr,quality,triage}.log`
- `/home/ruslan/jetix-os/tools/convert/{deep-cleanup-batches,deep-cleanup-verdicts}/`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/library-inventory.md`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md`
- `/home/ruslan/jetix-os/.claude/skills/ingest.md`
- `/home/ruslan/jetix-os/raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md` (sample)

**§2 ROY swarm:**
- `/home/ruslan/jetix-os/decisions/ROY-AGENTS-BUILT-2026-04-23.md`
- `/home/ruslan/jetix-os/decisions/ROY-ALIGNMENT-2026-04-22.md`
- `/home/ruslan/jetix-os/decisions/ROY-INFORMATION-DIET.md`
- `/home/ruslan/jetix-os/design/ROY-{BUILD-LOGIC,WIKI-V3-GOALS,WIKI-V3-ARCHITECTURE-SPEC}-2026-04-23.md`
- `/home/ruslan/jetix-os/decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
- `/home/ruslan/jetix-os/decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
- `/home/ruslan/jetix-os/.claude/agents/brigadier.md`
- `/home/ruslan/jetix-os/.claude/agents/{engineering,mgmt,systems,philosophy,investor}-expert.md`
- `/home/ruslan/jetix-os/.claude/agents/{project,quick-money,levenchuk-deep-dive}-brigadier.md`
- `/home/ruslan/jetix-os/.claude/agents/manager.md`
- `/home/ruslan/jetix-os/.claude/agents/{crazy-agent,inbox-processor,knowledge-synth,life-coach,meta-agent,personal-assistant,sales-lead,sales-outreach,sales-researcher,strategist,system-admin,staging-writer,sweep-worker}.md`
- `/home/ruslan/jetix-os/swarm/lib/shared-protocols.md`
- `/home/ruslan/jetix-os/swarm/lib/routing-table.yaml`
- `/home/ruslan/jetix-os/swarm/lib/README.md`
- `/home/ruslan/jetix-os/swarm/wiki/overview.md`
- `/home/ruslan/jetix-os/swarm/wiki/index.md`
- `/home/ruslan/jetix-os/swarm/wiki/foundations/swarm-alphas.md`
- `/home/ruslan/jetix-os/agents/brigadier/strategies.md`
- `/home/ruslan/jetix-os/agents/{engineering,mgmt,systems,philosophy,investor}-expert/strategies.md`
- `/home/ruslan/jetix-os/agents/{manager,sales-lead,sales-researcher,sales-outreach,life-coach,personal-assistant,knowledge-synth,system-admin,strategist,meta-agent,inbox-processor,crazy-agent,quick-money-brigadier}/strategies.md`

**§3 Compounding Engineering:**
- `/home/ruslan/jetix-os/raw/articles/2026-04-22-every-compound-engineering-guide.md`
- `/home/ruslan/jetix-os/raw/research/compounding-engineering-2026-04-22/R-{1..11}-*.md`
- `/home/ruslan/jetix-os/raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md`
- `/home/ruslan/jetix-os/swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/cycle-12-wave-a-history.md`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-{a,b,c,d,1-scaffolding}/`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/`
- `/home/ruslan/jetix-os/swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-C-BUNDLE-{1,2,3,4}-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement{,-2}-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/RUSLAN-ACK-STRATEGIC-LAYER-{BUNDLE-5,TEMPLATES,PHASE-1-BASELINE}-2026-04-28.md`
- `/home/ruslan/jetix-os/decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md`
- `/home/ruslan/jetix-os/decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- `/home/ruslan/jetix-os/decisions/AUDIT-CURRENT-STATE-2026-04-27.md`
- `/home/ruslan/jetix-os/.claude/skills/lint.md`
- `/home/ruslan/jetix-os/CLAUDE.md` (§4 Pillar C Principles boot context)
