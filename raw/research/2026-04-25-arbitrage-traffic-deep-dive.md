---
id: arbitrage-traffic-deep-dive-2026-04-25
title: "Арбитраж трафика — Глубокий research (рынок, вертикали, инструменты, экономика, юридика)"
date: 2026-04-25
type: research-deep-dive
state: raw
tier: tier-1-source-material
author: external-research-agent (provided by Ruslan)
delivered_by: ruslan-handoff
binding: input-only (NOT a decision; informs Phase-2+ future direction integration)
relates_to:
  - decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md (synthesis для Jetix integration)
  - decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md (parallel future direction — M&A)
  - decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md (will receive Direction-11 Arbitrage в future cycle)
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md (Mittelstand B2B affiliate angle)
  - decisions/JETIX-VISION.md (D11 Investment-fund philosophy, D20 USB-C positioning)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (AI-leverage thesis)
key_insights_for_jetix:
  - "Глобальный affiliate-маркетинг $17-18.5B (2025) → $20B+ (2026) → $71B (2034) при CAGR ~15%; 80% брендов используют партнёрский канал"
  - "B2B SaaS affiliate растёт +17% YoY — direct overlap с Mittelstand AI Alliance стратегией"
  - "AI domination обеих сторон: TikTok Symphony / Meta Advantage+ / Google Performance Max + 97% брендов уже используют AI"
  - "Server-side tracking обязателен 2026 (TikTok Events API v2, Meta CAPI) — техническая ниша для compliance-first players"
  - "Compliance-first игроки имеют growing advantage (FTC штрафы $51K/нарушение в US; GDPR + DSA + EU AI Act в EU)"
  - "Технологический стек арбитражника = отдельная B2B-индустрия (anti-detect / трекеры / прокси / spy tools / virtual cards) — потенциальная Jetix infrastructure layer"
  - "Cross-link с Mittelstand AI Alliance: AI-генерация персонализированных лендингов под сегмент B2B + A/B testing + CRM integration = lead-gen-as-a-service compliance-first"
  - "Tier-распределение по доходам: Beginner $0-1K/mo (большинство) / Advanced $10-80K/mo (~15%) / Top earners $100K+/mo (3.7%) / Super top $1M+/mo (<0.1%)"
  - "AI меняет соотношение: креатив дешевеет, конверсия дороже — конкуренция смещается к LTV + post-conversion воронке (CRM, retention)"
  - "Главный актив — tacit knowledge об источниках (какому push-сетке доверять, какой ангел в Tier-2 даёт CR) — стирается за 0.5-1 год при изменении модерации"
tags: [arbitrage-traffic, affiliate-marketing, performance-marketing, cpa-networks, ad-networks, tiktok, meta, adult, mittelstand-affiliate, compliance, research]
---

# Арбитраж трафика: глубокий research

> **Что внутри:** объяснение от азов до устройства рынка. Базовая механика → вертикали → adult и TikTok отдельными разделами → карта компаний → экономика → юридика → тренды 2025–2026.
> **Дата:** апрель 2026
> **Источники:** в конце документа

---

## TL;DR (если читать только это)

1. **Арбитраж трафика — это перепродажа внимания пользователей.** Ты покупаешь клики/показы у одной площадки (Facebook, TikTok, Google, push-сети, тизерки), направляешь людей на оффер другого бизнеса, и зарабатываешь, если выплата от этого бизнеса > твоих расходов на рекламу. Это performance-маркетинг на свой риск.
2. **Это не нишевая серая тема, а индустрия на $18–37 млрд** (в зависимости от того, как считать). Глобальный affiliate-маркетинг оценивается в $17–18,5 млрд в 2025 и должен пробить $20+ млрд в 2026, с прогнозом до $71 млрд к 2034 при CAGR ~15%. Около 80% брендов уже используют партнёрский канал.
3. **Рынок делится на три цвета:** белый (e-commerce, SaaS, образование, легальные финансы), серый (нутра, гемблинг, беттинг, крипта, дейтинг — на грани правил рекламных площадок), чёрный (фейковые товары, мошеннические схемы, обход модерации с фродом).
4. **Главные вертикали:** Nutra, Gambling/Betting (iGaming), Finance, Crypto, Dating, Adult, E-commerce, Sweepstakes, Mobile apps. Высокие выплаты в гэмблинге/крипте/беттинге, низкий порог входа в нутре и e-commerce.
5. **Стек арбитражника = 4 слоя:** источник трафика (Meta/TikTok/Google/push) → антидетект-браузер + прокси → трекер аналитики (Voluum, Binom, RedTrack) → CPA-сеть с офферами (MaxBounty, ClickDealer, Adsterra, AdCombo, CrakRevenue и тд).
6. **Adult-арбитраж — отдельная экосистема** с собственными ad-нетворками (TrafficJunky, ExoClick, TrafficStars, JuicyAds), потому что Google/Meta не пускают эту вертикаль.
7. **TikTok к 2026 — самый горячий источник трафика**, особенно для нутры, e-com, дейтинга, гэмблинга в Tier-2. Его обгон Facebook в ряде вертикалей идёт уже два года.
8. **Юридика жёсткая, но обходится:** FTC штрафует за нераскрытие affiliate-связей до $51 744 за нарушение (в США), в EU действуют GDPR + DSA. Серый и чёрный арбитраж живут на клоакинге — показывают модератору одно, юзеру другое. Это технически работает, экономически — рисково.

