"""Accessible SVG primitives. No scripts, remote fonts or external images."""
from __future__ import annotations

from html import escape
from theme import (BACKGROUND_0, BACKGROUND_1, SURFACE_0, SURFACE_1, BORDER_SUBTLE,
                   TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, BLUE, CYAN, PURPLE,
                   FONT, MONO, RADIUS_LARGE)


def e(value: object) -> str:
    return escape(str(value), quote=True)


def text(x: int, y: int, value: object, size: int = 20, color: str = TEXT_PRIMARY,
         weight: int = 400, anchor: str = 'start', mono: bool = False, spacing: int = 0) -> str:
    family = MONO if mono else FONT
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{spacing}">{e(value)}</text>')


def lines(x: int, y: int, values: list[str], size: int = 20, color: str = TEXT_SECONDARY,
          weight: int = 400, gap: int | None = None) -> str:
    return ''.join(text(x, y + i * (gap or size + 10), value, size, color, weight) for i, value in enumerate(values))


def rect(x: int, y: int, width: int, height: int, fill: str = SURFACE_0,
         stroke: str = BORDER_SUBTLE, radius: int = 16, opacity: float = 1) -> str:
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" opacity="{opacity}"/>')


def rule(x1: int, y1: int, x2: int, y2: int, color: str = BORDER_SUBTLE,
         width: int = 2, dash: str = '') -> str:
    extra = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"{extra} fill="none"/>'


def circle(x: int, y: int, radius: int, fill: str, stroke: str = 'none', width: int = 1,
           opacity: float = 1) -> str:
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" opacity="{opacity}"/>'


def pill(x: int, y: int, label: str, width: int, accent: str, size: int = 16) -> str:
    return rect(x, y, width, 38, SURFACE_1, accent, 10) + text(x + width//2, y+25, label, size, accent, 700, 'middle')


def panel(x: int, y: int, width: int, height: int, accent: str,
          fill: str = SURFACE_0, radius: int = 18) -> str:
    return (rect(x, y, width, height, fill, accent, radius)
            + f'<rect x="{x+1}" y="{y+1}" width="{width-2}" height="{min(height-2,90)}" rx="{radius-1}" fill="{accent}" opacity=".075"/>'
            + rule(x+18, y+2, x+width-18, y+2, accent, 3))


def node(x: int, y: int, width: int, height: int, label: str, accent: str, detail: str = '',
         size: int = 18) -> str:
    body = panel(x, y, width, height, accent, SURFACE_1, 13)
    body += circle(x+22, y+height//2, 5, accent)
    body += text(x+37, y+height//2+6 if not detail else y+height//2-1, label, size, TEXT_PRIMARY, 700)
    if detail:
        body += text(x+37, y+height//2+22, detail, 13, TEXT_MUTED, 600)
    return body


def arrow(x1: int, y1: int, x2: int, y2: int, accent: str) -> str:
    body = rule(x1, y1, x2, y2, accent, 2)
    if x2 > x1:
        body += f'<path d="M{x2-9} {y2-5}L{x2} {y2}L{x2-9} {y2+5}" stroke="{accent}" stroke-width="2" fill="none"/>'
    elif y2 > y1:
        body += f'<path d="M{x2-5} {y2-9}L{x2} {y2}L{x2+5} {y2-9}" stroke="{accent}" stroke-width="2" fill="none"/>'
    return body


def grid(width: int, height: int, step: int = 44) -> str:
    paths = []
    for x in range(0, width+1, step):
        paths.append(rule(x, 0, x, height, BORDER_SUBTLE, 1))
    for y in range(0, height+1, step):
        paths.append(rule(0, y, width, y, BORDER_SUBTLE, 1))
    return f'<g opacity=".25">{"".join(paths)}</g>'


def document(width: int, height: int, title: str, description: str, body: str,
             accent: str = BLUE, secondary: str = CYAN, gridded: bool = False) -> str:
    defs = (f'<defs><linearGradient id="shell" x2="1" y2="1"><stop stop-color="{BACKGROUND_1}"/>'
            f'<stop offset=".65" stop-color="{BACKGROUND_0}"/><stop offset="1" stop-color="{SURFACE_0}"/></linearGradient>'
            f'<linearGradient id="accent"><stop stop-color="{accent}"/><stop offset="1" stop-color="{secondary}"/></linearGradient>'
            f'<radialGradient id="aura"><stop stop-color="{accent}" stop-opacity=".3"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="clip"><rect width="{width}" height="{height}" rx="{RADIUS_LARGE}"/></clipPath></defs>')
    shell = (f'<rect width="{width}" height="{height}" rx="{RADIUS_LARGE}" fill="url(#shell)"/>'
             f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="{RADIUS_LARGE-1}" fill="none" stroke="{BORDER_SUBTLE}"/>'
             f'<path d="M28 1H{width-28}" stroke="url(#accent)" stroke-width="2" opacity=".8"/>')
    content = (grid(width, height) if gridded else '') + body
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">'
            f'<title id="title">{e(title)}</title><desc id="desc">{e(description)}</desc>{defs}{shell}'
            f'<g clip-path="url(#clip)">{content}</g></svg>\n')


def wrap(value: str, limit: int) -> list[str]:
    """Stable word wrapping for fixed-size SVG text blocks."""
    result: list[str] = []
    current = ''
    for word in value.split():
        trial = f'{current} {word}'.strip()
        if current and len(trial) > limit:
            result.append(current)
            current = word
        else:
            current = trial
    if current:
        result.append(current)
    return result
