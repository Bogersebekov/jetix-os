---
title: Server CC Brigadier Prompt — Canonical Cleanup (canonical/ + deferred/ + archive/ structure)
type: brigadier-prompt
created: 2026-05-06
author: cloud-cowork (Ruslan ack via CANONICAL-WALKTHROUGH-2026-05-06.md walkthrough feedback)
target_executor: server-cc on branch claude/jolly-margulis-915d34 (or successor)
authority: Ruslan full walkthrough ack (см. §1 — все 110 пунктов классифицированы)
push_policy: draft commit на server CC ветку (НЕ main), awaits Ruslan ack для merge to main + tag
F: F4
G: structural-cleanup-pre-platform-of-truth-execution
R: refuted_if_canonical_doc_moved_or_cross_refs_broken_silently
constitutional_anchor:
  - Tier 2 Rule 2 (no architectural changes without gate) — gate = Ruslan walkthrough ack via 110-item checklist; this prompt executes ack'd plan
  - Tier 2 Rule 11 (Default-Deny) — push to draft на свою ветку, await Ruslan ack для merge
  - Append-only — git mv preserves history; frontmatter добавляется, существующее не удаляется
sla_tier: L2 (cleanup deliverable; ≤ 24h)
estimated_effort: 1-2 hours brigadier autonomous
---

# Server CC Brigadier Prompt — Canonical Cleanup

> **Контекст.** Ruslan прошёл walkthrough 110 docs (CANONICAL-WALKTHROUGH-2026-05-06.md)
> и дал full ack. Этот prompt — execution plan для structural cleanup:
> создать `canonical/` (active source-of-truth), `deferred/` (не-активно-но-помним),
> `archive/` (pre-Foundation work). Append-only — git mv preserves history.
>
> **Beta-первый подход.** Просто почистить + organize. Cross-ref audit — log only,
> не fix (это будущая задача). Если возникнут conflicts — pause + signal Ruslan.

---

## §1 Categorization (Ruslan ack'd)

### §1.1 KEEP — canonical (живёт где есть, попадает в `canonical/INDEX.md`)

**Уровень 1 — Конституция (1):**
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`

**Уровень 2 — Концепция системы (4) — TRM получает status fix:**
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` ⚠️ **status fix:** добавить frontmatter `status: LOCKED v1.0` + `version: 1.0` + `locked: 2026-04-30` retroactively (companion canonical через commit message + Workshop frontmatter)
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md`
- `decisions/JETIX-CORPORATION-2026-05-05.md`

**Уровень 3a — Foundation Parts (13):**
- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`
- `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md`
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md`
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md`
- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md`
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md`
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md`
- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md`
- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md`
- `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md`
- `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md`
- `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md`
- `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md`
- `swarm/wiki/foundations/principles/architecture.md`

**Уровень 3b — Foundation Master Overviews (2):**
- `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md`
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md`

**Уровень 3c — F8 Constitutional Schemas (10):**
- `shared/schemas/message.schema.json`
- `shared/schemas/task.schema.json`
- `shared/schemas/task-return-packet.json`
- `shared/schemas/briefing.schema.json`
- `shared/schemas/executor-binding.yaml.template`
- `.claude/config/default-deny-table.yaml`
- `shared/schemas/principle-doc.json`
- `shared/schemas/project-strategy.json`
- `shared/schemas/strategic-direction-doc.json`
- `shared/schemas/decisions-db.json`

**Уровень 6 — Top-level living docs (KEEP active, 5):**
- `CLAUDE.md` (получает update — см. §3.6)
- `HOME.md`
- `README.md`
- `MIGRATION.md`
- `_meta/conventions.md`

**Уровень 7 — Operational pipelines (4):**
- `reports/retrospective_2025-05_to_2026-04.md`
- `swarm/wiki/operations/quick-log-template.md`
- `swarm/wiki/operations/` (folder — time-tracking pipeline)
- `tools/` (Voice pipeline scripts folder)

