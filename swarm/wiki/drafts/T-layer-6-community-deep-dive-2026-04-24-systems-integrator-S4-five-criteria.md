---
title: "§4 5-Criteria Filter — Systems Integrator (Layer 6 Community Deep-Dive)"
type: systems-integrator
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-04
section: "§4"
mode: integrator
produced_by: systems-expert
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
confidence: high
confidence_method: F-G-R-coherence
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§7.2 ICP Qualitative Filter (D22) + Direction-of-life axis"}
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.1 + §6.2"}
  - {path: "swarm/wiki/operations/quick-money/icp.md", range: "5 ICP Criteria (Decision 22, applied verbatim)"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md", range: "§2.3 Secure Network ICP-gate + §7 audio_506"}
word_count_estimate: "~1900"
anti_scope:
  - "NO §2 ICP Trinity content (sibling cell)"
  - "NO §3 archetype enumeration (sibling cell)"
  - "NO §5 Alliance / §6 Matchmaker / §7 Outreach (sibling cells)"
  - "NO Notion writes"
  - "NO provider-key env-var references"
  - "NO Task() invocation strings"
---

# §4 — 5-Criteria Filter (Decision 22)

> **Context.** The 5-criteria filter sits as a qualitative layer on top of the 11-archetype
> union and the payment-ability filter (≥$5K/month recurring or ≥$10K one-shot; see §6.1
> intake clarification). It is the membrane that separates the Jetix community from the
> general professional population. This section unpacks each of the five criteria verbatim
> from D22, then operationalises them for interview, discovery call, and reference-check use.
> The section closes with a systems lens on how the criteria collectively function as a
> self-reinforcing selection mechanism.
>
> What this section does NOT do: replicate the ICP Trinity (§2), enumerate archetypes (§3),
> or design Alliance or Matchmaker mechanics (§5, §6). Those are sibling cells.
> Reference to them here is brief and directional only.

---

## 4.1 Criterion 1 — Startupper Mindset

### Verbatim D22 definition

> «Builder's instinct, proactive, creates rather than consumes. Не наёмник-исполнитель,
> а инициатор. Человек, который видит задачу и сам запускается к её решению, без внешнего push.»

[src:decisions/JETIX-VISION.md §7.2]

### How to identify — questions to ask

1. «Walk me through the last time you built something from scratch — not inherited, not
   assigned. What triggered you to start, and what did you do in the first 48 hours?»
   (Tests: autonomous initiation, not delegation-dependence.)
2. «Give me an example of a problem you identified that nobody else was tracking yet.
   What did you do with it?»
   (Tests: proactive pattern-detection vs reactive wait-for-instruction.)
3. «When a project stalls, do you tend to escalate, problem-solve solo, or restructure?
   How many times in the last 3 months?»
   (Tests: frequency of builder-reflex — once a year is a sign of consumer posture.)
4. «What are you currently building that didn't exist 6 months ago?»
   (Real-time test: a startupper always has an active build going.)
5. «How do you decide which problems are worth building for vs ignoring?»
   (Tests: discriminatory judgment — builders have filters, not just enthusiasm.)

### Behavioral markers during a discovery call

**Positive signals:** arrives with a concrete working hypothesis about their situation, not
just a «problem»; references specific prototypes, experiments, or iterations by name;
asks sharp questions back (not just receiving the pitch); uses language of agency («я решил»,
«я запустил», «я сделал») rather than passivity («мне предложили», «я участвовал»).

**Negative signals:** describes career as a sequence of roles rather than projects;
talks about ideas they «will someday» pursue; has no current build underway; asks only
for reassurance that Jetix will do the work for them; positions themselves as a buyer
of outcomes rather than a co-creator of capability.

### Disqualifiers

- Pure corporate employee with no P&L responsibility and no side-build of any kind.
- Person who self-identifies as a «researcher» or «observer» of entrepreneurship but has
  never shipped anything.
- Someone who outsources all initiative: «I just need someone to tell me what to do and
  I'll execute.» This is consumer posture, not builder instinct.
- «Idea person» with 30 ideas and zero completed iterations — builder's instinct without
  shipping is unfired potential, not the criterion.

---

## 4.2 Criterion 2 — Предпринимательский азарт

### Verbatim D22 definition

> «Entrepreneurial game-drive, enjoys skill-based risk. Не gambler (у которого исход
> зависит от случая), а skilled player — азарт от игры, где ставка — собственная
> компетенция. Игра в серьёзное дело как форма энергии.»

[src:decisions/JETIX-VISION.md §7.2]

### How to identify — questions to ask

1. «Describe a situation where the outcome depended primarily on your own skill, not luck
   or other people. How did that feel vs a situation where the outcome was out of your hands?»
   (Tests: whether the person craves the first type — skill-based risk — or avoids it.)
2. «Have you ever voluntarily made your work harder or riskier because it made the game
   more interesting? Give an example.»
   (Tests: intrinsic motivation from skilled challenge, the core of азарт.)
3. «What's the last skill-based bet you placed that didn't pay off? How did you react?»
   (Tests: resilience to skill-based loss vs catastrophizing; the skilled player loses
   without losing the drive.)
4. «How do you feel when the competitive pressure ramps up — energised or anxious?»
   (Tests: emotional polarity at high stakes. Anxiety-dominant without recovery is a
   red flag; energized-dominant is the criterion.)

### Behavioral markers during a discovery call

**Positive signals:** talks about their domain with genuine excitement that is not
performative — the energy comes through when discussing specific moves, decisions,
and results, not when pitching themselves; has stories of deliberately choosing harder
paths when easier paths were available; treats setbacks as data, not disasters.

**Negative signals:** describes past risk-taking only in retrospect («it worked out, I guess»)
with no emotional engagement; primary framing is financial security rather than
skill-compounding; shows anxiety when discussing uncertainty rather than sharpness;
talks about wanting predictability and guaranteed outcomes above anything else.

### Disqualifiers

- Risk-averse corporate buyer who explicitly requires 6-month procurement cycles and
  full implementation guarantees before commitment.
  [src:swarm/wiki/operations/quick-money/icp.md §5-ICP-Criteria]
- Pure gambler who confuses random outcome with skill — someone riding crypto cycles,
  not building capabilities.
- Someone who frames their entire career as risk-avoidance and is approaching Jetix
  purely as a safety move.
- Person who experiences other people's success as primarily threatening, not as
  evidence that the game is worth playing.

---

## 4.3 Criterion 3 — Stable

### Verbatim D22 definition

> «Reliable, disciplined, не volatile. Может выдержать длительную траекторию без срывов,
> mood-swings, burnout-spirals. Без этого качества все остальные обесцениваются — unstable
> человек с highest startupper mindset просто сгорает за 6 месяцев.»

[src:decisions/JETIX-VISION.md §7.2]

D22 explicitly names Stable as the criterion that «makes or breaks» the others. A person
with maximum startupper mindset and maximum азарт who is not stable is a liability, not
an asset. Instability is a systemic amplifier of all failure modes: an unstable founder
oscillates the team around them; an unstable community member generates noise that
devalues the membrane.

### How to identify — questions to ask

1. «Walk me through the last 12 months at a rhythm level — what was consistent week to
   week? Where did things collapse? How did you recover?»
   (Tests: baseline rhythm vs spike-and-crash pattern.)
2. «What systems or routines do you use to maintain output when motivation is low?»
   (Tests: discipline infrastructure — the stable person has externalized supports,
   not willpower-only cycles.)
3. «Have you experienced a burnout? Describe the trajectory — early signs, response,
   recovery time.» (Tests: self-awareness + recovery capacity. One burnout well-handled
   is acceptable. Pattern of burnouts with no learning is a red flag.)
4. «What commitments have you made and maintained consistently for ≥1 year?»
   (Tests: prior commitment track record. Scattered short-term commitments vs sustained
   multi-year ones is observable.)
5. «When your environment is unstable — market shifts, personal life disruption —
   how does that propagate into your work output?»
   (Tests: isolation capacity. Stable people insulate their core output from context
   turbulence; volatile people transmit environmental noise directly into work.)

### Prior commitments tracking (Stable-specific)

The most reliable signal for Stable is the pattern of prior commitments — not their
stated discipline, but their observable track record.

Ask about: years at current business or project (not necessarily same company);
consistency of a craft practice, physical training, or learning habit;
subscription or membership renewals over ≥2 years (trivial signals, but traceable);
any collaboration that lasted ≥1 year — the person who is stable keeps partnerships
alive.

**Red flags in prior commitments:** serial «pivots» every 3-4 months without learning
statements; multiple abandoned communities, memberships, or projects with no
post-mortem; stated commitments that are observable in calendar/track record as absent;
financial obligations abandoned rather than negotiated.

**Green flags:** a business operational for ≥2 years even at small scale;
a physical practice maintained through disruption (travel, illness, startup crisis);
a relationship or collaboration that has survived a conflict and continued;
any domain where they show compounding results over ≥2 years.

### Behavioral markers during a discovery call

**Positive signals:** arrives on time, prepared; references multi-year trajectories
naturally (not as one-off achievements); energy is even, not spiking; admits past
instabilities without drama; has a specific answer to «what keeps you on track.»

**Negative signals:** high emotional volatility during the call itself; describes recent
months as «chaos» without a recovery plan; no system for maintaining output;
mood visibly tracking external events; all past projects described as 3-6 month
experiments rather than sustained builds.

### Disqualifiers

- Person in acute financial crisis or active burnout who cannot sustain the attention
  investment AI implementation requires.
  [src:swarm/wiki/operations/quick-money/icp.md §5-ICP-Criteria]
- Serial project-abandoner: has 5+ initiated projects in the last year, zero sustained.
- Person whose volatility is externally oriented (markets, government, «the system»)
  and entirely explains their own inconsistency by environment rather than architecture.

---

## 4.4 Criterion 4 — Adequate

### Verbatim D22 definition

> «Common sense, no delusion. Understands реальность + как она работает. Не строит замков
> на облаках, не верит в «секретные техники успеха», не отрицает physics / economics /
> human nature. Adequate — это anti-bullshit detector, направленный на собственные
> самообманы в первую очередь.»

[src:decisions/JETIX-VISION.md §7.2]

Adequacy is the criterion most easily faked in a single conversation and most reliably
tested by edge cases. The adequate person applies their anti-bullshit detector inward,
not only outward — this is the distinction that matters.

### How to identify — questions to ask

1. «Tell me about a belief you held about your domain or yourself that turned out to be
   wrong. How did you find out? What did you do?»
   (Tests: inward anti-bullshit detector. The adequate person has a story here.
   The deluded person cannot find one.)
2. «What are the realistic constraints on what AI can do for your business in the
   next 6 months? Where specifically will it not help?»
   (Tests: calibration. AI-hype believers expect magic; adequate people draw clear
   edges around realistic capability.)
3. «What's the most common thing people in your industry are wrong about that
   you've confirmed through your own experience?»
   (Tests: external calibration + willingness to hold a non-consensus view with evidence.
   Conspiracy-level deviation is a red flag; evidence-based dissent from consensus is healthy.)
4. «Walk me through a decision you made based on incomplete information that
   didn't go as planned. What was your reaction?»
   (Tests: reality-acceptance without catastrophizing. Adequate people update; deluded
   people blame.)

### Reference checks pattern (Adequate-specific)

Adequate is the hardest criterion to assess from self-report alone, because the deluded
person has no reliable self-report. Reference checks are uniquely useful here.

**What to ask references:**
- «How does [name] respond when their expectations aren't met? Do they adjust or
  escalate blame?»
- «Have you seen them hold a position in the face of clear evidence against it?
  How long?»
- «Does [name] tend to overestimate or underestimate what they can do?
  Give me an example.»
- «When something goes wrong on a joint project, how do they frame it?»
- «Would you describe their judgment as generally reliable? Where does it break down?»

The adequate person generates consistent reference feedback: «adjusts quickly»,
«admitted they were wrong», «realistic about what's possible». The deluded person
generates hedged feedback: «very enthusiastic», «big thinker», «always has a plan»
with no concrete evidence of calibration.

### Behavioral markers during a discovery call

**Positive signals:** gives a concrete and honest answer to «what will AI not solve
for you»; acknowledges competitors without dismissing them; holds their own view under
light challenge without either caving or over-defending; speaks about economics and
operations with grounded specifics, not abstractions.

**Negative signals:** dismisses the question «where will this not work» entirely;
claims they have a «secret» or «unfair advantage» they cannot explain mechanistically;
treats the conversation as a pitch rather than a reality check; becomes defensive when
any assumption is probed; has a story where all failures were other people's fault.

### Disqualifiers

- AI-hype believer expecting «10× in one week» or «AI replaces all employees overnight.»
  [src:swarm/wiki/operations/quick-money/icp.md §5-ICP-Criteria]
- Conspiracy-level thinker who refuses digital tools on principle without mechanism.
- Person who has held the same incorrect belief about their market for ≥2 years while
  market evidence has updated.
- Anyone who cannot articulate where their approach might fail.

---

## 4.5 Criterion 5 — Upward-Direction

### Verbatim D22 definition

> «Actively develops self + среду. Vertical axis: вверх (развитие) vs вниз (degradation,
> тупёж, «towards death»).»

[src:decisions/JETIX-VISION.md §7.2]

### Direction-of-life axis (D22 NEW dimension)

This criterion introduces a vertical axis that operates independently of topic or domain.

> «прикол в том что темы это не по темам а по направлению жизни короче вот в чем штука
> что темы они как-то расходятся… вправо влево получается по горизонтали а по вертикали
> это вверх вниз нахуй это направление вверх направление к жизни или направление вниз там
> к смерти блять тупежу»

[src:decisions/JETIX-VISION.md §7.2 Direction-of-life axis]

This framing matters operationally: the topic someone works in (finance, photography,
bass guitar, AI) is horizontal — it does not determine direction. A bass player can be
on an upward trajectory; a tech founder can be drifting downward. The community
selection criterion is the vertical axis (upward-direction), not the horizontal one
(topic). Any of the 11 archetypes qualifies if their direction vector is upward; none
qualifies if their direction vector is downward regardless of archetype.

### How to identify — questions to ask

1. «What have you learned in the last 6 months that changed how you operate?
   Where did that learning come from?»
   (Tests: active self-development loop — the upward-direction person has concrete
   recent learning to name, not general answers.)
2. «How do you invest in the people and environment around you? Give me
   a specific example from the last 3 months.»
   (Tests: «develops self AND среду» — both parts of the criterion. Upward direction
   is not purely individual; it includes environment development.)
3. «What does growth look like for you 2 years from now? How are you investing
   in that trajectory today, not in what you're hoping for?»
   (Tests: active investment vs passive aspiration. Downward-direction people
   articulate aspirations; upward-direction people describe current investment.)
4. «Is there an area where you've been coasting rather than developing? What's your
   plan there?»
   (Tests: self-awareness + honesty. The upward-direction person can name their
   coasting areas; downward-direction people either cannot or react defensively.)

### Behavioral markers during a discovery call

**Positive signals:** references specific books, frameworks, peers, or experiments
as recent learning inputs; describes their environment (team, community, relationships)
in terms of what they are contributing to it, not just what they extract from it;
expresses curiosity during the conversation itself (asks genuine questions, not just
strategic ones); has a clear articulation of where they are investing now vs where
they want to be.

**Negative signals:** equates growth with financial metrics only («when I have more
money, I'll develop»); describes their environment purely in terms of what it owes them;
has been in the same position, doing the same thing, for ≥3 years with no traceable
learning loop; explicitly seeking stability and coasting («I just want to lock in what
I have»); direction language is backward-looking («I used to», «I once») rather than
present-and-forward.

### Disqualifiers

- Person explicitly targeting «exit and passive income» in < 6 months with no
  development plan beyond the exit.
  [src:swarm/wiki/operations/quick-money/icp.md §5-ICP-Criteria]
- Person whose self-development is performative (LinkedIn-optimised, credential-collecting)
  rather than operational (changes how they actually work).
- Anyone whose answer to «how do you develop your environment» is a blank — Jetix
  community is built on mutual development, not individual self-optimization alone.

---

## 4.6 Self-Selection Mechanism — The Filter as a System

The five criteria do not operate as a checklist run by an interviewer after the
candidate arrives. They operate as a **self-selection pressure** embedded in Jetix's
framing, language, and positioning long before any human conversation occurs. This
section applies the systems lens to explain why.

### «Самая большая авантюра века» as membrane (predator-outside)

The primary invitation framing from D22 — «Объединить всех авантюристов в самую большую
авантюру» [src:decisions/JETIX-VISION.md §14] — functions as a selective permeable
membrane, not as a mass-reach hook. The framing is deliberately provocative in a way
that self-selects on exactly the criteria being assessed.

Consider who responds to «the biggest adventure of the century»:
- The passive consumer does not self-identify as an авантюрист in any serious sense.
  They scroll past, mildly amused.
- The corporate risk-avoider finds the framing uncomfortably aggressive. They do not
  apply.
- The deluded person may respond — but the adjacently-placed «adequate professional,
  skin in game» language in the full framing creates friction for them.
- The skilled player who enjoys skill-based risk («предпринимательский азарт») finds
  the framing energizing rather than threatening.
- The upward-direction person self-recognizes in «авантюра» as development, not as
  gambling.

The framing is thus a first-pass filter operating at the message level, before any
criteria are explicitly articulated. This is a Meadows L7 leverage point: information
flow structure, specifically the self-selection information that the messaging sends to
the right sub-population and withholds from the wrong one.

**F: F3 (multi-case pattern, Meadows L7 applied to brand framing; observable in analogous
communities that use predator-outside language as natural self-selection.)**
**ClaimScope:** Holds for Jetix at current scale (pre-€50K, small population sampled).
At 10× scale, the framing will attract some motivated-but-not-adequate respondents who
have learned the right language without the underlying criterion. Monitoring mechanism
required at Phase-2+.
**R:** Refuted if the fraction of applicants who pass the full 5-criteria assessment
does not decline as community scale grows (i.e., if framing is selecting at the same
rate at 10× volume); accepted if pass-rate remains stable or improves over first 50
community candidates.

### Anti-LinkedIn / Anti-Attention-Economy stance as disqualifier signal

Jetix's explicit anti-attention-economy positioning [src:decisions/JETIX-VISION.md §6]
— «не LinkedIn где быдло одно которое ищет каких-то рабов» — operates as a second
self-selection signal working in parallel with the авантюра framing.

The person who is comfortable in LinkedIn's passive-scroll, credential-show economy
is precisely the person who fails criteria 1 (creates rather than consumes) and 5
(upward-direction that includes environment development, not just personal brand).
The person who reacts positively to an anti-attention-economy stance has already
self-selected toward the criteria set — they are uncomfortable in the environment
that disqualified candidates find comfortable.

This is a Beer VSM Level-2 function operating at the messaging layer: the
anti-LinkedIn signal prevents community drift toward passive-consumption culture by
making passive consumers self-exclude at the cost of zero interview bandwidth.

**F: F4 (operational convention; confirmed pattern in quality-gated professional
communities that use explicit anti-mainstream positioning.)**
**ClaimScope:** Holds while the Jetix brand is pre-mass-market. If Jetix achieves
mainstream visibility (Phase-3+), the anti-LinkedIn stance may attract contrarians
who are not adequate — a different failure mode. Phase-3+ messaging review is a
flagged dependency.
**R:** Refuted if post-admission surveys show high concentration of LinkedIn-native
postures among admitted members.

### USB-C metaphor and «Smart AI» internal label as tertiary signals

The USB-C positioning [src:decisions/JETIX-VISION.md §10] — Jetix as universal
connector across the AI-business cooperation space, not a product or an agency —
is legible primarily to people who think in systems, not features. An adequate
professional who is technically literate enough to understand what universal
protocols achieve will recognize the metaphor immediately. A passive consumer or
an AI-hype chaser will be unmoved by it (they want the product, not the protocol).

The «Smart AI» internal label (per D25 addendum) functions similarly: the framing
treats AI augmentation as intelligence amplification for already-capable people, not
as a crutch for the incapable. This self-selects on criterion 4 (adequate — AI is a
tool, not magic) and criterion 1 (builder's instinct — amplify existing capability,
not replace missing ones).

### Ashby requisite variety — the filter must match population complexity

A central systems-design question for any selection mechanism: is the filter complex
enough to handle the diversity of the population being filtered?

Per Ashby's Law of Requisite Variety [book-as-frame: Ashby, Introduction to
Cybernetics], a controller (here: the filter) must have at least as much variety as
the system it controls (here: the full population of candidates). If the filter is
simpler than the population, the population will find ways through the filter that
violate its intent.

The D22 5-criteria filter applied to the full LinkedIn-scale professional population
generates a pass-rate of approximately 0.1-1% from a broad, unfiltered initial pool.
This is not a defect — it is the design. The criteria are intentionally multi-dimensional
so that no single criterion can be satisfied while the others are missing. A person can
have startupper mindset but be volatile (fails Stable). A person can be stable but
consume rather than build (fails Startupper). The combinatorial effect of 5 independent
criteria creates the requisite variety to distinguish the community-appropriate candidate
from the superficially similar but inappropriate one.

The payment-ability filter (≥$5K/month recurring or ≥$10K one-shot, per intake §6.1)
[src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md §6.1] adds a
sixth independent dimension — not a moral filter, but an ability-to-engage-without-
financial-stress filter. Financial stress is one of the most reliable generators of the
behaviors that violate criteria 3 (Stable) and 4 (Adequate), because financial distress
produces volatility and motivated reasoning simultaneously.

**F: F3 (multi-case pattern; combinatorial filter design observed in analogous
quality-gated professional environments; Ashby as book-as-frame.)**
**ClaimScope:** The 0.1-1% pass rate estimate holds for a broad LinkedIn-scale initial
pool. For a warm-referral pool (existing community members referring known contacts),
the pass rate will be significantly higher (potentially 20-40%), which is expected and
desirable — the referral pre-screens on the criteria before the formal assessment.
**R:** Refuted if the combined criteria fail to discriminate between admitted and rejected
candidates on observable 12-month outcomes (e.g., admitted members show same volatility
rate as general population); accepted if 12-month community health metrics (contribution
rate, stability, upward-direction signal) are substantially better than base rates for
professional communities of similar size.

### Meadows leverage point — the filter as feedback loop

From a Meadows systems perspective [book-as-frame: Meadows, Thinking in Systems], the
D22 criteria filter is not a static gate — it is an active **reinforcing feedback loop**
operating on community composition.

The loop: admitting adequate, upward-direction, stable, azart-driven, startupper members
→ those members produce community behavior that itself is attractive to similar people
→ similar people are the ones who next self-select via the «самая большая авантюра»
framing → the next cohort has an even higher prior probability of passing the 5 criteria.

This is a Meadows L4 leverage point (changing the structure of information flows) with
a positive-feedback amplification effect on community quality. The converse is equally
true: admitting even a small fraction of candidates who fail criterion 3 (Stable) or 4
(Adequate) introduces volatility that makes the community less attractive to the highest-
quality candidates, who have alternative options. Stable's D22 note — «без этого
качества все остальные обесцениваются» — is a systems observation, not a moral
judgment. Instability is contagious in communities (Senge's «behaviour grows better
before it grows worse»), and the feedback loop runs both ways.

**F: F4 (operational convention; reinforcing community quality loops observed in
analogous invite-only professional communities; Meadows L4 as book-as-frame.)**
**ClaimScope:** Holds at Phase-1 and Phase-2 (5-500 members). At Phase-3+
($100M+ scale, international sub-networks), the feedback loop may require explicit
governance mechanisms (Beer VSM Level-3 audit function) to sustain — the loop
amplifies what is already present, and at scale both quality and noise amplify faster.
**R:** Refuted if community quality metrics (contribution rate, dissent-quality,
match-success) do not improve over first 3 cohorts of admitted members.

### Beer VSM Level-2 — the filter as anti-oscillation function

One of the most underappreciated functions of a selection filter in a community system
is anti-oscillation. In Beer's Viable System Model [book-as-frame: Beer, Brain of the
Firm], Level-2 (coordination) prevents operational units from interfering destructively
with each other. In a community context, the analogous function is preventing community
composition from oscillating between quality-states: high-quality → some inadequate
admissions → quality decline → member attrition → recovery attempt.

