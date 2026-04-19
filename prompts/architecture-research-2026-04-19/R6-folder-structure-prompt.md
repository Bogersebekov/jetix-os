---
research-id: R6
wave: 2
topic: Folder structure patterns для solo → mega-corp (scale-up-first design)
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/folder-structure-deep-research-2026-04-19.md
priority: P1 (критично — блокирует D2 Folder Structure финальный документ)
builds-on: R2 дал draft (Part H1), R6 должен stress-test и финализировать
---

# R6 — Folder Structure Patterns solo → mega-corp

## Зачем этот research

R2 (company-as-code) уже дал **draft folder structure** для Jetix monorepo. Но это именно draft — нужен stress-test:

- Какие **alternative structures** существуют (academic, industry, open-source examples)?
- Как структура **эволюционирует** от solo (текущее) к 5, 20, 100, 500 executors?
- **Naming conventions** — что работает, что ломается
- **Deprecation patterns** — как archive старую роль / проект / папку
- **Nested Life-OS / Jetix** (R7 parallel) — specific folder implications
- **Cross-cutting concerns** — где хранится то что не fits в one category
- **Конфликты при scale** — какие папки растут неконтролируемо

Выход — **финальный stress-tested draft** для `design/JETIX-FOLDER-STRUCTURE.md` (D2).

## Как использовать

Скопируй **`=== PROMPT START ===` до `=== PROMPT END ===`** в Perplexity Max Computer. Собственная вкладка, параллельно R4, R5, R7.

---

=== PROMPT START ===

Ты — senior software architect с deep expertise в monorepo patterns, organizational file systems, и scaling code/data organization. Я прошу **глубокий академический research** по теме: **folder structure patterns для AI-native компании, которая начинается как solo-operator с AI-агентами и масштабируется до mega-corporation, с минимальным rebuild требованием**.

Это stress-test research — у меня уже есть draft structure (из предыдущего research). Нужны альтернативы, критика, и финальная recommendation.

## Контекст проекта Jetix (2000 слов)

**Jetix** — AI-native mega-corporation под одного founder (Ruslan, Берлин) + 12+ AI-агентов через Claude Code. Git monorepo на GitHub. Hetzner сервер.

**Архитектура:** 7 слоёв (L1 Foundation → L7 Portfolio) + L0 Executive Core. **Nested hierarchy:** Life-OS = root, Jetix = один из проектов. Scale-up-first design (10x growth без rebuild).

**Human + AI executors через единую role-abstraction** — роль-manifest абстрактна, AI сегодня / человек завтра.

**10 core alphas:** Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem.

**12 AI-роли:** strategic-management (Ruslan), manager, strategist, sales-lead, sales-research, sales-outreach, delivery, analyst, knowledge-synth, meta-agent, inbox-processor, crazy-agent, personal-assistant, system-admin, life-coach. Number is not constant — scale до 30/100/200+.

## Wave 1 draft structure (от R2)

R2 предложил следующую структуру (как starting point — нужно stress-test):

```
jetix-os/                             # Root monorepo
├── life-os/                          # Nested: личная OS
│   ├── decisions/
│   ├── OKRs/
│   ├── letters/
│   ├── health/
│   ├── reflection/
│   └── wiki/                         # Life knowledge (отдельно от jetix/wiki)
│
├── jetix/                            # Business part
│   ├── roles/                        # Abstract role definitions (Holacracy-style)
│   │   ├── sales-lead.md
│   │   ├── delivery.md
│   │   └── ...
│   ├── executors/
│   │   ├── agents/                   # AI-agent concrete implementations
│   │   │   └── claude-sales-lead.yaml
│   │   └── humans/                   # Future: человек assigned к role
│   │       └── (empty for now)
│   ├── prompts/                      # Prompt-as-code (SemVer)
│   │   └── <agent>/
│   │       └── vX.Y.Z/
│   │           └── system.md
│   ├── evals/
│   │   └── <agent>/
│   │       └── golden.jsonl
│   ├── decisions/                    # Oxide RFDs
│   ├── postmortems/
│   ├── letters/                      # Monthly/quarterly letters
│   ├── alphas/                       # (proposed) lifecycle entities
│   │   ├── clients/
│   │   ├── projects/
│   │   └── ...
│   └── wiki/                         # Business knowledge (existing 557 pages)
│
├── docs/                             # Diátaxis 4 forms
│   ├── tutorials/
│   ├── how-to/
│   ├── reference/
│   └── explanation/
│
├── .claude/
│   └── agents/                       # Claude Code agent pointers (YAML frontmatter)
│       └── sales-lead.md
│
├── infra/
│   ├── docker-compose.yml
│   ├── systemd/
│   └── coolify/
│
├── secrets/                          # SOPS-encrypted
│   └── anthropic.enc.yaml
│
├── tools/                            # Python pipelines (existing)
│   ├── transcribe/
│   └── ...
│
├── scripts/                          # Bash utilities
│
├── .github/workflows/
│   ├── eval.yml
│   ├── docs.yml
│   └── cost-check.yml
│
├── justfile                          # Task runner
├── promptfooconfig.yaml
└── README.md
```

