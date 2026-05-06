---
title: JETIX Foundation Build — Master Plan Brief (для ROY swarm cycles)
date: 2026-04-27
type: master-plan-brief
sub_stage: 1.3 of Этап 1 (Architecture) of Генеральная чистка
purpose: Specification + working document для построения реальной working architecture системы Jetix из LOCKED FUNDAMENTAL Vision. ROY swarm cycle(s) выполняют работу per этот brief. Этот документ = navigation map / progress tracker / quality discipline.
scope: ТОЛЬКО Foundation (FUNDAMENTAL Layer 1). RUSLAN-LAYER (Layer 2) — отложен до закрытия Foundation. Roy-replication / fork-and-merge для других потенциальных users — также после Foundation closed.
status: SPEC v1.0 — ready для ROY launch
parent_notion: https://www.notion.so/34e2496333bf816cb421c263beec172f
foundation_doc: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (LOCKED v1.0)
audit_doc: decisions/AUDIT-CURRENT-STATE-2026-04-27.md
status: archived
archived_at: 2026-05-06
archived_reason: Pre-Foundation snapshot — superseded
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# JETIX Foundation Build — Master Plan Brief

## §0 Что это за документ

Это **navigation document + work specification** для построения реальной working architecture системы Jetix Foundation на основе LOCKED FUNDAMENTAL Vision v1.0.

**Этот brief — НЕ сама архитектура.** Он определяет:
- Что мы строим (точка Б)
- Откуда стартуем (точка А)
- Какие sub-этапы work
- По каким принципам работаем (quality / best practices / discipline)
- Как ROY swarm executes work
- Как контролируем quality / integration

**Реальная архитектура** будет написана ROY swarm в multiple cycles per этот brief.

**Living document:** обновляется по мере progress (status per sub-этап / completion / blockers).

---

## §1 Точка А — что есть НА СТАРТЕ (27.04 evening)

### Foundation документы LOCKED:
- ✅ **JETIX VISION FUNDAMENTAL v1.0** (`decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`) — 24K слов, 12 категорий use cases, two-axis evolution, anti-scope ~50 hard rules, 5-tier access, 11 archetypes
- ✅ **AUDIT current state** (`decisions/AUDIT-CURRENT-STATE-2026-04-27.md`) — 5758 слов, 12 subagents inventoried system
- ✅ **JETIX FPF** (3758 строк, constitutional first-principles framework — Левенчук IP-1 база)
- ✅ **JETIX SYSTEM OVERVIEW** (1421 строка, 14-layer system map — existing architecture description)

### Существующие constitutional reference docs:
- D1-D29 Locks + 4 LOCKS-ADDENDUM
- 6 Strategic Insights (AI-BIOS / VISION-NEXT / MA / Arbitrage / AI-Psy-Led / Top Lists)
- D2 Philosophy (Левенчук integration / architect-orbit / engineering-faith)
- D4 Architecture-Brief (high-level patterns)

### Library / Research base (на сервере):
- `raw/research/` — multiple research dumps (architecture variants / agency / community / consulting / company-as-code / CRM / folder structure / holding / etc 18-19.04 deep research)
- `swarm/wiki/cycles/` — cycles 1-11 outcomes (accumulated patterns)
- Wiki concepts (6 ingested 26.04 + earlier)
- External resources: книжки на сервере по системному мышлению / менеджменту (path TBD ROY discovery)

### Working tools:
- ROY swarm (6 ROY agents + 14 legacy)
- voice-pipeline на CC headless (cycle 11 done)
- CRM cycle 10 (working CRM с 10 skills)
- Git-based Company-as-Code

---

## §2 Точка Б — что должно быть в КОНЦЕ Sub-stage 1.3+

### Главный outcome:

> **Гениально описанная и разобранная working система Jetix Foundation на лучших наработках из всех доступных best practices (Левенчук + системное мышление + менеджмент + multi-agent + observability / etc), без противоречий, готовая к реальному использованию на практике.**

### Конкретные deliverables:

**1. Master Architecture Document** (top-level)
- File: `decisions/JETIX-FOUNDATION-ARCHITECTURE-2026-04-27.md` (или похожий)
- Structured breakdown системы на main parts
- How parts work together (interfaces / dependencies / data flows)
- Constitutional alignment с FUNDAMENTAL Vision §0-§9
- Cross-references на per-part deep dives

