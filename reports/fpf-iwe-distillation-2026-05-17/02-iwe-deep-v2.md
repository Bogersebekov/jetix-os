---
title: IWE deep — Tseren FMT-exocortex-template + AI-guide gap + FPF dependency
date: 2026-05-17
phase: Phase B Шаг 2 (Phase A baseline 02-u-episteme-and-iwe.md 267 lines)
type: distillation
parent_prompt: prompts/fpf-iwe-phase-b-2026-05-17.md §2
corpus_snapshot:
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ (314 files, ver 0.31.0 @ 2026-05-17)
  - raw/external/ailev-FPF/FPF-Spec.md @ c86eabd 2026-05-16
F: F4
G: distillation-3
R: refuted_if_iwe_mis-encoded_OR_C5-decomposition_wrong_OR_template-vs-platform-conflated
prose_authored_by: brigadier-integrated (3 cells: knowledge-synth + engineering-expert × integrator + philosophy-expert × critic)
language: russian + english (verbatim where source-language)
audience: L1 (Anatoly Levenchuk, Tseren Tserenov) + Ruslan
cell_drafts:
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-knowledge-synth-iwe-collection.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-integrator-fmt-structure.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-iwe-verify.md
dissents_preserved: 4 (per AP-6 — see §10)
---

# IWE Цэрэна — deep collection v2

> **Constitutional posture.** Scribe-mode + structurer. Verbatim Tseren / Levenchuk
> где возможно. Surface'инг без оценки «лучше/хуже». F-G-R per non-trivial claim.
> Dissents preserved per AP-6, not averaged into consensus.

> **КРИТИЧНЫЙ DISSENT (top of doc — see §10 D-1).** «IWE» в Левенчуковском TG-message
> C5 likely refers to the **paid AI guide on aisystant.system-school.ru platform**,
> NOT the public `FMT-exocortex-template` GitHub repo. Phase B изучало template;
> платформенный AI guide остаётся blocked (B2 — Ruslan IWE subscription).
> Все findings ниже относятся к **template**, не к platform AI guide, если явно не сказано.

---

## §0 Freshness snapshot

| Параметр | Значение |
|---|---|
| Primary corpus | `github.com/TserenTserenov/FMT-exocortex-template` |
| Version | `0.31.0` released `2026-05-17` (today) |
| Repo type | `Base/Formats` (FMT) — template distribution |
| Files captured | 314 |
| Local path | `raw/external/tseren-github-2026-05-17/FMT-exocortex-template/` |
| Active staging | S-44 (Telegram reminders) promoted L1; S-45 (Agent Inbox) status: testing |
| Vendor-neutrality | knowledge stored Markdown/YAML/Git (open) + automation Claude Code CLI (vendor-locked) |
| Paid layer | Aisystant platform AI guide — **BLOCKED Phase B** (B2 blocker, см. blockers.md) |

---

## §1 IWE — verbatim definitions

> Канонический источник для определений — `ONTOLOGY.md` + `README.en.md` + `CLAUDE.md` template repo. Каждое определение — file:line attribution.

### §1.1 IWE — disambiguation FIRST

**Critical distinction (по `.claude/rules/distinctions.md`):**
> «**IWE = Intellectual Work Environment** (не «Intelligent», не «Working»). Аналогия: IDE.»

`F: F8 | G: tseren-canonical | R: R-high`

«**I**» = **Intellectual**, NOT «Intelligent». Аналогия: IDE для кода → IWE для мышления.

**Primary positioning (`README.en.md:7-9`, verbatim):**
> «An operating system for intellectual work. Your knowledge. Your experience. Your environment — runs on top of any AI platform.»
>
> **Repository type:** `Base/Formats` (FMT) — template distribution. After forking, it becomes your personal environment with AI agents.

**Marketing analogy (`README.en.md:31-32`):**
> «Just as an IDE combines editor, compiler, and debugger into one environment for a programmer — IWE combines knowledge, planning, and AI agents into one environment for thinking.»

### §1.2 Core IWE terms — verbatim

