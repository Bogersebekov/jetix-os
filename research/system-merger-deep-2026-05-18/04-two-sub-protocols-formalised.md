---
type: research-phase-3
phase: 3
date: 2026-05-18 evening
session: system-merger-deep-research-2026-05-18
cells: eng × scalability + phil × critic
constitutional_posture: R1 + R6 + R11 + EP-5
word_budget: 3500
F: F3
G: two-sub-protocols-namordnik-usbcport
R: refuted_if_namordnik_<10_constraints_OR_usbcport_modes_missing_OR_ashby_misapplied_OR_failure_modes_uncatalogued
---

# Phase 3 — Two Sub-Protocols Formalisation

> «Намордник» (constraint imposition) + «USB-C порт переделка» (interop bridge).
> Per text_009 Thread 10 ¶9 voice anchor + cybernetic + DDD bounded-context frame.

---

## §A. «Намордник» (Constraint Imposition Sub-Protocol)

### §A.1 Definition

**Намордник** = explicit set of constraints the **host system** requires the **incoming system**
to accept as a precondition of merger. Cybernetic frame: Ashby Law of Requisite Variety — host's
**constraint variety** ≥ incoming's **behavioural variety** to absorb without identity loss.

> **Etymology (voice anchor):** text_009 Thread 10 ¶9 verbatim Ruslan idiom — «надевание намордников».
> The metaphor: muzzle constrains behaviour without eliminating animal/system identity.

### §A.2 Cybernetic foundation — Ashby Requisite Variety

- **W. Ross Ashby, "Introduction to Cybernetics" 1956, Ch. 11** [src: Ashby 1956 Chapman & Hall, Ch.11 "Requisite Variety":retrieved 2026].
- **Theorem:** "Only variety can destroy variety." If a system R is to regulate a system D, R must have at least as many states (variety) as D — otherwise some D-states are unregulated.
- **Application to merger:** Host = R (regulator); Incoming = D (regulated). Host's constraint set must enumerate ≥ N states where N = behavioural variety of incoming system relevant to merger boundary.
- **Failure mode:** if constraint catalog is too sparse → incoming behaviours emerge that host cannot regulate → R12 violations, governance escapes, extractive patterns leak across boundary.
- **Failure mode:** if constraint catalog is too dense → incoming cannot operate; merger collapses to absorption (loss of variety; symbiosis impossible per §A integration mode).

**Sweet spot:** N constraints sufficient to cover R12 + IP-1 + F-G-R + audit baseline, ≤ N where incoming retains operational autonomy. Hypothesis (H-SM-11): N ≈ 10-20 constraints covers 80% of merger scenarios.

### §A.3 Constraint catalog (10 baseline constraints)

Per concept doc C §3.1 + ROY Pillar C Tier-2 + Mondragón federation patterns:

| # | Constraint | Definition | Enforcement | Violation detection | Resolution |
|---|---|---|---|---|---|
| **C1** | R12 anti-extraction | No extraction beyond agreed share; Mondragón ratio cap; fork-and-leave exit available | Smart contract (Ethereum overlay Option D Hybrid) | On-chain ratio monitor + audit trail | Smart contract clawback; if persistent → de-merge |
| **C2** | FPF F-G-R discipline | Per claim Formality / Group-scope / Reliability marker | Lint at promotion to canonical | F-G-R missing or stale (>180d) | Halt-Log-Alert F4; re-attest required |
| **C3** | Append-only history | No deletion / rewrite of merger artefacts | Git history + audit pre-commit hook | History rewrite attempted | Halt-Log-Alert F8 (constitutional); merger paused |
| **C4** | Default-Deny novel actions | Novel cross-boundary action classes require classification | Categorize at `.claude/config/default-deny-table.yaml`-equivalent merger table | Uncategorized action attempted | Deny + escalate to FPF-Steward |
| **C5** | Constitutional posture acceptance | Both systems agree A.14 alignment + E.5 guard-rails | Signed cryptographic commitment Day-0 | Subsequent A.14 violation | Sandbox affected sub-system; remediation cycle |
| **C6** | Audit trail commitment | All merger-affecting decisions traceable in shared substrate | Append-only event log (chain-anchored) | Off-record decision detected | Surface, attribute, demand re-record |
| **C7** | R1 sole-strategist binding (if applicable) | Strategic prose authored by named human(s); never AI-autonomous | Per claim `prose_authored_by:` markers | AI-authored strategic prose absent attribution | Halt-Log-Alert; rollback strategic claim |
| **C8** | IP-1 Role≠Executor | Foundation roles are abstract types; executors are RUSLAN-LAYER bindings | Schema validation on merger contracts | Role-name conflated with executor identity | Reject merger contract; require restructure |
| **C9** | Open-source default | Merger artefacts default to open-source unless explicit exception | License audit at promotion | Closed-source artefact in merger boundary without exception | Demand exception filing + Ruslan ack |
| **C10** | Fork-and-leave exit available | Either party can exit merger without penalty within N-day window per exit token policy | Exit token contract holds | Exit token claim attempted blocked | Constitutional violation F8; merger forcibly de-merged |

**Append-only:** Additional constraints (C11+) can be appended per specific merger context (e.g., GDPR compliance for EU mergers; SOC2 for enterprise B2B; ISO 27001 for security-critical).

### §A.4 Enforcement layer architecture

Three tiers:

**Tier 1 — Cryptographic (smart contract, fully automated):**
- C1 (R12 ratio cap)
- C10 (fork-and-leave exit tokens)
- C6 (audit chain anchoring)

**Tier 2 — Lint / Schema (machine-checked, semi-automated):**
- C2 (F-G-R discipline)
- C3 (append-only — git hook)
- C4 (Default-Deny table validation)
- C7 (`prose_authored_by` schema)
- C8 (IP-1 Role≠Executor schema)

**Tier 3 — Audit / Governance (human-in-loop, periodic):**
- C5 (constitutional posture review — quarterly)
- C9 (open-source default exceptions — quarterly)

### §A.5 Violation severity matrix (F-grade alignment)

| Grade | Severity | Examples (constraints) | Response time | Response action |
|---|---|---|---|---|
| **F8** | Constitutional | C3, C5 (rewriting history; constitutional violation) | ≤1 second | Halt; immediate alert; de-merge candidate |
| **F4** | High | C1 ratio breach, C10 exit blocked, C7 R1 violation | ≤5 seconds | Halt-Log-Alert; sandbox affected sub-system |
| **F2** | Medium | C2 F-G-R stale, C8 role/executor conflation | ≤60 seconds | Log + remediation cycle |
| **F0** | Low | C9 license audit drift | Periodic audit | Surface + correction request |

### §A.6 Compliance audit cadence

- **Continuous (Tier 1):** smart contract on-chain.
- **Daily (Tier 2):** lint hook on promote.
- **Quarterly (Tier 3):** human governance review (FPF-Steward + ROY swarm + Ruslan).
- **Annual:** full constraint catalog re-attestation.

### §A.7 Failure mode catalog (намордник sub-protocol)

| FM-# | Failure mode | Cause | Detection | Mitigation |
|---|---|---|---|---|
| **FM-N1** | Constraint catalog under-specified (Ashby variety insufficient) | Host underestimated incoming behavioural variety | Post-merger emergent violations | Append constraints (audit-driven); de-merge if catastrophic |
| **FM-N2** | Constraint catalog over-specified (incoming cannot operate) | Host imposed constraints incompatible с incoming domain | Operational paralysis; pilot project fails | Negotiate exceptions; relax non-constitutional constraints |
| **FM-N3** | Smart contract bug enables silent extraction | Code defect | On-chain monitor + independent audit | Pause contract; patch; re-deploy; payouts retroactive |
| **FM-N4** | Off-chain extraction undetected | Constraint applies on-chain only | Off-chain accounting audit | Demand on-chain anchoring of critical metrics |
| **FM-N5** | Governance capture (FPF-Steward compromised) | Single point of failure in audit | Distributed FPF-Steward role; ROY swarm cross-check | Multi-sig on constitutional changes |
| **FM-N6** | Exit token unenforceability (incoming jurisdiction refuses) | Legal-substrate mismatch | Pre-merger legal due diligence | Co-jurisdictional escrow; arbitration clause |

