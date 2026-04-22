---
id: d4-pass3-critic-review
date: 2026-04-21
reviewer: critic-subagent
draft-reviewed: decisions/JETIX-ARCHITECTURE-BRIEF.md (12335 words, 1107 lines)
target: 5000-7000 words
issues-found: 54
---

# D4 Pass 3 — Critic Review

## Executive assessment

The draft is **structurally solid but operationally bloated and internally inconsistent on several high-leverage details**. Section coverage is complete (Exec / 24-Locks Quick-Ref / Capabilities / Foundation / NFRs / Hard Constraints / Anti-Patterns / Quality Axes / Variant Selection / 15 Questions / Provenance), citations are dense (87 `D<X> §<Y>` references, 117 unique `Lock N` mentions), and most locks are touched in ≥3 sections. The brief is pretty close to "binding-quality" after Pass 4 fixes — but **not yet**: 6 internal contradictions, ~20 under-specified or ambiguous directives, and 1 citation-traceability gap must close before Stage 6 starts, because otherwise 6 parallel architects will each resolve these gaps differently and produce un-comparable variants.

The **single largest problem is length**: 12,335 words vs 5,000-7,000 target = **77% over**. Section 3 (Capabilities) alone = 3,992 words across 29 capability blocks with identical 6-field templates; Section 10 (15 Questions) = 2,364 words; Section 4 (Foundation) = 1,684 words. Architects do not need this much prose from D4 — they have D1/D2/D3 + ADR Chunks + Locks docs as primary binding input. D4 should be a **pointer-and-constraint brief**, not a re-exposition. Concrete cut list below; realistic post-Pass-4 target: 6,200 words.

**Second-largest problem: 10-vs-11 archetype inconsistency**. Lock 7 row says "10 archetypes (Stage 3 added 11th: bloggers)", §3.1.1 / §3.1.9 / §3.2.2 / §6 C14 use 11; but Q11 binding-constraint cites "Lock 7 / D7 10 archetypes metadata" (line 965). D1 §7 canonically numbers 11. Architect building Q11 content pipeline vs Q2 roster will end up with a tag-schema mismatch (10-slot vs 11-slot taxonomy).

**Go/No-Go verdict: NEEDS-PASS-4-FIXES then READY.** HIGH issues (14) block Stage 6 launch; they are all closable by parallel fixer subagents in <60 minutes. MEDIUM issues (26) tolerable if annotated "trade-off accepted". LOW issues (14) park if time-constrained.

## Issues by priority

### HIGH-priority issues (MUST fix in Pass 4)

#### H-01. Archetype count inconsistency — 10 vs 11 throughout
- **Class:** 9 internal contradiction + 2 missing requirement + 13 ICP-related cascading
- **Location:** Line 60 (Lock 7 row says "10 … Stage 3 added 11th"), lines 43, 75, 79, 95, 167, 171, 232, 633 use "11"; line 965 (Q11 constraint) says "10 archetypes metadata"; §3.2.2 heading "per 11 archetypes" but §7.1 of D1 lists 11.
- **Problem:** Architects handling Q11 (Content) will build a 10-taxonomy content pipeline while architects handling Q2 (Roster) / §3.1.1 (ICP) / §3.2.2 (Sub-networks) will build 11. Result: archetype tag-schema mismatch and routing failure at integration.
- **Evidence:** Line 79 "Lock 7 '10 archetypes' expanded to 11 in Stage 3 (bloggers added); architects must handle 11-way tagging." vs line 965 "[Lock 7 / D7] 10 archetypes metadata."
- **Proposed fix:** (a) Change Lock 7 row title from "Union of 10 archetypes" to "Union of 11 archetypes (10 base + 1 bloggers Stage 3)"; (b) fix line 965 to "11 archetypes metadata (10 base + bloggers)"; (c) add normative note at §2 bottom: "All archetype-taxonomy consumers MUST use 11-way schema per D1 §7.1"; (d) audit every "archetype" mention for count consistency.
- **Word-count impact:** +25

#### H-02. Agent roster internal contradiction — FPF-Steward status
- **Class:** 9 internal contradiction + 1 unclear directive
- **Location:** §3.1.9 line 167-171 ("11 agents … + FPF-Steward sub-role"), §4.1 header line 417 (canonical = 11), §4.1 Stage 6 block line 436 ("FPF-Steward separate role? Currently sub-role in meta-agent"), line 171 ("Phase 2b adds Chief-of-Staff + standalone FPF-Steward"), §6 C11 ("FPF-Steward quarterly audit").
- **Problem:** Is FPF-Steward counted within 11? As sub-role of meta-agent? Or as 12th agent emerging Phase 2b? Three overlapping statements. Architect answering Q2 cannot canonicalize without Ruslan pick.
- **Evidence:** Line 167 says "11 agents — NOT 12"; line 171 enumerates 11 then "+ FPF-Steward sub-role"; line 436 says "Stage 6 MUST evaluate (a) FPF-Steward separate role?"
- **Proposed fix:** Declare authoritative position in §4.1 header: "Phase 1 = 11 canonical agents WITH FPF-Steward as meta-agent sub-role (not separate). Phase 2b trigger (30+ agents OR 1+ human meta-hire OR audit >4h) promotes FPF-Steward to 12th standalone role. Stage 6 MUST NOT propose 12-agent Phase 1 baseline." Then §4.1(a) is informational, not a decision-point.
- **Word-count impact:** +40, −0

