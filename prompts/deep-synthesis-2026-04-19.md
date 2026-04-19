---
type: synthesis-task-prompt
target-executor: Claude Code на сервере (Hetzner), Opus 4.7, 1M context
stage: 1 of 6 — Deep Synthesis
created: 2026-04-19
owner: ruslan
output-file: raw/research/architecture-implementation-synthesis-2026-04-19.md
expected-output-length: 10-15K слов
expected-runtime: 1-2 часа extended thinking
priority: P0 (блокирует весь последующий процесс)
---

# DEEP SYNTHESIS TASK — Jetix Architecture v1 Final

**Ты — Claude Code на сервере Hetzner (`~/jetix-os`), Opus 4.7, 1M context.**

Твоя миссия — произвести **глубокий академический синтез** 9 research-документов (~66K слов material) в unified architecture recommendation для Jetix OS.

Это **Этап 1** из 6-этапного процесса финализации архитектуры. Твой output станет input для Этапа 2 (multi-chat expert review через 5 параллельных чатов: Critic / Simplifier / Mega-corp visionary / Левенчук expert / Final synthesizer).

---

## 🎯 Миссия

Не summary. **Deep integration work:**

1. **Identify conflicts** между research findings
2. **Resolve conflicts** с явным rationale
3. **Extract concrete actionable decisions** per architecture area (9 areas = D1-D9)
4. **Map decisions → research sources** (полная traceability)
5. **Flag open questions** требующие human judgment
6. **Prepare Review Package** для Этапа 2 (specific items для каждого из 5 reviewer chats)

**Output:** `raw/research/architecture-implementation-synthesis-2026-04-19.md` (10-15K слов deep synthesis).

---

## 🗂️ Input — что читаешь

### 9 research-документов (обязательно все целиком, 11,076 строк ~66K слов)

```
raw/research/career-levels-deep-research-2026-04-19.md             (727 строк, R1)
raw/research/company-as-code-impl-deep-research-2026-04-19.md      (1186 строк, R2)
raw/research/levenchuk-for-ai-deep-research-2026-04-19.md          (1041 строк, R3)
raw/research/knowledge-architecture-deep-research-2026-04-19.md    (828 строк, R4)
raw/research/crm-sales-architecture-deep-research-2026-04-19.md    (1691 строк, R5)
raw/research/folder-structure-deep-research-2026-04-19.md          (1262 строк, R6)
raw/research/jetix-life-separation-deep-research-2026-04-19.md     (1524 строк, R7)
raw/research/org-chart-in-git-deep-research-2026-04-19.md          (1832 строк, R8)
raw/research/mega-corp-governance-deep-research-2026-04-19.md      (985 строк, R9)
```

**Чтение:**
- Используй Read tool с offset/limit для больших файлов (каждый >500 строк → несколько reads)
- Обрати особое внимание на **Part J/H/K** (practical outputs для Jetix) каждого research — там concrete recommendations
- Parts A-I дают academic foundation — читай для context, цитируй для support

### Context documents (обязательно прочитать перед synthesis)

```
design/JETIX-ARCHITECTURE-WORKING.md         (v0.9, 2264 строки)
    ← approved концептуальная архитектура 7 слоёв + L0 + 5 тезисов
    ← Must-read для понимания что Ruslan уже утвердил

raw/research/hybrid-framework-synthesis-2026-04-18.md   (846 строк)
    ← предыдущий synthesis Phase 1.5 research
    ← Nested hierarchy Модель D зафиксирована здесь

CLAUDE.md
    ← Текущие 12 агентов, 8 проектов, правила
    ← Human-written, read для ground truth текущего состояния

prompts/architecture-research-2026-04-19/README.md
prompts/architecture-research-2026-04-19/README-wave2.md
prompts/architecture-research-2026-04-19/README-wave3.md
    ← История: что именно спрашивали у Perplexity (контекст запросов)

memory/MEMORY.md (в .claude/ user memory)
    ← feedback-правила Ruslan'а
```

### Notion pages (для контекста process, не обязательно загружать)