---

## Часть 1. Что такое арбитраж в принципе

**Арбитраж в широком смысле** — это извлечение прибыли из разницы цен на один и тот же актив или ресурс на разных рынках. Купил дешевле там, продал дороже здесь — заработал на спреде.

Концепт пришёл из финансов: классический пример — арбитраж криптовалют, когда биткоин стоит на одной бирже $60 000, на другой $60 200, и ты быстро покупаешь там и продаёшь здесь. Похожий принцип работает в:

- **Финансовом арбитраже** — разница курсов валют, акций, крипты на разных площадках.
- **Товарном арбитраже** — закупка на AliExpress / Pinduoduo, продажа на Amazon / Wildberries (это и есть основа дропшиппинга и Amazon Arbitrage).
- **Юридическом арбитраже** — здесь смысл другой: разрешение споров вне суда через арбитра. Не имеет отношения к нашей теме.
- **Арбитраже трафика (рекламы)** — про что мы и говорим дальше.

Общий знаменатель: **ты не создаёшь актив, ты используешь неэффективность рынка**. В арбитраже трафика неэффективность в том, что разные площадки оценивают одного и того же пользователя по-разному.

---

## Часть 2. Арбитраж трафика — базовая механика

### 2.1. Минимальное определение

**Арбитраж трафика** — это бизнес-модель, в которой ты:

1. Покупаешь рекламу на одной площадке (источник трафика) — Facebook, TikTok, Google Ads, Yandex Direct, push-сеть, тизерка, нативка.
2. Гонишь пользователей с этой рекламы на конкретное предложение (оффер) — лендинг бренда, форму регистрации, страницу скачивания приложения, страницу казино.
3. Зарабатываешь, если рекламодатель (или партнёрская сеть, агрегирующая офферы) платит тебе за целевое действие пользователя больше, чем ты потратил на рекламу.

**Прибыль = выплаты за конверсии − расход на трафик − комиссии трекеров/прокси/инструментов − налоги**.

### 2.2. Простой пример

- Ты заливаешь $1000 в Facebook Ads на оффер «препарат от боли в суставах» в Польше.
- Получаешь 2000 кликов по $0,50.
- Из них 80 человек оставили заявку на лендинге (2000 × 4% конверсия в лид).
- Из этих 80 заявок 60 подтвердились по телефону (apply rate 75%).
- За каждый подтверждённый лид CPA-сеть платит тебе $20.
- Доход: 60 × $20 = $1200. Расход: $1000. **Прибыль: $200, ROI: 20%**.

ROI 20% за пару дней — нормальный уровень для серой нутры. Для гэмблинга в Tier-1 ROI может быть 50–200%, но и риск выше: оффер может «протухнуть», аккаунт могут забанить, a лиды реклассифицировать как фрод.

### 2.3. Ключевые роли в экосистеме

| Роль | Что делает | Кто это |
|---|---|---|
| **Рекламодатель** | Производит товар/услугу. Покупает результат (лиды, продажи, регистрации). | Казино, фарма-бренд, банк, сервис знакомств, мобильная игра. |
| **Арбитражник (медиабайер, аффилейт, веб-мастер)** | Покупает трафик за свой счёт, льёт на офферы рекламодателя через CPA-сеть. | Соло-фрилансер с $500 / небольшая команда / арбитражная баинговая команда / международный affiliate-холдинг. |
| **CPA-сеть (партнёрка)** | Агрегатор офферов. Связывает рекламодателей и арбитражников, верифицирует лиды, платит. Берёт свой процент. | MaxBounty, ClickDealer, Adsterra, CrakRevenue, AdCombo, Dr.Cash и сотни других. |
| **Источник трафика (ad network)** | Площадка, где арбитражник покупает рекламу. | Facebook Ads, TikTok Ads, Google Ads, push-сети (PropellerAds, RichAds), нативка (Taboola, Outbrain, MGID), adult-сети (ExoClick, TrafficJunky). |

