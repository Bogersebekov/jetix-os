---
title: Phase 10 — ⚖️💰 Юр + Бизнес-счёт + invoice spec (combined foundational)
date: 2026-05-25
type: phase-report-artefact-spec
parent_main: decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-build-artefacts-specs-2026-05-25
R: low
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame + IP-1 STRICT + append-only
language: russian primary
phase: 10
artefact: legal-finance-foundational
primary_audience: Self (foundational) + downstream партнёры
---

# ⚖️💰 Phase 10 — Спека Юр + Бизнес-счёт + invoice (combined foundational)

> **Что это.** Чертёж foundational-блока: что спросить у Steuerberater, какую матрицу выбора
> форм подготовить, что в контракт-template, какой invoice + bookkeeping-минимум. НЕ юр-совет и
> НЕ заполненные значения — конкретика появляется **после консультации Steuerberater** (R1).
>
> **Дисциплина F3:** мы НЕ добываем нового юр-research про немецкие формы (это сделает
> Steuerberater). Мы специфицируем **вопросы и каркас матрицы**, чтобы Ruslan пришёл на
> консультацию подготовленным. Значения = R-low до консультации. [src: prompt §Phase 10 + §7
> F3 derivative — F2, R-high]

---

## 1. Назначение (one-liner)

Foundational-комплект из 4 под-артефактов (email Steuerberater'у + матрица Einzel/GmbH/UG +
контракт-template + invoice + bookkeeping-минимум), который выводит Ruslan в состояние «есть
легальный базис принимать деньги и оформлять партнёрства» к Build exit.

## 2. Цель (поведенческая)

К Build exit Ruslan имеет: (a) юр-форма выбрана и регистрация в процессе, (b) бизнес-счёт
открыт, (c) invoice-template готов отправить, (d) bookkeeping-минимум настроен. Целевое
поведение — не «понял про формы», а **email Steuerberater'у готов отправить + матрица позволяет
prep-решение до консультации**. [src: prompt Phase 10 цель + Platform Lifecycle §6 «юр+счёт
начинаем» — F2-F3, R-med]

## 3. Primary audience (умный партнёр)

**Self (foundational)** + downstream партнёры (которые должны видеть «эти ребята с легальным
базисом»).
- **Зачем партнёрам:** методолог/инвестор не зайдёт в структуру без легального базиса; контракт-
  template сигналит «серьёзно».
- **Что отпугнёт партнёра:** контракт с lock-in clauses; отсутствие fork-and-leave в контракте;
  непонятная налоговая структура для cohort revenue.
- *Пример роли (IP-1):* downstream — T1-инвестор/партнёр, проверяющий «можно ли тут законно
  делить деньги».

## 4. Secondary audience (mention only)

Steuerberater + банк (получатели прямых артефактов 4.1, 4.4). Будущий treasurer (Run) —
наследует bookkeeping. Юрист — проверяет контракт-template на немецкое право.

## 5. Ключевые сообщения (что foundational-блок обеспечивает)

1. **Легальный базис под приём денег** — без него ступень 5 (€1500/мес) не запустить.
2. **Форма совместима с кооперативом** — Einzel/GmbH/UG/Genossenschaft × R12-механики (5:1,
   75/25, fork-and-leave).
3. **Контракт с R12-зубами** — fork-and-leave + 30-day + asset retrieval встроены.
4. **Invoice SEPA-ready** — для EU-клиентов.
5. **Bookkeeping-минимум** — трекинг без over-engineering.

## 6. Структура — 4 под-артефакта (спека каждого)

### 6.1 Steuerberater email template (что спрашиваем)
Каркас вопросов (НЕ готовый текст письма):
- Какая форма (Einzelunternehmen / GmbH / UG) оптимальна для старта при cohort-revenue модели?
- Кооперативное управление (Genossenschaft / альтернативы) — feasibility в Германии?
- Налоговые импликации для cohort revenue 75/25 split?
- Ожидаемые costs (startup + ongoing) per форма?
- Как форма влияет на приём международных платежей (EU SEPA + не-EU)?
[src: prompt Phase 10 §4.1 + Execution Plan §3 foundational — F2-F3, R-med]

