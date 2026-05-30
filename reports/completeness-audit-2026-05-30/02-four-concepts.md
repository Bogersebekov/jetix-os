---
title: "Phase 2 — 4 новых концепт-кластера (invest-fund · crypto-coins · game-theory · intelligence)"
date: 2026-05-30
phase: 2-four-concepts
parent_prompt: prompts/presentation-completeness-audit-plus-wiki-ingest-2026-05-30.md
F: F2 (Ruslan voice hypotheses) + F3 (synthesis) + F4 (external comparables)
G: prompt-completeness-audit-plus-wiki-ingest-2026-05-30
constitutional_posture: R1 surface (гипотезы — Ruslan picks) + R6 per-claim + R11 + R12 paired-frame STRICT (influence-ethics RECEIVER auto-fire on all 4) + IP-1 + append-only
language: russian
roy_lens: investor-expert + systems-expert + philosophy-expert + methodology-engineer + gamification-engagement + influence-ethics (RECEIVER) + ml-ai-foundations
status: pool — R1 гипотезы, NO auto-add в V4 / пакет
---

# Phase 2 — 4 новых концепт-кластера

> **R1 surface.** Все 4 = **гипотезы Ruslan** (voice 30.05), проработанные роем и связанные
> с существующим substrate. НЕ auto-add в V4 metaplan и НЕ в пакет (R2 STRICT). Каждый
> завершается **R12-verdict** (influence-ethics RECEIVER auto-fired). Ruslan picks.
>
> **Ключевой вывод-синтез:** концепты **1-2-3-4 — не четыре отдельные темы, а один контур**.
> Game theory (#3) = *почему* кооперация выигрывает; crypto/coins (#2) = *чем* это
> enforced в коде; invest-fund (#1) = *как* ценность реинвестируется по петле; intelligence
> (#4) = *кто* (какие люди) удерживают кооперативное равновесие. Это **человеко-машинный
> R12-движок**: §4 — человеческая сторона того же равновесия, что §3 описывает формально,
> §2 enforced'ит в коде, а §1 финансирует.

---

## Концепт 1 — Инвест-фонд / управление 6 ресурсами

### Гипотеза Ruslan (F2)

Jetix управляет **6 ресурсами**; **инвест-фонд вшит в систему**; фонд **инвестирует
обратно в систему + в другие проекты**; «мощная часть компании».

### 6 ресурсов (определение — R1 surface, связано с substrate)

Ruslan назвал примеры (знакомства/помещения/идеи/деньги/информация/…). Рой предлагает
канонизировать **6**, прямо ложащихся на benefit-stack [[coach-thesis-why-jetix]] и на
resource-pooling [[resource-pooling-proof]] (O-271):

| # | Ресурс | Substrate-якорь | Pool-эффект |
|---|---|---|---|
| 1 | 🤝 **Знакомства / сеть** | CRM (24 роли) · #14 Сеть · «знать о сотнях людей» | combinatorial (N² связей) |
| 2 | 🏛️ **Помещения / пространство** | #12 Мастерская (8 зон) · workshop-concept | shared fixed-cost |
| 3 | 💡 **Идеи / методы / IP** | #1 Метод · meta-method · wiki KB | non-rival (копируется бесплатно) |
| 4 | 💰 **Деньги / капитал** | Economic V10 institutional treasury (T_inst=0.25R) | reinvest compound |
| 5 | 📊 **Информация / знание** | wiki (109+ concepts) · exocortex · #2 Платформа | non-rival + compound |
| 6 | 🎯 **Мастерство / таланты** | #13 Мастерство · #5 Партнёры · skill trees | принадлежит человеку (mobility) |

Тезис resource-pooling: соединение этих 6 у 20 человек **сверх-аддитивно** (network +
non-rival эффекты) — и это **арифметически считаемо** (O-271 «посчитать, что получится») →
прямой feed числовой модели (A1).

### Substrate-связь: фонд УЖЕ есть (не новое)

`ECONOMIC-MODEL-TOKENOMICS` (V10 LOCKED-substrate) уже содержит **institutional treasury**:
`T_inst = 0.25 × R` (25% в институциональную казну) + «treasury reinvestment ROI > 1.0» +
«treasury self-fund Y3+». **«Инвест-фонд вшит в систему» = формализация этой казны как
внутреннего инвест-фонда.** Реальный прецедент — **Mondragón Caja Laboral** (кооперативный
банк, который реинвестировал профицит в *порождение новых кооперативов*) — это в точности
«фонд инвестирует в систему + в другие проекты». [src: ECONOMIC-MODEL-TOKENOMICS §2 Mondragón
translation; §3 treasury math]

Два контура реинвестиции фонда:
1. **В систему** (R&D flywheel, 90%-reinvest insight) → substrate растёт → выше leverage.
2. **В другие проекты/кланы** (Caja-Laboral-pattern) → фонд spawn'ит новые клан-кооперативы
   (V4 §4 fork-and-spawn) → mesh растёт. Изоморф [[recursive-value-chain]] (петля ценности).

### Что добавляет (R1)

- **Triple-role «investor» dimension** (V10 §6) получает явный объект — фонд: worker (75%) +
  **investor (25% institutional stake → treasury share + dividends + voting)** + promoter.
  Фонд = то, во что инвестирует investor-роль партнёра.
- **«Мощная часть компании»** = фонд как leverage-движок: не «деньги лежат», а реинвест-петля
  (ROI>1.0 → exponential Y4 K≥1.0, V10 §0).

### ⚠️ R12-VERDICT — CRITICAL (investor-expert + influence-ethics RECEIVER)

| Surface | R12-чтение | Вердикт |
|---|---|---|
| фонд с возвратами investor-роли | доходность в рамках **agreed share** (25% institutional, прозрачно) | ✅ COMPATIBLE если share честный |
| фонд реинвестирует «в систему» | R&D flywheel = CC-quadrant payoff (game-theory M-C) | ✅ POSITIVE — anti-extraction anchor |
| **фонд как «доение» участников** | если фонд извлекает сверх доли → R12 rule 12 violation | 🚫 **GUARD** — extraction_beyond_share action class |
| lock-in капитала участника | если выход = потеря вклада → fork-prevention | 🚫 **GUARD** — Moloch RageQuit (proportional treasury claim) обязателен |
| wage-ratio через фонд-дивиденды | концентрация у investor-роли | ⚠️ Mondragón **5:1 cap** на distributions держится |

**Условия R12-чистоты фонда (4 guards из `default-deny-table.yaml` Layer-4):** (1)
`extraction_beyond_share` — доходность только в пределах agreed 25%; (2) `wage_ratio_violation`
— 5:1 cap на выплаты; (3) `fork_prevention_attempt` — RageQuit/exit-token гарантирует выход
с долей; (4) `non_consensual_distribution` — opt-in. Прозрачность казны = публичный on-chain
(связь с Концептом 2). **Без этих guards фонд = техно-феодализм (M-C запрещает конституционно).**

### → Куда (R1)

- **NEW-direction candidate #18? «Инвест-фонд / Capital allocation»** — R1 surface (Таблица 4
  fixation doc); НЕ auto-add. Альтернатива: суб-грань #3 Бизнес + #4 Заработок (не отдельное
  направление). Рекомендация роя: **суб-грань #4**, не #18 (избегать direction-inflation; фонд
  = механизм экономики, не самостоятельная тема). Ruslan picks.
