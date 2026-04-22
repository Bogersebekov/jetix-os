---
title: ROY Wiki v3 — Goals & Vision (Шаг 2.2.3 Стадия A)
date: 2026-04-23
status: vision-captured-from-ruslan
type: design-vision
parent_notion: https://www.notion.so/34a2496333bf81849f5fe7cc2666d68a
supersedes: none
---

# ROY WIKI v3 — GOALS & VISION

**Фиксация видения от Ruslan, 2026-04-23 вечер.** Это не finalized spec
архитектуры — это capture of goals, intent, and key decisions which
вместе формируют skeleton для того что Wiki v3 должна делать. На
основе этого документа дальше идут (a) mechanics discussion (Стадия B)
и (b) research-grounded architecture spec через Claude Code на сервере
(Стадия C).

## Meta-principle

> «Википедия должна быть на 1000% глубоко проработанной, настолько
> качественной, умной, инсайтной, интересной насколько это возможно,
> и реально помогать разработке, улучшать её.»
>
> «Мы просто разрабатываем новый вид памяти для агентов, просто
> улучшенную версию их коммуникации.»

**Wiki v3 = самый важный компонент всей системы.** Без неё swarm не
может координироваться, накапливать уроки, или улучшать себя. Это не
storage — это central cognitive infrastructure.

---

## 1. Главные идеи от Ruslan — narrative walkthrough

### 1.1 «Одна Wiki или несколько Wikis с переключением»

Ruslan flags an open design question: архитектура может быть
(a) одна монолитная Wiki, разделённая по слоям/темам внутри, или
(b) несколько отдельных Wikis с возможностью переключаться между
ними, соединять, вытягивать слои. Открытая дверь на дизайн multiple
wiki layers that can be composed, switched, or fused.

**Интерпретация:** multi-wiki layered architecture, где каждый слой
имеет свою специализацию, но все они queryable и combinable. Это не
много изолированных KB — это **one semantic space, layered into
addressable subviews.**

### 1.2 Brigadier имеет свою Wiki (Idea 1)

> «Для бригадира сделать отдельную Википедию. Чтобы он не в контексте
> у себя всё вёл, а заносил в Wiki: как улучшить этого чувака, как
> блять можно эту задачу решить, как возможно эту задачу решить.»

Brigadier не держит всю координационную логику в своём system prompt
context window. Вместо этого — всё wrapping в Wiki:

- Как улучшить конкретного expert'а (observed behavioural notes + fix ideas)
- Как можно решать данный class of tasks (multiple approaches + tradeoffs)
- Possible solution space для текущей задачи (enumerated before choosing)

**Rationale (implicit):** context window = scarce; wiki = persistent
cheap lookup. Offloading orchestration state to wiki → brigadier can
scale across many tasks without context bankruptcy.

### 1.3 Brigadier «жрёт книги» → создаёт Wiki on how to solve problems (Idea 2)

> «Этому же бригадиру в эту же википедию занести например какие-то
> основные... скормить в него несколько книжек пусть он на этих книжках
> создаёт википедию. Задание — не просто эти книжки сожрал, а создать
> максимально охуенную и удобную википедию, чтобы потом этот же или
> другой бригадир мог её открывать и соответственно исправить при
> решении разных задач он к ней обращался.»

- Brigadier reads curated books (e.g. PMBOK, High Output Management,
  Shape Up, Cagan, Grove, Laloux, и т.д.)
- Not just reads — **constructs Wiki content on:** how to manage
  projects, how to solve problems, how to orchestrate, how to decide
- Wiki becomes reference for future brigadier invocations

> «Чтобы не от пизды блять придумывал и так далее, а именно шёл
> википедию гнида блять читал, там какие-то основные варианты как
> можно управлять, как можно решать конкретно эту задачу, как возможно
> эту и так дальше, и соответственно с сверивался с википедией и
> потом уже шёл блять давать задание дальше этим работягам.»

