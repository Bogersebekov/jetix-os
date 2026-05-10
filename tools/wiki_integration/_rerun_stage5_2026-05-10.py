"""One-shot script: re-run Stage 5 v2 on existing voice-pipeline-2026-05-10
filtered data. Produces 04-wiki-candidates-v2.md + sidecar JSON.

Usage:
    python3 -m tools.wiki_integration._rerun_stage5_2026-05-10
"""

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path("/home/ruslan/jetix-os")
sys.path.insert(0, str(ROOT))


def main():
    # Load orchestrator dynamically (filename has hyphen)
    orch_path = ROOT / "tools" / "voice-pipeline-orchestrator.py"
    spec = importlib.util.spec_from_file_location("voice_pipeline_orchestrator", orch_path)
    orch = importlib.util.module_from_spec(spec)
    sys.modules["voice_pipeline_orchestrator"] = orch
    spec.loader.exec_module(orch)

    annotated_path = ROOT / "reports" / "voice-pipeline-2026-05-10" / "_filtered-annotated.json"
    if not annotated_path.exists():
        print(f"ERROR: {annotated_path} missing. Regenerate first from filter batch.")
        return 1

    filtered_data = json.loads(annotated_path.read_text(encoding="utf-8"))
    output_dir = ROOT / "reports" / "voice-pipeline-2026-05-10"

    # Use existing lens — voice-pipeline canonical lens config
    # Defaults applied if absent
    lens = {
        "lens_name": "voice-pipeline-2026-05-10",
        "wiki_match_threshold_high": 0.85,
        "wiki_match_threshold_medium": 0.60,
        "wiki_match_top_k_prefilter": 10,
        "wiki_match_skip_below_bm25": 1.0,
        "wiki_propose_new_min_frequency": 1,
    }

    log = orch.DisciplineLog(output_dir / "_stage5_rerun_log")
    log.path = output_dir / "_stage5_v2_rerun.log.md"

    print(f"Re-running Stage 5 v2 on {len(filtered_data.get('items', []))} items …")
    result = orch.stage_5_wiki_candidates(filtered_data, output_dir, log, lens=lens)
    log.write(lens, output_dir)

    print(f"\nResult: {result}")
    print(f"Markdown:  {output_dir / '04-wiki-candidates-v2.md'}")
    print(f"Sidecar:   {output_dir / '04-wiki-candidates-v2.json'}")
    print(f"Stage log: {log.path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
