---
type: knowledge-base
compiled: 2026-04-20
purpose: Unified reference для Jetix FPF adaptation (Gap Analysis + D6 writing)
sources-primary:
  - raw/external/ailev-FPF/FPF-Spec.md (Anatoly Levenchuk, March 2026, 62,202 строки)
  - raw/external/ailev-FPF/Readme.md (entry routes, 384 строки)
  - raw/external/ailev-FPF/ATTRIBUTION.md (license + citation)
sources-secondary:
  - raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md
  - raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md
  - raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md
  - raw/research/levenchuk-fpf-research-2026-04-20/R-D-essence-kernel-shsm-relation.md
  - raw/research/levenchuk-fpf-research-2026-04-20/R-E-mereology-holon-hierarchy.md
size: ~25K words / ~60 pages
status: draft
unblocks:
  - Gap Analysis Jetix vs FPF
  - D6 JETIX-FPF.md writing
attribution: Draws substantially from First Principles Framework (FPF) by Anatoly Levenchuk (https://github.com/ailev/FPF), March 2026 version. Adapted для Jetix OS internal use с acknowledgment of author's conceptual foundation.
---

# Knowledge Base — Левенчук + FPF (unified reference, 2026-04-20)

## Section 1 — About this knowledge base

### 1.1 Purpose

Это **unified reference document** для последующего использования в Jetix
FPF derivation pipeline:

1. **Gap Analysis Jetix vs FPF** — следующий шаг (mapping Jetix architecture
   к FPF patterns, выявление gaps).
2. **D6 JETIX-FPF.md writing** — написание Jetix-specific adaptation.
3. **Long-term Jetix methodology canon** — стабильный reference для
   strategist + knowledge-synth agents.

KB **digests** material из 6 inputs (1 primary FPF-Spec + 5 secondary
researches), не replicates их полностью. Это reference, не copy.

### 1.2 Sources overview

**Primary (authoritative, first-hand):**

- **`raw/external/ailev-FPF/FPF-Spec.md`** — 62,202 строки, 5.7 MB,
  Анатолий Левенчук + AI-агенты, March 2026. 11 Parts (Preface +
  A-K), pattern language с ~300+ patterns. Status: "Normative kernel,
  eternal alpha".
- **`raw/external/ailev-FPF/Readme.md`** — entry routes + quick-start.
- **`raw/external/ailev-FPF/ATTRIBUTION.md`** — citation requested,
  no formal license; conservative interpretation: internal Jetix
  reference + adaptation OK.

**Secondary (third-party compiled context, 2026-04-20 Perplexity):**

- **R-A** (~63 KB) — Левенчук as person + full corpus (books, courses,
  evolution 2000-2026, intellectual lineage).
- **R-B** (~99 KB) — 5 примитивов ШСМ deep dive (роль / альфа /
  граф создания / стратегирование / мышление письмом).
- **R-C** (~95 KB) — 16 trans-disciplines (intellect-stack) enumeration
  + hierarchy + relations к 5 примитивам.
- **R-D** (~60 KB) — Essence Kernel (SEMAT) origin + Levenchuk
  adaptation путь.
- **R-E** (~78 KB) — mereology theory + Holons (Koestler/Wilber/Fine)
  applied к organizations + AI-agent systems.

### 1.3 Triangulation methodology

Когда sources disagree — **FPF-Spec primary > secondary researches**.
Это потому что:

1. FPF-Spec — Левенчук first-hand, March 2026 (most current).
2. Researches compiled 2026-04-20 from public sources (могут быть
   slightly out of date или интерпретации third-party).
3. Researches покрывают broader context (биография, history) который
   FPF-Spec sequel НЕ содержит — здесь secondary авторитативны.

**Conflict-flagging convention:** где обнаружен conflict —
помечен `⚠ CONFLICT:` с указанием обеих позиций и предпочтённой.

### 1.4 Anti-hallucination commitments

- **Direct quotes** где FPF-Spec даёт authoritative definition —
  использованы с цитатой и pattern ID.
- **Pattern IDs verified** в FPF-Spec через line numbers (Glob/Grep
  на 62K-line файле).
- **Russian terms preserved** с English transliterations.
- **Уровни уверенности** помечены: ✅ verified в primary, 🟡 secondary
  only, ⚠ conflict / unverified.
- Если concept упомянут только в одном source без cross-validation
  — помечен 🟡 with source attribution.

### 1.5 How to use this document

**For Gap Analysis (next task):**
- Section 5 (FPF Architecture) — primary input для structural mapping.
- Section 8 (Triangulation) — list of points where adaptation
  decisions нужны.
- Section 9 (Glossary) — для consistent terminology.

**For D6 JETIX-FPF.md writing (later):**
- Sections 3 (5 primitives) + 5 (FPF patterns) — concept menu.
- Section 6 (Essence evolution) — historical lineage для context.
- Section 11 (Open questions) — Ruslan-review items.

**For long-term canon:**
- Sections 2 (intellectual context) + 7 (mereology) — depth reading
  для new agents joining strategy work.

---

## Section 2 — Anatoly Levenchuk — intellectual context

> Source attribution: primarily R-A; FPF-Spec preface gives Левенчук's
> own first-hand voice ✅; biographical material is ☆ secondary-only
> (R-A from public sources: in.wiki, ailev.livejournal.com, system-school.ru,
> arxiv.org, github.com/ailev).

### 2.1 Biographical sketch

**Анатолий Игоревич Левенчук** (born 23 January 1958, Rostov-on-Don,
Russia). Chemistry graduate of Rostov State University (РГУ), 1980.
Programmer-educator throughout 1980s. Moved Moscow 1989. Founded
**TechInvestLab** (1999) — operational consulting base for ~15 years
(Rosatom, RAO EES Rossii, ISO 15926, ArchiMate, etc.).

**INCOSE Russian Chapter:** President 2010 + 2013, Director of Research
2011-2012. Served on SEMAT executive committee 2013.

**ШСМ founding (2015):** Co-founded **Школа системного менеджмента
(ШСМ)** with Tseren Tserenov. Levenchuk holds title **научный
руководитель** (Scientific Director).

**МИМ rebranding (2025-2026):** ШСМ → **МИМ — Мастерская
инженеров-менеджеров** (Workshop of Engineer-Managers). Frame shift
от "school" к "practitioner community".

**FPF era (2024-2026):** Active development of First Principles
Framework via [github.com/ailev/FPF](https://github.com/ailev/FPF),
co-authored с AI agents (primarily Codex + GPT-5.4 Pro).

### 2.2 Intellectual lineage

Левенчук articulates **third-generation systems thinking** —
synthesis of:

**First-generation (absorbed):** Bertalanffy's General Systems Theory
(GST), Wiener's cybernetics, Koestler's holons.

**Second-generation (absorbed + critiqued):** Checkland's Soft Systems
Methodology, ISO 15288/42010 (lifecycle/architecture), ISO 15926
(4D extensionalism), **SEMAT/Essence Kernel** (Ivar Jacobson).

**Third-generation (his synthesis, 2020s):** Techno-evolution,
"continuous everything" CD/CI scaled to system development,
mereotopology + category theory как foundation, **Active Inference /
Free Energy Principle** (Karl Friston), **open-ended evolution** (NQD
OEE — Novelty/Quality/Diversity), scale-free physics-based systems
ontology.

**Russian school context:** Engages but rejects СМД-методология
(Shchedrovitsky tradition's Hegelian-Marxist dialectics). Replaces
с Popperian falsificationism + engineering pragmatism + Austrian
school praxeology (von Mises).

**Philosophical sources (per R-A):** Charles Sanders Peirce
(pragmatism, semiotics — currently formalizing в FPF semio-architecture
workstream, April 2026), John Searle (speech acts), Karl Popper,
Daniel Dennett ("hold your definition" anti-essentialism).

**Western SE positioning:** Member ACM/SIGSOFT, ASEM, ACDM. Aware of
INCOSE mainstream SE, but critiques его как "second-generation
insufficient" — misses evolutionary, continuous-delivery,
multi-agent coordination challenges.

### 2.3 Career arc (six phases)

| Phase | Period | Key output |
|---|---|---|
| Early technical | 1980-1988 | Chemistry → Rostov programming education |
| Runet pioneer | 1989-1999 | Securities markets, Libertarium, TechInvestLab |
| Industrial consulting | 1999-2010 | RAO EES, Rosatom, ISO 15926, .15926 Editor |
| INCOSE + SEMAT | 2010-2015 | INCOSE Russia President, SE Essence (arXiv 2015) |
| ШСМ + textbooks | 2015-2020 | Школа founding, annual textbook rewrites |
| AI-augmented intellect pivot | 2020-2024 | Exocortex framing, intellect stack formalization |
| FPF + МИМ era | 2024-2026 | Pattern language, semiotics workstream, AI co-authorship |

### 2.4 Current 2026 focus

Per R-A and ailev.livejournal.com posts April 2026:

1. Completing **NQD OEE** patterns в FPF (frontier/palette/portfolio).
2. **Semiotics architecture** в FPF (10-campaign plan, April 2026
   seminar).
3. **SPF/TPF** — Second/Third Principles Frameworks (domain- and
   enterprise-specific models built on FPF meta-model).
4. Methodology для human/AI **pattern-writing quality control**.
5. **МИМ practitioner community** evolution (резидентуры R0→R1→R2,
   IWE personal AI guide).

### 2.5 Where his body of work lives

**Books (Ridero, all Russian):**
- *Системное мышление 2024* — 2-volume set, 9th major rewrite,
  ISBN 978-5-0064-2853-9 / 978-5-0064-2855-3
- *Методология 2025* — ~872 pages, sequel
- *Системная инженерия 2022*
- *Системный менеджмент 2023*
- *Инженерия личности 2023*
- *Интеллект-стек 2023* — ISBN 978-5-0060-4990-1
- *Визуальное мышление* (2018)

**arXiv (English):**
- ["Towards a Systems Engineering Essence" (2015)](https://arxiv.org/abs/1502.00121)
- ["Toward an Ontology for Third Generation Systems Thinking" (2023)](https://arxiv.org/abs/2310.11524)

**Online presence:**
- Blog: [ailev.livejournal.com](https://ailev.livejournal.com) ("Лабораторный журнал", since 2003)
- МИМ: [system-school.ru](https://system-school.ru) + [aisystant.system-school.ru](https://aisystant.system-school.ru)
- Community: [systemsworld.club](https://systemsworld.club)
- Telegram: [@system_school](https://t.me/system_school)
- GitHub: [github.com/ailev/FPF](https://github.com/ailev/FPF) — 320 stars / 52 forks (April 2026)

**FPF as latest expression:** FPF-Spec.md is the current 2026 synthesis
of all prior frameworks, expressed as AI-readable pattern language.
Per R-A: "the 2026 synthesis of all prior frameworks, now expressed
as AI-readable pattern language."

---

## Section 3 — ШСМ 5 primitives (deep)

> Source attribution: R-B is the primary source for 5 primitives ⚠
> Note from R-C: "they do not appear as a named 'canonical list of
> 5 primitives' in any single Levenchuk source." 5-primitive
> framing is **R-B's analytical synthesis**, не Левенчук's own
> publishable taxonomy. Каждый primitive — first-class concept в
> specific текстах. ✅ verified что concepts существуют; ⚠ "5
> primitives" как unit — R-B's didactic frame for Jetix.

### 3.1 Critical preliminary: nature of misuse

R-B opens с principled distinction (важно для Jetix adaptation):

- **Violation by misuse:** practitioner uses ШСМ terms ("роль",
  "альфа", "стратегирование") но keeps semantics своего исходного
  domain (software, project management, HR) → ontological noise
  masquerading as systems thinking. **Более опасно**, чем полный
  отказ от ШСМ terminology.
- **Violation by omission:** practitioner не uses ШСМ terms но
  models reality correctly → less dangerous (только comm compatibility
  lost).

**For Jetix:** "Лучше говорить 'задача' и корректно моделировать,
чем говорить 'альфа' и думать о Jira-тикете" (R-B Section 1).

### 3.2 РОЛЬ (Role)

**Definition (Левенчук, "Методология 2025"):**

> «Агенты имеют роли в методе. Метод характеризуется своими
> знаниями/теориями/учениями/дисциплинами [...] Создатели — это
> агенты, всё что из методов умеет делать агент (совокупность
> мастерства агента) — это личность агента.»

**Definition (Левенчук, ailev/1741032):**

> «Если говоришь роль, то за ролью скрывается метод. [...] При
> разговоре о роли прежде всего разбираемся с методом: что и с чем
> эти роли делают»

**FPF-Spec correlation ✅:** Pattern A.2 (Role Taxonomy), A.2.1
(`U.RoleAssignment`), A.2.5 (`U.RoleStateGraph`), A.13 (Agential
Role & Agency Spectrum). FPF formalizes role как separate from
holder: holon играет role в context, role — "маска" холона
(per ailev/1776793).

**Formula:** Роль = signature метода × interest к системе × набор
мастерства. Concrete executor (human, team, AI, organization) —
holder role, не sama role.

**Role ≠ X (anti-patterns):**

| Концепт | Critical отличие |
|---|---|
| Должность (Position) | Place в org structure; role — функция в method |
| Человек (Person) | Биологический агент; роль — abstraction |
| Software class | Static description в коде; role — onto object в meta-model |
| Holacracy Role | Org governance unit; ШСМ-роль — onto object в method |
| RACI assignment | Matrix кто отвечает; ШСМ-роль — какой method применяется к каким альфам |
| ArchiMate Business Role | Behavioral; ШСМ-роль несёт signature метода |

**Strict separation: roles vs holders.** One holder может играть
несколько ролей последовательно (но не одновременно в одном методе).
Одну роль могут играть разные agents в разное время.

**Founder syndrome critique (Левенчук, ailev/1795494):**

> «Если наплодить много-много ролей, то в текущих многоагентных
> архитектурах типичный рост расхода токенов в 3-10 раз и идут
> провалы при handoff между рольными агентами»

**Dynamic role assignment запрещено** — разрушает граф создания
+ систему альф (роль назначается при создании задачи, не в ходе).

**Application examples (Jetix-relevant):**
- ✅ "Sales Lead" — describes method (lead-quality управление)
- ✅ "Delivery" — describes method (доставка ценности)
- ❌ "Ответственный" — RACI, не method
- ❌ "Помощник" — relation, не method
- ❌ "Claude Agent #3" — executor, не role

**Common mistakes:**
1. Naming role by holder, не method.
2. Более 7 accountability-items без декомпозиции (Miller's law).
3. Role describing position, не method.
4. Role совпадающая с org unit ("DevOps Team" — collective agent,
   не role).

### 3.3 АЛЬФА (Alpha)

**Definition (Левенчук, "Методология 2025"):**

> «Альфа — это предмет метода, который может быть и физическим
> объектом (системой), и абстрактным объектом (описанием).»

> «Альфа позволяет управлять вниманием создателя в ходе исполнения
> длинных цепочек операций»

> «Состояния предмета метода в альфе даются глаголами в прошедшем
> времени, эти глаголы соответствуют применённым составляющих
> разных методов к какому-то объекту»

**Origin:** OMG Essence 1.2 (2018), based on SEMAT (2009, Jacobson +
Meyer + Soley). Per ACM Queue:

> «An alpha is an essential element of the software-engineering
> endeavor — one that is relevant to an assessment of its progress
> and health»

Левенчук extends Essence-definition: scale-free, applicable beyond
software к любым проектным ситуациям.

**FPF-Spec correlation ✅:** No direct "U.Alpha" type! Concept of
"alpha" → разделено на FPF на:
- **`U.RoleStateGraph`** (A.2.5) — state machine роли
- **`U.Episteme`** (A.1, C.2.1) для knowledge alphas
- **`U.System`** (A.1) для physical alphas
- **`U.Work` / `U.WorkPlan`** (A.15.1, A.15.2) для work alphas
- **`PhaseOf`** (A.14) — temporal parts of same carrier

⚠ CONFLICT: R-B treats Alpha as core ШСМ primitive ✅. FPF-Spec
**doesn't preserve "alpha" as standalone term** — splits into more
fine-grained kernel types. Per FPF-Spec.md preface: "Alpha" не
mentioned. Per R-D Section 2.4: Levenchuk explicitly reinterprets
"alpha" as "предмет метода" в Methodology 2025. **For Jetix
adaptation:** decide whether keep "alpha" Russian-pedagogical term
OR migrate к FPF-Spec U.Type vocabulary.

**Альфа vs Work Product vs Entity vs Activity:**

| Концепт | What it is | State machine? |
|---|---|---|
| **Альфа** | Предмет метода | Да, обязательно |
| **Work Product** | Артефакт создаваемый методом | Нет (или draft/final) |
| **Entity** | Объект справочника без lifecycle | Нет |
| **Activity** | Работа по методу | Нет (это процесс) |

**Past-participle convention** ✅ (verified в OMG Essence + Левенчук):

| Неправильно | Правильно | Why |
|---|---|---|
| "qualifying" / "in qualification" | "Qualified" | State — fact, not process |
| "active" | "Activated" | Event vs description |
| "in progress" / "working" | "Started" | Verifiable fact |
| "delivering" | "Delivered" | Fact of delivery |

**For Russian:** краткие причастия: "квалифицирован", "активирован",
"начат", "доставлен", "закрыт", "принят", "согласован".

**Семантика обоснования:** Past-participle делает state машинно-читаемым
(`IF Client.state == "Qualified" THEN ...`); ensures verifiability
(checklist for completed event vs ongoing process); preserves
эпистемологическую precision (fact vs ongoing).

**Standard 7 alphas (OMG Essence Kernel):**

| Area | Alpha | States |
|---|---|---|
| Customer | Opportunity | Identified → Value Established → Viable → Addressed → Benefit Accrued |
| Customer | Stakeholders | Recognized → Represented → Involved → In Agreement → Satisfied for Deployment → Satisfied in Use |
| Solution | Requirements | Conceived → Bounded → Coherent → Acceptable → Addressed → Fulfilled |
| Solution | Software System | Architecture Selected → Demonstrable → Usable → Ready → Operational → Retired |
| Endeavour | Work | Initiated → Prepared → Started → Under Control → Concluded → Closed |
| Endeavour | Team | Seeded → Formed → Collaborating → Performing → Adjourned |
| Endeavour | Way of Working | Principles Established → Foundation Established → In Use → In Place → Working Well → Retired |

**State machine requirements:**
1. Each state — past-tense fact.
2. Each state has checklist of verifiable criteria.
3. Graph может be non-linear (returns OK).
4. Transitions attributed к role responsible.

**Common false positives (NOT alphas):**
- `Task` / `Ticket` — work item, не предмет метода
- `Meeting` — activity, не alpha
- `Document` — work product (unless documents itself is the subject)
- `Person` — agent, не alpha

**False negatives (often missed):**
- `Way of Working` — usually implicit but важен lifecycle
- `Trust` (in advisory contexts) — может иметь state machine
- `System Architecture` — может быть отдельной alpha при complex systems

### 3.4 ГРАФ СОЗДАНИЯ (Creation Graph)

**Definition (Левенчук, "Методология 2025"):**

> «моделировать граф создания [...] по мотивам OMG Essence 2.0:2024»

**Definition synthesis:** Граф создания — ориентированный мереологический
граф; узлы = системы, рёбра по отношению "кто создаёт кого / что".
Одновременно показывает целевую систему (что создаём), системы
создания (кто создаёт), надсистемы (где функционирует).

**FPF-Spec correlation ✅:** Pattern A.1 (Holonic Foundation), A.14
(Advanced Mereology с PortionOf/PhaseOf), B.1 (Universal Algebra of
Aggregation Γ), B.2 (Meta-Holon Transition MHT). FPF использует
"holarchy" / "partonomy" terminology с расширенной mereology
включая ComponentOf, ConstituentOf, PortionOf, PhaseOf, MemberOf.

**Three-level structure:**

```
Уровень 3: НАДСИСТЕМА (Supersystem)
   ↑ "operates-in" / "constrained-by"
Уровень 1: ЦЕЛЕВАЯ СИСТЕМА (Target System)
   ↑ "creates" / "methodologically-uses"
Уровень 2: СИСТЕМЫ СОЗДАНИЯ (Creation Systems)
```

**Edge types:**

| Тип | Направление | Пример (Jetix) |
|---|---|---|
| `part-of` | компонент → целое | `Sales Lead` part-of `Revenue Circle` |
| `creates` | создатель → создаваемое | `AI-agents` creates `Jetix deliverables` |
| `operates-in` | целевая → надсистема | `Jetix OS` operates-in `German Mittelstand` |
| `methodologically-uses` | создатель → метод | `Sales Lead` methodologically-uses `MECE qualification` |
| `constrained-by` | система → ограничения | `Jetix OS` constrained-by `EU AI Act` |

**Граф создания ≠:**

| Концепт | Critical отличие |
|---|---|
| Workflow / BPMN | Workflow — sequence activities; граф — onto relations |
| Dependency tree | Dep tree — technical зависимости; граф — кто создаёт кого |
| Org chart | Org chart — подчинения; граф — отношения создания |
| VSM | VSM — поток ценности; граф — supersystem context too |
| Supply chain | Supply chain — commercial; граф — SE typization с mereology |

**Recursive property:** Системы-создатели sami являются системами,
которые кто-то создаёт. Per ailev/1776793: "advanced mereology и
принципиальное свойство холонов — это многооперационная (отражающаяся
в многоуровневости иерархического kind-представления 'партономии')
сборка."

**Validation heuristics:**
- ✅ У каждой целевой системы — explicit creators
- ✅ Надсистема задаёт requirements к целевой
- ❌ Содержит только "поставщик → потребитель" без levels
- ❌ В узлах стоят activities вместо систем

### 3.5 СТРАТЕГИРОВАНИЕ (Strategizing)

**Definition (Левенчук, "Методология 2025"):**

> «метод выбора метода — стратегирование»

> «в условиях, когда вообще непонятно, что делать. А если непонятно,
> что именно делать, то и планировать ещё ничего нельзя (потребные
> ресурсы неизвестны), и работать нельзя»

**Structural positioning:**

```
СТРАТЕГИРОВАНИЕ → выбор метода (что и как делать, когда неизвестно)
        ↓
ПЛАНИРОВАНИЕ → распределение ресурсов под выбранный метод
        ↓
РАБОТА → исполнение по плану
```

**FPF-Spec correlation ✅:** Pattern E.9 (Design-Rationale Record DRR),
B.5.2 (Abductive Loop), C.11 (Decision Theory Decsn-CAL), C.18-C.19
(NQD Open-Ended Search + Explore-Exploit Governor). FPF formalizes
strategic decisions через DRR (Problem frame → Decision → Rationale →
Consequences) + treats method-selection как first-class via C.11.

**Triggered nature (НЕ scheduled):**

| Triggered type | Example (Jetix) |
|---|---|
| Сигнал рынка | 3+ запроса на новый тип услуги |
| Alpha failure | `Client.Qualified` → `Closed-Lost` персистентно |
| Method exhaustion | Pipeline conversion ниже threshold |
| Irreversible decision | Найм первого human-исполнителя |
| System boundary change | EU AI Act новый |
| New role/responsibility | Первый Enterprise sales |

**Critique scheduled "стратегирования":** Per R-B Section 4.2,
"если стратегирование поставлено на расписание без триггера — это
не стратегирование, это performance ritual." Реальная неопределённость
не появляется по расписанию.

**Three operational modes:**

| Mode | Description | AI capability |
|---|---|---|
| **1:1** | Метод полностью известен, без изменений | Полная автоматизация |
| **Adapt** | Известный метод адаптируется | AI с oversight founder'а |
| **Invent** | Метод неизвестен, требует изобретения | Только человек (founder) |

**"AI-агенты не стратегируют" принцип** (Левенчук, ailev/1795494):

> «Узкое место сейчас не в том, чтобы сделать ещё одного умного
> AI-агента [...] а в том, чтобы дать людям и агентам общий режим
> работы со смыслами»

Three причины:
1. **Нет identity и commitment.** Agent не несёт долгосрочной
   ответственности за strategic выбор.
2. **Нет долгосрочной памяти.** Agent имеет только context window
   текущей сессии.
3. **Нет "шкуры на кону".** Taleb: необратимые решения требуют
   personal stake.

**AI as support (not strategizing itself):**

| Function | AI can | AI cannot |
|---|---|---|
| Сбор SoTA по методам | ✅ | — |
| Генерация вариантов | ✅ | — |
| Critical critique | ✅ | — |
| **Выбор метода** | ❌ | Это задача founder'а |
| **Acceptance решения** | ❌ | Это задача founder'а |

**Required artifact components:** Trigger (event, не расписание),
≥2 alternatives + status quo, kill conditions, review checkpoint.

### 3.6 МЫШЛЕНИЕ ПИСЬМОМ (Writing-as-Thinking)

**Definition (Левенчук, "Системное мышление 2024", т. 1):**

> «Системное мышление происходит путём мышления моделированием...
> и письмом (с текстами на естественных языках, но с отслеживанием
> типов объектов и видов отношений объектов в этих текстах), поэтому
> внимание не только наводится на важные предметы, но и удерживается
> на них всё время проекта: записанное не так легко забыть в суете»

**Definition synthesis:** Когнитивный процесс, в котором письменный
текст на естественном языке является **орудием мышления** (не
продуктом). Ключевое требование — отслеживание типов объектов и
видов отношений в тексте (онтологизация).

**FPF-Spec correlation ✅:** Implicit throughout FPF — entire
specification is itself an artifact of writing-as-thinking. Pattern
E.14 (Human-Centric Working-Model), E.17 (Multi-View Publication Kit),
F.17 (Unified Term Sheet UTS). Preface explicit: "Thinking Through
Writing: The FPF Discipline of Conceptual Work."

**Мышление письмом ≠:**

| Концепт | Critical отличие |
|---|---|
| Documentation generation | Doc-gen — фиксация completed thoughts; мышление-письмом — generation thoughts during writing |
| Confluence pages | Confluence — knowledge storage; мышление-письмом — cognitive process |
| Note-taking | Заметки пассивны; мышление-письмом active transformation |
| Stenography | Точная фиксация past; мышление-письмом — generation new understanding |
| Prompted AI output | AI — model output на data; мышление-письмом — externalization concrete agent's cognition |

**Epistemological grounding:**

- **Peter Naur "Programming as Theory Building" (1985):** "The proper,
  primary aim of programming is, not to produce programs, but to
  have the programmers build theories." Для Jetix: AI-агент несёт
  theory в context — when session ends, theory dies. Письменное
  мышление externalizes theory, makes transferable.
- **Clark & Chalmers "Extended Mind" (1998):** Когнитивные процессы
  могут быть offloaded на external artifacts. Repository c
  `strategizing/`, `weekly/`, `letters/` — экзокортекс founder'а.

**Quality criteria:**
- ✅ Author открывает что-то нового during writing
- ✅ Текст содержит ontologically typed objects (roles, alphas, methods)
- ✅ Текст раскрывает противоречия не видимые до writing
- ❌ Fixes already known без new understanding
- ❌ Written "for audience", не для clarification

**AI + writing-as-thinking pattern:** Human writes → Agents extract
→ Agents propose:

| AI can | AI cannot |
|---|---|
| Извлекать structured data из текста | Писать primary writing rituals за founder'а |
| Critique structure стратегирования | Quarterly letter |
| Предлагать варианты для рассмотрения | Принятие стратегических решений |
| Direct questions ("Что если X неверно?") | "Онтологизировать" за человека |

**Левенчук warning (ailev/1769411):**

> «Без внешнего по отношению к LLM контуру обработки текста — никак,
> LLM всегда обманет. Если и сам текст пишет LLM — исчезает 'мышление
> письмом' как когнитивный процесс»

### 3.7 Composition diagram (как 5 связаны)

```
ГРАФ СОЗДАНИЯ
    │ задаёт контекст для
    ↓
РОЛИ ←────────── СТРАТЕГИРОВАНИЕ
    │                    │ принимает решения
    │ работают с         │ о методах
    ↓                    │
АЛЬФЫ ───────────────────┘
    │ переходы фиксируются
    ↓
МЫШЛЕНИЕ ПИСЬМОМ ──── экстернализирует все
    │
    ↓
ЭКЗОКОРТЕКС (input для агентов следующей сессии)
```

**Текстовое описание:**
- **Роли работают с альфами** как предметами метода. Без ролей —
  непонятно, кто производит transitions.
- **Граф создания определяет** какие роли необходимы на каждом уровне.
- **Стратегирование — meta-уровень** относительно ролей и альф;
  результат: выбор метода (включая roles, alphas, target state graph).
- **Мышление письмом ↔ Стратегирование:** strategy без письма —
  устное решение без артефакта (не verifiable, не transferable
  agents, быстро вытесняется).
- **Граф создания ← Стратегирование:** новые roles, новые levels
  по итогам strategy.

---

## Section 4 — 16 Trans-disciplines (Intellect Stack)

> Source attribution: R-C is primary source. ⚠ NOTE: count is **16**,
> not 17. "17" was 2021 version in *Образование для образованных 2021*;
> 2023 rewrite в *Интеллект-стек 2023* reorganized to 16. ШСМ marketing
> sometimes still uses "17" label for historical reasons. R-C confirms
> via system-school.ru/stack + Aisystant Docs + Intellect-Stack 2023
> ToC. ✅

### 4.1 Concept of trans-discipline

**Канонической definition (Левенчук, ailev/1705503):**

> «Дисциплины интеллект-стека называют часто трансдисциплинами, это
> 'дисциплины для рассуждения в ходе задействования прикладных
> дисциплин' (trans- — это 'находящиеся по ту сторону' от прикладных
> дисциплин).»

**Key distinctions:**

| Концепт | Relation к trans-disciplines |
|---|---|
| **Прикладная дисциплина** | Domain knowledge (lean, TRIZ, kanban). Trans-disciplines дают formal vocabulary |
| **Кругозорная дисциплина** | Survey knowledge (overview SE, management). Sit *above* trans-disciplines в applied stack |
| **Метод** | Method = pattern работы; methodology — trans-discipline studying *what kinds of methods exist* |
| **STEM** | Physics + math included specifically because their SoTA versions offer universal reasoning tools |

**Scale-freeness (безмасштабность):** Применимы к elementary particles,
организмам, organizations, galactic structures equally — reasoning
patterns не меняются с size.

### 4.2 Why "17"? Historical evolution

Per ailev.livejournal.com/1579339 + R-C Section 1.2:

1. **Pre-2019 (STEM era):** Standard STEM. No "trans-discipline" framing.
2. **2019:** Three-block ШСМ structure (6 proto-trans-disciplines).
3. **Mid-2021 (6 trans-disciplines):** онтологика + коммуникации,
   научное мышление, вычислительное мышление, системное мышление,
   праксеология, этика.
4. **August 2021 (16 levels):** "вместо 12 уровней стало 16"
   after splitting онтологика.
5. **End-2021 (17 in Образование для образованных 2021):** added
   Труд (инженерия + менеджмент + предпринимательство).
6. **2023 (16 in Интеллект-стек 2023):** Truд → Системная инженерия;
   added Математика + Физика; removed Экономика, Объяснения, Теория
   информации (last absorbed into Физика).

### 4.3 Enumeration of all 16 (bottom-to-top, 2023 canonical)

> Following ToC of *Интеллект-стек 2023* (Litres) + Aisystant Docs

**Foundation layer (фундамент) — disciplines 1-5:**

1. **Понятизация (Conceptualization, figuring-out)** — discipline of
   isolating figures from background and naming them. Bottom of stack.
   No prerequisites.

2. **Собранность (Sobrannost', Collectedness)** — holding objects
   in attention over time using exocortex. Includes мышление письмом
   как практику. Equivalent to attention mastery.

3. **Семантика (Semantics)** — linking physical/real objects with
   mathematical/abstract/mental ones, working with signs that denote
   objects. Bridge между physical world and descriptions.

4. **Математика (Mathematics)** — *Added 2023*. What kinds of mental
   (abstract/formal) objects exist, how they behave, how some constructed
   from others. Catalogue of ideal objects.

5. **Физика (Physics)** — *Added 2023*. What kinds of physical objects
   exist, how mathematical objects represent them. Includes Information
   Theory (absorbed from 2021 standalone).

**Formal reasoning layer — disciplines 6-9:**

6. **Теория понятий (Theory of Concepts)** — type system: classification,
   specialization, composition. "Машинка типов".

7. **Онтология (Ontology)** — modelling the world: what's important,
   meta-modelling levels, multi-level reasoning, constructive ontology.

8. **Алгоритмика (Algorithmics)** — efficient computation. Covers all
   universal computers: human minds, classical computers, quantum
   computers. Universal algorithms (deep learning).

9. **Логика (Logic)** — modes of computation-as-reasoning that yield
   error-free results: inference, functional evaluation, probabilistic.
   Includes cognitive biases.

**Knowledge-building layer — disciplines 10-11:**

10. **Рациональность (Rationality)** — *Restructured 2023*. Creating
    correct explanations (causes, effects). Rationality = explanations
    + decision-making + actions. Absorbed Объяснения slot from 2021.

11. **Познание/Исследования (Cognition/Research)** — *Merged with
    Объяснения 2023*. Popperian critical rationalism applied как
    practice: conjectures + refutations.

**Coordination/communication layer — disciplines 12-14:**

12. **Эстетика (Aesthetics)** — beauty/elegance criteria for results
    of thinking. Style as multilevel patterning. Applies to AI agents.

13. **Этика (Ethics)** — what goals acceptable, what means acceptable.
    Includes systemic ethics (multi-level conflicts) and AI ethics.

14. **Риторика (Rhetoric)** — persuading agents to take actions.
    Constrained by Этика. **Includes prompt engineering** для LLMs.

**Action/engineering layer — disciplines 15-16:**

15. **Методология (Methodology)** — scale-free teaching about agents'
    activities aimed at changing the world. Primary object: метод
    работы. **Home of роль, альфа, граф создания, стратегирование.**

16. **Системная инженерия (Systems Engineering)** — *2023 apex
    trans-discipline*. Normatively prescribes how activities for
    creating systems should be structured. Specializations: системный
    менеджмент, образовательная инженерия, медицина и т.д.

### 4.4 Hierarchical structure + dependency graph

**Foundation → Middle → Application zones:**

```
Application: Методология, Системная инженерия      [15-16]
Coordination/Norms: Эстетика, Этика, Риторика      [12-14]
Knowledge-building: Рациональность, Исследования   [10-11]
Formal reasoning: Теория понятий, Онтология,       [6-9]
                  Алгоритмика, Логика
Foundation: Понятизация, Собранность, Семантика,   [1-5]
            Математика, Физика
```

**Dependency matrix (simplified per R-C Section 3.2):**

| Discipline | Directly depends on |
|---|---|
| Понятизация | — (base) |
| Собранность | Понятизация |
| Семантика | Собранность |
| Математика | Семантика |
| Физика | Математика, Семантика |
| Теория понятий | Математика, Физика |
| Онтология | Теория понятий, Физика, Математика |
| Алгоритмика | Онтология, Физика |
| Логика | Алгоритмика, Онтология |
| Рациональность | Логика, Математика, Физика |
| Познание/Исследования | Рациональность, Логика |
| Эстетика | Исследования, Онтология |
| Этика | Эстетика, Исследования |
| Риторика | Этика, Исследования, Логика |
| Методология | Риторика + all lower |
| Системная инженерия | Методология + all lower |

⚠ Note (Левенчук, ailev/1579339): "true structure is a graph (lattice),
not a sequence." Linearization — pedagogical convenience.

### 4.5 Relation к 5 primitives

Per R-C Section 4: 5 primitives **NOT a published "canonical list"** в
Левенчук sources. Each — first-class concept в specific trans-disciplines.

| Trans-discipline | Primary home of concept |
|---|---|
| **Методология** | ★★★ Роль, Альфа, Граф создания, Стратегирование |
| **Собранность** | ★★★ Мышление письмом (как practice экзокортекса) |
| **Системная инженерия** | Normative role system + canonical alphas |

Other 13 trans-disciplines provide foundational support:
- Понятизация → ability to notice role-objects, alphas
- Семантика → grounding terms к actual objects
- Онтология → modelling роль/альфа в method's ontology
- Логика → reasoning о role compatibility, alpha state validity
- Эстетика → elegant decomposition of роль/альфа

### 4.6 Relation к FPF-Spec Parts A-K

⚠ R-C Section critical note: FPF-Spec **does not mention** intellect-stack
explicitly. FPF Part C (Kernel Extension Specifications) concerns
bounded-context reasoning tools (logics, characterisation families),
не educational intellect-stack taxonomy.

**However FPF-Spec Preface includes "Intellect Stack" section (informative):**

| FPF Layer | Question | Patterns |
|---|---|---|
| 1 — Structure & Reality | What exists and how is it bounded? | Kind-CAL, Sys-CAL |
| 2 — Knowledge & Reasoning | Why should we trust this claim? | KD-CAL (F-G-R), Arg-LOG |
| 3 — Action & Execution | How do we turn intent into change? | Agent-CHR, Method-CAL, Resrc-CAL |
| 4 — Strategy & Rationality | Which option wins under uncertainty? | Decsn-CAL |
| 5 — Governance & Purpose | Why act at all; what is permissible? | Norm-CAL |

⚠ FPF Preface stack is **5 layers, not 16 disciplines.** It's a
pedagogical projection of FPF patterns onto skills-layered map. Per
FPF-Spec line 730: "A full description of the Intellect Stack and its
layers resides in the Pedagogical Companion." FPF-Spec itself focuses
on pattern language, not on full intellect-stack curriculum.

**For Jetix:** ШСМ 16 trans-disciplines = curriculum/competency frame;
FPF 5-layer stack = patterns map. **Different abstractions для разных
audiences**, не contradictory.

---

## Section 5 — FPF-Spec Architecture ⭐ CRITICAL

> Source attribution: FPF-Spec.md primary, R-A/R-D contextualizing.
> All pattern IDs verified против actual FPF-Spec.md line numbers
> via Glob/Grep. ✅

### 5.1 FPF at a glance

**What FPF solves (per Readme.md):**

> FPF helps when the bottleneck is no longer raw ideation, but
> coordination.

It turns vague multi-actor problem into:
- a bounded-context map and stable shared vocabulary;
- explicit decision criteria, route guards, comparison characteristics;
- portfolio of lawful alternatives;
- evidence/test gap list, gates, auditable hand-offs;
- durable working forms (UTS, DRR, route-specific output forms);
- aligned outputs для engineers, managers, researchers, auditors.

**Use FPF when:** Work split across specialists/AI agents; real-world
oracle slow/expensive/noisy/risky; different audiences need different
views of same work; vocabulary breaking down; SoTA work needed as
managed portfolio (not leaderboard snapshot).

**Don't start FPF when:** One person/team can solve end-to-end;
vocabulary stable; feedback fast/cheap; semantic drift cost low;
quick answer over durable artefacts.

### 5.2 Six entry routes (per Readme.md)

⚠ Important: Old default `A.0 → A.1-A.3 → B.3 → F.17 → E.9` chain
is **NOT universal default anymore.**

1. **Project alignment** — `A.1.1 → A.15 → A.15.2/A.15.3 → B.5.1 →
   F.11 → F.9 → F.17 (UTS)`. Use when team mixing responsibilities,
   method, plans, actuality.

2. **Partly-said / language-state discovery** — `C.2.2a → C.2.LS/
   C.2.4-C.2.7 → A.16/A.16.1/A.16.2 → B.4.1 → B.5.2.0 → endpoint
   owner`. Use when serious cue too important to ignore but too
   early to settle.

3. **Boundary unpacking** — `A.6 → A.6.B → A.6.C` (+ A.6.P, A.6.Q,
   A.6.A). Use when contract/SLA mixing rules, gates, duties, evidence.

4. **Lawful comparison/selection** — `A.19:0 → A.17-A.19 → G.0 →
   A.19.CPM → A.19.SelectorMechanism → G.5`. Use when compare
   alternatives honestly.

5. **Generator / SoTA / portfolio kit** — `A.0 → G.0 → G.1 → G.2 →
   G.5 → B.5.2.1 + C.17-C.19`. Use when building reusable
   search/harvest/portfolio scaffold.

6. **Same-entity rewrite/comparison** — `A.6.3.CR → A.6.3.RT →
   E.17.EFP → E.17.ID.CR → E.17.AUD.LHR/E.17.AUD.OOTD`. Use when
   restating, explaining, repairing, comparing without changing
   what it's about.

### 5.3 Three modes of use

1. **Human-only.** FPF as reading/writing/review discipline без AI.
2. **Mixed team.** FPF as coordination layer across humans + AI agents.
3. **AI assistant.** FPF as attached file or indexed reference for
   assistant.

Per Readme.md: "FPF will not think instead of you."

### 5.4 Difference from project methodology

> "FPF is **not**: a shrink-wrapped project methodology; a quick-answer
> cheat sheet; a demand to read the whole specification linearly before
> doing useful work."

Per Preface: "FPF is closer to architecture for reasoning: a set of
reusable patterns and working forms that help teams turn tacit
thinking into shared, reviewable work."

### 5.5 Parts A-K overview

> Verified via line ranges from Grep on FPF-Spec.md ✅

#### Part A — Kernel Architecture Cluster (lines 767-25,578)

The immutable ontological core. Sub-clusters:

- **Cluster A.I — Foundational Ontology** (A.0 - A.2.9)
  - A.0: NQD onboarding glossary
  - A.1: Holonic Foundation (Entity → Holon → {System, Episteme})
  - A.1.1: U.BoundedContext (semantic frame)
  - A.2: Role Taxonomy (+ A.2.1-A.2.9)

- **Cluster A.II — Transformation Engine** (A.3 - A.3.3)
  - A.3: Transformer Quartet (System-in-Role, MethodDescription, Method, Work)

- **Cluster A.III — Time & Evolution** (A.4)
  - Temporal Duality & Open-Ended Evolution Principle

- **Cluster A.IV — Kernel Modularity** (A.5)
  - Open-Ended Kernel & Extension Layering

- **Cluster A.IV.A — Signature Stack & Boundary Discipline** (A.6.*)
  - Massive sub-cluster: A.6, A.6.B (Boundary Norm Square), A.6.C
    (Contract Unpacking), A.6.0 (U.Signature), A.6.1 (U.Mechanism),
    A.6.2-A.6.4 (epistemic morphisms), A.6.3.CR/RT (retextualization),
    A.6.P (Relational Precision Restoration), A.6.Q (Quality Term),
    A.6.A (Action Invitation), A.6.5-A.6.9 (slot/base/service/
    cross-context disciplines), A.6.S (Signature Engineering Pair),
    A.6.H (Wholeness Language Unpacking)

- **Cluster A.V — Constitutional Principles** (A.7 - A.13)
  - A.7: Strict Distinction (Clarity Lattice)
  - A.8: Universal Core (C-1)
  - A.9: Cross-Scale Consistency (C-3)
  - A.10: Evidence Graph Referring (C-4)
  - A.11: Ontological Parsimony (C-5)
  - A.12: External Transformer & Reflexive Split (C-2)
  - A.13: Agential Role & Agency Spectrum

- **Cluster A.VI — Mereology** (A.14)
  - Advanced Mereology: ComponentOf, ConstituentOf, PortionOf, PhaseOf

- **Cluster A.VII — Role-Method-Work** (A.15.*)
  - A.15: Role-Method-Work Alignment
  - A.15.1: U.Work (record of occurrence)
  - A.15.2: U.WorkPlan (schedule of intent)
  - A.15.3: SlotFillingsPlanItem

- **Cluster A.VIII — Language-State** (A.16.*)
  - Transduction Coordination, PreArticulationCuePack, etc.

- **Cluster A.IX — Characteristics & Spaces** (A.17 - A.21)
  - A.17 CHR-NORM, A.18 CSLC-KERNEL, A.19 CharacteristicSpace
  - A.19 sub-patterns: SURF-SPACE, SUPPORT-VIEW, CN-frame, CHR,
    UNM/UINDM/USCM/ULSAM/CPM/SelectorMechanism mechanisms
  - A.20 Flow.ConstraintValidity (Eulerian)
  - A.21 GateProfilization

#### Part B — Trans-disciplinary Reasoning Cluster (lines 25,579-30,377)

Logic of composition and trust.

- **B.1 Universal Algebra of Aggregation (Γ)** + B.1.1-B.1.6
  (Sys/Epist/Ctx/Time/Method/Work flavours)
- **B.2 Meta-Holon Transition (MHT)** + B.2.1-B.2.5 (BOSC triggers,
  MST, MET, MFT, Supervisor-Subholon)
- **B.3 Trust & Assurance Calculus (F-G-R с Congruence)** + B.3.1-B.3.5
  (CT2R-LOG)
- **B.4 Canonical Evolution Loop** (Observe → Notice → Stabilize → Route)
- **B.5 Canonical Reasoning Cycle** + B.5.1 (Explore → Shape → Evidence
  → Operate), B.5.2 (Abductive Loop), B.5.2.0 (U.AbductivePrompt),
  B.5.2.1 (Creative Abduction with NQD), B.5.3 (Role-Projection Bridge)

#### Part C — Kernel Extension Specifications (lines 30,378-39,963)

Pluggable domain-specific calculi (CALs), logics (LOGs), characterisation
families (CHRs).

- **C.1 Sys-CAL** (physical systems, conservation laws)
- **C.2 KD-CAL** + C.2.1 U.Episteme (slot graph), C.2.2 (Reliability R),
  C.2.2a (LanguageStateSpace), C.2.3 (Formality F), C.2.LS-C.2.7
  (language-state facets)
- **C.3 Kind-CAL** + C.3.1-C.3.A (Kind, KindSignature, KindBridge,
  RoleMask, KindAT, Typed Guards)
- **C.4 Method-CAL**, **C.5 Resrc-CAL**, **C.6 LOG-CAL**, **C.7 CHR-CAL**
- **C.9 Agency-CHR**, **C.10 Norm-CAL**, **C.11 Decsn-CAL** (Decision Theory)
- **C.12 ADR-Kind-CAL**, **C.13 Compose-CAL** (Constructional Mereology)
- **C.14-C.15 M-Sys-CAL / M-KD-CAL** (system-of-systems)
- **C.16 MM-CHR** (Measurement & Metrics)
- **C.17 Creativity-CHR**, **C.18 NQD-CAL** (Open-Ended Search Calculus),
  C.18.1 SLL (Scaling Law Lens), **C.19 E/E-LOG** (Explore-Exploit
  Governor), C.19.1 BLP (Bitter-Lesson Preference)
- **C.20-C.21 Discipline-CAL/CHR**
- **C.22 Problem-CHR** (TaskSignature), C.22.1 task-family adaptation
- **C.23 Method-SoS-LOG** (MethodFamily Evidence)
- **C.24 Agentic Tool-Use**, **C.25 Q-Bundle** (-ilities)

#### Part D — Multi-scale Ethics & Conflict Optimisation (lines 39,964-40,087)

Mostly **stub status** (D.1-D.4) with one Stable (D.5).

- D.1 Axiological Neutrality (stub)
- D.2 Multi-Scale Ethics + D.2.1-D.2.4 (stubs)
- D.3 Holonic Conflict Topology + D.3.1, D.3.2 (stubs)
- D.4 Trust-Aware Mediation + D.4.1, D.4.2 (stubs)
- **D.5 Bias-Audit & Ethical Assurance** (Stable) + D.5.1, D.5.2 (stubs)

⚠ For Jetix: Part D mostly aspirational; D.5 only operational.

#### Part E — FPF Constitution & Authoring Guides (lines 40,088-48,659)

Governance of the framework itself.

- **E.1 Vision & Mission** ("Operating System for Thought")
- **E.2 Eleven Pillars** (P-1 to P-11)
- **E.3 Principle Taxonomy & Precedence Model** (Gov ≫ Arch ≫ Epist ≫
  Prag ≫ Did)
- **E.4 FPF Artefact Architecture**
- **E.5 Four Guard-Rails** (E.5.1 DevOps Lexical Firewall, E.5.2
  Notational Independence, E.5.3 Unidirectional Dependency, E.5.4
  Cross-Disciplinary Bias Audit)
- **E.6-E.8** Didactic architecture, Archetypal Grounding, Authoring
  Conventions
- **E.9 DRR Method** (Design-Rationale Record)
- **E.10 LEX-BUNDLE** + E.10.P (Conceptual Prefixes), E.10.D1 (Context),
  E.10.D2 (I/D/S Discipline)
- **E.12-E.16** (Didactic Primacy, Pragmatic Utility, Human-Centric
  Working-Model, Lexical Authoring, RoC-Autonomy Budget)
- **E.17.0-E.17.AUD.OOTD** Multi-View Publication Kit (massive)
- **E.18 Transduction Graph Architecture (E.TGA)**
- **E.19 Pattern Quality Gates**
- **E.20 Mechanism Introduction Protocol (MIP)**

#### Part F — Unification Suite (U-Suite) (lines 48,660-55,678)

Techniques for aligning vocabularies across disciplines and AI agents.

- F.0.1 Contextual Lexicon Principles
- F.1-F.3 (Domain-Family Survey, Term Harvesting, Sense Clustering)
- F.4 Role Description (RCS + RoleStateGraph + Checklists)
- F.5 Naming Discipline
- F.6 Role Assignment & Enactment Cycle (Six-Step)
- F.7 Concept-Set Table
- F.8 Mint or Reuse decision
- F.9 Alignment & Bridge across Contexts + F.9.1 Bridge Stance Overlay
- F.10 Status Families Mapping
- F.11 Method Quartet Harmonisation
- F.12 Service Acceptance-Work Evidence Link
- F.13 Lexical Continuity & Deprecation
- F.14 Anti-Explosion Control
- F.15 SCR/RSCR Harness for Unification
- F.16 Worked-Example Template
- **F.17 Unified Term Sheet (UTS)** ← critical
- F.18 Local-First Unification Naming Protocol

#### Part G — Discipline SoTA Patterns Kit (lines 55,679-62,109)

Tools for harvesting state-of-the-art и building governed portfolios.

- G.Core Part G Core Invariants
- G.0 Frame Standard and Comparability Governance (CG-Spec)
- G.1 CG-Frame-Ready Generator
- G.2 SoTA Harvester & Synthesis
- G.3 CHR Authoring (Characteristics, Scales, Levels, Coordinates)
- G.4 CAL Authoring (Operators, Acceptance Clauses, Evidence Wiring)
- G.5 Multi-Method Dispatcher & MethodFamily Registry
- G.6 Evidence Graph & Provenance Ledger
- G.7 Cross-Tradition Bridge Calibration Kit
- G.8 SoS-LOG Bundles & Maturity Ladders
- G.9 Parity / Benchmark Harness
- G.10 SoTA Pack Shipping
- G.11 Telemetry-Driven Refresh & Decay Orchestrator
- G.12 DHC Dashboards (Discipline-Health time-series)
- G.13 External Interop Hooks

#### Parts H-K — Glossary, Annexes, Navigation

⚠ Note based on Grep: Only J.4 (line 62,110) appears as actual section
header. **Parts H, I, K are referenced в TOC but appear to be sparse
in the version vendored 2026-04-20.** Per Readme.md these are "glossary,
extended tutorials, indexes, migration notes, and other navigation
support around the core clusters." Treat as navigation aids, not
core content.

### 5.6 Key FPF concepts — deep definitions

#### 5.6.1 U.Holon (A.1) ⭐

> Pattern A.1 verified at line 1017 ✅

**Three-tier root ontology:**
- **U.Entity** — primitive of distinction (anything individuated/referenced;
  no structural assumptions)
- **U.Holon ⊑ U.Entity** — unit of composition (whole-and-part
  simultaneously)
- **U.System ⊑ U.Holon** — operational, physical (Sys-CAL)
- **U.Episteme ⊑ U.Holon** — knowledge holon (KD-CAL)

**Well-formedness:**
- WF-A1-1: Holon has exactly one U.Boundary
- WF-A1-2: Γ defined ONLY on sets of U.Holon
- WF-A1-3: Γ-application scoped to context + temporal scope

**U.Boundary kinds:**
- Open (matter + energy + info)
- Closed (energy + info, no matter)
- Permeable (filtered subset)

**Inside/Outside test (3 steps):**
1. Dependency: removing E breaks core invariant of H?
2. Interaction: E participates causal loops within H's boundary?
3. Emergence: E contributes к novel collective property?

Fail all → outside.

**Critical: agency rule.** Behavioral roles (including TransformerRole)
attach **only к U.System** (bearer). U.Episteme is **passive** content.
Any change to episteme = external system acting across boundary.

#### 5.6.2 Advanced Mereology (A.14) ⭐

> Pattern A.14 verified at line 17,478 ✅

**Two new sub-relations of partOf:**

- **PortionOf** — metrical, measure-preserving parthood of stuffs
  (governed by extensive measure μ; conservation Σ-laws)
  - Examples: "5 kg from 20 kg billet", "Pages 1-10 of report"

- **PhaseOf** — temporal parthood of *same* carrier across interval
  - Examples: "PumpUnit#3 before calibration", "Spec v2"

**Plus existing:**
- **ComponentOf** — structural discrete parts
- **ConstituentOf** — conceptual logical parts (sections, lemmas, clauses)
- **MemberOf** — collection membership (NOT partOf!)

**Decision table:**

| Want to say... | Use | Why |
|---|---|---|
| Piece of same stuff (less amount) | PortionOf | μ-additive |
| Discrete part inside whole | ComponentOf | Structural |
| Logical part в conceptual whole | ConstituentOf | Sections, lemmas |
| Same thing during sub-interval | PhaseOf | Temporal slicing |
| Item belongs to collection | MemberOf | Set, не parthood |
| System plays role/position | playsRole (A.15) | Roles are masks |

**Firewall reminder:** Если sentence about "who does what / how /
when" — A.15. Если carrier episteme structure (pages/sections) — A.14.

**MHT escalation (CC-PHA-5):** Если identity criteria break during
change → declare Meta-Holon Transition (B.2), not PhaseOf.

#### 5.6.3 U.System + U.Episteme (A.6, C.2)

- **U.System (Sys-CAL):** physical, operational holon obeying conservation
- **U.Episteme (KD-CAL):** knowledge holon — theories, models,
  specifications, standards, algorithms, proofs — defeasible/deductive
  about something + held to account by justification

**U.EpistemeSlotGraph (C.2.1)** — internal ontology of epistemes:
- DescribedEntitySlot
- GroundingHolonSlot
- ClaimGraphSlot
- ViewpointSlot
- ViewSlot
- ReferenceSchemeSlot

⚠ Critical: replaces legacy "semantic triangle" (Concept/Object/Symbol)
which had structural blind spots.

#### 5.6.4 DRR (Design-Rationale Record) — E.9 ⭐

> Pattern E.9 verified at line 41,506 ✅

**Four conceptual components:**

| Component | Question | Content |
|---|---|---|
| **Problem frame** | Why are we talking about this? | Problem statement, triggering insight |
| **Decision** | What will we do? | Precise normative text |
| **Rationale** | Why is this right? | Alternatives, Pillar check, taxonomy lens |
| **Consequences** | What happens next? | Benefits, trade-offs, impacts, risks |

**Guard:** DRR lives **outside** normative Core. Upon acceptance
*Decision* applied to relevant pattern(s) as explicit normative text.

**Δ-classes:**
- Δ-0/Δ-1 (typos, didactic clarity) → lightweight DRR (Context + Decision)
- Δ-2/Δ-3 (semantic change) → full DRR с all 4 components

#### 5.6.5 UTS (Unified Term Sheet) — F.17 ⭐

> Pattern F.17 verified at line 54,586 ✅

> "One table that a careful mind can hold."

**Core idea:** UTS = Concept-Set table с names. Each row = one
Concept-Set unified into one FPF U.Type. Each column family shows
how concept appears в chosen contexts.

**Two layouts:**
- **Layout A (Kernel-first):** rows keyed by FPF U.Type; Bounded-Context
  Columns (BCC)
- **Layout B (Base-concept):** rows keyed by Base concept (EN/RU);
  Discipline Columns (DC)

**Required row fields:**
- # / Block
- FPF U.Type
- Unified Tech name
- Unified Plain name
- (optional) Plain-Twin Governance (PTG) + Twin-Map Id
- FPF Description (one-line gist)
- SenseCells (by context)
- Bridges (CL/Loss)
- Unification Rationale
- (optional) Notes

**Constraint:** SenseCells MUST cite ≥3 distinct Contexts overall
across sheet (per A.8 Heterogeneity).

#### 5.6.6 U.BoundedContext (A.1.1) ⭐

> Pattern A.1.1 verified at line 1,202 ✅

**Plain-English:** "Make meaning local; make translation explicit."

Large systems break down when meaning treated as globally uniform.
Same label ("role", "service", "ticket", "evidence") routinely
carries incompatible senses across teams, disciplines, standards
editions, eras.

**FPF answers:** "In which semantic frame does this term, rule, or
role-claim hold?"

Bounded contexts → islands of closure inside open world. Cross-context
reuse is **never obvious**; needs explicit Bridge (F.9) с CL
(Congruence Level) and Loss notes.

#### 5.6.7 Gamma (Γ) operator — B.1 ⭐

Universal aggregation operator. Defined ONLY on sets of U.Holon.
Six flavours (per B.1.1-B.1.6):

| Flavour | Domain |
|---|---|
| **Γ_sys** | System-specific (mass, energy, resources) |
| **Γ_epist** | Knowledge-specific (provenance, trust) |
| **Γ_ctx** | Contextual (order matters) |
| **Γ_time** | Temporal (time-series, order-sensitive) |
| **Γ_method** | Order-sensitive method composition |
| **Γ_work** | Work as spent resource |

**Invariants preserved:**
- WLNK (weakest-link)
- MONO (monotonicity)
- IDEM (idempotence)
- COMM (commutativity, except Γ_ctx/Γ_time)
- LOC (locality)

#### 5.6.8 Meta-Holon Transition (MHT) — B.2 ⭐

> Pattern B.2 verified at line 27,444 ✅

**Plain-English:** When composition yields **new, coherent whole**
с own boundary, objective, capabilities that **cannot be faithfully
treated as just parts folded together** → declare MHT.

**BOSC-A-T-X triggers:**
- **B** — Boundary closure/opening
- **O** — Objective emergence/reframe
- **S** — Structural re-organization для supervision
- **C** — Capability super-additivity (beyond WLNK)
- **A** — Agency threshold crossing (A.13)
- **T** — Temporal consolidation
- **X** — Context rebase (bounded context)

**Rule of thumb:** BOSC = what holon is; A/T/X = how/where it lives.
Any **two together** almost always warrant MHT.

**Event taxonomy:**
1. Fusion
2. Fission
3. Phase Promotion
4. Role-Lift
5. Context Reframe

**Identity stance ecumenical:** 4D (world-tube, MHT = new tube)
OR 3D+1 (enduring entity, MHT = creation event). FPF doesn't force
metaphysical choice; requires **clear declarations**.

#### 5.6.9 F-G-R Trust Calculus (B.3, C.2) ⭐

**Three components:**
- **F (Formality)** — F0-F9 scale, rigor of episteme (informal sketch
  → formal proof)
- **G (ClaimScope)** — set-valued scope where claim applies (USM-based)
- **R (Reliability)** — evidence-bound warrant, weakest-link
  composition, pathwise justification

**Bridge-only reuse + CL (Congruence Level) penalties.** Cross-context
claim reuse propagates loss notes.

#### 5.6.10 NQD-CAL + E/E-LOG (C.18, C.19) ⭐

**NQD = Novelty + Quality + Diversity.** Open-ended search calculus
для creative work без illegal scalarization.

**Operations:**
- Γ_nqd.generate
- Γ_nqd.updateArchive
- Γ_nqd.illuminate
- Γ_nqd.selectFront

**Front vs Archive:** Front = current best non-dominated; Archive =
exploration history (диverity для creative search).

**E/E-LOG (Explore-Exploit Governor) actions:**
- Widen
- Keep frontier
- Narrow to subset
- Sunset line
- Reroute

**BLP (Bitter-Lesson Preference, C.19.1):** Prefer general/scalable
methods over hand-tuned heuristics when safety/legality constant.

### 5.7 FPF unique commitments — 9 "big storylines"

> Verified directly from FPF-Spec.md preface (lines 642-651) ✅

1. **Holonic kernel с physical anchoring** — everything composing is
   U.Holon; every change enacted by **external transformer** (A.1, A.12).

2. **Role-Method-Work split с time duality** — prevents endemic
   plan/reality conflation; only U.Work carries actuals (A.4, A.15.1-2).

3. **Assurance as first-class calculus** — evidence roles, decay,
   weakest-link composition make "trust" computable + auditable
   (B.3, A.10).

4. **Algebra of aggregation (Γ) с cross-scale invariants** — conservative
   composition generalizing from pumps to proofs (B.1).

5. **Local meaning, global alignment** — U.BoundedContext islands +
   explicit Bridges с congruence-loss turn "it depends" into a
   Standard (A.1.1, F.9).

6. **Publication Standard + guard-rails** — Core ↔ Tooling ↔ Pedagogy
   split, notational independence, Lexical Discipline prevent
   conceptual drift (E.5, E.10).

7. **Open-ended evolution by design** — evolve solutions AND problem
   frames; work на holons-of-interest AND across diversity of
   environments.

8. **Creativity с Novelty + Quality Diversity optimisation** — DRR,
   evidence refresh, **explicit creative search (NQD + E/E-LOG)** keep
   system alive без ossification (A.4, B.4, C.18, C.19, E.6, E.9, B.3.4).

9. **Semantic precision of boundary statements** — five moves (lexical
   → ontological → mathematical → adjusted ontological → adjusted
   lexical) для unpacking precision of statements "on the boundary"
   с multiple viewpoints (cluster A.6, особенно A.6.P + specializations).

**What FPF is:** *A generative, testable architecture for open-ended
evolutionary thinking that any domain can inhabit.*

**What FPF is not:** *A repository of domain facts, rule-chaining
engine, methodology du jour, или notation.*

### 5.8 Eleven Pillars (E.2) — FPF constitution

> Pattern E.2 verified at line 40,148 ✅

| ID | Pillar | Essence |
|---|---|---|
| **P-1** | Cognitive Elegance | Highlight decisive structure, eliminate ornamental formalism |
| **P-2** | Didactic Primacy | Human comprehension outranks theoretical purity |
| **P-3** | Scalable Formality | Single artefact matures step-by-step from informal guess to formally assured |
| **P-4** | Open-Ended Kernel | Kernel contains only meta-concepts; domain knowledge in patterns |
| **P-5** | FPF Layering | Patterns are modular declarative extensions |
| **P-6** | Lexical Stratification | Every core concept expressible in 4 registers (plain, technical, U.Type, math) |
| **P-7** | Pragmatic Utility | Falsification rewarded over confirmation |
| **P-8** | Cross-Scale Consistency | Composition algebras invariant across material/knowledge/methods |
| **P-9** | State Explicitness | Every artefact declares state (design-time, run-time) |
| **P-10** | Open-Ended Evolution | Every entity expected to evolve indefinitely |
| **P-11** | State-of-the-Art Alignment | Kernel + extensions track contemporary knowledge |

**Precedence:** Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did (E.3 Principle Taxonomy).

**Precedence stack (high → low):**
Law/Regulation → E.5 Guard-Rails → B.3 Trust & Assurance → E.3 governance
→ E/E-LOG policies → BLP → Product Policies → Implementation Tactics.

### 5.9 Four Guard-Rails (E.5)

- **GR-1 (E.5.1) DevOps Lexical Firewall** — никаких domain-specific
  tokens (yaml, docker, CI/CD) в Core patterns
- **GR-2 (E.5.2) Notational Independence** — patterns expressible в
  multiple formalisms; никакого locking в OWL/JSON-LD/category theory
- **GR-3 (E.5.3) Unidirectional Dependency** — Core → Tooling →
  Pedagogy (acyclic)
- **GR-4 (E.5.4) Cross-Disciplinary Bias Audit** — каждый pattern
  reviewed с lens diversity

### 5.10 Vision/Mission (E.1) ⭐

**Mission Statement:**

> *Enable any motivated system/actor/agent/transformer — human or AI —
> to transform a raw idea into a reproducible, auditable change in the
> physical world through incremental, falsifiable cycles.*

**Vision Statement:**

> *Reliable reasoning should be as accessible as version control:
> clone the conceptual kernel, extend it with domain patterns, and
> commit decisions that remain traceable across time, scale, and
> discipline.*

**Three core invariants** every artefact must honour:
- **Evolvability** — change expected and governed
- **Cross-Scale Coherence** — same algebra binds parts to wholes at any level
- **Didactic Transparency** — each element exposes its own reasoning path

---

## Section 6 — Essence Kernel + SEMAT legacy

> Source attribution: R-D primary; FPF-Spec preserves no direct
> "Alpha" type but inherits architectural pattern via A.15
> Role-Method-Work + A.2 RoleStateGraph. ✅

### 6.1 Essence Kernel original (SEMAT)

**Founders:** Ivar Jacobson, Bertrand Meyer, Richard Soley, September 2009.

**Manifesto:** Three pathologies in software engineering:
1. Fads driven by fashion not evidence
2. Methods designed для methodologists not practitioners
3. Standards too complex без extensive training

**OMG standardization:**
- Essence v1.0 (Nov 2014)
- Essence v1.1 (Dec 2015)
- Essence v1.2 (Jul 2018)
- Essence v2.0 Alpha draft (Feb 2024)

**Two-layer design (CRITICAL):**
- **Language** — type system для describing methods (alpha, activity
  space, competency, work product, practice)
- **Kernel** — instantiation of Language for software engineering
  (the seven alphas)

The Kernel is **example** of what Language can express, not Language itself.

**Three areas of concern (color-coded):**

| Area | Color | Focus | Alphas |
|---|---|---|---|
| Customer | Green | Why system exists | Stakeholders, Opportunity |
| Solution | Yellow | What system must be/do | Requirements, Software System |
| Endeavor | Blue | How team does work | Work, Way of Working, Team |

**Four kinds of essential elements:**
1. **Alphas** — essential things to work with
2. **Activity Spaces** — essential things to do (15 spaces)
3. **Competencies** — essential capabilities (6: Stakeholder
   Representation, Analysis, Development, Testing, Leadership,
   Management; 5 levels each)
4. **Patterns** — named bundles of synchronized alpha states

**Practice composition:** Practices compose by sharing kernel alphas;
~250 practices for software engineering, composable into thousands
of situational methods.

### 6.2 Levenchuk's adaptation путь

**2010-2013:** First major Russian exposition of Essence
(ailev/1051048 in 2012; ailev/1082662 in 2013).

**2013-2014:** INCOSE Russia × SEMAT joint project: adapt Essence
Kernel for systems engineering.

**2015 arXiv paper** ["Towards a Systems Engineering Essence"](https://arxiv.org/abs/1502.00121):
Modified Solution area replacing "Requirements / Software System" с
**"System Definition / System Embodiment"** (Определение системы /
Воплощение системы), aligned с ISO 42010.

**2014-2020 textbook period:** Replaced "Way of Working" с
**"Технология"** in Endeavor area. Seven ШСМ alphas: Возможности,
Стейкхолдеры, Определение системы, Воплощение системы, Работы,
Технология, Команда.

**2023-2024 (most recent editions):** Current ШСМ alpha set:
**воплощение системы, описание системы, метод (way of working),
работы системы**. External roles (стейкхолдеры, возможности),
team appear as sub-alphas.

### 6.3 What kept unchanged / modified / rejected / added

**Borrowed unchanged (Language):**
- Alpha construct (functional object tracking method-subject state)
- Past-participle state naming convention
- State-checklist structure (verifiable yes/no questions, AND logic)
- Alpha-state graph (non-linear OK, returns/cycles allowed)
- Work products as manifestation
- "Things to care about" framing
- Alpha containment + association

**Modified (Kernel):**
- Solution area: Requirements/Software System → System Definition/
  System Embodiment
- Endeavor area (intermediate period): Way of Working → Технология
- Stakeholders → "Внешние проектные роли" (external project roles)
  в recent editions
- Alpha definition broadened: "предмет метода" (method subject) — any
  important object whose state changes need tracking

**Added (entirely new):**
- **Граф создания (creation graph)** — three-level: super-system /
  target system / enabling system. Per Левенчук in *Методология 2025*:
  "по мотивам OMG Essence 2.0:2024" (Essence v2.0 partially adopted
  this multi-level view!)
- **Стратегирование (strategizing)** — meta-method choosing method
- **Интеллект-стек** — layered hierarchy of trans-disciplines
- **Трансдисциплины** — domain-independent thinking practices (16)
- **Мышление письмом** — explicit modeling through structured text
- **AI agents as role executors** (post-2020)

**Rejected/sidelined:**
- Activity spaces as compositional layer (effectively sidelined)
- Practice-as-composition formalism (replaced с informal table modeling)
- The software-specific kernel (explicitly rejected; Levenchuk uses
  Language only — *as the standard requires*: "for each new development
  domain one should develop one's own kernel")

### 6.4 Alpha mapping table (Essence vs ШСМ vs FPF)

| # | Original Essence | ШСМ (SE Essence 2015) | ШСМ (Textbook 2015-2020) | ШСМ (Current 2020-2024) | FPF (2026) |
|---|---|---|---|---|---|
| 1 | Stakeholders | Стейкхолдеры | Стейкхолдеры | Внешние проектные роли | (no direct) — A.2 Role |
| 2 | Opportunity | Возможности | Возможности | Возможности | (no direct) |
| 3 | Requirements | **Определение системы** | Определение системы | Описание системы | U.Episteme / U.Signature |
| 4 | Software System | **Воплощение системы** | Воплощение системы | Воплощение системы | U.System / U.Holon |
| 5 | Work | Работы | Работы | Работы системы | **U.Work** (A.15.1) |
| 6 | Way of Working | preserved | **Технология** | Метод (restored) | U.Method (A.3.1) + U.MethodDescription (A.3.2) |
| 7 | Team | Команда | Команда | Команда | (no direct) — collective via Γ |

⚠ KEY OBSERVATION: FPF-Spec **doesn't preserve "alpha" terminology
explicitly**. Alpha-as-track is dispersed into U.RoleStateGraph
(roles), U.Episteme (knowledge alphas), U.System (physical),
U.Work/WorkPlan (work alphas), PhaseOf (temporal parts). **FPF is
more fine-grained typing than Essence.**

**For Jetix:** decision needed — preserve "alpha" Russian-pedagogical
term для continuity с ШСМ, OR migrate к FPF-Spec U.Type vocabulary?

### 6.5 Activity Spaces vs Creation Graph

**Essence Activity Spaces (15):** Generic placeholders for specific
activities, organized by area of concern, connected к alphas through
Entry/Completion Criteria.

**ШСМ Creation Graph:** Three-level systems hierarchy contextualizing
project alphas spatially + causally. Each level corresponds to area
of concern:

```
Super-system   ← Customer (Stakeholders, Opportunity)
Target System  ← Solution (System Definition, System Embodiment)
Enabling System ← Endeavor (Work, Method, Team, Technology)
```

**Verdict:** Creation graph **complements** activity spaces, не
replaces. Spatial vs procedural metaphor. **For Jetix:** creation
graph is superior org framework; activity spaces can be mapped onto
it for projects requiring explicit phase gating.

### 6.6 AI agents and Essence

**Essence v1.2:** Не addresses AI agents.

**Essence v2.0 (Feb 2024 Alpha draft):** Begins formalizing relation
к AI systems but details not yet public normative form.

**Левенчук's AI angle (since ~2020):**
- **Agents as role executors:** Any intelligent agent (human, AI,
  robotic, collective) plays role в creation graph. Per *Методология
  2025*: "Создатели — это агенты, всё что из методов умеет делать
  агент — это личность агента."
- **Past-participle states as machine-readable protocol:** alpha
  checklist becomes **agent onboarding protocol**.
- **Exocortex (экзокортекс):** computational extension of agent's
  cognition (tools, AI assistants, structured note systems).
- **Moravec's paradox awareness:** AI excels at strategy advice + text
  generation; struggles с adapting method chains к unexpected
  situations.
- **Scale-free application:** AI agent managing subroutine + human
  managing civilization use **same alpha framework** at appropriate
  granularity.
- **Creation graph для AI pipelines:** super-system (business need),
  target system (AI output), enabling system (agent pipeline) — ШСМ
  alpha tracking serves as control layer for agentic AI orchestration.

### 6.7 Current FPF relationship к Essence

⚠ FPF-Spec.md does NOT cite Essence/SEMAT/Jacobson directly in any
of the patterns examined. FPF is **post-Essence** evolution where
the "alpha" idea has been generalized + dispersed into U.Holon-based
ontology с specific U.Types (RoleStateGraph, Episteme, System, Work,
WorkPlan, etc.).

**Effective relationship:** FPF inherits alpha-pattern (state machine
on a tracked subject) and applies it broadly. But the explicit
"alpha as standalone concept" is replaced by structured composition
of more atomic types (boundary, role state, episteme slot graph,
work record).

**For Jetix:** This dual heritage matters for D6 writing:
- ШСМ vocabulary (alpha, граф создания) — pedagogical entry для
  Russian-speaking audience + bridges к Essence community
- FPF U.Type vocabulary — formal precision + AI-agent compatibility
- Bridge mapping needed (per F.9 Bridges)

---

## Section 7 — Mereology + Holon Hierarchy

> Source attribution: R-E primary; FPF-Spec A.1 + A.14 verified
> directly. ✅

### 7.1 Foundational mereology

**Mereology (from Greek μερος, "part"):** Theory of part-whole relations.

**Historical lineage:**
- **Stanisław Leśniewski** *Foundations of the General Theory of Sets*
  (1916), *Foundations of Mathematics* (1927-1931). Polish nominalist
  motivation: alternative к Cantorian set theory без abstract objects.
- **Henry Leonard + Nelson Goodman** *The Calculus of Individuals*
  (1940). Modern accessible formulation.
- **Aristotle, Husserl, Leibniz** — pre-formal antecedents.

**Distinction from set theory:**
- Set theory: {A, B} is abstract, contains А, B as *members*
- Mereology: whole is **nothing over and above** parts; concrete fusion
- Tarski (1935): Models of GEM isomorphic to complete Boolean algebras
  minus zero element — algebraic character

**Major formal systems:**

| System | Additions | Character |
|---|---|---|
| M (Minimal) | Reflexivity + Transitivity + Antisymmetry | Partial ordering |
| MM | + Weak Supplementation | Proper part implies disjoint companion |
| EM | + Strong Supplementation | No two distinct wholes с same proper parts |
| GEM | + Unrestricted Composition | Classical (Leonard-Goodman) |
| CEM | = GEM | Classical Extensional Mereology |

**Three core axioms:**
- Reflexivity (P.1): ∀x Pxx
- Transitivity (P.2): (Pxy ∧ Pyz) → Pxz
- Antisymmetry (P.3): (Pxy ∧ Pyx) → x=y

**Critical supplementation:**
- **Weak Supplementation (P.4):** Proper part has companion disjoint part
- **Strong Supplementation (P.5):** Entails extensionality

**GEM Unrestricted Composition (P.15):** Any non-empty collection has
fusion. Implies "fusion of Cleopatra's nose and Eiffel Tower" exists.
Operationally irrelevant для Jetix (only intentional compositions matter).

**David Lewis's mereology** (*Parts of Classes*, 1991) — applied GEM
к set theory; defended mereological universalism (composition unrestricted,
relevance restricted). **The pragmatic stance Левенчук effectively adopts.**

**Kit Fine's hylomorphic mereology** (*Things and Their Parts*, 1999):
- Hylomorphism — form as constitutive element
- Qua-objects — object qua playing a role
- Mereological coincidence — distinct objects same location, different
  modal profiles (statue vs clay)
- "Monster Objection" against CEM: ham + cheese + bread fuse to
  ham-sandwich BEFORE assembly (since fusion exists whenever parts exist)
- Most philosophically sophisticated departure from CEM

**Constructor theory** (Deutsch + Marletto, 2012-present): Meta-theory
of physics — possible vs impossible transformations (tasks). Not
mereology per se but provides vocabulary for FPF creation graph.

### 7.2 Holon theory (Koestler + extensions)

**Arthur Koestler** *The Ghost in the Machine* (1967). Coined
"holon" from Greek *holos* (whole) + *-on* (part).

**Definition:** "Sub-wholes on any level of the hierarchy are
referred to as holons."

**Key propositions:**
- (1.2) Multi-levelled hierarchy of semi-autonomous sub-wholes
- (1.3) Parts and wholes in absolute sense don't exist
- (1.4) **Janus phenomenon** — holons face inward (parts) AND outward
  (containing whole) simultaneously
- (1.5) Applies к any stable bio/social sub-whole с rule-governed behaviour

**S-A vs INT tendencies (Proposition 4.1):**

> Every holon has dual tendency to preserve and assert its individuality
> as quasi-autonomous whole; AND to function as integrated part of
> larger whole.

- **S-A (Self-assertive)** — wholeness expression
- **INT (Integrative)** — partness expression

**Dynamic equilibrium (Prop 9.1):** Healthy organism balances S-A
and INT tendencies. Two failure modes:
- (9.4) S-A excess: holon "monopolizes functions"
- (9.5) INT excess: "power of whole erodes part autonomy" (groupthink)

**Holarchy:** Hierarchy of holons. Every node simultaneously
whole-and-part.

**Ken Wilber** (*Sex, Ecology, Spirituality*, 1995) — Four Quadrants:

| Quadrant | Label | Description |
|---|---|---|
| UL | "I" | Subjective experience, consciousness |
| UR | "It" | Physical form, observable behavior |
| LL | "We" | Shared culture, values |
| LR | "Its" | Social systems, institutions |

**Tetra-arising:** Every holon enacts all four quadrants simultaneously.

**Other extensions:**
- **Piero Mella** *The Holonic Revolution* — emphasis on functional
  emergence beyond structural
- **Erich Jantsch** *The Self-Organizing Universe* — self-organization
  through coherence thresholds
- **Maturana + Varela autopoiesis** — strong version of holonic
  self-assertion (system produces its own boundaries)

### 7.3 FPF's mereological treatment (A.1 + A.14)

**Левенчук's stance** (per ailev/1776793):

> «За основу мы берём мереологию холонов (эпистем, дисциплин, систем,
> сообществ и т.д.). Холоны отличаются конструированием их из частей
> и входимостью в другие целые как части.»

**FPF actively includes:**
1. **Holons as primitive unit** (not atoms; partonomy preferred over
   flat fusion)
2. **Role as mask (маска роли)** — roles aren't separate holons; they
   are masks holons wear in context
3. **Interface and encapsulation** — holons expose interfaces;
   internal assembly hidden behind invariant
4. **Three-level creation graph** — target / creating / supersystem
5. **Constructor theory vocabulary** — transformations, tasks,
   constructors imported (vocabulary only, не physics foundations)
6. **Advanced mereology** — multi-type parthood, hierarchical
   kind-representation (partonomy), metaholon transition

**FPF actively excludes from CEM/GEM:**
- Unrestricted composition (only intentional, lifecycle-relevant)
- Extensionality as identity condition (holons change parts без losing
  identity)
- Flat "no preferred decomposition" stance (privileges partonomy)

**FPF actively excludes from Kit Fine:**
- Qua-objects (role-as-mask sufficient)
- Mereological coincidence as general principle (single object с masks)
- Full location pluralism (multi-located objects)
- Constructor theory as physics (vocabulary only)

**FPF excludes from standard academic:**
- BFO (Basic Formal Ontology) — explicitly rejected per ailev/1451832
  as "негодная онтология для инженерных задач" (generates "a herd
  has a tail" monsters)
- Van Inwagen's organicism — would deny non-biological composites
- Pure extensionality — engineers need same system across lifecycle stages

**Левенчук's rationale (per ailev/1451832):**

> Теоретическая мереология: красивые логические формулы, никакой
> связи с жизнью.

Engineering needs: causally grounded decomposition, lifecycle-aware
parthood, multi-stakeholder view, encapsulation. None addressed by
CEM or Fine — hence "advanced" engineering mereology.

### 7.4 Organizational applications

**Holacracy (Brian Robertson):** Most explicit application of holarchy
к org governance. Nested circles (each whole + part). Roles ≠ jobs.
Double-link (rep + lead). Governance vs operational meetings separated.
Adopted by Zappos (controversial), HolacracyOne, hundreds of smaller orgs.

**Sociocracy 3.0 (S3):** Lighter pattern library, modular adoption
without full constitutional implementation.

**Teal organizations (Frédéric Laloux):** Developmental stage —
self-management, wholeness, evolutionary purpose. Not governance system,
а consciousness model.

**Beyond Budgeting (Hope + Fraser):** Rolling forecasts, relative
performance benchmarks — financial holonic decentralization.

**Bureaucratic vs Holonic vs Network structures:**

| Structure | Authority basis | Information flow | Failure mode |
|---|---|---|---|
| Bureaucratic | Position | Top-down | INT excess: rigidity |
| Holonic | Role | Bidirectional | Governance overhead |
| Network/DAO | Peer | Horizontal | S-A excess: coordination failure |

### 7.5 AI agent systems

**Multi-agent systems (MAS) literature** provides deepest academic
treatment.

**AGR model (Ferber, Gutknecht, Michel, AAMAS 2003):**
- **Agent** — individual autonomous entity
- **Group** — collection sharing context
- **Role** — abstract behavioral specification (any agent satisfying
  constraints can fill)

⚠ Mereologically: agents compose groups, groups compose orgs. Roles
are not parts but **functions/masks** parts play — exactly Левенчук's
"role as mask" formulation.

**Organization-Centered MAS (OCMAS) vs Agent-Centered MAS (ACMAS):**
- ACMAS — agents define their own relationships
- OCMAS — start с org structure, agents are interchangeable role-fillers
- **Jetix is OCMAS** — role manifests define skeleton; specific Claude
  models fill roles + replaceable

**Modern LLM agent frameworks:**

| Framework | Pattern | Mereology |
|---|---|---|
| CrewAI | Human team metaphor | Role-based hierarchy |
| LangGraph | State machine | Graph-theoretic |
| AutoGen | Conversational group | Peer agents |
| Claude Code sub-agents | Orchestrator-worker | Nested context windows |

**Anthropic's multi-agent research system** (June 2025): Orchestrator
(Claude Opus 4) spawns 3-5 subagents (Claude Sonnet 4) parallel.
Each subagent в own context window с defined objective, output format,
tool access, task boundaries.

⚠ Production cost note: Multi-agent systems use **~15x more tokens**
than chat. The INT overhead — coordinating parts. Holonic decomposition
justified ONLY when parallelization gain outweighs coordination cost.

**Critical insight для Jetix:** Role is correct unit of holonic
composition, NOT agent/person filling it.

### 7.6 Beyond Левенчук's "lightweight" — when to add depth

Per R-E Section 6, evaluation:

| Add layer | Value for Jetix | Cost | Verdict |
|---|---|---|---|
| Kit Fine's logical/physical separation | Low | Low | Extract one concept ("logical vs physical location"); skip formal apparatus |
| Constructor theory transformation vocab | High | Low | **Apply** — already imported via Левенчук |
| Constructor theory as physics | Zero | High | Skip |
| Category theory (functors, nat transformations) | Medium at 50+ agents | Very high | Defer to Phase 3 |
| Granular mereology vocabulary | Medium | Low | Extract concept ("granularity level"); skip formal apparatus |
| Van Inwagen's organicism | Negative | Medium | Acknowledge as critique, skip |

**Levenchuk's "middle path":** Use "advanced mereology" precisely
because importing more than standard part-whole thinking но less than
full philosophical apparatus. Метахолонный переход, kind-typing
(CT2R-LOG), role-as-mask formalism are genuine theoretical additions
earning place by solving specific engineering problems.

**Principle:** Import exactly as much formalism as needed to solve
specific problem informal language cannot solve. No more.

---

## Section 8 — Intersections, conflicts, convergence

> Triangulation results across primary (FPF-Spec) + secondary (R-A через R-E)

### 8.1 Where all sources agree

**Universal convergence points:**

1. **Holons as primitive unit.** A.1 + R-E + Левенчук posts —
   identical: holons (whole-and-part simultaneously) are foundation.

2. **Three-level systems hierarchy.** Граф создания (R-B/R-D) ≈
   target/creating/supersystem ≈ FPF U.System hierarchy. Все sources
   converge на 3-level mereology.

3. **Roles ≠ persons.** R-B + R-D + A.2/A.13 + R-E (AGR model) —
   universal: role is abstract, holder is concrete.

4. **Past-participle states.** OMG Essence + Левенчук + FPF
   RoleStateGraph — universal convention.

5. **Bounded contexts.** A.1.1 + R-B (мышление письмом requires
   ontologization) + Левенчук posts — all emphasize local meaning.

6. **AI-agent compatibility design.** All sources post-2020 explicitly
   accommodate AI agents.

7. **Writing-as-thinking primacy.** R-B + Левенчук *Системное
   мышление 2024* + FPF preface "Thinking Through Writing" — all
   agree on cognitive externalization.

8. **Strict separation of design vs run.** A.4 (Temporal Duality) +
   A.15 (Role-Method-Work split) + R-B (стратегирование before
   планирование) — all converge.

### 8.2 Where FPF has evolved past older ШСМ sources

⚠ **Key evolution points:**

1. **Alpha terminology dispersed.** ШСМ (R-B/R-D) treats "alpha" as
   core primitive. FPF-Spec disperses: U.RoleStateGraph (role state),
   U.Episteme (knowledge), U.System (physical), U.Work/WorkPlan (work),
   PhaseOf (temporal). **More fine-grained typing.**

2. **5 primitives → richer pattern language.** R-B's analytical "5
   primitives" framing → FPF has ~300+ patterns с explicit
   pattern IDs (A.X.Y.Z.). Conceptual core preserved, expression
   richer.

3. **17 → 16 trans-disciplines.** R-C confirms 2021 (17) → 2023 (16)
   restructure. Not in FPF-Spec at all (FPF-Spec is pattern language,
   not curriculum).

4. **Creation graph "по мотивам OMG Essence 2.0:2024".** Per R-D:
   Levenchuk credits Essence v2.0 as having "partially adopted this
   multi-level view." FPF-Spec then operationalizes via U.Holon
   composition + Γ algebra.

5. **NQD + E/E-LOG explicit (FPF), not in older ШСМ.** Per FPF-Spec
   preface: "explicit creative search (NQD + E/E-LOG)" is one of 9
   "big storylines" unique to FPF. R-B/R-D don't yet cover это depth.

6. **Boundary discipline (A.6 cluster) — new in FPF.** Massive
   sub-cluster A.6.* (Boundary Norm Square, Contract Unpacking,
   Relational Precision Restoration). Not present как explicit
   sub-discipline в older ШСМ literature.

### 8.3 Where sources conflict

⚠ **Explicit conflicts requiring resolution:**

**Conflict 1: "Alpha" as standalone term**
- R-B treats Alpha as 1st-class primitive ✅
- FPF-Spec doesn't preserve "Alpha" terminology
- **Resolution:** FPF primary. For Jetix: bridge mapping required.
  Alpha is now distributed across U.RoleStateGraph, U.Episteme,
  U.System, U.Work depending on what's tracked.

**Conflict 2: Number of trans-disciplines**
- R-C (2023+ canonical) = **16**
- ШСМ marketing/Levenchuk older posts sometimes still **17**
- Old version *Образование для образованных 2021* = 17
- **Resolution:** Use 16 (current canonical per *Интеллект-стек 2023*
  + system-school.ru/stack).

**Conflict 3: "5 primitives" status**
- R-B presents as analytical synthesis для Jetix purposes
- ⚠ Per R-C Section 4: "they do not appear as named 'canonical list
  of 5 primitives' в any single source found"
- **Resolution:** Treat "5 primitives" as **R-B's didactic frame**, не
  Левенчук's published taxonomy. Each concept is real в Levenchuk
  texts but не organized as "5 primitives" by him.

**Conflict 4: BFO / category theory inclusion**
- Some external sources view BFO + cat theory as natural fit
- Левенчук + FPF-Spec explicitly reject BFO; defer cat theory
- **Resolution:** Side с FPF/Левенчук stance per ailev/1451832.

### 8.4 Gaps — what researches missed что FPF-Spec covers

⚠ **Gap 1: Boundary discipline depth (A.6.*)**
- R-B/R-D barely touch boundary statement precision
- FPF Cluster A.6.* — substantial: Boundary Norm Square (L/A/D/E
  routing), Contract Unpacking, Relational Precision Restoration
  (RPR), Quality Term + Action Invitation specializations
- **Significance:** This is one of FPF's "9 big storylines" (#9).
  R-B/R-D don't cover; need FPF-Spec direct.

⚠ **Gap 2: Multi-View Publication Kit (E.17.*)**
- R-B/R-D don't address multi-view publication
- FPF Cluster E.17.* — substantial: U.MultiViewDescribing, ViewpointBundleLibrary,
  TEVB, MVPK, ExplanationFaithfulnessProfile, ComparativeReading,
  AuthoredUnitDiscipline
- **Significance:** Critical для serving multiple audiences (engineers,
  managers, researchers, auditors) от one underlying body of work.

⚠ **Gap 3: Transduction Graph Architecture (E.TGA = E.18)**
- Not in any secondary source
- FPF — flows of morphisms, OperationalGate, MVPK faces, SquareLaw,
  UNM single-writer, set-return selection, PathSlice/Sentinel refresh
- **Significance:** Operational backbone for FPF tooling layer.

⚠ **Gap 4: Characteristic Space + dynamics (A.17-A.21, A.19.*)**
- R-B/R-D cover альфа as state machine but не CharacteristicSpace
  formalism
- FPF — A.17 CHR-NORM, A.18 CSLC-KERNEL (Characteristic/Scale/Level/
  Coordinate), A.19 CharacteristicSpace + suite of mechanisms
  (UNM/UINDM/USCM/ULSAM/CPM/SelectorMechanism)
- **Significance:** Essential для measurement, scoring, comparison,
  selection в FPF.

⚠ **Gap 5: Constructor signature engineering (A.6.S)**
- Not in secondary
- FPF — TargetSignature + ConstructorSignature два-signature pair
  arrangement, EFEM, editioning, retargeting
- **Significance:** Engineering pattern for evolving signatures
  (substantial design tool).

⚠ **Gap 6: NQD-CAL + E/E-LOG depth (C.18, C.19)**
- R-B/R-D don't cover open-ended search calculus
- FPF — Γ_nqd operations, Pareto-only default, Bitter-Lesson Preference,
  Scaling-Law Lens, Creative Abduction integration
- **Significance:** This is "9 big storylines" #8 (creativity treatment).

### 8.5 Counter-gaps — what researches cover что FPF-Spec doesn't

✅ **Counter-gap 1: Биографический материал** (R-A)
- FPF-Spec doesn't include biographical context.
- R-A provides Левенчук's intellectual development, lineage, career
  arc, current 2026 focus.
- **Significance:** Essential для understanding the *why* of design
  choices.

✅ **Counter-gap 2: Essence/SEMAT historical context** (R-D)
- FPF-Spec doesn't cite Essence/SEMAT/Jacobson directly.
- R-D provides full SEMAT history, OMG standardization, Levenchuk's
  adaptation путь.
- **Significance:** Critical для bridging к engineering communities
  с Essence background.

✅ **Counter-gap 3: ШСМ curriculum + МИМ structure** (R-A + R-C)
- FPF-Spec doesn't address learning curriculum.
- R-A/R-C provide резидентура structure (R0→R1→R2), 16 trans-disciplines
  semester mapping, IWE personal AI guide.
- **Significance:** Important context for understanding Левенчук's
  practitioner community.

✅ **Counter-gap 4: Russian-language pedagogical conventions** (R-B)
- FPF-Spec is in English.
- R-B provides Russian terminology, examples, anti-patterns adapted
  для Russian-speaking audience (Jetix relevant).
- **Significance:** Critical для Jetix internal use (Russian primary
  language per CLAUDE.md).

✅ **Counter-gap 5: Mereology + holon philosophical depth** (R-E)
- FPF-Spec uses mereology operationally without philosophical depth.
- R-E provides Leśniewski → Lewis → Fine philosophical lineage,
  Koestler/Wilber holon theory, Holacracy/Sociocracy/Teal organizational
  applications, AGR/PROSA AI applications.
- **Significance:** Useful для intellectual grounding + organizational
  application analogies.

✅ **Counter-gap 6: Anti-pattern lists + violation-by-misuse warnings** (R-B)
- FPF-Spec mostly normative + how-to.
- R-B provides extensive "ШСМ X ≠ Y" tables + "violation by misuse"
  framework.
- **Significance:** Practical для AI-agent training (boundary
  conditions explicit).

---

## Section 9 — Terminology glossary (reference)

> Cross-source unified glossary. ✅ verified terms have primary source
> citation. ⚠ marks terms appearing in only one source.

### 9.1 ШСМ / Russian terms → English equivalents

| Russian (ШСМ) | English equivalent | Definition | Primary source |
|---|---|---|---|
| Альфа | Alpha | Предмет метода с lifecycle states | OMG Essence 1.2 + Метод 2025 ✅ |
| Граф создания | Creation Graph | 3-level mereological: target/creating/supersystem | Метод 2025 ✅ |
| Стратегирование | Strategizing | Метод выбора метода | Метод 2025 ✅ |
| Мышление письмом | Writing-as-Thinking | Externalization мышления через письмо | Сист.мышление 2024 ✅ |
| Роль | Role | Сигнатура метода × interest × мастерство | A.2 / R-B ✅ |
| Исполнитель | Executor / Holder | Concrete agent filling role | R-B |
| Создатель | Creator | Agent doing creating (per agent.everything-from-methods) | Метод 2025 |
| Целевая система | Target system | Что мы создаём для клиента | A.1 / R-B ✅ |
| Надсистема | Supersystem | Где функционирует целевая система | R-B + R-D ✅ |
| Создающая система | Creating system / Enabling system | Кто создаёт целевую | Метод 2025 ✅ |
| Способ работы / Метод | Way of Working / Method | Pattern работы | A.3.1 / R-D ✅ |
| Описание метода | Method description | Specification recipe | A.3.2 |
| Работа | Work | Record of occurrence | A.15.1 |
| Программа работ | Work plan | Schedule of intent | A.15.2 |
| Команда | Team | Group performing work | OMG Essence |
| Возможности | Opportunity | Customer-area alpha | OMG Essence |
| Стейкхолдеры | Stakeholders | Customer-area alpha | OMG Essence |
| Внешние проектные роли | External project roles | Recent ШСМ replacement для Stakeholders | R-D |
| Воплощение системы | System Embodiment / Realization | Solution-area alpha (физическая реализация) | SE Essence 2015 ✅ |
| Определение системы / Описание системы | System Definition / Description | Solution-area alpha (specification) | SE Essence 2015 ✅ |
| Технология | Technology | Endeavor-area alpha (intermediate ШСМ period) | R-D ⚠ |
| Холон | Holon | Whole-and-part entity (Koestler) | A.1 ✅ |
| Холархия | Holarchy | Hierarchy of holons | R-E |
| Партономия | Partonomy | Ordered hierarchical part-whole | ailev/1776793 ✅ |
| Холонизм / Маска роли | Holonism / Role mask | Role as mask holon wears in context | ailev/1776793 ✅ |
| Эмерджентность | Emergence | New property от composition | R-B + B.2 ✅ |
| Граф состояний | State machine / State graph | States + transitions for alpha | R-B + A.2.5 ✅ |
| Чеклист альфы | Alpha checklist | Verifiable criteria for state | R-B ✅ |
| Сигнатура метода | Method signature | Typed: subjects + roles | Метод 2025 ✅ |
| Предмет метода | Method subject / Alpha | Object метод трансформирует | Метод 2025 ✅ |
| Экзокортекс | Exocortex | External cognitive tools (LLMs, notes, repos) | Сист.мышление 2024 ✅ |
| Онтологизация | Ontologization | Typing objects + relations в тексте | R-B |
| Трансдисциплина | Trans-discipline | Discipline о disciplines (scale-free) | Интеллект-стек 2023 ✅ |
| Прикладная дисциплина | Applied discipline | Domain knowledge | R-C ✅ |
| Кругозорная дисциплина | Horizon discipline | Survey knowledge | R-C |
| Интеллект-стек | Intellect Stack | 16 trans-disciplines | Интеллект-стек 2023 ✅ |
| Понятизация | Conceptualization / Figuring-out | Discipline of isolating figures | Интеллект-стек 2023 |
| Собранность | Collectedness / Attentional mastery | Holding attention via exocortex | Интеллект-стек 2023 |
| Семантика | Semantics | Linking physical-abstract objects | Интеллект-стек 2023 |
| Математика | Mathematics | Abstract objects taxonomy | Интеллект-стек 2023 (added 2023) |
| Физика | Physics | Physical objects modeling (incl. info theory) | Интеллект-стек 2023 (added 2023) |
| Теория понятий | Theory of Concepts | Type system: classification, specialization, composition | Интеллект-стек 2023 |
| Онтология | Ontology | Multi-level meta-modeling | Интеллект-стек 2023 |
| Алгоритмика | Algorithmics | Computation: human + classical + quantum | Интеллект-стек 2023 |
| Логика | Logic | Reasoning modes + cognitive biases | Интеллект-стек 2023 |
| Рациональность | Rationality | Explanations + decisions + actions | Интеллект-стек 2023 |
| Познание / Исследования | Cognition / Research | Conjectures + refutations practice | Интеллект-стек 2023 |
| Эстетика | Aesthetics | Style/elegance criteria (incl. AI) | Интеллект-стек 2023 |
| Этика | Ethics | Acceptable goals + means (incl. AI) | Интеллект-стек 2023 |
| Риторика | Rhetoric | Persuasion (incl. prompt engineering) | Интеллект-стек 2023 |
| Методология | Methodology | Scale-free study of methods | Метод 2025 ✅ |
| Системная инженерия | Systems Engineering | Apex normative trans-discipline | Сист.инж. 2022 ✅ |
| Системный менеджмент | Systems Management | Specialization of SE для organisations | Сист.мен. 2023 |
| Стратег | Strategist | Role doing strategizing | Метод 2025 ⚠ |
| Резидентура | Residency | МИМ 19-week mentor-led format | R-A |
| Разбор | Structured review | Biweekly mentor session | R-A |
| Мастерство | Mastery / Competency | Skill set agent has wrt method | Метод 2025 |
| Личность агента | Personality of agent | Совокупность мастерства agent's | Метод 2025 ✅ |
| ШСМ | SSM (School of Systems Management) | Levenchuk's school 2015-2025 | R-A |
| МИМ | MIM (Workshop of Engineer-Managers) | Rebranded ШСМ 2025 | R-A |
| FPF | FPF (First Principles Framework) | Левенчук's pattern language | github.com/ailev/FPF ✅ |
| SPF / TPF | SPF / TPF | Second/Third Principles Frameworks (domain-specific) | R-A ⚠ |
| IWE | IWE (Intelligent Workflow Engine) | МИМ AI personal guide | R-A |
| СМД-методология | SMD methodology | Shchedrovitsky tradition (engaged but rejected by Левенчук) | R-A |

### 9.2 FPF U.Types (English) — added vocabulary

| FPF U.Type | Definition | Pattern |
|---|---|---|
| **U.Entity** | Primitive of distinction (no structural assumptions) | A.1 ✅ |
| **U.Holon** | Whole-and-part entity (composition unit) | A.1 ✅ |
| **U.Boundary** | Physical or conceptual surface delimiting holon | A.1 ✅ |
| **U.Interaction** | Flow of matter/energy/info crossing boundary | A.1 ✅ |
| **U.System ⊑ U.Holon** | Operational physical holon | A.1 / Sys-CAL |
| **U.Episteme ⊑ U.Holon** | Knowledge holon (passive) | A.1 / KD-CAL |
| **U.BoundedContext** | Local semantic frame | A.1.1 ✅ |
| **U.RoleAssignment** | Holder#Role:Context standard | A.2.1 ✅ |
| **U.Capability** | System ability (dispositional property) | A.2.2 |
| **U.PromiseContent** | Consumer-facing promise clause | A.2.3 |
| **U.EvidenceRole** | Evidential stance | A.2.4 |
| **U.RoleStateGraph** | Named state space of role | A.2.5 ✅ |
| **U.RoleAlgebra** | In-context role relations (≤, ⊥, ⊗) | A.2.7 |
| **U.Commitment** | Deontic commitment object | A.2.8 |
| **U.SpeechAct** | Communicative work object | A.2.9 |
| **U.Method** | Abstract way of doing | A.3.1 ✅ |
| **U.MethodDescription** | Recipe for action | A.3.2 ✅ |
| **U.Dynamics** | Law of change | A.3.3 |
| **U.Signature** | Universal law-governed declaration | A.6.0 ✅ |
| **U.Mechanism** | Law-governed application | A.6.1 |
| **U.EpistemicViewing** | DescribedEntity-preserving morphism | A.6.3 |
| **U.RelationSlotDiscipline** | Slot/Value/Ref n-ary relation discipline | A.6.5 |
| **U.Work** | Record of occurrence | A.15.1 ✅ |
| **U.WorkPlan** | Schedule of intent | A.15.2 ✅ |
| **U.LanguageStateSpace** | Language-state chart over CharacteristicSpace | C.2.2a |
| **U.Episteme.SlotGraph** | Internal ontology of epistemes | C.2.1 ✅ |
| **U.Kind** | Type | C.3.1 |
| **U.RoleMask** | Contextual adaptation of Kind without cloning | C.3.4 |
| **U.AbductivePrompt** | Prompt species ready for hypothesis work | B.5.2.0 |
| **U.MultiViewDescribing** | Viewpoints + Views + Correspondences | E.17.0 |

### 9.3 Operational vocabulary

| Term | Russian | Definition | Source |
|---|---|---|---|
| Γ (Gamma) | Гамма-оператор | Universal aggregation | B.1 ✅ |
| Γ_sys / Γ_epist / Γ_ctx / Γ_time / Γ_method / Γ_work | (same) | Γ flavours | B.1.* ✅ |
| MHT (Meta-Holon Transition) | Мета-холонный переход | Emergence + re-identification event | B.2 ✅ |
| BOSC-A-T-X | (same) | MHT triggers (Boundary/Objective/Structural/Capability/Agency/Time/conteX) | B.2:4.2 ✅ |
| F-G-R | (same) | Formality + ClaimScope + Reliability triad | B.3 / C.2 ✅ |
| CL (Congruence Level) | Уровень конгруэнтности | Cross-context bridge quality | F.9 ✅ |
| SCR / RSCR | (same) | Source Citation Record / Refresh-SCR | A.10 / F.15 |
| DRR | (same) | Design-Rationale Record | E.9 ✅ |
| UTS | Унифицированный термсет | Unified Term Sheet | F.17 ✅ |
| MVPK | (same) | Multi-View Publication Kit | E.17 ✅ |
| E.TGA | (same) | Transduction Graph Architecture | E.18 ✅ |
| NQD | (same) | Novelty + Quality + Diversity | C.18 ✅ |
| E/E-LOG | (same) | Explore-Exploit Governor | C.19 ✅ |
| BLP | (same) | Bitter-Lesson Preference | C.19.1 ✅ |
| CT2R-LOG | (same) | Working-Model Relations + Grounding | B.3.5 ✅ |
| KD-CAL | (same) | Knowledge Dynamics CAL | C.2 ✅ |
| Sys-CAL | (same) | Systems CAL | C.1 |
| Kind-CAL | (same) | Kinds + Typed reasoning | C.3 ✅ |
| Compose-CAL | (same) | Constructional Mereology | C.13 |
| Resrc-CAL | (same) | Resources | C.5 |
| Decsn-CAL | (same) | Decision Theory | C.11 ✅ |
| LOG-CAL | (same) | Logic | C.6 |
| CHR | (same) | Characterisation | A.17 / C.7 ✅ |
| MM-CHR | (same) | Measurement & Metrics | C.16 ✅ |
| CN-Spec | (same) | Comparability Normalization Spec | A.19.CN ✅ |
| CG-Spec | (same) | Comparability Governance Spec | G.0 ✅ |
| CSLC | (same) | Characteristic/Scale/Level/Coordinate | A.18 ✅ |

### 9.4 External philosophical / methodological vocabulary

| Term | Definition | Source |
|---|---|---|
| Mereology | Theory of part-whole relations | Leśniewski 1916 ✅ |
| GEM | General Extensional Mereology (CEM) | Leonard-Goodman 1940 ✅ |
| Hylomorphism | Aristotle/Fine: matter + form | Fine 1999 ✅ |
| Qua-object | Object qua playing role | Fine 1999 |
| SEMAT | Software Engineering Methods + Theory | Jacobson/Meyer/Soley 2009 ✅ |
| OMG Essence | OMG standard for software engineering methods | OMG 2014 ✅ |
| OCMAS / ACMAS | Organization-Centered / Agent-Centered MAS | Wooldridge 2003 ✅ |
| AGR model | Agent/Group/Role | Ferber et al. 2003 ✅ |
| PROSA | Product-Resource-Order-Staff Architecture | KU Leuven 1998 |
| Janus phenomenon | Holon faces inward + outward | Koestler 1967 ✅ |
| S-A vs INT tendencies | Self-Assertive vs Integrative | Koestler 1967 ✅ |
| Active Inference / FEP | Free Energy Principle | Friston 2010+ |
| Constructor Theory | Possible/impossible transformations | Deutsch + Marletto 2012+ |
| Autopoiesis | Self-producing systems | Maturana + Varela 1980 |

---

## Section 10 — Recommended reading / learning order

### 10.1 Total beginner к Левенчук methodology

**Week 1-2 (foundation):**
1. **Readme.md** of FPF (38 KB) — get orientation, understand entry routes
2. **R-A** — Левенчук intellectual context (~1 hour)
3. **First chapters of *Системное мышление 2024 Том 1*** — foundational
   ontology

**Week 3-4 (depth):**
4. **R-B** — 5 primitives deep dive (~3 hours, Russian)
5. **R-D** — Essence Kernel context (~2 hours)
6. **Second volume of Системное мышление 2024** — constructor systems,
   creation graph

**Month 2 (operational):**
7. **R-C** — 16 trans-disciplines (~2 hours)
8. **Методология 2025** — primary methodology textbook
9. **МИМ residency R0 (Рациональная работа)** — practical entry

### 10.2 Practitioner с Essence/SEMAT background

**Week 1 (bridge):**
1. **R-D** — directly addresses Essence → ШСМ adaptation путь
2. **arXiv 1502.00121** — SE Essence 2015 paper

**Week 2 (FPF entry):**
3. **Readme.md** of FPF — multiple entry routes
4. Choose **route 1 (Project alignment)** or **route 4 (Lawful comparison)**
   — closest к existing Essence practice
5. Read **A.1, A.1.1, A.2, A.15** (Holon, BoundedContext, Role, Role-Method-Work)

**Week 3-4 (depth):**
6. **A.6 cluster** — Boundary discipline (NEW vs Essence)
7. **B.1 Γ algebra** — (NEW vs Essence)
8. **F.17 UTS** — direct Essence-pattern continuation

### 10.3 Jetix-specific adapter (our use case) ⭐

**Phase 1 (Pre-Gap-Analysis):**
1. **Readme.md** of FPF (skim) — understand routes
2. **THIS DOCUMENT** (Sections 1-11) — unified reference
3. **FPF-Spec preface (lines 1-766)** — 9 big storylines + Intellect Stack

**Phase 2 (Gap Analysis):**
4. **A.1, A.1.1, A.2, A.13** — root ontology + roles + agency
5. **A.14** — mereology (creation graph mapping)
6. **A.15.*** — Role-Method-Work (alpha mapping)
7. **B.2** — MHT (when does Jetix L3 become emergent holon?)
8. **B.3** — F-G-R trust calculus (assurance for AI deliverables)
9. **C.18 + C.19** — NQD + E/E-LOG (creative search для consulting)
10. **E.9** — DRR (Jetix decision-making)
11. **F.17** — UTS (Jetix terminology table)

**Phase 3 (D6 writing):**
12. **E.1 + E.2** — Vision, Mission, 11 Pillars (frame Jetix philosophy)
13. **E.5 + E.10** — Guard-rails + LEX-BUNDLE (Jetix discipline)
14. **E.17.*** — Multi-View Publication (multiple audience outputs)

**Phase 4 (long-term):**
15. **R-E** — mereology depth (organizational analogies for L3+ scale)
16. **G.* (selected)** — SoTA discipline patterns (when Jetix consults clients)

---

## Section 11 — Open questions / uncertainties

> Items requiring Ruslan review OR next-wave research.

### 11.1 Terminology decisions для D6 writing

**Q1: Preserve "Альфа" as Russian-pedagogical term, or migrate к
FPF U.Type vocabulary?**
- Option A: Keep "Альфа" — bridges к ШСМ/Essence community, Russian-friendly
- Option B: Migrate к U.RoleStateGraph + U.Episteme + U.Work/U.WorkPlan
  — FPF-current, more precise
- **Recommendation:** Hybrid — use "Альфа" as Plain name, U.X as Tech
  twin (per LEX-BUNDLE pattern)

**Q2: 17 vs 16 trans-disciplines for Jetix curriculum (if any)?**
- Жива marketing legacy "17"
- Current canonical "16"
- **Recommendation:** Use 16 always; explicitly note "historical 17"
  context if needed

**Q3: Whether to import "5 primitives" framing or use FPF pattern IDs?**
- 5 primitives (R-B) — pedagogical, Russian-friendly, jelly-condensed
- FPF pattern IDs (A.X.Y.Z) — formal, AI-friendly, granular
- ⚠ Per R-C: "5 primitives" не is Левенчук's published framing
- **Recommendation:** Use 5 primitives для exec/onboarding-level; FPF
  patterns для technical/AI-agent level

### 11.2 Architecture decisions

**Q4: How to ground "advanced mereology" в Jetix?**
- Use ComponentOf/ConstituentOf/PortionOf/PhaseOf strictly per A.14?
- Lighter "lift only what we need" stance (Section 7.6)?
- **Recommendation:** Adopt per-pattern as need arises; don't pre-engineer

**Q5: Explicit MHT (Meta-Holon Transition) tracking для Jetix L2/L3?**
- Per B.2: declare когда new whole emerges
- For Jetix solo founder: probably overkill at Phase 1
- **Recommendation:** Document MHT vocabulary в KB; defer practical
  application к Phase 2+ (when emergent clusters actually form)

**Q6: NQD-CAL + E/E-LOG for Jetix consulting work?**
- Per FPF-Spec: critical для creative search + portfolio management
- Could apply: client engagements as "creative abduction" cases
- ⚠ Substantial implementation cost
- **Recommendation:** Pilot на 1-2 client cases в Phase 2

### 11.3 AI-agent integration questions

**Q7: How strictly should FPF discipline propagate в agent role manifests?**
- Strict: every agent loads full FPF context, applies patterns explicitly
- Loose: founder maintains FPF knowledge, agents follow simplified rules
- **Recommendation:** FPF-Lite для Phase 1 agents (per R-E Section 8
  on over-formalization risks); strict только для strategist + knowledge-synth

**Q8: Should "AI agents don't strategize" rule be hard constraint?**
- Per R-B: principled position
- Operational reality: AI may need to make some method-selection decisions
- **Recommendation:** Hard constraint for true invent-mode strategizing;
  AI can do adapt-mode method selection с founder oversight

**Q9: Past-participle state convention для AI-agent task tracking?**
- Per OMG Essence + R-B: machine-parseable, principled
- Many existing AI tools use present-tense ("doing", "in progress")
- **Recommendation:** Adopt past-participle for Jetix internal alpha
  tracking; document conversion rules для external tools

### 11.4 FPF-Spec coverage gaps

**Q10: Parts H-K (Glossary, Annexes, Walkthroughs, Routes, Extensions)
appear sparse в vendored copy — are they intended to grow?**
- Per Readme.md: these "appear later in this README or in 'monolith'
  FPF-Spec.md"
- ⚠ Vendored 2026-04-20 has only J.4 visible
- **Recommendation:** Quarterly check upstream для updates

**Q11: D Part (Multi-scale Ethics) is mostly stub — implications?**
- D.1-D.4 mostly stubs; only D.5 Stable
- Suggests area of active development
- **Recommendation:** Track upstream; Jetix can defer ethics
  formalization until D matures

**Q12: Semiotics workstream (Левенчук April 2026 focus per R-A) —
when becomes part of FPF-Spec?**
- Per R-A: 10-campaign plan, April 2026 seminar
- Not yet visible в vendored 2026-04-20 FPF-Spec
- **Recommendation:** Re-vendor FPF-Spec quarterly; semiotics likely
  affects A.6 cluster

### 11.5 Strategic / governance items

**Q13: License clarification needed before any Jetix public release?**
- Per ATTRIBUTION.md: NO formal license, citation requested only
- ⚠ Public Jetix-FPF derivative may need clarification от author
- **Recommendation:** Per ATTRIBUTION.md trigger — if Jetix goes
  public с FPF-derivative content, revisit formally

**Q14: Should Jetix engage с МИМ community / Левенчук directly?**
- Pros: validate adaptation, contribute back, build relationships
- Cons: time investment, public exposure of internal architecture
- **Recommendation:** Defer until Phase 2 when Jetix has results to share

**Q15: Quarterly upstream sync trigger?**
- Per ATTRIBUTION.md: "Quarterly check для upstream updates"
- Mechanics: how, by whom, at what cost?
- **Recommendation:** Schedule recurring task; assign к knowledge-synth
  agent

---

*END OF KNOWLEDGE BASE*

*Compiled 2026-04-20 by Claude Opus 4.7 (1M context). Primary inputs:
FPF-Spec.md (62,202 lines, Levenchuk March 2026); Readme.md +
ATTRIBUTION.md; 5 Perplexity researches R-A через R-E (~394 KB
combined). Triangulation prefers FPF-Spec primary; secondary sources
cited for biographical, historical, Russian-pedagogical, philosophical
depth content not present в primary.*
