---
id: 2026-04-20-jetix-architecture-final
title: Jetix Architecture v1 — Final Decision Record (DRAFT v0.6)
version: v0.6
previous-version: v0.5
date: 2026-04-20
state: draft
review_stage: 3.6
regenerated-from:
  - v0.5 (commit 110413a)
  - Chunk 8 additions (Post-FPF-Discovery, same-day commit)
based_on:
  - decisions/2026-04-19-architecture-v2-approval.md (APPROVED 2026-04-20,
    includes Chunk 8 Post-FPF-Discovery Additions)
  - decisions/gap-analysis-review-decisions-2026-04-20.md (60+ decisions)
  - raw/research/architecture-synthesis-v2-final.md
  - raw/research/fpf-gap-analysis-2026-04-20.md (commit 74cf858)
  - raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md (commit 3cb5f81)
  - raw/external/ailev-FPF/FPF-Spec.md (commit 0a22129)
authors:
  decision_maker: ruslan
  scribe: claude-opus-4-7
purpose: >
  Clean consolidation Stage 3 + Stage 3.6 review decisions. Single
  source of truth для Stage 4 writers (D1-D8 чистовики). Finalized
  в Stage 4.5 после D1-D8 written.
size_target: 40-50 pages
lang: [ru, en]
english_summary: >
  Final Architecture Decision Record for Jetix v1 Phase 1 (v0.6 —
  Post-FPF-Discovery Consolidation). Reference vs Operational
  Architecture split; 8 core principles (Portfolio of Directions as
  P8); 15 folders; 18 role manifests full depth; 8 true alphas with
  past-participle state machines; full JETIX-FPF (renamed from
  FPF-Lite; 30-50 pages, max Левенчук depth); Nested Holonic Structure
  (FPF A.1 + A.14 canonical, renamed from Model D). Post-FPF-
  Discovery additions: Boundary Discipline (A.6.*), Trust & Assurance
  Tagging (B.3 F-G-R), Characteristic Spaces (A.17-21 SKU pricing /
  direction kill / agent promotion), Unified Term Sheet (F.17 UTS),
  Multi-View Publication Kit (E.17 Viewpoint Bundle mandatory), Bias-
  Audit Cycle (D.5), Phase Transitions MHT (B.2, 4 transitions), Agency
  CHR (A.13:4.3 fallback). 7+10-14 day rollout realistic; ~€300-800/mo
  run rate Phase 1. 11 original Ruslan overrides preserved; 25+ new
  FPF-grounded adoptions (Chunk 8). 140-220h total Phase 1 writing
  estimate. Hard internal-only stance (no contribute-back к ailev/FPF
  community); semi-annual FPF sync reminder (Ruslan manual trigger).
unblocks:
  - Stage 4: D1-D8 writing (D6 JETIX-FPF first — unblocked с enriched SoT)
  - Stage 4.5: D9 finalization
---

# Jetix Architecture v1 — Final Decision Record (DRAFT v0.6)

## Section 1 — Context

### 1.1 Что такое Jetix

Jetix — AI-native mega-corporation, оперируемая solo founder'ом (Ruslan,
Berlin) при кооперации с array Claude-агентов. Primary market — DACH
Mittelstand; secondary — US и русскоязычные клиенты через unified funnel.
Правовая траектория: Freiberufler (Phase 1) → UG (Phase 2a) → GmbH
(Phase 2b+) → потенциально Holdings (Phase 2c+).

Архитектурная парадигма: **Company-as-Code** (git = единственный source
of truth) + **Portfolio-of-Directions** (холдинг для cross-functional
наблюдения за множественными business-ставками) + **JETIX-FPF
дисциплина Левенчука** на максимум (ontology не-компромиссна; FPF
patterns A.1 / A.6 / A.14 / A.17-21 / B.2-4 / C.18-22 / D.5 / E.10 /
E.17 / F.6 / F.11 / F.17 / G.5 adopted full depth per Chunk 8).

### 1.2 Stage 3 + 3.6 review — зачем и как

**Stage 3 (2026-04-19 — morning 2026-04-20)** представлял multi-
perspective audit v1 synthesis. 5-chat methodology: 4 reviewer-persons
(Critic / Simplifier / Mega-Corp / Левенчук) → synthesizer consolidated
v2 (1621 строка) с 38 accepted / 12 rejected / 6 meta-conflicts /
5 outstanding tensions. Ruslan approval — 7 chunks (`2026-04-19-
architecture-v2-approval.md` Chunks 1-7), **11 overrides** все в
+Левенчук direction.

**Stage 3.5 (2026-04-20 midday)** — первый D9 draft (v0.5, 980 строк,
30 pages).

**Stage 3.6 (2026-04-20 afternoon)** — Ruslan прислал ссылку
`github.com/ailev/FPF`. FPF-Spec (62K строк) vendor в `raw/external/
ailev-FPF/`. 5 Perplexity researches (R-A through R-E) + KB compilation
+ Gap Analysis (65/100 alignment, 5 critical gaps, 22 recs, 11 OQs,
9 innovations). Tracking file `gap-analysis-review-decisions-2026-04-20.
md` — 60+ Ruslan decisions locked тот же день. Consolidated в **ADR
Chunk 8** (Post-FPF-Discovery Additions, appended to approval ADR).

**v0.6 регенерация D9** — этот документ — incremental update v0.5
плюс Chunk 8 material. v0.5 structure preserved; content expanded.

### 1.3 Inputs упорядочены по waves

- **9 deep-research waves** (`raw/research/*-deep-research-*.md` + два
  hybrid-framework synthesis документа) — foundation
- **v1 synthesis** (`architecture-implementation-synthesis-2026-04-19.md`)
  — первый attempt
- **4 reviewer reports** (`raw/research/stage2-review/*`) — multi-angle
  critique
- **v2 synthesis** (`architecture-synthesis-v2-final.md`) — consolidated
  proposal
- **Stage 3 Approval ADR** (`2026-04-19-architecture-v2-approval.md`
  Chunks 1-7) — Ruslan decisions
- **Stage 3.6 FPF-Spec** (`raw/external/ailev-FPF/FPF-Spec.md`) —
  первоисточник Левенчука (62K строк)
- **Stage 3.6 KB + Gap Analysis** (`raw/research/levenchuk-fpf-
  knowledge-base-2026-04-20.md` + `fpf-gap-analysis-2026-04-20.md`)
- **Stage 3.6 tracking** (`gap-analysis-review-decisions-2026-04-20.md`)
- **Stage 3.6 ADR Chunk 8** — consolidated Post-FPF-Discovery

### 1.4 Outcome summary

Stage 3 + 3.6 закрылись с **four архитектурными commitments**:

1. **Reference vs Operational split** — полный 7-layer L0-L7 design-
   time; Phase 1 материализует 4 layers (L0 Executive Core + L1
   Foundation + L2 Cognitive discipline + L4 Revenue).
2. **8 core principles** (Portfolio-of-Directions added as P8).
3. **Phase 1 operational minimum viable architecture** — 15 folders,
   8 alphas, 18 role manifests, JETIX-FPF full (30-50 pages, не Lite),
   7+10-14 day rollout realistic, ~€300-800/mo run rate.
4. **JETIX-FPF adoption full depth** (Stage 3.6) — 5 critical gaps
   closed (A.6.* boundary, B.3 F-G-R, A.17-21 CHR, F.17 UTS, E.17
   multi-view), 22 recommendations adopted, 11 open questions
   resolved, 9 Jetix innovations preserved internal-only.

---

## Section 2 — Decision Summary

### 2.1 TL;DR

Jetix Phase 1 строится как Company-as-Code система с git как единственным
SoT, 15-folder structure в parallel-mounted `~/jetix-os/{life-os,jetix}/`
с asymmetric reference rule (Jetix never references Life-OS), 18
role-manifests written в full depth Day 1-9, **JETIX-FPF** (renamed from
FPF-Lite; Левенчук ontology на максимум, 30-50 pages Core + 10-20 pages
Tooling companion) загружен текстом в system prompt каждого из 11
агентов, 8 true alphas с past-participle state machines, **Portfolio-
of-Directions** как 8-ой first-class principle и 8-ая true alpha,
resource accounting в двух tier'ах (Capital + Compute + Deep Hours
ledger + Attention Budget quarterly; Phase 3 first-class Ecosystem
Resources 11 категорий), 7+10-14 day rollout realistic (sales Days 1-7,
foundation Days 8-14+, parallel tracks heavier post-Chunk 8), **~€300-
800/mo run rate Phase 1** (slight increase from v0.5 €275-737 due
primarily к compute tracking fidelity improvements), tool stack из 5
(+ Claude Code, git, Stripe, Toggl, Perplexity).

**Post-FPF-Discovery additions (Chunk 8, +60-98h):** Boundary Discipline
(A.6.*, L/A/D/E routing all contracts), Trust & Assurance Tagging (B.3
F-G-R на ADRs + client deliverables + agent outputs), Characteristic
Spaces (A.17-21; SKU pricing + direction kill + agent promotion CHR
spaces formal), Unified Term Sheet (F.17 UTS, 30-50 rows concurrent с
D6 writing, LEX-BUNDLE 4-register naming), Multi-View Publication Kit
(E.17 Viewpoint Bundle — 5 viewpoints — mandatory для ALL Audit SKU
deliveries from first delivery), Bias-Audit Cycle (D.5, 4-stage BA-0/
BA-1/BA-2/BA-3, BA-2 deferred Phase 2a), Phase Transitions MHT (B.2,
4 MHTs documented Phase 1→2a/2a→2b/2b→2c/2c→3), Agency CHR fallback
(A.13:4.3). Terminology: "Model D" → **"Nested Holonic Structure"**
(FPF A.1 + A.14 canonical, OQ-06 B Anglicize). **Hard internal-only
stance** — no contribute-back к ailev/FPF community (OQ-09 A); semi-
annual FPF sync reminder (OQ-10 C modified, Ruslan manual trigger).

### 2.2 Key architectural commitments

- Git = SoT. Commit = акт управленческого решения.
- Role ≠ Executor (strict split, 5-block `role.md` + separate
  `executor-binding.yaml`).
- 8 true alphas в `alphas/` с past-participle state machines (strict-
  enforce).
- **Nested Holonic Structure** (FPF A.1 + A.14 canonical) + full
  3-level mereological creation graph Phase 1 с **A.14 typed edges**
  (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf /
  AspectOf + 4 Jetix-introduced).
- L0 Executive Core декомпозирован в 5 atomic Ruslan sub-ролей +
  `executors/ruslan.yaml` multi-role-binding.
- DACH primary + US + RU secondary, unified funnel через Stripe.
- Resource accounting quantitative: Capital + Compute + Deep Hours;
  quarterly: Attention Budget; Phase 3 first-class: Ecosystem (11
  категорий).
- Portfolio-of-Directions model: `directions/_active|_hypotheses|
  _archived/` с Direction как 8-ой alpha; **C.18 NQD-CAL + C.19 E/E-
  LOG per-direction** (Rec-07).
- Physical Life-OS ≠ Jetix separation Day 1 (parallel folders, hook
  enforcement).
- JETIX-FPF full (не Lite), 30-50 pages Core + 10-20 pages Tooling
  companion, max Левенчук, full-text loading в каждый agent system.md,
  **internal-only hard stance** (OQ-09).
- **Boundary Discipline (A.6.*)** L/A/D/E routing applied во всех 3
  contract-class templates (contract / DPA / proposal).
- **Trust & Assurance Tagging (B.3 F-G-R)** обязательно в ADR + client
  deliverable + agent output frontmatter.
- **Characteristic Spaces (A.17-21)** formal для SKU pricing, direction
  kill, agent promotion (A.18 CSLC mandatory, OQ-11).
- **Unified Term Sheet (F.17)** 30-50 rows в `wiki/foundations/jetix-
  uts.md`; concurrent с D6 writing (OQ-08 B); LEX-BUNDLE 4-register.
- **Multi-View Publication (E.17)** mandatory все Audit SKU deliveries
  первой from first (OQ-04 modified); 5 Viewpoints (Executive /
  Technical / Governance / Regulatory / Internal-learning).
- **Bias-Audit Cycle (D.5)** 4-stage (BA-0/1/2/3; BA-2 Panel deferred
  к Phase 2a Beirat Ethics advisor).
