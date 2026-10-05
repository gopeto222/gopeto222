"""Evidence-grounded project maps and complete grouped archive."""
from __future__ import annotations

import math
from typing import Any

from theme import (ACCENTS, BLUE, CYAN, PURPLE, VIOLET, AMBER, GREEN, RED,
                   SURFACE_0, SURFACE_1, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED,
                   CATEGORY_ACCENTS, BORDER_SUBTLE)
from portfolio.svg import document, text, lines, rect, panel, node, circle, rule, arrow, pill, wrap

NAMES_BG = {
    'Engineering profile':'Инженерен профил', 'Development documentation':'Документация за разработка',
    'Armor plate resource':'Ресурс за бронеплочи', 'Business registry':'Бизнес регистър',
    'Collaborative FiveM server infrastructure':'Съвместна FiveM инфраструктура',
    'Crime system resource':'Криминална система', 'DMV tablet system':'DMV таблет',
    'Document resource':'Система за документи', 'Fishing resource':'Ресурс за риболов',
    'FiveM server resource collection':'Колекция FiveM ресурси',
    'Game environment integration collection':'Интеграции на игрова среда',
    'Pawnshop resource':'Заложна къща', 'Police boat resource':'Полицейска лодка',
    'Police equipment resource':'Полицейско оборудване', 'Small robberies resource':'Малки обири',
    'Traffic resource':'Трафик система', 'Vehicle identification resource':'Идентификация на превозни средства',
    'Voltage system resource':'Електрическа система', 'Rules administration platform':'Платформа за правила',
}
CATEGORY_BG = {'Developer tools':'Инструменти', 'Engineering operations':'Инженерни процеси',
               'FiveM systems':'FiveM системи', 'Web systems':'Уеб системи'}


def _flow(width: int, labels: list[str], accents: list[str], mobile: bool) -> str:
    body=''
    if mobile:
        x=61; y0=244; boxw=478; boxh=66; step=91
        for i,label in enumerate(labels):
            y=y0+i*step
            body+=node(x,y,boxw,boxh,label,accents[i],size=21)
            if i<len(labels)-1: body+=arrow(300,y+boxh+3,300,y+step-7,accents[i])
    else:
        count=len(labels); gap=20; boxw=(width-100-(count-1)*gap)//count; y=236
        for i,label in enumerate(labels):
            x=50+i*(boxw+gap)
            body+=node(x,y,boxw,96,label,accents[i],size=18 if len(label)<20 else 15)
            if i<count-1: body+=arrow(x+boxw+3,y+48,x+boxw+gap-3,y+48,accents[i])
    return body


