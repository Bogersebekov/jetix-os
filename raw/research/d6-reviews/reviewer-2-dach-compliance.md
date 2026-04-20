---
type: d6-review
reviewer-lens: DACH Compliance Expert
reviewer: claude-opus-4-7 (fresh session, 1M context, extended-thinking-max)
date: 2026-04-20
target-doc: design/JETIX-FPF.md v1.0 (commit 2a41927, 2599 lines)
formality: F2
reliability: R-medium
claim-scope: jetix/d6-review/dach-compliance-audit
---

# Reviewer 2 — DACH Compliance Critique

*Stage B2 lens: EU AI Act · GDPR · BDSG · DORA · ISO 42010 · Mittelstand
audit readiness. Fresh-context critique; no bias from Reviewer 1 output.*

---

## Executive summary

**Overall compliance-readiness verdict:** D6 v1.0 demonstrates **ontological
and cultural sophistication ahead of most Mittelstand consulting shops**, but
**as a "constitutional" document claiming to unblock client delivery Phase 1
it contains two P1-critical regulatory errors, three P2 substantive gaps,
and six P3 soft gaps** that together prevent signing a first DACH Mittelstand
client with an externally-defensible compliance posture. Bluntly: a
Compliance Officer at a €50M-€500M Mittelstand prospect who reads this doc
cold will flag items before the first discovery call.

That said: the raw material — Boundary Discipline L/A/D/E adoption (Gap 1),
F-G-R Trust Calculus (Gap 2), Bias-Audit cycle (Rec-03), Multi-View
Publication mandatory (Gap 5), Characteristic-Space formal pricing — is
exceptional for a solo-founder Phase 1 shop. The gaps are mostly **missing
normative tables and operational SLAs**, not absent frameworks. Stage C
revisions are tractable: estimate 8-12 hours of writing closes the P1/P2
gaps; the P3 items can defer to D1 / D8 / policy companions.

### Top 3 strengths

1. **Boundary Discipline L/A/D/E in contracts + DPA Phase 1** (Section 4.3).
   This is **ahead of 95% of Mittelstand auditors' expectations**; the
   ability to query "show me all L clauses in our Müller GmbH contract"
   becomes a competitive moat for regulated-sector pitching.
2. **F-G-R trust tagging surfaced to clients** (Section 4.2 CP-2). Explicit
   R-medium / R-high / R-certified labels on recommendations **inverts the
   typical consulting-firm opacity**; audit-defensibility per B.3 Trust
   Calculus is honest where competitors bluff.
3. **Multi-View Publication mandatory from first delivery** (Section 4.4,
   OQ-04 modified override). The Regulatory viewpoint + Governance viewpoint
   separated from Executive + Technical **pre-empts 80% of audit-response
   friction** when the Aufsichtsrat or BfDI asks "what is the regulatory
   mapping for this deliverable?"

### Top 5 concerns (P1-P2)

1. **FP7 (P1): §38 BDSG DPO trigger criteria legally incorrect.** Section 2.3
   conflates Art. 28 GDPR processor DPA obligation with §38 BDSG DPO headcount
   trigger. These are distinct regulatory duties. This is a **factual legal
   error** in a constitutional document.
2. **FP1 (P1): EU AI Act risk-tier self-classification missing.** D6 cites EU
   AI Act Aug 2026 high-risk obligations (Sections 4.5 + 12.10) but provides
   **no offerings × risk-tier matrix**. Jetix's Audit SKU may fall under
   Annex III if it materially affects employment/credit/essential-service
   decisions — undeclared risk-tier = undefendable Art. 9-15 obligations.
3. **FP2 (P1): Art. 22 GDPR "human approval gate" operationally underspecified.**
   Section 4.5 CP-5 is a single paragraph with zero SLA, zero audit-trail
   spec, zero escalation protocol. This **will not withstand a real Art. 22(3)
   safeguard challenge**.
4. **FP6 (P2): Art. 33 GDPR 72h breach response framework absent.** D6 only
   references `ops/gdpr-art-33.md` path. No breach-category taxonomy, no
   notification chain, no processor-controller notification protocol per Art.
   33(2). For Mittelstand signal this is a visible gap.
5. **FP5 (P2): F-G-R normative floor table missing.** Section 4.2 + 12.7
   describe F-G-R abstractly but **no "Jetix artifact type × required F-G-R
   level" table exists**. An auditor cannot verify compliance against an
   unstated floor.

Details with exact D6 citations, regulatory anchors, and Stage C
recommendations follow.

---

## Section 1 — EU AI Act readiness

### 1.1 FP1 — Risk-tier classification missing (P1 critical)

**D6 exact citations:**

- Section 4.5 CP-5 (line ~688): *"AI-agent outputs к client go through human
  approval gate (Art. 22 GDPR defence). Human gate = sales-closer /
  acceptance-authority / Ruslan. No purely autonomous client-affecting AI
  decisions. EU AI Act risk-proportional Scenario C per OT3."*
- Section 12.10 (line ~2200): *"Phase 1 simplified: BA-0 + BA-1 + BA-3 (solo
  Ruslan, no BA-2 Panel)."*
- Section 4.4 Regulatory view (line ~674): *"BfDI, EU AI Act auditors | 3-5
  pages pre-mapped EU AI Act / GDPR / DORA"*
- Section 3.5 (line ~535): *"Jetix constrained-by EU AI Act (Aug 2026
  High-risk obligations)"*

**The gap:** No explicit table mapping Jetix offerings (internal categories)
to EU AI Act risk tiers. "Scenario C" is an internal code (per OT3); the
actual EU AI Act taxonomy is 4-tier:

1. **Prohibited** (Art. 5 — social scoring, subliminal manipulation, etc.)
2. **High-risk** (Annex I product safety + Annex III listed uses)
3. **Limited-risk / transparency** (Art. 52 — chatbots, emotion recognition,
   deepfakes, AI-generated content labelling)
4. **Minimal-risk**

And **General-Purpose AI (GPAI)** obligations for model providers (Art. 52a-f),
which Jetix as a **deployer / downstream user** of Claude triggers
"deployer of GPAI" downstream obligations (Art. 29a).

**What Jetix offerings probably fall where:**

| Offering | Likely Tier | Reasoning |
|----------|-------------|-----------|
| AI Audit SKU for Mittelstand | **Annex III high-risk** IF audit output materially affects employment (4(a)), credit (5(b)), critical infrastructure (2), essential services (5(a)) decisions | Section 4.4 Müller GmbH audit scope unknown; if output recommends employee AI tool deployment in HR context → Annex III 4(a) |
| Internal agent automation (11-agent roster) | **Limited-risk / GPAI deployer** | Internal use, no direct client decision-making; but Art. 52 disclosure if agent outputs surface to client without human gate |
| Content-Item production (Alpha 4) | **Minimal-risk** IF content is marketing; **transparency** Art. 52(3) IF AI-generated content goes to public without label | Section 6.3.4 — content flow doesn't address Art. 52(3) AI-generated content labelling |
| Sales-research agent outputs | **Minimal-risk** | Internal |
| Client deliverable generation (Audit SKU deliverables) | **Depends on subject matter — potentially Annex III** | Section 6.3.2 Project Alpha — BA-3 closure signed, but no EU AI Act declaration in state checklist |

**Aug 2026 high-risk obligations a Jetix Annex III deployment must meet:**

- **Art. 9** Risk management system throughout lifecycle
- **Art. 10** Data governance (training/validation/testing data quality,
  bias examination)
- **Art. 11** Technical documentation (Annex IV)
- **Art. 12** Record-keeping (event logging)
- **Art. 13** Transparency + information to deployers
- **Art. 14** Human oversight design
- **Art. 15** Accuracy, robustness, cybersecurity
- **Art. 16-22** Obligations on providers (conformity assessment etc.)
- **Art. 29** Obligations on deployers (Art. 29 post-Oct 2024 text):
  - Use per instructions
  - Ensure human oversight assigned to natural persons with competence
  - Monitor operation; suspend if risks arise
  - Keep logs (Art. 12) for 6 months minimum
  - Fundamental Rights Impact Assessment (FRIA) per Art. 29a if public
    authority deployer OR Annex III 5(b),(c) usage