- **Phase Transitions MHT (B.2)** 4 transitions documented.
- **Canonical Evolution Loop (B.4)** mapped к 4 rituals (Observe /
  Reflect / Decide / Act).
- **FPF-Steward sub-role** в meta-agent (quarterly audit scope expanded
  per Chunk 8: UTS review + F-G-R compliance + edge-type verification +
  CHR space integrity + Viewpoint Bundle correspondence check).

### 2.3 Deferred / triggered

- **Phase 2a triggers (Triple-AND):** €20K MRR × 3mo + Ruslan >40%
  L1/L2 time + ≥1 client requesting GDPR DPA → `git filter-repo`
  extraction Life-OS в отдельный repo; BA-2 Panel Review activation
  (Beirat Ethics advisor); formal Customer Success J2 activation;
  Anglicize 2nd language targeting (roles/ DE added).
- **Phase 2b triggers:** Chief of Staff role, FPF-Steward как отдельная
  роль (30+ agents OR 1+ human meta-hire OR quarterly audit >4h); L3
  CRM full materialization (5+ concurrent clients); MHT-2 transition.
- **Phase 2c triggers:** 2nd entity → activate federation pattern
  (`entities/jetix-gmbh/` stub становится реальным); MHT-3 transition;
  first acquisition process.
- **Phase 3 triggers:** different servers/clouds; Ecosystem Resources
  first-class; Beirat/Aufsichtsrat formalization; MHT-4 transition.
- **Semi-annual FPF sync:** every 6 months (Q2 close + Q4 close) —
  FPF-Steward audit flags "upstream FPF sync review due" reminder;
  Ruslan manual decision whether to sync (OQ-10 C modified).
- **Открыто:** designated trustee identity (not Anton, TBD); trademark
  Jetix vs Disney (Perplexity research + backlog entry, formal
  resolution при €20-50K revenue range); first CHR space refinement
  (SKU pricing may need iteration post-1st client negotiation); UTS
  row-count refinement (30-50 target; may refine to 25 or 60 based
  on writing experience).

---

## Section 3 — Architecture Pillars (8 Core Principles)

Каждый principle — foundation ref architecture, applied в Phase 1
operational с explicit implications для D1-D8. Post-Chunk 8 refinements
marked inline.

### P1 — Company-as-Code, буквально. Git = SoT

**Statement:** Всё управленческое и организационное состояние
материализуется в git-репозитории. Commit = акт управленческого
решения. Notion decommission — завершён к Day 14 rollout'а.

**Rationale:** Mega-corp scalability начинается с reviewable org-state.
PR как управленческий ритуал даёт audit trail, rollback и distributed
collaboration free. Notion как secondary store создаёт divergence между
external/internal truth — устраняется.

**Phase 1 implication:** все 15 folders под `~/jetix-os/jetix/` живут
в git. Pre-commit hooks (4) enforce invariants: asymmetric reference
(Jetix→Life-OS blocked), Rechnungsnummer monotonicity, role-manifest
required fields, past-participle state check. Auto-translation hook
(5-ый) — OT2 addition.

**Cross-refs:** D1 Section "Reference Architecture"; D2; D8 hooks.

### P2 — Role ≠ Executor (+ Agency-CHR dimension)

**Statement:** Роль (обязанности, метод, outputs) — archetype. Executor
(agent instance или human) — привязка. Никогда не смешиваются.
**Post-Chunk 8:** роль + executor-binding получают **Agency-CHR
fallback** (A.13:4.3) — formal agency-scale 0.0-1.0 dimension к 3-tier
J-Auto/Approve/Strategic (Rec-08).

**Rationale:** Portability — Phase 1 honesty: roadmap goal v2.0+, не
Phase 1 claim. Но architectural seams разделения соблюдаются строго,
чтобы v2.0+ portability была механической, а не re-architecture'ом.
Agency-CHR добавляет разрешение к granularity: same executor может
operate at varying agency depending on decision class.

**Phase 1 implication:** 18 role-manifests (5-block `role.md` —
identity / ontological / method / production_dependencies / evolution)
+ separate `executor-binding.yaml` с секциями:
- `compute-contract` (model_preference, fallback_models, thinking_mode,
  max_tokens_per_session, cache_strategy, latency_class,
  escalation_rules) — P7 override
- `agent_onboarding` + **F.6 6-step Role Assignment Cycle** (identify /
  request / propose / negotiate / enact / retrospect) — Левенчук Part
  3 + Rec-15
- **`agency-profile`** (A.13:4.3) — formal agency-scale per decision
  class (Rec-08)
- `reasoning_examples` optional (Левенчук Part 3)

Dynamic role assignment forbidden (кроме founder exception: `executors/
ruslan.yaml` с multi-role-binding flag для 5 atomic sub-ролей).

**Cross-refs:** D3 — 18 full-depth manifests; `decisions/policy/
mereology-edge-types.md` (Rec-05 для "part-of-role" typed).

### P3 — 8 True Alphas + past-participle convention strict + A.14 typed mereology

**Statement:** 8 true alphas (Client, Project, Deal, Content Item,
Hypothesis, Member, Way of Working, **Direction**) материализуются в
`alphas/` с past-participle state machines. Work products (Invoice,
Postmortem, Research Note) живут в domain-appropriate folders
(`finance/`, `decisions/postmortem/`, `wiki/sources/`). Entity (SKU) —
в `catalog/` / `decisions/policy/`.

**Post-Chunk 8:** 3-level creation graph использует **A.14 typed
mereology edges** — ComponentOf / ConstituentOf / PortionOf / PhaseOf /
MemberOf / AspectOf (Rec-05). Plus 4 Jetix-introduced edges
(creates / operates-in / methodologically-uses / constrained-by /
fills). Convention documented в `decisions/policy/mereology-edge-
types.md`.

**Rationale:** Alpha = evolving stakeholder-concern. Work product =
deliverable artifact. Смешение первичных и вторичных элементов ломает
дисциплину (Левенчук ШСМ §1.3). Past-participle (`qualified`,
`activated`, `delivered`) — не gerunds — обеспечивает точный
онтологический статус: завершённое состояние, не процесс. A.14 typed
edges повышают reasoning accuracy — queries по part-of могут
differentiate ComponentOf (функциональная часть) vs PortionOf
(quantitative part) vs PhaseOf (temporal phase).

**Phase 1 implication:** 8 state machines past-participle (Table в
Section 5.2); Pre-commit Hook 4 блокирует gerunds в `state.yaml`;
«What ШСМ is NOT» section — обязательная часть JETIX-FPF; A.14
retagging applied к `wiki/foundations/jetix-creation-graph.md`.

**Cross-refs:** D5 Section "8 alpha state machines"; D6 JETIX-FPF
Section 6 (8 true alphas) + Section 10 (Mereology A.14); `decisions/
policy/mereology-edge-types.md`.

### P4 — Nested Holonic Structure (A.1 + A.14) + lightweight mereology explicit

**Statement:** Life-OS — корневая holonic система, Jetix вложен как
supersystem-contained в директории `life-os/projects/jetix/`
(conceptual model). Phase 1 physical layout — parallel mount: `~/
jetix-os/life-os/` и `~/jetix-os/jetix/` с asymmetric reference rule.

**Post-Chunk 8 — Terminology (OQ-06 B Anglicize):**
"Model D Nested Hierarchy" retired as primary term. Replaced by
**"Nested Holonic Structure"** — FPF **A.1 Holonic Foundation** (L.1017
FPF-Spec) + **A.14 Advanced Mereology** (L.17478) canonical. D6
introduces concept using FPF canonical: *"Jetix uses Nested Holonic
Structure (A.1 + A.14 Left мереологический, retired term)"*. Russian
lineage "Model D" приемлимо только legacy footnote где historically
referenced в v1/v2.

**Rationale:** A.1 Holonic Foundation корректно описывает отношения
part-of + supersystem-contained explicitly. A.14 Advanced Mereology
раскрывает typed edges (Components / Portions / Aspects / Phases /
Members). Lightweight subset materialized Phase 1 (part-of + creates +
operates-in + methodologically-uses + constrained-by + fills) +
A.14 core 6 typed; advanced full set reference-only в D6 JETIX-FPF.

**Phase 1 implication:** Asymmetric reference enforcement (Hook 1);
Phase 2a extraction via `git filter-repo --path life-os/`; Phase 3
physical separation на разные servers/clouds. A.14 typed edges applied
к `wiki/foundations/jetix-creation-graph.md` (retrofit).

**Cross-refs:** D4 JETIX-VS-LIFE-OS; D6 JETIX-FPF Section 10 Mereology
(A.14 full); `decisions/policy/mereology-edge-types.md` (Rec-05).

### P5 — L0 Executive Core (декомпозиция + scaffolding)

**Statement:** Strategic management декомпозирован на 5 atomic sub-
ролей: **strategy-lead / framing-lead / sales-closer / acceptance-
authority / external-relations**. Ruslan в Phase 1 — единственный
executor с multi-role-binding флагом (hybrid founder-mode). Agent
`strategy-support-analyst` (renamed от `strategist`, J3) — support-
роль, не strategic decision-maker (agents не стратегируют per Левенчук
§1.4).

**Bus-factor scaffolding:** `ops/hit-by-bus.md`, `ops/business-
continuity.md`, `ops/incident-playbook.md`, `ops/disaster-recovery.md`,
`ops/gdpr-art-33.md` + Constitution §11 Service Continuity protocol
(7d/14d/30d escalations) + `governance/trustee-designations.md` с
**placeholder `{trustee: TBD, NOT Anton}`**. Execution Day 13 (не Day
1 priority), до first client contract signed.

**Rationale:** Единая strategic-management роль — Левенчук §1.4
violation (5 distinct competencies merged). 5 atomic sub-ролей дают
clean delegation paths при найме (Phase 2a+). Trustee-identity-open —
Ruslan explicit override: "но это будет потом, это будет тоже не Антон".

**Phase 1 implication:** 18 role-manifests включают 5 Ruslan sub-ролей
с `executors/ruslan.yaml` multi-binding.

**Cross-refs:** D3 manifests list; D8 Day 13 artifacts; Constitution §11.

### P6 — DACH primary + US + RU secondary, unified funnel

**Statement:** Primary market — DACH Mittelstand (confirmed). Secondary
с Day 1 — US clients и русскоязычные клиенты. Все проходят через
**одну** воронку и **один** payment flow (Stripe + Wise для currency
conversion externally). Legal entity — DACH-based (Freiberufler → UG
→ GmbH).

