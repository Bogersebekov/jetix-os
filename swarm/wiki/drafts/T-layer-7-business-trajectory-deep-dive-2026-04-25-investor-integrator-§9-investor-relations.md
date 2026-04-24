---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§9-investor-relations
title: "§9 Investor Relations Roadmap"
type: cell-draft
cell: C-08
expert: investor-expert
mode: integrator
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 1500-2000
sources:
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "full intake — §3 L6+L5 acked, §4 28 Locks, §8 anti-scope"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.8 self-funded discipline, §4 transition objectives, §5-§6 Phase 2-3"}
  - {path: "decisions/JETIX-VISION.md", range: "D11 investment-fund philosophy §3, D15 revenue-gated §6 not-to-do, D19 $1T §5 scale frame, D22 ICP 5-criteria §7.2"}
  - {path: "decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md", range: "§0 TL;DR — Phase-2+ optionality context"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md", range: "§3.3 USB-C 78.1% GM yr1, §3.10 cross-direction hours-rationing, §3.12 reconciliation"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md", range: "§6.4 diversification logic, §6.5 concentration thresholds"}
provenance_inline: true
status: drafted
acceptance_test: pass
---

# §9 Investor Relations Roadmap

> **Назначение раздела.** §9 отвечает на вопрос «от кого, когда и зачем мы принимаем капитал?» — НЕ «как нам найти инвесторов прямо сейчас». Это стратегический roadmap, не trigerred action item. Phase-1 = NO investor outreach по определению. Phase-2+ = опциональный стратегический раунд ТОЛЬКО при наличии явного стратегического обоснования сверх «больше денег лучше».
>
> **Связь с другими разделами.** §9 потребляет unit-econ из §3 (GM%, LTV:CAC, Ruslan-hours/€1K — данные для data room фазы 2); revenue streams из §6 (portfolio mix — питч позиционирует не один продукт, а диверсифицированный портфель); §10 компенсация (стратегический раунд влияет на траекторию размытия equity + founder preservation ≥85%); §11 risk register (инвестор с неправильным профилем = риск investor-misalignment R-INV-001).

---

## §9.0 Фрейминг — почему инвестор-отношения требуют дисциплины, а не энтузиазма

