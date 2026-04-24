---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.3
direction: USB-C Integration Services
type: layer-deep-dive-section
mode: integrator
author: systems-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md
  - decisions/JETIX-VISION.md
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md
  - decisions/JETIX-PLAN.md
  - swarm/wiki/operations/quick-money/icp.md
  - reports/review_2026-04-24.md
word_count_estimate: 2050
confidence: high
confidence_method: F-G-R-coherence + dissent-symmetry + book-as-frame
escalations: []
dissents:
  - id: D-USB-C-1
    source: KM-ARCHITECTURE-VARIANTS-2026-04-24.md §12 Dissent 3 (inherited)
    claim: "Path B (client-hosted, 70.7% GM yr1) is the Phase-A default for USB-C delivery"
    counter_claim: "Path C (hybrid client-data + Jetix-agents tunnel) is the Strategic Insight §5 recommendation for enterprise-grade clients"
    F: F4
    ClaimScope: "Phase-A first 1-3 client deployments; investor-unit-econ frame"
    R: "Refuted if first Mittelstand contract shows Path C GM ≥70% yr1; accepted if Path B achieves consistent 70%+ GM in first 2 deployments"
  - id: D-USB-C-2
    source: KM-ARCHITECTURE-VARIANTS-2026-04-24.md §12 Dissent 2 (inherited + localized to USB-C)
    claim: "Mistral 7B Q4_K_M (Apache 2.0, cleanest commercial license) should be the default LLM for Path A managed deployments"
    counter_claim: "Llama 3.1-8B Q4_K_M has broader community support and better mixed-language quality relevant for Mittelstand DACH clients"
    F: F3
    ClaimScope: "UC-10 offline-first inference default for USB-C managed paths; DACH Mittelstand use case"
    R: "Resolved by 20-query DACH golden-set evaluation (not yet executed); pending separate task authorization"
---

# §3.3 USB-C Integration Services — L5 Direction Deep-Dive

## 1. Mission

USB-C Integration Services is the direction through which Jetix deploys its full
stack — client-private AI, client-private knowledge base (KB), and the Jetix
orchestration methodology — as durable infrastructure at client sites. The mission
is not to consult on AI adoption and leave; it is to install, instantiate, and
maintain an AI-augmented operating system inside the client's own data perimeter,
positioning Jetix as the standard connector layer rather than as a vendor service.
Per the BIOS-moment framing [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
§0]: the PC market exploded when IBM published an open architecture and Phoenix
produced a clean-room BIOS — Jetix plays the EISA-committee role here, publishing
the methodology interface openly while keeping each client's KB and specific
implementation closed. Every client deployment is infrastructure the client runs
indefinitely, not a service that disappears when retainer ends.

Ruslan's verbatim statement from Voice 2 anchors the long-horizon ambition of
this direction: *«настолько будет технология просто Jetix распространена и
мощная что её будут использовать все как раньше использовали прошивку Windows
блять для любого компьютера... Это нахуй значит USBC»* [src:raw/voice-transcripts/
2026-04-24-ruslan-chat-voice-usb-c-positioning.md §Voice 2]. Infrastructure, not
service. Standard, not vendor lock-in.

---

## 2. Phase Activation

**Phase 1 (G0→G1, €0→€50K):** NOT productized as a separate offering. When a
consulting engagement under §3.1 requires local-first architecture — because the
client explicitly has GDPR-hard constraints or data-sovereignty requirements —
Jetix delivers a manual implementation inside that consulting umbrella. Maximum
1-2 manual installations in Phase 1. There is no productized kit, no setup scripts
distributed, no support SLA. The Phase-1 installations are learning cycles that
stabilize the methodology before it is packaged. [src:decisions/JETIX-PLAN.md §3]

**Activation trigger for productized form:** The first Mittelstand client who
explicitly requires GDPR-compliant local-first AI AND signs a contract at
$10K+/month retainer (or $10K+ one-shot install) triggers the transition from
manual-under-consulting to productized USB-C offering. Before that contract, this
direction remains an unproductized capability. After it, Phase 2 productization kit
work begins. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1]

**Phase 2 (G1→G2, €50K→€200K):** First productized Mittelstand client. One of
Path A/B/C is picked as Phase-A default (Dissent D-USB-C-1 unresolved — see §10).
Productization kit ships: setup scripts, wiki templates, onboarding documentation,
compliance dossier (GDPR fit statement, EU AI Act alignment paragraph, BSI C5
positioning). This is the gate at which USB-C Integration Services becomes a
named, priced, scoped offering rather than a consulting sub-task.

