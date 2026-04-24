---
title: "§10 Secure Network Architecture — Layer 6 Community Deep-Dive"
type: integrated-synthesis
produced_by: engineering-expert
mode: integrator
cell: C-10
section: "§10"
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
confidence: high
confidence_method: schema-coverage
provenance_inline: true
word_count_estimate: 2400
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.4 binding — Telegram primary; §4 risk 7 Дуров"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md", range: "§2.3 Secure Network; §2.4 Цифровые портреты; §2.5 Fork-community"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D27 Fork-and-merge; D25 Company-as-code"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 Secure Network Phase-2+; §10 anti-LinkedIn positioning"}
anti_scope:
  - "NO §6 Matchmaker mechanics — matchmaker cell uses portraits as input but the routing mechanism is sibling cell's scope"
  - "NO §5 Alliance governance detail — sibling cell handles legal structure options"
  - "NO §11 Evolution per gate — sibling cell handles full gate-by-gate projection; Phase-1/2/3+ tags used here only for context"
  - "NO implementation code or SDK call signatures — description only per intake §2 anti-scope"
  - "NO Notion writes; NO provider-key env-var literals; NO Task() invocation strings"
escalations: []
dissents:
  - source_cell: "engineering × integrator (self-dissent)"
    claim: "Telegram-as-primary carries structural third-party platform risk — Jetix does not control Bot API ToS, data residency policy, or API versioning cadence; the community's operational continuity is hostage to Telegram's policy decisions"
    F: F4
    ClaimScope: "holds for all phases where Telegram is the primary hosting substrate; partially mitigated at Phase-3+ if own-platform is operational; NOT mitigated by D27 fork-and-merge which covers methodology not infrastructure"
    R:
      refuted_if: "Telegram demonstrates API-stable + ToS-stable history ≥5 years with zero community-disruptive changes (evidence: review Telegram Bot API changelog 2018-2024)"
      accepted_if: "Jetix community architect explicitly acknowledges the dependency risk and locks a migration-readiness escape hatch (member export format + migration drill) before Phase-2 Secure Network launch"
  - source_cell: "engineering × integrator (self-dissent)"
    claim: "Clean-room migration cost from Telegram to an own platform is non-trivial — member data (portraits, chat history, connection graph) stored in Telegram's infrastructure cannot be bulk-exported via Bot API; migration requires active member re-enrollment"
    F: F5
    ClaimScope: "holds for any Telegram-hosted community; Telegram Bot API (as of knowledge cutoff) does not expose chat history export endpoints for bots; member-generated content in group chats is not accessible to bots retroactively"
    R:
      refuted_if: "Telegram extends Bot API with a community data export endpoint before Phase-2 launch"
      accepted_if: "migration design separates portrait data (stored in Jetix EU KB, mirrored from Telegram intake) from conversational data (Telegram-native, acknowledged as non-migratable); migration cost is then limited to re-enrollment UX, not data loss"
---

# §10 Secure Network Architecture

## §10.1 Архитектура на базе Telegram — основной субстрат

Secure Network в Phase-1 строится на **официальном Telegram Bot API** без использования кастомных протоколов или нестандартных клиентских fork'ов. Выбор мотивирован тремя факторами из intake §6.4: (a) audio_524 прямо называет Telegram как основу, (b) Phase-1 не требует сложной инфраструктуры — 5-20 членов не оправдывают инвестиции в собственную платформу, (c) Telegram обеспечивает приемлемую модель безопасности (E2E для секретных чатов, transport encryption для групп) без дополнительных затрат на инфраструктуру. [src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md#§6.4]

**Claim 1:**
- Claim: Telegram Bot API — достаточный субстрат для Phase-1 Secure Network с ≤20 членами и не требует кастомного протокольного слоя
- F: F4 (операциональная конвенция — common practice для invite-only professional communities на Telegram)
- ClaimScope: holds для Phase-1 (≤20 членов); NOT sufficient для Phase-2 (≥200 членов) без дополнительного инструментального слоя поверх Bot API
- R: {refuted_if: "первые 20 членов сообщают о критических UX-проблемах специфичных для Telegram (не для Jetix контента)", accepted_if: "Phase-1 чат функционирует без операционных инцидентов на протяжении первых 3 месяцев"}

### Структура каналов

