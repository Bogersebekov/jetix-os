---
title: Phase 0 — FPF scope definition / каша cleanup / Jetix через FPF lens
date: 2026-05-17
type: deep-prompt
target: server CC (brigadier mode, autonomous, 4-6h)
trigger: Ruslan critique 17.05 evening — Phase B output = каша; reference frame нестабилен; нужен FPF-lens первым
parent: prompts/fpf-iwe-phase-b-2026-05-17.md (Phase B complete)
phase_b_outputs:
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - outreach/pack-for-l1-2026-05-17/
language: russian
deadline: ASAP перед отправкой L1 (или перед Phase C research)
---

# DEEP PROMPT — Phase 0: FPF scope definition / каша cleanup

> **Ты = brigadier** (per `.claude/agents/brigadier.md`, opus). Multi-agent swarm dispatch через Task() к 5 domain experts × 4 modes. Constitutional: Tier 2 R1/R2/R6/R11 + append-only + no API keys.

> **ultrathink — extended thinking ON для всей сессии и всех cell invocations.**

---

## §0 Триггер — что произошло

После Phase B (6 шагов / 15 cells / ~9000 LOC) Ruslan surface'нул критику:

1. **Каша в outputs** — Phase B working file говорит про «8 активных проектов», «12 агентов» как **факт** vs **концепция** «можно сколько хочешь добавить». Reference frame нестабилен.
2. **Compare Jetix vs IWE/FPF БЕЗ предварительного определения** — что есть Jetix? **System для управления информацией / корпорация / задумка / рабочий продукт?** Каждое = разный bar.
3. **Output непонятный** — «сравнивает что-то непонятное и берёт от кого-то залупные документы».

**Diagnosis (memory feedback_fpf_lens_first.md):** любой research/анализ БЕЗ FPF-lens-первого = каша. R1 violation замаскированная как «анализ».

**Эта Phase 0 = lens-first reset.** Перед Phase C research / final L1 messaging — **сначала через FPF определить ЧТО research'им**.

---

## §1 Цель Phase 0

**Server CC, ТЫ сам через FPF lens** (НЕ Ruslan, НЕ Cloud Cowork) предлагаешь:

1. **Inventory объектов Jetix** которые имеет смысл описать **отдельно через FPF** — минимум что Ruslan upcoming critique surface'нул (system управления инфо / корпорация / задумка / рабочий продукт), **плюс что ТЫ САМ surface'ишь** разбираясь по FPF (минимум 8-12 объектов).
2. **Per-object FPF-typed описание** — что это в FPF terms (primitive: U.System / U.Role / U.Method / U.Artefact / etc.), какой FPF Part hosts, какие primitives applicable, claims + F-G-R, bounded context.
3. **Comparison level matrix** — для каждого объекта **ТЫ предлагаешь** на каком FPF-level имеет смысл сравнивать с Левенчуковскими наработками (FPF полная) + Цэрэновскими (IWE FMT-exocortex-template + paid AI guide когда доступен). Mechanism / Artefact / Role / Outcome / System level.
4. **Каша cleanup flags** — surface всё устаревшее / противоречивое в существующих доках (Phase A+B reports, working file, Foundation, decisions/). Per item — что устарело, чем заменить.
5. **Master document Lakонично + L1-friendly** — financialfinal artefact который L1 может за 10 минут scan'ить и понять «вот что есть Jetix» структурно через FPF lens.

**Tier 2 R1.** Ruslan = sole strategist. Ты surface'ишь варианты, объекты, comparison levels — НЕ выбираешь «вот это важно, это нет». Ruslan потом ack'ает + использует.

---

## §2 Operating manual (read first)

- **FPF полная свежая версия:** `raw/external/ailev-FPF/FPF-Spec.md` (72,800 строк, vendored с upstream HEAD `c86eabd` 16.05). **Это primary source истины для FPF lens.**
- `.claude/agents/brigadier.md` — orchestration protocol
- `swarm/lib/shared-protocols.md` — Task() packet schema + §5.5.5 provenance gate
- `swarm/lib/routing-table.yaml` — dispatch matrix
- `.claude/agents/engineering-expert.md` + `philosophy-expert.md` + `systems-expert.md` + `mgmt-expert.md` + `investor-expert.md` — cells

