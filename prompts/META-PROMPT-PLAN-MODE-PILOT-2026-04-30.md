# META-BRIEF: Plan Mode + ultrathink + Wiki Library Methodology — Pilot Design

**Run instruction:** copy from `## Кто я и кто ты` line below to the end of this file, paste в Claude Code session с включёнными Plan Mode (Shift+Tab×2) + Opus 4.7 [1m]. Слово `ultrathink` в тексте триггерит deeper reasoning.

---

## Кто я и кто ты

Я — Ruslan, основатель Jetix OS (Berlin). Phase 1 цель — €50K Q2 2026, horizon — $1T market cap. Solo founder + AI agents (12 legacy + 6 ROY swarm).

Ты — Claude Code в Plan Mode + ultrathink. На этот цикл ты **не пишешь код и не делаешь edit'ов**. Ты — **проектировщик методологии**.

## Что я хочу спроектировать

Мне нужен подход «Claude Code как небольшая адекватная экспертная команда»:

- Я даю **конкретный бизнес-кейс / вопрос / ситуацию** + полный контекст + данные
- Ты в Plan Mode + ultrathink проектируешь **глубокий пошаговый план решения**
- План **обязан опираться на релевантные источники из wiki + книги в `raw/books-md/`** + Foundation v1.0 + Workshop/TRM concepts — но **не на «всю library»**, а на **отобранные ~5-15 релевантных книг под конкретный кейс**. Selection criteria — часть deliverable.
- Каждое утверждение — с **provenance** (citation на конкретный source + line-range)
- Ищем **multi-perspective синтез**: 3-5 разных оптик (например: ШСМ Левенчука / Compounding Engineering / SRE / PM Cagan / Stoic) → конкуренция мнений → синтез
- Качество > generic. Inputs из реальной мудрости, не выдуманные best-practices

**Главный вопрос пилота:** работает ли это адекватно? Реально ли мы получим планы лучше чем без books-grounding? Стоит ли инвестировать в эту методологию дальше?

## Что от тебя сейчас (deliverable Plan Mode session)

Составь **PILOT-DESIGN PLAN** — план как нам этот подход проверить и внедрить. **Не решай реальный кейс.** Спроектируй methodology + roadmap pilot'а.

Конкретно нужно:

### 1. Spec методологии (как настраивать Plan Mode session под этот подход)
- Какой starting prompt-skeleton использовать (template для test cases)
- Какие документы pre-load в context (Foundation, wiki, конкретные книги)
- **Selection algorithm**: как под конкретный кейс выбирать ~5-15 релевантных книг из 402? (по topic-tags? embedding search? manual mapping book→domain?)
- Как заставить CC реально читать книги, а не bypass'ить (citations gate, F-G-R, provenance scanner)
- Token budget management для wiki+books inputs (1M context Opus 4.7 — это много, но не бесконечно)
- Когда использовать Opus 4.7 [1m] vs Sonnet 4.6
- Использование sub-agents (Explore / general-purpose) для batch-чтения отобранных книг

### 2. Document map
- Какие документы из repo + wiki + books **обязательно** в context для каждой category кейса
- Как навигировать `raw/books-md/` (402 файла) — нужен ли index/manifest? topic-tags? cluster mapping?
- Mapping: business case category → top-5-15 candidate book clusters

### 3. 20 testable гипотез
- Что мы проверяем этим пилотом? (не «работает ли», а конкретные claims)
- Каждая гипотеза falsifiable
- Каждая — с метрикой / signal'ом для validation
- Примеры направлений: provenance accuracy / multi-perspective synthesis quality / books-grounding vs generic baseline / selection algorithm quality / token efficiency / human-in-loop friction / specific failure modes / drift over long sessions

### 4. 5-10 test cases (pilot caseload)
- Реальные бизнес-кейсы для прогона
- Включи **classical consulting cases** (McKinsey/BCG/Bain interview style — market-sizing / profitability / market-entry / M&A) — для baseline benchmarking
- Включи **Jetix-specific кейсы** (TRM L0 sales test design / Tseren outreach risk-analysis / Mittelstand niche selection / etc.)
- Для каждого: input brief + expected difficulty + что хорошо проверяется + ожидаемый книжный pool