**Key insight:** Wiki contains **enumerated options + methods** —
brigadier consults it as a "how to do X" library before choosing
approach. Not creative-from-scratch — grounded-in-best-practice-then-pick.

### 1.4 Per-agent Wikis — "mega-skill" (Idea 3)

> «Похожая Википедия потом будет под каждого мини-агентом в какой-то
> степени. Или же бригадир будет знать где что находится, а потом
> просто агенту говорить — ага, ты там иди блять еще это изучи или
> получи контекст отсюда или блять отсюда.»

Two sub-variants flagged:

- **A.** Each expert has **own Wiki**, domain-specific
- **B.** Brigadier maintains pointer-map: «engineering-expert → iди
  читать этот wiki section; systems-expert → iди сюда»

Either way — agents gain **mega-skill через Wiki access:**

> «То есть не просто ебаные скиллы, а именно вот Википедия должна
> позволить ещё мега-скилл им дать. Чтобы они были умными, чтобы они
> не забывали.»

Wiki = beyond ad-hoc skills — it's how agents become durably smart
and retain lessons across sessions.

### 1.5 Theme Wikis — per-domain baseline (Idea 4)

> «Википедия должна быть ещё по темам, как мне кажется, под основные
> — там блять инженер, там инвестор и так далее. Чтобы они уже тоже
> принимали решение на основе там каких-то адекватных данных из книг
> которые мы отметим хорошими, а не просто прям рандомно.»

Theme-wikis aligned с 5 domain experts:

- `engineering/` — distilled from Ousterhout, Brooks, Fowler, Hunt/Thomas, Raymond, Boris Cherny, Shape Up, Karpathy, Anthropic eng blog
- `management/` — distilled from Cagan, Grove, Laloux, Drucker, Horowitz, Netflix culture, 37signals, Torres
- `systems/` — distilled from Meadows, Senge, Ashby, Beer, Wiener, Kelly, Kauffman, Mitchell, Dawkins
- `philosophy/` — distilled from Popper, Kuhn, Lakatos, Naval, Stoics, Munger, Koen, Vincenti
- `investing/` — distilled from Buffett, Graham, Marks, Taleb, Fisher, Poundstone

Function: each expert **consults its theme-wiki as adequate ground
truth** для decision-making, instead of hallucinating from generic
training data.

### 1.6 Agent-improvement Wiki layer (Idea 5) ⭐

> «В этой Википедии было наверное отдельно как-то ещё блять слой под
> улучшение самих агентов. Да, чтобы они тоже не только куда-то в
> себя блять все это записывали, а возможно в Википедию. И тогда
> если вот вытянуть этот слой "как улучшать агентов" в Википедию —
> они сразу в агентов давать. То возможно у нас получится ну как-то
> больше инсайтов словить или же как-то благодаря их совместной работе
> какие-то там новые блять открытия для агентов для скилов и так
> далее сделать.»

**Critical insight:** there's a **separate wiki layer specifically
for "how to improve agents themselves."** Not mixed with task-solving
content. Dedicated meta-layer.

Why separate:
- Meta-improvement insights должны быть shared (not buried in per-agent
  strategies.md where only that agent sees them)
- Agents can **collaborate on improving each other** через this layer
- Cross-agent pattern discovery (e.g., engineering-expert notices
  systems-expert has same anti-pattern → writes improvement note)
- Brigadier can periodically sweep this layer → apply improvements

**This is new** — not in master synthesis. Key decision to lock.

### 1.7 Crazy-agent для Wiki (Future idea, Phase B+)

> «Еще должна быть как-то возможность генерировать инсайты. То есть
> отдельно у нас будет ещё какой-то блять агент — crazy-agent по
> Википедии. Но это уже на потом. Просто чтобы ты имел в виду —
> чтобы он там блять с разных тем берёт их просто там скрещивает,
> возможно что-то новое интересное получится.»

Future:
- Dedicated **insights-generation agent** ("crazy-agent" per existing
  Jetix archetype naming)
- Takes entries from different theme-wikis + domain-expert strategies +
  cross-pollinates them
