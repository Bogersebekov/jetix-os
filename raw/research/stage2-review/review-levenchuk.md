---
type: stage2-review
role: levenchuk-expert
reviewer: claude-opus-4-7-subagent
input: raw/research/architecture-implementation-synthesis-2026-04-19.md
references:
  - raw/research/levenchuk-for-ai-deep-research-2026-04-19.md
  - raw/research/levenchuk-deep-research-2026-04-18.md
created: 2026-04-19
length: ~4900 слов
---

# Левенчук / ШСМ Expert Review — Jetix Architecture Synthesis v1

> Ontological correctness audit. 5 примитивов deep-dive. Защита ШСМ-фреймворка
> от dilution в AI-extension.

---

## Executive Ontological Assessment

**Общий вердикт: partially correct, с системным риском dilution в трёх местах.**

Synthesis — добросовестная попытка переложить 5 примитивов ШСМ (роль, альфа,
граф создания, стратегирование, мышление письмом) в L2 Cognitive слой
AI-native архитектуры. Автор synthesis (1) корректно идентифицировал
центральный тезис R3 — «framing/acceptance — узкое место AI-эпохи»,
(2) сохранил тезис «роль ≠ исполнитель» как операционный инвариант, и
(3) аккуратно отделил «invent» (стратегирование) от «adapt» (альфа, граф,
мышление письмом) от «1:1» (роль). Это уже выше планки большинства
промышленных адаптаций ШСМ.

Однако: **там где synthesis встречается с инженерным давлением (folder
structure, role-manifest YAML, machine validation), онтологическая
чистота systematically уступает практичности**. Три самых важных
случая dilution:

1. **Альфа vs Work Product collapse.** Synthesis называет альфой и Client
   (lifecycle entity, корректно), и Invoice (work product, де-факто документ),
   и SKU (по сути Entity без state machine — Левенчук: «Entity / Object —
   объект без state machine»). Из 10 «alphas» как минимум 2 (Invoice,
   SKU) — НЕ альфы по строгому определению Essence. Это смешение
   примитивов на уровне терминологии.

2. **Past-participle convention нарушена.** Левенчук в R3 §A.2 explicit:
   «Состояния формулируются глаголами в прошедшем времени: не "Planning",
   а "Planned"». Synthesis повсюду использует **gerunds и nouns**:
   `lead`, `qualified`, `proposed`, `negotiating`, `closed-won`,
   `in-progress`, `delivery`, `validating`, `at-risk`. Из 50+ состояний
   через все 10 альф — past-participle строго соблюдается только в
   ~30%. Это не косметика: gerunds («negotiating», «validating») — это
   **процесс**, а не состояние; Essence именно потому требует past-participle,
   что состояние = checklist завершённых критериев.

3. **Граф создания свёлся к dependency list.** Synthesis помещает
   «graph_of_creation» в Block 4 role-manifest как `produces: [...]` /
   `consumes: [...]`. Это **bipartite supplier-consumer граф ролей с
   артефактами** — близко к [Sociocracy 3.0 role pattern], но не
   ориентированный мереологический граф **систем**, который
   определяет ШСМ. У Левенчука в R3 §A.3: «в узлах стоят **системы**,
   а рёбра — отношение "кто создаёт кого"», плюс рекурсивное свойство
   («системы-создатели сами — системы»). В synthesis нет ни single
   места, где зафиксированы **системы** как узлы (target system,
   creation system, supersystem) и их **mereological relationship**.
   Граф создания деградировал до workflow chart.

Что сделано **хорошо** и не должно меняться:

- Strategic-management role attribution исключительно Ruslan'у в L0,
  с прямым echo R3 §F.7 «Стратегирование — invent, агенты могут support
  но не страегировать» — это правильно и должно быть защищено от
  любых будущих compromise (например, «strategist» агент НЕ должен
  получить strategizing autonomy).
- Anti-pattern «полная автоматизация writing» (synthesis Part 2 Area 6
  принципы 6 «Writing as thinking») — корректно цитирует R3 §E.3.
- 5-layer per-agent memory structure эпистемологически согласована с
  тезисом «AI не имеет inner life» (R3 §F.1) — экстернализация tacit
  knowledge через explicit context файлы.
- FPF-Lite границы (включает 4-6 U-Types, исключает 17 disciplines/
  full mereology/Kit Fine) — честная linia для Phase 1, не overreach.

**Итоговая оценка:** synthesis не violates ШСМ концептуально, но в
нескольких ключевых operational деталях dilutes онтологическую чистоту.
Все три identified issue — fixable за 4-8 часов работы над v2 без
структурных изменений архитектуры. **Verdict: YES with changes**, при
условии исправления Альфа/Work Product confusion, past-participle
convention и Graph of Creation deepening.

---

## Part 1 — 5 Primitives Audit

### 1.1 Role primitive

**Synthesis treatment.** Area 3 Role Manifests + Part 3 Conflict 2
адоптируют 8-block manifest (R3 §C.1-C.9). Block 6 (`implementation_ai`)
и Block 7 (`implementation_human`) — оба внутри одного `role.md`.
Дополнительно: separate `executors/<id>.yaml` (Holacracy decoupling,
Area 2 Folder Structure).

**Левенчук position.** R3 §A.1: «Гамлет — это **роль**, конкретный
актёр на сцене — **исполнитель**»; «Роль — функция, актор — конкретный
исполнитель: человек, команда, организация или ИИ». R3 §F.7: роль
Адресована как 1:1 mapping в AI — «Уже абстракция от исполнителя».

