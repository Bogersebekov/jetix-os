---
title: SIPO/ZIPO Schulung BVG Deep Analysis — 19 photos vision extract + DE→RU + formulas + mermaid + PDF source
date: 2026-05-20 morning
type: autonomous-execution-prompt
phase_count: 7
parent_explain: prompts/explanations/_EXPLAIN-zipo-sipo-bvg-schulung-deep-2026-05-20.md
input_corpus: raw/external/zipo-bvg-schulung-2026-05-20/
output_namespace: research/zipo-sipo-bvg-schulung-deep-2026-05-20/
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: zipo-sipo-bvg-schulung-deep
R: refuted_if_glossary_misattributed_OR_formulas_misextracted_OR_intranet_bypass_attempted
constitutional_posture: R1 scribe-mode + R6 per-claim + R11 Default-Deny + EP-5 F2 + Russian-primary + no-paid-content
estimated_runtime: 90-120 min autonomous
estimated_cost: <€5 (vision-heavy Phase 1)
language: russian primary + german terms preserved verbatim
---

# SIPO / ZIPO Schulung BVG Deep Analysis — Prompt

> **Trigger:** Ruslan voice 2026-05-20 morning — личный SIPO Schulung BVG (Berlin U-Bahn track warning post role). 19 photos материалов теста vendored. Server CC autonomous deep run: vision extract → DE→RU glossary + formulas + test walkthrough + BVG public search + mermaid + printable PDF source. **NOT plan mode** — execute immediately on launch.

---

## §0 Pre-flight Reading (mandatory)

ПЕРЕД Phase 0 прочитай:
1. **EXPLAIN file:** `prompts/explanations/_EXPLAIN-zipo-sipo-bvg-schulung-deep-2026-05-20.md`
2. **Input corpus:**
   - `raw/external/zipo-bvg-schulung-2026-05-20/00-INVENTORY.md` (per-image surface descriptions + context)
   - `raw/external/zipo-bvg-schulung-2026-05-20/images/IMG_76{66,68-85}.JPG` (19 photos)
3. **Memory rules (load context):**
   - Russian primary output (Ruslan preference)
   - No paid content / no auth bypass attempt
   - Per-claim provenance discipline

---

## §1 Context recap

**Тест:** SIPO Schulung — сертификация **Sicherungsposten** (warning post) для BVG U-Bahn track works.

**Роль SIPO:** warns track workers via acoustic signals (Ro 1 / Ro 2 / Ro 3) о приближающихся rail vehicles. Critical safety role.

**BVG U-Bahn:** Großprofil (большой профиль линий) vs Kleinprofil (малый). Different clearance rules.

**Ключевая регуляция:** DUV (Dienstanweisung Unfallverhütung) — внутренний документ BVG о предотвращении несчастных случаев.

---

## §2 Phase 0 — Pre-flight + Output Namespace (5 min)

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/MANIFEST.md` (initial setup)

### Steps
1. Read `raw/external/zipo-bvg-schulung-2026-05-20/00-INVENTORY.md`
2. Verify все 19 photos present in `raw/external/zipo-bvg-schulung-2026-05-20/images/`
3. `mkdir -p research/zipo-sipo-bvg-schulung-deep-2026-05-20/diagrams`
4. Write initial MANIFEST.md (will be updated в Phase 7 с final cost + file inventory)
5. Print pre-flight log

Commit: `[zipo-bvg] Phase 0 pre-flight + output namespace setup`

---

## §3 Phase 1 — Vision Extract per-Image (25-35 min) ⭐

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/01-image-by-image-extraction.md`

### Approach

Используй Claude **vision** capability — Read tool с .JPG path = native image analysis. Photos rotated 90° → vision rotation-invariant, no preprocessing needed.

### Per-image extraction format

Для каждого из 19 photos:

```markdown
### IMG_NNNN.JPG

**Source path:** `raw/external/zipo-bvg-schulung-2026-05-20/images/IMG_NNNN.JPG`
**Content type:** [paper text / paper diagram / paper table / laptop screen / form / answer sheet]
**Orientation:** [normal / rotated 90° CW / rotated 90° CCW / rotated 180°]

**German verbatim content (text + numbers + signal info + diagram labels):**

> [полный verbatim немецкий текст — preserve original spelling, punctuation, numbers exactly]

**Diagrams / visuals (если есть):**

- [описание диаграммы verbatim: «cross-section view of two tracks, distance markings 3.70m / 4.50m, hatched safety zone in middle, scale arrows»]
- [signal symbols / illustrations / photos within photo]

**Tables (если есть):**

| German column | German column 2 |
|---|---|
| [verbatim] | [verbatim] |

**Markings / highlights (если есть):**

- Red rectangles / circles / pencil marks → describe what they highlight

**Illegible passages (если есть):**

- [Page corner / shadow / blur details]

**Краткое RU описание (≤50 слов):**

[Quick summary что на странице на русском — НЕ полный перевод, just orientation]

---
```

### Processing order

Process photos в порядке IMG_7666 → 7668 → 7669 → ... → 7685. Можно batch 3-5 photos per Read call но keep extraction per-image structured.

### Critical extraction targets per photo (priority surface)

Особенное внимание к:
- **Numbers** (distances в meters; signal tone durations; time intervals; speed limits в km/h; group sizes; percent angles)
- **Signal definitions** (Ro 1 / Ro 2 / Ro 3 / любые другие Rotten signals)
- **Acronyms** (SIPO / Sakra / DUV / DA U / DA O / LTB / KGT / ESO / ZUB / Sondervorschriften — extract все встречающиеся)
- **Conditional rules** («wenn... dann...» / «sofern... » / «außer...»)
- **Test marks** в IMG_7666 / 7668 / 7669 — sequence numbers / correct vs incorrect / score breakdown

Commit: `[zipo-bvg] Phase 1 vision extract 19 photos DE verbatim`

---

## §4 Phase 2 — DE→RU Concepts Glossary (15-20 min) ⭐

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/02-concepts-glossary-de-ru.md`

### Structure

Glossary entries organized по category:

```markdown
## §A Роли (Rollen / Roles)

### SIPO — Sicherungsposten
- **DE:** Sicherungsposten
- **RU:** Пост безопасности / сигнальщик / сигналист
- **Definition (RU):** Сертифицированный работник BVG, который warns track workers об опасности при приближении rail vehicles через acoustic signals. Несёт ответственность за timely warning + visual observation track approaches.
- **Verbatim DE source:** «SIPO warnt Beschäftigte durch Signal» [src: IMG_7670]
- **Ключевые responsibilities (per материалов теста):**
  - Постоянное наблюдение за track approaches с обеих сторон
  - Acoustic warning via Ro signals при approach
  - Notfall (emergency) handling через Ro 3
