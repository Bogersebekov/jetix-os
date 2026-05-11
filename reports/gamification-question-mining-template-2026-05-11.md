---
title: Gamification Question Mining — Шаг D Template Document (для Ruslan review)
date: 2026-05-11
type: question-mining-template
status: DRAFT — awaits Ruslan review + feedback (add / remove / refine) → конвертация в prompt
parent_plan: reports/gamification-deep-wiki-mining-plan-2026-05-11.md
parent_analysis: reports/gamification-mining-analysis-2026-05-11.md
strategic_anchor: decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md
F: F2
G: question-mining-template-applied-now
R: refuted_if_categories_or_questions_unused_in_Шаг_D_execution
blast_radius: F2
purpose: |
  Глубокий list вопросов по каждой категории и параметру для Шаг D Question Mining.
  Ruslan review в Antigravity → feedback → финальный prompt + execution.
---

# 🎮 Gamification Question Mining — Шаг D Template

> **Стратегическая цель:** взять wiki (722 entries / 742 staged edges after bulk-ack) и прогнать через **deep questions** по 4 categories.
> Output на каждый вопрос: 3-7 вариантов / гипотез / patterns extracted from wiki.
> Ты strategize'нешь (выберешь / scotrash'нешь / synthesize'нешь) — AI = scribe only.

---

## 🎯 Workflow

```
1. Ты читаешь этот template
2. Даёшь feedback:
   - Какие категории дополнить / убрать
   - Какие параметры дополнить
   - Какие конкретные вопросы добавить / убрать / переформулировать
   - Какой priority / weight у каждой категории
3. Я делаю финальный prompt для CC #3 (Шаг D Question Mining run)
4. CC запускает на ~1-2h autonomous
5. Output: per вопрос — 3-7 вариантов / гипотез / patterns
6. Ты strategize → выбираешь / refine → ФАЗА 4 (Ruslan-words spec)
```

---

## 📋 4 категории — preview

| # | Категория | Параметров | Вопросов total | Ключевая цель |
|---|---|---:|---:|---|
| **1** | **Платформа в целом** | 12 | 60+ | Как сделать саму платформу: UX / identity / aesthetics / anti-extraction |
| **2** | **Клан / Community** | 12 | 60+ | Как clan масштабируется 10→1000, retention, dynamics, экономика |
| **3** | **Workflow gamification** | 10 | 50+ | Real biz tasks → quests; TRM 6 resources как game stat; Tyson mentorship |
| **4** | **Core ядро / архитектура** | 10 | 50+ | 6 entities refinement, layer model (Linux pattern), foundation grounding |

**Total target:** ~44 параметров × 5 вопросов = **220+ deep questions**.

---

## 🟦 КАТЕГОРИЯ 1 — Платформа в целом (12 параметров)

### 1.1 First impression / Hook (что видит новый user в первые 30 секунд)
- Q1.1.1: Какой first screen optimally сразу сообщает Realm = workspace + game одновременно?
- Q1.1.2: Какой single CTA на onboarding? («Choose your Class»? «Find a Clan»? «Start your first Quest»?)
- Q1.1.3: Какой narrative hook (story-driven vs utility-driven) лучше для info-work ICP?
- Q1.1.4: Какие 3-5 game patterns можно apply для first 30 sec? (Torn intro / EVE Aura tutorial / WoW intro quest)
- Q1.1.5: Anti-pattern: чего НЕ показывать сразу? (TRM stats? cringe «level 1 noob»?)

### 1.2 Onboarding flow (первые 5-10 минут)
- Q1.2.1: Linear tutorial vs sandbox exploration — что для Jetix ICP лучше?
- Q1.2.2: Какой first «win» даём пользователю чтобы он почувствовал retention? (first Quest done / first Clan greeting / first AI agent dispatched?)
- Q1.2.3: Скрытая complexity vs visible complexity (Civilization показывает all, Candy Crush скрывает)?
- Q1.2.4: Как ввести 6 entities concept без overwhelm?
- Q1.2.5: Какие onboarding examples из top games применимы (Roblox tutorial / Fortnite training mode / Civ tutorial)?

### 1.3 Identity / Persona system
- Q1.3.1: Real name vs gamer tag vs hybrid (LinkedIn-style real identity)?
- Q1.3.2: Single Persona vs multiple Personae (per project / per Class)?
- Q1.3.3: TRM 6 stats — public / private / per-Clan visibility?
- Q1.3.4: Avatar customization — насколько deep (просто аватар vs full WoW-style customization)?
- Q1.3.5: Identity migration между Classes (можно ли сменить Class? cost?)
- Q1.3.6: Anti-doxing protections (как Ruslan не leak real identity к unknown clan members)?