**Verdict: ⚠️ partially correct, с тремя concerns.**

**Concern #1: Implementation-blocks blur role/executor boundary.**
Synthesis 8-block manifest содержит **внутри одного `role.md`** оба
`implementation_ai` (с current-executor: claude-opus-4-7) и
`implementation_human` (с hired-person, kpis, onboarding-path). По
строгой ШСМ: эти данные принадлежат к executor-объекту, а не к роли.
Когда роль `sales-lead.role.md` содержит `current-executor:
claude-opus-4-7`, она де-факто становится executor-binding документом.
Если завтра тот же `sales-lead` роль исполняется AI + human concurrently
(Phase 2 co-pilot mode, явно описан в onboarding-path), один файл
не сможет описать оба executor cleanly.

**Proposed fix:** Move `implementation_ai` + `implementation_human` из
`role.md` → отдельные `executors/<exec-id>/binding.yaml` файлы, которые
**ссылаются на** `roles/<slug>/role.md` через `assigned-role: sales-lead`.
Тогда роль остаётся чистой абстракцией; multiple executors на одну
роль становятся expressible (debatable agent ensembles, A/B model
testing). Synthesis уже имеет `executors/<id>.yaml` файлы (Area 2),
но не использует их fully — implementation-blocks дублируются в обоих
местах.

**Concern #2: Multi-role executor pattern не addressed.** R3 §A.1
explicit critique: «(1) размытая многоролевость (founder + CEO + CTO
одновременно)». Synthesis Part 5.4 признаёт это как open question, но
Part 4 Q3 («Strategic-management роль декомпозиция») **отдаёт решение
наверх Ruslan'у вместо предложения ontologically-clean answer**.
ШСМ-correct ответ: одна executor (Ruslan) исполняет N ролей через
явные **role-context switches**; ролей не объединяют в monolithic
"strategic-management" pseudo-role с пятью разными accountabilities,
которые на самом деле принадлежат пяти разным ролям.

**Proposed fix:** В D3 manifest для Ruslan не делать одну роль
«strategic-management», а сразу декомпозировать на 5 атомарных ролей
(`strategy-lead`, `framing-lead`, `sales-closer`, `acceptance-authority`,
`external-relations`), каждая с своим manifest. Один executor (Ruslan)
fills все пять. Это ШСМ-canonical answer на «multi-roled founder»
critique.

**Concern #3: Dynamic role assignment не определён.** R3 §A.1 также
critique: «(2) dynamic role assignment в AI-агентах (агент назначает
себе роль сам по ситуации)». Synthesis не запрещает это и не
определяет. Если завтра sales-lead agent самовольно «играет»
delivery-роль для одного task — нарушение или допустимое поведение?
Это onto-operational vacuum.

**Proposed fix:** В FPF-Lite §5 Internal Principles добавить explicit:
«Role assignment — only via assigned-role in executors/binding.yaml.
Dynamic role-switching by agent at task-time = anti-pattern.
Cross-role escalation through manager, not through role-switch.»

---

### 1.2 Alpha primitive

**Synthesis treatment.** 10 alphas с state machines (Area 5, Part 3
Conflict 1, Appendix B). Hybrid C storage. State machines в R3 Part D
определены mermaid diagrams. Synthesis explicit: alphas с state.yaml +
context.md + history.jsonl per instance.

**Левенчук position.** R3 §A.2: альфа — *«essential element of the
software-engineering endeavour — one that is relevant to an assessment
of its progress and health»* (Essence 1.2). Альфа НЕ является ни
документом, ни задачей, ни процессом. Чёткое разграничение:

| Понятие | Суть | Пример |
|---------|------|--------|
| Alpha | Предмет метода с отслеживаемыми **состояниями** | Requirements, Team |
| Work product | Артефакт, **результат работы** | Документ требований, код |
| Entity / Object | Объект **без state machine** | Клиент как юр. лицо |
| Activity | **Действие** по методу | Sprint planning |

**Verdict: ⚠️ concerns в 3 из 10 alphas, плюс past-participle violation
в 7 из 10.**

**Concern #1: Invoice — это work product, не alpha.** Synthesis D.4
определяет Invoice states `issued → sent → paid → reconciled` +
`disputed`. Но Invoice по своей природе — **документ** (work product
в Essence), результат работы Deal alpha. State machine приклеена
искусственно: «sent» — это event на Invoice (физическое действие
отправки), не состояние документа. «Paid» — это состояние **Deal**
alpha (financial closure), не Invoice. У Левенчука в R3 §A.2 этот
случай прямо в anti-example: «Document требований — work product,
Requirements — alpha».

**Proposed fix:** Удалить Invoice из списка 10 alphas. Заменить
явным work-product-tracking pattern: `clients/invoices/YYYY/R-YYYY-NNNN.{md,yaml}`
с metadata «issued-at / paid-at / status», но без претензии на
state machine alpha. Lifecycle тогда живёт в Deal alpha
(`deal.state: signed → invoiced → paid → completed`). Это редуцирует
до 9 alphas с чистой типизацией.

