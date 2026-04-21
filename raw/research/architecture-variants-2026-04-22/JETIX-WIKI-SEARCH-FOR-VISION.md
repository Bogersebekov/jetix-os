---
id: jetix-wiki-search-vision
title: Jetix Wiki Knowledge Extraction для Vision (Universal OS)
date: 2026-04-21
based-on:
  - Ruslan Vision 2026-04-21 evening (3-layer / universality / OS-for-thinking / separable / post-€200K open source)
  - Locked decisions (separable jetix-os+jetix-company / post-€200K open source / universality metrics added в SYNTHESIS-GOAL.md)
  - Open Questions 1-10 (см. prompts/jetix-wiki-search-for-vision-2026-04-21.md)
purpose: Provide complete picture "что у нас уже есть в knowledge base relevant к Vision" перед SYNTHESIS-GOAL.md writing
state: draft (input для Cloud Cowork + Ruslan review)
formality: F2
reliability: R-medium (primary-source citations; critical lens applied)
claim-scope: jetix/vision/knowledge-extraction
---

# Jetix Wiki Search для Vision — Knowledge Extraction for Goal Definition

---

## Executive Summary

**Headline verdict:** Wiki knowledge base **даёт полный vocabulary для Vision Layer 1 (Memory/Learning) и частичный vocabulary для Layer 3 (Agents/Acceleration)**, но **Layer 2 (Management/Projects) описан только fragmentarily в wiki/ideas/** — операционализация сидит глубже, в `design/JETIX-FPF.md` (3758 строк) и `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (1880 строк). Критичный gap против Vision: **"universality criterion" не представлен ни одним словом** в текущих ~500 wiki-страницах (`универсал` / `portable` / `plugin` / `overlay` / `base-vs-overlay` дают 0 matches в wiki/ и decisions/). Все design/decisions документы написаны в предположении **single use-case = DACH Mittelstand AI-consulting**: 210 mentions "Jetix|DACH|consulting|Mittelstand" в D6; 133 в JETIX-ARCHITECTURE-WORKING.md; 89 в ADR; 69 в D9. Separation jetix-os base / jetix-company overlay — **требует нового слоя документации, которого нет**.

**Surprises (5):** (1) `wiki/foundations/` / `wiki/summaries/` / `wiki/experiments/` / `wiki/comparisons/` **пустые** — все foundations, на которые ссылаются D6 (jetix-uts.md / shsm-primitives.md / holon-hierarchy.md / jetix-creation-graph.md) — **ещё не написаны** (Phase 1 Day 5-17 ETA per D9 §5.4). (2) **Все niches/* содержат только README.md** — per-agent niche symlinks упомянуты в CLAUDE.md но не заполнены. (3) **198 из 257 wiki/ideas файлов — "content preview only"** (500-char summary from Notion, full fetch deferred γ-phase per wiki/log.md). Качественный базис идей **тонкий по depth**, широкий по breadth. (4) **Synthesis v2 (commit 015e274, сегодня)** уже делает strategic recommendations **ортогональные к Vision** — adopt Skills, adopt Promptfoo+Langfuse, adopt 4-layer termination stack — ни одна из них не учитывает "universality" measure; они упаковывают Jetix глубже, не шире. (5) **Karpathy LLM Wiki pattern уже implement'ed** (см. wiki/overview.md:7 "по модели Karpathy LLM Wiki + OmegaWiki") + `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md` **уже описывает 3-layer memory architecture** (Karpathy LLM Wiki + GraphRAG/HippoRAG + Letta/Mem0/Zep) с прямыми source-links — но этот знаниевый артефакт **сидит в source-card form, не в active design doc**.

**Gaps (5):** (1) **Universality specification отсутствует** — нет ни definition, ни test framework, ни examples use cases B/C (астроном / животновод). (2) **Separable overlay architecture отсутствует** — D9 §5.1 говорит про 15 folders **внутри** `~/jetix-os/jetix/` (не base/overlay split); всё company-specific вложено inline. (3) **Base-layer primitives не вычленены** — FPF holonic foundation A.1, alphas, creation-graph могут быть universal, но нигде explicitly так не помечены. (4) **Open source governance plan отсутствует** — D9 §2.2 hard-codes "internal-only" (per OT5 + OQ-09 A) и "no contribute-back"; post-€200K timeline не материализован ни одним artifact. (5) **Onboarding curve для другого user (use case B/C) не описан** — 3-12 month ramp-up требование Vision нигде.

**Contradictions (3, top):** (1) **Hard Rule D9 §2.2 "internal-only hard stance, publish nowhere"** vs **Vision "open source post-€200K + Phase 2+ self-improving через forking/GitHub/community"** — resolved только temporally (now-internal, later-open), но архитектурный seam для этого не заложен. (2) **D6 §2.2 11-agent specialized roster** (sales-lead, sales-research, sales-outreach, sales-closer, acceptance-authority) vs **Vision universality demanding role replaceability for astronomer/animal-husbandry use cases** — роли хард-коданы под consulting. (3) **D9 P6 "DACH primary + US + RU secondary, unified funnel через Stripe"** (сквозной Jetix-specific) vs **Vision "base methodology + starter code на которые можно натянуть вообще всё"** — ни одна строка P6 не переносится.

**Verdict on wiki readiness:** **wiki/knowledge base ~40% ready** для Vision (vocabulary для Layer 1 is strong; Layer 2 operationalization находится в design/ and decisions/ НЕ в wiki/; Layer 3 partial coverage). **Design/decisions documents ~30% ready** — глубоко для Jetix-company layer; поверхностно для base-layer abstraction. **Separation/universality specification needs to be written fresh** в SYNTHESIS-GOAL.md; wiki может служить источником примеров, но не готовых шаблонов. Recommend Ruslan + Cloud Cowork treat wiki/ как inspiration reservoir, design/JETIX-FPF.md как ontology reservoir, а **SYNTHESIS-GOAL.md writing как greenfield specification task** (3-layer architecture + universality test + separability contract — ни одно из трёх не существует в текущих artifacts).

---

## Part 1 — Per-layer mapping (что есть в wiki для каждого слоя)

### 1.1 Layer 1: Ментальный / Когнитивный (Память + Обучение)

**Existing mechanisms (с citations):**

- **Wiki/ с 9 entity types** (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations) — структура из `wiki/overview.md:9-27` и `CLAUDE.md:69-89`. **Реальное наполнение** (counted 2026-04-21): `concepts/` 8 файлов, `entities/` 4, `sources/` 271, `ideas/` 257, `claims/` 5, `topics/` 1, `comparisons/` 0, `summaries/` 0, `experiments/` 0, `foundations/` 0. **Первые три entity types (foundations/summaries/comparisons) пустые** — критический gap, поскольку все design/decisions ссылаются на `wiki/foundations/jetix-uts.md`, `wiki/foundations/jetix-creation-graph.md`, `wiki/foundations/shsm-primitives.md`, `wiki/foundations/holon-hierarchy.md` как на authoritative artifacts (см. D6 §1.8, §3.7, §5.4a и др.).
- **Per-agent 5-layer memory** (Core / Strategies / Working / Archival / Recall) — описано в `CLAUDE.md:82-86` + `wiki/sources/2026-04-16-architecture-memory-kb-karpathy.md` + (originals) `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:179-218`. Маппинг на Letta primitives (Core=RAM, Archival=Disk, Recall=Recall). **Реальный статус:** только manager/strategies.md, sales-lead, strategist, crazy-agent, system-admin, life-coach имеют active traffic per `ARCHITECTURE-CURRENT.md:52`.
- **Voice-notes pipeline** — tools/transcribe.py → extract.py → filter.py → review_report.py, описан в `CLAUDE.md:119-128`. **Сознательная STOP-точка перед KB ingestion** — `tools/distribute.py.bak` архивирован чтобы не загрязнять wiki без human review (`CLAUDE.md:132-135`). Это реальный cognitive compounding mechanism Ruslan'а.
- **Karpathy LLM Wiki pattern** — `wiki/overview.md:7` "База знаний Jetix OS по модели Karpathy LLM Wiki + OmegaWiki knowledge graph"; `wiki/concepts/jetix-open-source-principles.md:32` "wiki-driven engineering у Karpathy"; `wiki/entities/claude-code.md:31` "модель пишет, человек направляет". Ingest → wiki → lint → compound loop formalized.
- **GraphRAG / HippoRAG references** — `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:22-26` описывает Microsoft GraphRAG (Leiden clustering, community summaries) + HippoRAG (NeurIPS'24, PageRank). Jetix implementation partial: `wiki/graph/edges.jsonl` (137 edges per `wiki/log.md:40`), `wiki/graph/communities.md`, `wiki/graph/summaries.md`.
- **4 Context Engineering стратегии** (Write / Select / Compress / Isolate) — `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:223-244`. Жёстко маппятся на Jetix artifacts.
- **"Second brain" / cognitive architecture idea cluster:**
  - `wiki/ideas/stek-instrumentov-dlya-vtorogo-mozga-2026.md:22-28` — "Heptabase + Obsidian + AI-поиск = мощнейшая система управления знаниями"
  - `wiki/ideas/vtoroy-mozg-kak-sistema-upravleniya-mnozhestvom-proekto.md:22-28` — "Система, которая хранит все проекты с метаданными (стадия, ресурсы, шаги)"
  - `wiki/ideas/kognitivnaya-arkhitektura-ot-umeniya-dumat-k-sisteme-my.md:22-28` — "Цикл facts→insights→hypotheses→decisions→results→rules, повторённый 20-30 раз, создаёт интеллект-систему"
  - `wiki/ideas/tsifrovoy-klon-myshleniya-cherez-zametki-ii.md:22-28` — "ИИ может обучиться на заметках и воспроизводить подход автора"
  - `wiki/ideas/perekhod-ot-ya-dumayu-k-sistema-dumaet-za-menya.md:22-28` — "следующий уровень — не умение думать, а создание системы, которая думает"

**Vision alignment (Layer 1):**
- ✅ Strong match: wiki/-as-memory Karpathy pattern **IS** the cognitive substrate Vision demands.
- ✅ Strong match: per-agent 5-layer memory maps cleanly к "agent accumulates learning".
- ✅ Strong match: "second brain" / "cognitive architecture" idea cluster **explicitly names** what Vision calls "Слой 1 Ментальный".
- ⚠️ Partial: voice-notes pipeline processes personal idea capture, но не "learning acceleration" в общем смысле.
- ❌ Missing: нет explicit training / learning curve mechanisms — Vision demands "ускоряет изучение, понимание, аналитику", в wiki только capture + storage.

**Universal vs Jetix-specific (Layer 1):**
- **Universal:** wiki structure 9-entity-type (inherited от OmegaWiki, не Jetix-originated); per-agent memory 5-layer (derived от Letta / Karpathy, не Jetix); voice-notes pipeline mechanics (Groq Whisper / Claude / markdown output — tool choice, не content); GraphRAG / HippoRAG references.
- **Jetix-specific:** `wiki/niches/{personal,business,sales,life,tech,meta}/` 6-niche naming (hardcoded по Jetix agent roster); actual page content 80%+ Jetix-brand-oriented; `topics/system-design-hub.md:21-199` — explicit "Jetix OS" hub.

**Gaps (Layer 1):**
- G1.1 `wiki/foundations/` полностью пустая — все D6-cited foundations artifacts не существуют. Phase 1 Day 5-17 backlog.
- G1.2 Нет "learning" mechanism — только memory. Vision требует "ускорить изучение, понимание" — нет spaced-repetition, active-recall, skill-tree, curriculum generator.
- G1.3 Analytics layer weak — `/ask` skill concepted в CLAUDE.md:172 but не operationalized в production.
- G1.4 Cross-user portability (Vision's use case B astronomer — его Sun/asteroid knowledge) — нет onboarding curve, нет import-from-other-KB tooling.

### 1.2 Layer 2: Управление / Проекты (Management + Deep Dive + Cross-Project Synergy)

**Existing mechanisms (с citations):**

- **8 True Alphas** (D6 §6 + D9 §5.2) — Client / Project / Deal / Content Item / Hypothesis / Member / Way of Working / Direction. Каждый с past-participle state machines + past-participle enforcement Hook 4. `decisions/2026-04-20-jetix-architecture-final-DRAFT.md:607-616` содержит полную state table. **Это самая сильная operationalization Layer 2 в текущей системе.**
- **Portfolio-of-Directions as 8th alpha** (D9 §P8, `decisions/2026-04-20-jetix-architecture-final-DRAFT.md:458-502`) — folder-per-direction `_active|_hypotheses|_archived/<slug>/`, per-direction `nqd-distinctions.yaml` + `ee-log.yaml` + `kill-chr.yaml`. **Cross-project synergy primitive** — по утверждению Ruslan quote :473: "Jetix как холдинг для кросс-функционального наблюдения за множественными business-ставками".
- **Creation Graph 3-level** (D6 §3, lines 723-895) — Target systems / Creation systems / Supersystems. Level 1 = 8 alphas + Product-SKU + Content Item; Level 2 = 5 Ruslan sub-роли + 11 agent roles + methodologies + processes; Level 3 = Jetix-Sales-Function + Jetix-Revenue-Engine + Jetix-Delivery-Function + Jetix-Ecosystem + external supersystems.
- **A.14 typed mereology edges** (D6 §3.5, lines 818-848) — ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf + 4 Jetix-introduced (creates / operates-in / methodologically-uses / constrained-by / fills).
- **Holonic foundation A.1** (D6 §1.1-1.7, lines 219-403) — U.Entity ⊃ U.Holon ⊃ U.System + U.Episteme. Jetix как holon; Life-OS как supersystem (D6 §1.6). Nested Holonic Structure (D6 §1.7).
- **Resource Accounting dual-tier** (D6 §12.6bis + D9 §P7 P7.1-P7.5 lines 416-456) — Tier 1 quantitative (Capital + Compute + Deep Hours) daily/monthly; Tier 2 strategic (Attention Budget) quarterly; Phase 3 Ecosystem Resources 11-category.
- **Decisions/ADR architecture** — `decisions/2026-04-19-architecture-v2-approval.md` (1995 lines, 8 chunks), `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (D9 v0.6, 1880 lines), `decisions/gap-analysis-review-decisions-2026-04-20.md` (509 lines). 60+ decisions locked.
- **Clients / CRM structure** — D9 §5.1 folder 4 `clients/` (companies, contacts, deals) Markdown CRM. References `jurisdiction: de|at|ch|us|ru|other` frontmatter (D6 §2.5 lines 680-691).
- **Rituals cadence** (D6 §7 + D9 §5.1 folder 7) — 4 rituals: weekly close / monthly P&L + OKR / quarterly strategy + letter / trigger-driven strategizing event.
- **Project-management idea cluster in wiki:**
  - `wiki/ideas/sistema-upravleniya-proektami-dashbordy-chit-kod.md:22-28` — "универсальный ускоритель: запуск бизнесов, тестирование гипотез, обучение, глубокий анализ, принятие решений"
  - `wiki/ideas/vtoroy-mozg-kak-sistema-upravleniya-mnozhestvom-proekto.md:22-28` — метаданные проектов + фильтрация идей + привязка
  - `wiki/ideas/personalnye-sistemy-upravleniya-kak-produkt-budushchego.md:22-28` — **"будущее за полностью персонализированными системами управления жизнью и бизнесом"** — ключевой alignment к Vision
  - `wiki/ideas/resursnoe-upravlenie-proektami-na-urovne-zhizni.md` (тизер в index)
- **4 Notion bizmodels references** — D9 §2.2 и `CLAUDE.md:57-59` referencing Notion external truth.

**Vision alignment (Layer 2):**
- ✅ Strong: 8 alphas = universal primitive для management, portable к астроному (Observation / Hypothesis / Experiment / ResearchNote / Paper — те же state-machine verbs).
- ✅ Strong: Portfolio-of-Directions **explicitly** — "holding для кросс-функционального наблюдения" = Vision's "cross-project synergies + перераспределение ресурсов".
- ✅ Strong: Creation Graph 3-level — universal decomposition modelling.
- ⚠️ Partial: ADR / decisions architecture — mechanism universal, но current content 100% Jetix-consulting-specific.
- ⚠️ Partial: rituals cadence — pattern universal, но описаны через Jetix-specific outputs (weekly close → client pipeline review).
- ❌ Missing: "deep dive в любой проект — stages, варианты развития" — Vision's Layer 2 middle bullet — нет template или framework в wiki. D6 §6 alphas дают state machines, но не "deep-dive template" (stages, scenario variants, risk analysis).

**Universal vs Jetix-specific (Layer 2):**
- **Universal:** 8-alpha pattern (generalizable, 6 из 8 — Client/Project/Deal/Hypothesis/Member/Way-of-Working — domain-agnostic in принципе, хотя content hardcoded); past-participle state discipline; Creation Graph 3-level abstraction; A.14 typed mereology; holonic A.1; Resource Accounting dual-tier abstraction; ADR / ritual cadence mechanics.
- **Jetix-specific:** Content Item alpha ($-marketing bound); Direction alpha (portfolio-of-businesses specific to Jetix holding model); 5 Ruslan sub-roles (strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations — consulting-bound; astronomer has no "sales-closer"); ai-consulting-dach direction entire substrate; DACH Mittelstand ICP; EU AI Act compliance matrix (D6 §4.5.1); Stripe payment flow; Freiberufler→UG→GmbH legal trajectory.

**Gaps (Layer 2):**
- G1.5 Нет Project "deep-dive template" — stages, scenarios, variant-tree. Vision requires "глубокий dive в любой проект".
- G1.6 Cross-project synergy operationalized только частично через `directions/` portfolio folder; нет formal "resource rebalancing" engine — Ruslan manually reassigns compute/hours per quarterly ritual.
- G1.7 Management "общая глубокая картина" — dashboard `dashboard/` folder exists per `ARCHITECTURE-CURRENT.md:86-89` но его status unclear, Layer 2 visualization не formalized.
- G1.8 Client / CRM structure currently only folder skeleton — D9 §5.1 folder 4 list структуру, но content Phase 1 Day 3+ ETA.

### 1.3 Layer 3: Ускорение / Автоматизация (Agents + Skills + Tools + MCP + Hooks)

**Existing mechanisms (с citations):**

- **11-agent hub-and-spoke** (D6 §2.2 lines 533-570; `CLAUDE.md:16-30`) — manager / personal-assistant / system-admin / sales-lead / sales-research / sales-outreach / inbox-processor / crazy-agent / knowledge-synth / strategy-support-analyst / meta-agent (+ FPF-Steward sub-role). Note: `CLAUDE.md:16` lists 12 agents including life-coach; per D6 Area 7 decision life-coach migrates к life-os/ (D9 §P5 and синтез `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md:1909-1910`).
- **Claude Code SDK usage** — `wiki/entities/claude-code.md:29-32` — "Пишет код dashboard, скриптов, агентских pipeline'ов. Поднимает Notion-данные в wiki через /ingest. Работает в режиме Karpathy."
- **Skills (current custom set)** — `CLAUDE.md:132-136`: `/plan-day`, `/close-day`, `/ingest`, `/compile`, `/search-kb`. Plus `/ask`, `/lint`, `/consolidate`, `/build-graph` per wiki/overview.md:31-35 + `ARCHITECTURE-CURRENT.md:48-49`.
- **Hooks** (D9 §P1 + §5.4 Day 2 lines 687-693) — 4 pre-commit hooks: asymmetric reference (Jetix→Life-OS blocked), Rechnungsnummer monotonicity, role-manifest required fields, past-participle state check. 5th auto-translation hook per OT2 addition. **No PostToolUse hooks currently** (identified gap in `SYNTHESIS-DEEP-CE-vs-JETIX.md:2068-2073`).
- **MCP** — used selectively; `CLAUDE.md` mentions `mcp__notion`, `mcp__miro` in agent tool list. No custom Jetix MCP server yet.
- **Voice-notes automation pipeline** — `CLAUDE.md:94-111`, tools/ Python scripts.
- **tools/ folder** — transcribe.py / extract.py / filter.py / review_report.py / summarize.py / sync_context.py per `ARCHITECTURE-CURRENT.md:75-80`.
- **Comms mailboxes JSONL** — `comms/mailboxes/<agent>.jsonl` + schema `shared/schemas/message.schema.json`; message types per D6 §2.2a.5 line 580-581: `task` / `result` / `question` / `escalation` / `notification` / `handoff`.
- **Agent-army / AI-army idea cluster:**
  - `wiki/ideas/armiya-ai-agentov-vokrug-odnoy-lichnosti.md:22-28` — "человек может достигать результатов, ранее доступных только большим командам"
  - `wiki/ideas/ai-stek-kak-polnotsennaya-armiya-i-zadacha-ey-upravlyat.md` (index listed)
  - `wiki/ideas/arkhitektura-kompanii-budushchego-profi-ai-armiya.md` (index listed)
  - `wiki/ideas/virtual-c-suite-expert-calibration.md:142` (line in index) — "эксперты + AI-роли"
  - `wiki/ideas/focus-theory-5-people-ai-1-task.md` — "5+AI+1"
  - `wiki/ideas/automate-research-via-crewai.md` — multi-agent pipeline

**Vision alignment (Layer 3):**
- ✅ Strong: 11-agent hub-and-spoke IS what Vision calls "агенты + automation — делать за неделю что было месяцем".
- ✅ Strong: Skills + hooks + MCP trio — EXACTLY Vision's enumeration "Skills, tools, MCP, hooks".
- ✅ Strong: Claude Code SDK as cognitive compounding substrate — universally portable (not Jetix-specific).
- ⚠️ Partial: "делать за неделю что было месяцем" productivity leap — claimed in wiki/ideas/* but не measured; Layer 3 depends on Layer 1/2 maturity.
- ❌ Missing: Universal skill registry Mode — current skills are bound to Jetix workflow; no "plugin marketplace" / "skill catalog for user to install per-use-case".
- ❌ Missing: Configuration / overlay mechanism — agents are hardcoded roles (sales-lead), nothing switches them into astronomer-roles (observation-lead) via configuration.

**Universal vs Jetix-specific (Layer 3):**
- **Universal:** Claude Code SDK, hooks primitive, MCP primitive, Skills primitive, subagents primitive, mailbox-based async communication schema (per message.schema.json), voice-notes pipeline mechanics (Groq Whisper / Claude extract), git-as-SoT pattern.
- **Jetix-specific:** agent roster (sales-*, inbox-processor — все роли bound к consulting workflow); 4 pre-commit hooks (Rechnungsnummer monotonicity — German invoice regulation; past-participle past-tense enforcement — FPF-specific); specific tools/ Python scripts bound к Jetix review format.

**Gaps (Layer 3):**
- G1.9 No native Skills migration yet (Compound Engineering synthesis v2 §G1 `SYNTHESIS-DEEP-CE-vs-JETIX.md:2058-2062`) — custom `/ingest` `/ask` `/lint` reinvent native Skills; missing hot-reload + cross-tool portability.
- G1.10 No PostToolUse hooks (CE synthesis v2 §G3 `SYNTHESIS-DEEP-CE-vs-JETIX.md:2068-2073`) — only git-level pre-commit, not runtime-level.
- G1.11 No MCP server for wiki (CE synthesis v2 §G6 line 2086-2091).
- G1.12 evals/ folder empty Day 1 (CE synthesis v2 §G4 + §G8 line 2098-2102) — Promptfoo + Langfuse adoption planned Phase 1 Day 14-17.
- G1.13 Agent roles hard-coded под consulting, не configurable per use case.

---

## Part 2 — Universality assessment (current Jetix wiki/docs)

### 2.1 Universal concepts (portable к astronomer / animal-husbandry use cases)

Inventory из design/decisions (wiki/ has ideas but не operationalizations; these are the concepts that **could** apply beyond Jetix):

1. **A.1 Holonic Foundation** (FPF canonical, D6 §1.1 lines 230-237) — U.Entity ⊃ U.Holon ⊃ U.System + U.Episteme. Astronomer's lab holon = Solar System as system-and-episteme; animal-husbandry farm holon. Tier structure portable.
2. **A.14 typed mereology edges** (D6 §3.5) — 6 canonical (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf) — pure ontological primitive.
3. **8 True Alphas pattern** — Client / Project / Hypothesis / Member / Way of Working — 4 from 8 are fully domain-agnostic (Project, Hypothesis, Member, Way of Working). Deal + Content Item + Direction — partial (Direction может mapped к "research program" in astronomy).
4. **Past-participle state machine discipline** (D6 §5.5 lines 1447-1521 + 5.5a whitelist) — universally applicable modelling primitive.
5. **ШСМ 5 primitives** (D6 §5 reference, elaborated в `wiki/foundations/shsm-primitives.md` — currently missing) — per D9 §1.2 and synthesis references `raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md`.
6. **Creation Graph 3-level** (D6 §3) — target / creation / supersystem — pure decomposition primitive.
7. **Role ≠ Executor strict separation** (D6 §5.1 = IP-1 lines 1273-1296) — archetype vs binding; universally applicable.
8. **Agency-CHR spectrum 0.0-1.0 с BMC/PH/MP/PER/OC dimensions** (D6 §2.1a lines 437-515) — generalizable scale.
9. **F-G-R trust tagging** (D6 §4.2 lines 922-942 + B.3 reference) — Formality / claim-Scope / Reliability on any deliverable.
10. **Multi-View Publication Kit** (D6 §4.4 lines 1007-1027 + E.17 reference) — 5 viewpoints pattern generalizable. Executive/Technical/Governance/Regulatory/Internal-learning can retarget к Astronomer (Public/Scientific/Funding-agency/Peer-review/Lab-internal).
11. **Bias-Audit Cycle BA-0/1/2/3** (D6 §12.10 + §4.3 5-class taxonomy REP/ALG/VIS/MET/LNG) — universal quality mechanism.
12. **Writing-as-thinking primitive** (D6 §5.3 IP-3 lines 1322-1366 + Левенчук grounding) — universal cognitive discipline.
13. **Unified Term Sheet (F.17 UTS)** — 30-50 rows × 6-8 context columns + LEX-BUNDLE 4-register (D9 Section §P1 and Gap 4 `decisions/gap-analysis-review-decisions-2026-04-20.md:128-144`). Ontology-translation mechanism generalizable.
14. **L/A/D/E Boundary Discipline** (D6 §4.3 lines 944-1005) — Laws / Admissibility / Deontics / Effects contract routing. Generalizable to any regulated domain.
15. **Resource Accounting Tier 1 + Tier 2** abstraction (D9 §P7 P7.1-P7.5) — Capital / Compute / Deep Hours / Attention — universal for knowledge-worker domain.
16. **Meta-agent as immune system / FPF-Steward sub-role** (D6 §5.4 lines 1367-1396) — universal pattern for knowledge-base integrity.
17. **ReAct loop + per-agent loop variant assignment** (R-9 + CE synthesis v2 Top-8 insight 7 `SYNTHESIS-DEEP-CE-vs-JETIX.md:143-151`) — pattern-library generalizable.
18. **4-layer termination stack** (R-9 + CE synthesis §G10 / Top-7) — universal agent-discipline primitive.
19. **Append-only ACE pattern** for compound learning (CE synthesis v2 §BP7 line 1720-1722) — universally applicable.
20. **Think-Do feedback loop** (`wiki/concepts/think-do-feedback-loop.md`) — cognitive model, domain-agnostic (described by Левенчук + Karpathy + Ruslan).

### 2.2 Jetix-specific concepts (hard-coded под consulting/DACH)

1. **DACH Mittelstand ICP** (D6 §1.1 + §2.5 + entire D9 §P6) — €10M-€500M revenue / DACH / C-level; 210 Jetix|DACH|consulting mentions в D6.
2. **ai-consulting-dach direction** (D9 §P8 + §5.1 folder 5) — primary Q2 revenue bet; entire `directions/_active/ai-consulting-dach/` substrate hardcoded.
3. **11 specific agent roles** — sales-lead / sales-research / sales-outreach / sales-closer (Ruslan sub-role) / acceptance-authority / inbox-processor / crazy-agent — all bound к consulting workflow. Astronomer has no sales-lead.
4. **EU AI Act + GDPR + DACH legal compliance matrix** (D6 §4.5.1 lines 1186-1242) — Annex III / Art. 14 / Art. 22 / Art. 28 / Art. 29 / Art. 37 / HGB §238/§257 / BGB §187 / §38 BDSG.
5. **Freiberufler → UG → GmbH trajectory** (D6 §1.1 line 228; D9 §1.1 lines 61-62).
6. **Stripe + Wise payment** (D9 §P6 line 398-399; D6 §1.3 + §2.5).
7. **Rechnungsnummer monotonicity hook** (D9 §P1 line 259) — German invoice regulation (UStG §14).
8. **DACH institutional networks** (D6 §2.6 line 703; D9 §P7.4 lines 218-221) — IHK / VDMA / BDI / BITKOM.
9. **4 bizmodels strategy pages** (Notion consulting-specific content per `wiki/sources/2026-04-16-command-center.md`).
10. **200-year vision framing** (`wiki/ideas/200-year-vision-jetix-humanity.md`) — long-term narrative Jetix-specific, но philosophically also universal vision genre.
11. **Specific Audit SKU template** (D9 Day 2, 5, 6; D6 §4.4 Multi-View binding к Audit SKU).
12. **5 Ruslan atomic sub-roles** (strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations, D9 §P5 + D6 §2.1) — specific to solo-founder-consulting context.
13. **Jetix 200-year North Star** (`wiki/ideas/200-year-vision-jetix-humanity.md` + Часть 1 Видение в topics/system-design-hub.md:39-60) — Jetix-as-infrastructure-for-humanity, but mission statement is Jetix-brand-bound.
14. **Revenue Share 70% philosophy** (`wiki/concepts/jetix-open-source-principles.md`) — Jetix contract model.
15. **jetix.de domain + GitHub `Bogersebekov/jetix-os` repo** (D9 §5.4 Day 1 line 689; `ARCHITECTURE-CURRENT.md:36-38`).
16. **Hard Rules sales-оргструктура** (D6 §2 table + `CLAUDE.md` — 10 global rules + 8-principle enforcement) — some universal (hub-and-spoke; mailbox schema), some Jetix-specific (Russian content language rule per `CLAUDE.md:46`).
17. **ICP Page / Research Hub / Life OS / Command Center Notion IDs** (`CLAUDE.md:32-40`) — hardcoded external references.
18. **200-year humanity mission** (`wiki/ideas/200-year-vision-jetix-humanity.md:26-30`) — philosophically generalizable but narratively Jetix-bound.
19. **Manifest 7 principles** (`raw/notion-pages/manifest-system-building-2026-04-16.md:37-43`) — Jetix-specific ("12 агентов остаются 12 агентами" rule #1) but several principles (system-first, engineering rigor) universal.

### 2.3 Borderline concepts (could go either way с decision)

1. **200-year vision framing** — philosophically universal, narratively Jetix-locked. **Tradeoff:** Keep as Jetix-company layer; base layer should have its own long-horizon placeholder.
2. **8 alphas roster** — 4 of 8 universal, 3 borderline (Client, Deal, Content Item), 1 specific-context (Direction — if user has no portfolio ambition). **Tradeoff:** extract 4 universal alphas as base; 4 optional as overlay-configurable.
3. **Hub-and-spoke 11-agent** — topology universal, agent names Jetix-specific. **Tradeoff:** abstract "N-department-leads + subagents" in base; overlay provides specific naming.
4. **Think-Do feedback loop** (`wiki/concepts/think-do-feedback-loop.md`) — universal as concept; но sourced из specific Ruslan personal philosophy. **Tradeoff:** Keep as universal but note `source-context: ruslan-anton-mentor-2026`.
5. **Engineering Faith** (`wiki/concepts/engineering-faith.md`) — universal mental model, но Jetix uses it в brand identity. **Tradeoff:** describe в base as pattern; overlay uses it в marketing.
6. **Voice-notes pipeline** — tool choice universal (Whisper / Claude); output format (markdown review-latest) aligned к Ruslan's workflow, но trivially reconfigurable. **Tradeoff:** base = pipeline abstraction + config hooks; overlay = Ruslan review format.
7. **Research Hub + Command Center Notion integration** — workflow pattern universal, specific Notion IDs Jetix-bound. **Tradeoff:** base = Notion adapter interface; overlay = specific IDs.
8. **Open source premium model / Red Hat philosophy** (`wiki/ideas/open-source-premium-jetix-model.md`) — pattern universal, но Jetix's particular business-model choice Jetix-company-specific.

### 2.4 Symbolic test results

**Quantitative baseline of Jetix-specificity in primary artifacts (counted 2026-04-21, grep pattern `Jetix|DACH|AI consulting|Mittelstand|consulting`):**

| Artifact | Jetix-specific mentions | Lines total | Jetix-specific density |
|----------|------------------------|-------------|-----------------------|
| `design/JETIX-FPF.md` | 210 | 3758 | 5.6% per line |
| `design/JETIX-ARCHITECTURE-WORKING.md` | 133 | 2264 | 5.9% |
| `decisions/2026-04-19-architecture-v2-approval.md` | 89 | 1995 | 4.5% |
| `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` | 69 | 1880 | 3.7% |
| `design/DATA-FLOWS.md` | not counted (inferred high) | 1091 | — |
| `design/SYSTEM-DESIGN-INPUTS.md` | not counted | 1289 | — |
| `design/SYSTEM-DESIGN-TECH.md` | not counted | 2456 | — |

**Wiki breadth counts (grep):**

- "universal|portable|use case|plugin|configurable|extensibility" в wiki/: **0 matches** (grep result)
- "open.source|open-source|opensource|revenue.share|форк|сообществ" в wiki/: 217 matches across 55 files (grep result) — но exclusively Jetix-contextualized.
- "универсал|платформ|конфигур|portable|fork|overlay|base" в wiki/: 306 matches across 250 files (grep), но manual sampling показал: абсолютное большинство — Jetix brand references ("платформа Jetix" / "базовый подход Jetix"), не в sense universality criterion.

**Implication:** **"universality" vocabulary полностью отсутствует** в текущем knowledge base. Vision's universality criterion — greenfield concept, не extension of existing.

**Full external count of "Engelbart|Augment|Memex|Xanadu|Dynabook":** 0 in design/ and 0 in wiki/ (grep). Only "Karpathy|LLM OS" matches (5 references in design/, 11 files in raw/research/). **Vision-relevant external lineage не зацитирована** — ни Engelbart Augmenting Human Intellect, ни Vannevar Bush Memex, ни Dynabook; Karpathy LLM Wiki — единственный external thinking-system reference в wiki.

---

## Part 3 — Vision-relevant patterns from research (R-1..R-11 + Synthesis v2)

Drawn from `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md` (3998 lines, finalized today commit 015e274) + constituent R-N reports.

### 3.1 Patterns directly supporting "OS-for-thinking" genre

1. **Karpathy "LLM Wiki" April 2026 framing** — `SYNTHESIS-DEEP-CE-vs-JETIX.md:136-137` "Echoed by Karpathy's 'LLM Wiki' framing (per Antigravity.codes April 2026 reporting)". R-10 §7.1 ref 4 + `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:248` direct link to Karpathy April 2026 gist. Karpathy frames personal LLM knowledge base as **ongoing wiki**, not RAG-query-and-forget.
2. **System Prompt Learning (SPL) as Karpathy's "third paradigm"** — synthesis `SYNTHESIS-DEEP-CE-vs-JETIX.md:358-363`. Third paradigm of LLM learning alongside pretraining + fine-tuning: "Something like the Memory feature, but not per-user random facts — general/global problem-solving knowledge and strategies… knowledge-guided 'review' stage is significantly higher-dimensional feedback channel than a reward scalar." This is explicitly "system **for** thinking", not just "system **that** thinks" — aligns Vision Layer 1.
3. **Memory-cognitive taxonomy (Baddeley-style)** — R-10 §1.4 / synthesis `SYNTHESIS-DEEP-CE-vs-JETIX.md:1058-1067`: episodic (mailboxes.jsonl) / semantic (wiki/concepts+entities+graph) / procedural (strategies.md + foundations) / working (scratchpad.md). **4-type memory taxonomy IS the cognitive-OS primitive.** Applies to any domain.
4. **Letta Context Repositories (Feb 2026) как reference architecture** — synthesis `SYNTHESIS-DEEP-CE-vs-JETIX.md:1130-1133`: *"git-backed memory + sleep-time consolidation + composable SKILL.md + sub-agent orchestration"*. **This IS the canonical OS-for-thinking pattern as of 2026.**
5. **File-based git-backed memory wins over managed vector stores** (T12 convergent theme, synthesis lines 1462-1469; BP14 line 1749-1752). Transparency + GDPR + portability + selective-forgetting viability. Universal pattern для any knowledge worker, not just consulting.
6. **Sleep-time compute pattern** — R-10 §2.9 / synthesis `SYNTHESIS-DEEP-CE-vs-JETIX.md:1084-1098`. Asynchronous inference during agent idle periods; 5× compute reduction at equal accuracy; 2.5× per-query cost reduction when 10 queries share context; +18% Stateful AIME. **Cognitive-OS primitive — "thinking ahead of demand".**
7. **Levenchuk practitioner community reference** — D6 §3.4 external supersystem line 813-814 "Левенчук practitioner community (reference-only)". ШСМ (Школа Системного Менеджмента) body of work — Система мышления + Системное мышление 2024 + Методология 2025 + Стратегирование 2025 etc. FPF (First Principles Framework) github.com/ailev/FPF is the ultimate "OS-for-thinking" body of work (62,202 lines per D6 §0.5). **Jetix's D6 IS an OS-for-thinking built by adapting someone else's OS-for-thinking.**
8. **Compound Learning / error→rule→skill pipeline** — synthesis T7 line 1437-1439. Boris Cherny's `@claude add to CLAUDE.md` PR pattern + Every's `/ce-compound-refresh` + jonathanmalkin /wrap-up Phase 3. **All are OS-for-thinking micro-operations (learning as first-class operation).**

### 3.2 Patterns supporting universality / extensibility

1. **Skills open standard (Dec 2025 agentskills.io)** — synthesis §BP2 line 1700-1701 / Top-3 line 102-106. Three-level progressive disclosure: metadata (~100 tok) → body (<5,000 tok) → files on-demand. Cross-tool portability Cursor / Codex CLI / Gemini CLI. **This IS a configurable plugin system** — Vision's use case A / B / C get distinct Skills configurations on same base.
2. **Plugin packaging R-1 §2-b** — Compound Engineering MIT-licensed plugin, 50+ agents + 42+ skills, forkable. Jetix Phase 2a+ plugin opportunity (synthesis §G2 line 2063-2067).
3. **Sub-agent patterns (R-7 §5.1)** — `.claude/agents/<name>.md` + YAML frontmatter. Extension via new agent file. Universal.
4. **Hooks system settings.json** — R-7 §5.2 27+ lifecycle events. Extension point для determinism.
5. **MCP servers (100M monthly downloads by April 2026 per synthesis T9 line 1445)** — tool integration open standard. Third-party knowledge sources pluggable.
6. **Anthropic memory tool (Sept 2025) — file-based, ZDR-eligible** — synthesis S12 line 1647-1653. 6 commands (view/create/str_replace/insert/delete/rename). Client-side storage. **File-based primitive = universally portable.**
7. **Voyager-style persistent skill library** — synthesis line 903-904 (R-9 §3 Q4) + line 1025-1028. Jetix's `wiki/niches/` currently closest analog; Phase 2a formalization as named skill registry with executable bindings — **this IS universality-adapter mechanism**.
8. **FPF Agency-CHR per decision class** (D6 §2.1a lines 437-515) — schema generalizable; overlay-configured CHR matrices per use case.

### 3.3 Patterns supporting "system for managing systems" (Jetix meta-level ambition)

1. **Holonic A.1 foundation** — D6 §1.1-1.7. System holons + episteme holons recursively nested. **This IS the "system of systems" primitive.**
2. **Creation Graph 3-level mereological** — D6 §3. Explicitly "systems creating systems operating-in systems". Recursion supported без upper bound.
3. **Compose-CAL composition primitives** (reference D6 §0.5 Preamble; full elaboration in wiki/foundations/ которые ещё не написаны).
4. **Nested Holonic Structure (A.1 + A.14)** — D6 §1.7. Recursive: Life-OS → Jetix-OS → Jetix-Sales-Function → 5 atomic sub-roles + 11 agent roles → 8 alphas. Universal pattern.
5. **Method Quartet Harmonisation (F.11 adoption)** — D6 §3.3 methodologies list line 787. Left-right meta-method coordination. Generalizable.
6. **MHT (Meta-Holon Transition) B.2** — D6 §0.7 line 122 + §12.13. Phase-change where composition yields new coherent whole. 4 MHTs planned Phase 1→2a / 2a→2b / 2b→2c / 2c→3. **Universal pattern** для system evolution.
7. **Γ (universal aggregation operator) 6 flavours** — D6 §0.7 line 123 + §12.6. Revenue / knowledge / method aggregation. Domain-configurable.
8. **A.14 full Advanced Mereology** — 6 canonical edges portable across domains.

---

## Part 4 — External references в wiki и design (что мы цитируем, что pertains к Vision)

### 4.1 Methodology references

- **Анатолий Левенчук** — primary external methodology anchor. References:
  - D6 preamble line 152-156 (Левенчук FPF quote + EN translation)
  - D6 §3.1 line 732-734 (Методология 2025)
  - D6 §5.1 line 1283-1284 (ШСМ method quote)
  - D6 §5.5 line 1453-1458 (Системное мышление 2024 quote + EN)
  - Hybrid methodology synthesis `raw/research/hybrid-framework-synthesis-2026-04-18.md`
  - 5 Perplexity researches `raw/research/levenchuk-fpf-research-2026-04-20/` (R-A full body of work, R-B ШСМ 5 primitives, R-C 17 trans-disciplines mapping)
  - `wiki/ideas/engineering-thinking-meta-role.md` — Левенчук: "менеджмент = инженерия организаций"
  - Full KB compilation `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`
- **SEMAT Essence** — D6 §3.1 line 734 "по мотивам OMG Essence 2.0:2024". 7 alphas legacy reference. `raw/notion-pages/*` reference via topics/system-design-hub.md.
- **Anthropic Constitutional AI / Constitutional Classifiers** — synthesis `SYNTHESIS-DEEP-CE-vs-JETIX.md:374-380`. Bai et al. Dec 2022 + Feb 2025 classifiers.
- **Karpathy** — wiki/concepts/jetix-open-source-principles.md:32, wiki/entities/claude-code.md:31, wiki/overview.md:7, raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:248-253 (direct links к Karpathy LLM Wiki gist, context engineering tweet, system prompt learning tweet, Year in Review 2025, Software 3.0 YC keynote, nanochat repo).
- **Boris Cherny** — D9 §2.1 implicit via R-7; synthesis §1.7 line 668-768. howborisusesclaudecode.com reference.
- **Every.to / Dan Shipper / Kieran Klaassen** — synthesis §1.6 line 587-665. Compound Engineering coinage.
- **Naval Ravikant** — `wiki/sources/2026-04-16-chetyre-urovnya-leverage-po-naval-ravikant.md` (index reference).
- **Taleb / Talab** — NOT found in grep (checked).
- **Adam Grant** — NOT found in grep.

### 4.2 Tooling references

- **Notion** — 11 Notion system-pages ingested per wiki/log.md line 9-18. Command Center (191 lines + 17 sub-pages), Research Hub (645 lines + 18 sub-pages), ICP Page (409 lines + 1 sub-page), Life OS, Daily Log format, Pipeline рабочего дня, Анализ недели, Типы чатов AI rules, Потоки информации. `CLAUDE.md:43-51` — 8 Notion database IDs hardcoded (Command Center / Daily Log DB / Projects DB / Journal of Chats / Банк идей / ICP Page / Research Hub / Life OS).
- **Obsidian** — `wiki/overview.md:63-65` "Откроется поверх wiki/ как vault. Структура совместима: flat-каталоги, wikilinks, markdown." + `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md:277` — Open question "Интеграция с Obsidian — да/нет? Karpathy рекомендует, но Jetix работает через Claude Code напрямую." **Ruslan personally uses Obsidian patterns (wikilinks) but not Obsidian app** per current architecture.
- **Heptabase** — `wiki/ideas/stek-instrumentov-dlya-vtorogo-mozga-2026.md:22-28` — "Heptabase (визуальные связи) + Obsidian (атомарные заметки) + AI-поиск".
- **GitLab Handbook** — NOT found in grep (0 matches).
- **Company-as-code** — 1 file: `raw/research/company-as-code-impl-deep-research-2026-04-19.md`. This is Jetix's own adaptation of GitLab Handbook genre. D9 §1.1 line 66 cites "Company-as-Code (git = единственный source of truth)" as first architectural paradigm.
- **Engelbart / Augment / Memex / Xanadu / Dynabook** — **0 matches anywhere in repo** (grep confirmed). Vision's underlying "augmenting human intellect" lineage is **unstated**.
- **Karpathy LLM OS** — 1 match `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md:1048` "Letta (ex-MemGPT): OS-inspired три уровня памяти". No direct "Karpathy LLM OS" naming, but Karpathy LLM Wiki + Letta OS-inspired together cover the genre.
- **Roam** — 1 match wiki/index.md (idea listing stek-instrumentov line).
- **Dynabook / Xanadu / Memex / Engelbart** — 0 matches anywhere.
- **Linux** — `wiki/entities/linux.md` (7 references in wiki/niches/business/README.md et al.). Inspiration for open-source principle only.
- **GitHub** — `wiki/entities/github.md` + "GitHub для бизнес-проектов" idea `wiki/ideas/github-for-business-projects.md`.
- **CrewAI** — `wiki/sources/2026-04-16-automate-research-via-crewai.md` + `wiki/ideas/automate-research-via-crewai.md`.

### 4.3 Concept references

- **Second Brain / Second brain** — `wiki/ideas/vtoroy-mozg-kak-sistema-upravleniya-mnozhestvom-proekto.md` + `wiki/ideas/stek-instrumentov-dlya-vtorogo-mozga-2026.md` + `wiki/ideas/sayt-vizitka-kak-vtoroy-mozg-narabotki-idei-sistema-zhi.md` — concept referenced 3+ times в wiki/ideas.
- **PARA** — 0 matches.
- **Building a Second Brain** (Tiago Forte) — 0 matches.
- **Personal OS / Personal Operating System** — 0 explicit matches; concept implicitly present в `wiki/ideas/personalnye-sistemy-upravleniya-kak-produkt-budushchego.md` line 22-28.
- **Networked Thought** — 0 matches.
- **Digital Sovereignty** — `wiki/concepts/digital-sovereignty.md`. Partial alignment: "right и возможность в любой момент перейти с вендора на альтернативу".
- **Engineering Faith** — `wiki/concepts/engineering-faith.md` + idea — "план + инструменты + вера".
- **Think-Do loop** — `wiki/concepts/think-do-feedback-loop.md`.

**Summary:** **Historical OS-for-thinking lineage (Engelbart, Memex, Xanadu, Dynabook, Personal Knowledge OS) is completely absent**. Modern references (Karpathy, Letta/MemGPT, Anthropic Skills, Obsidian, Heptabase, Second Brain, GitHub-for-business-projects metaphor, CrewAI) are partially present. Vision's claim "новый вид операционных систем для мышления — чего раньше не было" is **not backed by historical context** in the wiki — this is a gap that SYNTHESIS-GOAL.md needs to address (cite forebears to sharpen novelty claim).

---

## Part 5 — Contradictions между Vision и existing content

1. **Hard Rule "internal-only hard" (D9 §2.2 lines 161-163 + D6 §0.5 "scope: internal-only") + OQ-09 A "no contribute-back к ailev/FPF community" vs Vision "Self-improving through forking, GitHub, community — Phase 2+" + "post-€200K open source".**
   - Decision-level contradiction. D9 quotes Ruslan explicitly 2026-04-20: «всё держим, ничего никуда не отправляем, нигде не публикуем» (D6 §0.5 preamble line 182).
   - **Resolved temporally** (now = internal; Phase 2+ = open), but **architectural seam for separability is not laid down** in current design artifacts. D9 §5.1 puts everything inside single `~/jetix-os/jetix/` folder tree; no base/overlay split.

2. **D6 §2.2 11-agent specialized roster (sales-lead / sales-research / sales-outreach / ... / inbox-processor) vs Vision Universality (use case B astronomer / use case C animal-husbandry).**
   - Agent names are hard-coded к DACH consulting. Role ≠ Executor split (D6 §5.1 IP-1) provides architectural replaceability for executors but not for role names themselves.
   - Astronomer's role roster = observation-lead / data-reducer / hypothesis-formulator / peer-review-authority; animal-husbandry = herd-manager / breeding-analyst / feed-planner.
   - Jetix has **no "role-template vs role-instance" abstraction** — role.md IS role name IS role usage.

3. **Jetix-specific decisions vs universality ambition.**
   - D6 §4.5.1 EU AI Act 4-tier matrix — applicable only в EU. Astronomer in USA or animal-husbandry в Argentina has no EU AI Act obligations.
   - D6 §P7.1 Compute tracking в EUR — currency hardcoded.
   - D6 §P6 Unified funnel через Stripe — payment processor hardcoded.
   - Rechnungsnummer monotonicity hook (D9 §P1 line 259 + Day 2 line 690) — German invoice regulation-specific.
   - **All compliance + payment + currency assumptions are Jetix-company-specific; base layer has no place to absorb them.**

4. **"Методология работает очень качественно, глубоко проработана" (Vision Quality Fundamentals) vs wiki/foundations/ EMPTY.**
   - Vision claims deep methodology already exists. Check 1: `wiki/foundations/` folder **empty** (0 files per ls output). Check 2: D6 cites `wiki/foundations/jetix-uts.md`, `jetix-creation-graph.md`, `shsm-primitives.md`, `holon-hierarchy.md`, `trans-disciplines.md`, `jetix-innovations.md`, `fpf-tooling.md`, `fpf-distilled.md` — **all не существуют**. Phase 1 Day 5-17 ETA per D9 §5.4 lines 701-716.
   - **The deep methodology is в D6 constitutional document (3758 lines, draft-synthesized state), not в accessible foundations/ artifacts.** Onboarding другого user (Vision's use case B/C) would require reading D6 cover-to-cover — 3-4 hours per D6 §0.5 reader routes table.

5. **Vision "Можно откатиться назад" (simplicity + reversibility) vs D9 §2.2 + D6 §0 adopting 25+ new FPF-grounded patterns (Boundary Discipline / Trust Tagging / Characteristic Spaces / UTS / Multi-View / Bias-Audit / MHT / Agency-CHR).**
   - FPF adoption "max depth + no compromises" (gap-analysis-review-decisions-2026-04-20.md:27-34) creates learning curve Ruslan himself notes в D6 §0.5 — "3-4 hours" for full internal team member, «Full Document + §14 references» for FPF-Steward quarterly audit "4-6 hours".
   - **Base layer for use case B/C cannot demand this depth**. Need "FPF-Lite" base + "FPF-Full" overlay distinction — **no such architecture currently exists**.

6. **Voice-notes pipeline STOP before distribution (CLAUDE.md:132-135, `tools/distribute.py.bak` archived) vs Vision Layer 3 "делать за неделю что было месяцем".**
   - Intentional friction в autonomy to preserve human review — correct DACH compliance + Levenchuk "writing-as-thinking" preservation discipline.
   - Vision's productivity promise tension: manual review bottleneck limits Layer 3 acceleration scaling.
   - **Not necessarily contradiction — but Vision SYNTHESIS-GOAL should explicitly quantify "acceleration vs human-in-loop" tradeoff per tier (J-Auto / J-Approve / J-Strategic).**

7. **Manifest "Ничего мы не упрощаем" (raw/notion-pages/manifest-system-building-2026-04-16.md:18) vs Vision "Зациклено на простоту".**
   - Manifest 2026-04-16 explicitly chose "Путь A (полное оживление системы). Путь B (упрощение) — отклонён" line 46.
   - Vision 2026-04-21 says "Зациклено на простоту".
   - **Resolution pending:** likely "simple at user-facing API / deep under the hood" — but **nowhere articulated**.

---

## Part 6 — Gaps (что Vision требует что в wiki ещё нет)

### 6.1 Missing concepts

1. **Configuration / overlay system** — separability base/overlay architecture. Nothing in design/ or wiki/ defines HOW jetix-company overlay composes onto jetix-os base. No YAML schema, no merge rules, no precedence order.
2. **Universality testing methodology** — Vision locked decisions include "B benchmark + C multi-use-case + D symbolic test" — no existing framework, no measurement tool, no baseline.
3. **Plugin / extension formal spec** — D9 §5.1 has `.claude-plugin/plugin.json` mentioned в synthesis §G2 recommendation, but nothing in design/. No interface contract describing what base vs overlay CAN / CANNOT extend.
4. **Onboarding curve для другого user (3-12 months)** — D6 §5.8 "Onboarding" referenced but not expanded for non-Jetix user. No "astronomer boots this OS в day 1 does X" walkthrough.
5. **Open source governance plan** — post-€200K timeline but no written plan. License choice (MIT / Apache 2.0 / AGPL / custom?) not decided. Governance structure (BDFL / steering committee / foundation) — nothing. Trademark strategy vs Disney (D9 §P6 backlog) unresolved.
6. **Use case canonical examples** — Vision's use cases B (астроном + Солнце/астероиды) and C (животновод) exist only as 3-sentence Vision paragraph. No canonical user story, no sample artifacts, no validation with imagined users.
7. **"OS-for-thinking" canonical framing + historical lineage** — Engelbart Augmenting Human Intellect (1962), Bush Memex (1945), Nelson Xanadu (1960s), Kay Dynabook (1970s), Drexler Hypertext (1986) — none cited. Vision's novelty claim "чего раньше не было" unsupported by positioning against forebears.
8. **Layer 1 "Learning" mechanism** — wiki gives memory, no "spaced-repetition" / "skill tree" / "curriculum" / "learning velocity metric". Pure capture + retrieve, no acceleration of understanding.
9. **Layer 2 "Deep dive" project template** — stages + variants + scenarios + risk analysis. D6 alphas give state machines but not decomposition template.
10. **Layer 3 universality adapter** — "agent role configurable per domain" — 11 Jetix agent roles do not parameterize.

### 6.2 Missing mechanisms

1. **Auto-pattern extraction (quarterly only currently)** — synthesis §G5 line 2079-2084. Manual strategies.md append, no automated pattern detection like jonathanmalkin `/wrap-up` Phase 3.
2. **Multi-use-case test framework** — D (symbolic test) + B (benchmark) + C (multi-use-case) Vision metrics — no eval harness. evals/ folder empty (synthesis §G4 / G8).
3. **Demo readiness criteria** — "можно продемонстрировать как астроном натягивает Jetix base за 1 неделю" — no criteria, no staging env, no reset tooling.
4. **Overlay composition rules** — YAML / JSON schema for how `jetix-company/overlay.yaml` overrides `jetix-os/base/*.md` — not specified.
5. **Sleep-time compute для batch context** (synthesis §G11 / BP15 line 1754-1757) — 5× compute reduction but not implemented.
6. **Extended thinking on long-horizon agents** (synthesis §G12) — Goal Drift paper requires thinking variants для tasks >32 steps.
7. **4-layer termination stack per agent** (synthesis §G9 / G10) — maxTurns + Task Budget + verifiable predicate + HITL.
8. **Hook-based determinism for CP-5** (synthesis §G3) — currently advisory.
9. **Anti-sycophancy для multi-reviewer fan-out** (synthesis §G13) — heterogeneous models + PoLL ensemble.
10. **Voyager-style persistent skill library** (synthesis line 1025-1028) — Phase 2a formalization.

### 6.3 Missing connections

1. **Layer 1/2/3 explicit mapping в D-документах** — D6 + D9 не используют Vision's 3-layer taxonomy; they use L0-L7 7-layer reference architecture (D6 §1.5 lines 308-344). **7-layer ≠ 3-layer** — no crosswalk.
2. **Holonic foundation A.1 application к user-provided overlay** — conceptually Life-OS as supersystem, Jetix as holon, но overlay-layer как what? Not mapped.
3. **Multi-view publication for non-Audit SKU** — D6 §4.4 ties Multi-View к Audit SKU delivery. Use case B astronomer has no Audit SKU — how does Multi-View generalize?
4. **Karpathy LLM Wiki pattern → Vision's Layer 1** — wiki/ already implements it, но не labeled как cognitive Layer 1 anywhere.
5. **FPF ontology → universal vs Jetix-specific split** — no artifact currently labels which FPF patterns are base vs overlay.
6. **D9 8 principles ↔ Vision 3 layers** — no crosswalk. Some P map naturally (P1 Git=SoT → infrastructure, not layer; P3 alphas → Layer 2; P7 Resource Accounting → Layer 2; P8 Portfolio → Layer 2; rest → unclear).

---

## Part 7 — Recommendations для SYNTHESIS-GOAL.md

**Concrete suggestions based on findings above. These are inputs for SYNTHESIS-GOAL.md drafting — not finalized copy.**

### 7.1 Capabilities с пометкой "base" vs "overlay"

**Base capabilities (universal, minimum viable OS-for-thinking для астронома / животновода / Ruslan):**

- B1 **Memory architecture**: wiki/ 9 entity types + per-agent 5-layer memory (Core/Strategies/Working/Archival/Recall) — structure portable.
- B2 **Karpathy LLM Wiki loop**: ingest / ask / lint / consolidate / build-graph.
- B3 **Voice-notes pipeline** abstraction (transcribe → extract → filter → review).
- B4 **4 universal alphas**: Project / Hypothesis / Member / Way-of-Working (state-machine-per-alpha + past-participle discipline).
- B5 **Creation Graph 3-level** decomposition.
- B6 **A.14 typed mereology edges** (6 canonical).
- B7 **A.1 Holonic Foundation** + Nested Holonic Structure.
- B8 **Role ≠ Executor** + Agency-CHR schema (no specific role roster).
- B9 **F-G-R trust tagging** on deliverables + ADRs.
- B10 **Bias-Audit Cycle** (5-class taxonomy REP/ALG/VIS/MET/LNG or domain-configurable).
- B11 **L/A/D/E Boundary Discipline** (Laws / Admissibility / Deontics / Effects — regulated domains; optional for unregulated).
- B12 **Resource Accounting abstraction** — Capital + Compute + Deep Hours + Attention.
- B13 **Unified Term Sheet (UTS) skeleton** — rows = domain concepts × context columns.
- B14 **Multi-View Publication pattern** — N-viewpoint template (5 is default; domain-configurable).
- B15 **Meta-agent / Knowledge-steward immune system**.
- B16 **Writing-as-thinking primitive** — IP-3.
- B17 **Rituals cadence abstraction** — weekly / monthly / quarterly + trigger-driven (content domain-configurable).
- B18 **Skills + hooks + MCP + subagents** — Claude Code native primitives.
- B19 **Git-as-SoT pattern** + Company-as-Code adaptation.
- B20 **ReAct loop + per-agent loop variant assignment** + 4-layer termination stack (synthesis §BP11 / BP12).
- B21 **Append-only ACE pattern** for compound learning.

**Overlay capabilities (Jetix-company-specific, installed onto base):**

- O1 DACH Mittelstand ICP definitions.
- O2 ai-consulting-dach direction + folder.
- O3 11 specific agent roles (sales-lead, sales-research, sales-outreach, etc.).
- O4 EU AI Act + GDPR + BDSG compliance matrix.
- O5 Freiberufler→UG→GmbH legal trajectory.
- O6 Stripe + Wise payment + EUR currency.
- O7 Rechnungsnummer monotonicity hook.
- O8 DACH institutional networks references (IHK, VDMA, BDI, BITKOM).
- O9 5 Ruslan atomic sub-roles (strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations).
- O10 Jetix 200-year North Star + Revenue Share 70% philosophy.
- O11 Specific 4 bizmodels Notion content.
- O12 Audit SKU templates + Multi-View viewpoint bundle (5 views с DACH-specific audiences: Aufsichtsrat / BfDI / etc).

### 7.2 Anti-scope items extracted из Hard Rules

- "NEVER expose API keys" — base discipline, preserve.
- "Notion = external truth; filesystem = internal truth" — partial contradiction с Vision separability (internal truth must allow multiple overlays). Resolve in SYNTHESIS-GOAL.
- "NEVER trogat' ~/.ssh/, /etc/, .env, private/" — base discipline, preserve.
- "Russian for content; English for code and configs" — **Jetix-specific**; overlay choice для other users.
- "Hub-and-spoke: subagents report к Department Lead" — pattern universal; department names overlay-specific.
- "Manager attention budget: max 20 active tasks" — operational tuning parameter, base can expose as config.

### 7.3 Success metrics — quantified universality criteria

Based on Vision locked decisions:

- **B — benchmark**: fraction of base tests passing без overlay modifications. Target: 100% of B1-B21 tests pass на empty overlay.
- **C — multi-use-case**: 2+ non-Jetix use cases successfully onboarded (astronomer + animal-husbandry). Success = each completes "10-task canonical workflow" в <1 week учитывая 3-day onboarding + 1-day setup.
- **D — symbolic test**: grep count of "Jetix|DACH|AI consulting|Mittelstand|consulting" в base/ folder. Target: **0 matches** в base/*.md, except в explicit `examples/jetix-company/` sub-folder.
- **U1 — base/overlay code split**: % of D6/D9 content reclassified as base vs overlay. Baseline 2026-04-21: ~30% reclassifiable as base; target = ≥60% reclassifiable before Phase 1 Day 17.
- **U2 — learning curve**: time for external test user (Ruslan-simulating-astronomer) to set up base → produce first meaningful artifact. Target: ≤ 3 working days solo.

### 7.4 Constraints — explicit trade-offs

- T1 **Depth vs breadth**: FPF full-depth adoption (D6 §P8 "max Левенчук") conflicts с base simplicity Vision demands. Resolution: **base = FPF-Lite (10-12 patterns from Gap 1-5 + holonic A.1 + typed mereology A.14); overlay = FPF-Full (Levenchuk max-depth for Jetix-company)**.
- T2 **Hard internal-only (now) vs open source (post-€200K)**: resolved temporally. **SYNTHESIS-GOAL explicit Phase stages** (Phase 1 internal = now; Phase 2 private overlay structure = post-€20K MRR; Phase 3 open-source base = post-€200K ARR).
- T3 **11 named agents vs universality**: base has NO specific agent roster; overlay introduces specific agents.
- T4 **EU regulatory compliance embedded in templates vs non-EU users**: base provides L/A/D/E discipline as pattern, overlay fills with jurisdiction-specific regulations.

### 7.5 Priority directions — base vs overlay split

- **Base первый (Phase 1 post-SYNTHESIS-GOAL):** wiki architecture + 5-layer memory + voice-notes pipeline + 4 universal alphas + A.1 holonic + A.14 typed edges + Role≠Executor + F-G-R + Writing-as-thinking + ACE compound loop + ReAct + termination stack + append-only pattern.
- **Overlay второй:** 11 specific agents + 4 specific alphas (Client / Deal / Content Item / Direction) + EU AI Act matrix + Stripe + German invoicing + Notion IDs + 200-year vision + Revenue Share philosophy + bizmodel pages.

### 7.6 Quality criteria — universality axis added

- **Universality grade F/G/R extension** — extend B.3 F-G-R tagging с 4-й dimension U (universality-claim): U-base (portable universally), U-overlay (Jetix-specific), U-borderline (config-dependent). Mandatory on every design/decisions artifact.

### 7.7 Selection criteria — long-term platform vs Phase 1 €200K speed

- Phase 1 (€200K revenue): overlay-first execution (Jetix-company быстро зарабатывает €200K).
- Phase 2 (post-€200K): reclassification pass — extract base from overlay, publish base layer MIT/Apache 2.0, keep overlay proprietary.
- Phase 3: external validation via use case B/C onboarding; measure D symbolic test + U1/U2 metrics; iterate base.

---

## Part 8 — Open questions raised by search

1. **What is the exact base/overlay packaging model?** Separate git repos (`jetix-os/` + `jetix-company/`)? Submodule? Overlay-as-folder within single repo? D9 §P4 lightweight mereology gives part-of semantics but not file-system split. Needs Phase 1 decision.
2. **How does FPF-Lite relate к FPF-Full formally?** Fork? Subset profile? D6 §0.5 reader routes suggest tier 1/2/3 loading already solves for **agent** load; but for **external user learning Jetix-OS base** no equivalent tier exists.
3. **Use case B (астроном) canonical user story** — needed for benchmark C definition. Who writes it? Ruslan drafts? Cloud Cowork simulates?
4. **Will base language be bilingual (RU+EN) like Jetix-company, or EN-primary for international adoption?** Vision mentions Russian primary (Ruslan working language); base targeting international users likely requires EN-primary.
5. **D9 11 agent roster vs base "N agent roles configurable"** — how much of current role-manifest content is base (role.md structure is universal) vs overlay (specific role identities)? Who drafts role-template abstraction?
6. **Karpathy LLM Wiki vs OmegaWiki vs Letta Context Repositories** — which is canonical base reference? synthesis v2 endorses wiki/+strategies pattern verbatim — stabilize language в SYNTHESIS-GOAL.
7. **Voice-notes pipeline generalization** — currently Groq Whisper + Claude + markdown review format. Base should parameterize STT provider + LLM provider + output format — but what's the minimum viable config schema?
8. **How does Portfolio-of-Directions generalize?** Use case B (астроном) may have "research program portfolio"; use case C (животновод) may have "herd + production streams" — same pattern or different?
9. **Are 4 pre-commit hooks base or overlay?** Asymmetric reference = probably base (any user has base+overlay structure); Rechnungsnummer = definitely overlay; role-manifest validation = base schema but overlay content; past-participle = base.
10. **What is the minimal base evals/ harness?** synthesis §G4 + §BP17 recommend Promptfoo + Langfuse — base-worthy or overlay?

---

## Part 9 — References

### 9.1 Wiki files cited

- `wiki/index.md` (lines 1-187)
- `wiki/log.md` (lines 1-112)
- `wiki/overview.md` (lines 1-65)
- `wiki/entities/jetix.md` (lines 1-73)
- `wiki/entities/claude-code.md` (lines 29-32)
- `wiki/concepts/jetix-open-source-principles.md` (lines 22-36)
- `wiki/concepts/value-three-layers.md` (lines 22-46)
- `wiki/concepts/digital-sovereignty.md` (lines 22-32)
- `wiki/concepts/think-do-feedback-loop.md` (referenced)
- `wiki/concepts/engineering-faith.md` (referenced)
- `wiki/concepts/collaborative-project-versioning.md` (referenced)
- `wiki/concepts/curated-community-access.md` (referenced)
- `wiki/concepts/writing-as-telepathy.md` (referenced)
- `wiki/claims/business-projects-like-code.md` (line 34)
- `wiki/topics/system-design-hub.md` (lines 21-199)
- `wiki/ideas/200-year-vision-jetix-humanity.md` (lines 22-45)
- `wiki/ideas/system-first-myth-second.md` (lines 22-50)
- `wiki/ideas/self-improving-system-inevitable-dominance.md` (lines 22-50)
- `wiki/ideas/jetix-open-source-philosophy.md` (lines 22-45)
- `wiki/ideas/github-for-business-projects.md` (lines 22-70)
- `wiki/ideas/jetix-as-infrastructure-metaphor.md` (lines 22-46)
- `wiki/ideas/founder-responsibility-jetix-constitution.md` (lines 22-55)
- `wiki/ideas/vtoroy-mozg-kak-sistema-upravleniya-mnozhestvom-proekto.md` (lines 22-35)
- `wiki/ideas/stek-instrumentov-dlya-vtorogo-mozga-2026.md` (lines 22-45)
- `wiki/ideas/kognitivnaya-arkhitektura-ot-umeniya-dumat-k-sisteme-my.md` (lines 22-35)
- `wiki/ideas/tsifrovoy-klon-myshleniya-cherez-zametki-ii.md` (lines 22-35)
- `wiki/ideas/perekhod-ot-ya-dumayu-k-sistema-dumaet-za-menya.md` (lines 22-35)
- `wiki/ideas/armiya-ai-agentov-vokrug-odnoy-lichnosti.md` (lines 22-35)
- `wiki/ideas/sistema-upravleniya-proektami-dashbordy-chit-kod.md` (lines 22-35)
- `wiki/ideas/personalnye-sistemy-upravleniya-kak-produkt-budushchego.md` (lines 22-35)
- `wiki/sources/2026-04-16-architecture-memory-kb-karpathy.md` (lines 14-38)
- `wiki/sources/2026-04-16-manifest-system-building.md` (lines 14-36)
- `wiki/sources/2026-04-16-life-os.md` (lines 14-35)

### 9.2 Design files cited

- `design/JETIX-FPF.md` (3758 lines total) — §0 (lines 46-105), §0.5 (lines 80-105), §0.7 glossary (108-125), §1.1-1.8 (219-403), §2.1-2.7 (408-720), §3 Creation Graph (723-895), §4.1-4.6 Client Principles (898-1265), §5.1-5.7 Internal Principles (1273-1597)
- `design/JETIX-ARCHITECTURE-WORKING.md` (2264 lines) — referenced for Jetix-specificity counts
- `design/SYSTEM-DESIGN-INPUTS.md` (1289 lines) — referenced
- `design/SYSTEM-DESIGN-TECH.md` (2456 lines) — referenced
- `design/DATA-FLOWS.md` (1091 lines) — referenced
- `design/IMPLEMENTATION-PLAN-2026-04-18.md` (387 lines) — referenced

### 9.3 Decisions files cited

- `decisions/2026-04-19-architecture-v2-approval.md` (1995 lines) — Chunk 1 framing (lines 29-112), P1 (42-46), P2 (47-51), P3 (52-61), P4 (63-67), P5 (68-90), P6 (92-127), P7 (129-250)
- `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (1880 lines) — §1.1-1.4 (lines 54-128), §2.1-2.3 (130-235), §3 P1-P8 (239-502), §4 Reference vs Operational (504-558), §5.1-5.6 Phase 1 operational (564-747)
- `decisions/gap-analysis-review-decisions-2026-04-20.md` (509 lines) — Executive summary (45-80), Gap 1 (85-94), Gap 2 (95-111), Gap 3 (113-126), Gap 4 (128-144), Gap 5 (146-167)
- `decisions/life-decisions-log.md` (45 lines) — referenced
- `decisions/review-v2-progress-checklist.md` (170 lines) — referenced

### 9.4 Research files cited

- `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md` (v2, 3998 lines, commit 015e274 today) — Executive Summary (lines 26-195), Top 8 strategic insights (lines 84-163), Top 5 recommended actions (166-176), Part 1 per-wave (197-1399), Part 2 cross-wave patterns (1401-1899), Part 3 comparison (1902-2163), Part 4 strategic implications (2166+)
- `raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md` (510 lines) — referenced via synthesis
- `raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md` (736 lines) — referenced
- `raw/research/compounding-engineering-2026-04-22/R-3-self-improving-systems.md` (897 lines) — Karpathy SPL (§2.1), HITL spectrum (§3.3), 10 failure modes (§6.1)
- `raw/research/compounding-engineering-2026-04-22/R-4-failure-modes-critique.md` (616 lines) — referenced
- `raw/research/compounding-engineering-2026-04-22/R-5-production-case-studies.md` (853 lines) — Aider solo (§3), Claude Code case study (§6)
- `raw/research/compounding-engineering-2026-04-22/R-6-every-cora-compound.md` (594 lines) — 12-reviewer fan-out (§3)
- `raw/research/compounding-engineering-2026-04-22/R-7-boris-cherny-claude-code.md` (831 lines) — 10 design principles (§6.1), CLAUDE.md origin (§4), Boris sub-agent philosophy (§5.1)
- `raw/research/compounding-engineering-2026-04-22/R-8-skills-claudemd-knowledge.md` (1333 lines) — Skills (§1), CLAUDE.md size (§2.4), Jetix migration plan (§7)
- `raw/research/compounding-engineering-2026-04-22/R-9-agentic-loop.md` (1362 lines) — loop variants (§3), termination stack (§5), Recommendations per-dept variant table
- `raw/research/compounding-engineering-2026-04-22/R-10-continual-learning.md` (1295 lines) — Jetix endorsement (§7.2), cognitive taxonomy (§1.4), Letta Context Repositories (§8.2), Anthropic memory tool (§4.5)
- `raw/research/compounding-engineering-2026-04-22/R-11-evals.md` (1295 lines) — Promptfoo + Langfuse (§8.1), Hamel Critique Shadowing (§4), benchmark saturation (§3)
- `raw/research/architecture-synthesis-v2-final.md` — referenced in D9 based_on
- `raw/research/fpf-gap-analysis-2026-04-20.md` — referenced
- `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` — referenced
- `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md` — referenced
- `raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md` — referenced
- `raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md` — referenced
- `raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md` (288 lines) — crucial Vision-relevant substrate
- `raw/notion-pages/manifest-system-building-2026-04-16.md` (53 lines) — 7 principles

### 9.5 External references found в wiki (concept mentions)

- **Anatoly Levenchuk / FPF / ШСМ** — heavy presence via D6 + research
- **Karpathy LLM Wiki + context engineering + SPL + Software 3.0** — wiki + raw + synthesis
- **Boris Cherny / Claude Code** — synthesis R-7
- **Every.to / Dan Shipper / Kieran Klaassen / Cora** — synthesis R-6
- **Walden Yan / Cognition Devin** — synthesis R-2, R-4, R-5, R-9
- **Anthropic Skills (Oct 2025, open standard Dec 2025)** — synthesis R-8, R-10
- **Letta / MemGPT / Context Repositories** — synthesis R-10
- **Mem0 / Zep / Cognee** — synthesis R-10
- **Microsoft GraphRAG / HippoRAG / KARMA** — raw/notion-pages Karpathy page
- **OmegaWiki / Astro-Han karpathy-llm-wiki / SamurAIGPT llm-wiki-agent / LLM Wiki v2 gist / AgentWiki** — raw/notion-pages Karpathy page
- **Naval Ravikant** — wiki/sources/* (4 levels of leverage)
- **Anton (mentor) / Vladislav (economist) / Rodion (YouTuber)** — D6 §2.4 + wiki
- **SEMAT Essence / OMG Essence 2.0** — D6 §3.1
- **GitHub / Linux / Apache / Wordpress** — wiki/concepts/jetix-open-source-principles.md + wiki/entities/
- **Obsidian / Heptabase / Roam** — wiki/ideas/stek-instrumentov-dlya-vtorogo-mozga-2026.md
- **Hamel Husain / Eugene Yan / Shreya Shankar** — synthesis R-11
- **Promptfoo / Langfuse / Braintrust / Inspect AI / Phoenix** — synthesis R-11
- **MCP (Model Context Protocol)** — synthesis R-8

### 9.6 External references NOT found (Vision-relevant gaps)

- **Engelbart (Augmenting Human Intellect, 1962)** — 0 matches
- **Vannevar Bush (Memex, 1945)** — 0 matches
- **Ted Nelson (Xanadu, 1960s)** — 0 matches
- **Alan Kay (Dynabook, 1970s)** — 0 matches
- **Doug Lenat / Cyc** — 0 matches
- **Tiago Forte (Building a Second Brain / PARA)** — 0 matches
- **Emacs Org-mode** — 0 matches
- **Niklas Luhmann / Zettelkasten** — 0 matches
- **GitLab Handbook** — 0 matches

---

---

## Verifier Verdict (independent subagent audit 2026-04-21)

**Claims sampled:** 10. **Verified accurate:** 6. **Minor inaccuracies:** 2 (off-by-1 / off-by-2 line numbers). **Material inaccuracies:** 2 — both **fixed in this version**:
- `CLAUDE.md:113-116` → corrected к `CLAUDE.md:132-135` (distribute.py.bak citation).
- `CLAUDE.md:32-40` "7 Notion DB IDs" → corrected к `CLAUDE.md:43-51` "8 Notion DB IDs".
- Manifest quote line 17 → corrected к line 18.

**Core quantitative claims fully verified:** wiki/foundations/ empty (only .gitkeep); wiki/niches/*/ only README.md each (6 niches); grep count 210 Jetix|DACH|consulting|Mittelstand в design/JETIX-FPF.md; 0 matches для Engelbart|Memex|Xanadu|Dynabook across wiki/ and design/; commit 015e274 exists; Gap 1/4/5 line ranges correct; D6 §0.5 reader-routes table ("3-4 hours" / "4-6 hours") accurate.

**Overall verifier verdict:** MEDIUM-HIGH CONFIDENCE (post-fixes). Quantitative spine solid; remaining line-number citations in §9 (which references ~30+ file:line pointers) were not exhaustively re-verified — treat Part 9 references as **navigational, не quotable-as-authoritative** until a full verification pass before commit к production SYNTHESIS-GOAL.md.

---

**END OF WIKI SEARCH DELIVERABLE — draft for Cloud Cowork + Ruslan review before SYNTHESIS-GOAL.md writing**