**FPF-loaded engineering-expert** = ты dispatching `engineering-expert × integrator` cell с pre-loaded `raw/external/ailev-FPF/FPF-Spec.md` как primary context. Этот cell = «прокачанный FPF agent» per Ruslan terminology.

---

## §3 Task 1 — Inventory объектов Jetix через FPF lens

### §3.1 Что surface

Server CC, разбираясь по FPF, **сам предложи список объектов** которые имеет смысл описать **отдельно**. Минимум base (от Ruslan):

1. **Jetix как система управления информацией** (operational substrate)
2. **Jetix как корпорация / юр.лицо** (in-progress legal entity)
3. **Jetix как задумка / vision** (future state target)
4. **Jetix как рабочий продукт** (что РЕАЛЬНО работает СЕЙЧАС)

**Plus сам surface ещё 4-8 объектов** которые FPF lens предлагает:
- Jetix как methodology / pattern language?
- Jetix как community / network state?
- Jetix как business model (Phase 1 quick money)?
- Jetix как brand / public-facing positioning?
- Jetix как agent system (12 agents — концепция vs instantiated)?
- Jetix как Foundation architecture (Parts 1-11 + Pillar C)?
- Jetix как Strategic Layer (Hexagon 6+1 insights)?
- Jetix as Workshop concept?
- Jetix as personal Life OS substrate (Ruslan-specific)?
- Что ещё ты найдёшь по FPF разбору?

### §3.2 Per-object — что зафиксировать

| Поле | Содержание |
|---|---|
| Object name | Чёткое имя |
| FPF primitive | U.System / U.Role / U.Method / U.Artefact / U.Outcome / U.Plan / U.Work / U.View / etc. |
| FPF Part hosting | Part A kernel / Part B reasoning / Part C extensions / Part D ethics / Part E constitution / Part F unification / Part G SoTA kit |
| Applicable FPF primitives (list) | IP-1 Role≠Executor / B.3 F-G-R / E.5 Guard-Rails / E.9 DRR / etc. |
| Status | задумка / прорабатывается / работает-частично / работает-полно / устарело / archived |
| Bounded context | Где границы — что относится, что НЕ относится |
| F-G-R per top claim | F (F2-F8) / G (group scope) / R (low/medium/high) per FPF B.3 |
| Provenance | File paths + line refs где object реально живёт в repo |

### §3.3 Output Task 1

`reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` — exhaustive list с per-object table.

---

## §4 Task 2 — Per-object FPF-typed описание (deep)

Per object из Task 1, deep-dive:
- **Lakонично** (≤1 страницу per object)
- **Что есть** (concrete) vs **что задумано** (target) — explicit separation
- **FPF lens** — primitive + Part + applicable mechanisms
- **Claims + F-G-R triple** per top 5-10 claims per object
- **Boundaries** — что НЕ относится к этому object (anti-scope)
- **Cross-refs** к другим объектам inventory

### §4.1 Output Task 2

`reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md` — collection per object descriptions.

---

## §5 Task 3 — Comparison level matrix (с L1 наработками)

Server CC, **ты предлагаешь** per Jetix-object на каком уровне его сравнивать с:
- **FPF полной** (`raw/external/ailev-FPF/FPF-Spec.md`)
- **IWE template** (`raw/external/tseren-github-2026-05-17/FMT-exocortex-template/`)
- **IWE paid AI guide** (B2 blocked — но **что бы мы сравнивали** если бы имели доступ)
- **Левенчуковские книги** (Системное мышление / Методология / Системная инженерия / Менеджмент / Инженерия личности / Интеллект-стек / Системный фитнес-практика)
- **ШСМ residency R0/R1/R2** (blocked — apply pending)

### §5.1 Comparison levels (FPF lens)

- **Mechanism level** — конкретные функциональные паттерны
- **Artefact level** — конкретные документы / templates
- **Role level** — actor типы (manager / brigadier / expert / etc.)
- **Method level** — methodology / процедуры
- **System level** — общий ontology / architecture
- **Outcome level** — что система **производит** as deliverables

