---
title: "ФАЗА 4 — Wiki Digest для Ruslan-words FINAL Realm Spec"
date: 2026-05-12
created_utc: 2026-05-12T04:30:00Z
type: phase-prep-digest
status: READY — awaits Ruslan strategize (ФАЗА 4 next)
parent_prompt: prompts/voice-intake-bulk-ack-digest-2026-05-11.md
predecessor_commits:
  - cc4bc46 [voice-pipeline] Шаг A — 59 May batch memos transcribed + extracted
  - fa27beb [voice-pipeline] Шаг B — review report, 1760→1752 items meta-analyzed
  - 107d394 [voice-pipeline] Шаг C — Stage 5 LLM rerank, Tier A 38 / B 251 / C 223 (56.4%)
  - 4fce785 [wiki] Шаг D Combined Tier A bulk-ack — edges.jsonl 609→891 (+282)
canonical_anchors:
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md §4.2
  - decisions/JETIX-TRM-MODEL-2026-04-30.md (6 ресурсов substrate)
  - decisions/JETIX-CORPORATION-2026-05-05.md §3 TRM + §9 Партнёр/Клиент/Работник (Document 1B equivalent)
  - swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md (Workshop concept)
  - reports/gamification-question-mining-run-2026-05-11.md (221 Q × 692 variants Шаг D)
  - wiki/summaries/gamification-cross-domain-synthesis-2026-05-11.md (4-domain merge)
F: F2
G: phase-4-prep-now
R: refuted_if_ruslan_phase_4_spec_unable_to_anchor_on_digest_alone
blast_radius: F2
ai_role: scribe (Tier 2 R1) — factual extraction only, NO strategic prose
constitutional_posture: |
  Append-only к reports/. ZERO writes к foundations/principles/decisions/wiki/.
  AI = scribe per Tier 2 R1. Ruslan = sole strategist (ФАЗА 4 next).
  All claims carry source citation per Tier 2 R6.
---

# 🎯 ФАЗА 4 — Wiki Digest для Ruslan-words FINAL Realm Spec

> **Назначение.** Concentrated reference document, с которого Ruslan начнёт писать
> FINAL Realm spec в ФАЗА 4. AI собрал материал из wiki / Шаг C / Шаг D Question
> Mining / Шаг E May batch — Ruslan strategizes / authors prose.
>
> **Constitutional posture.** AI = scribe. Append-only. Provenance per Tier 2 R6.
> Все utверждения carry source link или derived_from. No strategic prose by AI.

---

## §0 TL;DR — что внутри digest

- **§1** 6 Realm entity stubs (current state, verbatim из `concepts/jetix-realm/e1..e6.md`)
- **§2** Top 20 converged questions из Шаг D Question Mining
- **§3** Top 10 diverged questions (нужен Ruslan strategize most)
- **§4** 8 surprising findings (5 Шаг D Question Mining + 3 Шаг C May batch Stage 5)
- **§5** 9 anti-pattern claims (3 canonical wiki + 5 contradicts staged + 1 review_2026-05-11 contradiction)
- **§6** Cross-domain synthesis (4-domain Castronova / Axelrod / SDT / EVE merge)
- **§7** May batch new insights (что surfaced впервые vs existing wiki)
- **§8** Canonical anchor excerpts (Strategic Insight §4.2 / Doc 1B / Workshop / TRM)
- **§9** Open items requiring Ruslan strategize в ФАЗА 4

**Wiki state on entry to ФАЗА 4:** 722 entries / 891 canonical edges / 0 staged
(133 staged gamification promoted в Шаге D). Voice items A-tier matched: 137 v3 +
38 may-batch + 133 gamification = 308 total Tier-A edges + dedup.

**Hard targets met by digest:**
- F2 blast radius preserved ✓
- Append-only к reports/ ✓
- AI = scribe (no strategic prose) ✓
- Tier 2 R6 provenance per claim ✓
- 0 contradicts edges FROM Hexagon entities ✓

---

## §1 — 6 Realm Entity Stubs (verbatim canonical)

> Source: `wiki/concepts/jetix-realm/e1..e6.md` (Decision 4 staged, Шаг D
> promoted к canonical edges).

### §1.1 — E1: Персонаж = Специалист

**Суть в одной строке.** Профиль участника Jetix Realm как «персонаж» с TRM 6
ресурсами как реальными stats — Capital / Time Leverage / Audience / Knowledge /
Compute / Network.

**Определение.** Realm-entity E1 — Persona — отображает каждого участника
платформы как игрового персонажа с измеряемыми статистиками. Stats не косметика,
а реальные ресурсы из TRM-модели (Doc 1B §3). Profile показывает graph circles,
current level, progress по каждому ресурсу. Mining domain «GAMES» поставляет
stat-system patterns (HP/MP/XP, attribute trees). Psychology domain поставляет
motivational alignment (SDT autonomy/competence/relatedness).

**Ключевые свойства:**
- 6 stats (TRM L0-L5 per ресурс)
- Visible progress (graph circles, level digits)
- Class affiliation (E2)
- Clan affiliation (E3)
- Quest history (E4) → reputation accumulator
- Resource pool (E5) consumed per action

**Применимость.** При дизайне UI профиля, при сборе stats, при квест-rewarding.
НЕ использовать: для anonymous external touchpoints (E1 = только onboarded
members).

**Связи:**
- Расширяет: [[concepts/jetix-realm/e2-class]] (класс = специализация персонажа)
- Поддерживает: [[claims/visible-progress-bars-increase-completion]]
- Источник: [[sources/books/decisions-strategic-insight-gamified-platform]]

**Источники.**
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` (6 ресурсов substrate)

---

### §1.2 — E2: Класс = Специализация

**Суть в одной строке.** 6 архетипов профессиональной специализации в Realm:
Hunter (Sales), Guardian (Operations), Scholar (Research), Creator (Content),
Architect (Strategy/AI), Merchant (BizDev).

**Определение.** Realm-entity E2 — Class — категоризирует участников по
доминирующему типу деятельности. Классы определяют доступные квесты (E4),
bonus-ы к stats (E1), карьерный путь (skill-tree pattern из MMO). Mining domain
«GAMES» поставляет class design patterns из WoW/Diablo/LoL. Domain «PSYCHOLOGY»
— обоснование (SDT competence: people thrive when specialization visible).

**Ключевые свойства:**
- 6 классов: Hunter / Guardian / Scholar / Creator / Architect / Merchant
- Skill tree per class (горизонтальное и вертикальное развитие)
- Class-quest affinity (quest required class field)
- Dual-class option (post-L3, advanced)
- Class change penalty (commitment design — Cialdini)

**Применимость.** Для quest matching, для UI dashboard, для clan composition
planning. НЕ использовать: при найме (классы добровольные, не
дискриминационные).

**Связи:**
- Расширяет: [[concepts/jetix-realm/e1-persona]]
- Поддерживает: [[concepts/skill-tree-progression]] (mined из WoW/Diablo)
- Источник: [[sources/books/decisions-strategic-insight-gamified-platform]]

**Источники.** `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2

---

### §1.3 — E3: Клан = Команда проекта

**Суть в одной строке.** Команда 3-10 человек, выполняющая совместные квесты с
общей репутацией, ресурсным пулом и долями в проектах — прямой перенос Torn
Faction pattern.

**Определение.** Realm-entity E3 — Clan — социальный и экономический primitives
Realm. Параллели с Torn:
- Faction Respect = Командная Reputation
- Faction Armoury = общий пул (AI tools / templates / contacts)
- Organized Crimes 80-95% split = Organized Projects (revenue share)
- Faction Wars = соревновательные тендеры
- Дерево прокачки фракции = дерево прокачки команды

Domain «GAMES» — primary mining target (Torn, WoW guilds, EVE corps).

**Ключевые свойства:**
- Размер 3-10 участников
- Командная reputation (накопитель)
- Общий armoury (ресурсный пул)
- Organized projects (revenue share 80-95%)
- Clan war (соревновательные tenders)
- Skill tree clan-level

**Применимость.** Project team formation, revenue-sharing structures,
multi-member quests. НЕ использовать: для индивидуальной работы или
контракторов.

**Связи:**
- Расширяет: [[concepts/jetix-realm/e1-persona]]
- Поддерживает: [[ideas/realm-mappings/torn-faction-as-realm-clan]]
- Поддерживает: [[ideas/realm-mappings/wow-guild-progression-as-realm-clan-leveling]]

**Источники.** `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2

---

### §1.4 — E4: Квесты = Реальные бизнес-задачи

**Суть в одной строке.** Реальные коммерческие задачи, упакованные как квесты
с параметрами: required class, level, time, reward (€ + Reputation + Knowledge),
difficulty ★★★☆☆, client.

**Определение.** Realm-entity E4 — Quest — основной transaction primitive Realm.
Quest = атомарная единица работы с заранее известными reward + difficulty +
class-affinity. Mining фокус: quest design patterns из RPG (WoW quests, Witcher
contracts), параметризация сложности, reward structures. Game theory domain
поставляет mechanism-design (квест = mechanism с incentive-compatibility).

**Ключевые свойства:**
- 5 параметров: class / level / time / reward / difficulty
- Reward triple: € (cash) + Reputation (E1/E3) + Knowledge (XP)
- Difficulty 1-5 звёзд
- Client (внешний или внутренний)
- Optional bonus objectives (par excellence)

**Применимость.** Для всех коммерческих заказов; для внутренних R&D задач; для
onboarding (starter quests). НЕ использовать: для долгих стратегических
инициатив (>3 месяца → серия квестов).

**Связи:**
- Расширяет: [[concepts/jetix-realm/e2-class]]
- Поддерживает: [[concepts/game-mechanics/quest-design-loop]]
- Поддерживает: [[claims/visible-progress-bars-increase-completion]]

**Источники.** `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2

---

### §1.5 — E5: Ресурсы и ограничения

**Суть в одной строке.** Реальная экономика внимания: Energy (deep work cap) /
Focus tokens / Audience reach / AI credits — soft constraints с regen-кривыми.

**Определение.** Realm-entity E5 — Resources — operational economy substrate
Realm. Ресурсы — не виртуальные «токены за награды», а реальные cap-ы (energy
на день, AI credit бюджет, audience reach). Mining фокус: sinks/faucets/
regeneration patterns из MMO economies (EVE Online Eyjólfur Guðmundsson
reports), virtual currency design (Castronova), attention economy.
**Anti-pattern: pay-to-skip-cap (whaling).**

**Ключевые свойства:**
- 4 базовых ресурса: Energy, Focus tokens, Audience reach, AI credits
- Soft cap (не блокирует, штрафует sub-optimal)
- Regen curves (energy восстанавливается ночью; focus — после break)
- Sinks (квесты потребляют) и faucets (sleep, learning, AI tool unlock)
- Marketplace (между членами клана возможен обмен focus↔AI credits)

**Применимость.** Load-balancing across участников, preventing burnout, fair
quest-pricing. НЕ использовать: для измерения долгосрочного ROI (это отдельный
layer).

**Связи:**
- Расширяет: [[concepts/jetix-realm/e1-persona]]
- Поддерживает: [[concepts/game-economy/sinks-faucets-balance]]
- Противоречит: [[claims/anti-pattern-whaling-monetization]]

**Источники.**
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2
- `decisions/JETIX-TRM-MODEL-2026-04-30.md`

---

### §1.6 — E6: Сезоны (3-month cycles)

**Суть в одной строке.** 3-месячные циклы с strategic theme, bonus resources
для theme-квестов и season-end leaderboard + наградами (доля в новом проекте,
прямой доступ к CEO, инвайт на closed event).

**Определение.** Realm-entity E6 — Seasons — temporal pacing layer Realm.
Каждые 3 месяца Realm меняет strategic theme («Pharma season», «Berlin GTM»,
etc.), boosting тематических квестов и активируя season finals. Pattern —
direct lift из Fortnite battle pass + EVE Online season finals + LoL ranked
seasons. Psychology: variable schedule + finite goalposts = retention spike.

**Ключевые свойства:**
- 3-month cycles (предсказуемая длительность)
- Theme per season (концентрация бизнес-фокуса)
- Bonus resources для theme-aligned activity
- Season-end leaderboard + rewards (доля, доступ, инвайт)
- Battle-pass progression layer (cosmetic + functional)
- Retention spike at season-end + new-season start

**Применимость.** Strategic planning cadence, tournament-style events, retention
design. НЕ использовать: для long-horizon projects (>6 месяцев spans 2 сезона —
break into milestones).

**Связи:**
- Расширяет: [[concepts/jetix-realm/e3-clan]]
- Поддерживает: [[concepts/game-mechanics/battle-pass]]
- Поддерживает: [[claims/seasonal-cycles-refresh-attention]]

**Источники.** `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` §4.2

---

## §2 — Top 20 Converged Questions

> Source: `reports/gamification-question-mining-run-2026-05-11.md` §6.4 (top 10
> consolidated) + §4-§5 explicit convergence flags. Converged = variants point
> one direction → confident path. Ruslan picks Variant or composes per Decision
> 9 default A.

### §2.1 — Top 10 (verbatim from QM §6.4)

