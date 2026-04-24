---
title: Next Strategic Horizon — Agent-Augmented System (brainstorm Ruslan 2026-04-24)
date: 2026-04-24
type: strategic-vision
state: draft (awaiting review)
author: Ruslan (voice brainstorm) → Cloud Cowork (structuring)
scope: next-week priority stack + 6-pillar roadmap beyond cycle-2 implementation
relates_to:
  - decisions/JETIX-VISION.md
  - decisions/JETIX-PHILOSOPHY.md
  - decisions/JETIX-PLAN.md
  - decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md
  - prompts/cycle-2-implementation-2026-04-24.md
  - memory/project_jetix_private_library_knowledge_leverage.md
---

# Next Strategic Horizon — Agent-Augmented System

## §0 Контекст момента (2026-04-24, 18:00 CET)

- **Phase A ROY swarm live:** 6 agents + wiki v3 infrastructure on disk
- **Cycle-1 closed:** 4 opportunities + 2 HITL acked by Ruslan 2026-04-24
- **Cycle-2 implementation in progress:** Session 2 (fresh CC) executes `prompts/cycle-2-implementation-2026-04-24.md` — 18-26 turns, Stage-Gated pause before report
- **Что дальше неясно** — отсюда и этот документ: отойти на шаг назад, посмотреть всю карту, зафиксировать следующие горизонты до того как cycle-2 закроется

---

## §1 Три фиксируемых концепта (Ruslan's brainstorm kernel)

### C-1. Topic-wiki per agent (domain brain)

**Тезис.** Каждый domain expert агент (engineering / mgmt / systems / philosophy / investor) должен иметь **свою wiki под свою тему**, собранную из Tier-4 curated books (Private Library):

- management-expert → wiki/management/ (PMBOK, Drucker, Grove, Cagan, OKR, etc.)
- systems-expert → wiki/systems-thinking/ (Левенчук ШСМ, Beer, Wiener, Senge, Meadows)
- engineering-expert → wiki/engineering/ (Fowler, Brooks, Clean Code, AI-native)
- philosophy-expert → wiki/philosophy-of-science/ (Popper, Kuhn, Munger, stoic, epistemology)
- investor-expert → wiki/investing/ (Graham, Buffett, Taleb, Kelly, capital allocation)

**Почему это "тренировка агентов":** когда brigadier зовёт `mgmt-expert` на задачу — эксперт не просто с system prompt'ом, а **с живой curated knowledge base** за спиной. Каждое consulting engagement / strategic decision / cycle — он читает свою wiki, извлекает применимые концепты, применяет.

**Ссылка на zakrepы:** D14 (Research revenue-instrumental), Private Library как moat (memory), W-5 Two-level Compounding Engineering.

### C-2. Project-wiki per Jetix project (project brain)

**Тезис.** Каждый Jetix проект (quick-money / research / brand / community / ai-tools / life-os / engineering-thinking / bets — 8 активных projects) имеет **свою wiki**. Внутри wiki может быть **мини-рой** агентов (brigadier + 2-3 experts) выделенных под этот проект.

**Пример:** проект **quick-money (Продюсерский центр + AI consulting)**:
- `wiki/projects/quick-money/` накапливает: клиенты / leads / contracts / ICP matches / outreach logs / offer iterations / pricing experiments
- Мини-рой: project-brigadier + sales-lead + mgmt-expert + philosophy-expert (для ICP calibration)
- Каждая сессия = агент читает накопленное + добавляет новое

**Почему это главное преимущество Jetix:** в отличие от single-session AI который каждый раз starts from zero — Jetix каждый проект становится **умнее со временем**. Это и есть operational manifestation D21 roy-replication: Jetix как meta-coordinator роёв per project.

### C-3. Memory-map externalization (Ruslan's cognitive leverage)

**Тезис.** Когда Ruslan'а в голове уже не хватает памяти чтобы держать все детали 8 проектов + системы + клиентов + стратегии — **carte agent+wiki compensates**.

- Ruslan держит стратегический слой (вертикальные направления, ключевые решения, архетипы)
- Agents+wikis держат tactical слой (детали, история, precedent, artefact provenance)
- Interface = естественный язык: Ruslan спрашивает agent-brigadier'а по проекту → тот достаёт из project-wiki релевантные контекст, отвечает с citations

**Это и есть knowledge-as-leverage в повседневной операции** (не только как конкурентный moat, но и как ежедневный cognitive amplifier).

---

