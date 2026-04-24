---
id: concept-L0-company-as-code-foundation
title: "L0 Foundation — Company-as-Code"
type: concept
layer: spine
niche: meta
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: drafted
state: drafted
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: engineering-expert-integrator
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
derived_from: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 verbatim + §Y"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md", range: "D.1-D.3 + D.8 + D.9"}
  - {path: "swarm/lib/shared-protocols.md", range: "§8 verb-dictionary + §9 retrieval"}
  - {path: "reports/review_2026-04-24.md", range: "audio_510 row 443-445, audio_519 row 454, audio_520 rows 455-456"}
  - {path: "CLAUDE.md", range: "Architecture + Global Rules"}
related: []
topics: [company-as-code, git-provenance, declarative-config, knowledge-as-code]
tags: [#type/concept, #status/drafted, #priority/P1, #topic/foundation]
provenance_inline: true
definition: "L0 — субстрат, в котором состояние всей Jetix (агенты, знания, конфиги, решения) живёт в git как единственный авторитетный источник истины."
examples:
  - "git revert как механизм отката компании"
  - "atomic commit как единица изменения системы"
  - "yaml declarative configs под .claude/config/ вместо hardcoded путей"
extends:
---

# L0 Foundation — Company-as-Code

## Суть в одной строке

Git-репозиторий IS компания: каждое изменение = snapshot, история = аудит-трейл, rollback = `git revert`.

## Миссия

L0 существует ровно для одного: обеспечить, чтобы **состояние Jetix было восстановимо из git-истории на любой момент времени**. Всё остальное — агенты, знания, клиентские проекты, стратегические решения — живёт поверх этого фундамента. Без него любой другой слой ненадёжен.

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

## Что живёт в L0

### Агенты

Три агента имеют прямое отношение к работе L0:

- **system-admin** (`agents/system-admin`) — инфраструктурный агент; отвечает за состояние `.claude/`, инструменты под `tools/`, конфиги под `.claude/config/*.yaml`. Commit-компетенция: infra, config, tools.
- **brigadier** (`.claude/agents/brigadier.md`) — единственный агент, который writes в `swarm/wiki/<canonical>/`; все wiki-операции проходят через него. Commit-компетенция: wiki, swarm, agents.
- **engineering-expert** (`.claude/agents/engineering-expert.md`) — этот агент; пишет в `swarm/wiki/drafts/` и в собственный `agents/engineering-expert/strategies.md`. Commit-компетенция: drafts, engineering strategies.

Остальные 4 эксперта (management, investor, philosophy, systems) имеют аналогичную write-scope per их frontmatter.

[src:CLAUDE.md#Agent-Roster] [src:swarm/lib/shared-protocols.md#5]

### Документы

- `decisions/` — locked decisions D1-D28, JETIX-VISION, JETIX-PLAN, JETIX-ARCHITECTURE-BRIEF. Read-only после ack. Авторитет наивысший.
- `design/` — архитектурные спецификации (ROY-WIKI-V3-ARCHITECTURE-SPEC, JETIX-FPF). Binding for downstream agents.
- `.claude/rules/` — global.md, project-specific rules; читаются каждым агентом при старте сессии.
- `raw/research/` — источники первого уровня (Tier-1); ingest-сырьё.
- `prompts/` — исполнительные брифы для конкретных задач (km-materialization-mvp-execution-2026-04-24.md и подобные).

[src:CLAUDE.md#Wiki-Architecture-v2] [src:swarm/lib/shared-protocols.md#2]

### Инструменты и навыки

Все skills живут как `.claude/skills/*.md` — markdown-файлы с bash/python блоками, которые Claude Code исполняет при вызове:

- `/ingest` — источник → wiki страницы + index + log + edges; принимает `--anchor=<project|topic>` (D28 requirement)
- `/lint` — health check (dangling-edge, orphan-concept, missing-frontmatter, duplicate-slug, cross-client-global) + `--check-stage-gates` + `--validate-predicate`
- `/consolidate` — merge дубликатов; `--weekly` для авто-merge
- `/build-graph` — community detection; пишет `swarm/wiki/graph/communities.jsonl`
- `/company-status` — git-native snapshot всей компании в ≤80 строк, zero network
- `/knowledge-diff` — delta wiki между двумя датами по git log

Каждый skill: config-driven (читает `${WIKI_ROOT}` из `.claude/config/wiki-roots.yaml`), zero hardcoded paths, zero provider API-key references.

[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.4] [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.7]

### Структуры данных

- **Atomic commits** — формат `[area] verb what (why)`. `area` ∈ {km-mvp, ingest, ask, lint, consolidate, build-graph, agents, config, templates, tools, docs}. Каждый commit = один логически завершённый шаг. No amend after push. No `--no-verify`. No force-push.
- **YAML declarative configs** под `.claude/config/` — `wiki-roots.yaml` (root paths + clients namespace), `project-types.yaml` (4 типа проектов), `sg-banned-phrases.yaml` (18 форм для SG lint). Каждый файл обязан иметь `schema_version:`, `last_modified:`, `managed_by:`.
- **Provenance fields** в frontmatter каждой wiki-страницы — `sources[]` non-empty, inline `[src:<path>#<section>]` per non-trivial paragraph, edge record в `swarm/wiki/graph/edges.jsonl` на каждый wikilink.
- **edges.jsonl** — append-only граф typed edges (9 типов: extends, supports, contradicts, supersedes, derived_from, related, cross-tree-ref, etc.)

[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.1] [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.2] [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.3]

## Границы

### In-scope

- **Git как системное состояние** — `git log --follow <file>` = полная линейная provenance любого файла; `git revert` = rollback компании; `git log --oneline` = человекочитаемый operations ledger.
- **Declarative configs** — все структурные параметры в `.claude/config/*.yaml`; никаких hardcoded Jetix-specific paths в skill-коде.
- **Atomic commits with provenance** — каждый коммит имеет `[area] verb what (why)` + API-key audit перед push (`grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY' <files>` → 0 hits обязательно).

### Out-of-scope

- **Контент знаний** → L1 (wiki foundations, concepts, themes, claims). L0 — субстрат, L1 — содержимое.
- **Voice-ingest pipeline** → L2 (transcribe → extract → filter → review; tools/run_pipeline.sh). L0 хранит результаты, не обрабатывает.
- **Agent memory** → L4 (per-agent strategies.md, scratchpad.md, niche/ symlinks). L0 — файловая система; L4 — что агенты помнят.
- **Notion** → UI-only collaboration layer; агенты НИКОГДА не пишут в Notion; при конфликте fs wins (D17).

[src:CLAUDE.md#Global-Rules] [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

## Интерфейсы с соседними слоями

**Читает из:** все слои L1-L13 читают L0 (git log, skill files, config yamls, decisions) как read-only substrate. L0 не читает из себя — оно IS субстрат.

**Пишет в:** L0 не пишет в другие слои напрямую. Напротив, **все остальные слои пишут В L0** через git commits. Каждое изменение в системе — snapshot в L0.

**Вызывает:** ничего. L0 вызывается всем остальным через git-операции: `git add`, `git commit`, `git push`, `git log`, `git revert`. Это инверсия зависимости — L0 пассивен, как filesystem под Unix.

[src:swarm/lib/shared-protocols.md#8] [src:swarm/lib/shared-protocols.md#1]

## Текущий статус 2026-04-24

- **Ветка:** `claude/jolly-margulis-915d34` (активная Phase A; no force-push; коммиты только через brigadier)
- **Видимые compounded cycles:** 3 цикла с явными KM-Mat commits (km-mat-mvp Wave-1..Wave-3 + gate-D + mailbox log — по git log из последних 5 коммитов в `README` истории)
- **Design record promoted:** `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md` — state=accepted, promoted_at=2026-04-24 brigadier после прохождения §5.5.5 gate
- **Configs present:** `.claude/config/wiki-roots.yaml`, `.claude/config/project-types.yaml`, `.claude/config/sg-banned-phrases.yaml` — declarative, schema-versioned, no hardcoded paths
- **Skills active:** `/ingest`, `/lint`, `/consolidate`, `/build-graph`, `/company-status`, `/knowledge-diff`, `/ask`, `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote`
- **Locks in force:** D1-D28; D25 Company-as-Code ACKED Ruslan 2026-04-24 22:45 CET

[src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md#D.10] [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#§X]

## Путь эволюции Phase 1 → Phase 3+

**Phase 1 (сейчас, €0-€50K):** Единственный разработчик (Ruslan) + 6 агентов. Все commits через brigadier. Дисциплина atomic commit + провенанс + declarative config уже в силе. Инфраструктура готова к масштабированию с Day 1 — именно это значит D25: *«инфраструктура способная выдержать масштабирование до триллиона капитализации»*.

**Phase 2 (€200K):** Первые 2-3 сотрудника. L0 переходит от single-developer commits к multi-developer commit discipline. Добавляются: CI pipeline (pre-commit hooks, PR review), multi-dev atomic-commit enforcement, branch protection rules. engineering-expert split-trigger может сработать (§1d): artefact mix > 60/40 code vs architecture.

**Phase 3 (€1M):** Federaton. Каждый client/partner/roy получает **fork** Jetix canonical upstream (D27). Downstream fork поддерживает свой git, адаптирует под свою нишу, свои процессы, свой vertical. Лучшие мутации возвращаются upstream через PR-style контрибуцию. L0 становится не одним репозиторием, а **distributed git network** с canonical upstream и downstream forks. Git-provenance остаётся audit-trail на каждом уровне.

**Phase 3+ (civilizational, $100M → $1T):** git-provenance as **legal audit-trail**. При SOC2 / GDPR для клиентских данных — `git log --follow` заменяет дорогостоящие compliance audit tools. USB-C позиционирование (D20 + reinforcement) реализуется через fork-and-merge: каждый бизнес работает на Jetix как «прошивке». D27 fork-and-merge — это и есть механизм, как Jetix становится «Windows прошивкой» для любого AI-augmented бизнеса.

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27] [src:decisions/JETIX-ARCHITECTURE-BRIEF.md#1]

## Голосовые записи Руслана

**audio_510 (21.04.2026, 15:21 CET)** — первичный источник D25. Из review_2026-04-24.md строки 443-445:

> Задача 443: «Описать систему взаимодействия локальных команд между собой — как они коммуницируют, берут совместные проекты при сохранении внутренней философии.» (audio_510@21-04-2026_15-21-15)
>
> Задача 444: «Плотно описать ICP и идеальный профиль людей команды, чётко распределить их под конкретные роли, набрать реально крутых специалистов.» (audio_510@21-04-2026_15-21-15)

Verbatim из D25: *«строить инфраструктуру Company as a Code с самого начала, способную выдержать масштабирование до триллиона капитализации»* + *«в режиме GitHub работала — компания как код, знания как код, чтобы это вместе соединить»*

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25] [src:reports/review_2026-04-24.md#audio_510]

**audio_519 (22.04.2026, 17:54 CET)** — источник D27 fork-and-merge. Из review_2026-04-24.md строка 464:

> Задача 454: «Создать мета-описания для каждой подсистемы с указанием что система делает и не делает, чтобы это служило первичным фильтром.» (audio_519@22-04-2026_17-54-47)

Verbatim из D27: *«Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя, а лучшие мутации возвращать в основную ветку»*

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27] [src:reports/review_2026-04-24.md#audio_519]

**audio_520 (22.04.2026, 18:40 CET)** — источник системного мышления о разграничении. Из review_2026-04-24.md строки 465-466:

> Задача 455: «Зафиксировать в философию и метод работы принципы системного разграничения задач на основе экспертных знаний для использования в Jetix.» (audio_520@22-04-2026_18-40-04)
>
> Задача 456: «Собрать в кучу все концепции системного управления и проверить гипотезу возможного варианта управления системой через практическое воплощение.» (audio_520@22-04-2026_18-40-04)

Контекст для L0: принцип разграничения задач по экспертным областям применяется на уровне L0 — каждый тип изменения (`[area]`) принадлежит конкретному субъекту с чёткими write-scope walls.

[src:reports/review_2026-04-24.md#audio_520]

## Открытые вопросы для Руслана

1. **Governance fork-and-merge (D27):** Кто maintains Jetix canonical upstream при появлении первых downstream forks? BDFL (Ruslan) / committee / meritocracy? Конкретный merge-back protocol пока не в D27 — будет в SYSTEM-OVERVIEW Phase 3 section.

2. **Licensing canonical Jetix:** MIT-like / proprietary с exception / dual-license? D13 (Closed outside / open inside) + D27 (fork-and-merge) вместе требуют решения: что именно «open» для fork (методология?) и что «closed» (core prompts/configs?).

3. **IP protection at git-level:** D25 даёт git-provenance как audit-trail. Достаточно ли этого для IP protection в Phase 3+? Или нужны дополнительные механизмы (patent + git-log как evidence, cryptographic signing коммитов)?

4. **Multi-developer atomic-commit discipline:** Когда (Phase 2) появятся 2-3 разработчика, кто enforcement-ит commit-message format и API-key audit? Нужен pre-commit hook + CI check. Brigadier сейчас единственный enforcer — при масштабировании это станет bottleneck.

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27] [src:decisions/JETIX-ARCHITECTURE-BRIEF.md#2]

## Diagram — git-repo-as-system-state

```
┌─────────────────────────────────────────────────────────────────┐
│  jetix-os/ (git repository = L0 substrate)                      │
│                                                                 │
│  ├── .claude/                  ← agent configs + rules + skills │
│  │   ├── agents/               ← brigadier + 5 experts          │
│  │   ├── config/               ← wiki-roots.yaml, project-types │
│  │   ├── rules/                ← global.md                      │
│  │   └── skills/               ← /ingest /lint /company-status  │
│  │                                                              │
│  ├── swarm/                    ← L1-L8 wiki + swarm machinery   │
│  │   ├── wiki/                 ← canonical area (brigadier-only)│
│  │   │   ├── drafts/           ← draft area (expert-written)    │
│  │   │   ├── foundations/      ← high-tier concepts             │
│  │   │   ├── designs/          ← accepted design records        │
│  │   │   └── graph/            ← edges.jsonl + communities.jsonl│
│  │   ├── lib/                  ← shared-protocols.md            │
│  │   └── gates/                ← AWAITING-APPROVAL gate packets │
│  │                                                              │
│  ├── decisions/                ← D1-D28 + VISION + PLAN + BRIEF │
│  ├── design/                   ← architecture specs (FPF, SPEC) │
│  ├── raw/research/             ← Tier-1 source material         │
│  ├── reports/                  ← voice-memo review reports      │
│  ├── tools/                    ← voice pipeline + run_pipeline  │
│  └── agents/                   ← per-agent strategies + memory  │
│                                                                 │
│  Commit DAG (append-only history):                              │
│                                                                 │
│  66fdcd6 ← [prompts] JETIX-SYSTEM-OVERVIEW.md                  │
│     ↑                                                           │
│  fbb8655 ← [locks] D25-D28 ACKED                               │
│     ↑                                                           │
│  f2f3a29 ← [km-mat-mvp] Wave-2 Gate-D + Wave-3 mgmt           │
│     ↑                                                           │
│  64297df ← [km-mat-mvp] AWAITING-APPROVAL gate                 │
│     ↑                                                           │
│  92bc629 ← [master-plan] Foundation to Execution plan          │
│     ↑                                                           │
│  ... (full history = full company audit trail)                  │
│                                                                 │
│  Remote (origin):                                               │
│  github.com/ruslan/jetix-os ← publish = git push = backup      │
└─────────────────────────────────────────────────────────────────┘
```

**Verb dictionary (per shared-protocols §8):**
- snapshot = git commit
- publish = git push
- local gate = pre-commit hook
- draft area = `swarm/wiki/drafts/`
- canonical area = `swarm/wiki/<type>/`

## Ключевые свойства

- **Восстановимость:** `git clone + git checkout <hash>` = полная реконструкция состояния компании на момент hash
- **Rollback механический:** `git revert <commit>` без "я помню что было"
- **Audit-trail неизменяемый:** no force-push, no amend-after-push, no --no-verify
- **Zero provider keys в кодовой базе:** `grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY' .` → 0 hits всегда
- **Config-driven, не hardcoded:** любой skill воспроизводим на clean clone без external setup

## Связи

- Расширяет: `[[concepts/filesystem-as-source-of-truth]]` (D17)
- Поддерживает: `[[claims/git-provenance-as-audit-trail]]`
- Связан с: `[[concepts/fork-and-merge-architecture]]` (D27)

## Edges

- `[[decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24]]` (derived_from) → `edges.jsonl`
- `[[swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code]]` (derived_from) → `edges.jsonl`
- `[[swarm/lib/shared-protocols]]` (supports) → `edges.jsonl`

## Источники

1. `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` — D25 verbatim lock (primary)
2. `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md` — engineering implementation record (D.1-D.9)
3. `swarm/lib/shared-protocols.md` — §8 verb dictionary + §9 retrieval stack
4. `reports/review_2026-04-24.md` — audio_510, audio_519, audio_520 voice memo citations
5. `CLAUDE.md` — global architecture + agent roster + conventions
6. `decisions/JETIX-ARCHITECTURE-BRIEF.md` — D4 §1 executive summary + D17 filesystem SoT