| Термин | Verbatim definition | Source |
|---|---|---|
| **Exocortex** | «Your external memory — files with plans, context, conclusions that Claude reads in every session» | `README.en.md:48` |
| **Pack** | «Formalized knowledge base for your domain — the single source-of-truth for domain knowledge» | `README.en.md:48` |
| **OWC** | «Open → Work → Close — a ritual for every session and every day, prevents context loss» | `README.en.md:48` |
| **ArchGate** | «Structured evaluation of architectural decisions across 7 characteristics (instead of 'I think it's fine')» | `README.en.md:48` |
| **Strategist** | «AI agent that automatically creates daily/weekly plans and tracks progress» | `README.en.md:48` |
| **FMT** | «Base/Formats (FMT) — template distribution. After forking, it becomes your personal environment» | `README.en.md:9` |
| **ZP** | Zero Principles — top of fallback chain `DS → Pack → SPF → FPF → ZP` | `CLAUDE.md §1` |
| **FPF** | «Фреймворк первых принципов» (First Principles Framework) — Base tier | `ONTOLOGY.md §4 abbr` |
| **SPF** | Second-level Principles Framework — derived from FPF, above Pack | `CLAUDE.md §1` |
| **Pack** | «Pack = source-of-truth для доменного знания. DS меняется вслед за Pack.» | `CLAUDE.md §1` |
| **DS** | Domain Specific (instrument/governance/surface) — production tier | `CLAUDE.md §1` |
| **AR** | Agent Rules (`AR.NNN.md` schema in PACK-agent-rules) | `CLAUDE.md §2` |
| **WP** | Рабочий продукт — work product unit (artefact + lifecycle) | `CLAUDE.md §2` |
| **ОРЗ** | Открытие → Работа → Закрытие = Open → Work → Close fractal | `CLAUDE.md §2` |
| **ЭМОГССБ** | 7 архитектурные характеристики ArchGate (Эластичность, Модульность…) | `archgate skill` |

### §1.3 Что IWE НЕ есть (anti-definitions, verbatim)

`README.en.md:219-220 FAQ Q:` «Obsidian is a note storage. IWE is a **work environment** with protocols, AI agents, and knowledge formalization.»

`README.en.md:41` (key principle, verbatim):
> «**Key principle: exoskeleton, not prosthesis.** IWE amplifies your thinking, not replaces it. After each session you become more competent, not just get a result.»

> **Test for exoskeleton vs автопилот** (`.claude/rules/distinctions.md`):
> «Тест: можешь объяснить без «ИИ подсказал»?»

`F: F6 | G: tseren-canonical | R: R-medium (positioning claim; falsifier defined as "test" but no published comparative benchmark)`

---

## §2 IWE = production-applied FPF — структурная dependency

> **Левенчуковский C5 claim** `[inbox/levenchuk-tg-2026-05-17.md:28]`:
> «У Церена IWE, там примерно всё так же устроено. Но внутри там интеллект опирается
> на тот же FPF — и понятно, за счёт чего его IWE умнее конкурентов.»

### §2.1 Decomposition of C5 (phil × critic finding 2)

C5 — composite claim из двух частей:

| Sub-claim | Что | F-G-R | Verified? |
|---|---|---|---|
| **C5a** | «Внутри [IWE] интеллект опирается на FPF» (structural FPF dependency) | F5 / structural / R-medium-to-high | **VERIFIED** from CLAUDE.md Fallback Chain + memory/fpf-reference.md presence |
| **C5b** | «IWE умнее конкурентов» (comparative intelligence advantage) | F2 / positioning / R-low | **NOT VERIFIABLE** from public corpus; requires C4-style benchmark (Phase B blocked) |

`F: F4 | G: jetix-synthesis | R: refuted_if_C5_re-stated_as_unitary_by_Левенчук`

**Implication.** Merging C5a + C5b as one statement = AP-PHIL-1 (epistemic conflation). Brigadier preserves them separately.

### §2.2 Verbatim evidence — FPF as IWE Base tier (CLAUDE.md §1 — template's own root spec)

> «| Тип | Что содержит | Первоисточник |
> |-----|-------------|---------------|
> | **Base** (Принципы + Форматы) | ZP, FPF, SPF, FMT-* | Да (платформа) |
> | **Pack** | Паспорт предметной области | Да (пользователь) |
> | **DS** (instrument/governance/surface) | Код, планы, курсы | Нет (производное от Pack) |
>
> **Fallback Chain:** DS → Pack → Base (SPF → FPF → ZP)
> **Pack = source-of-truth для доменного знания. DS меняется вслед за Pack.**»

`[raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md §1]`
`F: F8 | G: tseren-canonical | R: R-high (template's own root spec)`

### §2.3 Generative hierarchy (NOT only fallback) — knowledge-synth §5

5-level hierarchy is **both** a fallback chain AND a generative hierarchy. Upper levels generate / constrain lower levels.

```
ZP   ← Zero Principles (transdisciplines, top)
 ↓ generates / constrains
FPF  ← First Principles Framework (Levenchuk canonical)
 ↓
SPF  ← Second-level Principles Framework (Tseren-led)
 ↓
FMT  ← Formats (this template repo = exocortex template)
 ↓
Pack ← Domain knowledge passport (user-authored per-domain)
 ↓
DS   ← Domain-specific artifacts (code, plans, governance)
```

`F: F5 | G: tseren-canonical | R: R-high (explicit in CLAUDE.md + docs/principles-vs-skills.md)`

**docs/principles-vs-skills.md:L17 verbatim:**
> «Level 1: FPF | Первые принципы (рамка корректности) | Точный язык: Role ≠ Method ≠ Work ≠ Capability»

This confirms **FPF A.7 (Role-Method-Work-Capability)** is declared as the «central organizing principle» of IWE.

### §2.4 FPF reference inside template

`memory/fpf-reference.md` exists in template as a navigation guide.
`docs/LEARNING-PATH.md L50 verbatim:`
> «Центральный организующий принцип — триада FPF A.7: Роль → Метод → Рабочий продукт»

`F: F6 | G: tseren-canonical | R: R-medium`

**Engineering note (eng × integrator):** `memory/fpf-reference.md` is at *template* level (not Pack level). This means **every** IWE instance ships with FPF navigation pre-loaded; users do not need to install FPF separately.

### §2.5 Mapping FPF mechanisms → IWE constructs (knowledge-synth §2)

| FPF mechanism | IWE construct | F-G-R |
|---|---|---|
| A.1.1 U.BoundedContext | Pack as domain-specific bounded context | F5 / mapped / R-medium |
| A.2 Role Taxonomy | 5 roles (R1 Strategist / R2 Extractor / R8 Synchronizer / R23 Verifier / R24 Auditor) | F6 / mapped / R-high |
| A.3 / A.15 Method-Work quartet | WP (work product) lifecycle: открытие → работа → закрытие | F6 / mapped / R-high |
| A.6.B Claim Register | (NOT directly mapped — uses ad-hoc Memory + ArchGate) | F3 / gap / R-medium |
| A.6.P Compression-Decompression | Memory horizons (HOT/WARM/COLD/ARCHIVE) — implicit | F3 / partial / R-low |
| A.14 Advanced Mereology | 3-tier repo hierarchy (Base/Pack/DS) — surface mapping | F4 / mapped / R-medium |
| B.3 F-G-R Trust | NOT explicitly used (Memory + WP context replace it informally) | F2 / gap / R-low |
| B.5 Reasoning Cycle | OWC fractal at 4 scales + WP Gate | F5 / mapped / R-medium |
| C.17-C.19 NQD/E-E-LOG | NOT visible in template — likely in paid AI guide layer | F2 / unknown / R-low |
| E.9 DRR Design Rationale | WP-context files + Strategy session ritual | F5 / mapped / R-medium |
| E.17 MVPK Multi-View Publication | Service Clauses (DP.SC.NNN) + per-role views | F4 / partial / R-medium |
| C.2.1 U.EpistemeSlotGraph | NOT named or enforced — used implicitly | F2 / gap / R-low |

> **Phil × critic Finding 3:** «U.Episteme is **used but not named**». Pack/Exocortex функционально similar to U.Episteme aggregations, но primitive не declared.

`F: F4 | G: jetix-synthesis | R: refuted_if_mapping_disputed_by_Tseren`

---

## §3 IWE intelligence amplification workflow — OWC fractal

> Per `README.en.md §Work Culture` + `CLAUDE.md §2`.

### §3.1 ОРЗ (Open → Work → Close) at 4 scales (verbatim CLAUDE.md §2)

| Масштаб | Открытие | Работа | Закрытие |
|---------|----------|--------|----------|
| **Сессия** | `protocol-open.md § Сессия` (любое задание) | `protocol-work.md` | `/run-protocol close` |
| **День** | `/day-open` («открывай») | Между Day Open и Day Close | `/run-protocol day-close` |
| **Неделя** | — | — | `/run-protocol week-close` |
| **Месяц** | — | Между Month Close предыдущего и текущего | `/month-close` (первый Пн месяца) |

`F: F8 | G: tseren-canonical | R: R-high (operational, CI-tested)`

«Пропуск Открытия = незапланированная работа. Пропуск Закрытия = незафиксированный результат.»

### §3.2 WP Gate — БЛОКИРУЮЩЕЕ правило (CLAUDE.md §2 п.1)

> «**WP Gate:** ЛЮБОЕ задание → протокол Открытия → ДО начала работы.»

Ритуал согласования (горячий, не lazy):
- Шаг 1. Объявить: Роль пользователя · Роль Claude · Работа · РП (артефакт) · Класс верификации · Метод · Оценка ~Xh · Модель.
- Шаг 2. Дождаться согласования. Без явного «да» — НЕ регистрировать РП в 4 местах.
- Шаг 3-4. Детали → `memory/protocol-open.md`.

**4 places РП регистрируется** (S-14 promoted L1):
1. `REGISTRY.md` (WP-REGISTRY)
2. `WeekPlan W{N} YYYY-MM-DD.md`
3. `context/<WP-NNN>.md`
4. External tracker (Linear / similar)

`F: F8 | G: tseren-canonical | R: R-high (operational, S-14 promoted)`

### §3.3 ArchGate — 7-factor architectural decision

> «**АрхГейт** → `/archgate` → принципы (DP.ARCH.001 §7) → профиль **ЭМОГССБ** (✅/⚠️/❌) → conjunctive screening.»

`[CLAUDE.md §5]`

ЭМОГССБ = 7 архитектурных характеристик. Per `archgate skill description`:
> «Оценка архитектурного решения по 7 характеристикам ЭМОГССБ (v3 — профиль без агрегатного балла, conjunctive screening).»

`F: F6 | G: tseren-canonical | R: R-high`

> **Чеклист современности:** (1) Context Engineering SOTA.002, (2) DDD Strategic SOTA.001, (3) Coupling Model SOTA.011.

### §3.4 IntegrationGate — БЛОКИРУЮЩЕЕ при новых инструментах (CLAUDE.md §2)

При проектировании нового инструмента/агента/системы — строгая последовательность 4 фаз:
1. **Обещание** (Service Clause `DP.SC.NNN`)
2. **Сценарии** (≥3 разных потребителя)
3. **Роль** (`DP.ROLE.NNN`)
4. **Реализация**

«Прыжок сразу в реализацию = P10 (DP.FM.010).»

`F: F6 | G: tseren-canonical | R: R-medium`

### §3.5 Pre-action Gates table (CLAUDE.md §2)

| Момент | Проверка |
|--------|---------|
| Начало работы | Какие сервисы (MAP.002) затронуты? |
| Пользовательский сценарий | **SC Gate:** какое обещание (08-service-clauses/) затронуто? |
| Создание/размещение артефакта | **Routing Gate:** DP.KR.001 §5 (PACK-digital-platform) карта маршрутизации |
| Первое содержательное действие в репо | **Repo-Touch Gate:** прочитать `<repo>/CLAUDE.md` |
| Архитектурное решение | **АрхГейт** → `/archgate` |
| РП PII | **Security Gate (B7.3)** |
| РП ≥3h | **Priority Gate** |
| Новый инструмент | **IntegrationGate** |
| Legacy migration | **LegacyPortGate** |

`F: F6 | G: tseren-canonical | R: R-medium`

---

## §4 IWE Role Taxonomy — 5 agent roles (engineering-integrator §4)

| Role | Role-ID | Implementation | Function |
|---|---|---|---|
| **R1 Strategist** | agential | Claude (Sonnet) | Daily/weekly plan generation, Strategy session prep |
| **R2 Extractor** | agential | Claude (Sonnet) — HITL on all writes | Knowledge extraction from sessions, capture-to-Pack |
| **R8 Synchronizer** | non-agential bash | OS scheduler (launchd / cron / WSL) | Cross-repo sync, OS-level orchestration |
| **R23 Verifier** | agential | Claude **Haiku** (context isolation) | Checklist verification (Quick Close, Day Close) |
| **R24 Auditor** | agential | Claude (cross-context) | Security audit (Day cadence + Month deep) |

`F: F6 | G: tseren-canonical | R: R-medium (5 roles read directly from roles/*/README.md)`

> **Engineering observation (eng × integrator §4):** R8 is the OS-scheduler orchestrator (bash, NOT LLM). This is analogous to Jetix brigadier's dispatch role but implemented as scheduled bash, not as an LLM orchestrator. Different reliability profile.

### §4.1 Roles ≠ Skills ≠ Protocols (verbatim distinctions.md)

> «**Скилл ≠ Роль ≠ Протокол.** Точечное действие / контекст сессии / ритуал ОРЗ.»

This three-way distinction is operational: brigadier (Jetix) and Tseren agree on Role≠Executor; Tseren additionally distinguishes Role vs Skill vs Protocol along *granularity* axis.

---

## §5 Memory lifecycle (S-35) + Extensions Gate

### §5.1 Memory lifecycle (CLAUDE.md §9 + memory-lifecycle-spec.md)

Mandatory frontmatter for `memory/*.md`:
```yaml
---
name: "..."
description: "одна строка для MEMORY.md"
type: user | feedback | project | reference | lesson | protocol
horizon: hot | warm | cold | archive
domains: [...]
status: active | dormant | superseded | archived
valid_from: YYYY-MM-DD
owner: user | platform
schema_version: 1
---
```

Horizon rules:
- **HOT** — загружается каждую сессию. ≤150 lines (cumulative).
- **WARM** — по триггеру. Default для `project`, `reference`, `lesson`, `protocol`.
- **COLD/ARCHIVE** — time-based demotion.

**Archival cadence (proposed by agent, not autonomous):**
- HOT→WARM: 14 days без обращения
- WARM→COLD: 30 days
- COLD→archive: 90 days

`F: F6 | G: tseren-canonical | R: R-high (S-35 WP-217 Ф10.1, ArchGate 2026-04-30)`

### §5.2 Extensions Gate — БЛОКИРУЮЩЕЕ (CLAUDE.md §9)

> «**Для пользователей:** кастомизация протоколов/скиллов → ТОЛЬКО в `extensions/*.md`.
> Прямое редактирование `.claude/skills/` или `memory/protocol-*.md` = ошибка.»

3-layer architecture:
- **L1** (platform): `update.sh` overwrites
- **L2** (staging): `STAGING.md` register для обкатки `S-NN` (status: testing → validated → promoted)
- **L3** (author-only): `params.yaml: author_mode: true` permits L1 edits

`F: F6 | G: tseren-canonical | R: R-high`

### §5.3 Hooks/Scripts Bypass Gate (CLAUDE.md §2 п.6 — S-33 promoted L1)

> «Без явного разрешения пользователя НЕ менять скрипты шаблона и НЕ обходить хуки никаким способом.»

Enforcement: `extensions-gate.sh` PreToolUse hook blocks direct L1 writes.

`F: F8 | G: tseren-canonical | R: R-high (CI-verified)`

---

## §6 Update mechanism — HTTP manifest fetch + 3-way merge

Engineering-integrator §7:
- `update.sh` runs HTTP manifest fetch (no shared git history with user instance)
- 3-way merge preserves `extensions/`, `params.yaml`, `CLAUDE.md §8-§9` (staging + author-only)
- CI matrix: ubuntu + macOS, 2 gov_repo variants, upgrade-flow regression test
- Self-updating `update.sh` (the script that fetches the new template can update itself)

`F: F6 | G: tseren-canonical | R: R-high`

**Jetix comparison.** Jetix has no template-distribution model. Each Jetix instance = a single git repo at owner's machine. This is intentional (single-owner pattern) but means Jetix cannot scale to N users without re-architecting.

---

## §7 MCP + skill surface

### §7.1 MCP servers

**One** declared MCP server in `.mcp.json`:
- `iwe-knowledge` @ `https://mcp.aisystant.com/mcp` (external HTTP, Aisystant-hosted)

Optional MCPs configured via `claude.ai/settings/connectors`: Google Drive, Railway, Linear (per CLAUDE.md AUTHOR-ONLY).

**Engineering Dissent D-eng-2 (preserved per AP-6).** `iwe-knowledge` single external HTTP MCP endpoint, no declared SLA. Single point of failure for knowledge navigation. Only `/fpf` skill has documented local fallback (loads `memory/fpf-reference.md`).

### §7.2 Observed skills (22 total in template)

From IWE template's loaded slash-commands set (read via the agent's own context):

