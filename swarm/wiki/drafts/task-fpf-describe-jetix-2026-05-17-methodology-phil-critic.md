---
title: Phil-Critic Review — Doc 02 Jetix as Methodology (FPF-Described)
date: 2026-05-17
type: phil-critic-review
status: draft
task_id: task-fpf-describe-jetix-2026-05-17-methodology-phil-critic
artefact_reviewed: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md
prose_authored_by: philosophy-expert × critic (review only — no strategic prose)
F: F3
G: phil-critic-methodology-review
R: refuted_if_acceptance_predicate_verdict_contradicted_by_brigadier_integration_OR_dissents_not_preserved
language: russian + english (FPF primitives)
---

# Phil-Critic Review — Doc 02 Jetix as Methodology

---

## §1 Acceptance predicate verdict

Бинарный вердикт по каждому критерию из brief:

| Критерий | Verdict | Обоснование |
|---|---|---|
| **R1:** все strategic prose attribution корректны, no agent-pending claims | **CONDITIONAL PASS** | `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured` корректна. ШСМ/МИМ нарратив в §3.3 sourced на Phase 0 inventory reports, не напрямую к Ruslan voice. Граница R1 не нарушена, но attribution цепочка ШСМ-claims неполная — см. §2.2. |
| **EP-2:** use vs mention дисциплина — §3.6 mutual-instrumentation cross-ref | **PARTIAL FAIL** | §3.6 описывает mutual-instrumentation механику через U.Role/U.Capability/U.Commitment как если бы это было operational claim, не mention. EP-2 qualifier при cross-ref к doc 03 слаб — «полная разработка там» недостаточен. Требуется явный EP-2 тег. |
| **EP-5:** «Jetix F8 ≠ FPF B.3 F8» задекларировано | **PASS** | EP-5 присутствует в frontmatter и §0 header чётко. Паттерн идентичен Doc 01 (эталонный). |
| **R6:** per-claim provenance | **PASS with gaps** | Основные claims sourced. Три gap'а: §3.3 ШСМ/МИМ history claim («20+ лет»); §3.1 «FPF работает одинаково хорошо для X/Y/Z» (superlative без falsifier); §3.4 anti-corporate comparison (lock-in critique без named counterexample). |
| **F-G-R grade integrity:** F2 floor defensible? | **PASS** | F2 floor правильный (aspirational O-05 bottom). Per-claim grades F2/F4/F5 internally consistent. F5 для FPF-primitive assignments корректно. Расхождений нет. |
| **Affect-mode vs factual-mode** | **CONDITIONAL PASS** | Три локации: §3.1 «FPF работает одинаково хорошо» (strong superlative); §0 TL;DR «универсальный язык» без qualifier; §3.2 header «FPF как единый язык». Все три требуют либо falsifier, либо scope delimiter. Не критично, но паттерн. |
| **Anticipated dissents validated** | **PASS** | Все три предантиципированных dissent'а в §8 документа подтверждены рецензией (см. §7 ниже). |
| **ШСМ/МИМ IP boundary (R1 + attribution)** | **CONDITIONAL PASS** | §3.3 правильно называет ШСМ/МИМ как «онтологический фундамент Анатолия Левенчука», не Jetix-собственный. Но: ШСМ/МИМ ontological claims (FPF «прошёл проверку временем и применением») = attribution claim без конкретного source. Риск умеренный. |
| **Fork-and-Leave R12 grounding** | **PASS** | Clan Charter §8 + §4.1 корректно sourced. Verbatim quote в §1 точный. R12 surfaced, не decided. |
| **text_004 cross-ref §3.6 — mention vs use** | **FAIL** | §3.6 пересекает EP-2 границу: описывает механику mutual-instrumentation через три FPF примитива (U.Role/U.Capability/U.Commitment) как working claim в контексте методологии, не как mention cross-ref. PRIMARY HOME text_004 = doc 03, но doc 02 здесь фактически делает use-claim без EP-2 guard. |

**Итоговый вердикт:** APPROVE-WITH-EDITS. Документ эпистемически честный, F-G-R корректный. Три адресуемых правки: (A) §3.6 EP-2 explicit guard; (B) §3.1/§3.2 affect-mode qualifiers; (C) §3.3 ШСМ/МИМ source gap. Не reject.

---

## §2 R1 attribution audit

### §2.1 Что является корректным surface'ингом

