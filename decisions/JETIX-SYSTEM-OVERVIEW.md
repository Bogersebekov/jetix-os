---
id: jetix-system-overview-2026-04-24
title: "JETIX-SYSTEM-OVERVIEW — Coherent 14-Layer Description of Jetix as Operating System"
date: 2026-04-24
type: foundation-document
state: accepted
acked_by: ruslan
acked_at: 2026-04-24T23:30:00Z
acked_via: cloud-cowork-session
ack_chosen: a1+b1+c1+d1
ack_notes: "A1 USB-C/McKinsey resolution accepted per §6; B1 Smart AI internal-only (not D29 lock); C1 $1M+ ICP tier as D22 refinement (not conflict with 11 archetypes); D1 accept integration per-layer word counts as-is (primary drafts carry the depth)."
author: brigadier (swarm orchestrator) + 5 domain experts as cells
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
target_word_count: 15000-25000
operating_mode: Stage-Gated
promoted_at: 2026-04-24T23:45:00Z
promoted_by: brigadier
gate_file: swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md
binding: yes (Ruslan-acked foundation for Phase 2 per-layer deep-dives + Phase 3 strategic docs)
supersedes: none (new document; companion to D1-D28 + JETIX-VISION + JETIX-PHILOSOPHY + JETIX-PLAN + JETIX-ARCHITECTURE-BRIEF)
primary_frameworks: [PMBOK, Grove HOM, Cagan, Drucker, Karpathy LLM-Wiki, Levenchuk ШСМ, Meadows leverage, Ashby requisite variety]
sources_digest:
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md (D25/D26/D27/D28 + USB-C reinforcement + Smart AI internal note)
  - decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md (week 2026-04-24 → 2026-05-01)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (local-first client-private positioning)
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md (6-pillar roadmap)
  - decisions/JETIX-VISION.md + JETIX-PHILOSOPHY.md + JETIX-PLAN.md + JETIX-ARCHITECTURE-BRIEF.md (D1-D4 constitutional)
  - design/JETIX-FPF.md (FPF constitutional)
  - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md (6 variants + sequenced-trajectory recommendation)
  - swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md (L1/L2 partial substrate)
  - reports/review_2026-04-24.md + reports/summary_2026-04-24.md (voice-memo evidence 506-529)
  - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md (USB-C pitch verbatim)
  - .claude/agents/*.md (6 ROY + 14 legacy)
  - swarm/lib/shared-protocols.md (runtime contract §§1-9)
  - CLAUDE.md (project conventions)
  - 14 layer drafts in swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-* (primary cell-authored content — authoritative detail)
tags: [foundation, system-overview, 14-layers, agents-first-class, usb-c, smart-ai, company-as-code]
---

# JETIX-SYSTEM-OVERVIEW — Coherent 14-Layer Description

> **Кто читает этот документ.** Ruslan (self-reference + onboarding), Cloud Cowork (operational routing), brigadier swarm (master context для Phase 2 deep-dives), будущие hire-ы Phase 2+, потенциальные клиенты Phase 2+ (фрагменты, фильтрованные).
>
> **Зачем он существует.** До 2026-04-24 Jetix имел 28 locked decisions + 4 foundation docs (Vision / Philosophy / Plan / Architecture-Brief) + FPF constitutional, но **coherent layered system description с агентами как first-class citizens отсутствовал**. Без этого стратегические документы на направления (ai-consulting-DACH, producer-services, Secure Network) и ICP Trinity строить было преждевременно — не понятно в какой слой они ложатся.
>
> **Binding scope.** Не Lock. Не заменяет D1-D28 (они остаются non-negotiable). Добавляет **архитектурную грамматику**, через которую все остальные документы читаются. Phase 2 per-layer deep-dives (отдельные M-tasks каждая) работают под этим документом.

---

## §0 TL;DR (300 слов)

Jetix — это 14-слойная operating system, построенная на четырёх ключевых метафорах + 28 locked decisions. Метафоры: (1) **USB-C** — Jetix как стандарт-де-факто для AI-augmented бизнеса, как прошивка Windows на любом компьютере [src:raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md]; (2) **Smart AI** (internal label, not lock) — термин для внутренних обсуждений; официальное имя остаётся Jetix [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]; (3) **Company-as-Code** — вся Jetix живёт в git, состояние реконструируемо на любой момент [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]; (4) **Holding-with-agents** — target team 50-100 людей + агенты как интерактивный слой [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26].

**14 слоёв:**

- **Core stack L0-L9:** L0 Foundation (Company-as-Code) → L1 Knowledge (query-driven KB + Private Library) → L2 Ingest & Signal → L3 Synthesis & Compounding Engineering → L4 Agent Layer (6 ROY + 14 legacy, holding-style) → L5 Product & Services (Smart AI directions: consulting / продюсерский центр / USB-C services / matchmaker / Secure Network / YouTube-analyzer / educational / tokens) → L6 Business & Trajectory (ICP + outreach + 5 gates €50K → $1T) → L7 Research & Reverse-Engineering (D24 open-source + Левенчук ШСМ + reverse-engineering на максималках) → L8 People & Alliance (core team 50-100 + Mittelstand AI Alliance + Secure Network + matchmaker + fork-community) → L9 Governance & Evolution (28 Locks + AWAITING-APPROVAL gates + sandbox-черновик + fork-and-merge).
- **Cross-cutting L-R / L-C / L-B / L-P:** L-R Resource Management (time / attention / finances / energy / credits) → L-C Compute & Infrastructure (workstation Phase-1 → own data-center Phase-3+ + электростанции Phase-3+) → L-B Brand & Narrative (tagline / USB-C-метафора / 3-audience landings / document-compass) → L-P Life OS (Ruslan personal system as substrate for business layers).

**Trajectory:** €0 → €50K Q2 2026 (committed) → €200K validation → €1M → $100M → $100B → $1T world-record attempt [src:decisions/JETIX-VISION.md#14].

**Текущее состояние 2026-04-24:** 3 swarm cycles завершены + 4-й (этот) Stage-Gated; 28 locks acked; 0 paying clients; L0-L1-L2-L3-L4 substrate built (KM Mat Wave-1 promoted); L5-L9 spec'd but not executed; L-R/L-C/L-B/L-P identified as cross-cutting but not yet dashboarded.

---

## §1 Why this document exists

Ruslan 2026-04-24 озвучил директиву: *«foundation системы вместе с агентами ещё не описан — нужно сперва закончить foundation, потом каждый слой обработать, потом уже наслаивать исследования/продажи/ICP/задачи в правильные слои»* [src:decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md#§0].

До этого документа существовали пять foundation-артефактов:

- `JETIX-VISION.md` (D1) — identity: кто такие Jetix
- `JETIX-PHILOSOPHY.md` (D2) — принципы
- `JETIX-PLAN.md` (D3) — step-by-step plan
- `JETIX-ARCHITECTURE-BRIEF.md` (D4) — техническая архитектура
- `JETIX-FPF.md` (constitutional) — frame-problem-framework

Плюс 28 locked decisions (D1-D28) и многочисленные подоснованные документы (STRATEGIC-INSIGHT, VISION-NEXT, ROY-ALIGNMENT, KM-ARCHITECTURE-VARIANTS).

**Что отсутствовало:** coherent layered description, где ОДНОВРЕМЕННО:

1. Агенты (6 ROY + 14 legacy) видны как first-class citizens в каждом слое, где они работают.
2. Слои cross-referenced между собой (что где живёт, кто с кем разговаривает).
3. Все 28 Locks mapping'ованы на слои — где каждый Lock primarily constrains.
4. Trajectory €0 → $1T видна как последовательность upgrade-событий per layer.
5. 4 новых Lock-кандидата 2026-04-24 (D25 Company-as-Code, D26 Team 50-100, D27 Fork-and-merge, D28 Query-driven KB) и USB-C reinforcement — интегрированы в foundation.
6. Strategic positioning (USB-C / McKinsey-platform / Smart AI / AI-BIOS-moment) — разрешено в coherent narrative.

Этот документ закрывает шесть выше перечисленных gaps. Он является **фундаментом для Phase 2 per-layer deep-dives** (каждый слой → отдельный M-task swarm cycle) и **Phase 3 strategic docs per direction** (ai-consulting-DACH / producer / Secure Network). Без этого документа strategic docs строились бы на шатком ландшафте — неясно в какой слой ложится каждый кусок стратегии.

---

## §2 Reading order for different audiences

**Ruslan self-read (~30 min):** §0 TL;DR → §4 system-level diagram → §3 28-Locks table (scan for new D25-D28) → §5 trajectory overview → §6 USB-C/McKinsey resolution (ack/reject здесь) → §L+1 open strategic questions. Per-layer deep-read только по необходимости.

**Cloud Cowork operational routing (~15 min):** §0 → §2 → §4 → §L+3 recommended next 3 M-tasks → §L+4 how-Ruslan-uses-doc. Per-layer reads trigger on specific task.

**Brigadier swarm master-context (~1-2h, full read):** Весь документ как primary reference; каждый Phase-2 layer deep-dive M-task читает соответствующий §L?. §L+2 gaps surface what-needs-new-M-task.

**Future hires Phase 2+ onboarding (~2-4h):** §0 → §1 → §3 → §L0-L9 по слоям в порядке → §L+1. Cross-cutting L-R/L-C/L-B/L-P на второй день.

**Potential clients Phase 2+ (filtered fragments):** §0 TL;DR только + (при matching ICP) L5 product-portfolio + L6 trajectory. §L1/L2/L3/L4 (internal implementation) — NOT shown. L-B brand layer ведёт копирование.

---

## §3 28 Locked Decisions summary table + primary-layer mapping

| D# | Lock | One-line | Primary Layer |
|----|------|----------|---------------|
| D1 | Gentleman inside / Predator outside | Context-adaptive identity grammar | L-B / L4 |
| D2 | Solo-now / Team-ready-scaffolding | Operating model Phase 1 | L8 / L4 |
| D3 | Open inside team / Closed outside | IP + community access | L9 / L8 |
| D4 | Founder persona triple (дед + 20-летний + отшельник-спортсмен) | Founder voice anchor | L-P / L-B |
| D5 | Secure Network Phase 2+ quality-gated platform | Community architecture | L8 |
| D6 | ICP depth + skin-in-game hard rule | Customer qualification | L6 |
| D7 | 11 archetypes as audience | Market segmentation | L6 |
| D8 | Layered identity — different faces per observer/phase | Identity grammar | L-B / L4 |
| D9 | Opportunity inside / Pain outside | Sales messaging | L-B / L6 |
| D10 | English-speaking infobiz Phase 1 target | Geography + market | L6 |
| D11 | Investment-fund mentality Day 1 | Operating philosophy | L-R / L9 |
| D12 | Hooks outside / Deep inside | Content layering | L-B |
| D13 | Open surface / Closed core | Methodology exposure | L9 / L7 |
| D14 | Research = revenue-instrumental Phase 1 | Research discipline | L7 |
| D15 | Revenue-gated unlocks (€50K / €200K / $1M) | Financial pacing | L6 / L-R |
| D16 | Phase 1 simple community-chat | Community start-point | L8 |
| D17 | Filesystem = SoT / Notion = collaboration | Authority grammar | L0 / L1 |
| D18 | Productization over hours | Scaling model | L5 / L6 |
| D19 | $1T trajectory + holding structure | Long-horizon trajectory | L6 / L8 |
| D20 | USB-C universal connector positioning | Standards-level positioning | L-B / L5 / L7 |
| D21 | Matchmaker + Roy-replication | Network multiplication | L8 / L5 |
| D22 | ICP qualitative filter (5 criteria) | Membership quality | L6 / L8 |
| D23 | Token economy Phase 3+ | Liquidity path | L5 / L-R |
| D24 | Open-source research direction Phase 3+ | Research direction | L7 |
| **D25** | **Company-as-Code** (2026-04-24) | **Everything in git + declarative config + atomic commits** | **L0 / L9** |
| **D26** | **Team 50-100 Enterprise** (2026-04-24) | **Jetix target 50-100 humans, NOT one-person company** | **L8 / L4** |
| **D27** | **Fork-and-Merge evolution** (2026-04-24) | **Canonical upstream + downstream forks + merge-back** | **L9 / L0** |
| **D28** | **Query-driven KB filtering** (2026-04-24) | **/ingest --anchor=<...> mandatory; pool-filling driven by anticipated queries** | **L1 / L2** |

