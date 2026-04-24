---
id: decomposition-T-layer-5-product-deep-dive-2026-04-25
task_id: T-layer-5-product-deep-dive-2026-04-25
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
type: task-decomposition
phase: 2
state: drafted
created: 2026-04-25
produced_by: brigadier
cell_count: 15
wave_count: 4
parallelism_budget: 7 cells parallel max (HD-02 N=3 + 4 extra for Deep Dive breadth)
sources:
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "full"}
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", range: "§3-§6"}
---

# Phase-2 WBS — LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE

> 15 cells distributed across 4 waves. Every cell is `class: M` with explicit
> `cell_acceptance_predicate`. Integration is a dedicated final cell, not
> in-flight editing. Draft paths follow shared-protocols §1 convention:
> `swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-<expert>-<mode>-<section>.md`.

---

## §1 Cell matrix (15 cells)

| ID | Section | Expert × Mode | Wave | Class | Draft path | Floor |
|---|---|---|---|---|---|---|
| C-01 | §2 Portfolio overview | mgmt-expert × integrator | A | M | `...-mgmt-integrator-§2-portfolio.md` | 1500w |
| C-02 | §3.1 AI Consulting | mgmt-expert × integrator | A | M | `...-mgmt-integrator-§3.1-consulting.md` | 1500w |
| C-03 | §3.2 Продюсерский центр | mgmt-expert × integrator | A | M | `...-mgmt-integrator-§3.2-producer.md` | 1500w |
| C-04 | §3.3 USB-C Integration Services | systems-expert × integrator | B | M | `...-systems-integrator-§3.3-usb-c.md` | 1500w |
| C-05 | §3.4 Matchmaker Platform | systems-expert × integrator | B | M | `...-systems-integrator-§3.4-matchmaker.md` | 1500w |
| C-06 | §3.5 Secure Network | systems-expert × integrator | B | M | `...-systems-integrator-§3.5-secure-network.md` | 1500w |
| C-07 | §13 Evolution per gate master table | systems-expert × scalability | B | M | `...-systems-scalability-§13-evolution.md` | 1000w |
| C-08 | §3.6 YouTube-analyzer SaaS | investor-expert × scalability | B | M | `...-investor-scalability-§3.6-youtube.md` | 1500w |
| C-09 | §3.7 Educational + Investor Programs + Grant Hunting | investor-expert × scalability | B | M | `...-investor-scalability-§3.7-educational.md` | 1500w |
| C-10 | §3.8 Tokens / ICO (D23 Option B) | investor-expert × critic | B | M | `...-investor-critic-§3.8-tokens.md` | 1500w |
| C-11 | §3.9 Smart AI flagship narrative | philosophy-expert × critic | C | M | `...-philosophy-critic-§3.9-smart-ai.md` | 1500w |
| C-12 | §15 Open questions + preserved dissents | philosophy-expert × critic | C | M | `...-philosophy-critic-§15-open-q.md` | 500w |
| C-13 | §14 Tools Roadmap per phase | engineering-expert × integrator | C | M | `...-engineering-integrator-§14-tools.md` | 1500w |
| C-14 | §12 Cross-direction synergy + conflict matrix | mgmt-expert × scalability | C | M | `...-mgmt-scalability-§12-synergy.md` | 1000w |
| C-15 | §1 TL;DR + integration pass + canonical write | brigadier (integration) | D | M | `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` | 400w + full integration |

**Total floor:** 15 × stated = 9 × 1500 (directions) + 2 × 1500 (portfolio + tools) + 1 × 1000 (evolution) + 1 × 1000 (synergy) + 1 × 500 (open Q) + 1 × 400 (TL;DR) ≈ **16 900 words draft floor**. Integration typically adds 10-15% stitching prose → final **~18-20K words** with room to grow per direction.

---

## §2 Cell acceptance predicates (class:M)

### C-01 §2 Portfolio overview

```yaml
cell_id: C-01
class: M
owner: mgmt-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    contains_table("9 directions × [Phase activation | ICP | Pricing range | Revenue priority | Risk]"),
    narrative_answers("why exactly these 9, not more / not less"),
    narrative_answers("how 9 directions work together as portfolio (not 9 separate products)"),
    citations_present(locked_decisions: [D11, D18, D20, D21, D23]),
    citations_present(sources: [LAYER-6 §2, JETIX-SYSTEM-OVERVIEW §L5, audio_508, audio_529]),
    pricing_ranges_flagged_as_placeholder("L7 owns final pricing"),
    NO("reopening 28 Locks"),
    NO("final pricing commitments")
  )
dependencies: []
reads: [intake.md, JETIX-SYSTEM-OVERVIEW §L5, LAYER-6 §2, investor-integrator-L5 draft]
```

