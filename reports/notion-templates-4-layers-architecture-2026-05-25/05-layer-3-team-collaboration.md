---
title: Phase 4 — Layer 3 Team Collaboration (multi-tenant overlay, full Notion spec, R12 AUTO-FIRE)
date: 2026-05-25
type: phase-report-layer-3-spec
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 4
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only + no-sample-data
language: russian primary
layer: 3
baseline: TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md
roy_auto_fire: [influence-ethics, recruitment-dynamics, nlp, propaganda, gamification]
---

# Phase 4 — 🔵 Layer 3 Team Collaboration: полная Notion-схема (multi-tenant)

> **Что в этой фазе.** Полный Notion-implementation-ready spec слоя совместной работы поверх
> личных систем. N Personal OS ↔ одно общее пространство. 10 ролей, биржа, Charter, 4 монетизации,
> ежедневный брифинг, Stage Gates, Steward-feed, матрица прав 10×10, онбординг недели, R12
> paired-frame STRICT (4 action classes), fork-and-leave с 30-дневным окном.
> Baseline: `TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md`. **R12 AUTO-FIRE** — это primary R12-surface.
> NO sample data.

---

## §1 Топология shared workspace (multi-tenant)

У каждого участника — **приватное** пространство (его Layer 1+2). Есть одно **общее**
(Teamspace). Наверх (личное → общее) — **только opt-in publish** по решению человека. Вниз
(общее → личное) — уведомления, @упоминания, ссылки (linked databases), **не копирование** чужих
данных.

**Используем родные возможности Notion** (минимум кода):
- **Teamspace** (Team/Business plan) — общее пространство.
- **Linked databases** — общая запись видна, но живёт у владельца.
- **Synced blocks** — Charter синхронизирован во все воркспейсы.
- **Page/DB permissions по роли** — права из матрицы §9.
- **Guest access** — внешние советники (3 уровня §10).
- **Comments + @mentions** — координация без правки.

**Красная линия (изоляция данных):** личный Daily Log / Hypotheses / Life Pulse / Finances
**никогда** не синкаются в команду без явного действия. Брифинг одного **не раскрывает**
приватные данные другого.

**10 общих баз Layer 3:** Project Catalog / Skills-Needs / Project Workspaces / Charter / Revenue
Accounting / Contribution Ledger / Decisions Queue / R12 Audit Log / Daily Brief / Onboarding-Guides.

---

## §2 База ролей (10 ролей DB) — full schema per role

**Назначение.** Когда люди работают над общим проектом, у каждого роль. Роль отвечает на 4
вопроса: что **делает** / что **видит и меняет** / как считается **вклад** / какую **долю**.
Плюс уровень **R12-риска** + встроенная защита. **IP-1: роль ≠ человек** — один человек может
быть PM в одном проекте и Contributor в другом (multi-hat).

**База Roles (definition library):**

| Поле | Тип | Назначение |
|---|---|---|
| Role name | Title | название роли |
| Scope | Select | per-project / cross-team |
| Produces | Text | что роль производит |
| Contribution metric | Text | как считается вклад |
| Default share | Text | дефолтная доля |
| R12 risk | Select | low / mid / high / meta |
| Built-in protection | Text | защита (ротация / cap / fork-leave) |
| Permission profile | Relation → permissions matrix | ссылка на права |
| Rotation? | Checkbox | ротируется ли |

**10 ролей (карточки ≥7 атрибутов):**

