---
title: "§3 — 11 Archetypes Deep-Dive (L6 Community Document)"
type: integrated-synthesis
produced_by: mgmt-expert
mode: integrator
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-03
section_target: "§3 of decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md"
created: 2026-04-24
pipeline: drafted
state: drafted
confidence: high
confidence_method: structured-rubric + multi-source-trace
provenance_inline: true
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§7.1 + §7.2 + §8"}
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.1 ICP expanded spectrum"}
  - {path: "swarm/wiki/operations/quick-money/icp.md", range: "§ Archetype A + B + 5 ICP Criteria"}
  - {path: "prompts/swarm-launch-brigadier-l6-community-deep-dive-2026-04-24.md", range: "§3"}
word_count_estimate: ~4200
anti_scope:
  - NO §2 ICP Trinity content (sibling cell)
  - NO §4 5-criteria filter deep-dive (sibling cell)
  - NO §7 outreach message templates (sibling cell; only one-line message pattern here)
  - NO Notion writes
  - NO provider-key env-var literal references
  - NO Task() invocation strings
---

# §3 — 11 Архетипов: Глубокое погружение

> **Контекст.** JETIX-VISION §7.1 [src:decisions/JETIX-VISION.md §7.1] содержит каноническое
> перечисление 11 архетипов аудитории Jetix: Предприниматели/бизнесмены, Ресёрчеры,
> Инженеры, Инвесторы, Политики, Продавцы, Менеджеры/коммуникаторы, Философы,
> Разработчики идей, Разработчики жизни, Блогеры (Stage 3 addition 2026-04-21).
>
> Данный документ работает с версией списка, зафиксированной в лонч-промпте §3
> [src:prompts/swarm-launch-brigadier-l6-community-deep-dive-2026-04-24.md §3] — она
> содержит переименования и 5 дополнений Layer-6 (архетипы #7–#11 в новом списке).
> Эта новая нумерация является **канонической для документа LAYER-6-COMMUNITY-DEEP-DIVE.md**.
> Трассируемость к locked Decision 7 (D7, §7.1 JETIX-VISION) сохранена в каждом
> разделе через явный флаг соответствия.
>
> **ICP expanded spectrum** (binding per intake §6.1 2026-04-24):
> payment-ability-as-filter ≥$5K/month recurring или ≥$10K one-shot;
> income-spectrum — millionaires ($1M+/year), high-earners ($100K-150K+/year),
> предприниматели + блогеры. Доход — не жёсткий пол, а подтверждение
> платёжеспособности [src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md §6.1].

---

## 3.1 Startupper / Entrepreneur с нахрапом

**Соответствие JETIX-VISION §7.1:** архетип 1 «Предприниматели/бизнесмены» +
подтип «Startupper» из архетипа 11 «Блогеры» Stage 3 addition.
[src:decisions/JETIX-VISION.md §7.1 + §8 «Для Предпринимателя»]

### Кто

Владелец или со-фаундер цифрового бизнеса либо агрессивно растущего офлайн-дела.
Возраст: 24–42 года. Geography: English-speaking рынки (US / UK / международный),
реже — немецкоязычный DACH-регион как Phase-1 Archetype A overlap.
Типичная выручка: $50K–$500K в год (или растёт к этому уровню за счёт нескольких
активных проектов). Самостоятельно закрывает сделки, нанимает первых фрилансеров,
тестирует оффер на собственном кармане. Нет корпоративной защитной сетки — каждый
квартал либо растёт, либо режет расходы.

Типичный контекст: ведёт либо small consulting/coaching practice, либо infobiz-продукт
(курсы, мастермайнды, ретейнеры), либо ранний SaaS. Возможно имеет небольшую аудиторию
(LinkedIn, YouTube, X/Twitter), которую монетизирует непоследовательно. AI уже пробовал —
ChatGPT, Notion AI, Midjourney — но «система» не складывается: каждый проект начинается
с нуля, контекст теряется, масштабирование буксует.

### Мотивация

**Что говорит:** «Мне нужна система — не очередной инструмент.»
**Что на самом деле нужно:** compound-leverage: каждый следующий проект умнее предыдущего
за счёт накопленной базы знаний, шаблонов, агентов. Этот человек — не ленивый искатель
shortcuts; он работает много, но хочет, чтобы усилие не обнулялось при переходе
к следующему клиенту или продукту. Он принимает риск как ставку на компетенцию (D22
«предпринимательский азарт»), а не как азарт казино.

Вторичная мотивация: принадлежность к среде «своих» — людей с таким же уровнем drive
и адекватности, где нет corporate-bullshit и нет toxic-hustle. Jetix framing «самая
большая авантюра века» [src:decisions/JETIX-VISION.md §7] попадает в его
self-identification точно.

### Что ищет от Jetix

1. **Систему** — wiki + agent pipeline + шаблоны, которые работают вместе, а не
   набор разрозненных инструментов.
2. **Быстрый ROI** — первый результат виден в течение 2–4 недель, не кварталов.
3. **Matchmaking** — в Phase 2+ он хочет получать сложные задачи, которые вырастают
   за его текущие возможности, а Jetix находит правильных specialists.
4. **Среду** — peer group с таким же skin-in-game уровнем, без мотивационного
   circle и без LinkedIn-мусора.

### Что даёт Jetix

- **Phase 1:** 4-pack offer (сессия / 10 шаблонов / community / конкретная помощь)
  [src:decisions/JETIX-VISION.md §9]. Продюсерский центр D11 — если Startupper
  одновременно ведёт канал/аудиторию.
- **Phase 2+:** matchmaker mechanic (D21): Jetix матчит сложные задачи с
  specialists, AI-агенты смазывают coordination.
- **Phase 3+:** roy-leader path — стать координатором роя из 10 людей,
  зарабатывающих $10M–$100M, внутри Jetix methodology.
- **Community:** quality-gated Secure Network — пространство глубокой
  кооперации, не LinkedIn transactional noise.

**F-tag:** F4 — операциональная конвенция, подтверждена 4-pack структурой
Phase 1 и Продюсерским центром D11. Scope: holds for Phase-1 solo-founder Startupper;
unknown for Phase-2 если Startupper стал hired employee (теряет D22 предпринимательский азарт).
**R:** refuted если первый 4-pack клиент из этого архетипа не даёт renewal после пилота
(acceptance = 1+ renewal за 90 дней).

### Канал

LinkedIn (primary), Referral от existing clients, YouTube/podcast (secondary).

### Message pattern

*«Твой AI-стек есть — системы нет. Jetix строит систему, которая помнит всё
и работает за тебя между проектами.»*

---

## 3.2 Блогер / Content Creator

**Соответствие JETIX-VISION §7.1:** архетип 11 «Блогеры» (Stage 3 addition 2026-04-21).
[src:decisions/JETIX-VISION.md §7.1 + §8 «Блогеры specifically»]

### Кто

Специалист в конкретной теме — бизнес, технологии, финансы, медицина, право,
нутрициология — с выстроенной аудиторией, которой он/она доверяет как эксперту.
Не lifestyle-blogger и не tiktoker-развлекалка. Критерии из JETIX-VISION §7.1:
5K+ подписчиков + реальная глубокая экспертиза + возможно курсы / paid products /
обучающие материалы. [src:decisions/JETIX-VISION.md §7.1 archetype 11]

Возраст: 26–45 лет. Geography: English-speaking market primary (US / UK / Australia /
international); Phase-2+ — DACH немецкоязычный Fachblogger. Типичная выручка:
$80K–$600K в год (микс: рекламные интеграции + курсы + consulting retainer + speaking).
Структурная проблема: производство контента отнимает 60–80% рабочего времени, при этом
глубокая экспертиза монетизируется недостаточно — большинство времени уходит на
операционную рутину (editing, repurposing, scheduling), а не на мышление.

### Мотивация

**Что говорит:** «Мне нужна помощь с производством — я не успеваю делать контент
на нужном объёме.»
**Что на самом деле нужно:** освободить время для глубокого мышления и создания
flagship-материала, передав production pipeline AI-усиленной системе. Вторичная нужда —
monetization upgrade: превратить накопленную экспертизу в продуктизированные форматы
(курсы, мастермайнды, paid communities), которые масштабируются независимо от
количества часов.

Этот архетип одновременно является **клиентом** (платит за Продюсерский центр)
и **потенциальным партнёром** (его аудитория — рекрутинговый канал для
Jetix community). Layered identity D8 в действии.

### Что ищет от Jetix

1. **AI-enhanced production pipeline** — research → script → recording → edit →
   repurpose. Один воркшоп или интервью → 10+ derivative artifacts.
2. **Productization pathway** — превратить экспертизу в scaled revenue
   (шаблоны, курсы, retainer programs).
3. **Distribution clarity** — понять, какие каналы работают, на основе данных,
   а не интуиции.
4. **Community-as-trust-amplifier** — Jetix Secure Network как venue для
   engagement с наиболее вовлечённой частью аудитории.

### Что даёт Jetix

- **Phase 1:** Продюсерский центр D11 [src:decisions/JETIX-VISION.md §5 «Продюсерский центр»]
  — monthly retainer, AI-усиленный pipeline. НЕ почасовой рейт.
- **4-pack overlap:** шаблоны как lead-magnet, сессия как стратегическая точка входа.
- **Phase 2+:** Thematic sub-network — блогеры общаются между собой, sharing best
  practices по production, monetization, community. Tool-sharing складчина (Perplexity-max,
  Claude Code, expensive research tools) снижает operational cost.
- **Phase 3+:** roy-replication — Блогер с достаточным масштабом становится
  roy-leader своей ниши внутри Jetix methodology.

**F-tag:** F5 — D11 Продюсерский центр locked decision, KPI-trackable через monthly
retainer count. Scope: holds для English-speaking infobiz Phase 1; NOT valid для
Tier-2 lifestyle-bloggers без экспертизы.
**R:** refuted если первые 3 Продюсерский центр клиента не продлевают ретейнер через
90 дней (acceptance = ≥2 renewals из первых 3 клиентов).

### Канал

LinkedIn (B2B outreach к creator/educator сегменту), Referral (тёплые знакомства
через consuliting network), Podcast guesting (Блогер доверяет тому, кого слышал
в подкасте).

### Message pattern

*«Ты производишь меньше контента, чем мог бы — не из-за лени, а потому что
pipeline не выстроен. Jetix берёт production, ты остаёшься в thinking.»*

---

## 3.3 Исследователь / Researcher

**Соответствие JETIX-VISION §7.1:** архетип 2 «Ресёрчеры» (Stage 2B addition).
[src:decisions/JETIX-VISION.md §7.1 + §8 «Для Ресёрчера»]

### Кто

Человек, профессиональной деятельностью которого является глубокий анализ и синтез:
independent researcher, academic с прикладным фокусом, think-tank analyst, strategy
researcher в компании, data scientist с исследовательским уклоном. Возраст: 28–50 лет.
Geography: глобальный (US / EU / UK / Asia); Phase-2+ open-source research direction
привлекает международную аудиторию. Типичная выручка: $60K–$200K (academic / think-tank)
или $100K–$350K (corporate strategy research / independent consultant). Ключевая
характеристика: depth-of-analysis как профессиональная идентичность. Этот человек
не торопится, зато производит выводы, которые другие не могут.

Сложность Phase-1 квалификации: большинство Ресёрчеров НЕ являются Phase-1 buyer
[src:swarm/wiki/operations/quick-money/icp.md §Phase-1 Filtered Archetypes] — они
Phase-2+ через open-source research direction D24. Исключение: Ресёрчер, который
одновременно является independent consultant с клиентской базой — тогда он
проходит через Startupper-архетип по payment ability.

### Мотивация

**Что говорит:** «Мне нужны лучшие инструменты для анализа и синтеза.»
**Что на самом деле нужно:** multiplier на глубину и скорость — AI-усиленный
research workflow, который не заменяет мышление, а убирает операционные
bottlenecks (поиск, компиляция, форматирование). Плюс: платформа для распространения
выводов среди adequate audience — не academic echo-chamber и не LinkedIn-популяризаторы,
а practitioners, testing ideas on own operations.

Вторичная мотивация: contribute в значимое поле. «Как люди коммуницируют, как должны
компании вместе работать, как вообще должна будущая экономика работать» [src:decisions/JETIX-VISION.md §8 «Для Ресёрчера»] — это поле, в которое Исследователь
хочет вкладываться.

### Что ищет от Jetix

1. **AI-augmented research workflow** — structured synthesis pipeline, wiki-as-KB,
   агенты для компиляции и анализа.
2. **First-mover research data** — доступ к первичным данным о кооперации, AI-adoption,
   methodology effectiveness, которые Jetix собирает первым (D24).
3. **Adequate peer group** — co-researchers-practitioners в Secure Network, не academic
   publishers.
4. **Publication channel** — open-source research direction D24 как venue для
   признанных выводов.

### Что даёт Jetix

- **Phase 2+:** Open-source research direction D24 [src:decisions/JETIX-VISION.md §5 «Long-term»]
  — Jetix использует research first, публикует openly; Исследователь contributes
  в общее поле + получает first-mover dataset access.
- **Thematic sub-network для Ресёрчеров** — quality-gated пространство с
  practitioners-as-peers.
- **Wiki methodology** — structured KB архитектура (Karpathy++ подход), применимая
  к любой research domain.
- **Phase 3+:** institutional research direction (papers, conferences, standards).

**Примечание по Phase-1:** Ресёрчер в роли Phase-1 buyer — conditional. Только если
он является independent consultant с клиентами И проходит D22 5-criteria filter
(особенно «stable» и «предпринимательский азарт»). Чистый академический исследователь
без платёжеспособного проекта — Phase-2+ target.

### Канал

LinkedIn (academic/analyst segment), Email (direct холодный outreach через public
research publications), Referral (academia + think-tank networks).

### Message pattern

*«Jetix строит research infrastructure, которая помнит и синтезирует — чтобы
ты занимался анализом, а не компиляцией.»*

---

## 3.4 Инженер / Engineer

**Соответствие JETIX-VISION §7.1:** архетип 3 «Инженеры».
[src:decisions/JETIX-VISION.md §7.1 + §8 «Для Инженера»]

### Кто

System builder — software engineer, DevOps, solutions architect, technical founder,
embedded/hardware engineer с предпринимательским уклоном. Возраст: 25–45 лет.
Geography: глобальный, с концентрацией в US / EU / UK / Israel / Asia tech hubs.
Типичная выручка: $100K–$400K/год (senior IC или tech founder). Профессиональная
идентичность — строить вещи, которые работают надёжно и масштабируются. Не просто
писать код, а проектировать системы с правильными абстракциями.

Важный Phase-1 qualifier из icp.md [src:swarm/wiki/operations/quick-money/icp.md]:
Инженер квалифицируется как Phase-1 buyer ТОЛЬКО если является company-owner или
founder — не individual IC. Индивидуальный IC без P&L-ответственности — Phase-2+ target.

### Мотивация

**Что говорит:** «Мне интересны AI-агенты, протоколы взаимодействия, архитектурные
решения.»
**Что на самом деле нужно:** быть на острие технологического фронтира — строить
primitives, которые имеют значение, а не поддерживать legacy stack. USB-C positioning
(D20) — это именно тот уровень, который инженер узнаёт как «настоящую архитектурную
задачу». Вторичная нужда: productivity multiplier на собственные проекты через
AI-augmented workflow (wiki, agents, pipelines).

Инженер-founder дополнительно мотивирован бизнес-leverage: как построить компанию,
которая масштабируется без линейного роста команды? Jetix methodology отвечает именно
на этот вопрос.

### Что ищет от Jetix

1. **USB-C-level infrastructure** — участие в строительстве standards-level
   AI-to-AI и business-cooperation протоколов (D20).
2. **AI-augmented engineering workflow** — wiki + agent system как productivity
   multiplier на сложные технические задачи.
3. **Architectural insight** — framework мышления о multi-agent systems, которого
   нет в mainstream engineering literature.
4. **Phase 2+ sub-network** — общение с другими strong engineers строящими
   похожие системы, без ограничений NDA.

### Что даёт Jetix

- **Phase 1:** 4-pack с акцентом на «конкретную помощь» — AI-agent pipeline
  setup, KB architecture, consulting retainer.
- **Phase 2+:** Secure Network thematic sub-channel для инженеров; tool-sharing
  складчина (Claude Code max, expensive research tools); доступ к matchmaker
  mechanic D21 для сложных технических задач.
- **Phase 3+:** USB-C positioning D20 [src:decisions/JETIX-VISION.md §8 «Для Инженера»]
  — реальное участие в строительстве universal connector infrastructure.
  Roy-leader path: Инженер с командой может стать roy-leader технического роя.

**F-tag:** F4 — operational convention, подтверждена D20 locked decision.
Scope: holds для tech founder / company-owner engineers; NOT valid для individual
IC без decision authority (не Phase-1 buyer).
**R:** refuted если первые Инженер-клиенты не видят ROI в консалтинге за 90 дней
(acceptance = ≥1 engineering workflow improvement documented в их project KB).

### Канал

LinkedIn (technical founder segment), Referral (engineering communities: Hacker News,
internal Slack networks), Email.

### Message pattern

*«Ты строишь системы — Jetix даёт методологию, которая превращает AI в такую же
надёжную часть архитектуры, как хорошая база данных.»*

---

## 3.5 Инвестор / Investor

**Соответствие JETIX-VISION §7.1:** архетип 4 «Инвесторы».
[src:decisions/JETIX-VISION.md §7.1 + §8 «Для Инвестора»]

### Кто

Pattern-seeker с капиталом и горизонтом мышления. Ангел-инвестор, LP в венчурном
фонде, family-office manager, VC partner, serial entrepreneur перешедший в investment
mode. Возраст: 32–60 лет. Geography: US / EU / UK / Singapore / Israel — где
концентрируется early-stage tech capital. Типичная выручка/капитал: $1M+/year net
(millionaire tier) или значительный AUM ($5M+). Профессиональная идентичность:
видеть паттерны раньше рынка, делать ставки на правильных людей и системы.

Phase-1 квалификация: Инвестор — Phase-2+ target по дефолту [src:swarm/wiki/operations/quick-money/icp.md §Phase-1 Filtered Archetypes]. Исключение:
Инвестор, который одновременно является operating entrepreneur (строит свои компании
и инвестирует) — тогда он квалифицируется через Startupper или Operator архетип.
Чистый LP или пассивный VC — Phase-3+ через $1T trajectory и token economy.

### Мотивация

**Что говорит:** «Я хочу понять, куда движется AI и где реальные возможности.»
**Что на самом деле нужно:** информационное преимущество + portfolio compounding.
Инвестор платит за качественный signal, а не за noise. Jetix — это methodology +
operating system, применяемые к реальным бизнесам; это live case study с
measurable outcomes, который он может валидировать, прежде чем сделать ставку.
Плюс: engineering-faith framing (D19) — не hype, а реальные tools + план.

### Что ищет от Jetix

1. **$1T trajectory participation** — быть early в чём-то потенциально civilizational.
2. **Portfolio compounding mechanic** — roy-replication D21 как diversified portfolio:
   каждый рой — unit с multi-M ожидаемым return, ecosystem of roys = naturally
   diversified portfolio.
3. **Signal quality** — доступ к first-mover research data D24 + quality-gated
   peer network с другими adequate investors.
4. **Phase 2+ token economy** — альтернативный liquidity path D23.

### Что даёт Jetix

- **Phase 2+:** Secure Network — quality-gated пространство, где Инвестор
  встречает adequate entrepreneurs и researchers (matchmaker D21).
- **Phase 3+:** $1T trajectory bet [src:decisions/JETIX-VISION.md §8 «Для Инвестора»];
  holding structure D19; roy-replication methodology D21 как portfolio multiplier;
  token economy D23 как IPO-alternative liquidity.
- **Self-funded start + revenue-gated unlocks D15** — низкорисковая checkpoint model,
  которую Инвестор понимает как «строили правильно, не burn-and-hope».

### Канал

Referral (primary — Инвесторы приходят через доверенных людей, не через LinkedIn
outreach), LinkedIn (indirect — через content demonstrating methodology depth).

### Message pattern

*«Jetix — не очередной AI-стартап. Это methodology company, строящая infrastructure
для $1T trajectory. Ранние партнёры получают inside view на то, как выглядит
правильная AI-компания изнутри.»*

---

## 3.6 Философ / Thinker

**Соответствие JETIX-VISION §7.1:** архетип 8 «Философы».
[src:decisions/JETIX-VISION.md §7.1 + §8 «Для Философа»]

### Кто

Seeker of operational wisdom — не академический философ, читающий лекции, а человек
с глубоким концептуальным мышлением, применяющий его к практическим системам:
independent thinker, стратег с философским background, системный мыслитель, автор
non-fiction с прикладным уклоном, executive с сильной epistemological базой.
Возраст: 30–55 лет. Geography: глобальный. Типичная выручка: широкий диапазон —
от $80K (independent writer/speaker) до $500K+ (executive/consultant с философским
подходом к стратегии). Профессиональная идентичность: «я думаю глубже, чем большинство,
и хочу, чтобы это мышление имело практический выход».

Phase-1 квалификация: Философ — Phase-2+ target по дефолту
[src:swarm/wiki/operations/quick-money/icp.md]. Исключение: Философ, который является
entrepreneur с revenue — тогда проходит через Startupper. Чистый philosophical retreat
seeker без action-drive — анти-ICP (D22 upward-direction требует действия, не только
рефлексии).

### Мотивация

**Что говорит:** «Мне интересна методология, а не просто инструменты.»
**Что на самом деле нужно:** среда, где глубокое мышление не considered luxury, а
является primary asset. Философ устал от поверхностных профессиональных кругов;
он хочет reasoning на уровне — с людьми, которые понимают системы, историю, epistemology.
Jetix anti-attention-economy stance + cascading-leverage framework — это precisely те
якоря, которые его привлекают.

### Что ищет от Jetix

1. **200-year thinking frame** — место, где long-horizon думают операционально,
   не абстрактно.
2. **Open-source research direction D24** — канал для вклада в общественно значимые
   вопросы («как должна работать будущая экономика» [src:decisions/JETIX-VISION.md §8 «Для Философа»]).
3. **Adequate peer group** — Secure Network как качественная альтернатива
   philosophical retreat и academic echo-chamber.
4. **Operational wisdom infrastructure** — wiki + agent stack как инструмент
   превращения мышления в действия.

### Что даёт Jetix

- **Phase 2+:** Open-source research direction D24; thematic sub-network для философов
  и системных мыслителей; tool-sharing складчина.
- **Upward-direction community filter D22** — гарантия, что окружение adequate,
  не мотивационный circle.
- **Долгосрочная гравитация:** «смысл, который переживёт основателя» — compatible
  с философским natural affinity к things of life scale.

### Канал

Referral (primary — Философы приходят через интеллектуальные связи), LinkedIn (content
demonstrating depth: long-form methodology posts, not listicles), Email.

### Message pattern

*«Jetix — методология, а не ещё один tool. Если ты думаешь о системах на горизонте
десятилетий — здесь есть кому говорить об этом оперативно.»*

---

## 3.7 Соединитель / Connector

**Статус:** L6-deep-dive addition — НЕ присутствует под этим именем в JETIX-VISION §7.1
canonical 11-archetype list. Rationale: bridges «Менеджеры/коммуникаторы» (archetype 7
из §7.1) + matchmaker role D21. Соединитель — это операциональная специализация
Менеджера/коммуникатора, у которого primary value — не управление процессами, а
генерация connections между людьми и возможностями.
[src:decisions/JETIX-VISION.md §7.1 archetype 7 «Менеджеры/коммуникаторы»]

### Кто

Профессиональный networker и broker of relationships — Chief Partnership Officer,
business development lead, community builder, event organizer, executive recruiter
с предпринимательским уклоном, alliance manager. Возраст: 28–50 лет. Geography:
US / EU / UK — рынки с развитой professional networking культурой. Типичная
выручка: $80K–$300K (BD/partnerships roles) или $150K–$500K (independent broker).
Профессиональная суперсила: знает, кому нужен кто, и умеет сводить нужных людей
в нужный момент с правильным framing. Работает через доверие и репутацию — каждая
рекомендация несёт его личный бренд.

### Мотивация

**Что говорит:** «Мне нужна платформа, где я могу создавать ценность для своей сети.»
**Что на самом деле нужно:** инфраструктура для систематизации своей matchmaking
деятельности + качественный pool из которого делать connects. Соединитель — не
просто human matchmaker; он хочет, чтобы его connects приводили к measurable outcomes,
а не просто к coffee chats. Jetix matchmaker mechanic D21 + Secure Network — это
именно та инфраструктура, которая превращает его superpower в scalable practice.

Вторичная мотивация: быть «inside» качественного сообщества сильных людей —
это активы для его профессиональной деятельности. Quality network × quality
framing = его основной продукт.

### Что ищет от Jetix

1. **Matchmaker mechanic D21** — AI-assisted coordination infrastructure, которая
   умножает его naturally high throughput.
2. **Quality pool** — Secure Network как источник adequate matches, а не LinkedIn noise.
3. **Alliance membership** — позиция «connector inside Alliance» как professional
   credential в нише AI-business cooperation.
4. **Revenue-share mechanic** — Phase 2+ partnership revenue-share D21 для успешных
   introduc- tions/matches.

### Что даёт Jetix

- **Phase 2+:** matchmaker mechanic D21 [src:decisions/JETIX-VISION.md §5 «Emerging»]
  — AI-агенты смазывают coordination, Соединитель получает tool-layer под свою
  superpower. Revenue-share partnership за успешные matches.
- **Secure Network:** тематический sub-channel + качественный pool для connects.
- **Phase 3+:** роль connector-in-residence в экосистеме рой-репликации D21 —
  как масштабировать matchmaking methodology на другие рои.

**F-tag:** F3 — паттерн наблюдается из D21 matchmaker mechanic и JETIX-VISION §7.1
«Менеджеры/коммуникаторы»; нет прямого locked decision на этот архетип как отдельную
единицу. Scope: holds как operational specialisation в Phase 2+; unknown Phase 1
(matchmaker mechanic не активна в Phase 1).
**R:** refuted если в Phase 2+ Соединитель не конвертируется в revenue-generating
match (acceptance: ≥1 successful match с документированным revenue-share за первые
6 месяцев Phase 2).

### Канал

Referral (primary — Соединители живут в referral economy), LinkedIn (secondary — они
активны на LinkedIn по-другому: не pitch, а introductions/comments/reshares).

### Message pattern

*«Твоя суперсила — знать нужных людей. Jetix строит инфраструктуру, которая превращает
это в масштабируемую практику, а не личный героизм.»*

---

## 3.8 Athlete / Disciplined Builder

**Статус:** L6-deep-dive addition — НЕ присутствует в JETIX-VISION §7.1 canonical list.
Rationale: personification of D22 «Stable» criterion — habits + endurance + recovery
as life-OS. Overlap с «Разработчики жизни» (archetype 10 из §7.1). Athlete —
это Разработчик жизни, у которого physical discipline является primary identity frame
и source of his operating philosophy.
[src:decisions/JETIX-VISION.md §7.1 archetype 10 «Разработчики жизни» + §7.2 «Stable»]

### Кто

Человек, для которого физическая дисциплина — не хобби, а операционная философия:
triathlete-entrepreneur, военный офицер переходящий в business, professional athlete
заканчивающий карьеру и строящий второй act, high-performance coach (физический или
mental performance). Возраст: 28–45 лет. Geography: US / EU / AU — рынки с развитой
high-performance culture. Типичная выручка: $80K–$500K (спортивная карьера + бизнес /
coaching practice). Характерная черта: он применяет к бизнесу ту же структуру, что
к спортивным тренировкам — periodization, recovery, progressive overload, metrics.
«Stable» из D22 filter — это буквально он [src:decisions/JETIX-VISION.md §7.2].

### Мотивация

**Что говорит:** «Мне нужна система для жизни и бизнеса, которая работает как
спортивная программа — структурированно, с измеримым прогрессом.»
**Что на самом деле нужно:** перенести свои highest-performance habits в domain
building/business таким образом, чтобы они reinforced, а не competed with друг другом.
Главный pain: «всё, что я делал физически — работало, потому что у меня была методология.
В бизнесе такой методологии не было.» Jetix methodology — это что-то, что он
концептуально понимает: operating system с discipline layer + measurement + compounding.

### Что ищет от Jetix

1. **Life-OS methodology** — structured framework, объединяющий физическую дисциплину,
   знания и бизнес в единую систему (cascading-leverage: жизнь → проекты).
2. **AI-augmented performance tracking** — wiki + agents как «coach», который помнит
   всё, анализирует паттерны, предлагает adjustments.
3. **Peer group с skin-in-game** — среда, где дисциплина является нормой, а не
   исключением. Founder persona Ruslan («отшельник-спортсмен» [src:decisions/JETIX-VISION.md §3])
   — это именно тот archetype, которому Athlete доверяет.
4. **Build-in-public accountability** — Secure Network как structured accountability
   environment, не social media audience.

### Что даёт Jetix

- **Phase 1:** 4-pack — особенно «конкретная помощь» в structured life + project
  operating system setup. Wiki methodology applied to personal performance system.
- **Founder-resonance:** Ruslan's triple-archetype identity («отшельник-спортсмен»
  internal driver) [src:decisions/JETIX-VISION.md §3] создаёт credibility — он не
  продаёт productivity hacks, он сам так живёт.
