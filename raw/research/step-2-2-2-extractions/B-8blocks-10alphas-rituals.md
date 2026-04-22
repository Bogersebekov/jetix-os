---
title: "Sub-agent B extraction — 8-block manifest, 10 alphas, rituals"
date: 2026-04-23
sources: [levenchuk-for-ai-deep-research-2026-04-19.md]
pipeline: ingested
---

# Sub-agent B extraction — FPF enhancement scan (Step 2.2.2)

Source: `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` (1041 lines). Russian technical terms preserved verbatim. Enumerations quoted from source.

---

## Part 1 — The 8-block role-manifest format (Part C.1–C.8)

C.0 framing: format = **YAML frontmatter + Markdown body (единый `role.md`)**. File naming: `roles/{slug}/role.md`. Claude Code reads whole file; CI/CD parses only frontmatter. [cite: C.0]

### Block 1 — Identity

- **Purpose / problem solved**: "Уникальная идентификация для routing при 14→100 ролях". [cite: C.1]
- **Sub-fields** (verbatim):
  - `name` (slug)
  - `display-name`
  - `version` (SemVer)
  - `layer` (L0–L7 Jetix архитектуры)
  - `family` (functional group: sales/delivery/intelligence/ops)
  - `status` (draft/active/deprecated)
  - `created` / `updated` (ISO-dates)
- **Enumerations**:
  - `layer`: L0–L7
  - `family`: sales / delivery / intelligence / ops
  - `status`: draft / active / deprecated

### Block 2 — Ontological (по Левенчуку)

- **Purpose**: "Связка роли с онтологией ШСМ". Anchors: Holacracy Constitution v5 (Purpose + Domain) and Essence Alpha (role = mover of alpha). [cite: C.2]
- **Sub-fields** (verbatim YAML):
  - `purpose:` — "Что роль создаёт в мире"
  - `target-system:` — "Система, которой служит роль"
  - `primary-alpha:` — "Одна главная alpha" (example: `client`)
  - `secondary-alphas:` — list (example: `[deal, invoice]`)
  - `domains:` — "Что роль контролирует эксклюзивно"
  - `accountabilities:` — "Ongoing activities (глагол + объект)"
  - `out_of_scope:` — "Явные НЕ-accountabilities (scope creep prevention)"
  - `acceptance-criteria:` — "Когда переход альфы считается успешным"
- **Defaults / examples**: primary-alpha = `client`, secondary-alphas = `[deal, invoice]` (in source example).

### Block 3 — Method

- **Purpose**: "Epistemology роли. Без anti-methods роль деградирует к cargo cult." [cite: C.3]
- **Sub-fields**:
  - `primary_frameworks` (с URL)
  - `thinking_protocol` — "обязательные шаги перед работой"
  - `quality_criteria` — "когда артефакт готов"
  - `anti_patterns` — "что явно НЕ делать"
  - `golden_examples` — "few-shot: ссылки на 10 эталонных completed tasks"
- **Defaults**: golden_examples target = 10 completed tasks.

### Block 4 — Graph of Creation (граф создания)

- **Purpose**: "Из Sociocracy 3.0 role pattern — domain delegation требует чёткого понимания inputs/outputs"; "блок позволяет meta-agent строить dependency graph всей системы автоматически." [cite: C.4]
- **Sub-fields** (verbatim YAML):
  - `produces:` — list of items, each with:
    - `artifact:` (name)
    - `states:` (example: `[draft, final]`)
    - `consumers:` (list of role names, example: `[manager, strategic-management]`)
  - `consumes:` — list of items, each with:
    - `artifact:`
    - `produced_by:` (role)
    - `required:` (bool)
  - `artefacts-produced:` — list with:
    - `type:` (example: "Proposal")
    - `template:` (path, example: `templates/sales/proposal-v2.md`)

### Block 5 — Seniority / Scale

