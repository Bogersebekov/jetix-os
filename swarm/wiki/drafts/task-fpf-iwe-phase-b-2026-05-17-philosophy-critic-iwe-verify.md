---
title: "IWE definition fidelity audit — does published IWE match C5 claim 'IWE = production-applied FPF'?"
type: critic-review
mode: critic
expert: philosophy-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
artefact_under_consideration: "IWE public corpus (README.en.md, ONTOLOGY.md, CLAUDE.md, docs/principles-vs-skills.md) vs C5 claim in levenchuk-tg-2026-05-17.md"
date: 2026-05-17
F: F4
G: "epistemic-audit of IWE public artefacts; claim scope: Phase A read-only corpus; does not include paid IWE platform interaction (blocker B2)"
R: "refuted_if: any direct FPF-Spec.md passage cited verbatim in public IWE artefacts that contradicts findings below; accepted_if: pattern holds across all 4 public artefacts after Phase B empirical IWE session"
prose_authored_by: claude (scribe, R1 posture)
sources:
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/README.en.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ONTOLOGY.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/docs/principles-vs-skills.md
  - raw/external/ailev-FPF/FPF-Spec.md
  - raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md
  - reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md
  - inbox/levenchuk-tg-2026-05-17.md
---

# IWE Definition Fidelity Audit — philosophy-expert × critic

> **Constitutional posture.** R1 scribe. This artefact surfaces observable facts from the
> public IWE corpus and evaluates the falsifiability of specific claims. It does NOT evaluate
> whether IWE is good or bad, and does NOT author positioning for Tseren or Левенчук.
> All FPF references are to `raw/external/ailev-FPF/FPF-Spec.md` (canonical, c86eabd 2026-05-16).

---

## §1 Conformance Checklist (≥5 binary checks against artefact-under-review)

The claim under audit is C5 from `inbox/levenchuk-tg-2026-05-17.md`:
> «У Церена IWE, там примерно всё так же устроено. Но внутри там интеллект опирается на тот же FPF — и понятно, за счёт чего его IWE умнее конкурентов.»

For each check: the predicate is applied to the PUBLIC IWE corpus (the 4 artefacts named
in the sources list above). The check does NOT have access to the paid IWE platform internals.

### Check 1 — FPF-named-in-public-definition (Popper: is the claim traceable to observable artefacts?)

**Predicate:** Does the public IWE definition (README.en.md, the primary public-facing surface)
explicitly name FPF as the epistemic basis?

**Evidence from artefact:**
README.en.md contains zero occurrences of the string "FPF", "First Principles Framework",
"первых принципов", or "Левенчук". The word "intelligence" appears only in the product name
"Intellectual Work Environment" and the claim "amplifies your thinking, not replaces it".

**Result: FAIL**

The public definition does not name FPF. The claim that "inside there, the intelligence rests
on FPF" (C5) is Левенчуков's characterisation, not a claim Tseren makes publicly in README.en.md.

**AP triggered:** AP-PHIL-1 candidate — the C5 claim as-stated is not falsifiable via public
artefacts because FPF is not referenced in the primary public surface. The "FPF grounding" is
either (a) present only in the paid-platform layer (CLAUDE.md memory/ FPF-reference.md, which
is accessible but not public-facing), or (b) a meta-claim by Левенчук about architecture
he has reviewed, not a published claim by Tseren.

---

### Check 2 — FPF-present-in-operational-layer (Kuhn: does the operational substrate carry FPF?)

**Predicate:** Does the operational CLAUDE.md (the agent's working instructions, not the
marketing README) reference FPF as an upstream dependency?

**Evidence from artefact:**
CLAUDE.md §1 architecture table explicitly lists:

> | **Base** (Принципы + Форматы) | ZP, FPF, SPF, FMT-* | Да (платформа) |

And the Fallback Chain is stated as:

> **Fallback Chain:** DS → Pack → Base (SPF → FPF → ZP)

And Pack Creation Gate states:

> «Если `FPF/` или `SPF/` отсутствуют в рабочей директории — `/pack-new` клонирует их автоматически.»

ONTOLOGY.md §4 abbreviations table lists:

> | FPF | Фреймворк первых принципов | First Principles Framework | FPF |

**Result: PASS**

FPF is present and structurally declared as the upstream Base layer in the operational
artefacts (CLAUDE.md and ONTOLOGY.md). The agent is instructed to fall back to FPF when
DS and Pack do not resolve a question.

**Distinction:** FPF is in the operational layer (CLAUDE.md) but NOT in the marketing layer
(README.en.md). These are two different surfaces for two different audiences.

---

### Check 3 — U.Episteme-named-vs-used (Munger: which primitive is actually used vs named?)

**Predicate:** Does IWE explicitly name and use the FPF primitive `U.Episteme`, or does it
use derived constructs without naming the FPF archetype?

**Evidence from artefact:**
- README.en.md: zero occurrences of "U.Episteme", "EpistemeSlotGraph", "DescribedEntity",
  "GroundingHolon", "ViewpointSlot", "ClaimGraph".
- ONTOLOGY.md: zero occurrences of "U.Episteme". FPF is listed as upstream in the
  abbreviations table (row: FPF | Фреймворк первых принципов | First Principles Framework | FPF).
  IWE's own exocortex concept references "DP.EXOCORTEX.001" and "DP.CONCEPT.001" (Digital
  Platform Pack identifiers), not FPF's U.Episteme directly.
- CLAUDE.md: references `memory/fpf-reference.md` as the lookup file for "FPF/SOTA/Роли",
  and lists FPF in the Base tier. Does not name U.Episteme primitive directly.
- docs/principles-vs-skills.md: names FPF explicitly at Level 1 of the four-level hierarchy
  (ZP → FPF → Pack → DS) with description "Точный язык: Role ≠ Method ≠ Work ≠ Capability".
  Does not name U.Episteme.

**Result: FAIL (partial pass)**

IWE USES FPF's role/method/work/capability distinctions (the derived constructs that FPF
encodes via U.Episteme + U.System archetypes), but does NOT NAME `U.Episteme` as the archetype
being used. The derived constructs in active use are: Role ≠ Method ≠ Work ≠ Capability
(Level 1 FPF); Fallback Chain (structural dependency); ArchGate (DP.M.005 = derived from FPF
method-signature discipline).

This is a "used but not named" pattern: the FPF architecture is operative in the system, but
the U.Episteme primitive specifically is not surfaced in the public documentation.

**AP triggered:** AP-PHIL-8 candidate (mental-model-applied-out-of-context prevention):
the C5 claim uses the phrase "интеллект опирается на FPF" as if it implies U.Episteme-level
rigour. The public artefacts show FPF is present as a structural dependency (Base layer) but
the specific epistemic-slot discipline (U.EpistemeSlotGraph with DescribedEntity +
GroundingHolon + ClaimGraph + Viewpoint) is not demonstrably enforced in the public IWE
artefacts.

---

### Check 4 — intelligence-amplification-claim-falsifiable (Popper)

**Predicate:** Is the claim "exoskeleton, not prosthesis — IWE amplifies your thinking, not
replaces it. After each session you become more competent" falsifiable?

**Evidence from artefact:**
README.en.md states verbatim:
> «Key principle: exoskeleton, not prosthesis. IWE amplifies your thinking, not replaces it.
> After each session you become more competent, not just get a result.»

docs/principles-vs-skills.md elaborates:
> «При технологическом сдвиге (ИИ замещает функции, появляются новые профессии) агент с
> принципами создаёт новые роли. Агент только с навыками ищет курсы переодготовки.»

**Falsifier analysis:**

The claim "after each session you become more competent" has the following structure:
- It is a comparative claim (more competent than before the session)
- It requires a measurement of competence at t0 and t1
- The measurement instrument is not specified in the public artefacts
- The comparison condition (without IWE) is not specified

