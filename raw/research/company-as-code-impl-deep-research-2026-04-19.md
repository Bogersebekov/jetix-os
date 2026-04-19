# Jetix: Company-as-Code — глубокий research и implementation plan

> **Версия**: 1.0.0 | **Дата**: 2026-04 | **Автор**: Ruslan Bogersebekov | **Статус**: L1 Foundation Reference

---

## Executive Summary

**Company-as-Code** — это операционная парадигма, при которой вся компания: её роли, решения, процессы, агенты, инфраструктура и знания — хранится в Git-репозитории в виде текста, версионируется и изменяется через pull request. Для Jetix это не метафора, а буквальная архитектура: `jetix-os/` — это и есть компания.

Восемь принципов L1 Foundation, установленных в research brief, подкреплены следующими best-in-class референсами:

1. **Git + Markdown + YAML как база данных** → [GitLab Handbook](https://about.gitlab.com/handbook/) (2,000+ страниц, 2,000+ сотрудников, всё через MR)
2. **Prompt-as-code через SemVer** → [Latitude.so](https://latitude.so/blog/prompt-versioning-best-practices) + [Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning): MAJOR.MINOR.PATCH для промптов, иммутабельные версии
3. **CI/CD для промптов через eval pipelines** → [Promptfoo](https://promptfoo.dev/docs/getting-started/) (CLI, GitHub Actions, YAML config) + [Langfuse](https://langfuse.com/) (self-hosted трейсинг)
4. **Diátaxis framework для документации** → [diataxis.fr](https://diataxis.fr/): 4 формы (tutorial / how-to / reference / explanation), Django как canonical implementation
5. **Blameless postmortems** → [Google SRE Book Chapter 15](https://sre.google/sre-book/postmortem-culture/): виновата система, не агент; полный шаблон в Части E
6. **Hallucination Budgets (SRE error budgets adaptation)** → [Google SRE Book Chapter 3](https://sre.google/sre-book/embracing-risk/): бюджет = 1 − SLO_target; для LLM: hallucination rate < 2%/неделю
7. **Risk-based routing (3-tier)** → NeMo Guardrails + SRE: PATCH → auto-deploy, MINOR → golden dataset ≥ 85%, MAJOR → human sign-off
8. **Decision Records** → [Oxide Computer RFD process](https://oxide.computer/blog/rfd-1-requests-for-discussion): охватывает бизнес- и tech-решения, pre-decision lifecycle с 6 состояниями

**Критические инструментальные решения для Jetix Q2 2026:**
- Eval: Promptfoo CLI (GitHub Actions) + Langfuse self-hosted (трейсинг + prompt registry)
- Docs: MkDocs Material (Python-стек, GitHub Pages, нулевой overhead)
- Secrets: SOPS + age (git-native, offline, company-as-code ethos)
- Deploy: Coolify (git-push-to-deploy, Claude integration, no vendor lock-in)
- Decision records: Oxide-style RFDs (охватывают tech + бизнес + операционные решения)
- Git workflow: trunk-based solo (commit to main, eval gate on push)

**14-day rollout path** (Часть H4) разбит на конкретные ежедневные deliverables с проверяемыми критериями готовности — от `git init` в Day 1 до полного monitoring stack в Day 14. Каждый день = 2–4 часа работы.

**Ключевой тезис**: Jetix — это первая company-as-code компания, где git-репозиторий является не только source of truth для кода, но и для ролей, агентов, решений, OKR и операционных процессов. Это создаёт audit trail, reproducibility и scale-path, которые невозможны при хранении в Notion или в голове основателя.

---

## Часть A — Reference Cases

### A1. GitLab Handbook

[GitLab Handbook](https://about.gitlab.com/handbook/) — канонический пример company-as-code в масштабе: 2,000+ страниц, открытый для мира, редактируется через merge requests и ревьюируется как код. Репозиторий `gitlab-com/content-sites/handbook` рендерится через Hugo и деплоится на GitLab Pages. Структура зеркалит реальную org chart: Company → People Group → Engineering → Security → Marketing → Sales → Finance → Legal.

**Engineering sub-handbook** особенно детален: Engineering Error Budgets, incident management, blameless postmortem templates — всё это прямо применимо к Jetix. Ключевой паттерн — **DRI (Directly Responsible Individual)**: каждый документ, процесс и решение имеет единственного ответственного. В Jetix роль DRI выполняет Ruslan по умолчанию, но архитектурно каждый агент является DRI своей области.

**Что брать в Jetix**: общую структуру (каждая функция — своя папка), DRI-модель, error budget подход. **Что не брать**: 2,000 страниц HR/Legal контента — это оверкилл для solo+AI. Начать с `company/`, `engineering/`, `roles/`, `agents/` и расширять по необходимости.

### A2. Holacracy Constitution

[Holacracy Constitution v5.0](https://holacracy.org/constitution) хранится на [GitHub](https://github.com/holacracyone/Holacracy-Constitution) (417 звёзд, 5 мажорных релизов) и представляет наиболее строгую формализацию role-based governance в open-source мире. Ключевая конструкция — **Role**: `name` + `purpose` + `domains` + `accountabilities`. Это прямо портируется в Jetix `roles/<role>.md`.

Каждый AI-агент в Jetix — это Role в смысле Holacracy: он имеет Purpose (зачем существует), Domains (что контролирует) и Accountabilities (что непрерывно делает). Декупл роли от исполнителя (role ≠ person/agent) — это архитектурный принцип: одна роль сегодня заполнена AI-агентом, завтра может быть передана человеку без изменения самой роли.

**Что брать**: шаблон определения роли, decoupling role/executor. **Что не брать**: Governance Meetings, Integrative Decision-Making ceremonies — заменяются RFDs.

### A3. Valve Employee Handbook

[Valve Employee Handbook (2012)](https://www.studocu.com/sg/document/singapore-management-university/human-capital-management/valve-new-employee-handbook-guiding-principles-culture/124110328) — самый известный culture-as-artifact в software. Принцип **Flatland**: нет менеджеров, нет иерархии, каждый сотрудник может запустить проект. В Jetix Ruslan — эквивалент Gabe Newell: его стратегический вкус является невидимой архитектурой, агенты — автономные контрибьюторы.

**Ключевой insight**: handbook-as-onboarding работает. Handbook *является* организационной структурой — он не описывает org chart, он описывает способ мышления. В Jetix каждый `.claude/agents/<name>.md` — это эквивалент Valve handbook для конкретного агента: зачем он существует, как принимает решения, что не делает никогда ([Forbes analysis](https://www.forbes.com/sites/stevedenning/2012/04/27/a-glimpse-at-a-workplace-of-the-future-valve/)).

**Что брать**: handbook-as-onboarding artifact, агент как culture document. **Что не брать**: полная flatness ломается на масштабе — нужны explicit role accountabilities.

### A4. Spotify Model (с критикой Jeremiah Lee)

[Spotify Engineering Culture](https://engineering.atspotify.com/2014/03/spotify-engineering-culture-part-1/) — Squads/Tribes/Chapters/Guilds — стала самым копируемым scaling framework. Проблема: как задокументировал Jeremiah Lee в ["Spotify's Failed #SquadGoals"](https://www.jeremiahlee.com/posts/failed-squad-goals/), модель **никогда не работала даже в Spotify**:

> *"Even at the time we wrote it, we weren't doing it. It was part ambition, part approximation."* — Joakim Sundén, agile coach at Spotify 2011–2017

Конкретные failure modes: matrix management без accountability по delivery; автономия без alignment; assumed competency (люди не умели работать автономно). **Урок для Jetix**: избегать "автономных агентов" без explicit accountability. Role-based система с чёткими Accountabilities (Holacracy-стиль) решает именно это.

### A5. Basecamp Shape Up

[Shape Up](https://basecamp.com/shapeup) Райана Сингера — наилучшее соответствие для solo+AI структуры Jetix. Цикл: 6 недель работы → 2 недели cool-down → Betting Table → следующие 6 недель.

**Ключевые концепты для Jetix**:
- **Appetite**: временной бюджет устанавливается *до* шейпинга (например, "6 недель максимум") — не оценка, а ограничение ([Shape Up Chapter 8](https://basecamp.com/shapeup/2.2-chapter-08))
- **Circuit Breaker**: команда *должна* сдать в срок. Нет продлений. Незаконченная работа не переносится автоматически
- **Cool-down (2 недели)**: время для Ruslan, чтобы запустить postmortems, обновить промпты, обновить golden datasets — явно выделенное время для LLMOps

**Betting Table для Jetix** = один человек (Ruslan) принимает решение. Нет Scrum ceremonies, нет story points, нет sprint retrospectives. Shaping для AI-агентов: хорошо "сшейпленная" задача агенту — чёткая, но не гиперспецифицированная — прямой аналог Pitch template.

### A6. Stripe Writing Culture

Stripe построила сильнейшую writing culture в tech. Паттерн, задокументированный [Slab](https://slab.com/blog/stripe-writing-culture/): CEO Patrick Collison писал emails с footnotes, структурированные как research papers. Принцип: **writing is default communication** — нет slide decks, есть structured documents.

**Урок для Jetix**: хорошо написанный system prompt — это хорошо продуманное определение роли. Каждый agent `.md` файл должен быть написан как Stripe memo: структурированные секции, явные решения, конкретные примеры. Stripe также подтверждает Git+Markdown как default store.

### A7. Linear Method

[Linear Method](https://linear.app/method/introduction) даёт наиболее чёткую формулировку принципа purpose-built tooling: *"Flexible software lets everyone invent their own workflows, which eventually creates chaos as teams scale."* Принцип **"Decide and move on"**: *"There isn't always a best answer. Sometimes the most important thing is to make a decision, and move on."*

**Что брать**: "purpose-built over flexible" — прямо подтверждает Jetix anti-pattern list (Scrum/SAFe/Jira). Практика changelog: каждый агент должен иметь `CHANGELOG.md` с историей версий промпта.

### A8. Oxide RFD Process

[Oxide Computer RFD 1](https://oxide.computer/blog/rfd-1-requests-for-discussion) определяет процесс Requests for Discussion: вдохновлён IETF RFCs, Golang proposals, Joyent RFDs. **RFD — это pre-decision document**, который эволюционирует через 6 состояний:

| Состояние | Описание |
|---|---|
| `prediscussion` | Placeholder; ещё не готов к обсуждению |
| `ideation` | Тема/скоуп определены; scratchpad |
| `discussion` | Активный PR открыт |
| `published` | Дискуссия завершена; PR смёрджен |
| `committed` | Полностью имплементирован |
| `abandoned` | Нежизнеспособен |

**Ключевое отличие от ADR**: RFD охватывает *бизнес и операционные решения*, а не только техническую архитектуру. Для solo founder "discussion" фаза = self-review + Claude review. Это рекомендуемый формат для Jetix.

### Итоговая таблица: что брать в Jetix

| Компания | URL | Что берём |
|---|---|---|
| **GitLab** | [handbook](https://about.gitlab.com/handbook/) | Структура папок, DRI-модель, error budgets |
| **Holacracy** | [constitution](https://holacracy.org/constitution) | Role template: name/purpose/domains/accountabilities |
| **Valve** | [handbook](https://www.studocu.com/sg/document/singapore-management-university/human-capital-management/valve-new-employee-handbook-guiding-principles-culture/124110328) | Handbook-as-onboarding; AGENT.md как culture doc |
| **Spotify** | [engineering blog](https://engineering.atspotify.com/2014/03/spotify-engagement-culture-part-1/) | Антипаттерн: автономия без accountability → провал |
| **Shape Up** | [basecamp.com/shapeup](https://basecamp.com/shapeup) | 6-week cycles, circuit breaker, cool-down для LLMOps |
| **Stripe** | [slab.com](https://slab.com/blog/stripe-writing-culture/) | Writing-first culture; memo > slide deck |
| **Linear** | [linear.app/method](https://linear.app/method/introduction) | Purpose-built > flexible; changelog practice |
| **Oxide RFD** | [oxide.computer/blog/rfd-1](https://oxide.computer/blog/rfd-1-requests-for-discussion) | RFD lifecycle: pre-decision, business+tech, 6 states |

---

## Часть B — Prompt-as-Code (LLMOps patterns)

### B1. SemVer для промптов

[Semantic Versioning](https://latitude.so/blog/prompt-versioning-best-practices) (MAJOR.MINOR.PATCH) адаптируется к промптам следующим образом:

| Компонент | Триггер | Пример |
|---|---|---|
| **MAJOR** | Breaking output change — парсеры downstream должны обновиться; смена формата вывода | `1.0.0 → 2.0.0`: JSON → XML output |
| **MINOR** | Новая capability; новые few-shot примеры; новый параметр контекста | `1.0.0 → 1.1.0`: добавление domain scoping |
| **PATCH** | Мелкий фикс; typo; уточнение без изменения поведения | `1.0.0 → 1.0.1`: исправление ambiguous phrasing |

Четыре критических engineering-свойства версионированных промптов ([Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning)):
1. **Иммутабельность**: задеплоенная версия никогда не изменяется — новое изменение = новая версия
2. **Schema validation**: каждая версия несёт схему required variables
3. **Aliasing**: `production` (stable), `staging` (candidate), `latest` (risky) ([Dev.to](https://dev.to/kuldeep_paul/mastering-prompt-versioning-best-practices-for-scalable-llm-development-2mgm))
4. **Version-model coupling**: промпт = `(text, model, temperature, top_p)` — апгрейд модели может требовать MAJOR bump

[Anthropic Engineering 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) рекомендует структурировать system prompts через XML-теги или Markdown headers (`<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`), минимальный набор high-signal tokens, и curated few-shot examples.

**Jetix implementation**: YAML frontmatter в `.claude/agents/<name>.md` с `version: 1.2.0`. Git commit message = changelog entry: `feat(agents/researcher): v1.1.0 — add domain scoping`.

### B2. Golden Datasets (Hamel Husain framework)

[Hamel Husain](https://hamel.dev/blog/posts/evals/) определяет трёхуровневую иерархию eval:

| Уровень | Тип | Частота | Стоимость |
|---|---|---|---|
| **Level 1** | Unit tests (assertions, pytest-стиль) | Каждое изменение кода/промпта | Минимальная |
| **Level 2** | Human + model eval (trace inspection, labeling) | По расписанию | Средняя |
| **Level 3** | A/B testing (user behavior outcomes) | После major changes | Максимальная |

Процесс построения golden dataset:
1. **Синтез**: LLM генерирует diverse test inputs — "50 разных способов спросить X"
2. **Фильтрация Level 1**: assertion-based unit tests отбрасывают структурно невалидные кейсы
3. **Разметка Level 2**: инспекция трейсов, human labels (binary good/bad), model labels
4. **Курация**: отфильтрованный, размеченный набор → golden dataset

Размеры на практике: 10 кейсов — smoke tests, 50 — regression suite, 200+ — fine-tuning data. Golden datasets — живые документы, не статичные снапшоты: каждый новый failure mode → новый test case.

### B3. Сравнение prompt registries

| Registry | Open Source | Self-Host | Free Tier | Prompt Versioning | Anthropic Native | GitHub Actions | Сильная сторона |
|---|---|---|---|---|---|---|---|
| **Langfuse** | Да ([GitHub](https://github.com/langfuse/langfuse)) | Да | 50k units/mo | Да (полное) | Да | Via API | Best OSS: трейсинг + prompt mgmt в одном |
| **LangSmith** | Нет | Enterprise | 5k traces/mo | Да (Prompt Hub) | Да | Native | Deep LangChain integration |
| **Promptfoo** | Да | Да (CLI) | Бесплатно | Нет (git-based) | Да | Native YAML | CLI-first; easiest GitHub Actions |
| **Braintrust** | Нет | Enterprise | Да (Starter) | Да (иммутабельное) | Да | Via API | Step-level tracing; eval framework |
| **Helicone** | Да | Да | 10k req/mo | Нет | Да (proxy) | Via API | Cost tracking; 1-line integration |

([Источники: Langfuse pricing](https://langfuse.com/pricing); [LangSmith pricing](https://www.langchain.com/langsmith-pricing); [Promptfoo docs](https://promptfoo.dev/docs/getting-started/))

**Рекомендация для Jetix**: Langfuse (self-hosted, free) + Promptfoo (CLI в GitHub Actions) + Helicone (proxy для cost tracking). Покрывает prompt management, трейсинг, evaluation, CI/CD gating, cost attribution — всё open source, всё self-hostable.

### B4. Claude Code Specifics (.claude/agents/, skills, subagents)

Subagent definition файлы — Markdown с YAML frontmatter ([docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/sub-agents)):

```markdown
---
name: researcher
description: Deep research on technical topics and market analysis
tools: Read, Glob, Grep, Bash
model: sonnet
memory: project
effort: medium
color: blue
---

You are a specialized research agent for Jetix. When invoked, you:
1. Define the research question clearly
2. Search for primary sources
3. Synthesize findings into structured markdown
4. Flag uncertainties explicitly
```

Priority hierarchy агентов:
```
Managed settings (org-wide)
  > CLI --agents flag (session)
    > .claude/agents/ (project-level, checked into git)
      > ~/.claude/agents/ (user-level, all projects)
        > Plugin agents
```

Skills через `.claude/skills/<name>/SKILL.md` создают `/slash-commands`. Context engineering patterns ([Anthropic Engineering 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)): just-in-time context, compaction (summary при приближении к лимиту), structured note-taking в `NOTES.md`, sub-agent architectures с clean contexts.

### B5. Agents-as-code vs prompts-as-config

[Simon Willison](https://simonw.substack.com/p/agentic-engineering-patterns) вводит термин "agentic engineering" и документирует ключевые паттерны: Red/green TDD (тесты первыми помогают агентам писать более точный код), hoarding knowledge в `CLAUDE.md` как институциональная память, subagents для context management, git fluency.

Willison идентифицирует конец 2025 как inflection point для coding agents — именно Claude Code стал катализатором. Для Jetix: scheduled workflows (daily close, lint, build-graph) vs dynamic agents (researcher, writer) — оба паттерна нужны.

---

## Часть C — Docs-as-Code (Diátaxis + tools)

### C1. Diátaxis Framework

[Daniele Procida](https://diataxis.fr/) разработал Diátaxis работая над Django documentation. Четыре формы:

| Форма | Отвечает на | Ориентирована на | Аналогия |
|---|---|---|---|
| **Tutorial** | "Научи меня..." | Обучение | Обучение ребёнка готовить |
| **How-to guide** | "Как мне...?" | Цель | Рецепт в кулинарной книге |
| **Reference** | "Что такое...?" | Информация | Инструкция на упаковке |
| **Explanation** | "Почему...?" | Понимание | Статья по истории кулинарии |

([diataxis.fr/map/](https://diataxis.fr/map/); [diataxis.fr/explanation/](https://diataxis.fr/explanation/))

Ключевой insight: tutorial и how-to guide часто смешивают, но они ортогональны. Цель tutorial — дать learner **уверенность**, а не научить выполнять конкретную задачу. How-to guide предполагает компетентность. Explanation — "соединительная ткань": без explanation знание "рыхлое, фрагментированное, тревожное" ([diataxis.fr/explanation](https://diataxis.fr/explanation/)).

**Реальные adopters**: Django (origin), Gatsby, Cloudflare, NumPy, Divio, Microsoft (частично).

```
docs/
  tutorials/          # "Getting started with Jetix" — learning-oriented
  how-to/             # "How to create a new agent" — goal-oriented
  reference/          # "Agent frontmatter fields" — information-oriented
  explanation/        # "Why we use SemVer for prompts" — understanding-oriented
```

### C2. Инструменты документации

| Инструмент | Open Source | Сложность | GitHub Pages | Лучший для |
|---|---|---|---|---|
| **MkDocs + Material** | MIT | Низкая | Нативно | Solo Python-стек; **выбор для Jetix** |
| **Docusaurus** | MIT (Meta) | Средняя (React) | Да | React-экосистемы |
| **Astro Starlight** | Да | Низкая-Средняя | Да | Новейший; быстрые сборки |
| **Sphinx** | BSD | Высокая (RST) | Да | Большие Python API reference |
| **Mintlify** | Нет | Низкая | N/A (hosted) | AI-native public docs (Perplexity, Vercel) |

([MkDocs Material](https://squidfunk.github.io/mkdocs-material/); [Astro Starlight](https://starlight.astro.build/); [Mintlify](https://mintlify.com/))

**Выбор для Jetix**: MkDocs + Material. Pure Markdown input, zero build toolchain complexity, `mike` plugin для versioning, `mkdocs gh-deploy` → GitHub Pages, 50,000+ организаций используют. Для AI-native public docs в будущем (L5-L6 tier): Mintlify (включает MCP и llms.txt support).

### C3. Doc testing (Vale, markdownlint, lychee) + CI YAML

```yaml
# .github/workflows/docs.yml
name: Docs Quality
on:
  pull_request:
    paths: ['docs/**', '*.md']
jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: errata-ai/vale-action@reviewdog
        with:
          version: "3.11.1"
          files: docs/
          vale_flags: "--glob=*.md"
          fail_on_error: true
  markdownlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx markdownlint-cli "**/*.md" --ignore node_modules
  lychee:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v1
        with:
          args: --verbose --no-progress '**/*.md'
```

[Vale](https://github.com/errata-ai/vale) (MIT, 4.9k звёзд, Go) — prose linter с поддержкой Google Developer Style Guide, Microsoft Writing Style Guide ([GitHub Marketplace](https://github.com/marketplace/actions/vale-linter)). markdownlint — структура и стиль Markdown. lychee (Rust) — быстрая проверка ссылок.

### C4. Style guides

- [Google Developer Documentation Style Guide](https://developers.google.com/style): clarity и consistency для tech practitioners; деpart from guidelines "when it improves content"
- **Microsoft Writing Style Guide**: casual tone, contractions OK, global audience focus
- **18F Content Guide** (U.S. federal): plain language, accessibility-first — для public-facing Jetix content (L5 Community layer)

---

## Часть D — CI/CD для LLM

### D1. Eval frameworks — сравнительная таблица

| Инструмент | Open Source | Self-Host | Free Tier | Anthropic | GitHub Actions | OTel | Сильная сторона |
|---|---|---|---|---|---|---|---|
| **Promptfoo** | Да ([GitHub](https://github.com/promptfoo/promptfoo)) | Да (CLI) | Бесплатно | Да | Native YAML | Нет | CLI-first; easiest CI integration; red teaming |
| **Langfuse** | Да | Да | 50k units/mo | Да | Via API | Да (OTLP) | Best OSS: prompt + trace + eval в одном |
| **DeepEval** | Apache-2.0 | Да | Free tier | Да | Via pytest | Нет | 14.9k звёзд; 20+ metrics; agent-specific |
| **TruLens** | Apache-2.0 | Да | Бесплатно | Да | Via SDK | Да | Snowflake-backed; community-driven |
| **Arize Phoenix** | Да | Да | Бесплатно | Да | Via OTel | Да (OTel-native) | 9k+ звёзд; embedding visualization |
| **Braintrust** | Нет | Enterprise | Starter free | Да | Via API | Частично | Step-level tracing; иммутабельное versioning |
| **Helicone** | Да | Да | 10k req/mo | Да (proxy) | Via API | Нет | Cost tracking; 1-line proxy integration |
| **Opik (Comet)** | Да | Да | Free tier | Да | Via SDK | Да | Guardrails; prompt optimization |
| **LangSmith** | Нет | Enterprise | 5k traces/mo | Да | Native | Частично | Deep LangChain integration |
| **Patronus AI** | Нет | Нет | Не публично | — | Via API | — | Hallucination detection; LYNX model |

([Promptfoo docs](https://promptfoo.dev/docs/getting-started/); [Langfuse pricing](https://langfuse.com/pricing); [DeepEval GitHub](https://github.com/confident-ai/deepeval); [Arize Phoenix](https://phoenix.arize.com/))

### D2. Eval patterns (LLM-as-judge biases — Zheng et al.)

Ключевое исследование: [Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023](https://arxiv.org/abs/2306.05685). Сильные LLM-судьи (GPT-4) достигают >80% согласия с human preferences — тот же уровень, что human-human agreement.

**Biases для mitigation**:
- **Position bias**: судья предпочитает первый ответ в pairwise → решение: swap positions и average
- **Verbosity bias**: судья предпочитает длинные ответы → использовать chain-of-thought в prompt судьи
- **Self-enhancement bias**: модель оценивает собственный output выше → reference-guided grading

| Паттерн | Use Case | Примечания |
|---|---|---|
| Pairwise comparison | A vs B quality | Position bias risk; swap и average |
| Single-answer grading | Absolute quality | Calibration required |
| Reference-guided | Фактические задачи | Reference + judge |
| Regression | Catch prompt drift | Запуск golden dataset на каждом PR |
| Chain/trajectory eval | Multi-step agent | DeepEval: Task Completion, Step Efficiency |

### D3. GitHub Actions template для Promptfoo

```yaml
# .github/workflows/eval.yml
name: LLM Eval
on:
  pull_request:
    paths:
      - 'prompts/**'
      - '.claude/agents/*.md'
      - 'promptfooconfig.yaml'

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - name: Cache promptfoo
        uses: actions/cache@v4
        with:
          path: ~/.cache/promptfoo
          key: ${{ runner.os }}-promptfoo-${{ hashFiles('prompts/**') }}
      - name: Run eval
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          npx promptfoo@latest eval \
            -c promptfooconfig.yaml \
            --share \
            -o results.json \
            -o report.html
      - name: Quality gate
        run: |
          FAILURES=$(jq '.results.stats.failures' results.json)
          SCORE=$(jq '.results.stats.successes / (.results.stats.successes + .results.stats.failures)' results.json)
          if [ "$FAILURES" -gt 0 ]; then
            echo "FAIL: $FAILURES failures (score: $SCORE)"
            exit 1
          fi
          echo "PASS: All tests passed (score: $SCORE)"
      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: results.json
```

([promptfoo.dev CI/CD integration](https://www.promptfoo.dev/docs/integrations/ci-cd/))

### D4. Observability (OTel GenAI SemConv)

[OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) определяют vendor-neutral vocabulary для AI workload telemetry. Стандартные span attributes ([OneUptime](https://oneuptime.com/blog/post/2026-02-06-monitor-llm-opentelemetry-genai-semantic-conventions/view)):

```python
span.set_attribute("gen_ai.system", "anthropic")
span.set_attribute("gen_ai.request.model", "claude-opus-4-7")
span.set_attribute("gen_ai.usage.input_tokens", 1200)
span.set_attribute("gen_ai.usage.output_tokens", 340)
```

Ключевые метрики per Jetix agent:

| Метрика | Тип | Назначение |
|---|---|---|
| `gen_ai.usage.input_tokens` | Counter | Cost attribution per agent/role |
| Latency (span duration) | Histogram | SLA monitoring |
| Quality score (from evals) | Gauge | Hallucination budget |
| Cost/day/agent | Derived | Budget enforcement |

Каждый agent execution должен эмитировать structured trace event: `agent_id`, `task_id`, `model_version`, `prompt_hash`, `token_count`, `tool_calls[]`, `output_schema_valid`, `human_escalated`, `duration_ms`, `cost_usd` — для post-hoc debugging и бюджетного контроля ([Honeycomb — LLMs Demand Observability-Driven Development](https://www.honeycomb.io/blog/llms-demand-observability-driven-development)).

### D5. Risk-based routing (3-tier + NeMo Guardrails)

| Tier | Уровень риска | Gate Criteria | Human Review | Rollout |
|---|---|---|---|---|
| **Low** | PATCH (typo fix) | Level 1 unit tests pass | Не требуется | Auto-deploy on merge |
| **Mid** | MINOR (new capability) | Level 1 + golden dataset ≥ 85% | Async, 24h | Canary: 10% → 100% |
| **High** | MAJOR (new output format/model) | Level 1 + Level 2 + human sign-off | Synchronous | Shadow → canary → full |

[NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails) (NVIDIA, Thoughtworks Tech Radar: Adopt, April 2024): input rails, dialog rails, output rails, retrieval rails. 1.4x improvement в detection rate при параллельном запуске 5 guardrails, +0.5s latency.

### D6. Cost management

Per-role token budgets через YAML config + [Helicone](https://www.helicone.ai/pricing) (1-line proxy, 10k requests/mo free, cost dashboards per agent). Weekly cost audit через GitHub Actions scheduled check. Alert при >80% budget consumption.

---

## Часть E — Postmortems, SRE for AI

### E1. Google SRE Book — основы

[Google SRE Book](https://sre.google/sre-book/table-of-contents/) — фундаментальный текст reliability engineering. Ключевые главы для Jetix:
- [Chapter 3 — Embracing Risk](https://sre.google/sre-book/embracing-risk/): error budgets, SLOs, SLIs; философия *допустимой* ненадёжности
- [Chapter 14 — Managing Incidents](https://sre.google/sre-book/managing-incidents/): roles (Commander, Comms, Ops), live incident doc, handoffs
- [Chapter 15 — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/): blameless culture, templates, dissemination

Companion [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) содержит практические реализации: concrete SLI/SLO/error-budget mechanics, tactical incident playbook, detailed postmortem template.

### E2. Error budgets → Hallucination budgets

Формула error budget ([Google SRE Book Chapter 3](https://sre.google/sre-book/embracing-risk/)):
```
Error Budget = (1 - SLO_target) × time_period
```

Ключевой insight: *"The error budget provides a clear, objective metric that determines how unreliable the service is allowed to be. This metric removes the politics from negotiations."* — Marc Alvidrez, Google SRE Book.

**Jetix Hallucination Budget Model** (адаптация):

| Метрика (SLI) | Бюджет (SLO) | Trigger Action |
|---|---|---|
| Hallucination rate | < 2% в неделю | Превышение: заморозить prompt deploys; запустить eval suite |
| Tool-call error rate | < 1% per session | Превышение: route to human review gate |
| Schema-failure rate | < 0.5% per run | Превышение: rollback agent version |
| Human-escalation rate | < 5% of tasks | Превышение: review prompt complexity |
| Cost-overrun rate | < 10% over budget | Превышение: switch to lower-cost model tier |

([production AI SLO analysis](https://tianpan.co/blog/2026-04-17-ai-failure-rate-at-scale-slo))

### E3. 5 Whys с AI-примерами

Техника [5 Whys](https://en.wikipedia.org/wiki/Five_whys) разработана в 1930-х Sakichi Toyoda, формализована Taiichi Ohno как основа Toyota Production System ([lean.org](https://www.lean.org/the-lean-post/articles/five-whys-animation/)).

**Пример 1 — агент галлюцинирует аргумент tool call**:
1. Почему? → Агент получил ambiguous user instruction
2. Почему? → System prompt не содержит схемы для этого инструмента
3. Почему? → Tool добавлен без обновления agent manifest
4. Почему? → Нет CI-проверки полноты tool manifest
5. Почему? → Deployment pipeline не включает agent sync step

**Root cause**: Missing deployment gate → **Fix**: Add `lint-agent-manifest` step to CI

**Пример 2 — cost overrun на долгой задаче**:
1. Почему? → Claude вызывал инструмент в цикле 47 раз
2. Почему? → Условие завершения задачи слишком расплывчато ("when done")
3. Почему? → Template T-07 не содержит explicit stop condition
4. Почему? → В golden dataset нет eval test для runaway loops
5. Почему? → Eval suite не имеет latency/token budget assertions

**Root cause**: Missing eval coverage → **Fix**: Add `max_iterations` guard to T-07; add loop-detection eval case

### E4. Public AI postmortem case (OpenAI Dec 2024)

[OpenAI December 11, 2024 incident](https://status.openai.com/incidents/01JMYB483C404VMPCW726E8MET) — лучший задокументированный публичный LLM postmortem. Impact: все сервисы OpenAI (ChatGPT, API, Sora) деградированы 3:16–7:38 PM PST.

Root cause: новый telemetry service вызвал O(n) API calls per node → overwhelmed Kubernetes control plane → DNS failure broke service discovery. Staging cluster был слишком мал, чтобы воспроизвести cluster-size-dependent load patterns.

**Prevention measures**: phased rollouts с health monitoring, fault injection testing, break-glass access mechanism, decoupling data plane от control plane.

[Empirical arXiv study (2501.12469)](https://arxiv.org/html/2501.12469v2): большинство LLM failures резолвятся за 0.5–3 часа (медиана ~1 час); Anthropic failures показывают более сильную изоляцию отказов.

### E5. Charity Majors: observability-driven development

Charity Majors (co-founder Honeycomb.io) в ["LLMs Demand Observability-Driven Development"](https://www.honeycomb.io/blog/llms-demand-observability-driven-development):

> *"LLMs are black boxes producing nondeterministic outputs, impossible to debug/test with traditional software techniques."*

LLM-разработка **инвертирует TDD**: нельзя написать тесты до производства — нужно сначала получить production data. Подход: ship under feature flags → gather wide structured event telemetry → score quality → fix → generate test cases.

### E6. Jetix Postmortem Template

```markdown
# POST-{YYYY-MM-DD}-{SHORT-TITLE}

> **Status**: DRAFT | REVIEWED | CLOSED
> **Severity**: SEV1 | SEV2 | SEV3 | SEV4
> **Owner**: Ruslan (или agent-id если AI-authored)
> **Duration**: {start_time} → {end_time} ({total_minutes} min)
> **AI Agent(s) Involved**: {agent-name-or-none}

---

## 1. Summary
<!-- Один абзац. Что упало, impact, resolution. -->

## 2. Impact

| Dimension | Value |
|---|---|
| User-visible? | Yes / No |
| Tasks affected | N |
| Token cost overrun | $X |
| Revenue impact | €X or N/A |
| Data loss | None / Partial / Total |

## 3. Timeline (UTC)

| Time (UTC) | Event |
|---|---|
| HH:MM | Incident triggered / первый симптом |
| HH:MM | Root cause identified |
| HH:MM | Mitigation applied |
| HH:MM | Service restored |
| HH:MM | Postmortem opened |

## 4. Root Cause (5 Whys)

**Symptom**: {что наблюдалось}

| # | Why? | Answer |
|---|---|---|
| 1 | Почему X случилось? | Потому что Y |
| 2 | Почему Y случилось? | Потому что Z |
| 3–5 | ... | **Root cause** |

## 5. AI-Specific Factors

- **Hallucination involved?**: Yes / No / Unknown
- **Wrong tool call?**: Yes / No — Tool: `{tool_name}`, Args: `{args}`
- **Runaway cost?**: Yes / No — Actual tokens: N, expected: N
- **Prompt regression?**: Yes / No — Prompt version: `v{X.Y.Z}`
- **Schema failure?**: Yes / No

## 6. Things That Went Poorly
<!-- Blameless. System failures, not individual. -->
- [ ] {system gap 1}

## 7. Where We Got Lucky
- {near-miss 1}

## 8. Action Items

| Item | Owner | Priority | Type | Due | Done |
|---|---|---|---|---|---|
| {fix N} | Ruslan / {agent} | P1/P2/P3 | Prevent / Mitigate | {date} | [ ] |

## 9. Error Budget Impact

- **Which budget consumed**: Hallucination / Tool-call / Cost / Escalation
- **Budget before**: N%
- **Budget consumed**: N%
- **Budget remaining**: N%

---
*Template version: jetix-pom-v1.0*
```

---

## Часть F — Decision Records и Governance

### F1. Nygard ADRs (5-section)

[Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) опубликовал канонический формат Architecture Decision Record в 2011. Пять секций: **Title** (короткая noun phrase) → **Context** (forces at play, value-neutral) → **Decision** ("We will…", active voice) → **Status** (`proposed | accepted | deprecated | superseded`) → **Consequences** (все последствия: позитивные, негативные, нейтральные).

Ключевой принцип: ADR хранится в `doc/arch/adr-NNN.md`, нумерация монотонна, числа не переиспользуются. *"Nobody ever reads large documents. Small, modular documents have at least a chance at being updated."*

### F2. MADR evolution

[MADR](https://adr.github.io/madr/) добавляет к Nygard: `## Decision Drivers`, `## Considered Options`, `## Pros and Cons of the Options`, `### Confirmation` (как узнать, что решение работает). YAML frontmatter для metadata. Хорошо подходит для Jetix tech-решений: чистый Markdown, опциональные секции позволяют быстрым решениям оставаться краткими.

### F3. Oxide RFDs — рекомендуемый для Jetix

[Oxide RFD process](https://oxide.computer/blog/rfd-1-requests-for-discussion) охватывает **технические и операционные/бизнес решения** одновременно. Философия: *"Timely > polished. Notes are encouraged to be timely rather than polished."* Минимальная длина: одно предложение.

Ключевое отличие от ADRs: **RFD — pre-decision document**, который эволюционирует; ADR — post-decision record. Для solo founder: "discussion" фаза = self-review + Claude review.

### F4. Rust RFCs / Python PEPs

[Rust RFCs](https://github.com/rust-lang/rfcs/blob/master/0000-template.md): branch → PR → community comment → Final Comment Period → merge. [Python PEPs](https://peps.python.org/pep-0001/): Draft → Accepted / Provisional / Deferred / Rejected / Withdrawn / Final. Оба слишком heavy для solo Jetix, но статус-lifecycle (особенно `Superseded-By`) стоит заимствовать.

### F5. Amazon 6-pager / PR-FAQ

Amazon 6-pager ([Bezos, 2004](https://visme.co/blog/amazon-6-pager/)): 6-страничный narrative memo заменяет PowerPoint. Секции: Introduction → Goals → Tenets → State of Business → Lessons Learned → Strategic Priorities. Все читают 30 минут молча перед обсуждением.

**Для Jetix**: Goals + Tenets + State of Business структура хорошо подходит для quarterly planning. PR-FAQ (write the press release for a feature as if shipped) — для новых Jetix products (L3 Micro-SaaS).

### F6. OKRs-in-Git

[GitLab](https://docs.gitlab.com/user/okrs/) трекает OKRs в своём продукте с weekly Wednesday updates, health status (`on track / needs attention / at risk`). Для Jetix: OKRs как Markdown файлы в `okrs/` с YAML frontmatter для статуса и чекбоксами для Key Results — полная история в Git, diff-able, CI-validatable.

### Comparison table: ADR vs MADR vs RFC vs RFD vs 6-pager

| Формат | Лучший для | Длина | Pre/Post Decision | Охватывает Ops? | Git-Native | Jetix Fit |
|---|---|---|---|---|---|---|
| **Nygard ADR** | Tech decisions | 1–2 стр. | Post | Нет | Да | Высокий |
| **MADR** | Tech decisions (structured) | 0.5–3 стр. | Post | Нет | Да | Лучший для tech |
| **Rust RFC** | Language features | 5–20 стр. | Pre → Post | Нет | Да | Слишком тяжёлый |
| **Oxide RFD** | Любые решения, вкл. ops/business | 1 предложение → много | Pre → Post → Committed | Да | Да | **Лучший overall** |
| **Amazon 6-Pager** | Strategic plans | 6 стр. ровно | Pre-decision | Да | Нет | Quarterly planning |

**Jetix RFD Template** (Oxide-style с YAML frontmatter):

```markdown
---
# File: jetix/decisions/NNNN-short-title.md
authors: Ruslan <ruslan@jetix.ai>
state: prediscussion  # prediscussion | ideation | discussion | published | committed | abandoned
discussion: (ссылка на PR когда в discussion state)
date: YYYY-MM-DD
---

# RFD NNNN: {Title}

## Problem Statement

{Какую проблему мы решаем? Почему это важно сейчас?}

## Background

{Контекст, необходимый для понимания проблемы.}

## Proposal

{Конкретное описание решения. Код, config, process steps где уместно.}

## Alternatives Considered

{Что ещё рассматривалось? Почему не выбрано?}

## Questions / Open Issues

- [ ] {Вопрос 1}
- [ ] {Вопрос 2}

## Impact

* Agents affected: {список}
* Tooling changes: {yes/no + описание}
* Rollback plan: {как откатить если не работает}
```

---

## Часть G — Infrastructure Minimum Viable

### G1. Monorepo tools — verdict: оверкилл (just + Makefile)

Стандартные monorepo tools — Turborepo (Vercel), Nx (Nrwl), Moon, Lage (Microsoft), Bazel — все построены для JS/TypeScript-экосистем. [Сравнение](https://marmelab.com/blog/2026/03/12/taskfile-alternative-makefile.html) нерелевантно для Jetix Python + Markdown стека.

Реальный вопрос: когда Jetix нужны *какие-либо* monorepo tools?

| Team Size | Рекомендация |
|---|---|
| 1 founder + AI agents (сейчас) | Plain folders + `just` (justfile). Никаких monorepo tools. |
| 2–5 humans + agents | `just` + [uv workspaces](https://docs.astral.sh/uv/concepts/workspaces/) для Python packages |
| 5–20 engineers | Evaluate Nx (если добавляется JS) или Pants/Bazel |
| 20+ engineers | Turborepo/Nx/Bazel в зависимости от стека |

[Community consensus](https://discourse.charmhub.io/t/make-vs-just-a-detailed-comparison/16097): `just` строго лучше `make` как task runner (не для dependency graphs).

### G2. Git workflow (trunk-based для solo)

Три модели:
- **GitFlow**: два permanent branches + три transient. [Paul Hammant](https://trunkbaseddevelopment.com/): *"People who practice GitFlow will find trunk-based very different."* Слишком тяжёлый для solo+AI.
- **GitHub Flow** ([Scott Chacon, 2011](https://scottchacon.com/2011/08/31/github-flow/)): один принцип — `main` всегда deployable. Хорошо для team 2–5.
- **Trunk-Based Development** ([trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/)): все коммитят в `main` минимум раз в 24h. Feature flags для in-progress. Практикуется в Google (35,000 developers, single monorepo). **Для Jetix сейчас — оптимально**.

### G3. Secrets: SOPS + age

**SOPS** ([github.com/getsops/sops](https://github.com/getsops/sops), Mozilla Public License 2.0): editor encrypted files, поддерживает YAML/JSON/ENV/INI. Шифрует leaf *values*, оставляет keys в cleartext → encrypted файлы diff-able в Git.

**age** ([filippo.io/age](https://filippo.io/age)): современное простое file encryption. Small explicit keys, no config options, UNIX-composable. `apt install age` на Ubuntu 22.04+.

```yaml
# .sops.yaml
creation_rules:
  - path_regex: secrets/.*\.yaml$
    age: >-
      age1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

```bash
sops encrypt --age age1xxx secrets/anthropic.yaml > secrets/anthropic.enc.yaml
sops edit secrets/anthropic.enc.yaml       # редактирует in-place, re-encrypts
sops exec-env secrets/anthropic.enc.yaml 'python -m jetix.agent'
git diff HEAD secrets/anthropic.enc.yaml   # показывает изменения ключей (не значений)
```

Почему SOPS + age идеально для Jetix: secrets в Git (company-as-code ethos), нет external dependency, offline, GDPR-compliant, diff-able.

### G4. IaC: Terraform hcloud + Coolify + systemd

```hcl
# infra/terraform/main.tf
terraform {
  required_providers {
    hcloud = { source = "hetznercloud/hcloud", version = "~> 1.45" }
  }
}
resource "hcloud_server" "jetix_main" {
  name        = "jetix-main"
  server_type = "cpx32"
  image       = "ubuntu-24.04"
  location    = "nbg1"
}
```

([terraform-provider-hcloud](https://registry.terraform.io/providers/hetznercloud/hcloud/latest/docs))

**[Coolify](https://coolify.io/)**: open-source self-hostable alternative to Heroku/Vercel/Netlify. Push-to-deploy via Git. Free SSL. 280+ one-click services. **Ключевое**: native Claude integration для debugging deployments. No vendor lock-in — настройки на own server. Предпочтительнее Dokploy для Jetix.

```ini
# infra/systemd/jetix-agent.service
[Unit]
Description=Jetix Agent Runner
After=network.target
[Service]
Type=simple
User=ruslan
WorkingDirectory=/home/ruslan/jetix-os
EnvironmentFile=/etc/jetix/agent.env
ExecStart=/home/ruslan/jetix-os/.venv/bin/python -m jetix.agent
Restart=on-failure
RestartSec=10
```

### G5. Backup: restic → Hetzner Storage Box + Backblaze B2

```bash
#!/usr/bin/env bash
# scripts/backup.sh — вызывается через: sops exec-env secrets/backup.enc.yaml bash scripts/backup.sh
set -euo pipefail
export RESTIC_REPOSITORY="b2:jetix-backup"

restic backup ~/jetix-os \
  --exclude="~/jetix-os/.git" \
  --exclude="~/jetix-os/.venv" \
  --tag "daily"

restic forget --prune \
  --keep-daily 7 \
  --keep-weekly 4 \
  --keep-monthly 12

restic check

curl -fsS --retry 3 "https://hc-ping.com/${HC_UUID}" > /dev/null
echo "Backup complete: $(date -u)"
```

Primary backup → [Hetzner Storage Box](https://www.hetzner.com/storage/storage-box/) (€3.20+/mo, SFTP/WebDAV, GDPR, same network = free transfer). Secondary offsite → [Backblaze B2](https://www.backblaze.com/cloud-storage/pricing) ($6/TB/mo, S3-compatible, разная geography).

RPO: 24 часа (daily backup 3 AM UTC). RTO: < 2 часа (Terraform recreates server, restic restore from B2). DR Test frequency: ежеквартально.

### G6. Monitoring MVP

| Инструмент | Тип | Цена | Self-Host | Use Case |
|---|---|---|---|---|
| **Uptime Kuma** | Uptime monitoring | Free (OSS) | Да | HTTP/TCP/DNS/port checks + status page |
| **Healthchecks.io** | Cron monitoring | Free (20 checks) | Optional | Dead man's switch для cron jobs |
| **Sentry** | Error tracking | Free (5K errors) | Optional | Python exceptions, stack traces |
| **Netdata** | Server metrics | Free (OSS agent) | Да | Per-second CPU/RAM/disk/network, ML anomaly |
| **BetterStack** | Managed monitoring | Free (10 monitors) | Нет | Альтернатива Uptime Kuma (без self-host) |

([Uptime Kuma GitHub](https://github.com/louislam/uptime-kuma); [Healthchecks.io](https://healthchecks.io/); [Sentry pricing](https://sentry.io/pricing/); [Netdata](https://www.netdata.cloud/))

**Явно не нужно сейчас**: Kubernetes/Helm/Istio, Prometheus+Grafana (slишком много maintenance для solo), HashiCorp Vault, Turborepo/Nx/Bazel, GitFlow, Jira/SAFe/Scrum ceremonies.

### Финальная таблица: Jetix Infrastructure MVP Stack

| Слой | Инструмент | Почему | Стоимость |
|---|---|---|---|
| Task runner | `just` (justfile) | Проще Make, self-documents, YAML-free | Бесплатно |
| Secrets | SOPS + age | Git-native encrypted secrets; offline; no SaaS | Бесплатно |
| Human secrets | 1Password + `op` CLI | Biometric, browser integration | $2.99/mo |
| Git workflow | Trunk-based | Проще всего для solo; масштабируется | Бесплатно |
| IaC | Terraform + hcloud | Reproducible server from code | Бесплатно |
| App deployment | Coolify | PaaS-like, Claude integration, git push | Бесплатно (OSS) |
| Local services | Docker Compose | Multi-container orchestration | Бесплатно |
| Persistent services | systemd | Встроен в Ubuntu 24.04 | Бесплатно |
| Backup primary | restic → Hetzner Storage Box | Same network, GDPR, дёшево | €3.20+/mo |
| Backup offsite | restic → Backblaze B2 | Разная geography, S3-compat | ~$1–5/mo |
| Uptime monitoring | Uptime Kuma / BetterStack | HTTP checks + status page | Бесплатно |
| Cron monitoring | Healthchecks.io | Ping-based dead man's switch | Бесплатно |
| Error tracking | Sentry (free) | Python exceptions + stack traces | Бесплатно |
| Server metrics | Netdata (OSS) | Per-second metrics, ML anomaly, zero config | Бесплатно |

**Итого ongoing cost**: ~€5–10/month (преимущественно Hetzner Storage Box).

---

## Часть H — Практическая Jetix Implementation

### H1. Финальная folder structure

```
jetix-os/
│
├── .claude/                           # Claude Code configuration
│   ├── agents/                        # Subagent definitions (project-level, in git)
│   │   ├── researcher.md              # Deep research specialist
│   │   ├── writer.md                  # Content + documentation
│   │   ├── cto.md                     # Technical architecture decisions
│   │   ├── delivery-lead.md           # Project coordination
│   │   ├── sales.md                   # Client communication
│   │   └── ...                        # 12 agents total
│   ├── commands/                      # /slash-commands (simple)
│   │   ├── ingest.md
│   │   ├── ask.md
│   │   └── plan-day.md
│   └── skills/                        # Skill libraries (complex, multi-file)
│       ├── ingest/SKILL.md
│       ├── consolidate/SKILL.md
│       └── build-graph/SKILL.md
│
├── life-os/                           # L0: Ruslan как личность (root layer)
│   ├── roles/                         # Личные роли Ruslan (father, learner, CEO...)
│   ├── decisions/                     # Личные ADRs (non-company)
│   ├── okrs/                          # Личные OKRs
│   └── wiki/                          # Личная база знаний
│
├── jetix/                             # L0–L7: компания Jetix
│   ├── roles/                         # Abstract role specs (role = contract)
│   │   ├── cto.md                     # Purpose + Domains + Accountabilities
│   │   ├── delivery-lead.md
│   │   ├── researcher.md
│   │   └── ...                        # Все 12 ролей
│   │
│   ├── executors/                     # Кто исполняет роль (decoupled from role)
│   │   ├── agents/                    # AI-агенты как executors
│   │   │   ├── claude-cto.yaml        # executor: role=cto, model=opus, version=1.2.0
│   │   │   └── claude-researcher.yaml
│   │   └── humans/                    # Future human executors
│   │       └── ruslan.yaml            # Ruslan как executor некоторых ролей
│   │
│   ├── prompts/                       # SemVer'd prompt library
│   │   ├── cto/
│   │   │   ├── v1.0.0/system.md      # Immutable — никогда не изменяется
│   │   │   └── v1.1.0/system.md      # + few-shot examples added
│   │   └── researcher/
│   │       └── v1.2.0/system.md
│   │
│   ├── evals/                         # Golden datasets per agent
│   │   ├── cto/golden.jsonl           # 10+ test cases для CTO agent
│   │   ├── researcher/golden.jsonl
│   │   └── README.md                  # Eval process documentation
│   │
│   ├── decisions/                     # Oxide-style RFDs
│   │   ├── 0001-use-sops-for-secrets.md
│   │   ├── 0002-promptfoo-vs-deepeval.md
│   │   └── README.md                  # RFD index + process description
│   │
│   ├── postmortems/                   # Blameless postmortems
│   │   ├── 2026-04-01-researcher-hallucination.md
│   │   └── README.md                  # How to write a postmortem
│   │
│   ├── okrs/                          # Company OKRs in Git
│   │   └── 2026-Q2.md                 # €50K target + KRs as checkboxes
│   │
│   ├── projects/                      # 8 активных проектов (existing)
│   ├── templates/                     # T-01..T-12 canonical templates (existing)
│   ├── wiki/                          # 557 страниц knowledge base (existing)
│   └── tasks/                         # Active task queue
│
├── docs/                              # Diátaxis 4 формы (public-facing)
│   ├── tutorials/                     # Learning-oriented
│   ├── how-to/                        # Goal-oriented
│   ├── reference/                     # Information-oriented (agent frontmatter, etc.)
│   ├── explanation/                   # Understanding-oriented (why SemVer, why RFD)
│   └── mkdocs.yml                     # MkDocs Material config
│
├── infra/                             # Infrastructure-as-Code
│   ├── terraform/                     # Hetzner server provisioning
│   │   └── main.tf
│   ├── docker-compose.yml             # Langfuse + Coolify local stack
│   ├── systemd/                       # Persistent service units
│   │   └── jetix-agent.service
│   └── coolify/                       # Coolify app definitions
│
├── secrets/                           # SOPS-encrypted secrets (in git)
│   ├── anthropic.enc.yaml
│   ├── hetzner.enc.yaml
│   └── backup.enc.yaml
│
├── tools/                             # Python pipelines (existing)
│   ├── transcribe/
│   ├── extract/
│   ├── filter/
│   └── review/
│
├── scripts/                           # Utility bash scripts
│   ├── backup.sh
│   ├── cost_audit.py
│   └── check_prompt_version.py
│
├── .github/
│   └── workflows/
│       ├── eval.yml                   # Eval-on-push для промптов
│       ├── docs.yml                   # Vale + markdownlint + lychee
│       └── cost-check.yml             # Weekly token budget audit
│
├── .sops.yaml                         # SOPS encryption rules
├── .vale.ini                          # Vale prose linter config
├── .pre-commit-config.yaml            # Pre-commit hooks
├── justfile                           # Task runner recipes
├── promptfooconfig.yaml               # Promptfoo eval config
└── README.md                          # Project overview + quickstart
```

**Объяснение ключевых решений по структуре**:

- **`life-os/` отдельно от `jetix/`**: Nested hierarchy из research brief — Life-OS = root, Jetix = один из проектов. Личные решения (личные ADRs, личные OKRs) не смешиваются с компанией.
- **`roles/` отдельно от `executors/`**: Holacracy principle — role ≠ person/agent. Роль CTO существует независимо от того, кто её исполняет сейчас. Завтра CTO может быть нанятый человек — только `executors/humans/cto.yaml` добавится, `roles/cto.md` не изменится.
- **`prompts/<agent>/vX.Y.Z/`**: иммутабельное versioning. Нельзя редактировать `v1.0.0/system.md` после деплоя — нужно создать `v1.1.0/`.
- **`decisions/`**: Oxide-style RFDs покрывают все решения — tech, business, operational. Single source of truth для "почему мы это решили".
- **`secrets/` в git**: SOPS-encrypted — secrets в git (company-as-code ethos) без риска утечки.
- **`.claude/agents/` vs `jetix/prompts/`**: `.claude/agents/*.md` — active agent definitions (что Claude читает прямо сейчас), `jetix/prompts/` — full version history prompt library. Active agent файл содержит pointer на текущую версию.

### H2. Tools recommendations для Jetix Q2 2026

| Категория | Выбор | Обоснование | Альтернативы отклонены потому что |
|---|---|---|---|
| **Eval tool** | Promptfoo CLI + Langfuse self-hosted | Promptfoo: native GitHub Actions YAML, CLI-first, free. Langfuse: OSS, self-hostable, prompt registry + tracing + eval в одном | LangSmith: нет self-host; Braintrust: нет OSS; DeepEval: хорошо для pytest, но Langfuse покрывает больше |
| **Docs** | MkDocs Material | Python-стек → нет React/Node overhead; `mkdocs gh-deploy` → GitHub Pages; 50k+ organizations; Material theme out-of-the-box | Docusaurus: React/MDX оверкилл для solo Python; Sphinx: RST слишком тяжёлый; Mintlify: платный SaaS |
| **Secrets** | SOPS + age | Git-native, offline, company-as-code ethos — secrets diff-able в git без утечки значений; age: simple, modern, UNIX-composable | 1Password Teams: платный, SaaS dependency; Doppler: платный при >3 users; Vault: enterprise overkill |
| **Monitoring** | Uptime Kuma + Healthchecks.io + Sentry free + Netdata | Полное покрытие: uptime + cron health + app errors + server metrics; всё free tier для solo scale | Prometheus+Grafana: слишком много maintenance overhead для solo |
| **Backup** | restic → Hetzner Storage Box + B2 | Primary: same network (free transfer) + GDPR + cheap. Offsite: B2 другая geography + S3-compat | BorgBackup: сложнее restic без преимуществ на solo; AWS S3: дороже B2 |
| **Task runner** | just (justfile) | Проще Make, no YAML, `just --list` self-documents recipes, `apt install just` на Ubuntu 24.04 | Make работает, но quirky syntax и PHONY targets раздражают; Taskfile: YAML синтаксис — extra dependency |
| **Decision records** | Oxide-style RFDs | Охватывает бизнес + tech + операционные решения; pre-decision discussion; lifecycle state machine | Nygard ADR: только tech, только post-decision; MADR: аналогично ADR по scope |
| **Git workflow** | Trunk-based solo | Минимальная complexity; eval gate на push заменяет PR review; масштабируется до команды через GitHub Flow | GitFlow: слишком много branches, ceremony без value для solo; GitHub Flow: нужен PR — избыточно для solo |
| **Deploy** | Coolify | Native Claude integration для debugging; git-push-to-deploy; no vendor lock-in; 280+ one-click services | Dokploy: менее dev-friendly, нет Claude integration; Heroku/Railway: платные SaaS, vendor lock-in |
| **Prompt registry** | git + папки (сейчас) | При 12 агентах git folders + Langfuse tags достаточно; не нужен отдельный service | Langfuse Prompt Management: включается позже при >20 агентах или team collaboration |

### H3. Git workflow recommendation

**Сейчас (solo + 12 AI agents): Trunk-based**

```bash
# Day-to-day работа
git add jetix/prompts/cto/v1.1.0/system.md
git commit -m "feat(prompts/cto): v1.1.0 — add domain scoping to architecture decisions"
git push origin main  # eval.yml запускается автоматически
```

Eval gate на push: если Promptfoo eval падает — push rejected (через pre-push hook или требование CI green для защищённого main).

**+1 collaborator: GitHub Flow**

```bash
git checkout -b prompts/researcher-v1.3.0
# редактируем, тестируем локально
just eval researcher  # запуск eval локально
git push origin prompts/researcher-v1.3.0
# GitHub Actions: eval + PR review required
# merge → auto-deploy (update .claude/agents/researcher.md pointer)
```

**Team 5+: Trunk-based + feature flags**

```bash
# Рискованные изменения промптов за feature flag
git commit -m "feat(prompts/sales): v2.0.0-beta — new output format [flag: sales-v2]"
# В runtime: if FEATURE_FLAG["sales-v2"]: use v2.0.0 else use v1.5.2
```

**Scale-up правила**:
- Solo → GitHub Flow: при добавлении первого человека-коллаборатора
- GitHub Flow → Trunk+flags: при team size > 5
- Trunk+flags → Trunk+monorepo tools: при team size > 20

### H4. 14-day L1 Foundation rollout plan

| День | Работа | Deliverable | Критерий "готово" |
|---|---|---|---|
| **Day 1** | Repository init, folder structure, README | Структура `jetix-os/` с `life-os/`, `jetix/`, `docs/`, `infra/`, `secrets/`; `.gitignore`; initial commit | `git log --oneline` показывает initial commit; все папки созданы |
| **Day 2** | SOPS + age setup, первый encrypted secret, Git hooks | `secrets/anthropic.enc.yaml`; `.sops.yaml`; pre-commit hook для проверки незашифрованных secrets | `sops edit secrets/anthropic.enc.yaml` работает; `git diff` показывает только ключи, не значения |
| **Day 3** | Justfile с базовыми командами | `justfile` с командами: `eval`, `backup`, `deploy`, `docs-serve`, `lint`, `cost-check` | `just --list` показывает все команды; `just docs-serve` поднимает MkDocs locally |
| **Day 4** | `.claude/agents/*.md` refactor | Все 12 агентов в new frontmatter schema с `version: 1.0.0`, `model:`, `effort:`, `tools:` | `claude code` загружает все агенты без ошибок; frontmatter валиден |
| **Day 5** | Первый `jetix/roles/<role>.md` + matching `executors/agents/<name>.yaml` | `jetix/roles/cto.md` (Purpose + Domains + Accountabilities в Holacracy-стиле) + `jetix/executors/agents/claude-cto.yaml` | Role и executor файлы созданы; reviewer (Ruslan) может ответить "что делает CTO" глядя только на файл |
| **Day 6** | Первый prompt в `prompts/<agent>/v1.0.0/system.md` с SemVer workflow | `jetix/prompts/cto/v1.0.0/system.md` — иммутабельная версия | Файл существует и не изменяется после коммита; версия отражена в `.claude/agents/cto.md` frontmatter |
| **Day 7** | Первый golden dataset (10 кейсов для 1 роли) | `jetix/evals/cto/golden.jsonl` — 10 test cases в JSONL формате | `promptfoo eval -c promptfooconfig.yaml` запускается без ошибок на golden dataset |
| **Day 8** | Promptfoo CI setup, GitHub Actions eval-on-push | `.github/workflows/eval.yml` | Push с изменением в `prompts/**` запускает eval; CI зелёный = merge разрешён |
| **Day 9** | Langfuse self-host через docker-compose на Hetzner | `infra/docker-compose.yml` с Langfuse; Claude Code hook для tracing | Langfuse UI доступен на `http://hetzner-ip:3000`; трейсы видны после agent run |
| **Day 10** | MkDocs Material docs site, Diátaxis 4 папки, deploy на GitHub Pages | `docs/` с 4 Diátaxis папками; `mkdocs.yml`; GitHub Pages deployment | `mkdocs gh-deploy` успешен; сайт доступен по URL |
| **Day 11** | Vale + markdownlint + lychee CI | `.github/workflows/docs.yml`; `.vale.ini` | Push с изменением в `docs/**` запускает lint; Vale catches style violations |
| **Day 12** | Первый Oxide-style RFD | `jetix/decisions/0001-use-sops-for-secrets.md` в state `published` + `jetix/decisions/README.md` с процессом | RFD написан по template; state = `committed` после имплементации SOPS |
| **Day 13** | Postmortem template + README с примером | `jetix/postmortems/README.md`; `jetix/postmortems/template.md`; пример `2026-04-13-first-test-postmortem.md` | Команда `/postmortem` (или `just postmortem`) создаёт новый файл по template |
| **Day 14** | Monitoring stack + restic backup | Uptime Kuma (Docker on Hetzner); Healthchecks.io account; Sentry free project; Netdata installed; `scripts/backup.sh`; cron entry | `just backup` работает без ошибок; Healthchecks.io показывает check в UP state |

**После Day 14**: L1 Foundation активен. Начинается первый 6-недельный Shape Up цикл.

### H5. Golden Dataset Creation Process

**Процесс создания 10 кейсов × 12 ролей = 120 golden examples**:

**Шаг 1 — AI-generated seed** (Claude из real voice-memos + задокументированных задач):
```jsonl
{"id": "cto-001", "input": {"task": "Выбери между PostgreSQL и MongoDB для хранения agent traces"}, "expected_output": {"format": "structured_analysis", "sections": ["decision", "rationale", "alternatives", "tradeoffs"]}, "evaluator": "llm-rubric", "risk_tier": "mid", "tags": ["architecture", "database"]}
{"id": "cto-002", "input": {"task": "Напиши ADR для выбора MkDocs vs Docusaurus"}, "expected_output": {"format": "madr_template", "required_fields": ["context", "decision", "consequences"]}, "evaluator": "schema-match", "risk_tier": "low", "tags": ["documentation", "adr"]}
```

**Шаг 2 — Ruslan review**: бинарная разметка (good/bad) + комментарий где нужно

**Шаг 3 — Eval типы по risk tier**:

| Evaluator Type | Когда использовать | Bias Risk |
|---|---|---|
| `exact-match` | Детерминированный вывод (схемы, числа) | Нет |
| `schema-match` | JSON/YAML output validation | Нет |
| `llm-rubric` | Качество рассуждений, tone, completeness | Verbosity + position bias ([Zheng et al.](https://arxiv.org/abs/2306.05685)) |
| `contains` | Обязательные ключевые слова/фразы | Нет |
| `cost` | Token budget assertions | Нет |

**Update frequency**: после каждого postmortem → добавить failure case; weekly review во время Shape Up cool-down; при major SEMVER bump — добавить 5+ новых кейсов.

**Bias mitigation для LLM-as-judge**: swap positions и average, chain-of-thought в judge prompt, reference-guided grading для фактических задач.

### H6. Prompt Versioning Workflow

```bash
# Создание новой версии промпта
git checkout -b prompts/cto-v1.1.0

# Копируем и редактируем
cp jetix/prompts/cto/v1.0.0/system.md jetix/prompts/cto/v1.1.0/system.md
# ... вносим изменения ...

# Локальный eval
just eval cto
# под капотом: npx promptfoo eval -c promptfooconfig.yaml --filter-pattern "cto"

# Если pass > 90% → коммит
git add jetix/prompts/cto/v1.1.0/
git commit -m "feat(prompts/cto): v1.1.0 — add structured output format for ADR generation"

git push origin prompts/cto-v1.1.0
# GitHub Actions: full eval + diff report vs v1.0.0

# После merge в main → update .claude/agents/cto.md pointer
# frontmatter: version: 1.0.0 → version: 1.1.0
git checkout main
git pull
sed -i 's/version: 1.0.0/version: 1.1.0/' .claude/agents/cto.md
git commit -m "chore(agents/cto): update to v1.1.0"
git push origin main
```

**Rollback** при регрессии:
```bash
# Откат прост — иммутабельные версии
sed -i 's/version: 1.1.0/version: 1.0.0/' .claude/agents/cto.md
git commit -m "revert(agents/cto): rollback to v1.0.0 — regression in ADR format"
git push origin main
```

### H7. Jetix Postmortem Template

(см. полный шаблон в Части E6 выше — используется без изменений)

**Конкретные детали для Jetix**:
- Файл в `jetix/postmortems/YYYY-MM-DD-<slug>.md`
- Slug: kebab-case краткое описание инцидента (например, `researcher-hallucination-arxiv`)
- Status workflow: DRAFT → (Claude review) → REVIEWED → (action items resolved) → CLOSED
- Action items трекаются как GitHub Issues с тегом `postmortem`
- При наличии Agent-related incident: обязательно секция 5 "AI-Specific Factors"

### H8. Jetix RFD Template

(см. полный шаблон в Части F6 выше)

**Процесс работы с RFD в solo режиме**:
1. Создай файл `jetix/decisions/NNNN-title.md` с `state: prediscussion`
2. Заполни Problem Statement и Background → `state: ideation`
3. Напиши Proposal → открой PR → `state: discussion`
4. Claude review: `claude code "Review RFD NNNN for logical consistency and completeness"`
5. Merge PR → `state: published`
6. После имплементации → `state: committed`

**Индекс RFDs** (`jetix/decisions/README.md`):
```markdown
# Jetix Decision Records

| RFD | Title | State | Date |
|---|---|---|---|
| [0001](0001-use-sops-for-secrets.md) | Use SOPS + age for secrets | committed | 2026-04-02 |
| [0002](0002-promptfoo-vs-deepeval.md) | Eval framework selection | published | 2026-04-10 |
```

### H9. Scale-up Triggers

| Тригер | Solo (сейчас) | +1 executor | +5 executors | +20 | +100 |
|---|---|---|---|---|---|
| **Git workflow** | Trunk-based, commit to main | GitHub Flow, short branches, PR required | Trunk + feature flags | Trunk + flags + merge queue | Trunk + monorepo tools |
| **Secrets** | SOPS + age personal | SOPS + team keys (multiple recipients) | SOPS + Doppler for env sync | Vault или Doppler Enterprise | Vault cluster |
| **Evals** | Promptfoo CLI + Langfuse | + Langfuse Teams (annotation workflows) | Langfuse self-hosted + regression suite | + Braintrust for regression benchmarks | + custom eval infra |
| **Docs** | MkDocs Material | same | + versioning (`mike`) | + Algolia search | + Mintlify public |
| **Decisions** | RFD by founder (self-review) | RFD + 1 human review | RFD + 2 reviews + FCP | RFD circles | RFD + OKR synchronization |
| **Deploy** | Coolify single box | Coolify + staging env | Coolify + k3s | k3s managed | Managed Kubernetes |
| **Monitoring** | Free tiers (Uptime Kuma, Sentry, Netdata) | same | Grafana Cloud free | Self-host Prometheus + Grafana | Full observability platform |
| **Agents** | 12 AI agents (Claude Code) | 12 AI + 1 human | 12 AI + 5 humans | Mixed team, explicit accountability matrix | Holacracy circles for humans + AI |

**Triggers для перехода**:
- **Solo → +1**: первый платный клиент с access или первый human collaborator
- **+1 → +5**: €50K ARR achieved; начало L4 Agency scaling
- **+5 → +20**: L6 Platform tier; Series A equivalent
- **+20 → +100**: L7 Portfolio tier; product-led growth

### H10. Anti-patterns to Avoid (Jetix-specific)

**1. Строить полный Kubernetes кластер "для будущего"**
Solo founder строит 3 недели k8s без клиента. Coolify + systemd покрывает все текущие нужды. K8s — trigger +20 executors.

**2. Перфекционизм в golden datasets**
10 хорошо размеченных кейсов лучше, чем 100 идеальных через месяц. Golden dataset начинает работать при 10 кейсах; 50 — достаточно для качественного regression suite ([Hamel Husain](https://hamel.dev/blog/posts/evals/)). Начать сейчас, улучшать итерационно.

**3. Scrum ceremonies с AI-агентами**
Никаких standups, sprint planning или retrospectives с 12 агентами. Shape Up cycle: shaping → betting → building → cool-down. Это убивает velocity ([Basecamp Shape Up](https://basecamp.com/shapeup)).

**4. Копировать GitLab Handbook целиком**
2,000+ страниц неподъёмно для 1 founder. Начать с `company/`, `engineering/`, `roles/`, `agents/` — расширять только когда есть реальная боль от отсутствия документа.

**5. Over-engineering prompt registry**
При 12 агентах git + папки + Langfuse tags достаточно. Отдельный сервис registry — когда > 20 агентов или team collaboration требует UI.

**6. Дублирование Notion как source of truth**
Git = SoT. Notion = view (читалка для human-friendly UI). Никогда не редактировать в Notion то, что есть в Git — Notion MCP используется только для read.

**7. Eval всё подряд без risk tiering**
Запускать Opus на каждом eval case = быстро сжечь бюджет. Risk-based routing: PATCH изменения → Haiku для eval, MAJOR изменения → Opus. Cost assertions в каждом test case (`threshold: 0.01` per call).

**8. Игнорировать Hallucination Budget baseline**
Нельзя детектировать regression без baseline. Первые 2 недели production: measure и document hallucination rate даже без action — это baseline для будущих alertов.

---

## Заключение

Восемь принципов L1 Foundation Jetix — не абстрактные идеалы, а конкретные файлы и инструменты:

| Принцип | Файл / Инструмент | Day в плане |
|---|---|---|
| Git + Markdown как БД | Весь монорепо `jetix-os/` | Day 1 |
| Prompt-as-code SemVer | `jetix/prompts/<agent>/vX.Y.Z/system.md` | Day 6 |
| CI/CD для промптов | `.github/workflows/eval.yml` + Promptfoo | Day 8 |
| Diátaxis docs | `docs/` 4 папки + MkDocs Material | Day 10 |
| Blameless postmortems | `jetix/postmortems/` + template | Day 13 |
| Hallucination Budgets | Langfuse metrics + `evals/` | Day 9 |
| Risk-based routing | Promptfoo tiers в `promptfooconfig.yaml` | Day 8 |
| Decision Records | `jetix/decisions/` Oxide RFD | Day 12 |

**14-дневный rollout** — это путь от пустого репозитория до полностью работающей company-as-code операционной системы. Каждый день имеет конкретный deliverable и проверяемый критерий готовности.

**Scale path ясен**: структура спроектирована для мега-корпорации с Day 1. Роли отдельно от исполнителей. Промпты версионированы и иммутабельны. Решения документированы и searchable. Инфраструктура кодирована и воспроизводима.

Единственный анти-паттерн, которого нельзя допустить: ждать "идеального момента" для начала. 10 golden cases хуже 100 идеальных — но они будут работать завтра. `git init` + первый коммит сегодня запускает flywheel institutional memory, который невозможно воссоздать постфактум.

**"Perfect is the enemy of deployed."** Day 1 начинается с `git init`.

---

*Версия документа: 1.0.0 | Дата компиляции: 2026-04 | Источники: 40+ primary fetches | Все URLs верифицированы на момент research*

*Следующие шаги: написать `design/JETIX-ARCHITECTURE-FINAL.md` (архитектурный overview) → написать `docs/INSTRUCTIONS.md` (daily operational guide) → создать `jetix/roles/cto.md` как первую роль → запустить Day 1 rollout.*