**Total canonical: ~38 entries** (некоторые folders считаются как single canonical anchor).

### §1.2 DEFER — переезд в `deferred/`

**Уровень 5a — Strategic Insights (5):**
- `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md`
- `decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md`
- `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`
- `decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md`
- `decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md` ⚠️ verify exists; per §8 obs O3 may be missing on main

**Уровень 5c #75 — active WIP companion (1):**
- `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (Layer 2 RUSLAN-LAYER WIP — §1 filled, §2-§10 pending; companion to FUNDAMENTAL)

**Strategic Layer F2 scaffolds — special handling (Уровень 5b, 40 files):**
- `decisions/strategic/lock-entries/D-01..D-29.md` (29 files)
- `decisions/strategic/strategic-insights/*.md` (4 files)
- `decisions/strategic/_templates/*` (7 files)

**Decision per Ruslan walkthrough:** ОСТАВЛЯЕМ в `decisions/strategic/` где есть (это уже отдельная папка). НЕ moves. НЕ включается в `canonical/INDEX.md` (это F2 promotion queue для Wave 1.4, не canonical). Указывается в `deferred/INDEX.md` как "linked, not moved".

### §1.3 ARCHIVE — переезд в `archive/<original-path>` (preserve folder structure)

**Уровень 4a — v1-beta era (7):**
- `SYSTEM-DESIGN-HUMAN.md`
- `design/SYSTEM-DESIGN-TECH.md`
- `design/SYSTEM-DESIGN-TECH-SUMMARY.md`
- `design/AGENT-PROTOCOLS.md`
- `design/DATA-FLOWS.md`
- `design/ARCHITECTURE-TARGET.md`
- `design/IMPLEMENTATION-PLAN-2026-04-18.md`

**Уровень 4b — Stage-3 Genesis (6):**
- `decisions/JETIX-VISION.md`
- `decisions/JETIX-PHILOSOPHY.md`
- `decisions/JETIX-PLAN.md`
- `decisions/JETIX-ARCHITECTURE-BRIEF.md`
- `decisions/STAGE-3-APPROVAL.md`
- `decisions/STAGE-4-APPROVAL.md`

**Уровень 4c — Pre-Foundation cycle (9):**
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
- `decisions/JETIX-SYSTEM-OVERVIEW.md`
- `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md`
- `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md`
- `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md`
- `decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md`
- `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md`
- `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md`
- `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md`

**Уровень 4d — ROY layer (9):**
- `design/JETIX-FPF.md`
- `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
- `design/ROY-WIKI-V3-GOALS-2026-04-23.md`
- `design/ROY-BUILD-LOGIC-2026-04-23.md`
- `decisions/ROY-INFORMATION-DIET.md`
- `decisions/ROY-ALIGNMENT-2026-04-22.md`
- `decisions/ROY-AGENTS-BUILT-2026-04-23.md`
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
- `decisions/WIKI-V3-MECHANICS-2026-04-23.md`

**Уровень 4e — Stage-3 chunks (4):**
- `decisions/2026-04-19-architecture-v2-approval.md`
- `decisions/2026-04-20-jetix-architecture-final-DRAFT.md`
- `decisions/gap-analysis-review-decisions-2026-04-20.md`
- `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` + `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` (2 files)

**Уровень 5c (76-79) ARCHIVE remainder (5):**
- `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md`
- `decisions/AUDIT-CURRENT-STATE-2026-04-27.md`
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md`
- `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md`
- `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`

**Уровень 6 ARCHIVE (2):**
- `ARCHITECTURE-CURRENT.md`
- `LAUNCHERS-STAGE-6.md`

**Уровень 8 — Stale AWAITING-APPROVAL packets (15):**
- `decisions/AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md`
- `decisions/AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md`
- `decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md`
- `decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md`
- `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md`
- `decisions/AWAITING-APPROVAL-strategic-layer-foundation-bundle-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-30.md`
- `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-30.md` ⚠️ **EXCEPTION:** verify state — если pending Wave 1.4 → KEEP active в decisions/, иначе ARCHIVE
- `decisions/AWAITING-APPROVAL-foundation-overview-human-workshop-2026-05-06.md`
- `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md`
- `design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md`
- `design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md`

**Уровень 9 — RUSLAN-ACK historical (8):**
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-D-2026-04-28.md`
- `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BASELINE-2026-04-28.md`
- `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-B-SUPPLEMENT-2026-04-27.md`

**Total ARCHIVE: ~70 docs**

### §1.4 KEEP as-is (no move, no folder change)

- `_HANDOFF_to_next_cowork_session_2026-05-06.md` (today's working doc)
- `reports/*.md` (33 files — historical research deliverables, оставляем где есть)
- `prompts/*.md` (149 files — brigadier prompts + handoff chats)
- All other repo content not in §1.1-§1.3 lists (raw/, daily/, agents/, comms/, shared/state/, .claude/, etc.)

---

## §2 Process — Phases A-H

### Phase A — Preparation (10 min)

A.1 Read context:
   - `CANONICAL-WALKTHROUGH-2026-05-06.md` (Ruslan ack'd checklist — primary source)
   - `reports/canonical-docs-inventory-2026-05-06.md` (companion inventory)
   - `reports/github-repo-history-2026-05-06.md` (historical context)

A.2 Verify all paths in §1 exist (для §1.1, §1.2, §1.3):
   ```bash
   for path in <list>; do
     [ -e "$path" ] && echo "OK $path" || echo "MISSING $path"
   done
   ```
   Если MISSING — record в `archive/missing-files-2026-05-06.md`, не fail.

### Phase B — Create folder structure (5 min)

```bash
mkdir -p canonical/
mkdir -p deferred/
mkdir -p archive/
# Sub-structure для archive — preserve original paths:
mkdir -p archive/decisions/
mkdir -p archive/design/
# top-level archives goes to archive/ root:
# (SYSTEM-DESIGN-HUMAN.md, ARCHITECTURE-CURRENT.md, LAUNCHERS-STAGE-6.md)
```

### Phase C — DEFER moves (15 min)

For each path в §1.2 (5 strategic insights + 1 vision-of-system):

```bash
git mv decisions/STRATEGIC-INSIGHT-X-2026-04-XX.md deferred/STRATEGIC-INSIGHT-X-2026-04-XX.md
```

После move — frontmatter add (Edit tool):
```yaml
status: deferred-phase-2-plus
deferred_at: 2026-05-06
deferred_reason: pre-Phase-1 strategic exploration / not active focus / preserved for future activation
```

(Если у doc'а уже есть `status: deferred-phase-2-plus` — оставить, добавить только `deferred_at:` если отсутствует.)

### Phase D — ARCHIVE moves (30-45 min)

For each path в §1.3 (~70 docs):

```bash
# Determine target — preserve original folder structure under archive/:
# decisions/X.md → archive/decisions/X.md
# design/X.md → archive/design/X.md
# top-level X.md → archive/X.md
git mv <original-path> archive/<original-path>
```

После move — frontmatter add (Edit tool):
```yaml
status: archived
archived_at: 2026-05-06
archived_reason: <one of the categories below>
```

**`archived_reason:` taxonomy** (use the relevant one):
- `pre-Foundation v1.0 work — superseded by Foundation Architecture LOCKED 2026-04-28`
- `v1-beta design (April 2026) — superseded by Foundation v1.0 + Документ 1A/1B`
- `Stage-3 Genesis draft — superseded by JETIX-VISION-FUNDAMENTAL-2026-04-27 + Foundation v1.0`
- `Pre-Foundation cycle artifact — wrapped в Foundation Parts`
- `ROY layer pre-Foundation construction — wrapped в Foundation Part 4 + Pillar C`
- `Stage-3 chunk tracker — historical decision journal`
- `Stale AWAITING-APPROVAL packet — ack'd via RUSLAN-ACK record / Wave-E LOCK / git tag (frontmatter not updated post-ack)`
- `Historical RUSLAN-ACK record — preserved as audit trail`
- `Pre-Foundation snapshot — superseded`

**EXCEPTION для `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-30.md`:**
   - Read frontmatter — если `state: open` или `status: AWAITING-APPROVAL` без corresponding RUSLAN-ACK → **KEEP в decisions/** (active Wave 1.4 pending)
   - Если acked → ARCHIVE как остальные

### Phase E — TRM model status fix (5 min)

Edit `decisions/JETIX-TRM-MODEL-2026-04-30.md` frontmatter — добавить:

```yaml
status: LOCKED v1.0
version: 1.0
locked: 2026-04-30
locked_reason: retroactive frontmatter alignment with commit message [concept] LOCKED + companion canonical relationship to JETIX-WORKSHOP-CONCEPT-2026-04-30 LOCKED
```

(Tag retroactively НЕ создаём — Workshop concept LOCKED tag отсутствует тоже, а status frontmatter уже LOCKED.)

### Phase F — Index files (20 min)

#### F.1 — `canonical/INDEX.md`

Single-page navigation для all KEEP docs из §1.1. Structure:

```markdown
---
title: Canonical Docs INDEX — single source of truth navigation
date: 2026-05-06
type: index
status: active
git_tag: canonical-organized-2026-05-06
---

# Canonical Docs — Source of Truth (2026-05-06)

> Это **single page** со ссылками на все active canonical документы Jetix OS.
> Каждый doc ниже — LOCKED canonical (production source-of-truth) или active living
> infrastructure. Пройти структурированный walkthrough всего что было — см.
> `CANONICAL-WALKTHROUGH-2026-05-06.md` (root) или `reports/canonical-docs-inventory-2026-05-06.md`.
> Что-то в архиве — см. `archive/INDEX.md`. Deferred — `deferred/INDEX.md`.

## 1. Конституция (Tier 1)

- [JETIX-VISION-FUNDAMENTAL](../decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md) — 2624 строк — constitutional anchor (35 use cases × 12 categories, 11 hard rules)

## 2. Концепция системы

- [JETIX-WORKSHOP-CONCEPT](../decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md) — Workshop metaphor (мастерская)
- [JETIX-TRM-MODEL](../decisions/JETIX-TRM-MODEL-2026-04-30.md) — Total Resource Management
- [BASE-MANAGEMENT-SYSTEM (Документ 1A)](../decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md) — universal базовая система
- [JETIX-CORPORATION (Документ 1B)](../decisions/JETIX-CORPORATION-2026-05-05.md) — applied use case 1A

## 3. Foundation Architecture v1.0 (LOCKED 2026-04-28)

### 3a. 11 Parts + Pillar C
[... табличка с 13 architectures ...]

### 3b. Master Overviews
- [Technical](...) (engineering audience)
- [Workshop Human](...) (founder/partner/investor)

### 3c. F8 Constitutional Schemas
[... табличка с 10 schemas ...]

## 4. Top-level Living Configuration
[... CLAUDE.md / HOME.md / README.md / MIGRATION.md / _meta/conventions.md ...]

## 5. Operational Pipelines
[... retrospective / quick-log / time-tracking / voice pipeline ...]

---

**Что НЕ canonical:**
- Archive: `archive/INDEX.md` (~70 docs — pre-Foundation work, superseded)
- Deferred: `deferred/INDEX.md` (5 strategic insights + 1 active WIP)
- Strategic Layer F2 scaffolds: `decisions/strategic/` (29 D-Lock entries + insights + templates — F2 promotion queue для Wave 1.4)
- Reports: `reports/` (33 historical research deliverables)
- Prompts: `prompts/` (149 brigadier prompts + handoff chats)
```

Каждая ссылка должна работать в Antigravity (relative path с `../` префиксом потому что INDEX.md лежит в `canonical/`).

#### F.2 — `deferred/INDEX.md`

Похожая structure для DEFER docs из §1.2 + Strategic Layer F2 mention:

```markdown
# Deferred Docs INDEX (2026-05-06)

> Документы которые помним но не используем активно. Не trash, не canonical.
> Возможна re-activation в Phase 2+.

## Strategic Insights (deferred Phase-2+)
- [M&A Direction](MA-DIRECTION-2026-04-25.md) — ...
- [Arbitrage Traffic](ARBITRAGE-TRAFFIC-2026-04-25.md) — ...
- [BIOS Moment](JETIX-AI-BIOS-MOMENT-2026-04-24.md) — ...
- [AI-Psy-Led](AI-PSY-LED-DESIGN-2026-04-26.md) — ...
- [Top Lists + Partner Factory](TOP-LISTS-PARTNER-FACTORY-2026-04-26.md) — ...

## Active WIP (companion to FUNDAMENTAL)
- [JETIX-VISION-OF-SYSTEM (Layer 2 RUSLAN-LAYER)](JETIX-VISION-OF-SYSTEM-2026-04-27.md) — §1 filled, §2-§10 pending

## Linked (not moved)
- Strategic Layer F2 scaffolds — оставлены в `decisions/strategic/lock-entries/D-01..D-29.md`
  (это active F2 promotion queue для Wave 1.4 Strategic Layer; не moved чтобы не ломать pipeline)
```

#### F.3 — `archive/INDEX.md`

Большая table со всеми ~70 archived docs. Format:

```markdown
# Archive INDEX (2026-05-06)

> Все pre-Foundation work + superseded docs + stale packets + historical records.
> Append-only — ничего не удалено, всё в archive/<original-path>. История preserved
> через git mv. Frontmatter каждого: `status: archived` + `archived_at: 2026-05-06` + `archived_reason:`.

## v1-beta era (Apr 13-18, 2026)
| Original | Archive path | Reason |
|---|---|---|
| SYSTEM-DESIGN-HUMAN.md | archive/SYSTEM-DESIGN-HUMAN.md | v1-beta human design — superseded by 1A/1B |
| design/SYSTEM-DESIGN-TECH.md | archive/design/SYSTEM-DESIGN-TECH.md | ... |
[... все 7 ...]

## Stage-3 Genesis (Apr 21)
[... 6 docs ...]

## Pre-Foundation cycle (Apr 22-24)
[... 9 docs ...]

## ROY layer (Apr 22-23)
[... 9 docs ...]

## Stage-3 chunks (Apr 19-20)
[... 4 docs ...]

## Other ambiguous → archived (Apr 24-27)
[... 5 docs from Уровень 5c ...]

## Top-level pre-Foundation snapshots
- archive/ARCHITECTURE-CURRENT.md
- archive/LAUNCHERS-STAGE-6.md

## Stale AWAITING-APPROVAL packets (frontmatter not updated post-ack)
[... 15 packets — со ссылкой на corresponding RUSLAN-ACK record ...]

## Historical RUSLAN-ACK records (8)
[... 8 records ...]

---

**Что НЕ архивировано:**
- Active canonical — `canonical/INDEX.md`
- Deferred — `deferred/INDEX.md`
- Strategic Layer F2 scaffolds — `decisions/strategic/`
- Reports / Prompts — оставлены где есть
```

### Phase G — CLAUDE.md update + cross-ref audit (15 min)

#### G.1 — CLAUDE.md add `## Source of Truth` section

Найти подходящее место в CLAUDE.md (после `## Architecture` или в начале) и добавить:

```markdown
## 📖 Source of Truth (Canonical Docs)

Все active canonical документы — [canonical/INDEX.md](canonical/INDEX.md).

Walkthrough всех 110 docs со статусом → [CANONICAL-WALKTHROUGH-2026-05-06.md](CANONICAL-WALKTHROUGH-2026-05-06.md).

Other indices:
- Deferred — [deferred/INDEX.md](deferred/INDEX.md) (не активно но помним)
- Archive — [archive/INDEX.md](archive/INDEX.md) (~70 pre-Foundation docs, append-only history)
- Strategic Layer F2 promotion queue — `decisions/strategic/`
```

#### G.2 — Cross-ref audit

Grep canonical docs (Уровень 1-3 + 6) для cross-refs на now-archived/deferred paths:

```bash
# canonical paths
grep -rl "decisions/JETIX-VISION\.md\|decisions/JETIX-PHILOSOPHY\.md\|decisions/JETIX-PLAN\.md\|decisions/JETIX-ARCHITECTURE-BRIEF\.md\|decisions/MASTER-PLAN-FOUNDATION\|decisions/JETIX-SYSTEM-OVERVIEW\.md\|decisions/LAYER-5-\|decisions/LAYER-6-\|decisions/LAYER-7-\|decisions/JETIX-FOUNDATION-BUILD\|design/SYSTEM-DESIGN-TECH\.md\|design/JETIX-FPF\.md" decisions/ swarm/wiki/foundations/ swarm/wiki/synthesis/ shared/schemas/ CLAUDE.md _meta/
```

Каждое hit — record в `archive/cross-ref-changes-log-2026-05-06.md`:

```markdown
# Cross-ref changes log (post-canonical-cleanup 2026-05-06)

After moves to archive/, the following cross-refs in active canonical docs may need update:

| File | Line | Old ref | New ref (suggested) |
|---|---|---|---|
| ... | ... | decisions/JETIX-VISION.md | archive/decisions/JETIX-VISION.md |

**Status:** documented only. NOT auto-fixed (refactor deferred to follow-up cycle).
```

**Discipline:** НЕ автоматически updates cross-refs внутри canonical docs (это refactor с potential breakage). Только log.

### Phase H — Wiki maintenance + commit + push (10 min)

#### H.1 — wiki/index.md and swarm/wiki/log.md updates

Append entries сверху per Global Rule 2:

`swarm/wiki/log.md`:
```markdown
## 2026-05-06 — canonical cleanup (canonical/ + deferred/ + archive/ structure)

Established canonical/, deferred/, archive/ folder structure per Ruslan walkthrough ack
(CANONICAL-WALKTHROUGH-2026-05-06.md, 110 items classified). 70+ docs moved to archive/
(append-only, history preserved via git mv). 6 docs to deferred/. TRM model status fixed
retroactively. CLAUDE.md updated с pointer на canonical/INDEX.md.

Tag: canonical-organized-2026-05-06.
```

(skip wiki/index.md update если файла нет; иначе add canonical/, deferred/, archive/ entries.)

#### H.2 — Commit + push

Single commit:

```bash
git add -A
git commit -m "[canonical-cleanup] organize canonical/ + deferred/ + archive/ structure (Ruslan walkthrough ack 110 items)

Per CANONICAL-WALKTHROUGH-2026-05-06.md walkthrough feedback:
- KEEP canonical (~38 entries): Constitution + System Concept + Foundation Parts + Schemas + Top-level living + Operational
- DEFER (6 docs → deferred/): 5 Strategic Insights + 1 active WIP (Vision-of-System)
- ARCHIVE (~70 docs → archive/<original-path>): v1-beta era + Stage-3 Genesis + Pre-Foundation cycle + ROY layer + Stage-3 chunks + ambiguous remainder + stale packets + historical acks
- TRM model status fix (retroactive frontmatter alignment with commit + companion-canonical)
- canonical/INDEX.md / deferred/INDEX.md / archive/INDEX.md created
- CLAUDE.md updated with ## Source of Truth section
- archive/cross-ref-changes-log-2026-05-06.md (audit only, no auto-fix)
- swarm/wiki/log.md entry appended

Append-only: git mv preserves history; frontmatter updates only add fields, don't delete.

Authority: Ruslan walkthrough ack via 110-item checklist (CANONICAL-WALKTHROUGH-2026-05-06.md).
Constitutional check: Tier 2 Rule 2 gate satisfied via walkthrough ack; Default-Deny → push to draft branch (not main) awaiting Ruslan merge ack."
```

```bash
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** Ждёт Ruslan merge ack.

---

## §3 Constitutional check

| Rule | Application | Compliance |
|---|---|---|
| Tier 2 Rule 2 (no architectural changes без gate) | Gate = Ruslan walkthrough ack 110 items. This prompt = execution. | ✅ |
| Tier 2 Rule 6 (no aggregation без provenance) | Каждое move + frontmatter update — explicit reason из taxonomy + walkthrough ID. | ✅ |
| Tier 2 Rule 11 (Default-Deny + blast radius) | F4 structural reorganization. Default-Deny → push на draft branch, await Ruslan merge ack для main + tag. | ✅ |
| Append-only | git mv preserves history. Frontmatter add fields, не delete. canonical/INDEX.md, deferred/INDEX.md, archive/INDEX.md = new files (no overwrites). | ✅ |

---

## §4 What NOT to do

- ❌ НЕ удалять docs (всё через git mv)
- ❌ НЕ редактировать body archived docs (только frontmatter add fields)
- ❌ НЕ auto-fix cross-refs внутри canonical docs (только log)
- ❌ НЕ создавать canonical/INDEX.md без content (должен иметь все ~38 entries)
- ❌ НЕ push to main (draft на свою ветку, await ack)
- ❌ НЕ git tag (canonical-organized-2026-05-06 — после Ruslan ack mergе)
- ❌ НЕ trash strategic/ (40 F2 scaffolds — keep where они есть, mention в deferred/INDEX.md)
- ❌ НЕ archive Wave 1.4 scaffolding packet если pending (verify state — exception в §2 Phase D)

---

## §5 Time / size budget

- Phase A preparation: 10 min
- Phase B folder structure: 5 min
- Phase C DEFER moves: 15 min (6 docs)
- Phase D ARCHIVE moves: 30-45 min (~70 docs + frontmatter add)
- Phase E TRM status fix: 5 min
- Phase F INDEX files: 20 min (3 INDEX files)
- Phase G CLAUDE.md update + cross-ref audit: 15 min
- Phase H wiki + commit + push: 10 min

**Total estimated: 1.5-2 hours brigadier autonomous.**

Если значительно превышает 2 часа — pause + signal Ruslan.

---

## §6 Final deliverables — Phase D push checklist

After Phase H push, server CC ветка должна иметь:

```
# New folder structure
A  canonical/INDEX.md
A  deferred/INDEX.md
A  archive/INDEX.md
A  archive/cross-ref-changes-log-2026-05-06.md

# Moved files (R = rename via git mv):
R  decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md → deferred/...
R  decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md → deferred/...
R  ... (6 DEFER moves)
R  SYSTEM-DESIGN-HUMAN.md → archive/SYSTEM-DESIGN-HUMAN.md
R  design/SYSTEM-DESIGN-TECH.md → archive/design/SYSTEM-DESIGN-TECH.md
R  ... (~70 ARCHIVE moves)

# Modified (frontmatter updates):
M  decisions/JETIX-TRM-MODEL-2026-04-30.md (status fix)
M  CLAUDE.md (## Source of Truth section)
M  swarm/wiki/log.md (entry appended)
M  (each archived doc — frontmatter add status: archived + reason)
M  (each deferred doc — frontmatter add status: deferred + reason)
```

After push — signal Ruslan через cloud cowork bridge:
- Branch + commit SHA
- File count moved (DEFER / ARCHIVE)
- Any MISSING files flagged
- Any conflicts encountered
- Discipline check (constitutional posture, append-only verified, no canonical doc moved silently)
- Ready для Ruslan merge ack → push to main + tag `canonical-organized-2026-05-06`

---

**Brigadier signature.** Acting_as canonical-cleanup-orchestration-role.
Ruslan = sole authority по structural reorganization (ack via walkthrough).
Constitutional anchor: Tier 2 Rule 2 gate + Default-Deny + Append-only.