- **Phase 2+:** Secure Network thematic channel для high-performance builders;
  tool-sharing складчина для performance tracking tools.

**Честный флаг (dissent):** Athlete как отдельный архетип — самый слабо обоснованный
из L6-deep-dive additions. Overlap с «Разработчики жизни» (JETIX-VISION §7.1 archetype 10)
очень велик. Основание для включения: founder persona Ruslan явно содержит этот
archetype как internal driver, что создаёт authentic resonance в outreach.
Однако Athlete как primary buyer — Phase-2+ через Life-OS Secure Network sub-channel,
не Phase-1 консалтинг. Dissent preserved per AP-6.

**F-tag:** F2 — основан на founder-persona pattern и D22 «Stable» criterion.
Нет прямого locked decision на этот архетип. Scope: conditional.
**R:** refuted если Phase-2 Secure Network не привлекает ≥5% членов из
high-performance/disciplined-builder background (acceptance tracking через
onboarding profile data).

### Канал

Referral (primary — high-performance communities: CrossFit, triathlon, military alumni
networks), LinkedIn (secondary), Podcast (athletic/performance content creators).

### Message pattern

*«Ты уже знаешь как выглядит методология — в спорте. Jetix — это та же логика,
применённая к бизнесу и жизни одновременно.»*

---

