# swarm/evals/golden/solo-vs-matrix/ — M3 substrate (stub)

Reserved for **M3 solo-brigadier vs 6-cell matrix golden-set experiment**. See
`decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` §5 (M3 pitch +
experiment design) and the M3 opportunity artefact at
`swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md`
for the full specification (5-item RC-1..RC-5 rubric, double-blind eval protocol,
H0/H1 decision table).

**Status:** stub. M3 is DEFERRED — runs AFTER OPP-01 (this harness) ships AND
Ruslan acks the cycle-2 implementation. Cycle-2 creates the substrate; M3 is a
separate task brief launched after Part G of the cycle-2-impl report is acked.

**Hard dependency:** M3 results land here as `results.jsonl` following
`swarm/evals/schema.md` Section A. The `acceptance_predicate` field per record
is the Hamel-binary rubric verdict (RC-1..RC-5 pass count ≥ 3 of 5 in Run B
versus Run A).
