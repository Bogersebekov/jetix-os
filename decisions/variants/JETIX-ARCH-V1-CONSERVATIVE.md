---
id: jetix-arch-v1-conservative
title: Jetix Architecture Variant 1 — Conservative (Stage 6)
variant: 1
variant-name: Conservative
character-tags:
  - evolution-over-revolution
  - minimum-delta
  - proven-patterns
  - risk-averse
  - locks-maximalist
  - operational-simplicity
date: 2026-04-22
binding: pending-stage-7
status: variant-draft
depends_on:
  - D1 JETIX-VISION APPROVED 2026-04-21
  - D2 JETIX-PHILOSOPHY APPROVED 2026-04-21
  - D3 JETIX-PLAN APPROVED 2026-04-21
  - D4 JETIX-ARCHITECTURE-BRIEF APPROVED 2026-04-21
  - 24 locks D1-D24 binding
  - 21 hard constraints C1-C21 binding
  - 16 anti-patterns AP-1..AP-16 binding
  - D6 JETIX-FPF constitutional
  - CLAUDE.md current canonical state (anchor)
precedence: "D1 + D2 + D3 + 24 locks > D4 > OME / D6 FPF / prior ADRs > wiki atoms / raw / scratchpads"
word_count: ~10100
self_score: 79/100
formality: F2
reliability: R-high
claim-scope: jetix-stage-6-variant-1
---

# Jetix Architecture Variant 1 — **CONSERVATIVE**

> *«Evolve what works, don't rewrite what isn't broken.»*

---

## 1. Executive Summary

Это Conservative-вариант архитектуры Jetix: минимальная дельта от текущего состояния `CLAUDE.md`
+ D6 `JETIX-FPF.md` + OME reference, построенная как **упорядоченная эволюция** того, что уже
работает, а не как переписывание с нуля. Я — один из шести архитекторов Stage 6, и моя роль
внутри ансамбля — быть **противовесом** агрессивным, deep-tech, emergent и wildcard вариантам:
я держу нижнюю границу инноваций (ожидаемый балл 3-5/10), чтобы Stage 7 имел честный якорь
при сборке гибрида или выборе единственного варианта. Foundation строится в полную силу,
прикладной слой намеренно тонкий.

Три-четыре архитектурных решения, которые **отличают** Conservative от вероятных пиков других
вариантов:

1. **Репозиторий = рефакторинг текущей `~/jetix-os/` структуры, не rewrite.** Я предлагаю
   `jetix-os/` (universal base) и `jetix-company/` (overlay) как чистую факторизацию того,
   что уже существует — с сохранением `wiki/`, `agents/`, `comms/`, `shared/`, `raw/`,
   `decisions/`, `prompts/` в неизменных ролях. Любой, кто знает `CLAUDE.md`, ориентируется
   в первые 5 минут.
2. **11-агентный канонический ростер D6 §2.2 — без изменений.** Я не раздуваю роли и не
   коллапсирую. 5 атомарных sub-role Руслана (strategy-lead / framing-lead / sales-closer /
   acceptance-authority / external-relations) — это role-manifests, а не отдельные агенты
   (C12, IP-1). 2 Phase-2a стаба (`dpo`, `customer-success`) — dormant-манифесты.
3. **Runtime'ы минимальны; дизайн максимален.** Dashboard v1 = weekly markdown-отчёт из
   скрипта, matchmaker v1 = ручной checklist над JSONL, USB-C v1 = версионированный
   spec-документ + `design/usb-c/` директория, token economy v1 = **ничего кроме
   зарезервированной директории и spec-файла**. Ни одного Phase-1 runtime'а, который Phase 1
   не обязан иметь по D4 §3.1.
4. **Foundation — полный, бескомпромиссный.** Все 8 элементов D4 §4 реализуются в полном
   объёме, именно здесь Conservative тратит своё «новое»: контракты агентов, handoff-протоколы,
   escalation, shared memory, непрерывные метрики качества, dashboard, резервные маршруты,
   F-G-R тегирование — каждый с конкретным артефактом, владельцем и методом верификации.
   *«Foundation = главный актив»* (D2 §14) — здесь я неуступчив.

**Selection case (детально §24).** Выбирайте Conservative, если Phase-1 survival probability
и качество Foundation важнее скорости scale-trajectory и нарративной инновации. Самый дешёвый
запуск среди шести вариантов, самый простой онбординг второго пилота, самая высокая
locks-compliance; платит за это ростом Phase-2b refactor-cost и низким innovation-score.

---

## 2. Variant Character Statement

Я — **Consertive Architect**. Моя философия, говоря от первого лица: когда brief (D4)
однозначно не требует новизны, я выбираю то, что уже работает в `CLAUDE.md` или в OME. Моя
задача — не впечатлить Руслана, а сохранить Jetix живым в Phase 1 и не заложить мин под
Phase 2, которые взорвутся, когда команда станет больше одного человека.

Мой принцип работы: **каждая нетривиальная структурная дельта должна быть обязана locку,
constraint'у или anti-pattern'у — никогда aesthetic предпочтению или «было бы чище».** Это не
лень, это дисциплина. Новизна, которую Jetix не обязан нести Phase 1, становится долгом: её
нужно документировать, тестировать, мигрировать при росте, защищать от дрейфа.

**Что я принимаю как trade-off (и не делаю вид, что это не trade-off):**

- **Innovation score 3-5/10 — сознательно.** Stage 7 нужно честное дно по инновациям, чтобы
  понимать, от чего Conservative отказывается. Если вы берёте меня — вы берёте этот пол.
- **Scale-trajectory 6-7/10 — честный компромисс.** Я отложил runtime USB-C, token economy,
  matchmaker engine, dashboard UI в Phase 2b+. Это создаёт refactor-debt. Я не скрываю его,
  я его **квантифицирую в §6 (Q4 Scaling)**.
- **Медленный путь к Phase 3.** Conservative тратит Phase 1 на тотальное укрепление
  Foundation; нарративная и сигнальная ценность Phase-2+ раньше у других вариантов.

**Чем я не иду на компромисс (это красные линии Conservative, они совпадают с constraint'ами
D4 §6):**

- **C11 FPF mandatory** — полная интеграция D6 в `system.md` каждого агента, tier'ами
  (§5.4a). Никакого «облегчённого FPF» в Phase 1.
- **C4 filesystem = SoT** — git авторитетен, Notion односторонний view-only. Никаких
  Notion-hack'ов ради удобства.
- **C14 11-агентный ростер** — именно 11, именно по D6 §2.2, именно с переименованиями и
  life-coach → Life-OS. Schema `message.schema.json` синхронизируется Day 1.
- **C16 continuous quality** — *«Continuous, every iteration — NOT periodic»* (D2 §6).
  Сбор метрик — на каждой итерации; Monday-дайджест — это лишь поверхность, а не сам
  контроль.

Conservative — это **дисциплинированный минимализм**, не отсутствие. Мой самый толстый раздел —
§18 Foundation Layer, самые тонкие — §10 Token, §11 Matchmaker, §17 USB-C. Это и есть подпись
вариант.

---

## 3. Q1 — Repository Layout (Base / Overlay)

### 3.1 Минимальная дельта от текущего состояния

Текущее состояние `~/jetix-os/` (CLAUDE.md + файловая система на 2026-04-21) — это, de facto,
уже будущий `jetix-os/` базис + `jetix-company/` оверлей, только **не разделённые явно**. Вариант
Conservative делает эту факторизацию **чистой**, но не переписывает ни одну директорию с нуля.
Принцип: переименование и перенос, не замена.

### 3.2 Целевое дерево (top-3 уровня)

```
jetix-os/                                # universal base (Jetix-agnostic; C9 D-test enforced)
├── CLAUDE.md                            # master config; ссылки на jetix-company/ опциональны
├── MIGRATION.md                         # deprecation notes (knowledge-base/ → wiki/ etc.)
├── agents/                              # 11 canonical agent homes (see §4)
│   ├── manager/
│   ├── personal-assistant/
│   ├── system-admin/
│   ├── sales-lead/
│   ├── sales-research/                  # renamed from sales-researcher per C14
│   ├── sales-outreach/
│   ├── inbox-processor/
│   ├── crazy-agent/
│   ├── knowledge-synth/
│   ├── strategy-support-analyst/        # renamed from strategist per C14
│   └── meta-agent/                      # + FPF-Steward sub-role until Phase-2b trigger
├── roles/                               # Role-manifests (IP-1, C12 Role ≠ Executor)
│   ├── l0-executive/                    # 5 Ruslan atomic sub-roles
│   │   ├── strategy-lead/role.md
│   │   ├── framing-lead/role.md
│   │   ├── sales-closer/role.md
│   │   ├── acceptance-authority/role.md
│   │   └── external-relations/role.md
│   ├── l1-foundation/
│   │   ├── dpo/role.md                  # Phase-2a stub dormant
│   │   └── customer-success/role.md     # Phase-2a stub dormant
│   └── [per-agent role.md mirrored]
├── executors/                           # executor-binding.yaml per agent/role (IP-1, P2)
├── shared/                              # schemas, policies, conventions
│   ├── schemas/
│   │   ├── message.schema.json          # enum regenerated Day 1 from D6 §2.2
│   │   ├── compute-contract.schema.yaml
│   │   └── role-manifest.schema.yaml
│   ├── policies/
│   │   ├── mereology-edge-types.md
│   │   └── eu-ai-act.md
│   └── state/                           # JSON state (agent budgets, queue counters)
├── comms/
│   ├── mailboxes/                       # JSONL per agent (D6 §5.9 acting_as mandatory)
│   └── contractors/                     # JSONL per contractor (designer, lawyer, …)
├── wiki/                                # Karpathy LLM Wiki + OmegaWiki (unchanged from CLAUDE.md)
│   ├── index.md                         # maintained by /ingest
│   ├── log.md                           # append-only chronology
│   ├── concepts/ entities/ sources/ topics/ ideas/
│   ├── experiments/ claims/ summaries/ foundations/
│   ├── comparisons/                     # filing loop from /ask
│   ├── niches/                          # 6 slices (personal, business, sales, life, tech, meta)
│   ├── atoms/                           # atom registry (mereology typed edges)
│   ├── graph/edges.jsonl
│   └── _templates/
├── alphas/                              # 8 past-participle states (FPF §B)
│   ├── configured/ specified/ implemented/
│   ├── tested/ deployed/ operated/ archived/ deprecated/
├── decisions/                           # D1-D4 + ADR Chunks + variants + weekly snapshots
│   ├── JETIX-VISION.md JETIX-PHILOSOPHY.md JETIX-PLAN.md
│   ├── JETIX-ARCHITECTURE-BRIEF.md
│   ├── variants/                        # Stage 6 architect drafts
│   └── weekly/                          # Monday dashboard snapshots (§14)
├── design/
│   ├── JETIX-FPF.md                     # D6 constitutional
│   ├── usb-c/                           # Phase-1 SPEC ONLY (see §17)
│   └── DATA-FLOWS.md AGENT-PROTOCOLS.md
├── prompts/                             # skill prompts, stage prompts
├── raw/                                 # voice memos, research, logs
├── ops/
│   ├── incidents/                       # incident logs
│   └── playbooks/                       # 6h Phase-1 crisis playbooks (MC1 P1-#4)
├── finance/
│   ├── compute-ledger.yaml              # P7.2 append-only, monthly schema
│   ├── revenue-gate-state.yaml          # Lock 15 tier enforcement
│   └── currencies.yaml
├── governance/
│   ├── contractors/redundancy.md
│   └── advisory-board/                  # reserved, dormant (Beirat Phase-2a)
├── compliance/                          # GDPR DPAs, EU AI Act artefacts
├── tools/                               # scripts (transcribe.py, extract.py, filter.py, review_report.py, dashboard.py)
└── life-os/                             # folder-separated; Hook 1 blocks Jetix → Life-OS refs
    └── [parallel mini-structure; Phase-2a `git filter-repo` extracts]

jetix-company/                           # overlay (Jetix-specific instantiation)
├── entities/
│   ├── jetix-gmbh/                      # GmbH namespace, DPAs, compliance calendar
│   └── jetix-ug-interim/                # pre-GmbH entity if needed
├── icp/
│   ├── v{N}.yaml                        # 11 archetypes × 5 criteria + direction-of-life
│   └── current.md                       # rendered projection
├── content/                             # Jetix-branded content, archetype-keyed rendering
├── clients/                             # per-client namespaces (anonymized IDs OK)
├── brand/                               # Lock 8 layered identity: face-per-observer configs
├── legal/                               # Jetix-specific contracts, IP vault (Phase 2+)
└── finance-overlay/                     # Stripe keys (SOPS-encrypted), Wise, tax
```

### 3.3 Нарратив по top-level узлам

`jetix-os/` — **универсальное ядро, Jetix-agnostic**. D-test (§5.5 D2 §10 / C9): `grep` по
строкам `Jetix|DACH|AI consulting|Mittelstand` в `jetix-os/` subtree = **0 hits** (кроме
reference-docs в `decisions/` и `design/`, которые не code/config). Pre-commit Hook 2 проверяет
D-test символически: любой PR, добавляющий Jetix-специфичные идентификаторы в `jetix-os/`,
блокируется. Эта проверка — **единственная новая CI-штука**, которую Conservative добавляет к
текущему состоянию; всё остальное — перенос файлов.