**Concern #2: SKU — это Entity, не alpha.** D.7 SKU states `idea →
prototype → launched → active → deprecated`. Эти «states» де-факто
описывают **роль SKU в product portfolio во времени** — это Wardley map
evolution stage, а не lifecycle state по Essence convention. SKU после
launch не «прогрессирует» через lifecycle с verifiable acceptance
criteria — он просто существует в catalog. Synthesis Part 3 Conflict 1
это de facto признаёт: «SKU YAML-only, stable, no state machine after
issuance».

**Proposed fix:** SKU перенести в `entities/skus/<sku>.yaml` или
`products/<sku>.yaml`, не считать alpha. Заменить в списке: добавить
**Way of Working** alpha (Essence Kernel Endeavour group, отсутствующая
в synthesis 10), которая трекает evolution самой Jetix методологии (как
работает компания, какие практики живые). Это критично для AI-native
mega-corp — Way of Working IS продукт R&D.

**Concern #3: Hypothesis vs Research Note vs Postmortem — какой alpha?**
Synthesis декларирует все три как wiki-primary alphas в `wiki/claims/`,
`wiki/sources/`, `wiki/experiments/`. Это accepted, но вопрос: они
действительно «предметы метода с отслеживаемыми состояниями» или это
**работа над одной alpha — Knowledge** (R3 не явно, но логично)?
Postmortem содержит lessons learned, которые feed в Way of Working.
Research Note — knowledge artifact. Hypothesis — единственная из трёх
с настоящим state machine («formulated → validating → validated/
invalidated» — это falsifiability lifecycle, alpha-grade).

**Proposed fix:** Hypothesis — оставить как alpha. Research Note и
Postmortem — переклассифицировать как **work products of Knowledge alpha**
(или Way of Working alpha), хранить в wiki/, но без state machine
претензии. Это сократит и упростит. Либо honest: «10 entities, из них
6 alphas (Client, Project, Deal, Content Item, Hypothesis, Member),
3 work products (Research Note, Postmortem, Invoice), 1 entity (SKU)».

**Concern #4: Past-participle convention systemically нарушена.**
Левенчук R3 §A.2: «не "Planning", а "Planned"». Audit of states:

| Alpha | States | Past-participle compliance |
|-------|--------|---------------------------|
| Client | lead, qualified, proposed, negotiating, closed-won, closed-lost, churned | 4/7: «lead» (noun), «proposed» ✅, «qualified» ✅, «negotiating» ❌ (gerund), «closed-won» ✅, «closed-lost» ✅, «churned» ✅ |
| Project | scoped, kicked-off, in-progress, delivery, closed, follow-up | 2/6: «scoped» ✅, «kicked-off» ✅, «in-progress» ❌, «delivery» ❌ (noun), «closed» ✅, «follow-up» ❌ |
| Deal | draft, signed, active, completed, cancelled | 4/5: «draft» ❌, остальные ✅ |
| Invoice | issued, sent, paid, reconciled, disputed | 5/5 ✅ (но см. concern #1 — это не alpha) |
| Content | draft, in-review, approved, published, retired | 3/5: «draft» ❌, «in-review» ❌, «approved» ✅, «published» ✅, «retired» ✅ |
| Hypothesis | formulated, active, validating, validated, invalidated, implemented | 4/6: «active» ❌, «validating» ❌ |
| SKU | idea, prototype, launched, active, deprecated | 2/5 ✅ (но не alpha) |
| Member | applied, invited, active, at-risk, churned | 3/5: «active» ❌, «at-risk» ❌ |
| Research Note | started, draft, completed, integrated | 3/4 |
| Postmortem | incident, draft, reviewed, action-items, closed | 2/5: «incident» ❌, «draft» ❌, «action-items» ❌ |

**Aggregated: ~52% violations.** Это не косметика — gerunds
(`negotiating`, `validating`) описывают процесс, а Essence требует
checklist completed criteria. «Validated» = acceptance criteria met.
«Validating» = ongoing activity, не state.

**Proposed fix:** Systematic rename per audit table: `negotiating →
in-negotiation` (если требуется фаза) ИЛИ split на `proposal-presented`
и `terms-finalized`. `in-progress → started` или `executed`. `delivery
→ delivered`. `active → activated` (прошедшее participle, означает
момент перехода в operational). `at-risk → flagged-at-risk`.
`draft → drafted`. `validating → under-validation` или ещё лучше split:
`hypothesis-tested-once → hypothesis-tested-three-times`. Это не
prettification — это синхронизация с Essence semantics.

---

### 1.3 Graph of Creation

**Synthesis treatment.** Block 4 role-manifest содержит:

```yaml
graph_of_creation:
  produces: [{artifact: pipeline-report, consumers: [...]}]
  consumes: [{artifact: qualified-contact, produced_by: sales-research}]
