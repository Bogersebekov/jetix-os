---
title: "Doc 06 Eng-Critic — Jetix as Clean Internet Layer (FPF-Described)"
date: 2026-05-17
type: eng-critic-output
status: critic-draft
artefact_reviewed: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md
critic_cell: engineering-expert × critic
mode: critic
task_id: task-fpf-describe-jetix-2026-05-17
cycle_id: cyc-fpf-describe-2026-05-17
parent_docs:
  - swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md
  - swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md
F: F4
G: eng-critic-fpf-primitive-correctness-doc06
R: refuted_if_doc03_integrator_is_found_to_contain_§4.1.4_and_§4.1.5_with_formal_BoundedContext_and_Bridges
language: russian (narrative) + english (FPF primitives + critic schema)
---

# Doc 06 Eng-Critic — Jetix as Clean Internet Layer

---

## §1 Conformance Checklist (8 binary checks)

| check_id | result | evidence |
|---|---|---|
| 1-deep-module | N/A | Not a code artefact. Applied to FPF-primitive surface: §2.1 BoundedContext + §2.2 cluster table provide a thin, well-structured interface over the 7-primitive composition. No shallow-module analogue triggered. |
| 2-function-purpose | pass | Every section carries a declared purpose. §2.2 primitive table has per-row role declarations. §4.1 formal section named «Trust-formation без money — формальный механизм». §4.2 named «7-primitive composition». No ambiguous unlabelled sections. |
| 3-test-integrity | N/A | No test cases. Hamel-binary R-conditions declared per claim in §2.3 (6 claims with R-conditions). Equivalent obligation met. |
| 4-premature-abstraction | pass | All 7 primitives are used with concrete Jetix instances (git log = A.10 primitive; Default-Deny table = E.5 analog; 1A/1B view pair = E.17 partial). The «vision-stage» framing correctly tags aspirational uses. No abstraction without grounding. |
| 5-external-dependency | **fail** | A.2.9 SpeechAct row (§2.2) and §4.1 formal section both claim the «institutes» semantic without declaring the context-policy that FPF A.2.9:4.1 normatively requires. Additionally, §2.2 A.2.9 row states «Clan-context policy declared in doc 03 §4.1.4» — that section does not exist in the doc 03 integrator draft. External dependency (FPF A.2.9 normative constraint) declared without failure-mode. AP-ENG-10 trigger. |
| 6-dry | pass | No repeated definitions across sections. §2.2 primitive table and §4.1 formal section use distinct registers (descriptive vs pseudocode). §3 narrative does not duplicate §2.2 rows verbatim — it elaborates them. No substantial duplicates. |
| 7-tool-eval-acceptance | N/A | Not a tool-eval draft. |
| 8-architecture-pattern | pass | §4.2 names the composition as `trust_cluster(...)` — a multi-primitive cluster pattern consistent with the H8 brigadier note («first Jetix insight requiring multi-Part composition»). The pattern is named and justified. §4.3 declares cross-doc bridges with primitive anchors. |

**Overall: 7 of 8 applicable checks pass. Check 5 fails (A.2.9 context-policy: phantom cross-reference to non-existent doc 03 §4.1.4).**

---

## §2 Acceptance Predicate (Hamel-binary)

`swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md` passes Conformance checks 1 (N/A), 2 (pass), 3 (N/A), 4 (pass), 6 (pass), 7 (N/A), 8 (pass) BUT FAILS check 5 (A.2.9 external-dependency: context-policy not declared; cross-reference to doc 03 §4.1.4 is phantom) AND has two additional structural gaps (§4.1 SpeechAct formal expression contradicts §2.2 institutional claim; §4.3 cross-reference to doc 03 §4.1.5 is also phantom).

**Current predicate result: DOES NOT PASS.** Three corrective actions required before promotion to canonical:

1. Declare the trust-infrastructure-context policy for A.2.9 directly in §2.1 Roles/Bridges or a new §2.1.1 — do not rely on doc 03 §4.1.4 which does not exist.
2. Fix §4.1 formal section: replace `U.SpeechAct(A, publish(F_grade, G_scope, R_condition))` with an actType that institutes the trust-relation (not a publication act).
3. Fix or remove cross-references to doc 03 §4.1.4 and §4.1.5 — neither section exists in the current doc 03 integrator draft.

---

## §3 Alternatives (≥2 + status-quo + kill-conditions)

| # | Alternative | Kill condition |
|---|---|---|
| A | Declare the A.2.9 context-policy directly in doc 06 §2.1 BoundedContext (add a §2.1.1 Context-Policy subsection): «Trust-Infrastructure-BoundedContext policy: U.SpeechAct of actType="open-data-publish-under-FGR" institutes {F-G-R-graded reliability claim, verifiable provenance record (A.10 entry), scope declaration (ClaimScope)}». No reliance on doc 03 cross-reference. | Fails if the policy declared here conflicts with the one doc 03 will declare once its RC-2 (BoundedContext section) is implemented — creating a policy split between the two docs |
| B | Declare a minimal stub: «Context-policy pending doc 03 RC-2 (BoundedContext section implementation). Until RC-2 is complete, A.2.9 «institutes» claim is treated as communicative Work occurrence with observable provenance only (A.2.9:4.1 default).» Tag the institutional claim as aspirational (F2, not F4 partial). | Fails if this reduces the doc's persuasive value for the L1 audience before doc 03 RC-2 is implemented — which is imminent (doc 03 critic pass already raised RC-2) |
| C | Status-quo (retain «Clan-context policy declared in doc 03 §4.1.4» reference) | Fails because doc 03 §4.1.4 does not exist. Any reader who follows the cross-reference will find nothing, breaking the provenance chain. EP-5 / provenance gate fails on a phantom reference. |

**Recommendation: Alternative A (self-declare the policy in §2.1) is cleanest for doc 06 as a standalone artefact. Alternative B is acceptable as a transitional stub if A is too expensive given the R1-surface-only intent of this draft. Status-quo is not acceptable — phantom cross-references fail the provenance gate.**

---

## §4 Anti-scope

- Не оцениваю стратегический вопрос — является ли FPF корректным языком для описания trust. Это Ruslan decides (α-5 Direction).
- Не оцениваю достаточность «нового интернета» как vision claim — это phil × critic territory. D-DOC06-ENG-* dissents ниже не включают эту оценку.
- Не оцениваю H8 §6.1 Octagon linkage table (H1-H8 cross-insights) — это mgmt + systems territory; engineering подтверждает только FPF-primitive correctness.
- Не оцениваю OQ-D06-1..OQ-D06-7 open questions — это Ruslan strategic judgment; они корректно атрибутированы как open questions, не claims.
- Не оцениваю §3 plain English narrative — intentionally non-formal, правильно атрибутирован к Ruslan voice.
- Не оцениваю R12 anti-extraction constructive framing (§3.7) — это Pillar C constitutional territory; engineering подтверждает только правильность применения A.2.8 Commitment в этом контексте.
- Не оцениваю валидность F/G/R grades в §2.3 — это philosophy × critic territory; engineering оценивает только наличие triples, не их calibration.

---

## §5 Cross-doc consistency check

**Doc 03 critic (tribe-eng-critic.md) declared:**
- FAIL-2: A.2.9 missing context-policy dependency in doc 03
- FAIL-3: A.1.1 BoundedContext absent from doc 03 entirely
- FAIL-1: Γ_work misapplication in doc 03 (Γ_sys / Γ_method are correct)

**Doc 06 compatibility with these findings:**

