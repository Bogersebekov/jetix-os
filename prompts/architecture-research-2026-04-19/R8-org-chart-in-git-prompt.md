---
research-id: R8
wave: 3
topic: Org-chart-in-Git — компания как software artefact, version-controlled organizational structure
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/org-chart-in-git-deep-research-2026-04-19.md
priority: P1 (критично — блокирует Тезис 5 позиционирования + advanced L0 patterns)
builds-on: R1-R7 (все предыдущие)
---

# R8 — Org-chart-in-Git: компания как software artefact

## Зачем этот research

Тезис 5 архитектуры Jetix (approved, развёрнут):

> «Роли = организационная структура в Git, а не в HR-системе. Компания становится software artefact, а не legal+HR+tribal-knowledge конструкция.»

**Это может быть флагман positioning Jetix.** Но концепт требует **deep implementation spec**. Существующие примеры (GitLab handbook, Holacracy Constitution) — частичные. Нам нужно:

1. **Academic framework** для «organization as code» — формальная теория
2. **Полная existing practice map** — все серьёзные примеры с детальным анализом
3. **Technical implementation patterns** — как именно версионировать org chart
4. **Automated governance** — lint rules, policy enforcement, drift detection
5. **Org diff tools** — comparing orgs across time и across companies
6. **Open-source orgs** — licensing frameworks, transferability (связь с hybrid-framework vision)
7. **A/B testing структур** — branch experimental orgs
8. **Constitutional layer** — how invariants live in git, how changes are governed

Выход — critical input для D1 Architecture Final + positioning narrative + advanced L0 patterns + future L6 transferability когда Jetix framework licensable другим solo-operators.

## Как использовать

Скопируй **всё между `=== PROMPT START ===` и `=== PROMPT END ===`** и вставь в Perplexity Max Computer. Собственная вкладка, параллельно с R9.

---

=== PROMPT START ===

Ты — senior research analyst специализирующийся на organizational design, software engineering architecture patterns, и эволюции корпоративных forms в AI-эпохе. Я прошу **глубокий академический research** по теме: **«Компания как software artefact» — organizational structure, которая полностью живёт в git-репозитории как версионируемый код, а не в HR-системах и tribal knowledge**.

Это fundamental research — концепт зафиксирован, теперь нужна academic foundation и production implementation.

## Контекст проекта Jetix (2500 слов)

**Jetix** — AI-native mega-corporation одного founder (Ruslan, Берлин) + 12+ AI-агентов через Claude Code (Anthropic Opus 4.7, 1M context). Target market — немецкий Mittelstand. Цель Q2 2026: €50K revenue.

**Архитектура Jetix** — 7 слоёв + L0 Executive Core (утверждено):
- L0 Executive Core: Ruslan + AI-агенты + future human executors через **единую role-abstraction**
- L1 Foundation: Git + markdown + YAML, prompt-as-code, CI/CD, docs-as-code, postmortems
- L2 Cognitive: Левенчук / ШСМ (роль, альфа, граф создания, стратегирование, мышление письмом)
- L3 Product / L4 Delivery / L5 Membrane / L6 Topology / L7 Portfolio

**Nested hierarchy:** Life-OS = root, Jetix = один из проектов Life-OS с полной 7-слойной архитектурой внутри. Полное разделение ресурсов.

**Scale-up-first:** при 10x росте (капитала, часов, людей, проектов, ролей) — без rebuild.

**Principle:** Роль ≠ исполнитель. Role-manifest — абстрактный контракт. AI-агент сегодня или human завтра — меняется executor, не роль.

## Ключевой философский тезис (Тезис 5 архитектуры Jetix)

> «Агенты и роли = организационная структура, живущая в Git, а не в HR-системе. Это фундаментальный сдвиг в том, что такое компания. Org chart = файлы в git-репозитории. Это первая в истории architecture-pattern где company это software artefact, не legal-plus-HR-plus-tribal-knowledge конструкция.»

**Развёрнутые возможности (approved):**

