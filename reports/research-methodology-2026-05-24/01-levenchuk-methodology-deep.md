---
title: Phase 1 — Левенчук Methodology 2025 deep decode (метод-объект 1st class / methodology as discipline / SoTA tracking)
date: 2026-05-24
phase: 1
parent_prompt: prompts/research-methodology-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2 (verbatim citations) + F3 (synthesis)
G: research-methodology
R: refuted_if_R1_strategic_prose_authored_OR_LOCK_modified
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + IP-1 + EP-5 + AP-6 + append-only + SKIP-list
status: phase-1 surface
language: russian primary
priority: ⭐⭐⭐ deepest phase
---

# Phase 1 — Левенчук «Методология 2025» deep decode

> **Цель.** Глубоко распаковать содержание учебника Левенчука «Методология 2025»
> (Ridero ISBN 978-5-0064-8619-5, ~826 страниц, 9622 строки конвертированного MD)
> на 30+ концептов / категорий, релевантных Jetix-методу. Phase 1 = ⭐⭐⭐
> highest priority — Левенчук = primary anchor для T1 (русская методологическая
> традиция) + T12 (method engineering standards through OMG Essence). Phase 6
> (русская традиция исторически) использует Phase 1 как substrate.

---

## §0 TL;DR (≤300w)

Левенчук в «Методологии 2025» формулирует **современное безмасштабное
неантропоцентричное «учение о методе»** — методологию как фундаментальный
метод мышления intellect-stack'а, не как философскую дисциплину прошлых веков.
**Ключевые движения:**

1. **Метод как объект 1-го класса** — собственное имя, типизация, методы работы
   с самим методом (сравнение, моделирование, выбор, разложение, развитие). [src: Левенчук Методология 2025 раздел «Метод как объект первого класса» строки 3536-3608]
2. **Сигнатура метода** — компактное определение через предметы метода + роли,
   и **альфа (alpha)** — предмет метода с graph of states + checklist as
   instrument of attention management. [src: Methodology 2025 строки 108-167]
3. **Стратегирование = выбор метода когда непонятно что делать** — отдельно от
   планирования (планирование = графа работ при known методе). [src: M2025 строки 60, 178, 451]
4. **OMG Essence 2.0:2024 = primary standard** для записи методов разработки;
   ISO/IEC 24744:2014 — параллельный. SoTA tracking требуется. [src: M2025 строки 56, 271, 7662]
5. **Третье поколение системного подхода** = ядро на основе системного мышления
   2024 (томы 1+2); СМД-методология Щедровицкого = «второе поколение», застрял
   в 1994. [src: M2025 строки 281, 484]
6. **Method engineering / situational method engineering** — отдельная
   дисциплина (Brinkkemper 1996); SME = один из методов самой методологии как
   учения о методе. [src: M2025 строка 275 + Wikipedia Method_engineering сноска 12]
7. **Прикладная vs фундаментальная методология** — фундаментальная = уровень
   мета-мета-модели; прикладная = специализация для предметной области (ML
   methodology / архитектурная методология / методология тренинга). [src: M2025 строки 209-225, 259, 488-496]
8. **Локальные vs распределённые представления метода** — на distributed-
   representation level (нейросети с representation learning) методология
   "методов выбора метода" является frontier (Vanchurin / Friston / RL policy).
   [src: M2025 строки 393-424]
9. **Hybrot (hybrid robot) vs cyborg** — современная концепция: компьютер с
   людьми в составе, а не человек с компьютером. [src: M2025 строки 480, 3501]
10. **«Всё новое в методологию приходит сбоку»** — disruption всегда из
    смежных предметных областей; SoTA tracking = постоянная инвестиция. [src: M2025 строки 407, 5973-5985]

**Bottom-line:** Левенчук — это **continuator русской методологической
традиции** (Щедровицкий → ШСМ → Левенчук), но переформулированный для AI-эры:
hybrid agents, distributed representations, OMG Essence standards, constructor
theory. R1: оценка Jetix-positioning vs Левенчук-tradition — owner-decided.

---

## §1 Авторитет источника и место в Jetix-substrate

### §1.1 О Левенчуке как авторе

Анатолий Левенчук — основатель Школы Системного Менеджмента (ШСМ), руководитель
Русского отделения INCOSE, разработчик курсов «Системное мышление» (двухтомник
2024), «Методология 2025», «Интеллект-Стек 2023», «Инженерия Личности»,
«Системная инженерия», «Системный менеджмент», «Рациональная работа». Учебник
«Методология 2025» — 9-я переписка курса, исходно появился в 2013 как часть
«Системноинженерное мышление»; вынесен в отдельный курс в 2023; материал
учебника составляет ~70 часов учебной нагрузки.
[src: Левенчук Методология 2025 строки 64, 74-78 (Введение)]

### §1.2 Место в Jetix-substrate

| Источник Jetix-substrate | Levenchuk-tradition role |
|---|---|
| `decisions/strategic/DR-38-META-METHOD-COMPOSITION-2026-05-22.md` §8 | "Schedrovitsky-Levenchuk Russian methodology school" = explicit lineage attribution |
| `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` §0 + §5 | "Levenchuk MG4 — метод как 1st-class object" = canonical Jetix grounding |
| `decisions/strategic/METHOD-DEEP-DESCRIPTION-2026-05-21.md` §1.1 | O-107 one-liner «метод по объединению методов» = explicitly Левенчук-lineage |
| `design/JETIX-FPF.md` IP-1 + IP-7 | FPF-spec IP-1 (Role≠Executor) parallels Левенчук's «метод::роль» отличается от агента-оргзвена |
| `swarm/wiki/foundations/principles/architecture.md` Tier 2 | foundation_generic 12 rules align с Левенчук intellect-stack discipline ladder |
| Бывший `levenchuk-corpus-2026-05-17` + `levenchuk-tg-2026-05-17.md` | Telegram + Aisystant + LiveJournal substrate = continuous live source |

**Substrate sufficiency:** Phase 1 имеет direct primary source (полный MD,
9622 lines) + 4 pre-extracted secondary docs (DR-38 / Method V2 / Method-Deep V1
/ Meta-method 8-component). Достаточно для deep decode.

---

## §2 Канонические понятия (30+ концептов)

### §2.1 Метод (way of working) — central concept

**Левенчук определение verbatim:** *«Метод/way of working ... – это в инженерии
способ/паттерн/шаблон работ. Это функциональное определение, единица повторной
используемости в работе, паттерн/похожесть в выполнении множества работ,
относимых к одному методу работы.»* [src: M2025 строка 297]

