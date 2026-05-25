---
title: Build Artefacts Specs — детальные спецификации 10-12 Build артефактов перед сборкой
date: 2026-05-25
type: server-cc-autonomous-prompt
prompt_class: strategic-synthesis-per-artefact-specs-human-language
explain_file: _EXPLAIN-BUILD-ARTEFACTS-SPECS-2026-05-25.md
output_main_doc: decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md
output_reports_dir: reports/build-artefacts-specs-2026-05-25/
F: F2
G: prompt-build-artefacts-specs-2026-05-25
R: refuted_if_sample_artefact_content_written_OR_jargon_heavy_OR_lt_5_mermaid_OR_LOCK_modified_OR_R1_strategic_prose_authored_OR_new_research_attempted_OR_auto_launch_consequent
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
roy_dispatch_target: brigadier + project-brigadier + mgmt-expert + engineering-expert + systems-expert + philosophy-expert + investor-expert + methodology-engineer + recruitment-dynamics-expert + influence-ethics-expert (R12 auto-fire) + nlp-expert (R12) + propaganda-expert (R12) + gamification-engagement-expert (R12) + sota-tracker-expert + ml-ai-foundations-expert
language: russian primary
style_anchor: PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md + EXECUTION-PLAN-FIXATION-2026-05-24.md + PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md
mode: BUILD ARTEFACTS SPECS SYNTHESIS (F3 derivative — no new research, no sample artefact content)
mermaid_target: 5-7 schemes BS-1..BS-7
status: AWAITING-RUSLAN-ACK для launch
parent_plan: decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md
audience_focus: умные партнёры (T1 методологи + T1 R12-мост + smart T3 тестеры) — sweep principle per artefact
---

# 🏗️ Build Artefacts Specs — детальные спецификации 10-12 Build артефактов

## §0 Acceptance gate (что делает run "PASSED")

✅ Plain Russian primary (NO jargon без перевода)
✅ Style anchor PARTNER-OFFERING-HUMAN-LANG + EXECUTION-PLAN-FIXATION + PLATFORM-LIFECYCLE-STAGES-PLAN
✅ 10-12 артефактов получают full 15-point deep spec (см. §3 ниже)
✅ Audience focus sweep — «умные партнёры» сквозной principle per артефакт
✅ Substrate-pull map — explicit per артефакт (откуда что тянем — конкретные файлы + sections)
✅ Cross-artefact dependencies map + critical path + параллельность
✅ R12 8-Q check применён per каждому артефакту с partner-facing surface
✅ Main doc 12-15K plain Russian + 5-7 mermaid BS-1..BS-7 inline
✅ 00-SUMMARY ≤700w
✅ 10-15 R1 decisions surfaced (variants + facts, не resolved)
✅ Per-phase commit + push `[build-specs] Phase N`
✅ Final push с Main + Summary + per-artefact matrix + mermaid INDEX

⛔ FAIL if:
- Strategic prose `prose_authored_by` ≠ scribe role
- LOCK files modified (4 LOCKED canonical / Foundation paths / principles/ / shared/schemas/ / .claude/config/)
- New external research attempted (books / online sources / new fact-finding)
- **Sample artefact content written** (если в Видео A spec появляется реальный текст сценария > 1 короткого параграфа примера; если в Charter spec пишется готовый текст подписи; если в Notion spec появляются конкретные имена полей и формул > illustrative — FAIL. Мы пишем СПЕКИ, не сами артефакты)
- Auto-launch consequent prompts (no triggering записи видео / no запуск Notion implementation prompt)
- Auto-creation Notion pages / Notion API calls
- Bare facts без F-G-R triple per major claim
- Имена treated as bindings (Maxim/Дмитрий/Прапион/Левенчук = examples per IP-1)
- Audience focus отсутствует или размытый («для всех 5+1 архетипов» вместо «primary = умные партнёры + secondary = mention»)

---

## §17.0 ⭐⭐⭐ CRITICAL IMPORTANCE MANDATE (MAX-density)

> Per memory `feedback_max_density_max_tokens.md` 2026-05-21 ack.

Этот deliverable = **самый критичный prompt этой недели** — он стоит между текущим состоянием каши («что говорить в видео? какие базы в Notion? что в Charter?») и **состоянием когда ты можешь сесть и записать/собрать каждый артефакт целенаправленно** по готовой спеке. От качества этого spec'а зависит весь Build 4-недельный план.

1. **CRITICAL IMPORTANCE MANDATE** — это превращение Build-блокеров из «вид массы работы» в **конкретные spec sheets per артефакт, по которым умный партнёр потом тоже сможет работать**
2. **ROY swarm на 500%** — brigadier orchestrates:
   - 5 original ROY experts (engineering + investor + mgmt + philosophy + systems) full dispatch
   - 4 sub-brigadiers parallel (project-brigadier × per-artefact deep-dive)
   - 8 book-driven ROY experts auto-fire per R12 trigger rules:
     - **methodology-engineer** (Видео A spec + Method V2 §J substrate pull) ✅
     - **recruitment-dynamics** (видео C + Charter spec + лендинг — R12 paired) ✅
     - **influence-ethics** (AUTO-FIRE per Charter / лендинг / discovery call / видео C) ✅
     - **nlp** (AUTO-FIRE per лендинг текст / hooks / CTA framing — R12 STRICT) ✅
     - **propaganda** (AUTO-FIRE per video messaging analysis — R12 STRICT) ✅
     - **gamification-engagement** (R12 AUTO-FIRE per Notion + Charter mechanics) ✅
     - **ml-ai-foundations** (Notion implementation + Team OS spec — backend awareness) ✅
     - **sota-tracker** (видео B + paradigm shift O-176..O-185 grounding) ✅