**Phase-1 (≤20 членов, €0–€50K):**
Единый инвайт-only чат. Нет разделения на субканалы — при такой численности тематическая сегментация создаёт больше фрикции, чем пользы. Руслан — единственный модератор. Инвайты выдаются вручную.

**Phase-2+ (≤200 членов, €50K–€1M):**
Переход к структурированной экосистеме каналов:
- **Announcements channel** — только чтение для членов, пишет администрация. Протокольные объявления, изменения правил, новые инициативы. Входной/выходной интерфейс для новостей.
- **General lounge** — общее пространство для всех членов. Кросс-архетипный диалог. Не тематически ограничен, но модерируется по тональности (D22 — adequate + upward-direction).
- **Тематические субканалы per archetype** — по одному субканалу на каждый из 11 архетипов (предприниматели, ресёрчеры, инженеры, инвесторы, политики, продавцы, менеджеры, философы, разработчики идей, разработчики жизни, блогеры). Каждый субканал имеет собственного модератора из числа Alliance-членов.
- **Private DM канал matchmaker** — бот-ассистент для приватных match-запросов. Член отправляет структурированный запрос боту (задача + требуемые навыки + бюджет + сроки); бот проверяет по цифровым портретам (Phase-2+) и формирует shortlist. Детали механики matchmaker — в §6 (sibling cell; вне scope данного раздела).
- **Waitlist/onboarding channel** — временный канал для новых членов до прохождения portrait-intake.

**Phase-3+ (≥200 членов, €1M+):**
Структурная шардинг-необходимость. При превышении ~200 активных членов в одном Telegram-пространстве начинается degradation качества сигнала. Механика:
- Каждый архетипный субканал может стать самостоятельным invite-only чатом со своим Telegram-ботом
- Общий general lounge сохраняется как inter-shard пространство
- Announcements остаётся единым для всего Secure Network (broadcast-модель)
- На Phase-3+ рассматривается переход с Telegram-субстрата на собственную платформу (§10.7)

[src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§2.3]

### Invite-flow и ролевые разрешения

**Invite-flow:**
1. Руслан генерирует one-time invite token через Telegram-бота (Phase-1: вручную через стандартный invite link с ограничением по времени или числу использований; Phase-2+: бот генерирует уникальные токены per-member по команде администратора).
2. Новый член активирует токен — попадает в onboarding channel.
3. Бот запускает welcome flow: приветствие + краткое описание правил + запрос на заполнение portrait-intake (§10.2).
4. После завершения portrait-intake (или промежуточной версии для Phase-1) член получает полный доступ к разрешённым каналам для его роли.
5. В Phase-2+ — дополнительная проверка: член-поручитель (vouching mechanism §10.4) подтверждает нового кандидата прежде чем токен выдаётся.

**Ролевая матрица разрешений:**

| Роль | General lounge | Archetype sub-channel | Announcements | DM-matchmaker | Управление ботом |
|---|---|---|---|---|---|
| **Owner (Руслан)** | R/W | R/W (все) | R/W | R/W | Full admin |
| **Moderator** | R/W | R/W (свой архетип) | R | R/W | Limited (кик, мут, варн) |
| **Member** | R/W | R/W (своего архетипа + general) | R | R/W (запросы) | — |
| **Observer** | R (только general lounge) | — | R | — | — |

Observer-роль — временная: максимум 2 недели для новых членов до завершения portrait-intake, или постоянная для специальных гостей без Alliance-коммитмента (решение per-case Русланом).

**Инженерные контракты бота (input/output/error):**
- **Input:** Telegram Update object (message, callback_query, new_chat_member)
- **Output:** sendMessage / sendDocument / restrictChatMember API calls
- **Error handling:** при недоступности Telegram Bot API — бот логирует ошибку в Jetix KB (append-only event log), уведомляет администратора через fallback канал (direct message Руслану), не теряет pending actions (retry queue)
- **Failure mode — бот недоступен:** члены по-прежнему видят чат и общаются; только автоматические функции (invite validation, portrait-flow) деградируют. Критичность: medium (не блокирует базовое общение, блокирует онбординг новых членов)

---

## §10.2 Цифровые портреты — схема, intake и приватность

Цифровой портрет — machine-readable структурированная карточка каждого Alliance-члена. Без портретов matchmaker остаётся «в голове Руслана»; с портретами — становится scalable и передаётся агентам L4. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§2.4]