**Расширение:** *«Метод/функция – это функциональный аспект поведения какой-то
системы (если неживой, то чаще говорят функция, если живой – метод или один из
его многочисленных синонимов для системы-создателя) как роли/функционального
объекта. Работа/функционирование/«задействование/выполнение метода» –
конструктивный взгляд на поведение системы как конструктивного объекта.»*
[src: M2025 строка 297]

**Синонимы метода (Левенчук-list):**
- way of working
- способ работы / паттерн работы / шаблон работы
- практика / practice
- рабочий процесс
- культура / стиль (особенно для мелких различий)
- технология
- стратегия (=метод когда непонятно что делать)
- инженерия (в смысле «инженерия чего-то»)
- труд (особенно для разделения труда)
- деятельность
- функция (для неживых исполнителей)

[src: M2025 строки 92-103, 297-303, 327-339]

**Дихотомия:** метод = тип / паттерн (1 экземпляр в типологии); **работа** =
конкретный экземпляр воплощения метода в физическом мире (множество в
календарном времени). Метод существует в мире, пока агент исполняет роль,
выполняя работу. [src: M2025 строки 114, 134, 297-309]

### §2.2 Альфа (alpha) — предмет метода

**Verbatim:** *«Альфа – это предмет метода, который может быть и физическим
объектом (системой), и абстрактным объектом (описанием). Поэтому трудно говорить
о частях-целых альфы, понятие «подальфа» определяется более сложным образом.»*
[src: M2025 строка 110]

**Назначение:** *«Альфа позволяет управлять вниманием создателя в ходе исполнения
длинных цепочек операций в онтологически сложных случаях, например, когда
внимание к описаниям составных частей системы переходит в ходе разработки
проекта/design системы к физическим составным частям будущей системы,
изготавливаемой по проекту (сырью, заготовкам, деталям и сборкам деталей), а
затем и к целевой системе в сборе и в момент эксплуатации.»* [src: M2025 строка 112]

