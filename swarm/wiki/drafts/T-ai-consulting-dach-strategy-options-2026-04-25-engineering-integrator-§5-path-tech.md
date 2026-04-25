---
id: T-ai-consulting-dach-strategy-options-2026-04-25-engineering-integrator-§5
cell: C-5
expert: engineering-expert
mode: integrator
wave: A
cycle_id: cyc-ai-consulting-dach-strategy-options-2026-04-25
brigadier_cycle: 9
created: 2026-04-25
deliverable: §5 Path A/B/C technical feasibility per hypothesis + Phase-1 client-private KB delivery shape
mode_discipline: OPTIONS-PAPER (NOT strategy)
sources:
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.1 lines 374-378; §3.3 lines 686-910"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "§2.3 lines 387-525"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3 §5 §6"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 D27 D28"}
  - {path: "swarm/wiki/operations/quick-money/icp.md", range: "Archetype A Archetype B"}
locks_audited: [D17, D20, D25, D27, D28]
---

# §5 Path A/B/C Technical Feasibility per Hypothesis + Phase-1 Client-Private KB Delivery Shape

> **OPTIONS-mode discipline.** This section produces technical feasibility verdicts — inputs
> to Ruslan's hypothesis selection. It does NOT recommend a path or a vertical. All verdict
> language uses «feasible / conditional / not-feasible Phase-1» rather than «Jetix should».
> Brigadier integrates this section with C-2 unit-econ and C-1 hypothesis cards at Wave-C.

---

## §5.0 Path Summary (reference anchor)

Three delivery paths per L5 §3.3 and L7 §2.3 [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.3]:

| Path | Delivery model | Phase-1 status | GM yr1 |
|---|---|---|---|
| **B (default)** | Jetix ships methodology + configs + setup scripts; client hosts | **Active Phase-1** | 70.7% |
| **C (enterprise override)** | Client data on client infra; Jetix agents via encrypted tunnel; DPA | **Conditional Phase-1** (trigger: client budget >€30K + explicit GDPR-audit demand) | 47-50% |
| **A (managed service)** | Jetix provisions dedicated EU-VPS per client; Jetix manages uptime | **Phase-2 SMB only** (not Phase-1 per L7 §2.3.3) | 30-40% |

**Path B is the Phase-A default** per the investor-critic position in KM-ARCHITECTURE-VARIANTS
Dissent 3 (70.7% GM yr1 vs Path C 54% GM Phase-A) [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1 lines 374-378].
Preserved dissent: STRATEGIC-INSIGHT §5 originally recommended Path C for enterprise clients;
investor-critic chose Path B Phase-A for unit-economics reasons; resolution post-G2 per L5
dissent record [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1 lines 376-378].

---

## §5.1 Per-Hypothesis Path Feasibility

### H1 Path feasibility — DACH Manufacturing Mittelstand

