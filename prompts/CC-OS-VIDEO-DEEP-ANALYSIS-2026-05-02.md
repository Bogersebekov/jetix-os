# Brief: 2.5h YouTube Course «Claude Code as OS» — Deep Analysis + Permanent Living Doc

**Run instruction:** server CC, ветка `claude/jolly-margulis-915d34`, Opus 4.7 [1m], `--dangerously-skip-permissions`. **БЕЗ Plan Mode** (это execution + research). Слово `ultrathink` mandatory.

---

## Кто я и кто ты

Я — Ruslan, основатель Jetix OS. Phase 1 €50K Q2 2026, horizon $1T.

Ты — server CC. Сегодня обрабатываешь 2.5h YouTube курс про Claude Code как **операционную систему**. Цель: вытащить **всё** — full transcript + deep analysis + всё через призму текущих гипотез + integration plan + установить **постоянный living doc** который будет развиваться.

## Видение Ruslan-а (verbatim 02.05)

> Есть двух с половиной часовой курс YouTube про то как делать Claude Code операционную систему. Надо прям всю информацию из неё вытащить — по полочкам разобрать, полностью инструкцию создать, весь контекст вытянуть. Перевести в текст — в отдельный документ как анализ. Сделать подробно все инструкции, выписать. Плюс что надо ещё дописать / обработать.
>
> Это всё проанализировать **с точки зрения наших текущих гипотез / критериев / вопросов** — изначально их в начале выписать. Тех которые основные сейчас, которые в последних заметках обсуждались. Берём и соответственно прогоняем этот видос, всё собираем.
>
> Потом всё что можно сразу использовать или что быстро / качественно — тоже добавить как **план внедрения на ближайшее будущее**. Внедряем туда и идём дальше.
>
> Глубокая, качественная, ебейшая инфо. Прям вся инструкция, все инсайты которые только возможны, подсказки, таблицы как улучшать систему. Видео должно быть проработано на 1000%. Потом отдельно как документ — будем **постоянно развивать**. Как «инструкция для системы / улучшение для системы / лайфхаки». Чтобы не потерять — отдельно где-то ещё запиши.

## Что от тебя нужно (6 deliverables)

### 1. Transcript extraction — полный текст видео

**Source:** YouTube URL (Ruslan укажет в командной строке запуска или в /tmp/video-url.txt)

**Method (в порядке предпочтения):**
1. `yt-dlp --write-auto-subs --skip-download --sub-format vtt <URL>` → конвертация vtt → markdown
2. Если auto-subs нет — `yt-dlp -x --audio-format mp3 <URL>` + Groq Whisper (`tools/transcribe.py` шаблон существует)
3. Если URL недоступен — flag explicitly, попроси Ruslan upload file

**Output:** `raw/research/claude-code-os-course-2026-05-02-transcript.md`
- Frontmatter с source URL / duration / extracted timestamp
- Full text с timestamp markers (`[01:23:45]`)
- Speaker tags если несколько голосов

### 2. Deep analysis document

**Файл:** `swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md`

**Структура (≥30K слов если необходимо):**