**Claim 2:**
- Claim: Цифровой портрет как machine-readable YAML-запись в Jetix KB — необходимое условие для Phase-2+ scalable matchmaking; Phase-1 может функционировать без них
- F: F4 (операциональная конвенция — следует из audio_524 и L8 §2.4)
- ClaimScope: holds для Jetix Phase-A и Phase-B; масштабируется до Phase-3+ при добавлении полей (contribution-graph, trust-scores)
- R: {refuted_if: "Phase-1 matchmaking volume превышает ~10 connections/week при отсутствии портретов (manually breaks)", accepted_if: "первые 10 Alliance-членов заполняют portrait-intake в течение первого месяца Phase-2+ без операционных инцидентов"}

### Схема портрета (YAML)

```yaml
# Digital Portrait Schema — Jetix Secure Network
# Phase-1: поля name, archetype, location, languages, skills, available_hours_per_week, open_needs обязательны
# Phase-2+: все поля обязательны
# Phase-3+: расширение полями contribution_graph, trust_score (TBD governance)

portrait:
  id: "<member-slug>"                          # уникальный kebab-case идентификатор
  name: "<публичное имя>"                      # может быть псевдоним по желанию члена
  archetype:                                   # 1+ из 11 (JETIX-VISION §7.1)
    - предприниматель
    # - ресёрчер | инженер | инвестор | политик | продавец | менеджер | философ | разработчик-идей | разработчик-жизни | блогер
  location:
    city: "<город>"
    country: "<страна>"
    timezone: "UTC+N"
  languages:
    - code: "ru"
      level: native
    - code: "en"
      level: professional
  skills:                                      # структурированные теги, не prose
    - domain: "AI-implementation"
      proficiency: expert                      # beginner | intermediate | advanced | expert
    - domain: "B2B-sales"
      proficiency: advanced
  available_hours_per_week: 5                  # минимальный Alliance commitment; в часах
  current_focus: "<одна фраза — над чем работаю сейчас>"
  past_roy_contributions:                      # linked deliverables, заполняется с Phase-2+
    - deliverable_path: "swarm/wiki/..."
      date: "YYYY-MM-DD"
      description: "<одна строка>"
  open_needs:                                  # чего ищу в Alliance
    - "Партнёр с экспертизой в DACH Mittelstand sales"
    - "Ревьюер для методологического документа"
  contact_preferences:
    preferred_channel: telegram                # telegram | email | video-call
    response_time_sla: "24-48h"               # ожидаемое время ответа
    public_visibility: members_only            # members_only | alliance_only | public (не реализуется Phase-1)
  gdpr:
    consent_given_at: "YYYY-MM-DDTHH:MM:SSZ"
    data_deletion_requested: false
    last_updated: "YYYY-MM-DD"
```

### Portrait intake — как создаётся

**Phase-1 (бот-форма):** Telegram-бот задаёт серию структурированных вопросов в conversational режиме при onboarding. Вопросы охватывают обязательные поля схемы. Ответы записываются в Jetix KB как YAML-файл под `clients/<member-slug>/portrait.yaml` (или `community/<member-slug>/portrait.yaml` — конкретный путь TBD при имплементации). Опциональный апдейт: член может запросить `@JetixBot update portrait` в любое время.

**Phase-2+ (web-форма + опциональное интервью):** Форма на сайте Jetix (15-20 полей, conditional logic — инженерам показываются tech-поля, блогерам — аудитория-поля). 15-минутное структурированное интервью с Русланом или Alliance-модератором опционально для оценки D22 qualitative fit.

**Failure mode — member теряет доступ к Telegram:** Portrait хранится в Jetix EU KB (не в Telegram). Member может запросить восстановление через email-fallback. Это ключевой escape hatch против platform lock-in (см. §10.1 dissent).

### Приватность и GDPR

Секция напрямую затрагивает GDPR Art. 13/14 — информирование субъектов данных при сборе.

**Что собирается:** имя (может быть псевдоним), местоположение (город/страна), языки, навыки, доступные часы, текущий фокус, прошлые контрибуции, открытые потребности, предпочтения по контакту.

**Зачем:** matchmaking между Alliance-членами; routing задач к специалистам; компилирование community intelligence без centralizing individual conversations.

**Как долго хранится:** до момента удаления портрета по запросу члена + 30 дней на backup-purge. Нет retention beyond membership.

