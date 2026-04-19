# R4: Jetix vs Life-OS — Архитектура разделения

> **Путь файла:** `/home/user/workspace/jetix-vs-life-os-research.md`  
> **Статус:** Wave 2 Research Output — основа для `design/JETIX-VS-LIFE-OS.md` (D4)  
> **Дата:** 2026  
> **Автор:** AI Research Agent для Ruslan (Jetix, Berlin)

---

## Executive Summary

Ruslan ведёт две операционные системы: **Life-OS** (root: вся жизнь) и **Jetix** (один из проектов внутри Life-OS, но с корпоративной семилайерной архитектурой). Утверждённая **Модель D (Nested Hierarchy)** — единственный архитектурно зрелый выбор: она разрешает ссылки Life-OS → Jetix, запрещает обратные (GDPR-подготовка к найму), и предусматривает трёхфазную миграцию от монорепо-папок до полностью раздельной инфраструктуры.

Ключевые установки на 2026: (1) единый Hetzner, `~/jetix-os/life-os/` + `~/jetix-os/jetix/` + `~/jetix-os/shared/`, два SOPS-ключа `age-life.pub` / `age-jetix.pub`; (2) Toggl workspace с тегами `jetix:*` / `life:*`; (3) личный банковский счёт с категоризацией до момента Gewerbeanmeldung. Phase 2 (первый найм) — hard trigger для вынесения `life-os/` в отдельное приватное репо и заведения UG haftungsbeschränkt. Обратный порядок действий (сначала разделение кода, потом найм) — ошибка проектирования.

Критическая находка: 85% PKM-систем (PARA, PPV, Ultimate Brain) не решают проблему business/personal разделения — они используют единое пространство с тегами или фильтрами. Model D превосходит их в трёх аспектах: (a) hard boundary на уровне git ACL, (b) GDPR-готовность с Day 1, (c) Jetix спроектирован под 10x без rebuild.

---

## Оглавление

