"""Engineering overview, category maps, activity context and closing visuals."""
from __future__ import annotations

from typing import Any

from theme import (ACCENTS, CATEGORY_ACCENTS, BLUE, CYAN, PURPLE, VIOLET, GREEN, AMBER, RED,
                   TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, SURFACE_0, SURFACE_1,
                   BORDER_SUBTLE, ACTIVITY_LEVELS)
from portfolio.svg import document, text, lines, rect, panel, node, circle, rule, arrow, pill, wrap

CHAPTERS = [
    ('engineering','01','ENGINEERING','Инженерен профил','Domains and working style','Области и подход',BLUE),
    ('featured','02','SELECTED SYSTEMS','Основни системи','Evidence behind the work','Доказателства зад работата',PURPLE),
    ('archive','03','PROJECT ARCHIVE','Всички проекти','Complete verified inventory','Пълен проверен списък',AMBER),
    ('fivem','04','FIVEM ENGINEERING','FiveM инженерство','Client, server and persistence','Клиент, сървър и данни',AMBER),
    ('technology','05','TECHNOLOGY MAP','Технологии','Observed in projects','Потвърдени в проекти',CYAN),
    ('architecture','06','SYSTEM ARCHITECTURE','Архитектура','Boundaries and data flow','Граници и поток на данни',VIOLET),
    ('activity','07','DEVELOPMENT ACTIVITY','Активност','Public calendar and authored file touches','Публична активност и авторски промени',GREEN),
    ('practice','08','HOW I BUILD','Как разработвам','Decisions grounded in actual projects','Решения от реални проекти',BLUE),
    ('services','09','WORK WITH ME','Съвместна работа','Areas where experience is established','Области с установен опит',CYAN),
    ('contact','10','CONTACT','Контакт','A direct path to the next conversation','Начало на разговор',PURPLE),
]


def chapter(item: tuple, lang: str) -> str:
    key,num,en,bg,sub_en,sub_bg,accent=item
    name=bg if lang=='bg' else en
    sub=sub_bg if lang=='bg' else sub_en
    body=rect(27,23,4,68,accent,accent,2)
    body+=text(50,57,f'{num}  /  {name}',29,TEXT_PRIMARY,800,spacing=1)
    body+=text(51,83,sub,16,TEXT_SECONDARY)
    body+=rule(50,103,1154,103,accent,2)
    return document(1200,123,name,sub,body,accent,CYAN)


def command(lang: str, mobile: bool) -> str:
    w,h=(600,1170) if mobile else (1200,355)
    groups=[
        ('FOCUS' if lang=='en' else 'ФОКУС',['Developer tools','FiveM infrastructure','Web administration','macOS desktop'] if lang=='en' else ['Инструменти','FiveM инфраструктура','Уеб администриране','macOS приложение'],BLUE),
        ('LANGUAGES' if lang=='en' else 'ЕЗИЦИ',['Rust','Lua','TypeScript','Python'],CYAN),
        ('SYSTEMS' if lang=='en' else 'СИСТЕМИ',['Client / server','Data persistence','Access checks','Local tooling'] if lang=='en' else ['Клиент / сървър','Постоянни данни','Проверки на достъп','Локални инструменти'],PURPLE),
        ('PRACTICE' if lang=='en' else 'ПОДХОД',['Review before apply','Traceable changes','Tests and CI','Recovery paths'] if lang=='en' else ['Преглед преди промяна','Проследими промени','Тестове и CI','Връщане при нужда'],GREEN),
    ]
    body=text(30,45,'ENGINEERING COMMAND CENTER' if lang=='en' else 'ИНЖЕНЕРЕН КОМАНДЕН ЦЕНТЪР',21,CYAN,800,spacing=1)
    for i,(label,items,accent) in enumerate(groups):
        x=30 if mobile else 30+i*291
        y=70+i*265 if mobile else 70
        cw=540 if mobile else 270
        body+=panel(x,y,cw,245 if mobile else 277,accent,SURFACE_0,16)
        body+=text(x+17,y+42,f'{i+1:02d} / {label}',24 if mobile else 18,accent,800)
        body+=rule(x+17,y+60,x+cw-17,y+60,BORDER_SUBTLE)
        for j,item in enumerate(items):
            yy=y+102+j*40
            body+=circle(x+25,yy-6,4,accent)+text(x+40,yy,item,22 if mobile else 17,TEXT_PRIMARY,600)
    return document(w,h,'Engineering command center','Focus areas and engineering practice from verified work.',body,BLUE,CYAN)