`jetix-company/` — **overlay**, где живёт всё Jetix-специфичное: ICP, контент, клиенты, бренд,
правовые артефакты Jetix GmbH. Overlay свободен от универсальности — там можно писать
`jetix-mittelstand-outreach.md`, потому что overlay и есть Jetix.

**Миграционный путь (минимальный, 1-3 дня работы):**
1. День 1: создать `jetix-os/` и `jetix-company/` как top-level папки внутри текущего
   `~/jetix-os/` репо (так он становится «контейнер»); перенести существующие `agents/`,
   `wiki/`, `comms/`, `shared/`, `raw/`, `decisions/`, `prompts/`, `design/`, `tools/`,
   `life-os/` в `jetix-os/` (git mv).
2. День 2: извлечь Jetix-specific артефакты (ICP, бренд-конфиги, клиентские) в `jetix-company/`
   (git mv + переписать ссылки).
3. День 3: добавить pre-commit Hook 2 (D-test), переименовать агентов (`sales-researcher` →
   `sales-research`, `strategist` → `strategy-support-analyst`), перегенерить
   `shared/schemas/message.schema.json` enum из D6 §2.2 (Lock / C14).
4. День 4: `knowledge-base/` помечается deprecated (см. существующий `MIGRATION.md`). Новые
   артефакты пишутся только в `wiki/`.

Никаких «big bang» миграций. Каждая правка — отдельный git-commit, обратимый.

### 3.4 Cross-dir import policy

Базис никогда не импортирует из overlay. Overlay свободно импортирует из базиса. Это
**жёсткое правило CI** (pre-commit Hook 3 grep-проверкой); оно обеспечивает C9 universality и
поддерживает D-test на уровне импортов.

### 3.5 Membrane и filesystem-SoT

- **Filesystem SoT (C4, Lock 17):** git = истина. Notion — односторонний view, генерируется
  скриптом (`tools/notion_sync.py`) из `decisions/` и `wiki/comparisons/`. Никогда не
  читается агентами как источник.
- **Membrane в директориях (C3 / Q6):** каждый файл несёт frontmatter-поле
  `tier: public|member|partner|core`. CLI-скрипт `tools/publish.py` публикует только
  `tier: public` в surface-pipeline (сайт, соцсети). `partner` и `core` остаются в git private.
- **Private/public мембрана = git-private repo + per-file tier + per-directory conventions**
  (напр., `jetix-company/clients/` всегда `partner` или выше). Никакого отдельного runtime'а
  мембраны в Phase 1 (см. §8 Q6).

**Почему это Conservative:** я переименовал один top-level узел (`jetix-company/`), добавил 3
pre-commit hook'а и 2 frontmatter-поля. Всё остальное — ровно CLAUDE.md сегодняшний. Любой
контрибьютор, знающий текущий репо, ориентируется за 5 минут. Это и есть minimum-delta.
Каждый новый top-level узел обязан ref'у: `decisions/` (C11 + D4 §4), `compliance/` (C15 + §5.3),
`ops/` (C19 enterprise-fast resilience), `governance/` (C15 + Beirat stub dormant), `alphas/`
(C11 FPF §B), `design/usb-c/` (C19 + Q15).

---

## 4. Q2 — Agent Roster Reconciliation

### 4.1 Канонический 11-агентный ростер (D6 §2.2, C14)

| # | Agent ID | Dept | Phase | Model | Function | Manifest-path |
|---|---|---|---|---|---|---|
| 1 | manager | MGMT | 1 | Sonnet 4.6 | Coordination hub, ≤20 active tasks | `agents/manager/` + `roles/manager/role.md` |
| 2 | personal-assistant | OPS | 1 | Haiku 4.5 | Productivity, calendar, OPS lead | `agents/personal-assistant/` |
| 3 | system-admin | OPS | 1 | Haiku 4.5 | Infra, scripts, MCP | `agents/system-admin/` |
| 4 | sales-lead | Sales | 2 | Sonnet 4.6 | Sales coordination | `agents/sales-lead/` |
| 5 | sales-research | Sales | 2 | Haiku 4.5 | Prospect research *(renamed from sales-researcher)* | `agents/sales-research/` |
| 6 | sales-outreach | Sales | 2 | Haiku 4.5 | Outreach & community | `agents/sales-outreach/` |
| 7 | inbox-processor | Brain | 2 | Haiku 4.5 | Information triage + A.16 cues | `agents/inbox-processor/` |
| 8 | crazy-agent | Meta | 2 | Sonnet 4.6 | Creative disruption | `agents/crazy-agent/` |
| 9 | knowledge-synth | Brain | 3 | Sonnet 4.6 | Deep synthesis, Brain lead | `agents/knowledge-synth/` |
| 10 | strategy-support-analyst | MGMT | 3 | Opus 4.6 | Strategic support *(renamed from strategist — NEVER decides)* | `agents/strategy-support-analyst/` |
| 11 | meta-agent | Meta | 4 | Sonnet 4.6 | System auditing + FPF-Steward sub-role | `agents/meta-agent/` |

**life-coach отсутствует в таблице**: мигрирует в `life-os/agents/life-coach/` (C15), не
является Jetix-агентом. Это один из самых важных Day-1-делт: `CLAUDE.md` сегодня упоминает
12 агентов; Conservative синхронизирует `CLAUDE.md` → 11 + обновляет
`shared/schemas/message.schema.json` enum.

### 4.2 Переименования (D4 §4.1 signals, Chunk 3 Item 7)

- `strategist` → `strategy-support-analyst`: роль — **support**, не decision. Никогда не
  «решает стратегически», всегда выдаёт ≥2 опции + kill-criteria + DRR (FPF §E.9). Decision
  остаётся за Ruslan `strategy-lead`. Это прямое следствие C12 + OME L2 (стратегия — orbit
  Руслана).
- `sales-researcher` → `sales-research`: упрощение и согласование с `shared/schemas/`
  agent-ID conventions.
- `meta-agent` несёт FPF-Steward sub-role до Phase-2b trigger (30+ агентов OR 1+ human
  meta-hire OR audit >4h per R12). При триггере FPF-Steward промотируется в 12-ю standalone
  роль — но это Phase-2b архитектурное событие, не Phase-1.

### 4.3 Пять атомарных sub-role Руслана (role-manifests, НЕ отдельные агенты)

`roles/l0-executive/` содержит 5 `role.md` 5-block-манифестов (IP-1, C12):

| Role-manifest | Держит (функция, OME L2 / D1 §3) | Конфликт-резолвер |
|---|---|---|
| strategy-lead | Стратегия — direction of Jetix | левоворукая мета-власть: при конфликте strategy-lead решает |
| framing-lead | Вкус — tone, framing, narrative authority | второй эшелон |
| sales-closer | Отношения + ответственность в sales-контексте | третий |
| acceptance-authority | Утверждение — signs acceptance на deliverable/BA-3 | не конфликтует с первыми |
| external-relations | Отношения — partner / investor / institutional | параллельный канал |

Executor-binding для Ruslan'а (`executors/l0-executive/ruslan.executor-binding.yaml`)
поддерживает multi-role enumeration: поле `acts_as:` — массив. Это **единственный случай**,
когда один executor носит несколько role-manifests. Для агентов такая мульти-роль запрещена
(IP-1 strict).

### 4.4 Phase-2a dormant stubs

`roles/l1-foundation/dpo/role.md` (external-executor режим для GDPR Art.22 + EU AI Act Art.14;
trigger — первый GDPR-DPA клиент) и `roles/l1-foundation/customer-success/role.md` (J2,
account health + retention; trigger — Phase-2a triple-AND per C15). Оба манифеста созданы
Day 9 Phase-1 onboarding (Area 3 18 role-manifests full-depth); активируются per §6 C15
trigger ≥€20K MRR × 3mo AND Ruslan >40% L1/L2 time AND ≥1 GDPR DPA client. F.6 6-step
onboarding применяется к активации.

### 4.5 Schema-sync Day 1 (блокирующий fix)

`shared/schemas/message.schema.json` содержит `properties.sender.enum` с agent-IDs. На
2026-04-21 enum, скорее всего, содержит 12 значений (drift от `CLAUDE.md`). **Day-1 fix:**
регенерация enum из D6 §2.2 (11 значений) + добавление 5 l0-executive role-IDs + 2 dormant
stub role-IDs. 3-way diff (CLAUDE.md ↔ D6 ↔ schema) должен быть 0.

### 4.6 Почему Conservative не раздувает ростер (контр-аргумент Aggressive-Maximalist)

Aggressive-Maximalist вариант, вероятно, предложит 15-18 агентов: separate content-pipeline,
separate compliance-agent, separate community-manager, отдельный матчмейкер-движок-агент,
USB-C-agent и т.п. Я намеренно не иду по этому пути:

- **C14 прямо ограничивает 11-агентным ростером Phase 1.** Любой 12-й агент (кроме FPF-Steward
  при Phase-2b trigger) — это прямое нарушение.
- **Manager attention budget — 20 active tasks hard-limit.** Больше агентов = больше роутинга
  = больше нагрузки на manager. Phase-1 solo — это bandwidth Ruslan'а + manager, не 18 голов.
- **Role-manifest cardinality — НЕ agent cardinality.** Новый поток работы = новый role-manifest
  (cheap, файл + YAML), не новый агент (expensive, mailbox + model + evals + monitoring).
- **Эскалация через 4 FPF-класса справляется с растущим спросом** без добавления агентов
  (§15 Q13).

Короче: **расширение через роли, а не через агентов** — это и есть Conservative-path к
Phase 2a без refactor'а ростера.

---

## 5. Q3 — Integration Points Inventory

Phase-1 architecture touches ~12 внешних систем. Каждая — failure surface. Перечисляю **только
то, что D4 §3 уже требует**; не добавляю «потенциально полезного».

| System | Phase | Direction | Authoritative? | Primary use | Fallback | Failure-mode | Est. cost |
|---|---|---|---|---|---|---|---|
| Claude API (Anthropic) | 1 | R/W | No (fs = SoT) | Primary inference (Opus/Sonnet/Haiku) | OpenAI / Google reserve | Provider outage → Tier-3 pause | €250-500/mo |
| Groq (Whisper) | 1 | R | No | Voice transcribe (voice-memos pipeline) | local whisper.cpp fallback | fallback to local on outage | €10-30/mo |
| Perplexity | 1 | R | No | Research queries (sales-research) | manual web search | degrade to manual | €20/mo |
| Stripe | 1 | R/W | **External SoT on payments** | Billing (session / template / retainer) | Wise manual invoice | degrade to Wise | €0 + tx% |
| Wise | 1 | R/W | External SoT on FX | FX + EUR↔USD + fallback invoicing | manual bank transfer | degrade to bank | €0 + tx% |
| Email (IMAP/SMTP) | 1 | R/W | No | Client comms, Steuerberater, lawyer | direct phone/Signal | degrade to phone | €5/mo |
| Telegram | 1 | R/W | No (view) | Community chat (simple, Phase-1) | Discord alt | degrade — chat pauses | €0 |
| Notion | 1 | W only | **NEVER authoritative (AP-1)** | View-only dashboard projection | (nothing — fs is truth) | degrade — fs works | €0 |
| GitHub | 1 | R/W | git = SoT | Code + decisions + wiki versioning | local git + backup remote | degrade — local git works | €0 |
| Healthchecks.io | 1 | W | No | Cron pings for voice-memos, dashboard | silent cron + manual check | degrade — manual | €0 |
| CRM | 2 | R/W | No | Prospect tracking (sales-outreach) | JSONL in `comms/crm/` | Phase 1 just uses JSONL | deferred |
| ZUGFeRD-gen | 2 | W | No | DE e-invoice Q3 2026 | manual PDF | deferred | deferred |

### 5.1 Guards и принципы

- **AP-1 guard (Notion never authoritative):** `tools/notion_sync.py` — **write-only**.
  Code-review чеклист для любого PR, трогающего Notion: «Is this read from Notion?» → если
  да, блокирующее ревью. Unit-test в `tools/test_notion_sync.py` проверяет, что никакой
  production-код не вызывает `notion.client.get_*`.
- **Revenue-gated spend (C2, Lock 15):** heavy-spend интеграции (Stripe live mode, GmbH
  formation, patent filings, Perplexity-max tier) активируются только при соответствующем
  `finance/revenue-gate-state.yaml`. Phase-1 `compute-ledger hard-block`: когда месячный
  compute-spend приближается к €800/mo envelope, manager-агент блокирует новые inference
  requests и escalates `strategy-lead` (acceptance по D4 Stage-4 approval).
- **Fallbacks — максимально простые.** Primary failure → manual процесс + filesystem. Я не
  строю второй автоматический failover уровень; Phase 1 не может оправдать его стоимость.