### 2.4. Базовая терминология

- **Оффер** — конкретное предложение от рекламодателя
- **Гео (GEO)** — страна. Tier-1 (US/UK/DE/FR), Tier-2 (PL/CZ/BR/TR), Tier-3 (IN/ID/Africa)
- **Связка** — креатив + лендинг + оффер + источник + гео
- **Креатив (крео)** — рекламный материал
- **Лендинг (LP)** — посадочная страница
- **Преленд (pre-lander)** — промежуточная страница для разогрева
- **Прокладка / клоака** — техническая страница для маскировки от модераторов
- **Апрув / approval rate** — % подтверждённых лидов
- **EPC** — earnings per click
- **CR** — conversion rate
- **ROI** — return on investment
- **Бан / шадоу-бан** — блокировка / снижение охвата
- **Фарм аккаунтов** — «прогрев» новых рекламных аккаунтов
- **Спай (spy tool)** — сервис для подсматривания рекламы конкурентов

### 2.5. Pricing-модели

| Модель | За что платят | Размер выплаты |
|---|---|---|
| **CPA** | За любое целевое действие | $1–$200+ |
| **CPL** | За оставленный контакт | $1–$50 |
| **SOI** | За регистрацию без подтверждения | $1–$5 |
| **DOI** | За регистрацию + подтверждение | $3–$15 |
| **CPS** | Процент от продажи | 5–70% от чека |
| **CPI** | За установку приложения | $0.50–$8 |
| **CPC** | За клик | $0.05–$3 |
| **CPM** | За 1000 показов | $0.10–$10 |
| **RevShare** | % от выручки рекламодателя пожизненно | 20–60% |
| **CRG** | Гарантированный CR от рекламодателя | Высокий, мало где |
| **Pay Per Call** | За телефонный звонок длиннее N секунд | $30–$200 |
| **Hybrid (CPA + RevShare)** | Фикс + % от дальнейшей активности | Самая выгодная для опытных |

**Правило большого пальца:** новички берут CPA, опытные — RevShare и Hybrid в гэмблинге.

---

## Часть 3. Цвета арбитража: white / grey / black

### Белый (white)
**Что это:** легальные офферы, разрешённые правилами площадок и законами стран.
**Вертикали:** e-commerce, SaaS, образование, HR, недвижимость, страхование, финтех-розница, путешествия, легальная нутра (витамины с одобрением), беттинг с лицензией.
**Источники:** Google Ads, Meta (с осторожностью), TikTok, нативка, SEO, контент-маркетинг.
**Плюсы:** долгоиграет, низкий стресс. **Минусы:** низкие выплаты, конкуренция.

### Серый (grey)
**Что это:** на грани правил рекламных площадок. Сама ниша легальна, но реклама ограничена; креативы используют преувеличения; модерация обходится без явного фрода.
**Вертикали:** нутра (магические таблетки), гемблинг и беттинг (с лицензией), крипта (обучение, сигналы), дейтинг (mainstream), микрозаймы PDL.
**Источники:** Meta + клоакинг, push-сети, нативка, тизерки, in-app, PWA.
**Инструменты:** антидетект-браузеры, фарм-аккаунтов, прокси, клоакеры.
**Плюсы:** $50–$200 за лид. **Минусы:** банят, сжигаются креативы, нужен серьёзный стек.

### Чёрный (black)
**Что это:** прямое нарушение правил и закона. Скам-офферы, фишинг, фейковые БАДы, кликбейт с обманом, malware, фейковые «инвестиции», cookie stuffing, форс-клики, brand-jacking.
**Плюсы:** иногда быстрые большие деньги. **Минусы:** уголовное преследование, бан в индустрии, потеря денег при детекте.

**Анти-фрод сейчас зрелый:** Awin Conversion Protection Initiative (April 2025) — вернула рекламодателям >$250M ошибочных выплат. Rakuten Detect suite + Affiliate Conversion Transparency API в May 2025.

---

## Часть 4. Вертикали — что льют

### Nutra (здоровье и красота) — стартовая вертикаль
- **Подкатегории:** препараты от гипертонии/диабета/суставов/потенции/похудения; БАДы; косметика
- **Аудитория:** ж 25-55 (красота), м 30-55 (потенция), молодёжь 20-35 (фитнес)
- **Гео:** работает везде, позиционирование по тирам различно
- **Выплаты:** $5–$50 за подтверждённый заказ
- **Источники:** push-сети, нативка, тизерки, Meta, TikTok
- **Креативы:** before/after, тестимониалы, «эксперты-врачи», сторителлинг
- **Цвет:** серый (магические); белая — витамины с пройденными регуляторами

