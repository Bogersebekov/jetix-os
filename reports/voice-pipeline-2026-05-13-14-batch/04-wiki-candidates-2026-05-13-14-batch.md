---
title: Wiki Candidates v2 — 3-tier categorized — 2026-05-14
type: pipeline-output-candidates
policy: NEVER auto-merge to wiki/ — Ruslan bulk-acks per tier via /wiki-bulk-ack
created: 2026-05-14T00:37:23
lens: voice-pipeline-2026-05-13-14-batch
total_candidates: 94
tier_a_count: 10
tier_b_count: 49
tier_c_count: 35
skipped_count: 31
match_rate: 0.6277
threshold_high: 0.85
threshold_medium: 0.6
---

# Wiki Candidates v2 — 3-tier categorized

> ⚠️ All entries below are **proposals only**. wiki/ untouched. Ruslan bulk-acks per tier via /wiki-bulk-ack — third gate.

**Total:** 94 | **Tier A** (≥0.85): 10 | **Tier B** (0.6–0.85): 49 | **Tier C** (<0.6): 35 | **Skipped:** 31 | **Match rate (A+B):** 62.8%

**Sidecar:** `04-wiki-candidates-v2.json` (machine-readable for /wiki-bulk-ack)

---

# §A — Tier A: High-confidence match-to-existing

> **10 items** with score ≥ 0.85.
> Approval = create cross-reference edge in wiki/graph/edges.jsonl + log entry. Existing wiki entry **NOT modified**.
>
> **Bulk-ack command:** `/wiki-bulk-ack --tier A` (preview with `--dry-run` first)

