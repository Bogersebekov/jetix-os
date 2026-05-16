---
title: Honest self-audit — наша работа vs Левенчуковский bar
date: 2026-05-17
type: distillation-self-audit
parent_prompt: prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md §5
F: F4
G: distillation-self-audit
R: refuted_if_classification_overstates_intelligence_OR_understates_FPF_derivative
prose_authored_by: claude (scribe; surface facts; no eval «good/bad»)
language: russian + english
purpose: |
  Per Левенчуковский TG 2026-05-17 C3: «не очень верю, что у вас усиление интеллекта
  будет как-то больше, чем у vanilla AI-агента». Honestly classify Jetix components
  по 4 categories: memory / automation / intelligence amplification / FPF-derivative.
  Без selection «good/bad». Surface facts.
---

# Honest Self-Audit — Jetix components vs Левенчуковский intelligence amplification bar

> **Constitutional posture.** Scribe-mode. No eval «better/worse». Just classification
> + diff against FPF equivalent. Per prompt §5.1.

---

## §1 Classification rubric

- **memory** = aggregates / stores / retrieves information; passive accumulator
- **automation** = executes scripted action chain; replaces human key-presses
- **intelligence amplification** (Левенчуковский bar per FPF Spec L674):
  - bounded contexts declared explicitly
  - role-method-work separation enforced
  - F-G-R per claim
  - abductive loop (alternatives portfolio NOT first-answer)
  - multi-view publication (audience-specific aligned outputs)
  - generative architecture (errors structurally hard to commit)
- **FPF-derivative** = adopted/adapted FPF mechanism (acknowledged or not)

---

## §2 Foundation v1.0 — per-Part audit

| Part | Component | Type | Левенчуковский equivalent | Diff |
|------|-----------|------|---------------------------|------|
| Part 1 | System State Persistence | **memory** + structural | A.15.1 U.Work + tooling layer | Stores work state; не enforces alpha-state-graph past-participle convention; storage layer-only |
| Part 2 | Signal Ingestion & Triage | **memory** + automation | B.4.1 route publication + B.5.2.0 abductive handoff (concept-level) | Triage logic informal; не has F-G-R per signal |
| Part 3 | Knowledge Base & Methodology Library | **memory** | F.17 UTS storage substrate + Part F unification suite | Mostly retrieval substrate; UTS не in FPF formal sense (informal glossary) |
| Part 4 | Role Taxonomy & Coordination Protocol | **FPF-derivative + intelligence** | A.2 U.Role + A.2.1 U.RoleAssignment + A.13 Agential Role | Direct adoption; IP-1 Role≠Executor explicit; method-signature не yet enforced (RUSLAN-LAYER overlay incomplete) |
| Part 5 | Compound Learning & Methodology Capture | **memory + automation** | E.9 DRR governance + B.4 Canonical Evolution Loop | Captures cycles; не has explicit DRR shape; learning loop informal |
| Part 6a | Provenance Officer | **FPF-derivative + intelligence** | F-G-R B.3 + A.10 Evidence Graph Referring | Strong direct adoption (F8 grade halt-log-alert); F-G-R lint enforced |
| Part 6b | Human Gate | **FPF-derivative** | E.5.* Guard-Rails + Default-Deny Norm-CAL adjacent | Constitutional structure; не FPF-vocabulary-aligned terminology but mechanism-aligned |
| Part 7 | Project Lifecycle Substrate | **memory + automation** | A.4 Temporal Duality + B.4 Canonical Evolution Loop | Stage-gate mechanic adopted; abductive loop NOT implemented |
| Part 8 | Health Monitoring & System Integrity | **automation** | B.3 assurance levels + telemetry pattern | Operational health; не FPF-aligned «scale-aware» characteristics |
| Part 9 | Owner Interaction Scaffold | **memory + automation** | A.2 Role (owner role) + A.16 language-state transduction informal | Manager/owner cadence; not abductive |
| Part 10 | External Touchpoints & Network Interface | **automation** | F.9 Bridges (cross-context) | Touchpoint management; bridges informal |
| Part 11 | Strategic Direction Substrate (Pillar A) | **memory + structural** | E.9 DRR + E.17 MVPK (multi-view) for strategy artifacts | Stores 29 D-Lock entries + 6 strategic insights; не has multi-view publication enforced |
| Pillar C | Principles | **FPF-derivative + intelligence** | E.2 Eleven Pillars + E.5.* Guard-Rails analog | Two-tier (12 Tier-2 hard rules); direct adoption of «principles-as-canon» pattern |
| Strategic Layer Phase 1 | 7 templates exemplar | **structural** | E.8 Pattern template equivalent (informal) | Templates exist; не formal Conformance Checklists |