| # | Роль | Производит | Вклад | Доля | R12-риск | Защита |
|---|---|---|---|---|---|---|
| 1 | **PM (Управляющий)** | скорость + продвижение SG + всплытие блокеров | часы координации | 10-20%/проект | СРЕДНИЙ | ротация PM, «нет PM-на-всю-жизнь» |
| 2 | **Inv-Cap (Инвестор капитала)** | деньги на старт | сумма × срок | 20-40% капчасти | **ВЫСОКИЙ** | Mondragón 5:1 + fork-leave + 30-day + авто-этик-эксперт |
| 3 | **Inv-Time (Инвестор времени)** | часы + навык | часы × ставка (peer-validated) | трудовая часть | НИЗ-СРЕДН | потолок ≤50 ч/нед (анти-выгорание) |
| 4 | **Inv-Net (Инвестор сети)** | интро / аудитория | интро (число+цели) | 3-10% за интро | СРЕДНИЙ | анти-audience-extraction |
| 5 | **Contributor (Исполнитель)** | задачи | задачи × сложность × качество | почасовка/доля | НИЗКИЙ | самый частый вход |
| 6 | **Advisor (Советник)** | лёгкий совет 1-2ч/мес | сессии | 0.5-2%/ретейнер | НИЗКИЙ | советует≠управляет (анти scope-creep) |
| 7 | **Facilitator (Фасилитатор)** | ведёт сессии/когорту | сессии × фидбек | за сессию + бонус | СРЕДНИЙ | анти-культ + Schelling-чек |
| 8 | **Mentor (Наставник)** | долгосроч. сопровождение | 3-12 мес/менти | ретейнер | **ВЫСОКИЙ** | нет эксклюзивности/lock-in + потолок 12 мес |
| 9 | **Observer (Наблюдатель)** | смотрит, не участвует | — | — | НИЗКИЙ | безопасная прихожая |
| 10 | **Steward (Хранитель)** | ловит доение/запирание, останавливает ≤5с | надзор | плоский ретейнер (НЕ проектная) | МЕТА | ротация + peer-Steward проверка |

**Три инварианта здоровья:** (1) роль ≠ человек (IP-1); (2) высокий R12-риск → больше защиты
(Inv-Cap/Mentor); (3) власть ротируется (PM/Facilitator/Steward — «нет роли на всю жизнь»).

**R12 paired-frame (AUTO-FIRE influence-ethics + recruitment-dynamics):** роли Inv-Cap, Mentor,
Facilitator — это surfaces концентрации власти/контроля. Каждая несёт **defensive-counter**:
финансовый контроль ↔ Mondragón cap + fork-leave; власть наставника ↔ потолок 12 мес + согласие
менти на доступ; харизма фасилитатора ↔ ротация + анти-культ Schelling-чек. Steward = enforcement
cell, ловит нарушения.

---

## §3 Project Catalog DB (14 полей)

**Назначение.** Каталог: что делается, куда вписаться. **Язык R12 (nlp-expert lens):** НЕ «доска
вакансий», а «открытые роли / вписаться»; НЕ «вакансия», а «открытая роль»; НЕ «наняться», а
«вписаться». Рамка «дать/нужно» держит равенство сторон.

| # | Поле | Тип | Значения/формула |
|---|---|---|---|
| 1 | Title | Title | — |
| 2 | Type | Select | consulting / research / product / bets / cohort / community |
| 3 | Stage | Select | SG-1 / SG-2 / SG-3 / SG-4 |
| 4 | Status | Select | open / forming / active / paused / closed / archived |
| 5 | Project Manager | Relation → Members | один PM на проект |
| 6 | Active team | Relation → Members (multi) | — |
| 7 | Open roles needed | Multi-select | роли из §2 |
| 8 | Skills wanted | Multi-select | — |
| 9 | Monetization terms | Text | ссылка на шаблон §5 |
| 10 | **R12 audit status** | Select | passed / pending / failed |
| 11 | Time commitment | Text | ч/нед |
| 12 | Duration | Text | — |
| 13 | CTA join | Text | «вписаться» (не «наняться») |
| 14 | Description | Text | — |

**Views:** все открытые / по типу / по навыкам / по стадии (kanban SG) / новые 7д / мои проекты.

**Path нового проекта (Stage Gates lighter):** SG-1 propose (запись + open roles + черновик
R12-аудита) → PM определяется → команда формируется (matching уведомляет) → **Steward-гейт**
(R12 + Charter) → SG-2 active (revenue accounting) → SG-3 deliver (milestone + ре-аудит) → SG-4
promote/close (итог + ретро).

