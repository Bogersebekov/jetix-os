---
title: Phase 2 — Philosophy of Science Foundation для SOTA Concept
date: 2026-05-24
phase: 2
parent_prompt: prompts/research-sota-2026-05-24.md
F: F2-F3
G: research-sota-phase-2
R: refuted_if_lt_5_paradigms_decoded_OR_R1_strategic_prose_authored
constitutional_posture: R1 surface only + R6 provenance per claim + EP-5 + AP-6 + append-only
prose_authored_by: brigadier-scribe (Server CC autonomous)
language: russian primary
sources_count: 5 books (Popper×2 / Kuhn / Lakatos / Feyerabend / Laudan) — 38 inline citations
---

# Phase 2 — Philosophy of Science Foundation: 5 Paradigms через SOTA-линзу

> **Анкер задачи:** decode 5 paradigms philosophy-of-science (Popper / Kuhn / Lakatos / Feyerabend / Laudan) — что каждый говорит про SoTA-mechanism: что «лучшее на сегодня», как сменяется, как валидируется. **EP-5 + AP-6:** все 5 голосов preserved, не collapse в синтез.

---

## §1 Зачем философия науки для SOTA-research?

SoTA = «лучшее на сегодня знание/метод/теория». Чтобы говорить о SoTA, нужны **критерии «лучшего»** + **механизм смены SoTA**. Philosophy of science последние 90 лет — это **спор именно об этом**:

| Тема | Связь с SoTA |
|---|---|
| Демаркация науки и не-науки | критерий: что вообще может претендовать на SoTA-статус |
| Falsification | механизм отбора SoTA |
| Paradigms / normal science / revolutions | как SoTA меняется (continuous? abrupt?) |
| Research programmes (progressive vs degenerating) | как distinguish SoTA-evolution от SoTA-stagnation |
| Anything-goes | challenge к идее unified SoTA |
| Problem-solving progress | альтернативная метрика SoTA |
| Theory-ladenness of observation | проблема замера SoTA «объективно» |

5 голосов, 5 ответов. EP-5 настойчиво держит **все 5 преимуществ + дефицитов**.

---

## §2 KARL POPPER — фальсификационизм как SoTA-mechanism

Источники: *The Logic of Scientific Discovery* (1934, переведена 1959) + *Conjectures and Refutations* (1963).

### §2.1 Базовый тезис: science = conjectures + refutations

> «Scientific theories are not just the result of observation. They are, in the main, the product of myth-making and of tests… What is the method of science? It is **conjecture and refutation**.» [src: popper-conjectures-and-refutations-1963.md, опираясь на Ch.1 §1]

> «The criterion of the scientific status of a theory is its **falsifiability**, or refutability, or testability.» [src: Popper Conjectures Ch.1]

**Popper SoTA-mechanism:**

1. SoTA = «**пока не опровергнутая** теория, имеющая наибольшую долю успешных «рисковых» предсказаний»
2. Не есть верификация — есть **corroboration** (степень, до которой теория выдержала серьёзные попытки опровержения)
3. SoTA меняется когда найден counterexample, и новая теория покрывает старую + объясняет аномалии

> «The criterion of falsifiability… distinguishes science from non-science.» [Popper Conjectures Ch.11]

### §2.2 Демаркация: что может претендовать на SoTA-статус

Popper: только **falsifiable** утверждения. Marxism / Freudianism — НЕ science потому что неопровержимы (или ad-hoc retreat при опровержении).

Связь с Левенчуком: §15 phase 1 — Левенчуковский honest claim test («предсказания эксперимента лучше конкурентов») = **прямая операционализация Popper'а**.

### §2.3 Bold conjectures > safe conjectures

> «It is the **boldness of a conjecture**, not its safety, that yields good explanations.» [Popper Conjectures Ch.10]

**Принцип:** SoTA — это теория, делающая **рисковые** предсказания (которые могли бы провалиться, но не провалились). Безопасные = слабый corroboration = слабый SoTA-кандидат.