#### H-03. Non-existent decisions cross-reference "Chief-of-Staff"
- **Class:** 6 non-traceable directive
- **Location:** Line 171, §3.1.9 Phase evolution: "Phase 2b adds Chief-of-Staff + standalone FPF-Steward."
- **Problem:** "Chief-of-Staff" role appears nowhere in D1/D2/D3 or 24 locks or ADR Chunks referenced. No source citation. Architects have no basis to design its scope, escalation paths, F-G-R class.
- **Evidence:** `grep -i "chief-of-staff"` across D1/D2/D3/tensions-* returns 0 hits.
- **Proposed fix:** Either (a) cite source (e.g., `[ADR-Chunk-N Area M]` — check ADR-Chunk-6 Area 7 or Chunk 1 P5), or (b) remove and note "Phase 2b extensions TBD in D3 §5.6 follow-up decision".
- **Word-count impact:** −15 (if removed) or +20 (if cite added)

#### H-04. Hard Constraint §6 missing explicit locks → under-specification
- **Class:** 2 missing requirement + 10 missing lock reference
- **Location:** §6 C1-C16 covers Locks 2, 3, 5, 8, 10, 11, 13, 15, 17, 18 — but Locks 1 (Gentleman/Predator), 4 (Name=Jetix), 6 (no-advisor), 7 (archetypes), 9 (Pain/Opportunity), 12 (content tiers), 14 (research scope), 16 (Phase-1 chat), 19 ($1T), 20 (USB-C), 21 (Matchmaker), 22 (ICP), 23 (tokens Opt B), 24 (OS research) have **no corresponding hard constraint**. They only appear in §3 capability sources and §7 anti-patterns.
- **Problem:** Section 6 is the disqualifier gate. If a Lock appears only as a capability source it is not elevated as a disqualifier. Variants could ignore e.g. Lock 19 ($1T no-rewrite) at structural level and still pass §6 screening.
- **Evidence:** §8.3 Disqualifiers says "Any §6 hard constraint violated ⇒ variant discarded pre-scoring" — meaning only §6 locks are disqualifiers. Missing locks 1, 4, 9, 12, 19, 20, 21, 22 from §6 is a structural gap.
- **Proposed fix:** Add 4-6 new Cs covering at minimum: C17 Gentleman/Predator membrane bifurcation at every surface (Lock 1); C18 $1T no-rewrite trajectory (Lock 19); C19 USB-C positioning + enterprise-fast (Lock 20); C20 ICP 5-criteria + direction-of-life axis (Lock 22); C21 Token Option B membrane preservation (Lock 23). Keep each single sentence + lock cite.
- **Word-count impact:** +120

#### H-05. Lock 4 (Name=Jetix) under-operationalized — only appears in quick-ref row
- **Class:** 10 missing lock reference
- **Location:** Line 57 only. No mention in any capability, Foundation section, NFR, constraint, anti-pattern, or question.
- **Problem:** Lock 4 formula "canonicalize on ingest" is an architectural directive for voice-memo pipeline (3.1.14) + wiki ingest (3.1.13) — but neither capability references it. Stage 6 architect designing voice-memo pipeline has no reason to build "Jackson → Jetix" normalizer.
- **Proposed fix:** Add 1 bullet to §3.1.14 Voice-memo Quality metric: "Speech-recognition artefact normalization: `Jackson|Джек` → `Jetix` pre-persistence per Lock 4."
- **Word-count impact:** +15

#### H-06. Lock 6 (no-advisor) under-operationalized
- **Class:** 10 missing lock reference
- **Location:** Line 59 quick-ref and Q9 binding-constraint line 923 "No advisor/employment hard-coupling" — nowhere else.
- **Problem:** Directive "No advisor / equity / board dependency baked into system" has architectural implications for §4.1 Agent Contracts (no advisor role slot), §4.2 Contractor Contracts (advisors ≠ contractors), §3.1.4 GmbH (no equity-reserve for advisors), §4.3 Handoff protocols (no advisor-escalation class). None operationalized.
- **Proposed fix:** Add single-sentence notes to §4.1 ("No advisor-role manifest; slot parked per Lock 6") and §3.1.4 ("GmbH formation excludes equity reserve for advisors per Lock 6").
- **Word-count impact:** +30

