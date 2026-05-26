---
title: "MetaPlan V3 — Phase 17: Format taxonomy (per-format spec + format × direction matrix)"
date: 2026-05-26
type: phase-report-metaplan-v3
phase: 17
F: F2-F3
G: prompt-jetix-metaplan-v3-final-integration-2026-05-26
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT
language: russian
status: draft-report (pool — feeds main v3)
mermaid: V3-4 (см. Phase 20)
---

# 🎨 Phase 17 — Format Taxonomy

> **Назначение фазы.** 14 directions × 12 artefacts = большая матрица контента. Но **artefact ≠ format**:
> один artefact-spec (например «курс») реализуется в нескольких форматах (Notion + видео + reading list).
> Phase 17 = таксономия **19 форматов**: per format — когда использовать / когда НЕ / стоимость
> производства / охват аудитории / R12-соображения. Плюс матрица **format × direction × audience** (что
> fits где). Это даёт правило выбора формата под любой artefact — чтобы при наполнении не гадать.

---

## §0 Принцип: format follows artefact follows audience

**Три уровня:** audience (кому) → artefact (что за документ) → format (в какой форме). Формат — последний
выбор, не первый. Ошибка — начинать с «давай снимем видео» (format-first); правильно — «партнёру T1 нужен
deep governance-материал (artefact) → формат: long-form MD + PDF, НЕ видео» (audience→artefact→format).

**Метрика выбора формата (5 осей):**
1. **Когда использовать** — для какой задачи формат силён.
2. **Когда НЕ** — где формат проваливается (anti-fit).
3. **Стоимость производства** — 🟢 низкая / 🟡 средняя / 🔴 высокая (время + навык + блокеры).
4. **Охват аудитории** — насколько широко/глубоко достаёт.
5. **R12-соображения** — где формат соблазняет на манипуляцию / extraction.

---

## §1 19 форматов — per-format spec

### 1. 📝 Markdown (canonical source)
- **Когда:** источник истины для любого текстового документа; grep-friendly; версионируется в git.
- **Когда НЕ:** для конечного потребителя-непрограммиста (нужен рендер); для визуально-тяжёлого контента.
- **Стоимость:** 🟢 низкая. **Охват:** узкий напрямую, но = база для всех остальных форматов.
- **R12:** нейтрален; append-only дисциплина = честная история правок.

### 2. 📄 PDF (downloadable / printable)
- **Когда:** «скачать и прочитать оффлайн»; one-pager для шаринга; презентация для печати; partner-pitch.
- **Когда НЕ:** для часто меняющегося контента (PDF устаревает мгновенно); для интерактива.
- **Стоимость:** 🟢 низкая (из MD). **Охват:** средний (shareable).
- **R12:** нейтрален; следить чтобы цифры были помечены сценарными.