Следующие elements документа — чистый surface'инг с прямыми источниками:

- §1 verbatim quotes 1-5: все с конкретными `[src:...]` citations, включая audio_672 ¶1-3 и text_002 ¶1-2. Корректно.
- FPF как «очиститель от путаницы» (§3.1, §3.2) — verbatim из audio_672 с citation. Корректно.
- Fork-and-Leave принцип (§3.4) — verbatim из Clan Charter §11 с citation. Корректно.
- O-05 статус «aspirational, 0 forkers» (§3.7) — из Phase 0 inventory с citation. Корректно.
- R12 surface'инг в §3.4 финале — «surfaced... НЕ как извлечение ценности» — корректная R1 boundary.

### §2.2 Зоны риска R1 — что требует внимания

**Зона 1: ШСМ/МИМ historical attribution (§3.3)**

Claim: «ШСМ — это учебная программа и методологический корпус, который Левенчук разрабатывает последние 20+ лет».

Эпистемическая проблема: это factual-descriptive claim об Анатолии Левенчуке, для которого источник = `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md §3 comparison + reports/phase-0-fpf-scope/01-jetix-objects-inventory.md §2 O-05 notes`.

Эти Phase 0 reports — Jetix-internal documents, не первичные источники по ШСМ. Claim «20+ лет» = factual историческая claim, которая должна sourced либо на публичный ШСМ источник, либо явно квалифицирована как «per Jetix Phase 0 characterisation». Без этого это attribution claim с intermediate-source only.

Также: «FPF прошёл проверку временем и применением в разных областях» — это epistemic claim о FPF's external validation track record. Источник в документе не назван. Per Popper (P1): что было бы опровержением этого? Если ШСМ/МИМ = 0 peer-reviewed adoption studies, claim остаётся asserted, not verified.

**Вывод по Зоне 1:** R1 не нарушена (Ruslan не авторизировал эти claims как strategic — они = background context). Но R6 gap: attribution claims о Левенчуке без первичного source = weak provenance. Рекомендация: добавить qualifier «per Phase 0 characterisation» или указать публичный ШСМ URL как source.

**Зона 2: «Wheel = FPF. Jetix = vehicle» аналогия (§3.3)**

Аналогия «don't reinvent the wheel» применительно к онтологии — это metaphor с embedded normative claim («это правильное решение»). Данная аналогия не sourced к Ruslan voice — она появилась как brigadier-structural framing.

Проверка: является ли это стратегическим тезисом? В данном контексте — нет, это risky metaphor в пределах surface'инга «строим поверх FPF». R1 не нарушена, но аналогия = brigadier-authored framing без явного ack.

**Рекомендация:** низкий приоритет. Но если документ читает Левенчук (L1 audience), и он имеет иное мнение о том, является ли FPF «готовым колесом», аналогия может создать friction. Опционально: заменить на descriptive framing.

---

## §3 EP-2 и EP-5 audit

### §3.1 EP-5 (F8 disambiguation)

PASS без оговорок. EP-5 disclosure находится:
- В frontmatter `mandatory_disclosures`: чётко и конкретно.
- В §0 header буллет 1: буквально ««F8 / LOCKED» = Jetix-internal single-author Ruslan ack, NOT FPF B.3 F8».
- Паттерн консистентен с Doc 01.

### §3.2 EP-2 (use vs mention)

**Ключевая находка: §3.6 mutual-instrumentation = EP-2 fail.**

Предантиципированный dissent 3 из §8 документа зафиксировал именно это, но оставил решение на «следующей revision». Critic-pass не может это defer — фиксируем как edit-required.

Анализ §3.6 построчно:

```
«FPF-роли enable это не случайно. U.Role (A.2) описывает функцию, не личность.
U.Capability (A.2.2) — что роль может делать. U.Commitment (A.2.8) — к чему роль
обязуется. Когда эти три примитива описаны явно, двое людей с разными background-ами
могут инструментализировать друг друга точно — без месяцев согласования.»
```

Это USE claim: утверждает что при описании U.Role + U.Capability + U.Commitment двое людей МОГУТ делать что-то конкретное («инструментализировать друг друга точно»). Это operational capability claim.