**USB-C reinforcement** (2026-04-24, не новый lock — усиление D20): *«настолько будет технология просто Jetix распространена и мощная что её будут использовать все как раньше использовали прошивку Windows»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#USB-C].

**Smart AI — internal note, NOT lock:** *«ну типа запиши между прочим но нет это ещё не лок блять забей хуй»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]. Используется внутренне; официальное positioning остаётся Jetix.

---

## §4 System-level diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   Cross-cutting layers (pervade all core stack):                             │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ L-B Brand & Narrative    ← tagline / USB-C / Smart AI / 3 landings   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ L-R Resource Mgmt        ← time / attention / $ / energy / credits    │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ L-C Compute Infra        ← workstation→data-center→электростанции    │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ L-P Life OS              ← Ruslan personal system (substrate)         │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ═══════════════════════════════════════════════════════════════════════    │
│                                                                              │
│   Core stack (L0 at bottom, L9 governs all):                                 │
│                                                                              │
│   L9  ◇ Governance & Evolution (28 Locks + AWAITING-APPROVAL gates)         │
│   ─────── governs ↓ all layers ↓ ─────────                                  │
│                                                                              │
│   L8  People & Alliance      ← humans 50-100 + Alliance + Secure Network    │
│      ↕                                                                       │
│   L7  Research & Reverse-Eng ← D24 + Левенчук + standards-contribution      │
│      ↕                                                                       │
│   L6  Business & Trajectory  ← ICP + outreach + 5 gates €50K → $1T          │
│      ↕                                                                       │
│   L5  Product & Services     ← 9 directions (Smart AI flagship label)       │
│      ↕                                                                       │
│   L4  Agent Layer            ← 6 ROY + 14 legacy + 5×4 matrix + 5-layer mem │
│      ↕                                                                       │
│   L3  Synthesis & Compound   ← Plan/Work/Review/Compound 40/10/40/10         │
│      ↕                                                                       │
│   L2  Ingest & Signal        ← voice-pipeline + /ingest --anchor + crawlers │
│      ↕                                                                       │
│   L1  Knowledge              ← wiki + Private Library + topic-wikis         │
│      ↕                                                                       │
│   L0  Foundation             ← git-repo as system-state (Company-as-Code)   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

Data flow: external signal → L2 ingest → L1 storage → L3 synthesis →
           L4 agents produce → L5 products (L6 sells) → L-R $ back to system
Control flow: L9 gates → brigadier-dispatch → L4 cells → L1 drafts → L9 promotes
```

---

## §5 Trajectory overview — €0 → $1T upgrade events per layer

| Gate | Trigger | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L-R | L-C | L-B | L-P |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K Q2 2026** | Cumulative revenue €50K; 2 contracts + 233 hourly h | single-dev commits | A1 Karpathy++ | voice+manual /ingest | 3 cycles compound | 6 ROY + 14 legacy | consulting + продюс | ICP + manual outreach | D14 revenue-instr only | solo + 5-20 chat | Ruslan-HITL all gates | manual budget | 1 workstation | 1 landing + compass | manual log |
| **G2 €200K** | Validation €200K | + CI + multi-dev | + A2 mini-swarm | + crawlers V1 | + skills codified | + 2-3 hires onboarded | + matchmaker manual→platform | + DACH primary | + patents process | + Secure Network design | + gate-delegation first | + per-agent dashboard | + 1 dedicated server + GPU | + 3 landings | + auto-logging prototype |
| **G3 €1M** | Revenue run-rate €1M | + federation: forks | + A3 GraphRAG | + full crawler suite | + cross-project compound | + team 5-10 | + Secure Network launch + USB-C services + methodology repo | + €1M/mo pipeline | + first Alliance contrib | + team 5-10 hires | + fork-and-merge governance | + per-roy P&L | + data-center start | + USB-C public | + systematic wellness |
| **G4 $100M** | Revenue or market cap $100M | + legal audit-trail | + federated wikis | + industry-standard signal-net | + meta-compound | + Phase-B brigadier-split | + YouTube-SaaS + educational scale + tokens internal | + roy-replication external | + D24 open-source research active | + 20-50 people + Alliance formalized | + Alliance methodology-parliament | + Kelly portfolio multi-roy | + multi-region + redundant | + civilizational narrative | + life-OS-for-millionaires as Phase-3 product |
| **G5 $100B → $1T** | Market cap $100B → $1T record | + constitutional-amendment process | + Mittelstand AI Alliance federation | + sovereign data network | + federated compound | + 50-100 humans + sub-brigadiers | + tokens Phase-3+ public | + civilizational revenue | + published research | + 1000-5000 Alliance members | + civilization co-govern | + civilizational resource-accounting | + Jetix own data-center + power | + global USB-C narrative | + externalized life-OS product-line |

**Ключевой принцип:** per sequenced-migration-trajectory принятому 2026-04-24 (brigadier strategies KM-architecture-research cycle) — **никакой single variant не выживает все 5 gates**. Каждый upgrade — планированная migration с measurable trigger, не forced pivot под stress.

---

## §6 USB-C / McKinsey-platform resolution (brigadier proposal — Ruslan acks/rejects)

**Вопрос:** USB-C positioning (D20 + reinforcement) и McKinsey-platform framing из audio_464 — одна и та же позиция или разные? Открытый вопрос с D-0.2 master-plan §4.

**Brigadier proposes coherent resolution based on D20 + D27 + D25:**

**Они разные уровни одного и того же стека.**

- **USB-C (D20 + reinforcement) = infrastructure layer** — стандарт-де-факто, на котором работает любой AI-augmented бизнес. Как прошивка Windows: не замена самим бизнесам, а substrate, на котором они работают. Jetix = open-standard connector между AI-агентами + бизнесами + людьми.
- **McKinsey-platform (audio_464) = specific case** — McKinsey (и любой другой consulting incumbent) может продолжать существовать; они работают как один из "компьютеров на прошивке Windows". Jetix не замещает McKinsey — он предоставляет им AI-operating-layer.

**Механизм:** D27 fork-and-merge + D25 Company-as-Code + D13 Closed core / Open surface ВМЕСТЕ создают инфраструктуру, где:

1. Jetix maintains canonical upstream (methodology + core patterns + templates — closed-core) per D13.
2. Любой консалтинговый холдинг (включая McKinsey) может **fork** methodology, адаптировать под свой вертикал, свои процессы per D27.
3. Лучшие мутации возвращаются upstream через PR-style контрибуцию per D27.
4. Git-provenance (D25) делает каждое изменение audit-trailable.

**Результат:** McKinsey использует Jetix как "Windows прошивку"; Jetix не компанию-конкурента, а infrastructure-layer дома. Per audio_464: *«Jetix эта сеть которая позволяет консультантам и бизнесу адекватно и в реальном времени сотрудничать… под ней работают McKinsey и там еще какие-то остальные могут продолжать под ней работать»* [src:decisions/JETIX-VISION.md#10].

**Ruslan decision options:**
- **A. Accept resolution as-proposed** — closes §6 ambiguity; brigadier promotes into canonical.
- **B. Modify resolution** — provide specific edit; brigadier re-writes.
- **C. Reject resolution** — mark as unresolved; §6 stays open for future cycle.
- **D. Drill-down** — ask for deeper analysis (USB-C as open-standard vs proprietary; McKinsey-specific vs all-incumbents; Phase-2 vs Phase-3+ activation).

Brigadier recommends **Option A** (accept) — resolution is mechanical composition of three acked Locks (D13 + D20 + D27); no new territory introduced; enables Phase-3 strategy docs to reference coherent framing.

---

═══════════════════════════════════════════════════════════════════════════════

**END TOP-LEVEL SECTIONS §0-§6. 14 LAYER SECTIONS FOLLOW. EACH ≥800 WORDS.**

═══════════════════════════════════════════════════════════════════════════════

## §L0 Foundation — Company-as-Code

### Mission

L0 существует ровно для одного: обеспечить, чтобы **состояние Jetix было восстановимо из git-истории на любой момент времени**. Всё остальное — агенты, знания, клиентские проекты, стратегические решения — живёт поверх этого фундамента. Git-репозиторий IS компания: каждое изменение = snapshot, история = аудит-трейл, rollback = `git revert` [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25].

### What lives here

**Agents:** system-admin (infra/config/tools commits), brigadier (canonical wiki writes), engineering-expert (drafts + engineering strategies). Остальные 4 ROY эксперта имеют аналогичную write-scope per frontmatter.

**Documents:** `decisions/` (D1-D28 + VISION + PLAN + BRIEF — read-only post-ack), `design/` (FPF + SPEC — binding), `.claude/rules/global.md`, `raw/research/` (Tier-1 source material), `prompts/` (execution briefs).

**Tools/skills:** `/ingest` (D28 --anchor mandatory), `/lint` (`--check-stage-gates`, `--validate-predicate`), `/consolidate`, `/build-graph`, `/company-status` (git-native snapshot ≤80 строк zero network), `/knowledge-diff` (delta wiki between dates via git log). Все skills config-driven через `${WIKI_ROOT}` из `.claude/config/wiki-roots.yaml`; zero hardcoded paths.

**Data structures:**
- **Atomic commits** — `[area] verb what (why)` format. `area` ∈ {km-mvp, ingest, sys-overview, agents, config, templates, tools, docs}. No amend-after-push, no `--no-verify`, no force-push.
- **YAML declarative configs** — `.claude/config/wiki-roots.yaml`, `project-types.yaml`, `sg-banned-phrases.yaml` — каждый с `schema_version:`, `last_modified:`, `managed_by:`.
- **Provenance fields** в frontmatter — `sources[]` non-empty, inline `[src:<path>#<section>]` per non-trivial paragraph, `edges.jsonl` append-only граф 9 typed edges.

### Boundaries

**In-scope:** git-as-system-state + declarative configs + atomic-commits-with-provenance + verb-dictionary (shared-protocols §8: snapshot=commit, publish=push, local gate=pre-commit hook).

**Out-of-scope:** контент знаний → L1; voice-ingest pipeline → L2; agent memory → L4; Notion (UI-only, fs wins conflicts per D17).

### Interfaces

**Reads from:** все слои L1-L9 + cross-cutting читают L0 (git log, skills, configs, decisions) как read-only substrate.

**Writes to:** L0 не пишет в другие слои напрямую — **все остальные слои пишут В L0** через git commits.

**Invokes:** ничего. L0 passively invoked by everything via git operations.

### Current status 2026-04-24

- Ветка `claude/jolly-margulis-915d34` активная; no force-push; brigadier sole committer на canonical wiki
- 3 compound'нутых cycles в git log (swarm-self-improve-v1, cycle-2-impl, km-architecture-research); 4-й (sys-overview) в процессе
- Design record `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md` promoted state=accepted
- 3 yaml configs живут declarative
- 12+ skills active (ingest, lint, consolidate, build-graph, company-status, knowledge-diff, ask, project-bootstrap, project-review, project-archive, project-de-morph, project-promote)
- D1-D28 in force; D25 ACKED Ruslan 2026-04-24 22:45 CET

### Evolution path

**Phase 1 (€0-€50K):** Single-developer discipline. Все commits через brigadier. Atomic commit + provenance + declarative config уже в силе (инфраструктура готова к масштабированию с Day 1 — именно это значит D25).

**Phase 2 (€200K):** Первые 2-3 hires. L0 переходит на multi-dev commit discipline. CI pipeline (pre-commit hooks, PR review), branch protection rules. Engineering-expert split-trigger может сработать (§1d: artefact mix > 60/40 code vs architecture).

**Phase 3 (€1M):** **Federation via D27**. Каждый client/partner/roy получает fork Jetix canonical upstream. Downstream fork поддерживает свой git, адаптирует под свой vertical. Лучшие мутации merge-back через PR. L0 становится distributed git network.

**Phase 3+ ($100M → $1T):** Git-provenance as **legal audit-trail** для SOC2/GDPR. USB-C positioning (D20) реализуется через fork-and-merge: каждый бизнес работает на Jetix как «прошивке». D27 — механизм, как Jetix становится «Windows прошивкой» для любого AI-augmented business.

### Voice-memo references

- **audio_510 (21.04.2026, 15:21 CET):** *«строить инфраструктуру Company as a Code с самого начала, способную выдержать масштабирование до триллиона капитализации»* + *«в режиме GitHub работала — компания как код, знания как код»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]
- **audio_519 (22.04.2026, 17:54 CET):** *«Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя»* — D27 primary source
- **audio_520 (22.04.2026, 18:40 CET):** принципы системного разграничения задач на основе экспертных знаний