### 6.2 Einzel / GmbH / UG матрица (каркас, значения — после консультации)
Матрица сравнения по dimensions (значения = placeholder до Steuerberater, R-low):

| Dimension | Einzel | UG | GmbH | Заполняется |
|---|---|---|---|---|
| Startup cost | ? | ? | ? | после консультации |
| Ongoing cost | ? | ? | ? | после консультации |
| Liability (ответственность) | ? | ? | ? | после консультации |
| Tax regime | ? | ? | ? | после консультации |
| Cooperative compatibility | ? | ? | ? | после консультации |
| Optimal for Build/Run/Scale | ? | ? | ? | после консультации |

**Важно:** мы НЕ заполняем значения — это юр-факты, которые даёт Steuerberater. Спека = каркас
dimensions, чтобы prep-решение было структурированным. [src: prompt §Phase 10 «matrix позволяет
prep-decision до consultation» — F2, R-high]

### 6.3 Контракт template (partner agreement minimum)
Что обязательно внутри (функции, не готовый текст):
- обязанности сторон;
- доли (revenue split, с потолком 5:1 — связь с Charter Phase 7);
- **fork-and-leave clause** (R12 MUST);
- **30-day notice** (R12 MUST);
- **asset retrieval** (забор наработок/данных, R12 MUST);
- IP (кому принадлежит созданное);
- **cooperative-governance compatibility** (совместимость с Charter-механиками).
[src: prompt Phase 10 §4.3 R12 + Charter Phase 7 — F2-F3, R-med]

### 6.4 Invoice template + bookkeeping
- **Invoice:** SEPA-ready для EU; обязательные реквизиты (после выбора формы); генерирует
  валидный EU-инвойс.
- **Bookkeeping-минимум:** сравнение инструментов (FastBill / lexoffice / sevDesk) по
  dimensions (cost / EU-compliance / простота) — выбор R1 §15.
[src: prompt Phase 10 §4.4 — F2-F3, R-med]

## 7. Hook начала (для downstream-партнёра)

Не применимо как «hook видео» — но для downstream-партнёра первое впечатление от контракта =
**«выход первым, потолок виден»** (как в Charter). Контракт, открывающийся fork-and-leave, а не
обязательствами, сигналит «не кабала». [src: Charter Phase 7 hook — F2-F3, R-med]

## 8. CTA конца

Для Self: отправить email Steuerberater'у → назначить консультацию. Для downstream-партнёра:
контракт-template = «вот основа, адаптируем под тебя за ≤30 мин». Никакого «подпиши сейчас».

## 9. Формат / длина

- **4.1** email-template (короткий, структурированный список вопросов).
- **4.2** матрица 3×6 (каркас).
- **4.3** контракт-template (adapt за ≤30 мин под партнёра).
- **4.4** invoice-template (SEPA) + bookkeeping setup.

## 10. Зависимости

- **Pre-reqs:** ничего внешнего для 4.1-4.2 (можно начать сразу, параллельно видео A); Charter
  spec (Phase 7) для контракт-template R12-clauses.
- **Блокирует:** приём денег (ступень 5 €1500/мес = вход в Run); бизнес-счёт зависит от
  выбранной формы.
- **Параллельно:** видео A, CRM-разметка (Steuerberater email — independent, Week 1). [src:
  Platform Lifecycle §8 Week 1 «Steuerberater email параллельно» — F2-F3, R-med]
- **Строго последовательно:** Steuerberater email → консультация → выбор формы → регистрация →
  бизнес-счёт (нельзя открыть счёт до выбора формы).

## 11. Substrate sources (explicit)

| Под-артефакт | Источник + секция | F-G-R |
|---|---|---|
| 4.1 email | Execution Plan §3 foundational + Platform Lifecycle §6 юр | F2-F3, R-med |
| 4.2 матрица | prompt Phase 10 §4.2 (dimensions) — значения после консультации | F2, R-low до консультации |
| 4.3 контракт R12 | Charter Phase 7 + Economic V10 §11 (fork-and-leave + 30-day) | F8/F2, R-high/R-med |
| 4.4 invoice/bookkeeping | prompt Phase 10 §4.4 (SEPA + инструменты) | F2, R-med |
| cooperative-compat | Team OS Plan §6 (Mondragón 5:1 + revenue split) | F2-F3, R-med |

