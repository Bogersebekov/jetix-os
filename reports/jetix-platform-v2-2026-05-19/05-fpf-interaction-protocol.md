---
type: fpf-interaction-protocol
date: 2026-05-19 noon Berlin
session: jetix-platform-v2-description-2026-05-19
phase: 4
status: brigadier-scribe-surface
prose_authored_by: brigadier-scribe (voice-anchor-derived)
cells_dispatched:
  - eng × scalability (protocol stack design)
  - sys × cybernetics (feedback loops + dispute resolution)
voice_anchors:
  - text_010 §1 «по сути вот fpf язык да блять и то что они на этой платформе вот как бы встречаются и могут там на честно прозрачно блять обмениваться получаться ресурсами работать над сложными проектами»
constitutional_posture: R1 + R6 + R11 + R12 + IP-1 + EP-5
extends:
  - decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md (mode negotiation)
  - design/JETIX-FPF.md (FPF constitutional spec)
---

# Phase 4 — FPF Interaction Protocol

> Per Ruslan (text_010 §1): «FPF язык да... на этой платформе встречаются и могут на честно прозрачно обмениваться ресурсами». FPF as universal protocol stack — registration → matching → transaction → audit → dispute → R12 enforcement.
> FPF lens D primary (Bounded Context Bridge).

---

## §0 Protocol stack overview

| Layer | FPF primitive | Function | Phase 1 actors | Phase 2 resources |
|-------|---------------|----------|----------------|-------------------|
| **L1 Identity** | A.1.1 Bounded Context | Identity + FPF profile | ALL | R8 (skills) + R12 (reputation) |
| **L2 Promise** | U.PromiseContent | Resource offer + ask | ALL | ANY (R1-R32) |
| **L3 Match** | A.6.B Bridge + matching algo | Offer-ask matching | Connectors (Cat 14) | R13 (network) |
| **L4 Commitment** | A.2.8 Commitment | Commitment artefact | offer-ask pair | R6/R8/R10 etc. |
| **L5 Execution** | A.15 Work | Resource exchange + work | offer + ask | (committed resource) |
| **L6 Audit** | B.3 F-G-R + provenance | Truth verification | ALL | R12 (reputation update) |
| **L7 Dispute** | U.SpeechAct + arbitration | Conflict resolution | dispute panel | R12 + R11 (status check) |
| **L8 R12 Enforcement** | E.5 Guard-Rails | Anti-extraction discipline | Foundation governance | R32 (meaning) + R12 |

Eight layers; each operates per FPF discipline. Protocol layered stack — like TCP/IP for resource exchange.

---

## §1 L1 — Identity + FPF Profile Registration

### §1.1 Registration mechanism

Participant registers via:
1. **Identity claim** (basic — email + verified handle; not full ID per privacy)
2. **FPF profile** (FPF U.SkillSet over Phase 1 categories — self-attested + optional peer-attested)
3. **Bounded Context declaration** (A.1.1) — what domain, what project-set
4. **F-G-R credibility seed** (initial reliability = R-low per B.3; compounds via L6 audit)

### §1.2 Profile attributes (FPF-formal subset)

```yaml
participant_profile:
  identity:
    handle: <verified>
    contact: <verified>
    pgp_key: <optional>
    sbt_addresses: <optional — Phase 7 SBT issuance>
  fpf_profile:
    categories: <Phase 1 subset — multi-class possible>
    bounded_context: <free-text + tags>
    skills: <FPF U.SkillSet — self + peer attestations>
    methodology_fluency: <FPF-fluency / IWE-fluency / VSM-fluency / etc.>
  resources:
    offers: <Phase 2 R1-R32 subset; with bandwidth>
    asks: <Phase 2 R1-R32 subset; with priority>
  f_g_r_score:
    formality: <F-low / F-mid / F-high — recent updates>
    group_scope: <single-domain / cross-domain / institutional>
    reliability: <R-low / R-mid / R-high>
  charter_acks:
    r12_charter: <accepted | declined>  # required for participation
    fpf_discipline_charter: <accepted>
    ip_1_acknowledgement: <accepted>
```

### §1.3 Privacy + portability

- Participant data minimised (R12 alignment — no extraction)
- Profile portable (export-anytime; fork-and-leave per R12)
- Public-private toggle per attribute (transparent but not exhibitionist)
- No biometric / sensitive PII required (operationally avoidable)

### §1.4 IP-1 STRICT

