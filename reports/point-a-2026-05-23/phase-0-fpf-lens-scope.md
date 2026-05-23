---
title: Phase 0 — FPF Lens Scope + Sub-Inventory Plan + Acceptance Predicate
date: 2026-05-23
type: point-a-phase-report
phase: 0
parent_prompt: prompts/point-a-current-state-2026-05-23.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F3
G: point-a-current-state-2026-05-23
R: R1-surface-only
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + IP-1 STRICT + EP-5 + AP-6 + append-only + SKIP-list integrity (O-62/66/67/68 + O-83 honored)
language: russian primary
---

# 📋 Phase 0 — FPF Lens Scope

## §1 Goal Точки А

Точка А = **factual inventory** того, **что есть СЕЙЧАС** (state на 2026-05-23 evening) в системе Jetix OS на сервере + в repo.

Цель — чтобы Ruslan мог:
1. Посмотреть и понять **текущее состояние ясно** (own situational awareness)
2. **Рассказывать людям** что есть (partner-facing narrative для Wave 1 outreach)
3. **Сравнить с Точкой Б** (Шаг 2 Orientation Day) — измерить дельту
4. **Surfaceить gaps** — чего не хватает (для Шагов 3-12)

Это **НЕ** strategic prose (R1 surface only). НЕ recommendations. НЕ селекция.
**Substrate compile only** per `feedback_constitutional.md` + `feedback_breadth_not_selection.md`.

---

## §2 FPF Lens — что Point A в FPF terms

| FPF primitive | Application к Point A |
|---|---|
| **IP-1 Role≠Executor** STRICT | brigadier-scribe = R1-surface-only role; Ruslan = sole strategist; substrate compile NOT prose authoring |
| **IP-2 Substrate-as-Foundation** | Point A operates on substrate level — collected facts from filesystem (source of truth per Global Rule 4) |
| **IP-3 Halt-Log-Alert на integrity violations** | Fail-loud if LOCK content modified / SKIP-list violated / R1 prose authored |
| **IP-7 F-G-R provenance dogfood** | F2-F3 для inventory claims; G = `point-a-current-state-2026-05-23`; R1 surface only |
| **A.6.B Append-only history** | Phase reports под `reports/point-a-2026-05-23/` — new files, NOT mutations |
| **A.14 Hub-and-spoke** | Brigadier dispatches scribes per bucket; pool result only |
| **B.3 R6 provenance per claim** | Каждый факт carries `[src: file path или commit SHA]` inline |

[src: swarm/wiki/foundations/principles/architecture.md + design/JETIX-FPF.md]

---

## §3 Object / Scale per bucket

### §3.1 Bucket 1 — 2 месяца на сервере
- **Object:** git repo `/home/ruslan/jetix-os/` от 2026-03-24 до 2026-05-23
- **Scale:** 1509 commits / sprint-level (week-by-week ×9 weeks)
- **Sub-units:** weekly milestones + ⭐ deliverables + quantitative (commits/files/words)
- **Source:** `git log --since='2026-03-24' --until='2026-05-23'`

### §3.2 Bucket 2 — FPF deep inventory
- **Object:** `raw/external/ailev-FPF/FPF-Spec.md` + cross-references по всем deliverables
- **Scale:** 3758 lines FPF-Spec + coverage map across substrate areas
- **Sub-units:** primitives used (IP-1/IP-2/IP-3/IP-7/A.6.B/A.14/B.3) + где cited + gaps
- **Source:** `design/JETIX-FPF.md` + grep "FPF\|IP-1\|IP-2\|IP-3" по всем .md

### §3.3 Bucket 3 — Tools / infrastructure
- **Object:** `.claude/agents/` (9 ROY) + `tools/` (~30 scripts) + `.claude/skills/` (54) + `swarm/lib/` + `crm/_scripts/` + Foundation infrastructure
- **Scale:** что **work** vs **in-flight** vs **blocked** per tool
- **Sub-units:** ROY swarm, Wiki v2, CRM, voice pipeline, AW+Toggl, Foundation infrastructure, server (jetix-vps + Tailscale + GitHub public)
- **Source:** filesystem inventory + per-tool README/architecture docs