**Rationale:** Ruslan explicit override на v2 synthesis ("DACH-locked
Phase 1-2"). Unified funnel снимает internal multi-currency complexity
— Stripe/Wise обрабатывает conversion externally; internal ledger
остаётся EUR-reported. `finance/currencies.yaml` — placeholder (1h
setup), место держим под Phase 2a expansion.

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
- `finance/compute-ledger.yaml` (tokens/model, API spend EUR, cache-
  hit ratio, rate-limit incidents)
- `decisions/quarterly/YYYY-QN-attention-theme.md` (example: "60%
  Sales / 25% Delivery / 10% Architecture / 5% Learning")
- `governance/advisory-board/members.yaml` (Anton/Vladislav/Rodion
  formalized informally — Phase 3 first-class prep)
- Per-executor compute contract (см. P2 implications)
- Toggl `[deep]` vs `[shallow]` tags; target 25-30 deep hours/week
  founder-mode

**Cross-refs:** D2; D3 (compute contract); D8 (rituals).

### P8 — Portfolio of Directions (holding-style pattern + C.18/C.19)

**Statement:** Jetix оперирует как портфолио направлений (directions),
каждое — hypothesis → experimentation → activated / dropped cycle.
Jetix сам — research engine + operational infrastructure для multiple
bets, не single-business company.

**Post-Chunk 8 additions (Rec-07):** per-direction **C.18 NQD-CAL**
(Novel-Question Distinctions Calculus) + **C.19 E/E-LOG** (Explore-
Exploit Log). Files per direction:
- `directions/<slug>/nqd-distinctions.yaml` — novel questions + kill
  distinctions
- `directions/<slug>/ee-log.yaml` — exploration/exploitation balance
  log

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
  `experiments/`, `research/`, `pipeline.md`, `state.yaml`,
  `nqd-distinctions.yaml`, `ee-log.yaml`
- `directions/_hypotheses/*/` — hypothesis-stage direction folders
- `directions/_archived/*/` — dropped с post-mortem
- `directions/README.md` — portfolio dashboard
- `alphas/direction/` — 8-ая alpha с state machine instances (symlinks)
- Graph edges (3 portfolio-specific): `belongs-to-direction` /
  `applies-to-direction` / `sames-as-crm`
- Frontmatter convention: `direction: <slug>` OR `directions: [list]`
  на всех wiki/clients/alphas files
- **Direction kill-criteria CHR** (Gap 3): `directions/_templates/
  kill-chr-template.yaml` — formal CSLC измеряет готовность kill'у

**Cross-refs:** D1; D2; D5; D7 (direction authority: J-Auto open
hypothesis, J-Strategic activate / archive); `decisions/policy/sku-
pricing-chr.yaml` + `decisions/policy/agent-promotion-chr.yaml`.

---

## Section 4 — Reference vs Operational Architecture Split

Центральная архитектурная абстракция Stage 3 review (unchanged post-
Chunk 8 structurally; Chunk 8 specifics flow into Section 5).

### 4.1 Reference Architecture (L0-L7, design-time)

Полный 7-layer stack — commitment на дизайн-уровне, materialization по
триггерам. Layers:

- **L0** Executive Core (strategic management, decision authority)
- **L1** Foundation (legal entity, compliance, ops, governance)
- **L2** Cognitive (JETIX-FPF ontology discipline, wiki, UTS)
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
- **L2** Cognitive as discipline (не папка) — **JETIX-FPF full text
  loaded** в каждый agent system.md (OT5 Scenario A, full 7-10K
  tokens); wiki/ с 9 entity types; alphas/ с 8 state machines;
  creation-graph full 3-level с A.14 typed edges; **UTS central**
  (`wiki/foundations/jetix-uts.md`); bias-audit (`decisions/policy/
  bias-audit-cycle.md`)
- **L4** Revenue — `directions/_active/ai-consulting-dach/` operational;
  SKU в catalog; invoice/contract templates с **Boundary Discipline
  L/A/D/E** applied; Stripe configured; **Multi-View Viewpoint Bundle**
  mandatory для Audit SKU deliveries

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
(dropping layers entirely) — оба отвергнуты в пользу Reference-vs-
Operational compromise.

---

## Section 5 — Phase 1 Operational Specifics

### 5.1 15 folders Phase 1 (+ directions/ enhancement per Rec-07)

В `~/jetix-os/jetix/`:

| # | Folder | Purpose |
|---|--------|---------|
| 1 | `agents/<id>/` | Combined role + executor + system + scratchpad (11 agents) |
| 2 | `alphas/` | 8 subfolders с past-participle state machines |
| 3 | `alpha-log/` | Append-only event log (single log Phase 1) |
| 4 | `clients/` | Markdown CRM (companies/, contacts/, deals/) |
| 5 | `directions/` | **Portfolio model**: `_active|_hypotheses|_archived/` + per-direction `ee-log.yaml` + `nqd-distinctions.yaml` + `kill-chr.yaml` + `outreach/{de,en,ru}/` |
| 6 | `wiki/` | Cross-cutting knowledge, `scope: jetix` (не shared с Life-OS) + `foundations/jetix-uts.md` (Gap 4) + `foundations/fpf-tooling.md` (Rec-13) + `foundations/jetix-innovations.md` (Chunk 8 Section 6) |
| 7 | `decisions/` | ADR + postmortem + letter + strategy + weekly + okr + **policy/** (expanded per Chunk 8) + quarterly + promotions + fpf-stewardship + backlog + **templates/** (expanded per Chunk 8) + **bias-audit/YYYY-QN** |
| 8 | `evals/<role>/` | Golden datasets + manual evaluation results |
| 9 | `docs/` | Diátaxis 2-form: how-to + reference |
| 10 | `finance/` | Invoices + ledger + compute-ledger + resource-ledger + currencies.yaml placeholder |
| 11 | `inbox/` | Voice-notes pipeline output + **`cues/` (Rec-17 A.16 PreArticulationCuePack)** |
| 12 | `outreach/` | `_shared/` templates cross-direction |
| 13 | `entities/jetix-gmbh/` | Federation stub (4h scaffolding, inactive Phase 1) |
| 14 | `governance/` | advisory-board/, trustee-designations.md, beirat/, aufsichtsrat/ |
| 15 | `ops/` | hit-by-bus, business-continuity, incident-playbook, gdpr-art-33, disaster-recovery |

Plus files: `CONSTITUTION.md`, `CLAUDE.md`, `README.md`.

В `~/jetix-os/life-os/` (parallel mount): `wiki/` (personal), `daily-log/
{YYYY}/`, `reflection/`, `health/`, `relationships/`, `personal-goals/`,
`decisions/` (personal ADRs), `okrs/`, `letters/`, `agents/life-coach/`
(migrated out of Jetix per Area 7).

В `~/jetix-os/shared/` (top-level meta): `role-framework/`, `levenchuk-
ontology/`, `writing-templates/`.

**Deferred Phase 1 (Simplifier triggers preserved):** `comms/mailboxes/`,
`state/` (DuckDB), `sales/` отдельный, `templates/` отдельный (пока в
`decisions/templates/`), `processes/`, `products/` (1st SaaS commit),
`roles/` отдельный (30+ agents OR 1st human).

### 5.2 8 alphas with A.14 typed edges reference

Client / Project / Deal / Content Item / Hypothesis / Member / Way of
Working / **Direction**. Past-participle strict. Pre-commit Hook 4
enforces.

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

**A.14 typed edges** applied в `wiki/foundations/jetix-creation-graph.
md` (Rec-05): ComponentOf / ConstituentOf / PortionOf / PhaseOf /
MemberOf / AspectOf + Jetix 4: creates / operates-in / methodologically-
uses / constrained-by / fills. Documentation: `decisions/policy/
mereology-edge-types.md`.

### 5.3 18 role-manifests (full depth Day 1-9) + Chunk 8 enhancements

- **5 Ruslan atomic sub-ролей:** strategy-lead / framing-lead /
  sales-closer / acceptance-authority / external-relations
  (+ `executors/ruslan.yaml` multi-role-binding)
- **11 agent роли:** manager / personal-assistant / system-admin /
  sales-lead / sales-research / sales-outreach / inbox-processor /
  crazy-agent / knowledge-synth / strategy-support-analyst (renamed от
  `strategist`, J3) / meta-agent (+ **FPF-Steward sub-role** per R12
  override, expanded scope per Chunk 8)
- **2 Phase 2a stubs:** `dpo` (external-mode) / `customer-success` (J2)

**`executor-binding.yaml` структура Post-Chunk 8:**

```yaml
# Already approved (Chunks 1-7):
compute-contract:
  model_preference: claude-opus-4-7
  fallback_models: [claude-sonnet-4-6]
  thinking_mode: auto
  max_tokens_per_session: 50000
  cache_strategy: high
  latency_class: batch-ok | real-time
  escalation_rules: [...]
agent_onboarding:  # Левенчук Part 3 #2
  initial_context_pack: [...]
  warm_up_tasks: [...]
  calibration_checkpoint: ...

# NEW (Chunk 8):
role_assignment_cycle:  # F.6 6-step (Rec-15)
  identify: ...
  request: ...
  propose: ...
  negotiate: ...
  enact: ...
  retrospect: ...
agency-profile:  # A.13:4.3 (Rec-08)
  default_agency: 0.4  # 0.0-1.0 scale
  by_decision_class:
    j-auto: 0.8
    j-approve: 0.4
    j-strategic: 0.0
  fallback_rule: |
    If uncertain classification, downgrade to lower agency.

reasoning_examples: [...]  # optional (Part 3)
```

**role.md Block 5:** seniority-lite (J-Auto/Approve/Strategic) +
direction_authority mapping preserved (Item 7).

**Total cost:** ~35-45h writing (Ruslan override "всё, сука, писать
сразу, глубоко, качественно"). `life-coach` — migrates в `life-os/
agents/life-coach/`, не part of Jetix career ladder (Item 7 / Area 7
decision).

### 5.4 Rollout timeline (7+10-14 days realistic, Post-Chunk 8 slight extension)

**Days 1-7 Sales Infrastructure (unchanged):**

| Day | Output |
|-----|--------|
| 1 | jetix.de domain + git init + `directions/_active/ai-consulting-dach/` init (+ `ee-log.yaml` + `nqd-distinctions.yaml` stubs per Rec-07) |
| 2 | First SKU + 4 pre-commit hooks (asymmetric ref / Rechnungsnummer / role-manifest / past-participle) |
| 3 | Cold outreach list 50 Mittelstand (IHK directory + Perplexity research) |
| 4 | Discovery call template (DE+EN) + Cal.com booking |
| 5 | Proposal template (с **Boundary Discipline L/A/D/E** Gap 1) + Audit SKU pricing (с **SKU pricing CHR** Gap 3) |
| 6 | Contract + DPA template (с **Boundary Discipline L/A/D/E** Gap 1) + invoice template + Stripe account setup |
| 7 | Steuerberater intake + first hypothesis direction stub (с `kill-chr.yaml` Gap 3) |

**Days 8-14+ Foundation (realistic 7+10-14 timeline, Post-Chunk 8):**

| Day | Output |
|-----|--------|
| 8 | SOPS + age (1 key) + Life-OS ≠ Jetix folder separation |
| 9 (9a+9b+9c) | 18 role.md full-depth + 18 executor-bindings с agency-profile + F.6 cycle |
| 10 | First golden dataset sales-lead + 5-ый auto-translation hook + **bias-audit BA-0/BA-1 template** (Rec-03) |
| 11 | Diátaxis 2-form docs + **D6 JETIX-FPF first-pass** (Core, parallel track 20-30 pages) |
| 12 | First RFD + Constitution §11 с TBD trustee placeholder + **`wiki/foundations/jetix-uts.md` first 10-15 rows** (concurrent с D6, OQ-08 B) |
| 13 | ops/ artifacts (hit-by-bus + continuity + incident-playbook + disaster-recovery + gdpr-art-33) + **`decisions/policy/` batch** (trust-tagging + boundary-discipline + sku-pricing-chr + agent-promotion-chr + characteristic-space-conventions + mereology-edge-types + phase-transitions-mht + bias-audit-cycle + mechanism-introduction) |
| 14 | Backup restic → Backblaze B2 + Healthchecks.io |
| 15-17 (Post-Chunk 8 extension) | **Viewpoint Bundle templates** (Gap 5, 5 views) + **audit-canonical-template** + F-G-R retrofit 10-15 existing ADRs + **MHT 4 transitions documented** (Rec-06) + **UTS expanded к 30-50 rows** |

**Parallel tracks:**
- D6 JETIX-FPF full writing (Core 20-30 pages + Tooling 10-20 pages,
  3 passes) — parallel к Foundation Days 10-17
- `wiki/foundations/jetix-uts.md` — concurrent с D6 (rows = U.Types =
  Section 8 ontology; OQ-08 B)
- Migration script existing 568 wiki files (Life-OS vs Jetix
  classification) — post-Day 17
- First attention-theme setup — Day 14
- Per-agent compute contract activation — Day 9
- First Q2 2026 FPF-Steward audit — Q2 close (Rec-22)

### 5.5 Tool stack Phase 1

- git + GitHub (SoT)
- Claude Code (Opus 4.7 1M context)
- SOPS + age (1 key)
- restic → Backblaze B2 (backup)
- Healthchecks.io free tier (monitoring)
- Stripe (payment)
- Toggl (Deep Hours tracking per P7)
- Perplexity (research)

### 5.6 Cost model (€300-800/mo run rate Phase 1, slight increase from v0.5)

| Component | EUR/mo |
|-----------|--------|
| Claude Code API (~27-32K msgs/mo est.; slight increase for compute tracking fidelity + UTS writing + F-G-R retrofit work) | 170-550 |
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
| Auto-translation API (OT2 hook) | 1-5 |
| Miscellaneous (Cal.com, etc.) | 10-30 |
| **Total** | **~€300-800/mo** |

**12-month run rate:** €3,600-9,600
**Break-even:** 1st Audit SKU (€2000-5000) покрывает 5-15 мес
**Per-direction compute breakdown (Item 9 Variant B):** ai-consulting
~70-80%, hypotheses ~15-20%, meta ~10-15% — visibility через
`finance/compute-ledger.yaml`.

**Slight increase from v0.5 €275-737:**
- Чуть больше Claude Code API usage — UTS writing + F-G-R retrofit
  + D6 JETIX-FPF full depth (Chunks 8 +60-98h) → +€20-50/mo initial
  setup months
- Auto-translation API €1-5/mo steady-state
- **Steady-state (post Phase 1 setup):** возвращается к €275-750/mo
  range

### 5.7 4 rituals cadence + B.4 Canonical Evolution Loop framing (Rec-14)

- **Daily morning (30 min):** inbox + pipeline + intent → **Observe**
  (B.4.1)
- **Weekly Friday (60 min):** Shape Up + commits review + close-week →
  **Reflect**
- **Monthly last Friday (2h):** P&L + OKR + founder note + meta-review
  → **Decide**
- **Quarterly (1 day):** letter + OKR-next + role-manifest delta +
  strategy → **Act**

**B.4 Canonical Evolution Loop** — Observe / Reflect / Decide / Act —
mapped к 4 rituals explicitly в D8 section (Rec-14). Ritual outputs
track each B.4 phase.

**F.11 Method Quartet Harmonisation** (Rec-18) — monthly check per
direction:
- method-design (how direction's method was originally conceived)
- method-work (actual applied method)
- method-plan (next-iteration plan)
- method-evidence (evidence of effectiveness)

Harmonisation audit раз в месяц.

**G.5 Multi-Method Dispatcher** (Rec-21) — MethodFamily Registry для
cross-direction method reuse; dispatcher правила в `decisions/policy/
multi-method-dispatcher.md`.

**Strategizing:** trigger-driven event (не ceremony). Triggers: market
shift, financial inflection, direction kill-criteria hit, external
change (regulatory / competitive). Не monthly schedule.

### 5.8 Boundary Discipline (A.6.*) — NEW Chunk 8

**FPF basis:** A.6.B Boundary Norm Square (L/A/D/E routing: Laws /
Admissibility / Deontics / Work-Effects). Plus cluster A.6.C Contract
Unpacking, A.6.0 U.Signature, A.6.P Relational Precision Restoration,
A.6.Q Quality Term Precision Restoration, A.6.H Wholeness Language
Unpacking.

**Scope:** 3 templates Phase 1 получают **full L/A/D/E structure**:
1. **Proposal template** (Day 5)
2. **Contract template** (Day 6)
3. **DPA template** (Day 6)

**L/A/D/E routing convention:**

- **L** Laws — applicable regulations (GDPR / EU AI Act / HGB / BGB),
  grounded in public legal texts
- **A** Admissibility — parties' acceptance criteria (formal
  admissibility gates)
- **D** Deontics — obligations, permissions, prohibitions between
  parties
- **E** Effects — work-effects (deliverables, metrics, SLA, outcomes)

**Policy doc:** `decisions/policy/boundary-discipline.md` — routing
convention, A.6 cluster usage guide, anti-patterns.

**Applied patterns cluster:**
- A.6.C — contract sections unpacked с explicit cross-references
  между L/A/D/E lanes
- A.6.0 U.Signature — formal kind-explicit headers per role-manifest
  + per template signature section
- A.6.P — relational precision в concept cross-references
  (`mentions → cites / derives / contradicts / refines`)
- A.6.Q — quality term precision в SKU / quality descriptions
  ("timely" → "within 72h business days per BGB §187")
- A.6.H — wholeness language в complex-concept explanation (direction
  wholeness, client-relationship wholeness)

**Cost:** 4-6h Phase 1 + ~5 min per new clause ongoing.

**Consistency:** Hook 3 (role-manifest required fields) extended к
check L/A/D/E sections presence в contract/DPA templates.

### 5.9 Trust & Assurance Tagging (F-G-R) — NEW Chunk 8

**FPF basis:** B.3 Trust & Assurance Calculus. Plus B.3.3 Assurance
Subtypes, B.3.4 Evidence Decay, B.3.5 Working-Model Relations (CT2R-
LOG), Pathwise Justification, Weakest-Link analysis, CL (Congruence
Level).

**Frontmatter schema addition (ADR + client deliverable + agent
output):**

```yaml
---
formality: F0-F9         # F0=informal, F9=formally-verified
reliability: R-low | R-medium | R-high | R-certified | R-formally-proven
claim-scope: bounded-context-path  # e.g., sales/dach-mittelstand/pricing/2026
ground-evidence:
  - type: expert-opinion | empirical | citation | derivation
    source: <source>
    strength: low | medium | high
  - ...
congruence-level: 1-5     # CL across bridges
---
```

**F-scale F0-F9 Jetix expected range:**
- F0 — informal notes, scratchpad
- F1 — structured notes (most decisions)
- F2 — ADR-grade (most ADRs)
- F3 — policy-grade (policy docs, client deliverables)
- F4-F9 — rarely used Phase 1 (F4 specification-grade, F5+ formal
  methods territory)

**R-levels:**
- R-low — anecdotal, single-source
- R-medium — multi-source, plausibility-checked
- R-high — peer-reviewed, empirically validated
- R-certified — third-party certified (auditor sign-off)
- R-formally-proven — formal verification (rarely applicable)

**Scope (per OQ-05 — broader than Claude rec):**
- All ADRs (Phase 1: retrofit 10-15 existing)
- All client deliverables (audits, proposals, reports)
- All agent outputs (sales-research briefings, meta-agent reports,
  knowledge-synth syntheses)

**Policy doc:** `decisions/policy/trust-tagging.md` — F/G/R
conventions, Jetix examples, retrofit-guide.

**Meta-agent enforcement:** prompt update — block publication without
F-G-R tagging.

**FPF-Steward quarterly audit scope** extended (per Chunk 8):
- F-G-R compliance check (ADRs + deliverables)
- Evidence-decay detection (B.3.4 — stale citations, outdated claims)
- CL re-measurement между Bridges (Rec-10)

**Cost:** 3-5h Phase 1 (policy + retrofit 10-15 existing ADRs +
template updates) + ~1 min per new ADR/deliverable ongoing.

### 5.10 Characteristic Spaces (A.17-21) — NEW Chunk 8

**FPF basis:** A.17 CHR-NORM (Canonical Characteristic), **A.18
Minimal CSLC Kernel** (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate),
A.19 CharacteristicSpace + mechanisms (UNM / UINDM / USCM / ULSAM /
CPM / SelectorMechanism), A.20 Flow Constraint Validity, A.21 GateFit.

**3 concrete CHR spaces Phase 1:**

#### 5.10.1 SKU pricing CHR

File: **`decisions/policy/sku-pricing-chr.yaml`** (3-5h).

```yaml
chr-kind: sku-pricing
scales:
  - name: hours-invested
    type: quantitative-continuous
    unit: hours
  - name: deliverable-complexity
    type: ordinal
    levels: [trivial, simple, moderate, complex, expert]
  - name: client-risk-tier
    type: ordinal
    levels: [retail, sme, mittelstand, enterprise, regulated]
  - name: dach-premium-factor
    type: multiplicative
    range: 1.0-1.8
gate-profile:  # A.21
  acceptance:
    - revenue >= 2000 EUR
    - margin >= 35%
  blocking:
    - risk-tier >= enterprise AND regulated-compliance-gap
selector-mechanism:  # A.19
  method: weighted-sum
  weights: {hours: 0.4, complexity: 0.3, risk: 0.2, dach: 0.1}
```

#### 5.10.2 Direction kill criteria CHR

File: **`directions/_templates/kill-chr-template.yaml`** + applied к
existing `directions/_active/ai-consulting-dach/kill-chr.yaml` (3-5h).

```yaml
chr-kind: direction-kill
scales:
  - name: 90-day-revenue-generated
    type: quantitative
    unit: EUR
    threshold-kill: < 5000
  - name: pipeline-health
    type: ordinal
    levels: [empty, thin, developing, healthy, robust]
    threshold-kill: empty | thin (after 60 days)
  - name: unit-economics-ltv-cac-ratio
    type: quantitative
    threshold-kill: < 1.5
  - name: strategic-fit
    type: ordinal
    levels: [off-core, tangential, aligned, core, critical]
    threshold-kill: off-core | tangential (after pivot attempt)
trigger-evaluation: quarterly (per ritual) or when threshold-breach
```

#### 5.10.3 Agent promotion CHR (A.18 CSLC mandatory per OQ-11)

File: **`decisions/policy/agent-promotion-chr.yaml`** (2-5h).

```yaml
chr-kind: agent-promotion
scales:
  - name: task-success-rate
    type: quantitative
    unit: percentage
    window: 90 days
  - name: evidence-quality
    type: ordinal
    levels: [weak, adequate, strong, exceptional]
  - name: autonomy-demonstrated
    type: ordinal
    levels: [j-auto-only, j-approve-partial, j-approve-full, j-strategic-ready]
  - name: critical-decisions-ratified
    type: quantitative
    unit: count
    window: 90 days
level-transitions:  # A.18 CSLC
  j-auto-to-j-approve:
    thresholds:
      task-success-rate: >= 90
      evidence-quality: >= strong
      autonomy-demonstrated: >= j-approve-partial
      critical-decisions-ratified: >= 5
  j-approve-to-j-strategic:
    thresholds:
      task-success-rate: >= 95
      evidence-quality: >= exceptional
      autonomy-demonstrated: j-strategic-ready
      critical-decisions-ratified: >= 20
  # Review: meta-agent compiles evidence → decisions/promotions/ → Ruslan sign-off
```

#### 5.10.4 Conventions doc

**`decisions/policy/characteristic-space-conventions.md`** — общие
правила для Jetix CSLC usage:
- When formal CHR vs informal heuristic (threshold: decision reversibility)
- Scale choice guide (quantitative vs ordinal vs multiplicative)
- Gate-profile authoring (A.21)
- Selector-mechanism choice (A.19 UNM/CPM/etc.)
- NQD-CAL (C.18) + E/E-LOG (C.19) применение per-direction
- MM-CHR (A.21 GateProfilization) + Pareto dominance в multi-criterion
  decisions

**Cost total Gap 3:** 8-15h Phase 1 + 30-60 min per new SKU/direction/
promotion ongoing.

### 5.11 Unified Term Sheet (UTS F.17 + E.10 LEX-BUNDLE) — NEW Chunk 8

**FPF basis:** F.17 Unified Term Sheet (Layout A Kernel-first, 30-50
core rows × 6-8 context columns). E.10 LEX-BUNDLE (4-register naming:
tech / plain / legacy / mnemonic). SenseCells per non-trivial cell.
Bridges explicit equivalence mappings + F.9 Bridge + CL measurement.

**File:** **`wiki/foundations/jetix-uts.md`** — central table.

**Layout A structure:**
- **Rows (30-50):** Jetix U.Types (roles / alphas / concepts /
  mechanisms / principles / decisions / artifacts)
- **Columns (7-8 context):**
  1. FPF U.Type (canonical FPF-Spec reference)
  2. Jetix tech (engineering-grade term, ASCII-friendly identifier)
  3. Jetix plain (client-facing / plain English / plain DE)
  4. ШСМ-Russian (Левенчук legacy term)
  5. Essence-legacy (SEMAT Essence / v1 mapping — historical)
  6. DACH-legal (HGB / AktG / BGB / GDPR terms applicable)
  7. AI-industry (industry-standard vocabulary)
  8. Bridges (explicit equivalence mappings between contexts)
  + **Rationale** column — why this row included, key distinctions

**LEX-BUNDLE 4-register per row:**
- tech — engineering identifier (`client-relationship`)
- plain — plain-language term (`Kundenbeziehung / client relationship`)
- legacy — historical / SEMAT Essence term (`customer`)
- mnemonic — shorthand для communication (`C-Rel`)

**SenseCells per non-trivial cell** — clarify domain-specific sense
when term ambiguous across contexts.

**Bridges** — explicit equivalence mappings + CL (Congruence Level
1-5) measurement for semantic drift between contexts. Frontmatter
convention: `bridges-to: [context-a, context-b]` + `cl-level: 3` per
mapping.

**Timing (OQ-08 B):** **concurrent с D6 JETIX-FPF writing** — UTS
rows = U.Types = D6 Section 8 ontology. Single source of truth;
prevents dual-maintenance drift.

**Maintenance:** FPF-Steward quarterly audit scope includes UTS
review (row additions, Bridges updates, CL re-measurement).

**Cost:** 6-10h Phase 1 setup + ~2h per quarter FPF-Steward audit.

### 5.12 Multi-View Publication Kit (E.17 Viewpoint Bundle) — NEW Chunk 8

**FPF basis:** E.17 Multi-View Publication Kit. E.17.0
U.MultiViewDescribing (Viewpoints / Views / Correspondences). E.17.1
U.ViewpointBundleLibrary. E.17.2 TEVB (Typical Engineering Viewpoints
Bundle). Plus E.18 TGA Transduction Graph (simpler form via A.6.3.CR
ConservativeRetextualization для safe cross-view translation).

**Scope (per OQ-04 modified stronger):** **mandatory multi-view для
ALL Audit SKU deliveries from first delivery onward** (не pilot-only).

**Jetix Viewpoint Bundle — 5 viewpoints Phase 1:**

| # | Viewpoint | Audience | Depth | Language |
|---|-----------|----------|-------|----------|
| 1 | **Executive** | CEO, Aufsichtsrat | 2-3 pages | plain + finance |
| 2 | **Technical** | CTO, engineers | 20-40 pages | technical + specs |
| 3 | **Governance** | board, risk committee | 3-7 pages | governance + legal |
| 4 | **Regulatory** | BfDI, EU AI Act auditors | 3-5 pages | regulatory + legal (pre-mapped EU AI Act / GDPR Art. 22 / EU DORA) |
| 5 | **Internal-learning** | Jetix team | 5-10 pages | internal + FPF patterns referenced |

**Artifacts:**
- **`decisions/templates/jetix-viewpoint-bundle.yaml`** — Viewpoint
  definitions (name / audience / depth / language / canonical-sections
  -mapping)
- **`decisions/templates/audit-canonical-template.md`** — underlying
  canonical artifact structure (single source of truth per audit)
- **`decisions/templates/views/`** — 5 view templates:
  - `view-executive.md`
  - `view-technical.md`
  - `view-governance.md`
  - `view-regulatory.md`
  - `view-internal-learning.md`
- **Correspondences table** — canonical section → view section mapping
  (automated rendering check; FPF-Steward audit scope)
- **Update protocol:** canonical changes → views regenerated (A.6.3.CR
  Same-Entity Retextualization discipline prevents semantic drift)

**First pilot:** Müller GmbH audit (or first actual Audit SKU client).

**Cost:** 3-5h setup + 8-12h first pilot + marginal ongoing after
templates mature.

**ISO/IEC/IEEE 42010 alignment** noted (professionalism signal к
Aufsichtsrat-grade clients).

### 5.13 Bias-Audit Cycle (D.5) — NEW Chunk 8

**FPF basis:** D.5 Bias-Audit & Ethical Assurance.

**4-stage cycle:**
- **BA-0 Kickoff** — scope declaration, Bias Register initialization
- **BA-1 Scan** — structured bias scan across taxonomy (REP/ALG/VIS/
  MET/LNG)
- **BA-2 Panel Review** — external panel evaluation (**deferred к
  Phase 2a** — Beirat Ethics advisor activation)
- **BA-3 Closure** — mitigation plan, residual bias acceptance, sign-off

**Phase 1 simplified cycle:** BA-0 + BA-1 + BA-3 (solo Ruslan, no
BA-2 Panel Review).

**Artifacts:**
- **`decisions/policy/bias-audit-cycle.md`** — policy + 4-stage cycle
- **`decisions/templates/bias-audit/`**:
  - `ba-0-kickoff-template.md`
  - `ba-1-scan-template.md`
  - `ba-3-closure-template.md`
- **`bias-register.yaml` schema** per deliverable
- Per-deliverable structure: `clients/<client>/audits/<audit>/
  bias-audit/`
- Quarterly aggregation: **`decisions/bias-audit/YYYY-QN-bias-audit.md`**

**Bias Taxonomy (5-class):**
- **REP** — representation bias (demographic under-representation)
- **ALG** — algorithmic bias (model architecture / training)
- **VIS** — visual bias (UI, visualization choices)
- **MET** — measurement bias (metric design, operational definitions)
- **LNG** — linguistic bias (translation, terminology, framing)

**Integration:**
- `decisions/policy/eu-ai-act.md` (OT3 compliance calendar)
- FPF-Steward quarterly audit scope (R12 + Chunk 8 expansion)
- Art. 22 GDPR defence strengthened

**Cost:** 3-5h setup + 1h per deliverable + 2h quarterly.

**Rationale:** EU AI Act compliance Aug 2026; Art. 22 GDPR defence;
enterprise client readiness (DACH Mittelstand Compliance VP expects
formal bias-audit trail).

### 5.14 Phase Transitions MHT (B.2) — NEW Chunk 8

**FPF basis:** B.2 Meta-Holon Transition. Plus B.2.1 Emergence, B.2.2
Re-identification, B.2.5 Supervisor-Subholon Feedback Loop.

**4 MHTs documented Phase 1** (file: **`decisions/policy/phase-
transitions-mht.md`**):

#### MHT-1: Phase 1 → 2a (solo + hire)
- **Trigger:** Triple-AND (€20K MRR × 3mo + Ruslan >40% L1/L2 time +
  ≥1 client requesting GDPR DPA)
- **Emergence signals:** bottlenecks в Ruslan scheduling, increasing
  L1-ops time ratio, DPA request from client
- **Re-identification:**
  - **Invariants:** 8 true alphas preserved; JETIX-FPF preserved; git
    = SoT; 18 role-manifests preserved (некоторые re-bound human
    executor instead of Ruslan)
  - **Mutables:** executor-bindings (Ruslan → Human hire); physical
    separation (life-os/jetix filter-repo extract)
- **Supervisor-subholon feedback:** Ruslan (supervisor) ↔ first hire
  (subholon) — weekly 1:1, quarterly review

#### MHT-2: Phase 2a → 2b (team 5-20)
- **Trigger:** team size >=5 OR 3+ concurrent active directions
- **Invariants:** Portfolio model preserved; FPF-Steward сохраняется
  (возможно separated role); roles preserved (but instance count grows)
- **Mutables:** Chief of Staff activated; customer-success
  materialized; FPF-Steward potentially separate role (30+ agents
  trigger)

#### MHT-3: Phase 2b → 2c (€10-50M, multi-entity, first acquisition)
- **Trigger:** revenue €10M+ OR first acquisition OR 2nd entity formed
- **Invariants:** Portfolio model preserved; UTS central preserved;
  JETIX-FPF maintained
- **Mutables:** federation pattern activated (`entities/jetix-gmbh/`
  becomes real); holdings structure materialized; L7 materialized

#### MHT-4: Phase 2c → 3 (€50M+, multi-entity federation)
- **Trigger:** revenue €50M+ OR Aufsichtsrat formalized
- **Invariants:** JETIX-FPF; UTS; 8 alphas (per entity); A.14 mereology
- **Mutables:** physical separation на разные servers/clouds; Ecosystem
  Resources first-class materialized; BA-2 Panel Review fully
  operational

**Template:** **`decisions/templates/mht-template.yaml`** — reusable
for future transitions.

**Integration:**
- D8 rollout (MHTs reflected в timeline)
- D7 career levels (phase-column mapping)
- D4 Life-OS separation (Phase 2a / 3 triggers)
- Section 10 Review Triggers alignment

**Cost:** 2-4h Phase 1 + 2h per transition when happens.

### 5.15 Agency CHR + Role Assignment Cycle (A.13, F.6) — NEW Chunk 8

**FPF basis:** A.13 Agential Role & Agency Spectrum (plus A.13:4.3
Agency-CHR). F.6 Role Assignment & Enactment Cycle (Six-Step).

**Agency-CHR fallback (Rec-08):**

`executor-binding.yaml` получает `agency-profile` section (см. Section
5.3 schema). Formal agency-scale 0.0-1.0 dimension adds к 3-tier
J-Auto/Approve/Strategic.

- Default agency per executor (0.4 mid-range typical)
- Override per decision class (j-auto ~0.8; j-approve ~0.4; j-strategic
  ~0.0)
- Fallback rule: if uncertain classification, downgrade to lower
  agency (conservative default)

**F.6 6-step Role Assignment Cycle (Rec-15):**

Extends already-accepted `agent_onboarding` (Левенчук Part 3 #2) с
full cycle:
1. **Identify** — candidate executor для role fit check
2. **Request** — role sponsor requests assignment
3. **Propose** — candidate proposes fit (evidence, onboarding plan)
4. **Negotiate** — constraints + authority scope negotiated
5. **Enact** — assignment live; warm-up tasks + calibration
6. **Retrospect** — 30/90/180-day retrospective; re-negotiation or
   exit

Template: embedded в `agent_onboarding` section of `executor-binding.
yaml` (see Section 5.3).

**Cost Rec-08 + Rec-15:** 2-4h total.

---

## Section 6 — Evolution diff: v1 → v2 → v2-Ruslan-approved → v3-post-FPF-discovery

### 6.1 Compact 4-column table

| Aspect | v1 (baseline) | v2 (post-review) | v2-Ruslan-approved | **v3-post-FPF-discovery** |
|--------|---------------|------------------|-------------------|---------------------------|
| Core principles | 7 | 7 (refined) | **8** (+Portfolio of Directions) | 8 (refined P2 Agency / P3 A.14 / P4 Nested Holonic / P8 C.18-19) |
| Folders Phase 1 | 22 | 11 | **15** (+directions/, inbox/, outreach/) | 15 (expanded внутри: directions/ + ee-log/nqd/kill-chr; wiki/foundations/ += uts + fpf-tooling + innovations; decisions/policy/ +9 docs; decisions/templates/ +5 doc; decisions/bias-audit/; decisions/fpf-stewardship/) |
| True alphas | 10 | 7 (+3 WP, 1 entity) | **8** (+Direction) | 8 (same; с A.14 typed mereology edges retrofit) |
| Role manifests Phase 1 | 12 | 12 | **18** | 18 (executor-binding.yaml += agency-profile + F.6 cycle + agent_onboarding retrospective) |
| FPF document name | "FPF-Lite" | "FPF-Lite" | "FPF" (full, drop "Lite") | **"JETIX-FPF"** (attribution clarity, OQ-01 B) |
| FPF size | 3-5 pages | 3-5 pages | 30-50 pages max Левенчук | 20-30 Core + 10-20 Tooling companion (OQ-07 C soft split) |
| FPF loading | reference-only | few additions | Full text everywhere (OT5 A) | Full text везде + UTS concurrent write (OQ-08 B) |
| Mereological graph | simple dependencies | Lite Phase 1 + Full Phase 2 | Full 3-level Phase 1 (MC3 override) | **A.14 typed edges retrofit** (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf + Jetix 4) |
| Model D terminology | "Model D" | "Model D" | "Model D Nested Hierarchy" | **"Nested Holonic Structure" (FPF A.1 + A.14 canonical)** retired Russian lineage (OQ-06 B) |
| Resources first-class | Capital + Hours implicit | Capital + Hours + Attention | Capital + Compute + Deep Hours + Attention Budget + Ecosystem (11 cat) | Same (unchanged) |
| Life-OS ≠ Jetix | shared logical | Phase 2a extraction | Day 1 physical separation, Phase 3 different servers | Same (MHT-1 formalized, Rec-06) |
| Trustee | unspecified | Anton designated | TBD ≠ Anton (open) | Same (carry forward в Section 12) |
| FPF-Steward | none | none (meta-agent sufficient) | Sub-role в meta-agent Phase 1 (R12 override) | **Expanded scope** (UTS + F-G-R + edge-types + CHR integrity + Viewpoint Bundle correspondences + semi-annual upstream sync reminder) |
| Market scope | DACH-only | DACH-locked Phase 1-2 | DACH + US + RU, unified funnel Day 1 | Same (unchanged) |
| Multi-currency | deferred | rejected (R10) | External via Stripe/Wise + placeholder | Same (unchanged) |
| Bilingual frontmatter | Russian-only | EN summary policy/decisions/roles | Hybrid (Scenario E): EN summary + auto-translation hook + per-language outreach | Same (strengthened toward EN-primary ontological layer per OQ-06 B) |
| Rollout | 14-day Foundation-first | 7+7 split | Same + realistic 7+10-12 tolerance | **7+10-14** (Chunk 8 parallel tracks heavier; UTS + Viewpoint Bundle + F-G-R retrofit days 15-17) |
| Pre-commit hooks | 2 | 3 | 4 (+past-participle) + 5-ый auto-translation | Same (unchanged) |
| EU AI Act | internal-only | placeholder policy | Scenario C risk-proportional (4 tiers) + compliance calendar + DPA template | Same + **D.5 Bias-Audit Cycle** (Rec-03) integration |
| Trademark Jetix | assumed ok | flagged | Perplexity research + backlog entry | Same (unchanged) |
| crazy-agent level | J2 ad-hoc | J2 | J2 "brainstorming mode outside normal ladder" | Same (unchanged) |
| life-coach placement | Jetix agent | Jetix agent | Life-OS only | Same (unchanged) |
| AI promotion mechanism | 90-day self-graded | informal | External review (meta-agent evidence) + Ruslan sign-off | **A.18 CSLC formal** (mandatory, OQ-11) |
| **Trust tagging** | none | none | none | **F-G-R all ADRs + client deliverables + agent outputs (Gap 2)** |
| **Boundary discipline** | none | none | none | **A.6.B L/A/D/E all contracts (Gap 1)** |
| **CHR spaces** | none | none | none | **SKU + direction-kill + agent-promotion CHR formal (Gap 3)** |
| **UTS** | dispersed | dispersed | dispersed | **Centralized F.17 + LEX-BUNDLE 4-register (Gap 4)** |
| **Multi-view publication** | single | single | single | **E.17 Viewpoint Bundle mandatory all Audit SKU (Gap 5)** |
| **Bias-audit** | implicit | implicit | OT3 | **D.5 Cycle formal (BA-0/1/3; BA-2 Phase 2a) (Rec-03)** |
| **Phase transitions** | informal | triggers | triggers | **B.2 MHT formal 4 transitions (Rec-06)** |
| **Agency-CHR** | implicit | implicit | 3-tier | **A.13:4.3 fallback formal 0.0-1.0 (Rec-08)** |
| **Method harmonization** | none | none | none | **F.11 monthly per-direction (Rec-18)** |
| **Multi-method dispatcher** | none | none | none | **G.5 MethodFamily Registry (Rec-21)** |
| **Problem-CHR intake** | informal | informal | informal | **C.22 TaskSignature structured (Rec-16)** |
| **SKU signatures** | informal | informal | informal | **A.6.S versioned (Rec-19)** |
| **Mechanism introduction** | informal | informal | informal | **E.20 protocol formalized (Rec-20)** |
| **Canonical Evolution Loop** | implicit | implicit | implicit | **B.4 Observe/Reflect/Decide/Act mapped к 4 rituals (Rec-14)** |
| **Innovations sharing** | no policy | internal | internal | **Hard no-contribute (OQ-09 A)** |
| **FPF upstream sync** | n/a | n/a | n/a | **Semi-annual Ruslan manual reminder (OQ-10 C modified)** |

### 6.2 11 Ruslan overrides preserved (from Chunks 1-7)

Каждый override зафиксирован с rationale / quote / implications.

**Override #1 — Compute as 4th first-class resource.**
Ruslan Chunk 1 P7: "заносим в first principles". Machine cognition
становится как Capital / Hours — finite, measurable, budget-worthy.
Implications: `finance/compute-ledger.yaml`, per-executor compute
contract, monthly review.

**Override #2 — Deep Hours refinement (Attention → Hours collapse).**
Ruslan: "мне понравился вариант C; capital + compute + deep hours;
attention budget — квартальный уровень". Attention-as-daily-ledger-
metric — slippery. Hours refined to Deep Hours (session с Claude Code
/ strategic thinking / deep learning / architectural work / client
deliverable — yes; email triage / routine admin / meetings без
decision-making — no). Toggl `[deep]/[shallow]` tags; target 25-30
deep hours/week.

**Override #3 — Ecosystem Resources detailed (11 categories).**
Phase 3 first-class ресурс: advisory / community / partnerships /
brand equity / DACH institutional / alumni / media / talent / capital
/ academic / regulatory. Infrastructure Phase 1 prep: `governance/
advisory-board/members.yaml` (Anton/Vladislav/Rodion formalized
informally). Ruslan: "фаза 3 ecosystem это тоже очень важно".

**Override #4 — Trustee identity TBD, not Anton.**
v2 synthesis MC4 резолвил Anton как designated trustee. Ruslan
explicit: "но это будет потом, это будет тоже не Антон". Implications:
`governance/trustee-designations.md` пишется с `{trustee: TBD}`
placeholder.

**Override #5 — DACH primary + US + RU secondary с Day 1 unified funnel.**
v2 — "DACH-locked". Ruslan modification: "основной упор на DACH, но
при этом ещё будет US и русскоязычное тоже; они все у нас будут
проходить через одну воронку, или через один вид оплаты". Stripe/Wise
external multi-currency; split outreach folders per language.

**Override #6 — Full 3-level mereological creation graph Phase 1.**
v2 — "Lite Phase 1 + Full Phase 2". Ruslan MC3 override: "Три уровня
mereological важно, обязательно мы делаем все три уровня максимально
глубоко. Никаких упрощений". Cost +4-8h Phase 1. Artifact: `wiki/
foundations/jetix-creation-graph.md`. **Post-Chunk 8:** A.14 typed
edges retrofit.

**Override #7 — Physical Life-OS/Jetix separation Day 1.**
v2 — "shared logical Phase 1". Ruslan: "Life-OS и Jetix должны быть
принципиально вообще разделены. Потом физически разделим на разных
серверах". Parallel mount; asymmetric reference rule; Phase 2a `git
filter-repo` extraction.

**Override #8 — Portfolio of Directions (8-ая alpha + 8-ой principle).**
Ruslan: "Jetix = большая корпорация, десятки направлений. Jetix как
холдинг для кросс-функционального наблюдения". Model: Hybrid Variant
1+4. **Post-Chunk 8:** C.18 NQD-CAL + C.19 E/E-LOG per-direction
(Rec-07).

**Override #9 — Full FPF (renamed from FPF-Lite), 30-50 pages.**
v2 — "FPF-Lite 3-5 pages". Ruslan: "Мы к этому документу подходим
глубоко. Он не должен быть light". **Post-Chunk 8:** renamed к
**JETIX-FPF** (OQ-01 B); soft split Core (20-30 pages) + Tooling
companion (10-20 pages) per Rec-13 / OQ-07.

**Override #10 — Full FPF text everywhere (не reference-only).**
OT5 Sub-question 1. Ruslan: "Мы оставляем эти FPF контексты полностью
на всех". Monthly cost ~$5-10. **Post-Chunk 8:** strengthened — hard
internal-only (OQ-09 A) + semi-annual sync reminder (OQ-10 C modified).

**Override #11 — FPF-Steward sub-role Phase 1.**
v2 R12 — "REJECT". Ruslan: "мне нужен Левенчук на максимум. Берем
вариант B и внедряем глубоко". Sub-role в meta-agent. **Post-Chunk 8:**
scope expanded (UTS audit + F-G-R compliance + A.14 edge-types + CHR
space integrity + Viewpoint Bundle correspondences + semi-annual FPF
sync trigger).

### 6.3 25+ new additions from Chunk 8

Enumerated (not exhaustive):

1. **JETIX-FPF naming** (OQ-01 B)
2. **Nested Holonic Structure** terminology (OQ-06 B, Anglicize)
3. **Boundary Discipline A.6.*** (Gap 1) — L/A/D/E routing + cluster
4. **Trust & Assurance F-G-R tagging** (Gap 2) — ADRs + deliverables +
   agent outputs
5. **Characteristic Spaces A.17-21** (Gap 3) — 3 CHR formal (SKU /
   direction-kill / agent-promotion)
6. **UTS F.17 centralized** (Gap 4) — 30-50 rows concurrent с D6
7. **LEX-BUNDLE 4-register** (Rec-12 via Gap 4)
8. **Bridges + CL convention** (Rec-10)
9. **Multi-View Viewpoint Bundle** (Gap 5) — mandatory Audit SKU
10. **Bias-Audit D.5 Cycle** (Rec-03) — BA-0/1/3 Phase 1
11. **A.14 typed mereology edges** (Rec-05)
12. **B.2 MHT phase transitions** (Rec-06) — 4 MHTs
13. **C.18 NQD-CAL + C.19 E/E-LOG** per-direction (Rec-07)
14. **A.13:4.3 Agency-CHR fallback** (Rec-08)
15. **E.5.1 DevOps Lexical Firewall** — soft split D6 (Rec-13)
16. **B.4 Canonical Evolution Loop** (Rec-14)
17. **F.6 Role Assignment 6-step cycle** (Rec-15)
18. **C.22 Problem-CHR TaskSignature** (Rec-16)
19. **A.16 PreArticulationCuePack** (Rec-17)
20. **F.11 Method Quartet Harmonisation** (Rec-18)
21. **A.6.S SKU signature versioning** (Rec-19)
22. **E.20 Mechanism Introduction Protocol** (Rec-20)
23. **G.5 Multi-Method Dispatcher** (Rec-21)
24. **First Q2 2026 FPF-Steward audit** (Rec-22)
25. **Hard internal-only stance** (OQ-09 A) — no contribute-back
26. **Semi-annual FPF sync reminder** (OQ-10 C modified) — Ruslan manual
27. **9 Innovations catalog** — `wiki/foundations/jetix-innovations.md`
28. **F-G-R frontmatter schema** — ADR + deliverables
29. **agency-profile section** в executor-binding.yaml
30. **role_assignment_cycle section** в executor-binding.yaml
31. **MHT template** `decisions/templates/mht-template.yaml`
32. **Viewpoint Bundle template** + 5 views
33. **FPF-Steward scope expansion** — UTS / F-G-R / edge-types / CHR
    integrity / Correspondences / sync reminder

---

## Section 7 — Outstanding Tensions Resolution

### 7.1 v2 OT5 (все 5 resolved в Chunks 1-4; Post-Chunk 8 reconfirmation)

**OT1 Strategic-management decomposition — RESOLVED EARLY Chunk 1 P5.**
5 atomic sub-ролей (strategy-lead / framing-lead / sales-closer /
acceptance-authority / external-relations) + `executors/ruslan.yaml`
multi-role-binding (hybrid founder-mode).

**OT2 Bilingual frontmatter — Scenario E (Hybrid).**
Namespace conventions (unchanged post-Chunk 8):
- `policy/`, `decisions/` — bilingual (`lang: [ru, en]`), EN summary
  mandatory 150-300 words + RU body
- `roles/` — EN primary (`lang: en`); DE добавляется Phase 2a closer
  to 1st hire
- `ops/` — EN primary (trustee emergency accessibility)
- `wiki/concepts/`, `wiki/summaries/`, `directions/*/direction.md` —
  RU primary + auto-translation hook (5-ый pre-commit: `auto_en: true`
  triggers Opus 4.7 translation → saves `.en.md` sibling)
- `wiki/sources/`, `wiki/ideas/`, `alphas/` — RU default
- `finance/` — DE mandatory (HGB compliance)
- `clients/<id>.md` — internal notes RU; `client_language: de|en|ru`
  frontmatter для client-facing
- `outreach/` — separate folders per language (`de/`, `en/`, `ru/`):
  different copy, not translations

**Post-Chunk 8 subtle strengthening:** OQ-06 B (Anglicize Model D →
Nested Holonic Structure) aligns с OT2 direction toward EN-primary
ontological layer where FPF canonical applies.

Cost: 8-13h setup (5-10h EN summaries 30-50 docs + 2-3h auto-
translation hook) + ongoing €1-5/mo API.

**OT3 EU AI Act tier — Scenario C (Risk-proportional) + calendar + DPA.**
4 categories с different human gates (unchanged; plus Chunk 8 **D.5
Bias-Audit Cycle integration** per Rec-03 — compliance calendar +
bias-audit cycle jointly support Aug 2026 High-risk obligations
readiness).

| Category | Risk | Gate | Examples |
|----------|------|------|----------|
| Internal-only | Minimal | None (J-Auto) | Research, wiki ingestion, summaries |
| External reversible | Low-medium | Batch approval (J-Approve batch) | Outreach drafts (batch 20/week), social scheduling |
| External non-reversible | High | Per-action approval (J-Approve per) | Send specific email, publish content |
| Strategic / regulatory | Critical | Ruslan explicit (J-Strategic) | Sign contract, offer discount, compliance claim |

**OT4 Trademark Jetix vs Disney — DEFER (Perplexity research + backlog).**
Phase 1 informal usage; trigger €20-50K revenue. Backlog entry
`decisions/backlog/trademark-jetix-formal-resolution.md`.

**OT5 FPF token-budget + publishing — Variant A (full text) + Internal-only.**
См. Overrides #10 и #9 выше. **Post-Chunk 8:** strengthened hard
internal-only (OQ-09 A) + semi-annual Ruslan manual sync reminder
(OQ-10 C modified).

### 7.2 Chunk 8 11 Open Questions (all resolved)

См. ADR Chunk 8 Section 8.5 за detail. Summary:

| OQ | Topic | Decision |
|----|-------|----------|
| 01 | FPF rename | ✅ **B — JETIX-FPF** |
| 02 | P1 adoption scope | ✅ All 6 P1 + 3 P2 elevated |
| 03 | Portfolio NQD+E/E-LOG timing | ✅ Phase 1 (wiki artifact) |
| 04 | E.17 Multi-View threshold | ✅ **Modified A — Mandatory от first delivery** |
| 05 | F-G-R scope | ✅ ADRs + client deliverables + agent outputs |
| 06 | Model D terminology | ✅ **B — Anglicize (Nested Holonic Structure)** |
| 07 | D6 Core/Tooling split | ✅ Soft split (Option C) + wiki companion |
| 08 | UTS timing | ✅ Concurrent с D6 (Variant B) |
| 09 | Contribute-back | ✅ **A — No contribution (hard)** |
| 10 | Upstream FPF sync | ✅ **Modified C — Semi-annual reminder, Ruslan manual** |
| 11 | Agent promotion CSLC | ✅ A.18 CSLC full (mandatory) |

---

## Section 8 — Consequences

### 8.1 Что architecture enables (additional post-Chunk 8)

- **Mega-corp readiness без premature-materialization cost** — Reference
  architecture полный 7-layer, Operational Phase 1 lean 4-layer,
  triggered expansion painless.
- **Portfolio research engine** — cross-functional observation через
  wiki/concepts/ + edges.jsonl (A.14 typed) + direction-frontmatter
  convention; multiple bets одновременно; C.18 NQD-CAL + C.19 E/E-LOG
  per-direction discipline.
- **Solo-to-team transition без re-architecture** — 5 Ruslan atomic
  sub-ролей + 18 role-manifests + Role ≠ Executor + **A.13:4.3 Agency-
  CHR** + **F.6 6-step cycle** дают clean delegation paths при 1st
  hire (Phase 2a / MHT-1).
- **DACH + US + RU с Day 1** — unified funnel; Stripe/Wise external
  currency; split outreach per-language; legal compliance built-in
  (EU AI Act calendar + **D.5 Bias-Audit Cycle**, GDPR DPA template
  с **A.6.B L/A/D/E** structure, HGB `finance/` DE frontmatter).
- **Investment-grade foundation** — audit trail via git; formal ADRs
  с **F-G-R trust tags**; role-manifests; Constitution; JETIX-FPF
  (constitutional-depth); **multi-view publication** ready-to-deliver
  для Aufsichtsrat-grade stakeholders. Due diligence ready без
  retroactive documentation marathon.
- **Левенчук-correct ontology** — full 8 true alphas, past-participle
  strict, **3-level mereology с A.14 typed edges**, 17 trans-disciplines
  reference, holons recursive (**Nested Holonic Structure**).
  **FPF-Steward quarterly audit** (expanded scope) предохраняет от
  onto-drift; **UTS central** prevents terminology divergence;
  **semi-annual FPF sync** keeps alignment with upstream Левенчук.
- **Client deliverable excellence** — **Viewpoint Bundle** (5 views)
  serves Mittelstand audiences in parallel; **A.6.3.CR** Same-Entity
  Retextualization prevents semantic drift across views.
- **Phase transitions architected** — **B.2 MHT** 4 transitions
  documented (1→2a / 2a→2b / 2b→2c / 2c→3); invariants preserved,
  mutables explicit.
- **Defensible pricing + promotion** — **CHR spaces formal** (SKU
  pricing / direction kill / agent promotion) — measurable decisions
  > subjective, audit-trail grade.

### 8.2 Что architecture costs

- **Phase 1 setup work ~140-220h total (v0.5 was 80-120h):**
  - Previous Stage 4 writing commitment (D1-D8, Chunks 1-7): 80-120h
  - **Post-FPF-Discovery additions (Chunk 8): 60-98h** — 5 Gaps full
    depth (30-45h) + P1 standalone recs (Rec-03/05/06 7-13h) + P2
    (13-22h) + P3 (8-14h) + first FPF-Steward Q2 audit (2-4h)
- **Ongoing ~8-15h/month FPF maintenance** (v0.5 was 5-10h) + quarterly
  FPF-Steward audit expanded scope (~3-5h/quarter Phase 1).
- **API spend €300-800/month run rate** Phase 1; €3,600-9,600 12-month;
  break-even 1st Audit SKU.
- **Cognitive overhead Phase 1** — 15 folders, 18 manifests, 8 alphas,
  4 rituals + CHR spaces + UTS + Viewpoint Bundle + F-G-R tagging +
  bias-audit cycle. Mitigation: agents помогают (meta-agent
  onboarding, FPF-Steward audits expanded scope, inbox-processor
  triage + A.16 PreArticulationCuePack, knowledge-synth synthesis).
- **Realistic calendar:** 3.5-5.5 weeks intensive.

### 8.3 Что architecture forbids (explicit negative space; updated)

- **Notion как parallel SoT** — decommission Day 14.
- **Dynamic role assignment** — кроме `executors/ruslan.yaml` founder
  exception.
- **Jetix files referencing Life-OS paths** — Hook 1 blocks.
- **Gerund states** (`qualifying` vs `qualified`) — Hook 4 blocks.
- **Agent strategic decisions** — agents не стратегируют (Левенчук
  §1.4); `strategy-support-analyst` — support only, J3 level.
- **Internal multi-currency bookkeeping Phase 1** — Stripe/Wise external.
- **JETIX-FPF publishing external** — internal-only Phase 1+, secret
  sauce.
- **Life-coach в Jetix ladder** — миграция в Life-OS.
- **ADR без F-G-R tags** — meta-agent enforcement blocks (NEW Chunk 8).
- **Client deliverable без Viewpoint Bundle** — Audit SKU delivery
  blocked (NEW Chunk 8).
- **Contract без L/A/D/E structure** — proposal / contract / DPA
  templates enforce (NEW Chunk 8).
- **Agent promotion без A.18 CSLC** — promotion process mandatory
  formal (NEW Chunk 8, OQ-11).
- **Contribute-back к ailev/FPF community** — hard internal-only (NEW
  Chunk 8, OQ-09 A).
- **Automatic FPF upstream sync** — only semi-annual reminder, Ruslan
  manual decision (NEW Chunk 8, OQ-10 C modified).

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
| JETIX-FPF full text in system.md | Reversible | Swap back to reference-only loading (OT5 Scenario B) |
| Compute as first-class | Reversible | Collapse compute-ledger.yaml → informal tracking |
| Portfolio Directions | Semi-reversible | `directions/` можно deprecate; wiki frontmatter requires cleanup |
| **F-G-R tagging** (NEW) | Reversible | Meta-agent enforcement disabled; frontmatter tags remain as info-only |
| **Boundary Discipline L/A/D/E** (NEW) | Reversible | Collapse to simpler 2-section structure; A.6 cluster reference only |
| **CHR spaces** (NEW) | Reversible | Collapse to informal heuristics; keep ChR yaml files reference-only |
| **UTS** (NEW) | Semi-reversible | Collapse to scattered glossaries; bridges / CL measurements lost |
| **Multi-View Viewpoint Bundle** (NEW) | Reversible | Revert to single document; templates archived |
| **Bias-Audit Cycle** (NEW) | Reversible | Collapse к informal review; BA artifacts preserved reference-only |
| **B.2 MHT formal** (NEW) | Reversible | Collapse к informal phase triggers; MHT docs archived |
| **A.14 typed edges** (NEW) | Reversible | Retag back к generic edges; documentation preserved |

### 9.2 Hard-to-reverse decisions

- **Physical Life-OS ≠ Jetix separation Day 1** — requires `git filter-
  repo` reverse-merge (complex; 4-8h work). Mitigation: principle
  строгий, reversal probability low.
- **Past-participle rename** — applied везде; reversing semantic
  inconsistency создаст технически. Mitigation: convention ШСМ-
  grounded, reversal unlikely.
- **FPF-Steward sub-role expanded scope** — can deactivate by removing
  section; re-activation cheap. Low lock-in.
- **JETIX-FPF naming** (NEW Chunk 8) — rename-back potentially
  disruptive к cross-references в D1/D2/D4/D5/D6; mitigation: naming
  convention settled early, reversal unlikely.
- **Nested Holonic Structure terminology** (NEW Chunk 8) — terminology
  propagated across all docs; reversal creates Russian-English
  inconsistency. Mitigation: FPF canonical grounds decision,
  permanent.
- **Internal-only hard stance (OQ-09 A)** (NEW Chunk 8) — nothing
  published; reversal trivial technically (just publish), но
  reputational reversal может быть delicate. Mitigation: principle
  durable, reversal trigger explicit (Phase 3+ revisit).

### 9.3 Rebuild paths

- **Full JETIX-FPF burden excessive:** collapse к FPF-Lite v2 (3-5
  pages); hold full version в `wiki/foundations/fpf-full.md` как
  reference; loading switches to Lite.
- **18 manifests burden excessive:** compress к v2 (core 7 + skeleton
  5) rolling strategy; reconcile later.
- **Federation stub scaling cost:** если `entities/jetix-gmbh/` Day 1
  становится burden — collapse к `entities/README.md` placeholder;
  scaffold восстанавливается при 2nd entity emergence.
- **UTS maintenance burden excessive** (NEW): collapse к 10-15 most
  critical rows; extended rows move к per-context glossaries; FPF-
  Steward audit scope reduced.
- **CHR spaces too formal burden** (NEW): collapse к informal
  heuristics; keep structured YAMLs reference-only; formal CSLC
  re-activated only when specific decision requires audit trail.
- **Viewpoint Bundle burden excessive** (NEW): reduce к 2-3 viewpoints
  (Executive + Technical + Regulatory); drop Governance + Internal-
  learning for first iterations.

---

## Section 10 — Review Triggers

Когда эта архитектура пересматривается:

1. **Every 6 months** — formal architecture review (quarterly ritual
   extension); compare actual vs designed; update ADR с deltas.
2. **Semi-annual FPF upstream sync reminder** (NEW Chunk 8, OQ-10 C
   modified) — every 6 months (Q2 close + Q4 close) FPF-Steward
   flags "upstream FPF sync review due"; Ruslan manual decision
   whether to sync.
3. **Quarterly FPF-Steward ontology audit** (R12 + expanded scope per
   Chunk 8) — UTS review + F-G-R compliance + edge-type verification
   + CHR space integrity + Viewpoint Bundle correspondences; output
   `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md`.
4. **Phase transitions (B.2 MHT formal):**
   - **Phase 2a trigger (MHT-1)** (Triple-AND: €20K MRR × 3mo + Ruslan
     >40% L1/L2 + ≥1 client requesting GDPR DPA) — Life-OS extraction,
     2nd entity decision, Customer Success activation, BA-2 Panel
     activation, Beirat formal.
   - **Phase 2b trigger (MHT-2)** — Chief of Staff hire, FPF-Steward
     separate role (30+ agents OR 1+ human meta-hire OR quarterly
     audit >4h), L3 CRM full materialization (5+ concurrent clients).
   - **Phase 2c trigger (MHT-3)** — 2nd entity emergence → federation
     pattern activated; Holdings architecture L7 materialized.
   - **Phase 3 trigger (MHT-4)** — different servers/clouds; Ecosystem
     Resources first-class; Aufsichtsrat.
5. **Critical incident** — breaking architecture invariant (Hook
   failure, ontology drift detected, unexpected compute cost spike
   >3×).
6. **Major Левенчук framework update** — new ШСМ primitives или
   changed mereology semantics → FPF-Steward quarterly audit
   initiates revision.
7. **30+ agents milestone** — FPF-Steward separate role; `roles/`
   отдельный top-level; `comms/mailboxes/` materialized.
8. **Regulatory inflection** — EU AI Act High-risk obligations go
   live (Aug 2026; tied к D.5 BA-2 Panel activation); BaFin inquiry;
   Bundeskartellamt contact; new Member State implementation law.
9. **Direction kill-criteria hit** — `_active` direction fails kill
   criteria CHR (NEW: formal per Gap 3) → post-mortem + archive,
   attention-theme re-balance.
10. **Trademark Jetix formal resolution** — при revenue €20-50K range.
11. **First CHR space refinement (NEW Chunk 8)** — SKU pricing CHR
    may need iteration after first client negotiation.

---

## Section 11 — References

### 11.1 Decision artifacts

- **Approval ADR (Stage 3 + 3.6 journal):** `decisions/2026-04-19-
  architecture-v2-approval.md` (APPROVED 2026-04-20, includes Chunks
  1-7 + **Chunk 8 Post-FPF-Discovery Additions** same-day append)
- **Gap Analysis review tracking:** `decisions/gap-analysis-review-
  decisions-2026-04-20.md` (60+ decisions, Notion mirror:
  <https://www.notion.so/3482496333bf8174a7ffd6f30c02f0bf>)
- **Progress checklist:** `decisions/review-v2-progress-checklist.md`.
- **This document (D9 draft v0.6):** `decisions/2026-04-20-jetix-
  architecture-final-DRAFT.md` — single source of truth для Stage 4
  (regenerated from v0.5 commit 110413a).

### 11.2 Source materials

- **v2 synthesis:** `raw/research/architecture-synthesis-v2-final.md`
  (1621 строка) — Stage 3 baseline.
- **v1 synthesis:** `raw/research/architecture-implementation-
  synthesis-2026-04-19.md` (1592 строки) — historical reference.
- **4 reviewer reports:** `raw/research/stage2-review/*` (critic /
  simplifier / megacorp / levenchuk).
- **9 deep-research waves:** `raw/research/*-deep-research-*.md` +
  `hybrid-framework-synthesis-2026-04-18.md`.
- **Левенчук deep research:** `raw/research/levenchuk-for-ai-deep-
  research-2026-04-19.md` + `levenchuk-deep-research-2026-04-18.md`.
- **FPF-Spec первоисточник (Stage 3.6 vendor):**
  `raw/external/ailev-FPF/FPF-Spec.md` (62K строк, commit 0a22129)
- **FPF Attribution:** `raw/external/ailev-FPF/ATTRIBUTION.md`
- **FPF KB compilation:** `raw/research/levenchuk-fpf-knowledge-base-
  2026-04-20.md` (commit 3cb5f81)
- **FPF Gap Analysis:** `raw/research/fpf-gap-analysis-2026-04-20.md`
  (2486 строк, commit 74cf858)
- **5 Perplexity researches:** `raw/research/levenchuk-fpf-research-
  2026-04-20/R-{A,B,C,D,E}.md`

### 11.3 Future artifacts (Stage 4 writing targets)

- **D1 JETIX-ARCHITECTURE-FINAL** — 15-20 pages; 8 sections; Post-
  Chunk 8: Nested Holonic Structure terminology; directions с C.18/
  C.19; Bridges + CL.
- **D2 JETIX-FOLDER-STRUCTURE** — 15 Phase 1 folders detailed + Life-
  OS/shared layouts + deferred triggers + per-direction ee-log/nqd/
  kill-chr.
- **D3 JETIX-ROLE-MANIFESTS** — 18 full-depth 5-block role.md +
  executor-bindings с agency-profile + F.6 cycle + agent_onboarding +
  compute-contract (~35-45h).
- **D4 JETIX-VS-LIFE-OS** — separation principle; Triple-AND Phase 2a
  trigger (MHT-1); Phase 3 physical (MHT-4); SOPS 1 key; grey zone
  sanitization.
- **D5 JETIX-KNOWLEDGE-ARCHITECTURE** — 3-layer model; 8 alpha state
  machines; 25K exocortex hard reservation; manual writeback; latency-
  based GraphRAG trigger; ZUGFeRD Q3 2026; **A.14 typed mereology
  edges** (Rec-05); **UTS central reference** (Gap 4).
- **D6 JETIX-FPF** (renamed from FPF-Lite per OQ-01 B) — Core 20-30
  pages + **`wiki/foundations/fpf-tooling.md`** companion 10-20 pages
  (OQ-07 C soft split); 13+ sections; 17 trans-disciplines; advanced
  mereology A.14; holons (Nested Holonic Structure); category theory;
  constructor theory; 3-pass writing; + separate `wiki/foundations/
  jetix-creation-graph.md` (with A.14 typed edges), `shsm-primitives.
  md`, `holon-hierarchy.md`.
- **D7 JETIX-CAREER-LEVELS** — dual system J0-JX reference + Phase 1
  J-Auto/J-Approve/J-Strategic; AI promotion external-review + Ruslan
  sign-off + **A.18 CSLC formal** (OQ-11); crazy-agent J-Approve
  special; life-coach migrated out; FPF-Steward separation trigger;
  MHT phase transitions reference.
- **D8 docs/INSTRUCTIONS** — 7+10-14 rollout detailed + 4 rituals
  (B.4 Evolution Loop framed) + tool stack + cost model + triggers;
  plan-as-tracker primary.

### 11.4 Supplementary artifacts (Phase 1 — complete list Post-Chunk 8)

**Core governance:**
- `CONSTITUTION.md` (§11 Service Continuity — Day 12 draft с TBD
  trustee placeholder).
- `ops/` stack (Day 13): hit-by-bus, business-continuity, incident-
  playbook, disaster-recovery, gdpr-art-33.

**Policy documents (expanded per Chunk 8):**
- `decisions/policy/ai-agent-decision-authority.md`
- `decisions/policy/eu-ai-act.md`
- `decisions/policy/ecosystem-strategy.md` (placeholder)
- `decisions/policy/compensation.md`
- `decisions/policy/sku-catalog.md`
- **`decisions/policy/boundary-discipline.md`** (NEW Gap 1)
- **`decisions/policy/trust-tagging.md`** (NEW Gap 2)
- **`decisions/policy/sku-pricing-chr.yaml`** (NEW Gap 3)
- **`decisions/policy/agent-promotion-chr.yaml`** (NEW Gap 3)
- **`decisions/policy/characteristic-space-conventions.md`** (NEW Gap 3)
- **`decisions/policy/mereology-edge-types.md`** (NEW Rec-05)
- **`decisions/policy/phase-transitions-mht.md`** (NEW Rec-06)
- **`decisions/policy/bias-audit-cycle.md`** (NEW Rec-03)
- **`decisions/policy/mechanism-introduction.md`** (NEW Rec-20)
- **`decisions/policy/multi-method-dispatcher.md`** (NEW Rec-21)

**Templates (expanded per Chunk 8):**
- `decisions/templates/client-dpa-template.md` (с L/A/D/E structure)
- `decisions/templates/invoice.yaml`
- `decisions/templates/contract.md` (с L/A/D/E structure)
- `decisions/templates/proposal.md` (с L/A/D/E structure)
- **`decisions/templates/jetix-viewpoint-bundle.yaml`** (NEW Gap 5)
- **`decisions/templates/audit-canonical-template.md`** (NEW Gap 5)
- **`decisions/templates/views/`** (NEW Gap 5 — 5 files: executive /
  technical / governance / regulatory / internal-learning)
- **`decisions/templates/client-intake-problem-chr.yaml`** (NEW Rec-16)
- **`decisions/templates/kill-chr-template.yaml`** (NEW Gap 3)
- **`decisions/templates/mht-template.yaml`** (NEW Rec-06)
- **`decisions/templates/bias-audit/`** (NEW Rec-03 — 3 files:
  ba-0-kickoff / ba-1-scan / ba-3-closure)

**Wiki foundations (expanded per Chunk 8):**
- `wiki/foundations/jetix-creation-graph.md` (with A.14 typed edges
  retrofit)
- `wiki/foundations/shsm-primitives.md`
- `wiki/foundations/holon-hierarchy.md` (renamed к Nested Holonic
  Structure section in D6)
- **`wiki/foundations/jetix-uts.md`** (NEW Gap 4)
- **`wiki/foundations/fpf-tooling.md`** (NEW Rec-13)
- **`wiki/foundations/jetix-innovations.md`** (NEW Chunk 8 Section 6)

**Backlog:**
- `decisions/backlog/trademark-jetix-formal-resolution.md`
- `decisions/backlog/fpf-publishing-review.md`

**Governance:**
- `governance/advisory-board/members.yaml` (Anton/Vladislav/Rodion)
- `governance/trustee-designations.md` (TBD)
- `governance/beirat/` (Phase 2a)
- `governance/aufsichtsrat/` (Phase 3)

**FPF Stewardship:**
- `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` (first Q2
  2026 per Rec-22)

**Per-direction (per Rec-07):**
- `directions/<slug>/ee-log.yaml`
- `directions/<slug>/nqd-distinctions.yaml`
- `directions/<slug>/kill-chr.yaml`

---

## Section 12 — Open items for Ruslan review (Carry forward + new)

Документ — draft. Items которые могут потребовать clarify'я в Stage 4.5
после D1-D8 written.

### 12.1 Carry forward from v0.5

1. **Trustee identity** — Day 13 placeholder TBD. Нужно ли Phase 1
   proxy (Steuerberater? lawyer?) пока identity ищется, или пустой TBD
   достаточен до first client contract? MC4 original Ruslan decision:
   "это будет потом, это будет тоже не Антон". Implicit hard deadline:
   до first client contract signed.

2. **Per-direction compute allocation benchmarks** — Item 9 cost model
   breakdown ai-consulting ~70-80% / hypotheses 15-20% / meta 10-15%
   — revisit после first month actual data (Day 30+).

3. **Auto-translation hook (5-ый)** — Day 10 timing (parallel к golden
   dataset). Если Opus 4.7 translation quality для RU→EN wiki concepts
   не достаточно — fallback к manual EN summary для critical concepts;
   trigger decision на Day 10 после QA passage.

### 12.2 New post-Chunk 8

4. **UTS row completion (30-50 target)** — may refine to 25 or 60 based
   on D6 JETIX-FPF concurrent writing experience. FPF-Steward Q2 2026
   audit re-evaluates (Rec-22).

5. **First CHR space refinement (SKU pricing)** — may need iteration
   after first client negotiation. Gate: first Audit SKU close. If
   SKU pricing CHR poorly predicts outcome → revisit scale weights.

6. **BA-2 Panel Review activation** — Phase 2a trigger (Beirat Ethics
   advisor). Timing uncertain — depends on first client с ethics-
   sensitive audit AND Beirat formation. Placeholder в
   `decisions/policy/bias-audit-cycle.md`.

7. **FPF upstream sync first occurrence** — first semi-annual reminder
   Q2 close 2026 (or Q4 close if Q2 skipped). If FPF upstream delta
   substantive → 2-4h re-vendor work. If no delta → just defer.

8. **Viewpoint Bundle first pilot delivery** — Müller GmbH audit (or
   first actual Audit SKU client). Real-world validation of 5
   viewpoints + correspondences table. Feedback loop: may reduce к
   3-4 viewpoints if audience overlap too high, or expand к 6th
   viewpoint (e.g., specialist bundle).

9. **F-G-R retrofit existing ADRs** — 10-15 existing ADRs retrofit
   Day 15-17 Post-Chunk 8 extension. If retrofit burden >5h, collapse
   scope к Phase 1 new ADRs only; existing ADRs retrofit Phase 2a.

---

**END OF D9 DRAFT v0.6**

Stage 4 unblocked с enriched single source of truth. D1-D8 writing
proceeds using этот документ как authoritative input. D6 JETIX-FPF —
first priority (Core 20-30 pages + Tooling companion 10-20 pages +
UTS concurrent). Stage 4.5 finalization: state `draft` → `committed`,
rename `-DRAFT.md` → `.md`.