| Skill | Purpose |
|---|---|
| `/day-open`, `/run-protocol close`, `/run-protocol day-close`, `/run-protocol week-close`, `/month-close` | OWC fractal triggers |
| `/wp-new`, `/pack-new`, `/personal-guide-start`, `/personal-guide-render` | Object creation |
| `/strategy-session`, `/think`, `/ke`, `/fpf`, `/archgate` | Reasoning + knowledge extraction |
| `/extend`, `/iwe-update`, `/audit-installation`, `/iwe-rules-review`, `/iwe-bug-report`, `/setup-wakatime` | Platform maintenance |
| `/apply-captures`, `/verify` | Capture review + verification |

`F: F6 | G: tseren-canonical | R: R-high (read directly from skill manifests)`

---

## §8 IWE vs FPF — what IWE adds, what IWE skips (knowledge-synth §4)

### §8.1 What IWE adds (11 constructs NOT in FPF Spec)

1. **Pack** — concrete domain-distribution format (vs FPF's abstract `U.Episteme` aggregations).
2. **OWC ritual at 4 scales** — concrete Open→Work→Close fractal (vs FPF's B.5 abstract reasoning cycle).
3. **ArchGate 7-factor checklist** (ЭМОГССБ) — concrete decision-evaluation tool (vs FPF's E.9 abstract DRR).
4. **Memory lifecycle (S-35)** — HOT/WARM/COLD/ARCHIVE horizons + 14/30/90 day demotion (vs FPF's no-memory-policy).
5. **Scheduling layer** — launchd / cron / WSL OS-level triggers (vs FPF's no-runtime-spec).
6. **Creative Pipeline** — note → draft → template → publication (vs FPF's mentions but no operational pipeline).
7. **Digital Twin** — runtime mirror of user's work state.
8. **Harness** — orchestration substrate for skill execution.
9. **4-contour system** — multi-perspective work tracking.
10. **WP Gate** — operational alpha-state lifecycle (registration ритуал).
11. **TTL** — time-to-live на artefacts (auto-archival + freshness signals).

### §8.2 What IWE skips / defers (6 FPF elements)

1. **Full U.Episteme slot graph** (4 slots: DescribedEntity / GroundingHolon / ClaimGraph / Viewpoint) — used implicitly via Pack but **not enforced as discipline**.
2. **CausalUse-CAL (C.28)** as blocking rule — referenced в `memory/fpf-reference.md` but no operational gate.
3. **D-Ethics** layer — not visible in template (may be in paid AI guide).
4. **E-Constitution** (Eleven Pillars) — not enforced as rule-set; principles imported via `/fpf` skill only.
5. **B.3 F-G-R Trust** per-claim tagging — Memory + WP-context replace it informally, not formal F-G-R schema.
6. **Multi-View Publication (E.17 MVPK)** — partial (Service Clauses) but not full viewpoint bundles.

`F: F4 | G: jetix-synthesis | R: refuted_if_Tseren_clarifies_paid-layer_includes_these`

---

## §9 Hard distinctions (verbatim, 13 рядов from `.claude/rules/distinctions.md`)

> Эти 13 distinctions — IWE-canonical «хард-различения». Каждый — 1-2 строки. Test для каждого definitive.

| Distinction | Test / Criterion |
|---|---|
| **IWE = Intellectual Work Environment** (не «Intelligent», не «Working») | Аналогия: IDE |
| **Развитие ≠ Образование** | Не использовать: «школа», «вуз», «студент», «преподаватель» |
| **Скилл ≠ Роль ≠ Протокол** | Точечное действие / контекст сессии / ритуал ОРЗ |
| **settings.json ≠ settings.local.json** | Проектный (hooks, git) vs персональный (permissions, .gitignore) |
| **Pack-знание ≠ Реализационное решение** (HD #29) | Доменная истина → Pack. Технический выбор → DS. |
| **OwnerIntegrity** | Один факт — одно место. Дублирование Pack↔DS = ошибка синхронизации. |
| **WP-context ≠ Результат работы** | Context в governance-репо, результат в целевом DS/Pack |
| **Персона ≠ Память ≠ Контекст** (HD #27, DP.D.050) | Critic: writer + owner. Git / Neon / runtime |
| **Проблема ≠ Задача ≠ ФР ≠ Работа** (HD #24, DP.D.053) | Ступор / метод известен / спецификация / физ.мир |
| **Система ≠ Роль** (D.141 PD) | Носитель существует независимо; роль = функциональное место, переносима |
| **Экзоскелет ≠ Автопилот** (DP.D.046) | Усиление мышления / LLM автономно. Тест: можешь объяснить без «ИИ подсказал»? |
| **Лог ≠ Инцидент ≠ State file** (DP.D.049) | Хронология у исполнителя / сбой+разбор в governance / снимок |
| **Скрипт ≠ Агент** (DP.D.048) | Фиксированный flow / LLM выбирает шаг. Тест: уберу LLM — сломается? |
| **strategy_day** | Из `day-rhythm-config.yaml`. В этот день: session-prep вместо day-plan, DayPlan не создаётся. |
| **Ru-first (SPF §5 п.13)** | Русский — основной язык. EN только для: YAML-ключей, аббревиатур, имён собственных. |
| **OAuth через бота**, не ручные ключи | Все интеграции — через OAuth. |
| **Проектировать роль агента в контексте**, не «проектировать агента» (DP.D.025) | |

`F: F6 | G: tseren-canonical | R: R-high (canonical .claude/rules/distinctions.md)`

---

## §10 Dissents preserved (per AP-6)

### D-1 (CRITICAL): Template ≠ Platform AI guide

| Position | Held by | F-G-R |
|---|---|---|
| Phase B изучало FMT-exocortex-template (public GitHub) | engineering-integrator + knowledge-synth | F6 |
| Левенчуковский TG C5 «IWE умнее конкурентов» likely refers to paid AI guide on aisystant platform — different artefact | philosophy-critic | F5 |
| **Reconciliation** | Both preserved; Phase B C4 benchmark requires paid IWE sessions (B2 blocker) to resolve | — |

> **Implication for L1 reply.** Когда говорим «изучили IWE» — точнее: «изучили public FMT-exocortex-template, ver 0.31.0; paid AI guide на aisystant остаётся blocker B2».

### D-2: FPF-operative vs FPF-background-only

| Position | Held by | F-G-R |
|---|---|---|
| FPF is operationally active в IWE at runtime (cited in agent guidance) | 02-u-episteme-and-iwe.md §3.1 (Phase A inference) | F4 |
| FPF is background architectural dependency, not active runtime discipline (per public artefacts only) | philosophy-critic | F4 |
| **Reconciliation** | Cannot resolve from public artefacts. Refuted if Phase B sessions show FPF cited in >20% of guidance responses; accepted if FPF not cited in 10+ session logs | — |

### D-eng-1: `dt-collect.sh` author-only credential code in public template

| F | G | R |
|---|---|---|
| F4 | engineering-internal | smell, not security risk |

Brigadier note: this is an engineering observation, not a Jetix-relevant policy concern.

### D-eng-2: Single external HTTP MCP endpoint, no SLA

| F | G | R |
|---|---|---|
| F4 | engineering-internal | single point of failure for knowledge navigation |

Only `/fpf` skill has documented local fallback.

---

## §11 Roadmap signals (knowledge-synth §7)

From `CHANGELOG.md` (1560 lines, read in full):
- **Version 0.31.0 released 2026-05-17** (today)
- **S-44 Telegram reminders** — recently promoted to L1 (platform default)
- **S-45 Agent Inbox** — status: **testing** (currently in L2 staging)
- **S-33 Hooks/Scripts Bypass Gate** — promoted to L1 платформенное правило
- **FPF reference file** (`memory/fpf-reference.md`) — currently stale vs upstream FPF (does NOT yet reference A.6.P + E.10.SEMIO additions @ c86eabd)

`F: F6 | G: tseren-canonical | R: R-high (CHANGELOG read directly)`

---

## §12 Commercial / community layer (knowledge-synth §8)

| Параметр | Значение |
|---|---|
| Claude pricing recommended | Pro ($20/мес) for minimal install; Max (~$100/мес) for unlimited |
| Knowledge format | Vendor-neutral (Markdown / YAML / Git) |
| Automation | Vendor-locked (Claude Code CLI; adaptable to Codex / Aider) |
| Community free | GitHub Discussions + Issues |
| Community premium (Telegram) | Entry via `@aist_me_bot`; per `README.en.md:240` |
| Community premium fee | Seminar entry ~5000₽ (per Tseren TG references; not verbatim in template) |
| Platform AI guide | Aisystant.system-school.ru paid subscription (B2 blocker) |

---

## §13 Phase B open questions (Ruslan-direction)

1. **B2 unblock decision** — Ruslan subscription to aisystant (per §0.0 ack «Aisystant subscription — Ruslan платит, доступы будут»). When credentials live, Phase C empirical IWE sessions can resolve D-1 + D-2.
2. **C4 benchmark Arm C scope** — verify «IWE» в C4 design references PLATFORM AI guide (not template). Otherwise Arm C = Arm A в disguise (vanilla Claude reading the template repo).
3. **Tseren collaboration channel** — if Tseren reviews this v2 doc, ask: (a) does §2.5 mapping (FPF mechanisms → IWE constructs) match his model? (b) §8.2 «what IWE skips» — what's actually skipped vs deferred-to-paid-layer?
4. **A.7 vs A.2 alignment** — Tseren names «A.7: Role → Method → Work-Product» as central. FPF Spec uses A.2 Role Taxonomy + A.3 Method + A.15 Role-Method-Work. Are A.7 and A.2+A.3+A.15 the same thing or different?

---

## §14 Mermaid diagrams (separate files)

> Phase B Шаг 2 acceptance criterion §2.3: 3 mermaid in `diagrams/`.

- `diagrams/13-iwe-fpf-mechanism-map.md` — what IWE imports from FPF (verified mapping)
- `diagrams/14-iwe-user-workflow.md` — IWE OWC fractal end-to-end UX (4 scales × O/W/C)
- `diagrams/15-iwe-vs-competitors.md` — what differentiates IWE (positioning vs Obsidian / Notion / Logseq + the «exoskeleton vs prosthesis» distinction)

(Diagrams written separately per Шаг 2 §2.3 — see `reports/fpf-iwe-distillation-2026-05-17/diagrams/`.)

---

## §15 What was NOT collected (gap registry)

- **Aisystant platform AI guide internals** — B2 blocker (paid subscription pending)
- **Tseren TG corpus 619 posts deep filter** for IWE-specific posts — not done Phase B (knowledge-synth focused on public template; deeper TG filter Phase C)
- **YouTube transcripts top-20** for IWE-tagged talks — IP-blocked per `blockers.md` B6
- **Levenchuk LJ posts referencing IWE** — searched references but not exhaustive
- **МИМ internal mentor materials** — closed (per blockers.md B8)
- **Conference talks INCOSE / OMG / SOTA** with Tseren or Levenchuk on IWE — not collected Phase B

Phase C remit (если Ruslan нужно).

---

*Distillation §2 complete. Integrated 3 cell drafts (knowledge-synth + eng × integrator + phil × critic) per brigadier §5.5.5 gate. 4 dissents preserved. Acceptance criterion: L1 reader extracts IWE surface + understands C5 decomposition (C5a structural-verified / C5b not-verifiable-public) за 30 минут.*
