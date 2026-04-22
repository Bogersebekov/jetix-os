---
id: stage-6-variant-5-emergent
title: JETIX-ARCH-V5-EMERGENT — Stage 6 Variant 5 (EMERGENT / Trellis-Not-Cage)
date: 2026-04-21
stage: 6
variant: 5
variant-name: EMERGENT
status: draft
formality: F2
reliability: R-medium
claim-scope: jetix-stage-6-variant-5
character-tags: [trellis-not-cage, self-organization, protocol-rich, thin-governance,
                 decentralized-knowledge, structure-parameters, agent-driven-specialization]
binding: false
authority: variant-proposal
word_count_target: 8000-12000
self_score_est: 74
depends_on:
  - decisions/JETIX-VISION.md (D1 APPROVED)
  - decisions/JETIX-PHILOSOPHY.md (D2 APPROVED)
  - decisions/JETIX-PLAN.md (D3 APPROVED)
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 APPROVED)
  - decisions/STAGE-3-APPROVAL.md
  - decisions/STAGE-4-APPROVAL.md
  - design/JETIX-FPF.md (D6 constitutional)
  - raw/research/architecture-variants-2026-04-22/TENSIONS-{PRE-RESOLVED,RESOLVED,RESOLVED-STAGE-2B}.md
precedence: "D1+D2+D3+24 locks (D1-D24) > D4 > OME/FPF/ADR > wiki atoms"
---

# JETIX-ARCH-V5-EMERGENT — Stage 6 Variant 5 (EMERGENT)

> *«Проектируй пространство возможностей, а не сам результат. Построй шпалеру — дай растению вырасти.»*

---

## §1. Executive Summary

**Вариант 5 — Emergent** занимает угол карты вариантов с **минимумом предписанной иерархии и максимумом предписанных протоколов**. Его тезис: к $1T-траектории ведёт не проектирование каждого будущего решения Day 1, а **проектирование условий, при которых хорошие решения выкристаллизовываются из взаимодействия и собираются вовремя**. Это «трельяж, а не клетка» — шпалера задаёт границы, внутри которых рост свободен.

**Три самые отличительные архитектурные решения** (против вероятных профилей пяти других вариантов):

1. **Двухконтурная файловая структура.** `jetix-os/core/` (трельяж: FPF-контракты, мембрана, эскалация, hub-and-spoke, revenue-gates — жёсткие структурные параметры) + `jetix-os/emergence-surface/` (где паттерны кристаллизуются до промоушена: `claims/`, `capability-bids/`, `routing-traces/`, `protocol-candidates/`, `co-citation-graph/`). В Phase 1 каталогов меньше, чем у Conservative; гораздо меньше, чем у Maximalist — потому что у каждого нового каталога в Emergent должна быть **причина со стороны lock/constraint или criterion сходимости**, а не «на всякий случай».
2. **Capability-капсулы + протокол торгов для маршрутизации задач.** Каждый агент несёт `agents/{id}/capability-capsule.yaml` — декларация того, на какие задачи он претендует, с каким минимальным capability-score, с какими доказательствами (prior F-G-R-tagged hits). Менеджер (хаб) публикует задачу в пул; агенты биддят; менеджер утверждает победителя в пределах ≤20 активных задач (D6 §2.2). Специализация — паттерн, выкристаллизовывающийся из истории выигранных заявок, а не строка в иерархии папок.
3. **Децентрализованная запись в wiki + централизованная консолидация.** Каждый агент пишет claim-ы в `wiki/emergence-surface/claims/{YYYY-MM-DD}/{agent-id}/{claim-id}.md` с обязательным F-G-R Day 1 (emergence ≠ без качества; F-G-R — это **структурный параметр**, а не эмерджентная оптимизация). Ежедневно `knowledge-synth` прогоняет промоушен: стабильные ко-цитатные кластеры (≥3 независимых claim-а на одном концепте за 14 дней, каждый F≥4, R≥medium) графически восходят в `wiki/core/`. Типизированные рёбра (9 типов per A.14) **рождаются** из наблюдаемых паттернов ко-цитирования, дополняя ручные приоры.

**Честный компромисс.** Operational simplicity ≈ **9/10** (меньше предписанной структуры = меньше поддерживать), Innovation ≈ **8/10** (парадигма самоорганизации для соло-оператора — по-настоящему ново), Cost ≈ **PASS**. Phase-1 readiness ≈ **7/10** — скелет работает Day 1, но паттерны кристаллизуются за недели, не за дни. Foundation ≈ **7/10** — протоколы богатые, но энфорсмент распределённый (слабее, чем у Maximalist). Scale trajectory ≈ **6-7/10** — защищается тезисом «**структурные параметры ужесточаются с ростом**». Locks compliance ≈ **7-8/10** — напряжение C14 / C17 требует аргументации; она есть (§4, §8). **Итоговый estimate ~73-78/100.**

**Острейший риск.** *«На 4-й неделе эмерджентность ещё не закристаллизовалась, и поставка выглядит так, будто ничего не произошло».* Митигация — публичный signal-set (task-routing entropy, promotion rate, cadence variance) с порогами эскалации в §14, плюс обязательный seed-content в `core/` Day 1. Прогресс измеряется состоянием шпалеры + сигналами роста, а не объёмом вышедшего продукта Phase-1.

**Аргумент выбора.** Выбери Emergent, если веришь, что **$1T-устойчивость рождается из дисциплинированной самоорганизации внутри жёстких стен**, а не из предскаффолженной Day-1 поверхности; если готов инвестировать в **дисциплину измерения** (сигналы эмерджентности) вместо **дисциплины расширения** (Maximalist scaffold). *«Foundation = главный актив»* (D2 §14) — но в Emergent это означает: **шпалера и есть Foundation**.

---

## §2. Variant Character Statement

Эмерджентность в этом варианте имеет **рабочее определение**, а не метафорическое. Каждое утверждение «здесь возникает паттерн» обязано назвать **триаду**:

- **Структурный параметр** — что жёстко зафиксировано и эмерджентностью не трогается.
- **Наблюдаемый сигнал** — как мы увидим, что паттерн кристаллизуется (или дрейфует в шум).
- **Критерий сходимости** — какое пороговое значение сигнала запускает промоушен в `core/` или эскалацию к Руслану.

Если любое из трёх не названо — это не эмерджентность, это **дрейф**, а дрейф есть провал. Этот принцип — точка, в которой Emergent радикально расходится с «пусть система сама разберётся». Emergent никогда не говорит «сама разберётся»; Emergent говорит «внутри этой шпалеры при этих сигналах при этом пороге промоушен — иначе эскалация».

**Что я принимаю как компромиссы:**

- **Медленный видимый прогресс недели 1-4.** Паттерны ещё не накопились. Поставка в этом окне — шпалера + seed-content + сигнальная приборная панель. Это честный choice; его нельзя перекрыть.
- **Умеренная защита Locks-compliance.** C14 (11 агентов + hub-and-spoke) и C17 (мембрана) в Emergent требуют **отдельной аргументации**, а не тривиального соответствия. Аргументация в §4 и §8.
- **Задержка кристаллизации vs Maximalist-surface-ready.** Maximalist поставит Day 1 матчмейкер-каталог, роу-кит, стандарты-драфты. Emergent поставит **протокол появления этих артефактов** и пустые субстраты в `emergence-surface/`. Разница — в том, **что считается ценностью Phase 1**: готовая поверхность (Maximalist) или готовность эволюционировать (Emergent).

**Что я отказываюсь трогать:**

- **Lock 1 / C17 — Gentleman/Predator мембрана.** Мембрана — жёсткий структурный параметр. Внутри мембраны — Gentleman-режим: cooperation, emergence, bidding. На мембране и вне — Predator-режим: adversarial, контрактно-управляемый. Эмерджентность **никогда** не пересекает мембрану.
- **Lock 15 / C2 — revenue-gated spend.** Phase-гейты жёсткие. Никакая capability-капсула не может биддить работу, которая активирует Phase-2 subsystem в Phase 1. Проверка — на middleware, не на совести агента.
- **C11 — JETIX-FPF обязательна.** Capability-капсулы **расширяют** FPF role-manifest (блок 5 seniority-lite плюс bidding-metadata), **не заменяют**.
- **Lock 17 / C4 — filesystem = SoT.** Эмерджентность пишет на файловую систему (через `emergence-surface/`), не в эфемерную память и не в Notion.
- **AP-3 / AP-9 / AP-10 — никаких attention-economy механик.** Эмерджентность **структурная** (паттерны в графе взаимодействий), а не **поведенческая** (петли вознаграждения). Это различие будет заявлено ≥3 раз в документе.

**Воплощение цитаты.** *«Foundation = главный актив»* (D2 §14) в Emergent означает: **шпалера и есть Foundation**. Набор жёстких структурных параметров (hub-and-spoke, мембрана, 4-class эскалация, FPF-контракты, revenue-gates, capability-capsule схема, протокол торгов, правила промоушена, F-G-R дисциплина, reserve-routing дерево) — это тот фундамент, который Русану терять нельзя. Растение может отрасти заново; шпалера не может. Пекись о трельяже, терпи к растению.

---

## §3. Answer to Q1 — Repository Layout (trellis + emergence surface)

### §3.1 Каталог верхнего уровня (Phase-1, single-repo)

```
jetix-repo/
├── jetix-os/                          # universal kernel (base — domain-agnostic)
│   ├── core/                          # — ШПАЛЕРА (hard structure parameters) —
│   │   ├── fpf/                       #   FPF-контракты, 11 pillars, GR-1..4, alphas
│   │   ├── roster/                    #   11 канонических агентов (C14); ссылки на manifests
│   │   ├── capability-capsule/        #   schema + bidding-protocol spec
│   │   ├── escalation/                #   4-class taxonomy (atom-2558); CP-5 gate schema
│   │   ├── membrane/                  #   4-tier ACL; Gentleman/Predator правила
│   │   ├── revenue-gates/             #   Lock 15 enforcement hooks (gate-state.yaml)
│   │   ├── promotion-rules/           #   emergence → core правила (thresholds, criteria)
│   │   └── reserve-routes/            #   failure_mode tree
│   ├── emergence-surface/             # — СЦЕНА РОСТА —
│   │   ├── claims/{YYYY-MM-DD}/{agent-id}/ #   ежедневные агент-claim-ы
│   │   ├── capability-bids/           #   bid-history (JSONL)
│   │   ├── routing-traces/            #   что кому ушло
│   │   ├── co-citation-graph/         #   построенный из claims
│   │   ├── protocol-candidates/       #   кандидаты в USB-C (§17)
│   │   ├── boundary-drift-traces/     #   сигнал drift мембраны или dept-boundary
│   │   ├── content-cadence-traces/    #   публикационный ритм
│   │   ├── capsules/                  #   dormant capsules (dpo / customer-success)
│   │   ├── matchmaker/                #   Phase-2+ активируется после €200K gate
│   │   ├── roy-kit/                   #   пусто Phase-1; наполняется по мере стабилизации
│   │   └── token-economy/             #   spec only Phase 1 (§10)
│   ├── protocols/                     # rich protocol surface — канонические контракты
│   └── schemas/                       # shared JSON-Schema для core и emergence-surface
│
├── jetix-company/                     # overlay (Jetix-specific)
│   ├── icp/
│   ├── sales/
│   ├── finance/
│   ├── clients/{client-id}/           # per-client overlay
│   └── legal/
│
├── agents/{id}/                       # 11 канонических + 5 Ruslan sub-roles + 2 stubs
│   ├── role.md                        # 5-block FPF (P2, IP-1)
│   ├── executor-binding.yaml          # C12 separation
│   ├── capability-capsule.yaml        # ⭐ Emergent signature artefact
│   └── overlay/                       # agent-specific overlay (C9)
│
├── life-os/                           # C15 physical separation; Hook 1 asymmetric ban
│
├── wiki/                              # decentralised write-path (см. §7)
│   ├── core/                          #   promoted knowledge (append-only ethos)
│   │   ├── concepts/
│   │   ├── entities/
│   │   ├── topics/
│   │   ├── foundations/
│   │   └── summaries/
│   └── graph/edges.jsonl              #   typed edges (6 FPF mereology + 3-4 Jetix)
│
├── comms/mailboxes/*.jsonl            # JSONL mailboxes per agent (CLAUDE.md)
├── decisions/                         # ADR + DRR
├── raw/                               # ingestion staging
├── .pre-commit-config.yaml            # 4 базовых blocking hooks (§3.3)
└── CLAUDE.md
```

**Почему это СКУДНЕЕ Conservative в Phase 1.** Каталоги, которые Maximalist скаффолдит Day 1 (`matchmaker/` с алгоритмом, `roy-kit/` с шаблонами, `token-economy/` с леджером, `protocols/standards-draft/` с пустыми RFC-шаблонами) в Emergent **физически существуют как пустые подкаталоги** внутри `emergence-surface/`, и они становятся наполнены **только когда сигнал эмерджентности достигает порога промоушена** (см. §3.3 правила). Никакой преждевременной иерархии. Каждый новый каталог верхнего уровня обязан сослаться на lock/constraint/criterion сходимости, который форсирует его существование Day 1.