docs/distinctions.md offers one near-falsifier:
> «Экзоскелет ≠ Автопилот (DP.D.046). Усиление мышления / LLM автономно. Тест: можешь
> объяснить без "ИИ подсказал"?»

This informal test ("can you explain it without saying 'AI suggested it'?") is a distinguishing
criterion but is not a controlled falsifiability specification. It does not specify:
- What count as pre/post competence measurements
- What comparison group (vanilla AI users) is used
- What timeframe constitutes "after each session" vs longitudinal

**Result: FAIL**

The intelligence-amplification claim is NOT falsifiable as stated in the public artefacts.
No acceptance test, no measurement protocol, no comparison condition, no timeframe are
specified. The informal test in distinctions.md approaches a falsifier but falls short of
a Popper-grade specification.

**AP triggered:** AP-PHIL-1 (claim-without-falsifiability). The claim is structurally a
design preference ("we believe IWE amplifies"), not a scientific claim. Per Hume's is/ought:
this is a prescriptive claim about what users will experience, not a falsifiable descriptive
claim about measured outcomes.

---

### Check 5 — paradigm-named-on-shift (Kuhn: does IWE name its prior paradigm and anomaly?)

**Predicate:** IWE positions itself as a shift from "AI gives you answers" to "AI amplifies
your thinking". Does it name the prior paradigm + the anomaly that broke it?

**Evidence from artefact:**
README.en.md "The Problem" section names five failure modes of the prior paradigm:
1. Context is lost
2. Knowledge stays in your head
3. AI replaces thinking instead of amplifying it
4. No system
5. Time slips away

docs/principles-vs-skills.md names the prior paradigm implicitly:
> «Навыки — автоматизированная последовательность операций. Он отвечает на вопрос "как
> выполнить ЭТУ процедуру". Но вопрос "КАКУЮ процедуру выбрать" — это знание, порождённое
> принципами.»

The prior paradigm is "skills-first" (vanilla AI use = just get the output). The successor
paradigm is "principles-first" (ZP → FPF → Pack → DS generative hierarchy).

**Result: PARTIAL PASS**

The prior paradigm ("AI-as-answer-machine / skills-first") is implicitly named and the
anomaly ("competence doesn't grow without principles") is articulated. However:
- The prior_paradigm is not named explicitly with a field or label
- The Kuhnian shift is not formally declared with "prior_paradigm:" + "anomaly:" structure
  required by AP-PHIL-2 conformance check
- The principles-vs-skills.md document is closer to the paradigm naming but is in the
  docs/ subtree, not the primary README

**AP triggered:** AP-PHIL-2 (paradigm-conflation) — partial. The shift is present but the
paradigm naming is informal, not formal. A reader of only README.en.md would not receive the
full prior/successor paradigm articulation.

---

### Check 6 — method-declares-anti-scope (via-negativa, Stoic)

**Predicate:** Does IWE's public definition name what IWE is NOT trying to do?

**Evidence from artefact:**
README.en.md FAQ contains one relevant entry:
> «Q: How is IWE different from Obsidian / Notion / Logseq?
> A: Obsidian is a note storage. IWE is a work environment with protocols, AI agents, and
> knowledge formalization. You can use Obsidian inside IWE for notes, but IWE provides
> structure, planning, and competence accumulation.»

docs/principles-vs-skills.md implicitly names what IWE is NOT:
> «Пользователь IWE не просто получает инструменты (Level 3). Он получает методологию
> (Level 0-1) и доменное знание (Level 2)...»

CLAUDE.md §2 blocking rules implicitly name limits:
> «WP Gate: ЛЮБОЕ задание → протокол Открытия → ДО начала работы.»
> «Hooks/Scripts Bypass Gate (БЛОКИРУЮЩЕЕ): Без явного разрешения...»

**Result: PARTIAL PASS**

The anti-scope for tool comparison (not Obsidian/Notion/Logseq) is present. An implicit
anti-scope for "not replacing thinking" is present. However the anti-scope is fragmented
across multiple documents and does not constitute a formal `anti_scope:` block with ≥2 items
in the primary definition artefact. The primary README does not carry a structured
anti-scope section.