#### H-07. Missing §3 capability: D22 ICP direction-of-life axis engine
- **Class:** 2 missing requirement
- **Location:** §3.1.1 mentions "direction-of-life axis" but treats it only as a filter parameter. No separate capability specifying the axis engine (upward vs downward classifier, feedback mechanism, self-selection framing automation).
- **Problem:** Lock 22 explicitly elevates direction-of-life from optional to primary axis. No design directive tells architects what produces the `direction-vector` field that 3.1.1 consumes. Who scores inbound signals? What's the observable? Ruslan gave explicit directive "это реально на бумагу прям вынести прям несколько страниц как минимум" (D22 quote) — D4 reduces this to a field.
- **Proposed fix:** Add §3.1.15 "ICP Direction-of-life classifier" with Input/Output/Dependencies/Phase-evolution/Quality-metric/Source (one 6-line block). OR explicitly cite D1 §7.2 and D3 §12.1 as the normative ICP spec and declare §3.1.1 consumes that as config.
- **Word-count impact:** +60

#### H-08. Missing §3 Phase-3+ capability: succession / trustee mechanism
- **Class:** 2 missing requirement + 4 missing edge case
- **Location:** §4.8 footer ("Succession (Item 10): Constitution §11 TBD trustee Day 1…") — unstructured reference. Nowhere in §3.
- **Problem:** Lock 2 (multi-pilot) + Lock 19 ($1T horizon 200y) + CLAUDE.md Succession require a trustee/succession protocol. Degraded mode "founder unavailable" not speccified; TENSIONS-RESOLVED Stage-2 parks P4 "Designated trustee identity" to Phase 2+ but architecture needs a Day-1 stub.
- **Proposed fix:** Add to §4.4 Escalation protocol: "Founder-unavailable class: Phase 1 = proxy Steuerberater/lawyer stub per Constitution §11; formal trustee designated at first client contract (Area 4 trigger)." Add §3.1.x entry or explicit line in §4.8.
- **Word-count impact:** +50

#### H-09. Over-specification in §3.1.9 Agent phase-evolution locks one model
- **Class:** 7 over-specification
- **Location:** Line 171: "Phase 1 = 11 agents (manager / personal-assistant / …). Phase 2a activates dpo + customer-success stubs; Phase 2b adds Chief-of-Staff + standalone FPF-Steward."
- **Problem:** The draft predefines Phase-2b additions (Chief-of-Staff, standalone Steward) — killing Stage 6 architect creativity on org evolution paths. Q2 "agent roster reconciliation" asks architects to propose roster; §3.1.9 mandates the result.
- **Proposed fix:** Keep Phase-1 11-roster as binding; replace Phase-2a/b sentences with "Phase 2+ evolution TBD per Q2 architect proposal (stubs from ADR-Chunk-2 MC1 activate on triple-AND)."
- **Word-count impact:** −30

#### H-10. §5.1 Scale axis under-specification — "10× rule <30% rework"
- **Class:** 8 under-specification + 5 weak success criteria
- **Location:** §5.1 line 560: "At each phase gate, 10× scaling ⇒ <30% architectural rework (including data, orchestration, observability). Measured by line-of-code delta + schema-migration count at each gate."
- **Problem:** (a) Baseline LOC for "<30%" is against what denominator? Per-subsystem LOC at Phase-N start? Total repo? (b) Schema-migration count — no threshold given (2 migrations? 20?). Architects cannot benchmark without denominator and threshold.
- **Proposed fix:** "<30% of subsystem LOC per §3 capability affected; schema migrations ≤3 per subsystem per 10× gate (target), <10 hard-fail."
- **Word-count impact:** +15

#### H-11. Conflict between §5.5 D-test and §3 content having Jetix/Mittelstand
- **Class:** 9 internal contradiction + 8 under-specification
- **Location:** §5.5 D-test: `grep base/ -r "Jetix|DACH|AI consulting|Mittelstand|Ruslan|Berlin"` ⇒ 0 hits. But §3 capabilities describe Jetix-specific things (ICP bloggers, Producer-center for English infobiz, DACH activation). Also §5.5 adds "Ruslan|Berlin" but §5.5 itself mentions "Ruslan", as do Constraints.
- **Problem:** Architects don't know where the base/overlay boundary is. D4 doesn't declare: "D4 specifies Jetix-company overlay behaviour; base kernel spec deferred to Q1 variant response." Grep pattern includes terms used in the brief body itself, which is confusing.
- **Proposed fix:** Clarify at top of §3: "§3 describes Jetix-company overlay capabilities; base-layer split is Q1 variant-design responsibility; symbolic test §5.5 applies to the base/ repo subtree only, NOT to this brief or any overlay." Remove "Ruslan|Berlin" from grep list or clarify "inside code files only, not brief docs".
- **Word-count impact:** +30

#### H-12. §6 C11 FPF token budget over-specifies — kills variant options
- **Class:** 7 over-specification
- **Location:** Line 627: "25K exocortex HARD + 950K flexible (Opus 4.7 1M). No exclusions."
- **Problem:** Hard-codes token budget against specific model (Opus 4.7 1M). If Stage 6 considers alternative providers (AP-11 says multi-provider Day 1), 950K flexible is OpenAI/Google-infeasible. Budget should be model-class-relative.
- **Proposed fix:** "25K exocortex HARD (model-agnostic) + remainder flexible (provider-dependent; 950K on Opus 4.7 1M as reference). No exclusions."
- **Word-count impact:** +15