## §2 6-Pillar Roadmap (что строим в ближайшие 2-6 недель)

### Pillar 1 — CURRENT: Cycle-2 implementation (идёт сейчас)
**Ждём:** AWAITING-APPROVAL файл от Session 2 (~45-90 min реального времени). После ack → Part G report → cycle-2 закрыт. М3 solo-vs-matrix experiment — следующий отдельный task.

**Статус:** автоматика, не трогаем пока не закроется.

### Pillar 2 — Topic-wikis per domain expert (C-1 материализация)
**Что делаем:** рой агентов сам собирает свою wiki из Tier-4 books. Каждый expert читает свою allocation (у нас 393 книги в `raw/books-md/` после deep cleanup + Mistral OCR re-run).

**Deliverable:** 5 directories
- `wiki/management/` — mgmt-expert training corpus
- `wiki/systems-thinking/` — systems-expert training corpus
- `wiki/engineering/` — engineering-expert training corpus
- `wiki/philosophy-of-science/` — philosophy-expert training corpus
- `wiki/investing/` — investor-expert training corpus

Каждая wiki: 30-80 `concept.md` extracted + linked + с provenance [src:book-title.md].

**Launch:** после cycle-2 закрытия; ещё один swarm cycle с brigadier → 5 параллельных expert tasks (каждый собирает свою wiki).

**Estimate:** 10-20 swarm turns, ~2-4 hours real time при Max subscription.

### Pillar 3 — Project-wikis per Jetix проект (C-2 материализация)
**Что делаем:** для каждого активного проекта создаём `wiki/projects/<project-id>/`:
- `_moc.md` — mapping index (что есть в этой wiki)
- `context.md` — текущее состояние проекта (ICP, offers, pricing, leads)
- `history.md` — лог событий (append-only)
- `decisions.md` — key decisions made для этого проекта
- `open-questions.md` — что обсудить с Ruslan'ом

**Приоритет proof-of-concept:** **quick-money** первым (деньги Phase 1 €50K Q2 2026 — committed date).

**Estimate:** 1 проект ~ 2-4 swarm turns для bootstrap; 8 projects ~ 20-30 turns total. Можно делать параллельно.

### Pillar 4 — Architecture consolidation (new doc `JETIX-SYSTEM-OVERVIEW.md`)
**Что делаем:** верхнеуровневый coherent документ описывающий Jetix как operating system:
- Product core (consulting / producer center / Secure Network)
- Operations (agents + swarm + wikis + human-in-the-loop)
- Knowledge (Private Library + topic-wikis + project-wikis)
- Business model (revenue lines, unit-econ)
- Trajectory (€0 → €50K → €200K → €1M → $100M → $1T с gates)
- Community (ICP filter, archetypes, Secure Network architecture)

**Это плановый Шаг 4 на 24.04 per Daily Log.** Делает swarm с включёнными 5 domain experts — каждый contributes from его angle.

**Estimate:** 2-4 hours swarm, 30-60 min Ruslan review.

### Pillar 5 — Strategic documents (стратегии per direction)
**Что делаем:** с использованием топовых domain experts + project-wikis пишем стратегические документы, которые реально executable:
- `directions/_active/ai-consulting-dach/strategy.md`
- `directions/_active/producer-center/strategy.md`
- `directions/_hypotheses/secure-network-phase2/thesis.md`
- `decisions/policy/partnership-philosophy.md` (givers/takers, commission structures)
- `decisions/policy/business-portfolio-strategy.md` (Hard Rules + Resource-Allocation Engine)

**Это был backlog 22.04 ("Strategy directions materialize") — сейчас доделываем с агентами как ко-авторами.**

### Pillar 6 — Business execution (зарабатываем деньги)
**Что делаем:** стратегические документы → action items → реальные оутричи / клиенты / контракты.

- AI consulting DACH: первые 5-10 outreach с ICP match → 1-2 discovery call → 1 contract
- Продюсерский центр: 1-3 content pilot клиента на monthly retainer
- Target: €50K Q2 2026 (committed)

**Как agents помогают:**
- sales-researcher ищет prospects по ICP filter
- sales-outreach пишет personalized messages (RU/EN/DE)
- mgmt-expert готовит proposals / offers
- project-brigadier (quick-money) держит пайплайн

---

## §3 Next-Week Priority Stack (24-30 апреля)