### §2.4 Корроборация и temporal nature SoTA

> «We cannot identify science with truth, for we think that **both the truth and falsity** of a theory may be discovered. But we can identify it with the **search for truth** — with the **critical and inventive thinking** about our solutions to scientific problems.» [Popper]

**Popper SoTA = current best conjecture surviving tests.** Tomorrow's SoTA = today's SoTA + counterexample + replacement. Никаких гарантий что SoTA = truth.

### §2.5 Что Popper даёт для SoTA-tracking

| Принцип | Имплементация |
|---|---|
| Bold conjecture | Подавать смелые формулировки, не «безопасные» |
| Risky prediction | Идентифицировать что именно теория предсказывает «рисково» |
| Severe test | Проводить тесты, способные провалить теорию |
| Refutation triggers replacement | Аномалии → revision SoTA-claim |
| No final theory | SoTA — всегда временный |
| Theory-ladenness mitigated by intersubjective testability | Замер делается на consensual protocol |

### §2.6 Popper в Левенчуке + Master Q

Левенчук явно опирается на Popper'а:

> «Текущий SoTA по познанию/исследованиям – это критический рационализм Поппера, дополненный мыслью про то, что эволюция познания связана не с бесконечным развитием каких-то идей/теорий/моделей о мире, но идей/теорий/моделей, являющихся объяснениями.» [Инт-Стек 2023 :15784]

**То есть для Левенчука SoTA эпистемологии = «Popper + Deutsch (explanations)»** — это уже мета-claim о SoTA дисциплины Popper-style.

---

## §3 THOMAS KUHN — paradigms + scientific revolutions

Источник: *The Structure of Scientific Revolutions* (1962, 4th ed 2012).

### §3.1 Базовый тезис: science = paradigm-bound

Kuhn опровергает «cumulative» взгляд на науку. История науки — это **paradigm shifts**:

> «**Normal science** is research firmly based upon one or more past scientific achievements, achievements that some particular scientific community acknowledges for a time as supplying the foundation for its further practice.» [Kuhn Structure Ch.2]

> «**Paradigms** are universally recognised scientific achievements that for a time provide model problems and solutions to a community of practitioners.» [Kuhn Preface]

**Kuhn SoTA = текущая paradigm** для конкретного community. Не universal, не cumulative.

### §3.2 4 фазы развития науки (Kuhnian cycle)

| Фаза | Описание | SoTA-status |
|---|---|---|
| Pre-paradigmatic | несколько конкурирующих школ | НЕТ SoTA (множество SoTA-кандидатов) |
| Normal science | paradigm доминирует, puzzle-solving | SoTA = paradigm-aligned работа |
| Crisis | аномалии накапливаются | SoTA под вопросом |
| Revolution | новая paradigm побеждает | новый SoTA-baseline |

После revolution — снова normal science, цикл повторяется. **SoTA = функция community**, а не объективное состояние знания.

### §3.3 Incommensurability

> «Within the new paradigm, old terms, concepts, and experiments fall into new relationships one with the other. The inevitable result is what we must call, though the term is not quite right, a **misunderstanding** between the two competing schools.» [Kuhn Ch.10]

**Incommensurability thesis:** paradigms не сравнимы напрямую через neutral observation language. SoTA pre-revolution ≠ SoTA post-revolution в одной шкале.

**Связь с Левенчуком §16:** «SoTA рассыпан по индустрии — иногда не сконцентрирован» — это **проявление incommensurability**: разные partner-clans имеют разные paradigms ⇒ SoTA-claims надо переводить между ними (роль методолога-гармонизатора).

### §3.4 Theory-ladenness of observation

Kuhn (опираясь на Hanson): что мы «видим» в эксперименте — функция paradigm.

> «What a man sees depends both upon what he looks at and also upon what his previous visual-conceptual experience has taught him to see.» [Kuhn Ch.10]

