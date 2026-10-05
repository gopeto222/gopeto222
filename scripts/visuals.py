"""Render the public portfolio's deterministic, bilingual SVG design system."""
from __future__ import annotations

import json
import math
from html import escape
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'generated'
BG = '#0b111b'
PANEL = '#131e2b'
PANEL2 = '#172536'
LINE = '#365369'
CYAN = '#68e2e6'
BLUE = '#79a9ff'
WHITE = '#eef6fc'
MUTED = '#a7bfce'
SOFT = '#7294a9'
FONT = 'Arial,Helvetica,sans-serif'


def text(x: int, y: int, value: str, size: int = 20, color: str = WHITE, weight: int = 400, anchor: str = 'start', spacing: int = 0) -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{spacing}">{escape(str(value))}</text>'


def rect(x: int, y: int, w: int, h: int, fill: str = PANEL, stroke: str = LINE, radius: int = 14) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def line(x1: int, y1: int, x2: int, y2: int, color: str = LINE, width: int = 2) -> str:
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"/>'


def svg(w: int, h: int, title: str, body: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)} — AstroByte Development portfolio visual.</desc><defs><linearGradient id="shell" x2="1" y2="1"><stop stop-color="#101c2b"/><stop offset="0.65" stop-color="#0b111b"/><stop offset="1" stop-color="#102a34"/></linearGradient><radialGradient id="glow"><stop stop-color="#1d6170" stop-opacity=".65"/><stop offset="1" stop-color="#1d6170" stop-opacity="0"/></radialGradient></defs><rect width="{w}" height="{h}" rx="24" fill="url(#shell)"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="23" fill="none" stroke="#345065"/>{body}</svg>\n'


def grid(w: int, h: int, step: int = 40) -> str:
    return ''.join(line(x, 0, x, h, '#1b2b3a', 1) for x in range(0, w, step)) + ''.join(line(0, y, w, y, '#1b2b3a', 1) for y in range(0, h, step))