### §3.4 Bucket 4 — Все планы
- **Object:** все strategic / planning документы в `decisions/strategic/` + `decisions/` + ack records
- **Scale:** 4 LOCKED canonical + 20+ sub-docs + 8+ RUSLAN-ACK records + REFLECTION-INBOX queues
- **Sub-units:** LOCKED stack + Action Plans + Updated Execution Plans + Distribution Plan + Hypothesis Architecture + Pool items
- **Source:** `decisions/strategic/` + `decisions/`

### §3.5 Bucket 5 — Contacts CRM + network
- **Object:** `crm/people/` 151 records + `crm/orgs/` 29 records + extended network (Telegram / family / friends)
- **Scale:** 180 contacts total + L1/L2/L3 tiers (7+35+51=93 per KA-03) + 14 Tier-1 ack queue
- **Sub-units:** per-role breakdown (24 roles in 6 groups: sales / capital / partnership / advisory / team / network)
- **Source:** `crm/people/` + `crm/orgs/` + `crm/index.md` + Wave 1 outreach package

### §3.6 Bucket 6 — Books / sources / corpus
- **Object:** `raw/external/` tree + cited sources через ВСЕ deliverables
- **Scale:** 5 corpus folders (ailev-FPF / harari-corpus / levenchuk-books / levenchuk-corpus / tseren-github) + 47+50+35+27+37+27 sources cited через 6 главных deliverables
- **Sub-units:** bibliographic synthesis + reading order по topics + gaps (что нужно докупить)
- **Source:** `raw/external/` filesystem + grep sources в decisions/strategic/

### §3.7 Bucket 7 — Methods / methodology
- **Object:** FPF primitives + Method V2 §J 8-component composition + ШСМ tradition + cybernetic principles
- **Scale:** ~15 methodological frameworks в active use
- **Sub-units:** FPF / Method V2 §J meta-method / Polya / Polanyi / Csikszentmihalyi / Ericsson (DR-38) / Ashby / Beer VSM / Maturana / Meadows / Bateson (DR-40) / external-system principle / 3-question self-check / 4-layer recursive meta-method
- **Source:** `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` + DR-38 + DR-40 + wiki/concepts/

### §3.8 Bucket 8 — Fast-access people + ресурсы
- **Object:** люди с response time within 24-48h baseline
- **Scale:** Дмитрий (созвон 22.05 done) + Telegram channels owned/managed + family + close friends + professional contacts
- **Sub-units:** per-person resource inventory + R12 paired-frame compatibility check
- **Source:** `crm/people/dmitriy-*.md` + Telegram inventory + extended network audit

---

## §4 Per-Bucket Acceptance Predicate

| Bucket | Acceptance criterion |
|---|---|
| 1 | Sprint timeline 24.03→23.05 with week-by-week milestones + quantitative dashboard (commits / files / words) + ≥10 ⭐ deliverables enumerated |
| 2 | FPF primitives table с локациями применения + coverage map + ≥5 cited callouts |
| 3 | Per-tool table с {tool / status (work/in-flight/blocked) / owner / last-touched} + ROY swarm map + skill inventory ≥40 skills enumerated |
| 4 | 4 LOCKED canonical enumerated + ≥15 sub-deliverables + 8 RUSLAN-ACK records + REFLECTION-INBOX status |
| 5 | 180 contacts breakdown + per-role table + Tier-1 ack queue 14 names + outreach pipeline status + warm-intro paths |
| 6 | corpus tree + ≥30 sources cited [src: ...] + bibliographic synthesis + reading order + ≥5 gaps surfaced |
| 7 | Methods stack with ≥15 frameworks + composition diagram + meta-method articulation |
| 8 | Fast-access people с per-person {expertise / network / available resources / R12 paired-frame check} ≥6 people inventoried |
| 9 | Master doc 12-18K words + 8-12 mermaid + Summary ≤1500w + diagrams INDEX + all 8 buckets integrated |