### §3.2 Base/overlay separation (C9 Universality)

- **Base = `jetix-os/core/` + `jetix-os/emergence-surface/` + `jetix-os/protocols/` + `jetix-os/schemas/`.** Ни одного Jetix-специфического имени. D-test (grep `Jetix|DACH|Mittelstand|AI consulting` на `jetix-os/`) → **0 попаданий** (hook в CI).
- **Overlay = `jetix-company/` + `agents/{id}/overlay/`.** Всё Jetix-специфичное живёт здесь. При репликации кита (§12) копируется base + **пустой overlay-шаблон**; новый домен наполняет `jetix-company-<roy>/`.

### §3.3 Четыре blocking-hook-а Phase 1 (минимальный набор)

Emergent **принципиально** держит набор блокирующих хуков меньше, чем Deep-Tech (там 7). «Богатые протоколы, тонкая энфорсмент-поверхность» — хуки контролируют только то, что ни при каких условиях не должно дрейфовать.

```yaml
# .pre-commit-config.yaml — Emergent Phase-1 set
hooks:
  - id: hook-1-asymmetric-lifeos    # Jetix → Life-OS BLOCKED [C15]
  - id: hook-2-membrane-tier-cross  # partner-core linking from public → reject [C17]
  - id: hook-3-fgr-on-claims        # claims/*.md must have f_g_r [C13]
  - id: hook-4-acting-as-required   # mailbox messages must have acting_as [D6 §5.9]
```

Другие инварианты (GR-3 унидиректность, past-participle имён alpha, символический D-test) **в Emergent проверяются не хуком, а сигналом**: meta-agent в ежедневном проходе сверяет commit-лог против инвариантов и флагит аномалии на `emergence-surface/boundary-drift-traces/`. **Эмерджентная дисциплина = наблюдение, не принуждение** там, где принуждение слишком дорогое в сопровождении для Phase 1 соло-оператора.

### §3.4 Правила промоушена (ключевой artefact `core/promotion-rules/`)

Пример — `core/promotion-rules/concept.yaml`:

```yaml
promotion_rule_id: surface-to-core-concept
applies_to: wiki/emergence-surface/claims/**/*.md
target: wiki/core/concepts/{concept-slug}.md
structure_parameter:
  - "minimum 3 independent claims pointing at the same concept"   # [hard]
  - "F-G-R floor per claim: F>=4, R>=medium"                       # [D6 §4.2]
  - "span >= 14 days (not same-day noise)"                         # [D.5 BA window]
  - "from >= 2 distinct agents (not single-agent repetition)"
observable_signal:
  - co_citation_density_14d >= 0.35   # normalized graph density
  - f_g_r_median F = F2, R >= medium
  - claim_count >= 3
  - agent_diversity >= 2
convergence_criterion:
  - "signal holds for 48 consecutive hours (stability check)"
  - "no contradicting counter-claim at R-high or above"
action_on_convergence:
  - "knowledge-synth drafts a core/concept/{slug}.md merging citations"
  - "open DRR for Δ-1 review (D6 §12.14); merge on approval"
action_on_divergence:
  - "after 30d if criteria not met AND claims static: meta-agent escalates; Ruslan decides archive or tighten"
```

**Триада выполнена.** Это — прототип каждого будущего правила промоушена; шаблон повторяется для entities, topics, summaries, edges. Правила — часть `core/`, то есть **они сами не эмерджентны**. Меняются через DRR + подпись Руслана как framing-lead.

### §3.5 Мембранная реализация в директориях

```yaml
# jetix-os/core/membrane/tier-map.yaml
tiers:
  public:   {dirs: ["surface/", "public/"],   link_rule: "can_link_to: [public]"}
  member:   {dirs: ["members/"],              link_rule: "can_link_to: [public, member]"}
  partner:  {dirs: ["jetix-company/clients/*/"], link_rule: "can_link_to: [public, member, partner]"}
  core:     {dirs: ["jetix-os/core/", "wiki/core/foundations/"], link_rule: "can_link_to: [*]"}
enforcement:
  - hook-2 pre-commit (public→partner/core link = BLOCKED)   # [hard]
  - meta-agent daily trace audit on emergence-surface → reports drift (signal)
```

Мембрана — **hard, never-emergent**. Gentleman-поведение живёт **внутри** `partner/` и `member/`; Predator-контракты живут **на** membrane-переходах.

---

## §4. Answer to Q2 — Agent Roster + Capability Capsules

### §4.1 Канонические 11 агентов (C14 — нерушим)

Точное соответствие D6 §2.2. Никакой инфляции, никакого 12-го агента через «эмерджентность капсул».

| # | Agent | Dept | Model | Phase | J-level | Базовая capability-capsule |
|---|---|---|---|---|---|---|
| 1 | `manager`                   | MGMT  | Sonnet 4.6 | 1 | J-Approve (cross-dept) | `routing.capture`, `budget.≤20-active` |
| 2 | `personal-assistant`        | OPS   | Haiku 4.5  | 1 | J-Auto   | `scheduling.*`, `inbox.triage-light` |
| 3 | `system-admin`              | OPS   | Haiku 4.5  | 1 | J-Auto / J-Approve (spend) | `infra.*`, `secrets.rotate` |
| 4 | `sales-lead`                | Sales | Sonnet 4.6 | 2 | J-Approve (in CHR)     | `sales.propose`, `sku.pricing-in-CHR` |
| 5 | `sales-research`            | Sales | Haiku 4.5  | 2 | J-Auto                 | `icp.qualify`, `research.dossier` |
| 6 | `sales-outreach`            | Sales | Haiku 4.5  | 2 | J-Auto (templated)     | `outreach.templated`, `pre-research.enforce` |
| 7 | `inbox-processor`           | Brain | Haiku 4.5  | 2 | J-Auto                 | `triage.raw`, `voice.extract` |
| 8 | `crazy-agent`               | Meta  | Sonnet 4.6 | 2 | J-Approve (brainstorm) | `ideation.variants`, `cross-domain.bridge` |
| 9 | `knowledge-synth`           | Brain | Sonnet 4.6 | 3 | J-Approve (foundations)| `synthesis.promote`, `graph.consolidate`, `gardener.core` |
| 10 | `strategy-support-analyst` | MGMT  | Opus 4.6   | 3 | J-Approve (NEVER J-Strategic) | `options.memo`, `chr.kill-criteria` |
| 11 | `meta-agent` (+FPF-Steward) | Meta  | Sonnet 4.6 | 4 | J-Approve; halts on safety | `audit.trellis`, `bias.D5`, `safety.halt` |

**Не-агенты (только role-manifests):**

- **5 атомарных суб-ролей Руслана** (D6 §2.1): `strategy-lead`, `framing-lead`, `sales-closer`, `acceptance-authority`, `external-relations`. У каждой — своя capability-capsule (даже при недемонстрируемости), потому что капсула декларирует «что может эта роль», а не «когда она биддит».
- **2 dormant stubs (C14):** `dpo` (external-executor, активация при ≥1 GDPR DPA client), `customer-success` (J2, активация при ≥€20K MRR × 3mo). Capsules живут в `emergence-surface/capsules/`, промоутятся в `agents/{id}/` при пересечении J2-milestone × triple-AND trigger.
- **`life-coach`** физически в `life-os/` (C15); не в Jetix-enum.

Итого Day 1 manifest files: **11 + 5 + 2 = 18** (как и D4 §4.1).

### §4.2 Капсула — центральный Emergent-артефакт

```yaml
# agents/sales-lead/capability-capsule.yaml
capsule_id: sales-lead-v1
agent_id: sales-lead
role_manifest_ref: agents/sales-lead/role.md   # FPF 5-block, IP-1
home_department: sales
declared_capabilities:
  - task_shape: sales.propose
    capability_score_floor: 0.75
    evidence_sources:
      - wiki/core/summaries/sales-*.md      # prior successful proposals
      - wiki/emergence-surface/claims/*/sales-lead/*.md (last 30d, F>=2, R>=medium)
    cross_department_threshold: null        # home-dept — всегда
  - task_shape: content.strategy-frame
    capability_score_floor: 0.55
    evidence_sources:
      - wiki/emergence-surface/claims/*/sales-lead/framing-*.md
    cross_department_threshold: 1.3          # может биддить, если score >= 1.3× дефолтного
acting_as: [sales-lead]
fpf_bindings:
  pillars: [P-2, P-7, P-9]
  guard_rails: [GR-1, GR-3]
  alphas: [client, deal]
  bridges: [anthropic, stripe, notion]
fgr_declaration:
  max_formality: F3
  default_reliability: R-medium
  bias_audit_classes_covered: [REP, ALG, LNG]
escalation_classes_used: [dept-internal, cross-dept, strategic]
bid_policy:
  budget_cap_per_week: "20% манджер-attention-budget"
  no_bid_categories: [safety, strategizing]   # NEVER [C11, D6 §5.10.4]
compute_tier: "sonnet-default; opus-on-request-ruslan"
promotion_signals_contributed_to:
  - task_routing_entropy (via bid log)
  - capability_match_score_distribution (via score-per-task)
  - department_boundary_drift (cross_department_threshold hits)
```

**Structure parameter**: `home_department`, `capability_score_floor`, `cross_department_threshold = 1.3×`, `acting_as`, `bid_policy.no_bid_categories`.

**Observable signal**: bid-hit frequency, cross-dept-bid fraction, F-G-R при выигрыше задачи.

**Convergence criterion**: если `task_shape` на эмерджентной поверхности (`emergence-surface/capability-bids/`) собирает **≥5 побед с F≥2, R≥medium за 30 дней от данного агента**, задачный шейп промотируется в `declared_capabilities` этого агента через DRR Δ-1 (D6 §12.14). Это — специализация-как-паттерн, не как приписка.

### §4.3 Протокол торгов — hub-and-spoke сохранён

```yaml
# jetix-os/core/capability-capsule/bidding-protocol.yaml
protocol_id: bidding-v1
flow:
  - step: 1
    actor: task-originator (agent or ruslan@strategy-lead)
    action: "publish task to emergence-surface/capability-bids/open/{task-id}.md"
    fields: [task_shape, capability_requirement_vector, deadline, cp5_class, fgr_floor]
  - step: 2
    actors: all eligible agents (capsule.declared_capabilities.task_shape matches OR cross_dept_threshold met)
    action: "write bid.yaml with capability_score + evidence_links"
    timebox: 24h (configurable per task urgency)
  - step: 3
    actor: manager (hub)                        # [C14 hub-and-spoke preserved]
    action: "select top bid within ≤20-active-tasks budget; reject if budget full"
    tiebreak: [fgr_quality, workload_fairness, direction-of-life alignment]
    veto_classes: [safety, strategizing]        # [D6 §5.10.4 — agents не стратегируют]
  - step: 4
    actor: winner-agent
    action: "emit handoff message (acting_as declared); execute task"
  - step: 5
    actor: knowledge-synth
    action: "append outcome to emergence-surface/capability-bids/closed/{task-id}.yaml"
    outcome_fields: [success/failure, fgr_achieved, lessons]
structural_guards:
  - "если no bid clears floor → escalate cross-dept to manager → may escalate strategic to ruslan@strategy-lead"
  - "no bid may claim safety or strategic class"
  - "manager's ≤20-active budget is HARD (frontmatter counter; commit blocked if exceeded)"
```

**Hub-and-spoke остаётся.** Менеджер — хаб, но больше не **единоличный маршрутизатор**: он видит биды, выбирает из топ-кандидатов, утверждает. Агенты **самоаплаируются** через capsule-match. Это — hub-and-spoke с **широкоформатным bid pool**, не plain hub-routing.

### §4.4 Почему это НЕ 12-й агент

- Capsule — **overlay** к role.md (P2 / IP-1), не подмена.
- `acting_as` enum регенерируется из D6 §2.2 в CI (тот же скрипт, что и у Deep-Tech / Conservative).
- Cross-department торги ограничены множителем `1.3×` — это структурный параметр, не эмерджентность.
- Meta-agent в квартальном аудите флагит, если какой-то агент выиграл >50% задач категории вне home-dept за квартал. **Сигнал** того, что capsule-specialization приближается к де-факто новой роли → эскалация Руслану для явной структурной ревизии (новый агент или расширение capsule home-dept).

**Триада**: Structure param = 1.3× threshold + 50% audit; Signal = cross_department_bid_fraction per agent per quarter; Criterion = 50% hit → эскалация.

### §4.5 Отказ от инфляции