## 3.9 Designer / Creative

**Статус:** L6-deep-dive addition — НЕ присутствует под этим именем в JETIX-VISION §7.1.
Rationale: overlap с «Разработчики идей» (archetype 9 из §7.1). Designer — это
Разработчик идей с конкретным профессиональным skill-set в visual / product / UX
design, у которого creative work является primary identity, но который одновременно
строит свой бизнес или продукт.
[src:decisions/JETIX-VISION.md §7.1 archetype 9 «Разработчики идей»]

### Кто

Creative professional с бизнес-амбицией: UX designer-founder, brand strategist,
product designer перешедший в entrepreneurship, creative director с собственным
агентством, indie game developer. Возраст: 25–42 лет. Geography: US / EU — дизайн-
экосистемы (NYC, SF, Berlin, Amsterdam, London). Типичная выручка: $70K–$400K/год.
Profil: сильные conceptual и execution skills, но слабая бизнес-система. Идеи —
в избытке; structured delivery — bottleneck. AI-отношение: творческий скептик,
который боится, что AI убьёт creativity, но при этом любопытен к правильному
применению (AI как amplifier, не replacement).

### Мотивация

**Что говорит:** «Мне нужно mastering AI tools для творческой работы.»
**Что на самом деле нужно:** система, которая освобождает творческую энергию от
операционного overhead. Designer тратит 40–60% времени на non-creative work
(client management, project tracking, billing, repurposing outputs). AI-усиленный
workflow — это шанс вернуть эти часы в созидание. Вторичная нужда: превратить
творческую экспертизу в productized business, а не оставаться на hourly billing.

