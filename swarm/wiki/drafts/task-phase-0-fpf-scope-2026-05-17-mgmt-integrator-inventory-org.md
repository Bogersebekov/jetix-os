---
task_id: phase-0-fpf-scope-2026-05-17
produced_by: mgmt-expert × integrator
mode: integrator
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_functioning_vs_aspirational_not_distinguished_OR_org_entities_missed
date: 2026-05-17
sources:
  - CLAUDE.md
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-mgmt-integrator-jetix-vs-iwe.md
  - shared/state/active-projects.json
  - shared/state/system-health.json
  - comms/mailboxes/manager.jsonl
  - ls:.claude/agents/ (23 agent files enumerated)
  - ls:swarm/wiki/cycles/ (1 active cycle: cyc-foundation-build-2026-04-28)
  - ls:swarm/awaiting-approval/ (3 packets)
  - ls:outreach/ (6 files, most recent 2026-05-17)
  - ls:reports/review_*.md (11 voice-pipeline reviews, most recent 2026-05-14)
provenance_inline: true
---

# mgmt × integrator — Organizational Reality Inventory (Phase 0 FPF Scope)

> **Constitutional posture.** Scribe-mode per R1. Surface facts + organizational reality.
> No «следует» / «рекомендую». No evaluation «good/bad organization».
> Dissents preserved per AP-MGMT-11.

---

## §0 Summary

Через organizational-coherence lens Jetix Phase A выглядит как **two-layer system**:

**Layer A — operational substrate (functioning):** filesystem-as-SoT, voice pipeline,
CRM storage, wiki, git, shared state JSON, mailboxes, 23 agent definition files.
Этот слой реально работает каждый день. Evidence: 11 voice-pipeline review reports
(2026-04-15 → 2026-05-14); active commits; `shared/state/system-health.json` checked
2026-04-14; outreach files written 2026-05-17.

**Layer B — governance substrate (spec-locked, partially operational):** Foundation v1.0
(11 Parts + Pillar C), LOCKED 2026-04-28. Acked by Ruslan через 8 RUSLAN-ACK records.
Структурно присутствует: файлы существуют, F5 grade, git-tagged. Операционально:
маршрутизация, hub-and-spoke, AWAITING-APPROVAL механизм прописаны — но свидетельств
того, что они реально применяются в ежедневных решениях, недостаточно (JSONL mailboxes
содержат 4 записи все dated 2026-04-14, ни одной после; `shared/state/active-projects.json`
last_updated 2026-04-14; один активный cycle в `swarm/wiki/cycles/`).

**Layer C — strategic + vision documents (aspirational / in-flight):** Workshop / TRM /
Document 1A/1B / LOCKED Strategic Insights / Phase 1 plan. Написаны, locked. Но
коммерческая реализация (клиенты, договора, revenue) = 0 на 2026-05-17
(`revenue_current: 0` в active-projects.json).

**Layer D — organizational vision (future-state / vapor):** Corporation с 3 уровнями
вовлечения, партнёры, community, фазы эволюции → команда → multi-BU. Детально
описано в Document 1B, НО не реализовано ни в одном из перечисленных аспектов.

**Key organizational tension surface'нута:** формальная org chart (12 agents × 6 departments)
vs фактическое единство принятия решений (Ruslan = sole operator, все через него).
Формальная структура = taxonomy; фактическая структура = hub-and-spoke с единственным
human node.

[src: CLAUDE.md §Agent Roster; shared/state/active-projects.json:L1-18;
shared/state/system-health.json:L1-30; comms/mailboxes/manager.jsonl:L1-4;
swarm/wiki/cycles/ (1 cycle present); swarm/awaiting-approval/ (3 packets)]

---

## §1 Inventory Table — 14 организационных объектов

### Легенда

| Organizational reality | Значение |
|---|---|
| **functioning** | Реально используется сейчас; evidence: recent commits / file activity / process outputs |
| **partial** | Инфраструктура существует; часть работает; часть не задействована |
| **aspirational** | Решение принято, документировано, locked; реализация не началась или не проверена |
| **vapor** | Описано в docs; нет материальных свидетельств существования |

---

### Object 1 — Система управления информацией (operational substrate)

| Поле | Значение |
|---|---|
| **FPF primitive (mgmt версия)** | U.Work + U.Outcome (ежедневные рабочие процессы; выходы = structured artefacts) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | Filesystem-as-SoT + git (commit per session) + voice pipeline (manual trigger) |
| **Accountability** | Ruslan (единственный оператор Phase A) |
| **Provenance** | `CLAUDE.md §Voice-Notes Pipeline`; `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md`; `reports/review_2026-05-14.md` (267 заметок, 6691 items) |