**2. Per-part deep architectural documents** (один per main part системы)
- Files: `decisions/JETIX-FOUNDATION-PART-<name>-2026-04-27.md`
- For each main system part:
  - Что это (concept + boundary)
  - How это работает (mechanics / patterns / data structures)
  - Best practices integrated (с источниками — какая книжка / framework / research)
  - Implementation notes (что real, что aspirational)
  - Anti-patterns (что НЕ делает)
  - Cross-refs к other parts
  - Working examples / templates

**3. Integration document**
- File: `decisions/JETIX-FOUNDATION-INTEGRATION-2026-04-27.md`
- How всё связано in coherent whole
- Cross-cutting concerns (security / observability / Левенчук discipline / governance)
- Data flow integration
- Failure mode integration (что happens когда part X breaks)
- No contradictions verified

**4. Practical use instructions**
- File: `decisions/JETIX-FOUNDATION-USAGE-GUIDE-2026-04-27.md`
- "Как использовать эту систему" practical
- Onboarding pattern (Day 0 → Day 30 progression)
- Common workflows
- Troubleshooting basics

**5. Best practices integration manifest**
- File: `decisions/BEST-PRACTICES-INTEGRATION-MANIFEST-2026-04-27.md`
- List ВСЕХ external best practices use'нных
- Per practice: source / how integrated / where applied / verification
- "Provenance" for каждой архитектурной idea

**6. Updated CLAUDE.md root**
- Reference на FOUNDATION-ARCHITECTURE
- Quick navigation map к per-part documents

### Quality criteria:

- ✅ **Без противоречий** — между parts / с FUNDAMENTAL Vision / с FPF / с Locks
- ✅ **Best practices integrated** (не просто referenced — реально использованы в design)
- ✅ **Действительно работающее описание** (можно использовать на практике, не theoretical)
- ✅ **Левенчук discipline** preserved (constitutional limits / architect-orbit / agency-preservation)
- ✅ **Generic** (Foundation Layer — sector-agnostic, не Ruslan-specific)
- ✅ **Tested / verified** (где applicable — claims проверены через cross-reference / smoke test / etc)

---

## §3 Process — sub-этапы work

### Sub-этап 1.3.A — Master Plan Synthesis (cycle 12 wave A)

**Что ROY делает:**

1. Read FUNDAMENTAL v1.0 полностью (24K слов)
2. Read AUDIT current state полностью
3. Read FPF (skim 3758 строк, identify constitutional constraints)
4. Read SYSTEM-OVERVIEW (1421 строки, existing 14-layer description)
5. **Identify main parts of системы** — что должно быть discrete components в Foundation:
   - Может быть mapping на FUNDAMENTAL Vision 12 categories (но не obligatorily 1:1)
   - Может включать cross-cutting concerns как separate "parts"
   - Goal: tree-structure разбивки системы на manageable components
6. **Define interfaces между parts** (что один part exposes, что другой consumes)
7. **Initial dependency graph** (acyclic ideally; loops surfaced для resolution)
8. **Tree-structure document** = Master Architecture Document (deliverable §2.1)
9. **List sub-parts которые требуют deep work в Sub-этапе 1.3.C** (sub-этап 1.3.B = library research, parallel)

**Output:** Master Architecture Document + list of per-part work needed.

**ETA:** 2-3 часа ROY swarm (multiple subagents reading + synthesizing).

### Sub-этап 1.3.B — Library / Best Practices Research (cycle 12 wave B, parallel с 1.3.A possibly)

**ВАЖНО:** Per §4.5 critical constraint — **library на сервере primary, web research только supplementary**. Internal "consultant" agents create на основе **полного framework foundation study**, не surface-level summaries.

**Что ROY делает:**

1. **Discover library** (thorough — multiple search patterns):
   - `raw/research/*` (already known existing)
   - `~/jetix-os/raw/sources/` если есть
   - `~/Documents/` / `~/Library/` / `~/Books/` — anywhere PDF/EPUB stored на сервере
   - Find / locate / grep по common book filenames + canonical author names
   - Любые другие research / book extracts в repo / на disk
