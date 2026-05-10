"""Jetix AutoResearch — Karpathy-style propose→eval→keep-or-revert loop.

Phase 1 MVP per Ruslan ack 2026-05-11. Pilot domain D.2 voice-pipeline
lens configs. All Claude calls route through tools/lib/cc_helper.py
(Max-sub headless). Constitutional discipline: pre-mutation Default-Deny
gate (hard-fail per Q5) + draft_promotion gate on methodology candidates
(Q4 threshold ≥3 validated cycles).
"""
