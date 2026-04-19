---
research-id: R2
wave: 1
topic: Company-as-code implementation patterns для AI-native mega-corp
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/company-as-code-impl-deep-research-2026-04-19.md
priority: P1 (критично — блокирует финализацию L1 Foundation)
---

# R2 — Company-as-code: как инженерно реализовать

## Зачем этот research

Jetix следует принципу **«бизнес как кодовая база»** (approved Ruslan'ом 100%).
Всё управление компанией ведётся через git-репозиторий: решения, роли,
процессы, документация, промпты, evals, postmortems. Это L1 Foundation в
архитектуре.

Но **как это выглядит инженерно** — не решено. Нужно понять:

- Какие есть existing успешные примеры (GitLab handbook, Holacracy Constitution,
  Valve handbook, Spotify model, Shape Up)
- Как именно работает prompt-as-code, CI/CD для LLM, observability
- Какие tools применять (LangSmith / Langfuse / Braintrust / Patronus /
  Promptfoo и др.)
- Какая минимальная viable infrastructure для solo → team transition
- Какой git workflow (GitFlow / GitHub Flow / Trunk-based)
- Как работает docs-as-code (Diátaxis framework)
- Decision records (ADR) practices

Выход research'а — input для документа
`design/JETIX-ARCHITECTURE-FINAL.md` и `docs/INSTRUCTIONS.md`.

## Как использовать

Скопируй **всё между `=== PROMPT START ===` и `=== PROMPT END ===`** и
вставь в Perplexity Max Computer (собственная вкладка, параллельно R1 и R3).

---

=== PROMPT START ===

Ты — senior engineering architect с опытом построения dev-infrastructure для компаний от solo до 500+ engineers. Я прошу тебя провести **глубокий академический research** по теме «company as code» — как инженерно организовать компанию через git-репозиторий так, чтобы все процессы, роли, решения, документация версионировались как код. С прямым практическим выходом на специфический use case: AI-native компания с одним founder и 12+ AI-агентами, растущая в mega-corporation.

## Контекст проекта Jetix (2000 слов)

**Кто такой Jetix.** Jetix — операционная система для AI-native компании, построенная одним основателем (Ruslan, Берлин). Цель — вырасти в крупную корпорацию. Цель Q2 2026: €50K revenue до 30.06.2026 (сейчас €0).

**Текущий технологический стек:**
- **Repository:** `github.com/Bogersebekov/jetix-os` (private monorepo)
- **Server:** Hetzner CPX32 Nuremberg, Ubuntu 24.04, через Tailscale
- **Path на сервере:** `~/jetix-os`
- **Central LLM:** Claude Code CLI v2.1.104 с Anthropic Opus 4.7 (1M context)
- **12 AI-агентов** через Claude Code subagent system (Task tool)
- **Languages:** Python (tools), Markdown (docs), YAML (config), Bash (scripts)
- **Notion** как external source of truth через MCP (дублирование)

**Что уже работает на сервере:**
- `wiki/` — 557 страниц, 572 edges (Karpathy LLM Wiki + OmegaWiki pattern + HippoRAG PPR retrieval)
- `projects/` — 8 активных проектов
- `agents/` — папки для каждого из 12 агентов с частичными system prompts
- `.claude/agents/*.md` — agent definitions
- `tools/` — Python pipeline для voice-memos (transcribe / extract / filter / review)
- `templates/` — 15 canonical templates (T-01 до T-12 + legacy)
- Skills: `/ingest`, `/ask`, `/plan-day`, `/close-day`, `/lint`, `/consolidate`, `/build-graph`

**Что уже решено в архитектуре (9 месяцев работы над концептом):**

**Архитектура Jetix — 7 слоёв + L0:**
- L0 Executive Core: Ruslan + AI-агенты + future human team (единая role-abstraction)
- **L1 Foundation (этот research) = software company practices:** Git + CI/CD + Docs-as-code + prompt-as-code + SRE + blameless postmortems + observability + risk-based routing + shared infrastructure. Все 8 функций approved.
- L2 Cognitive: Анатолий Левенчук / ШСМ (role ontology, alphas with states, graph of creation, strategizing, thinking-by-writing)
- L3 Product: Micro-SaaS
- L4 Delivery: Agency + Consulting hybrid (primary Q2 revenue)
- L5 Membrane: Community (Alliance + Club + newsletter)
- L6 Topology: Platform (horizon 18-36 мес)
- L7 Portfolio: Holding-дисциплина (capital + hours + attention allocation)

**Ключевой принцип — Nested hierarchy (Life-OS root, Jetix внутри):**
- Life-OS = корневая операционная система жизни founder'а
- Jetix = один из проектов Life-OS с полноценной 7-слойной архитектурой
- Полное разделение ресурсов (часы / деньги / внимание считаются отдельно)
- Сейчас: один git-repo, разные папки
- Будущее: отдельные репозитории и серверы

**Ключевой принцип — Mega-corporation не solo:**
- Хотя сейчас один человек + AI, архитектура закладывается под большую компанию с Day 1
- Scale-up-first: при 10x росте (капитала / часов / людей / проектов / ролей) система справляется без rebuild
- Human+AI executors через единую role-abstraction (люди = продолжение агентов, не отдельная категория)

**Что мы уже знаем как L1 должен работать (high-level):**

1. **Git + markdown + YAML как база данных** — никакого SQL, Notion как internal truth, vector store. Вендор-независимость.
2. **Prompt-as-code** — промпты роль-агентов версионируются через Semantic Versioning (v1.2.0), не «latest».
3. **CI/CD для промптов (eval pipelines)** — перед деплоем нового промпта автопрогон на golden dataset (10-50 эталонных кейсов per role).
4. **Diátaxis framework** для документации — 4 формы: tutorials / how-to guides / reference / explanation.
5. **Blameless postmortems** — когда агент «галлюцинировал», виноват не агент а система (промпт / контекст / guardrails). 5 Whys.
6. **Error Budgets / Hallucination Budgets** — SRE-adaptation. Каждый role имеет бюджет допустимых ошибок. При превышении — stop, fix, evals update.
7. **Risk-based routing** — low/mid/high risk tasks через разные gates. High risk = human-in-the-loop.
8. **ADRs (Architecture Decision Records)** — Michael Nygard style.

**Что НЕ работает для solo + AI (cargo-cult warnings):**
- Scrum ceremonies, story points, daily standups с агентами — убивают velocity
- SAFe, Jira-микроменеджмент
- Альтернатива: Shape Up (Basecamp) — 2-6 недельные «bets»

**Что нам нужно от этого research:** deep technical implementation guide «как превратить концепцию company-as-code в working infrastructure» — конкретные patterns, tools choices, folder structures, workflows, examples из реальных компаний.

## Основной research-запрос

Проведи **глубокий академический research** по следующим темам. Каждая тема — обязательный раздел в финальном отчёте.

### Часть A — Reference cases (existing successful implementations)

Глубокое изучение следующих «company-as-code» примеров. Для каждого: как организован repo, какие папки, какой стиль документов, что делают хорошо / плохо, lessons for Jetix.

1. **GitLab Handbook** (about.gitlab.com/handbook) — самый полный и публичный example. Репозиторий `gitlab-org/handbook`. Какие разделы, как устроены onboarding docs, decision records, engineering handbook, security handbook. Ключевой paper: «Remote-first work manifesto».

2. **Holacracy Constitution** (holacracy.org/constitution) — версионированная «constitution» как code. Какие элементы org в коде: circles, roles, governance meetings. GitHub repo `holacracyone/holacracy-constitution`.

3. **Valve Employee Handbook** (PDF) — culture book as code (не формально, но как artefact). Структура, как работает без hierarchy.

4. **Spotify model documents** — official whitepaper «Scaling Agile @ Spotify», Henrik Kniberg videos. Squads / tribes / chapters / guilds как code-like structure.

5. **Basecamp / 37signals «Shape Up»** (shapeup.basecamp.com) — full book online. Как Basecamp управляет собой через «pitches» + «6-week cycles» + «cooldown». Public artefacts в github.com/basecamp.

6. **Stripe engineering / Patrick Collison approach** — public blogs, writing style. Подход к internal writing. Github examples where possible.

7. **The Economist «Company Brain» articles** (2023-2024) about AI-native org structures (если есть).

8. **Other examples** — HashiCorp, Vercel, Linear — public materials на internal org practices.

Для каждого case: структурированное сравнение в финальной таблице.

### Часть B — Prompt-as-code industry patterns (LLM ops 2024-2026)

1. **Semantic Versioning для промптов** — как именно. Anthropic recommendations (anthropic.com/engineering). OpenAI Cookbook patterns.

2. **Golden datasets** — как составлять, размеры, update frequency. Patterns из production LLM teams.

3. **Prompt registries** — public tools: PromptHub, Portkey, Humanloop. Сравнение.

4. **LangChain / LlamaIndex / LangGraph patterns** — как они версионируют workflows.

5. **Claude Code specific patterns** — как Anthropic рекомендует организовывать `.claude/agents/` и `.claude/commands/`. Из их documentation и blog.

6. **«Agents as code» vs «prompts as config»** — academic discussion 2024-2026.

Источники: anthropic.com/engineering, openai.com/blog, langchain blog, Humanloop case studies, Portkey blog. MIT paper «LLM as programs» если есть. ICML / NeurIPS 2024-2025 papers on agent workflows.

### Часть C — Docs-as-code (Diátaxis deep-dive + tools)

1. **Diátaxis framework** (diataxis.fr) — Daniele Procida's work. 4 формы (tutorial / how-to / reference / explanation). Почему именно 4, как не путать, когда какую применять. Ключевой paper: «The grand unified theory of documentation».

2. **Практические примеры Diátaxis** — какие проекты (Django, Write the Docs community, Grafana, Keystone.js) используют. Что хорошо / плохо.

3. **Tools:**
   - Sphinx (Python world)
   - MkDocs + Material theme (popular simple)
   - Docusaurus (React-based, Meta)
   - Retype, Obsidian Publish
   - Astro Starlight (latest)

   Comparison: когда какой выбирать, integration с GitHub Actions for autopublish.

4. **Documentation testing** — Vale, alex, markdownlint, link-checkers. Как вставлять в CI/CD.

5. **Writing style guides** — Google Developer Style Guide, Microsoft Writing Style Guide, 18F Content Guide. Main principles.

Источники: Daniele Procida articles и talks (particularly PyCon 2017 talk «What nobody tells you about documentation»), Write the Docs conference talks. Documentation tools comparison articles. Tom Johnson «I'd Rather Be Writing» blog.

### Часть D — CI/CD для LLM (evals, observability, tools choice)

Это самая техническая часть.

1. **LLM Evals frameworks comparison:**
   - **LangSmith** (LangChain) — pricing, capabilities, integration
   - **Langfuse** (open-source alternative) — features, self-hostable
   - **Braintrust** — step-level tracing focus
   - **Patronus AI** — hallucination detection specifically
   - **Promptfoo** (open-source CLI)
   - **TruLens**
   - **Opik** (Comet ML)
   - **Helicone**
   - **Arize Phoenix**
   - **LlamaIndex Evals**

   Detailed comparison table: cost / self-host option / features / integration / community.

2. **Eval patterns:**
   - Reference-based evals (vs golden)
   - LLM-as-judge patterns
   - Human-in-the-loop evals
   - A/B testing prompts
   - Regression testing
   - Chain evals (multi-step)

3. **CI/CD integration:**
   - GitHub Actions templates для prompt deployment
   - Pre-commit hooks для prompt linting
   - Staged rollout patterns (canary / shadow)

4. **Observability patterns:**
   - Tracing (distributed tracing for agents)
   - Metrics (latency, tokens, cost, quality)
   - Logging best practices

5. **Risk-based routing** (AI observability):
   - Low risk (internal queries) → minimal checks
   - Mid risk → ML classifier gate
   - High risk (client-facing, financial) → 3-layer validation + human

6. **Cost management:**
   - Token budget per role per day
   - Cost attribution (which role / project / client)
   - Cost alerts

Источники: Anthropic blog on evals (anthropic.com/research), OpenAI Cookbook, LangChain blog, Braintrust docs, Langfuse docs. arxiv.org papers 2024-2025 on LLM evals. Patronus AI research papers.

### Часть E — Postmortems, incident response, SRE for AI

1. **Google SRE Book** — full framework. «Hotness of the lost week» postmortem template. Blameless culture principles.

2. **Postmortem template evolution** — как adaptировать для AI-incidents. Когда incident это прohibit agent hallucination, wrong output, cost blowup.

3. **Error budgets adaptation** — SRE error budgets для SLA. Adapted: hallucination budgets per agent. Какие специфические metrics.

4. **5 Whys** technique — с примерами для AI agent failures.

5. **Incident response playbook** — как organized. PagerDuty / Opsgenie не для AI — что alternative.

6. **Pollcasts and postmortem reviews** — examples Google, Meta.

Источники: Google SRE Book (online), «Site Reliability Workbook» (2nd book). Charity Majors on observability. Pagerduty postmortem guide. Specific AI postmortem examples where public (OpenAI outage writeups).

### Часть F — Decision records, governance, contracts-as-code

1. **ADR (Architecture Decision Records)** — Michael Nygard original article. MADR template (madr.dev). Structurally-sound.

2. **RFC (Request for Comments)** processes — Rust RFC process, Python PEPs, IETF RFCs. Adaptation for business decisions.

3. **Amazon 6-pager** — написание, template, что включается. Public info.

4. **«Contracts as code»** — SLAs / OKRs / commitments в git. Tools (если существуют).

5. **OKR management в git** — public patterns. Templates.

6. **Commitments and accountability** — how track в code-style.

Источники: Michael Nygard original blog post «Documenting Architecture Decisions» (2011), adr.github.io repository. Google Design Doc template. Amazon blog posts on PR/FAQ template (PRFAQ). Rust RFC process.

### Часть G — Infrastructure minimum viable for solo → team

1. **Monorepo tools** (если multi-directory нужно):
   - Turborepo
   - Nx
   - Moon
   - Bazel (if mega-scale)
   - Lage

   Когда какой. Overhead.

2. **Git workflow:**
   - GitFlow (probably too heavy)
   - GitHub Flow (simple)
   - Trunk-based development (modern, for CI/CD heavy)
   - Forking workflow

   Для solo → team transition — какой выбрать.

3. **Secrets management:**
   - 1Password (personal)
   - Doppler (team-oriented)
   - Bitwarden
   - HashiCorp Vault (overkill for solo)
   - AWS Secrets Manager / GCP Secret Manager
   - SOPS (sops-based encrypted secrets in git)

4. **Infrastructure as Code (minimum viable):**
   - Docker Compose (local dev)
   - Terraform (server provisioning)
   - Ansible (config management)
   - systemd unit files for services
   - Comparison: when overkill vs necessary.

5. **Backup & disaster recovery:**
   - restic (tool focus)
   - rclone
   - Borgbackup
   - Off-site storage (B2, Wasabi, S3)
   - Recovery time objectives realistic for solo.

6. **Monitoring:**
   - Prometheus + Grafana (classic)
   - Uptime-kuma
   - Healthchecks.io
   - Sentry for errors
   - BetterStack / Cronitor

Recommended minimum viable stack for Jetix current state и path toward 10x scale.

### Часть H — Практическая Jetix implementation plan

**Это самая важная часть.** Подвяжи весь предыдущий research к конкретному Jetix-контексту и дай actionable implementation план.

1. **Финальная folder structure для Jetix monorepo** — детальная tree with comments про каждую папку. Включая:
   - `agents/<role>/` structure (system.md, manifest.yaml, prompts/, evals/, examples/)
   - `roles/<role-abstract>.md` (abstract role spec)
   - `executors/` (future human team)
   - `decisions/` (ADRs)
   - `evals/` (golden datasets)
   - `postmortems/`
   - `prompts/v1/`, `prompts/v2/` (SemVer'd)
   - `wiki/`, `projects/`, `templates/`, `tasks/` (уже существуют)
   - `docs/` (Diátaxis 4 forms)
   - `infra/` (IaC)
   - Life-OS separation: `life-os/` vs `jetix/` parent folders in same repo (interim) / separate repos (future).

2. **Tools choice для Jetix** (прямо сейчас, не overkill):
   - Eval tool? (LangSmith? Langfuse? Promptfoo? Самописный?)
   - Docs: MkDocs Material? Astro Starlight? Plain markdown in wiki?
   - Secrets: 1Password (already uses) / Doppler / SOPS?
   - Monitoring: минимум что реалистично для solo.
   - Backup: restic + B2?

3. **Git workflow recommendation** — для Jetix в Q2 (single developer + AI) и куда migrate когда team появится.

4. **First 14 days implementation plan** — согласно synthesis: «L1 Foundation должен быть deployed в 14 дней максимум». Concrete day-by-day plan: Day 1-14 — что делать каждый день.

5. **Golden dataset creation process** — как Jetix создаёт 10 кейсов per role × 12 roles = 120 golden examples. Кто пишет? Agent-generated + human review? Template.

6. **Prompt versioning workflow** — конкретный git workflow для обновления role prompts. Branch / PR / eval check / merge / deploy.

7. **Postmortem template для Jetix** — concrete markdown template. When to write (после каждого agent failure / significant incident only). Storage в `postmortems/YYYY-MM-DD-<slug>.md`.

8. **ADR template для Jetix** — Nygard-style. Storage `decisions/YYYY-MM-DD-<slug>.md` (уже есть этот принцип). Examples.

9. **Scale-up path** — что меняется когда Jetix от solo (сейчас) → 5 executors → 20 → 100. Какие tools add, какие upgrade, какие workflows меняются. Concrete triggers.

10. **Anti-patterns to avoid** — Jetix-specific чего НЕ делать (over-engineering — solo может 3 недели строить CI/CD без единого клиента).

## Format требования

- **Объём:** 5000-10000 слов
- **Format:** Markdown с явными частями A-H
- **Citations:** прямые URLs, inline format `[title](url)` или `[author year](url)`
- **Tables** для comparisons (особенно tools choice)
- **Code examples** где релевантно (git workflow commands, eval scripts, IaC snippets)
- **Honest about uncertainty**
- **Actionable** — Part H должна быть really implementable

## Anti-patterns (чего НЕ делать)

- ❌ Поверхностный обзор tools без hands-on comparison
- ❌ Без Part H (practical Jetix plan)
- ❌ Over-engineering recommendations для solo (Kubernetes / Istio / enterprise tools)
- ❌ Игнор specifics: мы solo сейчас, но scale-up-first дизайн обязателен
- ❌ Копипаст из generic «how to start a startup» блогов
- ❌ Без citations на Anthropic / Claude Code specific patterns (это наша базовая платформа)

## Критерий успеха

Research считается успешным если на его основе я могу:
1. Написать `design/JETIX-ARCHITECTURE-FINAL.md` (финальный чистовик архитектуры)
2. Написать `docs/INSTRUCTIONS.md` (daily operational guide)
3. Создать первую версию `roles/<role>.md` template
4. Deploy L1 Foundation в 14 дней
5. Запустить eval pipeline для первой роли

Приступай. Работай тщательно, технически, цитируй всё. Не торопись.

=== PROMPT END ===

---

## Notes для Ruslan

**Время запуска:** 30-90 минут. Параллельно с R1 и R3 в разных вкладках.

**Что делать если результат слабый:**
- Если tools comparison недостаточно — запроси «expand Part D with hands-on trial data for each tool»
- Если Part H generic — «make Part H more specific to our current stack (Claude Code, Hetzner, GitHub)»

**После получения файла:**
- Сохрани как `raw/research/company-as-code-impl-deep-research-2026-04-19.md`
- На сервер через `scp` или GitHub commit
- После Wave 1 complete — begin synthesis
