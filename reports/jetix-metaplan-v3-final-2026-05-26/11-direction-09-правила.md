---
title: "MetaPlan V3 — Direction #9: Правила работы (портфельный спек)"
date: 2026-05-26
type: phase-report-metaplan-v3
phase: 10
direction: 9
F: F2-F3
language: russian
status: draft-report
prose_authored_by: brigadier-scribe (R1 surface — Ruslan authors final integration)
constitutional_posture: R1 surface only + R2 STRICT (Pillar C LOCKED preserved) + R11 + R12 paired-frame STRICT + IP-1 STRICT
predecessors:
  - decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-V2-2026-05-25.md (§3)
  - reports/jetix-public-docs-metaplan-v2-2026-05-25/04-rules-document-spec.md
  - CLAUDE.md §4.1 (12 hard rules — Pillar C Tier-2)
  - swarm/wiki/foundations/principles/architecture.md
---

# Direction #9 — 📋 Правила работы: портфельный спек

## Введение: грань Foundation, позиция в метаплане, зачем это направление

Jetix — мега-мастерская мирового уровня. Три грани Foundation: **Мастерская** (ГДЕ — пространство, зоны, инфраструктура) · **Мастерство** (ЧТО прокачивают — репертуар методов, мета-метод, фронтир) · **Сеть** (КАК распределено — mesh cells, pooling ресурсов, fork-and-leave). One-liner: «Jetix — мега-мастерская мирового уровня: место, где люди становятся мастерами в эпоху AI, вместе двигают фронтир и не дают системе доить или запирать себя».

Direction #9 «Правила работы» — это **операционка всех трёх граней**: как ставить станок, как пулить ресурс, как форкнуть. Без правил мастерская превращается в хаос, мастерство — в произвол, сеть — в конфликт. При этом правило без enforcement и без процедуры нарушения — это пожелание, не правило. Именно это отличает Jetix-свод от типичного «манифеста с ценностями».

**Позиция в хабовой структуре.** #9 связан с хабом #8 R12 (правила — это enforcement-обёртка обещания), с #10 Ценности (каждое правило — ценность, ставшая операциональной), с #1 Метод (методологическая дисциплина). GAP текущего состояния: ⚠️ partial — правила существуют (Pillar C Tier-2, CLAUDE.md §4, Global Rules, AWAITING-APPROVAL discipline), но разбросаны по Foundation-документам; публичная vs внутренняя граница — R1.

**Мета-правило (главный принцип свода):** правило без enforcement и процедуры нарушения = пожелание, не правило.

**Формат каждого правила:** Утверждение → Зачем → Enforcement → Нарушение → Источник.

**10 углов, ~61 правило:**

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

~25-30 публичных + ~30 внутренних. Жанр-референс: **Apple HIG** (свод как стандарт дизайна) + **John Lewis Constitution** (правила как основа доверия сообщества) + **OpenAI Charter** (конституционный commitment перед внешним миром).

> **R1:** все формулировки ниже — варианты/опции для рассмотрения. Финальные решения за Ruslan.
> **R2 STRICT:** Pillar C LOCKED — ссылки, не правки.
> **R11:** ниже — описание ЧЕГО содержит каждый документ, не сам публичный текст.
> **IP-1 STRICT:** имена = role-type примеры (T1-методолог, T3-контрибьютор, F-партнёр и т.д.).

---

## §A — Главный документ «Свод правил»

### A.1 One-pager «Зачем нам правила» (≤500 слов, публичный)

**Аудитория.** Потенциальный участник, партнёр (T1/T2), журналист, инвестор. Человек, который видит название «Свод правил» и у которого возникает ощущение «бюрократия» или «манифест».

**Задача.** Сдвинуть восприятие: правила — это защита, не контроль. Правила — это то, что делает мастерскую безопасной для честной работы, а не инструмент власти.

**Разделы one-pager:**
1. **Почему правила — это не про контроль.** Один абзац: мета-правило (правило без enforcement = пожелание); что это означает для участника — что каждое обязательство реально.
2. **Структура: 10 углов.** Краткая карта — что публично (R12-обещание / Метод / Этика / Финансовая модель) и что внутреннее (операции / качество / контент / поведение). Честное разделение.
3. **Главные обещания наружу.** 3-4 пункта из публичных углов: не доим (R12-1), можно уйти с долей (R12-3), AI раскрываем (E-1), финансовая модель открыта (F-1).
4. **Где читать подробнее.** CTA: R12-обещание → полка #8; Governance → Charter; Метод → Direction #1.