Maximalist-соблазн: добавить `content-strategy-agent`, `matchmaker-agent`, `standards-steward-agent` Day 1 как dormant-роли. **Emergent отказывается.** Dormant-капсулы живут **в `emergence-surface/capsules/`**, а не в `agents/`. Промоушен капсулы в канонический роль-манифест требует:

- Не менее 10 выигранных задач соответствующего шейпа за 90 дней.
- Квартальный аудит meta-agent подтверждает устойчивость паттерна.
- DRR Δ-2 + Ruslan подпись framing-lead.

Это и есть **самоорганизация внутри hub-and-spoke**.

---

## §5. Answer to Q3 — Integration Points

### §5.1 Phase-1 инвентарь

| # | System | Direction | Phase-gate | Primary use | SoT status | Fallback | Failure mode |
|---|---|---|---|---|---|---|---|
| 1 | Stripe              | R/W | Phase-0    | multi-SKU billing               | external | Wise + manual reconcile | 3× 5xx in 5min → degraded |
| 2 | Wise                | W   | Phase-0    | FX reconciliation               | external | manual bank rail        | — |
| 3 | Anthropic Claude    | R/W | Phase-0    | primary LLM                     | external | OpenAI → Groq (voice)   | rate-limit → exponential backoff |
| 4 | Groq Whisper        | R   | Phase-0    | voice → text                    | external | OpenAI Whisper          | — |
| 5 | Notion              | **W only** | Phase-0 | UI / планирование (NEVER SoT) | **UI-only**; Lock 17 | skip (non-blocking) | — |
| 6 | Telegram            | R   | Phase-0    | ingress (community Phase-1)     | external | skip                    | — |
| 7 | GitHub              | R/W | Phase-0    | repo + CI                       | external | local git + delayed push | — |
| 8 | Healthchecks.io     | W   | Phase-1    | pings                           | external | log-only                | — |
| 9 | Email (IMAP/SMTP)   | R/W | Phase-0    | клиентская связь                | external | manual inbox           | — |
| 10 | Perplexity         | R   | Phase-1+   | research (если Ruslan одобрит)  | external | Claude research mode    | — |
| 11 | Toggl              | R   | Phase-1    | architect-hours dashboard       | external | manual log              | — |

### §5.2 Интеграция = **опубликованный контракт**, не специальный health-check

В Emergent каждая интеграция имеет manifest в `emergence-surface/integration-contracts/{name}.md`. Пример:

```yaml
# emergence-surface/integration-contracts/stripe.md
integration_id: stripe-v1
phase_of_first_need: Phase-0 (перед первым счётом)
direction: R/W
fgr_of_contract: F2/G:jetix-payments-de-2026-q2/R-medium
primary_use: multi-SKU billing (session / template / services / retainer / subscription)
soT_status: external
authoritative_read_path: finance/revenue-log.jsonl (mirror, filesystem-first)
auth_storage: SOPS (1-key rotation per C4 secret discipline)
failure_signal:
  protocol_violation_detected_in: emergence-surface/routing-traces/api-errors/stripe-*.jsonl
  threshold: "3 consecutive 5xx in 5min"
fallback_plan:
  - "Wise FX rail + manual reconcile within 48h"
  - "replay revenue events from finance/revenue-log.jsonl after recovery"
phase_gate_enforcement:
  spend_cap_phase_1_eur_per_month: 200
  - "reject outbound Stripe.create_* if compute-ledger.monthly_total_eur > budget_remaining"
membrane_tier: partner   # billing involves client data — partner-level
cp5_on_create: l1_contractual  # new PaymentIntent → CP-5 L1 gate
```

**Нет собственных health-daemon-ов.** Метрики приходят из нормальных API-ответов + append в `emergence-surface/routing-traces/`. Meta-agent ежедневно читает трассировки и поднимает `boundary-drift-traces/api-{name}-YYYYMMDD.md`, если сигнал пересёк порог.

### §5.3 AP-1 явно: Notion = UI, никогда SoT

Каждая запись в Notion **дублируется** на файловую систему в том же commit — либо в `emergence-surface/`, либо сразу в `core/` (зависит от зрелости данных). CLI-скрипт `tools/notion-mirror.sh` запускается после каждого значимого filesystem-change; Notion-лосс восстанавливается за 1 день (D2 §14). *Filesystem = SoT* (Lock 17 / C4) — не компромиссный тезис.

### §5.4 Phase-gate enforcement на интеграциях

Каждый manifest декларирует `phase_gate_enforcement.spend_cap_phase_1_eur_per_month`. Middleware перед вызовом API читает `finance/compute-ledger.jsonl` и `core/revenue-gates/gate-state.yaml`. Если порог близок к исчерпанию — **отказ**, эскалация `cross-dept` → `manager`. **Структурный параметр** — gate-state; **сигнал** — монтируемая часть бюджета; **критерий** — 90% → ворнинг, 100% → hard block.

---

## §6. Answer to Q4 — Scaling Mechanism ($0 → $1T)

### §6.1 Центральный тезис: **структурные параметры ужесточаются с ростом**

Противоположно наивной интерпретации эмерджентности. Phase 1: тонкая предписанная структура + широкая зона permissible-emergence. Phase 2: стабильные паттерны промотированы в `core/` (шпалера ужесточилась); эмерджентность происходит в **более узких коридорах**. Phase 3+: `core/` плотная, `emergence-surface/` узкая — система **визуально похожа на Conservative при $1T больше, чем при $0**.

Это ключ к ответу на возражение *«масштабируется ли эмерджентность предсказуемо?»*. Ответ — **да, потому что сигналы эволюции (entropy, promotion rate, boundary drift) непрерывно инструментированы, а meta-agent эскалирует к Руслану, если сигналы вышли из предсказанных полос**. Эмерджентность — не надежда, а гипотеза + измерение + фальсификация.

### §6.2 7 инвариантов масштаба (preserved $0 → $1T)

| # | Invariant | Phase-1 механизм | Сигнал эскалации |
|---|---|---|---|
| SI-1 | Hub-and-spoke сохраняется (manager ≤20 active) | frontmatter counter в manager mailbox | counter > 18 → warn; > 20 → block |
| SI-2 | Мембрана жёсткая (tier-crossing только через контракт) | hook-2 pre-commit | любой public→partner/core link → reject |
| SI-3 | FPF-контракты обязательны | capsule.fpf_bindings mandatory | empty fpf_bindings → CI fail |
| SI-4 | F-G-R per claim обязателен | hook-3 | untagged claim → block |
| SI-5 | Revenue-gates hard | middleware на всех API-вызовах | spend > gate → block |
| SI-6 | `acting_as` enum ≡ D6 §2.2 | regen script в CI | diff > 0 → fail |
| SI-7 | Promotion-rate в полосе ±1σ | emergence signal set (§14) | 14d out-of-band → escalation Ruslan |

**SI-1 через SI-6 — структурные.** **SI-7 — эмерджентный.** Это показывает: эмерджентность **поверх** жёсткого фундамента, не **вместо** него.

### §6.3 Как масштабируется Roster (вертикальное + горизонтальное)

**Горизонтально (Phase 1 → Phase 2a, 1 pilot → 3 pilots).** Новый overlay `jetix-company-<pilot>/`. Общий `jetix-os/core/`. Общие 11 агентов; capsule-ы те же. +≤10% LOC (D4 §5.1).

**Вертикально (capability-специализация через bid-победы).** Агент `X` собрал 10+ побед в новом task_shape → DRR добавляет shape в `declared_capabilities`. **Нет новой роли**, только расширение capsule. +0% LOC в `core/`.

**Переход capsule → новый агент.** Если capsule задаёт >50% задач вне home-dept за квартал → meta-agent флагит → Ruslan решает: (a) расширить home-dept capsule этого агента, (b) создать нового агента (редко; Phase 2b+ only). **Структурный параметр**: 50% порог; **сигнал**: cross-dept fraction per quarter; **criterion**: 50% за 2 квартала подряд → эскалация.

### §6.4 Как масштабируется протокол-поверхность

USB-C protocols (§17) в Phase 1 — **emergence-surface/protocol-candidates/**. Day 1 архитектор не пишет «стандарты»; агенты в процессе реальных handoff публикуют `protocol-candidate-{name}.md`. Daily `knowledge-synth` консолидирует: паттерны, повторяющиеся в ≥3 независимых handoff за 14 дней со стабильным message shape → промоушен в `core/protocols/` как draft standard.

**К $200K**: 2-4 зрелых draft в `core/protocols/`. **К $1M**: 6-8. **К $1T**: 15-25 стандартов de facto, каждый **эвиденс-driven**, не speculation.

### §6.5 LOC refactor per 10× gate

| Subsystem | Phase 1 | Phase 2a (3 pilots) | Phase 2b (team 5-10) | Est LOC delta |
|---|---|---|---|---|
| `jetix-os/core/`            | thin                | +promoted patterns | +promoted patterns | **<15% per gate** |
| `jetix-os/emergence-surface/` | open substrates    | partial fill        | richer fill         | **0% (schema-stable)** |
| `agents/*/capability-capsule.yaml` | 18 capsules | 18 + 2 activations | 25-30 (+ dept growth) | **<20%** |
| `jetix-os/protocols/`       | 0-2 promoted        | 2-4                 | 4-6                 | additive, <25% |
| `wiki/core/`                | seed + promoted     | +promoted           | +promoted           | additive, 0% schema change |
| `jetix-company-*/`          | 1 overlay           | 3 overlays          | 3-5 overlays        | +overlay, не base |

Все < 30% порог D4 §5.1 — потому что **`core/` растёт добавлением промотированных артефактов, не редизайном**. Это SI-инварианты в действии.

### §6.6 Phase-2a triple-AND trigger

```yaml
# jetix-os/core/revenue-gates/trigger-phase-2a.yaml
trigger_id: mht-1
all_of:
  - metric: mrr_12w
    condition: ">= 20000 EUR for 3 consecutive months"
    source: finance/revenue-log.jsonl
  - metric: ruslan_l1_l2_fraction
    condition: "< 0.40"
    source: ops/toggl-deep-hours.jsonl
  - metric: dpa_clients
    condition: ">= 1 active"
    source: legal/dpa/active.yaml
on_all_met:
  - "manager halts auto-dispatch; notify ruslan@strategy-lead"
  - "open decisions/mht-1-trigger-pending.md DRR"
  - "emergence-surface/capsules/{dpo, customer-success} promotion pre-approved"
```

Триггер — чистый dashboard-query, непрерывный (D2 §6 continuous, NOT periodic).

---

## §7. Answer to Q5 — Data Architecture (decentralised write + centralised consolidation)

### §7.1 9 сущностных типов + 9-10 типизированных рёбер

Соответствует CLAUDE.md v2. Сущности: `concepts/` · `entities/` · `sources/` · `topics/` · `ideas/` · `experiments/` · `claims/` · `summaries/` · `foundations/`. Рёбра (6 FPF mereology — `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, `MemberOf`, `AspectOf` (D6 §3.5 / A.14); + 3-4 Jetix-domain — `creates`, `operates-in`, `methodologically-uses`, `constrained-by`).

### §7.2 Двухконтурная запись

```
wiki/
├── emergence-surface/
│   └── claims/{YYYY-MM-DD}/{agent-id}/{claim-id}.md    # любой агент → сюда
└── core/
    ├── concepts/       # promoted only
    ├── entities/
    ├── topics/
    ├── foundations/
    ├── summaries/
    └── graph/edges.jsonl    # typed edges, append-only
```

**Emergence-surface claim обязан** иметь Day 1 полный F-G-R frontmatter (C13). Пример:

```markdown
---
id: c-2026-04-21-sales-lead-mueller-pain-0017
entity_type: claims
f_g_r: F2/G:jetix-dach-mueller-qualification-2026-q2/R-medium
bias_class: [REP, LNG]
alpha_touched: client:lead-identified→qualified
tier: member        # 4-tier ACL [§8]
ba_state: BA-0
sources:
  - raw/2026-04-10-mueller-intro-call-transcript.md
actor: sales-lead
cites:
  - wiki/core/concepts/dach-mittelstand.md
  - wiki/emergence-surface/claims/2026-04-18/sales-research/mueller-dossier.md
---
Мюллер-GmbH — DACH Mittelstand: компания 120 сотрудников, семейное управление
второго поколения, pain-вопрос по compliance-нагрузке...
```

### §7.3 Ежедневная консолидация (gardener operation)

`knowledge-synth` запускает `tools/promote-claims.py` ежедневно:

1. Граф ко-цитирования строится из `cites:` frontmatter всех claim-ов за 14 дней.
2. Кластеры с плотностью ≥0.35 и ≥3 claim-ами из ≥2 агентов проверяются.
3. Каждый concept-кандидат получает черновик `wiki/core/concepts/{slug}.md` с merged-citations + DRR Δ-1 review (D6 §12.14).
4. DRR — auto-approved, если contradicting counter-claim отсутствует и F-G-R-композиция держится; иначе эскалация Ruslan.
5. Промоутированные concept-ы возвращаются как нодовые ссылки в `edges.jsonl` (`ComponentOf`, `ConstituentOf`, etc.), дополняя hand-drawn приоры.