- **Purpose**: "Матрица принятия решений"; "Explicit decision-rights предотвращают paralysis у AI-агентов; при mega-corp scale это enforcement layer — CI/CD проверяет соблюдение." Draws from GitLab job families / Stripe levels. [cite: C.5]
- **Sub-fields** (verbatim YAML):
  - `current_level:` — enum: `phase1-solo | phase2-lead | phase2-manager | phase3-vp`
  - `decision-rights:` with three lists:
    - `autonomous:` — actions the role does alone
    - `requires-approval:` — actions needing approval (example: "Discount > 15% → manager")
    - `never:` — actions forbidden (example: "Sign contracts", "Change pricing")
  - `escalation-trigger:` — list of `condition` + `escalate-to` pairs (example: "Deal > $50k" → strategic-management)
  - `split_trigger:` — with:
    - `conditions:` (example: "accountabilities > 7", "2+ FTE needed concurrently")
    - `split_into:` (example: `[sales-strategy, sales-execution, account-management]`)
- **Enumerations**: `current_level` ∈ {phase1-solo, phase2-lead, phase2-manager, phase3-vp}.

### Block 6 — Implementation AI

- **Purpose**: "Первичный для Jetix"; least-privilege for AI; eval-dataset detects role breakage on model swap. [cite: C.6]
- **Sub-fields**:
  - `agent_type:` (example: `claude-code`)
  - `current-executor:` (example: `"claude-sonnet-4-5"`)
  - `prompt-file:` (example: `roles/sales-lead/system.md`)
  - `eval-dataset:` (example: `evals/sales-lead/eval-v1.jsonl`)
  - `eval-passing-threshold:` (example: `0.85`)
  - `tools-allowed:` with:
    - `mcp-tools:` — list of `name`, `permissions:` (e.g. `[read, write]`), `scope:` (path glob)
    - `forbidden-tools:` (example: `[email-send, git-push]`)
  - `context-window-budget:` (example: `180000`)
  - `memory-strategy:` (example: `"rolling-summary + pinned-client-context"`)
  - `upgrade-policy:` with:
    - `auto-upgrade:` (bool, example: `false`)
    - `eval-on-upgrade:` (bool, example: `true`)
- **Defaults**: eval-passing-threshold = 0.85; context-window-budget = 180000; auto-upgrade = false; eval-on-upgrade = true.

### Block 7 — Implementation Human

- **Purpose**: "Миграционный путь к гибридной модели"; "KPIs идентичны для AI и human — позволяет A/B сравнение." [cite: C.7]
- **Sub-fields**:
  - `hired-person:` (null = AI; name when hired)
  - `onboarding-path:` — list (source enumerates 4 default stages):
    1. "Изучить role.md + golden examples (2 дня)"
    2. "Shadow AI-агента на 10 сделках (1 неделя)"
    3. "Co-pilot mode: подтверждение решений агента (2 недели)"
    4. "Autonomous mode с weekly review"
  - `reporting-to:` (role name, example: `manager`)
  - `performance-kpis:` — list of `metric`, `target`, `cadence` (example: "Pipeline conversion (lead→closed-won)" / "> 25%" / `monthly`)
  - `handoff_from_ai:` (seen in C.9 example) with `triggers:` list (example: "Deal > €50k live pitch", "Client requests human call", "Legal/NDA")

### Block 8 — Evolution

- **Purpose**: "Audit trail". [cite: C.8]
- **Sub-fields**:
  - `created-at:` (ISO date)
  - `last-updated:` (ISO date)
  - `changelog:` — list of `version`, `date`, `change`
  - `expected-evolution:` — list of forecast items (example: "Q2 2025: LinkedIn Sales Navigator MCP"; "2026: Split sales-lead-smb vs enterprise при > 50 deals")
  - `last_review:` (seen in C.9, example: `"2025-07-01"`)

---

## Part 2 — The 10 core alphas (Part D)

Framing: "Все альфы — по OMG Essence 1.2: Abstract-Level Progress Health Attribute. Каждая alpha — lifecycle-entity (не объект данных!); acceptance criteria в стиле Essence State Cards." [cite: D.head]

### D.1 Client alpha