- Produces candidate novel insights (may be garbage, may be gold)
- Output candidates → reviewed by experts в critic mode → accepted
  insights promoted

**Deferred to Phase B+.** Flagged now to avoid structural choices that
preclude it.

### 1.8 Wiki под задачу — task-scoped assembly (Idea 6, already captured)

> «Википедия должна быть как бы отдельно под задачу.»

Already discussed 2026-04-23 earlier + зафиксирован в
`design/ROY-BUILD-LOGIC-2026-04-23.md` §4. Carried forward as decided.

Added nuance сегодня:

> «С одной стороны — Википедия по решению задачи. С другой стороны —
> одна папка или ещё какой-то слой именно операционного управления
> всеми этими агентами.»

**Two parallel layers per task:**
- Layer α — **Task-scoped knowledge Wiki** (how-to-solve content,
  domain references, decisions)
- Layer β — **Operational Wiki** (project management, agent activity
  log, iteration history, rollback points)

These are different concerns не должны быть фmerged. Task-knowledge
Wiki answers «how do I solve this»; Operational Wiki answers «what
happened, when, by whom, can we rollback».

### 1.9 Long-project logging + iterations + rollback (Idea 7) ⭐

> «Если они будут работать как-то над каким-то длинным проектом,
> какой-то длинной задачей — чтобы они тоже вот всё как-то логали,
> будь то в Википедии, будь то в этом документе, или в этой папке.
> Чтобы у нас как бы тоже всё шло этими итерациями, да, и мы если
> что могли от какой-то этой блять итерации по сути отойти назад и
> пробовать несколько вариантов.»

Long-horizon tasks:
- All agent activity logged persistently (wiki or operational folder)
- Structured as **iterations** (v1, v2, v3...)
- Every iteration = checkpoint — can be rolled back to
- Can branch/fork и try multiple variants in parallel

> «На гитхабе там отдельно как-то блять ветку создадим, да, и допустим
> будем там тестировать. Они там сделали версию продукта блять один —
> соответственно мы её там зафиксировали и возможно пошли дальше, или
> там какую-то другую блять или там форкнули блять ещё что-то.»

**Primary version-control mechanism = git branches.** Per-iteration
branch + ability to fork. Not a novel versioning system — leverage git.

> «Как раз за счёт этой возможности у нас должна появиться скорость
> — скорость более много версий создавать, их быстрее тестировать и
> так далее.»

**Purpose of version control:** speed of parallel exploration, не
careful-single-path. Many variants explored fast, best selected.

### 1.10 Meta-level Compounding Engineering (Idea 8) ⭐⭐⭐

> «Эти агенты внутри себя работают вот по этому методу compound
> engineers, и они как бы улучшаются и плюс еще ведут какие-то свои
> там записи. А потом у нас еще и бригадир — ну и не просто бригадир
> а вся система в целом должна будет точно так же по этому compound
> engineers работать и точно так же себя как-то улучшать на мета
> уровне. То есть вся их блять коммуникации так дальше тоже должны
> будут улучшаться.»

**Two levels of Compound Engineering:**

- **Level 1 — Per-agent CE** (already in master synthesis §2.1.1):
  Plan-Work-Review-Compound loop внутри caждого cell. Cycle учит 1-2
  rules → strategies.md. Individual agent improves.

- **Level 2 — System-level CE** ⭐ NEW: brigadier + communication
  protocols + orchestration mechanics themselves follow CE loop.
  System overall improves over time, not just agents individually.

**Implication:** brigadier не только orchestrates Level 1 CE для
cells — brigadier himself runs a meta-level Plan-Work-Review-Compound
loop on system operation. After N cycles, brigadier notes:
- «Decomposition pattern X failed 3 times — switch to Y»
- «Parallel invocation of 5 cells hits context-budget issues —
  cap at 3»
- «Gate trigger heuristic needs recalibration»

These meta-improvements → separate wiki layer (see 1.6
agent-improvement).