**Notes.** Ядро работает: транскрибация + extraction + review reports выходят регулярно
(11 review files за апрель–май 2026). НО: distribute.py.bak архивирован — авторасклад
по KB отключён, ручной. Wiki index 551 записей, 271 из них — sources (raw captures).
`shared/state/active-projects.json` last_updated 2026-04-14 — state-файлы не обновляются
через этот механизм в последний месяц.

[src: CLAUDE.md §Voice-Notes Pipeline; reports/review_2026-05-14.md:L1-7;
wiki/index.md:L9-10; shared/state/active-projects.json:L16]

---

### Object 2 — Юридическое лицо / корпорация

| Поле | Значение |
|---|---|
| **FPF primitive** | U.System (надсистема; правовая оболочка) |
| **Organizational reality** | **vapor** |
| **Coordination mechanism** | Нет (не инкорпорировано) |
| **Accountability** | Ruslan (физлицо, Берлин) |
| **Provenance** | `decisions/JETIX-CORPORATION-2026-05-05.md` существует как LOCKED concept doc, но purpose = «концептуальный документ» для партнёров/инвесторов; юрадрес не указан |

**Notes.** JETIX-CORPORATION-2026-05-05.md — это нарратив о будущей корпорации, не
свидетельство инкорпорации. Физическое юрлицо на 2026-05-17 не зарегистрировано
(нет упоминания GmbH/UG/Ltd/LLC регистрации ни в одном файле). Ruslan действует
как физлицо из Берлина.

[src: decisions/JETIX-CORPORATION-2026-05-05.md:frontmatter (purpose: «концептуальный документ»);
отсутствие файлов типа registration-certificate.md или entity-incorporation.md в repo]

---

### Object 3 — Vision / задумка (future-state Jetix)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Plan (замысел системы; North Star) |
| **Organizational reality** | **aspirational** |
| **Coordination mechanism** | Part 11 Strategic Direction Substrate (LOCKED F5); 6 типов strategic docs; Decisions DB |
| **Accountability** | Ruslan (sole strategist per Rule 1; Pillar C Tier-2) |
| **Provenance** | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (35 UC × 12 categories, LOCKED); `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (LOCKED F5); `decisions/JETIX-CORPORATION-2026-05-05.md` §0 TL;DR; `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` |

**Notes.** Vision хорошо задокументирован и locked. Структура для hosting vision-documents
существует (Part 11). НО: нет свидетельств регулярного «strategic reflection» или «North Star
review» через Part 9 (Owner Interaction Scaffold) — monthly cadence задекларирована в
архитектуре, но execution не виден в файловой системе (нет `daily-log/` директории,
нет `weekly-review/` директории).

[src: CLAUDE.md §Foundation Architecture v1.0 (LOCKED); decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md;
отсутствие daily-log/ / weekly-review/ директорий в ls]

---

### Object 4 — Рабочий продукт (shipped artefacts)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Outcome (produced work products) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | git commits (каждый working session); `swarm/wiki/drafts/` для cell outputs |
| **Accountability** | Ruslan + cell experts (brigadier dispatches, drafts commit) |
| **Provenance** | `git log` (recent commits: Phase B FPF/IWE cycle 2026-05-17, 9000+ LOC; Foundation v1.0 cycle 2026-04-28); `swarm/wiki/drafts/` (15 draft files from Phase B); `outreach/` (6 files incl 2026-05-17) |

**Notes.** Реально шиппится: (1) Foundation v1.0 architecture docs — F5 LOCKED, acked;
(2) Phase B FPF/IWE research cycle — 15 cell drafts + working file + cooperation plan (2026-05-17);
(3) outreach materials (levenchuk/tseren letters, video scripts). НЕ шиппится: клиентские
deliverables (revenue = 0). Продукт = internal knowledge artefacts + outreach infrastructure;
внешнего платящего клиента на 2026-05-17 нет.

[src: git recent commits (455b341 → 636a527); swarm/wiki/drafts/ (15 task-fpf-iwe files);
outreach/ (6 files); shared/state/active-projects.json:L9 revenue_current:0]

---

### Object 5 — Decision-making system

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Role (owner = sole decision-maker) + U.Plan (Decisions DB) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | AWAITING-APPROVAL packets (3 в `swarm/awaiting-approval/`); Pillar C Rule 1 (AI = scribe; Ruslan = sole strategist); Part 6b Human Gate |
| **Accountability** | Ruslan (ack authority per FUNDAMENTAL §6.2) |
| **Provenance** | `swarm/awaiting-approval/` (3 files: cycle-10, cycle-11, r12-anti-extraction); `decisions/RUSLAN-ACK-*` (8 ack records); `CLAUDE.md §4.1 Rule 1` |

**Notes.** Формальная структура принятия решений существует и применялась:
8 RUSLAN-ACK acks задокументированы, 3 AWAITING-APPROVAL пакета написаны.
НО: AWAITING-APPROVAL пакеты — самые старые (cycle-10/11: 2026-04-26;
r12: 2026-05-12); нет свидетельств что механизм применяется ежедневно.
Альтернативный decision flow наблюдается: решения через голосовые заметки → review report →
Ruslan ack неформально (не через AWAITING-APPROVAL пакет).

[src: swarm/awaiting-approval/ (3 files, dates visible); decisions/RUSLAN-ACK-*.md (8 records);
reports/review_2026-05-14.md (decisions category: 335 items из 6691)]

---

### Object 6 — Coordination protocol / Hub-and-spoke

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Role + U.Work (dispatch → execute → return pattern) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | `swarm/lib/routing-table.yaml` + `swarm/lib/shared-protocols.md` (written 2026-04-23); brigadier.md as dispatcher |
| **Accountability** | brigadier (orchestration authority) → Ruslan (HITL) |
| **Provenance** | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md`; `swarm/lib/shared-protocols.md`; `CLAUDE.md Global Rule 8 hub-and-spoke` |