### iGaming: Gambling + Betting
- **Аудитория:** мужчины 25-45
- **Гео:** Tier-2/3 (Бразилия, Турция, Индия, Латам, Восточная Европа)
- **Выплаты:** CPA $30–$300 за FTD, RevShare 25–50% пожизненно
- **KPI:** 40%+ игроков с FTD должны сделать ещё 2-3 депозита
- **Источники:** Facebook (через клоакинг), TikTok, in-app, push, ASO, SEO, Telegram
- **Цвет:** серый/чёрный в большинстве гео

### Crypto
- **Подкатегории:** биржи, кошельки, обучение, ICO, DeFi
- **Гео:** Tier-1 (US/CA/AU/EU), Tier-2/3 для обучения и MLM
- **Выплаты:** CPL $50–$200, CPA $200–$1000, RevShare с торговых комиссий
- **Источники:** SEO, YouTube, Telegram, Twitter/X, Reddit, native, Meta
- **Цвет:** серый; чёрный — фейковые инвест-платформы, PIG-butchering скамы

### Dating
- **Mainstream:** Tinder-подобные, серьёзные знакомства, niche (christian/senior/lgbtq)
- **Adult Dating:** в адалт-вертикали
- **Выплаты:** SOI $1–$5, DOI $3–$15, CPS до $50
- **Источники:** Meta, TikTok, push-сети, нативка
- **Цвет:** mainstream — белый, adult — серый/чёрный

### Finance
- **Подкатегории:** микрозаймы PDL, кредитные карты, депозиты, страхование, ипотека, инвестиции, форекс, брокерские счета
- **Аудитория:** 25-55 средний доход (PDL), 30-60 (инвестиции)
- **Выплаты:** $5–$200 за заявку (PDL), $20–$200 за выданный кредит, $30–$200 PPCall
- **Источники:** Google Search (intent!), Meta, TikTok, нативка, SEO
- **Цвет:** белый (банки) и серый (микрозаймы, бинарные опционы)

### E-commerce
- **Подкатегории:** дропшиппинг, реселлинг, COD-офферы, single-product brands
- **Гео:** везде, особенно Tier-2/3 для COD
- **Выплаты:** % от чека или фикс $10–$50
- **Источники:** TikTok #1 (TikTok Shop $64.3B GMV в 2025, +113% YoY), Meta, нативка
- **Цвет:** в основном белый

### Sweepstakes (розыгрыши)
- «выиграй iPhone», «получи Gift card», викторины
- Гео: США, UK, Канада, Австралия, Япония, Зап. Европа
- Выплаты: SOI $1–$10
- Источники: push, popunder, social
- Цвет: серый

### Mobile apps / gaming
- Install кампании для игр, утилит, fintech-приложений
- Выплаты: CPI $0.50–$8
- Источники: in-app сети (Moloco, AppLovin, Unity Ads), TikTok, Meta
- Цвет: в основном белый

---

## Часть 5. Adult-арбитраж

Adult — отдельная индустриальная экосистема внутри арбитража.

### Что льют в adult
- Adult Dating (AdultFriendFinder)
- Webcams (Chaturbate, BongaCams, LiveJasmin)
- VOD / Premium Tube
- Adult Games
- Sex toys (e-commerce)
- Adult VPN
- Adult Nutra (потенция, либидо)

### Главные ad-нетворки 2025-2026

**1. ExoClick** — >12B показов/день на 65,000+ паблишер-сайтах в 200+ странах. Форматы: попандер, нативка, баннеры, push, видео, interstitial. AI-оптимизатор Bidder 2.0.

**2. TrafficJunky** — эксклюзив сети Aylo (Pornhub, YouPorn, RedTube, Tube8) — ~4B показов/день. Премиум-инвентарь, низкий фрод. CPM $0.10–$0.20, до $2–$4 для Tier-1.

**3. TrafficStars** — 5000+ ad-слотов, RON и PRIME-трафик. Lookalike-аудитории и retargeting (редкость в adult). AI Smart Bidder.

**4. JuicyAds** — низкий порог входа ($100), ~2B показов/день. Удобен для тестирования офферов.

**5. PlugRush** — попандер + нативка для adult и mainstream, ~1B показов/день.

### CPA-сети для adult
**CrakRevenue** (14 лет, лидер), **Adsempire** (smartlink), **MyBid** (multi-vertical), **Cpamatica** (1000+ adult-офферов), **Traffcore** (smartlink).