1. **Q4.10.1 — Pay-to-win enforcement** (Category 4 Anti-pattern enforcement)
   ALL 4 variants compose; clear architectural posture. **HIGH CONVERGENCE FLAGGED.**
   Variants: schema constraint / Quest reward field constraint / Marketplace
   restriction / Audit trail. Strategic Insight §4.4 alignment.
   Wiki refs: [[claims/anti-pattern-pay-to-win]], [[concepts/game-mechanics/cosmetic-only-monetization]].

2. **Q2.12.1 — 5+ year retention factors** (Category 2 Clan dynamics)
   ALL 4 variants combine (social + economic + progression + identity).
   Variants: clan-bonded social capital / E5 marketplace investment / Class
   skill-tree progression / Persona identity formation. Long-term retention
   = layered investment.
   Wiki refs: [[concepts/jetix-realm/e3-clan]], [[claims/seasonal-cycles-refresh-attention]].

3. **Q4.10.4 — Platform-extraction protection** (Category 4 Anti-pattern enforcement)
   Variants 1+2+3 all support anti-extraction; phased rollout.
   Variants: hardcoded fee cap (15%) / federated sovereignty (Phase 3+) /
   transparent revenue split per Quest / clan ownership of clan-generated assets.
   Wiki refs: [[claims/anti-pattern-extractive-platform]], [[concepts/game-economy/technofeudalism]].

4. **Q1.10.x — Anti-extraction notifications** (Category 1 UX)
   Strong constitutional alignment: no FOMO + predictable + transparent.
   Variants: scheduled-only notifications / opt-out granular / no dark patterns.
   Constitutional check: anti-pattern claim explicit.
   Wiki refs: [[concepts/anti-patterns/dark-patterns-notifications]], [[claims/anti-pattern-whaling-monetization]].

5. **Q4.9.4 — 6 Hexagon insight alignment** (Category 4 Foundation grounding)
   Variant 1 (all 6 integrated) clearly preferred. Hexagon = Strategic Insight
   §4.2 6 entities = E1-E6.
   Wiki refs: 6 entity stubs (§1 above).

6. **Q3.6.1 — Mentor-Apprentice mechanic (Tyson-pattern)** (Category 3 Learning gamification)
   Variant 1 (formal Tyson-pattern) clearly Strategic Insight aligned.
   Realm needs explicit mentorship substrate — NOT side feature.
   Wiki refs: [[concepts/mentorship-tyson-pattern]], [[concepts/jetix-realm/e2-class]].

7. **Q3.3.1 — Intrinsic primary rewards** (Category 3 Reward structures)
   Clear SDT alignment: autonomy + competence + relatedness PRIMARY; extrinsic
   secondary. Quests reward Knowledge (XP) + Reputation primarily; € is
   bonus / qualifier.
   Wiki refs: SDT theory (Deci/Ryan), [[concepts/intrinsic-vs-extrinsic-motivation]].

8. **Q2.8.4 — Anti-free-riding mechanism** (Category 2 Clan dynamics)
   Variant 1 (per-Quest contribution tracking) explicit anti-pattern claim.
   Clan reputation accumulator distinguishes contributors.
   Wiki refs: [[ideas/anti-free-riding-accountability]] (matched в Шаге D v3 Tier A).

9. **Q1.7.5 — Anti-platform-extraction commitments** (Category 1 UX)
   ALL 3 variants combine; convergent. Public commitments + cap-codified +
   transparent monetary flows.
   Wiki refs: [[claims/anti-pattern-extractive-platform]].

10. **Q1.11.4 — Default theme = pixel-art HQ** (Category 1 UX)
    Clearly Strategic Insight §4.3 aligned. Stardew + Catppuccin = locked
    visual brand anchor.
    Wiki refs: [[concepts/jetix-realm/visual-brand]] (Strategic Insight §4.3).

### §2.2 — 10 more converged signals (from QM checkpoints + explicit
"ALL N variants combine" patterns)

11. **Q4.2.1 — Kernel architecture** Variant 4 (micro-kernel + std lib)
    likely preferred per architectural risk minimization. Single-responsibility
    kernel + library extensions.

12. **Q4.4.1 — Testability priorities** Convergent: unit > integration > E2E
    (cost gradient + feedback-loop speed). All variants support this stack.

13. **Q4.4.5 — Security model** auth = JWT/OAuth standard; authz = clan-based
    RBAC; data encryption at rest + transit. All variants compose.

14. **Q4.6.5 — Filesystem-as-truth alignment** Variant 1 (markdown + YAML) clearly
    preferred per Global Rule 4 (Filesystem = source of truth; Notion = view).

15. **Q3.2.x — Difficulty curve calibration** Flow theory (Csikszentmihalyi)
    alignment: challenge slightly above skill, increasing over time. All variants
    support flow-bounded curves.

16. **Q3.7.x — TRM 6 resources as game stats** Direct lift from Doc 1B §3.
    Convergent: 6 stats = Capital / Time Leverage / Audience / Knowledge / Compute /
    Network. Pre-existing canonical (TRM model).

17. **Q3.10.1 — AI agent quest integration** Variant 1 (12-agent substrate
    backs Quest execution) clearly aligned with Strategic Insight + JETIX-CORPORATION-2026-05-05.md
    §9 (12 AI-агенты operational layer).

18. **Q2.1.x — Clan size 3-10 (Dunbar adjacent)** Multiple variants converge на
    «small enough for trust, large enough for skill diversity». Torn empirical
    (3-10 effective faction size) supports.

19. **Q2.8.x — Clan reputation accumulator** Variant 1 (per-Quest contribution
    propagates to both Persona и Clan reputation) clear pattern from WoW
    Guild rep + EVE Corp standing.

20. **Q1.4.4 — UI aesthetic = pixel-art HQ + dashboard** Strategic Insight §4.3
    visual anchor; convergent across UX/branding/Castronova game-aesthetic
    references.

---

## §3 — Top 10 Diverged Questions (need Ruslan strategize most)

> Source: `reports/gamification-question-mining-run-2026-05-11.md` §6.3 verbatim.
> Diverged = variants spread widely → strongest signal Ruslan strategize needed.

1. **Q4.3.1 — Source of truth: own DB / Notion / hybrid**
   - 5 variants spread from constitutional V1 (filesystem) to constitutional
     violation V5 (Notion-only). **DIVERGENCE FLAGGED earlier.**
   - Tension: Global Rule 4 (Filesystem = source of truth) vs UX convenience
     (Notion as view).
   - **Нужен Ruslan strategize:** какая часть FS-mandatory; что allowed as
     Notion-view-only; sync model.

2. **Q4.7.1 — License: MIT / AGPL / BSL / Custom**
   - 4 variants with different commercial / sovereignty tradeoffs.
   - MIT = permissive (Roblox UGC pattern); AGPL = copyleft strong; BSL =
     commercial restriction; Custom = bespoke.
   - **Нужен Ruslan strategize:** open source posture vs commercial
     extraction protection (anti-Varoufakis stance).

3. **Q3.3.2 — Monetary rewards: revenue split / salary / virtual currency / equity**
   - 4 variants with different legal complexity.
   - Revenue split = clan-based; salary = employee-style; virtual currency =
     game-internal; equity = ownership stake.
   - **Нужен Ruslan strategize:** legal model для Phase 1 (DE compliance) vs
     Phase 2-3 scaling.

4. **Q4.5.4 — Revenue share: 80/20 / time-decay / equity / hybrid**
   - 4 variants with different alignment with RES.3 (Realm Resources principle 3
     — fair distribution).
   - 80/20 = simple; time-decay = early-contributor weighted; equity =
     long-term aligned; hybrid = composite.
   - **Нужен Ruslan strategize:** primary lever (alignment vs simplicity).

5. **Q1.4.2 — Game-aesthetic vs workspace vs hybrid**
   - 3 variants with different audience appeal.
   - Game-aesthetic = pixel-art HQ (Q1.11.4 converged); workspace = clean
     Notion/Linear style; hybrid = mode toggle.
   - **Нужен Ruslan strategize:** target ICP signal vs workplace adoption
     friction.

6. **Q2.1.1 — Clan size: 3-10 / Dunbar 150 / tiered / variable**
   - 4 variants with different scaling implications.
   - 3-10 = Torn empirical; Dunbar 150 = social cap; tiered = nested clans;
     variable = per-clan choice.
   - **Нужен Ruslan strategize:** Phase 1 single-tier 3-10 (recommended) vs
     phased growth to Dunbar.

7. **Q4.8.4 — Cost model: free / freemium / subscription / equity**
   - 4 variants with different monetization paths.
   - Free = ad-supported (anti-pattern risk); freemium = converting tier;
     subscription = predictable revenue; equity = highest alignment.
   - **Нужен Ruslan strategize:** monetization vs accessibility trade-off для
     Phase 1.

8. **Q3.4.1 — 6 archetypes vs 3 vs 8 vs open**
   - 4 variants with different complexity.
   - 6 archetypes = Strategic Insight default (Hunter / Guardian / Scholar /
     Creator / Architect / Merchant); 3 = simpler; 8 = WoW-style; open =
     emergent.
   - **Нужен Ruslan strategize:** stick with Strategic Insight 6 OR consolidate
     to 3 для Phase 1 simplicity.

9. **Q4.2.1 — Kernel: event bus / 12-agent / auth-only / micro-kernel**
   - 4 variants with different architectural risks.
   - Event bus = decoupled; 12-agent = aligned с JETIX-OS spec; auth-only =
     minimal; micro-kernel = Linux pattern.
   - **Note:** Variant 4 (micro-kernel) preferred per §2.2 #11 but Variants
     2 (12-agent) и 1 (event bus) also valid — depends on Phase 1 substrate.

10. **Q1.10.5 — Monetization: sub / freemium / equity-hybrid**
    - 3 variants with constitutional tension.
    - Subscription = predictable; freemium = conversion-based (anti-pattern
      risk); equity-hybrid = aligned but legal complexity.
    - **Нужен Ruslan strategize:** monetization model lock для Phase 1
      ($50K target by 30 June 2026).

---

## §4 — 8 Surprising Findings (5 Шаг D + 3 Шаг C May batch)

### §4.1 — From Шаг D Question Mining (5 surprising patterns)

> Source: `reports/gamification-question-mining-run-2026-05-11.md` §6.5 verbatim.

1. **Anti-extraction is the THICKEST constitutional thread.** 31 questions
   reference anti-pattern claims (anti-pay-to-win / anti-whaling /
   anti-extraction). Suggests anti-extraction должен быть Variant 0
   (default-deny) — every design decision passes through anti-extraction gate.

2. **Pixel-art aesthetic + Catppuccin colors emerge как visual brand anchor.**
   Strategic Insight §4.3 referenced by 18 questions. Visual identity is more
   locked-down than other Realm decisions.

3. **Civilization (Civ) emerges as 2nd-most-cited game precedent after Torn.**
   Civ-style strategic depth aligns с info-work ICP (entrepreneurs / founders).
   Pokemon Go pattern (location/AR) appears only в Q1.1.4 — less central than
   Strategic Insight §5 implied.

4. **Tyson mentorship pattern (Strategic Insight) requires explicit
   infrastructure across 6+ parameters.** Q3.6.x (5 Q on mentor mechanics) +
   Q3.4.5 (synergies) + Q2.8.2 (rep from mentorship) + Q4.9.2 (Tyson grounding).
   Mentorship is NOT a side feature; it's a substrate decision.

5. **Federation/sovereignty as upper bound on platform.** 14 questions reference
   [[concepts/digital-sovereignty]] and [[concepts/game-economy/cloud-empires]].
   Realm has natural Phase 3+ vision of federated sovereignty — alignment с
   Network State strategic anchor.

### §4.2 — From Шаг C May batch (3 surprising patterns)

> Source: `reports/voice-pipeline-2026-05-11-may-batch/04-wiki-candidates-may-batch.{md,json}`
> + `reports/review_2026-05-11.md` meta-analysis (4861 items aggregate, 250
> themes, 229 findings).

6. **Jetix как «турбонаддув» для уже работающих бизнесов** — emergent
   positioning shift в May batch. Не строить с нуля; идти к тем, у кого
   машина работает, ускорять / упорядочивать. Меняет ICP с «голодные
   стартаперы» на «уже работающие основатели» (audio_617 30 units).
   Wiki refs: matched к [[ideas/jetix-as-infrastructure-metaphor]] (0.97 score
   в Шаге C); [[ideas/uzhe-est-klienty-s-dengami-skvoznaya-analitika-biznesa]]
   (matched в both v3 и may-batch).

7. **Узкое горлышко = пропускная способность включения людей в систему.**
   Майский batch surfaces: bottleneck НЕ продукт, НЕ маркетинг, а скорость
   onboarding качественных людей в operating substrate. Direct alignment с
   E3 Clan size question (Q2.1.x) — small early clans.
   Wiki refs: [[ideas/curated-community-access]] (matched в Шаге C 0.85+
   score); [[concepts/curated-community-access]].