### Что ищет от Jetix

1. **AI-amplified creative workflow** — prompt engineering + agent pipeline adapted
   к creative work, не generic business automation.
2. **Productization guidance** — перейти от hourly billing к productized creative
   services / templates / courses.
3. **Conceptual resonance** — methodology, которая respects aesthetics и systems
   одновременно. Designer распознаёт качество системного мышления — это его язык.
4. **Peer environment** — среда creative professionals с drive, не lifestyle-bloggers.

### Что даёт Jetix

- **Phase 1:** 4-pack — особенно «10 шаблонов» как lead magnet (Designer ценит
  quality artifacts) и «конкретная помощь» в productization.
- **Phase 2+:** matchmaker mechanic D21 — дизайн-задачи для других членов
  сообщества (Designer как specialist в pool); Secure Network sub-channel для
  creative professionals.
- **Open inside / Closed outside D3 + methodology aesthetics** — качество
  самого Jetix operating system как демонстрация «что значит сделать хорошо».

**Честный флаг:** Designer как отдельный архетип — L6-deep-dive addition с умеренным
обоснованием. Сильный overlap с «Разработчики идей» из JETIX-VISION §7.1. Relevance
сохраняется через Phase-1 Продюсерский центр (дизайн-компонент content production)
и Phase-2+ matchmaker (creative specialists in pool).

