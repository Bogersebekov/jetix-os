---
title: ROY Alignment — baseline swarm parameters для Шага 2
date: 2026-04-22
status: approved-by-ruslan
type: alignment
supersedes: none
parent_notion: https://www.notion.so/34a2496333bf817d93bff4cb66775587
---

# ROY Alignment — утверждённые параметры baseline swarm

Фиксация alignment session Ruslan ↔ Cloud Cowork 2026-04-22 вечером. Выход для
Шага 2.1 (`MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM`) — без этих параметров
master synthesis не может быть написан.

---

## 1. Размер команды

**5 domain experts (base) + brigadier = 6 agents total.**

Не 9, не 10 как separate agents. 5 мёрджед мега-экспертов обладают
функциональным overlap с 9-expert handoff варианта, но без dilution.

---

## 2. Domain expertise — 5 merged experts

| Agent | Primary domain | Канонические первоисточники (Private Library) |
|---|---|---|
| **engineering-expert** | Compounding Engineering + clean code + unix + AI-native + architecture | Ousterhout (Philosophy of Software Design), Brooks (Mythical Man-Month), Fowler (Refactoring), Martin (Clean Code), Hunt/Thomas (Pragmatic Programmer), Karpathy, Boris Cherny, Anthropic engineering blogs, Aider, Cognition, 37signals, Shape Up, `compounding-engineering-2026-04-22/` R-1..R-11 + SYNTHESIS |
| **mgmt-expert** | Product Management + Project Management + management philosophy | Cagan (Inspired, Transformed), Torres (Continuous Discovery Habits), Grove (High Output Management, Only the Paranoid Survive), Laloux (Reinventing Organizations), Horowitz, Drucker (Effective Executive), 37signals ("It Doesn't Have to Be Crazy"), PMBOK, Shape Up, Netflix Culture, `phase-2-deep-research-2026-04-22/RESULT-05/06/07` |
| **systems-expert** | Systems thinking + cybernetics + complexity + biology/evolution | Meadows (Thinking in Systems), Senge (Fifth Discipline), Ashby (Introduction to Cybernetics), Beer (Brain of the Firm), Wiener (Cybernetics), Kelly (Out of Control), Dawkins (Selfish Gene, Blind Watchmaker), Dennett (Darwin's Dangerous Idea), Kauffman (At Home in the Universe), Mitchell (Complexity: A Guided Tour), Beinhocker (Origin of Wealth), Левенчук (3 deep research files) |
| **philosophy-expert** | Philosophy of science + mental models + stoic + epistemology + engineering foundations | Popper (Conjectures and Refutations, Logic of Scientific Discovery), Kuhn (Structure of Scientific Revolutions), Naval (Almanack), Stoics (Aurelius, Epictetus), Munger (Poor Charlie's Almanack), Farnam Street, SEP entries, Descartes (Discourse on the Method), Koen (Discussion of the Method), Vincenti (What Engineers Know), Altshuller (TRIZ) |
| **investor-expert** | Investing + value creation + capital allocation + long-term compounding | Buffett (Shareholder Letters Collection), Graham (Intelligent Investor), Marks (The Most Important Thing), Munger (Poor Charlie's Almanack), Taleb (Antifragile, Skin in the Game) |

**Brigadier** — отдельная роль вне matrix. Coordinator / task delegator /
synthesis manager. Orchestrates matrix invocations. Reads собственный
`brigadier.md` system prompt.

---

## 3. 🔑 UNIQUE JETIX PATTERN — Matrix agents (critical innovation)

**Это — ключевая дифференциация Jetix swarm от всех существующих multi-agent систем.**

### Концепция

Каждый domain expert может быть **invoked в одном из 4 role-modes**. Не либо
domain либо role — **обе оси одновременно**.

Competitors (Devin / Cora / Factory.ai / Sierra / etc.): либо domain-split
(engineer / PM / QA) либо role-split (critic / optimizer / integrator) —
never matrix.

Jetix: **matrix** = synergy.

### 4 role-modes (ortogonal axis)

| Role-mode | Функция |
|---|---|
| **Critic** | Ищет дыры / challenges assumptions / flags weakness / adversarial lens |
| **Optimizer** | Улучшает cost / complexity / elegance / removes unnecessary |
| **Integrator** | Синтезирует куски в coherent whole / finds unifying patterns |
| **Scalability-architect** | Phase 3 / $1T defense / anti-fragility / edge cases / long-term projections |

### Matrix — 5 domains × 4 role-modes = 20 possible invocations

Примеры концептуальных вызовов:
- `engineering-expert` as `critic` → технический критик архитектуры: ищет over-engineering, premature abstractions, fragile patterns
- `systems-expert` as `optimizer` → применяет cybernetic принципы (Ashby's requisite variety, Meadows leverage points) для упрощения design
- `philosophy-expert` as `integrator` → объединяет disparate куски через epistemic coherence (Popper falsifiability, Kuhn paradigm alignment)
- `investor-expert` as `scalability-architect` → capital allocation projections для Phase 3+, anti-fragility от Taleb, long-term compounding от Buffett
- `mgmt-expert` as `critic` → challenges PM roadmap через Cagan empowered-team lens, spotting process bloat (Shape Up minimalism)

### Implementation в system prompts

Каждый domain expert's system prompt содержит:
- **Primary section** (~800-1200 строк): domain expertise, canonical sources, primary frameworks, decision heuristics
- **Mode-switching section** (~300-500 строк × 4 modes): каждый role-mode как sub-prompt активирующийся при invocation parameter

Invocation pattern (pseudocode):
```
Task(
  agent: "systems-expert",
  mode: "critic" | "optimizer" | "integrator" | "scalability",
  context: {...}
)
```

Agent reads its base prompt + activates relevant mode section.

### Синергия — почему это работает

- Same deep domain knowledge в caждом mode → no dilution
- Role-mode provides **framing lens**, not separate knowledge base
- Можно запустить 4 experts в 1 mode (все critics) для parallel adversarial review — но из разных domain perspectives
- Можно запустить 1 expert в 4 modes (4 runs same agent) для deep single-domain analysis
- Можно комбинировать (systems-expert-critic + engineering-expert-optimizer) для complementary lenses

---

## 4. Operating modes — two regimes

### Full Auto
Рой работает автономно, Ruslan review'ит final output. Для:
- Smoke tests
- Simple well-defined scope tasks
- Validated patterns (после того как Stage-Gated прошёл несколько раз успешно)

### Stage-Gated
Рой останавливается на **key architectural decisions only** (не после каждого
output, не после каждой phase — только на critical long-term decisions). Для:
- Architecture synthesis
- Strategy decisions
- Anything с long-term consequences

**Pattern:**
1. Рой работает → достигает решения с long-term consequences
2. Пишет `decisions/AWAITING-APPROVAL-<topic>-<date>.md` (structured: context + options considered + recommendation + rationale + risk register)
3. Commits, pushes, pauses (can continue non-blocking work if any)
4. Ruslan review → approves / redirects / drills-down
5. Рой continues on approval signal

**Choice of mode = per-task decision.** Default для large architecture synthesis / first real roy launch = Stage-Gated.

---

## 5. System prompts granularity

**Maximal: 1500-3000 строк per agent.**

Deep, не скуповать. Каждый prompt = distillation of:
- Research canonical texts (compounding-engineering R-1..R-11, Phase 2 research)
- Primary sources (books из domain-specific Private Library subset)
- Role definition (mission, success criteria, failure modes)
- Mode-switching sections (critic / optimizer / integrator / scalability)
- Integration protocols (как output feeds back в wiki + brigadier synthesis)
- Examples (few-shot patterns для каждого mode)

---

## 6. Cost model

**Через Max subscription Claude** — НЕ API billing.

**Операционно:**
- `unset ANTHROPIC_API_KEY` перед каждым Claude Code launch на сервере
- Max plan 20× активна
- `--dangerously-skip-permissions` OK in tmux sessions
- Budget monitoring on per-turn / per-session basis via Max limits
- NO $47K-incident risk (API key unset)

---

## 7. Compute target

**Primary:** Claude Code на сервере (`ssh ruslan@100.99.156.28` → tmux).
**Model:** Opus 4.7 1M + extended thinking max.
**Branch:** `claude/jolly-margulis-915d34`.

**Secondary (Cloud Cowork):** этот чат — координация, промпт-генерация, review
assist. **NOT выполнение тяжёлых research / synthesis задач** (Ruslan's explicit feedback: Cloud Cowork = командный центр для server-side Claude Code).

---

## 8. Stage gates scope

**Only on key architectural decisions**, не после every output / phase.

**Triggers для gate:**
- Architectural decision с long-term consequences (>1 month impact)
- Trade-off между projects / resources / directions
- New framework / pattern proposal
- Addition / removal agent или skill
- Cost/budget escalation
- Conflict с existing 24 Locked decisions

**Non-triggers (рой continues without gate):**
- Research inventory
- Draft synthesis (не final)
- Cleanup / refactor existing artifacts
- Wiki entry creation
- Routine reviews

---

## 9. Первая задача для роя

**TBD — выбирается позже.**

После baseline setup + smoke test pass — Ruslan формулирует. НЕ fiksируется
сейчас (explicit instruction).

---

## 10. Что НЕ фиксируется сейчас (TBD в Шаге 2.1)

Эти параметры будут определены в `MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM`:

- Communication channels (wiki stigmergic only vs mailbox JSONL hybrid)
- Termination stack concrete implementation (maxTurns values, budget thresholds, verifier spec, HITL escalation trigger)
- Recursive iteration pattern (convergence detection, max passes, compound pattern)
- Exact smoke test design
- Skill roadmap finalization (какие CE skills в каком порядке)
- Hooks / monitoring (какие cc hooks нужны для visibility)
- Memory / wiki write protocol (single-writer serialization Phase 1 vs CRDT)

---

## 11. Approval

**Approved by Ruslan, 2026-04-22 evening.** Verbatim quote:

> «сделаем не так что вот либо оптимайзеры блять или там по конкретным темам
> — нет тогда блять давай идем сука делаем все 10, делаем все 10 но как то
> чтобы она вот работала с друг с другом … чтобы они могли каждый блять быть
> и критикам и оптимизатором и интегратором и так далее но при этом тоже
> самым сука глубоким образом чтобы мы могли как то вместе если что запустить
> например критика инженера либо там критика системного эксперта а потом
> взять этого системного эксперта и запустить как оптимайзера … это очень
> важно это тоже зафиксирует что у нас должна быть получиться синергия как
> раз между этими двумя направлениями … ну да можем как-то блять 5 тогда
> сделать в целом»

**Интерпретация:** 5 domain experts (не 10 separate), но **matrix 5×4 = 20
invocations** даёт synergy которую Ruslan требует. Это и есть "10+" через
matrix pattern, не через duplication.

---

## 12. Ссылки

- Parent Notion: [🤖 Шаг 2 — Настройка роя агентов самым лучшим образом](https://www.notion.so/34a2496333bf817d93bff4cb66775587)
- Grandparent Notion: [🔨 Создание метода разработки](https://www.notion.so/34a2496333bf810f9058fc783ce179e2)
- Great-grandparent Notion: [🧠 Глубокий Research + Рой Агентов + Рекурсивный Синтез](https://www.notion.so/34a2496333bf816fbddae3a9898c43a6)
- Information diet: `decisions/ROY-INFORMATION-DIET.md`
- 24 Locked decisions: `raw/research/architecture-variants-2026-04-22/TENSIONS-*.md`

---

## 13. Следующий шаг

**Шаг 2.1:** `MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-XX.md` — canonical
research-backed blueprint. Writes Claude Code на сервере (Opus 4.7 1M,
extended thinking max) через prompt созданный Cloud Cowork.

Inputs для master synthesis:
- Этот alignment doc (constraints)
- `raw/research/compounding-engineering-2026-04-22/` (11 R-files + SYNTHESIS)
- `raw/research/perplexity-market-ai-native-2026-04-22/`
- `raw/research/master-inventory-2026-04-22.md`
- `decisions/ROY-INFORMATION-DIET.md`
- Jetix Private Library 393 books (domain-filtered)
- All `design/*.md`
- All `decisions/JETIX-*.md` + 24 Locks
