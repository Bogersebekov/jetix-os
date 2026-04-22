---
source: raw/research/knowledge-architecture-deep-research-2026-04-19.md
extracted_by: W-1
date: 2026-04-23
scope: Q1, Q3, Q4, Q5, Q6
---

# W-1 extraction — knowledge architecture research

## Q1 — Retrieval mechanism primary

### Evidence (direct citations with §/line hints)

- §A.1 Karpathy pattern: «знания **компилируются один раз** и поддерживаются актуальными, а не переизвлекаются при каждом запросе. Паттерн работает „на удивление хорошо" при умеренном масштабе (~100 источников, сотни страниц) без embedding-инфраструктуры — только индекс + LLM-поиск.» (line 21)
- §A.3 HippoRAG: «текущий retrieval движок Jetix… Outperforms state-of-the-art RAG на multi-hop QA на **до 20%**… Single-step retrieval сопоставим с iterative IRCoT при **10-30x меньшей стоимости** и **6-13x быстрее**… Не требует dense vector infrastructure.» (lines 33–37)
- §B.1 таблица retrieval: «**Dense (BGE, Cohere, OpenAI)** … Подходит Jetix? — Нет при 557 стр.»; «**Graph (HippoRAG)** … Multi-hop, ассоциативный, не требует embeddings … **Текущий выбор ✓**»; «**Graph (GraphRAG)** … Дорогой preprocessing, latency … При 10K+ стр.» (lines 92–97)
- §B.2 pseudo-code: «HippoRAG Personalized PageRank retrieval. Текущий механизм wiki/graph/edges.jsonl + Seeds.» (lines 105–107). Pipeline: LLM keyword extraction → fuzzy_search seed nodes → PPR (alpha=0.85) → top-K → alpha-aware filtering.
- §B.4 long-context: «При 1M контексте Claude Opus 4.7 возникает соблазн просто загрузить всю вики… retrieval (select) + agent isolation — правильная стратегия. Long-context как **fallback** для edge cases, не как primary path.» (lines 186–187)
- §B.5 HyDE: «Применение в Jetix: перед keyword extraction для HippoRAG, LLM генерирует гипотетическую страницу вики → из неё извлекаются более точные keywords → лучшие seed nodes. Добавляет один LLM call, но улучшает качество на domain-specific запросах.» (lines 189–191)
- §H.5 retrieval_pipeline YAML: `primary: method: hipporag_ppr; index: wiki/graph/edges.jsonl; top_k: 20; alpha_aware: true`. HyDE as enhancement (+1 LLM call). Fallback_1: BM25 keyword when all PPR scores < 0.01. Fallback_2: long_context_full_load scoped to agent niche. `alpha_direct_lookup` (path lookup) wins with highest priority when query contains alpha ID. (lines 679–705)
- §A.6 / §E.3: filesystem grep/glob appears as a routing tier, not the primary semantic path: «1. Точный ID запрос (deal-042, client:acme) → прямой path lookup в alphas/ … 2. Семантический запрос … → HippoRAG на wiki/ … 4. Historical запрос → history.jsonl grep» (lines 384–390). Source does not explicitly call out "Claude Code agentic search" as separate candidate — it casts grep as the historical/ID-lookup tier.
- §G.3 evolution: «557 стр. Keyword + HippoRAG PPR»; «5K стр. BM25 + HippoRAG PPR»; «50K стр. Hybrid (BM25 + dense + PPR) + GraphRAG communities» (lines 462–465)
- Anti-pattern 6: «Vector DB для <3,000 страниц: дополнительная инфраструктура без выигрыша. HippoRAG PPR outperforms dense retrieval на multi-hop без embeddings.» (line 777)

### Pattern interpretation

Источник однозначно рекомендует **HippoRAG PPR на `wiki/graph/edges.jsonl` как primary retrieval** для Jetix при текущем масштабе (557 стр.), с HyDE как optional enhancement для domain-specific запросов. Dense embeddings и GraphRAG отвергаются до 5–10K страниц как over-engineering. Filesystem grep/glob и BM25 позиционируются как узкие tier-ы: grep для точных ID-запросов и history.jsonl scan, BM25 — как fallback при низких PPR score. Long-context прямо назван не-primary, а fallback для edge cases. Это совпадает с Max-subscription ограничением (PPR работает без paid embeddings) и принципом «не инфраструктура ради инфраструктуры» (§H.6, §G.1).