```markdown
## Executive Summary (≤500 слов)
- Что курс утверждает (3-5 главных тезисов)
- Top 10 actionable techniques
- Top 5 conceptual frames
- Что НЕ сказано / gaps

## §1 Метаданные курса
- Автор / channel / duration / upload date / уровень / target audience

## §2 Структурный outline
- Все секции / chapters / segments курса с timestamps
- Длительность каждой секции
- Ключевые термины введённые

## §3 Все техники / инструкции (по полочкам)
Для КАЖДОЙ техники упомянутой в курсе:
- Название
- Что делает (1-2 предложения)
- Когда использовать
- Точные команды / синтаксис / steps
- Citation: [video:HH:MM:SS-HH:MM:SS]
- Связь с уже известным (CLAUDE.md / agents/ / .claude/skills/ / hooks)

Группировки:
- Setup / configuration techniques
- Workflow techniques
- Memory / context management
- Subagent orchestration
- Hooks / event-driven automation
- MCP / external integrations
- Settings / permissions / security
- Skills / slash commands authoring
- Plan Mode / ultrathink usage
- Multi-CC orchestration (Cloud Cowork patterns)
- Productivity / lifehacks

## §4 Все концептуальные frames (deep insights)
Для каждой conceptual idea:
- Quote / paraphrase
- Citation
- Contradiction or alignment с canonical Jetix concepts (Workshop / TRM / Foundation)
- Implication для нас

## §5 Все таблицы / схемы / cheatsheets
Reproduce verbatim или summarized с citations

## §6 Lens analysis — через призму текущих гипотез

См. §A ниже (current hypotheses list). Для КАЖДОЙ hypothesis:
- Что курс говорит relevant к этой hypothesis?
- Поддерживает / противоречит / нейтрально / orthogonal?
- Какие новые connections / extensions появляются?
- Какие risks/blind-spots появляются?

## §7 Integration plan (что внедрять)

Группировка по приоритету и effort:

### Immediate (сегодня-завтра, <2h каждое)
- Технику Х добавить в .claude/skills/ или CLAUDE.md
- Hook Y настроить
- Скрипт Z создать
- ...

### Near-term (1-2 недели, <8h каждое)
- ...

### Defer / evaluate (требует Ruslan ack или Phase 2+)
- ...

Каждый item:
- Что внедряем
- Где (path / file / setting)
- Почему (хочется / нужно / лайфхак)
- Effort estimate
- Citation на video timestamp
- Status: pending / approved / done

## §8 Что НЕ покрыто курсом, но критично
Gap analysis — что должно быть проработано отдельно

## §9 Open questions для Ruslan
Sequential, не multi-choice

## §10 Provenance index
Таблица claim → video timestamp / external source → verified

## §A Current Hypotheses Snapshot (на момент analysis 02.05)
... см. ниже
```

### 3. Permanent living doc — установка

**Файл:** `swarm/wiki/operations/claude-code-os-mastery.md`

**Это НЕ одноразовый analysis** — это **постоянно развиваемый документ** «инструкция для системы / улучшение / лайфхаки». Каждый раз когда Ruslan находит новый source (видео / статья / hands-on lesson) — обновляем этот файл.

**Skeleton:**
```markdown
---
title: Claude Code OS Mastery — Living Document
status: ongoing
created: 2026-05-02
last_updated: 2026-05-02
sources_processed:
  - 2026-05-02: 2.5h YouTube course «Claude Code as OS» (URL TBD)
type: living_instruction
---

# Claude Code OS Mastery — Living Document

> Постоянно развиваемая инструкция / лайфхаки / techniques для Claude Code как ОС.
> Каждый новый source extract'ится сюда (с date + citation).
> Не canonical / не LOCKED — evolves.

## §0 Quick reference index
- Setup → §1
- Workflow → §2
- Memory → §3
- Subagents → §4
- Hooks → §5
- MCP → §6
- Skills → §7
- Plan Mode → §8
- Multi-CC → §9
- Lifehacks → §10

## §1 Setup & Configuration
... (filled from current course + future sources)

## §2 Workflow patterns
...

## §3 Memory & Context Management
...

## §4 Subagent Orchestration
...

## §5 Hooks & Automation
...

## §6 MCP & External Integrations
...

## §7 Skills / Slash Commands Authoring
...

## §8 Plan Mode / ultrathink
...

## §9 Multi-CC Orchestration (Cloud Cowork patterns)
...

## §10 Productivity Lifehacks
...

## §11 Anti-patterns / Don't do
...

## §12 Sources processed
- 2026-05-02: 2.5h YouTube course — full analysis в `swarm/wiki/synthesis/claude-code-os-analysis-2026-05-02.md`
```

При первом fill — заполнить из текущего курса. При последующих sources — append с date markers.

### 4. CLAUDE.md / Skills updates (Phase Immediate)

Если в курсе есть techniques которые **точно стоит внедрить immediately** (≥0.9 confidence + low risk):
- Update `CLAUDE.md` с new section / rule
- Create `.claude/skills/<new-skill>.md` если новая skill
- Modify `.claude/agents/<id>/system.md` если update agent system prompt

