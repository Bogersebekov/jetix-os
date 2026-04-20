---
id: JETIX-FPF
title: Jetix First Principles Framework — Constitutional Document
subtitle: Jetix-specific adaptation of First Principles Framework (FPF) by Anatoly Levenchuk
date: 2026-04-20
version: v2.0
previous-version: v1.0 (commit 2a41927)
state: draft-synthesized (awaiting Stage D verification)
synthesized-from:
  - v1 Stage A (commit 2a41927)
  - Reviewer 1 Левенчук Purist critique (commit a4cfac2)
  - Reviewer 2 DACH Compliance critique (commit 8dd5420)
  - Reviewer 3 AI-Agent Designer critique (commit 0e15f52)
  - Reviewer 4 Enterprise Reader critique (commit 582450b)
structural-decision: Option C (hybrid) — D6 keeps deep ontology core (Sections 1-9, 12-14) + Jetix application of mereology (10.6-10.11) + trans-discipline Jetix-subset (11.6); academic lineage material (10.1-10.5, 11.3-11.5, 11.7) compressed in-place with pointers к wiki/foundations/ companions. Preserves Ruslan "max Левенчук depth" hard requirement через companion files; restores constitutional-doc clarity per R4 readability critique.
conflict-resolution-ranking: ontology-fidelity > reader-clarity > compliance > ai-agent-operational (per Stage C prompt; R1 wins direct conflicts)
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
language-policy: >
  D6 itself RU-primary (Ruslan-Claude working language). Левенчук verbatim
  quotes bilingual format (RU original + EN translation). German-native hires
  route: read §0 + §0.5 + §2 + §4 + §6 + §7 first (EN sections); §5/§9/§11
  require translation aids. Client-facing artifacts DE-primary per CP-1.
  Sister artifact design/JETIX-FPF-BRIEF.md (EN-only, 5-8 pages, Phase 1 ETA)
  planned для external audiences.
scope: internal-only (per OT5 + OQ-09 A)
status: draft-synthesized v2.0 (unblocks Stage 4 D1/D2/D3/D4/D5/D7/D8 writing after Stage D verify)
formality: F2
reliability: R-medium
claim-scope: jetix/methodology/constitutional
---

# JETIX-FPF — Jetix First Principles Framework (Constitutional Document v2.0)

---

## §0 — Jetix in 90 seconds (plain language)

**What Jetix does.** Jetix is a solo-founder-plus-AI-agents consultancy
focused on DACH Mittelstand AI-audit services. One founder (Ruslan,
Berlin) collaborates with 11 Claude-agents across 6 internal departments
to deliver AI governance audits, research, and advisory work to
€10M-€500M revenue companies in Germany/Austria/Switzerland.

**What this document does.** JETIX-FPF is the **constitutional document**
of Jetix OS — it fixes the vocabulary, roles, lifecycles, decision-
authorities, and quality-gates used throughout the business. Every role
manifest, every agent system prompt, every client contract, every
strategic decision references this document as the source-of-truth for
"what counts as a client", "what states a project can be in", "who is
authorized to decide what", and "how we prove our work is trustworthy".

**Why this document exists.** Without a single constitutional anchor, a
multi-agent AI business drifts — each agent invents its own vocabulary,
each contract mixes categories, each decision loses its rationale.
JETIX-FPF freezes the shared conceptual backbone so the business scales
coherently from Phase 1 (solo + 11 agents) к Phase 2+ (team 5-20) к
Phase 3 (multi-entity federation).