### §2.1 Foundation aggregate read

- **Direct FPF-derivative** (4 Parts): Part 4 + Part 6a + Part 6b + Pillar C — strong adoption of role taxonomy + F-G-R + guard-rails + pillars-as-canon
- **Memory-dominant** (5 Parts): 1, 3, 5, 9, 11 — mostly substrate / storage / capture
- **Automation-dominant** (3 Parts): 2, 7, 8 — pipelines / triage / monitoring
- **Mixed memory + structural-intelligence** (3 Parts): 2 (signal triage adjacent к B.4.1), 5 (compound learning ≈ DRR shape), 10 (touchpoints ≈ F.9 informal)

**Surface.** Foundation v1.0 has 4 direct FPF-derivative parts + 11 supporting Parts in memory/automation/structural roles. Foundation is **organisational substrate** (per its own self-description) — это substrate FOR intelligence amplification, не сама intelligence amplification.

### §2.2 Per Левенчуковский C3

> «Ваш scope = «проектное управление, монетизация, сообщество» и прочее, что должно работать на «памяти» и «автоматизации».»

**Honest match.** Project management, monetization, community — все три substrate concerns. Foundation Parts 7+10+11 directly serve these. Per classification above: Part 7 + 10 = memory+automation; Part 11 = memory + structural. **C3 partially honest** for these three Jetix concerns.

**Partial counter.** Part 4 + 6a + 6b + Pillar C ARE FPF-derivative — но это applied к organisational coordination, не к novel intelligence work itself.

---

## §3 Wiki Architecture v2 — audit

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| `wiki/index.md` | memory | TBD (UTS adjacent) | Catalog only; no UTS discipline |
| `wiki/log.md` | memory | A.16.0 language-state lineage adjacent | Append-only chronology; informal |
| 9 entity types (concepts/ entities/ sources/ topics/ ideas/ claims/ summaries/ foundations/ + comparisons/) | memory + structural | A.1 Holon (entities/) + C.2.1 U.Episteme (claims/) approximation | Conceptually aligned but not enforced as formal episteme slot graphs |
| `wiki/niches/` 6 cross-cuts | memory + structural | A.1.1 BoundedContext informal version | Bounded-context idea; not formally typed |
| `wiki/graph/edges.jsonl` (9 edge types) | memory + structural | A.6.5 SlotKind/ValueKind/RefKind adjacent | Typed relations; не yet RelationSlotDiscipline rigor |
| `/ingest` skill | automation | analog (no FPF analog — pure tooling) | Pipeline only |
| `/ask` skill | **intelligence partial** | B.5 reasoning cycle + B.5.2 abductive (claim-only) | Search + synth с citations; не enforces abductive alternatives portfolio unless OFFLINE_MODE constraints |
| `/lint` skill | automation | Conformance Checklist tooling (E.8 shape) | Health checks; informal |
| `/consolidate` skill | automation | A.6.3.CR retextualization adjacent | Dup merging; not retextualization-discipline |
| `/build-graph` skill | automation | (no direct FPF analog — community detection tooling) | Louvain-equivalent; substrate |

### §3.1 Wiki v2 aggregate read

- **Memory + structural-only:** wiki itself, edge types, niches — substrate
- **Skills:** `/ingest`, `/lint`, `/consolidate`, `/build-graph` = automation
- **Intelligence partial:** `/ask` = approaches abductive but doesn't enforce portfolio
- **NO direct U.Episteme implementation** — `claims/` is closest but slot graph not enforced

**Surface.** Wiki v2 = **knowledge storage + retrieval substrate**, NOT knowledge processing intelligence amplification. Per Левенчуковский bar this is memory + automation.

---

