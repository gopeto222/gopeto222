"""Behavioral checks for public activity metrics."""

import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from metrics import parse_calendar, render_svg, streaks  # noqa: E402


class MetricsTests(unittest.TestCase):
    def test_calendar_and_streaks(self):
        calendar = {"totalContributions": 5, "weeks": [{"contributionDays": [
            {"date": "2026-10-02", "contributionCount": 2},
            {"date": "2026-10-03", "contributionCount": 0},
            {"date": "2026-10-04", "contributionCount": 2},
            {"date": "2026-10-05", "contributionCount": 1},
        ]}]}
        result = parse_calendar(calendar)
        self.assertEqual((result["total"], result["active_days"]), (5, 3))
        self.assertEqual(streaks(result["days"], date(2026, 10, 5)), (2, 2))
        self.assertEqual(streaks(result["days"], date(2026, 10, 6)), (2, 2))
        ET.fromstring(render_svg(result, "2026-10-05"))
        self.assertEqual(render_svg(result, "2026-10-05").count('<rect x='), 4)

    def test_rejects_bad_responses(self):
        for calendar in ({}, {"weeks": [], "totalContributions": 0}, {"weeks": [{}], "totalContributions": 0}, {"weeks": [{"contributionDays": [{}]}], "totalContributions": 0}, {"weeks": [{"contributionDays": [{"date": "2026-01-01", "contributionCount": -1}]}], "totalContributions": -1}):
            with self.subTest(calendar=calendar), self.assertRaises(ValueError):
                parse_calendar(calendar)

    def test_empty_activity(self):
        result = parse_calendar({"totalContributions": 0, "weeks": [{"contributionDays": [{"date": "2026-01-01", "contributionCount": 0}]}]})
        self.assertEqual(streaks(result["days"], date(2026, 1, 1)), (0, 0))
        self.assertIn("No public activity", render_svg(result, "2026-01-01"))


if __name__ == "__main__":
    unittest.main()
