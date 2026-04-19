---
type: stage2-review
role: simplifier
reviewer: claude-opus-4-7-subagent
input: raw/research/architecture-implementation-synthesis-2026-04-19.md
created: 2026-04-19
length: ~5400 слов
---

# Simplifier Review — Jetix Architecture Synthesis v1

> YAGNI/KISS. Phase 1 = solo founder, €0 revenue, 6-8 focused hours/day.
> Цель этого ревью — убрать всё, что не нужно для €50K к Q2 2026,
> сохранив архитектурные швы для re-introduction позже.

---

## Component Inventory (что synthesis предлагает)

Я подсчитал, прежде чем критиковать. По дереву из Area 2 + Areas 1-9:

- **Top-level директорий в `~/jetix-os/`:** 8 (life-os/, jetix/, shared/, .claude/, infra/, secrets/, tools/, scripts/, .github/) — ≈9 на самом деле
- **Top-level директорий внутри `jetix/`:** ~22 (CONSTITUTION.md + CLAUDE.md + README.md + roles/ + executors/ + agents/ + alphas/ + alpha-log/ + clients/ + wiki/ + decisions/ + postmortems/ + strategizing/ + weekly/ + letters/ + okrs/ + policy/ + processes/ + evals/ + docs/ + templates/ + products/ + comms/ + state/ + sales/ + finance/ + secrets/ symlink) — **≥22 директорий до того, как написана первая строка кода**
- **Слоёв архитектуры:** 8 (L0 + L1-L7)
- **Sub-folders в `life-os/`:** 9 (daily-log, reflection, health, relationships, personal-goals, decisions, okrs, letters, wiki)
- **Alphas:** 10 (Client, Project, Deal, Invoice, Content, Hypothesis, SKU, Member, Research Note, Postmortem)
- **Storage patterns для alphas:** 3 (Hybrid C × 6, wiki-primary × 3, YAML-only × 1)
- **Per-agent memory layers:** 5 (system.md, strategies.md, scratchpad.md, niche/, mailbox)
- **Wiki entity types:** 9 (concepts, entities, sources, topics, ideas, experiments, claims, summaries, foundations) + comparisons, niches, _templates
- **Wiki niches:** 6 (personal, business, sales, life, tech, meta)
- **Typed edges в wiki/graph/edges.jsonl:** 9
- **Role-manifest blocks:** 8 (identity, ontological, method, graph_of_creation, seniority, implementation_ai, implementation_human, evolution)
- **Career levels:** 7 (J0-JX)
- **Decision-rights matrix:** 13 decision types × 6 levels
- **Career promotion signals:** ≥4 documented (J1→J2, J2→J3, J3→J4, J4→J5)
- **C-suite роли потенциальные:** ≥7 (CFO, CMO, COO, CTO, CHRO, Chief of Staff, CAIO)
- **Текущих агентов:** 12, цель синтеза — 14 role-manifests немедленно
- **Ритуалы по cadence:** daily ×4, weekly ×3, monthly ×5, quarterly ×4, annual implicit
- **L1 tools (Day 14):** 9+ (Promptfoo, Langfuse, MkDocs Material, SOPS+age, Uptime Kuma, Healthchecks.io, Sentry, Netdata, restic + Coolify + just + Vale + markdownlint + lychee + pre-commit) → реально **14+ инструментов**
- **CI workflows:** ≥4 (eval, docs, structure-check + org-ci, cost-check)
- **Skills для wiki:** 5 (/ingest, /ask, /lint, /consolidate, /build-graph)
- **Operational metrics в Appendix C:** **31 метрик** определены
- **Open Questions to Ruslan:** 10 (Part 4) + 13 inline в areas (по Q1/Q2 на каждую область)
- **Conflicts resolved:** 10
- **D1-D9 чистовиков:** 9 документов, 29-39 hours estimate

**Итого: примерно 200+ архитектурных артефактов до первого €.**

Это — не критика стиля. Это — измеримая cognitive load для одного человека. Каждый компонент даёт цену поддержки, даже если "просто файл". Простая арифметика: 22 директории × 1 README × 100 строк × ревизия раз в квартал = **уже 2200 строк maintenance writing/quarter** только для скелета. Без контента.

---

## Executive Simplification (≈500 слов)

**Top-3 biggest over-engineering candidates** — те, которые реально съедят месяц времени и при этом не приблизят к €50K:

### #1 — Двойное хранение alpha-state (per-alpha history.jsonl + monthly alpha-log + git commits)

**Before:** Conflict 3 resolved as "both": `alphas/<type>/<id>/history.jsonl` (hot) + `alpha-log/YYYY-MM.jsonl` (projected) + git commits + GoBD compliance + DuckDB projections + compensating events. Это четыре источника истины (R5 §C.6 sам признаёт). `scripts/project.py` daily/weekly rebuilds aggregate.

**After (Phase 1):** Один файл — `alpha-log/YYYY-MM.jsonl`. Все события туда. Git commits = достаточный per-alpha audit trail (`git log -- alphas/clients/acme-gmbh/`). Никакого projection script, никакой консистентности. 5 клиентов × 50 событий/месяц = 250 lines/month — DuckDB справится с одним файлом до 100K events.

**Re-add trigger:** Когда single agent теряется в context loading (>10 активных клиентов с >100 событий каждый), или когда GoBD audit реально required (€100K+ ARR + Steuerberater spec).

**Saved:** 1-2 дня на projection script + ongoing debugging dual-write. И — главное — концептуальная честность: один источник истины.

### #2 — 8-блочный role-manifest для всех 14 агентов immediately