## §4 AutoResearch (Karpathy pattern + B2 Rich mini-swarm)

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| Karpathy LLM Wiki substrate | memory + structural | Pedagogical Companion territory (E.17 didactic) | Substrate idea aligns; не FPF-internal |
| B2 mini-swarm coordinator | automation | A.2 Role + A.15 Role-Method-Work | Role-binding lite version |
| Stage-gate mechanic (B3 merged into B2) | structural + automation | A.4 Temporal Duality + B.4 Canonical Evolution Loop adjacent | Reversibility via /project-de-morph; not full FPF evolution loop |
| `/project-bootstrap` (4 types + mini-swarm + client namespace) | automation | (no direct analog; tooling) | Substrate |
| `/project-review`, `/project-archive`, `/project-promote` | automation | E.9 DRR-shaped artifacts emerging | Decision records exist; not formal DRR |
| Predicate-based stage gates (`/lint --check-stage-gates`) | structural + automation | A.6.B Claim Register adjacent (gate-claims) | Predicates lint; informal claim register |

### §4.1 AutoResearch aggregate read

- **Memory + automation-dominant** overall
- **Approaching structural-intelligence** via stage-gate predicates + role-binding
- **NOT abductive** — stage-gates verify completion, не generate alternatives
- **NOT full F-G-R** — claims (predicates) exist but не formally tagged

**Surface.** AutoResearch = sophisticated automation + light structural FPF-aligned mechanics. Per Левенчуковский bar this is automation + structural, не intelligence amplification.

---

## §5 Voice pipeline + Toggl + CRM

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| Voice pipeline (transcribe + extract + filter + review) | automation | (no direct analog; tooling) | Transcription + triage |
| Voice → CRM DRAFT (voice_router) | automation | (no direct analog) | Routing tooling |
| Toggl tracking / time discipline | **memory** | (no direct analog) | Pure logging |
| CRM 14-section schema | memory + structural | A.2 Role analog (relationship-roles per crm/_schema/roles.yaml) | Stores; не FPF-aligned terminology |
| CRM pipeline statuses (13) | memory + structural | A.2.5 RoleStateGraph adjacent (past-participle informal) | Past-participle inspired but informal |
| `/crm-stuck`, `/crm-weekly` etc | automation | (no analog) | Health tooling |

### §5.1 Voice + Toggl + CRM aggregate read

- **Pure memory + automation** — these are operational substrate
- **NOT intelligence amplification** by any rubric

**Surface.** Per Левенчуковский C3 these are explicitly «память + автоматизация». No claim to amplification here.

---

## §6 Monetization bank 166 H (raw signals catalog)

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| 166 monetization hypotheses catalog | **memory + structural** | G.1 SoTA harvesting adjacent (informal) | Catalog of opportunities; not yet selector/dispatcher discipline |
| Grouping by H1-H8 (capability portfolio) | structural | G.0 portfolio publication shape | Approaches portfolio publication; not full G.0 |
| Per-H scoring | **memory** | A.17-A.19 Characteristic/Scale/Level adjacent | Implicit scoring; не formal characteristic spaces |

### §6.1 Monetization aggregate read

- **Memory-dominant** with hint of structural portfolio shape
- **NOT abductive** — doesn't generate H_167+ from first principles
- **NOT FPF-aligned formal portfolio** — informal grouping

**Surface.** Monetization bank = catalog. Per Левенчуковский bar = memory. Could BECOME a G.1 SoTA pack if formally structured.

---

## §7 Strategic Insights Hexagon (H1-H7) + Document 1A/1B

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| Hexagon synthesis (H1-H7 insights 2026-05-10/11) | **intelligence amplification (partial)** + memory | B.5.2 Abductive Loop output + E.9 DRR shape | Generated alternatives explicitly; provenance per insight; F-G-R tagged |
| H7 People-NS LOCKED | intelligence amplification + structural | DRR + Pillar A direction | Strategic decision Ruslan-authored с D-Lock entry |
| R12 anti-extraction packet | intelligence amplification + FPF-derivative | E.9 DRR + constitutional addition (Pillar C Tier-2 candidate rule) | Game Theory M-C mechanism §11 backing |
| Document 1A (single page Charter) | structural | E.17.0 U.View public-facing | Multi-view shape; informal |
| Document 1B (longer narrative) | structural | E.17 MVPK Plain face | Same |

