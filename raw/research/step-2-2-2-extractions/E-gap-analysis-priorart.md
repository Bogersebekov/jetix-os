---
title: "Sub-agent E extraction — FPF gap analysis + prior-art KB"
date: 2026-04-23
sources: [fpf-gap-analysis-2026-04-20.md, levenchuk-fpf-knowledge-base-2026-04-20.md]
pipeline: ingested
---

# Sub-agent E — Extraction

Scope: `fpf-gap-analysis-2026-04-20.md` (2486 lines, 65/100 alignment)
+ `levenchuk-fpf-knowledge-base-2026-04-20.md` (2456 lines, draft).
GA = gap-analysis, KB = KB. Step-2.2.2 tag: **[R]** relevant to
skeleton; **[D]** broader/deferred.

---

## Part 1 — Previously identified gaps (GA)

All gaps are status: **open** (pending Ruslan review per GA §8). No tracker
field. Severity per GA §1.4 / §3 headers.

### 1.1 Top-5 critical gaps (GA §1.4, §3)

- **G1. Boundary Unpacking A.6.\*** (~10K FPF lines: A.6, A.6.B Boundary
  Norm Square, A.6.C Contract Unpacking, A.6.0 U.Signature, A.6.P
  Relational Precision, A.6.Q Quality Term, A.6.A Action Invitation,
  A.6.H Wholeness). "Effectively unaddressed в Jetix". No L/A/D/E
  (Law/Admissibility/Deontics/Work-Effects) routing in contracts, DPAs,
  SKUs, SLAs. Severity: CRITICAL (DACH compliance). Remediation: Rec-01.
  Cite: GA §1.4, §3.6. **[D]**
- **G2. Trust & Assurance B.3 F-G-R.** Jetix J-Auto/J-Approve/J-Strategic
  = policy-gate heuristic, not Formality+ClaimScope+Reliability triad.
  No pathwise reliability; no CL cross-context penalty. "Art.22 GDPR
  defence weaker". CRITICAL. Remediation: Rec-04. GA §1.4, §3.14. **[D]**
- **G3. Characteristic Space A.17-A.21.** "Полностью отсутствует". No
  CHR-NORM, CSLC-KERNEL (Characteristic/Scale/Level/Coordinate),
  CharacteristicSpace mechanisms (UNM/UINDM/USCM/ULSAM/CPM/
  SelectorMechanism), MM-CHR. SKU pricing, direction kill criteria,
  agent promotions — all informal. MAJOR. Remediation: Rec-11 (Phase 2).
  GA §1.4, §3.11. **[R]** for agent-promotion CSLC; **[D]** for SKU.
- **G4. Unified Term Sheet F.17 + LEX-BUNDLE E.10.** Bilingual frontmatter
  partial; no UTS table; glossary not an artifact; SenseCells ≥3-contexts
  rule unmet. Ontological-drift risk for 18 agents + hires. CRITICAL.
  Remediation: Rec-02. GA §1.4, §3.20. **[R]** (vocabulary lock).
- **G5. Multi-View Publication E.17 + Transduction Graph E.18.** Same
  artifact for engineers/managers/clients/auditors without
  Viewpoint+View+Correspondences. Bilingual solves language only. MAJOR.
  Remediation: Rec-09. GA §1.4, §3.19. **[D]**

### 1.2 Coverage by cluster (GA §3.23)

Full/Partial/None, %. Weakest: A.6.\* 11%, A.16 0%, A.17-A.21 0%, D
10%, F 14%, G 18%. Strongest: A.15.\* 64%, A.7-A.13 61%, A.0-A.5 60%.
Full: A.0-A.5 3/6/1; A.6 0/2/16; A.7-A.13 3/5/1; A.14 0/3/1; A.15
4/2/1; A.16 0/0/4; A.17-A.21 0/0/7; B 1/8/4; C 3/14/8; D 0/1/4; E
7/8/7; F 1/3/14; G 0/5/9; H-K 0/2/2. Total 22/59/79 of 160.

### 1.3 Per-pattern unused / UNDER-SPECIFIED (GA §3.\*, all status open)