### Реальная экономика
- TrafficJunky CPM $2 на дейтинг-кам → реальная стоимость engaged-трафика ~$9 CPM (после фильтрации) = $0.09 за «настоящего» юзера в Tier-1 US/CA/Western Europe
- Push-трафик: $0.11 CPC, реальный «cost per head» ~$0.45
- Бизнес держится на оптимизации воронки: креатив → преленд → лендинг → активация

### Тренды adult-2026
- AI-оптимизация заменяет ручной байинг (ExoClick Bidder 2.0, TrafficStars Smart Bidder)
- Этичный сдвиг: Gen Z требует inclusive content (ManyVids/JustForFans/LoyalFans)
- Сжатие маржи в Tier-1
- Регулирование возраста и контента (UK Online Safety Act 2023, ЕС age-gates)

---

## Часть 6. TikTok-арбитраж

### Почему TikTok работает уникально хорошо

1. **1.9B MAU** в Q4 2025 (ByteDance)
2. Алгоритм продвигает новые аккаунты так же активно как старые — низкий барьер
3. Среднее время в приложении ~95 минут/день — больше любой соцсети
4. Engagement rate 2.5% (5× Instagram). Аккаунты до 100K фолловеров — 7.5%
5. Аудитория 36-38% юзеров 18-24, 32% 25-34
6. **TikTok Shop $64.3B GMV в 2025 (+113% YoY)**
7. CPC заметно ниже Facebook/Google

### Две модели

**Paid:** TikTok Ads Manager (In-Feed, TopView, Spark Ads, Lead Gen, Smart+). Бюджет $20-50/день на ad group для теста. Стек: антидетект + мобильные прокси + свежие карты + TikTok Pixel + Events API v2 (с 2026 обязателен). ROI 25-55%.

**Organic (шиллинг):** сеть контент-аккаунтов, короткие видео, ссылки в био. Дешевле, но требует контентной фабрики.

### Хорошо работающие вертикали на TikTok
- **Tier-1:** e-commerce, нутра, mobile apps, гэмблинг (с прелендами)
- **Tier-2:** финансы/крипта (через образовательный угол), дейтинг (SOI), sweepstakes

### Search arbitrage с TikTok
Дешёвый TikTok-трафик → страница-агрегатор поисковой выдачи (System1, AdSense for Search, Tonic). Юзер кликает по высокооплачиваемому поисковому объявлению, ты получаешь долю.

Кейс: CPC $0.50 → $0.30 (-40%), CTR +20%, ROI 25% → 55%, доход +45%.

### Опасности TikTok 2026
- Регуляторная неопределённость в США
- Усиление модерации (pass-rate в нутре/гэмблинге упал)
- Конкуренция (auction CPM растёт)
- Symphony AI (-40-60% производство креативов)

---

## Часть 7. Размер рынка

| Год | Affiliate marketing, $B | Источник |
|---|---|---|
| 2023 | 27.8 | Statista |
| 2024 | 32.3 | Marketing LTB |
| 2025 | 17–18.5 (узкое) / 37.3 (широкое) | Cognitive Market Research |
| 2026 | >20 (узкое) | Post Affiliate Pro |
| 2031 | 55 | Post Affiliate Pro |
| 2034 | 71.7 | CAGR 15.2% |

### Региональное разделение
- North America ~40%
- Europe 27-30%
- APAC 23-33% (быстрее всех, +10%/год)
- Latam ~6.4%
- Middle East ~5.2%
- Africa ~4.6%

### По вертикалям
- Retail / e-commerce ~44%
- Telecom / media ~25%
- Travel / leisure ~16%
- Fashion 23% всех affiliate-программ

### Подвижки 2025
- Креатор-driven affiliate $1.1B+/год
- B2B / SaaS affiliate +17% YoY
- Cross-border affiliate 25% всех транзакций
- 97% брендов и 96% креаторов уже используют AI

### Кому интересно
- 80-84% брендов используют affiliate
- 74% брендов получают 11-30% revenue через affiliate
- 65% retailers — affiliate приносит до 20% годового дохода
- 40% маркетологов увеличивают бюджеты на affiliate в 2025

---

## Часть 8. Карта игроков

### A. Tech platforms (бэкенд для брендов)
- **impact.com** — лидер enterprise
- **Awin AG** — глобальная сеть + платформа (Conversion Protection $250M+)
- **Rakuten Advertising** — сеть + DSP (Detect suite + API 2025)
- **CJ Affiliate** — одна из старейших, премиум-бренды
- **PartnerStack** — SaaS/B2B-фокус, 600+ B2B SaaS-брендов
- **Refersion / Impact / Post Affiliate Pro** — SaaS для брендов
- **Tipalti** — платежи аффилейтам глобально
- **TUNE / Everflow / HasOffers** — tracking software для CPA-сетей

