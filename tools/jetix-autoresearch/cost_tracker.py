#!/usr/bin/env python3
"""cost_tracker.py — daily cost cap + 80% alert + halt on breach.

Per Q2 (RUSLAN ack 2026-05-11): €10/day hard cap, alert at 80%.

Phase 1 reality: inference cost via cc_helper.py is €0 (Max sub flat fee).
Cap applies only to *external* services (LinkedIn, SaaS, etc.) — none used
in D.2 voice-lens pilot. We still track to exercise the discipline and
catch any accidental API-key usage drift.

Usage:
    from tools.jetix_autoresearch.cost_tracker import CostTracker
    tracker = CostTracker(daily_cap_eur=10.0)
    tracker.record(eur=0.0, label="propose-step-cc-helper-max-sub")
    if tracker.exceeded():
        raise RuntimeError("daily cost cap exceeded — halt + AWAITING-APPROVAL")
"""

import json
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path("/home/ruslan/jetix-os")
LEDGER_DIR = ROOT / "tools" / "jetix-autoresearch" / "results" / "cost-ledger"


class CostTracker:
    """Per-day rolling cost ledger with hard cap + soft alert."""

    def __init__(self, daily_cap_eur: float = 10.0, alert_pct: float = 0.80,
                 ledger_dir: Optional[Path] = None):
        self.daily_cap_eur = daily_cap_eur
        self.alert_pct = alert_pct
        self.ledger_dir = ledger_dir or LEDGER_DIR
        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        self.today = date.today().isoformat()
        self.ledger_path = self.ledger_dir / f"{self.today}.jsonl"
        self.today_total_eur = self._load_today_total()
        self.alert_fired = False

    def _load_today_total(self) -> float:
        if not self.ledger_path.exists():
            return 0.0
        total = 0.0
        for line in self.ledger_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                total += float(json.loads(line).get("eur", 0.0))
            except (json.JSONDecodeError, TypeError, ValueError):
                continue
        return total

    def record(self, eur: float, label: str, experiment_id: Optional[str] = None) -> None:
        """Append a cost line to today's ledger."""
        if eur < 0:
            raise ValueError(f"negative cost not allowed: {eur}")
        entry = {
            "timestamp": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
            "eur": round(eur, 4),
            "label": label,
            "experiment_id": experiment_id,
            "running_total_eur": round(self.today_total_eur + eur, 4),
        }
        with self.ledger_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self.today_total_eur += eur

        # Soft alert at 80% — fires once per day.
        if not self.alert_fired and self.today_total_eur >= self.daily_cap_eur * self.alert_pct:
            self.alert_fired = True
            self._emit_alert(grade="soft", pct=self.today_total_eur / self.daily_cap_eur)

    def exceeded(self) -> bool:
        """True if today's spend has crossed the hard cap."""
        return self.today_total_eur >= self.daily_cap_eur

    def _emit_alert(self, grade: str, pct: float) -> None:
        """Emit health signal — currently writes to ledger as alert event."""
        entry = {
            "timestamp": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
            "alert_grade": grade,
            "pct_of_cap": round(pct, 3),
            "today_total_eur": round(self.today_total_eur, 4),
            "daily_cap_eur": self.daily_cap_eur,
        }
        alert_path = self.ledger_dir / f"{self.today}.alerts.jsonl"
        with alert_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def summary(self) -> dict:
        return {
            "date": self.today,
            "today_total_eur": round(self.today_total_eur, 4),
            "daily_cap_eur": self.daily_cap_eur,
            "pct_of_cap": round(self.today_total_eur / self.daily_cap_eur, 3) if self.daily_cap_eur else 0.0,
            "exceeded": self.exceeded(),
            "alert_fired": self.alert_fired,
        }


if __name__ == "__main__":
    t = CostTracker()
    t.record(eur=0.0, label="self-test-zero-cost")
    print(json.dumps(t.summary(), indent=2))
