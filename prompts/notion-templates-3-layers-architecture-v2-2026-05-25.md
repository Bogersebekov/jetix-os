---
title: Notion Templates 3-Layers Architecture v2 — упрощённая standalone-capable + AI Tools mega-page
date: 2026-05-25
type: server-cc-autonomous-prompt
prompt_class: strategic-synthesis-notion-architecture-3-layers-v2
supersedes: prompts/notion-templates-4-layers-architecture-2026-05-25.md (v1)
output_main_doc: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
output_reports_dir: reports/notion-templates-3-layers-architecture-v2-2026-05-25/
output_mega_page: decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md
F: F2-F3
G: prompt-notion-templates-3-layers-architecture-v2-2026-05-25
R: refuted_if_over_engineered_OR_3_layers_not_standalone_OR_jetix_specific_in_layer_3_base_OR_lt_3_layers_OR_lt_15_ai_tools_OR_lt_7_mermaid_OR_LOCK_modified_OR_sample_data_content_OR_auto_launch_consequent
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
roy_dispatch_target: brigadier + project-brigadier + mgmt-expert + engineering-expert + systems-expert + philosophy-expert + investor-expert + methodology-engineer + recruitment-dynamics-expert + influence-ethics-expert (R12 AUTO-FIRE) + nlp-expert (R12) + gamification-engagement-expert (R12 AUTO-FIRE) + sota-tracker-expert + ml-ai-foundations-expert
language: russian primary
style_anchor: PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md + PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md + DOCS-CLASSIFICATION-2026-05-25.md
mode: 3-LAYERS COMPREHENSIVE ARCHITECTURE V2 (упрощённая + standalone-capable + 3 layers вместо 4 + AI Tools mega-page добавлено)
mermaid_target: 7-9 schemes ARCH-V2-1..ARCH-V2-9
status: READY-TO-EXECUTE
runtime_target: 4-5h autonomous
audience_primary: любой founder/executive любого бизнеса для Layer 3 + смешанный для Layer 1 (single user) + Layer 2 (team)
---

# 🏛️ Notion Templates 3-Layers Architecture v2 — SIMPLIFIED + STANDALONE + AI Tools

## §0 КРИТИЧНО — что изменилось vs v1 (read first)

**Per Ruslan voice feedback 25.05 evening — v2 принципиально проще + структурно другой чем v1:**

### Главные изменения