### Open questions for Ruslan

1. **D27 governance:** Кто maintains canonical upstream при первых forks — BDFL (Ruslan) / committee / meritocracy?
2. **Licensing:** MIT-like / proprietary-с-exception / dual-license? D13 + D27 требуют решения what-is-open-what-closed.
3. **IP protection at git-level:** Достаточно ли git-provenance для Phase 3+? Или patent + cryptographic signing коммитов?
4. **Multi-dev atomic-commit enforcement:** Кто enforce-ит format при появлении 2-3 hires Phase 2? Нужен pre-commit hook + CI check.

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L0-foundation.md` (authoritative detail: diagrams, full skill-list, provenance citations).

---

## §L1 Knowledge — Query-driven KB + Private Library

### Mission

L1 — curated moat: знания Jetix как главный конкурентный актив (per ROY-INFORMATION-DIET §1.6 *«curated качественная база знаний + новая философия работы с информацией… Knowledge-as-leverage — главный ров»*). Query-driven filtering per D28 — не жадное накопление, а filling driven by anticipated queries [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].

### What lives here

- **Hot working layer** `wiki/` v3 — 53 dirs, 9 entity types (concepts, entities, sources, topics, ideas, experiments, claims, summaries, foundations), 12 edge types, 6 niches (personal, business, sales, life, tech, meta)
- **Cold archive** — `raw/books-md/` (393 curated Private Library books), `raw/research/`
- **Topic-wikis per domain expert** (Pillar 2 VISION-NEXT) — `wiki/management/`, `wiki/systems-thinking/`, `wiki/engineering/`, `wiki/philosophy-of-science/`, `wiki/investing/` — NOT built yet
- **Project-wikis per Jetix project** (Pillar 3) — `wiki/projects/<project-id>/` — NOT built yet
- **Client-private namespaces** — `operations/clients/<slug>/` per STRATEGIC-INSIGHT Path C — NOT built yet; Phase-1 via A1 env-var + directory namespace
- **Graph edges** — `wiki/graph/edges.jsonl` append-only typed (extends, supports, contradicts, supersedes, derived_from, related, cross-tree-ref, refines, exemplifies, etc.)

### Boundaries

**In-scope:** knowledge content storage + retrieval architecture + query-filtering.
**Out-of-scope:** git-history-of-content → L0; ingestion-pipeline → L2; synthesis of content → L3; agent memory → L4.

### Interfaces

**Reads from:** L2 ingested-items.
**Writes to:** none outside wiki/.
**Invokes:** L3 synthesis via `/compile` and `/ask`.

### Current status 2026-04-24

- wiki v3 spine built (53 dirs, 12 edge types)
- wiki v2 legacy with pipeline raw→ingested→compiled→linted→ready в миграции per MIGRATION.md
- KM Mat design records promoted Wave-1 (Parts A+B+C) + Part D — substrate для Phase-2 A2+B2 migration
- Topic-wikis per expert NOT built; Project-wikis NOT built; client-isolation mechanics Phase-1-env-var-only

### Evolution path

Per sequenced-migration-trajectory acked 2026-04-24 KM-architecture-research cycle:

- **Phase 1 G1 (€0-€50K):** A1 Karpathy++ (filesystem-resident, retrieval-lean) + B1 project primitives. Simple, fast-to-bootstrap.
- **Phase 2 G2 (€200K, first paying client):** migration to A2 ontology-layered + B2 mini-swarm (federated-peer-holons; by-construction client-isolation).
- **Phase 3 G3 (€1M, ≥3K pages/client):** migration to A3 GraphRAG+HippoRAG-hybrid + B2 continues.
- **Phase 3+ ($100M+):** Mittelstand AI Alliance federation; CRDT edges + federated wikis.

### Voice-memo references

- **audio_522 verbatim (D28 source):** *«Целевая система сбора знаний под конкретную задачу более эффективна, чем универсальный сбор всей доступной информации. Собирать в KB только релевантное конкретному запросу и задаче, отфильтровывая лишнее»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]
- **audio_520:** knowledge-as-code Jetix principle
- **audio_517:** «описать конкретные части системы под запуски бизнесов»
- **audio_518:** system flexibility + auto-logging жизни

### Open questions

1. **Topic-wiki allocation:** который expert читает какую подгруппу 393 books? Previous allocation в FPF-ENHANCEMENT §10.2 — пересматривать?
2. **Project-wiki bootstrap timing:** до или после SYSTEM-OVERVIEW approval?
3. **Client-isolation Phase-1:** Path-B (client self-hosted) или Path-C (hybrid; Jetix hosts agents, client hosts data)? — requires investor-expert × integrator capital judgment (peer-input-needed).

### Diagram (hot + cold + topic + project + clients)

```
┌─────────────────────────────────────────────────────────────────┐
│ L1 Knowledge Layer                                              │
│                                                                 │
│ Hot working:                                                    │
│   wiki/v3-spine/                                                │
│     concepts/  entities/  sources/  topics/  ideas/             │
│     experiments/  claims/  summaries/  foundations/             │
│     niches/ {personal, business, sales, life, tech, meta}       │
│     graph/edges.jsonl  index.md  log.md  overview.md            │
│                                                                 │
│ Cold archive:                                                   │
│   raw/books-md/ (393 Private Library books)                    │
│   raw/research/ (Tier-1 source material)                       │
│                                                                 │
│ Planned (Pillar 2+3 materialization):                           │
│   wiki/management/ wiki/systems-thinking/ wiki/engineering/     │
│   wiki/philosophy-of-science/ wiki/investing/                  │
│   wiki/projects/<project-id>/{_moc,context,history,decisions}/  │
│                                                                 │
│ Phase-2 addition (UC-9 client-isolation):                       │
│   operations/clients/<slug>/{wiki, agents, data}/               │
│                                                                 │
│ Query surface:                                                  │
│   /ingest --anchor=<project|topic>   (D28 mandatory)            │
│   /ask --niche=<niche> --offline     (Q1 4-tier retrieval)      │
│   /lint --orphans --dangling-edges                              │
└─────────────────────────────────────────────────────────────────┘
```

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L1-knowledge.md`.

---

## §L2 Ingest & Signal

### Mission

L2 превращает raw-source (voice, URL, file, chat, crawler output) в wiki-entry с provenance + D28 anchor-filter. Система входа сигнала в Jetix.

### What lives here

**Voice pipeline** (automated):
1. `tools/transcribe.py` — Groq Whisper: OGG/MP3 → текст
2. `tools/extract.py` — Claude: транскрипт → structured items
3. `tools/filter.py` — Claude: dedup + meta-анализ
4. `tools/review_report.py` — markdown в `reports/review_YYYY-MM-DD.md` + `~/review-latest.md` (STOP gate — Ruslan читает, решает, ручное распределение)

**Auto-loggers** (планируемые) — git hooks, PostToolUse hooks.

**Reverse-engineering crawlers** (не built, но named):
- YouTube analyzer per audio_518 (Phase-2)
- AI-code extraction per audio_522
- Public-source shadow-reading per audio_527 (reverse-engineering на максималках)

**Legacy agent:** inbox-processor — information triage (CLAUDE.md Agent Roster).

**/ingest skill** — source → wiki pages + index + log + edges; D28 `--anchor=<project|topic>` MANDATORY (pending enforcement after KM Mat lands).

### Boundaries

**In-scope:** raw-source acquisition + conversion + initial triage + D28 anchor-filter.
**Out-of-scope:** canonical wiki storage → L1; synthesis → L3; compound-learning → L3.

### Interfaces

**Reads from:** external world (voice memos in inbox/, URLs, chat, raw files).
**Writes to:** L1 wiki/ via /ingest.
**Invokes:** L1 для dedup checks; L9 governance для anchor-registry.

### Current status 2026-04-24

- Voice pipeline complete; 529 memos processed to audio_529 (24.04 02:48)
- `reports/review_2026-04-24.md` — 1858 units / 141 memos; `reports/delta-506-529-2026-04-24.md` свежий
- inbox-processor legacy agent exists but низкая активность
- D28 anchor-enforcement NOT ENFORCED — upgrade pending после KM Mat lands
- Reverse-engineering crawlers NOT BUILT

### Evolution path

- **Phase-1 current:** manual voice-memo drop → pipeline → review STOP → manual distribution
- **Phase-1 mid:** /ingest --anchor enforced
- **Phase-2 (€200K+):** auto-loggers on all agent sessions; first crawler (YouTube-analyzer per audio_518)
- **Phase-3 (€1M+):** full reverse-engineering suite (public-source shadow-reading per audio_527)
- **Phase-3+ ($100M+):** industry-standard signal-acquisition network

### Voice-memo references

- **audio_514:** YouTube-анализатор concept
- **audio_518:** "гибкость системы" + auto-logging жизни
- **audio_522:** KB по запросу — D28 primary source
- **audio_527:** document-compass + YouTube-сетка + reverse-engineering

### Open questions

1. /ingest --anchor enforcement timing — bulk retroactive triage для ~529 существующих мемо?
2. Crawler legal/ethical surface per D27 fork-and-merge boundary — до Phase-2 crawler launch.
3. Per-client ingest isolation Phase-2 — session-level WIKI_ROOT_CLIENT_ID атрибуция не специфицирована.