### C-02 §3.1 AI Consulting

```yaml
cell_id: C-02
class: M
owner: mgmt-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items:
      [Mission, Phase_activation, ICP_mapping_L6_Trinity, Value_proposition,
       Offer_structure, Delivery_mechanism, Competitive_positioning,
       Evolution_per_gate_5_gates, Cross_direction_deps, Open_questions]),
    ICP_mapping_archetypes_present(from_L6_4_primary: [Startupper, Operator-Founder-CEO]),
    pricing_range_present_as_placeholder("€150/hr baseline + productized packages"),
    citations_present([audio_511 4-pack offer, D11, D18, quick-money/icp.md, quick-money/pipeline.md]),
    delivery_mechanism_names_agents(from_KM_Mat_roster),
    open_questions_count >= 2,
    NO("final pricing decisions"),
    NO("strategic doc writing")
  )
dependencies: []
```

### C-03 §3.2 Продюсерский центр

```yaml
cell_id: C-03
class: M
owner: mgmt-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    ICP_mapping_archetypes_present(from_L6: [Блогер, Teacher]),
    target_market_named("English-speaking infobiz — US + UK + international" per D10),
    offer_structure_monthly_retainer_D18_not_hourly,
    pipeline_described("research → script → footage → edit → repurpose"),
    leverage_multiplier_present("1 workshop = 10+ derivative artifacts"),
    citations_present([audio_508, D11, JETIX-VISION §5 Decision 11]),
    evolution_5_gates_present,
    open_questions_count >= 2
  )
dependencies: []
```

### C-04 §3.3 USB-C Integration Services

```yaml
cell_id: C-04
class: M
owner: systems-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    covers_Path_A_B_C_from_STRATEGIC_INSIGHT_§5,
    maps_to_D20_USB_C_positioning,
    BIOS_moment_narrative_present(from STRATEGIC-INSIGHT §1-§3),
    ICP_mapping_present(primary: Mittelstand_with_GDPR_constraints + high-earner_solopreneurs),
    offer_structure_3_tiers_named(Path_A_managed, Path_B_client_hosted, Path_C_hybrid),
    compliance_layer_mentioned(GDPR, EU_AI_Act, data_sovereignty),
    voice2_verbatim_cited(USB-C "Windows прошивка"),
    evolution_5_gates_present,
    citations_present([Voice 2 chat-voice, D13, D17, D20, STRATEGIC-INSIGHT §5, audio_508])
  )
dependencies: []
```

### C-05 §3.4 Matchmaker Platform

```yaml
cell_id: C-05
class: M
owner: systems-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    3_modes_documented(Phase_1_manual_Ruslan, Phase_2_AI_smoothed, Phase_2_plus_platform),
    L6_inheritance_acknowledged("Matchmaker Phase-1 already specified in L6 §6"),
    L5_adds_productization_layer("how matchmaker becomes a paid product / service tier"),
    mechanics_cited_from_Voice_2("ищутся сложные вопросы → находятся люди → соединяются → AI смазывает → фиксируется → нарастают контакты"),
    ICP_mapping_present(specialists + complex_task_buyers),
    D21_roy_replication_connected,
    evolution_5_gates_present,
    citations_present([audio_514, Voice 2, D21, LAYER-6 §6])
  )
dependencies: []
```

### C-06 §3.5 Secure Network

```yaml
cell_id: C-06
class: M
owner: systems-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    L6_inheritance_acknowledged("Telegram-primary per LAYER-6 §10"),
    L5_adds_product_layer("how Secure Network becomes a paid subscription / складчина tier"),
    anti_LinkedIn_positioning_preserved("not for рабов ищущих других рабов" per JETIX-VISION D5),
    pooled_tools_mechanic_described("складчина Perplexity/Claude/expensive tools"),
    thematic_sub_networks_named(предприниматели, инвесторы, инженеры, философы, политики),
    ICP_mapping_present(post_G2_invite_only_expanded_Tier_1),
    evolution_5_gates_present(from_design_to_multi_roy),
    phase_activation_trigger_named("G2 €200K validation gate"),
    citations_present([audio_510, audio_524, JETIX-VISION D5, LAYER-6 §10, D25 company-as-code])
  )
dependencies: []
```

### C-07 §13 Evolution per gate master table