| Item | Status | Notes |
|---|---|---|
| Γ_work misuse | Consistent (correct) | Doc 06 does NOT introduce Γ_work. §4.3 cross-ref uses «Γ_sys B.1.2» — consistent with doc 03 critic RC-1 recommendation. Conformance check 9 self-declared PASS in doc 06 integrator is correct. |
| A.2.9 context-policy | **INCONSISTENCY** | Doc 06 §2.2 A.2.9 row claims «Clan-context policy declared in doc 03 §4.1.4». Doc 03 critic (FAIL-2 + FAIL-3) found: (a) no formal A.1.1 BoundedContext in doc 03, (b) no §4.1.4 exists. Doc 06 relies on a policy that does not yet exist. |
| A.1.1 BoundedContext | Consistent | Doc 06 §2.1 HAS a full BoundedContext (Glossary + Invariants + Roles + Bridges). This is a structural improvement over doc 03. No inconsistency here — doc 06 correctly implements what doc 03 was criticised for lacking. |
| Cross-reference to doc 03 §4.1.5 Bridges | **INCONSISTENCY** | §4.3 states «Cross-ref: doc 03 §4.1.5 Bridges explicitly names doc 06». Doc 03 integrator has no §4.1.5 section. The cross-ref is phantom. Doc 03 does not name doc 06 in any formal Bridges section (because no formal Bridges section exists). |
| F-G-R floor | Consistent | Both docs at F2 document-level; per-claim grades compatible. |
| R1 attribution | Consistent | Both carry `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured`. |
| EP-5 + EP-2 disclosures | Consistent | Both carry identical EP-5 and EP-2 disclosure text. |
| Honest status disclosure | Consistent | Doc 06 carries INTERNET-STATUS + H8-CLUSTER-STATUS disclosures. Well-structured, compatible with doc 03's vapor framing for Clan activation. |

**Cross-doc verdict: Substantively sound; two phantom cross-references create provenance failures.**

---

## §6 Specific Failures Found

### FAIL-1 (Moderate): A.2.9 context-policy — phantom cross-reference

**AP code:** AP-ENG-10 (external dependency without failure-mode declared; FPF A.2.9 normative constraint is the external dependency)

**Location:** §2.2 A.2.9 row («Clan-context policy declared in doc 03 §4.1.4»); §4.1 formal section (`speech_act_constitutes: U.SpeechAct(A, publish(F_grade, G_scope, R_condition))`)

**Evidence (verbatim, per doc 03 critic FAIL-2 precedent):**
FPF A.2.9:4.1 normative: «Whether a given actType institutes commitments/permissions/status changes is **entirely context-policy dependent**. Absent an explicit policy, treat a U.SpeechAct as a communicative Work occurrence with observable provenance only; **do not infer deontic bindings from the act by default**.»

**Analysis (two-part):**

Part 1 — Phantom cross-reference. Doc 06 §2.2 A.2.9 row states: «Clan-context policy declared in doc 03 §4.1.4». Verified: doc 03 integrator (`task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md`) has no §4.1.4. The doc 03 formal section is §4.1 «Cooperation graph — formal» with no subsections. There is no formal A.1.1 BoundedContext section and no Bridges section. The cross-reference is phantom. Per §5.5.5 provenance gate: a cited path that does not exist = provenance gate failure.

Part 2 — Formal section contradiction. §4.1 formal section uses `speech_act_constitutes: U.SpeechAct(A, publish(F_grade, G_scope, R_condition))`. This maps SpeechAct to a publication-with-epistemic-grade act (F_grade, G_scope, R_condition are F-G-R fields). However, §2.2 claims SpeechAct «creates the trust-relation, not merely transmits information» and the §2.1 Invariant I-4 is about MVPK (not SpeechAct). The §4.1 formal expression makes SpeechAct an F-G-R publication act, not a trust-constituting act with institutional effects. This is internally inconsistent: the row description says «institutes trust-relation»; the formal expression says «publish(F-G-R triple)». An F-G-R publication is a B.3 primitive application, not a deontic SpeechAct.

**Correct direction:** The SpeechAct in a trust-infrastructure-context should carry actType = a trust-constituting declaration (e.g. `actType="open-data-role-commitment-declaration"`) with `institutes: {RoleAssignmentRef, CommitmentIdRef}`. The F-G-R triple is a B.3 overlay on top of the SpeechAct, not its content.