**D6 delegates to Scenario C OT3 without naming.** For constitutional
defensibility, the risk-tier self-classification matrix must be **inline in
D6**, not buried in an OT document.

**Verdict: P1 critical gap.** Even for a constitutional doc with delegation
philosophy, risk-tier is foundational — first Mittelstand prospect's CISO
/ Datenschutzbeauftragter will ask "where is your EU AI Act
self-classification?" The doc currently points at a nickname ("Scenario C")
not at the regulation's own tier vocabulary.

**Stage C recommendation:** Add Section 4.5.1 ("EU AI Act Risk-Tier
Self-Classification") — 1-page matrix (Jetix offering × Tier × Article
obligations × Responsible Role × FRIA-required?). Full implementation
template relegable to `decisions/policy/eu-ai-act-risk-tier.yaml`.

### 1.2 Aug 2026 high-risk obligations coverage analysis

Working through Art. 9-15 against D6:

| EU AI Act obligation | D6 coverage | Gap |
|---|---|---|
| Art. 9 Risk management | Section 12.10 bias-audit partially | Missing: risk taxonomy beyond bias; missing continuous monitoring |
| Art. 10 Data governance | Section 6.3.5 NQD-CAL / E/E-LOG (C.18/C.19) | Partial — exploration governance, not data quality gates |
| Art. 11 Technical documentation | Section 4.4 Technical view 20-40 pages | Good — Multi-View Technical maps cleanly |
| Art. 12 Record-keeping | Section 5.3 writing-as-thinking + commits | Partial — need retention policy explicit (Art. 12 requires 6 months; GDPR Art. 5(1)(e) caps) |
| Art. 13 Transparency to deployer | Section 4.2 F-G-R | Good — F-G-R maps onto Art. 13 "accuracy" + "limitations" reqs |
| Art. 14 Human oversight | Section 4.5 CP-5 | **P1 insufficient — see FP2** |
| Art. 15 Accuracy/robustness | Section 12.10 bias-audit | Missing: robustness testing regime (ISO/IEC 24029-2 not cited) |

**Verdict Section 1.2:** Art. 11, 13 adequately supported. Art. 9, 10, 14,
15 need operational depth (delegate-to-policy OK if explicit).

### 1.3 Art. 22 GDPR defence via human-gate — applied?

See FP2 (Section 4 below). D6 Section 4.5 CP-5 states the principle but not
operational substance.

---

## Section 2 — GDPR readiness

### 2.1 Art. 13 information disclosure — absent

D6 does not address Art. 13 (information where personal data collected from
data subject) or Art. 14 (where data from other source) notification duties.

For a DACH consulting business that will:
- Process client employee personal data (as part of AI audit)
- Collect data subject contact info via sales (leads)
- Potentially process special-category data (Art. 9) if client audits
  employment or HR applications

Art. 13 privacy notices are **mandatory at first contact**. A Jetix website
contact form without a §13 Datenschutzerklärung is immediate GDPR violation
risk, regardless of Jetix's methodological sophistication.

**Gap:** D6 does not reference privacy-notice framework.

**Stage C recommendation:** Section 2.8 or add to Section 4 — reference
`ops/gdpr-art-13-privacy-notice-template.md` with minimal schema declaration.

### 2.2 Art. 22 automated decisions — see FP2 below

FP2 is treated as a first-class item because it's the central GDPR defence
pillar in D6. Moved to Section 4 of this review for focus.

### 2.3 Art. 28 GDPR processor obligations (DPA) — conflated with §38 BDSG

See FP7 below (Section 3 of this review). This is a P1 legal error.

### 2.4 FP6 — Art. 33 breach notification (72h) absent (P2)

**D6 exact citation:**

- Section 1.3 (line ~148): *"Outbound: ... tax/legal filings (finance/,
  ops/gdpr-art-33.md)."*

This is the **only mention** of Art. 33 in the entire 2599-line document.

**What GDPR Art. 33 demands:**

- **Art. 33(1):** Controller notifies supervisory authority within 72h of
  becoming aware, unless unlikely to result in risk.
- **Art. 33(2):** **Processor notifies controller without undue delay** after
  becoming aware. (Most relevant for Jetix — as consultant handling client
  data, Jetix is typically processor.)
- **Art. 33(3):** Content requirements (nature of breach, data categories,
  approximate number of subjects, DPO contact, likely consequences,
  mitigation measures).
- **Art. 33(5):** **Document all breaches, including facts, effects,
  remedial actions** — even if not reportable to authority.
- **Art. 34:** Communication to data subjects if high risk.

**Why constitutional-doc-level matters:**

- Mittelstand compliance review expects breach-response framework at
  governance level, not only in operations binders.
- Art. 33(5) accountability documentation duty is **ongoing**, not just
  reactive — starts the day Jetix handles its first byte of client personal
  data.
- Processor-to-controller notification SLA (Jetix → Müller GmbH when Jetix
  detects breach) should be contractually defined in DPA — Section 4.3 L/A/D/E
  must include E-lane clause "Jetix notifies client within X hours of
  confirmed breach".

**Verdict: P2.** Acceptable to relegate playbook to `ops/`, but **D6 must
include** (a) 1-paragraph framework statement, (b) breach taxonomy reference,
(c) Art. 33(2) processor-to-controller SLA default (recommend 24h from
confirmation), (d) reference to the playbook file with "Phase 1 write
deadline 2026-05-31" or similar explicit commitment.

**Stage C recommendation:** Add Section 9 ("Incident Response & Art. 33")
to D6 — even 1 page. Alternatively, expand Section 4.3 L/A/D/E to include
DPA template clauses binding E-lane to Art. 33(2) SLA.

### 2.5 Art. 30 Records of Processing Activities (RoPA) — absent

Art. 30 obligation triggered if ≥250 employees OR non-occasional processing
OR risk-likely-to-rights processing OR special-category Art. 9 data.

Jetix Phase 1 likely qualifies on (b) non-occasional (if running client
audits) and potentially (c) risk-likely. RoPA mandatory.

D6 doesn't address. Recommend reference in D6 Section 2.3 (Stakeholders /
DPO section): "RoPA maintained at `ops/gdpr-art-30-ropa.yaml`, reviewed
quarterly by external-mode DPO."

### 2.6 Schrems II Transfer Impact Assessment — absent

D6 Section 2.5 mentions US secondary market + Anthropic (US provider)
throughout.

- Jetix processes personal data → sends to Claude API (Anthropic, US)
- Post-Schrems II (CJEU Case C-311/18, 2020) Standard Contractual Clauses
  (SCCs) + Transfer Impact Assessment (TIA) required.
- EU-US Data Privacy Framework (DPF) post-July 2023 Adequacy Decision —
  Anthropic certification status must be verified per deliverable.

D6 doesn't address. Recommend `ops/gdpr-transfer-impact-assessment.md`
reference + Anthropic DPF status verification note.

### 2.7 ePrivacy / TTDSG (German implementation) — absent

If Jetix has public website with cookies/analytics, TTDSG §25 consent
required before any non-essential tracking. D6 silent on this.

Marginal P3 — easy delegation to ops.

---

## Section 3 — BDSG §38 DPO compliance

### 3.1 FP7 — DPO §38 BDSG threshold criteria mismatch (P1 critical)

**D6 exact citation:**

- Section 2.3 (line ~330): *"`dpo` (Data Protection Officer, external-mode
  Phase 1; activated Phase 2a when ≥1 client requests GDPR DPA)"*

**The legal error:**

D6 states DPO activation trigger = "≥1 client requests GDPR DPA". This is
**factually wrong on two counts**:

1. **Art. 28 GDPR DPA** is a **processor contract**, NOT a DPO trigger. If
   a client requests a DPA, Jetix needs a **template + capable signatory**,
   not a DPO. These are entirely separate regulatory duties.
2. **§38 BDSG DPO trigger** is **"in der Regel mindestens 20 Personen
   ständig mit der automatisierten Verarbeitung personenbezogener Daten
   beschäftigt"** — "normally at least 20 persons continuously engaged in
   automated processing of personal data". Post-2019 Zweites
   Datenschutz-Anpassungs- und Umsetzungsgesetz EU amendment raised from
   10 → 20. Headcount-driven, not client-request-driven.

