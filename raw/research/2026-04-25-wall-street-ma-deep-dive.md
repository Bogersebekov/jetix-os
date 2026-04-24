---
id: wall-street-ma-deep-dive-2026-04-25
title: "Wall Street Deep Dive — M&A, Private Equity, Hedge Funds + AI-leverage strategy для Jetix"
date: 2026-04-25
type: research-deep-dive
state: raw
tier: tier-1-source-material
author: external-research-agent (provided by Ruslan)
delivered_by: ruslan-handoff
binding: input-only (not a decision; informs Phase-2 L7 + new M&A direction integration)
relates_to:
  - decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md (will receive M&A direction integration)
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md (Mittelstand ICP overlap)
  - decisions/JETIX-VISION.md (D11 Investment-fund philosophy)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (AI-leverage thesis)
key_insights_for_jetix:
  - "Mittelstand succession crisis: 560k companies seeking exit by end-2026; 190k will close without buyer; 3:1 demand/supply asymmetry per DIHK"
  - "AI atomizes M&A workflow Layers 1-5 (sourcing/analysis/modeling/DD/document-gen) by 60-90%"
  - "Layers 6-9 (process/negotiation/trust/judgment) remain human; this is where MD-value lives"
  - "1 senior partner + 2-3 mid-level + AI infrastructure = output equivalent to 17-person traditional team"
  - "Revenue projection AI-augmented boutique: €5-15M/year (6-10 closings @ €1-2M success-fee average)"
  - "3 candidate models for Jetix: M&A Boutique Advisory / Search Fund (ETA) / Alliance + implicit deal flow"
  - "Recommended hybrid: Model 1 (advisory) + Model 3 (alliance) — synergistic with existing Jetix infrastructure"
  - "Critical missing piece: senior co-founder with real M&A background (ex-Lincoln/IMAP boutique-partner level)"
  - "Window open ~2026-2028; Mittelstand AI-adoption from 7%→37% in 2 years (Dealsuite); category will close ~2027-28"
tags: [ma, private-equity, hedge-funds, mittelstand, succession-crisis, eta, search-fund, ai-leverage, wall-street, research]
---

# Wall Street Deep Dive: M&A, Private Equity, Hedge Funds и AI-leverage для Jetix

**Подготовлено для:** Ruslan, Founder/CEO Jetix
**Дата:** 25 апреля 2026
**Формат:** Аналитический отчёт со стратегическими выводами

---

## TL;DR — главный тезис в трёх абзацах

Wall Street — это машина по трансформации **информационной асимметрии и доверия** в деньги. Аналитик зарабатывает $30k за то, что строит модели; партнёр зарабатывает $5M за то, что у него есть отношения с CEO. Между ними — пропасть, и AI её **не закрывает**, а наоборот, обнажает: то, что было "престижной работой высокого класса" (моделирование, due diligence, генерация pitch books), стало commodity. То, что осталось дефицитным (доверие, judgment, deal access), стало ещё дороже.

Структурный сдвиг 2024-26: PE-индустрия выросла до $4+ трлн AUM, при этом **верхушка** (Blackstone $1T, Apollo $840B, KKR $686B) консолидирует капитал, оставляя огромное пространство для нишевых игроков снизу. В Германии параллельно идёт **Mittelstand succession crisis**: до конца 2026 года ~560,000 компаний ищут преемников, ~190,000 закроются без покупателя. Это асимметрия исторического масштаба.

**Применение для Jetix:** не пытаться стать "AI-powered Goldman Sachs" — это бессмысленно. Стратегия: использовать AI как **leverage-multiplier** для гибридной модели "консалтинг + M&A advisory + search fund". Конкретно — стать AI-augmented боутиком, который обслуживает Mittelstand сделки €5-50M (зону, которую большие банки игнорируют), и параллельно строит позицию для собственных acquisitions через ETA-модель. AI здесь не заменяет MD — он позволяет одному человеку с правильной экспертизой делать работу команды из 5-7.

---

## ЧАСТЬ 1. Что такое M&A на самом деле

### 1.1. Зачем компании делают M&A

Прежде чем разбирать механику, надо понять **мотивацию**. Без этого все модели и таблицы повисают в воздухе. M&A сделки делаются по 6 базовым причинам:

**1. Synergies (синергии).** Самая декларируемая причина, самая часто переоцениваемая. Бывают двух типов:
- *Cost synergies* — закрыть дублирующие функции (HR, IT, headquarters), консолидировать поставщиков, закрыть избыточные мощности. Это самое простое, что можно посчитать. Когда Bayer покупал Monsanto в 2018, было заявлено $1.2B годовых cost synergies.
- *Revenue synergies* — cross-selling в объединённую клиентскую базу, географическое расширение, complementary product lines. **Эти почти никогда не материализуются** в обещанном объёме. Это известная проблема — McKinsey оценивает, что 70%+ M&A сделок не достигают заявленных revenue synergies.

**2. Defensive consolidation.** Купить конкурента, чтобы не быть купленным; купить, чтобы убрать ценовое давление; купить supplier-а, чтобы контролировать цепочку. Когда Disney покупал Fox в 2019 за $71B — это было защитой от Netflix.

**3. Acquisition of capabilities.** Купить технологию, команду, IP, который дешевле/быстрее купить, чем построить. Microsoft/GitHub ($7.5B, 2018), Microsoft/Activision ($69B, 2023), Salesforce/Slack ($27.7B, 2021). Это особенно актуально в AI-эру: крупные компании сейчас активно скупают AI-стартапы — Bosch, Knorr-Bremse, Siemens среди немецких. В Германии, как отмечают исследования рынка, AI-продукты стали ключевым драйвером M&A: компании используют сделки для приобретения AI и digitalization capabilities.

**4. Financial engineering / arbitrage.** Купить, разделить, продать частями за большую сумму, чем купил целиком (классический LBO playbook 80-х). Купить недооценённое, нанять менеджмент, продать дороже. Это zone of PE-фондов.

**5. Roll-ups / buy-and-build.** Купить много мелких компаний в фрагментированной отрасли, объединить, получить scale, продать целое за multiple-uplift. Если 20 региональных HVAC-компаний торгуются по 4x EBITDA, то консолидированная компания на $200M EBITDA продаётся за 9x EBITDA. **Это сейчас доминирующая стратегия в Mittelstand сегменте**: PE-фонды в 2025 фокусируются на buy-and-build (это явно отмечено в немецких рыночных отчётах) — особенно в professional services, где Eurazeo купил OMMAX, Investcorp купил Miebach, EQT купил WTS Group.

**6. Succession / liquidity для founders.** Владелец стареет, дети не хотят бизнес, нужен exit. Это **именно то, что сейчас происходит с Mittelstand в массовом масштабе**.