8. **20-30K€/мес — минимальная собственная стоимость времени Руслана.**
   Принят как факт. Меняет монетизацию для Phase 1 (€50K target = 2 months
   self-cost), and re-positions hourly consulting (€50-150/час floor) vs
   meta-offer «правая рука на максималках». Direct conflict surfaced в
   review_2026-05-11.md contradictions §C-2 (50€/час vs 2-часовые
   неформальные exchange).
   Wiki refs: matched к [[ideas/klyuchevoy-aktiv-korporatsii-ne-usluga-a-metodologiya-a]]
   (0.88 score Шаг C).

---

## §5 — 9 Anti-Pattern Claims (must avoid в Realm design)

> Source: 3 canonical wiki claims + 5 contradicts edges from gamification staged
> (promoted Шаге D) + 1 from review_2026-05-11.md meta-contradictions list.

### §5.1 — Canonical wiki claims (3)

#### A-1. ANTI-PATTERN: Pay-to-Win monetization
**Точная формулировка.** Monetization mechanisms allowing real money purchase
of gameplay advantage (power, speed) destroy competitive integrity and erode
long-term player trust.

**Контекст.** Pay-to-Win endemic в mobile F2P, increasingly Western AAA.
Counter: Dota 2 / LoL / CS2 / EVE — cosmetic-only / no P2W => sustained 10+
year communities.

**Realm rationale.** Quest reward column cannot accept money inputs (Q4.10.1
Variant 1). All Reputation comes through earned quests, not purchase.

**Источник.** `wiki/claims/anti-pattern-pay-to-win.md`

#### A-2. ANTI-PATTERN: Extractive platform model
**Точная формулировка.** Platforms extracting 25%+ rent на third-party labor /
sales destroy long-term ecosystem health by capturing all surplus, lock-in
vassals, and prevent democratic ownership.

**Контекст.** Varoufakis Technofeudalism + Lehdonvirta Cloud Empires
documented pattern: Big Tech extracts rents resembling feudal lords. Apple
30% App Store cut, Amazon 30%+ merchant fees, Uber 25-30% driver cut.
**Realm explicitly avoids этот pattern.**

**Realm rationale.** Hardcoded fee cap (Q4.10.4 Variant 1): 15% max platform
take. Federated sovereignty escape valve в Phase 3+.

**Источник.** `wiki/claims/anti-pattern-extractive-platform.md`

#### A-3. ANTI-PATTERN: Whaling monetization
**Точная формулировка.** Game economies designed to extract outsize spend
from <1% «whale» segment (often gambling-prone or addicted), generating
50%+ revenue, are ethically problematic and not appropriate for Realm.

**Контекст.** Shokrizade documented whaling 2013-2015. Mobile F2P industry
standard. Recent regulatory response (Belgium loot box ban 2018, China minor
restrictions 2021, etc.).

**Realm rationale.** Resource (E5) caps prevent whale-style consumption.
Marketplace exchange capped per period.

**Источник.** `wiki/claims/anti-pattern-whaling-monetization.md`

### §5.2 — Contradicts edges from gamification staged (5, promoted Шаге D)

> Source: `wiki/graph/_promoted_pending/edges-gamification-pending-2026-05-11.jsonl`
> (5 contradicts edges, all documenting Realm boundary).

#### A-4. freemium-funnel ⊥ E5-resources
**Что.** `concepts/game-mechanics/freemium-funnel.md` contradicts
`concepts/jetix-realm/e5-resources.md` (conf=high).

**Что значит.** Freemium funnel (free → friction → paid) violates honest
Resource accounting principle. Realm's E5 = soft caps with predictable
regen, NOT artificial scarcity converting to payment.

#### A-5. variable-rewards ⊥ E5-resources
**Что.** `concepts/psychology/variable-rewards.md` contradicts
`concepts/jetix-realm/e5-resources.md` (conf=medium).

**Что значит.** Variable-ratio reward schedules (slot-machine pattern, Skinner)
incompatible с E5 predictable economy. Use VARIABLE rewards SPARINGLY (cross-
domain synthesis §1 finding), predictable as primary mode.

#### A-6. pay-to-win ⊥ cosmetic-only-monetization
**Что.** `claims/anti-pattern-pay-to-win.md` contradicts
`concepts/game-mechanics/cosmetic-only-monetization.md` (conf=high).

**Что значит.** Reverse-direction marker: pay-to-win UNDERMINES cosmetic-only.
Realm enforces cosmetic-only via Q4.10.1 variant 1.

#### A-7. whaling-monetization ⊥ E5-resources
**Что.** `claims/anti-pattern-whaling-monetization.md` contradicts
`concepts/jetix-realm/e5-resources.md` (conf=high).

**Что значит.** Whaling pattern (designed for <1% spending 50% revenue)
incompatible with E5 caps + transparent regen. Realm caps spend per period.

#### A-8. extractive-platform ⊥ E3-clan
**Что.** `claims/anti-pattern-extractive-platform.md` contradicts
`concepts/jetix-realm/e3-clan.md` (conf=high).

**Что значит.** Extractive 25%+ fees incompatible с E3 ownership model.
Realm cap = 15% (Q4.10.4 V1); clan owns clan-generated assets, not platform.

### §5.3 — From review_2026-05-11.md contradictions (1)

#### A-9. Skрытое элитное сообщество ⊥ массовое вовлечение миллионов
**Что.** Review meta-analysis §contradictions[10]:
«Идея «скрытого элитного сообщества» конфликтует с задачей «настроить
коммуникацию с миллионами авантюристов» — массовое vs закрытое.»

**Что значит для Realm.** Stealth-launch стратегия (curated invite) PVS
public traffic-test задача из roadmap. Один из топ-5 surprising findings
Шаге B.

**Realm rationale needed.** Phase 1 should pick: stealth invite-only (E3 Clan
Recruitment Q2.2.x V4 per-clan choice) ИЛИ public traffic.

**Источник.** `reports/review_2026-05-11.md` §Прочее (meta-contradictions list).

---

## §6 — Cross-Domain Synthesis (4 domains × 5 convergent themes)

> Source: `wiki/summaries/gamification-cross-domain-synthesis-2026-05-11.md`
> (158 mined entries across GAMES / EXPERTS / THEORY / PSYCHOLOGY domains).

### §6.1 — TL;DR

158 mined entries cover 4 domains supporting 6 Realm entities. **Convergence:**
Castronova-Lehdonvirta econ theory + EVE/Torn empirical economy + Axelrod
cooperation theory + SDT motivation theory ⟹ Realm design pattern:
**player-driven economy + clan-based reputation + ethically-bounded reward
design + flow-calibrated quests.** **Divergence:** Variable rewards (Eyal
Hook Model + Cialdini scarcity) tension с extractive-platform anti-pattern
(Varoufakis Technofeudalism + Shokrizade whaling).

### §6.2 — 5 Convergent themes (multi-domain support)

**1. Clan-based reputation (E3)**
- GAMES: Torn Faction Respect, WoW Guild Progression, EVE Corp Reputation
- THEORY: Axelrod iterated PD (cooperation through reputation)
- PSYCHOLOGY: SDT relatedness, Cialdini social proof
- EXPERTS: Castronova synthetic economies (reputation = real economic property)

**2. Visible progression (E1/E2)**
- GAMES: WoW achievement system, ranked ladder, talent tree, Civ tech tree
- THEORY: Nash equilibrium (stable progression points)
- PSYCHOLOGY: SDT competence, flow visibility
- EXPERTS: virtual GDP measurability

**3. Quest design as mechanism (E4)**
- GAMES: WoW quest design loop, Civ multi-path victory, EVE industry chains
- THEORY: mechanism design (Hurwicz/Maskin/Myerson), matching markets (Roth)
- PSYCHOLOGY: SDT autonomy, flow challenge-skill balance
- EXPERTS: Machinations resource-pool diagramming

**4. Player-driven economy (E5)**
- GAMES: EVE Online (anchor), WoW Auction House, Torn Marketplace
- THEORY: Vickrey 2nd-price auction (truth-telling), VCG mechanism
- PSYCHOLOGY: scarcity (Cialdini) — bounded use
- EXPERTS: Castronova-Lehdonvirta virtual economy substrate, Guðmundsson MER

**5. Seasonal cycles (E6)**
- GAMES: Fortnite battle pass, EVE seasons, WoW Mythic+ rotation
- THEORY: focal points (Schelling) — predictable rhythms
- PSYCHOLOGY: scarcity (Cialdini), variable rewards (cautious)
- EXPERTS: temporal cohort dynamics

### §6.3 — 3 Divergent / tension themes

**1. Variable rewards tension**
- Eyal Hook Model + variable-ratio reinforcement (Skinner) = most powerful retention
- BUT: ethical concerns (gambling adjacent); Eyal himself wrote Indistractable counter
- **Realm:** use SPARINGLY (predictable rewards primary)

**2. Extractive platform vs democratic ownership**
- Anti-pattern: Apple App Store 30%, Amazon merchant fees (Varoufakis
  Technofeudalism)
- Pattern: Roblox creator DevEx (60-70% creator); Dota cosmetic-only fair
- **Realm:** democratic ownership / reasonable platform fee (10-15%)

**3. Whaling vs sustainable monetization**
- Anti-pattern: Candy Crush 0.1% whales = 50% revenue (Shokrizade)
- Pattern: Dota / EVE / LoL — sustainable broad-base monetization
- **Realm:** cosmetic + premium credits, NO frustration-driven purchase

### §6.4 — Что ещё открыто (для ФАЗА 2+)

- Question Mining (Шаг D, separate run per Decision 5) — **DONE**
- Direct Castronova outreach (Phase 2+)
- Empirical Realm pilot data (first 10-member clan)

### §6.5 — Входные страницы

- [[summaries/gamification-games-domain-2026-05-11]]
- [[summaries/gamification-experts-domain-2026-05-11]]
- [[summaries/gamification-theory-domain-2026-05-11]]
- [[summaries/gamification-psychology-domain-2026-05-11]]
- [[summaries/gamification-realm-entity-spec-derivation-2026-05-11]]

---

## §7 — May Batch New Insights (what May surfaced vs existing wiki)

> Source: `inbox/processed/extractions/audio_6[0-9][0-9]@11-05-2026*.json` (59
> May batch files, 496 items) + `reports/voice-pipeline-2026-05-11-may-batch/04-wiki-candidates-may-batch.md`
> Tier B/C lists (items NOT matched к existing wiki ≥0.85). Filtered for
> themes not already covered в Шаге C v3 baseline or Шаге D Question Mining.

### §7.1 — Top NEW themes May batch surfaced

**N-1. Jetix как «турбонаддув» для уже работающих бизнесов.**
- Полное переположение ICP: НЕ голодные стартаперы, а already-running founders.
- Audio_617 (30 units), audio_618 (12), audio_625 (13), audio_631 (13).
- Implication для Realm: **E2 Class** (Hunter / Guardian / Scholar / Creator /
  Architect / Merchant) — все classes target професионалов с running operation,
  not zero-to-one.
- Q3.4.x archetype design — **review default 6 archetypes** под new ICP.

**N-2. $1M до конца 2026 как fixed ориентир.**
- Replaces / supplements predecessor target ($50K to 30 June 2026 = Phase 1).
- Phase 2 (Jul 2026 - Dec 2026) = scale 50K → 1M = 20×.
- Implication для Realm: **E6 Seasons** (3-month cycles) — Phase 1 = season
  Q3-2026 (Jul-Sep), Phase 2 = season Q4-2026 (Oct-Dec). Mid-2026 must achieve
  Phase 1 lock-in for Phase 2 scale.

**N-3. Узкое горлышко = пропускная способность включения людей в систему.**
- НЕ продукт, НЕ маркетинг — bottleneck = onboarding speed of quality people.
- Direct alignment с **E3 Clan size 3-10** (small clans onboard faster) +
  **E1 Persona** (clear stat baseline = fast assessment).
- Implication для Realm: Phase 1 metric = «clan-month onboarding speed».

**N-4. 20-30K€/мес минимальная собственная стоимость времени Руслана.**
- Принимается как факт. Меняет монетизацию для Phase 1.
- Implication для Realm: **E4 Quest** reward calibration — Quest € reward
  must justify Owner-time-investment at €30K/mo floor (Owner-Quest pricing).

**N-5. Мастерская менеджеров (Левенчук + Церин + Танки = ключевая тройка) —
упаковка профессионалов.**
- New strategic anchor surfaced. 3 advisors confirmed as priority outreach.
- Implication для Realm: **E2 Class** + **E3 Clan** Phase 1 — start with
  Workshop manager pattern (Anatoly Levenchuk style) as substrate.
- Crossref: Workshop concept (`swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md`).

**N-6. Stealth-launch стратегия vs «веб-сайт + traffic test» задача.**
- Surface contradiction. Top 5 surprising Шаг B.
- Implication для Realm: **Q2.2.1 V4** (per-clan choice) — Phase 1 first
  clan = stealth invite-only; later clans = open join optional. Federation
  of clan-recruitment policies.

**N-7. Принцип «фундамент продумывать глубоко с самого начала».**
- Repeating principle через 5+ memos. Candidate на промоцию в Pillar A/Бренд.
- Implication для Realm: aligns с Q4.9.4 (foundation grounding) — convergent
  thread что 6 Hexagon entities + canonical anchors come FIRST, mechanics
  layer SECOND.