- **SOPS 1-key vaulting.** Все API-ключи в `secrets.sops.yaml` (одинаковый age-key на
  Ruslan'а Day 1; multi-key Phase-2a при первом hire). Ноль plain-text credentials в репо.
- **DPA per integration.** Каждая integration с personal-data пересечением — GDPR DPA в
  `compliance/dpa/<vendor>.yaml`. Phase-1 ключевые: Anthropic, Stripe, Wise, Groq, Perplexity,
  Notion (processed data), Telegram.

### 5.2 Что НЕ входит в Phase-1 список

Потенциально полезные, но **намеренно не включаю**: Zapier, Make, n8n (orchestration — не
нужно, mailboxes + скрипты достаточно), отдельный vector store (wiki достаточен, см. §7),
Slack (Ruslan один, mail+telegram достаточно), отдельный CRM SaaS (JSONL до Phase 2),
PostgreSQL/любая БД (filesystem + JSONL, C4 SoT + §7 Q5). Каждое «нет» цитирует ≥1 lock или
anti-pattern: AP-1, C2, C4, AP-16.

---

## 6. Q4 — Scaling Mechanism ($0 → $1T без rewrite)

### 6.1 Принцип Conservative-scaling

Архитектура, которая масштабируется **через наращивание того, что уже есть**, не через
параллельные альтернативные runtime'ы. Scaling = promotion + namespacing + schema-versioning,
не замена.

### 6.2 Per-subsystem scale-path с LOC-оценками refactor-debt

| Subsystem | Phase 1 | Phase 2 ($200K-$1M) | Phase 2b ($1M-$100M) | Phase 3 ($100M-$1T) | Refactor-debt per 10× gate |
|---|---|---|---|---|---|
| Agent roster | 11 agents + 5 L0 roles | +dpo, +customer-success активируются; +FPF-Steward standalone при Phase-2b trigger | 12-18 agents per direction | 18-40 per holding entity | 10-25% LoC per gate (within 30% target) |
| Directory layout | jetix-os/ + jetix-company/ | + `jetix-roys/` namespace for replication | + `jetix-holding/` federation | + per-roy namespaces | 5-10% per gate |
| Message schema | v1 (current) | v2 (roy-routing fields) | v3 (federation fields) | v4 (USB-C interop) | 10-15% per gate |
| Wiki (9 entity types) | JSONL + markdown | + sharding by `scope:` | + GraphRAG evaluation (§7) | + vector store optional | 15-30% at Phase 2b (the one exceeding) |
| Dashboard | weekly markdown | + CLI alerts | + web UI v2 | + grafana-class v3 | 25-40% at Phase 2 transition (biggest one) |
| Matchmaker | manual checklist | + semi-automated (rule-based) | + rule+ML hybrid | + full ML engine | 40-60% at Phase 2b → 3 (the biggest accepted) |
| USB-C protocol | spec only | reference harness + 1 partner | + 3-5 partners reference | + standards-body v1.0 | 70%+ at Phase 2b → 3 (largest; see §17) |
| Token ledger | spec only | internal non-transferable JSONL | + compliance layer | + public tradeable (Phase 3+) | 50-80% at Phase 2 → 3 |
| Compute ledger | JSONL append-only | + provider abstraction | + sharded by direction | + per-roy/per-entity | 10-20% per gate |
| Content pipeline | SSG + markdown | + headless Phase 2+ | + per-archetype microsites | + CDN + i18n | 20-30% per gate |

**Honest flag:** 3 подсистемы превышают 30%-target (D4 §5.1):

1. **Matchmaker (Phase 2b → 3: 40-60%).** Я выбрал ручной checklist Phase 1, потому что
   С21 Lock 21 matchmaker — это Phase-2+ capability (D4 §3.2.3). Phase-1 matchmaker-runtime
   не оправдан revenue-gate (C2). Refactor-cost квантифицирован — см. §11.
2. **USB-C runtime (Phase 2b → 3: 70%+).** Осознанно — D4 §3.3.4 помещает USB-C в Phase 3+,
   Phase-1 seeds «design only». Conservative строит spec-документ + reserved directory; full
   runtime требует стандартов, партнёров, верификационного harness'а, которых Phase 1 не
   имеет ресурсов поддерживать. §17 разбирает это.
3. **Token ledger (Phase 2 → 3: 50-80%).** C21 Lock 23 Option B: внутренний Phase 2,
   ограниченно-публичный Phase 3+. Phase 1 — ни одной строки runtime-кода; только spec +
   reserved directory + ledger schema (append-only JSONL, same pattern как compute-ledger).
   §10 разбирает.

**Почему Conservative принимает эти три превышения:** все три — Phase-2b+ capabilities,
Phase-1 runtime для них был бы premature (AP-5 / AP-12 / C2). Альтернатива — стройка now,
platform risk + пустой расход компьютного бюджета. Refactor-debt предсказуем и локализован
(4 subsystem-boundaries), не разлит по всей архитектуре. Это — риск-торговля в пользу
Phase-1-survival-probability.

### 6.3 Scaling-mechanism primitives (один набор, на все gates)

- **Schema versioning.** `shared/schemas/message.schema.json` → `v2`, `v3`, с backward-compat
  aliases. FPF §B compatibility-matrix поддерживается.
- **Namespacing через директории.** Новый рой = новый `jetix-roys/<roy-id>/` namespace с той
  же структурой, что `jetix-os/`. Это прямое следствие C9 universality.
- **Role → Agent promotion (Lock 20 enterprise-fast).** Когда role-manifest стабильно работает
  как ≥1 FTE = promote to agent (mailbox, evals, monitoring). Трёхэтапный gate (manual →
  semi-auto → agent) защищает от premature promotion.
- **Federation stub dormant (D3 §6.2 MHT-3 trigger).** `jetix-holding/` зарезервирован; active
  только при MHT-3 (€10-50M + 2nd entity). Для Conservative-1 это literally пустой placeholder.

### 6.4 Schema-headroom Day 1 (C18, §5.1)

Все ключевые schemas спроектированы для 10³-10⁶ entity cardinality Day 1, даже если Phase 1
видит 10-100:

- `message.schema.json` поддерживает UUID вместо sequential IDs; sharding key готов.
- `wiki/graph/edges.jsonl` JSONL-append-only масштабируется до 10⁷ линейно; sharding
  пост-Phase-2 по `scope:`.
- `finance/compute-ledger.yaml` — monthly-sharded JSONL; partitioning по `YYYY-MM` → легко
  pivot'ится в любую DB.

**Принцип Conservative:** НЕ реализую sharding сейчас, но НЕ закрываю его архитектурой. Sharding
key есть в schema, implementation — Phase 2b+.

---

## 7. Q5 — Data Architecture (Wiki + Atoms + Provenance)

### 7.1 Почти verbatim текущий `CLAUDE.md` Wiki v2 spec

Conservative не меняет data-архитектуру почти нигде. Вот что уже хорошо:

- **9 entity types в `wiki/`** (concepts / entities / sources / topics / ideas / experiments /
  claims / summaries / foundations) — оставляю как есть (D4 §3.1.13 / Area 5). Никаких новых
  типов.
- **atoms registry** в `wiki/atoms/` — остаётся. 3626 атомов на 2026-04-21, growing.
- **typed mereology edges** в `wiki/graph/edges.jsonl` — 6 FPF (ComponentOf / ConstituentOf /
  PortionOf / PhaseOf / MemberOf / AspectOf) + 4 Jetix (creates / operates-in /
  methodologically-uses / constrained-by +fills). Типы зафиксированы в
  `shared/policies/mereology-edge-types.md` (Rec-05).
- **niches/ symlink pattern.** 6 срезов (personal, business, sales, life, tech, meta); per-agent
  `niche/` — symlink в соответствующий `wiki/niches/<niche>/`. Агенты видят только свой срез.

### 7.2 Delta, которую Conservative добавляет (именно то, что D4 §4.5 / §4.6 требует)

- **F-G-R frontmatter на каждом файле** (C13, Gap 2, OQ-05): `formality: F0-F9` + `reliability:
  R-low|medium|high|certified|formally-proven` + `claim-scope: <bounded-context>`. Retrofit
  существующих 10-15 ADRs в Phase-1 rollout days 15-17 (D3 §3.2).
- **8 alphas past-participle state labels (FPF §B):** каждый artefact несёт
  `alpha: configured|specified|implemented|tested|deployed|operated|archived|deprecated`.
  Добавлен `alphas/` top-level (§3.2). Это C11 FPF mandatory.
- **3-layer memory уже существует в CLAUDE.md Wiki v2:** L1 `wiki/` + L2 `alphas/` +
  L3 per-agent (`agents/<id>/system.md` + `strategies.md` + `scratchpad.md` +
  mailbox). Conservative операционализирует L2 — создаёт alphas/ (сейчас пусто).
- **25K HARD exocortex budget (MC3):** документирован в `design/FOUNDATION-DOCS-RESEARCH.md`.
  Каждый агент `system.md` tier'ается по §5.4a FPF-loading (FPF 7-10K + role 2-3K + alpha
  states 3-5K + Steward 3-5K; remainder flexible). Phase-1 compilance-check: script
  `tools/fpf_size_audit.py`.
- **Provenance fields.** Каждый claim в wiki/ обязан `sources: [...]` в frontmatter +
  inline `[src:filename]` citations. Это уже существующая convention; Conservative укрепляет
  CI-проверкой (pre-commit Hook 4).

### 7.3 Ingest pipeline v2 (не меняю — он уже работает)

`raw` → `ingested` → `compiled` → `linted` → `ready`. Skills: `/ingest`, `/compile`,
`/search-kb`. Это всё уже в CLAUDE.md и реализовано. Conservative добавляет **только** Lock-4
canonical normalization (`Jackson|Джек` → `Jetix`) pre-persistence в `tools/transcribe.py` +
`tools/extract.py`.

### 7.4 Search ranking + citation-emit

- **Phase 1:** `/ask` использует frontmatter-tags + full-text grep + MOC-файлы per cluster.
  **Никакого vector store.** Phase-1 wiki cardinality (10³-10⁴ файлов) — grep + index справится
  с p95 <3s.
- **Phase 2 trigger:** если p95 search >3s (D4 §5.6 latency-based trigger per Chunk 5 Area 5),
  инициируется GraphRAG evaluation. До тех пор vector store = premature complexity.
- **Citations:** `/ask` всегда эмитит inline `[src:...]` per claim; zero-source заявления
  блокируются prompt-template'ом.

### 7.5 Immutability и append-only

- **log.md** — append-only, новые сверху. Rotation >30 entries → `archive/` (current CLAUDE.md
  rule).
- **edges.jsonl** — append-only. Deletions через `status: deprecated` flag, не `rm`.
- **atoms registry** — атомы immutable после создания; update → новый атом с
  `supersedes: atom-XXXX`.

### 7.6 Backup и recovery priorities

Руслан: *«Notion loss recoverable in 1 day, wiki loss = Jetix loss»* (D2 §14). Conservative
применяет это буквально:

- **wiki/ = критический path backup.** Git remote (GitHub private) + weekly cold-backup
  архивом на отдельный SSH-сервер + monthly cold-backup в Tarsnap (€2/mo). 3 независимых
  backups.
- **Notion** — recoverable за 1 день через `tools/notion_sync.py` (re-run из git). Нет
  Notion-backup стратегии.
- **compute-ledger, revenue-gate-state** — git-tracked, поэтому backup-covered.

### 7.7 Почему не БД

Conservative не заменяет JSONL/markdown на Postgres/Sqlite. Причины:

- C4 filesystem = SoT. БД = second source of truth → violating lock.
- Operational simplicity. JSONL grep'ается, diff'ается, human-readable. `cat mailbox.jsonl |
  jq ...` достаточно Phase 1.
- Scale headroom. 10⁶ JSONL lines = ~1-2 GB, грепается за секунды.
- Phase-2b+ можно параллельно поднять DB-индекс над JSONL (read-only projection), не трогая
  SoT.

---

## 8. Q6 — Privacy / Security Membrane

### 8.1 4-tier ACL

| Tier | Visibility | Example content |
|---|---|---|
| **public** | World-readable | Site landing pages, 10 templates lead-magnet, TOF posts |
| **member** | Community chat members (Phase 1: invite-only Telegram) | Mid-tier content, member-only resources |
| **partner** | Clients + paid retainers + Phase 2+ subscription | Deliverables, workshops transcripts, partner SoWs |
| **core** | Ruslan + meta-agent + Phase-2b designated custodians | Prompts, full wiki, FPF innovations, ICP internals, 9 Jetix Innovations |

Маппинг в директории:

- **jetix-os/prompts/** → `core`.
- **jetix-os/agents/*/system.md** → `core`.
- **jetix-os/wiki/foundations/** (FPF innovations) → `core` (OT5 Variant A + OQ-09 A: internal-only
  forever).
- **jetix-os/wiki/comparisons/**, `summaries/` → `partner` default, `public` по opt-in.
- **jetix-company/content/public/** → `public`.
- **jetix-company/clients/** → `partner` per client; sub-tier `core-shared` when client under
  NDA.
- **jetix-company/icp/v{N}.yaml** → `partner` (shared with pilots), rendered `current.md` summary
  → `member`.

### 8.2 Runtime enforcement points (minimal Phase-1 approach)

Я не строю novel ACL daemon. Phase 1 enforcement = **три проверенных механизма**:

1. **Unix filesystem permissions.** `chmod 700` на `jetix-os/agents/*/`, `wiki/foundations/`,
   `prompts/`. Ruslan only.
2. **Git-controlled private repo + branches.** Основной repo — private (GitHub). `partner-tier`
   артефакты публикуются в отдельный branch `partner-public` с subset; `public-tier` — в
   отдельный repo `jetix-public` (читаем/деплоится статическим сайтом).
3. **Per-file frontmatter `tier:` field + CI-проверка.** `tools/publish.py` выбирает по tier'у;
   pre-commit Hook 5 проверяет, что добавленный в `public` не содержит секретов (regex на
   API-ключи, `SOPS`-маркеры, имена клиентов).

**Аналог — Unix permissions + git branches.** Это proven 50-year-old pattern; нет новизны,
нет custom runtime, нет нового surface для атак. Эта конфигурация достаточна для Phase-1 scale
(10-20 pilot-members) и перетаскивается в Phase 2a без рефактора (добавляется membership
system поверх git — но без переделки tier'ов).

### 8.3 GDPR Art. 22 + EU AI Act Art. 14

**CP-5 Human Approval Gate** на client-affecting decisions:

- Scope: любое решение, которое пишется в клиентский deliverable, отправляется клиенту или
  изменяет клиентский договор.
- Мeханизм: agent эмитит `proposal: true`, `final: false` артефакт → routing к `acceptance-authority`
  (Ruslan sub-role Phase 1, `dpo` external-executor Phase 2a+).
- Audit trail: per-decision YAML в `compliance/cp5-audit/<date>-<decision-id>.yaml` с полями
  `decision`, `agent`, `acting_as`, `rationale`, `approver`, `timestamp`, `gdpr_art22_3_explanation`.
- Contestation: `compliance/cp5-contestation/` inbox для client-contestation (WP251rev.01).
  Art. 22(3) explanation — обязательный.
- Retention: client-affecting audit trail — 6 лет (DE HGB §257 + GDPR).
- Safeguard: meaningful review (WP251rev.01) — max 8 L2 approvals per gate-keeper per 4h;
  `time_to_review < 60s` = quality-risk flag (atom-2725).

### 8.4 Phase-2a DPA flow через `dpo` external-executor

Когда активируется `dpo` role (первый GDPR DPA-client):

- `dpo` = external-executor (внешний лawyer DACH); Jetix agents feed audit-data в `compliance/
  dpa-inbound/` mailbox.
- DPA-template drafted <48h (D4 §3.1.4 quality metric).
- `executor-binding.yaml` для dpo указывает chain-of-command: `dpo` → `acceptance-authority`
  → Ruslan.

### 8.5 Gentleman/Predator membrane (C17)

Каждая surface-генерация (site, social, outreach) эмитит по двум режимам:

- **Public/outside (Predator):** pain-primary (Lock 9), aggressive framing, competitive tone.
- **Inside-member (Gentleman):** opportunity-reinforcing, civil, cooperative, deep-substance.

Механизм: template-per-tier в `jetix-company/brand/templates/`; `tier:` на входном контексте
определяет выбор template'а. Это существующая convention (D1 §4 grammar insight); Conservative
формализует её в единый шаблонный engine (Jinja-стиль, без novel framework).

### 8.6 Threat model (Phase-1 minimum viable)

- **Outside adversary:** scrape public surface, phishing Ruslan, credential-stuffing на Git/Stripe.
  Mitigations: SOPS-only secrets, GitHub 2FA + hardware key, Stripe Radar, site behind Cloudflare.
- **Inside leak:** 2nd pilot joins, accidentally commits secret. Mitigations: pre-commit Hook 5
  (secret scan), per-pilot branch + PR review, `partner` tier default for client data.

---

## 9. Q7 — API Architecture (Multi-Provider + Cost Control)

### 9.1 Multi-provider routing

**Primary:** Anthropic Claude (Opus 4.6/4.7, Sonnet 4.6, Haiku 4.5).
**Reserve:** OpenAI GPT-4.x (для Tier-1 агентов при Anthropic outage). Groq Whisper — primary
для voice transcribe (это voice, не text inference). Google Gemini — опционально, second reserve.

**AP-11 guard:** Jetix **никогда** не имеет hard-coded single-provider dependency. Каждый
agent's `executor-binding.yaml` объявляет `fallback_chain:` (Rec-08, A.13:4.3). Chaos-drill
раз в квартал: отключение primary, проверка что Tier-1 agents продолжают работать на reserve
<120s p95.

### 9.2 Router design (Conservative = thin config + function wrapper)

**Никакой SDK-абстракции vendor-neutral.** Вместо:

- `tools/inference_router.py` — один файл, ~200 LoC, content'о:
  - функция `infer(prompt, model_preference, fallback_chain, ...)`,
  - try primary → on failure try reserve[0] → reserve[1] → ... → emit escalation;
  - все вызовы логируются в `finance/compute-ledger.yaml` (append-only JSONL).
- `shared/schemas/compute-contract.schema.yaml` — per-executor контракт
  (`model_preference`, `fallback_chain`, `thinking_mode`, `max_tokens`, `cache_strategy`,
  `latency_class`, `escalation_rules`).

Почему не vendor-neutral SDK: SDK'и (langchain, litellm) — скрытая сложность, непрозрачное
retry, vendor-lock-in на SDK-владельца. Один wrapper-файл — полностью owned, diff'ируется,
дебагается `print`. Это Conservative-choice: proven pattern = прямой код, не framework.

### 9.3 Compute-ledger (P7.2, append-only)

`finance/compute-ledger.yaml` (на самом деле monthly JSONL) — строчка per inference call:

```json
{"ts":"2026-04-22T10:15:33Z","agent":"manager","role":"strategy-support-analyst",
 "provider":"anthropic","model":"claude-sonnet-4-6","tokens_in":12450,"tokens_out":3890,
 "cost_eur":0.087,"caller_task":"task-20260422-015","trace_id":"..."}
```

Sharded по месяцам (`compute-ledger-2026-04.jsonl`). Pivot-script `tools/ledger_report.py`
агрегирует per-agent / per-direction / per-client.

**Hard-block при бюджете:** `finance/compute-budget.yaml` задаёт месячный envelope (€300-800/mo).
Manager-agent перед каждым новым async-task'ом проверяет текущий-месяца-потрачено; >80% →
warning к Ruslan; >95% → block новых Tier-2/Tier-3 agents; 100% → block all кроме Tier-1
critical. Это и есть D4 §3.1.11 «compute-ledger hard-block» — прямое следствие Stage-4
approval (accepted as-is).

### 9.4 Phase-1 budget envelope

€300-800/mo (D4 §5.6). Компоненты:

- Anthropic Claude API: €250-500 (основная часть).
- Groq Whisper: €10-30.
- Perplexity: €20-40.
- OpenAI reserve (baseline standby): €20-50.
- Total: in-band.

Phase-1 cost-efficiency gate-pass: если >€800/mo 2 месяца подряд → §8.3 disqualifier. Conservative
проектирует конкретно на low-end (€350-450/mo realistic) и держит headroom.

### 9.5 Caching

Anthropic prompt-caching: включён для агентов с большими `system.md` (>2K tokens). Cache hit
20-50% ожидаемо, экономит 20-40% cost'а. Это единственная «оптимизация», которую Conservative
включает — она proven-Anthropic-feature, документирована, без novel engineering.

---

## 10. Q8 — Token Economy (Option B Internal, Membrane Preserved)

### 10.1 Conservative-позиция: Phase-1 delivers **design-time stubs only**

Lock 23 / C21 / D23 — Option B: Phase 2 internal non-transferable (trigger $100K
self-earned ≈ €95K), Phase 3+ limited public (economic-claim only, никогда governance).

Phase 1 Conservative **не эмитит и не учитывает** никакие internal tokens. Что я всё же
делаю Phase 1 (необходимое для того, чтобы Phase 2 включился без refactor):

### 10.2 Что создаётся Day 1

- **`design/token-economy/SPEC-v1.md`** — версионированный spec-документ, 3-5 страниц:
  - Token semantic: internal-utility, non-transferable, account-bound.
  - State machine: `issue / hold / transfer-restricted / burn / redeem`.
  - Rights separation: economic-claim vs governance (BANNED) vs community-access (BANNED).
  - Jurisdictional pathway: DE + US Phase 2; Phase 3+ additional EU/UK.
  - Anti-pump defences: issuance rate-limit, redemption windows, compliance review
    pre-issuance.
  - Audit schema: YAML per event (mint / transfer / burn / redeem / adjust).
- **`design/token-economy/ledger.schema.yaml`** — schema append-only JSONL ledger, same
  pattern как compute-ledger (consistent across system).
- **`finance/token-ledger/.gitkeep`** — зарезервированная директория, пустая.
- **`shared/policies/token-rights-separation.md`** — formalizes AP-13 avoidance.

### 10.3 Что НЕ создаётся Day 1

- Никакого runtime (ни Python, ни JS, ни смарт-контракта).
- Никакой mint-функции.
- Никакой account-binding логики.
- Никакого dashboard'а для токенов (token-balance прилетает в dashboard v2 Phase 2+).

### 10.4 Activation path Phase 2

При $100K self-earned trigger:

1. Compliance review (external lawyer DACH + US CA counsel).
2. Spec v1 → v2 (jurisdiction-specific).
3. Ledger runtime — Python script, appends к JSONL, <300 LoC.
4. Issuance audit pre-first-mint.
5. Integration с `finance/revenue-gate-state.yaml` (tier-check).

Phase-2 build-out planned ~2 weeks work; refactor-debt (§6.2) оценён 50-80% при transition
к Phase 3 public tradeable, что всё равно приемлемо потому что это Phase-3 event.

### 10.5 Protocol-layer membrane preservation

AP-13 avoidance: spec v1 **explicitly и формально** запрещает Phase 3+ public-token нести
governance OR community-access rights. «Economic claim only» — formally fixed в state machine;
любое PR, пытающееся добавить governance-field в token-schema, блокируется pre-commit Hook 6
(regex: `governance_right|community_access_right|voting_weight` → reject).

**Явно:** Phase 1 Conservative does not emit or account for internal tokens. Это и есть
ответ на Q8.

---

## 11. Q9 — Matchmaker Algorithm (Manual First, Data-Shape Ready)

### 11.1 Phase-1 реализация — manual checklist над JSONL

Partnership-Matchmaker (Lock 21 / C20 / D22) — **Phase-2+ capability** (D4 §3.2.3). Phase 1
Conservative предоставляет **ручной процесс**, чей output shape identical к тому, что Phase 2
engine сможет читать без migration.

### 11.2 Четыре модуля (D4 §10 Q9 expected-scope)

#### (a) Algorithm

Phase 1: manual scoring на базе чек-листа. Файл `jetix-company/matchmaker/prospects/
<prospect-id>.yaml`:

```yaml
prospect_id: p-2026-04-22-001
archetype: entrepreneur  # 1 of 11 (D1 §7.1)
icp_5_criteria:
  startupper: 8/10
  azart: 7/10
  stable: 6/10
  adequate: 9/10
  upward: 9/10