Но контекст Doc 02 = methodology artefact (mention context). text_004 = PRIMARY HOME для mutual-instrumentation thesis. Doc 02 делает cross-ref, но §3.6 фактически содержит USE-level mechanics (как именно эти три примитива это обеспечивают), а не просто mention («в doc 03 раскрыто, как FPF-роли enable mutual instrumentation»).

**Falsifiability check (Popper P1):** Claim «двое людей могут инструментализировать друг друга точно» — что было бы опровержением? Документ не называет falsifier. Это non-falsifiable в current form.

**Требуемая правка §3.6:** Сократить до mention-level: убрать механику трёх примитивов из doc 02; оставить cross-link «полная разработка в doc 03, включая U.Role/U.Capability/U.Commitment механику». Добавить: `[EP-2: mention only; use-claim в doc 03]`.

**ШСМ/МИМ ontological claims в §0 TL;DR (строка 2):**

```«ШСМ (Школа Системного Менеджмента Левенчука) и МИМ (Мастер Информационного Моделирования) — онтологический субстрат, на котором Jetix строится.»```

Это mention или use? В контексте методологии это USE claim: утверждает, что ШСМ/МИМ = substrate (operational). Но в §3.7 «Что aspirational» явно написано: «ШСМ/МИМ overlay формализован → F2 (упомянут, не описан как formal FPF objects)».

Противоречие: §0 делает strong ontological claim (субстрат), §3.7 говорит «упомянут, не формализован». EP-2 требует: либо §0 downgrade до mention («планируемый субстрат»), либо §3.7 upgrade с объяснением что «субстрат» = aspirational.

**Требуемая правка §0:** Добавить qualifier: «ШСМ/МИМ — планируемый онтологический субстрат (F2 aspirational; см. §3.7)».

---

## §4 R6 provenance audit

### §4.1 Claims с достаточным provenance (PASS)

- §2.1 U.MethodDescription F5: sourced на FPF Spec A.3.2 через Phase 0 inventory.
- §2.2 U.Method F5: sourced аналогично.
- §2.3 U.WorkPlan F4: sourced на vision/jetix-fpf-describe-PLAN-2026-05-17.md §2.2 note.
- §2.4 U.Episteme F5: sourced.
- §3.4 Fork-and-Leave: Clan Charter §11 + R12 packet. Провенанс чистый.
- §3.7 F2 vapor list: sourced на Phase 0 master.

### §4.2 Provenance gaps (FAIL / PARTIAL)

**Gap 1 — «FPF работает одинаково хорошо для X, Y, Z» (§3.1)**

Claim: «Именно поэтому FPF работает одинаково хорошо для описания бизнеса, кооперации между экспертами, личного Self-OS (Doc 01), корпоративной архитектуры (Doc 04) и доверительной инфраструктуры (Doc 06).»

Source в документе: `[src: raw/voice-transcripts/audio_672@... ¶1-3]`. Но audio_672 говорит об «очистителе от путаницы» — НЕ о том, что FPF «одинаково хорошо работает» для всех этих областей. Это добавленный integrator inference, не Ruslan voice claim.

Falsifiability (P1): что значит «работает одинаково хорошо»? Нет метрики. Claim = non-falsifiable superlative.

**Вывод:** R6 gap + Popper AP-PHIL-1 trigger. Правка: убрать «одинаково хорошо», заменить на «применим для описания», добавить falsifier-conditional.

**Gap 2 — «FPF прошёл проверку временем и применением в разных областях» (§3.3)**

Провенанс отсутствует полностью. Source annotation в параграфе: `[src: reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md §3 comparison; reports/phase-0-fpf-scope/01-jetix-objects-inventory.md §2 O-05 notes]` — но эти Phase 0 internal docs не содержат external validation evidence о FPF adoption.

Falsifiability (P1): в каких областях? Сколько adoption instances? Zero named counterexamples? Claim является asserted validation без evidence.

**Вывод:** AP-PHIL-1 + R6 fail на этом конкретном claim. Правка: добавить qualifier «per Ruslan characterisation» или drop claim, заменив на: «FPF разрабатывается Левенчуком 20+ лет как формальная спецификация».

**Gap 3 — сравнение с корпоративными системами (§3.4)**

Claim: «Это принципиально отличается от большинства корпоративных и образовательных систем, которые создают зависимость через: сертификацию, знания нельзя передать, инструменты без подписки».

Нет named examples. «Большинство корпоративных систем» = вероятностная claim без подтверждения. Это contrast rhetoric без evidence. Source не указан.