### 1.4 Visual / Aesthetic language
- Q1.4.1: Minimalist / Linear-style vs full-game UI (Torn screens / EVE complex)?
- Q1.4.2: Game-aesthetic vs workspace-aesthetic vs hybrid (Notion + game elements)?
- Q1.4.3: Color palette implications (cyberpunk / monastic / corporate / RPG fantasy)?
- Q1.4.4: Iconography for 6 entities — что выбрать (sword / shield / scroll)?
- Q1.4.5: Animation / transitions — насколько game-like (overdone = cringe)?

### 1.5 Mobile vs desktop
- Q1.5.1: Mobile-first vs desktop-first для info-work ICP?
- Q1.5.2: Какие mechanics только desktop (deep Quest editing), какие только mobile (quick check-in / Clan ping)?
- Q1.5.3: Cross-device sync expectations (real-time / batch)?
- Q1.5.4: Notification strategy mobile vs desktop?
- Q1.5.5: Какие top games well-execute mobile+desktop dual platform (Roblox? Honor of Kings? Fortnite?)?

### 1.6 Notifications / Attention strategy
- Q1.6.1: Push notification frequency / quiet hours / opt-in granular?
- Q1.6.2: Tier hierarchy (urgent Quest deadline / Clan ping / season update / etc.)?
- Q1.6.3: Anti-extractive principle — как избежать manipulative notifications (Hooked tension)?
- Q1.6.4: Daily / weekly digest format (что в digest)?
- Q1.6.5: Notification batching strategy (immediate vs aggregated)?

### 1.7 Privacy / Data ownership
- Q1.7.1: Какие данные ownership user (open / personal / private)?
- Q1.7.2: GDPR / EU compliance (Ruslan Berlin) baseline expectations?
- Q1.7.3: Clan data ownership (shared vs per-member)?
- Q1.7.4: Export rights — full data export?
- Q1.7.5: Anti-platform-extraction (Varoufakis warning) — concrete commitments?

### 1.8 Performance / latency / scale
- Q1.8.1: Real-time vs eventual-consistency для Clan interactions?
- Q1.8.2: Scale targets: 100 users / 1K / 10K / 100K — каждый предполагает разную архитектуру?
- Q1.8.3: Latency budget для key interactions (Quest update / Clan ping / TRM stat refresh)?
- Q1.8.4: Offline mode behavior?
- Q1.8.5: Bandwidth requirements (mobile concern)?

### 1.9 Internationalization / Language
- Q1.9.1: Multi-language UI с launch или English only Phase 1?
- Q1.9.2: Russian native (для Ruslan inner circle) — built-in или localization layer?
- Q1.9.3: Cyrillic / non-Latin name support?
- Q1.9.4: Localization of game terminology (Class names / Quest types)?
- Q1.9.5: RTL languages future support?

### 1.10 Anti-extraction principle (Hooked tension thread)
- Q1.10.1: Какие patterns Hook Model используем (autonomy/competence/relatedness через SDT — safe), какие НЕ (manipulative variable rewards)?
- Q1.10.2: «Time well spent» metrics tracked? Surface'ятся к user?
- Q1.10.3: Self-limiting mechanisms (daily caps на playtime / Quest count / etc.)?
- Q1.10.4: Indistractable mode availability (mute notifications / focus session)?
- Q1.10.5: Monetization model — sub vs freemium vs equity model (no whaling)?

### 1.11 Mechanic vs Theme separation
- Q1.11.1: Mechanics layer (data model + rules) vs Theme layer (visual + narrative) — разделить?
- Q1.11.2: Theme variations (Cyberpunk / Fantasy / Corporate) — switchable user-side?
- Q1.11.3: Multi-theme support architectural?
- Q1.11.4: Default Theme на launch — какой?
- Q1.11.5: How top games execute (Roblox engine vs themes / Minecraft texture packs)?

### 1.12 Skill ceiling / accessibility
- Q1.12.1: Onboarding gentle vs steep — что лучше для ICP (entrepreneurs / founders / info-workers)?
- Q1.12.2: Power-user features hidden vs surfaced?
- Q1.12.3: Customization depth — preset vs build-your-own?
- Q1.12.4: Tutorial layers (basic → intermediate → advanced)?
- Q1.12.5: Anti-pattern: «Excel for power users only» — как избежать?