def _system_map(key: str, labels: list[str], colors: list[str], mobile: bool) -> str:
    if key == 'codeguard':
        return _flow(600 if mobile else 1200, labels, colors, mobile)
    if mobile:
        # The narrow composition keeps a clear reading order, while the node
        # geometry identifies the type of system being described.
        x, width, ys = 61, 478, [244, 335, 426, 517, 608]
        output = ''
        if key == 'rules':
            for i, label in enumerate(labels):
                output += node(x, ys[i], width, 65, label, colors[i], size=19)
                if i < 4: output += arrow(300, ys[i] + 69, 300, ys[i+1] - 5, colors[i])
        elif key == 'dmv':
            for i, label in enumerate(labels):
                output += node(x + (20 if i in (0, 4) else 0), ys[i], width - (40 if i in (0, 4) else 0), 65, label, colors[i], size=20)
                if i < 4: output += arrow(300, ys[i] + 69, 300, ys[i+1] - 5, colors[i])
        elif key == 'registry':
            for i, label in enumerate(labels):
                y = 254 + i * 115
                output += node(x, y, width, 72, label, colors[i], size=20)
                if i < 3: output += arrow(300, y + 77, 300, y + 106, colors[i])
        else:
            for i, label in enumerate(labels):
                y = 251 + i * 113
                output += rect(x, y, width, 77, SURFACE_1, colors[i], 13, 1.5)
                output += rect(x, y, 8, 77, colors[i], radius=4)
                output += text(x + 27, y + 47, label, 21, TEXT_PRIMARY, 750)
                if i < 3: output += arrow(300, y + 82, 300, y + 106, colors[i])
        return output
    if key == 'rules':
        output = ''
        for i, (label, x) in enumerate(zip(labels, (51, 266, 481, 696, 911))):
            output += node(x, 240, 190, 91, label, colors[i], size=16)
            if i < 4: output += arrow(x + 193, 286, x + 212, 286, colors[i])
        output += text(53, 358, 'READ PATH' if labels[0] == 'PUBLIC VIEW' else 'ПРЕГЛЕД', 14, BLUE, 700)
        output += text(1127, 358, 'CONTROLLED WRITE' if labels[0] == 'PUBLIC VIEW' else 'КОНТРОЛИРАН ЗАПИС', 14, VIOLET, 700, 'end')
        return output
    if key == 'dmv':
        output = node(62, 255, 175, 67, labels[0], colors[0], size=17)
        output += node(283, 237, 216, 102, labels[1], colors[1], size=19)
        output += circle(626, 288, 66, SURFACE_1, AMBER, 2)
        output += text(626, 294, labels[2], 18, TEXT_PRIMARY, 750, 'middle')
        output += node(763, 234, 167, 67, labels[3], colors[3], size=18)
        output += node(947, 303, 165, 58, labels[4], colors[4], size=17)
        output += arrow(242, 288, 277, 288, BLUE) + arrow(502, 288, 553, 288, CYAN)
        output += arrow(695, 270, 756, 270, AMBER) + arrow(692, 311, 940, 331, AMBER)
        return output
    if key == 'registry':
        output = ''
        for i, label in enumerate(labels):
            x = (57, 327, 645, 924)[i]
            width = (226, 271, 234, 222)[i]
            output += rect(x, 242, width, 96, SURFACE_1, colors[i], 12, 1.7)
            output += rect(x, 242, width, 8, colors[i], radius=4)
            output += text(x + width/2, 298, label, 17, TEXT_PRIMARY, 750, 'middle')
            if i < 3: output += arrow(x + width + 5, 291, (57, 327, 645, 924)[i+1] - 7, 291, colors[i])
        output += text(600, 359, 'VALIDATE  /  RECORD  /  AUDIT' if labels[0] == 'TABLET' else 'ПРОВЕРКА  /  ЗАПИС  /  ОДИТ', 14, TEXT_MUTED, 700, 'middle')
        return output
    output = ''
    for i, label in enumerate(labels):
        y = 221 + i * 37
        output += rect(61, y, 1060, 31, SURFACE_1, colors[i], 6, 1.2)
        output += rect(61, y, 8, 31, colors[i], radius=3)
        output += text(88, y + 22, label, 16, TEXT_PRIMARY, 750)
        output += text(1097, y + 22, ('CONTRIBUTION LAYER' if i == 2 else 'SYSTEM LAYER') if labels[0] == 'CLIENT' else ('СЛОЙ НА ПРИНОС' if i == 2 else 'СИСТЕМЕН СЛОЙ'), 13, TEXT_MUTED, 650, 'end')
    return output


