---
title: Phase 2 — Extended Meta-Method (6-step → 8-step с явным этапом подготовки)
date: 2026-05-26
type: phase-report-extended-meta-method
parent_prompt: prompts/preparation-stage-concept-supplement-2026-05-26.md
parent_main: decisions/strategic/PREPARATION-STAGE-CONCEPT-SUPPLEMENT-2026-05-26.md
phase: 2
F: F2 (verbatim baseline extract) + F3 (extension synthesis)
G: prompt-preparation-stage-concept-supplement-2026-05-26
R: refuted_if_no_baseline_vs_extended_comparison
constitutional_posture: R1 surface only + R2 STRICT (Method V2 LOCKED preserved) + R6 + R11 + IP-1 + append-only
language: russian primary
---

# Extended Meta-Method — 6 шагов → 8 шагов (этап подготовки явно)

> **Что это.** Расширение мета-метода Method V2 §J: вынос **этапа подготовки** из имплицитного
> (внутри шагов 1-4) в явный (отдельные Steps 0-1). **R2 STRICT:** Method V2 §J 6-шаговая процедура
> = LOCKED, не модифицируется. Расширение = supplement-предложение (R1, Ruslan picks integration).

---

## §A Baseline — existing Method V2 §J мета-метод (verbatim extract)

Из `METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` §5 «6-шаговая процедура мета-метода (Ruslan voice)»:

> 1. **Identify системы влияния** — окружающие system (people / contexts / tools / resources)
> 2. **Целесообразно собирать информацию** — достаточно для действия, не больше (gradient
>    достаточности; satisficing per Simon)
> 3. **Целесообразно обрабатывать** — что важно / что фоновое; pattern matching
> 4. **Ставить цель целесообразно** — не «хочется», а «надо для жизни»
> 5. **Выбрать лучший метод** — на основе шагов 1-4
> 6. **Apply + measure + adjust** — execute, observe, update method library

[src: Method V2 §5, LOCKED — verbatim]

**Наблюдение (R6).** В baseline подготовка **уже присутствует**, но размазана внутри шагов 1-4: identify
систем (1), собрать info (2), обработать (3), поставить цель (4) — это всё суть **подготовка**. А шаги
5-6 — это **действие** (выбор метода + execute). То есть baseline уже содержит границу prep/action
между шагом 4 и шагом 5 — но **не называет её** и не делает её осознанной точкой решения. Voice 26.05
просит сделать эту границу **явной**: сначала понять, что есть подготовка, выбрать метод подготовки, и
лишь потом — метод действия.

---

## §B Extended procedure (с явным этапом подготовки)

Расширение добавляет **prep-gate (Step 0)** в начало и **explicit prep-method selection (Step 1)**, а
также **разворачивает feedback** в два шага (7-8). Baseline-шаги сохранены, перенумерованы и помечены.

| # | Шаг | Режим | Связь с baseline §J |
|---|---|---|---|
| **0** | **Preparation need detection** (NEW явно) — speed-mode или depth-mode? + 5 calibration questions | prep-gate | *было имплицитно* — решение «сколько info собирать» внутри шага 2 |
| **1** | **Preparation method selection** (NEW явно) — из готовых методов подготовки ИЛИ собрать свой | prep | *было имплицитно* — выбор «как собирать/обрабатывать» |
| **2** | **Preparation execution** — собрать контекст / изучить систему (C9) / сформулировать гипотезу | prep | = baseline шаги 1+2+3 (identify систем + собрать + обработать) |
| **3** | **Picture formation** — синтез выходов подготовки → ясная картина ситуации | prep→ | = baseline шаг 4 «поставить цель» + **новое: картина как условие** для шага 4 |
| **4** | **Action method selection / creation** — готовый (стандартная ситуация) ИЛИ уникальный (§E трюк) | action | = baseline шаг 5 «выбрать лучший метод» + **новое: опция создать уникальный** |
| **5** | **Action execution** | action | = baseline шаг 6 «apply» (часть) |
| **6** | **Feedback collection** — что сработало / что нет | feedback | = baseline шаг 6 «measure» (часть) |
| **7** | **Improvement note → next loop** — обновить библиотеку методов | loop | = baseline шаг 6 «adjust + update method library» (часть) |

> **Нумерация-нота.** Prompt говорит «8 steps» и местами перечисляет Step 0..Step 7 (= 8 шагов). Я
> сохраняю Step 0..7 (8 ячеек). Можно читать и как «6 baseline + 2 явно-выделенных prep-шага».

---

## §C Сравнение baseline vs extended

