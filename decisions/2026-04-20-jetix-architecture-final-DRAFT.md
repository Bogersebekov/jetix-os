---
id: 2026-04-20-jetix-architecture-final
title: Jetix Architecture v1 — Final Decision Record (DRAFT v0.5)
date: 2026-04-20
state: draft
review_stage: 3.5
based_on:
  - decisions/2026-04-19-architecture-v2-approval.md (approved 2026-04-20)
  - raw/research/architecture-synthesis-v2-final.md
authors:
  decision_maker: ruslan
  scribe: claude-opus-4-7
purpose: >
  Clean consolidation Stage 3 review decisions. Single source of truth
  for Stage 4 writers (D1-D8 чистовики). Will be finalized в Stage 4.5
  after D1-D8 written.
size_target: 10-15 pages
lang: [ru, en]
english_summary: >
  Final Architecture Decision Record for Jetix v1 Phase 1. Consolidates
  Reference vs Operational Architecture split, 8 core principles, 15 folders,
  18 role manifests, 8 true alphas, full FPF (max Левенчук depth),
  Portfolio of Directions model, 7+7 day rollout, €275-737/mo run rate.
  Includes 11 Ruslan overrides on top of v2 synthesizer recommendations.
unblocks:
  - Stage 4: D1-D8 writing
  - Stage 4.5: D9 finalization
---

# Jetix Architecture v1 — Final Decision Record (DRAFT v0.5)

## Section 1 — Context

### 1.1 Что такое Jetix

Jetix — AI-native mega-corporation, оперируемая solo founder'ом (Ruslan,
Berlin) при кооперации с array Claude-агентов. Primary market — DACH
Mittelstand; secondary — US и русскоязычные клиенты через unified funnel.
Правовая траектория: Freiberufler (Phase 1) → UG (Phase 2a) → GmbH
(Phase 2b+) → потенциально Holdings (Phase 2c+).

Архитектурная парадигма: **Company-as-Code** (git = единственный source
of truth) + **Portfolio-of-Directions** (холдинг для cross-functional
наблюдения за множественными business-ставками) + **ШСМ-дисциплина
Левенчука** на максимум (ontology не-компромиссна).

### 1.2 Stage 3 review — зачем и как

Stage 3 представлял собой multi-perspective audit изначального
`architecture-implementation-synthesis-2026-04-19.md` (v1, 1592 строки).
Применена была 5-chat methodology: 4 reviewer-persons (Critic /
Simplifier / Mega-Corp / Левенчук) независимо разобрали v1 →
synthesizer собрал `architecture-synthesis-v2-final.md` (1621 строка) с
38 accepted changes, 12 rejected changes, 6 meta-conflicts resolved,
5 outstanding tensions.

Ruslan-owned approval прошёл в 7 чанках (2026-04-19 — 2026-04-20),
зафиксирован в `decisions/2026-04-19-architecture-v2-approval.md`
(APPROVED). В процессе Ruslan внёс **11 overrides** на top of v2 —
все в направлении усиления (больше Левенчук, не меньше; больше
scaffolding, не меньше; раньше physical separation, не позже).

### 1.3 Inputs упорядочены по waves

- **9 deep-research waves** (`raw/research/*-deep-research-*.md` + два
  hybrid-framework synthesis документа) — foundation
- **v1 synthesis** (`architecture-implementation-synthesis-2026-04-19.md`)
  — первый attempt
- **4 reviewer reports** (`raw/research/stage2-review/*`) — multi-angle critique
- **v2 synthesis** (`architecture-synthesis-v2-final.md`) — consolidated proposal
- **Approval ADR** (`2026-04-19-architecture-v2-approval.md`) — Ruslan decisions

### 1.4 Outcome summary

Stage 3 закрылся с three архитектурными commitments:

1. **Reference vs Operational split** — полный 7-layer L0-L7 design-time;
   Phase 1 материализует 4 layers (L0 Executive Core + L1 Foundation +
   L2 Cognitive as discipline + L4 Revenue).
2. **8 core principles** (с Portfolio-of-Directions добавлен 8-ым).
3. **Phase 1 operational minimum viable architecture** — 15 folders,
   8 alphas, 18 role manifests, full FPF (30-50 страниц, не FPF-Lite),
   7+7 day rollout, €275-737/mo run rate.

---

## Section 2 — Decision Summary

### 2.1 TL;DR

Jetix Phase 1 строится как Company-as-Code система с git как единственным
SoT, 15-folder structure в parallel-mounted `~/jetix-os/{life-os,jetix}/`
с asymmetric reference rule (Jetix never references Life-OS), 18
role-manifests written в full depth Day 1-9, full FPF (Левенчук
ontology на максимум) загружен текстом в system prompt каждого из 11
агентов, 8 true alphas с past-participle state machines, Portfolio-of-
Directions как 8-ой first-class principle и 8-ая true alpha, resource
accounting в двух tier'ах (Capital+Compute+Deep Hours ledger + Attention
Budget quarterly), 7+7 day rollout (sales Days 1-7, foundation Days
8-14+), ~€275-737/mo run rate, tool stack из 5 (+ Claude Code, git,
Stripe, Toggl, Perplexity).

### 2.2 Key architectural commitments

- Git = SoT. Commit = акт управленческого решения.
- Role ≠ Executor (strict split, 5-block `role.md` + separate
  `executor-binding.yaml`).
- 8 true alphas в `alphas/` с past-participle state machines (strict-enforce).
- Full 3-level mereological creation graph Phase 1 (не Lite).
- L0 Executive Core декомпозирован в 5 atomic Ruslan sub-roles +
  `executors/ruslan.yaml` multi-role-binding.
- DACH primary + US + RU secondary, unified funnel через Stripe.
- Resource accounting quantitative: Capital + Compute + Deep Hours;
  quarterly: Attention Budget; Phase 3 first-class: Ecosystem (11
  категорий).
- Portfolio-of-Directions model: `directions/_active|_hypotheses|_archived/`
  с Direction как 8-ой alpha.
- Physical Life-OS ≠ Jetix separation Day 1 (parallel folders, hook
  enforcement).
- FPF full (не Lite), 30-50 pages, max Левенчук, full-text loading в
  каждый agent system.md, internal-only.

### 2.3 Deferred / triggered

- **Phase 2a triggers (Triple-AND):** €20K MRR × 3mo + Ruslan >40%
  L1/L2 time + ≥1 client requesting GDPR DPA → `git filter-repo`
  extraction Life-OS в отдельный repo.
- **Phase 2b triggers:** Chief of Staff role, FPF-Steward как отдельная
  роль (30+ agents OR 1+ human meta-hire OR quarterly audit >4h).
