---
research-id: R5
wave: 2
topic: CRM + sales tracking архитектура в git+markdown (solo AI-native → mega-corp)
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/crm-sales-architecture-deep-research-2026-04-19.md
priority: P1 (критично — блокирует часть D5 + D1 folder structure)
builds-on: R1, R2, R3 (уже получены)
---

# R5 — CRM + Sales Tracking архитектура для AI-native Jetix

## Зачем этот research

У Jetix будет клиентский поток (B2B Mittelstand), но пока **нет системы** где жить:
- Leads / prospects / clients
- Deals (scoped → signed → active → closed)
- Contracts / SOWs
- Invoices / receipts
- Communications (emails, calls, meetings)
- Relationships (partners, advisors, IHK members)

**Классический путь** — HubSpot / Salesforce / Pipedrive. **Проблема:** ломает company-as-code ethos, vendor lock-in, не интегрируется с wiki/role-framework.

**Нужен research:** как построить **markdown-based CRM + sales tracking** который:
- Живёт в git-репозитории (version control, diff, rollback)
- Интегрируется с 10 core alphas (R3) — Client / Deal / Invoice / Member
- Интегрируется с existing wiki (R4 будет)
- Поддерживает scale до hundreds of clients без rebuild
- Имеет migration path на HubSpot/Salesforce когда нужно (Phase 2/3)

Выход research'а — input для D5 (часть про CRM/sales storage) и детализация folder structure.

## Как использовать

Скопируй между `=== PROMPT START ===` и `=== PROMPT END ===` и вставь в Perplexity Max Computer. Собственная вкладка.

---

=== PROMPT START ===

Ты — senior architect по CRM systems, sales operations, и data architecture. Я прошу **глубокий академический research** по теме: **как построить markdown-based CRM и sales tracking систему для AI-native компании под git-репозиторием, с поддержкой роста solo → team → mega-corporation**.

Это specific integration research — у нас уже есть git-monorepo подход, concept of alphas (lifecycle entities), и clear need для structured sales data. Нужны конкретные patterns, а не generic CRM обзор.

## Контекст проекта Jetix (2000 слов)

**Jetix** — AI-native mega-corporation одного founder (Ruslan, Берлин) + 12+ AI-агентов через Claude Code. Target: немецкий Mittelstand (manufacturing/services 50-500 employees, €10-500M revenue). Цель Q2 2026: €50K revenue.

**Архитектура Jetix:** 7 слоёв (L1 Foundation → L7 Portfolio) + L0 Executive Core. Nested hierarchy: Life-OS = root, Jetix = один из проектов. Company-as-code философия — всё в git-monorepo в markdown+YAML.

**Утверждённые решения из Wave 1:**

**R3 (Левенчук) утвердил 10 core alphas** — lifecycle entities с состояниями:
1. **Client** — lead → qualified → proposed → negotiating → closed-won/lost → churned
2. **Project** — scoped → kicked-off → in-progress → delivery → closed → follow-up
3. **Deal/Contract** — draft → signed → active → completed/cancelled
4. **Invoice** — issued → sent → paid → reconciled/disputed
5. **Content Item**, **Hypothesis**, **SKU**, **Member (Alliance)**, **Research Note**, **Postmortem**

**R2 (Company-as-code) утвердил:**
- Git + markdown + YAML = база данных
- Folder structure draft с `clients/<name>.md` возможным местом
- Stripe billing integration (для L3 SaaS subscriptions)
- Cal.com для scheduling

**R1 (Career levels) дал:** sales-lead (Senior, decision-rights: квалификация, discount до 10%), sales-research (Junior), sales-outreach (Junior) роли.

## Business модель Jetix L4 Delivery (чтобы понять что трекаем)

**4 SKU-шаблона:**
- **AI Readiness Audit** €5-8K, 2 недели — entry product (Trojan Horse)
- **Quick Win Automation** €10-15K, 4 недели — one process automated
- **Custom Agent Build** €25-40K, 8-12 недель — premium
- **Operations Retainer** €3-5K/mo — recurring (MRR через L4, не L3)