### 5. Метрики оценки
- Как мерить «adequacy» плана?
- Quantitative: provenance density / hypothesis count / actionability score / time-to-plan / source diversity (≥3 perspectives)
- Qualitative: Ruslan judgement rubric
- **Baseline тест:** тот же кейс **без** books-grounding (только generic Plan Mode) — для comparative analysis

### 6. Iteration roadmap
- Phase 1 (week 1): meta-design ack + first 2-3 test cases → calibrate selection algorithm
- Phase 2 (week 2-3): полный caseload → measurement → analysis
- Phase 3 (week 4): verdict (scale / pivot / drop) + если scale — integration в operational workflow

### 7. Risk register + mitigation
- Какие failure modes ожидаем?
- Confabulation books / token blow-up / drift / cherry-picking sources / books-overhead-not-worth-it / selection algorithm mis-fires
- Что делаем когда они проявятся?

## Hard rules

1. **ultrathink** — используй полный reasoning budget, не торопись
2. **Plan Mode** — **НЕ выполняй**, только план. Никаких edits / writes / runs.
3. **Provenance** — каждое утверждение с pointer'ом на source (file path + section + line-range). Если source не существует — flag explicitly, не confabulate.
4. **Russian** prose · English code/configs · мат preserve если в quotes
5. **AI = scribe для strategic decisions** — варианты + анализ + trade-offs, но НЕ диктуй strategic выводы. Sole strategist = я.
6. **No solo-founder downgrade** — baseline enterprise + $1T trajectory. Не предлагай «упрощённую версию для одного человека».
7. **Beta-first но enterprise-grade** — v1 достаточно-хороший, не перфекционизм
8. **НЕ multi-choice опросы** — если нужен мой input, **сформулируй конкретный question**, не давай 4 варианта-кнопки
9. **Provenance gate ≥0.95** — лучше написать «не нашёл в источниках» чем confabulate
10. **Token budget** — если inputs не помещаются, предложи batching strategy, не молчи
11. **~5-15 книг под кейс, не 402** — selection algorithm важнее чем coverage. Лучше 7 правильных источников чем 50 поверхностных.

## Inputs (pre-load в context)

**Concept layer (must-read):**
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — что такое Jetix
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` — business model
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — 35 use-cases + 11 constitutional rules

**Foundation layer (architecture):**
- `swarm/wiki/foundations/part-{1..11}-*/architecture.md` — 11 LOCKED Parts
- `swarm/wiki/foundations/principles/architecture.md` — Pillar C
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`

**Methodology layer:**
- `raw/articles/2026-04-29-claude-code-best-practices/ultrathink-claude-code.md`
- `raw/articles/2026-04-29-claude-code-best-practices/plan-mode-claude-code.md`
- `raw/articles/2026-04-29-claude-code-best-practices/README.md`

**Synthesis layer:**
- `swarm/wiki/synthesis/foundation-master-overview-{technical,human}-2026-04-29.md`

**Books library:**
- `raw/books-md/` — 402 книги (full library). Тебе нужно **построить index/manifest + selection algorithm** этой library как часть deliverable §2 (НЕ пытайся прочитать все 402 — это и есть проблема которую мы решаем).

**Memory layer:**
- `memory/MEMORY.md` + все файлы под ним — мои preferences, ограничения, прошлые решения

## Out of scope (НЕ делай это сейчас)

- Не решай реальный бизнес-кейс — это design pilot'а
- Не пиши код — Plan Mode
- Не делай edits — только план
- Не предлагай UI / dashboards / nice-to-have — minimum viable methodology
- Не дублируй существующее (Foundation / Workshop / TRM) — ссылайся
- Не пытайся прочитать все 402 книги — спроектируй selection algorithm

## Формат output'а

Структурированный markdown plan, готовый к ack от меня и переходу в execution. Sections matching §1-§7 выше + executive summary в начале (≤150 слов) + open questions to me в конце.

Если в каком-то блоке тебе не хватает context'а — flag explicitly с конкретным запросом «нужно X из файла Y» вместо guessing.

---

ready? Начинай ultrathink reasoning. Когда план готов — present для ревью.
