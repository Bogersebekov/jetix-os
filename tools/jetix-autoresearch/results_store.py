#!/usr/bin/env python3
"""results_store.py — TSV results + DRR emit candidate per Part 5 §I.1 schema.

Per Part 5 schema (FPF E-9): DRR entry = {Decision, Reasoning, Result, Review}.
Each AutoResearch experiment yields one DRR-candidate record. These accumulate
under `agents/autoresearch-brigadier/strategies.md` (append-only) once
emitted; promotion to wiki/methodology/ requires Ruslan ack (Q4 threshold ≥3
validated cycles per `constitutional_gate.emit_awaiting_approval`).
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path("/home/ruslan/jetix-os")


class ResultsStore:
    """Writes per-run TSV + emits DRR-candidate records."""

    HEADER = [
        "timestamp", "experiment_id", "variant_name", "verdict",
        "baseline_metric", "new_metric", "delta",
        "secondary_metrics", "cost_eur", "commit_hash_or_unmade", "notes",
    ]

    def __init__(self, tsv_path: Path, drr_candidates_dir: Optional[Path] = None):
        self.tsv_path = tsv_path
        self.tsv_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.tsv_path.exists():
            self.tsv_path.write_text("\t".join(self.HEADER) + "\n", encoding="utf-8")
        self.drr_candidates_dir = drr_candidates_dir or (
            ROOT / "reports" / "autoresearch-karpathy-integration-2026-05-11" / "drr-candidates"
        )
        self.drr_candidates_dir.mkdir(parents=True, exist_ok=True)
        self.records: List[Dict[str, Any]] = []

    def record(self, *,
               experiment_id: str,
               variant_name: str,
               verdict: str,
               baseline_metric: float,
               new_metric: float,
               secondary_metrics: Dict[str, float],
               cost_eur: float,
               commit_hash_or_unmade: str,
               notes: str) -> None:
        delta = round(new_metric - baseline_metric, 6)
        row = [
            datetime.now().isoformat(timespec="seconds"),
            experiment_id,
            variant_name,
            verdict,
            f"{baseline_metric:.6f}",
            f"{new_metric:.6f}",
            f"{delta:+.6f}",
            json.dumps(secondary_metrics, ensure_ascii=False),
            f"{cost_eur:.4f}",
            commit_hash_or_unmade,
            notes.replace("\t", " ").replace("\n", " ")[:200],
        ]
        with self.tsv_path.open("a", encoding="utf-8") as f:
            f.write("\t".join(row) + "\n")
        self.records.append({
            "experiment_id": experiment_id,
            "variant_name": variant_name,
            "verdict": verdict,
            "delta": delta,
            "baseline_metric": baseline_metric,
            "new_metric": new_metric,
            "secondary_metrics": secondary_metrics,
            "cost_eur": cost_eur,
            "notes": notes,
        })

    def emit_drr_candidate(self, *,
                           experiment_id: str,
                           variant_name: str,
                           hypothesis: str,
                           changes: List[Dict[str, Any]],
                           verdict: str,
                           metrics_before: Dict[str, float],
                           metrics_after: Dict[str, float],
                           validated_in_cycles: int) -> Path:
        """Emit one DRR-candidate markdown to drr-candidates/.

        Brigadier promotes to strategies.md via standard cycle close
        (no autonomous self-modification per Tier 2 R9). Methodology
        promotion to wiki/methodology/ requires Ruslan ack via Part 6b
        draft_promotion gate (cf. constitutional_gate.emit_awaiting_approval).
        """
        path = self.drr_candidates_dir / f"{experiment_id}-{variant_name}.md"
        body = [
            "---",
            f"experiment_id: {experiment_id}",
            f"variant_name: {variant_name}",
            "type: drr-candidate",
            "schema: Part-5-FPF-E-9",
            f"verdict: {verdict}",
            f"validated_in_cycles: {validated_in_cycles}",
            "ack_state: pending_brigadier_cycle_close",
            f"created: {datetime.now().isoformat(timespec='seconds')}",
            "---",
            "",
            f"# DRR candidate — {experiment_id} / {variant_name}",
            "",
            "## Decision",
            f"- **Hypothesis tested:** {hypothesis}",
            "- **Mutation changes:**",
        ]
        for ch in changes:
            body.append(f"  - {ch.get('property')}: {ch.get('old_value')} → {ch.get('new_value')}")
        body.extend([
            "",
            "## Reasoning",
            "- Experiment proposed under deterministic mutation operator + LLM-creative fallback.",
            "- Search space = lens-config weights / thresholds / tier composition.",
            "- Selection pressure = greedy keep-if-better on Hamel-binary primary metric.",
            "",
            "## Result",
            "",
            "| metric | before | after | delta |",
            "|--------|--------|-------|-------|",
        ])
        for k in sorted(set(metrics_before) | set(metrics_after)):
            b = metrics_before.get(k, 0.0)
            a = metrics_after.get(k, 0.0)
            body.append(f"| {k} | {b:.4f} | {a:.4f} | {a-b:+.4f} |")
        body.extend([
            "",
            "## Review",
            f"- **Verdict:** `{verdict}`",
            f"- **Validated in cycles:** {validated_in_cycles}",
            "- **Methodology-promotion eligibility:** Q4 threshold is ≥3 validated cycles.",
            "  Below that → stays in DRR ledger; no draft_promotion gate emission.",
            "- **Ruslan ack required for promotion to canonical methodology.**",
            "",
        ])
        path.write_text("\n".join(body), encoding="utf-8")
        return path

    def summary(self) -> Dict[str, Any]:
        total = len(self.records)
        kept = sum(1 for r in self.records if r["verdict"] == "KEEP")
        reverted = sum(1 for r in self.records if r["verdict"] == "REVERT")
        skipped = total - kept - reverted
        total_cost = round(sum(r.get("cost_eur", 0.0) for r in self.records), 4)
        return {
            "total_experiments": total,
            "kept": kept,
            "reverted": reverted,
            "skipped": skipped,
            "keep_ratio": round(kept / total, 3) if total else 0.0,
            "total_cost_eur": total_cost,
        }
