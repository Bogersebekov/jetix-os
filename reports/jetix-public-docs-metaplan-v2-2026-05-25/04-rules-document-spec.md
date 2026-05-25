---
title: Phase 3 — Rules Document spec (10 углов свода правил)
date: 2026-05-25
type: phase-report
phase: 3
parent_prompt: prompts/jetix-public-docs-metaplan-v2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-jetix-public-docs-metaplan-v2-phase-3
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
language: russian primary
status: pool — Rules document SPEC (структура, не сам свод); NO auto-promotion
---

# 📋 Phase 3 — Свод правил: спецификация (10 углов)

> **Что это.** Спецификация документа «Правила работы Jetix» (полка #9). NEW в v2 — Руслан
> голосом: «правила надо устанавливать тоже». Это **не сам свод** (R11 — NO sample content), а
> **спека**: какие 10 углов, какие правила в каждом, формат каждого правила, enforcement,
> процедура нарушения, что публично vs internal.
>
> **Формат каждого правила (шаблон):** `Утверждение` (что делаем/не делаем, одной фразой) →
> `Зачем` (rationale) → `Enforcement` (auto / manual / Steward / Halt-Log-Alert / lint) →
> `Нарушение` (что происходит при нарушении) → `Источник` (Pillar C / CLAUDE.md / D-LOCK / packet).
>
> **Жанр-референс (Phase 1):** Apple HIG (свод как стандарт) + John Lewis Constitution (правила =
> идентичность, публичны) + OpenAI Charter (конституционный якорь). НЕ юридический мелкий шрифт —
> читаемый человеческий свод.

---

## §0 Зачем свод правил отдельным документом

Правила сейчас **разбросаны**: Pillar C Tier-2 (12 hard rules) + CLAUDE.md §4 + Global Rules +
конвенции + AWAITING-APPROVAL discipline + R12 8 вопросов. Партнёр/член когорты не должен читать
Foundation, чтобы понять «по каким правилам тут живут». Свод = **человеческая проекция** разбросанных
правил в один читаемый документ, с честным разделением «это для всех публично / это внутренняя
дисциплина команды».

**Главный принцип свода (мета-правило):** правило без enforcement и без процедуры нарушения = не
правило, а пожелание. Каждое правило в своде обязано иметь оба. Это отличает Jetix-свод от
«ценностей на стене» (те — отдельный документ, полка #10).

---

## §1 Угол 1 — Operational (ежедневные операции)

**Зачем:** без операционной гигиены система-как-код разваливается; это «правила дорожного движения».

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| O-1 | YAML frontmatter обязателен в каждом .md (кроме README) | grep-навигация + provenance | lint | файл невидим индексу → fail-loud | Global Rules / conventions |
| O-2 | Логи append-only, новое сверху; >30 записей → archive/ | история не переписывается | manual + lint | потеря истории = R6 violation | Global Rules |
| O-3 | Перед созданием файла — проверь, что его нет | не плодим дубли | manual | duplicate-slug lint signal | conventions |
| O-4 | Каждое изменение = структурированный коммит `[area] verb what (why)` | company-as-code (D-25) | pre-commit | untraceable change | D-25 / KM MVP |
| O-5 | Даты YYYY-MM-DD; имена kebab-case; даты относительные → абсолютные | единообразие | lint | inconsistency | conventions |
| O-6 | CRM: voice-pipeline DRAFT-only, никогда не перезаписывает prod | защита данных контактов | voice_router DRAFT-mode | overwrite prod = data loss | CRM discipline / §4.2 |
| O-7 | API-key audit перед каждым коммитом (0 hits) | NEVER expose keys | pre-commit grep | ключ в репо = security incident | §4.2 / Global Rule 6 |

**Public vs internal:** operational — преимущественно **internal** (cohort onboarding / partner
fork «как работать в нашей системе»); наружу идёт только принцип «company-as-code + всё версионируется».

---

## §2 Угол 2 — Methodological (дисциплина метода)

**Зачем:** Jetix = метод-компания; если сам метод применяется неряшливо — оффер фальшивый.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| M-1 | Question-first, не function-first (O-185) | учим думать, не зубрить функции | peer-review | «накопить ещё substrate» trap | Method V2 §J / O-185 |
| M-2 | Гипотезы трекаются + фальсифицируемы (Hypothesis Architecture) | метод проверяем, не вера | hypothesis log | непроверяемое утверждение | Method V2 / DR-38 |
| M-3 | Мета-метод L3 применяется осознанно (выбор метода под задачу) | это ядро отличия от МИМ | self + peer | applied L1 где нужен L3 | Method V2 §J |
| M-4 | Адекватный интеллект: выбираем развивающие методы, не shortcuts (O-180) | не зачитерить развитие | self-discipline | shortcut вместо роста | O-180 / O-181 |
| M-5 | AI = усилитель внешней системы, не замена мышления (O-128) | cybernetic principle | self + content-review | делегировал мышление AI | O-128 / DR-40 |
| M-6 | Saturation-awareness: «накопить ещё» ≠ прогресс (O-163) | паттерн-ловушка | strategist review | substrate-hoarding | O-163 |

**Public vs internal:** methodological — **публично** (это сам оффер: «вот по каким правилам мы
думаем»). M-1, M-3, M-4, M-5 идут в полку #1 Метод + #7 Образование.

---

## §3 Угол 3 — R12 anti-extraction (ядро обещания)

**Зачем:** R12 = constitutional candidate rule 12; самое чувствительное; нарушение = подрыв всего оффера.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| R12-1 | Нельзя извлекать ценность сверх согласованной доли | анти-extraction ядро | Halt-Log-Alert + on-chain (Phase 2+) | extraction_beyond_share class | Tier-2 R12 / default-deny |
| R12-2 | Mondragón 5:1 — макс. выплата ≤ 5× мин. | нет extreme inequality | on-chain revert (Phase 2+) | wage_ratio_violation class | Economic V10 §5.3 |
| R12-3 | Fork-and-leave: уйти можно с долей, без штрафа | свобода выхода | Charter + exit token | fork_prevention_attempt class | Tier-2 R12 / §4.2 |
| R12-4 | 30-day opt-out window при любом Charter change | согласие, не навязывание | re-ack process | non_consensual_distribution class | Economic V10 §10.1 |
| R12-5 | 8 paired-frame вопросов перед любым партнёрским действием | проверка не-extraction | manual checklist | пропуск checklist = F4 ≤5s | EXECUTION-PLAN §4 |
| R12-6 | Стоп-сигнал готов: нарушение → стоп + лог + alert | fail-loud, не silent | Halt-Log-Alert | silent swallowing | Pillar C / Part 6b |

**8 вопросов R12 (verbatim из EXECUTION-PLAN, идут в свод):** ① цена ≤ польза? ② конкретно? ③
соразмерно отношениям? ④ по ступени? ⑤ канал уместен? ⑥ не доим / не запираем? ⑦ нет манипуляции?
⑧ стоп-сигнал готов?

**Public vs internal:** R12 — **полностью публично** (это полка #8 «Наше обещание»). Это
единственный угол, который наружу идёт целиком, как коммитмент.
**R12-paired (влияет на influence-ethics-expert):** этот угол = сам объект enforcement; пишется с
участием influence-ethics + recruitment-dynamics paired-frame.

---

## §4 Угол 4 — Ethical (честность / раскрытие / без манипуляции)

**Зачем:** этика влияния — не опция; без неё engagement-паттерны превращаются в манипуляцию (China anti-урок).

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| E-1 | Раскрываем участие AI; не выдаём AI за человека внешне | честность | content-review | AI impersonation (Tier-2 rule 10) | Pillar C rule 10 |
| E-2 | Нет фейк-срочности / MLM / культ-динамики | анти-манипуляция | R12 вопрос 7 + peer | манипулятивный паттерн | R12 / influence-ethics |
| E-3 | Consent-гейты перед сбором/использованием данных | согласие | manual gate | non-consensual = R12-4 | privacy + R12 |
| E-4 | Приглашаем, не вербуем (recruitment ≠ coercion) | анти-секта | recruitment-dynamics paired | true-believer exploitation | recruitment-dynamics-expert |
| E-5 | «Кого НЕ берём» честно — не тратим время анти-фита | уважение | partner doc | over-promising | EXECUTION-PLAN |
| E-6 | Признаём ошибки публично (Berkshire-тон) | доверие | Strategic Reflection | сокрытие провалов | reference Berkshire |

**Public vs internal:** ethical — **публично** (часть #8 + #10). E-1 (AI disclosure) критично наружу.
**R12-paired (STRICT):** весь угол пишется с influence-ethics auto-fire (это его прямая зона).

---

## §5 Угол 5 — Governance (принятие решений / Steward / Stage Gates)

**Зачем:** кто решает что — должно быть прозрачно, иначе «кооператив» = слово без механики.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| G-1 | Руслан = единственный R1-стратег (стратегию пишет владелец) | AI не стратегирует (rule 1) | Halt на agent-pending strategic prose | стратегия от агента | Tier-2 rule 1 |
| G-2 | Архитектурные изменения → AWAITING-APPROVAL packet | AI не исполняет архитектуру без гейта (rule 2) | stage_gate / stop_gate | autonomous arch change | Tier-2 rule 2 |
| G-3 | Stage Gates SG-1..SG-4 + de-morph reversibility | поэтапность + откат | /lint --check-stage-gates | skip gate | KM MVP / B3 mechanic |
| G-4 | 1-член-1-голос (Mondragón); SBT soulbound (Phase 2+) | равенство голоса | on-chain (Phase 2+) | vote-buying | Economic V10 / Mondragón |
| G-5 | Default-Deny на novel actions; uncategorized → escalate | rule 11 | default-deny-table | action без категории | Tier-2 rule 11 / Part 6b |
| G-6 | Corrigibility: никто не может запереть владельца из управления | владелец ack-authority финал | Halt-Log-Alert | lock-out attempt | FUNDAMENTAL §4.3 |
| G-7 | Steward role: хранит дисциплину, не владеет решением | роль ≠ власть | peer + Руслан | Steward overreach | governance §1 |

**Public vs internal:** governance — **смешанно**. Наружу: 1-член-1-голос + Stage Gates +
Steward-роль (как устроено). Internal: Default-Deny table / AWAITING-APPROVAL механика / Halt grades.

---

## §6 Угол 6 — Behavioral (коммуникация / конфликты / ротация)

**Зачем:** как ведут себя люди (и агенты) друг с другом — определяет, секта это или здоровое сообщество.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| B-1 | Прямой стиль, без воды, ориентир на действие | Ruslan-стиль | self | многословие/вода | CLAUDE.md «Кто ты» |
| B-2 | Конфликт → human gate, не autonomous negotiation (rule 7) | агенты не решают противоречия сами | Halt | autonomous negotiation | Tier-2 rule 7 |
| B-3 | Peer-check: агент не оценивает агента без human review (rule 8) | анти-замкнутость | manual review | peer-eval без человека | Tier-2 rule 8 |
| B-4 | Ротация принципов: роли меняются, власть не накапливается | анти-культ | governance | role entrenchment | recruitment-dynamics |
| B-5 | Hub-and-spoke: subagents → Lead → Manager (≤20 задач) | attention budget | routing-table | bypass hub | §4.2 / Global Rule 8-9 |
| B-6 | Русский для контента, English для кода/конфигов | единообразие | manual | language-mix в коде | §4.2 / Global Rule 7 |

**Public vs internal:** behavioral — преимущественно **internal** (как работаем внутри); наружу
идёт принцип B-4 (ротация, анти-культ) как часть R12-обещания «не секта».

---

## §7 Угол 7 — Content (что публикуем / что гейтим)

**Зачем:** без content-правил substrate утечёт наружу неподготовленным (анти-паттерн DOCS-CLASSIFICATION).

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| C-1 | Substrate/System не идут наружу напрямую — суть переписывается в человеческий жанр | анти «секта-жаргон» | content-review | raw substrate наружу | DOCS-CLASSIFICATION фильтр |
| C-2 | R12-check (8 вопросов) перед отправкой партнёрского контента | не доим в коммуникации | manual checklist | extraction в outreach | R12 / EXECUTION-PLAN |
| C-3 | Не слать 5+ ссылок — одна дверь за раз (анти-overwhelm) | cognitive load | manual | overwhelm → закрывается | DOCS-CLASSIFICATION §9 |
| C-4 | Не давать substrate до пояснительных (порядок слоёв) | framing first | manual | substrate без framing | анти-паттерн |
| C-5 | DRAFT ≠ final; polish перед публикацией | качество | manual + lint | DRAFT наружу | анти-паттерн |
| C-6 | System (Foundation Parts / Halt-Log-Alert) — никогда наружу | анти «закрытый клуб» | content-review | System exposed | DOCS-CLASSIFICATION |

**Public vs internal:** content — **internal дисциплина** (как готовим публикации); наружу не идёт,
но определяет качество всего публичного набора.

---

## §8 Угол 8 — Financial (прозрачность / распределение / потолок)

**Зачем:** деньги — самая чувствительная зона доверия; кооператив без финансовой прозрачности = пустой звук.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| F-1 | Charter публикует split (75% worker / 25% Foundation) | прозрачность модели | Charter public | скрытый split | Economic V10 / R12-1 |
| F-2 | Mondragón 5:1 wage ratio cap | анти-неравенство | on-chain (Phase 2+) | F-2 = R12-2 | Economic V10 §5.3 |
| F-3 | Opt-in shares: доля обсуждается per Charter (10-25%) | согласие на условия | Charter signup | принудительная доля | PARTNER-OFFERING §3 |
| F-4 | Distribution options: cash / locked / mix — выбор партнёра | автономия | Charter | навязанная форма | Economic V10 §5.2 |
| F-5 | QF-распределение community pool (contribution-aligned) | анти-extraction | on-chain (Phase 2+) | произвольное распределение | Economic V10 §9 |
| F-6 | Revenue-gated spend (D-15): тратим из выручки, не из воздуха | дисциплина капитала | strategist | overspend | D-15 |

**Public vs internal:** financial — **модель публично** (75/25, 5:1, fork-and-leave = доверие,
Equal-Exchange урок); **отчётность — НЕ публично** (defer, специалисты; DOCS-CLASSIFICATION ⛔).
Это критичное разведение: «модель денег» ≠ «финансовая отчётность».

---

## §9 Угол 9 — Privacy (данные / члены / когорта)

**Зачем:** работаем с данными контактов (CRM 180), когорты, голосовыми; без privacy-правил — риск.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| P-1 | Не трогать private/ ~/.ssh/ .env | базовая безопасность | manual + gitignore | data leak | §4.2 / Global Rule 6 |
| P-2 | Данные члена — его; согласие на использование | consent | consent gate | non-consensual use | R12-4 / E-3 |
| P-2 | Cohort data не передаётся вовне без согласия | приватность когорты | manual | external sharing без consent | privacy |
| P-3 | Voice-pipeline DRAFT-only, не auto-distribute (distribute.py архивирован) | человеческое ревью | архив distribute.py | auto-distribute Claude-выводов | voice pipeline §|
| P-4 | Filesystem = source of truth; Notion = view | контроль данных | D-17 | Notion как авторитет | D-17 / §4.2 |

**Public vs internal:** privacy — **смешанно**. Наружу: принцип «твои данные — твои + согласие».
Internal: технические правила (private/ / gitignore / DRAFT-режим).

---

## §10 Угол 10 — Quality (provenance / cross-cite / no fake metrics)

**Зачем:** без quality-правил substrate теряет доказуемость; «fake metrics» = смерть доверия методолога.

| # | Утверждение | Зачем | Enforcement | Нарушение | Источник |
|---|---|---|---|---|---|
| Q-1 | F-G-R triple на каждое promoted утверждение | доказуемость | Part 6a schema | claim без F-G-R | Part 6a / FPF B.3 |
| Q-2 | Cross-cite: `[src:...]` на каждое заимствованное утверждение | provenance | lint | unsourced claim | R6 / pipeline |
| Q-3 | Append-only история; не переписываем прошлое | честность истории | lint | history rewrite | Global Rules |
| Q-4 | Нет fake metrics / выдуманных цифр | анти-маркетинг-ложь | peer + R6 | invented numbers | R6 / quality |
| Q-5 | Lint failure = fail-loud (FUNDAMENTAL §5.5) | не прячем поломки | /lint | silent fail | §4.4 / FUNDAMENTAL |
| Q-6 | Claims устаревают: stale-claim сигнал → ревью | актуальность | /lint stale-claim | устаревшее как факт | lint signals |

**Public vs internal:** quality — **internal дисциплина**, но **принцип** наружу (для двери C
методолога: «мы помечаем provenance и не выдумываем метрики» = аргумент доверия).

---

## §11 Сводная карта: 10 углов × public/internal × enforcement-тип

| Угол | Кол-во правил | Public/Internal | Главный enforcement | В какую полку |
|---|---|---|---|---|
| 1 Operational | 7 | internal | lint + pre-commit | #9 (internal split) |
| 2 Methodological | 6 | public | peer-review | #1 #7 |
| 3 R12 anti-extraction | 6 | **public целиком** | Halt-Log-Alert + on-chain | #8 |
| 4 Ethical | 6 | public | content-review + paired-frame | #8 #10 |
| 5 Governance | 7 | смешанно | gate + Halt | #3 |
| 6 Behavioral | 6 | internal (+B-4 public) | manual + routing | #9 #3 |
| 7 Content | 6 | internal | content-review | #9 |
| 8 Financial | 6 | модель public / отчётность ⛔ | Charter + on-chain | #4 #8 |
| 9 Privacy | ~5 | смешанно | gate + gitignore | #9 |
| 10 Quality | 6 | internal (+ принцип public) | lint + Part 6a | #9 |
| **ИТОГО** | **~61 правило** | 4 public / 3 смеш. / 3 internal | | |

**Мета-вывод для Руслана (R1):** свод естественно делится на **публичную часть** (Methodological /
R12 / Ethical / Financial-модель + принципы Governance) и **внутреннюю** (Operational / Content /
Quality / Behavioral / технический Privacy). Публичная часть = ~25-30 правил → идёт в полки #8/#9/#10/#1.
Внутренняя = ~30 правил → cohort onboarding + partner fork onboarding.

---

## §12 R1 decisions для свода (surface)

1. **Публичная vs внутренняя граница** — согласна ли разметка §11? (что наружу / что только команде)
2. **Формат свода** — единый длинный документ (John Lewis Constitution) ИЛИ 10 коротких страниц per угол (Apple HIG-разделы)?
3. **Тон R12-угла** — sworn-statement («мы обязуемся…») ИЛИ описательный («у нас так устроено»)?
4. **Когда писать** — Wave 3 (Build exit) per Phase 9, или раньше (R12-угол сейчас, остальное позже)?
5. **Violation-процедуры наружу** — показывать ли публично «что будет при нарушении» (Halt grades) или только принцип?

---

*Phase 3 closure. Rules document spec: 10 углов (Operational / Methodological / R12 / Ethical /
Governance / Behavioral / Content / Financial / Privacy / Quality), ~61 правило, каждое в шаблоне
Утверждение→Зачем→Enforcement→Нарушение→Источник. Public/internal разметка per угол. Сводная карта
§11 + 5 R1-решений. Жанр-референс: Apple HIG + John Lewis Constitution + OpenAI Charter. R12 paired-
frame STRICT (углы 3/4 пишутся с influence-ethics auto-fire). R11 — спека, NO sample свод. IP-1.
Источники: Pillar C Tier-2 12 rules + CLAUDE.md §4 + Global Rules + Economic V10 + EXECUTION-PLAN.
Pool result.*