### 1.2. Типы сделок — подробно

```
                         M&A landscape
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Strategic               Financial            Hostile/
   (corporate)             (PE/HF)              Friendly
        │                     │                     │
   Industry buyer         LBO/buyout          Tender offer
   buys for synergy       for return          vs negotiated
```

**Strategic vs Financial buyer.** Это критическое различие.

*Strategic* — корпорация, покупающая для стратегической выгоды. Готова платить премию за synergies. Долгосрочный horizon. Часто ставит вопросы: "Где это вписывается в нашу стратегию?", "Можем ли мы интегрировать?", "Как это повлияет на наш bunching рынков?"

*Financial* — PE-фонд или hedge fund. Покупает за финансовую доходность. Holding period 3-7 лет. Думает: "Какой IRR я получу?", "Какие operational improvements я могу сделать?", "Как и когда я выйду?"

Один и тот же актив может стоить совершенно разные деньги для двух типов покупателей. Strategic обычно платит больше (потому что у него synergies). PE платит больше, когда есть очевидный operational improvement или buy-and-build потенциал.

**Sell-side vs Buy-side advisory.** Когда инвестбанк работает с продавцом (sell-side), его задача — максимизировать цену через создание competitive auction. Когда работает с покупателем (buy-side) — найти target, оценить, помочь договориться о хорошей цене.

Sell-side обычно прибыльнее для банка (success fees выше — 3-6% для mid-market vs 1-2% для buy-side), но требует больше работы по подготовке материалов.

### 1.3. Анатомия сделки — что реально анализируется

Возьмём типичную mid-market сделку: немецкий Mittelstand €30M EBITDA, продаётся за ~7x = €210M EV.

**Phase 1: Preparation (3-6 месяцев)**

Sell-side банк готовит:

- **Information Memorandum (IM/CIM)** — главный маркетинговый документ. 60-150 страниц. Описывает: компанию, рынок, продукты, финансовое состояние, management team, growth potential. Это самый важный документ — на нём строится первичная оценка покупателями.
- **Financial Model** — Excel, обычно 5-летний прогноз с тремя сценариями. Включает: P&L, Balance Sheet, Cash Flow, working capital assumptions, capex schedule. На этом считается DCF (discounted cash flow).
- **Vendor Due Diligence (VDD)** — отчёты от Big 4 (KPMG, PwC, EY, Deloitte) по финансам, налогам, юридике, коммерции. Чтобы покупатели не задавали миллион вопросов в diligence-е, продавец предоставляет уже подготовленные отчёты. Стоит €200-500k, но ускоряет процесс.
- **Quality of Earnings (Q of E)** — детализированный анализ "качества" EBITDA: какая часть recurring, какая one-off, какие normalizations нужны. €35-200k.
- **Management Presentation** — деки для управленческих встреч с покупателями.

**Что физически анализируется:**

1. *Quality of revenue.* Recurring vs one-time. Customer concentration (>30% от одного клиента — red flag). Contract length и retention. Pricing power. Market share и trends.

2. *Quality of EBITDA.* "Adjusted EBITDA" — это всегда упражнение в манипуляции. Add-backs (одноразовые расходы, которые добавляются обратно): юридические fees от прошлых судов, разовые маркетинговые акции, owner compensation выше market rate. Покупатель будет оспаривать каждый add-back.

3. *Working capital dynamics.* DSO (days sales outstanding), DPO (days payable outstanding), DIO (days inventory outstanding). Сезонность. Это критично, потому что в большинстве сделок есть **working capital adjustment** — целевое NWC, и если на closing-е фактическое отличается, цена корректируется.

4. *Capex requirements.* Sustaining capex vs growth capex. Это сильно влияет на FCF (free cash flow), что и определяет valuation.

5. *Customer/supplier diligence.* Часто включает прямые звонки топ-10 клиентам и поставщикам (с разрешения продавца) для проверки отношений и retention.

6. *Operational diligence.* IT systems, HR, manufacturing capacity, supply chain risks.

7. *Legal/regulatory.* Litigation, IP, contracts, change-of-control clauses, regulatory licenses.

8. *Environmental.* Особенно важно в Германии — ESG due diligence стала стандартом, brownfield sites могут иметь огромные liabilities.

9. *Tax structure.* Optimal acquisition structure (asset deal vs share deal, tax-efficient routing).

**Phase 2: Marketing (2-4 месяца)**

- *Long list* — 50-200 потенциальных покупателей.
- *Teaser* — анонимная 2-страничная outline, рассылается потенциальным.
- *NDA* (Non-Disclosure Agreement) — подписывается заинтересованными.
- *CIM* — рассылается после NDA.
- *Initial Bids* — обычно 4-8 недель после CIM. Не binding, но указывает "indicative price range".
- *Management presentations* — 4-8 фаворитов встречаются с командой target.
- *Data Room access* — открывается доступ к виртуальной комнате с тысячами документов.
- *Final Bids* — binding offers после due diligence.

**Phase 3: Negotiation & Closing (2-4 месяца)**

- Negotiation of SPA (Share Purchase Agreement) — основной документ, 100-300 страниц.
- Reps & warranties (заверения и гарантии) — продавец даёт, покупатель опирается на них.
- W&I insurance (warranty & indemnity insurance) — страховка от breach of reps.
- Earn-outs, escrows, holdbacks — отложенные платежи, привязанные к performance.
- Regulatory clearances — antitrust, foreign investment review.
- Closing — money flows, ownership transfers.

### 1.4. Почему так дорого и сложно — что делают консультанты

Возьмём ту же €210M сделку. Ставка комиссии sell-side advisor: ~2.5% = ~€5.25M (плюс retainer €30-50k/месяц).

**За что платят:**

1. **Process management.** Координация 5+ workstreams: финансовый, юридический, налоговый, коммерческий, операционный. В сделке участвует 30-50 человек со стороны продавца (банкиры, юристы, аудиторы, консультанты, менеджмент). Без координатора это разваливается.

2. **Maximizing competitive tension.** Это главное искусство sell-side advisor. Чем больше серьёзных bidders, тем выше цена. Создание иллюзии (или реальности) competitive auction может поднять цену на 20-30%. Это buyer access — кто сидит на телефоне с потенциальными покупателями.

3. **Structuring** — какую структуру предлагать (asset vs share deal), как обходить налоги, как оптимизировать earn-outs.

4. **Negotiation tactics.** Когда показать слабину, когда блефовать, когда подключать другого bidder, как использовать deadline pressure.

5. **Closing certainty.** ~30% сделок разваливаются между LOI (letter of intent) и closing. Опытный advisor знает, как держать сделку в движении: где compromis, где hold firm, как управлять emotional dynamics founder-а, который продаёт life's work.