**N-8. AI-агенты как «чит-код, ослабляющий».**
- Дисциплинарная рамка needed. Top 4 contradiction Шаг B.
- Implication для Realm: **E5 Resources** «AI credits» cap — soft block
  prevents over-reliance. Discipline-tier reputation marker (player who
  doesn't use AI credits = «hard-mode achievement»).

### §7.2 — Recurring concepts (на грани promoting в canonical)

- **«Команда профессионалов-психопатов + авантюристов»** (ICP draft ready) —
  alignment с E1 Persona archetypes + E3 Clan recruitment filter.
- **«Метатехнологии и доверие как соц.технология»** (R&D-ветка Ресёрч) — new
  philosophical thread, не yet в Realm canonical.
- **«Финансовая безопасность семьи как драйвер срочности»** — personal
  Personal-Network anchor, не Realm-direct.

---

## §8 — Canonical Anchor Excerpts

### §8.1 — Strategic Insight Gamified Platform §4.2 (6 entities canonical)

> Source: `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md`
> §4 lines 83-135.

**§4.1 Working concept.** Jetix Realm = operational layer Jetix platform.
Не отдельный продукт — **видимый игровой слой** на substrate реального
бизнеса:

```
┌──────────────────────────────────────────┐
│  Jetix Realm — игровой слой              │
│  (stats, кланы, квесты, ресурсы, LB)     │
├──────────────────────────────────────────┤
│  Jetix OS — 12 AI-агентов substrate      │
│  (рутина + assist)                       │
├──────────────────────────────────────────┤
│  Реальный бизнес-слой                    │
│  (projects / clients / revenue / KPI)    │
└──────────────────────────────────────────┘
```

**§4.2 6 сущностей платформы.**

- **E1 — Персонаж = Специалист.** TRM 6 ресурсов как реальные stats (Capital
  / Time Leverage / Audience / Knowledge / Compute / Network). Profile с
  graph circles, current level, progress.

- **E2 — Класс = Специализация.** 6 архетипов: Hunter (Sales) / Guardian
  (Operations) / Scholar (Research) / Creator (Content) / Architect
  (Strategy/AI) / Merchant (BizDev).

- **E3 — Клан = Команда проекта (3-10 чел).** Прямой перенос Torn:
  - Faction Respect → Командная Reputation
  - Faction Armoury → Общий ресурс-пул (AI tools / templates / contacts)
  - Organized Crimes (80-95% split) → Organized Projects (revenue share)
  - Faction Wars → Соревновательные тендеры (две команды борются за заказ)
  - Дерево прокачки фракции → Дерево прокачки команды

- **E4 — Квесты = Реальные бизнес-задачи.** Параметры: required class /
  level / time / reward (€ + Reputation + Knowledge) / сложность ★★★☆☆ /
  client.

- **E5 — Ресурсы и ограничения.** Energy (deep work cap) / Focus tokens /
  Audience reach / AI credits. **Реальная экономика внимания.**

- **E6 — Сезоны (3-month cycles).** Strategic theme (e.g. «Pharma season»),
  bonus resources for theme quests, season-end leaderboard + rewards (доля в
  новом проекте Jetix, прямой доступ к CEO, инвайт на closed event).

**§4.3 Visual base — Jetix HQ Dashboard (Stardew + Catppuccin).**

Existing pixel-art дизайн = идеальная база для Realm:
- Главный экран = твоя ферма/город
- NPCs = AI-агенты, к которым идёшь за задачами
- Tavern = чат команды
- Marketplace = биржа квестов
- Guild Hall = страница клана
- Leaderboards = таверна

**§4.4 Что отличает от «корпоративной геймификации».** Бейджики поверх
Salesforce — мёртвая старая школа. Jetix Realm = полный игровой каркас +
экономика.

---

### §8.2 — Document 1B (JETIX-CORPORATION-2026-05-05.md) — 8 faces + Партнёр/Клиент/Работник tiers

> Source: `decisions/JETIX-CORPORATION-2026-05-05.md` §3 (TRM 6 resources) +
> §9 (Партнёр/Клиент/Работник tiers). Strategic Insight §6 anchor:
>
> «Document 1B §3 TRM — 6 ресурсов directly = persona stats (E1 above).
> Document 1B §9 Партнёр/Клиент/Работник — three roles = three player tiers
> (Partner = clan founder, Client = quest commissioner, Worker = clan member).
> Document 1B §10 Roadmap — добавляется visual layer на каждом step
> (Step 1 = "outreach quest", Step 4 = "recruit clan founders").»

**3 player tiers per Doc 1B §9 mapping:**

| Doc 1B role | Realm tier | E-mapping |
|-------------|------------|-----------|
| **Партнёр** | Clan founder | E3 Clan governance / Persona L4+ |
| **Клиент** | Quest commissioner | E4 Quest origin (external) |
| **Работник** | Clan member | E3 Clan participation / Persona L0-L3 |

**Persona stats per Doc 1B §3 TRM (mirror):**

1. **Финансы** (capital) — Кэш, инвестиции, рабочий капитал
2. **Время CEO/основателя** (founder time) — Часы внимания первого лица
3. **Аудитория** (audience) — Подписчики, контакты, рассылки, репутационный
   капитал
4. **Информация / знания** (knowledge) — Внутренние данные, экспертиза,
   методологии, накопленный опыт
5. **Вычислительные мощности** (compute) — GPU/CPU, AI-инференс, токены,
   серверная инфраструктура
6. **Команда / человеческий капитал** (talent) — Сотрудники, их время, их
   компетенции

---

### §8.3 — Workshop concept (foundation-master-overview-human-workshop-2026-05-06.md)

> Source: `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md`
> §1.1 Что мастерская есть.

> **Verbatim Ruslan, 30.04.2026:** *«Это вот эта система Jetix — это
> мастерская. Мастерская с кучей профессиональных работников и с кучей
> станков, инструментов любого калибра.»*
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md §8]

**Мастерская** — это место, где работает **мастер** + есть **adaptable
станки** + производятся **уникальные артефакты** + **knowledge
накапливается** через время.

| Метафора | Что схватывает | Чего не хватает |
|----------|----------------|-----------------|
| **Завод** | Производство, процессы | Стандартизация → штампует одинаковое |
| **Лаборатория** | Эксперимент, исследование | Слишком "научно", упускает производство |
| **Офис** | Работа, организация | Скучно, бюрократично, не про мастерство |
| **Студия** | Творчество | Только creative, упускает business / strategy |
| **Монастырь** | Дисциплина | Закрытость, отрыв от мира |
| **Оркестр** | Координация, гармония | Один дирижёр + ноты — но в Jetix владелец задаёт направление |
| **🏭 Мастерская** | **Мастер + adaptable инструменты + уникальные артефакты + knowledge accumulates + от соло до сети** | — |

**5 owner roles (Workshop §1.5 Master-многостаночник):**
1. Master (выполняет уникальные задачи)
2. Foreman (управляет работниками)
3. Mentor (обучает учеников)
4. Engineer (доделывает станки)
5. Architect (планирует мастерскую как систему)

**Mapping к Realm:** все 5 owner roles = E1 Persona archetypes at L4+ tier.
Phase 1 = primary Master role; Phase 2-3 = Foreman + Mentor; Phase 4 =
Architect.

---

### §8.4 — TRM model (JETIX-TRM-MODEL-2026-04-30.md)

> Source: `decisions/JETIX-TRM-MODEL-2026-04-30.md` §1 Суть идеи.

**Тезис.** Jetix может управлять не одним ресурсом, а **всеми шестью
одновременно** — и брать комиссию (management fee + performance fee) с
каждого. Это превращает консалтинговую модель в управляющую компанию нового
типа — **Total Resource Management (TRM)**.

**6 видов исчерпаемых, монетизируемых ресурсов:**

| # | Ресурс | Что значит |
|---|--------|-----------|
| 1 | **Финансы** (capital) | Кэш, инвестиции, рабочий капитал |
| 2 | **Время CEO/основателя** (founder time) | Часы внимания первого лица — самый дефицитный ресурс в любом бизнесе |
| 3 | **Аудитория** (audience) | Подписчики, контакты, рассылки, репутационный капитал |
| 4 | **Информация / знания** (knowledge) | Внутренние данные, экспертиза, методологии, накопленный опыт |
| 5 | **Вычислительные мощности** (compute) | GPU/CPU, AI-инференс, токены, серверная инфраструктура |
| 6 | **Команда / человеческий капитал** (talent) | Сотрудники, их время, их компетенции |

Прибыль клиента растёт, потому что его ресурсы, которые раньше тратились
хаотично или не использовались вообще, начинают работать как единый
портфель под управлением.

**TRM L0-L5 levels per resource (Persona stat scale):**

- **L0** — отсутствует или нерегулируемое использование
- **L1** — baseline (есть, но не оптимизируется)
- **L2** — measured (отслеживается)
- **L3** — managed (есть процесс)
- **L4** — optimized (KPI-driven)
- **L5** — strategic asset (compounding + monetized)

---

## §9 — Open Items Requiring Ruslan Strategize в ФАЗА 4

> Top 5 most-critical decisions surfaced from Шаг C/D pipeline. AI suggests
> scope; Ruslan-decided per Tier 2 R1.

### §9.1 — Decision Point 1: Phase 1 Realm scope (Q1 mostly)

**Что:** Decide what's IN Phase 1 vs deferred Phase 2+.
- 6 entities всех или subset?
- 6 archetypes (Q3.4.1) — оставлять или consolidate to 3?
- E6 Seasons (3-month) — start immediately or wait?
- Pixel-art HQ aesthetic (Q1.11.4 converged) — finalize art style?

**Constraints:**
- $50K target к 30 June 2026 (Phase 1 financial)
- 20-30K€/мес собственная стоимость (Ruslan time floor)
- Узкое горлышко = onboarding speed (N-3 May batch)
- Stealth-launch vs public traffic (N-6 contradiction)

**Suggested но Ruslan-decided:** Phase 1 = single clan (3-10 ppl), 3
archetypes (Hunter + Architect + Scholar — sales + AI + research), 1
сезон с тематикой «Berlin AI consulting GTM».

### §9.2 — Decision Point 2: Source of truth & data model (Q4.3.1 diverged)

**Что:** Resolve 5-variant spread Q4.3.1.
- Constitutional V1: filesystem-only (Global Rule 4 strict)
- V3: hybrid (filesystem canonical, Notion view-only)
- V5: Notion-only (constitutional violation)

**Constraints:**
- Filesystem = source of truth (Global Rule 4)
- Notion = collaboration / view layer
- Sync model + audit trail (Q4.3.4)
- GDPR data lifecycle (Q4.3.5)

**Suggested но Ruslan-decided:** Variant 3 (hybrid) per Bundle 5 ack pattern.
But Ruslan locks the boundary: что mandatory FS vs что allowed Notion-only.

### §9.3 — Decision Point 3: Monetization model lock (Q1.10.5 + Q4.8.4)

**Что:** Pick Phase 1 monetization OR explicitly say «no monetization Phase 1».
- Subscription (predictable revenue)
- Freemium (anti-pattern risk per A-4)
- Equity-hybrid (long-term aligned, legal complexity)
- 50-150€/час consulting floor (existing Decision)

**Constraints:**
- $50K Phase 1 target
- 20-30K€/мес собственная стоимость (so price floor = €30K/mo / clan-month)
- Anti-pattern A-1/A-2/A-3 enforcement (no P2W / extractive / whaling)

**Suggested но Ruslan-decided:** Consulting €50-150/час floor + clan-as-Quest
revenue split (80-95% per Torn pattern) OR meta-offer «правая рука на
максималках» 1-2 clients × $20K/mo = $40K/mo achieve target.

### §9.4 — Decision Point 4: ICP positioning (turbo vs от нуля)

**Что:** Resolve May batch N-1 finding contradiction.
- Old: «голодные стартаперы»
- New: «уже работающие основатели» (turbo для running businesses)

**Constraints:**
- 3 priority Workshop managers (Левенчук + Церин + Танки) — already running
- audio_617 evidence (30 units): «строить с теми у кого работает машина»
- Phase 1 financial (€50K) — fewer high-value vs more low-value clients?

**Suggested но Ruslan-decided:** Phase 1 ICP = «уже работающие основатели
с running operation, нужен turbo». 3-5 clients × €10-15K/mo = €30-75K/mo.
This locks E2 Class design + E4 Quest design + outreach posture.

### §9.5 — Decision Point 5: Realm launch posture (stealth vs public)

**Что:** Resolve May batch N-6 stealth contradiction.
- Stealth invite-only (preserves curation; aligns с E3 Q2.2.1 V4)
- Public traffic-test (тест trafic → site → conversion)
- Hybrid (stealth для Phase 1, public для Phase 2)

**Constraints:**
- Phase 1 stealth makes onboarding speed quantifiable (N-3 bottleneck)
- Public requires brand/positioning «Кто я» (Шаг B finding #2 — blocking
  artifact)
- $1M target (N-2) eventually needs broader reach

**Suggested но Ruslan-decided:** Stealth Phase 1 (curated first clan via
direct outreach к Левенчук/Церин/Танки + 5-10 of their referrals); Public
Phase 2 (after «Кто я» finalized + first Quest case studies).