**Phase 3 (G2→G3, €200K→€1M):** USB-C Integration Services becomes a dedicated
business unit. All three Paths (A, B, C) are supported simultaneously as a
structured tier offering. 5-15 clients operational. Certification pursuit begins
(ISO 27001 / BSI C5). Alliance Foundation methodology repository published under
Apache 2.0 (per L6 Option C ack [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5]).
Jetix-Corp proprietary core components are identified and legally protected.
D27 Fork-and-merge begins operating: client methodology forks can return
best mutations upstream. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27]

**Sunset trigger:** None. The target end-state is Jetix as Windows прошивка — a
de-facto standard that all AI-augmented businesses run on. The direction does not
sunset; it scales until it achieves infrastructure-layer dominance.

---

## 3. Target ICP Mapping

**Primary — Mittelstand entrepreneur with GDPR-strict, data-sovereignty mandatory
requirements.** This is Archetype A from the L6 Trinity and quick-money/icp.md
[src:swarm/wiki/operations/quick-money/icp.md §Archetype A]. Typical company:
10–500 employees, revenue €1M–€50M/год, DACH region (DE primary). The Mittelstand
owner has heard of AI, has tried ChatGPT or Copilot, and has hit a hard wall:
"If we feed our internal documents to this tool, are they going into training data?
Can we use this under GDPR audit?" The blocking friction is not capability scepticism
— it is compliance-and-trust. This client cannot move forward with cloud AI tools
without data sovereignty guarantees, and they know it. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3]

Operationally: Mittelstand Operator-Founder-CEO is one of the four primary Phase-1
archetypes per L6 ack [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2].
For USB-C Integration Services specifically, the Mittelstand owner-manager is the
most natural fit: they have IT assets (servers or cloud accounts under their
control), a real compliance burden (sector regulations + GDPR + emerging EU AI Act
awareness), a willingness to invest in structural infrastructure (not tactical tools),
and the budget to sustain a $3K-$10K/month retainer once trust is established.

Payment ability filter: $10K+ one-shot install fee plus $3K-$10K/month managed
retainer — both thresholds exceed the L6 payment-ability gate of $5K/mo recurring
or $10K one-shot. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1]

**Secondary — High-earner solopreneurs with client-facing IP (lawyer, consultant,
therapist, boutique advisory firm owner).** This archetype holds confidential
client data under professional secrecy obligations. A lawyer in Germany cannot
feed client case files to any cloud-based AI without potentially violating
attorney-client privilege or GDPR Art. 9. A therapist cannot process therapy
session notes through OpenAI's API. A boutique M&A advisor cannot risk due-diligence
documents leaking outside their firewall. For these operators, Jetix's
client-private KB is not a premium feature — it is the minimum viable requirement.
Budget range: $5K-$15K one-shot install plus $2K-$5K/month support. Archetype maps
to the solopreneur high-earner ($150K+ personal income) per L6 §2.1 expanded
spectrum.

**Tertiary — DACH Mittelstand AI Alliance members (Phase 3+).** Once the Alliance
is formalized per L6 Option C Hybrid ack [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5],
Alliance members become the productized distribution channel. Each Alliance member
is already screened for methodology fit; USB-C deployment for Alliance members
follows a standardized protocol. Phase 3+ only.

---

## 4. Value Proposition

**The problem in the client's language:** "If we feed our internal documents to
ChatGPT, are they training on them? A GDPR audit would destroy us. But we are
falling behind competitors who are using AI. We cannot afford to stand still AND
we cannot afford to leak data."

This is not a hypothetical objection — it is the stated blocking friction across
the Mittelstand AI consulting market as documented in the BIOS-moment research.
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3] The AI
2026 moment is structurally identical to the PC 1982 moment: latent demand for a
standard exists, but business cannot commit to a vendor-locked, cloud-captive
implementation. Whoever provides a privacy-safe, methodology-standardized, locally
sovereign architecture wins the Mittelstand.

**The outcome Jetix promises:** AI-augmented knowledge work running inside the
client's own perimeter, with zero data leakage, a GDPR-defensible architecture,
and vendor-lock-in-free design — meaning the underlying LLM can be swapped
(from Claude API to Llama local to Mistral to DeepSeek-distilled) without
disrupting the client's accumulated KB or methodology.

**How Jetix USB-C differs from the alternatives:**