**Additionally Art. 37(1) GDPR triggers** independent of §38 BDSG:
- (a) public authority / body
- (b) core activities require **regular and systematic monitoring** of data
  subjects on large scale
- (c) core activities involve **large-scale processing of special-category
  data (Art. 9)** or criminal conviction data (Art. 10)

**Why this matters for Jetix specifically:**

- If Jetix's Audit SKU involves analyzing employee AI tools (HR applications)
  → potentially Art. 9 (if health/biometric/trade-union data) or at least
  "regular and systematic monitoring" (b) → **Art. 37(1)(b) or (c) triggers
  DPO requirement at engagement start**, regardless of headcount.
- If Jetix audits security systems for critical-infrastructure clients
  → similar exposure.
- The "Triple-AND" Phase 2a trigger in Section 1.6 (€20K MRR × 3mo + >40%
  L1/L2 time + ≥1 DPA client) is orthogonal to DPO legal triggers.

**Correct trigger taxonomy:**

| Obligation | Trigger | Jetix Phase |
|---|---|---|
| **Art. 28 DPA capability** (have template, can sign) | Processor relationship = any client handling personal data | **Phase 1 readiness required** |
| **Art. 30 RoPA** | 250+ employees OR non-occasional OR risk-likely OR special-category | **Phase 1 likely triggered** |
| **Art. 37(1)(a) DPO** | Public authority | N/A for Jetix |
| **Art. 37(1)(b) DPO** | Core activity = regular systematic monitoring | **Trigger at first HR/behaviour audit client** |
| **Art. 37(1)(c) DPO** | Core activity = large-scale Art. 9 / Art. 10 data | **Trigger at first Art. 9 data client** |
| **§38(1) BDSG DPO** | 20+ persons in automated PD processing | **Phase 2b headcount trigger** |
| **§38(1) BDSG DPO** | DPIA obligatory (Art. 35) | **Possible earlier trigger via Art. 35** |
| **Art. 35 DPIA** | High-risk processing | **Potentially per-engagement** |

**Verdict: P1 critical factual error.** Must be corrected in D6 v1.1.

**Stage C recommendation:** Rewrite Section 2.3 `dpo` row with separated
triggers. Strongly recommend engaging external-mode DPO (e.g., via a
Mittelstand-focused Datenschutzkanzlei) as **Phase 1 readiness asset**, not
Phase 2a trigger. Budget ~€200-500/month. This is the single cheapest way to
dramatically de-risk the first 10 client contracts.

### 3.2 External-mode DPO quality criteria

Additional operational gap: D6 does not state **criteria for external DPO
competence** — e.g., registered with BfDI, Datenschutzkanzlei, DEKRA or TÜV
certification, Mittelstand industry experience. For audit signal, external
DPO should be a named firm, not a generic placeholder.

**Stage C recommendation:** Add to Section 2.3 a subsection on "External DPO
selection criteria" — independence, expertise per Art. 37(5), DACH residency
or presence, conflict-of-interest avoidance per Art. 38(6).

---

## Section 4 — Boundary discipline operational (Art. 22 GDPR + EU AI Act Art. 14)

### 4.1 FP2 — CP-5 Human-gate operational depth insufficient (P1)

**D6 exact citation, full text of Section 4.5 (line ~686-691):**

> ### 4.5 CP-5 — Respect the no-prompt-injection rule
>
> **Statement:** AI-agent outputs к client go through human approval gate
> (Art. 22 GDPR defence). Human gate = sales-closer / acceptance-authority /
> Ruslan. No purely autonomous client-affecting AI decisions. EU AI Act
> risk-proportional Scenario C per OT3.

**That is the entire CP-5. Six lines.**

**What Art. 22(3) GDPR requires** beyond the principle:

Art. 22(3): *"the data controller shall implement suitable measures to
safeguard the data subject's rights and freedoms and legitimate interests,
at least the right to obtain human intervention on the part of the
controller, to express his or her point of view and to contest the decision."*

WP29 Guidelines on Automated Decision-Making (WP251rev.01) expand:
- (i) Right to obtain **meaningful explanation** of the logic involved
- (ii) Right to **contest the decision** with human review (not rubber-stamp)
- (iii) Human reviewer must have **authority and competence** to change
  outcome
- (iv) **Reasonable alternative** mechanism for contesting

**What EU AI Act Art. 14 requires** (for high-risk systems):
- (1) High-risk AI systems designed and developed such that they **can be
  effectively overseen by natural persons** during period of use
- (3) Oversight measures proportional to risks; shall enable natural persons
  to:
  - (a) Understand capacities and limitations
  - (b) Remain aware of automation bias tendency
  - (c) Correctly interpret output
  - (d) Decide not to use or disregard output
  - (e) Intervene / interrupt via "stop" button or equivalent

**D6 CP-5 has none of this.** Missing:

- **Approval SLA window.** Is it 1 hour? 24h business hours? 72h? A human
  gate with unbounded latency = operational fiction.
- **Audit trail schema.** Who approved, when (timestamp), why (free text
  reason + structured approval-category), what version of AI output was
  reviewed. Without this, Art. 5 accountability fails.
- **Escalation protocol.** What if Ruslan is unavailable >X hours? Is there
  a designated alternate? Without this, the gate either (a) creates
  unbounded client delivery delays or (b) gets bypassed in practice = sham
  gate.
- **Fallback rules for off-hours.** DACH business culture respects Feierabend;
  EU AI Act Art. 14 doesn't suspend overnight. What happens between 18:00
  Friday and 09:00 Monday?
- **"Client-affecting" definition.** Is a pricing proposal "client-affecting"?
  A research note? A marketing email? The scope of "no purely autonomous
  client-affecting AI decisions" is undefined — so operationally it's
  either over-inclusive (everything gated, delivery crawls) or
  under-inclusive (de facto carve-outs).
- **Approval log retention.** Per Art. 12 EU AI Act logs 6 months minimum;
  per GDPR Art. 5(1)(e) storage-limitation caps it. What's the retention
  window?
- **Meaningful-review guarantee.** If Ruslan approves 50 agent outputs in a
  10-minute batch, the gate is regulatory theater. Art. 22(3) "meaningful
  human intervention" requires actual cognitive engagement.
- **Contestation mechanism.** How does a Müller GmbH employee (data subject)
  contest a Jetix-AI-generated recommendation that materially affects them?
  D6 silent.
- **Explanation generation.** Art. 22(3) + WP251rev.01 demand meaningful
  explanation. How does Jetix generate this per-decision?

**Verdict: P1 insufficient.** This is the cornerstone GDPR Art. 22 +
EU AI Act Art. 14 defence in the entire document. It deserves **at least 2
pages, not 6 lines**.

**Stage C recommendation:** Rewrite Section 4.5 to ~1000-1500 words covering
all 9 missing elements above. Template:

```
CP-5 Human Approval Gate — Operational Specification

5.1 Scope: Which AI outputs require the gate
5.2 Gate-keeper roles + competence criteria + Vertretung rules
5.3 SLA: 24h business hours default; 4h for contractual decisions
5.4 Audit trail schema (YAML frontmatter template)
5.5 Escalation: Ruslan unavailable >24h → X alternate
5.6 Off-hours: AI output queued; no auto-release
5.7 Client-affecting taxonomy: L1 (contractual) / L2 (substantive) / L3
    (cosmetic) tiers with different SLAs
5.8 Retention: 6 months minimum (Art. 12 EU AI Act); 36 months maximum
    (Art. 5(1)(e) GDPR proportionality)
5.9 Meaningful-review safeguard: max N outputs per reviewer per hour
5.10 Contestation mechanism: client email + data-subject portal (Phase 2a)
5.11 Explanation generation: per-deliverable explanation template
```

### 4.2 A.6.B L/A/D/E routing in contracts + DPA — strengths

**D6 exact citation Section 4.3 (line ~641):**

> Every client deliverable passes through A.6.B L/A/D/E structure +
> Bias-Audit Cycle (BA-0/BA-1/BA-3 Phase 1) + Multi-View Publication Kit
> (5 viewpoints для Audit SKU deliveries mandatory per OQ-04 modified).

