"""Behavioral checks for public activity metrics."""

import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from metrics import parse_calendar, render_svg, request_calendar, streaks  # noqa: E402


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
        ET.fromstring(render_svg(result, "2026-10-05", "bg", True))
        self.assertEqual(render_svg(result, "2026-10-05").count('width="11"'), 4)

    def test_rejects_bad_responses(self):
        for calendar in ({}, {"weeks": [], "totalContributions": 0}, {"weeks": [{}], "totalContributions": 0}, {"weeks": [{"contributionDays": [{}]}], "totalContributions": 0}, {"weeks": [{"contributionDays": [{"date": "2026-01-01", "contributionCount": -1}]}], "totalContributions": -1}, {"weeks": [{"contributionDays": [{"date": "2026-01-01", "contributionCount": 1},{"date": "2026-01-03", "contributionCount": 1}]}], "totalContributions": 2}):
            with self.subTest(calendar=calendar), self.assertRaises(ValueError):
                parse_calendar(calendar)

    def test_graphql_error_response(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *_): return False
        with patch('metrics.urllib.request.urlopen', return_value=Response()), patch('metrics.json.load', return_value={'errors':[{'message':'rate limit'}]}):
            with self.assertRaises(ValueError):
                request_calendar('gopeto222','placeholder')

    def test_empty_activity(self):
        result = parse_calendar({"totalContributions": 0, "weeks": [{"contributionDays": [{"date": "2026-01-01", "contributionCount": 0}]}]})
        self.assertEqual(streaks(result["days"], date(2026, 1, 1)), (0, 0))
        self.assertIn("Last contribution: —", render_svg(result, "2026-01-01"))


if __name__ == "__main__":
    unittest.main()