### Salient tradeoffs the source flags

- HippoRAG production-scale опыт на 10K+ страниц «ограничен — большинство бенчмарков работают на академических датасетах» (§A.3, line 39) и «точный performance threshold HippoRAG PPR при больших графах не задокументирован в production — это open research question» (§G.2, line 457).
- Качество PPR «зависит от KG extraction» (§B.1 таблица, line 96).
- HyDE — «дополнительный LLM call, latency» (§B.1 таблица, line 99; §H.5: «+1 LLM call, стоит для complex queries»).
- Long-context fallback рискует context rot (Anti-pattern 10, line 785).

## Q3 — Cross-reference format between layers

### Evidence (direct citations with §/line hints)

- §A.1 Karpathy three layers: raw sources / wiki (LLM-owned) / schema (CLAUDE.md / AGENTS.md) (lines 15–19).
- §B.2 synthesizer uses markdown wikilinks: «return llm_synthesize(query, context, citations)» где `citations = [f"[[{node.path}]]" for node in top_nodes]` (lines 136–138) — явный `[[file-ref]]` формат.
- §D.1 Вариант A (Alpha-as-Wiki) frontmatter пример:
  ```yaml
  wiki_edges:
    - supports: [[entities/deals/deal-042]]
    - based-on: [[entities/projects/website-redesign-q1]]
  ```
  (lines 261–271) — typed edges в YAML frontmatter **с** wikilink-синтаксисом.
- §D.3 Alpha ↔ Wiki edges как JSONL:
  ```jsonl
  {"from": "alphas/clients/acme-gmbh", "to": "wiki/entities/clients/acme-gmbh", "type": "alpha-ref", "ts": "2026-06-01"}
  ```
  (lines 323–328). Пять типов появляются: `alpha-ref`, `belongs-to`, `applies-to`, `derives-from`.
- §D.4 state.yaml использует path-refs: `client_ref: alphas/clients/acme-gmbh`, `history_ref: alphas/deals/deal-042/history.jsonl`, `wiki_ref: wiki/entities/deals/deal-042.md` (lines 336–347).
- §H.1 дерево: «`wiki/graph/edges.jsonl` — 572 typed edges (existing)» (line 530); «wiki/entities/ — wiki-side view для HippoRAG, не владеет state (только `alpha-ref` edge)» (line 565).
- §C.3 таблица: «Blackboard … `wiki/graph/edges.jsonl` (append-only = безопасно)»; «Event-sourced … применяется в `edges.jsonl` (append-only)» (§C.4, line 248).
- §F.2: «Karpathy: „good answers shouldn't disappear into chat history"» — citations писать в comparisons/ (line 426).
- §C.1 mapping: «Recall/Associative → Hippocampus → HippoRAG PPR traversal → `wiki/graph/edges.jsonl`» (line 210).

### Pattern interpretation

Источник описывает **комбинированный подход**: markdown wikilinks `[[path]]` используются внутри тела страниц и в синтезе (§B.2), YAML frontmatter хранит typed edges как human-authored declarations (`wiki_edges:` со вложенными `supports:`, `based-on:`) (§D.1), а `wiki/graph/edges.jsonl` — append-only, machine-consumable, event-sourced typed graph с полями `{from, to, type, ts}` (§D.3, §C.3/C.4). Между слоями (wiki ↔ alphas ↔ decisions) cross-ref идёт через явные `alpha-ref`, `belongs-to`, `applies-to`, `derives-from`, `wiki_ref`, `history_ref`, `client_ref` типы. Существующие 9 edge types расширяются alpha-aware вариантами.

### Salient tradeoffs the source flags