**Структурный параметр**: threshold density 0.35, 3 claim-а, 2 agent diversity, 14-day window.
**Сигнал**: cluster density, claim count, agent diversity over window.
**Critierion**: threshold hold 48h без contradicting counter-claim.

### §7.4 Почему wiki не выродится в шум

Потому что **F-G-R — структурный параметр, не эмерджентная оптимизация**. Claim без F-G-R — hook-3 блокирует коммит. Claim с R-low — живёт на поверхности, но не может promote в core (порог R≥medium). Meta-agent еженедельно аудитит `promotion_rate_variance`: если выше/ниже полосы ±1σ — эскалация. Threshold — tuneable parameter, под подписью Ruslan framing-lead.

*«Notion loss recoverable in 1 day, wiki loss = Jetix loss»* (D2 §14). В Emergent это усилено: **emergence-surface loss recoverable in 7 days** (восстановимо из git + mailbox-ов); **core loss recoverable in zero days**, потому что core — append-only (промоушен — commit, деструктивных операций нет).

### §7.5 ATOM-REGISTRY

Атомы — first-class entity в `wiki/core/foundations/atoms/` (промоутированные) + `wiki/emergence-surface/claims/.../atom-*` (кандидаты). atom-2558 (4-class escalation) — пример уже промотированного атома (D4 §4.4 цитирует его как устоявшийся). Новые атомы кристаллизуются тем же путём, что и concepts. **Emergent не переизобретает атомарную модель** — использует промоушен-пайплайн.

### §7.6 Alpha state + BA cycle на сущности

Каждая сущность несёт `alpha_state:` (если relevant per D6 §6.2) и `ba_state:` (D.5 cycle, D6 §12.10). Hook-4 проверяет past-participle имена состояний. BA-0 / BA-1 / BA-3 обязательны per-project; BA-2 (Panel) — Phase-2a+.

---

## §8. Answer to Q6 — Privacy / Security Membrane

### §8.1 Мембрана — единственная non-emergent структура

*«Gentleman inside / Predator outside»* (Lock 1) — верхнее правило. Behaviour **внутри** мембраны flexible, cooperative, emergent. Behaviour **на** мембране rigid, adversarial, contract-driven.

### §8.2 4-tier ACL

| Tier | Directory | Writer | Reader | Tier-crossing правило |
|---|---|---|---|---|
| `public`  | `public/`, `surface/`, `landing/` | auto-gen only (not hand) | anyone | — |
| `member`  | `members/`, invite-only channels  | inbox-processor, sales-outreach | invited + 5-criteria pass | member→public allowed (auto-gen) |
| `partner` | `jetix-company/clients/*/`        | sales-closer, acceptance-authority | active client + lawyer | partner→member forbidden |
| `core`    | `jetix-os/core/`, `wiki/core/foundations/` | Ruslan + knowledge-synth (promotion) | Ruslan + meta-agent (audit) | core→public only через deep-redact pipeline |

**Enforcement Phase 1** — комбо:

1. **filesystem permissions** (chmod 750 `jetix-os/core/`, etc.).
2. **directory convention** + **frontmatter `tier:`**.
3. **hook-2 pre-commit**: rejects any link where `src.tier < tgt.tier`.
4. **meta-agent daily audit**: sweeps for anomalous cross-tier references in `emergence-surface/`.

Никакого custom access-control daemon в Phase 1. Unix + git branch-permissions + hook — достаточно.

### §8.3 GDPR Art.22 + EU AI Act Phase-1

- **CP-5 human approval gate** (D6 §4.5) на любом client-affecting решении. Tier L1 / L2 / L3 per D6 §4.5.1.
- **Audit trail YAML** per gate decision (§15 контрастирует тут и там).
- **Contestation path**: WP251rev.01 — `time_to_review_seconds < 60` флагит rubber-stamp risk; alt-reviewer guarantee.
- **DPA stub** в `jetix-company/legal/dpa-template.md`; внешний `dpo` executor активируется Phase-2a при ≥1 DPA client.

### §8.4 Gentleman/Predator как **две YAML-конфигурации тона**

```yaml
# jetix-os/core/membrane/tone-profiles.yaml
inside:   # Gentleman — apply when src.tier ∈ {member, partner, core}
  formality: civil-direct
  disagreement: welcomed; log в wiki/emergence-surface/claims/ с counter-claim tag
  rejection: explicit rationale + DRR reference
  trust: rich; emergence allowed
outside:  # Predator — apply on membrane crossings or public-facing
  formality: precise-assertive
  disagreement: firm, evidence-forward
  rejection: clean decline + alternative + CP-5 trail
  trust: absent; контракты обязательны
```

Сообщение, пересекающее мембрану, валидируется по **outside**. Сообщение внутри — по **inside**. *Эмерджентность **не** пересекает мембрану.*

### §8.5 Защита от AP-3 / AP-9 / AP-10

Три anti-patterns, которые легче всего перепутать с эмерджентностью:

- **AP-3 (mass-market)**. Emergent — **структурная** эмерджентность: паттерны в графе взаимодействия (ко-цитирование, bidding-hit кластеры, capability-specialization). НЕ поведенческая. Нет engagement-loop, нет награды за время в системе, нет лидербордов.
- **AP-9 (motivational-circle)**. Фильтр 5-criteria + direction-of-life axis (C20) — жёсткий структурный параметр на членстве. Не «кто хочет» входит, а «кто проходит матрицу».
- **AP-10 (attention-extraction)**. Нет push-notifications, нет infinite-scroll, нет hook-механик. Пулл-based: пользователь приходит к контенту, контент не преследует пользователя.

**Эмерджентность структурная, не поведенческая — первое утверждение из трёх (см. также §13, §14).**

### §8.6 9 Innovations IP protection

Per ADR-Chunk-8 Area 2 + OT5-A: `wiki/core/foundations/jetix-innovations.md` — `tier: core`, `f_g_r: F3/G:jetix-innovations/R-high`. Hook-2 запрещает любой emission-link из `core/foundations/jetix-innovations.md` в outer tier. Secret-sauce защита **в файловой системе**, не в внешнем DRM.

---

## §9. Answer to Q7 — API Architecture (multi-provider)

### §9.1 Protocol, not a layer

API в Emergent — **опубликованный протокол**, не абстракционный слой. Каждый агент знает compute-contract-шаблон; вызов идёт через тонкий `tools/llm-call.py`, который:

1. Читает capability-capsule агента (`compute_tier` declaration).
2. Читает `core/revenue-gates/gate-state.yaml` — проверяет бюджет.
3. Направляет на `model_preference.primary`; при 5xx/timeout — на `fallback_chain[]`.
4. Логирует append-only в `finance/compute-ledger.jsonl`.
5. Failure events → `emergence-surface/routing-traces/api-errors/`.

### §9.2 Compute-ledger (append-only)

```jsonl
{"ts":"2026-04-21T14:22:00Z","agent":"sales-lead","provider":"anthropic","model":"claude-sonnet-4-6","task_id":"t-2026-04-21-018","capability_capsule_hash":"sha256:9ac1...","tokens_in":8203,"tokens_out":2104,"cost_eur":0.178,"purpose":"proposal-draft-mueller","fgr":"F2/G:jetix-dach-mueller/R-medium","bid_id":"b-2026-04-21-007"}
```

**Фишка Emergent**: запись содержит `capability_capsule_hash` и `bid_id` — пара, по которой можно отследить, **какая эмерджентная специализация стоит денег**. Meta-agent еженедельно рассчитывает **`compute_spent_per_promotion`** — новый сигнал: слишком много compute, слишком мало промоушенов ⇒ возможный drift.

### §9.3 Provider-fallback Phase 1

```yaml
# jetix-os/core/api/compute-contract-default.yaml
model_preference:
  primary: {provider: anthropic, model: claude-sonnet-4-6, thinking_mode: on}
  fallback:
    - {provider: anthropic, model: claude-haiku-4-5}
    - {provider: openai,    model: gpt-4o-2026-02}
    - {provider: google,    model: gemini-2-pro}
    - {provider: local,     model: cached-response}   # degraded
max_tokens_per_call: 16000
monthly_budget_eur_phase_1: 500  # under 800 hard gate
escalation_rules:
  exceed_budget: "reject; emit escalation class=cross-dept → manager"
  primary_5xx_3_times: "switch fallback_chain[0]; log to emergence-surface/routing-traces/"
  all_providers_down: "freeze auto-dispatch; ruslan@system-admin manual"
```

### §9.4 Phase-gated cost ceiling

| Gate | Monthly cap | Primary mode | Signal |
|---|---|---|---|
| €0 → €20-30K   | ≤ €300/mo | Haiku-default | compute_ledger.jsonl aggregate |
| €20-30K → €50K | ≤ €500/mo | Sonnet-on-bid | same |
| €50K → €200K   | ≤ €800/mo | **HARD (D4 §8.3)** | same |
| €200K → €1M    | ≤ €2500/mo | Opus expanded | same |

Emergent Phase-1 est ≤ €500/mo.

### §9.5 AP-11 защита

`fallback_chain[]` — обязательное поле в `compute-contract`; hook-аудит отвергает manifest без fallback. AP-11 (single-provider) невозможен.

---

## §10. Answer to Q8 — Token Economy (Option B, membrane preservation)

### §10.1 Эмерджентность **не** покрывает эту подсистему

**Самая чёткая иллюстрация дисциплины Emergent.** Phase 1 Emergent **не эмитит и не учитывает** внутренние токены. Токен-экономика — Lock 15 / Lock 23 / C21 **жёсткий** gate. Активация — Phase-2 internal-only + triple-AND trigger (C15). Phase 3+ limited public — **economic-claim only** (AP-13: никогда governance, никогда community-access).

### §10.2 Phase-1 дизайн-время подготовка

Только схемы и зарезервированная директория:

```
jetix-os/emergence-surface/token-economy/
├── spec/
│   ├── token-ledger.schema.yaml       # append-only JSONL — тот же паттерн, что compute-ledger
│   ├── seat-of-ownership.draft.md     # policy draft (not policy)
│   └── state-machine.draft.yaml       # issue / hold / transfer / burn / redeem состояния
```

### §10.3 Явное утверждение

> **Phase 1 Emergent не эмитит и не учитывает внутренние токены.** Активация происходит при: (a) Lock 15 €200K gate пройден, (b) Phase 2 internal-only scope (Lock 23 Option B), (c) triple-AND trigger (C15). Только все три одновременно.

Это и есть демонстрация того, что **Emergent уважает жёсткие гейты**. Эмерджентность происходит **внутри** их, не **поперёк**.

### §10.4 Orthogonality invariant

```yaml
# emergence-surface/token-economy/spec/orthogonality.md
forever_invariants:
  - "token.ownership NEVER correlates with ACL tier"
  - "public-token transfer NEVER grants member/partner/core access"
  - "governance right = NEVER bundled with token [AP-13]"
  - "community-access right = NEVER bundled with token [AP-13]"
enforcement_phase_2_plus:
  - schema-level orthogonality check in ledger state-machine
  - hook rejecting correlation in config
```

Инварианты **написаны** Day 1, даже когда **применены** будут только в Phase 2+. Writing before emitting = **structural preservation**.

### §10.5 5 канонических dry-run событий

| Event | Membrane effect | Check |
|---|---|---|
| mint(internal-credit, 100, agent-X)  | none | ✓ |
| transfer(restricted-public, A→B)     | none | ✓ |
| burn(internal-credit, 50, agent-X)   | none | ✓ |
| redeem(internal-credit, discount)    | none | ✓ |
| adjust(internal-credit, +5, reason)  | none | ✓ |

Каждое событие schema-validated и orthogonality-preserved. Phase-2+ активация происходит **без редизайна** — ровно в силу тщательности Phase-1 specs.

---

## §11. Answer to Q9 — Matchmaker Algorithm (Emergent signature: agent-bidding)

### §11.1 Центральный move: matchmaker = **агент-биддинг для обеих задач**

Традиционная интерпретация Lock 21: «матчмейкер = внешние task↔specialist матчи». Emergent расширяет: **тот же механизм работает для внутренней task-routing** (§4.3). Matchmaker = **унифицированный bid-pool protocol** — один контракт, два применения.

### §11.2 4 модуля

**(a) Algorithm — bidding-match**.

```yaml
# jetix-os/core/capability-capsule/match-algorithm.yaml
signature: |
  match(task: TaskSpec, bid_pool: [Bid]) -> RankedBids
  where
    TaskSpec = {
      task_shape,                       # str (e.g., "sales.propose")
      capability_requirement_vector,    # [dim, weight] pairs
      fgr_floor,                        # {f, r, scope-constraint}
      deadline,
      cp5_class                         # [D6 §4.5]
    }
    Bid = {
      bidder_agent_id,
      capability_score,                 # [0.0, 1.0]
      evidence_links,                   # prior hits, F-G-R tagged
      workload_current,                 # for fairness
      fresh_availability                # timestamp
    }
    RankedBids = sorted by:
      1. capability_score × evidence_weight_multiplier
      2. fgr_quality of past hits on shape
      3. workload fairness (anti-monopoly within manager's ≤20 budget)
```