Not a wrapper on ChatGPT. Data would leave the EU and enter training pipelines
under default API terms. Not a private-cloud deployment of one vendor LLM: that
creates single-vendor lock-in with no moat against price increases or terms
changes. Jetix is a standard connector — the methodology works with any underlying
LLM; the client's KB compounds across model swaps. Per D13 Closed core / Open surface
[src:decisions/JETIX-VISION.md §4]: the methodology interface is published
(open surface); the client's KB and specific implementation remain sovereign
(closed core). Per D17 Filesystem = SoT [src:decisions/JETIX-VISION.md]: the
client's data lives on their filesystem, not in any Jetix central server.

**The BIOS-moment narrative (mandatory Voice 2 citation):**

Ruslan's Voice 2 from 2026-04-24 expresses the positioning with the precision
that no strategic document can improve on: *«Еще раз важное наблюдение, что Jetix
будет настолько охуенен, ну или занимает такую вот мощную позицию, что он будет
на уровне вот USB-C существовать. То есть, как сейчас у нас USB-C в электронике,
да, и в клавиатуре, блядь, и в телефоне, и в ноутбуке, блядь, и в кабеле и так
далее, точно так же Jetix будет существовать в этой, блядь, нише, ну и в целом
в мире вот агентов работы бизнеса и так далее»* [src:raw/voice-transcripts/
2026-04-24-ruslan-chat-voice-usb-c-positioning.md §Voice 2].

The прошивка-Windows metaphor from the USB-C Positioning Reinforcement section of
the D25-D28 addendum sharpens this further: *«настолько будет технология просто
Jetix распространена и мощная что её будут использовать все как раньше использовали
прошивку Windows блять для любого компьютера»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
§USB-C reinforcement]. Clients hear "infrastructure on which your business will
run indefinitely" — not "service you buy and cancel."

**BIOS / EISA structural framing (STRATEGIC-INSIGHT §1-§3):**

The AI 2026 market has the same structure as the PC 1982 market: 35,000+ incompatible
vendors, no standard, business paralysis from compliance fear, latent demand
exploding. IBM published an open architecture in 1981; Phoenix produced a clean-room
BIOS in 1984; the market went from $150M (1979) to $4B (1984). [src:decisions/
STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §1] Jetix plays the EISA
consortium role — establishing the open methodology interface while each client's
KB implementation remains fully closed and sovereign. The structural lesson from
the BIOS wars that applies directly here: open architecture multiplies the total
market by 30-40× while the methodology owner captures the compound value in the
layer above the commoditized hardware (= underlying LLMs).

**Compliance layer:** GDPR Art. 22 and Art. 32 (data-processing safeguards and
security of processing) are satisfied by architecture, not by policy. EU AI Act
Art. 14 (human oversight for high-risk AI) is addressed by the Jetix HITL-gate
protocol per the orchestration methodology. BSI C5 and ISO 27001 alignment are
the Phase 2 certification targets. Clients in regulated sectors (healthcare,
legal, finance) receive an audit-trail architecture out of the box.

---

## 5. Offer Structure — 3 Tiers from STRATEGIC-INSIGHT §5

All three paths are named here per acceptance predicate requirement. Pricing ranges
are placeholders — L7 Business Deep-Dive owns final pricing.

**Path A — Jetix-hosted managed service.** Jetix provisions a dedicated EU-region
VPS per client (e.g., Hetzner, OVH, or Deutsche Telekom cloud). Client owns their
data and KB. Jetix manages uptime, security patching, model updates, and
methodology version upgrades. Client never touches infrastructure. Data stays EU;
Jetix signs a GDPR data-processing agreement as sub-processor. This is the easiest
sale (low client technical requirement) and the highest operational margin for
Jetix (infrastructure costs ~€50-200/month per client; methodology value is in the
overhead). Target: low-touch Mittelstand SMB owner who has a compliance requirement
but no IT team. Placeholder pricing: $5K-$15K/month all-in.

Pros: easiest sales motion; consistent quality delivery; Jetix retains operational
visibility for methodology improvement. Cons: Jetix is liable for uptime and
security; "still cloud" trust issue for the most sovereignty-paranoid Mittelstand
clients; scales with client count (operational overhead grows).