**Notes.** Протокол написан и locked (Part 4 F5). Реально применяется в swarm-cycle
dispatches: Phase B (2026-05-17) произвёл 15 expert cell dispatches с structured returns
(per `reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md`). НО: `comms/mailboxes/`
JSONL содержат устаревшие записи (manager.jsonl = 4 записи, последняя 2026-04-15) —
mailbox-based coordination не активна.

[src: swarm/lib/shared-protocols.md:L1-30; comms/mailboxes/manager.jsonl:L1-4 (last 2026-04-15);
reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§1 (15 dispatches)]

---

### Object 7 — Project portfolio (8 active projects)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Plan × U.Work (each project = bounded deliverable set) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | Part 7 Project Lifecycle Substrate (5-state machine SG-1..SG-4); `shared/state/active-projects.json` (stale) |
| **Accountability** | Ruslan (sole operator); `shared/state/active-projects.json` names sales-lead as owner of quick-money |
| **Provenance** | `CLAUDE.md §Проекты (8 активных)`; `shared/state/active-projects.json` (last_updated 2026-04-14); `swarm/wiki/projects/` = 0 files (directory does not exist) |

**Notes.** 8 projects задекларированы в CLAUDE.md. Фактическое состояние:
`shared/state/active-projects.json` = только quick-money (1 project), last_updated 2026-04-14,
revenue_current = 0. `swarm/wiki/projects/` не существует (Glob returned 0 files).
`swarm/wiki/cycles/` = 1 active cycle (cyc-foundation-build-2026-04-28) + 2 archived.
7 из 8 projects = нет материального project-file с recent activity. Декларация в CLAUDE.md
≠ активный project с stage-gate tracking.

[src: CLAUDE.md §Проекты; shared/state/active-projects.json; swarm/wiki/projects/ (0 files);
swarm/wiki/cycles/ (1 active cycle)]

---

### Object 8 — Agent roster (12 legacy + swarm agents)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Role (abstract role archetypes per IP-1; NOT executors) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | `.claude/agents/` system prompt files; Part 4 routing-table; RUSLAN-LAYER executor-binding.yaml.template |
| **Accountability** | Ruslan (instantiates via Claude Code Task dispatch) |
| **Provenance** | `ls .claude/agents/` = 23 files (12 legacy + brigadier + 5 ROY experts + levenchuk-deep-dive-brigadier + quick-money-brigadier + project-brigadier + systems-expert) |

**Notes.** Реально существующие (файлы написаны, активно используются):
brigadier.md, engineering-expert.md, mgmt-expert.md, philosophy-expert.md,
investor-expert.md, systems-expert.md (ROY swarm — 6 files). Кроме них:
23 agent definition files присутствуют.

Разрыв: CLAUDE.md таблица = 12 agents × 6 departments (Phase 1-4). Фактически ROY swarm
(brigadier + 5 experts) = основная операционная единица 2026-04-23 и далее.
12 legacy agents (manager/personal-assistant/system-admin и т.д.) = files exist,
mailboxes initialized, НО mailbox activity = практически отсутствует (manager.jsonl
последнее сообщение 2026-04-15). Legacy agent roster = taxonomy document, не
работающая org structure.