- **Презентация:** слайд-кандидат «Инвест-фонд: как ценность реинвестируется» → P-6/P-7 (после
  A1 числовой модели). R12-gated: показывать как петлю реинвеста, НЕ как «доходность инвестору».

---

## Концепт 2 — Крипта / коины / сеть взаимодействия

### Гипотеза Ruslan (F2)

Всё в криптовалюте/коинах; сеть настроена так, чтобы люди **адекватно, быстро,
добросовестно** взаимодействовали.

### Substrate-связь: это УЖЕ acked (не новое)

`R12 Programmable Ethereum` **Option D Hybrid acked 2026-05-18** (Ruslan: «давай всё туда
акаем») = полный R12-стек в коде:
1. **Mondragón ratio enforcement** (3:1→9:1 wage cap программно в смарт-контракте);
2. **Quadratic Funding** (Tang+Weyl, проверено Gitcoin) для distribution;
3. **Fork-and-leave exit tokens** (программная R12 anti-extraction гарантия на члена клана).

V10 token form **V10 Hybrid**: ERC-1155 Triple-role NFT (worker/investor/promoter SBT) +
Moloch RageQuit + Gitcoin QF pool + SBT identity. [src: ECONOMIC-MODEL-TOKENOMICS §0/§6;
r12-programmable-ethereum-2026-05-18]

