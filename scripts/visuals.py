"""Render the public portfolio's deterministic, bilingual SVG design system."""
from __future__ import annotations

import json
import math
from html import escape
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'generated'
from theme import (BG, SURFACE, ELEVATED, BORDER as LINE,
                   CYAN, BLUE, TEXT as WHITE, MUTED, SOFT, PURPLE, VIOLET,
                   GREEN, ORANGE, RED, FONT, PROJECT_ACCENTS, CATEGORY_ACCENTS,
                   ARCHITECTURE_ACCENTS, SHELL_END, GRID, SELECTED, CORE,
                   PREVIEW_BLUE, PREVIEW_ORANGE, PREVIEW_NODE, TRACK)
PANEL = SURFACE
PANEL2 = ELEVATED


def text(x: int, y: int, value: str, size: int = 20, color: str = WHITE, weight: int = 400, anchor: str = 'start', spacing: int = 0) -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{spacing}">{escape(str(value))}</text>'


def rect(x: int, y: int, w: int, h: int, fill: str = PANEL, stroke: str = LINE, radius: int = 14) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def line(x1: int, y1: int, x2: int, y2: int, color: str = LINE, width: int = 2) -> str:
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"/>'


def svg(w: int, h: int, title: str, body: str, accent: str = BLUE) -> str:
    defs = f'''<defs><linearGradient id="shell" x2="1" y2="1"><stop stop-color="{SURFACE}"/><stop offset=".58" stop-color="{BG}"/><stop offset="1" stop-color="{SHELL_END}"/></linearGradient><radialGradient id="glow"><stop stop-color="{accent}" stop-opacity=".30"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient><linearGradient id="accent"><stop stop-color="{accent}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient><clipPath id="clip"><rect width="{w}" height="{h}" rx="24"/></clipPath></defs>'''
    shell = f'<rect width="{w}" height="{h}" rx="24" fill="url(#shell)"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="23" fill="none" stroke="{LINE}"/><path d="M24 1H{w-24}" stroke="url(#accent)" opacity=".78"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)} — AstroByte Development portfolio visual.</desc>{defs}{shell}<g clip-path="url(#clip)">{body}</g></svg>\n'


def grid(w: int, h: int, step: int = 40) -> str:
    return ''.join(line(x, 0, x, h, GRID, 1) for x in range(0, w, step)) + ''.join(line(0, y, w, y, GRID, 1) for y in range(0, h, step))