1. **3 layers вместо 4** — Layer 2 Personal Expanded **УДАЛЁН** (потом сделаем отдельным «инструменты + полезные skills» слоем в другой итерации, **не в этом run'е**).

   Финальные 3 layers:
   - **Layer 1: Personal Core** (single user)
   - **Layer 2: Team Collaboration** (multi-user — было Layer 3 в v1)
   - **Layer 3: Universal Business Foundation** (любой бизнес — было Layer 4 в v1)

2. **STANDALONE mandate** — каждый из 3 layers можно взять **отдельно**, не обязательно вместе. Но fast-connect mechanics продумать (если человек захочет соединить Layer 1 + Layer 3 = founder personal daily + business management вместе) — НЕ обязательно, опция.

3. **SIMPLIFICATION mandate** — Ruslan voice «слои интересно, а внутри шаблоны так вообще пиздец блять настолько задрочено, ну как бы нахуй такое надо. Максимально просто для первых этапов, потом можно усложнять». Каждая DB — **минимум полей baseline** + отдельный sidebar «🔧 Что можно ещё добавить» (как инструкция). NOT 50+ полей per DB.

4. **Jetix-specific вещи УБРАТЬ из Layer 3 base** — раньше §5.X overlay был внутри Layer 3 deliverable. Теперь Layer 3 = clean universal foundation БЕЗ Jetix overlay. Jetix overlay будет в **отдельной будущей итерации** (упомянуть как «следующий слой опционально», не делать сейчас).

5. **Layer 2 (Team Collaboration) — generic + Jetix overlay КАК ОТДЕЛЬНЫЙ ШАБЛОН**. Generic Team Collaboration = clean (без R12 / Mondragón / 10 наших ролей в base). Jetix overlay = отдельный fork-able template поверх. Plus pattern «как blogger/brand/corporation adaptировать под себя» (replace Jetix-specific rules своими).

6. **NEW: AI Tools & Lifehacks Mega-page** — отдельный document со списком инструментов которые помогают быстрее работать с информацией (Telegram→Wiki processor / Mermaid quick / Miro для схем / 15+ tools). Surface'ить тоже из нашей системы что ещё полезного.

### Per-layer specific changes (см. detail в Phases)

- **Layer 1 Personal Core:**
  - Daily Log: **ADD** цель дня + реально сделано + deep work minutes + day type (production/development/recovery/orientation) + template дня (цели + точка А→Б + место для подстраниц-черновиков) + wrap-of-day template/CC-command
  - Knowledge: **ADD** «посмотреть позже / фильтр информации» (saved-for-later)
  - Goals: **поднять в strategic layer** — не просто база, а отдельный документ + точка А→точка Б + место для них
  - **ADD baseline в Layer 1**: Weekly review template + Monthly review template (чтобы место под проекты + гипотезы + дневную отчётность подтягивалось)
  - Остальное (Projects / Tasks / Ideas / Contacts / Hypotheses / Life pulse / Финансы / Views) — keep, упростить

- **Layer 2 Team Collaboration (бывший Layer 3 v1):**
  - 10 ролей / Project Catalog / Skills marketplace / 4 monetization / Charter / Daily CC / Stage Gates / Permissions / External / Onboarding 1-week + анти-секта — всё **OK по содержанию, упростить implementation**
  - **NEW: Generic version (без Jetix-specific 10 ролей / R12 / Mondragón)** — clean Team Collaboration baseline для любой команды
  - **NEW: Jetix-specific overlay = ОТДЕЛЬНЫЙ template** поверх generic (10 ролей наши + R12 + Mondragón + Stage Gates)
  - **NEW: Blogger/Brand/Corporation adaptation pattern** — как заменить Jetix-specific rules на свои

- **Layer 3 Universal Business Foundation (бывший Layer 4 v1):**
  - 12 generic DBs (Strategy/Goals / Financial / Team / Projects / CRM / Decisions / Risks / Compliance / Tools / Docs / Briefing / Crisis) — **keep, упростить**
  - **ADD: Hypotheses DB** в Layer 3 base (как минимум)
  - **ADD: Vision + Goals страницы** (не только DB — отдельные страницы с описанием зачем, удобненько)
  - **REMOVE §5.X Jetix overlay** — убрать из Layer 3 base (move в отдельную будущую итерацию, упомянуть briefly как «next iteration»)
  - **ADD: Layer 1 ↔ Layer 3 fast-connect mechanic** (если founder хочет personal daily + business management together)

- **NEW SEPARATE DELIVERABLE: AI Tools & Lifehacks Mega-page** (отдельный document)

---

## §17.0 ⭐⭐⭐ CRITICAL IMPORTANCE MANDATE (MAX-density + SIMPLIFICATION)

> Per memory `feedback_max_density_max_tokens.md` + Ruslan voice 25.05 evening.

Этот deliverable = **финальная упрощённая фиксация архитектуры**. ROY 500% на quality, но не на over-engineering. Density = clarity + completeness, НЕ количество полей per DB.

1. **Density для:** explanations / examples / mermaid / cross-layer mechanics / standalone capability rationale / AI tools list
2. **Simplicity для:** per-DB schemas (minimum baseline + "что можно добавить" sidebar отдельно)
3. **ROY swarm на 500%** — full dispatch на architecture work, но per-DB schemas keep simple
4. **Use MAX tokens × 3** — для cross-layer + standalone mechanics + AI Tools mega-page
5. **Максимально сырая information** — read FULL v1 prompt + v1 partial output если есть + Personal OS Plan + Team OS Plan + Platform Lifecycle + DOCS-CLASSIFICATION
6. **Concrete examples mandatory** per layer — простые worked examples (НЕ over-detailed)
7. **«Всё что только можно натянуть»** — applies к AI Tools mega-page + cross-layer mechanics, НЕ к per-DB field bloat
8. **Не stopover at minimum** — но minimum = clean simple baseline, дополнительно = в sidebar

---

## §1 3 Layers (canonical для v2)

- **Layer 1: Personal Core** — индивидуальный пользователь. Управление жизнью / идеями / проектами / гипотезами / контактами / финансами. Daily Log с CC-augmented wrap. Weekly+Monthly review templates. **Standalone-capable.**
- **Layer 2: Team Collaboration** — multi-tenant overlay для совместной работы. **Generic version baseline** + **Jetix-specific overlay (отдельный template)**. Blogger/Brand/Corporation adaptation pattern. **Standalone-capable** (любая команда без Personal OS под капотом).
- **Layer 3: Universal Business Foundation** — fork-able foundation для управления **любым** бизнесом (consulting/SaaS/agency/cooperative). 12 generic DBs + Hypotheses + Vision/Goals страницы. **Standalone-capable.** Jetix overlay = next iteration (НЕ в этом run'е).

**Plus отдельный sub-deliverable:** AI Tools & Lifehacks Mega-page.

---

## §2 Phases (14 phases, 0-13)

### Phase 0 — FPF lens scope + substrate read (включая v1 partial если есть)
- Apply FPF lens: «Notion layer = что в FPF terms?» (system / sub-system / artefact)
- Full substrate read: v1 prompt + v1 partial output (если есть commit'ы от старого run'а) + Personal OS Plan + Team OS Plan + Platform Lifecycle + DOCS-CLASSIFICATION + PARTNER-OFFERING
- Define **STANDALONE-capable** architecture principle (каждый layer работает один — fast-connect optional)
- Define **SIMPLIFICATION** principle (baseline simple + extension instructions sidebar)

**Output:** `reports/notion-templates-3-layers-architecture-v2-2026-05-25/01-fpf-lens-scope.md` (~1-2K)
**Commit:** `[notion-arch-v2] Phase 0 FPF lens + substrate read`

---

### Phase 1 — 3 Layers overview + STANDALONE + fast-connect

**Tasks:**
- 3 layers stack visualization (Layer 1 / Layer 2 / Layer 3 — standalone-capable each)
- Cross-layer fast-connect mechanics (если хочешь connect — как; если не хочешь — каждый работает один)
- Per-layer audience portrait
- Per-layer fork-friendly notes
- Mermaid ARCH-V2-1: 3 layers standalone + fast-connect optional
- Mermaid ARCH-V2-2: cross-layer fast-connect mechanics

**Output:** `.../02-overview-3-layers-standalone.md` (~2-3K)
**Commit:** `[notion-arch-v2] Phase 1 overview 3 layers + standalone + fast-connect`

---

### Phase 2 — 🟢 Layer 1 Personal Core REVISED (simplified + Daily Log enhancements + Reviews)

**Tasks — simplified baseline + extensions sidebar:**

#### Baseline DBs (Layer 1 core):
- **Daily Log DB** — REVISED:
  - Date / Energy / Linked Project / People / Hypothesis / Ideas (keep)
  - **ADD: Цель дня** (text)
  - **ADD: Реально сделано за день** (text)
  - **ADD: Deep work minutes** (number)
  - **ADD: Day type** (select: production / development / recovery / orientation)
  - **DROP: Day of week / Week number** (формулы могут вычислить если надо)
  - **Template дня (NEW critical):** структура страницы дня — цели + точка А→Б по шагам + место для подстраниц-черновиков (нативные Notion subpages)
  - **Wrap-of-day template/CC-command (NEW critical):** автоматическая отчётность в конце дня по ключевым параметрам — CC за день делает analysis + предложения по проектам, человек ack'ает (DRAFT-only per voice-pipeline pattern)
- **Projects DB** — simplified base
- **Tasks DB** — simplified base
- **Ideas DB** — simplified base
- **Goals DB** — moved to **Strategic Layer** sub-section (см. ниже)
- **Contacts DB** — simplified base
- **Knowledge DB** — REVISED: **ADD «Saved-for-later» field** (filter «посмотреть позже»)
- **Hypotheses DB** — simplified base (Method V2 §J users)
- **Life Pulse DB** — simplified base
- **Финансы DB** — opt-in, simplified

#### NEW: Strategic Layer (sub-section внутри Layer 1)
- **Vision document** (страница, не DB — текст)
- **Goals strategic document** (страница + ссылки на Goals DB)
- **Точка А → Точка Б** место (отдельная страница per current direction)
- Schema goals OK как есть, но **поднята из «просто DB» до strategic document level**

#### NEW: Weekly + Monthly Review Templates
- **Weekly review template** (каждое воскресенье — что сделано / что не / cycles / hypothesis updates / next week)
- **Monthly review template** (каждый месяц — projects review / goals progress / financial pulse / contacts touch audit)
- Auto-pulls из существующих DBs (через linked views)

#### Views — keep (из v1)

#### 🔧 Sidebar «Что можно добавить» (отдельная страница):
- Дополнительные analytics views
- Advanced hypothesis tracking (бывший Layer 2 Personal Expanded substance перенесён в инструкции — не в base)
- AI integration helpers
- Personal wiki expansion
- И т.д.

**Phase 2 ≥3-4K words (simplified — не 5K как раньше).**

**Output:** `.../03-layer-1-personal-core-revised.md`
**Commit:** `[notion-arch-v2] Phase 2 Layer 1 Personal Core REVISED (simplified + Daily enhancements + Reviews + Strategic sub)`

---

### Phase 3 — 🔵 Layer 2 Team Collaboration REVISED (Generic baseline + Jetix overlay separate + Brand pattern)

**Tasks:**

#### Part A — Generic Team Collaboration baseline
- 10 generic roles slots (не привязанных к Jetix terminology — user заполняет под свою команду; provide template categories: leader / contributor / advisor / observer / financial / customer-facing / etc.)
- Project Catalog DB simplified
- Skills/Needs marketplace simplified
- Charter slot (textual — user fills)
- Monetization templates universal (4 generic categories: revenue share / capital partnership / membership / IP licensing)
- Daily/Weekly team briefing (without CC-specific implementation — generic)
- Stage Gates simplified (SG-1..SG-4 generic — user defines criteria)
- Permissions matrix simplified
- External people slot
- Onboarding 1-week sequence generic
- **Анти-секта principles** (keep universally applicable — это generic best practice anti-extraction, не Jetix-specific)

#### Part B — Jetix-specific Team Collaboration OVERLAY (отдельный template поверх generic)
- 10 Jetix roles (PM / Inv-Cap×3 / Contributor / Advisor / Facilitator / Mentor / Observer / Steward)
- R12 4 RUSLAN-LAYER action classes integration
- Mondragón 5:1 enforcement formulas
- 4 Jetix monetization templates (стандарт / капитал / когорта €1500 / IP)
- Charter с 6 секций + R12 чек-лист
- Stage Gates Jetix-specific SG-1..SG-4 criteria
- Daily CC pass с Jetix-specific 5 секций briefing
- Cross-cite к Foundation Part 11 + Pillar C R12 + Economic V10

#### Part C — Brand/Blogger/Corporation Adaptation Pattern
- Pattern «как заменить Jetix-specific rules своими»
- 3 worked examples:
  - Blogger team (creator + assistants + collaborators): swap roles / monetization template
  - Corporate department: swap to corporate hierarchy
  - Startup co-founders: swap to equity-based partnership
- «Где Jetix overlay полезен сам по себе» vs «где fork полностью»

**Phase 3 ≥5K words (Generic + Jetix overlay + Brand pattern split).**

**Output:** `.../04-layer-2-team-collaboration-revised.md`
**Commit:** `[notion-arch-v2] Phase 3 Layer 2 Team Collaboration REVISED (Generic + Jetix overlay separate + Brand adapt) (R12 AUTO-FIRE на Jetix overlay)`

---

### Phase 4 — 🟠 Layer 3 Universal Business Foundation REVISED (simplified + Hypotheses + Vision/Goals страницы + L1↔L3 connect)

**Tasks — 12 generic DBs (упрощённые) + ADDs:**

#### Existing 12 generic DBs (per v1 spec, simplified — minimum baseline + sidebar):
1. Strategy & Goals (generic, без OKR-as-our-framework)
2. Financial Overview (generic)
3. Team / People (generic, slots для roles)
4. Projects Portfolio (generic)
5. Stakeholders / CRM lite (generic)
6. Decisions Log (generic)
7. Risks Register (generic)
8. Compliance & Legal (generic)
9. Tools Inventory (generic)
10. Documents / Knowledge Hub (generic)
11. Executive Daily/Weekly Briefing (generic)
12. Crisis Mode Playbook (generic)

#### NEW: Hypotheses DB (как минимум)
- Hypothesis title / type / status / metric / horizon / outcome
- Simple baseline — extension instructions sidebar для Method V2 §J users

#### NEW: Vision / Mission / Goals страницы (не только DB)
- **Vision document** (текстовая страница с описанием — зачем существует бизнес)
- **Mission document** (страница)
- **Goals strategic narrative** (страница связанная с Strategy & Goals DB — описание goals удобненько prose)
- Per-страница: «Зачем эта страница / как обновлять / когда ревизировать»

#### NEW: Layer 1 ↔ Layer 3 fast-connect mechanic
- Если founder хочет personal daily (Layer 1) + business management (Layer 3) together:
  - Linked view Daily Log → Briefing
  - Linked view Goals → Strategy & Goals
  - Linked view Projects (personal scope) → Projects Portfolio (business scope)
  - Permissions: founder sees both / others see only Layer 3
- Если не хочет — каждый layer работает один (no auto-merge)

#### REMOVE: §5.X Jetix overlay (из Layer 3 base)
- Brief mention в §5.X-DEFERRED: «Jetix-specific overlay для Layer 3 — будет в следующей итерации, отдельно».

**Phase 4 ≥4-5K words (simplified vs v1 ≥7-8K).**

**Output:** `.../05-layer-3-universal-business-foundation-revised.md`
**Commit:** `[notion-arch-v2] Phase 4 Layer 3 Universal Business Foundation REVISED (simplified + Hypotheses + Vision pages + L1↔L3 connect; Jetix overlay deferred)`

---

### Phase 5 — 🤖 NEW: AI Tools & Lifehacks Mega-page

**Tasks — отдельный sub-deliverable (отдельный document):**

#### Sections:
1. **Назначение страницы** (one-paragraph — зачем эта страница)
2. **15+ AI tools / lifehacks для работы с информацией:**

   **Capture & Process:**
   - 📱 **Telegram заметки processor** → автозанос в Wikipedia (voice / text → structured entry)
   - 🎙️ **Voice notes pipeline** (Wispr Flow / etc. → transcript → structured items)
   - 📥 **Mistral OCR pipeline** (PDF / scan → searchable MD)
   - ✂️ **Web clipper** (browser extension → Notion saved-for-later)

   **Visualize & Communicate:**
   - 📊 **Mermaid quick setup** (CC просьба → автоматом visualization)
   - 🎨 **Miro / Mural** для схем + общения с людьми (быстро рисовать)
   - 🖼️ **Excalidraw embed** в Notion (для quick sketches)
   - 📈 **Notion native charts** (после Notion AI updates)

   **Synthesize & Decide:**
   - 🧠 **Claude / GPT для synthesis** (готовые prompts — review / decision / brainstorm)
   - 🔍 **OFFLINE_MODE structured-excerpt** (`/ask` skill pattern — без inference fluff)
   - 💡 **Hypothesis tracker** (Method V2 §J — Bayesian-lite updates)
   - 🗂️ **Wiki ingest** (новый источник → wiki/concepts + log + edges)

   **Coordinate & Track:**
   - 🤖 **ROY swarm для multi-perspective analysis** (engineering / investor / mgmt / philosophy / systems)
   - 📅 **CRM voice integration** (voice → draft contact entries → manual promote)
   - ⏱️ **Toggl pipeline** (auto entries от ActivityWatch)
   - 📊 **ActivityWatch timeline** (daily report для self-review)

   **Plus 3-5 более:**
   - **Tools brainstorm от системы** — surface tools from CLAUDE.md skills (54), tools/ (30+), .claude/skills, etc.
   - **Mistral OCR books** (raw books → searchable MD)
   - **Schema validation / lint** (для consistency)
   - **Mermaid validation tool** (для diagrams reliability)
   - **AI-augmented review** (CC reads daily logs → wrap-of-day suggestions)

3. **Per tool — для каждого:**
   - Что делает (1-2 предложения)
   - Как использовать (quick start)
   - Когда использовать
   - Где живёт в системе Jetix (если есть link)

4. **Discovery section** — «как находить новые tools» (Twitter / Hacker News / Reddit / community recommendations)

#### Output destination
- Отдельный sub-document: `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md`
- Не в main `NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2`, отдельный standalone

**Phase 5 ≥3-4K words.**

**Output:** `.../06-ai-tools-lifehacks-mega-page.md` (для reports archive) + `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md` (main mega-page)
**Commit:** `[notion-arch-v2] Phase 5 AI Tools & Lifehacks Mega-page (NEW)`

---

### Phase 6 — 🔄 Cross-layer mechanics (data flows + permissions + sync + STANDALONE emphasis)
- 3 layers data flows (Layer 1 ↔ Layer 2 ↔ Layer 3 — все optional)
- Permissions matrix simplified (без Jetix-specific 10 ролей в base)
- Sync mechanics (Notion native: linked DBs / synced blocks / shared views)
- **STANDALONE deep emphasis** — каждый layer работает один; fast-connect = opt-in feature, не дефолт
- Mermaid ARCH-V2-3: data flows
- Mermaid ARCH-V2-4: permissions matrix

**Phase 6 ≥2-3K words.**

**Output:** `.../07-cross-layer-mechanics.md`
**Commit:** `[notion-arch-v2] Phase 6 cross-layer mechanics + STANDALONE`

---

### Phase 7 — 🚀 Per-layer onboarding sequence (revised для 3 layers)
- Layer 1 onboarding: solo user — fork → adapt → use в ≤30 мин
- Layer 2 onboarding: team setup → invite → 1-week observation→small task→role
- Layer 3 onboarding: founder setup → connect existing DBs → first executive briefing
- Per-layer buddy / docs / video helpers
- Layer 1↔3 connect onboarding (если выбран): добавочный шаг setup

**Phase 7 ≥2K words.**

**Output:** `.../08-per-layer-onboarding.md`
**Commit:** `[notion-arch-v2] Phase 7 per-layer onboarding`

---

### Phase 8 — 🍴 Fork-friendly mechanics + R12 (revised для 3 layers)
- Layer 1: fork → copy → adapt → use без association
- Layer 2: fork → swap Jetix overlay на свой / use generic baseline / use Brand pattern
- Layer 3: fork → adapt под свой бизнес / Jetix overlay opt-in next iteration
- R12 enforcement applicable ТОЛЬКО к Jetix overlay (Layer 2 Part B). Generic baselines = clean без R12-specifics
- Universal R12 best practices (anti-extraction / fork-and-leave / Mondragón-aware) упомянуть как «полезно для cooperative organizations» — не enforce на generic

**Phase 8 ≥2K words.**

**Output:** `.../09-fork-friendly-R12.md`
**Commit:** `[notion-arch-v2] Phase 8 fork-friendly + R12 mechanics (revised)`

---

### Phase 9 — 📅 Implementation roadmap (revised)
- Per-layer implementation order (standalone OR connected)
- Layer 1 first (most foundational + most users — Дмитрий-trial start)
- Layer 3 minimum second (founder personal use case)
- Layer 2 demo overlay third (team co-design с 1 партнёром)
- AI Tools mega-page parallel (можно сразу как companion document)
- Notion plan upgrade decisions per layer needs

**Phase 9 ≥2-3K words.**

**Output:** `.../10-implementation-roadmap.md`
**Commit:** `[notion-arch-v2] Phase 9 implementation roadmap revised`

---

### Phase 10 — ⚖️ R12 paired-frame sweep (только applicable layers)
- Layer 1: low R12 risk (single user, only privacy/data export)
- Layer 2 Generic: low-medium (team collaboration baseline)
- Layer 2 Jetix overlay: HIGH (monetization + roles + cohort dynamics)
- Layer 3 generic: low (executive view сама по себе not extractive)
- 8 paired-frame questions applied per layer where applicable
- AUTO-FIRE influence-ethics + recruitment-dynamics + nlp + propaganda + gamification на Layer 2 Jetix overlay

**Phase 10 ≥2K words.**

**Output:** `.../11-r12-sweep.md`
**Commit:** `[notion-arch-v2] Phase 10 R12 sweep (Layer 2 Jetix overlay AUTO-FIRE)`

---

### Phase 11 — 📐 Architecture mermaid suite (7-9 schemes ARCH-V2-1..ARCH-V2-9)
- ARCH-V2-1: 3 layers stack standalone-capable
- ARCH-V2-2: cross-layer fast-connect optional
- ARCH-V2-3: data flows
- ARCH-V2-4: permissions matrix
- ARCH-V2-5: Layer 2 generic vs Jetix overlay split
- ARCH-V2-6: implementation timeline
- ARCH-V2-7: AI Tools mega-page hub
- ARCH-V2-8: R12 risk overlay (только Layer 2 Jetix overlay)
- ARCH-V2-9: master synthesis (3 layers + AI Tools companion)

**Phase 11 ≥2-3K words.**

**Output:** `.../12-mermaid-suite.md`
**Commit:** `[notion-arch-v2] Phase 11 mermaid suite ARCH-V2-1..ARCH-V2-9`

---

### Phase 12 — 📄 Main consolidated + 00-SUMMARY + per-layer matrix + INDEX
- Main doc `decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md` ~20-25K plain Russian (меньше v1 35K — simplified):
  - §0 TL;DR + что изменилось vs v1
  - §1 3 layers overview + STANDALONE
  - §2 Layer 1 Personal Core REVISED (compressed)
  - §3 Layer 2 Team Collaboration REVISED (compressed — Generic + Jetix overlay + Brand pattern)
  - §4 Layer 3 Universal Business Foundation REVISED (compressed)
  - §5 AI Tools mega-page reference + link
  - §6 Cross-layer mechanics + STANDALONE emphasis
  - §7 Onboarding + fork-friendly + implementation roadmap (compressed)
  - §8 R12 sweep summary
  - §9 7-9 mermaid ARCH-V2-1..ARCH-V2-9 inline
  - §10 Per-layer matrix table (quick reference)
  - §11 10-15 R1 decisions queue
  - §12 Cross-refs + к чему ведёт
- 00-SUMMARY ≤1000w
- AI Tools mega-page = separate file `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md`

**Output:** main + summary + INDEX + AI Tools mega-page
**Commit:** `[notion-arch-v2] Phase 12 Main + SUMMARY + per-layer matrix + INDEX + AI Tools mega-page (final push)`

---

### Phase 13 — 🗑️ Deprecation v1 prompt (housekeeping)
- Add deprecation note в v1 prompt file (`prompts/notion-templates-4-layers-architecture-2026-05-25.md`):
  - Add YAML frontmatter field `status: DEPRECATED-SUPERSEDED-BY-V2`
  - Add note в §0 about v2 supersession
- If v1 partial output exists (`reports/notion-templates-4-layers-architecture-2026-05-25/`) — keep per append-only, mark folder как deprecated в README internal

**Output:** v1 prompt updated with deprecation note + reports README if applicable
**Commit:** `[notion-arch-v2] Phase 13 v1 deprecation housekeeping`

---

## §3 Output structure

```
decisions/strategic/
├── NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md   # main ~20-25K + 7-9 mermaid
└── AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md                # standalone sub-deliverable ~3-4K

reports/notion-templates-3-layers-architecture-v2-2026-05-25/
├── 00-SUMMARY-FOR-RUSLAN.md
├── 01-fpf-lens-scope.md
├── 02-overview-3-layers-standalone.md
├── 03-layer-1-personal-core-revised.md
├── 04-layer-2-team-collaboration-revised.md
├── 05-layer-3-universal-business-foundation-revised.md
├── 06-ai-tools-lifehacks-mega-page.md (archive ref)
├── 07-cross-layer-mechanics.md
├── 08-per-layer-onboarding.md
├── 09-fork-friendly-R12.md
├── 10-implementation-roadmap.md
├── 11-r12-sweep.md
├── 12-mermaid-suite.md
└── diagrams/_INDEX.md
```

---

## §4 Style anchors

- PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md — plain Russian conversational
- PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md — Build/Run/Scale alignment
- DOCS-CLASSIFICATION-2026-05-25.md — 4 категории baseline
- PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md — Layer 1 baseline
- TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md — Layer 2 baseline
- v1 prompt (`prompts/notion-templates-4-layers-architecture-2026-05-25.md`) + v1 partial output если есть — DELTA reference

---

## §5 Constitutional reminder

| Rule | Application |
|---|---|
| R1 surface only | Variants + facts; Ruslan picks final |
| R2 STRICT | Foundation paths untouched |
| R6 | F-G-R triple + cross-cite к substrate |
| R11 | NO auto-actions; NO Notion API; NO sample real data |
| R12 paired-frame STRICT | Только Layer 2 Jetix overlay = AUTO-FIRE influence-ethics + recruitment-dynamics + nlp + propaganda + gamification |
| IP-1 STRICT | Roles abstract; names = RUSLAN-LAYER examples |
| Append-only | New files only |
| Pool result | NO auto-launch consequent prompts |
| F2-F3 derivative | NO new external research |
| SIMPLIFICATION mandate | Per-DB baseline minimum + «что добавить» sidebar отдельно |
| STANDALONE mandate | Каждый layer работает один; fast-connect = opt-in |

---

## §6 К чему ведёт после прогона (~4-5h autonomous)

1. Ruslan reads SUMMARY → main → AI Tools mega-page → drill-down phases
2. Ruslan picks 10-15 R1 decisions
3. После ack → next iterations:
   - Per-layer Notion implementation prompts (separate)
   - Actual Notion templates building
   - Дмитрий-trial start с Layer 1 minimum
   - Jetix-specific Layer 3 overlay (next iteration after base)
4. **Pool result** — NO auto implementation

---

*Prompt v2 closure 2026-05-25. 3 Layers (Layer 2 Personal Expanded удалён — будет «инструменты» layer отдельно потом). STANDALONE-capable mandate + SIMPLIFICATION mandate + AI Tools mega-page NEW. Jetix-specific overlay для Layer 3 deferred next iteration. Generic + Jetix overlay split в Layer 2 + Brand adaptation pattern. F2-F3 derivative. R1 surface only. Pool result. Supersedes v1 prompt.*