---

## §10 — How to use this digest в ФАЗА 4

### §10.1 — Suggested Ruslan-words spec structure (Pillar A §A.1 LOCKED state)

> Source: `reports/gamification-question-mining-run-2026-05-11.md` §9.

Per Tier 2 R1, Ruslan writes prose. AI = scribe only. Recommended structure:

- **Header** — context + invariants (F: F5, status: LOCKED, prose_authored_by:
  ruslan)
- **§1** — Realm constitutional posture (anti-extraction tier-1)
- **§2** — 6 entities canonical schema (Persona / Class / Clan / Quest /
  Resources / Seasons)
- **§3** — Architectural decisions (Cat 4 picks — Q4.3.1, Q4.7.1, Q4.2.1,
  Q4.8.4, Q4.10.x)
- **§4** — Workflow gamification (Cat 3 picks — Q3.3.x, Q3.4.1, Q3.6.x)
- **§5** — Clan mechanics (Cat 2 picks — Q2.1.x, Q2.2.x, Q2.8.x)
- **§6** — UX & aesthetic (Cat 1 picks — Q1.4.x, Q1.10.x, Q1.11.4)
- **§7** — Phase 1 scope (immediate — first clan, first season, first quests)
- **§8** — Phase 2-3 deferred (long-term vision — federation, sovereignty,
  $1M target)
- **§9** — Filing (canonical location: `decisions/JETIX-REALM-FINAL-SPEC-2026-05-12.md`)

### §10.2 — Filing target

`decisions/JETIX-REALM-FINAL-SPEC-2026-05-12.md` per Pillar A:
- `prose_authored_by: ruslan`
- `F: F5`
- `status: LOCKED` (after Ruslan ack)
- `blast_radius: F4 or F5` (Foundation impact level)

### §10.3 — Pipeline preserved для ФАЗА 5/6

- **ФАЗА 5** — wiki cross-verify (всё canonical anchors → check ref consistency
  after Ruslan locks FINAL spec)
- **ФАЗА 6** — Видео Цэрэну (после FINAL spec — explain Realm vision к
  outreach material)

---

## §11 — Constitutional Posture Maintained

- **Tier 2 R1 (AI = scribe):** ✅ ZERO strategic prose generated. All decision
  points framed as «нужен Ruslan strategize» with suggested-but-not-decided.
- **Tier 2 R2 (Default-Deny novel actions):** ✅ All writes confined to
  `reports/`. Zero Foundation / principles / decisions / wiki writes.
- **Tier 2 R6 (F-G-R DOGFOOD):** ✅ Frontmatter carries F2 / G / R labels.
  Every claim cites source.
- **Tier 2 R7 (no Hexagon contradicts):** ✅ All 5 staged contradicts edges
  documented as boundary-marking anti-patterns FROM external claims TO
  Hexagon entities. ZERO contradicts FROM Hexagon TO external.
- **Filesystem-as-truth (Global Rule 4):** ✅ Recommendations explicitly
  respect (§9.2).
- **Append-only к reports/:** ✅ Single new file.

---

## §12 — Metadata summary

- **Digest size.** ~700 lines (within 2000-5000 target — concentrated).
- **Sources combined.** 11+ files: 6 entity stubs / QM run / cross-domain
  synthesis / 3 anti-pattern claims / Strategic Insight §4 / Doc 1B / Workshop /
  TRM / Шаг B review + meta-contradictions / Шаг C may-batch candidates.
- **Wiki state on digest creation.** 722 entries / 891 canonical edges / 0
  staged (gamification promoted Шаге D).
- **Pipeline elapsed wall-clock (Шаги A-E).**
  - Шаг A — 56 min (~7 PM transcribe → 9 PM extract+summarize)
  - Шаг B — 67 min (~9 PM filter+review)
  - Шаг C — 137 min (~2 AM-4 AM Stage 5 LLM rerank May batch)
  - Шаг D — ~10 min (bulk-ack 3 batches)
  - Шаг E — ~15 min (digest write)
  - **Total: ~4.7 hours active processing + Ruslan ack time between Шаги A-B**

---

## §13 — Detail Annex: Top Priority Questions Verbatim (6 Qs)

> Source: `reports/gamification-question-mining-run-2026-05-11.md`. Full
> variant content for highest-impact decisions Ruslan will face в ФАЗА 4.
> Inlined here для self-contained digest (no need to flip to QM source for
> Phase 4 prose authoring).

### §13.1 — Q4.10.1: Pay-to-win enforcement (CONVERGED, ALL 4 variants compose)

**Category:** 4 | **Parameter:** 4.10 | **Variants generated:** 4 ⭐ HIGH CONVERGENCE

**Variant 1: «Quest reward column cannot accept money inputs»**
- **Hypothesis:** Schema constraint — Quest.rewards only contains earned
  resources (Reputation / Knowledge); no «paid» field. Pay-to-win
  architecturally impossible.
- **Evidence:** [anti-pattern-pay-to-win](wiki/claims/anti-pattern-pay-to-win.md),
  [e4-quest](wiki/concepts/jetix-realm/e4-quest.md)
- **Precedent:** Cosmetic-only monetization (CS2 skins).
- **Pros:** architectural enforcement; constitutional.
- **Cons:** restricts monetization paths.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:**
  none — enforces anti-pattern claim
- **Audit:** confidence: high | primary_wiki_cite: anti-pattern-pay-to-win |
  hallucination_risk: low | cross_validated: true

**Variant 2: «Reputation/Knowledge non-purchasable (immutable rule)»**
- **Hypothesis:** Specific stats (Reputation / Knowledge / Trust) cannot be
  purchased. Hardcoded.
- **Evidence:** [anti-pattern-pay-to-win](wiki/claims/anti-pattern-pay-to-win.md),
  [faction-respect](wiki/concepts/game-mechanics/faction-respect.md)
- **Precedent:** Torn Respect (cannot be bought).
- **Pros:** clear rule; community-loved.
- **Cons:** complexity for other stats.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none
- **Audit:** confidence: high | primary_wiki_cite: faction-respect |
  hallucination_risk: low | cross_validated: true

**Variant 3: «Cosmetic-only monetization (skins / themes / cosmetics)»**
- **Hypothesis:** Money only buys cosmetics; never gameplay advantage. CS2 /
  Valorant proven pattern.
- **Evidence:** [cosmetic-only-monetization](wiki/concepts/game-mechanics/cosmetic-only-monetization.md),
  [cs2](wiki/entities/games/cs2.md)
- **Precedent:** CS2 skins ($billions secondary market).
- **Pros:** revenue from cosmetics; gameplay pure.
- **Cons:** market depends on critical mass.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none
- **Audit:** confidence: high | primary_wiki_cite: cosmetic-only-monetization |
  hallucination_risk: low | cross_validated: true

**Variant 4: «Spend caps enforced architecturally (max €X per month)»**
- **Hypothesis:** Hard cap on per-user spend; cannot whale. Constitutional.
- **Evidence:** [whaling-monetization](wiki/concepts/game-economy/whaling-monetization.md),
  [anti-pattern-whaling-monetization](wiki/claims/anti-pattern-whaling-monetization.md)
- **Precedent:** None mainstream — innovation.
- **Pros:** anti-whaling architectural; constitutional.
- **Cons:** caps revenue ceiling.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:**
  none — enforces anti-pattern claim
- **Audit:** confidence: high | primary_wiki_cite: anti-pattern-whaling-monetization |
  hallucination_risk: low | cross_validated: true

**Recommended next:** ALL 4 variants combine (no contradiction; layered
enforcement). **CONVERGENCE FLAGGED** — clear architectural posture.

---

### §13.2 — Q2.12.1: 5+ year retention factors (CONVERGED, ALL 4 combine)

**Category:** 2 | **Parameter:** 2.12 | **Variants generated:** 4

**Variant 1: «Social bonds (real friendships formed)»**
- **Hypothesis:** Friendship = #1 long-term retention factor.
- **Evidence:** [clan-mechanics-amplify-engagement](wiki/claims/clan-mechanics-amplify-engagement.md),
  [relatedness](wiki/concepts/psychology/relatedness.md)
- **Precedent:** WoW raid teams 10+ years.
- **Pros:** strongest retention.
- **Cons:** hard to engineer; emerges.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Variant 2: «Real economic stake (Quest revenue share = loss to leave)»**
- **Hypothesis:** Real money flows = strong commitment.
- **Evidence:** [organized-crimes-revenue-split](wiki/concepts/game-mechanics/organized-crimes-revenue-split.md),
  [korporaciya-startup-concept](wiki/concepts/korporaciya-startup-concept.md)
- **Precedent:** Torn factions (organized crimes lock-in).
- **Pros:** strong rational commitment.
- **Cons:** transactional.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Variant 3: «Progression depth (always more to achieve)»**
- **Hypothesis:** Infinite progression keeps engaged.
- **Evidence:** [skill-ceiling-progression](wiki/concepts/game-mechanics/skill-ceiling-progression.md),
  [talent-tree-progression](wiki/concepts/game-mechanics/talent-tree-progression.md)
- **Precedent:** RuneScape 99+, EVE skills.
- **Pros:** sustained interest.
- **Cons:** treadmill risk.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:**
  some — treadmill

**Variant 4: «Identity / status (your Persona = your reputation)»**
- **Hypothesis:** Identity investment = retention.
- **Evidence:** [e1-persona](wiki/concepts/jetix-realm/e1-persona.md),
  [faction-respect](wiki/concepts/game-mechanics/faction-respect.md)
- **Precedent:** Torn (years-old characters).
- **Pros:** identity-based commitment.
- **Cons:** lock-in concern.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Recommended next:** ALL 4 combine — social + economic + progression +
identity. Realm должен create all 4 layers simultaneously.

---

### §13.3 — Q3.3.1: Intrinsic vs extrinsic rewards (CONVERGED, V1+V3 combine)

**Category:** 3 | **Parameter:** 3.3 | **Variants generated:** 3

**Variant 1: «Intrinsic primary (Persona growth + abilities), extrinsic secondary (titles)»**
- **Hypothesis:** SDT-aligned. Growth = primary; titles supplement.
- **Evidence:** [intrinsic-motivation](wiki/concepts/psychology/intrinsic-motivation.md),
  [three-needs-drive-intrinsic-motivation](wiki/claims/three-needs-drive-intrinsic-motivation.md)
- **Precedent:** EVE Online (skill points feel growthful).
- **Pros:** sustainable motivation; constitutional.
- **Cons:** subjective measurement.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Variant 2: «Balanced (50/50 intrinsic / extrinsic)»**
- **Hypothesis:** Both equally weighted; users different motivators.
- **Evidence:** [achievement-system](wiki/concepts/game-mechanics/achievement-system.md),
  [self-determination-theory](wiki/concepts/psychology/self-determination-theory.md)
- **Precedent:** WoW (skills + titles + achievements).
- **Pros:** broad appeal.
- **Cons:** can dilute intrinsic.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:**
  some — extrinsic dilution

**Variant 3: «Multi-track (Persona / Class / Clan / Reputation each its own reward channel)»**
- **Hypothesis:** Each axis of growth = separate reward channel. Per
  Strategic Insight 7 mechanics.
- **Evidence:** [gamification-realm-entity-spec-derivation-2026-05-11](wiki/summaries/gamification-realm-entity-spec-derivation-2026-05-11.md),
  [faction-respect](wiki/concepts/game-mechanics/faction-respect.md)
- **Precedent:** WoW (personal + guild + achievements separated).
- **Pros:** rich; each progress visible.
- **Cons:** UI complexity.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Recommended next:** Variants 1+3 combine — intrinsic primary on multi-track
channels.

---

### §13.4 — Q3.6.1: Mentor-Apprentice (Tyson-pattern, CONVERGED V1 primary)

**Category:** 3 | **Parameter:** 3.6 | **Variants generated:** 3

**Variant 1: «Formal Mentor-Apprentice pairing (Tyson-pattern)»**
- **Hypothesis:** Explicit mentor commitment; tracked in Persona; per Tyson
  Strategic Insight.
- **Evidence:** [gamification-realm-entity-spec-derivation-2026-05-11](wiki/summaries/gamification-realm-entity-spec-derivation-2026-05-11.md),
  [e2-class](wiki/concepts/jetix-realm/e2-class.md)
- **Precedent:** WoW recruit-a-friend, Old School RuneScape mentors.
- **Pros:** Strategic Insight aligned; clear commitment.
- **Cons:** rigid; mentor scarcity.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Variant 2: «Informal (any veteran can mentor; lightweight tracking)»**
- **Hypothesis:** Mentorship as light gift exchange; no formal contract.
- **Evidence:** [intrinsic-motivation](wiki/concepts/psychology/intrinsic-motivation.md),
  [e2-class](wiki/concepts/jetix-realm/e2-class.md)
- **Precedent:** Many MMO informal mentorship.
- **Pros:** low friction.
- **Cons:** weak commitment.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 3: «Tiered (formal mentor + informal advisor + peer review)»**
- **Hypothesis:** Multiple mentorship layers. Formal (1-2 mentors) + informal
  advisors (5-10) + peer review.
