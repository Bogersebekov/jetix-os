---
title: Layer 9 — Insights playground (Phase B placeholder)
type: layer-readme
state: scaffold-only
updated: 2026-04-23
---

# Layer 9 — Insights playground

**Phase A status: scaffold-only.** No agent is instantiated to write
into this layer. Per W-10 (crazy-agent deferred) and Q8 (cumulative-AND
human-gated trigger), Layer 9 activates only when ALL THREE of the
following are simultaneously true AND Ruslan explicitly approves:

1. `≥50` closed α-4 cycles (count from `meta/health.md`).
2. `≥2` theme-wikis with `≥50` concepts each AND `≥3` inter-theme
   cross-references (`from.niche != to.niche` edges in
   `graph/edges.jsonl`).
3. Ruslan-approved `AWAITING-APPROVAL-layer-9-activation-*.md` lands
   in `swarm/gates/` and is acked.

Until activation:

- `candidates/`, `promoted/` MUST remain empty.
- `/lint` flags any non-README write under `swarm/wiki/insights/` as
  a Q8/W-10 violation.

Phase-B activation flow (when triggered):

- crazy-agent writes into `candidates/` (page enters at `state: drafted`).
- Critic / philosophy-expert reviews in-place: page advances α-2
  `state: drafted → reviewed → accepted` (no directory move).
- Brigadier promotes via §5.5.5 provenance gate → moves the
  `accepted` candidate file to `promoted/`, then promotes again to
  `swarm/wiki/global/` per W-11 cognitive-infrastructure mandate.