2. **Catalog best practices sources** which relevant к Foundation architecture:
   - **Левенчук ШСМ материалы** — full books / lectures / methodology если available
   - **Системное мышление books** (Senge / Meadows / Sterman / etc)
   - **Менеджмент frameworks** (Drucker / Lean / TOC / Kanban / Agile)
   - **Multi-agent patterns** (LangGraph / CrewAI papers / FrameStack)
   - **Event sourcing / CQRS** (Kleppmann / Fowler)
   - **Observability / SRE** (Google SRE / Honeycomb)
   - **Knowledge management** (Karpathy / Matuschak / Luhmann)
   - **AI safety / alignment** (Anthropic Constitutional AI / etc)
   - Любые другие relevant в library
3. **Per source detailed assessment:** не "brief" — а **deep read** key foundational frameworks (per §4.5 — consultant pattern). Marginal frameworks — brief reference OK.
4. **Build "consultants" per major framework** — internal expert agents ROY can consult:
   - **"Levenchuk consultant"** — прочитал ВСЮ Левенчук foundation (не пара статей); applies discipline rules с deep understanding
   - **"Systems thinking consultant"** — прочитал full systems thinking literature; applies systems perspective
   - **"Multi-agent architecture consultant"** — прочитал foundational multi-agent papers; applies patterns
   - **"Reliability consultant"** — прочитал SRE Book + event sourcing literature; applies disciplined patterns
   - **"KM consultant"** — прочитал KM frameworks (Luhmann / Matuschak / etc); applies methodology
   - etc per dominant frameworks identified
   - **Each consultant has documented foundation** (что прочитан) для transparency
5. **Web research только supplementary** — если library не покрывает framework, max 5 sources external (focused on canonical introductions / authoritative summaries) + flag в output что shallower coverage.

**Output:** Best Practices Integration Manifest (deliverable §2.5) draft + library inventory (с file paths) + consultant role definitions (с foundation read documented).

**ETA:** 2-3 часа ROY swarm (parallel с 1.3.A possibly, или sequential — ROY decides). Library discovery — отдельный effort если deep.

### Sub-этап 1.3.C — Per-part Deep Work (cycle 12 waves C+, sequential per part)

**For EACH main part identified in 1.3.A:**

**Pattern (per part):**

1. **Brief specific part scope** (что именно строим в этом sub-этапе)
2. **Consult relevant frameworks** (use консультантов из 1.3.B) — what best practices apply specifically к этой part
3. **Library deep dive** — read specific books / research relevant к этой part
4. **Synthesis cycle:**
   - Initial draft architecture для этой part (using best practices)
   - Internal review (consistency / Левенчук / anti-scope)
   - Refinement
   - Test against scenarios (как часть will work in real situations)
   - Iterate если нужно
5. **Document:** per-part architectural document (deliverable §2.2)
6. **Cross-refs added** — как эта part связана с уже built parts
7. **Strategy learning saved** — что worked / что не worked → ROY `strategies.md` updated

**Принципы для per-part work:**

- **На 1000% глубоко** — не "достаточно", а лучшее что можно сделать с available knowledge
- **Best practices REALLY integrated** — не "Левенчук говорит X, поэтому мы делаем X" формально, а **деeply applied**: как это конкретно работает в этой part, какие edge cases, какие trade-offs
- **Multiple iterations OK** — если первый draft не quality, refine. Quality > speed.
- **Test before commit** — где applicable smoke test claims (например claim "agents communicate через mailboxes" — verify mailbox infrastructure actually works)
- **No contradictions с уже built parts** — internal consistency check
- **Provenance per architectural idea** — какая книжка / framework / research basis

**ETA per part:** 1-3 часа ROY swarm. **Total for ~8-12 parts:** 12-30 часов ROY work distributed over multiple waves.

**Cycle structure suggestion:**
- Можно делать **bundle of 3-5 parts per cycle** для efficiency (если они related)
- Или **one part per cycle** для maximum focus
- ROY бригадир decides per scope

### Sub-этап 1.3.D — Integration Pass (cycle 12 final wave)

**Что ROY делает:**