Identity confirmation = automated (substrate); but **role assignment + cohort acceptance = human-decided** (cohort governance). [src: Recursive Engine 2026-05-18]

---

## §2 L2 — Offers + Asks (U.PromiseContent)

### §2.1 Offer format

**FPF-formal layer (machine-readable):**

```yaml
offer:
  offerer: <participant_id>
  resource: <R1-R32>
  sub_type: <e.g. "mentorship/technical/ML">
  bandwidth:
    quantity: <hours / amount>
    duration: <one-off / weekly / monthly / sustained>
  conditions:
    bounded_context: <FPF A.1.1 scope>
    skill_requirements: <FPF U.SkillSet expected of ask-er>
    r12_constraints: <participant-set R12 covenants>
  motivation: <FPF U.SpeechAct — why offering>
  validity: <until-date OR continuous>
```

**Plain-English layer (human-readable):**

«Я предлагаю 5 часов в месяц mentorship по ML-design к проектам Tier 2+ hackathon. Условия: участник должен иметь опыт прототипирования. Срок: до конца Q1 2027.»

**Dual representation** is required (per FPF B.5.1 explore + bilateral readability).

### §2.2 Ask format

**FPF-formal:**

```yaml
ask:
  asker: <participant_id>
  resource: <R1-R32>
  sub_type: <e.g. "compute/gpu/training">
  required_quantity: <hours / amount>
  required_quality: <description>
  willing_to_offer_in_return: <R1-R32 subset; can be R12 reciprocal>
  context: <bounded context + project>
  priority: <low / medium / high>
  validity: <date>
```

**Plain-English:**

«Ищу 100 GPU-hours для эксперимента ML-cohort-substrate. В обмен предлагаю: документация результатов + co-authorship + presentation at T2 hackathon. Срок: до 2026-08-31.»

### §2.3 Validity discipline

- Offers / asks expire (no zombie-listings)
- Modifications version-tracked (FPF append-only)
- Revocation possible (fork-and-leave preserved); but tracked в reputation history

### §2.4 R12 alignment per offer/ask

Each offer/ask MUST clear R12 audit:
- Offer not exploitative (e.g. «100 hours volunteer mentorship for $0» = check that mentor consents AND offer not made under coercive pressure)
- Ask not extractive (e.g. asking «all your IP for 1 hr consulting» = DECLINE)
- Reciprocity transparent (not «free» if commercial value generated)

---

## §3 L3 — Matching (A.6.B Bridge + algorithm)

### §3.1 Matching mechanisms (3 modes)

**Mode A — Algorithmic matching:**
- Participant offers + asks → algorithm surfaces candidate matches per FPF compatibility
- Bounded context overlap (FPF A.1.1)
- Skill complementarity (U.SkillSet matching)
- Resource bidirectionality (does offerer's offer match asker's ask?)
- F-G-R reliability compatibility (both parties accept partner reliability tier)

**Mode B — Curator-mediated:**
- Phase 1 Cat 14 (Connectors) suggest matches based on judgment
- Useful когда algorithmic match incomplete (cross-domain, novel collaboration patterns)
- Curator-introduced matches tracked as separate cohort (compound network effect)

**Mode C — Manual / serendipity:**
- Participants browse offers/asks directly
- Community-meetup matchings
- Event-based matchings (hackathon cohorts forming teams)

**Default:** combine all three modes; algorithm surfaces; curators amplify; manual fills gaps.

### §3.2 Matching algorithm fairness

- No bias-amplification (audit per Phase 1 category counts)
- T1 / new participants priority-boost (avoid Matthew effect)
- Cross-domain matches encouraged (diversity-bonus)
- R12 alignment: matching НЕ optimises Jetix-extraction; optimises participant-outcome

### §3.3 IP-1 STRICT

Matching algorithm = substrate-pre-authorized (per pre-published rules); but **major algorithm changes require human ack** (cohort governance). Edge cases escalate. [src: Recursive Engine 2026-05-18]

---

## §4 L4 — Commitment (A.2.8)

### §4.1 Commitment formation

Match → both parties agree → **FPF A.2.8 Commitment artefact created**:

```yaml
commitment:
  parties: [<offerer_id>, <asker_id>]
  offer_ref: <offer_id>
  ask_ref: <ask_id>
  agreed_terms:
    quantity_delivered: <updated from offer>
    timeline: <agreed-by-both>
    quality_criteria: <FPF F-G-R verifiable claims>
    reciprocity_terms: <what asker offers in return>
    r12_compliance: <verified>
  signed_at: <ISO-8601>
  signatures: [<offerer_sig>, <asker_sig>]
  bounded_context: <project + duration>
  audit_trail_pointer: <commitment-log entry>
```