### B. CPA-сети (агрегаторы)
- **MaxBounty** — #1 в mThink BlueBook 2025. Финансы/нутра/e-com/дейтинг/sweepstakes. 30K+ аффилейтов
- **ClickDealer** — 40+ вертикалей, SmartLink
- **Perform[cb]** — pay-per-call, медиабайинг
- **CrakRevenue** — adult/cam/dating/CBD (14 лет)
- **AdCombo** — нутра/e-commerce, 700+ офферов, 60+ гео
- **Adsterra** — универсальная (ad-network + CPA)
- **Dr.Cash** — нутра
- **TerraLeads** — нутра, COD
- **CPA.House** — gambling/betting, 200+ офферов
- **Adsempire** — дейтинг (smartlink)
- **MyBid Partners** — gambling/crypto/нутра/adult
- **OneCrypt** — крипта
- **Algo-Affiliates** — casino/crypto/нутра/ecommerce/insurance, 20K+ офферов
- **Magic Click Partners** — gambling/betting (прямые)
- **Advidi** — дейтинг/здоровье (премиум)

**Каталог-агрегатор:** Affpaying.com — 1000+ сетей с рейтингами.

### C. Adult-нетворки
ExoClick, TrafficJunky, TrafficStars, JuicyAds, PlugRush (см. Часть 5).

### D. Источники трафика (paid)
- **Mainstream:** Meta, TikTok Ads, Google Ads, Microsoft Ads, Yandex Direct, Twitter/X, Snap
- **Push-сети:** PropellerAds, RichAds, Adsterra, EvaDav, MegaPush, RollerAds
- **Native:** Taboola, Outbrain, MGID, Revcontent, Yahoo
- **In-app:** Moloco, AppLovin, Unity Ads, Liftoff, ironSource, Mintegral
- **Pop/Popunder:** PopAds, PopCash, Adsterra Popunder
- **Search arbitrage:** System1, Tonic, AdSense for Search

### E. Технологический стек арбитражника

**Трекеры:** Voluum (лидер cloud), Binom (self-hosted СНГ), RedTrack, BeMob (бюджет), Keitaro (Восточная Европа), PeerClick / FunnelFlux / TheOptimizer.

**Антидетект-браузеры:** Multilogin (стандарт enterprise), GoLogin (best all-around), AdsPower (RPA-автоматизация, e-com), Dolphin Anty (УК баеров), Kameleo (мобильная эмуляция), Octo Browser, MoreLogin, DICloak, MuLogin, Lalicat, ixBrowser, VMLogin.

**Прокси:** Bright Data (Luminati), Oxylabs, Smartproxy, IPRoyal, PIA, Soax, LTESocks, ProxyEmpire.

**Spy tools:** AdHeart (Meta 1.2B+ креативов), AdSpy (Meta, обход клоакеров), AdPlexity (Mobile/Native/E-commerce/Social), Anstrex (push+native), BigSpy, PowerAdSpy, SocialPeta, Pipiads (TikTok), TrendTrack, MagicAds.

**Cloaking:** Cloak IT, Adversy, Just Cloak It, KeitaroTDS, Adsbypass.

**Лендинг-конструкторы:** Unbounce/Leadpages/Instapage (белые), LanderLab/PureLander/AdsbyDragon (для арбитражников).

**AI-инструменты:** Symphony (TikTok native), CapCut, Midjourney, Ideogram, Runway, ElevenLabs, Canva, Figma.

**Финансовая инфраструктура:**
- Виртуальные карты: PST, FlexCard, EasyPay, FaceCard, PSTNet
- Платежи: Capitalist, Wise, Payoneer, Wire, Crypto USDT TRC20
- Регистрационные: SMS-Activate, sms-man

### F. Медиа и комьюнити
- **EN форумы:** AffiliateFix, AffLIFT, STM Forum, BlackHatWorld
- **Каталоги:** Affpaying, mThink BlueBook
- **Образование:** Authority Hacker, Diggity Marketing
- **RU:** Partnerkin, Conversion.im, Zorbas, Telegram-каналы
- **Конференции:** Affiliate World (Bangkok/Barcelona/Dubai), STM, MAC (Moscow), TES (Прага), iGB Affiliate (Berlin/London), Adsum

---

## Часть 9. Экономика

### Уровни доходов
| Уровень | Месячный доход | % арбитражников |
|---|---|---|
| Beginner | $0–$1K | большинство |
| Intermediate | $1K–$10K | значительная доля |
| Advanced | $10K–$80K | ~15% (AffStat) |
| Top earners | $100K+ | 3.7% |
| Super top | $1M+ | <0.1% (крупные команды) |