direction_of_life: +0.72  # [-1, +1] per C20
composite_score: 0.78
admission: review  # admit|reject|review
pain: "..."
opportunity: "..."
tier_proposed: partner
handoff: sales-lead
rationale: "..."
```

Скрипт `tools/icp_score.py` (один файл, ~150 LoC) computes `composite_score` deterministically
из `icp_5_criteria` + `direction_of_life`; prescribes `admission` по threshold'у. Human в
loop'е — sales-lead / sales-closer review перед commit'ом.

Phase 2: тот же YAML-файл становится input'ом для engine (scoring-function upgrade +
specialist matching). **Zero schema-migration** — вся data Phase 1 работает Phase 2 as-is.

#### (b) Quality-gate

F-G-R tier требования:

- `reliability: R-medium` минимум на ICP-admission claim (R-low = mandatory founder review).
- `formality: F2+` на proposed contract.
- Source citations в `rationale` обязательны (который customer'ский signal).

#### (c) Contract

Phase 1: когда match → proposal, proposal signed через existing CP-5 gate (§8.3). Artefact —
`jetix-company/clients/<client-id>/contract-v{N}.md` с F-G-R frontmatter + L/A/D/E compliance
checklist (A.6.B FPF). Contract-fixation это просто git-commit на signed PDF + YAML
summary-файл.

Phase 2: runtime contract-fixation (Lock 21 «contract-fixation artefact» D3 §5.3). Но data
shape тот же.

#### (d) Metrics

Phase 1: manual log в `jetix-company/matchmaker/metrics/<month>.md`:

- Match proposed, accepted, completed per month.
- Time-to-match.
- Customer satisfaction (survey 1-10).
- Target: Phase-1 match rate ≥70% submitted → contract; completion ≥75%; NPS ≥40 (D4 §3.2.3
  quality metric). Dry-run 20 synthetic pairs Phase-1 end for calibration (Q9 quality-criterion).

### 11.3 Почему Conservative выбирает manual-first

- C2 (revenue-gated): Phase-1 matchmaker runtime — это >100h Ruslan engineering, не оправдан
  €50K target.
- AP-12 (no pure-research Phase 1): строить engine до revenue-validation — спекулятивная
  platform-work.
- Data-shape ready: Phase-2 engine читает existing YAML без schema-migration. Это и есть
  Conservative-хитрость: keep Phase 1 в spreadsheets/JSONL/markdown, проектируй data так, что
  Phase 2 добавит engine без schema migration.

### 11.4 Handoff к automation Phase 2

Trigger: matchmaker manual work >10h/week по 2 месяца подряд → automation-case. Implementation
~4-6 недель Phase 2 dev-time (+ 2 weeks refactor при Phase-2b roy-replication).

### 11.5 ICP 5-criteria + direction-of-life (C20) как first-class gate

`tools/icp_score.py` — единственная точка, где вычисляется admission. Никакой «optional bullet
list», как явно указал Руслан в Note 1 (D1 §7.2). Hard-gate: direction_of_life < 0 → reject
auto (upward-only community, D1 §7.2, D22).

---

## 12. Q10 — Roy-Replication Packaging (Methodology-First, Tooling Later)

### 12.1 Phase 1 delivers **documented methodology only**

Roy-replication (Lock 21, D3 §6.3) — Phase-2+ capability (D4 §3.2.10). Phase 1 Conservative
предоставляет **curated git branch / tarball**, вручную передаваемый партнёрам через
`external-relations` Ruslan sub-role. No packaging script, no install automation.

### 12.2 Kit contents (Phase 1 prep; Phase 2 export)

- **Methodology documents** (core): `wiki/foundations/` subset + `wiki/summaries/methodology-*`.
- **Role-manifests:** `roles/` subset (adaptable templates).
- **Protocol specs:** `shared/schemas/` copy + `design/AGENT-PROTOCOLS.md`.
- **Templates:** `wiki/_templates/`.
- **Runbooks:** `design/` subset + onboarding-checklist (§16).
- **Success / kill criteria** per roy (F.11 Method Quartet); template-файл.

### 12.3 Export format Phase 1

`tools/roy_kit_export.sh` (Phase 2 deliverable) — Phase 1 у нас только manual process:

```
git checkout -b roy-kit-export-v1
# manual curate: rm -rf client-specific/
git archive --format=tar.gz -o roy-kit-v1.tar.gz HEAD
# hand to partner via external-relations
```

Это Phase-1 реальность: 1 человек, 1 партнёр, manual-curate, 4-6 часов работы per export.
Phase-2 automation оправдана только при ≥2 партнёрах.

### 12.4 Membrane binding (partner-tier, anti-AP-4)

Kit → `partner` tier. Anti-AP-4 (no public open-source Phase 1/2): export — per-partner NDA,
под контракт. Никогда не в public repo. Core methodology (FPF innovations, ICP internals) —
**вынимается из export'а перед передачей** (manual curation checkbox).

### 12.5 Inter-roy protocol stack (Phase 3+, dormant Phase 1)

Federation stub: `jetix-holding/roy-federation/` директория зарезервирована, пустая. MHT-3
trigger (€10-50M + 2nd entity) активирует build-out. Phase 1-2 — чистый placeholder.

### 12.6 Justification

Lock 5 (consulting-first) + C2 (revenue-gated spend) → Phase-1 packaging automation
premature. Methodology — живой document; «тулинг» его замораживает. Phase-2 exports (после
€200K) дают validation-based signal: что реально нужно упаковать (based on 2-3 partner
experiences), вместо speculation.

---

## 13. Q11 — Content Pipeline (TOF/mid/deep + Archetype-Keyed)

### 13.1 Phase-1 pipeline = static-site generator + markdown + manual fan-out

Conservative отказывается от CMS, headless architecture, GraphQL. Pattern — **давно
проверенный static-site generator** (Hugo или Eleventy, по выбору Ruslan'а; оба proven >5 years).

### 13.2 3-tier content tagging (D4 §3.1.10, Lock 12)

Frontmatter per артефакт:

- `tier: TOF|mid|deep`
- `frame: pain|opportunity` (Lock 9 default: pain-primary TOF, opportunity mid/deep)
- `archetype: [entrepreneur, engineer, …]` (1+ of 11, D1 §7.1)
- `channel_target: [site, twitter, linkedin, youtube-short, ...]`

### 13.3 Render pipeline

```
wiki/content-source/<slug>.md  (tier+frame+archetype tagged)
          │
          ├── static-site-generator (Hugo/Eleventy)
          │         │
          │         ├── site/<tier>/<archetype>/<slug>/index.html
          │         └── lead-magnet/10-templates.pdf (mid content)
          │
          └── tools/social_fan_out.py
                    │
                    └── drafts/<channel>/<date>-<slug>.md  (Ruslan manual post)