**(b) Quality-gate — D.5 BA cycle.**

Минимум F-G-R per task-shape. Bid ниже floor — отвергнут при step-2 bidding-protocol (§4.3). BA-0 инициируется с task-publish; BA-1 mid-execute; BA-3 при acceptance.

**(c) Contract fixation — L/A/D/E**.

Если задача cross-membrane (партнёр / клиент) — обязательный L/A/D/E контракт (FPF A.6.B), подписи: sales-closer + acceptance-authority (non-delegatable OME L2).

**(d) Metrics pipeline**.

Дашборд viewpoint-ы (§14): match-rate, bid-diversity entropy, time-to-match, completion-rate, false-match rate.

### §11.3 Спецификация matchmaker **как эмерджентного артефакта**

```
emergence-surface/matchmaker/
├── bid-pool/{YYYY-MM-DD}/{task-id}/
│   ├── task.md                    # task spec + capability_requirement_vector
│   ├── bids/{bidder}/bid.yaml
│   └── resolution.yaml            # manager's decision + tiebreak reasoning
└── metrics-daily.jsonl
```

**Phase-1 реализация** — **markdown + JSONL**, не runtime engine. Каждая торговля = git-commit (Lock 17). Менеджер — человеко-доступный actor: читает bid-ы, выбирает в ≤20-budget. Это **медленно**, но **ровно то, что нужно соло-оператору**: Ruslan может review-ить резолюции выборочно без инструментального прокси-слоя.

**Phase-2b** — automation: vector-match engine читает те же .yaml, возвращает RankedBids, менеджер approve-ит top-1 (or top-3 preview). Migration-free, потому что data shape уже структурированный.

### §11.4 Specialization эмерджент через bid-history

Агент `sales-lead` выигрывает 8 из 10 задач `content.strategy-frame` за квартал. **Сигнал**: bid-win-rate по shape per agent. **Порог**: 70% win + ≥10 hits → DRR расширяет `sales-lead.capability-capsule.declared_capabilities` этим task_shape-ом (промоушен cross-dept из threshold-based bidding в home-dept claim). **Критерий сходимости**: win-rate держится >60% ещё один квартал после расширения.

**Это структурная специализация**: паттерн в графе биддинга, промотированный в capsule. Не **назначенная**, не **спонтанная** — **харвестированная**.

### §11.5 Ruslan non-delegatable (OME L2 preserved)

6 non-delegatable функций (Strategy / Taste / Responsibility / Approval / Escalation / Relationships) остаются жёсткими. Матчмейкер **не** может выбирать для: `safety` events, `strategic` decisions. Capsule `bid_policy.no_bid_categories: [safety, strategizing]` — structural parameter. Agent трёт пол при попытке биддить safety — hook откажет коммит.

### §11.6 External matchmaker (Phase-2+)

Phase-2+ matchmaker для внешних task↔specialist — **тот же протокол**, только `bid_pool` включает partner-tier agents (внешних). Внешние специалисты публикуют свои `capability-capsule.yaml` в partner-тир директории. Контракт-фиксация обязательна; не-approved специалист не может биддить. **Scale trajectory axis преимущество**: к $200K gate, когда открывается external matchmaker, bidding-protocol **уже работает** 6+ месяцев на внутренних задачах; human + system confidence уже есть.

---

## §12. Answer to Q10 — Roy-Replication Packaging (harvested, not speculated)

### §12.1 Центральный тезис: kit — **эмерджентный артефакт**

Lock 21 + D3 §6.3: methodology-as-system kit для replication. Emergent специфический тезис: **kit = тот самый набор протоколов и капсул, которые были промотированы из emergence-surface в core к моменту €200K gate**. Packaging — не проектирование Day 1, а **curated export зрелых паттернов**.

### §12.2 Phase 1: **нет kit-tooling**

Документированная методология + draft template + pointer-guide для external-relations sub-role. **Нет installer-а, нет upgrade-скрипта, нет version-matrix-а.** Причина: ничего ещё не стабилизировалось; «инструмент для упаковки ещё не стабильного» = infrastructure debt.

### §12.3 Phase 2a: early kit (≤€200K)

Первые 2-3 замерзших паттерна промотированы:
- `core/protocols/agent-handoff-v*.md` (если emerged by Phase 2a)
- `core/capability-capsule/bidding-protocol.yaml` (уже стабильный)
- `core/membrane/tier-map.yaml` (стабильный Day 1)
- `core/promotion-rules/concept.yaml` (стабильный)

Сбор в tarball / curated git branch — ручной, раз в квартал, под подписью framing-lead.

### §12.4 Phase 2b+ (после €200K): kit-manifest Day 1

```yaml
# replica-kit/<domain>/kit-manifest.yaml
kit_id: jetix-kit-<domain>-v1
kit_version: 1.0.0
promoted_protocols:
  - core/protocols/agent-handoff-v1.md
  - core/protocols/contract-fixation-v1.md
  - core/protocols/bidding-v1.md
fpf_primitives: [mereology, alphas, viewpoints, pillars, guard_rails]
roster_included: [manager, sales-lead, sales-research, sales-outreach, inbox-processor, knowledge-synth, meta-agent]
roster_excluded: [strategy-support-analyst, crazy-agent]
install_mode: overlay          # jetix-os/ и core/ копируются; jetix-company-<roy>/ создаётся
partner_tier_bound: true       # [AP-4: internal-only forever for core]
success_criteria_ref: ./success.yaml
kill_criteria: ["no signed contract in 90d", "F-G-R compliance < 80% at 60d"]
license: internal-only
```

**Emergent тезис**: export-readiness = **promotion-readiness**. Порог промоушена паттерна из emergence-surface в core = одновременно и порог export-готовности. Один threshold, две функции.

### §12.5 Новый roy как overlay

Новый домен = новый overlay `jetix-company-<roy>/` + копия `jetix-os/` base. Emergence-surface этого roy — свой; co-citation-graph не пересекается с Jetix unless explicitly allowed. ≤14 days bootstrap — норма.

### §12.6 D-test проходит

Hook 5 (D-test) на `jetix-os/core/` и `jetix-os/emergence-surface/` — 0 попаданий Jetix-specific strings. Overlay — где Jetix живёт. Перенос в новый domain — **copy base + пустой overlay**, заполнить overlay. Universality (C9) **структурно** достижима.

---

## §13. Answer to Q11 — Content Pipeline

### §13.1 TOF / mid / deep + archetype-keyed

Per D4 §3.1.10 + Lock 12 + 11 archetypes (D4 §2 §3.1.1 C14-archetypes). Pipeline:

```
raw/  (transcripts, voice, research)
  ↓  inbox-processor
emergence-surface/claims/{date}/{agent}/  (F-G-R tagged)
  ↓  knowledge-synth promotion
core/content/{topic}.md  (promoted, ready)
  ↓  static-site-generator (Jinja-style templates per archetype)
public/ (TOF) + members/ (mid) + partners/ (deep)
```

### §13.2 Frame-tag + archetype-key (frontmatter-driven)

```markdown
---
id: content-mueller-audit-teaser
frame_tag: pain-primary      # [Lock 9 default TOF]
archetype_keys: [startupper-de, stable-de]   # target subset of 11
tier: public
f_g_r: F2/G:jetix-tof-de-2026-q2/R-medium
bias_class: [REP, LNG]
---
```

Static-site-generator рендерит один canonical file в N вариантов (по числу archetype-keys) применением per-archetype Jinja templates.

### §13.3 Cadence — **emergent signal**

Meta-agent отслеживает publication-rate variance. Sharp drop (>40% под trailing-28-day average) → escalation к Ruslan. Это **сигнал** здоровья маркетинговой машины.

**Структурный параметр**: публикационная cadence декларируется в `core/content/cadence-policy.yaml` (минимум 1 deep/mo + 2 mid/mo + 3 TOF/wk).
**Сигнал**: actual publication timestamps.
**Критерий**: variance > 40% для 14 дней → meta-agent emit escalation.

### §13.4 Site = primary channel (Lock 12)

Static site генерируется из `core/content/` + archetype-keyed templates. Social (LinkedIn, Twitter, YouTube) — pointer-posts с ссылками на site. Нет собственного CMS, нет headless. Site = substance; social = TOF acquisition only (Lock 12 / D12 / AP-14).

### §13.5 AP-3 / AP-9 / AP-10 явная защита

Эмерджентность **структурная** (какие концепты кристаллизуются и рендерятся), **не поведенческая** (никаких petle вознаграждения, engagement hacks, motivational content). Dashboard-viewpoint не содержит `time_spent` или `engagement_score` — только `substance_throughput` (published content) и `time_saved_proxy` (reads/views with depth-normalized weighting). **Второе утверждение о структурной-не-поведенческой эмерджентности** (см. §8.5 первое, §14 третье).

### §13.6 Lock-4 нормализация (Jackson/Джек → Jetix)

Ingest-pipeline на всех raw artefacts применяет canonical substitution перед записью в emergence-surface/. CI hook проверяет: pre-commit grep raw/→ emergence-surface/ выявляет residual Jackson/Джек.

---

## §14. Answer to Q12 — Dashboard Implementation

### §14.1 v1 Phase-1 — 7 мандатори + эмерджентный signal-set

**Мандатори 7 (D4 §4.7):**

1. Architect-hours/week (declining, OME 18h baseline)
2. Founder-dependency % (<30% Phase 2+)
3. Monthly revenue (trend + gates)
4. Failure-rate + MTTR (≤3 incidents/mo, p50 ≤60min)
5. Cash runway (≥6mo Phase 1)
6. Deep Hours (25-30h/wk Phase 1)
7. Productized-revenue % (≥40% €200K, ≥70% €1M)

**Emergent signal-set (Emergent signature):**

| # | Signal | Source | Порог escalation |
|---|---|---|---|
| E-1 | Task-routing entropy          | `emergence-surface/capability-bids/` | entropy < 0.5 (monopoly) or > 2.5 (chaos) for 14d |
| E-2 | Claim-promotion rate          | `wiki/core/concepts/` new files / 30d | <1/week trailing-30d after week 6 |
| E-3 | Capability-match score dist.  | bid.yaml capability_score per agent | variance > ±1σ from rolling mean for 14d |
| E-4 | Department-boundary drift     | cross-dept bid hits / total          | >50% for one agent for 2 quarters |
| E-5 | Content-cadence variance      | publication timestamps                | >40% drop for 14d |
| E-6 | Compute/promotion ratio       | compute-ledger × claim-promotion     | compute up AND promotion flat → drift |
| E-7 | Membrane-crossing anomaly     | `boundary-drift-traces/`             | any unaudited public→partner link |

Каждый signal имеет: **structure parameter** (порог), **observable source** (файловая метрика), **convergence criterion** (когда meta-agent эскалирует).

### §14.2 Schema viewpoint

```yaml
# dashboard/viewpoints/e-1-task-routing-entropy.yaml
viewpoint_id: e1-task-routing-entropy
publisher: meta-agent
audience: [ruslan@strategy-lead]
source_files: ["emergence-surface/capability-bids/*/*/*.yaml"]
query:
  type: shannon_entropy
  group_by: winner_agent_id
  window: rolling_7d
rendering:
  format: markdown-table
  location: dashboard/monday/e1-routing-entropy.md
alert_binding:
  trigger_if: value < 0.5 OR value > 2.5 for 2 consecutive weeks
  notify: [ruslan@strategy-lead]
  drr_required: true on second alert
fgr: F1/G:dashboard-phase-1/R-medium
```

### §14.3 Rendering — weekly markdown report

Phase 1: `pipeline/monday-render.sh` (cron Mon 12:00 Europe/Berlin — founder-anchor per D3 §14.2). Read JSONL + YAML → render 2-page markdown → commit to `dashboard/monday/YYYY-MM-DD.md`. Метрики пишутся **непрерывно** (каждый commit обновляет источник), но **рендер** — еженедельный. Цитата: *«Continuous, every iteration — NOT periodic»* (D2 §6) — сигнал **capture** непрерывен, dashboard **surface** еженедельный, потому что Phase-1 web UI = Phase-2 spend. Meta-agent потребляет сигналы **непрерывно** и эскалирует между Monday-render-ами при threshold-crossings.

### §14.4 v2 Phase-2+, v3 Phase-3+ — additive

**v2 (Phase-2+)**: + roy count, + member count, + match-rate, + subscription-vs-partnership ratio.
**v3 (Phase-3+)**: + market-cap, + token circulation, + research outputs, + sub-network activity.