1. **Transparency** — вся структура в 1 месте, diff-abilityi, читаемо любым agent'ом или человеком
2. **Rollback** — ошибочные org-changes откатываются через `git revert`
3. **Version control на уровне организации** — честно compare «Jetix Q2 2026» vs «Jetix Q4 2027»
4. **Transferability** — org chart как fork-able template (связь с hybrid-framework vision — licensing methodology другим solo-operators)
5. **AI-native governance** — агенты читают role-manifests напрямую, не через tribal knowledge
6. **Refactorable org** — extract role, inline, rename, move, split (как code)

**Новые use-cases:**

- **Automated org health checks** — lint rules (no orphan-roles, no duplicate responsibilities, единственная accountability per alpha)
- **Org diff** между компаниями — comparative analysis Jetix vs MBB-firm vs Mittelstand GmbH
- **Open-source org charts** — fork + adapt как open-source projects
- **A/B testing** структур — branch A vs branch B, run both, merge winner
- **Org как learning artifact** — new executor читает `git log org/` как обучающий курс
- **Constitutional layer** — invariants (§11 tech-doc) в git, change → visible impact

**Мета-мысль:** компания становится принципиально иным объектом — auditable, refactorable, transferable, open-source-able, A/B-testable. Это **concrete operational advantage AI-эры**.

## Wave 1 + Wave 2 findings для контекста

**R1 (Career Levels):** J1-J5 + JX ladder, role-manifest YAML template, decision-rights matrix, phase transitions (solo → team → mega-corp), 10-year view 2035.

**R2 (Company-as-code):** 8 reference cases (GitLab handbook, Holacracy Constitution, Valve, Spotify, Shape Up, Stripe, Linear, Oxide RFD). Folder structure draft с `roles/` vs `executors/` split. 14-day rollout. Tools: Promptfoo, Langfuse, SOPS+age, MkDocs Material, just, Oxide RFD.

**R3 (Левенчук/ШСМ для AI):** 5 примитивов (роль, альфа, граф создания, стратегирование, мышление письмом). FPF-Lite draft. Role-manifest 8-block structure. 10 core alphas. Metric FPAR (First-Pass Acceptance Rate).

**R4-R7 (Wave 2):** Knowledge architecture (HippoRAG + alpha integration), CRM+sales markdown-based, folder structure stress-tested, Jetix vs Life-OS separation.

## Ключевые вопросы этого research

1. **Academic framework** — существует ли формальная теория organization-as-artefact? Organizational ontology, computational organization theory, digital twins corporations?

2. **Full existing practice map** — все серьёзные компании с org-as-git + academic experimental cases. Что точно получилось, что провалилось.

3. **Technical implementation** — как **конкретно** версионировать org chart: formats, schemas, relationships, visualization, query patterns.

4. **Automated org policy** — lint rules, compliance checks, drift detection. Tools, patterns.

5. **Diff algorithms** для orgs — сравнение structures across time и across companies. Similarity metrics.

6. **Open-source methodology** — Holacracy Foundation licensed Constitution. Other examples. Transferability patterns. Legal implications.

7. **A/B testing org structures** — experimental orgs в branches. Measurement. Selection criteria.

8. **AI-native governance** — когда AI agents это first-class org chart entities. How versioning works for AI roles.

9. **Constitutional layer** — invariants, policies, meta-rules в git. Change governance.

10. **Tooling ecosystem** — что существует, что нужно построить для Jetix.

## Основной research-запрос

### Часть A — Academic foundation: organization as artefact

1. **Organizational ontology** — formal study. John Dijkman «Ontology of Organizations» (ISSOO). Peter Suchman «Managing Legitimacy».

2. **Computational organization theory** — Kathleen Carley (CMU). Studies of org structure simulation. Multi-agent organizational modeling.

3. **Digital twins corporations** — 2020-2025 research. AI-driven org design. IBM / Accenture research reports.

4. **Holacracy formal theory** — Brian Robertson «Holacracy: The New Management System» (2015). Core constructs: circles, roles, tactical/governance meetings, tensions.

5. **Sociocracy** (Gerard Endenburg) — consent-based governance, circles, double-linking. Academic sources.

6. **Agile organization** — Frederic Laloux «Reinventing Organizations» (2014). Teal organizations. Holacracy vs Sociocracy vs Teal comparison.

7. **Formal organizational models** — Mintzberg's structural configurations (Simple/Machine/Professional/Divisional/Innovative). Classical frameworks.

8. **Enterprise Architecture frameworks** — TOGAF, Zachman, ArchiMate — как они treat org structure as formal artifact.