3. **Use MAX доступных tokens × 3** — не экономь; depth > brevity per per-artefact section
4. **Максимально сырая information** — read FULL Platform Lifecycle Plan + FULL Execution Plan + FULL Consolidated HL + FULL Personal OS + FULL Team OS + FULL Outreach Content + FULL Method V2 §J + FULL ed-paradigm Notes (не summaries)
5. **Quality explanation focus** — densest plain-Russian explanations per артефакт; multiple angles per artefact; each spec section substantive prose, не bullets-only
6. **Concrete examples** mandatory per артефакт — multiple per artefact; vivid; bound к RUSLAN-LAYER examples (Дмитрий / Сева / Maxim / Oleg / Левенчук / Прапион / Цэрэн / Tseren — preserved per existing baseline) but treated as IP-1 examples not assigned
7. **Плотность всего** — each artefact spec ≥1-1.5K words; each mermaid dense (≥8-12 nodes); each per-spec section substantive
8. **Не stopover at minimum** — produce best work possible regardless of estimated runtime/cost; если 12-15K words main = недостаточно для density → push до 18-20K
9. **Если можно add 1 more diagram / variant / cross-cite → add**

---

## §1 Контекст и роль (что вообще делаем)

Ты — **brigadier-scribe** (Cloud Cowork Opus 4.7 [1M ctx] на server CC). Твоя задача — взять PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25 §6 (documents matrix) + §8 (Build 4-недельный план) и **развернуть** каждый Build-артефакт в детальную спецификацию по 15-point template (§3 ниже). Результат — единый plain-Russian документ ~12-15K слов + 5-7 mermaid + 8+ фазовых отчётов + 00-SUMMARY ≤700w.

**Ты НЕ пишешь сами артефакты** (не текст видео, не реальные Notion поля, не реальный текст Charter). Ты пишешь **спецификации** — что артефакт должен делать, на кого нацелен, как структурно устроен, откуда substrate тянем, как поймём что готово.

**Audience focus сквозной — умные партнёры** (T1 методологи + T1 R12-мост + smart T3 тестеры). Каждый артефакт specifically заточен под critical-thinking аудиторию, не массу. Это не «лендинг для всех» — это «лендинг который умный методолог сможет открыть, за 2 минуты понять substance, и решить тестировать ли». Mass appeal — secondary mention.

**Constitutional posture STRICT:**
- R1 surface only — все варианты per артефакт = options + facts. НЕ «рекомендую вариант X». Финальные decisions (стиль / тон / акценты) = Ruslan.
- R2 STRICT — Foundation paths не трогаем. 4 LOCKED canonical = reference only.
- R6 — каждый major claim per артефакт = F-G-R triple + cross-cite к substrate source (footnote-style).
- R11 — никаких auto-actions: не создаём артефакты, не пушим Notion, не отправляем письма.
- R12 paired-frame STRICT — каждый артефакт с partner-facing surface проходит 8 вопросов explicitly в spec'е.
- IP-1 STRICT — имена создателей/исполнителей = RUSLAN-LAYER examples, не binding.
- Append-only — новые файлы, не modify existing.

---

## §2 Список 10-12 Build артефактов (canonical для этого prompt)

| # | Артефакт | Phase | Кто primary audience (Build) | Зависимость от |
|---|---|---|---|---|
| 1 | 🎬 **Видео A — методология / прошивка / база** | Phase 2 | T1 методолог + сам R12-чек метода | Method V2, ed-paradigm O-176..O-185 |
| 2 | 🎬 **Видео B — видение обучения / 7 ступеней / paradigm shift** | Phase 3 | T3 умный тестер + потенциальные cohort members | Consolidated HL, Outreach Content Bloom 1-7 |
| 3 | 🎬 **Видео C — экосистема / Charter / R12 / 4 типа партнёров** | Phase 4 | T1 методолог + R12-мост (Прапион) + опытные T3 | Execution Plan, Economic V10, R12 STRICT |
| 4 | 📋 **Notion Personal OS Layer 1+2 — 5 баз core implementation** | Phase 5 | smart T3 тестер (Дмитрий → Сева) | Personal OS Plan, Method V2 §J |
| 5 | 📋 **Notion Team OS Layer 3 — multi-tenant demo-scope для 1 партнёра** | Phase 6 | T1 методолог co-design demo | Team OS Plan, Personal OS baseline |
| 6 | 📜 **Charter v1 текст + структура + R12 чек** | Phase 7 | T1 R12-мост (Прапион ревью) + future cohort | Execution Plan §4, Economic V10 §11 R12 |
| 7 | 🌐 **Лендинг + FAQ 10 вопросов** | Phase 8 | T1 + smart T3 (low-friction entry) | PARTNER-OFFERING, Outreach Content CTAs |
| 8 | 🗣️ **Discovery call script** | Phase 9 | T1 + T3 первый контакт | Outreach Content, discovery call existing templates |
| 9 | ⚖️ **Юр package — Steuerberater email + Einzel/GmbH/UG матрица + контракт template** | Phase 10 | Self (foundational) | Execution Plan §3 foundational needs |
| 10 | 💰 **Бизнес-счёт + invoice template + bookkeeping минимум** | Phase 10 | Self (foundational) | Execution Plan §3 foundational |
| 11 | 📚 **Supporting course skeleton + Telegram positioning + sales-minimum** | Phase 11 | T1 + smart T3 trust-building | Outreach Content P0-P6, brand baseline |
| 12 | 📊 **Brand-minimum — visual identity / one-pager / pitch deck-light** | Phase 11 | T1 + T3 + visual partners | PARTNER-OFFERING HL, Jetix vision |