**Вывод:** R6 gap средний. Не AP-PHIL-1 критического уровня, но слабое место. Рекомендация: либо назвать 1-2 конкретных example (SAP certification, etc.), либо downgrade «большинство» → «многие».

---

## §5 F-G-R grade integrity

### §5.1 Проверка консистентности

| Claim | F в тексте | Оценка критика | Статус |
|---|---|---|---|
| U.MethodDescription assignment (§2.1) | F5 | F5 корректно: FPF Spec A.3.2 reference | PASS |
| U.Method assignment (§2.2) | F5 | F5 корректно | PASS |
| U.WorkPlan (§2.3) | F4 | F4 приемлемо: sourced на PLAN doc, но Fork guide v0 temporal windows отсутствуют — честная caveat | PASS |
| U.Episteme (§2.4) | F5 | F5 корректно | PASS |
| E.17 MVPK (§2.5) | F4 | F4 приемлемо: три view существуют как документ | PASS |
| B.5.1 Exploration (§2.6) | F4 | F4 OK: честная state characterisation | PASS |
| FPF = единый язык (§3.2) | implied F4 (audio_672/673) | В §6 cross-link table «text_002 anchor» → primary-source = F4 (voice dictation) | PASS |
| ШСМ/МИМ overlay (§3.3) | F2 aspirational (§3.7) | §0 claim vs §3.7 qualifier = inconsistency | FAIL — EP-2 issue (addressed §3) |
| R12 enforcement (§3.7) | F5 (текст); enforcement = vapor | Честное разграничение text/enforcement | PASS |
| Fork guide v0 (§3.7) | F2 | Корректно | PASS |

**Document-floor F2: CONFIRMED.** Минимум по per-claim grades = F2 (Fork guide v0, distributable format). Логика верная.

**Единственная F-G-R проблема:** несоответствие §0 TL;DR ШСМ/МИМ claim (strong / implied F4+) с §3.7 explicit F2 aspirational для ШСМ/МИМ overlay. Адресовано в §3.

---

## §6 Affect-mode flags

### §6.1 Локации с affect-mode риском

**Flag 1 — «универсальный язык» в §0 TL;DR без scope delimiter**

```«FPF (Foundation Patterns Framework Анатолия Левенчука) — универсальный язык описания методов, бизнесов, вариантов кооперации, самостоятельной работы и философии.»```

«Универсальный» = strong superlative. В §1 source anchor для этого claim: audio_673 использует «универсальный язык человечества блять в какой-то степени» — ключевое «в какой-то степени» присутствует в оригинале. TL;DR убрал qualifier.

Поппер P1: что было бы опровержением тезиса «FPF = универсальный язык»? Если Levenchuk сам скажет, что FPF применим только к engineering systems management — claim опровергнут. Но без falsifier clause claim = affect-mode overclaim.

**Рекомендация:** TL;DR: «FPF — единый язык описания» (убрать «универсальный») OR добавить «в контексте Jetix как [src: audio_673 «в какой-то степени»]». Это repair Ruslan's hedge, не изменение стратегического тезиса.

**Flag 2 — «FPF работает одинаково хорошо» (§3.1)**

Уже адресован в R6 Gap 1. Affect-mode: «одинаково хорошо» = performance claim without evidence. Duplicate fix из §4.2.

**Flag 3 — «Jetix = vehicle» аналогия (§3.3)**

Риск умеренный (см. §2.2 Зона 2). Не affect-mode per se, но persuasive framing без epistemic grounding. Низкий приоритет для правки.

### §6.2 Что не является affect-mode (чистое)

- §3.7 честный статус: F2 vapor list явный и конкретный. Не overclaim.
- §2.6 B.5.1 Exploration: «Это не слабость — это честный статус» — нормальная epistemic qualification.
- §0 EP-2 disclosure: «0 forkers подтверждено» — честно.

---

## §7 Anticipated dissents validation

Документ предантиципировал три dissent'а в §8. Проверяем каждый:

### Dissent 1 — U.WorkPlan строгость (§2.3)

**Предантиципирован:** «Fork guide v0 может не соответствовать строгому A.15.2 требованию temporal windows».

**Critic verdict: CONFIRMED.** §2.3 сам отмечает: `forker_onboarding_window: undefined in v0 (LIVE-FLAG)`. Это честно. Но в §4 FPF formal block U.WorkPlan присвоен с `temporal_windows: forker_onboarding_window: undefined` — это означает что WorkPlan без temporal windows = proto-WorkPlan aspirational, не full A.15.2.

