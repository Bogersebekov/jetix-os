# Jetix Knowledge Architecture Research
## Академический research-отчёт: архитектура знаний для AI-native компании

**Автор контекста:** Ruslan, Jetix (Берлин)  
**Дата:** Июнь 2026  
**Статус:** Wave 2 — Knowledge Architecture Design  
**Опирается на:** Wave 1 findings R1 (Career Levels), R2 (Company-as-Code), R3 (ШСМ/Альфы)

---

## Part A — Knowledge Base Patterns для AI-Agent Systems: SOTA 2024–2026

### A.1 Karpathy LLM Wiki Pattern

В апреле 2026 Андрей Карпати опубликовал [LLM Wiki гист](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — паттерн, который Jetix уже реализует. Суть в том, что LLM выступает не поисковым инструментом, а **компилятором и главным редактором**: он читает сырые источники и строит структурированную вики из взаимосвязанных markdown-файлов. Три слоя:

1. **Raw sources** (иммутабельные) — source of truth
2. **Wiki** (LLM-owned) — скомпилированные статьи, entity pages, comparisons
3. **Schema** (CLAUDE.md / AGENTS.md) — конфигурационный файл, превращающий LLM в дисциплинированного редактора

Ключевое отличие от традиционного RAG: знания **компилируются один раз** и поддерживаются актуальными, а не переизвлекаются при каждом запросе. Паттерн работает «на удивление хорошо» при умеренном масштабе (~100 источников, сотни страниц) без embedding-инфраструктуры — только индекс + LLM-поиск. Хорошие ответы **файлятся обратно в вики**, что создаёт эффект компаундирования.

Jetix уже реализовал этот паттерн в расширенной форме: 557 страниц, 9 типов сущностей, 6 ниш, HippoRAG PPR, Skills Pipeline v2 (/ingest, /ask, /lint, /consolidate, /build-graph). Это значительно опережает базовый Karpathy-паттерн.

### A.2 GraphRAG (Microsoft Research, 2024)

[GraphRAG](https://arxiv.org/abs/2404.16130) — граф-базированный подход Microsoft Research для query-focused summarization. LLM строит entity knowledge graph в два этапа: (1) извлечение сущностей из документов → (2) прегенерация community summaries для кластеров связанных сущностей. При запросе каждый community summary генерирует partial response, которые затем синтезируются.

GraphRAG решает специфическую проблему **глобальных запросов** ("Какие основные темы в корпусе?") — то, с чем стандартный RAG не справляется. Масштаб: датасеты в 1M токенов. Ключевое ограничение для Jetix: GraphRAG требует сложной preprocessing-инфраструктуры и дорогих community detection вычислений. При 557 страницах это over-engineering. Актуально при масштабировании к 5000+ страниц для cross-domain synthesis.

### A.3 HippoRAG (NeurIPS 2024)

[HippoRAG](https://arxiv.org/abs/2405.14831) — текущий retrieval движок Jetix. Вдохновлён hippocampal indexing theory: LLM (неокортекс) + knowledge graph (гиппокамп) + Personalized PageRank (паттерны ассоциаций). Преимущества:

- Outperforms state-of-the-art RAG на multi-hop QA на **до 20%**
- Single-step retrieval сопоставим с iterative IRCoT при **10-30x меньшей стоимости** и **6-13x быстрее**
- Не требует dense vector infrastructure

[HippoRAG 2 (ICML 2025)](https://icml.cc/virtual/2025/poster/45585) добавляет deeper passage integration и более эффективное online использование LLM, давая ещё **+7% на associativity tasks**. Неопределённость: production-scale опыт HippoRAG на 10,000+ страниц ограничен — большинство бенчмарков работают на академических датасетах.

### A.4 MemGPT / Letta

[MemGPT](https://arxiv.org/abs/2310.08560) (ныне Letta) — виртуальное управление контекстом по аналогии с OS paging. Иерархия памяти: fast in-context ↔ slow external storage с interrupt-based control flow. Агент сам управляет тем, что держать в контексте. Ключевая концепция для Jetix: **агент как OS-процесс**, который активно перемещает данные между memory tiers.

### A.5 Mem0 (2025)

[Mem0](https://arxiv.org/abs/2504.19413) — production-ready архитектура для долгосрочной памяти AI-агентов. Динамически извлекает, консолидирует и извлекает информацию из разговоров. Граф-вариант добавляет реляционные структуры. На бенчмарке LOCOMO: **26% улучшение** над OpenAI memory system, **91% снижение p95 latency**, **>90% экономия токенов** по сравнению с full-context. Зрелость: публичный API, но production track record ограничен (2025 — early adoption).

### A.6 Claude Code Memory System

Детально исследован в контексте Jetix как ключевая интеграционная точка. [Официальная документация](https://code.claude.com/docs/en/memory) описывает две системы:

- **CLAUDE.md** — инструкции, написанные разработчиком; загружаются каждую сессию; 3 scope (project/user/org)
- **Auto memory** — заметки, которые Claude пишет сам; MEMORY.md как индекс (200 строк / 25KB limit); 4 категории (user, feedback, project, reference)

Agent scopes: Project (`.claude/agent-memory/<name>/`, в git), Local (`~/.claude/agent-memory-local/<name>/`), User (`~/.claude/agent-memory/<name>/`). Лимит MEMORY.md: 200 строк — критично для дизайна Jetix per-agent memory.

### A.7 Obsidian, Logseq, Foam, Dendron

Существующие PKM-инструменты для сравнения:
- **[Obsidian](https://obsidian.md)** — vault-based, markdown, backlinks, graph view; сильная plugin-экосистема
- **[Logseq](https://logseq.com)** — outliner + graph; блок-ориентированный
- **[Foam](https://foambubble.github.io)** — VS Code extension, Zettelkasten-like, git-native
- **[Dendron](https://dendron.so)** — иерархические заметки в VS Code, schema-driven

Для Jetix критично, что все эти инструменты **не интегрированы с агентами**. Git + markdown подход Jetix технически превосходит их с точки зрения CI/CD интеграции и multi-agent access.

### A.8 Zettelkasten / Luhmann / Ahrens

Niklas Luhmann начал строить Zettelkasten в 1950-х, накопив [90,000 карточек](https://www.ernestchiang.com/en/posts/2025/niklas-luhmann-original-zettelkasten-method/) за 40 лет. Его система: две slip-boxes (библиографическая + основная), уникальные адреса (folgezettel numbering), surfable hypertext. Luhmann называл её своим "communication partner" — внешним мозгом, способным удивлять.

Sönke Ahrens в «How to Take Smart Notes» (2017) систематизировал метод. Ключевые принципы, применимые к Jetix: (1) атомарность заметок, (2) заметки в собственных словах, (3) немедленное связывание с существующими концептами, (4) индекс как entry point.

### A.9 Tiago Forte: BASB и CODE

[Building a Second Brain](https://www.buildingasecondbrain.com) — методология Tiago Forte для экстернализации и организации знаний. Framework CODE:
- **C**apture — избирательный захват
- **O**rganize — структурирование (PARA: Projects/Areas/Resources/Archives)
- **D**istill — дистилляция к core insights
- **E**xpress — создание ценности из накопленного

Для Jetix CODE-принцип особенно важен в части Distill → Express: claims → patterns → summaries → foundations (аналог Левенчуковской мереологии).

---

## Part B — Retrieval Patterns: от Dense до Agentic RAG

### B.1 Taxonomия retrieval подходов

| Подход | Механизм | Преимущества | Ограничения | Подходит Jetix? |
|--------|----------|-------------|-------------|----------------|
| **Dense (BGE, Cohere, OpenAI)** | Векторное сходство в embedding space | Семантический поиск, без keyword matching | Инфраструктура (vector DB), embedding cost, нет multi-hop | Нет при 557 стр. |
| **Sparse (BM25)** | TF-IDF веса, inverted index | Точное keyword matching, нет GPU | Нет семантики, падает на синонимах | Полезен как fallback |
| **Learned Sparse (SPLADE)** | Sparse vector representations | Лучше BM25 семантически, эффективен | Требует обучения | Не нужен сейчас |
| **Hybrid (BM25 + Dense + RRF)** | Reciprocal Rank Fusion | +15-30% recall vs single methods | Сложность, инфраструктура | При 5000+ стр. |
| **Graph (HippoRAG)** | Knowledge graph + PPR | Multi-hop, ассоциативный, не требует embeddings | Качество зависит от KG extraction | **Текущий выбор ✓** |
| **Graph (GraphRAG)** | Community summaries | Global sensemaking queries | Дорогой preprocessing, latency | При 10K+ стр. |
| **Graph (LightRAG)** | Dual-level: low (facts) + high (themes) | Incremental updates, combined graph+vector | Новый (2024), early adoption | Следить |
| **HyDE** | LLM генерирует гипотетический ответ → embedding | Zero-shot, bridging query-doc gap | Дополнительный LLM call, latency | Улучшение /ask |
| **Self-RAG** | LLM решает когда и надо ли retrieval | Уменьшает ненужные retrievals | Требует обучения специального LLM | Reference only |

### B.2 HippoRAG PPR: pseudo-code для Jetix

```python
def hipporag_retrieve(query: str, graph: KnowledgeGraph, top_k: int = 20) -> list[Node]:
    """
    HippoRAG Personalized PageRank retrieval.
    Текущий механизм wiki/graph/edges.jsonl + Seeds.
    """
    # 1. Keyword extraction (неокортекс — LLM)
    keywords = llm_extract_keywords(query)  # e.g. ["Client", "onboarding", "friction"]
    
    # 2. Seed nodes — find matching nodes in KG
    seed_nodes = []
    for kw in keywords:
        matches = graph.fuzzy_search(kw)  # matches в 9 типах сущностей Jetix
        seed_nodes.extend(matches)
    
    # 3. Personalized PageRank (гиппокамп — ассоциативная активация)
    personalization = {node: 1.0 / len(seed_nodes) for node in seed_nodes}
    ppr_scores = graph.pagerank(personalization=personalization, alpha=0.85)
    
    # 4. Top-K nodes
    top_nodes = sorted(ppr_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    
    # 5. Alpha-aware filtering (Jetix-specific enhancement)
    if query_has_alpha_context(query):
        alpha_type = detect_alpha_type(query)  # Client, Project, Deal, etc.
        top_nodes = filter_by_alpha(top_nodes, alpha_type)
    
    return top_nodes


def hipporag_synthesize(query: str, top_nodes: list[Node]) -> str:
    """Синтезатор LLM с [[file-ref]] citations (текущий Jetix /ask)."""
    context = "\n\n".join([node.content for node in top_nodes])
    citations = [f"[[{node.path}]]" for node in top_nodes]
    return llm_synthesize(query, context, citations)
```

### B.3 Agentic RAG Loop

```python
async def agentic_rag_loop(
    query: str,
    agent_context: AgentContext,
    max_iterations: int = 3
) -> str:
    """
    Agentic RAG с self-reflection и writeback.
    Инспирирован MA-RAG (arxiv 2505.20096) и Agentic RAG patterns.
    """
    iteration = 0
    retrieved_docs = []
    
    while iteration < max_iterations:
        # Retrieve
        candidates = hipporag_retrieve(query, wiki.graph, top_k=20)
        retrieved_docs.extend(candidates)
        
        # Assess completeness (self-reflection)
        assessment = llm_assess_coverage(query, retrieved_docs)
        
        if assessment.is_complete:
            break
        
        # Decompose and re-query
        sub_queries = llm_decompose(assessment.gaps)
        for sq in sub_queries:
            additional = hipporag_retrieve(sq, wiki.graph, top_k=10)
            retrieved_docs.extend(additional)
        
        iteration += 1
    
    # Synthesize
    answer = hipporag_synthesize(query, deduplicate(retrieved_docs))
    
    # Writeback if insight is valuable
    if llm_assess_novelty(answer) > NOVELTY_THRESHOLD:
        wiki.ingest_comparison(query=query, answer=answer)
    
    return answer
```

### B.4 Long-context vs Retrieval

При 1M контексте Claude Opus 4.7 возникает соблазн просто загрузить всю вики. Anthropic context engineering (via LangChain analysis) определяет четыре стратегии: **write, select, compress, isolate**. Ключевой инсайт: "Many agents with isolated contexts outperformed single-agent." Для Jetix: retrieval (select) + agent isolation — правильная стратегия. Long-context как **fallback** для edge cases, не как primary path.

### B.5 HyDE для Jetix /ask

HyDE ([Hypothetical Document Embeddings](https://zilliz.com/learn/improve-rag-and-information-retrieval-with-hyde-hypothetical-document-embeddings)) улучшает recall когда запрос отличается по стилю от документов вики. Применение в Jetix: перед keyword extraction для HippoRAG, LLM генерирует гипотетическую страницу вики → из неё извлекаются более точные keywords → лучшие seed nodes. Добавляет один LLM call, но улучшает качество на domain-specific запросах.

---

## Part C — Memory Systems: Таксономия и Persistence Models

### C.1 Таксономия памяти: Tulving × Kahneman × AI

[Endel Tulving](http://donaldclarkplanb.blogspot.com/2020/02/tulving-episodic-semantic-memory.html) в 1972 предложил разделение на episodic (события в пространстве-времени) и semantic (факты, концепты, независимые от времени) memory. В 1983 расширил до System of Systems. Kahneman добавляет System 1 / System 2 — быстрое автоматическое vs медленное сознательное мышление.

Применение к AI-agent системам:

| Тип памяти | Tulving/Kahneman аналог | AI реализация | Jetix mapping |
|------------|------------------------|---------------|---------------|
| **Procedural** | Моторная память | CLAUDE.md rules, skills pipeline | `/skills/*.md`, `roles/<role>.md` |
| **Semantic** | Семантическая (факты, концепты) | Wiki entities, concepts, foundations | `wiki/concepts/`, `wiki/entities/`, `wiki/foundations/` |
| **Episodic** | Эпизодическая (события с контекстом) | Postmortems, logs, session history | `wiki/experiments/`, `postmortems/`, `agents/{id}/scratchpad.md` |
| **Working** | Рабочая память (System 1 fast) | In-context window | Активный conversation context |
| **Meta-cognitive** | Metacognition | Self-reflection, strategies | `agents/{id}/strategies.md` |
| **Recall/Associative** | Hippocampus | HippoRAG PPR traversal | `wiki/graph/edges.jsonl` |

### C.2 Claude Code Memory Specifics для Jetix

Текущая 5-слойная per-agent архитектура Jetix:

```
agents/{id}/
├── system.md          # Core — что агент есть (Procedural, всегда в контексте)
├── strategies.md      # System Prompt Learning — Meta-cognitive layer
├── scratchpad.md      # Working — эпизодическая, сбрасывается между сессиями
├── niche/ → symlinks  # Semantic — связь с wiki-нишами
└── comms/mailboxes/{id}.jsonl  # Recall — episodic межагентная коммуникация
```

Критические ограничения Claude Code auto-memory:
- 200 строк / 25KB на MEMORY.md — **жёсткий лимит**
- Только keyword search внутри auto-memory (без semantic)
- Machine-local — не shared между агентами
- Auto-compact срабатывает при ~75% контекста (50K токенов в 200K окне на компакцию)

Решение Jetix: использовать `agents/{id}/system.md` как CLAUDE.md-аналог (структурированный, version-controlled в git), а wiki/ как общую semantic memory через HippoRAG, минуя ограничения Claude Code auto-memory.

### C.3 Multi-Agent Shared Memory: Паттерны

| Паттерн | Механизм | Cons | Применение в Jetix |
|---------|----------|------|-------------------|
| **Blackboard** | Общая запись, все читают | Race conditions | `wiki/graph/edges.jsonl` (append-only = безопасно) |
| **Message-passing** | Async mailboxes | Потеря при сбое | `comms/mailboxes/{id}.jsonl` |
| **Shared KG** | Общий граф знаний | Конфликты при одновременном изменении | `wiki/` через git pull/push |
| **Per-agent niche** | Изолированные view через symlinks | Информационные siloes | `agents/{id}/niche/` → `wiki/niches/` |

### C.4 Writeback Patterns и Conflict Resolution

Четыре паттерна обновления памяти:

1. **Write-through** — немедленная запись при изменении; применяется для alpha state transitions
2. **Write-back (dirty flag)** — пакетная запись; применяется в `/consolidate` скилле
3. **Event-sourced** — только события, текущее состояние = replay; применяется в `edges.jsonl` (append-only)
4. **Reflection** — LLM синтезирует episodic → semantic; применяется в `/lint` и `/consolidate`

Для конфликтов в многоагентной среде: **git merge + conventional commits** решают 90% случаев. CRDTs ([crdt.tech](https://crdt.tech)) актуальны при масштабировании к distributed multi-user. Для текущего Jetix: append-only для edges.jsonl + timestamp-based versioning для alpha state.

---

## Part D — KB ↔ Alpha Lifecycle Integration

### D.1 Три варианта хранения Alpha Data

**Вариант A: Alpha-as-Wiki** — альфа живёт только в wiki/ как entity page

```yaml
# wiki/entities/clients/acme-gmbh.md
type: alpha
alpha_type: Client
state: active_deal
stage: proposal_sent
created: 2026-01-15
wiki_edges:
  - supports: [[entities/deals/deal-042]]
  - based-on: [[entities/projects/website-redesign-q1]]
```

Плюсы: единое хранилище, HippoRAG retrieval, linkable. Минусы: wiki не оптимизирована для operational state management, плохо для частых state transitions.

**Вариант B: Alpha-as-YAML in dedicated folder** — structured data отдельно, wiki — только semantic layer

```
jetix/
├── alphas/
│   ├── clients/acme-gmbh.yaml          # State + operational data
│   ├── projects/website-redesign.yaml  # Project alpha
│   ├── deals/deal-042.yaml             # Deal alpha
│   └── invoices/inv-2026-042.yaml      # Invoice alpha
└── wiki/                               # Semantic knowledge only
    └── entities/clients/acme-gmbh.md  # Wiki article, linked to YAML
```

Плюсы: clean separation of concerns, YAML для operational, wiki для semantic. Минусы: два места для одной сущности, sync overhead.

**Вариант C: Hybrid — Alpha State Machine + Wiki Sidecar**

```
jetix/
├── alphas/{type}/{id}/
│   ├── state.yaml          # Машина состояний: current_state, transitions, timestamps
│   ├── context.md          # Rich context для агентов
│   └── history.jsonl       # Event log (append-only, как edges.jsonl)
└── wiki/
    └── entities/{type}/{id}.md  # Wiki page с [[symlink-ref]] на alphas/
```

Плюсы: полное разделение state (YAML) / context (md) / history (jsonl), event-sourced audit trail, wiki остаётся semantic. Минусы: три файла на alpha.

### D.2 Alpha Storage Decision Matrix

| Alpha | Частота изменений | Operational complexity | Рекомендация | Хранение |
|-------|------------------|----------------------|--------------|---------|
| **Client** | Низкая (месяцы) | Средняя (CRM-like) | Hybrid C | `alphas/clients/{id}/` + wiki entity |
| **Project** | Средняя (недели) | Высокая (timeline, tasks) | Hybrid C | `alphas/projects/{id}/` + wiki |
| **Deal** | Высокая (дни) | Высокая (stage machine) | Hybrid C | `alphas/deals/{id}/` + wiki |
| **Invoice** | Низкая после создания | Низкая (finalized) | YAML-only B | `alphas/invoices/{id}.yaml` |
| **Content Item** | Средняя | Средняя | Hybrid C | `alphas/content/{id}/` + wiki |
| **Hypothesis** | Высокая (эксперименты) | Низкая | Wiki-primary A | `wiki/claims/{id}.md` + claims/ |
| **SKU** | Низкая (stable) | Низкая | YAML-only B | `jetix/products/{sku}.yaml` |
| **Member** | Низкая | Средняя | Hybrid C | `alphas/members/{id}/` + wiki |
| **Research Note** | Высокая | Низкая | Wiki-primary A | `wiki/sources/{id}.md` |
| **Postmortem** | Разовая (immutable) | Низкая | Wiki-primary A | `wiki/experiments/{id}.md` |

### D.3 Alpha ↔ Wiki Edge Types

Расширение существующих 9 edge types для alpha-awareness:

```jsonl
{"from": "alphas/clients/acme-gmbh", "to": "wiki/entities/clients/acme-gmbh", "type": "alpha-ref", "ts": "2026-06-01"}
{"from": "alphas/deals/deal-042", "to": "alphas/clients/acme-gmbh", "type": "belongs-to", "ts": "2026-06-01"}
{"from": "wiki/claims/client-onboarding-friction", "to": "alphas/clients/acme-gmbh", "type": "applies-to", "ts": "2026-06-01"}
{"from": "alphas/projects/website-redesign", "to": "wiki/concepts/dienstleistungen-mittelstand", "type": "derives-from", "ts": "2026-06-01"}
```

### D.4 State Machine для Deal Alpha (пример)

```yaml
# alphas/deals/deal-042/state.yaml
alpha_type: Deal
id: deal-042
client_ref: alphas/clients/acme-gmbh
current_state: proposal_sent
valid_transitions:
  proposal_sent: [negotiation, lost, on_hold]
  negotiation: [won, lost]
  won: [delivery]
  delivery: [completed, at_risk]
  completed: []  # terminal
  lost: []       # terminal
history_ref: alphas/deals/deal-042/history.jsonl
wiki_ref: wiki/entities/deals/deal-042.md
```

---

## Part E — Граница wiki / CRM / Projects / Decisions

### E.1 Source of Truth Matrix

Принцип: каждый тип данных имеет **одного владельца** и **понятный путь** для всех агентов.

| Категория данных | Source of Truth | Вторичное хранилище | Никогда не дублировать |
|----------------|----------------|--------------------|-----------------------|
| **Alpha state** | `alphas/{type}/{id}/state.yaml` | `wiki/entities/` (read-only ref) | В scratchpad агента |
| **Alpha history** | `alphas/{type}/{id}/history.jsonl` | — | В wiki (только summaries) |
| **Semantic knowledge** | `wiki/concepts/`, `wiki/foundations/` | agents niche symlinks | В YAML |
| **Claims & Hypotheses** | `wiki/claims/` | — | В alpha state |
| **Role definitions** | `roles/<role>.md` | agents/{id}/system.md | В wiki |
| **Agent strategies** | `agents/{id}/strategies.md` | — | В wiki/concepts |
| **Postmortems** | `wiki/experiments/` | — | В alphas/ |
| **Research & Sources** | `wiki/sources/` | — | В alphas/ |
| **Prompts & Skills** | `.claude/agents/`, `langfuse/` | — | В wiki |
| **Financial records** | `alphas/invoices/`, secrets/ | — | В wiki |
| **Decisions** | `decisions/` (ADR-pattern) | Wiki cross-ref | Дважды в разных местах |

### E.2 Принципы разграничения

**Критерий "Diátaxis для данных"** (по аналогии с [diataxis.fr](https://diataxis.fr)):
- **Tutorial/Procedural** → `roles/*.md`, `wiki/how-to/`
- **Reference/Facts** → `wiki/concepts/`, `wiki/foundations/`, alpha YAMLs
- **Explanation** → `wiki/topics/`, `wiki/ideas/`
- **Episodic/Log** → `history.jsonl`, `wiki/experiments/`, `log.md`

**Правило "один шаг до источника"**: любой агент должен уметь найти canonical data в ≤1 hop. Запрос "текущий статус deal-042" → `alphas/deals/deal-042/state.yaml` (не через wiki search).

### E.3 Search UX по слоям

```
Запрос агента → Routing logic:
1. Точный ID запрос (deal-042, client:acme) → прямой path lookup в alphas/
2. Семантический запрос (что мы знаем о Mittelstand) → HippoRAG на wiki/
3. State/status запрос → alphas/{type}/ YAML scan
4. Historical запрос → history.jsonl grep
5. Cross-domain synthesis → HippoRAG + LLM consolidation
```

### E.4 Scale Implications

При 5000+ страниц граница wiki/CRM начинает размываться. Решение: **строгий тегинг** через frontmatter `alpha_type:` на каждой wiki entity page, автоматический валидатор в CI что все alphas имеют state.yaml владельца.

---

## Part F — Knowledge Compounding: Writeback и Insight Loop

### F.1 Insight Loop: от Claims к Foundations

Левенчуковская мереология холонов применима к knowledge compounding:

```
Raw experience (episodic)
    ↓ /ingest
wiki/sources/{source}.md  (summary)
    ↓ claim extraction
wiki/claims/{claim}.md    (falsifiable assertion)
    ↓ pattern recognition (/consolidate)
wiki/topics/{pattern}.md  (recurring pattern)
    ↓ synthesis (/build-graph + LLM)
wiki/summaries/{domain}.md (domain synthesis)
    ↓ abstraction
wiki/foundations/{principle}.md (fundamental principle)
    ↓ role-manifest integration
roles/{role}.md → thinking_protocol (mini-FPF)
```

Каждый уровень — холон: целое на своём уровне и часть на следующем. Этот loop — механизм Knowledge Compounding в Jetix.

### F.2 Writeback Patterns

Три механизма writeback в Jetix:

1. **Explicit writeback** — `/ask` ответы файлятся в `wiki/comparisons/`. Karpathy: "good answers shouldn't disappear into chat history"
2. **Agent-triggered writeback** — агент при обнаружении нового инсайта вызывает `/ingest` с синтезированным контентом
3. **Scheduled consolidation** — `/consolidate` периодически запускается, находит orphan claims и создаёт pattern pages

### F.3 Cross-doc Synthesis

Проблема: 557 страниц содержат latent connections, которые не видны при single-document retrieval. Решение: `/build-graph` + GraphRAG-inspired community detection для выявления кластеров семантически близких концептов. При Jetix-масштабе (557 стр.) это делается через `/lint` + LLM synthesis раз в неделю.

### F.4 Quality Control

Метрика **FPAR** (First-Pass Acceptance Rate) из R3 применима к wiki-контенту: какой % /ask ответов принимается без follow-up. Цель: >80%. Индикаторы качества wiki:
- Orphan pages (нет inbound links) → `/lint` находит и флагит
- Stale claims (противоречат новым источникам) → `/lint` маркирует `status: disputed`
- Confidence levels в frontmatter: `confidence: high/medium/low` + `authority_source`

---

## Part G — Scale 557→5000→50,000 Pages

### G.1 Folder Evolution

**557 страниц (сейчас):** Flat-ish структура внутри 9 entity types. HippoRAG PPR на едином графе. `/lint` раз в неделю. Всё в памяти агента при необходимости.

**5,000 страниц:** Введение namespace-шардирования внутри entity types (по niches + alpha types). Граф может потребовать разбивки на subgraphs. `/consolidate` по расписанию daily. Начало использования GraphRAG для cross-domain global queries.

**50,000 страниц:** Необходима инфраструктура: sparse index (BM25) + граф (HippoRAG/LightRAG) + community summaries (GraphRAG). Multi-user PR workflows. Archive/cold storage для deprecated pages.

### G.2 Graph Performance

HippoRAG PPR на 572 edges (сейчас) — тривиальная операция. При 5,000 pages и ~5,700 edges (линейный рост) — всё ещё быстро в памяти. При 50,000 pages + 50K+ edges — требуется персистентный граф-хранилище. **Порог для Neo4j/ArangoDB: ~20,000 edges** при регулярных multi-hop queries. До этого `edges.jsonl` + networkx в памяти достаточен.

Неопределённость: точный performance threshold HippoRAG PPR при больших графах не задокументирован в production — это open research question.

### G.3 Search Infrastructure Evolution

| Масштаб | Search | Graph | Storage |
|---------|--------|-------|---------|
| 557 стр. | Keyword + HippoRAG PPR | edges.jsonl (networkx) | git + markdown |
| 5K стр. | BM25 + HippoRAG PPR | edges.jsonl + periodic graph rebuild | git + markdown |
| 50K стр. | Hybrid (BM25 + dense + PPR) + GraphRAG communities | Neo4j / LightRAG | git + markdown + vector DB |

### G.4 Multi-User PR Workflows

При добавлении human executors (R1 J1-J5 + JX): wiki изменения через Pull Requests. Конфликты в edges.jsonl (append-only) — минимальны. Конфликты в alpha state.yaml — требуют merge strategy: last-writer-wins для status fields, event-sourcing для history. `/lint` в CI validates graph integrity после каждого merge.

### G.5 Deletion и Archival

Никогда не удалять, только архивировать. Паттерн:
```
wiki/entities/clients/old-client.md → wiki/_archive/2026/entities/clients/old-client.md
```
`status: archived` в frontmatter. Граф сохраняет edges (помечаются `archived: true`). History.jsonl — иммутабельный.

---

## Part H — Финальная Knowledge Architecture для Jetix (Actionable)

### H.1 Финальный Folder Tree

```
life-os/                          # Root (Ruslan's Life OS)
├── jetix/                        # Jetix mega-corporation
│   ├── CLAUDE.md                 # Master schema для всех агентов
│   ├── .claude/
│   │   └── agents/               # Per-agent configs (R2 pattern)
│   │       ├── ceo-agent.yaml
│   │       ├── sales-agent.yaml
│   │       └── ...
│   ├── roles/                    # Abstract role definitions (R1/R2)
│   │   ├── ceo.md
│   │   ├── sales-executive.md
│   │   └── _template.md
│   ├── executors/
│   │   └── agents/               # Concrete agent manifests
│   │       └── {name}.yaml
│   ├── agents/                   # Per-agent memory (5-layer, R2)
│   │   └── {id}/
│   │       ├── system.md         # Core identity + role-manifest
│   │       ├── strategies.md     # Meta-cognitive strategies
│   │       ├── scratchpad.md     # Working memory
│   │       └── niche/ → symlinks # wiki/niches/* symlinks
│   ├── alphas/                   # 10 Alpha state machines (NEW)
│   │   ├── clients/
│   │   │   └── {id}/
│   │   │       ├── state.yaml    # Current state, transitions
│   │   │       ├── context.md    # Rich agent context
│   │   │       └── history.jsonl # Append-only event log
│   │   ├── projects/
│   │   │   └── {id}/ (same pattern)
│   │   ├── deals/
│   │   │   └── {id}/ (same pattern)
│   │   ├── invoices/
│   │   │   └── {id}.yaml         # Simple (no state machine needed)
│   │   ├── content/
│   │   │   └── {id}/ (same pattern)
│   │   ├── members/
│   │   │   └── {id}/ (same pattern)
│   │   └── skus/
│   │       └── {sku}.yaml        # Product definitions
│   ├── wiki/                     # 557 страниц — semantic KG (existing)
│   │   ├── CLAUDE.md             # Wiki schema (existing)
│   │   ├── index.md              # Master index
│   │   ├── log.md                # Chronological append-only
│   │   ├── graph/
│   │   │   └── edges.jsonl       # 572 typed edges (existing)
│   │   ├── concepts/             # {personal,business,sales,life,tech,meta}/
│   │   ├── entities/             # Clients, Projects, etc. (wiki-side refs)
│   │   ├── sources/              # Research Notes (Alpha wiki-primary)
│   │   ├── topics/
│   │   ├── ideas/
│   │   ├── experiments/          # Postmortems (Alpha wiki-primary)
│   │   ├── claims/               # Hypotheses (Alpha wiki-primary)
│   │   ├── summaries/
│   │   ├── foundations/
│   │   ├── comparisons/          # Writeback от /ask
│   │   └── _templates/
│   ├── decisions/                # ADR-pattern для major decisions
│   │   └── {YYYY-MM-DD}-{slug}.md
│   ├── comms/
│   │   └── mailboxes/
│   │       └── {agent-id}.jsonl  # Recall memory (existing)
│   ├── docs/                     # Diátaxis structure (R2)
│   │   ├── tutorials/
│   │   ├── how-to/
│   │   ├── reference/
│   │   └── explanation/
│   ├── products/                 # L3 Product layer
│   │   └── jetix-club/
│   └── secrets/                  # Encrypted, gitignored
│       └── .env.*
└── langfuse/                     # Prompt registry + tracing (R2)
    └── prompts/
        └── {agent}/{skill}.yaml
```

**Почему каждая папка:**
- `alphas/` — отделяет operational state от semantic knowledge, решает dual-write проблему
- `decisions/` — ADR-паттерн для трассируемости решений (не дублируется в wiki, только cross-ref)
- `agents/{id}/system.md` — заменяет Claude Code auto-memory, version-controlled в git
- `wiki/entities/` — wiki-side view для HippoRAG, не владеет state (только `alpha-ref` edge)

### H.2 Alpha Storage: где живёт каждая из 10 alphas

| Alpha | Canonical Location | Wiki Location | Storage Pattern | Обоснование |
|-------|-------------------|---------------|----------------|-------------|
| **Client** | `alphas/clients/{id}/state.yaml` | `wiki/entities/clients/{id}.md` | Hybrid C | Долгоживущий, много связей, нужен rich context |
| **Project** | `alphas/projects/{id}/state.yaml` | `wiki/entities/projects/{id}.md` | Hybrid C | Timeline, tasks, deliverables — нужна state machine |
| **Deal** | `alphas/deals/{id}/state.yaml` | `wiki/entities/deals/{id}.md` | Hybrid C | Частые state transitions (proposal→won→lost) |
| **Invoice** | `alphas/invoices/{id}.yaml` | Нет отдельной wiki page | YAML-only B | Финализирован после создания, нет semantic value |
| **Content Item** | `alphas/content/{id}/state.yaml` | `wiki/sources/{id}.md` (если research) | Hybrid C | Tracking production state + wiki для insights |
| **Hypothesis** | `wiki/claims/{id}.md` | **IS** the wiki page | Wiki-primary A | Семантика IS содержание; state = frontmatter |
| **SKU** | `alphas/skus/{sku}.yaml` | `wiki/entities/skus/{sku}.md` (если сложный) | YAML-only B | Stable, operational, не нуждается в narrative |
| **Member** | `alphas/members/{id}/state.yaml` | `wiki/entities/members/{id}.md` | Hybrid C | Community member journey tracking |
| **Research Note** | `wiki/sources/{id}.md` | **IS** the wiki page | Wiki-primary A | Это и есть wiki source ingestion |
| **Postmortem** | `wiki/experiments/{id}.md` | **IS** the wiki page | Wiki-primary A | Иммутабельный после написания; learning IS содержание |

### H.3 Agent Context Loading Pattern (50K Token Budget, Claude Opus 4.7)

```python
"""
Agent Context Loading для Claude Opus 4.7 с 1M context window.
Целевой budget: 50K токенов для типичной task-сессии.
Компонент auto-compact: срабатывает при ~75% (~150K), буфер ~50K.
"""

CONTEXT_BUDGET = {
    "core_identity": 2_000,      # agents/{id}/system.md (role-manifest)
    "strategies": 1_500,          # agents/{id}/strategies.md
    "task_context": 5_000,         # Текущий task + alpha state (если релевантен)
    "retrieved_wiki": 20_000,      # HippoRAG top-20 nodes
    "alpha_data": 5_000,           # Relevant alpha state.yaml + context.md
    "recent_decisions": 3_000,     # decisions/ за последние 30 дней
    "mailbox": 2_000,              # comms/mailboxes/{id}.jsonl (последние N)
    "scratch": 8_000,              # Рабочее пространство агента
    "overhead": 3_500,             # System prompt, tool schemas, etc.
    # TOTAL: ~50,000 tokens
}

async def load_agent_context(
    agent_id: str,
    task: Task,
    wiki: KnowledgeGraph
) -> AgentContext:
    """
    Порядок загрузки контекста (от критичного к опциональному).
    """
    context = AgentContext()
    
    # LAYER 1: Core identity (всегда, 2K) — CLAUDE.md equivalent
    context.add(read_file(f"agents/{agent_id}/system.md"), priority=1)
    
    # LAYER 2: Meta-cognitive strategies (всегда, 1.5K)
    context.add(read_file(f"agents/{agent_id}/strategies.md"), priority=2)
    
    # LAYER 3: Task + Alpha context (если задача связана с alpha)
    if task.alpha_ref:
        alpha_state = load_yaml(f"alphas/{task.alpha_type}/{task.alpha_id}/state.yaml")
        alpha_context = read_file(f"alphas/{task.alpha_type}/{task.alpha_id}/context.md")
        context.add(alpha_state, priority=3, budget=2_000)
        context.add(alpha_context, priority=3, budget=3_000)
    
    # LAYER 4: Wiki retrieval через HippoRAG (20K budget)
    wiki_nodes = await hipporag_retrieve(
        query=task.description,
        graph=wiki.graph,
        top_k=20,
        alpha_filter=task.alpha_type  # alpha-aware filtering
    )
    context.add(wiki_nodes, priority=4, budget=20_000)
    
    # LAYER 5: Recent decisions relevant to task domain (3K)
    relevant_decisions = grep_decisions(
        domain=task.domain,
        days=30,
        budget=3_000
    )
    context.add(relevant_decisions, priority=5)
    
    # LAYER 6: Mailbox (последние сообщения агенту, 2K)
    messages = load_jsonl(
        f"comms/mailboxes/{agent_id}.jsonl",
        last_n=10,
        budget=2_000
    )
    context.add(messages, priority=6)
    
    # LAYER 7: Если контекст не заполнен — scratchpad
    if context.remaining_budget > 5_000:
        context.add(read_file(f"agents/{agent_id}/scratchpad.md"), priority=7)
    
    return context.build()
```

**Правило приоритетов:** при сжатии (auto-compact) — срезается от Layer 7 к Layer 4. Layers 1-3 всегда остаются. Layer 4 (wiki) сжимается до top-5 nodes.

### H.4 Writeback Rules

| Trigger | Что записать | Куда | Формат |
|---------|-------------|------|--------|
| `/ask` возвращает comparison | Comparison page | `wiki/comparisons/{slug}.md` | Markdown wiki page |
| Alpha state изменился | State transition + timestamp | `alphas/{type}/{id}/history.jsonl` | `{"event":"state_change","from":"proposal_sent","to":"won","ts":"..."}` |
| Агент обнаружил новый паттерн | Новый claim | `wiki/claims/{slug}.md` | Claim page с frontmatter |
| /ingest нового источника | Source summary + entity pages | `wiki/sources/`, `wiki/entities/` | Полный wiki ingestion |
| Decision принято | ADR запись | `decisions/{date}-{slug}.md` | ADR template |
| Эксперимент завершён | Postmortem | `wiki/experiments/{slug}.md` | Postmortem template |
| Агент узнал стратегию | Стратегия | `agents/{id}/strategies.md` | Append strategy block |
| Новый инсайт из клиент-сессии | Alpha context update | `alphas/clients/{id}/context.md` | Append section |
| /consolidate выявил pattern | Pattern page | `wiki/topics/{slug}.md` | Topic synthesis |
| Claim опровергнут | Обновить claim status | `wiki/claims/{slug}.md` | `status: refuted` + evidence |

### H.5 Retrieval Integration: HippoRAG + Fallbacks

```yaml
# Retrieval strategy для /ask в Jetix
retrieval_pipeline:
  primary:
    method: hipporag_ppr
    index: wiki/graph/edges.jsonl
    top_k: 20
    alpha_aware: true          # фильтрация по alpha context
    
  hyde_enhancement:
    enabled: true              # HyDE для улучшения keyword extraction
    llm_calls: 1               # +1 LLM call, стоит для complex queries
    
  fallback_1:
    trigger: ppr_score_all_below_threshold  # Если все PPR scores < 0.01
    method: bm25_keyword
    index: wiki/ (full text)
    
  fallback_2:
    trigger: total_retrieved_tokens_below_5000  # Мало контента найдено
    method: long_context_full_load
    scope: wiki/niches/{agent_niche}/  # Только нища агента, не вся вики
    
  alpha_direct_lookup:
    trigger: query_contains_alpha_id  # "deal-042", "client:acme"
    method: direct_path_lookup
    priority: highest             # Перед wiki retrieval
```

### H.6 Memory Tier Recommendation

| Tier | Содержимое | Storage | Latency | Persistence |
|------|-----------|---------|---------|-------------|
| **T0: In-context** | Активный task, инструкции, retrieved docs | RAM (context window) | 0ms | Сессия |
| **T1: Hot** | agents/{id}/system.md, strategies.md, alpha state.yaml | Local disk, всегда читается | <10ms | Постоянная, git |
| **T2: Warm** | wiki/ (HippoRAG indexed), alpha context.md | Local disk + PPR index | 100-500ms | Постоянная, git |
| **T3: Cold** | history.jsonl, archived pages, decisions/ | Local disk | 500ms-2s (grep) | Постоянная, git |
| **T4: Archive** | _archive/, old experiments | Git history | Секунды | Immutable |

**Рекомендация:** Текущая архитектура Jetix (git + markdown + HippoRAG) полностью покрывает T0-T3 без дополнительной инфраструктуры. Добавление vector DB (T2 enhancement) рекомендуется при >3,000 страниц или при необходимости cross-lingual semantic search.

### H.7 Migration Path: Week 1-4

**Week 1: Alpha Layer Creation**
1. Создать `jetix/alphas/` folder tree (6 типов с state machines)
2. Мигрировать existing client/project/deal data из wiki entities в `alphas/`
3. Создать `wiki/entities/` как читаемые refs (добавить `alpha-ref` edge type)
4. Добавить alpha state validation в CI (`/lint` проверяет что каждый alias имеет state.yaml)

**Week 2: Role-Manifest ↔ Wiki Integration**
1. Обновить `agents/{id}/system.md` для включения `context_requirements` по R3 role-manifest
2. Добавить alpha_filter в HippoRAG `/ask` (по alpha_type из system.md)
3. Создать agent context loading script (H.3 псевдо-код → Python)
4. Тест: каждый агент получает правильный контекст для своей роли

**Week 3: Writeback Automation**
1. Implement writeback rules (H.4 таблица) как explicit triggers в agent skills
2. Создать `decisions/` folder + ADR template
3. Настроить `/consolidate` по расписанию (weekly cron)
4. Валидация: 5 writebacks через /ask → проверить что comparisons/ обновляется

**Week 4: Validation & Scale Preparation**
1. /lint прогон по всей вики — найти orphans, stale claims, missing alpha-refs
2. Benchmark HippoRAG PPR latency на текущем графе (572 edges)
3. Создать scale-up runbook (H.8 triggers)
4. FPAR baseline measurement: процент /ask ответов без follow-up

### H.8 Scale-Up Triggers

**1,000 страниц:**
- `/lint` переводится в daily (с weekly)
- Добавить BM25 как secondary retrieval (fallback tier)
- Мониторинг PPR latency (threshold: >2 секунды → оптимизация)
- Начать namespace sharding в wiki/entities/ по alpha types

**5,000 страниц:**
- Рассмотреть GraphRAG community detection для cross-domain queries
- Внедрить LightRAG для dual-level retrieval (low/high)
- PR workflow для wiki изменений (если >1 human contributor)
- Vector DB (Qdrant или Chroma) для semantic fallback retrieval

**10,000+ страниц:**
- Persistent graph store (проверить HippoRAG на данном масштабе; если latency >5s → Neo4j)
- Full hybrid search (BM25 + dense + PPR + RRF)
- Dedicated search infrastructure (отдельный сервис, не in-agent)
- Archive strategy: страницы >2 лет без обновления → `_archive/`

### H.9 Jetix-Specific Anti-Patterns

1. **Alpha-in-scratchpad**: хранение alpha state в `agents/{id}/scratchpad.md`. Scratchpad — ephemeral. State должен жить в `alphas/`. *Симптом: агент "забыл" состояние клиента после сессии.*

2. **Wiki как CRM**: использование `wiki/entities/clients/` для operational state. Wiki — semantic layer, не operational database. *Симптом: agent пытается обновить "current_deal_stage" в markdown файле через /ingest.*

3. **Over-eager writeback**: каждый /ask ответ файлится в comparisons/. Вики загрязняется низкокачественным контентом. *Решение: novelty threshold + agent decision о write.*

4. **Monolithic system.md**: role-manifest агента превышает 5K токенов. Нарушает принцип "shorter files get followed more reliably". *Решение: core identity <2K, детали → strategies.md.*

5. **GraphRAG для 557 страниц**: переинжиниринг с community detection при текущем масштабе. PPR уже делает лучше дешевле. *Триггер для GraphRAG: global sensemaking queries ("какие наши основные паттерны провала сделок").*

6. **Vector DB для <3,000 страниц**: дополнительная инфраструктура без выигрыша. HippoRAG PPR outperforms dense retrieval на multi-hop без embeddings. *Исключение: cross-lingual queries (немецкий Mittelstand → мультиязычный semantic search).*

7. **Игнор Alpha history**: изменение state.yaml без записи в history.jsonl. Теряется audit trail и обучение. *Правило: каждое изменение state.yaml → событие в history.jsonl.*

8. **Role-manifest без alpha context**: агент не знает с какими alphas он работает. R3 role-manifest требует явного `context_requirements` — список alpha types и wiki niches. *Симптом: sales-агент читает wiki/concepts/tech/ вместо wiki/business/.*

9. **Симметричное хранение Research Note и Postmortem в alphas/**: оба — wiki-primary по природе. Их ценность — в связях с концептами, не в state машине. Создание `alphas/research/` — anti-pattern.

10. **Context rot без compaction**: длинные сессии без /compact накапливают устаревший контекст. При ~75% использования (150K токенов в 200K окне) Opus автоматически компактирует — но CLAUDE.md и system.md пересчитываются. *Правило: ключевые инсайты сессии → writeback в strategies.md или wiki ПЕРЕД ожидаемой компакцией.*

---

## Заключение и Summary

Jetix уже работает на одной из наиболее продвинутых knowledge architectures для AI-native компании: HippoRAG PPR, Karpathy LLM Wiki pattern, per-agent 5-layer memory, Skills Pipeline v2. Wave 2 задача — интеграция с role-framework (R3) через explicit Alpha Layer.

**Три главных вывода:**

1. **Alpha Layer — критический missing piece.** Отсутствие `alphas/` как отдельного слоя создаёт смешение semantic knowledge (wiki) и operational state (что должно жить структурированно). Hybrid C паттерн решает это для 7 из 10 alphas.

2. **Context loading — первоклассный engineering.** При 50K token budget для типичной сессии порядок загрузки (system.md → strategies.md → alpha state → HippoRAG wiki → decisions → mailbox) должен быть детерминирован и explicit. Антропик определяет это как "#1 job of engineers building AI agents".

3. **Knowledge Compounding через Writeback Loop.** Insight loop (episodic → claims → patterns → summaries → foundations) замыкается только при автоматическом writeback. Без него wiki стагнирует вместо compounding. /ask + novelty threshold + `/consolidate` weekly — минимальный working set.

**Масштабный вывод:** git + markdown + HippoRAG достаточен до ~10,000 страниц. GraphRAG и vector DB — не сейчас, но runbook готов.

---

## Источники

- [HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs (NeurIPS 2024)](https://arxiv.org/abs/2405.14831) — Gutiérrez et al.
- [HippoRAG 2 (ICML 2025)](https://icml.cc/virtual/2025/poster/45585) — Non-Parametric Continual Learning
- [GraphRAG: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — Edge et al., Microsoft Research
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — Packer et al.
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) — Chhikara et al.
- [Self-RAG: Self-Reflective Retrieval Augmented Generation (NeurIPS 2023)](https://arxiv.org/pdf/2310.11511) — Asai et al.
- [LLM Wiki — Andrej Karpathy GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory) — Anthropic, 2026
- [Claude Code Experimental Memory System](https://giuseppegurgone.com/claude-memory) — Giuseppe Gurgone
- [Context Engineering for Agents — LangChain](https://www.langchain.com/blog/context-engineering-for-agents)
- [LightRAG: Graph-Based Knowledge Retrieval](https://lightrag.github.io)
- [Agentic RAG Survey (arxiv 2501.09136)](https://arxiv.org/abs/2501.09136)
- [HyDE: Hypothetical Document Embeddings](https://zilliz.com/learn/improve-rag-and-information-retrieval-with-hyde-hypothetical-document-embeddings)
- [Tulving: Episodic and Semantic Memory (1972, 1983)](http://donaldclarkplanb.blogspot.com/2020/02/tulving-episodic-semantic-memory.html) — Endel Tulving
- [Luhmann's Original Zettelkasten](https://www.ernestchiang.com/en/posts/2025/niklas-luhmann-original-zettelkasten-method/)
- [Introduction to the Zettelkasten Method](https://zettelkasten.de/introduction/) — Tietze & Fast
- [Diátaxis Documentation Framework](https://diataxis.fr)
- [CRDTs: Conflict-free Replicated Data Types](https://crdt.tech)
- [Hybrid Search: BM25 + Dense + RRF](https://dev.to/qvfagundes/dense-vs-sparse-retrieval-mastering-faiss-bm25-and-hybrid-search-4kb1)
- [MA-RAG: Multi-Agent RAG Framework (arxiv 2505.20096)](https://arxiv.org/html/2505.20096v2)
- [Claude Code Memory vs memsearch](https://milvus.io/blog/claude-code-memory-memsearch.md) — Milvus Blog
- [Tiago Forte: Building a Second Brain / CODE](https://www.buildingasecondbrain.com)