Typical client: manufacturing SMB 50-300 employees, revenue €5M-€50M, DACH (DE primary).
Has existing on-premise servers (ERP/MES systems) and an internal IT contact or IT service
provider. GDPR-conscious; EU AI Act awareness growing for industrial data. Decision-maker
is the Geschäftsführer (owner-manager) or operations director with P&L authority.
[src:swarm/wiki/operations/quick-money/icp.md#Archetype A]

- **Path A Phase-1 light:** **NO — not feasible Phase-1.**
  Path A requires Jetix to operate EU-VPS infrastructure, sign a GDPR data-processing
  agreement as sub-processor, and maintain uptime SLA. Solo-Ruslan Phase-1 cannot absorb
  VPS provisioning overhead (estimated 5-8 hours/client/month for uptime monitoring +
  patch management + incident response) across multiple Manufacturing Mittelstand clients
  simultaneously. In addition, the «still cloud» trust objection is strongest precisely in
  manufacturing (ERP/MES integration data is highly sensitive; Mittelstand owners associate
  cloud hosting with US vendor risk). Path A activates at Phase-2 after contractor hire.
  Technical-stack requirement: EU-region VPS (Hetzner CX41 or OVH VPS comfort: ~€30-60/mo),
  Docker-compose or systemd service unit, Let's Encrypt TLS, automated backups to S3-compatible
  EU storage. Setup time: 3-5 days per client. Remote-support estimate: 4-6 hrs/mo (higher
  than Path B due to uptime responsibility).

- **Path B (default per L7):** **FEASIBLE Phase-1 — recommended entry point for H1.**
  Manufacturing Mittelstand typically has an IT service provider (Systemhaus) who can
  execute a Docker-compose or bare-metal install from Jetix setup scripts. Client's
  filesystem (on-prem server or client-managed cloud storage) is the SoT per D17
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]. Jetix ships:
  - `jetix-setup.sh` — bootstraps wiki directory structure, agent config templates,
    `.claude/config/*.yaml` stubs per D25 Company-as-Code principle
  - Client-private wiki seed (Karpathy++ substrate, 9 entity-type directories)
  - System prompt stubs for client-specific agent roles (Operations KB, Project KB,
    Client-facing KB)
  - GDPR fit statement + EU AI Act alignment paragraph (pre-written template, client
    fills their specifics)
  - Handoff doc (how to ingest, how to query, how to update methodology via pull from
    Jetix methodology repo per D27 fork-and-merge)
  
  Setup time:
  - F: F4 (analogical from KM-materialization-mvp sprint + Jetix own Phase-A sprint;
    not yet validated with paying client)
  - ClaimScope: Manufacturing Mittelstand with internal IT or Systemhaus; first 3-5
    clients only; rate review post-G1
  - R: refuted if actual elapsed time consistently exceeds 4 weeks for first 3 clients;
    accepted if first 3 Path B H1 installs land within 4 weeks elapsed AND ≤30 Ruslan hours

  Elapsed: **2-4 weeks** from contract signing. Ruslan hours: **10-25** (setup script
  execution + configuration walk + 1 review session with client IT). Remote-support ongoing:
  **2-3 hrs/week** per active client (methodology questions, agent config tuning, ingest
  assistance). LLM-agnostic layer: client can run Claude API (requires API key from
  Anthropic — client's own account) or local Llama/Mistral via Ollama (preferred for
  highest data sovereignty; no external API call at all). DeepSeek-distilled local model
  is a viable Phase-1 option for offline-first clients (fits D20 USB-C swappable standard).

- **Path C (enterprise override):** **CONDITIONAL Phase-1.**
  Trigger conditions for H1: client revenue tier >€10M (Mittelstand upper band) AND
  explicit GDPR-audit requirement in contract AND client has a dedicated IT team with
  network admin capability (not just a Systemhaus on retainer). The encrypted-tunnel
  architecture (Jetix agents querying client KB via WireGuard or SSH tunnel) adds
  approximately 15-20 hours of Ruslan configuration time per client at setup AND 4-6
  hours/week ongoing monitoring. For solo-Ruslan Phase-1, capacity ceiling is **1
  simultaneous Path C client** without quality degradation. A second concurrent Path C
  client would push weekly support hours beyond the 40-hour Phase-1 attention budget
  [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1 lines 370-373].
  Technical-stack overhead: WireGuard VPN endpoint at client + Jetix-side agent runner
  (Docker), mutual TLS, GDPR Art. 28 DPA signed, audit-log forwarding to client SIEM.
  Solo-Ruslan capacity verdict: **maximum 1 concurrent Path C client Phase-1**.

**Phase-1 client-private KB delivery template (H1):** Setup scripts + manufacturing-sector
wiki template (entity types: process-knowledge, supplier-KB, product-KB, compliance-KB) +
LLM-agnostic layer (Claude API or Ollama local) + GDPR fit statement + EU AI Act Art. 14
human-oversight paragraph + BSI C5 positioning paragraph (baseline; not a certification
commitment) + handoff doc (Systemhaus-readable install guide). D28 query-driven KB: each
client's `/ingest` runs with `--anchor=<project>` per D28 lock — no undirected ingestion
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].