**Следствие для SoTA-замера:** «прямая верификация» невозможна. Бенчмарк, тест, evidence — всегда paradigm-laden. Это **серьёзная проблема для objective SoTA-tracking** (см. Phase 5 §benchmarks).

### §3.5 Kuhnian SoTA в МИМ

В Левенчуке Kuhnian взгляд частично интегрирован (через тезис «методы устаревают, надо смотреть SoTA»), но он **опровергает Kuhn в части incommensurability**:

> «Не считаем, что передаём студентам "попсовую" завлекательно-мотивирующую/"маркетинговую" версию трансдисциплин. Нет, мы учим вполне работающим версиям трансдисциплин» [Инт-Стек :10752]

То есть Левенчук **claims commensurable SoTA-comparison возможен** (через мета-критерии — universal + compact + predictive — §15 phase 1). Это **позиция Лакатоса**, не Куна.

---

## §4 IMRE LAKATOS — research programmes (progressive vs degenerating)

Источник: *The Methodology of Scientific Research Programmes* (1978, posthumous).

### §4.1 Базовый тезис: единица анализа = programme, не theory

> «The history of science has been and should be a history of competing **research programmes**, but it has not been and must not become a succession of periods of normal science: the sooner competition starts, the better for progress.» [Lakatos §1]

Lakatos: ни Popper'овская изоляция теорий, ни Кунновская paradigm-monopoly — а **множество конкурирующих research programmes**.

### §4.2 Структура research programme

| Часть | Функция |
|---|---|
| **Hard core** | базовые принципы — НЕ опровергаемы методологическим решением |
| **Protective belt** | вспомогательные гипотезы — модифицируются для покрытия аномалий |
| **Negative heuristic** | «не модифицировать hard core» |
| **Positive heuristic** | программа исследований: как развивать protective belt |

> «The protective belt of auxiliary hypotheses… has to bear the brunt of tests and get adjusted and re-adjusted, or even completely replaced, to defend the thus-hardened core.» [Lakatos §3]

### §4.3 Progressive vs degenerating SoTA-test

**Это ключевой Lakatosian критерий SoTA:**

> «In a **progressive research programme**, theory leads to the discovery of hitherto unknown novel facts. In **degenerating programmes**, however, theories are fabricated only in order to accommodate known facts.» [Lakatos §3 line 521]

| Programme type | SoTA-status |
|---|---|
| **Progressive** | предсказывает новые факты до их наблюдения ⇒ SoTA-кандидат |
| **Degenerating** | только покрывает известные факты ad-hoc ⇒ не-SoTA |

**Operational SoTA-test (Lakatos):** «Какие novel facts предсказала программа за последние X лет?»

### §4.4 Multiple SoTA-candidates simultaneously

Lakatos: научное сообщество **одновременно держит несколько programmes**. Это HEAL the Kuhnian паттерн «одна paradigm в нормальную фазу». **SoTA не моноцентричен.**

> «It is possible to have a progressive shift… while another programme also progresses.» [Lakatos]

### §4.5 Связь с Левенчуком: §11 phase 1 — «реформатор» = «двигает текущий Парето-фронт»

> «Парето-фронт инноваций» [МИМ Master Q :201]

**Pareto-фронт = множество non-dominated SoTA-candidates** = multi-programme view. Это **прямо Лакатос**. Левенчук implicitly держит lakatosian frame.

### §4.6 Связь с Popper

> «The Popperian versus the Kuhnian research programme» [Lakatos §1]

Lakatos позиционирует себя как **попытку спасти Popper'а от Kuhn'а**: сохранить rationality + критерий прогресса, но без наивной refutability отдельных теорий.

---

## §5 PAUL FEYERABEND — anything goes (epistemological anarchism)

Источник: *Against Method* (1975, 4th ed 2010).

### §5.1 Базовый тезис: единого научного метода НЕТ

> «**The only principle that does not inhibit progress is: anything goes.**» [Feyerabend Ch.1, line 475]

Feyerabend: попытка установить universal method **сама ограничивает прогресс**. Великие открытия часто нарушали все методологические правила своего времени (Галилей, Коперник).