def feature(case: dict[str, Any], key: str, project: dict[str, Any], lang: str, mobile: bool) -> str:
    copy=case[lang]; accent=ACCENTS[case['accent']]
    title_lines=wrap(copy['title'],24 if mobile else 42)
    shift=56*(len(title_lines)-1) if mobile else 0
    w,h=(600,780+shift) if mobile else (1200,440)
    body=f'<ellipse cx="{w-70}" cy="95" rx="260" ry="160" fill="url(#aura)"/>'
    body+=text(40,49,'02 / FEATURED SYSTEM' if lang=='en' else '02 / ОСНОВНА СИСТЕМА',18,accent,800,spacing=2)
    title_size=43 if mobile else 57
    body+=lines(40,105,title_lines,title_size,TEXT_PRIMARY,800,title_size+9)
    subtitle_y=105+(len(title_lines)-1)*(title_size+9)+43
    body+=text(42,subtitle_y,copy['eyebrow'],19 if mobile else 21,accent,700,spacing=1)
    role = {'personal':'PERSONAL / OWNER','organization':'ORG / CONTRIBUTOR','collaborative':'SHARED / CONTRIBUTOR'}[project['ownership']]
    if lang=='bg': role={'personal':'ЛИЧЕН / АВТОР','organization':'ОРГ. / ПРИНОС','collaborative':'СЪВМЕСТЕН / ПРИНОС'}[project['ownership']]
    if mobile:
        body+=panel(31,188+shift,538,525,accent,SURFACE_0,22)
        body+=text(57,223+shift,'SYSTEM MAP / VERIFIED COMPONENTS' if lang=='en' else 'СИСТЕМНА КАРТА / ПОТВЪРДЕНИ ЧАСТИ',16,TEXT_SECONDARY,700,spacing=1)
    else:
        body+=panel(31,170,1138,210,accent,SURFACE_0,22)
        body+=text(56,207,'SYSTEM MAP / VERIFIED COMPONENTS' if lang=='en' else 'СИСТЕМНА КАРТА / ПОТВЪРДЕНИ ЧАСТИ',17,TEXT_SECONDARY,700,spacing=1)
    labels={
        'codeguard':(['PROJECT','SCAN ENGINE','FINDINGS','REVIEW','APPLY'],['ПРОЕКТ','СКЕНЕР','НАХОДКИ','ПРЕГЛЕД','ПРИЛАГАНЕ']),
        'rules':(['PUBLIC VIEW','NEXT.JS','DISCORD AUTH','EDITOR','DATABASE'],['ПУБЛИЧЕН ИЗГЛЕД','NEXT.JS','DISCORD ВХОД','РЕДАКТОР','БАЗА ДАННИ']),
        'dmv':(['PLAYER','NUI TABLET','LUA SERVER','QBOX','MYSQL'],['ИГРАЧ','NUI ТАБЛЕТ','LUA СЪРВЪР','QBOX','MYSQL']),
        'registry':(['TABLET','SERVER CHECK','RECORDS','ACTIVITY LOG'],['ТАБЛЕТ','СЪРВЪРНА ПРОВЕРКА','ЗАПИСИ','ЖУРНАЛ']),
        'collaboration':(['CLIENT','SERVER RESOURCES','SHARED WORK','PERSISTENCE'],['КЛИЕНТ','СЪРВЪРНИ РЕСУРСИ','ОБЩА РАБОТА','ДАННИ']),
    }[key][lang=='bg']
    palettes={
        'codeguard':[BLUE,PURPLE,RED,VIOLET,CYAN],
        'rules':[BLUE,PURPLE,AMBER,VIOLET,CYAN],
        'dmv':[BLUE,CYAN,AMBER,GREEN,CYAN],
        'registry':[BLUE,RED,CYAN,GREEN],
        'collaboration':[BLUE,PURPLE,AMBER,CYAN],
    }
    flow=_system_map(key,labels,palettes[key],mobile)
    body+=f'<g transform="translate(0,{shift})">{flow}</g>' if mobile and shift else flow
    if key=='codeguard':
        body+=text(52,700+shift,'OPTIONAL: OPENAI / ANTHROPIC' if lang=='en' else 'ПО ИЗБОР: OPENAI / ANTHROPIC',15,VIOLET,700) if mobile else pill(880,178,'OPTIONAL AI PROPOSAL' if lang=='en' else 'AI ПРЕДЛОЖЕНИЕ ПО ИЗБОР',255,VIOLET,14)
    if mobile:
        body+=text(40,742+shift,role,17,accent,700,spacing=1)
    else:
        body+=text(40,413,role,17,accent,700,spacing=1)
        body+=text(1160,413,'DIAGRAM / NOT A PRODUCT SCREENSHOT' if lang=='en' else 'СХЕМА / НЕ Е КАДЪР ОТ ПРИЛОЖЕНИЕ',14,TEXT_MUTED,700,'end')
    return document(w,h,copy['title']+' system map',copy['build']+' Diagram, not a product screenshot.',body,accent,CYAN,True)


def archive_group(projects: list[dict[str, Any]], category: str, lang: str, mobile: bool) -> str:
    items=sorted((p for p in projects if p['category']==category),key=lambda p:p['name'])
    accent=CATEGORY_ACCENTS[category]
    columns=1 if mobile else 2
    rows=math.ceil(len(items)/columns)
    w=600 if mobile else 1200
    top=112; card_h=104 if mobile else 100; gap=12
    h=top+rows*(card_h+gap)+20
    category_name=CATEGORY_BG[category] if lang=='bg' else category
    body=text(31,45,category_name.upper(),24,accent,800,spacing=1)
    body+=text(31,78,f'{len(items):02d} / '+('ПРОВЕРЕНИ ПРОЕКТА' if lang=='bg' else 'VERIFIED PROJECTS'),18,TEXT_MUTED,700)
    for i,p in enumerate(items):
        col=i%columns; row=i//columns
        x=30+col*580; y=top+row*(card_h+gap); cw=540 if mobile else 550
        body+=panel(x,y,cw,card_h,accent,SURFACE_0,13)
        name=NAMES_BG.get(p['name'],p['name']) if lang=='bg' else p['name']
        name_size=19 if len(name)>37 else 21
        body+=text(x+18,y+32,name,name_size,TEXT_PRIMARY,700)
        tech=' / '.join(p['technologies'][:3]) or ('Документация' if lang=='bg' else 'Documentation')
        body+=text(x+18,y+62,tech,15,TEXT_SECONDARY,500)
        role={'personal':'Личен' if lang=='bg' else 'Personal','organization':'Принос' if lang=='bg' else 'Contributor','collaborative':'Съвместен' if lang=='bg' else 'Collaborative'}[p['ownership']]
        availability='Публичен' if lang=='bg' else 'Public' if p['visibility']=='public' else 'Частен код' if lang=='bg' else 'Private source'
        if p['visibility']=='private': availability='Частен код' if lang=='bg' else 'Private source'
        body+=text(x+18,y+88,f'{role}  /  {availability}',14,accent,700)
    return document(w,h,category_name+' project archive',f'{len(items)} verified project records with role, technology and availability.',body,accent,CYAN)