1. Read all per-part documents (8-12 deliverables from 1.3.C)
2. **Identify integration points** (where parts connect / share data / depend)
3. **Verify no contradictions** между parts
4. **Document cross-cutting concerns** (security / observability / Левенчук discipline / governance)
5. **Failure mode integration** — что happens когда part X breaks for part Y / Z
6. **End-to-end scenario walkthroughs** — common workflows traced через все parts
7. **Final coherence check** против FUNDAMENTAL Vision §0-§9
8. **Write Integration Document** (deliverable §2.3)
9. **Write Practical Use Instructions** (deliverable §2.4)
10. **Update CLAUDE.md root** с navigation map (deliverable §2.6)
11. **Final Best Practices Manifest** (consolidate from 1.3.B drafts + per-part sources)

**Output:** Complete Foundation Architecture set — все 6 deliverables ready.

**ETA:** 2-4 часа ROY swarm.

### Sub-этап 1.3.E — Ruslan Final Review + LOCKED

1. Ruslan reads all 6 deliverables
2. Ack / modify / iterate (back to specific sub-part if needed)
3. Final LOCKED — git tag `foundation-architecture-locked-2026-04-27` (или date после ack)
4. Update CLAUDE.md с reference

---

## §4 ROY work pattern (per part / per cycle)

**Discipline которой ROY следует в каждом cycle:**

1. **Read context first** (не start writing без full understanding)
2. **Consult relevant frameworks** (multiple consultants if applicable)
3. **Multiple passes acceptable** — first draft часто not quality
4. **Test claims where possible** — smoke test / cross-reference / scenario walkthroughs
5. **Provenance mandatory** — каждая architectural decision имеет source
6. **No contradictions** with FUNDAMENTAL / FPF / Locks / уже built parts
7. **Strategy learning** — что worked, что не worked → `strategies.md` updates
8. **Quality > speed** — Ruslan ack лучшего качества important чем fast delivery

**Anti-patterns** (avoid):

- ❌ "Скопировал из FPF" без deep understanding (=cargo cult)
- ❌ "Все best practices integrated" generic claim без specifics
- ❌ Premature integration (если parts не yet stable отдельно)
- ❌ Skipping verification ("кажется работает")
- ❌ Loss of provenance (где взяли idea?)
- ❌ Architecture drift от FUNDAMENTAL Vision

---

## §4.5 ⚠️ CRITICAL — Best practices research depth (Ruslan emphasis 27.04 evening)

**ОЧЕНЬ важная constraint которая applies ко всей работе ROY:**

> **НЕ работать с framework на основе одной-двух статей "о том как работает Левенчук" / "о том как работает event sourcing" / etc. Это unacceptable shallow approach.**

**Правильный pattern:**

1. **Primary source — library на сервере** (CC discovery в Sub-этап 1.3.B). **Большинство нужной информации УЖЕ есть** в books / extracts / research dumps / foundations. External web research — **ТОЛЬКО supplementary**, не primary.

2. **"Internal consultant" pattern (mandatory):** для каждого major framework (Левенчук / системное мышление / multi-agent / event sourcing / observability / KM / etc) — ROY создаёт **dedicated internal expert agent** который:
   - **Прочитал ВСЮ foundation framework'а** (book полностью, не chapter; entire methodology, не excerpts)
   - **Имеет deep понимание принципов** (не surface-level summary)
   - **Может answer detailed questions** про framework's application к specific architectural decisions
   - **Доступен другим subagents** для consultation per part work

3. **На 100% глубоко (везде помечать):**
   - Когда ROY work на specific part architecture — consultant'ы applied **на 100%**, не "почитал часть, забил хуй"
   - **"Foundation studied на 100% насколько это возможно"** — не выборочно, не через summary
   - Все decisions traced к specific framework principles (provenance per architectural choice)
   - НЕ "Левенчук говорит X, поэтому делаем X" — а "согласно Левенчук [page/chapter reference], принцип Y means Z в контексте data lifecycle, поэтому в Foundation [specific implementation]"

4. **Balance — sensible scope, но deep coverage chosen frameworks:**
   - НЕ overdo (не перья дрожжи / 50 frameworks superficially)
   - НЕ shallow (одна статья на framework — unacceptable)
   - **Pick few critical frameworks** (Левенчук + системное мышление + multi-agent + event sourcing + KM + observability — primary). Per chosen framework — **полное foundation study**.
   - Остальные frameworks — peripheral references (mentioned, not deep applied)

5. **Если нужного framework нет в library:**
   - **Сначала** check thoroughly что точно нет (multiple search patterns)
   - **Потом** web research — но 5 sources max, focused on canonical introductions / authoritative summaries
   - **Прямо flag в output** что "framework X не имеет полной library coverage, используется через web summary — risk: shallow application"