**Before:** D3 estimate "6-8 hours для spec + 14 examples". Реально (R3 §H.5): "33-47 часов work" — почти неделя только role-manifest writing. 8 блоков × 14 ролей = 112 sections to fill, multiple of which требуют hypothetical content (implementation_human для AI-only ролей, evolution.changelog без истории, split_trigger без data на load).

**After (Phase 1):** **Minimum Viable Manifest = Blocks 1, 2, 4, 6** (identity, ontological, graph-of-creation, implementation_ai). ~50 lines на роль вместо 500. **Только для 5 ролей**, реально работающих сейчас: strategic-management, sales-lead (когда появится), delivery, knowledge-synth, meta-agent. Остальные 7 — `agents/<id>/system.md` остаётся как есть (текущая Markdown инструкция).

**Re-add trigger:** Block 5 (seniority) при первом human hire. Block 7 (implementation_human) одновременно. Block 8 (evolution) при первом role-version bump (v1→v2). Block 3 (method) при первом постмортеме где method был причиной фейла.

**Saved:** 25-35 часов upfront. Сохраняет seam — расширяется без миграции (просто добавил блок в frontmatter).

### #3 — 22 top-level директории в `jetix/` на Day 1

**Before:** Дерево из Area 2 расписывает roles/, executors/, agents/, alphas/, alpha-log/, clients/, wiki/, decisions/, postmortems/, strategizing/, weekly/, letters/, okrs/, policy/, processes/, evals/, docs/, templates/, products/, comms/, state/, sales/, finance/, secrets/. Каждая нуждается в README ("норма для mega-corp aspiration" — Trade-off в Area 2).

**After (Phase 1):** **8 директорий в `jetix/`**: agents/ (combined roles+executors+system.md per Alt B в Area 2), alphas/, clients/, wiki/, decisions/, evals/, docs/, finance/. `policy/` сливается в `decisions/` (decisions and policy — same genre: committed organizational rules). `strategizing/`, `postmortems/`, `letters/`, `weekly/`, `okrs/` сливаются в `decisions/<type>/` (флат + tags в frontmatter — type: postmortem|letter|weekly|okr|strategy). `products/`, `comms/`, `state/`, `sales/`, `templates/`, `processes/` deferred — добавляются когда content реально появляется.

**Re-add trigger:** `comms/` при втором агенте, который должен координировать с другим (сейчас manager — единственный coordinator, mailbox — overengineered для 1-to-N broadcast). `sales/` когда есть второй человек, продающий (сейчас — проекция Ruslan'а на Ruslan'а). `templates/` когда есть второй автор. `state/` когда DuckDB реально нужна.

**Saved:** 14 директорий × 1 README × 50-100 строк × revisit = **≥700 строк документации**, которые иначе выпали бы из памяти и стали dead weight через 3 месяца.

**Cumulative Phase 1 saving:** ~50-60 часов upfront + cleaner mental model + zero "что в этой папке должно лежать?" ambiguity.

---

## Part 1 — Complexity Candidates by Architecture Area

### Area 1 — Overall Philosophy (D1)

**Что synthesis proposes:** 7 слоёв (L0-L7) + L0 как Executive Core, FPF-Lite, role-abstraction, company-as-code, mega-corp-as-software-artifact narrative, DACH-hardcoded, 10 alphas. D1 = 12-15 страниц.

**Что Phase 1 needs:** L1 (foundation = git + agents в Claude Code) + L4 (delivery = clients) + неявно L0 (Ruslan + agents). Всё. L2 как читательская дисциплина (ШСМ как методологический фон), не как папки. L3 (SKUs) — 4 штуки в одном `skus.md`. L5 (Membrane) — пусто до 1-го клиента (явно сказано). L6 (Topology) — пусто 2 года минимум. L7 (Portfolio) — Toggl + bank account, никакого Capital+Hours+Attention accounting фреймворка не нужно solo.

**Cut proposal:** D1 описывает 7 слоёв как **conceptual framework**, не как файловые директории. На диске: только L1 + L4 материализованы. L2 — упоминание FPF-Lite (1 файл) + 10 alphas (см. Area 5). L3 — `skus.md` + проекты в `clients/`. L5/L6/L7 — отсутствуют как директории до триггера. **D1 — 4-5 страниц, не 12-15.** Сохранить mega-corp framing (philosophical commitment), не materialize 7 слоёв as scaffolding.

**Re-add trigger:** L5 — после 1-го платящего клиента (явно). L6 — €1M ARR + competitive moat thinking. L7 — 1-й human hire (когда reality, что есть team capital, hours, attention).

---

### Area 2 — Folder Structure (D2)

**Что synthesis proposes:** Дерево с **22 top-level директориями** в `jetix/` + 9 в `life-os/` + 5 root-level (`shared/`, `.claude/`, `infra/`, `secrets/`, `tools/`, `scripts/`, `.github/`). README в каждой ("норма для mega-corp aspiration").

**Что Phase 1 needs:** 8 директорий в `jetix/`, 3-4 в `life-os/`, минимум root.

**Cut proposal — `jetix/` минимум:**

```
jetix/
├── CLAUDE.md                # Master agent schema (есть)
├── README.md
├── agents/<id>/
│   ├── system.md            # Что есть сейчас
│   ├── manifest.yaml        # 4 блока MVM (новое)
│   └── scratchpad.md        # Working memory (новое; strategies.md merged in)
├── alphas/
│   └── <type>/<id>/state.yaml    # Только для 4 alphas (см. Area 5)
├── alpha-log/YYYY-MM.jsonl  # Один файл/месяц
├── clients/                 # Markdown CRM
│   ├── companies/<slug>.md
│   ├── deals/YYYY-MM-DD-<slug>.md
│   └── activities/YYYY-MM-DD-<slug>.md
├── wiki/                    # Существует уже
├── decisions/               # Все жанры: ADR, postmortem, letter, weekly, OKR, strategy
│   ├── adr/0001-...md
│   ├── postmortem/YYYY-MM-DD-...md
│   └── ...
├── evals/<role>/golden.jsonl
├── docs/                    # Diátaxis 2-form (см. ниже)
└── finance/
    ├── invoices/YYYY/R-YYYY-NNNN.md
    └── next-invoice-number.txt
```