[src: ls .claude/agents/ (23 files); comms/mailboxes/ (13 legacy mailboxes, stale);
reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§1 (ROY swarm active)]

---

### Object 9 — Strategic Layer (Hexagon insights + Decisions DB)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Plan (strategic direction artefacts) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | Part 11 Strategic Direction Substrate; 6 doc types (Lock Entry / North Star / Strategic Insight / Direction Card / Phase Plan / Strategic Reflection); `decisions/strategic/` |
| **Accountability** | Ruslan (sole author of strategic prose per Rule 1) |
| **Provenance** | `decisions/STRATEGIC-INSIGHT-*` (6 files, 2026-05-10..12); `decisions/strategic/` (29 D-Lock entries + 4 insights + 7 templates per CLAUDE.md); `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md:§7` |

**Notes.** Hexagon synthesis cycle реально произошёл (2026-05-10/11/12) — 6 STRATEGIC-INSIGHT
files существуют. R12 anti-extraction = AWAITING-APPROVAL packet написан (r12-anti-extraction-2026-05-12.md).
Per honest-self-audit §7: «THIS is the closest to intelligence amplification in Jetix».
29 D-Lock entries в `decisions/strategic/` = functioning Decisions DB.
НО: процесс не регулярный (нет weekly cadence evidence до мая 2026).

[src: decisions/STRATEGIC-INSIGHT-*.md (6 files); swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md;
reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md:§7.1]

---

### Object 10 — Бизнес-модель (TRM / quick-money consulting)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Plan × U.Outcome (revenue model + delivery model) |
| **Organizational reality** | **aspirational** |
| **Coordination mechanism** | Document 1A/1B; TRM model (6 resources; L0-L5 ladder); ACTION-PLAN-PHASE-1 |
| **Accountability** | Ruslan (sole owner + salesperson Phase A) |
| **Provenance** | `decisions/JETIX-TRM-MODEL-2026-04-30.md` (LOCKED); `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md`; `shared/state/active-projects.json` revenue_current:0; `outreach/` (letters to Levenchuk/Tseren 2026-05-17) |

**Notes.** Модель детально описана (L0-L5 ladder; mgmt fee + performance fee; 6 resource types).
ICP = Mittelstand DACH 50-500 emp manufacturing — НО per ACTION-PLAN-PHASE-1: «RES.1 —
Mittelstand DACH ICP → ABANDONED. Online-first verticals = ONLY Phase 1 focus.»
Реальная revenue = 0. Первые платящие клиенты = нет на 2026-05-17.
Текущий operational focus — partnership unlock (Tseren/Levenchuk) before sales motion.

[src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§1; decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md:§0 RES.1;
shared/state/active-projects.json:L9 revenue_current:0; outreach/tseren-response-base-2026-05-17.md]

---

### Object 11 — CRM / stakeholder network

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Role (role per contact: client / partner / advisor / network) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | `crm/people/*.md` (contact files); 13 pipeline statuses; `/crm-*` skills; `crm/log.md` append-only |
| **Accountability** | Ruslan (sales motion Phase A) |
| **Provenance** | `crm/people/` (multiple files с draft suffix: anatoliy-levenchuk-draft-5/6.md, tserin-draft-10.md, fedorev-draft-10.md); CLAUDE.md §CRM System |

**Notes.** CRM файлы существуют. Суффиксы `-draft-N` указывают на активное ведение
через voice pipeline → DRAFT promotion. Levenchuk и Tseren — key contacts с
несколькими версиями. НО: pipeline statuses; «draft_from_voice» записи не промотированы
в canonical (Ruslan promotes manually after review). Status «active» с revenue = нет
— нет closed_won записей видимых в ls.

[src: crm/people/ (10 files sampled all with draft suffix); CLAUDE.md §CRM System pipeline statuses;
decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0 (Levenchuk/Tseren = главный stopper)]

---

### Object 12 — Foundation v1.0 (governance substrate)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.System (надсистема = governance architecture) |
| **Organizational reality** | **aspirational** (spec LOCKED; operational enforcement = partial) |
| **Coordination mechanism** | 11 Parts + Pillar C; constitutional_never_list (.claude/config/default-deny-table.yaml); F-G-R schema; Halt-Log-Alert |
| **Accountability** | FPF-Steward role (design/JETIX-FPF.md §5.1); Ruslan = ack authority |
| **Provenance** | `swarm/wiki/foundations/part-*/architecture.md` (12 files, all F5 LOCKED, all dated 2026-04-28); 8 RUSLAN-ACK records; CLAUDE.md §Foundation Architecture v1.0 |