### §5.2 Per cell matrix

```
| Jetix object | Compared with | Level | Compare predicate | Why this level fits |
|---|---|---|---|---|
| Jetix system управления инфо | FPF Part A kernel | System | bounded-context discipline | both define U.System with method-method-work separation |
| Jetix корпорация | (no direct L1 analogue) | — | — | L1 corpus = methodology not corp-as-such |
| ... | ... | ... | ... | ... |
```

### §5.3 Output Task 3

`reports/phase-0-fpf-scope/03-comparison-matrix.md` — exhaustive matrix per object × L1 analogue × level.

---

## §6 Task 4 — Каша cleanup flags

Surface всё устаревшее / противоречивое в existing docs:

### §6.1 Что проверить

- **Phase A + B reports** — anything stale / contradicting?
- **`JETIX-WORKING-FILE-v0-2026-05-17.md`** — «8 активных проектов» / «12 агентов» как **факт** vs **концепция**? Other stale claims?
- **Foundation Parts 1-11** — устаревшие cross-refs?
- **`canonical/INDEX.md`** — какие из 110 doc устарели?
- **`decisions/`** — pre-Foundation overreaches не флагнутые?
- **Strategic Insights Hexagon (6+1)** — каждый insight: F-G-R triple corretно? обновлено?

### §6.2 Per stale item

| File | Line/section | Claim | Why stale | Suggested action |
|---|---|---|---|---|
| ... | ... | ... | ... | append clarification / archive / mark deprecated |

**НЕ удалять** (append-only). Только flag + suggest действие. Ruslan ack'ает action.

### §6.3 Output Task 4

`reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md` — exhaustive list устаревшего.

---

## §7 Task 5 — Master document (Lakонично + L1-friendly)

**Цель.** Документ который Левенчук / Цэрэн читают **10 минут** и понимают:

- Что **есть** Jetix (через FPF terms)
- Что **в работе** (через FPF terms)
- Что **задумано** (через FPF terms)
- Где **fits** с FPF / IWE
- Где **extends** FPF / IWE
- Где **orthogonal**

### §7.1 Structure

- §0 1-фраза TL;DR (FPF terms)
- §1 Inventory объектов (table)
- §2 Per-object 1-абзац + FPF type
- §3 Comparison summary table
- §4 5-mermaid diagrams plotnym (per object cluster)
- §5 Provenance & status table
- §6 Open questions для Ruslan

### §7.2 Output Task 5

`reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` — final.

---

## §8 Cell dispatch matrix

| Task | task_shape | Cells |
|---|---|---|
| Task 1 (inventory) | design | engineering-expert × integrator (FPF-loaded) + philosophy-expert × critic (epistemic boundaries) + mgmt-expert × integrator (organizational coherence) |
| Task 2 (per-object deep) | design | engineering-expert × integrator + systems-expert × integrator (feedback loops per object) + philosophy-expert × critic |
| Task 3 (comparison matrix) | review | philosophy-expert × critic + engineering-expert × critic + systems-expert × scalability |
| Task 4 (каша cleanup) | review | philosophy-expert × critic + engineering-expert × critic + mgmt-expert × critic |
| Task 5 (master document) | design | engineering-expert × scalability (single navigable artefact) + mgmt-expert × integrator + philosophy-expert × critic |

Brigadier integrates с dissent preservation per AP-6 → §5.5.5 provenance gate (6-check) → canonical writes.

**ВСЕ writes в `reports/phase-0-fpf-scope/` namespace.** НЕ trog'ать Foundation paths (R2).

---

## §9 Constitutional posture

- **R1:** Ты scribe + structurer. Surface'инг variants. Ruslan = sole strategist (он ack'ает inventory / выбирает priority / решает action на cleanup flags).
- **R2:** Foundation paths read-only. Никаких writes в `swarm/wiki/foundations/` / `principles/` / `shared/schemas/` / `.claude/config/`.
- **R6:** Provenance per item — каждое utверждение в outputs = file:line или url:date.
- **R11:** Default-Deny.
- **Append-only** outputs.
- **NO API keys** — built-in tools only.
- **NO unsolicited alternatives** к выбранным Ruslan-ом путям.

