"""Validate public data, bilingual pages and every generated visual."""
from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
SVG_NS='{http://www.w3.org/2000/svg}'


def read_json(path: str) -> dict:
    value=json.loads((ROOT/path).read_text(encoding='utf-8'))
    if not isinstance(value,dict):
        raise ValueError(f'{path}: expected an object')
    return value


def validate_projects(inventory: dict, profile: dict, visuals: dict) -> None:
    projects=inventory['projects']
    ids=[p['id'] for p in projects]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate project IDs')
    if len(projects)!=inventory['auditSummary']['includedRepositories']:
        raise ValueError('Inventory summary mismatch')
    for project in projects:
        if not project['verified'] or not project['publicDisplayAllowed']:
            raise ValueError(f"Unverified project {project['id']}")
        if project['visibility']=='private' and (project.get('repository') or project.get('repositoryUrl') or project.get('demoUrl')):
            raise ValueError(f"Private URL exposed by {project['id']}")
        if project['ownership']!='personal' and not (
            project['contributionEvidence']['authoredCommitsObserved'] or
            project['contributionEvidence']['authoredPullRequestsObserved']
        ):
            raise ValueError(f"Unverified contribution {project['id']}")
        if project['architectureKey'] and project['architectureKey'] not in profile['caseStudies']:
            raise ValueError(f"Unknown architecture {project['id']}")
        for screenshot in project['screenshots']:
            if not (ROOT/screenshot).is_file():
                raise ValueError(f"Missing screenshot {screenshot}")
    featured={p['id'] for p in projects if p['featured']}
    cases={c['projectId'] for c in profile['caseStudies'].values()}
    if featured!=cases: raise ValueError('Featured project/case study mismatch')
    if set(visuals['featured'])!=set(profile['caseStudies']):
        raise ValueError('Visual manifest/case study mismatch')
    for key,item in visuals['featured'].items():
        if item['projectId']!=profile['caseStudies'][key]['projectId']:
            raise ValueError(f'Visual manifest project mismatch: {key}')
        for capture in item['screenshots']:
            if not capture.get('reviewed') or not capture.get('redacted'):
                raise ValueError(f'Unreviewed screenshot: {key}')
            if not (ROOT/capture['path']).is_file():
                raise ValueError(f"Missing screenshot {capture['path']}")


def validate_svg(path: Path) -> None:
    root=ET.parse(path).getroot()
    if root.tag!=SVG_NS+'svg': raise ValueError(f'{path}: not SVG')
    if not root.get('viewBox'): raise ValueError(f'{path}: missing viewBox')
    ids=[]
    for node in root.iter():
        if node.get('id'): ids.append(node.get('id'))
        if node.tag in (SVG_NS+'script',SVG_NS+'foreignObject'):
            raise ValueError(f'{path}: forbidden embedded code')
        if node.tag==SVG_NS+'text':
            size=float(node.get('font-size','0'))
            if size<13: raise ValueError(f'{path}: text too small')
        for key,value in node.attrib.items():
            if key.endswith('href') and urlsplit(value).scheme:
                raise ValueError(f'{path}: external dependency')
    if len(ids)!=len(set(ids)): raise ValueError(f'{path}: duplicate SVG ID')
    if root.find(SVG_NS+'title') is None or root.find(SVG_NS+'desc') is None:
        raise ValueError(f'{path}: missing accessible title/description')


def normalize(path: str) -> str:
    return re.sub(r'(?<=[-/])(en|bg)(?=[-.])','XX',path)


def validate_readmes() -> set[str]:
    referenced=set()
    counterparts=[]
    anchors_expected={'engineering','featured','archive','fivem','technology','architecture','activity','practice','services','contact'}
    for lang,name,other in [('en','README.md','README.bg.md'),('bg','README.bg.md','README.md')]:
        path=ROOT/name
        content=path.read_text(encoding='utf-8')
        if not content.startswith('<!-- Generated from'):
            raise ValueError(f'{name}: missing generator marker')
        if f'<a href="{other}"' not in content:
            raise ValueError(f'{name}: missing linked language control')
        anchors=set(re.findall(r'<a id="([^"]+)"></a>',content))
        if anchors!=anchors_expected: raise ValueError(f'{name}: chapter parity failure')
        assets=re.findall(r'(?:src|srcset)="([^"]+)"',content)
        counterparts.append([normalize(a) for a in assets])
        for asset in assets:
            if not (ROOT/asset).is_file(): raise ValueError(f'{name}: missing asset {asset}')
            referenced.add(asset)
        for alt in re.findall(r'<img[^>]+alt="([^"]*)"',content):
            if not alt.strip(): raise ValueError(f'{name}: empty image alt')
        for href in re.findall(r'href="([^"]+)"',content):
            if href.startswith('#'):
                if href[1:] not in anchors: raise ValueError(f'{name}: broken anchor {href}')
            elif not urlsplit(href).scheme and not (ROOT/href.split('#')[0]).is_file():
                raise ValueError(f'{name}: broken local link {href}')
        for href in re.findall(r'\[[^]]+\]\(([^)]+)\)',content):
            if not urlsplit(href).scheme and not (ROOT/href.split('#')[0]).is_file():
                raise ValueError(f'{name}: broken Markdown link {href}')
    if counterparts[0]!=counterparts[1]:
        raise ValueError('EN/BG visual coverage differs')
    generated={str(path.relative_to(ROOT)) for path in (ROOT/'assets/generated').glob('*.svg')}
    if generated != generated & referenced:
        raise ValueError(f'Unreferenced generated assets: {sorted(generated-referenced)}')
    return referenced


def verify() -> None:
    inventory=read_json('data/projects.json')
    profile=read_json('data/profile.json')
    visuals=read_json('data/visuals.json')
    validate_projects(inventory,profile,visuals)
    referenced=validate_readmes()
    for asset in (ROOT/'assets').rglob('*.svg'):
        validate_svg(asset)
    print(f"QA passed: {len(inventory['projects'])} verified projects, {len(referenced)} linked SVG references, EN/BG parity and valid assets")


if __name__=='__main__':
    verify()
