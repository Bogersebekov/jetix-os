---
title: Plain English append-all — добавить «На человеческом» секцию во все brigadier-generated docs
date: 2026-05-18
type: deep-prompt-append-all
target: server CC (brigadier mode, autonomous, 1-2h)
trigger: Ruslan ack — append plain English section ко всем docs (как уже сделано в 09/10/11 research-deepening)
parent_examples:
  - research/deepening-2026-05-18/09-people-karpathy-eureka-llm101n.md §8
  - research/deepening-2026-05-18/10-people-buterin-dacc-trajectory.md §10
  - research/deepening-2026-05-18/11-people-tang-weyl-plurality-2024.md §10
language: russian (primary plain English target language)
---

# DEEP PROMPT — Plain English append-all

> **Ты = brigadier**. Append «На человеческом» секцию **в конец** каждого substantive doc созданного brigadier'ом за последние 2-3 дня. Pattern reference = `research/deepening-2026-05-18/09 / 10 / 11` §8/§10 примеры (Cloud Cowork сделал 3 вручную).

> **ultrathink** ON. Append-only — НЕ trog'ай существующий content. Только добавь section в конец.

---

## §0 SCOPE — какие файлы обработать

### §0.1 IN scope (append plain English section)

**research/deepening-2026-05-18/** (12 docs, 3 уже сделаны Cloud Cowork — skip):
- 00-DEEPENING-PLAN.md
- 01-failure-xanadu-pre-mortem.md
- 02-failure-cybersyn-pre-mortem.md
- 03-failure-stackoverflow-friendtech-pre-mortem.md
- 04-success-engelbart-h-lam-t-mapping.md
- 05-success-alexander-cunningham-karpathy-lineage.md
- 06-success-mondragon-68yr-mechanism.md
- 07-substrate-matrix-vc-sbt-pgp-coordinape.md
- 08-lineage-semat-vs-fpf-gap-analysis.md
- 12-cross-domain-fpf-aerospace.md
- 13-tribe-eve-online-20yr.md
- 14-tacit-explicit-tps-mechanism.md
- 98-CROSS-CUTTING-SYNTHESIS.md
- ~~99-SUMMARY-FOR-RUSLAN.md~~ (уже plain English by design — skip)

**research/adjacent-ideas-2026-05-17/** (10 docs):
- 01-universal-language.md
- 02-intelligence-as-tool.md
- 03-platforms-connecting-people.md
- 04-engineering-methodologist-communities.md
- 05-trust-beyond-money.md
- 06-virtual-tribes.md
- 07-methodology-distribution.md
- 08-interesting-people-list.md
- 09-jetix-positioning-sharpened.md
- ~~00-MASTER-RESEARCH-INDEX.md~~ (navigation, skip)

**vision/jetix-fpf-describe/** (8 docs):
- 01-jetix-as-self-os-substrate.md
- 02-jetix-as-methodology.md
- 03-jetix-as-virtual-tribe-substrate.md
- 04-jetix-as-corporation.md
- 05-jetix-as-clean-internet-layer.md
- 06-jetix-as-platform.md
- 07-jetix-end-to-end-overview.md
- ~~00-MASTER-INDEX.md~~ (navigation, skip)

**vision/** (10 docs from vision-strategy-plan):
- 01-fpf-as-universal-language.md
- 02-internet-layer-for-engineers.md
- 03-jetix-as-masterskaya-platform.md
- 04-first-clan-10-people.md
- 05-testing-strategy-blogerov-clubs.md
- 06-layered-architecture-L0-L4.md
- 07-prototype-platform-2-days-cc.md
- 08-l1-collaboration-roadmap.md
- 09-immediate-steps-current.md
- ~~00-MASTER-VISION-PLAN-2026-05-17.md~~ (уже dual Plain English + FPF formal — skip)

**Total scope: ~38 docs.**

### §0.2 NOT in scope (skip)

- Master index / navigation docs (already plain English by design)
- 99-SUMMARY-FOR-RUSLAN files (designed for plain English)
- Diagrams (`.md` files в `diagrams/` subdirs — visual only, skip)
- 00-MASTER-VISION-PLAN-2026-05-17.md (already has Plain English §3 + FPF formal §4 dual versions)
- Cell drafts в `swarm/wiki/drafts/` (intermediate)
- Already-done by Cloud Cowork:
  - research/deepening-2026-05-18/09 §8
  - research/deepening-2026-05-18/10 §10
  - research/deepening-2026-05-18/11 §10

### §0.3 Verification ДО append

Per file, **check first** — есть ли уже «На человеческом» / «Plain English» / «§N — На человеческом» section в конце? Если ЕСТЬ — skip (already done). Если НЕТ — append.

---

## §1 Template для plain English section

Append в самый конец каждого file (после последней existing section). Numbering: next number после existing last §. Например если doc заканчивается §7 → новая section = §8.

```markdown
---

## §N На человеческом — <topic> (added <agent> 2026-05-18)

### §N.1 Что это (если doc описывает concept / artefact)

[1-2 параграфа простыми словами — кто/что/когда/где. Аналогии. Объяснить терминологию.]

### §N.2 Ключевые pointы

[Bullet list 5-8 пунктов — самое важное. Numbers + dates где есть. Verifiable facts.]

### §N.3 Зачем нам это для Jetix

[2-3 параграфа — конкретно как relates к Jetix vision / objects / Phase 0-1-2 actions. Cross-refs к specific Jetix artefacts.]

### §N.4 Concrete actions

[Numbered list — что Ruslan может сделать NOW / Phase 1 / Phase 2+ на основе этого.]

### §N.5 Резюме на 2 строки

[Compact bottom line — самое главное в одном-двух предложениях.]

---

*Plain English section added by brigadier 2026-05-18 per Ruslan request. Word count of §N: ~XXX.*
```

**Adapt structure per doc type:**

- **People profile** (09/10/11 examples): кто такой / что сделал / зачем нам / actions / резюме
- **Failure case** (01/02/03): что случилось / почему failed / Jetix lesson / mitigation / резюме
- **Success mechanism** (04/05/06/14): что работает / почему работает / Jetix borrow opportunity / actions / резюме
- **Substrate/matrix** (07/08/12): что варианты / trade-offs / Jetix decision input / recommended path / резюме
- **Vision doc**: что claim / FPF translation на человеческом / immediate steps / связь с other Jetix parts / резюме
- **Tribe/community** (13): pattern / longevity factors / Jetix application / actions / резюме

---

## §2 Стиль — что должно быть

1. **Русский primary** — это plain English target language Ruslan-ом ack'нут (он на русском)
2. **Простые слова** — избегай jargon без объяснения. Если термин нужен (FPF / R12 / SBT / etc.) — объясни в скобках первое употребление в section
3. **Аналогии** — «как X, но Y», «представь Z», «литерально как» — useful
4. **Numbers + dates** где есть — concrete > vague
5. **Names + handles** — full names + Twitter/GitHub handles где relevant
6. **Cross-refs к Jetix artefacts** — vision/* / decisions/STRATEGIC-INSIGHT-* / reports/phase-0-fpf-scope/* / wiki/ etc.
7. **No new claims** — surface от existing doc content + plain English rephrase + Jetix-tie. R1 surface-only.
8. **No prescription** — concrete actions = «Ruslan can consider X» / «possible», не «нужно делать X»

---

## §3 Стиль — что НЕ должно быть

- НЕ автор новые strategic claims (R1)
- НЕ изобретать новых facts (если не в parent doc — не упоминать)
- НЕ оценивать «эта идея лучше Jetix» / «эта хуже»
- НЕ promise outreach без Ruslan ack (R1 outreach discipline)
- НЕ дублировать existing structured content — append PE summary только
- НЕ удалять / редактировать existing sections (append-only)
- НЕ commit broken markdown (validate before write)
- НЕ trog'ать diagrams / index / summary docs (skip per §0.2)

---

## §4 Cell dispatch

| Doc type | Cells (2-3 per doc) |
|---|---|
| People profile | mgmt × integrator + phil × critic |
| Failure case | phil × critic + sys × integrator |
| Success mechanism | eng × integrator + mgmt × integrator |
| Substrate matrix | eng × integrator + phil × critic |
| Vision doc | mgmt × integrator + phil × critic |
| Tribe/community | sys × integrator + mgmt × integrator |
| Cross-cutting synthesis | phil × critic + mgmt × integrator + sys × integrator |

Brigadier integrates AP-6 + §5.5.5 gate (lighter — это PE rephrase, not new claims).

---

## §5 Workflow

1. **Phase 1 — Enumerate** — list all files per §0.1 scope; verify per §0.3 ('append' or 'skip already-done')
2. **Phase 2 — Dispatch** — per file, dispatch 2-3 cells parallel per §4 matrix
3. **Phase 3 — Integrate** — brigadier reviews cell drafts, picks best PE rendering, appends to file
4. **Phase 4 — Commit** — batch commits (3-5 files per commit to keep history sane), final push

---

## §6 Acceptance criteria

- [ ] All ~38 in-scope docs have «На человеческом» section appended
- [ ] Each section: что/key points/Jetix relevance/actions/резюме
- [ ] Russian primary, plain words, аналогии
- [ ] Cross-refs к Jetix artefacts
- [ ] Append-only (no overwrites)
- [ ] git commits batched (≤10 commits total)
- [ ] Final push origin main
- [ ] Skip rule respected (already-done docs untouched)

---

## §7 Cost cap

- Daily €10 baseline; halt+ask €50
- Expected: <€1 (text rephrase only, no external API, no large WebSearch)

---

## §8 Examples to mirror

Read these 3 Cloud Cowork-made examples first как style reference:
- `research/deepening-2026-05-18/09-people-karpathy-eureka-llm101n.md` §8 (people profile)
- `research/deepening-2026-05-18/10-people-buterin-dacc-trajectory.md` §10 (people + framework)
- `research/deepening-2026-05-18/11-people-tang-weyl-plurality-2024.md` §10 (people + book + tools)

Style features to mirror:
- Аналогии («как X, но Y»)
- Numbers + dates concrete
- 5-6 subsections per «На человеческом»
- Russian primary + minimal English (только names + tech terms)
- Concrete actions divided NOW / Phase 1 / Phase 2+
- 2-line резюме в самом конце

---

**Launch:**

```bash
tmux new -s plain-english
cd ~/Desktop/jetix-os && git pull --rebase origin main && claude --dangerously-skip-permissions
```

Paste:

```
ultrathink. Прочитай prompts/plain-english-append-all-2026-05-18.md полностью. Ты — brigadier. Append «На человеческом» секцию в конец каждого in-scope doc (~38 файлов; см. §0.1). Skip already-done (Cloud Cowork сделал 09/10/11 в research/deepening) + master indexes + summaries + diagrams. Style reference = 09/10/11 §8/§10 examples. Russian primary, простые слова, аналогии, numbers+dates concrete, cross-refs к Jetix artefacts, concrete actions NOW/Phase 1/Phase 2+, 2-line резюме в конце. Append-only — НЕ trog'ай existing content. Cell dispatch 2-3 per doc per §4 matrix. R1 surface-only (no new claims). Batch commits (3-5 files each), final push origin main. Действуй автономно 1-2 часа.
```

Detach: `Ctrl+B затем D`.
