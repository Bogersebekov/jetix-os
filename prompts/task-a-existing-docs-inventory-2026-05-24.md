---
title: Task A — Existing Docs Inventory (системное описание + tools/templates)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 5
ack_source: Ruslan voice 24.05 «все документы которые есть для описания системы + отдельно шаблоны/инструменты которые даются людям»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: task-a-existing-docs-inventory
R: refuted_if_LOCK_modified_OR_inventory_incomplete_OR_R1_strategic_prose_authored
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + append-only
estimated_runtime: 2-3h autonomous (substrate compile)
estimated_cost: <€1
language: russian primary
priority: ⭐⭐⭐ PREREQUISITE для PoD-24.05 Шаг 4 Core ideas + Plan B Docs execution
parent_pod: daily-logs/_PLAN-OF-DAY-2026-05-24.md
parent_synthesis: decisions/strategic/SYNTHESIS-EXECUTION-PLANS-2026-05-24.md
parent_plan_mode: decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
mode: INVENTORY (substrate compile only, NO new docs creation)
---

# 📋 Task A — Existing Docs Inventory

> **Trigger:** Ruslan voice 24.05 «collect ВСЁ что есть для описания системы + отдельно tools/templates которые даём людям».
>
> **Mode:** INVENTORY — substrate compile only. NO new docs. NO content interpretation. Just classify + map.

---

## §0 Pre-flight

1. **Memory:** constitutional + breadth (surface ВСЁ) + no-unsolicited
2. **Substrate read (FULL repo scan для docs):**
   - `decisions/strategic/` — all strategic docs
   - `decisions/` — all decisions
   - `wiki/concepts/` — 13 existing + 49 NEW Tier A/B-Plus
   - `swarm/wiki/foundations/` — Foundation 11 Parts + Pillar A/B/C
   - `swarm/wiki/synthesis/` — overviews
   - `principles/` — Tier 1+2 + R12
   - `shared/schemas/` — F-G-R / contracts
   - `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md`
   - `JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md`
   - `_HANDOFF_*` files (root)
   - `daily-logs/` recent
   - `reports/` recent (synthesis / plan-mode / lev-master / 4 researches)
   - `tools/` — все scripts (для Task A.2 tools inventory)
   - `crm/` — CRM system (для Task A.2 tools inventory)
   - `_meta/` — conventions
   - Root level all `*.md`
3. **NOT applying §11.0 MAX-density** — Task A = inventory. Speed > depth.

---

## §1 5 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + full repo scan | `reports/task-a-existing-docs-inventory-2026-05-24/phase-0-scan.md` |
| **1** | ⭐⭐⭐ **Task A.1 — System Description Docs Inventory** (всё что описывает Jetix систему) | `01-system-description-docs.md` (~500 lines) |
| **2** | ⭐⭐ **Task A.2 — Tools/Templates Inventory** (всё что мы даём / можем дать people) | `02-tools-templates-inventory.md` (~400 lines) |
| **3** | ⭐ **Cross-reference matrix** — какой doc для какого audience / какого funnel stage / public-private | `03-cross-reference-matrix.md` (~300 lines) |
| **4** | Main consolidated + Summary + 3-4 mermaid + push | `decisions/strategic/TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md` (~6-10K) + Summary ≤500w |

---

## §2 Phase 1 — System Description Docs (Task A.1)

**Categories:**

### §2.A Foundation layer (canonical LOCKED)
- 11 Parts F5 LOCKED
- Pillar A (Part 11 Strategic Direction)
- Pillar C (principles/ — Tier 2 12 rules incl R12 LOCK)
- shared/schemas/
- Vision FUNDAMENTAL
- FPF Constitutional Spec
- 8 RUSLAN-ACK records

### §2.B Strategic canonical (4 LOCKED + sub-deliverables)
- Method V2 main + 16 phase reports + 40 mermaid
- Strategic Plan Near-Future + 14 phases + 31 mermaid
- Economic Model V10 Hybrid + 3 sub-docs + 32 mermaid
- AI Market PLAN Stage 1 + Stage 2 scoped
- Partner Offering Human-Lang
- Navigation Guide DRAFT
- POINT-A / POINT-B compact / POINT-B-FOCUSED Week 1
- 25+ other sub-deliverables (TRIPLE-ROLE / RECURSIVE / TOKENOMICS-VARIANTS / etc.)

### §2.C Wiki layer
- 13 existing Tier A wikis
- 49 NEW Tier A/B-Plus wikis (3 + 31 + 15)
- wiki/index.md + wiki/log.md
- wiki/_templates/