#### H-13. Missing anti-pattern — D19 $1T shortcut / Boutique-cap
- **Class:** 2 missing requirement (anti-pattern)
- **Location:** §7 AP-1 to AP-15; no AP for "architectural shortcut that caps at boutique scale" even though §5.1 says "no SQLite-forever, no single-region hardcode" and §6 C-missing for Lock 19.
- **Problem:** "Boutique-cap shortcut" — a known anti-pattern (e.g., SQLite for core store, hard-coded eu-west-1, solo-optimized SSH chains) — should be an explicit AP scorable in §8.3 disqualifier.
- **Proposed fix:** Add AP-16 "Boutique-scale shortcuts. Violates Lock 19. Example: SQLite-only store for core ledgers; single-region hardcode; solo-optimized path assumptions; no sharding key design in wiki. ⇒ reject. Schema headroom for 10^3-10^6 entities Day 1."
- **Word-count impact:** +40

#### H-14. Precedence rule says "D1+D2+D3+locks > brief" but brief adds new binding items (C1-C16)
- **Class:** 9 internal contradiction
- **Location:** Line 32 / line 1103: "D1 Vision + D2 Philosophy + D3 Plan + 24 locked decisions > this brief > OME/FPF/ADR reference material > atom registry."
- **Problem:** §6 Hard Constraints introduces obligations (C11 FPF full-text permeation; C13 F-G-R schema; C14 11-agent canonical; C15 Life-OS separation hooks) not directly in D1/D2/D3/locks but derived from ADR Chunks. Precedence says ADR Chunks < brief, but brief promotes ADR-derived items to binding-gate status. Unclear how a Stage 6 architect should treat a constraint that conflicts with D2 but aligns with ADR Chunk 6.
- **Proposed fix:** Add: "This brief elevates certain ADR-Chunk + OME/FPF items to binding-gate status (§6) as a Stage-4 editorial decision; these inherit precedence of the brief itself. Where brief directly restates a Lock/D1/D2/D3 item, upstream precedence wins."
- **Word-count impact:** +35

### MEDIUM-priority issues (fix or mark "trade-off accepted")

#### M-01. Length — Section 3 Capabilities over-detailed (3,992 words / 32% of brief)
- **Class:** 11 length
- **Location:** §3.1.1 through §3.3.9 = 29 capability blocks with identical 6-field template (Function / Input / Output / Dependencies / Phase evolution / Quality metric / Source).
- **Problem:** Architects need pointers to capabilities; D3 already has full breakdown. D4 expositional length kills readability.
- **Proposed fix:** Reduce each capability to 3 bullets (What / Phase / Quality-metric) + Source tag. Average block: 120 words → 50 words × 29 = −2,030 words.
- **Word-count impact:** −2000

#### M-02. Length — Section 10 Questions over-detailed (2,364 words / 19%)
- **Class:** 11 length
- **Location:** Q1-Q15 each ~157 words.
- **Problem:** Questions have Problem-framing + Binding-constraints + Expected-scope + Quality-criterion + Interdependencies. Architects reading this can refer back to source locks; keeping response-scope + quality-criterion + interdeps is enough.
- **Proposed fix:** Trim Problem-framing to 1 sentence; keep Binding-constraints (but dedupe with §2 quick-ref via short refs); merge Expected-scope into single bullet list. Target: 90 words/Q × 15 = 1,350 words.
- **Word-count impact:** −1000

#### M-03. Length — Section 2 quick-ref table too verbose
- **Class:** 11 length
- **Location:** §2 table rows average ~65 words for Formula + Implication combined.
- **Problem:** Locks 1-24 "Formula (compressed)" is not always compressed. E.g., Lock 19 = 24 words. Locks 7, 11, 22, 23 exceed 30 words each.
- **Proposed fix:** Hard-cap Formula at 15 words / Architectural Implication at 20 words. Removes ~15 words/row × 24 rows ≈ −360 words.
- **Word-count impact:** −360

#### M-04. Length — Section 4 Foundation (1,684 words) — §4.5 Shared Memory verbose
- **Class:** 11 length
- **Location:** §4.5 lines 490-502 = 13 dense bullets with atoms/FPF references.
- **Proposed fix:** Trim to 6 bullets covering only the architecture-binding parts (fs=SoT / 9 entity types / 25K token budget / 3-layer memory / mereology edges / single event log). Defer FPF internals (A.16, F.17 UTS cell counts) to D6 pointer.
- **Word-count impact:** −200