- **Phase 2c triggers:** 2nd entity → activate federation pattern
  (`entities/jetix-gmbh/` stub становится реальным).
- **Phase 3 triggers:** different servers/clouds; Ecosystem Resources
  first-class; Beirat/Aufsichtsrat formalization.
- **Открыто:** designated trustee identity (not Anton, TBD); trademark
  Jetix vs Disney (Perplexity research + backlog entry, formal
  resolution при €20-50K revenue range).

---

## Section 3 — 8 Core Principles

Каждый principle — foundation ref architecture, applied в Phase 1
operational с explicit implications для D1-D8.

### P1 — Company-as-Code, буквально. Git = SoT

**Statement:** Всё управленческое и организационное состояние
материализуется в git-репозитории. Commit = акт управленческого решения.
Notion decommission — завершён к Day 14 rollout'а.

**Rationale:** Mega-corp scalability начинается с reviewable org-state.
PR как управленческий ритуал даёт audit trail, rollback и distributed
collaboration free. Notion как secondary store создаёт divergence между
external/internal truth — устраняется.

**Phase 1 implication:** все 15 folders под `~/jetix-os/jetix/` живут в
git. Pre-commit hooks (4) enforce invariants: asymmetric reference
(Jetix→Life-OS blocked), Rechnungsnummer monotonicity, role-manifest
required fields, past-participle state check. Auto-translation hook
(5-ый) — OT2 addition.

**Cross-refs:** D1 Section "Reference Architecture"; D2; D8 hooks.

### P2 — Role ≠ Executor

**Statement:** Роль (обязанности, метод, outputs) — archetype. Executor
(agent instance или human) — привязка. Никогда не смешиваются.

**Rationale:** Portability — Phase 1 honesty: roadmap goal v2.0+, не
Phase 1 claim. Но architectural seams разделения соблюдаются строго,
чтобы v2.0+ portability была механической, а не re-architecture'ом.

**Phase 1 implication:** 18 role-manifests (5-block `role.md` —
identity / ontological / method / production_dependencies / evolution)
+ separate `executor-binding.yaml` с compute contract (model_preference,
fallback_models, thinking_mode, max_tokens_per_session, cache_strategy,
latency_class, escalation_rules). Dynamic role assignment forbidden
(кроме founder exception: `executors/ruslan.yaml` с multi-role-binding
flag для 5 atomic sub-roles).

**Cross-refs:** D3 — 18 full-depth manifests.

### P3 — 8 True Alphas + past-participle convention strict

**Statement:** 8 true alphas (Client, Project, Deal, Content Item,
Hypothesis, Member, Way of Working, **Direction**) материализуются в
`alphas/` с past-participle state machines. Work products (Invoice,
Postmortem, Research Note) живут в domain-appropriate folders
(`finance/`, `decisions/postmortem/`, `wiki/sources/`). Entity (SKU) —
в `catalog/` / `decisions/policy/`.

**Rationale:** Alpha = evolving stakeholder-concern. Work product =
deliverable artifact. Смешение первичных и вторичных элементов ломает
дисциплину (Левенчук ШСМ §1.3). Past-participle (`qualified`,
`activated`, `delivered`) — не gerunds (`qualifying`, `activating`) —
обеспечивает точный онтологический статус: завершённое состояние, не
процесс. 52% v1-violations исправлены системным rename'ом.

**Phase 1 implication:** 8 state machines past-participle:

| # | Alpha | States |
|---|-------|--------|
| 1 | Client | lead-identified → qualified → proposed → in-negotiation → won / lost → churned |
| 2 | Project | scoped → kicked-off → started → delivered → closed → in-follow-up |
| 3 | Deal | drafted → signed → activated → completed / cancelled |
| 4 | Content Item | drafted → in-review → approved → published → retired |
| 5 | Hypothesis | formulated → under-validation → validated / invalidated → implemented |
| 6 | Member | applied → invited → activated → flagged-at-risk → churned |
| 7 | Way of Working | drafted → implemented → refined → deprecated |
| 8 | Direction | hypothesized → under-validation → validated → activated → scaled → plateaued / invalidated / dropped → archived |

Pre-commit Hook 4 блокирует gerunds в `state.yaml` файлах. «What ШСМ
is NOT» section — обязательная часть FPF.

**Cross-refs:** D5 Section "8 alpha state machines"; D6 FPF Section 6.

### P4 — Model D Nested Hierarchy + lightweight mereology explicit

**Statement:** Life-OS — корневая система, Jetix вложен как supersystem-
contained в директории `life-os/projects/jetix/` (conceptual model).
Phase 1 physical layout — parallel mount: `~/jetix-os/life-os/` и
`~/jetix-os/jetix/` с asymmetric reference rule.

**Rationale:** Model D (Levenchuk) описывает отношения part-of и
supersystem-contained explicitly. Lightweight mereology (part-of, creates,
operates-in, methodologically-uses, constrained-by) Phase 1 достаточна.
Advanced mereology (Kit Fine) — reference-only в FPF, not materialized.

**Phase 1 implication:** Asymmetric reference enforcement (Hook 1); Phase
2a extraction via `git filter-repo --path life-os/`; Phase 3 physical
separation на разные servers/clouds.

**Cross-refs:** D4 JETIX-VS-LIFE-OS; D6 FPF Section 10 Mereology.

### P5 — L0 Executive Core (декомпозиция + scaffolding)

**Statement:** Strategic management декомпозирован на 5 atomic sub-ролей:
**strategy-lead / framing-lead / sales-closer / acceptance-authority /
external-relations**. Ruslan в Phase 1 — единственный executor с
multi-role-binding флагом (hybrid founder-mode). Agent
`strategy-support-analyst` (renamed от `strategist`, J3) — support-роль,
не strategic decision-maker (agents не стратегируют per Левенчук §1.4).

**Bus-factor scaffolding:** `ops/hit-by-bus.md`, `ops/business-
continuity.md`, `ops/incident-playbook.md`, `ops/disaster-recovery.md`,
`ops/gdpr-art-33.md` + Constitution §11 Service Continuity protocol
(7d/14d/30d escalations) + `governance/trustee-designations.md` с
**placeholder `{trustee: TBD, NOT Anton}`**. Execution Day 13 (не Day 1
priority), до first client contract signed.

**Rationale:** Единая strategic-management роль — Левенчук §1.4
violation (5 distinct competencies merged). 5 atomic sub-ролей дают
clean delegation paths при найме (Phase 2a+). Trustee-identity-open —
Ruslan explicit override: "но это будет потом, это будет тоже не Антон".

**Phase 1 implication:** 18 role-manifests включают 5 Ruslan sub-ролей
с `executors/ruslan.yaml` multi-binding.

**Cross-refs:** D3 manifests list; D8 Day 13 artifacts.