**Severity: Moderate.** Two distinct sub-failures: (a) phantom cross-reference breaks provenance chain; (b) formal section contradiction weakens the FPF-correctness of the core trust-formation predicate in §4.1.

---

### FAIL-2 (Minor): §4.3 phantom cross-reference to doc 03 §4.1.5

**AP code:** AP-ENG-10 analogue (external dependency — stated Bridges — without verifiable grounding)

**Location:** §4.3 U.BoundedContext bridges bullet «→ doc 03 Virtual Tribe»: «Cross-ref: doc 03 §4.1.5 Bridges explicitly names doc 06.»

**Evidence:** Doc 03 integrator has no §4.1.5. Doc 03 has no formal Bridges section at all (doc 03 critic FAIL-3). The claim that «doc 03 §4.1.5 Bridges explicitly names doc 06» is not supported by any content in the doc 03 integrator draft.

**Analysis:** This is a second phantom cross-reference in the same document. The pattern is consistent with the integrator draft being written with aspirational cross-references to doc 03 sections that the doc 03 critic subsequently found to be absent. The doc 06 integrator anticipated a doc 03 BoundedContext structure that does not yet exist.

**Severity: Minor.** The substantive claim (doc 03 mutual instrumentation operates on doc 06 trust infrastructure) is correct and supported by doc 03 narrative content. The specific §4.1.5 reference is simply wrong. Fix = remove the specific section reference; replace with «doc 03 names doc 06 in cross-link §6.3 series table» (which is verifiable — doc 03 §6.3 does reference doc 06 as a dependency in the plain narrative).

---

### FAIL-3 (Minor): A.10 formal application insufficiently tagged as aspirational

**AP code:** AP-ENG-4 analogue (precision gap in primitive assignment — formal section overstates operational status)

**Location:** §4.1 formal section: `evidence_available: A.10.EvidenceGraph(A, observed_work_trail) ∧ A.10.EvidenceGraph(B, observed_work_trail)`

**Evidence:** §2.2 A.10 row correctly states «F2 primitive: git log functional as evidence ledger; formal Evidence Graph = aspirational». §3.8 honest status correctly lists «A.10 Evidence Graph формальная = stub (нет schema, нет query interface)».

**Analysis:** The §4.1 formal section expresses `A.10.EvidenceGraph(A, observed_work_trail)` as a binary predicate over A — implying that the Evidence Graph query exists and is callable. This is inconsistent with the §2.2 and §3.8 honest-status declarations. The formal section should tag A.10 application as aspirational, e.g. `A.10.EvidenceGraph(A, observed_work_trail) [aspirational — current primitive: A.10_primitive = git_log(A)]`. Without this tag, the TrustFormation predicate in §4.1 appears to require an operational Evidence Graph that the document itself admits does not exist.

**Severity: Minor.** The honest-status machinery (§2.2, §3.8) elsewhere in the doc is correct and thorough. The formal section is the one place where the operational gap is not surfaced. Fixable by a one-line annotation.

---

## §7 Mermaid validity

**Validity assessment:** PASS with one architectural note.

The §5 mermaid flowchart TB is syntactically valid:
- `%%{init: ...}%%` configuration block: correct JSON structure, valid themeVariables keys.
- `classDef` declarations: 8 definitions, all syntactically correct (color / fill / stroke / stroke-width / stroke-dasharray).
- Node labels: `<b>`, `<br/>`, `<i>` HTML tags — valid in Mermaid flowchart node labels.
- Edge labels: quoted strings on `-.->` and `-->` edges. All valid.
- Subgraphs: `subgraph H8_CLUSTER[...]`, `subgraph TRUST_OUTCOME[...]`, `subgraph NETWORK[...]` with `direction` directives. Syntactically valid.
- No undefined node references.

