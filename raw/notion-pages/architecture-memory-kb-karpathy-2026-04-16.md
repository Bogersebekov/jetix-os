---
type: raw-notion-page
notion_id: 3442496333bf819cb864cf0e04c9de74
source_url: https://www.notion.so/3442496333bf819cb864cf0e04c9de74
captured: 2026-04-16
title: "🏗️ Архитектура Jetix OS — Память + KB (Karpathy+)"
topics: [system-design]
pipeline: raw
---

# 🏗️ Архитектура Jetix OS — Память + KB (Karpathy+)

# Цель страницы
Скелет архитектуры памяти и KB для Jetix OS. Собрано из новейших наработок (апрель 2026). Работаем по этой странице — здесь решения, ссылки на первоисточники, открытые вопросы.
**Статус:** draft / в процессе обсуждения с Ruslan.
---
# Три уровня фреймворка
## Уровень 1: Karpathy LLM Wiki (скелет)
**Идея:** вместо RAG — `raw/` источники + LLM-компилятор + `wiki/` маркдаун-артефакт, который компаундит знание.
**Три операции:** `ingest` (добавить источник → обновить 10-15 страниц + index + log), `query` (найти → синтезировать → **опционально записать ответ назад в wiki**), `lint` (противоречия, orphan-страницы, пробелы, устаревшие claims).
**Два служебных файла:** `index.md` (каталог с одно-строчными summary) и `log.md` (append-only хронология).
**Почему это лучше RAG:** RAG пере-открывает знание каждый раз. Wiki — persistent, compounding artifact.
## Уровень 2: GraphRAG + HippoRAG (верхний слой поверх wiki)
**GraphRAG (Microsoft):** из wiki-страниц извлекаем entities + relationships → knowledge graph → hierarchical clustering (Leiden) → community summaries на разных уровнях абстракции. Дороже обычного RAG на 10-100x при индексации, но радикально лучше answer quality на "global" вопросах (что связано с чем, какие тренды во всём корпусе).
**HippoRAG (NeurIPS'24):** схемелесс KG + Personalized PageRank. +20% на multi-hop QA, 10-20x дешевле iterative retrieval. Вдохновлено гиппокампом: LLM = неокортекс, KG = hippocampal index.
**Как встроить:** поверх Karpathy wiki добавляем `wiki/graph/edges.jsonl` + entity pages с обратными ссылками. Skill `/build-graph` периодически перестраивает граф из wiki. Query может использовать либо прямой поиск по [index.md](http://index.md) (дёшево), либо PageRank по графу (для сложных multi-hop запросов).
## Уровень 3: Agent Memory (Mem0 / Letta / Zep как inspiration)
**Letta (ex-MemGPT):** OS-inspired три уровня памяти. Core memory = в контексте постоянно (RAM). Archival = external vector store (disk). Recall = история взаимодействий. Мапится прямо на агентов Jetix.
**Mem0:** hybrid store (vector + graph + KV), three-tier scope (user/session/agent). 47K stars, prod-ready.
**Zep:** temporal knowledge graph с fact validity windows. Для Jetix критично для решений типа "что было актуально в марте, что сейчас".
**Вывод:** не тащим фреймворк целиком, берём модель — каждый агент имеет Core (в system prompt), Working (scratchpad текущей задачи), Archival (своя ниша в общей KB), Recall (JSONL mailbox + conversation logs).
---
# Архитектура Jetix KB — предложение
```javascript
jetix-os/
├── CLAUDE.md                    # Schema (правила системы — уже есть)
├── raw/                         # Immutable источники (только человек кладёт)
│   ├── articles/
│   ├── transcripts/            # voice-notes через whisper
│   ├── meetings/
│   ├── books/
│   └── web/
│
├── wiki/                        # LLM-maintained knowledge base
│   ├── index.md                 # Глобальный каталог (NEW)
│   ├── log.md                   # Append-only хронология (NEW)
│   ├── overview.md              # Верхнеуровневый синтез
│   │
│   ├── personal/                # Личная ниша Ruslan
│   │   ├── goals.md
│   │   ├── beliefs.md
│   │   ├── people.md            # Антон, Владислав, Родион
│   │   └── decisions.md
│   │
│   ├── business/                # Бизнес-ниша
│   │   ├── icp.md
│   │   ├── offers.md
│   │   ├── pricing.md
│   │   └── case-studies.md
│   │
│   ├── tech/                    # Техническая ниша
│   │   ├── ai-tools.md
│   │   ├── agents.md
│   │   └── patterns.md
│   │
│   ├── concepts/                # Общие концепты (cross-nich)
│   ├── entities/                # Люди, компании, инструменты
│   ├── sources/                 # Source summaries
│   ├── claims/                  # Testable assertions с evidence
│   ├── comparisons/             # Query-выводы (filing loop)
│   │
│   └── graph/                   # GraphRAG/HippoRAG слой
│       ├── edges.jsonl          # Typed relationships
│       ├── communities.md       # Leiden clustering выходы
│       └── summaries.md         # Community summaries
│
├── agents/                      # Per-agent memory
│   ├── manager/
│   │   ├── system.md           # System prompt (Core memory)
│   │   ├── strategies.md       # System prompt learning
│   │   ├── scratchpad.md       # Working memory текущей сессии
│   │   └── niche/              # Symlinks в wiki/ — срез KB агента
│   ├── sales-lead/
│   ├── life-coach/
│   └── ...
│
├── comms/mailboxes/            # Inter-agent messages (уже есть)
└── shared/state/               # Оперативное состояние (уже есть)
```
---
# Маппинг текущий pipeline → новая модель
<table header-row="true">
<tr>
<td>Было</td>
<td>Станет</td>
<td>Комментарий</td>
</tr>
<tr>
<td>`raw` → `ingested`</td>
<td>`raw/`</td>
<td>Слияние. LLM всегда читает из raw, сам решает что в wiki.</td>
</tr>
<tr>
<td>`ingested` → `compiled`</td>
<td>`wiki/sources/` (summary) + `wiki/concepts/` (обновлённые)</td>
<td>Компиляция происходит при ingest, без промежуточной папки.</td>
</tr>
<tr>
<td>`compiled` → `linted` → `ready`</td>
<td>`wiki/` (всё ready по умолчанию) + `/lint` skill</td>
<td>Lint периодический, не блокирующий.</td>
</tr>
<tr>
<td>Нет глобального index</td>
<td>`wiki/index.md`</td>
<td>NEW</td>
</tr>
<tr>
<td>Логи по проектам</td>
<td>`wiki/log.md` глобальный + проектные остаются</td>
<td>NEW для KB</td>
</tr>
<tr>
<td>Нет query writeback</td>
<td>`wiki/comparisons/` куда `/query` может складывать ответы</td>
<td>NEW</td>
</tr>
<tr>
<td>Нет entity extraction</td>
<td>`wiki/entities/`  • `wiki/graph/edges.jsonl`</td>
<td>NEW (GraphRAG-style)</td>
</tr>
</table>
---
# Операции (Skills) — обновлённые
<table header-row="true">
<tr>
<td>Skill</td>
<td>Что делает</td>
<td>Статус</td>
</tr>
<tr>
<td>`/ingest <source>`</td>
<td>raw → wiki (summary + revise 10-15 pages + index + log + entity update)</td>
<td>обновить существующий</td>
</tr>
<tr>
<td>`/ask <question>`</td>
<td>search wiki → synthesize → опциональная запись в wiki/comparisons/</td>
<td>**NEW**</td>
</tr>
<tr>
<td>`/search-kb <query>`</td>
<td>быстрый grep-поиск (legacy, для простых случаев)</td>
<td>оставить</td>
</tr>
<tr>
<td>`/lint`</td>
<td>health check wiki (contradictions, orphans, stale claims)</td>
<td>**NEW**</td>
</tr>
<tr>
<td>`/build-graph`</td>
<td>извлекает entities + edges из wiki → graph/</td>
<td>**NEW**</td>
</tr>
<tr>
<td>`/consolidate`</td>
<td>merge duplicates, prune index</td>
<td>**NEW** (inspired by Anthropic consolidate-memory skill)</td>
</tr>
<tr>
<td>`/plan-day`, `/close-day`</td>
<td>daily operations</td>
<td>оставить</td>
</tr>
</table>
---
# Память агентов — модель
Для каждого из 12 агентов:
<table header-row="true">
<tr>
<td>Слой</td>
<td>Где хранится</td>
<td>Что содержит</td>
<td>Аналогия (Letta)</td>
</tr>
<tr>
<td>**Core**</td>
<td>`agents/{agent}/system.md`</td>
<td>System prompt, роль, ключевые принципы</td>
<td>RAM (always in-context)</td>
</tr>
<tr>
<td>**Strategies**</td>
<td>`agents/{agent}/strategies.md`</td>
<td>"Когда X, делай Y" — накопленный опыт</td>
<td>System prompt learning</td>
</tr>
<tr>
<td>**Working**</td>
<td>`agents/{agent}/scratchpad.md`</td>
<td>Текущая задача, промежуточные результаты</td>
<td>Short-term</td>
</tr>
<tr>
<td>**Archival**</td>
<td>`wiki/` с агентским срезом через `agents/{agent}/niche/`</td>
<td>Вся KB по домену агента</td>
<td>Disk (external searchable)</td>
</tr>
<tr>
<td>**Recall**</td>
<td>`comms/mailboxes/{agent}.jsonl`</td>
<td>Conversation history</td>
<td>Recall memory</td>
</tr>
</table>
**Ключевая идея:** агент НЕ имеет собственной изолированной KB. У него есть свой **срез** общей KB (symlinks в `wiki/` + фильтр в [CLAUDE.md](http://CLAUDE.md) по тегам/папкам). Это даёт compounding: то что узнал sales-lead — доступно и life-coach через общий entity `person/Ruslan`.
**System Prompt Learning (Karpathy):** каждый агент ведёт `strategies.md` — когда встретил проблему и нашёл решение, добавляет "it seems when I encounter X, I should try Y". Читается в начале каждой сессии.
---
# Context Engineering — 4 стратегии для агентов
<table header-row="true">
<tr>
<td>Стратегия</td>
<td>Реализация в Jetix</td>
</tr>
<tr>
<td>**Write**</td>
<td>[MEMORY.md](http://MEMORY.md) у Claude Code + agents/\{x\}/[strategies.md](http://strategies.md)  • wiki/comparisons/</td>
</tr>
<tr>
<td>**Select**</td>
<td>[CLAUDE.md](http://CLAUDE.md) с инструкцией читать [index.md](http://index.md) → relevant wiki pages → niche symlinks</td>
</tr>
<tr>
<td>**Compress**</td>
<td>`/consolidate` skill + auto-compact от Claude Code + summary pages</td>
</tr>
<tr>
<td>**Isolate**</td>
<td>Per-agent context (symlinks), sub-agent spawning для тяжёлых задач</td>
</tr>
</table>
**Failure modes которых избегаем:** Context Poisoning (галлюцинации закрепились в wiki) — защита через `/lint` + confidence в frontmatter. Context Distraction (много нерелевантного) — niche-фильтры для агентов. Context Clash (конфликты) — `/lint` ищет противоречия.
---
# Ссылки на первоисточники
## Karpathy (основа)
- [LLM Wiki gist (апрель 2026)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — главная работа
- [Context engineering твит](https://x.com/karpathy/status/1937902205765607626)
- [System prompt learning твит](https://x.com/karpathy/status/1921368644069765486)
- [2025 Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/)
- [Software 3.0 YC keynote](http://ikyle.me/blog/2025/andrej-karpathy-software-is-changing-again)
- [nanochat репо](https://github.com/karpathy/nanochat)
## GraphRAG / HippoRAG
- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) · [репо](https://github.com/microsoft/graphrag)
- [HippoRAG репо (NeurIPS'24)](https://github.com/OSU-NLP-Group/HippoRAG) · [arxiv](https://arxiv.org/abs/2405.14831)
- [KARMA — multi-agent KG enrichment](https://arxiv.org/html/2502.06472v1)
## Memory frameworks 2026
- [Mem0 (top choice general-purpose)](https://github.com/mem0ai/mem0)
- [Letta (ex-MemGPT, OS-inspired)](https://forum.letta.com/t/agent-memory-letta-vs-mem0-vs-zep-vs-cognee/88)
- [Zep (temporal KG)](https://atlan.com/know/best-ai-agent-memory-frameworks-2026/)
- [Сравнение 2026](https://dev.to/varun_pratapbhardwaj_b13/5-ai-agent-memory-systems-compared-mem0-zep-letta-supermemory-superlocalmemory-2026-benchmark-59p3)
## Прецеденты реализации Karpathy-паттерна
- [OmegaWiki](https://github.com/skyllwt/OmegaWiki) — 23 skills, 9 entity types, 9 edge types. **Самый полный прецедент**
- [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) — как Agent Skill
- [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)
- [LLM Wiki v2 gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2)
- [AgentWiki](https://agentwiki.org/)
---
# Открытые вопросы (TODO с Ruslan)
- [ ] Добавляем ли GraphRAG/HippoRAG сразу или MVP на чистом Karpathy-wiki + потом upgrade?
- [ ] Formal entity types (9 как у OmegaWiki) — переборщик или must-have?
- [ ] Как мигрировать существующий knowledge-base/ и raw/ voice-notes в новую структуру без потери данных?
- [ ] `/ask` skill — с каким LLM (Opus для синтеза или Sonnet для скорости)?
- [ ] Per-agent niche через symlinks vs через [CLAUDE.md](http://CLAUDE.md)-filter — какой подход?
- [ ] Интеграция с Obsidian — да/нет? Karpathy рекомендует, но Jetix работает через Claude Code напрямую.
- [ ] Daily cron `/ingest` новых voice-notes (по аналогии с OmegaWiki daily arxiv)?
---
# Следующие шаги (пошагово)
1. **Сейчас:** обсудить и утвердить скелет выше
2. **Phase 1:** миграция — переименование папок, создание [index.md](http://index.md) + [log.md](http://log.md) + базовой структуры wiki/
3. **Phase 2:** skills `/ingest`, `/ask`, `/lint`, `/consolidate`
4. **Phase 3:** per-agent memory (Core / Strategies / Working / Archival)
5. **Phase 4:** GraphRAG/HippoRAG слой — опционально если MVP работает
6. **Phase 5:** возврат к дашборду — visualize все слои (index, log, graph, agent niches)
---
*Создано: 2026-04-16. Обновляется по ходу работы.*
