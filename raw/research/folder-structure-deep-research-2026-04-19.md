# Jetix OS: Стресс-тест структуры папок и архитектурный разбор

> **Контекст:** Solo-founder + 12-30+ AI-агентов (Claude Code), монорепо на GitHub, сервер Hetzner, Берлин. Язык: русский. Дата: апрель 2026.
>
> **Задача этого документа:** не повторить R2-черновик, а атаковать его — найти слабые места, предложить альтернативы с доказательной базой, дать конкретные решения D1–D10.

---

## Часть A. Монорепо vs. Мультирепо: академика + индустрия

### Что говорит Google

Исследование Potvin и Levenberg ([Potvin & Levenberg, ACM CACM 2016](https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/)) — самый цитируемый аргумент в пользу монорепо. Ключевые числа: **2 млрд строк кода**, **86 ТБ данных**, **25 000+ разработчиков**, **35 млн коммитов за 18 лет**. Практически всё Google хранит в единой Piper-репозитории. Бенефиты очевидны — атомарные изменения через границы проектов, единый source of truth, отсутствие «diamond dependency» проблемы.

Но критически важны **условия**: Piper — это кастомная распределённая система поверх Perforce, работающая на 10 дата-центрах с алгоритмом Paxos. У Ruslan нет Piper. **Вывод для Jetix:** монорепо оправдан не потому что Google, а потому что у Ruslan есть главная причина Google: единый source of truth для AI-агентов, которые работают с кодом, промптами, бизнес-документами и клиентскими данными одновременно.