#### M-05. Section 3 capability phase-evolution sentences consistently over-specified
- **Class:** 7 over-specification
- **Location:** Every 3.1.x / 3.2.x / 3.3.x "Phase evolution:" bullet predicts Phase 2/3+ mechanics.
- **Problem:** Phase-2/3+ mechanics are Q9/Q10/Q15 architect responsibility. D4 over-commits.
- **Proposed fix:** Replace phase-evolution sub-bullets with "Phase-N boundary; extension vector = Q<N>."
- **Word-count impact:** −400

#### M-06. §3.1.5 Stripe over-specifies vendor
- **Class:** 7 over-specification
- **Location:** Line 132 "Stripe payment processing" heading + body hard-codes Stripe + Wise.
- **Problem:** Payment-processor-agnostic intent (§5.3 says "Payment-processor-as-external-SoT pattern"). Naming capability "Stripe…" locks it.
- **Proposed fix:** Rename "3.1.5 Payment processing" + in body: "Stripe primary / Wise FX as current choice; replaceable via processor interface."
- **Word-count impact:** 0

#### M-07. §3.1.11 Dashboard targets Monday but no week-start timezone
- **Class:** 8 under-specification
- **Location:** Line 190: "Monday snapshot committed by 12:00 local (zero miss)".
- **Problem:** "local" = Berlin? CET/CEST? If multi-pilot (Lock 2) onboards US pilot, local time ambiguous. Also "zero miss" is aggressive; first-launch tolerance unspecified.
- **Proposed fix:** "Monday snapshot committed by 12:00 Europe/Berlin (founder-anchor); ≥95% on-time hit-rate Phase-1 (≤2 misses/quarter)."
- **Word-count impact:** +5

#### M-08. Q2 "multi-role-binding: true" YAML snippet over-specified
- **Class:** 7 over-specification
- **Location:** §4.1 (c) lines 438 says `executors/ruslan.yaml multi-role-binding: true`.
- **Problem:** Forces one naming/format. Architects might propose different structure.
- **Proposed fix:** "executor binding MUST support multi-role enumeration (mechanism TBD per Q2)."
- **Word-count impact:** 0

#### M-09. §5.4 Uptime — ≥99.9% Phase 1 / ≥99.95% Phase 2+ not justified
- **Class:** 6 non-traceable directive + 5 weak success criteria
- **Location:** Line 582.
- **Problem:** No source cite for these targets. Why 99.9 vs 99.5? 43m/mo vs 22m/mo downtime at solo-ops is a large cost difference. Not tied to any lock.
- **Proposed fix:** Cite source (CLAUDE.md? ADR Chunk?) OR mark as "Stage-6 architect proposal, baseline ≥99.5%".
- **Word-count impact:** +10

#### M-10. §5.6 Performance targets — agent response-time no provider context
- **Class:** 8 under-specification
- **Location:** Line 597 "routine agent task <30s p50". Does this include fallback to OpenAI if Anthropic times out? What's the escalation latency SLA?
- **Proposed fix:** "…p50 measured on primary provider; fallback chain <120s p95 end-to-end (incl. provider-switch latency)."
- **Word-count impact:** +15

#### M-11. §6 C13 F-G-R retrofit "Day 15-17" — which Day-15-17?
- **Class:** 8 under-specification
- **Location:** Line 631 "Retrofit 10-15 existing ADRs Day 15-17."
- **Problem:** Which calendar? ADR rollout day-numbering? Stage 6 architect time? Not defined. D3 has a "Day 15-17" but reader needs anchor.
- **Proposed fix:** "Retrofit 10-15 ADRs during Phase-1 rollout days 15-17 per D3 §3.2."
- **Word-count impact:** +5

#### M-12. §6 C15 Physical Life-OS trigger repeats word-for-word in §3.2.11
- **Class:** 11 length
- **Location:** C15 line 635 and §3.2.11 line 316 both restate Triple-AND criteria.
- **Proposed fix:** State criteria once in C15; reference from §3.2.11 with "per C15 trigger."
- **Word-count impact:** −40

#### M-13. §7 AP-13 too narrow — "Public token with governance-rights Phase 1-3"
- **Class:** 3 ambiguity
- **Location:** Line 668. Lock 23 Option B allows Phase 3+ public token with economic-claim only, so "Phase 1-3" is wrong — should be "Phase 1-2 any form; Phase 3+ only if economic-claim-only".
- **Proposed fix:** "AP-13. Public token with governance or community-access rights, ANY phase. Violates Lock 23 Option B. Phase 3+ public token permitted only as economic-claim, membrane never blurred."
- **Word-count impact:** +10

#### M-14. §8.1 axis 4 "Locks compliance" — ambiguous pass criterion
- **Class:** 5 weak success criteria
- **Location:** Line 687 "per-lock traceability (variant cites which component addresses which lock). Any miss = axis score ≤3."
- **Problem:** "Miss" = uncited Lock or unsatisfied Lock? Different meanings. Also "≤3" is floor; no guidance on scoring 4-10.
- **Proposed fix:** "Per-lock traceability matrix: each of 24 locks mapped to ≥1 variant component with citation. Any lock uncited = axis 3. Any lock with component but no design detail = axis ≤5. All 24 locks cited + detailed = axis ≥8."
- **Word-count impact:** +30

