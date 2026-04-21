---
id: knot-map-2026-04-21
title: Knot Map — Tensions, Clusters, Gaps (Stage 1 navigation)
date: 2026-04-21
type: knot-map
status: ready
companion_to: ATOM-REGISTRY.md
total_atoms: 3626
---

# Knot Map — Navigation по Atom Registry

Companion-документ к `ATOM-REGISTRY.md`. Используется как входной overview:
где узлы напряжения, где кластеры, где gaps, что sirотно.

## 0. Statistics overview

- Total atoms: **3626**
- Tensions (explicit type): **59**
- Tensions pre-resolved (LOCKED): **8** (см. TENSIONS-PRE-RESOLVED.md)
- Atoms overridden by locked decisions: **54**
- Atoms reinforced (multi-source): **357**
- Orphans (no relates_to): **3420**
- Clusters (size ≥ 3): **310**
- Dimension gaps (< 20 atoms): none
- Phase gaps (< 10 atoms): none

### Per dimension
- base: 1168
- company: 1159
- philosophy: 374
- life: 364
- community: 293
- money: 184
- relationships: 53
- brand: 28
- long-term: 2
- research: 1

### Per phase
- any: 1433
- phase-1: 1064
- now: 451
- phase-2: 403
- long-term: 239
- phase-3: 36

---

## 1. Tensions

### 1.1 Tensions resolved в TENSIONS-PRE-RESOLVED (reference — LOCKED)

1. **Gentlemen vs Piranhas** → Gentleman inside / Predator outside.
2. **Solo vs Team** → Solo-now-with-team-ready-scaffolding.
3. **Open-source vs Patents** → Closed outside / Open inside (team).
4. **Name (Jetix vs Jackson)** → Jetix, без изменений.
5. **Phase priority** → Consulting-first Phase 1, Secure Network = Phase 2+.
6. **Anton/Vladislav/Rodion** → Не ключевые, не упоминать.
7. **6 архетипов vs 5 каста** → Union (10 archetypes merged).
8. **Jetix multiplicity frames** → Layered identity (different faces per observer/phase).

Все 8 decisions — **binding overrides** для registry.
Atoms, попавшие под override, имеют `status: "overridden"` + note.

Count of atoms overridden: **54**.

### 1.2 Remaining tensions (explicit type="tension" atoms — OPEN)


#### Dimension: Base

- **atom-0172** — Tension: CrewAI как tactical tool сейчас vs claim что orchestration временный — решение: не строить долгосрочный бизнес 
  - Source: `wiki/ideas/automate-research-via-crewai.md:L48`
  - Relates: —

- **atom-0629** — Contradiction edge: orchestration-is-temporary-feature-gap.md ⇄ automate-research-via-crewai.md
  - Source: `wiki/_lint-report-2026-04-16.md:L40`
  - Relates: —
  - Note: Internal tension in wiki — build-vs-wait on orchestration.

- **atom-0883** — Психологический барьер: мозг не верит что за 3 дня AI-ресёрч = валидная основа; качество было = недели работы
  - Source: `wiki/sources/2026-04-16-mozg-ne-verit-chto-za-3-dnya-mozhno-sdelat-kachestvenny-2.md:L19`
  - Relates: —
  - Note: Duplicated in parallel file — reinforced.

- **atom-1477** — AI как магия vs AI как усилитель: «magic» эмоциональный регистр, «усилитель» инженерный. Не противоречие, но разное удар
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L1285`
  - Relates: —
  - Note: Conflict 3 — not a true contradiction, just register difference.

- **atom-1479** — Contrarian: orchestration-слой (LangChain, CrewAI, n8n) исчезнет, когда базовые модели дорастут. Не строй стратегию на с
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L429`
  - Relates: —
  - Note: Ruslan self-flagged внутри Theme 11 как conflicting с основной линией. Stage 1 — сохраняем обе стороны.

- **atom-1483** — Строить слой агентов vs Orchestration temporary: позиция 1 — North Star 100K+ агентов, Jetix OS = 12 агентов, CrewAI pip
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L1279`
  - Relates: —
  - Note: Conflict 2 — flagged by Ruslan himself via contradicts edge. Agent-layer vs business-logic-layer.

- **atom-3456** — OT5 FPF-Lite Token-budget: Вариант A (full text везде) — 7-10K tokens loaded в каждый agent
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L795`
  - Relates: —
  - Note: Глубина > efficiency. Quality over token savings

- **atom-3457** — OT3 EU AI Act: Scenario C (Risk-proportional) — 4 risk categories with different human gates
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L847`
  - Relates: —

- **atom-3458** — OT5 Publishing: Вариант A (internal forever initially) — secret sauce protected, revisit at €1M+ ARR
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L811`
  - Relates: —
  - Note: backlog fpf-lite-publishing-review.md

- **atom-3459** — OT1 Strategic-management decomposition — RESOLVED EARLY: hybrid 5 manifests + executor ruslan multi-role-binding
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L90`
  - Relates: —
  - Note: Reduced Chunk 4 outstanding 5->4

- **atom-3460** — OT2 Bilingual Frontmatter: Scenario E (Hybrid) — namespace-specific language conventions + auto-translation hook
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L877`
  - Relates: —