**[R]** skeleton-relevant:
- A.1.1 U.BoundedContext — implicit via `direction:`; drift risk (§3.1).
- A.2.2-A.2.9 (Capability / PromiseContent / RoleAlgebra / Commitment /
  SpeechAct / EvidenceRole) — not typed; Deal doesn't capture "what is
  promised structurally" (§3.2).
- A.3 Transformer Quartet — "not named" (§3.3).
- A.5 Open-Ended Kernel/Extension — no kernel-vs-extension declaration
  (§3.5). UNDER-SPECIFIED.
- A.13:4.3 Agency-CHR — 3-tier vs FPF spectrum ambiguous (§3.7).
- A.14 typed partonomy (ComponentOf / ConstituentOf / PortionOf /
  PhaseOf / MemberOf) — flat "part-of" only (§3.8).
- C.18 NQD-CAL + C.19 E/E-LOG + C.19.1 BLP — "biggest missed
  opportunity" for Portfolio/Direction (§3.17).
- E.3 Precedence (Gov≫Arch≫Epist≫Prag≫Did) — not used (§3.19).
- E.5.1 DevOps Lexical Firewall — Jetix "actively violates" ("yaml",
  "git", "pre-commit") (§3.19).
- E.5.3 Unidirectional Dependency (Core→Tooling→Pedagogy) — "not
  enforced" (§3.19).
- E.10 LEX-BUNDLE + Conceptual Prefixes — not used (§3.19).
- E.15 Lexical Authoring & Evolution — not used (§3.19).
- E.20 MIP — ad-hoc additions (§3.19).
- H-K lexical-debt map — sparse; "axis", "dimension", "generality"
  deprecated per K, "could help avoid deprecated terms" (§3.22).
  UNDER-SPECIFIED.

**[D]** broader / deferred:
- A.6.9 Cross-Context Sameness partial via `sames-as-crm`, no CL (§3.6).
- A.15.1:5 Work mereology — alpha-log flat (§3.9).
- A.16 full cluster — no typed move-family in inbox (§3.10).
- B.1 Γ flavours — Γ_sys implicit only (§3.12).
- B.2 MHT — acknowledged, not applied (§3.13).
- B.3 F/G/R — no F-scale, ClaimScope, Reliability (§3.14).
- B.5.2.1 Creative Abduction w/ NQD — not used (§3.16).
- C.2.1 U.EpistemeSlotGraph — wiki 9 types "informal; no slot graph"
  (§3.17).
- C.6 / C.7 / C.17 / C.20 / C.22 / C.23 / C.25 CALs+CHRs — not used
  (§3.17).
- D.5 Bias-Audit — "directly operational for EU AI Act" (§3.18).
- E.17.EFP / E.17.AUD.\* / E.18 E.TGA — not used (§3.19).
- F.1-F.3 / F.6-F.8 / F.10-F.13 / F.15 / F.16 / F.18 — mostly unused
  (§3.20).
- G cluster — "consumer, not producer" Phase 1 (§3.21).

### 1.4 Gaps on the prior-art KB itself (KB §8.4)

Secondary researches R-A..R-E missed but FPF-Spec covers: A.6.\*
Boundary depth, E.17.\* Multi-View Kit, E.18 Transduction Graph,
A.17-A.21 Characteristic Space, A.6.S Constructor Signature, C.18/C.19
NQD/E-E-LOG depth. Status: open.

---

## Part 2 — FPF KB structure

Document = unified reference, not a KB for agents. ~25K words / ~60 pages,
status draft (KB frontmatter).

### 2.1 Taxonomy

Three parallel registers (KB §§3-5):

1. **FPF pattern IDs A.X.Y.Z** — formal, AI-friendly (KB §5).
2. **ШСМ 5 primitives** — pedagogical, Russian: роль / альфа / граф
   создания / стратегирование / мышление письмом (KB §3). ⚠ KB flags:
   not Левенчук's published list; R-B's synthesis.
3. **16 trans-disciplines** (2023 canonical, not 17) — intellect-stack
   hierarchy (KB §4).

### 2.2 Entities (~30 U.Types; KB §9.2)