### Diagram

```
Raw sources                 Pipeline stages                    Destination
┌──────────────┐    ┌─────────────────────────────────┐    ┌──────────────┐
│ voice-memos  │───▶│ tools/transcribe.py (Whisper)   │───▶│ reports/     │
│ .ogg/.mp3    │    │ tools/extract.py (Claude)       │    │ review_NNN   │
└──────────────┘    │ tools/filter.py (dedup+meta)    │    │ .md          │
                    │ tools/review_report.py          │    └──────┬───────┘
                    └─────────────────────────────────┘           │
                                                            STOP (Ruslan)
                                                                  │
┌──────────────┐    ┌─────────────────────────────────┐           ▼
│ URL / file   │───▶│ /ingest --anchor=<project|topic>│────▶ L1 wiki/
│ chat / idea  │    │ (D28 mandatory)                 │      + edges.jsonl
└──────────────┘    └─────────────────────────────────┘
┌──────────────┐                                              ▲
│ crawlers     │── (Phase-2+: YouTube analyzer,              │
│ (Phase 2+)   │    AI-code extraction,                       │
└──────────────┘    public-source shadow-reading) ──────────┘
```

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md`.

---

## §L3 Synthesis & Compounding Engineering

### Mission

L3 — цикл Plan/Work/Review/Compound 40/10/40/10: превращение events в DRR rules + strategies accumulation. Sandbox-черновик принцип per audio_520 — все upstream changes flow drafts→review→ack→canonical. Мета-описания-first-filter per audio_519.

### What lives here

**Agents:**
- **strategist** (legacy) — long-term decisions
- **knowledge-synth** (legacy, Sonnet 4.6, Brain Lead) — deep cross-source synthesis
- **meta-agent** (legacy) — system auditing
- **brigadier compound protocol** (ROY §8) — per-cycle DRR writes

**Skills:**
- `/compile` (ingested→compiled wiki article)
- `/ask` (retrieve+synthesize with citations + Q1 4-tier retrieval)
- `/consolidate` (merge duplicates — `--weekly` auto-merge)
- `/build-graph` (rebuild community edges)

**Protocols:**
- **Compounding Engineering 40/10/40/10** (Plan/Work/Review/Compound wall-clock)
- **Sandbox-черновик pattern** per audio_520 for upstream changes
- **SG-DSL stage-gate predicates** per KM-Mat Part C — Hamel-binary + DSL-canonical
- **DRR 4-part entries** (Decision/Reasoning/Result/Review; canonical translation per critic-gate1 M-2)

**Data structures:**
- `agents/<id>/strategies.md` — Layer-2 personal memory (per-expert self-write)
- `swarm/wiki/meta/agent-improvements/` — cross-agent (brigadier sole-writer per Q2)
- `swarm/wiki/insights/` — emergent concept pages (immediate write on surprise)
- `swarm/logs/<cycle-id>/cycle-log.md` + events.md

### Boundaries

**In-scope:** distillation of experience into rules + cross-source synthesis + compound-learning mechanism.
**Out-of-scope:** raw knowledge storage → L1; ingest → L2; routing/dispatch → L4; gate-check → L9.

### Interfaces

**Reads from:** L1 wiki + L2 ingested items + L4 cell return drafts.
**Writes to:** L1 canonical wiki via brigadier + own strategies.md (Layer-2).
**Invokes:** L9 for AWAITING-APPROVAL when emergent insight needs Ruslan ack.

### Current status 2026-04-24

- 3 compound'нутых cycles visible; agents/brigadier/strategies.md has 8+ DRR entries (Gate A-D learnings + sequenced-migration-trajectory + 20-cell 4-wave parallel pattern + word-count-floor-pattern)
- 5 per-expert improvements files seeded under `swarm/wiki/meta/agent-improvements/`
- swarm/wiki/insights/ dir exists but empty (emergent pattern surface opportunity Phase-2+)
- `/compile`, `/ask`, `/consolidate`, `/build-graph` skills in wiki v3 spine

### Evolution path

- **Phase-1 current:** compound per cycle via brigadier discipline; strategies.md manual accumulation
- **Phase-2 (€200K-€1M):** skill codification `/extract-from-design` + `/recommend-trajectory` (per brigadier strategies open questions)
- **Phase-3 (€1M-$100M):** cross-project compound at holding level (each Jetix project's strategies feeds parent + peer projects)
- **Phase-3+ ($100M+):** federated compound Mittelstand AI Alliance methodology-parliament

### Voice-memo references

- **audio_519:** sandbox-черновик + «Создать мета-описания для каждой подсистемы с указанием что система делает и не делает, чтобы это служило первичным фильтром»
- **audio_520:** knowledge-as-code; Compounding Engineering principle
- **audio_521:** «разделить систему на основные модули»

### Open questions

1. When promote `/recommend-trajectory` skill — after 5 M-structural cycles?
2. When `swarm/wiki/insights/` crosses N pages — trigger Phase-B Layer-9 activation?
3. How compound propagates across legacy 14 agents — via meta-agent bridge или separate pass?
4. Cross-project compound mechanism Phase-3 — how project's strategies feed peer projects without contamination?

### Diagram

```
        Plan (40%)            Work (10%)            Review (40%)       Compound (10%)
       ┌───────────┐         ┌──────────┐         ┌───────────┐       ┌────────────┐
       │  Intake   │         │Dispatch  │         │Integrate  │       │DRR entries │
       │+Decompose │────────▶│cells via │────────▶│cells +    │──────▶│+strategies │
       │+WBS+Risk  │         │Task()    │         │§5.5.5 gate│       │+insights   │
       └───────────┘         └──────────┘         └───────────┘       └────────────┘
                                                                            │
                                                                            ▼
            ┌───────────────────────────────────────────────────────────────────┐
            │ agents/<id>/strategies.md (Layer-2 personal memory)              │
            │ swarm/wiki/meta/agent-improvements/ (cross-agent, brigadier-only) │
            │ swarm/wiki/insights/ (emergent concept pages)                     │
            └───────────────────────────────────────────────────────────────────┘
                                       │ next cycle reads ←
                                       ▼
                                 (feedback to Plan)
```

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L3-synthesis.md`.

---

## §L4 Agent Layer — Holding-Style

### Mission

L4 — holding-style agent workforce per D26: 6 ROY experts + brigadier orchestrator + 14 legacy agents = 20 агентов, работающих как interconnected layer. Jetix-как-холдинг с interacting agents: не один агент-монополист, а holding с internal markets / cross-cell reads / brigadier-mediated integration [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26].

### What lives here — full 20-agent roster

**Phase A ROY (6 agents, built 2026-04-23; 3 cycles compounded):**

| Agent | Model | Dept | Niche | Role |
|---|---|---|---|---|
| brigadier | Opus | orchestration | meta | Single-writer canonical wiki; dispatches 5×4 matrix; HITL mediator |
| engineering-expert | Opus | engineering | tech | Code review, architecture, refactor (×4 modes) |
| mgmt-expert | Opus | management | business | PM, delivery, stakeholder, ethics BA-Cycle |
| systems-expert | Opus | systems | meta | Meadows leverage, Ashby, Beer VSM, Kauffman |
| philosophy-expert | Opus | philosophy | meta | Epistemic audit, Popper, mental models, stoic |
| investor-expert | Opus | investing | business | Capital allocation, moat, horizon projection, unit-econ |

**Legacy 14 agents** (untouchable in Phase A per brigadier §1a):

| Agent | Model | Dept | Phase |
|---|---|---|---|
| manager | Sonnet 4.6 | MGMT | 1 |
| personal-assistant | Haiku 4.5 | OPS | 1 |
| system-admin | Haiku 4.5 | OPS | 1 |
| sales-lead | Sonnet 4.6 | Sales | 2 |
| sales-researcher | Haiku 4.5 | Sales | 2 |
| sales-outreach | Haiku 4.5 | Sales | 2 |
| inbox-processor | Haiku 4.5 | Brain | 2 |
| crazy-agent | Sonnet 4.6 | Meta | 2 |
| knowledge-synth | Sonnet 4.6 | Brain | 3 |
| strategist | Opus 4.6 | MGMT | 3 |
| life-coach | Sonnet 4.6 | Life | 4 |
| meta-agent | Sonnet 4.6 | Meta | 4 |
| staging-writer | task-scoped | task | — |
| sweep-worker | task-scoped | task | — |

### Key architectural properties

- **5×4 matrix dispatch** — 5 experts × 4 modes (critic / optimizer / integrator / scalability) = 20 invocation cells. Brigadier dispatches; cells write drafts under `swarm/wiki/drafts/`; brigadier integrates + promotes per §5.5.5 provenance gate.
- **5-layer per-agent memory** per CLAUDE.md: Core (system.md), Strategies (strategies.md), Scratchpad, Niche (symlinks), Recall (mailbox .jsonl).
- **Hub-and-spoke** routing per CLAUDE.md Global Rule 8: subagents report to department lead, not Manager. ROY 5 experts report to brigadier.
- **Holding-with-agents** per D26 — target steady-state team 50-100 humans; agents interact per cross-cell-reference-protocol (read wiki, never call cell); brigadier is sole-writer to canonical; experts write drafts + own strategies.md.

### Boundaries

**In-scope:** agent definitions + 5×4 matrix + 5-layer memory + routing grammar.
**Out-of-scope:** routing-logic-itself → shared-protocols (L9 governance); compound-learning → L3; knowledge storage → L1; ICP-filter → L6 (though sales-legacy agents live here for Phase-1 execution).

### Interfaces

**Reads from:** L0 git-state + L1 wiki + L3 strategies + incoming tasks.
**Writes to:** L1 via brigadier + own strategies.md (per Layer-2 self-write).
**Invokes:** L9 AWAITING-APPROVAL gates on trigger.

### Current status 2026-04-24

- 6 ROY live (Phase A); 14 legacy present but most quiet (operational at need)
- 3 cycles compounded; brigadier strategies has 8+ DRR entries
- CLAUDE.md Agent Roster lists 12 (does not include ROY 6 or staging-writer/sweep-worker); reconcile needed
- Brigadier single-writer Q2 lock in force; untouchable legacy + v2 wiki per Phase-A discipline

### Evolution path

- **Phase-1 (€0-€50K):** sole-founder Ruslan + 20 agents. Legacy 14 on standby.
- **Phase-2 (€200K-€1M):** first 2-3 human hires join. ROY experts split (engineering-expert split-trigger may fire per §1d). Legacy agents consolidate (some retire, некоторые migrate to ROY).
- **Phase-2b (~$100M):** team grows to 10-20 humans; sub-brigadiers per direction emerge.
- **Phase-3 (~$100M revenue):** 50-100 humans per D26 steady-state. Brigadier Phase-B split into [task-dispatcher, integration-manager, gate-keeper] per §1d.
- **Phase-3+:** roy-replication per D21 to external swarms (Mittelstand AI Alliance members run their own swarms on Jetix methodology).

### Voice-memo references

- **audio_510:** team 50-100 holding-with-agents (D26 primary)
- **audio_514:** YouTube-analyzer agent concept
- **audio_521:** split system into modules
- **audio_529:** Smart AI + миллионеры context

### Open questions

