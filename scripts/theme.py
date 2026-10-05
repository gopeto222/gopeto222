"""Shared visual tokens for the public profile SVG generators."""
from __future__ import annotations

BG = '#090F1B'
SURFACE = '#111C2D'
ELEVATED = '#17263B'
BORDER = '#344B67'
TEXT = '#F2F6FF'
MUTED = '#AEC0D8'
SOFT = '#849BB8'
BLUE = '#3B82F6'
CYAN = '#22D3EE'
PURPLE = '#8B5CF6'
VIOLET = '#A855F7'
GREEN = '#22C55E'
ORANGE = '#F59E0B'
RED = '#EF4444'
SHELL_END = '#121C36'
GRID = '#22314B'
SELECTED = '#243F69'
CORE = '#202956'
PREVIEW_BLUE = '#182E4D'
PREVIEW_ORANGE = '#192D4C'
PREVIEW_NODE = '#274268'
TRACK = '#243652'
FONT = 'Arial,Helvetica,sans-serif'
RADIUS_SMALL = 9
RADIUS_MEDIUM = 14
RADIUS_LARGE = 24
SPACE = 8

PROJECT_ACCENTS = {
    'codeguard': PURPLE,
    'rules': BLUE,
    'dmv': ORANGE,
    'registry': ORANGE,
    'collaboration': ORANGE,
}
CATEGORY_ACCENTS = {
    'Developer tools': PURPLE,
    'Engineering operations': CYAN,
    'FiveM systems': ORANGE,
    'Web systems': BLUE,
}
ARCHITECTURE_ACCENTS = {
    'frontend': BLUE,
    'backend': PURPLE,
    'database': CYAN,
    'security': RED,
    'external': ORANGE,
    'ai': VIOLET,
    'infrastructure': GREEN,
}
ACTIVITY_LEVELS = ('#213147', '#2856A4', BLUE, CYAN, PURPLE)


def tinted(accent: str, opacity: float = .12) -> str:
    """Opaque dark surface tinted by an accent; SVG opacity handles the color layer."""
    return f'<rect width="100%" height="100%" fill="{accent}" opacity="{opacity}"/>'