### §4.2 Modification / cancellation

- Modifications require both-party ack (FPF U.SpeechAct exchange)
- Cancellation possible но tracked (reputation history — both parties)
- Force-majeure (illness, crisis) honored без reputation penalty (per cohort norms; case-by-case curator review)

### §4.3 R12 alignment

- Commitment cannot create indefinite obligation (max-duration commitment per cohort norms)
- Fork-and-leave preserved (party can exit per agreed exit conditions)
- No «golden handcuffs» — terms NOT structured to prevent exit

---

## §5 L5 — Execution (A.15 Work)

### §5.1 Execution mechanism

Committed resources flow:
- Time / mentorship → calendar booking + meeting cadence
- Compute → cloud-credit allocation
- Money → transfer / escrow (multi-sig for large amounts)
- IP / Code → repository contribution + license clarity
- Skills / methodology → workshop sessions / pairing

### §5.2 Progress tracking

- Milestones (FPF A.15 sub-tasks)
- Periodic check-ins (FPF U.SpeechAct status)
- Asynchronous progress reports

### §5.3 Failure handling

- Slippage flagged early (FPF discipline — surface deviation per acceptance predicate)
- Escalation path: L4 commitment modification OR L7 dispute
- Force-majeure clauses documented

### §5.4 IP-1 STRICT

Execution = substrate facilitates; participants execute. Jetix NOT in execution chain (humans decide what to deliver, how). [src: Recursive Engine 2026-05-18]

---

## §6 L6 — Audit (F-G-R + provenance)

### §6.1 Audit-trail discipline

All L1-L5 actions emit audit-trail entries (append-only):

```yaml
audit_entry:
  timestamp: <ISO-8601>
  actor: <participant_id | substrate-auto>
  action_type: <register | offer | ask | match | commit | deliver | dispute>
  ref: <offer/ask/commitment/dispute id>
  metadata:
    bounded_context: <scope>
    f_g_r:
      formality: <F2-F8>
      group_scope: <participant_set>
      reliability: <R-low / R-mid / R-high>
    provenance: <source citations>
```

### §6.2 Reputation update mechanism

- Successful commitment completion → both parties' F-G-R reliability incremented
- Failed commitment (uncontested fault) → reliability decremented
- Disputed completion (L7) → reliability frozen pending arbitration
- Cohort-vote weight per reliability tier (но no permanent disenfranchisement; R12 fork-and-leave)

### §6.3 Public-private audit visibility

- Default-private (participant data minimised per R12)
- Aggregated statistics public (cohort-level reputation distribution)
- Per-participant audit history shareable on opt-in (e.g. CV-substrate)

### §6.4 IP-1 STRICT

Audit-trail emission = substrate-automated; but **interpretation of audit entries (e.g. «is this performance failure?») = human-decided** (cohort governance + dispute panel). [src: Recursive Engine 2026-05-18]

---

## §7 L7 — Dispute Resolution (U.SpeechAct + Arbitration)

### §7.1 Dispute types

- Performance failure (committed resource not delivered)
- Quality failure (delivered but below agreed criteria)
- R12 violation alleged (extractive behaviour by counterparty)
- Reciprocity failure (asker received but failed to reciprocate)
- Boundary violation (FPF A.1.1 bounded context breach)

### §7.2 Dispute mechanism

**Tier 1 (informal):**
- Parties attempt direct resolution (FPF U.SpeechAct exchange)
- Curator (Cat 14 Connector who knows parties) mediates if requested
- 1-2 week resolution window