Добавление = новый viewpoint-file. **Zero schema migration** (SI-инвариант сохранён).

### §14.5 Anti-engagement

**Третье утверждение о структурной-не-поведенческой эмерджентности.** Dashboard измеряет **time-saved** и **substance throughput**, не **time-spent** или **engagement**. Нет `engagement_score` в схеме viewpoint-а — любой PR, добавляющий подобное поле, **отвергается на code-review** (policy-guard, не runtime). AP-3 / AP-9 / AP-10 структурно запрещены.

---

## §15. Answer to Q13 — Escalation Routing

### §15.1 4-class (atom-2558 / D4 §4.4) — **жёстко, не эмерджентно**

| Class | Router | Пример | SLA |
|---|---|---|---|
| `dept-internal` | Dept Lead                        | pricing off-CHR <5%       | 24h |
| `cross-dept`    | manager (≤20 active)             | content needing legal     | 48h |
| `strategic`     | ruslan@strategy-lead              | quarterly attention-theme | 5 days |
| `safety`        | meta-agent + ruslan (halt task)  | DPA breach / GDPR Art.33  | immediate |

Safety-event **не** «постепенно кристаллизуется» в эскалацию — маршрутизация мгновенная.

### §15.2 CP-5 gate YAML (полностью соответствует D6 §4.5)

```yaml
# core/escalation/cp5-gate-template.yaml
decision_id: d-{YYYY-MM-DD}-{slug}
tier: l1_contractual | l2_substantive | l3_cosmetic
class: strategic | safety | cross-dept | dept-internal
client_affecting_category: <text>
originator:
  role: <agent or ruslan-sub-role>
  f_g_r: F<n>/G:<scope>/R-<reliability>
evidence_links: [...]
bias_class: [REP, ALG, VIS, MET, LNG]   # subset
gate_keeper:
  role: <role>
  holder: <person-id>
  approved_at: <ISO>
  decision: approved | rejected | modified | escalated
  reason: <text>
  time_to_review_seconds: <int>
retention:
  retention_until: +6y (HGB §257) or +6mo (EU AI Act Art. 12 minimum)
contestation_path:
  gdpr_art_22_3: enabled
  wp251rev_01_compliant: true
  alt_review_available_until: +10_business_days
rubber_stamp_guards:
  - time_to_review_seconds >= 60 (else flag)
  - max_8_l2_per_gate_keeper_per_4h_block
```

### §15.3 Эмерджентность **на topologии**, не на маршрутизации

**Маршрутизация** — жёсткая (классы фиксированные). **Но**: паттерны **частых** cross-dept эскалаций = **сигнал**, что departmental topology требует эволюции.

**Triad:**
- **Structure param**: 4 классы фиксированы; `manager ≤20` фиксирован; никакая эмерджентность не меняет эти правила.
- **Observable signal**: cross-dept escalation frequency per department per quarter.
- **Convergence criterion**: если one department > 40% эскалаций cross-dept за 2 квартала → meta-agent flag → Ruslan рассматривает явную структурную ревизию (новый департамент? разделение? merger?).

Это и есть «эмерджентность поверх жёстких классов»: классы не меняются; топология департаментов — негосударственна, эволюционирует за phase time.

### §15.4 6 non-delegatable functions (OME L2) preserved

Стратегия / Вкус / Ответственность / Утверждение / Эскалация / Отношения — Ruslan-only (D1 §3 / D2 §14). `acting_as` enum в CI прямо **отклоняет** попытку agent-а принять эти роли. Это и есть жёсткий структурный параметр.

### §15.5 Founder-unavailable chain

Phase 1: proxy-Steuerberater + lawyer stub per `executor-binding.yaml.chain_of_command`. Формальный трасти — при первом клиентском контракте. Phase-2a+: Beirat-alternate добавляется.

---

## §16. Answer to Q14 — Onboarding Architecture (7-artefact sequence)

### §16.1 Цель: 2-й pilot client готов ≤7 дней cold-start

### §16.2 7-artefact sequence (на emergence-surface)

```
emergence-surface/clients/{client-id}/
├── 01-discovery-notes.md       # Day 1: интервью + pain scan
├── 02-scope-doc.md             # Day 1-2: согласованный scope
├── 03-fpf-contract.md          # Day 2-3: L/A/D/E clauses
├── 04-capability-capsule-overlay.yaml   # Day 3: per-client cap overlay
├── 05-partner-tier-acl.yaml    # Day 3: tier assignment + permissions
├── 06-kickoff-meeting-log.md   # Day 4: first working session
├── 07-first-week-success-metric.md  # Day 7: initial delivery + BA-0 init
```

Каждый артефакт = markdown + git-commit. Никакого SaaS workflow engine.

### §16.3 Pilot-manifest (analogue)

```yaml
# emergence-surface/clients/mueller-gmbh/pilot-manifest.yaml
client_id: mueller-gmbh
icp_archetype: startupper-de    # [Lock 7 / D7]
five_criteria:                   # [Lock 22 / C20]
  startupper: 0.8
  azart: 0.6
  stable: 0.4
  adequate: 0.9
  upward: 0.7
direction_of_life_axis: +0.6
jurisdiction: DE
engagement_type: consulting-audit
tier: partner
f_g_r: F2/G:client-mueller/R-medium
bias_class: [REP, LNG]
promotion_signal:
  - "3 successful pilots of same shape → promote onboarding-template to core/"
```

### §16.4 Почему 7 дней достижимо

- `emergence-surface` **готов** писать claim-ы с Day 1 (F-G-R дисциплина уже есть).
- Capability capsule overlay — **копия** существующего capsule с client-specific edits (≤30 минут).
- ACL tier provisioning — filesystem permissions + frontmatter tier:. Не rockets-science.
- `07-first-week-success-metric.md` — initial BA-0 launched; дальнейшее delivery — по Alpha-прогрессии.

### §16.5 3-pilot promotion

После 3 успешных pilot-ов того же shape, emergence-surface template → `core/onboarding-templates/{shape}.md`. Это **эмерджентный гардеринг** onboarding процесса.

**Triad:**
- **Structure param**: 7-artefact sequence жёсткая.
- **Signal**: pilots matching shape × success rate.
- **Criterion**: 3 successful → promote to `core/onboarding-templates/`.

### §16.6 C1 / AP-6 (no `/home/ruslan/*`)

Все пути в manifest-ах repo-relative. `$JETIX_ROOT` env-var поддерживается. Hook-5 D-test на `jetix-os/` и `agents/*/`. C1 structural-by-default.

---

## §17. Answer to Q15 — USB-C Protocol Layer (harvested, not speculated)

### §17.1 Emergent подпись: **harvested, not drafted**

Lock 20 / C19: Jetix-defined standards для AI↔business cooperation. Обычная интерпретация: *«architect drafts standards Day 1»*. Emergent пересматривает: **standards emerge from real interaction patterns; Phase-1 = harvesting infrastructure, не drafting.**

### §17.2 Phase-1 pipeline

```
agent A handoff to agent B
  ↓  каждый handoff публикует message shape в:
emergence-surface/protocol-candidates/{pattern-name}/{YYYY-MM-DD}-{agent-pair}.md
  ↓  daily consolidation (knowledge-synth):
if ≥3 independent handoffs того же shape за 14 days with stable envelope:
  ↓  promote:
core/protocols/{pattern-name}-v{N}.md (draft standard)
  ↓  meta-agent review + DRR Δ-2 → version-bump
```

**Phase-1 deliverable**: pipeline работает; первые 0-2 кандидата промотированы в `core/protocols/`. **Не** standards submission. **Не** verification harness.

### §17.3 Phase-2a: verification harness

Phase-2a (после €20-50K / triple-AND): архитектор добавляет `tests/protocol/{name}/` — fixtures + test-runners. Каждый промотированный протокол получает conformance-test. **Пишется ПОСЛЕ** того, как паттерн стабилизировался — не ДО.

### §17.4 Phase-3+: standards submission

Только после того, как протоколы работали на ≥3 roys и ≥2 external partners, — submission в external standards body (IETF / ISO / IEEE). К этому моменту это не draft; это **evidence-driven specification** с proven interoperability.

### §17.5 Почему этот путь сильнее, чем Day-1 drafting

- **Drafts приглашают review** («изменить этот пункт»); **evidence приглашает adoption** («уже работает, внедрим»).
- Day-1 standards speculate о interaction patterns, которые ещё не случились; harvested standards описывают patterns, которые уже случились.
- К €200K gate Jetix **владеет** набором de-facto standards, выросших из реальной кооперации — **это сильнее Phase-1 positioning**, не слабее.

**Triad:**
- **Structure param**: promotion threshold (≥3 handoffs × 14d × stable envelope); `protocols/` directory в `core/`.
- **Signal**: handoff shape recurrence count.
- **Criterion**: ≥3 recurrences stable for 14d → promote draft; pass BA-0/1/3 → finalise as core/protocol.

### §17.6 Phase-1 concrete output

```
emergence-surface/protocol-candidates/
├── agent-handoff/
│   └── 2026-04-21-inbox-processor-to-knowledge-synth.md  # one sample
├── contract-fixation/
│   └── 2026-04-25-sales-lead-to-acceptance-authority.md  # one sample
└── README.md    # pipeline explainer

core/protocols/                       # empty Day 1; populated on promotion
```

К концу Phase 1 (€50K gate), если Emergent работает как ожидается, 1-2 протокола промоутированы. Это **меньше Phase-1 артефактов**, чем у Deep-Tech (§17 там прямо публикует 2 протокола Day 1), но **больше доказательств**, что эти протоколы вообще нужны.

### §17.7 Trade-off vs Deep-Tech

- **Deep-Tech**: Day 1 публикует 2 reference protocols + verification harness. Buyer-credibility **немедленная**, но протоколы могут оказаться не-used.
- **Emergent**: Day 1 готовит **harvesting infrastructure**. Buyer-credibility **отложенная** (к €200K), но промотированные протоколы **гарантированно use-case-driven**.

Stage 7 hybrid-candidate: взять Emergent's harvesting pipeline **плюс** Deep-Tech's 2 seed-reference-protocols Day 1 (Bootstrap-комбо).

---

## §18. Foundation Layer Specification (thickest section — trellis = Foundation)

> *«Foundation = главный актив»* (D2 §14).

В Emergent Foundation = **шпалера**: набор жёстких структурных параметров, внутри которых эмерджентность разрешена. Все 8 элементов D4 §4 — spec-complete Day 1. Эмерджентность **не** заменяет Foundation; **работает на** Foundation.

### §18.1 FE-1 — Wiki + ATOM-REGISTRY

**В core**: `wiki/core/` 9 entity types; 9-10 typed edges в `wiki/graph/edges.jsonl` (append-only). ATOM-REGISTRY в `wiki/core/foundations/atoms/`.

**В emergence-surface**: `claims/` (daily decentralized write), `co-citation-graph/` (built from claims).

**Promotion rule**: §3.4. **Триада**: min 3 claim-ов / F≥4, R≥medium / 14d stability → promotion. Trellis-set.

### §18.2 FE-2 — Agent contracts

5-block `role.md` (P2 / IP-1) + `executor-binding.yaml` + **`capability-capsule.yaml`** (Emergent-специфический третий файл). 18 Day-1 manifest files (11 + 5 Ruslan + 2 stubs). **Trellis-set**: schema жёстко; capsule-content эмерджентен через bid-history.

### §18.3 FE-3 — Handoff protocols

`core/protocols/` (promoted drafts; Day 1 — 0-1 seeds); `emergence-surface/protocol-candidates/` (harvesting pipeline). Message envelope с `acting_as:` (hook-4). F-G-R mandatory (hook-3). **Trellis-set**: envelope schema + hooks; **эмерджентное**: какие именно протоколы кристаллизуются.

### §18.4 FE-4 — Escalation protocols

4-class taxonomy (atom-2558) + CP-5 gate YAML (D6 §4.5). Non-emergent жёстко (§15). **Эмерджентное**: department topology (эскалация-паттерны могут триггерить ревизию границ департаментов через meta-agent quarterly audit).

### §18.5 FE-5 — Shared memory

3-layer (D4 §4.5): `wiki/` + `alphas/` (8 past-participle state machines per D6 §6.2) + per-agent (`system.md` / `strategies.md` / `scratchpad.md` / mailbox). Single event log Phase 1 + Life-OS physical separation (C15).

**Emergent Adaption**: per-agent `strategies.md` = **наблюдаемая эмерджентная specialization**. Начинается пустым; каждую неделю `knowledge-synth` дописывает в него сводку выигранных bid-ов и их паттернов. Это делает emergent specialization **видимой** и аудируемой.

### §18.6 FE-6 — Continuous quality metrics

