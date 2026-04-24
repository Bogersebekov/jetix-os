---
id: master-plan-foundation-to-execution-2026-04-24
title: "Master Plan — Foundation → Layers → Strategy → Execution (неделя 2026-04-24 → 2026-05-01)"
type: master-plan
state: active
created: 2026-04-24
target_week: 2026-04-24 → 2026-05-01
owner: Ruslan (decisions) + Cloud Cowork (execution) + brigadier swarm (heavy lifting)
priority: critical — это единственный living plan document для текущей недели
tags: [master-plan, foundation, layers, execution, phase-sequence]
supersedes_for_this_week: prior priority stacks (VISION-NEXT §3 будет обновлён после Phase 1 done)
---

# Master Plan — Foundation → Layers → Strategy → Execution

> Единственный source-of-truth для текущей недели. Возвращаемся сюда каждый раз когда не понятно "что дальше". Ruslan + Cloud Cowork + brigadier swarm работают **по этому списку**.

---

## ⚡ DEEP DIVE POLICY (lock per Ruslan directive 2026-04-24 23:50 CET)

**Ruslan verbatim:** *«мы делаем full foundation настолько deep чтобы дышать даже было невозможно. Deep dive. Наш подход — deep dive. Каждой задаче у нас deep dive. Везде deep dive. Документы которые deep dive мы делаем deep dive. Запомни сука.»*

**Binding principle:** каждый foundation-level документ (Phase 2 layer deep-dives + Phase 3 strategic docs) пишется на **МАКСИМАЛЬНУЮ глубину**:
- 15-25K слов минимум per document
- Каждый sub-component раскрыт полностью (не skipping / compression)
- Diagrams обязательны
- Evolution per gate (€0 → €50K → €200K → €1M → $100M → $1T) expanded verbally + tabular
- Все preserved dissents с обоснованием
- F-G-R tagging per major claim
- Citations к source (voice-memos / existing docs / books / research)
- Open questions resolved or explicitly deferred с reasoning
- Ruslan approval gate после КАЖДОГО document — никакого Full-Auto

**Anti-pattern disqualified:**
- Compression под "word-count floor marginally missed" (как было в SYSTEM-OVERVIEW integration §L? per-layer 356-874 слов вместо 800 floor — впредь no tolerance)
- Summary mode vs depth mode
- "Beta-enough" для foundation documents — beta применяется к gate-timing, не к craft standard

**Beta-first остаётся для:** gate-timing (skippy ship), execution artefacts (landings / outreach / sales materials — fix-in-flight).

**Deep Dive применяется к:** foundation (this master plan) + layer deep-dives (Phase 2) + strategic docs per direction (Phase 3) + JETIX-COMPASS.

---

## §0 Почему этот план существует

Ruslan 2026-04-24 озвучил: *«foundation системы вместе с агентами ещё не описан — нужно сперва закончить foundation, потом каждый слой обработать, потом уже наслаивать исследования/продажи/ICP/задачи в правильные слои»*. Существующие Vision/Philosophy/Plan/Architecture-Brief + 24 Locks покрывают philosophy и goals, но **coherent layered system description с агентами как first-class citizens отсутствует**. Без этого стратегические документы на направления (ai-consulting-DACH, producer-services, Secure Network) и ICP Trinity строить преждевременно — не понятно в какой слой они ложатся.

Дополнительно — накопились 4 новых lock-кандидата (D25-D28) из voice-memos 506-529, плюс открытый вопрос USB-C vs McKinsey-platform, плюс product name "Smart AI" из audio_529 — всё это должно войти в foundation **до** materialization strategy.

## §1 Точка А — что реально готово (repo state 2026-04-24)

### Foundation documents (approved)
- `decisions/JETIX-VISION.md` D1 (495 строк)
- `decisions/JETIX-PHILOSOPHY.md` D2 (983 строки)
- `decisions/JETIX-PLAN.md` D3 (923 строки)
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` D4 (842 строки)
- `design/JETIX-FPF.md` constitutional (3758 строк)
- **24 Locked decisions** (D1-D24) в 3 TENSIONS документах

### Strategic additions 2026-04-24
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` — 6-pillar roadmap
- `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` — local-first client-private KB positioning
- `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` (621 строк)
- `raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md` (sales asset)

### Swarm infrastructure live
- 6 agents в `.claude/agents/` (brigadier + 5 experts) — 8077 строк
- `swarm/wiki/` v3 (53 dirs, 9 entity templates, 12 edge types)
- `swarm/lib/shared-protocols.md` — 9-section runtime contract
- 5 alphas определены