**Notes.** Foundation = самый extensively documented объект в системе. Все 12 architecture.md
файлов существуют, F5 grade, acked. НО per honest-self-audit §2.1: 4 Parts = FPF-derivative
(intelligence amplification); 5 Parts = memory-dominant; 3 Parts = automation-dominant.
Foundation = governance spec, не operational enforcement layer (Halt-Log-Alert механизм
описан в Part 6b но runtime enforcement = STUB per §3.0 in agent files). Operational
enforcement = Phase B implementation target.

[src: swarm/wiki/foundations/ (12 architecture.md files); reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md:§2.1;
.claude/agents/mgmt-expert.md §3.0 «STUB Phase-B implementation»]

---

### Object 13 — Owner / Ruslan (единственный human node)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Role (owner; HITL; sole strategist; sole external-facing actor) |
| **Organizational reality** | **functioning** |
| **Coordination mechanism** | Part 9 Owner Interaction Scaffold (daily-log + weekly-review schema); 3-tier SLA; attention-budget cap (max 20 active tasks) |
| **Accountability** | Self-accountable; no external accountability mechanisms in Phase A |
| **Provenance** | `CLAUDE.md §System Overview`; `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md`; Berlin address; Max subscription (no API key cost per memory rule) |

**Notes.** Ruslan = единственная реально functioning организационная единица в полном смысле.
Все остальные объекты существуют постольку поскольку Ruslan их активирует.
Attention-budget cap = 20 active tasks (CLAUDE.md §4.2) — механизм cap задекларирован,
но нет evidence что он enforcement'ится (kanban.json существует в shared/state/;
содержимое не проверялось в этой сессии).
Part 9 cadence (daily/weekly/monthly) = spec LOCKED; нет `daily-log/` директории
в repo (отсутствует по Glob).

[src: CLAUDE.md §System Overview + §Кто ты; swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md:§0;
shared/state/kanban.json (exists, contents not read); отсутствие daily-log/ directory]

---

### Object 14 — External touchpoints (outreach + L1 interface)

| Поле | Значение |
|---|---|
| **FPF primitive** | U.Work × U.Role (external-facing work products + stakeholder roles) |
| **Organizational reality** | **partial** |
| **Coordination mechanism** | Part 10 External Touchpoints (LOCKED); `outreach/` directory; `crm/` pipeline; `comms/` (email not active per repo) |
| **Accountability** | Ruslan (all external comms) |
| **Provenance** | `outreach/` (6 files: pitch, video script, document pool, cooperation plan, levenchuk + tseren response bases — all 2026-05-12..17); Part 10 architecture.md (F5 LOCKED); reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§2.5..§2.6 |

**Notes.** Outreach infrastructure реально создаётся: за последние 2 недели (2026-05-12/17)
6 outreach files написаны — видео-скрипт для Tseren, letter bases для Levenchuk/Tseren,
cooperation plan. Phase B Summary §2.5-§2.6 описывает эти outputs. НО: «отправлены» ли
эти materials = нет evidence в repo. Part 10 = spec for external interface; actual
external communication = manual Ruslan action not tracked in repo.

[src: outreach/ (6 files, ls evidence); reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§2.5-§2.6]

---

## §2 Functioning vs Aspirational — explicit separation