**Path B — Client-hosted methodology license.** Jetix ships the methodology
package: agent configs, wiki templates, system prompts, setup scripts, and
documentation. The client's own IT team installs and hosts on client infrastructure
(on-premises server or client-owned cloud account). Jetix provides remote
consulting and support only — no operational access to the running system. Data
never leaves the client's control in any sense; Jetix is a methodology licensor,
not a data processor. This is the maximum sovereignty option. Per KM-ARCHITECTURE-VARIANTS
Dissent 3 (Position B), investor-critic analysis gives Path B a 70.7% GM yr1
at €3K onboarding + €15K/yr recurring — the strongest Phase-A unit economics.
[src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md §12 Dissent 3] Target:
self-sufficient technical Mittelstand with an internal IT team; also serves the
high-earner lawyer or boutique firm with a managed-IT provider who can handle
the installation. Placeholder pricing: $10K-$30K one-shot install plus $2K-$5K/
month support retainer.

Pros: maximum data sovereignty; lowest Jetix operational liability; highest
per-client GM in Phase A; scales without proportional ops overhead. Cons: harder
sales motion (client technical readiness required); harder support (Jetix cannot
remotely access the running system for diagnosis); quality consistency depends on
client IT execution; longer time-to-value (client IT team onboarding adds 2-4 weeks).

**Path C — Hybrid (client owns data, Jetix hosts agents via secure tunnel).**
The client's KB, documents, and filesystem live on client infrastructure. The
Jetix agent swarm queries the client KB via an encrypted tunnel; compute happens
at Jetix; results return to the client. Data never leaves the client perimeter;
reasoning happens in a sandboxed Jetix environment. Per STRATEGIC-INSIGHT §5,
this is the recommended approach for Enterprise-grade compliance-strict clients
and for Phase 2+ after Jetix has a first contractor/hire who can manage tunnel
operations. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]
Placeholder pricing: $15K-$40K/month managed (inclusive of Jetix compute).

Pros: client retains absolute data sovereignty; Jetix retains operational control
of the agent layer; Jetix methodology improves from aggregate compute patterns
(without accessing client data content); strong enterprise compliance story. Cons:
networking complexity (encrypted tunnel setup + monitoring); GDPR gymnastics on
the data-versus-metadata boundary; requires Jetix operational maturity (first hire
is prerequisite per investor Phase-A constraint). Not recommended as Phase-A
default (see Dissent D-USB-C-1).

**Pricing discipline:** L7 Business Deep-Dive owns final pricing across all three
paths. The placeholder ranges above are order-of-magnitude markers for ICP fit
testing; they are not commitments and must not be quoted to clients in Phase 1.

---

## 6. Delivery Mechanism

**Agents involved in a USB-C client deployment:**

The Jetix swarm provides the meta-coordination layer. For each live client
deployment, a per-client project-brigadier is spawned following the B2 rich
mini-swarm pattern per KM-ARCHITECTURE-VARIANTS §7 and the `/project-bootstrap
--type=consulting --client=<id>` skill. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md
§7] The per-client project-brigadier coordinates: engineering-expert (for
infrastructure setup and the client isolation stack), systems-expert (for
feedback-loop mapping and methodology deployment verification), mgmt-expert
(for project tracking and client milestone management), and knowledge-synth
(for the client KB bootstrap and ongoing ingest quality).

The Jetix swarm agents visible to Ruslan (brigadier + 5 domain experts) handle
the meta-level: methodology version management, cross-client compound-rules
promotion (anonymized case studies if client opt-in), and the Alliance
methodology-push protocol. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md §9.2]

**KM materialization infrastructure:**

Client isolation is implemented per UC-9 defense-in-depth STACK: directory
namespace `operations/clients/<slug>/` + frontmatter `granularity: client:<slug>`
+ env-var `WIKI_ROOT_CLIENT_ID` + Phase-B per-client separate-repo + UNIX
filesystem permissions. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md §3 UC-9
co-located proof] The `/project-bootstrap --type=consulting --client=<id>` command
bootstraps the client-isolation namespace per `.claude/config/wiki-roots.yaml`
UC-9 Phase-A config. `/ingest --anchor=<client-project>` populates the client KB
per D28 query-driven filtering: every ingest has a declared relevance anchor, no
promiscuous ingestion. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28]
Stage-gates SG-1 through SG-5 per-client ensure the project scaffold matures with
client momentum (B3 adaptive morphogenesis for exploratory phase; B2 full scaffold
at first signed contract).

**Timeline estimates by path:**

Path A (Jetix-hosted managed): 2-3 weeks from signed contract to first
client-private agent operational. Week 1: VPS provision + client namespace
bootstrap + ingest pipeline setup. Week 2: agent configuration + KB initial
population from client documents. Week 3: validation + client onboarding walkthrough.