---

## 🟢 КАТЕГОРИЯ 2 — Клан / Community (12 параметров)

### 2.1 Clan size dynamics
- Q2.1.1: Optimal Clan size? (3-10 per Strategic Insight default, but Dunbar 150? WoW guild 100s?)
- Q2.1.2: Size tiers (small / medium / large) different rules / mechanics?
- Q2.1.3: Hard cap vs soft cap on Clan size?
- Q2.1.4: Sub-clans (squad внутри clan) при scale?
- Q2.1.5: Best patterns from EVE corporations / WoW guilds / Torn factions?

### 2.2 Recruitment механика
- Q2.2.1: Open join / application / invite-only? (LinkedIn vs Soho House model)?
- Q2.2.2: Application criteria (TRM stat thresholds? past Quest completions? Class compatibility?)
- Q2.2.3: Trial period before full membership?
- Q2.2.4: Cross-Class clan composition rules?
- Q2.2.5: Anti-pattern: «cliques» / closed groups — как mitigate?

### 2.3 Exit механика / Leaving
- Q2.3.1: Как Clan member уходит cleanly (без drama)?
- Q2.3.2: Cool-down period (cannot rejoin same Clan for X days)?
- Q2.3.3: Data ownership при exit (own Quests stay / shared Quests revert)?
- Q2.3.4: Public exit reason / private exit?
- Q2.3.5: Reputation impact (exit без drama vs ghosting)?

### 2.4 Internal hierarchy / Roles
- Q2.4.1: Flat (all equal) vs hierarchical (Leader / Officers / Members) vs dynamic (role rotation)?
- Q2.4.2: Какие roles внутри clan (Quest Master / Treasurer / Recruiter / Diplomat / Lore Keeper)?
- Q2.4.3: Role appointment (election / appointment / earned by Quest stats)?
- Q2.4.4: Term limits?
- Q2.4.5: Best patterns: WoW guild ranks / EVE corp roles / Torn faction leadership?

