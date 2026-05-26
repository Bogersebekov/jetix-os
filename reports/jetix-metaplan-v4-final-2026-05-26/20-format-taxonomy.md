---
title: "MetaPlan V4 — Phase 19: Format taxonomy (26 formats: 19 base + 7 NEW for Геймификация/Хакатоны)"
date: 2026-05-26
type: phase-report-metaplan-v4
phase: 19
F: F2-F3
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT
language: russian
status: draft-report (pool — feeds main v4)
mermaid: V4-4 (см. Phase 22)
---

# 🎨 Phase 19 — Format Taxonomy (26 forms)

> **Назначение фазы.** V3 дал 19 форматов × 5 осей (когда / когда НЕ / стоимость / охват / R12). V4
> добавляет **7 NEW форматов**, продиктованных новыми directions — 3 для Геймификации (#15: dashboard /
> achievement system / skill-tree) + 4 для Хакатонов (#16: event playbook / expedition template /
> inter-clan rules / sponsorship deck). Итого **26 форматов**. Правило выбора неизменно:
> **audience → artefact → format**.

---

## §0 Принцип (preserved): audience → artefact → format

Формат — последний выбор. 5 осей: когда использовать / когда НЕ / стоимость (🟢🟡🔴) / охват / R12. V4
добавляет 7 форматов — и 4 из них **R12-чувствительны** (game-mechanic форматы = dark-pattern риск).

---

## §1 19 base форматов (из V3 — сжато)

1. 📝 **Markdown** (canonical, 🟢, universal) · 2. 📄 **PDF** (downloadable, 🟢) · 3. 🎬 **Видео YouTube**
(5-15м, 🔴 блокер Ruslan, R12: witness не clickbait) · 4. 🎥 **Видео long-form** (1-2h, 🔴) · 5. 🎙️
**Podcast** (🟡, R12: para-social риск) · 6. 🗃️ **Notion DB** (🟡, R12: данные члена=его) · 7. 📋 **Notion
page** (🟢) · 8. 📊 **Spreadsheet** (🟡, internal, цифры сценарные) · 9. 🖼️ **Slide deck** (🟡) · 10. 🎓
**Course** (🔴, R12: ступени 1-4 free) · 11. 📖 **Book** (🔴, witness) · 12. 🏛️ **Workshop** (🔴, R12
primary f2f) · 13. 💻 **Webinar** (🟡, R12: no urgency) · 14. 📧 **Email sequence** (🟢, 🔴 R12 риск —
drip=manipulation; только honest onboarding) · 15. 📱 **Telegram** (🟢, R12: рост не время) · 16. 🐙
**GitHub** (🟢, R12-positive fork-friendly) · 17. 🖱️ **Live demo** (🟡) · 18. 📐 **Diagram/Mermaid/Miro**
(🟢, universal) · 19. 🧩 **Interactive worksheet/one-pager** (🟢, self-selection).

Полная V3-таксономия (5 осей each): `reports/jetix-metaplan-v3-final-2026-05-26/18-format-taxonomy.md`.

---

## §2 7 NEW форматов (V4)

### Для Direction 15 🎮 Геймификация (3 формата — все R12-чувствительны)

#### 20. 📊 Interactive dashboard (real-time stats visualization)
- **Когда:** личная статистика прокачки (Life Pulse Layer 1 + Habits + deep work min); видеть прогресс
  «каждый день» (Ruslan voice). Cohort progress (R12: opt-in видимость).