### §7.1 Strategic Insights aggregate read

- **THIS is the closest to intelligence amplification in Jetix** — abductive output, F-G-R, multi-view (1A/1B), provenance trail
- **Still draft-grade** (F2-F4 max so far; not F8 normative)
- **Direct FPF-derivative discipline** without explicit FPF terminology

**Surface.** Strategic Insights = closest analog к Левенчуковский intelligence work. Without FPF spec loaded explicitly but reasoning shape converging on FPF abductive + DRR + MVPK patterns.

---

## §8 archive/design/JETIX-FPF.md (3762-line derivative — archived)

| Aspect | Read |
|--------|------|
| Type | **FPF-derivative** (heavy + acknowledged) |
| FPF equivalent | direct attempted adaptation of FPF spec к Jetix domain |
| Diff | Per CLAUDE.md walkthrough: archived 2026-05-06 because «ROY layer pre-Foundation construction — wrapped в Foundation Part 4 + Pillar C» |
| Authoritative status | NOT canonical; archived for history |
| Honest assessment | Heavy 3762-line attempt к FPF formality; superseded by simpler Pillar C + Part 4 + boot context inlining |

**Per Левенчуковский TG C1 2026-05-17:**
> «у нас много более скромные интересы: я вот делаю FPF, и там не так много документов, как у вас, всего один»

**Honest read.** JETIX-FPF.md = naive derivative attempt; **Левенчук's critique direct hit.** Levenchuk has 1 doc (FPF-Spec.md), we made 3762-line derivative interpretation. Then archived и replaced с simpler Pillar C structure. Implicit acknowledgement of overreach.

---

## §9 F-G-R / Default-Deny / AWAITING-APPROVAL

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| F-G-R per claim (shared/schemas/f-g-r.json) | **FPF-derivative + intelligence** | B.3 F-G-R Trust & Assurance | **DIRECT ADOPTION** per CLAUDE.md §4.1 boot context |
| Default-Deny table (.claude/config/default-deny-table.yaml) | FPF-derivative + automation | E.5.* Guard-Rails analog + Norm-CAL deontic constraints | Adapted (11 entries from Pillar C Tier-2 foundation_generic) |
| AWAITING-APPROVAL packet (shared/schemas/) | FPF-derivative + structural | E.9 DRR shape + B.3 escalation | Mechanism-adopted; terminology Jetix-specific |
| Halt-Log-Alert (Part 6b §I.2) | FPF-derivative + automation | B.3 grade enforcement + assurance escalation | F8/F4/F2 grade halts adopted |

### §9.1 F-G-R aggregate read

- **DIRECT FPF-derivative + intelligence** — это самая чистая прямая adoption
- Acknowledged в CLAUDE.md §4.1: «Per FPF B.3»

---

## §10 IP-1 Role≠Executor

| Component | Type | FPF equivalent | Diff |
|-----------|------|----------------|------|
| IP-1 Role≠Executor (Bundle 1 RUSLAN-ACK) | **FPF-derivative + intelligence** | A.2 Role + A.13 Agential Role + RUSLAN-LAYER overlay | DIRECT adoption per CLAUDE.md §4.1 + executor-binding.yaml.template |
| executor-binding.yaml.template | structural | A.2.1 U.RoleAssignment | Template adopted |

### §10.1 IP-1 aggregate read

- **Direct FPF-derivative** with explicit RUSLAN-LAYER overlay extension
- One of strongest FPF adoptions в Jetix

---

## §11 Cross-component summary table

| Type | Count of Jetix components | Notes |
|------|---------------------------|-------|
| **memory-dominant** | ~15 (Foundation Parts 1,3,5,9,11 + Wiki substrate + Toggl + Monetization bank + CRM storage + voice transcripts) | substrate accumulation |
| **automation-dominant** | ~12 (Foundation Parts 2,7,8 + Wiki skills + AutoResearch ops + voice pipeline + CRM ops + Halt-Log-Alert + Default-Deny enforcement) | substrate execution |
| **intelligence amplification (partial)** | ~5 (Strategic Insights Hexagon + `/ask` skill + Pillar C 12 rules + Provenance Officer + Hexagon multi-view 1A/1B) | structurally aligned с FPF abductive + F-G-R + DRR |
| **FPF-derivative (direct adoption)** | ~7 (F-G-R schema + IP-1 + Default-Deny table + Pillar C principles + Guard-Rail analog + AWAITING-APPROVAL + executor-binding) | terminology often differs from FPF but mechanism direct |
| **FPF-derivative (heavy archived)** | 1 (JETIX-FPF.md 3762 lines) | superseded by simpler structure |