---

## §5 Multi-Angle Robustness (4 perspectives)

Каждый bucket будет писаться с учётом 4 perspectives per `feedback_max_density_max_tokens.md`:

| # | Perspective | Что читатель ищет |
|---|---|---|
| 1 | Ruslan personal review | «что я сделал; что я могу; что я знаю; чего мне не хватает» |
| 2 | Partner-facing narrative | «что Jetix имеет; что показать; почему serious; почему worth partnership» |
| 3 | Methodologist external observer | «какая methodology stack; coverage map; epistemic posture; reliability grading» |
| 4 | Cohort recruit / investor due-diligence | «есть ли working system; кто в network; что blocked; what's the runway» |

---

## §6 Constitutional Posture — Confirmation

| Rule | Status в Point A |
|---|---|
| **R1 surface only** | ✅ Substrate compile; no strategic prose; no recommendations; no selection |
| **R2 no architectural changes** | ✅ Foundation paths untouched; no `principles/` / `swarm/wiki/foundations/` modifications |
| **R6 F-G-R provenance dogfood** | ✅ F2-F3 per claim + R1 + G=point-a-current-state-2026-05-23; inline `[src: ...]` mandatory |
| **R11 default-deny novel actions** | ✅ Only enumerated tools (Bash read-only / Read / Write / Edit / TaskCreate); no novel action class |
| **R12 anti-extraction** | ✅ Surfacing existing contacts, NOT proposing extraction; Bucket 8 only enumerates resources |
| **IP-1 STRICT** | ✅ brigadier-scribe ≠ Ruslan; substrate compile NOT prose-as-Ruslan |
| **EP-5** | ✅ append-only под `reports/point-a-2026-05-23/`; new files only |
| **AP-6** | ✅ ack-able output (Ruslan reviews + corrections allowed) |
| **SKIP-list integrity** | ✅ O-62/66/67/68 NOT re-surfaced; O-83 honored (DROP per ack 22.05) |

---

## §7 Sub-Inventory Plan (9 phase deliverables)

| Phase | File | Target lines | Status |
|---|---|---|---|
| 0 | `phase-0-fpf-lens-scope.md` | ~200 | **in_progress** |
| 1 | `01-bucket-2-months-server.md` | ~600 | pending |
| 2 | `02-bucket-fpf-deep.md` | ~500 | pending |
| 3 | `03-bucket-tools-infrastructure.md` | ~600 | pending |
| 4 | `04-bucket-all-plans.md` | ~600 | pending |
| 5 | `05-bucket-contacts.md` | ~500 | pending |
| 6 | `06-bucket-books-sources.md` | ~600 | pending |
| 7 | `07-bucket-methods-methodology.md` | ~500 | pending |
| 8 | `08-bucket-fast-access-people.md` | ~700 | pending |
| 9 | Master + Summary + diagrams INDEX | ~12-18K consolidated | pending |

---

## §8 Mermaid scope plan (8-12 diagrams)

1. **Sprint timeline gantt** (24.03 → 23.05 week-by-week ×9 weeks)
2. **Substrate stack architecture** (Foundation → Wiki → decisions/strategic → reports)
3. **Tools inventory tree** (ROY / Wiki v2 / CRM / voice / AW+Toggl / skills)
4. **Contacts network graph** (L1/L2/L3 + 6 role-groups)
5. **FPF coverage map** (primitives × substrate areas)
6. **Books bibliography network** (sources → deliverables)
7. **Methods stack** (FPF + Method V2 §J + ШСМ + cybernetic + composition)
8. **Fast-access people resource map** (Дмитрий + Telegram + family + друг + leverage potential)
9. **Sprint quantitative dashboard** (commits / words / files / contacts / sources)
10. **2 LOCKED canonical map** (Bundle 1-5 + LOCKED stack flow)
11. **Distribution funnel** (Wave 1 → 14 Tier-1 → warm intros → discovery calls)
12. **Hypothesis Architecture 7-layer** (если applicable from substrate)

