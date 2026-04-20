---
id: JETIX-FPF
title: Jetix First Principles Framework — Constitutional Document
subtitle: Jetix-specific adaptation of First Principles Framework (FPF) by Anatoly Levenchuk
date: 2026-04-20
version: v1.0
state: draft
based-on:
  - FPF-Spec.md (Anatoly Levenchuk, March 2026 version, raw/external/ailev-FPF/)
  - Knowledge Base compilation (raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md)
  - ADR Chunks 1-8 approved (decisions/2026-04-19-architecture-v2-approval.md)
  - D9 Draft v0.6 (decisions/2026-04-20-jetix-architecture-final-DRAFT.md)
  - Gap Analysis 60+ decisions (decisions/gap-analysis-review-decisions-2026-04-20.md)
  - 5 Perplexity researches (raw/research/levenchuk-fpf-research-2026-04-20/)
attribution: >
  JETIX-FPF — Jetix-specific adaptation of First Principles Framework (FPF)
  by Anatoly Levenchuk (https://github.com/ailev/FPF). Upstream repo has
  no formal license; citation explicitly requested and provided.
  Internal Jetix use с adaptation. No contribute-back (per OQ-09 A hard stance).
lang: [ru, en]
scope: internal-only (per OT5 + OQ-09 A)
status: draft (unblocks Stage 4 D1/D2/D3/D4/D5/D7/D8 writing)
formality: F2
reliability: R-medium
claim-scope: jetix/methodology/constitutional
---

# JETIX-FPF — Jetix First Principles Framework (Constitutional Document v1.0)

> *Максимальная глубина + качество, на 100%. Никаких compromises. Всё что
> применимо из FPF — внедряем. Стратегический курс как с 11 overrides —
> +Левенчук direction.* — Ruslan, 2026-04-20

---

## Preamble — Why this document exists

JETIX-FPF — конституционный документ Jetix OS. Он описывает **онтологический
каркас** в котором оперирует каждая роль, агент, альфа, direction, client-
relationship и management ritual компании. Источник первичный — **First
Principles Framework (FPF)** Анатолия Левенчука
([github.com/ailev/FPF](https://github.com/ailev/FPF)), март 2026, 62,202
строки pattern language'а. Jetix-адаптация **"JETIX-FPF"** — специфическая
для нашего business-context и AI-native реальности, но с максимальной
fidelity Левенчуковской онтологии.

### Role в архитектуре

D6 — **primary reference** для всех 18 role-manifests. Агенты загружают
полный текст D6 в system.md (OT5 Scenario A — full-text везде). D6 —
основа для D1 (Architecture Final), D3 (Role Manifests), D5 (Knowledge
Architecture), D7 (Career Levels), D8 (Instructions). **Это sacred text
Jetix methodology.**

### Scope stance

**Internal-only hard** (per OT5 + OQ-09 A). Ruslan explicit 2026-04-20:
> "всё держим, ничего никуда не отправляем, нигде не публикуем."

Semi-annual FPF upstream sync reminder (OQ-10 C modified) — Q2 close и Q4
close FPF-Steward flags "upstream sync review due"; Ruslan manual decision.

### What reader will find here

14 sections. ~40-50 pages. Constitutional depth. Максимум Левенчука.
Full 8 true alphas, Nested Holonic Structure (A.1 + A.14), Boundary
Discipline (A.6.*), Trust & Assurance (B.3 F-G-R), Characteristic Spaces
(A.17-21), UTS (F.17), Multi-View Publication (E.17), Eleven Pillars
(E.2), Four Guard-Rails (E.5), plus Jetix-specific innovations (Portfolio-
of-Directions, FPF-Steward sub-role, 4-tier Resource Accounting, Full-FPF-
Permeation).

### What reader will NOT find here

- **Tooling specifics** (YAML schemas, git commit conventions, CLI flags).
  Уходят в companion: `wiki/foundations/fpf-tooling.md` (per Rec-13 + OQ-07
  C soft split; E.5.1 DevOps Lexical Firewall + E.5.3 Unidirectional
  Dependency).
- **Curriculum / pedagogical expansion**. Уходят в отдельные foundations
  artifacts: `shsm-primitives.md`, `trans-disciplines.md`, `holon-
  hierarchy.md`, `jetix-creation-graph.md`.
- **Implementation roadmap**. Уходит в D8 (Instructions).

---

## Section 1 — Target System (Jetix as holon)

### 1.1 Jetix как holon

**Jetix** — AI-native mega-corporation в состоянии `activated` (в терминах
state machine 8-й alpha Direction), операционно управляемая solo founder'ом
(Ruslan, Berlin) в кооперации с array из 11 Claude-агентов. Primary market:
DACH Mittelstand. Secondary: US + русскоязычные клиенты через unified
funnel (Stripe + Wise externally). Legal trajectory: Freiberufler (Phase
1) → UG (Phase 2a) → GmbH (Phase 2b+) → Holdings (Phase 2c+).

**Jetix — это holon** в смысле FPF [**A.1 Holonic Foundation**, FPF-Spec
L.1017]. Три-tier root ontology FPF:

```
U.Entity          — primitive of distinction (anything individuable)
    ↓
U.Holon ⊑ Entity  — unit of composition (whole-and-part simultaneously)
    ↓
U.System ⊑ Holon  — operational, physical (Sys-CAL)
U.Episteme ⊑ Holon — knowledge holon (KD-CAL, passive)
```

Jetix одновременно:
- **U.System** — оперирует в DACH Mittelstand market, генерирует revenue,
  имеет физическое воплощение (git-repo, infrastructure, клиенты).
- **U.Episteme** — методологический holon (wiki/, все role-manifests, JETIX-
  FPF конституция, UTS, все ADRs).

Обе одновременно. Jetix-as-System генерирует Jetix-as-Episteme как work
product через **writing-as-thinking** primitive (Левенчук, *Системное
мышление 2024* т.1) — каждый commit = акт strategic reasoning, externalized
в exocortex.

### 1.2 Well-formedness (A.1 WF-invariants)

FPF A.1 задаёт три well-formedness constraints на holons:

- **WF-A1-1:** У holon exactly one U.Boundary.
  - Jetix boundary = границы `~/jetix-os/jetix/` papka + legal entity
    Freiberufler Ruslan → UG/GmbH trajectory + membership в DACH
    institutional networks (IHK, VDMA etc).
- **WF-A1-2:** Γ (universal aggregation operator, B.1) defined ONLY on
  sets of U.Holon.
  - Jetix aggregation (revenue Γ_sys, knowledge Γ_epist, method Γ_method)
    всегда over well-typed holons, не raw entities.
- **WF-A1-3:** Γ-application scoped to context + temporal scope.
  - Quarterly attention-theme Γ_method scoped к `decisions/quarterly/`
    bounded context; monthly revenue Γ_sys scoped к `finance/resource-
    ledger.yaml` + `T^R` temporal tag.

### 1.3 Jetix boundary kinds

FPF A.1 определяет три boundary kinds:
- **Open** — matter + energy + info crossing.
- **Closed** — energy + info, no matter.
- **Permeable** — filtered subset.

Jetix boundary **permeable** — фильтрованно пропускает:
- Inbound: client contracts (L layer), research-sources (wiki/sources/),
  advisory input (governance/advisory-board/), compute (Claude API).
- Outbound: deliverables (Audit SKU с Multi-View Viewpoint Bundle E.17 —
  per Gap 5), content items (newsletter, LinkedIn), tax/legal filings
  (finance/, ops/gdpr-art-33.md).

**Inside/Outside test** (FPF A.1, 3 steps) применяется при каждом Resource
allocation:
1. Dependency — removing E breaks core invariant of Jetix?
2. Interaction — E participates causal loops within Jetix's boundary?
3. Emergence — E contributes to novel collective property?

Fail all → outside. Пример: **life-coach** agent fails all 3 tests
relative to Jetix → migrated к Life-OS (per Chunk 6 Area 7 decision).

### 1.4 Agency rule (A.1 critical)

FPF A.1 normative: **behavioral roles (including TransformerRole) attach
ONLY к U.System (bearer). U.Episteme is PASSIVE content.** Любое изменение
episteme = external system acting across boundary.

Для Jetix это означает:
- Wiki/foundations/jetix-uts.md (episteme) — passive. Changes come от
  внешних actors (Ruslan + FPF-Steward agent).
- Role-manifests (episteme) — passive reference. Operational execution
  выполняется U.System bearers (Ruslan executor multi-bound к 5 sub-
  roles + 11 Claude-agents each filling defined role).

Это обосновывает **P2 — Role ≠ Executor strict separation** (см. Section 5).

### 1.5 L0-L7 7-layer architecture — Reference vs Operational split

Per ADR Chunk 1 + Area 1 D1 decision — Jetix supports 7-layer reference
architecture; Phase 1 materializes 4 layers.

**Reference Architecture (L0-L7, design-time commitment):**

| Layer | Name | Role |
|-------|------|------|
| L0 | Executive Core | Strategic management, decision authority |
| L1 | Foundation | Legal entity, compliance, ops, governance |
| L2 | Cognitive | JETIX-FPF ontology discipline, wiki, UTS |
| L3 | Customer Relations | CRM, sales, customer success, community |
| L4 | Revenue | Products, deals, invoices, directions operational |
| L5 | Alliance / Community / Membrane | Ecosystem gravity |
| L6 | Research Engine | Hypothesis portfolio, experiments, insights |
| L7 | Holdings / Federation | Multi-entity supersystem |

**Operational Architecture Phase 1 MVA (4 layers materialized):**

- **L0** Executive Core — 5 atomic Ruslan sub-ролей (strategy-lead /
  framing-lead / sales-closer / acceptance-authority / external-relations)
  + `executors/ruslan.yaml` multi-role-binding.
- **L1** Foundation — partial: entity-stub `entities/jetix-gmbh/`; DPO
  external-mode; advisory-board informal; ops artifacts Day 13.
- **L2** Cognitive as discipline (не папка) — JETIX-FPF full-text loaded
  в каждый agent system.md (OT5 Scenario A, full 7-10K tokens); wiki/ с
  9 entity types; alphas/ с 8 state machines; creation-graph с A.14
  typed edges; UTS central (`wiki/foundations/jetix-uts.md`); bias-audit
  cycle.
- **L4** Revenue — `directions/_active/ai-consulting-dach/` operational;
  SKU в catalog; invoice/contract templates с Boundary Discipline L/A/D/E;
  Stripe configured; Multi-View Viewpoint Bundle mandatory для Audit SKU.

**L3, L5, L6, L7 — Reference только**, materialization triggered (Phase
2a, 2b, 2c, 3; см. Section 14 MHT integration).

### 1.6 Jetix как part-of Life-OS supersystem (lightweight mereology)

Life-OS — корневая holonic система (Ruslan's personal life operating
system). Jetix вложен как supersystem-contained namespace: conceptually
`life-os/projects/jetix/`. Physical layout Phase 1 — parallel mount:
`~/jetix-os/life-os/` + `~/jetix-os/jetix/` — для clean separation в git
+ hook enforcement (asymmetric reference rule: Jetix files never reference
Life-OS paths; Life-OS may reference Jetix).

**Phase evolution:**
- Phase 1 Day 1 — folder-level separation, parallel structure.
- Phase 2a (Triple-AND trigger: €20K MRR × 3mo + >40% L1/L2 time + ≥1 DPA
  client) — `git filter-repo --path life-os/` extraction в отдельный repo.
  Это **MHT-1** (см. Section 7).
- Phase 3 — different servers/clouds.

### 1.7 Nested Holonic Structure (OQ-06 B canonical)

Per OQ-06 B (Anglicize per Левенчук direction), Jetix uses **Nested Holonic
Structure** (FPF **A.1 Holonic Foundation** L.1017 + **A.14 Advanced
Mereology** L.17478 canonical). Term "Model D Nested Hierarchy" retired as
primary; may appear только legacy footnote где historically referenced в
v1/v2 synthesis documents.

**Nested structure Jetix:**

```
Life-OS (супер-супер-холон)
    ↓ ComponentOf (A.14)
Jetix-OS (супер-холон)
    ↓ ComponentOf
[Jetix-Sales-Function | Jetix-Revenue-Engine | Jetix-Delivery-Function |
 Jetix-Ecosystem-Phase-3] (Level 3 Creation Graph supersystems)
    ↓ creates + ComponentOf
[5 Ruslan sub-roles | 11 agent roles | methodologies | processes]
(Level 2 Creation Graph creation systems)
    ↓ creates + PhaseOf (during lifecycle)
[8 true alphas | 8 directions | 2 Phase 2a stubs]
(Level 1 Creation Graph target systems)
```

Каждый уровень — holon в смысле A.1 (whole-and-part simultaneously,
Janus-face per Koestler 1967). Recursive без upper bound: Life-OS part of
Ruslan's life part of Berlin's economy part of DACH supersystem part of EU
Union part of humanity part of biosphere... FPF A.1 позволяет recursion;
Jetix pragmatically materializes 3 levels через creation-graph + implies
higher levels reference-only.

### 1.8 Cross-refs

- **FPF A.1 Holonic Foundation** (L.1017) — three-tier root ontology
- **FPF A.1.1 U.BoundedContext** (L.1202) — locality discipline
- **FPF A.14 Advanced Mereology** (L.17478) — typed edges
- **D1** Section "Reference Architecture" — 7-layer detail
- **D4** Section "Life-OS ≠ Jetix separation" — asymmetric reference + MHT-1
- `wiki/foundations/holon-hierarchy.md` — full recursive structure (Phase 1
  post-D6)
- `wiki/foundations/jetix-creation-graph.md` — 3-level graph с A.14 typed
  edges

---

## Section 2 — Stakeholders

Stakeholders = U.RoleAssignment instances (FPF **A.2.1**, per Role Taxonomy
L.~1500-3000) — holders occupying roles в bounded contexts с committed
obligations.

### 2.1 Ruslan (primary executor, 5 atomic sub-roles)

**Executor:** `executors/ruslan.yaml` с `multi-role-binding: true` flag
(hybrid founder-mode, per P5 Chunk 1 + Левенчук §1.4 #1).

**5 atomic sub-roles Phase 1** (per P5 + D3):

| Role | Context | Responsibilities |
|------|---------|------------------|
| **strategy-lead** | L0 Executive Core | Портфолио of directions curation, quarterly attention-theme setting, kill/activate decisions (J-Strategic), B.4 Canonical Evolution Loop coordination |
| **framing-lead** | L0 + L2 | Client value-proposition framing, methodology articulation, writing-as-thinking rituals (quarterly letters, strategic write-ups) |
| **sales-closer** | L3 + L4 | Pre-contract negotiation, DPA walkthrough, "yes" authority at signing; A.6.B L/A/D/E routing discipline applied |
| **acceptance-authority** | L4 | Delivery quality sign-off, bias-audit BA-3 closure authority, F-G-R tagging enforcement |
| **external-relations** | L5 + L6 | Advisory board conversations (Anton/Vladislav/Rodion), DACH institutional outreach (IHK/VDMA), media (Rodion YouTube) |

**Agency profile** (per Rec-08 A.13:4.3 Agency-CHR fallback): Ruslan
default agency 1.0 (founder full-stack); agents default 0.4 with override
per decision class.

**Left-hand rule** (Jetix custom, not FPF canonical): При conflict между
sub-roles, **strategy-lead** имеет meta-authority (analogous к Левенчук's
meta-method стратегирование selecting which sub-method dominates).

### 2.2 11 Claude agents (L2 Cognitive + L0 support)

Per ADR Chunk 6 Area 3 + D3:

| # | Agent | Dept | Model | J-level |
|---|-------|------|-------|---------|
| 1 | manager | MGMT | Sonnet 4.6 | J-Approve |
| 2 | personal-assistant | OPS | Haiku 4.5 | J-Auto |
| 3 | system-admin | OPS | Haiku 4.5 | J-Auto |
| 4 | sales-lead | Sales | Sonnet 4.6 | J-Approve |
| 5 | sales-research | Sales | Haiku 4.5 | J-Auto |
| 6 | sales-outreach | Sales | Haiku 4.5 | J-Auto |
| 7 | inbox-processor | Brain | Haiku 4.5 | J-Auto |
| 8 | crazy-agent | Meta | Sonnet 4.6 | J-Approve (special brainstorm mode) |
| 9 | knowledge-synth | Brain | Sonnet 4.6 | J-Approve |
| 10 | strategy-support-analyst | MGMT | Opus 4.6 | J-Approve (NOT J-Strategic per Левенчук §1.4 — agents не стратегируют) |
| 11 | meta-agent (+ FPF-Steward sub-role R12) | Meta | Sonnet 4.6 | J-Approve |

**Role ≠ Executor strict** (P2) — каждый agent — `executor-binding.yaml`
bound к defined role.md. Holder (agent instance) может change (Claude
Haiku 4.5 → Haiku 5.x upgrade) — role remains stable. **Agency-CHR
fallback** (Rec-08 A.13:4.3) per-binding.

### 2.3 Future human hires (Phase 2a+)

Stub role-manifests Phase 1 (per MC1 + Area 3):

- `dpo` (Data Protection Officer, external-mode Phase 1; activated Phase
  2a when ≥1 client requests GDPR DPA)
- `customer-success` (J2 Phase 2a activation)

Phase 2b additions triggered:
- Chief of Staff (team 5-20)
- FPF-Steward as separate role (30+ agents OR 1+ human meta-hire OR
  quarterly audit burden >4h)

Phase 2c additions:
- CFO fractional (at €1M ARR)
- Finance head (€10M)

All Future hires — role-manifest exists Phase 1, executor-binding.yaml
activated at trigger.

### 2.4 Advisory board (Phase 1 informal, Phase 3 first-class)

`governance/advisory-board/members.yaml`:

| Name | Context | Relationship |
|------|---------|--------------|
| **Anton** | Mentor — systems thinking, psychology | Informal Phase 1; Beirat Phase 2a formalization candidate |
| **Vladislav** | Economist — value-based pricing | Informal Phase 1 |
| **Rodion** | YouTuber — AI topics, DACH reach | Informal Phase 1 |

Future Phase 2a Beirat (4-6 members) + Phase 3 Aufsichtsrat (formal
supervisory board).

**Trustee**: TBD, **NOT Anton** (per Ruslan explicit override Chunk 1 P5).
Placeholder `governance/trustee-designations.md`. Hard deadline для
identification: before first client contract signed.

### 2.5 Clients (DACH primary + US + RU secondary, unified funnel)

Per P6 + Chunk 1 modification:

- **Primary (DACH Mittelstand)**: AI-consulting-dach direction ICP
  (Industrial / SaaS / Professional Services; €10M-€500M revenue; C-level
  or VP-level decision-maker; existing digital transformation budget).
- **Secondary (US)**: remote DACH advisors, DACH expats в US, high-value
  solo entrepreneurs.
- **Secondary (RU)**: русскоязычные клиенты через unified funnel (Stripe/
  Wise external currency handling).

**Client frontmatter** (per clients/companies/<slug>.md):
```yaml
jurisdiction: de | at | ch | us | ru | other
client_language: de | en | ru
direction: ai-consulting-dach  # primary direction binding
alpha_ref: alphas/client/instances/<slug>.yaml
crm_tier: mittelstand | sme | enterprise | regulated
```

Relationship alphas — **Client** + **Deal** + **Project** (см. Section 6).

### 2.6 Ecosystem Phase 3 (11 categories detailed)

Per P7 + Chunk 1 Ecosystem resources elaboration — Phase 3 first-class
resource, infrastructure prep Phase 1:

| Category | Examples | Phase 1 status |
|----------|----------|----------------|
| **Advisory relationships** | Anton, Vladislav, Rodion + future Beirat | ✅ informal active |
| **Community members** | Alliance members (L5 Membrane), newsletter list | 🟡 Phase 2a trigger |
| **Partnerships** | Cross-referral, co-marketing, JVs, tech integrations | 🟡 Phase 2a expand |
| **Brand equity / reputation** | Testimonials, case studies, NPS, inbound ratio | 🟡 Phase 2a ++ |
| **DACH institutional networks** | IHK, VDMA, BDI, BITKOM | 🟡 Phase 2 clients dают access |
| **Alumni / reference network** | Former client references, intros | 🟡 Phase 2a (5+ clients delivered) |
| **Media / content relationships** | Rodion YouTube, journalists, podcasts, LinkedIn | 🟡 Phase 2+ |
| **Talent network** | Fractional experts, future hire candidates, OSS contribs | 🟡 Phase 2b |
| **Capital relationships** | Angels, VCs, banks, Steuerberater, KfW/EXIST grants | 🟡 Phase 2b |
| **Academic / research** | TU Berlin, TU München, Fraunhofer | 🟡 Phase 3 if relevant |
| **Regulatory / government** | BaFin, Bundeskartellamt, EU AI Act regulators, Berlin Senat | 🟡 Phase 3 |

Phase 1 artifact: `decisions/policy/ecosystem-strategy.md` (placeholder).
Phase 3 activation trigger: mega-corp stage (revenue €50M+).

### 2.7 Cross-refs

- **FPF A.2 Role Taxonomy** (+ A.2.1 U.RoleAssignment, A.2.5 U.RoleStateGraph)
- **FPF A.13 Agential Role & Agency Spectrum** (+ A.13:4.3 Agency-CHR)
- **D3** — 18 full-depth role-manifests
- `governance/advisory-board/members.yaml`

---

## Section 3 — Creation Graph (full 3-level mereological, MC3 override)

Per MC3 Ruslan override (Chunk 2): **Full 3-level creation graph Phase 1,
no simplifications.** Per Rec-05 (Chunk 8): **A.14 typed mereology edges**
retrofit. Separate artifact: `wiki/foundations/jetix-creation-graph.md`.

### 3.1 Conceptual frame

**Creation Graph** (граф создания, Левенчук *Методология 2025* "по мотивам
OMG Essence 2.0:2024") = ориентированный мереологический граф; узлы =
системы, рёбра по отношению "кто создаёт кого / что / где функционирует".
Одновременно показывает:

1. **Target systems** (Level 1) — что мы создаём (для клиента + для
   себя как organization).
2. **Creation systems** (Level 2) — кто создаёт target'ы (роли, методологии,
   processes, agents).
3. **Supersystems** (Level 3) — где функционируют target systems (Jetix-
   as-whole + Jetix subordinate functions + external market ecosystem).

**FPF correlation** ✅: **A.14 Advanced Mereology** (L.17478) supplies
typed edges; **B.1 Γ Universal Algebra** (L.~26000) aggregates; **A.1
Holonic Foundation** (L.1017) grounds holons.

### 3.2 Level 1 — Target systems

**Jetix target systems — 8 + context items:**

| # | Target system | Alpha? | Role binding |
|---|---------------|--------|--------------|
| 1 | **Client-relationship** | ✅ Client (alpha 1) | sales-closer enacts; sales-lead shepherds |
| 2 | **Deal-opportunity** | ✅ Deal (alpha 3) | sales-lead + sales-closer |
| 3 | **Project (delivered)** | ✅ Project (alpha 2) | acceptance-authority + knowledge-synth |
| 4 | **Product-SKU** | ❌ Entity (catalog/) | strategy-lead authoring; framing-lead pricing CHR |
| 5 | **Content-item** | ✅ Content Item (alpha 4) | framing-lead + sales-outreach |
| 6 | **Member-engagement** | ✅ Member (alpha 6) | framing-lead + external-relations |
| 7 | **Hypothesis (validated)** | ✅ Hypothesis (alpha 5) | strategy-support-analyst + knowledge-synth |
| 8 | **Way-of-working (refined)** | ✅ Way of Working (alpha 7) | meta-agent (+ FPF-Steward) curates |
| 9 | **Direction (portfolio bet)** | ✅ Direction (alpha 8, 8-я) | strategy-lead (open hypothesis J-Auto; activate/archive J-Strategic) |

Items 1-3, 5-9 — 7 из 8 alphas (Direction = 8-я, Portfolio-of-Directions
innovation). Item 4 SKU reclassified as entity per Chunk 2 MC3.

### 3.3 Level 2 — Creation systems (кто создаёт)

**5 Ruslan atomic sub-roles** (см. Section 2.1):
- strategy-lead, framing-lead, sales-closer, acceptance-authority,
  external-relations.

**11 agent roles** (см. Section 2.2):
- manager, personal-assistant, system-admin, sales-lead, sales-research,
  sales-outreach, inbox-processor, crazy-agent, knowledge-synth,
  strategy-support-analyst, meta-agent (+FPF-Steward sub-role).

**2 Phase 2a stubs:**
- dpo (external-mode), customer-success (J2).

**Methodologies (U.MethodDescription per A.3.2):**
- FPF-Lite → JETIX-FPF adaptation (this document).
- MECE qualification для sales.
- Shape Up для project planning (Basecamp-inspired).
- SEMAT Essence → ШСМ адаптация (legacy bridge).
- Bias-Audit Cycle (D.5 adoption).
- Multi-View Publication discipline (E.17 adoption).
- Method Quartet Harmonisation (F.11 adoption).

**Processes (U.Method runtime):**
- Weekly close ritual.
- Monthly P&L + OKR ritual.
- Quarterly strategy + letter + meta-review ritual.
- Trigger-driven strategizing event (не scheduled).
- Agent onboarding F.6 6-step cycle (per Rec-15).

### 3.4 Level 3 — Supersystems (где функционируют)

**Internal supersystems** (within Jetix holon boundary):

| Supersystem | Purpose | Materialization Phase |
|-------------|---------|-----------------------|
| **Jetix-Sales-Function** | Lead→close pipeline, outreach, CRM | Phase 1 Day 1-7 |
| **Jetix-Revenue-Engine** | SKU catalog, pricing, invoicing, cash | Phase 1 Day 5-14 |
| **Jetix-Delivery-Function** | Project scoping, delivery, acceptance, bias-audit | Phase 1 Day 5 + Phase 2a scale |
| **Jetix-Ecosystem (Phase 3)** | Advisory/partnerships/brand/institutional/alumni/media/talent/capital/academic/regulatory (11 categories) | Phase 1 prep → Phase 3 first-class |

**External supersystems** (Jetix operates-in):

- DACH Mittelstand market (primary)
- US professional-services market (secondary)
- Russian-speaking diaspora market (secondary)
- EU regulatory environment (EU AI Act, GDPR, MiCA, DORA)
- Левенчук practitioner community (reference-only; no contribute-back per
  OQ-09 A)
- Anthropic ecosystem (model evolution, pricing, capability changes)
- Life-OS (Ruslan personal namespace; Jetix = part-of Life-OS conceptually)

### 3.5 A.14 typed mereological edges (Rec-05)

Per **FPF A.14 Advanced Mereology** (L.17478), following typed edges
applied в `wiki/foundations/jetix-creation-graph.md`:

**A.14 canonical 6 edges:**

| Edge type | Semantics | Jetix example |
|-----------|-----------|---------------|
| **ComponentOf** | Structural discrete part | `sales-lead` ComponentOf `Jetix-Sales-Function` |
| **ConstituentOf** | Conceptual/logical part (section, lemma, clause) | `jetix-uts.md Row 15 (U.Role)` ConstituentOf `jetix-uts.md` |
| **PortionOf** | Metrical measure-preserving part (μ-additive) | `Q2 2026 compute spend` PortionOf `Jetix annual compute` |
| **PhaseOf** | Temporal part — same carrier across interval | `Müller GmbH relationship (lead-identified state)` PhaseOf `Müller GmbH relationship (lifecycle whole)` |
| **MemberOf** | Collection membership (NOT partOf!) | `Anton` MemberOf `advisory-board collection` |
| **AspectOf** | Facet/perspective of same entity | `Security view of Müller audit` AspectOf `Müller audit canonical artifact` |

**Jetix-introduced 4 (domain-specific, не в A.14 canonical):**

| Edge type | Semantics | Jetix example |
|-----------|-----------|---------------|
| **creates** | Creator system → target (Левенчук creation graph) | `framing-lead role` creates `Audit SKU proposal` |
| **operates-in** | Target system → supersystem | `Jetix` operates-in `DACH Mittelstand market` |
| **methodologically-uses** | Creator → U.MethodDescription | `sales-closer role` methodologically-uses `A.6.B L/A/D/E contract discipline` |
| **constrained-by** | System → constraint | `Jetix` constrained-by `EU AI Act (Aug 2026 High-risk obligations)` |

**Plus Jetix-5th** (implicit, для portfolio model):
- **fills** — direction → ICP slot (`ai-consulting-dach direction` fills
  `DACH Mittelstand ICP`).

**Documentation:** `decisions/policy/mereology-edge-types.md` — when-to-
use-which + anti-patterns. Hook 4 pre-commit check (past-participle + edge
type verification).

**Firewall reminder** (per A.14 normative): Если предложение о "who does
what / how / when" → A.15 (Role-Method-Work Alignment). Если carrier
episteme structure (pages/sections) → A.14 ConstituentOf. Если identity
criteria break during change → MHT (B.2), not PhaseOf.

### 3.6 Creation Graph sample traversal (Müller GmbH prospect)

Scenario: Müller GmbH prospect в ai-consulting-dach direction.

```
[Level 3 Supersystem]
    Jetix-Sales-Function
        ⤷ contains (ComponentOf)
[Level 2 Creation System]
    sales-lead agent (Claude Sonnet 4.6)
        ⤷ creates
[Level 1 Target system]
    Müller GmbH client-relationship (alpha 1, state: qualified)
        ⤷ operates-in
[Level 3 External supersystem]
    DACH Mittelstand market
        ⤷ constrained-by
[Level 3 Regulatory supersystem]
    EU AI Act + GDPR DPA requirements
```

Query "что знаю про Müller" (через `/ask`) traverses:
`clients/companies/muller-gmbh.md` (CRM) →
`wiki/entities/muller-gmbh.md` (knowledge) →
`directions/_active/ai-consulting-dach/pipeline.md` (portfolio) →
`alphas/client/instances/muller-gmbh.yaml` (state machine) →
synthesis с citations.

Edges traversed: sames-as-crm + belongs-to-direction + applies-to + A.14
typed portfolio-specific edges.

### 3.7 Cross-refs

- **FPF A.14 Advanced Mereology** (L.17478) — typed edges canonical
- **FPF A.15 Role-Method-Work Alignment** (L.~17200) — firewall
- **FPF B.1 Γ Universal Algebra** (L.~26000) — aggregation
- **Rec-05** — A.14 typed edges adoption
- `wiki/foundations/jetix-creation-graph.md` — full 3-level graph
- `decisions/policy/mereology-edge-types.md` — edge type guide

---

## Section 4 — Client Principles

Principles governing client-facing interactions. Grounded в FPF **A.6.B
Boundary Norm Square** (per Gap 1 adoption) + **F-G-R Trust & Assurance**
(per Gap 2) + **E.17 Multi-View Publication Kit** (per Gap 5).

### 4.1 CP-1 — Respect (DACH Konsenskultur alignment)

**Statement:** Clients treated as peers в adult discourse. No condescension,
no jargon overload, no premature lock-in. DACH Konsenskultur — decisions
reached through substantive discussion + demonstrated competence, не hard
sell tactics.

**Operational implications:**
- Discovery calls — framing-lead listens 60-70% of time first call.
- Written proposals — DE primary + EN secondary (per OT2 + P6); structured
  per A.6.B L/A/D/E (contracts aren't mixed).
- Pricing CHR — defensible measurable scales (per Gap 3 SKU pricing CHR);
  никакой magic-quadrant subjectivity.

**FPF grounding:** A.2.1 U.RoleAssignment — explicit contract clauses;
A.6.Q Quality Term Precision (quality terms like "timely" expanded к "within
72h business days per BGB §187").

### 4.2 CP-2 — Honesty (F-G-R tagging visible in deliverables)

**Statement:** All client deliverables carry explicit **F-G-R trust tags**
(per Gap 2). Client видит:
- **F (Formality)** — насколько formal рассуждение: F0 informal notes, F1
  structured analysis, F2 ADR-grade, F3 policy-grade (most client
  deliverables land F2-F3).
- **G (ClaimScope)** — bounded context of claim (e.g., "Müller GmbH internal
  data pipeline 2026 Q2").
- **R (Reliability)** — R-low anecdotal / R-medium multi-source / R-high
  peer-reviewed / R-certified auditor / R-formally-proven.

**Operational implications:**
- No false certainty. If recommendation = R-medium, labeled R-medium.
- No silent scope expansion. If finding applies к ai-consulting-dach but
  not cybersec-dach — explicit.
- Evidence decay tracking (B.3.4) — stale citations flagged after validity
  window expiry.

**FPF grounding:** B.3 Trust & Assurance Calculus (L.28201) + C.2.2
Reliability R (L.31301).

### 4.3 CP-3 — No-surprise discipline

**Statement:** Every client deliverable passes through A.6.B L/A/D/E
structure + Bias-Audit Cycle (BA-0/BA-1/BA-3 Phase 1) + Multi-View
Publication Kit (5 viewpoints для Audit SKU deliveries mandatory per OQ-04
modified).

**L/A/D/E routing mapping:**

| Lane | Content | Example |
|------|---------|---------|
| **L — Laws** | Applicable regulations, grounded в public legal texts | GDPR Art. 22 automated decision-making; EU AI Act Aug 2026 High-risk obligations; HGB §238 Buchführungspflicht; BGB §187 date calculation |
| **A — Admissibility** | Parties' acceptance criteria, formal gates | "Client accepts intermediate milestones within 3 business days"; "Rework bounded to 2 cycles per deliverable" |
| **D — Deontics** | Obligations, permissions, prohibitions | "Jetix obliged to retain project data 6 months post-closure"; "Client permitted to extend engagement at same price within 30 days" |
| **E — Effects** | Work-effects, deliverables, metrics, SLA, outcomes | "Audit deliverable ≥40 pages PDF + Multi-View 5 viewpoints"; "Identified bias count ≥ N per bias taxonomy 5-class"; "SLA: response within 24h business hours" |

**Bias Taxonomy 5-class** (per Rec-03 + D.5):
- REP (representation) — demographic under-representation.
- ALG (algorithmic) — model architecture / training bias.
- VIS (visual) — UI, visualization choices.
- MET (measurement) — metric design, operational definitions.
- LNG (linguistic) — translation, terminology, framing.

**Operational:** Proposal, contract, DPA templates — all три carry full
L/A/D/E Phase 1 (per Day 5-6 rollout).

### 4.4 CP-4 — Multi-View Publication mandatory (Gap 5, OQ-04 modified)

**Statement:** All Audit SKU deliveries — **mandatory multi-view from first
delivery onward** (не pilot-only, per Ruslan override OQ-04). 5 viewpoints:

| # | Viewpoint | Audience | Depth |
|---|-----------|----------|-------|
| 1 | **Executive** | CEO, Aufsichtsrat | 2-3 pages plain + finance |
| 2 | **Technical** | CTO, engineers | 20-40 pages specs + references |
| 3 | **Governance** | Board, risk committee | 3-7 pages governance + legal |
| 4 | **Regulatory** | BfDI, EU AI Act auditors | 3-5 pages pre-mapped EU AI Act / GDPR / DORA |
| 5 | **Internal-learning** | Jetix team | 5-10 pages FPF patterns referenced |

**A.6.3.CR Same-Entity Retextualization** discipline prevents semantic drift
между views. Correspondences table (canonical section → view section) —
automated rendering check, FPF-Steward quarterly audit scope.

**Implementation:** `decisions/templates/jetix-viewpoint-bundle.yaml` + 5
view templates (`decisions/templates/views/`). First pilot: Müller GmbH
audit (or first actual Audit SKU client).

### 4.5 CP-5 — Respect the no-prompt-injection rule

**Statement:** AI-agent outputs к client go through human approval gate
(Art. 22 GDPR defence). Human gate = sales-closer / acceptance-authority /
Ruslan. No purely autonomous client-affecting AI decisions. EU AI Act
risk-proportional Scenario C per OT3.

### 4.6 Cross-refs

- **FPF A.6.B Boundary Norm Square** (L.7097) — L/A/D/E routing canonical
- **FPF A.6.C Contract Unpacking** (L.7741)
- **FPF A.6.Q Quality Term Precision** (L.11326)
- **FPF A.6.3.CR Same-Entity Retextualization** (L.9521)
- **FPF B.3 F-G-R Trust Calculus** (L.28201)
- **FPF D.5 Bias-Audit** (L.39964)
- **FPF E.17 Multi-View Publication** (L.45107)
- `decisions/policy/boundary-discipline.md`
- `decisions/policy/trust-tagging.md`
- `decisions/policy/bias-audit-cycle.md`
- `decisions/templates/jetix-viewpoint-bundle.yaml`

---

## Section 5 — Internal Principles (8 principles + ШСМ 5 primitives)

8 principles governing internal Jetix discipline. Каждый grounded в FPF
pattern + Левенчук primitive.

### 5.1 IP-1 — Role ≠ Executor strict separation (P2 + A.2 Role Taxonomy)

**Statement:** Роль (обязанности, метод, outputs) — archetype. Executor
(agent instance или human holder) — привязка. Never mixed.

**FPF grounding:** **A.2 Role Taxonomy** + **A.2.1 U.RoleAssignment**
(Holder#Role:Context).

**Левенчук grounding:** *Методология 2025* — "Если говоришь роль, то за
ролью скрывается метод. При разговоре о роли прежде всего разбираемся с
методом: что и с чем эти роли делают."

**Operational (D3 implementation):**
- 5-block role.md (identity / ontological / method / production_dependencies
  / evolution) separates WHAT the role is.
- Separate `executor-binding.yaml` says WHO is bound.
- Dynamic role assignment **forbidden** (kroме founder exception: Ruslan
  multi-role-binding).
- **Agency profile** (per Rec-08 A.13:4.3) per-binding — formal 0.0-1.0
  scale + fallback rule.

**Anti-pattern (forbidden):** "Claude Agent #3" as role name (это executor,
не method signature).

### 5.2 IP-2 — Context is king (A.1.1 U.BoundedContext)

**Statement:** Agent reasoning must be context-grounded. Never assume
globally uniform meaning. Same label ("role", "service", "ticket",
"evidence") routinely carries incompatible senses across teams, standards,
eras.

**FPF grounding:** **A.1.1 U.BoundedContext** (L.1202) — "Make meaning
local; make translation explicit."

**Operational:**
- Every concept в JETIX-UTS declares its Context (F.0.1 Source Localisation).
- Cross-context reuse requires **explicit Bridge** (F.9) с CL (Congruence
  Level) and Loss notes. Never silent.
- Wiki frontmatter: `scope: jetix` mandatory (prevents Life-OS bleed).
- Role-manifests: `context:` field explicit.
- UTS rows: SenseCells per Context columns.

**Phase 1 Contexts** (per F.1, ≥3 domain families):
1. JETIX-ops (operational management Phase 1)
2. FPF-canonical (Левенчук ontology)
3. DACH-legal (HGB/BGB/GDPR/EU AI Act)
4. AI-industry (Anthropic, broader LLM ecosystem)
5. ШСМ-Russian (legacy pedagogy reference)

### 5.3 IP-3 — Artifacts over conversations (writing-as-thinking primitive)

**Statement:** Document the output. Conversation ephemeral; artifact
persistent. Agent reasoning externalizes через письменный артефакт, не
stays в chat window.

**FPF grounding:** Implicit throughout FPF — entire FPF-Spec itself is
artifact of writing-as-thinking. Preface explicit: "Thinking Through
Writing: The FPF Discipline of Conceptual Work."

**Левенчук grounding:** *Системное мышление 2024* т.1 — "Системное
мышление происходит путём мышления моделированием и письмом (с текстами
на естественных языках, но с отслеживанием типов объектов и видов
отношений объектов в этих текстах), поэтому внимание не только наводится
на важные предметы, но и удерживается на них всё время проекта: записанное
не так легко забыть в суете."

**Operational:**
- Every Ruslan session ends с commit (daily, weekly, monthly, quarterly
  artifacts).
- Agents output к mailboxes + scratchpads + wiki ingest — никакой
  chat-only ephemeral work.
- Quarterly ritual — founder letter (written, не spoken).
- Trigger-driven strategizing event — structured write-up mandatory.

**Anti-pattern** (Левенчук warning, ailev/1769411):
> «Без внешнего по отношению к LLM контуру обработки текста — никак, LLM
> всегда обманет. Если и сам текст пишет LLM — исчезает 'мышление письмом'
> как когнитивный процесс.»

→ Ruslan primary writer для critical strategic artifacts; agents support,
не substitute.

### 5.4 IP-4 — Meta-agent as immune system (FPF-Steward sub-role)

**Statement:** Ontological integrity defended by dedicated meta-agent sub-
role. Without immune system — concepts bleed between contexts, terms
drift, alpha/entity/work-product distinctions erode.

**FPF grounding:** FPF has no explicit "steward" pattern; Jetix innovation
#4 (per Section 8.6 Gap Analysis innovations). Grounded в **E.2 Eleven
Pillars** (P-1 Cognitive Elegance, P-11 SoTA Alignment) + **E.5 Four
Guard-Rails**.

**Operational (R12 override + Chunk 8 scope expansion):**
- Sub-role section в `agents/meta-agent/system.md`.
- **Quarterly audit scope** (expanded per Chunk 8):
  - Alpha/WP/Entity classification sanity
  - Past-participle convention (automated Hook 4 + manual cross-check)
  - Concept duplication detection
  - Role-manifest structural integrity
  - Direction-concept boundary clarity
  - Frontmatter schema compliance
  - **UTS review** (row additions, Bridges updates, CL re-measurement)
  - **F-G-R compliance** check (ADRs + deliverables)
  - **A.14 edge-type verification**
  - **CHR space integrity** (SKU pricing, direction kill, agent promotion)
  - **Viewpoint Bundle correspondences** check
  - **Semi-annual FPF upstream sync trigger** (Q2/Q4 close)
- **Output:** `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md`.
- **Separation trigger** (FPF-Steward → separate role, Phase 2b):
  30+ agents OR 1+ human meta-hire OR quarterly audit burden >4h.

### 5.5 IP-5 — Explicit alpha state transitions (past-participle, MC6 + Hook 4)

**Statement:** Alpha states — past-participle глаголы. No gerunds, no
present-continuous.

**Левенчук grounding:** *Методология 2025* — "Состояния предмета метода в
альфе даются глаголами в прошедшем времени, эти глаголы соответствуют
применённым составляющих разных методов к какому-то объекту."

**FPF grounding:** **A.2.5 U.RoleStateGraph** (past-tense state names
implicit throughout); **A.4 Temporal Duality** (design vs run stance).

**Operational (MC6 + Hook 4):**

| Неправильно (gerund) | Правильно (past-participle) |
|---------------------|-----------------------------|
| "qualifying" | `qualified` |
| "in qualification" | `qualified` |
| "active" | `activated` |
| "in progress" | `started` |
| "delivering" | `delivered` |

**For Russian** (краткие причастия): "квалифицирован", "активирован",
"начат", "доставлен", "закрыт".

Pre-commit **Hook 4** blocks commits с gerunds в `state.yaml` (52% v1
violations fixed Phase 1 rename).

**Semantic justification:**
- State — fact, not process. Verifiable (checklist for completed event).
- Machine-readable (`IF Client.state == "Qualified" THEN ...`).
- Preserves epistemological precision (fact vs ongoing).

### 5.6 IP-6 — No role left undefined (5-block role.md mandatory)

**Statement:** Every Jetix role has structured 5-block role.md. No "вот
такой-то выполняет...". Ontologically explicit.

**FPF grounding:** **A.2 Role Taxonomy** + **A.15 Role-Method-Work
Alignment** (roles bind к methods bind к work records).

**Operational (D3):**

```yaml
# Block 1 — Identity
role_name: sales-closer
family: sales
context: jetix/l4-revenue
language: [de, en, ru]
version: v1.0

# Block 2 — Ontological positioning
archetypal_kind: U.Role
scope: jetix/sales/dach-mittelstand
fpf_patterns_applied: [A.2.1 U.RoleAssignment, A.6.B L/A/D/E, B.3 F-G-R]
u_type_mapping: U.Role (sales-closer-kind @ ops context)

# Block 3 — Method
primary_method: value-based-pricing-mece-qualification
method_description_ref: wiki/methodologies/mece-sales.md
deliverable_kinds: [Client-in-Negotiated-state, Deal-in-Signed-state]
state_graph_ref: alphas/deal/states.yaml

# Block 4 — Production dependencies
depends_on_roles: [sales-lead, sales-research]
depends_on_artifacts: [decisions/templates/proposal.md, contract.md]
produces_artifacts: [alphas/deal/instances/<slug>.yaml]

# Block 5 — Evolution (seniority-lite)
current_level: J-Approve
autonomous: [draft-proposal, schedule-call, send-DPA]
approve_required: [discount-offer-above-10%, custom-terms]
never: [sign-contract (J-Strategic), accept-brief-without-QTerm-precision]
direction_authority:
  open_hypothesis: n/a
  activate_direction: n/a
  archive_direction: n/a
```

### 5.7 IP-7 — Writing as thinking (Левенчук primitive)

**Statement:** Cognitive process; writing ≠ documentation. Author
"discovers" через act of writing, не pre-composes thoughts.

**Already covered IP-3** — но repeated here as first-class principle per
Chunk 6 Area 6 8-principle list.

**Quality criteria:**
- ✅ Author opens something new during writing.
- ✅ Text contains ontologically typed objects (roles, alphas, methods).
- ✅ Text reveals contradictions not visible pre-writing.
- ❌ Fixes already-known без new understanding.
- ❌ Written "for audience" не для clarification.

**Epistemological grounding:**
- **Peter Naur "Programming as Theory Building" (1985):** "The proper,
  primary aim of programming is not to produce programs, but to have the
  programmers build theories."
- **Clark & Chalmers "Extended Mind" (1998):** Cognitive processes can be
  offloaded на external artifacts. Git-repo = Ruslan's экзокортекс.

### 5.8 IP-8 — Agents as new participants of master class (Левенчук Part 3)

**Statement:** AI-agent onboarding — **полное введение в роль + метод +
контекст**, not just prompt loading. F.6 6-step Role Assignment & Enactment
Cycle + `agent_onboarding` section в executor-binding.yaml.

**FPF grounding:** **F.6 Role Assignment & Enactment Cycle** (Six-Step,
L.50641) — M1 Locate / M2 Stance / M3 Qualify / M4 Bind/Assert / M5 Evidence
/ M6 Conclude.

**Левенчук grounding:** *Методология 2025* — agents как participants в
master class, не tools. "Создатели — это агенты, всё что из методов умеет
делать агент (совокупность мастерства агента) — это личность агента."

**Operational:**
- `executor-binding.yaml` получает **agent_onboarding** section с:
  - `initial_context_pack` (wiki refs, role ref, alpha refs).
  - `warm_up_tasks` (calibration tasks, trivial success criteria).
  - `calibration_checkpoint` (meta-agent reviews output quality).
  - F.6 6-step cycle retrospective (30/90/180-day).
- Full JETIX-FPF text loaded в system.md (per OT5 Scenario A).

### 5.9 Forbidden: dynamic role-switching by agent at task-time

**Statement (negative principle):** Agent cannot dynamically switch role
during task execution. Role assignment happens при task creation (F.6 M4
Bind/Assert), не runtime mid-task.

**Founder exception:** Ruslan multi-role-binding explicit (executors/
ruslan.yaml `multi-role-binding: true` flag). Allowed because founder has
long-term identity + commitment + skin-in-game (Taleb) — preconditions
для true strategizing per Левенчук.

**Rationale (Левенчук, ailev/1795494):**
> «Если наплодить много-много ролей, то в текущих многоагентных архитектурах
> типичный рост расхода токенов в 3-10 раз и идут провалы при handoff
> между рольными агентами.»

→ Role stability > role flexibility (at Phase 1 scale).

### 5.10 ШСМ 5 primitives — full treatment

Per ADR reference — 5 primitives ШСМ foundational для Jetix methodology.
Note: **"5 primitives" is R-B analytical synthesis**, не Левенчук's
published taxonomy (per KB Section 3.1). Each primitive — first-class
concept в specific Левенчук texts. For Jetix they serve as didactic frame.

#### 5.10.1 Роль (Role)

Already covered IP-1 (Section 5.1). FPF correlation ✅ A.2, A.2.1, A.2.5,
A.13.

Formula: **Роль = signature метода × interest к системе × набор мастерства.**

#### 5.10.2 Альфа (Alpha)

**Definition** (Левенчук, *Методология 2025*):
> «Альфа — это предмет метода, который может быть и физическим объектом
> (системой), и абстрактным объектом (описанием). Альфа позволяет
> управлять вниманием создателя в ходе исполнения длинных цепочек операций.»

**FPF correlation ⚠ CONFLICT:** FPF-Spec не preserves "alpha" as standalone
term. Alpha-as-track dispersed в FPF на:
- **U.RoleStateGraph** (A.2.5) — state machine роли
- **U.Episteme** (C.2.1) для knowledge alphas
- **U.System** (A.1) для physical alphas
- **U.Work / U.WorkPlan** (A.15.1, A.15.2) для work alphas
- **PhaseOf** (A.14) — temporal parts of same carrier

**Jetix resolution** (per KB Section 11.1 Q1): **Hybrid** — keep "альфа" as
Plain label (pedagogical continuity с ШСМ), U.X as Tech twin (per E.10
LEX-BUNDLE 4-register). Section 6 8 true alphas — uses Russian-pedagogical
"альфа" term + cross-references к FPF U.Types.

#### 5.10.3 Граф создания (Creation Graph)

Fully covered Section 3. FPF correlation ✅ A.1 + A.14 + B.1.

#### 5.10.4 Стратегирование (Strategizing)

**Definition** (Левенчук, *Методология 2025*):
> «метод выбора метода — стратегирование. В условиях, когда вообще
> непонятно, что делать. А если непонятно, что именно делать, то и
> планировать ещё ничего нельзя (потребные ресурсы неизвестны), и работать
> нельзя.»

**Structural positioning:**
```
СТРАТЕГИРОВАНИЕ → выбор метода
        ↓
ПЛАНИРОВАНИЕ → распределение ресурсов под выбранный метод
        ↓
РАБОТА → исполнение по плану
```

**FPF correlation ✅:** **E.9 DRR Design-Rationale Record** (Problem frame
/ Decision / Rationale / Consequences) + **B.5.2 Abductive Loop** + **C.11
Decsn-CAL** + **C.18/C.19 NQD + E/E-LOG**.

**Strategizing as trigger-driven event, НЕ scheduled** (Section 7.2).

**"AI agents don't strategize" hard rule** (per Левенчук, ailev/1795494):
- No identity / no commitment / no long-term memory / no skin-in-game.
- AI can support: SoTA harvesting (G.2), variant generation, critique,
  abductive prompting. AI cannot: method selection, final acceptance.
- `strategy-support-analyst` agent — J3 support, not J4 strategic.

#### 5.10.5 Мышление письмом (Writing-as-Thinking)

Fully covered IP-3 + IP-7. FPF correlation ✅ throughout.

### 5.11 Composition of 5 primitives

```
ГРАФ СОЗДАНИЯ
    │ задаёт контекст для
    ↓
РОЛИ ←────────── СТРАТЕГИРОВАНИЕ
    │                    │ принимает решения
    │ работают с         │ о методах
    ↓                    │
АЛЬФЫ ───────────────────┘
    │ переходы фиксируются
    ↓
МЫШЛЕНИЕ ПИСЬМОМ ──── экстернализирует все
    │
    ↓
ЭКЗОКОРТЕКС (input для агентов следующей сессии)
```

### 5.12 Cross-refs

- **FPF A.2.*** (Role Taxonomy) — roles
- **FPF A.6.0 U.Signature** (L.8062) — kind-explicit role headers
- **FPF A.13 Agential Role & Agency Spectrum** (L.17328)
- **FPF A.14 Advanced Mereology** (L.17478) — creation graph edges
- **FPF A.15 Role-Method-Work Alignment** — firewall
- **FPF E.2 Eleven Pillars** (L.40148)
- **FPF E.5 Four Guard-Rails** (L.40487)
- **FPF F.6 Role Assignment Cycle** (L.50641) — F.6 6-step
- Левенчук *Методология 2025*, *Системное мышление 2024* т.1
- Левенчук ailev/1795494 (founder syndrome critique)
- Левенчук ailev/1769411 (LLM writing-as-thinking warning)

---

## Section 6 — 8 True Alphas (with A.14 typed mereology)

Per MC6 strict + Item 6 Portfolio override + Rec-05 A.14 retrofit. 8 true
alphas материализуются в `alphas/` с past-participle state machines.

### 6.1 Reclassification table (v1 → v2-Ruslan-approved)

| v1 Original | v2 + Ruslan decision |
|-------------|----------------------|
| Client (alpha 1) | ✅ Alpha 1 — Client |
| Project (alpha 2) | ✅ Alpha 2 — Project |
| Deal (alpha 3) | ✅ Alpha 3 — Deal |
| Content Item (alpha 4) | ✅ Alpha 4 — Content Item |
| Hypothesis (alpha 5) | ✅ Alpha 5 — Hypothesis |
| Member (alpha 6) | ✅ Alpha 6 — Member (preserved despite Левенчук drop rec; Ruslan MC3) |
| Way of Working (alpha 7) | ✅ Alpha 7 — Way of Working |
| — | ✅ Alpha 8 — **Direction** (NEW — Jetix innovation, Portfolio-of-Directions P8) |
| Invoice | ❌ Reclassified — work product (finance/invoices/YYYY/) |
| SKU | ❌ Reclassified — entity (catalog/) |
| Postmortem | ❌ Reclassified — work product (decisions/postmortem/) |
| Research Note | ❌ Reclassified — work product (wiki/sources/) |

### 6.2 State machines (past-participle strict)

| # | Alpha | States |
|---|-------|--------|
| 1 | **Client** | `lead-identified` → `qualified` → `proposed` → `in-negotiation` → `won` / `lost` → `churned` |
| 2 | **Project** | `scoped` → `kicked-off` → `started` → `delivered` → `closed` → `in-follow-up` |
| 3 | **Deal** | `drafted` → `signed` → `activated` → `completed` / `cancelled` |
| 4 | **Content Item** | `drafted` → `in-review` → `approved` → `published` → `retired` |
| 5 | **Hypothesis** | `formulated` → `under-validation` → `validated` / `invalidated` → `implemented` |
| 6 | **Member** | `applied` → `invited` → `activated` → `flagged-at-risk` → `churned` |
| 7 | **Way of Working** | `drafted` → `implemented` → `refined` → `deprecated` |
| 8 | **Direction** | `hypothesized` → `under-validation` → `validated` → `activated` → `scaled` → `plateaued` / `invalidated` / `dropped` → `archived` |

### 6.3 Per-alpha deep treatment

#### 6.3.1 Alpha 1 — Client

**Cross-refs:** FPF U.Episteme slot `DescribedEntitySlot` holds Client-as-
entity; RoleStateGraph (A.2.5) applied per-instance; ClaimGraphSlot tracks
pipeline-stage claims.

**State checklist examples (verifiable):**
- `qualified`: MECE eligibility matrix passed (jurisdiction DACH|US|RU;
  industry Jetix-ICP; revenue >€10M; decision-maker identified;
  pain-signal explicit).
- `in-negotiation`: Proposal sent; 1+ call scheduled; decision-maker
  engaged; A.6.B L/A/D/E template applied.
- `won`: Contract signed (wet signature OR DocuSign); 1st invoice paid
  OR Scope-of-Work acknowledged.

**A.14 typed edges:**
- Client ComponentOf Jetix-Sales-Function (at operational runtime).
- Client fills ICP slot (directions/_active/ai-consulting-dach/).
- Client methodologically-uses MECE-qualification method.

#### 6.3.2 Alpha 2 — Project

**State checklist examples:**
- `kicked-off`: SoW signed; project manager (Ruslan or sub-role) assigned;
  kickoff meeting minutes committed к decisions/; bias-audit BA-0 template
  initialized (per D.5 Rec-03).
- `started`: 1st work-session committed; 1st deliverable draft created.
- `delivered`: All SoW deliverables submitted; Multi-View Viewpoint Bundle
  emitted (5 viewpoints per Gap 5, if Audit SKU); BA-3 closure signed.
- `closed`: Client acceptance signed; final invoice paid; lessons-learned
  artifact committed к wiki/summaries/.

#### 6.3.3 Alpha 3 — Deal

**Past-participle discipline strict.** Deal ≠ Client (client is relationship,
deal is specific transaction).

**A.14 typed edge:** Deal ComponentOf Client-relationship lifecycle;
PhaseOf representative temporal slice (Q2 2026 Deal vs Q3 Expansion Deal).

#### 6.3.4 Alpha 4 — Content Item

Includes: blog posts, LinkedIn posts, YouTube videos (co-produced с Rodion),
newsletter editions, conference talks, podcast appearances.

**State flow:** drafted → in-review (Ruslan / framing-lead / acceptance-
authority) → approved → published → retired.

#### 6.3.5 Alpha 5 — Hypothesis

**Portfolio integration (Rec-07):** Hypothesis belongs to Direction;
**NQD-CAL (C.18)** + **E/E-LOG (C.19)** per-direction tracking applied.
Files: `directions/<slug>/nqd-distinctions.yaml` + `ee-log.yaml`.

**State flow:** formulated (initial observation) → under-validation
(experiment designed, running) → validated / invalidated (evidence
sufficient to commit) → implemented (validated hypothesis becomes
operational practice или direction pivot).

#### 6.3.6 Alpha 6 — Member (preserved per Ruslan MC3)

Левенчук recommendation was drop Member alpha. **Ruslan override:** preserve
("Member — это альфа, да, мы это оставляем").

Phase 1: schema + empty instances. Activation trigger: 1st L4 client
closed → Founding Alliance Member (L5 Membrane).

**State flow:** applied → invited → activated → flagged-at-risk → churned.

#### 6.3.7 Alpha 7 — Way of Working

Meta-alpha — Jetix methodology evolution itself as tracked object.
**Self-reference property**: this D6 document is one WoW instance (state:
drafted → in-review). When D6 passes FPF-Steward Q2 audit → state:
implemented.

#### 6.3.8 Alpha 8 — Direction (Portfolio-of-Directions innovation)

**State flow:** hypothesized → under-validation → validated → activated →
scaled → plateaued / invalidated / dropped → archived.

**Direction authority (per D7):**
- **Open hypothesis direction:** J-Auto (strategy-support-analyst может
  propose).
- **Activate direction:** J-Strategic (Ruslan only).
- **Archive direction:** J-Strategic (Ruslan only, с post-mortem).

**Kill criteria CHR** (Gap 3, Rec-11): `directions/_templates/kill-chr-
template.yaml` + applied к existing directions. Formal A.18 CSLC measures
readiness-to-kill.

**Per-direction artifacts (Rec-07):**
- `direction.md` (thesis / ICP / economics / conviction / kill-criteria)
- `hypotheses/` (testable hypothesis alphas within direction)
- `experiments/` (planned + running)
- `research/`
- `pipeline.md`
- `state.yaml`
- `nqd-distinctions.yaml` (C.18 novel-question distinctions)
- `ee-log.yaml` (C.19 exploration-exploitation log)
- `kill-chr.yaml` (Gap 3 CHR formal)
- `outreach/{de,en,ru}/` (per-language copy)

**Active Phase 1:** `directions/_active/ai-consulting-dach/` (primary Q2
revenue bet).

**Hypothesis directions** (some):
- `_hypotheses/shaurma-chains-automation/`
- `_hypotheses/cybersecurity-dach-mittelstand/`
- `_hypotheses/ai-tools-opensource-saas/`

### 6.4 Reclassified (NOT alphas)

**Invoice:** Work product (not state-tracked lifecycle holon). Lives в
`finance/invoices/YYYY/<Rechnungsnummer>.yaml`. **Invoice monotonicity
hook** (Hook 2) enforces sequential numbering per HGB §14 UStG.

**SKU:** Entity (object справочника без lifecycle). Lives в
`catalog/<sku>.yaml` OR `decisions/policy/sku-catalog.md`. **Versioned
A.6.S signatures** (per Rec-19) — v1 active для old clients + v2 для new.

**Postmortem:** Work product. Lives в `decisions/postmortem/YYYY/<slug>.md`.

**Research Note:** Work product. Lives в `wiki/sources/<slug>.md`.

### 6.5 Cross-references к SEMAT Essence Kernel (R-D legacy)

Jetix alphas evolve SEMAT Essence kernel:

| SEMAT Essence | Jetix |
|---------------|-------|
| Opportunity | Implicit в Client pre-qualification |
| Stakeholders | Implicit в Client + advisory-board entities |
| Requirements | `direction.md` thesis + Project SoW + Client briefing |
| Software System | n/a (Jetix is consulting, not software shipping Phase 1) |
| Work | Alpha 2 Project |
| Way of Working | Alpha 7 Way of Working |
| Team | Implicit в 11 agent roster + Ruslan multi-binding |

### 6.6 FPF pattern cross-refs

- **FPF A.2.5 U.RoleStateGraph** (role state machine) — all 8 alphas
  carry this structure.
- **FPF A.6 boundary discipline** — alpha transitions require explicit
  state checklist satisfaction (per MC6).
- **FPF C.2.1 U.EpistemeSlotGraph** — alphas 4-7 (Content Item,
  Hypothesis, Way of Working, Direction portions) are epistemic; slot
  graph applies.
- **FPF A.15.1 U.Work** — Project (alpha 2) carries U.Work record-of-
  occurrence.
- **FPF A.15.2 U.WorkPlan** — Project `kicked-off` state requires U.WorkPlan
  artifact.
- **FPF C.18 NQD-CAL** + **C.19 E/E-LOG** — Hypothesis + Direction
  use these for portfolio-level exploration.

### 6.7 Cross-refs

- **FPF A.2.5 U.RoleStateGraph** — state machine pattern
- **FPF C.2.1 U.EpistemeSlotGraph** (L.30495) — epistemic slot structure
- **FPF A.14 Advanced Mereology** — typed edges applied here
- **Rec-05** — A.14 typed edges retrofit
- **Rec-07** — C.18/C.19 per-direction
- **Rec-19** — A.6.S SKU signature versioning
- `alphas/` — 8 state machines + instances
- `decisions/policy/mereology-edge-types.md`

---

## Section 7 — Ritual Cadence + Strategizing as Event

### 7.1 4 rituals Phase 1 + B.4 Canonical Evolution Loop mapping (Rec-14)

Per D8 Chunk 6 Area 8 + Rec-14 (Chunk 8). B.4 Observe/Reflect/Decide/Act
mapped к 4 rituals:

| Ritual | Cadence | Duration | B.4 phase | Content |
|--------|---------|----------|-----------|---------|
| **Daily morning** | Every day | 30 min | **Observe** (B.4.1) | Inbox triage + pipeline snapshot + daily intent |
| **Weekly Friday** | Weekly | 60 min | **Reflect** | Shape Up commits review + close-week log + next-week framing |
| **Monthly last Friday** | Monthly | 2h | **Decide** | P&L review + OKR progress + founder note + meta-review |
| **Quarterly** | Quarterly | 1 day | **Act** | Quarterly letter + OKR-next + role-manifest delta + strategy updates + attention-theme setting |

**FPF grounding** (per Rec-14):
- **B.4 Canonical Evolution Loop** (L.29094) — Observe → Notice → Stabilize
  → Route pipeline.
- Jetix 4-ritual cadence operationalizes loop per temporal granularity.

**Quarterly ritual includes:**
- Founder letter (written, long-form; writing-as-thinking primitive).
- OKR-next (objective + key results for next quarter).
- Role-manifest delta (any changes к 18 role-manifests).
- Strategy updates (pivot signals, major decisions).
- Attention-theme setting (`decisions/quarterly/YYYY-QN-attention-theme.md`).
- **Example attention-theme Q2 2026:** "First €50K revenue from DACH
  Mittelstand" с 60% Sales / 25% Delivery / 10% Architecture / 5%
  Learning allocation.

### 7.2 Strategizing as trigger-driven event (NOT scheduled)

**Statement (hard rule):** Strategizing happens на триггере, не по
расписанию. If strategizing scheduled without trigger → not strategizing,
это performance ritual (per Левенчук R-B Section 4.2).

**Trigger types** (applied from Jetix context):

| Trigger type | Example |
|--------------|---------|
| **Market signal** | 3+ DACH Mittelstand requests for new AI-audit type |
| **Alpha failure persistent** | `Client.qualified → Client.lost` persistently (>5 consecutive) |
| **Method exhaustion** | Pipeline conversion below threshold (e.g. <10% for 2 consecutive months) |
| **Irreversible decision** | 1st human hire (Phase 2a trigger Triple-AND hit) |
| **System boundary change** | New EU AI Act obligation goes live (Aug 2026) |
| **New role / responsibility** | First enterprise-tier client needing Customer Success |
| **Regulatory inflection** | BaFin inquiry, Bundeskartellamt contact, new Member State implementation law |
| **Direction kill criteria hit** | `_active` direction fails kill criteria CHR |
| **Resource inflection** | Compute spend >3× expectation (P7 anomaly) |

**Required artifact components (per E.9 DRR):**
- **Problem frame** — what trigger fired? Why strategizing now?
- **Decision** — chosen method (включая roles, alphas, target state graph).
- **Rationale** — alternatives considered; Pillar check; taxonomy lens;
  DRR Δ-class (Δ-0/1/2/3).
- **Consequences** — benefits, trade-offs, impacts, risks.
- **Kill conditions** — explicit criteria for reverting decision.
- **Review checkpoint** — когда revisit.

**Written artifact:** `decisions/strategy/YYYY-MM-DD-<trigger-slug>.md`.

### 7.3 F.11 Method Quartet Harmonisation (Rec-18, monthly)

Per **F.11** (L.52604) Method Quartet Harmonisation — monthly check per
direction:

| Box | What |
|-----|------|
| **method-design** | How direction's method was originally conceived (intent) |
| **method-work** | Actual applied method (what happened) |
| **method-plan** | Next-iteration plan |
| **method-evidence** | Evidence of effectiveness |

**Harmonisation audit** monthly — verify 4 boxes коhere. If design diverges
от work without explicit Bridge (F.9) — flag for strategizing trigger.

**Artifact:** `directions/<slug>/method-harmonisation-YYYY-MM.md`.

### 7.4 G.5 Multi-Method Dispatcher (Rec-21)

**MethodFamily Registry** — дispatch among rival method families within
direction.

**Operational:** `decisions/policy/multi-method-dispatcher.md` — registry
+ dispatcher rules для multi-method decisions.

**FPF grounding:** **G.5 Multi-Method Dispatcher & MethodFamily Registry**
(L.58316) — selector outcome kinds: `Shortlist (unordered)`,
`RankedShortlist (ordered)`, `SpecialistHandoff`, `AbstainOutcome`,
`EscalationOutcome`.

**Jetix applicability:** Phase 1 limited (single ai-consulting-dach
direction methodology). Phase 2b+ when 3+ active directions simultaneously
— registry becomes operational.

### 7.5 Rec-07 C.18 NQD-CAL + C.19 E/E-LOG per-direction

**NQD-CAL** (C.18, L.37808) — Novelty + Quality + Diversity open-ended
search calculus.

**E/E-LOG** (C.19, L.38008) — Explore-Exploit Governor pool-policy
actions:
- **Widen** (increase exploration)
- **Keep frontier**
- **Narrow to subset**
- **Sunset line**
- **Reroute**

**Per-direction files:** `nqd-distinctions.yaml` + `ee-log.yaml` per
`directions/<slug>/`.

**BLP (Bitter-Lesson Preference, C.19.1):** Prefer general/scalable methods
over hand-tuned heuristics when safety/legality equivalent. Jetix BLP: try
generic LLM-based approach before bespoke custom workflow.

### 7.6 Cross-refs

- **FPF B.4 Canonical Evolution Loop** (L.29094) + B.4.1 Observe step
- **FPF B.5.2 Abductive Loop** + B.5.2.0 U.AbductivePrompt
- **FPF E.9 DRR** (L.41506) — strategizing artifact structure
- **FPF F.11 Method Quartet Harmonisation** (L.52604)
- **FPF G.5 Multi-Method Dispatcher** (L.58316)
- **FPF C.18 NQD-CAL** (L.37808) + **C.19 E/E-LOG** (L.38008)
- **Rec-14, Rec-18, Rec-21, Rec-07** — Chunk 8 adoptions
- `decisions/quarterly/` — attention-theme records
- `decisions/strategy/` — trigger-driven strategizing records

---

## Section 8 — U-Types Full (Deep Левенчук treatment)

Per Chunk 6 Area 6 — "Full" (not "Lite" 6 U-Types). Per Gap 4 UTS + Rec-12
LEX-BUNDLE — **4-register naming (tech / plain / legacy / mnemonic)**.

### 8.1 U-Types list Phase 1 (Jetix applicable)

Per **E.10 LEX-BUNDLE** (L.41604) naming discipline:

| # | FPF U.Type | Tech name | Plain name (EN) | Legacy (SEMAT/ШСМ) | Mnemonic |
|---|-----------|-----------|-----------------|--------------------|----|
| 1 | **U.System** | `jetix-system` | Jetix system | Jetix-as-whole (v1) | Jxs |
| 2 | **U.Episteme** | `jetix-episteme` | Knowledge artifact | Description / Alpha knowledge (SEMAT) | Epi |
| 3 | **U.Holon** | `jetix-holon` | Whole-and-part entity | — (Koestler legacy) | Hol |
| 4 | **U.Boundary** | `jetix-boundary` | Entity interface | System interface (SE) | Bnd |
| 5 | **U.BoundedContext** | `jetix-context` | Local semantic frame | — (DDD legacy bridge) | BC |
| 6 | **U.Role** | `jetix-role` | Role (method signature) | ШСМ роль / SEMAT role | Rol |
| 7 | **U.RoleAssignment** | `role-assignment` | Role assignment (Holder#Role:Context) | — | RAsg |
| 8 | **U.RoleStateGraph** | `role-state-graph` | Role state machine | Alpha state machine (SEMAT) | RSG |
| 9 | **U.Method** | `jetix-method` | Method | ШСМ метод / Way of Working | Mth |
| 10 | **U.MethodDescription** | `method-description` | Method recipe / SOP | Практика (ШСМ) / Practice | MDesc |
| 11 | **U.Stakeholder** | `jetix-stakeholder` | Stakeholder | SEMAT stakeholders / ШСМ внешние проектные роли | Stk |
| 12 | **U.Objective** | `jetix-objective` | Quarterly attention-theme / direction goal | OKR objective | Obj |
| 13 | **U.Decision** | `jetix-decision` | Decision (ADR + DRR record) | — (FPF E.9 DRR) | Dec |
| 14 | **U.Practice** | `jetix-practice` | Practice protocol | SEMAT Practice | Prct |
| 15 | **U.Case** | `jetix-case` | Case study (CHR application) | — (Gap 3 CHR) | Cse |
| 16 | **U.Knowledge** | `jetix-knowledge` | Cross-cutting knowledge (wiki/) | — | Knw |
| 17 | **U.Artifact** | `jetix-artifact` | Deliverable artifact | SEMAT work product | Art |
| 18 | **U.Work** | `jetix-work` | Work (record of occurrence) | SEMAT work alpha | Wrk |
| 19 | **U.WorkPlan** | `jetix-work-plan` | Work plan (schedule of intent) | Plan | WPl |
| 20 | **U.Signature** | `jetix-signature` | Kind-explicit header | — | Sig |
| 21 | **U.Mechanism** | `jetix-mechanism` | Law-governed application | — | Mch |
| 22 | **U.Kind** | `jetix-kind` | Type (intent) | — | Knd |
| 23 | **U.RoleMask** | `jetix-role-mask` | Contextual role adaptation | — | Msk |
| 24 | **U.Capability** | `jetix-capability` | Dispositional capability | — | Cap |
| 25 | **U.Commitment** | `jetix-commitment` | Deontic commitment | — | Cmt |
| 26 | **U.SpeechAct** | `jetix-speech-act` | Communicative work | — | SpA |
| 27 | **U.MultiViewDescribing** | `multi-view-kit` | Multi-View Publication Kit | — (E.17) | MVPK |
| 28 | **U.LanguageStateSpace** | `lang-state-space` | Position on language-state chart | — (C.2.2a) | LSS |
| 29 | **U.AbductivePrompt** | `abductive-prompt` | Prompt for hypothesis work | — (B.5.2.0) | AbP |
| 30 | **U.ClaimScope** | `claim-scope` | Bounded context path of claim | — (new canonical) | CS |
| 31 | **U.WorkScope** | `work-scope` | Capability scope | — (new canonical) | WS |
| 32 | **U.Holon** | `direction-holon` | Direction (Jetix innovation) | — (P8) | Dir |
| 33 | **U.Case** | `chr-space` | Characteristic Space (SKU / direction-kill / agent-promotion) | — (Gap 3) | CHR |

**Note:** Actual UTS `wiki/foundations/jetix-uts.md` Layout A Kernel-first
carries 30-50 rows × 6-8 context columns (concurrent с D6 writing per
OQ-08 B). This D6 Section 8 list provides ontology foundation; UTS provides
cross-context mapping.

### 8.2 LEX-BUNDLE 4-register discipline (per Rec-12 via Gap 4 UTS)

**FPF grounding:** **E.10 LEX-BUNDLE** (L.41604) — Unified Lexical Rules.

**Tech label (authoritative):** testable semantic token used в normative
clauses.

**Plain label (didactic):** display-only synonym; permitted только в
expository text; must map 1:1 к Tech meaning.

**Legacy label:** historical/SEMAT/ШСМ reference (bridges к prior
pedagogy).

**Mnemonic label:** shorthand для communication (3-4 letter code).

**Example row** (U.Method):
- Tech: `jetix-method`
- Plain: "Method" / "Metodo" / "Метод"
- Legacy: SEMAT "Way of Working" / ШСМ "метод" / intermediate "технология"
- Mnemonic: "Mth"

**Morphology discipline** (per E.10 Onto2 I/D/S):
- Bare head = Intension (`jetix-method` = the idea)
- `…Description` = Description (`method-description` = the recipe)
- `…Spec` = testable Specification (`method-spec` = acceptance criteria)

### 8.3 Vertical stratification ladder (per E.10 §2)

```
1. Kernel (U.* types, kernel relations, invariants)
2. Extension patterns (CAL/LOG/CHR exports — Sys-CAL, KD-CAL, CHR-CAL,
   Decsn-CAL, etc.)
3. Context (U.BoundedContext + Glossary + Invariants + Roles + Bridges)
4. Instance (concrete identifiers: holders, role assignments, work
   records, carriers)
```

No cross-bleed allowed. Jetix context (jetix-ops) sits Stratum 3; Ruslan
as holder sits Stratum 4; JETIX-FPF Kernel alignment Stratum 1-2.

### 8.4 Bridges to external contexts

Explicit Bridges (F.9) с CL per E.10 + Gap 4:

| Jetix concept | External context | Bridge relation | CL | Loss notes |
|---------------|------------------|-----------------|----|-----|
| `jetix-role` | ArchiMate Business Role | Partial-overlap (Interpretation) | CL=1 | Missing method-signature binding |
| `jetix-role` | Holacracy Role | Partial-overlap (Interpretation) | CL=1 | Governance unit vs ontological object |
| `jetix-alpha` (Plain) | SEMAT Essence Alpha | Near-identity (Substitution) | CL=3 | Full equivalence preserved |
| `jetix-method` | BPMN Process | Partial-overlap (Interpretation) | CL=2 | BPMN flat; method recursive + meta-method |
| `role-assignment` (Holder#Role:Context) | RACI matrix role | Narrower | CL=1 | RACI orthogonal; role-assignment richer |
| `jetix-holon` | Koestler holon | Equivalence (Substitution) | CL=3 | Koestler 1967 + FPF A.1 aligned |
| `jetix-work` | SEMAT Work | Narrower | CL=3 | FPF refines; record-of-occurrence precision |
| `jetix-objective` | OKR objective | Broader | CL=2 | OKR narrower (quarter-bound metric); U.Objective includes attention-theme |
| `jetix-decision` | ADR (architecture decision record) | Broader | CL=3 | FPF DRR generalizes ADR to non-architectural decisions |

### 8.5 Forbidden patterns (per E.10 + IP-2 + GR-1)

**Anti-patterns blocked Hook 3 + E.5.1 DevOps Lexical Firewall:**
- Bare `yaml`, `docker`, `CI/CD` tokens в Core patterns (go к Tooling
  companion).
- Figurative heads в Kernel (no "Tradition" / "family" / "process" /
  "function" without head noun signalling kind).
- Global label illusion ("Client" without Context-scope).
- Direction amnesia (Bridge without direction → / ↔).
- String-equals fallacy (name match ≠ semantic match).

### 8.6 Cross-refs

- **FPF A.2.*** Role Taxonomy family
- **FPF A.3 Transformer Quartet** (L.~1700) — System-in-Role /
  MethodDescription / Method / Work
- **FPF A.6.0 U.Signature** (L.8062)
- **FPF A.15 Role-Method-Work Alignment** (L.~17200)
- **FPF C.2.1 U.EpistemeSlotGraph** (L.30495)
- **FPF C.3 Kind-CAL** (L.33185)
- **FPF E.10 LEX-BUNDLE** (L.41604)
- **FPF F.17 UTS** (L.54586)
- **FPF K Lexical Debt** (L.62123) — deprecated terms mandatory replacements
- `wiki/foundations/jetix-uts.md` (30-50 rows UTS)

---

## Section 9 — "What ШСМ is NOT" (protection section, expanded)

Per Chunk 6 Area 6 + ШСМ anti-pattern tradition. **Protect discipline from
misuse-by-name.**

### 9.1 The misuse-by-name principle

Per R-B opening principled distinction:
- **Violation by misuse:** practitioner uses ШСМ terms ("роль", "альфа",
  "стратегирование") но keeps semantics своего исходного domain (software,
  PM, HR) → ontological noise masquerading as systems thinking. **Более
  опасно** чем полный отказ от ШСМ terminology.
- **Violation by omission:** practitioner не uses ШСМ terms но models
  reality correctly → less dangerous.

**For Jetix:** "Лучше говорить 'задача' и корректно моделировать, чем
говорить 'альфа' и думать о Jira-тикете."

### 9.2 Core protection table

| ШСМ concept | **IS NOT** | Why matters |
|-------------|-----------|-------------|
| **ШСМ роль** | software class | Static description в коде ≠ onto object в meta-model |
| **ШСМ роль** | Holacracy role | Governance unit ≠ method signature |
| **ШСМ роль** | RACI assignment | Matrix кто отвечает ≠ method применяется к каким альфам |
| **ШСМ роль** | должность (position) | Place в org ≠ function в method |
| **ШСМ альфа** | database table | Table = storage schema; альфа = предмет метода |
| **ШСМ альфа** | Jira ticket / JTBD | Ticket = work item; альфа = tracked method-subject |
| **ШСМ альфа** | activity / process | Activity = доing; альфа = being-done-to |
| **ШСМ граф создания** | workflow | Workflow = sequence activities; граф = онтологические relations |
| **ШСМ граф создания** | dependency tree | Dep tree = technical zависимости; граф = кто создаёт кого |
| **ШСМ граф создания** | org chart | Org chart = подчинения; граф = отношения создания |
| **ШСМ стратегирование** | planning meeting | Planning = allocation; strategizing = method choice under uncertainty |
| **ШСМ стратегирование** | brainstorming | Brainstorm = idea generation; strategizing = decision with kill conditions |
| **ШСМ мышление письмом** | documentation generation | Doc-gen = fixation; writing-as-thinking = cognitive process |
| **ШСМ мышление письмом** | Confluence pages | Confluence = storage; writing-as-thinking = active transformation |
| **ШСМ мышление письмом** | prompted AI output | AI output = model on data; writing-as-thinking = externalization concrete agent cognition |

### 9.3 FPF Holon extensions (per KB Section 7.3 exclusions)

| FPF Holon | **IS NOT** | Why matters |
|-----------|-----------|-------------|
| **FPF Holon** | software component | Component = module; holon = whole-and-part simultaneously |
| **FPF Holon** | microservice | Microservice = deployment unit; holon = ontological unit |
| **FPF Holon** | Kubernetes pod | Pod = runtime entity; holon = design-level composition unit |
| **FPF Holon** | class hierarchy member | Class hierarchy = IS-A static typing; holon = Janus-face dynamic |
| **FPF Holon** | BFO entity | BFO explicitly rejected per ailev/1451832 — "негодная онтология для инженерных задач"; holon = engineering-grounded |

### 9.4 A.14 mereology firewall (per A.14 normative)

Confusion that A.14 rules out:

| Tempting to say... | A.14 rules out |
|--------------------|-----|
| "Task belongs to project" | Use `ComponentOf` (structural) or `creates` edge; NOT `PortionOf` (measure-preserving stuff) |
| "Project is phase of program" | If identity breaks → declare MHT; NOT `PhaseOf` |
| "Team is part of organization" | Teams are collective agents; `MemberOf` collection relation, NOT `ComponentOf` |

### 9.5 Jetix-specific: FPF vs JETIX-FPF distinction

**Statement:** **"FPF"** (canonical, Левенчук's) ≠ **"JETIX-FPF"** (our
adaptation).

**Why matters:**
- Attribution clarity (no confusion about authorship).
- Freedom to adapt without misrepresenting Левенчук.
- Hard internal-only stance (OQ-09 A) preserved — JETIX-FPF secret sauce,
  FPF community-open (sort of — upstream "all rights reserved" default
  anyway).

**Cross-reference convention** в Jetix documents:
- Cite **FPF canonical** for authoritative reference: "FPF A.6.B Boundary
  Norm Square (Левенчук 2026, L.7097)".
- Cite **JETIX-FPF** for Jetix-specific adaptation: "JETIX-FPF Section
  5.3 IP-3 Artifacts over conversations".

**Cross-reference frequency:** 80%+ JETIX-FPF sections cite canonical FPF
patterns explicitly (see Section 14 References).

### 9.6 Strategizing ≠ scheduled event

Already covered Section 7.2. Hard rule: trigger-driven, not calendar-
driven. If calendar-driven → performance ritual, not strategizing.

### 9.7 Agent ≠ strategizing entity

Already covered Section 5.10.4. Hard rule: agents support strategizing,
cannot substitute. Strategy-support-analyst = J3 support, not J4.

### 9.8 Cross-refs

- **FPF A.7 Strict Distinction** (Clarity Lattice)
- **FPF E.5.1 DevOps Lexical Firewall** (L.40589)
- **FPF K Lexical Debt** (L.62123)
- **R-B anti-patterns** (KB Section 3.*)
- `decisions/policy/mereology-edge-types.md` — A.14 firewall

---

## Section 10 — Mereology + Holon Hierarchy (full, not lightweight)

Per MC3 override — "Три уровня mereological важно, обязательно мы делаем
все три уровня максимально глубоко... Никаких упрощений."

### 10.1 Classical mereology lineage

**Foundational:**
- **Stanisław Leśniewski** *Foundations of the General Theory of Sets*
  (1916), *Foundations of Mathematics* (1927-1931). Polish nominalist
  motivation: alternative к Cantorian set theory без abstract objects.
- **Henry Leonard + Nelson Goodman** *The Calculus of Individuals* (1940).
  Modern accessible formulation.
- **Aristotle, Husserl, Leibniz** — pre-formal antecedents.

**Distinction from set theory:**
- Set theory: {A, B} is abstract, contains А, B as *members*.
- Mereology: whole is **nothing over and above** parts; concrete fusion.
- Tarski (1935): Models of GEM isomorphic to complete Boolean algebras
  minus zero element — algebraic character.

**Major formal systems:**

| System | Additions | Character |
|--------|-----------|-----------|
| M (Minimal) | Reflexivity + Transitivity + Antisymmetry | Partial ordering |
| MM | + Weak Supplementation | Proper part implies disjoint companion |
| EM | + Strong Supplementation | No two distinct wholes с same proper parts |
| GEM | + Unrestricted Composition | Classical (Leonard-Goodman) |
| CEM | = GEM | Classical Extensional Mereology |

**Three core axioms:**
- Reflexivity (P.1): ∀x Pxx
- Transitivity (P.2): (Pxy ∧ Pyz) → Pxz
- Antisymmetry (P.3): (Pxy ∧ Pyx) → x=y

**Critical supplementation:**
- **Weak Supplementation (P.4):** Proper part has companion disjoint part.
- **Strong Supplementation (P.5):** Entails extensionality.

**GEM Unrestricted Composition (P.15):** Any non-empty collection has
fusion. Implies "fusion of Cleopatra's nose and Eiffel Tower" exists.
Operationally irrelevant для Jetix (only intentional compositions matter).

### 10.2 David Lewis mereological universalism

*Parts of Classes* (1991) — applied GEM к set theory; defended mereological
universalism (composition unrestricted, relevance restricted). **The
pragmatic stance FPF effectively adopts** (Левенчук-favored approach).

### 10.3 Kit Fine hylomorphic mereology (acknowledged, applicable где useful)

*Things and Their Parts* (1999):
- **Hylomorphism** — form as constitutive element.
- **Qua-objects** — object qua playing a role.
- **Mereological coincidence** — distinct objects same location, different
  modal profiles (statue vs clay).
- **"Monster Objection"** against CEM: ham + cheese + bread fuse to ham-
  sandwich BEFORE assembly (since fusion exists whenever parts exist).

**Most philosophically sophisticated departure from CEM.**

**FPF stance (per KB Section 7.3):** Kit Fine qua-objects excluded — FPF
uses **RoleMask** (C.3.4) pattern instead (role as mask holon wears в
context, no separate qua-object needed).

**For Jetix:** Kit Fine granular mereology vocabulary **acknowledged where
useful**; full formal apparatus skipped. Per Section 7.6 KB evaluation,
extract concept "granularity level"; skip formal apparatus.

### 10.4 Constructor theory (Deutsch + Marletto, vocabulary only)

**Constructor theory** (2012-present): Meta-theory of physics — possible
vs impossible transformations (tasks). Not mereology per se but provides
vocabulary for FPF creation graph. FPF imports **vocabulary only** (not
physics foundations) per ailev/1776793.

**For Jetix:** applicable где useful (Section 13 Constructor/Category
applications).

### 10.5 Koestler holons + Wilber four-quadrants

**Arthur Koestler** *The Ghost in the Machine* (1967). Coined "holon"
from Greek *holos* (whole) + *-on* (part).

**Definition:** "Sub-wholes on any level of the hierarchy are referred to
as holons."

**Key propositions:**
- (1.2) Multi-levelled hierarchy of semi-autonomous sub-wholes.
- (1.3) Parts and wholes in absolute sense don't exist.
- (1.4) **Janus phenomenon** — holons face inward (parts) AND outward
  (containing whole) simultaneously.
- (1.5) Applies к any stable bio/social sub-whole с rule-governed behaviour.

**S-A vs INT tendencies (Proposition 4.1):**
> Every holon has dual tendency to preserve and assert its individuality
> as quasi-autonomous whole; AND to function as integrated part of larger
> whole.

- **S-A (Self-assertive)** — wholeness expression.
- **INT (Integrative)** — partness expression.

**Dynamic equilibrium (Prop 9.1):** Healthy organism balances S-A and INT
tendencies. Two failure modes:
- (9.4) S-A excess: holon "monopolizes functions".
- (9.5) INT excess: "power of whole erodes part autonomy" (groupthink).

**Ken Wilber** (*Sex, Ecology, Spirituality*, 1995) — Four Quadrants:

| Quadrant | Label | Description |
|----------|-------|-------------|
| UL | "I" | Subjective experience, consciousness |
| UR | "It" | Physical form, observable behavior |
| LL | "We" | Shared culture, values |
| LR | "Its" | Social systems, institutions |

**Tetra-arising:** Every holon enacts all four quadrants simultaneously.

**Other extensions acknowledged:**
- **Piero Mella** *The Holonic Revolution* — functional emergence beyond
  structural.
- **Erich Jantsch** *The Self-Organizing Universe* — self-organization
  through coherence thresholds.
- **Maturana + Varela autopoiesis** — strong version of holonic self-
  assertion.

### 10.6 Jetix holon hierarchy fully documented

Per Chunk 6 Area 6 requirement. Full structure:

```
Level 0 (Biosphere)
    ↓ ComponentOf
Level 1 (Humanity)
    ↓ ComponentOf
Level 2 (EU Union / DACH region)
    ↓ ComponentOf
Level 3 (Berlin / Germany)
    ↓ ComponentOf
Level 4 (Ruslan's personal life)
    ↓ ComponentOf (conceptually) / parallel-mount (physically)
Level 5 (Life-OS)
    ↓ ComponentOf
Level 6 (Jetix-OS)
    ↓ ComponentOf
Level 7 (Jetix-Sales-Function | Jetix-Revenue-Engine | Jetix-Delivery-Function)
    ↓ ComponentOf + creates
Level 8 (5 Ruslan atomic sub-roles | 11 agent roles | methodologies)
    ↓ creates
Level 9 (8 directions | 8 alphas instances)
    ↓ ComponentOf + PhaseOf (during lifecycle)
Level 10 (specific alpha state instances: "Müller GmbH Client.qualified")
```

**Materialized Phase 1:** Levels 5-10 (Life-OS folder-level separation +
Jetix filesystem structure).

**Reference-only:** Levels 0-4 (acknowledged, not directly operated on).

### 10.7 A.14 typed mereology edges applied (Section 3 reference)

See Section 3.5 for full A.14 edge catalog. Applied в `wiki/foundations/
jetix-creation-graph.md`.

**Compose-CAL (C.13) foundation** (per **FPF C.13**, L.36503):
Three canonical constructors:
- **`Γₘ.sum(parts)`** → whole (published alias: **ComponentOf**)
- **`Γₘ.set(elems)`** → collection (published alias: **MemberOf**)
- **`Γₘ.slice(entity, facet)`** → aspect (published alias: **AspectOf**)

Jetix uses Compose-CAL pragmatically через wiki/foundations/jetix-creation-
graph.md artifact.

### 10.8 FPF exclusions adopted

Per FPF A.1/A.14 stance — **actively excludes:**

From **CEM/GEM:**
- Unrestricted composition (only intentional, lifecycle-relevant).
- Extensionality as identity condition (holons change parts без losing
  identity).
- Flat "no preferred decomposition" stance (privileges partonomy).

From **Kit Fine:**
- Qua-objects (role-as-mask sufficient via C.3.4 RoleMask).
- Mereological coincidence as general principle.
- Full location pluralism.

From **academic:**
- BFO (Basic Formal Ontology) — explicitly rejected ailev/1451832.
- Van Inwagen's organicism — would deny non-biological composites.

### 10.9 Organizational applications (AGR model)

**For Jetix as OCMAS** (Organization-Centered Multi-Agent System):

**AGR model** (Ferber, Gutknecht, Michel, AAMAS 2003):
- **Agent** — individual autonomous entity.
- **Group** — collection sharing context.
- **Role** — abstract behavioral specification.

Jetix is **OCMAS** (not ACMAS) — role manifests define skeleton; specific
Claude models fill roles + replaceable.

⚠ Production cost note (per KB Section 7.5): Multi-agent systems use **~15x
more tokens** than chat. INT overhead coordinating parts. Holonic
decomposition justified only when parallelization gain outweighs
coordination cost.

**Jetix mitigation:**
- Full-FPF-Permeation (OT5) preloads ontology; reduces per-call overhead.
- UTS centralizes terminology; prevents drift cost.
- FPF-Steward quarterly audit catches drift early.
- Phase 1: 11 agents (not 30+); scale incrementally.

### 10.10 Compose-CAL foundation (C.13 future composition)

Per Rec **implicit** — C.13 Compose-CAL provides **foundations для future
composition** beyond Phase 1 3 constructors (sum/set/slice).

Phase 2b+ potential: Cross-direction composition patterns, multi-entity
federation (L7), BA-2 Panel composition.

### 10.11 Cross-refs

- **FPF A.1 Holonic Foundation** (L.1017)
- **FPF A.14 Advanced Mereology** (L.17478)
- **FPF C.13 Compose-CAL** (L.36503)
- **Леśniewski 1916**, **Lewis 1991**, **Fine 1999**
- **Koestler 1967**, **Wilber 1995**, **Mella**, **Jantsch**
- `wiki/foundations/holon-hierarchy.md` — full recursive structure
- `wiki/foundations/jetix-creation-graph.md` — 3-level A.14 typed graph

---

## Section 11 — 16 Trans-disciplines reference (Левенчук intellect-stack)

Per R-C research + KB Section 4 — **16** trans-disciplines (2023
canonical), not 17 (2021 retired version).

### 11.1 Concept of trans-discipline

**Левенчук definition** (ailev/1705503):
> «Дисциплины интеллект-стека называют часто трансдисциплинами, это
> 'дисциплины для рассуждения в ходе задействования прикладных дисциплин'
> (trans- — это 'находящиеся по ту сторону' от прикладных дисциплин).»

**Scale-freeness:** Применимы к elementary particles, организмам,
organizations, galactic structures equally.

### 11.2 16 trans-disciplines (bottom-to-top, 2023 canonical)

**Foundation layer (фундамент) — disciplines 1-5:**

1. **Понятизация (Conceptualization, figuring-out)** — discipline of
   isolating figures from background and naming them.
2. **Собранность (Sobrannost', Collectedness)** — holding objects в
   attention over time using exocortex. **Home of мышление письмом.**
3. **Семантика (Semantics)** — linking physical/real objects with
   mathematical/abstract/mental ones.
4. **Математика (Mathematics)** — abstract objects taxonomy, how behave,
   how constructed.
5. **Физика (Physics)** — physical objects modelling (including information
   theory since 2023).

**Formal reasoning layer — disciplines 6-9:**

6. **Теория понятий (Theory of Concepts)** — type system (classification,
   specialization, composition). "Машинка типов".
7. **Онтология (Ontology)** — multi-level meta-modeling; constructive
   ontology.
8. **Алгоритмика (Algorithmics)** — efficient computation; universal
   computers (human, classical, quantum).
9. **Логика (Logic)** — modes of computation-as-reasoning; inference,
   functional, probabilistic; includes cognitive biases.

**Knowledge-building layer — disciplines 10-11:**

10. **Рациональность (Rationality)** — creating correct explanations
    (causes, effects); rationality = explanations + decisions + actions.
11. **Познание / Исследования (Cognition / Research)** — Popperian critical
    rationalism applied как practice: conjectures + refutations.

**Coordination/communication layer — disciplines 12-14:**

12. **Эстетика (Aesthetics)** — style/elegance criteria for results of
    thinking. Applies to AI agents.
13. **Этика (Ethics)** — what goals/means acceptable. Includes systemic
    ethics, AI ethics.
14. **Риторика (Rhetoric)** — persuading agents to take actions.
    **Includes prompt engineering** for LLMs.

**Action/engineering layer — disciplines 15-16:**

15. **Методология (Methodology)** — scale-free teaching about agents'
    activities changing world. **Home of 5 primitives: роль / альфа /
    граф создания / стратегирование.**
16. **Системная инженерия (Systems Engineering)** — **2023 apex** —
    normatively prescribes how activities for creating systems should be
    structured.

### 11.3 Dependency graph (simplified)

```
Foundation:    Понятизация → Собранность → Семантика → Математика, Физика  [1-5]
Formal:        Теория понятий → Онтология → Алгоритмика → Логика           [6-9]
Knowledge:     Рациональность → Познание/Исследования                       [10-11]
Coordination:  Эстетика → Этика → Риторика                                  [12-14]
Action:        Методология → Системная инженерия                            [15-16]
```

Per R-C Section 3.2: true structure is **graph (lattice), not sequence**.
Linearization — pedagogical convenience.

### 11.4 Relation к 5 primitives

| Trans-discipline | Primary home of |
|------------------|-----------------|
| **Методология (15)** | ★★★ Роль, Альфа, Граф создания, Стратегирование |
| **Собранность (2)** | ★★★ Мышление письмом (как practice экзокортекса) |
| **Системная инженерия (16)** | Normative role system + canonical alphas |

Others 13 trans-disciplines provide foundational support.

### 11.5 Relation к FPF-Spec Parts A-K

⚠ **Critical note (per R-C):** FPF-Spec **does not mention** intellect-
stack explicitly. FPF Part C (Kernel Extension Specifications) concerns
**bounded-context reasoning tools** (logics, characterisation families),
не educational intellect-stack taxonomy.

**However** FPF-Spec Preface includes informative "Intellect Stack" section
(5 layers, not 16 disciplines):

| FPF Layer | Question | Patterns |
|-----------|----------|----------|
| 1 — Structure & Reality | What exists? | Kind-CAL, Sys-CAL |
| 2 — Knowledge & Reasoning | Why trust claim? | KD-CAL (F-G-R), Arg-LOG |
| 3 — Action & Execution | Intent → change? | Agent-CHR, Method-CAL, Resrc-CAL |
| 4 — Strategy & Rationality | Option under uncertainty? | Decsn-CAL |
| 5 — Governance & Purpose | Why act; what permissible? | Norm-CAL |

**⚠ FPF Preface stack is pedagogical projection.** Per FPF-Spec L.730:
"A full description of the Intellect Stack and its layers resides in the
Pedagogical Companion."

**For Jetix:** ШСМ 16 trans-disciplines = curriculum/competency frame;
FPF 5-layer stack = patterns map. **Different abstractions для разных
audiences** (не contradictory).

### 11.6 Jetix-specific subset — which trans-disciplines Jetix practitioners need

**Ruslan + agents + future hires core competencies Phase 1:**

**Essential (master):**
- 2. **Собранность** — daily practice (writing-as-thinking, экзокортекс
  discipline).
- 7. **Онтология** — core FPF competency (JETIX-FPF authoring, UTS
  maintenance).
- 10. **Рациональность** — Popperian discipline (conjectures + refutations
  в hypothesis management).
- 11. **Познание / Исследования** — portfolio research methodology.
- 15. **Методология** — 5 primitives + role-manifest authoring.
- 16. **Системная инженерия** — Jetix-as-product + client audits.

**Applied (functional):**
- 13. **Этика** — EU AI Act + GDPR compliance thinking; bias-audit.
- 14. **Риторика** — prompt engineering for all agents; client communication.
- 6. **Теория понятий** — type discipline (past-participle, U.Types).
- 9. **Логика** — reasoning validity; cognitive bias awareness.

**Foundational (implicit):**
- 1. **Понятизация**, 3. **Семантика** — через Собранность practice.
- 4. **Математика**, 5. **Физика** — implicit context for FPF abstractions.
- 8. **Алгоритмика** — implicit for compute/AI architecture choices.
- 12. **Эстетика** — code quality, artifact quality.

### 11.7 17 vs 16 — historical note

Per R-C Section 1.2 + KB Section 4.2:

- **Pre-2019 (STEM era):** Standard STEM. No "trans-discipline" framing.
- **2019:** Three-block ШСМ structure (6 proto-trans-disciplines).
- **Mid-2021 (6 trans-disciplines):** онтологика + коммуникации, научное
  мышление, etc.
- **August 2021 (16 levels):** "вместо 12 уровней стало 16" after splitting
  онтологика.
- **End-2021 (17 в Образование для образованных 2021):** added Труд
  (инженерия + менеджмент + предпринимательство).
- **2023 (16 в Интеллект-стек 2023):** Труд → Системная инженерия; added
  Математика + Физика; removed Экономика, Объяснения, Теория информации
  (last absorbed into Физика).

**For Jetix:** Use **16** always; note "historical 17" if referenced в
older Ruslan notes.

### 11.8 Cross-refs

- **Левенчук *Интеллект-стек 2023*** (ISBN 978-5-0060-4990-1)
- **Левенчук ailev/1705503, ailev/1579339**
- **R-C research** — full 16 disciplines deep mapping
- `wiki/foundations/trans-disciplines.md` (to be written Phase 1 post-D6)

---

## Section 12 — Full FPF Architectural Invariants (deep Левенчук)

Per Chunk 6 Area 6 Ruslan "max-depth stance" — include full FPF invariants,
не excluded. Each invariant: statement + Jetix implementation mapping.

### 12.1 Holonic trinity invariant (A.1)

**Statement:** U.Entity → U.Holon → {U.System, U.Episteme}.

All composition units are **U.Holon** (whole-and-part simultaneously). Every
change enacted by external transformer (A.12 Reflexive Split). U.System
(operational) separate от U.Episteme (passive knowledge).

**Jetix mapping:**
- Jetix itself = U.Holon (dual U.System + U.Episteme aspect).
- All 8 alphas = U.Holon instances.
- Wiki entries = U.Episteme (passive).
- Agents operational = U.System.

### 12.2 Transformer Quartet (A.3)

**Statement:** Four canonical types ground method execution:
- **U.System-in-Role** (bearer playing role).
- **U.MethodDescription** (recipe).
- **U.Method** (abstract way of doing).
- **U.Work** (record of occurrence).

**Jetix mapping:**
- `executor-binding.yaml` = U.System-in-Role.
- role.md Block 3 method_description_ref = U.MethodDescription.
- Shape Up, MECE, F.6 6-step = U.Method instances.
- `alphas/project/instances/<slug>.yaml` + Git commit log = U.Work.

### 12.3 Role-Method-Work Alignment (A.15)

**Statement:** Roles bind к Methods bind к Work records. Plan vs reality
never conflated. Only U.Work carries actuals.

**Jetix mapping:**
- 18 role-manifests bind (role ↔ method) via Block 3 primary_method.
- Work planning via quarterly OKR + weekly Shape Up → U.WorkPlan (A.15.2).
- Actual work logged in git + alpha state transitions → U.Work (A.15.1).
- Firewall: "who does what/how/when" → A.15, NOT mereology A.14.

### 12.4 11 Pillars (E.2)

**Statement** (per **FPF E.2** L.40148):

| ID | Pillar | Essence |
|----|--------|---------|
| **P-1** | Cognitive Elegance | Highlight decisive structure, eliminate ornamental formalism |
| **P-2** | Didactic Primacy | Human comprehension outranks theoretical purity |
| **P-3** | Scalable Formality | Artefact matures step-by-step (informal → formally assured) |
| **P-4** | Open-Ended Kernel | Kernel contains only meta-concepts; domain knowledge in patterns |
| **P-5** | FPF Layering | Patterns are modular declarative extensions |
| **P-6** | Lexical Stratification | Every concept expressible in 4 registers (plain/tech/U.Type/math) |
| **P-7** | Pragmatic Utility | Falsification rewarded over confirmation |
| **P-8** | Cross-Scale Consistency | Composition algebras invariant across material/knowledge/methods |
| **P-9** | State Explicitness | Every artefact declares state (design-time, run-time) |
| **P-10** | Open-Ended Evolution | Every entity expected to evolve indefinitely |
| **P-11** | State-of-the-Art Alignment | Kernel + extensions track contemporary knowledge |

**Precedence (per E.3):** Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did.

**Jetix mapping:**
- Every Jetix DRR (strategizing event artifact) must cite ≥3 pillars.
- D6 itself adheres: P-1 (dense), P-2 (Russian primary for clarity), P-3
  (formality F2 declared), P-4 (no domain-specifics bleeding), P-6 (UTS
  4-register), P-9 (frontmatter state: draft).

### 12.5 Four Guard-Rails (E.5)

**Statement** (per **FPF E.5** L.40487):

- **GR-1 (E.5.1) DevOps Lexical Firewall** — no domain-specific tokens
  (yaml, docker, CI/CD) в Core patterns. Applied: D6 Core refers Tooling
  by conceptual role; `wiki/foundations/fpf-tooling.md` companion holds
  DevOps specifics.
- **GR-2 (E.5.2) Notational Independence** — patterns expressible в
  multiple formalisms. Applied: UTS Layout A + Layout B, JETIX-FPF uses
  markdown + YAML but also legible в plain prose.
- **GR-3 (E.5.3) Unidirectional Dependency** — Core → Tooling → Pedagogy
  acyclic. Applied: D6 JETIX-FPF Core → `wiki/foundations/fpf-tooling.md`
  Tooling → Ruslan reading/learning notes Pedagogy (never reverse).
- **GR-4 (E.5.4) Cross-Disciplinary Bias Audit** — every pattern reviewed
  с lens diversity. Applied: FPF-Steward quarterly audit includes bias-
  audit cycle D.5 integration.

### 12.6 B.1 Γ Universal Algebra of Aggregation

**Statement (per FPF B.1):** Universal aggregation operator, defined ONLY
on sets of U.Holon. Six flavours:

| Flavour | Domain |
|---------|--------|
| **Γ_sys** | System-specific (mass, energy, resources) |
| **Γ_epist** | Knowledge-specific (provenance, trust) |
| **Γ_ctx** | Contextual (order matters) |
| **Γ_time** | Temporal (time-series, order-sensitive) |
| **Γ_method** | Order-sensitive method composition |
| **Γ_work** | Work as spent resource |

**Invariants preserved:** WLNK (weakest-link), MONO (monotonicity), IDEM
(idempotence), COMM (commutativity, except Γ_ctx/Γ_time), LOC (locality).

**Jetix mapping:**
- Revenue monthly — Γ_sys (sum of deal revenue).
- Knowledge wiki growth — Γ_epist (provenance-preserving).
- Weekly Shape Up plan — Γ_method (order matters).
- Monthly resource ledger — Γ_work.
- Attention-theme percentage — Γ_ctx (direction-ordered).

### 12.7 B.3 F-G-R Trust Calculus (+ CL)

**Statement (per FPF B.3** L.28201**):** Three components:
- **F (Formality)** — F0-F9 scale.
- **G (ClaimScope)** — set-valued scope где claim applies.
- **R (Reliability)** — evidence-bound warrant, weakest-link composition,
  pathwise justification.

Bridge-only reuse + CL penalties (Bridge-only → R only, never F or G).

**Jetix mapping:**
- Every ADR + client deliverable + agent output carries F-G-R frontmatter
  (per Gap 2 + Rec-04).
- Expected Jetix range: F0-F3 (rarely F4+).
- R-levels: R-low / R-medium / R-high / R-certified / R-formally-proven.
- FPF-Steward Q-audit includes F-G-R compliance check.

### 12.8 A.17-A.21 Characteristic Space (CSLC)

**Statement (per FPF A.17-A.21):** Formalism для characterization,
measurement, comparison, selection:
- **A.17 CHR-NORM** — Canonical Characteristic.
- **A.18 Minimal CSLC Kernel** — Characteristic ⟷ Scale ⟷ Level ⟷
  Coordinate.
- **A.19 CharacteristicSpace** + mechanisms (UNM / UINDM / USCM / ULSAM /
  CPM / SelectorMechanism).
- **A.20 Flow Constraint Validity**.
- **A.21 GateProfilization**.

**Jetix mapping (per Gap 3 + Chunk 8 adoption):**
- **SKU pricing CHR** (`decisions/policy/sku-pricing-chr.yaml`) — scales:
  hours-invested, deliverable-complexity, client-risk-tier, DACH-premium-
  factor. A.21 gate-profile acceptance criteria.
- **Direction kill criteria CHR** (`directions/_templates/kill-chr-
  template.yaml`) — 90-day revenue, pipeline-health, unit-economics, strategic-
  fit.
- **Agent promotion CHR** (`decisions/policy/agent-promotion-chr.yaml`) —
  **A.18 CSLC mandatory** (OQ-11 resolution).

### 12.9 A.6.B Boundary Discipline L/A/D/E

See Section 4.3. **FPF A.6.B Boundary Norm Square** (L.7097) — applied
proposal/contract/DPA templates.

### 12.10 D.5 Bias-Audit & Ethical Assurance

**Statement (per FPF D.5** L.39964**):** 4-stage cycle BA-0/BA-1/BA-2/BA-3.

**Jetix (per Rec-03 + Chunk 8):**
- Phase 1 simplified: BA-0 + BA-1 + BA-3 (solo Ruslan, no BA-2 Panel).
- BA-2 activation: Phase 2a (Beirat Ethics advisor).
- `decisions/policy/bias-audit-cycle.md` + templates.
- 5-class Bias Taxonomy: REP / ALG / VIS / MET / LNG.

### 12.11 E.17 Multi-View Publication Kit

See Section 4.4. **FPF E.17** (L.45107) — Viewpoint Bundle, 5 viewpoints
mandatory для Audit SKU.

### 12.12 F.17 Unified Term Sheet

See Section 8. **FPF F.17** (L.54586) — 30-50 rows concurrent с D6 writing
(OQ-08 B). **`wiki/foundations/jetix-uts.md`**.

### 12.13 B.2 Meta-Holon Transition (MHT)

**Statement (per FPF B.2** L.27444**):** When composition yields new coherent
whole с own boundary, objective, capabilities that **cannot be faithfully
treated as just parts folded together** → declare MHT.

**BOSC-A-T-X triggers:** Boundary / Objective / Structural / Capability /
Agency / Temporal / Context-rebase.

**Event taxonomy:** Fusion / Fission / Phase Promotion / Role-Lift /
Context Reframe.

**Jetix mapping (per Rec-06 + Chunk 8):** 4 MHTs documented
`decisions/policy/phase-transitions-mht.md`:
- **MHT-1:** Phase 1 → 2a (solo + hire) — trigger: Triple-AND.
- **MHT-2:** Phase 2a → 2b (team 5-20).
- **MHT-3:** Phase 2b → 2c (€10-50M, multi-entity, first acquisition).
- **MHT-4:** Phase 2c → 3 (€50M+, multi-entity federation).

Each MHT: from-holon / to-holon / trigger-conditions / emergence-signals /
re-identification (invariants + mutables) / transition-process / supervisor-
subholon-feedback.

### 12.14 E.9 DRR (Design-Rationale Record)

**Statement (per FPF E.9** L.41506**):** 4 conceptual components:
- Problem frame
- Decision
- Rationale
- Consequences

**Δ-classes:** Δ-0/Δ-1 (typos, clarity) → lightweight DRR; Δ-2/Δ-3
(semantic change) → full DRR.

**Jetix mapping:** Every strategizing event produces DRR
(`decisions/strategy/` or `decisions/adr/`). Every Chunk 8 adoption
decision was DRR-grade.

### 12.15 Cross-refs

- **FPF A.1, A.3, A.7-A.13, A.14, A.15, A.17-A.21, A.6.B**
- **FPF B.1, B.2, B.3, B.4, B.5**
- **FPF C.2, C.11, C.13, C.18, C.19**
- **FPF D.5**
- **FPF E.1, E.2, E.3, E.5, E.9, E.10, E.17, E.18**
- **FPF F.6, F.11, F.17**
- **FPF G.5**
- All ADR Chunk 8 cross-references в same ADR Section 8.9

---

## Section 13 — Constructor/Category Theory Applications (where applicable)

Per Chunk 6 Area 6 — "не excluded constructor/category theory, selectively
apply где реально enables better reasoning".

### 13.1 Category theory applications (pragmatic)

**Category theory** = mathematics of morphisms between objects. FPF uses
category-theoretic vocabulary selectively (notational, not foundational
per GR-2 Notational Independence).

**Applicable Jetix:**

- **Morphisms between epistemes** (A.6.2 U.EffectFreeEpistemicMorphing):
  Multi-View Publication Kit (E.17) morphisms from canonical artifact к 5
  views are **functorial projections** (per E.17 L.45107). Naturality
  property: view promotion commutes с arrow composition.
  - Jetix: canonical Audit artifact → Executive view; canonical →
    Technical view; etc. F-G-R preserved across views (up to CL
    penalties).

- **Transduction Graph (E.18 E.TGA):** typed, editioned directed multigraph
  whose vertices are morphisms and edges are typed transfers. Preserves
  CtxState = ⟨L, P, E⃗, D⟩ across raw transfers. Plane/Context/edition
  changes only at OperationalGate.
  - Jetix: decision pipeline от "Problem frame" (FormalSubstrate) →
    "Decision" (PrincipleFrame) → "Method Selection" (SelectionAndTuning)
    → "Implementation" (WorkPlanning + Work) → "Review" (EvaluatingAndRefreshing)
    — can be modeled as Transduction Graph.

### 13.2 Constructor theory applications (vocabulary-only, vague)

**Constructor theory** (Deutsch + Marletto 2012-present): meta-theory of
physics — possible vs impossible transformations (tasks). FPF imports
vocabulary, not physics foundations (per ailev/1776793).

**Applicable Jetix:**

- **Creation Graph depth** (3-level mereology) — creation systems create
  target systems = constructors performing tasks.
  - Jetix: Which tasks (Jetix deliverables) are **possible** given our
    current constructor (role-manifests + agents + methodologies)? Which
    **impossible** with current stack? → strategizing event trigger.

- **Compose-CAL (C.13)** 3 constructors (sum / set / slice) — explicit
  constructor-theoretic thinking about composition.

- **A.6.S Signature Engineering Pair** (per Rec-19) — Constructor +
  Target signature pair для SKU evolution. **Versioned SKU signatures**
  (v1 active для old clients + v2 для new).

### 13.3 Pragmatic stance (per E.5.2 GR-2)

Per **GR-2 Notational Independence** — JETIX-FPF patterns expressible в
multiple formalisms. Category theory / constructor theory are OPTIONAL
vocabularies, не locked-in dependencies.

**Rule:** Import exactly as much formalism as needed to solve specific
problem informal language cannot solve. No more. (Per KB Section 7.6
Левенчук middle path.)

**When to defer:**
- Full category theory apparatus (functors, natural transformations,
  monads) — defer к Phase 3 OR когда 50+ agents warrant formal
  composition reasoning.
- Full constructor theory as physics — skip permanently (FPF explicitly
  excludes).

### 13.4 Cross-refs

- **FPF A.6.2 U.EffectFreeEpistemicMorphing**
- **FPF C.13 Compose-CAL** (L.36503) — 3 constructors
- **FPF E.17 MVPK** (L.45107) — functorial multi-view projection
- **FPF E.18 Transduction Graph Architecture** (L.47502)
- **A.6.S Signature Engineering Pair** (L.15419) — per Rec-19
- **Deutsch + Marletto constructor theory literature**

---

## Section 14 — References + Cross-docs

### 14.1 FPF primary sources

- **FPF-Spec.md** — Anatoly Levenchuk + AI-agents, March 2026 version.
  62,202 lines, 5.7 MB. Vendored `raw/external/ailev-FPF/FPF-Spec.md`
  (commit 0a22129). Status: "Normative kernel, eternal alpha."
- **Readme.md** — entry routes + six canonical routes.
  `raw/external/ailev-FPF/Readme.md`.
- **ATTRIBUTION.md** — citation requested, no formal license.
  `raw/external/ailev-FPF/ATTRIBUTION.md`.
- **Upstream:** [github.com/ailev/FPF](https://github.com/ailev/FPF) — 320
  stars / 52 forks (April 2026).

### 14.2 FPF patterns cited in JETIX-FPF (verified line numbers)

All patterns verified against FPF-Spec.md via Grep/Read:

| Pattern ID | Name | Line | Section in D6 |
|------------|------|------|---------------|
| A.0 | NQD Onboarding | ~769 | Preamble |
| A.1 | Holonic Foundation | 1017 | 1.1, 1.2, 1.7, 10.7, 12.1 |
| A.1.1 | U.BoundedContext | 1202 | 1.1, 5.2 |
| A.2 | Role Taxonomy | ~1500 | 2.1, 5.1, 8.1 |
| A.2.1 | U.RoleAssignment | ~1600 | 2.1, 4.1, 8.1 |
| A.2.5 | U.RoleStateGraph | ~2100 | 5.5, 6.1 |
| A.3 | Transformer Quartet | ~1700 | 8.1, 12.2 |
| A.4 | Temporal Duality | ~7000 | 5.5 |
| A.6.0 | U.Signature | 8062 | 5.12 |
| A.6.B | Boundary Norm Square | 7097 | 4.3, 4.6, 5.8, 12.9 |
| A.6.C | Contract Unpacking | 7741 | 4.3 |
| A.6.H | Wholeness Unpacking | 15851 | 4.3 |
| A.6.P | Relational Precision | 10601 | 4.3 |
| A.6.Q | Quality Term Precision | 11326 | 4.1, 4.3 |
| A.6.S | Signature Engineering Pair | 15419 | 6.4, 13.2 |
| A.6.3.CR | Same-Entity Retextualization | 9521 | 4.4 |
| A.7 | Strict Distinction | ~16500 | 9.8 |
| A.8 | Universal Core | ~17000 | 8.2 |
| A.13 | Agential Role & Agency Spectrum | 17328 | 2.1, 5.12 |
| A.14 | Advanced Mereology | 17478 | 1.7, 3.1, 3.5, 3.7, 5.12, 9.4, 10.7, 12.1 |
| A.15 | Role-Method-Work Alignment | ~17200 | 3.5, 5.12, 12.3 |
| A.15.1 | U.Work | ~17250 | 6.6, 12.2 |
| A.15.2 | U.WorkPlan | ~17280 | 6.6, 12.2 |
| A.16 | PreArticulationCuePack | 18954 | Phase 1 Rec-17 integration |
| A.16.1 | PACK extension | 19549 | Rec-17 |
| A.17 | CHR-NORM | 20064 | 4.3, 12.8 |
| A.18 | Minimal CSLC Kernel | 20202 | 6.3.8, 12.8 |
| A.19 | CharacteristicSpace | 20359 | 12.8 |
| A.20 | Flow Constraint Validity | 24927 | 12.8 |
| A.21 | GateProfilization | 25224 | 12.8 |
| B.1 | Γ Universal Algebra | ~26000 | 3.1, 10.7, 12.6 |
| B.2 | Meta-Holon Transition | 27444 | 7.2 trigger, 12.13 |
| B.2.5 | Supervisor-Subholon Feedback | 28100 | 12.13 |
| B.3 | Trust & Assurance Calculus | 28201 | 4.2, 12.7 |
| B.4 | Canonical Evolution Loop | 29094 | 7.1, 7.6 |
| B.5.2 | Abductive Loop | ~29500 | 5.10.4 |
| B.5.2.0 | U.AbductivePrompt | ~29600 | 5.10.4, 8.1 |
| C.2.1 | U.EpistemeSlotGraph | 30495 | 6.6, 8.1 |
| C.2.2 | Reliability R | 31301 | 4.2 |
| C.2.2a | U.LanguageStateSpace | 31676 | 8.1 |
| C.3 | Kind-CAL | 33185 | 8.1 |
| C.11 | Decsn-CAL | ~35500 | 5.10.4 |
| C.13 | Compose-CAL | 36503 | 10.7, 10.10, 13.2 |
| C.18 | NQD-CAL | 37808 | 5.10.4, 6.3.5, 7.5 |
| C.18.1 | Scaling-Law Lens | 37919 | 7.5 BLP |
| C.19 | E/E-LOG | 38008 | 5.10.4, 6.3.5, 7.5 |
| C.19.1 | Bitter-Lesson Preference | ~38100 | 7.5 BLP |
| C.22 | Problem-CHR TaskSignature | 38734 | Phase 1 Rec-16 |
| D.5 | Bias-Audit & Ethical Assurance | 39964 | 4.3, 12.10 |
| E.1 | Vision & Mission | 40088 | Preamble |
| E.2 | Eleven Pillars | 40148 | 12.4 |
| E.3 | Principle Taxonomy & Precedence | 40264 | 12.4 |
| E.5 | Four Guard-Rails | 40487 | 12.5 |
| E.5.1 | DevOps Lexical Firewall | 40589 | Preamble, 8.5 |
| E.5.3 | Unidirectional Dependency | 40743 | Preamble |
| E.9 | DRR Design-Rationale Record | 41506 | 7.2, 12.14 |
| E.10 | LEX-BUNDLE | 41604 | 5.10.2, 8.1, 8.2, 8.3 |
| E.17 | Multi-View Publication Kit | 45107 | 4.4, 13.1 |
| E.17.0 | U.MultiViewDescribing | 43945 | 8.1 |
| E.17.1 | U.ViewpointBundleLibrary | 44325 | 4.4 |
| E.17.2 | TEVB | 44696 | 4.4 |
| E.18 | Transduction Graph Architecture | 47502 | 13.1 |
| E.20 | Mechanism Introduction Protocol | 48322 | Rec-20 |
| F.0.1 | Contextual Lexicon Principles | 48660 | 5.2 |
| F.1 | Domain-Family Landscape Survey | 49995 | 5.2 |
| F.4 | Role Description | 50333 | 5.6 |
| F.6 | Role Assignment Cycle | 50641 | 5.8 |
| F.7 | Concept-Set Table | 51194 | 8.1 |
| F.9 | Alignment & Bridge | 51539 | 5.2, 8.4 |
| F.9.1 | Bridge Stance Overlay | 52071 | 8.4 |
| F.11 | Method Quartet Harmonisation | 52604 | 7.3 |
| F.17 | Unified Term Sheet (UTS) | 54586 | 5.2, 8.1, 12.12 |
| G.5 | Multi-Method Dispatcher | 58316 | 7.4 |
| J.4 | First Practical Entry Route Index | 62110 | 14.5 |
| K | Lexical Debt & Mandatory Replacements | 62123 | 8.5 |

**Total verified patterns: ~60+.**

### 14.3 Jetix cross-references (D1-D9 internal)

- **D1** JETIX-ARCHITECTURE-FINAL — 15-20 pages; 8 principles (Section 3
  this doc); 7-layer Reference + 4-layer Phase 1 Operational (Section 1.5).
  Post-Chunk 8: Nested Holonic Structure terminology; directions с
  C.18/C.19; Bridges + CL.
- **D2** JETIX-FOLDER-STRUCTURE — 15 Phase 1 folders + Life-OS/shared
  layouts + per-direction ee-log/nqd/kill-chr.
- **D3** JETIX-ROLE-MANIFESTS — 18 full-depth 5-block role.md + executor-
  bindings с agency-profile (Rec-08) + F.6 cycle (Rec-15) + agent_onboarding
  + compute-contract.
- **D4** JETIX-VS-LIFE-OS — separation principle; MHT-1 trigger (this doc
  Section 12.13).
- **D5** JETIX-KNOWLEDGE-ARCHITECTURE — 3-layer model; 8 alpha state
  machines (Section 6 this doc); 25K exocortex reservation; **A.14 typed
  edges** (Section 3.5 this doc); UTS central reference (Section 8.1).
- **D6** JETIX-FPF — **this document**.
- **D7** JETIX-CAREER-LEVELS — J0-JX reference + J-Auto/Approve/Strategic;
  AI promotion external-review + **A.18 CSLC formal** (OQ-11; Section 12.8).
- **D8** docs/INSTRUCTIONS — 7+10-14 rollout + 4 rituals (B.4 Evolution
  Loop framed; Section 7.1) + tool stack + cost model + triggers.
- **D9** Jetix Architecture Final Decision Record — `decisions/2026-04-20-
  jetix-architecture-final-DRAFT.md` v0.6.

### 14.4 Primary supporting Jetix artifacts (Phase 1 post-D6)

**Wiki foundations:**
- `wiki/foundations/jetix-creation-graph.md` — 3-level A.14 typed graph.
- `wiki/foundations/jetix-uts.md` — 30-50 rows UTS (Gap 4, concurrent).
- `wiki/foundations/fpf-tooling.md` — Rec-13 companion (Core/Tooling split).
- `wiki/foundations/jetix-innovations.md` — 9 innovations catalog (Chunk 8
  Section 6).
- `wiki/foundations/shsm-primitives.md` — 5 primitives deep reference.
- `wiki/foundations/holon-hierarchy.md` — full recursive structure.
- `wiki/foundations/trans-disciplines.md` — 16 disciplines full reference.

**Policy docs (per Chunk 8):**
- `decisions/policy/boundary-discipline.md` (Gap 1)
- `decisions/policy/trust-tagging.md` (Gap 2)
- `decisions/policy/sku-pricing-chr.yaml` (Gap 3)
- `decisions/policy/agent-promotion-chr.yaml` (Gap 3)
- `decisions/policy/characteristic-space-conventions.md` (Gap 3)
- `decisions/policy/mereology-edge-types.md` (Rec-05)
- `decisions/policy/phase-transitions-mht.md` (Rec-06)
- `decisions/policy/bias-audit-cycle.md` (Rec-03)
- `decisions/policy/mechanism-introduction.md` (Rec-20)
- `decisions/policy/multi-method-dispatcher.md` (Rec-21)

**Templates:**
- `decisions/templates/jetix-viewpoint-bundle.yaml` (Gap 5)
- `decisions/templates/audit-canonical-template.md` (Gap 5)
- `decisions/templates/views/` — 5 view templates
- `decisions/templates/client-intake-problem-chr.yaml` (Rec-16)
- `decisions/templates/kill-chr-template.yaml` (Gap 3)
- `decisions/templates/mht-template.yaml` (Rec-06)
- `decisions/templates/bias-audit/` — 3 templates (BA-0, BA-1, BA-3)

**FPF Stewardship:**
- `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` — first Q2 2026
  audit (Rec-22).

### 14.5 Levenchuk primary sources (Russian)

- **Левенчук A. "Системное мышление 2024"** — 2-volume, 9th major rewrite,
  ISBN 978-5-0064-2853-9 / 978-5-0064-2855-3.
- **Левенчук A. "Методология 2025"** — ~872 pages.
- **Левенчук A. "Интеллект-стек 2023"** — ISBN 978-5-0060-4990-1.
- **Левенчук A. "Системная инженерия 2022"**.
- **Левенчук A. "Инженерия личности 2023"**.

**arXiv (English):**
- ["Towards a Systems Engineering Essence" (2015)](https://arxiv.org/abs/1502.00121).
- ["Toward an Ontology for Third Generation Systems Thinking" (2023)](https://arxiv.org/abs/2310.11524).

**Online:**
- Blog: [ailev.livejournal.com](https://ailev.livejournal.com) ("Лабораторный журнал").
- МИМ: [system-school.ru](https://system-school.ru), [aisystant.system-school.ru](https://aisystant.system-school.ru).
- Community: [systemsworld.club](https://systemsworld.club).

**Key Левенчук posts cited:**
- ailev/1776793 — mereology + holons + role-as-mask.
- ailev/1795494 — founder syndrome critique + agents не strategize.
- ailev/1769411 — LLM writing-as-thinking warning.
- ailev/1741032 — role/method relationship.
- ailev/1579339 — 16 trans-disciplines evolution history.
- ailev/1451832 — BFO rejection rationale.
- ailev/1705503 — trans-discipline definition.

### 14.6 J.4 entry routes (navigational reference)

Per **FPF J.4** (L.62110) — 6 canonical first-practical entry routes:

1. **Project alignment** — role/method/plan/work confusion → F.11 (Method
   Quartet) + A.15 + F.17 UTS.
2. **Partly-said / language-state discovery** — preserve cue without claiming
   endpoint → A.16 PreArticulationCuePack.
3. **Boundary unpacking** — contract mixing law/gate/duty/evidence → A.6.B
   L/A/D/E.
4. **Lawful comparison / selected-set publication** — compare options → A.17-
   A.19 CSLC + G.5 Multi-Method Dispatcher.
5. **Generator / SoTA / selector / set-surface scaffold** — reusable
   generator/selector → G.0-G.5 + C.18 NQD + C.19 E/E-LOG.
6. **Same-entity rewrite / explanation / comparative reading** — re-explain
   object без minting semantic track → A.6.3.CR + E.17 MVPK.

**Jetix entry-route usage Phase 1:**
- Route 1 — Role-manifest design (D3 writing).
- Route 3 — Contract/DPA template Day 5-6 (Gap 1 adoption).
- Route 4 — SKU pricing + direction kill + agent promotion (Gap 3 adoption).
- Route 6 — Multi-View Publication (Gap 5 adoption).

### 14.7 Reference research (Perplexity 5 waves, 2026-04-20)

- **R-A** — `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-
  full-body-of-work.md` — Левенчук intellectual context.
- **R-B** — `R-B-shsm-5-primitives-deep.md` — 5 primitives deep dive.
- **R-C** — `R-C-17-trans-disciplines-mapping.md` — 16 (née 17) disciplines
  enumeration.
- **R-D** — `R-D-essence-kernel-shsm-relation.md` — SEMAT Essence origin +
  Левенчук adaptation путь.
- **R-E** — `R-E-mereology-holon-hierarchy.md` — mereology theory + holons.

### 14.8 Consolidated ADR / decision trail

- **Stage 3 ADR** (Chunks 1-7 approved 2026-04-19 to 2026-04-20 + Chunk 8
  same-day append):
  `decisions/2026-04-19-architecture-v2-approval.md`.
- **Gap Analysis tracking**: `decisions/gap-analysis-review-decisions-
  2026-04-20.md` (60+ decisions).
- **Notion mirror**: <https://www.notion.so/3482496333bf8174a7ffd6f30c02f0bf>.
- **D9 Draft v0.6**: `decisions/2026-04-20-jetix-architecture-final-DRAFT.md`
  (regenerated from v0.5 commit 110413a).

### 14.9 Attribution (formal)

**JETIX-FPF — Jetix-specific adaptation of First Principles Framework (FPF)
by Anatoly Levenchuk ([github.com/ailev/FPF](https://github.com/ailev/FPF)).
Upstream repo has no formal license; citation explicitly requested and
provided. Internal Jetix use с adaptation. No contribute-back (per OQ-09 A
hard stance).**

**Semi-annual FPF upstream sync reminder** (OQ-10 C modified): every 6
months (Q2 close + Q4 close) — FPF-Steward flags "upstream FPF sync review
due". Ruslan manual decision whether to sync.

---

**END OF JETIX-FPF v1.0**

*Written 2026-04-20 by Claude Opus 4.7 (1M context) orchestration: 3
parallel FPF Scholar subagents (Parts A-B / C-E / F-K) + Verifier subagent.
Stage A complete per Hybrid Ultimate V5 methodology. Unblocks Stage B (4
parallel perspective reviews) + Stage 4 D1/D2/D3/D4/D5/D7/D8 writing.*