---

### Check 7 — dichotomy-of-control identified (Stoic, for the intelligence-amplification meta-claim)

**Predicate:** Does IWE name which variables in the intelligence-amplification claim are
in the user's control vs not?

**Evidence from artefact:**
The closest approach is in docs/distinctions.md:
> «Экзоскелет ≠ Автопилот (DP.D.046). Усиление мышления / LLM автономно. Тест: можешь
> объяснить без "ИИ подсказал"?»

And the OWC protocol design (CLAUDE.md §2) places the deliberate work practice in the
user's control: Open → Work → Close is a user-executed ritual, not an AI-executed ritual.
This implicitly encodes the Stoic dichotomy: the protocol compliance is in the user's control;
the LLM's response quality is not.

**Result: PARTIAL PASS**

The dichotomy is structurally encoded in the OWC ritual design (user controls the ritual;
AI outputs are not controlled). The Stoic framing is not explicit but the design implies it.
No formal `in_control: [...] / not_in_control: [...]` declaration exists.

---

## §2 Acceptance Predicate (Hamel-binary — for the C5 claim itself)

```
acceptance_predicate:
  "C5 claim 'IWE внутри опирается на тот же FPF' is VERIFIED if:
   (1) the public IWE artefacts contain ≥1 direct structural dependency declaration on FPF
       (not merely a naming mention), AND
   (2) ≥1 FPF pattern (named by FPF identifier: A.x, B.x, C.x, E.x, etc.) is directly
       cited in the IWE operational layer as the grounding for a specific IWE behaviour, AND
   (3) the 'умнее конкурентов' comparative is supported by ≥1 empirical comparison
       (controlled experiment, case study, or benchmark) in any public IWE artefact.
   CURRENT STATUS: (1) PASS — CLAUDE.md declares FPF as Base tier with Fallback Chain.
                   (2) FAIL — no FPF pattern identifier (A.x etc.) is cited in public artefacts.
                   (3) FAIL — no empirical comparison artefact found in public corpus.
   OVERALL: C5 is PARTIALLY VERIFIED (structural dependency is real; superiority claim is unverified)."
```

The C5 claim is a composite claim. Breaking it down:
- Sub-claim C5a: "IWE's intelligence rests on FPF" — STRUCTURALLY SUPPORTED (Base tier
  dependency declared in CLAUDE.md), NOT DEMONSTRATED at the FPF-pattern level.
- Sub-claim C5b: "it is clear why IWE is smarter than competitors" — NOT SUPPORTED by
  public evidence. No competitor comparison, no measurement, no benchmark exists in the
  public IWE corpus.

C5 as a whole is a positioning statement (F2 grade by FPF F-G-R), not a verified empirical
claim (which would require F5+ with supporting evidence and comparison data).

---

## §3 Alternatives (≥2 + status quo, each with kill-condition)

### Alternative A — C5 as Левенчук's insider architectural claim (not a public-facing guarantee)

Interpretation: Левенчук has reviewed IWE (or has insider knowledge of Tseren's architecture
since Tseren studies at ШСМ and applies FPF through the school's curriculum). C5 is
Левенчук's characterisation based on his knowledge of the underlying architecture —
not a claim that IWE publicly makes about itself.

Kill-condition: This interpretation fails if Tseren explicitly disavows FPF as the basis
of IWE, or if the paid IWE platform's memory/ files contain no FPF-Spec reference.

Status: Supported by structural evidence (CLAUDE.md FPF Base tier, SPF hierarchy). The
public artefacts do not claim "IWE = FPF-applied" in marketing language, but the
operational layer does depend on FPF as a Base.

### Alternative B — C5 as over-claim (FPF is present superficially but IWE is operationally a memory/automation tool)

Interpretation: FPF is named in the Base tier of CLAUDE.md as a fallback, but the actual
everyday operation of IWE (OWC protocol + Pack + ArchGate + Strategist) is a structured
workflow environment — consistent with Левенчук's characterisation of Jetix as
"память + автоматизация". The FPF grounding may be present as architecture-in-principle but
not as active runtime epistemic discipline.

Kill-condition: This interpretation fails if Phase B empirical IWE sessions reveal that
IWE's agent actively invokes FPF patterns (citing A.x, B.x identifiers, applying role≠method
distinctions, enforcing bounded contexts) in routine guidance rather than falling back to
FPF only as a last resort.