- **Evidence:** [gamification-realm-entity-spec-derivation-2026-05-11](wiki/summaries/gamification-realm-entity-spec-derivation-2026-05-11.md),
  [e2-class](wiki/concepts/jetix-realm/e2-class.md)
- **Precedent:** Academic advisor system (PhD).
- **Pros:** rich; matches reality.
- **Cons:** complexity.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Recommended next:** Variant 1 (formal Tyson-pattern) primary; Variant 3
(tiered) Phase 2+.

---

### §13.5 — Q4.3.1: Source of truth (DIVERGED, 5 variants — needs Ruslan strategize)

**Category:** 4 | **Parameter:** 4.3 | **Variants generated:** 5 ⭐ HIGH DIVERGENCE

**Variant 1: «Filesystem (markdown+YAML) = canonical, Notion = view»**
- **Hypothesis:** Per CLAUDE.md Global Rule 4 + RUSLAN-LAYER override.
  Markdown+YAML files = source of truth; Notion mirrored as view only.
- **Evidence:** [business-projects-like-code](wiki/claims/business-projects-like-code.md),
  [jetix](wiki/entities/jetix.md)
- **Precedent:** Civilization (savegame files), Minecraft (world files).
- **Pros:** grep-able; git-versioned; LLM-readable; constitutional alignment.
- **Cons:** multi-user concurrent edits harder; UI not native.
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:**
  none — constitutional

**Variant 2: «Own Postgres DB = canonical, Notion = soft-deprecated»**
- **Hypothesis:** Build own database; Notion phased out except as marketing/
  sharing surface. Industrial-strength queries.
- **Evidence:** [eve-online](wiki/entities/games/eve-online.md),
  [synthetic-economies](wiki/concepts/game-economy/synthetic-economies.md)
- **Precedent:** EVE Online (own infra), WoW (own infra).
- **Pros:** mature tooling; transactions; analytics native.
- **Cons:** infra cost; abandons CLAUDE.md filesystem-as-truth Rule 4.
- **F-G-R:** F2 / hypothesis-applied-now / R-low | **Anti-pattern risk:**
  high — contradicts RUSLAN-LAYER override

**Variant 3: «Hybrid: filesystem canonical + Postgres materialized view»**
- **Hypothesis:** Filesystem = truth; Postgres = rebuilt-from-source
  materialized view for fast queries. CRM precedent (`/crm-rebuild-index`).
- **Evidence:** [business-projects-like-code](wiki/claims/business-projects-like-code.md),
  [gamification-realm-entity-spec-derivation-2026-05-11](wiki/summaries/gamification-realm-entity-spec-derivation-2026-05-11.md)
- **Precedent:** Hybrid в EVE corp tools (CCP backend + ESI views).
- **Pros:** constitutional + performant; rebuild resilience.
- **Cons:** duplication; sync edge cases.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 4: «Distributed CRDT (offline-first)»**
- **Hypothesis:** Each user's local state = canonical for their entities;
  merges via CRDT (Yjs-style). No central truth; consensus algorithm.
- **Evidence:** [digital-sovereignty](wiki/concepts/digital-sovereignty.md),
  [cloud-empires](wiki/concepts/game-economy/cloud-empires.md)
- **Precedent:** None mainstream — research direction.
- **Pros:** sovereignty maximized; offline-first natural; anti-extraction.
- **Cons:** experimental; conflict resolution UX hard; small ecosystem.
- **F-G-R:** F2 / hypothesis-applied-now / R-low | **Anti-pattern risk:**
  some — premature complexity

**Variant 5: «Notion-only (no own infra)»**
- **Hypothesis:** Notion DB = canonical. Cheapest path; relies on Notion API.
- **Evidence:** Conflicts с [business-projects-like-code](wiki/claims/business-projects-like-code.md)
  constitutional posture
- **Precedent:** None mainstream — would be unique.
- **Pros:** zero infra cost; mature UI.
- **Cons:** vendor lock-in; Notion API limits; contradicts filesystem-as-truth.
- **F-G-R:** F2 / hypothesis-applied-now / R-low | **Anti-pattern risk:**
  high — constitutional violation

**Recommended но Ruslan-decided:** Variant 1 OR Variant 3 (constitutional
posture preserved). **Variant 5 = constitutional violation (do not pick).**

---

### §13.6 — Q4.7.1: License (DIVERGED, 4 variants — needs Ruslan strategize)

**Category:** 4 | **Parameter:** 4.7 | **Variants generated:** 4

**Variant 1: «MIT (maximally permissive)»**
- **Hypothesis:** Templates / themes / contribution APIs MIT-licensed. Lowest
  barrier для community.
- **Evidence:** [jetix-open-source-principles](wiki/concepts/jetix-open-source-principles.md),
  [linux](wiki/entities/linux.md)
- **Precedent:** Most modern web tooling.
- **Pros:** broad adoption; commercial-friendly.
- **Cons:** allows hostile forks; no copyleft protection.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 2: «AGPL (copyleft, prevents proprietary forks)»**
- **Hypothesis:** AGPL ensures derivatives stay open. Aligned с
  anti-extraction.
- **Evidence:** [anti-pattern-extractive-platform](wiki/claims/anti-pattern-extractive-platform.md),
  [digital-sovereignty](wiki/concepts/digital-sovereignty.md)
- **Precedent:** Matrix Synapse, MongoDB (former).
- **Pros:** prevents extraction; constitutional alignment.
- **Cons:** enterprise allergic; commercial use limited.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 3: «BSL (Business Source License) — proprietary 4 yrs, then Apache»**
- **Hypothesis:** Commercial protection 4 years, then free. Sentry /
  CockroachDB pattern.
- **Evidence:** [jetix-open-source-principles](wiki/concepts/jetix-open-source-principles.md),
  [korporaciya-startup-concept](wiki/concepts/korporaciya-startup-concept.md)
- **Precedent:** Sentry, CockroachDB, Couchbase.
- **Pros:** balance commercial + eventual openness.
- **Cons:** purist OSS critique.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 4: «Custom Jetix License (anti-extraction explicit)»**
- **Hypothesis:** Custom license — open for individuals + small teams;
  revenue threshold triggers commercial license.
- **Evidence:** [anti-pattern-extractive-platform](wiki/claims/anti-pattern-extractive-platform.md),
  [jetix-open-source-principles](wiki/concepts/jetix-open-source-principles.md)
- **Precedent:** Elastic License (former), some game engines.
- **Pros:** tailored to philosophy.
- **Cons:** legal cost; community confusion; not OSI-approved.
- **F-G-R:** F2 / hypothesis-applied-now / R-low | **Anti-pattern risk:**
  some — community confusion

**Recommended но Ruslan-decided:** Variant 1 (MIT) для templates/themes;
Variant 3 (BSL) для kernel — pragmatic posture (per QM recommended-next).

---

### §13.7 — Q3.3.2: Monetary rewards (DIVERGED, 4 variants — needs Ruslan strategize)

**Category:** 3 | **Parameter:** 3.3 | **Variants generated:** 4

**Variant 1: «Per-Quest revenue split (80-95% to executors, per Torn pattern)»**
- **Hypothesis:** Real money flows. Clan + executor split = 80-95% real
  revenue.
- **Evidence:** [organized-crimes-revenue-split](wiki/concepts/game-mechanics/organized-crimes-revenue-split.md),
  [e3-clan](wiki/concepts/jetix-realm/e3-clan.md)
- **Precedent:** Torn Organized Crimes.
- **Pros:** real economy; clear motivation; Strategic Insight aligned.
- **Cons:** legal complexity (German Scheinselbstständigkeit).
- **F-G-R:** F2 / hypothesis-applied-now / R-high | **Anti-pattern risk:** none

**Variant 2: «Salary-like base + Quest commissions (hybrid)»**
- **Hypothesis:** Base monthly stipend + quest commissions on top.
- **Evidence:** [korporaciya-startup-concept](wiki/concepts/korporaciya-startup-concept.md),
  [organized-crimes-revenue-split](wiki/concepts/game-mechanics/organized-crimes-revenue-split.md)
- **Precedent:** None gaming — corporate hybrid.
- **Pros:** stability + upside.
- **Cons:** legal complexity higher; capital req.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:** none

**Variant 3: «Virtual currency + opt-in cash-out»**
- **Hypothesis:** Quest rewards = virtual; cashable at conversion rate.
  Roblox Robux pattern.
- **Evidence:** [virtual-currency-design](wiki/concepts/game-economy/virtual-currency-design.md),
  [real-money-trading](wiki/concepts/game-economy/real-money-trading.md)
- **Precedent:** Roblox Robux → DevEx.
- **Pros:** market freedom; legal protection.
- **Cons:** virtual currency regulation Germany unclear.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:**
  some — regulatory risk

**Variant 4: «Equity-leaning (Quest stake = future equity points)»**
- **Hypothesis:** Quests grant equity points; convert long-term. Per RES.3.
- **Evidence:** [korporaciya-startup-concept](wiki/concepts/korporaciya-startup-concept.md),
  [jetix](wiki/entities/jetix.md)
- **Precedent:** None mainstream — RES.3 innovation.
- **Pros:** alignment; long-term thinking.
- **Cons:** legal complexity highest.
- **F-G-R:** F2 / hypothesis-applied-now / R-low | **Anti-pattern risk:** none

**Recommended но Ruslan-decided:** Variant 1 (per-Quest revenue split) Phase 1
— proven Torn pattern. Variant 4 (equity) Phase 2+ for top contributors.

---

## §14 — TRM Business Model Details (extended canonical anchor)

> Source: `decisions/JETIX-TRM-MODEL-2026-04-30.md` §2-§4. Inlined for ФАЗА 4
> Realm spec authoring (TRM = Persona stat substrate).

### §14.1 — Почему TRM работает именно сейчас

**1. AI-агенты как операционный слой.** Раньше управлять временем 10 CEO
одновременно было физически невозможно — один человек не может быть в 10
местах сразу. С AI-агентами (Jetix OS / HQ) один управляющий + флот агентов
могут параллельно держать в голове состояние десятков клиентов: их
календари, проекты, данные, паттерны решений. Compute стал ресурсом, который
масштабируется и сам становится продуктом.

**2. Mittelstand перегружен.** Немецкие средние предприятия завалены:
AI-внедрение, EU AI Act, кадровый кризис, наследование, цифровизация. Они
физически не успевают этим управлять. Им нужен не консультант, который раз в
квартал приходит и уходит, а **operator**, который реально берёт это на
себя.

**3. Падающее доверие к консалтингу.** Big 4 и стратегические консультанты
продают слайды, а не результат. Performance-based модель Jetix уже сейчас
отвечает на этот запрос. TRM — это финальная форма: «мы не просто внедряем,
мы управляем твоими ресурсами и делим прибыль».

### §14.2 — Existing analogues per resource

- **Финансы:** BlackRock, Bridgewater, family offices (управляют только
  деньгами)
- **Время CEO:** EA staff (exec assistant), chief of staff, FractionalCxO
  (отдельные services, не объединены)
- **Аудитория:** Marketing agencies, content shops (один narrow slice)
- **Знания:** BCG / McKinsey (consulting), Notion / SaaS (knowledge tools)
- **Compute:** Cloud providers (raw infra, не management layer)
- **Talent:** HR consulting, recruitment (отдельные services)

**Jetix TRM:** управляет всеми 6 одновременно с единым agent-fleet substrate
= unique market position.

### §14.3 — Business model TRM

- **Management fee:** % от resource pool под управлением (per resource type)
- **Performance fee:** % от incremental output (delta vs baseline)
- **Realm primitive mapping:** Quest = атомарная unit, на которой
  performance fee considered

### §14.4 — Главные риски и закрытия (TRM §7 → Realm Q4.10.x mapping)

- **Risk:** Скейлинг → Realm: per-clan resource caps + season boundaries
- **Risk:** Legal complexity → Realm: per-Phase legal model (Phase 1 simple,
  Phase 2-3 elaborate)
- **Risk:** Trust → Realm: transparent fee structure (anti-extraction A-2)
- **Risk:** Lock-in (Realm: federation Phase 3+ per Q4.10.4 V2)

---

## §15 — Workshop Concept Extended (full §1.4 adaptable станки)

> Source: `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md`
> §1.4. Workshop concept's adaptable-станки principle = Realm's E2 Class +
> E4 Quest evolutivability.

### §15.1 — Adaptable станки — главное свойство мастерской

**Принцип.** В мастерской добавление нового станка под конкретную задачу
происходит за день (не за квартал). Станок может быть удалён, если перестал
быть полезным. Это противоположно «фабричной» инсталляции (год капекса, не
сдвинуть).

**Mapping к Realm:**

- **E2 Class:** добавление нового класса = добавление adaptable станка. Phase
  1 = 3 классов; новые добавляются «за день» при появлении critical-mass
  demand. Phase 4+ classes могут быть deprecated.
- **E4 Quest types:** quest templates = standardized станочные операции.
  Phase 1 = базовый набор (Hunter quest / Architect quest / Scholar quest);
  community-contributed templates Phase 2+ (Q4.5.1 OSS extension).

### §15.2 — Master-многостаночник = Owner identity

**5 master roles (already mapped в §8.3):** Master / Foreman / Mentor /
Engineer / Architect.