---

## §4 Skills/Needs marketplace DB (10 полей)

**Назначение.** «Что могу дать / что надо» + подбор пар. По строке на человека.

| # | Поле | Тип | Приватность |
|---|---|---|---|
| 1 | User | Relation → Members | — |
| 2 | Skills can offer | Multi-select | публично |
| 3 | Time availability (ч/нед) | Number | публично |
| 4 | Capital availability | Select (диапазон) | **можно скрыть** |
| 5 | Network value | Text | публично |
| 6 | Mentorship offered | Checkbox | публично |
| 7 | Skills needed | Multi-select | публично |
| 8 | Project interest | Relation → Catalog | публично |
| 9 | Monetization preference | Select | — |
| 10 | Active until (свежесть) | Date | авто-устаревание |

**Подбор пар (раз в день CC, DRAFT):** offer × Projects-wanted / needed × Users-offer / capital ×
Inv-Cap-открыто / network × Inv-Net / mentorship-offered × mentorship-needed → черновик в брифинг.

**Schelling-слой (gamification lens, R12 paired-frame):** мягкая подсветка точек схождения («3
человека тоже хотят навык X — можно собрать группу»). **Defensive-counter:** без насильной
группировки, без FOMO, без «успей вписаться». Координация ≠ принуждение.

**4 ловушки биржи:** витринные навыки / рамка «доска вакансий» / пере-матчинг (лимит 3-5) /
преждевременный пропуск R12-аудита.

---

## §5 Монетизация: 4 шаблона revenue share

**Главный принцип:** 75-90% человеку, 10-25% Foundation. Потолок неравенства Mondragón 5:1. Уйти
можно в любой момент с долей, без штрафа. 30 дней на выход при изменении правил. *(Точная
каноническая модель V10: каждый отдаёт 25% → институциональный пул, оставляет 75%; «75-90%» —
human-language обёртка.)*

**4 шаблона (как Notion templates в базе Monetization):**

| Шаблон | Кому | Split паттерн | Ключевая защита |
|---|---|---|---|
| **T1 Стандартный проект** | обычная команда | 75-90% контрибьюторам / 10-25% Foundation | 5:1 + fork-leave |
| **T2 С капитальным инвестором** | проект с Inv-Cap | + капчасть 20-40% | 5:1 капитал+труд + exit terms |
| **T3 Когортная программа** | мастерская ≈€1500/мес | ценность > €1500 | 5:1 между тирами + анти-культ |
| **T4 Вклад знанием/IP** | методолог-партнёр | ретейнер за фреймворк | анти-fork-prevention + open-ish лицензия |

**База Revenue Accounting:** Project / Total revenue / Foundation cut / Capital cut / Worker pool
/ Distribution status / Mondragón check (formula). **База Contribution Ledger:** Member / Project
/ Contribution units / Hours / Share % / Payout / прозрачно для участников проекта.

**Formula pattern (Mondragón 5:1):** `if(max(payouts)/min(payouts) > 5, "🛑 HALT", "✅ pass")` —
проверка **перед** распределением; нарушение → Steward HALT F4 ≤5с.

### ⚖️ 8-пунктовый R12-чек на КАЖДЫЙ денежный шаблон

Любой шаблон проходит чек **перед** применением (поля-чеклист в Charter / Monetization record):

1. Стоимость для получателя ≤ выгода
2. Предложение конкретно, не размыто
3. Запрос пропорционален глубине отношений
4. Уместно по стадии (не пушим деньги «новичку»)
5. Уместно по каналу
6. R12 paired-frame PASS (нет извлечения / lock-in / нарушения 5:1 / fork-prevention)
7. Анти-CTA (нет манипуляции / MLM / культа / нарушения порядка ступеней)
8. Halt-Log-Alert готов (≤5 сек при нарушении)