**Кто видит:** только другие члены Secure Network (members_only по умолчанию). Не индексируется в публичных поисковиках. Не передаётся третьим лицам. Jetix-внутренний matchmaker L4 агент обрабатывает данные for routing, не для ML-training (нет обучения на пользовательских данных).

**Право на удаление:** member может запросить удаление портрета через `@JetixBot delete my portrait` (Phase-1) или через web-форму (Phase-2+). Выполнение в течение 72 часов. Удаление portrait не удаляет Telegram account — это member's собственный аккаунт.

**Резидентность данных:** Telegram хранит чат-данные на серверах Telegram (EU или non-EU в зависимости от настроек Telegram; уточнить при Phase-2 GDPR audit). Portrait YAML-файлы зеркалятся в Jetix EU KB — GDPR-compliant infrastructure. Критически: при GDPR data-deletion request portrait из Jetix KB удаляется целиком; conversational data в Telegram-чатах технически вне прямого контроля Jetix (Telegram-side deletion требует обращения к Telegram через официальный канал Privacy Policy запросов).

[src:decisions/JETIX-VISION.md#§5 "Secure Network quality-gated"]

---

## §10.3 Модель модерации

**Phase-1 (≤20 членов):** Руслан модерирует всё самостоятельно. Единственный модератор, полные полномочия. Scalability: приемлемо при численности ≤20 активных членов и низкой частоте инцидентов (invite-only сильно снижает spam/trolling baseline).

**Phase-2 (≤200 членов):** 1-2 trusted Alliance-члена назначаются co-модераторами. Отбор критерии: ≥3 месяца в сообществе, verified D22 qualitative fit (stable + adequate), активность ≥5h/week, отсутствие prior moderation incidents. Компенсация — Phase-2+ Alliance benefits (tool-sharing складчина, приоритетный matchmaking доступ); денежная компенсация деферирована до D26 team hire trajectory.

**Phase-3+ (≥200 членов, субканалы по архетипам):** Распределённая модерация. Один модератор на каждый архетипный субканал (11 субканалов = 11 потенциальных модераторов). Модераторы субканалов не имеют cross-channel полномочий — их scope ограничен собственным архетипным каналом.

**Эскалационный путь:**
1. Member флагирует сообщение (Telegram report / команда боту `@JetixBot flag <message_id> <reason>`)
2. Mod-review: модератор субканала (или Руслан в Phase-1) рассматривает в течение 24h
3. Owner-decision: финальное решение за Русланом в течение 48h SLA (Phase-2+)
4. Действия: предупреждение / временный мут / кик из канала / бан из Secure Network

**Covered topics:**
- Spam (повторяющиеся сообщения, рекламные вставки без разрешения, off-topic flood)
- Harassment (personal attacks, публичные обвинения без доказательств)
- Off-topic (не matching archetype канала или general lounge тональности)
- IP / NDA violations (публикация конфиденциальных материалов, нарушение форк-условий)
- Fork-community governance disputes (разногласия по merge-back принятиям — эскалируются напрямую к Руслану, не к субканальному модератору)

---

## §10.4 Предотвращение спама

**Phase-1 — нулевой вектор cold-spam:** Invite-only модель исключает возможность cold-spam по определению. Нет public registration, нет open join link, нет discoverability через Telegram search. Единственный вектор входа — персональный invite token от Руслана.

**Phase-2+ — многоуровневая защита:**

**Portrait-required gate:** Без завершённого portrait-intake новый член остаётся в Observer роли с Read-only доступом к general lounge. Нет возможности публиковать сообщения до верификации. Это уничтожает типичную spam-модель (создать аккаунт → начать рассылку).

**Waitlist + member-vouching:** Phase-2+ кандидаты попадают в waitlist. Один действующий Alliance-член (с Member ролью ≥3 месяца) должен поручиться за кандидата (vouching). Voucher несёт репутационную ответственность: если поручённый член получает бан за грубые нарушения в первые 90 дней — voucher получает предупреждение и временное лишение vouching-права.

**Rate limits на DM от новых членов:** В первые 30 дней после онбординга новый Member ограничен в частоте DM-инициаций через matchmaker-бот (Phase-2+): не более 3 match-запросов в неделю. Ограничение снимается после 30 дней или после первого успешного verified match (зафиксированного в portrait как past_roy_contribution).

**Bot detection:** Стандартные сигналы: аккаунт создан <24h до попытки входа в Secure Network, отсутствие верифицированного phone number (Telegram требует), паттерны активности совпадающие с known bot fingerprints (сообщения каждые N минут без вариации). Флагирование автоматическое, кик — manual (Owner/Mod решение).

**Reputation layer:** Каждый модераторский flag против члена записывается в portrait-метаданные (поле не публичное, visible только Owner/Mod). Накопление: 2 предупреждения → временный мут (7 дней); 3 предупреждения → review кандидата на исключение; 1 ban-worthy incident → немедленный кик + блокировка. Score не показывается члену публично — исключает gamification/gaming репутационной системы.

---

## §10.5 Fork-community governance согласно D27

D27 (ACKED Ruslan 2026-04-24): *«Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя, а лучшие мутации возвращать в основную ветку»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]