- Append-only edges.jsonl — безопасен к race conditions (§C.3, §C.4) но требует `/build-graph` пересборки.
- Dual-write при Hybrid C (state.yaml + wiki page + edges.jsonl) создаёт «sync overhead» (§D.1 Вариант B contra).
- §E.4: «При 5000+ страниц граница wiki/CRM начинает размываться. Решение: строгий тегинг через frontmatter `alpha_type:` на каждой wiki entity page, автоматический валидатор в CI».
- Anti-pattern 7: «изменение state.yaml без записи в history.jsonl. Теряется audit trail» (line 779).

## Q4 — Task-scoped Wiki context population

### Evidence (direct citations with §/line hints)

- §H.3 agent context loading — детальный pseudo-code с фиксированным бюджетом 50K токенов. «LAYER 4: Wiki retrieval через HippoRAG (20K budget)»:
  ```python
  wiki_nodes = await hipporag_retrieve(
      query=task.description,
      graph=wiki.graph,
      top_k=20,
      alpha_filter=task.alpha_type  # alpha-aware filtering
  )
  ```
  (lines 627–634). Это прямой HippoRAG PPR, **seeded from task description**, с фильтрацией по alpha.
- §H.3 priority rule: «при сжатии (auto-compact) — срезается от Layer 7 к Layer 4. Layers 1-3 всегда остаются. Layer 4 (wiki) сжимается до top-5 nodes.» (line 659)
- §H.3 LAYER 3: «Task + Alpha context (если задача связана с alpha)» — state.yaml + context.md загружаются автоматически если `task.alpha_ref` присутствует (lines 620–625).
- §H.3 LAYER 5: «Recent decisions relevant to task domain (3K)» — `grep_decisions(domain=task.domain, days=30, budget=3_000)` — auto-pull по domain tag (lines 637–642).
- §H.3 LAYER 6: mailbox — last 10 messages (lines 644–650).
- §B.2 PPR mechanism suits task description seeding: «Keyword extraction (неокортекс — LLM)» → seed nodes → PPR — это и есть «HippoRAG-style PPR seeded from task description».
- §B.3 agentic RAG loop: iterative retrieval with self-reflection — «assessment = llm_assess_coverage(query, retrieved_docs) … sub_queries = llm_decompose(assessment.gaps)» (lines 156–174).
- §H.5 `alpha_aware: true` в retrieval_pipeline (line 686) — alpha_type из task становится фильтром.
- §A.6 per-agent niche pattern: «agents/{id}/niche/ → symlinks … Semantic — связь с wiki-нишами» (line 222) — agent domain statically определяет срез, но task pulls через PPR.
- §E.3 routing: «Семантический запрос (что мы знаем о Mittelstand) → HippoRAG на wiki/» (line 387).

### Pattern interpretation

Источник рекомендует **hybrid automated pull**: preview через HippoRAG PPR, seeded from task description (query = task.description) с top_k=20 и alpha_filter = task.alpha_type. Agent niche (symlinks) даёт статический domain-scoped view, но для конкретной task основной наполнитель — PPR. Decisions pull by domain/time (auto-by-tags), mailbox — last-N. Manual pick источник явно не обсуждает; acquisition фундаментально автоматизирован через priority layers. Agentic RAG loop (§B.3) описан как iterative расширение если первое retrieval не покрывает gaps. Ни одно из решений не требует paid embeddings — всё строится на PPR поверх `edges.jsonl`.

### Salient tradeoffs the source flags

- Priority-based compaction: «Layer 4 (wiki) сжимается до top-5 nodes» когда не хватает места (§H.3) — риск потерять релевантный контекст.
- «top_k=20» как конкретное число без обсуждения sensitivity.
- Agentic RAG loop добавляет «max_iterations=3» LLM calls — стоимость (§B.3, line 147).
- Anti-pattern 8: «sales-агент читает wiki/concepts/tech/ вместо wiki/business/» — если role-manifest не имеет explicit `context_requirements` (alpha types + wiki niches), PPR может вытянуть нерелевантные nodes (line 781).
- Anti-pattern 10 (context rot): «ключевые инсайты сессии → writeback в strategies.md или wiki ПЕРЕД ожидаемой компакцией» (line 785).