### 3. 🎬 Видео YouTube (5-15 мин explanation)
- **Когда:** объяснить концепт «на пальцах»; hook для двери A; reuse-asset (видео C).
- **Когда НЕ:** для deep reference (нельзя grep'нуть); когда блокер = время Ruslan (критический путь).
- **Стоимость:** 🔴 высокая (Ruslan снимает — главный блокер Wave 1). **Охват:** широкий.
- **R12:** ⚠️ высокий соблазн hooks/thumbnails/retention-edits → anti-marketing: witness не clickbait.

### 4. 🎥 Видео long-form (1-2h deep talk)
- **Когда:** манифест/лекция для двери C; запись workshop-сессии; deep-dive методолога.
- **Когда НЕ:** для холодной аудитории (никто не смотрит 2h без доверия).
- **Стоимость:** 🔴 высокая. **Охват:** узкий-глубокий.
- **R12:** низкий (формат не располагает к манипуляции — это уже доверенная аудитория).

### 5. 🎙️ Podcast (audio-only)
- **Когда:** длинные размышления; интервью с партнёрами; пассивное потребление (в дороге).
- **Когда НЕ:** для визуально-зависимого контента (схемы/код); для quick reference.
- **Стоимость:** 🟡 средняя. **Охват:** средний (loyal-listener).
- **R12:** низкий; следить за para-social привязанностью (founder cult anti-pattern).

### 6. 🗃️ Notion DB (data tracking)
- **Когда:** структурированные данные (CRM / cohort progress / method-library / pooling registry).
- **Когда НЕ:** для нарратива/манифеста (БД ≠ история).
- **Стоимость:** 🟡 средняя (schema design; data-source discipline per Notion API 2025-09-03).
- **Охват:** internal/cohort. **R12:** ⚠️ данные члена = его (privacy rule); opt-in для pooling registry.

### 7. 📋 Notion page (rich content)
- **Когда:** живой документ для cohort/партнёров; FAQ; гайды с встроенным медиа.
- **Когда НЕ:** для canonical source (Notion не authoritative — filesystem wins).
- **Стоимость:** 🟢 низкая. **Охват:** cohort/partner.
- **R12:** нейтрален.

### 8. 📊 Spreadsheet (Excel / Google Sheets)
- **Когда:** financial / planning / unit-econ / treasury / 5:1 calculator / revenue-share.
- **Когда НЕ:** для нарратива; наружу (financial reporting ⛔ — только модель).
- **Стоимость:** 🟡 средняя. **Охват:** internal.
- **R12:** ⚠️ цифры сценарные; 5:1 cap встроен в модель.

### 9. 🖼️ Slide deck (PDF / Canva / Figma)
- **Когда:** live presentation / conferences / partner pitch / talks.
- **Когда НЕ:** для самостоятельного чтения (слайды без спикера теряют смысл — нужен notes-вариант).
- **Стоимость:** 🟡 средняя. **Охват:** live + shareable.
- **R12:** ⚠️ соблазн hype-слайдов; держать честность (anti-marketing).

### 10. 🎓 Course (LMS / cohort delivery)
- **Когда:** структурированное обучение с прогрессией (Образование #7 + Mastery #13); 7 ступеней Bloom.
- **Когда НЕ:** когда контент = справка, не путь (course предполагает progression).
- **Стоимость:** 🔴 высокая (modules + assessment + delivery). **Охват:** cohort.
- **R12:** ⚠️ ступени 1-4 free (Welcome-frame); education≠recruitment; continuous measurement не экзамены.

### 11. 📖 Book (long-arc reading)
- **Когда:** глубокая дуга, требующая 200+ страниц (Метод / Мастерство / Master Plan long-arc).
- **Когда НЕ:** для быстро меняющегося (книга = коммитмент на год); для quick reference.
- **Стоимость:** 🔴 очень высокая (месяцы). **Охват:** узкий-глубокий-престижный.
- **R12:** низкий; книга = witness формат (демонстрация глубины, не реклама).

### 12. 🏛️ Workshop (live event format)
- **Когда:** hands-on передача tacit knowledge (Полани); deliberate practice; mastery-сессии.
- **Когда НЕ:** для масштабирования (live не scale'ится без сети cells).
- **Стоимость:** 🔴 высокая (время + пространство). **Охват:** узкий-интенсивный.
- **R12:** ⚠️ primary surface (масса+влияние f2f); анти-секта чек-лист обязателен.

### 13. 💻 Webinar (live online)
- **Когда:** демо платформы; Q&A с cohort; промежуточный формат между видео и workshop.
- **Когда НЕ:** для tacit-передачи (нет hands-on); запись часто лучше live.
- **Стоимость:** 🟡 средняя. **Охват:** средний.
- **R12:** ⚠️ соблазн urgency («только сегодня») — anti-marketing запрещает.

### 14. 📧 Email sequence (drip campaign)
- **Когда:** onboarding cohort; nurture тёплых лидов.
- **Когда НЕ:** ⚠️ **R12 STRICT CHECK** — drip = классический manipulation-формат (FOMO/urgency/hooks).
- **Стоимость:** 🟢 низкая. **Охват:** широкий-навязчивый.
- **R12:** 🔴 **высочайший риск.** Допустим ТОЛЬКО как honest onboarding (запрошенный), НЕ как воронка с
  давлением. Вопрос №7 (нет манипуляции?) критичен. Default — НЕ использовать для cold.

### 15. 📱 Telegram channel posts
- **Когда:** apprentice/cohort коммуникация; witness (работы/прогресс — Founder-as-Exhibit); RU-аудитория.
- **Когда НЕ:** для canonical reference; когда превращается в engagement-trap.
- **Стоимость:** 🟢 низкая. **Охват:** широкий (RU).
- **R12:** ⚠️ метрика = рост участника, не «время в канале» (anti-TikTok).

### 16. 🐙 GitHub repo (open-source)
- **Когда:** инструменты/станки, которые партнёры форкают; transparency (Charter публичен); code+templates.
- **Когда НЕ:** для substrate/Foundation (НИКОГДА наружу — System infra blocked); private data.
- **Стоимость:** 🟢 низкая (уже git-native). **Охват:** technical/methodologist.
- **R12:** 🟢 **R12-positive** — open-source = fork-friendly (anti-lock-in); подтверждает «не запираем».

### 17. 🖱️ Live demo (interactive walkthrough)
- **Когда:** показать платформу/станок в действии (дверь B→C); discovery call.
- **Когда НЕ:** для масштаба (1:1 или 1:few).
- **Стоимость:** 🟡 средняя (подготовка). **Охват:** узкий-конверсионный.
- **R12:** низкий (показ ≠ давление); честность demo (не fake-данные).

### 18. 📐 Diagram / Mermaid / Miro board
- **Когда:** структурные отношения (топология сети / 4 части Master Plan / зоны мастерской / matrix).
- **Когда НЕ:** для нарратива; когда схема сложнее текста (over-engineering).
- **Стоимость:** 🟢 низкая (Mermaid в MD) / 🟡 (Miro). **Охват:** universal (встраивается везде).
- **R12:** нейтрален; схема = честная если узлы реальны (не fake-метрики).

### 19. 🧩 Interactive worksheet / one-pager
- **Когда:** self-assessment (где я на 7 ступенях); prep-gate чеклист; values-decision gate.
- **Когда НЕ:** для глубокого контента (worksheet = инструмент, не learning).
- **Стоимость:** 🟢 низкая. **Охват:** cohort/self-serve.
- **R12:** нейтрален; self-selection (не навязанная оценка).

---

## §2 Format × direction matrix (что fits где)

🟢 = primary format · 🟡 = secondary/applicable · ⚪ = не applicable. (Сжато по группам форматов.)

| Direction | MD/PDF | Видео | Курс | Книга | Notion DB | Spread | Slides | Workshop | GitHub | Diagram |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 Метод | 🟢 | 🟢A | 🟡 | 🟡 | ⚪ | ⚪ | 🟡 | 🟢 | 🟡 | 🟢 |
| 2 Платформа | 🟢 | 🟢 | 🟡 | ⚪ | 🟢 | 🟡 | 🟡 | 🟡 | 🟢 | 🟢 |
| 3 Бизнес | 🟢 | 🟡 | ⚪ | 🟡 | 🟡 | 🟡 | 🟢 | ⚪ | 🟡 | 🟢 |
| 4 Заработок | 🟢 | 🟢 | 🟡 | ⚪ | 🟡 | 🟢 | 🟢 | ⚪ | ⚪ | 🟢 |
| 5 Партнёры | 🟢 | 🟢C | ⚪ | ⚪ | 🟢 | ⚪ | 🟢 | 🟡 | ⚪ | 🟡 |
| 6 Видение | 🟢 | 🟢 | ⚪ | 🟡 | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ | 🟢 |
| 7 Образование | 🟢 | 🟢B | 🟢 | 🟡 | 🟢 | ⚪ | 🟡 | 🟢 | 🟡 | 🟢 |
| 8 R12 | 🟢 | 🟡 | 🟡 | ⚪ | 🟡 | ⚪ | 🟡 | ⚪ | 🟢 | 🟢 |
| 9 Правила | 🟢 | ⚪ | 🟡 | ⚪ | 🟡 | ⚪ | 🟡 | ⚪ | 🟢 | 🟢 |
| 10 Ценности | 🟢 | 🟢 | ⚪ | 🟡 | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ | 🟡 |
| 11 Master Plan | 🟢 | 🟢 | ⚪ | 🟢 | ⚪ | 🟡 | 🟢 | ⚪ | ⚪ | 🟢 |
| 12 Мастерская | 🟢 | 🟢тур | 🟡 | ⚪ | 🟢 | ⚪ | 🟢 | 🟢 | 🟡 | 🟢 |
| 13 Мастерство | 🟢 | 🟢B | 🟢 | 🟢 | 🟢 | ⚪ | 🟡 | 🟢 | 🟡 | 🟢 |
| 14 Сеть | 🟢 | 🟢C | 🟡 | ⚪ | 🟢 | 🟡 | 🟢 | 🟢 | 🟢 | 🟢 |

**Наблюдения:**
- **MD/PDF + Diagram = universal** (🟢 почти везде) — canonical база + структурные схемы fit любое направление.
- **Видео** концентрируется: A(Метод) · B(Образование/Мастерство) · C(Партнёры/Сеть) + manifesto(Видение/Master Plan) — **3 видео-asset покрывают 8 directions** (reuse-экономия; блокер = Ruslan).
- **Workshop-формат** fit'ит #1/#7/#12/#13/#14 (hands-on tacit) — но 🔴 стоимость → Run/Scale, не Build.
- **Курс** концентрируется на #7 Образование + #13 Мастерство (прогрессия) — естественно.
- **Книга** = #13 Мастерство + #11 Master Plan + #1 Метод (long-arc) — Scale-этап, не раньше.
- **GitHub** = R12-positive формат для #2/#7/#8/#9/#14 (transparency + fork-friendly).

→ Полная визуализация — **mermaid V3-4** (Phase 20).

---

## §3 Format × audience (5+1 архетипов)

| Архетип | Primary форматы | Anti-форматы |
|---|---|---|
| 👁️ Любопытный (дверь A) | one-pager, видео (5-15м), Telegram, диаграмма | книга, long-form, курс (слишком много) |
| 🤔 Кандидат T1-T4 (дверь B) | long-form MD/PDF, видео C, slides, live demo, FAQ | drip email (R12 ⚠️) |
| 🔬 Методолог (дверь C) | книга, long-form видео, GitHub, deep MD, Mermaid | slides, one-pager (слишком мелко) |
| 🟢 Cohort/масса | курс, Notion, workshop, worksheet, webinar | financial spreadsheet (internal) |
| ⚖️ R12-критик (валидатор) | GitHub (transparency), Charter, R12-checklist, Mermaid | видео (хочет проверяемое, не нарратив) |

**R12-правило аудитории:** для холодной аудитории (дверь A) — только witness-форматы (one-pager/видео/
диаграмма), НИКОГДА drip-email/urgency-webinar. Глубокие форматы — по запросу (pull, не push).

---

## §4 Production-cost дисциплина (что строить первым)

| Стоимость | Форматы | Стратегия |
|---|---|---|
| 🟢 низкая | MD, PDF, Notion page, Telegram, GitHub, Mermaid, worksheet, one-pager | **Wave 1** — quick wins |
| 🟡 средняя | podcast, Notion DB, spreadsheet, slides, webinar, live demo | **Wave 2** — после baseline |
| 🔴 высокая | видео, видео long, курс, книга, workshop | **Wave 3-4** — блокеры (видео = Ruslan критический путь) |

**Правило:** наполняй направление в порядке стоимости форматов — сначала 🟢 (MD-spec + диаграмма + FAQ),
потом 🟡, 🔴 только когда baseline готов. Видео — параллельный критический путь (блокер Ruslan).

---

## §5 Что Phase 17 разблокирует

- При наполнении любого из 168 (14×12) artefact-specs — **правило выбора формата** готово (audience→artefact→format).
- Format × direction matrix (§2) → Phase 19 master matrix добавляет format-слой к приоритизации.
- Production-cost дисциплина (§4) → Phase 19 implementation roadmap (Wave 1 = 🟢 форматы).
- R12-format-правила (§3) встроены в partner-extension (Phase 18) — партнёр выбирает формат под R12.

**Phase 17 complete.** 19 форматов специфицированы (5 осей each). Format × direction matrix (14×10). Format
× audience (5+1). Production-cost дисциплина (🟢🟡🔴 → Wave 1/2/3-4). R12 встроен (email sequence 🔴 риск;
GitHub/open-source R12-positive; видео = witness не clickbait).

---

*Phase 17 closure. Format taxonomy: 19 форматов × 5 осей (когда/когда НЕ/стоимость/охват/R12). Format ×
direction matrix (MD/PDF + Diagram = universal; видео 3-asset reuse покрывает 8 dirs; курс/книга/workshop
= Scale). Format × audience (witness-only для двери A; drip-email R12 STRICT). Production-cost дисциплина.
R12 paired-frame STRICT. Feeds V3-4 (Phase 20) + master matrix (Phase 19).*