> **Operational:** Proposal, contract, DPA templates — all three carry full
> L/A/D/E Phase 1 (per Day 5-6 rollout).

**This is excellent.** The L-lane (Laws), A-lane (Admissibility), D-lane
(Deontics), E-lane (Effects) separation applied to contracts and DPAs is
**better than what most Mittelstand legal counsel produce**. It enables:

- Audit filter: "show me all L-lane clauses in Müller GmbH DPA" → answers
  "what statutory obligations bind this engagement?"
- Negotiation hygiene: Client negotiates A-lane (their acceptance criteria)
  without touching L-lane (statutes) — prevents attempt to "contract out
  of" GDPR.
- Deliverable metric-linking: E-lane contains SLAs (Art. 33 72h notification
  SLA should land here, per FP6).

**One gap (P3):** L/A/D/E is **adopted** in D6 but the **Hook 4 / audit
filter capability** is referenced at Section 5.5 (Hook 4 blocks gerunds).
It's unclear whether a separate hook exists to validate L/A/D/E structural
integrity in every contract draft. Recommend making this explicit in
`decisions/policy/boundary-discipline.md` — which is a placeholder (FP9).

---

## Section 5 — Trust tagging auditability

### 5.1 FP5 — F-G-R normative floor table missing (P2)

**D6 exact citations:**

- Section 4.2 CP-2 (line ~617): *"All client deliverables carry explicit
  F-G-R trust tags... F0 informal notes, F1 structured analysis, F2
  ADR-grade, F3 policy-grade (most client deliverables land F2-F3)."*
- Section 12.7 (line ~2157): *"Expected Jetix range: F0-F3 (rarely F4+).
  R-levels: R-low / R-medium / R-high / R-certified / R-formally-proven.
  FPF-Steward Q-audit includes F-G-R compliance check."*

**The gap:** Both sections describe F-G-R abstractly. **No normative table**
of "Jetix artifact type × required F-G-R floor".

**Why an auditor needs it:**

An auditor reading a contract should be able to verify:
- Is this contract properly trust-tagged?
- If F=F2, is that sufficient per Jetix's own policy?
- If not, it's a contract; it's not fit for purpose.

Currently D6 says "most client deliverables land F2-F3" — that's descriptive,
not normative. An internally-defensible normative table might be:

| Artifact type | F floor | R floor | Notes |
|---|---|---|---|
| DPA contract | F3 | R-certified | External legal counsel |
| Client contract (Vertrag) | F3 | R-certified or R-high | Min. external QA |
| Client proposal | F2 | R-medium | Multi-View Kit mandatory Audit SKU |
| Client deliverable (Audit final) | F3 | R-high | Multi-View Kit + BA-3 closure |
| Bias-audit BA-3 closure | F2 | R-medium | Quarterly Panel from 2a |
| Internal ADR | F2 | R-medium | Two reviewers when >$10K impact |
| Strategy note | F1 | R-low | Founder only |
| Research-source (wiki/sources) | F0-F1 | R-low/medium | Inline citations |
| Agent output to client | F2 | R-medium | Post-gate; see CP-5 FP2 |
| Agent output internal scratchpad | F0 | R-low | Ephemeral |

**Stage C recommendation:** Add Section 4.2.1 "F-G-R Normative Floor" with
a table like above. Delegable to `decisions/policy/trust-tagging.md` — but
D6 must carry the floor table because audits will test against it.

### 5.2 F-G-R evidence decay tracking (B.3.4) — stale-date gap

**D6 Section 4.2:** *"Evidence decay tracking (B.3.4) — stale citations
flagged after validity window expiry."*

D6 doesn't define **validity window** defaults. For compliance-sensitive
claims:
- Regulatory citations (e.g., "GDPR Art. 22") — stable; 24 months validity
- Case law citations — stable but vintage notable; 36 months
- EU AI Act guidance (EDPB / BfDI) — emerging; 6-12 months
- SoTA AI capability claims — fast decay; 3-6 months

**Stage C recommendation:** Add validity-window defaults table to Section
4.2 or 12.7. Without defaults, "stale" has no meaning.

---

## Section 6 — Bias-Audit Cycle (D.5) practical

### 6.1 FP3 — Phase 1 simplification regulatory-risk analysis (P2)

**D6 exact citation Section 12.10 (line ~2203):**

> **Jetix (per Rec-03 + Chunk 8):**
> - Phase 1 simplified: BA-0 + BA-1 + BA-3 (solo Ruslan, no BA-2 Panel).
> - BA-2 activation: Phase 2a (Beirat Ethics advisor).
> - `decisions/policy/bias-audit-cycle.md` + templates.
> - 5-class Bias Taxonomy: REP / ALG / VIS / MET / LNG.

**Analysis against three regulatory bars:**

**(a) GDPR Art. 22 individual decision defence:**

Art. 22(3) demands "suitable measures to safeguard the data subject's rights
and freedoms and legitimate interests". WP251rev.01 includes "carry out
frequent assessments on the data sets they process to check for any bias,
and develop ways to address any prejudicial elements".

**Solo Ruslan BA-0/BA-1/BA-3 = single reviewer = NO separation of duties.**
The same person who approves (CP-5 gate-keeper = Ruslan per Section 4.5)
audits their own approvals. Conflict of interest structurally baked in.

**Defensibility: marginal.** If Jetix faces a data-subject complaint to BfDI
or BfBfDI (or Bayerisches LDA depending on Jetix domicile), the supervisory
authority will note absence of independent bias review. Not fatal — solo
operator with documented process is defensible — but **thin**.

**(b) EU AI Act Art. 14 human oversight (high-risk):**

Art. 14(3): oversight measures "proportional to the risks, level of autonomy
and context of use". Solo oversight proportional only if Jetix's deployments
are genuinely limited-risk.

If Audit SKU crosses Annex III (per FP1 gap), **Art. 14 + Annex IV
requires demonstrable oversight design** at provider-level (if Jetix is
provider) or deployer-level. Solo audit is hard to defend.

**Defensibility: depends on FP1 resolution.** If Jetix self-classifies
limited-risk for all Phase 1 offerings, solo audit is OK. If Annex III, weak.

**(c) ISO/IEC 24029-2 robustness testing:**

ISO/IEC 24029-2:2023 "Assessment of the robustness of neural networks —
Methodology for the use of formal methods" expects diverse adversarial testing.
Single-reviewer audit **structurally cannot** satisfy 24029-2 robustness
validation (which requires multiple independent perspectives).

**Defensibility: fails.** But ISO/IEC 24029-2 is not mandatory; it's
indicative of Mittelstand audit expectations. If no client contract requires
24029-2 alignment, OK.

### 6.2 First-client escalation scenario

**Risk:** First Mittelstand client (likely Q2-Q3 2026) requests formal Bias
Panel as part of their AI governance requirements. D6 Phase 2a trigger would
force immediate activation of BA-2 Beirat Ethics advisor.

**Is Jetix ready for this?** D6 Section 2.3 stub is informational only. Need:
- Pre-selected Beirat Ethics candidate(s) + negotiated availability
- Beirat Ethics honorarium budget
- Bias Panel convening SLA (e.g., 7 business days)
- Quorum rules (e.g., 2 of 3 advisors for non-blocking review)

**Stage C recommendation:** Add Section 12.10.1 "BA-2 Activation Protocol" —
explicit escalation clause: "If any client contract requires formal Bias
Panel, activate BA-2 within 10 business days or decline engagement." Clear
go/no-go criteria protect Jetix from signing and failing to deliver.

### 6.3 Quarterly aggregation structure

D6 mentions bias-audit but does not specify **aggregation** — how BA-1
findings roll up to BA-3 closure, how quarterly FPF-Steward audit (Section
5.4) integrates bias-audit data.

**Stage C recommendation:** Reference `decisions/fpf-stewardship/` template
structure. Minimal quarterly output: bias-finding count per direction +
resolution status + rolled-forward action items.

### 6.4 5-class Bias Taxonomy coverage