---

## §12 Левенчуковский C3 honest answer

> «не очень верю, что у вас усиление интеллекта будет как-то больше, чем у vanilla AI-агента.»

**Honest answer based on §1-11:**

- **~27 memory + automation components vs ~12 intelligence/FPF-derivative components** — C3 critique partially correct: bulk is substrate.
- **HOWEVER, ~12 intelligence/FPF-derivative components ARE there** — F-G-R + IP-1 + Pillar C + Strategic Insights + Provenance Officer = converging on FPF amplification mechanisms.
- **Gap to Левенчуковский bar:** abductive loop NOT formally implemented; multi-view publication informal; UTS не formal; Claim Register absent; bridges informal.
- **NOT vanilla AI**: F-G-R discipline + Default-Deny + Halt-Log-Alert + provenance enforcement = real architectural intelligence support, не vanilla.
- **Not yet FPF-grade either**: derivative attempt (JETIX-FPF.md archived) shows we tried + retreated; current state = lighter FPF-aligned mechanisms applied tactically, без full FPF-Spec loaded as context.

**Conclusion (surface, no eval):**
- C3 = «mostly right» (bulk = substrate)
- C3 = «not fully right» (4 direct FPF adoptions + ~5 intelligence-amplification-partial components present)
- Honest read: **Jetix = memory + automation + ~25% structural-intelligence + ~10% FPF-derivative — but missing full Левенчуковский intelligence amplification layer.**

---

## §13 What we have that's UNIQUELY ours (NOT FPF-derived)

Per prompt §5.1.2 «**Если есть уникальные intelligence mechanisms у нас (которых нет в FPF) — surface их.**»

| Our unique | What it is | FPF parallel? |
|------------|------------|---------------|
| Strategic Insights Hexagon (6 insights weekly cadence) | Structured weekly Левенчуковский-style synthesis but Jetix-domain-specific | Loose: abductive loop output + DRR shape |
| R12 anti-extraction (constitutional candidate rule 12 — additive 2026-05-12) | Anti-extraction principle: substrate cannot extract value from members beyond agreed share; fork-and-leave without penalty | NOT in FPF — Pillar C addition derived from Game Theory M-C + H7 People-NS |
| 5 layers per-agent memory (Core/Strategies/Scratchpad/Niche/Recall) | System Prompt Learning + per-agent compounding | NOT in FPF — Jetix-specific (informed by Karpathy LLM Wiki + Claude Code architecture) |
| Stage-gated B2 mini-swarm с de-morph reversibility | Project-type-aware orchestration with stage-gate predicates | A.4 Temporal Duality adjacent but не this specific shape |
| F2-F8 6-level Formality grade scale (Part 6a) | Quantized formality levels for halt-log-alert grade enforcement | B.3 mentions F2-F8 but Jetix encoding more operational |

**Honest.** ~5 unique mechanisms — small but real. None compete с full FPF spec; they extend / specialize.

---

## §14 What's the path forward (Phase B input)

Per prompt §11 + §0.0 — NOT to start Phase B now. But this audit prepares it:

1. **Direct adoptions that work:** keep F-G-R + IP-1 + Pillar C + Default-Deny + Halt-Log-Alert
2. **Partial intelligence to strengthen:** convert Strategic Insights process к explicit B.5.2 Abductive Loop + E.9 DRR shape
3. **Missing mechanisms to add (Phase B integration plan items):**
   - U.UTS (F.17) для glossary discipline
   - A.6.B Claim Register для contracts/spec text
   - F.9 Bridges для cross-niche translations
   - U.EpistemeSlotGraph for claims/
   - MVPK (E.17) for 1A/1B-style multi-view
4. **Heavy derivative to deprecate / reuse:** archive/design/JETIX-FPF.md — wrapped in simpler structure but content could feed adaptations

---

*Audit complete. Surface facts only. Phase B uses this for integration plan.*