```yaml
cell_id: C-07
class: M
owner: systems-expert × scalability
word_floor: 1000
cell_acceptance_predicate: |
  AND(
    word_count >= 1000,
    contains_matrix_9_directions_x_5_gates("(active / preparing / deferred / sunset) per cell"),
    narrative_per_gate_present("what unlocks / what decommissions"),
    narrative_answers("sequencing logic — why these directions at this gate"),
    citations_present([JETIX-SYSTEM-OVERVIEW §L5 gate table, STRATEGIC-INSIGHT §8 7 recommendations]),
    ASCII_or_Mermaid_diagram_present,
    cross_reference_to_L7("pricing / unit-econ detail deferred to L7")
  )
dependencies: [C-02 through C-06, C-08, C-09, C-10, C-11]  # needs to see draft shapes
```

### C-08 §3.6 YouTube-analyzer SaaS

```yaml
cell_id: C-08
class: M
owner: investor-expert × scalability
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    золотая_жила_framing_preserved(from audio_514),
    SaaS_unit_econ_placeholder_ranges("€X-€Y per seat, per query, per channel"),
    competitive_positioning_names_alternatives(TubeBuddy, vidIQ, SocialBlade),
    reverse_engineering_methodology_cited(audio_527),
    data_advantage_described("asymmetric via bulk analysis of niche channels"),
    ICP_mapping_present(primary: Блогеры + secondary: agencies/infobiz operators),
    evolution_5_gates_present(concept → MVP → SaaS → scale → international),
    citations_present([audio_514, audio_527, review_2026-04-24 row 684-689])
  )
dependencies: []
```

### C-09 §3.7 Educational + Investor Programs + Grant Hunting

```yaml
cell_id: C-09
class: M
owner: investor-expert × scalability
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    three_subtracks_described(Educational_products, Investor_programs, Grant_hunting),
    D27_fork_and_merge_connected("clients fork methodology, best mutations return upstream"),
    D28_query_driven_KB_connected("educational products filter by anchor-query, not bulk"),
    alliance_option_C_hybrid_connected("Foundation-published docs = Apache 2.0 per L6 ack"),
    pricing_placeholder_range_named(course_tier, cohort_tier, license_tier),
    ICP_mapping_present(Teacher_archetype + ecosystem_specialists),
    evolution_5_gates_present(stabilize_in_Phase_1 → repo_V1 → scale → licensing_program),
    citations_present([audio_524, audio_527, D27, STRATEGIC-INSIGHT §5 Path B, JETIX-VISION §7])
  )
dependencies: []
```

### C-10 §3.8 Tokens / ICO (D23 Option B)

```yaml
cell_id: C-10
class: M
owner: investor-expert × critic
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(10_items_full),
    D23_preserved_verbatim("safe + adequate + thoughtful; NOT crypto-pump"),
    internal_utility_phase_2_vs_public_phase_3_distinction_present,
    $100K_self_earned_trigger_named,
    specialist_compensation_use_case_present,
    alternative_to_IPO_positioning,
    regulatory_surface_mentioned(EU_MiCA, US_securities_considerations),
    Ruslan_anti_pump_quote_cited("не какая-то там ебаная пирамида"),
    evolution_5_gates_present(not_designed_phase_1_2 → internal_utility_G3_G4 → public_G4_G5),
    open_questions_minimum_3(legal_structure, jurisdiction, distribution_mechanism),
    citations_present([JETIX-VISION §8 D23, audio_511, audio_527, LAYER-6 §11])
  )
dependencies: []
```

### C-11 §3.9 Smart AI flagship narrative

```yaml
cell_id: C-11
class: M
owner: philosophy-expert × critic
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    template_coverage(9_items_adapted_for_narrative_flagship — no Offer_structure_required),
    NO_promotion_to_D29_lock(Ruslan_explicit "ну типа запиши между прочим но нет это ещё не лок"),
    смартфон_vs_телефон_framing_preserved(audio_529),
    narrative_frames_8_other_directions("Smart AI = category descriptor applied to all 8"),
    distinction_from_external_brand_Jetix_preserved("Jetix = Jetix; Smart AI = internal label"),
    internal_vs_external_usage_guidance_present("may use in early sales / NOT on landing pages"),
    D25_company_as_code_connected("Smart AI behavior = system built with D25 discipline"),
    D13_closed_core_open_surface_connected,
    philosophy_lens_applied("epistemic rigor — not over-claiming; category not technology"),
    citations_present([audio_529 verbatim, D25-D28 §Smart AI, JETIX-VISION §7])
  )
dependencies: []
```

### C-12 §15 Open questions + preserved dissents