**Architectural note (not a syntax failure):** The linear chain `COM → SA → RA → EG → FGR → GR → MVPK` implies these 7 primitives form an ordered pipeline. The §2.2 cluster description correctly says they «compose» (not pipeline). The linear rendering in the mermaid diagram could mislead a reader into thinking trust-formation requires this exact sequence. A more accurate rendering would show them as parallel contributors to the trust cluster, with arrows going from each to a central `H8_CLUSTER_OUTPUT` node. This is not a blocking failure — the diagram caption correctly states «7 FPF primitives working together» — but it is a representational risk for the L1 audience.

**Mermaid verdict: Syntactically valid. One representational risk noted (pipeline vs composition confusion). Non-blocking.**

---

## §8 Dissents (new, from this critic pass)

**D-DOC06-ENG-4 (this pass, eng-critic).** §2.2 A.2.9 row claims «Clan-context policy declared in doc 03 §4.1.4». Doc 03 integrator has no §4.1.4 and no formal BoundedContext section. The policy grounding for A.2.9 «institutes» claim is undeclared in any existing artefact. Without the policy, FPF A.2.9:4.1 normative default applies: treat as «communicative Work occurrence with observable provenance only».
- F: F5 (codified — FPF A.2.9:4.1 normative; phantom reference confirmed by direct grep of doc 03 integrator)
- ClaimScope: holds for doc 03 integrator draft as of 2026-05-17; once doc 03 RC-2 (BoundedContext section) is implemented, this dissent resolves
- R: {refuted_if: doc 03 integrator found to contain §4.1.4 with context-policy declaration; accepted_if: §4.1.4 absent — which it is}

**D-DOC06-ENG-5 (this pass, eng-critic).** §4.1 formal section maps U.SpeechAct to `publish(F_grade, G_scope, R_condition)` — an F-G-R publication act, not a deontic institutional act. This contradicts §2.2's own claim that SpeechAct «creates the trust-relation». The formal section should use actType with institutional effects (CommitmentIdRef, RoleAssignmentRef) per FPF A.2.9 canonical field structure, not F-G-R triple fields.
- F: F4 (FPF A.2.9 canonical structure confirmed in FPF Spec; internal inconsistency between §2.2 description and §4.1 formal expression is directly observable in the artefact)
- ClaimScope: holds for §4.1 formal section as-written; does not affect the §3 plain English narrative which correctly describes SpeechAct as institutional
- R: {refuted_if: FPF A.2.9 found to permit F-G-R triple as the institutes content; accepted_if: A.2.9 institutes field expects CommitmentIdRef/RoleAssignmentRef — which is confirmed by archive/design/JETIX-FPF.md table showing U.SpeechAct = «Communicative work» SpA type}

**D-DOC06-ENG-6 (this pass, eng-critic).** §4.3 claims «doc 03 §4.1.5 Bridges explicitly names doc 06». Doc 03 integrator has no §4.1.5 and no formal Bridges section. The cross-reference is phantom. Convergent with FAIL-2 above; recorded as dissent for AP-6 preservation.
- F: F5 (confirmed by direct grep of doc 03 integrator for §4.1.4, §4.1.5 — no matches)
- ClaimScope: holds for doc 03 integrator draft as of 2026-05-17; once doc 03 RC-2 (BoundedContext + Bridges) is implemented, the substantive claim will become true even if the section number changes
- R: {refuted_if: doc 03 found to contain §4.1.5 or equivalent formal Bridges declaration naming doc 06; accepted_if: no such section exists — confirmed}

---

## §9 Recommended Changes