## Q5 — Rot / staleness detection

### Evidence (direct citations with §/line hints)

- §F.4 Quality Control: «Индикаторы качества wiki: Orphan pages (нет inbound links) → `/lint` находит и флагит; Stale claims (противоречат новым источникам) → `/lint` маркирует `status: disputed`; Confidence levels в frontmatter: `confidence: high/medium/low` + `authority_source`.» (lines 436–439) — это прямой перечень сигналов: orphan, contradiction, confidence.
- §H.4 writeback rules включают: «Claim опровергнут → Обновить claim status → `wiki/claims/{slug}.md` → `status: refuted` + evidence» (line 674) — version-based superseded flag.
- §H.7 Week 4: «/lint прогон по всей вики — найти orphans, stale claims, missing alpha-refs» (line 740).
- §H.8 scale-up: «1,000 страниц: `/lint` переводится в daily (с weekly)» (line 748).
- §H.8 archival trigger: «10,000+ страниц: … страницы >2 лет без обновления → `_archive/`» (line 763) — **time-based signal**.
- §G.5 archival pattern: «Никогда не удалять, только архивировать … `status: archived` в frontmatter. Граф сохраняет edges (помечаются `archived: true`).» (lines 473–477).
- §A.1 compounding: «знания компилируются один раз и поддерживаются актуальными» (line 21) — принцип, но без указания механизма.
- §C.4 writeback patterns: «Reflection — LLM синтезирует episodic → semantic; применяется в `/lint` и `/consolidate`» (line 249) — LLM-based detection inside /lint.
- §F.4 FPAR metric: «FPAR (First-Pass Acceptance Rate) … какой % /ask ответов принимается без follow-up. Цель: >80%» — indirect signal on wiki staleness (line 436).
- Anti-pattern 10 context rot: «длинные сессии без /compact накапливают устаревший контекст» — но это context-level, не wiki-level (line 785).

### Pattern interpretation

Источник описывает **комбинацию сигналов**, оркестрируемую `/lint` (weekly now, daily at 1K pages):
1. **Orphan-based** (structural): нет inbound links.
2. **Contradiction-based** (semantic, via LLM): «противоречат новым источникам» → `status: disputed`.
3. **Version-based / superseded flag**: `status: refuted` + evidence при явном опровержении (§H.4).
4. **Manual confidence/authority tags**: `confidence: high/medium/low` + `authority_source` в frontmatter.
5. **Time-based**: только при 10K+ страниц (>2 лет без обновления → archive).

Автоматическое контрадикционное детектирование делает LLM внутри `/lint` (§C.4 reflection pattern), а не semantic embedding diff — что совместимо с Phase A «no paid embeddings». Источник ни разу не предлагает embedding-based staleness detection.

### Salient tradeoffs the source flags

- «Over-eager writeback: каждый /ask ответ файлится в comparisons/. Вики загрязняется низкокачественным контентом. Решение: novelty threshold + agent decision о write.» (Anti-pattern 3, line 771) — косвенно про upstream rot.
- §B.3 `NOVELTY_THRESHOLD` — параметр без указания значения (line 179).
- Time-based triggers — только at scale (>10K стр.), т.е. источник не считает time-based достаточным при Jetix-текущем масштабе.
- `/lint` в CI после каждого merge: «`/lint` в CI validates graph integrity после каждого merge» (§G.4, line 469) — но только integrity, не staleness content.

## Q6 — Skill learning pipeline (candidate → active)

### Evidence (direct citations with §/line hints)

- §A.1: «Jetix уже реализовал этот паттерн в расширенной форме: 557 страниц, 9 типов сущностей, 6 ниш, HippoRAG PPR, Skills Pipeline v2 (/ingest, /ask, /lint, /consolidate, /build-graph).» (line 23) — существующий skill inventory.
- §C.1 Procedural memory mapping: «CLAUDE.md rules, skills pipeline → `/skills/*.md`, `roles/<role>.md`» (line 205).
- §H.1 folder tree:
  ```
  langfuse/                     # Prompt registry + tracing (R2)
  └── prompts/
      └── {agent}/{skill}.yaml
  ```
  (lines 556–558). Promt registry layer for skills существует.