```yaml
cell_id: C-12
class: M
owner: philosophy-expert × critic
word_floor: 500
cell_acceptance_predicate: |
  AND(
    word_count >= 500,
    top_5_for_ruslan_ack_explicit,
    F-G-R_tagging_applied_to_each_claim_group,
    consolidates_from_per_direction_§3.N_open_questions,
    consolidates_from_WBS_C-02_through_C-11,
    preserved_dissents_from_prior_cycles_referenced(Dissent_3_Path_B_vs_Path_C from KM-ARCHITECTURE-VARIANTS),
    NO("override of 28 Locks — only flag"),
    citations_present_for_every_open_question,
    states_which_questions_block_Phase_3_strategic_docs_vs_which_can_wait
  )
dependencies: [C-02 through C-11]  # sees all direction open questions
```

### C-13 §14 Tools Roadmap per phase

```yaml
cell_id: C-13
class: M
owner: engineering-expert × integrator
word_floor: 1500
cell_acceptance_predicate: |
  AND(
    word_count >= 1500,
    four_subsections_present(Phase_1_tools, Phase_2_tools, Phase_3plus_tools, Cross_phase_tools),
    per_tool_format_applied(
      [Current_state, Trigger_for_build, Build_estimate_cycles, Dependencies, Revenue_justification]),
    Phase_1_inventory_complete(CRM_lite_existing, project_bootstrap_existing, voice_pipeline_existing, landings_missing, email_LinkedIn_manual),
    Phase_2_tools_enumerated(YT_analyzer_MVP, proper_CRM, matchmaker_portal_MVP, Secure_Network_Telegram_setup, educational_platform),
    Phase_3_plus_tools_enumerated(Token_ICO_infrastructure, EU_sovereign_compute, platform_matchmaker_scale),
    cross_phase_tools_enumerated(wiki + Private_Library, skills /ingest /ask /consolidate, 20_agents_orchestration),
    anti_scope_enforced("NOT implementation — only spec + roadmap"),
    revenue_triggers_named_per_tool,
    map_to_L6_§14_prior_tools_roadmap (no duplication),
    citations_present([CLAUDE.md, KM-MATERIALIZATION-MVP Report, LAYER-6 §14])
  )
dependencies: [C-02 through C-11]  # needs direction drafts to know what tools each direction needs
```

### C-14 §12 Cross-direction synergy + conflict matrix

```yaml
cell_id: C-14
class: M
owner: mgmt-expert × scalability
word_floor: 1000
cell_acceptance_predicate: |
  AND(
    word_count >= 1000,
    synergy_map_present("consulting leads → Secure Network membership leads → Alliance members"),
    synergy_map_present("YouTube-analyzer research → educational products content"),
    synergy_map_present("Matchmaker connects specialists to consulting projects → revenue uplift"),
    synergy_map_present("Smart AI narrative frames all consulting + producer offers"),
    conflict_matrix_present(9x9_where_directions_compete_for: [attention, resources, ICP_bandwidth]),
    ASCII_or_Mermaid_diagram_present,
    portfolio_balance_logic_named("which directions Phase-1 → Phase-2 transition implies for others"),
    citations_present([C-01 portfolio overview draft, LAYER-6 §12 evolution, D21])
  )
dependencies: [C-02 through C-11]
```

### C-15 §1 TL;DR + integration pass + canonical write

```yaml
cell_id: C-15
class: M
owner: brigadier (integration role, post §5.5.5 gate runs)
word_floor: 400_for_TLDR + integration_pass
cell_acceptance_predicate: |
  AND(
    TLDR_word_count >= 400,
    TLDR_summarizes_9_directions_one_paragraph_each,
    TLDR_names_Phase_1_active_directions(Consulting + Producer),
    TLDR_flagship_narrative_Smart_AI_present,
    integration_verifies(
      [all_15_sections_drafted, word_floors_met_per_cell, §5.5.5_provenance_gate_pass_per_draft,
       cross_section_consistency, anti_scope_compliance, inline_citations_density >= 1_per_paragraph]),
    canonical_doc_written_at("decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md"),
    frontmatter_complete(state=drafted, state_transition_target=AWAITING-APPROVAL,
                         deep_dive_policy=APPLIES, hitl_gate_path_set,
                         locks_referenced=[D1..D28 subset], sources=full_provenance),
    total_word_count BETWEEN 15000 AND 30000,
    AWAITING-APPROVAL_packet_filed,
    HALT_asserted_before_Phase_7
  )
dependencies: [ALL 14 previous cells]
```

---

## §3 Wave sequencing

### Wave A (parallel 3 cells — mgmt-expert has highest revenue-primary load)
- **C-01** §2 Portfolio overview
- **C-02** §3.1 AI Consulting
- **C-03** §3.2 Продюсерский центр