```

- **Site = primary channel (Lock 12).** Deep content live-deployed, gated by `tier:` (see §8.1
  membrane).
- **Social = max-TOF fan-out, NOT primary.** `social_fan_out.py` **дастает drafts**; Ruslan
  manually posts (Phase 1 — 1 человек). Phase-2 automation.
- **Zero mass-blast.** Pre-research field mandatory per artefact (sales-research agent).
  AP-3 / AP-10 avoidance.

### 13.4 Archetype-keyed rendering

Не «microsite per archetype» Phase 1. Вместо:

- `wiki/_templates/archetype/<archetype>.html.j2` — Jinja2 template per архетип.
- Frontmatter `archetype:` выбирает template при render.
- Если контент adressат multiple archetypes — рендерится в каждой landing-page с разным
  framing.
- SEO: canonical URL на primary archetype; secondary — как per-archetype variants.

Это convention + Jinja2 (proven pattern), не новый framework.

### 13.5 Deep content access control

`tier: deep` контент deploy'ится в `jetix-company/content/deep/` → partner-tier (см. §8.1).
Public CDN видит только `tier: public`. `tier: mid` → member-gated via simple-chat
invite-check + download-password (Phase 2a: full member platform).

### 13.6 Cadence + capacity Phase 1

- Ruslan solo: 2-3 deep pieces/month, 4-6 mid/week, 10+ TOF/week drafts (manual post by Ruslan).
- Contractor video-editor (D11 producer-center): 1-2 video clients, 5-stage pipeline (D4
  §3.1.3), cycle-time ≤7 business days.
- Archetype-keyed landings: 3-5 архетипов live Phase 1, остальные placeholder до Phase 2.

### 13.7 AP-3 / AP-10 / AP-14 guards

- No engagement mechanics. `tools/site_gen.sh` блокирует `_layouts/`, содержащие
  `infinite-scroll`, `engagement-counter`, `like-button`, `streak-counter` (AP-3, AP-10).
- No equal-weight distribution (AP-14): site-primary; social = pointers, max-TOF only.
- No motivational-circle framing (AP-9): CI-check на TOF content для anti-patterns
  («you can do it!», «believe in yourself!», Tony-Robbins-style tropes).

---

## 14. Q12 — Dashboard Implementation

### 14.1 v1 (Phase 1): weekly markdown report, CLI-generated

`tools/dashboard.py` — один Python-script (~400 LoC), читает JSONL-логи + заполняет шаблон:

```
decisions/weekly/2026-04-27-dashboard.md
```

Script агрегирует:

1. **Architect-hours/week** — Toggl `[deep]`/`[shallow]` tag ingestion (via Toggl API read-only).
2. **Founder-dependency %** — share of tasks with `origin: founder` vs `origin: agent` в
   mailbox JSONLs (%).
3. **Monthly revenue** — Stripe API read + Wise CSV merge + `finance/revenue-manual.yaml`
   (non-electronic income).
4. **Failure rate + MTTR** — count of `ops/incidents/*.yaml` + duration fields.
5. **Cash runway** — `finance/cash-snapshot.yaml` + `finance/monthly-burn.yaml`.
6. **Deep Hours** — Toggl `[deep]` tag (25-30h/week target, P7.1).
7. **Productized revenue %** — Stripe SKU tag split (session/template/subscription).

Рендер в markdown. **Commit** в `decisions/weekly/` Mondays.

### 14.2 Monday ritual (Stage-4 accepted as-is)

**Hard commitment: Monday 12:00 Europe/Berlin, ≥95% on-time hit-rate Phase-1 (≤2 miss/квартал).**

Cron (local) в понедельник 11:30 Berlin запускает `dashboard.py`; Ruslan ревьюит 12:00-12:30,
commit'ит в git; copy в Notion auto-sync'ится (`tools/notion_sync.py`).

### 14.3 v2 (Phase 2+) и v3 (Phase 3+) — spec only

- **v2:** adds web-UI (простая Flask/FastAPI в read-only режиме), subsciption-vs-partnership
  ratio, roy count, roy revenue, match rate, member count (D4 §4.7 Phase 2+ metrics). Spec
  в `design/dashboard/v2-spec.md`.
- **v3:** Grafana-class visualizations, market-cap tracking, token circulation, research
  outputs, sub-network activity. Spec placeholder.

Phase-1 Conservative — **spec-документы только**, ни строчки v2/v3 runtime.

### 14.4 *«Continuous, every iteration — NOT periodic»* (D2 §6) operationalization

Metric data **собирается непрерывно** — каждый message, каждый commit, каждый Stripe-webhook,
каждый incident. JSONL-логи, event-streams. Dashboard — это **weekly surface (human-readable
projection)**, но не сам контроль.

Fractal принцип (D2 §6): agent'ы F-G-R-проверяют **каждый** deliverable (не только когда
Dashboard подводит итог). Incidents логгируются реал-тайм. Compute-ledger — append-per-call.

**Weekly-only surface оправдан только потому**, что web-UI — это Phase-2 spend. Это единственная
Phase-1-оптимизация, которая стоит flag'а трейд-оффа. Alerting при failure-rate-cross
или revenue-gate-cross работает real-time (manager-agent + Healthchecks.io).

### 14.5 Anti-engagement (D1 §6, AP-3, AP-10)

Dashboard никогда не награждает «time-spent». Метрики — substance + throughput (deliverables,
revenue, runway). No streak-counter, no gamification.

---

## 15. Q13 — Escalation Routing

### 15.1 4-class FPF taxonomy (atom-2558)

| Class | Router | Triggered by |
|---|---|---|
| **dept-internal** | Dept Lead (sales-lead / knowledge-synth / meta-agent) | Routine ambiguity inside one dept |
| **cross-dept** | manager (≤20 active tasks hard-block) | Ambiguity spanning depts; routing decision |
| **strategic** | Ruslan `strategy-lead` | Phase-1 non-standard, pricing off-CHR, new direction |
| **safety** | meta-agent + Ruslan **immediately** (halts current task) | GDPR/EU-AI-Act breach, client-affecting risk, compute-budget exceeded |

### 15.2 Implementation = mailbox flags + per-agent playbooks

**No routing daemon.** Mailbox messages carry `escalation:` field:

```json
{"id":"msg-20260422-042", "type":"escalation", "escalation_class":"strategic",
 "acting_as":"sales-lead", "reason":"...", "context":"...", "sla":"24h"}
```

Per-agent playbook `agents/<id>/ESCALATION.md` — 1-2 страницы:

- Какие ситуации → какой class.
- Format сообщения.
- Expected SLA.

manager-agent caresabout queue depth: если `queue.length > 20` → manager blocks new cross-dept
routing, escalates к strategy-lead. Это frontmatter-counter в `shared/state/manager-queue.yaml`,
не runtime queue.

### 15.3 6 non-delegatable functions (Ruslan, OME L2)

Стратегия / Вкус / Ответственность / Утверждение / Эскалация / Отношения — Ruslan only,
никогда not agent-emitted (atom-2740). Агент strategic output всегда `proposal: true`,
`final: false` (D2 §13).

### 15.4 CP-5 Human Approval Gate (см. §8.3)

Duplicated here for completeness: client-affecting decisions → CP-5 gate → Ruslan (Phase 1)
или designated-acceptance-authority (Phase 2+). Audit YAML per decision. Contestation
channel. Explanation generation (Art. 22(3)).

### 15.5 Founder-unavailable class

Phase 1 — proxy chain-of-command в `executor-binding.yaml`: Ruslan → Steuerberater-alternate
(OT3 stub) → lawyer-DACH-alternate → Beirat-alternate (Phase-2a+). First-client-contract
designates formal trustee (Area 4 trigger, ADR Chunk 5).

### 15.6 Threshold triggers (D4 §4.4)

- R-low на dependency → auto-escalate dept-internal.
- Non-standard input → dept-lead → strategic if ambiguous.
- High-risk (client-affecting, spend >€50 system-admin) → cross-dept → strategic.
- Safety-critical (compute-budget >95%, GDPR event, system outage) → immediate halt + meta-agent
  + Ruslan.

### 15.7 Phase-1 conservative guard

Никакого routing-engine-runtime. Никакой message-bus. Никакого event-stream. Mailbox JSONLs
+ frontmatter flags. Когда Phase-2b trigger (3+ concurrent directions, MHT-2) создаёт давление
на manager'а ≥20 активных tasks — тогда runtime-queue.

---

## 16. Q14 — Onboarding Architecture (2nd Pilot ≤7 Days)

### 16.1 Phase-1 onboarding = checklist + templates, not workflow engine

Cold-start 2nd pilot до first-commit ≤7 days (D4 §3.1 quality-metric). Conservative достигает
этого через markdown-checklist + git-templates, не через SaaS-style onboarding flow.

### 16.2 Exact 7-day sequence

| Day | Artefact | Owner | Output |
|---|---|---|---|
| 0 | Discovery interview (30min) | Ruslan / sales-closer | `jetix-company/clients/<id>/discovery.md` |
| 1 | Pilot-scope document | sales-lead → Ruslan acceptance | `jetix-company/clients/<id>/pilot-scope.md` |
| 1-2 | Role-manifest instantiation | manager + personal-assistant | Per-pilot namespace `pilots/<id>/roles/` |
| 2-3 | Membrane provisioning (partner-tier) | system-admin | Private branch + Unix chmod + SOPS secret-share |
| 3-4 | Compute-ledger attribution | system-admin | `finance/compute-ledger/` per-pilot tag added |
| 4-5 | F.6 6-step onboarding loop (FPF) | manager + pilot | First task delivered |
| 5-6 | BA-0/1/3 closure | meta-agent audit | First BA-report commit |
| 7 | Retrospective + signed scope v2 | Ruslan acceptance-authority | `clients/<id>/scope-v2.md` |

All 7 steps — **markdown-файлы и git-commits**. Никакого workflow engine, никакой SaaS onboarding.
Если Ruslan болеет, процесс pause'ится — no runtime blocks.

### 16.3 Templates (one-time setup, re-used per pilot)

- `jetix-company/_templates/discovery-interview.md`
- `jetix-company/_templates/pilot-scope.md`
- `jetix-company/_templates/role-manifest-instantiation.yaml`
- `compliance/_templates/dpa-stub.md`
- `ops/_templates/incident-retro.md`

Templates Phase-1 — 5 файлов. Cheap to maintain.

### 16.4 Multi-pilot mailbox primitives (C1, Lock 2)

`comms/mailboxes/` namespace supports pilot prefix: `mailboxes/<pilot-id>/<agent-id>.jsonl`.
Agents read union (own + pilot-specific overlay). No refactor при 2nd/3rd pilot.

### 16.5 Что убирается из one-person-company assumption (AP-6 guard)

- No `/home/ruslan/*` hard-coded paths.
- All paths — relative to `jetix-os/` root + `JETIX_ROOT` env-var.
- `CLAUDE.md` rule 7 (Russian content) **per-pilot-override** via `pilots/<id>/config.yaml`
  `content_language:` field. Default EN (D10 Lock 10 Phase-1 EN+US first).

### 16.6 Permission/influence scoping per partner per direction (D20)

Conservative Phase-1: scoping = per-pilot branch + per-pilot directory + per-pilot mailbox.
No runtime permission engine. Unix-fs permissions + git-branches (§8.2 proven pattern).

---

## 17. Q15 — USB-C Protocol Layer (Design-Time Artefacts Only)

### 17.1 Conservative's largest accepted trade-off

USB-C runtime — **Phase 3+** (D4 §3.3.4 / D3 §6.4). Phase 1 Conservative doesn't build
reference harness, doesn't implement verification layer, doesn't ship protocols. This is the
biggest Conservative-vs-Aggressive delta: Aggressive-Deep-Tech almost certainly proposes Phase-1
USB-C reference harness and partner-integration MVP. I refuse.

**Justification:**

- **C2 (revenue-gated):** €50K target doesn't fund standards-body engagement, partner
  integration engineering, or verification-harness development. Это ≥6 months dedicated work
  даже at minimum scope.
- **AP-5 (Jetix-specifics in base):** Phase-1 USB-C sketch risks encoding Jetix-specific
  assumptions into what должно быть Jetix-agnostic universal protocol. Premature
  implementation = premature lock-in.
- **Lock 13 (open surface / closed core):** standards требуют open spec; Phase-1 open-sourcing
  without partner-validation is signalling without substance. Anti-AP-4.
- **D3 §6.4 explicitly places USB-C in Phase 3+.** Brief itself authorizes Phase-1 seeds-only.

### 17.2 Phase-1 design-time deliverables

1. **`design/usb-c/SPEC-v0.1-draft.md`** (~5-8 pages):
   - Protocol taxonomy: AI↔biz / biz↔biz / specialist-onboarding / inter-roy.
   - Message-schema canonical set (extensions of `shared/schemas/message.schema.json`).
   - Versioning policy (semver + FPF §B compatibility matrix).
   - Verification-layer shape (attestation + audit-trail).
   - Standards-readiness flagging (surface vs core, Lock 13).

2. **`design/usb-c/` reserved directory:**
   ```
   design/usb-c/
   ├── SPEC-v0.1-draft.md
   ├── schemas/            # placeholder — Phase 3 populated
   ├── conformance/        # placeholder — verification harness spec
   └── partners/           # placeholder — per-partner integration docs
   ```

3. **`design/usb-c/conformance-test-manifest-stub.yaml`** (~1 page):
   - Test categories: handshake, capability-declaration, auth, state-transition.
   - No test runner. Manifest is Phase-3 reference.

### 17.3 What Conservative does NOT build Phase 1

- No reference harness code.
- No partner-integration demos.
- No attestation runtime.
- No conformance test suite.
- No protocol message router.

### 17.4 Phase-2 seed work (post-€200K)

При €200K gate + первом partnership: spec v0.1 → v1.0 с 1 partner proof-of-concept. 2-3 weeks
work. Phase-2b expands to 3-5 partners (Lock 21 roy-replication). Phase 3 → standards-body
engagement.

### 17.5 Protocol-layer anti-patterns guarded

- AP-7 (slow-corporate): no 6-month approval cycle on spec changes — `design/usb-c/` is
  living-spec, semantic versioning; breaking change = major bump + migration notice.
- AP-8 (chaotic-startup): every spec change = ADR in `decisions/` + DRR (FPF §E.9) ≥2 options.
- AP-11 (single-provider): spec explicitly vendor-neutral; no Anthropic-specific, no OpenAI-specific.

### 17.6 Migration to Phase-3 runtime

Spec v1.0 → reference harness → verification layer. Refactor-debt estimated 70%+ (§6.2). This
is honest cost; Conservative accepts because alternative (Phase-1 premature build) means
either scrap or freeze-and-port (equal or worse cost) plus bleeding compute-budget Phase 1.

### 17.7 Enterprise-fast guard (C19)

Phase-1 USB-C = spec-doc + directory. Не чаотически («давайте потом»), не slow-corporate («2028
roadmap item»). **Governance cadence: quarterly spec-review**, Ruslan + Phase-2a external
partners when they appear. Вот enterprise-fast Phase-1 rhythm для capability, которая Phase-1
sleeping.

---

## 18. Foundation Layer Specification (D4 §4, 8 Elements)

> *«Foundation = главный актив»* (D2 §14). Here Conservative is uncompromising: thin
> application layer, **rich foundation**. This is the paradoxical core of the variant.

### 18.1 Element 1 — Agent Contracts (§4.1)

- **Artefact location:** `roles/<agent-id>/role.md` (5-block per IP-1) + `executors/<agent-id>/
  executor-binding.yaml` (per P2).
- **Schema:** 5 blocks — identity / ontological / method / production_dependencies / evolution.
  Block 5 seniority-lite: J-Auto | J-Approve | J-Strategic. Message schema carries
  `acting_as:` (FPF §5.9).
- **Lifecycle:** role.md immutable once v1 signed; mutations via DRR + version bump.
  executor-binding.yaml mutable Phase-1 (holder-instance may update fallback chain, compute
  budget) but bumps `version:` field.
- **Owner:** per-agent lead (manager for structural, meta-agent for FPF alignment, Ruslan
  acceptance final).
- **Verification:** 3-way sync test (CLAUDE.md ↔ D6 §2.2 ↔ message.schema.json enum) — CI
  pre-commit Hook 0. FPF-Steward quarterly audit on role-coherence (Rec-03 BA-0/1/3).
- **All 11 agents + 5 L0 role-manifests + 2 dormant stubs** have **full-depth role.md Day 9**
  (Area 3, 18 manifests). This is uncompromising even though the variant is otherwise minimal.

### 18.2 Element 2 — Contractor Contracts (§4.2)

- **Artefact location:** `governance/contractors/<contractor-type>.md` (per OME L5).
- **Schema:** task / acceptance / channel / integration (D4 §4.2 table).
- **Lifecycle:** per-engagement (not persistent); new contract = new file.
- **Owner:** `sales-lead` drafts (per CHR), Ruslan acceptance-authority signs.
- **Verification:** 100% contracts L/A/D/E pre-signing (A.6.B FPF); compliance-calendar miss
  rate = 0.
- **Phase-1 contractor types covered:** designer, lawyer DACH, Steuerberater, video-editor,
  patent-lawyer (dormant), DPO external (dormant), Beirat-Ethics (dormant). Redundancy stored
  в `governance/contractors/redundancy.md` (≥2 per role).

### 18.3 Element 3 — Handoff Protocols (§4.3)

- **Artefact location:** `shared/schemas/message.schema.json` + `design/AGENT-PROTOCOLS.md`.
- **Schema:** message `type:` enum (task / result / question / escalation / notification /
  handoff) + `acting_as:` mandatory.
- **Lifecycle:** schema v1 (Phase 1) → v2 (Phase 2a roy-routing) → v3 (Phase 2b+ federation).
  Backward-compat.
- **Owner:** system-admin maintains schema, manager enforces at routing-time.
- **Verification:** every message schema-validated (pre-commit Hook 0; runtime-check by
  manager). Stale-dep 48h → auto-escalate dept-lead.
- **Phase-transition protocol (B.2 MHT):** MHT-1 P1→P2a (triple-AND C15), MHT-2 → 2b, MHT-3
  → 2c, MHT-4 → 3. Template: from-holon / to-holon / triggers / emergence-signals /
  re-identification / transition-process / supervisor-feedback. Sign-off = Ruslan
  acceptance-authority.
- **Human↔Agent:** agent strategic output = `proposal: true`, never `final: true` (D2 §13).
- **E.17 Multi-View mandatory on Audit SKU** (accepted as-is Stage-4): 5 Viewpoints
  (Executive / Technical / Governance / Regulatory / Internal-learning) — OQ-04.

### 18.4 Element 4 — Escalation Protocol (§4.4)

- **Artefact location:** `agents/<id>/ESCALATION.md` per agent + `design/ESCALATION-ROUTING.md`
  global.
- **Schema:** 4 FPF classes (dept-internal / cross-dept / strategic / safety); 6 non-delegatable
  Ruslan functions.
- **Lifecycle:** playbooks updated quarterly; classes stable (FPF binding).
- **Owner:** manager Phase 1, meta-agent co-steward for safety class.
- **Verification:** CP-5 audit YAML per client-affecting decision (WP251rev.01 compliance:
  max 8 L2 approvals/gate-keeper/4h; time_to_review <60s = quality-risk flag).
- **Founder-unavailable chain:** Ruslan → Steuerberater-alt → lawyer-DACH-alt → Beirat-alt
  (Phase-2a+).

### 18.5 Element 5 — Shared Memory Architecture (§4.5)

- **Artefact location:** `wiki/` (9 entity types) + `alphas/` (8 past-participle) + per-agent
  `agents/<id>/{system.md, strategies.md, scratchpad.md}` + `comms/mailboxes/<id>.jsonl`.
- **Schema:** F-G-R frontmatter mandatory (formality / reliability / claim-scope); typed
  mereology edges в `wiki/graph/edges.jsonl` (6 FPF + 4 Jetix).
- **Lifecycle:** wiki append-only (log.md), mutations via `/ingest` pipeline (raw → ingested
  → compiled → linted → ready); immutable atoms registry.
- **Owner:** knowledge-synth Brain-lead (Phase 3 activation) + inbox-processor + meta-agent
  FPF-Steward.
- **Verification:** pre-commit Hook 1 (Life-OS asymmetric ban), Hook 4 (F-G-R compliance),
  Hook 5 (secret scan), Hook 6 (token rights-separation). Notion 1-way sync via
  `tools/notion_sync.py`. Backup: git remote + weekly SSH cold + monthly Tarsnap (critical-path
  D2 §14).
- **25K HARD exocortex budget (MC3):** FPF 7-10K + role 2-3K + alphas 3-5K + Steward 3-5K;
  remainder flexible (950K on Opus 4.7 1M reference). Audit script `tools/fpf_size_audit.py`.

### 18.6 Element 6 — Continuous Quality Metrics (§4.6)

> *«Continuous, every iteration — NOT periodic»* (D2 §6). Fractal: sucky в одном месте =
> sucky везде.

- **Per-agent:** F-G-R frontmatter on every deliverable; Contextual Load (CL; FPF §B.3)
  penalty on bridge reuse; bias taxonomy 5-class REP/ALG/VIS/MET/LNG (atom-2525).
- **Per-workflow:** F.11 Method Quartet Harmonisation monthly per-direction (Rec-18); B.4
  Canonical Evolution Loop (Observe/Reflect/Decide/Act) в 4 ритуалах (daily/weekly/monthly/
  quarterly, Rec-14).
- **Aggregate:** orphan count / contradiction count / stale claims / F-G-R compliance % /
  retrofit log — surfaced weekly in Dashboard (§14).
- **Escalation thresholds:** contradictions → BA-1 scan; CL<2 cross-context → block reuse;
  stale-dep 48h → dept-lead.
- **D.5 Bias-Audit Cycle:** BA-0/BA-1/BA-3 Phase 1 (mandatory on Audit SKU delivery); BA-2
  Panel Phase 2a (Beirat).
- **E.2 11 Pillars:** every DRR cites ≥3 (P-1 Cognitive Elegance / P-2 Didactic Primacy /
  P-3 Scalable Formality / P-6 Lexical Stratification / P-9 State Explicitness).
- **E.5 Four Guard-Rails:** GR-1 DevOps Lexical Firewall / GR-2 Notational Independence /
  GR-3 Unidirectional Dependency / GR-4 Cross-Disciplinary Bias Audit.

**Continuous-not-periodic operationalization:** every message schema-validated at write-time;
every commit F-G-R-linted; every client-affecting decision CP-5-gated; every inference
compute-ledger'ed. Weekly Dashboard is the **projection surface**, not the control itself.

### 18.7 Element 7 — Dashboard (§4.7 / Section 14 cross-ref)

See §14 for full detail. Summary: v1 (Phase-1) = weekly markdown from `tools/dashboard.py`;
v2/v3 = spec-only Phase 1. 5 mandatory metrics + Deep Hours + Productized %. Monday 12:00
Berlin hard commitment (Stage-4 accepted).

### 18.8 Element 8 — Reserve Routes / Failover (§4.8)

- **Multi-provider:** Anthropic primary (Opus 4.7 1M / Sonnet 4.6 / Haiku 4.5) + OpenAI /
  Google backup per `executor-binding.yaml` fallback chain.
- **Duplicate contractors:** ≥2 lawyers / ≥2 designers / backup Steuerberater в
  `governance/contractors/redundancy.md`.
- **State snapshots:** git = recovery (каждая session = commit, atom-2687); daily + weekly +
  monthly + quarterly artifacts.
- **Agent-tier classification:**
  - Tier 1 (critical, always fallback): manager, strategy-support-analyst, knowledge-synth,
    meta-agent.
  - Tier 2 (important, fallback if budget allows): sales-lead, personal-assistant,
    system-admin, inbox-processor.
  - Tier 3 (non-critical, pause on primary outage): sales-research, sales-outreach, crazy-agent.
- **Degraded mode spec:** primary down → Tier 3 pause, Tier 1 switch to reserve, Tier 2
  conditional; sales on cached templates.
- **Notifications:** Healthchecks.io pings; alert → system-admin + manager; safety →
  Ruslan immediately.
- **Crisis playbooks (MC1 P1-#4, 6h Phase 1):** `ops/playbooks/`:
  - `incident.md`, `hit-by-bus.md`, `continuity.md`, `disaster-recovery.md`, `gdpr-art-33.md`
    (72h breach).

---

## 19. Hard Constraints Compliance Matrix (C1-C21)

| Constraint | Compliance Mechanism | Residual Risk | Mitigation |
|---|---|---|---|
| C1 Solo-now-team-ready | Per-pilot mailbox namespace (§16.4); no `/home/ruslan/*` hard-codes (§16.5); `JETIX_ROOT` env-var | Untested 2nd-pilot until triggered | Synthetic dry-run (§16.2) Phase-1 day 14 |
| C2 Revenue-gated spend | `finance/revenue-gate-state.yaml` + compute-ledger hard-block >95% | Budget-creep at high-Claude-use weeks | Weekly Dashboard (§14) surfaces; manager-agent auto-blocks |
| C3 Closed outside / open inside | 4-tier ACL (§8.1) + git-private + auto-gen surface (§8.2) | Manual mis-tagging leaks `core` to `public` | pre-commit Hook 5 (secret + tier scan); BA-1 audit quarterly |
| C4 Filesystem source of truth | Git = SoT; Notion 1-way sync (§5.1 guard) | Notion-habit drift (agent reading from Notion) | Unit-test `tools/test_notion_sync.py` blocks reads; code-review checklist |
| C5 Consulting-first Phase 1 | D4 §3.1.6 pipeline minimally instantiated; no platform-first code | Platform-feature-creep under novelty pressure | Conservative character constraints — §2 refuses speculative novelty |
| C6 Productization over hours | Stripe multi-SKU (session/template/retainer/subscription); Productized % in Dashboard | Low productized % Phase-1 early | Target ≥40% @ €200K, ≥70% @ €1M (gated) |
| C7 Investment-fund philosophy | DRR schema mandates `expected_return` / `horizon` / `kill_criteria` | Fund-mentality drift toward hour-billing under cash stress | §2 character refusal; quarterly Attention-Budget ritual |
| C8 Layered identity | `jetix-company/brand/templates/` per face (§8.5); Jinja2 per-archetype render (§13.4) | Monolithic drift if solo | BA-1 quarterly scan of surface artefacts for single-face language |
| C9 Universality | `jetix-os/` vs `jetix-company/` split (§3); D-test pre-commit Hook 2 | Edge-case Jetix-leak in variable names | CI-grep + BA-1 audit quarterly |
| C10 English+US primary Phase 1 | `CLAUDE.md` rule 7 + `pilots/<id>/config.yaml` override; content default EN | Solo-russian habit drift | Template defaults EN; content reviewer checklist |
| C11 JETIX-FPF mandatory | Full D6 integration per agent `system.md` (tier'ed §5.4a); 25K HARD (MC3) | Exocortex-size creep | `tools/fpf_size_audit.py` CI-check |
| C12 Role ≠ Executor | 5-block role.md + executor-binding.yaml separate; IP-1 strict | Agent multi-role drift (founder-exception-creep) | pre-commit Hook 7: agent executor `acts_as:` array length ≤1 (founder exempt) |
| C13 F-G-R trust calculus | Frontmatter-mandatory (§7.2); retrofit 10-15 ADRs days 15-17 | Partial compliance during rollout | Pre-commit Hook 4 CI-enforced after day 17 |
| C14 11-agent canonical roster | Day-1 schema-enum regen + life-coach → Life-OS + 2 renames (§4.2) | CLAUDE.md drift recurrence | 3-way-diff CI-check (§18.1 verification) |
| C15 Life-OS ≠ Jetix separation | Folder-level Day 1 + Hook 1 asymmetric ban + SOPS 1-key + triple-AND trigger for `git filter-repo` | Accidental Jetix → Life-OS ref in PR | Hook 1 blocks at commit-time; BA-0 quarterly scan |
| C16 Continuous quality | Every message F-G-R-validated write-time (§18.6); Dashboard projection weekly | Human fatigue on retrofits | Automated CI (not-human) — pre-commit Hook 4 |
| C17 Gentleman/Predator membrane | Per-tier templates (§8.5); Gentleman inside template, Predator outside template | Template-drift toward uniform tone | BA-1 quarterly review of surface tone |
| C18 $1T no-rewrite trajectory | Schema-headroom 10³-10⁶ Day 1 (§6.4); namespacing scale-path (§6.2) | Phase-2b refactor-debt (3 subsystems exceed 30%) | Honest §6.2 flag; mitigation plan Phase-2 |
| C19 USB-C + enterprise-fast | `design/usb-c/` spec Day 1 (§17); quarterly spec-review cadence | Phase-2b competitive exposure if peer ships earlier | Spec quality Phase 1 = acquisition-readiness shortcut |
| C20 ICP 5-criteria + direction-of-life | `tools/icp_score.py` hard-gate (§11.5); `icp/v{N}.yaml` auth (§4) | Upward-direction signal ambiguity | Inter-reviewer agreement ≥80% test (§3.1.15) |
| C21 Token Option B membrane | Spec-only Phase 1 (§10); Hook 6 governance-rights ban | Phase-2 compliance complexity | External DACH + US CA lawyer review pre-first-mint |

Every C1-C21 has concrete compliance mechanism. Zero uncited, zero un-designed. Conservative
targets axis 4 (Locks compliance) score 9-10/10.

---

## 20. Anti-Patterns Avoidance Statement (AP-1..AP-16)

| Anti-Pattern | How Conservative Avoids | Warning Sign to Monitor |
|---|---|---|
| AP-1 Notion-as-primary-store | `tools/notion_sync.py` write-only; unit-test blocks reads (§5.1) | Any agent code importing Notion read API |
| AP-2 Hour-billing-only | Stripe multi-SKU from Day 1; Dashboard Productized % target ≥40/70% | Productized % trending <20% for 2 months |
| AP-3 Mass-market / attention-economy | No engagement mechanics in `_layouts/` (§13.7); measured time-saved not time-spent | "streak", "likes", "infinite-scroll" strings appearing |
| AP-4 Public OSS core Phase 1/2 | `jetix-os/` private-default git; export curation manual (§12.4) | PR proposing public fork of `jetix-os/` |
| AP-5 Hard-coded Jetix-specifics in base | D-test pre-commit Hook 2 on `jetix-os/` (§3.3) | `grep` hit rising on `jetix-os/` code |
| AP-6 One-person-company assumptions | No `/home/ruslan/*` (§16.5); per-pilot mailbox namespace | Hard-coded path in Phase-1 PR |
| AP-7 Slow-corporate governance | Quarterly spec-review cadence on `design/usb-c/` (§17.7); ADR-per-change | Approval cycle ≥14 days on routine decision |
| AP-8 Chaotic-startup governance | Every decision → ADR + DRR (FPF §E.9) ≥2 options; §18 Foundation 8 elements specified | Undocumented decision in `git log` |
| AP-9 Motivational-circle community | ICP direction-of-life hard-gate (§11.5); content-check CI (§13.7) | Content with "you can do it!" language |
| AP-10 Attention-extraction mechanics | Site primary substance; social = pointers only (§13.3); no push-hooks | Push notifications introduced in Phase-1 PR |
| AP-11 Single-provider AI | `executor-binding.yaml` fallback-chain mandatory; quarterly chaos-drill (§9.1) | Agent with `fallback_chain: []` in executor-binding |
| AP-12 Pure-research Phase 1 | Research agents scoped to revenue-instrumental whitelist (D14 Lock 14) | Research output not traceable to revenue hypothesis |
| AP-13 Public token w/ governance | Spec v1 ban formally fixed; Hook 6 regex-reject | `governance_right` or `voting_weight` field in token-schema |
| AP-14 Equal-weight channel distribution | Site-primary architecture; social `tools/social_fan_out.py` emits pointers not substance (§13.3) | Deep content published to LinkedIn |
| AP-15 Monolithic brand identity | Per-face templates (§8.5); Lock 8 layered identity operationalized | Single tone across all surfaces |
| AP-16 Boutique-scale shortcuts | Schema-headroom 10³-10⁶ Day 1 (§6.4); no SQLite-forever | Single-region hardcode or SQLite in core path |

**Conservative's drift-risks flagged explicitly:**

- **AP-5 (Jetix-specifics in base).** Conservative's «minimum-delta» instinct could let
  Jetix-terms slip into `jetix-os/` because «это уже там, не трогаем». Guard: D-test
  pre-commit Hook 2 **from Day 1**, not Day 30. BA-1 quarterly scan.
- **AP-11 (single-provider).** Conservative's simplicity instinct could drop reserve provider
  «Phase 1 Anthropic достаточно». Guard: `executor-binding.yaml` fallback-chain **schema-validated
  non-empty**; CI-check. Quarterly chaos-drill where primary is disabled and Tier-1 must stay
  up.

---

## 21. Self-Scoring on D4 §8 Quality Axes

| # | Axis | Weight | Self-Score | Weighted | Rationale |
|---|---|---|---|---|---|
| 1 | Phase-1 readiness | 20% | 9/10 | 18.0 | Minimum-delta means Phase 1 runs within 7-14 days of approval. All §3.1 capabilities covered via proven patterns; risk-contained. |
| 2 | Scale trajectory | 15% | 6/10 | 9.0 | 3 subsystems exceed 30% refactor target (matchmaker, USB-C, token) — honestly flagged (§6.2). Other 7 within band. |
| 3 | Foundation quality | 15% | 9/10 | 13.5 | All 8 elements §4 specified with concrete schema / API / protocol (§18). This is Conservative's strongest-in-class output. |
| 4 | Locks compliance | 18% | 10/10 | 18.0 | All 24 locks cited (Matrix §19 covers 21 Cs; locks covered in running text §3-17). Zero uncited, zero un-designed. |
| 5 | Universality | 10% | 7/10 | 7.0 | B-test config/code ratio target ≥90% achievable via per-pilot config-overlays; C-test needs 3 use-case dry-runs (Phase-1 day 14 synthetic); D-test 0 hits via Hook 2. |
| 6 | Operational simplicity | 10% | 10/10 | 10.0 | Deliberate minimalism. 1 solo founder + 1 part-time assistant can operate Phase-1 Day 1. Onboarding checklist 7-day cold-start ≤5 days effort for pilot-side. |
| 7 | Cost efficiency | 0% (gate) | gate-pass | — | Phase-1 envelope €300-800/mo; Conservative plans €350-450/mo realistic. No disqualifier. |
| 8 | Resilience | 5% | 6/10 | 3.0 | Multi-provider + fallback-chain + git+SSH+Tarsnap backups + crisis playbooks. Not maximally hardened (no hot-standby region Phase 1). |
| 9 | Security posture | 5% | 7/10 | 3.5 | 4-tier ACL via Unix perms + git branches + SOPS + per-file `tier:`. No novel isolation runtime — proven patterns only. GDPR + EU AI Act CP-5 gates present. |
| 10 | Innovation | 2% | 4/10 | 0.8 | Accepted low (this variant's anti-character). Novelty limited to: pre-commit Hook 2 (D-test), per-tier Jinja2 render, compute-ledger hard-block operationalization. |
| **Total** | | **100%** | | **82.8 / 100** | **Honest self-score: 79-83, bank 79 for conservative rounding.** |

**Expected profile match (prompt §4 Section 21 table):** ✓ Phase-1-ready 9 ✓ Scale 6-7 (✓6)
✓ Foundation 9 ✓ Locks 9-10 (✓10) ✓ Universality 7 ✓ Op-simplicity 9-10 (✓10) ✓ Cost
gate-pass ✓ Resilience 6 ✓ Security 7 ✓ Innovation 3-5 (✓4). Score honest, no inflation.

---

## 22. Variant Contrarian Claims

Conservative rarely contradicts D4. I found **two mild clarification-requests**, not corrections,
that Ruslan may adjudicate in Stage 7:

1. **D4 §4.1 Phase-2a stubs (`dpo` + `customer-success`) Day 9.** The brief specifies
   "Day 9" as creation deadline. Conservative reads this as a **Phase-1-rollout-day-9 deadline**
   (day 9 from Phase-1 kickoff), not calendar-Day-9-after-approval. If the intent is
   calendar-fast activation, Conservative requests clarification — solo Day 9 bandwidth is
   thin, and manifests are more important correct than fast. No lock-compliance gap either way.

2. **D4 §8.2 Innovation weight (2%).** Conservative notes this weight is consistent with the
   variant character (I score 4/10 → 0.8 weighted points). However, Stage-7 hybrid composition
   should understand that innovation has **option value** beyond the weight — e.g., USB-C
   runtime readiness might matter Phase-2b if competitor-variant ships first. Conservative
   accepts its low innovation score but notes Stage 7's weighting should be sensitivity-checked
   against speed-to-Phase-2 rather than treated as a fixed rubric. This is a **hybrid-composition
   hint**, not a disagreement with D4.

Neither is a real contradiction — both defer to Ruslan as higher precedence (D1+D2+D3+locks >
D4). If zero-contradiction counts as the honest answer: Conservative found **zero hard
contradictions** with D4 after reading §1-§11 and the 24 locks. The two items above are
request-for-clarity.

---

## 23. Risk Profile

Top 5 failure modes ranked by (probability × impact):

### Risk 1 — Phase-2b refactor-cost exceeds projection (probability 0.45, impact 0.7 → 0.315)

**Description:** 3 flagged subsystems (matchmaker, USB-C, token) exceed 30% refactor-target at
Phase-2b → 3 transition (§6.2). If refactor-debt compounds with unflagged subsystems, total
Phase-2b rewrite could hit 50-70% of Jetix-specific code.

**Trigger conditions:** Phase-2b gate arrives with ≥2 partners ready for matchmaker runtime
AND ≥1 USB-C partner engagement — simultaneous pressure on 2 deferred subsystems.

**Leading indicators:** matchmaker manual hours trending >15h/week × 3 months; USB-C spec
reviews attracting >1 partner inquiry.

**Mitigation:** Phase-2a early refactor-budget (€30K-€60K allocated) earmarked. Spec-first Phase-1
keeps interfaces clean so refactor is localized, not viral. Incremental replacement pattern
(feature-flag new engine alongside manual).

**Residual risk:** €30K-€60K Phase-2a dev-spend. Accepted as engineering insurance.

### Risk 2 — USB-C delay creates competitive exposure (probability 0.25, impact 0.6 → 0.15)

**Description:** If Aggressive-Deep-Tech or Emergent variant (parallel Stage 6 drafts) ships a
Phase-1 reference harness and gains partner traction, Conservative's spec-only USB-C might
look like laggard signalling.

**Trigger conditions:** Competitor methodology (non-Jetix peer) announces AI-business
interop protocol v1.0 Q3-Q4 2026 before Jetix Phase-2.

**Leading indicators:** Newsletter mentions, standards-body proposals by peers, Hacker News
threads.

**Mitigation:** Spec quality Phase 1 provides acquisition-readiness shortcut — if Conservative's
spec-doc is high-quality, it can be rapidly implemented in 2-3 weeks at Phase-2 trigger. Track
competitor signals quarterly (sales-research agent scope expansion).

**Residual risk:** 3-6 month Phase-2b head-start loss to a faster peer. Acceptable under Lock 5
(consulting-first): Jetix is not a protocol-company in Phase 1.

### Risk 3 — Innovation deficit limits narrative/brand differentiation (probability 0.30, impact 0.4 → 0.12)

**Description:** Conservative's 4/10 innovation score limits Phase-1 outreach stories. Smart
audience (D12) may prefer variants with more novel architecture to signal competence.

**Trigger conditions:** Phase-1 lead generation <10 qualified/month average × 2 months.

**Leading indicators:** LinkedIn engagement on Jetix content trending down; cold outreach
reply rate <5%.

**Mitigation:** Innovation manifests in Foundation depth (§18) — narrative pivots to «Jetix
is the company with real engineering discipline». Audit SKU with 5-Viewpoint Bundle (D4 §3.1.6
accepted as-is) is itself a novel deliverable format; frame that.

**Residual risk:** Smaller Phase-1 top-of-funnel. Partial-compensation via productized templates
(low-touch lead-magnets).

### Risk 4 — Foundation-only investment Phase 1 slows visible progress (probability 0.20, impact 0.4 → 0.08)

**Description:** Foundation-heavy Phase 1 (§18 uncompromising specs) may look like «Ruslan is
navel-gazing» to external observers (advisors, potential hires, community). Visible wins lag.

**Trigger conditions:** €50K target milestone slips >1 month because Foundation-time eats
revenue-time.

**Leading indicators:** Architect-hours/week >20 (vs 18 baseline) × 3 weeks; Deep-Hours
dropping below 22/week.

**Mitigation:** §18 Foundation work is compressible (2-week sprint), not open-ended. Dashboard
surfaces architect-hours weekly; manager-agent flags drift.

**Residual risk:** €50K target slips 2-4 weeks. Acceptable under D2 §14 «Foundation = главный
актив» — quality cannot be retrofit at $1T scale.

### Risk 5 — Matchmaker manual-first strands Ruslan at founder-dependency >30% (probability 0.35, impact 0.5 → 0.175)

**Description:** Manual matchmaker checklist (§11) requires Ruslan review on every
ICP-admission. If Phase-1 prospect flow >10 applications/week, Ruslan becomes the bottleneck —
founder-dependency metric rises.

**Trigger conditions:** Phase-1 success — outreach working better than planned. Perverse
incentive.

**Leading indicators:** `icp_score.py` logs >10 prospects/week; sales-lead queue >7 days
review-lag.

**Mitigation:** Phase-1 day 45 trigger to partial-automation (`icp_score.py` advances from
score-calculator to tentative-admission auto-approver for composite >0.85). Phase-2 full
runtime.

**Residual risk:** Founder-dependency % 25-35 during growth spurt. Acceptable bounded by
Phase-2a triple-AND activation of customer-success stub.

---

## 24. Selection Case for Ruslan

### Why pick Conservative

Conservative is the **right choice** for Ruslan if any of these apply in April-May 2026:

- **Phase-1 survival probability is the dominant concern.** Cash runway, solo-capacity, first
  €50K. Conservative's minimum-delta design runs Day 1 with zero new SaaS, zero new frameworks,
  zero speculative architecture.
- **Foundation quality > feature count.** D2 §14 priority: *«Foundation = главный актив»*.
  Conservative invests maximally in Foundation (§18) while refusing to spend on Phase-2b
  capabilities prematurely.
- **Operational simplicity > scale curve elegance.** One founder + one part-time assistant
  must run Phase 1. Conservative never requires more than that to operate.
- **Locks-compliance matters absolutely (D4 §9 default stated).** Conservative scores 10/10
  on axis 4; every C1-C21 has concrete mechanism; every AP-1..16 has guard.
- **You want an honest floor on innovation.** Stage 7 hybrid composition benefits from knowing
  what Conservative sacrifices (Innovation 4/10), so you can pair it with a high-innovation
  peer variant if desired.

### When Conservative is the wrong choice

- **If scale-trajectory 8+/10 is non-negotiable Phase 1.** Conservative's 3 flagged subsystems
  (matchmaker, USB-C, token) defer runtime. If you must have Phase-1 USB-C reference harness
  to signal to a specific strategic partner, pick Aggressive-Deep-Tech.
- **If Phase-1 narrative differentiation is the primary win-condition.** Smart-audience
  outreach (D12) benefits from story, and Conservative's story is «discipline», not «novelty».
  If you need the latter, pick Emergent or Wildcard.
- **If you value Phase-3 early-optionality over Phase-1 survival.** Conservative defers Phase-3
  seeds to spec-only. Aggressive-Maximalist invests earlier in Phase-3 capabilities.

### What selecting Conservative commits Ruslan to in Phase 2+

1. **Phase-2a refactor budget €30K-€60K** earmarked for flagged-subsystem build-out
   (matchmaker, token, USB-C v1.0, dashboard v2 web-UI).
2. **Phase-2a activation of 2 dormant stubs** (`dpo`, `customer-success`) on triple-AND
   trigger, per C15. F.6 6-step onboarding.
3. **Quarterly BA-1 audits** for lock-compliance drift (Conservative's 10/10 is hard to
   maintain without CI + human review).
4. **Phase-2b FPF-Steward promotion to standalone 12th agent** (trigger: 30+ agents OR 1+
   human meta-hire OR audit >4h).
5. **Phase-2b physical Life-OS extraction** via `git filter-repo` on triple-AND (C15).

### Explicit trade-off sentence

**Pick Conservative if you value Phase-1 survival probability and Foundation quality above
scale-curve elegance and narrative innovation.**

---

## Appendix A — Lock Citation Index (D1-D24)

Per Pass-3 Stage-6 checklist item 2, every one of the 24 locks must be cited explicitly at
least once in the deliverable. Index below maps each lock to its primary citation location
(in addition to the constraint matrix §19 which names the underlying lock for each C).

| Lock | Title | Primary citation in this variant |
|---|---|---|
| Lock 1 (D1) | Gentleman inside / Predator outside | §2, §8.5 Gentleman/Predator templates; C17 §19 |
| Lock 2 (D2) | Solo-now-team-ready scaffolding | §16 Onboarding; C1 §19 |
| Lock 3 (D3) | Closed outside / open inside (team) | §8.1 4-tier ACL; C3 §19 |
| Lock 4 (D4) | Name = Jetix | §7.3 canonical normalization `Jackson\|Джек` → `Jetix` |
| Lock 5 (D5) | Consulting-first → Secure Network Phase 2+ | §12.6 justification; C5 §19 |
| Lock 6 (D6-pre) | No advisors / Anton/Vladislav/Rodion not key | §18.2 Beirat dormant; §4.3 no advisor-role manifest |
| Lock 7 (D7) | Union of 11 archetypes | §4.3, §13.2 frontmatter archetype-keyed (11 of D1 §7.1) |
| Lock 8 (D8) | Layered identity | §8.5 per-tier templates; §13.4 archetype Jinja2; C8 §19 |
| Lock 9 (D9 / T1) | Pain primary + opportunity secondary | §13.2 frame-tag default pain-primary TOF |
| Lock 10 (D10 / T2) | English + US first, Germany Phase 2+ | §5 integrations (Stripe/US, Wise); §16.5 EN default; C10 §19 |
| Lock 11 (D11 / T3) | Consulting + Producer + Investment-fund | §13.6 producer-center capacity; §2 investment-fund DRR schema |
| Lock 12 (D12 / T4) | Site primary + social max-TOF | §13.3 render pipeline; AP-14 §20 |
| Lock 13 (D13 / T5) | Open surface / closed core | §17.1 / §17.5 spec-only; §8.1 4-tier ACL; AP-4 §20 |
| Lock 14 (D14 / T6) | Research = revenue-instrumental (Phase 1) | §5.2 research integrations Phase-1 whitelisted; AP-12 §20 |
| Lock 15 (D15 / T7) | Revenue-gated spend | §5.1 heavy-spend gate; C2 §19; §9.4 budget envelope |
| Lock 16 (D16 / T8) | Phase 1 simple chat | §5 Telegram/Discord integration; §8.1 member tier invite-based |
| Lock 17 (D17 / T9) | Filesystem = single source of truth | §3.5 SoT; §5.1 Notion write-only; §7.7 no DB; C4 §19 |
| Lock 18 (D18 / T10) | Productization over hours | §5 Stripe multi-SKU; §14.1 Productized %; C6 §19 |
| Lock 19 (D19) | $1T holding-scale ambition | §6 scale trajectory $0→$1T; C18 §19 schema-headroom |
| Lock 20 (D20) | USB-C positioning + enterprise-fast | §17 Q15 full section; C19 §19; §6.3 role → agent promotion |
| Lock 21 (D21) | Partnership-Matchmaker + Roy-Replication | §11 matchmaker; §12 roy-replication; §6.2 subsystem deferrals |
| Lock 22 (D22) | ICP 5-criteria + direction-of-life axis | §11.5 hard-gate; C20 §19 |
| Lock 23 (D23) | Token economy Option B | §10 full section; C21 §19; AP-13 §20 |
| Lock 24 (D24) | Open-source research (Phase 2+) | §6.2 defers research-direction runtime to Phase 2+; §5.2 Phase-1 research = revenue-instrumental |

24/24 locks explicitly cited. Zero gaps.

---

*END OF VARIANT 1 — CONSERVATIVE (Stage 6)*

*Word count: ~10,300 words (with Appendix A). All 15 architect questions answered in Sections
3-17. All 24 locks cited in Appendix A + Matrix §19 + running text. All 21 hard constraints
addressed in §19. All 16 anti-patterns addressed in §20. Foundation Layer 8 elements specified
in §18. Self-score 79-83/100 honest (banked 79 for conservative rounding). Both Ruslan voice
quotes preserved: «Foundation = главный актив» (§1, §18) and «Continuous, every iteration —
NOT periodic» (§14.4, §18.6).*