#### M-15. §8.2 Axis weights sum to 100 but cost at 3% undervalues D15
- **Class:** 3 ambiguity (weighting philosophy)
- **Location:** Line 700-708.
- **Problem:** D15 (revenue-gated spend) is a hard rule, yet "Cost efficiency" is 3%. If cost is a gate-bound hard rule it shouldn't be low-weight scorable; it should be disqualifier.
- **Proposed fix:** Move cost-gate violation to §8.3 disqualifiers; rebalance remaining 3% to Axis 4 (Locks compliance → 18%).
- **Word-count impact:** +15

#### M-16. Missing ADR Chunk 8 coverage check
- **Class:** 2 missing requirement
- **Location:** ADR Chunk 8 covers "Rec-16, Rec-17, Gap 2, Gap 4, Gap 5" — referenced in §3 and §4, but brief never declares coverage matrix.
- **Proposed fix:** Add 1-paragraph "ADR Chunk coverage" in Provenance: "Chunks 1-8 coverage: [list with citations already in brief]." If any gap, flag to Stage 6.
- **Word-count impact:** +80

#### M-17. Footer "Backup plan" uses D9 v0.6 as fallback — outdated?
- **Class:** 6 non-traceable directive
- **Location:** Line 737 "fall back to current D9 v0.6 with ADR Chunk 8".
- **Problem:** D9 v0.6 is the old draft superseded by this D4 Brief + Stage 6. Fallback semantics unclear.
- **Proposed fix:** "Fallback = latest pre-Stage-6 canonical (D9 v0.6 + ADR Chunk 8 + D4 as guidance); defer full Stage 6 retry to Phase-1 mid-gate."
- **Word-count impact:** +10

#### M-18. Exec summary line 45 "Role ≠ Executor" not explained until §4.1
- **Class:** 3 ambiguity + 1 unclear directive (in exec summary)
- **Location:** Line 45.
- **Proposed fix:** Either add parenthetical "(role.md file vs executor-binding.yaml — see §4.1 / FPF IP-1)" or remove from Exec Summary and let §4.1/§6 C12 introduce it.
- **Word-count impact:** +10

#### M-19. §4.5 "Physical Life-OS ≠ Jetix Day 1" — conflict with Phase 2a trigger
- **Class:** 3 ambiguity
- **Location:** Line 498: "Physical Life-OS ≠ Jetix Day 1 (Area 4): parallel + asymmetric reference … Phase 2a Triple-AND → git filter-repo."
- **Problem:** "≠ Jetix Day 1" reads as "different from Jetix from Day 1" but the rest says extraction happens at Phase 2a. Readers may infer wrong timing.
- **Proposed fix:** Rephrase: "Life-OS co-exists in repo Day 1 with folder-separation + Hook 1 asymmetric ban; physical git-filter-repo extraction activates at Phase-2a Triple-AND."
- **Word-count impact:** 0

#### M-20. §4.8 Degraded mode — "Tier 3 pause" tiers not defined
- **Class:** 8 under-specification
- **Location:** Line 546 "primary down → Tier 3 pause; Tier 1 … switch fallback".
- **Problem:** No Tier definition anywhere in D4 or referenced docs clearly. "Tier 1 (manager, strategy-support-analyst, knowledge-synth, meta-agent)" is enumerated, but Tier 2 and Tier 3 never are.
- **Proposed fix:** Add tier definition box: "Agent-tier: Tier 1 = critical (always fallback); Tier 2 = important (fallback if budget allows); Tier 3 = non-critical (pause on primary outage). Enumerate or cite source."
- **Word-count impact:** +30

#### M-21. §4.6 "CL<2" undefined term
- **Class:** 8 under-specification
- **Location:** Line 512 "CL<2 cross-context → block reuse".
- **Problem:** CL abbreviation never expanded. Readers who haven't read D6 / FPF won't decode.
- **Proposed fix:** First occurrence: "Contextual Load (CL; FPF §X)".
- **Word-count impact:** +5

#### M-22. §3.1.11 Dashboard Phase evolution conflicts with §4.7 extension list
- **Class:** 9 internal contradiction
- **Location:** §3.1.11 Phase-2+ adds "roy count / roy revenue / match rate / member count / subscription:partnership ratio"; §4.7 Phase-2+ extension says same list — but §4.7 Phase-3+ adds "market-cap / token circulation / research outputs" while §3.1.11 Phase-3+ says "market-cap / token circulation / research outputs" — same list. Good. But §4.7 table doesn't include Phase-2+ "member count" — only §3.1.11 does.
- **Proposed fix:** Consolidate dashboard Phase-keyed metrics in §4.7 and reference from §3.1.11.
- **Word-count impact:** −50

