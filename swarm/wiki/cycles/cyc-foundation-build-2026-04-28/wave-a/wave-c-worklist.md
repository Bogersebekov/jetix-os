---
title: Wave C Work-List Bullets — per Foundation Part (Phase A-3 integrator)
date: 2026-04-27
phase: A-3
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
inputs:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/cycle-artefact-register.md
F: F4
ClaimScope: "Holds for the 10-part Foundation decomposition as specified in Wave-A interface cards and dependency graph. Does not prescribe exact dispatch brief wording — that is brigadier's responsibility per each bundle cycle."
R:
  refuted_if: "Wave C cycle completion report shows ≥3 parts whose actual work scope diverged substantially from these bullets without an explicit re-scope gate"
  accepted_if: "Wave C bundle cycles align with the dependency build order in §4 and every open dependency-graph contradiction (C1-C4) and underspecification (UND-1..UND-5) maps to an addressed bullet"
dissents:
  - source: engineering-expert (OQ-MERGED-2)
    claim: "Part 5 Wave C bullets may reduce to zero residue — compound learning engine should be confirmed standalone or dissolved into Parts 3+4 after one Wave C spec pass"
    F: F2
    ClaimScope: "Contingent on Ruslan ack of OQ-MERGED-2"
    R: "Accepted if OQ-MERGED-2 is acked in favor of Part 5 standalone; refuted if Ruslan acks dissolution"
---

# Wave C Work-List — Per Foundation Part

> Per spec §4 Phase A-3. For each of 10 Foundation parts: 2-5 bullets describing Wave C work.
> Every bullet cites the interface card section, dependency graph finding, or consultant card that
> grounds it. No bullet without provenance.

---

## §1 Effort Taxonomy

- **S** = 1-2h ROY work (single agent dispatch + brigadier review; one mode pass)
- **M** = 2-4h ROY work (multi-agent dispatch + integrator pass + critic gate)
- **L** = 4-8h ROY work (multi-agent + critic + scalability review + likely one revision iteration)

---

## §2 Per-Part Wave C Bullets

---

### Part 1 — System State Persistence (~S-M total)

Part 1 is the most operationally mature Foundation part. `/company-status`, `/knowledge-diff`, D25
git discipline, and atomic commit format are all operational (cycle 3b). Wave C work is narrow:
clarifications and two declared gaps from the dependency graph.

- **Bullet 1 — Cross-fork provenance schema stub.** Define the architectural stub for D27
  fork-and-merge provenance: declare (a) what fields a cross-fork commit must carry to remain
  traceable to the parent repo's audit trail, (b) which parts of the audit trail fragment across
  a fork boundary and require Phase-B reconciliation architecture, (c) add an explicit entry in
  `decisions/policy/` marking "cross-fork audit trail is Phase-B architecture work." Do NOT
  implement; declare the gap with explicit deferred-to-Phase-B label so Wave C does not inherit
  the ambiguity silently.
  | Effort M | Expert engineering-expert integrator | Book/consultant refs dependency-graph.md §6.1
  "cross-fork provenance requires architectural extension"; part-1 §E Laws "reversibility via
  git revert"; levenchuk-shsm-fpf.md §4 P4 "operates-in A.14 edge type" |

- **Bullet 2 — D25 commit-format lint rule as Foundation artefact.** The `[area] verb what (why)`
  format is declared in CLAUDE.md but is not yet a machine-checkable Foundation artefact. Author
  one canonical `swarm/wiki/foundations/part-1-commit-format.md` with: the format rule, accepted
  area tokens (enumerated), anti-scope (what NOT to put in a commit message), and a Hamel-binary
  acceptance predicate enabling `/lint` to check compliance. Add the check as lint signal #12
  (extending the current 11 KB health checks). Reuses existing `/lint` skill — do NOT reinvent.
  | Effort S | Expert engineering-expert integrator + philosophy-expert critic (Hamel-binary
  predicate review) | Book/consultant refs part-1 §E Laws "Commit messages MUST follow [area]
  format"; candidate-parts-merged.md §2 Part 1 D-Lock D25; levenchuk-shsm-fpf.md §4 P6
  "Deontics — observable obligation" |

- **Bullet 3 — Inline [src:] citation standardisation for Parts 7, 8, 9.** Dependency graph §5.2
  (cross-cutting 2 — provenance tagging) identified Parts 7, 8, 9 as PARTIAL for inline [src:]
  citation density. Wave C must add inline citations to §D and §E sections of all three interface
  cards to match the standard set by Parts 1-3 and 6. This is a Part 1 Wave C item because Part
  1 is the provenance substrate and the cross-cutting discipline is enforced through it.
  | Effort S | Expert engineering-expert critic (Conformance check 6 — DRY violation in
  provenance schema) | Book/consultant refs dependency-graph.md §5.2 "PARTIAL — Wave C: add
  inline [src:] to §D and §E"; part-1 §B "git history as audit trail" |

---

### Part 2 — Signal Ingestion & Triage (~M total)

Part 2's pipeline is operational (cycle 11). Wave C work focuses on three structural gaps: the
STOP gate schema (UND-4), the multi-owner scalability stub (dependency graph OQ-6), and the PARA
tier field enforcement.

- **Bullet 1 — STOP gate packet schema with `gate_class` field (UND-4).** Define a canonical
  gate packet schema for Part 2's STOP gate submissions to Part 6. The schema must include a
  `gate_class: stop_gate` field distinguishing STOP gate packets from stage-gate (Part 7) and
  arbitrary draft-promotion (Part 3) packets. Hamel-binary acceptance predicate: "gate_class
  field is present and non-null in every STOP gate submission arriving at Part 6." This resolves
  UND-4 and ensures Part 6 can apply the correct J-Approve authority rule without ambiguity.
  | Effort M | Expert engineering-expert integrator + philosophy-expert critic (J-level
  decision class compliance review per A.13 Agency-CHR) | Book/consultant refs
  dependency-graph.md §4.4 UND-4 "gate_class field"; part-2 §D "methodologically-uses Part 6";
  anthropic-constitutional-ai.md §4 P6 "transparency/corrigibility — gate failure surfaced with
  specific reason"; levenchuk-shsm-fpf.md §4 P6 "Deontics — surface gate failure with reason
  not generic reject" |

- **Bullet 2 — PARA-tier field enforcement in `/ingest`.** Interface card §E Deontics declares
  "MUST tag every draft with a `para_tier:` field before handoff to Part 3." The current `/ingest`
  skill does not enforce this (no lint signal exists for missing `para_tier`). Wave C must: (a)
  add `para_tier` as a required frontmatter field in the draft-candidate schema, (b) add `/lint`
  check that rejects drafts lacking `para_tier`, (c) update `/ingest` to prompt for the field
  when absent. Reuses existing `/ingest` and `/lint` — extend, do NOT reinvent.
  | Effort S | Expert engineering-expert integrator | Book/consultant refs
  part-2 §E Deontics "MUST tag every draft with para_tier"; knowledge-management-karpathy-luhmann-matuschak.md
  §6 Part 2 item 1 "PARA-tier field before handoff"; candidate-parts-merged.md §2 Part 2 AUDIT |