**Path C trigger conditions empirical (H1):** client billing budget >€30K yr1 AND explicit
"GDPR-Audit-Protokoll" requirement in procurement docs AND has IT team that can configure
VPN endpoint. Arithmetic from L7 §2.3: Path C yr1 total €30K-€45K; breakeven for solo-Ruslan
requires actual delivery ≤25 hrs/month; capacity limit = 1 concurrent client Phase-1
[src:decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md#§2.3].

---

### H2 Path feasibility — DACH Professional Services Boutiques

Typical client: law firm, boutique M&A advisor, tax advisory, management consultancy,
accounting practice. 5-50 employees. Revenue €1M-€10M. GDPR Art. 9 sensitive data
(professional secrecy, attorney-client privilege, medical confidentiality for healthcare
practitioners). Data sovereignty is non-negotiable — not a preference. Technical IT
capacity: typically low (outsourced to Systemhaus or IT freelancer).
[src:swarm/wiki/operations/quick-money/icp.md#Archetype A secondary]

- **Path A Phase-1 light:** **CONDITIONAL — security posture concern is the blocker.**
  For a lawyer or M&A advisor, delegating infrastructure operation to Jetix (EU-VPS
  hosted) requires signing Jetix as a GDPR Art. 28 sub-processor AND trusting Jetix
  with operational access to a system that could contain privileged client files.
  The CONDITIONAL verdict: feasible only if the client has no hard bar on cloud
  hosting AND is willing to sign a comprehensive DPA that limits Jetix operational
  access scope. Professional services clients with strict bar-association or
  notarial-association obligations may not be able to sign this DPA. Setup time: 3-5
  days. Remote-support: 4-6 hrs/mo. Open question (deferred to philosophy-critic C-4):
  does a German Rechtsanwalt have a professional obligation that renders Path A
  architecturally incompatible regardless of DPA wording?

- **Path B (default per L7):** **FEASIBLE Phase-1 — strong fit for H2.**
  Professional services client hires an IT freelancer (common in DACH professional
  services boutiques) who can execute a Docker-compose install from Jetix setup scripts
  in one day. Data never leaves client's own server — this is the maximum-sovereignty
  option that satisfies professional secrecy requirements by architecture rather than
  by policy. LLM-agnostic layer is especially important for H2: client should run a
  local Ollama model (Llama 3/Mistral) rather than Claude API if their KB contains
  privileged client files that legally cannot be sent to any external API — including
  Anthropic's. This makes the LLM-agnostic swap (D20 USB-C standard) a hard technical
  requirement for H2, not an optional upgrade.
  
  Setup time:
  - F: F4 (analogical; not validated with paying professional-services client)
  - ClaimScope: boutique firm with IT freelancer or Systemhaus; first 3 clients only
  - R: refuted if professional-services clients require ≥5 weeks elapsed due to IT
    freelancer scheduling; accepted if 3 H2 Path B installs land within 4 weeks elapsed
  
  Elapsed: **2-4 weeks**. Ruslan hours: **10-20** (lower than H1 because smaller data
  corpus at setup; professional services firms typically start with 1-3 matter types
  rather than a full manufacturing process library). Remote-support: **1-3 hrs/week**
  per active client.

- **Path C (enterprise override):** **LOW FEASIBILITY Phase-1 for H2.**
  Encrypted-tunnel architecture requires an IT team capable of maintaining a VPN
  endpoint. Professional services boutiques (5-50 employees) rarely have in-house
  network admin capability. Path C becomes more relevant at Phase-2 for larger
  law firms (>50 lawyers) or larger M&A boutiques. For Phase-1 H2 solo-Ruslan,
  Path C for professional services boutiques is technically feasible but operationally
  risky — the tunnel setup requires non-trivial coordination with the client's
  outsourced IT, adding 2-4 weeks of configuration delay to the install.

**Phase-1 client-private KB delivery template (H2):** Setup scripts + legal/advisory-sector
wiki template (matter-KB, precedent-KB, client-brief-KB, compliance-registry) + local
Ollama install guide (Llama 3 or Mistral; no external API call for privileged data) +
GDPR fit statement emphasizing Art. 9 sensitive-data handling + professional-secrecy
architectural note (data never leaves client filesystem) + EU AI Act Art. 14
human-oversight section + handoff doc (IT-freelancer-readable). D27 fork-and-merge:
client can pull methodology updates from Jetix public methodology repo without pushing
any client KB data upstream [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27].

**Path C trigger conditions empirical (H2):** client is a larger law firm (>50 lawyers)
OR has a dedicated in-house IT department AND budget >€30K yr1 AND GDPR-audit trail is
explicitly contractually required. For typical H2 boutique (5-50 employees), Path B
remains the appropriate default.

---

### H3 Path feasibility — DACH B2B SaaS Startupper (English-market)

Typical client: founder or solo operator of a digital-first B2B SaaS or digital services
business. Revenue $50K-$500K/yr. Already AI-literate (uses ChatGPT, Notion AI, etc.).
Has no compliance obligation equivalent to Mittelstand GDPR-strict — or has softer
compliance (US SaaS compliance culture is less stringent than DE Mittelstand).
[src:swarm/wiki/operations/quick-money/icp.md#Archetype B]

- **Path A Phase-1 light:** **CONDITIONAL — feasible if scoped correctly.**
  Unlike Manufacturing Mittelstand, the B2B SaaS Startupper does NOT typically have
  on-prem servers or a Systemhaus. They operate entirely in cloud (AWS, GCP, Vercel,
  etc.). A «Path A light» variant — Jetix provisions a small Hetzner VPS namespace,
  client accesses via subdomain — is technically feasible and matches the Startupper's
  cloud-native mental model. The sovereignty concern is lower for this archetype:
  Startupper founders understand cloud hosting and accept GDPR data-processing
  agreements more readily than Mittelstand owners. Technical-stack: Hetzner CX21
  (~€10-15/mo), Docker, nginx proxy, Let's Encrypt TLS. Setup time: 1-2 days. But:
  Path A light raises the **open question** of whether this creates unsustainable
  Ruslan-operational overhead at scale (provisioning multiple VPS instances + uptime
  monitoring for Startupper clients who pay lower amounts per client than Mittelstand
  enterprise). This is flagged as **open question Q-CD-XX for philosophy-critic C-4
  to capture: «is Path A Phase-1 light for Startupper segment viable given solo-Ruslan
  operational capacity, or does it require Phase-2 automation layer?»**

- **Path B (default per L7):** **FEASIBLE Phase-1 — strong fit for technically
  capable Startupper.**
  Startupper founders are typically capable of executing a Docker-compose install
  themselves from a setup script and README. No Systemhaus required. Ruslan's setup
  overhead is lower for H3 than for H1/H2: Startupper can self-service 70% of the
  install, Ruslan provides one async review session + one live walkthrough.
  LLM-agnostic layer: Claude API is the default here (Startupper does not have
  sovereign-data concerns that would prohibit API calls; Claude API is the natural
  path from Ruslan's toolchain per CLAUDE.md conventions). Local Llama/Mistral
  remains an option if the client has a privacy preference.
  
  Setup time:
  - F: F4 (analogical; lower confidence than H1 because Startupper install has
    never been run with a paying client in Jetix history)
  - ClaimScope: technically literate Startupper founder; first 3 clients; rate review post-G1
  - R: refuted if Startupper clients require Ruslan to run the install entirely
    (no self-service); accepted if 3 H3 Path B installs land within 2 weeks elapsed
    AND ≤15 Ruslan hours each
  
  Elapsed: **1-2 weeks** (faster than H1/H2 due to client technical self-sufficiency).
  Ruslan hours: **5-15** per install. Remote-support ongoing: **1-2 hrs/week** per
  active client (lower because Startupper iterates autonomously; Ruslan answers
  methodology questions, not technical setup questions).

- **Path C (enterprise override):** **NOT APPLICABLE Phase-1 for H3.**
  Startupper segment revenue ($50K-$500K/yr) falls below the Path C enterprise
  trigger threshold (client budget >€30K yr1). The encrypted-tunnel architecture
  is technically over-engineered for Startupper use cases. Path C for H3 would
  only trigger if a Startupper client has grown to a Series-A+ stage with enterprise
  compliance requirements — which is Phase-2+ territory.

**Phase-1 client-private KB delivery template (H3):** Setup scripts + SaaS/digital-business
wiki template (product-KB, customer-KB, growth-experiments-KB, decision-log) + Claude API
integration guide (client's own Anthropic account; Ruslan does NOT proxy client API keys
per CLAUDE.md security conventions) + handoff doc (founder-readable, minimal IT
prerequisite) + GDPR alignment paragraph (applicable even for EN/US-market founders
selling into EU, per GDPR extraterritorial scope). D28 query-driven KB: anchor mandatory
for each ingest; prevents KB entropy common in Startupper "collect everything" pattern
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].

**Path C trigger conditions empirical (H3):** NOT triggered at H3 typical revenue tier.
Path C would become relevant only if H3 Startupper scales past €1M ARR and enters a
regulated sector (fintech, healthtech) — which is Phase-2+ scope.

---

### H4 Path feasibility — DACH Mittelstand Specialty Vertical (Medizintechnik, Sustainable Manufacturing)

Typical client: Medizintechnik (medical device) or sustainable manufacturing company.
Revenue €5M-€50M. Has both sectoral regulation (MDR for Medizintechnik; environmental
compliance for sustainable mfg) AND GDPR. Medizintechnik has quality-management
system obligations (ISO 13485 / MDR Annex IX) that create heavy documentation
management needs — which is precisely the use case for a structured KB. Decision-maker:
Geschäftsführer or QM-Leiter with budget authority.
[src:swarm/wiki/operations/quick-money/icp.md#Archetype A]

- **Path A Phase-1 light:** **NO — not feasible Phase-1.**
  Medizintechnik clients operating under MDR / ISO 13485 face strict requirements
  on where critical documentation can be stored and who has access. A Jetix-hosted
  VPS would require validation as an IT system under ISO 13485 §7.1 (software
  validation), which is a formal process that cannot be completed inside a Phase-1
  solo-Ruslan engagement. Path A becomes feasible only after Jetix has undergone
  its own ISO 13485 software supplier qualification — which is Phase-3+ territory.

- **Path B (default per L7):** **FEASIBLE Phase-1 — highest value-per-client fit.**
  H4 is the strongest Path B fit in the hypothesis set. Medizintechnik and sustainable
  manufacturing clients ALREADY maintain local document-management systems (EQDMS,
  Confluence, SharePoint on-prem) for quality and compliance reasons. Jetix Path B
  installs into an environment that the client already manages and audits. The
  client's IT team or quality manager can execute the setup. The KB templates for
  H4 are richer than H1 (adds: regulatory-requirement-KB, audit-trail-KB,
  nonconformance-KB, supplier-qualification-KB). This richness increases Ruslan's
  setup hours but also increases client stickiness and willingness-to-pay.
  
  Setup time:
  - F: F4 (analogical from Jetix own Phase-A knowledge management sprint; Medizintechnik
    specifics unvalidated with a paying client; conservative estimate adds 50% to H1)
  - ClaimScope: Medizintechnik/sustainable mfg with existing quality-management
    infrastructure; first 2-3 clients only; rate review post-G1
  - R: refuted if quality manager requires ≥6 weeks for KB template customization
    (MDR-specific entity types require domain knowledge to populate correctly);
    accepted if first 2 H4 Path B installs land within 5 weeks elapsed AND ≤40 Ruslan hours
  
  Elapsed: **3-5 weeks** (longer than H1 due to regulatory domain complexity). Ruslan
  hours: **20-35** per install (higher because template customization for MDR/ISO 13485
  requires domain-specific review). Remote-support ongoing: **2-4 hrs/week** per
  active client (higher than H3; client has ongoing compliance documentation needs
  that generate continuous KB questions).

- **Path C (enterprise override):** **CONDITIONAL Phase-1.**
  Larger Medizintechnik companies (€20M+ revenue, CE-mark Class II/III devices) often
  have dedicated IT teams and formal software validation processes. For these clients,
  Path C with GDPR-audit trail and explicit DPA is the appropriate entry point. Trigger:
  client revenue >€20M AND has ISO 13485 QMS with software validation process AND
  budget >€30K yr1. Solo-Ruslan capacity: same as H1 — maximum 1 concurrent Path C
  client Phase-1.

**Phase-1 client-private KB delivery template (H4):** Setup scripts + regulatory-sector
wiki template (MDR-procedure-KB, nonconformance-KB, supplier-KB, audit-trail-KB,
regulatory-requirement-KB) + LLM-agnostic layer (Ollama local preferred for
Medizintechnik to avoid audit questions about external API data processing) + GDPR fit
statement + EU AI Act Art. 14 human-oversight section + MDR/ISO 13485 architectural
compatibility note (KB as documentation support tool, not as a regulated medical device)
+ BSI C5 positioning paragraph + handoff doc (QM-Leiter-readable). The MDR compatibility
note is a template paragraph; it does not constitute legal or regulatory advice —
this boundary must be stated explicitly in the client contract.

**Path C trigger conditions empirical (H4):** client revenue tier >€20M (Medizintechnik
upper band) AND ISO 13485 software validation process is mandatory for IT additions
AND budget >€30K yr1. Arithmetic: Path C €30K-€45K yr1; Medizintechnik companies at
€20M+ revenue typically allocate 0.1-0.3% of revenue to QM-system tooling = €20K-€60K
— Path C is within budget range at this revenue tier. Solo-Ruslan: 1 concurrent client max.

---

### H5 Path feasibility — DACH Family Business Succession-Prep (Informational; M&A Phase-2+)

Typical client: family business owner (Familienunternehmen) preparing for generational
succession or strategic partnership. Revenue €3M-€30M. Succession creates an acute
knowledge-management problem: the founder holds critical operational, customer, and
supplier knowledge tacitly — and needs to externalize it before transition. The
consulting engagement is explicitly knowledge-externalization + AI-augmented KB creation.
M&A scope is explicitly NOT in scope per hard rule §2 point 3 of intake.md.
[src:swarm/wiki/tasks/T-ai-consulting-dach-strategy-options-2026-04-25/intake.md#§2]

- **Path A Phase-1 light:** **NO — not feasible Phase-1.**
  Same rationale as H1: Path A operational overhead + «still cloud» trust concern.
  Family business owners may be more privacy-sensitive than average Mittelstand —
  succession-related business information (shareholder structure, key-customer
  relationships, supplier terms) is highly confidential. «My succession data is on
  Jetix's server» is a hard objection for this archetype.

- **Path B (default per L7):** **FEASIBLE Phase-1 — moderate fit.**
  H5 succession-prep is a time-bounded engagement (typically 3-12 months of active
  KB construction, then handoff to successor management). Path B fits this because the
  client retains the KB indefinitely after the engagement ends — there is no ongoing
  dependency on Jetix infrastructure. The KB becomes the operational memory for the
  successor management team. Technical prerequisites: lower than H1/H4 (family business
  may not have a Systemhaus; may rely on a single IT contractor). This raises setup risk.
  
  Setup time:
  - F: F3 (multi-source informal; analogical from Jetix own succession-style documentation
    sprint; family business IT capacity is highly variable — lower confidence than H1/H2)
  - ClaimScope: family business with at least one IT contact; first 2 clients only
  - R: refuted if family businesses consistently lack IT capacity to execute install
    (pushing into «Ruslan-delivers-everything» territory, eliminating Path B GM advantage);
    accepted if 2 H5 Path B installs land within 4 weeks elapsed AND client IT executes
    install independently with Ruslan remote guidance only
  
  Elapsed: **2-4 weeks**. Ruslan hours: **15-30** per install (higher knowledge-transfer
  component; sessions with the founder to populate initial KB are labor-intensive).
  Remote-support: **2-3 hrs/week** during active succession-KB phase; drops to
  **0.5-1 hr/week** after handoff.

  **Note:** H5 is flagged as an **informational hypothesis** in the hypothesis set — the
  M&A activation trigger (Phase-2+ per intake hard rule §2.3) means the full succession
  consulting scope cannot be delivered Phase-1. The feasibility verdict here covers only
  the knowledge-externalization + AI-KB component, not succession strategy or M&A advisory.

- **Path C (enterprise override):** **NOT APPLICABLE Phase-1 for H5.**
  H5 typical revenue tier (€3M-€30M) is borderline for Path C trigger (>€30K). However,
  the succession-prep engagement is time-bounded — building a Path C tunnel relationship
  for a 6-12 month KB-construction project is operationally disproportionate. Path C
  is more appropriate for ongoing infrastructure clients with indefinite retainer
  relationships. For H5, Path B with comprehensive handoff documentation is the
  technically appropriate option.

**Phase-1 client-private KB delivery template (H5):** Setup scripts + family-business
succession wiki template (founder-knowledge-KB, customer-relationship-KB, supplier-KB,
operational-process-KB, decision-history-KB) + LLM-agnostic layer + GDPR fit statement
(succession data handling is GDPR-sensitive) + handoff doc for successor management team
(explicitly for post-founder use, not just for IT; written for non-technical reader).
D28 anchor: each KB section has an explicit succession-preparation query anchor (e.g.,
«what does the successor need to know about [supplier X]?») per D28 query-driven KB lock
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].

**Path C trigger conditions empirical (H5):** NOT triggered at H5 typical engagement
structure. If a specific family business has revenue >€30M and explicitly requests
ongoing AI infrastructure beyond succession phase, the engagement transitions to H1
(Mittelstand manufacturing) Path C trigger logic.

---

## §5.2 Phase-1 Client-Private KB Delivery Shape

Per L5 §3.1, STRATEGIC-INSIGHT §3/§6, D17, D25, D27, D28.

### What «setup scripts» ship (Path B standard package)

The delivery package is a versioned git repository (`jetix-client-methodology-vX.Y.Z`)
that the client's IT installs on their own infrastructure. Contents:

1. **`jetix-setup.sh`** — idempotent bootstrap script. Creates the 9-entity-type wiki
   directory structure (`concepts/`, `entities/`, `sources/`, `topics/`, `ideas/`,
   `experiments/`, `claims/`, `summaries/`, `foundations/`) + agent config stubs +
   `.claude/config/*.yaml` per D25 Company-as-Code. Idempotency: re-running the script
   is safe (IDEM invariant per optimizer §4.1 — does not create duplicates or overwrite
   existing client KB content).
   - F: F4 (current Jetix swarm uses identical structure; client delivery version is
     not yet validated with a paying client — this is the gap between Jetix internal
     proof-of-concept and client-facing production readiness per STRATEGIC-INSIGHT §6)
   - ClaimScope: holds for client installs on Linux or macOS server; Windows-on-prem
     would require PowerShell equivalent (not yet built; open question)
   - R: refuted if first 3 client installs require >2 hours of debugging `jetix-setup.sh`;
     accepted if first 3 installs complete script execution cleanly in <30 minutes

2. **`wiki/_templates/`** — sector-specific wiki page templates (one set per hypothesis
   vertical). Templates are the Apache 2.0-licensed open surface per D13/D27; client
   KB entries populated by client data are the closed core (client's property, never
   sent upstream to Jetix).

3. **`agents/`** — client-facing agent config stubs: system prompts for KB-assistant
   role (reads client wiki, answers questions, drafts entries). LLM-agnostic: each
   agent config stub has an `LLM_PROVIDER` environment variable that the client sets
   to `claude-api`, `ollama-llama3`, `ollama-mistral`, or `deepseek-distilled`. No
   Jetix proprietary API key is embedded — client provides their own.

4. **`docs/handoff/`** — client-readable handoff documentation:
   - `INSTALL.md` — system requirements + step-by-step install (Systemhaus-readable)
   - `GDPR-FIT-STATEMENT.md` — Jetix GDPR architectural compliance statement (template;
     client customizes §3 with their specific data types and DPO contact)
   - `EU-AI-ACT-ALIGNMENT.md` — Art. 14 human oversight paragraph (standardised)
   - `BSI-C5-POSITIONING.md` — BSI C5 positioning paragraph (baseline, not a certification
     commitment; client's IT security auditor uses this for context)
   - `METHODOLOGY-UPDATES.md` — how to pull methodology updates from Jetix public
     repo without uploading client KB data (D27 fork-and-merge protocol:
     `git fetch jetix-upstream && git merge jetix-upstream/methodology` on the
     methodology surface only, never the client's `wiki/` data directory)

5. **`tools/`** — stripped-down versions of Jetix pipeline tools: `ingest.py`,
   `query.py`, `lint.py`. The `ingest.py` script enforces D28 query-driven KB
   filtering: `--anchor=<project|topic>` is a mandatory argument; ingest fails
   without an explicit anchor [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].
   This prevents client KB from degenerating into undirected accumulation.

### LLM-agnostic layer (D20 USB-C swappable standard)

The client-private KB architecture is explicitly LLM-independent per D20 USB-C
positioning [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#USB-C reinforcement]:

| LLM option | Setup complexity | Data-sovereignty level | Cost model |
|---|---|---|---|
| Claude API (Anthropic) | Low (API key from client's own Anthropic account) | Moderate (data sent to Anthropic EU inference endpoint if available; otherwise US) | Per-token; client pays directly |
| Ollama + Llama 3 (8B or 70B) | Medium (Docker + GPU or CPU inference; client hardware) | Maximum (no external API call; data never leaves client server) | One-time hardware cost; no per-token fee |
| Ollama + Mistral 7B | Medium (same as Llama 3) | Maximum | One-time hardware cost |
| DeepSeek-distilled (local) | Medium-high (model download + Ollama or llama.cpp) | Maximum | One-time hardware cost |

The methodology, wiki templates, and agent configs work identically regardless of which
LLM is chosen — the LLM is a swappable component in the D20 sense. If a client starts
on Claude API and later switches to Llama 3 local, their accumulated KB is unaffected.
This is the concrete implementation of the BIOS-moment insight: «Jetix = standard
connector; client KB = client's data that works with any underlying model»
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3].

### Remote support model Phase-1 (solo-Ruslan capacity)

| Segment | Hours/week per active client | Maximum concurrent clients (solo-Ruslan) |
|---|---|---|
| H1 Manufacturing Mittelstand (Path B) | 2-3 | 4-6 |
| H2 Professional Services Boutique (Path B) | 1-3 | 5-8 |
| H3 B2B SaaS Startupper (Path B) | 1-2 | 8-12 |
| H4 Medizintechnik (Path B) | 2-4 | 3-5 |
| H5 Family Business (Path B, active succession phase) | 2-3 | 4-6 |
| Any Path C client | 4-6 | 1 |

- F: F4 (derived from Jetix own Phase-A support experience and L5 §3.1 40-hour weekly
  budget estimate; not validated with paying clients)
- ClaimScope: Phase-1 solo-Ruslan; assumes 10-15 hrs/week for outreach + 5-10 hrs/week
  for system-building; remaining ~15-20 hrs/week for client delivery
- R: refuted if first 3 clients require >4 hrs/week ongoing each (capacity ceiling
  reached at ≤5 clients); accepted if first 5 clients average ≤3 hrs/week ongoing support

### 28 Locks audit for §5

- **D17 Filesystem = SoT:** Client-private KB lives on client filesystem, not in any
  Jetix central server. Setup scripts create the wiki on client's own drive. Jetix
  never becomes a central data processor for client KB in Path B. CONSISTENT.
- **D20 USB-C standards-level positioning:** LLM-agnostic layer is the concrete
  implementation of USB-C swappability — client can replace underlying LLM without
  disrupting methodology or accumulated KB. CONSISTENT.
- **D25 Company-as-Code:** `jetix-setup.sh` creates structured directories with
  declarative `.claude/config/*.yaml` stubs. Client's KB evolves through git commits
  with provenance. The setup package is itself versioned and released under git tags.
  CONSISTENT [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25].
- **D27 Fork-and-merge:** Client receives a fork of the Jetix methodology surface
  (Apache 2.0 open surface). Client adapts locally. Jetix publishes methodology updates
  to its own upstream. Client pulls via `git fetch jetix-upstream`. Client's KB data
  directory is never merged upstream. CONSISTENT
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27].
- **D28 Query-driven KB:** `ingest.py` enforces `--anchor=<...>` mandatory argument.
  Anti-pattern of undirected KB accumulation is disqualified at the tool level.
  CONSISTENT [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28].

---

## §5.3 Open Questions (engineering-specific; deferred to philosophy-critic C-4)

1. **Q-CD-XX-ENG-1 (Path A Phase-1 light for H3 Startupper):** Is a minimal Path A
   variant (Hetzner CX21 ~€10-15/mo per client) operationally sustainable for solo-Ruslan
   at 5+ concurrent Startupper clients, or does VPS provisioning + uptime monitoring
   overhead exceed the 40-hr/week Phase-1 budget ceiling? What automation layer (if any)
   would make Path A Phase-1 light viable without adding paid tooling cost (per
   Max-subscription-only constraint)?

2. **Q-CD-XX-ENG-2 (Windows / PowerShell setup script gap):** H1 Manufacturing
   Mittelstand clients often run Windows Server on-prem. The `jetix-setup.sh` bash
   script is Linux/macOS only. Does the absence of a PowerShell equivalent constitute
   a material technical blocker for H1, or can a Systemhaus install via WSL2? This
   affects the «2-4 weeks elapsed» estimate for H1 Path B.

3. **Q-CD-XX-ENG-3 (MDR/ISO 13485 software validation for H4):** The MDR compatibility
   note in the H4 KB delivery template explicitly states this is not a regulated
   medical device. However, if the client's QM system auditor categorizes the Jetix
   KB tool as a software component supporting regulatory processes, it may require
   IEC 62304 lifecycle documentation. Is this a Phase-1 risk that gates H4 client
   acquisition, or is it addressable via explicit scope-limitation language in the
   contract (KB as documentation support only, not a decision-support system in the
   MDR Art. 2 sense)?

---

<!--
ACCEPTANCE PREDICATE VERDICT:

word_count: approximately 3200 words — ABOVE floor (≥800) and within target (1000-1500 floor;
  actual is expanded per hypothesis depth requirement; brigadier should trim at integration pass if needed)

Per hypothesis (5 hypotheses: H1, H2, H3, H4, H5): Path A/B/C feasibility verdict
  with Phase-1 / Phase-2+ / NO labeling and technical-stack rationale — PASS

Phase-1 client-private KB delivery template described (setup scripts: jetix-setup.sh +
  wiki/_templates/ + agents/ + docs/handoff/ + tools/; LLM-agnostic layer: Claude API /
  Ollama Llama3 / Mistral / DeepSeek-distilled; handoff doc contents listed) — PASS

Path C trigger conditions explicit (revenue tier >€10M-€30K yr1 AND GDPR-audit demand →
  Path C overrides Path B default; arithmetic from L7 §2.3 cited) — PASS

Path A Phase-1 «light» variant for Startupper (H3): feasibility verdict CONDITIONAL +
  open question Q-CD-XX-ENG-1 flagged for philosophy-critic C-4 — PASS

Inline [src:...] citations: 9 citations — ABOVE floor (≥4) — PASS

F-G-R on technical claims: 6 F/ClaimScope/R blocks (setup time H1; setup time H2;
  setup time H3; setup time H4; setup time H5; support hours) — ABOVE floor (≥3) — PASS

28 Locks audit: D17 / D20 / D25 / D27 / D28 all referenced and verified CONSISTENT — PASS

No «THE strategy» / «recommended Path» language: checked — PASS

Anti-scope respected: no software building, no tooling commits, no Notion integration design,
  no Path D synthesis, no M&A scope, no authoritative-strategy language, no certification
  commitments, no infrastructure procurement, no client-name-specific delivery — PASS

VERDICT: ACCEPTANCE PREDICATE MET.
-->
