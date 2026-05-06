---
id: locks-d25-d28-addendum-2026-04-24
title: "Locks D25-D28 Addendum — 4 новых locked decisions + USB-C reinforcement"
type: locks-addendum
state: ACKED
acked_by: ruslan
acked_at: 2026-04-24T22:45:00Z
created: 2026-04-24
extends: raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md (D19-D24)
successor_to: D1-D24 (24 Locks)
tags: [locks, foundation, non-negotiable]
preservation_rule: these 4 locks are non-negotiable for all downstream work; any conflicting prose must be flagged and resolved in favor of these
status: archived
archived_at: 2026-05-06
archived_reason: Pre-Foundation snapshot — superseded
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# Locks D25-D28 — 4 новых locked decisions

> Зафиксированы Ruslan'ом 2026-04-24 22:45 CET на основе voice-memos 506-529 (21-24.04.2026). Эти locks extend'ят предыдущие D1-D24 и являются non-negotiable для всех будущих документов, swarm cycles, strategic decisions.

---

## D25 — Company-as-Code (методологический principle)

**Источник:** audio_510 (21.04.2026 15:21 CET), voice-transcript chat 24.04

**Verbatim Ruslan:** *«строить инфраструктуру Company as a Code с самого начала, способную выдержать масштабирование до триллиона капитализации»* + *«в режиме GitHub работала — компания как код, знания как код, чтобы это вместе соединить»*

**Суть:** Вся Jetix — это **company-as-code** с day 1. Конкретно:
- Всё в git-репозитории, atomic commits с provenance
- Декларативные конфиги в `.claude/config/*.yaml` (не hardcoded пути)
- Каждое изменение системы = commit с чёткой attribution
- Real rollback через `git revert` — не "я помню что было"
- Knowledge-as-code: wiki тоже versioned, каждая мысль — commit
- Company state reconstructable из git history на любой момент

**Implications:**
- Все новые agents, skills, configs, strategies — через structured commits
- Никаких hidden Jetix-specific hardcoded paths в skill коде
- D17 filesystem-SoT усилен: git — это и есть Jetix operationally
- Scale-ready с day 1: инфраструктура которая выдержит $1T капитализации D19

**Anti-patterns disqualified:**
- Конфиги в prose doc instead of yaml
- Agents которые знают Jetix-specific imagine-paths hardcoded
- Решения "в голове Ruslan'а" без git-commit provenance
- Notion как source-of-truth (D17 + D25 совместно делают Notion optional view)

---

## D26 — Team 50-100 Enterprise (НЕ one-person company)

**Источник:** audio_510 (21.04.2026), явное решение #119 в review report

**Verbatim Ruslan:** *«Jetix будет не one person company, а команда из 50-100 человек, работающая как холдинг»* + *«у нас тут большая компания с мощными дядями ребятами у нас enterprise но только enterprise который довольно быстрый»*

**Суть:** Jetix target — enterprise-scale team 50-100 человек. **Явно переопределяет** ранее звучавшие "one-person company" / "One Million Company" upside.

**Implications:**
- Solo-with-team-ready (D2) остаётся в силе для текущей фазы (€0-€50K)
- Но target steady-state — команда 50-100, не soloist с agents
- Phase 2 (€200K+) — первые 2-3 hires
- Phase 2b → Phase 3 — команда вырастает к 50-100 к моменту $100M milestone
- Holding-структура применяется к team, не только к entity (roy-replication)
- Solo-forever mindset vs enterprise-fast — решено в пользу enterprise-fast

**Conflict resolution с earlier vision:**
- Ruslan проговаривал в audio_541 "можно создать one-million one-person company" — **отменено** D26
- Naval-style solo philosophy — **не применимо** к Jetix после validation phase
- D26 strictly **переопределяет** эту ветку

---

## D27 — Fork-and-Merge Evolution Architecture

**Источник:** audio_519 (22.04.2026)

**Verbatim Ruslan:** *«Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя, а лучшие мутации возвращать в основную ветку»*

**Суть:** GitHub-style workflow применён к продукту/методологии:
- Jetix = canonical upstream (stable, curated)
- Каждый client / partner / ecosystem participant может fork
- Локальные mutations (adaptations под свою нишу, свои процессы, свой vertical)
- Лучшие мутации возвращаются upstream через PR-style контрибуцию
- Upstream maintains quality bar + integration
- Downstream получает stability + custom adaptations

**Implications:**
- D13 Closed core / Open surface — усилен: core = canonical Jetix upstream, surface = allowed fork-and-merge
- D21 Roy-replication — уточнён: каждый roy в другой нише = fork + adaptations + потенциальный merge-back
- D20 USB-C positioning — механизм: fork-and-merge это и есть "standards-level interoperability" на уровне методологии
- Новая архитектурная primitive — методология сама эволюционирует через distributed contribution
- Governance question: кто maintains upstream? Какой review process?