- §E.1 Source of Truth: «**Prompts & Skills** | `.claude/agents/`, `langfuse/` | — | В wiki» (line 367) — skills canonical в `.claude/agents/` + langfuse, не в wiki.
- §H.4 writeback: «Агент узнал стратегию → Стратегия → `agents/{id}/strategies.md` → Append strategy block» (line 671) — strategies layer как «System Prompt Learning накопления».
- §H.4: «/ingest нового источника → Source summary + entity pages → `wiki/sources/`, `wiki/entities/` → Полный wiki ingestion» (line 668) — формализованный /ingest.
- §F.4 FPAR metric «First-Pass Acceptance Rate» — метрика для оценки качества, но применена к wiki ответам, не к skills как таковым.
- §H.7 migration: «Implement writeback rules (H.4 таблица) как explicit triggers в agent skills» (line 734) — skills как explicit-triggered, но без формального lifecycle.

### Pattern interpretation

Источник **не описывает формализованный skill learning lifecycle** (Candidate → Draft → Eval → Activation → Usage monitoring → Deprecation). То что явно присутствует:
- Skills Pipeline v2 как inventory: `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph` (§A.1) — уже активные.
- Prompt registry слой: `langfuse/prompts/{agent}/{skill}.yaml` (§H.1) — инфраструктура для versioning.
- Strategies accumulation: `agents/{id}/strategies.md` как «System Prompt Learning» layer, append-strategy-block паттерн (§H.4, §C.1).
- FPAR metric для quality, но на уровне ответов /ask, не skills.
- Owner roles источник не закрепляет — skills упоминаются как «agent skills» без назначения dept/role ownership.

**[source largely silent]** на eval (golden-set), activation gating, deprecation procedures. Это gap, который данный источник не закрывает.

### Salient tradeoffs the source flags

- Anti-pattern 4: «Monolithic system.md: role-manifest агента превышает 5K токенов … Решение: core identity <2K, детали → strategies.md.» (line 773) — косвенное ограничение на длину, влияет на skill scope.
- §A.6: «Лимит MEMORY.md: 200 строк — критично для дизайна Jetix per-agent memory» (line 56) — capacity constraint для procedural memory.
- Langfuse как prompt registry (§H.1) — готовая инфраструктура для tracing и versioning, но lifecycle-гейтинг не описан.

## New variants / insights found (optional)

- **Alpha-aware retrieval filtering** (§B.2 pseudo-code, lines 126–129; §H.5 `alpha_aware: true`) — не-стандартное расширение HippoRAG PPR: top nodes фильтруются по `alpha_type` из текущего контекста. Потенциально релевантно для Q1/Q4.
- **`alpha_direct_lookup` как highest-priority retrieval tier** (§H.5, lines 701–705): если query содержит alpha ID (e.g. "deal-042", "client:acme"), path lookup в `alphas/` обгоняет семантический retrieval. Это конкретный argument в пользу filesystem lookup *в дополнение* к PPR, не как замена. Может быть релевантно для Q1 как hybrid.
- **Hierarchical compounding holonic loop** (§F.1, lines 400–420): «Raw experience → sources → claims → topics (patterns) → summaries → foundations → role-manifest integration». Каждый уровень — холон. Это явный promotion ladder для knowledge (не skills), релевантен как mental model для Q6 (по аналогии).
- **Diátaxis-for-data mapping** (§E.2, lines 373–378) — структурный принцип разграничения «Tutorial/Procedural → roles/*.md»; «Reference/Facts → wiki/concepts/, alpha YAMLs»; «Explanation → wiki/topics/, wiki/ideas/»; «Episodic/Log → history.jsonl, wiki/experiments/». Релевантно для Q3 как meta-framework cross-ref.
- **Rule «один шаг до источника»** (§E.2, line 379): «любой агент должен уметь найти canonical data в ≤1 hop». Релевантно для Q1 default tier выбора.