**Claim 3:**
- Claim: D27 fork-and-merge применён к методологии Jetix, не к инфраструктуре Secure Network; форки методологии живут в member namespaces независимо от Telegram-субстрата
- F: F5 (кодифицировано в D27, ACKED Ruslan 2026-04-24; применяется к SYSTEM-OVERVIEW downstream)
- ClaimScope: holds для Phase-2+ (D27 timing: открытие механики при €200K validation); NOT applicable в Phase-1 (механика не запущена)
- R: {refuted_if: "D27 downstream decisions (merge-back protocol, IP licensing) решены иначе и меняют scope применения", accepted_if: "первый PR-style merge-back contribution от Alliance-члена принят в upstream без конфликта с существующим core"}

### Конкретный stub merge-back протокола

**Canonical upstream:** `github.com/jetix/methodology` (спекулятивный путь — финальное расположение repo TBD post-Phase-2; D25 Company-as-code обязывает к git-native approach). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

**Шаги форка:**
1. **Fork:** любой Alliance-член с Member ролью ≥3 месяца (Phase-2+ unlock) форкает methodology repo в свой personal/org namespace на GitHub. Форк — это адаптация под свою нишу, свою вертикаль, свои процессы.
2. **Adapt:** форк живёт в namespace участника. Member тегирует изменения с явным context-тегом: `adaptation/niche:<archetype>`, `adaptation/vertical:<industry>`, `adaptation/locale:<country>`. Тег помогает upstream maintainer понять где мутация применима.
3. **Tag for merge-back:** Member создаёт специальный `MERGE-BACK.md` файл в корне форка с: описанием мутации (≤500 слов), контекстом где она протестирована (сколько членов/клиентов, период), ожидаемым импактом для canonical upstream.
4. **PR submission:** Member открывает PR в canonical upstream. Шаблон PR включает: summary, context (где применялось), quality evidence (результаты, метрики или qualitative description), requested-reviewer (если Member знает кого тегировать).
5. **Maintainer review:** Phase-1 — Руслан единственный maintainer (BDFL модель). Phase-3+ — committee формируется из Alliance-членов с ≥12 месяцев в сети и ≥3 успешными merge-back контрибуциями. Review checklist: (a) не противоречит D1-D28 locks; (b) проходит Jetix integration tests (автоматическая проверка, TBD implementation); (c) ≥1 maintainer +1 голос (Phase-1: Руслан; Phase-3+: ≥2 committee members).
6. **License compliance:** открытый вопрос — MIT / proprietary / dual-license (flag для §12 open questions; per intake §1 acceptance predicate пункт 6 "backup options brief, not deep"). D13 Closed core / Open surface применяется: core методологии остаётся closed, surface (frameworks, templates, guides) может быть открыта для fork-and-merge. Конкретное лицензионное решение — downstream D27 pending, не D27 itself.

**Governance model decisions (deferred per D27 §Downstream-decisions-pending):**
- **BDFL Phase-1:** Руслан — единственный maintainer upstream. Все merge-back PR через него.
- **Committee Phase-3+:** при достижении ≥10 Alliance-членов с ≥3 merged contributions каждый — рассматривается переход к committee governance (advisory или decision-making — TBD по решению Руслана). D27 фиксирует архитектурный принцип; governance детали не решены.
- **Timing:** открытие fork-community механики — Phase-2+ (post €200K validation), или при первых 10 Alliance-членах — открытый вопрос per D27.