### Синтез: как «адекватно/быстро/добросовестно» ложится на код

Гипотеза Ruslan = **точное описание того, что enforced'ят коины** (не метафора — механика):

| Слово Ruslan | Механизм-в-коде | Эффект |
|---|---|---|
| **адекватно** | incentive-compatibility (mechanism design) — кооперация = best-response | честное поведение выгодно |
| **быстро** | Moloch RageQuit + matching FPF «2 часа в проекты» | мгновенный exit + matching |
| **добросовестно** | SBT reputation (soulbound, нельзя купить/подделать) + visible repeated play | репутация = актив, defection дорог |

**Коины = enforcement-слой R12, а не спекулятивный актив.** Это переводит Концепт 3 (game
theory) из «дизайна правил» в «правила, исполняемые автоматически» — смарт-контракт = mechanism
design, который нельзя обойти.

### ⚠️ R12-VERDICT — MED (influence-ethics RECEIVER + sota-tracker)

| Surface | Вердикт |
|---|---|
| коины как R12-enforcement (QF/cap/exit) | ✅ NATIVE-COMPLIANT — distinctive feature (никто из crypto не делает программный R12) |
| **«всё в крипте»** hype/speculation framing | 🚫 **SCREEN** — НЕ «coin go up» / НЕ «токен вырастет»; коин = utility/governance/reputation |
| pay-to-win через токены | ⚠️ V10 §14 п.8: virtual economy = max R12-риск → **defer** до отдельной R12-design session |
| обязательность крипты | ✅ per-Clan **opt-in** (не required adoption); Phase 2+ overlay |
| Tier 2 R12 text | ✅ PRESERVED — substrate-agnostic; коин = RUSLAN-LAYER overlay, не Foundation generic |

**Вывод:** native-compliant как enforcement, но **публичный framing = строго anti-speculation**.
Для партнёрской презентации: коины = «как мы гарантируем честность в коде» (P-4 R12), НЕ
«инвестируй в токен». Phase 2+ — НЕ в текущий пакет как обещание.

### → Куда (R1)

- **Направление:** суб-грань **#8 R12** (enforcement) + **#4 Заработок** (token form). НЕ новое
  направление (уже в substrate).
- **Презентация:** P-4 (Ценности+R12) — абзац-кандидат «R12 в коде: смарт-контракты, которые
  не дадут доить или запереть» (anti-speculation framing). Только Phase 2+ disclaimer.

---

## Концепт 3 — Теория игр / кооперация

### Гипотеза Ruslan (F2)

Система позволяет кооперироваться и «теорию игр нагнуть» (сдвинуть равновесие к сотрудничеству).

### Substrate-связь: глубоко проработано (M-C mechanism §11)

`reports/jetix-game-theory-cheating-research-2026-05-12` + 12 wiki game-theory concepts
(`wiki/concepts/game-theory/`) дают полный аппарат. Ключевые тезисы [src: §11 synthesis]:

1. **«Нагнуть» ≠ «отменить PD как теорему».** Jetix **структурно инвертирует 7 условий**,
   защёлкивающих defection (single-round → repeated; anonymous → reputation-visible;
   no-punishment → punishment; no-communication → communication; low-stakes → meaningful;
   + folk-theorem applicability). Парадокс не отменён — **изменены условия игры**.
2. **Mechanism design делает кооперацию dominant strategy** (Hurwicz-Maskin-Myerson Nobel
   2007): дизайн правил так, что incentive-compatibility + individual-rationality →
   truth-telling и cooperation = best-response. **Jetix Realm = applied mechanism design.**
3. **Кооперация — эволюционный аттрактор** (Axelrod 1984 ecological tournament): TFT-family
   выигрывает ALL-D при iterated play + selection. При reputation-visible network →
   cooperation = attractor, defection = repulsor («virus»-эффект, позитивный).
4. **M-C Anti-Extraction Constitutional Anchor** = R12 Tier 2 делает мутацию в техно-феодализм
   **конституционно запрещённой** → payoff-matrix перебалансирован к CC-quadrant.

### Синтез: 3 рычага «нагибания» (Meadows leverage + Schelling)