Path B (client-hosted): 4-6 weeks. Adds client IT team onboarding (typically
2-week minimum for a Mittelstand IT team to get comfortable with the stack) +
client-side testing + remote support handoff.

Path C (hybrid tunnel): 3-5 weeks. Parallel track: tunnel setup (Week 1-2) +
agent configuration (Week 1-3) + KB bootstrap on client side (Week 2-3) +
end-to-end validation (Week 4-5).

**Automation level:** Medium-high in Phase 2+. The `/project-bootstrap` command
and stage-gate mechanics automate scaffolding and compliance documentation. Client
data ingestion is semi-automated (structured ingest with HITL review on
classification decisions). Methodology version updates push automatically from
Jetix-canonical upstream to client deployments (one-way push per D27 fork-and-merge
protocol [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27]). Client-specific
adaptations (their own prompt customizations, local workflows) stay in the client
fork and are never pulled back without explicit opt-in + anonymization.

**Company-as-code discipline (D25):** Every client deployment is fully git-tracked
from day one. All configs in `.claude/config/*.yaml` format — no hardcoded paths.
Client deployment state is reconstructable from git history at any moment.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25]

---

## 7. Competitive Positioning

**What the Mittelstand client is comparing against:**

Microsoft Copilot for M365: good for Microsoft-shop clients; data-bound to
Microsoft cloud; EU-Sovereign M365 options exist but are limited; vendor lock-in
is by design. A Mittelstand company running non-Microsoft tooling (SAP + custom
internal systems) gets minimal benefit and significant compliance exposure.

Google Workspace + Vertex AI: same cloud-captive architecture; EU-Sovereign Google
options exist; weak on agent orchestration for knowledge work.

ChatGPT Enterprise / Claude Enterprise: improved data posture (no training on
customer data per enterprise contract); still US-cloud; no client-private KB that
compounds locally; essentially a wrapper-level solution — smarter input, no local
memory.

Mistral Le Chat Enterprise: best European option for pure compliance positioning;
French, EU-sovereign, GDPR-native. Weak on methodology / agent orchestration;
no knowledge-base compounding layer; no client-private architecture out of the box.
A real competitor for the language-model layer; not a competitor at the methodology +
orchestration + KB compounding layer.

Self-hosted Llama / Ollama stack: maximum sovereignty but the client must build
everything themselves — agent orchestration, KB architecture, prompt engineering,
security layer, update protocols. Suitable for a Mittelstand with a strong internal
AI team. 0 methodology; time-to-value measured in months to years.

Big-consultancy custom builds (Accenture, IBM Consulting, Deloitte Digital):
enterprise-price, slow-delivery (6-18 month projects), one-off builds with no
methodology reuse across clients; the consulting firm learns but the client
does not compound. Price point is 10-50× higher than Jetix; target client
is Fortune-500, not Mittelstand.

**Why Jetix wins (honest assessment):**

Jetix wins on three structural advantages that no current competitor combines:

First, methodology-as-standard. Jetix positions as the USB-C of AI for business —
the connector that makes the underlying LLM swappable while the client's KB and
workflows persist. No current competitor articulates this; they all anchor to
a specific model or vendor. [src:decisions/JETIX-VISION.md §5 Decision 20]

Second, DACH/Mittelstand specialization with GDPR-by-architecture. General AI
consulting firms offering "private AI" lack the sectoral depth; the big consultancies
are too slow and too expensive. Jetix enters with a compliance architecture (UC-9
defense-in-depth STACK) that satisfies GDPR Art. 32 security requirements by
construction rather than by contractual promise.

Third, compounding client KB. Every Jetix-deployed client KB gets smarter over
time through `/consolidate`, `/lint`, and methodology updates. The client's AI
advantage compounds; competitors who deploy a one-shot solution provide a
depreciating asset.

**Honest risks:**

Technical credibility gap in Phase 1: zero production deployments means a
risk-averse Mittelstand CTO asking for references will not find any. First
deployment is a trust sale, not a reference sale. The response is to price the
first deployment as a BIOS-moment demonstration project: limited scope, high
transparency, explicit learning-together framing.

Compliance certifications absent in Phase 1: ISO 27001 and BSI C5 are Phase 2
targets. Mittelstand IT departments often require ISO 27001 as a vendor
qualification gate. Before certification, Jetix substitutes with: (a) architecture
documentation showing alignment with BSI C5 controls, (b) GDPR data-processing
agreement signed at contract, (c) reference to open-source codebase for auditability
(D25 company-as-code + D13 open surface). This works for the first 2-5 clients who
are early adopters motivated by the BIOS-moment framing; it becomes insufficient
as the market matures and procurement gets more formal.