- **Definition**: "не контакт в CRM и не компания-объект, а живые отношения с progression и health. Аналог Opportunity в Essence." [cite: D.1]
- **States** (verbatim): `lead`, `qualified`, `proposed`, `negotiating`, `closed_won` (also `closed-won`), `closed_lost` (also `closed-lost`), `churned`.
- **Transitions / movers** (verbatim):
  - `— → lead`: Inbound/outbound (inbox-processor / sales-research)
  - `lead → qualified`: ICP ≥ 70, BANT partial (sales-lead)
  - `lead → closed_lost`: ICP < 40 / no budget
  - `qualified → proposed`: Proposal sent (sales-lead)
  - `qualified → closed_lost`: No response 14d
  - `proposed → closed-won`: Verbal acceptance (sales-lead)
  - `proposed → negotiating`: Client requests changes
  - `negotiating → closed-won`: Signed (sales-lead)
  - `negotiating → closed_lost`: Breakdown
  - `closed-won → churned`: Cancellation (delivery)
  - `closed-lost → lead`: Win-back / new champion (sales-research)
  - `churned → lead`: Win-back campaign
- **Acceptance per state**: lead → "company + domain + assigned"; qualified → "ICP ≥ 70 + BANT + no blockers"; proposed → "proposal + champion + follow-up"; closed-won → "signed + handoff + CRM updated"; closed-lost → "reason documented + lessons-learned".
- **Metrics**: "time in `lead` (< 2d), lead→qualified (> 40%), qualified→closed-won (> 25%), avg deal cycle (< 30d)".
- **ШСМ primitive**: Альфа (Essence Opportunity analogue). Primary mover: `sales-lead`.

### D.2 Project alpha (Work analogue) [cite: D.2]
- **States**: `scoped → kicked-off → in-progress → delivery ⇄ closed → follow-up`.
- **Rules**: "Рождается при `client.closed-won`; backward `delivery→in-progress` при client revision."
- **Responsible**: delivery. **Metrics**: on-time delivery, Client NPS, scope creep incidents, revision count.
- **ШСМ**: Альфа (Essence Work).

### D.3 Deal/Contract alpha [cite: D.3]
- "Client = отношения, Contract = документ с правовыми последствиями."
- **States**: `draft → signed → active → completed / cancelled`; `cancelled → draft` (renegotiation).
- **Responsible**: "sales-lead (draft), system-admin (signed/active), manager (cancelled)".
- **ШСМ**: Альфа.

### D.4 Invoice alpha [cite: D.4]
- **States**: `issued → sent → paid → reconciled`; boundary: `sent→disputed`, `paid→disputed` (chargeback), `disputed→paid/cancelled`.
- **Responsible**: "system-admin; manager — для disputes". **Metrics**: DSO, dispute rate.
- **ШСМ**: Альфа (QuickBooks-based).

### D.5 Content Item alpha [cite: D.5]
- **States**: `draft ⇄ in-review → approved → published → retired → draft` (repurpose).
- **Responsible**: knowledge-synth / delivery. **ШСМ**: Альфа.

### D.6 Hypothesis alpha [cite: D.6]
- "Каждая гипотеза — falsifiable, с confidence threshold и success metric."
- **States**: `formulated → active → validating → validated / invalidated → implemented`; pivot loop `invalidated → formulated`.
- **ШСМ**: Альфа + стратегирование adjacency.

### D.7 SKU/Product alpha [cite: D.7]
- "Не внутренний процесс, а рыночная единица."
- **States**: `idea → prototype → launched → active → deprecated`. **ШСМ**: Альфа (target-system).

### D.8 Member (Alliance) alpha [cite: D.8]
- **States**: `applied → invited → active → at-risk ⇄ active / → churned → applied` (re-application). HubSpot Lifecycle-inspired. **ШСМ**: Альфа.

### D.9 Research Note alpha [cite: D.9]
- "Не документ, а epistemic entity с progression статуса достоверности."
- **States**: `started → draft ⇄ started → completed → integrated`. **ШСМ**: Альфа + мышление письмом.