def chip(x: int, y: int, label: str, width: int) -> str:
    return rect(x, y, width, 32, '#17303a', '#3c7f8b', 9) + text(x + width//2, y + 22, label, 13, CYAN, 700, 'middle', 1)


def hero(lang: str, mobile: bool) -> str:
    bg = lang == 'bg'; w, h = (600, 760) if mobile else (1200, 530)
    b = grid(w,h,40) + f'<ellipse cx="{w-105}" cy="150" rx="270" ry="230" fill="url(#glow)"/>'
    b += text(38, 53, 'ASTROBYTE / DEVELOPMENT', 17, CYAN, 700, spacing=3)
    if mobile:
        b += text(38, 151, 'GEORGI', 77, WHITE, 800, spacing=2)
        b += text(38, 214, 'KANCHEV', 66, WHITE, 800, spacing=1)
        b += text(40, 260, 'SOFTWARE ENGINEER  /  PRODUCT BUILDER' if not bg else 'СОФТУЕРЕН ИНЖЕНЕР  /  СЪЗДАТЕЛ', 17, CYAN, 700)
        b += rect(34, 310, 532, 267, '#111d2a', '#4a7080', 20)
        b += text(56, 347, 'ENGINEERING / LIVE SYSTEMS' if not bg else 'ИНЖЕНЕРСТВО / РЕАЛНИ СИСТЕМИ', 15, MUTED, 700, spacing=1)
        hero_signals = ['RUST CORE', 'FIVEM SERVER', 'WEB PLATFORM', 'LOCAL AI'] if not bg else ['RUST ЯДРО', 'FIVEM СЪРВЪР', 'УЕБ ПЛАТФОРМА', 'ЛОКАЛЕН AI']
        for i, label in enumerate(hero_signals):
            yy=389+i*43
            b += '<circle cx="63" cy="%d" r="5" fill="%s"/>'%(yy-6,CYAN)
            b += line(67, yy-6, 135, yy-6, CYAN, 2)
            b += text(150, yy, label, 20, WHITE, 700)
        b += text(38, 631, 'Builds tools, server systems and web products.' if not bg else 'Създава инструменти, сървърни системи и уеб продукти.', 20, WHITE)
        b += text(38, 676, 'SECURITY  /  ARCHITECTURE  /  SHIPPING' if not bg else 'СИГУРНОСТ  /  АРХИТЕКТУРА  /  ДОСТАВЯНЕ', 15, SOFT, 700, spacing=1)
        b += line(38, 704, 562, 704, LINE)
        b += text(38, 735, '01 — PROFILE / 2026', 14, CYAN, 700, spacing=2)
    else:
        b += text(53, 172, 'GEORGI', 105, WHITE, 800, spacing=2)
        b += text(55, 243, 'KANCHEV', 76, WHITE, 800, spacing=2)
        b += text(57, 290, 'SOFTWARE ENGINEER  /  PRODUCT BUILDER' if not bg else 'СОФТУЕРЕН ИНЖЕНЕР  /  СЪЗДАТЕЛ', 22, CYAN, 700, spacing=1)
        b += text(57, 353, 'Building developer tools, server systems and web products.' if not bg else 'Инструменти, сървърни системи и уеб продукти.', 23, WHITE)
        b += chip(57, 398, 'RUST', 95)+chip(165, 398, 'FIVEM', 105)+chip(283, 398, 'FULL-STACK', 147)+chip(443, 398, 'MACOS', 105)
        b += rect(760, 92, 390, 346, '#111f2d', '#4a7080', 20)
        b += text(788, 130, 'SYSTEM / SIGNAL', 16, CYAN, 700, spacing=2)
        b += line(790, 151, 1120, 151, LINE)
        for xx,yy in ((855,202),(1055,202),(855,366),(1055,366)):
            b += line(955,282,xx,yy,CYAN,2)
        b += '<circle cx="955" cy="282" r="58" fill="#17404c" stroke="#68e2e6" stroke-width="2"/>'
        b += text(955,276,'ASTRO',20,WHITE,800,'middle')+text(955,301,'BYTE',20,CYAN,800,'middle')
        for xx,yy,label,detail in [(785,172,'CODEGUARD','SCAN / REVIEW'),(985,172,'FIVEM','SERVER / DATA'),(785,336,'WEB','ADMIN / AUTH'),(985,336,'DELIVERY','TEST / SHIP')]:
            b += rect(xx,yy,140,61,'#183544','#4c8291',10)
            b += text(xx+70,yy+27,label,15,WHITE,700,'middle')
            b += text(xx+70,yy+48,detail,10,MUTED,700,'middle')
        b += text(55, 493, '01 / ENGINEERING PORTFOLIO' if not bg else '01 / ИНЖЕНЕРНО ПОРТФОЛИО', 16, SOFT, 700, spacing=2)
    return svg(w,h,'Georgi Kanchev — software engineering portfolio',b)


def command(lang: str, mobile: bool) -> str:
    bg=lang=='bg'; w,h=(600,710) if mobile else (1200,360)
    b=text(32,45,'02 / DEVELOPER COMMAND CENTER' if not bg else '02 / ЦЕНТЪР ЗА РАЗРАБОТКА',18,CYAN,700,spacing=2)
    cols=[('CURRENT FOCUS' if not bg else 'ТЕКУЩ ФОКУС',['Developer tools','FiveM infrastructure','Full-stack systems','macOS desktop'] if not bg else ['Инструменти','FiveM инфраструктура','Уеб системи','macOS приложение']),('CORE LANGUAGES' if not bg else 'ЕЗИЦИ',['Rust','Lua','TypeScript','Python']),('ENGINEERING' if not bg else 'ИНЖЕНЕРСТВО',['Security','Architecture','Testing','Automation'] if not bg else ['Сигурност','Архитектура','Тестове','Автоматизация']),('STATUS' if not bg else 'СТАТУС',['Building','Validating','Shipping','Improving'] if not bg else ['Разработка','Проверка','Доставка','Подобряване'])]
    for i,(heading,items) in enumerate(cols):
        x=30+(i%2)*274 if mobile else 30+i*291
        y=66+(i//2)*314 if mobile else 67
        cw=264 if mobile else 270
        b+=rect(x,y,cw,280,'#121f2c','#35576b',14)
        b+=text(x+20,y+37,f'0{i+1} / {heading}',16,CYAN,700)
        b+=line(x+20,y+53,x+cw-20,y+53,LINE)
        for j,item in enumerate(items):
            yy=y+94+j*42
            b+=f'<circle cx="{x+27}" cy="{yy-7}" r="4" fill="{CYAN}"/>'
            b+=text(x+42,yy,item,17,WHITE,600)
    return svg(w,h,'Developer command center' if not bg else 'Център за разработка',b)

FEATURES={
'codeguard':('CODEGUARD','LOCAL CODE INTELLIGENCE','Rust scanner → findings → AI proposal → review',['STATIC ANALYSIS','SECURITY SIGNAL','AI FIX REVIEW','SAFE REVERT'],['RUST','TAURI','REACT','OPENAI / ANTHROPIC']),
'rules':('RULES PLATFORM','WEB ADMINISTRATION','Public rules → Discord OAuth → editorial workflow',['DRAFT / PUBLISH','VERSION HISTORY','ACCESS CONTROL','AUDIT LOG'],['NEXT.JS','TYPESCRIPT','POSTGRESQL','PRISMA']),
'dmv':('DMV SYSTEM','FIVEM VEHICLE WORKFLOW','NUI tablet → Lua server → Qbox → MySQL',['REGISTRATION','PLATE HISTORY','QR VERIFICATION','LOCALIZATION'],['LUA','QBOX','OX LIB','MYSQL']),
'registry':('BUSINESS REGISTRY','FIVEM RECORD SYSTEM','Tablet → server validation → records → log',['BUSINESS RECORDS','DOCUMENTS','SERVER VALIDATION','ACTIVITY LOG'],['LUA','QBOX','NUI','MYSQL']),
'collaboration':('SERVER INFRASTRUCTURE','COLLABORATIVE FIVEM WORK','Authored changes in a shared private repository',['RESOURCE INTEGRATION','DATABASE CHANGES','TEAM REPOSITORY','SHARED OWNERSHIP'],['LUA','TYPESCRIPT','VUE','GIT']),
}


def product_preview(key: str, x: int, y: int, w: int, h: int, bg: bool) -> str:
    """Distinct miniature product views; labels describe architecture, not live metrics."""
    b = rect(x, y, w, h, '#10202e', '#456f83', 14)
    small = 13 if w < 400 else 15
    b += text(x+17, y+30, {
        'codeguard':'СКЕНЕР / НАХОДКИ' if bg else 'SCANNER / FINDINGS',
        'rules':'ЧЕРНОВА / ПУБЛИКУВАНЕ' if bg else 'DRAFT / PUBLISH',
        'dmv':'РЕГИСТРАЦИЯ / ПРЕВОЗНО СРЕДСТВО' if bg else 'REGISTRATION / VEHICLE',
        'registry':'ЗАПИСИ / ДОКУМЕНТИ' if bg else 'RECORDS / DOCUMENTS',
        'collaboration':'СПОДЕЛЕНА ИНФРАСТРУКТУРА' if bg else 'SHARED INFRASTRUCTURE',
    }[key], small, CYAN, 700, spacing=1)
    if key == 'codeguard':
        for i, length in enumerate((.78,.55,.86,.45,.68)):
            b += rect(x+20,y+52+i*23,round((w*.43)*length),8,'#42677b','#42677b',3)
        b += line(x+w//2,y+54,x+w//2,y+h-22,CYAN,2)
        b += text(x+w//2+20,y+81,'TRACE',15,WHITE,700)
        b += text(x+w//2+20,y+116,'→ REVIEW',15,CYAN,700)
        if h>200:b+=text(x+w//2+20,y+151,'→ APPLY',15,WHITE,700)
    elif key == 'rules':
        labels=['DRAFT','REVIEW','PUBLIC'] if not bg else ['ЧЕРНОВА','ПРЕГЛЕД','ПУБЛИЧНО']
        for i,label in enumerate(labels):
            xx=x+16+i*(w-32)//3;ww=(w-50)//3
            b+=rect(xx,y+68,ww,75,'#183445','#4b7b91',9)
            b+=text(xx+ww//2,y+110,label,13 if w<400 else 15,WHITE,700,'middle')
        b+=text(x+w//2,y+h-20,'DISCORD AUTH  /  AUDIT',12,MUTED,700,'middle')
    elif key == 'dmv':
        b+=rect(x+18,y+58,w-36,83,'#173444','#5a92a2',10)
        b+=text(x+35,y+88,'VIN  →  PLATE  →  RECORD' if not bg else 'VIN  →  НОМЕР  →  ЗАПИС',14,WHITE,700)
        b+=line(x+35,y+104,x+w-35,y+104,CYAN,2)
        b+=text(x+35,y+129,'QBOX  /  LUA  /  MYSQL',14,CYAN,700)
        if h>200:b+=text(x+20,y+h-18,'REGISTRATION HISTORY' if not bg else 'ИСТОРИЯ НА РЕГИСТРАЦИИТЕ',12,MUTED,700)
    elif key == 'registry':
        labels=['BUSINESS','DOCUMENTS','AUDIT'] if not bg else ['БИЗНЕС','ДОКУМЕНТИ','ЖУРНАЛ']
        for i,label in enumerate(labels):
            yy=y+58+i*43
            b+=rect(x+18,yy,w-36,34,'#183445','#3b6679',7)
            b+=text(x+34,yy+23,label,14,WHITE,700)
            b+=text(x+w-34,yy+23,'✓',16,CYAN,700,'end')
    else:
        labels=['CLIENT','SERVER','DATA'] if not bg else ['КЛИЕНТ','СЪРВЪР','ДАННИ']
        centers=[x+w//6,x+w//2,x+w*5//6]
        b+=line(centers[0],y+105,centers[2],y+105,CYAN,2)
        for center,label in zip(centers,labels):
            b+=f'<circle cx="{center}" cy="{y+105}" r="19" fill="#1e4758" stroke="{CYAN}" stroke-width="2"/>'
            b+=text(center,y+149,label,12,WHITE,700,'middle')
        if h>200:b+=text(x+w//2,y+h-18,'SHARED REPOSITORY' if not bg else 'СПОДЕЛЕНО ХРАНИЛИЩЕ',12,MUTED,700,'middle')
    return b

def feature(key: str, lang: str, mobile: bool) -> str:
    name,subtitle,flow,signals,tech=FEATURES[key]; bg=lang=='bg'
    if bg:
        translations={
            'codeguard':('ЛОКАЛЕН АНАЛИЗ НА КОД','Rust скенер → находки → AI предложение → преглед',['СТАТИЧЕН АНАЛИЗ','СИГНАЛИ ЗА СИГУРНОСТ','ПРЕГЛЕД НА AI ПОПРАВКИ','ЗАЩИТЕНО ВРЪЩАНЕ']),
            'rules':('УЕБ АДМИНИСТРИРАНЕ','Правила → Discord вход → редактор',['ЧЕРНОВА / ПУБЛИКУВАНЕ','ИСТОРИЯ НА ВЕРСИИТЕ','КОНТРОЛ НА ДОСТЪПА','ОДИТЕН ЖУРНАЛ']),
            'dmv':('FIVEM РЕГИСТРАЦИЯ','NUI таблет → Lua сървър → Qbox → MySQL',['РЕГИСТРАЦИЯ','ИСТОРИЯ НА НОМЕРА','QR ПРОВЕРКА','ЛОКАЛИЗАЦИЯ']),
            'registry':('FIVEM РЕГИСТЪР','Таблет → валидация → записи → журнал',['БИЗНЕС ЗАПИСИ','ДОКУМЕНТИ','СЪРВЪРНА ВАЛИДАЦИЯ','ЖУРНАЛ']),
            'collaboration':('СЪВМЕСТНА FIVEM РАБОТА','Авторски промени в споделено частно хранилище',['ИНТЕГРАЦИЯ','ПРОМЕНИ ПО ДАННИТЕ','ЕКИПНО ХРАНИЛИЩЕ','СПОДЕЛЕНА РАБОТА']),
        }
        subtitle,flow,signals=translations[key]
    w,h=(600,900) if mobile else (1200,470)
    b=grid(w,h,44)
    b+=text(34,45,('ОСНОВЕН / ' if bg else 'FEATURED / ')+key.upper(),16,CYAN,700,spacing=2)
    b+=text(34,105,name,47 if mobile else 61,WHITE,800,spacing=1)
    b+=text(36,142,subtitle,19,BLUE,700,spacing=1)
    if mobile:
        b+=rect(30,169,540,356,'#101d2b','#456477',16)
        b+=text(49,202,'SYSTEM / '+('SIGNALS' if not bg else 'СИГНАЛИ'),15,MUTED,700,spacing=2)
        for i,s in enumerate(signals):
            y=233+i*73
            b+=rect(49,y,502,59,'#172a39','#365d70',10)
            b+=text(68,y+36,s,18,WHITE,700)
            b+=text(527,y+36,f'0{i+1}',16,CYAN,700,'end')
        b+=product_preview(key,30,546,540,208,bg)
        b+=text(33,792,flow,16,MUTED)
        b+=text(33,832,' / '.join(tech[:3]),17,CYAN,700)
        b+=text(33,867,'PRIVATE SOURCE  ·  VERIFIED WORK' if not bg else 'ЧАСТЕН КОД  ·  ПРОВЕРЕН ПРИНОС',13,SOFT,700,spacing=1)
    else:
        b+=rect(34,178,730,242,'#101d2b','#456477',16)
        b+=text(57,212,'ПРОДУКТ / СИСТЕМА' if bg else 'PRODUCT / SYSTEM VIEW',15,MUTED,700,spacing=2)
        for i,s in enumerate(signals):
            x=55+(i%2)*345; y=240+(i//2)*79
            b+=rect(x,y,323,60,'#172a39','#365d70',10)
            b+=text(x+17,y+36,s,18,WHITE,700)
        b+=product_preview(key,789,178,376,242,bg)
        b+=text(35,451,' / '.join(tech),16,CYAN,700)
    return svg(w,h,name+' project dashboard',b)


def matrix(projects: list[dict[str,Any]], lang: str, mobile: bool) -> str:
    bg=lang=='bg'; w=600 if mobile else 1200
    ordered=sorted(projects,key=lambda p:(p['category'],p['name']))
    rows=math.ceil(len(ordered)/(1 if mobile else 2)); h=110+rows*(91 if mobile else 92)
    b=text(30,43,'04 / ALL VERIFIED PROJECTS' if not bg else '04 / ВСИЧКИ ПОТВЪРДЕНИ ПРОЕКТИ',19,CYAN,700,spacing=2)
    b+=text(30,72,f'{len(ordered)} PROJECT RECORDS / OWNER OR AUTHORED CONTRIBUTION' if not bg else f'{len(ordered)} ПРОЕКТА / СОБСТВЕНОСТ ИЛИ АВТОРСКИ ПРИНОС',14,MUTED,700)
    bg_names={'AstroByte CodeGuard':'AstroByte CodeGuard','Engineering profile':'Инженерен профил','Development documentation':'Документация за разработка','Armor plate resource':'Ресурс за бронеплочи','Business registry':'Бизнес регистър','Collaborative FiveM server infrastructure':'Съвместна FiveM инфраструктура','Crime system resource':'Криминална система','DMV tablet system':'DMV таблет','Document resource':'Система за документи','Fishing resource':'Ресурс за риболов','FiveM server resource collection':'Колекция FiveM ресурси','Game environment integration collection':'Интеграции на игрова среда','Pawnshop resource':'Заложна къща','Police boat resource':'Полицейска лодка','Police equipment resource':'Полицейско оборудване','Small robberies resource':'Малки обири','Traffic resource':'Трафик система','Vehicle identification resource':'Идентификация на превозни средства','Voltage system resource':'Електрическа система','Rules administration platform':'Платформа за правила'}
    bg_categories={'Developer tools':'Инструменти','Engineering operations':'Инженерни процеси','FiveM systems':'FiveM системи','Web systems':'Уеб системи'}
    for i,p in enumerate(ordered):
        col=i%2 if not mobile else 0; row=i//2 if not mobile else i
        x=30+col*580; y=93+row*(91 if mobile else 92); cw=540 if mobile else 550
        b+=rect(x,y,cw,78,'#152332','#35566a',10)
        b+=text(x+15,y+28,bg_names.get(p['name'],p['name']) if bg else p['name'],19,WHITE,700)
        role={'personal':'OWNER','organization':'ORG CONTRIBUTOR','collaborative':'COLLABORATOR'}[p['ownership']]
        if bg: role={'personal':'ЛИЧЕН','organization':'ПРИНОС В ОРГ.','collaborative':'СЪВМЕСТЕН'}[p['ownership']]
        stack=' / '.join(p['technologies'][:3]) or 'Documentation'
        category=bg_categories.get(p['category'],p['category']) if bg else p['category']
        b+=text(x+15,y+53,category.upper()+'  •  '+stack.upper(),12,MUTED,700)
        b+=text(x+cw-14,y+28,role,11,CYAN,700,'end')
        b+=text(x+cw-14,y+53,p['status'].upper() if not bg else ('ПУБЛИЧЕН' if p['status']=='Public' else 'ЧАСТЕН'),11,SOFT,700,'end')
    return svg(w,h,'All verified projects' if not bg else 'Всички потвърдени проекти',b)


def technology(projects: list[dict[str,Any]], lang: str, mobile: bool) -> str:
    bg=lang=='bg'; w,h=(600,700) if mobile else (1200,410)
    b=text(30,46,'06 / TECHNOLOGY MAP' if not bg else '06 / ТЕХНОЛОГИЧНА КАРТА',20,CYAN,700,spacing=2)
    groups=[('SYSTEMS' if not bg else 'СИСТЕМИ',['Rust','Lua','Python']),('WEB' if not bg else 'УЕБ',['TypeScript','Next.js','React']),('DATA' if not bg else 'ДАННИ',['PostgreSQL','MySQL','Prisma']),('DESKTOP + AI' if not bg else 'НАСТОЛНИ + AI',['Tauri 2','OpenAI','Anthropic']),('DELIVERY' if not bg else 'ДОСТАВЯНЕ',['GitHub Actions','Git'])]
    for i,(title,items) in enumerate(groups):
        if mobile: x=30+(i%2)*275; y=73+(i//2)*189; cw=260
        else: x=30+i*232; y=79; cw=216
        b+=rect(x,y,cw,164,'#142334','#36576a',12)
        b+=text(x+15,y+35,title,16,CYAN,700,spacing=1)
        for j,item in enumerate(items): b+=text(x+15,y+72+j*28,item,18,WHITE,600)
    note='Technologies observed in selected repository READMEs and file trees.' if not bg else 'Технологии, потвърдени в README и структурата на избрани хранилища.'
    b+=text(30,h-29,note,16,MUTED)
    return svg(w,h,'Technology map' if not bg else 'Технологична карта',b)


def languages_visual(snapshot: dict[str, Any], lang: str, mobile: bool) -> str:
    bg = lang == 'bg'; w, h = (600, 580) if mobile else (1200, 460)
    ordered = list(snapshot['languages'].items())[:7]
    largest = max((count for _, count in ordered), default=1)
    b = text(30, 44, 'AUTHORED COMMIT / FILE TOUCHES' if not bg else 'АВТОРСКИ COMMIT-И / ПРОМЕНЕНИ ФАЙЛОВЕ', 18, CYAN, 700, spacing=1)
    b += text(30, 77, f"{snapshot['commitsAnalyzed']} commits · {snapshot['repositoriesAnalyzed']} repositories · snapshot {snapshot['auditDate']}", 16, MUTED)
    for i, (name, count) in enumerate(ordered):
        y = 118 + i * (59 if mobile else 42)
        if mobile:
            b += text(30, y, name.upper(), 17, WHITE, 700)
            b += rect(30, y+13, 470, 17, '#203647', '#203647', 5)
            b += rect(30, y+13, max(4, round(470*count/largest)), 17, CYAN, CYAN, 5)
            b += text(550, y+29, count, 18, CYAN, 700, 'end')
        else:
            b += text(30, y+15, name.upper(), 17, WHITE, 700)
            b += rect(220, y, 850, 18, '#203647', '#203647', 5)
            b += rect(220, y, max(4, round(850*count/largest)), 18, CYAN, CYAN, 5)
            b += text(1140, y+16, count, 18, CYAN, 700, 'end')
    note = 'File touches, not code ownership or proficiency.' if not bg else 'Променени файлове, не собственост върху кода или умения.'
    b += text(30, h-25, note, 16, MUTED)
    return svg(w, h, 'Contribution-aware language activity' if not bg else 'Езикова активност от авторски промени', b)


def engineering(lang: str,mobile: bool)->str:
    bg=lang=='bg'; w,h=(600,690) if mobile else (1200,352)
    cols=[('SECURITY' if not bg else 'СИГУРНОСТ',['Validate server input','Guard credentials','Review AI edits'] if not bg else ['Сървърна валидация','Защита на ключове','Преглед на AI промени']),('PERFORMANCE' if not bg else 'ПРОИЗВОДИТЕЛНОСТ',['Bound work','Avoid needless polling','Measure bottlenecks'] if not bg else ['Ограничена работа','Без излишно обхождане','Измерване']),('ARCHITECTURE' if not bg else 'АРХИТЕКТУРА',['Clear trust boundaries','Modular components','Traceable data flow'] if not bg else ['Ясни граници','Модулни компоненти','Проследим поток']),('SHIPPING' if not bg else 'ДОСТАВЯНЕ',['Git and review','Tests and CI','Recovery paths'] if not bg else ['Git и преглед','Тестове и CI','Възстановяване'])]
    b=text(30,45,'05 / HOW I BUILD' if not bg else '05 / КАК РАЗРАБОТВАМ',20,CYAN,700,spacing=2)
    for i,(title,items) in enumerate(cols):
        x=30+(i%2)*274 if mobile else 30+i*291; y=70+(i//2)*300 if mobile else 73; cw=260 if mobile else 270
        b+=rect(x,y,cw,260,'#132231','#36576a',14)
        b+=text(x+20,y+44,f'0{i+1}',23,BLUE,800)+text(x+20,y+88,title,17,CYAN,700)
        for j,item in enumerate(items):
            b+=line(x+20,y+119+j*39,x+33,y+119+j*39,CYAN,2)
            b+=text(x+40,y+125+j*39,item,15,WHITE)
    return svg(w,h,'Engineering principles' if not bg else 'Инженерни принципи',b)

ARCH={
'codeguard':['LOCAL PROJECT','RUST SCANNER','FINDINGS','AI PROPOSAL','REVIEW / APPLY'],
'rules':['BROWSER','NEXT.JS','DISCORD AUTH','EDITOR','POSTGRESQL'],
'dmv':['PLAYER','NUI TABLET','LUA SERVER','QBOX / OX','MYSQL'],
'collaboration':['CLIENT','SERVER RESOURCES','SHARED WORKFLOW','PERSISTENCE'],
}

def architecture(key:str,lang:str,mobile:bool)->str:
    words=ARCH[key]; w=600 if mobile else 1200; h=112+len(words)*83 if mobile else 242
    if lang=='bg':
        words={'codeguard':['ЛОКАЛЕН ПРОЕКТ','RUST СКЕНЕР','НАХОДКИ','AI ПРЕДЛОЖЕНИЕ','ПРЕГЛЕД / ПРИЛАГАНЕ'], 'rules':['БРАУЗЪР','NEXT.JS','DISCORD ВХОД','РЕДАКТОР','POSTGRESQL'], 'dmv':['ИГРАЧ','NUI ТАБЛЕТ','LUA СЪРВЪР','QBOX / OX','MYSQL'], 'collaboration':['КЛИЕНТ','СЪРВЪРНИ РЕСУРСИ','СПОДЕЛЕН ПРОЦЕС','ДАННИ']}[key]
    title={'codeguard':'CODEGUARD','rules':'RULES PLATFORM','dmv':'DMV SYSTEM','collaboration':'FIVEM COLLABORATION'}[key]
    b=text(30,42,'07 / SYSTEM MAP — '+title,18,CYAN,700,spacing=1)
    for i,word in enumerate(words):
        if mobile:
            x=38;y=68+i*83;cw=524;ch=60
            b+=rect(x,y,cw,ch,'#152838','#427086',12)+text(x+cw//2,y+38,word,19,WHITE,700,'middle')
            if i<len(words)-1:b+=text(300,y+79,'↓',19,CYAN,700,'middle')
        else:
            cw=190 if len(words)==5 else 245; gap=(w-60-len(words)*cw)//(len(words)-1);x=30+i*(cw+gap);y=88
            b+=rect(x,y,cw,82,'#152838','#427086',12)+text(x+cw//2,y+49,word,17,WHITE,700,'middle')
            if i<len(words)-1:b+=text(x+cw+gap//2,y+51,'→',23,CYAN,700,'middle')
    b+=text(30,h-21,'Verified components / high-level view' if lang=='en' else 'Потвърдени компоненти / общ преглед',14,MUTED)
    return svg(w,h,title+' architecture',b)


def section(number:int,name:str,lang:str)->str:
    w,h=1200,94
    b=text(28,38,f'{number:02d}',27,CYAN,800)+line(80,19,80,73,LINE)+text(104,54,name,31,WHITE,800,spacing=2)
    b+=line(28,78,1172,78,CYAN,2)
    return svg(w,h,name,b)


def generate(projects: list[dict[str,Any]]) -> list[Path]:
    OUT.mkdir(parents=True,exist_ok=True)
    generated=[]
    language_snapshot = json.loads((ROOT/'data/languages.json').read_text(encoding='utf-8'))
    sections={'en':['COMMAND CENTER','FEATURED SYSTEMS','ALL PROJECTS','HOW I BUILD','TECHNOLOGY','ARCHITECTURE','ACTIVITY','ABOUT','CONTACT'],'bg':['ЦЕНТЪР ЗА РАЗРАБОТКА','ОСНОВНИ СИСТЕМИ','ВСИЧКИ ПРОЕКТИ','ИНЖЕНЕРЕН ПОДХОД','ТЕХНОЛОГИИ','АРХИТЕКТУРА','АКТИВНОСТ','ЗА МЕН','КОНТАКТ']}
    for lang in ('en','bg'):
        for mobile in (False,True):
            suffix='-mobile' if mobile else ''
            items={'hero':hero(lang,mobile),'command':command(lang,mobile),'matrix':matrix(projects,lang,mobile),'technology':technology(projects,lang,mobile),'languages':languages_visual(language_snapshot,lang,mobile),'engineering':engineering(lang,mobile)}
            for key in FEATURES: items['feature-'+key]=feature(key,lang,mobile)
            for key in ARCH: items['architecture-'+key]=architecture(key,lang,mobile)
            for name,content in items.items():
                path=OUT/f'{name}-{lang}{suffix}.svg';path.write_text(content,encoding='utf-8');generated.append(path)
        for i,title in enumerate(sections[lang],2):
            path=OUT/f'section-{i:02d}-{lang}.svg';path.write_text(section(i,title,lang),encoding='utf-8');generated.append(path)
    return generated


def main()->None:
    data=json.loads((ROOT/'data/projects.json').read_text(encoding='utf-8'))
    projects=data['projects']
    if len({p['id'] for p in projects})!=len(projects):raise ValueError('Duplicate project id')
    if any(p['visibility']=='private' and p['repository'] for p in projects):raise ValueError('Private repository URL in public inventory')
    print(f'Generated {len(generate(projects))} SVG assets from {len(projects)} projects')


if __name__=='__main__':main()