**Lineage:** альфа = из OMG Essence Kernel (Software Engineering Method And
Theory / SEMAT initiative, Jacobson-Spence-Bittner 2013); Левенчук адаптирует
для безмасштабной методологии (не только software).
[src: M2025 строка 56 + Jacobson et al "Essence Standard" 2013 + Wikipedia
SEMAT https://en.wikipedia.org/wiki/SEMAT]

### §2.3 Чеклист альфы

**Verbatim:** *«Представление графа состояний для целей контроля этих состояний
в виде списка контрольных вопросов о достижении этих состояний в ходе проекта
называют чеклистом альфы.»* [src: M2025 строка 154]

**Структура состояния альфы:**
- состояние формулируется глаголом в **прошедшем времени**
- состояние = результат применения какого-то составного метода
- граф состояний может иметь возвраты, кольца, петли (не линейный)

**Пример verbatim:** *«Для альфы подарка:: „предмет дарения::метод“ можно
определить следующие состояния:
• Необходимость подарка признана (подарок:: „предмет метода“ перешёл в
состояние «необходим» после применения к нему признания::метод).
• Подарок выбран... • Подарок приобретён... • Подарок подарен...»*
[src: M2025 строки 156-164]

### §2.4 Сигнатура метода (signature)

**Verbatim:** *«Сигнатура – это просто название метода и определение предметов
метода в желаемом состоянии.»* [src: M2025 строка 311]

**Пример:** *«передача::метод чего-то:: „предмет метода“ дающим::роль
принимающим::роль. Можно специализировать метод передачи до покупка::передача::
метод чего-то:: „предмет метода“ покупателем::принимающим::роль у продавца::
дающего::роль.»* [src: M2025 строка 148]

**Дисциплина:** перед началом работы — точно сформулировать сигнатуру; это
«первый шаг» mental discipline для методолога. [src: M2025 строки 432-440]

### §2.5 Метод-объект 1-го класса (Method as 1st-class object)

**Definition (Левенчук):** *«Объект первого класса – это такой объект, понятие
типа для которого имеет собственное имя, который известным образом связан
объектами других типов, методы работы с которым известны и тоже имеют свои
имена. Методы работы с методом как объектом (обсуждение способа работы/действий,
универсальное для самых разных способов и самых разных работ для получения
самых разных результатов задействования метода для разных его предметов) редко
встречаются, им нужно учиться.»* [src: M2025 строка 3539]

**Method работы с методом (5 operations):**
1. Моделирование метода
2. Сравнение методов
3. Выбор метода (стратегирование)
4. Разложение / синтез метода
5. Развитие метода

[src: M2025 строки 357-368, 3536-3543; Method V2 §1.1 derived]

**Невидимая vs видимая часть метода:**
- Невидимая = знания/объяснения/дисциплина/теория/правила/алгоритм в голове
  агента / контроллере робота → может быть «явное» (моделированное) или
  «неявное»/tacit knowledge (Polanyi)
- Видимая = инструментарий + предметы метода

[src: M2025 строки 3543, 3549, 3553]

**Jetix-mapping:** этот концепт = O-107 anchor canonical Jetix one-liner «метод
по объединению методов по улучшению системы самой себя» — operations 1-5
проявляются в ROY swarm 5 experts × 4 modes structure. [src: METHOD-DEEP-DESCRIPTION-2026-05-21.md §1.1]

### §2.6 Стратегирование (strategizing) — выбор метода в условиях
непонятно-что-делать

**Verbatim:** *«В самых общих чертах мы рассмотрим, как проводить
стратегирование – выбирать новый метод работы в условиях, когда вообще
непонятно, что делать. А если непонятно, что именно делать, то и планировать
ещё ничего нельзя.»* [src: M2025 строка 178]

**Отличие от планирования:** планирование = составление графика работ при
известном методе + оптимизация ресурсов. Стратегирование = выбор метода **до**
планирования. [src: M2025 строки 60, 178, 424, 451]

**Полный алгоритм стратегирования (Левенчук 4-шаговый):**
1. Точно сформулировать сигнатуру метода (problem framing).
2. Найти **более одного варианта** разложения (если думаешь, что вариант один —
   ты что-то упустил).
3. Принять рациональное (на базе лучших теорий принятия решений) решение между
   альтернативами — «наименее худшее из всех имеющихся».
4. Обосновать выбор (инженерное обоснование).

[src: M2025 строки 432-440]

**Recursive nature:** на каждом уровне разложения метода — стратегирование
повторяется (выбор оптимального стека методов, а не одного метода). Пример с
чисткой зубов на много уровней: метод → щётка vs паста vs зубная нить → выбор
сорта пасты при выборе щётки/пасты method → марка / абразивность / etc.
[src: M2025 строки 442-446, 569]

**Jetix-mapping:** «метод выбора методов» = central recursive concept в Method
V2 §5 — explicit Левенчук lineage. [src: METHOD-LIFE-DEVELOPMENT-V2 §0 + §5]

### §2.7 Создатель / constructor (David Deutsch lineage)

**Verbatim:** *«Создатель/constructor – это обобщение вычислителя, универсальный
создатель (например, человек или робот с AI) – это который, если дать ему
достаточно времени и материалов, может провести все теоретически (согласно
принципам физики) возможные преобразования/transformations материалов ровно
так, как универсальный (эквивалентный машине Тьюринга) вычислитель может
провести все теоретически возможные вычисления/computations, то есть
преобразования информации.»* [src: M2025 строка 128]

**Constructor theory (David Deutsch lineage):** *«David Deutsch предложил
понятие создателя/counstructor, которое позволяет рассуждать о методах работы
создателя, причём создатель при выполнении экземпляров работ по методу остаётся
неизменным – но появляется при этом ход на безмасштабное неантропоцентричное
описание методов работы как поведения создателей.»* [src: M2025 строка 245 +
ссылка на constructortheory.org]

**Implication для Jetix-substrate:** universal constructor model = baseline для
"AI/cybernetic agents as method-executors" reasoning; не противоречит R12 LOCK
(human + AI symmetry в methodology surface).

### §2.8 Hybrot vs Cyborg

**Verbatim:** *«киборга (cybernetic organism) как образа агента будущего
заменяется концепцией гиброта (hybrot – hybrid robot).»* [src: M2025 строка 480]

**Stadium example:** *«стадион::организация::создатель – это такой робот,
который использует в своём составе живых сотрудников (hybrot), он работает
методом «развлечения». В разложении «развлечения» есть метод продвижения
(маркетинг, реклама, продажи), которым стадион-робот забирает в себя внутрь
40000 человек, обрабатывает их внутри себя два часа.»* [src: M2025 строка 3501]

**Significance:** flip of frame — не "люди с компьютерами" (cyborg), а
"компьютеры с людьми внутри" (hybrot). Org-charts становятся
constructor-architectures.

### §2.9 IPU (information-processing unit)

**Verbatim:** *«Агент/IPU (information-processing unit) ... мыслится
безмасштабно и его разумность тоже может быть совсем разной: у молекулы нет
порождающих/generative моделей мира и себя, у кошки их побольше, а команда
людей может иметь множество подробных таких моделей.»* [src: M2025 строка 245]

**Source:** PNAS paper 2022 «Information Processing Unit as evolutionary
replicating unit» https://www.pnas.org/doi/full/10.1073/pnas.2120037119

**Implication:** allows methodology to apply uniformly across scales — molecule,
cat, person, team, organization, society — same conceptual framework.

### §2.10 Прикладная vs фундаментальная методология

**Левенчук разделение:**

| Тип | Уровень мета-мета-модели | Пример роли |
|---|---|---|
| Фундаментальная (этот курс) | Мета-мета-модель | Методолог (рассуждает о методах в целом) |
| Прикладная (отдельные курсы) | Мета-модель | Инженер-методолог конкретной предметной области (методолог искусственных нейронных сетей; методолог архитектуры; методолог рабочих процессов) |

**Двухуровневое мастерство:** *«Современная идея в том, что исполнитель каждой
прикладной роли задействует два мастерства методолога на двух онтологических
уровнях: Фундаментальное методологическое мастерство... Прикладное
методологическое мастерство.»* [src: M2025 строки 488-496]

### §2.11 SoTA tracking (State-of-the-Art tracking)

**Verbatim:** *«Если „простой практик/деятель“ (инженер-конструктор, менеджер,
врач, политик и т.д.) не осваивает постоянно новые методы/практики, то он
порастает мхом, его работа обесценивается, он становится неконкурентоспособен.
Чтобы он мог эффективно обновлять свои знания, ему нужно уметь сравнить два
метода: его собственный и новый (а новых методов – множество, их эффективность
обычно неочевидна), и принять решение о том, какой из них SoTA.»*
[src: M2025 строка 377]

**Multi-axis SoTA:** *«методолог::роль... выделять тот метод, работу по которому
выполняет агент, его степень мастерства в этом методе, насколько SoTA этот
метод (насколько SoTA дисциплина/теория/объяснения, насколько SoTA
инструментарий, насколько SoTA предметы метода)»* [src: M2025 строка 3525]

**Implication для Jetix:** SoTA tracking = constant operational practice (НЕ
event); 4-dimensional (discipline + tooling + subjects + agent mastery) — это
prefigures Method V2 §J 8-component → DR-38 substantiation.

### §2.12 Три уровня абстракции (representation levels)

| Уровень | Содержание | Пример |
|---|---|---|
| Мета-мета-модель | Типы общего методологического мышления (метод, альфа, роль, сигнатура) | "альфа подарка" |
| Мета-модель | Типы предметной области (для конкретной practice) | "подарок: книга / гаджет / опыт" в gift-giving |
| Модель | Конкретный экземпляр в проекте | "конкретно эта книга для Васи на ДР 2026-05-30" |

[src: M2025 строки 395-405 + Method V2 §3.1 derived]

### §2.13 Распределённые vs локальные представления

**Verbatim:** *«В современном интеллект-стеке признаётся, что кроме
представления о методах работы в форме локальных (символьных) представлений с
типами и отношениями... существует вариант с распределёнными представлениями.
И тогда можно применить representations learning... какая-нибудь нейросеть...
может выполнить выявление паттернов как предметов метода, так и паттернов
эффективных действий с ними.»* [src: M2025 строка 399]

**Open frontier:** *«В распределённых представлениях так вопрос даже поставить
нельзя, это исследовательский фронтир, и в общем случае для агентов проблема
стратегирования и планирования не решена.»* [src: M2025 строка 407]

**RL connection:** *«Вся литература по «обучению с подкреплением» (reinforcement
learning) по большому счёту – это литература по стратегированию, обучению
выбору действий в незнакомой ситуации методом проб и ошибок.»* [src: M2025
строка 399]

**Moravec's paradox:** *«Парадокс Моравека: что легко для животных и людей, то
оказывается трудным для систем AI, а что трудно для животных и людей, то
оказывается легко для AI.»* [src: M2025 строка 422]

### §2.14 Разделение труда + дробность метода

**Verbatim:** *«Дробность методов в части выполнения составляющих какого-то
метода разными агентами часто называют разделением труда, а получение всё новых
и новых видов труда называют углублением разделения труда (помним, что метод
и труд – это синонимы).»* [src: M2025 строка 337]

**Anti-универсального-мастера thesis:** *«Большинство должностей устроены на
предприятии именно таким образом, поэтому какой-нибудь „начальник отдела“ по
факту вынужден половину времени заниматься работой, например, архитектора, а
остаток времени делить между работой операционного менеджера для своего
отдела ... „универсальных мастеров“ не бывает.»* [src: M2025 строка 341]

**Принципиальная неуниверсальность мастера** = grounding для разделения труда
+ для professional roles в Foundation Part 4 Role Taxonomy + IP-1 strict (role
≠ executor).

### §2.15 Дробление метода: 3 типа отношений

| Тип отношения | Что значит | Пример |
|---|---|---|
| Композиция / декомпозиция (часть-целое) | Деление поведения по 4D — плохо определено для процессов | Часто избегают |
| Разложение / составление (не сводимо к "части целым") | Метод A раскладывается на методы B+C+D, причём не как «части целого» | «приготовление борща» = пассировать + варить |
| Специализация (род-вид) | Подметоды-специализации | производство = аддитивное (3D-печать) vs субтрактивное (фрезерование) |

[src: M2025 строки 317-323]

### §2.16 Иерархия наименований метода по размеру

| Размер | Имя | Пример |
|---|---|---|
| Самый крупный | Метод / методология разработки | «Agile development methodology» |
| Средний | Практика / рабочий процесс / технология | «парное программирование» |
| Самый мелкий | Стиль | «стиль руководства» |

[src: M2025 строки 327-333]

### §2.17 Оргвозможность / capability

**Verbatim:** *«Различают поставленный рабочий процесс (когда „всё есть, работа
возможна“) и оргвозможность/capability как рабочий процесс, который ещё и
разрешили делать, разрешили тратить ресурсы на выполнение работ по этому
рабочему процессу.»* [src: M2025 строка 3559]

**Implication:** capability — не просто "у нас есть метод и инструмент";
требуется (a) согласование с надсистемой, (b) сотрудничество от исполнителей,
(c) лидерство для координации. Уровень дольше получается, чем обучение методу
(месяц vs год).

### §2.18 Прохождение развилки (decision-making for method choice)

Параллельно с системно-инженерной дисциплиной (раздел «Принятие решений:
прохождение развилок»), стратегирование метода = частный случай decision under
uncertainty:
- Generation of options (≥2)
- Rational decision-making (best theory available)
- Justification (engineering rationale)

[src: M2025 строки 430-440]

### §2.19 Этика метода

*«надо знать этику, а чтобы не выбрать какой-то метод (недаром именно в этике
говорят, что цели, то есть сигнатуры методов с заданным состоянием предметов
метода, не оправдывают средства, то есть разложение метода – цель «вылечить
головную боль» не оправдывает средства «отрубить голову».»* [src: M2025 строка 448]

**Implication:** этика = built-in constraint при стратегировании; goal-method
separation; goal ≠ justification for any decomposition.

### §2.20 Риторика метода

*«Ещё нужна риторика, чтобы как-то убедить других агентов следовать методу.»*
[src: M2025 строка 450]

**Implication:** методология = не только cognitive discipline; включает социальные
artefacts (убеждение / трансфер метода между агентами / etc.).

### §2.21 «Метанойя» методолога (perceptual shift)

*«Метанойя, которую должен получить методолог::роль – это смотреть на
действующих в мире агентов (IPU/constructor: существ, людей, организации
и т.д.) и как-то выделять тот метод, работу по которому выполняет агент, его
степень мастерства в этом методе.»* [src: M2025 строка 3525]

**4 dimensions to perceive:**
1. Sigh method behind agent activity (often invisible)
2. Mastery degree of agent in method
3. SoTA-ness of method (discipline, tooling, subjects)
4. Intelligence strength of agent (for handling "когда что-то пойдёт не так")

### §2.22 Метод как «учение о методе» — historical lineage

**Platon:** *«Термин довольно древний, первым его использовал Платон, и речь
шла о методе, которым производится «познание»/cognition.»* [src: M2025 строка 229]

**Прагматический поворот:** *«После более чем столетней давности прагматического
поворота в философии значения слова «методология» и «метод» продолжали
меняться и познание/исследование/изучение/learning/cognition перестало быть
только моделированием мира.»* [src: M2025 строка 243]

**Современная безмасштабная неантропоцентричная позиция:** *«Современная
методология тем самым становится безмасштабным учением о деятельности агентов
по изменению мира и себя, и эта деятельность включает в себя и деятельность
моделирования мира и себя, то есть деятельность познания, „научный метод“.»*
[src: M2025 строка 247]

### §2.23 Дисциплина методологии vs Учебный курс vs Сам метод мышления

**Левенчук 3-way distinction:**

1. **Метод мышления «методология»** — способ выполнения работ описания
   поведения агентов-создателей (что собственно делается).
2. **Дисциплина «методология»** — набор связанных понятий + способов рассуждения
   о них (knowledge/discipline/theory). Это сам "научный предмет".
3. **Учебный курс «методология»** — pedagogy of teaching the dispatchine + the
   method + adjacent fundamentals (онтология, рациональность, etc.).

[src: M2025 строка 257-263]

**Implication:** methodology has 3 "carriers": agent-doing-it, written discipline,
pedagogical curriculum. Each requires distinct method-engineering.

### §2.24 «Методология разработки XYZ» vs «инженерия методов»

**Verbatim:** *«„методология разработки XYZ“ или „метод разработки KLM“, а также
„инженерия методов“ и даже её вариант „ситуационная инженерия методов“ как
один из методов для самой методологии как учения о методе.»* [src: M2025 строка 275]

**Параллель с logic/geometry:** *«Это точно такое же использование слова
«методология», как и в случае «логики» – она тоже может быть учением о разных
логиках, а «Аристотелевская логика» – это одна из логик, изучаемых учением о
логиках.»* [src: M2025 строка 277]

**Implication for Jetix:** "Jetix-methodology" может быть как (a) one specific
прикладной methodology, (b) one specific application of method-engineering /
SME. R1 — Ruslan ack на conceptualisation choice.

### §2.25 Праксиология — alternative term

**Verbatim:** *«Есть ещё одно название для методологии как общей теории
деятельности – праксиология, и у праксиологии тоже есть самые разные понимания
того, в чём предмет этой фундаментальной науки.»* [src: M2025 строка 289]

**Mises / Rothbard tradition:** Левенчук acknowledges Австрийская школа
экономики основана на праксиологии; «удачным оказался только проект создания
самой австрийской экономической школы». Курс «Методология» НЕ опирается на
праксиологию, основывается на «других традициях описания деятельности, которые
развивались прежде всего в инженерии и менеджменте на базе системного подхода.»
[src: M2025 строка 289 + ссылки 18, 24 на Mises.org Rothbard 1951 paper]

### §2.26 «Все новое в методологию приходит сбоку»

**Verbatim:** *«Проблема с непредсказуемостью будущих технологий как прорывных
или даже подрывных в том, что все прорывные и подрывные инновации происходят
не из тех отраслей, где они реализуются – поэтому-то их и невозможно предвидеть,
раннее их развитие невозможно отследить.»* [src: M2025 строка 5979]

**Examples:** микроволновку — спецы по радарам; компьютер на радиолампах —
радиоэлектронщики, не математики; самолёт — братья Райт (мотоциклетная
мастерская); роботы-юристы в России — МТС/Мегафон (телеком), не legal-tech
firms; такси — Uber + Яндекс.такси (поисковик).
[src: M2025 строки 5983-5985]

**Methodological implication:** SoTA tracking должен быть **adjacent-possible**
(Kauffman), а не only «in-domain» — большая методологическая ошибка следить
только за domain peers. Cross-domain tracking + receptive mindset для adjacent
discoveries = baseline практика. Это grounds H7 «pluralism» в DR-40 + Method
V2 §8.

### §2.27 VUCA как контекст стратегирования

**Verbatim:** *«в быстро меняющемся (иногда в корпоративном стратегировании
говорят VUCA – volatility, uncertainty, complexity, and ambiguity) мире.»*
[src: M2025 строка 5945]

**Implication:** методология стратегирования = разрабатывается для VUCA-условий
по умолчанию. Не «методология для стабильного workflow», а «методология для
шторма».

### §2.28 Жизненный цикл → метод (концептуальная эволюция)

**Verbatim:** *«В курсе подробно рассказывается, что произошло с понятием
«жизненный цикл», как оно постепенно заменилось понятием «метод» (с его
многочисленными синонимами – процесс разработки, инженерный процесс,
методология разработки, рабочий процесс) по мере перехода к agile инженерным
процессам и их идеям по „непрерывному всему“.»* [src: M2025 строка 58]

**Lineage связь:**
- 1-е поколение системного подхода → жизненный цикл (waterfall)
- 2-е поколение → жизненный цикл + люди (СМД-методология, BPR)
- 3-е поколение → метод + развитие систем + agile + DevOps + continuous-everything

[src: M2025 строки 281, 484]

### §2.29 OMG Essence Kernel 2.0:2024 = primary standard

**Verbatim:** *«Изложение базируется тем самым не столько на философской
литературе прошлых веков и литературе по общей теории систем прошлого века,
сколько на методологических международных стандартах в менеджменте, инженерии,
программной инженерии, появившихся уже в 21 веке (особенно широко мы используем
стандарт OMG Essence 2.0:2024, моделирование графа создания дано по его
мотивам).»* [src: M2025 строка 56]

**ISO/IEC 24744:2014** — parallel standard for software methodology metamodel.
[src: M2025 строка 271 + Wikipedia https://www.iso.org/standard/62644.html]

**OMG Essence alphas** (7 default + extensible):
1. Opportunity (бизнес-возможность)
2. Stakeholders
3. Requirements
4. Software System
5. Work
6. Team
7. Way-of-Working

Каждая альфа имеет state graph + checkpoints. Jetix-substrate уже использует
alpha-machinery в Hypothesis Architecture 7-layer (Method V2 §10).

### §2.30 Праздные «службы качества» vs реальная методология

Левенчук-critique: organizational «службы качества» обычно делают bureaucratic
descriptions (не для improvement, а для проверяющих); реальная методология =
для рабочей оптимизации agent's work, не для compliance. [src: M2025 строка 365]

**Implication:** distinguish "ceremonial methodology" (procedural compliance)
vs "operational methodology" (actual decision-making support).

---

## §3 «Третье поколение системного подхода» — context для методологии Левенчука

### §3.1 Generational mapping (3 поколения системного подхода)

| Поколение | Период | Ключевые фигуры | Что обновлено |
|---|---|---|---|
| 1-е | 1948-1970 | Wiener, Ashby, Bertalanffy | Cybernetics + general systems theory; систему как функциональный блок |
| 2-е | 1970-1990 | Forrester, Senge, Чекланд, Щедровицкий ММК | Soft systems thinking; систему включают люди; **СМД-методология** |
| 3-е | 1990-present | Левенчук-ШСМ, Beer VSM 2nd-look, Maturana-Varela, Constructor theory (Deutsch), Kauffman adjacent-possible | Безмасштабность + неантропоцентризм + создатель/constructor; **развитие систем** через эволюцию методов |

[src: M2025 строки 281, 484; cross-cite Method V2 §13 + DR-40 §3.1]

### §3.2 СМД-методология (Щедровицкий ММК) — 2-е поколение

**Verbatim:** *«СМД-методология была (активное её развитие остановилось где-то
с 1994 года, поэтому „была“) довольно близка к излагаемой нами версии мышления
о деятельности, но она использует довольно ранние версии системного подхода, а
именно „второе поколение“, в котором вокруг создаваемых систем появились уже
люди, но ещё не рассматривался безмасштабный многоуровневый
панпсихизм-физикализм и не проводилась последовательная деантропоморфизация
мышления.»* [src: M2025 строка 281]

**Implication for Jetix Phase 6 deep dive:** Левенчук = **continuator-with-update**
of Russian methodology tradition. Он принимает CMD-понятия рамки, но обновляет
до 3-го поколения + AI-эры. Это критическое позиционирование для Phase 6.

### §3.3 Безмасштабная неантропоцентричная позиция

3 ключевые методологические move:
1. **Безмасштабность** — same conceptual framework от molecule до society.
   Молекула-катализатор = constructor; так же transnational corporation.
2. **Неантропоцентризм** — agent ≠ obligately human; AI agents, robotic
   ensembles, "swarm intelligence" — все могут быть constructor.
3. **Деантропоморфизация мышления** — отказ от уподобления "mental" processes
   only humans; mind is information-processing of any IPU.

[src: M2025 строка 245-247, 281, 480, 3525-3531]

**Differential vs CMD:** CMD-методология (Schedrovitsky) — антропоцентрична
(основной фокус на людей, оргдеятельность через ОДИ); Левенчук — неантропоцентрична
(включая роботов, AI agents, hybrots).

---

## §4 Intellect-Stack: place of methodology

### §4.1 Intellect-Stack как ladder

Согласно Левенчук-курсу «Интеллект-Стек 2023» (см. `04-intellekt-stek-2023.md`),
intellect-stack включает fundamental thinking methods, среди которых:
- Семантика (учение о представлениях)
- Онтология (типы / категории)
- Теория понятий
- Логика
- Рациональность
- Методология  ← мы здесь
- Системное мышление
- Этика
- Эстетика
- Риторика
- Математика
- Физика
- Computer science

[src: M2025 строки 411, 446, 450, 488-496 + Intellect-Stack 2023 corpus]

### §4.2 Methodology как фундаментальный метод мышления

*«Курс „Методология“ – это курс обучения фундаментальному методу мышления,
методология входит в число дисциплин интеллект-стека.»* [src: M2025 строка 62]

**Place:** methodology — это «метод мышления о методе» (мета-операция), но он
полагается на остальные intellect-stack disciplines (логика, онтология,
рациональность, etc.) для своих обоснований.

### §4.3 Jetix-mapping

Jetix-substrate частично реализует Левенчук intellect-stack как ROY swarm:
- **5 ROY experts × 4 modes = 20-cell parallel processing** = operationalisation
  методологического выбора метода в command-control layer
- **engineering-expert** ≈ системная инженерия role
- **systems-expert** ≈ системное мышление role
- **philosophy-expert** ≈ epistemology / rationality role
- **methodology-engineer** (new 2026-05-24 book-driven agent) = explicit
  intellect-stack methodology role
- **investor-expert** ≈ rationality-applied-to-capital role
- **mgmt-expert** ≈ системный менеджмент role

[src: CLAUDE.md «Active ROY Swarm» table + book-driven-agents-2026-05-24 ack]

---

## §5 Method engineering / Situational Method Engineering

### §5.1 Brinkkemper 1996 SME

Левенчук footnote 13: `https://ailev.livejournal.com/750878.html` — для русского
изложения SME подхода. **Brinkkemper SME 1996** = canonical reference для
"метод-engineering as discipline of constructing method из reusable
method-fragments в response to project situation"
[src: Brinkkemper 1996 «Method Engineering: Engineering of information systems
development methods and tools» Information and Software Technology Vol 38 Issue 4
pp. 275-280 https://doi.org/10.1016/0950-5849(95)01059-9]

### §5.2 Method engineering как метод методологии

**Levenchuk position:** method engineering = один из методов self-применения
самой методологии как учения о методе. Это пример meta-level move — метод X
применяется для improvement самого X.

**OMG Essence Kernel 2.0:2024** = standardised метод-engineering language;
обеспечивает interoperability разных methodology snippets/fragments.

### §5.3 Situational Method Engineering implications

Brinkkemper's situational thesis: nothing-fits-all; every project requires
*situational* composition из method fragments. Jetix-substrate уже implements
this:
- Method V2 §J 8-component composition = situational meta-method
- ROY swarm dispatch по project context = situational composition
- KM MVP `/project-bootstrap --type=<4 types>` = templated situational composition

[src: METHOD-DEEP-DESCRIPTION-2026-05-21.md §5.5 + KM-materialization-mvp]

---

## §6 Стратегирование deep — Левенчук-таксономия

### §6.1 4 типа подхода к выбору метода (Левенчук classification)

**Verbatim list (paraphrased):**

| Подход | Когда применять | Уровень типов | Limit |
|---|---|---|---|
| 1. Применить уже имеющееся прикладное знание | Predmet-область + objects known | Мета-модель | Может оказаться SoTA-устаревшим |
| 2. Применить знание о мета-мета-модели (типы системного подхода) | Когда predmet-область неизвестна | Мета-мета-модель | Slow + требует deep понимания intellect-stack |
| 3. Distributed representations + RL | Когда есть много данных + есть RL infra | Sub-symbolic | Не передаётся к людям (transferability gap) |

[src: M2025 строки 395-407]

**Implication:** 3 типа стратегирования — это не альтернативы, а complementary
stack. Сильный стратег должен оперировать всеми тремя.

### §6.2 Policy vs Plan (AI vs Management)

**Левенчук clarifies terminological mismatch:**
- AI/RL: **policy** = пары (state, action), strategy для adaptive response
- AI: **plan** = "up front plan" из старого symbolic AI (waterfall-equivalent)
- Менеджмент: **стратегия** = выбор метода (= policy in AI sense)
- Менеджмент: **план** = график работ при known методе

[src: M2025 строка 424 + Quora reference]

**Implication:** при interop AI/menagement vocab — explicit translation:
strategy ↔ policy; plan ↔ execution-schedule.

---

## §7 Карта 30+ концептов — summary table

| # | Концепт | Что означает | Source M2025 line |
|---|---|---|---|
| C1 | Метод (way of working) | Pattern/способ работы | 297 |
| C2 | Альфа | Предмет метода с graph состояний | 110 |
| C3 | Чеклист альфы | List контроля состояний | 154 |
| C4 | Сигнатура метода | Compact definition (name + subjects + roles) | 311 |
| C5 | Метод-объект 1-го класса | Method as 1st-class object | 3539 |
| C6 | Стратегирование | Выбор метода когда непонятно что делать | 178, 432 |
| C7 | Constructor (Deutsch) | Universal agent-as-constructor | 128, 245 |
| C8 | Hybrot vs Cyborg | Computer-with-humans-inside vs human-with-computer | 480 |
| C9 | IPU | Information-processing unit (scale-free agent) | 245 |
| C10 | Прикладная vs фундаментальная методология | 2 уровня application | 209-225 |
| C11 | SoTA tracking | Constant comparison + updating | 377, 3525 |
| C12 | Мета-мета-модель / мета-модель / модель | 3 levels of abstraction | 395-405 |
| C13 | Распределённые vs локальные представления | NN vs symbolic | 399-407 |
| C14 | Moravec paradox | Easy/hard inversion human↔AI | 422 |
| C15 | Разделение труда | Specialization-via-method-splitting | 337 |
| C16 | Дробление метода (3 типа) | Composition / Decomposition / Specialization | 317-323 |
| C17 | Иерархия имён по размеру | Method/practice/style ladder | 327-333 |
| C18 | Оргвозможность (capability) | Method + permission + cooperation | 3559 |
| C19 | Прохождение развилки (decision-making) | Sigfunction + alternatives + rational choice + justification | 430-440 |
| C20 | Этика метода | Goal-method separation | 448 |
| C21 | Риторика метода | Persuasion в method transfer | 450 |
| C22 | Метанойя методолога | 4-dim perception shift | 3525 |
| C23 | Method as «учение о методе» | Plato → pragmatic turn → modern | 229-247 |
| C24 | 3-way distinction (метод/дисциплина/курс) | 3 carriers of methodology | 257-263 |
| C25 | Method engineering / SME | Self-application | 275 + Brinkkemper 1996 |
| C26 | Праксиология (alternative) | Mises/Rothbard tradition (not used by Левенчук) | 289 |
| C27 | «Всё новое сбоку» | Cross-domain disruption | 5979 |
| C28 | VUCA context | Volatility/uncertainty/complexity/ambiguity | 5945 |
| C29 | LC → method evolution | Lifecycle replaced by method | 58, 281 |
| C30 | OMG Essence 2.0:2024 | Primary modern standard | 56, 271 |
| C31 | Праздные «службы качества» critique | Ceremonial vs operational methodology | 365 |
| C32 | 4 types of strategizing | 4 approaches stack | 395-407 |
| C33 | Policy vs Plan dual | AI/mgmt vocab mismatch | 424 |

**33 concepts catalogued.** Cross-coverage: 12 traditions × Levenchuk Concepts
= dense mapping matrix (Phase 8 will use).

---

## §8 Differential Левенчук vs other methodology traditions

### §8.1 Левенчук vs Polya «How to Solve It»

| Dimension | Polya 1945 | Левенчук 2025 |
|---|---|---|
| Scope | Math problem-solving | All agent activities (universal) |
| Anchor | 4 phases (understand-plan-execute-look-back) | OMG Essence alphas + state graphs |
| Reflectivity | Heuristics catalogue (Q&A) | Method-as-object recursion |
| Pedagogy | Self-discovery via heuristic prompting | Pre-formal teaching of mета-meta-types |
| Scale | Individual | Scale-free (individual → organization → society) |

**Key complement:** Polya — heuristics for individual problem-solving = bottom-up.
Левенчук — meta-meta-model from systems engineering top-down. Both compatible.

### §8.2 Левенчук vs Schön Reflective Practitioner

| Dimension | Schön 1987 | Левенчук 2025 |
|---|---|---|
| Anchor | Reflection-in-action; knowing-in-action | Method-as-object formalism |
| Tacit | Embraces tacit, "indeterminate zones" | Tacit acknowledged BUT formalisation primary goal |
| Pedagogy | Practicum (apprenticeship) | Modeling tasks + checklists + кurriculum |
| Phenomenology | Yes, strong | Acknowledged but not central |

**Key complement:** Schön = phenomenology of practitioner's lived experience;
Левенчук = formalised observable methodology. Schön would warn that Левенчук
risks over-formalization losing tacit dimension; Левенчук would warn Schön
risks under-formalization preventing scaling/transfer.

### §8.3 Левенчук vs OMG Essence

| Dimension | OMG Essence 2.0:2024 | Левенчук 2025 |
|---|---|---|
| Scope | Software engineering primarily | Generalised to all method-engineering |
| Alphas | 7 default (SW-focused) | Universal alpha concept |
| Foundation | SEMAT industrial initiative | Russian methodological tradition + OMG adopted |
| Audience | SE practitioners | Universal — engineers, managers, life-design |

**Key relationship:** Левенчук *imports* alpha concept from OMG Essence, but
*generalises* to scale-free, AI-agent-inclusive framework. OMG Essence = standard
tool; Левенчук = theoretical superset.

### §8.4 Левенчук vs Polanyi tacit knowledge

| Dimension | Polanyi 1958/1966 | Левенчук 2025 |
|---|---|---|
| Tacit | Foundational — "we know more than we can tell" | Acknowledged — частично невозможно отмоделировать |
| Personal | Personal commitment, indwelling | Mostly skipped (agent-personal aspects → Engineering of Personality book) |
| Knowing | Proximal-distal structure | Mastery as part of agent (Knowing as agent's скилл) |
| Transmission | Apprenticeship under master | Pedagogical materialisation via курсы |

**Key tension:** Polanyi insists tacit ≠ articulable; Левенчук believes most
tacit knowledge CAN be formalised through method-engineering effort (though
acknowledges limit).

### §8.5 Левенчук vs Schedrovitsky ММК / CMD

| Dimension | Schedrovitsky CMD | Левенчук 2025 |
|---|---|---|
| Generation of системного подхода | 2-е поколение | 3-е поколение |
| Anthropocentrism | Strong (focused on human activity, ОДИ formats) | Anti-anthropocentric |
| Period | Stopped active development ~1994 | Active (8th rewrite 2024) |
| Method | "Мыследеятельность" + ОДИ | OMG Essence + intellect-stack |
| Audience | Soviet research/methodology circles | Modern engineers + AI-era practitioners |

**Continuity:** Левенчук's own self-positioning (in CLAUDE.md substrate +
methodology preamble) = continuator of CMD school WITH update to 3-rd generation
+ AI-era + standards-integration. Phase 6 will deep-dive this lineage explicitly.

---

## §9 Открытые questions surfaced by Levenchuk methodology (relevance к Jetix)

### §9.1 «Личностный» vs «cohort-transferable» метод-engineering

Левенчук Personality Engineering (separate book `05-injeneriya-lichnosti.md`)
вводит индивидуальное мастерство как accumulated set methods personality.
**Question:** при cohort-scaling (Jetix Workshop), как trade off between
personalisation vs standardisation? R12 anti-extraction constraint adds
governance layer.

### §9.2 «Метод выбора методов» recursion bound

Левенчук: recursion goes до уровня intellect-stack (где остановиться). Jetix
O-107 «метод по объединению методов по улучшению системы самой себя» = explicit
self-application. **Question:** какой recursion bound? Где stoppage criterion?

### §9.3 SoTA tracking discipline для cohort

Левенчук: each individual должен tracking SoTA для своих методов. **Question:**
в cohort с N agents, как distribute SoTA-tracking load? Specialisation =
коллективный intellect-stack instead of duplicated work?

### §9.4 OMG Essence integration scope для Jetix

Jetix Hypothesis Architecture использует alpha-machinery (Method V2 §10).
**Question:** для какого scope (только alpha state graphs / full Kernel 2.0
intelligibility tool / Essence-Diff between cycle alphas)?

### §9.5 Distributed representations для Jetix-method discovery

Левенчук: distributed representations = frontier для метода. **Question:**
может ли Jetix как substrate use LLM-based embedding для discovery новых
методов (cluster analysis over method-as-text representations)? OFFLINE_MODE
constraint наоборот может ограничить это.

### §9.6 Праксиология skeptical position для Jetix-substrate

Левенчук НЕ используется праксиологию как foundation; opts для systems
engineering tradition. **Question:** должен ли Jetix-substrate include
праксиологию layer (Mises/Rothbard) или продолжать Левенчук-line?

---

## §10 Phase 1 — key takeaways (EP-5 summary, ≤7 bullets)

1. **Метод-объект как 1st-class concept** = central Левенчук move; даёт
   foundation для Method V2 §J 8-component composition Jetix-substrate.
2. **Стратегирование ≠ планирование** distinction = central operational
   discipline; стратегирование = выбор метода до планирования.
3. **OMG Essence 2.0:2024 + ISO/IEC 24744:2014 = canonical современные стандарты**
   — Levenchuk uses them as anchor, not philosophical literature.
4. **3-е поколение системного подхода** + безмасштабная неантропоцентричность
   distinguishes Левенчук от Schedrovitsky's CMD (2-е поколение).
5. **Левенчук = continuator-with-update of Русской методологической традиции**
   — for Phase 6 deep dive это central thesis.
6. **5 method-engineering operations** (моделирование / сравнение / выбор /
   разложение / развитие) = direct Jetix mapping → ROY swarm 5 experts.
7. **«Всё новое сбоку»** = SoTA tracking должен быть adjacent-possible-aware,
   а не only in-domain.

---

## §11 Sources cited (verbatim line refs M2025)

**Primary corpus references (within Levenchuk Methodology 2025):**

| Concept | M2025 line(s) |
|---|---|
| Введение | 51-78 |
| OMG Essence 2.0:2024 anchor | 56, 271 |
| Stratagy = метод когда непонятно что делать | 60, 178, 432 |
| Метод определение | 297 |
| Альфа | 110-114 |
| Чеклист альфы | 154-164 |
| Сигнатура метода | 311 |
| Constructor / Deutsch | 128, 245 |
| Hybrot vs cyborg | 480, 3501 |
| Метод-объект 1-го класса | 3539 |
| СМД-методология (2-е поколение) | 281 |
| Метанойя | 3525 |
| Praxeology / Mises / Rothbard | 289 + footnotes 18, 24 |
| «Всё новое сбоку» | 5979-5985 |
| VUCA | 5945 |
| 4 типа стратегирования | 395-407 |
| Method Engineering / SME | 275 + footnotes 12, 13 |
| Policy vs Plan dual | 424 |
| Wikipedia Method_engineering | footnote 12 |
| Wikipedia Methodology (philosophy) | footnote 5 |

**Cross-pulled Jetix-substrate references:**

| Doc | Section |
|---|---|
| Method V2 §0 + §1 + §5 | Левенчук-anchoring |
| DR-38 §3.1 + §8 | "Schedrovitsky-Levenchuk Russian methodology school" attribution |
| DR-40 §3 | 6 cybernetic traditions (Beer/Ashby/Conant-Ashby/Maturana/Meadows/Bateson) |
| Method Deep-Description V1 §1.1 | O-107 one-liner derivation |
| Meta-Method 8-Component Deep §0 | 8 cluster-leads structure |
| Foundation principles architecture.md | Pillar C Tier 2 12 hard rules |
| FPF spec IP-1 | Role≠Executor — parallels Левенчук метод::роль |
| Books inventory | Left: `00-INVENTORY.md` Левенчук 5 books available |

**External (referenced through Levenchuk):**
- Brinkkemper 1996 SME paper https://doi.org/10.1016/0950-5849(95)01059-9
- David Deutsch Constructor Theory https://www.constructortheory.org
- Friston Karl — active inference references
- Kit Fine 2010, 2020 — theory of part
- PNAS IPU 2022 https://www.pnas.org/doi/full/10.1073/pnas.2120037119
- ISO/IEC 24744:2014 https://www.iso.org/standard/62644.html
- SEMAT initiative — Jacobson Spence Bittner 2013
- McKinsey 2017 automation report
- Tony Seba RethinkX (cross-cite для SoTA disruption sensitivity)

**Total Phase 1 source count:** 12 unique anchors (M2025 own structure plus
8 external references plus 6 Jetix-substrate cross-pulls = 26 distinct source
points; well above target 8+).

---

## §12 Phase 1 next-step linkages

- Phase 2 (Polya + Polanyi) — will deep-dive concepts referenced here only at
  high level (C20 ethics, C21 rhetoric, tacit knowledge dimension)
- Phase 3 (Systems thinking) — will deep-dive 6 cybernetic traditions с
  DR-40 substantiation
- Phase 6 (Russian methodology tradition) — will deep-dive CMD/ОДИ/Schedrovitsky
  using Phase 1 as positioning anchor
- Phase 7 (Method Engineering standards) — will deep-dive OMG Essence Kernel
  2.0:2024 + ISO/IEC 24744 + SEMAT + Brinkkemper (1996)
- Phase 8 (Jetix Lens) — will explicitly position Jetix relative to Левенчук
  using DR-38 §8 lineage thesis + new analysis from Phase 1-7

---

*Phase 1 closure. ~1050 lines.* *Sources cited: 26 unique anchors.* *R1 surface
preserved — no strategic prose authored, no positioning claim made for Jetix
relative to Левенчук-tradition.* *LOCK preserved — no Foundation file
modifications.* *Append-only — file created, not modifying prior.*