## 12. R12 paired-frame check (8 вопросов) — фокус на контракт-template

| # | Вопрос | Применение | Вердикт |
|---|---|---|---|
| 1 | Цена ≤ польза? | контракт даёт партнёру защиту > обязательств | ✅ |
| 2 | Конкретно? | да — доли, потолок, выход явно | ✅ |
| 3 | Соразмерно? | контракт = ступ.6, для прогретых | ✅ |
| 4 | По ступени? | не суём контракт новичку | ✅ |
| 5 | Канал уместен? | юр-документ читается осознанно | ✅ |
| 6 | Не доим / не запираем? | **fork-and-leave + 30-day + asset retrieval = MUST в контракте** | ✅ STRICT |
| 7 | Нет манипуляции? | нет gotcha-clauses; cooperative-governance compatible | ✅ |
| 8 | Стоп-сигнал готов? | юрист ревьюит контракт; нет lock-in clauses | ✅ |

**Главная R12-зона (вопрос 6):** контракт — это место, где lock-in обычно прячут юридически.
Защита: **fork-and-leave + 30-day notice + asset retrieval — обязательные пункты контракта**, не
опции. [src: prompt Phase 10 R12 «контракт MUST include fork-and-leave» — F2, R-high]

## 13. Acceptance criteria

- ✅ Email Steuerberater'у **готов отправить** (структурированные вопросы).
- ✅ 3-форма matrix позволяет **prep-decision до консультации** (каркас dimensions готов).
- ✅ Контракт-template можно **adapt под партнёра за ≤30 мин**.
- ✅ Invoice-template **генерирует валидный EU SEPA-инвойс**.
- ✅ Bookkeeping-минимум настроен (инструмент выбран).
- ✅ Контракт содержит fork-and-leave + 30-day + asset retrieval (R12 MUST).
- ✅ Значения матрицы НЕ выдуманы — заполняются после Steuerberater.

## 14. Анти-паттерны

- ❌ **Over-engineering форм** — выбор GmbH без консультации «потому что солиднее».
- ❌ **Выбор формы без Steuerberater** — юр-решение без эксперта.
- ❌ **Контракт с lock-in clauses** — нарушение R12.
- ❌ **Invoice без SEPA** — не работает для EU.
- ❌ **Bookkeeping over-engineering** — сложная система до первых денег.
- ❌ **Выдуманные юр-факты** в матрице — это F3-нарушение (нового research не добываем).

## 15. Варианты / R1 decisions (surface)

- **R1-LF1 Какая форма preferred default** — Einzel (cheapest) / UG (limited-liability low-cap) /
  GmbH (classic)? *Факт:* решение после Steuerberater; влияет на Build exit. [src: Platform
  Lifecycle §10 R1-3 — F2-F3, R-med]
- **R1-LF2 Cooperative-legal hosting** — DE Genossenschaft vs international structure? *Факт:*
  Genossenschaft ближе к Mondragón-модели, но сложнее зарегистрировать.
- **R1-LF3 Bookkeeping инструмент** — FastBill / lexoffice / sevDesk? (по dimensions cost/compliance).
- **R1-LF4 Когда отправлять Steuerberater email** — Week 1 (параллельно видео A, по плану) или
  после первых ответов Wave 1?
- **R1-LF5** Контракт-template — один универсальный или per-тип партнёра (T1/T2/T4)?

Все — за Ruslan. [src: prompt §0 R1 surface only — F2, R-high]

---

*Phase 10 closure 2026-05-25. Юр + Финансы combined spec по 15-точечному template (4 под-
артефакта). F3 STRICT — НЕ добываем юр-research, специфицируем вопросы + каркас матрицы;
значения после Steuerberater (R-low). R12 главная зона — вопрос 6 (контракт fork-and-leave +
30-day + asset retrieval MUST). NO выдуманные юр-факты. R1 surface (5 вариантов). Дальше —
Phase 11: Supporting materials spec.*