---

## §B. «USB-C порт переделка» (Interop Bridge Sub-Protocol)

### §B.1 Definition

**USB-C порт** = the **translation / bridge layer** that allows incoming system's native data /
role / commitment / artefact representations to be re-expressed in FPF's universal merger
language, and vice versa. Per FPF A.6.B Bounded Context Bridge primitive + Eric Evans DDD
Anti-Corruption Layer (ACL).

> **Etymology (voice anchor):** text_009 Thread 10 ¶9 — «переделки порта блять под юсб си».
> Metaphor: physical connector retrofit makes any device universally interoperable.

### §B.2 DDD foundation — Anti-Corruption Layer

- **Eric Evans, "Domain-Driven Design: Tackling Complexity in the Heart of Software" 2003, Ch. 14** [src: Evans 2003 Addison-Wesley, "Bounded Context" + "Anti-Corruption Layer":retrieved 2026].
- **Anti-Corruption Layer (ACL):** translation layer between two bounded contexts that protects the host model from incoming model's conceptual contamination.
- **Strategic design patterns relevant:** Shared Kernel (high overlap; risky), Customer-Supplier (asymmetric coupling), Conformist (incoming submits), Anti-Corruption Layer (defensive translation), Open Host Service (host publishes protocol; this is the FPF analog), Published Language (formal interchange spec; FPF itself).
- **FPF positioning:** Open Host Service (host) + Published Language (FPF) + Anti-Corruption Layer (incoming side).

### §B.3 Translation rule format (formal spec)

**Per merger entity-class, translation rule:**

```yaml
rule_id: TR-<merger_slug>-<entity_class>-<version>
incoming_term: <native term in incoming system>
fpf_term: <FPF primitive or U.* concept>
translation:
  direction: bidirectional | incoming→fpf | fpf→incoming
  function: <pure function or lookup-table>
  invariants:
    - <invariant 1>
    - <invariant 2>
  failure_mode: <what happens on translation failure>
provenance:
  authored_by: <human-or-attributed>
  attested_at: <ISO 8601>
  F: F2 | F3 | F4 | F8
```

**Example (hypothetical):**

```yaml
rule_id: TR-acmeAI-jetixFPF-Person-v1
incoming_term: "User" (AcmeAI internal model)
fpf_term: U.Performer (FPF role primitive)
translation:
  direction: bidirectional
  function: User.id ↔ Performer.role_binding; User.email ↔ Performer.contact_handle
  invariants:
    - 1:1 mapping (no User maps to >1 Performer)
    - acting_as field on Performer derived from User.team_label
  failure_mode: log + halt translation; surface to FPF-Steward
provenance:
  authored_by: ruslan + acmeai-eng-lead
  attested_at: 2026-06-15T10:00:00Z
  F: F3
```

### §B.4 Mode negotiation (USB-C CC-pin analog)

Three modes available during Phase 1 Discovery:

#### Mode FULL-FPF
- Incoming system fully adopts FPF primitive set internally.
- Maximum interop; minimum overhead long-term.
- Maximum disruption to incoming short-term.
- **Use case:** incoming system is small, greenfield, or already FPF-curious.

#### Mode PARTIAL-FPF (translation-bridge)
- Incoming retains native model; ACL translates at boundary.
- Medium interop; ongoing translation overhead.
- Lower disruption; mid-term migration possible.
- **Use case:** incoming is mid-sized with significant legacy; high pragmatism.