**Sales cycle DACH:**
- 6-12 недель Konsenskultur (CFO + IT-Leiter + Geschäftsführer)
- Discovery call → AI Audit proposal → signed → delivery → upsell
- Sources: LinkedIn outreach, IHK/VDMA networks, Antoh referrals, newsletter
- **Pipeline ICP:** Mittelstand manufacturing 50-500 employees, DACH

**Data что нужно трекать:**
- **Lead:** source, first contact, ICP match
- **Contact person:** name, role (Geschäftsführer/CFO/IT-Leiter), email, LinkedIn, phone
- **Company:** name, size, industry, revenue estimate, location
- **Deal:** stage, value, probability, expected close date, competitor
- **Activities:** emails, calls, meetings, proposals sent, contracts signed
- **Communications history:** полный thread
- **Contracts/SOWs:** signed documents
- **Invoices:** issued, paid status, reconciliation
- **Relationships:** connections, referrals, introductions

**Wave 2 partner research (параллельно):**
- R4 — Knowledge architecture (wiki + alphas integration)
- R6 — Folder structure (scale-up patterns)
- R7 — Jetix vs Life-OS separation

## Ключевой вопрос

Как spec'ить CRM + sales tracking так, чтобы:

1. **Каждый lead / client / deal / invoice** = markdown/YAML файл в git (version-controlled, diff-able, scriptable)
2. **Alpha state transitions** tracked cleanly (git commits или alpha-log)
3. **Communications history** сохранён (emails, call notes)
4. **Query performance** приемлема (поиск «all deals > €10K in last quarter» fast)
5. **AI-agents могут работать** с CRM данными (sales-lead agent видит pipeline, analyst делает reports)
6. **Migration path к HubSpot/Salesforce** когда team scale (не lock-in в git-only)
7. **GDPR compliance** (client data handling в EU context)

## Основной research-запрос

### Часть A — Markdown-based CRM: existing patterns (SOTA 2024-2026)

1. **Obsidian CRM patterns** — community approaches:
   - Obsidian + Dataview plugin для queries
   - Obsidian + Canvas для pipeline visualization
   - Person / Company / Deal linked notes pattern
   - Tools: PKM CRM templates, Breadcrumbs plugin

2. **Logseq для CRM** — block-based approach, properties, queries. Advantages/limitations.

3. **Notion as CRM** — hybrid (structured DB + markdown). Many teams start here. Why fails at scale (vendor lock-in, API limits, performance).

4. **Monica CRM** — personal relationship manager, open-source, self-hostable. Architecture. What Jetix can learn.

5. **Krayin CRM / EspoCRM** — open-source enterprise CRM. PostgreSQL-based. Лerning for data model.

6. **Markdown frontmatter patterns** — YAML frontmatter для structured data в markdown files. Examples из обscure but effective implementations.

7. **Git as database patterns:**
   - Irmin (Git-like database by Tarides)
   - dolt (Git for data)
   - dbt seeds в git
   - Lessons applicable для CRM data

8. **Jupyter notebooks as CRM** — для data-heavy teams (analyst-focused). Not Jetix primary, but noted.

Источники: Obsidian forum (CRM templates), Logseq discourse, EspoCRM/Krayin docs, Monica documentation, dolt.io blog, Tarides Irmin papers. r/ObsidianMD community showcases.

### Часть B — Data model для markdown-based CRM

Glubокое проектирование.

1. **Entity types:**
   - **Company** — organization entity
   - **Contact** — person (belongs to Company)
   - **Lead** — pre-client contact
   - **Deal/Opportunity** — sales transaction in progress
   - **Contract/SOW** — signed agreement
   - **Invoice** — billing item
   - **Activity** — email/call/meeting (связь с deal)
   - **Task** — follow-up action items

