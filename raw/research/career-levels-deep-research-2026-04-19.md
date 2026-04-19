# Career Ladders, Decision-Rights и Phase Transitions: Академическое исследование для Jetix

**Язык:** Русский | **Дата:** 2025 | **Аудитория:** Ruslan Tymchuk, founder Jetix, Берлин

---

## Введение

Проектирование карьерной лестницы — это не HR-документ, а архитектурное решение. Оно определяет, кто вправе принимать какие решения, с каким скоупом, на каком горизонте и с какой accountability. Для Jetix — AI-native operating system, строящегося одним founder под mega-corporation — эта архитектура критически важна с Day 1: 12 ролей сегодня, 30–200 завтра, причём исполнители могут быть Ruslan, Claude-агенты или future humans, использующие единую role-abstraction.

Данный отчёт охватывает семь частей: software IC ladders (A), consulting + German Mittelstand (B), C-suite evolution (C), decision-rights frameworks (D), delegation patterns (E), AI-augmentation карьерных путей (F) и финальные практические рекомендации для Jetix (G).

---

## Part A. Career Ladders в Software-индустрии

### A1. IC Track: от Junior до Distinguished Engineer

Современный Individual Contributor (IC) трек в software-индустрии сформировался в 1990-х в Microsoft и IBM, а в 2010-х систематизирован в FAANG-компаниях. [Will Larson](https://staffeng.com/guides/staff-archetypes/) в книге «Staff Engineer» (2021) первым описал post-senior IC-роли как самостоятельный карьерный путь с собственными архетипами и decision-rights.

| Уровень | Google | Meta | Amazon | Netflix | Scope | Time-in-role | Decision-rights |
|---------|--------|------|--------|---------|-------|-------------|-----------------|
| Junior / IC-1 | L3 | E3 | SDE I (L4) | E3 | Задача, feature | 1–2 года | Execute only |
| Mid / IC-2 | L4 | E4 | SDE II (L5) | E4 | Feature, компонент | 2–3 года | Feature-level decisions |
| Senior / IC-3 | L5 | E5 | SDE III (L6) | E5 | Система, команда | 3–5 лет | Architecture decisions in scope |
| Staff / IC-4 | L6 | E6 | Principal (L7) | E6 | Multi-team, домен | 3–6 лет | Cross-team technical authority |
| Principal / IC-5 | L7 | E7 | Sr. Principal (L8) | E7 | Org, business unit | Varies | Org-level technical strategy |
| Distinguished / Fellow | L8–L10 | E8–E10 | Distinguished (L9–L10) | — | Company / Industry | Career | Company + industry direction |

**Junior (L3/E3/SDE I):** Работает на хорошо определённых задачах под менторством. Impact измеряется в features, delivered за спринт. [Meta E3](https://www.lodely.com/blog/meta-software-engineer-levels) фокусируется на изучении инструментов и кодовой базы; [Amazon SDE I](https://www.levels.fyi/blog/amazon-leveling-progress.html) решает clearly defined проблемы с ограниченной имплементационной самостоятельностью. Decision-rights: execute only — выбор подхода к реализации конкретного таска, не более.

**Mid (L4/E4/SDE II):** Переход от «делать задачи» к «владеть фичами». Значительно меньший надзор. [Meta E4](https://www.lodely.com/blog/meta-software-engineer-levels) участвует в design discussions, принимает технические решения самостоятельно. У Amazon L5 — намеренно широкая полоса неопределённости, перекрывающая SDE I снизу и SDE III сверху. Decision-rights: feature-level, выбор технического подхода внутри границ команды.

**Senior (L5/E5/SDE III):** Исторически «терминальный» уровень для большинства инженеров. В Google L5 — первый уровень с реальной автономией ([Interview Kickstart](https://interviewkickstart.com/blogs/articles/google-software-engineer-level)). [Amazon SDE III](https://www.levels.fyi/blog/amazon-leveling-progress.html) «начинает делать business tradeoff decisions», менторит других, ведёт large chunks работы. Impact: team-level, квартальный. Time-in-role: 3–5 лет типично, ceiling для многих.

**Staff (L6/E6/Principal):** Критический переход. По [Larson](https://staffeng.com/guides/staff-archetypes/), Staff engineer действует в одном из четырёх архетипов:
- **Tech Lead** — ведёт подход одной или нескольких команд; ~1 на 8 инженеров; самый распространённый; первый Staff-опыт для большинства
- **Architect** — отвечает за направление, качество и подход в критической области (API design, storage strategy, cloud infrastructure); требует «organizational authority earned by consistently good judgment»
- **Solver** — погружается в произвольно сложные проблемы, обозначенные организационным руководством; bounces between hotspots; «requires soft touch to avoid infuriating teams left to maintain the solved problem»
- **Right Hand** — расширяет внимание executive, заимствует его scope и authority; «akin to operating as senior organizational leader without direct managerial responsibilities»; появляется в компаниях от 500+ инженеров

Meta E6 [«играет критическую роль в постановке целей команды, влияет на организацию за пределами команды»](https://www.lodely.com/blog/meta-software-engineer-levels). Amazon Principal SDE (L7) «влияет на работу 50–100+ инженеров», предоставляет стратегическое техническое руководство директорам и VP. Decision-rights: cross-team technical authority, участие в hiring decisions, право блокировать architectural направления.

**Principal (L7/E7/Sr. Principal):** [Meta E7](https://dev.to/alexr/meta-software-engineer-levels-4bdm) «влияет на техническую стратегию по большим секциям Meta», ведёт инициативы, охватывающие несколько продуктов или целые домены. Amazon Senior Principal (L8) «влияет на сотни инженеров», отвечает за multiple large systems. Impact: org-level, annual + multi-year. Decision-rights: организационная техническая стратегия, budget advocacy.

**Distinguished / Fellow:** [Meta E8](https://dev.to/alexr/meta-software-engineer-levels-4bdm) — «industry expert/leader», влияет за пределы компании. Google L10 Fellow «обычно ведёт несколько тысяч инженеров» ([Interview Kickstart](https://interviewkickstart.com/blogs/articles/google-software-engineer-level)). Эти роли существуют в 0.01–0.1% от engineering населения.

### A2. Management Track: Tech Lead → CTO

По [Camille Fournier](https://www.shortform.com/blog/the-managers-path-camille-fournier/) «The Manager's Path» (2017, O'Reilly):

1. **Tech Lead** — не официальная позиция, а set of responsibilities: технический лидер команды без прямых reports. Требует «готовности отойти от кода и найти баланс между техническими обязательствами и тем, что нужно всей команде». Fournier: нельзя ставить в TL только потому, что person — сильнейший инженер; нужна готовность развивать people skills.
2. **Engineering Manager (EM)** — первая официальная management роль: hiring, feedback, project management. Управляет 4–8 IC. «Even though you may stop writing code, your job will require that you guide technical decision making.» Ключевой навык: удержание технической relevance без прямого кодирования.
3. **Engineering Director** — управляет несколькими командами через EM'ов. Долгосрочное планирование, identify систем для обновления, training subordinates в новых навыках.
4. **VP Engineering** — large group management. Управляет менеджерами, cross-org alignment, hiring at director level. Fournier: 10 productive engineering weeks per engineer per quarter — ключевой planning benchmark.
5. **CTO** — по Fournier, специфика варьируется по компании. Фокус: техническое видение, внешнее представительство (клиенты, инвесторы), архитектурные решения company-wide. В стартапе CTO = principal engineer + VP Eng + external evangelist.

### A3. Dual Ladder и компенсационный паритет

Dual ladder — параллельные IC и management треки с эквивалентными уровнями, компенсацией и prestige. [Levels.fyi данные Q1 2026](https://letsdatascience.com/blog/staff-engineer-or-engineering-manager-which-pays-more) демонстрируют паритет:

| Компания | IC уровень | Медианная TC | Аналог менеджмента |
|---------|-----------|------------|-------------------|
| Google | L6 Staff | $580K | $591K (L6 EM) |
| Meta | E6 Staff | $775K | $700–900K (EM) |
| Amazon | L7 Principal | $654K | $651K (L7 Sr SDM) |
| Netflix | E6 | $728K | $670K–1.2M (SEM) |

Паритет реален при correct level alignment. Ключевая асимметрия: переход IC→management занимает один разговор, обратный путь — 2 года технического перестроения. Для dual ladder важен вопрос: есть ли у компании _реальный_ IC ladder или только номинальный? Тест: можно ли назвать имена Staff+ engineers, недавно получивших повышение на IC-треке?

### A4. Specialist Tracks и Startup специфика

**SRE / Security / ML / Data** треки существуют в компаниях 500+ инженеров. В Google SRE book (Beyer et al., 2016) описан SRE как гибрид software engineering + operations: 50% engineering minimum rule, error budget policy как shared decision-making механизм между SRE и product. Security engineers имеют собственный ladder с дополнительными expectations вокруг threat modeling и incident response. ML Engineers в компаниях типа Anthropic — отдельная специализация, где research publications служат leveling signal наряду с production impact.

**Tanya Reilly, «The Staff Engineer's Path» (2022)** ([O'Reilly](https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/)) описывает три столпа Staff-работы: (1) big-picture thinking — стратегический взгляд, понимание business context, «what will Future You wish Present You had done?»; (2) execution сложных проектов с ambiguity; (3) leveling up others — менторство и создание future leaders. Reilly: «The metric for success is whether other people want to work with you.»

**Startup (10–50 человек):** Титулы misleading — «Senior Engineer» в стартапе из 15 человек по scope ближе к Staff в FAANG. Netflix исторически имел **один** уровень для всех — Senior Software Engineer — и успешно масштабировался до ~2000 инженеров ([Pragmatic Engineer](https://blog.pragmaticengineer.com/netflix-levels/)). В 2022 году ввёл E3-E7 по двум причинам: cost efficiency и retention (Staff-инженеры из Big Tech не присоединялись, не видя Staff-title). Многие Senior из Netflix при retroactive leveling оказались на E5, что спровоцировало волну увольнений.

**Founder-led title inflation:** в стартапах до 50 человек founder часто раздаёт Senior+ ради найма, создавая inflation проблему при росте. Лучший proxy уровня в стартапе — «scope of decisions made autonomously», а не job title.

---

## Part B. Consulting Ladders (MBB) + German Mittelstand

### B1. MBB Career Ladder

MBB (McKinsey, BCG, Bain) имеют практически идентичную структуру с незначительными отличиями в названиях ([Hacking The Case Interview](https://www.hackingthecaseinterview.com/pages/mckinsey-career-path)):

| Уровень | McKinsey | BCG | Bain | Время в роли | Компенсация McKinsey |
|---------|----------|-----|------|-------------|----------------------|
| Entry | Business Analyst | Associate | Associate Consultant | 2–3 года | $112–148K |
| Post-MBA | Associate | Consultant | Consultant | 2–3 года | $192–249K |
| Project Leader | Engagement Manager | Project Leader | Senior Manager | 2–3 года | $250–300K |
| Pre-Partner | Associate Partner | Principal | Associate Partner | 2–3 года | $350–450K |
| Partner | Partner | Partner & MD | Partner | 3–5 лет | $500K–$2M+ |
| Senior Partner | Senior Partner | Senior Partner & MD | Director | До выхода | $2M–$5M+ |

**Decision-rights по уровням в MBB:**
- BA/Associate: Execute analysis, нет клиентских решений
- EM: Manage client expectations, approve workstream directions, lead client-facing meetings
- AP/Partner: Sign new engagements, expand/contract scope, fire or retain clients
- Senior Partner: Approve firm-level strategic direction, define practice areas

**Up-or-out:** [CaseCoach](https://casecoach.com/b/up-or-out-policy-mckinsey-bcg-or-bain/) описывает механизм: каждые 6 месяцев performance reviews, ~5% cohort выбывает после первого года. Комитет партнёров голосует анонимно. Весь путь BA→Partner занимает 8–12 лет при стандартном прогрессе; top performers достигают Partner за 6–8 лет.

**Utilization и billing rates:** Consultants билингуются клиентам по $300–500/час на junior-уровнях, $800–2000/час на partner-уровнях. Целевой utilization — 75–85% billable time. EM несёт ответственность за utilization команды. Значительная часть Partner-компенсации зависит от revenue generated (origination fees).

### B2. Big4 vs MBB vs Boutiques

Big4 (Deloitte, PwC, EY, KPMG) имеют более широкую лестницу: Analyst → Consultant → Senior Consultant → Manager → Senior Manager → Director → Partner. Ключевые отличия: меньше up-or-out давления, больше specialization по функциям (audit, tax, advisory), ниже billing rates, медианный путь до Partner — 12–18 лет. Менее жёсткая client development responsibility у нижних уровней.

Roland Berger (крупнейший независимый европейский) и Simon-Kucher (boutique pricing) — промежуточная модель: структура MBB, но менее жёсткий up-or-out, более глубокая отраслевая специализация. Roland Berger особенно силён в немецком automotive и Mittelstand контексте, что релевантно для Jetix как инструмента для немецкого рынка.

### B3. German Mittelstand: иерархия и Konsenskultur

[Mittelstand](https://en.wikipedia.org/wiki/Mittelstand) — немецкие SME с выручкой до €50M и штатом до 500 (по EU-определению), хотя в Германии включают и более крупные. 99% немецких компаний принадлежит к Mittelstand, обеспечивая 60%+ занятости.

Типичная иерархия Mittelstand-компании:

| Уровень | Немецкое название | Аналог в tech | Scope | Как назначается |
|---------|------------------|--------------|-------|----------------|
| 1 | Geselle / Facharbeiter | IC-1 | Исполнение | Ausbildung + Gesellenprüfung |
| 2 | Meister / Senior Fachkraft | IC-2/3 | Экспертиза + надзор | Meisterprüfung (IHK) |
| 3 | Teamleiter | Team Lead | 3–8 человек | Назначение Abteilungsleiter |
| 4 | Abteilungsleiter | Department Head | 1 функция | Назначение GF или Bereichsleiter |
| 5 | Bereichsleiter | Division Head | Несколько отделов | Назначение Geschäftsführer |
| 6 | Prokurist | Deputy MD | Юридическое делегирование | Handelsregister-регистрация |
| 7 | Geschäftsführer | CEO/MD | Вся компания | GmbHG §35, Handelsregister |

**Geschäftsführer** по немецкому праву (GmbHG §35) — юридически ответственный управляющий, обязательно регистрируется в Handelsregister. Не просто CEO-title, а legal accountability role. В малом Mittelstand нередко 1–2 Geschäftsführer совмещают роли стратегии, продаж и operations. Prokurist — промежуточная конструкция: юридически уполномоченный представитель без полных прав GF.

**Konsenskultur и семейный капитализм:** [The Conversation](https://theconversation.com/the-secret-behind-germanys-thriving-mittelstand-businesses-is-all-in-the-mindset-25452) описывает Mittelstand как «enlightened family capitalism» — ownership, control и risk в одних руках устраняет principal-agent разрыв. Работники часто остаются десятилетиями; лояльность двусторонняя — в кризис компании сохраняют кадры через гибкость зарплат (Kurzarbeit), а не массовые увольнения. Это создаёт долгосрочную identity-based культуру.

**IHK (Industrie- und Handelskammer):** Публичная корпорация с обязательным членством всех компаний. Устанавливает квалификационные стандарты, контролирует профессиональное обучение. [IHK структура](https://www.ihk.de/gera/servicemarken/in-english/structures-and-tasks-of-the-chamber-of-commerce-and-industry-325144) — демократическая: члены выбирают совет, совет избирает Präsident и Geschäftsführer. Для Jetix: IHK-сети — важный channel для B2B access к Mittelstand Geschäftsführern.

**VDMA (Verband Deutscher Maschinen- und Anlagenbau):** 3600 членов, немецкий и европейский машиностроительный сектор. Публикует отраслевые стандарты и иерархические norms для Facharbeiter и Meister.

**Betriebsrat и Co-determination:** По закону Betriebsverfassungsgesetz (BetrVG), при от 20 сотрудников обязательно формирование Betriebsrat (производственного совета). Betriebsrat имеет co-determination rights по кадровым вопросам — в частности, должен быть проконсультирован перед увольнением и существенными изменениями рабочих условий. Это значительно замедляет кадровые решения и требует навыков навигации Konsenskultur. Для Jetix-клиентов: понимание Betriebsrat = ключевой cultural competency для delivery команды.

**Ключевое различие Mittelstand vs Tech:** В Mittelstand лестница более steep, смена уровня требует formal qualification (Meisterprüfung через IHK, Studium). В tech уровень определяется demonstrated impact. Mittelstand — tenure-based с merit overlay; tech — merit-based с tenure safety net.

---

## Part C. C-Level: Структура и Phase Transitions

### C1. Полный C-Suite и timing найма

| Роль | Момент найма | KPIs | Reporting |
|------|-------------|------|-----------|
| CEO | Day 1 (founder) / Series B (hired) | Revenue, survival, vision | Board |
| COO | 50–100 сотрудников / $5–10M ARR | Operations efficiency, OKR execution | CEO |
| CFO | $1M ARR (fractional) / $10M (full-time) | Burn rate, cash runway, EBIT | CEO |
| CTO | 10–30 engineers или $2M ARR | Technical debt, velocity, uptime | CEO |
| CMO | $1M ARR (boutique) / $15–20M (full C) | CAC, LTV, brand NPS | CEO |
| CSO | $3–5M ARR / 20–50 sales reps | Quota attainment, pipeline coverage | CEO |
| CPO | $5–15M ARR | Product NPS, retention, feature velocity | CEO |
| CHRO | 100–200 сотрудников | eNPS, retention, time-to-hire | CEO |
| CDO | Зависит от data maturity | Data quality, model performance | CEO/CTO |
| CCO | Series B+ (customer-first companies) | NPS, churn, expansion MRR | CEO |

[SaaStr](https://www.saastr.com/dear-saastr-when-should-a-bootstrapped-startup-hire-a-cfo-coo-cmo/) рекомендует: VP of Everything к $5M ARR, CXO к $15–20M ARR. CFO часто последний из C-suite; CMO нередко первый. При bootstrapping: VPM к $0.2M ARR, VPS к $1–1.5M, VPE к $5–6M.

[StarupConsulting](https://startupconsulting.com/blog/when-to-hire-a-cfo-startup): полноценный CFO появляется между late Series B и mid-Series C (~$10M ARR), когда burn patterns требуют «eight-figure precision». [K38 Consulting](https://k38consulting.com/when-to-hire-a-cfo-for-startup/) указывает: только 9% бизнесов достигают $1M ARR, и именно здесь CFO-экспертиза становится критической.

### C2. Founder Mode vs Manager Mode (Paul Graham, 2024)

В эссе «[Founder Mode](https://paulgraham.com/foundermode.html)» (сентябрь 2024) Paul Graham описывает два принципиально разных способа управления:

**Manager Mode:** CEO взаимодействует только через direct reports. Org chart = чёрные ящики. «Детали — микроменеджмент». Результат: «hire professional fakers and let them drive the company into the ground».

**Founder Mode:** Skip-level meetings — норма, не исключение. Jobs проводил ежегодные retreats для «100 важнейших людей» — не топ-100 по org chart, а тех, кто реально двигает компанию. Прямое вовлечение в детали стратегических проектов через границы иерархии. Founder Mode сложнее, но «works better».

Пример: Brian Chesky (Airbnb) следовал manager mode advice → катастрофа. Изучил Jobs → перестроил → Airbnb стал лидером Silicon Valley по free cash flow margin. Jensen Huang (Nvidia): 60 direct reports, ест в корпоративной столовой — extreme founder mode при огромном масштабе.

Graham: «Мы не знаем точно, что такое Founder Mode. Это будет такой же великой темой для изучения, как manager mode.» Ключевое ограничение: «нельзя управлять компанией из 2000 человек так же, как из 20 — но есть варианты, и Jobs был одним из них».

### C3. Chief of Staff и Fractional C-Level

**Chief of Staff** появляется при 20–50 сотрудниках или когда CEO теряет стратегический фокус из-за операционной перегрузки. По [Voltage Control](https://voltagecontrol.com/articles/the-strategic-value-of-a-chief-of-staff-at-a-startup-key-roles-and-essential-skills/), ключевые функции:
1. Стратегическое планирование и OKR alignment
2. Операционная структура и cadences
3. Управление cross-functional relationships
4. Поддержка CEO в high-stakes decisions (sounding board)
5. Special projects (launches, fundraising prep)

CoS — не ассистент, а «extension of CEO's cognitive bandwidth». В стартапе до Series B часто fractional или временная роль перед hiring COO.

**Fractional C-Level:** Опытный экзекутив работает part-time (0.25–0.5 FTE) за proportional compensation. Актуально при $0.5M–$5M ARR. Fractional CFO, CMO, CTO — зрелая модель в Берлинском startup ecosystem. Для Jetix: fractional Mittelstand-эксперт как первый «CSO» — релевантная модель до €500K ARR.

---

## Part D. Frameworks Decision-Rights

### D1. RACI

Классический матричный инструмент: **R**esponsible (делает), **A**ccountable (несёт ответственность), **C**onsulted (консультирует до), **I**nformed (уведомляется после). Правило: ровно один A на каждое decision. Проблема: RACI описывает workflow, но не уровень иерархии; не отвечает на вопрос «кто может отменить чьё решение».

### D2. DACI / DARE

**DACI** (Driver, Approver, Contributor, Informed) — [Culture Amp](https://www.cultureamp.com/blog/how-daci-supports-employee-engagement), [ProductPlan](https://www.productplan.com/glossary/daci/):
- **Driver** — движет процесс вперёд, координирует, ответственен за deadline
- **Approver** — финальный вотум, один на decision
- **Contributor** — вносит экспертизу, не имеет veto
- **Informed** — уведомляется о результате, не влияет на него

**DARE** — вариант [Management Consulted](https://managementconsulted.com/dare-decision-making-model/): Deciders, Advisors, Recommenders, Executors. Смещает акцент на голосование (Deciders) и разделение advisory от execution.

Оба фреймворка решают ключевую проблему: в консалтинге и стартапах ambiguity вокруг «кто решает» — главный источник политики и bottlenecks.

### D3. Bezos Two-Way / One-Way Doors

В письмах акционерам Amazon (2015–2016) Jeff Bezos описал две категории решений ([Blueprints Guide](https://blueprints.guide/posts/one-way-door-vs-two-way-door)):

- **Type 1 / One-Way Doors:** высокий impact, трудно обратимые. «Once you walk through and don't like what you see, you can't get back.» Требуют «methodically, carefully, slowly, with great deliberation». Примеры: крупное acquisition, выход в новую страну, радикальная platform change.
- **Type 2 / Two-Way Doors:** обратимые, низкий cost of mistake. Move quickly, experiment. Примеры: product feature, A/B test, новый процесс.

Bezos-правило: использовать heavyweight process только для Type 1. Большинство компаний ошибочно применяют его ко всем — отсюда замедление. «70% информации, которую вы хотели бы иметь — достаточно для Type 2. На 90% вы уже опоздали.» AWS, Prime, one-click ordering — всё начиналось как Type 2 эксперименты small teams.

### D4. Andy Grove: High Output Management

Grove ([High Output Management](https://friday.app/p/high-output-management), 1983) формализовал принципы Intel:

- **Manager's output = output своей org + output соседних org под его влиянием** — leverage-thinking
- «Waffling» (откладывание решения) = high negative leverage: «no green light = red light, work stops for a whole organization»
- Decision framework: What decision? When? Who decides? Who consulted? Who ratifies/vetoes? Who informed?
- Meetings как средство принятия решений: Process-oriented (1-1, staff, skip-level) vs Mission-oriented (ad-hoc по конкретному output)
- Принцип: решение принять → all parties give full support, независимо от prior disagreement

### D5. Holacracy: Circles и Domain-Based Decision Rights

Holacracy Constitution v5.0 ([holacracy.org](https://www.holacracy.org/constitution/5-0/)) описывает self-management через:
- **Circles** — контейнеры для ролей с общим Purpose; вложенные иерархически
- **Lead Link** — назначается Super-Circle, отвечает за outcomes Circle без микроменеджмента method
- **Rep Link** — избирается Core Members, представляет Circle наверх, транслирует tensions
- Domain-based authority: «You have authority to take any action or make any decision to enact your Role's Purpose or Accountabilities, as long as you don't break a rule» — boundary-based autonomy

Holacracy хорошо работает для knowledge-intensive, малых команд (20–100), плохо масштабируется без сильных facilitators и высокой organizational literacy.

### D6. Stripe/Collison подход

Patrick Collison не публиковал единого документа о decision rights, но интервью описывают: тщательный первоначальный найм (hire right people, then trust them), сильная письменная культура (документы > встречи), высокая планка качества как proxy для decentralized quality control. Stripe известен тем, что нанимает медленнее конкурентов и платит premium за «the world's most talented people» — что позволяет делегировать большинство decisions на уровень исполнителя.

### D7. Escalation Anti-Patterns и Grove's Waffling

1. **HiPPO escalation** (Highest Paid Person's Opinion): решения, которые должен принимать owner роли, поднимаются CEO — парализует рост
2. **Endless escalation loops:** проблема bouncing между уровнями без resolver
3. **Pseudo-consensus:** «решение принято», но несколько stakeholders продолжают revisit
4. **Silent veto:** Informed party не сигнализирует несогласие, потом саботирует execution
5. **Emergency escalation abuse:** Type 2 решения обрабатываются как Type 1 кризис

**AI-native adaptation:** В системах с AI-агентами accountability за ошибку всегда остаётся у human-approver на ближайшем уровне. Type 2 decisions максимально делегируются агентам, Type 1 требуют human-approver с auditable decision trace.

---

## Part E. Delegation Patterns

### E1. Six Levels of Delegation

[Covey / Meisel / Maxwell](https://foundr.com/articles/leadership/how-to-delegate-effectively) описывают 6 уровней делегации (от наименее к наиболее автономному):

1. **Do exactly as I say** — полный контроль; применять для простых/однозначных задач, не требующих суждения
2. **Look into this, report options, I decide** — research задача; исполнитель собирает данные, суждение остаётся у делегирующего
3. **Look into this, tell me what you intend, wait for yes** — conditional autonomy; исполнитель предлагает, не действует до approval
4. **Look into this, tell me what you intend, do unless I say no** — default-yes autonomy; действие начинается, если нет explicit «нет» в течение window
5. **Take action, let me know what you did** — post-hoc reporting; полная автономия с прозрачностью
6. **Just get it done** — полная делегация, no check-in; для высокодоверенных долгосрочных отношений

Ключевой принцип: делегация — непрерывный спектр, не бинарный выбор. Цель — постепенно двигаться к уровням 5–6 по мере роста доверия через track record.

### E2. Amazon Two-Pizza Teams и Single-Threaded Ownership

Bezos ввёл правило «two-pizza team»: команда не должна быть больше, чем можно накормить двумя пиццами (~6–10 человек). Причина: communication overhead растёт как O(n²). Каждая two-pizza team имеет **single-threaded owner** (STO) — PM + tech + OKR в одном лице, ответственный за весь outcome конца в конец. STO не согласует метод с соседними командами, только outcome. Это организационный аналог Bezos Type 2 door: дать команде bounded autonomy в своём домене.

### E3. Spotify Model: Squads, Tribes, Chapters, Guilds

Henrik Kniberg и Anders Ivarsson (2012) описали [Spotify Scaling Model](https://blog.crisp.se/2012/11/14/henrikkniberg/scaling-agile-at-spotify):

- **Squad** (6–10 человек, cross-functional): autonomous mini-startup, владеет problem space. Product Owner owns outcomes, prioritizes backlog; Engineering Lead guides technical approach (не people manager).
- **Tribe** (40–150, 4–12 squads): общий product area. Tribe Lead как GM: vision, budget, enabling conditions — без micromanaging squads.
- **Chapter** (дисциплина внутри Tribe): Chapter Lead = line manager для discipline members; 50–70% contributor + 30–50% people leadership; создаёт craft standards.
- **Guild** (voluntary, cross-Tribe): community of practice, no delivery commitments. Участие добровольное, любой может войти/выйти.

Ключевое: автономия + alignment через OKR. Squads выбирают Scrum/Kanban самостоятельно, но соблюдают tribe-level guardrails.

### E4. Autonomy-Alignment Matrix (Kniberg)

Kniberg описал матрицу 2x2:
- **Low alignment + Low autonomy** = Micromanagement (anti-pattern)
- **High alignment + Low autonomy** = Command & Control (OK в crisis, bad by default)
- **Low alignment + High autonomy** = Chaos (good intentions, divergent execution)
- **High alignment + High autonomy** = Agility (цель)

«Высокое выравнивание» достигается через shared mission, OKR, стратегические документы — не через ежедневный контроль. Для AI-агентов в Jetix: context в system prompt = alignment mechanism; broad decision rights = autonomy mechanism.

### E5. Auftragstaktik / Mission Command

[Auftragstaktik](https://en.wikipedia.org/wiki/Mission-type_tactics) — прусская военная доктрина XIX века, кристаллизованная фельдмаршалом Хельмутом фон Мольтке. Генерал Otto von Moser первым использовал термин в «Training and Control of the Battalion in Combat» (1906). Генерал Hans von Seeckt (1866–1936) определил как «метод управления и контроля войск, основанный на предоставлении подчинённым свободы действий при выполнении возложенных задач».

**Принцип:** командир даёт **Auftrag** (задание: намерение + цель + ресурсы + ограничения), подчинённый самостоятельно определяет метод. «Intention of the higher commander must be maintained» — не буква приказа. Auftragstaktik не позволяет нарушать приказы, но требует отступления от буквы, если изменившаяся ситуация делала бы исполнение буквы контрпродуктивным.

**Применение в бизнесе:** Amazon (mission + output metric → team autonomy), OKR-фреймворк (What + Why, не How), Spotify squads. Для Jetix: role-manifest с Purpose + Accountabilities + Decision-rights = Auftrag для AI-агента или human executor. Исполнитель выбирает method; контракт — outcome и accountability.

### E6. Micromanagement Anti-Patterns

По Grove и современным исследованиям:
1. **Task intervention** — supervisor перехватывает задачу вместо coaching
2. **Permission bottleneck** — все Type 2 decisions требуют approval
3. **Reporting overload** — frequent status reports без action
4. **Delegation reversal** — задача делегирована, потом отобрана назад
5. **Invisible boundaries** — нет явного контракта, что person может решать самостоятельно

McKinsey data: организации с aligned goals и streamlined communication растут на 25% быстрее. Gallup: 70% вариации team engagement объясняется эффективностью менеджмента.

### E7. Scaled Delegation: 10 → 10,000+ человек

При росте компании делегация должна масштабироваться структурно, не линейно:

**OKR каскад (Grove → Google → мировой стандарт):** Company OKRs → Department → Team → Individual. 60% OKRs формируются bottom-up (genuine alignment), 40% — top-down (strategic priority). Grove: превратить implicit expectations в explicit commitments.

**Written culture как delegation enabler:** Amazon 6-pager memos заменяют PowerPoint — письменное решение = auditable delegation. Для AI-native компаний критически важно: агент должен иметь доступ к written rationale, а не только к outcome.

**Span of control по уровням (McKinsey benchmark):**
- J1–J2 (execution): 1 manager на 8–15 исполнителей (высокий repetition, низкий ambiguity)
- J3 (staff): 1 manager на 5–8 leads
- J4–J5 (principal/strategic): 1 на 3–5 principals
- JX (executive): 1 на 4–8 direct reports (Jensen Huang исключение: 60 direct reports в Nvidia)

---

## Part F. AI и Карьерные Лестницы: Трансформация

### F1. Что AI меняет в junior-работе

**Stack Overflow Developer Survey 2024** ([survey.stackoverflow.co](https://survey.stackoverflow.co/2024/ai)):
- 62% профессиональных разработчиков используют AI-инструменты (vs 44% в 2023)
- 76% используют или планируют использовать
- 72% положительно относятся к AI на работе
- Только 43% доверяют точности AI-инструментов; 45% считают, что AI плохо справляется со сложными задачами
- 12% считают AI угрозой своей работе; 81% называют продуктивность главным benefit

**Brynjolfsson, Li & Raymond (2023, обновлено 2025):** Fortune 500 customer-support deployment — AI conversational tool увеличил продуктивность на **15% в среднем** и на **36% для работников bottom-quintile** ([MIT Sloan](https://mitsloan.mit.edu/centers-initiatives/institute-work-and-employment-research/generative-ai-and-worker-productivity)). Механизм: AI распространяет tacit organizational knowledge топ-исполнителей на всех, «delivering real-time coaching at scale». Attrition у новых агентов снизился на ~40%.

**Noy & Zhang (2023):** ChatGPT снижает время writing tasks на ~40%, повышает качество на 18%; эффект максимален у initially lower-performing workers.

**ICLE обзор** ([laweconcenter.org](https://laweconcenter.org/resources/ai-productivity-and-labor-markets-a-review-of-the-empirical-evidence/)): «AI может автоматизировать дискретные задачи, традиционно служившие entry-level работой, снижая предельный спрос на junior labor без вытеснения senior workers». Вывод: структурное изменение career ladders, а не broad job loss.

**AI компрессирует skill differential:** junior workers с AI → производительность как mid-level без AI. Это структурно меняет ценность entry-level позиций и вопрос «зачем нанимать junior».

### F2. Что остаётся человеческим

**McKinsey State of AI 2025** ([mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)):
- 88% организаций регулярно используют AI хотя бы в одной функции
- 32% ожидают сокращения workforce в следующем году; 43% — без изменений; 13% — рост
- Только 6% высокоэффективных компаний видят EBIT impact 5%+
- Ключ успеха: redesigning workflows, не просто adoption

**McKinsey AI in Workplace 2025** ([mckinsey.com](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work)): сотрудники в 3 раза более готовы к AI, чем лидеры думают; 47% employees считают, что будут использовать AI более чем для 30% daily tasks в ближайший год (vs только 4% ожиданий C-suite).

**Что AI не заменяет (горизонт 2025–2027):**
- Клиентские отношения с высокими stakes — trust-based, reputation-dependent
- Стратегические решения с incomplete information и political context
- Культурное изменение организации
- Legal accountability и compliance responsibility
- Межличностные конфликты и negotiation с adversarial parties
- Creative briefs + final positioning judgment
- Mittelstand Geschäftsführer-to-Geschäftsführer relationship building (особенно релевантно для Jetix)

### F3. AI-Native Companies: Новые паттерны

**Anthropic (1097 сотрудников, 2025):**
Все technical staff — единый титул «Member of Technical Staff (MTS)» ([LinkedIn analysis](https://www.linkedin.com/posts/johnkim5480931a8_every-technical-employee-at-anthropic-shares-activity-7275943947439415296-qh5w)): защита от headhunting, размытие research/engineering разрыва, культура «engineers do research, researchers do engineering». 4 research teams: Interpretability, Alignment, Societal Impacts, Frontier Red Team. Рост с 300 до 950 за год (2023–2024), намеренно замедлили. Dario Amodei: «Talent density beats talent mass» ([Contrary Research](https://research.contrary.com/company/anthropic)). Первый CFO, CPO, CCO — наняты в 2024–2025. В 2026: Mike Krieger перешёл от CPO к Anthropic Labs, заменён Ami Vora.

**Cursor (Anysphere):**
$100M ARR за 12 месяцев с командой 30 человек; ~300 человек при $10B valuation ([LinkedIn](https://www.linkedin.com/posts/suman-siva-64b0712b_cursor-grew-to-100m-in-revenue-in-12-months-activity-7377053238346395649-nAYh)). CEO Michael Truell: «мы всё ещё интервьюируем без AI для первых технических screening» ([Business Insider](https://www.businessinsider.com/cursor-interview-process-no-ai-on-site-project-coding-tool-2025-6)). Hiring через 2-day onsite: кандидаты строят real project с командой. Найм: «intellectual curiosity and experimentation» + «bottom-up experimentation culture».

**Lovable (Sweden):**
$10M ARR за 60 дней с командой 15 человек ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/building-lovable-anton-osika)). К марту 2026 — 146 человек, план: 400 к концу года ([Business Insider](https://www.businessinsider.com/lovable-hiring-strategy-founder-dna-structure-vibe-coding-2026-3)). Hiring philosophy: «founder DNA» — ownership, speed, autonomy. «Если человек хочет высокоструктурированную, низко-ambiguous среду — Lovable не для него». Ожидание meaningful work от Day 1. 30% найма через referrals.

**DeepSeek (Hangzhou, ~200 сотрудников, 2025):**
Обучили V3 за 2 месяца <$6M (vs $100M+ GPT-4). Нанимают преимущественно fresh graduates; намеренно избегают тех, у кого 8+ лет experience. Lean структура, чистый research focus ([ElectroIQ](https://electroiq.com/stats/how-many-employees-does-deepseek-ai-have/)). Точных данных о внутренней иерархии публично нет; по доступным интервью — flat structure с founder-as-chief-researcher.

**AI-Native паттерны 2024–2025 (Fortune analysis):**
- ~50% headcount в engineering (vs 30–35% в традиционном tech)
- ~13% больше senior IC, ~16% меньше junior employees
- Leaner back-office, сжатие corporate functions
- 50–100 AI агентов управляются 2–3 людьми ([Fortune](https://fortune.com/2025/08/07/ai-corporate-org-chart-workplace-agents-flattening/))
- Healthcare example: 10-person dev team → 3-person (product owner + AI engineer + systems architect)

### F4. Трансформация карьерных путей

**«Senior» в AI-эпоху:** Senior статус больше не определяется скоростью кодирования — его определяет способность задавать правильные вопросы, оценивать AI output, принимать architectural decisions с учётом AI constraints, и управлять AI-командой.

**AI Teammate vs AI Tool:**
- **Tool:** детерминированный, scope ограничен конкретной задачей (Copilot autocomplete, ChatGPT для draft)
- **Teammate:** имеет context, memory, goals; выполняет multi-step работу автономно; требует management, не только prompting; несёт «quasi-accountability» за своё поведение

Ключевой сдвиг для карьерных лестниц: **orchestration skill** становится leveling signal — способность управлять командой AI-агентов, задавать им правильные ограничения, оценивать их output на соответствие intent.

---

## Part G. Практические Рекомендации для Jetix

*Самая важная часть: ~2500 слов.*

### G1. Jetix Career Ladder: Финальная Структура

Jetix работает в уникальной парадигме: Role ≠ Executor. Один role-manifest исполняется Claude-агентом сегодня, junior-human завтра, senior-human послезавтра. Поэтому ladder описывает **роль по scope и decision-rights**, не человека или агента.

**Предложенная лестница: 6 уровней + Executive**

| Уровень | Jetix-название | Scope | Decision-rights | Horizon | Аналог |
|---------|---------------|-------|----------------|---------|-------|
| J0 | **Executor** | Чётко определённая задача, один workflow | Execute only — нет выбора метода | <1 день | Amazon SDE I / BA intern |
| J1 | **Specialist (Junior)** | Компонент, функция | Метод выполнения в границах задачи | 1–7 дней | Meta E3 / McKinsey BA |
| J2 | **Senior Specialist** | Feature, workflow, client deliverable | Technical approach + minor process decisions | 1–4 недели | Meta E5 / McKinsey Associate |
| J3 | **Lead (Staff)** | Домен, несколько ролей | Domain-level architecture, hire/fire recommendation, process design | 1–3 месяца | Meta E6 / McKinsey EM |
| J4 | **Principal** | Бизнес-функция, cross-domain | Business decisions в функции, OKR setting, client strategy | 3–12 месяцев | Meta E7 / McKinsey AP |
| J5 | **Strategic** | Вся компания / portfolio | Company-level strategy, C-suite decisions с Ruslan | 1–3 года | Meta E8 / McKinsey Partner |
| JX | **Executive (C-level)** | Компания + экосистема | Irreversible decisions (M&A, market exit, funding) | 3–10 лет | McKinsey Senior Partner / CTO |

**Mapping текущих 12 ролей на лестницу:**

| Текущая роль | Уровень | Примечание |
|-------------|---------|-----------|
| inbox-processor | J1 | Pure execution, чётко bounded |
| personal-assistant | J1 | Task-scoped, follow instructions |
| sales-research | J1 | Bounded research scope |
| sales-outreach | J1–J2 | Has sequencing decisions |
| system-admin | J2 | Technical method autonomy |
| delivery | J2 | Client deliverable ownership |
| analyst | J2–J3 | Insight recommendations = quasi-decision |
| knowledge-synth | J2–J3 | Synthesis requires cross-domain judgment |
| life-coach | J2 | Scoped in Life-OS, не Jetix |
| sales-lead | J3 | Owns pipeline domain |
| meta-agent | J3 | Cross-cutting QA authority |
| crazy-agent | J3 (hackathon mode) | Full autonomy в bounded sandbox |
| manager | J3–J4 | Operations + deal-level authority |
| strategist | J4 | Method + strategy doc authority |
| strategic-management (Ruslan) | J5 + JX | Founder = both |

### G2. Role-Manifest Format

Минимально жизнеспособный role-manifest для Jetix:

```yaml
# JETIX ROLE MANIFEST v1.0
id: "sales-lead"
level: "J3"
domain: "sales"
version: "1.2"

purpose: |
  Генерирует и закрывает pipeline немецкого Mittelstand клиентов.
  Достигает revenue targets в Q-горизонте.

accountabilities:
  - "Ведёт pipeline от qualified lead до signed contract"
  - "Отбирает и квалифицирует ICPs на входе"
  - "Делегирует research-tasks sales-research (J1) агентам"
  - "Репортит win/loss metrics в manager еженедельно"

decision_rights:
  can_decide:
    - "Квалификация/дисквалификация лида"
    - "Выбор outreach тактики"
    - "Скидка до 10% без апрувала"
    - "Scheduling client meetings"
  must_escalate:
    - "Скидка >10%"
    - "Нестандартный contract term"
    - "Работа с клиентом не из ICP"
    - "Цена ниже floor-rate"
  informs:
    - "Все закрытые сделки → manager"
    - "Все потерянные deals с win/loss reason → strategist"

kpis:
  - "Qualified leads / month: ≥8"
  - "Pipeline value: ≥€150K active"
  - "Close rate: ≥20%"

executors_compatible: ["human-sales", "claude-agent"]
reports_to: "manager (J3-J4)"
supervises: ["sales-research (J1)", "sales-outreach (J1)"]
budget_authority_eur: 5000

time_in_role: "6-18 months before J4 promotion review"
promotion_signals:
  - "Consistent target overachievement 2+ quarters"
  - "Managed J1-agents without escalations"
  - "Proposed process improvement adopted"
```

**Минимальные обязательные поля (Minimum Viable Manifest):**
`id`, `level`, `purpose`, `accountabilities`, `decision_rights` (can_decide + must_escalate), `reports_to`

**Optional поля:** stakeholder_map, context_window_requirements, memory_type (ephemeral/persistent), tool_access, budget_authority_€, kpis, time_in_role, promotion_signals.

**Философия формата:** Role-manifest — контракт между системой и любым executor (AI или human). Аналог Auftragstaktik-Auftrag: чёткий Purpose и Accountabilities = intent; Decision-rights = свобода выбора метода в границах.

### G3. Decision-Rights Matrix

| Decision Type | J1 | J2 | J3 Lead | J4 Principal | J5 Strategic | JX |
|--------------|----|----|---------|-------------|-------------|-----|
| Accept new client (ICP) | ❌ | ❌ | Рекомендует | ✅ | ✅ | ✅ |
| Accept non-ICP client | ❌ | ❌ | ❌ | Рекомендует | ✅ | ✅ |
| Fire/reject client | ❌ | ❌ | Рекомендует | ✅ (<€10K) | ✅ любой | ✅ |
| Discount до 5% | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Discount 5–10% | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Discount 10–20% | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Discount >20% / change floor | ❌ | ❌ | ❌ | ❌ | Рекомендует | ✅ |
| Launch new SKU/product | ❌ | ❌ | ❌ | Рекомендует | ✅ | ✅ |
| Hire J1 (agent or human) | ❌ | Рекомендует | ✅ | ✅ | ✅ | ✅ |
| Hire J3+ (human) | ❌ | ❌ | Рекомендует | ✅ с Ruslan | ✅ | ✅ |
| Fire human employee | ❌ | ❌ | ❌ | Рекомендует | С Ruslan | ✅ |
| Enter new market/geography | ❌ | ❌ | ❌ | ❌ | Рекомендует | ✅ |
| Fundraising / M&A | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Ruslan только |

**Принципы матрицы:**
- Скорость: J1–J2 решения занимают минуты, J4–J5 — часы/дни, JX — дни/недели
- Reversibility: Type 2 (обратимые) делегируются максимально низко по лестнице
- One Approver: ровно один ✅ на каждое decision (DACI principle)
- Escalation threshold: если decision в «Рекомендует» — Recommender должен предоставить written recommendation с pros/cons перед Approver decision

### G4. Phase Transitions Roadmap

**Phase 0: Сейчас → Q2 2026 (Solo + 12 AI-агентов)**
- Ruslan исполняет J5+JX
- 12 агентов: J1–J4 роли
- Метрика: первые €50K revenue
- Trigger следующей фазы: revenue > €30K/месяц стабильно 2 месяца ИЛИ Ruslan теряет >30% времени на J2-операции (opportunity cost сигнал)

**Первый human hire:**
- **Роль:** Sales Lead (J3) — первый, потому что pipeline немецкого Mittelstand требует human trust. Mittelstand Geschäftsführer ожидают Geschäftsführer-to-Geschäftsführer отношения; AI-агент не может это заменить на первом встрече
- **Профиль:** Erfahrener Mittelstand-Berater или Sales-Exec с IHK/VDMA-сетью, понимание Konsenskultur, немецкий native
- **Метрика-триггер:** Pipeline outbound > 50 leads/month, конверсия падает из-за отсутствия human credibility / trust barrier
- **Тип:** Fractional или part-time сначала (0.5 FTE) — типичная практика для берлинских стартапов
- **Время при оптимистичном сценарии:** ~$20–30K MRR / Q3 2026

**Первый C-level:**
- **Роль:** Fractional CFO (JX) — при достижении €1M ARR или Series A contemplation
- **Почему CFO первый:** Немецкий B2B рынок требует прозрачной финансовой отчётности; IHK-среда ожидает Jahresabschluss; fundraising из Германии требует Jahresabschluss + прогноза
- **Метрика-триггер:** Monthly burn > €50K, ARR > €500K, investors asking for financial projections
- **Тип:** Fractional CFO (Berlin Ecosystem) — 0.25–0.5 FTE, €3–5K/месяц

**Chief of Staff vs COO:**
- **CoS первый (~30–50 человек / €1–2M ARR):** Ruslan теряет strategic focus из-за coordination overhead. CoS handles: OKR cadences, board prep, cross-functional coordination, special projects
- **COO только после:** реальное operations separation (production + delivery масштабируется отдельно от стратегии). Не делать COO-mistake Chesky — это был manager-mode trap

**Split Ruslan's strategic-management role:**
- **Когда:** 20–30 human employees, ARR > €2M, два отчётливых продукта или сегмента
- **На что:** (1) CEO/MD-Ruslan (JX) — external: fundraising, vision, key clients, IHK/ecosystem; (2) COO/General Manager (J5) — internal: operations, delivery, team scaling
- **Модель:** Jobs (vision) + Cook (operations) — при сохранении Founder Mode у Ruslan
- **Опасность:** Не превращаться в «manager mode» CEO. Ruslan сохраняет право skip-level meetings и прямого доступа к любому уровню

**Divisions (по каким критериям):**
- **Trigger:** >100 employees ИЛИ >3 revenue streams >€1M каждый ИЛИ geographical expansion DACH → EU
- **Критерии деления:** Product/service type × Customer segment (Mittelstand 50–200 vs 200–500) × Geography (DACH vs EU)
- **Структура Division:** каждый Division имеет свой P&L, свой Bereichsleiter-analog (J4), reporting в Jetix HoldCo (JX)
- **Аналогия:** Fraunhofer-Gesellschaft — немецкая федерация исследовательских институтов, каждый с автономным P&L под единым зонтиком

### G5. Escalation Protocol Jetix

```
ОБЯЗАТЕЛЬНАЯ ЭСКАЛАЦИЯ (trigger немедленно):
  - Client угрожает churn или юридическими действиями
  - Любой financial commitment >budget_authority роли
  - Security/data breach, любая утечка клиентских данных
  - Новый прямой конкурент в core Mittelstand сегменте с агрессивным pricing
  - Team conflict, который невозможно разрешить за 48 часов
  - Обнаружена ошибка в deliverable, уже переданном клиенту

ESCALATION PATH:
  J1–J2 → J3 Lead (manager) → J4 Principal → J5 Strategic (Ruslan)
  
  Время реакции по уровням:
    J3: ответ в течение 4 часов
    J4: ответ в течение 24 часов  
    J5/Ruslan: ответ в течение 48 часов

ФОРМАТ ЭСКАЛАЦИИ (обязательный):
  1. Ситуация (2-3 предложения)
  2. Мои рекомендации с pros/cons (если есть)
  3. Что я уже сделал/не сделал
  4. Что мне нужно от вас: решение / совет / информация

ANTI-PATTERNS — НИКОГДА:
  ❌ Эскалировать Type 2 decision без своей рекомендации
  ❌ Bypass level (J1 напрямую к J5 без попытки решить с J3)
  ❌ Эскалировать постфактум ("мы уже сделали X")
  ❌ Infinite loop (две роли bouncing проблему 48+ часов)
  ❌ Эскалировать ambiguity без попытки clarify самостоятельно
```

### G6. Human-AI Boundary

**«Точно человек» (не делегируется AI в 2025–2027 горизонте):**
- Первые встречи с Mittelstand Geschäftsführer — первичный trust-building
- Подпись контрактов, юридическая accountability
- Увольнение / difficult conversations с сотрудниками (особенно в немецком праве с Betriebsrat)
- Публичное представительство (IHK-мероприятия, VDMA, конференции)
- Financial decisions >J4 threshold
- Кризисное управление с внешними stakeholders

**«Точно AI» (полная делегация уже сейчас):**
- inbox-processor: email triage, labeling, first-response draft
- sales-research: company lookup, firmographic data, ICP qualification check
- knowledge-synth: cross-document synthesis, summarization
- system-admin: routine monitoring, alert triaging
- Первичный анализ данных, report generation, slide assembly

**«Зависит» (human override required при определённых условиях):**
- sales-outreach: AI пишет письмо, human review при >€50K deal size или non-ICP клиенте
- delivery: AI создаёт deliverable, human review при стратегическом клиенте или новом типе проекта
- analyst: AI анализирует данные, human validates business interpretation перед презентацией клиенту
- meta-agent: AI проводит QA, human подписывает при юридических implications

**Как граница смещается с новыми моделями:**
- Claude Opus 5 / аналоги 2026–2027: граница «зависит» сдвигается к «точно AI» по мере роста context reasoning и track record
- Trust formula: track record + explainability + reversibility = delegation authority
- Правило Jetix: «Does this executor understand WHY this matters culturally to the German Mittelstand client?» — если нет, human override.
- Мониторинг: ежеквартальная ревизия Human-AI boundary sheet на основе actual errors, near-misses и model capability updates

### G7. Promotion Signals по уровням

Повышение в Jetix-лестнице — не tenure-based, а scope-based: «promoted in a job, not into a job» (Amazon principle). Роль должна выполняться на следующем уровне стабильно прежде, чем получить формальный апгрейд.

**J1 → J2 (Specialist → Senior Specialist):**
- Выполняет задачи без clarification-запросов >80% времени
- Предлагает альтернативные подходы к выполнению, не только исполняет
- Выявляет пограничные случаи, которые не были явно описаны в задаче
- Self-reviews свою работу перед submission, нулевые obvious errors
- Trigger: 3+ consecutive delivery cycles на J1 с «exceeds» rating

**J2 → J3 (Senior → Lead/Staff):**
- Управляет workflow нескольких J1-агентов без микроменеджмента
- Принимает domain-level технические/процессные решения самостоятельно
- Инициирует улучшения процесса, не только реагирует на задачи
- Delivers клиентский outcome, а не только технический output
- Trigger: 2+ quarters consistent domain ownership + один крупный проект без escalations

**J2 → J3 для AI-агентов:** расширение decision_rights в role-manifest Ruslan'ом после 90-дневного track record с <2% escalation rate и zero false-positive critical decisions.

**J3 → J4 (Lead → Principal):**
- Работает cross-domain, не только в своём домене
- Способен определить OKR для своей функции на квартал
- Revenue contribution или clear cost savings attributable к роли
- Первый hiring recommendation принят (для human track)
- Trigger: Business-level impact (€ или % metrics), не только operational excellence

**J4 → J5 (Principal → Strategic):**
- Принимает irreversible J4-level decisions самостоятельно
- Строит roadmap бизнес-функции на год
- Привлекает revenue или partnerships через thought leadership / network
- Идентифицирует стратегические risks раньше, чем они становятся crisis
- Trigger: Ruslan делегирует whole domain без check-in 1+ месяц; peer J4s обращаются за советом

**Anti-patterns при promotion:**
- ❌ Promotion как compensation fix — дайте больше денег, а не уровень
- ❌ Promotion за tenure без demonstrated next-level scope
- ❌ Title inflation в первые 6 месяцев до оценки real impact
- ❌ Downgrade без explicit conversation — разрушает trust

### G8. 10-Year View: Jetix Org 2035

Гипотетическая структура при успешном росте:

```
JX: Jetix Executive Board
    ├── CEO/Founder (Ruslan или successor)
    ├── CFO
    ├── CTO (AI Infrastructure & Platform)
    └── CCO (Chief Client Officer — Mittelstand relations)

J5 Strategic Level (~10 roles):
    ├── Head of Mittelstand 50-200 (Division 1 GM)
    ├── Head of Mittelstand 200-500 (Division 2 GM)
    ├── Head of Platform/SaaS
    ├── Head of AI Research & Products
    ├── Chief of Staff
    └── Head of Ecosystem (IHK, VDMA partnerships)

J4 Principal Level (~20–30 roles):
    ├── Principal Consultants per industry vertical
    ├── Principal Engineers per product domain
    └── Principal Analysts per market segment

J3 Staff Level (~50–80 roles):
    ├── Engagement Leads (human, Mittelstand-facing)
    ├── Team Leads per squad
    └── AI Orchestration Leads

J1–J2 Level:
    ├── ~200–300 humans (sales, delivery, engineering)
    └── ~1000–2000 AI agents (various roles)

Ratio: ~400 humans : 2000 AI agents (5:1 AI-to-human)
Revenue target 2035: €50–200M ARR
```

**Ключевые структурные принципы к 2035:**
1. **Role-manifest как единый интерфейс** — люди и агенты взаимозаменяемы в J1–J3
2. **Mittelstand-first culture** — немецкая Konsenskultur интегрирована в operating principles; немецкий язык как first language для клиентской команды
3. **Auftragstaktik** — каждый J3+ получает Auftrag (mission + intent + resources), метод выбирает сам
4. **Two-way doors everywhere** — максимальный push-down decision-rights, JX занимается только Type 1
5. **Founder Mode preserved** — Ruslan или преемник сохраняет skip-level access, не превращается в «manager mode» CEO

---

## Заключение

Академический обзор трёх систем — software ladders (IC/management dual track), consulting ladders (MBB up-or-out, German Mittelstand Konsenskultur) и executive structures (C-suite timing, Founder Mode) — выявляет **конвергирующий принцип**: лестница работает, когда scope каждого уровня явно определён, decision-rights прозрачны, а escalation paths — исключением, а не правилом.

Для Jetix этот принцип особенно важен в AI-native контексте: role-manifest становится **контрактом между системой и любым executor** — Auftrag в понимании фон Мольтке. Давай intent и resources, доверяй методу. Граница между человеком и AI определяется не техническими возможностями, а культурными требованиями клиента (Mittelstand Konsenskultur), юридической accountability и reversibility решений.

AI-трансформация карьерных лестниц (Part F) указывает на сжатие skill premium у junior-уровней и рост premium у тех, кто **orchestrates AI** — принимает staked decisions, строит доверие с клиентами, несёт accountability. В Jetix-лестнице J1–J2 будут всё больше исполняться агентами, а Human-by-design остаются J4–JX и клиентский front.

**На основе этого отчёта можно написать:**
- `JETIX-CAREER-LEVELS.md` — таблица G1 + описание каждого уровня
- `role-manifest-template.yaml` — шаблон G2
- `decision-rights-matrix.md` — таблица G3
- `phase-transitions.md` — роадмап G4 с метриками-триггерами
- `human-ai-boundary.md` — guidelines G5 + G6 с quarterly review cadence

---

*Все inline citations основаны на реальных источниках из research sessions. Uncertain данные (точная внутренняя иерархия Cursor, DeepSeek) отмечены явно. Цифры Levels.fyi и McKinsey — актуальны на дату публикации (2024–2026).*