Status: Currently cannot be falsified from public artefacts alone. The operational distinction
"FPF as active discipline vs FPF as fallback-only" requires live IWE interaction (blocked
by B2).

### Alternative C — status quo (C5 is accepted at face value, no further verification needed)

Interpretation: Левенчук said it; he is the FPF author; his testimony about IWE's FPF
grounding is authoritative. No audit needed.

Kill-condition: This interpretation fails under Popper's basic constraint — authority is
not a falsifier. Левенчук's testimony is F8 for the claim "Левенчук believes IWE uses FPF",
but it is not evidence for the claim "FPF is actively operative in IWE's epistemic discipline".
The authority argument is valid only if we treat C5 as a claim about architecture-of-record
(which Левенчук could reasonably know), not as a claim about operational epistemic discipline
(which requires behavioural evidence).

Status: Acceptable as a starting hypothesis; insufficient as a final verdict.

---

## §4 Anti-Scope

- This audit is NOT evaluating whether IWE is a good product or better than Jetix.
- This audit is NOT arbitrating whether Jetix should adopt FPF — that is an instrumental
  decision (investor-expert + Ruslan HITL per FPF L1003-1006 wall).
- This audit is NOT running an engineering analysis of IWE's code architecture — that is
  engineering-expert territory.
- This audit is NOT producing a report for Tseren or ШСМ — it is an internal epistemic
  instrument for Jetix's own understanding of FPF/IWE relationship.
- This audit does NOT have access to IWE's paid platform (blocker B2 per
  `reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md §4`). Conclusions
  about the paid layer are provisional.

---

## §5 F-G-R Audit Table

| IWE claim | Formality (F) | ClaimScope (G) | Reliability (R) | Over-claimed? |
|---|---|---|---|---|
| "IWE = intellectual work environment, OS for thinking" (README marketing claim) | F2 (informal, brand framing) | G: prospective users; not_valid_when: rigorous systems theory evaluation | R: unfalsified — no measurement | Yes — R is presented as high; actual grade is F2 |
| "exoskeleton, not prosthesis — after each session you become more competent" (README) | F2 (design intent claim) | G: any user following OWC protocol; not_valid_when: user does not follow OWC | R: no longitudinal study cited; informal self-report pattern | Yes — claim implies empirical regularity (F5+) but no evidence given |
| "FPF is the Base tier" (CLAUDE.md operational layer) | F5 (structural declaration in operational artefact) | G: within the IWE template system; not_valid_when: user overwrites CLAUDE.md §1 | R: directly falsifiable — can be checked by reading CLAUDE.md §1 | No — F5 is appropriate for a structural dependency declaration |
| "IWE = ZP → FPF → Pack → DS hierarchy" (principles-vs-skills.md) | F4 (design rationale document) | G: architectural rationale; not_valid_when: actual agent behaviour diverges from hierarchy | R: structurally coherent; not empirically validated at operational level | Slight — F4 is appropriate for design rationale; it would be over-claimed if presented as empirical operational fact |
| "Pack is single source-of-truth for domain knowledge" (README + ONTOLOGY) | F4 (architectural design claim) | G: within a single IWE deployment; not_valid_when: user has multiple IWE deployments with divergent Packs | R: structurally coherent for single-user deployment | No — F4 appropriate |
| "ArchGate evaluates across 7 characteristics (ЭМОГССБ) instead of 'I think it's fine'" (README) | F4 (method claim) | G: when ArchGate is invoked; not_valid_when: user bypasses ArchGate | R: behavioural pattern in CLAUDE.md §5; falsifiable by observing whether ArchGate is actually invoked | No — F4 appropriate |
| "OWC prevents context loss" (README) | F3 (protocol claim, no outcome data) | G: users who run OWC; not_valid_when: LLM context window resets or user skips OWC | R: no outcome data; plausible mechanism | Slight — implies high reliability; no evidence |

