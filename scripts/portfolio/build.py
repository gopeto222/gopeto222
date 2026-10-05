"""Generate the bilingual visual portfolio from public-safe source data."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from portfolio import hero, projects as project_views, architecture, sections

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/generated'


def data() -> tuple[dict, list[dict], dict]:
    profile=json.loads((ROOT/'data/profile.json').read_text(encoding='utf-8'))
    projects=json.loads((ROOT/'data/projects.json').read_text(encoding='utf-8'))['projects']
    languages=json.loads((ROOT/'data/languages.json').read_text(encoding='utf-8'))
    return profile,projects,languages


def generate() -> list[Path]:
    profile,projects,languages=data()
    ids={p['id'] for p in projects}
    if len(ids)!=len(projects): raise ValueError('Duplicate project IDs')
    if any(not p['publicDisplayAllowed'] or not p['verified'] for p in projects):
        raise ValueError('Unverified or non-public record in public inventory')
    if any(p['visibility']=='private' and (p['repository'] or p['repositoryUrl']) for p in projects):
        raise ValueError('Private repository URL in public inventory')
    for key,case in profile['caseStudies'].items():
        if case['projectId'] not in ids: raise ValueError(f'Unknown featured project {key}')
    OUT.mkdir(parents=True,exist_ok=True)
    results=[]
    names=[]
    by_id={p['id']:p for p in projects}
    category_names={'Developer tools':'tools','Engineering operations':'operations','FiveM systems':'fivem','Web systems':'web'}
    for lang in ('en','bg'):
        for mobile in (False,True):
            suffix='-mobile' if mobile else ''
            assets={
                'hero':hero.render(profile,lang,mobile),
                'command':sections.command(lang,mobile),
                'fivem':sections.fivem(lang,mobile,sum(p['category']=='FiveM systems' for p in projects)),
                'technology':sections.technology(projects,lang,mobile),
                'languages':sections.languages(languages,lang,mobile),
                'practice':sections.practice(lang,mobile),
                'services':sections.services(profile,lang,mobile),
                'contact':sections.contact(lang,mobile),
            }
            for key,case in profile['caseStudies'].items():
                assets[f'feature-{key}']=project_views.feature(case,key,by_id[case['projectId']],lang,mobile)
                assets[f'architecture-{key}']=architecture.render(key,lang,mobile)
            for category,slug in category_names.items():
                assets[f'archive-{slug}']=project_views.archive_group(projects,category,lang,mobile)
            for name,svg in assets.items():
                path=OUT/f'{name}-{lang}{suffix}.svg'
                path.write_text(svg,encoding='utf-8')
                results.append(path)
                names.append(path.name)
        for item in sections.CHAPTERS:
            path=OUT/f'chapter-{item[0]}-{lang}.svg'
            path.write_text(sections.chapter(item,lang),encoding='utf-8')
            results.append(path);names.append(path.name)
    for path in OUT.glob('*.svg'):
        if path.name not in names:
            path.unlink()
    return results


if __name__=='__main__':
    print(f'Generated {len(generate())} bilingual SVG assets')