| Object | Что реально работает (с evidence) | Что в процессе | Что задумано |
|---|---|---|---|
| 1. Информационная система | Voice pipeline (11 reviews); wiki (551 records); git commits active | distribute.py manual; state JSON stale | Full auto-KB distribution; Part 3 methodology library |
| 2. Юрлицо | Ruslan как физлицо (Berlin) | — | GmbH/UG инкорпорация не упомянута |
| 3. Vision / задумка | FUNDAMENTAL LOCKED; Workshop LOCKED; 8 RUSLAN-ACK records | Phase B research (FPF/IWE scope definition) | Реализация vision в client-facing product |
| 4. Рабочий продукт | Foundation docs (F5 LOCKED); 15 Phase-B cell drafts; outreach files | FPF scope definition Phase 0 (этот цикл) | Client deliverables (revenue = 0) |
| 5. Decision-making | 8 RUSLAN-ACK records; 3 AWAITING-APPROVAL packets; 29 D-Lock entries | — | Daily Part 9 cadence + SLA enforcement |
| 6. Coordination protocol | Part 4 LOCKED; Phase-B ROY swarm dispatches (15 cells) | — | Mailbox-based legacy coordination (stale) |
| 7. Project portfolio | 1 project в active-projects.json (quick-money) | Phase 0 FPF scope (этот цикл) | 7 из 8 проектов без материального tracking |
| 8. Agent roster | 6 ROY swarm agents (brigadier + 5 experts) активно используются | — | 12 legacy agents = taxonomy без операционального использования |
| 9. Strategic Layer | 6 STRATEGIC-INSIGHT files; 29 D-Lock entries; R12 AWAITING-APPROVAL | Hexagon weekly cadence emerging | Formal B.5.2 Abductive Loop enforcement |
| 10. Бизнес-модель | TRM model LOCKED; ACTION-PLAN written | Tseren/Levenchuk partnership unlock | First paying client; L0-L5 ladder activation |
| 11. CRM / stakeholders | crm/people/ files (draft статусы); Levenchuk/Tseren records | Voice → draft promotion backlog | closed_won records; active pipeline |
| 12. Foundation v1.0 | 11 Parts architecture.md (F5 LOCKED); constitutional schemas | — | Runtime enforcement (Halt-Log-Alert = STUB) |
| 13. Ruslan (owner) | All work flows through Ruslan; active daily | — | Part 9 daily-log cadence (no directory exists) |
| 14. External touchpoints | 6 outreach files written (2026-05-12..17) | Tseren/Levenchuk outreach pending actual send | Part 10 external interface full activation |

---

## §3 Coordination gaps

**Gap 1 — Strategic layer → project portfolio disconnect.**
29 D-Lock entries + 6 Strategic Insights существуют. 8 active projects задекларированы.
Нет evidence того, что конкретные projects имеют explicit linkage к конкретным Lock entries.
`swarm/wiki/projects/` = 0 files. Part 7 stage-gate predicates = declared in architecture,
не в project files. Handoff: кто и когда переводит strategic insight → project task = неясно.
[src: CLAUDE.md §Проекты; swarm/wiki/projects/ (0 files); decisions/strategic/ (29 entries)]

**Gap 2 — Agent roster → actual dispatch disconnect.**
CLAUDE.md декларирует 12 agents × 6 departments. Реально dispatched = ROY swarm (6 agents).
Legacy agents имеют mailboxes, но последнее сообщение = 2026-04-15. Нет механизма
который уточняет когда и почему sales-lead / knowledge-synth / life-coach становятся
active. Граница между «legacy roster» и «ROY swarm» в документации нечёткая —
они описаны в одном CLAUDE.md разделе.
[src: CLAUDE.md §Agent Roster; comms/mailboxes/ (13 legacy, stale); ls .claude/agents/ (23 files)]

**Gap 3 — Voice pipeline → decision execution gap.**
Voice pipeline производит тысячи items (6691 за 2026-05-14 batch; 1627 за 2026-05-10 batch).
«Ожидает ревью» = статус у большинства tasks в review reports. Нет evidence того что
items проходят из «ожидает ревью» → конкретные AWAITING-APPROVAL пакеты → Git-tracked decisions.
Альтернативный path: Ruslan принимает решения неформально (голосом → осознание → действие)
минуя formal decision track.
[src: reports/review_2026-05-14.md:L8 (1505 tasks status «Ожидает ревью»);
swarm/awaiting-approval/ (3 packets только)]

**Gap 4 — External-facing documentation → actual external communication.**
6 outreach files написаны. Нет evidence того что они отправлены (нет email/Telegram
sent confirmation в repo). CLAUDE.md: «Notion = collaboration / planning / UI (not authoritative)».
Коммуникация с Tseren/Levenchuk = состояние «готово к отправке» но не «отправлено».
[src: outreach/ (6 files); отсутствие sent-confirmation records; decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md §0 «Critical path 24-48h»]

**Gap 5 — Бизнес-модель → revenue execution gap.**
TRM model детально описана (6 resources, L0-L5 ladder). ICP = переопределён (Mittelstand → Online-first).
Revenue = 0. Нет evidence первого клиентского engagement (нет `crm/people/<client>.md`
со статусом discovery_call или выше). Critical path item — Tseren/Levenchuk partnership —
уже 7 дней в «critical 24-48h» статусе (ACTION-PLAN написан 2026-05-10).
[src: shared/state/active-projects.json:L9; decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md;
crm/people/ (all files = draft suffix, no closed_won visible)]