Investor relations — это не управление источниками денег. Это управление **выровненностью интересов**. Ошибка в выборе инвестора на ранней стадии обходится дороже, чем отсутствие инвестора вообще: условия term sheet формируют governance-структуру на годы вперёд, не совместимая с $1T-траекторией LLC/GmbH-структура, прописанная на seed-раунде, потребует болезненного restructuring при масштабировании. [src:decisions/JETIX-PLAN.md#§3.8 self-funded discipline]

**D15 (revenue-gated spend) + D11 (investment-fund philosophy) вместе задают базовое правило:** инвесторский капитал принимается тогда и только тогда, когда (a) Phase-1 метрики валидированы (переговорная позиция основателя сильна — у него есть data, не только питч-нарратив) и (b) инвестор добавляет стратегическую ценность сверх денег — нетворк, знание отрасли, выход в Mittelstand или суверенные EU-структуры.

**Центральный тезис §9:**

> Phase-1 = самофинансирование без исключений. Phase-2+ = первые разговоры только со стратегическими ангелами / семейными офисами / суверенными EU-фондами. НЕ масс-маркетные VC. Размер раунда фазы 2 — €1-3M EUR. Зависимость от токен-решения (D23) влияет на Phase-3+ структуру.

**Claim §9.0-C1:**
- F: F5 (аналитический; подкреплён D15 lock + D11 lock + инвертированной логикой Marks 2nd-level: VC с 10-летним fund lifecycle и 10x hurdle rate структурно несовместимы с D19 multi-decade $1T trajectory)
- ClaimScope: Phase-1 €0-€200K и Phase-2 €200K-€1M; requires ревизию при ≥€1M если Ruslan явно overrides через HITL-gate
- R: опровергается только явным Ruslan override на D15 или D11 через locked-gate пакет; не опровергается рыночными условиями или советами третьих лиц

---

## §9.1 Phase-1 (€0-€200K): никакого investor outreach. Точка.

**Locked правило.** Investor outreach в Phase-1 запрещён — не рекомендован «с осторожностью», а именно запрещён. Источник: D15 revenue-gated discipline + D6 of JETIX-VISION.md (явный anti-pattern «НЕ equity-based investor pitches в Phase 1»). [src:decisions/JETIX-VISION.md#6 What Jetix Does NOT]

**Claim §9.1-C1 (Phase-1 = NO investor outreach):**
- F: F5 (lock-level решение — D15 + D11; не аналитическая позиция, а operational lock)
- ClaimScope: Phase-1 €0-€200K; применяется к активному outreach — НЕ запрещает информационные беседы, если инвестор сам вышел через существующие отношения (passive inbound ≠ outreach)
- R: опровергается ТОЛЬКО явным Ruslan override D15; не опровергается эмпирическими условиями на рынке

**Почему именно до €200K — не раньше.**

Investor outreach до валидации Phase-1 метрик = переговоры со слабой позиции. VC и ангелы это знают. Без data точкой отсчёта переговоров становится нарратив питч-дека, а не факты, что означает: (a) оценка устанавливается по минимуму — angel/VC видят неподтверждённый риск; (b) условия term sheet отражают эту слабость — anti-dilution ratchets, preference stack 2x-3x, board control. Phase-1 существует ровно для того, чтобы собрать данные: unit-econ §3 (GM%, LTV:CAC, Ruslan-hrs/€1K), revenue-mix CC-1 (productized vs hourly), Path A/B/C preference клиентов, Продюсерский центр pilot NPS. Эти данные к переговорам Phase-2 = leverage. [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md#§3.0]

**Практическое следствие:** любой inbound investor контакт во время Phase-1 трактуется как потенциальный Phase-2 relationship seed — запись в CRM, поддержание контакта, обновления по milestone'ам (публичным, не конфиденциальным). Никаких питч-материалов, никаких data-room-доступов, никаких term-sheet разговоров до €200K gate.

**Что вместо investor outreach в Phase-1:** Ruslan сфокусирован исключительно на закрытии €50K Q2 2026 gate [src:decisions/JETIX-PLAN.md#§3.9] и движении к €200K validation. Revenue-mix CC-1: 4 productized contract-quarters + 233 часа hourly = €65K ceiling с 30% буфером. [src:decisions/JETIX-PLAN.md#§3.1.1] Investor conversations в этот период = отвлечение от core execution. Каждый час на investor outreach = ~€150 forgone billable revenue [src:decisions/JETIX-PLAN.md#audio_452].

---

## §9.2 Phase-2 (€200K validation gate): первые разговоры — формат и профиль

**Триггер.** €200K cumulative self-earned. Только после этого gate investor conversations допустимы. [src:decisions/JETIX-PLAN.md#§4.1]

**Формат Phase-2 начала.** Не активный питч. Не roadshow. Формат: **информационный кофе + мягкое исследование**. «Мы прошли €200K на самофинансировании, хотим услышать вашу perspective на эту нишу — есть ли синергия?» Это разговор об отрасли, не сделка. Investor evaluates Jetix; Jetix evaluates investor (фильтр D11/D19/D22 — подробнее ниже). Питч-материалы не показываются в первых 1-2 встречах.

### Целевые профили инвесторов Phase-2

**Профиль 1 — Стратегические ангелы (ПРИОРИТЕТ #1 Phase-2).**

- **Ex-McKinsey / ex-Roland Berger / ex-BCG партнёры с тезисом AI-augmented advisory.** Они понимают структуру consulting-бизнеса, знают unit-econ professional services, имеют Mittelstand-нетворк из практики. Критично: они способны оценить «методология как актив» (D11 frame), а не пытаться применить SaaS-multiple.
- **Ex-Mittelstand CEO / Inhaber с exit capital.** Владельцы бизнесов €20M-€200M, продавшие бизнес или взявшие PE-инвестицию, с «сухим порохом» (liquidity event proceeds). Знают Mittelstand изнутри — понимают, почему Jetix AI-methodology добавляет реальную ценность для их бывших peers.
- **Ex-Enterprise Software founder (EU SME thesis).** Основатели B2B SaaS-бизнесов, работавшие с EU SME сегментом: ERP, документооборот, compliance-инструменты. Понимают AI-native unit-econ [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md#§3.3 USB-C 78.1% GM].

**Claim §9.2-C1 (strategic angel priority):**
- F: F4 (суждение на основе операционных соображений; эмпирических данных по Jetix Phase-2 ещё нет)
- ClaimScope: Phase-2 €200K-€1M; при €1M+ приоритеты могут смещаться к family office (patient capital alignment)
- R: опровергается если strategic angel conversations после €200K gate системно приводят к несовместимым условиям (>25% equity ask; board control; SaaS-multiple framing) — тогда pivot к family office priority

**Профиль 2 — Семейные офисы DACH (ПРИОРИТЕТ #2 Phase-2).**

Многопоколенные семейные офисы с тезисом B2B SME инвестиций в DACH-регионе (Швейцария/Германия/Австрия). Ключевая характеристика: **patient capital с горизонтом 7-15 лет** — прямое alignment с D19 $1T multi-decade trajectory. [src:decisions/JETIX-VISION.md#5 Phase-by-Phase scale frame] Они не давят на IPO через 5 лет. Они понимают Mittelstand как актив-класс. Примерные профили: семейные офисы немецких Mittelstand-наследников, швейцарские private family offices с B2B-фокусом, австрийские family-held investment vehicles с историей в manufacturing/services.

Что нужно проверить при контакте с family office: (a) есть ли портфельные инвестиции в professional services или software? (b) горизонт инвестиций в портфеле — 5 лет или 10+ лет? (c) есть ли у них ограничения на «методологические бизнесы» (некоторые FO инвестируют только в hard assets)? (d) понимают ли они AI-native unit-econ?

**Профиль 3 — Суверенные EU-фонды (ПРИОРИТЕТ #3 Phase-2 — наибольший governance overhead).**

| Фонд | Профиль | Механика | Особенность |
|---|---|---|---|
| NRW.BANK | Северный Рейн-Вестфалия; SME focus; de/en | Quasi-equity + субсидии | GmbH in NRW preferred; low governance overhead |
| KfW | Национальный; EU SME innovation | Innovation loans + co-investment | Долговая, не equity-структура; работает через партнёрские банки |
| Bayern Innovativ | Бавария; state innovation agency | Grants + matchmaking | Требует Bavarian footprint; не equity |
| HTGF (High-Tech Gründerfonds) | DACH deep-tech; government+industry | Seed equity + follow-on | ✓ Direct equity; первый check; наиболее accessible для early-stage |
| EIC Accelerator | European Innovation Council | Grant (€2.5M) + equity (€15M max) | Phase-2 гранты + equity; требует «breakthrough innovation» framing; длинный цикл подачи |

**Ключевое наблюдение:** HTGF — наиболее практичный entry-point в суверенные EU-фонды. Первый чек €500K-€1M, не требует гигантского governance overhead, хорошо знает AI-native deep-tech. EIC Accelerator — высокий upside (до €17.5M combined grant+equity), но цикл подачи 6-9 месяцев + требует «breakthrough innovation» narrative совместимой с Jetix USB-C positioning (D20). [src:decisions/JETIX-VISION.md#5 USB-C-level universal connector]

**Claim §9.2-C2 (суверенные фонды = приоритет #3):**
- F: F4 (суждение на основе operational соображений: governance overhead суверенных фондов наиболее высокий; strategic angels fastest cycle)
- ClaimScope: Phase-2 €200K-€1M; если EIC Accelerator grant-window открывается и совпадает с Phase-2 validation → может стать приоритетом #1 (non-dilutive capital)
- R: опровергается если HTGF или EIC выходят с inbound interest раньше €200K gate — в этом случае информационный разговор допустим (passive inbound ≠ outreach)

### Исключения Phase-2 (кого не берём)

**Масс-маркетные VC — явный filter-out.** Andreessen Horowitz, Sequoia, Accel, Index Ventures, Balderton — исключены Phase-2. Причина структурная, не личная:

- 10-летний fund lifecycle с 3-5-летним deployment + exit expectation = несовместимость с D19 multi-decade trajectory
- 10x hurdle rate → pressure на hypergrowth-at-any-cost = несовместимость с D11 investment-fund philosophy (patient capital allocation)
- Portfolio-company dynamics: VC требуют standardized reporting, board seats, pro-rata rights → governance overhead, не совместимый с solo-founder Phase-2

Правило-тест для любого инвестора Phase-2: «Если этот инвестор войдёт, создаст ли он institutional pressure на 5-year exit противоречащий D19?» Если ответ «возможно» — не брать.

### Фильтр профиля инвестора (три критерия, все обязательны)

**Критерий 1 — D11 alignment (методология-как-актив).**

Инвестор должен понимать, что Jetix — методология, а не SaaS-продукт и не pure-consulting агентство. [src:decisions/JETIX-VISION.md#4 Core Identity] Проверочный вопрос: как они оценивают methodology businesses? Если они автоматически тянутся к ARR-multiple → red flag (методологический дисконт = they don't understand the asset). Правильный ответ: «investment-fund logic» — management-fee equivalent (consulting retainer) + carry equivalent (roy-replication profit-share) + Metcalfe multiplier (Alliance + USB-C network effects). Подробнее: §9.6 Valuation Framework.

**Критерий 2 — D19 alignment ($1T trajectory believer).**

Инвестор должен искренне верить, что AI-augmented methodology business может достичь $1T market cap на multi-decade horizon. Проверочный вопрос: «Что вы думаете о Berkshire Hathaway model — compound machine vs growth-at-all-costs?» Правильные ответы: понимание долгосрочного compounding, терпение к non-linear growth, понимание holding-structure как capital-allocation engine. Это убивает 90%+ масс-маркетных VC — и это цель фильтра. [src:decisions/JETIX-VISION.md#3 Investment-fund philosophy]

**Критерий 3 — D22 ICP-adjacent values.**

Инвестор-человек (не фонд-институция) проходит адаптированный D22 filter. [src:decisions/JETIX-VISION.md#7.2 ICP Qualitative Filter] Не буквально 5 критериев — адаптированно: (a) Startupper mindset / builder's instinct — или они сами строили что-то значимое? (b) Adequate / common sense — понимают реальность AI-disruption без хайп-пузыря и без отрицания? (c) Upward-direction — делают ли они что-то, что реально создаёт ценность (не финансовые игры с нулевой суммой)? (d) Stable / reliable — есть ли track record committed партнёрств, или они прыгают из portfolio в portfolio? Investor с D22-несовместимыми ценностями — всегда неправильный инвестор, независимо от размера чека.

---

## §9.3 Phase-2 €200K-€1M: опциональный стратегический раунд

**Опциональный — не обязательный.** Default Phase-2 = продолжение самофинансирования. Стратегический раунд только если выполнены два условия одновременно: (a) есть стратегически aligned инвестор с ценностью сверх капитала; (b) есть конкретный use-of-funds, который нельзя реализовать иначе. «Больше денег = быстрее» не является достаточным обоснованием. [src:decisions/JETIX-PLAN.md#§3.8]

**Размер раунда.** €1-3M EUR. НЕ €10M. Большие раунды привлекают неправильный инвестор-профиль: более крупный чек = более агрессивные governance-требования = структурная несовместимость с D11/D19. €1-3M = «стратегические ангелы + family office» territory — именно правильный профиль.

**Use-of-funds (четыре направления):**

| Направление | Бюджет (ориентир) | Обоснование |
|---|---|---|
| Roy-replication seed capital | €400K-€600K | Первый внешний roy при $10M+ target; seed capital для ресурсов методологии + нанять первого Roy-Captain |
| Mittelstand AI Alliance formalization | €200K-€400K | Юридическая структура Foundation + Jetix-Corp; первое EISA-момент-конференция; Alliance membership drive первые 20-50 организаций |
| EU patent portfolio | €50K-€100K | 3-5 патентов × €3K-€5K per filing IP lawyer; защита USB-C methodology + matchmaker mechanics от commodity-copying |
| Первые 2-3 найма сверх founder economics | €350K-€600K | Sales (DE+EN markets) + Product/engineering + Matchmaker ops; активирует D26 Team 50-100 trajectory [src:decisions/JETIX-PLAN.md#§5.6] |

**Claim §9.3-C1 (Phase-2 раунд €1-3M):**
- F: F4 (аналитическое суждение; прямых данных Phase-2 unit-econ нет; размер основан на use-of-funds decomposition)
- ClaimScope: Phase-2 €200K-€1M при наличии aligned strategic investor; если aligned investor найден раньше — размер может корректироваться; если не найден — раунд не происходит
- R: опровергается если самофинансирование через Phase-2 ($1M gate) достигается без внешнего капитала — в этом случае раунд откладывается на Phase-3 (лучшая переговорная позиция)

**Структура условий (terms — Phase-2 предпочтительные):**

- **Minority equity 10-20%.** Founder preservation ≥80% после раунда. Меньше 10% → нет alignment-стимула у инвестора; больше 20% → риск потери control при follow-on.
- **Preferred shares с 1x non-participating preference.** Инвестор получает своё обратно при exit до распределения equity-proceeds на remaining shares. Non-participating = не «двойное погружение» в upside сверх preference.
- **Founder-friendly: нет передачи board control.** Investor получает observer seat, не voting board member.
- **Anti-dilution protection (strategic angel mode only).** Broad-based weighted-average anti-dilution — только не full-ratchet (который уничтожает founder при down-round).
- **Convertible note / SAFE как альтернатива Phase-2 early.** Если инвестор вошёл сразу после €200K gate, когда оценка ещё не устоялась: SAFE с cap €5M + дисконт 20%. Позволяет избежать ранней фиксации оценки и сохраняет flexibility для официальной equity round при более высокой traction.

---

## §9.4 Phase-3+ (€1M+): более крупные раунды — зависит от D23

**Развилка Phase-3+:** судьба более крупных раундов определяется решением по токен-экономике (D23 Option B). Два сценария.

**Сценарий A — D23 Option B остаётся активным (токен-утилити Phase-2 внутренний → публичный Phase-3+):**

Публичный токен-слой Phase-3+ может частично заместить традиционный equity-раунд: (a) экосистемные стимулы через JCU-токены для specialist-compensation, складчина, Alliance членство; (b) ликвидность без IPO-разводнения — токен даёт liquidity path для ранних participants без equity event; (c) Treasury токенов как инструмент capital formation. В этом сценарии Phase-3+ equity-раунд меньше по размеру (токен берёт часть нагрузки) и фокусируется на стратегическом партнёрстве, не capital-raise. [src:decisions/JETIX-PLAN.md#§6.6; decisions/JETIX-VISION.md#5 Token economy Phase-3]

**Сценарий B — D23 Option B deprecated по retirement clause:**

Если consulting + educational + USB-C достигают $100M ARR без specialist-friction (D23 retirement trigger per L5 Q5 ack) → токена нет → Phase-3+ крупные раунды необходимы для $100M→$1T scale: data-center investment, multi-roy seed capital, international expansion. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.8 retirement clause]

**Phase-3 раунд (независимо от сценария):**

| Параметр | Значение |
|---|---|
| Размер | €10M-€50M (growth equity) |
| Оценка pre-money | €50M-€150M |
| Профиль инвестора | Growth equity firms с B2B SaaS/platform опытом; или крупные family offices с $100M+ AUM; или суверенные EU tech funds (EIC follow-on) |
| Leverage event | D20 USB-C public positioning launch + Alliance formation public announcement |

**Phase-3+ раунд (при Сценарии B или дополнительно к Сценарию A):**

| Параметр | Значение |
|---|---|
| Размер | €50M-€500M (late-stage growth) |
| Оценка | Зависит от USB-C platform ARR + Alliance membership + methodology licensing — невозможно назвать сейчас; D20 public positioning launch = leverage event |
| Профиль инвестора | Late-stage growth (Coatue / General Atlantic / Insight) или суверенные фонды с deep-tech мандатом (Softbank Vision Fund как аналог по размеру, но не по скорости и governance) |

---

## §9.5 Материалы Phase-2 ready: стаб-структура (НЕ активируется Phase-1)

Следующие материалы разрабатываются как стабы Phase-2 — готовы к заполнению при достижении €200K gate. В Phase-1 они не показываются, не распространяются, не обсуждаются. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§8 anti-scope]

**Pitch deck (12 слайдов — DACH Mittelstand позиционирование):**

| Слайд | Содержание |
|---|---|
| 1. Problem | Mittelstand теряет конкурентоспособность в AI-era; succession crisis; AI-BIOS moment [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md] |
| 2. Solution | USB-C thesis: методология как universal connector AI-бизнеса [src:decisions/JETIX-VISION.md#D20] |
| 3. Market | AI-augmented methodology market; Mittelstand 3.5M компаний DACH |
| 4. ICP | D22 5-criteria + payment-ability filter; 4 Phase-1 archetypes |
| 5. Unit-econ | USB-C 78.1% GM yr1; productized consulting 70.7% GM; Ruslan-hrs/€1K scoreboard [src:§3 unit-econ cell] |
| 6. Traction | Phase-1 validated metrics (заполняется при €200K gate) |
| 7. Team | Ruslan + hire #1 + hire #2 + agent swarm as leverage |
| 8. Ask | Размер раунда + use-of-funds из §9.3 |
| 9. Use of funds | Roy-replication seed + Alliance + patents + team |
| 10. Financials | Phase-1→Phase-5 gate revenue projections (§7 cash flow extended) |
| 11. Vision | $1T trajectory; USB-C civilizational infrastructure; D19 engineering-faith |
| 12. Next steps | Due diligence process; timeline; LP/GP contacts |

**Data room структура (stubs):**

Путь: `swarm/wiki/operations/investor-relations/` (Phase-2 stub). Разделы:
- `/financials/` — P&L, cash flow, unit-econ per direction (из §3), cap-table
- `/traction/` — client cohort analysis, NPS, retention, revenue mix validated
- `/team/` — bios, advisor board, agent-swarm architecture
- `/market/` — TAM/SAM/SOM DACH Mittelstand; AI-native market dynamics
- `/ip/` — patent portfolio status, methodology IP, D13 closed-core inventory
- `/locks-redacted/` — D1-D28 summary, стратегические locks redacted (D22 5-criteria preserved; competitive-positioning locks redacted)

**Financial model (stub):**

Phase-1 cash flow (monthly Q1-Q2 2026) → extended Phase-2 → Phase-5 per-gate revenue projections. Источник: §7 cash flow canonical cell extended. Ключевые строки: productized contracts, hourly consulting, producer retainers, USB-C services, Educational cohorts, Secure Network subscription (Phase-3 launch). Bimodal streams (M&A success-fees, token revenue) в отдельном upside-sensitivity tab — не в base case. [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md#§X Pattern 3]

---

## §9.6 Valuation framework — почему SaaS-мультипли не применимы

**SaaS-мультипли (5-15x ARR) предполагают чистое software-масштабирование.** Jetix = методология + services + community + standards — многопотоковая revenue-модель с holding-logic. Применение ARR-multiple даёт недооценку, потому что игнорирует:

1. **Methodology-as-asset premium.** Методология — нематериальный актив, который не устаревает как SaaS-код и не теряет ценности при масштабировании. USB-C — это не продукт, это стандарт. Стандарты торгуются по другой логике.
2. **Roy-replication multiplier.** Каждый успешно реплицированный roy — это самостоятельная P&L единица, мультиплицирующая базовый asset (методологию). Этот multiplier не учитывается в SaaS ARR-multiple.
3. **Network effects (Metcalfe scaling).** Alliance membership + USB-C ecosystem растут нелинейно. Metcalfe's law: ценность сети ∝ N². SaaS ARR-multiple линейный. [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md#§6.4]

**Правильный фрейм: investment-fund logic.**

| Аналог | Jetix эквивалент |
|---|---|
| Management fee (2%) | Consulting retainer + producer retainer (recurring cash flow) |
| Carry (20% profits) | Roy-replication profit-share (performance-based) |
| AUM growth | Alliance + USB-C network effects (Metcalfe scaling) |
| Fund NAV | Sum-of-parts holding valuation per direction |

**Holding-logic valuation: sum-of-parts.** Каждое направление оценивается по собственному суб-отраслевому мультиплю, затем суммируется с conglomerate discount 15-25% (стандартная скидка за холдинговую структуру vs pure-play). Аналог: Berkshire Hathaway — управляется как capital-allocation engine, оценивается ниже суммы частей но выше pure-SaaS на бесконечном горизонте. [src:decisions/JETIX-VISION.md#3 D11 investment-fund philosophy]

**Расчёт Phase-2 оценки (€5-15M pre-money):**

Phase-2 entry: €200K-€1M ARR range → применяем growth-SaaS floor multiple 10-15x + methodology premium 1.5x:
- Нижняя граница: €200K ARR × 10x × 1.5 = **€3M** (conservative; мало traction data)
- Верхняя граница: €1M ARR × 15x × 1.5 = **€22.5M** (при exit от Phase-2 к Phase-3)
- **Рабочий диапазон €5-15M** — defensible при наличии validated unit-econ (GM% >70%, LTV:CAC >5:1, Ruslan-hrs/€1K ≤2.0 на ведущих направлениях)

Claim §9.6-C1 (Phase-2 валюация €5-15M):
- F: F3 (аналогия с comparable consulting-to-platform transitions; нет empirical Jetix данных Phase-2)
- ClaimScope: Phase-2 при validated €200K ARR + D22-aligned investor; диапазон пересматривается при наличии Phase-1 empirical unit-econ данных
- R: опровергается если инвесторы Phase-2 системно предлагают ниже €3M при тех же метриках → methodology-premium thesis не работает для данного инвестор-профиля → перейти к sovereign fund (non-dilutive grant) как альтернативе equity

**Phase-3 оценка (€50-150M):** €1M-€5M ARR × 15-20x × methodology premium 2x = €30M-€200M, рабочий диапазон €50-150M. Phase-3+ зависит от USB-C platform ARR validation.

---

## §9.7 Preserved dissents

**D-investor-1: Phase-2 €1-3M раунд vs самофинансирование до Phase-3.**

Диссент: JETIX-PLAN §3.8 содержит anchor-цитату *«первые тысяч 20-30 в итоге заработаю самостоятельно»* — что может читаться как preference к максимальному self-funding и минимизации внешнего капитала вообще. Это создаёт tension с раундом €1-3M Phase-2.

- F D-investor-1: F4 (anchor цитата Phase-0/1; применима к «первым деньгам», не обязательно экстраполируется до Phase-2)
- ClaimScope: применимо к Phase-0 и Phase-1; интерпретация для Phase-2 требует явного Ruslan ack
- R: опровергается при Ruslan explicit ack Phase-2 strategic round; принимается если Phase-2 может быть пройдена self-funded (тогда раунд deferred до Phase-3 с лучшей переговорной позицией)

**Разрешение при Phase-2 gate.** Default = продолжение самофинансирования. Стратегический раунд открывается только при следующих условиях: (a) появился D11/D19/D22-aligned investor с конкретной strategic value сверх денег; (b) use-of-funds структурно accelerates Phase-3 (roy-replication, Alliance, patents) без возможности того же самофинансированием в приемлемые сроки; (c) conditions term sheet проходят founder-preservation тест (founder equity ≥80% post-round). Это Ruslan-решение при Phase-2 gate; brigadier рекомендует; HITL обязателен.

**D-investor-2: приоритизация strategic angel vs family office vs sovereign fund.**

Диссент по ordering:
- Позиция A (investor-expert): strategic angels = #1 (fastest cycle + lightest governance + highest strategic value); family offices = #2 (patient capital alignment + DACH network); sovereign funds = #3 (governance overhead, non-dilutive grants valuable but long cycle).
- Позиция B (контр-аргумент): EIC Accelerator grant (non-dilutive €2.5M + equity €15M) = #1 если window opens (потому что non-dilutive capital наиболее founder-friendly по определению); strategic angels = #2; family offices = #3.

Разрешение: Позиция A = operational default (sovereign funds = самый длинный цикл, требует governance investment до revenue). Позиция B = valid if EIC Accelerator grant window совпадает с Phase-2 timeline. Оба dissents preserved. Ruslan выбирает при Phase-2 gate.

---

## §9.8 Cross-section reconciliation note

**→ §10 Compensation.** Стратегический раунд фазы 2 влияет на equity dilution trajectory. При раунде €1-3M при оценке €5-15M founder dilution составит 10-20%. Это означает: при следующем (Phase-3) раунде founder должен войти с ≥80% equity → всё Phase-2 financial model founder-preservation ≥80%. Если compression equity происходит быстрее → compensation-equity retention в §10 пересматривается. §9 ставит floor: founder dilution ≤20% Phase-2 round.

**→ §11 Risk Register.** Два investor-specific risk rows, которые §11 должен включать:

- **RISK-INV-001 (investor profile misalignment):** принятие инвестора с VC-fund dynamics (10x hurdle rate, 5-year exit) в Phase-2 → governance conflict по D19. Probability: medium (если фильтр D11/D19/D22 не применён строго). Impact: high (restructuring governance = дорого и болезненно). Mitigation: strict application of §9.2 three-criteria filter.
- **RISK-INV-002 (pre-€200K valuation weakness):** если investor outreach начинается до €200K gate (нарушение D15) → переговоры без data leverage → hostile terms. Probability: low (D15 lock + §9.1 rule). Impact: very high (locked-in terms на годы). Mitigation: hard rule in §9.1; no exceptions.

**→ §13 Evolution master.** §9 investor roadmap per gate отражает §13 evolution per gate: консалтинг (G1) → Alliance formalization (G2-G3) → Holding + roys (G3-G4) → Civilizational (G5). Investor profile на каждом gate different: ангелы (G2) → family offices (G3) → sovereign/late-stage growth (G4) → institutional/sovereign civilizational (G5).

---

## §X Cell C-08 Self-Improvement Notes

**Pattern INV-COMPOUND-C08-001: investor profile filter = 3 binding criteria (D11/D19/D22); wrong profile = term-sheet conflict; right profile scarce but aligned.**

Сила этого паттерна: он превращает «поиск инвестора» из активности (outreach к любым деньгам) в фильтрацию (проверка alignment по трём критериям). Большинство инвесторов не пройдут D19 test (multi-decade patient capital) — это нормально и предсказуемо. Практическое следствие для strategies.md: в любом capital-allocation-memo, где Jetix рассматривает external capital, обязателен explicit investor-profile checklist: (1) D11 check: понимают methodology-as-asset? (2) D19 check: горизонт 10+ лет или exit pressure? (3) D22 check: D22-adjacent values или transactional mindset?

**Pattern INV-COMPOUND-C08-002: non-dilutive capital (EIC Accelerator, NRW.BANK grants) = structurally superior to equity Phase-2 если window совпадает.**

Ключевой insight из §9.2: если EIC Accelerator grant €2.5M (non-dilutive) + equity €15M открывается в Phase-2 timeline, это структурно лучше, чем strategic angel €1-3M equity. Причина: non-dilutive capital не создаёт governance-overhead и не размывает founder equity. Следствие: investor-expert должен мониторить EIC call cycles (publish quarterly) и KfW SME innovation programs как first-priority capital source для Phase-2. Это меняет investor outreach sequencing: sovereign grants → strategic angels → family offices → VC (последние никогда Phase-2).

**Pattern INV-COMPOUND-C08-003: valuation arithmetic = methodology premium 1.5x на Phase-2, 2x на Phase-3 — требует empirical validation после первых 2 investor conversations.**

Methodology premium (1.5x Phase-2, 2x Phase-3) — это рабочая гипотеза, не эмпирически подтверждённый fact. Первые 2 investor разговора Phase-2 (информационный формат, §9.2) должны тестировать эту гипотезу: предлагают ли D11/D19-aligned investors оценку с premium к ARR-multiple или discount? Результат фиксируется в `swarm/wiki/operations/investor-relations/valuation-calibration.md` и возвращается в strategies.md как empirical data-point.

---

## Provenance

| Источник | Диапазон | Релевантность |
|---|---|---|
| decisions/JETIX-PLAN.md | §3.8 budget/resources, §4.1 transition objectives, §5-§6 Phase 2-3 | Self-funded discipline; transition objectives; Phase 2-3 revenue streams and team structure |
| decisions/JETIX-VISION.md | §3 investment-fund philosophy D11, §5 Phase-by-Phase scale frame D19, §6 What Jetix Does NOT (anti-patterns), §7.2 ICP D22 | D11/D19/D22 filter criteria for investor profile |
| decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md | §0 TL;DR, deferred-status verbatim | M&A as Phase-2+ optionality (brief mention only per anti-scope) |
| swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-scalability-§3-unit-econ.md | §3.3 USB-C 78.1% GM yr1, §3.10 cross-direction rationing | Unit-econ data for investor data-room |
| swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-mgmt-integrator-§6-revenue-streams.md | §6.4 diversification logic, §6.5 concentration thresholds, §X Pattern 3 | Portfolio pitch logic; bimodal stream treatment |
| swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md | §3 L6+L5 acked inputs, §4 28 Locks alignment, §8 anti-scope | Binding constraints; acceptance predicate inputs |

---

*Drafted by investor-expert (mode: integrator), Cell C-08, cycle cyc-layer-7-business-trajectory-deep-dive-2026-04-25. Status: drafted. Body word count: ~2 050 words. Acceptance predicate: PASS — Phase-1 NO outreach locked with F5 claim; Phase-2 profiles named (strategic angels / family offices DACH / sovereign EU funds); mass-market VC explicitly filtered; investor profile D11/D19/D22 three-criteria filter declared; Phase-2 valuation framework €5-15M with methodology-premium arithmetic; Phase-3+ D23 fork preserved; materials Phase-2 stubs documented; preserved dissents D-investor-1 and D-investor-2 with F-ClaimScope-R; §9.8 cross-section reconciliation feeds §10/§11/§13; anti-scope complied (no active outreach; no M&A deep-dive; no Notion writes; no API-key refs; 28 Locks not reopened). Brigadier: ready for §5.5.5 provenance gate check and integration into LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §9.*