### P6 — DACH primary + US + RU secondary, unified funnel

**Statement:** Primary market — DACH Mittelstand (confirmed). Secondary
с Day 1 — US clients и русскоязычные клиенты. Все проходят через **одну**
воронку и **один** payment flow (Stripe + Wise для currency conversion
externally). Legal entity — DACH-based (Freiberufler → UG → GmbH).

**Rationale:** Ruslan explicit override на v2 synthesis ("DACH-locked
Phase 1-2"). Unified funnel снимает internal multi-currency complexity —
Stripe/Wise обрабатывает conversion externally; internal ledger остаётся
EUR-reported. `finance/currencies.yaml` — placeholder (1h setup), место
держим под Phase 2a expansion.

**Phase 1 implication:**
- `clients/` CRM structure умеет различать jurisdiction в одной системе
- Contract templates: EN primary + DE localization; RU nice-to-have
- `outreach/` split: top-level `_shared/` templates + per-direction
  `directions/*/outreach/{de,en,ru}/` per-language content (cultural
  tuning, не переводы)
- Tax handling: reverse-charge VAT, W-8BEN-E — Steuerberater consult
  Phase 2a
- Trademark Jetix vs Disney: Perplexity research now, formal resolution
  при €20-50K revenue (backlog entry в `decisions/backlog/`)

**Cross-refs:** D1; D2; D4.

### P7 — Resource Accounting (two-tier + Phase 3 Ecosystem)

**Statement:** Jetix учитывает ресурсы в двух измерениях.

**Tier 1 — Quantitative ledger (daily/monthly):**
- **Capital** — деньги, runway, commitments
- **Compute** — machine cognition (tokens, models, thinking-time, cache)
- **Deep Hours** — focused human cognition (attention-weighted time)

**Tier 2 — Strategic allocation (quarterly):**
- **Attention Budget** — focus-theme квартала, % распределение
  внимания по directions (не ledger-metric, а decision-concept в
  `decisions/quarterly/YYYY-QN-attention-theme.md`)

**Phase 3 first-class (infrastructure prep Phase 1):**
- **Ecosystem Resources** — 11 категорий relational capital:
  advisory relationships / community members / partnerships / brand
  equity / DACH institutional networks (IHK, VDMA, BDI, BITKOM) /
  alumni & reference / media & content / talent network / capital
  relationships / academic & research / regulatory & government.

**Rationale (evolution история 3 итераций 2026-04-19):**
v2 synthesis proposed Capital + Hours + Attention. Ruslan added Compute
как 4-ый first-class ресурс (override #1: "заносим в first principles"),
затем collapsed Attention-as-ledger → Attention-as-quarterly-decision,
refined Hours → Deep Hours (attention-weighted time, not wall-clock).
Вариант C (hybrid) — accepted.

**Phase 1 implication:**
- `finance/resource-ledger.yaml` (monthly: Capital + Compute + Deep Hours)
- `finance/compute-ledger.yaml` (tokens/model, API spend EUR, cache-hit
  ratio, rate-limit incidents)
- `decisions/quarterly/YYYY-QN-attention-theme.md` (example: "60% Sales /
  25% Delivery / 10% Architecture / 5% Learning")
- `governance/advisory-board/members.yaml` (Anton/Vladislav/Rodion
  formalized informally — Phase 3 first-class prep)
- Per-executor compute contract (см. P2 implications)
- Toggl `[deep]` vs `[shallow]` tags; target 25-30 deep hours/week founder-mode

**Cross-refs:** D2; D3 (compute contract); D8 (rituals).

### P8 — Portfolio of Directions (holding-style pattern)

**Statement:** Jetix оперирует как портфолио направлений (directions),
каждое — hypothesis → experimentation → activated / dropped cycle.
Jetix сам — research engine + operational infrastructure для multiple
bets, не single-business company.

**Rationale (Ruslan override #8 — 8-ой principle, not was 7):**
> "Jetix = большая корпорация, десятки направлений. Шаурмечные,
> кибербезопасность, AI-tools, и т.д. Википедия должна работать с
> людьми, с CRM, cross-functional. Jetix как холдинг для кросс-
> функционального наблюдения."

Model: **Hybrid Variant 1+4** — folder-per-direction (`directions/
_active|_hypotheses|_archived/<slug>/`) + Direction как 8-ая true alpha
(Portfolio-of-Directions materialized operationally).

**Phase 1 implication:**
- `directions/_active/ai-consulting-dach/` (primary Q2 revenue bet):
  `direction.md` (thesis/ICP/economics/conviction), `hypotheses/`,
  `experiments/`, `research/`, `pipeline.md`, `state.yaml`
- `directions/_hypotheses/*/` — hypothesis-stage direction folders
- `directions/_archived/*/` — dropped с post-mortem
- `directions/README.md` — portfolio dashboard
- `alphas/direction/` — 8-ая alpha с state machine instances (symlinks)
- Graph edges (3 portfolio-specific): `belongs-to-direction` /
  `applies-to-direction` / `sames-as-crm`
- Frontmatter convention: `direction: <slug>` OR `directions: [list]` на
  всех wiki/clients/alphas files

**Cross-refs:** D1; D2; D5; D7 (direction authority: J-Auto open
hypothesis, J-Strategic activate / archive).

---

## Section 4 — Reference vs Operational Architecture Split

Центральная архитектурная абстракция Stage 3 review.

### 4.1 Reference Architecture (L0-L7, design-time)

Полный 7-layer stack — commitment на дизайн-уровне, materialization по
триггерам. Layers:

- **L0** Executive Core (strategic management, decision authority)
- **L1** Foundation (legal entity, compliance, ops, governance)
- **L2** Cognitive (ontology discipline Левенчук, FPF, wiki)
- **L3** Customer Relations (CRM, sales, customer success, community)
- **L4** Revenue (products, deals, invoices, directions operational)
- **L5** Alliance / Community / Membrane (ecosystem gravity)
- **L6** Research Engine (hypothesis portfolio, experiments, insights)
- **L7** Holdings / Federation (multi-entity supersystem)

### 4.2 Operational Architecture Phase 1 MVA

Phase 1 материализует 4 layer'а:

- **L0** Executive Core — 5 atomic Ruslan sub-ролей; `executors/
  ruslan.yaml` multi-binding
- **L1** Foundation — partial: entity-stub `entities/jetix-gmbh/`;
  DPO external-mode; advisory-board informal; ops artifacts Day 13
- **L2** Cognitive as discipline (не папка) — FPF full text loaded в
  каждый agent system.md; wiki/ с 9 entity types; alphas/ с 8 state
  machines; creation-graph full 3-level
- **L4** Revenue — `directions/_active/ai-consulting-dach/` operational;
  SKU в catalog; invoice/contract templates; Stripe configured

**L3, L5, L6, L7 — Reference только, materialization triggered:**

| Layer | Trigger |
|-------|---------|
| L3 CRM infrastructure full | 5+ concurrent clients или Customer Success stub activated |
| L5 Alliance membrane | 1st L4 client closed → Founding Alliance Member |
| L6 Research Engine full | 3+ active directions simultaneously |
| L7 Holdings pattern | 2nd entity emergence (acquisition или split) |

### 4.3 Почему split

Mega-corp readiness без premature-materialization cost. Phase 1
execution lean, но architectural seams preserved для painless scale-up.
Критик v1 review (monolithic 7-layer implementation) + Simplifier
(dropping layers entirely) — оба отвергнуты в пользу Reference-вс-
Operational compromise.

---

## Section 5 — Phase 1 Operational Specifics

### 5.1 15 folders Phase 1 (full list)

В `~/jetix-os/jetix/`:

| # | Folder | Purpose |
|---|--------|---------|
| 1 | `agents/<id>/` | Combined role + executor + system + scratchpad (11 agents) |
| 2 | `alphas/` | 8 subfolders с past-participle state machines |
| 3 | `alpha-log/` | Append-only event log (single log Phase 1) |
| 4 | `clients/` | Markdown CRM (companies/, contacts/, deals/) |
| 5 | `directions/` | **NEW** — portfolio model: `_active|_hypotheses|_archived/` |
| 6 | `wiki/` | Cross-cutting knowledge, `scope: jetix` (не shared с Life-OS) |
| 7 | `decisions/` | ADR + postmortem + letter + strategy + weekly + okr + policy + quarterly + promotions + fpf-stewardship + backlog + templates |
| 8 | `evals/<role>/` | Golden datasets + manual evaluation results |
| 9 | `docs/` | Diátaxis 2-form: how-to + reference |
| 10 | `finance/` | Invoices + ledger + compute-ledger + resource-ledger + currencies.yaml placeholder |
| 11 | `inbox/` | **NEW** — voice-notes pipeline output lands here |
| 12 | `outreach/` | **NEW** — `_shared/` templates cross-direction |
| 13 | `entities/jetix-gmbh/` | Federation stub (4h scaffolding, inactive Phase 1) |
| 14 | `governance/` | advisory-board/, trustee-designations.md, beirat/, aufsichtsrat/ |
| 15 | `ops/` | hit-by-bus, business-continuity, incident-playbook, gdpr-art-33, disaster-recovery |

Plus files: `CONSTITUTION.md`, `CLAUDE.md`, `README.md`.

В `~/jetix-os/life-os/` (parallel mount): `wiki/` (personal), `daily-log/
{YYYY}/`, `reflection/`, `health/`, `relationships/`, `personal-goals/`,
`decisions/` (personal ADRs), `okrs/`, `letters/`.

В `~/jetix-os/shared/` (top-level meta): `role-framework/`, `levenchuk-
ontology/`, `writing-templates/`.

**Deferred Phase 1 (Simplifier triggers preserved):** `comms/mailboxes/`,
`state/` (DuckDB), `sales/` отдельный, `templates/` отдельный,
`processes/`, `products/` (1st SaaS commit), `roles/` отдельный (30+
agents OR 1st human).

### 5.2 8 alphas (summary; detailed states в Section 3 P3)

Client / Project / Deal / Content Item / Hypothesis / Member / Way of
Working / **Direction**. Past-participle strict. Pre-commit Hook 4
enforces.

### 5.3 18 role-manifests (full depth Day 1-9)

- **5 Ruslan atomic sub-ролей:** strategy-lead / framing-lead /
  sales-closer / acceptance-authority / external-relations
  (+ `executors/ruslan.yaml` multi-role-binding)
- **11 agent роли:** manager / personal-assistant / system-admin /
  sales-lead / sales-research / sales-outreach / inbox-processor /
  crazy-agent / knowledge-synth / strategy-support-analyst (renamed от
  `strategist`, J3) / meta-agent (+ **FPF-Steward sub-role** per R12
  override)
- **2 Phase 2a stubs:** `dpo` (external-mode) / `customer-success` (J2)

**Total cost:** ~35-45h writing (Ruslan override "всё, сука, писать
сразу, глубоко, качественно"). `life-coach` — migrates в `life-os/
agents/life-coach/`, не part of Jetix career ladder (Item 7 / Area 7
decision).

### 5.4 7+7 day rollout (realistic 7+10-12 tolerance)

**Days 1-7 Sales Infrastructure:**

| Day | Output |
|-----|--------|
| 1 | jetix.de domain + git init + `directions/_active/ai-consulting-dach/` init |
| 2 | First SKU + 4 pre-commit hooks (asymmetric ref / Rechnungsnummer / role-manifest / past-participle) |
| 3 | Cold outreach list 50 Mittelstand (IHK directory + Perplexity research) |
| 4 | Discovery call template (DE+EN) + Cal.com booking |
| 5 | Proposal template + Audit SKU pricing |
| 6 | Contract + invoice template + Stripe account setup |
| 7 | Steuerberater intake + first hypothesis direction stub |

**Days 8-14+ Foundation (realistic 7+10-12 timeline):**

| Day | Output |
|-----|--------|
| 8 | SOPS + age (1 key) + Life-OS ≠ Jetix folder separation |
| 9 (9a+9b) | 18 role.md full-depth + 18 executor-bindings |
| 10 | First golden dataset sales-lead + 5-ый auto-translation hook |
| 11 | Diátaxis 2-form docs + D6 FPF first-pass (parallel track) |
| 12 | First RFD + Constitution §11 с TBD trustee placeholder |
| 13 | ops/ artifacts text (hit-by-bus + continuity + incident-playbook + disaster-recovery + gdpr-art-33) с TBD trustee |
| 14 | Backup restic → Backblaze B2 + Healthchecks.io |

**Parallel tracks:**
- D6 FPF full writing (30-50 pages, 3 passes) — parallel к Foundation
  Days 10-14+
- Migration script existing 568 wiki files (Life-OS vs Jetix
  classification) — post-Day 14
- First attention-theme setup — Day 14
- Per-agent compute contract activation — Day 9

### 5.5 Tool stack Phase 1

- git + GitHub (SoT)
- Claude Code (Opus 4.7 1M context)
- SOPS + age (1 key)
- restic → Backblaze B2 (backup)
- Healthchecks.io free tier (monitoring)
- Stripe (payment)
- Toggl (Deep Hours tracking per P7)
- Perplexity (research)

### 5.6 Cost model (€275-737/mo run rate Phase 1)

| Component | EUR/mo |
|-----------|--------|
| Claude Code API (~27K msgs/mo est.) | 150-500 |
| Hetzner VPS | 10-30 |
| Backblaze B2 | 5-15 |
| Domain (jetix.de + secondary) | 5-15 |
| Langfuse cloud (free tier) | 0 |
| Healthchecks.io | 0 |
| Stripe fees (~2.9% + 0.30) | variable (per transaction) |
| Toggl | 10-20 |
| Perplexity Pro | 20-40 |
| GitHub (free; upgrade Pro if needed) | 0-10 |
| SOPS + age | 0 |
| Miscellaneous (Cal.com, etc.) | 10-30 |
| **Total** | **~€275-737/mo** |

**12-month run rate:** €3,300-8,850
**Break-even:** 1st Audit SKU (€2000-5000) покрывает 6-18 мес
**Per-direction compute breakdown (Item 9 Variant B):** ai-consulting
~70-80%, hypotheses ~15-20%, meta ~10-15% — visibility через
`finance/compute-ledger.yaml`.

### 5.7 4 rituals cadence + strategizing as event

- **Daily morning (30 min):** inbox + pipeline + intent
- **Weekly Friday (60 min):** Shape Up + commits review + close-week
- **Monthly last Friday (2h):** P&L + OKR + founder note + meta-review
- **Quarterly (1 day):** letter + OKR-next + role-manifest delta + strategy

**Strategizing:** trigger-driven event (не ceremony). Triggers: market
shift, financial inflection, direction kill-criteria hit, external
change (regulatory / competitive). Не monthly schedule.

---

## Section 6 — Evolution diff: v1 → v2 → v2-Ruslan-approved

### 6.1 Compact table

| Aspect | v1 (baseline) | v2 (post-review) | v2-Ruslan-approved |
|--------|---------------|------------------|-------------------|
| Core principles | 7 | 7 (refined) | **8** (+Portfolio of Directions) |
| Folders Phase 1 | 22 | 11 | **15** (+directions/, inbox/, outreach/) |
| True alphas | 10 | 7 (+3 WP, 1 entity) | **8** (+Direction) |
| Role manifests Phase 1 | 12 | 12 | **18** (5 Ruslan sub + 11 agents + 2 stubs) |
| FPF document name | "FPF-Lite" | "FPF-Lite" | **"FPF" (full, drop "Lite")** |
| FPF size | 3-5 pages | 3-5 pages | **30-50 pages, max Левенчук** |
| FPF loading | reference-only | few additions | **Full text everywhere (OT5 Variant A)** |
| Mereological graph | simple dependencies | Lite Phase 1 + Full Phase 2 | **Full 3-level Phase 1 (MC3 override)** |
| Resources first-class | Capital + Hours implicit | Capital + Hours + Attention | **Capital + Compute + Deep Hours + Attention Budget + Ecosystem (11 cat)** |
| Life-OS ≠ Jetix | shared logical | Phase 2a extraction | **Day 1 physical separation, Phase 3 different servers** |
| Trustee | unspecified | Anton designated | **TBD ≠ Anton (open)** |
| FPF-Steward | none | none (meta-agent sufficient) | **Sub-role в meta-agent Phase 1 (R12 OVERRIDE Variant B)** |
| Market scope | DACH-only | DACH-locked Phase 1-2 | **DACH + US + RU, unified funnel Day 1** |
| Multi-currency | deferred | rejected (R10) | **External via Stripe/Wise + placeholder `finance/currencies.yaml`** |
| Bilingual frontmatter | Russian-only | EN summary policy/decisions/roles | **Hybrid (Scenario E): EN summary + auto-translation hook + per-language outreach folders** |
| Rollout | 14-day Foundation-first | 7+7 split | **Same + realistic 7+10-12 tolerance** |
| Pre-commit hooks | 2 | 3 (asymmetric ref + Rechnungsnummer + role-manifest) | **4 (+past-participle Hook 4) + 5-ый auto-translation** |
| EU AI Act | internal-only | placeholder policy | **Scenario C risk-proportional (4 tiers) + compliance calendar + DPA template** |
| Trademark Jetix | assumed ok | flagged | **Perplexity research + backlog entry при €20-50K revenue** |
| crazy-agent level | J2 ad-hoc | J2 | **J2 "brainstorming mode outside normal ladder" + special evaluation criteria** |
| life-coach placement | Jetix agent | Jetix agent | **Life-OS only (не part of Jetix ladder)** |
| AI promotion mechanism | 90-day self-graded | informal | **External review (meta-agent evidence) + Ruslan sign-off, `decisions/promotions/`** |

### 6.2 11 Ruslan overrides — narrative

Каждый override зафиксирован с rationale / quote / implications.

**Override #1 — Compute as 4th first-class resource.**
Ruslan Chunk 1 P7: "заносим в first principles". Причина: machine
cognition становится как Capital / Hours — finite, measurable, budget-
worthy. Implications: `finance/compute-ledger.yaml`, per-executor
compute contract, monthly review.

**Override #2 — Deep Hours refinement (Attention → Hours collapse).**
Ruslan Chunk 1 P7: "мне понравился вариант C; capital + compute + deep
hours; attention budget — квартальный уровень". Attention-as-daily-
ledger-metric — slippery (trackable only retrospectively). Hours refined
to Deep Hours (attention-weighted: session с Claude Code / strategic
thinking / deep learning / architectural work / client deliverable —
yes; email triage / routine admin / meetings без decision-making — no).
Toggl `[deep]/[shallow]` tags; target 25-30 deep hours/week.

**Override #3 — Ecosystem Resources detailed (11 categories).**
Phase 3 first-class ресурс: advisory / community / partnerships / brand
equity / DACH institutional (IHK, VDMA, BDI, BITKOM) / alumni / media /
talent / capital / academic / regulatory. Infrastructure Phase 1 prep:
`governance/advisory-board/members.yaml` (Anton/Vladislav/Rodion
formalized informally), `decisions/policy/ecosystem-strategy.md`
placeholder. Ruslan: "фаза 3 ecosystem это тоже очень важно, она будет
довольно мощной и массивной".

**Override #4 — Trustee identity TBD, not Anton.**
v2 synthesis MC4 резолвил Anton как designated trustee. Ruslan
explicit: "но это будет потом, это будет тоже не Антон". Implications:
`governance/trustee-designations.md` пишется с `{trustee: TBD}`
placeholder; Constitution §11 ссылается на TBD; execution artifacts
Day 13 (не Day 1 priority).

**Override #5 — DACH primary + US + RU secondary с Day 1 unified funnel.**
v2 — "DACH-locked". Ruslan modification: "основной упор на DACH, но при
этом ещё будет US и русскоязычное тоже; они все у нас будут проходить
через одну воронку, или через один вид оплаты". Implications: Stripe/
Wise external multi-currency; `finance/currencies.yaml` placeholder;
split outreach folders per language; partial R10 reversal (Rejection
preserved formally, но practical pathway created).

**Override #6 — Full 3-level mereological creation graph Phase 1.**
v2 — "Lite Phase 1 + Full Phase 2" (deferral). Ruslan MC3 override:
"Три уровня mereological важно, обязательно мы делаем все три уровня
максимально глубоко, как говорит Левенчук. Качественно, удобно, глубоко.
Никаких упрощений". Cost +4-8h Phase 1. Artifact: `wiki/foundations/
jetix-creation-graph.md`. Levels: L1 target systems (client-relationship,
deal-opportunity, product-SKU, content-item, member-engagement,
hypothesis, way-of-working); L2 creation systems (5 Ruslan sub-roles +
11 agent roles + methodologies + processes); L3 supersystems (Jetix-
Sales-Function, Jetix-Revenue-Engine, Jetix-Delivery-Function, Jetix-
Ecosystem Phase 3 hooks); mereological edges (part-of, creates,
operates-in, methodologically-uses, constrained-by).

**Override #7 — Physical Life-OS/Jetix separation Day 1.**
v2 — "shared logical Phase 1, Phase 2a extraction". Ruslan Item 6
directive: "Life-OS и Jetix должны быть принципиально вообще разделены,
никак не коим образом не смешиваться. Ничего с Life-OS не должно
попадать в Jetix. Потом физически разделим на разных серверах".
Implementation: parallel mount `~/jetix-os/{life-os,jetix}/`;
asymmetric reference rule (Hook 1 blocks Jetix → Life-OS);
Phase 2a `git filter-repo` extraction; Phase 3 different servers.

**Override #8 — Portfolio of Directions (8-ая alpha + 8-ой principle).**
Ruslan Item 6 directive: "Jetix = большая корпорация, десятки
направлений. Шаурмечные, кибербезопасность, AI-tools. Википедия должна
работать с людьми, с CRM, cross-functional. Jetix как холдинг для
кросс-функционального наблюдения". Model: Hybrid Variant 1+4 —
folder-per-direction + Direction как 8-ая alpha. Implications: 7
alphas → 8; principles 7 → 8; new `directions/` top-level folder
structure; 3 portfolio-specific graph edges (belongs-to-direction /
applies-to-direction / sames-as-crm); frontmatter `direction:` /
`directions:` convention.

**Override #9 — Full FPF (renamed from FPF-Lite), 30-50 pages.**
v2 — "FPF-Lite 3-5 pages". Ruslan Area 6 directive: "Мы к этому
документу подходим глубоко. Он не должен быть light — он должен быть
constitutional, адекватный, глубокий. Максимально глубоко всё что можно,
прописываем по Левенчуку. Вообще никакого компромисса". Document
renamed: `D6 JETIX-FPF-LITE.md` → `D6 JETIX-FPF.md`. Content expanded:
full 17 trans-disciplines reference, advanced mereology (Kit Fine
acknowledgment, holon hierarchy), category theory (objects/morphisms/
functors где useful), constructor theory (Creation Graph depth).
Writing: 3-pass (first pass all 10+ sections; second deepen; third
FPF-Steward audit). Cost 25-40h.

**Override #10 — Full FPF text everywhere (не reference-only).**
OT5 Sub-question 1 — Вариант A: full 7-10K tokens в каждый agent
`system.md`. Ruslan: "Мы оставляем эти FPF контексты полностью на всех.
Мы можем себе это позволить. Главное чтобы это глубоко и качественно
использовалось и работало". Monthly cost ~$5-10. Context pressure
minimal (10K = 1% Opus 4.7 1M; 5% Sonnet/Haiku 200K). Consistent с
Левенчук exocortex 25K hard reservation. Publishing — internal only
Phase 1+ (secret sauce, review trigger €1M+ ARR).

**Override #11 — FPF-Steward sub-role Phase 1.**
v2 R12 — "REJECT, meta-agent sufficient". Ruslan override Variant B:
"Здесь мне нужен Левенчук на максимум. Всё что его техника предлагает,
мы используем на 100% на максимум. Берем вариант B и внедряем глубоко".
Sub-role section в `agents/meta-agent/system.md`; scope: FPF consistency,
Alpha/WP/Entity classification, past-participle verification (автоматика
Hook 4 + manual cross-check), concept duplication detection, role-
manifest structural integrity, Direction-concept boundary clarity,
frontmatter schema; quarterly audit cycle (Q1/Q2/Q3/Q4 within 2 weeks
of close) + ad-hoc при major ontology changes; output `decisions/
fpf-stewardship/YYYY-QN-ontology-audit.md`. Trigger to separate role:
30+ agents OR 1+ human meta-hire OR quarterly audit burden >4h
(whichever fires first — Phase 2b likely).

---

## Section 7 — Outstanding Tensions Resolution

Все 5 OT tensions resolved в Chunks 1-4.

**OT1 Strategic-management decomposition — RESOLVED EARLY Chunk 1 P5.**
Resolution: 5 atomic sub-ролей (strategy-lead / framing-lead /
sales-closer / acceptance-authority / external-relations) + `executors/
ruslan.yaml` multi-role-binding (hybrid founder-mode). Не "monolithic
founder vs Левенчук-correct 5 separate" — accept both via hybrid
architecture: 5 manifests written + executor binding unifies в одной
person Phase 1.

**OT2 Bilingual frontmatter — Scenario E (Hybrid).**
Namespace conventions:
- `policy/`, `decisions/` — bilingual (`lang: [ru, en]`), EN summary
  mandatory 150-300 words + RU body
- `roles/` — EN primary (`lang: en`); DE добавляется Phase 2a closer
  to 1st hire
- `ops/` — EN primary (trustee emergency accessibility)
- `wiki/concepts/`, `wiki/summaries/`, `directions/*/direction.md` — RU
  primary + auto-translation hook (5-ый pre-commit: `auto_en: true`
  triggers Opus 4.7 translation → saves `.en.md` sibling)
- `wiki/sources/`, `wiki/ideas/`, `alphas/` — RU default
- `finance/` — DE mandatory (HGB compliance)
- `clients/<id>.md` — internal notes RU; `client_language: de|en|ru`
  frontmatter для client-facing
- `outreach/` — separate folders per language (`de/`, `en/`, `ru/`):
  different copy, not translations

Cost: 8-13h setup (5-10h EN summaries 30-50 docs + 2-3h auto-translation
hook) + ongoing €1-5/mo API.

**OT3 EU AI Act tier — Scenario C (Risk-proportional) + calendar + DPA.**
4 categories с different human gates:

| Category | Risk | Gate | Examples |
|----------|------|------|----------|
| Internal-only | Minimal | None (J-Auto) | Research, wiki ingestion, summaries |
| External reversible | Low-medium | Batch approval (J-Approve batch) | Outreach drafts (batch 20/week), social scheduling |
| External non-reversible | High | Per-action approval (J-Approve per) | Send specific email, publish content |
| Strategic / regulatory | Critical | Ruslan explicit (J-Strategic) | Sign contract, offer discount, compliance claim |

Artifacts Phase 1: `decisions/policy/ai-agent-decision-authority.md`
(categories + examples), `decisions/policy/eu-ai-act.md` (calendar:
2025 GPAI monitor → 2026-Q2 AI inventory → 2026-Q3 tier classification
→ Aug 2026 High-risk obligations live), `decisions/templates/
client-dpa-template.md` (3-4h, IP lawyer consult). Art. 22 GDPR
compliance — automated via J-Approve/J-Strategic gates.

**OT4 Trademark Jetix vs Disney — DEFER (Perplexity research + backlog).**
Phase 1 immediate: Ruslan Perplexity research (~30 min, €0) — DPMA/EUIPO
status для "Jetix", Disney brand history post-2009. Phase 1 ongoing:
informal brand usage, no formal registration. Trigger: first meaningful
revenue €20-50K. Phase 2a action: IP lawyer consult + full trademark
search + defensive registration OR rename (~€2000-3500). Backlog entry
`decisions/backlog/trademark-jetix-formal-resolution.md`.

**OT5 FPF token-budget + publishing — Variant A (full text) + Internal-only.**
См. Overrides #10 и #9 выше. Full 7-10K tokens в каждый agent system.md;
internal Phase 1+; publishing review trigger €1M+ ARR
(`decisions/backlog/fpf-publishing-review.md`).

---

## Section 8 — Consequences

### 8.1 Что architecture enables

- **Mega-corp readiness без premature-materialization cost** — Reference
  architecture полный 7-layer, Operational Phase 1 lean 4-layer,
  triggered expansion painless.
- **Portfolio research engine** — cross-functional observation через
  wiki/concepts/ + edges.jsonl + direction-frontmatter convention;
  multiple bets одновременно, cross-direction learning.
- **Solo-to-team transition без re-architecture** — 5 Ruslan atomic
  sub-ролей + 18 role-manifests + Role ≠ Executor split дают clean
  delegation paths при 1st hire (Phase 2a).
- **DACH + US + RU с Day 1** — unified funnel, не Phase 3 expansion;
  Stripe/Wise external currency; split outreach per-language; legal
  compliance built-in (EU AI Act calendar, GDPR DPA template, HGB
  `finance/` DE frontmatter).
- **Investment-grade foundation** — audit trail via git, formal ADRs,
  role-manifests, Constitution, FPF (constitutional-depth). Due diligence
  ready без retroactive documentation marathon.
- **Левенчук-correct ontology** — full 8 true alphas, past-participle
  strict, 3-level mereology, 17 trans-disciplines reference, holons
  recursive. FPF-Steward quarterly audit предохраняет от onto-drift.

### 8.2 Что architecture costs

- **Phase 1 setup work ~80-120h total Stage 4 writing:**
  - Bilingual setup: 8-13h
  - FPF full (3 passes): 25-40h
  - 18 role-manifests full depth: 35-45h
  - Ops artifacts (Day 13): 6h
  - Mereological graph: +4-8h (встроено в FPF)
  - Misc (D1-D5, D7, D8): 10-20h
- **Ongoing ~5-10h/month FPF maintenance** + quarterly FPF-Steward audit
  (~2-4h/quarter Phase 1).
- **API spend €275-737/month run rate** Phase 1; €3,300-8,850 12-month;
  break-even 1st Audit SKU.
- **Cognitive overhead Phase 1** — 15 folders, 18 manifests, 8 alphas,
  4 rituals держать в голове. Mitigation: agents помогают (meta-agent
  onboarding, FPF-Steward audits, inbox-processor triage).

### 8.3 Что architecture forbids (explicit negative space)

- **Notion как parallel SoT** — decommission Day 14.
- **Dynamic role assignment** — кроме `executors/ruslan.yaml` founder
  exception.
- **Jetix files referencing Life-OS paths** — Hook 1 blocks.
- **Gerund states** (`qualifying` vs `qualified`) — Hook 4 blocks.
- **Agent strategic decisions** — agents не стратегируют (Левенчук §1.4);
  `strategy-support-analyst` — support only, J3 level.
- **Internal multi-currency bookkeeping Phase 1** — Stripe/Wise external.
- **FPF publishing external** — internal-only Phase 1+, secret sauce.
- **Life-coach в Jetix ladder** — миграция в Life-OS.

---

## Section 9 — Rollback Plan

### 9.1 Per-decision reversibility

Большинство решений — additive и reversible:

| Decision | Reversibility | Path |
|----------|---------------|------|
| 15 folders | Additive | Drop folder + migrate contents via `git mv` |
| 18 role-manifests | Additive | Delete role.md + archive binding.yaml |
| 8 alphas (Direction added) | Reversible | Drop `alphas/direction/` + collapse back to 7 (если Portfolio model fails) |
| Pre-commit hooks (5) | Reversible | Disable hook в `.git/hooks/` |
| FPF full text in system.md | Reversible | Swap back to reference-only loading (OT5 Scenario B) |
| Compute as first-class | Reversible | Collapse compute-ledger.yaml → informal tracking |
| Portfolio Directions | Semi-reversible | `directions/` можно deprecate; wiki frontmatter requires cleanup |

### 9.2 Hard-to-reverse decisions

- **Physical Life-OS ≠ Jetix separation Day 1** — requires `git filter-
  repo` reverse-merge (complex; 4-8h work). Mitigation: principle строгий,
  reversal probability low.
- **Past-participle rename** — applied везде; reversing semantic
  inconsistency создаст технически. Mitigation: convention ШСМ-grounded,
  reversal unlikely.
- **FPF-Steward sub-role** — can deactivate by removing section; re-
  activation cheap. Low lock-in.

### 9.3 Rebuild paths

- **Full FPF burden excessive:** collapse к FPF-Lite v2 (3-5 pages); hold
  full version в `wiki/foundations/fpf-full.md` как reference; loading
  switches to Lite.
- **18 manifests burden excessive:** compress к v2 (core 7 + skeleton 5)
  rolling strategy; reconcile later.
- **Federation stub scaling cost:** если `entities/jetix-gmbh/` Day 1 скам
  становится burden — collapse к `entities/README.md` placeholder;
  scaffold восстанавливается при 2nd entity emergence.

---

## Section 10 — Review Triggers

Когда эта архитектура пересматривается:

1. **Every 6 months** — formal architecture review (quarterly ritual
   extension); compare actual vs designed; update ADR с deltas.
2. **Phase transitions:**
   - **Phase 2a trigger** (Triple-AND: €20K MRR × 3mo + Ruslan >40%
     L1/L2 + ≥1 client requesting GDPR DPA) — Life-OS extraction, 2nd
     entity decision, Customer Success activation, Beirat formal.
   - **Phase 2b trigger** — Chief of Staff hire, FPF-Steward separate
     role (30+ agents OR 1+ human meta-hire OR quarterly audit >4h),
     L3 CRM full materialization (5+ concurrent clients).
   - **Phase 2c trigger** — 2nd entity emergence → federation pattern
     activated; Holdings architecture L7 materialized.
   - **Phase 3 trigger** — different servers/clouds (Life-OS/Jetix
     physical); Ecosystem Resources first-class; Aufsichtsrat.
3. **Critical incident** — breaking architecture invariant (Hook
   failure, ontology drift detected, unexpected compute cost spike >3×).
4. **Major Левенчук framework update** — new ШСМ primitives или
   changed mereology semantics → FPF-Steward quarterly audit initiates
   revision.
5. **30+ agents milestone** — FPF-Steward separate role; `roles/`
   отдельный top-level; `comms/mailboxes/` materialized.
6. **Regulatory inflection** — EU AI Act High-risk obligations go live
   (Aug 2026); BaFin inquiry; Bundeskartellamt contact; new Member
   State implementation law.
7. **Direction kill-criteria hit** — `_active` direction fails kill
   criteria → post-mortem + archive, attention-theme re-balance.
8. **Trademark Jetix formal resolution** — при revenue €20-50K range.

---

## Section 11 — References

### 11.1 Decision artifacts

- **Approval ADR (Stage 3 journal):** `decisions/2026-04-19-architecture-
  v2-approval.md` (APPROVED 2026-04-20) — полная history 7 chunks.
- **Progress checklist:** `decisions/review-v2-progress-checklist.md`.
- **This document (D9 draft v0.5):** `decisions/2026-04-20-jetix-
  architecture-final-DRAFT.md` — single source of truth для Stage 4.

### 11.2 Source materials

- **v2 synthesis:** `raw/research/architecture-synthesis-v2-final.md`
  (1621 строка) — baseline пересмотренный.
- **v1 synthesis:** `raw/research/architecture-implementation-synthesis-
  2026-04-19.md` (1592 строки) — historical reference.
- **4 reviewer reports:** `raw/research/stage2-review/*` (critic /
  simplifier / megacorp / levenchuk).
- **9 deep-research waves:** `raw/research/*-deep-research-*.md` +
  `hybrid-framework-synthesis-2026-04-18.md`.
- **Левенчук source material:** `raw/research/levenchuk-for-ai-deep-
  research-2026-04-19.md` + `levenchuk-deep-research-2026-04-18.md`.

### 11.3 Future artifacts (Stage 4 writing targets)

- **D1 JETIX-ARCHITECTURE-FINAL** — 15-20 pages; 8 sections (Context /
  Reference Architecture / Operational Phase 1 MVA / Decision /
  Consequences / Alternatives / Migration / Review triggers).
- **D2 JETIX-FOLDER-STRUCTURE** — 15 Phase 1 folders detailed +
  Life-OS/shared layouts + deferred triggers.
- **D3 JETIX-ROLE-MANIFESTS** — 18 full-depth 5-block role.md +
  executor-bindings (~35-45h).
- **D4 JETIX-VS-LIFE-OS** — separation principle, Triple-AND Phase 2a
  trigger, Phase 3 physical, SOPS 1 key, grey zone sanitization.
- **D5 JETIX-KNOWLEDGE-ARCHITECTURE** — 3-layer model, 8 alpha state
  machines, 25K exocortex hard reservation, manual writeback, latency-
  based GraphRAG trigger, ZUGFeRD Q3 2026.
- **D6 JETIX-FPF** (renamed от `-LITE`) — full 30-50 pages, 13+ sections,
  17 trans-disciplines, advanced mereology, holons, category theory,
  constructor theory; 3-pass writing; + separate `wiki/foundations/
  jetix-creation-graph.md`, `shsm-primitives.md`, `holon-hierarchy.md`.
- **D7 JETIX-CAREER-LEVELS** — dual system J0-JX reference + Phase 1
  J-Auto/J-Approve/J-Strategic; AI promotion external-review + Ruslan
  sign-off; crazy-agent J-Approve special; life-coach migrated out;
  FPF-Steward separation trigger.
- **D8 docs/INSTRUCTIONS** — 7+7 rollout detailed + 4 rituals + tool
  stack + cost model + triggers; plan-as-tracker primary.

### 11.4 Supplementary artifacts

- `CONSTITUTION.md` (§11 Service Continuity — Day 12 draft с TBD
  trustee placeholder).
- `ops/` stack (Day 13): hit-by-bus, business-continuity, incident-
  playbook, disaster-recovery, gdpr-art-33.
- `decisions/policy/`: ai-agent-decision-authority.md, eu-ai-act.md,
  ecosystem-strategy.md (placeholder), compensation.md, sku-catalog.md.
- `decisions/templates/`: client-dpa-template.md, invoice.yaml,
  contract.md, proposal.md.
- `decisions/backlog/`: trademark-jetix-formal-resolution.md,
  fpf-publishing-review.md.
- `governance/`: advisory-board/members.yaml (Anton/Vladislav/Rodion),
  trustee-designations.md (TBD), beirat/ (Phase 2a), aufsichtsrat/
  (Phase 3).

---

## Open items for Ruslan review

Документ — draft. Три класса items которые могут потребовать clarify'я
в Stage 4.5 после D1-D8 written:

1. **Trustee identity** — Day 13 placeholder TBD. Нужно ли Phase 1
   proxy (Steuerberater? lawyer?) пока identity ищется, или пустой TBD
   достаточен до first client contract?
2. **Per-direction compute allocation benchmarks** — item 9 cost model
   breakdown ai-consulting ~70-80% / hypotheses 15-20% / meta 10-15% —
   revisit после first month actual data (Day 30+).
3. **Auto-translation hook (5-ый)** — Day 10 timing (parallel к golden
   dataset). Если Opus 4.7 translation quality для RU→EN wiki concepts
   не достаточно — fallback к manual EN summary для critical концептов;
   trigger decision на Day 10 после QA passage.

---

**END OF D9 DRAFT v0.5**

Stage 4 unblocked. D1-D8 writing proceeds using этот документ как
authoritative input. Stage 4.5 finalization: state `draft` → `committed`,
rename `-DRAFT.md` → `.md`.