### Завершённые swarm cycles
1. **swarm-self-improve-v1** — 47 hyp → 19 clusters → 4 opp + 2 HITL ✓
2. **cycle-2 implementation** — OPP-01 evals + OPP-02 hooks + OPP-04 predicate + HD-01 + HD-02 ✓
3. **km-architecture-research** — 6 variants + 9 dissents + sequenced-trajectory recommendation ✓

### Voice-memos
- 529 memos обработано до audio_529 (24.04 02:48)
- `reports/review_2026-04-24.md` — 1858 units / 141 memo
- `reports/summary_2026-04-24.md`
- `reports/delta-506-529-2026-04-24.md` — свежий delta digest

## §2 Точка A — что СЕЙЧАС в полёте

### KM Materialization MVP swarm (T-km-materialization-mvp-2026-04-24)
- ✓ Phase 1 intake + Phase 2 WBS (10 cells × 4 waves, HD-02 N=3 override)
- ✓ Wave 1: Parts A+B+C design records promoted (philosophy-critic integrated)
- ⏳ **Wave 2 pending:** Part D company-as-code cross-cutting
- ⏳ **Wave 3 pending:** Part E real Jetix application (quick-money + research adaptive bootstrap + E2E demo)
- ⏳ **Wave 4 pending:** 5-gate horizon projection
- ⏳ Part F verification + AWAITING-APPROVAL → HALT

**Estimate до AWAITING-APPROVAL:** 1-2 дня (brigadier resume через fresh session).

## §3 Критичные gaps в foundation

### Gap 1: **JETIX-SYSTEM-OVERVIEW отсутствует**
Coherent layered system description с агентами как first-class citizens. Foundation для всей остальной работы.

### Gap 2: Явной layered architecture нет
8 слоёв (L0 Philosophy / L1 Foundation / L2 Knowledge / L3 Operations / L4 Product / L5 Business / L6 Community / L7 Trajectory) нигде не описаны единообразно.