Опытные с >3 года стажа зарабатывают в **9.5 раз больше новичков**.

### Стартовые бюджеты по вертикалям
- E-commerce / mainstream: $300–$500
- Нутра, push/тизерки: $500–$1500
- Дейтинг (mainstream): $500–$2000
- Гэмблинг Tier-2/3: $2000–$5000
- Гэмблинг Tier-1: $10,000+
- Adult dating / cams: $1000–$3000
- Финансы Google Ads: $1000–$3000

### KPI и бенчмарки
- Средний CR: 0.5–1%
- RPM на affiliate-сайте: ~$150 (Authority Hacker)
- Топ-вертикаль по средней зарплате: обучение/онлайн-курсы $15,551/мес, gaming/eSports $12,475/мес, здоровье $8,038/мес
- Cyber Monday 2024: товары через affiliate-ссылки = в 6 раз больше покупок

### Юнит-экономика команды
3 человека:
- $500/день общий бюджет → $15,000/мес расход
- ROI 30% → выручка $19,500/мес
- Чистая прибыль до зарплат: $4,500
- Зарплаты тимлида/2 баеров: $6,000–$10,000

Реальные деньги начинаются с бюджетов от $5K/день.

---

## Часть 10. Юридические риски

### США (FTC)
- **Endorsement Guides** обязывают раскрывать affiliate-связь
- Июнь 2025: FTC расширило определение «paid endorsement» на ВСЕ упоминания бренда (теги, промокоды, brand mentions)
- Штраф: **до $51,744 за каждое нарушение**
- Кейсы: Кардашьян $1.26M за нераскрытое крипто-промо. В 2025 крупный бренд урегулировал на $4.2M

### EU
- **GDPR** Article 6 — affiliate-tracking без согласия = риск
- **DSA** — обязательства по прозрачности рекламы
- **EU AI Act** — регулирует AI-генерацию креативов (mandatory отметка)
- **Германия (UWG)** — особенно строго к cold email

### Cloaking — основная серая зона
В США может квалифицироваться как **wire fraud** (federal crime). Глобальные потери от ad fraud в 2025 — **$84B/год**.

### Другие риски
- **Cookie stuffing** — Shawn Hogan кейс (eBay 2010) $25M
- **Brand bidding** — биддинг по торговой марке рекламодателя
- **Forced clicks / injection**
- **Trademark infringement**

### Российский контекст
После 2022 Meta — экстремистская организация в РФ. VK/Yandex Direct — основной легальный mainstream.

---

## Часть 11. Тренды 2025-2026

### Что меняется быстро
1. **AI-доминирование платформ:** TikTok Symphony, Meta Advantage+, Google Performance Max автоматизируют байинг
2. **AI у аффилейтов:** 97% брендов и 96% креаторов используют AI
3. **TikTok > Facebook** для импульсных вертикалей
4. **Server-side tracking обязателен:** TikTok Events API v2 с 2026 не option, а must. Meta CAPI аналогично
5. **Anti-detect стал mainstream** — стандарт даже у белых медиа-команд
6. **Креатор-affiliate сливается** — 59% брендов планируют отдать 25%+ affiliate-бюджетов креаторам
7. **Cross-device attribution** — главная техническая боль (59% брендов жалуются)
8. **Скам эволюционирует:** AI-генерация фейковых отзывов, бот-саппорт. +35% YoY потери (CPA.ru)

### Что замедляется
- Чистый Facebook-арбитраж на серых вертикалях (банят, фарм дороже)
- Coupon-affiliate (-24% YoY июль 2024 в US)
- Простой SEO-аффилейт (AI Overviews съедают traffic)

### Что появляется
- **Telehealth-аффилейт** (CEO ClickDealer прогноз: 2025 = «год telehealth»)
- **B2B SaaS affiliate** растёт быстрее всего (+17%)
- **Second-hand market** (Vinted, ThredUp, eBay) — $350B к 2027
- **AI-туллинг как вертикаль:** ChatGPT alternatives, AI-image, AI-video — отдельные категории с RevShare 30-50%

---

## Часть 12. Что это значит стратегически (КЛЮЧЕВОЕ для Jetix)

1. **Это zero-sum game в моменте, но positive-sum в среднем.** Рекламодателям выгодно платить только за результат, медиабайерам выгоден доступ к экспертизе и масштабу, юзер получает product он хотел. Проблемы возникают, когда любая сторона пытается оптимизироваться за счёт другой.

