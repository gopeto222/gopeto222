"""Generate a small, auditable public GitHub activity card."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "activity.json"
SVG = ROOT / "assets" / "metrics" / "activity.svg"
QUERY = "query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"


def request_calendar(login: str, token: str) -> dict[str, Any]:
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql", data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "astrobyte-profile-metrics"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = json.load(response)
            if payload.get("errors"):
                raise ValueError("GitHub GraphQL returned errors")
            return payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("GitHub request failed")


def parse_calendar(calendar: dict[str, Any]) -> dict[str, Any]:
    weeks = calendar.get("weeks")
    if not isinstance(weeks, list) or not weeks:
        raise ValueError("Missing contribution weeks")
    days: dict[str, int] = {}
    for week in weeks:
        for item in week["contributionDays"]:
            day = date.fromisoformat(item["date"])
            count = item["contributionCount"]
            if not isinstance(count, int) or count < 0 or day.isoformat() in days:
                raise ValueError("Invalid contribution day")
            days[day.isoformat()] = count
    if not days or sum(days.values()) != calendar.get("totalContributions"):
        raise ValueError("Calendar total mismatch")
    return {"total": sum(days.values()), "active_days": sum(n > 0 for n in days.values()), "days": dict(sorted(days.items()))}


def streaks(days: dict[str, int], today: date) -> tuple[int, int]:
    longest = run = 0
    for key, count in sorted(days.items()):
        run = run + 1 if count else 0
        longest = max(longest, run)
    cursor = today if days.get(today.isoformat(), 0) else today - timedelta(days=1)
    current = 0
    while days.get(cursor.isoformat(), 0):
        current += 1
        cursor -= timedelta(days=1)
    return current, longest


def render_svg(data: dict[str, Any], generated: str) -> str:
    days = data["days"]
    current, longest = streaks(days, date.fromisoformat(generated))
    last = max((key for key, value in days.items() if value), default="No public activity")
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 250" role="img" aria-labelledby="t d">',
        '<title id="t">GitHub activity</title><desc id="d">Public contribution calendar summary</desc>',
        '<rect width="900" height="250" rx="18" fill="#151b23"/>',
        '<text x="30" y="43" fill="#69d2c7" font-family="Arial,sans-serif" font-size="18">GITHUB ACTIVITY</text>',
    ]
    for x, label, value in [(30, "CONTRIBUTIONS", data["total"]), (245, "ACTIVE DAYS", data["active_days"]), (460, "CURRENT STREAK", current), (675, "LONGEST STREAK", longest)]:
        lines.extend([f'<text x="{x}" y="105" fill="#f0f6f8" font-family="Arial,sans-serif" font-size="42" font-weight="700">{value}</text>', f'<text x="{x}" y="133" fill="#adc2c8" font-family="Arial,sans-serif" font-size="14">{label}</text>'])
    lines.extend([f'<text x="30" y="200" fill="#adc2c8" font-family="Arial,sans-serif" font-size="18">Last contribution: {last}</text>', f'<text x="30" y="229" fill="#789ca3" font-family="Arial,sans-serif" font-size="14">GitHub public calendar · generated {generated} UTC · rolling yearly window</text>', '</svg>'])
    return "\n".join(lines) + "\n"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    if args.validate:
        stored = json.loads(DATA.read_text())
        parsed = parse_calendar({"weeks": [{"contributionDays": [{"date": key, "contributionCount": value} for key, value in stored["days"].items()]}], "totalContributions": stored["total"]})
        if parsed != stored:
            raise ValueError("Invalid generated JSON")
        ET.parse(SVG)
        return
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN or GITHUB_TOKEN is required")
    data = parse_calendar(request_calendar("gopeto222", token))
    today = datetime.now(timezone.utc).date().isoformat()
    atomic_write(DATA, json.dumps(data, indent=2, sort_keys=True) + "\n")
    atomic_write(SVG, render_svg(data, today))


if __name__ == "__main__":
    main()