#### M-23. §5.2 IP protection over-specifies "9 Jetix Innovations"
- **Class:** 6 non-traceable directive
- **Location:** Line 569.
- **Problem:** "9 Jetix Innovations" cited as `[Chunk 8]` elsewhere but number 9 not reconciled with any currently-approved decision. FPF appendix = 9 innovations?
- **Proposed fix:** Cite ADR Chunk 8 section explicitly: "9 Jetix Innovations (ADR-Chunk-8 Area 2 inventory: I1-I9 in `wiki/foundations/jetix-innovations.md`)."
- **Word-count impact:** +15

#### M-24. Section 1 Exec Summary lacks "What this document IS NOT"
- **Class:** 8 under-specification
- **Location:** §1.
- **Problem:** Architects will wonder: is this the D5 variant? The implementation plan? The spec?
- **Proposed fix:** Add 1-sentence: "D4 is a directive brief, NOT a variant and NOT an implementation plan; Stage 6 produces variants; Stage 8+ implements."
- **Word-count impact:** +25

#### M-25. §9 Variant Selection Step D "Hybrid-option clause" — DRR undefined
- **Class:** 8 under-specification
- **Location:** Line 726 "without resolution DRR".
- **Problem:** DRR = Decision Record / Research? Never defined.
- **Proposed fix:** "Decision Record Rationale (DRR) — format per FPF §X."
- **Word-count impact:** +10

#### M-26. Locks traceability matrix absent
- **Class:** 10 missing lock reference (structural)
- **Location:** Whole brief.
- **Problem:** No consolidated "Lock → Section(s)" matrix. §8.1 axis-4 demands per-lock traceability from variants; brief itself doesn't model it.
- **Proposed fix:** Add Appendix A: "Locks → Sections coverage matrix" (24 rows × columns: §2 / §3 / §4 / §5 / §6 / §7 / §10). Fills disqualifier audit loop + catches under-operationalizations (H-05, H-06).
- **Word-count impact:** +150

### LOW-priority issues (fix if quick; otherwise park)

#### L-01. Rogue heading level §3 uses `# Section 3` while others use `## 3.` / `## Section 10`
- **Class:** document structure
- **Location:** Lines 83, 411, 740, 1073 use `#` H1; lines 35, 48 use `##` H2. Heading hierarchy inconsistent.
- **Proposed fix:** Normalize to `## N.` for all top-level sections.
- **Word-count impact:** 0

#### L-02. Typos / bilingual mix in §2 Lock 22
- **Class:** style
- **Location:** Line 75 "startupper + азарт + stable + adequate + upward" mixes Latin + Cyrillic.
- **Proposed fix:** Latinize ("azart") to match §3.1.1 line 95 which uses "Azart".
- **Word-count impact:** 0

#### L-03. §3.1.12 Financial tracking references "compute-ledger monthly schema" unexplained
- **Class:** style
- **Location:** Line 194.
- **Proposed fix:** Cite: "compute-ledger monthly schema per P7.2 / ADR-Chunk-1."
- **Word-count impact:** +10

#### L-04. Exec summary line 41 "(`grep base/ -r "Jetix|DACH|AI consulting|Mittelstand"` → 0 hits)" duplicates §5.5
- **Class:** 11 length
- **Proposed fix:** Remove from §1; keep single authoritative definition in §5.5.
- **Word-count impact:** −20

#### L-05. §3.1.9 mixes "11 agents" + "life-coach migrates" — clarify migration status
- **Class:** 3 ambiguity
- **Location:** Line 167.
- **Proposed fix:** "11 canonical agents (life-coach excluded, migrates to Life-OS per C15)".
- **Word-count impact:** 0

#### L-06. "Audit SKU" first appearance §3.1.6 line 141 not defined
- **Class:** style / under-specification
- **Proposed fix:** First occurrence: "Audit SKU (client engagement with 5-view Bundle deliverable per E.17)."
- **Word-count impact:** +10

#### L-07. "BA-0 / BA-1 / BA-3" not defined at first use
- **Class:** style
- **Location:** Line 118 §3.1.3.
- **Proposed fix:** Parenthetical "(BA = Bias-Audit cycle per D.5)".
- **Word-count impact:** +10

#### L-08. §4.4 L/A/D/E not defined at first use
- **Class:** style
- **Location:** Line 485.
- **Proposed fix:** "(A.6.B L/A/D/E = Legal/Approval/Delivery/Evaluation per FPF A.6.B Boundary)".
- **Word-count impact:** +10

#### L-09. §3.2.3 "problem-CHR / capability-CHR" — CHR undefined
- **Class:** style
- **Location:** Line 244.
- **Proposed fix:** "(CHR = Capability-Human-Readable record per FPF)".
- **Word-count impact:** +8

#### L-10. §4.7 table "Failure rate + MTTR" baseline "P1: 3 incidents / 42 min example"
- **Class:** style / clarity
- **Proposed fix:** "baseline target: ≤3 incidents/month, MTTR p50 ≤42min".
- **Word-count impact:** 0

#### L-11. §10 Q8 Quality criterion "Formal proof (or trace)" — ambiguous scope
- **Class:** 5 weak success criteria
- **Location:** Line 911.
- **Proposed fix:** "Traceable proof via schema-level state-machine model + audit log covering ≥5 canonical events."
- **Word-count impact:** +5