**F-tag:** F3 — pattern наблюдается из «Разработчики идей» §7.1 и Продюсерский
центр D11 context. Scope: conditional Phase-1; stronger Phase-2+.
**R:** refuted если Designer-archetype не представлен в первых 10 Продюсерский центр
клиентах (acceptance: ≥2 из 10 с creative-professional background).

### Канал

LinkedIn (designer/creative-founder segment), Referral (design community networks:
Dribbble, Behance professional circles), Instagram/Behance (secondary portfolio
discovery).

### Message pattern

*«Jetix не заменяет твоё творчество — он берёт operational overhead, чтобы у тебя
осталось время и энергия на то, что только ты можешь сделать.»*

---

## 3.10 Teacher / Educator

**Статус:** L6-deep-dive addition — НЕ присутствует под этим именем в JETIX-VISION §7.1.
Rationale: overlap с «Блогеры» (archetype 11 §7.1, особенно «specialist-blogger делающий
deep technical / business / research content»). Teacher — это Блогер с первичной
identity в teaching/education (курсы, bootcamps, corporate training, workshops),
а не в content creation per se. Referenced in voice-memos context (audio_528 per
launch prompt §3 framing).
[src:decisions/JETIX-VISION.md §7.1 archetype 11 «Блогеры»]

### Кто

