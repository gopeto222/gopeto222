"""Render clean, matching EN/BG Markdown from public portfolio data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]


def picture(name: str, lang: str, alt: str, directory: str = 'assets/generated') -> str:
    return (f'<picture><source media="(max-width: 650px)" srcset="{directory}/{name}-{lang}-mobile.svg">'
            f'<img src="{directory}/{name}-{lang}.svg" alt="{alt}" width="100%"></picture>')


def chapter(key: str, lang: str, alt: str) -> str:
    return f'<a id="{key}"></a>\n<img src="assets/generated/chapter-{key}-{lang}.svg" alt="{alt}" width="100%">'


def case_block(key: str, case: dict, project: dict, lang: str) -> str:
    c=case[lang]
    labels={
        'en':('Problem','System','My contribution','Engineering decision','Status','Verified system diagram; no product screenshot is implied.'),
        'bg':('Проблем','Система','Моят принос','Инженерно решение','Статус','Проверена системна схема; не е кадър от приложението.'),
    }[lang]
    tech=' · '.join(project['technologies'])
    stack_label='Технологии' if lang=='bg' else 'Stack'
    image=picture(f'feature-{key}',lang,('System diagram for ' if lang=='en' else 'Системна схема за ')+c['title'])
    return (f'### {c["title"]}\n\n{image}\n\n<sub>{labels[5]}</sub>\n\n'
            f'- **{labels[0]}:** {c["problem"]}\n'
            f'- **{labels[1]}:** {c["build"]}\n'
            f'- **{labels[2]}:** {c["contribution"]}\n'
            f'- **{labels[3]}:** {c["decision"]}\n'
            f'- **{labels[4]}:** {c["status"]}\n'
            f'- **{stack_label}:** {tech}\n')


def render(lang: str, profile: dict, inventory: dict) -> str:
    projects=inventory['projects']; by_id={p['id']:p for p in projects}
    other='README.bg.md' if lang=='en' else 'README.md'
    switch='Switch to Bulgarian' if lang=='en' else 'Към английската версия'
    copy=profile['copy'][lang]
    labels={
        'en':{'engineering':'Engineering','featured':'Selected systems','archive':'Project archive','fivem':'FiveM engineering','technology':'Technology','architecture':'Architecture','activity':'Activity','practice':'How I build','services':'Work with me','contact':'Contact'},
        'bg':{'engineering':'Инженерен профил','featured':'Основни системи','archive':'Всички проекти','fivem':'FiveM инженерство','technology':'Технологии','architecture':'Архитектура','activity':'Активност','practice':'Как разработвам','services':'Съвместна работа','contact':'Контакт'},
    }[lang]
    parts=['<!-- Generated from data/profile.json and data/projects.json by scripts/build_readmes.py. -->']
    parts.append(f'<a href="{other}" title="{switch}">{picture("hero",lang,switch+("; AstroByte engineering portfolio" if lang=="en" else "; инженерно портфолио AstroByte"))}</a>')
    parts.append('<p align="center">'+' · '.join(f'<a href="#{key}">{title}</a>' for key,title in labels.items() if key in ('featured','archive','technology','activity','contact'))+'</p>')
    parts.append(copy['intro'])
    parts.append(chapter('engineering',lang,labels['engineering']))
    parts.append(picture('command',lang,('Dashboard of verified domains and engineering practice' if lang=='en' else 'Табло с проверени области и инженерни практики')))
    parts.append(chapter('featured',lang,labels['featured']))
    parts.append(('Selected work is described from repository evidence. Private sources remain private.' if lang=='en' else 'Подбраните проекти са описани според проверените хранилища. Частният код остава частен.'))
    for key,case in profile['caseStudies'].items():
        parts.append(case_block(key,case,by_id[case['projectId']],lang))
    parts.append(chapter('archive',lang,labels['archive']))
    summary=inventory['auditSummary']
    parts.append((f"{summary['includedRepositories']} verified records from {summary['accessibleRepositories']} accessible repositories. {summary['excludedWithoutAuthorshipEvidence']} organization repositories were excluded because authored work was not established. Personal ownership, organization contributions and collaborative work are labeled separately. [Audit method](docs/discovery.md)." if lang=='en' else
                  f"{summary['includedRepositories']} проверени проекта от {summary['accessibleRepositories']} достъпни хранилища. {summary['excludedWithoutAuthorshipEvidence']} организационни хранилища са изключени, защото не е установен авторски принос. Личните, организационните и съвместните проекти са обозначени отделно. [Метод на одита](docs/discovery.md)."))
    for slug,title_en,title_bg in [('tools','Developer tools','Инструменти'),('operations','Engineering operations','Инженерни процеси'),('fivem','FiveM systems','FiveM системи'),('web','Web systems','Уеб системи')]:
        title=title_en if lang=='en' else title_bg
        parts.append(f'#### {title}\n\n'+picture(f'archive-{slug}',lang,title+(' project inventory with role and availability' if lang=='en' else ': проекти с роля и достъпност')))
    parts.append(('[Public source: this profile repository](https://github.com/gopeto222/gopeto222).' if lang=='en' else '[Публичен код: хранилището на този профил](https://github.com/gopeto222/gopeto222).'))
    parts.append(chapter('fivem',lang,labels['fivem']))
    parts.append(picture('fivem',lang,'FiveM client, server and persistence topology' if lang=='en' else 'FiveM схема на клиент, сървър и постоянни данни'))
    parts.append(('This is a pattern across documented resources, not a claim that every resource uses every component. The DMV and registry cases above provide concrete examples.' if lang=='en' else 'Това е модел от документираните ресурси, а не твърдение, че всеки проект използва всички компоненти. DMV и регистърът по-горе са конкретни примери.'))
    parts.append(chapter('technology',lang,labels['technology']))
    parts.append(picture('technology',lang,'Technology groups from verified project records' if lang=='en' else 'Групи технологии от проверените проекти'))
    parts.append(chapter('architecture',lang,labels['architecture']))
    parts.append(('The diagrams show documented components and important boundaries. Optional integrations are labeled.' if lang=='en' else 'Схемите показват документирани компоненти и важни граници. Незадължителните интеграции са обозначени.'))
    for key in ('codeguard','rules','dmv'):
        title=profile['caseStudies'][key][lang]['title']
        parts.append(f'#### {title}\n\n'+picture(f'architecture-{key}',lang,title+(' architecture diagram' if lang=='en' else ': архитектурна схема')))
    extra='Additional architecture maps' if lang=='en' else 'Още архитектурни схеми'
    details=f'<details><summary>{extra}</summary>\n\n'
    for key in ('registry','collaboration'):
        title=profile['caseStudies'][key][lang]['title']
        details+=f'#### {title}\n\n'+picture(f'architecture-{key}',lang,title+(' architecture diagram' if lang=='en' else ': архитектурна схема'))+'\n\n'
    parts.append(details+'</details>')
    parts.append(chapter('activity',lang,labels['activity']))
    parts.append(picture('activity',lang,'Public GitHub contribution calendar and streaks' if lang=='en' else 'Публичен календар на GitHub приносите и поредици',directory='assets/metrics'))
    parts.append(('The card is generated from GitHub’s public contribution calendar. Counts are not hours, code ownership or project impact. [Metric method](docs/metrics.md).' if lang=='en' else 'Картата се генерира от публичния календар на GitHub. Броят не измерва часове, собственост върху код или влияние на проекта. [Метод](docs/metrics.md).'))
    parts.append(picture('languages',lang,'Source-file touches in authored non-merge commits' if lang=='en' else 'Променени файлове в авторски commit-и без merge'))
    parts.append(('Language activity is a dated, contribution-aware snapshot of source-file touches. It does not measure proficiency. [Audit limits](docs/discovery.md).' if lang=='en' else 'Езиковата активност е датирана извадка от промени по файлове в авторски commit-и. Тя не измерва умения. [Ограничения](docs/discovery.md).'))
    parts.append(chapter('practice',lang,labels['practice']))
    parts.append(picture('practice',lang,'Engineering decisions for security, performance, architecture and delivery' if lang=='en' else 'Инженерни решения за сигурност, производителност, архитектура и доставка'))
    parts.append(('These are examples from specific projects, not a claim that every repository has the same safeguards.' if lang=='en' else 'Това са примери от конкретни проекти, а не твърдение, че всяко хранилище има еднакви защити.'))
    parts.append(chapter('services',lang,labels['services']))
    parts.append(picture('services',lang,'Work areas supported by verified experience' if lang=='en' else 'Области на работа с потвърден опит'))
    parts.append(chapter('contact',lang,labels['contact']))
    parts.append(copy['contact'])
    parts.append(f'<a href="{profile["contactUrl"]}" title="'+('Contact Georgi on GitHub' if lang=='en' else 'Свържете се с Георги в GitHub')+'">'+picture('contact',lang,('Contact @gopeto222 on GitHub' if lang=='en' else 'Контакт с @gopeto222 в GitHub'))+'</a>')
    name='Георги Канчев' if lang=='bg' else 'Georgi Kanchev'
    parts.append(f'<sub>AstroByte Development · {name} · <a href="{other}">{switch}</a></sub>')
    return '\n\n'.join(parts)+'\n'


def generate() -> list[Path]:
    profile=json.loads((ROOT/'data/profile.json').read_text(encoding='utf-8'))
    inventory=json.loads((ROOT/'data/projects.json').read_text(encoding='utf-8'))
    paths=[]
    for lang,name in [('en','README.md'),('bg','README.bg.md')]:
        path=ROOT/name
        path.write_text(render(lang,profile,inventory),encoding='utf-8')
        paths.append(path)
    return paths