```

Дополнительно: Area 5 mermaid diagram с ролями как узлами и стрелками
(R3 §H.1 §3). Auto-generation script `grep produces:|consumes: roles/`
→ DOT (R3 §G.3).

**Левенчук position.** R3 §A.3: «Граф создания — ориентированный граф,
в узлах которого стоят **системы**, а рёбра — отношение "кто создаёт
кого"». Ключевое: «Граф создания **мереологически ориентирован**:
системы-создатели сами — системы, которые кто-то создаёт. Это
рекурсивное свойство делает его средством навигации по уровням
сложности.» Также: «целевая система vs creation system vs supersystem».

**Verdict: ❌ violation. Это не граф создания, это bipartite supplier
chart.**

**Concern #1: Узлы — артефакты, не системы.** Synthesis-граф имеет
roles → artifacts → roles structure. Но в ШСМ узлы — **системы**.
Sales-lead роль не создаёт «pipeline-report», она создаёт (или
поддерживает) **client-pipeline systeme**. Pipeline-report — view на
эту систему. Без узлов-систем граф не может выполнить свою главную
функцию: показать, какая роль что **создаёт в мире** (что-то существенное
вне docs).

**Concern #2: Mereology отсутствует.** В ШСМ-canonical creation graph
target system декомпозируется на subsystems, каждая из которых имеет
свой creation team. Synthesis не имеет ни одного места, где Jetix-system
декомпозирована мерологически. FPF-Lite §1 называет «AI-native delivery
process» как target system — но это не декомпозировано на subsystems
(client-pipeline, knowledge-system, executor-pool, evaluation-loop, etc.).

**Concern #3: Bidirectional creation не выражена.** Левенчук:
«системы-создатели сами — системы, которые кто-то создаёт». Кто
создаёт sales-lead роль? Кто её обновляет? Это manager-роль + meta-agent
+ Ruslan. Это второй уровень creation graph, который synthesis вообще
не addresses. Org chart в Git без этого слоя не работает на mega-corp
scale.

**Proposed fix:** В D6 FPF-Lite добавить отдельный artifact
`jetix-creation-graph.md` с тремя слоями:

1. **Level 1 (Operational):** Target system (Client Outcome — successfully
   delivered AI-engagement) → создаётся системами Sales-Pipeline,
   Delivery-Engagement, Client-Relationship — каждая со своими
   subsystems.
2. **Level 2 (Methodological):** Sales-Pipeline создаётся ролями
   `sales-research`, `sales-lead`, `sales-outreach` + tools (CRM, eval).
   Эта система сама — артефакт, который создают: Ruslan +
   role-framework + meta-agent.
3. **Level 3 (Meta):** Role-framework + ШСМ-онтология + writing-templates
   создают **способность** системы существовать — это создаётся Ruslan +
   ШСМ-влияние + AI-tools (Claude Code как platform).

Каждый уровень — Mermaid diagram с системами-узлами (не артефактами,
не ролями). Block 4 «graph_of_creation» в role-manifest остаётся
useful как **dependency view** (workflow chart), но переименовать в
`production_dependencies`, чтобы не путать с настоящим creation graph.

---

### 1.4 Strategizing

**Synthesis treatment.** Part 2 Area 6 FPF-Lite Section 7 «Strategizing
Protocol»; Area 8 monthly cadence «strategizing trigger check»; Part 1
principle 7 «5 примитивов ШСМ, selectively. ... стратегирование (invent
= исключительно Ruslan)»; folder `strategizing/YYYY-MM-DD-<slug>.md`.
Template из R3 §E.1 (8 sections). R3 §F.7 «Стратегирование — invent.
Агенты не стратегируют — нет identity, нет долгосрочной памяти, нет
commitment к выбору. Исключительно роль Ruslan. Агенты могут support
(генерировать alternatives, проверять anti-scope).»

**Левенчук position.** R3 §A.4: «Метод выбора метода — стратегирование»;
«трёхступенчатый примат: стратегирование → планирование → работа.
Без стратегирования планирование невозможно — потребные ресурсы
неизвестны». Strategizing precedes business-strategy в literal sense
(strategizing выбирает метод, business strategy = выбранный метод).
**Strategizing happens только при unknown** («не знаю что делать»),
не как regular ceremony.

**Verdict: ✅ correct in principle, ⚠️ две second-order concerns.**

**Concern #1: «Monthly strategizing trigger check» risks ceremony.**
Synthesis Area 8 daily/weekly/monthly/quarterly cadence помещает
«strategizing trigger check» в monthly. Это правильно как **trigger
check** (проверить, не появился ли сигнал unknown), но если Ruslan
будет проводить strategizing session каждый месяц по календарю — это
**violates** strategizing-only-on-unknown principle. Strategizing
становится ритуалом ради ритуала, превращается в ежемесячное
business-planning под другим именем.

**Proposed fix:** В D6 FPF-Lite Section 7 добавить explicit:
«Strategizing — событие, не ceremony. Triggers: ... [перечень].
Если за месяц ни одного trigger — strategizing НЕ проводится. Monthly
check — это **проверка наличия trigger**, не сам strategizing». Также:
`strategizing/YYYY-MM-DD-<slug>.md` slug должен начинаться с trigger
description (не с date), чтобы было видно что породило сессию.

**Concern #2: «Strategist» agent имя misleading.** Synthesis имеет
agent role `strategist` (R1 mapping J4, current 12 agents список).
По строгой R3 §F.7 «агенты не стратегируют». Если agent называется
«strategist», возникает confusion. Либо agent действительно strategizes
(violation R3) — либо он что-то другое (research support, options
generation, scenario analysis), и название misleading.

**Proposed fix:** Renamed `strategist → strategy-research-support`
или `strategy-options-generator`. Это honest naming. Альтернатива:
оставить «strategist» с explicit `out_of_scope: ["Make strategic
decisions", "Choose method (strategizing)"]` в role-manifest. R3 §F.7
прямо это указывает, но synthesis Area 7 Career Levels mapping
помещает strategist на J4 «Principal — Business decisions в функции»
— этот wording НЕ исключает стратегические решения. Conflict.

---

### 1.5 Thinking by Writing

**Synthesis treatment.** FPF-Lite §5 Internal Principle 7 «Writing as
thinking. Мысль не существует, пока не написана.» Part 2 Area 8 ritual
cadence: daily-log, weekly-review, monthly note, quarterly letter.
R3 §E.3 cited — «Human writes → Agents extract → Agents propose» pattern.
Anti-pattern «полная автоматизация writing» preserved.

**Левенчук position.** R3 §A.5: «Системное мышление происходит путём
мышления моделированием... и письмом... Мышление письмом — не
документирование, а **онтологизация** мышления: типизация свободного
текста». R3 §E.3 explicit: «Письмо — не output, это process».

**Verdict: ✅ correct, с одной concern на edge.**

**Concern: `Agent as critic` для strategizing-документов рекомендуется,
но threshold не определён.** R3 §E.3: «Агент как критик — для
стратегирование-документов рекомендуется (есть ли минимум 2
альтернативы? acceptance criteria? anti-scope?)». Synthesis принимает,
но не определяет, в какой момент agent-critique входит:
- ДО написания (предварительная structured outline) — нарушение
  «writing-as-thinking happens DURING writing process».
- ПОСЛЕ написания (review draft) — OK, как proofreader/structure-checker.
- ПАРАЛЛЕЛЬНО (autocompletion типа Cursor) — нарушение, ломает
  generation effect (van der Meer 2024 cited в R3).

**Proposed fix:** В D6 FPF-Lite §5 add: «Agent participates as critic
ONLY на завершённый draft. Не co-author, не autocompleter, не
outline-suggester. Strategizing/letter writing process выполняется
Ruslan'ом sin agent assistance во время initial draft phase. После
draft — agent reads → проверяет structural completeness checklist →
flags missing sections». Это сохраняет Naur «Programming as Theory
Building» analogy (R3 §A.5): theory building возможен ТОЛЬКО через
human cognitive struggle с написанием, не через AI suggestions.

---

## Part 2 — FPF-Lite Honesty Review

**Honest subset или approximation? Ответ: honest subset, с одной
overreach.**

**Что включено правильно:**

- Target System (FPF Kernel concept) ✅
- Stakeholders (системно-инженерная классика) ✅
- Creation Graph (5 примитивов, см. concerns 1.3) ⚠️
- Roles 5-7 ключевых ✅
- Key Alphas (5 → расширено до 10, см. concerns 1.2) ⚠️
- Strategizing Protocol ✅
- Writing Principles ✅
- U-Types Lite (4-6) ✅

**Что исключено правильно (Phase 1 scope):**

- Полная иерархия холонов ✅ (но см. concern ниже)
- 17 трансдисциплин (read-only ref) ✅
- Advanced mereology Kit Fine ✅
- Category theory ✅
- Constructor theory ✅
- Architectural invariants полного FPF ✅

**Concern: U-Types Lite список неполный.** Synthesis: «U.System, U.Role,
U.Method, U.Stakeholder». Это 4. Но R3 §B.1 определяет U.Types через
Kernel: «U.System, U.Objective, U.Reliability» — OBJECTIVE отсутствует
в synthesis. Без U.Objective модель не может выразить «зачем» (purpose
hierarchy), что критично для acceptance criteria и для разговора с
Mittelstand клиентами на их языке. Аналогично U.Method без U.Decision
не может моделировать decision-making как объект.

**Proposed fix:** Расширить U-Types Lite до 6: U.System, U.Role, U.Method,
U.Stakeholder, **U.Objective, U.Decision**. Это всё ещё минимальный
upper ontology, но closing the gap для objectives + decision records.

**Mereology/holons cleanly excluded?** Yes — synthesis не претендует
на холоны. Но edge case: Model D Nested Hierarchy (Life-OS root, Jetix
nested project) — это **де-факто mereological structure** (Jetix-as-part
of Life-OS-as-whole). Если FPF-Lite excludes mereology, как обосновать
Model D Nested? Это inconsistency: synthesis использует mereological
intuition в архитектурных решениях, но не expose её как principle.

**Proposed fix:** Либо honest «Lightweight mereology — Jetix-as-part-of
Life-OS — explicit принцип; advanced mereology (Kit Fine, constructor
theory) excluded»; либо удалить Model D nested framing, заменить на
«parallel projects sharing methodology layer». Текущее состояние —
mereology used implicitly без acknowledgment.

---

## Part 3 — AI-Adaptation Risks

**R3 §F.1-F.7 явно адресует AI-adaptation. Synthesis наследует это
correctly с одним notable risk.**

**Risk #1: «Context engineering replaces prompt engineering» применён
правильно, но не distinguishes между context AS exocortex vs context
AS state.** R3 §F.3 cites Karpathy: context engineering = «filling the
context window with just the right information for the next step».
Synthesis treats per-agent memory 5 layers как context engineering, но
смешивает два разных типа:
- **Exocortex layer** (CLAUDE.md, role.md, FPF-Lite, decisions/) —
  durable knowledge, theory of operation. Loaded each session.
- **State layer** (alphas/state.yaml, history.jsonl, scratchpad.md) —
  ephemeral, task-specific.

Это разные epistemological objects. Их смешение в одном «context budget
50K tokens» (Area 5) рискует deteriorate, когда state layer выталкивает
exocortex out of context при busy week.

**Proposed fix:** В D5 KNOWLEDGE-ARCHITECTURE add explicit budget split:
«25K tokens hard reservation for exocortex (system/strategies/role/FPF);
25K tokens soft for state/scratchpad/RAG. Never compress exocortex». Это
implicit в synthesis, нужно сделать explicit.

**Risk #2: «AI agents as new participants of master class» (R3 §B.5
МИМ-2026 thesis) не отражён в архитектуре.** Левенчук: «AI-агенты как
новые участники мастерской — их нужно обучать по тем же руководствам,
что и людей». Synthesis имеет `implementation_human` block с
onboarding-path, но NO equivalent `agent_onboarding_path` block. AI agent
получает role.md и работает — нет explicit onboarding journey
(progressive disclosure of FPF, role-specific tutorials, golden
examples calibration).