Educational entrepreneur — создатель онлайн-курсов, корпоративный тренер с собственным
IP, bootcamp founder, workshop facilitator, university professor монетизирующий экспертизу
через independent education business. Возраст: 28–50 лет. Geography: English-speaking
market primary (US / UK / AU / international). Типичная выручка: $80K–$600K/год (микс:
Teachable/Kajabi courses + corporate training + live cohorts). Структурная проблема:
курс создаётся один раз, а curriculum update + новые cohorts + community management —
ongoing overhead, который съедает время. Каждый новый курс начинается с нуля по
research и production.

### Мотивация

**Что говорит:** «Мне нужно масштабировать обучение без роста overhead.»
**Что на самом деле нужно:** методология создания, обновления и delivery обучающего
контента с AI-усилением, которая позволяет масштабировать количество студентов и курсов
без пропорционального роста рабочего времени. Вторичная нужда: community layer вокруг
обучения — вовлечённые студенты, которые становятся peer learners и ambassadors, а
не пассивные потребители видео.

Teacher-архетип — прямой overlap с Продюсерским центром D11 (research → curriculum →
production → repurposing pipeline) и с Blогер-архетипом через shared dimension
«specialist с аудиторией». Разница: Блогер монетизирует через контент + аудиторию;
Teacher монетизирует через образовательные программы как primary product.