**Rationale:** portfolio overview and Phase-1 core revenue directions are the spine; they seed all downstream waves. Run in parallel via 3 concurrent `Task()` invocations. Drafts land in `swarm/wiki/drafts/`; brigadier §5.5.5 gate runs per draft on return.

### Wave B (parallel 7 cells — systems + investor experts)
- **C-04** §3.3 USB-C Integration Services (systems)
- **C-05** §3.4 Matchmaker Platform (systems)
- **C-06** §3.5 Secure Network (systems)
- **C-07** §13 Evolution per gate master table (systems-scalability — depends on Wave-A directions for shape; seed from JETIX-SYSTEM-OVERVIEW §L5 gate table)
- **C-08** §3.6 YouTube-analyzer SaaS (investor)
- **C-09** §3.7 Educational + Investor Programs + Grant Hunting (investor)
- **C-10** §3.8 Tokens / ICO (investor-critic)

**Rationale:** 7 independent direction drafts in parallel. C-07 Evolution master table can run in this wave because it seeds from existing §L5 gate table + JETIX-SYSTEM-OVERVIEW; final synthesis happens in Wave-C when all direction drafts are available. If 7-concurrent exceeds session budget, split to B-1 (4 systems cells) + B-2 (3 investor cells) sequentially.

### Wave C (parallel 4 cells — philosophy + engineering + mgmt-scalability; depends on Wave-A + Wave-B)
- **C-11** §3.9 Smart AI flagship narrative (philosophy-critic)
- **C-12** §15 Open questions + preserved dissents (philosophy-critic — needs all direction open-Qs)
- **C-13** §14 Tools Roadmap per phase (engineering — needs direction drafts to know tool needs)
- **C-14** §12 Cross-direction synergy + conflict matrix (mgmt-scalability — needs all direction drafts)

**Rationale:** these 4 cells all require the direction drafts. Run parallel after Wave-B cells return drafts.

### Wave D (sequential — brigadier integration)
- **C-15** §1 TL;DR + integration pass + canonical write

**Rationale:** integration is single-writer per shared-protocols §1. Brigadier reads all 14 drafts, runs §5.5.5 gate per draft, writes canonical `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` with TL;DR synthesized from integrated content.

---

## §4 Post-Wave-D actions (Part F verification + AWAITING-APPROVAL + HALT)

1. **Part F internal verification** — word count per section meets floor; total 15-25K; citations density; 28 Locks not violated; anti-scope compliance; Deep Dive policy applied.
2. **Write `swarm/gates/AWAITING-APPROVAL-layer-5-product-deep-dive-2026-04-25.md`** — 1-line summary per direction; top-5 open questions with brigadier recommendations; known limitations; how Ruslan acks.
3. **HALT** — Full-Auto NOT authorized. Wait for Ruslan ack before Phase 7 compound + Phase 8 archive.

---

## §5 Schema return contract per cell

Per shared-protocols §3, every `Task()` return must include:

- `summary:` ≤500 chars
- `proposed_writes[]:` at minimum `{path: drafts/<expert>-<mode>-<section>.md, frontmatter, body, edges_to_add[]}`
- `provenance[]:` ≥1 per proposed_write
- `confidence:` low|medium|high
- `confidence_method:` named
- `escalations[]:` empty unless blocking
- `dissents[]:` required for `*-integrator` returns

Brigadier §5.5.5 gate runs per draft on return. Reject → draft stays in drafts/; re-invoke with `context:{schema_error}` or HITL escalate on 2nd rejection.

---

## §6 Commit cadence (per launch prompt §10)

- `[l5-deep-dive] phase-1 intake + phase-2 WBS` (this commit)
- `[l5-deep-dive] Wave-A drafts: §2 portfolio + §3.1 consulting + §3.2 producer`
- `[l5-deep-dive] Wave-B drafts: §3.3 USB-C + §3.4 matchmaker + §3.5 secure-network + §13 evolution`
- `[l5-deep-dive] Wave-B drafts: §3.6 youtube + §3.7 educational + §3.8 tokens`
- `[l5-deep-dive] Wave-C drafts: §3.9 smart-ai + §12 synergy + §14 tools + §15 open-q`
- `[l5-deep-dive] Canonical document integrated — 15 sections`
- `[l5-deep-dive] Part F verification + AWAITING-APPROVAL packet — brigadier HALTS`

Target: 7-10 commits. Push after each.

---

*WBS produced by brigadier 2026-04-25. Dispatch begins immediately with Wave-A (3 parallel cells).*