def chip(x: int, y: int, label: str, width: int, accent: str = CYAN) -> str:
    return rect(x, y, width, 32, PANEL2, accent, 9) + text(x + width//2, y + 22, label, 13, accent, 700, 'middle', 1)


def header(lang: str, mobile: bool) -> str:
    w, h = (600, 76) if mobile else (1200, 76)
    x = w - 164
    active = 0 if lang == 'en' else 1
    b = f'<rect x="1" y="1" width="{w-2}" height="74" rx="21" fill="{BG}" stroke="{LINE}"/>'
    b += f'<path d="M24 75H{w-24}" stroke="url(#accent)" stroke-width="2"/>'
    b += f'<circle cx="36" cy="38" r="7" fill="{CYAN}"/><circle cx="36" cy="38" r="14" fill="none" stroke="{CYAN}" opacity=".35"/>'
    b += text(58, 44, 'ASTROBYTE  /  DEV', 16 if mobile else 18, WHITE, 800, spacing=2)
    b += rect(x, 17, 136, 42, PANEL2, LINE, 12)
    b += rect(x+4+active*64, 21, 64, 34, SELECTED, BLUE, 9)
    b += text(x+36, 43, 'EN', 13, WHITE if active == 0 else MUTED, 800, 'middle')
    b += text(x+100, 43, 'BG', 13, WHITE if active == 1 else MUTED, 800, 'middle')
    return svg(w, h, 'Language: English selected; switch to Bulgarian' if lang == 'en' else 'Език: избран български; към английски', b)


def hero(lang: str, mobile: bool) -> str:
    bg = lang == 'bg'; w, h = (600, 760) if mobile else (1200, 530)
    b = grid(w, h, 40)
    b += f'<ellipse cx="{w-90}" cy="125" rx="280" ry="220" fill="url(#glow)"/>'
    b += f'<ellipse cx="{w//2}" cy="{h-20}" rx="360" ry="160" fill="{PURPLE}" opacity=".09"/>'
    b += text(38, 53, 'ENGINEERING  /  SYSTEMS  /  DELIVERY' if not bg else 'ИНЖЕНЕРСТВО  /  СИСТЕМИ  /  РЕЗУЛТАТИ', 15, CYAN, 700, spacing=2)
    if mobile:
        b += text(38, 150, 'GEORGI', 77, WHITE, 800, spacing=2)
        b += text(38, 214, 'KANCHEV', 66, WHITE, 800, spacing=1)
        b += text(40, 259, 'SOFTWARE ENGINEER / PRODUCT BUILDER' if not bg else 'СОФТУЕРЕН ИНЖЕНЕР / СЪЗДАТЕЛ', 17, BLUE, 700)
        b += rect(34, 307, 532, 282, SURFACE, BLUE, 20)
        b += f'<rect x="35" y="308" width="530" height="280" rx="19" fill="{PURPLE}" opacity=".07"/>'
        b += text(55, 345, 'SYSTEM / SIGNAL' if not bg else 'СИСТЕМА / СИГНАЛ', 16, MUTED, 700, spacing=2)
        nodes = [('RUST CORE' if not bg else 'RUST ЯДРО', PURPLE), ('FIVEM SERVER' if not bg else 'FIVEM СЪРВЪР', ORANGE), ('WEB PLATFORM' if not bg else 'УЕБ ПЛАТФОРМА', BLUE), ('LOCAL AI' if not bg else 'ЛОКАЛЕН AI', CYAN)]
        for i, (label, accent) in enumerate(nodes):
            yy = 386+i*46
            b += f'<circle cx="65" cy="{yy-6}" r="7" fill="{accent}" opacity=".28"/><circle cx="65" cy="{yy-6}" r="3" fill="{accent}"/>'
            b += line(72, yy-6, 133, yy-6, accent, 2) + text(150, yy, label, 19, WHITE, 700)
        b += text(38, 635, 'Tools, infrastructure and web products.' if not bg else 'Инструменти, инфраструктура и уеб продукти.', 19, WHITE)
        b += text(38, 678, 'SECURE  /  DESIGN  /  SHIP' if not bg else 'СИГУРНОСТ  /  ДИЗАЙН  /  ДОСТАВКА', 15, SOFT, 700, spacing=1)
        b += line(38, 704, 562, 704, BLUE) + text(38, 735, '01 / PORTFOLIO / 2026', 14, CYAN, 700, spacing=2)
    else:
        b += text(53, 172, 'GEORGI', 105, WHITE, 800, spacing=2)
        b += text(55, 243, 'KANCHEV', 76, WHITE, 800, spacing=2)
        b += text(57, 290, 'SOFTWARE ENGINEER / PRODUCT BUILDER' if not bg else 'СОФТУЕРЕН ИНЖЕНЕР / СЪЗДАТЕЛ', 21, CYAN, 700, spacing=1)
        b += text(57, 352, 'Building developer tools, server systems and web products.' if not bg else 'Инструменти, сървърни системи и уеб продукти.', 22, WHITE)
        b += chip(57, 397, 'RUST', 95, PURPLE)+chip(165, 397, 'FIVEM', 105, ORANGE)+chip(283, 397, 'FULL-STACK', 147, BLUE)+chip(443, 397, 'MACOS', 105, CYAN)
        b += rect(748, 88, 405, 355, SURFACE, BLUE, 20)
        b += f'<rect x="750" y="90" width="401" height="351" rx="18" fill="{PURPLE}" opacity=".07"/>'
        b += text(775, 128, 'SYSTEM / SIGNAL', 16, CYAN, 700, spacing=2)
        b += text(1120, 128, '● ONLINE', 12, GREEN, 800, 'end')
        b += line(775, 149, 1125, 149, LINE)
        nodes = [(795,174,'CODEGUARD','SCAN / REVIEW',PURPLE),(984,174,'FIVEM','SERVER / DATA',ORANGE),(795,332,'WEB','ADMIN / AUTH',BLUE),(984,332,'DELIVERY','TEST / SHIP',GREEN)]
        for xx,yy,label,detail,accent in nodes:
            b += line(950, 271, xx+67, yy+32, accent, 2)
            b += rect(xx, yy, 145, 66, ELEVATED, accent, 10)
            b += f'<rect x="{xx+2}" y="{yy+2}" width="141" height="62" rx="8" fill="{accent}" opacity=".10"/>'
            b += text(xx+72, yy+27, label, 15, WHITE, 800, 'middle')+text(xx+72, yy+48, detail, 10, MUTED, 700, 'middle')
        b += f'<circle cx="950" cy="271" r="51" fill="{CORE}" stroke="{CYAN}" stroke-width="2"/><circle cx="950" cy="271" r="62" fill="none" stroke="{PURPLE}" opacity=".28"/>'
        b += text(950, 266, 'ASTRO', 18, WHITE, 800, 'middle')+text(950, 289, 'BYTE', 18, CYAN, 800, 'middle')
        b += text(55, 492, '01 / ENGINEERING PORTFOLIO' if not bg else '01 / ИНЖЕНЕРНО ПОРТФОЛИО', 16, SOFT, 700, spacing=2)
    return svg(w, h, 'Georgi Kanchev — software engineering portfolio', b, PURPLE)


def command(lang: str, mobile: bool) -> str:
    bg=lang=='bg'; w,h=(600,710) if mobile else (1200,360)
    b=text(30,45,'02 / DEVELOPER COMMAND CENTER' if not bg else '02 / ЦЕНТЪР ЗА РАЗРАБОТКА',18,BLUE,700,spacing=2)
    cols=[('CURRENT FOCUS' if not bg else 'ТЕКУЩ ФОКУС',['Developer tools','FiveM infrastructure','Full-stack systems','macOS desktop'] if not bg else ['Инструменти','FiveM инфраструктура','Уеб системи','macOS приложение'],BLUE),('CORE LANGUAGES' if not bg else 'ЕЗИЦИ',['Rust','Lua','TypeScript','Python'],CYAN),('ENGINEERING' if not bg else 'ИНЖЕНЕРСТВО',['Security','Architecture','Testing','Automation'] if not bg else ['Сигурност','Архитектура','Тестове','Автоматизация'],PURPLE),('WORKFLOW' if not bg else 'РАБОТЕН ПРОЦЕС',['Build','Validate','Review','Ship'] if not bg else ['Разработка','Проверка','Преглед','Доставка'],GREEN)]
    for i,(heading,items,accent) in enumerate(cols):
        x=30+(i%2)*274 if mobile else 30+i*291; y=66+(i//2)*314 if mobile else 67; cw=264 if mobile else 270
        b+=rect(x,y,cw,280,SURFACE,accent,14)
        b+=f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="80" rx="13" fill="{accent}" opacity=".11"/>'
        b+=f'<path d="M{x+18} {y+3}H{x+cw-18}" stroke="{accent}" stroke-width="3"/>'
        b+=text(x+20,y+37,f'0{i+1} / {heading}',16,accent,700)
        b+=line(x+20,y+55,x+cw-20,y+55,LINE)
        for j,item in enumerate(items):
            yy=y+94+j*42
            b+=f'<circle cx="{x+27}" cy="{yy-7}" r="4" fill="{accent}"/>'
            b+=text(x+42,yy,item,17,WHITE,600)
    return svg(w,h,'Developer command center' if not bg else 'Център за разработка',b,BLUE)

FEATURES={
'codeguard':('CODEGUARD','LOCAL CODE INTELLIGENCE','Rust scanner → findings → AI proposal → review',['STATIC ANALYSIS','SECURITY SIGNAL','AI FIX REVIEW','SAFE REVERT'],['RUST','TAURI','REACT','OPENAI / ANTHROPIC']),
'rules':('RULES PLATFORM','WEB ADMINISTRATION','Public rules → Discord OAuth → editorial workflow',['DRAFT / PUBLISH','VERSION HISTORY','ACCESS CONTROL','AUDIT LOG'],['NEXT.JS','TYPESCRIPT','POSTGRESQL','PRISMA']),
'dmv':('DMV SYSTEM','FIVEM VEHICLE WORKFLOW','NUI tablet → Lua server → Qbox → MySQL',['REGISTRATION','PLATE HISTORY','QR VERIFICATION','LOCALIZATION'],['LUA','QBOX','OX LIB','MYSQL']),
'registry':('BUSINESS REGISTRY','FIVEM RECORD SYSTEM','Tablet → server validation → records → log',['BUSINESS RECORDS','DOCUMENTS','SERVER VALIDATION','ACTIVITY LOG'],['LUA','QBOX','NUI','MYSQL']),
'collaboration':('SERVER INFRASTRUCTURE','COLLABORATIVE FIVEM WORK','Authored changes in a shared private repository',['RESOURCE INTEGRATION','DATABASE CHANGES','TEAM REPOSITORY','SHARED OWNERSHIP'],['LUA','TYPESCRIPT','VUE','GIT']),
}


def product_preview(key: str, x: int, y: int, w: int, h: int, bg: bool) -> str:
    """Distinct miniature product views; labels describe architecture, not live metrics."""
    accent = PROJECT_ACCENTS[key]
    b = rect(x, y, w, h, SURFACE, accent, 14)
    b += f'<rect x="{x+1}" y="{y+1}" width="{w-2}" height="{h-2}" rx="13" fill="{accent}" opacity=".06"/>'
    small = 13 if w < 400 else 15
    b += text(x+17, y+30, {
        'codeguard':'СКЕНЕР / НАХОДКИ' if bg else 'SCANNER / FINDINGS',
        'rules':'ЧЕРНОВА / ПУБЛИКУВАНЕ' if bg else 'DRAFT / PUBLISH',
        'dmv':'РЕГИСТРАЦИЯ / ПРЕВОЗНО СРЕДСТВО' if bg else 'REGISTRATION / VEHICLE',
        'registry':'ЗАПИСИ / ДОКУМЕНТИ' if bg else 'RECORDS / DOCUMENTS',
        'collaboration':'СПОДЕЛЕНА ИНФРАСТРУКТУРА' if bg else 'SHARED INFRASTRUCTURE',
    }[key], small, accent, 700, spacing=1)
    if key == 'codeguard':
        for i, length in enumerate((.78,.55,.86,.45,.68)):
            b += rect(x+20,y+52+i*23,round((w*.43)*length),8,PURPLE,PURPLE,3)
        b += line(x+w//2,y+54,x+w//2,y+h-22,VIOLET,2)
        b += text(x+w//2+20,y+81,'FINDINGS',15,RED,700)
        b += text(x+w//2+20,y+116,'→ REVIEW',15,VIOLET,700)
        if h>200:b+=text(x+w//2+20,y+151,'→ APPLY',15,WHITE,700)
    elif key == 'rules':
        labels=['DRAFT','REVIEW','PUBLIC'] if not bg else ['ЧЕРНОВА','ПРЕГЛЕД','ПУБЛИЧНО']
        for i,label in enumerate(labels):
            xx=x+16+i*(w-32)//3;ww=(w-50)//3
            b+=rect(xx,y+68,ww,75,PREVIEW_BLUE,BLUE,9)
            b+=text(xx+ww//2,y+110,label,13 if w<400 else 15,WHITE,700,'middle')
        b+=text(x+w//2,y+h-20,'DISCORD AUTH  /  AUDIT',12,MUTED,700,'middle')
    elif key == 'dmv':
        b+=rect(x+18,y+58,w-36,83,PREVIEW_ORANGE,ORANGE,10)
        b+=text(x+35,y+88,'VIN  →  PLATE  →  RECORD' if not bg else 'VIN  →  НОМЕР  →  ЗАПИС',14,WHITE,700)
        b+=line(x+35,y+104,x+w-35,y+104,CYAN,2)
        b+=text(x+35,y+129,'QBOX  /  LUA  /  MYSQL',14,CYAN,700)
        if h>200:b+=text(x+20,y+h-18,'REGISTRATION HISTORY' if not bg else 'ИСТОРИЯ НА РЕГИСТРАЦИИТЕ',12,MUTED,700)
    elif key == 'registry':
        labels=['BUSINESS','DOCUMENTS','AUDIT'] if not bg else ['БИЗНЕС','ДОКУМЕНТИ','ЖУРНАЛ']
        for i,label in enumerate(labels):
            yy=y+58+i*43
            b+=rect(x+18,yy,w-36,34,PREVIEW_BLUE,ORANGE,7)
            b+=text(x+34,yy+23,label,14,WHITE,700)
            b+=text(x+w-34,yy+23,'✓',16,CYAN,700,'end')
    else:
        labels=['CLIENT','SERVER','DATA'] if not bg else ['КЛИЕНТ','СЪРВЪР','ДАННИ']
        centers=[x+w//6,x+w//2,x+w*5//6]
        b+=line(centers[0],y+105,centers[2],y+105,CYAN,2)
        for center,label in zip(centers,labels):
            b+=f'<circle cx="{center}" cy="{y+105}" r="19" fill="{PREVIEW_NODE}" stroke="{accent}" stroke-width="2"/>'
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
    accent=PROJECT_ACCENTS[key]
    b=grid(w,h,44)
    b+=f'<ellipse cx="{w-80}" cy="85" rx="260" ry="150" fill="{accent}" opacity=".10"/>'
    b+=text(34,45,('ОСНОВЕН / ' if bg else 'FEATURED / ')+key.upper(),16,accent,700,spacing=2)
    b+=text(34,105,name,47 if mobile else 61,WHITE,800,spacing=1)
    b+=text(36,142,subtitle,19,accent,700,spacing=1)
    if mobile:
        b+=rect(30,169,540,356,SURFACE,accent,16)
        b+=text(49,202,'SYSTEM / '+('SIGNALS' if not bg else 'СИГНАЛИ'),15,MUTED,700,spacing=2)
        for i,s in enumerate(signals):
            y=233+i*73
            b+=rect(49,y,502,59,ELEVATED,accent,10)
            b+=text(68,y+36,s,18,WHITE,700)
            b+=text(527,y+36,f'0{i+1}',16,accent,700,'end')
        b+=product_preview(key,30,546,540,208,bg)
        b+=text(33,792,flow,16,MUTED)
        b+=text(33,832,' / '.join(tech[:3]),17,accent,700)
        b+=text(33,867,'PRIVATE SOURCE  ·  VERIFIED WORK' if not bg else 'ЧАСТЕН КОД  ·  ПРОВЕРЕН ПРИНОС',13,SOFT,700,spacing=1)
    else:
        b+=rect(34,178,730,242,SURFACE,accent,16)
        b+=text(57,212,'ПРОДУКТ / СИСТЕМА' if bg else 'PRODUCT / SYSTEM VIEW',15,MUTED,700,spacing=2)
        for i,s in enumerate(signals):
            x=55+(i%2)*345; y=240+(i//2)*79
            b+=rect(x,y,323,60,ELEVATED,accent,10)
            b+=text(x+17,y+36,s,18,WHITE,700)
        b+=product_preview(key,789,178,376,242,bg)
        b+=text(35,451,' / '.join(tech),16,accent,700)
    return svg(w,h,name+' project dashboard',b,accent)


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
        accent=CATEGORY_ACCENTS[p['category']]
        b+=rect(x,y,cw,78,SURFACE,accent,10)
        b+=f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="76" rx="9" fill="{accent}" opacity=".055"/>'
        b+=f'<rect x="{x+2}" y="{y+10}" width="3" height="58" rx="1" fill="{accent}"/>'
        b+=text(x+15,y+28,bg_names.get(p['name'],p['name']) if bg else p['name'],19,WHITE,700)
        role={'personal':'OWNER','organization':'ORG CONTRIBUTOR','collaborative':'COLLABORATOR'}[p['ownership']]
        if bg: role={'personal':'ЛИЧЕН','organization':'ПРИНОС В ОРГ.','collaborative':'СЪВМЕСТЕН'}[p['ownership']]
        stack=' / '.join(p['technologies'][:3]) or 'Documentation'
        category=bg_categories.get(p['category'],p['category']) if bg else p['category']
        b+=text(x+15,y+53,category.upper()+'  •  '+stack.upper(),12,MUTED,700)
        status=p['status'].upper() if not bg else ('ПУБЛИЧЕН' if p['status']=='Public' else 'ЧАСТЕН')
        b+=text(x+cw-14,y+53,role+' / '+status,11,accent,700,'end')
    return svg(w,h,'All verified projects' if not bg else 'Всички потвърдени проекти',b)


def technology(projects: list[dict[str,Any]], lang: str, mobile: bool) -> str:
    bg=lang=='bg'; w,h=(600,670) if mobile else (1200,320)
    b=text(30,46,'06 / TECHNOLOGY MAP' if not bg else '06 / ТЕХНОЛОГИЧНА КАРТА',20,BLUE,700,spacing=2)
    groups=[('SYSTEMS' if not bg else 'СИСТЕМИ',['Rust','Lua','Python'],PURPLE),('WEB' if not bg else 'УЕБ',['TypeScript','Next.js','React'],BLUE),('DATA' if not bg else 'ДАННИ',['PostgreSQL','MySQL','Prisma'],CYAN),('DESKTOP + AI' if not bg else 'DESKTOP + AI',['Tauri 2','OpenAI','Anthropic'],VIOLET),('DELIVERY' if not bg else 'ДОСТАВКА',['GitHub Actions','Git'],GREEN)]
    for i,(title,items,accent) in enumerate(groups):
        if mobile: x=30+(i%2)*275; y=73+(i//2)*189; cw=260
        else: x=30+i*232; y=79; cw=216
        b+=rect(x,y,cw,164,SURFACE,accent,12)
        b+=f'<path d="M{x+12} {y+2}H{x+cw-12}" stroke="{accent}" stroke-width="3"/>'
        b+=f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="72" rx="11" fill="{accent}" opacity=".08"/>'
        b+=text(x+15,y+35,title,16,accent,700,spacing=1)
        for j,item in enumerate(items):
            b+=f'<circle cx="{x+21}" cy="{y+66+j*28}" r="3" fill="{accent}"/>'
            b+=text(x+35,y+72+j*28,item,18,WHITE,600)
    note='Observed in selected repositories and documentation.' if not bg else 'Потвърдени в избрани хранилища и документация.'
    b+=text(30,h-29,note,16,MUTED)
    return svg(w,h,'Technology map' if not bg else 'Технологична карта',b,BLUE)


def languages_visual(snapshot: dict[str, Any], lang: str, mobile: bool) -> str:
    bg = lang == 'bg'; w, h = (600, 580) if mobile else (1200, 460)
    ordered = list(snapshot['languages'].items())[:7]
    largest = max((count for _, count in ordered), default=1)
    b = text(30, 44, 'AUTHORED COMMIT / FILE TOUCHES' if not bg else 'АВТОРСКИ COMMIT-И / ПРОМЕНЕНИ ФАЙЛОВЕ', 18, CYAN, 700, spacing=1)
    b += text(30, 77, f"{snapshot['commitsAnalyzed']} commits · {snapshot['repositoriesAnalyzed']} repositories · snapshot {snapshot['auditDate']}", 16, MUTED)
    language_accents={'Lua':ORANGE,'Rust':PURPLE,'TypeScript':BLUE,'Python':CYAN,'SQL':CYAN,'JavaScript':BLUE,'HTML':VIOLET,'CSS':VIOLET}
    for i, (name, count) in enumerate(ordered):
        accent=language_accents.get(name,CYAN)
        y = 118 + i * (59 if mobile else 42)
        if mobile:
            b += text(30, y, name.upper(), 17, WHITE, 700)
            b += rect(30, y+13, 470, 17, TRACK, TRACK, 5)
            b += rect(30, y+13, max(4, round(470*count/largest)), 17, accent, accent, 5)
            b += text(550, y+29, count, 18, accent, 700, 'end')
        else:
            b += text(30, y+15, name.upper(), 17, WHITE, 700)
            b += rect(220, y, 850, 18, TRACK, TRACK, 5)
            b += rect(220, y, max(4, round(850*count/largest)), 18, accent, accent, 5)
            b += text(1140, y+16, count, 18, accent, 700, 'end')
    note = 'File touches, not code ownership or proficiency.' if not bg else 'Променени файлове, не собственост върху кода или умения.'
    b += text(30, h-25, note, 16, MUTED)
    return svg(w, h, 'Contribution-aware language activity' if not bg else 'Езикова активност от авторски промени', b)


def engineering(lang: str,mobile: bool)->str:
    bg=lang=='bg'; w,h=(600,690) if mobile else (1200,352)
    cols=[('SECURITY' if not bg else 'СИГУРНОСТ',['Validate server input','Guard credentials','Review AI edits'] if not bg else ['Сървърна валидация','Защита на ключове','Преглед на AI промени']),('PERFORMANCE' if not bg else 'ПРОИЗВОДИТЕЛНОСТ',['Bound work','Avoid needless polling','Measure bottlenecks'] if not bg else ['Ограничена работа','Без излишно обхождане','Измерване']),('ARCHITECTURE' if not bg else 'АРХИТЕКТУРА',['Clear trust boundaries','Modular components','Traceable data flow'] if not bg else ['Ясни граници','Модулни компоненти','Проследим поток']),('SHIPPING' if not bg else 'ДОСТАВЯНЕ',['Git and review','Tests and CI','Recovery paths'] if not bg else ['Git и преглед','Тестове и CI','Възстановяване'])]
    b=text(30,45,'05 / HOW I BUILD' if not bg else '05 / КАК РАЗРАБОТВАМ',20,CYAN,700,spacing=2)
    accents=[RED,CYAN,PURPLE,GREEN]
    for i,(title,items) in enumerate(cols):
        accent=accents[i]
        x=30+(i%2)*274 if mobile else 30+i*291; y=70+(i//2)*300 if mobile else 73; cw=260 if mobile else 270
        b+=rect(x,y,cw,260,SURFACE,accent,14)
        b+=text(x+20,y+44,f'0{i+1}',23,accent,800)+text(x+20,y+88,title,17,accent,700)
        for j,item in enumerate(items):
            b+=line(x+20,y+119+j*39,x+33,y+119+j*39,accent,2)
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
    semantic={'codeguard':['infrastructure','security','security','ai','frontend'],'rules':['frontend','backend','external','backend','database'],'dmv':['frontend','frontend','backend','infrastructure','database'],'collaboration':['frontend','backend','infrastructure','database']}[key]
    b=text(30,42,'07 / SYSTEM MAP — '+title,18,CYAN,700,spacing=1)
    for i,word in enumerate(words):
        accent=ARCHITECTURE_ACCENTS[semantic[i]]
        if mobile:
            x=38;y=68+i*83;cw=524;ch=60
            b+=rect(x,y,cw,ch,SURFACE,accent,12)+text(x+cw//2,y+38,word,19,WHITE,700,'middle')
            if i<len(words)-1:b+=text(300,y+79,'↓',19,accent,700,'middle')
        else:
            cw=190 if len(words)==5 else 245; gap=(w-60-len(words)*cw)//(len(words)-1);x=30+i*(cw+gap);y=88
            b+=rect(x,y,cw,82,SURFACE,accent,12)+text(x+cw//2,y+49,word,17,WHITE,700,'middle')
            if i<len(words)-1:b+=text(x+cw+gap//2,y+51,'→',23,accent,700,'middle')
    b+=text(30,h-21,'Verified components / high-level view' if lang=='en' else 'Потвърдени компоненти / общ преглед',14,MUTED)
    return svg(w,h,title+' architecture',b,PURPLE if key=='codeguard' else ORANGE if key in ('dmv','collaboration') else BLUE)


def section(number:int,name:str,lang:str)->str:
    w,h=1200,110
    accent={2:BLUE,3:PURPLE,4:ORANGE,5:CYAN,6:BLUE,7:VIOLET,8:GREEN,9:CYAN,10:BLUE}[number]
    subtitles={'en':{2:'Systems in focus',3:'Selected engineering work',4:'Verified project inventory',5:'Principles and practice',6:'Tools behind the work',7:'How the pieces connect',8:'Public GitHub activity',9:'The engineer behind the systems',10:'Start a conversation'},'bg':{2:'Системи във фокус',3:'Избрани разработки',4:'Проверен списък с проекти',5:'Принципи и практика',6:'Инструменти и технологии',7:'Връзки между компонентите',8:'Публична GitHub активност',9:'За човека зад системите',10:'Свържете се с мен'}}
    b=f'<rect x="1" y="1" width="1198" height="108" rx="23" fill="{accent}" opacity=".045"/>'
    b+=f'<rect x="28" y="23" width="3" height="61" rx="1" fill="{accent}"/>'
    b+=text(46,45,f'{number:02d} / {name}',26,WHITE,800,spacing=1)
    b+=text(47,77,subtitles[lang][number],17,MUTED,500)
    b+=line(46,93,1155,93,accent,2)
    return svg(w,h,name,b,accent)


def generate(projects: list[dict[str,Any]]) -> list[Path]:
    OUT.mkdir(parents=True,exist_ok=True)
    generated=[]
    language_snapshot = json.loads((ROOT/'data/languages.json').read_text(encoding='utf-8'))
    sections={'en':['COMMAND CENTER','FEATURED SYSTEMS','ALL PROJECTS','HOW I BUILD','TECHNOLOGY','ARCHITECTURE','ACTIVITY','ABOUT','CONTACT'],'bg':['ЦЕНТЪР ЗА РАЗРАБОТКА','ОСНОВНИ СИСТЕМИ','ВСИЧКИ ПРОЕКТИ','ИНЖЕНЕРЕН ПОДХОД','ТЕХНОЛОГИИ','АРХИТЕКТУРА','АКТИВНОСТ','ЗА МЕН','КОНТАКТ']}
    for lang in ('en','bg'):
        for mobile in (False,True):
            suffix='-mobile' if mobile else ''
            items={'header':header(lang,mobile),'hero':hero(lang,mobile),'command':command(lang,mobile),'matrix':matrix(projects,lang,mobile),'technology':technology(projects,lang,mobile),'languages':languages_visual(language_snapshot,lang,mobile),'engineering':engineering(lang,mobile)}
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