- [Part A — Personal OS + Business OS patterns](#part-a)
- [Part B — Technical separation patterns](#part-b)
- [Part C — Shared vs private components](#part-c)
- [Part D — Cross-references](#part-d)
- [Part E — Migration path: nested → separate](#part-e)
- [Part F — Time, money, attention accounting](#part-f)
- [Part G — Access control & privacy](#part-g)
- [Part H — Backup & disaster recovery](#part-h)
- [Part I — Identity & authentication](#part-i)
- [Part J — Практические выходы](#part-j)

---

<a name="part-a"></a>
## Part A — Personal OS + Business OS patterns

### PARA Method (Tiago Forte, 2022)

[Tiago Forte](https://fortelabs.com/blog/basboverview/) в "Building a Second Brain" (Atria Books, 2022) предложил PARA — четырёхкатегорийную систему организации любой цифровой информации: **Projects** (активные цели с дедлайном), **Areas** (долгосрочные ответственности), **Resources** (потенциально полезные темы), **Archive** (неактивное).

Ключевой момент для нашего контекста: Forte явно указывает, что Projects и Areas охватывают *и work, и personal life одновременно*. PARA не предусматривает архитектурного разделения по типу personal/business — предполагается единый workspace с тегами или разделением внутри категорий. Это рабочий подход для solopreneur, но **принципиально недостаточен для случая с командой Jetix и GDPR**.

Архитектурная разница с Model D:
- PARA: единое пространство, разделение через именование (`Work/Project-X` vs `Personal/Health`)
- Model D: hard boundary на уровне файловой системы + git ACL, с явным asymmetric reference rule

В контексте Jetix PARA может использоваться *внутри каждой OS* как организационный принцип, но не как разделительный механизм между ними.

### August Bradley — PPV (Pillars, Pipelines, Vaults)

[August Bradley](https://esilva.net/tla_insights/ppv_bradley) разработал "Life Operating System" на Notion, построенный вокруг трёх компонентов:
- **Pillars** — организационные категории (здоровье, работа, отношения, творчество), охватывающие *всю жизнь* горизонтально
- **Pipelines** — процессные потоки для достижения целей (Value Goals → Goal Outcomes → Projects → Actions)
- **Vaults** — база знаний с настроенным resurface в нужный момент

PPV ещё более интегративен, чем PARA: Pillars намеренно пересекают work/life границу. Философия Bradley: "there's nothing wrong with doing little segments of your life in different parts of Notion, but when you take it to the next level and really integrate everything — that's what a lot of these superpowers start to arise." Это прямо противоположно Model D.

Что PPV даёт для проекта: хорошая модель для *Life-OS* внутри — Jetix как один из Pillars с полным набором Pipelines. Но разделение business/personal в PPV возможно только через отдельные Notion-аккаунты — не через инфраструктурный контроль.

### Thomas Frank — Ultimate Brain

[Thomas Frank](https://thomasjfrank.com/brain/) реализовал PARA в Notion-шаблоне "Ultimate Brain" с поддержкой GTD. Для разделения work/personal пользователи используют либо два отдельных темплейта (два Notion-аккаунта), либо property `Location: {home, work, errand}` с фильтрами. По отзывам Forte: "If you use Notion as your Second Brain, this is the ultimate template." Граница снова мягкая — программная, не инфраструктурная.

### Obsidian — multi-vault vs single-vault

[Сообщество Obsidian](https://forum.obsidian.md/t/one-vault-vs-multiple-vaults/1445) разделилось на два лагеря:

**Single-vault аргументы:**
- Cross-linking между всеми заметками
- Один бэкап, одна конфигурация плагинов
- Нет context switching
- Рекомендация Preslav Rachev: "start with a single vault; separate only if explicitly necessary"

**Multi-vault аргументы:**
- Жёсткое разделение по GDPR или рабочим требованиям ("I am a person whose work requires rigid separation")
- Контроль синхронизации: work vault — на рабочем компьютере; personal — только на личных устройствах
- Инкрементальная приватность: нельзя случайно связать personal с work через wikilinks

Практический вывод: multi-vault в Obsidian — ближайший аналог Model D на уровне note-taking. Пользователи переходят на multi-vault именно когда появляются командные или compliance требования. **Для Ruslan: life-os/ vault и jetix/ vault, без cross-vault ссылок из Jetix в Life-OS.**

### Cal Newport — Deep Work (2016)

[Cal Newport](https://www.neuyear.net/blogs/productivity/cal-newports-deep-work-time-blocking-method) в "Deep Work" вводит **shutdown ritual** — полное переключение из рабочего режима: просмотр всех задач, подтверждение capture, финальная фраза "Shutdown complete." Это поведенческий эквивалент архитектурного разделения: Context switch с осознанным закрытием рабочего контекста. Поддерживает концепцию разных энергетических "режимов" для Jetix (deep work, execution) и Life-OS (reflection, recovery).

**Time-blocking** у Newport — каждой минуте дана работа. Для двух OS это означает явный тег контекста: "Jetix/L4-Delivery: 09:00–12:00" vs "Life-OS/Health: 07:00–08:00". Без этого метрики смешиваются.

### Paul Graham — Maker's Schedule

[Paul Graham](https://paulgraham.com/makersschedule.html) описывает асимметрию издержек: для maker'а одна встреча в 14:00 уничтожает половину дня. Founders (Ruslan = AI-native founder + maker) работают на maker's schedule. Прямое применение к Model D: время Jetix (L2 Cognitive, L3 Product, L4 Delivery) требует полудневных блоков; переключение на Life-OS (рефлексия, здоровье) — отдельный блок, не прерывание.

Graham пишет: "I never thought of it in these terms, but in effect I had two workdays each day, one on the manager's schedule and one on the maker's." Ruslan имеет два OS — это системное воплощение того же паттерна.

### Naval Ravikant — Almanack

[Naval Ravikant](https://grahammann.net/book-notes/almanack-of-naval-ravikant-eric-jorgenson) формулирует: "Health, Love, and Mission — in that order." Это структурно совпадает с Model D: Life-OS (Health + Relationships) = root; Jetix (Mission) = дочерний проект. Naval также: "Value your time at an hourly rate, and ruthlessly spend to save time at that rate." Прямое применение — Part F (P&L учёт времени).

Leverage framework Naval'а (labour, capital, code, media) описывает Jetix 7-слойную архитектуру: L0 = labour leverage (AI агенты), L7 = capital/code leverage (portfolio компаний).

### Академические паттерны разделения

**Clark (2000) Work/Family Border Theory.** [Sue Campbell Clark](https://journals.sagepub.com/doi/10.1177/0018726700536001) ("Human Relations", vol. 53, №6) описывает work и family как два разных "государства" с разным языком, нормами поведения и задачами. Граница между ними — не физическая, а управляемая через participation (вовлечённость) и flexibility (проницаемость). Ключевой вывод: satisfaction достигается при конгруэнтности личных предпочтений по разделению и организационных структур.

**Kossek & Lautsch (2008) — Boundary Management Styles.** [Kossek and Lautsch](https://www.ellenkossek.com/s/Work-familyboundarymanagementstylesinorganizationsAcross-levelmod.pdf) выделяют три стиля:
- **Separators** — жёсткое разделение ролей по времени и месту, непроницаемые границы
- **Integrators** — высокая гибкость, роли перекрываются
- **Volleyers/Alternators** — гибридный стиль, переключение по необходимости

Для Ruslan-сегодня оптимален **Alternator** на поведенческом уровне: Jetix = deep work blocks; Life-OS = recovery, reflection, health. Но на инфраструктурном уровне — **Separator** (разные repos, ключи, учётные записи). Эта асимметрия поведенческий стиль vs инфраструктурная политика — отличительная черта Model D.

### Итог Part A: где Model D превосходит PKM-паттерны

| Паттерн | Разделение | GDPR-ready | Team-ready | Model D |
|---|---|---|---|---|
| PARA (Forte) | Теги/папки | ❌ | ❌ | Использовать *внутри* каждой OS |
| PPV (Bradley) | Pillars | ❌ | ❌ | Модель для Life-OS structure |
| Ultimate Brain | Property filters | ❌ | ❌ | Не применим |
| Obsidian multi-vault | Hard FS | Частично | Частично | Ближайший аналог |
| Model D | Git ACL + FS permissions | ✅ | ✅ | **Выбранный подход** |

---

<a name="part-b"></a>
## Part B — Technical separation patterns

### 1. Monorepo с папками (текущий черновик из R2)

```
~/jetix-os/
├── life-os/
├── jetix/
└── shared/
```

**Pros:**
- Нулевая сложность setup
- Единая история в git log
- Atomic commits ("life-os: add health note + jetix: update weekly OKR")
- Один clone, один CI pipeline
- Простой поиск по всему дереву

**Cons:**
- GitHub Teams/CODEOWNERS не обеспечивают *истинную* изоляцию — только workflow protection
- Будущий сотрудник Jetix технически может прочитать `life-os/` при наличии repo access
- Grow risk: через 3 года монорепо с личными записями и enterprise кодом неудобен
- Нет server-side ACL — только client-side SOPS шифрование

**Оценка:** Оптимально для Phase 1 (solo). Требует миграции при найме.

---

### 2. Monorepo с git submodules

```
~/jetix-os/
├── .gitmodules  → life-os = git@github.com:ruslan/life-os-private.git
├── life-os/     → submodule (private repo)
├── jetix/
└── shared/
```

**Pros:**
- `life-os` существует как separate private repo — настоящий контроль доступа
- Jetix team: `git clone --recurse-submodules` без `life-os` = не видят приватное

**Cons:**
- Submodules — известный источник friction ("submodule hell")
- Atomic commits невозможны — нужно делать commit в submodule, потом в parent
- CI/CD усложняется: две цепочки secrets, две проверки
- `git pull` требует `--recurse-submodules` или `git submodule update --init`
- Detached HEAD в submodule — распространённая ошибка

**Оценка:** Технически правильно для Phase 2, но высокий DX tax. Альтернатива — отдельный репо без submodule связи.

---

### 3. Separate repos + orchestration

```
~/life-os/     → github.com:ruslan/life-os-private (private)
~/jetix/       → github.com:Bogersebekov/jetix (separate)
~/shared/      → github.com:ruslan/shared-methods (public или private)
```

Orchestration через:
- **Makefile** с target `setup`: клонирует все репо в нужные пути
- **Dotfiles-style symlinks**: `~/.jetix.env → ~/jetix/.env`
- **Ansible/Chezmoi** для machine setup

**Pros:**
- Истинное разделение прав на уровне GitHub
- Разные billing/audit trails
- GDPR: `life-os` только у Ruslan, `jetix` — у команды
- Phase 3-ready

**Cons:**
- Три разных git remote, три набора credentials
- Нет cross-repo atomic commits (нельзя одновременно обновить shared + jetix)
- Shared library updates требуют PR в двух местах
- Onboarding: "clone these 2 repos, not 3"

**Оценка:** Целевой для Phase 2+. До первого найма — overhead без benefit.

---

### 4. Monorepo tools: Nx, Turborepo, Bazel, Pants, Buck2

[Monorepo tools](https://www.youngju.dev/blog/culture/2026-03-24-monorepo-strategy-nx-turborepo-guide-2025.en) решают в первую очередь *build speed и caching*, а не *privacy separation*.

**CODEOWNERS + Nx module boundaries:**
```
# .github/CODEOWNERS
/jetix/   @jetix-team
/life-os/ @ruslan-only
/shared/  @jetix-team @ruslan-only
```

```json
// nx.json — visibility rules
{
  "projects": {
    "life-os": { "tags": ["scope:private"] },
    "jetix": { "tags": ["scope:company"] }
  }
}
```

**ВАЖНО:** [GitHub community](https://github.com/orgs/community/discussions/186401) явно предупреждает: "Tools like CODEOWNERS, branch protection, and required reviews help enforce ownership, but they don't provide true permission isolation." Nx visibility rules — ESLint rules (runtime check), не filesystem ACL.

**Рекомендация:** Nx/Turborepo полезны **внутри** `jetix/` для L1–L7 слоёв когда появится команда. Не для life-os/jetix разделения.

| Tool | Use case | Phase |
|---|---|---|
| Nx | Build graph + module boundaries внутри jetix/ | Phase 2–3 |
| Turborepo | CI caching для jetix/ packages | Phase 2 |
| Bazel/Buck2 | Enterprise scale (1000+ packages) | Phase 3+ |
| CODEOWNERS | Code review assignment | Phase 2 |

---

### 5. Git sparse-checkout + partial clone

[Git sparse-checkout](https://git-scm.com/docs/sparse-checkout) позволяет контролировать какие файлы instantiate в working tree:

```bash
# Jetix team member onboarding:
git clone --filter=blob:none --sparse https://github.com/Bogersebekov/jetix-os.git
cd jetix-os
git sparse-checkout init --cone
git sparse-checkout set jetix/ shared/
# life-os/ НЕ скачивается и НЕ видна в working tree
```

**КРИТИЧЕСКОЕ ОГРАНИЧЕНИЕ:** [Git документация](https://git-scm.com/docs/sparse-checkout) предупреждает: "If commands attempt to access paths in history outside the sparsity specification, then the partial clone will attempt to download additional blobs on demand." История коммитов `life-os/` остаётся в объектной базе репо. Если сотрудник явно запросит `git log -- life-os/` или `git show <commit>`, он получит данные.

**Вывод:** Sparse-checkout — инструмент UX/performance, не security boundary. Достаточен для Phase 1 (нет сотрудников), недостаточен для Phase 2+.

---

### 6. Git worktrees

Git worktrees позволяют иметь несколько working directories с одной git-историей. Это **инструмент разработки**, не разделения. Worktree для `main` и `jetix-feature-branch` — нормальный workflow. Worktrees для life-os/jetix privacy — неприменимо: обе директории читают одну и ту же object database.

---

### 7. Separate servers / separate clouds

```
Phase 3 Architecture:
┌─────────────────┐      ┌──────────────────┐
│  Personal VPS   │      │  Jetix Server    │
│  (или home NAS) │      │  Hetzner CPX32   │
│  Life-OS data   │      │  Jetix workloads │
│  age-life.key   │      │  age-jetix.key   │
└─────────────────┘      └──────────────────┘
```

**Pros:** Истинная инфраструктурная изоляция. GDPR DPA возможна.  
**Cons:** Дорого ($30–50/месяц дополнительно), overhead управления двумя серверами.  
**Trigger:** 5+ сотрудников Jetix или GDPR DPA с enterprise клиентом.

---

### Recommendation Matrix: Phase vs Pattern

| Фаза | Триггер | Паттерн | Инструменты |
|---|---|---|---|
| **Phase 1** (2026, solo) | Сейчас | Monorepo + folders | SOPS+age (2 ключа), CODEOWNERS (Ruslan only) |
| **Phase 2** (первый найм) | 1 сотрудник | Separate repos | `git filter-repo`, два GitHub репо, UG |
| **Phase 2b** (5 сотрудников) | 5 сотрудников | Separate repos + servers | Второй Hetzner VPS, separate domains |
| **Phase 3** (scale) | GDPR DPA / 20+ people | Полная инфраструктурная изоляция | Jetix Legal entity, enterprise GitHub org |

---

<a name="part-c"></a>
## Part C — Shared vs private components

### Компоненты с обоснованием

#### ✅ SHARED (`~/jetix-os/shared/`)

| Компонент | Обоснование |
|---|---|
| **role-framework** (роли Левенчука) | Одна онтология для обеих OS; роль = обезличенная абстракция |
| **Левенчук ШСМ онтология** | Методологическая база, не данные |
| **writing-templates** | Форматы заметок, decision records — без контента |
| **Claude Code skill configs** | Техническая конфигурация агентов; содержимое prompt'ов без контекста |
| **methodology-wiki** | Описание процессов (как делать), не результатов |
| **Obsidian/editor settings** | Конфигурация инструментов |

**Правило для shared:** если компонент описывает *как делать* (method) без конкретных данных о *том, что происходит* (content) — shared.

---

#### 🔒 PRIVATE TO LIFE-OS (`~/jetix-os/life-os/`)

| Компонент | Обоснование |
|---|---|
| **health/** | Медицинские данные — GDPR Special Categories (Art. 9), абсолютно приватно |
| **finance/personal** | Личные банковские данные, активы, налоги |
| **relationships/** | Контакты, переписки, связи — privacy risk |
| **reflection/journal** | Raw мысли, эмоции, личные оценки людей |
| **personal-goals/** | Долгосрочные цели вне Jetix (семья, здоровье, образование) |
| **letters/** | Личная переписка |

---

#### 🔒 PRIVATE TO JETIX (`~/jetix-os/jetix/`)

| Компонент | Обоснование |
|---|---|
| **client-data/** | GDPR Art. 5 — данные клиентов, строго Jetix |
| **business-financials/** | P&L, runway, investor relations |
| **strategic-plans/** | Конкурентная разведка, roadmap |
| **employee-data/** | (будущие) персональные данные сотрудников — GDPR |
| **competitive-intel/** | Бизнес-разведка |
| **L5-membrane/** | Внешние API ключи, партнёрские договора |

---

#### ⚠️ GREY ZONE — правила классификации

**1. Learning notes**

Правило: *Что стало триггером обучения?*
- Читаешь о системах распределённых баз данных для Jetix product → `jetix/L2-cognitive/learning/`
- Читаешь о психологии принятия решений для личного роста → `life-os/learning/`
- Общий курс (ШСМ Левенчук) → `shared/levenchuk-ontology/`

Если неясно — используй тест: "Если этот материал увидит сотрудник Jetix — нормально?" Если нет — в `life-os/`.

**2. Network / Contacts**

Правило: *В каком контексте познакомился?*
- Клиент / потенциальный клиент / партнёр → `jetix/L5-membrane/contacts/`
- Друг / семья / личный ментор → `life-os/relationships/`
- Пересечение (enterprise-контакт, который также личный друг): основная запись в `life-os/relationships/`, ссылка-stub в `jetix/L5-membrane/` с anonymized note: "Friend XY — potential intro to [industry]"

Это asymmetric reference rule в действии: Life-OS знает детали, Jetix получает только business-relevant excerpt.

**3. Creative ideas**

Правило: *Есть ли потенциал монетизации через Jetix?*
- Идея нового AI продукта для enterprise → `jetix/L3-product/ideas/`
- Идея для личного проекта (блог, арт) → `life-os/learning/creative/`
- Неопределённые идеи → `life-os/reflection/ideas-inbox/` (personal inbox) с тегом `#candidate-jetix` для еженедельного ревью

**4. Reflection об усталости / выгорании**

Всегда → `life-os/reflection/`. Jetix dashboards могут видеть *агрегированный health score* (0–10), но не raw текст.

---

<a name="part-d"></a>
## Part D — Cross-references

### Asymmetric Reference Rule

```
Life-OS ──[read/write]──→ Jetix    ✅ разрешено
Jetix   ──[read/write]──→ Life-OS  ❌ запрещено
```

**Обоснование:**
1. **GDPR подготовка:** Когда команда Jetix получит доступ к репо, они не должны иметь возможность читать личные данные Ruslan.
2. **Контекстная гигиена:** Jetix агенты с доступом к `jetix/` не должны получать контекст из `life-os/` — иначе неконтролируемая утечка в LLM.
3. **Ролевая чистота:** По Левенчуку, роль Ruslan-как-founder (в Jetix) не должна знать о роли Ruslan-как-человека (в Life-OS).

### Реализация паттернов cross-reference

#### Паттерн 1: Wiki-links с prefix

В Life-OS заметках (Obsidian/markdown):
```markdown
<!-- В life-os/reflection/weekly-2026-W03.md -->
## Jetix Status
Смотри [[jetix/L7-portfolio/weekly-review-2026-W03]] для деталей.
Energy budget: 8/10 — хватит на L4 Delivery sprint.
```

Это разрешено: Life-OS ссылается на Jetix. Обратное (в `jetix/` → `life-os/`) — никогда.

#### Паттерн 2: Copy-with-sanitization (Insight Flow)

Механизм передачи знаний из Life-OS в Jetix без раскрытия raw данных:

```markdown
<!-- Источник: life-os/reflection/burnout-signals.md (PRIVATE) -->
Три недели подряд сплю меньше 6 часов. Тревожность растёт.
Конкретные ситуации: [список личных событий]

<!-- Dest: jetix/L0-executive/energy-constraints-2026-Q1.md (Jetix-private) -->
# Q1 2026 Energy Constraints
Energy budget: 60% (vs 100% baseline)
Recommendation: reduce L4 sprint velocity by 40% in January.
Rationale: [агрегированный паттерн, без raw personal data]
```

**Правило:** Из Life-OS в Jetix передаётся только *агрегированный вывод* (число, рекомендация), не raw контент.

#### Паттерн 3: Aggregated health score → Jetix capacity planning

```python
# life-os/health/weekly-summary.py (runs locally, never in Jetix)
health_score = calculate_weekly_health()  # 0-10
energy_budget = {
    "score": health_score,
    "jetix_capacity_pct": min(100, health_score * 12),
}
# Export: jetix/L7-portfolio/capacity-input.json
# ТОЛЬКО числа — никакого текста, никаких симптомов
```

#### Паттерн 4: Selective sharing в conversations

Когда Ruslan обсуждает с Jetix агентом: "Мне нужно скорректировать OKR" — причина формулируется без personal details: "Energy constraints identified in personal review suggest 20% capacity reduction for next 6 weeks." Не: "У меня личные проблемы." Jetix агент получает business-relevant fact, не личную информацию.

### Privacy preservation

```
Life-OS raw data → Sanitization layer → Jetix actionable inputs
[health metrics]     [aggregate only]    [capacity %]
[relationships]      [never crosses]     [not exported]
[reflection journal] [never crosses]     [not exported]
[personal finance]   [never crosses]     [not exported]
[strategic analysis] [insights only]     [priority weights]
```

---

<a name="part-e"></a>
## Part E — Migration path: nested → separate

### Overview трёх фаз

```
Phase 1 (2026)                Phase 2 (2027)               Phase 3 (2028+)
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│  ~/jetix-os/     │          │  ~/jetix-os/     │          │  Jetix Server    │
│  ├── life-os/    │  ─────►  │  (jetix only)    │  ─────►  │  (cloud, EU)     │
│  ├── jetix/      │  trigger │  ~/life-os/      │  trigger │  Life-OS Server  │
│  └── shared/     │  =1hire  │  (separate repo) │  =5emp   │  (home/VPS)      │
│  Single Hetzner  │          │  Two repos       │          │  Separate clouds │
└──────────────────┘          └──────────────────┘          └──────────────────┘
```

### Детальная таблица фаз

| Атрибут | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| **Триггер входа** | Сейчас | 1 hire ИЛИ GDPR DPA клиент | 5 сотрудников ИЛИ funding |
| **Репозитории** | 1 monorepo | 2 repos (jetix + life-os) | 2+ repos + org |
| **Серверы** | 1 Hetzner CPX32 | 1-2 Hetzner (jetix-srv + personal) | Jetix: enterprise EU cloud; Life-OS: отдельно |
| **Секреты** | SOPS 2 ключа в одном `.sops.yaml` | SOPS раздельные `.sops.yaml` в каждом репо | HashiCorp Vault для Jetix |
| **Юрлицо** | Freiberufler / нет | UG haftungsbeschränkt | GmbH или established UG |
| **GDPR status** | Self-compliance | DPA готов | Полный compliance |
| **Сложность** | Low | Medium | High |
| **Стоимость/месяц** | €30 (один сервер) | €60–90 (два сервера) | €200–500 (enterprise infra) |

### Rollback protection

**Перед любой фазной миграцией:**
```bash
# 1. Полный снимок состояния
git tag -a "pre-phase2-migration-$(date +%Y%m%d)" -m "Before life-os extraction"
git push --tags

# 2. Бэкап monorepo как bare clone
git clone --bare . ~/backups/jetix-os-backup-$(date +%Y%m%d).git

# 3. Test environment
cp -r ~/jetix-os ~/jetix-os-migration-test
cd ~/jetix-os-migration-test
```

### Phase 1 → Phase 2: Извлечение life-os/

Используем [`git-filter-repo`](https://jboylantoomey.com/post/migrating-subfolder-while-preserving-git-history) — рекомендованная замена `git filter-branch`:

```bash
# Установка
pip install git-filter-repo

# Шаг 1: Создай fresh clone (filter-repo требует чистый clone)
git clone https://github.com/Bogersebekov/jetix-os.git jetix-os-life-extract
cd jetix-os-life-extract

# Шаг 2: Фильтрация — оставить только life-os/ историю
git filter-repo --path life-os/ --path-rename life-os/:

# Шаг 3: Результат — репо с историей только life-os/ файлов
# (путь переименован: life-os/health/ → health/)

# Шаг 4: Создай private репо на GitHub
gh repo create ruslan/life-os-private --private

# Шаг 5: Push
git remote add origin git@github.com:ruslan/life-os-private.git
git push -u origin main

# Шаг 6: В оригинальном jetix-os — удали life-os/
cd ~/jetix-os
git rm -rf life-os/
git commit -m "feat(separation): extract life-os to separate private repo

Phase 2 migration: first hire triggered separation.
life-os/ history preserved in github.com/ruslan/life-os-private
GDPR boundary: life-os data no longer in jetix team repo"

git push

# Шаг 7: Локальная структура
mkdir ~/life-os
git clone git@github.com:ruslan/life-os-private.git ~/life-os
```

**Проверка после миграции:**
```bash
# В jetix-os: убеждаемся что life-os данных нет
git log --all --full-history -- life-os/
# Должно быть пусто после filter-repo

# В life-os: проверяем историю
cd ~/life-os && git log --oneline | head -20
# Должны видеть preserved history
```

### Phase 2 → Phase 3: Раздельные серверы

```bash
# На новом Jetix сервере (Hetzner CX32, EU)
# Создать Jetix-specific user
adduser jetix-svc
# Deploy Coolify, только Jetix workloads
# Настроить отдельный SSH ключ для Jetix deploys

# На личном сервере / Hetzner Storage
# Life-OS данные остаются у Ruslan only
# Отдельный restic repo, отдельный encryption key
```

### Rollback сценарии

| Сценарий | Rollback action |
|---|---|
| filter-repo сломал историю | `git tag pre-phase2-...` → restore from bare clone |
| Потеряли доступ к life-os-private | GitHub backup в Hetzner Storage Box (restic) |
| Phase 3 migration fails | Tag + bare clone перед миграцией; revert = re-clone from bare |
| Секрет скомпрометирован | SOPS re-encrypt с новым ключом; отзыв старого в `~/.sops.yaml` |

---

<a name="part-f"></a>
## Part F — Time, money, attention accounting

### Time Tracking

#### Toggl Structure (Phase 1)

[Toggl Track](https://toggl.com/blog/time-tracking-for-project-management) структура для Phase 1:

```
Workspace: "Ruslan" (один workspace, бесплатный план)
├── Project: "Jetix"
│   ├── Tag: jetix:L0-executive
│   ├── Tag: jetix:L2-cognitive
│   ├── Tag: jetix:L3-product
│   ├── Tag: jetix:L4-delivery
│   └── Tag: jetix:admin
└── Project: "Life-OS"
    ├── Tag: life:health
    ├── Tag: life:learning
    ├── Tag: life:reflection
    ├── Tag: life:relationships
    └── Tag: life:finance
```

**Правило Phase 1:** один workspace, теги как разделитель. Toggl бесплатно поддерживает `Projects + Tags`.

#### Phase 2: два workspace

```
Workspace 1: "Jetix" (платный, team workspace)
├── Members: [Ruslan, Future-hire-1]
├── Projects: client-specific, delivery, admin
└── Reports: billable hours per project

Workspace 2: "Personal" (только Ruslan)
├── Projects: Life-OS
└── Reports: personal time allocation
```

**Важно:** Toggl [поддерживает](https://support.toggl.com/manage-your-teams-time-more-efficiently) разные роли в workspace. Phase 2: сотрудники видят только "Jetix" workspace. Personal workspace — только Ruslan.

#### ActivityWatch (автоматический трекинг)

[ActivityWatch](https://activitywatch.net) — open-source, self-hosted (важно: никаких SaaS — данные на сервере Ruslan):

```bash
# Установка на Hetzner (или локально)
# ActivityWatch работает как background daemon
# Трекает: активное окно, заголовок, временные блоки

# Watchers:
# aw-watcher-window: какое приложение активно
# aw-watcher-afk: AFK detection
# aw-watcher-web: браузерные страницы (опционально)
```

Правила категоризации (ActivityWatch `category_rules.json`):
```json
{
  "categories": [
    {"name": "Jetix/Code", "rule": {"type": "regex", "regex": "jetix|cursor|vscode.*jetix"}},
    {"name": "Jetix/Research", "rule": {"type": "regex", "regex": "notion.*jetix|github.*jetix"}},
    {"name": "Life-OS/Health", "rule": {"type": "regex", "regex": "health|workout|sleep"}},
    {"name": "Life-OS/Learning", "rule": {"type": "regex", "regex": "coursera|obsidian.*learning"}}
  ]
}
```

ActivityWatch может экспортировать данные → Jetix L7 Portfolio dashboard (только Jetix-категории).

#### Granularity: Pomodoro-aligned 25 min

Рекомендация: минимальный блок = 25 минут (один pomodoro). Это:
- Устраняет фрагментацию трекинга
- Совместимо с deep work blocks (Newport: минимум 90 мин = 3–4 pomodoro)
- Практичный порог: всё под 25 мин не трекается отдельно (round up или ignore)

#### Daily 3-line reflection template

```markdown
## Daily Time Reflection — {{date}}
**Украло:** [что поглотило время без плана — макс 1 строка]
**Вложил:** [самый важный завершённый блок — макс 1 строка]  
**Баланс:** Jetix {{X}}h / Life-OS {{Y}}h | Energy: {{1-10}}
```

Сохраняется в `life-os/reflection/daily/{{date}}.md`. Никогда не в `jetix/`.

#### Weekly audit checklist

```markdown
## Weekly Time Audit — W{{week}}
- [ ] Jetix L4 Delivery > 20h? → если нет, причина в L7 journal
- [ ] Life-OS Health > 7h? → exercise + sleep + food prep
- [ ] Deep work blocks > 60% рабочего времени?
- [ ] Admin/meetings < 20% рабочего времени?
- [ ] Поглотители > 10%? → identify и block следующую неделю
```

---

### Money Tracking

#### Phase 1: до Gewerbeanmeldung

Текущая структура — DKB или N26. Категоризация в [YNAB](https://www.youneedabudget.com/) или [Firefly III](https://www.firefly-iii.org/) (self-hosted):

```
Категории расходов:
├── jetix:server (Hetzner, B2 storage)
├── jetix:tools (Claude API, GitHub Pro, Coolify)
├── jetix:education (книги, курсы для Jetix)
├── jetix:legal (юридические консультации)
├── life:housing
├── life:food
├── life:health
├── life:education (личное развитие)
└── life:transport
```

**Важно:** даже в Phase 1 чёткая категоризация критична для налогового учёта будущего.

#### Phase 2: Юридическое лицо — UG vs GmbH vs Estonian OÜ

| Фактор | UG (haftungsbeschränkt) | GmbH | Estonian OÜ |
|---|---|---|---|
| **Стартовый капитал** | €1 (мин.) | €25,000 (€12,500 при регистрации) | €0.01 (рекомендуется €2,500) |
| **Нотариальные расходы** | [€150–€500](https://www.betahaus.com/magazine/gmbh-vs-ug-in-germany-which-business-structure-is-right-for-your-startup-in-2026) | €300–€1,200 | Нотариус не нужен |
| **Срок регистрации** | 4–8 недель | 6–12 недель | 1–2 дня (e-Residency) |
| **Корпоративный налог** | ~30% (KSt + GewSt) | ~30% (KSt + GewSt) | 0% на реинвестированную прибыль |
| **Ведение учёта** | €100–€400/мес | €150–€500/мес | €165+/мес |
| **Reputable для B2B DE** | Средне | Высоко | Низко (German clients prefer DE entity) |
| **Конвертация** | → GmbH при €25k | N/A | → DE branch |
| **Риск для берлинского резидента** | Нет | Нет | [Gefahr: Permanent Establishment в Германии](https://www.reddit.com/r/eResidency/comments/1ne58mz/german_resident_estonian_eresidency_ou_risk_of/) |

**Рекомендация для Ruslan:**

1. **Phase 2a (первый клиентский contract):** UG haftungsbeschränkt. Минимальный капитал, быстро, защищает личные активы, достаточно для немецких клиентов.
2. **Phase 2b (Series A / enterprise клиент ≥€100k ARR):** Конверсия UG → GmbH. Стоимость €800–2,000, 4–8 недель. Сигнал credibility для Mittelstand.
3. **Estonian OÜ:** НЕ рекомендуется пока Ruslan живёт в Берлине — риск Betriebsstätte (Permanent Establishment) в Германии, двойное налогообложение.

**German Steuerrecht:**
- После Gewerbeanmeldung: строгое разделение **Betriebsausgaben** (бизнес-расходы, вычитаемые) vs **Privatausgaben**
- Home office: если designated desk = proportional rent может быть Betriebsausgabe
- Steuerberater: нанять с момента Gewerbeanmeldung — DATEV/Elster система, ежеквартальная Umsatzsteuervoranmeldung

#### Unified dashboard (два datasource)

```
Anti-pattern:                    Правильно:
┌───────────────────┐            ┌──────────────┐  ┌──────────────┐
│ Смешанный график  │            │ Jetix P&L    │  │ Life Finance │
│ jetix+personal    │   vs.      │ (Grafana DS1)│  │ (Grafana DS2)│
│ расходы           │            │              │  │              │
└───────────────────┘            └──────────────┘  └──────────────┘
                                 ↓
                          ┌──────────────┐
                          │ Overview     │
                          │ (read-only   │
                          │  summary)    │
                          └──────────────┘
```

### Attention Tracking

**Ежедневный 3-line шаблон** (см. выше).

**Еженедельный аудит внимания:**
```markdown
## Weekly Attention Audit
**Deep focus (L2/L3/L4 Jetix):** {{X}}% — цель ≥50%
**Admin/ops:** {{Y}}% — предел ≤15%
**Life-OS (health, reflect):** {{Z}}% — минимум 15%
**Погружение без плана (distraction):** {{W}}% — предел ≤10%

**Attention thief этой недели:** [1 конкретный источник]
**Action:** [1 конкретное изменение на следующей неделе]
```

---

<a name="part-g"></a>
## Part G — Access control & privacy

### Git & GitHub

**Phase 1 CODEOWNERS:**
```
# .github/CODEOWNERS
*           @Bogersebekov
/life-os/   @Bogersebekov  # Ruslan only — не добавлять команду
/shared/    @Bogersebekov
/jetix/     @Bogersebekov
```

**Phase 2 CODEOWNERS (после найма):**
```
# В jetix repo (life-os уже отдельный private repo)
*              @jetix-team
/jetix/L0-executive/  @Bogersebekov  # Только Ruslan
```

**Branch protection:**
```yaml
# .github/branch-protection.yaml
branch: main
required_reviewers: 1
dismiss_stale_reviews: true
require_code_owner_reviews: true
restrict_pushes_to: ["Bogersebekov"]  # Phase 1: только Ruslan
```

### Server: Linux permissions

**Phase 1 (single server):**
```bash
# Файловые права для life-os
chmod -R 700 ~/life-os/          # только owner
chmod -R 750 ~/jetix/            # owner + group читают (будущая группа)
chmod -R 755 ~/shared/           # все читают

# Phase 2: отдельный Linux user для Jetix services
adduser jetix-svc
chown -R jetix-svc:jetix-svc /opt/jetix/
# life-os/ остаётся только у ruslan

# Phase 2b: systemd-nspawn container для Jetix workloads
# Изолирует файловую систему на уровне namespace
```

### SOPS+age: раздельные ключи

[SOPS](https://github.com/getsops/sops/discussions/1579) поддерживает несколько age-recipients (ключи через запятую — любой может дешифровать):

```bash
# Генерация ключей
age-keygen -o ~/.config/sops/age-life.key    # Только Life-OS
age-keygen -o ~/.config/sops/age-jetix.key   # Только Jetix
# (опционально) recovery key для обеих
age-keygen -o ~/.config/sops/age-recovery.key

# Извлечь публичные ключи
AGE_LIFE_PUB=$(age-keygen -y ~/.config/sops/age-life.key)
AGE_JETIX_PUB=$(age-keygen -y ~/.config/sops/age-jetix.key)
```

**`.sops.yaml` для Phase 1 (monorepo):**
```yaml
# ~/jetix-os/.sops.yaml
creation_rules:
  - path_regex: life-os/.*\.env$
    age: >-
      age1life_public_key_here
  - path_regex: life-os/.*\.yaml$
    age: >-
      age1life_public_key_here
  - path_regex: jetix/.*\.env$
    age: >-
      age1jetix_public_key_here,
      age1recovery_public_key_here
  - path_regex: jetix/.*\.yaml$
    age: >-
      age1jetix_public_key_here,
      age1recovery_public_key_here
  - path_regex: shared/.*
    age: >-
      age1life_public_key_here,
      age1jetix_public_key_here
```

**Использование:**
```bash
# Для Life-OS секретов: используешь age-life key
SOPS_AGE_KEY_FILE=~/.config/sops/age-life.key sops -d life-os/.env

# Для Jetix секретов: используешь age-jetix key
SOPS_AGE_KEY_FILE=~/.config/sops/age-jetix.key sops -d jetix/.env
```

**Phase 3:** HashiCorp Vault с разными namespaces (`life-os/` secret engine vs `jetix/`), LDAP auth, audit log.

### LLM access (Claude Code)

**Принцип:** Claude Code сессия должна знать только тот контекст, который нужен для текущей задачи.

```
# ~/jetix-os/jetix/CLAUDE.md (Jetix scope)
You are working on Jetix — an AI-native company project.
Your scope: ~/jetix-os/jetix/ and ~/jetix-os/shared/ only.
NEVER read or reference ~/jetix-os/life-os/ or ~/life-os/.
You represent the Jetix organization context.

# ~/life-os/CLAUDE.md (Life-OS scope)  
You are working on Life-OS — personal operating system.
Your scope: ~/life-os/ and ~/jetix-os/shared/ only.
For Jetix-specific work, launch a separate Claude session.
```

**Раздельные API ключи:**
- `ANTHROPIC_API_KEY_LIFE` (личная карточка) → env для Life-OS сессий
- `ANTHROPIC_API_KEY_JETIX` (будущий Jetix Claude for Work account) → env для Jetix сессий

**MCP server restrictions (Phase 2):**
```json
// jetix/CLAUDE.md → MCP tools
{
  "tools": ["filesystem:jetix", "filesystem:shared", "github:jetix"],
  "forbidden": ["filesystem:life-os"]
}
```

**Anti-pattern:** запускать одну Claude сессию с CWD в корне `~/jetix-os/` — агент получает контекст обеих OS.

### GDPR: TOM (Technische und Organisatorische Maßnahmen)

[GDPR Art. 32](https://riscreen.de/en/art-32-gdpr-technical-and-organizational-measures-toms/) требует "appropriate technical and organizational measures":

| TOM категория | Phase 1 мера | Phase 2 мера |
|---|---|---|
| **Encryption at rest** | SOPS+age для secrets | Full-disk encryption (LUKS на Hetzner) |
| **Encryption in transit** | HTTPS/TLS everywhere, SSH | + mTLS для internal services |
| **Access control** | SSH keys, SOPS keys раздельные | GitHub Teams, Linux users разделены |
| **Pseudonymisation** | Contacts → anonymized stubs в Jetix | Formal pseudonymisation policy |
| **Availability** | Restic backups (daily) | Restic + geo-redundant |
| **Audit logs** | Git log | Git log + server auth logs |
| **DPA (Auftragsverarbeitung)** | N/A (solo) | DPA with GitHub, Hetzner, Anthropic |
| **Breach response** | Informal | Formal process doc в jetix/L5-membrane/ |

**Auftragsverarbeitung:** при наличии клиентских данных (GDPR Art. 28) — Ruslan как Data Controller, процессоры (GitHub, Hetzner, Anthropic) = Data Processors. Требуется заключить DPA с каждым:
- [GitHub DPA](https://docs.github.com/en/site-policy/privacy-policies/github-data-protection-agreement)
- Hetzner: EU-based, GDPR-compliant by default
- Anthropic: проверить Enterprise terms

---

<a name="part-h"></a>
## Part H — Backup & disaster recovery

### Phase 1: Unified restic

```bash
# Структура бэкапа Phase 1
# Один restic репозиторий с раздельными тегами

# Hetzner Storage Box (primary, EU)
restic -r sftp:u123456@u123456.your-storagebox.de:/backups backup \
  ~/jetix-os --tag "monorepo"

# Backblaze B2 (secondary, EU region critical!)
restic -r b2:jetix-backup-bucket backup \
  ~/jetix-os --tag "monorepo"

# Schedule: cron daily 03:00
0 3 * * * restic -r ... backup ~/jetix-os --tag daily
0 4 * * 0 restic -r ... backup ~/jetix-os --tag weekly
```

**КРИТИЧНО для GDPR:** B2 bucket должен быть в EU регионе (Amsterdam). Hetzner Storage Box — Nuremberg, Finnland — оба EU. ✅

### Phase 2: Separate restic repos

```bash
# Два отдельных restic репозитория
# Jetix backup (команда может иметь доступ к restore)
JETIX_REPO="b2:jetix-prod-backup"
restic -r $JETIX_REPO \
  --password-file ~/.config/restic/jetix-backup.password \
  backup ~/jetix/

# Life-OS backup (только Ruslan)
LIFEOS_REPO="b2:ruslan-personal-backup"
restic -r $LIFEOS_REPO \
  --password-file ~/.config/restic/life-backup.password \
  backup ~/life-os/
```

**Разные пароли, разные B2 buckets, разные access keys.** Jetix команда (если нужен restore) получает доступ только к `jetix-prod-backup`.

### Phase 3: Enterprise separation

| Хранилище | Jetix | Life-OS |
|---|---|---|
| **Primary** | AWS Backup (eu-central-1) или Leitwerk (DE) | Hetzner Storage Box |
| **Secondary** | Hetzner Storage Box | Backblaze B2 EU |
| **Encryption** | AWS KMS или SOPS (Vault) | age key |
| **Retention** | 90 days daily, 1 year weekly | 30 days daily |
| **Access** | Jetix ops team | Ruslan only |

### Shared Claude credentials — предупреждение

**Если личный Anthropic API ключ используется и для Jetix, и для Life-OS:**
- При компрометации ключа — под угрозой оба контекста
- Решение Phase 1: один ключ, но разные `.env` с явными именами (`ANTHROPIC_LIFE_KEY`, `ANTHROPIC_JETIX_KEY`) даже если значения одинаковые (заготовка для ротации)
- Решение Phase 2: Jetix Claude for Work Organization с отдельным billing и key management

### Test restore — quarterly procedure

```bash
# Quarterly restore test (добавить в calendar)
# 1. Выбрать случайный файл из backup
SNAPSHOT=$(restic snapshots --json | jq -r '.[0].id')
restic restore $SNAPSHOT --target /tmp/restore-test/

# 2. Проверить integrity
diff -r /tmp/restore-test/jetix/L0-executive/ ~/jetix/L0-executive/

# 3. Документировать в jetix/L1-foundation/backup-test-log.md
echo "$(date): Restore test OK, snapshot $SNAPSHOT" >> backup-test-log.md
```

**RTO (Recovery Time Objective):** Phase 1 = 4 часа (single server restore). Phase 2 = 2 часа (separate servers). Phase 3 = 30 минут (enterprise HA).

---

<a name="part-i"></a>
## Part I — Identity & authentication

### Git Identity: conditional includes

[Git `includeIf`](https://jdsalaro.com/tutorial/git-configuration-folder-dependent-conditional-includes/) — встроенный механизм с Git 2.13+:

```ini
# ~/.gitconfig
[user]
  name = Ruslan Bogersebekov
  email = ruslan@bogersebekov.com  # Life-OS default

[includeIf "gitdir:~/jetix-os/jetix/"]
  path = ~/.gitconfig-jetix

[includeIf "gitdir:~/jetix/"]  # Phase 2 separate repo
  path = ~/.gitconfig-jetix
```

```ini
# ~/.gitconfig-jetix
[user]
  name = Ruslan Bogersebekov
  email = ruslan@jetix.de
[commit]
  gpgsign = true
  gpgSigningKey = <jetix-gpg-key-id>
```

**Правило:** коммиты в `life-os/` = `ruslan@bogersebekov.com`, в `jetix/` = `ruslan@jetix.de`. Это важно при публичном Jetix репо — не раскрывает личный email.

### SSH Keys: separate ed25519

```bash
# Генерация ключей
ssh-keygen -t ed25519 -C "ruslan@bogersebekov.com" -f ~/.ssh/id_ed25519_life
ssh-keygen -t ed25519 -C "ruslan@jetix.de" -f ~/.ssh/id_ed25519_jetix

# ~/.ssh/config
Host github.com-life
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_life
  IdentitiesOnly yes

Host github.com-jetix
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_jetix
  IdentitiesOnly yes

Host hetzner-personal
  HostName <personal-server-ip>
  User ruslan
  IdentityFile ~/.ssh/id_ed25519_life

Host hetzner-jetix
  HostName <jetix-server-ip>
  User jetix-svc
  IdentityFile ~/.ssh/id_ed25519_jetix
```

**Использование:**
```bash
# Clone Life-OS repo (через life identity)
git clone git@github.com-life:ruslan/life-os-private.git

# Clone Jetix repo (через jetix identity)
git clone git@github.com-jetix:Bogersebekov/jetix-os.git
```

### GPG/SSH commit signing

```bash
# Phase 1: можно использовать SSH signing (проще чем GPG)
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_jetix.pub

# GitHub: добавить SSH signing key отдельно от auth key
# Settings → SSH and GPG keys → New signing key
```

### Third-party accounts

| Сервис | Life-OS аккаунт | Jetix аккаунт | Когда разделять |
|---|---|---|---|
| Google | ruslan@bogersebekov.com (личный) | ruslan@jetix.de (Workspace) | При регистрации домена |
| Notion | Personal plan | Team plan (Jetix) | При первом найме |
| GitHub | @Bogersebekov | Jetix Org (будущее) | При создании Org |
| Claude/Anthropic | Personal account | Jetix Claude for Work | При первом найме |
| Toggl | Personal workspace | Jetix workspace | При первом найме |
| Domain email | bogersebekov.com | jetix.de | Сейчас (зарегистрировать домен) |

**Домен jetix.de:** зарегистрировать сейчас (€10–15/год через Hetzner или INWX). Google Workspace Business Starter = €6/user/месяц — нужен с первым наймом.

### 2FA: YubiKey рекомендация

**Опция A (рекомендуется):** два YubiKey 5 NFC
- YubiKey #1: Life-OS accounts (Google Personal, боголобный GitHub)
- YubiKey #2: Jetix accounts (Google Workspace, Jetix GitHub Org, Hetzner Jetix)
- Resilience: если один потерян — другой не компрометирует обе OS

**Опция B:** один YubiKey с разными slots
- Slot 1: FIDO2 для личных аккаунтов
- Slot 2: FIDO2 для Jetix аккаунтов
- Минус: потеря = потеря обоих

**TOTP backup:** Aegis (Android) или Raivo (iOS) — отдельные entries с тегами Life/Jetix.

---

<a name="part-j"></a>
## Part J — Практические выходы

### 1. Folder Structure Phase 1 (немедленно)

```
~/jetix-os/                          # git repo: github.com/Bogersebekov/jetix-os
├── life-os/                         # [PRIVATE] Personal operating system
│   ├── health/                      # медицинские данные, workout logs
│   │   ├── weekly-metrics.md
│   │   └── .gitignore              # чувствительные файлы
│   ├── reflection/                  # journal, ретроспективы, решения
│   │   ├── daily/
│   │   ├── weekly/
│   │   └── decisions/              # personal decision log
│   ├── learning/                    # личное обучение (не для Jetix напрямую)
│   │   ├── books/
│   │   ├── courses/
│   │   └── ideas-inbox/            # grey zone: кандидаты для Jetix
│   ├── relationships/               # contacts, network (personal context)
│   ├── finance/                     # личные финансы, банковские выписки
│   │   ├── budget.md
│   │   └── categories.yaml
│   ├── letters/                     # личная переписка
│   ├── wiki/                        # личная вики, life principles
│   └── README.md
│
├── jetix/                           # [JETIX-PRIVATE] Company OS
│   ├── L0-executive/                # Ruslan + AI agents + future team
│   │   ├── vision.md
│   │   ├── okr/
│   │   ├── energy-constraints/      # aggregated only, no personal data
│   │   └── ai-agents/              # agent configs, CLAUDE.md
│   ├── L1-foundation/              # git, CI/CD, docs-as-code
│   │   ├── CLAUDE.md               # Jetix scope definition
│   │   ├── backup-test-log.md
│   │   └── runbooks/
│   ├── L2-cognitive/               # Левенчук ШСМ applied to Jetix
│   │   ├── roles/
│   │   ├── alphas/
│   │   ├── practices/
│   │   └── learning/               # learning for Jetix (не personal)
│   ├── L3-product/                 # product definitions, roadmap
│   │   ├── ideas/
│   │   ├── specs/
│   │   └── research/
│   ├── L4-delivery/                # sprint work, tasks, client delivery
│   │   ├── sprints/
│   │   ├── clients/                # GDPR: client data here
│   │   └── weekly-reviews/
│   ├── L5-membrane/                # external relationships, contracts
│   │   ├── contacts/               # business contacts only
│   │   ├── contracts/
│   │   └── partnerships/
│   ├── L6-topology/                # org structure, team design
│   │   └── future-hires.md
│   ├── L7-portfolio/              # metrics, P&L, business performance
│   │   ├── financials/
│   │   ├── capacity-input.json     # aggregated from life-os (no personal)
│   │   └── dashboards/
│   └── README.md
│
├── shared/                         # [PUBLIC-SHARED] Method-only
│   ├── role-framework/             # Левенчук roles без контента
│   ├── levenchuk-ontology/         # ШСМ concepts reference
│   ├── writing-templates/          # форматы без контента
│   └── README.md
│
├── .claude/                        # Global Claude config (scope: shared only)
│   └── CLAUDE.md                  # "Read README of each subdirectory for scope"
├── .sops.yaml                      # Раздельные age keys per path
├── .gitignore                      # Exclude: *.log, .env.local, health/raw/
└── README.md                       # "This monorepo contains Life-OS + Jetix"
```

### 2. Concrete Decisions Table

| Компонент | Расположение | Обоснование | Команда видит? |
|---|---|---|---|
| Левенчук роли | `shared/role-framework/` | Метод без данных | ✅ |
| Writing templates | `shared/writing-templates/` | Формат без контента | ✅ |
| CLAUDE.md (Jetix scope) | `jetix/CLAUDE.md` | Jetix context definition | ✅ |
| CLAUDE.md (Life scope) | `life-os/CLAUDE.md` | Life context — never Jetix | ❌ |
| Health metrics | `life-os/health/` | GDPR Special Cat. | ❌ Never |
| Jetix OKR | `jetix/L0-executive/okr/` | Confidential biz data | Team Level |
| Client data | `jetix/L4-delivery/clients/` | GDPR — controller data | Team w/need |
| Personal journal | `life-os/reflection/` | Raw personal | ❌ Never |
| Business contacts | `jetix/L5-membrane/contacts/` | Business context | Team |
| Personal contacts | `life-os/relationships/` | Personal context | ❌ Never |
| Learning (Jetix) | `jetix/L2-cognitive/learning/` | Professional dev | ✅ |
| Learning (personal) | `life-os/learning/` | Personal growth | ❌ |
| Ideas inbox | `life-os/learning/ideas-inbox/` | Private ideation | ❌ |
| Capacity input | `jetix/L7-portfolio/capacity-input.json` | Aggregated number only | Team |
| Personal finance | `life-os/finance/` | Personal | ❌ Never |
| Business P&L | `jetix/L7-portfolio/financials/` | Business | Team (limited) |

### 3. Cross-Reference Patterns (markdown examples)

**Разрешённое (Life-OS → Jetix):**
```markdown
<!-- life-os/reflection/weekly-2026-W04.md -->
## Jetix Status этой недели
Детали: [[jetix/L7-portfolio/weekly-review-2026-W04]]
Energy: 7/10 → Jetix capacity: 84%
Decision: снизить L4 velocity на 15% следующие 2 недели.
```

**Запрещённое (Jetix → Life-OS) — никогда не делай:**
```markdown
<!-- ❌ ЗАПРЕЩЕНО: jetix/L0-executive/context.md -->
<!-- Ruslan has health issue, see [[life-os/health/...]] -->
```

**Правильная агрегация (Life-OS → Jetix/L7):**
```bash
# Скрипт запускается Ruslan вручную (не автоматически)
# ~/jetix-os/jetix/L7-portfolio/update-capacity.sh
echo '{
  "updated": "'$(date -I)'",
  "energy_score": 7,
  "capacity_pct": 84,
  "constraints": "mild fatigue, no blockers"
}' > ~/jetix-os/jetix/L7-portfolio/capacity-input.json
# НЕТ ссылок на life-os/ файлы, нет raw данных
```

### 4. Time Accounting Setup (concrete)

**Toggl structure (сегодня):**
```
1. Создай два Projects: "Jetix" и "Life-OS"
2. Tags для Jetix: L0, L1, L2, L3, L4, L5, L6, L7, admin
3. Tags для Life-OS: health, learning, reflection, relationships, finance
4. Установи Toggl browser extension + mobile app
5. Правило: НИКОГДА не начинай работу без активного Toggl таймера
```

**Daily review (3-line) — шаблон:**
```markdown
## {{date}} — Daily Time Log
**Украло:** [дистракция/переключение] {{X}} мин
**Вложил:** [главный accomplishment] {{description}}
**Баланс:** Jetix {{X}}h | Life-OS {{Y}}h | Energy: {{1-10}}/10
```

**Weekly audit checklist:**
```markdown
## Week {{N}} — Time Audit
- [ ] Toggl report: Jetix total hours = ?
- [ ] Jetix deep work (L2+L3+L4) ≥ 60% from Jetix hours?
- [ ] Life-OS Health block ≥ 7h week?
- [ ] Admin ≤ 15% of total?
- [ ] Главный distraction identified? → block/eliminate
- [ ] ActivityWatch cross-check: manual vs auto matches?
- [ ] Capacity input updated in jetix/L7-portfolio/capacity-input.json
```

### 5. Money Separation Roadmap

**Сейчас (Phase 1):**
1. В DKB/N26: завести отдельные labeled savings pockets или использовать YNAB категории:
   - Jetix Expenses (инфраструктура, инструменты, обучение для бизнеса)
   - Life Expenses (жильё, еда, здоровье, личное)
2. Все Jetix-расходы фиксировать немедленно с тегом

**UG vs GmbH vs OÜ — финальное решение:**

| Критерий | Рекомендация |
|---|---|
| Первый клиент (контракт < €10k) | Freiberufler (если применимо) или UG |
| Первый enterprise клиент (> €10k) | UG (зарегистрировать немедленно при sign) |
| Venture / angel funding | Конверсия UG → GmbH |
| Найм сотрудника в Германии | GmbH (preference для employer status) |
| Все клиенты немецкие | UG/GmbH — никогда OÜ пока в Берлине |

**Steuerberater engagement timing:**
- Trigger: Gewerbeanmeldung → нанять Steuerberater в течение 1 месяца
- Бюджет: €150–300/месяц (DATEV система)
- Задачи: Umsatzsteuervoranmeldung (ежеквартально), Körperschaftssteuererklärung (ежегодно)
- Рекомендация: Berlin-based, знакомый с tech startups (NB: Frankfurt-Schule vs Berliner подходы)

### 6. Phase 2 Access Control: First Hire Checklist

```markdown
## First Jetix Hire — Security Onboarding Checklist

### До их первого дня:
- [ ] life-os/ извлечён в отдельный private repo (git filter-repo)
- [ ] jetix-os монорепо теперь содержит ТОЛЬКО jetix/ + shared/
- [ ] CODEOWNERS обновлён: /jetix/ @jetix-team
- [ ] UG зарегистрирован, ruslan@jetix.de email работает
- [ ] GitHub Org "Jetix" создана (или просто repo with Teams)
- [ ] Отдельный Toggl workspace "Jetix" создан

### В первый день:
- [ ] Invite в GitHub Team (только jetix repo, не life-os)
- [ ] Выдать ruslan@jetix.de или @jetix.de email
- [ ] SOPS: создать age key для нового сотрудника
- [ ] Добавить их public key в .sops.yaml для jetix/ paths only
- [ ] Onboarding doc: jetix/L1-foundation/onboarding.md

### Что они видят:
✅ jetix/ (полностью)
✅ shared/ (полностью)
❌ life-os/ (не существует в их clone)
❌ Личные финансы, здоровье, отношения Ruslan
❌ Personal Claude sessions / Personal API keys

### Security check 30 дней после:
- [ ] git log | grep life-os → пустой результат в их clone
- [ ] Нет secrets из life-os в jetix envs
- [ ] ActivityWatch на личном ноутбуке отделён от рабочего
```

### 7. Migration Triggers (concrete numerical)

| Триггер | Число | Действие | Timeframe |
|---|---|---|---|
| Первый найм (human) | 1 человек | life-os → отдельный private repo; UG регистрация | До их Day 1 |
| 5 сотрудников | 5 человек | Отдельный Hetzner сервер для Jetix; GitHub Org | Перед 5-м наймом |
| GDPR DPA клиент | 1 enterprise DPA | Юридическое лицо (GmbH если нет UG) | До подписания DPA |
| ARR €100k | €100k годовой | UG → GmbH конверсия + Google Workspace | Этот квартал |
| 20 сотрудников | 20 человек | Максимальное разделение: Jetix org, Vault, enterprise infra | Перед 20-м наймом |
| 2030 exit / funding | Series A | Full legal и инфраструктурный separation | Due diligence prep |

### 8. Backup Strategy per Phase

| Фаза | Jetix backup | Life-OS backup | Trigger |
|---|---|---|---|
| **Phase 1** | restic → Hetzner Box + B2 EU (общий repo, тег `jetix`) | restic → Hetzner Box + B2 EU (тег `life-os`) | Сейчас |
| **Phase 2** | restic отдельный repo → B2 bucket `jetix-backup` | restic отдельный repo → B2 bucket `personal-backup` | При найме |
| **Phase 3** | AWS Backup eu-central-1 + Hetzner Storage Box | Hetzner Storage Box + B2 EU | При 5+ сотрудниках |
| **Restore test** | Квартальный (Calendar: каждые 3 мес) | Квартальный | Всегда |
| **Encryption** | age-jetix.key (отдельный) | age-life.key (отдельный) | Phase 1 уже |

### 9. Anti-patterns (критический список)

```
❌ Единый decisions/ folder в корне репо
   → Смешивает personal life decisions с business decisions
   → Исправление: life-os/reflection/decisions/ + jetix/L0-executive/decisions/

❌ Jetix агент читает life-os/
   → Privacy breach даже в Phase 1 — привычка формируется сейчас
   → Исправление: CLAUDE.md с явным scope запретом

❌ Shared secrets file (.env в корне репо)
   → Одна утечка = все контексты скомпрометированы
   → Исправление: SOPS с path-specific keys

❌ Unified daily-log (один файл для Jetix + личного)
   → Невозможно разделить при найме, создаёт privacy risk
   → Исправление: отдельные daily logs в каждой OS

❌ Один GitHub Team с доступом к обоим repos
   → Phase 2: будущие сотрудники не должны видеть life-os
   → Исправление: CODEOWNERS от начала, separate repos при найме

❌ Одна Claude Code сессия в ~/jetix-os/ (корень)
   → Агент видит всё дерево, включая life-os/
   → Исправление: всегда запускать из ~/jetix-os/jetix/ или ~/life-os/

❌ Estonian OÜ при проживании в Берлине
   → Betriebsstätte риск = двойное налогообложение
   → Исправление: UG haftungsbeschränkt

❌ Откладывать Toggl setup "до первого клиента"
   → Потеря данных о времени, нет baseline для P&L
   → Исправление: настроить сегодня

❌ Смешивать Jetix и Life-OS метрики на одном графике
   → Невозможно аудировать, нарушает GDPR-логику
   → Исправление: два отдельных Grafana datasource

❌ Один restic repo без тегирования контекста
   → При компрометации нет возможности изолировать restore
   → Исправление: раздельные repos уже в Phase 1 (разные пароли)
```

### 10. 10-year vision table (2026 → 2036)

| Год | Jetix | Life-OS | Разделение | Команда |
|---|---|---|---|---|
| **2026** | Monorepo, solo, 12 AI агентов | Nested в jetix-os/ | Папки + SOPS | Ruslan only |
| **2027** | Separate repo, первый найм, UG | Отдельный private repo | git filter-repo | 1–3 человека |
| **2028** | GmbH (конверсия UG), два сервера | Полностью изолирован | Separate infra | 5–10 человек |
| **2029** | GitHub Org "Jetix", Vault secrets | ~/ home VPS или NAS | Enterprise ACL | 10–20 человек |
| **2030** | Series A / €1M ARR | Полностью отдельный stack | SOC2-prep | 20–50 человек |
| **2031** | Mehrere Portfolio companies | Life-OS = personal HQ | Чёткий firewall | 50+ человек |
| **2032** | International expansion | Life-OS интегрирован с family? | Legal structures | 100+ человек |
| **2033–2036** | IPO-track / Mega-corp | Life-OS = founder legacy | Total separation | 500–1000+ |

**Invariant через все годы:** asymmetric reference rule (Life-OS → Jetix ✅, Jetix → Life-OS ❌) никогда не меняется. GDPR compliance улучшается поэтапно.

### 11. This-Week Action Items

```markdown
## На этой неделе (Ruslan, Berlin, 2026)

1. **[Monday] Настроить SOPS с двумя age-ключами**
   age-keygen -o ~/.config/sops/age-life.key
   age-keygen -o ~/.config/sops/age-jetix.key
   Обновить ~/jetix-os/.sops.yaml по шаблону из Part G.
   Re-encrypt все существующие секреты.

2. **[Monday-Tuesday] Реструктурировать репо по Part J схеме**
   mkdir -p ~/jetix-os/{life-os,jetix,shared}/{<все подпапки>}
   git mv (существующие файлы в новые места)
   Обновить CLAUDE.md в каждой директории.

3. **[Wednesday] Настроить Toggl**
   - Создать Projects: "Jetix" + "Life-OS"
   - Создать Tags по схеме из Part F
   - Установить mobile app + browser extension
   - Ретроактивно залогировать эту неделю (примерно)

4. **[Wednesday] Git identity separation**
   Зарегистрировать/купить домен jetix.de (Hetzner или INWX, €10–15)
   Настроить ~/.gitconfig с includeIf для ~/jetix-os/jetix/
   Сгенерировать два SSH ключа по схеме из Part I.

5. **[Thursday] Backup setup**
   Убедиться что restic backup включает ~/jetix-os/ полностью
   Добавить теги jetix/ и life-os/ в backup policy
   Запустить test restore одного файла.

6. **[Friday] Зафиксировать Phase 2 triggers в calendar**
   "IF: 1 hire → BEFORE their Day 1: git filter-repo + UG registration"
   Добавить в jetix/L0-executive/decisions/phase2-triggers.md
   Добавить quarterly backup test в calendar.

7. **[Friday] GDPR baseline**
   Скачать и подписать DPA с GitHub и Hetzner
   Создать jetix/L5-membrane/gdpr/tom-phase1.md с текущими мерами
   (Шаблон TOMs из Part G).
```

---

## Дополнение: ASCII топология по фазам

### Phase 1 (сейчас)

```
┌─────────────────────────────────────────────┐
│              Hetzner CPX32 Nuremberg         │
│                                             │
│  ~/jetix-os/ (git monorepo)                 │
│  ├── life-os/  [SOPS: age-life.key]         │
│  ├── jetix/    [SOPS: age-jetix.key]        │
│  └── shared/   [both keys]                  │
│                                             │
│  Claude Code: scoped per subdirectory       │
│  Coolify: Jetix services only               │
│  restic → Hetzner Box + B2 EU               │
└─────────────────────────────────────────────┘
          │
          └── GitHub: Bogersebekov/jetix-os (private)
              CODEOWNERS: Ruslan only
```

### Phase 2 (first hire)

```
┌─────────────────────────────┐    ┌───────────────────────────┐
│     Hetzner CPX32 (Jetix)   │    │   Hetzner CX21 (Personal) │
│                             │    │                           │
│  ~/jetix/ (git repo)        │    │  ~/life-os/ (git repo)    │
│  SOPS: age-jetix.key        │    │  SOPS: age-life.key       │
│  Claude: jetix scope        │    │  Claude: life scope       │
│  User: jetix-svc            │    │  User: ruslan             │
│                             │    │                           │
│  restic → B2 jetix-bucket   │    │  restic → B2 life-bucket  │
└─────────────────────────────┘    └───────────────────────────┘
          │                                   │
          └── GitHub Org: Jetix               └── GitHub: ruslan/life-os-private
              Team: jetix-team                    Access: Ruslan ONLY
              (Hire sees this)                    (Hire CANNOT access)
```

### Phase 3 (mega-corp track)

```
┌──────────────────────────────┐    ┌─────────────────────────────┐
│     Jetix Infra (Enterprise) │    │   Life-OS Infra (Personal)  │
│                              │    │                             │
│  AWS eu-central-1 / Hetzner  │    │  Home server / VPS          │
│  Jetix GmbH entity           │    │  Personal accounts only     │
│  GitHub Enterprise Org       │    │  No corporate access        │
│  HashiCorp Vault             │    │  age-life.key (offline)     │
│  SOC2 compliant              │    │  Separate restic repo       │
│  DPA with all processors     │    │                             │
│  50+ employees               │    │  Ruslan ↔ Life-OS only      │
│                              │    │                             │
│  Claude for Work (Jetix Org) │    │  Claude Personal (separate) │
└──────────────────────────────┘    └─────────────────────────────┘

              Asymmetric reference: Life-OS reads Jetix public outputs
                                    Jetix NEVER reads Life-OS
```

---

## Источники

1. [Tiago Forte, "Building a Second Brain"](https://fortelabs.com/blog/basboverview/) — PARA method overview, Forte Labs
2. [August Bradley, PPV — Notion Life OS](https://esilva.net/tla_insights/ppv_bradley) — Pillars, Pipelines & Vaults framework
3. [Thomas Frank, "Ultimate Brain"](https://thomasjfrank.com/brain/) — Notion second brain template
4. [Obsidian Forum — One vault vs multiple vaults](https://forum.obsidian.md/t/one-vault-vs-multiple-vaults/1445) — Community patterns
5. [Cal Newport, time blocking method](https://www.neuyear.net/blogs/productivity/cal-newports-deep-work-time-blocking-method) — Deep Work shutdown ritual
6. [Paul Graham, "Maker's Schedule, Manager's Schedule"](https://paulgraham.com/makersschedule.html) — Founder time management
7. [Naval Ravikant Almanack summary](https://grahammann.net/book-notes/almanack-of-naval-ravikant-eric-jorgenson) — Leverage and founder life frameworks
8. [Clark, S.C. (2000), "Work/Family Border Theory"](https://journals.sagepub.com/doi/10.1177/0018726700536001) — Human Relations, vol. 53, no. 6
9. [Kossek & Lautsch — Work-family boundary management styles](https://www.ellenkossek.com/s/Work-familyboundarymanagementstylesinorganizationsAcross-levelmod.pdf) — Separators, Integrators, Volleyers
10. [Git sparse-checkout documentation](https://git-scm.com/docs/sparse-checkout) — Official git docs
11. [git filter-repo — migrating subfolder with history](https://jboylantoomey.com/post/migrating-subfolder-while-preserving-git-history) — Technical guide
12. [Nx vs Turborepo monorepo strategy 2025](https://www.youngju.dev/blog/culture/2026-03-24-monorepo-strategy-nx-turborepo-guide-2025.en) — CODEOWNERS and visibility
13. [SOPS multiple age recipients](https://github.com/getsops/sops/discussions/1579) — getsops GitHub
14. [GmbH vs UG comparison](https://www.betahaus.com/magazine/gmbh-vs-ug-in-germany-which-business-structure-is-right-for-your-startup-in-2026) — Betahaus, 2026
15. [Estonian OÜ vs German GmbH — PE risk](https://www.reddit.com/r/eResidency/comments/1ne58mz/) — Reddit r/eResidency, legal analysis
16. [GDPR Art. 32 TOM requirements](https://riscreen.de/en/art-32-gdpr-technical-and-organizational-measures-toms/) — Riscreen legal analysis
17. [Git conditional includes (includeIf)](https://jdsalaro.com/tutorial/git-configuration-folder-dependent-conditional-includes/) — Technical tutorial
18. [ActivityWatch open-source time tracker](https://activitywatch.net) — Official site
19. [Partial clone + sparse-checkout guide](https://www.mslinn.com/git/600-partial-clone.html) — Mike Slinn
20. [heydata.eu — TOM under GDPR](https://heydata.eu/en/magazine/technical-and-organizational-measures/) — Comprehensive TOM guide