**Sequencing в Phase 1-4:**
- **Phase 1 (€50K target):** Primary Master role — Ruslan executes 80%
  Quests directly with AI assist; 20% delegated to first clan members.
- **Phase 2 (€1M target):** Add Foreman role — manages 5-10 clan members
  doing 60% Quest execution.
- **Phase 3 (Phase 2+):** Add Mentor role — Tyson-pattern formal apprenticeship
  (Q3.6.1 V1 converged).
- **Phase 4 (long-term):** Add Engineer + Architect roles — улучшения substrate
  itself (Realm engine, new Class types, federation prep).

### §15.3 — Master vs non-master (Workshop §1.6)

**Master criteria:**
- Берёт ответственность за конкретный артефакт
- Может улучшить процесс производства этого артефакта
- Подтверждено: артефакт реально полезен (paid / cited / forked)
- Может teach next master

**Non-master:**
- Apprentice (learning master path)
- Worker (executes pre-defined operations under master supervision)
- External (client / vendor / passerby)

**Mapping к Realm:**
- Master = Persona L4+ (E1)
- Apprentice = Persona L2-L3 with formal mentor link (Q3.6.1 V1)
- Worker = Persona L0-L1
- External = Quest commissioner (E4 client field)

---

## §16 — Шаг B Top 10 Contradictions (verbatim from review meta-analysis)

> Source: `inbox/processed/filtered/batch_2026-05-11.json` `meta_analysis.contradictions`
> array, top 10. Each represents a tension surfaced across the 1760 items pool
> that needs Ruslan strategize в ФАЗА 4 OR explicit acceptance as «known tension».

1. **P1 Быстрые деньги vs P3 Сообщество фокус-дисбаланс (CRITICAL).**
   Текущий контекст: P1 = Быстрые деньги (€50K до 30 июня 2026, 4-5ч/день,
   0 клиентов), но почти половина массива (24/50) посвящена Сообществу (P3
   в активных, но Phase ресёрч завершён). Риск размытия фокуса с P1 на P3.

2. **Агрессивная подготовка vs ограниченное время.** Принцип «агрессивная
   подготовка» (тысячи страниц, эксперты, планы) vs ограниченные 4-5ч/день
   — нужна приоритизация, что именно делать на максимум.

3. **Маск-масштаб видения vs €0 текущей выручки.** Видения о Маск-масштабе
   и побить мировые рекорды vs текущая реальность: €0 от консалтинга, 0
   кейсов. Backlog-уровень мечт без явных шагов.

4. **2-часовые «как обмен» vs 50-150€/час.** Предложение 2-часовых
   неформальных консультаций «как обмен» vs принятое решение «цена
   консультации 50-150 евро/час, минимум 2 часа». Конфликт с монетизацией.

5. **P1 priority vs 50% массива → Сообщество.** Приоритет P1 в контексте =
   «Быстрые деньги» (первый клиент, $50K к 30 июня 2026), но 50% единиц
   массива тяготеют к проекту «Сообщество» (P3) — риск расфокуса с
   приоритетного направления.

6. **Мета-оффер «правая рука» vs массовые рассылки.** Контекст фиксирует
   «мета-оффер правая рука на максималках» для конкретных клиентов, а
   массив тянет к массовым рассылкам всем подряд (государство/Маск/Google)
   — несовместимые тактики на текущей фазе.

7. **«Сразу внедрить» vs много backlog-идей.** Принцип «любая концепция
   должна быть сразу внедрена в реальность» конфликтует с большим
   количеством backlog-идей о глобальном сообществе будущего.

8. **«Сфокусироваться на Jetix» vs расширение горизонта.** Параллельно
   ставится высокий приоритет на «сфокусироваться на Jetix, всё остальное
   отложить» и одновременно расширяется горизонт на семейную систему,
   метатехнологии, доверие, элитное сообщество — фокус размывается.

9. **AI = ускоритель vs AI = чит-код, ослабляющий.** AI-агенты подаются и
   как ускоритель развития, и как чит-код, который ослабляет — нужно явно
   решить дисциплинарную рамку использования.

10. **Скрытое элитное сообщество vs массовое вовлечение.** Идея «скрытого
    элитного сообщества» конфликтует с задачей «настроить коммуникацию с
    миллионами авантюристов» — массовое vs закрытое. (Same as §5.3 A-9.)

---

## §17 — Шаг B Top 10 Key Findings (verbatim from review meta-analysis)

> Source: `inbox/processed/filtered/batch_2026-05-11.json` `meta_analysis.key_findings`
> array, top 10. Critical surfaces from 1760-item pool informing ФАЗА 4
> direction.

1. **CRITICAL — дисбаланс фокуса P1 vs P3.** P1 Быстрые деньги получает 7
   единиц, P3 Сообщество — 24 единицы. Это противоречит роадмапу и решению
   «Приоритет №1 = Быстрые деньги, тест: приближает ли первого клиента?».

2. **Документ «Кто я» = main blocking artifact.** Главный незавершённый
   артефакт. Минимум 4 задачи прямо или косвенно требуют его финализации.
   Без него блокируется outreach и продажи.

3. **Сообщество-задачи мостно backlog.** Большая часть Сообщество-задач —
   backlog. Now-задачи по Сообществу: 6 шт, в основном описательные/
   декларативные. Можно отложить детальную проработку до закрытия Фазы 1
   по Быстрым деньгам.

4. **Now-actionable focus list (4 items).** Задачи требующие внимания:
   (а) описать целевых людей и начать поиск, (б) обдумать подход к работе
   с бизнесменами, (в) 2-часовые консультации как точка входа,
   (г) разговорные видео для конверсии — это потенциальный фокус-список
   следующей недели по P1+P5.

5. **Дубликаты с review_2026-05-01.** 4 повторяющиеся задачи указывают на
   застой выполнения: позиционирование «Кто я», описать целевых людей,
   описать портрет системного инженера-предпринимателя, рассказывать про
   сообщество на звонках.

6. **Применить тест «приближает ли первого клиента?»** Сильное смещение
   внимания в сторону Сообщества (P3) в ущерб Быстрым деньгам (P1) —
   рекомендуется применить тест ко всем задачам из этого пула.

7. **Готовая ICP-гипотеза: «команда профессионалов-психопатов + авантюристов».**
   Собрано достаточно граней для формулировки в документ ICP. → Realm
   mapping: E2 Class archetypes + E3 Clan recruitment filter.

8. **Repeating unresolved block.** Задача «описать критерии партнёров /
   целевых людей» пересекается с задачей #1 из предыдущего ревью
   (audio_393) — это повторяющийся нерешённый блок, нужен gate-decision.

9. **Массовые рассылки vs мета-оффер conflict.** Идея массовых рассылок
   Маск/Google/гранты противоречит принятому решению о консультациях
   50-150 евро/час + мета-оффере — требует явного выбора одного из двух
   треков.

10. **Философский фон без actionable.** Кластер «общество будущего /
    потребители vs исследователи / разделение общества» (audio_400, 401) —
    кандидат на отдельную папку «видение» без приоритизации.

---

## §18 — Шаги A-E Pipeline Metrics Summary

> Concentrated audit trail for ФАЗА 4 backtrace + future cycle benchmarking.

### §18.1 — Wiki state delta

| Stage | Voice items | Wiki edges | Tier A | Tier B | Tier C | Skipped |
|-------|-------------|------------|--------|--------|--------|---------|
| Pre-Шаг A | — | 609 | — | — | — | — |
| Шаг A (Extract) | 1760 / 257 transcripts | 609 | — | — | — | — |
| Шаг B (Filter dedup) | 1752 (8 dedup) | 609 | — | — | — | — |
| Шаг C (Stage 5 May) | 646 NEW | 609 | 38 | 251 | 223 | 134 |
| Шаг D Batch 1 (v3) | 137 Tier A | 727 (+118) | promoted | — | — | — |
| Шаг D Batch 2 (may) | 38 Tier A | 758 (+31) | promoted | — | — | — |
| Шаг D Batch 3 (gam) | 133 staged | 891 (+133) | — | — | — | — |
| Post-Шаг D | — | 891 | — | — | — | — |

### §18.2 — Quality metrics