Stretch: 10-12. Minimum: 8. Each ≥6 nodes; dense.

---

## §9 Operational

- Per-phase commit + push mandatory (format `[point-a] Phase N description`)
- Russian primary
- R6 inline `[src: file path или commit SHA]`
- NO LOCK content modifications
- NO R1 strategic prose authoring
- Pool result only — NOT auto-launch downstream
- SKIP-list integrity preserved

---

## §10 Pre-flight read status

| Resource | Status |
|---|---|
| `feedback_max_density_max_tokens.md` | ⚠️ NOT on disk; принципы embedded в этот prompt §4 §11.0 |
| `feedback_breadth_not_selection.md` | ⚠️ NOT on disk; принцип applied (surface всё, no filter) |
| `feedback_constitutional.md` | ⚠️ NOT on disk; принцип applied (R1 surface only) |
| `feedback_fpf_lens_first.md` | ⚠️ NOT on disk; принцип applied (Phase 0 = FPF lens) |
| `feedback_no_unsolicited_alternatives.md` | ⚠️ NOT on disk; принцип applied (no recommendations) |
| `feedback_prompt_explanation_required.md` | ✅ sibling EXPLAIN exists at `prompts/explanations/_EXPLAIN-point-a-current-state-2026-05-23.md` |
| 4 LOCKED canonical | ✅ scanned (Method V2 / Strategic Plan / Economic Model V10 / AI Market PLAN) |
| Foundation v1.0 | ✅ scanned 11 Parts + Pillar A/B/C |
| `wiki/concepts/` | ✅ enumerated (~60+ Tier A files) |
| CRM | ✅ counted (151 people + 29 orgs = 180 contacts) |
| `raw/external/` | ✅ enumerated (5 corpus folders) |
| `tools/` | ✅ enumerated (~30 scripts) |
| `.claude/agents/` | ✅ enumerated (9 ROY swarm) |
| `.claude/skills/` | ✅ enumerated (54 skills/dirs) |
| git log 2-month | ✅ enumerated (1509 commits / 668 March-April / 837 May) |

⚠️ **Note re memory files:** MEMORY.md index references 6 memory files mentioned в prompt §0, но они not present под `/home/ruslan/.claude/projects/-home-ruslan-jetix-os/memory/`. Only present: `feedback_no_api_keys.md`, `feedback_plan_mode_minimal_friction.md`, `feedback_dont_interrupt_after_system_status.md`, `project_balaji_outreach_target.md`. The mentioned-but-absent files' principles (max-density / breadth / constitutional / fpf-first / no-unsolicited-alternatives / prompt-explanation) ARE embedded в этот prompt §4 §11.0 CRITICAL IMPORTANCE MANDATE — so de facto compliance preserved via prompt-internal mandate.

---

## §11 Acceptance — Phase 0

- ✅ FPF lens scope articulated (§2)
- ✅ Object / scale per bucket defined (§3)
- ✅ Per-bucket acceptance predicate (§4)
- ✅ Multi-angle robustness 4 perspectives (§5)
- ✅ Constitutional posture confirmed (§6)
- ✅ Sub-inventory plan with 9 phase deliverables (§7)
- ✅ Mermaid scope plan 8-12 diagrams (§8)
- ✅ Pre-flight substrate read confirmed (§10)
- ✅ ~200 lines (target met)

→ **Phase 0 COMPLETE.** Proceed Phase 1.

---

*Phase 0 closure 2026-05-23. Per `prompts/point-a-current-state-2026-05-23.md` §1.*