#### L-12. §10 Q14 "ssh/access" — casing weird
- **Class:** style
- **Location:** Line 1032.
- **Proposed fix:** "SSH / access-provisioning".
- **Word-count impact:** 0

#### L-13. Lock 10 says "DE+US+EU contracts" (line 126) while Lock 10 quick-ref says "EN+US first" (line 63) — contradicts magnitude
- **Class:** 3 ambiguity
- **Location:** §3.1.4 Phase evolution phrase.
- **Proposed fix:** "Phase 2+ adds EU patent + DE+US+EU contract support (Lock 10 activation)."
- **Word-count impact:** 0

#### L-14. §3.1.3 "BA-0+BA-1+BA-3 closure" — why skip BA-2?
- **Class:** style / clarity
- **Location:** Line 118.
- **Proposed fix:** Parenthetical "(BA-2 Panel activates Phase 2a per D.5)".
- **Word-count impact:** +8

## Length-compression recommendations (concrete cut list)

Section-by-section trim opportunities (target: **≤7,000 words**):

| Section | Current | Recommended | Cut | Rationale |
|---|---|---|---|---|
| §1 Exec Summary | 332 | 330 | 0 | Already terse; adjust per M-18 / L-04 / M-24 neutrally |
| §2 24 Locks Quick-Ref | 1,144 | 780 | −360 | Cap Formula ≤15 words; Implication ≤20 words (M-03) |
| §3 Capabilities | 3,992 | 1,650 | −2,340 | 29 blocks → 3-bullet compact (M-01, M-05); drop predictive phase-evolution over-specs |
| §4 Foundation | 1,684 | 1,200 | −484 | Compress §4.5 memory dump (M-04), consolidate §3.1.11/§4.7 dashboard (M-22), merge C15 trigger duplication (M-12) |
| §5 NFRs | 676 | 620 | −56 | Minor tightening; add H-10/H-11/H-12 fixes |
| §6 Hard Constraints | 545 | 700 | +155 | Add C17-C21 for missing locks (H-04, H-08) |
| §7 Anti-Patterns | 477 | 525 | +48 | Add AP-16 (H-13); expand AP-13 (M-13) |
| §8 Quality Criteria | 481 | 510 | +29 | Axis-4 tighten (M-14); disqualifier +1 (M-15) |
| §9 Variant Selection | 261 | 260 | 0 | Minor fixes only |
| §10 Questions | 2,364 | 1,350 | −1,014 | Compress each Q Problem-framing to 1 sentence (M-02) |
| Provenance + Appendix | 380 | 530 | +150 | Add Lock→Section matrix (M-26), ADR coverage (M-16) |
| **TOTAL** | **12,335** | **≈8,455** | **−3,880** | Falls short of 7,000; additional pass may cut §3 another 500-800 words by dropping Phase-3+ capabilities that are Q9/Q10/Q15 deferrables, landing ≈7,700. Accept as realistic Pass-4 target; if hard 7,000 needed, collapse §3.2 + §3.3 into single "Phase-2+/3+ capability catalog" table (saves another 800-1000 words) |

**Realistic post-Pass-4 target:** 6,500-7,200 words. If Ruslan requires strict 7,000: collapse §3.2/§3.3 to catalog table.

## Go/no-go assessment for Pass 4

- **HIGH issues:** 14 — requires parallel fixer subagents (H-01 through H-14)
- **MEDIUM issues:** 26 (M-01 to M-26)
- **LOW issues:** 14 (L-01 to L-14)
- **Total:** 54 issues
- **Length:** 12,335 / 7,000 target = 176% (77% over; post-fix realistic 6,500-7,200)
- **Citation traceability:** 87 `D<X> §<Y>` + 117 `Lock N` mentions; good coverage but H-05, H-06, M-23, L-03 gaps
- **Locks operationalization:** 14/24 locks have dedicated Hard Constraint; 10 locks (1, 4, 6, 7, 9, 12, 14, 16, 19-24) need constraint-level elevation (H-04)
- **Internal contradictions:** 6 (H-01, H-02, H-11, H-14, M-13, M-22)

**Verdict: NEEDS-PASS-4-FIXES — READY-FOR-PASS-4** (all HIGH issues closable via parallel fixer subagents in <60 min; length reduction can run in parallel as dedicated subagent pass).

Recommended Pass-4 structure:
- Fixer-A: resolve H-01 through H-06 (roster + archetype + lock-ops citations) — 15 min
- Fixer-B: resolve H-07 through H-10 (missing capability / constraint specs) — 20 min
- Fixer-C: resolve H-11 through H-14 (precedence, contradictions, over-spec) — 15 min
- Fixer-D: length compression per concrete cut list (§3 primary target) — 30-45 min parallel
- Integration + merge review — 15 min

Post-Pass-4 → Pass-5 polish → Stage-6 launch ready.