**Применение к 4 шаблонам (матрица):**

| Пункт | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| 1 Cost≤benefit | 75-90% человеку | 60-80% труду | ценность>€1500 | ретейнер за фреймворк |
| 4 По стадии | только SG-2+ | только SG-2+ | только step-5+ | при реальном вкладе |
| 6 R12 pass | 5:1 + fork-leave | 5:1 кап+труд | 5:1 между тирами | анти-fork-prevention |
| 7 Анти-CTA | нет MLM | нет lock-in | нет культа | нет IP-захвата |
| 8 Halt готов | Steward F4 | Steward F4 | Steward F4 | Steward F4 |

---

## §6 Charter DB (6 секций + R12 чек-лист fields)

**Назначение.** Договор команды. Реализуется как **synced block** (виден всем одинаково) +
запись в базе Charter с полями-чеклистами.

**6 обязательных секций:**
1. **Ценности** — на чём стоим.
2. **Управление** — принятие решений + разрешение споров + Stage Gates.
3. **Монетизация** — revenue split + **Mondragón 5:1 явно** + метод учёта + exit terms.
4. **R12-комплаенс (центральная)** — нет извлечения + fork-and-leave + 30-дневное окно +
   Mondragón STRICT + HALT при wage-ratio + запрет non-consensual distribution + запрет
   fork-prevention.
5. **Разрешение споров** — Steward → peer-Steward → внешний медиатор.
6. **Ethereum overlay** (опционально Phase 2+).

**R12 чек-лист fields (checkbox per Charter record):** `no_extraction` / `fork_and_leave_enabled`
/ `30day_window` / `mondragon_5to1_strict` / `halt_on_wage_ratio` / `no_nonconsensual_dist` /
`no_fork_prevention`. Все должны быть ✅ перед SG-2.

---

## §7 Daily CC pass per user (5 секций брифинга)

**Назначение.** Раз в день Claude Code за каждого делает обход: читает личное + командное +
(опц.) интернет → персональная подборка. **Всегда черновик** — CC ничего не делает за человека
(перенос дисциплины голосового ввода).

**База Daily Brief (по строке на user×день):**

| Поле | Тип |
|---|---|
| User | Relation → Members |
| Date | Date |
| Intros (3-5) | Text (draft) |
| Skill gaps (2-3) | Text |
| Marketplace finds (3-5) | Text |
| New projects (1-3) | Text |
| Internet finds (1-3, opt-in) | Text |
| Action checklist | Checkbox-list (draft) |
| Reviewed? | Checkbox |

**5 секций (~300-500 слов):** 🤝 3-5 знакомств / 🎯 2-3 пробела в навыках / 🔄 3-5 находок на
бирже / 🚀 1-3 новых проекта / 📖 1-3 из интернета + чек-лист действий.

**CC читает 4 источника:** личная система (топ-5 проектов/гипотез, skills, цели, пульс) +
командное (роли, решения, биржа) + общее (новые проекты 7д) + интернет (opt-in RSS/arxiv/поиск).

**DRAFT-only железно (R12 + gamification anti-pattern):** CC не пишет сообщения, не записывает в
проекты, не меняет навыки, не отправляет наружу. Лимит 3-5 на секцию (анти пере-матчинг, анти
FOMO). Приватность: нет cross-user утечки. Каденс: 1×/день + недельный дайджест (опц.) + opt-out.

---

## §8 Stage Gates dashboard + Steward escalation feed

**Stage Gates dashboard** — вид Project Catalog kanban по Stage (SG-1→SG-4) + поля predicate
(что должно быть истинно для перехода). SG-2 переход требует Steward-гейт PASS (R12 + Charter).

**Steward escalation feed (база R12 Audit Log):**

| Поле | Тип |
|---|---|
| Trigger | Select (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt) |
| Project / Member | Relation |
| Severity | Select (F2 / F4 / F8) |
| Detected | Date+time |
| Action taken | Text (HALT / review / resolved) |
| Resolution | Text |
| Status | Select (open / halted / resolved) |