#### Mode OPAQUE-BRIDGE
- Incoming exposes minimal interface; host treats as black-box service.
- Minimal interop; maximum encapsulation.
- Minimum disruption to incoming.
- **Use case:** incoming is highly proprietary, regulated, or has irreconcilable native model (e.g., banking core systems).

**Negotiation protocol:** Phase 1 Discovery includes mode declaration. Mode can be upgraded over time (OPAQUE → PARTIAL → FULL) but not silently downgraded.

### §B.5 Performance characterisation

**Overhead estimates (hypotheses, refutable):**

| Mode | Compute overhead per cross-boundary call | Maintenance burden | Drift risk |
|---|---|---|---|
| FULL-FPF | ~0% (native) | High initially; low after migration | Low |
| PARTIAL-FPF | 5-15% (translation step) | Medium ongoing | Medium |
| OPAQUE-BRIDGE | 0-2% (thin wrapper) | Low | High (semantic drift) |

**Hypothesis (H-SM-12):** PARTIAL-FPF translation overhead <10% acceptable for first 5 mergers; if >20% → bridge sub-protocol redesign required.

### §B.6 Backward compatibility

- **Fork-and-leave preserved:** USB-C bridge does NOT bind incoming to host indefinitely; can exit via constraint C10 (намордник).
- **Mode downgrade requires merger event** (FULL→PARTIAL = formal de-integration step, governance-gated).
- **Versioning:** translation rules carry semver; breaking changes = new merger event sub-phase.

### §B.7 Audit hooks

Every cross-boundary call generates audit event:

```jsonl
{"timestamp": "2026-06-15T10:00:00Z", "rule_id": "TR-acmeAI-jetixFPF-Person-v1", "direction": "incoming→fpf", "input_hash": "...", "output_hash": "...", "translation_latency_ms": 3, "F": "F3"}
```

**Append-only event log** anchored to chain per audit cadence (e.g., Merkle-root every 1000 events committed on-chain).

### §B.8 Failure mode catalog (USB-C порт sub-protocol)

| FM-# | Failure mode | Cause | Detection | Mitigation |
|---|---|---|---|---|
| **FM-U1** | Translation rule missing for entity class | Discovery phase missed entity | Cross-boundary call rejected | Add rule; halt affected workflow until rule attested |
| **FM-U2** | Translation rule wrong (semantic mismatch) | Misunderstood domain mapping | Pilot project errors; audit findings | Revise rule; surface as F4-grade; provenance updated |
| **FM-U3** | Bidirectional translation lossy | Information not preserved in both directions | Round-trip test fails | Accept loss + document; or split into uni-directional rules |
| **FM-U4** | Performance overhead > budget (>20%) | Translation function inefficient | Profiling | Optimize; or upgrade incoming to FULL-FPF |
| **FM-U5** | Mode silently downgraded | Misimplementation | Audit log review | Halt; remediate; F8 if intentional |
| **FM-U6** | OPAQUE-BRIDGE semantic drift | Black-box incoming behaviour evolves | Mismatch in expected outputs | Force PARTIAL-FPF upgrade or de-merge |
| **FM-U7** | ACL pattern leaks (incoming model contaminates host) | ACL discipline failure | Code review; static analysis | Restore ACL boundary; refactor host model if contaminated |

---

## §C. Symmetric pair — why both sub-protocols are needed

| Aspect | Намордник (constraint) | USB-C порт (interop bridge) |
|---|---|---|
| **Primary direction** | Host → Incoming (impose) | Bidirectional (translate) |
| **Domain layer** | Constitutional / commitment | Data / model / artefact |
| **Cybernetic role** | Regulator (Ashby) | Translator (DDD ACL) |
| **Enforcement** | Cryptographic + lint + audit | Schema + audit hooks |
| **Failure consequence** | R12 violation; ext extraction; constitutional damage | Data corruption; semantic mismatch; operational errors |
| **Time horizon** | Persistent (lifetime of merger) | Persistent + version-evolving |
| **Cross-precedent analog** | TCP/IP RFC governance | USB-C Alt Mode + Type-C signaling |