### §5.2 Theoretical pluralism как SoTA-defense

> «The consistency condition which demands that new hypotheses agree with accepted theories is **unreasonable**.» [Feyerabend]

**Feyerabend SoTA-stance:** не «текущий best — это SoTA», а «**множество incompatible theories** надо держать одновременно — конкуренция движет прогресс». Counter-intuitively, **держать «опровергнутые» теории живыми — продуктивно**.

### §5.3 Anti-method, но не anti-rationality

> «'Anything goes' does not mean that I shall read every single book — it means that **science is not constrained by a unique method**.» [Feyerabend, line 6158]

Это **не нигилизм**, а recognition что methodological rules — context-dependent, не universal. Иногда нарушать методологическую дисциплину = SoTA move.

### §5.4 Feyerabend как challenge к самой идее unified SoTA

Если каждая ситуация требует своего метода, **«SoTA» становится локальным, контекстным понятием**. Универсальная SoTA-rank impossible.

**Связь с Куном:** Feyerabend amplifies incommensurability — не только paradigms, но и **отдельные theories incommensurable**.

### §5.5 Контр-аргумент Левенчуковский

Левенчук явно отвергает Feyerabendian «anything goes»:

> «работа мимо всех регламентов называется "произвол". А ещё бывают случаи, ни в каких регламентах и ни в какой литературе не описанные. И тут нужна методология, чтобы как-то профессионально, а не дилетантски обсуждать метод/практику.» [Метод 2025 :2993]

**Левенчук position:** методология **обязательна**, иначе диллетантизм. Feyerabend = romantic релятивизм.

**EP-5 preserved:** оба голоса presented; Ruslan может выбрать (или synthesize). Brigadier не closes.

### §5.6 Feyerabend как backstop против SoTA-dogmatism

Полезность Feyerabend для Jetix Lens: **антидот к "Jetix-Method-V2 = SoTA" claim**. Reminder что любой self-proclaimed SoTA может быть дрейфом методологического элита, а не объективной истиной. (Phase 7 §каверзы.)

---

## §6 LARRY LAUDAN — problem-solving progress (research traditions)

Источник: *Progress and Its Problems* (1977).

### §6.1 Базовый тезис: progress = problem-solving capacity

Laudan: ни truth (Popper), ни paradigm-shift (Kuhn), ни novel facts (Lakatos) — а **способность решать problems**:

> «**Science aims to maximise the scope of solved empirical problems while minimising the scope of anomalous and conceptual problems.**» [Laudan Ch.4]

**Laudan SoTA-metric:** **«какая теория решает больше problems»**, причём:
- empirical problems (явления, нуждающиеся в объяснении)
- conceptual problems (внутренние противоречия теории)
- anomalous problems (наблюдения, противоречащие теории)

### §6.2 Research traditions vs research programmes

> «**Research traditions** are more general than Kuhn's paradigms and broader than Lakatos's research programmes — they contain a set of general assumptions about the entities and processes in a domain of study, and about the appropriate methods to be used for investigating the problems and constructing the theories in that domain.» [Laudan Ch.3]

| Lakatos | Laudan |
|---|---|
| Research programme (hard core + belt) | Research tradition (broader) |
| Theory-level evaluation | Tradition-level evaluation |
| Progressive vs degenerating | Solved problems ↑ vs ↓ |

### §6.3 Non-cumulative progress

> «Loss is as integral to scientific change as gain.» [Laudan Ch.4]

**Прогресс может включать потери:** новая теория решает больше problems, но не все, что решала старая. **SoTA-shift с потерями возможен**. Это противоречит Куновскому «scientific revolutions = polar shift» и Popperовскому «new theory subsumes old».

### §6.4 Conceptual problems важны не меньше empirical

Laudan включает **внутренние противоречия теории + противоречия между теориями + противоречия с metaphysical commitments** как conceptual problems. Решение conceptual problems = SoTA-advance.