Дополнительный аргумент из [CircleCI blog](https://circleci.com/blog/monorepo-dev-practices/): монорепо принципиально лучше для AI coding assistants (Claude Code, Copilot) — агент видит весь контекст сразу, а не отдельный срез. Это прямой аргумент для Jetix с 12-30+ агентами.

### Meta/Facebook: EdenFS + Sapling

Meta пошла по пути масштабирования монорепо вместо разбиения, разработав [Sapling — Git-совместимый клиент](https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/) с виртуальной файловой системой, sparse checkout и segmented changelog. Репозиторий Meta: **десятки миллионов файлов и коммитов**. Ключевой урок: *«разбиение монорепо невозможно — теряются основные преимущества»* (упрощённый dependency management, атомарные изменения).

**Для Jetix:** sparse checkout — это паттерн для будущего (когда у агента есть 50+ ролей и нужно загружать только нужный контекст). Сегодня это избыточно, но нужно проектировать директории так, чтобы будущий sparse profile работал.

### Microsoft: VFS for Git / Scalar

Microsoft перевёл репозиторий Windows (гигантский) на [VFS for Git / Scalar](https://devblogs.microsoft.com/devops/introducing-scalar/): виртуальная файловая система, фоновый maintenance, sparse checkout с tiered indexing. Ключевое: **физически скачивается только то, что нужно**, но логически есть «весь репозиторий».

**Для Jetix:** при росте до 100+ агентов и тысячах файлов стоит использовать `git sparse-checkout` для агент-специфических рабочих пространств. Scalar настраивается через `scalar clone`.

### Monorepo antipatterns — когда монорепо ломается

По данным [Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/monorepo-vs-multirepo) и [Gigamonkeys](https://gigamonkeys.com/mono-vs-multi/):

1. **Тайно связанные команды** — если разные части репо требуют разных deployment-пайплайнов и доступов, монорепо создаёт больше coordination overhead, чем даёт пользы.
2. **Blast radius на CI** — любой коммит в любую часть может сломать весь пайплайн.
3. **Поиск полиспован** — `grep` по 10+ ГБ репозитория требует ripgrep + специальных инструментов.
4. **Гигантские PR** — без инструментов типа Rosie глобальные рефакторинги становятся кошмаром.

**Для Jetix:** антипаттерн №1 нерелевантен (один owner — Ruslan), №3 критичен уже сейчас (557 страниц wiki → нужен ripgrep + fzf workflow), №4 решается через автоматику агентов.

### Hybrid: docs+data+prompts+code — специфика Jetix

Большинство monorepo tooling (Bazel, Buck2, Pants, Nx, Turborepo, Moon) **оптимизировано под код**. Jetix — гибрид: код (Python pipelines, scripts), данные (alphas JSONL, clients), документы (wiki, decisions, letters), промпты (AI system prompts с версиями), конфиги (YAML/TOML). Это делает стандартные build tools частично применимыми:

| Инструмент | Применимость к Jetix | Что использовать |
|---|---|---|
| Bazel / Buck2 | Низкая — code-first, сложная настройка | Нет |
| Nx | Средняя — умеет tasks graph, поддерживает non-code | Только если появится много Python микросервисов |
| Turborepo | Средняя — хорош для JS/TS | Нет |
| Moon | Средняя — более гибкий, поддерживает Python | Возможно при 10+ Python pipelines |
| **just / justfile** | Высокая — простой task runner, нет ограничений | **Рекомендовано сейчас** |
| GitHub Actions | Высокая — CI/CD для любых типов файлов | **Рекомендовано** |

**Вывод Part A:** монорепо правильный выбор для Jetix. Единый контекст для AI-агентов — это killer argument. Стандартные monorepo build tools не подходят под docs+data hybrid; `just` + GitHub Actions — правильная пара инструментов сейчас.

---

## Часть B. Индустриальные референсы

### GitLab Handbook: 2000+ страниц в одном репо

[GitLab Handbook](https://handbook.gitlab.com/handbook/) — открытый, 2000+ страниц текста, организован **по функциям, не по командам**. Ключевой принцип: **DRI (Directly Responsible Individual)** — каждый раздел или документ имеет одного явного владельца. Изменения через merge requests, вопросы через issues. Структура — плоская по функциям: Company → People Group → Product → Engineering → Security → Marketing → Sales → Finance → Legal.

**Применимо к Jetix:**
- Принцип «функция, не команда» → роли в `roles/` организованы по функции (sales-lead, delivery, analyst), не по проекту.
- DRI-паттерн → каждый файл в `wiki/` должен иметь поле `owner:` в YAML frontmatter.
- Merge request как ворота изменений → применимо для критических документов (roles manifests, prompts).

**Критика GitLab-структуры для Jetix:** GitLab организует handbook по «глобальным функциям» потому что у них 2000+ сотрудников. У Ruslan — 1 человек + AI. Копировать GitLab-структуру напрямую — антипаттерн. Нужен более гранулярный, операционный слой.

### Oxide Computer: RFD Process

[Oxide RFD 1](https://rfd.shared.oxide.computer/rfd/0001) — Request for Discussion, вдохновлён IETF RFC, Rust RFC, Kubernetes proposals. Структура:

```
rfd/
  0001/README.adoc
  0042/README.adoc
prototypes/prototype.adoc
scripts/new.sh
```

Каждый RFD: 4-значный номер с нулями (0001), отдельная ветка, состояния: `prediscussion → ideation → discussion → published → committed → abandoned`. Ветка называется так же, как номер RFD.

**Применимо к Jetix:**
- `decisions/` → полностью перенять Oxide RFD-нумерацию (0001–9999).
- Состояния RFD применить к Jetix decisions.
- Короткие URL через алиасы: `12.rfd.jetix.internal`.

**Критика для Jetix:** Oxide использует AsciiDoc — избыточно для solo-founder. Markdown достаточно.

### PARA-метод (Tiago Forte)

[PARA](https://fortelabs.com/blog/para/) — Projects, Areas, Resources, Archives. Ключевое разграничение:
- **Projects** — конечная цель, определённый дедлайн.
- **Areas** — бесконечные зоны ответственности (health, finances).
- **Resources** — темы интереса без привязки к проекту.
- **Archives** — всё неактивное.

**Применимо к Jetix:** PARA — хороший фреймворк для `life-os/`, где нет строгой business-иерархии. Для бизнес-части Jetix PARA недостаточно структурирован — нет места для roles, alphas, prompts.

**Ограничение PARA:** разработан для личной PKM-системы одного человека. Не масштабируется на командную работу без дополнительного слоя (DRI, governance).

### Zettelkasten / Luhmann

Никлас Луман создал 90 000 заметок за 40 лет, используя плоскую нумерацию с ветвлением: `22 → 22a → 22a1 → 22a1b`. Система выжила при такой шкале благодаря **связям, не иерархии** ([zettelkasten.de](https://zettelkasten.de/introduction/)). Каждая заметка атомарна (одна идея), связана с другими через явные ссылки.

**Применимо к Jetix wiki:** 557 страниц — это уже Zettelkasten-шкала. Ключевые уроки:
1. Не пытаться создать идеальную таксономию заранее — она убьёт рост.
2. Связи важнее иерархии — использовать `[[wikilinks]]` в Obsidian.
3. Atomic notes — каждая wiki-страница = одна концепция.

### Johnny.Decimal

[Johnny.Decimal](https://johnnydecimal.com/) — 10 areas × 10 categories × 100 IDs = максимум 1000 папок. Номера: `12.34` (area 10-19, category 12, item 34). Ключевое свойство: **числа не перемещаются**, строится muscle memory.

**Применимо к Jetix:** Johnny.Decimal — отличная система для `life-os/` (личные файлы ограничены). Для бизнес-части **не подходит** — 1000 клиентов, 500 проектов взрывают Johnny.Decimal уже на второй год.

### Diátaxis (документационный фреймворк)

[Diátaxis](https://diataxis.fr/) — 4 типа документации: tutorials (learning-oriented), how-to guides (problem-oriented), reference (information-oriented), explanation (understanding-oriented). Структура возникает органически, не навязывается сверху.

**Применимо к `docs/`:** папка `docs/` в Jetix организована по Diátaxis:
```
docs/
  tutorials/
  how-to/
  reference/
  explanation/
```

### Holacracy: роли отдельно от людей

[Holacracy Constitution 5.0](https://www.holacracy.org/constitution/5-0/) определяет роль как: **Purpose + Domains + Accountabilities**. Роль заполняется человеком или агентом, но определяется независимо. Когда роль не заполнена — Circle Lead автоматически берёт её функции.

**Прямой аналог для Jetix:** `roles/<name>/manifest.md` — это Holacracy-определение роли. Executor (агент или человек) — это временный носитель роли. Это концептуально верно и должно быть сохранено в R3.

---

## Часть C. Нейминг-конвенции: глубокий разбор

### kebab-case vs. snake_case vs. PascalCase vs. camelCase

| Конвенция | Где применять | Обоснование |
|---|---|---|
| `kebab-case` | Все папки и файлы в файловой системе | URL-безопасен, читаем, case-insensitive OS-совместим, стандарт для web |
| `snake_case` | Python файлы (обязательно по PEP8), JSONL ключи | Языковой стандарт Python |
| `PascalCase` | Никогда в FS; только классы Python | Создаёт проблемы на case-insensitive macOS |
| `camelCase` | Никогда в FS; только JS/TS код | Та же проблема |

**Универсальное правило для Jetix:** `kebab-case` для всего в файловой системе. Без исключений. Python-файлы используют `snake_case` внутри (переменные, функции), но сами файлы и папки — `kebab-case`.

### Дата-префиксы: когда нужны, когда вредны

Формат `YYYY-MM-DD-slug.md` — классика для:
- Дневники (`daily-log/2025-04-15.md`) — **обязательно**, иначе 1000 файлов не сортируются.
- Postmortems — **рекомендовано** (постмортем привязан к инциденту в дату).
- Letters — **рекомендовано**.
- Решения (decisions) — **НЕТ**: Oxide использует последовательный номер, не дату. Дата создания = метаданные внутри файла.
- Wiki-страницы — **НЕТ**: дата в имени wiki-страницы создаёт ложное ощущение устаревания.
- Roles, prompts — **НЕТ**: версия решает задачу лучше даты.

### Иерархическая нумерация

| Схема | Пример | Применение | Предел |
|---|---|---|---|
| RFD-style | `0001-decision-title.md` | decisions/ | 9999 решений |
| Luhmann | `21/3d7a7` | Исторический, не для FS | Практически бесконечно |
| Johnny.Decimal | `12.34` | Личные файлы, life-os | 1000 items max |
| Sequential ISO | `2025-04-15.md` | daily-log | Бесконечно (год/папка) |

**Для Jetix:** decisions/ → `0001-` префикс (4 знака), flat. Zettelkasten-нумерация избыточна.

### Версионирование промптов в именах файлов

Сравнение подходов:

| Паттерн | Пример | Плюсы | Минусы |
|---|---|---|---|
| SemVer в папке | `prompts/analyst/v1.2.3/system.md` | Чёткая неизменность, параллельные версии | 100+ версий × 30+ агентов = 3000+ папок |
| SemVer в имени | `analyst-v1.2.3.md` | Плоско, быстро находить | Сортировка ломается на v1.10 < v1.9 |
| Git-тег | `analyst/system.md` + git tag `analyst-v1.2.3` | Нет folder explosion, история в git | Нельзя иметь две версии одновременно в working tree |
| Symlink current | `analyst/current → analyst/v1.2.3/` | Удобная ссылка на текущую | Symlinks в git — проблемы на Windows |

Рекомендуемый гибрид (R3): папки только для **major** версий, git tag для minor/patch:

```
prompts/
  analyst/
    v1/
      system.md      # major API, неизменен после тега
      README.md      # changelog
    v2/
      system.md
```

Git tags: `prompt-analyst-v1.2.3`. Это решает folder explosion и сохраняет возможность parallel versions для A/B тестирования.

### Reserved names

```
README.md      # обязательно в каждой папке-зоне
_meta.yaml     # YAML frontmatter для автоматики
_index.md      # Obsidian-совместимый индекс зоны
.gitkeep       # placeholder для пустой папки в git
justfile       # task runner
```

`.hidden` файлы — для tooling (`.claude/`, `.github/`), не для контента.

---

## Часть D. Паттерны масштабирования: Solo → 500

### Фазы роста и триггеры рефакторинга

| Фаза | Executors | Проектов | Клиентов | Ключевые папки | Триггеры для следующей фазы |
|---|---|---|---|---|---|
| **Solo-0** (сейчас) | 1 + 5-8 агентов | 5-15 | 20-50 | Все в одном монорепо, flat | >100 файлов в одной папке, search > 30 сек |
| **Solo-1** | 1 + 12-15 агентов | 15-40 | 50-200 | Alphas с sub-типами, decisions растут | >500 clients flat, >50 decisions, CI > 5 мин |
| **Small Team** | 1 человек + 2-3 фрилансера + 20+ агентов | 40-100 | 200-500 | Отдельные индексы по типам клиентов, sharding clients/ | >1000 clients, life-os начинает конфликтовать |
| **Scale-up** | 5-10 людей + 30+ агентов | 100-300 | 500-2000 | Submodule для life-os, sharding по году/типу, отдельные сервисы | Права доступа, GDPR compliance, multi-team CI |
| **Mega-corp** | 50+ людей + 100+ агентов | 300+ | 2000+ | Отдельные репо по доменам, federation | Piper-like tooling, dedicated VFS |

### Sharding при >500 клиентов

Flat `clients/acme-corp/` хорошо до ~500 директорий. После — cognitive overhead и медленный `ls`. Варианты sharding:

**Option A: Алфавитный shard** — `clients/a-f/acme-corp/` — работает, но неинтуитивно.

**Option B: Год первого контакта** — `clients/2024/acme-corp/` — хорошо для архивации, плохо для поиска активных.

**Option C: Тип + алфавит** — `clients/enterprise/acme-corp/` vs `clients/smb/local-coffee/` — **рекомендовано** для Jetix: Business logic sharding.

**Option D: Hash prefix** — первые 2 символа UUID — масштабируется до бесконечности, нечитаемо.

**Рекомендация для Jetix:** до 500 клиентов — flat. После — Option C (тип клиента). Это соответствует бизнес-логике: enterprise-клиенты требуют другого workflow.

---

## Часть E. Депрекация и архивация

### Стратегии архивации

| Паттерн | Структура | Плюсы | Минусы |
|---|---|---|---|
| `_archive/` внутри родителя | `clients/_archive/old-client/` | Близко к оригиналу, легко найти | Засоряет корневой listing |
| Top-level `archive/` | `archive/clients/old-client/` | Чисто разделено | Далеко от контекста |
| Archive branch | `git branch archive/2024` | Не занимает место в working tree | Нельзя искать без checkout |
| По году | `archive/2024/old-client/` | Понятно по времени закрытия | Дублирует структуру внутри |
| По статусу | `archive/closed/old-client/` | Понятная причина | Статус меняется редко |

**Рекомендация для Jetix (R3):** `_archive/` внутри каждой зоны, сортировка по году закрытия:

```
clients/
  acme-corp/
  local-coffee/
  _archive/
    2024/
      old-client/
    2025/
      another-closed/
```

Это сохраняет контекст (архив клиентов рядом с активными клиентами), легко исключить из поиска через `.gitignore`-patterns или ripgrep exclude.

### Soft delete vs. hard delete vs. BFG purge

- **Soft delete** (`mv client/ _archive/2024/client/`) — стандарт для бизнес-данных. Сохраняет историю.
- **Hard delete** (`git rm -r`) — только для временных файлов, никогда для бизнес-контента.
- **BFG Repo Cleaner** — для удаления secrets из истории git. Никогда для бизнес-данных.

### Протокол закрытия роли/проекта

```
1. Обновить статус: status: closed + closed_at: YYYY-MM-DD
2. Создать postmortem (если проект > 1 месяца)
3. Переместить в _archive/YYYY/
4. Обновить _index.md родительской папки
5. Git commit: "archive: close project/client-name (reason)"
6. Создать запись в decisions/ если было значимое решение о закрытии
```

### GDPR + немецкое законодательство (Germany HGB/AO)

По данным [CSP Intelligence](https://www.csp-sw.com/blog/retention-periods) и [European Commission](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr/how-long-can-data-be-kept-and-it-necessary-update-it_en):

| Тип данных | Срок хранения | Основание |
|---|---|---|
| Бухгалтерские документы, инвойсы | **10 лет** | AO §147 / HGB §257 |
| Коммерческие письма, переписка | **6 лет** | HGB §257 |
| Бизнес-email (tax-relevant) | **10 лет** | AO §147 / GoBD |
| Персональные данные (GDPR) | До достижения цели, затем удалить | GDPR Art. 5, 17 |
| Зарплатные документы | **до 30 лет** | §28f SGB IV |

**Критический конфликт:** GDPR требует удалить персональные данные после достижения цели, HGB требует хранить invoices с персональными данными 10 лет. Решение: **purpose-scoped archiving** — персональные данные архивируются с ограниченным доступом и помечаются для удаления после истечения срока.

**Практически для Jetix:**
```
clients/acme-corp/
  invoices/           # 10 лет хранения обязательно
  contracts/          # 10 лет после окончания контракта  
  correspondence/     # 6 лет
  _gdpr-deletion-log.yaml  # когда удалить персональные данные
```

---

## Часть F. Кросс-сквозные concerns

### Документ, релевантный 5 клиентам + 2 проектам + 1 стратегии

Это классическая проблема иерархической файловой системы. Варианты решения:

| Подход | Механизм | Плюсы | Минусы |
|---|---|---|---|
| **Canonical location + references** | Файл в одном месте, ссылки из других | Нет дублирования, чистый source of truth | Нужна дисциплина обслуживания ссылок |
| **Tags в frontmatter** | YAML: `tags: [client-acme, project-x]` | Работает с Obsidian, DuckDB query | Зависит от tooling поиска по тегам |
| **Symlinks** | `ln -s ../../wiki/shared-doc.md clients/acme/` | Нативно для FS | Плохо работает в git на Windows, хрупко |
| **Duplicate** | Копия в каждом месте | Работает без tooling | Ад консистентности |

**Рекомендация для Jetix:** Canonical location + YAML frontmatter tags + ripgrep по тегам.

Схема:
```yaml
# В каждом файле wiki/ или shared-docs/
---
title: Стратегия ценообразования Q3
tags: [strategy, client-acme, client-beta, project-alpha]
owner: ruslan
related: [clients/acme-corp/, projects/alpha/]
---
```

Поиск: `rg "client-acme" --glob "*.md" -l` или через Obsidian graph.

### Templates: top-level vs. per-domain

| Подход | Структура |
|---|---|
| Top-level | `templates/client.md`, `templates/postmortem.md` |
| Per-domain | `clients/templates/`, `postmortems/templates/` |
| Hybrid | Top-level `templates/` + domain-specific overrides |

**Рекомендация:** top-level `templates/` с namespace в именах:

```
templates/
  client-brief.md
  project-charter.md
  postmortem.md
  decision.md
  role-manifest.md
  prompt-system.md
  daily-log.md
  research-note.md
```

Это упрощает поиск шаблонов — одно место, предсказуемо.

### Configs, env, secrets

```
jetix/
  config/           # YAML/TOML конфиги, которые можно коммитить
    agents.yaml     # реестр агентов
    roles.yaml      # реестр ролей  
    settings.toml   # глобальные настройки
  
secrets/            # SOPS-encrypted, не в plain text
  .sops.yaml        # правила шифрования
  api-keys.enc.yaml # зашифрованные ключи

.env.example        # template для .env, коммитится
.env                # в .gitignore, не коммитится
```

---

## Часть G. Life-OS vs. Jetix: 4 варианта и эволюционные триггеры

### Четыре опции

**Option 1: Полностью вложенный** (`jetix-os/life-os/` + `jetix-os/jetix/`)

Преимущества:
- Один `git clone` даёт всё.
- AI-агент видит весь контекст: личные решения Ruslan влияют на бизнес-решения.
- Единый `justfile`, единый CI.

Недостатки:
- **Дублирование схожих структур**: `life-os/wiki/` + `jetix/wiki/`, `life-os/decisions/` + `jetix/decisions/`.
- Приватные личные данные в корне бизнес-репозитория.
- При найме людей придётся давать доступ ко всему монорепо или сложно городить subpath access.

**Option 2: Параллельные папки на корне** (`life-os/` + `jetix/` на одном уровне) — **R2 текущий вариант**

Преимущества:
- Чёткое разграничение без вложенности.
- Проще объяснить структуру.

Недостатки:
- Те же `wiki/`, `decisions/`, `letters/` появляются дважды — нет conceptual merge.
- При росте бизнеса life-os продолжает жить в бизнес-репозитории.

**Option 3: Git submodule** — `life-os` как submodule внутри `jetix-os`

Преимущества:
- Физически отдельный репозиторий с независимой историей.
- Можно дать коллаборатору доступ к `jetix-os` без `life-os`.

Недостатки:
- Git submodules — известный источник боли: нужен `git submodule update --recursive` после каждого clone.
- CI становится сложнее.
- Claude Code и другие AI-агенты часто не понимают submodule контекст.

**Option 4: Полностью отдельные репо**

Преимущества:
- Максимальная изоляция.
- Разные права доступа, разные CI, разные бэкапы.

Недостатки:
- AI-агент теряет контекст между `life-os` и `jetix`.
- Дополнительный когнитивный overhead для Ruslan.
- Cross-references между репо — markdown ссылки ломаются.

### Сравнительная таблица

| Критерий | Option 1 (вложен) | Option 2 (параллельно, R2) | Option 3 (submodule) | Option 4 (отдельные) |
|---|---|---|---|---|
| AI-контекст | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| Приватность | ★☆☆☆☆ | ★★☆☆☆ | ★★★★☆ | ★★★★★ |
| Простота setup | ★★★★★ | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| Масштаб найма | ★☆☆☆☆ | ★★☆☆☆ | ★★★★☆ | ★★★★★ |
| CI сложность | Низкая | Низкая | Средняя | Средняя |
| GDPR разделение | ★★☆☆☆ | ★★☆☆☆ | ★★★★☆ | ★★★★★ |

### Эволюционные триггеры

| Событие | Переход |
|---|---|
| Первый нанятый человек (доступ к репо) | Option 2 → Option 3 |
| 5+ людей с разным уровнем доступа | Option 3 → Option 4 |
| GDPR audit или юридическая экспертиза | Option 2 → Option 3/4 немедленно |
| life-os > 2000 файлов и мешает CI | Option 2 → Option 3 |
| Ruslan хочет поделиться jetix без life-os | Option 2 → Option 3 |

**Рекомендация (D5):** Сейчас — Option 2 (R2 правильный). Переход к Option 3 при первом найме человека или при GDPR audit. Option 4 — только при 5+ людях с разными правами доступа.

---

## Часть H. Зональный анализ Jetix-специфики

### `wiki/` (557 существующих страниц)

**Текущее состояние:** 557 страниц — это уже Zettelkasten-масштаб. Плоская организация работает только при качественных [[wikilinks]] и хорошем поиске.

**Ожидаемый рост:** при активной работе +50-100 страниц в месяц = 2000+ страниц за год. Flat wiki начинает проседать при >1500 страниц без поиска.

**Anti-patterns:**
- Вложенность >3 уровней — ломает Obsidian graph и поиск.
- Дата в имени wiki-страницы — создаёт ложное устаревание.
- Дублирование между `life-os/wiki/` и `jetix/wiki/` — нет единого source of truth для концептов.

**Рекомендация:** единый `wiki/` на уровне monorepo root (или внутри `jetix/`) с тегами для разграничения `#life` vs `#business`. Obsidian-совместимые [[wikilinks]] + frontmatter с `area:` полем.

```
wiki/
  concepts/          # атомарные концепты (Zettelkasten-стиль)
  processes/         # бизнес-процессы
  clients/           # client-specific knowledge (не дублировать с alphas)
  technologies/      # tech wiki
  _templates/        # шаблоны страниц
  _index.md          # master index
```

### `roles/` vs. `executors/` — стресс-тест

Текущий R2 делает разделение на `roles/` (абстрактные определения) и `executors/agents/` (конкретные реализации). Теоретически красиво — Holacracy-инспирировано. Практически?

**Проблема №1:** Каждое изменение роли требует обновления в двух местах. Solo-founder + AI — это реальная friction.

**Проблема №2:** При добавлении нового агента нужно создать файлы в обоих местах. Легко сделать inconsistency.

**Проблема №3:** AI-агент, которому нужно понять свою роль, должен читать файл из `roles/` И файл из `executors/agents/`. Два обращения вместо одного.

**Три альтернативы:**

**Alt 1: Combined manifest** — `roles/<name>/manifest.md` содержит и абстрактное определение, и конкретный executor config:

```
roles/
  analyst/
    manifest.md      # Purpose, Accountabilities, Domains (Holacracy)
    executor.yaml    # model: claude-3-7-sonnet, tools: [...], constraints: [...]
    evals/
      golden.jsonl
```

**Alt 2: Single `agents/<name>/`** — всё в одном:

```
agents/
  analyst/
    system.md        # system prompt (текущая версия)
    manifest.md      # role definition
    evals/
    v1/system.md     # предыдущие версии
```

**Alt 3: Hybrid с registry** — роли как YAML-entries в `config/roles.yaml`, конкретные файлы в `agents/`:

```yaml
# config/roles.yaml
analyst:
  purpose: "Synthesize data into actionable insights"
  accountabilities: [...]
  executor: agents/analyst/
  current_prompt: agents/analyst/v2/system.md
```

**Решение (D1):** **Alt 1** — Combined manifest. Это сохраняет Holacracy-разделение концептуально, но в одной папке. Физическое разделение R2 (`roles/` + `executors/`) создаёт ненужный overhead при solo-founder масштабе.

### `prompts/<agent>/vX.Y.Z/` — SemVer или нет?

**Аргументы за SemVer в папках (R2):**
- Неизменность: раз задеплоен `v1.2.3` — он никогда не меняется.
- Parallel versions: можно иметь v1 и v2 одновременно в working tree.
- Явная сигнализация: v2.0.0 означает breaking change в API.

**Аргументы против полного SemVer в папках:**
- **Folder explosion:** 30 агентов × 100 версий = 3000 папок. Git history становится нечитаемым.
- **SemVer для промптов — спорная аналогия:** промпты не имеют «API» в классическом смысле. Major/minor/patch для текстовых инструкций — философски сомнительно.
- **Git already IS the version history:** `git log agents/analyst/system.md` даёт полную историю. SemVer-папки дублируют git.

**Сильное мнение (D2):** SemVer в папках имеет смысл только для **major versions** (breaking changes в поведении агента). Patch и minor — через git tags и git history.

Рекомендуемая структура R3:

```
agents/
  analyst/
    v1/
      system.md          # locked, immutable after tag
      changelog.md       # что изменилось от предыдущей major
    v2/
      system.md          # current major
      changelog.md
    evals/
      golden.jsonl
      regression.jsonl
```

Git tags: `agent-analyst-v2.1.3`. При `git log agents/analyst/v2/system.md --oneline` видны все minor/patch изменения внутри major.

### `alphas/` — существовать ли отдельно?

**R2 проблема:** `alphas/` — абстрактная концепция (lifecycle entities), но конкретные клиенты/проекты живут отдельно. Это создаёт путаницу: куда класть новый клиент — в `alphas/clients/` или `clients/`?

**Три альтернативы:**

**Alt A: `alphas/` как отдельная папка** (R2 текущий)
```
alphas/
  clients/
  projects/
  deals/
  invoices/
```
Проблема: дублирует очевидную структуру. Добавляет уровень вложенности без смысловой нагрузки.

**Alt B: Прямые папки по типу** (убрать `alphas/` namespace):
```
jetix/
  clients/
  projects/
  deals/
  invoices/
  research-notes/
  hypotheses/
```
Проще. Каждый тип alpha — первоклассная папка.

**Alt C: `state/` как events log** — отдельный JSONL-файл для state tracking, физические папки для документов:
```
jetix/
  clients/acme-corp/       # документы
  projects/alpha/          # документы
  state/
    clients.jsonl          # lifecycle events: created, active, closed
    projects.jsonl
    deals.jsonl
```

**Решение (D3):** **Alt B** — убрать `alphas/` namespace, сделать прямые папки. При необходимости state tracking добавить `state/` с JSONL (Alt C как дополнение, не замена). `alphas/` — хорошее концептуальное слово для документации, плохое имя для папки в daily workflow.

### `decisions/` — flat vs. date-folder

**Flat** `0001-title.md` → `9999-title.md`:
- Oxide RFD использует именно это: `rfd/0001/README.adoc`.
- Плюс: линейная история, легко найти по номеру.
- Минус: при 9999 решениях всё ещё flat, сортировка нужна.

**Date-folder** `2026-04/001-title.md`:
- Плюс: natural sharding по времени.
- Минус: путаница нумерации (001 в 2026-04 vs 001 в 2026-05 — разные решения?).

**Решение (D4):** Flat, global sequential `0001-title.md` (Oxide-style). 9999 решений = ~27 лет при 1 решении в день. Достаточно. Если потребуется, перейти на 5 знаков (00001).

### `daily-log/` — 3 года = 1000 файлов

1000 файлов flat — это граница где `ls` и file explorer начинают тормозить. Year subfolders — очевидное решение:

```
daily-log/
  2024/
    2024-01-15.md
    2024-01-16.md
  2025/
    ...
  2026/
    2026-04-15.md
```

При Obsidian — работает calendar plugin. При `rg` — искать по всем годам без проблем. При `ls daily-log/2026/` — видны только текущие записи.

**Решение (D7):** Year subfolders обязательны при >365 файлов в `daily-log/`.

---

## Часть I. Tooling для обеспечения структуры

### Git hooks для нейминг-валидации

```bash
#!/bin/bash
# .git/hooks/pre-commit
# Валидация: все новые файлы должны быть kebab-case

git diff --cached --name-only --diff-filter=A | while read file; do
  basename=$(basename "$file")
  # Проверить на PascalCase, camelCase, snake_case (кроме Python)
  if [[ "$basename" =~ [A-Z] ]] && [[ "$file" != *.py ]]; then
    echo "ERROR: $file uses uppercase. Use kebab-case for file names."
    exit 1
  fi
  if [[ "$basename" =~ _ ]] && [[ "$file" != *.py ]] && [[ "$file" != *.yaml ]]; then
    echo "WARNING: $file uses underscore. Consider kebab-case."
  fi
done
```

### CI checks (GitHub Actions)

```yaml
# .github/workflows/structure-check.yml
name: Structure Compliance

on: [push, pull_request]

jobs:
  check-naming:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check kebab-case naming
        run: |
          python scripts/check-naming.py
      - name: Check README exists in key dirs
        run: |
          for dir in clients projects roles agents wiki; do
            [ -f "jetix/$dir/README.md" ] || echo "Missing README in jetix/$dir/"
          done
      - name: Check prompts have evals
        run: |
          for agent_dir in agents/*/; do
            agent=$(basename "$agent_dir")
            [ -d "agents/$agent/evals" ] || echo "Missing evals for $agent"
          done
      - name: Lint markdown
        uses: DavidAnson/markdownlint-cli2-action@v16
        with:
          globs: '**/*.md'
```

### Search tooling

```bash
# ripgrep алиасы в ~/.zshrc
alias jrg='rg --glob "!_archive" --glob "!.git"'  # поиск без архива
alias jwiki='rg -l --glob "jetix/wiki/**"'           # поиск только по wiki
alias jdec='ls jetix/decisions/ | sort -r | head -20' # последние решения

# fzf preview для быстрой навигации
alias jf='rg --files jetix/ | fzf --preview "bat --color=always {}"'

# DuckDB для JSONL state queries
# duckdb -c "SELECT * FROM 'jetix/state/clients.jsonl' WHERE status = 'active'"
```

### Obsidian-совместимая валидация

```python
# scripts/check-frontmatter.py
import os
import yaml
import re

REQUIRED_FIELDS = {
    'wiki': ['title', 'area', 'tags'],
    'decisions': ['title', 'state', 'authors'],
    'roles': ['title', 'purpose', 'accountabilities'],
}

def check_file(path, file_type):
    with open(path) as f:
        content = f.read()
    if not content.startswith('---'):
        print(f"WARN: {path} missing YAML frontmatter")
        return
    frontmatter = yaml.safe_load(content.split('---')[1])
    for field in REQUIRED_FIELDS.get(file_type, []):
        if field not in frontmatter:
            print(f"ERROR: {path} missing field '{field}'")
```

---

## Часть J. Практические выходы для Jetix

### J1. Финальная стресс-тестированная структура (R3)

```
jetix-os/                                    # Root monorepo
│
├── life-os/                                 # Личная OS (Option 2: параллельно)
│   ├── decisions/                           # Личные решения (YYYY-MM-DD-slug.md)
│   ├── okrs/                               # OKRs по кварталам
│   ├── letters/                             # Личные письма
│   ├── health/                              # Здоровье (PARA-Resources)
│   ├── reflection/                          # Рефлексии и ретроспективы
│   ├── daily-log/                           # Дневник
│   │   ├── 2025/
│   │   └── 2026/
│   └── wiki/                               # Личное знание (отдельно от бизнес)
│       └── _index.md
│
├── jetix/                                   # Business part
│   │
│   ├── roles/                              # D1: Combined manifest (Alt 1)
│   │   ├── README.md                       # Что такое role manifest
│   │   ├── strategic-management/
│   │   │   ├── manifest.md                 # Purpose + Accountabilities + Domains
│   │   │   └── executor.yaml              # Кто/что сейчас заполняет роль
│   │   ├── analyst/
│   │   ├── sales-lead/
│   │   ├── delivery/
│   │   ├── knowledge-synth/
│   │   └── ... (12+ ролей)
│   │
│   ├── agents/                             # D1: Конкретные AI-implementations
│   │   ├── README.md
│   │   ├── analyst/
│   │   │   ├── v1/
│   │   │   │   ├── system.md              # D2: Только major versions как папки
│   │   │   │   └── changelog.md
│   │   │   ├── v2/
│   │   │   │   ├── system.md              # Current major
│   │   │   │   └── changelog.md
│   │   │   └── evals/
│   │   │       ├── golden.jsonl
│   │   │       └── regression.jsonl
│   │   └── ... (12+ агентов)
│   │
│   ├── clients/                            # D3: Прямая папка (убран alphas/ namespace)
│   │   ├── README.md
│   │   ├── acme-corp/
│   │   │   ├── _meta.yaml                 # status, owner, tags, gdpr-delete-at
│   │   │   ├── brief.md
│   │   │   ├── contracts/
│   │   │   ├── invoices/                  # 10 лет хранения (HGB)
│   │   │   ├── correspondence/
│   │   │   └── research/
│   │   └── _archive/
│   │       └── 2025/
│   │
│   ├── projects/                           # D3: Прямая папка
│   │   ├── README.md
│   │   ├── alpha-mvp/
│   │   │   ├── _meta.yaml
│   │   │   ├── charter.md
│   │   │   ├── tasks/
│   │   │   └── deliverables/
│   │   └── _archive/
│   │
│   ├── deals/                              # D3: Pipeline сделок
│   │   ├── README.md
│   │   ├── deal-2026-001/
│   │   └── _archive/
│   │
│   ├── decisions/                          # D4: Flat 0001-slug.md (Oxide-style)
│   │   ├── README.md                       # Как создать новое решение
│   │   ├── 0001-monorepo-architecture.md
│   │   ├── 0002-agent-naming-convention.md
│   │   └── template.md
│   │
│   ├── postmortems/
│   │   ├── README.md
│   │   ├── 2025-04-15-api-outage.md
│   │   └── _archive/
│   │
│   ├── wiki/                              # D6: Отдельный бизнес-wiki (не мерджить с life-os)
│   │   ├── _index.md
│   │   ├── concepts/
│   │   ├── processes/
│   │   ├── technologies/
│   │   └── clients/                       # Общее знание о клиентском сегменте
│   │
│   ├── research-notes/                    # D3: Исследовательские заметки
│   │   ├── README.md
│   │   └── 2026-04-15-market-analysis.md
│   │
│   ├── hypotheses/                        # D3: Эксперименты и гипотезы
│   │   └── README.md
│   │
│   ├── letters/                           # Бизнес-письма
│   │   └── 2026-04-15-to-investor.md
│   │
│   ├── state/                             # D3: JSONL lifecycle tracking
│   │   ├── clients.jsonl
│   │   ├── projects.jsonl
│   │   └── deals.jsonl
│   │
│   └── config/
│       ├── agents.yaml                    # Реестр агентов
│       └── roles.yaml                     # Реестр ролей
│
├── docs/                                  # Diátaxis framework
│   ├── tutorials/
│   ├── how-to/
│   ├── reference/
│   └── explanation/
│
├── tools/                                 # Python pipelines
│   ├── README.md
│   ├── state-sync.py                      # Sync JSONL state
│   ├── archive.py                         # Archive automation
│   └── check-naming.py                    # CI validation
│
├── scripts/                               # Bash/shell helpers
│   ├── new-decision.sh
│   ├── new-client.sh
│   └── new-agent.sh
│
├── infra/                                 # Hetzner / server configs
│   ├── docker-compose.yml
│   └── nginx/
│
├── secrets/                               # SOPS-encrypted
│   ├── .sops.yaml
│   └── api-keys.enc.yaml
│
├── templates/                             # D8: Top-level templates
│   ├── client-brief.md
│   ├── project-charter.md
│   ├── postmortem.md
│   ├── decision.md
│   ├── role-manifest.md
│   ├── agent-system-prompt.md
│   ├── research-note.md
│   └── daily-log.md
│
├── .claude/
│   └── agents/                            # Claude Code sub-agents config
│
├── .github/
│   └── workflows/
│       ├── structure-check.yml
│       ├── prompt-eval.yml
│       └── markdown-lint.yml
│
├── justfile                               # Task runner
├── .markdownlint.yaml
├── .gitignore
└── README.md
```

**Ключевые изменения от R2 к R3:**
1. `roles/` + `executors/` → `roles/` (manifest) + `agents/` (implementation) с combined manifest
2. `prompts/<agent>/vX.Y.Z/` → `agents/<name>/v1/`, `agents/<name>/v2/` (только major)
3. `alphas/` убран — прямые папки `clients/`, `projects/`, `deals/`
4. `_archive/` внутри каждой зоны (не top-level)
5. `state/` как отдельная JSONL-директория для lifecycle tracking
6. `daily-log/` разбит по годам

### J2. Нейминг-конвенция: полная спецификация

```
НЕЙМИНГ СТАНДАРТ JETIX OS v1.0
================================

ФАЙЛОВАЯ СИСТЕМА:
- Все папки и файлы: kebab-case
- Python файлы: snake_case (исключение)
- YAML/TOML keys: snake_case

ЗАПРЕЩЕНО:
- PascalCase, camelCase в именах файлов
- Пробелы в именах файлов
- Специальные символы кроме дефиса и точки
- Подчёркивание в папках (кроме _archive, _meta, _index)

ДАТЫ:
- daily-log: YYYY-MM-DD.md (обязательно)
- postmortems: YYYY-MM-DD-incident-slug.md
- letters: YYYY-MM-DD-to-recipient.md
- decisions: НЕТ даты в имени → только 0001-slug.md
- wiki: НЕТ даты в имени

НУМЕРАЦИЯ:
- decisions/: 0001-slug.md (4 знака, глобально sequential)
- agents/: имя-роли/ (без номеров)
- clients/: slug компании (acme-corp, not acme_corp)

ВЕРСИИ:
- Промпты (major): agents/<name>/v1/, v2/
- Git tags (minor/patch): agent-<name>-v1.2.3
- Никогда: file-v1.md, file.md.v1

ЗАРЕЗЕРВИРОВАННЫЕ ИМЕНА:
- README.md       # каждая папка-зона
- _meta.yaml      # метаданные папки/записи
- _index.md       # навигационный индекс
- _archive/       # архив внутри зоны
- .gitkeep        # placeholder
- template.md     # в папке decisions/

РАСШИРЕНИЯ:
- Документы: .md (markdown)
- Данные: .jsonl (events), .yaml (config), .toml (app config)
- Секреты: .enc.yaml (SOPS encrypted)
- Скрипты: .py, .sh
- Tasks: justfile (без расширения)
```

### J3. Таблица масштабирования (Solo → Mega-corp)

| Фаза | Executors | Clients | Projects | Ключевые изменения структуры |
|---|---|---|---|---|
| **Solo-0** | 1 + 8 agents | <50 | <15 | Текущая R3 структура |
| **Solo-1** | 1 + 15 agents | 50-200 | 15-50 | Добавить `state/` JSONL, year-subfolders в daily-log |
| **Small Team** | 1 + 3 humans + 20 agents | 200-500 | 50-100 | Submodule для life-os, client sharding по типу |
| **Scale-up** | 5-10 + 30 agents | 500-2000 | 100-300 | Отдельный репо life-os, отдельный wiki-сервис, Scalar |
| **Mega-corp** | 50+ + 100 agents | 2000+ | 300+ | Federation, отдельные репо по доменам, custom VCS |

### J4. Протокол депрекации/архивации

```markdown
ТРИГГЕРЫ АРХИВАЦИИ:
- Клиент: status = closed > 30 дней
- Проект: last activity > 90 дней или explicit close
- Роль: unassigned > 6 месяцев и нет active projects
- Агент: prompt not updated > 12 месяцев, eval score dropping

ПРОЦЕДУРА:
1. Обновить _meta.yaml: status: archived, archived_at: YYYY-MM-DD
2. Создать postmortem (если проект/агент был активен > 1 месяца)
3. Проверить GDPR: пометить в _gdpr-deletion-log.yaml сроки удаления
4. mv <entity>/ _archive/YYYY/<entity>/
5. git commit -m "archive(<type>): <name> — <причина>"
6. Обновить _index.md родительской зоны

GDPR DELETION:
- Персональные данные клиентов: удалить после 10 лет (HGB/AO)
- Email-адреса и личные данные: проверить каждые 2 года
- Инвойсы: хранить 10 лет, удалить персональные данные после срока
- Формат записи: _gdpr-deletion-log.yaml с датами

ХРАНИЛИЩЕ:
- Архив остаётся в git (не BFG, не hard delete)
- Исключение: secrets (BFG при случайном commit)
- GDPR-удаление: документировать в deletion-log, не молча удалять
```

### J5. Cross-cutting: рекомендованный паттерн

**Canonical location + YAML frontmatter tags**

```yaml
# Пример wiki-страницы с cross-cutting тегами
---
title: Стратегия ценообразования Enterprise
area: business
tags: [strategy, pricing, enterprise, client-acme, client-beta, project-scale]
related:
  - clients/acme-corp/
  - projects/enterprise-scale/
owner: ruslan
last_reviewed: 2026-04-15
---
```

Поиск cross-cutting документов:
```bash
# Всё, связанное с клиентом acme
rg "client-acme" --glob "*.md" -l

# Через DuckDB если state в JSONL
duckdb -c "SELECT path, tags FROM 'wiki/**/*.jsonl' WHERE tags LIKE '%client-acme%'"
```

### J6. Life-OS vs. Jetix: граница и миграция

**Сейчас (Option 2):** `life-os/` и `jetix/` параллельно в одном репо. Разделение по смыслу:

| Принадлежит `life-os/` | Принадлежит `jetix/` |
|---|---|
| Личный дневник, рефлексии | Бизнес-решения (decisions/) |
| Личные OKRs (здоровье, отношения) | Бизнес-OKRs (revenue, clients) |
| Личные письма | Бизнес-переписка |
| Личное wiki (книги, идеи) | Бизнес-wiki (processes, clients) |
| Health-трекинг | Postmortems |

**Серая зона:** Личные бизнес-решения Ruslan как founder — в `life-os/decisions/` (это его личный выбор) или в `jetix/decisions/` (это влияет на компанию)? **Рекомендация:** если решение влияет на Jetix-операции → `jetix/decisions/`. Личное → `life-os/decisions/`.

**Миграция Option 2 → Option 3** (когда нанят первый человек):
```bash
# 1. Создать отдельный репо для life-os
cd /tmp && git clone --bare /path/to/jetix-os/life-os life-os.git

# 2. В jetix-os: заменить папку на submodule
git rm -r life-os/
git submodule add git@github.com:ruslan/life-os.git life-os
git commit -m "chore: convert life-os to submodule"

# 3. Обновить .gitmodules и CI
```

### J7. 10 зонализированных решений (D1–D10)

---

**D1: `roles/` vs `executors/` — объединить или разделить?**

**Решение:** Объединить в `roles/<name>/` с `manifest.md` (абстрактное определение) + `executor.yaml` (конкретный исполнитель). Папка `agents/` существует отдельно для AI-специфичного: prompts, evals.

**Ратионал:** R2-разделение `roles/` + `executors/agents/` создаёт два места для одной концепции. Solo-founder не должен обновлять два файла при изменении роли. Holacracy-принцип «роль отдельно от человека» сохраняется внутри папки роли, а не через разделение папок.

---

**D2: `prompts/vX.Y.Z/` или альтернатива?**

**Решение:** `agents/<name>/v1/system.md` (только major versions как папки) + git tags для minor/patch. Никаких `prompts/` как отдельной зоны.

**Ратионал:** Full SemVer в папках при 30+ агентах и 100+ версиях создаёт folder explosion (3000+ папок). Git уже является version control для minor/patch. Major versions как папки сохраняют возможность параллельного A/B тестирования (v1 и v2 одновременно в working tree). Git tags `agent-analyst-v2.1.3` дают traceability.

---

**D3: `alphas/` отдельно или в других папках?**

**Решение:** Убрать `alphas/` namespace. Прямые папки: `clients/`, `projects/`, `deals/`, `invoices/`, `research-notes/`, `hypotheses/`. Добавить `state/` с JSONL для lifecycle tracking.

**Ратионал:** `alphas/` — хорошее концептуальное слово, плохое имя папки. Вводит лишний уровень вложенности. В ежедневной работе хочется `cd jetix/clients/`, а не `cd jetix/alphas/clients/`. JSONL в `state/` даёт гибкое lifecycle tracking без жёсткой иерархии.

---

**D4: `decisions/` — flat или date-folder?**

**Решение:** Flat `0001-slug.md` (Oxide RFD-style), глобальная сквозная нумерация.

**Ратионал:** Oxide Computer успешно использует эту схему. Дата создания — это метаданные внутри файла, не имя файла. Date-folder `2026-04/001-...` создаёт путаницу с локальной нумерацией. 9999 решений = 27 лет работы при интенсивном использовании — достаточный горизонт.

---

**D5: Life-OS nesting — Option 1/2/3/4?**

**Решение:** Сейчас Option 2 (параллельные папки в одном репо). Перейти к Option 3 (submodule) при первом найме человека или GDPR audit.

**Ратионал:** Option 2 даёт AI-агентам полный контекст без overhead submodules. Option 3 нужен при разграничении доступа. Option 4 (отдельные репо) — только при 5+ людях с разными правами.

---

**D6: Wiki — раздельный или объединённый?**

**Решение:** Раздельные `life-os/wiki/` и `jetix/wiki/`. НЕ объединять.

**Ратионал:** Концептуально разная аудитория и разный контент. `life-os/wiki/` — личное знание, книги, идеи. `jetix/wiki/` — бизнес-процессы, клиенты, технологии. Объединение создаёт сигнал/шум проблему для AI-агентов: агент по продажам не должен видеть личные рефлексии Ruslan в контексте поиска. YAML frontmatter `area: life` vs `area: business` — недостаточный фильтр при масштабировании.

---

**D7: Daily-log масштабирование**

**Решение:** Year subfolders с первого дня: `daily-log/2026/2026-04-15.md`.

**Ратионал:** 3 года = 1095 файлов flat. Хороший file explorer тормозит при >500 файлов в папке. Year subfolder — ноль cognitive overhead, естественная навигация, совместим с Obsidian calendar plugin.

---

**D8: Templates — top-level или per-domain?**

**Решение:** Top-level `templates/` с namespace в именах файлов.

**Ратионал:** Шаблоны — это cross-cutting. Хранить `clients/templates/`, `projects/templates/`, `postmortems/templates/` отдельно — избыточно. При top-level `templates/` есть одно предсказуемое место. Namespace в именах (`client-brief.md`, `project-charter.md`) устраняет путаницу без вложенности.

---

**D9: Archive pattern — `_archive/` per parent или top-level?**

**Решение:** `_archive/` внутри каждой зоны, с year subfolders.

**Ратионал:** Архив клиента должен быть рядом с активными клиентами (контекстуальная близость). Top-level `archive/` требует дублирования структуры и усложняет навигацию. Подчёркивание prefix (`_archive`) гарантирует что папка идёт в конце алфавитного listing'а. Year subfolders в `_archive/2025/` дают natural temporal sharding.

---

**D10: Case convention — kebab-case универсально?**

**Решение:** Да, kebab-case для всей файловой системы. Единственное исключение: Python файлы используют snake_case (PEP8).

**Ратионал:** kebab-case — URL-безопасен, case-insensitive OS-совместим (macOS HFS+), читаем без Shift. snake_case в Python — языковой стандарт, менять его под filesystem-конвенцию контрпродуктивно. PascalCase и camelCase в именах файлов запрещены: создают проблемы на case-insensitive macOS при `git clone`.

---

### J8. План миграции из текущего состояния

```
ТЕКУЩЕЕ СОСТОЯНИЕ → R3 TARGET
Estimated time: 2-4 часа active work + 1 week stabilization

ШАГ 1 (30 мин): Подготовка
- git checkout -b migration/r2-to-r3
- Создать скрипт rollback: git stash + git checkout main
- Проверить что все изменения закоммичены

ШАГ 2 (20 мин): Реструктуризация alphas/
- git mv jetix/alphas/clients/ jetix/clients/
- git mv jetix/alphas/projects/ jetix/projects/
- git mv jetix/alphas/deals/ jetix/deals/
- git mv jetix/alphas/invoices/ jetix/invoices/
- rmdir jetix/alphas/
- git commit -m "refactor: flatten alphas/ to direct folders"

ШАГ 3 (30 мин): Реструктуризация roles/ + executors/
- Для каждой роли: объединить roles/<name>/ + executors/agents/<name>/ 
  в roles/<name>/{manifest.md, executor.yaml}
- Создать agents/<name>/v1/system.md из prompts/<name>/vX.Y.Z/system.md
- git mv prompts/<name>/ agents/<name>/
- Переименовать папки в agents/<name>/v1/ (только current major)
- git commit -m "refactor: consolidate roles+executors, rename prompts→agents"

ШАГ 4 (15 мин): Добавить year-subfolders в daily-log
- mkdir -p life-os/daily-log/{2024,2025,2026}
- git mv life-os/daily-log/2024-*.md life-os/daily-log/2024/
- git mv life-os/daily-log/2025-*.md life-os/daily-log/2025/
- git mv life-os/daily-log/2026-*.md life-os/daily-log/2026/
- git commit -m "refactor: year-subfolder daily-log"

ШАГ 5 (20 мин): Templates
- mkdir templates/
- Создать базовые шаблоны из существующих файлов
- git add templates/
- git commit -m "feat: add top-level templates directory"

ШАГ 6 (15 мин): State JSONL
- mkdir jetix/state/
- python tools/generate-state.py  # генерировать из существующих _meta.yaml
- git add jetix/state/
- git commit -m "feat: add JSONL state tracking"

ШАГ 7 (10 мин): CI и tooling
- Добавить .github/workflows/structure-check.yml
- Добавить .markdownlint.yaml
- git add .github/
- git commit -m "feat: add structure compliance CI"

ШАГ 8: PR + Review
- git push origin migration/r2-to-r3
- Создать PR, проверить CI, смержить

BREAKING POINTS (где может сломаться):
- Все hardcoded пути в scripts/ и tools/ нужно обновить
- .claude/agents/ конфиги могут ссылаться на prompts/ → обновить на agents/
- Obsidian vault settings нужно обновить если есть excluded folders
- Любые external automation (Zapier, n8n) с путями к файлам

ОТКАТ:
- git revert <merge commit SHA> — если что-то сломалось после merge
- git checkout main && git stash — если ещё в branch
```

### J9. Антипаттерны Jetix (8-10 конкретных)

1. **«Alpha namespace as extra layer»** — вкладывать `alphas/clients/` вместо `clients/`. Добавляет уровень вложенности без смысловой нагрузки. Каждый navigate event стоит когнитивных усилий.

2. **«Full SemVer folder explosion»** — `prompts/analyst/v1.0.0/`, `v1.0.1/`, `v1.1.0/`... при 30+ агентах и 100+ версиях = 3000+ папок. Git уже version control — использовать его.

3. **«Split roles and executors across top folders»** — `roles/analyst/manifest.md` + `executors/agents/analyst/executor.yaml`. Одна концепция в двух местах. При изменении роли нужно обновить оба файла — гарантированный drift.

4. **«Flat 1000-file directories»** — `clients/` с 1000 папками без sharding. `ls`, file explorer, AI context window — всё тормозит. Trigg: >500 entries → sharding по типу.

5. **«Wiki date-in-filename»** — `wiki/2024-03-15-pricing-strategy.md`. Дата в wiki-странице сигнализирует устаревание. Через год страница выглядит obsolete даже если актуальна.

6. **«Life-OS forever nested»** — держать `life-os/` в бизнес-монорепо после найма первого человека. Придётся давать доступ к личным данным или городить subpath access control.

7. **«Two wikis без разграничения»** — `life-os/wiki/` и `jetix/wiki/` со схожим контентом без чёткого разделения. AI-агенты получают смешанный контекст. Правило: концепт принадлежит только одному wiki.

8. **«Decisions by date-folder»** — `decisions/2026-04/001-...` создаёт локальную нумерацию (001 есть в каждом месяце). Ссылаться на решение по номеру невозможно без знания месяца.

9. **«Templates scattered per-domain»** — `clients/templates/`, `projects/templates/`, `agents/templates/`. Новый collaborator (человек или агент) не знает где искать шаблон. Единое место → predictable.

10. **«Archive as separate top-level repo или branch»** — `git branch archive/2024` требует checkout для поиска. Архив должен быть доступен для поиска в рабочем дереве — `_archive/` внутри зоны решает это.

### J10. Критерии успеха (измеримые)

| Критерий | Целевое значение | Как измерять |
|---|---|---|
| **Onboarding нового агента** | <1 часа от нуля до первого самостоятельного action | Засечь время, задокументировать в postmortem |
| **Найти любой документ** | <2 минут без поиска для известной категории | User test с новым collaborator |
| **Поиск по репо** | <5 секунд с `rg` для любого термина | `time rg "term" jetix/` |
| **Нет дублирования source of truth** | 0 файлов с одинаковым canonical content в двух местах | `scripts/check-duplicates.py` |
| **Структура выдерживает 10x рост** | Те же правила работают при 500 clients, 50 agents, 200 projects | Design review при каждой фазе |
| **GDPR compliance** | Все client records имеют `gdpr-delete-at` в _meta.yaml | `scripts/check-gdpr-meta.py` |
| **CI check** | <3 минут на все structure checks | GitHub Actions timing |
| **Naming compliance** | 0 файлов нарушающих kebab-case (кроме Python) | `scripts/check-naming.py` в CI |

---

## Итоговое резюме: что изменить от R2, что оставить

### Оставить из R2 ✓

| R2-решение | Почему оставить |
|---|---|
| Монорепо | Единый контекст для AI-агентов — критически важно |
| `decisions/` как RFD-процесс | Oxide-паттерн правильный |
| `postmortems/` отдельно | Правильно — это отдельный жанр |
| `.claude/agents/` | Tooling-специфично, правильное место |
| `infra/` отдельно | Правильное разделение concerns |
| `secrets/` с SOPS | Обязательно |
| `justfile` | Правильный task runner для гибридного репо |
| Holacracy-inspired `roles/` | Концептуально верно |
| `evals/<agent>/golden.jsonl` | Правильная структура для eval |
| `life-os/` параллельно `jetix/` | Option 2 правильный на текущем этапе |

### Изменить в R2 → R3 ✗→✓

| R2-проблема | R3-решение |
|---|---|
| `alphas/` как namespace-папка | Убрать, прямые папки `clients/`, `projects/` |
| `roles/` + `executors/agents/` split | Объединить в `roles/<name>/` + отдельный `agents/` для prompts/evals |
| `prompts/<agent>/vX.Y.Z/` full SemVer | Только major versions как папки в `agents/<name>/v1/` |
| `daily-log/` flat | Year subfolders обязательно |
| Templates разбросаны | Top-level `templates/` |
| Нет JSONL state tracking | Добавить `state/` |
| Нет CI structure checks | `.github/workflows/structure-check.yml` |
| Нет явных GDPR-меток | `_gdpr-deletion-log.yaml` в client folders |

---

*Документ подготовлен: апрель 2026. Источники: [Google ACM CACM](https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/), [Meta Sapling](https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/), [Microsoft Scalar](https://devblogs.microsoft.com/devops/introducing-scalar/), [Oxide RFD 1](https://rfd.shared.oxide.computer/rfd/0001), [GitLab Handbook](https://handbook.gitlab.com/handbook/), [Johnny.Decimal](https://johnnydecimal.com/), [PARA Method](https://fortelabs.com/blog/para/), [Diátaxis](https://diataxis.fr/), [Holacracy Constitution 5.0](https://www.holacracy.org/constitution/5-0/), [Zettelkasten.de](https://zettelkasten.de/introduction/), [SemVer 2.0](https://semver.org), [Germany Data Retention Law](https://www.csp-sw.com/blog/retention-periods), [Thoughtworks Monorepo](https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/monorepo-vs-multirepo), [Latitude.so Prompt Versioning](https://latitude.so/blog/prompt-versioning-best-practices), [Braintrust Prompt Versioning](https://www.braintrust.dev/articles/what-is-prompt-versioning).*