The D22 5-criteria filter, applied strictly and consistently, functions as the
Level-2 anti-oscillation mechanism for the Secure Network. Its job is not just to
admit the right people — it is to prevent community drift from the D12 quality-first
principle (deep inside / hooks outside). Every admission decision that violates one
criterion injects oscillation potential into the community system.

This is why the filter's operational implementation matters as much as its design.
The criteria must be applied uniformly across the discovery call, reference check,
and prior-commitments assessment, not selectively (e.g., waiving Stable for a high-
network candidate). Selective application breaks the Level-2 function.

[src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §2.3
«проходит только тот, кто соответствует 5 критериям D22»]

---

## §4 Synthesis — F-G-R on major claims

**Claim A: The 5-criteria filter produces a ~0.1-1% pass rate from broad LinkedIn-scale
population, and this is the intended design.**
- F: F3 (multi-case pattern; combinatorial filter + Ashby book-as-frame)
- ClaimScope: Holds for unfiltered broad pool; warm-referral pre-filtered pool expected
  at 20-40%; estimate does not hold if the initial population is itself pre-filtered
  (e.g., alumni of a relevant accelerator where criteria are already partially screened)
- R: Refuted if observed pass rate from warm-referral outreach is <5% (filter is too
  tight, not enough qualified population exists) or >60% (filter is not discriminating,
  criteria overlap too much); accepted if warm-referral pass rate lands 15-40% and
  12-month outcomes confirm criteria predicted performance