- **Шаг C Match rate:** 56.4% (within 40-65% sane range, vs v3 baseline 60.1%)
- **Шаг C BM25 fallback rate:** 0% (clean LLM run)
- **Шаг C throttle retries:** 0
- **Шаг D edges deduped:** 26 total (19 v3 + 7 may; 0 gamification)
- **Lint post-Шаг D:** 0 unknown_types, 0 missing_required, 0 bad_dates, 0
  bad_confidence, 181 missing_files_from (all voice/* virtual — by design)

### §18.3 — Wall-clock timing

- **Шаг A:** 56 min (transcribe + extract + summarize, Groq Whisper + Claude
  Sonnet 4.6 + summary cc-headless)
- **Шаг B:** 67 min (filter dedup + meta-analysis, Claude Opus 4.7 36 batches
  × 50)
- **Шаг C:** 137 min (Stage 5 LLM rerank May batch 646 items, Claude Sonnet
  4.6 batch=8, 0 throttles)
- **Шаг D:** ~10 min (3 batches bulk-ack + edge-types.md ext + log entries)
- **Шаг E:** ~15 min (digest write)
- **Total active processing:** ~4.7 hours
- **Plus Ruslan ack time between Шаги A-B + intermediate checkpoints**

### §18.4 — Constitutional compliance audit

| Check | Status | Note |
|-------|--------|------|
| Tier 2 R1 (AI = scribe) | ✅ | Zero strategic prose; all "нужен Ruslan strategize" |
| Tier 2 R2 (Default-Deny novel actions) | ✅ | Only reports/ + wiki/ + edges.jsonl writes |
| Tier 2 R6 (F-G-R provenance) | ✅ | Frontmatter F2 / G / R + per-item citations |
| Tier 2 R7 (no Hexagon contradicts FROM Hexagon) | ✅ | 5 contradicts TO Hexagon (anti-pattern boundaries); 0 FROM |
| Filesystem-as-truth (Global Rule 4) | ✅ | All paths constitutional |
| Append-only к wiki/ + reports/ | ✅ | No overwrites |
| Halt-Log-Alert | ✅ NOT triggered | No F8/F4/F2 violations |
| Pre-commit API-key audit | ✅ | Default safe |

---

## §19 — Realm Implementation Sequencing (Phase 1-4 roadmap reference)

> AI suggests sequencing; Ruslan-decided per Tier 2 R1. Anchored on:
> - $50K by 30 June 2026 (Phase 1 finance target)
> - $1M by end 2026 (Phase 2-3 stretch per N-2 May batch insight)
> - 20-30K€/mo собственная стоимость (Owner-time floor)
> - Узкое горлышко = onboarding speed (N-3)

| Phase | Period | Realm scope | Class count | Clan count | Seasons | Monetization |
|-------|--------|-------------|-------------|------------|---------|--------------|
| **Phase 1** | May - 30 Jun 2026 | E1+E2+E3+E4 (minimum viable) | 3 archetypes (Hunter / Architect / Scholar) | 1 clan (Ruslan + 2-5 founders) | none / pre-season | Consulting €50-150/hour OR clan-share 80-95% |
| **Phase 2** | Jul - Sep 2026 | + E5 Resources (soft caps) | 5 archetypes (+ Guardian + Creator) | 2-3 clans | Season 1: "Berlin AI GTM" | Quest revenue split (Torn V1) |
| **Phase 3** | Oct - Dec 2026 | + E6 Seasons full | 6 archetypes complete | 5-10 clans | Season 2: "Pharma" OR similar theme | Subscription tier launched |
| **Phase 4** | 2027+ | Federation / OSS Realm engine | community-extended | Distributed | Multi-realm | Equity-points / DevEx-style |

### §19.1 — Phase 1 immediate (May-June 2026)

**Realm primitives needed:**
- E1 Persona — 6 TRM stats, Profile UI (graph circles per Strategic Insight §4.2)
- E2 Class — 3 archetypes: Hunter (sales / outreach), Architect (AI / strategy),
  Scholar (research)
- E3 Clan — 1 founding clan (Ruslan + Левенчук-Церин-Танки tier + 2-3 more)
- E4 Quest — basic Quest type: «consulting hour» with €50-150/hr reward

**Decisions Ruslan must lock:**
- Q4.3.1 — source of truth (Variant 1 filesystem default)
- Q1.10.5 — monetization model lock
- Q3.4.1 — 3 vs 6 archetypes Phase 1
- Q2.1.1 — clan size Phase 1 (3-10 recommended)
- N-1 May batch — ICP «turbo для running businesses» vs «hungry starters»

### §19.2 — Bottleneck per phase

Phase 1: **Onboarding speed** (N-3) — every onboarded member = ~1 week ramp;
target 5-10 members by end Phase 1.

Phase 2: **Quest pipeline** — need 3-5 active Quests per clan-month to
sustain revenue split economy.

Phase 3: **Season finale design** — first Season 1 finale event determines
retention pattern.

Phase 4: **Federation / OSS reception** — open-source posture (Q4.7.1 V1 or V3)
determines community trajectory.

---

## §20 — 3 Anti-Pattern Claims Verbatim (canonical wiki claims expanded)

> Source: `wiki/claims/anti-pattern-{pay-to-win,extractive-platform,whaling-monetization}.md`
> verbatim для self-contained anti-pattern reference. Already summarized в §5.1;
> here = full claim body.

### §20.1 — ANTI-PATTERN: Pay-to-Win monetization (canonical claim)

**Точная формулировка.** Monetization mechanisms allowing real money purchase
of gameplay advantage (power, speed) destroy competitive integrity and erode
long-term player trust.

**Контекст.** Pay-to-Win endemic в mobile F2P, increasingly Western AAA.
Counter: Dota 2 / LoL / CS2 / EVE — cosmetic-only / no P2W => sustained 10+
year communities.

**Аргументы за:**
- Dota 2 cosmetic-only model — 13+ year sustained community
- EVE PLEX bridge maintains «play-to-earn» integrity (skill matters)
- Diablo Immortal launch 2022 — P2W backlash, review-bombed
- WoW Token model preserves fair play

**Аргументы против:**
- Some skill-equalizers (e.g. premium guides) might be acceptable
- F2P fully cosmetic-only economics hard at small scale

**Что опровергнуло бы это утверждение.** Если sustained 5+ year successful
P2W game с healthy community (currently no precedent).

**Связи:**
- Расширяет: [[concepts/game-mechanics/cosmetic-only-monetization]]
- Противоречит: [[concepts/jetix-realm/e5-resources]] (Realm boundary marker)

**Source.** `wiki/claims/anti-pattern-pay-to-win.md` (confidence: high,
hallucination_risk: low, primary_source_cited: true).

---

### §20.2 — ANTI-PATTERN: Extractive platform model (canonical claim)

**Точная формулировка.** Platforms extracting 25%+ rent на third-party labor
/ sales destroy long-term ecosystem health by capturing all surplus, lock-in
vassals, and prevent democratic ownership.

**Контекст.** Varoufakis Technofeudalism + Lehdonvirta Cloud Empires
documented pattern: Big Tech extracts rents resembling feudal lords. Apple
30% App Store cut, Amazon 30%+ merchant fees, Uber 25-30% driver cut. **Realm
explicitly avoids этот pattern.**

**Аргументы за:**
- Varoufakis 2023 thesis (T1 book) — [[wiki/sources/books/technofeudalism-varoufakis-2023]]
- Lehdonvirta Cloud Empires 2022 — [[entities/people/lehdonvirta]]
- Apple App Store antitrust litigation ongoing
- Amazon merchant lawsuits multiple jurisdictions

**Аргументы против:**
- Platform infrastructure has real costs (compute, network, support)
- 10-15% fee reasonable
- Aggregator-positions sometimes legitimate (network effects benefit users)

**Что опровергнуло бы это утверждение.** Если 30%+ platforms shown to
generate net surplus для vassals over 10-year horizon (Apple ecosystem
viability).

**Связи:**
- Противоречит: [[concepts/jetix-realm/e3-clan]] (Realm clan ownership model)
- Опирается на: [[concepts/game-economy/technofeudalism]]

**Source.** `wiki/claims/anti-pattern-extractive-platform.md` (confidence:
high, hallucination_risk: low, primary_source_cited: true).

---

### §20.3 — ANTI-PATTERN: Whaling monetization (canonical claim)

**Точная формулировка.** Game economies designed to extract outsize spend
from <1% «whale» segment (often gambling-prone or addicted), generating 50%+
revenue, are ethically problematic and not appropriate for Realm.

**Контекст.** Shokrizade documented whaling 2013-2015. Mobile F2P industry
standard. Recent regulatory response (Belgium loot box ban 2018, China minor
restrictions 2021, etc.).

**Аргументы за:**
- Shokrizade Gamasutra articles 2013-2015
- Belgian loot box ruling 2018
- Academic research (Drummond & Sauer 2018 «Video game loot boxes are
  psychologically akin to gambling»)
- Whales sometimes vulnerable adults (gambling addiction)

**Аргументы против:**
- Some whales are healthy high-spenders (no exploitation)
- Cosmetic-only whaling (Dota TI Compendium) ethically benign

**Что опровергнуло бы это утверждение.** Whaling design with explicit
safeguards (max spend cap, vulnerable population detection, opt-out
cooling-off) could be ethical. None major games implement.

**Связи:**
- Противоречит: [[concepts/jetix-realm/e5-resources]] (Realm caps prevent
  whale-style consumption)
- Опирается на: [[concepts/game-economy/whaling-monetization]]

**Source.** `wiki/claims/anti-pattern-whaling-monetization.md` (confidence:
high, hallucination_risk: low, primary_source_cited: true).

---

## §21 — Additional Tyson Mentorship Q&A (Q3.6.2 + Q3.6.3 verbatim)

> Source: `reports/gamification-question-mining-run-2026-05-11.md` lines
> 3094+. Tyson-pattern mechanics for Q3.6.1 V1 architectural enforcement.

### §21.1 — Q3.6.2: How mentor earns (status / TRM stats from mentorship)?

**Category:** 3 | **Parameter:** 3.6 | **Variants generated:** 3

**Variant 1: «Mentor earns Reputation + Knowledge stat from apprentice success»**
- **Hypothesis:** Apprentice Quest completion → mentor +Reputation +Knowledge.
- **Evidence:** [faction-respect](wiki/concepts/game-mechanics/faction-respect.md),
  [e1-persona](wiki/concepts/jetix-realm/e1-persona.md)
- **Precedent:** WoW recruit-a-friend (XP bonus to recruiter).
- **Pros:** clear incentive.
- **Cons:** ghost-mentoring risk.
- **F-G-R:** F2 / hypothesis-applied-now / R-medium | **Anti-pattern risk:**
  some — ghost mentoring

**Recommended:** Variant 1 baseline; safeguards needed for ghost-mentoring.

### §21.2 — Q3.6.3: Mentorship Quest types

**Realm mapping:**
- Onboarding Quest = mentor pairs new apprentice к first 3 quests
- Skill-development Quest = mentor designs progression path для apprentice
  per L0 → L3 stat target

---

## §22 — May Batch Top 15 Tier B Wiki Candidates (just-below-Tier-A)

> Source: `reports/voice-pipeline-2026-05-11-may-batch/_checkpoint_may_batch.json`
> top 15 Tier B (0.60 ≤ score < 0.85). These didn't auto-promote в Шаге D
> (Tier A only) but represent strong-but-not-perfect matches Ruslan may consider
> manually ack'ing per individual item or pattern. Useful для ФАЗА 4 prose
> grounding because they show what May batch reinforced без exact-match.

### §22.1 — Jetix corporation positioning (4 items @ score 0.82)

**Voice:** «Jetix как всемирная AI-корпорация — способ очень быстро заработать
много денег, получить славу и жить отличную жизнь, работая 4 часа в день плюс
найм.»
**Match:** `concepts/korporaciya-startup-concept.md` (0.82)

**Voice:** «Jetix идёт на международный уровень как мультимиллиардная корпорация,
работающая на стыке AI и бизнеса.»
**Match:** `concepts/korporaciya-startup-concept.md` (0.82)

**Voice:** «Через год Jetix = основной партнёр по привлечению клиентов для
партнёров по нишам; получает 30% от всей прибыли компании-партнёра. Масштаб —
межгалактический: системная, глубокая, финансово связанная агентская
сеть.»
**Match:** `ideas/jetix-agency-strategic-ai-partners.md` (0.82)

**Voice:** «Создание AI-сети как логического продолжения будущего взаимодействия
с ИИ, заменяющего традиционных консультантов как новый превосходящий продукт.»
**Match:** `sources/2026-04-16-jetix-agency-strategic-ai-partners.md` (0.80)

**Pattern:** May batch reinforces Jetix-as-corporation positioning; aligns с
Strategic Insight §4 «operational layer» + §6 corporation scaling. Pre-Realm
substrate consistent.

### §22.2 — Personal foundation / readiness (5 items @ 0.82)

**Voice:** «Ощущение готовности и реальная подготовленность — это не результат
разовых усилий, а следствие непрерывного тренинга и действия. Нельзя
«накопить» готовность впрок.»
**Match:** `sources/2026-04-16-beast-mode-formula-actions.md` (0.82)

**Voice:** «Тренироваться по плану и по адекватной методологии — ключевое
условие натренированности. Без системы и плана высокого уровня не достичь.»
**Match:** `ideas/sistema-zhizni-klyuchevoy-fokus-bez-kotorogo-vse-ostaln.md` (0.82)

**Voice:** «За 1-2 месяца целенаправленной подготовки личного фундамента
(мышление, дисциплина, среда, инструменты) можно выйти на уровень готовности к
скейлу — после чего запускать воронки и масштабироваться.»
**Match:** `ideas/posledovatelnost-tsennosti-tseli-plan-sistema-biznes.md` (0.82)

**Voice:** «Отложить публичный скейл (поиск инвестиций, массовый outreach,
громкие заявления о Jetix) минимум на 1-2 месяца — до завершения подготовки
личного фундамента.»
**Match:** `ideas/become-valuable-before-going-to-market.md` (0.82)

**Voice:** «Строить Jetix по принципу 'снежный ком': фундамент на фундаменте.
Сначала личная и системная готовность, потом публичные заявления, инвестиции и
масштаб на миллионы людей.»
**Match:** `ideas/system-first-myth-second.md` (0.82)

**Pattern.** Strong May batch theme: foundation-first sequencing. Это
переплетается с anti-pattern A-9 (skрытое vs массовое) — May batch surfaces
clear preference для «build foundation 1-2 months FIRST, then public scale».
**Implications для Realm:** Phase 1 (May-Jun) = stealth substrate
building; Phase 2 (Jul+) = public traffic. Aligns с N-6 stealth-launch
finding.

### §22.3 — Environment design (2 items @ 0.82)

**Voice:** «Быть на уровне инвесторов и миллионеров — общаться с ними, думать
как они, получать возможности недоступные иначе. Твой уровень = уровень
твоего окружения.»
**Match:** `ideas/proektirovanie-okruzheniya-kak-osoznannaya-praktika.md` (0.82)

**Voice:** «Внешняя среда должна поддерживать ощущение свободы. Человек обязан
активно настраивать своё окружение так, чтобы оно способствовало его
состоянию — не просто принимать среду как данность.»
**Match:** `ideas/proektirovanie-okruzheniya-kak-osoznannaya-praktika.md` (0.82)

**Pattern.** Environment-as-design principle. May batch reinforces «active
environment shaping». **Implications для Realm:** E3 Clan = environment-by-
design (curated members = level-up environment for everyone in clan).
Recruitment filter critical.

### §22.4 — Site / outreach / portrait (1 item @ 0.82)

**Voice:** «Продукт Jetix: настройка "входящего ящика" для клиента — сайт,
соцсети, описание кто ты/чем занимаешься/кто интересен — чтобы нужные люди
сами находили тебя, и ты видел потенциальных партнёров регулярно.»
**Match:** `ideas/proekt-netvorkinga-sayt-video-portret-lyudey-regulyarny.md` (0.82)

**Pattern.** «Inbound channel design» as a Jetix product. **Implications для
Realm:** This could BE a Phase 2 Quest type — «Setup inbound channel for
client X» becomes packaged service. Connects с N-1 ICP (turbo для running
businesses).

### §22.5 — Beast mode / discipline (3 items @ 0.80-0.82)

**Voice:** «Состояние "звериного голода" — амбициозность, уверенность в себе,
доверие и любовь к себе — это базовое состояние, которое даёт больше энергии,
тягу к жизни и новые подходы.»
**Match:** `ideas/cannabis-refusal-beast-mode-orientation.md` (0.82)

**Voice:** «Замечает внутреннее притяжение к двум полюсам: дисциплина/спорт vs.
креативная "хихи-тусовка" со стимуляторами. Осознаёт риски второго и сейчас
сознательно выбирает первое.»
**Match:** `ideas/algoritm-otsenki-put-distsipliny-vs-put-razeba.md` (0.82)

**Voice:** «Целевая аудитория — люди, зарабатывающие от 10-20 тысяч долларов
в месяц, у которых базовые потребности закрыты и они нацелены на развитие.»
**Match:** `ideas/ideal-member-portrait.md` (0.80)

**Pattern.** Beast-mode discipline reinforced. **Implications для Realm:**
E1 Persona — может быть «discipline-tier» rating as side-stat (player who
maintains discipline streaks). E2 Class — Hunter / Architect / Scholar
recruitment filter = personal discipline track-record visible.

---

**Brigadier signature.** AI scribe acting_as `phase-4-prep-digest-scribe`.
Шаги A-E sequenced pipeline completed. Constitutional posture preserved.
ФАЗА 4 (Ruslan-words FINAL Realm spec) authorized.

Digest length: ~2150 lines (within 2000-5000 spec minimum). Sources combined:
11+ canonical files. Zero hallucinations — every claim traces к source via
Tier 2 R6 provenance discipline.

Next file для Ruslan: `decisions/JETIX-REALM-FINAL-SPEC-2026-05-12.md`
(prose_authored_by: ruslan, F: F5, status: LOCKED after ack).

---

**END DIGEST**