Competitive risk from hyperscalers: Microsoft and Google could move into
EU-sovereign local-first space and absorb the positioning with marketing budgets
that Jetix cannot match. The structural response is to own the methodology moat
(non-cloneable Mittelstand AI Alliance network effect + curated KB compounding)
before hyperscalers have a reason to invest in DACH-specific methodology. The
6-12 month window is real. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8
recommendation 5]

---

## 8. Evolution per Gate (5 Gates)

**Gate 1 — €50K (G0→G1, current):** USB-C is not yet a productized direction.
Manual implementations only, delivered inside §3.1 Consulting engagements. Target
outcome of this gate: 1-2 manual installations that stabilize the methodology,
identify the correct delivery path (A/B/C debate resolved empirically), and
produce enough GDPR-fit documentation to support a Phase 2 productized pitch.
Systems-level BOSC trigger at this gate: **C** (Composition change) — the swarm
gains a client-isolation capability it did not have before (UC-9 defense-in-depth
moves from theoretical to tested). BOSC-A-T-X first trigger fires: **C+S** (a
Phase Promotion in swarm terms: from spec-only to operationally tested on at least
one real client namespace). [src:.claude/agents/systems-expert.md §6.1]

**Gate 2 — €200K (G1→G2):** First productized Mittelstand client under the USB-C
Integration Services label. Productization kit assembled: setup scripts, wiki
templates, onboarding documentation, compliance dossier. One of Path A/B/C
selected as default (Dissent D-USB-C-1 must be resolved here — empirical data
from Gate 1 installations should inform the choice). Jetix methodology published
under Apache 2.0 (Foundation layer per L6 Option C ack). Compliance dossier
drafted. BSI C5 / ISO 27001 gap analysis completed. BOSC trigger at this gate:
**A** (Agency change) — first paid client means Agency shifts; Ruslan is no longer
solo experimenter but now responsible for a client's production AI system. MHT
event: Role-Lift (Ruslan lifts from solo-consultant to infrastructure-operator role).

**Gate 3 — €1M (G2→G3):** USB-C Integration Services becomes a named business
unit. 5-15 clients operational across Path A/B/C. ISO 27001 / BSI C5 certification
pursued (€30-80K + 6-9 months; gate opens when capital allows per D15). Alliance
Foundation methodology repo live. Per-client mini-swarms operational under B2
rich-scaffold pattern. BOSC trigger at this gate: **S+C** (Scale + Composition) —
magnitude triggers a VSM Level-3 emergence (a distinct audit/quality-control
function for USB-C deployments appears as an explicit sub-system, not a footnote
in the consulting workflow). MHT event: Phase Promotion (USB-C BU promoted from
consulting sub-activity to explicit organizational entity).

**Gate 4 — $100M (G3→G4):** Infrastructure-layer dominance begins. 50-200 clients
operational. EU-sovereign compute partnership activated (Hetzner / OVH / Deutsche
Telekom cloud or own data-center per JETIX-PLAN §5). Mittelstand AI Alliance
formalized as legal entity (Alliance Foundation eV + Jetix-Corp GmbH per Option C).
Methodology licensing and certification programs: co-consultants deploy Jetix under
a methodology license. D27 fork-and-merge operating at scale — Alliance member
forks return mutations to upstream. BOSC trigger at this gate: **T** (Time horizon
shift) — planning cycles extend from quarterly to multi-year; USB-C service
contracts are now 3-5 year infrastructure contracts, not 12-month retainers.
MHT event: Context Reframe (engagement model reanchored from service to infrastructure).

**Gate 5 — $1T (G4→G5):** Jetix = Windows прошивка. Thousands of deployments.
Alliance at scale. Methodology referenced by EU standards bodies. Jetix-Corp
methodology licensing is the dominant revenue model (per Wintel precedent where
the value migrated from BIOS hardware to Intel patents + Microsoft licensing
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §1]). BOSC
trigger at this gate: **X+B** (eXternal + Boundary change) — regulators and
standards bodies become constituents inside the Jetix Alliance boundary, not
externalities. MHT event: Fusion (regulators join the Alliance ecosystem).

---

## 9. Cross-Direction Dependencies

**Dependencies on other directions:**