**Proposed fix:** В Block 6 Implementation AI добавить subsection
`agent_onboarding`:
```yaml
agent_onboarding:
  initial_context_pack: [docs/onboarding/agent-orientation.md, ...]
  warm_up_tasks: [3-5 tasks от простых до domain-specific]
  calibration_checkpoint: "after 10 tasks → eval against golden, threshold 0.85"
```

**Risk #3: Role-manifest как «worldview не rules» (Anthropic Constitution
2026 в R3 §F.4) присвоен но не enforced.** Synthesis Block 3 Method
содержит `anti_patterns` — это rules-based approach. Левенчук-style
worldview means agent generalizes principles. Лучший pattern: добавить
`reasoning_examples` field — narratives того, как роль mediates between
competing concerns в edge cases.

**Proposed fix:** Block 3 Method добавить optional field
`reasoning_examples: [path to narrative .md]` с примерами «когда роль
sales-lead должна выбрать между discount и walking away — narrative
с reasoning, не правило».

---

## Part 4 — Role-Manifest Format Review

| Block | R3 fidelity | Verdict | Concerns |
|-------|------------|---------|----------|
| 1. Identity | High | ✅ | Naming convention OK |
| 2. Ontological | High | ✅ | `purpose` + `target-system` + `primary-alpha` correct mapping |
| 3. Method | Medium | ⚠️ | `anti_patterns` is rules-based; нет worldview-style reasoning. Add `reasoning_examples` |
| 4. Graph of Creation | Low | ❌ | Это dependency list, не creation graph (см. 1.3). Rename `production_dependencies` |
| 5. Seniority/Scale | Hybrid | ⚠️ | R3 не содержит career levels — это R1 import. Honest, но `decision-rights` matrix can read как corporate org chart, не Левенчук role definition |
| 6. Implementation AI | Medium | ⚠️ | Дублирует executor binding (см. 1.1 concern #1). Move к executors/ |
| 7. Implementation Human | Medium | ⚠️ | Same dublication. Move к executors/ |
| 8. Evolution | High | ✅ | Audit trail correct |

**Overall format verdict:** 8 blocks **structurally OK** для AI-native
mega-corp aspiration, но онтологически 3 блока (4, 6, 7) need cleanup:
Block 4 переименовать; Blocks 6-7 — extract в executor-binding files.
После cleanup core role.md содержит Blocks 1, 2, 3, 5, 8 — это
roughly maps к R3 §C.1-C.5 + С.8 + Holacracy Role Definition (Purpose
+ Domains + Accountabilities). Чище.

---

## Part 5 — Specific Ontology Concerns

(Детальный walk-through Part 5.4 items из synthesis.)

**5.4 Item 1 — Multi-role executor (Ruslan).** Addressed in 1.1 concern #2.
**Synthesis answer:** не решено, defer to Ruslan. **ШСМ-correct answer:**
декомпозировать на 5 sub-roles, один executor fills все. Не предлагать
`strategic-management` monolithic role.

**5.4 Item 2 — Manager agent orchestration.** Synthesis имеет manager
role «coordinates other agents». Это **coordinator role** (Holacracy:
Lead Link circle), legitimate. Но если manager делает решения **на
behalf of** sales-lead role — нарушение. Cleaner pattern: manager
**routes** tasks к sales-lead и **enforces** acceptance criteria,
но не **substitutes** sales-lead.

**Proposed fix:** В manager role-manifest explicit `out_of_scope: ["Make
domain decisions on behalf of other roles", "Override role accountabilities"]`.

**5.4 Item 3 — Dynamic role assignment.** Addressed in 1.1 concern #3.
ШСМ-correct: forbid dynamic role-switching by agents. Roles assigned
statically through executor binding.

**5.4 Item 4 — Холоны recursive (Ruslan as executor → role → Jetix
holon → Life-OS holon).** Это правильное mereological intuition.
Synthesis Model D Nested Hierarchy implicit подтверждает. Но FPF-Lite
excludes mereology. Inconsistency (см. Part 2 above).

**Proposed fix:** Добавить «Lightweight mereology» как explicit FPF-Lite
component (см. Part 2 fix).

**5.4 FPF-Lite honesty Item 1 — 3-5 pages truly Левенчук subset?** Yes,
но с overreach: 4 U-Types недостаточно, 6 нужно (см. Part 2).

**5.4 FPF-Lite honesty Item 2 — Excluded cleanly или postponed?**
Mostly cleanly excluded. Mereology — postponed, не excluded (см. above).

**5.4 FPF-Lite honesty Item 3 — Risk «переводить на язык доминирующей
области»?** **Yes, real risk.** R3 §B.4: LLM tendency «всё на Фортран».
Symmetric risk: synthesis (writeen by Claude) translates ШСМ в
software-engineering language: SemVer для ролей (Block 1 version), git
tags, JSON Schema, CI/CD validation, lint rules, golden datasets. Это
все pragmatically useful, но риск: ШСМ становится «software practices
с ШСМ названиями». Доказательство: state machines рисуются как
mermaid diagrams (software diagrams), не как Essence State Cards
(карточки состояний с текстовыми checklist criteria, как у Левенчука).

**Proposed fix:** В D6 FPF-Lite добавить раздел «What ШСМ is NOT»:
- ШСМ роль ≠ software class или GitHub team
- ШСМ alpha ≠ database table или Kanban column
- ШСМ creation graph ≠ workflow diagram или dependency tree
- ШСМ strategizing ≠ planning meeting или OKR session
- ШСМ thinking by writing ≠ documentation generation или Confluence pages

Это явная защита от software-language colonization.

---

## Part 6 — Terminology Consistency

Audit terminology через synthesis:

**«Роль» vs «agent»:**
- Synthesis explicit: «role ≠ executor», role-abstraction, etc. Хорошо.
- НО: «12 agents» в Executive Summary, «agents/<id>/» folder, «agent
  mailboxes». В разговорной части synthesis «agent» означает
  executor + role bundle. Должно быть «12 executors filling N roles»
  где N может быть < 12 (Ruslan executor fills multiple roles) или
  > 12 (агент может fill multiple roles).

**Proposed fix:** Glossary entry: «Agent — colloquial = AI-executor.
Strictly = Claude-instance executing N role-manifests. Не
взаимозаменяем с role». Audit synthesis для terminology consistency.

**«Альфа» vs «entity» vs «data object»:**
- Synthesis Appendix B: «Alpha — Essence Kernel concept. Lifecycle entity
  with states, not data object or process.» ✅
- НО Invoice, SKU обозваны alphas — нарушение own definition (см. 1.2).

**Proposed fix:** Apply 1.2 fixes — reduce 10 alphas → 6 true alphas +
3 work products + 1 entity.

**«Метод» vs «процесс»:**
- Synthesis preserves R3 distinction (Block 3 Method = epistemology,
  rituals = process). ✅
- BUT: Area 8 «Daily/Weekly/Monthly/Quarterly rituals» mixes both
  (writing rituals = writing-as-thinking, не process; sales pipeline
  review = operational process). Conflation.

**Proposed fix:** Split Area 8 в две parts: «Cognitive rituals»
(writing, strategizing, reflection — exocortex maintenance) vs
«Operational cadences» (pipeline, billing, monitoring — process).
Different epistemological status.

**«Стратегия» (business) vs «стратегирование» (ШСМ):**
- Synthesis preserves distinction via folder name (`strategizing/`, не
  `strategy/`) ✅
- BUT: Part 1 principle 7 mentions «Стратегирование (invent =
  исключительно Ruslan)» — кажется, что Ruslan имеет roleg strategist;
  потом R1 Career Ladder есть `strategist` agent на J4. Confusion.

**Proposed fix:** Rename agent `strategist → strategy-options-generator`
или `strategy-support-analyst`. Strategizing-the-process — только
Ruslan. Strategy-as-business-plan (документ) — output strategizing
session, может быть assisted by strategy-support-analyst.

---

## Part 7 — Proposed Changes для v2

Operational checklist для Stage 3 final synthesizer:

1. **Reduce 10 alphas → 6 true alphas.** Remove Invoice, SKU, Postmortem,
   Research Note from alphas list. Add Way of Working alpha.
2. **Past-participle audit & rename.** Apply audit table из 1.2:
   `negotiating → in-negotiation`, `in-progress → started`, `delivery
   → delivered`, `validating → under-validation`, `at-risk →
   flagged-at-risk`, `draft → drafted`, etc.
3. **Extract `implementation_ai` + `implementation_human` из role.md
   в `executors/<exec-id>/binding.yaml`.** Role.md остаётся pure
   abstraction. Multiple executors per role становится possible.
4. **Decompose `strategic-management` Ruslan-role на 5 atomic roles.**
   `strategy-lead`, `framing-lead`, `sales-closer`, `acceptance-authority`,
   `external-relations`. Один executor fills все 5.
5. **Forbid dynamic role assignment.** FPF-Lite §5 explicit principle
   + role-manifest Block 5 `out_of_scope: ["Switch role at task-time"]`.
6. **Rename Block 4 `graph_of_creation` → `production_dependencies`**.
   Add separate `jetix-creation-graph.md` artifact с настоящим
   ШСМ-style creation graph (3 levels mereological).
7. **U-Types Lite expanded: 4 → 6.** Add U.Objective, U.Decision.
8. **Strategizing — событие, не ceremony.** D6 FPF-Lite §7 explicit
   trigger-only language. Monthly check = trigger detection, not session.
9. **Rename agent `strategist` → `strategy-support-analyst`.** Avoid
   confusion с strategizing-as-Ruslan-only.
10. **Add «What ШСМ is NOT» section в D6 FPF-Lite.** Защита от
    software-language colonization.
11. **Hard reservation 25K tokens for exocortex** в context budget
    (D5). Никогда не compresses durable knowledge.
12. **Add `agent_onboarding` field в Block 6.** Initial context pack +
    warm-up tasks + calibration checkpoint.
13. **Add `reasoning_examples` optional field в Block 3.** Worldview
    pattern, не just rules.
14. **Lightweight mereology explicit в FPF-Lite.** Acknowledge Model D
    nested as mereological pattern; honest exclusion of advanced
    (Kit Fine, constructor theory).
15. **Manager role-manifest explicit `out_of_scope`** для domain
    decisions on behalf of other roles. Coordinator pattern, не
    substitute pattern.

---

## Part 8 — Questions для Final Synthesizer

Meta-questions для Stage 3:

1. **Должен ли v2 strict-enforce past-participle convention для всех
   alpha states, или допустить «practical compromise» с readability
   priority?** ШСМ-strict = past-participle всегда; pragmatic = «proposed»
   OK, но «negotiating» приемлем для UX. Это ontological purity vs
   AI-readability trade-off. Recommend strict.

2. **Если декомпозировать Ruslan-role на 5 атомарных, как трактовать
   «Founder Mode» (Paul Graham 2024) preservation?** Founder mode
   подразумевает fluid role-switching by Ruslan. ШСМ-strict: фиксированные
   роли. Pragmatic: founder is unique exception. Recommend hybrid:
   5 ролей в manifests, но executor `ruslan.yaml` permitted to fill
   все 5 simultaneously (multi-role binding flag).

3. **Risk: 6 true alphas vs 10 «alphas» communication.** Если v2
   reduces до 6, как объяснить в external positioning, что Invoice/
   SKU не alphas? Risk: outsiders не поймут. Recommend: внутренне 6
   alphas + 3 work products + 1 entity; externally говорить «10 core
   business objects, из них 6 lifecycle entities (alphas)».

4. **Creation graph 3-level structure vs operational simplicity.**
   Полный 3-level creation graph (operational/methodological/meta) =
   2-3 страницы Mermaid. Поддержка в Phase 1 — реалистично или
   over-engineered? Recommend: только Level 1 (operational) full в
   D6; Level 2-3 sketch с future-iteration commitment.

5. **«AI agent onboarding» как concept — стоит ли elevate в principle
   или leave как practical detail?** Левенчук МИМ-2026 explicit
   принцип. Recommend: yes, elevate в FPF-Lite §5 Internal Principles
   как 8-й principle: «Agents — new participants of master class.
   Onboarding required, not just prompt loading.»

6. **«What ШСМ is NOT» section — preserve как public artifact или
   keep internal?** Если eventually publishing FPF-Lite (Open Q6 в
   synthesis), эта section показывает intellectual honesty но также
   reveals self-doubt. Recommend: preserve internal-only, но keep
   spirit в operational guides.

7. **Mereology — full disclosure vs pragmatic silence.** Model D
   Nested IS mereological, но FPF-Lite tries to exclude mereology.
   Honest path: acknowledge lightweight mereology. Pragmatic path:
   silently use it without theory. Recommend: honest acknowledge —
   defends ШСМ from accusation of «using-without-understanding».

---

## Part 9 — Verdict

**Synthesis ШСМ-correct достаточно для Jetix L2 Cognitive? YES with changes.**

Synthesis показывает understanding ШСМ-фреймворка достаточно глубокое,
чтобы не fundamentally violate его. Pяtь примитивов всех присутствуют,
центральный thesis (framing/acceptance bottleneck) сохранён, division
labour между AI vs human (стратегирование = human only) защищён.

Однако три systemic dilution issues требуют v2 cleanup:

1. **Альфа vs Work Product confusion** — 3 of 10 «alphas» (Invoice,
   SKU, Postmortem) не являются alphas по Essence definition. Reduce
   до 6 true alphas + honest typing of work products / entities.
2. **Past-participle convention violated в ~52% состояний.** Systematic
   rename per audit table. Это не косметика — gerunds описывают process,
   а Essence state требует completed checklist.
3. **Graph of Creation degraded к bipartite supplier chart.** Узлы —
   артефакты вместо систем; mereology отсутствует. Add separate proper
   creation-graph artifact с 3-level mereological structure.

Дополнительные ontological cleanups (Part 7 list of 15) — none
fundamental, все executable за 4-8 часов работы над v2.

**Что Jetix получает при правильной applying ШСМ:**

L2 Cognitive layer становится не «декорация Левенчуком software
practices», а настоящий cognitive scaffold для AI-эпохи: framing
quality measurable (FPAR), role abstraction durable across model
upgrades, alpha lifecycle disciplines disciplined progress tracking,
creation graph navigable mega-corp complexity, strategizing protected
от ceremony degradation, writing-as-thinking protected от LLM-substitution.

**Что Jetix теряет если ne fix dilution issues:**

L2 становится «ШСМ-флёр поверх обычного software project management».
Через год Ruslan обнаружит, что 10 «alphas» работают как HubSpot
pipeline stages, role-manifests = job descriptions с YAML, strategizing
= monthly OKR planning, creation graph = Miro workflow diagram. ШСМ
тогда не extends framework, а decorates его — обратное от Левенчуковской
intention. Это violation by misuse, более dangerous чем violation by
omission.

**Recommendation for Stage 3 final synthesizer:** apply 15 changes из
Part 7 в v2 architecture. Защитить три core conventions: past-participle
states, Альфа/Work Product distinction, role-NOT-executor strict
separation в файловой структуре. Keep остальное — synthesis в целом
качественный и работоспособный.

---

**END OF LEVENCHUK / ШСМ EXPERT REVIEW**
