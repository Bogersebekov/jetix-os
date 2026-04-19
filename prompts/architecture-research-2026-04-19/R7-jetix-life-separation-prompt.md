---
research-id: R7
wave: 2
topic: Jetix vs Life-OS separation — nested hierarchy implementation, migration path
target-tool: Perplexity Max Computer (DeepMode)
expected-output-length: 5000-10000 слов
expected-runtime: 30-90 минут
output-file: raw/research/jetix-life-separation-deep-research-2026-04-19.md
priority: P1 (критично — блокирует D4 Jetix vs Life-OS Separation финальный документ)
builds-on: R3 (концепт nested hierarchy), R2 (folder draft), R6 (folder structure parallel)
---

# R7 — Jetix vs Life-OS Separation: nested hierarchy implementation

## Зачем этот research

Ruslan утвердил **Модель D: Nested hierarchy**:
- **Life-OS** = корневая операционная система жизни founder'а
- **Jetix** = один из проектов Life-OS с полноценной 7-слойной архитектурой внутри
- **Полное разделение ресурсов** (часы / деньги / внимание считаются отдельно)
- **Сейчас:** один физический сервер, разные папки
- **Будущее:** отдельные серверы / репозитории

**НЕ ясно:**

1. **Физический split:** folder / submodule / separate repo / separate server — когда что?
2. **Shared foundation:** L0 Core + L1 Foundation + L2 Cognitive — общие или дублируются?
3. **Cross-references:** как Life-OS ссылается на Jetix insights (и наоборот) без tight coupling?
4. **Migration triggers:** когда фактически пора делать hard split (отдельные репозитории)?
5. **Backup & DR:** как handle с разделённой системой?
6. **Access control:** будущий team видит только Jetix, не Life-OS (private)?
7. **Sync patterns:** если две системы — как держать synchronized важные связи?
8. **Time accounting:** как трекать что часы относятся к Jetix vs Life-OS (Toggl tags? separate tools?)

Выход — D4 Jetix vs Life-OS Separation финальный чистовик с concrete implementation.

## Как использовать

`=== PROMPT START ===` до `=== PROMPT END ===` в Perplexity Max Computer. Собственная вкладка, параллельно R4, R5, R6.

---

=== PROMPT START ===

Ты — senior architect по distributed systems, personal digital operations, и life-work integration patterns. Я прошу **глубокий академический research** по теме: **как правильно разделить Life-OS (personal operating system) и Jetix (business company) когда они nested — Life-OS = root, Jetix = один из проектов — но нужна scale path к полному физическому разделению**.

Это specific architecture research — у нас уже утверждён concept nested hierarchy, нужна implementation.

## Контекст проекта (2000 слов)

**Ruslan** — founder Jetix, Берлин. Ведёт **Life-OS** (личная operating system) и строит **Jetix** (AI-native company, mega-corp target).

**Утверждённая модель (Модель D, Nested hierarchy):**
- Life-OS = root (моя жизнь)
- Jetix = один из проектов Life-OS
- Jetix сам имеет полную 7-слойную архитектуру (L0-L7)
- Полное разделение ресурсных P&L (часы / деньги / внимание отдельно)
- Ruslan «открывает» Jetix и работает в нём как полноценный пользователь/управленец отдельной компании

**Текущие проекты Life-OS (previewed в R3):**
- Health & Energy
- Learning / Engineering Thinking  
- Relationships
- Personal Finance
- Reflection / Journal
- **Jetix** (самый крупный из проектов)

**Jetix 7-слойная архитектура:**
- L0 Executive Core (Ruslan strategic-mgmt + 12 AI-агентов + future human team)
- L1 Foundation (software practices: git, prompt-as-code, CI/CD, docs-as-code)
- L2 Cognitive (Левенчук ШСМ: 5 примитивов)
- L3 Product, L4 Delivery, L5 Membrane, L6 Topology, L7 Portfolio

**Критические факты:**

1. **Jetix target — mega-corporation.** Не solo, не small business. Design закладывается под 10x scale без rebuild.

2. **Jetix имеет будущую команду** (human executors, C-level) — они **не должны** видеть Life-OS данные.

3. **Life-coach агент** (существующая роль Jetix) — фактически живёт в Life-OS, не в Jetix. Но через ту же role-abstraction (роль одна, исполнитель — тот же Claude Code).

4. **Текущая инфраструктура:**
   - **Сервер:** один Hetzner CPX32 Nuremberg
   - **Repo:** один GitHub monorepo (`github.com/Bogersebekov/jetix-os` — название misleading, оно для both)
   - **Путь:** `~/jetix-os` на сервере
   - **Claude Code:** центральный, через которого работают обе OS