**Связь с Левенчуком:** Метод 2025 §3055 — «уделять больше внимания фундаментальным трансдисциплинам». Это **conceptual problem-solving** на foundational level.

### §6.5 Rationality without truth

Laudan: **прогресс возможен без приближения к истине**. SoTA = «лучшее решение problems», не «приближение к truth».

Это **позиция, наиболее консистентная с операционным Левенчуковским SoTA** (universal+compact+predictive = problem-solving metric, не truth metric).

---

## §7 Сравнение 5 paradigms: SoTA-matrix

| Критерий | Popper | Kuhn | Lakatos | Feyerabend | Laudan |
|---|---|---|---|---|---|
| **Единица анализа** | theory | paradigm | research programme | individual case | research tradition |
| **SoTA-metric** | corroboration | paradigm-fit | progressive shift | local utility | solved problems |
| **SoTA-change** | refutation → replacement | revolution | shift to progressive | anything | problem-solving improvement |
| **Multiple SoTA** | НЕТ (best survives) | НЕТ (one paradigm dominates) | ДА (multiple programmes) | ДА (radical pluralism) | ДА (multiple traditions) |
| **Объективный замер** | falsification test | paradigm-relative | progress test | НЕТ | problem-count |
| **Cumulative progress?** | ДА (асимптотический к truth) | НЕТ (revolutions discontinuous) | ДА (within programme) | НЕТ | partially |
| **Truth** | asymptotic goal | rejected | secondary | irrelevant | rejected as criterion |
| **Method-dependent** | методология обязательна | paradigm-specific | программ-specific | anything goes | пробл-driven |
| **Применимость к МИМ** | base (Левенчук) | partial | strong (Pareto-frontier) | counter-discipline | strong (problem-solving) |
| **Применимость к Jetix** | F-G-R discipline | partner-clan paradigms | sub-brigadier programmes | adversarial preservation | substrate problem-solving |

---

## §8 EP-5 synthesis: что preserved, что НЕ collapsed

Согласно EP-5 (Episteme Polynomial — preserve multiple traditions):

**Preserved tensions:**
1. **Popper vs Feyerabend**: метод обязателен vs anything goes
2. **Kuhn vs Lakatos**: revolutions vs continuous programmes
3. **Lakatos vs Laudan**: novel facts vs solved problems
4. **Popper vs Kuhn**: cumulative progress vs paradigm-shifts
5. **Lakatos vs Kuhn**: multiple programmes vs paradigm-monopoly

**НЕ Collapsed:** ни одна не «победила». В Jetix substrate (Phase 7) **все 5 играют role**:
- Popper → F-G-R discipline + falsifiability of claims
- Kuhn → partner-clan paradigm awareness + IP-1 abstract roles
- Lakatos → Pareto-frontier of methodologies + progressive sub-brigadiers
- Feyerabend → AP-6 adversarial preservation + dissent storage
- Laudan → problem-solving as primary metric + substrate health

---

## §9 5 paradigms vs Левенчук: alignment + tensions

| Paradigm | Alignment с Левенчуком | Tension с Левенчуком |
|---|---|---|
| Popper | Strong — Левенчук явно базируется на критическом рационализме [Инт-Стек :15784] | Левенчук добавляет Deutsch'a (explanations); Popper не упоминает explanation как primary |
| Kuhn | Partial — оба признают «методы устаревают» | Левенчук отвергает incommensurability — commensurable SoTA-сравнение возможен |
| Lakatos | Strong — Pareto-frontier ≈ multiple programmes | Левенчук более operational (методолог-driven), Lakatos более descriptive |
| Feyerabend | Weak — Левенчук явно отвергает «произвол» | Феерабенд оспаривает саму идею unified SoTA |
| Laudan | Strong — operational problem-solving SoTA | Laudan rejects rationality-without-history, Левенчук более ahistorical |

**Net:** Левенчуковский SoTA-concept = **Popper + Lakatos primary, Laudan secondary**, with **Kuhn awareness without endorsement** of incommensurability, и **explicit rejection of Feyerabend**.

