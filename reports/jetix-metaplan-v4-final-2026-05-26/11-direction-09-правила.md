---
title: "MetaPlan V4 — Direction #9: Правила работы (портфельный спек)"
date: 2026-05-26
type: phase-report-metaplan-v4
phase: 10
direction: 9
F: F2-F3
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
language: russian
status: draft-report
prose_authored_by: brigadier-scribe (R1 surface — Ruslan authors final integration)
constitutional_posture: R1 surface only + R2 STRICT (Pillar C LOCKED preserved) + R11 + R12 paired-frame STRICT + IP-1 STRICT
predecessors:
  - reports/jetix-metaplan-v3-final-2026-05-26/11-direction-09-правила.md (V3 baseline)
  - decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-V2-2026-05-25.md (§3)
  - reports/jetix-public-docs-metaplan-v2-2026-05-25/04-rules-document-spec.md
  - CLAUDE.md §4.1 (12 hard rules — Pillar C Tier-2)
  - swarm/wiki/foundations/principles/architecture.md
v4_additions:
  - §V4-delta: anti-dark-patterns rules (#15 Геймификация R12-HIGHEST)
  - §V4-delta: event conduct rules (#16 Хакатоны)
  - §V4-delta: inter-clan competition rules
  - §V4-delta: clan governance boundary rules (platform floor vs inner-clan freedom)
---

# Direction #9 — Правила работы: портфельный спек (V4)

## Введение: грань Foundation, позиция в метаплане, зачем это направление

Jetix — мега-мастерская мирового уровня. Три грани Foundation: **Мастерская** (ГДЕ — пространство, зоны, инфраструктура) · **Мастерство** (ЧТО прокачивают — репертуар методов, мета-метод, фронтир) · **Сеть** (КАК распределено — mesh cells, pooling ресурсов, fork-and-leave). One-liner: «Jetix — мега-мастерская мирового уровня: место, где люди становятся мастерами в эпоху AI, вместе двигают фронтир и не дают системе доить или запирать себя».

Direction #9 «Правила работы» — это **операционка всех трёх граней**: как ставить станок, как пулить ресурс, как форкнуть. Без правил мастерская превращается в хаос, мастерство — в произвол, сеть — в конфликт. При этом правило без enforcement и без процедуры нарушения — это пожелание, не правило. Именно это отличает Jetix-свод от типичного «манифеста с ценностями».

**V4-контекст: 16 направлений.** К 14 направлениям V3 добавлены #15 Геймификация (R12-HIGHEST — наиболее высокий R12-риск из всех направлений) и #16 Хакатоны (events). Свод правил Direction #9 в V4 расширяется на эти два новых домена: anti-dark-patterns правила для геймификации и event conduct правила для хакатонов. Кроме того, появляется новый раздел о правилах кланов: принципиальное разграничение между тем, что enforced платформой (ценностной floor), и тем, что остаётся внутренней свободой клана. Это самое важное новое различие V4.

**Позиция в хабовой структуре.** #9 связан с хабом #8 R12 (правила — это enforcement-обёртка обещания), с #10 Ценности (каждое правило — ценность, ставшая операциональной), с #1 Метод (методологическая дисциплина), с #14 Кланы (lifecycle governance), с #15 Геймификация (anti-dark-patterns enforcement), с #16 Хакатоны (event conduct). GAP текущего состояния: ⚠️ partial — правила существуют (Pillar C Tier-2, CLAUDE.md §4, Global Rules, AWAITING-APPROVAL discipline), но разбросаны по Foundation-документам; публичная vs внутренняя граница — R1.

**Мета-правило (главный принцип свода):** правило без enforcement и процедуры нарушения = пожелание, не правило.

**Формат каждого правила:** Утверждение → Зачем → Enforcement → Нарушение → Источник.

**10 углов, ~61 правило (V3-baseline) + V4-delta кластеры:**

| Угол | Правил | Режим | Главный предмет |
|---|---|---|---|
| 1 Operational | 7 | internal | frontmatter / append-only / commit / API-key audit |
| 2 Methodological | 6 | public | question-first / гипотезы / мета-метод / адекватный интеллект |
| 3 R12 anti-extraction | 6 | public целиком | 8 вопросов + 5:1 + fork-and-leave + 30-day |
| 4 Ethical | 6 | public | AI disclosure / нет манипуляции / consent / приглашаем не вербуем |
| 5 Governance | 7 | смешанно | Ruslan=стратег / AWAITING-APPROVAL / Stage Gates / 1-голос |
| 6 Behavioral | 6 | internal (+B-4 public) | прямой стиль / конфликт→gate / ротация анти-культ |
| 7 Content | 6 | internal | substrate не raw наружу / R12-check |
| 8 Financial | 6 | модель public / отчётность internal | 75/25 / 5:1 / opt-in / QF |
| 9 Privacy | ~5 | смешанно | private/ / данные члена=его / voice DRAFT-only |
| 10 Quality | 6 | internal (+принцип public) | F-G-R / cross-cite / нет fake metrics / fail-loud |
| **V4** Anti-dark-patterns | ~6 | **public** | Геймификация #15: no addictive loops / intrinsic primacy / opt-out |
| **V4** Event conduct | ~5 | **public** | Хакатоны #16: fair competition / sponsorship transparency / payout cap |
| **V4** Inter-clan competition | ~4 | **public** | Уважение между соревнующимися / no poaching / no sabotage |
| **V4** Clan governance boundary | ~5 | **смешанно** | Platform floor vs inner-clan freedom — ключевое V4-различие |

~25-30 публичных (V3) + ~16 публичных (V4-delta) + ~30 внутренних. Жанр-референс: **Apple HIG** (свод как стандарт дизайна) + **John Lewis Constitution** (правила как основа доверия сообщества) + **OpenAI Charter** (конституционный commitment перед внешним миром).

> **R1:** все формулировки ниже — варианты/опции для рассмотрения. Финальные решения за Ruslan.
> **R2 STRICT:** Pillar C LOCKED — ссылки, не правки.
> **R11:** ниже — описание ЧЕГО содержит каждый документ, не сам публичный текст.
> **IP-1 STRICT:** имена = role-type примеры (T1-методолог, T3-контрибьютор, F-партнёр и т.д.).
> **R12 paired-frame STRICT:** influence-ethics-expert auto-pair для углов 3/4 + весь §V4-delta anti-dark-patterns.

---

## §A — Главный документ «Свод правил»

### A.1 One-pager «Зачем нам правила» (≤500 слов, публичный)

**Аудитория.** Потенциальный участник, партнёр (T1/T2), журналист, инвестор. Человек, который видит название «Свод правил» и у которого возникает ощущение «бюрократия» или «манифест».

**Задача.** Сдвинуть восприятие: правила — это защита, не контроль. Правила — это то, что делает мастерскую безопасной для честной работы, а не инструмент власти.

**Разделы one-pager:**
1. **Почему правила — это не про контроль.** Один абзац: мета-правило (правило без enforcement = пожелание); что это означает для участника — что каждое обязательство реально.
2. **Структура: 10 углов + V4 кластеры.** Краткая карта — что публично (R12-обещание / Метод / Этика / Финансовая модель / Anti-dark-patterns / Event conduct) и что внутреннее (операции / качество / контент / поведение). Честное разделение.
3. **Главные обещания наружу.** 4-5 пунктов из публичных углов: не доим (R12-1), можно уйти с долей (R12-3), AI раскрываем (E-1), финансовая модель открыта (F-1), геймификация не манипулятивная (Anti-dark-patterns).
4. **Где читать подробнее.** CTA: R12-обещание → полка #8; Governance → Charter; Метод → Direction #1; Геймификация → Direction #15; Хакатоны → Direction #16.

**V4-добавление в one-pager.** В V4 одно из «главных обещаний наружу» — anti-dark-patterns commitment. Это отдельный пункт: «Мы не строим петли зависимости, не используем переменное вознаграждение для удержания, не создаём FOMO как инструмент давления. Мотивация — только внутренняя». Этот пункт публичный и R12-несущий — нарушение = нарушение R12 (extraction через манипулятивное удержание).

**Формат.** Markdown-источник → лендинг-секция + PDF (A4). Три варианта заголовка на выбор Ruslan: (a) «Правила как защита, не как контроль» (b) «Что мы обязуемся делать и не делать» (c) «10 углов + новые стандарты: полный свод».

### A.2 Long-form свод (≤4K слов спек)

**Главный вопрос R1 (Ruslan выбирает до написания):** единый документ — один файл ~4K (John Lewis Constitution) ИЛИ 10+ страниц per угол (Apple HIG-разделы, каждая ~400 слов)?

**Аргументы за единый:** проще как коммитмент, проще ссылаться («§3 R12»), психологически весомее. **Аргументы за 10+ страниц:** проще обновлять по-угольно, легче фильтровать public/internal, удобнее для partner-fork (берут нужные углы), V4-delta кластеры добавляются как дополнительные страницы без переписывания основного.

**V4-изменение структуры long-form.** Добавляются новые секции:
- §13 Anti-dark-patterns правила (V4, для Геймификации #15)
- §14 Event conduct правила (V4, для Хакатонов #16)
- §15 Inter-clan competition правила (V4)
- §16 Clan governance boundary: platform floor vs inner-clan freedom (V4 — ключевое различие)

**Структура long-form (V4, оба варианта включают):**
- §0 Мета-правило и формат шаблона (обязательный вводный блок)
- §1–§10 Каждый угол: список правил в шаблоне Утверждение→Зачем→Enforcement→Нарушение→Источник
- §11 Сводная карта public/internal
- §12 Violation-классы и enforcement-градиент (F2/F4/F8 из Part 6b)
- §13–§16 V4-delta кластеры (anti-dark-patterns / event conduct / inter-clan / clan governance boundary)
- §Appendix Источники (Pillar C Tier-2 ссылки, Economic V10, EXECUTION-PLAN, R12 paired-frame)

**Public/internal разметка:** каждое правило помечается тегом `[public]` / `[internal]` / `[partner]`. V4-delta правила преимущественно `[public]` — они нужны внешнему участнику для оценки trustworthiness.

**Enforcement-градиент (из Part 6b §I.2):**
- F8 grade: остановка ≤1s + Halt-Log-Alert (extraction_beyond_share, fork_prevention_attempt, addictive_loop_implementation)
- F4 grade: ≤5s (пропуск R12-checklist, missing paired-frame, anti-dark-patterns violation в геймификации)
- F2 grade: ≤60s (frontmatter missing, commit без area-prefix, event conduct violation)

---

## §B — Видео

Для «Свода правил» видео в обычном смысле (YouTube-ролик, курс) **не является приоритетным артефактом**. Правила — это документ-референс, не нарратив. Однако возможны два мини-сценария:

**B.1 Orientation clip (3-5 мин, опционально).** Для cohort onboarding: кто-то из T1-методологов объясняет мета-правило и структуру 10 углов. Не заменяет документ — дополняет для тех, кто не читает до онбординга. Формат: screenshare + голос, не продакшн-видео.

**B.2 R12-обещание clip.** Если Direction #8 R12/Обещание делает своё видео — правила угла 3 и 4 туда вставляются как shared block. Правила #9 как самостоятельного видео-направления — defer до Wave 3+.

**B.3 V4-добавление: Anti-dark-patterns clip (опционально, для #15).** Если Direction #15 Геймификация делает объяснительный контент — rules угла anti-dark-patterns вставляются туда как shared block. Это важно: аудитория #15 должна видеть не просто «у нас геймификация», но «у нас геймификация с явными anti-dark-patterns правилами, и вот что это означает на практике».

**R1:** нужен ли orientation clip — Ruslan решает после Wave 2 cohort-feedback. Нужен ли anti-dark-patterns clip — решается вместе с Direction #15.

---

## §C — Курс / Onboarding rules module

Правила — не самостоятельный курс, но **обязательный модуль в двух местах:**

**C.1 Cohort onboarding (первый день).** Модуль «Как мы работаем»: мета-правило → 10 углов (обзор 15 мин) → практика: заполнить frontmatter-шаблон + сделать пробный commit → consent gate (подтвердить R12-3 понял). V4-добавление в onboarding: явный блок про clan governance — какой floor платформа enforces, а какой governance остаётся за кланом. Это снимает вопрос «кто мной управляет» на старте.

**C.2 Partner onboarding.** Отдельный трек: какие правила обязательны при форке (R12/Ethical/Anti-dark-patterns = mandatory), какие адаптируемы (Operational/Content). V4: Anti-dark-patterns добавляется в mandatory — форк не может убрать запрет на аддиктивные петли, если хочет ассоциироваться с Jetix. Ссылка на §L (Partner-extension hook).

**C.3 AI-agent onboarding.** Текущее состояние: CLAUDE.md §4.1 (12 hard rules Pillar C) + default-deny-table.yaml. В рамках direction #9 это не новый артефакт — это документирование существующего как «machine-readable модуль правил». V4: добавляются 4 новых violation classes в default-deny-table.yaml: `addictive_loop_implementation`, `fomo_pressure_tactic`, `variable_reward_for_retention`, `event_payout_cap_violation`.

**C.4 V4-добавление: Clan onboarding.** При создании нового клана (Direction #14 lifecycle) — специализированный modular check: (a) подтверждение platform floor (триада + R12 + уважение — это не опционально); (b) принятие inner-clan freedom на своё усмотрение; (c) consent на inter-clan competition правила. Этот check документируется в clan charter.

**Что НЕ строим здесь:** полноценный e-learning курс с LMS — defer до Wave 3, зависит от Direction #7 Образование.

---

## §D — Книга

Книга по «Своду правил» как отдельный артефакт — **не релевантна**. Правила — это живой операционный документ, не нарратив для книги. Единственный сценарий, где правила попадают в книгу — это глава в более широкой книге о Jetix-методе (Direction #1 или #6 Vision). Там угол R12 anti-extraction и угол Governance могут составить отдельную главу «Почему правила — это инфраструктура свободы».

**V4-добавление.** В такой главе теперь появляется тема anti-dark-patterns как часть той же «инфраструктуры свободы»: свобода не только от extraction (R12) и lock-in (fork-and-leave), но и от манипулятивного удержания через психологические механизмы. Три составляющих свободы: 1) не доим → R12; 2) можно уйти → fork-and-leave; 3) не удерживаем манипулятивно → anti-dark-patterns. Это сильная нарративная триада для книги.

**R1:** если Ruslan планирует книгу по Jetix — правила направлений #3/#4/#5 (governance + extraction) + V4 anti-dark-patterns → одна глава «The Rules That Protect, Not Control: три составляющих свободы».

---

## §E — Инструкции / SOP (per-угол enforcement procedures)

Это самая операционная часть арсенала. Каждый угол требует своей SOP.

**E.1 SOP угла 1 Operational.**
- Чеклист перед каждым коммитом: frontmatter present? / append-only не нарушен? / API-key grep → 0 hits? / commit message format?
- Decision tree: файл уже существует → не создавать новый; лог > 30 записей → ротировать в archive/
- Violation-процедура: lint failure → fail-loud, блок коммита; API-key в файле → immediate halt + remove + alert Ruslan

**E.2 SOP угла 2 Methodological.**
- Процедура: перед любым claim в публичном документе — явная гипотеза (H:) + confidence (R-low/mid/high) + источник
- Anti-pattern: «мы знаем, что…» без источника → F4 grade, возврат на revision
- Decision tree: если claim требует inference → пометить R-low; если из locked Foundation → R-high + ссылка

**E.3 SOP угла 3 R12 anti-extraction.**
- 8 вопросов R12 = обязательный чеклист перед любым партнёрским outreach, публикацией оффера, изменением Charter
- Violation-процедура: extraction_beyond_share → Halt-Log-Alert F8 + log в swarm/approvals/log.jsonl + alert Ruslan; fork_prevention_attempt → same
- Anti-pattern: «одно исключение» без AWAITING-APPROVAL = нарушение, не исключение

**E.4 SOP угла 4 Ethical.**
- AI disclosure: любой публичный output, созданный AI, должен иметь пометку (в метаданных или явно). Проверяется перед публикацией.
- Манипуляция-check: использовать R12 вопрос 7 («есть ли срочность/страх?»). Паттерн найден → revision + influence-ethics-expert review
- Consent gate: перед сбором/использованием данных участника → explicit ack, записывается в лог

**E.5 SOP угла 5 Governance.**
- AWAITING-APPROVAL packet: любой Foundation-level path write → пакет создаётся, Ruslan approve обязателен
- Stage Gate check: `/lint --check-stage-gates` ежедневно; SG predicate fail → блок промоции
- 1-голос-1-участник: любое голосование в cohort → equal weight независимо от доли вклада (кроме RUSLAN-LAYER решений)

**E.6–E.10 SOP углов 6-10** (Behavioral / Content / Financial / Privacy / Quality): аналогичная структура — чеклист + decision tree + violation-процедура. Приоритет разработки: после E.1–E.5.

**E.11 V4: SOP anti-dark-patterns (Геймификация #15).**
- Чеклист перед любым геймификационным feature: (a) использует ли переменное вознаграждение для удержания? (b) создаёт ли FOMO как инструмент давления? (c) есть ли social pressure mechanics (leaderboard без opt-out)? (d) есть ли sunk-cost трапы? (e) мотивация внешняя или внутренняя по дизайну?
- Violation-процедура: любой ответ «да» на (a)–(d) → revise feature + influence-ethics-expert review (обязательный paired-frame для #15)
- Grade: внедрение аддиктивной петли = F8 (addictive_loop_implementation в default-deny-table.yaml)
- Anti-pattern: «все так делают» — не аргумент. Jetix anti-dark-patterns = конкурентное преимущество через честность, не handicap.

**E.12 V4: SOP event conduct (Хакатоны #16).**
- Чеклист перед каждым хакатоном: спонсорство раскрыто публично? / выплаты ≤ 5:1 cap? / правила fair competition опубликованы? / есть ли anti-competitive exclusions?
- Violation-процедура: event_payout_cap_violation → F2 grade + пересмотр призового фонда до публикации; скрытое спонсорство → F4 + публичное исправление
- Decision tree: если спонсор хочет влиять на результаты → reject или separate track с явной маркировкой

**Anti-pattern главный для всего свода:** написать правило без enforcement и без violation-процедуры. Это мета-нарушение самого мета-правила. Проверяется на lint стадии перед любой публикацией из свода.

---

## §F — Шаблоны / Templates

**F.1 Rule template (5 элементов).**
Стандартный шаблон для записи любого правила в своде:
```
Утверждение: [одна фраза — что делаем/не делаем]
Зачем: [1-2 предложения — ценность правила]
Enforcement: [механизм — lint / gate / checklist / on-chain / peer-review]
Нарушение: [что происходит — grade F2/F4/F8 + action]
Источник: [Pillar C rule N / Economic V10 §X / EXECUTION-PLAN / D-Lock entry]
```
Этот шаблон = единица свода. Все ~61 правило (V3) + V4-delta правила записаны в нём.

**F.2 Enforcement log template.**
Формат записи в swarm/approvals/log.jsonl при F4/F8 нарушении:
```json
{
  "ts": "ISO-8601",
  "rule_id": "R12-1 / O-3 / Q-5 / ADP-2 / EC-1 ...",
  "grade": "F8 / F4 / F2",
  "violation_class": "extraction_beyond_share / addictive_loop_implementation / ...",
  "action_taken": "halt / revision / alert",
  "resolved_by": "Ruslan / auto-lint / influence-ethics-expert / ...",
  "notes": ""
}
```

**F.3 Violation report template.**
При нарушении F4/F8 — краткий отчёт (до 10 строк): что нарушено, когда, кем (role-type, не executor per IP-1), как разрешено, изменилось ли правило по итогу.

**F.4 Charter amendment template.**
При изменении любого public-правила (особенно R12/Governance/Anti-dark-patterns): AWAITING-APPROVAL packet → 30-day opt-out window → re-ack process → обновление свода + лог.

**F.5 V4: Clan governance boundary template.**
При создании или форке клана — стандартный шаблон разграничения:
```
Клан: [название]
Platform floor (enforced, не меняется): [триада + R12 + уважение + anti-dark-patterns]
Inner-clan freedom: [methods / topics / management style / schedule / internal language]
Inter-clan agreement: [подтверждение no-poaching / no-sabotage / fair competition]
Charter date: [ISO-8601]
```
Этот шаблон = единица clan governance documentation.

---

## §G — Презентация (10-20 слайдов)

**Назначение.** Объяснить структуру 10 углов + V4-delta команде, партнёрам, новым участникам cohort. Не маркетинг — навигация.

**Структура (14 слайдов, V4):**

1. **Слайд 1.** Заголовок + мета-правило: «Правило без enforcement = пожелание». Почему это важно.
2. **Слайд 2.** Схема: мега-мастерская → 3 грани → правила как операционка всех трёх. V4-добавление: кланы + хакатоны как новые элементы системы.
3. **Слайд 3.** 10 углов — дерево (Operational/Methodological/R12/Ethical/Governance/Behavioral/Content/Financial/Privacy/Quality). Раскраска: public (зелёный) / internal (серый) / смешанно (жёлтый).
4. **Слайды 4-6.** Публичные углы (R12 / Ethical / Methodological / Financial-модель): по одному слайду на 2 угла. Ключевые правила — не полный список, а «зачем это публично».
5. **Слайды 7-9.** Внутренние углы (Operational / Content / Quality / Behavioral): аналогично, зачем это внутреннее.
6. **Слайд 10.** Governance-угол отдельно: Ruslan=стратег + AWAITING-APPROVAL + Stage Gates + 1-голос. Это и public и internal одновременно.
7. **Слайд 11.** Enforcement-градиент: F8/F4/F2 — что за что. V4: новые violation classes в таблице.
8. **Слайд 12 (V4 новый).** Anti-dark-patterns правила: 5 запретов (addictive loops / variable rewards / FOMO / sunk-cost / social pressure) + почему это R12-несущее, не просто этическое предпочтение.
9. **Слайд 13 (V4 новый).** Clan governance boundary: схема — что платформа enforces (floor, неизменный) vs что клан решает сам (freedom). Это самый важный V4-слайд для участников.
10. **Слайд 14.** CTA: где читать полный свод (публичная часть → полка #9; партнёрская → Charter; machine-readable → CLAUDE.md §4.1; clan governance → Direction #14).

**Референс по стилю.** Apple WWDC engineering session: без декоративности, максимум схем и таблиц, минимум bullet points.

---

## §H — FAQ (10-20 вопросов, честные ответы)

**H.1 «Зачем столько правил? 61+ — это много.»**
61+ звучит много, но ~30 из них internal — партнёр/участник их не читает, это наша операционная гигиена. Публичных ~25-30 (V3) плюс ~16 V4-delta. И каждое правило маленькое: одна фраза + зачем + что будет. Это не юридический договор — это навигация.

**H.2 «Кто следит за выполнением?»**
Три уровня: (a) машина — lint, pre-commit hooks, Halt-Log-Alert автоматически на F4/F8; (b) peer-review в cohort — для Methodological и Ethical; (c) Ruslan — для Governance и архитектурных решений. Нет «полиции правил» — есть встроенные механизмы.

**H.3 «Правила можно менять?»**
Да, через Charter amendment process: AWAITING-APPROVAL + 30-day opt-out window + re-ack. Это не бюрократия — это гарантия, что изменение правил не происходит тихо и без согласия участников.

**H.4 «Что будет, если нарушить?»**
Зависит от класса нарушения. F8 (extraction_beyond_share, fork_prevention, addictive_loop_implementation) — немедленный halt + alert. F4 (пропуск R12-checklist, anti-dark-patterns) — возврат на revision ≤5s. F2 (frontmatter missing, event conduct) — lint failure, коммит блокируется. Violation log пишется всегда.

**H.5 «Правила R12 — это реально или только декларация?»**
Реально ровно настолько, насколько enforcement механизм реален. Сейчас: manual checklist + gate + Halt-Log-Alert. Phase 2+: on-chain smart-contract (Ethereum substrate, per §4.2 RUSLAN-LAYER). Мы честны: Phase 2+ = будущее, не настоящее.

**H.6 «Это как манифест стартапа — напишете и забудете?»**
Анти-паттерн, который мы знаем. Именно поэтому мета-правило стоит первым: без enforcement = пожелание. Свод живёт пока работают enforcement-механизмы. Если механизм сломан → правило помечается как INACTIVE, не удаляется (append-only discipline).

**H.7 «Могу ли я форкнуть и взять только часть правил?»**
Да, это явно предусмотрено. Угол R12, Ethical и Anti-dark-patterns — mandatory при форке. Operational и Content — адаптируемы. Governance — рекомендуем сохранить AWAITING-APPROVAL дисциплину, но можно адаптировать под свою org. Детали в §L (Partner-extension hook).

**H.8 «Правило "AI не принимает стратегических решений" — что это значит на практике?»**
AI генерирует варианты, surfaces options, drafts. Любая strategic prose должна быть authored Ruslan или hybrid-with-ack-trail. Если AI написал стратегический документ без ack-trail — это нарушение Pillar C rule 1 (F4 grade). На практике: каждый ключевой документ имеет `prose_authored_by:` в frontmatter.

**H.9 «Правила звучат как что-то для больших компаний. Зачем это маленькой мастерской?»**
Потому что доверие строится до масштаба, а не после. Партнёр T1-методолог, который приходит сейчас, смотрит: «есть ли структура или будет хаос при росте?». Правила — это архитектура доверия, не бюрократия.

**H.10 «Что такое "правило без enforcement = пожелание"?»**
Это главный принцип, зафиксированный в §0 свода. Смысл: если написано «мы не доим участников», но нет механизма проверки и нет последствия при нарушении — это просто фраза. Enforcement делает правило реальным. Именно поэтому каждое из ~61 правил имеет обязательное поле Enforcement.

**H.11 V4: «Что такое anti-dark-patterns и зачем это отдельные правила?»**
В V4 появился Direction #15 Геймификация. Геймификация — самый высокий R12-риск из всех 16 направлений, потому что она технически может использовать психологические механизмы (переменное вознаграждение, FOMO, social pressure) для манипулятивного удержания участников. Это extraction через психологию, не через финансы — но всё равно extraction по духу R12. Anti-dark-patterns правила делают это нарушением с F4/F8 grade, не просто «нежелательной практикой». Это R12-несущие правила, поэтому они публичные.

**H.12 V4: «Что клан может решать сам, а что нельзя?»**
Разграничение: **platform floor** (что enforced платформой, не меняется) = ценностная триада + R12 anti-extraction + уважение к другим кланам + anti-dark-patterns. Всё остальное — **inner-clan freedom**: методы работы, темы, стиль управления, внутренний язык, расписание, внутренняя governance (если она не нарушает floor). Клан не может убрать floor — но внутри floor делает что хочет. Это самое важное V4-различие, которое снимает страх «нас будут контролировать».

**H.13 V4: «Правила для хакатонов — это серьёзно? Хакатон же просто мероприятие.»**
Хакатон — это конкурс с призами, спонсорами и публичной репутацией. Event conduct правила: fair competition (нет читинга, нет anti-competitive exclusions), sponsorship transparency (кто платит, тот видим всем), payout cap 5:1 (нет гиперконцентрации призов), no anti-competitive tactics (нет блокировки конкурентов через правила мероприятия). Без этих правил один плохо организованный хакатон может подорвать репутацию всего направления #16. Мы честны про деньги и конкуренцию.

---

## §I — Worked examples (3-5 примеров правила в действии)

**I.1 API-key audit (угол 1 Operational, правило O-API).**

Сценарий: T3-контрибьютор добавляет скрипт интеграции, случайно оставляет `ANTHROPIC_API_KEY=sk-...` в коде.

Что происходит: pre-commit hook запускает `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|sk-ant-'` по staged files. Находит совпадение. Коммит блокируется. Lint output: `[F2-VIOLATION] O-API: API key detected in path tools/integration.py:14`. Contributor получает сообщение с инструкцией: убрать key → переменная окружения → повторить коммит.

Поучительное: ключ не попадает в git history. Нарушение зафиксировано в enforcement log (grade F2). Ruslan не получает alert (F2 — авто-блок, не эскалация). Правило сработало без человека.

**I.2 Конфликт → gate (угол 5 Governance, правило G-GATE).**

Сценарий: два члена cohort не сходятся во мнении по вопросу архитектуры Knowledge Base. Ситуация длится 3 дня, решение не принято.

Что происходит по правилу: конфликт не разрешается автономно агентами без human gate (Pillar C rule 7). После 3 дней без resolution → escalation trigger → AWAITING-APPROVAL packet создаётся → Ruslan review → решение фиксируется в D-Lock entry с ack-trail.

Поучительное: правило G-GATE не запрещает дискуссию — оно задаёт таймаут (3 дня без resolution = эскалация). Это предотвращает и зависание, и автономное «просто сделаем так».

**I.3 Fork-and-leave (угол 3 R12, правило R12-3).**

Сценарий: F-партнёр решает, что направление Jetix не совпадает с его планами. Хочет уйти и взять свою часть работы с собой.

Что происходит: Charter exit-процедура: (a) уведомление Ruslan; (b) расчёт fair share (QF-formula из Economic V10); (c) передача артефактов (fork-copy, не удаление из общего репозитория); (d) exit token выдаётся (Phase 2+ on-chain; сейчас — письменная фиксация в Charter amendment log); (e) уход без штрафа, без burn-bridge.

Что НЕ происходит: нет блокировки доступа до расчёта; нет скрытых «выходных fee»; нет удаления из cohort history (append-only: имя остаётся в contributor list).

Поучительное: правило R12-3 (fork-and-leave без штрафа) — это не риск для системы, это её конкурентное преимущество. Человек возвращается или рекомендует, зная что можно уйти по-честному.

**I.4 R12-checklist перед outreach (угол 3 R12, правило R12-5).**

Сценарий: sales-направление готовит партнёрское письмо для потенциального T2-ресурса.

Правило: 8 вопросов R12 = обязательный чеклист перед отправкой. Вопрос 7: «есть ли срочность/страх в сообщении?» Автор замечает: письмо содержит фразу «ограниченное число мест, следующий набор через год». Это — фейк-срочность.

Что происходит: письмо возвращается на revision. Фраза убирается. Checklist заново пройден. Теперь ответ «нет» на вопрос 7 — можно отправлять.

Поучительное: 8 вопросов R12 — это не бюрократия, это защита от drift. Письма со временем начинают содержать «стандартные маркетинговые элементы», которые незаметно становятся манипулятивными. Checklist останавливает drift.

**I.5 V4: Anti-dark-patterns check (угол anti-dark-patterns, Direction #15).**

Сценарий: дизайнер геймификации в Direction #15 предлагает leaderboard с публичным рейтингом активности всех участников. Идея: «это мотивирует».

Правило anti-dark-patterns (ADP-3): leaderboard без opt-out = social pressure mechanic. Проверка: есть ли возможность участнику скрыть свой результат из публичного рейтинга? Ответ: нет, leaderboard глобальный.

Что происходит: feature отправляется на revision. Варианты на выбор (R1): (a) leaderboard с opt-out как default; (b) leaderboard только внутри клана (не платформенный); (c) leaderboard только для хакатонов (explicit competition context), не для обычного участия. Influence-ethics-expert auto-pair: проверяет revision на манипулятивность до approval.

Поучительное: anti-dark-patterns ≠ «никакой геймификации». Правило различает intrinsic motivation support (achievement badges, progress visualization, skill trees) и extrinsic pressure mechanics (global rankings, social shame, FOMO countdowns). Первое — ok. Второе — нарушение.

**I.6 V4: Clan governance boundary (угол clan governance boundary, Direction #14).**

Сценарий: клан AI-инженеров хочет работать без weekly sync, используя async-only коммуникацию. Другой участник Jetix говорит: «это нарушает правила сообщества».

Правило clan governance boundary (CGB-1): расписание и формат работы = inner-clan freedom. Platform enforces: триада + R12 + уважение. Platform НЕ enforces: формат митингов, частоту синхронизации, внутренний язык коммуникации.

Что происходит: проверяется platform floor — async-only не нарушает ни триаду, ни R12, ни уважение к другим кланам. Решение: клан может работать async-only, это их право. Нет нарушения.

Поучительное: разграничение floor vs freedom — это не абстрактный принцип, это конкретный decision tree при любом конфликте про «так нельзя делать». Первый вопрос: это нарушение platform floor или просто отличие от другого клана? Если второе — это freedom, не нарушение.

---

## §J — R12 paired-frame check

Угол #9 «Правила» — один из R12-несущих направлений, потому что:
1. Угол 3 (R12 anti-extraction) — непосредственно R12 content
2. Угол 4 (Ethical) — influence/manipulation смежный домен
3. **V4: §V4-delta Anti-dark-patterns** — R12-HIGHEST (Direction #15 геймификация); любая работа по этому кластеру требует influence-ethics-expert paired-frame ОБЯЗАТЕЛЬНО

**Обязательный R12 paired-frame для этого направления:**

При написании, редактировании или публичной коммуникации по угол 3, угол 4 и V4-delta Anti-dark-patterns — автоматически задействуется influence-ethics-expert (auto-pair receiver per R12 discipline). Пропуск paired-frame = Halt-Log-Alert F4 ≤5s (Part 6b §I.2).

**Главный R12 anti-pattern для «Свода правил»:** правила как инструмент контроля vs правила как инфраструктура защиты.

Рабочая таблица проверки:

| Вопрос | Правила как контроль (BAD) | Правила как защита (GOOD) |
|---|---|---|
| ① Цена ≤ польза для участника? | Правила создают compliance-overhead без ценности | Правила убирают неопределённость, защищают участника |
| ② Конкретно? | «Мы ценим честность» (без enforcement) | «E-1: AI disclosure обязательно; violation = F4» |
| ③ Можно проверить? | «Мы всегда соблюдаем этику» | «Checklist R12 пройден? Лог есть?» |
| ④ Можно опровергнуть? | Принципы, которые нельзя нарушить по определению | Правила с явным violation-классом |
| ⑤ Доходчиво? | Юридический язык → участник не понимает | Простой язык + пример применения |
| ⑥ Источник прозрачен? | «Мы так решили» | «Pillar C rule 1 / Economic V10 §5.3 / D-Lock» |
| ⑦ Нет срочности/страха? | «Нарушишь — будешь исключён» (в публичном тексте) | Violation-процедура описана нейтрально, только факт |
| ⑧ Легко уйти? | Правила с lock-in (штрафы за уход, недоступность данных) | R12-3 fork-and-leave явно прописан в своде |

**V4-добавление в R12 check — anti-dark-patterns специфика:**

| Вопрос | ADP как manipulation tool (BAD) | ADP как честный стандарт (GOOD) |
|---|---|---|
| ADP-① Мотивация? | Внешняя: reward, rank, peer pressure | Внутренняя: прогресс, мастерство, смысл |
| ADP-② Opt-out? | Нет выхода из ratingloop без потери статуса | Opt-out из любого рейтинга — default доступен |
| ADP-③ Прозрачность механики? | Скрытые алгоритмы удержания | Все mechanics задокументированы публично |
| ADP-④ FOMO? | Countdown timers, «последний шанс», limited access | Доступ не искусственно ограничивается |
| ADP-⑤ Sunk-cost? | «Ты уже столько вложил, нельзя уходить» | Уход всегда доступен без штрафа за прошлые вложения |

**Anti-pattern «правила как контроль»** — конкретные сигналы:
- Правило сформулировано как «нельзя делать X» без объяснения зачем (Зачем обязателен в шаблоне)
- Violation-процедура публично сформулирована как угроза, а не как процедура
- Governance-правила ограничивают участника, но не ограничивают стратега/owner
- Правила меняются без 30-day opt-out (тихое изменение = non_consensual_distribution)

---

## §K — AI tooling integration

**Принцип:** AI enforces operational/quality rules (lint, hooks, рутина) → человек решает policy rules. Это прямое следствие Pillar C rule 1 (AI не принимает стратегических решений) и rule 9 (AI не self-модифицируется).

**K.1 AI-enforced сейчас (автоматически, no human needed):**

| Правило | Механизм | Trigger |
|---|---|---|
| O-1 YAML frontmatter | lint → fail-loud | pre-commit |
| O-2 Append-only | diff check → new records only at top | pre-commit |
| O-3 API-key audit | grep pattern match | pre-commit |
| O-5 Commit format | regex check on message | commit-msg hook |
| Q-1 F-G-R schema | shared/schemas/f-g-r.json validation | pre-promote |
| Q-4 No fake metrics | lint flag on claim without source | pre-publish |

**K.2 AI-assisted (AI флагирует, человек решает):**

| Правило | Механизм | Human action |
|---|---|---|
| R12-5 8 вопросов | checklist output + flag если ответ «да» на 7 | Ruslan / peer review |
| E-2 Манипуляция-check | influence-ethics-expert trigger | Content revision |
| G-GATE 3-day conflict | timer + escalation trigger | Ruslan review |
| M-2 Methodological claim | R-low/R-high suggestion | Author confirms |
| **ADP-all V4** | influence-ethics-expert paired-frame review | Feature revision |
| **EC-1 V4** | event checklist auto-run перед публикацией | Event organizer confirms |

**K.3 Human-only (AI не может, не должен):**

| Правило | Почему human-only |
|---|---|
| R12-1 Fair share calculation | Strategic decision (Pillar C rule 1) |
| G-STRAT Ruslan=стратег | Definitional: нельзя auto-enforce |
| Charter amendment | AWAITING-APPROVAL: требует Ruslan ack |
| Fork exit procedure | Financial + legal consequence |
| **CGB — Clan floor определение** | Архитектурное решение, требует AWAITING-APPROVAL |

**K.4 Machine-readable свод.**
Текущий substrate: `CLAUDE.md §4.1` + `.claude/config/default-deny-table.yaml` = machine-readable проекция 12 Pillar C rules + violation classes. V4-добавление: в default-deny-table.yaml добавляются 4 новых violation class:
- `addictive_loop_implementation` (F8) — Геймификация #15
- `fomo_pressure_tactic` (F4) — Геймификация #15
- `variable_reward_for_retention` (F4) — Геймификация #15
- `event_payout_cap_violation` (F2) — Хакатоны #16

Возможное расширение (R1): `shared/schemas/rules-manifest.yaml` со всеми ~61+V4 правилами в машиночитаемом виде + enforcement-type поле.

---

## §L — Partner-extension hook

При форке Jetix-системы партнёр получает свод правил. Какие обязательны, какие адаптируемы? V4 добавляет Anti-dark-patterns в mandatory.

**L.1 Mandatory-at-fork (R12/Ethical/Anti-dark-patterns = нельзя убирать):**

| Угол | Обязательность | Причина |
|---|---|---|
| 3 R12 anti-extraction | **MANDATORY** | Это основа доверия всей системы; убрать = не Jetix-fork |
| 4 Ethical (E-1 AI disclosure, E-2 no manipulation) | **MANDATORY** | Влияет на внешних участников; убрать = риск для реальных людей |
| R12-3 Fork-and-leave | **MANDATORY** | Это гарантия что форк сам не создаёт lock-in для своих участников |
| **V4: Anti-dark-patterns** | **MANDATORY** | Геймификационные манипуляции = extraction через психологию; убрать = нарушение духа R12 |

Нарушение mandatory-правил партнёром = fork_prevention_attempt class (если создаёт lock-in) или extraction_beyond_share (если нарушает R12/ADP). Это не наша юрисдикция в юридическом смысле, но это условие ассоциации с Jetix-брендом.

**L.2 Recommended (сохранить, но можно адаптировать):**

| Угол | Рекомендация | Что адаптируется |
|---|---|---|
| 5 Governance | Сохранить AWAITING-APPROVAL дисциплину + Stage Gates | Конкретные SG predicates, timing, threshold |
| 2 Methodological | Сохранить question-first + гипотезы | Конкретный формат M: / H: можно менять |
| 8 Financial | Сохранить принцип прозрачности модели | Конкретный split (75/25) — адаптируется под контекст |
| 10 Quality | Сохранить fail-loud + no fake metrics | Конкретные lint rules — адаптируются |
| **V4: Event conduct** | Сохранить transparency + payout cap | Конкретный cap (5:1 default) — адаптируется по формату |

**L.3 Адаптируемые полностью (operational/content):**

| Угол | Зачем адаптируемо |
|---|---|
| 1 Operational | Зависит от их stack (другой CI, другой VCS) |
| 6 Behavioral | Зависит от культуры команды |
| 7 Content | Зависит от их publication workflow |
| 9 Privacy | Зависит от их jurisdiction |
| **V4: Clan governance** | Inner-clan freedom по определению адаптируемо под каждый клан |

**R12-compliance для partner-fork:** при форке партнёр проходит R12-checklist (8 вопросов) применительно к своему своду. Вопрос 8 («легко уйти из форка?») должен иметь ответ «да» — иначе форк создаёт тот же lock-in, против которого R12 направлен. V4-добавление: вопрос 9 (неформальный): «есть ли в форке геймификационные механики удержания без opt-out?» — если да, mandatory revision.

**Partner onboarding документ:** отдельный артефакт (2-3 стр.) — «Rules fork guide»: mandatory/recommended/adaptable таблица + amendment process + R12-compliance checklist. Разрабатывается в Wave 3 при первом реальном партнёрском форке.

---

## §V4-delta — Новые кластеры правил V4

Это центральный новый раздел V4. Четыре кластера, каждый в полном шаблоне Утверждение→Зачем→Enforcement→Нарушение→Источник.

### §V4-1 Anti-dark-patterns правила (Геймификация #15, R12-HIGHEST)

Геймификация Direction #15 — наибольший R12-риск из всех 16 направлений. Механизм риска: геймификация технически может использовать психологические паттерны из игровой индустрии (variable rewards, streak mechanics, social comparison) для манипулятивного удержания участников. Это extraction через психологию, а не через финансы. По духу R12 anti-extraction — нарушение.

Ниже — спек кластера (R1: конкретные формулировки финализирует Ruslan):

**ADP-1: No addictive loops.**
Утверждение: геймификационные механики Jetix не строятся на переменном вознаграждении с целью создания психологической зависимости.
Зачем: переменное вознаграждение (variable ratio schedule) — самый мощный поведенческий conditioning механизм; его использование с целью удержания = манипуляция. Intrinsic motivation primacy = участник участвует потому что ценно, не потому что «подсел».
Enforcement: influence-ethics-expert paired-frame review для каждого нового геймификационного feature. AI-checklist: «является ли reward schedule variable для удержания?»
Нарушение: F8 grade (addictive_loop_implementation в default-deny-table.yaml) + halt + revision + Ruslan alert
Источник: R12 candidate rule 12 + CLAUDE.md §4.2 + influence-ethics-expert domain

**ADP-2: No FOMO pressure.**
Утверждение: Jetix не создаёт искусственный дефицит или временное давление как инструмент побуждения к участию.
Зачем: FOMO (fear of missing out) через countdown timers, «последний шанс», «ограниченный доступ» — это манипуляция страхом, не мотивация. Участник должен участвовать по желанию, не по давлению.
Enforcement: R12 вопрос 7 checklist перед любым публичным communication о событиях/возможностях. Фраза с дефицитом/давлением → automatic revision flag.
Нарушение: F4 grade (fomo_pressure_tactic) + revision
Источник: R12 8 вопросов #7 + угол 4 Ethical anti-manipulation

**ADP-3: Opt-out always available.**
Утверждение: любой рейтинг, leaderboard или social comparison механика в Jetix имеет opt-out как доступную опцию (по умолчанию или явно).
Зачем: участие в публичном сравнении — это выбор, не условие членства. Принудительная публичность = social pressure. Opt-out = уважение автономии.
Enforcement: design review перед внедрением любого leaderboard/ranking механизма. Вопрос: «есть ли opt-out?» Если нет — блок на внедрение.
Нарушение: F4 grade + feature revision до появления opt-out
Источник: угол 4 Ethical (consent) + R12 spirit

**ADP-4: No sunk-cost traps.**
Утверждение: Jetix не строит структуры, в которых уход участника наказывается потерей прошлых вложений (времени, репутации, материалов).
Зачем: sunk-cost trap — психологический механизм удержания через привязанность к прошлым инвестициям. Это форма manipulation, потому что решение «оставаться» принимается не на основе текущей ценности.
Enforcement: при любом изменении правил, статусов или уровней — проверка: теряет ли участник прошлые достижения при уходе? Если да — revision.
Нарушение: F4 grade + structural revision
Источник: R12-3 fork-and-leave + Economic V10 exit механики

**ADP-5: Intrinsic motivation primacy.**
Утверждение: дизайн геймификации в Jetix приоритизирует intrinsic motivation (прогресс, мастерство, смысл, автономия) над extrinsic (баллы, ранги, внешние награды как основной драйвер).
Зачем: SDT (Self-Determination Theory) показывает: extrinsic rewards при неправильном применении undermines intrinsic motivation. Цель Jetix — люди-мастера, не люди-зависимые от системы вознаграждений.
Enforcement: design review — соотношение intrinsic vs extrinsic mechanics в каждом feature. Флаг если extrinsic > 50% механики.
Нарушение: F4 grade + redesign рекомендация
Источник: gamification-engagement-expert domain + influence-ethics-expert paired-frame

**ADP-6: Public anti-dark-patterns commitment.**
Утверждение: Jetix публично коммитируется к anti-dark-patterns стандарту — это не внутреннее правило, это публичное обещание участникам и внешним наблюдателям.
Зачем: публичность commitment = accountability. Если обещание не выполняется — это не «внутренняя проблема», это нарушение публичного контракта. Это делает ADP-правила верифицируемыми внешне.
Enforcement: публикация ADP-6 на сайте/полке #15 + включение в R12-обещание публичный документ (#8)
Нарушение: нарушение ADP-1..ADP-5 после публичного commitment = нарушение публичного контракта + Halt-Log-Alert
Источник: R12 spirit + угол 4 Ethical + OpenAI Charter model (публичные commitments)

> **Paired-frame note:** весь §V4-1 Anti-dark-patterns — обязательный receiver для influence-ethics-expert. Разработка, review, изменение любого ADP-правила = auto-pair trigger. Пропуск = F4 Halt-Log-Alert.

### §V4-2 Event conduct правила (Хакатоны #16)

Direction #16 Хакатоны — events с конкуренцией, спонсорством, призами. Без явных правил события могут создавать репутационные риски (нечестная конкуренция, непрозрачное спонсорство, концентрация призов) или R12-нарушения.

**EC-1: Sponsorship transparency.**
Утверждение: все спонсоры хакатона раскрываются публично до старта события и их форма влияния на результаты явно ограничена.
Зачем: скрытое спонсорство = conflict of interest. Участник имеет право знать, кто финансирует событие и как это влияет на правила/критерии.
Enforcement: Event checklist перед публикацией: «спонсоры раскрыты?» + «влияние спонсора на результаты = 0 или явно задекларировано?»
Нарушение: F4 grade + публичная коррекция до старта; если уже началось → публичное исправление + лог
Источник: угол 4 Ethical + R12 вопрос 6 (источник прозрачен?) применительно к событиям

**EC-2: Payout cap 5:1.**
Утверждение: в хакатонах Jetix максимальный разрыв между первым и последним призом — не более 5:1.
Зачем: гиперконцентрация призов (winner-takes-all) создаёт tournament dynamics, где рациональная стратегия для большинства участников — не участвовать. 5:1 cap = распределение стимулов, поощряющее широкое участие.
Enforcement: prize structure review перед публикацией. Расчёт: max prize / min prize ≤ 5. Автоматический flag если превышено.
Нарушение: F2 grade (event_payout_cap_violation) + revision prize structure до публикации
Источник: Economic V10 QF distribution principles + R12 fair share spirit

**EC-3: Fair competition rules.**
Утверждение: правила хакатона не создают structurally unfair advantage для определённых участников (insider information, pre-access to criteria, team size disparities без категорий).
Зачем: fair competition = доверие участников. Нечестные правила — даже случайные — разрушают мотивацию и репутацию события.
Enforcement: peer review правил хакатона (минимум два T1-методолога) до публикации. Вопрос: «есть ли structural advantages?»
Нарушение: F2 grade + правило revision до публикации
Источник: угол 2 Methodological (question-first) + угол 4 Ethical

**EC-4: No anti-competitive exclusions.**
Утверждение: правила хакатона не используются для исключения конкурентов или для получения несправедливого рыночного преимущества через контроль результатов.
Зачем: хакатон как маркетинговый инструмент для создания barriersдругих — это манипуляция, не конкуренция. Jetix reputation ≠ anti-competitive tool.
Enforcement: правовой / этический review правил (R1: решается с юристом при масштабе; на ранних этапах — internal review)
Нарушение: F4 grade + revision + Ruslan alert
Источник: угол 4 Ethical + R12 anti-extraction spirit

**EC-5: Results transparency.**
Утверждение: критерии оценки на хакатоне публикуются до старта, результаты с обоснованием публикуются после.
Зачем: прозрачность результатов = accountability и обучение. Участники имеют право знать почему победил тот или иной проект.
Enforcement: Event checklist: «критерии опубликованы?» pre-event + «результаты с обоснованием опубликованы?» post-event
Нарушение: F2 grade + публикация недостающего
Источник: угол 10 Quality (no fake metrics) + угол 4 Ethical

### §V4-3 Inter-clan competition правила

При наличии нескольких кланов возникает inter-clan competition: за участников, за проекты, за ресурсы. Без правил это может создавать токсичную конкуренцию внутри платформы.

**ICC-1: No poaching.**
Утверждение: кланы Jetix не практикуют активный переманивание участников из других кланов через дискредитацию или скрытые оферты.
Зачем: здоровая конкуренция = лучший продукт/среда. Poaching через дискредитацию = разрушение trust в платформе целиком. Участник выбирает клан сам, не под давлением.
Enforcement: если участник сообщает о попытке переманивания через дискредитацию → formal complaint → Ruslan review → предупреждение клану
Нарушение: F4 grade при подтверждении + warning; повторное = discussion о выходе клана из платформы
Источник: угол 4 Ethical + угол 6 Behavioral + R12 spirit (respect as foundation)

**ICC-2: No sabotage.**
Утверждение: кланы Jetix не саботируют работу других кланов: не распространяют ложную информацию, не вмешиваются в проекты, не перехватывают ресурсы нечестными методами.
Зачем: кланы работают в shared ecosystem. Sabotage одного клана = ущерб платформе целиком. Это anti-commons поведение.
Enforcement: formal complaint process + Ruslan review; серьёзное нарушение = halt на клановой активности до разбора
Нарушение: F8 grade при явном саботаже + halt + Ruslan decision
Источник: угол 5 Governance (конфликт → gate) + Pillar C rule 7

**ICC-3: Respectful competition framing.**
Утверждение: кланы, конкурирующие за участников или ресурсы, коммуницируют свои преимущества без дискредитации конкурентов.
Зачем: compete on merit, not on dirt. Это и этический, и практический принцип: дискредитация → культура токсичности → уход лучших участников из платформы целиком.
Enforcement: public communication review при заметных inter-clan communications. AI-flag: дискредитирующие формулировки.
Нарушение: F2 grade + revision коммуникации
Источник: угол 4 Ethical + угол 6 Behavioral

**ICC-4: Dispute resolution.**
Утверждение: конфликты между кланами разрешаются через formal dispute process, а не через эскалацию или публичное давление.
Зачем: кланы — автономные единицы, но они в shared space. Dispute process = protect autonomy while maintaining shared peace.
Enforcement: G-GATE mechanism применяется к inter-clan конфликтам: 3 дня без resolution → escalation → Ruslan review → D-Lock entry
Нарушение: F4 grade за пропуск процесса и прямую эскалацию
Источник: угол 5 Governance G-GATE + Pillar C rule 7

### §V4-4 Clan governance boundary (ключевое V4-различие)

Это самое важное V4-разграничение в Direction #9. Без него участники и кланы не понимают: что платформа от них требует vs что они решают сами. Страх «нас будут контролировать» = нет ясности об этой границе.

**CGB-0: Принцип разграничения (мета-правило для клан governance).**
Утверждение: Jetix enforces platform floor (минимальный стандарт для всех кланов) и НЕ вмешивается в inner-clan freedom (всё, что не нарушает floor).
Зачем: без этого разграничения платформа либо тоталитарна (всё контролирует) либо хаотична (ничего не контролирует). Floor+Freedom = minimum viable trust + maximum viable autonomy.
Enforcement: clan governance boundary template (§F.5) + clan charter review при создании клана
Нарушение: нет, это мета-правило. Нарушением является попытка платформы вмешиваться в inner-clan freedom (это нарушение CGB-0 самой платформой).
Источник: Pillar C Tier-2 + R12 spirit + FPF constitutional design

**CGB-1: Platform floor — что enforced.**
Утверждение: platform floor для всех кланов включает три элемента: (a) ценностная триада (Мастерская + Мастерство + Сеть); (b) R12 anti-extraction rules (нельзя убрать для своих участников); (c) уважение к другим кланам (ICC-правила).
Зачем: это минимум для того, чтобы платформа оставалась trustworthy для всех. Клан, нарушающий floor, разрушает доверие не только к себе, но к Jetix целиком.
Enforcement: clan charter review + periodic compliance check (R1: частота определяется Ruslan)
Нарушение: F4/F8 grade в зависимости от типа нарушения + escalation → Ruslan decision о судьбе клана
Источник: Foundation ценностная триада + R12 (CLAUDE.md §4.1 rule 12) + ICC-правила §V4-3

**CGB-2: Inner-clan freedom — что НЕ enforced платформой.**
Утверждение: кланы самостоятельно определяют: методы работы, темы и домены, стиль управления, расписание, внутренний язык коммуникации, внутренние reward/recognition системы (при условии ADP-compliance), состав — кого принимать, как онбордить.
Зачем: автономия клана = его конкурентное преимущество. Разные кланы экспериментируют с разными подходами → платформа обучается через diversity. Клан не должен спрашивать разрешения у платформы на каждое операционное решение.
Enforcement: нет (это свобода, не обязанность). Исключение: если inner-clan решение нарушает platform floor → переходит в нарушение CGB-1.
Нарушение: N/A — это свобода
Источник: FPF inner-clan autonomy principles + R12-3 spirit (fork-and-leave = право на самоопределение)

**CGB-3: Gray zone — как определять.**
Утверждение: при неопределённости («это floor или freedom?») действует следующий decision tree: (a) нарушает ли R12 anti-extraction? → floor; (b) нарушает ли уважение к другим кланам? → floor; (c) нарушает ли ценностную триаду? → floor; (d) всё остальное → inner-clan freedom.
Зачем: gray zone создаёт тревогу и конфликты. Explicit decision tree = предсказуемость.
Enforcement: clan disputes о gray zone → G-GATE process → Ruslan arbitration → D-Lock entry с прецедентом для будущего
Нарушение: N/A — это процедура, не правило с violation
Источник: Part 9 Owner Interaction Scaffold + Part 4 Coordination Protocol

**CGB-4: Floor vs Freedom публичная коммуникация.**
Утверждение: разграничение platform floor vs inner-clan freedom явно публикуется в публичных документах Jetix — не только во внутренних.
Зачем: потенциальный участник при выборе платформы должен знать: что от него требует платформа vs что он решает с кланом. Прозрачность этой границы = доверие.
Enforcement: публикация CGB-0..CGB-3 summary на сайте/полке #9 + в Direction #14 Кланы документации
Нарушение: отсутствие публикации = нарушение угла 4 Ethical (E-прозрачность) + F2 grade
Источник: R12 вопрос 3 (можно ли проверить?) + угол 4 Ethical

---

## R12 section — итоговый check (V4)

**Объект:** Direction #9 «Правила работы» V4 как целое.

8 вопросов применительно к самому документу-своду + V4-delta:

1. **Цена ≤ польза?** Да: свод убирает неопределённость для участников и партнёров; compliance-overhead минимален за счёт AI-автоматизации; V4-delta добавляет ценность для участников #15/#16/кланов.
2. **Конкретно?** Да: каждое правило — шаблон с 5 элементами; V4-delta столь же конкретны; нет абстрактных «ценностей».
3. **Можно проверить?** Да: lint / enforcement log / violation report → верифицируемо. V4: clan compliance check + event checklist = дополнительные верификационные механизмы.
4. **Можно опровергнуть?** Да: каждое правило имеет violation-класс → falsifiable. ADP-правила имеют explicit grade F4/F8.
5. **Доходчиво?** Требует работы: long-form ≤4K должен быть написан простым языком, не Foundation-jargon. V4-delta требует дополнительного глоссария (addictive loop, FOMO, sunk-cost — для нетехнической аудитории).
6. **Источник прозрачен?** Да: поле Источник обязательно в шаблоне (Pillar C / Economic V10 / D-Lock / R12 8 вопросов). V4-delta: добавлены ссылки на gamification-engagement-expert и influence-ethics-expert domains.
7. **Нет срочности/страха?** Требует внимания при написании violation-процедур: нейтральный тон, не угрожающий. Особенно важно для ICC-правил (inter-clan competition) — тон должен быть «process», не «punishment».
8. **Легко уйти?** Да: R12-3 fork-and-leave явно в угол 3; mandatory при любом форке. V4: CGB-2 inner-clan freedom включает право клана уйти с платформы (exit procedure по аналогии с R12-3 fork-and-leave — детали R1).

**Итог V4:** структура свода R12-compliant по архитектуре. V4-delta добавляет R12-несущие правила (ADP) и операционные стандарты (EC, ICC, CGB). Ключевые риск-точки при исполнении: тон violation-процедур в ICC-правилах (§V4-3) — нейтральный, не репрессивный; и ясность CGB gray zone decision tree (§V4-4 CGB-3) — нужны реальные примеры при написании финального текста.

---

## Закрытие (V4)

Direction #9 «Правила работы» V4 — наиболее инфраструктурное направление из 16. Оно не производит новый контент для аудитории напрямую — оно делает все остальные 15 направлений trustworthy. Свод правил без enforcement = манифест. Свод с enforcement = архитектура доверия.

V4 добавляет четыре принципиально новых кластера: anti-dark-patterns для самого высокого R12-риска (Геймификация #15), event conduct для хакатонов (#16), inter-clan competition для многокланового мира, и clan governance boundary — самое важное новое различие для понимания того, что платформа требует, а что оставляет кланам.

Главные R1-решения до начала написания (V3-baseline сохраняется, V4 добавляет):
1. **Формат свода:** единый документ (John Lewis) ИЛИ 10+ страниц per угол (Apple HIG)? V4-delta = отдельные страницы в любом случае.
2. **Публичная/внутренняя граница:** согласна ли таблица §11 из Phase 3 spec + V4-delta (ADP = public)?
3. **Когда писать:** Wave 2 (R12-угол + ADP) ИЛИ Wave 3 (полный свод)?
4. **Violation-процедуры наружу:** показывать публично enforcement-градиент (F2/F4/F8) или только принципы?
5. **Machine-readable расширение:** добавить 4 V4 violation classes в default-deny-table.yaml?
6. **V4-new: Clan governance boundary документ:** отдельная страница или раздел в Charter?
7. **V4-new: ADP public commitment:** когда публиковать — вместе с #15 или отдельно?

Substrate для написания уже есть полностью: Pillar C Tier-2 12 rules (CLAUDE.md §4.1) + Global Rules + AWAITING-APPROVAL discipline + R12 8 вопросов (EXECUTION-PLAN) + Economic V10 (5:1, QF, fork-and-leave) + default-deny-table.yaml (violation classes) + gamification-engagement-expert и influence-ethics-expert domains (V4-delta ADP) + Direction #14 Кланы lifecycle + Direction #15 Геймификация + Direction #16 Хакатоны.

---

*Direction #9 V4 closure. Rules document portfolio spec: 10 углов (~61 правило V3) + 4 V4-delta кластера (~20 правил), 12 основных арtefacts (§A..§L) + §V4-delta, R12 paired-frame STRICT (углы 3/4 + §V4-delta anti-dark-patterns + influence-ethics auto-pair). Public/internal разметка per угол. 7 R1-решений до исполнения (5 V3 + 2 V4-new). Жанр-референс: Apple HIG + John Lewis Constitution + OpenAI Charter. R11 — спека, NO sample свод. IP-1 STRICT. Источники: Pillar C Tier-2 / CLAUDE.md §4.1 / 04-rules-document-spec.md (Phase 3) / Economic V10 / EXECUTION-PLAN / gamification-engagement-expert domain / influence-ethics-expert domain.*