| Аспект | Baseline (Method V2 §J) | Extended (этот supplement) |
|---|---|---|
| Кол-во явных шагов | 6 | 8 (0-7) |
| Подготовка | имплицитна (внутри 1-4) | **явная стадия** (Steps 0-3) |
| Prep-gate (нужна ли prep) | нет явного решения | **Step 0** — осознанный триаж speed/depth |
| Метод подготовки | не выбирается отдельно | **Step 1** — выбор/сборка метода prep |
| «Картина» как условие | неявно (шаг 4 цель) | **Step 3** — явный сигнал перехода prep→action |
| Создание уникального метода | «выбрать лучший» (шаг 5) | **Step 4** — выбрать ИЛИ **создать** уникальный (§E) |
| Обратная связь | свёрнута в шаг 6 | **Steps 6-7** развёрнуты (collect → improve) |

### Где подготовка была имплицитна → стала явной

- Baseline шаг 2 «целесообразно собирать» содержал **калибровку объёма** — теперь это Step 0 (5
  calibration questions) + Step 1 (выбор метода prep).
- Граница prep/action (между baseline 4 и 5) была **неназванной** — теперь это Step 3 «картина» как
  явная точка перехода (где мастерство видно, §F Phase 1).

### Почему расширение имеет значение (per voice)

Voice 26.05: мастерство «видно и накапливается» именно на **переходах** (prep→action, study→action,
action→feedback). Если переходы не выделены явно — их нельзя осознанно тренировать. Baseline отлично
описывает **что делать**, но скрывает **где тренируется мастерство**. Extended вытаскивает эти точки
наружу, чтобы их можно было видеть, мерить и прокачивать. Это не «больше шагов ради шагов», а **делание
видимыми тех мест, где живёт навык** (P-08, P-10).

---

## §D Application examples (3 домена, extended procedure)

### D.1 Инженерия — рефакторинг легаси-модуля

- **Step 0 (detect):** depth-mode — модуль критичный, последствия каскадные. Calibration: сколько = 1
  день; детальность = структурный план; зачем = понять зависимости; куда = только этот модуль + его
  контракты.
- **Step 1 (prep method):** прочитать код + тесты + историю коммитов + нарисовать граф зависимостей.
- **Step 2 (execute prep):** разобрал модуль, нашёл узкое горлышко (C10) — не там, где думал.
- **Step 3 (picture):** ясно — проблема в одном контракте, не во всём модуле.
- **Step 4 (action method):** **уникальный** — точечный рефактор контракта + adapter, а не переписывание
  (готовый метод «переписать всё» был бы вреден).
- **Step 5-7:** выполнил → тесты зелёные → заметка: «граф зависимостей до рефактора экономит дни».

### D.2 Sales — звонок с потенциальным клиентом

- **Step 0 (detect):** depth-mode — важный лид. Calibration: 1 час; структурный план; перед звонком;
  зачем = понять его реальную задачу; куда = его контекст + fit, не «впарить».
- **Step 1 (prep method):** изучить компанию + роль человека + сформулировать гипотезы о его боли.
- **Step 2-3 (execute → picture):** картина — у него не та проблема, что в типовом скрипте.
- **Step 4 (action method):** **уникальный discovery-flow** под него (не шаблонный pitch).
  **R12-нота:** цель — понять и помочь, не «продавить» (§H Phase 1).
- **Step 5-7:** провёл звонок → feedback: гипотеза подтвердилась наполовину → улучшить prep-вопросы.

### D.3 Daily — рутинная запись в Daily Log

- **Step 0 (detect):** **speed-mode** — шаблон существует, низкий impact. Prep минимальна.
- **Steps 1-4 (skip):** берём готовый метод (template) напрямую.
- **Step 5 (action):** заполнил по шаблону (≤2 мин).
- **Step 6-7 (feedback):** короткая заметка, если что-то не влезло в шаблон. Всё.

**Вывод по примерам.** Extended procedure **не утяжеляет** рутину (speed-mode проскакивает Steps 1-4),
но **спасает важное** (depth-mode заставляет построить картину до выбора метода). Это и есть калибровка
из §C Phase 1 в действии.

---

*Phase 2 closure. Baseline §J (6 шагов, LOCKED-verbatim) → extended (8 шагов 0-7 с явным этапом
подготовки). §A baseline + наблюдение о имплицитной границе · §B extended таблица (mapping к baseline)
· §C baseline-vs-extended сравнение + почему важно · §D 3 application examples (инженерия / sales /
daily). R2 STRICT — Method V2 не модифицируется; extension = R1 supplement-предложение. Переход к Phase
3 (augmentation patches per doc).*