- **atom-3626** — Notion = external truth; filesystem = internal truth — partial contradiction с Vision separability (internal truth must 
  - Source: `raw/research/architecture-variants-2026-04-22/JETIX-WIKI-SEARCH-FOR-VISION.md:L451`
  - Relates: —
  - Note: Needs resolution в SYNTHESIS-GOAL.

#### Dimension: Life

- **atom-0674** — Мозг пока не верит, что за 3 дня можно сделать качественный анализ — но результат показывает что да
  - Source: `wiki/sources/2026-04-16-ai-uskoryaet-analiz-rynka-v-5-10-raz-3-dnya-s-ai-2-nede-3.md:L19`
  - Relates: —

- **atom-0724** — Риск выгорания если не научиться отдыхать без травы
  - Source: `wiki/sources/2026-04-16-cannabis-refusal-beast-mode-orientation.md:L23`
  - Relates: —

- **atom-0748** — Ritual conflict: weekly-analysis ритуал пропущен 2026-03-22, «признан нерелевантным в темпе»
  - Source: `wiki/sources/2026-04-16-daily-log-insights-digest.md:L41`
  - Relates: —

- **atom-1133** — UNCLEAR — meditation-attention-management-now: life-ritual (Часть 4) или мета-навык (Часть 1)?
  - Source: `wiki/topics/system-design-hub.md:L164`
  - Relates: —

- **atom-1134** — UNCLEAR — safe-hedonism-personal-motivation: включать ли в Часть 1 (Видение) как личный pipeline?
  - Source: `wiki/topics/system-design-hub.md:L159`
  - Relates: —

- **atom-1135** — UNCLEAR из Phase 5 — cannabis-refusal-beast-mode-orientation: личное; считать ли частью life-system protocol?
  - Source: `wiki/topics/system-design-hub.md:L157`
  - Relates: —
  - Note: Open question flagged for manual review

- **atom-1480** — Психологический барьер: мозг не верит что за 3 дня с AI = качественный анализ. Нужно перестраивать отношение: качество о
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L295`
  - Relates: —
  - Note: Source wiki: mozg-ne-verit-chto-za-3-dnya-mozhno-sdelat-kachestvenny-2.md. Повторяется 3+ раза.

- **atom-2208** — Скорость vs глубина
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L485-L487`
  - Relates: —
  - Note: Resolution: ICP+сайт+видео быстро; философия+патенты+методология глубоко

#### Dimension: Company

- **atom-0067** — Tension: не строить на orchestrators vs использовать CrewAI прямо сейчас
  - Source: `wiki/graph/summaries.md:L24`
  - Relates: —

- **atom-0213** — Риски консалтинга: привязка к часам (consulting trap), невозможность масштаба без productization, конфликт интересов
  - Source: `wiki/ideas/consulting-as-trojan-horse.md:L44`
  - Relates: —

- **atom-0346** — Фундаментальный вопрос контент-стратегии: хуки для масс vs аналитика для умных? Деньги или влияние?
  - Source: `wiki/ideas/kontent-strategiya-khuki-dlya-debilov-ili-analitika-dly.md:L22`
  - Relates: atom-0847 (reinforces)

- **atom-0847** — Фундаментальный вопрос контент-стратегии: хуки для масс ИЛИ аналитика для умных? Денег или влияния? Показать что умный и
  - Source: `wiki/sources/2026-04-16-kontent-strategiya-khuki-dlya-debilov-ili-analitika-dly.md:L19`
  - Relates: atom-0346 (reinforces), atom-1478 (reinforces)

- **atom-0939** — Фундаментальная дилемма: либо ты хищник (используешь reverse-engineering для захвата рынка), либо жертва (кто-то другой 
  - Source: `wiki/sources/2026-04-16-predator-corporation-business-vulnerability.md:L23`
  - Relates: —
  - Note: Core to TENSION #1 Predator outside.

- **atom-1033** — Парадокс: сам стратегический план Jetix — это тоже «миф», который убеждает людей действовать. Значит миф нужен, но он до
  - Source: `wiki/sources/2026-04-16-system-first-myth-second.md:L23`
  - Relates: —

- **atom-1476** — Одиночка с AI — мощно, но bottleneck в его внимании. 5 человек делят слепые пятна, AI ускоряет каждого.
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L103`
  - Relates: —
  - Note: Source wiki: focus-theory-5-people-ai-1-task.md. Tension between solo-now и team-ready scaffolding — aligned с override #2

- **atom-1478** — Фундаментальный вопрос контент-стратегии: хуки для масс vs аналитика для умных. Деньги vs влияние. Показать что умный vs
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L935`
  - Relates: atom-0847 (reinforces)
  - Note: Theme 30 OP-BRAND. Explicit Ruslan internal conflict. Source wiki: kontent-strategiya-khuki-dlya-debilov-ili-analitika-dly.md

- **atom-1481** — Портфель vs Последовательность: позиция 1 — портфель 5-20 параллельных направлений, можно спокойно тестировать 5 направл
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L1273`
  - Relates: —
  - Note: Conflict 1 from RUSLAN-IDEAS meta-observation. Reconciliation: parallel for tests, sequential for core.

- **atom-1482** — Нарратив нужен vs Система первична: позиция 1 — нужен собственный миф для масштабирования, философская работа центральна
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L1291`
  - Relates: —
  - Note: Conflict 4 — Ruslan's stance: myth needed but must follow the system.

- **atom-1484** — Community-family vs Predator mode: позиция 1 — Jetix семья, safe partners, revenue-share защищает; позиция 2 — хищник ли
  - Source: `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md:L1297`
  - Relates: —
  - Note: Conflict 5 — aligns with locked TENSION #1 (Gentleman inside / Predator outside). Not a real contradiction.

- **atom-1967** — Командный vs solo-режим: 'Собрать 100 инженеров + философов + влиятельных' (audio_424) vs 'одиночная игра, один я, никак
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L632`
  - Relates: —
  - Note: Resolved by lock #2 Solo-now-with-team-ready-scaffolding — solo now, team ready

- **atom-1968** — Open vs moat: 'Открытая методология / open-source GitHub' (audio_451,459) vs 'патентная стратегия / юридическая защита Е
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L636`
  - Relates: —
  - Note: Resolved by lock #3 Closed outside / Open inside (team)

- **atom-1969** — Scale vs selection: 'Продюсерский центр для инфобиза (англоязычные)' (audio_474,475,477) vs 'элитное community, вино не 
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L635`
  - Relates: —
  - Note: likely resolved by Layered Identity (lock #8) — different faces different observers

- **atom-1970** — Coalition vs sovereignty: 'Fortune 500 через Mythos + дядя Руслан' (audio_429,448) vs 'независимость, без подчинения кру
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L634`
  - Relates: —
  - Note: internal tension unresolved

- **atom-2209** — 'Только деньги, никакой ресёрч' vs 11 research TODOs
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L469-L471`
  - Relates: —
  - Note: Resolution: research только для продаж (ICP/рынок/практики), не 'великие дела'

- **atom-2210** — Фокус на одном vs параллельные новые проекты (4 NEW projects)
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L489-L491`
  - Relates: —
  - Note: Resolution: NEW projects = candidate directions для Jetix-core, не параллельные entities

- **atom-2211** — 'Собрать команду 10-20 человек' vs 'one million one person company'
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L473-L475`
  - Relates: —
  - Note: Tension #2 (solo-now-with-team-ready-scaffolding) phased resolution

- **atom-2355** — Geo-фокус: Германия (патенты) vs англоязычный инфобиз — выбор не сделан
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md:L416`
  - Relates: —
  - Note: phased resolution: Germany для patents, English для sales

- **atom-2356** — Соло vs команда — 10K страниц перечитаю vs башка не справится, 10→20→мир
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md:L411`
  - Relates: —
  - Note: consistent с lock #2 — solo-now-with-team-ready-scaffolding; phased resolution

- **atom-2358** — Скрытая vs публичная методология — audio_416 (скрыта, иначе обесценится), audio_418 (показатель силы Claude Code), audio
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md:L410`
  - Relates: —
  - Note: unresolved tension — совпадает с Genesis tension #2, synthesis direction: open surface / closed core

- **atom-3148** — Открытые вопросы: designated trustee identity (not Anton, TBD); trademark Jetix vs Disney; first CHR space refinement; U
  - Source: `decisions/2026-04-20-jetix-architecture-final-DRAFT.md:L231`
  - Relates: —

- **atom-3461** — OT4 Trademark Jetix vs Disney: DEFER — Perplexity research Phase 1, unofficial usage, formal resolution at €20-50K reven
  - Source: `decisions/2026-04-19-architecture-v2-approval.md:L828`
  - Relates: —
  - Note: Phase 2a IP lawyer €2000-3500 budget

- **atom-3527** — Fortune 500 coalition vs sovereignty — parked bet, может Phase 3+
  - Source: `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md:L329`
  - Relates: —
  - Note: Soft tension, long-horizon.

- **atom-3528** — Pain-based vs opportunity-based sales — Ruslan склонялся к opportunity-based post-17 апреля, не resolved
  - Source: `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md:L327`
  - Relates: —
  - Note: Soft tension для Stage 2 resolve. Не блокирует D1/D2/D3.

- **atom-3529** — Geo first — Germany-patents vs English-infobiz — возможно phased (English для revenue, Germany для защиты)
  - Source: `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md:L328`
  - Relates: —
  - Note: Soft tension для Stage 2 resolve.

- **atom-3530** — NEW projects (ideas-platform / job-matching / investment-fund) — продюсерский центр внутри, остальные parked?
  - Source: `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md:L330`
  - Relates: —
  - Note: Soft tension для Stage 2 resolve.

#### Dimension: Community

- **atom-0157** — Открытые вопросы анти-free-riding: что считается вкладом, как измерять без бюрократии, публичность vs приватность, кто с
  - Source: `wiki/ideas/anti-free-riding-accountability.md:L34`
  - Relates: —

- **atom-0689** — Anti-free-riding: как предотвратить постепенное free-riding в сообществе Jetix, когда каждый надеется на вклад других
  - Source: `wiki/sources/2026-04-16-anti-free-riding-accountability.md:L27`
  - Relates: —

- **atom-2212** — Community-first (ранние транскрипты) vs Money-first (поздние транскрипты)
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L493-L496`
  - Relates: —
  - Note: Pivot уже произошёл. Tension #5 — Secure Network = Phase 2+

- **atom-2357** — Джентльмены (Kingsman) vs хищники (пираньи) — две community identities не синтезированы
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md:L413`
  - Relates: —
  - Note: per lock #1 — Gentleman inside / Predator outside; синтез существует

#### Dimension: Money

- **atom-1136** — UNCLEAR — money-value-mindset-pre-launch: pre-launch mindset; релевантно Части 1, но не уверен какой sub-topic
  - Source: `wiki/topics/system-design-hub.md:L161`
  - Relates: —

- **atom-1972** — Tactical money vs strategic humanity: '€50K → €200K money-only focus' (audio_435,436,503) vs 'польза человечеству, 200-y
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L633`
  - Relates: —
  - Note: Phase sequencing — tactical now, strategic later

- **atom-2214** — '$5k на счету, увольняюсь' vs resource-heavy планы (патентование, $10k/мес×10, $1000 эксперимент)
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md:L481-L483`
  - Relates: —
  - Note: Resolution: heavy-spend на phase-2+

- **atom-2354** — Pain-based vs голодное позиционирование — tone-пивот за 3 дня
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md:L415`
  - Relates: —
  - Note: context-resolved: hunger для starter, opportunity для scale

- **atom-2396** — Tactical vs strategic — 50 косарей и не меньше, никакие исследования vs 200-year vision capitalism→communism
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md:L37`
  - Relates: —
  - Note: Ruslan explicit resolve: тактика прибыль, стратегия польза

#### Dimension: Philosophy

- **atom-1966** — Safety vs power positioning: 'Jetix как безопасная мастерская' (audio_422) vs 'бугай с самой большой дубиной' (audio_496
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L638`
  - Relates: —
  - Note: Resolved by lock #1 Gentleman-inside/Predator-outside

- **atom-1971** — Helpful vs aggressive framing: 'захватнический → useful' (audio_430) vs 'я иду разъёбывать' (audio_437) vs 'Jetix уничто
  - Source: `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md:L637`
  - Relates: —
  - Note: Resolved by lock #1 Gentleman-inside/Predator-outside


### 1.3 Soft tensions / parked (из TENSIONS-PRE-RESOLVED §Remaining)


Не locked, ждут Stage 2:
- **#4 Pain-based vs opportunity-based sales** — склонность к opportunity-based post-17 апреля.
- **#6 Geo first (Germany-patents vs English-infobiz)** — возможно phased.
- **#7 Fortune 500 coalition vs sovereignty** — parked bet (Phase 3+).
- **#8 NEW projects (ideas-platform / job-matching / investment-fund)** — продюсерский центр внутри, остальные parked?

Gaps из digest §7.2 (thin coverage):
- **Exit / liquidity / equity structure** — не обсуждалось.
- **Regulatory / compliance (GDPR / AI Act / DE)** — thin.
- **Recovery / nutrition / sleep (Jetix-life)** — thin.


---

## 2. Clusters (groups of related atoms ≥ 3)

### C-01 — company / bet (26 atoms)
- Dimension: **company**
- Topic tag: **bet**
- Density: 26 atoms
- Members: atom-1920, atom-1921, atom-1924, atom-1925, atom-1926, atom-1927, atom-1931, atom-1932, atom-1934, atom-1935, atom-1939, atom-1941, atom-1943, atom-1944, atom-1945, atom-1948, atom-1949, atom-1950, atom-1951, atom-1952, atom-1955, atom-1957, atom-1959, atom-1962, atom-1963 _(+1 more)_

### C-02 — base / ai (19 atoms)
- Dimension: **base**
- Topic tag: **ai**
- Density: 19 atoms
- Members: atom-0002, atom-0070, atom-0072, atom-0114, atom-0135, atom-0139, atom-0143, atom-0286, atom-0287, atom-0293, atom-0369, atom-0407, atom-0416, atom-0420, atom-0597, atom-0650, atom-0652, atom-1087, atom-1580

### C-03 — base / rule (18 atoms)
- Dimension: **base**
- Topic tag: **rule**
- Density: 18 atoms
- Members: atom-0385, atom-3210, atom-3211, atom-3212, atom-3213, atom-3214, atom-3215, atom-3216, atom-3217, atom-3218, atom-3219, atom-3220, atom-3221, atom-3222, atom-3223, atom-3224, atom-3226, atom-3227

### C-04 — base / wiki (17 atoms)
- Dimension: **base**
- Topic tag: **wiki**
- Density: 17 atoms
- Members: atom-0066, atom-0692, atom-0693, atom-1357, atom-1486, atom-2000, atom-3175, atom-3196, atom-3203, atom-3205, atom-3207, atom-3362, atom-3547, atom-3549, atom-3553, atom-3557, atom-3614

### C-05 — company / icp (17 atoms)
- Dimension: **company**
- Topic tag: **icp**
- Density: 17 atoms
- Members: atom-0476, atom-0584, atom-0679, atom-0795, atom-1073, atom-1668, atom-1693, atom-1741, atom-2032, atom-2134, atom-2218, atom-2241, atom-2361, atom-2460, atom-2495, atom-2576, atom-2819

### C-06 — life / life-os (15 atoms)
- Dimension: **life**
- Topic tag: **life-os**
- Density: 15 atoms
- Members: atom-0068, atom-0298, atom-0299, atom-0382, atom-0514, atom-0515, atom-0850, atom-0851, atom-1011, atom-1012, atom-1487, atom-2086, atom-2518, atom-2882, atom-3372

### C-07 — life / bon-ritual (15 atoms)
- Dimension: **life**
- Topic tag: **bon-ritual**
- Density: 15 atoms
- Members: atom-1154, atom-1259, atom-1281, atom-1294, atom-1303, atom-1318, atom-1327, atom-1372, atom-1378, atom-1379, atom-1389, atom-1405, atom-1428, atom-1521, atom-1522

### C-08 — community / cross-ref (15 atoms)
- Dimension: **community**
- Topic tag: **cross-ref**
- Density: 15 atoms
- Members: atom-1619, atom-1646, atom-1664, atom-1721, atom-1734, atom-1736, atom-1759, atom-1768, atom-1788, atom-1793, atom-1798, atom-1799, atom-1805, atom-1809, atom-1811

### C-09 — base / notion (14 atoms)
- Dimension: **base**
- Topic tag: **notion**
- Density: 14 atoms
- Members: atom-0052, atom-1142, atom-1235, atom-1264, atom-1460, atom-2071, atom-2359, atom-3189, atom-3190, atom-3191, atom-3192, atom-3193, atom-3195, atom-3626

### C-10 — base / rollback (14 atoms)
- Dimension: **base**
- Topic tag: **rollback**
- Density: 14 atoms
- Members: atom-3000, atom-3001, atom-3002, atom-3005, atom-3006, atom-3007, atom-3009, atom-3011, atom-3012, atom-3013, atom-3015, atom-3016, atom-3017, atom-3018

### C-11 — company / sales (13 atoms)
- Dimension: **company**
- Topic tag: **sales**
- Density: 13 atoms
- Members: atom-0240, atom-0454, atom-0491, atom-0492, atom-0660, atom-0992, atom-0993, atom-0994, atom-1090, atom-2107, atom-2287, atom-2820, atom-3528

### C-12 — community / concept (13 atoms)
- Dimension: **community**
- Topic tag: **concept**
- Density: 13 atoms
- Members: atom-1676, atom-1688, atom-1690, atom-1716, atom-1717, atom-1722, atom-1751, atom-1755, atom-1766, atom-1787, atom-1790, atom-1794, atom-1795

### C-13 — base / d6 (13 atoms)
- Dimension: **base**
- Topic tag: **d6**
- Density: 13 atoms
- Members: atom-2656, atom-2731, atom-2778, atom-2784, atom-3118, atom-3267, atom-3341, atom-3354, atom-3359, atom-3361, atom-3409, atom-3424, atom-3497

### C-14 — base / agents (12 atoms)
- Dimension: **base**
- Topic tag: **agents**
- Density: 12 atoms
- Members: atom-0053, atom-2029, atom-2054, atom-2089, atom-2130, atom-2398, atom-3198, atom-3199, atom-3200, atom-3201, atom-3204, atom-3555

### C-15 — company / consulting (12 atoms)
- Dimension: **company**
- Topic tag: **consulting**
- Density: 12 atoms
- Members: atom-0211, atom-0212, atom-0344, atom-0486, atom-0740, atom-0741, atom-1126, atom-1230, atom-1640, atom-1738, atom-2099, atom-2297

### C-16 — company / b-open (12 atoms)
- Dimension: **company**
- Topic tag: **b-open**
- Density: 12 atoms
- Members: atom-1265, atom-1300, atom-1309, atom-1361, atom-1364, atom-1377, atom-1424, atom-1427, atom-1448, atom-1465, atom-1473, atom-1527

### C-17 — company / tension (11 atoms)
- Dimension: **company**
- Topic tag: **tension**
- Density: 11 atoms
- Members: atom-0067, atom-1967, atom-1968, atom-1969, atom-1970, atom-2209, atom-2210, atom-2211, atom-2355, atom-2356, atom-2358

### C-18 — philosophy / ai (11 atoms)
- Dimension: **philosophy**
- Topic tag: **ai**
- Density: 11 atoms
- Members: atom-0107, atom-0116, atom-0117, atom-0118, atom-0151, atom-0288, atom-0292, atom-0498, atom-1850, atom-2249, atom-2311

### C-19 — company / positioning (11 atoms)
- Dimension: **company**
- Topic tag: **positioning**
- Density: 11 atoms
- Members: atom-0110, atom-0308, atom-0475, atom-0821, atom-0953, atom-1065, atom-1066, atom-1067, atom-1336, atom-1354, atom-2362

### C-20 — company / methodology (11 atoms)
- Dimension: **company**
- Topic tag: **methodology**
- Density: 11 atoms
- Members: atom-0152, atom-0337, atom-0687, atom-0820, atom-0838, atom-0839, atom-1207, atom-1330, atom-1355, atom-2303, atom-2310

### C-21 — community / clan (11 atoms)
- Dimension: **community**
- Topic tag: **clan**
- Density: 11 atoms
- Members: atom-0334, atom-0336, atom-0377, atom-0520, atom-0521, atom-0837, atom-0879, atom-1017, atom-1250, atom-1665, atom-1680

### C-22 — life / environment (11 atoms)
- Dimension: **life**
- Topic tag: **environment**
- Density: 11 atoms
- Members: atom-0459, atom-0468, atom-0531, atom-0699, atom-0948, atom-0949, atom-0965, atom-1029, atom-1093, atom-1489, atom-1873

### C-23 — community / community (10 atoms)
- Dimension: **community**
- Topic tag: **community**
- Density: 10 atoms
- Members: atom-0021, atom-0278, atom-0281, atom-1590, atom-1995, atom-2219, atom-2369, atom-2464, atom-2472, atom-3537

### C-24 — base / research (10 atoms)
- Dimension: **base**
- Topic tag: **research**
- Density: 10 atoms
- Members: atom-0093, atom-0129, atom-0141, atom-0284, atom-0400, atom-0472, atom-0556, atom-0663, atom-0974, atom-2655

### C-25 — base / architecture (10 atoms)
- Dimension: **base**
- Topic tag: **architecture**
- Density: 10 atoms
- Members: atom-0418, atom-0427, atom-0610, atom-2122, atom-2451, atom-2983, atom-3206, atom-3431, atom-3511, atom-3592

### C-26 — company / concept (10 atoms)
- Dimension: **company**
- Topic tag: **concept**
- Density: 10 atoms
- Members: atom-1596, atom-1605, atom-1629, atom-1689, atom-1700, atom-1708, atom-1771, atom-1772, atom-1800, atom-1801

### C-27 — company / evolution (10 atoms)
- Dimension: **company**
- Topic tag: **evolution**
- Density: 10 atoms
- Members: atom-2255, atom-2257, atom-2855, atom-2858, atom-2862, atom-2863, atom-2885, atom-2893, atom-2899, atom-2905

### C-28 — company / cost (10 atoms)
- Dimension: **company**
- Topic tag: **cost**
- Density: 10 atoms
- Members: atom-2790, atom-3123, atom-3125, atom-3126, atom-3127, atom-3128, atom-3130, atom-3135, atom-3136, atom-3142

### C-29 — base / claude-code (9 atoms)
- Dimension: **base**
- Topic tag: **claude-code**
- Density: 9 atoms
- Members: atom-0051, atom-1559, atom-2016, atom-2040, atom-2116, atom-2121, atom-2337, atom-2402, atom-2403

### C-30 — company / portfolio (9 atoms)
- Dimension: **company**
- Topic tag: **portfolio**
- Density: 9 atoms
- Members: atom-0102, atom-0103, atom-0444, atom-1257, atom-2598, atom-2838, atom-2874, atom-2972, atom-3581

### C-31 — philosophy / concept (9 atoms)
- Dimension: **philosophy**
- Topic tag: **concept**
- Density: 9 atoms
- Members: atom-1599, atom-1701, atom-1747, atom-1762, atom-1779, atom-1781, atom-1785, atom-1804, atom-2094

### C-32 — base / shsm (9 atoms)
- Dimension: **base**
- Topic tag: **shsm**
- Density: 9 atoms
- Members: atom-2555, atom-2652, atom-2769, atom-2774, atom-2779, atom-2786, atom-2792, atom-2797, atom-3445

### C-33 — company / chunk-8 (9 atoms)
- Dimension: **company**
- Topic tag: **chunk-8**
- Density: 9 atoms
- Members: atom-2831, atom-2851, atom-2906, atom-2925, atom-3056, atom-3060, atom-3063, atom-3068, atom-3121

### C-34 — base / forbidden (9 atoms)
- Dimension: **base**
- Topic tag: **forbidden**
- Density: 9 atoms
- Members: atom-2930, atom-2933, atom-2934, atom-2938, atom-2941, atom-2945, atom-2954, atom-2964, atom-2966

### C-35 — company / focus (8 atoms)
- Dimension: **company**
- Topic tag: **focus**
- Density: 8 atoms
- Members: atom-0014, atom-0253, atom-0254, atom-0255, atom-0370, atom-2048, atom-2087, atom-2169

### C-36 — base / github (8 atoms)
- Dimension: **base**
- Topic tag: **github**
- Density: 8 atoms
- Members: atom-0055, atom-0056, atom-1138, atom-2007, atom-2026, atom-2154, atom-2278, atom-2324

### C-37 — company / content (8 atoms)
- Dimension: **company**
- Topic tag: **content**
- Density: 8 atoms
- Members: atom-0085, atom-0122, atom-0346, atom-0347, atom-0683, atom-1695, atom-2440, atom-2706

### C-38 — company / outreach (8 atoms)
- Dimension: **company**
- Topic tag: **outreach**
- Density: 8 atoms
- Members: atom-0087, atom-0127, atom-0493, atom-1784, atom-2042, atom-2076, atom-2399, atom-3086

### C-39 — company / research (8 atoms)
- Dimension: **company**
- Topic tag: **research**
- Density: 8 atoms
- Members: atom-0094, atom-0099, atom-0331, atom-0355, atom-0865, atom-0909, atom-0969, atom-2220

### C-40 — life / discipline (8 atoms)
- Dimension: **life**
- Topic tag: **discipline**
- Density: 8 atoms
- Members: atom-0145, atom-0146, atom-0554, atom-0677, atom-0817, atom-0963, atom-1052, atom-1983

### C-41 — company / business-model (8 atoms)
- Dimension: **company**
- Topic tag: **business-model**
- Density: 8 atoms
- Members: atom-0187, atom-0567, atom-0661, atom-0685, atom-0845, atom-0982, atom-1059, atom-1132

### C-42 — company / op-sales (8 atoms)
- Dimension: **company**
- Topic tag: **op-sales**
- Density: 8 atoms
- Members: atom-1200, atom-1297, atom-1298, atom-1310, atom-1319, atom-1337, atom-1344, atom-1406

### C-43 — base / q-depth (8 atoms)
- Dimension: **base**
- Topic tag: **q-depth**
- Density: 8 atoms
- Members: atom-1345, atom-1351, atom-1384, atom-1403, atom-1408, atom-1463, atom-1464, atom-1520

### C-44 — philosophy / cross-ref (8 atoms)
- Dimension: **philosophy**
- Topic tag: **cross-ref**
- Density: 8 atoms
- Members: atom-1699, atom-1726, atom-1733, atom-1735, atom-1777, atom-1783, atom-1797, atom-1806

### C-45 — base / review (8 atoms)
- Dimension: **base**
- Topic tag: **review**
- Density: 8 atoms
- Members: atom-2970, atom-2973, atom-2975, atom-2978, atom-2986, atom-2996, atom-3048, atom-3141

### C-46 — base / source (8 atoms)
- Dimension: **base**
- Topic tag: **source**
- Density: 8 atoms
- Members: atom-3151, atom-3160, atom-3161, atom-3162, atom-3163, atom-3165, atom-3167, atom-3171

### C-47 — base / orchestration (7 atoms)
- Dimension: **base**
- Topic tag: **orchestration**
- Density: 7 atoms
- Members: atom-0015, atom-0124, atom-0125, atom-0658, atom-0912, atom-1117, atom-1137

### C-48 — company / jetix (7 atoms)
- Dimension: **company**
- Topic tag: **jetix**
- Density: 7 atoms
- Members: atom-0058, atom-0134, atom-2276, atom-2280, atom-2344, atom-2504, atom-2556

### C-49 — company / reverse-engineering (7 atoms)
- Dimension: **company**
- Topic tag: **reverse-engineering**
- Density: 7 atoms
- Members: atom-0132, atom-0133, atom-0448, atom-0667, atom-0938, atom-0984, atom-1129

### C-50 — company / platform (7 atoms)
- Dimension: **company**
- Topic tag: **platform**
- Density: 7 atoms
- Members: atom-0233, atom-0263, atom-0435, atom-0436, atom-0797, atom-0822, atom-1292

### C-51 — money / pricing (7 atoms)
- Dimension: **money**
- Topic tag: **pricing**
- Density: 7 atoms
- Members: atom-0314, atom-0583, atom-2185, atom-2187, atom-2188, atom-2190, atom-2677

### C-52 — base / meta (7 atoms)
- Dimension: **base**
- Topic tag: **meta**
- Density: 7 atoms
- Members: atom-0367, atom-1620, atom-1682, atom-1718, atom-1997, atom-2243, atom-2485

### C-53 — company / website (7 atoms)
- Dimension: **company**
- Topic tag: **website**
- Density: 7 atoms
- Members: atom-0376, atom-0495, atom-0995, atom-2066, atom-2360, atom-2453, atom-2462

### C-54 — relationships / networking (7 atoms)
- Dimension: **relationships**
- Topic tag: **networking**
- Density: 7 atoms
- Members: atom-0397, atom-0398, atom-0460, atom-0894, atom-0895, atom-0896, atom-0950

### C-55 — life / dashboard (7 atoms)
- Dimension: **life**
- Topic tag: **dashboard**
- Density: 7 atoms
- Members: atom-0419, atom-0428, atom-0915, atom-0924, atom-1169, atom-1185, atom-1499

### C-56 — money / target (7 atoms)
- Dimension: **money**
- Topic tag: **target**
- Density: 7 atoms
- Members: atom-0497, atom-0565, atom-2181, atom-2182, atom-2186, atom-2239, atom-2371

### C-57 — company / bon-multi (7 atoms)
- Dimension: **company**
- Topic tag: **bon-multi**
- Density: 7 atoms
- Members: atom-1153, atom-1164, atom-1202, atom-1260, atom-1326, atom-1331, atom-1475

### C-58 — base / q-found (7 atoms)
- Dimension: **base**
- Topic tag: **q-found**
- Density: 7 atoms
- Members: atom-1194, atom-1212, atom-1255, atom-1311, atom-1360, atom-1390, atom-1398

### C-59 — base / b-under (7 atoms)
- Dimension: **base**
- Topic tag: **b-under**
- Density: 7 atoms
- Members: atom-1222, atom-1253, atom-1305, atom-1312, atom-1316, atom-1514, atom-1525

### C-60 — company / op-brand (7 atoms)
- Dimension: **company**
- Topic tag: **op-brand**
- Density: 7 atoms
- Members: atom-1245, atom-1275, atom-1365, atom-1472, atom-1478, atom-1505, atom-1531

### C-61 — company / meta (7 atoms)
- Dimension: **company**
- Topic tag: **meta**
- Density: 7 atoms
- Members: atom-1606, atom-1647, atom-1683, atom-1737, atom-1756, atom-2483, atom-2488

### C-62 — philosophy / bet (7 atoms)
- Dimension: **philosophy**
- Topic tag: **bet**
- Density: 7 atoms
- Members: atom-1923, atom-1930, atom-1933, atom-1938, atom-1942, atom-1947, atom-1964

### C-63 — base / strategizing (7 atoms)
- Dimension: **base**
- Topic tag: **strategizing**
- Density: 7 atoms
- Members: atom-2505, atom-2510, atom-2615, atom-2659, atom-2697, atom-2734, atom-3426

### C-64 — company / open-source (6 atoms)
- Dimension: **company**
- Topic tag: **open-source**
- Density: 6 atoms
- Members: atom-0034, atom-0411, atom-0413, atom-0828, atom-0908, atom-0910

### C-65 — base / writing (6 atoms)
- Dimension: **base**
- Topic tag: **writing**
- Density: 6 atoms
- Members: atom-0047, atom-0048, atom-0049, atom-0614, atom-1103, atom-1104

### C-66 — philosophy / vision (6 atoms)
- Dimension: **philosophy**
- Topic tag: **vision**
- Density: 6 atoms
- Members: atom-0076, atom-0079, atom-0320, atom-0636, atom-1122, atom-3525

### C-67 — company / leverage (6 atoms)
- Dimension: **company**
- Topic tag: **leverage**
- Density: 6 atoms
- Members: atom-0083, atom-0084, atom-0202, atom-0203, atom-0338, atom-0339

### C-68 — base / information-discipline (6 atoms)
- Dimension: **base**
- Topic tag: **information-discipline**
- Density: 6 atoms
- Members: atom-0109, atom-0227, atom-0758, atom-0808, atom-1119, atom-1407

### C-69 — base / tools (6 atoms)
- Dimension: **base**
- Topic tag: **tools**
- Density: 6 atoms
- Members: atom-0113, atom-0524, atom-1021, atom-2062, atom-2900, atom-3237

### C-70 — company / attention (6 atoms)
- Dimension: **company**
- Topic tag: **attention**
- Density: 6 atoms
- Members: atom-0153, atom-0154, atom-0236, atom-0237, atom-0688, atom-1435

### C-71 — base / karpathy (6 atoms)
- Dimension: **base**
- Topic tag: **karpathy**
- Density: 6 atoms
- Members: atom-0171, atom-2149, atom-2202, atom-3575, atom-3576, atom-3625

### C-72 — community / club (6 atoms)
- Dimension: **community**
- Topic tag: **club**
- Density: 6 atoms
- Members: atom-0204, atom-0205, atom-0207, atom-0732, atom-2080, atom-2415

### C-73 — company / delegation (6 atoms)
- Dimension: **company**
- Topic tag: **delegation**
- Density: 6 atoms
- Members: atom-0219, atom-0221, atom-0433, atom-0753, atom-0754, atom-0927

### C-74 — company / product (6 atoms)
- Dimension: **company**
- Topic tag: **product**
- Density: 6 atoms
- Members: atom-0229, atom-0294, atom-0328, atom-0395, atom-0396, atom-0430

### C-75 — community / icp (6 atoms)
- Dimension: **community**
- Topic tag: **icp**
- Density: 6 atoms
- Members: atom-0279, atom-0282, atom-1131, atom-2291, atom-2306, atom-2339

### C-76 — money / investment (6 atoms)
- Dimension: **money**
- Topic tag: **investment**
- Density: 6 atoms
- Members: atom-0300, atom-0302, atom-0304, atom-0306, atom-0818, atom-1589

### C-77 — company / accenture (6 atoms)
- Dimension: **company**
- Topic tag: **accenture**
- Density: 6 atoms
- Members: atom-0329, atom-0330, atom-0831, atom-0832, atom-0833, atom-1233

### C-78 — life / metrics (6 atoms)
- Dimension: **life**
- Topic tag: **metrics**
- Density: 6 atoms
- Members: atom-0372, atom-0373, atom-0552, atom-0678, atom-0874, atom-1411

### C-79 — life / self-management (6 atoms)
- Dimension: **life**
- Topic tag: **self-management**
- Density: 6 atoms
- Members: atom-0473, atom-0474, atom-0975, atom-0976, atom-1401, atom-1414

### C-80 — money / revenue-share (6 atoms)
- Dimension: **money**
- Topic tag: **revenue-share**
- Density: 6 atoms
- Members: atom-0482, atom-0827, atom-0878, atom-2237, atom-2351, atom-3564

### C-81 — life / focus (6 atoms)
- Dimension: **life**
- Topic tag: **focus**
- Density: 6 atoms
- Members: atom-0526, atom-0527, atom-1422, atom-2023, atom-2045, atom-2168

### C-82 — community / symbiosis (6 atoms)
- Dimension: **community**
- Topic tag: **symbiosis**
- Density: 6 atoms
- Members: atom-0546, atom-1047, atom-1170, atom-1366, atom-1380, atom-2252

### C-83 — money / investment-fund (6 atoms)
- Dimension: **money**
- Topic tag: **investment-fund**
- Density: 6 atoms
- Members: atom-0816, atom-1706, atom-2150, atom-2161, atom-2231, atom-2407

### C-84 — relationships / op-rel (6 atoms)
- Dimension: **relationships**
- Topic tag: **op-rel**
- Density: 6 atoms
- Members: atom-1190, atom-1290, atom-1335, atom-1370, atom-1383, atom-1392

### C-85 — company / op-part (6 atoms)
- Dimension: **company**
- Topic tag: **op-part**
- Density: 6 atoms
- Members: atom-1271, atom-1277, atom-1286, atom-1287, atom-1296, atom-1322

### C-86 — money / bet (6 atoms)
- Dimension: **money**
- Topic tag: **bet**
- Density: 6 atoms
- Members: atom-1919, atom-1928, atom-1953, atom-1956, atom-1961, atom-2349

### C-87 — company / dach (6 atoms)
- Dimension: **company**
- Topic tag: **dach**
- Density: 6 atoms
- Members: atom-2593, atom-2932, atom-3045, atom-3152, atom-3289, atom-3561

### C-88 — base / lang (6 atoms)
- Dimension: **base**
- Topic tag: **lang**
- Density: 6 atoms
- Members: atom-2926, atom-2928, atom-2929, atom-2936, atom-2958, atom-2985

### C-89 — base / open-item (6 atoms)
- Dimension: **base**
- Topic tag: **open-item**
- Density: 6 atoms
- Members: atom-3087, atom-3090, atom-3102, atom-3104, atom-3105, atom-3114

### C-90 — base / d3 (6 atoms)
- Dimension: **base**
- Topic tag: **d3**
- Density: 6 atoms
- Members: atom-3097, atom-3313, atom-3315, atom-3319, atom-3388, atom-3413

### C-91 — base / innovation (6 atoms)
- Dimension: **base**
- Topic tag: **innovation**
- Density: 6 atoms
- Members: atom-3244, atom-3247, atom-3249, atom-3256, atom-3276, atom-3328

### C-92 — company / ai (5 atoms)
- Dimension: **company**
- Topic tag: **ai**
- Density: 5 atoms
- Members: atom-0010, atom-0071, atom-0111, atom-0130, atom-0296

### C-93 — company / offer (5 atoms)
- Dimension: **company**
- Topic tag: **offer**
- Density: 5 atoms
- Members: atom-0011, atom-0028, atom-0101, atom-0181, atom-0446

### C-94 — company / review (5 atoms)
- Dimension: **company**
- Topic tag: **review**
- Density: 5 atoms
- Members: atom-0019, atom-2269, atom-2960, atom-2990, atom-3131

### C-95 — philosophy / faith (5 atoms)
- Dimension: **philosophy**
- Topic tag: **faith**
- Density: 5 atoms
- Members: atom-0030, atom-0031, atom-0033, atom-2274, atom-2437

### C-96 — base / thinking (5 atoms)
- Dimension: **base**
- Topic tag: **thinking**
- Density: 5 atoms
- Members: atom-0039, atom-0128, atom-0463, atom-0662, atom-0960

### C-97 — base / speed (5 atoms)
- Dimension: **base**
- Topic tag: **speed**
- Density: 5 atoms
- Members: atom-0040, atom-0405, atom-0902, atom-1518, atom-2248

### C-98 — company / agency (5 atoms)
- Dimension: **company**
- Topic tag: **agency**
- Density: 5 atoms
- Members: atom-0100, atom-0819, atom-1241, atom-2680, atom-2853

### C-99 — base / learning (5 atoms)
- Dimension: **base**
- Topic tag: **learning**
- Density: 5 atoms
- Members: atom-0120, atom-0209, atom-0387, atom-0388, atom-0539

### C-100 — base / stack (5 atoms)
- Dimension: **base**
- Topic tag: **stack**
- Density: 5 atoms
- Members: atom-0136, atom-0137, atom-0138, atom-1178, atom-2345

### C-101 — base / workflow (5 atoms)
- Dimension: **base**
- Topic tag: **workflow**
- Density: 5 atoms
- Members: atom-0140, atom-0404, atom-0673, atom-0898, atom-2015

### C-102 — base / cognitive-architecture (5 atoms)
- Dimension: **base**
- Topic tag: **cognitive-architecture**
- Density: 5 atoms
- Members: atom-0208, atom-0341, atom-0734, atom-0843, atom-0920

### C-103 — philosophy / engineering-thinking (5 atoms)
- Dimension: **philosophy**
- Topic tag: **engineering-thinking**
- Density: 5 atoms
- Members: atom-0242, atom-0769, atom-1191, atom-1339, atom-1400

### C-104 — philosophy / value (5 atoms)
- Dimension: **philosophy**
- Topic tag: **value**
- Density: 5 atoms
- Members: atom-0364, atom-0389, atom-1834, atom-1845, atom-1877

### C-105 — philosophy / myth (5 atoms)
- Dimension: **philosophy**
- Topic tag: **myth**
- Density: 5 atoms
- Members: atom-0374, atom-0375, atom-0875, atom-2258, atom-2424

### C-106 — base / quality (5 atoms)
- Dimension: **base**
- Topic tag: **quality**
- Density: 5 atoms
- Members: atom-0384, atom-0829, atom-0830, atom-0884, atom-2313

### C-107 — company / predator (5 atoms)
- Dimension: **company**
- Topic tag: **predator**
- Density: 5 atoms
- Members: atom-0445, atom-0987, atom-1106, atom-1108, atom-1572

### C-108 — life / rules (5 atoms)
- Dimension: **life**
- Topic tag: **rules**
- Density: 5 atoms
- Members: atom-0466, atom-0509, atom-0510, atom-1005, atom-1500

### C-109 — life / notion (5 atoms)
- Dimension: **life**
- Topic tag: **notion**
- Density: 5 atoms
- Members: atom-0481, atom-0626, atom-1176, atom-1206, atom-3187

### C-110 — base / leverage (5 atoms)
- Dimension: **base**
- Topic tag: **leverage**
- Density: 5 atoms
- Members: atom-0841, atom-0842, atom-1149, atom-1591, atom-1608

### C-111 — base / pipeline (5 atoms)
- Dimension: **base**
- Topic tag: **pipeline**
- Density: 5 atoms
- Members: atom-0919, atom-1272, atom-1385, atom-1412, atom-2742

### C-112 — base / gem (5 atoms)
- Dimension: **base**
- Topic tag: **gem**
- Density: 5 atoms
- Members: atom-1165, atom-1225, atom-1278, atom-1346, atom-1510

### C-113 — life / bon-dec (5 atoms)
- Dimension: **life**
- Topic tag: **bon-dec**
- Density: 5 atoms
- Members: atom-1291, atom-1356, atom-1359, atom-1373, atom-1491

### C-114 — base / bon-dec (5 atoms)
- Dimension: **base**
- Topic tag: **bon-dec**
- Density: 5 atoms
- Members: atom-1333, atom-1425, atom-1438, atom-1444, atom-1469

### C-115 — life / bon-other (5 atoms)
- Dimension: **life**
- Topic tag: **bon-other**
- Density: 5 atoms
- Members: atom-1423, atom-1462, atom-1504, atom-1509, atom-1512

### C-116 — base / dependency (5 atoms)
- Dimension: **base**
- Topic tag: **dependency**
- Density: 5 atoms
- Members: atom-1975, atom-1977, atom-1984, atom-1990, atom-1993

### C-117 — company / alpha (5 atoms)
- Dimension: **company**
- Topic tag: **alpha**
- Density: 5 atoms
- Members: atom-2492, atom-2493, atom-2497, atom-2513, atom-2580

### C-118 — base / alpha (5 atoms)
- Dimension: **base**
- Topic tag: **alpha**
- Density: 5 atoms
- Members: atom-2502, atom-2519, atom-2548, atom-2591, atom-2809

### C-119 — company / chr (5 atoms)
- Dimension: **company**
- Topic tag: **chr**
- Density: 5 atoms
- Members: atom-2514, atom-2896, atom-2921, atom-2923, atom-2962

### C-120 — base / alphas (5 atoms)
- Dimension: **base**
- Topic tag: **alphas**
- Density: 5 atoms
- Members: atom-2575, atom-3252, atom-3356, atom-3374, atom-3604

### C-121 — base / fpf-steward (5 atoms)
- Dimension: **base**
- Topic tag: **fpf-steward**
- Density: 5 atoms
- Members: atom-2629, atom-2637, atom-3324, atom-3379, atom-3421

### C-122 — base / fpf (5 atoms)
- Dimension: **base**
- Topic tag: **fpf**
- Density: 5 atoms
- Members: atom-2644, atom-2803, atom-2808, atom-2814, atom-3423

### C-123 — base / adr (5 atoms)
- Dimension: **base**
- Topic tag: **adr**
- Density: 5 atoms
- Members: atom-2657, atom-3174, atom-3250, atom-3325, atom-3400

### C-124 — base / eu-ai-act (5 atoms)
- Dimension: **base**
- Topic tag: **eu-ai-act**
- Density: 5 atoms
- Members: atom-2956, atom-2967, atom-2969, atom-2971, atom-3486

### C-125 — base / hard-reverse (5 atoms)
- Dimension: **base**
- Topic tag: **hard-reverse**
- Density: 5 atoms
- Members: atom-3019, atom-3023, atom-3024, atom-3030, atom-3033

### C-126 — base / d9 (5 atoms)
- Dimension: **base**
- Topic tag: **d9**
- Density: 5 atoms
- Members: atom-3044, atom-3266, atom-3288, atom-3308, atom-3399

### C-127 — base / rebuild (5 atoms)
- Dimension: **base**
- Topic tag: **rebuild**
- Density: 5 atoms
- Members: atom-3079, atom-3089, atom-3094, atom-3100, atom-3101

### C-128 — base / d2 (5 atoms)
- Dimension: **base**
- Topic tag: **d2**
- Density: 5 atoms
- Members: atom-3088, atom-3343, atom-3401, atom-3411, atom-3420

### C-129 — base / d1 (5 atoms)
- Dimension: **base**
- Topic tag: **d1**
- Density: 5 atoms
- Members: atom-3092, atom-3271, atom-3322, atom-3330, atom-3417

### C-130 — company / competition (4 atoms)
- Dimension: **company**
- Topic tag: **competition**
- Density: 4 atoms
- Members: atom-0013, atom-0112, atom-0267, atom-0449

### C-131 — community / trust (4 atoms)
- Dimension: **community**
- Topic tag: **trust**
- Density: 4 atoms
- Members: atom-0023, atom-0335, atom-1039, atom-1841

### C-132 — community / platform (4 atoms)
- Dimension: **community**
- Topic tag: **platform**
- Density: 4 atoms
- Members: atom-0035, atom-0434, atom-1641, atom-2043

### C-133 — company / phase-1 (4 atoms)
- Dimension: **company**
- Topic tag: **phase-1**
- Density: 4 atoms
- Members: atom-0060, atom-2478, atom-2870, atom-2919

### C-134 — philosophy / worldview (4 atoms)
- Dimension: **philosophy**
- Topic tag: **worldview**
- Density: 4 atoms
- Members: atom-0089, atom-0559, atom-0641, atom-1054

### C-135 — base / notebooklm (4 atoms)
- Dimension: **base**
- Topic tag: **notebooklm**
- Density: 4 atoms
- Members: atom-0105, atom-0106, atom-0648, atom-1391

### C-136 — base / skills (4 atoms)
- Dimension: **base**
- Topic tag: **skills**
- Density: 4 atoms
- Members: atom-0108, atom-3202, atom-3209, atom-3605

### C-137 — company / youtube (4 atoms)
- Dimension: **company**
- Topic tag: **youtube**
- Density: 4 atoms
- Members: atom-0149, atom-0616, atom-0617, atom-1105

### C-138 — life / audit (4 atoms)
- Dimension: **life**
- Topic tag: **audit**
- Density: 4 atoms
- Members: atom-0162, atom-0163, atom-0624, atom-1496

### C-139 — life / time-audit (4 atoms)
- Dimension: **life**
- Topic tag: **time-audit**
- Density: 4 atoms
- Members: atom-0167, atom-0168, atom-0701, atom-1494

### C-140 — life / cannabis (4 atoms)
- Dimension: **life**
- Topic tag: **cannabis**
- Density: 4 atoms
- Members: atom-0193, atom-0194, atom-0722, atom-0723

### C-141 — company / ecosystem (4 atoms)
- Dimension: **company**
- Topic tag: **ecosystem**
- Density: 4 atoms
- Members: atom-0238, atom-0239, atom-1295, atom-2568

### C-142 — philosophy / engineering-faith (4 atoms)
- Dimension: **philosophy**
- Topic tag: **engineering-faith**
- Density: 4 atoms
- Members: atom-0241, atom-0766, atom-0767, atom-3585

### C-143 — base / experiment (4 atoms)
- Dimension: **base**
- Topic tag: **experiment**
- Density: 4 atoms
- Members: atom-0273, atom-0525, atom-1578, atom-2420

### C-144 — community / ecosystem (4 atoms)
- Dimension: **community**
- Topic tag: **ecosystem**
- Density: 4 atoms
- Members: atom-0313, atom-0765, atom-1674, atom-2914

### C-145 — company / quality (4 atoms)
- Dimension: **company**
- Topic tag: **quality**
- Density: 4 atoms
- Members: atom-0326, atom-0327, atom-2253, atom-2388

### C-146 — company / role (4 atoms)
- Dimension: **company**
- Topic tag: **role**
- Density: 4 atoms
- Members: atom-0349, atom-2400, atom-2848, atom-2943

### C-147 — company / scaling (4 atoms)
- Dimension: **company**
- Topic tag: **scaling**
- Density: 4 atoms
- Members: atom-0408, atom-0905, atom-1143, atom-1328

### C-148 — company / experiment (4 atoms)
- Dimension: **company**
- Topic tag: **experiment**
- Density: 4 atoms
- Members: atom-0550, atom-0777, atom-2261, atom-2353

### C-149 — base / second-brain (4 atoms)
- Dimension: **base**
- Topic tag: **second-brain**
- Density: 4 atoms
- Members: atom-0609, atom-1098, atom-1227, atom-3603

### C-150 — life / weekly-review (4 atoms)
- Dimension: **life**
- Topic tag: **weekly-review**
- Density: 4 atoms
- Members: atom-0612, atom-0613, atom-0681, atom-1102

### C-151 — company / pricing (4 atoms)
- Dimension: **company**
- Topic tag: **pricing**
- Density: 4 atoms
- Members: atom-0717, atom-1075, atom-1085, atom-2865

### C-152 — money / sales (4 atoms)
- Dimension: **money**
- Topic tag: **sales**
- Density: 4 atoms
- Members: atom-0943, atom-2256, atom-2308, atom-2309

### C-153 — company / producer-center (4 atoms)
- Dimension: **company**
- Topic tag: **producer-center**
- Density: 4 atoms
- Members: atom-0945, atom-0947, atom-1748, atom-2298

### C-154 — company / case-study (4 atoms)
- Dimension: **company**
- Topic tag: **case-study**
- Density: 4 atoms
- Members: atom-0970, atom-0971, atom-0972, atom-0973

### C-155 — company / q-found (4 atoms)
- Dimension: **company**
- Topic tag: **q-found**
- Density: 4 atoms
- Members: atom-1211, atom-1374, atom-1399, atom-1417

### C-156 — company / b-fork (4 atoms)
- Dimension: **company**
- Topic tag: **b-fork**
- Density: 4 atoms
- Members: atom-1218, atom-1262, atom-1293, atom-1317

### C-157 — community / adventurers (4 atoms)
- Dimension: **community**
- Topic tag: **adventurers**
- Density: 4 atoms
- Members: atom-1243, atom-1666, atom-2277, atom-2370

### C-158 — company / pattern (4 atoms)
- Dimension: **company**
- Topic tag: **pattern**
- Density: 4 atoms
- Members: atom-1251, atom-1288, atom-1304, atom-1308

### C-159 — philosophy / bon-other (4 atoms)
- Dimension: **philosophy**
- Topic tag: **bon-other**
- Density: 4 atoms
- Members: atom-1320, atom-1325, atom-1471, atom-1529

### C-160 — company / bon-other (4 atoms)
- Dimension: **company**
- Topic tag: **bon-other**
- Density: 4 atoms
- Members: atom-1321, atom-1450, atom-1470, atom-1507

### C-161 — base / documentation (4 atoms)
- Dimension: **base**
- Topic tag: **documentation**
- Density: 4 atoms
- Members: atom-1485, atom-2074, atom-2133, atom-2167

### C-162 — philosophy / hottest-transcript (4 atoms)
- Dimension: **philosophy**
- Topic tag: **hottest-transcript**
- Density: 4 atoms
- Members: atom-1538, atom-1539, atom-1541, atom-1542

### C-163 — company / hypothesis (4 atoms)
- Dimension: **company**
- Topic tag: **hypothesis**
- Density: 4 atoms
- Members: atom-1588, atom-2643, atom-2829, atom-3295

### C-164 — company / taskrabbit (4 atoms)
- Dimension: **company**
- Topic tag: **taskrabbit**
- Density: 4 atoms
- Members: atom-1697, atom-2044, atom-2207, atom-3534

### C-165 — company / agents (4 atoms)
- Dimension: **company**
- Topic tag: **agents**
- Density: 4 atoms
- Members: atom-1792, atom-2490, atom-2653, atom-3610

### C-166 — philosophy / principle (4 atoms)
- Dimension: **philosophy**
- Topic tag: **principle**
- Density: 4 atoms
- Members: atom-1905, atom-1907, atom-1916, atom-1917

### C-167 — base / bet (4 atoms)
- Dimension: **base**
- Topic tag: **bet**
- Density: 4 atoms
- Members: atom-1922, atom-1929, atom-1958, atom-1960

### C-168 — money / tension (4 atoms)
- Dimension: **money**
- Topic tag: **tension**
- Density: 4 atoms
- Members: atom-1972, atom-2214, atom-2354, atom-2396

### C-169 — brand / patents (4 atoms)
- Dimension: **brand**
- Topic tag: **patents**
- Density: 4 atoms
- Members: atom-2027, atom-2057, atom-2063, atom-2105

### C-170 — money / revenue (4 atoms)
- Dimension: **money**
- Topic tag: **revenue**
- Density: 4 atoms
- Members: atom-2047, atom-2236, atom-2238, atom-3526

### C-171 — base / sop (4 atoms)
- Dimension: **base**
- Topic tag: **sop**
- Density: 4 atoms
- Members: atom-2078, atom-2079, atom-2172, atom-2397

### C-172 — company / stripe (4 atoms)
- Dimension: **company**
- Topic tag: **stripe**
- Density: 4 atoms
- Members: atom-2081, atom-2325, atom-2363, atom-3156

### C-173 — company / direction (4 atoms)
- Dimension: **company**
- Topic tag: **direction**
- Density: 4 atoms
- Members: atom-2498, atom-2543, atom-2640, atom-3491

### C-174 — base / creation-graph (4 atoms)
- Dimension: **base**
- Topic tag: **creation-graph**
- Density: 4 atoms
- Members: atom-2512, atom-2579, atom-2755, atom-3574

### C-175 — company / fpf-steward (4 atoms)
- Dimension: **company**
- Topic tag: **fpf-steward**
- Density: 4 atoms
- Members: atom-2515, atom-2759, atom-2872, atom-2876

### C-176 — company / boundary (4 atoms)
- Dimension: **company**
- Topic tag: **boundary**
- Density: 4 atoms
- Members: atom-2544, atom-2772, atom-2895, atom-2961

### C-177 — base / rituals (4 atoms)
- Dimension: **base**
- Topic tag: **rituals**
- Density: 4 atoms
- Members: atom-2562, atom-2912, atom-3353, atom-3578

### C-178 — base / u-types (4 atoms)
- Dimension: **base**
- Topic tag: **u-types**
- Density: 4 atoms
- Members: atom-2569, atom-2606, atom-2633, atom-3274

### C-179 — base / uts (4 atoms)
- Dimension: **base**
- Topic tag: **uts**
- Density: 4 atoms
- Members: atom-2596, atom-2762, atom-3489, atom-3584

### C-180 — base / fpf-spec (4 atoms)
- Dimension: **base**
- Topic tag: **fpf-spec**
- Density: 4 atoms
- Members: atom-2651, atom-2821, atom-3386, atom-3505

### C-181 — base / mc3 (4 atoms)
- Dimension: **base**
- Topic tag: **mc3**
- Density: 4 atoms
- Members: atom-2662, atom-3287, atom-3339, atom-3425

### C-182 — company / project (4 atoms)
- Dimension: **company**
- Topic tag: **project**
- Density: 4 atoms
- Members: atom-2695, atom-3182, atom-3185, atom-3197

### C-183 — company / viewpoint-bundle (4 atoms)
- Dimension: **company**
- Topic tag: **viewpoint-bundle**
- Density: 4 atoms
- Members: atom-2873, atom-2917, atom-3120, atom-3403

### C-184 — company / override (4 atoms)
- Dimension: **company**
- Topic tag: **override**
- Density: 4 atoms
- Members: atom-2999, atom-3020, atom-3028, atom-3050

### C-185 — base / d5 (4 atoms)
- Dimension: **base**
- Topic tag: **d5**
- Density: 4 atoms
- Members: atom-3113, atom-3294, atom-3298, atom-3387

### C-186 — base / voice-notes (4 atoms)
- Dimension: **base**
- Topic tag: **voice-notes**
- Density: 4 atoms
- Members: atom-3208, atom-3229, atom-3233, atom-3594

### C-187 — base / mc1 (4 atoms)
- Dimension: **base**
- Topic tag: **mc1**
- Density: 4 atoms
- Members: atom-3259, atom-3363, atom-3392, atom-3414

### C-188 — base / frontmatter (4 atoms)
- Dimension: **base**
- Topic tag: **frontmatter**
- Density: 4 atoms
- Members: atom-3260, atom-3307, atom-3321, atom-3395

### C-189 — base / mc4 (4 atoms)
- Dimension: **base**
- Topic tag: **mc4**
- Density: 4 atoms
- Members: atom-3286, atom-3305, atom-3316, atom-3455

### C-190 — company / market (3 atoms)
- Dimension: **company**
- Topic tag: **market**
- Density: 3 atoms
- Members: atom-0001, atom-0098, atom-2517

### C-191 — company / git (3 atoms)
- Dimension: **company**
- Topic tag: **git**
- Density: 3 atoms
- Members: atom-0006, atom-0017, atom-2263

### C-192 — life / execution (3 atoms)
- Dimension: **life**
- Topic tag: **execution**
- Density: 3 atoms
- Members: atom-0046, atom-2166, atom-2385

### C-193 — philosophy / legacy (3 atoms)
- Dimension: **philosophy**
- Topic tag: **legacy**
- Density: 3 atoms
- Members: atom-0077, atom-0190, atom-0719

### C-194 — base / meta-skills (3 atoms)
- Dimension: **base**
- Topic tag: **meta-skills**
- Density: 3 atoms
- Members: atom-0080, atom-0638, atom-1254

### C-195 — base / ai-assistant (3 atoms)
- Dimension: **base**
- Topic tag: **ai-assistant**
- Density: 3 atoms
- Members: atom-0121, atom-0285, atom-0664

### C-196 — company / pipeline (3 atoms)
- Dimension: **company**
- Topic tag: **pipeline**
- Density: 3 atoms
- Members: atom-0123, atom-0432, atom-2824

### C-197 — company / architecture (3 atoms)
- Dimension: **company**
- Topic tag: **architecture**
- Density: 3 atoms
- Members: atom-0158, atom-0159, atom-2573

### C-198 — base / ai-agents (3 atoms)
- Dimension: **base**
- Topic tag: **ai-agents**
- Density: 3 atoms
- Members: atom-0161, atom-0595, atom-1086

### C-199 — base / crewai (3 atoms)
- Dimension: **base**
- Topic tag: **crewai**
- Density: 3 atoms
- Members: atom-0169, atom-0170, atom-1186

### C-200 — life / automation (3 atoms)
- Dimension: **life**
- Topic tag: **automation**
- Density: 3 atoms
- Members: atom-0174, atom-0707, atom-1402

### C-201 — company / mvp (3 atoms)
- Dimension: **company**
- Topic tag: **mvp**
- Density: 3 atoms
- Members: atom-0185, atom-0277, atom-0431

### C-202 — company / blog (3 atoms)
- Dimension: **company**
- Topic tag: **blog**
- Density: 3 atoms
- Members: atom-0188, atom-0189, atom-0718

### C-203 — life / checklists (3 atoms)
- Dimension: **life**
- Topic tag: **checklists**
- Density: 3 atoms
- Members: atom-0198, atom-0199, atom-0727

### C-204 — base / project-launch (3 atoms)
- Dimension: **base**
- Topic tag: **project-launch**
- Density: 3 atoms
- Members: atom-0200, atom-0729, atom-1268

### C-205 — community / family (3 atoms)
- Dimension: **community**
- Topic tag: **family**
- Density: 3 atoms
- Members: atom-0206, atom-1418, atom-1833

### C-206 — life / decomposition (3 atoms)
- Dimension: **life**
- Topic tag: **decomposition**
- Density: 3 atoms
- Members: atom-0217, atom-0752, atom-1216

### C-207 — base / cycle (3 atoms)
- Dimension: **base**
- Topic tag: **cycle**
- Density: 3 atoms
- Members: atom-0225, atom-0226, atom-1205

### C-208 — base / audit (3 atoms)
- Dimension: **base**
- Topic tag: **audit**
- Density: 3 atoms
- Members: atom-0246, atom-2816, atom-2827

### C-209 — money / capital (3 atoms)
- Dimension: **money**
- Topic tag: **capital**
- Density: 3 atoms
- Members: atom-0251, atom-0252, atom-0623

### C-210 — philosophy / founder (3 atoms)
- Dimension: **philosophy**
- Topic tag: **founder**
- Density: 3 atoms
- Members: atom-0256, atom-0781, atom-1860

### C-211 — money / game-center (3 atoms)
- Dimension: **money**
- Topic tag: **game-center**
- Density: 3 atoms
- Members: atom-0259, atom-0783, atom-1519

### C-212 — company / hr (3 atoms)
- Dimension: **company**
- Topic tag: **hr**
- Density: 3 atoms
- Members: atom-0276, atom-0794, atom-0959

### C-213 — base / focus (3 atoms)
- Dimension: **base**
- Topic tag: **focus**
- Density: 3 atoms
- Members: atom-0289, atom-1024, atom-1025

### C-214 — company / pitch (3 atoms)
- Dimension: **company**
- Topic tag: **pitch**
- Density: 3 atoms
- Members: atom-0316, atom-0485, atom-0601

### C-215 — company / geo (3 atoms)
- Dimension: **company**
- Topic tag: **geo**
- Density: 3 atoms
- Members: atom-0318, atom-2336, atom-3529

### C-216 — base / template (3 atoms)
- Dimension: **base**
- Topic tag: **template**
- Density: 3 atoms
- Members: atom-0342, atom-0422, atom-0512

### C-217 — company / management (3 atoms)
- Dimension: **company**
- Topic tag: **management**
- Density: 3 atoms
- Members: atom-0361, atom-0362, atom-0863

### C-218 — life / mindset (3 atoms)
- Dimension: **life**
- Topic tag: **mindset**
- Density: 3 atoms
- Members: atom-0379, atom-0380, atom-1006

### C-219 — life / tracking (3 atoms)
- Dimension: **life**
- Topic tag: **tracking**
- Density: 3 atoms
- Members: atom-0393, atom-0551, atom-1051

### C-220 — base / information (3 atoms)
- Dimension: **base**
- Topic tag: **information**
- Density: 3 atoms
- Members: atom-0399, atom-0897, atom-2300

### C-221 — philosophy / elite (3 atoms)
- Dimension: **philosophy**
- Topic tag: **elite**
- Density: 3 atoms
- Members: atom-0403, atom-0558, atom-1053

### C-222 — company / strategy (3 atoms)
- Dimension: **company**
- Topic tag: **strategy**
- Density: 3 atoms
- Members: atom-0417, atom-0605, atom-0913

### C-223 — base / automation (3 atoms)
- Dimension: **base**
- Topic tag: **automation**
- Density: 3 atoms
- Members: atom-0423, atom-1020, atom-2049

### C-224 — money / partnership (3 atoms)
- Dimension: **money**
- Topic tag: **partnership**
- Density: 3 atoms
- Members: atom-0484, atom-0891, atom-1692

### C-225 — community / trials (3 atoms)
- Dimension: **community**
- Topic tag: **trials**
- Density: 3 atoms
- Members: atom-0540, atom-0541, atom-1038

### C-226 — company / simulators (3 atoms)
- Dimension: **company**
- Topic tag: **simulators**
- Density: 3 atoms
- Members: atom-0561, atom-1055, atom-1217

### C-227 — community / truth (3 atoms)
- Dimension: **community**
- Topic tag: **truth**
- Density: 3 atoms
- Members: atom-0563, atom-0564, atom-1056

### C-228 — base / digital-clone (3 atoms)
- Dimension: **base**
- Topic tag: **digital-clone**
- Density: 3 atoms
- Members: atom-0571, atom-1061, atom-1062

### C-229 — company / twitter (3 atoms)
- Dimension: **company**
- Topic tag: **twitter**
- Density: 3 atoms
- Members: atom-0573, atom-1063, atom-1064

### C-230 — life / morning-ritual (3 atoms)
- Dimension: **life**
- Topic tag: **morning-ritual**
- Density: 3 atoms
- Members: atom-0580, atom-0581, atom-1071

### C-231 — company / c-suite (3 atoms)
- Dimension: **company**
- Topic tag: **c-suite**
- Density: 3 atoms
- Members: atom-0592, atom-0594, atom-3280

### C-232 — money / assets (3 atoms)
- Dimension: **money**
- Topic tag: **assets**
- Density: 3 atoms
- Members: atom-0598, atom-0599, atom-1452

### C-233 — life / life-as-game (3 atoms)
- Dimension: **life**
- Topic tag: **life-as-game**
- Density: 3 atoms
- Members: atom-0625, atom-1174, atom-1687

### C-234 — company / one-person-company (3 atoms)
- Dimension: **company**
- Topic tag: **one-person-company**
- Density: 3 atoms
- Members: atom-0635, atom-0665, atom-1434

### C-235 — life / ritual (3 atoms)
- Dimension: **life**
- Topic tag: **ritual**
- Density: 3 atoms
- Members: atom-0748, atom-2118, atom-2176

### C-236 — life / future-self (3 atoms)
- Dimension: **life**
- Topic tag: **future-self**
- Density: 3 atoms
- Members: atom-0868, atom-1853, atom-2226

### C-237 — base / sequential-focus (3 atoms)
- Dimension: **base**
- Topic tag: **sequential-focus**
- Density: 3 atoms
- Members: atom-0872, atom-0873, atom-1415

### C-238 — company / platform-logic (3 atoms)
- Dimension: **company**
- Topic tag: **platform-logic**
- Density: 3 atoms
- Members: atom-0930, atom-0931, atom-1256

### C-239 — base / tool (3 atoms)
- Dimension: **base**
- Topic tag: **tool**
- Density: 3 atoms
- Members: atom-1022, atom-1023, atom-1663

### C-240 — philosophy / values (3 atoms)
- Dimension: **philosophy**
- Topic tag: **values**
- Density: 3 atoms
- Members: atom-1060, atom-1368, atom-1513

### C-241 — company / brand (3 atoms)
- Dimension: **company**
- Topic tag: **brand**
- Density: 3 atoms
- Members: atom-1084, atom-2271, atom-2343

### C-242 — life / unclear (3 atoms)
- Dimension: **life**
- Topic tag: **unclear**
- Density: 3 atoms
- Members: atom-1133, atom-1134, atom-1135

### C-243 — base / voice-memos (3 atoms)
- Dimension: **base**
- Topic tag: **voice-memos**
- Density: 3 atoms
- Members: atom-1139, atom-3535, atom-3541

### C-244 — base / migration (3 atoms)
- Dimension: **base**
- Topic tag: **migration**
- Density: 3 atoms
- Members: atom-1140, atom-3263, atom-3478

### C-245 — company / op-rel (3 atoms)
- Dimension: **company**
- Topic tag: **op-rel**
- Density: 3 atoms
- Members: atom-1152, atom-1314, atom-1394

### C-246 — base / q-revert (3 atoms)
- Dimension: **base**
- Topic tag: **q-revert**
- Density: 3 atoms
- Members: atom-1158, atom-1168, atom-1306

### C-247 — base / bon-other (3 atoms)
- Dimension: **base**
- Topic tag: **bon-other**
- Density: 3 atoms
- Members: atom-1183, atom-1238, atom-1451

### C-248 — philosophy / q-found (3 atoms)
- Dimension: **philosophy**
- Topic tag: **q-found**
- Density: 3 atoms
- Members: atom-1221, atom-1352, atom-1381

### C-249 — company / uni-onboard (3 atoms)
- Dimension: **company**
- Topic tag: **uni-onboard**
- Density: 3 atoms
- Members: atom-1276, atom-1284, atom-1302

### C-250 — base / q-simple (3 atoms)
- Dimension: **base**
- Topic tag: **q-simple**
- Density: 3 atoms
- Members: atom-1329, atom-1343, atom-1456

### C-251 — company / conflict (3 atoms)
- Dimension: **company**
- Topic tag: **conflict**
- Density: 3 atoms
- Members: atom-1481, atom-1482, atom-1484

### C-252 — money / metric (3 atoms)
- Dimension: **money**
- Topic tag: **metric**
- Density: 3 atoms
- Members: atom-1532, atom-1533, atom-1535

### C-253 — base / metric (3 atoms)
- Dimension: **base**
- Topic tag: **metric**
- Density: 3 atoms
- Members: atom-1534, atom-3234, atom-3235

### C-254 — company / mckinsey (3 atoms)
- Dimension: **company**
- Topic tag: **mckinsey**
- Density: 3 atoms
- Members: atom-1545, atom-2333, atom-2368

### C-255 — base / anthropic (3 atoms)
- Dimension: **base**
- Topic tag: **anthropic**
- Density: 3 atoms
- Members: atom-1564, atom-2106, atom-3590

### C-256 — company / resources (3 atoms)
- Dimension: **company**
- Topic tag: **resources**
- Density: 3 atoms
- Members: atom-1576, atom-2273, atom-2867

### C-257 — philosophy / power (3 atoms)
- Dimension: **philosophy**
- Topic tag: **power**
- Density: 3 atoms
- Members: atom-1594, atom-1601, atom-2307

### C-258 — company / legal (3 atoms)
- Dimension: **company**
- Topic tag: **legal**
- Density: 3 atoms
- Members: atom-1613, atom-2506, atom-2852

### C-259 — company / wikipedia (3 atoms)
- Dimension: **company**
- Topic tag: **wikipedia**
- Density: 3 atoms
- Members: atom-1621, atom-1650, atom-2414

### C-260 — company / apple (3 atoms)
- Dimension: **company**
- Topic tag: **apple**
- Density: 3 atoms
- Members: atom-1638, atom-2302, atom-2332

### C-261 — community / exchange (3 atoms)
- Dimension: **community**
- Topic tag: **exchange**
- Density: 3 atoms
- Members: atom-1671, atom-1770, atom-1802

### C-262 — company / niches (3 atoms)
- Dimension: **company**
- Topic tag: **niches**
- Density: 3 atoms
- Members: atom-1678, atom-2012, atom-2075

### C-263 — base / concept (3 atoms)
- Dimension: **base**
- Topic tag: **concept**
- Density: 3 atoms
- Members: atom-1715, atom-1803, atom-1810

### C-264 — company / patents (3 atoms)
- Dimension: **company**
- Topic tag: **patents**
- Density: 3 atoms
- Members: atom-1720, atom-2262, atom-2405

### C-265 — base / meta-system (3 atoms)
- Dimension: **base**
- Topic tag: **meta-system**
- Density: 3 atoms
- Members: atom-1769, atom-2145, atom-2163

### C-266 — philosophy / archetypes (3 atoms)
- Dimension: **philosophy**
- Topic tag: **archetypes**
- Density: 3 atoms
- Members: atom-1867, atom-2111, atom-2153

### C-267 — company / holding (3 atoms)
- Dimension: **company**
- Topic tag: **holding**
- Density: 3 atoms
- Members: atom-1871, atom-2017, atom-2234

### C-268 — life / principle (3 atoms)
- Dimension: **life**
- Topic tag: **principle**
- Density: 3 atoms
- Members: atom-1879, atom-1892, atom-1898

### C-269 — life / bet (3 atoms)
- Dimension: **life**
- Topic tag: **bet**
- Density: 3 atoms
- Members: atom-1937, atom-1940, atom-1946

### C-270 — money / escalation (3 atoms)
- Dimension: **money**
- Topic tag: **escalation**
- Density: 3 atoms
- Members: atom-1989, atom-2246, atom-2381

### C-271 — brand / positioning (3 atoms)
- Dimension: **brand**
- Topic tag: **positioning**
- Density: 3 atoms
- Members: atom-2002, atom-2152, atom-2215

### C-272 — life / mercedes (3 atoms)
- Dimension: **life**
- Topic tag: **mercedes**
- Density: 3 atoms
- Members: atom-2005, atom-2233, atom-2323

### C-273 — company / google (3 atoms)
- Dimension: **company**
- Topic tag: **google**
- Density: 3 atoms
- Members: atom-2028, atom-2203, atom-2321

### C-274 — base / security (3 atoms)
- Dimension: **base**
- Topic tag: **security**
- Density: 3 atoms
- Members: atom-2095, atom-2178, atom-2465

### C-275 — money / fortune-500 (3 atoms)
- Dimension: **money**
- Topic tag: **fortune-500**
- Density: 3 atoms
- Members: atom-2098, atom-2232, atom-2410

### C-276 — base / perplexity (3 atoms)
- Dimension: **base**
- Topic tag: **perplexity**
- Density: 3 atoms
- Members: atom-2109, atom-2204, atom-3367

### C-277 — company / team (3 atoms)
- Dimension: **company**
- Topic tag: **team**
- Density: 3 atoms
- Members: atom-2143, atom-2195, atom-2401

### C-278 — company / phased (3 atoms)
- Dimension: **company**
- Topic tag: **phased**
- Density: 3 atoms
- Members: atom-2221, atom-2222, atom-2379

### C-279 — community / kingsman (3 atoms)
- Dimension: **community**
- Topic tag: **kingsman**
- Density: 3 atoms
- Members: atom-2283, atom-2327, atom-2427

### C-280 — base / compute (3 atoms)
- Dimension: **base**
- Topic tag: **compute**
- Density: 3 atoms
- Members: atom-2285, atom-3290, atom-3428

### C-281 — community / secure-network (3 atoms)
- Dimension: **community**
- Topic tag: **secure-network**
- Density: 3 atoms
- Members: atom-2439, atom-2442, atom-3520

### C-282 — company / sku (3 atoms)
- Dimension: **company**
- Topic tag: **sku**
- Density: 3 atoms
- Members: atom-2489, atom-2683, atom-3490

### C-283 — base / role (3 atoms)
- Dimension: **base**
- Topic tag: **role**
- Density: 3 atoms
- Members: atom-2494, atom-2682, atom-3567

### C-284 — base / gamma (3 atoms)
- Dimension: **base**
- Topic tag: **gamma**
- Density: 3 atoms
- Members: atom-2500, atom-2661, atom-3579

### C-285 — base / a14 (3 atoms)
- Dimension: **base**
- Topic tag: **a14**
- Density: 3 atoms
- Members: atom-2509, atom-2741, atom-3599

### C-286 — base / constitution (3 atoms)
- Dimension: **base**
- Topic tag: **constitution**
- Density: 3 atoms
- Members: atom-2511, atom-3158, atom-3306

### C-287 — company / mht (3 atoms)
- Dimension: **company**
- Topic tag: **mht**
- Density: 3 atoms
- Members: atom-2521, atom-2605, atom-2944

### C-288 — company / phase-2a (3 atoms)
- Dimension: **company**
- Topic tag: **phase-2a**
- Density: 3 atoms
- Members: atom-2529, atom-2850, atom-3106

### C-289 — company / eu-ai-act (3 atoms)
- Dimension: **company**
- Topic tag: **eu-ai-act**
- Density: 3 atoms
- Members: atom-2545, atom-2603, atom-3586

### C-290 — base / chr (3 atoms)
- Dimension: **base**
- Topic tag: **chr**
- Density: 3 atoms
- Members: atom-2589, atom-2609, atom-2627

### C-291 — company / ruslan (3 atoms)
- Dimension: **company**
- Topic tag: **ruslan**
- Density: 3 atoms
- Members: atom-2638, atom-2642, atom-3589

### C-292 — base / levchuk (3 atoms)
- Dimension: **base**
- Topic tag: **levchuk**
- Density: 3 atoms
- Members: atom-2650, atom-2654, atom-2815

### C-293 — company / forbidden (3 atoms)
- Dimension: **company**
- Topic tag: **forbidden**
- Density: 3 atoms
- Members: atom-2703, atom-2951, atom-2955

### C-294 — base / git (3 atoms)
- Dimension: **base**
- Topic tag: **git**
- Density: 3 atoms
- Members: atom-2705, atom-2901, atom-2927

### C-295 — base / cost (3 atoms)
- Dimension: **base**
- Topic tag: **cost**
- Density: 3 atoms
- Members: atom-2739, atom-2805, atom-3143

### C-296 — base / oq-06 (3 atoms)
- Dimension: **base**
- Topic tag: **oq-06**
- Density: 3 atoms
- Members: atom-2840, atom-3021, atom-3358

### C-297 — base / ot2 (3 atoms)
- Dimension: **base**
- Topic tag: **ot2**
- Density: 3 atoms
- Members: atom-2845, atom-3415, atom-3460

### C-298 — base / shared (3 atoms)
- Dimension: **base**
- Topic tag: **shared**
- Density: 3 atoms
- Members: atom-2846, atom-3302, atom-3304

### C-299 — company / alphas (3 atoms)
- Dimension: **company**
- Topic tag: **alphas**
- Density: 3 atoms
- Members: atom-2857, atom-2924, atom-2935

### C-300 — company / fpf (3 atoms)
- Dimension: **company**
- Topic tag: **fpf**
- Density: 3 atoms
- Members: atom-2860, atom-3049, atom-3098

### C-301 — company / jetix-fpf (3 atoms)
- Dimension: **company**
- Topic tag: **jetix-fpf**
- Density: 3 atoms
- Members: atom-2871, atom-2982, atom-3061

### C-302 — base / ot5 (3 atoms)
- Dimension: **base**
- Topic tag: **ot5**
- Density: 3 atoms
- Members: atom-2878, atom-3456, atom-3458

### C-303 — company / uts (3 atoms)
- Dimension: **company**
- Topic tag: **uts**
- Density: 3 atoms
- Members: atom-2904, atom-2965, atom-2977

### C-304 — company / p6 (3 atoms)
- Dimension: **company**
- Topic tag: **p6**
- Density: 3 atoms
- Members: atom-2992, atom-3443, atom-3551

### C-305 — company / open-item (3 atoms)
- Dimension: **company**
- Topic tag: **open-item**
- Density: 3 atoms
- Members: atom-3096, atom-3103, atom-3111

### C-306 — base / project (3 atoms)
- Dimension: **base**
- Topic tag: **project**
- Density: 3 atoms
- Members: atom-3180, atom-3184, atom-3194

### C-307 — company / r10 (3 atoms)
- Dimension: **company**
- Topic tag: **r10**
- Density: 3 atoms
- Members: atom-3278, atom-3332, atom-3453

### C-308 — base / chunk-8 (3 atoms)
- Dimension: **base**
- Topic tag: **chunk-8**
- Density: 3 atoms
- Members: atom-3333, atom-3412, atom-3422

### C-309 — company / locked-decision (3 atoms)
- Dimension: **company**
- Topic tag: **locked-decision**
- Density: 3 atoms
- Members: atom-3508, atom-3513, atom-3514

### C-310 — philosophy / locked-decision (3 atoms)
- Dimension: **philosophy**
- Topic tag: **locked-decision**
- Density: 3 atoms
- Members: atom-3512, atom-3515, atom-3517


---

## 3. Gaps (weak coverage)

### 3.1 Dimension gaps (< 20 atoms)

_All dimensions have ≥ 20 atoms. No major dimension gap._

### 3.2 Phase gaps (< 10 atoms)

_All phases have ≥ 10 atoms._

### 3.3 Topic gaps (manual review — см. TENSIONS §Remaining)


- Exit / liquidity / equity structure
- GDPR / AI Act / DE compliance detail
- Recovery / nutrition / sleep (Jetix-life)
- Pricing mechanics beyond €150/час baseline
- Partnership legal structure

---

## 4. Orphans (atoms без relates_to)

Total orphans: **3420** из 3626.

_Orphans — это либо unique insights without near-duplicates (возможно важные) либо noise (возможно park). Manual triage needed._

### Sample (top 100 by high-salience types — principle/bet/hypothesis/concept/tension):

- **atom-0008** `concept` [company/base] — Wiki-driven business (параллель к wiki-driven engineering / Karpathy LLM Wiki)
- **atom-0011** `concept` [company] — Двойной оффер Jetix: защита + нападение (reverse-engineering)
- **atom-0014** `principle` [company] — Jetix фокус: 82% застрявших в Mittelstand, НЕ 6% high performers и НЕ 12% без AI
- **atom-0016** `principle` [company/philosophy] — Ставить на бизнес-логику и экспертизу — они не поглощаются базовыми моделями
- **atom-0017** `concept` [company/community] — Collaborative project versioning — бизнес-проекты как git-репозиторий
- **atom-0018** `principle` [community/base] — Артефакты = first-class objects, не чаты
- **atom-0019** `principle` [company] — Review перед merge — не меняем main пока не согласились
- **atom-0020** `principle` [company] — Ветки как гипотезы: давайте попробуем вот такой подход в отдельной ветке
- **atom-0021** `concept` [community] — Curated community access — курированный допуск в сообщество
- **atom-0022** `principle` [community] — Репутация и вклад — валюта внутри сообщества
- **atom-0023** `principle` [community/relationships] — Доверие по умолчанию внутри сообщества: каждого проверили
- **atom-0027** `concept` [company/philosophy] — Digital sovereignty — цифровой суверенитет клиента, отсутствие vendor lock-in
- **atom-0028** `principle` [company] — Jetix оффер: мы оставляем вам ваш стек под контролем, не делаем lock-in
- **atom-0030** `concept` [philosophy/base] — Engineering faith — вера в результат обоснованная планом и инструментами (план + инструменты + вера)
- **atom-0031** `principle` [philosophy] — Engineering faith противостоит FUD и hype одинаково
- **atom-0032** `principle` [philosophy/base] — Фильтр идей: это инженерная вера или просто wishful thinking?
- **atom-0033** `principle` [philosophy] — Engineering faith фальсифицируема: любой из трёх компонентов отсутствует → вера ненадёжна
- **atom-0034** `concept` [company/community] — Jetix Open Source Principles: Revenue Share + прозрачность + платформа
- **atom-0035** `principle` [community] — Платформа, не клуб: масштаб за счёт притягивания, не gatekeeping-а
- **atom-0036** `principle` [community/money] — Revenue Share: партнёр сохраняет ресурсы даже если Jetix исчезнет (antifragility)
- **atom-0037** `principle` [community/base] — Прозрачность подхода: методы, фреймворки, ошибки документируются и делятся (Karpathy LLM Wiki patter
- **atom-0039** `concept` [base/life] — Think-Do feedback loop — два базовых режима мозга (thinking, doing) и их цикл
- **atom-0040** `principle` [base/life] — Быстрый цикл think-do > медленный при прочих равных
- **atom-0041** `principle` [base/life] — Отсутствие feedback = бесконечный thinking без прогресса
- **atom-0042** `principle` [philosophy/base] — Внешний мир — источник истины, мысли без действия не проверены
- **atom-0043** `concept` [life/philosophy] — Value three layers — ценить / знать / делать, совпадение даёт поток
- **atom-0044** `principle` [life] — Провал знать = нужна рефлексия / терапия / journaling
- **atom-0045** `principle` [life] — Провал ценить = нужно восстановление (отдых, природа, близкие), не дисциплина
- **atom-0046** `principle` [life/base] — Провал делать = инструменты действия (план + инструменты + engineering faith)
- **atom-0047** `concept` [base/philosophy] — Writing as telepathy — передача образа sending place → receiving place (Стивен Кинг)
- **atom-0048** `principle` [base] — Слова — не сам образ, а запускающие триггеры
- **atom-0049** `principle` [base/company] — Успех письма = совпадение образа у автора и читателя
- **atom-0060** `concept` [company] — Текущая фаза Jetix: быстрые деньги (AI-консалтинг) + параллельная сборка сообщества и инфраструктуры
- **atom-0061** `concept` [company/money] — Бизнес-модели Jetix (рассматриваемые): Консалтинг-троян, Open Source + Premium, Tools-feedback-commu
- **atom-0067** `tension` [company/base] — Tension: не строить на orchestrators vs использовать CrewAI прямо сейчас
- **atom-0068** `concept` [life] — Life OS кластер: ценить → знать → делать + шкала влияния 0-100% + режимы заряжен/чил + дозировка дей
- **atom-0069** `concept` [company] — Business cluster объединяет: философию (open-source, Revenue Share, суверенитет), predator-защиту, б
- **atom-0073** `hypothesis` [company/philosophy] — За жизнь реально создать 200-300 массовых продуктов (one-person + AI)
- **atom-0074** `principle` [philosophy/company] — Принципиально другой масштаб мышления: не один бизнес на всю жизнь, а серия быстрых решений
- **atom-0076** `bet` [philosophy/company] — 200-year vision: Jetix как вклад в будущее где голод/болезни/неравенство решены
- **atom-0077** `principle` [philosophy/company] — Смысл переживающий основателя — закладывать ценности так, чтобы сохранились при росте
- **atom-0078** `principle` [philosophy] — Для решения глобальных проблем нужны: инновации + экономический рост + безопасность (не самоуничтожи
- **atom-0083** `concept` [company/money] — 5 рычагов масштабирования дохода: трафик, контент, автоматизация, команда, продукт
- **atom-0084** `principle` [company] — Каждый рычаг работает только с системой за ним
- **atom-0086** `principle` [life/base] — Дозировка действий: распределение во времени ≠ сумма во времени
- **atom-0087** `concept` [company] — Outreach dosage: 50 писем за раз vs 10 в день vs 3 в неделю дают разные response rates
- **atom-0089** `concept` [philosophy/base] — Адекватная картина мира на 3 уровнях: мир / группа / ты
- **atom-0090** `principle` [philosophy/base] — Если на любом уровне картина неадекватная — даже лучшие решения приведут к говну
- **atom-0095** `concept` [philosophy/company] — Метафора крепости: стены защищают, чтобы армия могла атаковать
- **atom-0096** `concept` [philosophy/company/community] — Агрессия через безопасность: внешняя экспансия возможна ТОЛЬКО из максимальной внутренней безопаснос
- **atom-0097** `principle` [company/money] — Клиент остаётся не потому что продали, а потому что уйти = потерять безопасность (lock-in без принуж
- **atom-0098** `concept` [company/money] — Глубокий анализ рынка AI-агентов с выводом ниш для Jetix в Mittelstand
- **atom-0100** `concept` [company/money] — AI-агентство: автоматизация + воронки + R&D на всех доступных рынках с быстрой скоростью запуска
- **atom-0102** `concept` [company/money] — AI-аналитика + группировка = колоссальная скорость запуска бизнесов при минимальном риске (портфель 
- **atom-0103** `principle` [company] — Не один бизнес, а портфель из 5-20 параллельных направлений
- **atom-0105** `principle` [base/life] — Notebook LM и AI-инструменты позволяют обрабатывать книги/материалы намного быстрее — встроить в еже
- **atom-0107** `concept` [philosophy/base] — AI как электричество: ценность сдвигается от ума к выбору (правильные вопросы, интеграция)
- **atom-0109** `concept` [base/company] — AI как информационный экскаватор: дисциплина работы с информацией + мощные инструменты
- **atom-0112** `principle` [company] — За несколько месяцев подготовки можно выйти на уровень, где обходишь игроков с ресурсами но без техн
- **atom-0114** `concept` [base/life] — AI как хранилище и продолжение личной мудрости: выжимки, принципы, опыт → AI подсказывает оптимальны
- **atom-0118** `bet` [philosophy/company] — AI = тектонический сдвиг; кто раньше освоит — получит непропорциональное преимущество
- **atom-0119** `principle` [philosophy/money] — Везение = наткнуться на технологию вовремя — нужно конвертировать в конкретные действия и финансовый
- **atom-0120** `concept` [base/life] — AI ускоряет обучение: цикл услышал → понял → применил сжимается с дней до минут
- **atom-0122** `concept` [company/community] — AI-контент-машина: запись всех мыслей/звонков → AI нарезка/анализ/публикация на YouTube/TikTok
- **atom-0126** `concept` [company/money] — AI-поиск клиентов с ресурсами и нерешёнными проблемами + системный инженер-задрот как позиционирован
- **atom-0128** `concept` [base/life] — AI помогает чётче формулировать мысли — структурирует хаос через диалог с машиной
- **atom-0130** `hypothesis` [company/philosophy] — AI-помощник как множитель одного человека до уровня корпорации — путь к one-person-billion-dollar-co
- **atom-0132** `concept` [company/base] — AI reverse-engineering бизнеса за дни (промпты + парсеры + LLM = информационный экскаватор)
- **atom-0133** `concept` [company] — Reverse-engineering слои: воронка, стратегия найма, рекламные кампании, юнит-экономика, стек, партнё
- **atom-0136** `concept` [base/company] — AI-стек Jetix: Notion + Miro + код + Claude = полноценная рабочая армия
- **atom-0140** `concept` [base] — Новый workflow: собрать 20-50 источников → NotebookLM → точечные вопросы → выжимки с цитатами → Noti
- **atom-0142** `principle` [base/philosophy] — Принять как новую норму: 3 дня с AI = полноценный анализ рынка (мозг пока не верит, но это факт)
- **atom-0144** `concept` [company/money] — AI-услуги: один набор методологий — множество локальных рынков (DE, ES, IT и т.д.)
- **atom-0145** `concept` [life] — Алгоритм оценки: путь дисциплины vs путь разъёба — нужны метрики и чекпоинты без самообмана
- **atom-0147** `concept` [relationships/community] — Карта нужных людей: где они, чем живут, как выйти на контакт — готовый план на случай ресурсов
- **atom-0150** `principle` [company/base] — Перед запуском канала/блога — холодный анализ затрат vs выхлопа
- **atom-0151** `concept` [philosophy] — AI = электричество нового уровня. Базовые вещи (машина, навык) станут доступны всем — это новый пол 
- **atom-0152** `concept` [company/money/philosophy] — AI = электричество, методология = завод, исполнители = электрики. Деньги зарабатывает владелец метод
- **atom-0153** `hypothesis` [company/money] — Система управления вниманием появится как индустрия (аналог фитнес-индустрии как ответа на сидячий о
- **atom-0155** `concept` [community] — Anti-free-riding: механизмы accountability в сообществе (притча о 10 мудрецах с водой)
- **atom-0156** `concept` [community] — Возможные механики anti-free-riding: regular check-ins, peer-review вкладов, tiered membership, rene
- **atom-0157** `tension` [community] — Открытые вопросы анти-free-riding: что считается вкладом, как измерять без бюрократии, публичность v
- **atom-0160** `concept` [base/company] — Армия AI-агентов вокруг одной личности — один человек достигает результатов больших команд
- **atom-0162** `concept` [life] — Аудит действий по выхлопу: каждое регулярное действие описывается через что даёт сейчас / что даст в
- **atom-0164** `concept` [life] — Аудит сред: разные среды (дом, зал, работа, машина) по-разному влияют на продуктивность. Лучшая — ти
- **atom-0167** `concept` [life] — Аудит свободного времени как стартовая точка: если 20% впустую, 2 часа в неделю на новое — минимум
- **atom-0169** `concept` [base] — Стек research: CrewAI → LlamaIndex RAG → LangGraph (когда production)
- **atom-0170** `concept` [base/company] — Автоматизировать research Фазы А через CrewAI: Researcher + Analyst + Writer мультиагентный пайплайн
- **atom-0171** `concept` [base] — Карпати-подход: Claude Code пишет код → Руслан направляет. Prototype за 1 вечер, refine через неделю
- **atom-0172** `tension` [base/company] — Tension: CrewAI как tactical tool сейчас vs claim что orchestration временный — решение: не строить 
- **atom-0176** `bet` [company/money] — B2G: аналитика безопасности AI → госконтракты Германии (long cycle 12-36 месяцев)
- **atom-0177** `concept` [company] — Двойное применение безопасности AI: оружие (отчёты, фреймворки, метрики) которое продаётся и в B2B и
- **atom-0179** `concept` [life/philosophy] — Beast mode formula: 1) понимание себя+цели 2) тактические приоритеты 3) никаких отвлечений 4) тело в
- **atom-0182** `principle` [company/philosophy] — Сначала стань ценным рынку, потом иди на рынок. 100ч практики+теории >> 10ч только теории
- **atom-0183** `principle` [company] — Что НЕ делать: cold outreach пустых офферов, продавать методологию без результата, громкое позициони
- **atom-0184** `concept` [company/money] — Бизнес-направление: кросс-профессиональные команды под ключ (рекрутинг + обучение + менеджмент-конса
- **atom-0186** `concept` [company/money] — Бизнес на внедрении дашбордов визуальной аналитики (Jetix готов заплатить 2000€ — крупные готовы пла
- **atom-0188** `concept` [company/community] — Блог как инструмент нетворкинга и роста (не просто контент)
- **atom-0192** `principle` [life] — Скука + спорт дают поток инсайтов в разы лучше чем трава
- **atom-0193** `principle` [life] — Отказ от травы: трезвая голова + солнце + сон + лёгкий голод = лучшее состояние для инсайтов

---

## 5. Cross-dimension connections

Total cross-dimension atoms: **2550**.

### Top dimension-pair connections

- **base ↔ company**: 498 atoms
- **company ↔ money**: 363 atoms
- **base ↔ philosophy**: 300 atoms
- **company ↔ philosophy**: 257 atoms
- **base ↔ life**: 220 atoms
- **community ↔ company**: 219 atoms
- **life ↔ philosophy**: 125 atoms
- **community ↔ philosophy**: 94 atoms
- **base ↔ community**: 65 atoms
- **company ↔ relationships**: 63 atoms
- **company ↔ life**: 60 atoms
- **money ↔ philosophy**: 42 atoms
- **community ↔ relationships**: 39 atoms
- **community ↔ money**: 39 atoms
- **base ↔ money**: 32 atoms

---

## 6. Recommendations for Stage 2


### 6.1 Priority tensions to resolve (Ruslan ↔ Cloud Cowork)
Из §1.3 soft tensions:
1. **Pain-based vs opportunity-based sales** — быстро, нужно для Phase 1 ICP.
2. **Geo first (Germany vs English-infobiz)** — средне, влияет на revenue-path Phase 1.
3. **Продюсерский центр vs остальные NEW projects** — park vs pursue.
4. **Exit / liquidity / equity** — нужно если Phase 2+ partners на горизонте.

### 6.2 Gaps to fill vs park
- **Fill now:** Pricing mechanics (beyond €150/час), ICP detail (archetype-level).
- **Fill phase-1 end:** GDPR / AI Act compliance skeleton.
- **Park:** Fortune 500 coalition, exit structure (revisit Phase 2+).
- **Life-OS thin:** fill only if life-coach delegate уже работает. Otherwise park.

### 6.3 Orphans to triage
Смотри §4 sample. Приоритет ручного review:
- `principle` orphans — могут быть core принципы без pair'ов.
- `bet` orphans — strategic wagers без context.
- `tension` orphans — обычно уже unfolded в pairs, но некоторые могут быть unique.

### 6.4 Action flags
- **Before D1 synthesis:** решить 4 remaining tensions из §1.3.
- **Before D2 synthesis:** принципы dimension=philosophy проверить на coherence с 8 locked decisions.
- **Before D3 synthesis:** Phase 1 task atoms (priority=P1) отфильтровать и пересчитать.
- **Before D4 synthesis:** architecture-related atoms (dimension=base) cross-check с D6 + D9.

---

_End of Knot Map._