9. **Organizational Learning** — Chris Argyris, Peter Senge «The Fifth Discipline». Knowledge-as-artefact continuum.

10. **Constitution theory** — political and organizational. Federalist Papers. Corporate bylaws tradition.

Источники: Holacracy.org (formal constitution + theory papers), Harvard Business Review, MIT Sloan Management Review, Journal of Organizational Design. Kathleen Carley CMU publications. Frederic Laloux book + Teal Organizations community.

### Часть B — Existing practice map (serious implementations)

For each — deep analysis including what works, what doesn't, lessons applicable to Jetix.

1. **GitLab Handbook** ([about.gitlab.com/handbook](https://about.gitlab.com/handbook)) — самый полный public example. 2000+ страниц, edited via MR. Repository structure. How engineering / security / marketing / finance organized. DRI (Directly Responsible Individual) model. Metrics обновления. Critique — scales issues, hanбуbооk сaturation.

2. **Holacracy Constitution** on GitHub ([github.com/holacracyone/Holacracy-Constitution](https://github.com/holacracyone/Holacracy-Constitution)) — v5.0 current. 417 stars. Markdown + version tagging. Companies that adopted (Zappos full migration then partial rollback, Medium's adoption then abandonment). Holacracyone commercial implementation.

3. **Valve Employee Handbook** — 56-page PDF, no technical implementation, но ideological foundation для flat orgs.

4. **Oxide Computer RFD process** ([rfd.shared.oxide.computer](https://rfd.shared.oxide.computer)) — Requests for Discussion как codified decision-making. Covers tech + business + operational. Lifecycle states. GitHub-based.

5. **Artsy Engineering** public principles — Artsy's open engineering handbook. Smaller scale.

6. **Basecamp / 37signals** Shape Up + handbook. David Heinemeier Hansson approach.

7. **Linear Method** — public methodology documents.

8. **Mozilla Project** — historical org-as-openness (Project Statement, Governance Model).

9. **Cloudflare / Vercel / Stripe** — public posts об org structures, но handbooks не open.

10. **Chinese tech** (Alibaba, ByteDance) — partial public org documentation.

11. **Academic / Research orgs:**
    - **Mozilla Foundation** governance
    - **Wikimedia Foundation** governance — very public, board-structured, community-governed
    - **Apache Software Foundation** — PMC structures, meritocracy patterns
    - **Linux Foundation** — how they publish governance

12. **Historical examples:**
    - **U.S. Constitution** as versioned artefact (amendments как commits)
    - **Rule of St. Benedict** (529 AD) — одна из oldest org constitutions, still maintained
    - **Jesuit Constitutions** (Ignatius of Loyola 1540s) — still-living org document

13. **DAOs (Decentralized Autonomous Organizations):**
    - **Moloch DAO** — governance docs on GitHub
    - **Compound Protocol** governance
    - **Aragon** DAO framework — org-as-smart-contracts
    - **Colony.io** — formal DAO structures

14. **Internal Anthropic, OpenAI** public info about org structures (if any).

Составь comparative table с критериями: scale (people), public access, format (Markdown/PDF/Wiki), version control (git/none), governance mechanism, AI integration, adopted outside.

### Часть C — Technical implementation patterns

Core deep-dive: **как precisely версионировать org chart в git**.

1. **File formats:**
   - Pure Markdown (.md) with frontmatter
   - YAML schemas
   - JSON with schema validation
   - Dhall (configuration language)
   - Cue (configuration + validation)
   - TOML
   - Hybrid approaches
   - Comparison table: validity checking, human-readability, tooling, git-diffability

2. **Entity schemas:**
   - Role entity: name, purpose, accountabilities, domains, decision-rights
   - Executor entity: person/agent, assigned roles, skills, availability
   - Team/Circle: roles, parent/child, coordination patterns
   - Process/Ritual: cadence, participants, artefacts
   - Alpha: lifecycle state, ownership, dependencies
   - Что стандартизовать, что free-form

3. **Relationships representation:**
   - Hard links (file paths)
   - Soft references (by ID/name)
   - Graph data (edges.jsonl)
   - Wikilinks (Obsidian-style [[Role Name]])
   - Когда какой pattern

4. **Directory structure options:**
   - Flat (all roles в `roles/`)
   - By department (`roles/sales/`, `roles/engineering/`)
   - By layer (`roles/L4-delivery/`, `roles/L7-portfolio/`)
   - By seniority (`roles/senior/`, `roles/junior/`)
   - Comparison

5. **Naming conventions** (R6 uses this, углубить specifically for orgs):
   - kebab-case for files
   - Role uniqueness guarantees
   - Historical stability (don't rename role even if function changes)

6. **Version control patterns:**
   - Tags для major org version (org-v1.0, org-v2.0)
   - Branches для experimental structures
   - Semantic versioning for org (MAJOR/MINOR/PATCH)
   - How to handle CHANGELOG for org

7. **Metadata & provenance:**
   - Who created role, when, why (git log gives free)
   - Creating explicit provenance fields?
   - Effective date tracking (role exists from X date)
   - Deprecation tracking

Источники: Holacracy Constitution structure (GitHub repo анализ), GitLab handbook directory structure, Oxide RFD format. Dhall / Cue documentation for typed configs. GraphDB representations.

### Часть D — Version control patterns для organization

Это углубление git-flow-based thinking для org changes.

1. **Change types:**
   - PATCH: clarification, typo, minor accountability edit
   - MINOR: new role, new responsibility, new executor
   - MAJOR: eliminate role, merge roles, fundamental restructuring

2. **Branch strategies:**
   - main = current org
   - future/* branches = planned changes (upcoming promotion, hire)
   - experimental/* = A/B tested structures
   - archive/* = historical orgs preserved separately

3. **Merge patterns:**
   - Squash (clean history)
   - Merge commits (preserve branch structure)
   - Rebase (linear history)
   - Trade-offs

4. **Tagging patterns:**
   - org/2026-Q2 (quarterly snapshots)
   - org/pre-first-hire, org/post-first-hire (event-based)
   - org/v1.0.0 (SemVer)

5. **Release cycles для orgs:**
   - Weekly "pulls" (small changes)
   - Monthly "releases" (big structural)
   - Quarterly "major versions"
   - Annual "SemVer majors"

6. **Commit message conventions:**
   - `org(roles/sales-lead): promote to J3`
   - `org(structure): merge sales-research and sales-outreach into sales-team`
   - Standard taxonomy (add/remove/rename/restructure)

7. **Atomic commits:**
   - One role change per commit (readability)
   - Or batch related (promotion + new hire + responsibility transfer)

8. **Reviewing org changes:**
   - Who reviews (currently Ruslan solo; later — C-level)
   - What signals review needed (significant change → PR not direct commit)
   - Review checklist

### Часть E — Automated org health checks

Это где tools become important.

1. **Lint rules для org:**
   - No orphan roles (role без executor, не archived)
   - No duplicate responsibilities (two roles own same accountability)
   - No unassigned alphas (every alpha has one accountable role)
   - No circular reporting (A → B → A infinite)
   - Every role has at least one KPI
   - Every role has defined decision-rights
   - Every role has reporting-to
   - Manager span of control ≤ X (e.g., 8 direct reports)

2. **Static analyzers:**
   - Custom scripts (Python parse frontmatter)
   - JSON Schema validation для YAML
   - Promql-style queries over repo
   - Tools that work for policy-as-code (Open Policy Agent, Rego)

3. **Drift detection:**
   - Role exists в git but no recent executor activity
   - Executor has activity but role never reviewed
   - Accountabilities defined but никто не tracks metrics

4. **Compliance checks:**
   - GDPR: personal data in right places
   - Legal accountability: who is formally Geschäftsführer, registered?
   - Who signed what contracts (liability tracking)

5. **Executable documentation:**
   - CI runs org-lint on every commit
   - PR blocked if lint fails
   - Metrics dashboard from org analysis

6. **Policy evolution tracking:**
   - When rule added, why
   - When rule relaxed, why
   - Historical audit

Источники: Open Policy Agent (OPA), Rego language, policy-as-code papers. GitLab handbook linting practices (если exist). Apache Fluent Docs approach.

### Часть F — Org diff + comparative analysis

Новый domain — сравнение orgs.

1. **Simple git diff patterns:**
   - `git diff org/2026-Q2 org/2026-Q4` — what changed
   - Readable diffs для org structures (not just file-level)

2. **Cross-company comparison:**
   - Jetix org vs MBB-firm org (extracted from public data)
   - Jetix org vs manufacturing Mittelstand
   - Jetix org vs tech startup
   - Structural similarity metrics

3. **Tree-edit distance** для org structures — academic approach. Когда полезно.

4. **Graph similarity** — if orgs represented as graphs. Similarity measures.

5. **Evolution visualization:**
   - Timeline view of org changes
   - «Growth tree» visualization
   - D3.js, Observable notebooks

6. **Org fingerprinting:**
   - Identify org patterns (hierarchical vs flat vs matrix)
   - Style classification
   - Cultural indicators

7. **Benchmark databases:**
   - Anthropic / OpenAI / Cursor public info
   - Build Jetix benchmark dataset

### Часть G — Open-source orgs + transferability

Критично для Jetix vision (hybrid-framework licensable).

1. **Licensing models:**
   - MIT / CC-BY для org documents (permissive)
   - AGPL для systems that include org
   - CC-BY-SA (copyleft) для methodology
   - Custom licenses (Holacracy Creative Commons)

2. **Transferability patterns:**
   - Fork + adapt (most common, OSS-style)
   - License + support (commercial model)
   - Community standard (Holacracy Foundation model)
   - Franchise model (McDonald's-style но для methodology)

3. **Jetix framework distribution:**
   - Open-source repo template
   - `jetix-framework` that anyone can fork
   - Template для solo-operator starting новый AI-native business
   - Revenue streams (consulting, certification, tooling)

4. **Legal implications:**
   - Trademarks (Jetix как brand)
   - Patent considerations
   - Copyright in org documents
   - EU vs US legal differences

5. **Community governance модели:**
   - Apache Software Foundation (PMC-based)
   - Linux Foundation (fee-based membership)
   - OpenJS Foundation
   - Creative Commons (nonprofit fiscal host)
   - Какая подходит для Jetix framework

6. **Certification programs:**
   - «Certified Jetix Practitioner» — possible future
   - How to design certification
   - Examples из Holacracy (Certified Coach), Scrum.org (PSM)

### Часть H — AI-native governance

Это где org-as-artefact becomes uniquely AI-era.

1. **AI agents как first-class org entities:**
   - Claude-sales-lead в executors/ как human would be
   - Role-manifest одинаково applies
   - Performance review = prompt eval scores
   - Promotion = expanded decision-rights (role-manifest edit)

2. **Automated compliance for AI:**
   - Agent обязательно проверяет org rules перед acting
   - Policy-as-code enforces constraints
   - Audit trail для each agent action

3. **Evolutionary org design:**
   - AI proposes org changes (meta-agent)
   - Human approves
   - A/B test in branch
   - Merge если better

4. **Self-modifying org (limits):**
   - Agents can edit own role manifests?
   - Boundaries (what agents cannot change)
   - Human checkpoint для major changes

5. **AI-driven org analytics:**
   - Load balancing across roles
   - Predict bottlenecks
   - Suggest restructuring
   - Anthropic's internal research on agent team dynamics

6. **Multi-agent coordination в org:**
   - Message-passing via comms/mailboxes (existing Jetix pattern)
   - Shared memory via wiki + alphas
   - Conflict resolution protocols
   - Mediator roles (meta-agent, manager)

7. **Org в prompts:**
   - Role-manifest embedded в system prompt
   - Context about other roles (граф создания)
   - How org changes propagate к running agents

### Часть I — Visualization и tooling

1. **Visualization tools:**
   - Mermaid.js org diagrams (flow, graph)
   - D3.js custom visualizations
   - Graphviz (DOT language)
   - Obsidian Canvas
   - Excalidraw для concepts
   - D2 declarative diagrams
   - PlantUML activity diagrams

2. **Interactive tools:**
   - Self-generated org chart website (static site from YAML)
   - Query interface (search org by accountability, by role, by person)
   - Live edit UI (low-code for non-technical editors)

3. **CLI tools:**
   - `jetix-org list` — all current roles
   - `jetix-org diff v1.0 v2.0` — what changed
   - `jetix-org assign executor role` — helper для changes
   - `jetix-org lint` — health check

4. **Integration:**
   - With GitHub API (PR-based review for org changes)
   - With Langfuse (agent performance → role manifests)
   - With Claude Code (agents read org context)

5. **Existing tools что approximate:**
   - OrgChartPro, OrgChart Now (enterprise, not git-native)
   - Lucidchart / Miro (visual, not version-controlled)
   - Obsidian Canvas (closest to what Jetix needs?)
   - Custom solutions

### Часть J — Практические выходы для Jetix

**Самая важная часть.**

1. **Финальный format для Jetix org в git:**
   - Полный schema (concrete YAML + Markdown structure)
   - Example filled для 3 ролей (sales-lead, delivery, manager)
   - Directory structure finalized
   - Naming conventions

2. **CI/CD для org changes:**
   - Which repo hooks runs lint
   - Which PR template для org changes
   - Approvals required based on change magnitude
   - Automated announcement на merge (monthly letter update)

3. **Automated health checks** — starter pack:
   - Initial 10 lint rules (concrete)
   - Tool choice (custom Python vs OPA/Rego)
   - CI integration
   - Alert thresholds

4. **Versioning strategy** для Jetix org:
   - When bump MAJOR (reorganize layers?)
   - When MINOR (new role, new executor)
   - When PATCH (clarifications)
   - Tag schedule

5. **Transferability preparation:**
   - What в org документах specific Jetix vs abstract pattern
   - How to extract reusable framework
   - License decision (recommend)
   - Distribution plan (horizon 2027+)

6. **A/B testing experimental orgs:**
   - Concrete process для testing alternate structures
   - When to use (quarterly re-examination?)
   - Measurement (what metrics matter)

7. **Constitutional layer для Jetix:**
   - §11 invariants из SYSTEM-DESIGN-TECH — где живут (в git)
   - Change governance (кто меняет, как)
   - Agent-enforcement

8. **Tooling recommendation:**
   - For current scale (solo): минимум — git + Mermaid + custom scripts
   - For team: GitHub + CI lint + Dashboard
   - For mega-corp: OPA + custom UI + full observability

9. **Migration from current Jetix state:**
   - Currently: agents defined в `.claude/agents/`, minimal role-manifest
   - Target: full org-as-code with roles/, executors/, policy/
   - Steps с timeline

10. **Jetix positioning narrative:**
    - How to tell the story к клиентам: «наш org chart в git»
    - How to demonstrate (показать репо)
    - Competitive advantage framing

11. **Anti-patterns specific Jetix:**
    - Over-engineering (OPA для 12 ролей)
    - Under-engineering (ad-hoc changes без lint)
    - Mixing roles и people в одном файле
    - Vendoring other orgs' structure without adapting
    - Premature licensing

12. **10-year vision org-as-artefact:**
    - 2026: Jetix internal
    - 2027: Open-source framework repo
    - 2028: First external adopters
    - 2030: Certification program
    - 2032: Industry standard for AI-native companies?

## Format требования

- **Объём:** 5000-10000 слов
- **Parts A-J** structured
- **Citations:** academic frameworks + concrete implementations. Primary sources.
- **Code examples** everywhere (YAML schemas, CI configs, lint rules)
- **Comparison tables** (file formats, existing orgs, tooling)
- **Diagrams** где relevant (org evolution, workflows)
- **Honest about uncertainty** — много ground is new

## Anti-patterns

- ❌ Superficial «org как wiki» без formal structure
- ❌ Ignoring Holacracy (самый формальный существующий пример)
- ❌ Generic «agile org» обзор без technical implementation specifics
- ❌ Пропустить AI-native angle (это unique Jetix context)
- ❌ Без Part J

## Критерий успеха

На основе research я могу:
1. Написать detailed section в `design/JETIX-ARCHITECTURE-FINAL.md` про org-as-artefact
2. Implement 10 lint rules для Jetix org
3. Define versioning strategy для org changes
4. Plan open-source framework release (horizon 2027)
5. Explain к клиентам / партнёрам why «org в git» это advantage (positioning)

Приступай. Академично, с citations, Part J максимально actionable.

=== PROMPT END ===

---

## Notes для Ruslan

**Output file:** `raw/research/org-chart-in-git-deep-research-2026-04-19.md`

**Параллельно с R9.** Оба — Wave 3.