**Рекомендация:** В §2.3 и §4: добавить explicit qualifier «proto-WorkPlan (A.15.2-candidate; pending v1.0 with defined temporal windows)». Текущий wording уже честный, но qualifier делает EP-2 грань явной.

Dissent с тройкой (F, ClaimScope, R):
```
F: F3
ClaimScope:
  holds_when: "Fork guide получает явные temporal windows + named performers в v1.0"
  not_valid_when: "v0 = 6-step outline без дат — A.15.2 strict applicability not met"
R:
  refuted_if: "U.WorkPlan A.15.2 spec допускает workplans без temporal windows"
  accepted_if: "v1.0 Fork guide содержит ≥1 temporal window + performer assignment"
```

### Dissent 2 — ШСМ/МИМ FPF-typing gap (§3.3)

**Предантиципирован:** «§3.3 ШСМ/МИМ overlay описан narratively, не FPF-typed».

**Critic verdict: CONFIRMED.** §3.3 описывает ШСМ/МИМ как «онтологический субстрат», но не присваивает FPF primitive. OQ-D02-2 в §7 документа это отмечает: «оставить как reference или формализовать как O-22?».

Дополнительно critic фиксирует: ШСМ = Levenchuk IP, не Jetix IP. Если Doc 02 будет читать Levenchuk (L1 audience), narrative framing «FPF = substrate на котором Jetix строится» без explicit attribution chain к ШСМ как Levenchuk's primary work может создать IP boundary ambiguity. «Wheel/vehicle» аналогия в этом контексте — тонкий риск: она implies что FPF = tool, Jetix = user. Для Levenchuk-as-reader, правильная framing скорее: Jetix = один из instances того что ШСМ/FPF описывает.

Dissent с тройкой:
```
F: F2
ClaimScope:
  holds_when: "ШСМ/МИМ overlay formalized as O-22 с explicit FPF primitive assignment"
  not_valid_when: "ШСМ/МИМ остаётся narrative reference без FPF-typing"
R:
  refuted_if: "Levenchuk ack'нет что ШСМ/МИМ = FPF substrate в смысле ontological foundation (не только source)"
  accepted_if: "O-22 создан с Levenchuk ack"
```

### Dissent 3 — §3.6 EP-2 use vs mention (mutual-instrumentation)

**Предантиципирован:** «является ли §3.6 use или mention?»

**Critic verdict: CONFIRMED — это use, не mention.** Механика трёх FPF примитивов полностью развёрнута в §3.6, это USE-level claim. PRIMARY HOME = doc 03 (text_004). Требуется правка.

Dissent с тройкой:
```
F: F3
ClaimScope:
  holds_when: "§3.6 содержит только cross-link mention без operational FPF-mechanic description"
  not_valid_when: "§3.6 содержит U.Role/U.Capability/U.Commitment mechanic (current state)"
R:
  refuted_if: "EP-2 discipline explicitly допускает mechanic preview in cross-ref sections"
  accepted_if: "§3.6 редуцирован до mention с explicit [EP-2: mention only] tag"
```

---

## §8 Новые dissents (не предантиципированные)

### Новый Dissent D-DOC02-D — «FPF прошёл проверку» = ungrounded validation claim

Claim в §3.3: «FPF прошёл проверку временем и применением в разных областях».

Это epistemic claim о FPF's external track record. В документе нет источника. Per Lakatos (P3): claim находится в «protective belt» тезиса «FPF = надёжный субстрат». Если belt не sourced, core тезис уязвим.

Claim-scope: этот dissent касается только epistemic status claim'а, не стратегического решения строить на FPF (то Ruslan's R1 territory).

```yaml
dissent:
  position: "«FPF прошёл проверку временем» — validation claim без первичного source"
  triggered_by: AP-PHIL-1 (claim without falsifier) + R6 gap
  F: F2
  ClaimScope:
    holds_when: "Named external adoption instances cited (организации / публикации / ШСМ students применяющих FPF)"
    not_valid_when: "Source = только Phase 0 Jetix-internal characterisation"
  R:
    refuted_if: "FPF adoption = zero confirmed external instances per public record"
    accepted_if: "≥1 named external FPF application with published record surfaced"
  recommended_action: "Либо remove claim, либо source на public ШСМ materials, либо qualifier: «per Ruslan's assessment of FPF corpus»"
```