| # | Voice item (preview) | → Wiki entry | Score | Rationale | Memo refs |
|---|---|---|---|---|---|
| 1 | Когда за плечами есть инструменты, опыт и уверенность в результате — возникает н | `concepts/engineering-faith.md` | 0.88 | Engineering faith = неподдельная вера в результат от наличия |  |
| 2 | Сначала фундамент, обучение и настройка системы — потом реализация амбиций и акт | `ideas/system-first-myth-second.md` | 0.88 | «Система/движок первична — потом играть» = «сначала фундамен |  |
| 3 | Сначала зафиксировать и проработать мощный майнсет глобального масштаба, и тольк | `ideas/money-value-mindset-pre-launch.md` | 0.87 | Оба: проработать установки о ценности/деньгах ДО запуска про |  |
| 4 | Если зафиксировать майнсет глобального масштаба до выхода на продажи — уровень к | `ideas/masshtab-resheniy-opredelyaet-masshtab-zhizni-osoznanno.md` | 0.87 | Both: scale of mindset/decisions directly determines scale o |  |
| 5 | Уверенность и знание — не слепая вера. Заходить в переговоры только с уже зафикс | `concepts/engineering-faith.md` | 0.90 | Exact match: confidence grounded in plan+tools ≠ blind faith |  |
| 6 | Jetix в мировом масштабе: автоматизированный аутрич, воронки, онбординг настроен | `ideas/scaling-plan-self-clients-team-worldwide.md` | 0.85 | Both: Jetix worldwide scale with team, automation, funnels g |  |
| 7 | Добавить к мастерским жилые пространства и питание — создать полноценную среду о | `ideas/vork-khata-vork-selo-idealnoe-rabochee-okruzhenie.md` | 0.88 | «Ворк-хата → Ворк-село» с инфраструктурой (спорт, питание, о |  |
| 8 | Jetix как система ответственного подхода к жизни — сначала метод взаимодействия  | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.85 | Модель влияния мирового масштаба через локальных распростран |  |
| 9 | Последовательный захват аудиторий по единому шаблону (один блогер/индустрия → сл | `ideas/metod-posledovatelnogo-fokusa-v-biznese.md` | 0.85 | Оба о последовательном фокусе: не распыляться, брать одну те |  |
| 10 | Jetix создаёт универсальную 'дорогу' — единые правила управления сложными систем | `ideas/jetix-as-infrastructure-metaphor.md` | 0.87 | Метафора 'дорога + машины' совпадает напрямую: Jetix как уни |  |

---

# §B — Tier B: Medium-confidence match-to-existing

> **49 items** with score 0.6–0.85. Match plausible but not certain.
> Ruslan reviews + acks subset.
>
> **Bulk-ack command:** `/wiki-bulk-ack --tier B --select 1,3,5,7-10` (subset)

| # | Voice item (preview) | → Wiki entry | Score | Rationale | Memo refs |
|---|---|---|---|---|---|
| 1 | Чувствует огромный подъём и гордость за накопленные наработки — количество докум | `concepts/engineering-faith.md` | 0.68 | Engineering faith = обоснованная уверенность от наличия план |  |
| 2 | Идея развития Jetix до мирового уровня оформилась лаконично и воспринимается как | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.70 | Мировой масштаб Jetix с владельцем как идейным вдохновителем |  |
| 3 | При продажах обязательно транслировать состояние уверенности — оно неподдельное  | `ideas/beast-mode-formula-actions.md` | 0.60 | Формула пикового состояния близка к «транслировать состояние |  |
| 4 | В одиночку систему дальше стратегически не описать и не развить — для этого нужн | `ideas/focus-theory-5-people-ai-1-task.md` | 0.72 | Команда 5 экспертов >> одиночка; совпадает с «в одиночку сис |  |
| 5 | Как научиться «тянуть систему» до нужного уровня самостоятельно, прежде чем пере | `ideas/metod-posledovatelnogo-fokusa-v-biznese.md` | 0.65 | Разбирать тему до нужной кондиции прежде чем двигаться дальш |  |
| 6 | Приоритет на ближайший период — сначала подтянуть систему и настроить стратегию  | `sources/2026-04-16-scaling-plan-self-clients-team-worldwide.md` | 0.70 | Последовательность: сначала настроить систему и агентов, пот |  |
| 7 | Накоплено достаточно наработок, идей и материалов — ощущение готовности идти к л | `ideas/youtube-kak-kanal-dlya-translyatsii-idey-stabilno-paru.md` | 0.60 | Накопленные идеи и инсайты стоит доносить до людей — слабо с |  |
| 8 | Две стратегические сессии с ключевыми людьми (Царь + Левенчук) дадут ясность по  | `sources/2026-04-16-virtual-c-suite-expert-calibration.md` | 0.72 | Оба о 1-2 живых сессиях с экспертами для калибровки стратеги |  |
| 9 | Продвижение Jetix на мировой уровень — глобальная амбиция подтверждена как ориен | `ideas/scaling-plan-self-clients-team-worldwide.md` | 0.70 | Глобальный уровень как конечный ориентир + текущие шаги (Jet |  |
| 10 | Jetix строится как компания вселенского масштаба — десятки специалистов, работаю | `ideas/200-year-vision-jetix-humanity.md` | 0.72 | Оба о Jetix как организации вселенского/трансформационного м |  |
| 11 | Собственная школа реальных профессионалов, предоставляющих услуги и владеющих пр | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.80 | «Клан и школа — система подготовки людей, доказавших компете |  |
| 12 | Создать собственную школу реальных профессионалов, которые будут предоставлять у | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.82 | Школа для подготовки профессионалов с доказанной компетентно |  |
| 13 | Не размениваться на мелочи — Jetix занимается глобальными вещами и воплощает гло | `ideas/global-vision-system-of-future.md` | 0.63 | Both about Jetix operating at global/planetary scale, but wi |  |
| 14 | Аналогия мытья рук: один человек начал мыть руки перед операциями → смертность у | `sources/2026-04-16-merchants-analogy-jetix-unifies-via-ai.md` | 0.62 | Both use historical analogy for Jetix's global spread potent |  |
| 15 | С правильными автоматизациями (аутрич, воронки, онбординг) Jetix можно масштабир | `ideas/scaling-plan-self-clients-team-worldwide.md` | 0.75 | Wiki описывает пошаговый план масштабирования до worldwide ч |  |
| 16 | Сходить на 100 конкретных тематических подкастов для распространения Jetix-метод | `ideas/blog-kak-instrument-netvorkinga-i-rosta.md` | 0.62 | Оба — о медиаприсутствии для личного бренда и нетворкинга, н |  |
| 17 | Нанять людей (фрилансеры/студенты) для нарезки видеоконтента из длинных материал | `ideas/ai-kontent-mashina-youtube-tiktok-na-avtopilote.md` | 0.75 | Та же идея: нарезка длинного контента → дистрибуция в соцсет |  |
| 18 | Нанять психологов для дальнейшей проработки и научного обоснования Jetix-системы | `concepts/ai-proektirovanie-psy-led.md` | 0.80 | Оба о роли психологов в проектировании AI/Jetix-системы; wik |  |
| 19 | Создать бесплатную и платную версию Jetix-системы/инструкции: бесплатный вход сн | `ideas/tools-feedback-community-flywheel.md` | 0.82 | Wiki описывает ту же freemium-модель: низкий барьер входа (б |  |
| 20 | Jetix-система = привычка уровня мытья рук: управлять тем, что в тебя попадает, ч | `ideas/weekly-analysis-rest-as-life-maintenance.md` | 0.68 | Оба о регулярном обслуживании системы жизни как обязательной |  |
| 21 | Сколько людей потенциально увидят, попробуют и заинтересуются Jetix-системой? Ка | `ideas/sistema-udlineniya-idey-ot-zamysla-k-realistichnnoy-mode.md` | 0.63 | Оба о расчёте реалистичного потенциала идеи/системы: охват,  |  |
| 22 | Jetix станет настолько профессиональной и мощной командой с интеллектуальными ра | `ideas/jetix-corporation-1000-pros-100k-agents.md` | 0.80 | North Star Jetix Corporation с мировым масштабом и офисами в |  |
| 23 | Jetix создаст новую (модифицированную) структуру экономики и общества с разными  | `ideas/ekonomika-vladeltsev-k-2035-chelovek-bez-aktivov-novyy-bednyy.md` | 0.61 | Оба о новой структуре экономики будущего, хотя голос акценти |  |
| 24 | Уровень амбиций Jetix — ни капли меньше, ни сантиметра ниже: мировой масштаб, ра | `ideas/jetix-corporation-1000-pros-100k-agents.md` | 0.78 | North Star vision (мировой масштаб, страны, миллиардная капи |  |
| 25 | При правильном накоплении интеллектуальных разработок и технологий управления ст | `sources/2026-04-16-jetix-corporation-1000-pros-100k-agents.md` | 0.70 | Источник о Jetix Corporation с офисами по всем странам — бли |  |
| 26 | Разработать концепцию модульной социально-экономической структуры с разными верс | `ideas/vork-khata-vork-selo-idealnoe-rabochee-okruzhenie.md` | 0.62 | Оба о создании осознанно выбранного рабочего окружения с кол |  |
| 27 | Мировая сеть мастерских как метро: множество станций и ответвлений, люди свободн | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.61 | Оба — о глобальном распространении через локальных участнико |  |
| 28 | Мастерские + жильё + питание = полностью упакованная экосистема, максимально удо | `ideas/ekosistema-proizvodstva-osoznannykh-lyudey-5-komponento.md` | 0.65 | 5-компонентная экосистема (онлайн+офлайн+сообщество) перекры |  |
| 29 | Открытые пространства с свободным перемещением между мастерскими/идеологиями — п | `ideas/jetix-open-source-philosophy.md` | 0.82 | Оба: открытость как ключевой дифференциатор Jetix vs закрыты |  |
| 30 | Бизнес-модель Jetix проникает в другие бизнесы как вирус: прокачивает их через м | `sources/2026-04-16-self-improving-system-inevitable-dominance.md` | 0.67 | Wiki: «систематически взламывает и улучшает другие системы ( |  |
| 31 | Мастерские способствуют синергии и созданию новых проектов/изобретений — это R&D | `ideas/github-for-business-projects.md` | 0.62 | Совместная работа над проектами внутри Jetix-экосистемы близ |  |
| 32 | Подход распространяется по миру через взаимовыгодное сотрудничество — по чуть-чу | `ideas/tools-feedback-community-flywheel.md` | 0.65 | Flywheel «помощь инструментами → community» — взаимовыгодный |  |
| 33 | Разные уровни команд, кланов, сообществ внутри экосистемы мастерских — тестирова | `ideas/dynamic-teams-by-topic-level.md` | 0.62 | «AI подсказывает, кого соединить по теме и уровню» ≈ разные  |  |
| 34 | Строить в правильном порядке: сначала себя → потом клан → потом мировое распрост | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.60 | Модель «вдохновитель → локальные распространители → мировой  |  |
| 35 | Выбирать более адекватные и благоприятные варианты жизни и бизнеса, тестировать  | `ideas/zapas-prochnosti-pravo-na-bolshe-testov-i-bystree-razvi.md` | 0.72 | «Запас прочности = право на больше тестов и быстрее развитие |  |
| 36 | Jetix как глобальная экосистема «кланов» вокруг брендов инфлюенсеров и блогеров: | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.62 | Оба о глобальной модели с распределённой сетью и долями (30% |  |
| 37 | Каждый партнёр/блогер получает свой «клан» — лояльную аудиторию, которая сотрудн | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.68 | Оба описывают клан как инфраструктуру кооперации; вики делае |  |
| 38 | Инфлюенсеры и блогеры с уже готовой аудиторией (даже 10K подписчиков) — главный  | `ideas/proekt-netvorkinga-sayt-video-portret-lyudey-regulyarny.md` | 0.65 | Вики явно упоминает блогеров 10-20K как ускорителей роста; в |  |
| 39 | «Клан» (геймифицированное сообщество под брендом конкретного человека) даёт боль | `ideas/soobshchestvoklan-skhozhie-tsennosti-vzaimozashchita-se.md` | 0.70 | Оба о клане/сообществе как более глубоком формате, чем прост |  |
| 40 | Система «кланов» вокруг брендов блогеров: участники выполняют задачи, сотруднича | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.68 | Оба о клане как платформе кооперации участников; вики — про  |  |
| 41 | Продюсирование немедийных экспертов: упаковка, YouTube daily-life контент, сбор  | `ideas/prodyuserskiy-tsentr-value-proposition-dlya-sozdateley.md` | 0.75 | Продюсерский центр для создателей контента — упаковка экспер |  |
| 42 | Аудитория блогера изолирована внутри себя и не умеет сотрудничать — именно этот  | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.63 | Клан как инфраструктура кооперации — родственная идея создан |  |
| 43 | Сначала заработать деньги — без денег нет ресурсов на продвижение и масштабирова | `ideas/strategiya-zapuska-odna-ideya-startovyy-kapital-masshta.md` | 0.80 | «Одна идея → стартовый капитал → масштабирование» прямо совп |  |
| 44 | Экспансивное состояние с каскадной генерацией идей — ощущение «всё уже есть, бер | `ideas/sistema-udlineniya-idey-ot-zamysla-k-realistichnoy-mode.md` | 0.62 | Обе записи о конвертации сырых идей в конкретные шаги/модели |  |
| 45 | Если собрать 10 стратегических партнёров + инвесторов, которые направят ресурсы  | `ideas/nayti-investorapartnera-s-dengami-dlya-uskoreniya.md` | 0.68 | Оба о привлечении инвестора/партнёра с ресурсами для ускорен |  |
| 46 | Продукт/направление Jetix — сертификация управленцев сложными AI-системами ('фюр | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.62 | Клан/школа как система проверки компетентности (прошёл испыт |  |
| 47 | Сложными системами должны управлять реальные люди с опытом — это уже происходит  | `ideas/klan-kak-infrastruktura-proverennoy-kooperatsii.md` | 0.65 | 'Система подготовки людей, доказавших компетентность через и |  |
| 48 | Синергия предпринимательского сообщества с топовыми музыкантами и блогерами — их | `ideas/model-vliyaniya-ideynyy-vdokhnovitel-lokalnye-rasprostr-2.md` | 0.63 | Оба о масштабировании через блогеров/распространителей с эфф |  |
| 49 | Окружать себя людьми, которые понимают тебя и делают аналогичные дела — путешест | `sources/2026-04-16-safe-hedonism-personal-motivation.md` | 0.68 | Safe-hedonism явно упоминает тусовки+путешествия как ядро мо |  |

---

# §C — Tier C: Propose-new entries

> **35 items** with score < 0.6 OR no plausible match.
>
> **Bulk-ack commands:**
> - `/wiki-bulk-ack --tier C --select N,N,N --as-new` (creates new wiki entries)
> - `/wiki-bulk-ack --defer-backlog N,N,N` (parks in backlog only)

## §C.1 — High-frequency (freq ≥3) — strong propose-new candidates

_(none)_

## §C.2 — Medium-frequency (freq=2)

_(none)_

## §C.3 — Single-mention (freq=1) — backlog stub list

_35 items — full list in `04-wiki-candidates-v2.json`. Top 80 below._

| # | Voice content | Proposed slug | Memo |
|---|---|---|---|
| 1 | Ночью — отдых, нужно хорошо выспаться перед активным днём с записью видео. Высокий эмоцион | `claims/nochyu` |  |
| 2 | Голосовая заметка выполняет функцию самонастройки — вербализация масштаба видения служит и | `claims/golosovaya-zametka-vypolnyaet-funktsiyu-samonastroyki` |  |
| 3 | Есть чёткое ощущение, что текущий момент — только начало, и масштаб будущего настолько вел | `claims/est-chyotkoe-oschuschenie-chto-tekuschiy-moment` |  |
| 4 | Jetix-методология должна стать глобальной привычкой уровня мытья рук: управление входящей  | `topics/jetix-metodologiya-dolzhna-stat-globalnoy-privychkoy-urovnya` |  |
| 5 | Целевая аудитория Jetix самофильтруется: те, кому важно развиваться и следить за собой, бу | `claims/tselevaya-auditoriya-jetix-samofiltruetsya` |  |
| 6 | Конкретный план масштабирования Jetix: 100 подкастов + нарезчики видеоконтента + сильные п | `claims/konkretnyy-plan-masshtabirovaniya-jetix` |  |
| 7 | Нанять сильных продавцов для персонального аутрича — анализ каждого потенциального клиента | `ideas/nanyat-silnykh-prodavtsov-dlya-personalnogo-autricha` |  |
| 8 | Философия Jetix: управлять собой ради собственной безопасности и развития, чтобы не причин | `claims/filosofiya-jetix` |  |
| 9 | Руслан ощущает, что Jetix уже находится на уровне методологии ('мы есть этот уровень') — н | `claims/ruslan-oschuschaet-chto-jetix-uzhe-nakhoditsya-na-urovne-met` |  |
| 10 | Онлайн-мастерские сначала мощно развиваются, затем переходят в офлайн: склады и workspaces | `topics/onlayn-masterskie-snachala-moschno-razvivayutsya-zatem-perek` |  |
| 11 | Физическое пространство мастерской: работаешь за компом и тут же тестируешь продукты на то | `topics/fizicheskoe-prostranstvo-masterskoy` |  |
| 12 | Долгосрочно всё переходит к разработке игр и Ready Player One-уровню реальности: сложные в | `topics/dolgosrochno-vsyo-perekhodit-k-razrabotke-igr-i-ready-player` |  |
| 13 | Один склад/warehouse можно адаптировать под невообразимое количество разных занятий и напр | `claims/odin-sklad-warehouse-mozhno-adaptirovat-pod-nevoobrazimoe-ko` |  |
| 14 | Физические мастерские/workspaces со своими стилями и направлениями: от изучения конкретных | `ideas/fizicheskie-masterskie-workspaces-so-svoimi-stilyami-i-napra` |  |
| 15 | Готов бесконечно заниматься поиском, тестированием и продвижением новых, более эффективных | `claims/gotov-beskonechno-zanimatsya-poiskom-testirovaniem-i-prodviz` |  |
| 16 | Как выстроить бизнес-модель мастерских так, чтобы она была устойчива к «разрушителям» — те | `topics/kak-vystroit-biznes-model-masterskikh-tak-chtoby-ona-byla-us` |  |
| 17 | Геймификация с повторяющимися взаимодействиями «взламывает» теорему заключённого: в доверя | `claims/geymifikatsiya-s-povtoryayuschimisya-vzaimodeystviyami-vzlam` |  |
| 18 | Централизованная библиотека шаблонов контента в Jetix (видео, влоги, стратегические поясне | `ideas/tsentralizovannaya-biblioteka-shablonov-kontenta-v-jetix-vid` |  |
| 19 | «Цифровые аватары» + инфраструктура для коммуникации внутри аудитории одного блогера: сейч | `ideas/tsifrovye-avatary-infrastruktura-dlya-kommunikatsii-vnutri-a` |  |
| 20 | Существующие аудитории блогеров — уже готовый «комбайн»: один сигнал в 600K аудиторию даёт | `claims/suschestvuyuschie-auditorii-blogerov` |  |
| 21 | Каждому потенциальному партнёру доносить идею кланов до полного понимания — не останавлива | `claims/kazhdomu-potentsialnomu-partnyoru-donosit-ideyu-klanov-do-po` |  |
| 22 | Какие существуют методы управления/вовлечения людей в систему: просьба, покупка, аренда ре | `topics/kakie-suschestvuyut-metody-upravleniya-vovlecheniya-lyudey-v` |  |
| 23 | Как организовать взаимодействие между аудиториями разных блогеров под единым брендом Jetix | `topics/kak-organizovat-vzaimodeystvie-mezhdu-auditoriyami-raznykh-b` |  |
| 24 | Перед любым значимым взаимодействием (продажи, найм, убеждение, партнёрство) — собирать бо | `claims/pered-lyubym-znachimym-vzaimodeystviem-prodazhi-naym-ubezhde` |  |
| 25 | Перед любым стратегическим взаимодействием — максимальная предварительная разведка: собрат | `claims/pered-lyubym-strategicheskim-vzaimodeystviem` |  |
| 26 | Начинать с малого и масштабировать по шаблону: один элемент → второй → третий. Сфокусирова | `claims/nachinat-s-malogo-i-masshtabirovat-po-shablonu` |  |
| 27 | Принцип 'бить твёрдым по пустому' универсален: применим к продажам, найму, переговорам, уб | `claims/printsip-bit-tvyordym-po-pustomu-universalen` |  |
| 28 | Фреймворк 'pre-interaction intelligence': систематический сбор данных о человеке перед про | `ideas/freymvork-pre-interaction-intelligence` |  |
| 29 | Руслан работает в одиночку над задачей масштаба 'собрать 10 стратегических партнёров + инв | `claims/ruslan-rabotaet-v-odinochku-nad-zadachey-masshtaba-sobrat-10` |  |
| 30 | Единые мировые правила управления сложными системами необходимы для глобальной совместимос | `claims/edinye-mirovye-pravila-upravleniya-slozhnymi-sistemami-neobk` |  |
| 31 | Слушал Майкла Джексона ночью — ощущение отличное, заряжает. Хочет научиться так же чувство | `claims/slushal-maykla-dzheksona-nochyu` |  |
| 32 | Научиться танцевать и лучше чувствовать тело — для харизмы, энергии, самовыражения. | `ideas/nauchitsya-tantsevat-i-luchshe-chuvstvovat-telo` |  |
| 33 | Гениальная корпорация, которая продвигает предпринимателей, дисциплинированных людей, топо | `topics/genialnaya-korporatsiya-kotoraya-prodvigaet-predprinimateley` |  |
| 34 | Продвигать предпринимательство и системный подход как спорт и игру — стабильно и логично в | `ideas/prodvigat-predprinimatelstvo-i-sistemnyy-podkhod-kak-sport-i` |  |
| 35 | Строить жизнь вокруг путешествий, тусовок и больших проектов с людьми, которые тебя понима | `topics/stroit-zhizn-vokrug-puteshestviy-tusovok-i-bolshikh-proektov` |  |

---

# §D — Skipped (CRM contacts, tasks, low-quality)

> **31 items** routed elsewhere or out-of-scope.
> CRM contacts → use `/crm-add` separately.

| # | Reason | Item preview |
|---|---|---|
| 1 | Задачи → operational | На следующей неделе провести созвоны, собрать обратную связь по наработкам, нача |
| 2 | Задачи → operational | Приоритет ближайших двух недель — работа с мастерской менеджеров: обсуждение сис |
| 3 | Задачи → operational | Записать видео с целями и планом: сначала подтягиваем систему до нужного уровня, |
| 4 | Задачи → operational | Организовать встречу (2 часа) с Царём и Анатолием Левенчуком — представить нараб |
| 5 | Задачи → operational | Завтра записать видео (первый видеоконтент для Jetix). |
| 6 | Задачи → operational | Настроить сайт для Jetix — как часть упаковки и позиционирования. |
| 7 | Задачи → operational | Заняться упаковкой: оформление, позиционирование, имидж — в рамках плана на меся |
| 8 | Задачи → operational | Настроить фундамент системы совместно с мастерской менеджеров, пройти необходимо |
| 9 | Контакты → /crm-add | Анатолий Левенчук — запланирована стратегическая сессия по монетизации (формат:  |
| 10 | Контакты → /crm-add | Царь — упомянут как ключевой человек для совместной работы по стратегии монетиза |
| 11 | Задачи → operational | Проработать майнсет совместно с Цериным и Анатолием Левенчуком — настроить на гл |
| 12 | Задачи → operational | Зафиксировать проработанный майнсет в системе для регулярного пересмотра — повес |
| 13 | Задачи → operational | Обучиться у более опытных людей управлению командой и построению очереди из спец |
| 14 | Задачи → operational | Внедрить геймификацию в систему личного развития — использовать как инструмент р |
| 15 | Контакты → /crm-add | Церин — упомянут как человек, с которым нужно совместно проработать майнсет на г |
| 16 | Контакты → /crm-add | Анатолий Левенчук — упомянут в контексте работы с майнсетом и настройки на глоба |
| 17 | Задачи → operational | Накидать конкретный план масштабирования Jetix до мирового уровня: гипотезы, ког |
| 18 | Задачи → operational | На следующей неделе начать воплощать наговоренные идеи по позиционированию и мас |
| 19 | Контакты → /crm-add | Царин — автор поста с аналогией 'системный подход = привычка мыть руки', которую |
| 20 | Задачи → operational | На человека реально влияет только ближайшее окружение — примерно 10–100 человек  |
| 21 | Задачи → operational | Зафиксировать и детально проработать концепцию ближнего окружения (10–100 челове |
| 22 | Задачи → operational | Донести видение масштаба и амбиций Jetix (уровень стран) в первую очередь до уча |
| 23 | Задачи → operational | Зафиксировать концепцию мастерских (онлайн → офлайн → экосистема), переварить и  |
| 24 | Задачи → operational | За 2 недели описать фундамент системы: кланы, монетизацию, продвижение через инф |
| 25 | Задачи → operational | Детально описать модель бартера/партнёрства для каждого типа потенциального парт |
| 26 | Задачи → operational | Составить список целевых инфлюенсеров и блогеров по всем платформам (LinkedIn, T |
| 27 | Задачи → operational | Детально описать геймификацию кланов: механики, типы задач, структуру вознагражд |
| 28 | Задачи → operational | Собрать первых 10 стратегических партнёров и инвесторов — людей, готовых вложить |
| 29 | Задачи → operational | Разработать и зафиксировать шаблон предварительного исследования перед любым стр |
| 30 | Задачи → operational | Оформить концепцию 'фюрершайна Jetix' в документ позиционирования: Jetix как соз |
| 31 | Задачи → operational | Изучить историю Майкла Джексона — как строил образ, харизму, движение вокруг себ |