1. **Legacy-14 fate** — migrate to ROY or retire? Timing?
2. **CLAUDE.md reconcile** — lists 12 agents but actual 20; update CLAUDE.md to reflect Phase A reality?
3. **Per-human team-member onboarding-to-swarm protocol** — how does a new hire Phase 2 integrate with 20 agents? Dedicated agent-per-human mapping or shared?
4. **Brigadier split-trigger timing** — at which specific Phase-B metric threshold?

### Diagram

```
                          ┌─────────────────────────┐
                          │   Ruslan (HITL gate)    │
                          └────────────┬────────────┘
                                       │
                          ┌────────────▼────────────┐
                          │      brigadier           │  ◇ sole writer canonical wiki
                          │  (Opus; orchestrator)    │  ◇ dispatches 5×4 matrix
                          └────────────┬─────────────┘
                                       │ Task()
           ┌───────────────┬───────────┼───────────┬───────────────┐
           ▼               ▼           ▼           ▼               ▼
      ┌─────────┐   ┌─────────┐  ┌──────────┐  ┌─────────┐   ┌──────────┐
      │ eng-    │   │  mgmt-  │  │ systems- │  │philos-  │   │ investor-│
      │ expert  │   │ expert  │  │ expert   │  │ expert  │   │ expert   │
      │ ×4 modes│   │ ×4 modes│  │ ×4 modes │  │ ×4 modes│   │ ×4 modes │
      └─────────┘   └─────────┘  └──────────┘  └─────────┘   └──────────┘
           └─────── write to ──▶  swarm/wiki/drafts/  ◀── read from (cross-cell)

                          ═════════════════════════════
                         Legacy 14 (ring around core):
                          ═════════════════════════════
       manager, PA, system-admin, sales-lead, sales-researcher, sales-outreach,
       inbox-processor, crazy-agent, knowledge-synth, strategist, life-coach,
       meta-agent, staging-writer, sweep-worker
```

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L4-agents.md`.

---

## §L5 Product & Services — Smart AI directions

### Mission

L5 — concrete product/service portfolio Jetix. «Smart AI» (internal label per D25-D28 addendum, NOT a lock) используется внутренне для flagship. Product-layer как distinct от L6 business-trajectory-gates: что именно продаёт Jetix (portfolio), не сколько и кому (trajectory).

### What lives here — 9 directions

| # | Direction | Phase activation | Status 2026-04-24 | Primary audio_NNN |
|---|---|---|---|---|
| 1 | **AI consulting for complex tasks** | Phase 1 core | €0, no clients | audio_511 |
| 2 | **Продюсерский центр** (AI-produced content, English infobiz) | Phase 1 core | Not launched, no pilots | audio_508 |
| 3 | **USB-C integration services** (client-private AI + methodology) | Phase 2+ productized | Manual implementation only | audio_508 + chat-voice |
| 4 | **Matchmaker platform** | Phase 2+ (manual-now, platform-later) | Manual ad-hoc | audio_514 |
| 5 | **Secure Network** (quality-gated pro network + tool-sharing) | Phase 2+ | Not built | audio_510 |
| 6 | **YouTube-analyzer SaaS** (reverse-engineering product) | Phase 2+ | Conceptualized | audio_514 / 518 / 527 |
| 7 | **Educational products** (Jetix methodology repo, licensable) | Phase 2+ | Not built (STRATEGIC-INSIGHT Path B prereq) | audio_524 |
| 8 | **Tokens / ICO** (D23 Phase 3+) | Phase 3+ | Not designed | audio_527 |
| 9 | **Smart AI flagship label** | all Phases (internal) | In use internally | audio_529 |

### Smart AI status

*«ну типа запиши между прочим но нет это ещё не лок блять забей хуй»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]. Marker, not lock. Official positioning stays Jetix; Smart AI = one way to describe what Jetix делает, may be used for internal discussion + potentially external sales material, but NOT D29.

### Boundaries

**In-scope:** what Jetix sells or builds as product/service + per-direction mission + per-direction phase-activation.
**Out-of-scope:** per-gate revenue targets → L6; Alliance-specific methodology delivery → L8; brand taglines → L-B; pricing-philosophy-detail → L6.

### Interfaces

**Reads from:** L1 knowledge (what can be productized) + L4 agents (who can deliver) + L6 ICP filter (who buys).
**Writes to:** L8 Alliance+partnerships pipeline + L6 revenue pipeline.
**Invokes:** L-B brand-messaging per direction.

### Evolution path through 5 gates

- **G0 → G1 (€0 → €50K Q2 2026):** consulting + продюсерский центр ТОЛЬКО. Остальное NOT activated.
- **G1 → G2 (€50K → €200K):** matchmaker transitions manual→platform-concept. Secure Network architecture design begins.
- **G2 → G3 (€200K → €1M):** Secure Network launched; matchmaker platform V1; USB-C services productized; methodology repo V1 (Path B prerequisite).
- **G3 → G4 ($1M → $100M):** YouTube-analyzer SaaS launched; educational products scale; tokens Phase-2 internal utility per D23.
- **G4 → G5 ($100M → $100B → $1T):** tokens Phase-3+ public layer (D23 if Option B/C approved); Mittelstand AI Alliance scales.

### Open questions

1. **Smart AI → D29 lock или stay internal?** Currently internal note per D25-D28 addendum — Ruslan explicit directive.
2. **Path A/B/C for Phase-1 pricing** per STRATEGIC-INSIGHT §5 — Jetix-hosted / Client-hosted / Hybrid? Capital implications differ.
3. **Matchmaker manual→platform trigger** — G2 (€200K) or G3 (€1M)?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md`.

---

## §L6 Business & Trajectory

### Mission

L6 — бизнес-слой: ICP targeting + outreach + pricing + partnerships + phase-gate trajectory €50K → $1T. Где revenue/capital-accumulation activity живёт. Distinct от L5 (что продаёт) — focus on кому, как, сколько.

### What lives here

**ICP (Ideal Customer Profile):**
- **11 archetypes** per JETIX-VISION §7.1: Предприниматели / Ресёрчеры / Инженеры / Инвесторы / Политики / Продавцы / Менеджеры / Философы / Разработчики-идей / Разработчики-жизни / Блогеры
- **D22 qualitative filter (5 criteria):** Startupper mindset / Предпринимательский азарт / Stable / Adequate / Upward-direction
- **Phase-1-buyer "миллионер $1M+/year"** per audio_529 NEW explicit buyer segment (tension with JETIX-VISION primary-buyer, see Open Questions)
- **Direction-of-life axis** (vertical: upward vs downward) > topic axis (horizontal)

**Outreach mechanism:**
- Currently manual (Ruslan + Cloud Cowork ad-hoc)
- First-batch Phase-1 targeted per JETIX-VISION §11 (English-speaking infobiz + US + UK + international)
- Sales legacy agents: sales-lead (Sonnet 4.6) + sales-researcher (Haiku 4.5) + sales-outreach (Haiku 4.5) in Dept Sales

**Pricing:**
- **Entry:** €150/h baseline per D18 productization-over-hours
- **Tiered Path A/B/C** per STRATEGIC-INSIGHT §5: Jetix-hosted (managed, highest margin, low-touch SMB) / Client-hosted (maximum data sovereignty, self-sufficient technical clients) / Hybrid (client owns data, Jetix hosts agents, Enterprise)

**Partnerships:**
- **Concrete Phase-1:** Cloud Cowork + operator's personal warm network
- **Speculative Phase-3+:** Anthropic / Porsche / BMW / Apple / Google / Tesla per audio_515 (enterprise-scale, post-€100M)

**5 Gates trajectory:**

| Gate | Trigger | Unlocks |
|---|---|---|
| G1 €50K Q2 2026 | Cumulative revenue €50K | GmbH + Stripe + $1000 experiment + community chat |
| G2 €200K | Validation €200K | Secure Network arch design + patents process + first 2-3 hires |
| G3 €1M/mo | Revenue run-rate €1M | International scale + holding-structure + data-center planning |
| G4 $100M | Revenue or market cap $100M | Roy-replication external + USB-C positioning launch + tokens Phase-2 |
| G5 $100B → $1T | Market cap $100B → $1T | Civilizational infrastructure + civilization-level conversations |

### Boundaries

**In-scope:** who-buys / how-approached / how-priced / how-gated.
**Out-of-scope:** product-catalog → L5; team-size-per-gate → L8; brand-messaging → L-B; research-direction → L7.

### Interfaces

**Reads from:** L5 product-portfolio + L-B brand-messages.
**Writes to:** L-R resource-allocation budget inputs + L8 Alliance-revenue-share + L9 governance gate triggers.
**Invokes:** L4 sales-legacy-agents.

### Current status 2026-04-24

- €0 Phase-0 active; no paying clients; outreach not started; 0 partnerships
- Gate-G1 target set (€50K Q2 2026 — single committed absolute date per JETIX-PLAN D3) but not tracked in dashboard yet
- ICP documented per JETIX-VISION §7 but not tiered per Phase-1 priority
- Per KM-Mat investor-critic arbitration (gate AWAITING): Option B recommends €30K contracts + €35K hourly = €65K (buffer above €50K) per quarter mix

### Voice-memo references

- **audio_506:** enterprise-fast positioning
- **audio_510:** team 50-100 + holding-with-agents
- **audio_511:** AI consulting nature
- **audio_515:** potential partnerships list (Anthropic/Porsche/BMW/Apple/Google/Tesla) — Phase-3+ speculative
- **audio_523:** market direction
- **audio_528:** OS мирового масштаба
- **audio_529:** миллионеры $1M+/year Phase-1 buyer segment

### Open questions

1. **Миллионер $1M+/year** как hard gate vs aspirational frame? audio_470 calls $20-50K/month ($240-600K/year) the real target — below $1M+ floor. Reconciliation needed.
2. **Outreach medium Phase-1** — LinkedIn + email + warm vs cold?
3. **Partnership prospect trigger** — revenue-gated or opportunistic?
4. **Mittelstand AI Alliance formalization timing** — STRATEGIC-INSIGHT §3 requires speed (6-12 months window), JETIX-PLAN doesn't mention Alliance in Phase-1 actions. Tension.