def fivem(lang: str, mobile: bool, count: int) -> str:
    w,h=(600,820) if mobile else (1200,425)
    body=text(33,46,'FIVEM / CLIENT → SERVER → DATA' if lang=='en' else 'FIVEM / КЛИЕНТ → СЪРВЪР → ДАННИ',20,AMBER,800,spacing=1)
    body+=text(34,82,(f'{count} verified FiveM repository records' if lang=='en' else f'{count} потвърдени FiveM хранилища'),18,TEXT_SECONDARY)
    if mobile:
        body+=panel(28,112,544,630,AMBER,SURFACE_0,22)
        labels=['NUI / PLAYER','LUA SERVER','QBOX / OX','MYSQL / RECORDS'] if lang=='en' else ['NUI / ИГРАЧ','LUA СЪРВЪР','QBOX / OX','MYSQL / ЗАПИСИ']
        colors=[BLUE,AMBER,GREEN,CYAN]
        for i,(label,color) in enumerate(zip(labels,colors)):
            y=158+i*136
            body+=node(71,y,458,84,label,color,size=22)
            if i<3: body+=arrow(300,y+89,300,y+131,color)
        body+=text(50,718,'VERIFIED COMPONENT PATTERN' if lang=='en' else 'ПОТВЪРДЕН МОДЕЛ НА КОМПОНЕНТИ',15,TEXT_MUTED,700)
        body+=text(31,787,'Not every repository contains every component.' if lang=='en' else 'Не всеки проект съдържа всички компоненти.',17,TEXT_SECONDARY)
    else:
        body+=panel(29,112,1142,254,AMBER,SURFACE_0,22)
        labels=['NUI / PLAYER','LUA SERVER','QBOX / OX','MYSQL / RECORDS'] if lang=='en' else ['NUI / ИГРАЧ','LUA СЪРВЪР','QBOX / OX','MYSQL / ЗАПИСИ']
        colors=[BLUE,AMBER,GREEN,CYAN]
        for i,(label,color) in enumerate(zip(labels,colors)):
            x=55+i*277
            body+=node(x,207,230,92,label,color,size=19)
            if i<3: body+=arrow(x+235,253,x+273,253,color)
        body+=rule(324,133,324,348,RED,2,'6 8')
        body+=text(336,157,'CLIENT / SERVER BOUNDARY' if lang=='en' else 'ГРАНИЦА КЛИЕНТ / СЪРВЪР',14,RED,700)
        body+=text(33,403,'Pattern synthesized from documented resources; components vary by project.' if lang=='en' else 'Модел от документираните ресурси; компонентите варират по проект.',16,TEXT_SECONDARY)
    return document(w,h,'FiveM engineering topology','High-level pattern from verified resources; not a claim that all projects share every component.',body,AMBER,BLUE)