**Если в substrate появляется лишний обязательный артефакт — surface в Phase 12 как R1 decision, не add silently.**

---

## §3 15-point spec template (применяется per каждому артефакту в Phases 2-11)

Per каждому артефакту в его phase'е — заполняется этот template plain-Russian, dense, ≥1-1.5K words:

1. **Назначение (one-liner)** — что это вообще, в одной строке
2. **Цель (что хотим достичь)** — что должно случиться у читателя/смотрящего/пользователя после взаимодействия (поведенческая цель, не «знание»)
3. **Primary audience (умные партнёры)** — кто конкретно (типы партнёров + Bloom stage + что они знают / не знают / хотят / что отпугнёт)
4. **Secondary audience (mention only)** — кого ещё зацепит, но НЕ primary
5. **Ключевые сообщения (3-7 главных мыслей)** — что обязательно должно остаться у аудитории после взаимодействия
6. **Структура (sections/scenes/баз/полей/etc.)** — анатомия артефакта, разбивка на части
7. **Hook начала** — как зацепить за первые секунды/строки/поля; что показываем чтобы человек продолжил
8. **CTA конца** — к чему ведём (next action — пробовать / писать / читать / переходить)
9. **Формат / длина** — минуты (для видео) / страницы (для текста) / поля и базы (для Notion) / разделы (для Charter)
10. **Зависимости** — что должно быть готово ДО (pre-reqs), что блокирует, что параллельно
11. **Substrate sources** — какие готовые документы и какие именно sections тянутся в этот артефакт (explicit file paths + section refs)
12. **R12 paired-frame check** — 8 вопросов применённые к этому артефакту (цена ≤ польза? / конкретно? / соразмерно? / по ступени? / канал уместен? / не доим/не запираем? / нет манипуляции? / стоп-сигнал готов?)
13. **Acceptance criteria (чек-лист)** — explicit условия, по которым артефакт считается готовым (НЕ субъективное «готово», а measurable)
14. **Анти-паттерны** — чего НЕ делаем (что часто хочется добавить, но это убивает артефакт)
15. **Варианты / R1 decisions** — surface variants + facts по тем dimensions где есть несколько подходов (тон / акценты / длина / визуальный стиль / etc.). НЕ resolve.

---

## §4 Phases (per-phase task list)

### Phase 0 — FPF lens scope + substrate read (foundation)

**Tasks:**
- Read FULL prerequisite substrate (см. §3 EXPLAIN file для списка)
- Apply FPF lens: «Build артефакт = что в FPF terms?» (instance of artefact vs spec vs method vs role)
- Define F-G-R triple framework per артефакт class
- Define IP-1 separation rule (артефакт-роль vs создатель-исполнитель)
- Define audience focus principle (умные партнёры sweeping)
- List 10-12 Build артефактов с phase mapping (mirror §2 этого prompt)

**Output:** `reports/build-artefacts-specs-2026-05-25/01-fpf-lens-scope.md` (~1-2K)
**Commit:** `[build-specs] Phase 0 FPF lens + substrate read`

---

### Phase 1 — Overview + cross-artefact map + audience focus

**Tasks:**
- Plain-Russian обзор: что значит «Build артефакты» в контексте Platform Lifecycle (зачем эти 10-12 артефактов нужны именно сейчас, не позже, не раньше)
- Cross-map (table + mermaid BS-1): 10-12 артефактов × 4 типа партнёров (T1/T2/T3/T4) × 3 этапа Lifecycle (Build/Run/Scale) — где каждый артефакт нужен primary
- Audience focus deep dive: portrait of «умного партнёра» (что знает / не знает / хочет / отпугнёт) — с RUSLAN-LAYER examples (Maxim / Oleg / Дмитрий / Сева / Левенчук / Прапион / Ilshat / Ivan)
- Mermaid BS-1: cross-artefact map (10-12 nodes + audience + lifecycle connections)
- Surface R1 decision: «которые из 12 артефактов критичные для Build exit, которые nice-to-have»