### Новый Dissent D-DOC02-E — audio_673 «универсальный» hedge removed from TL;DR

audio_673 verbatim: «универсальный язык человечества блять **в какой-то степени**». Qualifier «в какой-то степени» = epistemic hedge из первоисточника. TL;DR §0 убирает этот hedge, делая claim stronger than source.

Это не R1 violation (Ruslan сказал «в какой-то степени»), но это fidelity-to-source issue: документ представляет более сильную версию claim, чем оригинальная dictation.

```yaml
dissent:
  position: "TL;DR «универсальный язык» stronger than source audio_673 «в какой-то степени»"
  triggered_by: AP-PHIL-1 (affect-mode) + R6 source-fidelity
  F: F3
  ClaimScope:
    holds_when: "TL;DR воспроизводит qualifier из audio_673"
    not_valid_when: "TL;DR упрощает до bare superlative"
  R:
    refuted_if: "Ruslan отдельно подтвердит bare superlative «универсальный» без qualifier"
    accepted_if: "TL;DR добавляет «в значительной степени» или «по замыслу» qualifier"
  recommended_action: "TL;DR: «FPF — язык описания методов, бизнесов, кооперации» (убрать «универсальный» из TL;DR; сохранить в §1 verbatim где он quotation)"
```

### Новый Dissent D-DOC02-F — §3.6 lacks falsifier (Popper P1)

Claim в §3.6: «двое людей с разными background-ами могут инструментализировать друг друга точно — без месяцев согласования».

Что было бы опровержением? Документ не называет. «Точно» = precision claim. «Без месяцев» = time claim. Оба без measurement criterion.

Поскольку §3.6 будет перемещён в doc 03 (per dissent 3 fix), этот dissent адресован инструкцией к doc 03: при разработке full thesis, добавить falsifier к основному mutual-instrumentation claim.

```yaml
dissent:
  position: "mutual-instrumentation «точно» = precision claim без falsifier"
  triggered_by: AP-PHIL-1
  F: F2
  ClaimScope:
    holds_when: "Named measurement of coordination time documented in trial instance"
    not_valid_when: "Claim aspirational (0 confirmed mutual-instrumentation instances)"
  R:
    refuted_if: "FPF-described role cooperation takes longer than non-FPF baseline in ≥1 documented case"
    accepted_if: "≥1 documented case: FPF-role cooperation faster than non-FPF baseline"
  route: "Для doc 03 (text_004 PRIMARY HOME) — передать engineering-integrator + phil-critic doc 03 pass"
```

---

## §9 Net recommendation + required edits

### §9.1 Обязательные правки (must-fix до brigadier canonical promotion)

**Edit A — §3.6 EP-2 compliance (CRITICAL)**

Текущий §3.6 содержит USE-level mechanics для text_004 material. Reduce to mention:

```
Одно из ключевых применений FPF-методологии в Jetix — **mutual instrumentation**: 
когда участники с разными ролями становятся инструментами усиления друг друга.

[EP-2: mention only. Механика U.Role / U.Capability / U.Commitment — PRIMARY HOME doc 03,
где text_004 = первоисточник. → doc 03 для полного тезиса.]

[src: vision/jetix-fpf-describe-PLAN-2026-05-17.md §5 text_004 distribution map «02 cross-ref»]
```

**Edit B — §0 TL;DR ШСМ/МИМ qualifier**

Добавить: «ШСМ/МИМ — планируемый онтологический субстрат (F2 aspirational; формализация = OQ-D02-2; §3.7)».

**Edit C — §3.2 / §3.1 «универсальный» и «одинаково хорошо» repair**

- §0 TL;DR: убрать bare «универсальный язык» → «единый язык» (без superlative). Verbatim cite из audio_673 с hedge сохранить в §1.
- §3.1: «FPF работает одинаково хорошо» → «FPF применим для описания». Добавить: `[non-falsifiable in current form; pending §2.1 falsifier per AP-PHIL-1]`.

**Edit D — §3.3 провенанс ШСМ/МИМ «20+ лет» и «проверка временем»**