**This is the closed loop:** system improves system improves system.
Recursive self-improvement не only at knowledge level, но at
coordination level.

### 1.11 Skill learning layer (Idea 9)

> «Еще раз блять — скилы им тоже внедрять максимально глубоко и
> качественно. И потом чтобы они ну вот по такому уже подходу блять
> Левенчук плюс вот это вот логирование плюс возможность откатиться
> к этой там старой версии плюс блять Википедия вот глубокая
> проработанная на блять 500 процентов — они должны работать.»

Wiki has dedicated layer для:
- **Potential skills** — candidates identified during operation, waiting
  for formalization
- **Active skills** — per-agent skill registry, referenced in system
  prompts
- **Skill learning protocol** — as new skills emerge from Compound step,
  they're not just added ad-hoc; they're properly introduced into
  agents (training, golden-set population, eval pass, then activation)
- **Skill usage patterns** — which agent + mode uses which skill when

Purpose: skills deeply internalized, not loosely attached.

### 1.12 Standard workflow integrated

Финальная формула workflow (Ruslan's quote paraphrased):

```
standard workflow = Левенчук FPF
                  + версионное логирование + rollback
                  + глубокая Wiki (проработана на 500%)
                  + Level 1 + Level 2 Compound Engineering
```

Это баseline для **every piece of work** swarm does. Не заадhoc. Не
«шустренько набросать». **Глубоко, ответственно, качественно, с первого
шага**, «чтобы у нас потом не было ебаных спагетти».

---

## 2. Wiki v3 multi-layer architecture — hypothesized structure

На основе идей выше, Wiki v3 likely выглядит так (к уточнению в
Стадии B):

### Layer 1 — Theme Wikis (5 штук, per domain)
Per-domain distilled knowledge from curated books.
- `swarm/wiki/themes/engineering/`
- `swarm/wiki/themes/management/`
- `swarm/wiki/themes/systems/`
- `swarm/wiki/themes/philosophy/`
- `swarm/wiki/themes/investing/`

Each contains: concepts, canonical methods, key heuristics, anti-patterns,
citations back to source books (in `raw/books-md/`).

### Layer 2 — Brigadier's Wiki
Brigadier-specific knowledge for orchestration.
- `swarm/wiki/brigadier/`
  - `how-to-solve-problems/` (from books: Shape Up cycles, OKR, PMBOK,
    Grove's paired-indicator, Laloux teal, etc.)
  - `how-to-manage-agents/` (heuristics for orchestration)
  - `how-to-decompose-tasks/` (task-shape → cell selection patterns)
  - `orchestration-state/` (offloaded state per active task)

### Layer 3 — Per-agent Wikis (5 experts)
Each expert's own working wiki.
- `swarm/wiki/agents/engineering-expert/`
- `swarm/wiki/agents/mgmt-expert/`
- ...
- Contains: domain scratchwork, ongoing hypotheses, cross-refs to theme
  wiki, strategies.md (rolling rules)

### Layer 4 — Agent-improvement Wiki ⭐ (meta-layer, shared)
Cross-agent observations and improvement proposals.
- `swarm/wiki/meta/agent-improvements/`
  - `engineering-expert-improvements.md` (observations + fix candidates)
  - `systems-expert-improvements.md`
  - ... (one per agent)
  - `system-level-improvements.md` (orchestration, protocols, hooks)
  - `emergent-insights.md` (cross-agent pattern discoveries)

**Brigadier sweeps this layer periodically** → applies accepted
improvements via system prompt edits.

### Layer 5 — Task-scoped Wikis ⭐
Per-task ephemeral Wiki (already per build logic §4).
- `swarm/wiki/tasks/<task-id>/`
  - `context/` — domain-filtered baseline
  - `artefacts/` — expert outputs
  - `decisions/` — brigadier decisions
  - `open-questions.md`

### Layer 6 — Operational Wiki ⭐ NEW (long-project logging)
Per long-horizon project — logs, iterations, rollback points.
- `swarm/wiki/operations/<project-id>/`
  - `iterations/v1/`, `/v2/`, `/v3/` ...
  - `decisions-log.md` (chronological)
  - `rollback-points.md` (named checkpoints + git-SHA refs)
  - `forks.md` (parallel variants tracked)

Git branches per project:
- `roy/<project-id>/main`
- `roy/<project-id>/iter-v1`, `iter-v2`, `iter-v3`
- `roy/<project-id>/fork-<variant>`

### Layer 7 — Global accumulated learnings
Post-task: promoted rules, solved-problem patterns, confirmed anti-patterns.
- `swarm/wiki/global/`
  - `solved-patterns/` — solved problem templates
  - `confirmed-anti-patterns/` — production-validated APs
  - `compound-rules/` — rules promoted from individual strategies

### Layer 8 — Skill wiki
Skills registry + learning protocol.
- `swarm/wiki/skills/`
  - `active/` — deployed skills
  - `candidates/` — potential skills awaiting formalization
  - `learning/` — skill introduction protocols (golden-set, eval, activation)
  - `usage/` — observed usage patterns per agent × mode

### Layer 9 — Insights playground (Future, Phase B+)
Crazy-agent domain.
- `swarm/wiki/insights/`
  - `candidates/` — cross-pollinated candidate insights
  - `reviewed/` — critic-reviewed insights
  - `promoted/` — accepted insights (moved to global)

---

## 3. Ключевые решения — LOCKED

Фиксация принципиальных решений, которые влияют на все дальнейшие
этапы. Не менять без re-approval.

### Decision W-1 — Multi-layer architecture (not monolithic)
Wiki v3 = **multiple specialized layers** co-located under
`swarm/wiki/` with defined boundaries + cross-referencing. Not one
flat KB.

### Decision W-2 — Brigadier has own Wiki
Brigadier's Layer 2 (own Wiki) is mandatory — not optional. Offloads
orchestration state from context window to persistent store.

### Decision W-3 — Books → Wiki distillation via brigadier (seed) + experts (Phase B ongoing)
Initial seeding of theme-wikis = brigadier reads curated books, distills
to wiki content. Phase B: experts read their domain-specific books,
further deepen theme-wikis.

### Decision W-4 — Agent-improvement Wiki is separate dedicated layer
Meta-improvement не mixed with task content. Dedicated Layer 4 shared
between all agents.

### Decision W-5 — Two-level Compounding Engineering
- Level 1: per-agent CE (master synthesis §2.1.1)
- Level 2: system-level CE (brigadier + protocols improve themselves)
Both layers mandatory. Brigadier Level-2 CE output goes to Layer 4
(agent-improvement Wiki).

### Decision W-6 — Long-horizon projects use git branches for versions
Version control mechanism = native git branches. Per iteration branch.
Fork for variants. Rollback via git checkout to named branch.

### Decision W-7 — Two parallel task layers
Per task:
- Layer α — Task-knowledge Wiki (what to do, how to do it)
- Layer β — Operational Wiki (activity log, iteration history, rollback)
Кept separate, not fused.

### Decision W-8 — Workflow standard = FPF + versioning + deep Wiki + 2-level CE
Every swarm work follows this standard. Not shortcut-able. No shallow
«just ship it».

### Decision W-9 — Skill learning as first-class wiki layer
Skills не loosely attached — properly learned (candidate → eval →
golden-set → activation). Dedicated Layer 8.

### Decision W-10 — Crazy-agent / insights generation deferred
Future feature, Phase B+. Layer 9 placeholder prepared but not
instantiated in Phase A.

### Decision W-11 — Wiki is central cognitive infrastructure, not storage
Wiki = «a new kind of memory for AI agents». Central coordination,
communication, and improvement layer. Treated accordingly — cannot be
skimpy.

### Decision W-12 — 1000% depth requirement
«Википедия должна быть на 1000% глубоко проработана.» This sets the
quality bar: не 100%, не adequate-enough. Deep-deep-deep. Every page,
every cross-reference, every provenance tag. This affects Стадия C
prompt — CC must be instructed to not settle for surface.

---

## 4. What we're really building

Wiki v3 is not a wiki in traditional sense. It is **a new species of
memory architecture for multi-agent AI systems.** It integrates:

- **Individual memory** (per-agent strategies + scratchpads)
- **Collective memory** (global accumulated learnings)
- **Theme-expert memory** (domain canonical methods + heuristics)
- **Orchestration memory** (brigadier's offloaded state)
- **Meta-memory** (how to improve the system itself)
- **Episodic memory** (task-scoped + operational logs)
- **Creative memory** (insights candidates from cross-pollination)
- **Skill memory** (learned capabilities registry)

All under provenance tracking, access control, rot prevention, and
version discipline. All mutually cross-referencing. All queryable by
the agents that operate on them.

**No public production system has this architecture.** CrewAI doesn't.
Devin doesn't. Every/Cora doesn't. Letta/Mem0 touch parts. Karpathy's
LLM Wiki is a small slice of this vision.

This is a **Jetix-specific innovation on the scale of matrix 5×4.**
If matrix 5×4 is «how agents think», Wiki v3 is «how they remember,
communicate, and improve together».

---

## 5. Open design questions для Стадии B (mechanics)

Эти вопросы **не решены** сегодня. Будут решены в следующих sessions:

- **Retrieval mechanism primary:** filesystem grep / semantic embeddings /
  graph traversal / HippoRAG PPR — какой default для агентов?
- **Write serialization:** single-writer (brigadier) vs per-layer owners —
  scales ли single-writer при увеличении layers?
- **Layer-to-layer cross-references:** typed edges в graph.jsonl или
  markdown wikilinks? HippoRAG style или Obsidian style?
- **Task-scoped Wiki context population:** автоматически из tags /
  keywords / domain-expert lists / brigadier manual / hybrid?
- **Rot detection signals:** time / version / contradiction / manual tag /
  combination?
- **Skill learning pipeline concrete:** candidate → draft → eval →
  golden-set → activation — где формально описать, кто отвечает?
- **Git branches naming conventions:** `roy/<task>/iter-vN` / `roy/fork/X` —
  окончательная схема
- **Insights layer (Layer 9) Phase B trigger:** когда activate crazy-agent?
- **Existing `wiki/` top-level v2 vs new `swarm/wiki/` v3:** migrate / coexist /
  merge?

Все эти решения — Стадия B (следующая итерация).

---

## 6. Next step — Стадия B (mechanics discussion)

После approval этого GOALS doc — переходим к mechanics. Вопрос-за-вопросом
решаем 9 open design questions (§5). Потом Стадия C — пишем prompt для
Claude Code, который создаёт full architecture spec с research grounding.

---

## 7. Approval

Approved by Ruslan, 2026-04-23 вечер. Verbatim key quotes captured в
секциях 1.1-1.12 выше.

---

## 8. Ссылки

- Parent Notion: [📚 Wiki v3 Spec](https://www.notion.so/34a2496333bf81849f5fe7cc2666d68a)
- Grand-parent: [🏗️ Шаг 2.2 — Логика построения](https://www.notion.so/34a2496333bf81d1b5b6eeb9819eedd2)
- Great-grand-parent: [🤖 Шаг 2 — Настройка роя](https://www.notion.so/34a2496333bf817d93bff4cb66775587)
- Upstream design docs:
  - `design/ROY-BUILD-LOGIC-2026-04-23.md` (где файлы лежат)
  - `decisions/ROY-ALIGNMENT-2026-04-22.md` (base params)
  - `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (blueprint)
- Research inputs (Стадия C primary):
  - `raw/research/knowledge-architecture-deep-research-2026-04-19.md` (828 lines — main)
  - `raw/articles/karpathy-llm-wiki-gist-2026-04.md`
  - Existing `wiki/` v2 infrastructure (templates, graph, skills)