Holon layer: U.Entity, U.Holon, U.Boundary, U.Interaction, U.System,
U.Episteme, U.BoundedContext (A.1, A.1.1). Role layer: U.RoleAssignment
(Holder#Role:Context), U.Capability, U.PromiseContent, U.EvidenceRole,
U.RoleStateGraph, U.RoleAlgebra, U.Commitment, U.SpeechAct (A.2.1-9).
Method: U.Method, U.MethodDescription, U.Dynamics (A.3.1-3). Boundary:
U.Signature, U.Mechanism, U.EpistemicViewing, U.RelationSlotDiscipline
(A.6.0-5). Work: U.Work, U.WorkPlan (A.15.1-2). Knowledge/Kind:
U.Episteme.SlotGraph (6 slots: DescribedEntity, GroundingHolon,
ClaimGraph, Viewpoint, View, ReferenceScheme — C.2.1), U.Kind,
U.RoleMask (C.3.1/4). Reasoning: U.AbductivePrompt (B.5.2.0),
U.MultiViewDescribing (E.17.0), U.LanguageStateSpace (C.2.2a).

Sub-categories: roles (A.2, A.13); practices/methods (A.3, C.4);
~25 CALs/LOGs/CHRs in Part C (Sys-CAL, KD-CAL, Kind-CAL, Method-CAL,
Resrc-CAL, Decsn-CAL, Norm-CAL, NQD-CAL, E/E-LOG, Agency-CHR, MM-CHR,
Creativity-CHR, Discipline-CHR, Problem-CHR, Q-Bundle). Alphas = ШСМ
term; ⚠ "FPF-Spec doesn't preserve 'alpha' as standalone term" —
dispersed into U.RoleStateGraph / U.Episteme / U.System / U.Work /
PhaseOf (KB §3.3 CONFLICT).

### 2.3 Organization — hierarchical, multi-layer

- **Pattern-ID nesting:** 11 Parts A-K → sub-patterns A.X.Y.Z (KB §5.5).
  Part A Kernel (lines 767-25,578) immutable; Part B Reasoning; Part C
  Extensions pluggable; Part D Ethics (mostly stub); Part E
  Constitution; Part F Unification; Part G SoTA Kit; Parts H-K
  navigation (sparse).
- **Intellect-stack dependency lattice** (16 disciplines, KB §4.4):
  foundation (Понятизация → Собранность → Семантика → Математика →
  Физика) → formal reasoning → knowledge → coordination/norms →
  methodology → systems engineering. "True structure is a graph
  (lattice), not a sequence".
- **Mereological 3-level:** target / creating / supersystem (KB §3.4).
- **Constitutional:** 11 Pillars P-1..P-11 + precedence "Gov ≫ Arch ≫
  Epist ≫ Prag ≫ Did" (KB §5.8, E.3).

### 2.4 Operational vs descriptive

**Operational** (procedures/gates/checklists): DRR 4-part record (E.9,
KB §5.6.4); UTS table (F.17, §5.6.5); 6 entry routes (project
alignment, language-state, boundary unpacking, lawful comparison,
generator/SoTA, same-entity rewrite — §5.2); 4 Guard-Rails E.5.1-4
(§5.9); D.5 BA-Cycle (BA-0→BA-1→BA-2→BA-3); BOSC-A-T-X triggers for
MHT (B.2); Γ operator + invariants WLNK/MONO/IDEM/COMM/LOC (B.1);
F-G-R triad, F0-F9; NQD Γ-ops (generate / updateArchive / illuminate /
selectFront) + E/E-LOG actions (Widen / Keep / Narrow / Sunset /
Reroute) (§5.6.10); past-participle checklist; Inside/Outside 3-step
test (dependency / interaction / emergence) (§5.6.1); E.20 MIP
(Problem→Mechanism→Interface→Pilot→Promote).

**Descriptive** (ontology / lineage): biography + lineage (§2); U.Type
catalogue; 11 Pillars essences (E.2); 3-tier root ontology
U.Entity/U.Holon/{U.System, U.Episteme}; mereology lineage (§7); 9 big
storylines (§5.7); ~100-entry glossary RU↔EN + U.Type table (§9).

---

## Part 3 — Already-proposed FPF integrations

GA has 22 numbered recs (§6) P1×6 / P2×10 / P3×6 + 11 OQs. **None
marked accepted/rejected** — all pending Ruslan review (GA §8).
Eleven prior Ruslan overrides (GA §2.10) are the only decided items;
all 11 are "+Левенчук direction" (more discipline); zero toward
"less discipline, more pragmatic".

### 3.1 Agent structure proposals (all **[R]** unless marked)

- **P3.A. Full FPF in every agent system.md** (~7-10K tokens) — Override
  #10, DECIDED (GA §2.6, §5.9).
- **P3.B. FPF-Steward sub-role on meta-agent** — Override #11; quarterly
  audit; output `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md`;
  split-off trigger: 30+ agents OR 1+ human meta-hire OR audit >4h
  (GA §5.4). DECIDED.
- **P3.C. 18-manifest multi-role-binding** — 5 Ruslan atomic sub-roles +
  11 agent roles + 2 Phase-2a stubs + per-executor compute contract
  (model_preference, fallback_models, thinking_mode,
  max_tokens_per_session, cache_strategy, latency_class,
  escalation_rules) (GA §5.3). DECIDED; candidate contribution-back as
  "Multi-Role-Binding Agent Architecture" extending A.2.1.
- **P3.D. 5-block role.md** (identity / ontological / method /
  production_dependencies / evolution) — Divergence 6: "Keep + cross-link
  appendix to F.4 RCS+RoleStateGraph+Checklists" (GA §4.6).
- **P3.E. F.6 Six-Step Role Assignment Cycle** — Rec-15 P2: expand
  `agent_onboarding` into candidate-id → context-binding →
  capability-check → assignment → warm-up → calibration; 3-5h (GA §6).

### 3.2 Alpha-ownership proposals

- **P3.F. 8 True Alphas** (Client / Project / Deal / Content Item /
  Hypothesis / Member / Way of Working / Direction); past-participle;
  Hook 4 strict. DECIDED; Divergence 4 "Keep strict" (§2.4, §4.4). **[R]**
- **P3.G. Direction alpha** — Override #8; states hypothesized→
  under-validation→validated→activated→scaled→plateaued/invalidated/
  dropped→archived. Divergence 3 "Keep; document as extension" (§4.3,
  §5.1). Rec-07 P2 (6-10h): map to C.18 NQD-CAL (Γ_nqd.generate /
  updateArchive / illuminate / selectFront) + C.19 E/E-LOG + C.19.1
  BLP (§6). **[R]**
- **P3.H. A.14 typed edges** — Rec-05 P1 (2-4h): relabel "part-of" to
  ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf (§6,
  §3.8). **[R]** if in manifests.
- **P3.I. Alpha-flavour split** — §3.2 narrative: Jetix flattens
  role-states (Client/Member) + entity-states (Project/Deal/
  ContentItem/Hypothesis/Direction) + method (WayOfWorking) into
  uniform 8-alpha; FPF would split Client ≈ U.RoleAssignment, Project
  ≈ U.Work phase, Deal ≈ U.Commitment. Flagged, no numbered rec. **[R]**

### 3.3 Ritual proposals (all **[D]**)

Rec-14 P2 (1-2h): map 4 rituals to B.4 Observe→Notice→Stabilize→Route
(§6, §3.15). Rec-03 P1 (3-5h setup + 2h/audit): D.5 BA-Cycle quarterly
or per-SKU; output `decisions/bias-audit/YYYY-QN-bias-audit.md`; Phase 1
simplified (§6). Rec-22 P3 (2-4h, calendar-bound): first FPF-Steward
audit 2026-Q2 — concept-duplication scan, past-participle residuals,
role-manifest integrity, Direction-concept boundary, frontmatter
schema, UTS delta (§6). Rec-06 P1 (2-3h): map phase transitions to B.2
MHT events (Fission / Phase Promotion / Role-Lift / Fusion / Context
Reframe) with BOSC-A-T-X tags (§6). OQ-10: quarterly upstream FPF sync
inside FPF-Steward audit ~30-60 min/Q (§7; KB §11.5 Q15).

### 3.4 Other (template / policy / wiki artifacts)

Rec-01 P1 boundary templates 4-6h [D]; Rec-02 P1 UTS skeleton
`wiki/foundations/jetix-uts.md` 30-50 rows 6-10h [R]; Rec-04 P1 F+R
frontmatter on ADRs/deliverables 3-5h [R] if on manifests; Rec-08 P2
Agency-CHR fallback 2-3h [R]; Rec-09 P2 Multi-View 8-15h [D]; Rec-10 P2
F.9 Bridge+CL (cl:A/B/C/D) 2-3h [D]; Rec-11 P2 A.18 CSLC 8-12h [R]
agent-promotion only; Rec-12 P2 LEX-BUNDLE prefixes (alpha.\* /
role.\* / direction.\* / method.\* / sku.\*) 3-5h [R]; Rec-13 P2 D6
Core/Tooling split 4-8h [R]; Rec-16 P2 C.22 TaskSignature 3-5h [D];
Rec-17 P3 A.16 cue-pack 4-6h [D]; Rec-18 P3 F.11 Method Quartet 5-8h
[R]; Rec-19 P3 A.6.S Signature Pair 3-5h [D]; Rec-20 P3 E.20 MIP 2-3h
[R]; Rec-21 P3 G.5 MethodFamily Registry 4-6h [D]. Totals: P1 20-33h,
P2 42-71h, P3 20-32h, grand 82-136h (§6.3).

---

## Part 4 — Contradictions / open questions

### 4.1 Divergences Jetix↔FPF (GA §4 verdicts)

D1 "FPF" name collision (Jetix derivative vs Левенчук canon) → revisit;
prefer "JETIX-FPF". D2 5 primitives vs 11 Pillars → keep both. D3
Direction alpha (Jetix innovation) → keep; document as extension. D4
past-participle strict (Hook 4) vs FPF "SHOULD" → keep strict. D5
"Model D" not in FPF-Spec → add English expansion in D6. D6 5-block
role.md vs FPF F.4 → keep + cross-link appendix. D7 3-tier agency vs
FPF multi-grade spectrum → keep + Agency-CHR fallback. Verbatim: "0
reversals recommended. 2 minor fixes (Divergences 1 and 5). 5
validated as intentional" (§4.8).

### 4.2 Unresolved tensions (verbatim where possible)

- **T1. "FPF" attribution** (§4.1): "Attribution.md requires crediting
  Levenchuk FPF — naming our derivative 'FPF' creates attribution
  confusion." MEDIUM. **[R]**
- **T2. Past-participle edge cases** (§4.4): "'in-progress' state might
  be legitimate where event granularity is coarse — Jetix Hook 4 may
  false-positive. Mitigation: `past-participle-exempt: true`." **[D]**
- **T3. Alpha dispersion** (KB §3.3, §8.3 Conflict 1): R-B treats Alpha
  as 1st-class primitive ✅; "FPF-Spec doesn't preserve 'Alpha'
  terminology" — split into U.RoleStateGraph / U.Episteme / U.System /
  U.Work / PhaseOf. Resolution: "FPF primary. For Jetix: bridge
  mapping required." **[R]**
- **T4. "5 primitives" provenance** (KB §3 preamble, §8.3 Conflict 3):
  "Per R-C Section 4: 'they do not appear as a named canonical list of
  5 primitives in any single source found.' 5-primitive framing is
  R-B's analytical synthesis, не Левенчук's own publishable taxonomy."
  **[R]**
- **T5. 16 vs 17 disciplines** (KB §4.2, §8.3 Conflict 2): marketing
  "17" (2021) vs canonical "16" (2023). Resolution: 16. **[R]**
- **T6. E.5.1 DevOps Lexical Firewall violation** (GA §3.19): "Jetix
  actively violates (FPF text uses 'yaml', 'git', 'pre-commit' —
  tooling tokens)." **[R]**
- **T7. E.5.3 Unidirectional Dependency violation** (GA §3.19): "Jetix
  FPF text references Jetix folder structure (Sections discuss
  `finance/`, `alphas/`) creating reverse dependency (Pedagogy →
  Core)." **[R]**
- **T8. AI-агенты не стратегируют** (KB §3.5, §11.3 Q8): principled
  Левенчук stance; operational reality may require adapt-mode method
  choice. Rec: "Hard constraint for true invent-mode strategizing; AI
  can do adapt-mode method selection с founder oversight." **[R]**
- **T9. License** (KB §11.5 Q13): "No formal license, citation
  requested only. Public Jetix-FPF derivative may need clarification от
  author." **[D]**
- **T10. H-K sparsity + semiotics lag** (KB §11.4 Q10-Q12): Parts H-K
  sparse in vendored 2026-04-20 copy; D mostly stubs; semiotics
  workstream (April 2026) not yet in vendored FPF-Spec. **[D]**

### 4.3 Open questions (all pending Ruslan)

GA §7 OQ-01..11 with Claude recs: OQ-01 name collision → "JETIX-FPF"
[R]; OQ-02 P1 scope → adopt all 6 (+20-30h) [R]; OQ-03 Portfolio-NQD →
separate wiki artifact Phase 1 [R]; OQ-04 E.17 Multi-View → pilot first
Audit SKU [D]; OQ-05 F-G-R scope → ADRs + client deliverables [R];
OQ-06 Model D → expand in D6 [R]; OQ-07 Core/Tooling → soft split [R];
OQ-08 UTS timing → concurrent with D6 [R]; OQ-09 contribute back →
soft engagement [D]; OQ-10 upstream sync → quarterly integrated [D];
OQ-11 agent promotion → hybrid optional CSLC [R].

KB §11 Q1-Q15 (subset): Q1 Альфа vs U.Type → hybrid (alpha=Plain,
U.Type=Tech per LEX-BUNDLE) [R]; Q3 5 primitives vs IDs → 5 for
exec/onboarding; IDs for technical [R]; Q7 FPF strict-vs-Lite in agents
→ KB rec "Lite for Phase 1; strict only for strategist + knowledge-synth"
⚠ SUPERSEDED by Override #10 (full FPF everywhere) [R]; Q8 AI-strategizing
hard constraint → hard invent-mode only [R]; Q9 past-participle → adopt
[R]; others (Q2, Q4-6, Q10-15) [D].

---

## Part 5 — Step-2.2.2 applicability summary

**[R] skeleton-relevant:** UTS lock (G4, Rec-02); U.Type taxonomy in
role manifests (A.2.2-9, A.3, A.5, A.13, A.15); 5-block role.md + F.4
cross-link (P3.D); F.6 onboarding (P3.E / Rec-15); Full-FPF permeation
(P3.A / Override #10); FPF-Steward on meta-agent (P3.B); 18-manifest
architecture (P3.C); 8 alphas incl. Direction + NQD formalization (P3.F
/ P3.G / Rec-07); A.14 typed edges in manifests (P3.H / Rec-05);
alpha-flavour split (P3.I); Agency-CHR fallback (Rec-08);
agent-promotion CSLC (Rec-11 subset); LEX-BUNDLE prefixes (Rec-12);
Core/Tooling split (Rec-13); MIP for skeleton edits (Rec-20); Method
Quartet (Rec-18); E.3 precedence + E.5.1/E.5.3 guard-rail compliance +
E.10/E.15 lexical discipline; lexical-debt avoidance (K); OQ-01/05/06/
07/08/11, Q1/Q3/Q7/Q8/Q9; tensions T1, T3-T8.

**[D] deferred:** contract/DPA templates (G1, Rec-01); F+R trust tags
outside manifests (G2, Rec-04); SKU CSLC (Rec-11 subset); Multi-View
Kit (G5, Rec-09); F.9 Bridge+CL (Rec-10); bias-audit ritual (P3.K);
phase-MHT mapping (P3.M); B.4 ritual labels (P3.J); upstream sync
mechanics (P3.N, OQ-10); TaskSignature intake (Rec-16); inbox cue-pack
(Rec-17); SKU signature pair (Rec-19); MethodFamily Registry (Rec-21);
alpha-log mereology (A.15.1:5); Γ-flavour ledgers (B.1); inbox
language-state (A.16); episteme slot graph (C.2.1); Transduction graph
(E.18); E.17 audit stances; license (T9); H-K/semiotics (T10).

*END.*