**Tier 2 (formal):**
- 3-person arbitration panel (FPF-fluent; not parties' close networks)
- Evidence submission (audit-trail entries + party statements)
- Panel deliberation (FPF-discipline; F-G-R verifiable claims)
- Decision rendered + audit-trail entry
- Decisions appealable to cohort governance Tier 3

**Tier 3 (governance):**
- Foundation governance / cohort vote on appealed Tier-2 decisions
- Rare (most disputes resolved Tier 1-2)

### §7.3 Outcomes

- Performance ack (reputation restoration / penalty)
- Restitution (resource replacement / refund)
- Cohort-temporary suspension (R12 violation grade)
- Cohort-permanent removal (severe R12 violation — extraction, R12 evasion)
- Fork-and-leave (any party can exit; preserves R12)

### §7.4 R12 violation handling (special)

- R12 violations = HIGH-priority dispute
- Default-Deny per `.claude/config/default-deny-table.yaml` constitutional_never_list
- Halt-Log-Alert per Pillar C Tier 2 R11
- Foundation governance review mandatory
- Severe R12 violations trigger Ruslan ack (Pillar A Tier-1 escalation)

### §7.5 IP-1 STRICT

Dispute panel = humans (NOT Jetix substrate); decisions = human verdicts; substrate provides infrastructure + audit-trail access. [src: Recursive Engine 2026-05-18]

---

## §8 L8 — R12 Enforcement (Anti-Extraction)

### §8.1 R12 substrate enforcement (4 mechanisms)

Per `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` Ruslan ack 2026-05-18:

**Mechanism 1 — Mondragón wage-ratio cap.** Within cohort governance, max compensation ratio (founder ↔ junior contributor) capped (e.g. 6:1 baseline per Mondragón). Enforced via Phase 7 monetization R12 audit gate.

**Mechanism 2 — Quadratic Funding revenue distribution.** Per [Plurality / Glen Weyl mechanism], revenue distribution weighted by quadratic-vote per cohort member. Prevents whale-extraction.

**Mechanism 3 — Fork-and-leave exit tokens.** Participants hold exit-tokens (SBT-bound) that enable cohort-exit with proportional asset claim. No participant locked-in.

**Mechanism 4 — Default-Deny constitutional_never_list.** 4 RUSLAN-LAYER action classes in `.claude/config/default-deny-table.yaml`:
- `extraction_beyond_share`
- `wage_ratio_violation`
- `non_consensual_distribution`
- `fork_prevention_attempt`

All four = Halt-Log-Alert per Pillar C Tier 2 [src: `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md`].

### §8.2 R12 audit cadence

- Per-offer / per-ask R12 quick-check (L2 + L4)
- Quarterly cohort-level R12 audit (compensation ratios + revenue distribution + fork-and-leave health)
- Annual full R12 audit (Foundation governance)
- Continuous Halt-Log-Alert on violation trigger

### §8.3 Programmable Ethereum overlay (Phase 2+ deferred)

- Phase 2+ overlay binds R12 to smart contracts
- Per Cohort opt-in (per Charter)
- Substrate-default R12 enforcement initially via cohort governance + Foundation; later programmable Ethereum
- Not Phase 1 substrate (deferred per acked plan)

[src: `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md`]

### §8.4 IP-1 STRICT

R12 enforcement = constitutional rule (NOT discretionary Jetix decision); Default-Deny per Pillar C Tier 2 candidate rule 12 (LOCKED 2026-05-12). Substrate executes enforcement; humans (Foundation governance + Ruslan) define + tune parameters.

---

## §9 Mode negotiation (System Merger Protocol cross-ref)

Per `decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md`, FPF protocol supports 3 modes for cross-system / cross-organisation interactions:

### §9.1 Mode 1 — Full-FPF (default within Jetix)

- All FPF primitives accessible (FPF discipline learned)
- F-G-R verifiable claims
- High-trust environment
- Within-cohort default

### §9.2 Mode 2 — Partial-FPF (bridge with FPF-aware partners)

- Subset of FPF primitives supported
- Mapping to partner's vocabulary
- Mid-trust environment
- Cross-cohort / cross-community bridges (e.g. Cat 20 communities adopting partial-FPF)

### §9.3 Mode 3 — Opaque-bridge (interface with non-FPF partners)

- Translation layer between FPF and partner's protocol
- Limited FPF features (transactional minimum)
- Low-trust assumed; explicit boundary
- Most corporate (Cat 16) / government (Cat 17) interactions

**Mode negotiation:** at L3 matching, mode determined by both parties' FPF-fluency level. Stored in commitment metadata.

[src: System Merger Protocol 2026-05-18]

---

## §10 Operational scenario examples

### §10.1 Scenario A — Mentor-mentee match (T1 hackathon)

1. **L1:** ML engineer (Cat 1) registers; profile includes mentorship offer (R10; 3 hrs/month T1-T2 events)
2. **L2:** T1 hackathon participant (Cat 1 entering) submits ask for ML-design mentor
3. **L3:** Algorithmic match suggested; both accept
4. **L4:** Commitment artefact created — 3 hours over 4 weeks, FPF F-G-R mentor discipline
5. **L5:** Mentor delivers 3 hrs; participant submits artefact + F-G-R reflection
6. **L6:** Both report completion; reputation updated (+R12 for both)
7. **L7:** No dispute
8. **L8:** R12 check — voluntary on both sides, reciprocity transparent ✓

Outcome: cohort-level R12 + reputation compound. Both parties available for T2 cohort.

### §10.2 Scenario B — Corporate sponsorship (T4 hackathon)

1. **L1:** Anthropic (Cat 16) registers institutional profile (FPF mode 3 — opaque-bridge); cohort governance reviews acceptance
2. **L2:** Anthropic offers compute credits (R2; €500K equivalent) + judge participation
3. **L3:** Matched к T4 cohort (curator-mediated); R12 alignment audited
4. **L4:** Commitment artefact — multi-year terms reviewed by Cat 9 (Legal); Mondragón ratio + fork-and-leave verified
5. **L5:** Compute credits allocated to T4 cohort; Anthropic judges participate
6. **L6:** Audit-trail emission; cohort + Anthropic reputation updated
7. **L7:** No dispute
8. **L8:** R12 check — Anthropic acceptance of R12 charter pre-execution; quarterly audit

Outcome: T4 cohort + Anthropic partnership compounds; Mode 3 opaque-bridge demonstrates feasibility.

### §10.3 Scenario C — R12 violation dispute

1. Participant alleges: «counterparty extracted IP beyond agreed share»
2. L7 Tier 1: informal mediation fails
3. L7 Tier 2: arbitration panel reviews audit-trail; counterparty's behaviour confirmed violation
4. L8: Halt-Log-Alert triggered; severe R12 violation grade
5. Foundation governance review; Ruslan ack required (Pillar A Tier-1 escalation)
6. Decision: counterparty removed from cohort; restitution ordered; SBT cohort-membership revoked (но fork-and-leave preserved — they leave with their work-product)
7. Audit-trail entry permanent; cohort awareness sustained

Outcome: R12 enforcement demonstrated; cohort trust preserved; FPF discipline reinforced.

---

## §11 Protocol metrics + observability

| Metric | Target | Failure trigger |
|--------|--------|------------------|
| Profile registration completion | >90% within 1 week | <60% = UX broken |
| Offer/ask validity rate | >85% | <60% = listing-hygiene broken |
| Matching algo accuracy (parties accept match) | >50% | <25% = algorithm broken |
| Commitment-completion rate | >80% | <60% = cohort-engagement broken |
| Dispute rate / total commitments | <5% | >15% = trust substrate broken |
| R12 violation rate / quarter | <0.5% | >2% = enforcement broken |
| Audit-trail emission lag | <60s | >5min = substrate broken |

---

## §12 IP-1 STRICT summary (per layer)

| Layer | Substrate auto | Human decision required |
|-------|----------------|--------------------------|
| L1 | Identity validation, profile storage | Cohort acceptance |
| L2 | Offer/ask publication, validation | Acceptance criteria changes |
| L3 | Algorithmic suggestion | Match acceptance (both parties) |
| L4 | Commitment artefact creation | Terms agreement |
| L5 | Execution facilitation | Project decisions |
| L6 | Audit-trail emission | Audit-entry interpretation |
| L7 | Dispute infrastructure | Dispute resolution verdicts |
| L8 | R12 enforcement automation | R12 parameter tuning |

All Jetix-automated actions = pre-authorized per published rules; all human-required actions = Default-Deny without human ack. ✓

---

## §13 Cross-references

- voice anchors text_010 + text_011
- `decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md` (mode negotiation)
- `decisions/strategic/JETIX-RECURSIVE-SELF-DEVELOPMENT-ENGINE-2026-05-18.md` (IP-1 STRICT substrate)
- `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` (R12 substrate)
- `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` (H8 trust substrate)
- `design/JETIX-FPF.md` (FPF constitutional spec)
- `swarm/wiki/foundations/principles/architecture.md` (Pillar C Tier 2)
- `.claude/config/default-deny-table.yaml` (constitutional_never_list 11+4 entries)
- Phase 1-3 cross-refs

---

*Phase 4 closure. 8-layer FPF protocol stack operational spec. Identity → Promise → Match → Commitment → Execution → Audit → Dispute → R12 Enforcement. Mode negotiation (full/partial/opaque-bridge). Operational scenarios. IP-1 STRICT per layer. Mermaid flow в `diagrams/04-fpf-interaction-protocol-flow.md` (Phase 9).*