8 директорий. `roles/`, `executors/` — слиты в `agents/<id>/manifest.yaml`. `policy/`, `postmortems/`, `strategizing/`, `weekly/`, `letters/`, `okrs/` — слиты в `decisions/<type>/`. `comms/`, `state/`, `sales/`, `templates/`, `processes/`, `products/`, `secrets/` symlink — отсутствуют как top-level (либо deferred, либо живут глубже).

**Re-add triggers:** `roles/` separate при 30+ агентах (когда Holacracy decoupling реально начинает экономить). `comms/mailboxes/` при 3+ агентах с inter-agent coordination. `sales/` projections при 2+ продавцах. `policy/` separate при первом human hire (Betriebsrat подготовка). `templates/` при втором автор. `state/` при DuckDB queries реально used. `products/` при первом SaaS commit.

---

### Area 3 — Role Manifests (D3)

**Что synthesis proposes:** 8 блоков, ~500-1000 строк per manifest (с system prompt body), 14 examples immediately, 33-47 часов work, JSON Schema validation, lint в CI, SemVer для роли.

**Что Phase 1 needs:** Достаточно знать "кто что делает" + "когда AI escalates". Это 4 блока (identity / ontological / graph_of_creation / implementation_ai). Block 5 (seniority/decision-rights) — нужен только когда есть human для escalation OR когда AI делает irreversible действия. Сейчас Ruslan сам approves каждое action.

**Cut proposal:** **MVM = 4 блока × 5 ролей** (strategic-management, sales-lead, delivery, knowledge-synth, meta-agent). Остальные 9 агентов оставить как есть (текущий формат `.claude/agents/<id>.md`). JSON Schema — Python script проверяющий required keys, не JSON Schema spec. SemVer — git tags только (никаких `v1/` папок).

**Re-add trigger:** Block 5 — первый AI-action который Ruslan не успел approved (escalation logic нужна). Block 7 — первый human hire. Block 8 — первый promote/demote action. Full 8-block — когда добавляется 5-й role-manifest и lint показывает дрейф (>3 разных схемы).

---

### Area 4 — Life-OS Separation (D4)

**Что synthesis proposes:** Model D, 3 фазы migration, asymmetric reference rule, SOPS с 2 ключами, pre-commit hook validation references, 1-day filter-repo migration plan, GDPR DPA enterprise client trigger.

**Что Phase 1 needs:** Понимание, что когда-то будет split. Сейчас — solo, 1 человек, никаких внешних читателей. GDPR self-only — irrelevant.

**Cut proposal:** Phase 1 = `life-os/` + `jetix/` parallel folders в одном репо (как уже есть). Asymmetric reference rule — **convention в CLAUDE.md, не pre-commit hook**. SOPS — 1 ключ (Phase 1 secrets — твои Anthropic ключи, Hetzner SSH, Geschäftskonto creds — все твои). Migration script — **не пишется до триггера** (filter-repo команда — 5 минут, когда нужно). 

**Re-add trigger:** Pre-commit reference validator — за неделю до Phase 2 trigger (1-й human или DPA contract). Двойной SOPS ключ — одновременно. Filter-repo script — за 1 день до миграции (там 30 строк bash).

**Saved:** 4-6 часов на pre-commit hook + maintenance + ложных срабатываний.

---

### Area 5 — Knowledge Architecture (D5)

**Что synthesis proposes:** Three-layer (wiki/ + alphas/ + per-agent 5-layer memory) + 10 alphas + Hybrid C/wiki-primary/YAML-only patterns + per-alpha history.jsonl + monthly alpha-log + DuckDB projections + 9 wiki entity types + 6 niches × symlinks per agent + 9 typed edges + HippoRAG PPR + 5 skills (/ingest, /ask, /lint, /consolidate, /build-graph) + 50K context budget + writeback rules + ZUGFeRD 2.x + sequential Rechnungsnummer + GDPR retention log.

**Что Phase 1 needs:** wiki/ (есть), 4 alphas (Client, Deal, Invoice, Content), per-agent memory = 2 layers (system.md + scratchpad), monthly alpha-log only, 1 niche per agent (или вообще без niches на старте).

**Cut proposal:**

- **4 alphas, не 10.** Phase 1: Client, Deal, Invoice, Content. Hypothesis/Research Note/Postmortem — **просто markdown в `wiki/claims/`, `wiki/sources/`, `decisions/postmortem/`** без alpha state machine (никакого state.yaml/history.jsonl). SKU — 1 YAML файл `skus.yaml` с 4 строчками. Member — отсутствует до 1-го Alliance member. Project — необязательно отдельно от Deal в Phase 1 (deal won → activity tracking continues; project lifecycle = deal lifecycle). 
- **Per-agent memory = 2 layers:** `system.md` (с merged strategies — strategies — это просто bullet list в конце system.md, не отдельный файл) + `scratchpad.md`. `niche/` — пока 1 общая wiki/, не subdivide. Mailbox — отдельно ОК (это inter-agent контракт).
- **Single event log:** `alpha-log/YYYY-MM.jsonl` only. Drop per-alpha history.jsonl. Read-locality для агента — через `jq` filter по alpha_id (один grep по одному файлу — миллисекунды для 1000 events).
- **6 niches → 1.** До 12+ агентов с реально разной читательской диетой — niche subdivision = premature.
- **9 typed edges → 3** (related, supports, contradicts). Остальные 6 — abstract abstraction до wiki не разрастётся в graph problem.
- **5 wiki skills → 2.** /ingest и /ask. /lint, /consolidate, /build-graph — добавляются когда orphans/duplicates реально становятся проблемой (>500 страниц + measurable retrieval degradation).
- **ZUGFeRD 2.x** — необязателен Phase 1. Обычный PDF + entry в `finance/ledger.md` достаточен для 5-10 invoices/year. ZUGFeRD становится hard requirement в B2B Pflichtangaben **с 2025-01 для receiver-side**, sender-side mandatory с 2027-01. У тебя время.