### Gap 3: 4 новых lock-кандидата висят
- **D25 Company-as-Code** (audio_510) — явная методология
- **D26 Team 50-100 (не one-person)** (audio_510, решение #119) — переопределение из one-person
- **D27 Fork-and-merge evolution** (audio_519) — GitHub-style mutation → merge mechanism
- **D28 Query-driven KB filtering** (audio_522) — уточнение Private Library

### Gap 4: USB-C vs McKinsey-platform не разрешён
Открытый вопрос — одно и то же или разные positioning. Блокирует document-compass.

### Gap 5: Product name "Smart AI" (audio_529) — статус
Потенциальный D29 lock: external product name Jetix = Smart AI.

### Gap 6: ICP Trinity фрагментирован
13 TODO про ICP по разным файлам. Нужен consolidation, но **только после OVERVIEW** — сейчас преждевременно.

## §4 План по фазам (неделя 2026-04-24 → 2026-05-01)

### Phase 0 — Decisions (сейчас, ≤15 мин)

**Blocker:** без этих решений foundation содержит противоречия.

- **D-0.1** Ruslan ack'ает/reject'ит D25-D28 (по одному или скопом)
- **D-0.2** Ruslan разрешает USB-C vs McKinsey-platform (a/b/c из 5 предложенных опций)
- **D-0.3** Ruslan решает статус "Smart AI" как product name (D29 или internal-only)
- **D-0.4** Ruslan ok'ает порядок фаз (foundation → layers → strategy → execution)
- **D-0.5** Ruslan ok'ает запуск SYSTEM-OVERVIEW swarm параллельно с KM Mat resume

### Phase 1 — Foundation consolidation (24-27 апреля, 2-4 дня)

**Task 1.1 [Cloud Cowork]:** Если D25-D28 ack'нуты → создать `decisions/LOCKS-D25-D29-ADDENDUM-2026-04-24.md` + update 24-Locks canonical reference.

**Task 1.2 [new swarm cycle — JETIX-SYSTEM-OVERVIEW]:**
- Запускается параллельно с KM Mat resume (HD-02 N=3 budget accommodates)
- Brigadier орcхестрирует 5 experts в system-description mode
- Output: `decisions/JETIX-SYSTEM-OVERVIEW.md` (~15-25K слов)
- Структура: 8 layers (L0-L7) × для каждого: что это / какие agents живут тут / boundaries / interfaces с соседними слоями / current status / open questions
- Включает: D1-D24 + D25-D29 (если ack'нуты) + USB-C/McKinsey resolution + Smart AI status
- Mermaid/ASCII диаграммы для каждого слоя
- Stage-Gated: AWAITING-APPROVAL перед Phase 7 compound

**Task 1.3 [Ruslan]:** Review SYSTEM-OVERVIEW → approve/modify/reject.

**Task 1.4 [KM Mat resume — brigadier fresh session]:** продолжение Wave 2+3+4+F текущего KM Mat cycle. Ruslan запускает в отдельном tmux.

### Phase 2 — Layered Deep-Dives (25-30 апреля, 5-6 дней) — **DEEP DIVE POLICY APPLIES**

**Revised per Ruslan 2026-04-24 23:50 directive: full foundation, maximum depth, Ruslan approval gate per document.**

После OVERVIEW approved (✓) и KM Mat extracted (✓) — последовательные layer deep-dives. Каждый — **отдельный M-task swarm cycle с Stage-Gated AWAITING-APPROVAL перед Ruslan ack**.

Порядок (по criticality для revenue + downstream dependencies):

**Wave 1 — Revenue critical path:**
1. **`decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md`** (включает ICP Trinity как §N) — клиенты + партнёры + команда + Alliance + matchmaker + archetypes + 5-criteria filter; unblocks outreach
2. **`decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md`** — 9 directions детально (consulting / producer / USB-C services / matchmaker / Secure Network / YouTube-SaaS / educational / tokens / Smart AI flagship); unblocks strategic docs
3. **`decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md`** — pricing Path A/B/C, unit-econ, 5 gates €50K → $1T, revenue streams per direction, миллионер reconciliation (audio_529 $1M+ vs audio_470 $240-600K/year)

**Wave 2 — System depth:**
4. **`decisions/LAYER-4-AGENTS-DEEP-DIVE.md`** — 20 agents roster (6 ROY + 14 legacy) reconcile CLAUDE.md, 5×4 matrix mechanics, 5-layer memory per agent, hub-and-spoke, fork-and-merge agent evolution per D27
5. **`decisions/LAYER-8-PEOPLE-ALLIANCE-DEEP-DIVE.md`** — team 50-100 evolution per D26, hires roadmap, Alliance legal structure (Linux Foundation vs ARM Holdings), Secure Network architecture, digital portraits, fork-community governance
6. **`decisions/LAYER-2-KNOWLEDGE-DEEP-DIVE.md`** — Private Library architecture, wiki v3 vs future, D28 query-driven filtering mechanics, topic-wikis per expert, project-wikis, A1→A2→A3 migration triggers
7. **`decisions/LAYER-3-OPERATIONS-DEEP-DIVE.md`** — agents + swarm + skills в production, Plan/Work/Review/Compound 40/10/40/10 mechanics, swarm cycles catalogue

**Wave 3 — Cross-cutting + critical gap:**
8. **`decisions/LAYER-0-FOUNDATION-DEEP-DIVE.md`** — Company-as-Code per D25 governance, git workflow, fork-and-merge protocol (D27), licensing decision (MIT / proprietary / dual), multi-dev atomic commits
9. **`decisions/LAYER-9-GOVERNANCE-DEEP-DIVE.md`** — 28 Locks constitutional + operational policies, constitutional amendment process, beta-first canonicalization, AWAITING-APPROVAL mechanics, dissent preservation §1d
10. **`decisions/LAYER-R-RESOURCE-DEEP-DIVE.md`** — 5 resources (time/attention/money/energy/credits) tracking, dashboard design, OPP-01 ap_cost instrumentation, alerts at thresholds
11. **`decisions/LAYER-C-COMPUTE-DEEP-DIVE.md`** — infrastructure evolution (workstation → data-center → электростанции), client-private inference (Mistral 7B / Llama), sovereign compute
12. **`decisions/LAYER-B-BRAND-DEEP-DIVE.md`** — USB-C narrative + прошивка Windows + operating system мирового масштаба + Smart AI internal label + 3-audience landings + JETIX-COMPASS как output
13. **`decisions/LAYER-P-LIFEOS-DEEP-DIVE.md`** — Ruslan personal system, auto-logging, Life OS as Phase-3 product prototype (audio_529 insight)

**Ruslan approval gate after every deep-dive.** Каждый cycle = fresh brigadier session. Deep dive policy enforced (15-25K words, no compression).

**Estimate:** 1-2 days per layer deep-dive swarm. Total Phase 2: 5-10 дней при последовательном execution. Parallel 2-3 cycles одновременно (HD-02 N=3) сокращает до 4-6 дней.

### Phase 3 — Strategic execution documents (30 апреля - 1 мая, 2 дня)

После всех layer deep-dives:

- `directions/_active/ai-consulting-dach/strategy.md`
- `directions/_active/producer-services/strategy.md`
- `directions/_hypotheses/secure-network-phase2/thesis.md`
- `decisions/JETIX-COMPASS.md` — document-compass 5-15 страниц (TODO 468 из voice-memos) — **производная** от OVERVIEW + strategies
- `decisions/policy/partnership-philosophy.md`
- `decisions/policy/business-portfolio-strategy.md`
- Sales Methodology Wiki — research swarm cycle (параллельно)

### Phase 4 — Business execution (с 1 мая)

- Outreach first batch (5-10 Mittelstand prospects per ICP L6)
- quick-money P1 project bootstrapped live (KM Mat MVP даёт infrastructure)
- First discovery call scripts
- Movement towards €50K Q2 2026

## §5 HD-02 бюджет этой недели

One-cycle override to **N=3** Method-class active per cycle:

- **Slot 1 (running):** KM Materialization MVP (resume для Wave 2+3+4+F)
- **Slot 2 (propose):** JETIX-SYSTEM-OVERVIEW — новый cycle, параллельно
- **Slot 3 (reserve):** свободен — для emergency structural fix или для первого Phase 2 layer deep-dive когда Slot 1 закроется

После этой недели restore to N=2 unless Ruslan re-asserts.

## §6 Конкретные checkpoints

| Дата | Checkpoint | Owner |
|---|---|---|
| 2026-04-24 конец дня | Phase 0 decisions made + Phase 1 swarm launched | Ruslan + Cloud Cowork |
| 2026-04-25 | KM Mat Wave 2-3-4 done; SYSTEM-OVERVIEW Wave 1 done | brigadier × 2 |
| 2026-04-26 | KM Mat AWAITING-APPROVAL + Part G; SYSTEM-OVERVIEW draft | brigadier + Ruslan ack |
| 2026-04-27 | SYSTEM-OVERVIEW approved; Layer deep-dives начаты | brigadier + Ruslan |
| 2026-04-28-29 | Per-layer deep-dives (L6, L4 first) | brigadier swarm |
| 2026-04-30 | Remaining layers + start strategic docs | brigadier swarm |
| 2026-05-01 | Strategic docs + JETIX-COMPASS | brigadier swarm + Ruslan |

Slippage допустим на 1-2 дня. Если > 2 дня — пересмотр плана.

## §7 Риски

**R-1 Сервер перегрев** — два параллельных swarm cycles могут провоцировать "Too many open files" incident. Mitigation: `ulimit -n 65535` прописан permanently в `~/.bashrc` до запуска второго cycle.

**R-2 Ruslan drift to architecture** — из voice-memos видно склонность к architectural refinements в ущерб $50K execution. Mitigation: Phase 3 strategic docs + Phase 4 execution — **не переносятся позже 2026-05-01**.

**R-3 HD-02 context budget per-cycle** — brigadier session кончается на context budget, нужна resume. Mitigation: brigadier пишет resume-state.md каждый раз когда approaching limit (уже доказано работает в KM Mat).

**R-4 Lock-decisions delay** — D25-D28 без ack'а блокируют SYSTEM-OVERVIEW. Mitigation: решить все 4 одним блоком decision в Phase 0.

## §8 Anti-scope (чего НЕ делаем в этой неделе)

- **NO запуск Phase 2 (A2 federated, A3 GraphRAG)** из KM Materialization — deferred to triggers
- **NO Phase 4 business execution до Phase 3 done** — не выходить в sales без compass + strategy
- **NO M3 solo-vs-matrix experiment** — deferred
- **NO new research tasks** (books/papers/Левенчук deep-dive) пока foundation + layers не готовы
- **NO Notion Dashboard development** — `project_next_focus.md` гласит "на паузе"

## §9 Как Ruslan использует этот документ

1. **Каждое утро:** открываешь этот файл, смотришь §6 текущий checkpoint
2. **Когда не ясно "что дальше":** смотришь §4 текущую фазу → следующий task
3. **Когда появляется новая идея:** добавляешь в backlog, НЕ в текущую фазу (защита от drift)
4. **Когда checkpoint slip больше 2 дней:** зовёшь Cloud Cowork пересмотреть план

## §10 Как Cloud Cowork использует этот документ

1. **Каждое сообщение Ruslan'у:** ссылаемся на §§ этого документа ("по Phase 1.2 сейчас...")
2. **При новой задаче:** проверяем "вписывается в текущую фазу или вне scope?"
3. **При swarm cycle complete:** обновляем §6 checkpoints
4. **При каждом approved artefact:** обновляем §1 точку А

---

## §11 Status log (append-only, newest first)

### 2026-04-24 22:30 CET — Plan created
- Document spawned from Ruslan voice directive "нам надо закончить foundation"
- Current state: Phase 0 decisions pending
- Parallel KM Mat swarm at Wave 1 complete
- No SYSTEM-OVERVIEW exists yet

---

*End of master plan. Updates via append-only status log §11.*