### Что ищет от Jetix

1. **Curriculum development pipeline** — AI-усиленный research → curriculum design →
   content production workflow.
2. **Cohort community infrastructure** — Secure Network или sub-platform как venue
   для engaged learning community.
3. **Productization upgrade** — перейти от «я продаю курс» к «я управляю
   educational system с AI backend».
4. **Peer educator network** — качественный обмен best practices по AI-усиленному
   обучению с другими educators.

### Что даёт Jetix

- **Phase 1:** Продюсерский центр D11 [src:decisions/JETIX-VISION.md §5 «Продюсерский центр»]
  — research → curriculum → production pipeline под AI-enhanced operations. Прямой fit.
- **4-pack overlap:** «конкретная помощь» в построении educational pipeline;
  «10 шаблонов» как sample of Jetix methodology applied to curriculum design.
- **Phase 2+:** Secure Network sub-channel для educators; matchmaker D21 для
  collab между educators и subject-matter experts.
- **Phase 3+:** open-source research direction D24 — educational research contribution.

**Честный флаг:** Teacher и Блогер сильно пересекаются. Разделение оправдано для
messaging differentiation (Teacher лучше реагирует на «curriculum» и «learning system»
framing, Блогер — на «production pipeline» и «audience monetization»). В Secure
Network они могут находиться в одном sub-channel.

**F-tag:** F4 — operational convention подкреплена Продюсерский центр D11 и audio_528
reference. Scope: holds для English-speaking educational entrepreneur; NOT valid для
academic professor без independent business.
**R:** refuted если Teacher-archetype не конвертируется в Продюсерский центр retainer
(acceptance: ≥1 Teacher-клиент на retainer в Phase 1).

### Канал

LinkedIn (educator/course-creator segment), Email (direct outreach через public
course-landing pages или edu-community presence), Referral (educator mastermind
groups, bootcamp networks).

### Message pattern

*«Ты создаёшь знания — Jetix строит систему, которая превращает их в масштабируемые
образовательные продукты без роста твоих часов.»*

---

## 3.11 Operator / Founder-CEO

**Статус:** L6-deep-dive addition — НЕ присутствует под этим именем в JETIX-VISION §7.1.
Rationale: overlap с «Менеджеры/коммуникаторы» P&L-responsible variant (archetype 7
из §7.1) + «Предприниматели/бизнесмены» founder subtype (archetype 1 из §7.1).
Operator/Founder-CEO — это конкретный sub-archetype: человек, который одновременно
является основателем и операционным руководителем компании с командой, P&L и
scaling challenges. Это не просто «entrepreneur с нахрапом» — это человек, который
уже прошёл стадию founder и now operates as a CEO managing people and systems.
[src:decisions/JETIX-VISION.md §7.1 archetype 1 + archetype 7 + §8 «Для Менеджера»]

### Кто

Founder-CEO компании с командой 5–50 человек и revenue $1M–$50M/год.
Может быть Series-A стартапом, семейным бизнесом в growth phase, или digital agency
перешедшей в product-led model. Возраст: 30–52 года. Geography: US / EU / UK — рынки
с достаточно зрелым startup ecosystem. Ключевая характеристика: этот человек носит
слишком много шляп. Он — стратег, продавец, HR director, product manager, и operational
coordinator одновременно. AI — это его шанс создать leverage в тех областях, где он
тратит время, но не создаёт непропорциональный вклад.

Overlap с Deutscher Mittelstand Archetype A из icp.md [src:swarm/wiki/operations/quick-money/icp.md §Archetype A] — но Operator шире: включает digital-first businesses,
не только manufacturing/services Mittelstand.

### Мотивация

**Что говорит:** «Мне нужно делегировать операционную рутину — но правильно, с
системой, а не хаотично.»
**Что на самом деле нужно:** governance framework + AI-delegation pattern, который
позволяет ему фокусироваться на 6 non-delegatable функциях (стратегия / вкус /
ответственность / утверждение / эскалация / отношения — architect-orbit из
JETIX-VISION §3 [src:decisions/JETIX-VISION.md §3]) и делегировать всё остальное
системе, агентам и команде.

Он не хочет «больше AI tools» — он хочет operating system, которая работает как
у него в голове, но с командой из 20 человек + AI-агентами. Jetix — это именно
такая операционная методология, не очередной task manager.

### Что ищет от Jetix

1. **Governance framework** — architect-orbit (6 non-delegatable functions) +
   delegation pattern + handoff protocols. Как правильно выстроить принятие решений
   в организации с AI-layer.
2. **Solo-with-team-ready scaffolding D2** — infrastructure, которая масштабируется
   с командой без full refactor каждые 6 месяцев.
3. **AI-augmented operations** — agent pipeline setup, KB architecture для corporate
   memory, structured decision-making protocols.