**Проблемы в draft который нужно stress-test:**

1. **life-os/** внутри jetix-os/ monorepo — это nested hierarchy, но запутывает (есть `life-os/wiki/` и `jetix/wiki/`, есть два `decisions/` и два `letters/`)
2. **`roles/` vs `executors/` split** — теоретически красиво, но удобно ли в ежедневной работе
3. **`prompts/vX.Y.Z/` иммутабельность** — как практически работает при 100+ версий промптов для 30+ ролей
4. **`alphas/`** — новая папка, не ясно где заканчивается alpha и начинается project / client / research note
5. **Scale** — при 1000 clients в `clients/`, 500 projects в `projects/` — как structure работает
6. **Cross-cutting** — документ, который relevant для 5 клиентов, 2 проектов и одной стратегии — где живёт
7. **Life/Jetix separation** — когда пора переходить в отдельные репозитории/серверы (R7 parallel research)

## Основной research-запрос

### Часть A — Monorepo vs Multi-repo: academic and industry

1. **Monorepo пример кейсы:**
   - **Google monorepo** (Piper, Blaze/Bazel) — 2 billion LoC scale patterns. Rachel Potvin paper «Why Google Stores Billions of Lines of Code in a Single Repository» (ACM 2016).
   - **Facebook/Meta monorepo** — similar scale, EdenFS filesystem.
   - **Microsoft monorepos** (Windows, Office) — VFS for Git.
   - **GitLab mono-mode** vs. multi-repo.
   - **Twitter's Birdcage / Pants** — build system.

2. **Multi-repo examples:**
   - Netflix — many repos.
   - Most startups default to multi-repo.
   - Tradeoffs vs monorepo.

3. **Tools for monorepo at scale:**
   - Bazel (Google), Buck2 (Meta), Pants (Twitter)
   - Nx (JavaScript-focused), Turborepo (Vercel)
   - Moon (newer, multi-language)

4. **When monorepo breaks** — known antipatterns, when migrate.

5. **Jetix context** — data + code + docs + prompts monorepo. Не pure code monorepo. Какие tools applicable.

Источники: Potvin & Levenberg ACM 2016 (Google), Meta engineering blog, Microsoft Dev Blogs, Nx documentation, Turborepo documentation. «Monorepo vs polyrepo» academic reviews.

### Часть B — Industry reference cases

Deep-dive на successful monorepo structures в comparable scale (1-100 people orgs):

1. **GitLab Handbook repo** (~2000 страниц, open source) — folder structure деталей:
   - `/company/`, `/people-group/`, `/engineering/`, `/security/`, etc.
   - Почему organized по function не по team
   - DRI pattern

2. **Oxide Computer** — RFD process, `rfd/` folder structure.

3. **Solarwinds / Tailscale / Clerk / Linear** — public repos если есть.

4. **Obsidian community vaults** — PKM-style monorepos. How they grow.

5. **Zettelkasten / Niklas Luhmann** — flat numbering system at 90000 cards. Scalability lessons.

6. **Academic research labs** — `/projects/`, `/papers/`, `/data/` patterns. LaTeX overleaf mirroring.

7. **Notion workspaces** — сравнение folder/page hierarchy patterns.

### Часть C — Naming conventions (deep-dive)

1. **Кей-case variants:**
   - kebab-case (jetix-standard)
   - snake_case
   - PascalCase
   - camelCase
   - Когда какой

2. **Date prefixes:**
   - `YYYY-MM-DD-<slug>.md` — sorted chronologically
   - Когда date prefix needed (decisions, letters, activities)
   - Когда counter-productive (concepts, entities)

3. **Hierarchical numbering:**
   - `0001-use-sops-for-secrets.md` (RFD-style)
   - `001/002/003` subfolder numbering
   - Luhmann Zettelkasten `1, 1a, 1a1, 1b` pattern

4. **Slug design:**
   - Длина (short vs descriptive)
   - Special chars (no periods, spaces)
   - Uniqueness strategies

5. **Versioning в filenames:**
   - `file-v1.md` vs `file.md.v1` vs folder `v1/file.md`
   - R2 предложил `prompts/<agent>/vX.Y.Z/system.md` — критика

6. **Reserved names:**
   - `README.md`, `INDEX.md`, `_meta.md`
   - `.hidden` files для meta
   - What patterns established

### Часть D — Scale patterns: solo → 5 → 20 → 100 → 500 executors

Для каждой фазы — какая structure работает, какие boundaries пересматриваются.

1. **Solo (0-1 executor, 10 projects):**
   - Minimal structure
   - Everything flat if possible
   - Jetix current state

2. **Small team (2-5 executors):**
   - Clear ownership per folder
   - Collaboration workflows
   - PR reviews

3. **Team (5-20 executors):**
   - Functional subfolders
   - DRI model (GitLab-style)
   - Automated ownership (CODEOWNERS)

4. **Department scale (20-100):**
   - Multiple functions
   - Cross-team коллабурация patterns
   - Shared vs team-specific folders

5. **Division scale (100-500):**
   - Consider multi-repo split
   - Or BFG repo management
   - Sharding strategies

6. **Mega-corp (500+):**
   - Multiple monorepos per division
   - Shared libraries pattern
   - Data warehouse separate

7. **Triggers для structural refactors:**
   - Folder > 500 entries (performance, cognitive load)
   - Cross-cutting concerns > 20% of edits
   - Build times degrade
   - Search results polluted

### Часть E — Deprecation and archival patterns

Папки растут, но нужно и освобождать.

1. **Archive folders:**
   - `_archive/` внутри каждого parent (Jetix uses это)
   - Top-level `archive/` folder
   - Separate archive branch
   - Git submodule для архивов

2. **Soft delete:**
   - Move to `_archive/` but keep in repo
   - Historical access preserved

3. **Hard delete:**
   - Git rm + commit
   - Still in git history
   - BFG для полной очистки

4. **Role/project deprecation:**
   - Closing a role — куда его manifest
   - Closing a project — куда его artifacts
   - When keep linked, when untangle

5. **Dated archives:**
   - `archive/2025/` by year
   - `archive/closed-projects/` by status

6. **Retention policies:**
   - How long keep active
   - When truly delete (GDPR)

### Часть F — Cross-cutting concerns

Data/artifacts которые не fit в один clear parent.

1. **Shared knowledge** — документ, relevant для multiple clients/projects/strategies
   - Tag-based (wiki tags)
   - Symlinks (existing Jetix niches pattern)
   - Multiple locations (duplicate)
   - Parent + references

2. **Templates:**
   - `templates/` top-level (Jetix current)
   - Или per-domain (`decisions/templates/`, `clients/templates/`)
   - Both patterns, hybrid

3. **Configurations:**
   - `.config/`, `config/`, `.env`, YAML + TOML + JSON
   - When each

4. **Temporary files:**
   - `tmp/`, `.cache/`, `workspace/`
   - In `.gitignore`?

5. **External dependencies:**
   - `vendor/` for locked deps
   - Submodules for third-party references
   - Когда copy vs submodule

### Часть G — Nested Life-OS / Jetix specific

1. **Option 1: Fully nested в одном monorepo**
   - `jetix-os/life-os/` + `jetix-os/jetix/`
   - Pros: единый репо, simple backup
   - Cons: смешение metrics, attention allocation confusion

2. **Option 2: Separate folders in same repo**
   - `life-os/` + `jetix/` at root
   - Simpler than Option 1 nesting
   - Currently proposed

3. **Option 3: Separate repos linked via submodules**
   - `life-os` repo + `jetix` repo
   - Submodule для cross-references
   - Pros: clean separation
   - Cons: submodule complexity

4. **Option 4: Separate repos, independent**
   - Max separation
   - No automated cross-reference
   - Migration path к этому eventually

5. **Evolution triggers:**
   - Когда нужно перейти Option 2 → 3 → 4
   - Data flow between (Life-OS insights → Jetix strategy)

### Часть H — Специфичные Jetix зоны

Детально для каждой key folder — что внутри, как расти, антипаттерны.

1. **`wiki/`** (existing 557 pages) — уже работает. Ожидаемые изменения при scale.

2. **`roles/` vs `executors/`** — правильный split или over-engineered?
   - Alternative 1: `roles/<name>/manifest.md` + `roles/<name>/executor.yaml` combined
   - Alternative 2: single `agents/<name>/` with all

3. **`prompts/<agent>/vX.Y.Z/`** — production-ready SemVer pattern? Or over-engineered?
   - Alternative: `prompts/<agent>.md` + git log for history
   - When SemVer adds value

4. **`alphas/` folder** — should exist как separate?
   - Alternative 1: inside `clients/`, `projects/` (R5 proposal)
   - Alternative 2: только state tracking в `events.jsonl`
   - Alternative 3: hybrid

5. **`decisions/`** — RFD format. Numbering.
   - `decisions/0001-...md` vs `decisions/2026-04/001-...md`
   - Scale implications

6. **`daily-log/`** — existing. Scale: 3 years = 1000 files. Still flat? Year subfolders?

7. **`projects/`** — active + archived. Consistent naming.

### Часть I — Tooling for structure enforcement

1. **Git hooks для naming validation** (pre-commit, pre-push)
2. **CI checks** (structure compliance GitHub Actions)
3. **Linting tools:**
   - markdownlint для format
   - Custom scripts для structure
   - Obsidian-compatible validation
4. **Search tools:**
   - ripgrep, ugrep, fzf
   - Obsidian search
   - DuckDB queries
5. **Visualization:**
   - `tree` command
   - Obsidian graph view
   - Custom scripts generating SVG

### Часть J — Практические выходы для Jetix

**Самая важная часть.**

1. **Финальная stress-tested folder structure** для Jetix monorepo (с явной улучшением vs R2 draft если есть):

```
(полное дерево с комментариями что куда)
```

2. **Naming convention spec** — concrete:
   - Dates format
   - Slug format
   - File extensions
   - Reserved names
   - Numbering

3. **Scale-up evolution table:**
   - Solo (now) / Small team / Team / Department / Division / Mega-corp
   - Какие папки добавить / разделить / архивировать

4. **Deprecation/archive protocol** для Jetix:
   - Когда archive (triggers)
   - Куда (`_archive/` pattern)
   - Retention policy
   - GDPR implications

5. **Cross-cutting concerns решение** — tags / symlinks / references

6. **Life-OS vs Jetix boundary** — сейчас recommendation, migration path.

7. **10 zonalized decisions** — конкретные choices с rationale:
   - `roles/` vs `executors/` split? → Решение + почему
   - `prompts/vX.Y.Z/` или alternative? → Решение
   - `alphas/` отдельно или inside other? → Решение
   - Decisions numbering? → Решение
   - И т.д.

8. **Migration plan от current state:**
   - Current structure (что есть)
   - Target structure (recommended)
   - Step-by-step migration (что когда переносить)
   - Breaking points (что ломает current workflows)
   - Estimated time

9. **Anti-patterns специфичные Jetix:**
   - Over-engineered structure для 2 clients
   - Under-engineered (everything flat при 500 entries)
   - Mixing life и jetix metrics
   - Orphan folders (no-one owns)

10. **Success criteria** — как узнать что structure хорошая:
    - Onboarding nового executor < 1 hour
    - Find any item < 2 minutes
    - No duplicate truth
    - Structure survives 10x growth

## Format требования

- **Объём:** 5000-10000 слов
- **Parts A-J** structured
- **Visual tree diagrams** для structures
- **Code blocks** для scripts/conventions
- **Tables** для comparisons
- **Primary citations**

## Anti-patterns

- ❌ Копия R2 draft без критики
- ❌ Generic «monorepo lessons» без Jetix-specific adaptation
- ❌ Ignoring nested Life-OS requirement
- ❌ Без Part J

## Критерий успеха

На основе research я могу:
1. Написать `design/JETIX-FOLDER-STRUCTURE.md` (D2) финальный чистовик
2. Migrate current structure к recommended
3. Setup git hooks для structure enforcement
4. Document naming conventions
5. Plan archival protocol

Приступай. Stress-test the R2 draft, academic, practical.

=== PROMPT END ===

---

## Notes для Ruslan

**Output file:** `raw/research/folder-structure-deep-research-2026-04-19.md`

**Критическая связь с R7** — оба касаются Life-OS vs Jetix separation.