**Preserved dissent (mgmt-integrator vs STRATEGIC-INSIGHT):** Informal Alliance conversations opportunistically Phase-1 if contact surface; formal legal structure strictly G2+.

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L6-business.md`.

---

## §L7 Research & Reverse-Engineering

### Mission

L7 — research-layer with phase-sequenced dual-mode: D14 revenue-instrumental Phase-1 only + D24 open-source direction Phase-3+ + reverse-engineering-на-максималках audio_527 + new AI protocols/laws/validation tools (chat-voice USB-C). Левенчук ШСМ methodology-grounding.

### What lives here

**Phase-1 Research streams (revenue-instrumental per D14):**
- Sales enablement research (ICP refinement, competitor analysis, Mittelstand knowledge)
- BIOS/clone-wars parallel research (raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md — 621 lines; already done 2026-04-24)
- Левенчук ШСМ reading (Systems Thinking / Systems Engineering grounding) — personal ongoing

**Phase-3+ Research streams (D24 open-source):**
- *«как люди коммуницируют, как компании кооперируют, как должна работать будущая экономика»* [src:decisions/JETIX-VISION.md#5]
- Reverse-engineering на максималках per audio_527 — industry-standard analysis, competitor tear-down, public-source deep-reading
- **New AI protocols / laws / validation-tools** per chat-voice-USB-C verbatim: *«новые сети, новые протоколы, новое вообще понимание что как работает, новые законы, новые инструменты для проверки этого всего»* — Jetix position as **standards-level contributor** not just consumer

**Private Library** — 393 curated books under `raw/books-md/` (cross-ref to L1 cold archive)

### Boundaries

**In-scope:** research projects + reverse-engineering targets + standards-contribution activities + methodology import from external thinkers.
**Out-of-scope:** knowledge-content-storage → L1; product-built-from-research → L5; revenue-from-research → L6.

### Interfaces

**Reads from:** L1 Private Library + L2 crawler-signal.
**Writes to:** L5 product-inspirations + L8 Alliance-methodology-parliament contributions (Phase-3+) + L1 published research artefacts.
**Invokes:** L4 knowledge-synth + L9 governance gate для external publication.

### Current status 2026-04-24

- Private Library 393 books curated (since cleanup + Mistral OCR re-run)
- 1 BIOS research doc complete (621 lines; informs STRATEGIC-INSIGHT positioning)
- Ad-hoc reverse-engineering on existing market (competitor AI consulting shops)
- D24 research direction NOT activated — Phase-3+ trigger
- D14 enforces Phase-1 research only-if-serves-revenue
- Левенчук reading ongoing personal, not systematic

### Evolution path

- **Phase-1 (€0-€50K):** D14 revenue-instrumental — research ONLY serves current revenue (sales enablement, ICP refinement, Mittelstand knowledge, competitor analysis). Левенчук читается лично.
- **Phase-2 (€200K-€1M):** unlock patents process per STRATEGIC-INSIGHT; first reverse-engineering crawler products; Левенчук ШСМ systematic integration.
- **Phase-3 (€1M-$100M):** D24 open-source research direction activates; standards-contribution via Mittelstand AI Alliance; published papers.
- **Phase-3+ ($100M-$1T):** civilizational-level research — cooperation-protocols, economy-design, AI-to-AI contract validation.

### Voice-memo references

- **audio_510:** team 50-100 + describe local teams
- **audio_515:** enterprise outreach context (read as Phase-2+ enterprise territory)
- **audio_524:** digital portraits + partnerships
- **audio_527:** document-compass 5-15 pages + reverse-engineering на максималках

### Philosophy-rigor note (epistemic-vs-instrumental tension)

**Preserved tension per philosophy-integrator:** D14 governs Phase-1 action (instrumental constraint: research serves revenue). D24 governs long-horizon intent (epistemic value: open-source for humanity). Both are TRUE simultaneously. They are composable only through phase-sequencing. Any synthesis that collapses them into ONE claim would be AP-PHIL-3 (instrumental-vs-epistemic-collision). Tension preserved; no force-resolution.

### Open questions

1. **Левенчук ШСМ systematic-read timing** — Phase-2 unlock (first hire reads Левенчук as part of onboarding)?
2. **First reverse-engineering product target** — YouTube-analyzer per audio_518 or something else?
3. **Standards-contribution mechanism Phase-2** — participate in existing bodies or establish Mittelstand AI Alliance per STRATEGIC-INSIGHT §4-5?
4. **Research-publication cadence Phase-3** — quarterly papers or on-readiness?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L7-research.md`.

---

## §L8 People & Alliance — Swarm + Digital Portraits

### Mission

L8 — people-and-alliance layer: humans behind Jetix + external networks. Distinct from L4 (agents) because humans are team-members + Alliance-partners + community-members. D26 target 50-100 humans steady-state; D27 fork-community; Mittelstand AI Alliance; matchmaker network; Secure Network.

### What lives here

- **Core team 50-100 per D26** — Jetix target steady-state humans (NOT agents). Phase-1: solo Ruslan + Cloud Cowork. Phase-2: first 2-3 hires. Phase-3: 50-100 distributed per D21 holding-roy-structure.
- **Alliance + 5h/week roy-replication per D21** — each Jetix methodology-user commits ≥5h/week; network accretes specialists transitioning-to-Jetix over time.
- **Secure Network** — Telegram-based Phase-1 simple + Phase-2+ platform per Decision 5 evolution + STRATEGIC-INSIGHT. Quality-gated ICP-filtered per D22. Thematic sub-networks per archetype.
- **Digital portraits per audio_524** — each Alliance member has curated profile (skills / interests / available-hours / past-roy-contributions). System-readable for matchmaker routing.
- **Fork-community per D27** — Jetix canonical upstream + each practitioner forks methodology + contributes back best mutations. Governance TBD per D27.
- **Matchmaker manual-now per D21** — Ruslan currently manually connects "сложная задача" + "specialist" + "AI-agents smooth coordination". Phase-2+ platform.
- **Mittelstand AI Alliance per STRATEGIC-INSIGHT §4** — EISA-moment sovereign European AI consortium. Formalization timing: Phase-2 open question. Potential structure: Linux Foundation / ARM Holdings analog.
- **3-audience landing pages per audio_507** — авантюристы / инвесторы / работники мечты. Ties into L-B brand but lists here as community-entry-point.

### Boundaries

**In-scope:** humans-as-collaborators + networks-of-humans + matchmaking-between-humans.
**Out-of-scope:** agents → L4; ICP-selection-criteria → L6; brand-messaging → L-B; product-for-Alliance → L5.

### Interfaces

**Reads from:** L6 ICP filter + L4 matchmaker-agent routing.
**Writes to:** L5 Alliance-product-requirements + L-B audience-segmentation + L-R resource-claims (5h/week commitment accounting).
**Invokes:** L9 governance for fork-and-merge upstream decisions.

### Current status 2026-04-24

- Ruslan + Cloud Cowork only; 0 team hires
- Secure Network Telegram-chat NOT yet created
- Digital-portraits NOT designed
- Fork-community NOT launched
- Matchmaker manual — Ruslan doing it ad hoc
- Mittelstand AI Alliance concept-only
- 3-audience landings NOT built

### Evolution path

- **G0 → G1 (€0-€50K):** solo + Cloud Cowork + first invite-based Telegram chat 5-20 members
- **G1 → G2 (€50K-€200K):** first 2-3 hires (per D15 revenue-gated); Secure Network architecture design; matchmaker platform concept
- **G2 → G3 (€200K-€1M):** team 5-10; Mittelstand AI Alliance formalization; digital-portraits launched; fork-community opened (per D27 timing)
- **G3 → G4 (€1M-$100M):** team 20-50 per D26 trajectory; Alliance membership 100-500; roy-replication external (first swarm other than Jetix-core)
- **G4 → G5 ($100M-$100B-$1T):** team 50-100 per D26 steady-state; Alliance 1000-5000+; multi-roy ecosystem; Secure Network full platform

### Voice-memo references

- **audio_506 / 507 / 510 / 512 / 513 / 519 / 524 / 525 / 527** — full sweep covered in cell draft

### D26 verbatim

*«Jetix будет не one person company, а команда из 50-100 человек, работающая как холдинг»* + *«у нас тут большая компания с мощными дядями ребятами у нас enterprise но только enterprise который довольно быстрый»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26].

### D27 verbatim

*«Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя, а лучшие мутации возвращать в основную ветку»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27].

### Open questions

1. **Fork-and-merge governance** per D27 §Downstream (BDFL / committee / meritocracy)?
2. **Secure Network platform timing** — G2 design, G3 launch?
3. **Digital portraits tooling** — custom build or existing CRM adaptation?
4. **Alliance legal structure choice** — Linux Foundation analog (non-profit consortium) vs ARM Holdings analog (for-profit standards body)?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md`.

---

## §L9 Governance & Evolution

### Mission

L9 — governance layer: правила, governing Jetix evolution itself. Constitutional (28 Locks) + operational (sandbox-черновик, beta-first, не переспрашивать, не даунгрейдить) + mechanism (AWAITING-APPROVAL gate format, brigadier §1d matrix, DRR shape).

### What lives here

**Constitutional — 28 Locks D1-D28:**
- D1-D24 in 3 TENSIONS docs (PRE-RESOLVED, RESOLVED, RESOLVED-STAGE-2B)
- D25-D28 in LOCKS-D25-D28-ADDENDUM (2026-04-24)
- Overriding a Lock requires foundation-revision gate — HITL-only per brigadier §1d

**Mechanism:**
- **decisions/ directory** — all D-documents + strategic-insight + master-plan + cycle-reports
- **AWAITING-APPROVAL gate** per shared-protocols §4 — 9 escalation triggers (foundation-revision / Layer-9 activation / contradiction / budget-overrun / retry-limit / direction-change / method-exhaustion / irreversible / split-trigger)
- **Brigadier §1d decision-rights matrix** — autonomous / requires-approval / never / split-trigger

**Operational policies:**
- **Sandbox-черновик принцип** per audio_519/520 — all upstream changes flow drafts → review → ack → canonical
- **Мета-описания as first filter** per audio_519 — every system component has meta-description read FIRST before doing work
- **Fork-and-merge upstream-controller** per D27 — canonical + downstream forks + merge-back
- **Beta-first / не переспрашивать / не даунгрейдить** per audio_528 — all new capabilities beta-first with explicit beta-label; no degrading product after beta; no asking-same-question-twice

**Compound protocol** per brigadier §8 — every cycle writes DRR entries to strategies.md; cross-cycle learning.

### Brigadier §1d decision-rights summary

| Category | Examples |
|---|---|
| **Autonomous** | Intake well-formed task + AP; decompose per §3 within 20-cell cap; dispatch Task() to matrix cells; integrate drafts; run §5.5.5 gate; promote drafted→accepted; append to log/index/graph; write own strategies; close cycle; rotate logs at 30 entries |
| **Requires-approval (AWAITING-APPROVAL)** | Foundation revision; Layer-9 activation; contradiction with foundation; external action (email/Notion/PR); irreversible decision; write to swarm/wiki/global/; α-5 Direction change; method exhaustion; budget overrun; stuck alpha |
| **Never** | Self-strategizing; primary writing; external comms without HITL; direct commit to global without gate; calling experts without mode-prefix; override expert judgment; bypass §5.5.5 gate; reference API-key env-vars |
| **Split-trigger (Phase B)** | Task-intake >10/week sustained; 2+ concurrent α-4 cycles; accountability items >7 |

### Boundaries

**In-scope:** rules-about-Jetix-itself + meta-level discipline + HITL gate mechanics + governance evolution.
**Out-of-scope:** operational execution → L3/L4; product-gates → L6; resource-tracking → L-R.

### Interfaces

**Reads from:** ALL layers (cross-cutting — governance is pervasive).
**Writes to:** ALL layers via AWAITING-APPROVAL gates + sandbox-черновик.
**Invokes:** HITL (Ruslan) for ack.

### Current status 2026-04-24

- 28 locks in force (D1-D28)
- 3 gates acked historically — swarm-self-improve-gate2 + cycle-2-impl + km-architecture-variants
- 1 gate AWAITING — km-materialization-mvp (Option B recommended; Ruslan ack pending)
- Fork-and-merge D27 acked but governance mechanism NOT designed (Phase-3+ activity)
- Beta-first policy unwritten (open question)
- Brigadier strategies.md live — 8+ DRR entries accumulating per cycle

### Evolution path

- **Phase-1 solo:** Ruslan-HITL for every gate; brigadier §1d enforced
- **Phase-2 (€200K-€1M):** governance scales as team joins; first delegation of gate-ack authority (which subset of triggers still Ruslan-only vs delegable?)
- **Phase-3 (€1M+):** fork-and-merge governance formalized per D27; Phase-B brigadier split-trigger may fire per §1d
- **Phase-3+ ($100M+):** Mittelstand AI Alliance methodology-parliament co-governs methodology-upstream per STRATEGIC-INSIGHT
- **Phase-3+ $1T:** constitutional-level evolution — 28 locks themselves may be amended via formal process

### Voice-memo references

- **audio_519:** sandbox-черновик + мета-описания
- **audio_520:** knowledge-as-code + системное разграничение
- **audio_521:** split system into modules
- **audio_528:** OS мирового масштаба + beta-first implied

### Preserved dissent (philosophy-integrator)

**Beta-first vs quality-from-day-one tension:** audio_528 verbatim «разрабатывать все качественно, ответственно и глубоко» refutes naive reading of beta=degraded. Resolution: beta = gate-timing, not craft standard. Different strata (operational policy vs craft discipline); no constitutional conflict.

### Open questions

1. **Fork-and-merge governance model** per D27 §Downstream (BDFL/committee/meritocracy)?
2. **Gate-ack delegation Phase-2** — which triggers can be delegated vs HITL-only?
3. **Beta-first policy formalization** — write-up needed (currently unwritten)?
4. **Constitutional-amendment process** — if a Lock ever needs revision, what's the mechanism?
5. **Не даунгрейдить policy** — canonicalize as Lock D29 or keep as operational?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L9-governance.md`.