**4 RUSLAN-LAYER action classes (детекторы жадности и принуждения):**
- `extraction_beyond_share` — забрать сверх договорённого → HALT
- `wage_ratio_violation` — сделать одного в >5× богаче → HALT (проверка перед распределением)
- `non_consensual_distribution` — опубликовать чужое без согласия → HALT
- `fork_prevention_attempt` — язык «теперь не уйдёшь» → HALT

---

## §9 Permissions matrix 10 баз × 10 ролей

Значения: **EDIT** / **COMMENT** / **VIEW** / **VOTE** / **OVERSIGHT** / **NONE** / «(own)» = только своё.

| База \ Роль | PM | Inv-Cap | Inv-Time | Inv-Net | Contrib | Advisor | Facilit | Mentor | Observ | Steward |
|---|---|---|---|---|---|---|---|---|---|---|
| Project Catalog | EDIT(own) | V+C | V+C | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | EDIT |
| Skills/Needs | EDIT(own) | EDIT(own) | EDIT(own) | EDIT(own) | EDIT(own) | EDIT(own) | EDIT(own) | EDIT(own) | VIEW | VIEW |
| Project Workspaces | EDIT(own) | VIEW | EDIT(asgn) | VIEW | EDIT(asgn) | COMMENT | EDIT(sess) | COMMENT | VIEW | VIEW |
| Charter | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | EDIT |
| Revenue Accounting | EDIT(own) | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | NONE | NONE | NONE | NONE | OVERSIGHT |
| Contribution Ledger | EDIT(own) | VIEW(own) | EDIT(own) | VIEW(own) | EDIT(own) | VIEW(own) | EDIT(own) | VIEW(own) | NONE | OVERSIGHT |
| Decisions Queue | EDIT(own) | VOTE | VOTE | VOTE | COMMENT | COMMENT | COMMENT | COMMENT | NONE | OVERSIGHT |
| R12 Audit Log | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | VIEW(own) | NONE | EDIT |
| Daily Brief | own | own | own | own | own | own | own | own | own | own |
| Onboarding/Guides | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | VIEW | EDIT |

**Три правила чтения:** (1) PM силён только в СВОЁМ проекте (hub-and-spoke per-project); (2) деньги
видны только свои (полная картина — только Steward OVERSIGHT); (3) Steward — единственная сквозная
роль, но не голосует в проектах и не берёт проектную долю (анти конфликт интересов).

---

## §10 Внешние люди — 3 уровня (Part 10 external touchpoints)

- **Guest** — read-only витрина, отзывается в 1 клик.
- **Observer** — роль-член, пред-онбординг.
- **Steward audit** — надзор за R12, без личных данных.

Любая внешняя запись требует **зафиксированного согласия** — нет согласия → стоп.

---

## §11 Cross-Personal-OS sync mechanics (opt-in shares)

- **Наверх (личное → общее):** только opt-in publish (человек выбирает, что показать).
- **Вниз (общее → личное):** уведомления + ссылки, не копирование.
- **4 helper-скрипта (спека R11, не код):** `team_os_sync.py` (двусторонний синк по frontmatter) /
  `team_os_invite.py` (онбординг + права) / `team_os_marketplace_match.py` (подбор) /
  `team_os_daily_brief.py` (брифинг). Config-driven, идемпотентные, ключи в `private/`.
- **Конфликт версий:** личное → личный файл главнее; общее → общее пространство; спорное →
  `pending-review`, Steward смотрит. **Табу — молчаливая авто-перезапись.**

(Детальная механика — Phase 8 cross-layer sync.)

---

## §12 Onboarding 1-week sequence (анти-секта)

**Главная рамка: когорта, а не секта.** Выход называется вслух **сразу**, до подписи.