**Gap 6 — Foundation governance → daily operational enforcement.**
Foundation v1.0 = extensively documented. Runtime enforcement hooks (Halt-Log-Alert;
UserPromptSubmit validation; automated conformance checks) = STUB / Phase-B per agent files.
Нет `swarm/wiki/meta/health.md` файла с closed_cycles_count метрикой.
Governance = spec quality F5; operational enforcement = F2 at best.
[src: .claude/agents/mgmt-expert.md §3.0 «STUB Phase-B»; swarm/wiki/meta/ (health.md absent)]

---

## §4 Stakeholder map per organizational object

| Object | Primary owner | Secondary stakeholders | External stakeholders |
|---|---|---|---|
| 1. Информационная система | Ruslan | — (Phase A solo) | — |
| 2. Юрлицо | Ruslan (физлицо) | — | Берлинские регуляторы (потенциально) |
| 3. Vision | Ruslan (sole author) | L1 audience (Levenchuk, Tseren) — review + dialogue target | Future Jetix-partners (aspirational) |
| 4. Рабочий продукт | Ruslan + ROY swarm | — | L1 (Levenchuk/Tseren) как review audience |
| 5. Decision-making | Ruslan (ack authority) | — | — |
| 6. Coordination protocol | brigadier (orchestration authority) | Ruslan (HITL) | — |
| 7. Project portfolio | Ruslan | sales-lead (named owner quick-money в state JSON) | Потенциальные клиенты (vapor) |
| 8. Agent roster | Ruslan (instantiates) | brigadier (dispatches) | — |
| 9. Strategic Layer | Ruslan (author) | ROY swarm (drafts + surfaces) | L1 audience (Levenchuk/Tseren) |
| 10. Бизнес-модель | Ruslan | — | Tseren (Partnership target); Левенчук (L1 dialogue) |
| 11. CRM / stakeholders | Ruslan | — | Levenchuk, Tseren, Fedorev, others (draft records) |
| 12. Foundation v1.0 | Ruslan (ack authority) | FPF-Steward role (abstract) | FPF community (indirect) |
| 13. Ruslan | Self | — | Berlin community; online professional network |
| 14. External touchpoints | Ruslan | ROY swarm (draft письма) | Levenchuk + Tseren (primary) |

**Observation.** Почти каждый объект имеет Ruslan как primary owner / accountability.
Это структурная характеристика Phase A: single-operator system. Не оценочное суждение.

[src: decisions/JETIX-CORPORATION-2026-05-05.md (3 уровня вовлечения = aspirational);
CLAUDE.md §System Overview; shared/state/active-projects.json owner: «sales-lead»]

---

## §5 Dissents

**Dissent D-1 (preserved from Phase-B SUMMARY-PHASE-B §2.2):**
«IWE» в Левенчуковском C5 = paid AI guide on aisystant, NOT public FMT-exocortex-template v0.31.0.
Клеймскоуп для сравнения Jetix vs IWE в предыдущем draft = FMT public template, не aisystant.
Organizational reality inventory в этом файле NOT зависит от этого dissent, но зафиксировано
для полноты audit trail.
[src: reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§2.2 D-1]

**Dissent D-2 (mgmt-side, этот draft):**
Organizational реальность по shared/state/ и comms/mailboxes/ указывает на то что
legacy 12-agent system практически неактивен (last activity 2026-04-14..15).
НО: нельзя утверждать что legacy system «не работает» — возможно активация
происходит через Claude Code direct dispatch (без mailbox trace). Отсутствие mailbox
записей = необходимое но не достаточное свидетельство неактивности.
[src: comms/mailboxes/manager.jsonl:L1-4; CLAUDE.md (не требует mailbox для dispatch)]

**Dissent D-3 (mgmt-side, этот draft):**
`shared/state/active-projects.json` last_updated 2026-04-14 = может быть stale artifact,
не отражающий реальное состояние. Более актуальные indicators = git commits + outreach
files + review reports + swarm/wiki/drafts/. Organizational reality оценена через
комбинацию источников; single stale JSON не является единственным свидетельством.
[src: shared/state/active-projects.json:L16; git recent commits (all May 2026)]

---

## §6 Open questions для Ruslan

1. **Юрлицо.** Планируется ли инкорпорация (GmbH/UG/Ltd) до первого клиентского
   контракта, или Ruslan работает как физлицо indefinitely? Это меняет stakeholder
   map и accounting structure.