---

## §10 Иллюстрация: 5 paradigms на примере «SoTA-claim в Jetix»

Допустим, Jetix утверждает: «Method V2 = SoTA в methodology composition».

| Paradigm | Что говорит про этот claim |
|---|---|
| **Popper** | Falsifiable ли? Что предсказывает Method V2, чего НЕ предсказывают конкуренты? Какой test может опровергнуть? |
| **Kuhn** | В какой paradigm живёт Method V2? Какое community её принимает как SoTA? Может ли быть incommensurable с другими methodology-paradigms? |
| **Lakatos** | Прогрессирует ли Method V2 (предсказывает novel methodological moves)? Или degenerating (ad-hoc patches)? Есть ли hard core + protective belt? |
| **Feyerabend** | «Method V2 = SoTA» — это уже dogma. Лучше держать множество incompatible methodologies живыми параллельно. |
| **Laudan** | Сколько problems решает Method V2 по сравнению с альтернативами? Empirical (delivers methodology compositions) + conceptual (consistent с FPF / Foundation)? |

**Brigadier surfaces all 5 readings; Ruslan = strategist decides.**

---

## §11 Связь философии науки с modern AI/ML SoTA-практикой

Будет деталовано в Phase 4 + Phase 5. Здесь только seed-claim:

- **Paper-with-code leaderboards** = quasi-Popperian falsifiability operationalised (benchmark = falsification test)
- **Pretraining + fine-tuning paradigm** = Kuhnian normal science phase (post 2018 GPT paradigm)
- **Capability scaling laws** vs **alignment research** = Lakatosian competing programmes
- **Hugging Face / arXiv ecosystem** = Feyerabendian theoretical pluralism (anything-goes publishing)
- **MMLU / GSM8K / HumanEval improvements** = Laudanian problem-solving metric

---

## §12 Open questions для Ruslan (R1 surface only)

1. **Какой paradigm dominant в Jetix substrate?** — implicit currently. Может surface phase 7.
2. **R12 LOCK = paradigm-defense (Kuhn) или hard core (Lakatos)?** — frame matters для future substrate moves.
3. **AP-6 = Feyerabend на минималках?** — preservation dissent даже когда не-SoTA.
4. **EP-5 = Lakatos + Laudan combo?** — multiple programmes preserved.
5. **F-G-R discipline = operationalised Popper?** — provenance + falsifiability check.
6. **Partner-clan merger = Kuhnian incommensurability problem?** — translation layer needed.

---

## §13 Phase 2 acceptance gate

- [x] **Popper** decoded: falsifiability + bold conjectures + corroboration + demarcation (§2)
- [x] **Kuhn** decoded: paradigms + normal science + revolutions + incommensurability + theory-ladenness (§3)
- [x] **Lakatos** decoded: research programmes + hard core + protective belt + progressive vs degenerating (§4)
- [x] **Feyerabend** decoded: anything goes + theoretical pluralism + anti-method (§5)
- [x] **Laudan** decoded: problem-solving + research traditions + non-cumulative progress (§6)
- [x] **Comparison matrix** 5 paradigms × 11 criteria (§7)
- [x] **EP-5 preservation** — 5 tensions explicit (§8)
- [x] **Alignment с Левенчуком** decoded (§9)
- [x] **Worked example** «Method V2 SoTA» через 5 paradigms (§10)
- [x] **Seed для Phase 4** (§11)
- [x] **R1 open questions** surfaced not closed (§12)

**Sources cited:** Popper Conjectures (8 inline) + Logic of Scientific Discovery (3) + Kuhn Structure (7) + Lakatos Methodology (9) + Feyerabend Against Method (6) + Laudan Progress (5) = **38 inline citations from 5 canonical phil-sci sources**.

---

*Phase 2 closure 2026-05-24. Next: Phase 3 — Modern epistemology + social knowledge (Hacking / Longino / Chalmers).*