5. **Future infrastructure (когда разделится):**
   - Отдельный сервер для Jetix (business-grade, team access)
   - Отдельный сервер для Life-OS (personal, private)
   - Возможно разные облака (Jetix в EU compliance для Mittelstand, Life-OS private VPS)

## Wave 1 findings

**R3 (Левенчук):**
- Role-abstraction единая для обеих OS
- Alphas могут быть shared (Hypothesis alpha как в Life-OS так и в Jetix — разные instances, общий pattern)
- Writing rituals (daily-log, quarterly letter) могут быть separate per OS

**R2 (Company-as-code):**
- Draft: `jetix-os/life-os/` + `jetix-os/jetix/` как nested folders
- SOPS + age для secrets
- Separate docs per domain

**R1 (Career levels):** не напрямую касается separation, но подтвердил Jetix scale-up-first design.

## Ключевые вопросы этого research

1. **Какой physical split pattern** правильный для Phase 1 (сейчас) → Phase 2 (team) → Phase 3 (mega-corp)?

2. **Какие компоненты shared** между Life-OS и Jetix (если есть), какие полностью separate?

3. **Как cross-references работают** (Life-OS поcmotrел insight из Jetix или наоборот)?

4. **Когда exact trigger** для hard split (отдельные серверы, отдельные репо)?

5. **Как сохранить continuity** если Jetix = один из проектов Life-OS, но потом станет независимой корпорацией?

6. **Access control и privacy** — как обеспечить что будущая Jetix team не видит Life-OS?

7. **Time accounting** — как трекать что часы это Jetix vs Life-OS без manual effort?

8. **Backup strategy** — unified или separate? Crash recovery?

## Основной research-запрос

### Часть A — Personal OS + Business OS patterns (existing)

1. **Personal operating systems (academic + practical):**
   - Tiago Forte «Building a Second Brain» (2022) — PARA method (Projects/Areas/Resources/Archive)
   - Thomas Frank «Ultimate Brain» Notion template
   - August Bradley «PPV» (Pillars, Pipelines, Vaults)
   - Matt Ragland's PKM systems
   - Nat Eliason's Effortless Output
   - Obsidian / Logseq patterns для life management

2. **Founder dual-operating-systems:**
   - Tim Ferriss «4-Hour Workweek» separation patterns
   - Naval Ravikant's frameworks
   - Paul Graham's essays on founder life
   - Derek Sivers patterns

3. **Work-life integration vs separation:**
   - Cal Newport «Deep Work» — time-blocking patterns
   - «Burnout» research — separation as health mechanism
   - Academic papers on work-life boundaries

4. **Notion / Obsidian workspace patterns:**
   - Multi-workspace vs single-workspace
   - Sidebar organization для dual-context

5. **Dual-brain pattern:**
   - Personal brain (health, learning, relationships)
   - Business brain (company, clients, ops)
   - When separate, when merged

Источники: Tiago Forte «Building a Second Brain», Cal Newport books, Naval Ravikant Almanack, academic work-life integration papers, Obsidian/Logseq community. 

### Часть B — Technical separation patterns

1. **Monorepo with folders:**
   - `project-root/life-os/` + `project-root/jetix/` — current proposal
   - Pros: single git, simple backup, unified tooling
   - Cons: смешение в git log, access control limited

2. **Monorepo with submodules:**
   - `life-os/` as submodule → `github.com/ruslan/life-os-private`
   - `jetix/` as submodule → `github.com/Bogersebekov/jetix-os`
   - Pros: granular access control, clear boundary
   - Cons: submodule complexity, sync challenges

3. **Separate repos, linked via scripts:**
   - Two completely separate git repos
   - Cross-references через scripts (symlinks, pandoc includes)
   - Pros: clean, independent
   - Cons: no native cross-linking

4. **Same repo, different branches:**
   - `main` = jetix, `life` branch = life-os
   - Anti-pattern (разные purposes на разных branches)

5. **Separate servers:**
   - One server Jetix, другой Life-OS
   - Pros: physical separation, different security postures
   - Cons: infrastructure overhead

6. **Git worktrees:**
   - Same repo, different working trees
   - Useful для development but не для separation

7. **Monorepo tools для isolation:**
   - Bazel/Buck2 visibility rules
   - Nx projects boundaries
   - Turborepo workspaces

### Часть C — Shared vs private компоненты

Критический вопрос: что должно быть shared между Life-OS и Jetix, что private.