2. **Relationships:**
   - Company ←→ Contacts (1:N)
   - Contact ←→ Deals (N:M usually one primary)
   - Deal ←→ Activities (1:N)
   - Deal ←→ Contract (1:1)
   - Contract ←→ Invoices (1:N)
   - Как represent в markdown + wikilinks + YAML references

3. **YAML frontmatter schemas:**
   - Concrete YAML schema для каждого entity
   - Required vs optional fields
   - Validation (JSON Schema via yq / jq?)

4. **File naming conventions:**
   - `clients/companies/acme-gmbh.md`
   - `clients/contacts/hans-schmidt.md`
   - `clients/deals/2026-04-19-acme-audit.md`
   - Date-prefix for deals, slug-based for companies
   - Comparison patterns

5. **Dynamic data (frequent changes):**
   - Deal stage changes каждые несколько дней
   - Activity log grows daily
   - Invoice paid/unpaid
   - Как handle — append-only log? separate activity.jsonl? git commit history?

6. **Static data (rare changes):**
   - Company profile, ICP analysis
   - Contact person details
   - Single source of truth pattern

### Часть C — State transitions и event sourcing

1. **Alpha state tracking:**
   - R3 proposed: git commit с tag `[alpha:client:acme][state:proposal→active]`
   - Альтернативы: dedicated `alpha-log.jsonl` event stream
   - events.jsonl pattern from event-sourcing

2. **Event sourcing для CRM:**
   - Append-only event log
   - Current state derived from events (projection)
   - Benefits: full audit trail, time-travel queries, immutability
   - Costs: complexity, re-projection on schema changes

3. **Event types для Jetix CRM:**
   - `lead.created`, `lead.qualified`, `lead.disqualified`
   - `deal.created`, `deal.stage-changed`, `deal.won`, `deal.lost`
   - `contact.added`, `contact.role-changed`, `contact.moved-company`
   - `contract.signed`, `contract.amended`, `contract.completed`
   - `invoice.issued`, `invoice.sent`, `invoice.paid`, `invoice.disputed`
   - `activity.logged` (email/call/meeting)

4. **Projection patterns:**
   - Current pipeline view (all active deals)
   - Client history (all events for one client)
   - Revenue reports (from invoice events)
   - As files regenerated from events

5. **Reversibility:**
   - Git log rewinding
   - Event replay from date X
   - What если event был wrong (correct via compensating event)

Источники: Martin Kleppmann «Designing Data-Intensive Applications» (event sourcing chapter), Greg Young's event sourcing articles, Martin Fowler's event sourcing/CQRS patterns. 

### Часть D — Communications tracking

Critical для B2B sales где cycle 6-12 weeks and тысячи emails/calls.

1. **Email integration:**
   - Как сохранять emails в git (safely, GDPR)
   - Plain-text archival (mbox, maildir formats)
   - Attachment handling (binary in git = bad)
   - Alternatives: separate email storage + references в CRM

2. **Meeting notes:**
   - Structured template (T-xx for meetings)
   - Audio recording → transcript (existing Jetix voice-memo pipeline)
   - Link meetings to deals/contacts
   - Search across meeting notes

3. **Call logs:**
   - Short notes after each call
   - Phone + Zoom/Google Meet integration
   - Auto-transcription (Otter.ai, Fireflies)

4. **LinkedIn messages** — export + import patterns. LinkedIn data ownership.

5. **Thread continuity** — как показать полную conversation history с одним контактом (cross-channel).

### Часть E — Contract / SOW / Invoice management

1. **Contract templates:**
   - Markdown-based contracts (Pandoc to PDF?)
   - Legal review patterns
   - Version control (signed version immutable)
   - Digital signatures (DocuSign / HelloSign integration)

2. **SOW (Statement of Work) specifics:**
   - Scope definition + change order process (R2 reference)
   - Scope creep protection
   - Template для AI Audit / Quick Win / Custom / Retainer

3. **Invoicing:**
   - Stripe Billing integration (existing Jetix plan)
   - FreeAgent / Xero API для accounting
   - German Rechnung requirements (Steuernummer, USt-ID, mandatory fields)
   - Sequential numbering (legal requirement)

