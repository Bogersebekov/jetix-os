---
title: CRM System Build — Deep Prompt для бригадира на сервере
date: 2026-04-26
type: deep-prompt
target: Claude Code на сервере (бригадир) → swarm cycle (1-3 циклов)
parent_task: Daily Log 26.04 → "Создание CRM-системы на сервере"
notion_ref: https://www.notion.so/34e2496333bf81108ab3e774f992c52e
authored_by: Cloud Cowork (по прямой инструкции Ruslan'а — глубокий prompt сразу, не short brief)
status: ready-to-launch
---

# CRM System Build — Deep Prompt

## §0. Контекст + цель

Ruslan строит **мега-CRM** для всех людей и организаций которые встречаются на пути Jetix. Не sales-only — **multi-purpose network database**: клиенты + инвесторы + партнёры + менторы/advisors/facilitators/consultants + co-founders + друзья + просто интересные люди.

**Принципы (non-negotiable):**

1. **Filesystem = SoT (D17).** CRM живёт в `crm/`. Notion = опциональный read-only view-layer (Phase 2).
2. **Markdown-first.** Каждый человек = один `.md` файл с YAML frontmatter (= "колонки таблицы") + Markdown body (= детальная страница).
3. **Grep-friendly.** До ~10K записей grep по frontmatter — мгновенно. Никаких heavy DB зависимостей в Phase 1.
4. **Multi-role с Day 1.** Один человек может быть одновременно client + advisor + friend; роли мигрируют (interesting → friend → partner → investor).
5. **Strategy-aware.** Поля §7 (что мы можем предложить) и §8 (что можем получить) автоматически подтягивают hooks из `decisions/` через CC.
6. **Lean, не Salesforce.** Никаких enterprise-CRM features (workflow automation, multi-tenancy, permissioning) в Phase 1.
7. **Conventions per CLAUDE.md.** YAML frontmatter обязателен, kebab-case slugs, YYYY-MM-DD даты, append-only logs (новое сверху).

**Цель cycle:** к концу — **готовый рабочий продукт** (skeleton + 8 skills + dashboard + tests + первые 5 импортированных контактов + README). Ruslan нажимает `/crm-add` и оно работает.

---

## §1. Layout (file tree)

```
crm/
├── PLAN.md                      # копия Notion-плана (ref doc)
├── README.md                    # как работает CRM, для людей
├── icp.md                       # EXISTS, не трогать (data-asset, ICP cards)
├── people/                      # один .md файл на человека
│   ├── _example-person.md       # эталонный пример (committed для reference)
│   └── ...
├── orgs/                        # организации (та же schema + extra fields)
│   └── ...
├── index.md                     # auto-generated каталог-таблица (read-only header)
├── log.md                       # append-only хронология (новое сверху)
├── views/                       # сохранённые queries (read-only output)
│   ├── advisors-search-2026-04-26.md
│   ├── stuck-no-touch-14d.md
│   └── dach-warm-leads.md
├── _templates/
│   ├── person.md                # template для нового человека (14 секций)
│   └── org.md                   # template для организации
├── _schema/
│   ├── frontmatter.yaml         # JSON Schema-style спецификация полей
│   ├── roles.yaml               # enum ролей + переходы
│   ├── statuses.yaml            # enum pipeline statuses + переходы
│   └── strategy-hooks.yaml      # mapping Jetix-strategy → "что предложить" / "что получить"
├── _scripts/
│   ├── crm.py                   # main CLI (все skills delegate сюда)
│   ├── frontmatter.py           # parser + validator
│   ├── index_builder.py         # rebuild crm/index.md
│   ├── dashboard.py             # /crm-dash output
│   ├── views.py                 # query engine
│   ├── voice_router.py          # routing items с target:crm из voice-pipeline
│   └── strategy_hooks.py        # подтягивает offers/asks из decisions/
└── _tests/
    ├── fixtures/
    │   ├── sample-person-anton.md
    │   ├── sample-person-vladislav.md
    │   └── sample-org-acme.md
    ├── test_frontmatter.py
    ├── test_views.py
    ├── test_index_builder.py
    └── test_strategy_hooks.py
```

**Skills (`.claude/skills/`):**

```
.claude/skills/
├── crm-add.md
├── crm-show.md
├── crm-list.md
├── crm-search.md
├── crm-touch.md
├── crm-update.md
├── crm-rebuild-index.md
├── crm-dash.md
├── crm-stuck.md
└── crm-weekly.md
```

Каждый skill — тонкий wrapper (3-10 строк) который вызывает соответствующую команду `_scripts/crm.py`.

---

## §2. Schema (frontmatter)

Полная спецификация полей. Все поля — **optional** кроме `name`, `slug`, `type`, `roles`, `created`, `updated`. Нет данных = поле опускается (не пустое).

### 2.1 Identity

```yaml
name: "Иван Иванов"                    # required, человеческое полное имя
slug: ivan-ivanov                       # required, kebab-case, = filename без .md
type: person                            # required, person | org
aliases: [ "Vanya", "ii_dev", "ivan_xyz_telegram" ]   # альт. имена/handles
```

### 2.2 Roles (multi)

```yaml
roles:                                  # required, минимум 1
  - advisor
  - friend
```

Возможные значения (см. `_schema/roles.yaml`):

- **Sales pipeline:** `client_lead`, `client_active`, `client_past`, `client_lost`
- **Capital:** `investor_prospect`, `investor_active`
- **Partnership:** `partner_prospect`, `partner_active`, `partner_past`
- **Personal advisory:** `mentor`, `advisor`, `facilitator`, `consultant`
- **Team:** `cofounder_prospect`, `hire_prospect`, `hire_active`, `hire_past`
- **Network:** `friend`, `interesting`, `vendor`, `competitor`

### 2.3 Background

```yaml
niche: "AI consulting / DACH Mittelstand"
occupation: "Founder @ Acme AI"
income_bucket: "200K-1M"                # < 50K | 50K-200K | 200K-1M | 1M-10M | > 10M | unknown
location_country: DE
location_city: Berlin
languages: [ ru, en, de ]
age: 34                                  # optional
```

### 2.4 Contact

```yaml
contact:
  email: ivan@example.com
  telegram: "@ivan_xyz"
  linkedin: "linkedin.com/in/ivan-ivanov"
  twitter: "@ivanovx"
  instagram: "@ivan.xyz"
  youtube: "youtube.com/@ivanovich"
  tiktok: ""
  website: "ivan.dev"
  phone: "+49 ..."
  other_links:                           # любые другие
    - "github.com/ivanivanov"
    - "substack.com/@ivan"
```

### 2.5 Audience (новое поле per Ruslan 26.04)

```yaml
audience:
  total_followers: 12500                 # суммарно across platforms
  breakdown:
    linkedin: 8000
    twitter: 3500
    youtube: 1000
  audience_type: "DACH startup founders + AI builders"   # WHO именно подписан
  audience_quality: "engaged, technical, ~30% AI-native"  # короткая характеристика
  icp_overlap_pct: 60                    # % overlap с Jetix ICP (D22)
  notes: "большинство в DACH, активны в LinkedIn comments"
```

### 2.6 Tools / Platforms (новое поле per Ruslan 26.04)

```yaml
tools:
  uses: [ "Cursor", "Claude Code", "Notion", "Linear" ]   # что использует
  owns:                                  # что построил/владеет
    - "acme-ai.com (SaaS, 50 paying customers)"
    - "ai-newsletter (substack, 5K subs)"
  platforms_active_on: [ linkedin, twitter, indiehackers ]
```

### 2.7 Origin

```yaml
origin:
  source_channel: indiehackers          # indiehackers | linkedin | referral | event | cold_outreach | warm_intro | etc.
  introduced_by: anton-mentor           # slug или null
  first_contact_date: 2026-04-20
  context: "ответил на мой пост про AI Pilot в IH milestone thread"
```

### 2.8 ICP fit (D22 — semi-automatic, refine later)

```yaml
icp:
  startupper: yes                        # yes | no | unknown
  azart: 4                               # 1-5
  stable: 5                              # 1-5
  adequate: 5                            # 1-5
  upward: 4                              # 1-5
  total: 18                              # auto-computed sum (см. index_builder.py)
  scored_at: 2026-04-26
  scored_by: ruslan                      # ruslan | cc | tbd
```

### 2.9 Pipeline

```yaml
pipeline:
  status: discovery_call                 # см. _schema/statuses.yaml
  last_touch_date: 2026-04-26
  next_action: "прислать proposal до 30.04"
  next_action_date: 2026-04-30
  owner: ruslan                          # кто двигает (Ruslan / agent / partner)
```

### 2.10 Value lens

```yaml
value:
  to_jetix: 4                            # 1-5
  to_jetix_why: "deep DACH Mittelstand network + 50 paying customers as case-study sources"
  to_them: "early access к Jetix Network methodology + co-marketing"
  relationship_strength: 3               # 1-5 (1=cold, 5=close ally)
```

### 2.11 Meta

```yaml
tags: [ "#dach", "#mittelstand", "#ai-native", "#high-priority" ]
created: 2026-04-26
updated: 2026-04-26
```

### 2.12 Schema validation

`_scripts/frontmatter.py` валидирует:

- Required fields присутствуют
- Enum-значения валидны (roles, statuses, source_channel, income_bucket)
- Даты в YYYY-MM-DD
- Slugs в kebab-case
- Telegram handles начинаются с `@`
- 1-5 поля в диапазоне
- ICP total = sum (azart + stable + adequate + upward); startupper отдельно (gate)

При ошибке — exit 1 с явным error message ("which file, which field, what wrong, how to fix").

---

## §3. Per-person markdown body (14 секций)

Файл `crm/people/<slug>.md` имеет YAML frontmatter (см. §2) + Markdown body со **строго фиксированной структурой** (для grep, parse, и Claude Code-навигации):

```markdown
---
<frontmatter>
---

# Иван Иванов

## §1. Кто
[3-5 строк краткое био. Чем занимается, откуда, что важно знать с первого взгляда.]

## §2. Связи (existing)
[Список людей и организаций уже находящихся в CRM с которыми этот человек связан.
Auto-pulled из wiki/graph/edges.jsonl + ручные дополнения. Формат:]

- **[anton-mentor](../people/anton-mentor.md)** — co-founder в предыдущем стартапе (2018-2021)
- **[acme-corp](../orgs/acme-corp.md)** — текущий employer
- **[vladislav-economist](../people/vladislav-economist.md)** — общий ментор у обоих

## §3. Потенциальные связи (network он может принести)
[Кого этот человек может представить нам. Конкретные имена/организации с описаниями.
Source: что он сам сказал + observable network.]

- **CEO [Beta GmbH]** — близкий друг, потенциальный P1A client (DACH, €5M revenue)
- **[Имя инвестора]** — angel в его стартапе, активен в DACH AI deals
- **сообщество X** — он там модератор, может представить группе

## §4. Аудитория
[Детали (дублирует frontmatter audience: для читаемости + раскрывает контекст).]

- **Размер:** 12,500 across platforms (LinkedIn 8K + Twitter 3.5K + YouTube 1K)
- **Кто:** DACH startup founders + AI builders, ~30% AI-native, средний engagement 4-6%
- **Overlap с Jetix ICP:** ~60% (Startupper archetype dominant)
- **Качество:** technical audience, реагируют на конкретные case-studies, не на marketing fluff
- **Где активен:** LinkedIn comments, Twitter threads, IH milestones
- **Channel value для Jetix:** возможный co-marketing partner (newsletter swap), guest posts

## §5. Инструменты / платформы
[Что он использует (показывает совместимость с нашим стеком) и что он построил/владеет.]

**Использует:** Cursor, Claude Code, Notion, Linear, Vercel
**Построил / владеет:**
- acme-ai.com — SaaS для DACH manufacturing, 50 paying customers, ~€500K ARR
- ai-newsletter — Substack, 5K подписчиков, weekly DACH AI digest
**Активен на:** LinkedIn (primary), Twitter, IndieHackers

## §6. Цели и задачи (его)
[Что ОН хочет. Карьерные / финансовые / личные цели если знаем. Помогает понять как align с нашими offers.]

- Растит acme-ai.com до €2M ARR к концу 2026 (textile/manufacturing vertical)
- Хочет европейский AI-community lead role (publicly stated в LinkedIn)
- Long-term: exit acme-ai.com через 3-5 лет, перейти в investing
- Personal: научиться strategic frameworks (упоминал Левенчука и системное мышление)

## §7. Что мы можем предложить ему сейчас
[Auto-suggested CC через strategy_hooks.py на основе decisions/JETIX-* + L5/L6/L7 + текущих offers.
Формат: <hook> — <как применимо к этому человеку>. Manually editable.]

- **[L6 Community access]** — early invite в Mittelstand AI Alliance founding cohort (он fits как DACH AI-native founder)
- **[L7 Producer Services hypothesis H4+H5]** — collab возможность: его newsletter + наш content
- **[Sales Methodology Wiki]** — share early version в exchange за case-study acme-ai.com
- **[D20 USB-C positioning]** — позиционирование Jetix как infrastructure layer ПОД его SaaS (не конкурент)

## §8. Что мы можем получить от него / cooperation
[Auto-suggested + manual. Отталкиваемся от наших страт нужд (Phase 1: paying clients + advisors + DACH network).]

- **DACH Mittelstand intros** — у него 50 paying customers в textile/manufacturing — потенциальные P1A clients для Jetix
- **Advisor role** — opt-in candidate per cooperation-not-paid pattern (RU+EN, weekly, скоринг finalized 26.04)
- **Newsletter swap** — co-marketing когда у нас будет content
- **Use-case validation** — feedback на Jetix Methodology v1 от practitioner-фаундера
- **Investor pipeline (Phase 2)** — он cited хочет в investing → потенциальный angel в Jetix round

## §9. Гипотезы (что с ним можно сделать)
[Конкретные ideas с status. Helps Ruslan + рой предлагать new approaches.]

| # | Гипотеза | Status | Notes |
|---|----------|--------|-------|
| H1 | Привлечь как advisor за early access к Jetix Methodology | testing | discovery call 26.04, ждём response |
| H2 | Co-host webinar "AI for DACH Mittelstand" | untested | wait until Methodology v1 ready |
| H3 | Pilot Jetix Operating System в acme-ai.com (revenue share модель) | untested | premature до Phase 3 strategy ack |
| H4 | Newsletter cross-promotion (его 5K subs + наш list когда будет) | untested | wait until у нас newsletter |
| H5 | Через него выйти на CEO Beta GmbH (P1A lead) | untested | спросить на следующем call |

Status enum: `untested` | `testing` | `confirmed` | `refuted` | `paused`

## §10. Связь с Jetix (history overview)
[Как пересеклись + текущая температура. 3-5 строк.]

Ответил на мой post в IH milestone thread 20.04. Discovery call 26.04 (50 мин) — обсудили его acme-ai.com, мою Jetix Methodology, общих знакомых (vladislav-economist), потенциальный advisor role. Договорились: я пришлю proposal до 30.04. Темп — warm, реактивный, valuates concrete > abstract.

## §11. История взаимодействий (newest top, append-only)

### 2026-04-26 — discovery call (50 мин)
- **Channel:** Zoom
- **Agenda:** взаимное introduce, его acme-ai.com, Jetix Methodology, общие знакомые
- **Что обсудили:** [...]
- **Что договорились:** я → proposal до 30.04; он → подумает над advisor role
- **Цитаты:** "интересно посмотреть на Methodology в живую — у меня сейчас pain именно с systematizing"
- **Next:** prepare proposal

### 2026-04-20 — first contact (Telegram)
- Reply на его IH post про AI Pilot
- Согласился на discovery call

## §12. Текущий статус + next action

- **Status:** `discovery_call`
- **Next action:** прислать proposal до 30.04
- **Next action date:** 2026-04-30
- **Owner:** ruslan
- **Why this status:** ждём его response на 3 вопроса из звонка 26.04
- **Risk if stalled:** low (warm relationship, не critical lead)

## §13. Observations / red flags / notes
[Personal observations. Tone, communication style, red flags, mutual interests, life events.]

- Reaguируe на конкретику + numbers, не на marketing
- Ценит честность > polish (упомянул что "ненавижу sales decks")
- Жена работает в DACH-funded healthtech VC — потенциальный investor channel Phase 2
- Интересуется Левенчуком (общая почва для discussion)
- ⚠️ Будет осторожен с partnerships которые могут конфликтовать с acme-ai.com positioning

## §14. Источники + артефакты
[Все ссылки на профили, posts, recordings, transcripts, screenshots.]

- **LinkedIn:** linkedin.com/in/ivan-ivanov
- **IH profile:** indiehackers.com/ivan
- **Acme website:** acme-ai.com
- **Newsletter:** ivan-ai.substack.com
- **Discovery call recording:** `crm/recordings/ivan-ivanov-2026-04-26-discovery.m4a`
- **Discovery call transcript:** `crm/transcripts/ivan-ivanov-2026-04-26-discovery.md`
- **IH thread где познакомились:** [link]
```

**Орг-схема (`crm/orgs/<slug>.md`)** идентична personal схеме + extra fields в frontmatter:

```yaml
org_type: company                  # company | nonprofit | community | gov | other
founded: 2019
employees: 12
revenue_estimate: "200K-1M"        # тот же bucket-список что income_bucket
key_people: [ ivan-ivanov, peter-cto ]    # slugs (обратные ссылки)
```

И секция **§ Команда** (replaces §6 Цели individual) — список ключевых людей в этой org с roles.

---

## §4. Strategy hooks integration

**Цель:** §7 (что предложить) и §8 (что получить) **полу-автоматически** подтягиваются из живой Jetix-strategy. CC reads `_schema/strategy-hooks.yaml` + `decisions/` и предлагает relevant hooks для конкретного человека.

### 4.1 strategy-hooks.yaml — структура

```yaml
# crm/_schema/strategy-hooks.yaml
offers:                              # что МЫ можем предложить (для §7)
  - id: l6-community-access
    label: "L6 Community access"
    source: decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
    description: "Early invite в Mittelstand AI Alliance founding cohort"
    relevant_for:                    # filters per CRM person
      roles: [ partner_prospect, advisor, friend, interesting, client_lead ]
      icp_startupper: yes
      tags: [ "#dach", "#ai-native" ]
    status: active                    # active | draft | paused

  - id: l7-producer-collab
    label: "L7 Producer Services collab"
    source: decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md
    description: "Co-creation возможность (H4+H5 hypotheses из cycle 8)"
    relevant_for:
      roles: [ partner_prospect ]
      audience.total_followers_min: 1000
    status: draft

  - id: methodology-early-access
    label: "Sales Methodology Wiki — early access"
    source: decisions/JETIX-PHILOSOPHY.md
    description: "Share early Methodology в exchange за feedback / case-study"
    relevant_for:
      roles: [ advisor, mentor, facilitator, consultant, partner_prospect ]
    status: active

  # ... добавляются по мере появления новых offers

asks:                                # что мы можем ПОЛУЧИТЬ (для §8)
  - id: dach-intros
    label: "DACH Mittelstand intros (P1A leads)"
    description: "Если у человека есть DACH-network — попросить warm intros к 2-3 P1A candidates"
    relevant_for:
      location_country: DE
      tags: [ "#dach", "#mittelstand" ]

  - id: advisor-cooperation
    label: "Advisor role (cooperation-not-paid)"
    description: "RU+EN, weekly, ack params 26.04. Все 3 типа параллельно (mentor/facilitator/consultant)"
    relevant_for:
      roles: [ advisor, mentor, facilitator, consultant ]

  - id: case-study-source
    label: "Case-study source (если они paying client'ы AI-products)"
    description: "Feedback + permission использовать как case-study"
    relevant_for:
      roles: [ client_active, partner_active ]

  - id: methodology-feedback
    label: "Methodology v1 feedback"
    description: "Practitioner критика на Jetix Methodology до public launch"
    relevant_for:
      roles: [ advisor, mentor, facilitator, partner_prospect ]
      icp.adequate_min: 4

  # ...
```

### 4.2 strategy_hooks.py — функция

```python
# crm/_scripts/strategy_hooks.py

def suggest_offers(person_frontmatter: dict) -> list[dict]:
    """Returns list of {id, label, description, source, why_match} matching this person."""
    hooks = load_yaml("crm/_schema/strategy-hooks.yaml")
    matches = []
    for offer in hooks["offers"]:
        if offer["status"] != "active":
            continue
        if matches_filter(person_frontmatter, offer["relevant_for"]):
            matches.append({
                **offer,
                "why_match": explain_match(person_frontmatter, offer["relevant_for"])
            })
    return matches

def suggest_asks(person_frontmatter: dict) -> list[dict]:
    # симметрично
    ...
```

### 4.3 Использование

При `/crm-add` — после создания черновика, CC автоматически вызывает `suggest_offers + suggest_asks` и **префиллит §7 и §8** suggestions с пометкой `[auto-suggested, edit me]`. Ruslan/CC потом ручную правят / расширяют.

При `/crm-update` или `/crm-touch` — если в frontmatter поменялись `roles`, `tags`, `icp.*`, `audience.*` — re-run suggestions, добавить новые matched (existing manually-added не трогать).

При обновлении `strategy-hooks.yaml` (новые offers/asks) — отдельная команда `/crm-resync-hooks` пробегается по всем `crm/people/*.md` + перепоследовательно дополняет §7/§8 (с пометкой и без перетирания manual edits).

---

## §5. Skills spec (8 + 2)

Каждый skill — **3-10 строк** в `.claude/skills/crm-*.md`, тонкий wrapper над `_scripts/crm.py`.

### 5.1 `/crm-add <name>`

Создаёт черновик нового человека:

1. Generate slug (kebab-case from name)
2. Check `crm/people/<slug>.md` не существует (если да — fail с suggestion `<slug>-2`)
3. Apply template from `_templates/person.md`
4. Prompt user (через CC interaction) для **минимально-обязательных полей**: `roles[]`, `niche`, `location_country`, `source_channel`, `first_contact_date`, `context (1 строка)`
5. Auto-fill `created`, `updated` (today)
6. Run `suggest_offers + suggest_asks` → префилл §7 §8
7. Validate frontmatter
8. Write file
9. Append entry в `crm/log.md`: `## YYYY-MM-DD HH:MM — added <slug> (<name>)\n  roles: [...] / source: <channel>`
10. Trigger `rebuild_index` (silent — no terminal output, just regen `index.md`)

Вывод: `Added crm/people/<slug>.md. Roles: [...]. ICP scoring: TBD (run /crm-score later). Run /crm-show <slug> to view.`

### 5.2 `/crm-show <slug>`

Pretty-print full file (frontmatter parsed + body rendered):

```
=== Иван Иванов (ivan-ivanov) ===
Roles:    advisor, friend
Status:   discovery_call → next: proposal (by 2026-04-30)
ICP:      Startupper=yes, total=18/20 (azart=4, stable=5, adequate=5, upward=4)
Location: Berlin, DE
Income:   200K-1M
Audience: 12,500 (LinkedIn 8K + Twitter 3.5K + YouTube 1K)
Last touch: 2026-04-26 (today)

=== §1 Кто ===
[body §1 rendered]

=== §2 Связи (existing) ===
[body §2 rendered]

[... все 14 секций ...]
```

### 5.3 `/crm-list <filters>`

Filtered table view. Filter syntax:

```
/crm-list roles=advisor
/crm-list status=warm icp.startupper=yes
/crm-list roles=client_lead location_country=DE icp.total>=15
/crm-list tags=#dach status=cold,warm
/crm-list audience.total_followers>=5000
```

Output — Markdown table в терминал:

```
Slug              | Name             | Roles              | Status         | ICP | Last touch  | Next action
ivan-ivanov       | Иван Иванов     | advisor, friend    | discovery_call | 18  | 2026-04-26  | proposal by 04-30
peter-cto         | Peter Schmidt    | partner_prospect   | warm           | 16  | 2026-04-22  | follow-up
...
3 matches.
```

Sortable by `--sort=icp,last_touch,name` (default = `last_touch desc`).

### 5.4 `/crm-search <query>`

Полнотекстовый grep по name + aliases + body §1 (Кто) + §13 (Observations) + tags:

```
/crm-search "DACH AI"
```

Output — ranked list (по relevance):

```
ivan-ivanov         (3 hits in §1, §4, tags)
peter-cto           (2 hits in §1, §13)
acme-corp [org]     (2 hits in §6 Команда)
```

### 5.5 `/crm-touch <slug> "<note>"`

Quick log of an interaction — самый частый use-case:

```
/crm-touch ivan-ivanov "ответил в Telegram по proposal — нужен tweak по pricing"
```

Что делает:

1. Append в §11 History новую запись (newest top, today's date, note text)
2. Update frontmatter: `pipeline.last_touch_date = today`, `updated = today`
3. Append в `crm/log.md`: `## YYYY-MM-DD HH:MM — touch ivan-ivanov: ответил в Telegram...`

**No status change.** Для этого — `/crm-update`.

### 5.6 `/crm-update <slug> --field=value [--note="..."]`

Update любых fields:

```
/crm-update ivan-ivanov --status=proposal --next-action="отправить v2 proposal" --next-action-date=2026-05-02 --note="acked overall direction, просит pricing tweak"
```

Если `--note` дан — append в §11 + update last_touch_date.
Validate frontmatter после изменения. Append в `crm/log.md`.

### 5.7 `/crm-rebuild-index`

Re-generates `crm/index.md` от scratch:

```markdown
<!-- Auto-generated by /crm-rebuild-index. Do not edit manually. Last: 2026-04-26 18:42 -->

# CRM Index — All Contacts

**Total:** 47 (people: 41, orgs: 6)
**Last rebuilt:** 2026-04-26 18:42

## By role

| Role            | Count | Slugs |
|-----------------|-------|-------|
| client_lead     | 12    | [acme-ai](people/acme-ai.md), [beta-gmbh](orgs/beta-gmbh.md), ... |
| advisor         | 5     | [anton-mentor](people/anton-mentor.md), ... |
| ...             | ...   | ... |

## All contacts (sortable table)

| Slug | Name | Roles | Status | ICP | Last touch | Audience | Country |
|------|------|-------|--------|-----|------------|----------|---------|
| ivan-ivanov | Иван Иванов | advisor, friend | discovery_call | 18 | 2026-04-26 | 12.5K | DE |
| ...
```

Должно быть idempotent: если ничего не поменялось — file diff = 0.

### 5.8 `/crm-dash`

Output дашборда (см. §7 этого prompt).

### 5.9 `/crm-stuck`

Список людей `status ∈ {warm, contacted, discovery_call, proposal, negotiation}` с `last_touch_date > 14 дней назад`. Для weekly review.

### 5.10 `/crm-weekly`

Combined weekly report (см. §7).

---

## §6. Index generator

`_scripts/index_builder.py`:

1. Glob `crm/people/*.md` + `crm/orgs/*.md`
2. Parse frontmatter каждого
3. Validate (skip + warn если invalid)
4. Group by role (один человек может попасть в несколько групп)
5. Compute aggregates (counts per status, avg ICP, etc.)
6. Render Jinja2 template → `crm/index.md`
7. Compare с existing → write только если diff

**Performance target:** < 1 sec на 1000 records. Если медленнее — оптимизируй (cache parsed frontmatter в `.crm-cache.json`, invalidate by mtime).

---

## §7. Dashboard spec

`/crm-dash` outputs:

```
=== CRM DASHBOARD (2026-04-26 18:42) ===

Total: 47 contacts (41 people + 6 orgs)
Updated last 7d: 12

By role:
  client_lead:        12 (warm: 4, contacted: 5, discovery_call: 2, proposal: 1)
  client_active:       2
  client_past:         3
  investor_prospect:   3 (all cold)
  partner_prospect:    8 (warm: 3, contacted: 2, paused: 1)
  partner_active:      1
  advisor/mentor:      5 (4 в активном search 26.04)
  cofounder_prospect:  0
  hire_prospect:       2
  friend:              7
  interesting:        14

Sales pipeline (clients only):
  cold:           5
  warm:           4
  contacted:      5
  discovery_call: 2
  proposal:       1
  negotiation:    0
  closed_won:     0  ⚠️  (€0 / €50K Q2 target)
  closed_lost:    3

This week (since 2026-04-19):
  + 4 new contacts (3 indiehackers, 1 referral)
  ↑ 2 status upgrades
  ↓ 1 closed_lost

Stuck (status≠cold, no touch >14d):
  - vladislav-x  (warm, 22 days)  [client_lead]
  - acme-corp    (proposal, 18 days) ⚠️ high value [client_lead]
  - peter-mentor (contacted, 16 days) [advisor]

ICP fit distribution (clients only):
  total ≥18: 3   total 15-17: 5   total 10-14: 8   total <10: 6   unscored: 4

Channel performance (paying clients to date):
  indiehackers:  8 contacts → 0 won (insufficient data)
  linkedin:      5 contacts → 0 won
  referral:      3 contacts → 0 won
  cold_outreach: 4 contacts → 0 won

Audience leverage (advisors + partners):
  Total reach available: 47,300 followers
  AI-native audience overlap: ~62%
```

**Dashboard должен полностью fit в один terminal screen** (height ≤ 50 lines на стандартном терминале).

`/crm-weekly` — расширенная версия: + новые контакты detail, + status changes detail, + action items на следующую неделю, + ICP-channel correlation, → save в `crm/views/weekly-YYYY-MM-DD.md`.

---

## §8. Voice-pipeline integration

Existing `tools/run_pipeline.sh` (transcribe → extract → filter → review_report).

**Add:** `_scripts/voice_router.py` который смотрит на `extract` output items с polem `target: crm`:

```yaml
# пример item из voice extraction
- id: item-2026-04-26-014
  type: contact_mention
  target: crm
  intent: add | touch | update
  person_name: "Иван Иванов"
  role_hint: advisor
  source_channel: indiehackers
  context: "встретили в IH, ответил на milestone post"
  raw_quote: "[verbatim Russian quote from voice memo]"
```

При `intent: add` → создаёт draft в `crm/people/<slug>-DRAFT.md` (помечен `pipeline.status: draft-from-voice`) → ждёт Ruslan ack.

При `intent: touch` или `intent: update` — slug matching (fuzzy) → если 1 match → applies update → log в `crm/log.md` с пометкой `auto-from-voice`. Если ≥2 matches → list в review_report для disambiguation.

**Critical:** **никогда** не auto-write production записи без human review (per `feedback_review_before_build`). Voice-routed items всегда **DRAFT** до explicit ack от Ruslan'а.

---

## §9. Tests

`_tests/`:

### 9.1 `test_frontmatter.py`

- valid frontmatter parses correctly
- missing required field → ValidationError с правильным message
- invalid enum (роль `xyz`) → ValidationError
- ICP total ≠ sum → auto-fix + warning
- date в неверном формате → ValidationError
- 1-5 поле = 6 → ValidationError

### 9.2 `test_views.py`

- filter `roles=advisor` возвращает только людей с `advisor in roles`
- combined filter (3+ conditions) работает
- sort работает
- pagination работает (если >50 records)
- invalid filter syntax → friendly error

### 9.3 `test_index_builder.py`

- single person rebuilds correctly
- 100 people rebuilds под 1 sec
- идемпотентность (rebuild дважды = identical files)
- skip invalid frontmatter с warning

### 9.4 `test_strategy_hooks.py`

- offer matches person с правильными filters
- offer не matches при mismatched роле
- multiple matches order'ятся по relevance
- offers с `status: draft` не показываются по default

### 9.5 fixtures

3-5 sample персон в `_tests/fixtures/` — используется во всех tests.

**Test runner:** `pytest crm/_tests/`. Должно быть green перед AWAITING-APPROVAL.

---

## §10. README spec

`crm/README.md` — для людей (Ruslan + agents) — как пользоваться:

1. **Что это** (1 параграф, цель)
2. **Quickstart** — `/crm-add`, `/crm-show`, `/crm-touch` (3 примера)
3. **Schema** — short ref + link на `_schema/frontmatter.yaml`
4. **Skills cheatsheet** — table 10 skills с одной строкой описания каждого
5. **Conventions** (slugs, dates, append-only, кто owns)
6. **Strategy hooks** — что это + как обновлять `strategy-hooks.yaml`
7. **Voice pipeline** — как item с `target: crm` попадает в CRM
8. **Backups** — git = backup
9. **Privacy notice** — repo private, sensitive поля (income, observations) — be mindful
10. **Phase 2 roadmap** — Notion sync / sqlite cache / agent suggestions

---

## §11. Acceptance criteria (что должно быть готово)

Перед AWAITING-APPROVAL packet — все pункты должны быть green:

- [ ] `crm/` skeleton создан (полный layout per §1)
- [ ] `_schema/frontmatter.yaml` + `_schema/roles.yaml` + `_schema/statuses.yaml` + `_schema/strategy-hooks.yaml` (initial 5+ offers, 5+ asks из текущей strategy)
- [ ] `_templates/person.md` + `_templates/org.md` (полные 14 секций per §3)
- [ ] `_scripts/crm.py` + `frontmatter.py` + `index_builder.py` + `dashboard.py` + `views.py` + `strategy_hooks.py` (все скрипты работают)
- [ ] `_scripts/voice_router.py` (basic version — DRAFT-only, no auto-write to production)
- [ ] 10 skills в `.claude/skills/` (`crm-add`, `-show`, `-list`, `-search`, `-touch`, `-update`, `-rebuild-index`, `-dash`, `-stuck`, `-weekly`)
- [ ] `README.md` написан
- [ ] Tests все green (`pytest crm/_tests/`)
- [ ] Sample fixtures committed (3-5 sample персон)
- [ ] `_example-person.md` в `crm/people/` (committed как reference)
- [ ] `index.md` regenerated и committed
- [ ] `crm/log.md` initialized
- [ ] Smoke test: `/crm-add Test Person` → `/crm-show test-person` → `/crm-touch test-person "test"` → `/crm-update test-person --status=warm` → `/crm-list status=warm` — всё работает
- [ ] Strategy hooks integration: при `/crm-add` префиллит §7-§8 минимум 1-2 suggestions
- [ ] Dashboard `/crm-dash` outputs полную картину
- [ ] Documentation в `crm/PLAN.md` — копия Notion-плана (для offline reference)
- [ ] Commit + push в working branch (`claude/jolly-margulis-915d34` — текущий main working) per single coherent commit (или max 3 logical commits)

---

## §12. AWAITING-APPROVAL packet structure

После завершения — бригадир пишет в `swarm/awaiting-approval/cycle-N-crm-build-2026-04-26.md`:

```markdown
---
cycle: N
date: 2026-04-26
type: crm-build
status: awaiting-approval
---

# Cycle N — CRM Build — AWAITING APPROVAL

## §0 TL;DR

CRM-система v1 готова. 10 skills работают. Tests green. README + PLAN written.
Smoke test passed. Ready для production usage.

## §1 What was built
[bullet list of files created + LOC + key choices]

## §2 What was decided autonomously (non-spec)
[если бригадир сделал какие-то judgment calls вне spec — list them с rationale]

## §3 What deviates from prompt
[если что-то не сделано или сделано иначе — explicit list]

## §4 Tests output
[pytest summary]

## §5 Demo
[curl/bash trace из smoke test]

## §6 Open questions for Ruslan
[если что-то всплыло что нужно decision]

## §7 Next cycle proposal
[что в cycle N+1: import existing contacts? voice integration deeper? Notion sync?]

## §8 Status

**RECOMMEND:** Ruslan ack → можно начинать production usage (заносить advisor candidates 26.04).

Brigadier: <agent-name>
Time spent: <X> мин
LOC: ~<N>
```

---

## §13. Anti-scope (НЕ делать в этом cycle)

- ❌ **Notion sync** — Phase 2. Не build sync скрипты сейчас.
- ❌ **Web UI** — никогда. CLI + Markdown only.
- ❌ **Sqlite cache** — Phase 2 (когда >1000 records). Сейчас just grep.
- ❌ **Encryption** — repo private = достаточно. Phase 2 если понадобится.
- ❌ **Multi-user permissioning** — single user.
- ❌ **Workflow automation** (auto-status-change after N days) — Phase 2.
- ❌ **Email integration** (auto-import от Gmail) — Phase 3.
- ❌ **AI auto-scoring of ICP** — Phase 2 после накопления 30+ scored examples.
- ❌ **Import existing contacts** — отдельный cycle (cycle 2). Не trying в cycle 1.
- ❌ **Strategy hooks для ВСЕХ existing decisions/** — Phase 1 = 5-7 hooks ручных. Auto-extraction Phase 2.

---

## §14. Notes for follow-up cycles

**Cycle 2 (после ack cycle 1):**
- Import existing contacts: Антон, Владислав, Родион + любые advisor candidates которые Ruslan уже нашёл из 26.04 search → manual `/crm-add` через CC
- Test pipeline на real data
- Найти edge-cases (ru-name slugs, missing fields, multi-role transitions)
- Refine strategy-hooks.yaml на основе real data

**Cycle 3:**
- Voice-pipeline integration deeper (item-routing, fuzzy matching tuning)
- `/crm-weekly` automation (запускать каждое воскресенье auto через cron)
- Add `/crm-resync-hooks` skill

**Cycle 4 (опционально):**
- Notion sync (push-only, view layer) — если Ruslan хочет mobile browse
- `/crm-sync-notion` skill

**Phase 2 backlog (не cycles):**
- Sqlite cache когда >1000 records
- AI ICP auto-scoring
- Email integration
- Mobile-friendly Notion view
- Public team access (если Jetix будет hire)

---

## §15. Технические детали launch

### Branch
Working branch: `claude/jolly-margulis-915d34` (current main working).

### Pre-launch checklist
```bash
ssh ruslan@100.99.156.28
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull
unset ANTHROPIC_API_KEY
ulimit -n 65535
```

### Launch
```bash
tmux new -ds crm-build-cycle-1
# inside tmux:
claude --dangerously-skip-permissions
# затем feed этот prompt полностью + добавить:
# "Ты — бригадир. Веди swarm cycle. После завершения — AWAITING-APPROVAL packet per §12. Не задавай clarifying questions если не БЛОКЕР — действуй per spec; решения вне spec — log в §2 packet'а."
# Ctrl+B, D
```

### Monitor
```bash
tmux attach -t crm-build-cycle-1
# Ctrl+B, D to detach
```

### Expected duration
1.5 - 3 hours (skeleton + 10 skills + tests + dashboard + README). Depends on swarm parallelism.

### Если бригадир застрял
Бригадир может задать **1 critical blocking question** в Daily Log Notion comment (page id `34d2496333bf81f88180f6bd22a859f2`). Иначе — действуй per spec.

---

**End of deep prompt. Бригадир: ты можешь начинать.**
