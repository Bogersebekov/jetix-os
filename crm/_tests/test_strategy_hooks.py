"""Strategy hooks engine tests."""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from crm._scripts import strategy_hooks as sh  # noqa: E402


class HooksTests(unittest.TestCase):
    def _dach_advisor(self):
        return {
            "name": "X", "slug": "x", "type": "person",
            "roles": ["advisor", "friend"],
            "tags": ["#dach", "#ai-native"],
            "icp": {"startupper": "yes", "adequate": 4},
            "audience": {"total_followers": 5000},
            "location_country": "DE",
            "created": "2026-04-26", "updated": "2026-04-26",
        }

    def _ru_mentor(self):
        return {
            "name": "Y", "slug": "y", "type": "person",
            "roles": ["mentor", "interesting"],
            "tags": [],
            "icp": {"startupper": "no"},
            "location_country": "RU",
            "created": "2026-04-26", "updated": "2026-04-26",
        }

    def test_offers_for_dach_advisor(self):
        offers = sh.suggest_offers(self._dach_advisor())
        ids = {o["id"] for o in offers}
        # DACH+startupper+advisor should match l6-community-access + methodology-early-access
        self.assertIn("l6-community-access", ids)
        self.assertIn("methodology-early-access", ids)
        # draft should NOT appear by default
        self.assertNotIn("l7-producer-collab", ids)

    def test_draft_visible_with_flag(self):
        offers = sh.suggest_offers(self._dach_advisor(), include_draft=True)
        ids = {o["id"] for o in offers}
        self.assertIn("l7-producer-collab", ids)

    def test_offers_filtered_by_role_mismatch(self):
        # ai-pilot-engagement requires role=client_lead
        offers = sh.suggest_offers(self._dach_advisor())
        ids = {o["id"] for o in offers}
        self.assertNotIn("ai-pilot-engagement", ids)

    def test_asks_for_advisor(self):
        asks = sh.suggest_asks(self._dach_advisor())
        ids = {a["id"] for a in asks}
        self.assertIn("advisor-cooperation", ids)
        self.assertIn("methodology-feedback", ids)
        self.assertIn("dach-intros", ids)

    def test_asks_no_match_for_offrole(self):
        asks = sh.suggest_asks(self._ru_mentor())
        ids = {a["id"] for a in asks}
        # DACH-only ask should not appear for RU
        self.assertNotIn("dach-intros", ids)
        # mentor satisfies advisor-cooperation
        self.assertIn("advisor-cooperation", ids)

    def test_render_section_empty(self):
        out = sh.render_section([])
        self.assertIn("none", out.lower())

    def test_render_section_nonempty(self):
        out = sh.render_section(sh.suggest_offers(self._dach_advisor()))
        self.assertIn("auto-suggested", out)


if __name__ == "__main__":
    unittest.main()