- **Когда НЕ:** для нарратива; когда метрики становятся самоцелью (vanity).
- **Стоимость:** 🟡 средняя (Notion/Grafana-style; на базе Platform #2). **Охват:** cohort/self.
- **R12:** ⚠️⚠️ **HIGH** — dashboard = классический engagement-trap. Discipline: метрика = «насколько
  вырос» НЕ «время в приложении»; intrinsic motivation; opt-out; no streak-shaming; no infinite-scroll.
  Проходит Anti-Dark-Patterns audit (Phase 18 §8).

#### 21. 🏅 Achievement system spec (milestones / badges)
- **Когда:** meaningful progression markers (mastery достигнут — не просто «зашёл 30 дней»).
- **Когда НЕ:** ❌ vanity badges; ❌ completion-for-completion's-sake.
- **Стоимость:** 🟡. **Охват:** cohort.
- **R12:** ⚠️⚠️ **HIGH** — achievements = vanity-metric ловушка. Discipline: badge = реальный mastery
  marker (решил N уникальных задач тяжести X), portfolio>diploma; НЕ social-comparison-driven. Anti-Dark-Patterns gate.

#### 22. 🌳 Skill tree visualization tool
- **Когда:** визуализировать «темы vs уровни» (Mastery #13 — нелинейная развитость, дерево тем со своими
  вершинами, НЕ одна лестница). Помогает выбрать «куда расти».
- **Когда НЕ:** ❌ как ranking-инструмент (сравнивать мастеров разных тем глупо — anti-ranking).
- **Стоимость:** 🟡. **Охват:** self/cohort.
- **R12:** ⚠️ medium — skill tree = potential comparison-trap. Discipline: anti-ranking culture (multiple
  valid peaks); прогрессия для себя не для лидерборда; curiosity-driven не competition-driven (хотя
  inter-clan competition #16 = отдельный opt-in контекст).

### Для Direction 16 🏆 Хакатоны (4 формата)

#### 23. 📕 Event playbook (hackathon hosting guide)
- **Когда:** воспроизводимый гайд организации хакатона (Initiate→Match→Solve→Reward→Recurse cycle);
  T1 organizers / sponsors / clan founders.
- **Когда НЕ:** для участника (ему нужен другой формат — FAQ/quest).
- **Стоимость:** 🟡 (один раз → reuse для всех событий). **Охват:** organizers.
- **R12:** ⚠️ — playbook должен встроить R12: 5:1 payout cap, sponsorship transparency, fork-and-leave,
  no anti-competitive. Anti-pattern: playbook оптимизирует «retention любой ценой».

#### 24. 🧭 Expedition planning template
- **Когда:** small-group travel to learn deeply one niche (workshop-concept Phase 7 expedition example);
  cross-clan expeditions.
- **Когда НЕ:** для крупных событий (expedition = intimate).
- **Стоимость:** 🟢-🟡. **Охват:** small group.
- **R12:** добровольно (не отработка лояльности); гостеприимство = gift (per Network direction).

#### 25. ⚔️ Inter-clan competition rules document
- **Когда:** правила соревнования между кланами (хакатоны/mastery tournaments); «дух соревнования + уважение».
- **Когда НЕ:** для внутри-клана.
- **Стоимость:** 🟢 (MD rules). **Охват:** clans.
- **R12:** ⚠️⚠️ **STRICT** — это R12-критичный формат: explicit no member poaching / no resource sabotage
  / no anti-clan extraction; «уважение между соревнующимися». Cross-ref Klan Charter + R12 #8.

#### 26. 💼 Sponsorship deck
- **Когда:** привлечение sponsors для events (T2 ресурс-партнёры); revenue engine.
- **Когда НЕ:** для участников (это B2B-sponsor формат).
- **Стоимость:** 🟡 (slides). **Охват:** sponsors.
- **R12:** ⚠️ — sponsorship transparency (на что идут деньги); no sponsor capture (sponsor не диктует
  ценности/манипуляции); 5:1 + QF preserved.

---

## §3 Format × direction matrix (V4 — обновлённый, ключевые)

🟢 primary · 🟡 applicable · ⚪ нет. (Только directions, где NEW форматы релевантны + ключевые.)

| Direction | dashboard | achievement | skill-tree | playbook | expedition | inter-clan | sponsor-deck |
|---|---|---|---|---|---|---|---|
| 2 Платформа | 🟢 (хост) | 🟢 (хост) | 🟢 (хост) | ⚪ | ⚪ | ⚪ | ⚪ |
| 7 Образование | 🟡 | 🟡 | 🟡 | ⚪ | 🟡 | ⚪ | ⚪ |
| 13 Мастерство | 🟡 | 🟡 | 🟢 | ⚪ | 🟡 | ⚪ | ⚪ |
| 14 Сеть/Кланы | ⚪ | ⚪ | ⚪ | 🟡 | 🟢 | 🟢 | ⚪ |
| 15 Геймификация | 🟢 | 🟢 | 🟢 | ⚪ | ⚪ | ⚪ | ⚪ |
| 16 Хакатоны | ⚪ | 🟡 | ⚪ | 🟢 | 🟢 | 🟢 | 🟢 |

**Наблюдение:** 3 геймификация-формата хостятся на Платформе (#2) + питают #13/#7/#15. 4 события-формата
концентрируются на #16/#14. Universal (MD/PDF/diagram) + видео — как в V3.

→ Полная визуализация — **V4-4** (Phase 22).

---

## §4 Production-cost дисциплина (V4)

| Стоимость | NEW форматы | Wave |
|---|---|---|
| 🟢 низкая | inter-clan rules (MD), expedition template | Wave 1-2 |
| 🟡 средняя | dashboard, achievement, skill-tree, event playbook, sponsorship deck | Wave 2-3 |
| 🔴 высокая | (game-mechanic полная реализация = Run/Scale + R12 audit) | Wave 3-4 |

**Правило V4:** game-mechanic форматы (dashboard/achievement/skill-tree) — 🟡 на спеку, но **gated за
Anti-Dark-Patterns audit** перед публикацией (не Wave 1 — нужен R12-дизайн). Event-форматы — Wave 1-2
(хакатоны = Wave 1→2 revenue engine, per HP-T1 first event ≤90d).

---

## §5 R12-format-правила (V4 расширены)

- **Game-mechanic форматы (dashboard/achievement/skill-tree)** = проходят Anti-Dark-Patterns audit. Default
  discipline: meaningful progression / intrinsic motivation / opt-out / metric=рост.
- **Event-форматы (playbook/sponsorship)** = встраивают 5:1 + QF + transparency + fork-and-leave.
- **Inter-clan rules** = STRICT (no poaching/sabotage/extraction).
- **Email sequence (#14 base)** остаётся 🔴 риск — для events НЕ использовать FOMO-маркетинг.

---

## §6 Что Phase 19 разблокирует

- 26 форматов (19 + 7 new) → правило выбора формата для всех 192 (16×12) artefact-specs.
- Game-mechanic форматы gated за Anti-Dark-Patterns audit (R12 primary surface).
- Event-форматы → Phase 21 master matrix (Wave 1-2 revenue engine).
- Format × direction matrix → Phase 21 + V4-4.

**Phase 19 complete.** 26 форматов (19 base + 7 NEW: dashboard/achievement/skill-tree для #15;
playbook/expedition/inter-clan-rules/sponsorship-deck для #16). 4 из 7 new = R12-чувствительны (gated за
Anti-Dark-Patterns audit). Format × direction matrix обновлён. R12 paired-frame STRICT.

---

*Phase 19 closure (v4). Format taxonomy 26 forms. 7 NEW: Геймификация (dashboard ⚠️HIGH / achievement
⚠️HIGH / skill-tree ⚠️) + Хакатоны (event playbook / expedition template / inter-clan rules ⚠️STRICT /
sponsorship deck). Game-mechanic форматы gated за Anti-Dark-Patterns audit. Event-форматы Wave 1-2 (revenue
engine). R12 paired-frame STRICT. Feeds V4-4 (Phase 22) + master matrix (Phase 21).*