**Формат.** Markdown-источник → лендинг-секция + PDF (A4). Три варианта заголовка на выбор Ruslan: (a) «Правила как защита, не как контроль» (b) «Что мы обязуемся делать и не делать» (c) «10 углов: полный свод».

### A.2 Long-form свод (≤4K слов спек)

**Главный вопрос R1 (Ruslan выбирает до написания):** единый документ — один файл ~4K (John Lewis Constitution) ИЛИ 10 страниц per угол (Apple HIG-разделы, каждая ~400 слов)?

**Аргументы за единый:** проще как коммитмент, проще ссылаться («§3 R12»), психологически весомее. **Аргументы за 10 страниц:** проще обновлять по-угольно, легче фильтровать public/internal, удобнее для partner-fork (берут нужные углы).

**Структура long-form (оба варианта включают):**
- §0 Мета-правило и формат шаблона (обязательный вводный блок)
- §1–§10 Каждый угол: список правил в шаблоне Утверждение→Зачем→Enforcement→Нарушение→Источник
- §11 Сводная карта public/internal
- §12 Violation-классы и enforcement-градиент (F2/F4/F8 из Part 6b)
- §Appendix Источники (Pillar C Tier-2 ссылки, Economic V10, EXECUTION-PLAN)

**Public/internal разметка:** каждое правило помечается тегом `[public]` / `[internal]` / `[partner]`. Публичная версия = фильтр только `[public]` — это то, что идёт на сайт/полку #9. Internal версия = полный свод для onboarding.

**Enforcement-градиент (из Part 6b §I.2):**
- F8 grade: остановка ≤1s + Halt-Log-Alert (extraction_beyond_share, fork_prevention_attempt и др.)
- F4 grade: ≤5s (пропуск R12-checklist, missing paired-frame)
- F2 grade: ≤60s (frontmatter missing, commit без area-prefix)

---

## §B — Видео

Для «Свода правил» видео в обычном смысле (YouTube-ролик, курс) **не является приоритетным артефактом**. Правила — это документ-референс, не нарратив. Однако возможны два мини-сценария:

**B.1 Orientation clip (3-5 мин, опционально).** Для cohort onboarding: кто-то из T1-методологов объясняет мета-правило и структуру 10 углов. Не заменяет документ — дополняет для тех, кто не читает до онбординга. Формат: screenshare + голос, не продакшн-видео.

**B.2 R12-обещание clip.** Если Direction #8 R12/Обещание делает своё видео — правила угла 3 и 4 туда вставляются как shared block. Правила #9 как самостоятельного видео-направления — defer до Wave 3+.

**R1:** нужен ли orientation clip — Ruslan решает после Wave 2 cohort-feedback.

---

## §C — Курс / Onboarding rules module

Правила — не самостоятельный курс, но **обязательный модуль в двух местах:**

**C.1 Cohort onboarding (первый день).** Модуль «Как мы работаем»: мета-правило → 10 углов (обзор 15 мин) → практика: заполнить frontmatter-шаблон + сделать пробный commit → consent gate (подтвердить R12-3 понял). Delivery: синхронно или async через checklist.

**C.2 Partner onboarding.** Отдельный трек: какие правила обязательны при форке (R12/Ethical = mandatory), какие адаптируемы (Operational/Content). Ссылка на §L (Partner-extension hook).

**C.3 AI-agent onboarding.** Текущее состояние: CLAUDE.md §4.1 (12 hard rules Pillar C) + default-deny-table.yaml. В рамках direction #9 это не новый артефакт — это документирование существующего как «machine-readable модуль правил».

**Что НЕ строим здесь:** полноценный e-learning курс с LMS — defer до Wave 3, зависит от Direction #7 Образование.

---

## §D — Книга