### D.10 Postmortem alpha [cite: D.10]
- Google SRE culture. "Blameless tone обязателен."
- **States**: `incident → draft ⇄ reviewed → action-items → closed`. **ШСМ**: Альфа + мышление письмом.

**UNDER-SPECIFIED across D.2–D.10**: per-state acceptance checklists (only D.1 is full); per-transition responsible-role tables (only D.1).

---

## Part 3 — Rituals (Part E)

### E.1 Стратегирование-ритуал

- **Name + purpose**: Стратегирование-ритуал — generating and documenting the method choice (a la ШСМ «метод выбора метода») in 1-page form.
- **Triggers** (verbatim): "новый проект / новый SKU; новая роль или смена ответственности; крупное решение с необратимыми последствиями; квартальный reset; сигнал от альфы о смене состояния".
- **Procedural steps** (verbatim section numbering from template):
  1. **Context и триггер** — "Что происходит · Почему сейчас · Горизонт (< 3м / 3–12м / > 1г)"
  2. **Текущая реальность** — "Что работает · Что не работает · Ключевые метрики (таблица)"
  3. **Проблематизация (MECE)** — "Главный вопрос · Декомпозиция: ветки A, B, C (MECE-проверка)"
  4. **Гипотезы** — table: `# | Гипотеза | Основание | Риск | Проверяемость`
  5. **Опции (≥ 2 + status quo)** — table: `Опция | Описание | Плюсы | Минусы | Ресурс`
  6. **Решение** — "Выбор · Логика (2–4 предл) · Assumptions · Kill conditions"
  7. **Action Plan** — table: `Действие | Роль | Дедлайн | Артефакт`
  8. **Review checkpoint** — "Когда · Критерии успеха"
- **Frequency / cadence**: triggered (not fixed); also "Квартальный reset" and explicit monthly cadence per H.1 ritual table ("Strategizing — Monthly / trigger — strategist").
- **Artefacts produced**: `strategizing/YYYY-MM-DD-slug.md` (1-page document).
- **Format target**: "1 стр" — "Целевой формат" (vs Amazon 6-pager 6pp, ADR/MADR 0.5–1pp, Shape Up Pitch 1–2pp, IETF RFC 3–20pp).
- **Why 1-pager for AI agents**: "Для AI-агентов смысл документа другой — он передаёт framing. Агенты не читают 6 страниц с 'тенетами' — им нужен 1-страничный манифест с чёткой декомпозицией."
- [cite: E.1]

### E.2 Thinking-by-writing rituals (мышление письмом)

Framing (verbatim): "у агентов есть S1 (генерация), нет S2 (рефлексия) — он «внешнее, в обвязке». Writing rituals — это и есть обвязка." [cite: E.2]

Three nested rituals:

#### E.2.a Daily log

- **Artefact**: `daily-log/YYYY-MM-DD.md`
- **Procedural steps**:
  1. **Утро** — "brain dump (Julia Cameron Morning Pages): поток сознания, framing проблем дня"
  2. **Вечер** — "structured check: alpha transitions today, framing failures, one-sentence summary"
  3. **Секция Tasks → Agents** — table: `задача | агент | framing OK? | acceptance | статус EOD`
- **Cadence**: Daily.

#### E.2.b Weekly review

- **Artefact**: `weekly/YYYY-Www.md` (Shape Up-style + GTD weekly review)
- **Procedural steps** (verbatim three phases):
  1. **Get Clear** — "collect inbox агентов, loose ends"
  2. **Get Current** — "alpha states table: было → стало, agent performance: framing failures count + top example"
  3. **Get Creative** — "betting table на следующую неделю: appetite, shaped, bet? — и решение: стратегирование нужно? Y/N"
- **Cadence**: Weekly.

#### E.2.c Quarterly letter

- **Artefact**: `letters/YYYY-Qn.md` — "сначала для себя, потом Alliance" (pattern: Buffett / Mark Leonard Constellation / Patrick Collison Stripe)
- **Procedural steps — mandatory sections (verbatim)**:
  1. **The Quarter in One Paragraph** — "честный summary"
  2. **Alpha States Then vs Now** — "таблица"
  3. **What I Got Wrong** — "обязательно; без этого письмо — PR, не рефлексия"
  4. **What Worked and Why** — "конкретно: не «агенты стали лучше», а «framing audit снизил redo с N до M»"
  5. **System Changes Made**
  6. **Outlook: What I'm Betting On** — "Shape Up language"
  7. **One Question I Can't Answer Yet**