**Re-add triggers:** 5-й alpha (Project) — когда Deal становится "ongoing" больше 3 месяцев и активити больше не fit в `clients/activities/`. Per-alpha history.jsonl — когда context loading реально упирается в 50K (вряд ли в 2026). 6 niches — при 12 ролях реально с разными зонами знания (вероятно Phase 2). ZUGFeRD — за 6 месяцев до 2027-01.

---

### Area 6 — FPF-Lite (D6)

**Что synthesis proposes:** 3-5 страниц, 8 секций (Target System / Stakeholders / Creation Graph / Client Principles / Internal Principles / 10 Alphas / Ritual Cadence / U-Types Lite).

**Что Phase 1 needs:** 1 страница — Target System + Internal Principles (5 шт) + 4 alphas. U-Types Lite (4-6) — academic completeness, не нужно solo до 12+ агентов.

**Cut proposal:** **FPF-Mini = 1 страница.** Sections: (1) Что Jetix создаёт (3-4 предложения); (2) 4 alphas с states; (3) 5 internal principles ("Role ≠ executor", "Artifacts over conversations", "Explicit alpha state transitions", "Writing as thinking", "Context is king"). Drop Stakeholders (известны), Creation Graph (Mermaid → нарисуется когда понадобится), Client Principles (живут в `docs/how-to/client-engagement.md`), U-Types Lite (academic, не operational). Ritual Cadence — отдельная section в `docs/`, не часть FPF.

**Re-add trigger:** Stakeholders блок при первом регуляторном interaction. Creation Graph при 5+ ролях и реальной cross-role handoff confusion. U-Types Lite при первом role-manifest review где ontology questions реально замедлили decision.

---

### Area 7 — Career Levels + Scale-up (D7)

**Что synthesis proposes:** 7 levels (J0-JX), decision-rights matrix 13 × 6, 4+ promotion signals, phase transitions Phase 0-3, AI agent promotion mechanism (90-day track record), human-AI boundary, C-suite timing table (CFO/CMO/COO/CTO/CHRO/Chief of Staff/CAIO), DACH regulatory triggers.

**Что Phase 1 needs:** Понимание "это AI-agent делает autonomously vs escalate to Ruslan". Это **бинарное решение**, не 7-уровневая лестница, пока ты solo.

**Cut proposal:** Phase 1 — **3 уровня**:
- J-Auto: agent делает без approval (sales-research scraping, inbox-processor triage, knowledge-synth daily summaries)
- J-Approve: agent подготавливает, Ruslan approves (sales-outreach messages, delivery proposals, любой external communication)
- J-Strategic: только Ruslan (sign contracts, fire/hire, change pricing, reposition)

Это покрывает 100% Phase 1 reality. J0/J1/J2/J3/J4/J5/JX — academic ceremony для AI-agents (R1 §F sам отмечает что AI compresses junior premium). Decision-rights matrix 13×6 — заменить **5-line list в каждом role-manifest** ("autonomous: [...], advisory: [...], never: [...]"). Phase transitions Phase 2/3 — keep narrative description, не materialize в structure.

**Re-add trigger:** J3 уровень при первом human hire (нужен для Mittelstand "Lead" titre на визитке + clear escalation path). J4 при втором human. Full J0-JX ladder при 5+ humans (career path conversation реально начинается). C-suite slots — реактивно, не proactively (Q2 design).

---

### Area 8 — Operational Instructions (D8)

**Что synthesis proposes:** 14-day rollout, 14+ инструментов (Promptfoo, Langfuse, MkDocs Material, SOPS+age, Uptime Kuma, Healthchecks.io, Sentry, Netdata, restic + Backblaze B2, Coolify, just, Vale, markdownlint, lychee, pre-commit), 4 CI workflows, daily/weekly/monthly/quarterly/annual rituals, Shape Up cycles 6+2.

**Что Phase 1 needs:** Минимальная стабильная инфраструктура для work + sales. Без "self-host all the things".

**Cut proposal:** см. Part 5 (Tool Stack Reduction) и Part 6 (Ritual Cadence Reduction) ниже. Спойлер: 14 → 5 tools, 14-day → 5-day rollout, 14 ритуалов → 4.

---

### Area 9 — Final Decision Record (D9)

**Что synthesis proposes:** Oxide RFD для D9 + 9 D-документов (D1-D9) + state machine prediscussion→committed.

**Что Phase 1 needs:** D9 — да. D1-D9 — overkill. **3 документа достаточно для Phase 1:** D1 (Architecture как philosophy 4-5 стр), D2 (Folder Structure как современная карта монорепо), D8 (Instructions как 5-day rollout). Остальные D3-D7 — section в одном combined `JETIX-PLAYBOOK.md`. Single source.

**Re-add triggers:** Separate D3 при 5-м role-manifest (когда spec нужен standalone reference). D5 separate при добавлении 5-го alpha. D7 separate при первом human hire.

---

## Part 2 — Minimum Viable Architecture (MVA)

Что **остаётся**, если применить YAGNI brutally:

### Layers (conceptual, не file scaffolding)

- **L0:** Ruslan + 12 Claude-агентов (как сейчас). "Executive Core" — narrative term, не директория.
- **L1:** git + Claude Code + 5 базовых tools (см. Tool Stack ниже).
- **L4:** clients/ + 4 SKUs. Это primary revenue layer.
- **L2/L3/L5/L6/L7:** упоминаются в D1, не materialize в файлы до триггеров.

### Folders (jetix/)

8 директорий: `agents/`, `alphas/`, `clients/`, `wiki/`, `decisions/`, `evals/`, `docs/`, `finance/`. Плюс CLAUDE.md, README.md.

### Alphas

4: Client, Deal, Invoice, Content. State.yaml + context.md (не history.jsonl per-alpha).

### Roles (с MVM = 4 блока)

5 manifests: strategic-management, sales-lead, delivery, knowledge-synth, meta-agent. Остальные 9 — текущий `.claude/agents/<id>.md` формат.

### Per-agent memory

2 layers: `system.md` (с inline strategies) + `scratchpad.md`. + Mailbox separate.

### Wiki

Existing structure (557 pages). Drop subdivision на 6 niches до Phase 2. 3 typed edges (related/supports/contradicts) вместо 9. 2 skills (/ingest, /ask).

### Decision Records

Combined `decisions/` директория с subfolders: `adr/`, `postmortem/`, `letter/`, `strategy/`, `weekly/`, `okr/`. Один RFD format (Oxide), one schema.

### Rituals

4: daily inbox triage, weekly Shape Up review (Friday), monthly P&L + OKR check, quarterly letter draft + retros. (Подробности в Part 6.)

### Tools (5 + Claude Code)

- git + GitHub
- Claude Code (CLI + agents)
- SOPS + age (secrets — 1 ключ Phase 1)
- restic → Backblaze B2 (backup)
- Healthchecks.io (uptime/heartbeat)

(Drop Promptfoo, Langfuse, MkDocs, Uptime Kuma, Sentry, Netdata, Coolify, just, Vale, markdownlint, lychee для Phase 1. См. Part 5.)

### Career levels

3: J-Auto, J-Approve, J-Strategic. Bare-minimum binary-plus-one.

### Metrics tracked

5 (не 31): ARR (€/month), Pipeline value (€), Avg deal cycle time (days), Hallucination rate per week, Token cost per week. Остальные 26 — define-not-track до триггеров.

### Documents

3: D1 (Architecture-as-philosophy 5 стр), D2 (Folder Structure tour), D8 (5-day Instructions). + Combined `JETIX-PLAYBOOK.md` 10-15 стр для роли/альф/career-level/FPF-mini.

**MVA total scope: ≈30-35% полного synthesis.**

---

## Part 3 — Triggers Для Re-introducing Complexity

| Component (cut в MVA) | Cut reason | Re-add trigger |
|---|---|---|
| 22 top-level folders в jetix/ → 8 | Premature scaffolding, README maintenance burden | Каждая директория добавляется когда реально появляется ≥3 файла её содержимого |
| `roles/` + `executors/` separate | Holacracy decoupling overkill для AI-only | 30+ агентов OR 1-й human (нужен exec swap-out) |
| `policy/` separate | Same genre as decisions/ | 1-й Betriebsrat conversation OR 1-й DPA |
| `strategizing/`, `letters/`, `weekly/`, `okrs/` separate | Same genre as decisions/ | Когда decisions/ имеет >50 файлов и tags не помогают navigate |
| `comms/mailboxes/` | Над-инжиниринг для 1 manager + N satellites | 3+ агента с inter-agent dependency |
| `sales/`, `state/` projections | Premature — DuckDB queries не нужны solo | 2-й продавец OR 5+ activities/day OR Steuerberater asks for query |
| 10 alphas → 4 | 6 wiki-primary alphas можно держать как просто markdown без state machine | Когда alpha-без-state реально становится stateful (e.g., Hypothesis с явными "tested/disproven" gates) |
| Per-alpha history.jsonl | Read-locality можно через grep | Context loading >50K consistently |
| 8-block role-manifest → 4 (MVM) | Block 5/7/8 — speculative для AI-only | Block 5 — 1-й AI escalation logic; Block 7 — 1-й human; Block 8 — 1-й role v1→v2 bump |
| 14 role-manifests → 5 | 9 агентов работают на текущей системе | По мере того, как role меняется (вместо переписывания .claude/agents/<id>.md, начинаем role.md MVM) |
| 7 career levels → 3 | Solo не нужна 7-step ladder | J3 при 1-м human; J4 при 2-м; full ladder при 5+ humans |
| Decision-rights matrix 13×6 → 5-line list | Premature governance | Конкретный escalation conflict случается |
| FPF-Lite 3-5 стр → FPF-Mini 1 стр | Stakeholders/U-Types — academic | Stakeholders при 1-м регулятор interaction; U-Types при 2-м role-onto debate |
| MkDocs Material + GitHub Pages | Никто не читает Phase 1 | 1-й external reader (client, advisor, hire-candidate) |
| Promptfoo CI on push | Eval-on-push для 1 разработчика — overhead | 2-й разработчик OR 100+ golden cases |
| Langfuse self-hosted | Tracing для 12 агентов = data nobody looks at | Hallucination/cost surprise OR 30+ агентов OR client request audit |
| Vale + markdownlint + lychee | Solo writing — discipline > linter | 2-й автор |
| Coolify | Push-to-deploy — нет prod service на Phase 1 | 1-й SaaS deploy OR 1-й client-facing service |
| Uptime Kuma + Sentry + Netdata | Monitoring-всего без production | 1-й client-facing service running 24/7 |
| 4 CI workflows | CI ради CI | Конкретный failure mode появляется (broken eval, broken docs link, schema drift) |
| GraphRAG / OPA/Rego / CUE / Vector DB / K8s | Все известные premature optimizations | Phase 2b+ scale numbers (5000+ pages, 50+ roles, 100+ roles, 3000+ pages, 20+ executors) |
| /lint /consolidate /build-graph skills | Wiki еще не "болит" | 500+ orphans OR 50+ duplicates measured |
| Per-agent niche/ symlinks (6 niches) | Subdivision до того, как diet diverges | 6+ агентов с явно разной context need (вероятно Phase 2) |
| ZUGFeRD 2.x XML | Mandatory только с 2027-01 sender-side | 2026-Q3 (за 6 мес до deadline) OR 1-й client demands |
| `shared/` директория | Нет 2-го репо для shared | Phase 2 (2-й репо появляется) |
| Asymmetric reference pre-commit hook | 1 разработчик = self-discipline | Phase 2 (2-й репо) |
| Constitution §6-§11 | YAGNI — invariant ради invariant | Каждый § добавляется когда конкретный incident происходит, который этот § предотвратил бы |