2. **Agent roster taxonomy vs operation.** Является ли таблица 12 agents × 6 departments
   в CLAUDE.md активной org chart, или историческим remnant от до-ROY-swarm периода?
   Если legacy roster deprecated — когда/как это будет отражено в CLAUDE.md?

3. **Part 9 daily cadence.** `daily-log/` директория отсутствует. Part 9 architecture
   декларирует daily-log + weekly-review schema. Активировался ли этот механизм?
   Если нет — это намеренное отложение (Phase B) или gap?

4. **Voice pipeline → formal decision track.** 1505+ tasks в «ожидает ревью» в одном
   только review report (2026-05-14). Какой процент из них доходит до formal decision
   record (D-Lock entry или AWAITING-APPROVAL)? Нет tracking этого ratio.

5. **External outreach status.** Levenchuk/Tseren letters существуют как files.
   Отправлены ли они? ACTION-PLAN-PHASE-1 (2026-05-10) называл это «critical path 24-48h».
   7 дней прошло.

6. **ICP.** RES.1 в ACTION-PLAN = Mittelstand DACH ABANDONED → Online-first. Document 1B §7
   не обновлён. Какой сейчас canonical ICP statement? В каком документе?

7. **Revenue path.** Revenue = 0 на 2026-05-17. Phase 0 FPF scope definition = текущая работа.
   Когда ожидается первый платящий клиент / engagement? Это за пределами mgmt-expert
   scope (стратегический вопрос → Ruslan).

---

## Structured return packet

```yaml
summary: |
  Organizational reality inventory: 14 объектов через mgmt lens.
  Layer A (operational substrate) = partial-functioning (voice pipeline, git, wiki, ROY swarm active).
  Layer B (governance) = spec-locked F5, operational enforcement = STUB/Phase B.
  Layer C (strategic docs) = aspirational-locked (vision/TRM/Workshop LOCKED; revenue = 0).
  Layer D (corporation/community/partners) = vapor.
  6 coordination gaps surface'нуто.
  Key finding: единственный full-functioning org node = Ruslan.
  12-agent legacy roster = taxonomy artifact, not operational structure.

proposed_writes:
  - path: swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-mgmt-integrator-inventory-org.md
    note: this file

provenance:
  - {path: "CLAUDE.md", range: "§System Overview + §Agent Roster + §Проекты + §Voice-Notes Pipeline + §CRM System + §Foundation Architecture v1.0"}
  - {path: "reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md", range: "§2-§13"}
  - {path: "decisions/JETIX-CORPORATION-2026-05-05.md", range: "frontmatter + §0 TL;DR"}
  - {path: "decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md", range: "§0 + §1.1 + §1.2 RES.1"}
  - {path: "decisions/JETIX-TRM-MODEL-2026-04-30.md", range: "§1 (6 resource types)"}
  - {path: "swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md", range: "§0 Mission"}
  - {path: "swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md", range: "frontmatter ClaimScope"}
  - {path: "swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md", range: "frontmatter ip2_single_owner_bounded"}
  - {path: "swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md", range: "§0 Mission"}
  - {path: "swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-mgmt-integrator-jetix-vs-iwe.md", range: "§1 Org unit definition"}
  - {path: "shared/state/active-projects.json", range: "full (18 lines)"}
  - {path: "shared/state/system-health.json", range: "full (30 lines)"}
  - {path: "comms/mailboxes/manager.jsonl", range: "L1-4"}
  - {path: "reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md", range: "§1 + §2.1-§2.6"}
  - {path: "ls:.claude/agents/", range: "23 files enumerated"}
  - {path: "ls:swarm/wiki/cycles/", range: "1 active cycle + 2 archived"}
  - {path: "ls:swarm/awaiting-approval/", range: "3 packets"}
  - {path: "ls:outreach/", range: "6 files"}
  - {path: "ls:reports/review_*.md", range: "11 voice pipeline reviews"}

confidence: medium
confidence_method: structured-rubric + filesystem-evidence (Glob/Grep/ls) + document reads

escalations: []

dissents:
  - {position: "legacy 12-agent roster not necessarily inactive — direct dispatch without mailbox trace possible", evidence: ["comms/mailboxes/manager.jsonl:L1-4", "CLAUDE.md §Agent Roster"], F: F3}
  - {position: "stale shared/state/ JSON may not reflect actual project activity", evidence: ["shared/state/active-projects.json:L16", "git recent commits (May 2026 active)"], F: F3}
  - {position: "IWE=aisystant paid guide, not FMT public template (D-1 from Phase B)", evidence: ["reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md:§2.2"], F: F4}
```