- **Cadence**: Quarterly.

### E.3 Как агенты участвуют в writing rituals

- **Pattern (verbatim)**: "**Human writes → Agents extract → Agents propose.**" [cite: E.3]
- **Procedural steps (verbatim)**:
  1. "Ruslan пишет weekly review вручную (без агентов)."
  2. "Extraction-агент читает → извлекает alpha transitions, framing failures с categorization, задачи без acceptance."
  3. "Strategy-support агент → предлагает возможные стратегирования и задачи для betting decision."
- **Roles agents may play**:
  - "Агент как автор — никогда для primary writing rituals." (may draft quarterly-letter section from weekly one-liners, but Ruslan rewrites in first person)
  - "Агент как редактор — для quarterly letter OK (проверка структуры, пропущенных разделов), но не переписывает содержание."
  - "Агент как критик — для стратегирование-документов рекомендуется (есть ли минимум 2 альтернативы? acceptance criteria? anti-scope?)."
- **Critical anti-pattern (verbatim)**: "полная автоматизация writing... «без внешнего по отношению к LLM контуру обработки текста — никак, LLM всегда обманет»... Агент генерирует синтаксически корректные, семантически пустые тексты. **Письмо — не output, это process.**"

### Additional rituals from H.1 cadence table

Supplementary operational rituals listed in H.1 (source cross-ref):

| Ритуал | Частота | Владелец | Артефакт |
|--------|---------|----------|----------|
| Inbox triage | Daily | inbox-processor | classified-inbox.md |
| Pipeline review | Daily | sales-lead | pipeline-snapshot.md |
| Agent grading | Daily | manager | graded-output.md |
| Weekly review | Weekly | manager | weekly/YYYY-Www.md |
| Strategizing | Monthly / trigger | strategist | strategizing/YYYY-MM-DD-slug.md |
| QA audit | Monthly | meta-agent | audit/YYYY-MM.md |
| Founder letter | Monthly | strategic-management | letters/monthly/YYYY-MM.md |
| OKR review | Quarterly | strategic-management | OKR-scorecard.md |
| Quarterly letter | Quarterly | strategic-management | letters/YYYY-Qn.md |
| Role manifest update | Quarterly / trigger | meta-agent + Ruslan | updated role.md |

[cite: H.1]

---

## Part 4 — B.4 FPF as protocol for AI agents (full extraction)

Title in source: **"B.4 FPF как протокол для AI-агентов"** [cite: B.4]

Full verbatim content:

> Левенчук позиционирует FPF как инструмент, адресованный AI:
>
> > *«FPF как "большой системный промпт" (manual вместо fine tuning), заставляющий AI умнеть, новое применение — поддержка хода на "умный экзокортекс киберличности инженера-менеджера"»* ([ailev 1769890](https://ailev.livejournal.com/1769890.html)).
>
> > *«В рамках Software 3.0 можно давать экзокортексу для его настройки прямо FPF или даже Guides»* ([ailev 1769548](https://ailev.livejournal.com/1769548.html)).
>
> Инфраструктура: [fpf-problem-solving-skill](https://github.com/CodeAlive-AI/fpf-problem-solving-skill), [fpf-agent](https://github.com/pokrovskiyv/FPF-agent). FPF должен бороться с тенденцией LLM переводить всё на язык доминирующей обучающей области (DevOps/programming): *«LLM ведёт себя так же, как программист: он долго тебя слушает, потом его взгляд проясняется — и он говорит "я понял! это можно написать на Фортране!"»*.

**Key operational elements extracted (no paraphrase beyond structure)**:

- **Metaphor / frame**: FPF = "большой системный промпт" — a manual that replaces fine tuning. Function: "заставляющий AI умнеть".
- **Application**: "поддержка хода на 'умный экзокортекс киберличности инженера-менеджера'" — i.e. FPF is delivered into the agent's runtime context to upgrade it to a thinking-engineer-manager exocortex.
- **Software 3.0 delivery mechanism**: "в рамках Software 3.0 можно давать экзокортексу для его настройки прямо FPF или даже Guides" — FPF or the Guides are handed to the exocortex for its configuration.
- **Reference infrastructure (existing)**:
  - `fpf-problem-solving-skill` — https://github.com/CodeAlive-AI/fpf-problem-solving-skill
  - `fpf-agent` — https://github.com/pokrovskiyv/FPF-agent
- **Explicit problem FPF is solving for LLMs**: LLMs reduce all framing to their dominant training domain (DevOps/programming). FPF is the counter-protocol for cross-frame disambiguation.
- **Illustrative failure mode (verbatim)**: "LLM ведёт себя так же, как программист: он долго тебя слушает, потом его взгляд проясняется — и он говорит 'я понял! это можно написать на Фортране!'"

**Sub-sections of B.4**: none (B.4 is a single uninterrupted section in the source). B.4 does NOT subdivide into B.4.1/B.4.2 etc. UNDER-SPECIFIED on: explicit protocol steps for loading FPF into an agent context; precise context-budget accounting; which FPF sections are "mandatory" vs "optional" for an AI agent load. These are flagged as UNDER-SPECIFIED in the source — the complementary operational content is in Part F (AI-specific adaptation: F.1 inner life, F.2 no cross-session learning, F.3 context engineering, F.4 role-manifest as worldview / constitution, F.5 meta-cognitive abilities: CoT/ReAct/Reflexion/ToT, F.6 multi-agent patterns) and Part H (FPF-Lite Jetix full draft).

Neighbouring B context also relevant to "FPF as protocol for AI agents" but located elsewhere:

- B.5 МИМ-2026 key thesis (verbatim): "Framing как узкое место AI: LLM имеют мощные вычислительные способности, но 'застревают' в доминирующем фрейме обучающих данных. FPF — ответ: явный протокол смены фреймов через upper ontology." And: "AI-агенты как новые участники мастерской — их нужно обучать по тем же руководствам, что и людей." [cite: B.5]
- B.6 explicitly lists Jetix among "FPF обязателен": "multi-agent architectures (Jetix), трансдисциплинарные проекты, онбординг нового агента (FPF как системный промпт резко сокращает time-to-first-contribution), стратегирование, долгоживущие системы." [cite: B.6]

---

## Part 5 — Cross-block mapping (dependency grid)

Mapping which of the 8 manifest blocks references which alpha(s) and ritual(s). Derived strictly from Part C block definitions, D alpha definitions and E rituals; no enhancement.

| Block | Alphas referenced | Rituals referenced |
|-------|------------------|---------------------|
| **1. Identity** | — | Role manifest update (H.1) |
| **2. Ontological** | `primary-alpha` + `secondary-alphas` (any of D.1–D.10, typically D.1 Client, D.3 Deal, D.4 Invoice) | — (block feeds Strategizing via acceptance-criteria) |
| **3. Method** | (indirectly, via `quality_criteria` & `golden_examples`) | Thinking-by-writing (E.2) — `thinking_protocol` is a write-before-act step |
| **4. Graph of Creation** | All alphas whose artefacts flow between roles (D.1 Client → D.2 Project; D.3 Deal → D.4 Invoice; D.9 Research Note → D.5 Content Item; D.10 Postmortem) | — (feeds Weekly review "Get Current" alpha states table) |
| **5. Seniority / Scale** | D.3 Deal (escalation-trigger example "Deal > $50k"), D.1 Client (autonomous rights "Disqualify lead ICP < 40") | Стратегирование E.1 (split_trigger produces a strategizing session) |
| **6. Implementation AI** | — (but eval-dataset tests alpha transitions) | — (runs inside context engineering per F.3) |
| **7. Implementation Human** | D.1 Client (KPI "Pipeline conversion lead→closed-won"); D.2 Project (on-time delivery) | Onboarding path (4 steps); handoff_from_ai triggers |
| **8. Evolution** | — (versions the manifest itself as a meta-alpha "Role Manifest" per G.2) | Role manifest update cadence (H.1) + Quarterly letter "System Changes Made" section (E.2.c) |

### Alpha → Role (mover) mapping (derived from D-sections)

| Alpha | Primary mover role | Secondary movers |
|-------|-------------------|------------------|
| D.1 Client | sales-lead | inbox-processor, sales-research, delivery |
| D.2 Project | delivery | — |
| D.3 Deal/Contract | sales-lead (draft), system-admin (signed/active), manager (cancelled) | — |
| D.4 Invoice | system-admin | manager (disputes) |
| D.5 Content Item | knowledge-synth / delivery | — |
| D.6 Hypothesis | (UNDER-SPECIFIED — no explicit mover role named) | strategist (inferred from Part G.4) |
| D.7 SKU/Product | (UNDER-SPECIFIED — no explicit mover role named) | strategic-management (inferred) |
| D.8 Member (Alliance) | (UNDER-SPECIFIED) | — |
| D.9 Research Note | (UNDER-SPECIFIED — likely knowledge-synth) | — |
| D.10 Postmortem | (UNDER-SPECIFIED) | meta-agent (inferred from audit role) |

### Ritual → Block and Alpha mapping

| Ritual | Blocks that depend on it | Alphas it touches |
|--------|-------------------------|-------------------|
| E.1 Стратегирование | Block 2 (ontological → purpose), Block 5 (split_trigger), Block 8 (expected-evolution) | D.6 Hypothesis (direct); all alphas as "related-alphas" front-matter |
| E.2.a Daily log | Block 3 (thinking_protocol), Block 5 (decision log) | D.1 Client transitions ("alpha transitions today") |
| E.2.b Weekly review | Block 4 (consumes/produces reflected in "Get Current"), Block 5 (betting → decision-rights test) | All alphas (alpha states table) |
| E.2.c Quarterly letter | Block 8 (Evolution — "System Changes Made") | All alphas ("Alpha States Then vs Now") |
| E.3 Extract/propose agent pattern | Block 3 (Method — agent as critic), Block 6 (Implementation AI — tools-allowed) | — |
| H.1 Role manifest update | Block 8 (Evolution changelog) | Role Manifest as meta-alpha (G.2) |
| H.1 QA audit (meta-agent monthly) | Block 3 (anti_patterns), Block 6 (eval-dataset) | D.10 Postmortem |

---

## Flagged UNDER-SPECIFIED items

1. **Per-state acceptance criteria** for D.2–D.10 (only D.1 has full checklists). [D.2–D.10]
2. **Explicit mover role** for D.6 Hypothesis, D.7 SKU/Product, D.8 Member, D.9 Research Note, D.10 Postmortem (only prose hints, no transitions table as in D.1). [D.2–D.10]
3. **B.4 protocol for loading FPF into agent context** — B.4 gives the rationale ("большой системный промпт", manual vs fine-tuning, Software 3.0 delivery) but no step-by-step loading protocol, no context-budget allocation, no mandatory-vs-optional FPF sections list. Complementary operational guidance scattered in Parts F (F.3, F.4) and H (H.1 FPF-Lite). [B.4]
4. **`domains:` field in Block 2** — mentioned as Holacracy-style "что роль контролирует эксклюзивно" but no format spec (list? single value? URI?) and no example in the C.9 sales-lead filled manifest. [C.2]
5. **`agent_type:` enumeration in Block 6** — only example `claude-code`; no full enum. [C.6]
6. **Graph of Creation auto-generation format** — G.3 hints at `grep -r "produces:\|consumes:" | parse_to_dot` but no parser spec. [G.3]
7. **Sub-sections inside B.4** — B.4 is single-section; no B.4.1/B.4.2 decomposition. All operational detail for "FPF-for-AI" is spread across B.5, B.6, F.*, H.1.

---

**End of extraction.**