**Where the depth comes from.** JETIX-FPF adapts the **First Principles
Framework (FPF)** by Anatoly Levenchuk ([github.com/ailev/FPF](https://github.com/ailev/FPF),
March 2026, ~62K lines of pattern language). FPF supplies a vocabulary
for coordinating complex multi-actor work; JETIX-FPF specializes it for
AI-native DACH consulting. Internal-only adaptation (per OQ-09 A); no
contribute-back upstream.

---

## §0.5 — Reader routes (which sections should you read?)

| Audience | Priority sections | Est. time | Skip-for-now |
|----------|-------------------|-----------|--------------|
| **Investor / Aufsichtsrat** | §0 + §1 + §4 + §6 (overview) + §12.13 MHT + §12.6bis "defensible moat" | ~45 min | §8, §10 (academic), §11 (trans-disciplines) |
| **First hire — Sales Lead (DACH-native)** | §0 + §0.5 + §2 + §4 + §6 + §7 | ~2 hours | §5 deep, §10, §11; return to these after onboarding |
| **Enterprise client (Geschäftsführer)** | §0 + §4 Client Principles + §4.4 Multi-View + §4.5.1 EU AI Act tier | ~15 min | everything else (defer к DE executive brief Phase 1) |
| **AI agent booting up** | §0 + full doc per assigned loading tier (see §5.4a) | Session init | Tier 3 agents: reference-only с on-demand section fetch |
| **External DPO / compliance auditor** | §0 + §2.3 DPO triggers + §4.3 L/A/D/E + §4.5 CP-5 + §4.5.1 EU AI Act matrix + §9 incident response + §12.10 bias-audit | ~1 hour | §10, §11, §13 |
| **Internal team member (Ruslan, agents, methodology authors)** | Full document | ~3-4 hours | nothing |
| **FPF-Steward quarterly audit** | Full document + §14 references | ~4-6 hours | nothing; this is the scope |

### Navigation principles

- **Ontological core** (must-read for anyone authoring role-manifests or
  decisions): §1 Target System, §2 Stakeholders, §3 Creation Graph,
  §5 Internal Principles, §6 Alphas, §12 Invariants.
- **Client-facing** (must-read before any client interaction): §4 Client
  Principles, §4.4 Multi-View Publication, §4.5 CP-5 Human Gate, §4.5.1
  EU AI Act Matrix, §7 Rituals.
- **Operational** (must-read before agent boots or hire starts): §0.7
  Glossary, §2.1 Agency-CHR, §5.4a Per-agent loading tier, §5.8
  Onboarding, §5.9 Role-switching prevention.
- **Deep background** (read-once, then reference): §8 U-Types,
  §10 Mereology, §11 Trans-disciplines, §13 Constructor theory.

---

## §0.7 — Quick Glossary (12 essential terms before §1)

| Term | Plain-English | Reference |
|------|---------------|-----------|
| **FPF** | First Principles Framework (Левенчук, ~62K lines) — upstream parent methodology | §14.1 |
| **JETIX-FPF** | Jetix-adapted FPF (this document) — internal only | Preamble |
| **Holon** | Something that is simultaneously a whole (has its own boundary) and a part (nested inside larger wholes). Koestler 1967. | §1.1, §10.5 |
| **U.Type** | A "universal kind" — kernel-level concept like U.Role, U.System, U.Episteme. Capital-U prefix = FPF-canonical Kernel concept. | §8.1 |
| **Alpha** | A thing whose lifecycle we track via explicit past-participle state machine (e.g., Client goes `lead-identified` → `qualified` → `won`). 8 alphas in Jetix Phase 1. | §6 |
| **Creation Graph** | 3-level directed mereological graph showing who creates what where: target systems / creation systems / supersystems. | §3 |
| **Direction** | Portfolio-of-directions pattern (Jetix innovation) — a revenue bet with its own hypothesis, kill criteria, and lifecycle. 8th alpha. | §6.3.8 |
| **L/A/D/E** | Contract lane discipline: Laws / Admissibility / Deontics / Effects. Prevents category-mixing in client deliverables. (FPF A.6.B) | §4.3 |
| **F-G-R** | Trust tagging triad: Formality (F0-F9), claim-Scope (G), Reliability (R-low/medium/high/certified). Surfaced on every deliverable. | §4.2, §12.7 |
| **J-level** | Career/authority level of a role: J-Auto (autonomous execution), J-Approve (requires sign-off), J-Strategic (founder-only). See D7 for matrix. | §2.2, §5.12 |
| **MHT** | Meta-Holon Transition — phase change where composition yields genuinely new coherent whole (e.g., solo→team, team→multi-entity). 4 MHTs планируются. | §12.13 |
| **Γ** | Universal aggregation operator — how wholes compose from parts (revenue aggregation, knowledge aggregation, method composition). 6 flavours. | §12.6 |

Full 33-row U-Types table в §8.1. Full JETIX-UTS 30-50 rows в `wiki/foundations/jetix-uts.md` (concurrent Phase 1 write).

---

## §0.9 — Document Table of Contents

1. [§1 — Target System (Jetix as holon)](#section-1--target-system-jetix-as-holon)
2. [§2 — Stakeholders](#section-2--stakeholders)
3. [§3 — Creation Graph (3-level mereological)](#section-3--creation-graph-full-3-level-mereological-mc3-override)
4. [§4 — Client Principles (CP-1..CP-5 + EU AI Act tier matrix)](#section-4--client-principles)
5. [§5 — Internal Principles (IP-1..IP-8 + ШСМ 5 foundational concepts)](#section-5--internal-principles-8-principles--шсм-5-primitives)
6. [§6 — 8 True Alphas](#section-6--8-true-alphas-with-a14-typed-mereology)
7. [§7 — Ritual Cadence + Strategizing as Event](#section-7--ritual-cadence--strategizing-as-event)
8. [§8 — U-Types Full (Deep Левенчук treatment)](#section-8--u-types-full-deep-левенчук-treatment)
9. [§9 — "What ШСМ is NOT" (protection section)](#section-9--what-шсм-is-not-protection-section-expanded)
10. [§10 — Mereology + Holon Hierarchy (Jetix application + companion pointer)](#section-10--mereology--holon-hierarchy-jetix-application)
11. [§11 — 16 Trans-disciplines (Jetix-subset + companion pointer)](#section-11--16-trans-disciplines-jetix-subset--companion-pointer)
12. [§12 — Full FPF Architectural Invariants](#section-12--full-fpf-architectural-invariants-deep-левенчук)
13. [§13 — Constructor/Category Theory Applications](#section-13--constructorcategory-theory-applications-where-applicable)
14. [§14 — References + Cross-docs](#section-14--references--cross-docs)

---

## Preamble — For methodology authors (depth context)

> *Максимальная глубина + качество, на 100%. Никаких compromises. Всё что
> применимо из FPF — внедряем. Стратегический курс как с 11 overrides —
> +Левенчук direction.* — Ruslan, 2026-04-20
>
> **[EN translation]** *Maximum depth and quality, 100%. No compromises.
> Everything applicable from FPF — we incorporate. Strategic course held
> with the 11 overrides — plus Levenchuk direction.*

JETIX-FPF — конституционный документ Jetix OS. Он описывает **онтологический
каркас** в котором оперирует каждая роль, агент, альфа, direction, client-
relationship и management ritual компании. Источник первичный — **First
Principles Framework (FPF)** Анатолия Левенчука
([github.com/ailev/FPF](https://github.com/ailev/FPF)), март 2026, 62,202
строки pattern language'а (FPF **E.1 Vision & Mission**, FPF-Spec L.40088).
Jetix-адаптация **"JETIX-FPF"** — специфическая для нашего business-context
и AI-native реальности, но с максимальной fidelity Левенчуковской онтологии.

### Role в архитектуре

D6 — **primary reference** для всех 18 role-manifests. Агенты загружают
текст D6 в system.md **через tiered loading** (per §5.4a, не full-text
uniformly — per AI-Agent Designer cost critique integrated Stage C). D6 —
основа для D1 (Architecture Final), D3 (Role Manifests), D5 (Knowledge
Architecture), D7 (Career Levels), D8 (Instructions). **Это primary
methodology reference** (v1 slogan "sacred text" retired per Enterprise
Reader critique — overstatement).

### Scope stance

**Internal-only hard** (per OT5 + OQ-09 A). Ruslan explicit 2026-04-20:
> «всё держим, ничего никуда не отправляем, нигде не публикуем.»
>
> **[EN translation]** *"We keep everything, send nothing anywhere,
> publish nowhere."*

Semi-annual FPF upstream sync reminder (OQ-10 C modified) — Q2 close и Q4
close FPF-Steward flags "upstream sync review due"; Ruslan manual decision.

### What reader will find here

14 sections + §0..§0.9 reader-orientation block. ~40-50 pages. Constitutional
depth. Max Левенчук fidelity, with academic-lineage material externalized
to `wiki/foundations/` companions (per Option C hybrid Stage C structural
decision). Full 8 true alphas, Nested Holonic Structure (**FPF A.1 +
A.14**), Boundary Discipline (**FPF A.6.* family**), Trust & Assurance
(**FPF B.3** F-G-R triad), Characteristic Spaces (**FPF A.17-A.21**), UTS
(**FPF F.17**), Multi-View Publication (**FPF E.17**), Eleven Pillars
(**FPF E.2**), Four Guard-Rails (**FPF E.5**), plus Jetix-specific innovations
(Portfolio-of-Directions, FPF-Steward sub-role, 4-tier Resource Accounting,
tiered Full-FPF-Permeation).

### What reader will NOT find here

- **Tooling specifics** (YAML schemas, git commit conventions, CLI flags).
  Уходят в companion: `wiki/foundations/fpf-tooling.md` (per Rec-13 + OQ-07
  C soft split; **FPF E.5.1 DevOps Lexical Firewall** + **E.5.3
  Unidirectional Dependency**).
- **Pure academic-lineage expansion** (mereology Leśniewski→Lewis→Fine,
  trans-discipline 17-vs-16 history, full Koestler/Wilber treatment).
  Уходят в отдельные foundations artifacts: `shsm-primitives.md`,
  `trans-disciplines.md`, `holon-hierarchy.md`, `jetix-creation-graph.md`
  (Option C hybrid — depth preserved в companions, clarity restored in D6).
- **Implementation roadmap** (Phase 1 Day 1-14 rollout schedule). Уходит
  в D8 (Instructions).
- **Policy documents operational detail** — D6 references policies; full
  content в `decisions/policy/*.md` per §14.4 ETA schedule.

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

Stakeholders = U.RoleAssignment instances (FPF **A.2.1**, FPF-Spec
L.1613, per Role Taxonomy family L.1403-5465) — holders occupying roles
в bounded contexts с committed obligations.

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

**Agency profile** (per Rec-08 **FPF A.13:4.3 Agency-CHR** fallback):
Ruslan default agency 1.0 (founder full-stack); agents default 0.4 with
override per decision class (see §2.1a canonical schema).

**Left-hand rule** (Jetix custom, not FPF canonical): При conflict между
sub-roles, **strategy-lead** имеет meta-authority (analogous к Левенчук's
meta-method стратегирование selecting which sub-method dominates).

### 2.1a Agency-CHR canonical schema + storage (P1-R3-4 resolution)

**Canonical storage location decision** (per Stage C synthesis):
**Option D hybrid** (defaults in policy, per-binding overrides in executor-
binding):
- `decisions/policy/agent-promotion-chr.yaml` — **default matrix per role**
  (authoritative).
- `executors/<id>/executor-binding.yaml` — `agency_profile:` block
  **overrides defaults per-holder instance**.

Other 3 locations considered (`agents/<id>/agency-chr.yaml`, inline-in-
executor-binding as sole source, separate `agency-chr.yaml` без policy
defaults) — rejected because either (a) creates N different sources of
truth when holder/role combinations grow, or (b) loses role-level policy
authority needed for FPF-Steward quarterly audit.

**Canonical schema (v1 Phase 1):**

```yaml
# decisions/policy/agent-promotion-chr.yaml (default CHR by role)
version: v1
authoritative: role-level defaults (binding overrides in executor-binding.yaml)
dimensions:
  bmc: Boundary Maintenance Capacity (0.0-1.0)
  ph:  Predictive Horizon (0.0-1.0, 0 = <1day / 1 = >quarter)
  mp:  Model Plasticity (0.0-1.0)
  per: Policy Enactment Reliability (0.0-1.0)
  oc:  Objective Complexity (0.0-1.0)
default_by_role:
  strategy-lead:   # Ruslan sub-role
    bmc: 1.0; ph: 1.0; mp: 0.8; per: 1.0; oc: 1.0
    agency_grade: 4  # "Strategizing" per FPF A.13:4.4
  sales-lead:      # agent role
    bmc: 0.6; ph: 0.5; mp: 0.3; per: 0.7; oc: 0.5
    agency_grade: 2  # "Operating"
  manager:
    bmc: 0.7; ph: 0.4; mp: 0.2; per: 0.8; oc: 0.4
    agency_grade: 2
  strategy-support-analyst:
    bmc: 0.5; ph: 0.7; mp: 0.1; per: 0.6; oc: 0.8
    agency_grade: 3  # "Adaptive" per FPF A.13:4.4
  # ... (other 8 roles filled Phase 1 Day 5-7 in policy doc)
promotion_rules:
  promote_to_j_strategic:
    ruling: "never for AI agents (hard rule per §5.10.4)"
    exception: "Ruslan only"
  promote_to_j_approve:
    threshold:
      bmc: ">= 0.5"
      per: ">= 0.6"
      evidence_tasks_passed: ">= 10"
evidence_ref_requirement:
  phase_1_bootstrap: "R-low acceptable; evidence_ref: pending OK для Day 1"
  phase_2a_and_beyond: "R-medium minimum; evidence_ref must cite concrete task-log artifact (per FPF CC-A13.3)"
task_family_overrides:
  # Per FPF A.13:4.3.1 — context-bounded task-family specialization
  # Per-agent override when same holder has diff reliability по task-family
  sales-lead:
    - task_family: discovery-call
      bmc: 0.8  # higher reliability in discovery
    - task_family: de-contract-negotiation
      bmc: 0.2  # low reliability — German-language contract requires escalation
      per: 0.3
```

**Per-holder override syntax** (excerpt `executors/sales-lead/executor-
binding.yaml` — full example §5.8.1):

```yaml
agency_profile:
  inherit: decisions/policy/agent-promotion-chr.yaml#default_by_role.sales-lead
  overrides:
    - decision_class: outbound-email-draft
      bmc: 0.7  # overrides role default 0.6
    - decision_class: discount-above-10-pct
      bmc: 0.0  # must escalate
  bmc: 0.6  # explicit repeat of inherited (for audit clarity)
  ph: 0.4   # smaller predictive horizon than role-default (holder-specific)
  evidence_ref: decisions/fpf-stewardship/2026-Q2-agency-chr-bootstrap.md
```

**Phase 1 Day 1 bootstrap caveat (per FPF CC-A13.3 pre-compliance):**
Initial profiles labeled `R-low, evidence_ref: pending` acceptable for
Day-1 boot; FPF-Steward Q2 2026 audit scope includes populating
`evidence_ref:` from actual task-logs (see §5.4 FPF-Steward audit items).

**Per-task-family Agency-CHR discipline** (per FPF A.13:4.3.1 context-
bounded specialization) — same holder may have different BMC/PH/PER in
different task-families (e.g., sales-lead high-reliability in discovery-
calls, low in German-language contract-negotiation). Overrides section
above operationalizes this; D3 role-manifest authors must enumerate
decision-classes per role.

### 2.2 11 Claude agents (L2 Cognitive + L0 support)

Per ADR Chunk 6 Area 3 + D3:

| # | Agent | Dept | Model | Primary J-level* |
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

> **\* J-level dimensionality note (P1-R3-2 resolution):** This table shows
> each agent's **primary (global default) J-level**. Real operational
> authority is **2D: agent × decision-category × J-level**. Per-category
> granular matrix lives в D3 role-manifests Block 5 `autonomous:` /
> `approve_required:` / `never:` enumerations, with D7 Career Levels
> documenting promotion-path transitions across J-levels. Example for
> sales-lead: `draft-proposal` = J-Auto; `discount 0-10%` = J-Approve;
> `discount >10%` = J-Strategic; `sign-contract` = J-Strategic (founder
> only). D3 role.md Block 5 MUST enumerate decision-classes per role;
> this D6 table is the primary-bucket header, not the full specification.

**Ground-truth reconciliation (P1-R3 ground-truth findings):** Agent IDs
in D6 §2.2 table are canonical; `shared/schemas/message.schema.json` enum
MUST match (e.g., v2 uses `sales-research` not `sales-researcher`;
`strategy-support-analyst` not `strategist`; `life-coach` removed from
Jetix namespace per §1.3). Schema update is Phase 1 Day 1 task (per D8
rollout) — **blocker для inter-agent message validation**.

**Role ≠ Executor strict** (IP-1) — каждый agent — `executor-binding.yaml`
bound к defined role.md. Holder (agent instance) может change (Claude
Haiku 4.5 → Haiku 5.x upgrade) — role remains stable. **Agency-CHR
fallback** (Rec-08 **FPF A.13:4.3**) per-binding (schema §2.1a).

### 2.2a Coordination principles (P1-R3-6 addition)

Multi-agent coordination primitives — constitutional level (implementation
detail в D8):

1. **Hub-and-spoke discipline** (per CLAUDE.md global rule #8): subagents
   report к Department Lead, not Manager. Manager attention budget: max
   20 active tasks. No skip-level unless escalation (classified как
   `escalation` type message). Structural pattern matches **FPF A.2.5
   U.RoleStateGraph** supervisor-subordinate semantics при A.14
   `ComponentOf` edges between role-department-function levels.
2. **Message schema** — all agent-to-agent messages follow
   `shared/schemas/message.schema.json`. Canonical `type:` enum:
   `task` / `result` / `question` / `escalation` / `notification` /
   `handoff`. Each message carries **`acting_as:` field** (per P1-R3-3
   enforcement mechanism — see §5.9) binding message к sender's current
   role.
3. **Escalation taxonomy** — `dept-internal` (stays within dept-lead) /
   `cross-dept` (routes через manager) / `strategic` (routes к Ruslan
   strategy-lead sub-role) / `safety` (routes к meta-agent + Ruslan
   immediately — halts current task).
4. **Async default, sync only at named synchronous points** — default
   all inter-agent коммуникация async (mailbox-polling). Synchronous
   blocking only at: proposal-signing (sales-closer ↔ Ruslan), client
   deliverable acceptance (acceptance-authority), bias-audit BA-3
   closure (per §12.10), trigger-driven strategizing event convening
   (per §7.2).
5. **Stale-dependency timeout** — if `depends_on_roles:` target не
   responds в 48h business hours → dependent agent emits `escalation`
   type message к department lead; proceeds с stale data only if flagged
   `R-low` in output F-G-R tag.
6. **Ground-truth sync invariant** — `shared/schemas/message.schema.json`
   agent-ID enum ← D6 §2.2 table ← `executor-binding.yaml` role_ref.
   If divergence detected (FPF-Steward Q-audit item) — schema is
   regenerated from D6 authoritative table.

### 2.3 Future human hires (Phase 2a+)

### 2.3 Future human hires (Phase 2a+)

Stub role-manifests Phase 1 (per MC1 + Area 3):

**`dpo` — Data Protection Officer (P1-R2-1 legal-error correction).**
D6 v1 incorrectly conflated **Art. 28 GDPR DPA** (processor contract
obligation) с **§38 BDSG DPO** (headcount-driven appointment obligation).
These are **distinct regulatory duties** с different triggers. v2
separates them:

| Obligation | Legal basis | Trigger | Jetix Phase |
|------------|-------------|---------|-------------|
| **Art. 28 DPA capability** (have template, capable signatory) | Art. 28 GDPR processor obligation | Processor relationship = any client handling personal data | **Phase 1 readiness required** (template Day 5-6) |
| **Art. 30 RoPA** (Records of Processing) | Art. 30 GDPR | 250+ employees OR non-occasional OR risk-likely OR Art. 9 special-category | **Phase 1 likely triggered** (non-occasional) |
| **Art. 37(1)(a) DPO appointment** | Art. 37 GDPR | Public authority deployer | N/A (Jetix non-public) |
| **Art. 37(1)(b) DPO** | Art. 37 GDPR | Core activity = regular systematic monitoring | **Trigger at first HR/behaviour audit client** |
| **Art. 37(1)(c) DPO** | Art. 37 GDPR | Core activity = large-scale Art. 9/10 data | **Trigger at first Art. 9 data client** |
| **§38(1) BDSG DPO** (headcount) | §38 BDSG (post-2019 Zweites Datenschutz-Anpassungs- und Umsetzungsgesetz) | "In der Regel mindestens 20 Personen ständig mit der automatisierten Verarbeitung personenbezogener Daten beschäftigt" | **Phase 2b headcount trigger** |
| **§38(1) BDSG DPO** (DPIA) | §38 BDSG + Art. 35 | DPIA mandatory (high-risk processing) | **Possible earlier trigger per-engagement** |

**External-mode DPO Phase 1 strategy** (Ruslan directive — single cheapest
de-risking move for first 10 client contracts): engage
Datenschutzkanzlei или external Datenschutz-Beratungsfirma by Phase 1
Day 7; budget ~€200-500/month. DPO competence criteria per Art. 37(5):
independence, expertise, DACH residency preferred, conflict-of-interest
avoidance per Art. 38(6), registered with BfDI или equivalent Länder DSB.
**NOT "Phase 2a when ≥1 client requests DPA"** — that conflates Art. 28
DPA readiness (Phase 1) с §38/Art. 37 DPO appointment (different
triggers).

**`customer-success`** (J2 Phase 2a activation — per MC1).

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
typed edges; **B.1 Γ Universal Algebra** (L.25581) aggregates; **A.1
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
- **FPF A.15 Role-Method-Work Alignment** (L.17754) — firewall
- **FPF B.1 Γ Universal Algebra** (L.25581) — aggregation
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

**Example — L/A/D/E applied к Audit SKU proposal for Müller GmbH Q2 2026:**

```yaml
# alphas/deal/instances/muller-gmbh-audit-q2-2026-proposal.yaml (excerpt)
L (Laws):
  - GDPR Art. 22 (automated decision defence — relevant к any AI-tool audit recommendations)
  - GDPR Art. 28 (Jetix = processor under Müller controller; DPA required)
  - EU AI Act Aug 2026 high-risk obligations IF Müller HR-tool audit triggers Annex III 4(a)
  - HGB §238 Buchführungspflicht (Müller retains delivered audit artifact ≥10 years per §257)
  - BGB §187 business-day calculation for all SLA references

A (Admissibility):
  - Müller accepts intermediate milestone within 3 business days (else default-accepted)
  - Rework bounded к 2 cycles per deliverable; third cycle = scope-change conversation
  - Multi-View bundle (5 viewpoints) mandatory — not negotiable per CP-4
  - Bias-audit BA-3 closure document required for Project.closed transition

D (Deontics):
  - Jetix obliged to retain anonymized project data 6 years (HGB §257 + GDPR proportionality per §4.5.9)
  - Müller obliged to provide access to AI-tool inventory by Day 5 of engagement
  - Jetix permitted to reference anonymized Müller learnings в future wiki/sources/ entries post-closure
  - Müller permitted to extend engagement at same price within 30 days of delivery

E (Effects):
  - Audit PDF ≥40 pages, 5 viewpoints (Executive 2-3pp / Technical 20-40pp / Governance 3-7pp / Regulatory 3-5pp / Internal-learning 5-10pp)
  - Identified bias count ≥ N per 5-class taxonomy (REP/ALG/VIS/MET/LNG)
  - SLA: response within 24h business hours (Berlin CET); incident 4h per Art. 33(2) processor notification
  - F-G-R tag on each major recommendation: F2-F3 / G: müller-internal-2026-q2 / R-medium-to-high
  - EU AI Act Art. 14 human-oversight disclosure included в Regulatory viewpoint
```

**Reader sees at glance:** which parts of this proposal are statute-
bound (L), which are negotiated with client (A), which are obligations/
permissions (D), which are measurable outcomes (E). Audit filter:
"show all L-lane in Müller contract" answers "what statutes bind this
engagement" в seconds.

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

### 4.5 CP-5 — Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14)

**Statement:** AI-agent outputs affecting clients go through **human
approval gate** designed to satisfy (a) GDPR Art. 22(3) automated-
decision safeguards, (b) EU AI Act Art. 14 human-oversight obligations
(for high-risk deployments per §4.5.1), and (c) Jetix internal
accountability discipline. No purely autonomous client-affecting AI
decisions. Gate = sales-closer / acceptance-authority / Ruslan
(founder strategic gate).

**Operational specification** (P1-R2-3 resolution — full 9-element
expansion):

#### 4.5.1 Gate scope — what requires the gate ("client-affecting" taxonomy)

Three tiers с different SLAs:

| Tier | Content | SLA (business-hours) | Example |
|------|---------|----------------------|---------|
| **L1 — Contractual** | Content binding legal obligations, payment, or material deliverable commitment | 4h | Signed proposal, DPA signature, deliverable acceptance sign-off, pricing change >10% |
| **L2 — Substantive** | Content materially influencing client decisions or perceptions | 24h | Audit recommendations, research conclusions, governance advice emails, risk assessments |
| **L3 — Cosmetic** | Minor format/language edits, scheduling, acknowledgments | No gate required (J-Auto); post-hoc log only | Calendar invite, typo fix, neutral acknowledgment |

**Default rule для unlisted:** escalate to L2 (conservative default).

#### 4.5.2 Gate-keepers — competence + Vertretung (escalation alternates)

| Gate-keeper | Primary scope | Backup (Vertretung) | If both unavailable |
|-------------|---------------|---------------------|---------------------|
| **sales-closer** (Ruslan sub-role) | L1 contractual / pricing / signature decisions | acceptance-authority (Ruslan) | Queue; no auto-release |
| **acceptance-authority** (Ruslan sub-role) | L2 deliverable quality sign-off / bias-audit closure | sales-closer for contractual overlap | Queue; no auto-release |
| **Ruslan (founder strategic)** | Anything flagged `strategic` escalation class | — (no alternate Phase 1) | Queue с 24h extension; if still unavailable, client notified of delay |

All gate-keepers must satisfy **Art. 22(3) + WP251rev.01** "meaningful
intervention" criteria: authority AND competence to change outcome,
not rubber-stamp. Phase 2a Beirat member may act как alternate for
non-urgent L2 decisions.

#### 4.5.3 Approval SLA windows

- **L1 Contractual**: 4h business-hours (Berlin CET 08:00-18:00 Mon-Fri).
- **L2 Substantive**: 24h business-hours default; 72h maximum with
  client-visible delay notification.
- **L3 Cosmetic**: no gate.
- **Off-hours (18:00 Fri — 08:00 Mon)**: AI outputs queue, не auto-
  release. Feierabend-respecting. Exception: `safety` classification
  escalation pages Ruslan via notification channel; Ruslan decides
  whether to gate off-hours.

#### 4.5.4 Audit trail schema (YAML frontmatter для every gated decision)

```yaml
# comms/approval-log/YYYY-MM-DD-<decision-slug>.yaml
decision_id: dec-20260421-0042
tier: L2                            # L1/L2/L3
client_affecting_category: [audit-recommendation]
ai_output_ref:                       # versioned
  source_agent: sales-lead
  output_version: v1
  artifact_path: alphas/client/instances/muller-gmbh/drafts/audit-rec-v1.md
  f_g_r: F2/G:jetix-audit-dach-2026-q2/R-medium
gate_keeper:
  role: acceptance-authority
  holder: ruslan-berlin
  approved_at: 2026-04-21T14:32:00+02:00
  decision: approved                 # approved | rejected | modified | escalated
  modification_if_any: none
  reason: "MECE matrix satisfied; bias-audit REP class flagged appropriate; EU AI Act Art. 14 disclosure-to-deployer present"
  time_to_review_seconds: 420        # cognitive engagement proxy
client_notice:
  sent_at: 2026-04-21T14:35:00+02:00
  channel: email
  art_22_right_to_contest_included: true
retention:
  retention_until: 2032-04-21        # 6 years per HGB §257 + GDPR Art. 5(1)(e) proportionality
```

#### 4.5.5 Escalation protocol — when gate-keeper unavailable

```
IF primary gate-keeper unavailable >SLA:
  1. Message queued in comms/mailboxes/ruslan.jsonl с priority flag
  2. Vertretung notified (see §4.5.2)
  3. IF Vertretung accepts → delegates decision с full audit trail
  4. IF no-one available within 2x SLA window:
     a. Client notified: "decision delayed, new ETA YYYY-MM-DD"
     b. Meta-agent logs `escalation`-type message (FPF-Steward quarterly review item)
     c. AI output held; NO auto-release
  5. Off-hours policy overrides SLA counter — queue resumes at 08:00 CET next business day
```

#### 4.5.6 Contestation mechanism (Art. 22(3) + WP251rev.01)

Every client deliverable derived through AI-gated decision carries:
- **Contest right notice** в Executive + Regulatory viewpoints of
  Multi-View bundle (§4.4).
- **Contact channel**: `contest@jetix.ai` (Phase 2a) or
  `ruslan@jetix-domain` (Phase 1) с SLA 10 business days for initial
  response.
- **Data-subject portal** (Phase 2a+ activation) — self-service
  contestation submission.
- **Re-review by alternate gate-keeper** guaranteed per WP251rev.01
  "meaningful review" (same person cannot be original approver and
  contest reviewer, per conflict-of-interest).

#### 4.5.7 Meaningful-review safeguard

Per WP251rev.01 "actual cognitive engagement" requirement:

- Maximum **8 L2 approvals per gate-keeper per 4-hour block** (hard
  cap — prevents rubber-stamp batch approvals).
- Audit trail `time_to_review_seconds` field <60s flagged as
  quality-risk в FPF-Steward quarterly audit (per §5.4).
- Batch approval forbidden for L1 contractual; each reviewed individually.

#### 4.5.8 Explanation generation (Art. 22(3) "meaningful information")

Every L1/L2 gated decision emits per-deliverable explanation template
(derived from canonical artifact + agency-CHR evidence):

```
Explanation fields:
- Decision summary (plain language)
- AI-component role (which agent, which method)
- Evidence sources (citations, data references)
- Bias-audit classes checked (REP/ALG/VIS/MET/LNG per §4.3)
- F-G-R trust tag с rationale
- Contest pathway
- Retention + access rights
```

Template lives в `decisions/templates/art22-explanation.md` (Phase 1
Day 5-6 write).

#### 4.5.9 Retention policy

- **Minimum 6 months** (EU AI Act Art. 12 event-log requirement).
- **Default 6 years** (HGB §257 commercial record retention; aligns с
  tax/audit record discipline per §1.3).
- **Maximum** bounded by GDPR Art. 5(1)(e) proportionality — purge
  approval logs containing identifying personal data at 6 years
  unless legal hold applies.
- **Retention policy artifact**: `decisions/policy/retention-gdpr-hgb.md`
  (Phase 1 Day 7 write).

#### 4.5.10 Art. 22 per-decision evidence package (for contestation)

If data-subject contests AI-derived recommendation, Jetix assembles:
- Agent output (versioned)
- Human-gate approval record (§4.5.4 schema)
- Most recent BA-3 bias-audit closure referencing this decision class
- Bias-taxonomy coverage per §4.3 5-class таксономия
- Art. 22(3) explanation (§4.5.8)
- Agency-CHR profile of AI-component (§2.1a) showing BMC/PH/PER/evidence_ref

**Delivery SLA**: 10 business days от contest submission to package
delivery к data subject or supervisory authority.

### 4.5.1 EU AI Act Risk-Tier Self-Classification Matrix (P1-R2-2)

D6 v1 cited EU AI Act Scenario C (OT3 internal code) без explicit
EU AI Act taxonomy. v2 resolves: every Jetix offering carries explicit
EU AI Act risk-tier classification, Annex reference, and obligation
roadmap к Aug 2026 high-risk deadline.

**EU AI Act 4-tier taxonomy** (Regulation (EU) 2024/1689):
1. **Prohibited** (Art. 5) — social scoring, subliminal manipulation, etc.
2. **High-risk** (Annex I product safety + Annex III listed uses)
3. **Limited-risk / transparency** (Art. 52 — chatbots, emotion
   recognition, deepfakes, AI-generated content labelling)
4. **Minimal-risk**

Plus **GPAI deployer obligations** (Art. 29a post-Oct 2024) — Jetix как
deployer of Claude triggers downstream GPAI deployer obligations.

| Jetix offering | Likely Tier | Annex/Article | Key obligations | Aug 2026 deadline status | Responsible role |
|----------------|-------------|---------------|------------------|---------------------------|------------------|
| **Audit SKU для Mittelstand** | **Annex III high-risk IF output materially affects employment/credit/essential-service/critical-infra decisions** | Annex III 4(a) employment; 5(a)/(b) essential services; 2 critical infra | Arts. 9 (risk mgmt) / 10 (data gov) / 11 (tech docs) / 12 (records 6mo) / 13 (transparency) / 14 (human oversight) / 15 (accuracy) + Art. 29 deployer + FRIA per Art. 29a if public-authority context | **High-risk obligations Aug 2, 2026** — per-engagement self-classification (if audit includes HR/credit/infra → full Annex III) | acceptance-authority (sub-role) + external-mode DPO |
| **Internal 11-agent automation** | **Limited-risk / GPAI deployer** | Art. 52 + Art. 29a | Art. 52 disclosure if agent outputs reach client без human gate; Art. 29a GPAI deployer logs; use per Anthropic-stated instructions | — (applies at deployment; ongoing) | system-admin |
| **Lead-scoring + sales-research agent** | **Minimal-risk** (internal use, no automated client-affecting decisions due CP-5 gate) | n/a | Voluntary codes of conduct; internal documentation | n/a | sales-lead |
| **Content-Item production (Alpha 4 — newsletter, LinkedIn, YouTube)** | **Limited-risk / transparency** — Art. 52(3) AI-generated content labelling IF published без explicit human authorship | Art. 52(3) + (4) | Disclosure "generated with AI assistance" on AI-involved content; framing-lead ensures labelling | Ongoing from now | framing-lead |
| **Multi-View deliverables (Audit SKU output)** | **Flow-through from Audit SKU tier** — depends on underlying audit subject matter | Same as Audit SKU row | Same as Audit SKU row | Same as Audit SKU row | acceptance-authority |
| **Future hires onboarding content (internal)** | **Minimal-risk** | n/a | Internal docs; no client-affecting AI decisions | n/a | meta-agent |
| **Strategic advisory (sales-closer conversations + founder letters)** | **Minimal-risk** (human-originated; AI assists research, не produces final) | n/a | F-G-R tagging per §4.2 discipline | n/a | sales-closer + Ruslan |

**Per-engagement self-classification protocol:**
1. Before accepting Audit SKU contract → framing-lead runs classification
   questionnaire against Annex III taxonomy.
2. Result documented в `alphas/project/instances/<slug>/eu-ai-act-
   classification.yaml`.
3. If Annex III triggered: Art. 9-15 obligations + FRIA (Art. 29a)
   activated; contract E-lane includes explicit Art. 14 human-oversight
   clause; pricing reflects compliance overhead.
4. If limited/minimal: standard L/A/D/E contract; Art. 52 disclosure if
   applicable.

**Full operational template**: `decisions/policy/eu-ai-act-risk-tier.yaml`
(Phase 1 Day 7 write, ETA 2026-04-30). **EU AI Act FAQ для sales
conversations**: `decisions/policy/eu-ai-act-client-faq.md` (Phase 1
Day 10).

**Aug 2, 2026 high-risk obligations coverage snapshot** (for Audit SKU
Annex III engagements):

| EU AI Act Article | Jetix implementation | Artifact |
|-------------------|----------------------|----------|
| **Art. 9 Risk management** | Bias-audit (§12.10) + risk taxonomy expansion Phase 2a | `decisions/policy/bias-audit-cycle.md` |
| **Art. 10 Data governance** | NQD-CAL + E/E-LOG (§7.5) per-direction + data-quality gates в SoW | `directions/<slug>/nqd-distinctions.yaml` |
| **Art. 11 Technical documentation** | Multi-View Technical (§4.4, 20-40 pages) + Annex IV template | `decisions/templates/views/technical.md` |
| **Art. 12 Record-keeping (6mo min)** | Retention policy §4.5.9 + commit log | `decisions/policy/retention-gdpr-hgb.md` |
| **Art. 13 Transparency-to-deployer** | F-G-R tagging §4.2 + explanation generation §4.5.8 | Per-deliverable |
| **Art. 14 Human oversight** | CP-5 gate §4.5.1-4.5.10 | This section |
| **Art. 15 Accuracy/robustness** | Bias-audit + Multi-View correspondences check + ISO/IEC 24029-2 alignment (Phase 2a) | `decisions/policy/robustness-testing.md` (Phase 2a) |
| **Art. 29 Deployer obligations** | Use-per-instructions + human oversight assignment + Art. 12 logs + FRIA if applicable | CP-5 + §4.5.4 audit trail |
| **Art. 29a GPAI deployer** | Anthropic usage documentation + deployer-role acknowledgment | `decisions/policy/anthropic-deployment.md` (Phase 1 Day 7) |

### 4.5.2 GDPR processor-to-controller incident notification (Art. 33(2))

Per Art. 33(2) GDPR processor obligation: Jetix notifies client controller
of confirmed breach **within 24h from confirmation** (Jetix internal SLA;
default in DPA E-lane). Jetix Art. 33(5) documentation duty begins Day 1
of first personal-data processing. Full Art. 33 breach framework в `ops/
gdpr-art-33-playbook.md` (Phase 1 Day 10 ETA).

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

## Section 5 — Internal Principles (8 principles + ШСМ 5 foundational concepts)

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

**Левенчук grounding:** *Системное мышление 2024* т.1:
> «Системное мышление происходит путём мышления моделированием и письмом
> (с текстами на естественных языках, но с отслеживанием типов объектов
> и видов отношений объектов в этих текстах), поэтому внимание не только
> наводится на важные предметы, но и удерживается на них всё время
> проекта: записанное не так легко забыть в суете.»
>
> **[EN translation]** *"Systems thinking proceeds through thinking-by-
> modelling and thinking-by-writing (with natural-language texts, but
> with tracked object-types and relation-types between those objects in
> those texts). Thus attention is not only directed к important subjects
> but also retained on them throughout the project: what is written down
> is not so easily forgotten amidst the bustle."*

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
>
> **[EN translation]** *"Without an external-to-LLM circuit of text
> processing — no way; the LLM will always deceive. If the LLM itself
> writes the text, 'thinking-by-writing' disappears as a cognitive
> process."*

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

### 5.4a Per-agent FPF-loading tier (P1-R3-1 resolution)

**Context (R3 cost-model critique, Stage C synthesis).** OT5 Scenario A
(full-text D6 в каждый agent system.md) unexamined for per-agent cost.
Back-of-envelope: D6 ~10K tokens × 11 agents × 40-80 invocations/day ×
per-model pricing = **€40-60/day (€1100-1650/mo) before any useful work**
(~3-8% of €50K Q2 revenue target burned on ontology-permeation overhead).

**Resolution:** **Tiered loading strategy** — retains Full-FPF-Permeation
target (shared ontology across agents) while respecting cost discipline.

| Tier | Agents | Loading pattern | Tokens loaded | Rationale |
|------|--------|------------------|----------------|-----------|
| **Tier 1 — Full-text** | strategy-support-analyst (Opus), knowledge-synth (Sonnet), meta-agent (+ FPF-Steward sub-role, Sonnet), manager (Sonnet in deep-coord mode) | Full D6 via system.md | ~10K tokens baseline + sections as needed | These agents **reason over** the ontology — synthesis, coordination, audit require full apparatus |
| **Tier 2 — Distilled essence** | sales-lead (Sonnet), crazy-agent (Sonnet), manager (Sonnet in routine-route mode) | Distilled summary ~2K tokens + on-demand section fetch | ~2-3K baseline | These agents **apply** the ontology в bounded decision domains; distilled summary covers §0-§1 + §2 + §4 + §5.1-5.5 + §6 + §12 headers; deep sections fetched via `Read` tool only when needed |
| **Tier 3 — Reference-only с on-demand fetch** | personal-assistant (Haiku), system-admin (Haiku), sales-research (Haiku), sales-outreach (Haiku), inbox-processor (Haiku) | Section-indexed TOC + on-demand section fetch | ~500-1000 tokens baseline | These agents **execute narrow tasks** that don't need full ontology; inbox-processor classifying a voice note does not need A.14 mereology edges |

**Distilled essence** (~2K tokens, Tier 2 content) = §0 + §0.5 + §0.7
Glossary + §2.1 Ruslan sub-roles + §2.2 agents + §2.2a coordination +
§4.1-4.5 CP headlines + §5.1-5.5 IP headlines + §6.1-6.2 alpha table +
§12 headers. Generated artifact `wiki/foundations/jetix-fpf-distilled.md`
(Phase 1 Day 5-7 write, ETA 2026-04-27).

**Prompt-caching amortization** (per Anthropic prompt-cache TTL 5min):
All agents share identical D6 preamble → **single cache entry amortizes
across agents**. Tier 1 full-text agents benefit most (~90% input-cost
reduction when cache-hit). Tier 2/3 distilled-essence similarly cached.

**Per-agent context-budget** (§1.5 operational clarification, per R3
FP1):

| Layer | Budget | Content |
|-------|--------|---------|
| System preamble | 1K | role.md Blocks 1-2 |
| D6 load (tier-dependent) | 0.5-10K | Tier 1-3 per above |
| Exocortex hard | 25K | Accessible wiki/ slices через niche/ symlinks |
| Task context soft | 25K | per-task KB-pulls, prior messages |
| Working budget | ~20K | reasoning + output |
| **Total floor** | **~70-80K of 200K (Sonnet/Haiku) / 1M (Opus)** | ~40% ctx floor |

**Per-session startup sequence** (all tiers):
1. Read role.md (full).
2. Read D6 loading-pattern-per-tier (system.md preamble).
3. Glob `niche/` symlinks + Read index.md of niche.
4. Proceed к task.

**Cost projection Phase 1 with tiered loading:** ~€15-25/day (reduction
of ~60% vs uniform full-text). Monthly €450-750 — absorbed within P7
compute budget без revenue-target impact.

### 5.5 IP-5 — Explicit alpha state transitions (past-participle discipline, MC6 + Hook 4)

**Statement:** Alpha states — past-participle глаголы (preferred) OR
explicitly-scoped **in-progress phase labels** (narrow exception, see
§5.5a). No gerunds, no present-continuous verbs-as-states.

**Левенчук grounding:** *Методология 2025* — «Состояния предмета метода в
альфе даются глаголами в прошедшем времени, эти глаголы соответствуют
применённым составляющих разных методов к какому-то объекту.»

> **[EN translation]** *"States of a method-subject in an alpha are given
> as past-participle verbs; these verbs correspond to applied components
> of various methods against some object."*

**FPF grounding:** **FPF A.2.5 U.RoleStateGraph** (FPF-Spec L.3282 —
past-tense state names implicit throughout); **FPF A.4 Temporal Duality**
(FPF-Spec L.6489 — design vs run stance).

**Operational primary rule (MC6 + Hook 4):**

| Неправильно (gerund/present-continuous) | Правильно (past-participle) |
|------------------------------------------|-----------------------------|
| "qualifying" | `qualified` |
| "active" | `activated` |
| "in progress" | `started` |
| "delivering" | `delivered` |
| "reviewing" | `reviewed` |

**For Russian** (краткие причастия): "квалифицирован", "активирован",
"начат", "доставлен", "закрыт", "отрефакторен".

### 5.5a In-progress phase exception (P1-R1-3 resolution)

**Exception rule (policy decision Stage C):** Past-participle discipline
**preferred universally**; **`in-X` / `under-X` compound labels ALLOWED**
for genuine in-progress phases where past-participle lexeme either
(a) loses semantic precision (collapses distinct lifecycle stages) или
(b) creates unavoidable ambiguity с terminal-done states.

**Rationale:** Certain lifecycle alphas have a **pending-state** between
entry and resolution that is meaningfully distinct from either. Examples:

- `Client.in-negotiation` ≠ `Client.negotiated` — "negotiated" reads как
  terminal (negotiation concluded), but in sales pipeline we need
  distinct mid-negotiation state where parties exchange actively, before
  either `won` or `lost` is reached. "negotiated" would incorrectly
  collapse `won`/`lost` into parent "negotiated" state.
- `Project.in-follow-up` ≠ `Project.followed-up` — in-follow-up = active
  period of post-delivery support; followed-up would read как single
  past event.
- `Content Item.in-review` ≠ `Content Item.reviewed` — reviewed implies
  review complete (approval or rejection decision made); in-review =
  active review window.
- `Hypothesis.under-validation` ≠ `Hypothesis.validated` — "validated"
  claims truth established; "under-validation" = experiment running,
  outcome pending.
- `Direction.under-validation` — same semantic as Hypothesis.

**Policy decision** (per Ontology > Clarity ranking): **allow** `in-X` /
`under-X` labels **only при explicit semantic distinction от past-
participle sibling state**; Hook 4 enforcement updated к allow these
specific compound forms when both labels exist в same state machine AND
distinction documented в state checklist.

**5 Phase 1 whitelisted exceptions** (Hook 4 explicit allow-list):

| Alpha | State | Why exception | Past-participle would-be ambiguous with |
|-------|-------|---------------|-----------------------------------------|
| Client | `in-negotiation` | Active mid-negotiation phase, distinct from terminal won/lost | would collapse won/lost into single "negotiated" |
| Project | `in-follow-up` | Active post-delivery support window, distinct from "followed-up" terminal | "followed-up" reads как single event, не window |
| Content Item | `in-review` | Active review window, decision pending | "reviewed" implies decision made |
| Hypothesis | `under-validation` | Experiment running, outcome pending | "validated" claims truth established |
| Direction | `under-validation` | Direction thesis tested, outcome pending | same as Hypothesis |

**All 5 documented в `decisions/policy/past-participle-exceptions.md`**
(Phase 1 Day 7 ETA) с per-exception semantic distinction rationale.

**Hook 4 logic (updated):**
```
Block IF state.name ends with -ing AND state.name NOT in whitelist.
Allow IF state.name matches in-X or under-X pattern
      AND (alpha, state.name) in decisions/policy/past-participle-exceptions.md
      AND state machine also contains corresponding past-participle terminal state
            (OR explicit "no-terminal: true" annotation).
Flag to FPF-Steward review IF state added as in-X/under-X WITHOUT exception registration.
```

**Semantic justification preserved:**
- State = fact, NOT process. In-progress exception preserves fact
  character — "fact of being in this specific bounded-pending phase".
  Verifiable через checklist (e.g., in-negotiation = proposal sent +
  ≥1 response received + no final-decision-yet).
- Machine-readable: `IF Client.state == "in-negotiation" THEN trigger
  follow-up-at-day-3 handler`.
- Past-participle preserved for terminal states (won, lost, delivered,
  closed, archived) — where "fact of X happened" is unambiguous.

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
  - **FPF F.6 6-step cycle retrospective** (30/90/180-day).
- JETIX-FPF text loaded в system.md per **tiered loading** (§5.4a — не
  uniform full-text).

### 5.8.1 Concrete example — sales-lead Day-1 executor-binding (P1-R3-5 resolution)

Canonical example of fully-populated `executor-binding.yaml` для first
agent onboarding. D3 role-manifest authors MUST derive their YAML from
this template structure — prevents 11-agent schema divergence (P-6
Lexical Stratification violation).

```yaml
# executors/sales-lead/executor-binding-v1.yaml
# ===========================================================================
# HOLDER + ROLE BINDING (U.RoleAssignment per FPF A.2.1)
# ===========================================================================
holder:
  kind: claude-agent
  model: claude-sonnet-4-6
  instance_id: sales-lead-claude-sonnet-4-6-v1-20260425
role_ref: roles/sales-lead/role.md
context: jetix/l4-revenue/dach-mittelstand        # FPF A.1.1 U.BoundedContext
stance: run                                         # FPF F.6 M2 (design|run)
window:                                             # FPF F.6 M4 Window W
  start: 2026-04-25T08:00:00+02:00
  end: open
  renewal_trigger: 180-day retrospective OR model-upgrade
loading_tier: 2                                     # per §5.4a — distilled essence
primary_j_level: J-Approve                          # per §2.2 table
# ===========================================================================
# AGENCY-CHR PROFILE (per §2.1a canonical schema + FPF A.13:4.3)
# ===========================================================================
agency_profile:
  inherit: decisions/policy/agent-promotion-chr.yaml#default_by_role.sales-lead
  # Base defaults from policy: bmc 0.6 / ph 0.5 / mp 0.3 / per 0.7 / oc 0.5
  # Instance-specific overrides:
  overrides_by_decision_class:
    - class: draft-proposal
      j_level: J-Auto
      bmc: 0.7
    - class: schedule-call
      j_level: J-Auto
      bmc: 0.8
    - class: send-DPA-first-time
      j_level: J-Approve
      bmc: 0.5
      note: "First send of DPA template requires gate; subsequent sends J-Auto once validated"
    - class: send-DPA-subsequent
      j_level: J-Auto
      bmc: 0.7
    - class: discount-offer-0-to-10-pct
      j_level: J-Approve
      bmc: 0.3
    - class: discount-offer-above-10-pct
      j_level: J-Strategic
      bmc: 0.0
      note: "Hard escalation к Ruslan sales-closer sub-role"
    - class: custom-terms
      j_level: J-Strategic
      bmc: 0.0
    - class: sign-contract
      j_level: J-Strategic
      bmc: 0.0
      note: "Founder only per §5.10.4"
    - class: withdraw-from-deal
      j_level: J-Strategic
      bmc: 0.0
  task_family_overrides:                            # per FPF A.13:4.3.1
    - task_family: discovery-call
      bmc: 0.8                                       # high reliability in English-discovery
      per: 0.8
    - task_family: de-contract-negotiation
      bmc: 0.2                                       # low — German-language legal escalates
      per: 0.3
  bmc: 0.6
  ph: 0.5
  mp: 0.3
  per: 0.7
  oc: 0.5
  agency_grade: 2                                    # "Operating" per FPF A.13:4.4
  evidence_ref: decisions/fpf-stewardship/2026-Q2-agency-chr-bootstrap.md#sales-lead
  evidence_status: R-low-pending-phase-1-bootstrap   # upgraded к R-medium Q2 audit
# ===========================================================================
# ONBOARDING (IP-8 + FPF F.6 6-step cycle)
# ===========================================================================
agent_onboarding:
  # FPF F.6 M1 Locate — which context does this role-assignment live in?
  m1_locate: jetix/l4-revenue/dach-mittelstand
  # FPF F.6 M2 Stance — design vs run
  m2_stance: run
  # FPF F.6 M3 Qualify — Holder eligibility verification
  m3_qualify:
    reviewer: meta-agent (FPF-Steward sub-role)
    criteria:
      - Claude Sonnet 4.6 system-prompt integration verified
      - past-participle + in-X exception discipline understood
      - L/A/D/E vocabulary usable by agent on read-test
      - F-G-R tagging syntax demonstrable
    status: passed | pending | failed
    evidence: decisions/fpf-stewardship/2026-Q2-sales-lead-m3-qualify.md
  # FPF F.6 M4 Bind/Assert — the assignment artifact itself
  m4_bind_assert:
    window_stamped_on: this file (executor-binding-v1.yaml)
    role_stamped_on: roles/sales-lead/role.md
    mutual_references_verified: true
  # FPF F.6 M5 Evidence — Σ(Context) evidence shape
  m5_evidence_shape:
    warm_up_task_id_pattern: wu-YYYYMMDD-NNN
    calibration_task_id_pattern: cal-YYYYMMDD-NNN
    production_task_id_pattern: task-YYYYMMDD-NNN
  # FPF F.6 M6 Conclude — confidence γ threshold for promotion
  m6_promotion_threshold:
    to_j_approve_from_j_auto: agency_profile.bmc >= 0.5 AND agency_profile.per >= 0.6 AND warm_up_tasks_passed >= 10
    never_to_j_strategic: true  # hard rule per §5.10.4
  # Initial context pack (loaded at session start per §5.4a Tier 2)
  initial_context_pack:
    mandatory:
      - wiki/foundations/jetix-fpf-distilled.md         # ~2K tokens, Tier 2
      - roles/sales-lead/role.md                         # role-archetype
      - alphas/client/states.yaml                        # state machine
      - alphas/deal/states.yaml
      - directions/_active/ai-consulting-dach/direction.md
      - directions/_active/ai-consulting-dach/pipeline.md
      - wiki/niches/sales/_moc.md                        # niche MOC
    on_demand:
      - design/JETIX-FPF.md § 4 (Client Principles)      # fetch when proposal work
      - design/JETIX-FPF.md § 4.5 (CP-5 Human Gate)      # fetch before sending
      - decisions/policy/boundary-discipline.md           # L/A/D/E detail
      - decisions/policy/trust-tagging.md                 # F-G-R detail
  # Warm-up tasks (calibration before live client work)
  warm_up_tasks:
    - id: wu-20260425-001
      description: Classify 3 mock leads against MECE eligibility matrix; route to qualified/unqualified; emit L/A/D/E-tagged disposition note per lead
      success_criteria:
        - past_participle_violation_count: 0
        - role_executor_conflation_count: 0
        - missing_f_g_r_tag_rate: 0
        - state-name-correctly-uses in-negotiation-exception-if-applicable
    - id: wu-20260425-002
      description: Draft proposal для mock client Müller GmbH per template; structure per A.6.B lanes; do NOT include executor details (no "sonnet-4-6 will perform..."); mark each lane
      success_criteria:
        - L-lane contains ≥1 DACH-legal source (GDPR Art, BGB §, HGB §, EU AI Act Art)
        - A-lane has ≥2 client-acceptance gates
        - D-lane has explicit Jetix+client obligations
        - E-lane contains ≥1 SLA metric + deliverable spec
        - no-exec-details-in-role-archetype: true
    - id: wu-20260425-003
      description: Write F-G-R-tagged response к mock sales inquiry; include R-medium rationale; do NOT overstate certainty
      success_criteria:
        - F-level declared in frontmatter
        - G-scope explicit bounded context
        - R-level matches evidence strength (auto-check against evidence_ref list)
  calibration_checkpoint:
    reviewer: meta-agent (FPF-Steward sub-role)
    at_n_production_tasks: 5
    pass_threshold:
      past_participle_violation_rate: 0.0
      role_executor_conflation_count: 0
      missing_f_g_r_tag_rate: < 0.1
      avg_time_to_review_seconds: > 60   # meaningful-engagement floor per §4.5.7
    failure_action: escalate к Ruslan + retraining via extra warm-up tasks
  retrospective:
    intervals_days: [30, 90, 180]
    format: decisions/fpf-stewardship/YYYY-MM-DD-<agent>-retrospective.md
    items:
      - warm_up_to_live_drift (did agent behavior change post-calibration?)
      - agency_chr_re_measurement (update bmc/per/ph based on actuals)
      - method_description_updates (any method refinements?)
      - decision_class_taxonomy_changes (new categories emerging?)
      - cost_actuals_vs_budget (tokens/day per §5.4a)
# ===========================================================================
# COMPUTE CONTRACT (per P7 Compute budget framework)
# ===========================================================================
compute_contract:
  daily_token_budget_input: 500_000
  daily_token_budget_output: 100_000
  cost_cap_daily_eur: 3.0
  on_exceed_action: soft-throttle-then-notify-ruslan
# ===========================================================================
# COMMUNICATION BINDING
# ===========================================================================
mailbox_address: comms/mailboxes/sales-lead.jsonl
department_lead_for_escalation: sales-lead (self)   # dept head; escalate к Ruslan
acting_as_default: sales-lead                       # per §5.9 enforcement
```

**Lines: ~120.** Covers all D6-mandated fields. D3 role-manifest writers
derive their agent-specific executor-binding по этому pattern. Full
canonical **`shared/schemas/executor-binding.schema.json`** JSON-schema
(Phase 1 Day 5-7 write, ETA 2026-04-27) validates each binding.

### 5.9 Forbidden: dynamic role-switching by agent at task-time

**Statement (negative principle):** Agent cannot dynamically switch role
during task execution. Role assignment happens при task creation (**FPF
F.6 M4 Bind/Assert**), не runtime mid-task.

**Founder exception:** Ruslan multi-role-binding explicit (`executors/
ruslan.yaml` `multi-role-binding: true` flag). Allowed because founder has
long-term identity + commitment + skin-in-game (Taleb) — preconditions
для true strategizing per Левенчук.

**Rationale (Левенчук, ailev/1795494):**
> «Если наплодить много-много ролей, то в текущих многоагентных архитектурах
> типичный рост расхода токенов в 3-10 раз и идут провалы при handoff
> между рольными агентами.»
>
> **[EN translation]** *"If you proliferate many-many roles, in current
> multi-agent architectures typical token-spend increase is 3-10×, and
> handoff failures between role-agents occur."*

→ Role stability > role flexibility (at Phase 1 scale).

### 5.9a Enforcement mechanism (P1-R3-3 resolution)

**Three-layered enforcement** (constitutional mechanism — D6 specifies,
D8 implements):

**Layer 1 — Message-schema tagging (primary, mechanical).** Every agent-
to-agent message carries **`acting_as: <role-id>`** field bound к
sender's `executor-binding.yaml` role_ref. `shared/schemas/message.
schema.json` (Phase 1 Day 1 update) enforces the field; messages without
`acting_as:` fail schema validation and are rejected at mailbox write.

```json
// shared/schemas/message.schema.json excerpt
{
  "required": ["id", "type", "from", "acting_as", "to", "body"],
  "properties": {
    "acting_as": {
      "type": "string",
      "description": "Role-id from D6 §2.2 table — MUST match sender's executor-binding.yaml role_ref",
      "enum": ["strategy-lead", "framing-lead", "sales-closer", "acceptance-authority", "external-relations", "manager", "personal-assistant", "system-admin", "sales-lead", "sales-research", "sales-outreach", "inbox-processor", "crazy-agent", "knowledge-synth", "strategy-support-analyst", "meta-agent"]
    }
  }
}
```

Pre-commit hook on `comms/mailboxes/` additions verifies `acting_as`
field presence + binding-consistency. Violations block commit.

**Layer 2 — Manager-agent monitoring (secondary, detection).** Manager
scans mailbox deltas periodically (morning + evening pipeline). Flags
for review any message where:
- `acting_as` mismatches expected role for current task, OR
- Message body contains role-switch language ("я также как [other-role]
  подготовлю..." / "switching to strategist mode", etc.).

Flagged messages routed к meta-agent for FPF-Steward quarterly audit
aggregation (see §5.4 audit scope item added).

**Layer 3 — FPF-Steward quarterly audit (tertiary, strategic).** Added
к §5.4 audit scope: *"Role-switching compliance — scan mailbox
аggregates; flag pattern-level drift (e.g., sales-lead consistently
acting_as sales-closer)"*. Output: quarterly report + remediation ADR
if pattern detected.

**Founder exception enforcement.** Ruslan's multi-role-binding messages
declare `acting_as:` с current sub-role (strategy-lead / framing-lead /
etc.); sub-role transitions documented inline in commit frontmatter
when consequential (e.g., "sub-role active: strategy-lead" for
strategic-decision commits). Not monitored same как agent role-switch
(founder has identity + commitment), но quarterly review still
aggregates sub-role time-allocation к inform Phase 2a hiring triggers.

**Agreement with D8 (Instructions).** Detailed hook implementation,
manager monitoring logic, audit scripts в D8 §<TBD>. D6 specifies
WHAT is enforced; D8 specifies HOW.

### 5.10 ШСМ 5 foundational concepts — full treatment

Per ADR reference — 5 ШСМ foundational concepts that ground Jetix
methodology. Note (P2-R1-2 terminology honesty — applied consistently
throughout v2): **"5 primitives" was v1 shorthand — actually an R-B
analytical synthesis, не Левенчук's published taxonomy** (per KB Section
3.1). v2 uses «5 ШСМ foundational concepts» или «5 ШСМ method-objects»
consistently. Each concept — first-class в specific Левенчук texts;
для Jetix they serve as didactic frame.

#### 5.10.1 Роль (Role)

Already covered IP-1 (Section 5.1). FPF correlation ✅ A.2, A.2.1, A.2.5,
A.13.

Formula: **Роль = signature метода × interest к системе × набор мастерства.**

#### 5.10.2 Альфа (Alpha)

**Definition** (Левенчук, *Методология 2025*):
> «Альфа — это предмет метода, который может быть и физическим объектом
> (системой), и абстрактным объектом (описанием). Альфа позволяет
> управлять вниманием создателя в ходе исполнения длинных цепочек операций.»
>
> **[EN translation]** *"Alpha is a method-subject that can be either a
> physical object (system) or an abstract object (description). Alpha
> enables managing the creator's attention over the execution of long
> operation chains."*

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
>
> **[EN translation]** *"The method of method-selection is strategizing.
> In conditions where it is entirely unclear what to do. And if it's
> unclear what exactly to do, then nothing can yet be planned (required
> resources unknown), and work cannot yet begin."*

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

### 5.11 Composition of 5 ШСМ foundational concepts

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
entity; **RoleStateGraph (FPF A.2.5)** applied per-instance; ClaimGraphSlot
tracks pipeline-stage claims.

**State checklist examples (verifiable):**
- `qualified`: MECE eligibility matrix passed (jurisdiction DACH|US|RU;
  industry Jetix-ICP; revenue >€10M; decision-maker identified;
  pain-signal explicit).
- `in-negotiation`: Proposal sent; 1+ call scheduled; decision-maker
  engaged; A.6.B L/A/D/E template applied. (In-progress exception per §5.5a.)
- `won`: Contract signed (wet signature OR DocuSign); 1st invoice paid
  OR Scope-of-Work acknowledged.

**FPF A.14 typed edges:**
- Client ComponentOf Jetix-Sales-Function (at operational runtime).
- Client fills ICP slot (directions/_active/ai-consulting-dach/).
- Client methodologically-uses MECE-qualification method.

**Example — Müller GmbH Client transitions over 3 months (Mar-May 2026):**

| Date | Transition | Trigger | Evidence |
|------|------------|---------|----------|
| 2026-03-05 | → `lead-identified` | LinkedIn connection from sales-outreach agent after Rodion podcast mention | `clients/companies/muller-gmbh.md` created; source=linkedin |
| 2026-03-18 | → `qualified` | MECE eligibility: DE jurisdiction + Maschinenbau industry (ICP) + €80M revenue + CTO+CDO identified + AI-compliance pain explicit | MECE matrix committed к `alphas/client/instances/muller-gmbh.yaml` |
| 2026-04-02 | → `proposed` | Proposal sent per L/A/D/E template (§4.3 example above) | `directions/_active/ai-consulting-dach/proposals/muller-gmbh-v1.md` |
| 2026-04-09 | → `in-negotiation` | Client CTO called with 3 counter-proposals (discount request, timeline extension, additional viewpoint) | `alphas/deal/instances/muller-gmbh-audit-q2-2026/negotiation-log.md` — sales-closer (Ruslan) engaged |
| 2026-04-22 | → `won` | Contract signed; DPA Anlage 2 TOMs attached; first invoice paid €15K retainer | `finance/invoices/2026/R-2026-0042.yaml`; contract `clients/companies/muller-gmbh/contract-v1.md` |
| 2026-07-15 | → `churned` (hypothetical) | End of audit engagement + post-close no renewal at 90-day mark | would emit `post-mortem-muller-gmbh.md` |

Each transition documented через git commit; state machine enforced при
YAML update; Hook 4 verifies past-participle + in-X exception discipline.

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

**Protective note (P2-R1-3 addition — SEMAT generalization honesty):**
SEMAT Essence cross-reference = **legacy bridge for SEMAT-literate
audiences only**. Jetix ontology aligned с **Левенчук's generalization
of SEMAT Essence**, NOT с SEMAT software-specific kernel. Per R-D
analysis: Левенчук replaced Requirements → System Definition; Software
System → System Embodiment; Way of Working → Technology (temp) → Method;
Stakeholders → External Project Roles. **Essence Language (type system)
preserved в JETIX-FPF; Essence Kernel (7 software-specific alphas)
superseded by Jetix domain-independent 8-alpha set**. Do not infer SEMAT
Essence software-semantics into Jetix alphas.

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

**Example — Weekly Friday close agenda (60 min):**

```
14:00-14:10  Shape Up commits review
             - What shipped this week (per direction)?
             - Which alpha states transitioned?
             - Any Hook 4 violations flagged by meta-agent?

14:10-14:25  Close-week log
             - Revenue status (pipeline + signed + invoiced + collected)
             - Direction-level NQD distinctions (new novelty observed?)
             - E/E-LOG actions taken (widen/narrow/reroute)
             - F-G-R compliance sampling (3 random deliverables)

14:25-14:45  Next-week framing
             - Top 3 tasks per direction
             - Any strategizing-trigger signals accumulating?
             - Mailbox triage — escalations, stale deps, handoffs

14:45-15:00  Founder reflection (written, not spoken)
             - 1-page note to `decisions/weekly/YYYY-WW.md`
             - Writing-as-thinking primitive: externalize insights
             - Commit + push — artifact persists across sessions
```

**Outputs:** `decisions/weekly/YYYY-WW.md` (founder-written),
`decisions/weekly/YYYY-WW-metrics.yaml` (revenue + state snapshots),
plus `alphas/*/states.yaml` updates.

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
| 32 | **U.Direction ⊑ U.Holon** | `jetix-direction` | Direction (Jetix innovation, Stratum-3 specialization of U.Holon) | — (P8) | Dir |
| 33 | **U.CHRSpace ⊑ U.Case** | `chr-space` | Characteristic Space (SKU / direction-kill / agent-promotion — Stratum-3 specialization of U.Case) | — (Gap 3) | CHR |

**Note:** Actual UTS `wiki/foundations/jetix-uts.md` Layout A Kernel-first
carries 30-50 rows × 6-8 context columns (concurrent с D6 writing per
OQ-08 B). This D6 Section 8 list provides ontology foundation; UTS provides
cross-context mapping.

**Stratum discipline clarification (P1-R1-2 resolution).** Per **FPF E.10
LEX-BUNDLE** §2 Vertical Stratification (FPF-Spec L.41604):
- **Stratum 1-2 (Kernel + Extension)**: U-Types like U.System, U.Holon,
  U.Episteme, U.Role, U.Method, U.Case — exactly one Kernel entry per
  U-Type. Rows #1-31 above = Kernel/Extension Stratum-1/2.
- **Stratum 3 (Context specialization)**: Context-specific subtypes
  declared via `⊑` (subtype-of) relation. Row #32 U.Direction ⊑ U.Holon
  (Direction is a Jetix-context specialization of Kernel U.Holon, not a
  second U.Holon Kernel entry). Row #33 U.CHRSpace ⊑ U.Case (CHR-space
  is a Gap 3 Jetix-context specialization of Kernel U.Case).
- **Stratum 4 (Instance)**: concrete identifiers (Ruslan-as-holder,
  specific role-assignments, specific client instances). Not in this
  table; lives в alphas/ + executors/ + clients/.

D6 v1 presented Rows #3 & #32 both as Kernel U.Holon (violation),
and Rows #15 & #33 both as Kernel U.Case (violation). v2 corrects via
Stratum-3 subtyping labels.

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
- **FPF A.3 Transformer Constitution (Quartet)** (L.5466) — System-in-Role /
  MethodDescription / Method / Work
- **FPF A.6.0 U.Signature** (L.8062)
- **FPF A.15 Role-Method-Work Alignment** (L.17754)
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

**For Jetix:**
> «Лучше говорить 'задача' и корректно моделировать, чем говорить 'альфа'
> и думать о Jira-тикете.»
>
> **[EN translation]** *"Better to say 'task' and model correctly, than
> to say 'alpha' and think about a Jira ticket."*

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
- Hard internal-only stance (OQ-09 A) preserved. **FPF licensing clarity
  (P2-R1-4 rewording):** FPF = Левенчук-authored single-source-of-truth
  (no formal license; citation requested per `raw/external/ailev-FPF/
  ATTRIBUTION.md`). JETIX-FPF = Jetix-internal adaptation (internal-only
  per OQ-09 A hard stance; no contribute-back). Former is **not
  community-open**; it is all-rights-reserved с informal citation
  expectation. v1 phrasing "community-open (sort of)" was misleading.

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

- **FPF A.7 Strict Distinction** (Clarity Lattice, L.16217)
- **FPF E.5.1 DevOps Lexical Firewall** (L.40589)
- **FPF K Lexical Debt** (L.62123)
- **R-B anti-patterns** (KB Section 3.*)
- `decisions/policy/mereology-edge-types.md` — A.14 firewall

### 9.9 What's defensible about JETIX-FPF (proprietary moat vs forkable)

Addresses R4 FP11 investor-readiness critique. JETIX-FPF = adaptation
of unlicensed third-party framework; what stops competitor forking
FPF and out-shipping? **9 genuine Jetix-specific innovations** (documented
`wiki/foundations/jetix-innovations.md` Phase 1 write):

1. **Portfolio-of-Directions (Alpha 8)** — Direction as first-class
   8th alpha с state machine (`hypothesized` → ... → `archived`), NQD-
   CAL per-direction, E/E-LOG per-direction, kill-CHR formal. Not
   canonical FPF.
2. **FPF-Steward sub-role** — dedicated quarterly-audit immune system
   для ontological integrity. 13-item audit scope (ontology sanity,
   past-participle, dedup, role-manifest integrity, direction-concept
   boundary, frontmatter schema, UTS review, F-G-R compliance, A.14
   edge verification, CHR space integrity, Viewpoint Bundle
   correspondences, semi-annual FPF upstream sync, role-switching
   compliance, bias-audit aggregate).
3. **Tiered Full-FPF-Permeation** (per §5.4a) — operationalized
   ontology-permeation с per-agent loading tier (Tier 1/2/3) respecting
   cost discipline. Not in canonical FPF.
4. **4-tier Resource Accounting** (per P7 + D8) — compute / time /
   attention / relational capital as first-class tracked resources.
5. **DACH-specific L/A/D/E template stack** (proposal + contract + DPA
   Phase 1 Day 5-6) с jurisdiction-aware L-lane citations (BGB/HGB/
   GDPR/EU AI Act/DACH-legal) + A-lane Konsenskultur adaptations.
6. **Müller-style traversal pattern** (§3.6) — CRM + KB + portfolio +
   alpha + regulatory supersystem unified query across A.14 typed
   edges. Concrete implementation; not in canonical FPF.
7. **Hybrid founder-mode multi-role-binding** (executors/ruslan.yaml
   `multi-role-binding: true`) + agent role-stability discipline
   enforced via message-schema `acting_as:` (§5.9a). Specific operational
   synthesis.
8. **Past-participle discipline + Hook 4 + in-X exception whitelist**
   (§5.5 + §5.5a) — ML/LLM-friendly binary state reasoning surface,
   operational rigor preventing drift.
9. **JETIX-UTS 30-50 rows Layout-A Kernel-first** — Jetix-specific UTS
   with 5 Phase-1 contexts (jetix-ops, FPF-canonical, DACH-legal,
   AI-industry, ШСМ-Russian) concurrent с D6. Bridges + CL discipline
   Gap 4 adoption.

**Investor story:** not "fork of unlicensed framework" but
"**opinionated DACH-AI-native commercial extension of FPF с 9 Jetix-
proprietary innovations + Phase-1 operational discipline + Q2
audit-defensibility baseline**". These 9 items + 14 Invariants deep
application (§12) + client-facing discipline (§4) constitute moat
against forks.

---

## Section 10 — Mereology + Holon Hierarchy (Jetix application)

Per MC3 Ruslan override — «Три уровня mereological важно, обязательно мы
делаем все три уровня максимально глубоко... Никаких упрощений.» Depth
preserved via hybrid structure (per Option C Stage C structural decision):
Jetix application of mereology stays in D6 (§10.6-§10.11); full academic
lineage material moves к `wiki/foundations/holon-hierarchy.md` companion
(ETA Phase 1 post-D6).

### 10.1 Academic lineage (compressed + companion pointer)

**Lineage summary:** Classical mereology Leśniewski (1916) → Leonard-
Goodman *Calculus of Individuals* (1940) → Lewis *Parts of Classes*
(1991) → Kit Fine *Things and Their Parts* (1999) → Koestler *Ghost in
the Machine* (1967) → Wilber *Sex, Ecology, Spirituality* (1995) →
Mella / Jantsch / Maturana-Varela extensions.

**FPF canonical stance (Jetix adopts):** **Lewis mereological
universalism with relevance restricted** — composition unrestricted as
formal device; operationally only intentional/lifecycle-relevant
compositions matter. **GEM (General Extensional Mereology) foundations
adopted**, CEM unrestricted-composition excluded for operations. **Kit
Fine qua-objects excluded** — FPF uses **RoleMask** (**FPF C.3.4
RoleMask**, FPF-Spec L.34687 — Contextual Adaptation of Kinds without
cloning) pattern instead; agency semantics routed via **FPF A.13**
(L.17328).

**Koestler holon three essentials preserved for Jetix:**
- **Janus phenomenon** (Koestler Prop 1.4) — holons face inward (parts)
  AND outward (containing whole) simultaneously. Jetix = U.System AND
  U.Episteme simultaneously (§1.1).
- **S-A vs INT tendencies** (Prop 4.1) — healthy holon balances self-
  assertive wholeness AND integrative partness. Failure modes: S-A
  excess (Prop 9.4 "monopolizing") / INT excess (Prop 9.5 groupthink).
  Used в bias-audit reasoning (§12.10).
- **Any stable bio/social sub-whole applies** (Prop 1.5) — licences
  calling Jetix departments / alphas / roles holons.

**Wilber 4-quadrants** (UL "I" subjective / UR "It" observable / LL
"We" culture / LR "Its" institutions) — used для Multi-View Publication
(§4.4) analogical framing + bias-audit quadrant-coverage check.

**Full academic treatment (Leśniewski axiom derivation, GEM ⇄ Boolean
algebra isomorphism per Tarski 1935, Kit Fine hylomorphism, Monster
Objection, autopoiesis critique)**: moved к `wiki/foundations/holon-
hierarchy.md` (Phase 1 post-D6 write). D6 retains Jetix-application
depth (§10.6-§10.11) + exclusion justification (§10.8).

**Critical exclusions (unchanged from v1):** CEM unrestricted composition
operationally ignored; BFO explicitly rejected (per ailev/1451832
«негодная онтология для инженерных задач» / "unfit ontology for
engineering tasks"); Van Inwagen's organicism excluded (would deny non-
biological composites). Full exclusion list + rationales в §10.8.

### 10.2 (Lewis, Fine, constructor-theory vocabulary — moved к companion)

*Placeholder — full content в `wiki/foundations/holon-hierarchy.md`.*
D6 retains only D6-operationally-consequential residue:
- Lewis pragmatic stance = FPF canonical (above §10.1).
- Kit Fine qua-objects **excluded**; A.13 RoleMask used instead (see
  §10.8).
- Constructor theory vocabulary imported only (not physics); operational
  residue в §13 + §10.10 Compose-CAL.

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
- Qua-objects (role-as-mask sufficient via **FPF C.3.4 RoleMask** —
  Contextual Adaptation of Kinds, FPF-Spec L.34687; coexists with **FPF
  A.13 Agential Role & Agency Spectrum** L.17328 which covers agency
  semantics — v1 citation was correct; P3-R1-5 reviewer-finding rejected
  per FPF-Spec verification `grep -n "^## C\.3\.4" raw/external/ailev-FPF/
  FPF-Spec.md` → L.34687).
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
>
> **[EN translation]** *"Intellect-stack disciplines are often called
> trans-disciplines — 'disciplines for reasoning during the engagement of
> applied disciplines' (trans- meaning 'located on the other side of'
> applied disciplines)."*

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
    activities changing world. **Home of 5 ШСМ foundational concepts:
    роль / альфа / граф создания / стратегирование / мышление письмом.**
16. **Системная инженерия (Systems Engineering)** — **2023 apex** —
    normatively prescribes how activities for creating systems should be
    structured.

### 11.3 Dependency structure (compressed + companion pointer)

Layered structure (Foundation 1-5 → Formal 6-9 → Knowledge 10-11 →
Coordination 12-14 → Action 15-16). Per R-C Section 3.2: true structure
is **graph (lattice), not sequence** — linearization is pedagogical
convenience.

**Full dependency graph + FPF-5-layer-vs-16-disciplines tension analysis
+ 17-vs-16 evolution history** moved к `wiki/foundations/trans-
disciplines.md` companion (per Option C hybrid Stage C structural
decision). D6 retains concept + enumeration + Jetix-subset.

### 11.4 Relation к 5 ШСМ foundational concepts

| Trans-discipline | Primary home of |
|------------------|-----------------|
| **Методология (15)** | ★★★ Роль, Альфа, Граф создания, Стратегирование |
| **Собранность (2)** | ★★★ Мышление письмом — primary home (экзокортекс practice); **BUT cross-cuts all disciplines** per R-C Executive Summary (scale-free practice, central instrument в every skill) |
| **Системная инженерия (16)** | Normative role system + canonical alphas |

**Cross-cutting note (P3-R1-1 refinement):** «Мышление письмом» is
scale-free practice, not exclusively housed в Собранность — per
ailev/1513051 practised across all ШСМ courses. Primary home =
Собранность (exocortex discipline); **applied instrument across all
15 other disciplines**.

### 11.5 FPF-5-layer vs ШСМ-16-discipline — different abstractions

Summary (full в companion): FPF-Spec **does not mention intellect-stack**
explicitly; FPF-Preface 5-layer stack (Structure & Reality / Knowledge &
Reasoning / Action & Execution / Strategy & Rationality / Governance &
Purpose) is pedagogical projection (per FPF-Spec L.730). ШСМ 16
trans-disciplines = curriculum/competency frame; FPF 5-layer = patterns
map. **Not contradictory** — different abstractions для different
audiences.

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
- 15. **Методология** — 5 ШСМ foundational concepts + role-manifest authoring.
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

### 11.7 17 vs 16 — historical note (compressed)

Evolution: Pre-2019 STEM → 2019 6 proto-trans-disciplines → Aug 2021 16
levels → End-2021 17 (Труд added) → 2023 16 (Труд → Системная инженерия,
Математика + Физика added, Экономика/Объяснения/Теория-информации
removed). **For Jetix: use 16 always.** Full historical detail в
`wiki/foundations/trans-disciplines.md` companion.

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

**Example — DRR for "Adopt Option C hybrid structural decision" (this Stage C):**

```markdown
# DRR-2026-04-20-d6-structural-decision-option-c

Δ-class: Δ-3 (full semantic change — restructures D6 sections 10 + 11)

## Problem frame
Trigger: Stage B Reviewer 4 Enterprise Reader critique (commit 582349f)
flagged Sections 10 + 11 as "constitutional-document cargo" — academic
mereology lineage (Leśniewski→Lewis→Fine→Koestler→Wilber→Mella→Jantsch)
and 16-trans-disciplines history reading as founder-syndrome perfectionism
to investor/Aufsichtsrat audience. Concurrent Ruslan MC3 hard override:
"full mereology, никаких упрощений, max Левенчук depth".

## Decision
**Option C (hybrid):** Keep D6 constitutional core + Jetix application of
mereology (§10.6-10.11) + trans-discipline Jetix-subset (§11.6) в place;
move academic-lineage content (§10.1-10.5 reduced к summary + pointer,
§11.3-11.5 + 11.7 reduced к summary + pointer) к `wiki/foundations/holon-
hierarchy.md` + `wiki/foundations/trans-disciplines.md` companions.

## Rationale
- **Ontology fidelity primary** (per Stage C prompt ranking): R1 Левенчук
  Purist says "do not shrink Section 10" — depth is mereology requirement.
- **Hybrid satisfies both**: depth preserved (in companions) + clarity
  restored (D6 reads as constitutional doc). Ruslan MC3 literal text
  "три уровня максимально глубоко" — depth in companion satisfies literal
  text; full formalism не required in constitutional doc per GR-2
  Notational Independence.
- **R4 Enterprise Reader critique valid**: 55-y.o. Mittelstand
  Geschäftsführer closing PDF at page 3 is real risk; founder-syndrome
  signal unfavorable for Series A defensibility.
- **Option A (keep monolithic)** rejected: ignores R4; 50-page constitutional
  doc impossible to сoherently orient new hires.
- **Option B (aggressive split — 6 companions)** rejected: too much
  scaffolding overhead для Phase 1; loses constitutional coherence.

## Pillars check (FPF E.2)
- P-1 Cognitive Elegance ✓ (tighter structure; less ornamental)
- P-2 Didactic Primacy ✓ (reader comprehension elevated)
- P-3 Scalable Formality ✓ (depth available in companions when needed)
- P-10 Open-Ended Evolution ✓ (companions can evolve independently)

## Consequences
- D6 length: ~40 pages (vs v1 ~50) — target fit for constitutional role.
- Companion files become "deep-depth references" — writable Phase 1 post-D6.
- Reader-routing table (§0.5) operational immediately.
- FPF-Steward Q2 audit scope expands к verify companion-file integrity.

## Kill conditions
- If quarterly readership metrics show companions unused (<2 reads/qtr
  by FPF-Steward + knowledge-synth combined) → reconsider whether split
  justified (re-merge к monolithic possible).
- If Ruslan writing workflow blocked by pointer-indirection — reconsider.

## Review checkpoint
2026-Q3 close (FPF-Steward quarterly audit) — verify companion files
populated; measure D6 onboarding-to-usable-agent time baseline.
```

This DRR itself is a worked example: **Problem frame + Decision +
Rationale + Consequences + Kill conditions + Review checkpoint**
structure, ~250 words core, committed to `decisions/strategy/2026-04-20-
d6-v2-structural-decision.md` alongside v2 commit.

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

### 14.2 FPF patterns cited in JETIX-FPF (exact verified line numbers)

All line numbers verified against `raw/external/ailev-FPF/FPF-Spec.md`
(62,202 lines, March 2026 vendored commit 0a22129) via reproducible
`grep -n "^## <pattern-id> -"` commands. v1 contained ~17 citations off
by 100-3766 lines (worst: A.3 off by 3766); v2 replaces all `~approx`
values с exact line numbers (P1-R1-1 resolution).

| Pattern ID | Name | Line | Section in D6 |
|------------|------|------|---------------|
| A.0 | Onboarding Glossary (NQD & E/E-LOG) | 769 | Preamble |
| A.1 | Holonic Foundation | 1017 | 1.1, 1.2, 1.7, 10.7, 12.1 |
| A.1.1 | U.BoundedContext | 1202 | 1.1, 5.2 |
| A.2 | Role Taxonomy | 1403 | 2.1, 5.1, 8.1 |
| A.2.1 | U.RoleAssignment | 1613 | 2.1, 4.1, 8.1 |
| A.2.5 | U.RoleStateGraph | 3282 | 5.5, 6.1 |
| A.3 | Transformer Constitution (Quartet) | 5466 | 8.1, 12.2 |
| A.4 | Temporal Duality & Open-Ended Evolution | 6489 | 5.5 |
| A.6 | Signature Stack & Boundary Discipline | 6671 | 12.9 |
| A.6.0 | U.Signature | 8062 | 5.12 |
| A.6.B | Boundary Norm Square | 7097 | 4.3, 4.6, 5.8, 12.9 |
| A.6.C | Contract Unpacking | 7741 | 4.3 |
| A.6.H | Wholeness Unpacking (RPR-WHOLE) | 15851 | 4.3 |
| A.6.P | Relational Precision (RPR) | 10601 | 4.3 |
| A.6.Q | Quality Term Precision (Q-TERM) | 11326 | 4.1, 4.3 |
| A.6.S | Signature Engineering Pair | 15419 | 6.4, 13.2 |
| A.6.3.CR | Same-Entity Retextualization | 9521 | 4.4 |
| A.7 | Strict Distinction (Clarity Lattice) | 16217 | 9.8 |
| A.8 | Universal Core Principle (C-1) | 16681 | 8.2 |
| A.10 | Evidence Graph Referring (C-4) | 16930 | 2.1a |
| A.12 | External Transformer & Reflexive Split | 17194 | 12.1 |
| A.13 | Agential Role & Agency Spectrum | 17328 | 2.1, 2.1a, 5.12, 10.8 |
| A.14 | Advanced Mereology | 17478 | 1.7, 3.1, 3.5, 3.7, 5.12, 9.4, 10.7, 12.1 |
| A.15 | Role-Method-Work Alignment | 17754 | 3.5, 5.12, 12.3 |
| A.15.1 | U.Work | 18020 | 6.6, 12.2 |
| A.15.2 | U.WorkPlan | 18389 | 6.6, 12.2 |
| A.16 | Language-State Transduction Coordination | 18954 | Phase 1 Rec-17 |
| A.16.1 | U.PreArticulationCuePack | 19549 | Rec-17 |
| A.17 | Canonical Characteristic (CHR-NORM) | 20064 | 4.3, 12.8 |
| A.18 | Minimal CSLC Kernel | 20202 | 6.3.8, 12.8 |
| A.19 | CharacteristicSpace & Dynamics Hook | 20359 | 12.8 |
| A.20 | Flow Constraint Validity | 24927 | 12.8 |
| A.21 | GateProfilization | 25224 | 12.8 |
| B.1 | Γ Universal Algebra of Aggregation | 25581 | 3.1, 10.7, 12.6 |
| B.2 | Meta-Holon Transition (MHT) | 27444 | 7.2 trigger, 12.13 |
| B.2.5 | Supervisor-Subholon Feedback | 28100 | 12.13 |
| B.3 | Trust & Assurance Calculus (F-G-R) | 28201 | 4.2, 12.7 |
| B.3.4 | Evidence Decay & Epistemic Debt | 28670 | 4.2 |
| B.4 | Canonical Evolution Loop | 29094 | 7.1, 7.6 |
| B.5.2 | Abductive Loop | 29606 | 5.10.4 |
| B.5.2.0 | U.AbductivePrompt | 29905 | 5.10.4, 8.1 |
| C.2.1 | U.Episteme — Epistemes and slot graph | 30495 | 6.6, 8.1 |
| C.2.2 | Reliability R in F-G-R triad | 31301 | 4.2 |
| C.2.2a | U.LanguageStateSpace | 31676 | 8.1 |
| C.3 | Kinds, Intent/Extent, Typed Reasoning (Kind-CAL) | 33185 | 8.1 |
| C.3.4 | RoleMask — Contextual Adaptation of Kinds | 34687 | 10.1, 10.8 |
| C.11 | Decision Theory (Decsn-CAL) | 35856 | 5.10.4 |
| C.13 | Constructional Mereology (Compose-CAL) | 36503 | 10.7, 10.10, 13.2 |
| C.18 | Open-Ended Search Calculus (NQD-CAL) | 37808 | 5.10.4, 6.3.5, 7.5 |
| C.18.1 | Scaling-Law Lens Binding | 37919 | 7.5 BLP |
| C.19 | Explore-Exploit Governor (E/E-LOG) | 38008 | 5.10.4, 6.3.5, 7.5 |
| C.19.1 | Bitter-Lesson Preference (BLP) | 38327 | 7.5 BLP |
| C.22 | Problem Typing & TaskSignature (Problem-CHR) | 38734 | Phase 1 Rec-16 |
| D.5 | Bias-Audit & Ethical Assurance | 39964 | 4.3, 12.10 |
| E.1 | Vision & Mission | 40088 | Preamble |
| E.2 | Eleven Pillars | 40148 | 12.4 |
| E.3 | Principle Taxonomy & Precedence | 40264 | 12.4 |
| E.5 | Four Guard-Rails of FPF | 40487 | 12.5 |
| E.5.1 | DevOps Lexical Firewall | 40589 | Preamble, 8.5 |
| E.5.3 | Unidirectional Dependency | 40743 | Preamble |
| E.9 | Design-Rationale Record (DRR) | 41506 | 7.2, 12.14 |
| E.10 | LEX-BUNDLE (Unified Lexical Rules) | 41604 | 5.10.2, 8.1, 8.2, 8.3 |
| E.17.0 | U.MultiViewDescribing | 43945 | 8.1 |
| E.17.1 | U.ViewpointBundleLibrary | 44325 | 4.4 |
| E.17.2 | TEVB | 44696 | 4.4 |
| E.17 | Multi-View Publication Kit | 45107 | 4.4, 13.1 |
| E.18 | Transduction Graph Architecture | 47502 | 13.1 |
| E.20 | Mechanism Introduction Protocol | 48322 | Rec-20 |
| F.0.1 | Contextual Lexicon Principles | 48660 | 5.2 |
| F.1 | Domain-Family Landscape Survey | 48995 | 5.2 |
| F.4 | Role Description (RCS + RoleStateGraph + Checklists) | 49984 | 5.6 |
| F.6 | Role Assignment & Enactment Cycle (Six-Step) | 50641 | 5.8, 5.8.1 |
| F.7 | Concept-Set Table | 50898 | 8.1 |
| F.9 | Alignment & Bridge across Contexts | 51539 | 5.2, 8.4 |
| F.9.1 | Bridge Stance Overlay | 52071 | 8.4 |
| F.11 | Method Quartet Harmonisation | 52604 | 7.3 |
| F.17 | Unified Term Sheet (UTS) | 54586 | 5.2, 8.1, 12.12 |
| G.5 | Multi-Method Dispatcher & MethodFamily Registry | 58316 | 7.4 |
| J.4 | First Practical Entry Route Index | 62110 | 14.5 |
| K | Lexical Debt & Mandatory Replacements | 62123 | 8.5 |

**Total verified patterns: 72.** All line numbers exact per FPF-Spec.md
(March 2026 vendored commit 0a22129). Reproducible verification:
```bash
grep -n "^## <pattern-id> -" raw/external/ailev-FPF/FPF-Spec.md
```
Tooling commitment: `tools/verify-fpf-citations.sh` (Phase 1 Day 10 ETA)
runs this check automatically в pre-commit hook; prevents recurrence of
v1 line-number drift.

### 14.2a Reference status audit table (P1-R2/R3 Theme-T3 reference-chain integrity)

Addresses cross-reviewer theme **T3** — per R1 + R2 + R3: cross-references
к non-existing artifacts create trust-erosion. Each policy/companion/
template referenced throughout D6 carries explicit status + ETA:

| Reference | Status | ETA | Writer |
|-----------|--------|-----|--------|
| `wiki/foundations/jetix-uts.md` | concurrent с D6 | 2026-04-26 | Ruslan + knowledge-synth |
| `wiki/foundations/jetix-creation-graph.md` | placeholder | 2026-04-27 | Ruslan |
| `wiki/foundations/fpf-tooling.md` | placeholder (Rec-13) | 2026-05-04 | Ruslan + system-admin |
| `wiki/foundations/jetix-innovations.md` | placeholder | 2026-05-04 | knowledge-synth |
| `wiki/foundations/shsm-primitives.md` | placeholder | 2026-05-04 | knowledge-synth |
| `wiki/foundations/holon-hierarchy.md` | placeholder (Option C hybrid move) | 2026-05-04 | knowledge-synth |
| `wiki/foundations/trans-disciplines.md` | placeholder (Option C hybrid move) | 2026-05-04 | knowledge-synth |
| `wiki/foundations/jetix-fpf-distilled.md` | placeholder (P1-R3-1 loading tier) | 2026-04-27 | Ruslan |
| `decisions/policy/boundary-discipline.md` | placeholder (Gap 1) | 2026-04-27 | Ruslan + external legal |
| `decisions/policy/trust-tagging.md` | placeholder (Gap 2) | 2026-05-04 | Ruslan |
| `decisions/policy/sku-pricing-chr.yaml` | placeholder (Gap 3) | 2026-05-11 | Ruslan + Vladislav advisor |
| `decisions/policy/agent-promotion-chr.yaml` | placeholder (Gap 3 + P1-R3-4) | 2026-04-27 | Ruslan + meta-agent |
| `decisions/policy/characteristic-space-conventions.md` | placeholder | 2026-05-11 | Ruslan |
| `decisions/policy/mereology-edge-types.md` | placeholder (Rec-05) | 2026-05-04 | knowledge-synth |
| `decisions/policy/phase-transitions-mht.md` | placeholder (Rec-06) | 2026-05-11 | Ruslan |
| `decisions/policy/bias-audit-cycle.md` | placeholder (Rec-03) | 2026-05-04 | Ruslan + ethics advisor |
| `decisions/policy/mechanism-introduction.md` | placeholder (Rec-20) | 2026-05-11 | Ruslan |
| `decisions/policy/multi-method-dispatcher.md` | placeholder (Rec-21) | 2026-06-15 (Phase 2b relevance) | Ruslan |
| `decisions/policy/past-participle-exceptions.md` | placeholder (P1-R1-3) | 2026-04-27 | Ruslan |
| `decisions/policy/eu-ai-act-risk-tier.yaml` | placeholder (P1-R2-2) | 2026-04-30 | Ruslan + external DPO |
| `decisions/policy/eu-ai-act-client-faq.md` | placeholder (P1-R2-2) | 2026-05-04 | framing-lead sub-role |
| `decisions/policy/retention-gdpr-hgb.md` | placeholder (P1-R2-3) | 2026-05-04 | Ruslan + external DPO |
| `decisions/policy/anthropic-deployment.md` | placeholder (EU AI Act Art. 29a) | 2026-05-04 | system-admin |
| `decisions/policy/robustness-testing.md` | placeholder (Phase 2a ISO 24029-2) | 2026-09-01 | Ruslan |
| `decisions/policy/dach-mittelstand-conventions.md` | placeholder (R2 FP8) | 2026-05-11 | Ruslan + external DACH advisor |
| `decisions/policy/tom-security-measures.md` | placeholder (Art. 32 TOMs) | 2026-05-04 | system-admin |
| `ops/gdpr-art-33-playbook.md` | placeholder (R2 FP6 breach framework) | 2026-05-11 | Ruslan + external DPO |
| `ops/gdpr-art-30-ropa.yaml` | placeholder | 2026-05-11 | Ruslan |
| `ops/gdpr-art-13-privacy-notice-template.md` | placeholder | 2026-05-04 | Ruslan |
| `ops/gdpr-art-35-dpia-template.md` | placeholder (Art. 35 DPIA) | 2026-05-11 | Ruslan + external DPO |
| `ops/gdpr-transfer-impact-assessment.md` | placeholder (Schrems II) | 2026-05-04 | system-admin |
| `ops/regulatory-incidents/` | directory structure | 2026-05-11 | system-admin |
| `decisions/templates/jetix-viewpoint-bundle.yaml` | placeholder (Gap 5) | 2026-05-11 | framing-lead sub-role |
| `decisions/templates/audit-canonical-template.md` | placeholder | 2026-05-11 | Ruslan |
| `decisions/templates/views/` (5 viewpoint templates) | placeholder | 2026-05-18 | framing-lead sub-role |
| `decisions/templates/client-intake-problem-chr.yaml` | placeholder (Rec-16) | 2026-05-11 | sales-closer sub-role |
| `decisions/templates/kill-chr-template.yaml` | placeholder (Gap 3) | 2026-05-11 | strategy-lead sub-role |
| `decisions/templates/mht-template.yaml` | placeholder (Rec-06) | 2026-05-11 | Ruslan |
| `decisions/templates/bias-audit/` (3 templates BA-0/1/3) | placeholder | 2026-05-11 | Ruslan + ethics advisor |
| `decisions/templates/art22-explanation.md` | placeholder (P1-R2-3) | 2026-05-04 | Ruslan + external DPO |
| `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` | placeholder (Rec-22) | 2026-06-30 (Q2 close) | meta-agent + Ruslan |
| `shared/schemas/executor-binding.schema.json` | placeholder (P1-R3-5) | 2026-04-27 | system-admin |
| `shared/schemas/message.schema.json` update (`acting_as` field) | Phase 1 Day 1 update | 2026-04-25 | system-admin |
| `design/JETIX-FPF-BRIEF.md` | placeholder (R4 external brief) | 2026-06-01 | Ruslan + framing-lead sub-role |
| `design/diagrams/d6/` (6 SVG sister diagrams) | placeholder (R4) | 2026-06-30 | Ruslan |

**FPF-Steward Q2 2026 audit scope includes:** verify each placeholder
fulfilled by ETA OR ADR explains deferral. Missing artifacts past ETA
+ 2 weeks → escalation class `strategic` message к Ruslan.

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
- `wiki/foundations/shsm-primitives.md` — 5 ШСМ foundational concepts deep reference.
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

**END OF JETIX-FPF v2.0**

*Stage A v1.0 written 2026-04-20 by Claude Opus 4.7 (1M context)
orchestration: 3 parallel FPF Scholar subagents (Parts A-B / C-E / F-K)
+ Verifier subagent. Commit 2a41927.*

*Stage C v2.0 synthesized 2026-04-20 by Claude Opus 4.7 (1M context, main
session, extended-thinking-max). Synthesis integrated 4 independent
perspective reviews (commits a4cfac2 Левенчук Purist / 8dd5420 DACH
Compliance / 0e15f52 AI-Agent Designer / 582349f Enterprise Reader).
Structural decision: Option C hybrid — academic-lineage material
moved к wiki/foundations/ companions, Jetix application preserved
in-place. All 12 P1 findings from 4 reviewers addressed (fix-applied /
deferred-to-companion / rejected-with-rationale). All 5 cross-reviewer
themes (T1 RU/EN language / T2 Operationalization / T3 Reference-chain /
T4 PP discipline / T5 Cost) addressed.*

*Conflict-resolution ranking (per Stage C prompt): Ontology fidelity >
Reader clarity > Compliance > AI-Agent operational. R1 Левенчук Purist
wins direct conflicts. Exception: P3-R1-5 RoleMask cross-ref rejected-
with-rationale — v1 citation C.3.4 actually correct per FPF-Spec
verification `grep -n "^## C\.3\.4"` → L.34687 RoleMask; R1 reviewer
finding was incorrect.*

*D6 v2 state: **draft-synthesized** — awaiting Stage D independent
final verification. Unblocks Stage 4 D1/D2/D3/D4/D5/D7/D8 writing after
Stage D sign-off.*