**Summary:** Marketing-layer claims (README) are F2 with over-implied reliability. Operational
layer claims (CLAUDE.md) are F4-F5 and appropriately graded. C5 as a whole is F2 
(positioning statement by Левенчук) presented in context as if F5+.

---

## §6 Hot-Spot Register (predicted Левенчук objections to the future 02-iwe-deep-v2.md)

The following are predicted hot spots where Левенчук would flag "вы не то поняли":

### Hot Spot 1 — Confusing "FPF as Base dependency" with "FPF as operative epistemic discipline"

The Phase A distillation (`02-u-episteme-and-iwe.md §3.1`) states:
> «IWE's reasoning is constrained by FPF's bounded contexts, role/method-work distinction,
> F-G-R assurance, abductive loop, multi-view publication.»

This inference is correct in architectural intent but goes beyond what the public artefacts
demonstrate. The public artefacts show FPF is in the Fallback Chain (Base tier). They do NOT
show that F-G-R tags, abductive loop, or multi-view publication are enforced at runtime.

Левенчук would likely flag: "You inferred operational FPF discipline from architectural
dependency. These are different. FPF as Base means 'fall back to FPF when stuck'; it does not
mean every Pack entry carries F-G-R + Viewpoint + GroundingHolon."

**Epistemic status of the hot spot:** Valid objection. The distillation over-infers from
structural dependency to operational discipline.

### Hot Spot 2 — Treating C5 as a verifiable claim about IWE when it is Левенчук's architectural testimony