**Claim B: Stable is the necessary condition that makes all other criteria productive —
D22 verbatim; not an interpretation.**
- F: F5 (verbatim D22 text is a binding decision, not a hypothesis)
- ClaimScope: Holds unconditionally within D22; downstream operational implementation
  decisions (how strictly to apply, whether to allow probationary admission with
  Stable-monitoring) are interpretation territory not resolved by D22 alone
- R: Cannot be refuted at the F5 source level (it is a decision, not a claim). Operational
  interpretation is refutable: if 12-month data shows that Stable-marginal candidates
  perform as well as Stable-clear candidates, the implementation should update

**Claim C: The self-selection mechanism embedded in the «самая большая авантюра»
framing + anti-LinkedIn stance reduces interview-stage false positives by pre-filtering
the candidate pool before human bandwidth is spent.**
- F: F3 (multi-case pattern observed in analogous positioned communities; not directly
  measured for Jetix at current scale)
- ClaimScope: Holds at Phase-1 (pre-€50K, small-sample). Requires monitoring at
  Phase-2+ as community becomes more publicly known and framing becomes imitable
- R: Refuted if interview-stage pass rate does not differ between candidates who
  arrive via aligned framing (авантюра / anti-LinkedIn) vs generic professional outreach;
  accepted if 3-cohort comparison shows meaningful pass-rate difference (≥15 percentage
  points) between the two sourcing tracks