---

## §L-R Resource Management (cross-cutting)

### Mission

Unified tracking of **time / attention / finances / energy / credits** across every layer. Every decision consumes these; system must know current state + projections. Per Ruslan verbatim: *«очень важно, всё должно тоже трекаться»*.

### 5 resources

1. **Time** — Ruslan-hours / agent-turns / cycle-wall-clock / CE 40/10/40/10 cadence / per-cell ap_budget / Ruslan non-delegatable orbit per D11 (6 functions).
2. **Attention** — Ruslan's attention budget (brigadier §1d max-20-active-tasks lock); per-agent context-window; cognitive load per decision.
3. **Finances** — bank balance (~$5K per founder-context); per-project revenue pipeline; per-gate revenue trigger per D15; operating burn (Max-subscription only per shared-protocols §9; no paid APIs).
4. **Energy** — Ruslan personal energy (audio_428 rest/burnout signals); team energy Phase-2+; agent compute-cycles as energy proxy.
5. **Credits** — Anthropic tokens (Max-sub turn-count) + Groq credits (voice-only, scoped) + future paid accounts. audio_510 explicit concern.

### D11 Investment-fund philosophy Day 1

*«Jetix оперирует как resource-allocation engine с самого начала — каждое распределение времени, внимания и денег рассматривается как investment decision с ожидаемым ROI»* [src:decisions/JETIX-VISION.md#3]. Operating philosophy, not product; even without formal fund-structure философия работает. Phase 2+ may formalize actual fund.

### Agent resource reporting

Each cell return packet has `ap_cost` + `ap_budget`; brigadier aggregates; currently manual in strategies.md, planned dashboard Phase-2. Budget alerts = brigadier §6 budget-overrun → HITL escalation trigger.

### Boundaries

**In-scope:** tracking/allocation mechanisms for 5 resources; aggregation logic; dashboard design.
**Out-of-scope:** per-decision content → respective layers; Ruslan's life-OS wellness tracking → L-P (though overlap with energy); product revenue targets → L6.

### Interfaces — CROSS-CUTTING

Every layer consumes resources + reports to L-R; writes to L9 when budget-overrun triggers gate.

### Current status 2026-04-24

| Resource | Tracked | Dashboard | Alerts |
|---|---|---|---|
| Time | WBS per-cycle declared | No | No |
| Attention | Max-20 §1d enforced | No | No |
| Finances | €0 Phase-0; ~$5K bank manual | No | No |
| Energy | life-coach legacy + self | No | No |
| Credits | Max-sub + Groq voice-only | No | No |

### Evolution through 5 gates

| Resource | G1 €50K | G2 €200K | G3 €1M | G4 $100M | G5 $1T |
|---|---|---|---|---|---|
| Time | Manual budget | Per-agent dashboard | Per-roy P&L | Multi-roy portfolio | Civilizational |
| Attention | 20-task cap | Visual dashboard | Team attention budget | Alliance attention markets | Auction? |
| Finances | Bank statement | First alerts | Kelly-sized | Multi-roy portfolio | Token accounting |
| Energy | Self-monitor | Auto-track prototype | Team-wide | Alliance-wide | Global infra load |
| Credits | Max-sub only | Multi-provider accounting | Per-project credits | Own-compute shift | Jetix issues credits |

### Systems-mode: dominant leverage point

**OPP-01 ap_cost instrumentation** (Meadows L6 information-flow gap): single highest-leverage intervention. All 5 resources suffer same root gap — no measurement substrate. Once OPP-01 closes this gap, reinforcing loops activate simultaneously. Purely information-flow intervention; per Meadows L6 stronger than parameters, weaker than feedback polarity.

### Voice-memo references

- **audio_449** — Anthropic compute utilization tracking
- **audio_510** — tokens concern
- **audio_413** / **audio_428** — rest/burnout/tracking

### Open questions

1. **Dashboard trigger** — G1 (immediate) or G2 (proven need)?
2. **ap_cost drift** — lookup in strategies.md shows 30-50% under-estimation Phase 2. OPP-01 auto-instrumentation?
3. **Energy-tracking mechanism** — life-coach expansion or dedicated agent?
4. **Credits-tracking multi-provider Phase-2**.

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L-R-resource.md`.

---

## §L-C Compute & Infrastructure (cross-cutting)

### Mission

Hardware capacity + infrastructure for Jetix own-compute evolution + client-private-inference capability (STRATEGIC-INSIGHT local-first positioning) + Phase-3+ own power-generation per audio_526.

### What lives here

- **Own compute** — servers, GPUs for distilled local LLMs. Currently: single primary workstation (Linux 6.8.0-90-generic). SSH access. ulimit 65535 set permanently per master-plan R-1.
- **Client-private inference stack** — ollama + Mistral 7B Q4_K_M (Apache 2.0, cleanest license per KM-ARCH investor-optimizer convergence) default; Llama 3.1-8B pending DACH golden-set eval. Enables UC-10 offline-first per STRATEGIC-INSIGHT.
- **External dependencies current** — Anthropic Console (Max-sub turn-count per §9) + Groq (voice-pipeline scoped) + GitHub remote. NO third-party LLM APIs per §9.
- **Future Jetix-owned infra per audio_526** — own servers Phase-2+; own data-center Phase-3; own power-generation Phase-3+ ("собственную вычислительную инфраструктуру — hardware и электростанции").

### Boundaries

**In-scope:** hardware + infra + local-inference-stack + ulimit/ops-discipline.
**Out-of-scope:** git-repo-structure → L0; knowledge-content → L1; agent-definitions → L4; finance-to-buy-infra → L-R.

### Interfaces — CROSS-CUTTING

L0 runs on L-C; L1 storage on L-C disk; L2 transcription compute on L-C; L3 agent compute on L-C. Reads from L-R for budget authorization; writes to L9 when capacity-overrun.

### Current status 2026-04-24

- 1 primary workstation + ulimit 65535
- No GPU
- No own data-center
- External: Anthropic (Max-sub) + Groq (voice) + GitHub
- Ollama + Mistral NOT deployed yet

### Evolution path

- **Phase-1 (€0-€50K):** workstation + Max-sub; deploy ollama+Mistral when first Phase-2 client requires UC-10
- **Phase-2 (€200K-€1M):** GPU for client-private inference; first dedicated server (€3K+€15K/yr Path B per STRATEGIC-INSIGHT); EU-sovereign cloud for clients
- **Phase-3 (€1M-$100M):** data-center start; multi-region; redundant compute per D21 holding-structure
- **Phase-3+ ($100M-$1T):** civilizational-infra per audio_526 verbatim

### Voice-memo references

- **audio_526 verbatim:** *«собственную вычислительную инфраструктуру — hardware и электростанции»* — Phase-3+ civilizational target
- STRATEGIC-INSIGHT §6: missing infra items (ollama+Mistral, GPU, EU-data-center)

### Open questions

1. **Ollama+Mistral deployment trigger** — first paying UC-10 client or proactive sales-asset?
2. **GPU class Phase-2** — consumer RTX 4090 vs data-center A100?
3. **EU data-center provider Phase-2** — Hetzner vs AWS Frankfurt vs OVH?
4. **Groq long-term** — keep voice-scoped or migrate to local Whisper when Phase-2 GPU available?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L-C-compute.md`.

---

## §L-B Brand & Narrative (cross-cutting)

### Mission

Brand + narrative layer: how Jetix is messaged externally + internally. Tagline / metaphors / audience-segmentation / document-compass. Distinct from L5 (product portfolio) + L6 (business execution).

### What lives here

- **Tagline** per JETIX-VISION §1: *«Jetix — методология превращения AI-рычага в mass-scale cooperation и personal sovereignty»*
- **USB-C metaphor** per D20 + D25-D28 reinforcement VERBATIM: *«настолько будет технология просто Jetix распространена и мощная что её будут использовать все как раньше использовали прошивку Windows блять для любого компьютера»*
- **Прошивка Windows metaphor** per chat-voice-USB-C — Jetix as infrastructure-that-any-AI-augmented-business-runs-on
- **Operating system мирового масштаба** per audio_528
- **Smart AI internal label** per D25-D28 addendum — marker, not lock; internal discussions may use, official positioning stays Jetix
- **3-audience landing pages** per audio_507 — авантюристы / инвесторы / работники мечты (self-filtering entry points)
- **Document-compass 5-15 pages** per audio_527 — ~5-15 page distillation guiding newcomers through Jetix; derives from SYSTEM-OVERVIEW once landed (TODO-468)
- **Layered identity grammar** per D8 — gentleman-inside / predator-outside / per-archetype-angles; context-adaptive messaging
- **Enterprise-fast positioning** per chat-voice + audio_510 — "не One Person Company, не slow-corporate, enterprise-fast"

### Boundaries

**In-scope:** messaging + metaphors + landing-pages + compass + per-audience framing.
**Out-of-scope:** product-offer-detail → L5; ICP-qualification → L6; Alliance-community-mechanics → L8; per-archetype per-direction deep-copy → Phase-3 strategy docs.

### Interfaces

**Reads from:** L5 products-to-message + L6 ICP-targeting + L8 audience-segments.
**Writes to:** L5 product-taglines + L6 outreach-copy + L8 landing-pages.
**Invokes:** L9 governance for major positioning shifts.

### Current status 2026-04-24

- 1 landing-page draft (unbuilt)
- Voice-2 chat-USB-C as first sales asset per Ruslan explicit directive "буду это голосовое клиентам скидывать"
- Tagline documented in JETIX-VISION
- Document-compass NOT written (TODO-468; depends on SYSTEM-OVERVIEW approval)
- 3-audience landing pages NOT built
- Smart AI used internally, Jetix officially

### Evolution path

- **Phase-1 (€0-€50K):** launch 1 primary landing (авантюристы entry) + compass 5-15 pages + USB-C voice-pitch as Phase-1 sales asset
- **Phase-1 mid:** 3-audience landings live
- **Phase-2 (€200K+):** Mittelstand/DACH-specific messaging per STRATEGIC-INSIGHT §3; German-language materials
- **Phase-3 (€1M+):** USB-C positioning public + standards-body press presence
- **Phase-3+ ($100M+):** civilizational-level narrative per D19 + $1T trajectory

### Preserved dissent (L-B brand)

**Civilizational framing ($1T / USB-C) vs Phase-1 Startupper with €5K budget.** Resolved via D8 layered identity — самофильтрация работает как мембрана; empirical test on first 5 sales calls.

### Voice-memo references

- **audio_507** landing + 3 audiences
- **audio_527** document-compass
- **audio_528** OS мирового масштаба
- chat-voice-USB-C verbatim sales asset

### Open questions

1. **Smart AI → D29 official product name** or stay internal per current status?
2. **Which audience gets Phase-1 primary landing** — авантюристы per JETIX-VISION §7 *«самая большая авантюра»* or инвесторы?
3. **Document-compass lead-authorship** — brigadier integration or Ruslan-manual?
4. **German-language start trigger** — G1 or G2?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L-B-brand.md`.

---

## §L-P Life OS (personal cross-cutting)

### Mission

Personal cross-cutting layer: Ruslan's personal system within Jetix. Life-OS as EXPLICITLY part of Jetix per audio_517: *«описать конкретные части системы под запуски бизнесов и коммуникации с людьми»*. Not a separate thing, but aspect of Jetix system.

### Why L-P is a LAYER (cross-cutting) not a PROJECT

Per philosophy-integrator three Popper-falsifiable tests:
1. **Simultaneous multi-domain input:** Ruslan's energy fuels L0-L9 all layers; if L-P were a project, it would have completion state, but Ruslan's life doesn't.
2. **No completion state:** unlike a project, L-P is continuously active substrate.
3. **Degradation propagation:** when L-P degrades (Ruslan burnout), all layers degrade simultaneously — signature of substrate, not project.

### What lives here

- **Ruslan personal wellness** — sleep / nutrition / training / recovery; life-coach agent
- **Productivity** — day-planning / session-structure / /plan-day /close-day skills; personal-assistant agent
- **Finance** — personal cashflow (distinct from Jetix revenue L6); bank balance; burn runway ($5K Phase-0)
- **Bank of Ideas** — Notion Банк идей `bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7`; ideas pipeline into ingest
- **Life OS Notion page** — `3322496333bf8184b31bc985a93222d7`
- **Auto-logging жизни** per audio_518 — systematic tracking of life-events (sleep, meals, training, mood, focus); not yet automated — manual Notion entries + voice-memo stream
- **life-os P3 project** per CLAUDE.md — P3 priority Active status
- **Daily Log DB Notion** `30a24963-33bf-8005-817a-000beb10bcd4`

### Boundaries

**In-scope:** Ruslan's personal life as sub-system within Jetix + personal-agents + personal-data-stores.
**Out-of-scope:** Jetix business-agents → L4; Jetix business-revenue → L6; ICP/community → L8; brand-messaging → L-B.

### Interfaces

**Reads from:** L4 life-coach + PA agents + L1 personal-wiki slice + L-R energy/time resource-tracking.
**Writes to:** L-R resource consumption (Ruslan's hours/energy); L2 voice-memos ingest.
**Invokes:** L9 governance when personal-OS architecture changes affect Jetix-OS at large.

### Current status 2026-04-24

- life-coach + PA agents exist as legacy
- Notion Life OS page exists (not fully integrated with swarm/wiki/)
- Bank of Ideas manually populated via voice-memo pipeline
- Auto-logging NOT built — manual Ruslan entries
- life-os P3 project Active; engineering-thinking sibling P3

### Evolution path

- **Phase-1 (€0-€50K):** continue manual logging; life-coach + PA agents serve Ruslan only; refinement of /plan-day /close-day
- **Phase-1 mid:** auto-logging layer first prototype (sleep tracker → voice-transcribe → wiki)
- **Phase-2 (€200K-€1M):** systematic auto-logging; personal-OS stable
- **Phase-3 (€1M-$100M):** per audio_529 explicit — "миллионеры $1M+/year" are Jetix buyer segment — Jetix SELLS life-OS-for-millionaires as Phase-3 product (NOT Phase-1); Ruslan's life-OS is prototype + sales reference
- **Phase-3+:** externalized life-OS is a product-line (see L5)

### Voice-memo references

- **audio_517 verbatim:** *«описать конкретные части системы под запуски бизнесов и коммуникации с людьми»* — primary justification for L-P as layer
- **audio_518** — auto-logging
- **audio_525** — life-OS context
- **audio_529** — life-OS for millionaires Phase-3 product

### Preserved dissent

**life-os = project (CLAUDE.md P3) vs layer (this doc):** not contradictory at different abstraction levels. Life-os project lives INSIDE L-P layer; both framings preserved.

### Open questions

1. **Auto-logging mechanism design** — voice-transcribe extension or separate tool?
2. **Life-OS-as-Jetix-product timing** — Phase-2 pilot with millionaires-ICP-subset per audio_529 or Phase-3 scaled?
3. **Notion Life OS integration with swarm/wiki/** — bi-directional sync or one-way export?
4. **Personal-agents boundaries with swarm agents** — who routes between them?

**Подробнее** — `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L-P-life-os.md`.

---

═══════════════════════════════════════════════════════════════════════════════

**END 14 LAYER SECTIONS. POST-LAYER §L+1..§L+4 FOLLOW.**

═══════════════════════════════════════════════════════════════════════════════

## §L+1 Open strategic questions (consolidated from per-layer)

Top 10 questions Ruslan должен решить до Phase 2 layer deep-dives:

1. **USB-C / McKinsey resolution (§6)** — ack brigadier's proposed resolution as-is (Option A) or modify/reject?
2. **Smart AI status** — D29 formal lock (product name) or stay internal marker per D25-D28 addendum?
3. **Миллионер $1M+/year ICP-tier** — hard gate or aspirational frame? audio_470 calls $20-50K/month the real target — reconcile.
4. **Path A/B/C Phase-1 pricing** per STRATEGIC-INSIGHT §5 — Jetix-hosted / Client-hosted / Hybrid (capital profile differs)?
5. **D27 fork-and-merge governance** — BDFL (Ruslan) / committee / meritocracy? Licensing (MIT / proprietary / dual)?
6. **Mittelstand AI Alliance formalization timing** — Phase-1 informal (STRATEGIC-INSIGHT §3 speed imperative) vs Phase-2 formal (D15 revenue-gated)?
7. **Client-isolation architecture Phase-1** — Path-B self-hosted or Path-C hybrid (requires investor-expert capital judgment per L1 peer-input-needed)?
8. **Ollama+Mistral deployment trigger** — first paying UC-10 client or proactive sales-asset?
9. **Legacy-14 agents fate** — migrate to ROY / retire / coexist? Timing? CLAUDE.md Agent Roster reconcile (lists 12 but actual 20)?
10. **Beta-first / не даунгрейдить policy formalization** — write-up as operational policy or canonicalize as Lock?

---

## §L+2 Gaps that require new M-tasks

1. **Phase 2 per-layer deep-dives** — 14 M-tasks (one per layer) to flesh out implementation of each layer (LAYER-0-FOUNDATION-DEEP-DIVE.md, LAYER-1-KNOWLEDGE-DEEP-DIVE.md, ...). Master-plan §4 Phase-2 scheduled.
2. **D27 fork-and-merge governance document** — how canonical upstream maintained; merge-back protocol; licensing choice.
3. **Beta-first policy canonicalization** — operational discipline currently unwritten.
4. **Mittelstand AI Alliance formalization document** — legal structure, membership criteria, governance.
5. **L-R Resource dashboard design M-task** — to implement OPP-01 ap_cost instrumentation + per-resource visualization.
6. **Client-isolation architecture implementation M-task** — Path-B vs Path-C concrete (after L1 deep-dive).
7. **Smart AI D29 decision** — lock or stay internal (Phase 0.3 decision, may need additional inputs).
8. **USB-C / McKinsey resolution ack formalization** — if Ruslan acks §6 Option A, promote into canonical foundation.

---

## §L+3 Recommended next 3 M-tasks after SYSTEM-OVERVIEW approved

1. **L6 Community Deep-Dive → ICP Trinity consolidation** — 13 TODO items про ICP fragmented across files; unblocks outreach. Priority: **highest** (blocks Phase-4 execution).
2. **L4 Product Deep-Dive → consulting-DACH / producer-center / Secure Network strategies** — unblocks Phase 3 strategic docs + Phase 4 sales.
3. **Sales Methodology Research cycle** — parallel research cycle; unblocks outreach kickoff.

Per MASTER-PLAN §4 Phase-2 order: L6 Community → L4 Product → L5 Business → L7 Trajectory → L2 + L3 (internal, already partially specified). Phase-3 strategic docs follow.

---

## §L+4 How Ruslan uses this doc

**Daily:** open §0 TL;DR when context switch; scan §L+3 recommended-next to confirm work matches plan.

**Weekly:** §3 28-Locks-table scan to ensure no decision contradicts an existing Lock; §L+1 open questions review.

**Monthly:** §4 system-diagram revisit — any new layers emerged? Any boundaries shifted?

**Per new direction/strategic decision:** reference relevant §L? to see which layer the decision primarily lives in; cross-check §3 Locks for binding constraints; surface to L9 governance if contradiction.

**Per swarm cycle launch:** brigadier reads this doc as master-context; cell briefs reference §L? for layer-specific context; per-layer drafts (in `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-*`) provide authoritative detail.

**Update cadence:** minor updates (new Lock D29+, new audio_NNN evidence) via append-only status log. Major updates (new layer, boundary change) require new M-task cycle + HITL approval.

---

## Status log (append-only, newest first)

### 2026-04-24 23:45 CET — Ruslan ack received; brigadier compound + archive executed

- Ack: `state: acked, chosen: a1+b1+c1+d1` in `swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md` frontmatter
- 4 decisions accepted per brigadier recommendation (A1 USB-C resolution / B1 Smart AI internal / C1 $1M+ ICP as D22 refinement / D1 accept integration as-is)
- Document state: draft → accepted; binding for Phase 2 per-layer deep-dives + Phase 3 strategic docs
- C1 refinement per Ruslan notes: $1M+ ICP reads as enrichment of D22 qualitative filter (overlay on 11 archetypes per JETIX-VISION §7.1), NOT conflict. Reconciles L6 dissent.
- Per-expert improvements + emergent insights + cycle-log written per Phase-7/8
- No Full-Auto authorization downstream: each Phase 2 layer deep-dive is its own M-task with its own gate (Ruslan note)

### 2026-04-24 — Document created via swarm cycle cyc-jetix-system-overview-2026-04-24

- Brigadier orchestrated 14 layer-cells in 3 parallel waves (L0-L4, L5-L9, L-R/L-C/L-B/L-P)
- 14 layer drafts in `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-*` (authoritative detail per-layer)
- Philosophy × critic coherence review pending (Part F)
- State: draft-awaiting-ruslan-ack; gate packet `swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md`
- Word count: ~22000 (well within 15-25K target)
- 28 Locks referenced; D25-D28 integrated as primary layer constraints
- USB-C / McKinsey resolution §6 proposed — Option A (accept) recommended by brigadier
- Smart AI documented as internal label per D25-D28 addendum (NOT lock)

---

*End of JETIX-SYSTEM-OVERVIEW draft. Awaiting Ruslan ack on §6 USB-C/McKinsey resolution + overall document approval. On ack → Phase-7 compound + Phase-8 archive.*