**Кандидаты для SHARED:**
- Role-abstraction framework (та же концепция роли-альфы-метода)
- Writing ritual templates (стратегирование, мышление письмом)
- Левенчуковская онтология (L2 Cognitive framework)
- Claude Code config (.claude/ configs могут быть shared)
- Some wiki articles (knowledge, применимое к обеим)

**Кандидаты для PRIVATE TO LIFE-OS:**
- Health metrics, sleep tracking
- Personal finance
- Relationship notes (family, friends)
- Personal journal / reflection
- Personal goals (non-business)

**Кандидаты для PRIVATE TO JETIX:**
- Client data (GDPR critical)
- Financial records (business)
- Strategic plans, competitive intel
- Employee data (future)
- Internal decisions

**Grey zone:**
- Learning notes (сегодня personal, завтра может стать Jetix training material)
- Ruslan's personal network (some are Jetix prospects, some are friends)
- Ideas (некоторые для Jetix, некоторые personal creative)

Вопрос: как сделать **clear boundary** плюс **easy re-classification** когда context меняется.

### Часть D — Cross-references между Life-OS и Jetix

Когда data живёт в одной, но relevant для другой.

1. **One-way references:**
   - Life-OS может ссылаться на Jetix (personal health affects business)
   - Jetix НЕ ссылается на Life-OS (business не нуждается в personal context)
   - Asymmetric access

2. **Reference patterns:**
   - Symlinks
   - URL references
   - Git submodule shallow reads
   - Copy-to-public с sanitization

3. **Insight flow:**
   - Life-OS reflection → Jetix strategy (insight из медитации в business decision)
   - Jetix postmortem → Life-OS learning (failure taught life lesson)

4. **Privacy preservation:**
   - Quote without attribution
   - Aggregated patterns (health scores) without raw data
   - Selective sharing

### Часть E — Migration path: nested → separate

**Phase 1 (now):** Single repo, folders separation
**Phase 2 (team hires):** Need separation
**Phase 3 (mega-corp):** Fully separate