- Per-commit: F-G-R frontmatter (hook-3); `acting_as` (hook-4).
- Per-workflow: F.11 Method Quartet Harmonisation monthly per-direction.
- Per-gate: B.4 Canonical Evolution Loop в 4 ритуалах (daily/weekly/monthly/quarterly).
- **Emergent-дополнительно**: 7 эмерджентных сигналов §14 E-1..E-7, непрерывно измеряемых.

Aggregate: orphans, contradictions, stale claims, F-G-R compliance %, promotion-rate.

*«Continuous, every iteration — NOT periodic»* (D2 §6) — сигнал capture непрерывен, surface еженедельный.

### §18.7 FE-7 — Dashboard

§14 v1 / v2 / v3. Weekly markdown Phase 1. **Эмерджентная добавка**: 7 signal-viewpoints — прибор-панель шпалеры.

### §18.8 FE-8 — Reserve routes / failover

- Multi-provider `compute-contract` с `fallback_chain[]` (§9).
- Duplicate contractors (≥2 lawyers / designers / backup Steuerberater).
- State snapshots: git = recovery (каждая session = commit).
- Agent-tier classification (Tier 1 critical / Tier 2 important / Tier 3 non-critical).
- Crisis playbooks (MC1 P1-#4): 6h Phase-1 allocated; playbooks in `ops/playbooks/`.

### §18.9 FE-bonus — F-G-R tagging (Foundation-element per D4 §4.5)

Hook-3 enforces. Composition rule: weakest-link, pathwise justification (D6 §12.7). Bridge-only reuse → R only. Bias-class audit (5-class REP/ALG/VIS/MET/LNG) per deliverable (D6 §12.10).

### §18.10 10 жёстких структурных параметров (шпалера)

| # | Trellis element | Phase-1 enforcement | Never emergent |
|---|---|---|---|
| T-1  | Hub-and-spoke topology (manager ≤20 active) | mailbox-counter + bidding-protocol step-3 | ✓ |
| T-2  | 4-class escalation                            | atom-2558 + CP-5 schema                  | ✓ |
| T-3  | FPF-contracts (5-block role.md + capsule)     | JSON-Schema validator                    | ✓ |
| T-4  | Gentleman/Predator мембрана                    | hook-2 tier-cross + tone-profiles.yaml   | ✓ |
| T-5  | Revenue-gate enforcement hooks                 | middleware + gate-state.yaml             | ✓ |
| T-6  | Capability-capsule schema                      | YAML schema + CI-validator              | ✓ |
| T-7  | Bidding-protocol spec                          | `core/capability-capsule/bidding-protocol.yaml` | ✓ |
| T-8  | Claim-promotion rules                          | `core/promotion-rules/*.yaml`           | ✓ (ruleset; values tuneable по DRR) |
| T-9  | F-G-R discipline                               | hook-3                                   | ✓ |
| T-10 | Reserve-routing tree                           | `core/reserve-routes/failover-tree.yaml` | ✓ |

**Эмерджентность происходит ВНУТРИ этой шпалеры.** Вне шпалеры — эмерджентность запрещена, это drift, это провал.

### §18.11 Foundation quality invariants (10) — continuous across $0 → $1T

| # | Invariant | Phase-1 mechanism | $1T mechanism |
|---|---|---|---|
| FQ-1  | Hub-and-spoke preserved                    | mailbox counter            | same + graph-DB queries |
| FQ-2  | Membrane tier-crossing controlled          | hook-2 + convention         | same + per-roy federation |
| FQ-3  | Every claim has F-G-R                      | hook-3                      | same |
| FQ-4  | CP-5 gate per L1/L2 decision               | YAML template + audit      | + external auditor |
| FQ-5  | Every integration has failure_mode         | contract-manifest          | same |
| FQ-6  | Every agent has capability-capsule         | JSON-Schema               | same |
| FQ-7  | Every project closes with BA-3             | hook-4 alpha check         | same |
| FQ-8  | Token ops orthogonal to ACL                | schema-level (Phase 2+)    | formal verification |
| FQ-9  | Promotion-rate в полосе ±1σ               | meta-agent weekly audit    | continuous + alerting |
| FQ-10 | D-test: jetix-os/core/ Jetix-term free    | hook-5                     | same |

**10 invariants. 10 механизмов. Scale trajectory defended.**

---

## §19. Hard Constraints Compliance Matrix (21 × 4)

| C# | Constraint (short) | Emergent compliance mechanism | Residual risk | Mitigation |
|---|---|---|---|---|
| C1 | Solo-now-team-ready         | Capability-capsules = team-onboarding seam; 18 Day-1 manifests | capsule-content could drift to de-facto single-user patterns | meta-agent quarterly audit — `home-dept distribution` signal |
| C2 | Revenue-gated spend         | Middleware на всех API; gate-state.yaml; bid-rejection при over-budget | Emergent-agent может биддить за Phase-2 work Phase-1 | hard bid-gate в step-3 bidding-protocol |
| C3 | Closed outside / open inside | 4-tier ACL + hook-2; auto-gen pipeline для public from core | emergent cross-tier link в claims | daily meta-agent audit |
| C4 | Filesystem = SoT            | wiki/emergence-surface/ + wiki/core/ — файловая система; Notion mirror only | Notion-first writes (human error) | CLI `notion-mirror.sh` принудительно; CI audit |
| C5 | Consulting-first Phase-1    | jetix-company/sales/ Day-1; matchmaker external — Phase-2+ | Emergent temptation to build matchmaker engine Phase-1 | explicit §12 — Phase-1 kit = doc only |
| C6 | Productization over hours   | `core/content/` + archetype templates Day 1 | Emergent focus on protocols could shadow productization work | dashboard viewpoint `productized_revenue_pct` |
| C7 | Investment-fund philosophy  | DRR schema has expected_return + horizon + kill_criteria | emergent patterns без ROI-justification | meta-agent quarterly: DRR-ROI completeness audit |
| C8 | Layered identity            | 11 archetypes + face/frame metadata in frontmatter | emergent content без face-declaration | hook-validator на content frontmatter |
| C9 | Universality                | emergence-surface/ + jetix-os/core/ base-clean; overlay for Jetix | emergent claim accidentally references Jetix strings in base | hook-5 D-test + C-test dry-runs |
| C10 | English+US primary Phase-1 | icp/ defaults EN+US; jurisdiction field | emergent DE-first drift | dashboard sales-jurisdiction split |
| C11 | JETIX-FPF mandatory         | capability-capsule extends FPF role-manifest (never replaces) | capsule authors forget FPF bindings | JSON-Schema validator requires `fpf_bindings` non-empty |
| C12 | Role ≠ Executor             | 3-file separation (role.md + executor-binding.yaml + capsule.yaml) | accidental merge | schema + CI |
| C13 | F-G-R mandatory             | hook-3 enforces frontmatter | hook-bypass attempts | pre-receive hook on GitHub side too |
| C14 | 11-agent canonical          | Day-1 18 manifests (11+5+2 stubs); capsules — overlays | **Emergent primary risk**: capsule bidding drifts to de-facto 12th agent | see §4.4 + dashboard E-4 (boundary-drift signal) |
| C15 | Life-OS physical separation | `life-os/` folder; hook-1 asymmetric ban | — | — |
| C16 | Continuous quality          | 7 emergent signals continuous capture; daily promotion | signal capture discipline could lag | meta-agent daily report |
| C17 | Gentleman/Predator          | **HARD — non-emergent.** 2 tone-profiles YAML; hook-2 membrane | emergence accidentally softens inside-tier interactions with outside | §8.4 two-namespace discipline |
| C18 | $1T no-rewrite              | 7 SI invariants (§6.2); promotion-additive core | emergent patterns require schema revision | DRR Δ-2 per schema change |
| C19 | USB-C + enterprise-fast     | Phase-1 harvesting pipeline; draft protocols by €200K | "harvested" read as "missing" by investors | explicit §17.5 positioning defense |
| C20 | ICP 5-criteria + direction  | pilot-manifest.yaml fields Day 1 | — | — |
| C21 | Token Option B              | §10 orthogonality invariant; Phase-1 spec-only | — | schema-level forever-invariant |

**Все 21 constraint имеют механизм.** C14 и C17 — главные Emergent risk, явно адресованы (§4.4, §8.4) и инструментированы сигналами (E-4, E-7).

---

## §20. Anti-Patterns Avoidance Statement (16 × 3)

| AP# | Anti-pattern (short) | How Emergent avoids | Warning sign to monitor |
|---|---|---|---|
| AP-1  | Notion-as-primary-store   | Notion W-only; filesystem mirror | commit-diff shows Notion-first writes |
| AP-2  | Hour-billing-only         | multi-tier SKU schema; productized % target | SKU split dashboard < 40% @ €200K |
| AP-3  | Mass-market / engagement  | structural emergence, NOT behavioral (§13.5) | dashboard viewpoint with `engagement_score` proposed |
| AP-4  | Public OSS of core        | ACL tier core-internal-forever | public-link to core/ in emergence-surface traces |
| AP-5  | Jetix-specific in base    | D-test + emergence-surface/ in base-clean path | grep hits in jetix-os/core/ |
| AP-6  | One-person assumptions    | capability-capsules = team-seam; no /home/ruslan/* | hook-5 grep hits |
| AP-7  | Slow-corporate governance | SLA on CP-5 L2 24h; emergent topology revision quarterly | time_to_review monthly average |
| AP-8  | Chaotic-startup governance| every decision → DRR (D6 §12.14); promotion-rules audit | uncited promotions in core/ |
| AP-9  | Motivational-circle       | 5-criteria + direction-of-life filter (hard C20) | community-claim без criteria score |
| AP-10 | Attention-extraction      | no push notifications Phase-1 | notification-proposal in emergence-surface |
| AP-11 | Single-provider AI        | fallback_chain mandatory in compute-contract | validator rejects empty fallback |
| AP-12 | Pure-research Phase-1     | emergence-surface is work-area, не research lab; bid-pool tied to revenue | research-claims without revenue alignment |
| AP-13 | Public token + gov/access | orthogonality invariant (§10.4) | any ledger-entry correlating tier with ownership |
| AP-14 | Equal-weight channels     | site=primary, social=TOF only (Lock 12 coded in routing) | deep content auto-published to social |
| AP-15 | Monolithic brand          | frame_tag + archetype_keys frontmatter | content без frame/archetype declaration |
| AP-16 | **Boutique-scale shortcuts**| **Emergent hidden risk**: thin prescribed structure can become solo improvisation | meta-agent quarterly audit — "trellis state" report card |

**AP-3 / AP-9 / AP-10 triple-statement (emergence = structural, not behavioral):** §8.5, §13.5, §14.5. **Третий раз сейчас:** эмерджентность в Emergent — паттерны в графе взаимодействия (ко-цитирование, bidding-победы, capability-кристаллизация). **Не** reward-loops, **не** engagement-mechanics, **не** motivational-content. Dashboard измеряет substance throughput и time-saved, никогда time-spent или engagement-score.

**AP-16 Emergent-specific defence**: thin prescribed structure **не значит** laziness. Шпалера (§18.10 — 10 элементов) — плотная Day 1. Emergent инвестирует в **Foundation**, а **не** в Phase-1-surface. Это противоположно boutique.

---

## §21. Self-Scoring on D4 §8 Quality Axes

| Axis | Weight | Self-score | Contribution |
|---|---|---|---|
| 1. Phase-1 readiness      | 20% | **7/10**   | 14.0 |
| 2. Scale trajectory       | 15% | **7/10**   | 10.5 |
| 3. Foundation quality     | 15% | **7/10**   | 10.5 |
| 4. Locks compliance       | 18% | **7/10**   | 12.6 |
| 5. Universality           | 10% | **8/10**   |  8.0 |
| 6. Operational simplicity | 10% | **9/10**   |  9.0 |
| 7. Cost efficiency        |  0% | **PASS**   | gate |
| 8. Resilience             |  5% | **7/10**   |  3.5 |
| 9. Security posture       |  5% | **7/10**   |  3.5 |
| 10. Innovation            |  2% | **8/10**   |  1.6 |
| **Total (weighted)**      | **100%** |       | **~73.2** |

### §21.1 Defence

**Axis 1 — Phase-1 readiness: 7/10.** Скелет работает Day 1. Capability-capsule за 20 минут на агента. Bidding-протокол — 3-step markdown процесс. Но патэрны кристаллизуются за недели — наделю 1-4 deliverable может выглядеть sparse. Это честный 7, не 9 (Conservative).

**Axis 2 — Scale trajectory: 7/10.** SI-инварианты (§6.2) защищают $1T-trajectory. Но «эмерджентность предсказуемо масштабируется» — тезис, требующий обоснования. Обосновано (§6.1, §6.4): структурные параметры ужесточаются с ростом. Не 9/10, потому что обоснование уязвимо для «что если промоушен-пайплайн застрянет».

**Axis 3 — Foundation quality: 7/10.** Шпалера Day-1 full-spec (§18). Но enforcement **распределён** (4 hooks + meta-agent signals) vs Maximalist-централизованный. Слабее на принуждение, сильнее на прозрачность. 7 честный.

**Axis 4 — Locks compliance: 7/10.** Все 24 locks + 21 constraint адресованы. C14 и C17 требуют аргументации (есть). Не 9/10, потому что напряжение есть — читатель, проверяющий compliance buchstablich, может сомневаться.

**Axis 5 — Universality: 8/10.** `emergence-surface/` — чистейший overlay-паттерн. Base-layer Jetix-term free (hook-5). Kit-replication (§12) — harvested overlay. 8 обосновано.

**Axis 6 — Operational simplicity: 9/10.** **Сильнейшая ось Emergent.** Меньше предписанной структуры = меньше поддерживать. 4 blocking hook-а vs 7 у Deep-Tech. 18 manifest-ов (как Deep-Tech) + простой bidding-протокол. Новый pilot читает: Foundation spec (§18) + 7-artefact onboarding (§16). 9 обосновано.

**Axis 7 — Cost efficiency: PASS.** Phase-1 est ≤ €500/mo. Compute при bid-торге — Haiku-default, Sonnet-on-demand. Под €800 gate с запасом.

**Axis 8 — Resilience: 7/10.** Multi-provider, duplicate contractors, git-recovery. Но distributed enforcement менее отказоустойчив к operator fatigue — Ruslan может пропустить один weekly dashboard и promotion-rate подрейфует.

**Axis 9 — Security posture: 7/10.** Мембрана жёсткая (§8). 4-tier ACL. CP-5 gate (§15). Но emergence-surface — дополнительная attack-surface; signal-set должен её покрыть. 7 честный.

**Axis 10 — Innovation: 8/10.** Self-organising paradigm для соло-оператора — по-настоящему ново. Capability-capsule + bidding = свежее. **Но** OME уже содержит role-declared-not-folder-pinned специализацию; Emergent её формализует, не изобретает. 8 — ceiling; 9-10 было бы inflated.

### §21.2 Weighted total

Сумма: **73.2/100**. Диапазон честного self-assessment: **73-78** (если капсулы кристаллизуются быстрее — ближе к 78; если promotion-пайплайн буксует — ближе к 73). Показатели на hard-floor §8.3 не попадают.

---

## §22. Variant Contrarian Claims

Три мягких несогласия с D4, каждое — **запрос на уточнение, не коррекция**.

### §22.1 Контрадикция 1 — D4 Q15 USB-C Phase-3+

**D4 позиция (Q15)**: "Jetix-defined standards"; 3 workstreams (protocol / tools / verification); Phase-3+ submission.

**Emergent позиция**: "Jetix-harvested standards" Phase 1; drafted Phase 2; submitted Phase 3+. Сильнее аргумент: evidence-driven protocols приглашают adoption, draft protocols приглашают review.

**Резолюция**: не конфликт с D4 — уточнение положения "Jetix-defined" в сторону "Jetix-harvested". Stage 7 решает.

### §22.2 Контрадикция 2 — Phase-2/3 features designed Day 1

**D4 позиция (§3)**: capabilities Phase-2/3+ должны быть архитектурно продуманы Day 1.

**Emergent позиция**: если promotion-rate из emergence-surface достаточен, Phase-2/3 features **выкристаллизовываются** к своему gate — не нужно designed-Day-1 surface. Это НЕ предложение пропускать Phase-2 spec-работу; это предложение, что **spec = harvested artefact**, собранный к gate-активации.

**Резолюция**: спрос на уточнение — может ли "designed Day 1" быть трактован как "spec-поверхность готова Day 1, заполнение из эмерджентности"?

### §22.3 Контрадикция 3 — D6 §2.2 specialization pre-assigned

**D6 позиция**: canonical 11 agents с pre-assigned department + function.

**Emergent позиция**: department = **декларируемая** с capability-capsule + threshold cross-dept bidding, вместо pre-assigned. Departments — light-bound containers, не walls.

**Резолюция**: Emergent **не меняет** canonical roster (11 агентов, D6-compliant). Добавляет capsule-overlay с declared home-dept. Не конфликт — расширение. Stage 7 может принять, отклонить, или попросить hybrid.

---

## §23. Risk Profile (top 7)

| # | Risk | Probability | Impact | Leading indicator | Mitigation | Residual |
|---|---|---|---|---|---|---|
| R1 | **Convergence failure** — patterns don't stabilize | Med (30%) | HIGH | promotion-rate trailing-30d < 1/wk after week 6 | meta-agent escalates; Ruslan tightens threshold / adds structure-param | if persistent 60d → hybrid pivot |
| R2 | **C14 / C17 drift** — capsule bidding creates de-facto 12th; mem softens | Low-Med (20%) | DISQUALIFIER if materialised | bid-diversity entropy > threshold; membrane-trace anomaly | hard bid-gate at step-3; separate middleware on membrane; monthly audit | none — killed by hook |
| R3 | **Phase-1 visible-progress deficit** — week 1-4 sparse | High (60%) | MED (perception) | weekly dashboard appears quiet | seed-content Day 1; honest Executive Summary narrative | acknowledged trade-off |
| R4 | **Compute-spend drift** — richer protocols → more agent exchanges | Med (25%) | HIGH if over €800 | compute-ledger weekly trend | capability-capsule compute_tier cap + Haiku default | block at middleware |
| R5 | **Promotion-threshold misconfiguration** — too loose / too tight | Med (30%) | MED | promotion-rate variance outside ±1σ band for 14d | Ruslan-tunable parameter; DRR log | adjustable; not fatal |
| R6 | **Meta-agent gardener overload** — quarterly insufficient at scale | Low (10%) Phase 1; rising | MED | meta-agent audit backlog > 2 quarters | promotion cadence tightens with phase (daily → hourly @ $100M+) | scale-contingent |
| R7 | **Emergence-vs-anarchy perception** — partners/investors read "emergent" = "ad hoc" | Med (25%) | MED | partner/investor feedback | §18 Foundation spec unambiguous; external communication uses "structured self-organization" | narrative discipline |

---

## §24. Selection Case for Ruslan

**Выбери Emergent, если:**

- Веришь, что **$1T-scale устойчивость рождается из дисциплинированной самоорганизации внутри жёстких стен**, а не из pre-scaffolded Day-1 surface.
- Ценишь **operational simplicity и cost efficiency** выше Phase-1 visible-progress velocity.
- Готов инвестировать в **дисциплину измерения** (signal set) вместо **дисциплины расширения** (Maximalist scaffold).
- Видишь **шпалеру как Foundation**, а не сценарий Day 1.
- Принимаешь, что неделя 1-4 будет выглядеть sparse, потому что паттерны ещё не накопились — и это **ожидаемое поведение**, а не отказ.

**Не выбирай Emergent, если:**

- Q2 consulting velocity — единственное связующее ограничение, и формалистический риск или convergence-риск недопустим → выбрать Conservative.
- Нужна видимая Phase-1 capability scaffold для investor/partner demo → выбрать Maximalist.
- Emergence-surface convergence latency невыносима → выбрать Conservative.
- Веришь, что формальная верификация token-state-machine Phase-1 стоит своей стоимости → выбрать Deep-Tech.

**Hybrid candidates (Stage 7 частичное усыновление):**

1. **§4 capability-capsule + §11 bidding-протокол** — без остальной эмерджентности. Добавляет rich task-routing к Conservative-варианту.
2. **§17 harvesting pipeline** — без Day-1 promoted protocols. Seeds USB-C к €200K gate, не Day 1.
3. **§14 emergent signal set** — добавить к любому другому варианту. 7 signal-viewpoints = приборная панель шпалеры — полезны любому варианту.

**Not composable individually** (требуется полный Emergent):

- §3 sparse skeleton + `emergence-surface/` двухконтурная — переносит архитектурные consequences во все другие секции.
- §7 decentralized write + централизованная consolidation — требует emergence-surface/ как целой директории.

---

**Pick Emergent if you believe the trellis is Foundation and the plant should grow where it finds light — within the hard walls you have already built.**

*«Foundation = главный актив.»* *«AI = electricity.»* *«Gentleman inside / Predator outside.»*

Эмерджентность — структурная, не поведенческая. Эмерджентность — гипотеза + измерение + фальсификация. Эмерджентность не пересекает мембрану. Trellis not cage.

---

## Appendix A — Emergence Triad Audit (per emergence claim)

Каждое утверждение «здесь возникает паттерн» в документе имеет триаду. Консолидированный индекс:

| § | Claim | Structure param | Observable signal | Convergence criterion |
|---|---|---|---|---|
| §3.4 | Concept promotion from emergence-surface to core | 3 claims / F≥4, R≥medium / 14d / 2 agents | co-citation density, claim count, F-G-R median | density ≥0.35 × 48h stability, no R-high contradiction |
| §4.2 | Capsule task_shape расширяется in bid-history | 70% win + ≥10 hits / quarter | bid-win-rate per shape per agent | 70% × 10 hits → DRR promote |
| §4.4 | Capability-capsule NOT 12th agent | 1.3× threshold, 50% audit | cross_department_bid_fraction per agent per quarter | 50% × 2 quarters → escalation |
| §6.3 | Vertical specialization via bid-victories | 10+ wins in new shape in 1 quarter | bid-log win count per shape | 10+ wins → DRR capsule-расширение |
| §6.4 | USB-C protocol promotion | ≥3 handoffs same shape × 14d + stable envelope | handoff shape recurrence | 3 × 14d → draft in core/ |
| §7.3 | Wiki typed edges emerge from co-citation | co-citation graph + hand-drawn priors | new edges/week vs hand-drawn baseline | >20% auto-discovered edges by Phase-2a |
| §11.4 | Specialization via bidding-hit frequency | task_shape, 70% win-rate | bid-win per shape per agent | 70% + ≥10 → capsule-extension DRR |
| §13.3 | Content-cadence as health signal | 1 deep/mo + 2 mid/mo + 3 TOF/wk declared | publication timestamps | variance > 40% × 14d → escalation |
| §14.1 | 7 emergent signals (E-1..E-7) | each signal has declared threshold | each signal has source file | each has escalation criterion |
| §15.3 | Department topology evolution | 40% cross-dept threshold | escalation-class frequency per department per quarter | 40% × 2 quarters → topology DRR |
| §16.5 | Onboarding-template promotion | 3 successful pilots of same shape | pilot-success by shape | 3 successful → template promotion to core/ |
| §17.2 | USB-C protocol-harvest pipeline | 3 recurrences × 14d × stable envelope | handoff shape frequency | 3 × 14d → draft standard |

**12 emergence claims × 12 triads.** Каждая триада specified; ни одной «драфт-эмерджентности».

---

## Appendix B — Locks Coverage Matrix (24 × 3)

| Lock | Section(s) | Mechanism |
|---|---|---|
| D1  | §8, §15.5 | Gentleman/Predator; tone-profiles; external-relations routes |
| D2  | §4, §6, §16 | solo-now-team-ready via capsules; multi-pilot seam |
| D3  | §8 ACL | 4-tier; hook-2 tier-cross |
| D4  | §3 (Jetix name) | canonical normalization in ingest |
| D5  | §3, §5 (consulting primary) | jetix-company/sales/ Day-1 |
| D6  | §4, §11 | advisory slot parked; no advisor-role manifest |
| D7  | §4.1, §13 | 11 archetypes; 11 capsules seed-bias |
| D8  | §13, §22 | layered identity; frame_tag + archetype_keys |
| D9  | §13.2 | frame_tag: pain-primary default |
| D10 | §5 (Phase-1 EN+US default) | icp/ jurisdiction field |
| D11 | §5, §14 | consulting + producer + fund: 3 lines |
| D12 | §13 | site primary; social = TOF only |
| D13 | §8 | surface/core auto-gen; hand-maintained duplicates forbidden |
| D14 | §20 AP-12 | research revenue-instrumental Phase 1 |
| D15 | §6.6, §9, §10 | revenue-gated spend enforcement; gate-state.yaml |
| D16 | §5 (Phase-1 chat), §3 | simple Telegram adapter; peer-review Phase-3+ |
| D17 | §3, §5 AP-1 | filesystem = SoT; Notion mirror only |
| D18 | §13 | productization via content template + multi-tier SKU |
| D19 | §6 | $1T trajectory; 7 SI invariants |
| D20 | §17 | USB-C harvest Phase-1; promoted drafts Phase-2a+ |
| D21 | §11, §12 | matchmaker + roy-replication (both emergent-harvested) |
| D22 | §4, §13, §16 | ICP 5-criteria + direction-of-life; pilot-manifest field |
| D23 | §10 | token Option B; orthogonality invariant |
| D24 | §13, §20 AP-4 | research split (open Phase-2+ / closed core forever) |

**Все 24 locks в ≥2 секциях.** Matrix — для Stage-7 verification.

---

*End of JETIX-ARCH-V5-EMERGENT.md. Build the trellis. Let the plant grow.*
