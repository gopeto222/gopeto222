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

from theme import BG, SURFACE, BORDER, TEXT, MUTED, SOFT, BLUE, CYAN, GREEN, ACTIVITY_LEVELS

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "activity.json"
SVGS = [ROOT / "assets" / "metrics" / f"activity-{lang}{suffix}.svg" for lang in ("en", "bg") for suffix in ("", "-mobile")]
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
        if not isinstance(week, dict) or not isinstance(week.get("contributionDays"), list):
            raise ValueError("Invalid contribution week")
        for item in week["contributionDays"]:
            if not isinstance(item, dict) or "date" not in item or "contributionCount" not in item:
                raise ValueError("Invalid contribution day")
            if not isinstance(item["date"], str):
                raise ValueError("Invalid contribution date")
            day = date.fromisoformat(item["date"])
            count = item["contributionCount"]
            if type(count) is not int or count < 0 or day.isoformat() in days:
                raise ValueError("Invalid contribution day")
            days[day.isoformat()] = count
    if not days or sum(days.values()) != calendar.get("totalContributions"):
        raise ValueError("Calendar total mismatch")
    ordered = sorted(date.fromisoformat(key) for key in days)
    if any(right - left != timedelta(days=1) for left, right in zip(ordered, ordered[1:])):
        raise ValueError("Non-contiguous contribution calendar")
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


def render_svg(data: dict[str, Any], generated: str, lang: str = "en", mobile: bool = False) -> str:
    """Render a responsive activity dashboard from GitHub's calendar."""
    days = data["days"]
    current, longest = streaks(days, date.fromisoformat(generated))
    bg = lang == "bg"
    labels = ("ПРИНОСИ", "АКТИВНИ ДНИ", "ТЕКУЩА ПОРЕДИЦА", "НАЙ-ДЪЛГА ПОРЕДИЦА") if bg else ("CONTRIBUTIONS", "ACTIVE DAYS", "CURRENT STREAK", "LONGEST STREAK")
    last = max((key for key, value in days.items() if value), default="—")
    width, height = (600, 650) if mobile else (1200, 455)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
        '<title id="t">Development activity</title><desc id="d">Public GitHub contribution calendar with totals and daily intensity</desc>',
        f'<rect width="{width}" height="{height}" rx="24" fill="{BG}"/>',
        f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="23" fill="none" stroke="{BORDER}"/>',
        f'<text x="30" y="44" fill="{CYAN}" font-family="Arial,sans-serif" font-size="19" font-weight="700" letter-spacing="2">{("08 / АКТИВНОСТ" if bg else "08 / DEVELOPMENT ACTIVITY")}</text>',
    ]
    values = (data["total"], data["active_days"], current, longest)
    for i, (label, value) in enumerate(zip(labels, values)):
        if mobile:
            x, y, card_w = 30 + (i % 2) * 274, 74 + (i // 2) * 132, 260
        else:
            x, y, card_w = 30 + i * 290, 78, 270
        accent = GREEN if i in (1, 2, 3) else BLUE
        lines += [
            f'<path d="M{x+14} {y+1}H{x+card_w-14}" stroke="{accent}" stroke-width="3"/>',
            f'<rect x="{x}" y="{y}" width="{card_w}" height="110" rx="13" fill="{SURFACE}" stroke="{accent}"/>',
            f'<text x="{x+17}" y="{y+33}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{13 if mobile else 15}" font-weight="700">{label}</text>',
            f'<text x="{x+17}" y="{y+83}" fill="{accent}" font-family="Arial,sans-serif" font-size="44" font-weight="700">{value}</text>',
        ]
    heading_y = 365 if mobile else 243
    lines.append(f'<text x="30" y="{heading_y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="16">{("Последен принос: " if bg else "Last contribution: ")}{last}</text>')
    selected = sorted(days.items())[-182:] if mobile else sorted(days.items())
    first = date.fromisoformat(selected[0][0])
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    cell = 18 if mobile else 15
    palette = ACTIVITY_LEVELS
    top = 390 if mobile else 268
    for key, count in selected:
        day = date.fromisoformat(key)
        week = (day - start).days // 7
        row = (day.weekday() + 1) % 7
        shade = 0 if count == 0 else min(4, 1 + (count >= 2) + (count >= 4) + (count >= 8))
        lines.append(f'<rect x="{30 + week * cell}" y="{top + row * cell}" width="{cell-4}" height="{cell-4}" rx="2" fill="{palette[shade]}"/>')
    window = "26 weeks shown / totals for rolling year" if mobile else "Rolling yearly window"
    if bg:
        window = "26 седмици / годишни общи данни" if mobile else "Последните 12 месеца"
    lines.append(f'<text x="30" y="{height-57}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="15">{window}</text>')
    lines.append(f'<text x="30" y="{height-27}" fill="{SOFT}" font-family="Arial,sans-serif" font-size="14">GitHub public calendar · {generated} UTC</text>')
    lines.append('</svg>')
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
    parser.add_argument("--force-render", action="store_true", help="Regenerate visuals after a design change")
    args = parser.parse_args()
    if args.validate:
        stored = json.loads(DATA.read_text())
        parsed = parse_calendar({"weeks": [{"contributionDays": [{"date": key, "contributionCount": value} for key, value in stored["days"].items()]}], "totalContributions": stored["total"]})
        if parsed != stored:
            raise ValueError("Invalid generated JSON")
        for path in SVGS:
            ET.parse(path)
        return
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN or GITHUB_TOKEN is required")
    data = parse_calendar(request_calendar("gopeto222", token))
    if DATA.exists() and not args.force_render:
        previous = json.loads(DATA.read_text())
        meaningful = lambda payload: (
            payload['total'], payload['active_days'],
            {key: count for key, count in payload['days'].items() if count}
        )
        if meaningful(data) == meaningful(previous):
            print('No contribution change; keeping the existing dated snapshot.')
            return
    today = datetime.now(timezone.utc).date().isoformat()
    atomic_write(DATA, json.dumps(data, indent=2, sort_keys=True) + "\n")
    for lang in ("en", "bg"):
        for mobile in (False, True):
            suffix = "-mobile" if mobile else ""
            atomic_write(ROOT / "assets" / "metrics" / f"activity-{lang}{suffix}.svg", render_svg(data, today, lang, mobile))


if __name__ == "__main__":
    main()