### §2.D Research outputs (5 + lev-master)
- RESEARCH-METHODOLOGY / SOTA / PROPAGANDA-RECRUITMENT / NLP / LEVENCHUK-MASTER-QUALIFICATION
- Plus DR-26 (unit-econ) / DR-33 (communication) / DR-34 (AI commoditisation) / DR-38 (8-component meta-method) / DR-40 (cybernetic)

### §2.E Synthesis + plan-mode + Plan-of-Day
- SYNTHESIS-EXECUTION-PLANS-2026-05-24
- PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24
- PoD-24.05 + history

### §2.F Concepts / ideas pool
- ideas/ folder
- knowledge-base/ legacy

**Per-doc:** title / path / size / public-or-internal / R12 status / cross-cite count / last-modified.

---

## §3 Phase 2 — Tools/Templates Inventory (Task A.2)

**Categories:**

### §3.A Skills / commands (что мы можем dispatch)
- 25+ `.claude/skills/` (plan-day / close-day / ingest / ask / lint / consolidate / build-graph / project-bootstrap / etc.)
- 10 CRM skills (/crm-*)
- KM MVP skills (/project-bootstrap / /project-review / etc.)

### §3.B Scripts / tools (`tools/` folder)
- voice-pipeline (transcribe / extract / filter)
- mistral-ocr scripts
- toggl entries + push
- activitywatch aggregate.py
- monetization tools
- crm scripts (Python CLI)

### §3.C ROY swarm agents (17 total) — agents-as-tools
- 9 original (brigadier + 5 experts + 4 sub-brigadiers)
- 8 NEW book-driven (propaganda / recruitment / nlp / sota-tracker / methodology-engineer / ml-ai-foundations / influence-ethics / gamification)

### §3.D Wiki templates (`wiki/_templates/`)
- Per-entity-type templates (concepts / sources / topics / etc.)

### §3.E Notion templates (existing in repo OR planned)
- (currently mostly planned per Plan C; existing Notion templates если есть)

### §3.F Charter / outreach templates (planned via Plan B but maybe existing draft)
- Per-tier Charter draft (L4 / L5 / L6 / L7)
- R12 paired-frame 8-item checklist template
- Welcome-frame R12-compatible message template

### §3.G Voice / video / writing tools
- Wispr Flow (Ruslan's external tool)
- Recording setup (planned per Plan A)
- Mermaid style guide

**Per-tool:** name / path / category / status (active / planned / deprecated) / who-uses (Ruslan / partners / cohort) / docs-link.

---

## §4 Phase 3 — Cross-reference matrix

**Per-doc:**
- Which audience archetype consumes? (Левенчук / MIM-inner / Karpathy-tier / Дмитрий-humanitarian / cohort member / external general)
- Which funnel stage applicable? (Stage 0-7 per PoD-24.05 Шаг 2 §B)
- Public-or-private (4-level per Plan B classification: P1 public ready / P2 landing / P3 NDA / P4 never-share)
- R12 status (clean / needs review / R12-violating-MUST-skip)
- Cross-references map

**Output:** matrix table — N docs × 6 dimensions = ready-to-use map для Plan B execution.

---

## §5 Acceptance criteria

- ✅ 5 phases per-phase commit + push (`[task-a] Phase N`)
- ✅ ALL repo strategic docs inventoried (min 80+)
- ✅ ALL tools/templates inventoried (min 50+)
- ✅ Cross-reference matrix complete
- ✅ 3-4 mermaid diagrams
- ✅ R1 surface only (NO content interpretation)
- ✅ INVENTORY mode — NO new docs creation
- ✅ Constitutional posture preserved

---

## §6 Operational

- Per-phase commit + push
- Russian primary
- NO LOCK modifications
- NO content interpretation — pure inventory + classification
- Pool result only

---

## §7 Final push

```bash
git add reports/task-a-existing-docs-inventory-2026-05-24/ decisions/strategic/TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md
git commit -m "[task-a] Phase 4 Main + Summary + final push (5 commits / Task A.1 system description docs / Task A.2 tools-templates / cross-ref matrix / inventory only NO new docs / R1 surface)"
git push origin main
```

---

## §8 What this prompt does NOT do

- ❌ NOT create new docs (INVENTORY only)
- ❌ NOT modify existing content
- ❌ NOT interpret content
- ❌ NOT promote anything
- ❌ NOT trigger downstream
- ❌ NOT R1 strategic prose

---

## §9 К чему ведёт

После finish:
- **Plan B Docs execution unlocked** — gap analysis precise (knows what exists vs missing)
- **Шаг 4 PoD Core ideas selection unlocked** — full doc landscape visible
- **Plan C Notion templates** has reference set для adaptation
- **Plan A Video script** has substrate inventory для reference

---

*Inventory prompt closure 2026-05-24. Pure compile mode. Per Ruslan voice ack «всё в кучу собрать».*