---

## §10 Что НЕ делать

- НЕ выбирать «вот это важный object, это нет» — Ruslan решает priority
- НЕ trog'ать Foundation paths
- НЕ удалять existing docs — append-only, flag в cleanup list
- НЕ писать «§РЕКОМЕНДАЦИИ» / «следует» — surface'инг only
- НЕ оценивать «Левенчук прав / неправ» — surface факты
- НЕ выполнять Phase C actual research — это Phase 0 (scope definition only)
- НЕ обходить paywalls для IWE paid AI guide

---

## §11 Acceptance criteria

- [ ] `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` — ≥8-12 объектов с FPF-typed table
- [ ] `reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md` — per-object 1-page description
- [ ] `reports/phase-0-fpf-scope/03-comparison-matrix.md` — exhaustive matrix
- [ ] `reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md` — все stale items флагнуты
- [ ] `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` — L1-friendly final (≤2000 слов, 10 мин read)
- [ ] 5+ mermaid в `diagrams/`
- [ ] git commits per Task + final push origin main
- [ ] Dissents preserved per AP-6 (НЕ averaged)

---

## §12 Context files (read first)

- `inbox/levenchuk-tg-2026-05-17.md` — C1-C7 trigger
- `raw/external/ailev-FPF/FPF-Spec.md` — **canonical FPF source** (72K строк, vendored 16.05)
- `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md` — what's new в upstream
- `reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md` — Phase A overview
- `reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md` — Phase B overview
- `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md` — наш текущий FPF understanding
- `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` — Jetix vs FPF (Phase A)
- `reports/jetix-vs-iwe-audit-2026-05-17.md` — Jetix vs IWE (Phase B)
- `JETIX-WORKING-FILE-v0-2026-05-17.md` — current working file (содержит кашу — task 4 cleanup)
- `CLAUDE.md` — constitutional posture + project description
- `swarm/wiki/foundations/synthesis/foundation-master-overview-technical-2026-04-29.md` — Foundation technical
- `decisions/JETIX-CORPORATION-2026-05-05.md` — Doc 1B (corporation)
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` — Doc 1A
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md`
- `decisions/STRATEGIC-INSIGHT-*.md` (6+1 Hexagon insights)
- `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md`

---

## §13 Output structure

```
reports/phase-0-fpf-scope/
  00-JETIX-FPF-MASTER-2026-05-17.md        # L1-friendly final
  01-jetix-objects-inventory.md            # 8-12 объектов FPF-typed
  02-objects-per-fpf-deep.md               # per-object descriptions
  03-comparison-matrix.md                  # × L1 analogues × levels
  04-kasha-cleanup-flags.md                # stale items
  diagrams/
    01-objects-cluster.md
    02-comparison-matrix-visual.md
    03-fpf-layers-jetix-mapping.md
    04-kasha-heatmap.md
    05-master-tldr-mermaid.md
swarm/wiki/drafts/task-phase-0-*-*.md      # cell drafts (15 cells)
```

---

**Launch (Ruslan command line):**

```bash
tmux new -s phase-0
cd ~/Desktop/jetix-os && git pull --ff-only && claude --dangerously-skip-permissions
```

Paste prompt:
```
ultrathink. Прочитай файл prompts/phase-0-fpf-scope-definition-2026-05-17.md полностью. Ты — brigadier Jetix swarm. Phase 0 = FPF lens scope definition. 5 tasks через cell dispatch (per §8 matrix). Ты сам предлагаешь inventory объектов Jetix (минимум 8-12), per-object FPF-typed описание, comparison levels matrix с L1 наработками, каша cleanup flags, master document для L1. R1 — Ruslan = sole strategist, ты surface'ишь варианты. R2 — Foundation read-only. Действуй автономно 4-6 часов, коммить per task, push в main в конце.
```

Detach: `Ctrl+B затем D`.
