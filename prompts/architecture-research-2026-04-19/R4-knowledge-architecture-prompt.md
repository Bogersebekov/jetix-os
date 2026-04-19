---
research-id: R4
wave: 2
topic: Knowledge-base архитектура для AI-native company — wiki + context + memory systems
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/knowledge-architecture-deep-research-2026-04-19.md
priority: P1 (критично — блокирует D5 Knowledge Architecture + интеграцию wiki/ с role-framework)
builds-on: R1 (career levels), R2 (company-as-code), R3 (Левенчук)
---

# R4 — Knowledge Architecture для AI-native Jetix

## Зачем этот research

У Jetix уже есть **557-страничная wiki/** (Karpathy LLM Wiki + OmegaWiki pattern + HippoRAG PPR retrieval) — это мощный актив. Но **не ясно как интегрировать** её с новой company-as-code архитектурой:

- Где хранится **контекст для ролей** — в wiki или в role-manifests?
- Как связаны **wiki entries** с **10 core alphas** из R3 (Client, Project, Deal...)?
- Какие **memory systems** нужны AI-агентам — persistent vs ephemeral, shared vs per-role?
- Как wiki **питает L2 Cognitive** (стратегирование, мышление письмом) и **L5 Membrane** (authority content)?
- Где **граница** между wiki (knowledge) vs CRM (relationships) vs projects (work) vs decisions (RFDs)?
- Как **retrieval** работает в runtime (когда agent выполняет задачу, что он читает)?

Выход research'а — input для **D5 Knowledge Architecture** документа + detailed integration plan wiki ↔ role-framework.

## Как использовать

Скопируй **всё между `=== PROMPT START ===` и `=== PROMPT END ===`** и вставь в Perplexity Max Computer. Собственная вкладка, параллельно R5, R6, R7.

---

=== PROMPT START ===

Ты — senior knowledge management architect с экспертизой в knowledge bases для AI-agent systems, retrieval patterns, graph databases, и corporate knowledge management. Я прошу **глубокий академический research** по теме: **как спроектировать knowledge architecture для AI-native компании, где у нас уже есть working wiki (557 страниц, 572 edges, Karpathy/OmegaWiki pattern, HippoRAG retrieval) и нужно интегрировать её с company-as-code архитектурой (роли + альфы + 12+ AI-агентов)**.

Это specific integration research, не generic «как построить wiki».

## Контекст проекта Jetix (2500 слов)

**Jetix** — AI-native mega-corporation под один founder (Ruslan, Берлин) + 12+ AI-агентов через Claude Code (Opus 4.7, 1M context). Target market — немецкий Mittelstand. Q2 2026 цель €50K revenue.

**Архитектура Jetix — 7 слоёв + L0** (утверждена):
- **L0 Executive Core** — Ruslan + AI-агенты + future human executors через единую role-abstraction
- **L1 Foundation** — Git + markdown + YAML, prompt-as-code, CI/CD, docs-as-code, postmortems
- **L2 Cognitive** — системное мышление Левенчука (ШСМ): роль, альфа, граф создания, стратегирование, мышление письмом
- **L3 Product** — repetitive products (Jetix Club, productized SKUs)
- **L4 Delivery** — agency+consulting hybrid (primary Q2 revenue)
- **L5 Membrane** — community (newsletter, Alliance, Club)
- **L6 Topology** — platform horizon 18-36 мес
- **L7 Portfolio** — holding-дисциплина (attention + capital + hours allocation)

**Nested hierarchy:** Life-OS = root (жизнь founder'а), Jetix = один из проектов Life-OS с полной 7-слойной архитектурой внутри. Полное разделение ресурсов.

**Принцип scale-up-first:** при 10x росте (капитала / часов / людей / проектов / ролей) система справляется **без rebuild**. Это обязательное требование.

## Существующая wiki/ (уже на сервере)

**Структура wiki/ (557 страниц):**
- **9 entity types** (Karpathy LLM Wiki pattern): concepts/, entities/, sources/, topics/, ideas/, experiments/, claims/, summaries/, foundations/
- **9 edge types**: supports/, extends/, contradicts/, based-on/, refines/, applies-to/, derives-from/, cross-refs/, cited-by/
- **6 niches** для агентских views: personal/, business/, sales/, life/, tech/, meta/
- **wiki/graph/edges.jsonl** — 572 typed edges в JSONL (append-only)
- **wiki/log.md** — append-only хронология
- **wiki/comparisons/** — writeback `/ask` (вопросы с ответами)
- **wiki/_templates/** — шаблоны для каждого entity type

**Retrieval:**
- **HippoRAG Personalized PageRank** на графе (не vector embeddings!)
- Keyword match → seed nodes → PPR → top-20 страниц
- Synthesizer LLM формирует ответ с citations `[[file-ref]]`

**Skills (wiki pipeline v2):**
- `/ingest <path-or-url>` — источник → wiki-страницы + index + log + edges
- `/ask <question>` — поиск + синтез с citations + опциональная запись в comparisons/
- `/lint` — health check (orphans, contradictions, stale claims)
- `/consolidate` — merge дубликатов
- `/build-graph` — пересборка communities

**Per-agent memory (5 layers) — текущий дизайн:**
- `agents/{id}/system.md` — Core (system prompt)
- `agents/{id}/strategies.md` — System Prompt Learning накопления
- `agents/{id}/scratchpad.md` — Working memory
- `agents/{id}/niche/` — symlinks в wiki/niches/{niche}/
- `comms/mailboxes/{id}.jsonl` — Recall

## Wave 1 findings, на которые надо опираться

**R3 (Левенчук для AI)** утвердил концепцию **5 примитивов ШСМ**:
- **Роль** = функциональная позиция (Purpose + Accountabilities + Decision-rights)
- **Альфа** = lifecycle-entity с состояниями. 10 core alphas для Jetix: Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem
- **Граф создания** = кто создаёт что для кого
- **Стратегирование** = метод выбора метода (ДО работы)
- **Мышление письмом** = экзокортекс для founder и агентов

R3 определил **ключевое открытие:** в AI-эпоху узкое место — **framing** (постановка задачи). Метрика FPAR (First-Pass Acceptance Rate) — целевая.

R3 также предложил **role-manifest** структуру (8 блоков) где агент имеет:
- `context_requirements` (что надо прочитать ДО работы)
- `produces:` / `consumes:` (граф создания)
- `thinking_protocol` (как думать — mini-FPF)

**R2 (Company-as-code)** утвердил:
- Git + markdown + YAML = база данных
- **Diátaxis documentation framework** (4 формы: tutorial / how-to / reference / explanation)
- **Langfuse self-hosted** как prompt registry + tracing
- Folder structure draft с `life-os/`, `jetix/`, `docs/`, `secrets/`, `.claude/agents/`
- Separate `roles/<role>.md` (abstract) vs `executors/agents/<name>.yaml` (concrete executor)

**R1 (Career levels)** дал:
- J1-J5 + JX ladder
- Role-manifest YAML template (example sales-lead)
- Decision-rights matrix

## Ключевой вопрос этого research

Как **интегрировать** существующую wiki/ (557 страниц, HippoRAG retrieval) с новой role-framework так, чтобы:

1. **Agents получали правильный context в runtime** — не слишком мало (плохой framing), не слишком много (context pollution)
2. **Альфы (Client, Project и т.д.) жили понятно** — где их state tracking, где их content, как связаны с wiki knowledge
3. **Knowledge compounding работал** — новые insights от работы агентов попадали обратно в wiki
4. **Retrieval был production-grade** — быстрый, точный, traceable
5. **Scale-up поддерживался** — от 557 страниц сейчас до 10,000+ при team phase

## Основной research-запрос

Проведи **глубокий академический research** по следующим темам. Каждая — обязательный раздел финального отчёта.

### Часть A — Knowledge base patterns для AI-agent systems (SOTA 2024-2026)

1. **Andrej Karpathy LLM Wiki** — [original tweet](https://twitter.com/karpathy) + community iterations. Full concept: 9 entity types, why 9, how graph grows, какие limitations.

2. **OmegaWiki / OmegaT patterns** — concept-based knowledge organization. Как отличается от traditional wiki.

3. **HippoRAG** (Gutiérrez et al. NeurIPS 2024) — original paper. Personalized PageRank retrieval vs vector embeddings. Performance benchmarks. Когда лучше чем dense retrieval, когда хуже.

4. **GraphRAG** (Microsoft Research 2024) — community detection, hierarchical summaries. Сравнение с HippoRAG.

5. **MemGPT** (Packer et al. 2023) — OS-inspired memory management. Context window management. Hierarchical storage (working/archival).

6. **Letta** (evolution of MemGPT 2024-2025) — persistent agent memory. Production patterns.

7. **Mem0** (open-source memory layer 2025) — как organize agent memories.

8. **Claude Code memory system** — Anthropic documentation. `auto memory` (user/feedback/project/reference types). Integration patterns.

9. **Obsidian / Foam / Dendron** — personal knowledge management tools с linked notes. Adoption в AI-agent contexts.

10. **Logseq / AnyType** — block-based alternative. Database-style properties.

11. **Academic frameworks:**
   - **PKM (Personal Knowledge Management)** — Niklas Luhmann Zettelkasten, Sönke Ahrens «How to Take Smart Notes»
   - **Second Brain** — Tiago Forte CODE framework (Capture/Organize/Distill/Express)
   - **Building a Second Brain** digital patterns

Источники: arxiv.org papers (HippoRAG, GraphRAG, MemGPT, Mem0), Anthropic engineering blog, Andrej Karpathy blog/tweets, Obsidian forum, Logseq documentation. Academic papers on PKM. Tiago Forte «Building a Second Brain» (2022).

### Часть B — Retrieval patterns deep-dive

Академический сравнительный обзор retrieval approaches для agent context.

1. **Dense retrieval** (vector embeddings) — BGE, Cohere embed-v3, OpenAI text-embedding-3. When best, when fails.

2. **Sparse retrieval** (BM25, SPLADE) — когда vector overkill.

3. **Hybrid retrieval** — Reciprocal Rank Fusion, какие weighting schemes работают.

4. **Graph-based retrieval** — HippoRAG PPR, GraphRAG communities, LightRAG. Когда лучше чем dense.

5. **Query-aware retrieval** — HyDE (Hypothetical Document Embeddings), Query Decomposition patterns.

6. **Long-context vs retrieval** — когда Claude 1M context hooked, когда retrieval нужен. Anthropic research на long-context limits.

7. **Agentic RAG** (2024-2025) — agent сам выбирает что читать. Self-RAG, Agentic search patterns.

8. **Context engineering** (Anthropic 2025) — вместо prompt engineering. Как organize context for agents.

9. **Production latency considerations** — response time budgets, caching strategies, prefetching.

Источники: arxiv.org retrieval papers 2023-2026, Anthropic context engineering blog, OpenAI retrieval docs, Vespa / Weaviate / Qdrant documentation. ACL/NeurIPS/EMNLP 2024-2025 retrieval track.

### Часть C — Memory systems для AI-agents

1. **Memory taxonomy:**
   - **Short-term** (session context) — chat history
   - **Working** (active task) — scratchpad
   - **Long-term episodic** (past interactions) — agent history
   - **Long-term semantic** (facts, knowledge) — wiki-like storage
   - **Procedural** (how to do things) — playbooks, skills
   - **Meta-cognitive** (self-model) — role-manifest

   Academic framework из cognitive science. Как применимо к AI-agents.

2. **Persistence models:**
   - Ephemeral (context window only) — default Claude/GPT
   - Session-persistent — chat history
   - Project-persistent — папка данных
   - Agent-persistent — собственная память агента
   - Shared — все агенты видят
   - Public wiki — видны всем + client-facing

3. **Memory in Claude Code specifically:**
   - `.claude/CLAUDE.md` project memory
   - `~/.claude/projects/*/memory/` auto-memory (user/feedback/project/reference)
   - `MEMORY.md` index
   - Как это integrates с `agents/<name>/system.md`

4. **Multi-agent shared memory patterns:**
   - Blackboard architecture (classic AI)
   - Message-passing (agent mailboxes — существует в Jetix как `comms/mailboxes/`)
   - Shared knowledge graph (all agents read/write)
   - Per-agent niche views (existing Jetix pattern)

5. **Memory update patterns:**
   - Write-through (каждое действие → update memory)
   - Write-back (batch updates в конце session)
   - Reflection-based (periodic consolidation)
   - Event-sourced (append-only, views derived)

6. **Memory conflict resolution:**
   - CRDTs для concurrent updates
   - Eventual consistency
   - Version vectors
   - Single-writer assumption (Jetix current)

Источники: arxiv.org memory papers (MemGPT, Letta, Mem0 specifically), cognitive psychology references (Endel Tulving memory systems, Kahneman System 1/2), distributed systems textbooks (Kleppmann «Designing Data-Intensive Applications»). Claude Code documentation.

### Часть D — Knowledge base ↔ Alpha lifecycle integration

Это критическая интеграция. 10 core alphas из R3 (Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem) должны как-то связаны с wiki/ (existing knowledge graph).

Вопросы:

1. **Где живёт Alpha data?**
   - Вариант A: полностью в wiki/ (каждый клиент = страница wiki/entities/)
   - Вариант B: separate `alphas/<type>/<id>.md` + cross-references в wiki
   - Вариант C: external DB для fast-changing alphas (invoices, deals) + wiki for stable (clients, members)
   - Сравнительный анализ

2. **State transitions:**
   - Как atomically update state (git commit с alpha-state tag предложен в R3)
   - Как обеспечить eventual consistency (alpha state matches wiki content)
   - Как rollback state changes

3. **Alpha ↔ knowledge:**
   - Client alpha → запись в wiki/entities/<client-name>.md (история, решения, insights from this client)
   - Project alpha → wiki/projects/<slug>.md (goals, decisions, artefacts)
   - Hypothesis alpha → wiki/ideas/<hypothesis>.md (formulation, evidence, verdict)
   - Research Note alpha → wiki/sources/ or wiki/summaries/
   - Paradigmas для каждого типа

4. **Linking alphas:**
   - Client × Project × Deal edges
   - Hypothesis × Project × Research edges
   - Как navigate graph: «show me all projects for client X» / «show me all hypotheses related to SKU Y»
   - Existing wiki/graph/edges.jsonl 9 edge types — достаточно ли?

5. **Alpha history:**
   - Как store старые states (git log достаточен? или отдельный alpha-log/?)
   - Audit trail «когда Deal перешёл из draft в signed, кто approved»

### Часть E — Где граница? (Wiki vs CRM vs projects vs decisions)

У Jetix много «мест где живёт информация»:

- `wiki/` — knowledge
- `projects/` — active work  
- `decisions/` — RFDs
- `clients/` (proposed) — CRM-like
- `sales/` (proposed) — pipeline
- `daily-log/` — temporal
- `reflection/`, `health/` — Life-OS
- `tasks/` — work items

Вопросы:

1. **Taxonomy principles** — как решить что где живёт?

2. **Cross-linking** — когда один item имеет aspects в разных папках:
   - Client Schmidt GmbH имеет presence в `clients/schmidt-gmbh.md` (CRM), `wiki/entities/schmidt-gmbh.md` (history), `projects/schmidt-audit/` (active work), множество `decisions/` (проектные RFDs)
   - Как keep in sync, чтобы не стало inconsistent

3. **Source of truth pattern** — каждый facet has one authoritative location, остальные ссылаются.

4. **Migration and evolution** — когда перемещать данные (project закончился → в wiki/summaries/?)

5. **Search experience** — founder ищет «Schmidt GmbH» и должен найти всё relevant без duplicates.

6. **Scale implications** — когда `clients/` вырастет до 500 entries, какой pattern работает, какой ломается.

### Часть F — Knowledge compounding (как knowledge растёт через работу)

1. **Writeback patterns:**
   - `/ask` writeback в `comparisons/` (existing Jetix)
   - Every closed project → writeback в `wiki/summaries/`
   - Every client interaction → update `wiki/entities/<client>/`
   - Every decision → link в relevant wiki entry
   - Automated vs manual writeback

2. **Insight loop:**
   - Client interactions produce insights
   - Insights → wiki/claims/
   - Claims aggregate into patterns → wiki/summaries/
   - Patterns inform strategies → wiki/foundations/
   - Это Левенчуковская мереология холонов в действии

3. **Cross-document synthesis (agent-driven):**
   - `knowledge-synth` agent genera periodic summaries
   - Monthly «what did we learn this month»
   - Quarterly review pulls from wiki log

4. **Community vs internal knowledge:**
   - Какие wiki entries eventually стать newsletter content
   - Sanitization (remove client-sensitive info)
   - Версионирование public vs private

5. **Quality control:**
   - `/lint` для orphan detection, contradictions
   - When to merge (`/consolidate`)
   - When to archive (stale)

### Часть G — Scale: 557 pages → 5000 → 50,000

1. **Folder structure evolution:**
   - Когда `wiki/concepts/` нужно разделить на subcategories
   - How to avoid nested nightmare

2. **Graph performance:**
   - HippoRAG PPR на 50,000 nodes — performance?
   - Когда нужно sharding

3. **Search infrastructure:**
   - Сейчас grep-based? Или full-text index (ripgrep, ugrep)?
   - Когда нужна proper search (Meilisearch / Typesense)?
   - When vector search adds value (despite HippoRAG preference)

4. **Multi-user scenarios:**
   - Когда team editing wiki — how avoid conflicts
   - Review workflows (PR-based для wiki changes)

5. **Preservation:**
   - Как не потерять context когда системе 3 года и 50K страниц
   - Retrieval «what did we think about X in 2026 vs 2028»

6. **Deletion vs archival:**
   - Append-only pattern vs hard delete
   - Когда нужен proper archive

### Часть H — Практические выходы для Jetix

**Самая важная часть.**

1. **Финальная knowledge architecture для Jetix** — конкретный folder tree + дата-flows между компонентами:
   - `wiki/` (knowledge, existing)
   - `alphas/<type>/<id>.md` (lifecycle entities — новое?)
   - `projects/<slug>/` (active work)
   - `clients/<name>.md` (CRM-lite)
   - `decisions/` (RFDs)
   - и т.д.

   С объяснением что куда идёт и почему.

2. **Alpha storage decision** — где именно хранятся 10 alphas. С таблицей.

3. **Agent context loading pattern** — когда agent начинает task:
   - Что читает из role-manifest
   - Что читает из wiki (via retrieval)
   - Что читает из alpha state (current client/project/etc)
   - Что читает из history (previous similar tasks)
   - Budget: max ~50K tokens context для Claude Opus 4.7

4. **Writeback rules** — после каждого task:
   - Что записывается в wiki
   - Что в alpha state
   - Что в daily-log
   - Что в postmortem (if failure)

5. **Retrieval integration** — HippoRAG pipeline сейчас + что улучшить:
   - Keep: PPR retrieval
   - Add: long-context fallback (если PPR top-20 недостаточно)
   - Add: alpha-aware filtering (отфильтровать по client/project context)

6. **Memory tier recommendation** — какая memory для чего:
   - Ephemeral (context only): current tasks
   - Project-persistent: `projects/<slug>/context.md`
   - Agent-persistent: `agents/<name>/strategies.md`, `scratchpad.md`
   - Shared knowledge: `wiki/`
   - Alpha state: `alphas/<type>/<id>.md`

7. **Migration path** от current state (557 pages wiki + нет alphas + некоторые CRM attempts):
   - Week 1: заложить alphas/ folder, первая client alpha
   - Week 2: migration текущих clients в alphas + wiki entries
   - Week 3: connect alphas to wiki via edges
   - Week 4: agent context loading refactor

8. **Scale-up triggers:**
   - 1000 pages → what changes
   - 5000 pages → what changes
   - Team phase (multiple writers) → what changes

9. **Anti-patterns specific Jetix:**
   - Duplicate truth в нескольких местах
   - Orphan entries
   - Stale writes (прочитал, не обновил)
   - Context pollution (agent читает слишком много)
   - Premature scale infrastructure (sharding 557 pages)

## Format требования

- **Объём:** 5000-10000 слов
- **Format:** Markdown, явные Parts A-H
- **Citations:** primary sources (arxiv papers, official docs, authoritative blogs)
- **Code examples** для retrieval pipelines, folder structures
- **Tables** для comparisons (memory types, retrieval approaches, alpha storage options)
- **Honest about uncertainty** — где research не устоявшийся, явно
- **Build on Wave 1** — reference R1/R2/R3 findings где релевантно, не переповторять

## Anti-patterns

- ❌ Generic «how to build wiki» без учёта существующей Karpathy/OmegaWiki pattern
- ❌ Без integration с role-framework из R3
- ❌ Игнор Claude Code-specific memory system
- ❌ Over-engineered рекомендации (vector DB для 557 pages)
- ❌ Ignoring HippoRAG уже работающий pattern
- ❌ Без Part H

## Критерий успеха

На основе этого research я могу:
1. Написать `design/JETIX-KNOWLEDGE-ARCHITECTURE.md` (D5 финальный чистовик)
2. Спроектировать alpha storage + cross-linking pattern
3. Определить agent context loading rules
4. Spec writeback automation
5. Migration plan 557 pages → integrated knowledge system

Приступай. Академично, с citations, Part H actionable.

=== PROMPT END ===

---

## Notes для Ruslan

**Параллельно с R5/R6/R7.** Все 4 можно запустить в 4 отдельных Perplexity Computer tabs одновременно.

**Output file:** `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