- **Rule-change** (highest leverage, Meadows #5): смарт-контракты (Концепт 2) = правила, что
  делают кооперацию best-response. Это и есть «нагнуть» — не уговорить, а **изменить payoff**.
- **Shadow of the future** (δ→1): длинный горизонт → folk theorem → кооперация устойчива.
  Прямой мост к **Концепту 4** (forecasting depth = низкий discount rate).
- **Schelling focal points** (gamification-engagement domain): координация без принуждения —
  общие точки фокуса (триада O-138, Charter) = где люди сходятся сами.

### ⚠️ R12-VERDICT — MED (gamification-engagement SENDER → influence-ethics RECEIVER + philosophy)

| Surface | Вердикт |
|---|---|
| mechanism design к кооперации | ✅ POSITIVE если **incentive-compatible + individual-rational** (truth-telling = best-response, не принуждение) |
| **«нагнуть» как манипуляция payoff** | ⚠️ **LINE** — nudge к кооперации, что *также* выгодна каждому ✅ vs скрытая манипуляция payoff против интереса участника 🚫 |
| cooperation-virus «spread» | ✅ NOT epidemiological/non-consensual; positive evolutionary spread при visible iterated play |
| «полезно для обществу» civic claim | ✅ healthier ecosystem чем default-defection; NOT anti-state/anti-corporate |

**Линия R12:** механизм-дизайн легитимен, когда кооперация — **best-response каждого** (никто
не проигрывает от честности). Становится манипуляцией, когда payoff скрыто искажён против
интереса участника. Тест: *прозрачны ли правила и выгодна ли честность каждому игроку?* Если да
— ✅. Связь с anti-dark-patterns (#15): «нагибать» нельзя через addictive loops / coercion.

### → Куда (R1)

- **Strategic Insight candidate:** «**Cooperation as Strategic Moat**» (8-я Insight Octagon
  evolution, per §12 game-theory report) — R1 surface; рой рекомендует promote. Это **moat-аргумент**
  для партнёра/инвестора: «почему Jetix не скопировать» = кооперативное равновесие, защищённое
  R12-конституцией.
- **Направление:** суб-грань **#8 R12** + **#14 Сеть** (densest hubs). НЕ новое направление.
- **Презентация:** слайд-кандидат **«Почему это работает — кооперация как преимущество»** → P-1
  (moat) / P-4 (R12). Сильный investor-аргумент (defensibility).

---

## Концепт 4 — Интеллект + ответственность + долгосрочная кооперация

### Гипотеза Ruslan (F2)

Чем **ответственнее** человек и чем **дальше может просчитать/продумать**, тем выше шанс
**скооперироваться надолго** → это **важная часть интеллекта**.

### Синтез: это человеческая сторона Концепта 3 (сильнейшая связка аудита)

Гипотеза Ruslan **точно совпадает с условием устойчивости кооперативного равновесия** в
теории игр — и это не совпадение, а **изоморфизм**:

| Слово Ruslan | Game-theory эквивалент | Механизм |
|---|---|---|
| «дальше может **просчитать/продумать**» | **низкий discount rate** δ→1 (shadow of future) | folk theorem: при δ→1 кооперация = равновесие |
| «**ответственнее**» | **reputation / commitment-credibility** | repeated game + SBT: надёжность делает defection дорогим |
| «скооперироваться **надолго**» | sustained CC-equilibrium | iterated play, не one-shot |

**Вывод-синтез (R1):** «интеллект» здесь = **не raw IQ, а (горизонт прогноза δ→1) ×
(надёжность/ответственность)**. Это **две человеческие переменные, которые удерживают
кооперативное равновесие**, описанное Концептом 3. Jetix **отбирает и развивает обе**: метод
(#1) и meta-method (Method V2 §5) тренируют горизонт прогноза; ценности/R12 (#10/#8) и
репутация (SBT, Концепт 2) формируют ответственность. Так концепты 3-4 смыкаются: §3 —
формальное условие, §4 — человеческий капитал, который ему соответствует.

### Substrate-связь (Method V2 + FPF + philosophy)

- **Intelligence layer concept** (Method V2 §6): «слой интеллекта» = inserted deliberation
  между stimulus и response — буквально «просчитать дальше прежде чем реагировать».
- **Meta-method (recursion level 3)** (Method V2 §5 ⭐⭐): метод выбора методов = способность
  прогнозировать, какой метод сработает = forecasting depth. Ключевое отличие Jetix-подхода.
- **VSM System 4 = Intelligence** (Method V2 §2, Beer): система, смотрящая в будущее/наружу =
  forecasting организма. «Управление через уровень-выше».
- **Exocortex** (Method V2 §10, Bush→Karpathy): AI substrate **расширяет горизонт прогноза** —
  solo+AI = leverage Fortune 500 → радикально углубляет «насколько дальше можешь просчитать».
- **WHY-якорь:** [[coach-thesis-why-jetix]] — «с тренером лучше» = тренер расширяет твой
  горизонт прогноза и держит ответственность (accountability).

### Что ещё про интеллект добавить (R1 — philosophy + methodology + sota-tracker + ml-ai)

1. **Коллективный/распределённый интеллект** (systems-expert + ml-ai): ROY swarm + MAS scaling
   — интеллект не только индивидуальный; кооперация *сама есть* форма коллективного интеллекта
   (group выше суммы). Связь с #14 Сеть.
2. **Интеллект как уровень оперирования** (Levenchuk, methodology-engineer): «умнее» = способен
   работать на правильном уровне абстракции (мета-уровень). Ложится на meta-method.
3. **Стоический угол** (philosophy-expert): ответственность = «дихотомия контроля» + долгосрочная
   агентность; интеллект включает эмоц. саморегуляцию (не только расчёт). Method V2 motivational stack.
4. **Bloom-прогрессия** (#7 Образование): forecasting depth тренируема (не fixed) → интеллект =
   развиваемый skill tree, не данность (anti-IQ-fatalism; согласуется с #13 Мастерство).
5. **SOTA-угол** (sota-tracker): в эпоху AI «интеллект» сдвигается от хранения/расчёта (делегируемо
   машине) к **выбору горизонта + ответственности за выбор** (то, что НЕ делегируемо) — точно то,
   что Ruslan назвал ядром.

### ⚠️ R12-VERDICT — LOW-MED (influence-ethics RECEIVER + philosophy)

| Surface | Вердикт |
|---|---|
| «интеллект = горизонт + ответственность» | ✅ POSITIVE — non-extractive, развивает СВОЙ интеллект участника (Method V2 R12-conformant) |
| **отбор «ответственных»** | ⚠️ **SCREEN** — capability-fit ✅, НО не превращать в loyalty-test / status-shaming «безответственных» (cont. O-270 selectivity) |
| «дальше просчитал» как превосходство | ⚠️ держать как развиваемый skill (anti-IQ-fatalism), НЕ как касту «умных vs глупых» |

### → Куда (R1)

- **Wiki Tier A/B candidate:** концепт `intelligence-responsibility-cooperation` (связка 3↔4) —
  кандидат на отдельную concept-страницу (R1; не материализовал в Phase 1 т.к. это
  synthesis-гипотеза, не voice-anchor). Ruslan ack → materialize.
- **Направление:** обогащает **#1 Метод** + **#13 Мастерство** + **#10 Ценности** (определение
  интеллекта = ценностный слой). НЕ новое направление.
- **Презентация:** усиливает P-2 (Метод) и P-1 (WHY) — «что мы развиваем = горизонт + ответственность
  = способность к долгой кооперации». Также moat-аргумент (P-1): люди, отобранные/развитые по этим
  осям, = устойчивое кооперативное ядро (смыкается с Концептом 3 moat).

---

## §Свод — 4 концепта как один контур

```
         §3 GAME THEORY            §4 INTELLIGENCE
      (почему кооперация            (кто удерживает
       = равновесие)         ←→     равновесие: δ→1 + ответственность)
            │                              │
            │  mechanism design            │  human capital
            ▼                              ▼
         §2 CRYPTO/COINS  ──enforced in code──►  R12 движок
      (чем enforced: QF/cap/exit/SBT)
            │
            ▼
         §1 INVEST-FUND
      (как реинвестируется ценность: treasury → система + проекты)
```

**Один R12-вывод на все 4:** контур работает, **только если** 4 guards держатся
(`extraction_beyond_share` / `wage_ratio_violation` / `fork_prevention_attempt` /
`non_consensual_distribution`). Без них фонд (#1) = доение, коины (#2) = спекуляция,
mechanism design (#3) = манипуляция, отбор «ответственных» (#4) = каста. **R12 = то, что
держит все 4 концепта на здоровой стороне.** Это и есть «нагнуть теорию игр» этично.

**Ни один из 4 НЕ требует нового направления** (рекомендация роя): все ложатся суб-гранями в
#4/#8/#14/#1/#13. Единственный direction-candidate для §14-решения = **#18 Инвест-фонд**
(R1 surface, рой рекомендует НЕ выделять — суб-грань #4). Ruslan picks.