**Главный инсайт:** комиссия €5M — это не плата за работу. Это плата за **разницу в final price**. Если без advisor компания продастся за €180M, а с advisor за €230M — €5M комиссии всё ещё дают net +€45M продавцу. **Advisor зарабатывает свою комиссию через delta в final price.**

---

## ЧАСТЬ 2. Private Equity — как работает машина

### 2.1. Структура PE-фонда

Это первое, что надо понять — PE-фирма не одна сущность. Это иерархия:

```
                  ┌─────────────────┐
                  │  PE FIRM (GP)   │  ← Blackstone, Apollo, KKR
                  │  (General       │     Управляющая компания
                  │   Partner)      │
                  └────────┬────────┘
                           │ creates and manages
                           ▼
        ┌──────────────────────────────────┐
        │         FUND (vehicle)           │  ← Blackstone Capital Partners IX
        │                                  │
        │  ┌─────────┐    ┌─────────┐     │
        │  │ LP1     │    │ LP2     │ ... │  ← Pension funds, sovereigns,
        │  │ Pension │    │ Sovereign│    │     endowments, family offices
        │  │ commits │    │ commits │     │
        │  │ $500M   │    │ $300M   │     │
        │  └─────────┘    └─────────┘     │
        └──────────┬───────────────────────┘
                   │ invests in
                   ▼
        ┌──────────────────────────────┐
        │   PORTFOLIO COMPANIES        │
        │   (Hilton, Refinitiv,        │
        │    Toys R Us, etc.)          │
        └──────────────────────────────┘
```

**General Partner (GP) = PE firm** — Blackstone, KKR, Apollo. Они управляют фондами и принимают инвестиционные решения. Партнёры PE-фирмы — реальные владельцы.