| # | Change | Failure addressed | Estimated effort |
|---|---|---|---|
| RC-1 (Moderate) | In §2.2 A.2.9 row: replace «Clan-context policy declared in doc 03 §4.1.4» with a self-declared policy in §2.1 BoundedContext (add §2.1.1 or expand Bridges): «Trust-Infrastructure-BoundedContext policy: U.SpeechAct of actType="trust-constituting-open-data-declaration" institutes {agreed-share commitment (A.2.8), role-token (A.2.1 Holder#Role:Context), verifiable provenance record (A.10 entry)}». In §4.1: replace `U.SpeechAct(A, publish(F_grade, G_scope, R_condition))` with `U.SpeechAct(A, actType="trust-constituting-declaration", institutes={CommitmentIdRef: agreed_share_A, RoleAssignmentRef: Role_A, ProvenanceRef: A.10_entry_A})`. | FAIL-1 (both parts) | Medium (§2.1 expansion + §4.1 replacement) |
| RC-2 (Minor) | In §4.3 «→ doc 03 Virtual Tribe» bullet: remove «Cross-ref: doc 03 §4.1.5 Bridges explicitly names doc 06.» Replace with: «Cross-ref: doc 03 §6.3 doc-series table references doc 06 as a dependency (narrative level). Formal Bridge declaration pending doc 03 RC-2 (BoundedContext implementation).» | FAIL-2 | Small (one sentence replacement) |
| RC-3 (Minor) | In §4.1 TrustFormation predicate: add aspirational tag to A.10 application: `A.10.EvidenceGraph(A, observed_work_trail) [aspirational; current primitive: A.10_primitive(A) = git_log_entries(A, repo_path)]` | FAIL-3 | Small (one-line annotation per A.10 occurrence in §4.1) |

---

## §10 Proposed Writes

```yaml
mode: critic
context:
  task_id: task-fpf-describe-jetix-2026-05-17
  artefact_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md
  cycle_id: cyc-fpf-describe-2026-05-17
critique:
  conformance_checklist:
    - {check_id: "1-deep-module", result: "N/A", evidence: "Not a code artefact; FPF-primitive surface is thin and well-structured"}
    - {check_id: "2-function-purpose", result: "pass", evidence: "All sections named with declared purpose; §2.2 has per-row role declarations"}
    - {check_id: "3-test-integrity", result: "N/A", evidence: "No test cases; 6 Hamel-binary R-conditions in §2.3"}
    - {check_id: "4-premature-abstraction", result: "pass", evidence: "All 7 primitives grounded with Jetix instances; vision-stage correctly tagged"}
    - {check_id: "5-external-dependency", result: "fail", evidence: "A.2.9 context-policy: phantom ref to doc 03 §4.1.4 (does not exist); §4.1 SpeechAct formal expression contradicts §2.2 institutional claim; AP-ENG-10"}
    - {check_id: "6-dry", result: "pass", evidence: "No duplicate definitions; §2.2 and §4.1 use distinct registers"}
    - {check_id: "7-tool-eval-acceptance", result: "N/A", evidence: "Not a tool-eval draft"}
    - {check_id: "8-architecture-pattern", result: "pass", evidence: "§4.2 names trust_cluster() composition pattern; §4.3 declares cross-doc bridges"}
  acceptance_predicate: "artefact passes 6/8 applicable checks but FAILS check 5 (A.2.9 context-policy: phantom cross-reference + formal section contradiction) AND has two secondary phantom cross-references (doc 03 §4.1.4 + §4.1.5); DOES NOT PASS"
  alternatives:
    - {label: A, description: "Self-declare trust-infrastructure context-policy in §2.1; fix §4.1 SpeechAct formal; fix phantom refs", kill_condition: "Fails if policy declared in doc 06 conflicts with doc 03 RC-2 policy once implemented"}
    - {label: B, description: "Tag A.2.9 institutional claim as aspirational stub pending doc 03 RC-2; replace phantom refs with narrative cross-refs", kill_condition: "Fails if L1 audience requires the institutional claim for trust-formation argument to hold"}
    - {label: "status-quo", description: "Retain phantom cross-references and current §4.1 SpeechAct expression", kill_condition: "Fails: phantom refs break provenance gate; formal section contradicts §2.2 institutional claim"}
  anti_scope:
    - "Not evaluating strategic validity of «новый интернет» vision — Ruslan decides (α-5 Direction)"
    - "Not evaluating F/G/R calibration of §2.3 claims — phil × critic territory"
    - "Not evaluating H8 Octagon insight linkage table (§6.1) — mgmt + systems territory"
    - "Not evaluating OQ-D06-1..7 open questions — Ruslan strategic judgment, correctly attributed"
    - "Not evaluating §3 plain English narrative — intentionally non-formal, correctly attributed to Ruslan voice"
specific_failures_found:
  - {ap_code: "AP-ENG-10", location: "§2.2 A.2.9 row + §4.1 formal section", evidence: "Phantom ref 'doc 03 §4.1.4' (does not exist); §4.1 SpeechAct maps to publish(F_grade,G_scope,R_condition) contradicting §2.2 institutional claim"}
  - {ap_code: "AP-ENG-10 analogue", location: "§4.3 bullet '→ doc 03 Virtual Tribe'", evidence: "Phantom ref 'doc 03 §4.1.5 Bridges' — section does not exist in doc 03 integrator"}
  - {ap_code: "AP-ENG-4 analogue", location: "§4.1 TrustFormation predicate A.10 application", evidence: "A.10.EvidenceGraph used as binary predicate without aspirational tag; §2.2 and §3.8 correctly tag A.10 as F2 primitive stub — §4.1 does not"}
recommended_changes:
  - {change: "Self-declare trust-infrastructure A.2.9 context-policy in §2.1; fix §4.1 SpeechAct formal expression to use actType + institutes fields", ap_code_addressed: "AP-ENG-10 (FAIL-1)", estimated_effort: "medium"}
  - {change: "Remove phantom '§4.1.5 Bridges' reference from §4.3; replace with verifiable doc 03 §6.3 narrative cross-ref", ap_code_addressed: "AP-ENG-10 analogue (FAIL-2)", estimated_effort: "small"}
  - {change: "Add aspirational tag to A.10 application in §4.1 TrustFormation predicate", ap_code_addressed: "AP-ENG-4 analogue (FAIL-3)", estimated_effort: "small"}
proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-critic.md
    status: written (this file)
    action: Write (complete)
provenance:
  - {path: "swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md", range: "L145 (§2.2 A.2.9 row)", quote: "Clan-context policy declared in doc 03 §4.1.4"}
  - {path: "swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md", range: "L281 (§4.1 formal)", quote: "speech_act_constitutes: U.SpeechAct(A, publish(F_grade, G_scope, R_condition))"}
  - {path: "swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-internet-eng-integrator.md", range: "L315 (§4.3)", quote: "doc 03 §4.1.5 Bridges explicitly names doc 06"}
  - {path: "swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md", range: "L43-49 (§2 Acceptance Predicate)", quote: "FAIL-2: A.2.9 context-policy missing; FAIL-3: A.1.1 BoundedContext absent"}
  - {path: "swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md", range: "grep for §4.1.4 — no matches", quote: "no §4.1.4 or §4.1.5 sections exist"}
  - {path: "archive/design/JETIX-FPF.md", range: "L3144-3154 (Γ flavour table + Jetix mapping)", quote: "Γ_work: Work as spent resource; Γ_method: Order-sensitive method composition; Γ_sys: System-specific"}
confidence: high
confidence_method: rubric-pass-rate
escalations: []
dissents:
  - {source_cell: "engineering-expert × critic (this pass)", claim: "A.2.9 §4.1 formal expression maps SpeechAct to F-G-R publication, contradicting §2.2 institutional claim", F: "F4", ClaimScope: "§4.1 formal section only; §3 narrative is consistent", R: {refuted_if: "FPF A.2.9 found to permit F-G-R triple as institutes content", accepted_if: "A.2.9 institutes field confirmed to expect CommitmentIdRef/RoleAssignmentRef"}}
```

---

*Engineering-expert × critic pass. §5.5.5 gate status: provenance ✓ (inline citations + path evidence) / 3 FAILs found (1 moderate, 2 minor) / acceptance predicate DOES NOT PASS / 3 recommended changes (RC-1 medium, RC-2 small, RC-3 small) / Γ_work NOT introduced by doc 06 (correct) / mermaid syntactically valid (1 representational note) / cross-doc consistency: 2 phantom cross-references to doc 03 sections absent from doc 03 integrator. Pending: phil × critic pass.*