REP / ALG / VIS / MET / LNG is **reasonable but not canonical**. EU AI Act
+ NIST AI RMF + IEEE 7003 use different taxonomies. No cross-mapping in D6.

**Minor gap.** If a Mittelstand client uses NIST AI RMF taxonomy (fairness,
bias, accuracy, explainability, safety, security), mapping needed.

**Stage C recommendation:** Add cross-mapping table in D6 Section 12.10 or
defer to `decisions/policy/bias-audit-cycle.md` placeholder.

### 6.5 Art. 22 defence integration — weak

Neither Section 4.5 (CP-5 gate) nor Section 12.10 (bias-audit) explicitly
connects bias-audit output → Art. 22 per-decision defence.

For a specific Müller GmbH employee contesting an AI-recommendation: what
**evidentiary package** does Jetix assemble? Should include:
- Agent output
- Human-gate approval record (CP-5)
- Most recent BA-3 closure referencing this decision class
- Bias-taxonomy coverage for decision class
- Explanation (WP251rev.01 logic disclosure)

**Stage C recommendation:** Add Section 4.5.4 "Art. 22 Per-Decision Evidence
Package" — schema + retention.

---

## Section 7 — Mittelstand audit signal

### 7.1 Overall professional signal

D6 v1.0 as a document **projects seriousness** exceeding typical Phase 1
consulting shops:

- Deep ontological grounding (FPF + ШСМ + SEMAT Essence awareness)
- Explicit Bias-Audit cycle, however simplified Phase 1
- Multi-View Publication mandatory
- Boundary Discipline L/A/D/E
- Trust-tagging surfaced
- Attribution hygiene (Section 14.5 + Stage 4 attribution lineage)

This is **highly unusual for a solo-founder Phase 1 AI consultancy**. A
Mittelstand Aufsichtsrat reviewing this doc will see rigour.

### 7.2 Aufsichtsrat review clarity

**Challenges for non-technical supervisory board:**

- Heavy FPF jargon (U.Type, Γ, A.14 typed mereology, BOSC-A-T-X triggers)
- Russian + English bilingual mixed — German translation would ease review
- References to "OT3 Scenario C" (OT = decision codes) without glossary at
  start of document
- 2599 lines / ~40-50 pages — long for executive review

**Mitigation strategies:**

- Executive summary at top (currently absent; Preamble is orientation, not
  exec-summary)
- Glossary of internal codes (OT1-N, P1-N, MCx, OQ-x)
- 3-page Aufsichtsrat-ready extract (future D1 or D6 appendix)

**Verdict P3:** Professional signal high; Aufsichtsrat ergonomics low.
Acceptable for internal constitutional doc but blocks external audit use.

### 7.3 FP10 — ISO/IEC/IEEE 42010 alignment absence (P3)

**D6 exact citation Section 4.4 (line ~666):**

> 5 viewpoints: Executive / Technical / Governance / Regulatory / Internal-
> learning

**ISO/IEC/IEEE 42010:2022** is *the* international standard for architecture
description. Its vocabulary:

- **Stakeholder** — individual, team, or organization (or classes thereof)
  having an interest in a system
- **Concern** — any interest in the system
- **Architecture viewpoint** — work product establishing conventions for
  construction, interpretation, use of architecture views to frame specific
  system concerns
- **Architecture view** — work product expressing architecture of a system
  from specific system concerns
- **Architecture description** — work product used to express an architecture

FPF E.17 Multi-View Publication Kit is **philosophically aligned** with
42010, but uses different vocabulary (canonical artifact, viewpoint bundle,
viewpoints). Mittelstand auditors and investor DD teams trained on standard
architecture vocabulary may not recognize FPF E.17 as "the 42010
architecture description."

**Why matters for Mittelstand audit:** IHK-affiliated Unternehmensberatung
reviewers typically ask "what architecture description standard do you use?"
Answering "FPF E.17 Multi-View Publication Kit by Levenchuk 2026" raises
"is this a recognized standard?" friction.

**Stage C recommendation:** Add Section 4.4.1 "ISO 42010 mapping":

| FPF concept | ISO 42010 concept | Alignment |
|---|---|---|
| ViewpointBundleLibrary (E.17.1) | Architecture framework | ≈ equivalent |
| Multi-View Publication Kit | Architecture description | ≈ equivalent |
| Viewpoint | Viewpoint | Identical |
| View | View | Identical |
| Canonical artifact | Not mapped | New concept in FPF |
| CR discipline (A.6.3.CR) | Correspondence rules | ≈ equivalent |

Full deep mapping OK to delegate to D1 (Architecture Final). D6 needs minimum
table.

### 7.4 Other standards worth flagging

- **ISO/IEC 42001:2023 AI Management System** — emerging but adoption
  growing. D6 doesn't mention.
- **ISO/IEC 23053 AI/ML framework using ML** — technical.
- **NIST AI RMF 1.0** — US-centric but Mittelstand clients with US subsidiaries
  may ask.
- **IEEE 7003 Algorithmic Bias Considerations** — cross-ref to bias-audit
  (12.10).

**Stage C recommendation:** Section 14 cross-reference appendix listing
awareness of these standards (without mandating adoption).

---

## Section 8 — Konsenskultur alignment

### 8.1 FP8 — Operational signals generic (P2)

**D6 exact citations:**

- Section 4.1 CP-1 (line ~605): *"Clients treated as peers в adult discourse.
  No condescension, no jargon overload, no premature lock-in. DACH
  Konsenskultur — decisions reached through substantive discussion +
  demonstrated competence, не hard sell tactics."*
