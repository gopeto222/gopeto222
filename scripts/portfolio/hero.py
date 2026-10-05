"""One opening composition, including the linked language state."""
from __future__ import annotations

from theme import (BLUE, CYAN, PURPLE, VIOLET, GREEN, AMBER, TEXT_PRIMARY,
                   TEXT_SECONDARY, TEXT_MUTED, SURFACE_0, SURFACE_1, BORDER_SUBTLE, CONTROL_ACTIVE, ORBIT_CORE)
from portfolio.svg import document, text, lines, panel, rect, circle, rule, arrow, pill, wrap


def language_control(width: int, lang: str) -> str:
    x = width - 175
    active = 0 if lang == 'en' else 1
    body = rect(x, 37, 137, 42, SURFACE_1, BORDER_SUBTLE, 12)
    body += rect(x+4+active*64, 41, 64, 34, CONTROL_ACTIVE, BLUE, 9)
    body += text(x+36, 63, 'EN', 16, TEXT_PRIMARY if active == 0 else TEXT_MUTED, 800, 'middle')
    body += text(x+100, 63, 'BG', 16, TEXT_PRIMARY if active == 1 else TEXT_MUTED, 800, 'middle')
    return body


def brand(width: int, lang: str) -> str:
    body = circle(52, 58, 18, 'none', CYAN, 2)
    body += circle(52, 58, 5, CYAN)
    body += rule(63, 46, 74, 35, PURPLE, 2)
    body += text(84, 65, 'ASTROBYTE  //  ENGINEERING', 19 if width == 1200 else 17, TEXT_PRIMARY, 800, spacing=2)
    body += language_control(width, lang)
    body += rule(36, 104, width-36, 104, BORDER_SUBTLE)
    return body


def orbit_map(cx: int, cy: int, scale: float = 1) -> str:
    """Abstract domain topology; labels describe work areas, never live metrics."""
    r = round(110*scale)
    body = circle(cx, cy, r+42, 'none', BORDER_SUBTLE, 1, .8)
    body += circle(cx, cy, r+12, 'none', PURPLE, 1, .5)
    body += circle(cx, cy, r, SURFACE_0, BLUE, 2)
    body += circle(cx, cy, round(54*scale), ORBIT_CORE, CYAN, 2)
    body += circle(cx, cy, round(30*scale), 'none', PURPLE, 2, .7)
    body += text(cx, cy+7, 'AB', round(31*scale), TEXT_PRIMARY, 800, 'middle', spacing=1)
    offsets = [(-143,-108,'TOOLS',PURPLE), (142,-108,'WEB',BLUE),
               (-180,24,'FIVEM',AMBER), (170,30,'DATA',CYAN),
               (-118,145,'MACOS',VIOLET), (120,145,'SECURITY',GREEN)]
    for dx,dy,label,accent in offsets:
        nx,ny=cx+round(dx*scale),cy+round(dy*scale)
        body += rule(cx,cy,nx,ny,accent,2)
        body += circle(nx,ny,round(7*scale),accent)
        body += circle(nx,ny,round(15*scale),'none',accent,1,.5)
        body += text(nx,ny-round(18*scale),label,20,TEXT_SECONDARY,700,'middle',spacing=1)
    return body


def render(profile: dict, lang: str, mobile: bool) -> str:
    copy=profile['copy'][lang]
    w,h=(600,850) if mobile else (1200,600)
    body=brand(w,lang)
    body += f'<ellipse cx="{w-80}" cy="180" rx="320" ry="220" fill="url(#aura)"/>'
    body += f'<ellipse cx="{w//2}" cy="{h-30}" rx="380" ry="130" fill="{PURPLE}" opacity=".08"/>'
    if mobile:
        body += text(40,158,'GEORGI',65,TEXT_PRIMARY,800,spacing=2)
        body += text(40,219,'KANCHEV',57,TEXT_PRIMARY,800,spacing=1)
        body += text(42,259,'SOFTWARE ENGINEER  /  PRODUCT BUILDER' if lang=='en' else 'СОФТУЕРЕН ИНЖЕНЕР  /  СЪЗДАТЕЛ',17,CYAN,700)
        body += lines(42,308,wrap(copy['heroLine'],42),22,TEXT_SECONDARY,500,31)
        body += rule(42,367,558,367,PURPLE,2)
        body += pill(42,385,'DEV TOOLS',145,PURPLE,18)+pill(202,385,'FIVEM',108,AMBER,18)+pill(325,385,'WEB',105,BLUE,18)
        body += panel(38,454,524,317,BLUE,SURFACE_0,22)
        body += text(58,488,'DOMAIN TOPOLOGY',19,CYAN,800,spacing=2)
        body += orbit_map(300,624,.59)
        body += rule(38,800,562,800,BORDER_SUBTLE)
        body += text(40,830,'01 / ENGINEERING PORTFOLIO',17,TEXT_MUTED,700,spacing=1)
    else:
        body += text(56,190,'GEORGI',97,TEXT_PRIMARY,800,spacing=3)
        body += text(56,273,'KANCHEV',77,TEXT_PRIMARY,800,spacing=1)
        body += text(59,316,'SOFTWARE ENGINEER  /  PRODUCT BUILDER' if lang=='en' else 'СОФТУЕРЕН ИНЖЕНЕР  /  СЪЗДАТЕЛ',22,CYAN,700,spacing=1)
        body += lines(59,371,wrap(copy['heroLine'],54),25,TEXT_SECONDARY,500,36)
        body += pill(58,459,'DEVELOPER TOOLS',185,PURPLE)+pill(257,459,'FIVEM SYSTEMS',170,AMBER)+pill(441,459,'FULL STACK',145,BLUE)
        body += text(59,562,'01 / BUILD  →  REVIEW  →  SHIP',17,TEXT_MUTED,700,spacing=1)
        body += panel(669,135,483,406,BLUE,SURFACE_0,24)
        body += text(695,172,'SYSTEM / DOMAIN MAP',18,CYAN,700,spacing=2)
        body += orbit_map(910,330,.78)
    title = 'Georgi Kanchev — AstroByte engineering portfolio' if lang=='en' else 'Георги Канчев — инженерно портфолио на AstroByte'
    return document(w,h,title,copy['heroLine']+' Language control links to the other README.',body,PURPLE,CYAN,True)