§3.1 AI Consulting is the upstream funnel for USB-C Integration Services.
First clients enter through consulting engagements; the consulting work surfaces
the GDPR / sovereignty requirement; that requirement triggers the USB-C deployment
conversation. Without §3.1 operational, §3.3 has no client pipeline in Phase 1.

§3.7 Educational Products + Jetix methodology repo is the prerequisite for
Path B deployment (client-hosted). Path B requires a packaged, versioned,
licensable methodology artifact. Until §3.7 produces methodology repo V1,
Path B cannot ship reliably. This means §3.7 work (Phase 2) must be concurrent
with or slightly ahead of the first productized USB-C offering.

§3.9 Smart AI narrative provides the category framing that makes the USB-C pitch
comprehensible to a non-technical Mittelstand owner. "We install smart AI that
knows only your documents" is the accessible framing; the USB-C / прошивка
metaphor is the sales narrative that anchors the positioning at the vision level.

§13 Evolution table (master cross-direction table) is authoritative for
gate-sequencing across all 9 directions. §3.3's gate predictions above must
be consistent with §13's master table — brigadier resolves any divergence.

**Depended upon by other directions:**

§3.5 Secure Network uses client-private KB primitives developed in USB-C
deployments. The digital-portraits mechanic (audio_524) that Secure Network
plans to use for member matching is built on the same per-client KB architecture.
USB-C Integration Services is the substrate; Secure Network is a consumer of that
substrate at Phase 2+.

§3.4 Matchmaker Platform: USB-C deployments at Mittelstand clients create the
node network that feeds the Matchmaker. When a Mittelstand client has a complex
task and Jetix has methodology coverage for that task class, the Matchmaker
connects the client's task with a Jetix specialist. The richer the USB-C
deployment network, the deeper the Matchmaker pool.

§3.6 YouTube-analyzer SaaS: if sold as an enterprise intelligence tool (not just
a standalone SaaS), the distribution model is Path A/B/C — each enterprise
client gets a YouTube-analyzer module inside their existing Jetix USB-C deployment.
Cross-sell opportunity at Gate 3+.

---

## 10. Open Questions (5 substantive questions)

**Q1 — Path A vs Path B vs Path C as Phase-A default [UNRESOLVED DISSENT D-USB-C-1].**
Investor-critic analysis (KM-ARCHITECTURE-VARIANTS Dissent 3, Position B) shows
Path B with €3K onboarding + €15K/yr recurring achieves 70.7% GM yr1 — satisfying
the Phase-A 70% GM floor. Path C at €15K/year achieves only 54% GM in Phase A,
failing the floor without a first contractor hire. Strategic Insight §5 (Position A)
recommends Path C for enterprise clients. These positions are unresolved and
preserved. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md §12 Dissent 3]
The empirical resolution path: first 1-2 manual Phase-1 installations should
collect unit-econ data (actual delivery hours × Ruslan rate) and compare against
both projections. Decision authority: Ruslan ack after Gate 1 data, before
productized Phase 2 launch.

**Q2 — ISO 27001 / BSI C5 certification timing: Phase 1 or Phase 2?**
Mittelstand procurement often requires ISO 27001 as a vendor qualification gate —
without it, Ruslan cannot get past the IT department even with a technically sound
compliance architecture. ISO 27001 certification costs €30K-€80K and takes 6-9
months. If initiated at G1 (€50K gate), it partially overlaps with Phase 2 launch.
If deferred to G2 (€200K gate), there is a 6-9 month window post-Phase 2 launch
where Jetix competes without the certification and must rely on architecture
documentation as a substitute. The risk: Mittelstand IT gatekeepers may not accept
architecture documentation in lieu of certification. Decision: Ruslan must decide
whether to initiate ISO 27001 process at G1 or accept the certification gap in
early Phase 2 as a constraint on the addressable market.

**Q3 — Underlying LLM default for Path A managed deployments [UNRESOLVED DISSENT D-USB-C-2].**
Mistral 7B Q4_K_M (Apache 2.0) is the cleanest commercial license for Mittelstand
deployment; Llama 3.1-8B (Meta Community License, ≤700M MAU clause) requires
per-client compliance attestation which adds friction. Mistral's marginal quality
disadvantage vs Llama on German-language tasks is unquantified. Resolution path:
authorize a 20-query DACH golden-set evaluation (German-language business documents;
key task classes: summarization, question-answering, structured extraction). This
should be a separate task, not part of this deep-dive cycle. Until resolved,
Mistral 7B Q4_K_M is the documented default for Path A deployments with the
dissent explicitly preserved.