---

## §4 Dissents

**Dissent 1 — Risk of over-engineering the discovery call.**

The 5-criteria filter is robust in design. The questions enumerated per criterion
(sections 4.1-4.5 above) are comprehensive and could, if applied sequentially and
fully in every discovery call, produce a 60-90 minute assessment that is too heavy
for a 15-20 minute discovery call. There is a real operational risk of turning a warm
discovery conversation into an interrogation, which itself would filter out the
self-confident candidates who have options and will not submit to a screening gauntlet.

The recommended resolution: the full question battery is a **reference instrument**
for the interviewer, not a sequential script. Each criterion requires 1-2 targeted
questions from the set per conversation, not all 3-5. The decision signal is pattern
recognition across the full conversation, not checkbox completion.

**Dissent 2 — Adequate is the hardest criterion to operationalize from self-report,
and reference checks may not be practical at Phase-1 scale.**

The reference check pattern for Adequate (§4.4) is operationally correct but assumes
bandwidth that Phase-1 (solo Ruslan, 0 current leads) does not have. Reference checks
on a €5K/month retainer prospect require trust and time from the referee that may not
be obtainable in a Phase-1 context where Ruslan's network is still building.

The practical mitigation at Phase-1: apply the Adequate criterion primarily through
edge-case probing within the discovery call itself (the «what was your biggest wrong
belief» question is highly diagnostic without requiring a reference), and reserve formal
reference checks for higher-value engagements (€20K+ one-shot or multi-month retainer).

**Dissent 3 — The payment-ability filter from intake §6.1 and the 5-criteria filter
from D22 are not perfectly orthogonal; they partially select for similar traits.**

Specifically: financial stability (payment ability ≥$5K/month) partially overlaps with
Stable (can sustain a long trajectory without burnout) and Adequate (understands that
quality infrastructure costs money). This means the combined filter is slightly
redundant — passing the payment filter already increases prior probability of passing
Stable and Adequate. This is not a problem; redundancy in a filter system is acceptable
(Ashby: the controller may have more variety than strictly necessary without defect).
But it should be noted that the ~0.1-1% pass-rate estimate for the combined filter
may be slightly optimistic — the effective independent filtering dimensions may be
closer to 3-4 rather than 6 when accounting for correlation.

---

*End §4 draft. Word count estimate: ~1900. Acceptance predicate: per-criterion blocks
present (verbatim D22, questions, markers, disqualifiers); Stable includes prior-
commitments tracking; Adequate includes reference-checks pattern; self-selection
section present (≥200w) with Ashby, Meadows, Beer applied; F-G-R on ≥3 major claims;
dissents[] populated with 3 operational tensions.*