4. **Payment reconciliation:**
   - Bank statement import
   - Match payments to invoices
   - Partial payments / credits

5. **Accounting integration:**
   - Jahresabschluss preparation
   - VAT handling (19% Germany, cross-EU rules)
   - Export для Steuerberater

### Часть F — Query и reporting patterns

1. **Simple grep queries:**
   - `grep -r "status: active" clients/deals/`
   - `find clients/deals/ -newer 30 days`
   - Limits at scale

2. **Dataview-like queries для markdown:**
   - Obsidian Dataview plugin patterns
   - jq для YAML queries
   - Custom scripts (Python + PyYAML)

3. **DuckDB over markdown frontmatter:**
   - `SELECT * FROM 'clients/**/*.md' WHERE status='active'` — R2 mentioned
   - Feasibility, performance, practical examples

4. **Reporting:**
   - Weekly pipeline report (active deals, stuck deals)
   - Monthly revenue (from invoices)
   - Quarterly win/loss analysis
   - Automated generation (GitHub Actions + cron)

5. **Dashboards:**
   - Static markdown dashboard auto-updated
   - Obsidian Dataview dashboard
   - Minimal web-UI (if needed)

### Часть G — AI-agent integration

1. **sales-research agent** — задачи, access patterns:
   - Чтение target company info из wiki + public sources
   - Writing новый `clients/companies/<name>.md`
   - Tools: WebFetch, wiki ingestion

2. **sales-lead agent:**
   - Чтение current pipeline (`clients/deals/*`)
   - Обновление deal stages
   - Generation proposal (from SOW template)
   - Decision-rights matrix (R1): discount до 10% OK, выше — escalate

3. **sales-outreach agent:**
   - Read contact profile + company info
   - Generate personalized message (LinkedIn template + customization)
   - Log activity после send

4. **analyst agent:**
   - Read pipeline data
   - Generate reports (win/loss analysis, CAC estimation)
   - Produce insights from client history

5. **Agent context loading:**
   - Sales agent нужен какой context перед task
   - Pipeline snapshot + relevant company info + past activities
   - Budget: не перегружать context window

### Часть H — Scale: solo → 100 clients → 1000

1. **Current solo (0-20 clients):**
   - Pure git + markdown works fine
   - grep-based queries adequate

2. **Team phase (20-100 clients):**
   - Multiple writers — merge conflict risks
   - Need proper index (DuckDB или similar)
   - Notion или Airtable as read-only view

3. **Scale phase (100-1000 clients):**
   - HubSpot / Pipedrive / Salesforce migration
   - Но keep audit trail в git (snapshot import)
   - Bi-directional sync patterns

4. **Mega-corp phase (1000+ clients):**
   - Proper CRM mandatory
   - Git retains only decisions, strategic context
   - Data warehouse integration

5. **Migration patterns:**
   - Когда перейти (triggers: client count, team size, query complexity)
   - Как migrate (CSV export → CRM import)
   - Что keep в git даже после migration

6. **Multi-product scaling:**
   - Когда L4 delivery + L3 Jetix Club + L5 Alliance каждый имеет свою «CRM-like» — как keep separated

### Часть I — GDPR и compliance

1. **GDPR requirements для CRM data:**
   - Consent tracking
   - Right to be forgotten (problematic с append-only git!)
   - Data minimization
   - Lawful basis для processing

2. **Data in git - particular challenges:**
   - Git history almost impossible to fully delete
   - BFG repo cleaner
   - Separate sensitive data (emails, attachments) from git

3. **Encryption at rest:**
   - SOPS + age patterns (R2 recommendation)
   - Selective encryption (sensitive fields only)
   - Separate secrets repo?

4. **Access control:**
   - Future team: who sees all clients, who sees только свои
   - Git access controls limited
   - When need proper RBAC (move to CRM)

5. **Audit trail:**
   - Git log gives free audit
   - But git log itself contains data (commit messages)
   - Periodic review / rotation