**Output:** `reports/build-artefacts-specs-2026-05-25/02-overview-cross-map.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 1 overview + cross-map + audience portrait`

---

### Phase 2 — 🎬 Видео A spec (методология / прошивка / база)

**Apply 15-point template (§3).** Special focus:

- **Цель:** умный методолог за 5-15 мин понимает СУТЬ нашей методологии (не маркетинг) — может оценить substance, решить «есть здесь что проверить» или «всё уже у Левенчука»
- **Primary audience:** T1 методолог (Maxim/Oleg/Левенчук-tier) — критическое мышление, methodology-savvy, fluent в как минимум 1-2 методологиях
- **Substrate pull:** Method V2 §H (meta-control) + §J (методология композиции 8-component) + O-176..O-185 paradigm shift + Method V2 §G external system
- **R12 check:** не подаёмся как «новая революция»; явно ссылаемся на FPF/Левенчука/MMK; не обещаем результатов
- **Acceptance:** умный методолог после просмотра может пересказать 3-5 ключевых тезисов; понимает чем отличаемся от существующих методологий; решает дальше копать или нет
- **Анти-паттерны:** перфекционизм визуала / длинные пояснения базовых понятий (системное мышление и т.д. — assume аудитория знает) / маркетинговые обещания / «купи курс»
- **Варианты:** длительность (5/10/15 мин), стиль (talking head / screen-record schema / mix), глубина (entry / deep)

**Output:** `reports/build-artefacts-specs-2026-05-25/03-video-A-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 2 Видео A spec`

---

### Phase 3 — 🎬 Видео B spec (видение обучения / 7 ступеней / paradigm shift)

**Apply 15-point template.** Special focus:

- **Цель:** умный тестер/cohort-кандидат за 5-15 мин видит **новую парадигму обучения** (O-176..O-185 — прошивка vs накопление + AI usage stratification + question-first learning) — может понять «это про мне» или «это не про меня»
- **Primary audience:** smart T3 тестер (Дмитрий/Сева-tier) — humanitarian/curious/system-thinking-friendly, готовый попробовать новое
- **Substrate pull:** Consolidated HL §1-5 + Outreach Content 7 ступеней Bloom + RUSLAN-NOTES-EDUCATION-PARADIGM (2 verbatim voice notes) + Method V2 §J meta-method
- **R12 check:** не «избранные», явно «можешь уйти», не клятвы, fork-and-leave упомянут
- **Acceptance:** smart T3 после просмотра может сформулировать 3 ключевых отличия нашего подхода от стандартного обучения; понимает «прошивку» vs «накопление»; знает где попробовать
- **Анти-паттерны:** академический жаргон / слишком много терминологии / «революция в образовании» / over-promising результатов
- **Варианты:** длительность, акцент (на критику старого vs на новое), включение AI angle сильно или слабо

**Output:** `reports/build-artefacts-specs-2026-05-25/04-video-B-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 3 Видео B spec`

---

### Phase 4 — 🎬 Видео C spec (экосистема / Charter / R12 / 4 типа партнёров)

**Apply 15-point template.** Special focus:

- **Цель:** умный потенциальный партнёр (T1 + R12-мост) за 5-15 мин понимает **как устроена партнёрская экосистема** — 4 типа партнёров, что просим/даём, Charter / R12 защиты, fork-and-leave, доли — может оценить «есть здесь моё место» или «нет»
- **Primary audience:** T1 методолог + T1 R12-мост (Прапион-tier) + опытные T3 (Дмитрий после видео A+B)
- **Substrate pull:** Execution Plan §4 (4 типа партнёров) + Platform Lifecycle §4-5 (per-stage actors + give/ask) + Economic V10 §11 R12 + PARTNER-OFFERING HL (цены L1-L7 + 75/25)
- **R12 check:** **AUTO-FIRE influence-ethics + recruitment-dynamics + propaganda** — это самое опасное видео, mass-movement language temptation maximum; защита растёт быстрее системы; явно показываем потолки и выходы; нет «семьи»/«племени» frame
- **Acceptance:** умный партнёр после просмотра может сформулировать (1) 4 типа партнёров и в каком он подходит (2) что просят у него и что дают (3) как уйти если что (4) почему НЕ секта и НЕ пирамида
- **Анти-паттерны:** mass-movement language / «семья Jetix» / clan-pride / over-emphasis на growth metrics / fudge'инг про доли / умолчание про fork-and-leave
- **Варианты:** включение Economic V10 deep (или абстрактно), включение Programmable Ethereum Phase 2 (или skip), длительность

**Output:** `reports/build-artefacts-specs-2026-05-25/05-video-C-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 4 Видео C spec`

---

### Phase 5 — 📋 Notion Personal OS implementation spec (Layer 1+2 — 5 баз core)

**Apply 15-point template.** Special focus:

- **Цель:** smart T3 тестер (Дмитрий первым) получает рабочий Personal OS в Notion, может fork → adapt → реально использовать ≥1 неделю → дать feedback
- **Primary audience:** smart T3 (Дмитрий → Сева → other humanitarian) — Notion-comfortable, не developer
- **Substrate pull:** Personal OS Notion Template Plan FULL (Phase 1-15) + Method V2 §J + 4 типа партнёров (для frame integration)
- **Implementation scope для Build:** **5 баз core (НЕ полный Layer 1+2)** — что именно входит в demo-ready scope для Дмитрия (R1 decision: какие 5 из 7+ возможных баз)
- **R12 check:** fork-friendly (не lock-in), explicit copy-instructions, нет привязки к нашему workspace
- **Acceptance:** Дмитрий открывает demo → видит 5 баз → fork'нул в свой workspace в ≤30 мин → 1 неделю использует → даёт structured feedback (5-7 точек)
- **Анти-паттерны:** over-engineering (50 баз сразу) / Jetix-specific терминология в полях / formulas требующие технического background / нет fork-instructions
- **Варианты:** какие 5 баз (R1 decision), уровень формул (lite vs medium), включение AI integration helpers (готовые prompts) или нет

**Output:** `reports/build-artefacts-specs-2026-05-25/06-notion-personal-os-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 5 Notion Personal OS spec`

---

### Phase 6 — 📋 Notion Team OS Layer 3 implementation spec (multi-tenant demo для 1 партнёра)

**Apply 15-point template.** Special focus:

- **Цель:** T1 партнёр (Maxim или Oleg) видит как из Personal OS вырастает collaboration layer — может оценить «есть смысл со-вести когорту здесь» или «нет»
- **Primary audience:** T1 методолог + R12-мост (для проверки на анти-секту mechanics)
- **Substrate pull:** Team OS Notion Template Plan FULL (Phase 1-9) + Charter spec (Phase 7 этого prompt'a, для cross-ref)
- **Implementation scope для Build:** **demo-ready overlay (НЕ полный multi-tenant)** — minimum viable что показывает 10 ролей + Project Catalog + Skills/Needs + Charter slot + R12 чек-лист поля
- **R12 check:** AUTO-FIRE influence-ethics + gamification — Team OS = highest R12-risk surface; проверяем все 4 monetization шаблона на 8 вопросов; Mondragón 5:1 явно в полях; fork-and-leave button literal
- **Acceptance:** T1 партнёр за 30-60 мин понимает мульти-роль архитектуру; может симулировать своё participation в одной из 10 ролей; даёт structured feedback на R12 mechanics
- **Анти-паттерны:** показ «успешного клана» как fait accompli / lock-in поля (member commitments / vesting / etc.) / hidden formulas / отсутствие fork-button
- **Варианты:** demo scope (1 mock проект vs 3), monetization шаблон в demo (стандарт vs €1500 cohort), включение Ethereum Phase 2 overlay визуально

**Output:** `reports/build-artefacts-specs-2026-05-25/07-notion-team-os-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 6 Notion Team OS spec`

---

### Phase 7 — 📜 Charter v1 spec (текст + структура + R12 чек)

**Apply 15-point template.** Special focus:

- **Цель:** **R12-мост (Прапион)** может прочитать → дать структурированный feedback на анти-секту mechanics ≤2h reading + ≤1h call; T1 партнёр может прочитать → понять «здесь я не в кабале» → готов подписать когда придёт time
- **Primary audience:** R12-мост (Прапион primary) + T1 методолог + future cohort founder
- **Substrate pull:** Economic V10 §11 R12 STRICT + Execution Plan §4 8 вопросов + Team OS Plan Phase 5 Charter 6 секций + Foundation principles Tier 2 Rule 12 + 4 RUSLAN-LAYER action classes
- **Structure spec (6 секций per Team OS baseline):** preamble (зачем) / values (R12 anti-extraction + fork-and-leave) / roles (10 + multi-hat) / money (Mondragón 5:1 + 75-90% + revenue templates) / governance (Stage Gates + Steward) / exit (30-day notice + non-punitive + asset retrieval)
- **R12 check:** **AUTO-FIRE influence-ethics + recruitment-dynamics** — Charter = primary R12 surface; явно перечислены 4 RUSLAN-LAYER action classes (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt) и как ловим; Mondragón 5:1 в money секции с numerical example; fork-and-leave с 30-day notice ПЕРВЫМ пунктом exit секции
- **Acceptance:** Прапион reads in ≤2h → даёт structured feedback (5-10 точек) → 90%+ R12-checks PASS → revision → v1.1 ready для T1 партнёра review
- **Анти-паттерны:** legal-eze без plain-language версии / fluffy values prose без teeth / spending много времени на growth metrics / отсутствие explicit numerical потолков / hidden gotcha clauses
- **Варианты:** формат signature (текст-согласие vs juridical document vs смарт-контракт — Scale phase) / длина (краткий 3-page vs detailed 10-page) / включение Programmable Ethereum overlay явно или footnote

**Output:** `reports/build-artefacts-specs-2026-05-25/08-charter-spec.md` (~2-2.5K — этот самый critical R12-surface)
**Commit:** `[build-specs] Phase 7 Charter spec (R12 AUTO-FIRE)`

---

### Phase 8 — 🌐 Лендинг + FAQ 10 вопросов spec

**Apply 15-point template.** Special focus:

- **Цель:** умный методолог/тестер заходит на лендинг → за 2-5 мин понимает substance → может решить (a) попробовать (low-friction CTA) (b) написать с конкретным вопросом (c) уйти без раздражения
- **Primary audience:** T1 методолог + smart T3 (low-friction first touch)
- **Substrate pull:** PARTNER-OFFERING HL (style anchor + цены L1-L7) + Outreach Content 13 CTAs (выбор 2-3 для лендинга) + Consolidated HL ключевые мысли + Execution Plan §4 partner types
- **Structure spec (sections):** hero (1-liner + что мы делаем + НЕ что мы делаем) / for whom (4 partner types + 5+1 архетипов abstract) / what we offer (L1-L7 ступени + 75/25 + Mondragón) / how to start (3-step low-friction CTA) / FAQ (10 вопросов из реальных или anticipated) / R12 honesty (явно: что НЕ обещаем) / signup minimal (email + 1 question)
- **FAQ 10 вопросов:** spec включает 10 placeholder questions (с указанием что текст ответов = после первых реальных разговоров — Build exit checkpoint) — типы вопросов (сomparison с Левенчуком, цена, обязательства, выход, AI-replacement fear, time commitment, etc.)
- **R12 check:** AUTO-FIRE nlp + influence-ethics — каждая фраза лендинга на манипуляцию проверена; «купи сейчас» / scarcity / FOMO — FAIL; «попробуй и решай сам» — PASS
- **Acceptance:** Tester (Дмитрий-like) открывает → 5 мин на лендинг → может пересказать суть + 2-3 различия от типичных «AI курсов» + не чувствует давления
- **Анти-паттерны:** марketing-buzz / numbers без context / fake testimonials / hero claim про life change / hidden costs / forced signup для просмотра контента
- **Варианты:** одностраничный vs multi-page / включение video embed (после видео A готово) / language (только русский vs +английский) / hosting (Notion public / Webflow / static HTML)

**Output:** `reports/build-artefacts-specs-2026-05-25/09-landing-faq-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 8 Лендинг + FAQ spec`

---

### Phase 9 — 🗣️ Discovery call script spec

**Apply 15-point template.** Special focus:

- **Цель:** ≤45-минутный звонок где (a) ты понимаешь нужды/контекст партнёра (b) партнёр понимает наш substance (c) оба честно решают go/no-go без давления
- **Primary audience:** T1 первый контакт + T3 умный тестер pre-trial
- **Substrate pull:** Outreach Content sections про discovery + Execution Plan §4 partner types + 8 R12 вопросов + existing discovery templates если есть
- **Structure spec:** opening (≤3 мин — кто-я, цель звонка, time check, разрешение на нет) / context из их стороны (10-15 мин — что они делают, какие нужды) / substance из нашей (10-15 мин — что мы делаем, partner types match, R12) / mutual fit check (5-10 мин — есть ли смысл) / next steps (≤5 мин — explicit options + no-pressure exit)
- **R12 check:** AUTO-FIRE influence-ethics + nlp — каждая question template проверена на манипуляцию; «закрываем сделку» language → FAIL; «решай за неделю и без давления» → PASS; explicit «можно сейчас сказать нет — спасибо, спокойной ночи»
- **Acceptance:** Ruslan репетирует ≥5 раз (alone or with друг) → mid-track 5-минутный сomfort; partner после звонка может сформулировать «что Jetix делает» + «что от меня хотят» + «как уйти»
- **Анти-паттерны:** pre-canned pitch / leading questions / pressure для commitment в звонке / over-talking (>50% времени с нашей стороны) / отсутствие «нет — спасибо»
- **Варианты:** длина (30 vs 45 vs 60 мин) / формат (audio only vs video) / preparation expected (партнёр читает что ДО? видео A? PARTNER-OFFERING?)

**Output:** `reports/build-artefacts-specs-2026-05-25/10-discovery-call-spec.md` (~1.5-2K)
**Commit:** `[build-specs] Phase 9 Discovery call script spec`

---

### Phase 10 — ⚖️ Юр + 💰 Бизнес-счёт + invoice template spec (combined foundational)

**Apply 15-point template (combined для юр + финансы).** Special focus:

- **Цель:** Build exit состоянии — Ruslan имеет (a) юр форма выбрана и регистрация в процессе (b) бизнес-счёт открыт (c) invoice template готов отправить (d) bookkeeping минимум настроен
- **Primary audience:** Self (foundational) + downstream партнёры (которые должны видеть «эти ребята с легальным базисом»)
- **Substrate pull:** Execution Plan §3 foundational + ed-research если есть на Berlin / Germany legal forms
- **Structure spec — 4 sub-deliverables:**
  - 4.1 **Steuerberater email template** (что спрашиваем — Einzel/GmbH/UG decision matrix; cooperative governance feasibility; tax implications для cohort revenue 75/25; cost expectations)
  - 4.2 **Einzel/GmbH/UG matrix** (per форма: cost startup, ongoing cost, liability, tax regime, cooperative compatibility, optimal for Build/Run/Scale)
  - 4.3 **Контракт template** (partner agreement minimum — обязанности, доли, exit, IP)
  - 4.4 **Invoice template + bookkeeping** (SEPA-ready invoice for EU + минимум для tracking — FastBill/lexoffice/sevDesk сравнение)
- **R12 check:** контракт template MUST include fork-and-leave clause + 30-day notice + asset retrieval + cooperative-governance compatibility
- **Acceptance:** Ruslan получает (a) email Steuerberater'у готов отправить (b) 3-форма matrix позволяет prep-decision до consultation (c) контракт template можно adapt для конкретного партнёра in ≤30 мин (d) invoice template generates valid EU invoice
- **Анти-паттерны:** over-engineering форм / выбор GmbH без Steuerberater consultation / контракт с lock-in clauses / invoice template без SEPA support
- **Варианты:** какая форма preferred default (Einzel cheapest / UG limited-liability low-cap / GmbH classic) — R1 decision after Steuerberater / cooperative-legal hosting (DE Genossenschaft vs international structure)

**Output:** `reports/build-artefacts-specs-2026-05-25/11-legal-finance-spec.md` (~2-2.5K combined)
**Commit:** `[build-specs] Phase 10 Юр + Финансы spec`

---

### Phase 11 — 📚 Supporting materials spec — course skeleton + Telegram + sales-minimum + brand-minimum

**Apply 15-point template (combined для 4 sub-deliverables).** Special focus:

- **Цель:** umные партнёры открывая Telegram канал / one-pager / pitch deck / course skeleton видят «здесь serious work, эти ребята настоящие, есть substance» — НЕ полноценные финальные artefacts, а **minimum credible baseline**
- **Primary audience:** T1 + smart T3 (trust-building secondary surface beyond видео + лендинг)
- **Structure spec — 4 sub-deliverables:**
  - 11.1 **Course skeleton** (table of contents для будущего курса — sections + Bloom 1-7 mapping + 7 принципов intersection — НЕ реальный контент, только skeleton что появится в Run stage когда T1 партнёр будет co-creating)
  - 11.2 **Telegram positioning** (channel description + первые 5-7 постов outline — что публикуем чтобы умный новый подписчик понял substance; НЕ content calendar на месяцы)
  - 11.3 **Sales-minimum** (one-pager — 1 страница которую можно отправить «вот что мы делаем» в ответ на «расскажи»; pitch deck-light 5-7 slides для face-to-face)
  - 11.4 **Brand-minimum** (visual identity — logo если есть / typography / 2-3 colors / минимум template для consistency)
- **R12 check:** AUTO-FIRE nlp на Telegram positioning + sales-minimum — phrasing проверен; one-pager НЕ marketing fluff; pitch deck без vanity metrics
- **Acceptance:** smart T3 после consuming любого из 4 sub-deliverables получает consistent picture; не противоречит видео A/B/C / лендингу / Charter
- **Анти-паттерны:** premature brand-investment (полный logo redesign / website rebuild перед Build exit) / fake metrics / pitch deck > 10 slides / Telegram cadence-pressure до того как substance готов
- **Варианты:** course skeleton глубина (sections only vs sections+lessons titles) / Telegram language (только русский vs +английский) / pitch deck design (DIY Canva vs professional designer)

**Output:** `reports/build-artefacts-specs-2026-05-25/12-supporting-materials-spec.md` (~2-2.5K combined)
**Commit:** `[build-specs] Phase 11 Supporting materials spec`

---

### Phase 12 — 🔗 Dependencies + sequencing + risk map + критический path

**Tasks:**
- Cross-artefact dependency graph (mermaid BS-2): какой артефакт от какого зависит, что блокирует
- Critical path (mermaid BS-3): минимальный critical sequence для Build exit (≥80% gates from Platform Lifecycle §8)
- Параллельность: что можно делать одновременно (видео A + Steuerberater email + CRM-разметка — independent), что строго sequentially (Charter → Charter R12 review → Charter v1.1 → подписи)
- Risk map per артефакт: top 2-3 риска + mitigation
- Timeline overlay на Platform Lifecycle §8 4-недельный план — какие артефакты ready by which week
- Surface 5-7 R1 decisions: priority order, что критично / nice-to-have, скоро ли запускать Notion implementation prompt (Week 1) vs позже (Week 2)

**Output:** `reports/build-artefacts-specs-2026-05-25/13-dependencies-risks.md` (~2-2.5K)
**Commit:** `[build-specs] Phase 12 dependencies + sequencing + risks + mermaid BS-2/BS-3`

---

### Phase 13 — Main consolidated + 00-SUMMARY + per-artefact matrix + mermaid INDEX

**Tasks:**
- Main doc `decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md` ~12-15K plain Russian:
  - §0 90-сек TL;DR
  - §1 Главная мысль (зачем спеки, audience focus = умные партнёры)
  - §2 Список 10-12 артефактов + cross-map mermaid BS-1
  - §3-12 per-artefact deep specs (compressed из phase reports — full version в reports)
  - §13 Dependencies + sequencing
  - §14 R12 sweep — какие артефакты highest-risk surface
  - §15 Build exit checkpoint per артефакт
  - §16 R1 decisions queue (10-15 решений for Ruslan)
  - §17 Cross-refs к substrate
  - §18 К чему ведёт (что разблокирует следом)
- 00-SUMMARY ≤700w (per Ruslan reading time ≤5 мин)
- Per-artefact matrix table — quick reference (артефакт / цель / audience / зависимости / acceptance / status)
- Mermaid INDEX 5-7 schemes BS-1..BS-7 (cross-map / dependencies / critical path / R12 risk overlay / build-to-run handoff / audience priority / sequencing weeks)

**Output:** `decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md` (main) + `00-SUMMARY-FOR-RUSLAN.md` + `diagrams/_INDEX.md`
**Commit:** `[build-specs] Phase 13 Main + Summary + INDEX (final push)`

---

## §5 Output structure (что ожидаем на выходе)

```
decisions/strategic/
└── BUILD-ARTEFACTS-SPECS-2026-05-25.md         # main ~12-15K + 5-7 mermaid

reports/build-artefacts-specs-2026-05-25/
├── 00-SUMMARY-FOR-RUSLAN.md                    # ≤700w
├── 01-fpf-lens-scope.md                        # Phase 0
├── 02-overview-cross-map.md                    # Phase 1
├── 03-video-A-spec.md                          # Phase 2
├── 04-video-B-spec.md                          # Phase 3
├── 05-video-C-spec.md                          # Phase 4
├── 06-notion-personal-os-spec.md               # Phase 5
├── 07-notion-team-os-spec.md                   # Phase 6
├── 08-charter-spec.md                          # Phase 7
├── 09-landing-faq-spec.md                      # Phase 8
├── 10-discovery-call-spec.md                   # Phase 9
├── 11-legal-finance-spec.md                    # Phase 10
├── 12-supporting-materials-spec.md             # Phase 11
├── 13-dependencies-risks.md                    # Phase 12
└── diagrams/
    └── _INDEX.md                               # 5-7 mermaid BS-1..BS-7
```

---

## §6 Style anchors (mandatory reference)

- **PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md** — plain Russian conversational tone, emoji headers, dense readable prose, mermaid inline (light bg)
- **EXECUTION-PLAN-FIXATION-2026-05-24.md** — 4 партнёров / 2 направления / 8 R12 вопросов pattern
- **PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md** — parent план, его §6 documents matrix + §8 4-week plan = baseline
- Mermaid theme: `{'theme':'base', 'themeVariables': {'primaryTextColor':'#000', 'textColor':'#000', 'lineColor':'#333', 'primaryBorderColor':'#333', 'primaryColor':'#fafafa'}}` (light bg для GitHub readability)

---

## §7 Constitutional reminder

| Rule | Application |
|---|---|
| **R1 surface only** | Spec'и = options + facts. НЕ «рекомендую вариант X». R1 decisions queue в §16 main + §15 каждой phase |
| **R2 STRICT** | Foundation paths не трогаем. 4 LOCKED canonical = reference only |
| **R6 provenance** | F-G-R triple per major claim + cross-cite к substrate source (footnote-style) |
| **R11 Default-Deny** | NO auto-actions: не создаём артефакты, не пушим Notion API, не отправляем письма, не записываем видео |
| **R12 paired-frame STRICT** | 8 вопросов explicitly в каждом артефакт spec'е с partner-facing surface. AUTO-FIRE influence-ethics + recruitment-dynamics + nlp + propaganda + gamification per applicable phases |
| **IP-1 STRICT** | Имена создателей/исполнителей = RUSLAN-LAYER examples (Maxim/Дмитрий/Прапион), артефакт-роли = abstract |
| **Append-only** | Новые файлы, не modify existing decisions/strategic/ |
| **Pool result** | NO auto-launch consequent prompts (не триггерим запись видео / не запускаем Notion implementation prompt) |
| **F3 derivative** | Никакого нового external research; только перерезка существующего substrate |

---

## §8 К чему ведёт после прогона

После завершения (~3-5h автономной работы server CC):

1. Ruslan reads 00-SUMMARY (5 мин) → main doc (20-30 мин) → at most 1-2 phase reports per artefact он хочет deep
2. Ruslan picks 10-15 R1 decisions из §16
3. На основе spec'ов → следующая неделя (per Platform Lifecycle §8 Week 1):
   - Видео A запись (по spec'у Phase 2)
   - Notion Personal OS implementation (по spec'у Phase 5) — для Дмитрий trial
   - Steuerberater email отправлен (по spec'у Phase 10)
   - CRM 5+1 архетипов разметка первых 10
4. **Это НЕ запускает auto** — pool result, Ruslan launches каждый сам когда готов

---

*Prompt closure 2026-05-25. Build Artefacts Specs — F3 derivative per Platform Lifecycle Plan §6+§8. 10-12 артефактов get 15-point deep specs. Audience focus = умные партнёры sweeping. NO sample artefact content (specs only). Pool result. R12 paired-frame STRICT. Awaiting Ruslan ack для launch на server CC.*