def technology(projects: list[dict[str,Any]], lang: str, mobile: bool) -> str:
    observed={t for p in projects for t in p['technologies']}
    choices=[
        ('SYSTEMS','СИСТЕМИ',['Rust','Python'],PURPLE),
        ('FIVEM','FIVEM',['Lua','Qbox','NUI'],AMBER),
        ('WEB','УЕБ',['TypeScript','Next.js','React','Vue'],BLUE),
        ('DATA','ДАННИ',['PostgreSQL','MySQL','Prisma'],CYAN),
        ('DESKTOP','НАСТОЛНИ',['Tauri 2'],VIOLET),
        ('AI + DELIVERY','AI + ДОСТАВКА',['OpenAI','Anthropic','GitHub Actions'],GREEN),
    ]
    groups=[(en if lang=='en' else bg,[t for t in names if t in observed],accent) for en,bg,names,accent in choices]
    groups=[g for g in groups if g[1]]
    w,h=(600,1050) if mobile else (1200,390)
    body=text(31,46,'OBSERVED TECHNOLOGY / PROJECT EVIDENCE' if lang=='en' else 'ТЕХНОЛОГИИ / ДОКАЗАТЕЛСТВА ОТ ПРОЕКТИ',20,CYAN,800,spacing=1)
    for i,(label,items,accent) in enumerate(groups):
        x=30 if mobile else 30+(i%3)*390
        y=75+i*157 if mobile else 76+(i//3)*135
        cw=540 if mobile else 370; ch=140 if mobile else 119
        body+=panel(x,y,cw,ch,accent,SURFACE_0,14)
        body+=text(x+16,y+35,label,24 if mobile else 18,accent,800,spacing=1)
        if mobile:
            for j,item in enumerate(items):
                xx=x+20+(j%2)*255; yy=y+79+(j//2)*35
                body+=circle(xx+4,yy-6,3,accent)+text(xx+17,yy,item,22,TEXT_PRIMARY,600)
        else:
            for j,item in enumerate(items):
                xx=x+18+(j%2)*170; yy=y+72+(j//2)*28
                body+=circle(xx+5,yy-6,3,accent)+text(xx+18,yy,item,17,TEXT_PRIMARY,600)
    note='Only technologies listed in verified project records.' if lang=='en' else 'Само технологии от проверените проектни записи.'
    body+=text(31,h-22,note,16,TEXT_MUTED)
    return document(w,h,'Technology map',note,body,CYAN,PURPLE)


def languages(snapshot: dict[str,Any], lang: str, mobile: bool) -> str:
    values=list(snapshot['languages'].items())[:7]
    largest=max(n for _,n in values)
    w,h=(600,630) if mobile else (1200,405)
    body=text(31,46,'AUTHORED FILE TOUCHES' if lang=='en' else 'ФАЙЛОВЕ В АВТОРСКИ COMMIT-И',20,PURPLE,800,spacing=1)
    body+=text(31,78,f"{snapshot['commitsAnalyzed']} commits  /  {snapshot['repositoriesAnalyzed']} repositories  /  {snapshot['auditDate']}",16,TEXT_SECONDARY)
    palette={'Lua':AMBER,'TypeScript':BLUE,'JavaScript':BLUE,'CSS':CYAN,'HTML':CYAN,'SQL':VIOLET,'Python':PURPLE,'Rust':PURPLE,'Swift':VIOLET}
    for i,(name,n) in enumerate(values):
        accent=palette.get(name,CYAN)
        if mobile:
            y=120+i*66
            body+=text(31,y,name.upper(),19,TEXT_PRIMARY,700)
            body+=rect(31,y+13,450,18,SURFACE_1,SURFACE_1,5)
            body+=rect(31,y+13,max(4,round(450*n/largest)),18,accent,accent,5)
            body+=text(555,y+29,n,19,accent,700,'end')
        else:
            y=115+i*36
            body+=text(31,y+15,name.upper(),17,TEXT_PRIMARY,700)
            body+=rect(210,y,840,18,SURFACE_1,SURFACE_1,5)
            body+=rect(210,y,max(4,round(840*n/largest)),18,accent,accent,5)
            body+=text(1148,y+16,n,18,accent,700,'end')
    note='Source-file touches, not proficiency or ownership.' if lang=='en' else 'Променени файлове, не оценка на умения или собственост.'
    body+=text(31,h-25,note,16,TEXT_MUTED)
    return document(w,h,'Authored language activity',snapshot['measurement'],body,PURPLE,CYAN)


def practice(lang: str, mobile: bool) -> str:
    groups=[
        ('SECURITY','СИГУРНОСТ',['Redacted AI context','Server access checks','Keychain credentials'],['Редактиран AI контекст','Сървърни проверки','Ключове в Keychain'],RED),
        ('PERFORMANCE','ПРОИЗВОДИТЕЛНОСТ',['Bounded scan work','Avoid needless polling','Measure before tuning'],['Ограничена работа','Без излишно обхождане','Измерване преди оптимизация'],CYAN),
        ('ARCHITECTURE','АРХИТЕКТУРА',['Clear trust boundaries','Traceable data flow','Modular systems'],['Ясни граници на доверие','Проследим поток на данни','Модулни системи'],PURPLE),
        ('DELIVERY','ДОСТАВЯНЕ',['Reviewable diffs','Tests and CI','Recovery paths'],['Прегледни diff-ове','Тестове и CI','Възстановяване'],GREEN),
    ]
    w,h=(600,1140) if mobile else (1200,360)
    body=text(30,45,'ENGINEERING PRACTICE' if lang=='en' else 'ИНЖЕНЕРЕН ПОДХОД',20,BLUE,800,spacing=1)
    for i,(en,bg,en_items,bg_items,accent) in enumerate(groups):
        label=en if lang=='en' else bg; items=en_items if lang=='en' else bg_items
        x=30 if mobile else 30+i*291; y=72+i*262 if mobile else 72
        cw=540 if mobile else 270
        body+=panel(x,y,cw,245 if mobile else 266,accent,SURFACE_0,15)
        body+=text(x+17,y+44,f'{i+1:02d} / {label}',24 if mobile else 17,accent,800)
        for j,item in enumerate(items):
            yy=y+98+j*49
            body+=rule(x+17,yy-7,x+31,yy-7,accent,2)
            body+=text(x+39,yy,item,22 if mobile else (15 if len(item)>23 else 17),TEXT_PRIMARY,500)
    return document(w,h,'Engineering practice','Project-specific examples of security, performance, architecture and delivery decisions.',body,BLUE,CYAN)


def services(profile: dict, lang: str, mobile: bool) -> str:
    items=profile['copy'][lang]['services']; w,h=(600,740) if mobile else (1200,245)
    body=text(30,45,'SYSTEMS I CAN HELP BUILD' if lang=='en' else 'СИСТЕМИ, ПО КОИТО МОГА ДА РАБОТЯ',19,CYAN,800,spacing=1)
    accents=[PURPLE,AMBER,BLUE,GREEN]
    for i,item in enumerate(items):
        x=30 if mobile else 30+i*291; y=78+i*150 if mobile else 78
        cw=540 if mobile else 270
        body+=panel(x,y,cw,130,accents[i],SURFACE_0,16)
        body+=text(x+18,y+46,f'{i+1:02d}',22,accents[i],800)
        for j,row in enumerate(wrap(item,32 if mobile else 22)):
            body+=text(x+70 if mobile else x+18,y+52+j*30 if mobile else y+88+j*30,row,24 if mobile else 19,TEXT_PRIMARY,700)
    note='Scope and availability are discussed per project.' if lang=='en' else 'Обхватът и възможностите се уточняват за всеки проект.'
    body+=text(31,h-23,note,16,TEXT_MUTED)
    return document(w,h,'Work areas',note,body,CYAN,BLUE)


def contact(lang: str, mobile: bool) -> str:
    w,h=(600,430) if mobile else (1200,300)
    body=f'<ellipse cx="{w-100}" cy="{h//2}" rx="320" ry="180" fill="url(#aura)"/>'
    body+=text(38,58,'10 / CONTACT' if lang=='en' else '10 / КОНТАКТ',18,PURPLE,800,spacing=2)
    title='BUILD SOMETHING SERIOUS.' if lang=='en' else 'ДА ИЗГРАДИМ НЕЩО СЪЩЕСТВЕНО.'
    title_rows=wrap(title,24 if mobile else 44)
    body+=lines(38,124,title_rows,44 if mobile else 58,TEXT_PRIMARY,800,53 if mobile else 65)
    offset=(len(title_rows)-1)*(53 if mobile else 65)
    body+=text(40,184+offset,'Tell me what the system needs to do.' if lang=='en' else 'Разкажете ми какво трябва да прави системата.',21,TEXT_SECONDARY)
    body+=panel(38,227+offset,524 if mobile else 370,75,PURPLE,SURFACE_0,14)
    body+=text(62,274+offset,'GITHUB  /  @GOPETO222',23,CYAN,800)
    body+=text(40,h-22,'PUBLIC CONTACT CHANNEL' if lang=='en' else 'ПУБЛИЧЕН КАНАЛ ЗА ВРЪЗКА',15,TEXT_MUTED,700,spacing=1)
    return document(w,h,'Contact Georgi Kanchev','Contact on GitHub at github.com/gopeto222.',body,PURPLE,CYAN)