The 02-u-episteme-and-iwe.md treats C5 ("IWE опирается на FPF — и понятно, за счёт чего его
IWE умнее конкурентов") as if it is a claim that can be verified from IWE's public artefacts.
It cannot, because:
- "умнее конкурентов" is a comparative requiring a comparison (not present in public artefacts)
- "за счёт чего понятно" is Левенчук's shorthand meaning "I can see the architectural
  mechanism" — not Tseren's claim

Левенчук would likely flag: "I said it is clear *to me* why IWE is smarter, based on the
FPF grounding I can see. I did not say Tseren publishes a proof of superiority."

**Epistemic status:** Valid objection. The C5 claim is Левенчук's first-person architectural
reading, not a third-person verifiable fact.

### Hot Spot 3 — Mapping IWE terms to FPF archetypes without confirming the mappings

The distillation `02-u-episteme-and-iwe.md §3.1` maps:
- IWE recommendation → U.EpistemeView
- IWE guidance → "rendered surface (Plain/Tech/Interop/Assurance)"

These mappings are inferences. The public IWE artefacts do NOT use the FPF archetypes
U.EpistemeView, U.View, PublicationScope, or the MVPK faces (Plain/Tech/Interop/Assurance).
The IWE public artefacts reference FPF terminologically (Role ≠ Method ≠ Work ≠ Capability)
but do not map their operational constructs to FPF's specific type identifiers.

Левенчук would likely flag: "You are saying IWE implements multi-view publication per FPF.
Show me where IWE declares a Viewpoint + DescribedEntity + GroundingHolon for any of its
outputs. If it doesn't, it's not the same as the FPF mechanism."

**Epistemic status:** Valid objection. The mapping is architecturally plausible but not
demonstrated in public artefacts.

### Hot Spot 4 — Treating "Pack = single source of truth" as equivalent to FPF's ClaimGraph discipline

The public IWE artefacts describe Pack as "single source-of-truth for domain knowledge".
FPF's ClaimGraph (the C-slot in U.EpistemeSlotGraph) is a formal claim-bearing structure
with DescribedEntity, GroundingHolon, and Viewpoint slots. Pack in IWE is a knowledge
domain passport maintained as Markdown/YAML files in a git repository.

These are structurally similar (single-source, provenance-tracking intent) but not
definitionally equivalent. Pack does not enforce U.Episteme slot graph structure.

Левенчук would likely flag: "Pack is a practical knowledge-management pattern. U.Episteme
is a formal holon. Don't conflate them unless you show the episteme slots in Pack entries."

**Epistemic status:** Valid objection. The conflation is a category error if stated as identity.

### Hot Spot 5 — Missing the significance of the ZP (Zero Principles) layer above FPF

The Phase A distillation focuses on FPF as the top of the architecture. But the IWE
principles-vs-skills.md and ONTOLOGY.md consistently show the hierarchy as ZP → FPF → Pack → DS,
where ZP (Zero Principles / transdisciplines) is ABOVE FPF. Левенчук's FPF is explicitly
positioned as Level 1 in this four-level stack, not the top.

The distillation `02-u-episteme-and-iwe.md` does not surface the ZP layer or its significance
for intelligence amplification.

Левенчук would likely flag: "FPF is not the top. ZP is the transdisciplinary layer that
gives FPF its generative power. Your distillation treats FPF as the foundation when it is
actually the second tier. The first tier — transdisciplines — is what makes the system
domain-invariant."

**Epistemic status:** Valid objection. Structurally supported by principles-vs-skills.md.

---

## §7 Dissents Register

Per E-5 protocol — both positions preserved with (F, ClaimScope, R) triples.

### Dissent D1 — Does IWE operationally implement FPF?

**Position A (FPF-operative):**
> IWE has FPF as Base tier in Fallback Chain (CLAUDE.md §1). The agent is instructed to
> fall back to FPF when DS and Pack do not resolve a question. The principles-vs-skills.md
> places FPF at Level 1 of the generative hierarchy. Therefore FPF is operative.

F: F4 (design declaration in operational artefact)
ClaimScope: holds_when the IWE agent actually consults FPF-reference.md when DS/Pack
             don't resolve; not_valid_when the Fallback Chain is never triggered in practice
R: refuted_if: empirical IWE session logs show FPF never cited in agent responses;
   accepted_if: ≥1 session log shows FPF pattern (A.x identifier) cited in guidance

**Position B (FPF-as-background-only):**
> The Fallback Chain places FPF at the far end (DS → Pack → SPF → FPF → ZP). In practice,
> most IWE sessions operate at the DS level (protocols, tools, daily planning). FPF is
> referenced structurally but may be rarely invoked in actual operation. "Опирается на FPF"
> may mean "was designed using FPF" rather than "actively uses FPF at runtime".

F: F3 (inference from operational architecture; not empirically tested)
ClaimScope: holds_when most IWE sessions are at DS level (daily planning, OWC ritual);
             not_valid_when user does deep architectural reasoning that triggers Pack fallback
R: refuted_if: Phase B empirical sessions show FPF cited in >20% of non-trivial guidance
               responses; accepted_if: FPF never appears in 10+ session logs

**Reconciliation:**
Cannot resolve from public artefacts. Route to Phase B empirical sessions (B2 blocker must
be lifted — Ruslan IWE subscription required). Both positions preserved. Integrator should
NOT average; present both to brigadier.

---

### Dissent D2 — Is C5's "умнее конкурентов" claim a fact or a positioning statement?

**Position A (positioning statement):**
> C5 was stated in a single Telegram message by Левенчук. It is a rhetorical comparison
> made to motivate Ruslan to explore FPF. It is not a controlled benchmark claim. F2 grade
> is appropriate. Treating it as a verifiable fact sets up a misleading research program
> (trying to verify a positioning claim as if it were empirical).

F: F2 (informal Telegram message, single source, no comparison methodology)
ClaimScope: holds_when evaluated as rhetorical/motivational framing;
             not_valid_when treated as empirical benchmark claim
R: refuted_if: Левенчук provides controlled comparison data; accepted_if: no such data exists

**Position B (insider architectural testimony):**
> Левенчук is the FPF author. He knows what FPF does to agent reasoning quality. His claim
> that IWE is smarter because of FPF is expert testimony from the person who designed both
> FPF and the curriculum in which Tseren trained. This is F6+ for the sub-claim "FPF
> grounding produces architecturally superior epistemic discipline".

F: F6 (expert testimony from domain author about his own framework's application)
ClaimScope: holds_when restricted to "FPF produces better epistemic discipline than no FPF";
             not_valid_when extended to "IWE product is better than Jetix in practice"
R: refuted_if: Phase B C4 benchmark (levenchuk-tg-2026-05-17.md §C4) shows no difference
               between FPF-loaded AI and vanilla AI on Jetix-domain questions;
   accepted_if: FPF-loaded AI consistently names role-method-work distinctions that vanilla
               AI misses in 5+ test prompts

**Reconciliation:**
Both positions are valid for different sub-claims. C5b ("умнее конкурентов" as product claim)
is F2. C5a ("FPF grounding is architecturally superior to no grounding") is F6+ per Левенчук
testimony, falsifiable via C4 benchmark. These are distinct claims that must not be merged.

---

## §8 Specific AP codes triggered

| AP code | Trigger | Location in artefacts |
|---|---|---|
| AP-PHIL-1 | Intelligence-amplification claim has no explicit falsifier in public artefacts | README.en.md "after each session you become more competent" |
| AP-PHIL-1 | C5b "умнее конкурентов" has no comparison methodology | inbox/levenchuk-tg-2026-05-17.md C5 |
| AP-PHIL-2 | Phase A distillation 02-u-episteme-and-iwe.md conflates FPF-as-base with FPF-as-operative-discipline without naming the prior paradigm explicitly | reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md §3.1 |
| AP-PHIL-8 | C5 invokes FPF as context for "intelligence amplification" without stating which FPF model applies and under which conditions | inbox/levenchuk-tg-2026-05-17.md:28 |
| AP-PHIL-11 | 02-u-episteme-and-iwe.md §3.1 makes meta-claim "IWE's reasoning is constrained by FPF's bounded contexts" without a concrete object-level instance from IWE operation | reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md §3.1 |

---

## §9 Recommended changes for 02-iwe-deep-v2.md (brigadier integration target)

1. **Split C5 into C5a and C5b.** C5a (structural FPF dependency) and C5b (comparative
   intelligence superiority) are distinct claims with different F grades and different
   falsifiers. Merging them under one C5 causes scope confusion.

2. **Replace "IWE's reasoning is constrained by FPF..." with a conditional.** Change the
   strong claim to: "IF IWE's agent actively consults FPF-reference.md when DS/Pack don't
   resolve (which the Fallback Chain permits but does not mandate), THEN FPF's bounded
   contexts / role-method-work discipline operates. This requires Phase B empirical
   verification."

3. **Surface the ZP layer.** Add §ZP-above-FPF noting that the generative hierarchy in
   IWE is ZP → FPF → Pack → DS; FPF is Level 1, not Level 0. ZP (transdisciplines) is
   the domain-invariance layer above FPF.

4. **Add the "used vs named" distinction for U.Episteme.** Explicitly state that U.Episteme
   is the FPF archetype underlying IWE's exocortex concept but is not named in IWE's public
   artefacts. IWE uses derived constructs (Pack, Exocortex-Interface DP.EXOCORTEX.001) that
   are downstream of U.Episteme but do not enforce the full EpistemeSlotGraph structure.

5. **Add the FAIL entry for public surface.** README.en.md contains zero FPF mentions.
   The FPF dependency is an operational/architectural fact, not a publicly marketed
   differentiator. This is architecturally coherent (users don't need to know FPF to use IWE)
   but it means C5a is an insider claim, not a publicly verifiable product claim.

---

*Draft produced by philosophy-expert × critic per task-id: task-fpf-iwe-phase-b-2026-05-17*
*Brigadier integrates this draft into 02-iwe-deep-v2.md after parallel cell returns.*