**Инженерные failure modes fork-community:**
- **PR flood без качества:** rate-limit на PR submissions (не более 2 PR/member/month Phase-2+) предотвращает спам в upstream. Review SLA: maintainer рассматривает в течение 14 дней или явно defer/reject с комментарием.
- **IP conflict:** если форк содержит material из третьих лиц (не Jetix-authorized) — PR автоматически помечается флагом, требует дополнительной IP-review. Rejection без обсуждения при явных third-party IP conflicts.
- **Fork-drift (форк далеко ушёл от upstream):** merge conflict resolution — ответственность submitter'а (не upstream). Upstream не обязан помогать с rebase.
- **Governance dispute по merge-back принятию:** эскалирует к Owner (Русану) — финальное слово за ним в Phase-1 и Phase-3+. Сообщество не голосует по отдельным PR — это не democracy, это BDFL Phase-1 / curated-committee Phase-3+.

[src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§2.5]

---

## §10.6 Интеграция — Telegram и Дуров

Контакт с Дуровым = **"potential future contact, NOT assumed"** per intake §6.4 binding. [src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md#§4 risk-7]

Из audio_524: *«связаться с Дуровым для интеграции Telegram в концепцию Jetix-сообщества»* — это было записано как aspirational note, не как активная задача с дедлайном. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§7 audio_524]

**Default план (Phase-1 и Phase-2):** стандартный Telegram Bot API. Никакого специального доступа не требуется. Все функции, описанные в §10.1-§10.5, реализуются через публично доступный Bot API без каких-либо партнёрских соглашений с Telegram.

**Aspirational Phase-2+ low-priority initiative:** если outreach к Дурову состоится и будет успешным — возможны варианты углублённой интеграции: кастомные bot API extensions (например, верифицированный Jetix-badge для аккаунтов членов), sponsored visibility в Telegram ecosystem (каналы в рекомендациях), или ecosystem партнёрство в рамках Telegram Stars / TON экосистемы. Ни одна из этих возможностей не закладывается в Phase-1 или Phase-2 архитектуру как зависимость — все они опциональные upside.

Инженерная позиция: архитектура Secure Network должна функционировать полностью на стандартном Bot API. Любые Дуров-specific extensions — additive опции, не critical path.

---

## §10.7 Backup options — краткий обзор

### Discord

Discord предлагает богатую модель разрешений (roles + channel permissions + категории + threads), встроенный voice/video, threading для асинхронных обсуждений и webhook-интеграции. С инженерной точки зрения Discord's API более зрелый для community-management, чем Telegram Bot API: более детальные permission scopes, audit log, bulk export возможности.

Однако Discord несёт культурный friction с целевым ICP Jetix. В DACH Mittelstand и среди европейских предпринимателей/инвесторов Discord устойчиво ассоциируется с gaming-community и молодёжными tech-проектами. Telegram в этой аудитории воспринимается нейтрально или профессионально. Введение Discord как основного субстрата создало бы onboarding-барьер ("ещё одна платформа + gaming-коннотация") у именно тех ICP-сегментов (предприниматели, инвесторы, политики), которые составляют核心 Alliance.

**Contingency:** Discord рассматривается только если (a) Telegram заблокирован регулятором в целевой географии, или (b) численность сообщества превысит возможности Telegram-шардинга и Phase-3+ own-platform ещё не готова.

### Собственная платформа

Собственная платформа даёт полный data ownership, кастомные features (contribution-graph visualization, AI-powered portrait matching, token economy D23), отсутствие third-party ToS рисков и полный GDPR compliance stack без зависимости от Telegram's privacy policies.

Барьеры значительны: build burden (минимальный MVP — несколько месяцев разработки + DevOps), member friction ("ещё один логин"), необходимость критической массы до запуска (chicken-and-egg: platform без членов не привлекает членов). По D15 revenue-gated unlocks — собственная платформа разблокируется при Phase-3+ ($1M+ milestone, D19 scale frame). До этой точки Telegram-субстрат остаётся операционально достаточным при правильно спроектированном portrait-layer в Jetix KB (что защищает от data lock-in — см. §10.1 dissent).

Ключевой инженерный принцип для подготовки к own-platform переходу: **portrait data и community intelligence хранятся в Jetix KB, не в Telegram**. Telegram — transport-layer, не data-store. Это делает потенциальную миграцию операцией re-enrollment (приглашение членов на новую платформу с уже готовыми портретами), не data recovery.

