"""Check public portfolio assets, links, localization parity and attribution data."""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def verify() -> None:
    projects=json.loads((ROOT/'data/projects.json').read_text(encoding='utf-8'))['projects']
    if len(projects)!=len({project['id'] for project in projects}):
        raise ValueError('Duplicate project IDs')
    if any(project['visibility']=='private' and project['repository'] for project in projects):
        raise ValueError('Private repository path in public inventory')
    for asset in (ROOT/'assets').rglob('*.svg'):
        ET.parse(asset)
    for language in ('en','bg'):
        path=ROOT/('README.md' if language=='en' else 'README.bg.md')
        content=path.read_text(encoding='utf-8')
        other='README.bg.md' if language=='en' else 'README.md'
        if f'<a href="{other}"' not in content or f'header-{language}.svg' not in content or f'header-{language}-mobile.svg' not in content:
            raise ValueError(f'{path}: missing linked language control')
        ids=set(re.findall(r'<a id="([^"]+)"></a>',content))
        for target in re.findall(r'(?:src|srcset|href)="([^"]+)"',content):
            if target.startswith(('http://','https://')):continue
            if target.startswith('#'):
                if target[1:] not in ids:raise ValueError(f'{path}: missing anchor {target}')
            elif not (ROOT/target.split('#')[0]).exists():
                raise ValueError(f'{path}: missing file {target}')
        for target in re.findall(r'\[[^]]+\]\(([^)]+)\)',content):
            if not target.startswith(('http://','https://','#')) and not (ROOT/target.split('#')[0]).exists():
                raise ValueError(f'{path}: missing Markdown link {target}')
        for alt in re.findall(r'<img[^>]+alt="([^"]*)"',content):
            if not alt.strip():raise ValueError(f'{path}: image without alt text')
        for project in (p for p in projects if p['featured']):
            name={'AstroByte CodeGuard':'codeguard','Rules administration platform':'rules','DMV tablet system':'dmv','Business registry':'registry','Collaborative FiveM server infrastructure':'collaboration'}[project['name']]
            if f'feature-{name}-{language}.svg' not in content:
                raise ValueError(f'{path}: missing featured {name}')
        for required in ('command-center','featured-systems','all-projects','how-i-build','technology','architecture','activity','about','contact'):
            if required not in ids:raise ValueError(f'{path}: missing {required}')
    print(f'QA passed: {len(projects)} projects, bilingual links, anchors, alt text and SVGs')


if __name__=='__main__':verify()