- «20+ лет» добавить qualifier: «per Jetix Phase 0 characterisation».
- «FPF прошёл проверку временем и применением» — либо source на public ШСМ materials, либо replace: «FPF разрабатывается Левенчуком как формальная спецификация. Jetix строится поверх этого фундамента.» (Claim фактуальный и defensible без track-record assertion.)

### §9.2 Рекомендованные правки (should-fix)

**Edit E — §2.3 U.WorkPlan qualifier**

Добавить: «proto-WorkPlan (A.15.2-candidate; pending v1.0 formalisation с defined temporal windows)».

**Edit F — §3.4 корпоративные системы comparison**

Добавить 1-2 named examples (SAP certification lock-in, proprietary LMS systems) или downgrade «большинство» → «многие».

### §9.3 Acceptability без правок

Если правки A + C + D выполнены, документ готов к brigadier integration с оставшимися dissents preserved (D-DOC02-D, D-DOC02-E как resolved-in-text; D-DOC02-F route to doc 03 pass).

---

## §10 Conformance checklist (§3.1 из Core memory)

| Check | Result | Evidence |
|---|---|---|
| 1. Falsifier-named (Popper) | PARTIAL FAIL | «FPF работает одинаково хорошо», mutual-instrumentation claim, «проверка временем» — все без falsifier |
| 2. Paradigm-named on shift (Kuhn) | PASS | Нет paradigm-shift claims без explicit framing |
| 3. Mental-model + applicable-conditions | PASS | Никаких bare mental-model invocations без context |
| 4. Method declares anti-scope | PASS | §3.4 описывает что НЕ является Fork-and-Leave; §9 anti-scope в смысле «что не в этом doc» |
| 5. Dichotomy-of-control for meta-decisions | N/A | Нет meta-decision-note в этом artefact type |
| 6. Fallacy-named when named | PASS | Нет unnamed fallacy references |
| 7. Meta-claim grounded in object-level | PARTIAL FAIL | «FPF прошёл проверку» = meta-claim без object-level instance (named application) |

---

## §11 Acceptance predicate (Hamel-binary)

```
acceptance_predicate:
  "Все N claims в §2 и §3 Doc 02 карают явный [src:...] reference;
  §3.6 содержит только mention-level cross-ref к doc 03 с [EP-2: mention only] tag;
  TL;DR §0 не содержит bare superlative «универсальный» без qualifier из audio_673;
  §3.3 ШСМ/МИМ validation claim sourced на public ШСМ materials OR qualified as «per Phase 0 characterisation»;
  все четыре предикаты = TRUE одновременно."
```

---

## §12 R1 reaffirmation + dissents preserved

**R1:** это critic review, не strategic authorship. Все позиции в этом документе = epistemic critique. Стратегические решения (делать ли правки, как именно) = R1 Ruslan authority.

**Dissents preserved (AP-6):**

| ID | Position | F | ClaimScope | R |
|---|---|---|---|---|
| D-DOC02-1 (confirmed) | U.WorkPlan A.15.2 strict applicability: v0 = proto-WorkPlan | F3 | holds when temporal windows defined | refuted if A.15.2 допускает undated workplans |
| D-DOC02-2 (confirmed) | ШСМ/МИМ FPF-typing gap; IP boundary framing risk | F2 | holds when O-22 created | refuted if Levenchuk ack'нет substrate claim |
| D-DOC02-3 (confirmed) | §3.6 = USE not MENTION (EP-2 fail) | F3 | holds when §3.6 reduced to mention | refuted if EP-2 discipline допускает mechanic preview |
| D-DOC02-D (new) | «FPF проверка временем» = ungrounded validation | F2 | holds when named external instances cited | refuted if FPF = zero external adoption |
| D-DOC02-E (new) | audio_673 «в какой-то степени» hedge removed in TL;DR | F3 | holds when TL;DR restores qualifier | refuted if Ruslan confirms bare superlative |
| D-DOC02-F (new, route doc 03) | mutual-instrumentation «точно» lacks falsifier | F2 | holds when measurement criterion named | refuted if ≥1 documented faster coordination case |

---

*Review completed by philosophy-expert × critic. Conformance checks 7/7 evaluated; 2 partial fails addressed in required edits A-D. AP-PHIL-1 triggered on 3 claims (§3.1, §3.3, §3.6). AP-PHIL-2 not triggered. AP-PHIL-3 not triggered. AP-mental-model-out-of-context not triggered. Pending: eng-critic pass → brigadier integration.*