### 2.5 Communication tools
- Q2.5.1: Built-in chat vs Discord / Telegram integration?
- Q2.5.2: Async (forums / posts) vs sync (voice / video) — что primary?
- Q2.5.3: Channel structure (#general / #quests / #strategy / etc.)?
- Q2.5.4: Voice room для real-time strategy?
- Q2.5.5: Tools integration (Notion / Linear / GitHub references в chat)?

### 2.6 Activity rhythm (daily / weekly / seasonal)
- Q2.6.1: Daily mandatory check-in vs flexible engagement?
- Q2.6.2: Weekly ritual (Monday standup / Friday recap / etc.)?
- Q2.6.3: Monthly events / challenges?
- Q2.6.4: Seasonal milestones (3-month cycle finals)?
- Q2.6.5: Time zone management (synchronous events with global Clan)?

### 2.7 Conflicts resolution
- Q2.7.1: Disagreement / dispute mechanism (voting / Leader decides / arbitration)?
- Q2.7.2: Anti-toxicity rules (clear code of conduct)?
- Q2.7.3: Removal of bad actors (process / threshold)?
- Q2.7.4: Mediation tier (Clan internal / Realm moderator / community court)?
- Q2.7.5: Lessons from WoW guild drama / EVE corp warfare?

### 2.8 Reputation / Accountability
- Q2.8.1: Reputation score per Clan member (public / private)?
- Q2.8.2: How earned (Quest completion / Clan contribution / mentor-of)?
- Q2.8.3: How lost (no-show / abandoning Quest / toxicity)?
- Q2.8.4: Anti-free-riding mechanism (per wiki 1.00 perfect match insight)?
- Q2.8.5: Reputation portability cross-Clans (when you leave / join new)?

### 2.9 Cross-Clan interaction
- Q2.9.1: Alliances / federations between Clans?
- Q2.9.2: Competition / rivalry (PvP-like — sublimated в info-work context)?
- Q2.9.3: Resource trade between Clans?
- Q2.9.4: Joint Quests (multi-Clan large objectives)?
- Q2.9.5: Cross-Clan reputation transfer?

### 2.10 Identity / Branding (Clan colors / emblems)
- Q2.10.1: Customizable Clan name / emblem / colors / motto?
- Q2.10.2: Public Clan profiles (visible to all Realm members)?
- Q2.10.3: Heraldic system / symbology?
- Q2.10.4: Clan «story» / founding lore?
- Q2.10.5: Anti-pattern: cringe / over-stylized vs sincere identity?

### 2.11 Economic mechanism (shared Clan resources)
- Q2.11.1: Shared treasury (AI credits pool / Audience reach pool)?
- Q2.11.2: Contribution accounting (who put in what)?
- Q2.11.3: Distribution rules (per Quest / per Class / per seniority)?
- Q2.11.4: Tax mechanism (% of personal Quest rewards to Clan)?
- Q2.11.5: Lessons from EVE corp wallets / WoW guild banks?

### 2.12 Retention > 6 months
- Q2.12.1: Что заставляет players staying в WoW guild 5+ years?
- Q2.12.2: Что причиняет Clan dissolution (top reasons)?
- Q2.12.3: Onboarding new members при established Clan?
- Q2.12.4: Renewal / refresh mechanisms (season transitions / leadership changes)?
- Q2.12.5: Anti-stagnation mechanisms?

---

## 🟧 КАТЕГОРИЯ 3 — Workflow gamification (10 параметров)

### 3.1 Quest = real business task — как mapping
- Q3.1.1: Какие реальные tasks (consulting deliverable / content piece / outreach) лучше gamify как Quests?
- Q3.1.2: Granularity — Quest = 1 day / 1 week / 1 month task?
- Q3.1.3: Какие task types ПЛОХО gamify (admin work / waiting on external)?
- Q3.1.4: Solo Quest vs Party Quest vs Raid Quest (Clan-scale objectives)?
- Q3.1.5: Quest difficulty derivation (estimate hours / skill required / risk)?

### 3.2 Difficulty curves / Progression
- Q3.2.1: Linear progression (each Quest harder) vs branching (skill tree)?
- Q3.2.2: Plateaus / breakthrough moments?
- Q3.2.3: Failure handling (retry / restart / penalty)?
- Q3.2.4: Difficulty scaling per Persona TRM stats?
- Q3.2.5: Flow channel preservation (Csikszentmihalyi challenge/skill balance)?

### 3.3 Reward structures
- Q3.3.1: Intrinsic rewards (Persona growth / new abilities) vs extrinsic (badges / titles)?
- Q3.3.2: Monetary rewards (revenue share / commission)?
- Q3.3.3: Variable vs fixed rewards (Hooked tension)?
- Q3.3.4: Public recognition (Clan/Realm announcement) vs private?
- Q3.3.5: Resource rewards (AI credits / Audience reach / Energy refill)?

### 3.4 Skill trees / Class specialization
- Q3.4.1: Какие 6 archetypes (Strategic Insight default — confirm or refine)?
- Q3.4.2: Skill tree depth (5 levels / 10 / 20)?
- Q3.4.3: Multi-class progression (can be 2 Classes simultaneously)?
- Q3.4.4: Respec mechanism (reset Class choice — cost?)?
- Q3.4.5: Class synergies в Clan composition?

### 3.5 Time tracking integration (Toggl + game)
- Q3.5.1: Auto-import Toggl time into Quest progress?
- Q3.5.2: Manual time entry vs automated?
- Q3.5.3: Time-based stats (DW hours → Persona growth)?
- Q3.5.4: Productivity gameification vs surveillance line (privacy concern)?
- Q3.5.5: Best patterns from RescueTime / Clockify / Toggl?

### 3.6 Learning gamification (Tyson mentorship pattern)
- Q3.6.1: Mentor / Apprentice mechanic — formal или informal?
- Q3.6.2: How mentor earns (status / TRM stats from mentorship)?
- Q3.6.3: Knowledge transfer Quests (mentor sets Quest для apprentice)?
- Q3.6.4: Multi-mentor system (different Class mentors)?
- Q3.6.5: Apprentice graduation rituals (when ready for own Quests)?

### 3.7 TRM 6 resources as game stats
- Q3.7.1: Mapping: Capital / Time-leverage / Audience / Knowledge / Compute / Network → как gauges / stats / bars?
- Q3.7.2: Per-resource L0-L5 progression visibility?
- Q3.7.3: Resource interactions (spend Knowledge to grow Audience etc.)?
- Q3.7.4: Resource decay (use-it-or-lose-it for Time-leverage)?
- Q3.7.5: Resource conversion rates (AI credits → Knowledge growth etc.)?

### 3.8 Status / Public visibility
- Q3.8.1: Public leaderboards (Realm / Clan / Class)?
- Q3.8.2: Personal achievement showcase (LinkedIn-like profile)?
- Q3.8.3: Anti-toxicity (status without status anxiety)?
- Q3.8.4: Anonymous high-performer option?
- Q3.8.5: Status decay (recent vs lifetime)?

### 3.9 Critique / Feedback loops
- Q3.9.1: Peer review on Quest completion (Clan members rate)?
- Q3.9.2: Critique mechanic — formal Quest type?
- Q3.9.3: Reputation impact от giving good critique?
- Q3.9.4: Anti-low-quality review (incentivize substantive feedback)?
- Q3.9.5: Best patterns: code review / open-source contribution review?

### 3.10 AI agent integration
- Q3.10.1: Agents as visible Realm participants (NPCs)?
- Q3.10.2: Agent assigning to Quests (Quest delegation to agent / hybrid)?
- Q3.10.3: Agent reputation / quality rating?
- Q3.10.4: Cost economy (AI credit consumption per agent task)?
- Q3.10.5: Agent personality / persona customization per user?

---

## 🟪 КАТЕГОРИЯ 4 — Core ядро / архитектура (10 параметров)

### 4.1 6 entities refinement (Persona / Class / Clan / Quest / Resources / Seasons)
- Q4.1.1: Каждая entity — какой data model примерно (fields / relations)?
- Q4.1.2: Какие entities mutable vs immutable post-creation?
- Q4.1.3: Lifecycle states per entity?
- Q4.1.4: Entity versioning (season-over-season changes)?
- Q4.1.5: Hidden / deprecated fields (sunset patterns)?

### 4.2 Layer architecture (Linux pattern — base + apps)
- Q4.2.1: Какой «base layer» (kernel-equivalent)?
- Q4.2.2: Какие «system services» (auth / state / messaging)?
- Q4.2.3: Какие «apps» (Quest types / Class kits / Clan templates)?
- Q4.2.4: Open API surface — что exposed для extension?
- Q4.2.5: Plugin / Extension model?

### 4.3 Data model
- Q4.3.1: Source of truth: own DB / Notion / hybrid?
- Q4.3.2: Sync model (event-driven / batch / real-time)?
- Q4.3.3: Privacy boundaries (Personal data / Clan-shared / Realm-public)?
- Q4.3.4: Audit trail / history retention?
- Q4.3.5: GDPR-compliant data lifecycle?

### 4.4 Engineering principles
- Q4.4.1: Testability priorities (unit / integration / E2E)?
- Q4.4.2: Observability (metrics / logs / traces)?
- Q4.4.3: Error handling philosophy (fail fast / graceful degrade)?
- Q4.4.4: Performance targets (p50 / p99 latency)?
- Q4.4.5: Security model (auth / authz / data encryption)?

### 4.5 Extensibility / Community contribution
- Q4.5.1: Open-source какой части (engine / templates / themes)?
- Q4.5.2: Community Quest types — accepted via PR?
- Q4.5.3: Reputation / governance для community contributions?
- Q4.5.4: Revenue share для contributors?
- Q4.5.5: Lessons from Roblox UGC / Minecraft mod / Linux kernel?

### 4.6 Versioning / Migration
- Q4.6.1: Season-to-season schema changes — auto-migration?
- Q4.6.2: Backward compatibility window?
- Q4.6.3: User-visible vs invisible version transitions?
- Q4.6.4: Deprecation timeline?
- Q4.6.5: Rollback mechanism?

### 4.7 Open source policy
- Q4.7.1: Какой license (MIT / AGPL / Custom)?
- Q4.7.2: Core engine OSS or proprietary?
- Q4.7.3: Templates / Themes / Quest types OSS?
- Q4.7.4: Trademark / brand protection?
- Q4.7.5: Lessons from Discord (closed) vs Matrix (open) vs Slack (closed)?

### 4.8 Scale targets
- Q4.8.1: Phase 1 — 10 users (Clan pilot). Phase 2 — 100? 1000? 10K?
- Q4.8.2: Infrastructure trade-offs per scale?
- Q4.8.3: Multi-region eventual?
- Q4.8.4: Cost model per user (free / paid / equity)?
- Q4.8.5: When to invest в horizontal scaling?

### 4.9 Foundation grounding (existing canonical)
- Q4.9.1: How Realm extends Workshop (5 owner roles)?
- Q4.9.2: How Realm extends TRM (6 resources × L0-L5)?
- Q4.9.3: How Realm extends Doc 1B (8 faces, Partner/Client/Worker tiers)?
- Q4.9.4: How Realm aligns с 6 Hexagon insights — explicit anchors?
- Q4.9.5: Where Realm contradicts existing canonical — must be reconciled before launch?

### 4.10 Anti-pattern enforcement (architectural)
- Q4.10.1: Pay-to-win enforcement (data model prevents monetary-only progression)?
- Q4.10.2: Whaling protection (cap on individual spend)?
- Q4.10.3: Manipulation prevention (variable rewards architectural caps)?
- Q4.10.4: Platform-extraction protection (data ownership in code)?
- Q4.10.5: Mandatory grinding prevention (Quest design rules at engine level)?

---

## 🎯 Per-question output format (когда Шаг D запустится)

Для каждого вопроса CC выдаст:

```yaml
question: <verbatim text>
category: <1-4>
parameter: <X.Y>
variants:
  - variant_1:
      hypothesis: "<text>"
      evidence_from_wiki: [<entry-slug-1>, <entry-slug-2>]
      precedent_games: [<game-1>, <game-2>]
      pros: [...]
      cons: [...]
      F-G-R: F2 / hypothesis-applied-now / R-medium
  - variant_2: ...
  - variant_3: ...
  ... (3-7 variants typical)
recommended_next: "Ruslan strategize: choose / refine / synthesize"
```

Wiki entries referenced — provenance trail full Tier 2 R6 compliant.

---

## 🔴 STRATEGIC DECISION POINTS — для Ruslan (review feedback)

### Decision 6: Priority / Weight по категориям
- **(A)** Equal weight — каждая категория 25% time/effort
- **(B)** Weighted: Core ядро + Workflow gamification heavy (35% / 35% / 15% Platform / 15% Clan) — основа важнее UX layers
- **(C)** Weighted: Платформа + Clan heavy (35% / 35% / 15% / 15%) — first cohort experience важнее

Recommend **(B)** — Core + Workflow ядро design.

### Decision 7: Total questions
- **(A)** 220+ (current draft — comprehensive)
- **(B)** 100-150 (selected key questions per parameter)
- **(C)** 50 (только top 1-2 per parameter)

Recommend **(A)** — глубоко на 1000%.

### Decision 8: Parameter granularity
- **(A)** Current 12+12+10+10 = 44 parameters
- **(B)** More granular (15+15+12+12 = 54)
- **(C)** Less granular (8+8+8+8 = 32)

Recommend **(A)** — sufficient depth.

### Decision 9: Output format
- **(A)** Per-question variants 3-7 (per draft)
- **(B)** Top 1-3 only per question (narrower)
- **(C)** Open-ended exploration per question (no limit on variants)

Recommend **(A)** — balanced breadth/depth.

### Decision 10: Wiki entry references
- **(A)** Mandatory ≥2 wiki refs per variant (current — strong provenance)
- **(B)** Optional refs (faster но weaker provenance)
- **(C)** Mandatory ≥3 refs + cross-domain (rigorous но slower)

Recommend **(A)** — Tier 2 R6 compliance.

---

## ❓ Open items для Ruslan feedback

1. **Какие категории дополнить** (mentioned in Strategic Insight но не в template — например Seasons rhythm? Outreach mechanic for Clan growth? Mentor-Apprentice protocol depth?)
2. **Какие параметры убрать** (если категория too broad / off-target)?
3. **Какие конкретные вопросы добавить** (что важно тебе НЕ упустить)?
4. **Какие переформулировать** (если frame слишком narrow / leading)?
5. **Какие priority/weight на категории** (Decision 6)?
6. **Total questions** count (Decision 7)?

---

## 📋 Next step after Ruslan feedback

1. Ruslan читает в Antigravity → даёт feedback (add / remove / refine)
2. Я updating template based on feedback
3. Я конвертирую финальный template в **trigger prompt** для CC #3
4. CC #3 запускает Шаг D autonomous (~1-2h)
5. Output: `reports/gamification-question-mining-run-2026-05-11.md` со всеми вариантами
6. Ты strategize → ФАЗА 4 (Ruslan-words spec)

---

*Awaits Ruslan review + feedback в Antigravity → finalize → convert to prompt → execute.*