---

## Part 4 — Premature Optimizations Identified

Synthesis sам признаёт 5 (Part 5.2) — я confirm все:

1. **GraphRAG** — trigger 5000+ pages, не 557. Confirm.
2. **OPA/Rego** — trigger 50+ roles, не 12. Confirm.
3. **CUE/Dhall** — trigger 100+ roles. Confirm.
4. **Vector DB** — trigger 3000+ pages. Confirm. Добавляю: HippoRAG PPR на 557 pages — overkill; обычный grep/BM25 справится; HippoRAG sам — premature до 1500+ pages.
5. **Kubernetes** — trigger +20 executors. Confirm.

**Дополнительно нашёл:**

6. **DuckDB projections** — trigger при первом ad-hoc query, который реально нужен (а не "в будущем будет красиво"). Phase 1 — `jq` справляется с alpha-log/.
7. **Pre-commit reference validator** — trigger Phase 2 separate repos. Phase 1 один разработчик.
8. **Sequential Rechnungsnummer pre-commit monotonicity check** — overkill для 5-10 invoices/год; ручная дисциплина + finance/next-invoice-number.txt достаточна. Trigger: 50+ invoices/year или delegated invoice creation.
9. **Compensating events для dual-write consistency** — premature, потому что dual-write сам premature (см. #1 в Executive Simplification).
10. **`scripts/project.py` daily/weekly aggregate rebuild** — premature (drop dual-write, drop projection script).
11. **Promptfoo + Langfuse дуэт** — single tool sufficient. Pick Promptfoo (CLI fits CI mental model) OR drop both Phase 1 (manual eval по 5 cases в неделю — 30 min, вернёт сразу понятные failure modes).
12. **MkDocs Material + GitHub Pages** — published docs без readers. Phase 1: README.md + `docs/how-to/*.md` — Markdown в git, читается через GitHub UI.
13. **Vale style enforcement** — solo discipline > tooling.
14. **Backblaze B2 + Hetzner Storage Box dual** — single backup destination достаточно Phase 1. Trigger: ≥1 client с GoBD audit обещаниями.
15. **`agent-cost-check.yml` weekly token budget CI** — solo может посмотреть Anthropic console раз в неделю; CI ради CI.
16. **agents/<id>/v1/, v2/ major-version folders** — single `system.md` + git tags. Trigger major version folder: первый раз когда parallel A/B тестирование реально нужно (pre-release confidence).

---

## Part 5 — Tool Stack Reduction

**Synthesis recommends 14+ tools для Day 14:**
Promptfoo, Langfuse, MkDocs Material, SOPS+age, Uptime Kuma, Healthchecks.io, Sentry, Netdata, restic, Coolify, just, Vale, markdownlint, lychee, pre-commit (+ Hetzner Storage Box, Backblaze B2 backup destinations).

**Simplifier recommends 5 tools (+ Claude Code, + git):**

| Tool | Why keep | Cut alternatives |
|---|---|---|
| **git + GitHub** | Sine qua non | — |
| **Claude Code** | Primary executor | — |
| **SOPS + age** | Secrets management; offline; git-native | Vault premature |
| **restic → Backblaze B2** | Backup is non-negotiable; single destination Phase 1 | Drop Hetzner Storage Box duplication |
| **Healthchecks.io free tier** | Heartbeat для daily backup + critical cron | Drop Uptime Kuma (no production service); drop Sentry (no app); drop Netdata (no server-side service) |

**Drop Phase 1, re-add by trigger:**
- **Promptfoo** — re-add при 100+ golden cases OR 2-й разработчик
- **Langfuse** — re-add при unexplained cost spike OR 30+ агентов
- **MkDocs Material** — re-add при 1-м external reader
- **Coolify** — re-add при 1-м deployed service
- **just** — overkill для 5 commands; bash scripts в `scripts/` достаточны
- **Vale + markdownlint + lychee** — re-add при 2-м авторе
- **Uptime Kuma** — re-add при 1-м client-facing service
- **Sentry** — re-add при 1-м app deploy
- **Netdata** — re-add при 1-м server-managed service (Coolify, Langfuse)
- **pre-commit framework** — keep ONE simple bash hook для очевидных проблем (no Anthropic key in commit, valid YAML); full pre-commit framework re-add при 5+ hooks реально нужны

**Saved: 5-day rollout vs 14-day. ~25-30 hours setup.**

---

## Part 6 — Ritual Cadence Reduction

**Synthesis recommends:**
- Daily ×4: inbox triage, pipeline review, agent grading, morning approvals
- Weekly ×3: Shape Up review, Toggl review, close-week commit
- Monthly ×5: strategizing trigger check, QA audit, P&L review, OKR update, founder letter draft
- Quarterly ×4: quarterly letter, OKR set, role-manifest review, strategy offsite
- Annual: implicit

**Total: ~16 distinct ritual events per quarter.**

**Simplifier recommends 4 rituals:**

| Cadence | Ritual | Duration | Why this only |
|---|---|---|---|
| **Daily** | Morning inbox triage + pipeline glance + day's intent | 30 min | Single combined ritual; avoid 4 micro-rituals (cost-switching) |
| **Weekly (Friday)** | Shape Up bet status + week's commits + next week intent + close-week commit | 60 min | Combines synthesis's "Shape Up review" + "close-week commit" + light Toggl reflection |
| **Monthly (last Friday)** | P&L glance + OKR adjustment + 1-page founder note (для self-archive, not yet quarterly letter) + meta-review (что замедляло) | 2 hours | Combines synthesis's monthly 5 → 1 expanded session |
| **Quarterly** | Quarterly letter draft + OKR-next + role-manifest delta review + strategy decisions doc (1-2 RFDs) | 1 day (4-6h) | Heavy session, но quarterly = manageable |

**Drop:**
- "Daily agent grading" — meta-agent runs autonomous; Ruslan reviews only when score drops <threshold.
- "Daily morning approvals" — приходят в течение дня at-will; not scheduled ritual.
- "Strategizing trigger check monthly" — strategizing happens at trigger event (decision требуется), не by calendar.
- "QA audit monthly" — само-вкючается в monthly meta-review ("что замедляло").
- "Strategy offsite quarterly" — solo offsite — это просто quarterly letter day; не отдельное mероприятие.

**Re-add triggers:**
- Daily morning approvals as scheduled — при 5+ агентов одновременно ждут approval (queue management).
- Daily agent grading — при 1-м serious mis-action (audit needed).
- Monthly QA audit — при 2-м compliance request.
- Quarterly strategy offsite — при первом human hire (нужен team alignment event).

**Saved: ~8-10 hours/month** на церемонии, которые сейчас не дают сигнала.

---

## Part 7 — Proposed Changes для v2 (10-15 reductions с saved hours)

| # | Change | Saved (Phase 1) | Notes |
|---|---|---|---|
| 1 | Drop dual event log; keep `alpha-log/YYYY-MM.jsonl` only | 4-6h setup + ongoing | См. Executive #1 |
| 2 | Reduce role-manifests: 14 → 5 with MVM (4 blocks) | 25-35h | См. Executive #2; биggest single saving |
| 3 | Reduce jetix/ folders: 22 → 8 | 8-12h README writing + ongoing clarity | См. Executive #3 |
| 4 | Combine roles/+executors/+agents/ into agents/<id>/ | 4-6h | Holacracy-decouple — overkill для AI |
| 5 | Combine policy/+strategizing/+postmortems/+letters/+weekly/+okrs/ into decisions/<type>/ | 3-4h + cleaner mental model | Same genre |
| 6 | Drop alphas: 10 → 4 (Client, Deal, Invoice, Content) | 6-8h state machine writing | Hypothesis/Research/Postmortem — markdown без machine |
| 7 | Reduce per-agent memory: 5 layers → 2 (system+scratchpad) | 3-4h | strategies merged inline; mailbox separate; niche/ deferred |
| 8 | Reduce career ladder: 7 levels → 3 (Auto/Approve/Strategic) | 4-6h matrix writing | 13×6 matrix → 5-line list per role |
| 9 | Reduce FPF: 3-5 pages → 1 page (FPF-Mini) | 2-3h | U-Types Lite, Stakeholders, Creation Graph deferred |
| 10 | Reduce tools: 14 → 5 | 25-30h Day 1-14 setup → Day 1-5 | Biggest infrastructure saving |
| 11 | Reduce rituals: 16/quarter → 4/quarter | 8-10h/month ongoing | См. Part 6 |
| 12 | Reduce wiki niches: 6 → 1 | 2-3h symlink + maintenance | Subdivision premature |
| 13 | Reduce wiki edges: 9 → 3 (related/supports/contradicts) | 1-2h schema + ongoing tagging | 6 edge types unused Phase 1 |
| 14 | Reduce wiki skills: 5 → 2 (/ingest, /ask) | 4-6h skill writing | /lint /consolidate /build-graph at scale |
| 15 | Reduce metrics: 31 defined → 5 tracked (ARR, pipeline €, deal cycle, halluc rate, weekly token cost) | Mental load + dashboard ambition | Tracking metric you don't action = noise |
| 16 | Reduce D-documents: 9 → 3 (D1, D2, D8) + combined PLAYBOOK | 15-20h writing | См. Area 9 |
| 17 | Drop pre-commit reference validator (Phase 1) | 4-6h | Self-discipline, no 2nd repo |
| 18 | Drop ZUGFeRD 2.x XML | 6-8h | Mandatory 2027-01 sender; entry в `finance/ledger.md` Phase 1 |

**Total estimated saving: ~120-160 hours upfront + ongoing weekly cognitive load reduction.**

Это эквивалент **3-4 weeks of focused founder time, реинвестированных в actual sales activity.** Для €0 → €50K в Q2 2026, это разница между запуском и продолжением проектирования.

---

## Part 8 — Questions для Final Synthesizer (5-7 meta-questions)

1. **Scaffolding vs emergence — где провести черту?** Synthesis committed к scale-up-first. Но "scale-up-first design" не равно "build all scaffolding upfront". Можно ли formulate principle: "Build the seam, defer the scaffolding"? — то есть структура должна **расширяться без миграции**, но не **существовать пустой**. Верифицируемый critierion: каждая директория содержит ≥3 реальных артефакта или удаляется.

2. **Какой percentage architecture overhead приемлем для €0 → €50K founder?** Сейчас D1-D9 написание = 29-39 часов; rollout 14 days; role-manifest migration 33-47 hours. Это ≈100-120 часов до первого продаваемого SKU. Если 1 час Ruslan'а в Phase 1 = €100 opportunity cost (consulting билителлег), это €10-12K opportunity-cost инвестиции в инфраструктуру до первого €. Sustainable? Где cap?

3. **"Mega-corp ambition" принцип — операционализируется как design-time или as run-time?** Mega-corp aspiration = "system extends to 200+ roles without rebuild". Это design-time принцип. Но синтез often реализует его run-time (existing scaffolding для будущих ролей). Можно ли differentiate: "design must support extension" (mandatory) vs "implementation must include extension scaffolding" (optional)?

4. **Role-manifest как contract vs as documentation.** Если 8-block role-manifest — это contract между ролью и executor (включая будущего human), он должен быть minimal (контракт = surface). Если documentation — он может быть expansive. Synthesis treats it as both. Hard simplification: split в **`roles/<slug>/contract.yaml` (10-20 lines, mandatory)** + **`roles/<slug>/README.md` (expansive prose, optional)** — это лучше, чем 500-line single file?

5. **Что должно быть materialized vs implied?** Synthesis materializes 7 layers as folders. Multi-layer architecture может жить в philosophy doc (D1) и не в file structure. Phase 1 file structure — flat with smart frontmatter (`layer: L4`, `alpha: client`). Это потеряет что-то существенное?

6. **DACH-hardcoded — design constraint или Phase 1 constraint?** Если DACH — это Phase 1 market choice (target customer cohort), то architecture не должна hardcode `clients/` schema на German. Если DACH — это long-term identity, то ZUGFeRD/UStG/GoBD должны быть в core. Synthesis treats as identity. Если Phase 3 expansion возможна, hardcoding = future cost.

7. **Cognitive-load metric — где measurable threshold?** "Solo founder cognitive load" — слово, но не метрика. Можно formulate: "Phase 1 architecture passes если Ruslan может через 30 дней без работы вернуться и работать без re-onboarding". Verifiable: оставить repo на 30 дней, вернуться, time-to-productive-work. Если >2 часа — слишком сложно.

---

## Part 9 — Verdict

**Phase 1 architecture ready for deployment:** **YES, but with simplifications.**

Synthesis correctly identifies все ключевые conceptual commitments (mega-corp ambition, role ≠ executor, company-as-code, Model D nested, DACH positioning, FPF-Lite, Oxide RFD format, 10 alphas as concept). Эти — **architectural seams**, и они должны быть в D1 как principles.

Но synthesis — особенно Areas 2, 3, 5, 7, 8 — материализует эти концепции как **scaffolding на Day 1**, что неоправданно для solo founder с €0 revenue.

**Simplified architecture target: ~30-35% полного synthesis scope** (по конкретным компонентам — folders, role-manifests, alphas, layers, tools, rituals, metrics, documents).

**Конкретно:**
- **Folders (jetix/):** 22 → 8 (~36%)
- **Role-manifests:** 14 × 8 blocks → 5 × 4 blocks = ~18% объёма
- **Alphas:** 10 → 4 (40%)
- **Tools:** 14 → 5 (~36%)
- **Rituals:** 16/quarter → 4 (~25%)
- **D-documents:** 9 → 3 + 1 combined (~40%)
- **Per-agent memory layers:** 5 → 2 (40%)
- **Wiki niches:** 6 → 1 (~17%)
- **Wiki edges:** 9 → 3 (~33%)
- **Career levels:** 7 → 3 (~43%)
- **Tracked metrics:** 31 → 5 (~16%)

Усреднённо ≈30%.

**Critical:** seams сохранены. MVA расширяется до synthesis-vision **без миграции** (additive only):
- 5 role-manifests расширяются до 14 при необходимости (новые файлы, не reformatting)
- 4 blocks → 8 blocks (добавление в frontmatter, lint-обратно совместимо)
- 4 alphas → 10 alphas (новые директории, существующие нетронуты)
- 8 folders → 22 folders (новые директории, не reorganization)
- 5 tools → 14 tools (additive)
- 3 levels → 7 levels (extension, not rewrite)

**Архитектура остаётся scale-up-ready, но не scale-up-built.**

**Risk если synthesis принят полностью without simplification:** 100-120 часов архитектурного оверхеда до первого продаваемого SKU. При opportunity cost €100/h — €10-12K not-realized revenue. И — мore importantly — **1-2 месяца перед первым контактом с реальным клиентом**, где architecture должна была подстроиться под обнаруженные patterns. Premature commitment к structure, которая не survived contact с reality.

**Risk если simplifier accepted полностью:** небольшой Phase 2 cost при добавлении компонент. Но — additive — никакой миграции data. Re-add triggers конкретны и observable.

**Recommendation:** Final Synthesizer должен принять ≥80% Simplifier proposals по folders/tools/rituals/metrics (low-cost, high-saving). Для role-manifests/alphas/career-levels — найти middle ground (например, 3 alphas → 6 alphas вместо 10; 4 blocks → 5 blocks вместо 8). Для FPF-Lite — оставить 3-5 страниц как explicit philosophical anchor (это identity-shaping, не operational overhead).

**Финальный Simplifier KPI для D1-D9:** Каждый D-документ должен содержать секцию **"Phase 1 minimum / Phase 2 add / Phase 3 add"**. Если D-документ описывает только Phase-3 vision без Phase-1 cut, он не deployable.

---

**END OF SIMPLIFIER REVIEW.**