---

## §10.8 Инженерные границы и failure modes

### Что входит в scope §10

- Telegram Bot API как transport + orchestration layer
- Структура каналов и ролевая матрица
- Portrait schema + intake flow + privacy/GDPR mechanics
- Moderation model + escalation path
- Spam prevention + reputation layer
- Fork-and-merge governance stub per D27
- Backup options assessment

### Что вне scope §10

- Matchmaker routing logic и алгоритм match → §6 sibling cell
- Alliance governance (legal structure options A/B/C) → §5 sibling cell
- Full gate-by-gate evolution projection → §11 sibling cell
- Token economy design (D23) → L9 governance downstream
- Implementation code, SDK calls, deployment configs → intake §2 anti-scope

### Критические failure modes (engineering lens)

**Bot downtime:** Telegram-бот недоступен (hosting failure, rate-limit block, API outage). Последствия: новые инвайты не работают, portrait-intake заблокирован, matchmaker-запросы не обрабатываются. Члены по-прежнему общаются в чате напрямую — коммуникация не прерывается. Mitigation: health-check мониторинг бота (Phase-2+; Phase-1 manual check), restart procedure задокументирован.

**Member теряет Telegram-аккаунт:** Telegram аккаунт linked к phone number. Если member меняет номер или теряет доступ — теряет Telegram identity. Portrait в Jetix KB сохраняется. Процедура восстановления: member пишет Руслану по email-fallback (email указан при portrait-intake как backup contact), Руслан вручную выдаёт новый invite token под новый Telegram аккаунт, portrait transferируется к новому slug.

**GDPR data-deletion request:** Member запрашивает полное удаление. Portrait из Jetix KB — удаляется в течение 72h. Conversational history в Telegram-группах — технически вне прямого контроля Jetix (Telegram хранит на своих серверах); Jetix не владеет chat-data. Member информируется об этом ограничении при portrait-intake consent. Для чувствительных данных — member должен самостоятельно удалить свои сообщения в Telegram (Telegram позволяет удаление своих сообщений в чатах).

**Telegram API ToS change:** Telegram меняет Bot API Terms или вводит ограничения несовместимые с Secure Network use-case (например, запрет на invite-token automation). Mitigation: portrait-data остаётся в Jetix KB (не теряется при смене платформы); migration plan = re-enrollment членов на Discord или own-platform с готовыми портретами. Recovery time estimate: 2-4 недели для re-enrollment 50 членов; 8-16 недель для 200+ членов (Phase-2+ scenario). Это core rationale для §10.1 engineering dissent.

---

## Synthesis notes (integrator)

Данный раздел интегрирует input из трёх источников: intake §6.4 (binding constraints), L8 draft §2.3-2.5 (Secure Network + portraits + fork-community concept-level), и D27 (fork-and-merge architectural lock). Противоречий между источниками не обнаружено. Pending dissents поверхностно расходятся с управленческим оптимизмом в L8 draft по Telegram-as-primary — L8 draft описывает функциональность без engineering failure-mode lens; данный раздел добавляет этот lens без опровержения L8 позиций.

Два engineering dissent'а сохранены (см. frontmatter dissents[]):
1. Telegram platform lock-in risk — структурная зависимость от третьей стороны
2. Clean-room migration cost — chat history не мигрирует через Bot API

Оба dissent'а не блокируют Phase-1 реализацию (при Phase-1 scale риски приемлемы). Оба становятся load-bearing для Phase-2 архитектурного решения по own-platform timeline.

Recommended next step: brigadier dispatch `mgmt × integrator` для синтеза §10 (engineering) с §5 (Alliance governance) по вопросу Telegram vs own-platform timing — engineering surfaced risk, mgmt должен принять feasibility/priority decision.

---

## Источники (provenance)

- [src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md] §6.4 binding — Telegram primary; §4 risk-7 Дуров; §2 anti-scope
- [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md] §2.3 Secure Network Telegram-based; §2.4 Цифровые портреты; §2.5 Fork-community D27; §7 audio_524
- [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md] D27 Fork-and-merge verbatim; D25 Company-as-code git-native
- [src:decisions/JETIX-VISION.md] §5 Secure Network Phase-2+ evolution; §10 anti-LinkedIn positioning; §7.1 11 архетипов