**Rule:** не делать changes автоматически — **predloить в integration plan §7 Immediate, Ruslan approve, потом merge**.

### 5. Notion mirror

**После Phase E commit** — обновить Notion-страницу [🎓 CC as OS deep analysis](https://www.notion.so/3542496333bf...) (Ruslan создаст до запуска) с:
- Link на repo files
- Top 10 techniques
- Top 5 frames
- Top 10 integration items с приоритетами

### 6. Final summary в чат

После Phase E — summary ≤500 слов:
- Top 10 techniques (1 line each)
- Top 5 frames (1 line each)
- Lens findings (1 line per hypothesis: support/contradict/extend)
- Top 10 integration items (Immediate / Near-term / Defer)
- Top 5 «aha-moments» (что surprised тебя)
- 3-5 open questions Ruslan'у

---

## §A Current Hypotheses Snapshot (для Lens Analysis §6)

Lens через каждую из этих:

### A.1 Workshop concept (LOCKED 30.04)
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- Jetix = «мастерская для работы с информацией»; adaptable станки; владелец adaptive role; input/output = информация; 3 фазы (1 владелец → команда → community); Visual/View principle (программа = код, Jetix = visual editor)

### A.2 TRM business model (LOCKED 30.04)
- `decisions/JETIX-TRM-MODEL-2026-04-30.md`
- 6 ресурсов (финансы / время / аудитория / знания / **compute** / команда); лестница L0-L5 (€3K → €40-60K/мес); 3 фазы → платформа €1.5-3 млрд valuation; 7 слоёв защиты от disintermediation

### A.3 Plan Mode + ultrathink + 402 books grounding (PILOT, AWAITING ACK 30.04)
- `swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md`
- Methodology «AI как консалтинг-команда» — selection algorithm + 5-15 books-grounded plans per кейс; provenance ≥0.95; 8 test cases (3 classical + 5 Jetix); 4-6 weeks pilot; verdict scale/pivot/drop

### A.4 Malware-inspired partnership + 10/10 contract (DRAFT 02.05)
- `swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md`
- Worm/virus/trojan/spy mechanics → legitimate partnership structures; 10/10 (10% perf fee + 10% mandatory reinvestment); §307 BGB high risk; sensitivity threshold 70% acceptance; 4 variants (A Lite-7/7 / B Operator Worm / C Useful Spy 0/20 / D Spotlight Worm + ROFR)

### A.5 Abstraction levels in management (RAW 02.05)
- Notion 3542496333bf81cb9e15d7b49410db73 (`memory/idea_abstraction_levels_management.md`)
- Assembly→C→Python→DSL→LLM→visual stack mapping → management levels; subsidiarity (4 criteria); связь с Workshop §7 Visual/View

### A.6 CPU + Memory analog для Jetix (RAW 02.05)
- Same Notion (extension §6)
- 4 levels evolution: founder solo (single-core) → founder+Jetix (multi-core+GPU/NPU+SSD+RAM) → Phase 2 datacenter → Phase 3 cloud platform; 14 computing concepts → business analogs; «компьютер для управления бизнесом» frame

### A.7 Voice extraction → Workshop people (DRAFT 01.05, AWAITING walkthrough)
- `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
- 12 CRM voice-router DRAFTs новых людей упомянутых в заметках; pending Ruslan walkthrough

### A.8 Foundation v1.0 (LOCKED 28.04)
- `swarm/wiki/foundations/part-{1..11}/architecture.md` + Pillar C
- 11 LOCKED Parts; F-G-R schema; Default-Deny; Halt-Log-Alert; Phase B trigger predicate

### A.9 Phase 1 €50K Q2 2026 commitment
- Solo founder + 12 legacy + 6 ROY swarm
- 8 active projects (`CLAUDE.md`)

### A.10 Workshop concept depths (in progress)
- `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md`
- Deep system narrative через workshop frame (≥8K слов target)

**Lens questions per hypothesis (apply to KAЖДОЙ):**
1. Курс **поддерживает** ли эту hypothesis? Какие конкретные techniques/frames support'ят?
2. Курс **противоречит** ли? Где tension / contradiction?
3. Курс **расширяет** ли? Какие новые dimensions появляются?
4. **Blind spot** — что курс ПРОПУСКАЕТ что нам критично?
5. **Integration vector** — какая техника из курса apply'ит к этой hypothesis для immediate use?

---

## Hard rules

1. **ultrathink** mandatory — это deep extraction, не surface skim
2. **Provenance ≥0.95** — каждое утверждение с timestamp citation `[video:HH:MM:SS]` или external source
3. **Russian primary** prose, English code/configs, мат preserve если в video quotes
4. **No solo-founder downgrade** — baseline enterprise + $1T trajectory
5. **AI = scribe для strategic** — extract + analyze + structure, **НЕ диктуй** «Jetix должен принять X»
6. **Beta-first** — достаточно-хороший v1, не perfectionism. Скорость > полировка.
7. **No multi-choice опросы** — конкретные questions если нужен Ruslan input
8. **Не делай automatic changes в CLAUDE.md / .claude/skills/ / .claude/agents/** — propose в integration plan §7, Ruslan approves
9. **Living doc updates additive** — не перезаписывай предыдущие sources, append с date markers
10. **Honest flag** для unverified claims — если video не покрывает аспект, не выдумывай

## Workflow

1. **Phase A — Transcript extraction** (15-30 min)
   - yt-dlp / Whisper / manual depending on source
   - Output: `raw/research/claude-code-os-course-2026-05-02-transcript.md`

2. **Phase B — Structural outline** (15 min)
   - Sections / timestamps / key terms

3. **Phase C — Deep extraction** (60-90 min)
   - Все techniques (§3)
   - Все frames (§4)
   - Все таблицы/cheatsheets (§5)

4. **Phase D — Lens analysis** (30-60 min)
   - 10 hypothesis lenses через course content

5. **Phase E — Integration plan** (30-45 min)
   - Immediate / Near-term / Defer triage
   - Concrete actions с paths + effort

6. **Phase F — Permanent living doc установка** (15-30 min)
   - `swarm/wiki/operations/claude-code-os-mastery.md` skeleton + initial fill

7. **Phase G — Commit + push** (5 min)
   - Multiple commits для clean history

8. **Phase H — Summary в чат** (5 min)
   - ≤500 слов

**Total estimate:** 3-4.5 hours.

## Inputs (pre-load)

**YouTube course:**
- URL: см. `/tmp/cc-os-video-url.txt` (Ruslan создаст перед запуском) или command line param

**Canonical Jetix concepts (для lens analysis):**
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- `decisions/JETIX-TRM-MODEL-2026-04-30.md`
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- `swarm/wiki/foundations/part-{1..11}/architecture.md` + `principles/architecture.md`
- `swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md`
- `swarm/wiki/synthesis/malware-partnership-analysis-2026-05-02.md`
- `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
- `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md` (если уже есть)

**Current operational state:**
- `CLAUDE.md` (root)
- `.claude/skills/` (existing skills)
- `.claude/agents/` (12 legacy + 6 ROY swarm)
- `.claude/settings.json`

**Memory:**
- `memory/MEMORY.md` + все ссылки

**Methodology articles (existing):**
- `raw/articles/2026-04-29-claude-code-best-practices/{ultrathink,plan-mode,README}.md`

## Out of scope

- Не trogai canonical Foundation Parts / Vision / Workshop / TRM (только reference)
- Не пиши Plan Mode pilot artefacts (пилот отложен)
- Не make automatic changes в CLAUDE.md без Ruslan ack
- Не дублируй existing methodology articles — extend / cross-reference
- Не делай Pricing / sales / marketing strategy — out of scope (это про CC techniques)

---

ready? Жди URL video от Ruslan'а в `/tmp/cc-os-video-url.txt` или CLI param. Когда URL есть — начинай Phase A. Все 8 phases sequential. ultrathink mandatory throughout. После Phase G — summary в чат.