- **Кто может быть SIPO:** [extract из materials или mark «not surfaced photos»]
- **Где встречается в материалах:** IMG_7670 (signals) / IMG_7676 (concepts) / [list other relevant]
- **Пример use case:** [построить пример: «при работе на путях 2 worker'ов + 1 SIPO (= Kleingruppe), SIPO стоит на elevated position с clear view, при approach дает Ro 1 (внимание) → если train не остановится / continues → Ro 2 (clear tracks) → workers убирают tools и идут в Sicherheitsraum в течение Räumzeit»]

### Sakra
- **DE:** Sakra (Sicherheitsaufsicht / Sicherheitsaufsichtskraft / Sachkundige Arbeitssicherheit)
- **RU:** Куратор / надзиратель безопасности / эксперт по безопасности работ
- ...

### Bauleiter
- ...

### Beschäftigte
- ...

## §B Пространство / расстояния (Räume / Distances)

### Sicherheitsraum
- **DE:** Sicherheitsraum
- **RU:** Безопасное пространство / зона безопасности
- ...

### Nachbargleis
- ...

### Fahrbereich
- ...

### Gefahrenanstrich (Kennzeichen 41)
- ...

## §C Сигналы (Signale)

### Ro 1
- **DE:** Ein langer Ton
- **RU:** Один длинный сигнал
- **Meaning:** [extract from material]
- **When used:** ...

### Ro 2
- ...

### Ro 3 (Notfall)
- ...

## §D Время / процедуры (Zeit / Prozeduren)

### Räumzeit
- **DE:** Räumzeit
- **RU:** Время эвакуации / clearance time
- **Definition (RU):** Время, отведённое работникам после signal Ro 2 для того чтобы убрать tools профильно (profilfrei) и зайти в Sicherheitsraum «без спешки» (ohne Hast).
- **Кто устанавливает:** Bauleiter или Sakra (verbatim DE: «legt Bauleiter bzw. Sakra fest» [src: IMG_7676])
- **Формула расчёта:** [см. 03-formulas-tabelle.md]
- ...

## §E Регуляции / документы

### DUV — Dienstanweisung Unfallverhütung
- ...

### DA U / DA O
- ...

### LTB
- ...

## §F Группы и режимы работы

### Kleingruppe
- **DE:** Kleingruppe
- **RU:** Малая группа
- **Definition:** max 2 Beschäftigte + 1 SIPO [src: IMG_7676]
- ...

### Einsatz mehrerer Dienststellen
- ...

### einfache Verhältnisse
- ...

## §G Меры безопасности

### Grundarten der Sicherungsmaßnahmen — Основные виды мер безопасности
- (1) Von der BVG zugelassene technische Einrichtungen — Утверждённые BVG технические устройства
- (2) SIPO — Sicherungsposten
- (3) Fahrdienstliche Maßnahmen (Gleissperrung / Langsamfahrstrecken) — Меры эксплуатационной службы (закрытие путей / участки тихого хода)
- ...

### Gleissperrung
- ...

### Langsamfahrstrecken
- ...
```

**Минимум 25 glossary entries** ожидается (covers все основные surfaced terms из Phase 1 extraction).

Per entry: DE term + RU translation + RU definition + verbatim DE source citation + примеры use cases + cross-link к IMG sources.

Commit: `[zipo-bvg] Phase 2 concepts glossary DE→RU (~25 entries)`

---

## §5 Phase 3 — Formulas Standalone Table (10-15 min) ⭐

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/03-formulas-tabelle.md`

### Structure

```markdown
# Основные формулы / расчёты — SIPO Schulung BVG

> Все numeric thresholds, signal counts, time intervals, distance limits в одной таблице. Каждая строка: название (DE+RU) / формула или правило / логика расчёта / worked пример.

---

## §A Расстояния (Distance thresholds)

| # | DE название | RU название | Правило / формула | Логика | Worked пример |
|---|---|---|---|---|---|
| F-1 | Sicherheitsraum zwischen zwei Gleisen — kein Sicherheitsraum | Безопасного пространства нет | Abstand < 3.70m → kein Sicherheitsraum | Если расстояние между путями <3.70m, работать на путях без дополнительных мер запрещено | На путях U-Bahn Großprofil distance = 3.50m → kein Sicherheitsraum → нужна Gleissperrung или другие меры |
| F-2 | Sicherheitsraum vorhanden, wenn (bedingt) | Безопасное пространство есть условно | Abstand ≥ 3.70m UND (Gefahrenfreiheit ODER zulässige Geschwindigkeit ≤ 30 km/h auf beiden Gleisen) | ≥3.70m достаточно если конструктивная безопасность ИЛИ ограничение скорости 30 км/ч на обоих путях | Distance = 3.80m + speed limit 30 km/h обоими путями → Sicherheitsraum bedingt |
| F-3 | Sicherheitsraum vorhanden (unbedingt) | Безопасное пространство есть безусловно | Abstand ≥ 4.50m | ≥4.50m → автоматически Sicherheitsraum без conditions | Distance = 4.60m → Sicherheitsraum vorhanden |
| F-4 | Nachbargleis definition | Соседний путь | Abstand zwischen Fahrbereichen < 1.5m | Если расстояние между Fahrbereichen <1.5m, считается Nachbargleis (повышенные требования безопасности) | ... |
| F-5 | Seitlich Sicherheitsraum bis 2.20m | Боковой безопасный зазор до 2.20m | bis 2.20m от Wand / festes Hindernis → требуется Gefahrenanstrich (weiß-rot-weiß) | ... | ... |
| F-6 | Seitlich Sicherheitsraum ab 2.20m | Боковой безопасный зазор от 2.20m + 0.70m | ab 2.20m + 0.70m | ... | ... |

## §B Сигналы (Signal counts / durations)

| # | DE название | RU название | Правило | Логика | Когда применяется |
|---|---|---|---|---|---|
| F-7 | Ro 1 | Сигнал «внимание» | 1× Ein langer Ton | Длинный сигнал привлекает внимание | Train approach detection (initial warning) |
| F-8 | Ro 2 | Сигнал «убрать tools» | 2× lange Töne (две длинных, hintereinander) | ... | Workers убирают tools и идут в Sicherheitsraum |
| F-9 | Ro 3 (Notfall) | Аварийный сигнал | Mindestens 5× zwei kurze Töne hintereinander (минимум 5 повторов двух коротких звуков подряд) | ... | Emergency — немедленный clearance |

## §C Время (Time intervals)

| # | DE название | RU название | Правило / формула | Логика | Worked пример |
|---|---|---|---|---|---|
| F-10 | Räumzeit | Время эвакуации | Räumzeit = устанавливается Bauleiter / Sakra; зависит от distance к Sicherheitsraum + scope of tools + tracks layout | Достаточно времени после Ro 2 чтобы убрать tools profilfrei + зайти в Sicherheitsraum ohne Hast | Если до Sicherheitsraum 10m walk + heavy tools layout → Räumzeit может быть 20-30 секунд (расчёт по conservative estimate) |
| F-11 | Vorwarnzeit (если surfaced в materials) | ... | ... | ... | ... |

## §D Группы (Group composition)

| # | DE название | RU название | Правило | Worked пример |
|---|---|---|---|---|
| F-12 | Kleingruppe | Малая группа | max 2 Beschäftigte + 1 SIPO | 3 workers + 1 SIPO = НЕ Kleingruppe; требуются дополнительные меры |
| F-13 | ... | ... | ... | ... |

## §E Скорости (Speed limits)

| # | DE название | RU название | Правило | Worked пример |
|---|---|---|---|---|
| F-14 | Reduzierte Geschwindigkeit bei Sicherheitsraum bedingt | Ограничение скорости при условном безопасном пространстве | ≤ 30 km/h auf beiden Gleisen (для активации F-2 Sicherheitsraum bedingt) | Track section с 3.80m distance → speed limit 30 km/h обоими путями → Sicherheitsraum bedingt qualified |

---

## §F Decision tree — выбор Sicherheitsmaßnahme

[mermaid flowchart embedded — также в diagrams/]

---

## §G Quick-lookup: «дано X — ответ Y»

| Situation (RU) | Sicherheitsraum status | Required actions |
|---|---|---|
| Расстояние между путями 3.50m | kein Sicherheitsraum | Gleissperrung obligatoria |
| Расстояние 3.85m + speed limit 30 km/h обоими путями | bedingt vorhanden | SIPO + reduced speed enforced |
| Расстояние 4.60m | unbedingt vorhanden | SIPO + standard procedures |
| Расстояние до feste Wand 1.80m | seitlich kein (zone до 2.20m) | Gefahrenanstrich weiß-rot-weiß требуется + Vorsicht |
| 2 worker'a + 1 SIPO | Kleingruppe | Standard SIPO procedures sufficient |
| 4 worker'a + 1 SIPO | NOT Kleingruppe | Additional measures + dedicated Bauleiter/Sakra |
```

**Минимум 15 formula/threshold entries** ожидается. Surface всё что extracted в Phase 1 + cross-link к photo IMG sources.

Commit: `[zipo-bvg] Phase 3 formulas standalone table (~15 entries)`

---

## §6 Phase 4 — Test Walkthrough (10-15 min)

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/04-test-walkthrough.md`

### Structure

```markdown
# Walkthrough пройденного теста — пример расчётов

> Сборка из IMG_7666 (intranet test result) + IMG_7668 + IMG_7669 (answer sheets с markings) — показывает «как что высчитывается» step-by-step.

## §1 Что мы видим в materials

**IMG_7666** — laptop screen, BVG intranet, результат теста / страница регламентов:
- [extracted content из Phase 1]
- Score / pass status / sections passed (если visible)

**IMG_7668 + IMG_7669** — answer sheets с red markings:
- Question numbers визуализированы
- Marked answers (correct / incorrect) — analyze patterns

## §2 Per-question walkthrough

### Question 1 (extracted из IMG_7668 / 7669)
**Question DE:** [verbatim if extractable]
**Question RU:** [translation]
**Answer choices:** [if extractable]
**Correct answer:** [from markings / from concept knowledge]
**Расчёт / логика:**
1. Шаг 1: identify which concept применим (e.g., F-3 Sicherheitsraum unbedingt)
2. Шаг 2: apply rule (≥4.50m)
3. Шаг 3: compare против given values
4. Шаг 4: arrive at answer
**Связано с formula:** F-3

### Question 2
...

[continue for all questions extractable from answer sheets]

## §3 Common test scenarios

Per материалов теста, ожидаемые типы вопросов:

1. **«Дано расстояние X между путями — есть Sicherheitsraum?»** → Apply F-1/F-2/F-3 decision tree
2. **«Какой signal даётся в ситуации Y?»** → Apply F-7/F-8/F-9
3. **«Допустимо ли N workers с 1 SIPO?»** → Apply F-12 Kleingruppe rule
4. **«Кто устанавливает Räumzeit?»** → Bauleiter ИЛИ Sakra (per IMG_7676)
5. **«Что означает weiß-rot-weiß Anstrich?»** → Kennzeichen 41 → kein Sicherheitsraum [src: IMG_7676]

## §4 Memorization aids

[Short memorable rules:]
- «**3-4-5**»: <3.70m kein → 3.70m bedingt → 4.50m unbedingt
- «**Ro: 1 long, 2 long, 3 panic**» (Ro 3 = 5×2 short panic pattern)
- «**Kleingruppe = 2+1**»: max 2 workers + 1 SIPO
- «**Räumzeit = Bauleiter ODER Sakra**»
- ...
```

Commit: `[zipo-bvg] Phase 4 test walkthrough + memorization aids`

---

## §7 Phase 5 — BVG Public Materials Search (10-15 min)

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/05-bvg-public-materials.md`

### Steps

1. **WebFetch bvg.de homepage** → identify navigation structure
2. **WebSearch queries:**
   - «Sicherungsposten BVG Schulung»
   - «DUV Dienstanweisung Unfallverhütung BVG U-Bahn»
   - «SIPO Ausbildung Berlin U-Bahn»
   - «Gleisarbeiten Sicherheit BVG»
   - «Rottensignal Ro 1 Ro 2 Ro 3 Bahn»
3. **WebFetch relevant URLs surfaced** — extract content per relevance
4. **Document each source:**
   ```markdown
   ### Source N — [Title]
   - **URL:** [full URL]
   - **Retrieved:** 2026-05-20
   - **Tool:** WebFetch
   - **Type:** [public BVG / DB Netze / Wikipedia / training provider / Reddit thread / etc.]
   - **Relevance to test:** [high / medium / low + explanation]
   - **Key content:**
     - [extracted relevant points]
   ```
5. **Intranet attempt** — WebFetch any `intranet.*` URLs surfaced → expected 401/403 → flag «AUTH-BLOCKED, requires Ruslan SSO export»
6. **Cross-reference к Phase 1-4 outputs** — note where public materials confirm/extend extracted concepts

**Target: 5-10 public sources captured + intranet explicit blocked-list.**

Commit: `[zipo-bvg] Phase 5 BVG public materials search`

---

## §8 Phase 6 — 7 Mermaid Diagrams (10-15 min)

**Output:** `research/zipo-sipo-bvg-schulung-deep-2026-05-20/diagrams/01..07.md`

ВСЕ диаграммы — black text theme init (per `wiki/operations/mermaid-style-guide-2026-05-07.md`):

```
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
```

### Diagram 01 — `01-sicherheitsraum-cross-section.md`
Graph showing cross-section of two parallel tracks: 3.70m / 4.50m thresholds + hatched Sicherheitsraum zone + Fahrbereich + feste Gegenstände с labels in DE+RU. Decision branches для kein / bedingt / unbedingt status.

### Diagram 02 — `02-ro-signal-sequence.md`
Sequence diagram: SIPO sees train → Ro 1 (1 long) → workers acknowledge → Ro 2 (2 long) → Räumzeit countdown → workers in Sicherheitsraum → train passes. Emergency branch: Ro 3 (5× 2 short).

### Diagram 03 — `03-räumzeit-flow.md`
Flowchart: Bauleiter/Sakra устанавливают Räumzeit → Ro 2 sounds → countdown → tools profilfrei → walk ohne Hast к Sicherheitsraum → arrived → safe-confirmed.

### Diagram 04 — `04-sipo-role-responsibilities.md`
Mindmap или graph: SIPO core role split into Observation / Signaling / Emergency / Coordination + responsibility boundaries vs Bauleiter / Sakra / Beschäftigte.

### Diagram 05 — `05-grossprofil-vs-kleinprofil.md`
Comparison table mermaid OR side-by-side graph: Großprofil U-Bahn distance thresholds vs Kleinprofil thresholds (extract из photos если surfaced; иначе note «Großprofil only в этих materials, Kleinprofil не surfaced»).

### Diagram 06 — `06-gefahrenanstrich-identification.md`
Visual decision tree: see weiß-rot-weiß marking → Kennzeichen 41 → kein Sicherheitsraum → required behaviour.

### Diagram 07 — `07-grundarten-sicherungsmassnahmen.md`
Tree: Grundarten der Sicherungsmaßnahmen → (1) technische Einrichtungen BVG-zugelassen / (2) SIPO / (3) fahrdienstlich (Gleissperrung / Langsamfahrstrecken) с when-applies conditions.

Commit: `[zipo-bvg] Phase 6 7 mermaid diagrams`

---

## §9 Phase 7 — Synthesis + Quick-Ref + Printable + Push (10 min)

**Output:**
- `research/zipo-sipo-bvg-schulung-deep-2026-05-20/00-SUMMARY-FOR-RUSLAN.md` (≤500w entry)
- `research/zipo-sipo-bvg-schulung-deep-2026-05-20/06-quick-reference-card.md` (1-2 page cheat sheet ⭐)
- `research/zipo-sipo-bvg-schulung-deep-2026-05-20/07-printable-pdf-source.md` (combined для pandoc → PDF)
- `research/zipo-sipo-bvg-schulung-deep-2026-05-20/MANIFEST.md` (updated с file inventory + cost)

### 00-SUMMARY-FOR-RUSLAN.md structure (≤500w)

```markdown
# Summary для Ruslan — SIPO/ZIPO Schulung BVG (2026-05-20)

## §0 TL;DR (≤100w)
- 19 photos материалов extracted; ~25 концепт glossary entries DE→RU; ~15 формул standalone table; 7 mermaid схем; printable PDF source ready; ~N public BVG materials linked.
- **Top 3 must-remember:** (1) Distance rule «3-4-5» (<3.70m kein / 3.70m+ bedingt / 4.50m+ unbedingt); (2) Ro signals 1 long / 2 long / 3 = 5× 2 short Notfall; (3) Kleingruppe = max 2+1.
- **Ready to use:** Quick-Ref card для pre-test (~2 min read), full glossary для deep prep (~10 min).

## §1 Что в материалах
[brief — 19 photos / concepts covered / regulations referenced]

## §2 Где открыть first
1. `06-quick-reference-card.md` — pre-test scan
2. `02-concepts-glossary-de-ru.md` — DE↔RU понятия
3. `03-formulas-tabelle.md` — все формулы
4. `04-test-walkthrough.md` — пример как считать
5. `diagrams/01-sicherheitsraum-cross-section.md` — visual ⭐

## §3 PDF generation
`pandoc research/zipo-sipo-bvg-schulung-deep-2026-05-20/07-printable-pdf-source.md -o zipo-bvg.pdf --pdf-engine=xelatex -V mainfont="DejaVu Sans"` → PDF готов.
Иначе VS Code Markdown PDF extension OR браузер print-to-PDF.

## §4 BVG public sources captured
[5-10 links с relevance flags]

## §5 What's NOT covered (gaps surface)
- [any concepts mentioned but not deeply explained в photos]
- BVG intranet content (AUTH-blocked; экспорт manually if needed)
- YT/video training (если surfaced — не fetched)

## §6 Cost snapshot
Phase 1 vision: ~€X / Phases 2-7: ~€Y / Total: <€5
Runtime: ~90-120 min
```

### 06-quick-reference-card.md (1-2 page cheat sheet)

```markdown
# SIPO Schulung BVG — Quick Reference

## Distances
| Distance | Status | Action |
|---|---|---|
| <3.70m | kein Sicherheitsraum | Gleissperrung обязательна |
| ≥3.70m + Gefahrenfreiheit OR ≤30 km/h обоими путями | bedingt | SIPO + reduced speed |
| ≥4.50m | unbedingt | SIPO standard |
| Seitlich bis 2.20m | kein | weiß-rot-weiß Anstrich |
| Seitlich ab 2.20m + 0.70m | sufficient | standard |

## Signals
| Signal | DE name | Sound | Meaning |
|---|---|---|---|
| Ro 1 | ein langer Ton | 1× long | Внимание / Train approach detected |
| Ro 2 | zwei lange Töne | 2× long | Убрать tools + зайти в Sicherheitsraum |
| Ro 3 (Notfall) | 5× zwei kurze hintereinander | 5× (short-short) panic | АВАРИЯ! Immediate clear |

## Roles
| Role | DE | Set Räumzeit? | Group composition |
|---|---|---|---|
| SIPO | Sicherungsposten | No | 1 SIPO per Kleingruppe |
| Sakra | Sicherheitsaufsicht | YES | Supervisor |
| Bauleiter | Site manager | YES | Coordinator |
| Beschäftigte | Workers | No | max 2 в Kleingruppe |

## Decision tree
1. Расстояние между путями? → choose F-1 / F-2 / F-3
2. Сколько workers? → ≤2 = Kleingruppe / >2 = additional Maßnahmen
3. Какой signal слышишь? → Ro 1 ждать / Ro 2 убирать tools / Ro 3 PANIC

## Top 10 формул / правил
[10 strict rules с numbers]

## Acronyms
- SIPO = Sicherungsposten
- Sakra = Sicherheitsaufsicht
- DUV = Dienstanweisung Unfallverhütung
- DA U / DA O = Dienstanweisung U-Bahn unterirdisch / oberirdisch
- LTB = [extracted from materials]
- ...
```

### 07-printable-pdf-source.md

Single combined document concatenating: cover page + quick-ref + full glossary + formulas table + walkthrough + diagrams (mermaid blocks rendered or referenced) + BVG sources appendix. Designed для pandoc → PDF generation.

### Final push

```bash
git add research/zipo-sipo-bvg-schulung-deep-2026-05-20/
git commit -m "[zipo-bvg] Phase 7 Summary + Quick-Ref + Printable + MANIFEST + final push"
git push origin main
```

Final echo:
```
DONE Phase 7 — N commits / M files / 7 mermaid / printable PDF source ready / glossary ~25 entries / formulas ~15 / BVG public ~N sources / cost <€5
```

---

## §10 Operational rules

- **Per-phase commit + push** (mandatory)
- **Russian primary** в всех output docs (concept descriptions / examples / cheat sheets)
- **German terms preserved verbatim** — never translate term names, only их definitions/examples
- **No auth bypass** — intranet URLs returning 401/403 → flag «AUTH-blocked», do not retry
- **No paid content** — Ruslan handles separately if needed
- **R6 provenance per claim** — `[src: IMG_NNNN]` или `[src: bvg.de/path retrieved 2026-05-20]`
- **Mermaid black text init** — все 7 diagrams
- **EP-5 F-grade explicit** — verbatim extraction = F2 R-high; translation/examples = F2 R-medium derivative
- **Per-photo timing budget Phase 1:** ~1-2 min per image (vision read + extraction); если photo полностью illegible — flag + continue, не halt

---

## §11 If blocked

- Photo полностью illegible (shadow / blur / corner cut) → flag «UNREADABLE» в that image's section + continue
- WebFetch fails / 404 → log + continue
- Single phase commit fails → retry с force-add (not force-push); если повтор fails → log + continue to next phase
- НЕ halt entire run at single failure point
- **NEVER attempt auth bypass** to intranet

---

*Prompt closure 2026-05-20 morning Berlin. Per memory `feedback_prompt_explanation_required.md` + `feedback_cowork_can_push.md` — EXPLAIN written; Ruslan acked «ебашь записывай промпт я запущу»; commit+push без re-ack.*