**Anti-pattern — категорически запрещено:**

- ❌ "Левенчук рекомендует X" из одного блог-поста / Twitter thread
- ❌ Generic "best practices integrated" claims без specific references
- ❌ Surface-level framework citations как decoration
- ❌ Сherry-picking convenient principles, ignoring inconvenient ones from same framework
- ❌ Using framework as cargo cult ("делаем X потому что framework сказал" без understanding why)

**Везде помечать в documents:** "100% framework foundation studied" / "consultant agent X validated this section" / "framework principles applied to N% — areas Y/Z deferred к future work due to Z reason".

**Это constraint applies ко ВСЕМ Sub-этапам 1.3.B + 1.3.C + 1.3.D**, не только library research.

---

## §5 Quality bar + best practices discipline

**Quality bar** (per part document):

- **Comprehensible by professional knowledge worker** — не jargon-soup
- **Actionable** — после reading можно implement / use
- **Cross-referenced** — claims linked к sources / related parts
- **Anti-scoped** — что часть НЕ делает explicit
- **Scenario-tested** — common use cases walkthrough'нуты
- **Best-practices-grounded** — major design choices traced к external proven framework

**Best practices integration discipline:**

- **NOT** mention book → done. **YES** principles от book deeply understood + applied + adapted к Jetix context
- **NOT** "Левенчук говорит X" без understanding why. **YES** "per Левенчук architect-orbit principle, founder retains strategic authority because [reasoning]; в Jetix это означает [specific implementation]"
- **NOT** add framework just because exists. **YES** if framework solves real problem in Foundation, integrate; if не applicable, skip cleanly with reason
- **Honest tradeoffs** — если 2 frameworks suggest different approaches → explicit reasoning why одно chosen

---

## §6 Critical inputs (где ROY должен читать)

**Mandatory reads per ROY:**

| Source | Что взять |
|--------|-----------|
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | Foundation Vision (constitutional baseline) — must-not-violate |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | What we have RIGHT NOW |
| `decisions/JETIX-FPF.md` | Constitutional first principles (Левенчук IP-1 base) |
| `decisions/JETIX-SYSTEM-OVERVIEW.md` | Existing 14-layer description (предыдущая версия architecture) |
| D1-D29 Locks + LOCKS-ADDENDUM (especially D2, D26, D27, D28, D29) | Constitutional anchors |

**Library reads (per Sub-этап 1.3.B discovery):**

| Source | Что взять |
|--------|-----------|
| `raw/research/architecture-variants-2026-04-22/*` | Architecture options explored | 
| `raw/research/folder-structure-deep-research-2026-04-19.md` | Org patterns |
| `raw/research/company-as-code-impl-deep-research-2026-04-19.md` | CaC patterns |
| `raw/research/agency-deep-research-2026-04-18.md` | Operations patterns |
| `raw/research/community-deep-research-2026-04-18.md` | Network patterns |
| `raw/research/consulting-deep-research-2026-04-18.md` | Service patterns |
| `raw/research/holding-deep-research-2026-04-18.md` | Org evolution patterns |
| `raw/research/crm-sales-architecture-deep-research-2026-04-19.md` | CRM patterns |
| `raw/research/career-levels-deep-research-2026-04-19.md` | Role patterns |
| Any books / extracts in repo | Per discovery |

**External references (web research где applicable):**

- Левенчук ШСМ public materials
- Multi-agent system papers (LangGraph / CrewAI architecture papers)
- SRE Book (Google)
- DDD / Event Sourcing (Eric Evans / Vaughn Vernon / Kleppmann)
- Knowledge Management (Andy Matuschak / Karpathy / Luhmann)
- Anthropic Constitutional AI papers

---

## §7 Anti-patterns (что ROY НЕ делает в этой работе)