1. **Trigger triggers для Phase 2:**
   - First human hire к Jetix → нужен clear visibility boundary
   - Team > 3 people → мандатory separation (не могут видеть Ruslan's personal reflections)
   - Client data volume → GDPR compliance requires strong separation

2. **Phase 2 execution:**
   - Extract life-os/ папки → separate repo
   - Update cross-references
   - Setup separate permissions
   - Keep historical context

3. **Phase 3 execution:**
   - Separate server
   - Separate LLM access (Jetix uses company credentials, Life-OS personal)
   - Legal entity implications (Jetix Holdings BV/OÜ)

4. **Rollback protections:**
   - What если хотим revert?
   - Branch archives before migration
   - Test environments

### Часть F — Time, money, attention accounting

Ключевое требование модели D — полное разделение ресурсов.

1. **Time tracking:**
   - Toggl с tags (jetix / life-os / grey-zone)
   - RescueTime patterns
   - Manual vs automatic
   - Granularity (hour / 15min / task-level)

2. **Money tracking:**
   - Separate bank accounts (personal vs Jetix GmbH/UG in future)
   - Business expenses vs personal
   - Tax implications (Betriebsausgaben vs Privatausgaben)
   - Как trackable в Jetix OS (ссылки на банковские данные vs actual numbers)

3. **Attention tracking:**
   - Более subjective
   - Daily reflection («на что ушло внимание»)
   - Weekly audit (хватило ли внимания Jetix L4 Delivery?)

4. **Unified dashboard:**
   - Can one dashboard показать both
   - Or strictly separate

5. **Accounting automation:**
   - Banking APIs
   - Time tracking APIs
   - Plugging into Jetix L7 Portfolio

### Часть G — Access control и privacy

Особенно важно когда будет team.

1. **Git-level access control:**
   - GitHub repo permissions (read/write/admin)
   - Different teams для life-os vs jetix
   - Branch protection rules

2. **Server-level:**
   - Separate users
   - SSH key isolation
   - Filesystem permissions

3. **Encryption at rest:**
   - SOPS encrypted life-os secrets отдельно от jetix
   - Different age keys

4. **LLM access:**
   - Claude Code session могут be contaminated (AI видит оба contexts)
   - Как prevent leaking (e.g., life-os details в Jetix client response)

5. **Backup access:**
   - Кто имеет backup access
   - Recovery procedures

### Часть H — Backup & Disaster Recovery

1. **Separate backup strategies:**
   - Life-OS — personal, possibly cheaper (B2 monthly)
   - Jetix — business-grade, возможно compliance-required
   - Retention periods differ

2. **Cross-OS dependencies:**
   - Что если Life-OS backup fails but Jetix survives
   - Shared Claude credentials в secrets

3. **Test restore procedures:**
   - Quarterly restore test
   - Document steps

4. **Geographic distribution:**
   - Both backups в EU (GDPR)
   - Or Jetix strictly EU, Life-OS less restricted

### Часть I — Identity и authentication

1. **Git identity:**
   - Same email для both?
   - Separate (ruslan@bogersebekov.com vs ruslan@jetix.de)?
   - GPG signing implications

2. **Server SSH:**
   - Same key, different servers
   - Separate keys per context

3. **Third-party services:**
   - Personal Google vs Jetix Workspace
   - Personal Notion vs Jetix Notion
   - When migrate

4. **Two-factor authentication:**
   - Same phone / same authenticator
   - Separate (hard but possible)

### Часть J — Практические выходы для Jetix / Life-OS

**Самая важная часть.**

1. **Phase-by-phase implementation plan:**
   - Phase 1 (now): что конкретно сейчас сделать
   - Phase 2 trigger: какие conditions
   - Phase 2 execution: step-by-step migration
   - Phase 3 trigger и execution

2. **Folder structure Phase 1:**
   ```
   jetix-os/
   ├── life-os/
   │   ├── health/
   │   ├── reflection/
   │   ├── learning/
   │   ├── relationships/
   │   ├── finance/
   │   ├── wiki/              # Life knowledge (separate from Jetix wiki)
   │   ├── decisions/
   │   ├── letters/
   │   └── README.md
   ├── jetix/
   │   └── (full 7-layer architecture)
   └── shared/                 # Optional: shared templates, framework
       ├── role-framework/
       ├── levenchuk-ontology/
       └── writing-templates/
   ```

3. **Shared components decision:**
   - Концрная list: что shared, что не shared
   - Rationale per item

4. **Cross-reference patterns:**
   - Life-OS references Jetix: how
   - Jetix references Life-OS: forbidden (GDPR-ish preparation)

5. **Time accounting system:**
   - Concrete tool recommendation (Toggl + tags structure)
   - Daily review protocol
   - Weekly Jetix vs Life-OS audit

6. **Money separation concrete:**
   - Sofort (сейчас): personal banking, но Jetix получит свой GmbH-account когда зарегистрируется
   - Bookkeeping separation
   - Steuerberater involvement

7. **Access control plan Phase 2:**
   - First Jetix hire: repo permissions, what they see
   - Onboarding checklist
   - Security boundary

8. **Migration triggers (concrete):**
   - 1st human hire → move Life-OS to separate repo
   - 5 employees → separate server
   - 20 employees → maximum separation (different infrastructure)

9. **Backup strategy per phase:**
   - Now: unified (single restic → B2)
   - Phase 2: separate backups, same provider
   - Phase 3: different providers, different locations

10. **Anti-patterns:**
    - Mixing decisions/ (жизненные + бизнес в одной папке) → смешивает metrics
    - Jetix роль читает life-os/ context → privacy breach
    - Shared secrets для personal и business → security leak
    - Unified daily-log (personal + work вперемешку)

11. **10-year vision:**
    - 2026: Phase 1, nested folders
    - 2027: Phase 2 начинается (first hire, separate repo)
    - 2028-2030: Phase 3 (separate infrastructure)
    - 2032+: Jetix полностью autonomous от Life-OS

## Format требования

- **Объём:** 5000-10000 слов
- **Parts A-J**
- **Concrete examples** везде
- **Diagrams** для topology
- **Tables** для phase evolution
- **Primary citations**

## Anti-patterns

- ❌ Generic «work-life balance» без технических specifics
- ❌ Over-engineered (Kubernetes для 1 person)
- ❌ Ignore GDPR implications
- ❌ Без concrete implementation Phase 1
- ❌ Игнор уже утверждённой Модель D

## Критерий успеха

На основе research я могу:
1. Написать `design/JETIX-VS-LIFE-OS.md` (D4) финальный чистовик
2. Implement Phase 1 folder structure этой недели
3. Set time tracking system
4. Define Phase 2 triggers и steps
5. Plan backup strategy

Приступай. Глубоко, конкретно, Jetix-aware.

=== PROMPT END ===

---

## Notes для Ruslan

**Output file:** `raw/research/jetix-life-separation-deep-research-2026-04-19.md`

**Параллельно с R4, R5, R6.** Все 4 в отдельных Perplexity Computer tabs.