4. **Peer CEO network** — quality-gated среда для обмена с другими операционно-
   компетентными основателями, без investor pitch dynamics.

### Что даёт Jetix

- **Phase 1:** 4-pack с акцентом на «конкретную помощь» — AI-agent pipeline setup,
  corporate KB architecture, consulting retainer с governance focus.
- **For Менеджера angle** [src:decisions/JETIX-VISION.md §8 «Для Менеджера»]:
  governance pattern (architect-orbit + agent delegation + handoff protocols);
  solo-with-team-ready scaffolding D2; Phase 2+ meta-coordination рой-репликации D21.
- **Phase 2+:** matchmaker D21 — Operator может делегировать complex tasks на
  specialists через Jetix network; Secure Network CEO/founder sub-channel.
- **Phase 3+:** roy-coordination phase — Operator с достаточным scale становится
  roy-leader и meta-coordinator в Jetix ecosystem.

**F-tag:** F4 — operational convention, подкреплена D2 solo-with-team-ready locked
decision + architect-orbit из §3 JETIX-VISION. Scope: holds для company-with-team
(≥5 people) Founder-CEO; NOT valid для solo-operator без команды (тот — Startupper).
**R:** refuted если Operator-клиенты не видят governance improvement через 60 дней
работы с Jetix (acceptance: ≥1 documented decision-framework deployed in client
company per consulting engagement).

### Канал

LinkedIn (CEO/founder segment — decision-maker по определению), Referral (CEO peer
networks: Vistage, EO, YPO, founder mastermind groups), Email (direct к known
company owners через research).

### Message pattern

*«Ты уже знаешь, что делегировать. Jetix строит систему, которая делает делегирование
воспроизводимым — с AI-layer, который помнит всё и не устаёт.»*

---

## §3.X Сводная таблица архетипов

| # | Архетип | JETIX-VISION §7.1 соответствие | Phase-1 buyer? | Основной канал | Jetix value в одном предложении |
|---|---|---|---|---|---|
| 3.1 | Startupper | Предприниматели/бизнесмены + Блогеры subtype | YES (Tier-1) | LinkedIn, Referral | Система вместо набора инструментов |
| 3.2 | Блогер | Блогеры (archetype 11) | YES (Продюсерский центр) | LinkedIn, Referral, Podcast | Production pipeline под AI |
| 3.3 | Исследователь | Ресёрчеры (archetype 2) | Conditional | LinkedIn, Email | Research infrastructure с memory |
| 3.4 | Инженер | Инженеры (archetype 3) | Conditional (founder only) | LinkedIn, Referral | AI как надёжная часть архитектуры |
| 3.5 | Инвестор | Инвесторы (archetype 4) | Phase-2+ primary | Referral | $1T trajectory inside view |
| 3.6 | Философ | Философы (archetype 8) | Phase-2+ primary | Referral, LinkedIn | Methodology + adequate peer group |
| 3.7 | Соединитель | Менеджеры/коммуникаторы (archetype 7) — L6-addition | Phase-2+ primary | Referral, LinkedIn | Matchmaking как масштабируемая практика |
| 3.8 | Athlete | Разработчики жизни (archetype 10) — L6-addition | Phase-2+ conditional | Referral, Podcast | Спортивная методология → бизнес |
| 3.9 | Designer | Разработчики идей (archetype 9) — L6-addition | Conditional Phase-1 | LinkedIn, Referral | Creative time без operational overhead |
| 3.10 | Teacher | Блогеры/Educator subtype — L6-addition | YES (Продюсерский центр) | LinkedIn, Email | Знания → масштабируемые образовательные продукты |
| 3.11 | Operator/Founder-CEO | Предприниматели + Менеджеры — L6-addition | YES (primary) | LinkedIn, Referral | Делегирование как воспроизводимая система |

---

## §3.Y Интегративные наблюдения (F/ClaimScope/R)

### Claim-1: L6-deep-dive additions (#7–#11) не создают новые archetypes, они детализируют существующие

**F:** F4 (операциональная конвенция, логически выводима из JETIX-VISION §7.1 + §8)
**ClaimScope:** holds для целей документа LAYER-6-COMMUNITY-DEEP-DIVE.md (outreach
messaging + community segmentation); NOT valid как replacement для locked D7 canonical
list в других документах. JETIX-VISION §7.1 остаётся авторитетной canonical
11-archetype enumeration для D1.
**R:** refuted если Ruslan в ack решит сократить список обратно до 7 JETIX-VISION-aligned
архетипов (принятая canonical enumeration supersedes L6 additions); accepted если
LAYER-6-COMMUNITY-DEEP-DIVE.md §3 принимается с 11 позициями как-есть.

### Claim-2: Phase-1 активный outreach — максимум 4 из 11 архетипов

**F:** F5 (KPI-trackable через icp.md + intake §6.1 expanded spectrum)
**ClaimScope:** holds для Phase-1 solo-founder bandwidth constraint + €50K Q2 2026
kill-or-continue deadline; NOT valid после SG-2 (first signed contract = unlock trigger).
**R:** refuted если expanded ICP spectrum (intake §6.1) позволяет Operator/Founder-CEO
и Блогер/Teacher конвертироваться в Phase-1 Продюсерский центр или consulting clients
до SG-2; accepted если first 5 signed contracts come from Startupper + Блогер +
Teacher + Operator четырёх архетипов (что подтвердит Phase-1 scope).

### Claim-3: Соединитель и Athlete — самые слабо обоснованные L6-additions; их inclusion в §3 оправдан messaging value, не archetype distinctiveness

**F:** F3 (паттерн из founder-persona и D21/D22, нет прямого locked decision)
**ClaimScope:** holds для outreach messaging segmentation в §7; conditional для
community sub-channel segmentation в §10.
**R:** refuted если в Phase-2 Secure Network onboarding data показывает <3% членов
self-identifying с Соединитель/Athlete primary identity; accepted если ≥5% самоидентифицируются.

---

*End of §3 cell C-03 draft.*