2. **Главный актив арбитражника — не креативы и не связки, а tacit knowledge об источниках.** Какой push-сетке доверять, какой аккаунт-фарм работает, какой ангел в Tier-2 даёт стабильный CR — это знание не масштабируется в SaaS, его нельзя купить, оно стирается за полгода-год при изменении модерации. Поэтому индустрия так фрагментирована.

3. **Технологический стек вокруг арбитража — это отдельная B2B-индустрия на сотни миллионов долларов.** Anti-detect, трекеры, прокси, спай-тулы, виртуальные карты. Есть свои unicorn-кандидаты (impact.com уже там).

4. **AI меняет соотношение: креатив дешевеет, конверсия становится дороже.** Раньше уникальное видео = конкурентное преимущество. Теперь все могут сгенерить 100 вариантов за час. Конкуренция смещается к качеству таргетинга, lifetime value юзера, и пост-конверсионной воронке (CRM, retention, win-back).

5. **Регуляторное давление = возможность для compliance-first игроков.** Бренды боятся FTC и DSA → платят больше за «чистых» партнёров. Indust фрагментируется: ультра-серые + полностью-белые, без середины.

6. **Связь с Jetix контекстом (Mittelstand AI Alliance):** арбитраж — performance-marketing вид B2C, а Mittelstand-клиенты в основном B2B. Но **B2B affiliate растёт +17% YoY**, и лидген для немецкого B2B через performance-каналы (legitimate-interest cold email + affiliate landing pages) — это ровно та зона, где AI-агенты могут сильно помочь: написание персональных лендингов под каждый сегмент Mittelstand, A/B тестирование с DeepEval/G-Eval как KPI, интеграция с CRM. Здесь стек Jetix (Hetzner + Ollama + LiteLLM + Claude Code agents) реально может стать инфраструктурой для **compliance-first lead-gen-as-a-service**.

---

## Часть 13. Глоссарий

- **Affiliate / Webmaster** — арбитражник
- **Advertiser** — рекламодатель
- **CPA-сеть** — посредник
- **Offer** — конкретное предложение
- **Lander / LP** — посадочная страница
- **Pre-lander** — промежуточная страница
- **Bundle / Связка** — креатив + лендинг + источник + гео + оффер
- **CR / CTR** — % конверсии / кликабельности
- **CPA / CPL / CPS / CPI / CPC / CPM / RevShare** — модели оплаты
- **GEO / Tier-1/2/3** — страна / категория стран
- **Cap / Капа** — лимит на конверсии
- **Hold / Холд** — период удержания денег
- **Apply / Apruv** — % одобренных лидов
- **EPC** — earnings per click
- **Cloaking / Клоакинг** — разный контент модератору и юзеру
- **Farm / Фарм** — прогрев аккаунтов
- **ROI** — return on investment
- **Smartlink** — динамическая ссылка от партнёрки
- **Burnout креатива** — момент когда CTR падает ниже рентабельности

---

## Источники (~80 источников)

**Базовые объяснения:** Wikipedia, Habr, T-Bank, LP-Generator, IT-Atlas, Web-Promo, AdverMedia.

**Вертикали:** Dolphin-Anty Blog, MoreLogin Blog, AdHeart Blog, MyBid Blog, Magic-Click Medium.

**Размер рынка:** Post Affiliate Pro, Marketing LTB, Cognitive Market Research, Grand View Research, Entrepreneurs HQ, FirstPromoter, DemandSage, impact.com State of Affiliate Marketing 2025, Udonis, Affiliate Statistics Marketing.

**TikTok arbitrage:** Incogniton, MegaDigital, SearchAdx (System1), LTESocks, Undetectable, AdsPower, MediaGCG, Aivix, NPPRTeam, Dataslayer.

**Adult arbitrage:** Noumenal Marketing, CrakRevenue Blog, AffTank, TrafficPartner, Voluum Blog, AffiliateFix, BlackHatWorld.

**CPA-сети:** ROIAds, FractalMax, Geekflare, mThink BlueBook, Strackr, Authority Hacker, HilltopAds, Adsterra Blog, Affpaying.

**Tools:** MoreLogin Services, DICloak Blog, Shoplazza, ScrapingBee, Dolphin-Anty, LanderLab.

**Юридика:** 15m.com, Federal-Lawyer, Influencer Marketing Hub, MeetMarkko, BluePear, AutomateEd, UserCentrics, JoinBrands, FTC.gov.

---

*Документ собран на основе ~80 источников из академических обзоров, индустриальных отчётов (impact.com, mThink BlueBook, Cognitive Market Research, Grand View Research), профильных блогов CPA-сетей и tooling-вендоров, форумов AffiliateFix/BlackHatWorld. Цифры по рынку могут отличаться у разных аналитиков на 30-50% из-за методологии — приведены диапазоны.*