- ❌ **Architectural decisions без human ack** — per FUNDAMENTAL §4.5 hard rule. Architecture proposals да, execute final structures без ack — нет.
- ❌ **Ruslan-specific content** — это Foundation, не RUSLAN-LAYER. Если что-то Ruslan-specific surface'ится → flag для RUSLAN-LAYER, not include here.
- ❌ **Premature optimization** — если current pattern works, не "improve" без need.
- ❌ **Feature creep** — оставаться в FUNDAMENTAL Vision scope, not add new use cases.
- ❌ **Best practices как decoration** — integrate deeply or skip honestly.
- ❌ **Conflict resolution without surfacing** — если sources conflict → surface к Ruslan / в Open Q, не silent compromise.
- ❌ **Skipping verification** — где applicable, claims tested.
- ❌ **Loss of constitutional alignment** — FUNDAMENTAL Vision LOCKED, FPF LOCKED, D1-D29 LOCKED. Architecture conforms, не overrides.

---

## §8 ROY swarm self-improvement через этот process

**Каждый cycle ROY должен:**

- **Save strategy learnings** в `strategies.md` per agent role что worked / что не worked
- **Document patterns** discovered (если pattern reusable → methodology library)
- **Surface improvement opportunities** (если ROY tooling lacks something → suggest для system improvement)
- **Reduce friction next time** — automation of repeating tasks where possible

**Compound effect:** к Sub-этапу 1.3.D (integration pass) ROY должен быть significantly better чем at start of 1.3.A. Track velocity / quality improvements.

---

## §9 Open Q

1. **Per-part bundle size:** делать ли parts по одному per cycle (max focus) или bundle 3-5 (efficiency)? **Recommend:** bundle related parts (e.g. all info-lifecycle parts together), single cycle для unrelated parts.
2. **External web research depth:** где библиотека на сервере не покрывает framework — насколько глубоко ROY делает external web research? **Recommend:** 2-3 sources external per framework, не infinite.
3. **Verification depth:** smoke test per part или only for critical (foundation parts)? **Recommend:** critical только (KB integrity / agent communication / data persistence).
4. **Cycle count estimate:** сколько cycles надо? Best estimate: 3-5 cycles total (1.3.A + 1.3.B parallel = 1 cycle / 1.3.C = 2-3 cycles depending bundle size / 1.3.D = 1 cycle).
5. **Time estimate:** Best estimate: 12-25 hours total ROY work + 3-5 hours Ruslan reviews. **Realistic timeline:** EOD 28.04 для 1.3.A+B + initial 1.3.C parts; EOD 29.04 для все 1.3.C parts; EOD 30.04 для 1.3.D + Ruslan ack.

---

## §10 Cross-refs

- **Foundation Vision (input):** `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- **AUDIT (input):** `decisions/AUDIT-CURRENT-STATE-2026-04-27.md`
- **Parent Notion:** [🏗️ Генеральная чистка — 3 этапа](https://www.notion.so/34e2496333bf816cb421c263beec172f)
- **Daily Log 27.04:** [📅 27.04.2026 — Development](https://www.notion.so/34e2496333bf81c99b55d634e658b93c)
- **Workflow split (FUNDAMENTAL + RUSLAN-LAYER):** [📌 Workflow split](https://www.notion.so/34f2496333bf81bbb4dfd50a27a941d6)
- **RUSLAN-LAYER (deferred):** `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` — finalize'ится после Foundation closed
- **Output deliverables (будут created):** `decisions/JETIX-FOUNDATION-ARCHITECTURE-2026-04-27.md` + per-part docs + integration + usage guide + best practices manifest

---

## §11 Status

**SPEC v1.0 — ready для ROY launch.**

**Next action:** Cloud Cowork пишет deep prompt для ROY на сервере (на основе этого brief) → Ruslan launch'ит cycle 12 wave A в новом tmux session.

**Living doc:** progress per sub-этап обновляется здесь. Каждый sub-этап completed → check ✅ ниже.

### Progress tracker

- [ ] **Sub-этап 1.3.A** — Master Plan Synthesis (cycle 12 wave A)
- [ ] **Sub-этап 1.3.B** — Library / Best Practices Research (cycle 12 wave B)
- [ ] **Sub-этап 1.3.C** — Per-part Deep Work (cycle 12 waves C+, multiple)
- [ ] **Sub-этап 1.3.D** — Integration Pass (cycle 12 final wave)
- [ ] **Sub-этап 1.3.E** — Ruslan Final Review + LOCKED
- [ ] **Final tag:** `foundation-architecture-locked-YYYY-MM-DD`

---

*Brief created Cloud Cowork 27.04 evening per Ruslan directive. ROY launches per follow-up deep prompt из Cloud Cowork.*