**Theorem (informal):** Either alone is insufficient.
- Намордник alone (no bridge): incoming cannot operationally interact with host → merger is contract-only, no synergy.
- USB-C порт alone (no constraints): operational integration without constitutional discipline → R12 violations + drift → AOL-Time Warner failure mode.
- **Both together** = sufficient (necessary AND sufficient, claim refutable; H-SM-13).

---

## §D. Cybernetic diagram — Ashby variety alignment

**Conceptual frame:**

- Let V_I = behavioural variety of incoming system at merger boundary.
- Let V_C = variety of host constraint catalog.
- Let V_T = variety of translation rules (USB-C порт).
- Let V_R = variety of regulation = V_C + V_T (constraint + translation jointly absorb V_I).

**Ashby Law (informal):** V_R ≥ V_I required for successful merger.

**Practical implication:**
- Phase 1 Discovery = enumerate V_I (which behaviours of incoming are relevant to merger boundary).
- Phase 2 = construct V_C (намордник catalog) + V_T (translation rules) such that V_C + V_T ≥ V_I.
- Phase 3 = pilot test → empirically verify V_R sufficiency.

(See `diagrams/03-ashby-requisite-variety-merger.md` Phase 8 batch.)

---

## §E. Conway's Law consideration

- **Conway 1968** "How Do Committees Invent?" [src: Conway 1968 Datamation:retrieved 2026] — "Organizations design systems that mirror their communication structure."
- **Merger implication:** Two systems with different communication structures → merging without restructuring communication = double-Conway artefact (two mirrors mismatched).
- **FPF mediates:** FPF protocol provides shared communication structure → merged system's emergent communication ≈ FPF structure (intended consequence; this is the design).
- **Failure mode:** if FPF protocol is not actually used in communication day-to-day, system structures revert and merger drifts.

---

## §F. Sub-protocols + Strategic Q

How sub-protocols change across Strategic Q options (Phase 4 deep-dive):

| Aspect | Option A (Outsource) | Option B (Platform) | Option C (Hybrid) |
|---|---|---|---|
| **Намордник catalog** | Per-engagement custom subset of C1-C10 | Standardized C1-C10 baseline + opt-in extensions | C1-C10 baseline; per-engagement extensions |
| **Smart contract enforcement** | Optional (Jetix-internal audit) | Mandatory (platform fee dependency) | Phase-gated |
| **USB-C порт** | Jetix-custom-built per engagement | Standardised tooling (SDK / lint) | Custom Phase 1; SDK Phase 2 |
| **Tooling investment** | Low | High upfront | Medium phased |

---

## §G. Refutation conditions (Phase 3)

This Phase 3 doc = refuted_if:
- Constraint catalog (10 baseline) is provably incomplete for 2 hypothetical merger cases (Phase 5).
- Translation rule format is provably insufficient (translation needed that doesn't fit yaml structure).
- Ashby variety frame is misapplied (cybernetic critique from ROY phil-expert critic mode).
- Failure mode catalog missing critical class (e.g., regulatory failure not enumerated).

---

## §H. Diagrams (in `diagrams/`)

- `diagrams/03-ashby-requisite-variety-merger.md` — V_I / V_C / V_T / V_R relationship
- `diagrams/04-namordnik-constraint-flowchart.md` — C1-C10 enforcement flow
- `diagrams/05-usb-c-port-translation-flow.md` — incoming → ACL → FPF → host

(Authored in Phase 8 batch.)

---

*Phase 3 brigadier-scribe. R6 provenance per claim. EP-5 F3 (Ashby + DDD + Conway + concept doc C triangulation). Next: Phase 4 Strategic Q decision matrix.*