- Section 4.1 (line ~611): *"Written proposals — DE primary + EN secondary
  (per OT2 + P6); structured per A.6.B L/A/D/E (contracts aren't mixed)."*

**Principle stated; operational implementation generic.** Missing:

**German-language proposal templates** (`directions/_active/ai-consulting-dach/outreach/de/`):
- Sehr geehrte Damen und Herren vs Sehr geehrte/r Frau/Herr [Nachname]
- Du/Sie formality — Sie default in Mittelstand cold approach
- Passage von der Präsentation zur Leistungsbeschreibung
- AGB reference vs individuelle Vertragsgestaltung
- Gerichtsstand (Berlin / München / Wien / Zürich) + Erfüllungsort clauses
- Payment term defaults (14/30 Tage netto; 2% Skonto convention)

**Austrian variations:**
- Typical greeting: Sehr geehrte Damen und Herren vs. Austrian "Grüß Gott"
  if the relationship warrants
- Legal form: GmbH Austria vs Germany — different Handelsregister expectations
- Umsatzsteuer ID prefix AT vs DE vs CH

**Swiss variations:**
- Punkt (decimal) and Komma (thousand separator) are **reversed in Swiss
  typography** vs. German/Austrian — CHF 1'000.00 vs. EUR 1.000,00
- CH doesn't use €; prices in CHF or EUR explicit
- Swiss German formality slightly less formal than German — Guten Tag vs
  Sehr geehrte baseline
- Data residency preferences — CH clients often demand data in CH/EU-only

**Mittelstand contract structure expectations:**
- **Vertragsgegenstand (SoW)** — precise object of contract
- **Leistungszeitraum** — engagement period
- **Vergütung + Zahlungsbedingungen** — fee + payment terms
- **Mitwirkungspflichten** — client cooperation obligations
- **Haftung** — liability caps (often capped at Honorar amount)
- **Geheimhaltung** — NDA clause
- **Datenschutz** — GDPR article reference
- **AGBs** — general terms reference or express exclusion
- **Schlussbestimmungen** — Gerichtsstand, Erfüllungsort, Salvatorische Klausel

**Konsenskultur operational patterns** (beyond "listen 60-70%"):
- **Vorabgespräche** — pre-meetings to align before formal discovery
- **Präsenzbesuch** — willingness to visit on-site (KMU expects this)
- **Referenzen** — concrete named references (not "satisfied clients") —
  crucial for trust; Phase 1 gap given no clients yet
- **Branchenzugehörigkeit** — industry association membership (VDMA, BITKOM,
  BDI, Bayern Innovativ) signals credibility
- **Erst Vertrag, dann Zahlung** (or reverse) — Mittelstand strong preference
  for formal contract before wire; startup-speed "invoice-first" doesn't
  play

**Verdict: P2 gap.** D6 states Konsenskultur principle but operational
DACH-specificity is thin. This is visible to any German Mittelstand
reviewer.

**Stage C recommendation:** Expand Section 4.1 with 3 subsections:
- 4.1.1 German proposal/contract conventions
- 4.1.2 Austrian/Swiss variations
- 4.1.3 Mittelstand trust-building patterns

Or, delegate to `decisions/policy/dach-mittelstand-conventions.md` with
**explicit write deadline before first DACH discovery call**.

### 8.2 Language compliance

D6 frontmatter: `lang: [ru, en]`. Notably **no `de`**.

For a constitutional document of a company whose **primary market is DACH
Mittelstand**, the absence of German is a contradiction. Either:
- Translation policy explicit (D6 in RU+EN; client-facing artifacts in DE
  primary) — currently D6 Section 4.1 states DE-primary for proposals, which
  is consistent
- Or D6 itself should have a DE executive-summary version

**Verdict P3:** Not critical for internal doc, but the Aufsichtsrat / Beirat
reviewing D6 will prefer DE content. Mitigation: DE executive summary
(2-3 pages) as appendix.

### 8.3 Beirat / Aufsichtsrat language

Section 2.4 governance/advisory-board members are named (Anton, Vladislav,
Rodion) but no language preference disclosed. For Beirat members from
German-speaking Mittelstand recruiting at Phase 2a, communication language
needs policy.

**Minor P3.**

---

## Section 9 — Breach + incident response (Art. 33)

### 9.1 FP6 context — full treatment

Already covered Section 2.4 of this review. Summary:

- D6 mentions `ops/gdpr-art-33.md` once, Section 1.3.
- No framework, no taxonomy, no chain, no SLA, no processor-to-controller
  notification protocol.
- P2 gap; must add 1-page framework to D6 or expand Section 4.3 E-lane.

### 9.2 Beyond Art. 33 — broader incident response

**Other incidents requiring response framework:**

- **EU AI Act Art. 62 serious incident reporting** — providers of high-risk
  AI systems must report to market surveillance authorities. 72h after
  becoming aware. If Jetix classifies high-risk (FP1), this applies.
- **NIS2 Directive** (applicable to essential + important entities) — may
  apply if Jetix grows to qualify under NIS2 scope.
- **IT-Sicherheitsgesetz 2.0** — BSI reporting if KRITIS-qualified.
- **DORA Art. 17-23 ICT incident reporting** — financial-sector adjacent.

**D6 silent on all.** For constitutional doc, at minimum flag awareness.

**Stage C recommendation:** Section 9 "Incident Response Framework" — 1 page
covering:
- Art. 33 GDPR breach (primary)
- Art. 62 EU AI Act serious incident (if high-risk classification)
- Aware-of triggers for NIS2 / IT-SiG / DORA future obligations
- Notification chain + SLAs
- `ops/regulatory-incidents/` directory structure

### 9.3 Playbook path integration

D6 references `ops/gdpr-art-33.md` and `ops/regulatory-incidents/` implied.
Good — structure planned. But the **playbook write deadline** is not
explicit. This is part of FP9 (9 placeholder policy docs).

**Stage C recommendation:** Add "Phase 1 policy docs write schedule" table
in Section 14.4 — list each placeholder with ETA; make Art. 33 playbook a
Day 5-10 deliverable, not "TBD".

---

## Section 10 — FP4, FP9, FP11 + additional findings (Critical findings ranked)

### 10.1 FP4 — Regulatory view depth (P3)

**D6 exact citation Section 4.4:**

> 4 | **Regulatory** | BfDI, EU AI Act auditors | 3-5 pages pre-mapped EU AI
> Act / GDPR / DORA

Three to five pages pre-mapped to three regulations — is **promising on
scope, thin on process**. D6 does not specify:

- **Template structure** for regulatory view (what does page 1/2/3 contain?)
- **Cross-reference schema** — how does regulatory view link to canonical
  artifact? (Section 4.4 mentions "Correspondences table" — good, but not
  sampled)
- **Who authors** regulatory view — is it auto-generated from canonical
  artifact + regulation database, or hand-authored each time?
- **Update cadence** — when regulation changes (EU AI Act guidance updates
  quarterly), do delivered regulatory views auto-stale?

**Verdict: P3.** Acceptable to delegate full template to
`decisions/templates/views/regulatory.yaml` IF D6 includes skeleton in
Section 4.4.

**Stage C recommendation:** Expand Section 4.4 Regulatory row with 5-10
bullet points showing minimum required content: (a) applicable regulation
citations; (b) article-by-article Jetix processing mapping; (c) risk
classification + rationale; (d) DPIA reference if required; (e) DPO contact;
(f) contestation mechanism.

### 10.2 FP9 — 9 placeholder policy docs (P2)

**D6 exact citation Section 14.4:**

> **Policy docs (per Chunk 8):**
> - `decisions/policy/boundary-discipline.md` (Gap 1)
> - `decisions/policy/trust-tagging.md` (Gap 2)
> - `decisions/policy/sku-pricing-chr.yaml` (Gap 3)
> - `decisions/policy/agent-promotion-chr.yaml` (Gap 3)
> - `decisions/policy/characteristic-space-conventions.md` (Gap 3)
> - `decisions/policy/mereology-edge-types.md` (Rec-05)
> - `decisions/policy/phase-transitions-mht.md` (Rec-06)
> - `decisions/policy/bias-audit-cycle.md` (Rec-03)
> - `decisions/policy/mechanism-introduction.md` (Rec-20)
> - `decisions/policy/multi-method-dispatcher.md` (Rec-21)

**(Note: D6 lists 10 docs in Section 14.4, not 9 per prompt; same gap.)**

References throughout D6 treat these as operational authorities:
- Section 4.3 "proposal, contract, DPA templates — all three carry full
  L/A/D/E Phase 1 (per Day 5-6 rollout)" — relies on boundary-discipline.md
- Section 4.2 "F-G-R trust tags" — relies on trust-tagging.md
- Section 12.10 "bias-audit cycle" — relies on bias-audit-cycle.md

**For compliance audit:** An external auditor following references into
non-existent documents is a trust-erosion event. Even if the rest of D6 is
excellent, unresolved pointer chains signal immaturity.

**Mitigation intensity depends on audience:**

- **Internal-only constitutional doc** (current scope per OT5 + OQ-09 A):
  acceptable P2 if each reference marked "Phase 1 post-D6, ETA YYYY-MM-DD"
- **Shared with external DPO / legal counsel / external DD team:** P1 —
  must complete placeholders before sharing
- **Shared with Mittelstand client during audit:** P1 — hard block

**Verdict: P2.** D6 currently lacks explicit "Phase 1 post-D6 write schedule"
linking each placeholder to a target date.

**Stage C recommendation:** In Section 14.4, reformat:

| Policy doc | Gap/Rec | Status | ETA | Writer |
|---|---|---|---|---|
| boundary-discipline.md | Gap 1 | placeholder | 2026-04-27 | Ruslan+legal |
| trust-tagging.md | Gap 2 | placeholder | 2026-05-04 | Ruslan |
| bias-audit-cycle.md | Rec-03 | placeholder | 2026-05-04 | Ruslan+ethics advisor |
| ... | | | | |

**Minimum:** 10 policy docs + 3 templates need write dates before D6 v1.0
claims "unblocks Stage 4 D1/D2/D3/D4/D5/D7/D8".

### 10.3 FP11 — DORA applicability (P3)

**D6 exact citations:**

- Section 4.4 (line ~674): Regulatory view mentions DORA
- Section 3.4 (line ~506): External supersystem "EU regulatory environment
  (EU AI Act, GDPR, MiCA, DORA)"

Only two mentions, both orienting not operational.

**DORA scope** (Regulation (EU) 2022/2554, effective Jan 17, 2025):
- Applies to 20 categories of financial entities (credit institutions,
  payment service providers, investment firms, insurance, crypto-asset
  service providers, etc.)
- Plus designated **critical ICT third-party service providers** (Art. 31)
  — if providing services to multiple financial entities meeting
  criticality thresholds

**Jetix current direction (ai-consulting-dach):** ICP is Industrial / SaaS /
Professional Services (Section 2.5). Not inherently financial-sector.

**But:** If Jetix pivots or expands to serve financial-sector Mittelstand
(local banks like Sparkassen, Genossenschaftsbanken; regional insurance;
fintech SaaS) → DORA applicability as ICT third-party provider triggers:

- Art. 28-44 contractual arrangements requirements
- Art. 45-49 subcontracting rules
- Art. 50 concentration risk
- Reporting to ESAs
- Register of information (Art. 28(3))

**Verdict: P3 acceptable for Phase 1 ai-consulting-dach primary direction.**
But D6 should flag: *"DORA applicability gates financial-sector client
engagement. Before accepting first financial-sector client contract,
complete DORA Art. 28-44 gap analysis."*

**Stage C recommendation:** Add Section 4.4.2 or Section 12.16 "DORA
Applicability Gate" with explicit pre-conditions for financial-sector
expansion.

### 10.4 Additional findings not in prompt focus

#### 10.4.1 Art. 35 DPIA absent

**No DPIA (Data Protection Impact Assessment) framework** in D6.

Art. 35 GDPR mandates DPIA for high-risk processing. BfDI / Länder DSBs
maintain lists of processing operations requiring DPIA ("muss-Liste").
Common Jetix-relevant triggers:
- Systematic profiling (Jetix audit that profiles employees)
- Large-scale processing special-category data
- Systematic monitoring of publicly accessible area
- Innovative use of new technology (AI!) — specifically flagged by BfDI

**DPIA mandatory before processing starts.** Missing DPIA = Art. 35
violation = Art. 83(4) fine up to €10M or 2% global turnover.

**Verdict P2 (upgrading from not-in-prompt to P2).**

**Stage C recommendation:** Add Section 2.9 or 9.2 "DPIA Framework" —
per-engagement DPIA template; `ops/gdpr-art-35-dpia-template.md` + process.

#### 10.4.2 Art. 30 RoPA absent

Already noted Section 2.5 this review.

**Verdict P3.** Easy fix.

#### 10.4.3 Schrems II TIA absent

Already noted Section 2.6 this review.

**Verdict P2 (US Claude API → Anthropic processing).**

#### 10.4.4 Art. 32 security measures framework absent

Art. 32 GDPR technical-and-organizational measures (TOMs) — the classic
"Schutzziele": Vertraulichkeit, Integrität, Verfügbarkeit, Belastbarkeit,
Pseudonymisierung / Verschlüsselung.

D6 doesn't describe Jetix TOMs. Every DPA template requires TOMs schedule
(Anlage 2).

**Verdict P2.** Expected.

**Stage C recommendation:** Add TOMs reference in Section 4.3 E-lane and
`decisions/policy/tom-security-measures.md` path.

#### 10.4.5 Trade secrets protection (GeschGehG)

Geschäftsgeheimnisgesetz (2019) implementing EU Directive 2016/943. Jetix's
methodology (JETIX-FPF internal) + client confidential info require
"angemessene Geheimhaltungsmaßnahmen" (reasonable protection measures) to
qualify as trade secrets.

**Verdict P3.** Delegation to contracts + HR + ops acceptable.

### 10.5 Critical findings ranked (consolidated)

| Rank | Finding | D6 Section | Verdict | Effort |
|---|---|---|---|---|
| **P1** | FP7 §38 BDSG vs Art. 28 DPA conflation | 2.3 | Factual legal error | 1h |
| **P1** | FP1 EU AI Act risk-tier matrix missing | 4.5, 12.10 | Undefendable Art. 9-15 | 2h |
| **P1** | FP2 CP-5 Art. 22 gate operational depth | 4.5 | Undefendable Art. 22(3) | 3h |
| **P2** | FP6 Art. 33 breach framework absent | 1.3 only | Mittelstand signal gap | 2h |
| **P2** | FP5 F-G-R normative floor table | 4.2, 12.7 | Audit-defensibility floor | 1h |
| **P2** | FP3 Bias-Audit Phase 1 solo — no escalation clause | 12.10 | Escalation protocol missing | 1h |
| **P2** | FP8 Konsenskultur operational DE/AT/CH signals | 4.1 | Mittelstand ergonomic signal | 2h |
| **P2** | FP9 Policy-doc placeholders no ETA | 14.4 | External review blocker | 0.5h |
| **P2** | Art. 35 DPIA framework absent | — | Mandatory pre-processing | 2h |
| **P2** | Schrems II TIA absent | — | US Claude API risk | 1h |
| **P2** | Art. 32 TOMs framework absent | — | DPA Annex 2 required | 1h |
| **P3** | FP4 Regulatory view depth skeleton | 4.4 | Template delegable | 1h |
| **P3** | FP10 ISO 42010 mapping | 4.4 | Vocabulary interop | 0.5h |
| **P3** | FP11 DORA applicability gate | 4.4, 3.4 | Financial-sector expansion | 0.5h |
| **P3** | Art. 30 RoPA absent | — | Documentation obligation | 0.5h |
| **P3** | Art. 13 privacy notice absent | — | Website + sales flow | 1h |
| **P3** | Trade secrets measures | — | Methodology protection | 0.5h |
| **P3** | DE translation for DACH signal | 4.1 | Executive extract | 2h |

**Total P1-P2 effort estimate: ~16-18 hours** of focused writing to bring
D6 v1.0 → v1.1 compliance-defensible.

---

## Section 11 — Strengths to preserve

D6 v1.0 is — compliance lens set aside briefly — an **ambitious and mostly
well-executed constitutional document**. The following elements should be
**preserved verbatim** through Stage C revision:

### 11.1 A.6.B Boundary Discipline L/A/D/E (Section 4.3)

**Best-in-class.** No mainstream Mittelstand consulting shop separates Laws
/ Admissibility / Deontics / Effects in contracts. This is structural
innovation that will pay dividends when facing audit queries like "show me
all statutory obligations bound in this engagement" — answer in seconds,
not days.

### 11.2 F-G-R Trust Calculus surfaced to clients (Section 4.2 CP-2)

**Market-differentiating.** Most consultancies hide confidence levels behind
executive-voice certainty. Jetix surfaces F-G-R explicitly. A client's
Compliance Officer can audit "is this recommendation R-medium or R-certified?"
This is honest, auditable, and rare.

### 11.3 Multi-View Publication mandatory from first delivery (Section 4.4)

**Pre-empts audit friction.** Separating Executive / Technical / Governance /
Regulatory / Internal-learning views means the Regulatory view exists before
the regulator asks for it. Most consultancies scramble to reverse-engineer
regulatory mapping when BfDI writes; Jetix has it at Tag 1.

### 11.4 Attribution hygiene (Section 9.5 + Section 14.9)

Explicit distinction between "FPF" (Levenchuk canonical) and "JETIX-FPF"
(adaptation) prevents IP confusion, signals Urheberrechts-bewusst maturity,
and supports "internal-only" stance per OQ-09 A. Attribution paragraph in
frontmatter is properly formed.

### 11.5 Past-participle state discipline + Hook 4 (Section 5.5)

**Operational rigor.** Forcing past-participle states prevents the classic
"Jira-ticket drift" where state.yaml says `qualifying` forever. Pre-commit
hook enforcement means the discipline survives team scale.

### 11.6 ShSM + FPF cross-pedagogy in U-Types table (Section 8.1)

**Learning-friendly.** The 4-register table (Tech / Plain / Legacy / Mnemonic)
honors SEMAT Essence / ShSM / ArchiMate legacy readers while introducing
FPF Kernel vocabulary. Strong P-2 Didactic Primacy per E.2.

### 11.7 Characteristic-Space formal pricing (Gap 3, Section 12.8)

**Defensible pricing.** A.18 CSLC scales for SKU pricing eliminate magic-
quadrant subjectivity. In Mittelstand Vergabeverfahren, defensible pricing
methodology is a criterion.

### 11.8 FPF-Steward sub-role (Section 5.4)

**Immune system** for ontological discipline. Quarterly audit scope explicit.
This is how a solo founder prevents drift that would otherwise emerge at
scale. Unique Jetix innovation.

### 11.9 Internal-only scope stance (OQ-09 A)

Preserves competitive moat + regulatory freedom. D6 visible only internally
means compliance attention can focus on auditability, not public disclosure
hygiene.

### 11.10 Nested Holonic Structure terminology (OQ-06 B)

Anglicizing "Model D Nested Hierarchy" → "Nested Holonic Structure" aligns
FPF A.1 + A.14 canonical vocabulary. Reduces drift.

**Compliance lens verdict on strengths:** The above 10 elements are what
makes Jetix **professionally differentiated**. The P1-P2 gaps identified in
this review do not invalidate them — they indicate that the operational
floor needs normative clarity. Strengths remain strong after Stage C fixes.

---

## Section 12 — Recommended changes для Stage C

### 12.1 Must-do (P1 — block D6 v1.0 adoption until resolved)

**Stage C.1 — FP7 DPO/DPA separation fix** (1h)

Rewrite Section 2.3 `dpo` row:

```markdown
- `dpo` (Data Protection Officer)
  - **External-mode Phase 1** — engage Datenschutzkanzlei or
    Datenschutz-Beratungsfirma before first client personal-data processing.
  - **Art. 28 DPA capability** (processor template, capable signatory) —
    **Phase 1 readiness; independent of DPO.**
  - **DPO trigger hierarchy** (evaluate at each engagement):
    (a) Art. 37(1)(a) — N/A (Jetix non-public)
    (b) Art. 37(1)(b) — core activity = regular systematic monitoring →
        evaluate per engagement; HR/behaviour audit clients trigger
    (c) Art. 37(1)(c) — Art. 9/10 large-scale data → evaluate per engagement
    (d) §38(1) BDSG — 20+ persons in automated PD processing → **Phase 2b
        headcount trigger**
    (e) §38(1) BDSG — mandatory DPIA (Art. 35) → evaluate per engagement
- `customer-success` (J2 Phase 2a activation)
```

**Stage C.2 — FP1 EU AI Act risk-tier matrix** (2h)

Add Section 4.5.1 "EU AI Act Self-Classification Matrix" with table from
Section 1.1 of this review, plus:
- Retention policy for Art. 12 logs (6-36 month window)
- Per-offering Fundamental Rights Impact Assessment (FRIA) requirement
- GPAI deployer obligations acknowledgment (Art. 29a post-Oct 2024)

Delegate full template to `decisions/policy/eu-ai-act-risk-tier.yaml` with
explicit ETA 2026-04-30.

**Stage C.3 — FP2 CP-5 human-gate operational spec** (3h)

Rewrite Section 4.5 to ~1500 words covering 9 missing elements (see Section
4.1 of this review).

### 12.2 Should-do (P2 — block external review until resolved)

**Stage C.4 — FP6 Art. 33 incident framework** (2h)

Add Section 9 "Incident Response Framework" — 1 page covering Art. 33 GDPR
+ Art. 62 EU AI Act + NIS2/DORA awareness. Reference
`ops/regulatory-incidents/gdpr-art-33-playbook.md` with Phase 1 ETA.

**Stage C.5 — FP5 F-G-R normative floor table** (1h)

Add Section 4.2.1 with floor table (Section 5.1 of this review has draft).
Validity-window defaults in Section 12.7.

**Stage C.6 — FP3 Bias-Audit escalation clause** (1h)

Add Section 12.10.1 "BA-2 Activation Protocol" — "first client requiring
formal Bias Panel triggers BA-2 within 10 business days". Plus Section
12.10.2 "Quarterly aggregation structure" + Section 12.10.3 "Bias Taxonomy
cross-mapping" (REP/ALG/VIS/MET/LNG vs NIST AI RMF vs IEEE 7003).

**Stage C.7 — FP8 Konsenskultur operational DACH** (2h)

Expand Section 4.1 with 4.1.1 (DE conventions), 4.1.2 (AT/CH variations),
4.1.3 (Mittelstand trust-building patterns). Delegate full templates to
`directions/_active/ai-consulting-dach/outreach/de/` + `at/` + `ch/`.

**Stage C.8 — FP9 policy-doc ETAs** (0.5h)

Reformat Section 14.4 table with ETA + writer columns (Section 10.2 of this
review has draft).

**Stage C.9 — DPIA framework** (2h)

Add Section 2.9 "DPIA Framework" per-engagement template. Reference BfDI
Muss-Liste. Integrate with Section 12.10 bias-audit (DPIA + bias-audit
often overlap).

**Stage C.10 — Schrems II TIA + Art. 32 TOMs** (2h)

Section 2.10 "Third-country transfers + Anthropic DPF status verification
schedule". Section 4.3 E-lane: TOMs reference; `decisions/policy/tom-security-measures.md` placeholder with ETA.

### 12.3 Nice-to-have (P3 — post-Stage C)

**Stage C.11 — FP4 Regulatory view skeleton** (1h) — Section 4.4 bullet
list.

**Stage C.12 — FP10 ISO 42010 mapping** (0.5h) — Section 4.4.1 table.

**Stage C.13 — FP11 DORA applicability gate** (0.5h) — Section 4.4.2.

**Stage C.14 — Art. 30 RoPA reference** (0.5h) — Section 2.11.

**Stage C.15 — Art. 13 privacy notice template reference** (1h) — Section
2.8 + link to `ops/gdpr-art-13-privacy-notice-template.md`.

**Stage C.16 — Trade secrets measures** (0.5h) — Section 4.1 or contract
template reference.

**Stage C.17 — DE executive summary appendix** (2h) — 2-3 pages for
Aufsichtsrat / Beirat review.

**Stage C.18 — Internal-code glossary** (0.5h) — Decode OT1-N, P1-N, MCx,
OQ-x at document start for non-technical reviewers.

### 12.4 Total effort summary

| Category | Count | Hours |
|---|---|---|
| P1 (block v1.0 adoption) | 3 | 6h |
| P2 (block external review) | 7 | 10.5h |
| P3 (nice-to-have) | 8 | 6.5h |
| **Total** | **18** | **~23h** |

**Recommended Stage C approach:** Single-pass rewrite targeting P1 + P2 first
(~16 hours), push commit, then P3 in second pass (~6 hours) before
externally-facing use.

### 12.5 Closing recommendation

D6 v1.0 is a **serious constitutional document** with rare ontological depth
and genuine compliance sophistication on key pillars (L/A/D/E, F-G-R,
Multi-View). The gaps identified are **fixable normative clarifications**,
not foundational problems. Specifically:

- The P1 items are **factual errors or operational lacunae in existing
  principles** — write 3-10 pages of additional normative content and the
  document moves to audit-defensible.
- The P2 items are **missing tables and explicit ETAs** — low cognitive
  effort, high external-signal value.
- The P3 items are **interoperability + soft-signal improvements** —
  delegable without blocking.

After Stage C incorporation, D6 v1.1 should **meet or exceed** DACH
Mittelstand external-DPO audit expectations and give a first Audit SKU
client meaningful evidence of compliance posture.

**Critical prerequisite for going live:** All 10 `decisions/policy/*.md`
placeholders (FP9) must be written before first client signs — not because
regulations demand each doc named, but because D6 **references them as
operational authorities**. Empty authorities = broken chain of trust.

---

**END OF REVIEWER 2 — DACH COMPLIANCE CRITIQUE**

*Compiled by claude-opus-4-7 (fresh session, 1M context, extended-thinking-
max), 2026-04-20. No bias from Reviewer 1 / Reviewer 3 / Reviewer 4
(independent lens). Regulatory citations verified against: GDPR (Regulation
(EU) 2016/679), BDSG (Bundesdatenschutzgesetz 2017 as amended), EU AI Act
(Regulation (EU) 2024/1689), DORA (Regulation (EU) 2022/2554), ISO/IEC/IEEE
42010:2022, ISO/IEC 24029-2:2023, IEEE 7003-2024, NIST AI RMF 1.0, WP29
Guidelines on Automated Decision-Making (WP251rev.01), Geschäftsgeheimnisgesetz
2019 (implementing EU Directive 2016/943).*