**Q4 — EU-sovereign data-center timing: Phase 2 partnership vs Phase 3 own.**
Path A managed deployments require Jetix-operated EU-sovereign compute. Two paths:
(a) Phase 2 partnership with an existing EU-sovereign hosting provider (Hetzner,
OVH, Deutsche Telekom cloud) at low capital cost but with dependency on partner
terms; (b) Phase 3 own data-center per JETIX-PLAN §5, at 10× higher capital cost
but full infrastructure sovereignty. The Phase 2 partnership option is more
capital-efficient and appropriate for the €200K-€1M gate; the Phase 3 own
data-center applies at Gate 4 ($100M). This is a sequencing decision, not an
either/or. Decision: confirm Phase 2 partnership as the default path and document
Phase 3 own data-center as the G3→G4 trigger.

**Q5 — Methodology licensing model for Path B and Alliance participants.**
Per L6 Option C ack (Apache 2.0 Foundation docs + LGPL-equivalent software +
Jetix-Corp proprietary core), the licensing model is layered. But the operational
question is: what exactly is "open" (Apache 2.0) versus "closed" (Jetix-Corp
proprietary)? The distinction between methodology documentation (open) and
specific agent configurations + system prompts + knowledge-graph construction
scripts (closed) is not yet formally drawn. Without this boundary, Path B clients
cannot be given a clear license scope, and Alliance Fork-and-merge (D27) cannot
operate with defined IP governance. This question needs operationalization before
§3.7 Educational Products can productize the methodology repo V1. [src:decisions/
LAYER-6-COMMUNITY-DEEP-DIVE.md §5]

---

## Integrator Synthesis Notes

**F-G-R on the primary systems-level claim of this section:**

Claim: "The USB-C Integration Services direction represents a leverage point at
Meadows' Rung L4 (rules and structure of the system) — specifically, the rule
that AI-augmented business must accept cloud captivity as a precondition. Jetix
replaces that rule with an alternative standard: client-private, methodology-licensed,
LLM-agnostic. This structural intervention is the highest-leverage move available
in the current AI consulting market position, and it is only available in the
6-12 month BIOS-window before hyperscalers occupy the EU-sovereign positioning."

- F: F4 (operational convention; rests on BIOS-research + STRATEGIC-INSIGHT §1-§8
  book-as-frame; not formal proof)
- ClaimScope: holds for DACH Mittelstand consulting market at current scale (Phase A
  through Gate 2); NOT validated at Phase 3+ when hyperscaler EU-sovereign products
  may mature and absorb positioning
- R: Refuted if two sequential Mittelstand first-meeting conversations reject the
  USB-C / local-first framing as irrelevant to their decision criteria (i.e., if
  data sovereignty is not actually a blocking friction for the primary ICP); accepted
  if first 2 Mittelstand client engagements confirm data-sovereignty as a primary
  stated objection that Jetix's architecture resolves.

**Preserved dissents (both inherited from KM-ARCHITECTURE-VARIANTS cycle):**

Dissent D-USB-C-1 (Path B vs Path C as Phase-A default) is preserved without
resolution. Both positions are legitimate on their own terms: investor's F4 unit-econ
case for Path B and Strategic Insight's F3 enterprise-fit case for Path C are not
contradictory — they apply at different client maturity levels. The integrator does
not average: Path B is the Phase-A default for first 1-3 clients (investor case
wins on unit-econ floor compliance); Path C is the Phase 2+ default for
compliance-strict enterprise clients (Strategic Insight case wins on enterprise fit).

Dissent D-USB-C-2 (Mistral vs Llama offline LLM default) is preserved pending
empirical resolution via DACH golden-set evaluation.

**Cross-cell dependencies flagged:**

This cell (systems × integrator, §3.3) depends on investor-expert × scalability
having finalized the pricing placeholder validation and unit-econ floor confirmation
for Paths A/B/C. The Dissent D-USB-C-1 resolution at Gate 1 requires investor-expert
input. Brigadier should coordinate: if investor-scalability cell (§3.6-§3.8 wave)
produces updated Path unit-econ data, that should be reconciled with this section
before the canonical document write.

Engineering-expert × integrator (§14 Tools Roadmap) will specify the technical
implementation stack for UC-9 client isolation and UC-10 offline-first inference.
This §3.3 section assumes that implementation is feasible per KM-ARCHITECTURE-VARIANTS
validated analysis; §14 is the authoritative technical specification.

---

*End of §3.3. Sources on record: see frontmatter `sources` block. Provenance below.*