### Часть J — Практические выходы для Jetix

**Самая важная часть.**

1. **Полная folder structure для clients/sales area:**
   ```
   clients/
   ├── companies/
   │   └── <slug>.md           # Company profile
   ├── contacts/
   │   └── <slug>.md           # Person profile
   ├── leads/
   │   └── <slug>.md           # Pre-client
   ├── deals/
   │   └── YYYY-MM-DD-<slug>.md # Deal / opportunity
   ├── activities/
   │   └── YYYY-MM-DD-<slug>.md # Email / call / meeting log
   ├── contracts/
   │   ├── drafts/
   │   ├── signed/
   │   └── templates/
   └── invoices/
       └── YYYY/<number>.md    # Sequential numbering
   
   sales/
   ├── pipeline.md              # Current pipeline snapshot
   ├── reports/
   │   └── YYYY-Www-weekly.md
   └── playbooks/               # Outreach templates
   ```

2. **Полный YAML frontmatter schema** для каждого entity type (copy-paste ready).

3. **Example filled files** для first test case:
   - `clients/companies/test-gmbh.md`
   - `clients/contacts/hans-mueller.md`
   - `clients/deals/2026-04-20-test-audit.md`
   - `clients/activities/2026-04-20-discovery-call.md`

4. **Event-sourcing decision** — использовать или нет?
   - Если да — `events.jsonl` или `alpha-log/` схема
   - Если нет — почему git commits sufficient

5. **Communications pattern** — где хранить emails, meeting notes, LinkedIn messages.

6. **Contract workflow** — template → draft → review → signed (DocuSign) → stored в git.

7. **Invoicing pattern** — Stripe Billing + FreeAgent + German legal requirements.

8. **Agent decision tree** — «когда sales-lead agent читает что»:
   - Task arrives → читает role-manifest + current pipeline summary
   - Nie читает: full history всех клиентов (context explosion)
   - Always читает: active deal summary

9. **Query cookbook** — 10 common queries для Jetix:
   - All active deals > €10K
   - Deals stuck in negotiation > 14 days
   - Clients без активности > 30 days
   - Revenue this quarter
   - Pipeline value by stage
   - и т.д., с примерами grep/jq/DuckDB

10. **Migration triggers:**
    - 50 active deals → add Dataview-like querying
    - 100 clients → consider HubSpot sync
    - 300 clients / multi-user → mandatory CRM migration

11. **Anti-patterns specific Jetix:**
    - Storing emails as git blobs (BFG horror)
    - Notion as source of truth (не компатибельно с company-as-code)
    - Over-engineering events для 5 deals
    - Under-engineering (everything in one file, unsearchable)

## Format требования

- **Объём:** 5000-10000 слов
- **Format:** Markdown, Parts A-J
- **Citations:** primary (Kleppmann book, event-sourcing papers, Obsidian community, Monica/EspoCRM docs)
- **YAML code examples** везде где релевантно
- **German specifics** (Rechnung, Steuernummer, GDPR)
- **Tables** для comparisons

## Anti-patterns

- ❌ Generic «Salesforce vs HubSpot» comparison (мы не туда ещё)
- ❌ Над-complexity (event sourcing для 5 deals)
- ❌ Игнор GDPR
- ❌ Без Part J (practical Jetix output)
- ❌ Ignoring existing Jetix stack (git + Claude Code + wiki)

## Критерий успеха

На основе research я могу:
1. Написать `design/JETIX-KNOWLEDGE-ARCHITECTURE.md` (D5) часть про CRM/sales
2. Создать `clients/` folder structure + first test company
3. Spec agent context loading для sales roles
4. Define migration triggers
5. Establish GDPR-compliant patterns with Day 1

Приступай. Академично, с German specifics, Part J actionable.

=== PROMPT END ===

---

## Notes для Ruslan

**Output file:** `raw/research/crm-sales-architecture-deep-research-2026-04-19.md`

**Параллельно с R4, R6, R7.**