| День | Что | Время |
|---|---|---|
| 1 | Personal OS bootstrap (своя система) | 2ч |
| 2 | тур командного пространства | 1.5ч |
| 3 | тень проекта (без обязательств) | 1-2ч |
| 4 | биржа offer/need | 1ч |
| 5 | первый brief review | 30мин |
| 6 | Charter + R12 ethics doc (чтение «как мы защищаем тебя») | 1-2ч |
| 7 | первый маленький вклад | — |

**Ритуалы перехода (вехи, не экзамены):** Observer→Contributor (неделя тени + первая задача) /
Contributor→PM (3 мес + Steward review) / Contributor→Investor (формальное обязательство + поправка
Charter) / Mentor→Steward (12 мес + peer-номинация + R12-аудит).

**R12 ethics doc (9 секций, ~1500 слов, тон «как мы защищаем тебя»):** что делаем / чего НЕ делаем
/ fork-and-leave / Mondragón 5:1 / Charter / роль Steward + как поднять тревогу / разрешение споров
/ красные флаги / **твои права** (уйти / усомниться / возразить / форкнуть).

**Анти-секта (recruitment-dynamics + propaganda lens, defensive):** ❌ клятвы верности на входе /
❌ эскалация преданности («докажи, что свой») / ❌ спаситель-фигура / ❌ «мы против них» / ❌ не
упомянут выход. Каждый — это known cult-formation pattern; защита = их явное отсутствие.

---

## §13 Fork-and-leave button (literal — 30-day notice + asset retrieval)

**Реализация в Notion:** кнопка/процедура «Уйти из когорты» (страница в Onboarding-Guides):

1. **Объявление выхода** — запись в Decisions Queue (тип `fork-and-leave`), дата.
2. **30-дневное окно** — при изменении Charter; для добровольного выхода — немедленно.
3. **Asset retrieval** — экспорт своих данных: Personal OS остаётся полностью (приватный
   воркспейс не трогается); своя строка Contribution Ledger + накопленная доля выгружаются.
4. **Доля без штрафа** — proportional treasury share (R12: «без penalty»).
5. **Не-punitive язык** — никакого «ты предал»; запись нейтральна.

**R12 (influence-ethics enforcement):** любая попытка `fork_prevention_attempt` (язык «теперь не
уйдёшь», удержание данных, штраф за выход) → HALT F4 ≤5с + Steward + лог.

---

## §14 Constitutional posture Phase 4 (R12 AUTO-FIRE)

- **R1 surface only** — число ролей (7/10), Mondragón (5:1 strict/гибко), Charter (обяз/опц),
  первая когорта (5/10) = решения Ruslan (см. Team OS §12 + main §11).
- **R12 paired-frame STRICT** — каждая роль высокого риска + биржа + монетизация + онбординг несут
  defensive-counter + abuse-flag. AUTO-FIRE: influence-ethics (enforcement), recruitment-dynamics
  (анти-секта онбординг), nlp (язык биржи «дать/нужно»), propaganda (анти «мы против них»),
  gamification (Schelling без FOMO).
- **IP-1 STRICT** — 10 ролей абстрактны; Maxim/Прапион/Цэрэн = примеры применения.
- **R6** — наследует Team OS Plan §3-§8 + Economic V10 (75/25, Mondragón) + R12 LOCK 2026-05-12.
- **R11** — 4 helper-скрипта = спека; Notion API не зовётся.
- **No sample data** — суммы €10K в примере деления = иллюстративный one-liner (см. main), не запись.

---

*Phase 4 closure. Layer 3 Team Collaboration = 10 общих баз, 10 ролей, биржа, Charter 6 секций,
4 монетизации с 8-пунктовым R12-чеком, Daily Brief 5 секций DRAFT-only, Stage Gates, Steward feed,
матрица прав 10×10, онбординг 7 дней анти-секта, fork-and-leave 30-day. R12 AUTO-FIRE применён.
Дальше Phase 5 — ⭐ Layer 4 Universal Business Foundation (центральная, ≥7-8K).*