**Downstream decisions still pending (не в D27, будут в SYSTEM-OVERVIEW):**
- Конкретный merge-back protocol
- Governance model (BDFL / committee / meritocracy)
- IP licensing (MIT-like / proprietary с exception / dual-license)
- Timing: когда open this mechanic — Phase 2+ (€200K valid'd) или раньше

---

## D28 — Query-Driven KB Filtering

**Источник:** audio_522 (22.04.2026)

**Verbatim Ruslan:** *«Целевая система сбора знаний под конкретную задачу более эффективна, чем универсальный сбор всей доступной информации. Собирать в KB только релевантное конкретному запросу и задаче, отфильтровывая лишнее»*

**Суть:** **Уточнение Private Library moat** из memory `project_jetix_private_library_knowledge_leverage.md`:

**Было:** "pool first, query second" — сперва собираем качественный pool всего first-source материала, потом query по нему.

**Стало D28:** "pool first, **но pool-filling driven by anticipated queries**, query second".

Конкретно:
- `/ingest` не жадно — у каждого ingest есть declared relevance anchor (project / topic / question)
- KB не превращается в свалку всего качественного
- Сборщик имеет **критерий фильтрации** — соответствие текущим active queries
- Unfit material не ingestится even если "качественный"
- Результат: KB меньше по объёму, плотнее по сигнал/шум, быстрее на retrieval

**Implications для существующей архитектуры:**
- `swarm/wiki/` — нужен query-registry: какие anchors активны сейчас
- `/ingest` skill расширяется: `--anchor=<project|topic>` mandatory
- `/lint` check #14: каждый wiki entry должен иметь связь с хотя бы одним anchor
- Stale anchors → garbage collection candidate (не удаление, архивирование)
- Сильно связано с D27 fork-and-merge: fork создаёт свои queries, свой KB-срез

**Anti-patterns disqualified:**
- Жадный ingestion "просто потому что книга хорошая"
- KB без anchor-trace
- Universal "собираем всё из категории X" без специфического задачного вопроса

---

## USB-C Positioning Reinforcement (не новый lock, усиление D20)

**Источник:** voice transcript chat 24.04, audio_508

**Verbatim Ruslan 24.04 (пояснение что он имел в виду):** *«настолько будет технология просто Jetix распространена и мощная что её будут использовать все как раньше использовали прошивку Windows блять для любого компьютера ну или сейчас точно так же будут блять Jetix использовать. Это нахуй значит USBC. Это значит охуенный уровень»*

**Verbatim Ruslan audio_508:** *«Jetix займёт позицию стандарта в мире AI-агентов как USB-C в электронике — будет присутствовать везде»*

**Усиление D20:** USB-C positioning — это **infrastructure-layer dominance**: как Windows прошивка на любом компьютере, Jetix на любой AI-augmented business. Не просто "standards-level interoperability" из raw D20 formulation, а **мир де-факто стандарт**.

**Implications:**
- SYSTEM-OVERVIEW должен показать эту дугу: от сегодня (€0 consulting) до Jetix-on-every-business (infrastructure dominance)
- USB-C + D25 Company-as-Code + D27 Fork-and-merge вместе дают **mechanism** для Jetix становится "Windows прошивкой"
- Прошивка-метафора — ключевая для sales pitch: клиент понимает "это не услуга, это инфраструктура на которой твой бизнес будет работать вечно"

**Relation to McKinsey-platform question (Ruslan deferred — будет в SYSTEM-OVERVIEW):**
- USB-C = infrastructure уровень (под всеми, включая McKinsey)
- McKinsey-platform — возможный private case (McKinsey использует Jetix как их operational OS)
- Не противоречат — McKinsey просто ещё один "компьютер на Windows"
- SYSTEM-OVERVIEW brigadier предложит coherent resolution

---

## Smart AI — internal note (НЕ lock)

Из audio_529: *«Jetix делает Smart AI — как раньше были телефоны, потом смартфоны, так же произойдёт с ИИ»*

**Ruslan 24.04:** *«ну типа запиши между прочим но нет это ещё не лок блять забей хуй»*

**Статус:** **Internal marker, not external product name.** Не D29. Продукт-метка "Smart AI" может использоваться в дискуссиях / internal sales discussions, но официальное positioning не завязывается на этом термине. Jetix = Jetix; Smart AI = one way to describe what Jetix делает.

---

## §X Status

- D25 Company-as-Code: **ACKED** Ruslan 2026-04-24
- D26 Team 50-100 Enterprise: **ACKED** Ruslan 2026-04-24
- D27 Fork-and-merge Evolution: **ACKED** Ruslan 2026-04-24
- D28 Query-driven KB Filtering: **ACKED** Ruslan 2026-04-24
- USB-C reinforcement: зафиксирован как уточнение D20 (не новый lock)
- Smart AI: internal note (NOT lock)

Total Locks after addendum: **D1-D28 = 28 locks**.

## §Y Downstream effects

**Immediate:**
- `decisions/JETIX-SYSTEM-OVERVIEW.md` (будущий) должен явно ссылаться на D25-D28 в каждом relevant слое
- `swarm/wiki/foundations/` — добавить страницу `d25-d28-addendum.md` с cross-refs
- KM Materialization MVP — Wave 2 (Part D company-as-code) теперь работает не "на основе meta-brief", а **на основе утверждённого D25**
- `/ingest` skill после KM Mat lands должен получить `--anchor=<...>` mandatory parameter (D28 requirement)

**Mid-term:**
- `wiki/foundations/team-evolution-phase-1-to-phase-3.md` (будущий) должен отразить D26 team growth trajectory
- Fork-and-merge governance document — writable в Phase 3 (€1M+ validity)

**Long-term:**
- D27 + D28 + D25 вместе создают платформу для Phase 3+ roy-replication — каждый roy = fork + adaptations + query-driven KB + code provenance

---

*End of addendum. D25-D28 locked. Any conflicting prose must flag + resolve in favor of these locks.*