- **Bullet 3 — Multi-owner STOP gate delegation stub.** Dependency graph OQ-6 flags: at Phase
  B/C, the single-owner STOP gate becomes a bottleneck (structural change estimate ~35% — above
  30% fragility threshold). Part 2's Wave C interface card must include a Phase-B delegation
  stub: declare (a) the gate authority delegation mechanism (per-owner gate instance with scoped
  authority), (b) which F.9 Bridge fields are required for multi-owner activation, (c) what
  triggers delegation (owner count > 1 is the predicate). This is a spec-only bullet — no
  implementation; just the declaration committed as a Foundation artefact so Phase-B doesn't need
  to rediscover the design intent.
  | Effort S | Expert mgmt-expert integrator + engineering-expert critic | Book/consultant refs
  dependency-graph.md §6.2 "structural change estimate ~35% — ABOVE 30% threshold";
  dependency-graph.md §7 OQ-6; part-9 §E Laws "F.9 Bridge documentation — multi-owner" |

---

### Part 3 — Knowledge Base & Methodology Library (~M-L total)

Part 3's wiki substrate is operationally mature (552 entities, 577 edges, 9 entity types). Three
structural gaps remain: accessor pipeline ownership (C1), methodology library sub-layer, and CRM
edge validation ownership (UND-5).

- **Bullet 1 — Accessor pipeline ownership resolution (C1).** Contradiction C1 in dependency
  graph §3.1: Part 3 disowns `/ask`, `/ingest`, `/consolidate`, `/build-graph`, `/lint` to Part
  4 or "shared infrastructure"; Part 4 does not accept them. Wave C Part 3 interface card must
  add to §F Anti-scope: explicit statement of where the accessor pipeline IS owned (Part 4 or
  declared shared infrastructure). If Part 4 rejects ownership, a new cross-cutting concern entry
  must be added to candidate-parts-merged.md §3 with a named maintenance party. Without this,
  the skills are architecturally orphaned. BLOCKING for Wave C task assignment per
  dependency-graph §3.1.
  | Effort M | Expert engineering-expert integrator + systems-expert critic (shared-infra vs
  Part-4-owned decision requires VSM S3 lens) | Book/consultant refs dependency-graph.md §3.1
  C1 "BLOCKING for Wave C task assignment"; part-3 §F Anti-scope "pipeline sub-system owned by
  Part 4"; part-4 §H "Note for Wave C: routing table as declarative YAML"; systems-thinking-cybernetics.md
  §4 VSM S1-S5 boundary clarity principle |

- **Bullet 2 — Methodology library sub-layer materialisation.** The methodology library
  sub-layer within Part 3 is not yet consistently populated from compound outputs
  (candidate-parts-merged.md §2 Part 3 "Cycles reuse?"). Wave C must: (a) define the target
  entity-type for promoted methodology patterns — canonicalise whether they live in
  `wiki/foundations/`, `wiki/concepts/`, or a new `wiki/methodology/` entity type, (b) add to
  Part 3 §E Admissibility: "methodology pattern from Part 5 accepted only if it carries ≥1 DRR
  'Result: validated' marker from ≥2 distinct cycles AND a `rule_slug` for deduplication,"
  (c) target edge density ≥2.0 edges/entity (current 1.05) by adding typed edges to methodology
  entries. Resolves UND-3 partially (the promotability criterion side).
  | Effort M | Expert engineering-expert integrator + knowledge-management-karpathy-luhmann-matuschak
  framework (Matuschak evergreen note → methodology entry promotion chain) | Book/consultant refs
  dependency-graph.md §4.3 UND-3; part-3 §E Effects "edge density Wave C target ≥2.0
  edges/entity"; knowledge-management-karpathy-luhmann-matuschak.md §4 Principle 1 "density as
  quality signal"; compounding-engineering.md §5 "DRR → methodology pattern promotion pipeline" |