| # | Задача | Зависимость | Assignee | Estimate |
|---|---|---|---|---|
| 1 | Cycle-2 implementation landing + Ruslan Part G ack | в процессе | Session 2 CC → Ruslan | 1-2h active + 30min review |
| 2 | M3 solo-vs-matrix experiment (task T-B unit-econ) | OPP-01 shipped | swarm | 2-3h swarm + review |
| 3 | Topic-wikis collection cycle (5 parallel experts) | cycle-2 closed | swarm | 2-4h swarm |
| 4 | `JETIX-SYSTEM-OVERVIEW.md` draft (Pillar 4) | Topic-wikis landed | swarm + Ruslan | 3-4h swarm + 1h review |
| 5 | Project-wiki bootstrap for `quick-money` | OVERVIEW done | swarm | 1-2h |
| 6 | AI consulting DACH strategy draft | quick-money wiki + OVERVIEW | swarm (mgmt + investor experts) | 2-3h |
| 7 | First 5 outreach drafts (sales-outreach agent) | strategy draft | sales-outreach | 1h |
| 8 | Telegram notes batch processing | параллельно | inbox-processor | 30-60min |

**Порядок:** 1 → (2 параллельно с 3) → 4 → 5 → 6 → 7 → 8 идёт параллельно где возможно.

**Ruslan's active role:** review gates (1 / 4 / 6 / 7), approval on major direction shifts. Остальное swarm делает в фоне на Max subscription.

---

## §4 Принципы которые зафиксируем на будущее

1. **"Pool first, query second"** — агент не отвечает от головы, агент reads wiki → synthesizes → cites. Никогда fresh из модели на сложный вопрос.

2. **"Каждый проект = wiki + optional mini-swarm"** — new project → new `wiki/projects/<id>/` в день первого контакта; агенты видят всё что было раньше.

3. **"Experts get smarter monthly"** — раз в ~2-4 недели domain experts делают "knowledge refresh cycle": новые книги/articles/cases из Tier 4 → добавляется в topic-wiki → expert strategies.md обновляется.

4. **"Ruslan держит стратегию, agents держат tactics"** — разделение memory: Ruslan = vertical direction + values + 24 Locks; agents = horizontal execution + precedent + details.

5. **"Business-class tasks (B) имеют приоритет над Method-class (M)"** — HD-02 N=2 rate limiter работает на M-class. На B-class лимита нет. Method exists для Business, не наоборот.

---

## §5 Что НЕ делаем в этом горизонте

- **НЕ перестраиваем foundation docs** (D1-D4 + FPF approved, держим как есть)
- **НЕ ломаем 24 Locks** (все non-negotiable)
- **НЕ запускаем Secure Network Phase 2+** (ждём €200K validation gate)
- **НЕ делаем US market outreach** (пока DACH + English infobiz через продюс-центр)
- **НЕ тратим на paid API** (Max subscription only)
- **НЕ делаем "новую архитектуру"** — то что Ruslan говорил "новую но не новую" = **консолидация существующей с агентами как first-class** (Pillar 4), не redesign

---

## §6 Open questions (Ruslan обсуждаем когда вернёмся)

1. **Topic-wiki allocation per expert:** кто читает какую подгруппу books? У нас 393 books. Allocation уже частично сделан в `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §10.2` — пересматриваем или оставляем?

2. **Project-wiki format:** минимальный scaffold (_moc + context + history + decisions + open-questions) vs больше секций? Начинаем с минимума?

3. **Business execution kickoff:** ждём JETIX-SYSTEM-OVERVIEW + strategy docs ИЛИ параллельно пилим outreach пока swarm занят overview'ом? (Рекомендация: параллельно — sales work runs в твоих руках, swarm работает в фоне.)

4. **M-class vs B-class classification** — rate limiter HD-02 требует чёткого определения "это M-task или B-task?" для каждой новой задачи. Нужен short decision tree.

5. **Budget per cycle** — сколько swarm cycles в день реально affordable на Max subscription до ceiling? Эмпирически 2-3 cycles/day (per EOD 23.04). Этот лимит держим?

---

## §7 Definition of done для этого документа

- [x] 3 concepts fixed (C-1 topic-wiki / C-2 project-wiki / C-3 memory-map)
- [x] 6-pillar roadmap с dependencies
- [x] Next-week priority stack с estimates
- [x] Принципы (5 штук) зафиксированы
- [x] Out-of-scope items explicit
- [x] Open questions surfaced
- [ ] Ruslan review + modifications (pending)
- [ ] Daily Log 24.04 updated с ссылкой на этот документ (pending)
- [ ] Committed + pushed

---

*End of document. Awaiting Ruslan review.*