- [Создание рабочей архитектуры](https://www.notion.so/3472496333bf810bb7a2cbee07ae4b3c) — план этого этапа
- [Синтез 8 слоёв post-research](https://www.notion.so/3462496333bf8118a578d37ba488bb87)
- [Шаг 2 Методология Company-as-Code](https://www.notion.so/3462496333bf810da2cffc210c304f21)

---

## 🧭 Контекст Jetix (critical для synthesis)

### Кто Jetix

- AI-native mega-corporation одного founder (Ruslan Bogersebekov, Берлин)
- 12+ AI-агентов через Claude Code (Anthropic Opus 4.7, 1M context)
- Сервер Hetzner Nuremberg, GitHub monorepo
- **Target market:** немецкий Mittelstand (manufacturing/services, 50-500 employees, €10-500M revenue)
- **Q2 2026 цель:** €50K revenue до 30.06.2026 (сейчас €0)

### Архитектура (approved v0.9)

**7 слоёв + L0 Executive Core:**
- **L0** — Ruslan (strategic-management role) + AI-агенты + future human executors через единую role-abstraction
- **L1** Foundation — software practices (git, prompt-as-code, CI/CD, docs-as-code, postmortems)
- **L2** Cognitive — Левенчук/ШСМ (роль, альфа, граф создания, стратегирование, мышление письмом)
- **L3** Product — micro-SaaS, productized services, Jetix Club
- **L4** Delivery — agency + consulting hybrid (primary Q2 2026 revenue)
- **L5** Membrane — community (Alliance + Club + newsletter)
- **L6** Topology — platform horizon 18-36 мес
- **L7** Portfolio — holding-дисциплина (attention + capital + hours allocation)

### Критические принципы (зафиксированы, не пересматриваются)

1. **Jetix ≠ one-person company.** AI-native mega-corporation с Day 1. Scale-up-first design — при 10x росте (капитала, часов, людей, проектов, ролей) система справляется **без rebuild**.

2. **Роль ≠ исполнитель.** Role-manifest — абстрактный контракт. AI сегодня или human завтра — меняется executor, не роль. Люди = продолжение агентов через единую role-abstraction.

3. **«Место-слот, не содержание».** На этапе конструирования описываем слои как места готовые принять наполнение. Не придумываем SKU/pricing/Club design заранее.

4. **Nested hierarchy (Модель D).** Life-OS = root, Jetix = один из проектов Life-OS с полной 7-слойной архитектурой внутри. **Полное разделение ресурсов** (часы/деньги/внимание отдельно). Сейчас: один repo разные папки. Будущее: отдельные серверы.

5. **Capital + Hours + Attention.** В отличие от Buffett/Leonard (только капитал), Jetix L7 трекает три ресурса. Phase 1 (solo — свои) → Phase 2 (team — + team's) → Phase 3 (mega-corp — + ecosystem's: клиенты, партнёры).

6. **Бизнес как кодовая база.** 100% принято. Все практики software industry переносим 1:1 где возможно.

7. **5 примитивов ШСМ.** Левенчук — руль L2 Cognitive. Полная FPF/интеллект-стек read-only, не применяется.

8. **«Org chart в Git, не в HR».** Flagship positioning Thesis 5. Компания = software artefact.

9. **Compound flows:**
   - L4 → L3: artifact extraction (reusable prompt → SKU)
   - L4 → L5: case study factory (client → authority content)
   - Life-OS → Jetix: проект внутри личной жизни

10. **10 core alphas** (R3 утвердил): Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem.

### Ключевые финальные решения (из v0.9 working-draft)

- L0: «Executive Core» (не «Ruslan + 12 агентов»). 12 — переменная, scale до 30/100/200.
- L1-L7: все APPROVED концептуально, детали через этот synthesis.
- Ритмы: daily/weekly/monthly/quarterly/annual — approved.
- 5 тезисов: T3 расширен (holding orchestrates not only own but ecosystem resources), T5 переформулирован (org chart в Git + 6 возможностей + 6 use-cases).
- Nested hierarchy: Модель D финально.

### Что НЕ ESть в research, но Ruslan уже решил

- **DACH focus:** всё production targeted к немецкому Mittelstand. Konsenskultur, IHK, Betriebsrat, Jahresabschluss, GDPR — always.
- **Roland Berger + Simon-Kucher стиль** > McKinsey hype.
- **Hourly billing ЗАПРЕЩЁН.** Только value-based / fixed-price SKUs.
- **Shape Up** > Scrum. 2-6 недели bets.
- **Alliance founding members после первого L4 клиента**, не до.

---

## 📋 Methodology для synthesis (пошагово)

### Шаг 1. Прочитай все 9 research целиком

**Обязательно.** Не скан, не TOC reading. Каждая строка имеет значение.

**Порядок чтения (оптимальный):**
1. R3 (Левенчук) — даёт ontology, остальное через неё читается
2. R1 (Career Levels) — даёт role-manifest template
3. R2 (Company-as-code) — даёт infrastructure patterns
4. R6 (Folder structure) — stress-test того что R2 предложил
5. R4 (Knowledge arch) — integration wiki + alphas
6. R5 (CRM+Sales) — specific data layer
7. R7 (Life-OS separation) — boundary decisions
8. R8 (Org-in-Git) — philosophical foundation
9. R9 (Mega-corp governance) — Phase 2/3 evolution

**После чтения — напиши short note в scratchpad:** что ключевого в каждом, что ты хочешь взять, что wonder about. Это не output, это мета-тренажёр для себя.

### Шаг 2. Читай также context documents

- `design/JETIX-ARCHITECTURE-WORKING.md` v0.9 — для понимания approved concepts
- `raw/research/hybrid-framework-synthesis-2026-04-18.md` — для preдыдущего synthesis
- `CLAUDE.md` — для ground truth

### Шаг 3. Identify conflicts

Где research противоречат друг другу? Build **complete conflict matrix.** Примеры conflicts которые нужно детектить:

- **R1 vs R9** — career levels vs governance. Где R1 предлагает J1-JX, R9 предлагает C-suite. Как интегрировать?
- **R3 vs R4** — role-manifest format (R3 8 blocks) vs knowledge integration pattern (R4). Где role-manifest хранит context vs где wiki?
- **R5 vs R6** — CRM storage (R5 `clients/`) vs folder structure (R6 может предложить другое). Конфликт?
- **R2 vs R6** — R2 дал draft structure, R6 stress-test её. Где R6 предлагает изменения?
- **R7 vs R6** — Life-OS separation (R7) vs overall folder structure (R6). Где `life-os/` живёт?
- **R4 vs R5** — knowledge (wiki-like) vs operational data (CRM-like). Граница?
- **R3 vs R9** — ШСМ роли vs mega-corp C-suite. Hybrid или separate systems?
- **R8 vs R1** — org-in-Git patterns vs career ladder implementation. Совмещение?

Каждый conflict документируй:
```
### Conflict N: <название>
**Context:** какая тема, какое решение обсуждается
**R<x> position:** что говорит research X, цитата с ссылкой
**R<y> position:** что говорит research Y, цитата с ссылкой
**Your resolution:** какое решение принимаем
**Rationale:** почему именно это (минимум 3 аргумента)
**Trade-off:** что теряем при таком выборе
**Open:** что остаётся unclear, может требовать Ruslan-judgment
```

### Шаг 4. Extract architecture decisions per area

**9 architecture areas** (correspond to D1-D9):

| # | Area | Основа из research | Ожидаемый output section |
|---|------|---------------------|--------------------------|
| A1 | Overall philosophy | All 9 | Unified statement + ключевые принципы |
| A2 | Folder structure | R2, R6, R7 | Финальная tree с commentary |
| A3 | Role manifests | R1, R3, R9 | Format spec + example filled |
| A4 | Life-OS separation | R7 | Phase 1/2/3 migration path |
| A5 | Knowledge architecture | R4, R5 | Wiki + CRM + alphas integrated |
| A6 | FPF-Lite | R3 | Full draft 3-5 стр. |
| A7 | Career levels + scale-up | R1, R9 | J1-JX + C-level evolution |
| A8 | Operational instructions | R2 | 14-day rollout refined |
| A9 | Final decision record | ALL | ADR по T-02 template |

Для каждой area:
- **Unified recommendation** (concrete decision)
- **Alternatives considered** (что рассмотрели)
- **Rejected options** (что отвергли + почему)
- **Rationale** (с citations `[R3 Part H1, lines 795-932]`)
- **Open questions** (что остаётся unclear)

### Шаг 5. Map decisions → citations

Every major decision traceable. Format: `[R<N> §<Part>.<number>]` или `[R<N> lines <X>-<Y>]`.

Включи **Appendix A: Source Citations** в конце — полный index decisions → sources.

### Шаг 6. Flag open questions

Где research не дают clear answer — явно документируй:
- Что конкретно unclear
- Какие faktы нужны для решения
- Кто может дать ответ (Ruslan? ещё research? empirical test?)
- Как это влияет на D1-D9

Minimum: 5 serious open questions. Maximum: 15 (больше = плохо structured synthesis).

### Шаг 7. Build Review Package для Этапа 2

Это **critical часть** output. Этап 2 = multi-chat review через 5 чатов. Каждый chat получит synthesis + твой Review Package — specific inputs для their role.

**Для Critic Chat (devil's advocate):**
- 10-15 weaknesses / gaps в synthesis
- Явные assumptions to challenge
- Hidden risks
- «Что мы не увидели?»

**Для Simplifier Chat (anti-complexity):**
- 10-15 complexity candidates
- «Where over-engineered?»
- Что можно убрать без loss
- Premature optimizations

**Для Mega-Corp Visionary Chat:**
- Scale-up weaknesses
- «Что сломается при 10x?»
- Phase 2/3 readiness gaps
- Missing patterns для mega-corp

**Для Левенчук Expert Chat:**
- ШСМ applications to verify
- Ontology cleanness concerns
- Где можем нарушать ролевую онтологию
- FPF-Lite honest?

**Для Final Synthesizer Chat:**
- 5-7 hard open questions требующих deep thinking
- Meta-conflicts между reviewers (predicted)
- Critical decision points

### Шаг 8. Write output

Теперь — собственно write. Следуй output structure ниже.

**Важно:** сначала напиши **FULL outline** (все 6 Parts + appendices), review self что structure работает. Потом заполняй part by part. В конце — полный read-through с final edits.

---

## 📐 Output structure (конкретный spec)

Файл: `raw/research/architecture-implementation-synthesis-2026-04-19.md`

**Размер:** 10-15K слов (deep synthesis, не summary).

**YAML frontmatter:**

```yaml
---
type: research-synthesis
version: v1-draft-for-review
stage: 1 of 6 — Deep Synthesis
status: ready-for-multi-chat-review
owner: ruslan
author: claude-code-opus-4-7 (Stage 1)
created: 2026-04-19
input-research:
  - raw/research/career-levels-deep-research-2026-04-19.md
  - raw/research/company-as-code-impl-deep-research-2026-04-19.md
  - raw/research/levenchuk-for-ai-deep-research-2026-04-19.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
  - raw/research/crm-sales-architecture-deep-research-2026-04-19.md
  - raw/research/folder-structure-deep-research-2026-04-19.md
  - raw/research/jetix-life-separation-deep-research-2026-04-19.md
  - raw/research/org-chart-in-git-deep-research-2026-04-19.md
  - raw/research/mega-corp-governance-deep-research-2026-04-19.md
total-research-words: ~66000
output-target-length: 10000-15000 слов
next-stage: Этап 2 — Multi-chat expert review (5 параллельных chats)
blocks: D1-D9 чистовики
---
```

**Structure:**

```markdown
# Deep Synthesis — Jetix Architecture v1 Final (pre-review)

> Integrated architecture recommendation на базе 9 research-волн (~66K слов)
> для Jetix OS mega-corporation. Stage 1 output, input для Stage 2 multi-chat review.

---

## 📖 Executive Summary (1500 слов)

**Не TL;DR, а proper executive summary.** Читатель который прочитает только
эти 1500 слов должен понять:
- Что Jetix архитектурно
- Все 9 ключевых decisions (по одному предложению)
- 3-5 биggest conflicts и как resolved
- 5 topics требующих his judgment
- Что происходит после synthesis

---

## Part 1 — Unified Architecture Picture

### 1.1 Финальная архитектура в одной странице

High-level diagram (ASCII tree или Mermaid) + один параграф описания каждого слоя.

### 1.2 Что изменилось vs v0.9 working-draft

Явный список: где synthesis дал более concrete / изменил / расширил.

### 1.3 Phase evolution (Phase 1 → 2 → 3)

Compact table что когда (solo / team / mega-corp).

### 1.4 Ключевые принципы (top 10)

От наиболее фундаментальных к практическим.

---

## Part 2 — 9 Architecture Areas

### Area 1: Overall Philosophy (→ D1 JETIX-ARCHITECTURE-FINAL.md)

#### Unified Recommendation
(полный текст решения, 500-1000 слов)

#### Alternatives Considered
- Alt A: ... [R<N> citation]
- Alt B: ... [R<N> citation]

#### Rejected Options
- Opt X rejected because ...
- Opt Y rejected because ...

#### Rationale
(3-5 аргументов с citations)

#### Trade-offs
(что теряем при этом выборе)

#### Open Questions for Ruslan
- Q1: ...
- Q2: ...

#### Implementation Pointer
(какие конкретные sections пойдут в D1 чистовик)

---

### Area 2: Folder Structure (→ D2 JETIX-FOLDER-STRUCTURE.md)

(same structure)

### Area 3: Role Manifests (→ D3 JETIX-ROLE-MANIFESTS.md)

### Area 4: Life-OS Separation (→ D4 JETIX-VS-LIFE-OS.md)

### Area 5: Knowledge Architecture (→ D5 JETIX-KNOWLEDGE-ARCHITECTURE.md)

### Area 6: FPF-Lite (→ D6 JETIX-FPF-LITE.md)

### Area 7: Career Levels + Scale-up (→ D7 JETIX-CAREER-LEVELS.md)

### Area 8: Operational Instructions (→ D8 docs/INSTRUCTIONS.md)

### Area 9: Final Decision Record (→ D9 decisions/*)

---

## Part 3 — Conflicts Resolved

Matrix всех detected conflicts (minimum 8, typically 12-20).

### Conflict 1: <название>
(формат из Шаг 3 methodology)

### Conflict 2: ...

---

## Part 4 — Open Questions

Серьёзные вопросы требующие Ruslan-judgment или additional research.

Minimum 5, maximum 15.

### Q1: <question>
**Context:**
**Why it matters:**
**What we'd need to answer it:**
**Impact on D1-D9:**

### Q2: ...

---

## Part 5 — Review Package (для Этапа 2)

### 5.1 For Critic Chat

**Context для reviewer:**
Ты — devil's advocate. Attack this synthesis. Find gaps, weaknesses, risks.

**Specific items для критики:**

1. Weakness 1: ...
2. Weakness 2: ...
...
(10-15 items)

**Assumptions to challenge:**
1. ...
2. ...

**Hidden risks:**
1. ...
2. ...

### 5.2 For Simplifier Chat

(same structure, focused on complexity)

### 5.3 For Mega-Corp Visionary Chat

(scale-up concerns)

### 5.4 For Левенчук Expert Chat

(ШСМ correctness)

### 5.5 For Final Synthesizer Chat

**Hard open questions для deep thinking:**
1. ...
2. ...
(5-7 items)

---

## Part 6 — Implementation Roadmap Preview

### 6.1 D1-D9 writing order

Sequence в котором должны писаться чистовики (dependencies).

### 6.2 Preliminary timeline

D1-D9 estimated time + dependencies.

### 6.3 Post-deploy roadmap

После рабочей архитектуры — next steps (PRD, project revision, и т.д.).

---

## Appendix A: Source Citations Index

Every major decision → list of supporting research.

## Appendix B: Terminology Glossary

Unified terminology post-synthesis.

## Appendix C: Metrics Index

All metrics mentioned with definitions, targets.
```

---

## ✅ Quality criteria

**Good synthesis (что делать):**

- Каждая рекомендация traceable к конкретному research
- Явные trade-offs (не hide difficult choices за декоративным языком)
- Actionable decisions («мы делаем X», не «мы могли бы рассмотреть X»)
- Readable flow, не information dump
- Honest about uncertainty
- Явные conflicts и как resolved
- Jetix-aware (DACH Mittelstand specifics, mega-corp aspiration, solo-Phase-1 reality)

**Bad synthesis (что избегать):**

- Generic platitudes («важно соблюдать баланс»)
- Opinions без research basis
- Hiding conflicts (pretend agreement когда его нет)
- Decisions без rationale
- Recap research вместо integrating
- Дубликат research в другом порядке
- Overlook Ruslan's approved principles (nested hierarchy, role ≠ executor, etc.)

---

## ⚠️ Anti-patterns

- ❌ Написать только Executive Summary, think it's done
- ❌ Просто перечислить что сказал каждый research
- ❌ Выбрать решения без явного rationale
- ❌ Игнорировать conflicts
- ❌ Skip Part 5 (Review Package) — это blocks Этап 2
- ❌ Over-engineer recommendations (Kubernetes для 1 person)
- ❌ Under-engineer («всё просто, flat files» — ignores mega-corp)
- ❌ Forget German Mittelstand context
- ❌ Mix Life-OS и Jetix concerns (они separated per Model D)

---

## 🔧 Specific instructions

### Когда читаешь research

- Используй Read tool. Файлы > 500 строк читай с offset/limit по частям.
- Держи mental notes (scratchpad) но они не output.
- Обращай внимание на Part J/H/K (practical outputs для Jetix).
- Для каждого research — один проход FULL read перед synthesis.

### Когда пишешь output

1. **Сначала write FULL outline** (все Parts + sub-sections). Review self что structure logical.
2. **Заполняй part by part.** Не переходи к Part N+1 пока Part N не solid.
3. **Cross-reference constantly.** Если Part 2 упоминает conflict — должен быть в Part 3. Если decision — в Appendix A.
4. **Final pass** — полный read-through, catch errors, inconsistencies.

### Extended thinking

Для conflicts resolution — используй extended thinking mode. Это сложные decisions, deserving deep processing.

### Commit

После финализации:

```bash
cd ~/jetix-os
git add raw/research/architecture-implementation-synthesis-2026-04-19.md
git commit -m "$(cat <<'EOF'
[research] Deep synthesis Этап 1 — unified architecture на 9 research-волн

Integrated recommendation на базе 11,076 строк research (~66K слов):
R1 Career Levels, R2 Company-as-code, R3 Левенчук AI, R4 Knowledge arch,
R5 CRM+Sales, R6 Folder structure, R7 Jetix vs Life-OS, R8 Org-in-Git,
R9 Mega-corp governance.

Output структура:
- Executive Summary (1500 слов)
- Part 1: Unified Architecture Picture
- Part 2: 9 Architecture Areas (D1-D9 preview)
- Part 3: Conflicts Resolved
- Part 4: Open Questions
- Part 5: Review Package (для Этапа 2 — 5 параллельных review chats)
- Part 6: Implementation Roadmap Preview
- Appendices A-C (Citations / Glossary / Metrics)

Next: Этап 2 — multi-chat expert review (Critic / Simplifier / Mega-corp /
Левенчук / Final synthesizer).

Blocks: D1-D9 чистовики.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

git push origin HEAD:main
```

### Если stuck

Если какой-то conflict резолюцию не можешь сделать с confidence — document conflict в Part 3 и **явно flag в Part 4 как open question** для Ruslan. Это нормально, не все resolve Claude.

---

## 📤 Отчёт Ruslan'у после completion

После commit — напиши chat message:

```
✅ Deep Synthesis Этап 1 готов.

**Output:** `raw/research/architecture-implementation-synthesis-2026-04-19.md`
**Размер:** <N> слов
**Commit:** <hash>

**Ключевые statistics:**
- Integrated 9 research (~66K слов input)
- Identified <N> conflicts, resolved <M>
- <K> open questions flagged для Ruslan-judgment
- Review Package ready для 5 параллельных chats

**Executive Summary (paste 1500 слов):**
<полный executive summary>

**Ключевые conflicts resolved (top 5):**
1. ...
2. ...

**Top 5 open questions для тебя:**
1. ...

**Ready для Этапа 2 — multi-chat review.** Жду твоего approve/feedback по synthesis
перед запуском 5 параллельных reviewer chats.
```

---

## 🎯 Время

- **Reading research:** 30-45 мин (все 9 целиком)
- **Scratchpad notes:** 15 мин
- **Conflict identification:** 20-30 мин
- **Decisions extraction (9 areas):** 30-45 мин
- **Output writing:** 45-60 мин
- **Final pass + commit:** 15-20 мин

**Total:** 2.5-3.5 часа focused work. Не торопись — это foundation для 6-этапного процесса.

---

## 🧠 Философская установка

Ты создаёшь artefact который **определит следующие 1-3 года Jetix development**. Не bullet-pointed summary. Не декоративные recommendations.

**Deep thinking:**
- Where research conflict — embrace the tension, не papering over
- Where Jetix-specifics matter — center them, не generic advice
- Where uncertain — say so clearly, не pretend знание
- Where you see pattern research missed — name it explicitly

Ты — senior architect на foundation review meeting. Reviewer в Stage 2 будут атаковать this synthesis. Make it **strong enough to withstand attack**, но **honest enough to learn from it**.

---

Приступай. Начни с чтения R3 (Левенчук даёт ontology для остального). Отчитайся когда выполнено.