- **Bullet 3 — CRM edge validation ownership (UND-5 + Part 3 §D update).** Dependency graph
  §4.5 UND-5: Part 10 writes CRM relationship edges to `wiki/graph/edges.jsonl` but Part 3 §D
  does not acknowledge Part 10 as a content creator. Wave C must add to Part 3 §D: "`receives-from
  Part 10` — CRM relationship edges (8 CRM edge types) written to `wiki/graph/edges.jsonl` by
  Part 10; these edges are NOT Part 3's own writes but are stored in Part 3's managed file. Part
  3's `/lint` validates CRM-origin edges; malformed CRM edges surface as Part 3 lint failures,
  not Part 10 failures." Resolves UND-5 boundary ambiguity.
  | Effort S | Expert engineering-expert critic | Book/consultant refs dependency-graph.md §4.5
  UND-5 "asymmetry — who validates CRM edges?"; part-10 §B Outputs "CRM graph edges →
  wiki/graph/edges.jsonl"; part-3 §E Laws "edges.jsonl is append-only"; levenchuk-shsm-fpf.md
  §4 P4 A.14 typed mereology |

- **Bullet 4 — `/ask --save` default enforcement.** Interface card §E Deontics declares
  "`/ask --save` MUST file synthesis responses to `wiki/comparisons/` by default — discard
  requires explicit `--no-save` flag." Current `/ask` does not enforce this. Wave C must update
  the `/ask` skill to implement the default-save behaviour and add a `/lint` check that flags
  `wiki/comparisons/` emptiness as a health signal when `/ask` usage is confirmed in session
  history.
  | Effort S | Expert engineering-expert integrator | Book/consultant refs part-3 §E Deontics
  "/ask --save MUST file synthesis"; knowledge-management-karpathy-luhmann-matuschak.md §6 Part
  3 item 3 "discard requires explicit --no-save flag" |

---

### Part 4 — Role Taxonomy & Coordination Protocol (~M-L total)

Part 4 has the highest convergence (4/5 experts independently proposed it) and the clearest Wave
C primary gap: the routing table as declarative YAML. Secondary gaps: accessor pipeline ownership
(C1) and the DRR message schema boundary (UND-1).

- **Bullet 1 — Routing table as declarative YAML artefact (primary Wave C gap).** Extract
  routing logic from `brigadier.md` and expert `.md` system prompts into
  `swarm/lib/routing-table.yaml`. The YAML must declare: role slug, J-level authority per role,
  allowed modes, write-scope-glob, escalation taxonomy per trigger, and the hub-and-spoke dispatch
  chain. Hamel-binary acceptance predicate: "routing-table.yaml exists, parses without errors,
  and contains an entry for every role in `comms/mailboxes/`." This is the highest-leverage
  structural investment in Part 4 — without it, federated coordinator substitution at Phase C
  is impossible without system-prompt surgery. Do NOT reinvent existing role semantics — extract
  and canonicalise what already exists.
  | Effort L | Expert engineering-expert integrator + systems-expert scalability (hub-and-spoke
  →federated topology planning; dependency graph §6.4 ~40% structural change risk at 10×) |
  Book/consultant refs part-4 §H "routing table as declarative YAML — Wave C primary gap";
  dependency-graph.md §6.4 "structural change estimate ~40% ABOVE 30% threshold"; levenchuk-shsm-fpf.md
  §4 P1 IP-1 "role manifests are U.Episteme; executor bindings are RUSLAN-LAYER";
  systems-thinking-cybernetics.md §4 "VSM S4 variety management through declarative routing" |

- **Bullet 2 — Accessor pipeline ownership decision (C1 resolution for Part 4 side).** Wave C
  Part 4 interface card must explicitly state whether Part 4 accepts or rejects ownership of
  `/ask`, `/ingest`, `/consolidate`, `/build-graph`, `/lint`. If accepted: Part 4 §B Outputs
  must list "wiki accessor pipeline skills :: invocable by any consumer :: on-demand" and §D
  must add a `creates` edge to Part 3. If rejected: nominate a named shared-infrastructure
  maintainer (candidate: `swarm/lib/` as the shared-infra home with an explicit owner role
  declared in routing-table.yaml). This must be resolved before Part 3's Bullet 1 can close —
  dependency-graph §3.1 marks C1 as BLOCKING.
  | Effort S | Expert engineering-expert integrator (the decision itself is fast; the rationale
  must be crisp) | Book/consultant refs dependency-graph.md §3.1 C1 "BLOCKING — resolve before
  Wave C Part 4 spec"; part-4 §H "Wave C note: accessor pipeline ownership"; levenchuk-shsm-fpf.md
  §4 P4 operates-in A.14 edge type |

- **Bullet 3 — Part 4 → Part 5 DRR message schema (UND-1).** Define the data-shape contract at
  the Part 4 → Part 5 boundary: does Part 5 receive raw structured task-return packets (and do
  its own DRR extraction) or pre-processed DRR extractions from Part 4? Recommendation per
  dependency-graph §4.1: Part 5 receives raw task-return packets (maintains DRR extraction
  close to compound-phase semantics). Wave C must update Part 4 §B Outputs to say "Structured
  task-return packets from all dispatched roles :: `compound-phase-start-event`." This resolves
  UND-1 unambiguously.
  | Effort S | Expert engineering-expert integrator | Book/consultant refs dependency-graph.md §4.1
  UND-1 "data-shape contract at Part 4 → Part 5 boundary"; part-5 §A Inputs "Structured packets
  from all parts"; compounding-engineering.md §3 "DRR extraction logic" |

---

### Part 5 — Compound Learning & Methodology Capture (~M total)

Part 5's DRR pattern is operationally validated (cycles 1-11). Wave C work: canonicalise the
compound ritual, define the methodology promotion pipeline (UND-3), and declare the OQ-MERGED-2
dissent resolution path.

- **Bullet 1 — Compound ritual as canonical Foundation artefact.** The 40/10/40/10 cadence is
  declared in FUNDAMENTAL §2.2 but is not yet a discrete Foundation artefact with its own
  canonical path, Hamel-binary acceptance predicate, and drift-tolerance specification. Wave C
  must produce `swarm/wiki/foundations/part-5-compound-ritual.md` declaring: (a) cadence
  definition (40/10/40/10 with ±10pp drift tolerance), (b) mandatory compound-phase outputs
  (DRR entry in strategies.md + at least one methodology pattern candidate), (c) compound-phase
  trigger predicate, (d) health SLI "compound-application-rate ≥ 80%" as the acceptance
  predicate. Reuses existing DRR pattern from agents/*/strategies.md — canonicalise, do NOT
  reinvent.
  | Effort M | Expert systems-expert integrator + engineering-expert critic | Book/consultant refs
  part-5 §E Laws "40/10/40/10 cadence ratio is constitutional value"; compounding-engineering.md
  §2 "Main Loop definition: Plan / Work / Review / Compound"; candidate-parts-merged.md §2 Part
  5 D-Lock FUNDAMENTAL §2.2; systems-thinking-cybernetics.md §4 R2 reinforcing loop as the
  structural rationale |

- **Bullet 2 — Methodology promotion pipeline (UND-3 resolution).** Dependency graph §4.3
  UND-3: neither Part 5 nor Part 3 specifies the admissibility criterion for methodology pattern
  promotion, the target entity-type, or who triggers the promotion. Wave C must produce a
  canonical promotion pipeline specification declaring: (a) admissibility: ≥1 DRR 'Result:
  validated' marker across ≥2 distinct cycles AND a `rule_slug`, (b) target entity-type (per
  Part 3 Bullet 2 decision), (c) promotion trigger: agent during compound phase generates a
  promotion candidate; owner acks via Part 6 gate before the entry reaches `wiki/foundations/`.
  This closes UND-3 from the Part 5 side.
  | Effort M | Expert engineering-expert integrator + philosophy-expert critic (F-G-R compliance
  on promoted methodology patterns; F level must rise to F5 post-promotion) | Book/consultant
  refs dependency-graph.md §4.3 UND-3 "who triggers promotion?"; part-5 §G F-G-R "methodology
  pattern promoted: F4→F5 on promotion"; compounding-engineering.md §5 "validated pattern
  threshold"; knowledge-management-karpathy-luhmann-matuschak.md §6 Part 3 item 1 "Karpathy wiki
  proves itself by accumulating validated entries" |

- **Bullet 3 — OQ-MERGED-2 dissent resolution declaration.** The engineering-expert dissent
  (Part 5 dissolves into Parts 3+4) is held open contingent on Ruslan ack. Wave C Part 5 spec
  must include a one-page "dissolve condition" declaration: what observable cycle evidence would
  trigger the dissolve (candidate: if methodology promotion pipeline is fully owned by Part 3
  after two Wave C bundle cycles with zero residual compound-phase-exclusive work), what the
  recombination would look like, and what the Ruslan ack gate packet would contain. If Ruslan acks
  standalone, close OQ-MERGED-2 with a LOCKED record in `decisions/`. If Ruslan acks dissolve,
  initiate bundle redesign before Wave C Part 5 cycle runs.
  | Effort S | Expert philosophy-expert critic (OQ-MERGED-2 is an epistemic boundary question
  — when does a part lose independent lifecycle?) | Book/consultant refs candidate-parts-merged.md
  §6 OQ-MERGED-2; part-5 §H "dissent preserved — dissolve path held open contingent on OQ-MERGED-2
  Ruslan ack"; dependency-graph.md §2.4 P4↔P5 "R2 reinforcing loop is healthy, not blocking" |

---

### Part 6 — Governance, Provenance & Human Gate (~M-L total)

Part 6's stage-gate pattern is the most validated in the system (10/10 cycles, Pattern 1). Wave
C gaps: F-G-R compliance scanner, blast-radius classifier, and TRADEOFF-01 VSM S3 designation.

- **Bullet 1 — F-G-R compliance scanner as Part 6 owned function.** F-G-R compliance enforcement
  is not yet a systematic function owned by Part 6 (candidate-parts-merged.md §2 Part 6 "F-G-R
  compliance enforcement is NOT yet a systematic Part-owned function — flagging as Wave C gap").
  Wave C must specify and stub a `/lint --check-fg-r` subcommand that scans all canonical
  artefacts for: (a) F-G-R fields present in frontmatter, (b) F level ≥ F3 for anything marked
  canonical (F2 or below = not yet ready for canonical state), (c) ClaimScope non-empty,
  (d) R.accepted_if is a falsifiable predicate (Hamel-binary form check). Output: a compliance
  report surfaced to Part 8's quarterly immune audit. "Specify and stub" scope — tool skeleton,
  not full implementation.
  | Effort M | Expert engineering-expert integrator + philosophy-expert critic (Hamel-binary
  predicate check is philosophy domain; F-G-R triad definition is levenchuk-shsm-fpf territory) |
  Book/consultant refs part-6 §E Deontics "F-G-R compliance enforcement distinct from Part 8's
  audit"; levenchuk-shsm-fpf.md §4 P5 B.3 F-G-R Trust & Assurance; anthropic-constitutional-ai.md
  §4 P3 "hardcoded never-list parallel — Part 6 enforces structural invariants" |

- **Bullet 2 — Blast-radius classification table as Foundation artefact (OQ-MERGED-6).** The
  J-level decision matrix (J-Auto / J-Approve / J-Strategic) exists in FUNDAMENTAL §4.6 but is
  not yet a canonical Foundation artefact with enumerated blast-radius categories and the
  Default-Deny classifier for novel actions. Wave C must produce `swarm/wiki/foundations/part-6-blast-radius-table.md`
  declaring: blast-radius categories (local-only / local-modifying / external-read / external-write /
  financial / public), J-level authority mapping per category, and the Default-Deny rule for
  uncategorised actions. Resolves OQ-MERGED-6. Hamel-binary acceptance predicate: "every novel
  action classification query against the table returns a J-level authority assignment or
  Default-Deny within one lookup — no open-ended interpretation path."
  | Effort M | Expert philosophy-expert integrator + investor-expert critic (blast-radius has
  capital implications at J-Strategic tier) | Book/consultant refs part-6 §E Laws "Default-Deny
  on uncategorized actions"; dependency-graph.md §7 "OQ-4 gate_class field should include
  blast-radius"; candidate-parts-merged.md §6 OQ-MERGED-6; FUNDAMENTAL §4.6 |

- **Bullet 3 — TRADEOFF-01 VSM S3 authority designation (dependency graph OQ-1 — BLOCKED on
  Ruslan ack).** Beer VSM predicts oscillation risk when S3 (Audit/Optimisation) authority is
  split between two parts without a designated lead. Dependency graph §7 OQ-1 designates this
  as MUST be resolved before Wave C Part 8 spec. The recommendation (Part 8 = S3 audit authority
  lead; Part 6 = enforcement arm) must be submitted to Ruslan as an AWAITING-APPROVAL gate packet
  before the Part 8 bundle cycle runs. Wave C Part 6 bullet: produce the S3-authority gate packet
  with the rationale, the temporal distinction (Part 6 = real-time per-artefact; Part 8 = periodic
  system-wide), and the explicit delineation of what escalation events flow to each part. This
  bullet is BLOCKED until Ruslan acks OQ-1.
  | Effort M (gate packet authoring) | Expert systems-expert integrator (VSM S3 lens; Beer VSM
  S3 chapter is the theoretical grounding) | Book/consultant refs dependency-graph.md §7 OQ-1
  "MUST be resolved before Wave C Part 8 spec"; systems-thinking-cybernetics.md §4 Beer VSM
  S3-S4 authority clarity; part-6 §D Dependencies "Part 6 ↔ Part 8 dual: constrained-by +
  methodologically-uses" |

- **Bullet 4 — C4 edge type correction (Part 9 → Part 6).** Dependency graph §3.4 C4: Part 9
  §D declares `PhaseOf Part 6` but this is a nomenclature imprecision — Part 9 is not
  structurally a phase of Part 6's lifecycle; it uses Part 6's gate as a service for owner-
  initiated promotions. Wave C must update Part 9 §D from `PhaseOf Part 6` to
  `methodologically-uses Part 6` with explicit rationale. This is a Part 6 Wave C bullet because
  Part 6 owns the gate mechanism and must confirm the correct edge type on its side.
  | Effort S | Expert engineering-expert critic (A.14 edge type precision) | Book/consultant
  refs dependency-graph.md §3.4 C4 "LOW severity — nomenclature correction, not behavioural";
  levenchuk-shsm-fpf.md §4 P4 A.14 Advanced Mereology edge type taxonomy |

---

### Part 7 — Project Lifecycle Substrate (~M total)

Part 7's project scaffold skills are operational (cycle 3b B2 mini-swarm). Wave C gaps: canonical
project schema YAML, IP-5 exception whitelist, and cadence alignment declaration.

- **Bullet 1 — Canonical project schema YAML.** The Foundation-level "what a project is" schema
  with enforced stage-gate sequences is not yet canonical (candidate-parts-merged.md §2 Part 7
  "Wave C materialisation needed"). Wave C must produce `swarm/wiki/foundations/part-7-project-schema.yaml`
  declaring: required frontmatter fields per project type (type / appetite / scope-boundary /
  acceptance-predicate / accountable / escalation-path), state machine (scoped → staged →
  activated → under-review → closed | archived), and stage-gate predicate per state transition.
  The schema must be D26-compliant from the start: no hardcoded "Ruslan does X" — all accountable
  fields are role-typed. Reuses existing `.claude/config/project-types.yaml` as the starting
  point — extend, do NOT reinvent.
  | Effort M | Expert engineering-expert integrator + mgmt-expert critic (D26 team-50-100
  compliance review) | Book/consultant refs part-7 §H "define canonical Foundation-level project
  schema YAML — M effort"; part-7 §E Laws "IP-5 past-participle state names"; levenchuk-shsm-fpf.md
  §4 P2 A.2 Role Taxonomy (accountable field role-typed per IP-1) |

- **Bullet 2 — IP-5 past-participle exception whitelist.** A-1 critic gate applied FLAG-MAJOR
  correction to Part 7 state naming (`active` → `activated`; `review` → `under-review`). The
  whitelist for past-participle exceptions (`under-review` and similar) must be committed as a
  canonical Foundation policy artefact at `decisions/policy/past-participle-exceptions.md` so
  future interface card authors and lint tools can reference it without re-deriving the exception
  rule. Hamel-binary acceptance predicate: "any state name appearing in a Foundation interface
  card that is not a bare past-participle must appear in this whitelist with explicit semantic
  justification."
  | Effort S | Expert philosophy-expert critic (IP-5 exception rationale is philosophy domain)
  | Book/consultant refs part-7 §H FLAG-MAJOR correction "add to decisions/policy/past-participle-exceptions.md";
  levenchuk-shsm-fpf.md §4 P2 IP-5 alpha state naming discipline; A-1-critic-gate.md §6 item 1 |

- **Bullet 3 — Cadence alignment declaration (dependency graph OQ-5).** Dependency graph §5.3
  (cross-cutting 3): Part 7 does not declare whether project stage gates align with 40/10/40/10
  cycle boundaries or operate event-driven. OQ-5 must be answered in Wave C Part 7 interface
  card. Add to §E Laws: "Project stage gates are event-driven (not cycle-boundary-gated) to
  prevent project throughput bottlenecks during Work phases. A stage gate may open at any point
  in the 40/10/40/10 cycle when the predicate fires; it does not wait for a cycle boundary."
  | Effort S | Expert mgmt-expert integrator | Book/consultant refs dependency-graph.md §5.3
  "GAP — Part 7 does not declare cadence alignment"; dependency-graph.md §7 OQ-5; part-7 §E
  Deontics "MUST append state transition to swarm/wiki/log.md before returning" |

---

### Part 8 — Health Monitoring & System Integrity (~M-L total; BLOCKED on OQ-1)

Part 8 has the largest operationalisation gap of any Foundation part. `system-health.json` reports
"all green" with no computation mechanism; lint and company-status are disconnected. Wave C scope
is "specify and stub" per OQ-MERGED-5. BLOCKED on TRADEOFF-01 OQ-1 Ruslan ack before starting.

- **Bullet 1 — SLI/SLO schema definition (Foundation artefact).** FUNDAMENTAL §3 names 30+
  SLI/SLO pairs across 8 health domains. None are yet in a canonical schema-declared artefact.
  Wave C must produce `swarm/wiki/foundations/part-8-sli-slo-schema.md` declaring: the field
  spec (what is measured / how measured / cadence / starter-value / calibration-trigger /
  calibration-cadence), and the first 8-10 SLI entries (one per major health domain) with
  starter values explicitly labeled as "calibration-grade, not production-grade." Hamel-binary
  acceptance predicate: "every SLI entry carries all 6 required fields and the starter-value
  label." Resolves the health signal schema underspecification (C2) from the Part 8 side.
  | Effort M | Expert systems-expert integrator + engineering-expert critic | Book/consultant
  refs part-8 §E Laws "SLI/SLO values MUST be labeled starter/calibration"; part-8 §G F-G-R
  "SLI/SLO schema F5 once schema acked"; dependency-graph.md §3.2 C2 "health signal schema
  underspecified — MEDIUM severity"; systems-thinking-cybernetics.md §4 Ashby requisite variety
  principle applied to monitoring channel design |

- **Bullet 2 — Health signal schema per emitting part (C2 resolution — producer side).** C2
  in dependency-graph §3.2: multiple parts (P1, P5, P7) declare structured outputs for Part 8
  but use different schemas; Part 9 does not declare a Part 8 output at all. Wave C must update
  §B Outputs sections of Parts 1, 5, 7, 9 to use the field names defined in the SLI/SLO schema
  from Bullet 1. Specifically: Part 9 must add a §B Output row for Part 8 declaring the health
  signals it emits (daily log creation rate, attention-budget utilisation, weekly review completion
  rate, draft clearance rate). This is coordinateed with Parts 1, 5, 7, 9 Wave C work but is
  owned from the Part 8 consumer side.
  | Effort M | Expert engineering-expert integrator (schema harmonisation across 4 interface
  cards) | Book/consultant refs dependency-graph.md §3.2 C2 "no agreed schema — MEDIUM severity";
  part-8 §A Inputs "daily log creation rate, attention-budget utilisation" listed but no
  declared field names; part-8 §H F-G-R dual-ownership note |

- **Bullet 3 — Weekly health dashboard and quarterly immune audit artefact templates.** Part 8
  §E Effects declares weekly `decisions/weekly/<YYYY-WNN>-health.md` and quarterly
  `decisions/quarterly/<YYYY-QN>-immune-audit.md` but no templates exist. Wave C must produce
  both templates with required sections (weekly: SLI snapshot per domain, anomalies, recommendations;
  quarterly: F-G-R compliance sweep, alpha-classification drift, role-manifest freshness,
  strategies.md staleness). The quarterly template must include the philosophy-expert lens
  (F-G-R compliance audit). "Specify and stub" — template authoring, not live computation.
  | Effort M | Expert mgmt-expert integrator (weekly template) + philosophy-expert integrator
  (quarterly immune audit template — F-G-R compliance audit requires philosophy lens) |
  Book/consultant refs part-8 §H "Wave C bullets: weekly health dashboard template — S effort;
  quarterly immune audit — M effort; philosophy-expert integrator cited"; part-8 §E Deontics
  "MUST produce weekly health dashboard for Part 9"; FUNDAMENTAL §2.5 health checkup cadence |

- **Bullet 4 — Alert-routing interface stub to Part 6.** Part 8 §H "Wave C bullets" explicitly
  cites "stub alert-routing interface to Part 6 escalation taxonomy — S effort." Wave C must
  produce a minimal stub: an alert packet schema (anomaly-type / severity / affected-part /
  recommended-action / J-level-authority-required) and the routing rule that maps alert types
  to Part 6 escalation taxonomy entries. BLOCKED on TRADEOFF-01 OQ-1 (S3 authority designation
  must be resolved before alert routing can be designed — routing depends on knowing whether Part
  8 or Part 6 is the S3 lead).
  | Effort S | Expert engineering-expert integrator | Book/consultant refs part-8 §H "stub
  alert-routing interface to Part 6 — S effort"; part-6 §E Deontics "MUST surface every gate
  failure with specific reason"; anthropic-constitutional-ai.md §5 T3 "fail-loud: anomaly →
  committed alert record within one monitoring cycle" |

---

### Part 9 — Owner Interaction Scaffold (~M total)

Part 9's `/plan-day` and `/close-day` skills exist. The Foundation-level schema for daily-log
artefacts, weekly review, and 3-tier SLA taxonomy is not yet canonical.

- **Bullet 1 — Daily-log artefact schema.** Define the canonical schema for daily working page
  artefacts at `swarm/wiki/foundations/part-9-daily-log-schema.md`: required YAML frontmatter
  fields (date, created-by, status), required sections (morning plan, draft area, EOD reflection),
  admissibility criteria (date header present, plan section non-empty before work session starts),
  Hamel-binary acceptance predicate ("daily log file at `daily-log/YYYY-MM-DD.md` exists with
  all required sections non-empty before EOD ritual completes"). Update `/plan-day` to scaffold
  this schema automatically. Do NOT reinvent `/plan-day` — extend it.
  | Effort S | Expert engineering-expert integrator + mgmt-expert critic | Book/consultant refs
  part-9 §H "Wave C bullets: define daily-log artefact schema — S effort; engineering-expert
  integrator + mgmt-expert critic"; part-9 §E Effects "daily log creation rate ≥5 per working
  week"; FUNDAMENTAL §2.6 daily ops flow |

- **Bullet 2 — Weekly review artefact schema with draft-disposition table.** Define the canonical
  schema for the weekly review artefact with: required sections (open-drafts disposition table,
  strategic alignment check, stuck-contact surfacing from Part 10, health signals from Part 8,
  next-week appetite declaration). IP-7 asymmetry must be built into the template: agent sections
  (structured extractions) are clearly distinguished from owner-authored sections (strategic
  reflection). Update `/close-day` or produce a dedicated `/weekly-review` skill. Resolves the
  Part 9 → Part 8 health signal gap from C2 (by specifying what health signals feed the weekly
  review).
  | Effort M | Expert mgmt-expert integrator | Book/consultant refs part-9 §H "Wave C bullets:
  weekly review artefact schema — M effort; mgmt-expert integrator"; levenchuk-shsm-fpf.md §4
  P7 IP-7 "writing-as-thinking asymmetry — owner authors; agents contribute extractions";
  dependency-graph.md §3.2 C2 Part 9 "no explicit Part 8 output declared" |

- **Bullet 3 — 3-tier SLA taxonomy as canonical Foundation artefact.** The L1/L2/L3 approval
  SLA classification is referenced in FUNDAMENTAL §4.2 and Part 9 §E Laws but has no dedicated
  canonical Foundation artefact with enumerated examples, classification heuristics, and a
  Hamel-binary predicate for compliance. Wave C must produce
  `swarm/wiki/foundations/part-9-approval-sla-taxonomy.md` with: L1 definition and examples
  (external commitments, Lock modifications — "no batching permitted"), L2 definition (standard
  approval, 24h SLA), L3 definition (low-blast-radius, auto-processable within session).
  Philosophy-expert critic review required for agency-CHR compliance.
  | Effort S | Expert philosophy-expert critic (A.13 Agency-CHR compliance — SLA classification
  is a decision-class authority mapping) | Book/consultant refs part-9 §H "Wave C bullets:
  canonicalise 3-tier SLA taxonomy — S effort; philosophy-expert critic (agency-CHR compliance)";
  part-9 §E Laws "L1-classified items gated within same-session"; FUNDAMENTAL §4.2 L1/L2/L3 |

---

### Part 10 — External Touchpoints & Network Interface (~M total)

Part 10's CRM subsystem is fully operational (cycle 10). Wave C gaps are structural: L.1-L.3
integration stubs, C3 Phase-A boundary clarification, and privacy architecture.

- **Bullet 1 — L.1-L.3 external integration adapter stubs.** L.1-L.3 are explicitly Phase-A
  stubs. Wave C must produce `swarm/wiki/foundations/part-10-integration-stubs.md` declaring:
  (a) the generic integration adapter pattern (interface contract: read-only intelligence tracker
  vs write-ack action coordinator), (b) the required gate mechanism for each adapter type
  (read-only: no gate required; write-action: J-Approve minimum via Part 6), (c) the multi-channel
  output routing interface (voice / text / webhook delivery target declaration). Do NOT implement
  actual API connectors — spec the interface contracts so Phase-B materialisation knows exactly
  what to build.
  | Effort M | Expert engineering-expert integrator + systems-expert scalability (external
  integration introduces variety that Part 8 must monitor; Ashby requisite variety applies) |
  Book/consultant refs part-10 §F Anti-scope "L.1-L.3 Phase-A stubs ONLY"; part-10 §G F-G-R
  "L.1-L.3 integration stubs: F3, Phase-A stub only"; candidate-parts-merged.md §2 Part 10
  "K.1-K.3, L.1-L.3 gap addressed here"; systems-thinking-cybernetics.md §4 Ashby variety
  matching |

- **Bullet 2 — C3 Phase-A boundary clarification (Part 10 vs Part 2 inbound routing).** C3 in
  dependency-graph §3.3: Part 10 claims to route inbound signals to Part 2 (Part 10's model);
  Part 2 claims the signal source is "owner-initiated /ingest" (Part 2's model). For Phase A,
  Part 2's model is correct (FUNDAMENTAL §6.2 human-in-loop at all ingest events). Wave C must
  add to Part 10 §F Anti-scope: "In Phase A, Part 10's `PhaseOf Part 2` edge applies ONLY when
  L.1-L.3 external integrations are operational (Phase B). Phase-A role of Part 10 is CRM record
  management and write-ack gating, not automated signal routing." This prevents the C3 ambiguity
  from propagating into Phase-B design.
  | Effort S | Expert engineering-expert critic | Book/consultant refs dependency-graph.md §3.3
  C3 "LOW — becomes real at Phase B; flag now"; part-2 §A Inputs "owner initiates /ingest";
  part-10 §D "PhaseOf Part 2" |

- **Bullet 3 — Privacy architecture declaration (FUNDAMENTAL §6.4).** Part 10 is the only
  Foundation part that explicitly stores data about third parties (FUNDAMENTAL §6.4 — added as
  A-1 critic correction FLAG-MINOR). Wave C must produce
  `swarm/wiki/foundations/part-10-privacy-architecture.md` declaring: consent-respected data
  collection policy, forget-request hard-delete procedure with verifiable mechanism, sensitive
  data encryption-at-rest requirement, cross-context contamination prevention rules, and the
  "no inference of protected characteristics" absolute prohibition. This must be a canonical
  Foundation artefact (not just a CLAUDE.md note) so any future fork of the system inherits
  the privacy architecture structurally.
  | Effort M | Expert philosophy-expert integrator (privacy principles are constitutional;
  require same rigour as FUNDAMENTAL §6 anti-scope) | Book/consultant refs part-10 §E Laws
  "FUNDAMENTAL §6.4 privacy principles apply structurally"; A-1-critic-gate.md §6 item 5
  "FLAG-MINOR: §6.4 privacy reference omitted — required because Part 10 is structural home
  of third-party data"; candidate-parts-merged.md §2 Part 10 D-Lock FUNDAMENTAL §6.4 |

- **Bullet 4 — OQ-MERGED-3 fork-separation checklist.** Part 10 is the highest-risk part for
  RUSLAN-LAYER content leaking into Foundation (ICP scoring weights, outreach templates, strategy-
  hooks YAML). OQ-MERGED-3 asks whether a fork-separation checklist is Wave A or Wave C scope.
  Wave C materialises it per-part-10: produce a one-page "what is Foundation vs RUSLAN-LAYER"
  declaration for Part 10 covering: contact schema fields (Foundation: name / context / source-
  provenance / status), RUSLAN-LAYER fields (ICP-score / offers / asks / strategy-hooks), and the
  parameterisation mechanism (RUSLAN-LAYER YAML overlay over Foundation schema). Resolves
  OQ-MERGED-3 for Part 10.
  | Effort S | Expert investor-expert critic (fork-separation has capital implications — D27
  fork-and-merge provenance must be preserved; investor risk lens applies) | Book/consultant refs
  candidate-parts-merged.md §6 OQ-MERGED-3 "fork-separation checklist — Wave A or Wave C?";
  part-10 §E Deontics "MUST NOT embed RUSLAN-LAYER ICP content in Foundation contact schema";
  dependency-graph.md §6.10 "D27 CRM schema must be forkable with ICP parameters externalized" |

---

## §3 Wave C Bundle Composition Recommendation

Per spec §10 + Q5 Ruslan ack default ("group by cross-cutting theme"). Suggested bundles derived
from the topological build order in dependency-graph §2.5:

```
Layer 0 (no upstream): Part 1
Layer 1 (depends on P1): Part 6
Layer 2 (depends on P1, P6): Parts 2, 4, 3
Layer 3 (depends on P1, P6, P4): Part 5
Layer 4 (depends on P1-P6, P5): Parts 7, 8
Layer 5 (depends on P1-P8): Parts 9, 10
```

**Bundle 1 — Substrate Clarifications (Parts 1 + 6 partial): Information flow foundation.** ~6-10h total.
- Part 1: Bullets 1-3 (provenance schema + commit format lint + inline citation standardisation)
- Part 6: Bullet 4 (C4 edge type correction) + Bullet 2 (blast-radius table) as standalone deliverables not requiring TRADEOFF-01 resolution
- Reason: Part 1 is zero-dependency substrate; Part 6 blast-radius and C4 corrections are not blocked on OQ-1. These close the fast-path clarifications before the heavier bundles begin.
- BLOCKED items: Part 6 Bullet 3 (TRADEOFF-01) and Part 8 all bullets — deferred to Bundle 3.

**Bundle 2 — Information Lifecycle (Parts 2, 3, 4): Knowledge flow path.** ~12-18h total.
- Part 2: Bullets 1-3 (STOP gate schema, PARA-tier, multi-owner stub)
- Part 3: Bullets 1-4 (C1 accessor ownership, methodology sub-layer, CRM edge validation, /ask --save)
- Part 4: Bullets 1-3 (routing table YAML, C1 resolution for Part 4, DRR message schema UND-1)
- Reason: tight coupling — C1 spans Parts 3 and 4 and must be resolved together; routing table and accessor pipeline ownership are the same structural question. Co-designing saves rework. UND-1 is the Part 4 → Part 5 boundary which must be resolved before Bundle 3 designs Part 5.
- Prerequisite: Bundle 1 complete (commit format lint enables provenance standardisation across these parts).

**Bundle 3 — Compound + Health (Parts 5, 8): Self-improvement + observability.** ~10-16h total.
- Part 5: Bullets 1-3 (compound ritual, methodology promotion pipeline, OQ-MERGED-2 dissent declaration)
- Part 8: Bullets 1-4 (SLI/SLO schema, health signal schema, dashboard templates, alert routing stub)
- Reason: Part 8 health signal schema (C2) depends on knowing what signals Part 5 emits (resolved in Bundle 2 via UND-1). Part 5 compound ritual must be canonical before Part 8 can declare the compound-application-rate SLI meaningfully.
- BLOCKED: Part 8 Bullet 4 (alert routing) until TRADEOFF-01 OQ-1 Ruslan ack. Recommend: Ruslan acks OQ-1 before Bundle 3 begins. Gate packet to be prepared as part of Bundle 1 (Part 6 Bullet 3).
- BLOCKED: Part 5 Bullet 3 (OQ-MERGED-2 declaration) — if Ruslan acks dissolution, Bundle 3 Part 5 scope collapses to zero and its bullets redistribute to Parts 3 and 4.

**Bundle 4 — Operations + External (Parts 7, 9, 10): Owner-facing and lifecycle.** ~12-16h total.
- Part 7: Bullets 1-3 (project schema YAML, IP-5 whitelist, cadence alignment)
- Part 9: Bullets 1-3 (daily-log schema, weekly review schema, 3-tier SLA taxonomy)
- Part 10: Bullets 1-4 (L.1-L.3 stubs, C3 clarification, privacy architecture, fork-separation checklist)
- Reason: Parts 7, 9, 10 are all owner-facing artefacts with coherent UX. Part 7 project schema feeds Part 9's draft-disposition table (weekly review). Part 10's stuck-contact surfacing feeds Part 9's weekly review. Co-designing the three interaction surfaces produces a coherent owner experience.
- Prerequisite: Bundle 1 complete (provenance standardisation applies to all three parts).

**Total Wave C estimate: ~40-60h of ROY swarm work + potential revision iterations.**
**Cycles needed: 4 cycles** (1 per bundle), each ~10-15h walltime.
**Recommended cycle order: Bundle 1 → Bundle 2 → Bundle 3 → Bundle 4** (acyclic build order per topological sort).

---

## §4 Cross-Bundle Dependencies

- **Bundle 1 → all**: Commit-format lint (Part 1 Bullet 2) and inline citation standardisation
  (Part 1 Bullet 3) apply to every artefact produced by Bundles 2-4. Run Bundle 1 first.
- **Bundle 1 (Part 6 Bullet 3) → Bundle 3 (Part 8 all)**: TRADEOFF-01 OQ-1 Ruslan ack is the
  gate condition for Bundle 3. The gate packet is a Bundle 1 deliverable.
- **Bundle 2 (Part 4 routing table) → Bundle 3 (Part 5 compound ritual)**: Routing table YAML
  from Part 4 Bullet 1 defines the dispatch protocol that Part 5's compound ritual operates
  within. Part 5 compound-phase trigger predicate references routing table entries.
- **Bundle 2 (UND-1 resolution) → Bundle 3 (Part 8 C2 resolution)**: The Part 4 → Part 5
  message schema defined in UND-1 determines which health signals Part 5 emits, which Part 8
  must declare in its SLI schema.
- **Bundle 3 (Part 8 SLI schema) → Bundle 4 (Part 9 weekly review)**: The SLI field names
  from Part 8 Bullet 1 must appear in Part 9's weekly review template (Part 9 Bullet 2). Run
  Bundle 3 before Bundle 4 or accept a revision pass on the weekly review template.
- **Bundle 2 (Part 3 accessor ownership C1) → Bundle 2 (Part 4 routing table)**: These are in
  the same bundle because they are the same decision. Resolve C1 ownership in the same spec pass
  that produces the routing table YAML.

---

## §5 Wave C Dispatch Template References

- Per spec §4 Phase A-2, dispatch templates referenced in
  `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-2-dispatch-template.md`
- Wave C bundle dispatch templates are brigadier's responsibility at cycle prep — outside Phase
  A-3 scope.
- Each bullet's "Expert + mode" field is the recommended dispatch cell; brigadier may substitute
  per availability.

---

## §6 Open Questions Requiring Ruslan Ack Before Wave C Starts

The following OQs from the dependency graph require Ruslan ack before specific Wave C bundles
can proceed. Brigadier must author AWAITING-APPROVAL gate packets for each.

| OQ | Gate condition | Blocks |
|---|---|---|
| OQ-1 (TRADEOFF-01 VSM S3) | Ruslan acks: Part 8 = S3 audit lead; Part 6 = enforcement arm | Bundle 3 (Part 8 entire scope) |
| OQ-MERGED-1 (Part 6 split) | Ruslan acks: consolidated (10 parts) vs split (11 parts: 6a+6b) | Bundle 1 Part 6 scope |
| OQ-MERGED-2 (Part 5 dissolve) | Ruslan acks: Part 5 standalone vs dissolve into Parts 3+4 | Bundle 3 Part 5 scope |
| OQ-MERGED-3 (fork-separation) | Ruslan acks: Wave C scope (one page per part) vs Wave A scope addition | Bundle 4 Part 10 Bullet 4 |
| OQ-3 (UND-1 DRR schema) | Ruslan acks: Part 5 receives raw packets and extracts (recommended) vs Part 4 pre-processes | Bundle 2 UND-1 resolution |

---

## §7 Provenance

All claims above trace to the following sources.

| Claim | Source |
|---|---|
| Part 1 cross-fork provenance gap | dependency-graph.md §6.1 "FRAGILE at multi-org scale — ~25% structural change estimate" |
| Part 1 commit-format lint gap | part-1 §E Laws "Commit messages MUST follow [area] format"; not yet machine-checkable |
| Part 2 UND-4 gate packet schema | dependency-graph.md §4.4 UND-4 "gate_class field distinguishing STOP gate" |
| Part 2 PARA-tier enforcement gap | part-2 §E Deontics "MUST tag every draft with para_tier"; knowledge-management-karpathy-luhmann-matuschak.md §6 Part 2 item 1 |
| Part 2 multi-owner gate scalability | dependency-graph.md §6.2 "~35% structural change — ABOVE 30%" + OQ-6 |
| Part 3 C1 accessor pipeline ownership | dependency-graph.md §3.1 C1 "BLOCKING for Wave C task assignment" |
| Part 3 methodology sub-layer gap | candidate-parts-merged.md §2 Part 3 "methodology library not yet consistently populated — Wave C materialisation needed" |
| Part 3 UND-5 CRM edge validation | dependency-graph.md §4.5 UND-5 "asymmetric view of who writes edges.jsonl" |
| Part 3 /ask --save gap | part-3 §E Deontics "/ask --save MUST file to wiki/comparisons/ by default"; knowledge-management-karpathy-luhmann-matuschak.md §6 Part 3 item 3 |
| Part 4 routing table gap | part-4 §H "routing table as declarative YAML — Wave C primary gap"; candidate-parts-merged.md §2 Part 4 AUDIT |
| Part 4 C1 resolution | dependency-graph.md §3.1 C1 "Part 4 must explicitly accept or reject" |
| Part 4 UND-1 DRR schema | dependency-graph.md §4.1 UND-1 |
| Part 5 compound ritual gap | part-5 §H "Wave C primary gap: methodology library sub-layer"; compounding-engineering.md |
| Part 5 UND-3 promotion pipeline | dependency-graph.md §4.3 UND-3 |
| Part 5 OQ-MERGED-2 dissent | candidate-parts-merged.md §6 OQ-MERGED-2; part-5 §H dissent preserved |
| Part 6 F-G-R scanner gap | candidate-parts-merged.md §2 Part 6 "NOT yet a systematic Part-owned function" |
| Part 6 blast-radius table OQ-MERGED-6 | candidate-parts-merged.md §6 OQ-MERGED-6; part-6 §E Laws "Default-Deny on uncategorized" |
| Part 6 TRADEOFF-01 | dependency-graph.md §7 OQ-1 "MUST be resolved before Wave C Part 8 spec"; systems-thinking-cybernetics.md §4 Beer VSM S3 |
| Part 6 C4 edge correction | dependency-graph.md §3.4 C4 "PhaseOf → methodologically-uses correction" |
| Part 7 project schema gap | candidate-parts-merged.md §2 Part 7 "Wave C materialisation needed"; part-7 §H Wave C bullets |
| Part 7 IP-5 whitelist | A-1-critic-gate.md §6 item 1; part-7 §H FLAG-MAJOR correction |
| Part 7 cadence alignment OQ-5 | dependency-graph.md §5.3 "GAP — Part 7 does not declare cadence alignment"; OQ-5 |
| Part 8 SLI/SLO schema gap | part-8 §H "Wave C bullets: define SLI/SLO schema — M effort"; dependency-graph.md §3.2 C2 |
| Part 8 C2 health signal schema | dependency-graph.md §3.2 C2 "no agreed schema between emitter and collector" |
| Part 8 dashboard templates | part-8 §H "Wave C bullets: weekly dashboard S; quarterly immune audit M" |
| Part 8 alert routing stub | part-8 §H "stub alert-routing interface to Part 6 — S effort" |
| Part 9 daily-log schema gap | part-9 §H Wave C bullets; FUNDAMENTAL §2.6 |
| Part 9 weekly review schema | part-9 §H Wave C bullets; levenchuk-shsm-fpf.md §4 P7 IP-7 |
| Part 9 3-tier SLA taxonomy | part-9 §H Wave C bullets; FUNDAMENTAL §4.2 |
| Part 10 L.1-L.3 stubs | part-10 §F "L.1-L.3 Phase-A stubs ONLY"; candidate-parts-merged.md §2 Part 10 |
| Part 10 C3 clarification | dependency-graph.md §3.3 C3 "ambiguity must not propagate to Phase-B design" |
| Part 10 privacy architecture | A-1-critic-gate.md §6 item 5; part-10 §E Laws FUNDAMENTAL §6.4 |
| Part 10 fork-separation OQ-MERGED-3 | candidate-parts-merged.md §6 OQ-MERGED-3 |
| Bundle composition build order | dependency-graph.md §2.5 topological sort (Layer 0-5) |