**Limited Partners (LPs)** — те, кто даёт деньги. В основном это:
- Pension funds (CalPERS, ADIA, GPIF) — самый большой источник
- Sovereign wealth funds (Norway's NBIM, Saudi PIF)
- Endowments (Yale, Harvard — Yale's David Swensen первым активно инвестировал в PE в 80-х)
- Insurance companies
- Family offices wealthy individuals
- Funds of funds

Когда говорят "Blackstone manages $1 trillion" — это значит, что LPs commited $1 трлн в фонды Blackstone. Это **не деньги Blackstone**. Это деньги, которые Blackstone **распоряжается**.

### 2.2. Экономика PE — "2 and 20"

Классическая модель компенсации:

- **2% management fee** — на committed capital, ежегодно. На $10B фонд = $200M/год просто за управление, независимо от results.
- **20% carried interest (carry)** — после того как LPs вернули свой капитал плюс 8% preferred return ("hurdle rate"), GP получает 20% всей последующей прибыли.

Пример: $1B фонд, 7-летний holding, фонд возвращает $3B (3x MOIC, ~17% IRR).

- LPs получают свой $1B обратно + 8% preferred = ~$540M
- Profit above hurdle = $3B - $1B - $540M = $1.46B
- GP carry = 20% × $1.46B = $292M
- LPs получают остальные 80% = $1.17B

Plus management fees за 7 лет = ~$140M (на invested capital).

**Итого GP получает ~$432M** за управление $1B. Это объясняет, почему партнёры PE-фондов настолько богаче, чем Wall Street MDs — единичный успешный фонд приносит партнёру десятки миллионов.

### 2.3. Leveraged Buyout (LBO) — механика

Это ключевой инструмент PE. Возьмём упрощённый пример:

**Цель:** купить компанию за $1B EV.
**Структура финансирования:**
- $400M equity (от PE-фонда)
- $600M debt (банки, mezzanine, high-yield bonds)

**5 лет спустя:**
- EBITDA выросла с $100M до $150M (50% рост за 5 лет = ~8.5% CAGR — реалистично для buy-and-build)
- Multiple expansion: купили за 10x EBITDA, продали за 11x = $1.65B EV
- Долг частично выплачен из cashflow: $600M → $300M

**Returns:**
- Sale price: $1.65B
- Pay off remaining debt: -$300M
- Equity proceeds: $1.35B
- vs initial equity: $400M
- **Return: 3.4x MOIC, ~28% IRR**

**Откуда returns в LBO:**
1. **EBITDA growth** (50% × $400M equity = $200M value creation)
2. **Multiple expansion** (от 10x к 11x = $150M, возможно через buy-and-build, отраслевую тенденцию, или просто timing market)
3. **Debt paydown / financial leverage** (это "магия" — без leverage те же operational improvements принесли бы только 1.65x MOIC. С leverage получается 3.4x.)
4. **Tax shield** от процентных выплат (debt interest is tax-deductible)

Это и есть фундаментальный принцип PE: **leverage умножает returns на equity**. Когда дёшево занимать (как в 2010-2021), PE летит. Когда дорого (как с 2022 после rate hikes) — индустрия adjustment-ится.

### 2.4. Big Four PE: что они реально делают

**Blackstone** ($1T AUM) — крупнейший. Структурно diversified:
- Real estate (~30%) — крупнейший в мире landlord
- Private equity (~20%)
- Credit & insurance (~33%) — растёт быстрее всех
- Hedge fund solutions, tactical opportunities — остальное

Blackstone придерживается "capital-light, fee-based" модели — много management fees на огромный AUM.

**Apollo** ($840B AUM, цель $1T к концу 2026) — фокус на credit и distressed.
- Credit — основной бизнес. Apollo владеет Athene (life insurance), которая даёт permanent capital — деньги с long-duration liabilities, которые можно вкладывать в illiquid yield assets.
- Apollo продемонстрировала контртрендовый подход в начале 2025: вложила $2B+ в четыре сделки за 2 месяца после announcement тарифов, поддерживая агрессивный dealmaking несмотря на market volatility.

**KKR** ($686B AUM, рост 18% CAGR с 2010, цель $1T к 2030) — основатели pioneer-ы LBO (RJR Nabisco $31B сделка 1989, описанная в "Barbarians at the Gate").
- Diversified: PE ($183B), credit ($260B), infrastructure ($61B), real estate ($71B)
- В Q3 2025 KKR подняла $43B fresh capital — самый сильный квартал за 4 года.
- Только что (конец 2025) объявили $50B стратегическое партнёрство с Energy Capital Partners для AI infrastructure (data centers + power generation) — это showing где big money сейчас идёт.

**Carlyle** ($426B AUM) — diversified, балансирует buyouts, real assets, ESG-focused investing.

### 2.5. Где PE сегодня — структурные сдвиги 2024-26

**1. Private credit становится больше PE.**

В 2024 у Blackstone credit&insurance стало 33% AUM (vs PE 31%). У Apollo credit — главный бизнес. Это **historical inversion** — PE-фонды стали в основном debt-фондами.

Почему: после 2008 банки стали менее охотно кредитовать средний рынок (Basel III, regulatory capital requirements). Эту нишу заняли private credit funds. К 2025 индустрия достигла $2T+ и продолжает расти 15-20%/год.

Для немецкого Mittelstand это критично: компании средней руки всё чаще занимают не у Sparkasse, а у Apollo / Blackstone Credit / Ares.

**2. Infrastructure и energy для AI**

KKR, Blackstone, Apollo сейчас активно строят позиции в data centers, power generation (modular nuclear), renewable infrastructure. Это новый core asset class — "AI infrastructure" treated как новая category. Тренд "Innovation Supercycle" по терминологии индустриальных аналитиков.

**3. Mid-market PE как место максимальных returns**

Mega-fund returns стабилизируются (просто слишком много денег chase одни и те же deals). Mid-market фонды ($1-5B) — где исторически были лучшие returns, и где их продолжают ожидать.

**4. Германия / Mittelstand специфика**

В Германии PE традиционно был менее agressive чем в US/UK. Но сейчас:
- Mittelstand selectively selling (succession crisis + 560k owners ищут exit)
- Sellers требуют high valuations, медленные процессы (due diligence стало longer)
- US strategic buyers активно входят (диверсификация против tariffs/geopolitics)
- ETA / search funds начинают распространяться (виден активный германский ETA-комьюнити, Search Fund Hub, Tilia Nachfolgekapital и др.)

---

## ЧАСТЬ 3. Hedge Funds — другой зверь

### 3.1. Принципиальное отличие от PE

| Параметр | Private Equity | Hedge Funds |
|----------|---------------|-------------|
| Holding period | 3-7 лет | Дни — месяцы |
| Liquidity | Locked up | Quarterly/monthly redemptions |
| Asset target | Whole companies | Public securities, derivatives |
| Value-add | Operational improvement | Market timing / arb |
| Fund size | Massive ($10B+) | Variable ($1B-$60B) |
| Returns | IRR 15-25% | Variable — but 10-20% top funds |
| Strategy | Buy → improve → sell | Trade based on edge |

PE — это **operating business** маскированный под investment. HF — чистая trading machine.

### 3.2. Hedge Fund стратегии — таксономия

**Long/Short Equity** — самая распространённая. Покупаешь акции, которые считаешь underpriced, продаёшь short то, что overpriced. Beta-neutral по конструкции. Pioneer — A.W. Jones (1949). Современные: Tiger Global, Coatue, Maverick.

**Global Macro** — ставки на курсы валют, процентные ставки, commodity cycles на основе макроэкономического анализа. Bridgewater (Ray Dalio) самый известный. George Soros 1992 ставка против фунта = $1B за день.

**Event-Driven** — спекуляция на конкретных корпоративных событиях:
- *Merger arb* — покупка target после announced M&A, ставка что сделка закроется
- *Distressed* — bankruptcy / restructuring (Elliott Management известен этим)
- *Activist* — взятие позиции и push на change (Pershing Square, ValueAct)

**Quantitative** — алгоритмы и data. Это самый растущий сегмент. Подразделяется на:
- *Statistical arbitrage* — ловля mean-reversion patterns в high-frequency data
- *Trend following* / managed futures — Winton, AQR
- *Market making* — Citadel Securities, Jane Street

**Credit / Fixed Income arb** — ставки на спреды между bond prices.

### 3.3. Quant Funds — где живёт magic

Это самая интересная категория для понимания "куда движется индустрия".

**Renaissance Technologies (RenTech)** — лeгендарный quant fund. Основан Jim Simons (математик, бывший cryptographer для NSA). Medallion Fund — внутренний фонд только для сотрудников — вернул **66% gross annualized с 1988 по 2018**. Это самая высокая sustained return в истории финансов. В 2024 Medallion вернул 30%, при этом institutional funds вернули 22.7% (RIEF) и 15.6% (RIDA).

Как они это делают: огромная команда PhD по математике, физике, computer science. Они находят микроскопические patterns в данных, которые исчезают через дни или недели. Используют thousands strategies одновременно. Никогда не публикуют, как именно работают — это **самый закрытый investment process в мире**.

**Two Sigma** ($60B AUM) — основан John Overdeck и David Siegel (бывшие D.E. Shaw quants). Tech-driven, machine learning, distributed computing. Flagship Spectrum fund в 2024 вернул 10.9%, Absolute Return Enhanced 14.3%.

**Citadel** (Ken Griffin) — multi-strategy mega fund. ~$65B AUM. Классический пример "platform" модели — много pod-ов trading разных стратегий, жёсткая risk management в центре. Citadel Securities (отдельная entity) — один из крупнейших market makers в мире, исполняет ~25% всего US equity trading volume.

**D.E. Shaw** — research-intensive, AI + computational finance. Основан David Shaw (computer scientist). Jeff Bezos работал там до Amazon.

**Jane Street** — ультра-секретная HFT/market making firm. Использует OCaml language. Платит $300-500k стартовая зарплата для new grads (выше Goldman analyst). Из ex-Jane Street сотрудников вышли многие основатели AI-компаний.

### 3.4. Откуда у них деньги

LP-структура у HF проще чем у PE:
- Накопления HNWI (high net worth individuals) — $5M+ minimum обычно
- Funds of funds, which aggregate
- Pension funds, endowments, sovereigns
- Family offices

Многие топ-фонды **закрыты** для new investors. RenTech Medallion Fund доступен **только сотрудникам** — outside money turned away. Citadel закрывал inflows многократно.

Вот ключевое отличие: PE-фонды постоянно raise new funds (Blackstone Capital Partners V, VI, VII, VIII...). HF обычно работают как continuous vehicle — деньги входят и выходят квартально.

### 3.5. Compensation realities

HF compensation для топ-производителей:
- *Portfolio Manager* в multi-strategy fund: $1-5M base + 10-20% от P&L книги. Хороший PM, generating $50M alpha, может получать $5-10M.
- *Quant researcher* в Renaissance: $500k-$5M+
- *Trader* в Citadel pod: highly variable, top traders получают десятки миллионов.
- *Founder* топ-фонда: миллиарды. Ken Griffin (Citadel) — net worth ~$45B. Jim Simons — был ~$30B на смерть в 2024.

Сравните с Wall Street MD ($2-5M typical) — HF/PE верхний эшелон **на порядок** выше.

---

## ЧАСТЬ 4. Главный вопрос — что делает MD незаменимым

Это самый важный концептуальный вопрос в твоём списке. Ответ: дело не в "связях" в наивном смысле. Дело в **моаде доверия**.

### 4.1. Что такое "связи" на самом деле — anatomy of trust capital

Когда говорят, что у Боба Рубина (Goldman Sachs, 1960s-90s) был telephone-роди CEO Coca-Cola — это не значит, что Боб мог "позвонить и узнать котировки". Это значит, что:

1. CEO Coca-Cola **доверяет конкретно Рубину** информацию, что компания думает о acquisition
2. CEO **верит**, что Рубин не сольёт это конкурентам
3. CEO **знает по 20 годам опыта**, что Рубин даст honest advice (даже против commission interests)
4. CEO **видел**, как Рубин справлялся с similar situations

Это не просто отношения. Это **накопленный capital доверия**. Который:
- Строится годами и десятилетиями
- Может быть потерян за один проступок
- **Не передаётся** между людьми (нельзя сказать "новенький Joe возьмёт твоего клиента")
- Имеет асимметричную ценность — одна высоко-уровневая связь может стоить миллионы, тысяча средних — почти ничего

### 4.2. Что конкретно делает MD во время сделки

**До сделки (origination, 80% работы):**
- Знает, кто из CEO думает о selling/buying
- Знает приватную информацию о готовности (CEO разводится → личная liquidity нужна; CFO уволили → расstroyed strategic plan; founder сделал 70 → succession crisis в близкой перспективе)
- Поддерживает relationship через breakfast/dinners/golf 5-10 раз/год даже когда ничего не происходит
- Когда CEO решает "пора" — звонит в первую очередь conditioning trusted advisor

**Во время сделки (judgment moments):**
- "Stop the auction here, take this bid" — когда останавливать и принимать предложение, а когда давить дальше
- "Bring in this third party" — кого ещё подключить как stalking horse bidder
- "We need to speak privately with the buyer's CEO" — когда переходить на CEO-level conversation
- Negotiation tactics с другой стороной (которую MD тоже знает 20 лет)
- Crisis management когда сделка валится

**После сделки (legacy):**
- Семья продавца, employees, community ему доверяют
- Это repeats — следующий sale или acquisition этого CEO опять придёт к нему

### 4.3. Почему это сложно автоматизировать

**Информационная асимметрия не в данных, а в нюансах.** AI может просканировать SEC filings, но не знает, что CFO компании tipsy на ужине в Hamptons сказал, что они **уже** нашли buyer-а, просто ещё не announced. Это knowledge не в датасетах.

**Trust требует time-in-market.** Даже если AI generated perfect pitch deck завтра, CEO Coca-Cola не отдаст $50B сделку AI-системе. Он позвонит человеку, которого знает.

**Judgment under uncertainty.** Когда сделка discrete — "ваш CEO sleeps with our CEO's wife", "regulator может зарубить", "конкурент готовит hostile bid" — нужно мгновенное human judgment в нюансированном контексте.

**Reputational hostage.** Banker рискует своей repuation на каждой сделке. Если он "cheat" клиента, ему конец — и индустрия знает это. AI не имеет таких stakes.

### 4.4. **Где AI на самом деле ломает старую модель**

Но! И это ключевое для твоей стратегии:

AI не заменяет MD. AI **разрушает обоснование** для целой army of associates и VPs, которые поддерживали MD.

Раньше структура была: 1 MD : 3 VPs : 6 associates : 12 analysts. Это пирамида, которая существовала потому, что для исполнения сделки нужно было 80,000 человеко-часов работы.

С AI tools (Rogo, Hebbia, AlphaSense, и т.д.) эта работа **сокращается на 60-80%**. Согласно индустриальным отчётам, AI уже автоматизирует:
- CIM analysis за минуты вместо дней
- Comparison across 50 CIMs одновременно
- First drafts of pitch books, IM-ов
- Financial modeling templates
- Due diligence document review (Hebbia заявляет 75% time reduction)
- Comp analysis, precedent transactions

Например: фирма Rogo в апреле 2025 подняла $50M Series B, valuation $350M, и активно используется Lazard, Moelis, Nomura. Их founder Gabriel Stengel (бывший Lazard analyst) явно сказал: "Banks that adopt AI will win more deals, generate more revenue, higher revenue per employee."

**Что это означает структурно:** старый "junior banker" уровень становится unnecessary. **Один умный человек с правильным AI tooling может делать работу команды из 5-7 ассоциатов.**

И вот тут для тебя открывается окно.

---

## ЧАСТЬ 5. AI-leverage — что меняется и что нет

### 5.1. Слои работы и их automation potential

```
МОДЕЛЬ AUTOMATION ПО СЛОЯМ M&A WORKFLOW

Layer 1: Sourcing & Screening    ████████████░ 85% automatable
Layer 2: Initial Analysis        ███████████░░ 80% automatable
Layer 3: Financial Modeling      █████████░░░░ 70% automatable
Layer 4: Due Diligence           ████████░░░░░ 65% automatable
Layer 5: Document Generation     █████████████ 90% automatable
Layer 6: Process Management      ██████░░░░░░░ 45% automatable
Layer 7: Negotiation             ██░░░░░░░░░░░ 15% automatable
Layer 8: Trust / Origination     ▒░░░░░░░░░░░░ 5% automatable
Layer 9: Judgment in Crisis      ░░░░░░░░░░░░░ 0% automatable
```

**Что AI делает превосходно (Layer 1-5):**

*Layer 1 (Sourcing).* Можно построить агента, который continuously мониторит:
- Bundesanzeiger filings
- Handelsregister changes
- LinkedIn для key personnel changes (CFO leaves, CEO retires)
- News mentions для signals (succession, divestiture, restructuring rumors)
- Patent filings, M&A databases, industry conferences

Это **то, что раньше делал отдел из 5 джуниоров**. Один AI-pipeline может это делать в 1000x масштабе.

*Layer 2 (Initial Analysis).* Дав CIM или teaser — AI оценивает за 5 минут:
- Базовые финансовые метрики (revenue, EBITDA, growth, margins)
- Customer concentration risks
- Industry positioning
- Likely valuation range
- Red flags

*Layer 3 (Financial Modeling).* DCF templates, comp tables, precedent transactions — всё automatable. Standard LBO models — 10 минут вместо 10 часов. Sensitivity analysis — instant.

*Layer 4 (Due Diligence).* Hebbia phenomenally хороша — может ответить на questions cross-thousands documents в data room: "Where are change-of-control clauses?", "What's customer churn rate in 2023 vs 2022?", "Are there pending lawsuits?".

*Layer 5 (Document Generation).* Pitch books, IMs, investor memos — first drafts генерируются в часы, не недели.

**Что AI делает плохо (Layer 6-9):**

*Layer 6 (Process Management).* Можно automate notifications, deadlines, document tracking. Но реальное project management между 30 stakeholders с conflicting interests — это эмоциональная работа.

*Layer 7 (Negotiation).* Можно prep arguments, simulate scenarios. Но реальная negotiation — это reading room, sensing weakness, knowing when to bluff. Это пока за пределами AI.

*Layer 8 (Trust / Origination).* CEO выбирает с кем talk based on relationship history. AI здесь не at the table.

*Layer 9 (Judgment in Crisis).* "Сделка вот-вот сорвётся, CEO в истерике, конкурент launched hostile bid — что делаем?" Это требует years of pattern recognition в high-stakes situations.

### 5.2. Стратегическое следствие — где living wage

Возникают **two equilibrium states** в индустрии:

**A. Top tier (Layer 8-9 dominant):** Senior bankers с trust capital. Becoming MORE valuable, потому что AI commodititized всё below их. Goldman MD сегодня зарабатывает больше реально, чем Goldman MD 1995, потому что один человек теперь leverage от AI larger team.

**B. AI-augmented mid-tier (Layer 1-5 dominant):** Solo operators / small teams делающие то, что 10 лет назад требовало 50 человек. Возможный пример — boutique advisor с 3 партнёрами + AI делающие 20 mid-market deals/год = $30-50M revenue.

**Disappearing middle:** Old-school analyst/associate roles в bulge bracket. Уже идёт — индустрия hires меньше juniors. Через 5 лет это будет dramatically.

### 5.3. Где **именно** ты можешь оперировать

Возьмём AI-augmented model для mid-market M&A в German Mittelstand:

**Что нужно:**
- 1 senior partner (это ты или кто-то senior + ты как orchestrator) — handles relationships, judgment, negotiation
- 2-3 mid-level operators — управляют processes, проверяют AI output
- AI infrastructure — Rogo/Hebbia/custom built на Anthropic API
- Network — связи в Mittelstand сообществе, Verbänden, network of trusted partners (lawyers, tax advisors, Big 4)

**Output capacity:**
- Process: 15-25 sell-side mandates parallel
- Closing: 6-10 deals/year
- Average fee: €250k-€2M (mid-market)
- **Revenue: €5-15M/год**

Сравни с traditional структурой того же output:
- 1 MD + 3 VPs + 5 associates + 8 analysts = 17 people
- Cost: ~€8-12M/год payroll
- AI-version: 4-5 people = ~€2-3M payroll + €500k AI tools

Margin difference dramatic. **AI-leverage превращает M&A advisory из people-heavy в capital-light business.**

---

## ЧАСТЬ 6. Mittelstand opportunity — твоя ситуация

### 6.1. Размер рынка

Это исторически уникальная ситуация. Сводные данные:

- **560,000 Mittelstand companies** ищут succession до конца 2026
- **190,000** планируют exit рынка (закрытие) если не найдут buyer
- **57%+ Mittelstand owners** старше 55 лет
- **42%** family businesses не имеют family successor
- **Demand/supply asymmetry:** "Number of business owners seeking succession solutions is three times higher than the number of interested buyers" (DIHK)
- В крупном сегменте Mittelstand: **1,200 компаний с >€50M revenue** ищут transfer 2022-2026

Это **самая большая wave succession в истории Германии**. И она происходит в стране, где Mittelstand генерирует ~50% GDP, employs ~60% workforce.

### 6.2. Where are big banks

Bulge bracket banks (Goldman, Morgan Stanley, JP Morgan) **не работают** с deal size <€100M-€200M. Минимальная economic deal value для них — слишком мало fees relative to time investment.

Это означает, что огромная часть Mittelstand deals (компании €5M-€50M EBITDA, EV €30M-€350M) обслуживается:
- Mid-tier German banks (Macquarie, Lazard, Rothschild Frankfurt)
- Boutique M&A advisors (Lincoln, IMAP, Concentro, Translink)
- Big 4 corporate finance teams
- WPs (auditors selling advisory)

**И всё ещё это недостаточно.** Многие Mittelstand owners продают через personal network, без professional advisor — оставляя 20-40% value на столе.

Согласно European M&A Monitor (Dealsuite, 828 advisory firms), **37% advisors уже используют AI regular** (vs 7% в 2023) — тренд явный, но это in early stages. Окно для AI-native players ещё открыто.

### 6.3. Три модели позиционирования для Jetix

Вот концептуально, как Jetix может атаковать эту возможность. Не one-size-fits-all — три отдельных модели, которые можно комбинировать:

#### Модель 1: AI-Augmented Boutique M&A Advisor

**Концепция:** Sell-side advisor для Mittelstand €5M-€50M EBITDA. Использует AI как multiplier для всего process.

**Value proposition:**
- 50% lower fees чем traditional boutiques (благодаря AI leverage)
- Faster process (3-4 месяца до signing vs 6-9 traditional)
- Better outcomes (лучше matching через AI screening 1000+ potential buyers)
- Founder-friendly (less paperwork, less stress for owner)

**Revenue:**
- Retainer €15-30k/месяц
- Success fee 2-4% deal value
- Average deal size €50M EV → €1-2M success fee
- Target: 6-10 closings/year → €8-15M revenue

**Что нужно построить:**
- AI pipeline для deal sourcing (continuous monitoring of succession signals)
- Document automation (CIM, IM, financial models templates)
- Buyer database с AI-driven matching
- Partner network (lawyers, Big 4, banks)

#### Модель 2: AI-Augmented Search Fund / ETA

**Концепция:** Не консультировать продажи — **самим acquire** Mittelstand company и operate с AI как core advantage.

**Mechanics (классический search fund):**
- Phase 1: Raise ~$500k search capital (10-15 investors, $25-50k каждый)
- Phase 2: Search 12-24 месяца, screen 300-500 targets
- Phase 3: Acquire one target ($5-30M deal с PE-backed equity)
- Phase 4: Operate as CEO 5-10 years
- Phase 5: Exit via secondary or strategic sale

**Это buy-and-build** возможно. Купил one base company, потом acquire smaller competitors с AI-leveraged operations.

**Returns:** Search fund average ROI ~4x (по INSEAD data). Operator equity stake ~20-30%.

**Для тебя specifically:** AI infrastructure Jetix может стать direct value-add для acquired company — embedded AI tools в operations create immediate margin expansion.

INSEAD ETA Hub, Search Fund Hub Germany, Tilia Nachfolgekapital — есть active community с 70+ studets in Erasmus, conferences, mentorship. ETA в Germany ramping up rapidly.

#### Модель 3: Mittelstand AI Alliance + Implicit Deal Flow

**Концепция:** Это extension того, что у тебя в memory как "Mittelstand AI Alliance" — но с M&A angle.

Если Jetix building network non-competing Mittelstand companies sharing AI infrastructure, ты сидишь на **proprietary deal flow**:
- Знаешь, какой Mittelstand owner cooming retirement (через network conversations)
- Знаешь, какие companies looking buy AI-enabled assets
- Знаешь financial state (через AI implementations)
- Можешь introduce buyers/sellers внутри alliance

Это classic 2-sided platform play. Alliance member companies — and Jetix sit в middle of information flow.

**Monetization:**
- Alliance membership fees (recurring base)
- M&A advisory fees когда members транзагируют
- Eventually marketplace fee для introductions

Это "infrastructure layer + catalyst consultant" роль из твоей strategy, плюс M&A overlay.

### 6.4. Реалистичная оценка — что hard, что easy

**Что сравнительно easy** (с твоими existing capabilities):
- Building AI tooling (12 Claude Code agents infra уже есть)
- Document automation, financial modeling, screening
- CRM and pipeline management
- Initial outreach automation (с GDPR compliance — у тебя уже expertise)
- Web sourcing, OSINT

**Что hard** (требует separate skill build):
- M&A specific knowledge (deal structuring, LBO mechanics, legal structuring) — это надо изучать или партнёр-юрист с этой expertise
- Trust building в Mittelstand circles — это **только время и presence на industry events, Verbände, conferences**
- Negotiation expertise — практика в реальных deals, не tutorials
- Financial Modeling proper accounting (отличие от business analysis) — нужно тренировка или CFA-уровень co-founder

**Что critical missing piece:** senior банковская/M&A expertise. Вариант — найти **co-founder с M&A backgrond** (ex-Lincoln, IMAP, или похожие boutique-firms partner) с большим network.

### 6.5. Что НЕ работает

Несколько традиций которые я хотел бы dispel:

❌ **"Я могу сам делать sophistication-уровня M&A с AI"** — нет. Junior-уровня анализ — да. Но финальный judgment в complex deal требует years of pattern recognition в hundreds of deals. Pure-AI M&A advisor для сложных сделок will fail badly.

❌ **"Mittelstand owners выберут AI-первого consultant"** — наоборот, они conservative, ценят personal touch. AI должен быть invisible advantage, не headline.

❌ **"Можно скейлить через automated lead generation"** — Mittelstand sales cycles 6-18 месяцев, требуют warm intros, multiple touchpoints. Не SaaS funnel.

❌ **"Comp с big banks"** — нет, ты not competing с Goldman. Они не там играют. Compete с similar boutiques, mid-tier.

❌ **"Faster всегда better"** — иногда medication owner needs 6 месяцев emotional preparation для exit. Pushing process — losing deal.

---

## ЧАСТЬ 7. Стратегические рекомендации

### 7.1. Как начать (next 6 months)

**Если идти Модель 1 (M&A advisory):**

1. **Найти co-founder/senior partner** с реальной M&A experience (boutique partner-уровень). Это critical. Без этого all credibility crumbles в первой клиентской встрече.
2. **Pick narrow vertical.** Не "Mittelstand вообще" — а "AI-enabled Mittelstand sellers in DACH industrial automation" or similar. Focus dramatically improves deal flow и credibility.
3. **Build AI advantage stack.** Hebbia/Rogo subscriptions + custom Claude infrastructure для proprietary advantages. Demonstrable AI advantage в pitches.
4. **Initial 5 mandates discount/free** — build case studies. Без track record никто не подпишет real engagement.
5. **Industry presence.** Verband attendance, IHK events, M&A conferences. Year 1 mostly relationship building, not selling.

**Если идти Модель 2 (Search Fund):**

1. **Decide self-funded vs traditional search fund.** Self-funded даёт больше equity (50-100% vs 20-30%) но requires personal capital.
2. **Investor outreach** для traditional model. INSEAD/HSG/Mannheim alumni networks, Search Fund Hub.
3. **Define investment thesis.** Industry, geography, size. AI-enabled services? Industrial automation? Specialty manufacturing?
4. **Search infrastructure** — это где AI shines. Build proprietary screening / outreach engine.
5. **2-year search horizon** — be psychologically prepared.

**Если идти Модель 3 (Alliance + deal flow):**

1. Continue building Mittelstand AI Alliance как primary
2. Start tracking transactional intent inside alliance
3. Add M&A advisory как secondary service для members
4. Eventually evolve в platform

### 7.2. Hybrid recommendation

В реальности, я бы предложил **hybrid Model 1 + Model 3**:

- Build Jetix как AI consultancy → gateway to relationships
- Add M&A advisory как premium service для existing relationships
- Alliance grows из organic network → captive deal flow
- Eventually optionally add ETA acquisitions (Model 2) если accumulate enough capital и right opportunities

**Почему hybrid:**
- Меньше risk чем pure search fund
- Faster cash flow чем pure M&A play
- Compounding network effects
- Ставит тебя в idea position для optionality (any of these models can be optimized later)

### 7.3. Метрики успеха для следующих 12 месяцев

Year 1 milestones:
- [ ] First M&A advisory mandate signed (pilot)
- [ ] 100+ Mittelstand owners в proprietary CRM (warm contact level)
- [ ] AI infrastructure для M&A specifically built and tested
- [ ] 1-2 case studies published
- [ ] Industry presence (3+ conferences, Verband membership)
- [ ] Co-founder/senior partner identified или recruited

Year 2:
- 3-5 closed transactions
- €1-3M revenue from M&A activity
- Established AI-augmented brand в German Mittelstand
- Optional: first ETA target identified

### 7.4. Капитал и risk profile

**Realistic capital requirements:**

Model 1 (M&A advisory): €200-500k bootstrap (covering 12-18 months runway with co-founder)
Model 2 (Search fund traditional): $400-600k search capital from investors
Model 2 (Self-funded search): €100-300k personal capital
Model 3 (Alliance evolution): minimal incremental — мостик from existing Jetix

**Risk-reward для каждой модели:**

| Model | Capital risk | Time horizon | Upside ceiling | Probability of $10M+ outcome |
|-------|-------------|--------------|----------------|------------------------------|
| 1. M&A Boutique | Medium | 3-5 years | $50-100M (firm value) | 25% |
| 2. ETA / Search Fund | Low (OPM) | 5-10 years | $30-100M (operator equity) | 30% |
| 3. Alliance + M&A | Low | 5-7 years | $100-500M (platform) | 15% if it works, but harder |

### 7.5. Конкретный AI tooling stack для M&A

Если будешь идти этой дорогой, вот specific stack:

**Sourcing layer:**
- Custom Claude/ChatGPT агент мониторящий Bundesanzeiger, news, LinkedIn
- Crunchbase / Pitchbook for German market
- Custom Bundesanzeiger scraper (legal с public data)

**Analysis layer:**
- Hebbia или Rogo (если можешь afford enterprise pricing) — лучше всего на сегодня
- Альтернатива: build custom on Anthropic API + RAG для cheaper option
- AlphaSense для market research

**Modeling:**
- Excel + Anthropic API integrations для template generation
- Custom DCF / LBO templates с AI-driven assumption suggestions

**Document generation:**
- Claude/GPT for first drafts CIM, IM, pitch books
- Final human polish обязательно

**CRM / Process:**
- Affinity (M&A specialist CRM) или Salesforce
- Custom pipeline management built on existing Jetix infra

**Communications:**
- Standard tooling but with personalization automation

---

## ЧАСТЬ 8. Mental models на дорогу

### 8.1. Главный takeaway — где происходит ценность

Wall Street, M&A, PE — это всё машины, которые трансформируют **разрыв в информации, доверии, и способности executive complex transactions** в деньги. AI atomizes the **information processing** и **execution mechanics** parts. Что остаётся:
- Trust / relationship capital
- Judgment under uncertainty
- Negotiation / persuasion
- Network access

Эти **аугментируются** AI, но не заменяются. Это означает:

> Будущее принадлежит **human-AI hybrid operators**, у которых есть real judgment, relationships, и network — augmented с unprecedented analytical/execution capacity.

### 8.2. Параллель с твоим existing бизнесом

Та же логика прямо applies к Jetix consulting:
- McKinsey партнёр приносит проект (relationship value)
- Junior consultants делают slides (commodity work, AI-replaceable)
- Senior partner makes judgment calls в client meetings (judgment value)

В новой эпохе: **single sophisticated operator + AI = team of 10 in old model**. Это работает в M&A, в consulting, в PE. Это новая структурная реальность.

### 8.3. Самое контринтуитивное

Большие банки (Goldman, Morgan Stanley) **выживут лучше**, чем mid-tier. Потому что у них tier 1 relationships, которые AI не tronche. Massive PE (Blackstone, Apollo) **выживут лучше**, чем mid-fund PE — потому что они have access к largest LP allocations и mega-deals.

**Самое уязвимое место — это middle.** Mid-tier banks. Mid-tier PE. Junior bankers. Это где AI + AI-native competitors come to eat.

И это где **opportunity for new entrants** наибольший. Не competing с Goldman (you can't). Competing с indecisive boutique boutique that hasn't moved on AI. Они тяжёлые, slow, expensive.

### 8.4. Long view

Если этот тренд continue 10 лет:
- Goldman, Morgan Stanley, JP Morgan — survive в premium tier (top 10% deals)
- Mid-tier banks — decimated
- Consolidation в boutiques — winners take all через AI-leverage
- New form: AI-native boutique с 15-30 partners doing $50M-$2B deals — replacing old 200-person investment banks
- PE and HF — quants и AI-augmented funds win big; traditional fundamental funds compress

В Mittelstand specifically:
- **Massive succession transfer** completes 2026-2032 — most M&A in Germany history
- Buy-and-build strategies dominate
- AI as standard tooling (not differentiator) by 2028
- Window для AI-native players closes ~2027-28

То есть **окно открыто сейчас**. Не вечно.

---

## Sources & References

### Primary data sources used in this report

**On private equity industry:**
- Apollo Global Management Q2 2025 reports — $840B AUM, 21% YoY growth, target $1T by 2026
- KKR & Co Q3 2025 reports — $686B AUM, $43B raised in single quarter
- Blackstone Inc earnings calls — $1T+ AUM, 33% in credit & insurance
- S&P Global Market Intelligence on private credit growth

**On hedge funds:**
- Hedgeweek 2024 quant fund returns
- Renaissance Technologies disclosed returns (Medallion 30%, RIEF 22.7%, RIDA 15.6%)
- Two Sigma flagship Spectrum 10.9%, AR Enhanced 14.3%
- Multiple sources on Citadel, D.E. Shaw, Jane Street

**On German M&A market:**
- IMAP 2026 German M&A outlook (mid-cap segment)
- PwC German M&A Trends in Industrials & Services 2025
- Chambers and Partners Corporate M&A 2025 Germany
- Reed Smith 2025 German Mid-Cap Market analysis
- Datasite Mittelstand M&A spotlight
- Lexology M&A in German Mittelstand (Lexology 2025)

**On Mittelstand succession:**
- KfW Research Nachfolge-Monitoring Mittelstand (560k businesses by 2026)
- DIHK: 215k+ owners intend handover by end 2026
- ifo Institute: 42% of family businesses without internal successor
- Translink Corporate Finance succession analysis

**On AI in investment banking:**
- Rogo $50M Series B announcement (April 2025)
- Hebbia AI platform documentation
- V7 Labs 2026 best AI tools for IB
- Vals AI study on AI accuracy in financial tasks
- European M&A Monitor 2025 (Dealsuite, 828 advisory firms)
- Anthropic Economic Index AI's Impact on Software Development

**On M&A fees:**
- Firmex Global M&A Fee Guide 2024
- First Page Sage M&A Advisory Fee Structure 2025
- MNA Community Fee Guide 2025

**On ETA / Search Funds in Germany/Europe:**
- INSEAD Centre for Entrepreneurship ETA Hub
- Search Fund Hub Germany
- Tilia Nachfolgekapital (Lisa Stuhler)
- Stanford GSB Search Fund Study
- ScienceDirect: European Search Fund characteristics

### Recommended further reading

**Books:**
- "Liar's Poker" — Michael Lewis (Salomon 1985-88)
- "Barbarians at the Gate" — Bryan Burrough, John Helyar (RJR Nabisco LBO)
- "Private Equity at Work" — Eileen Appelbaum, Rosemary Batt
- "King of Capital" — David Carey, John Morris (Blackstone story)
- "More Money Than God" — Sebastian Mallaby (hedge fund history)
- "The Man Who Solved the Market" — Gregory Zuckerman (Jim Simons / RenTech)
- "Buying Your Way into Entrepreneurship" — Richard Ruback, Royce Yudkoff (HBS, ETA)

**Frameworks worth deep-diving:**
- DCF (Discounted Cash Flow) valuation
- LBO modeling
- Comparable Company Analysis ("trading comps")
- Precedent Transaction Analysis ("transaction comps")
- IRR vs MOIC vs DPI vs TVPI metrics (PE returns)
- Lehman Formula vs modern fee structures

---

*Конец отчёта.*

*Если будет интересно углубить какой-то конкретный угол — например, написать отдельный deep-dive по LBO mechanics с реальными numbers, или strategic plan для конкретной модели (M&A boutique vs ETA), или построить proprietary AI sourcing pipeline для Mittelstand — это уже следующий слой работы.*