Книга по «Своду правил» как отдельный артефакт — **не релевантна**. Правила — это живой операционный документ, не нарратив для книги. Единственный сценарий, где правила попадают в книгу — это глава в более широкой книге о Jetix-методе (Direction #1 или #6 Vision). Там угол R12 anti-extraction и угол Governance могут составить отдельную главу «Почему правила — это инфраструктура свободы».

**R1:** если Ruslan планирует книгу по Jetix — правила направления #3/#4/#5 (governance + extraction) → одна глава «The Rules That Protect, Not Control».

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
Этот шаблон = единица свода. Все ~61 правило записаны в нём.

**F.2 Enforcement log template.**
Формат записи в swarm/approvals/log.jsonl при F4/F8 нарушении:
```json
{
  "ts": "ISO-8601",
  "rule_id": "R12-1 / O-3 / Q-5 ...",
  "grade": "F8 / F4 / F2",
  "violation_class": "extraction_beyond_share / ...",
  "action_taken": "halt / revision / alert",
  "resolved_by": "Ruslan / auto-lint / ...",
  "notes": ""
}
```

**F.3 Violation report template.**
При нарушении F4/F8 — краткий отчёт (до 10 строк): что нарушено, когда, кем (role-type, не executor per IP-1), как разрешено, изменилось ли правило по итогу.

**F.4 Charter amendment template.**
При изменении любого public-правила (особенно R12/Governance): AWAITING-APPROVAL packet → 30-day opt-out window → re-ack process → обновление свода + лог.

---

## §G — Презентация (10-20 слайдов)

**Назначение.** Объяснить структуру 10 углов команде, партнёрам, новым участникам cohort. Не маркетинг — навигация.

**Структура (12 слайдов):**

1. **Слайд 1.** Заголовок + мета-правило: «Правило без enforcement = пожелание». Почему это важно.
2. **Слайд 2.** Схема: мега-мастерская → 3 грани → правила как операционка всех трёх.
3. **Слайд 3.** 10 углов — дерево (Operational/Methodological/R12/Ethical/Governance/Behavioral/Content/Financial/Privacy/Quality). Раскраска: public (зелёный) / internal (серый) / смешанно (жёлтый).
4. **Слайды 4-6.** Публичные углы (R12 / Ethical / Methodological / Financial-модель): по одному слайду на 2 угла. Ключевые правила — не полный список, а «зачем это публично».
5. **Слайды 7-9.** Внутренние углы (Operational / Content / Quality / Behavioral): аналогично, зачем это внутреннее.
6. **Слайд 10.** Governance-угол отдельно: Ruslan=стратег + AWAITING-APPROVAL + Stage Gates + 1-голос. Это и public и internal одновременно.
7. **Слайд 11.** Enforcement-градиент: F8/F4/F2 — что за что.
8. **Слайд 12.** CTA: где читать полный свод (публичная часть → полка #9; партнёрская → Charter; machine-readable → CLAUDE.md §4.1).

**Референс по стилю.** Apple WWDC engineering session: без декоративности, максимум схем и таблиц, минимум bullet points.

---

## §H — FAQ (10-20 вопросов, честные ответы)

**H.1 «Зачем столько правил? 61 — это много.»**
61 звучит много, но ~30 из них internal — партнёр/участник их не читает, это наша операционная гигиена. Публичных ~25-30. И каждое правило маленькое: одна фраза + зачем + что будет. Это не юридический договор — это навигация.

**H.2 «Кто следит за выполнением?»**
Три уровня: (a) машина — lint, pre-commit hooks, Halt-Log-Alert автоматически на F4/F8; (b) peer-review в cohort — для Methodological и Ethical; (c) Ruslan — для Governance и архитектурных решений. Нет «полиции правил» — есть встроенные механизмы.

**H.3 «Правила можно менять?»**
Да, через Charter amendment process: AWAITING-APPROVAL + 30-day opt-out window + re-ack. Это не бюрократия — это гарантия, что изменение правил не происходит тихо и без согласия участников.

**H.4 «Что будет, если нарушить?»**
Зависит от класса нарушения. F8 (extraction_beyond_share, fork_prevention) — немедленный halt + alert. F4 (пропуск R12-checklist) — возврат на revision ≤5s. F2 (frontmatter missing) — lint failure, коммит блокируется. Violation log пишется всегда.

**H.5 «Правила R12 — это реально или только декларация?»**
Реально ровно настолько, насколько enforcement механизм реален. Сейчас: manual checklist + gate + Halt-Log-Alert. Phase 2+: on-chain smart-contract (Ethereum substrate, per §4.2 RUSLAN-LAYER). Мы честны: Phase 2+ = будущее, не настоящее.

**H.6 «Это как манифест стартапа — напишете и забудете?»**
Анти-паттерн, который мы знаем. Именно поэтому мета-правило стоит первым: без enforcement = пожелание. Свод живёт пока работают enforcement-механизмы. Если механизм сломан → правило помечается как INACTIVE, не удаляется (append-only discipline).

**H.7 «Могу ли я форкнуть и взять только часть правил?»**
Да, это явно предусмотрено. Угол R12 и Ethical — mandatory при форке. Operational и Content — адаптируемы. Governance — рекомендуем сохранить AWAITING-APPROVAL дисциплину, но можно адаптировать под свою org. Детали в §L (Partner-extension hook).

**H.8 «Правило "AI не принимает стратегических решений" — что это значит на практике?»**
AI генерирует варианты, surfaces options, drafts. Любая strategic prose должна быть authored Ruslan или hybrid-with-ack-trail. Если AI написал стратегический документ без ack-trail — это нарушение Pillar C rule 1 (F4 grade). На практике: каждый ключевой документ имеет `prose_authored_by:` в frontmatter.

**H.9 «Правила звучат как что-то для больших компаний. Зачем это маленькой мастерской?»**
Потому что доверие строится до масштаба, а не после. Партнёр T1-методолог, который приходит сейчас, смотрит: «есть ли структура или будет хаос при росте?». Правила — это архитектура доверия, не бюрократия.

**H.10 «Что такое "правило без enforcement = пожелание"?»**
Это главный принцип, зафиксированный в §0 свода. Смысл: если написано «мы не доим участников», но нет механизма проверки и нет последствия при нарушении — это просто фраза. Enforcement делает правило реальным. Именно поэтому каждое из ~61 правил имеет обязательное поле Enforcement.

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

---

## §J — R12 paired-frame check

Угол #9 «Правила» — один из R12-несущих направлений, потому что:
1. Угол 3 (R12 anti-extraction) — непосредственно R12 content
2. Угол 4 (Ethical) — influence/manipulation смежный домен

**Обязательный R12 paired-frame для этого направления:**

При написании, редактировании или публичной коммуникации по угол 3 и угол 4 — автоматически задействуется influence-ethics-expert (auto-pair receiver per R12 discipline). Пропуск paired-frame = Halt-Log-Alert F4 ≤5s (Part 6b §I.2).

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

**K.3 Human-only (AI не может, не должен):**

| Правило | Почему human-only |
|---|---|
| R12-1 Fair share calculation | Strategic decision (Pillar C rule 1) |
| G-STRAT Ruslan=стратег | Definitional: нельзя auto-enforce |
| Charter amendment | AWAITING-APPROVAL: требует Ruslan ack |
| Fork exit procedure | Financial + legal consequence |

**K.4 Machine-readable свод.**
Текущий substrate: `CLAUDE.md §4.1` + `.claude/config/default-deny-table.yaml` = machine-readable проекция 12 Pillar C rules + violation classes. Direction #9 не создаёт новый machine-readable файл — она документирует и структурирует уже существующий. Возможное расширение (R1): `shared/schemas/rules-manifest.yaml` со всеми ~61 правилами в машиночитаемом виде + enforcement-type поле.

---

## §L — Partner-extension hook

При форке Jetix-системы партнёр получает свод правил. Какие обязательны, какие адаптируемы?

**L.1 Mandatory-at-fork (R12/Ethical = нельзя убирать):**

| Угол | Обязательность | Причина |
|---|---|---|
| 3 R12 anti-extraction | **MANDATORY** | Это основа доверия всей системы; убрать = не Jetix-fork |
| 4 Ethical (E-1 AI disclosure, E-2 no manipulation) | **MANDATORY** | Влияет на внешних участников; убрать = риск для реальных людей |
| R12-3 Fork-and-leave | **MANDATORY** | Это гарантия что форк сам не создаёт lock-in для своих участников |

Нарушение mandatory-правил партнёром = fork_prevention_attempt class (если создаёт lock-in) или extraction_beyond_share (если нарушает R12). Это не наша юрисдикция в юридическом смысле, но это условие ассоциации с Jetix-брендом.

**L.2 Recommended (сохранить, но можно адаптировать):**

| Угол | Рекомендация | Что адаптируется |
|---|---|---|
| 5 Governance | Сохранить AWAITING-APPROVAL дисциплину + Stage Gates | Конкретные SG predicates, timing, threshold |
| 2 Methodological | Сохранить question-first + гипотезы | Конкретный формат M: / H: можно менять |
| 8 Financial | Сохранить принцип прозрачности модели | Конкретный split (75/25) — адаптируется под контекст |
| 10 Quality | Сохранить fail-loud + no fake metrics | Конкретные lint rules — адаптируются |

**L.3 Адаптируемые полностью (operational/content):**

| Угол | Зачем адаптируемо |
|---|---|
| 1 Operational | Зависит от их stack (другой CI, другой VCS) |
| 6 Behavioral | Зависит от культуры команды |
| 7 Content | Зависит от их publication workflow |
| 9 Privacy | Зависит от их jurisdiction |

**R12-compliance для partner-fork:** при форке партнёр проходит R12-checklist (8 вопросов) применительно к своему своду. Вопрос 8 («легко уйти из форка?») должен иметь ответ «да» — иначе форк создаёт тот же lock-in, против которого R12 направлен.

**Partner onboarding документ:** отдельный артефакт (2-3 стр.) — «Rules fork guide»: mandatory/recommended/adaptable таблица + amendment process + R12-compliance checklist. Разрабатывается в Wave 3 при первом реальном партнёрском форке.

---

## R12 section — итоговый check

**Объект:** Direction #9 «Правила работы» как целое.

8 вопросов применительно к самому документу-своду:

1. **Цена ≤ польза?** Да: свод убирает неопределённость для участников и партнёров; compliance-overhead минимален за счёт AI-автоматизации.
2. **Конкретно?** Да: каждое правило — шаблон с 5 элементами; нет абстрактных «ценностей».
3. **Можно проверить?** Да: lint / enforcement log / violation report → верифицируемо.
4. **Можно опровергнуть?** Да: каждое правило имеет violation-класс → falsifiable.
5. **Доходчиво?** Требует работы: long-form ≤4K должен быть написан простым языком, не Foundation-jargon.
6. **Источник прозрачен?** Да: поле Источник обязательно в шаблоне (Pillar C / Economic V10 / D-Lock).
7. **Нет срочности/страха?** Требует внимания при написании violation-процедур: нейтральный тон, не угрожающий.
8. **Легко уйти?** Да: R12-3 fork-and-leave явно в угол 3; mandatory при любом форке.

**Итог:** структура свода R12-compliant по архитектуре. Риск-точки при исполнении: тон violation-процедур (п.7) и доходчивость long-form (п.5). Оба — решаемы на уровне редактуры при написании.

---

## Закрытие

Direction #9 «Правила работы» — наиболее инфраструктурное направление из 14. Оно не производит новый контент для аудитории напрямую — оно делает все остальные 13 направлений trustworthy. Свод правил без enforcement = манифест. Свод с enforcement = архитектура доверия.

Главные R1-решения до начала написания:
1. **Формат свода:** единый документ (John Lewis) ИЛИ 10 страниц per угол (Apple HIG)?
2. **Публичная/внутренняя граница:** согласна ли таблица §11 из Phase 3 spec (04-rules-document-spec.md)?
3. **Когда писать:** Wave 2 (сейчас R12-угол) ИЛИ Wave 3 (полный свод)?
4. **Violation-процедуры наружу:** показывать публично enforcement-градиент (F2/F4/F8) или только принципы?
5. **Machine-readable расширение:** нужен ли `shared/schemas/rules-manifest.yaml` или CLAUDE.md §4.1 + default-deny-table.yaml достаточно?

Substrate для написания уже есть полностью: Pillar C Tier-2 12 rules (CLAUDE.md §4.1) + Global Rules + AWAITING-APPROVAL discipline + R12 8 вопросов (EXECUTION-PLAN) + Economic V10 (5:1, QF, fork-and-leave) + default-deny-table.yaml (violation classes). Свод = человеческая проекция разбросанного substrate в один читаемый документ.

---

*Direction #9 closure. Rules document portfolio spec: 10 углов (~61 правило), 12 арtefacts (§A..§L), R12 paired-frame STRICT (углы 3/4 + influence-ethics auto-pair). Public/internal разметка per угол. 5 R1-решений до исполнения. Жанр-референс: Apple HIG + John Lewis Constitution + OpenAI Charter. R11 — спека, NO sample свод. IP-1 STRICT. Источники: Pillar C Tier-2 / CLAUDE.md §4.1 / 04-rules-document-spec.md (Phase 3) / Economic V10 / EXECUTION-PLAN.*
