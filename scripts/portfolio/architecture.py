"""Shared grammar for verified high-level system flows."""
from __future__ import annotations

from theme import (BLUE, CYAN, PURPLE, VIOLET, RED, AMBER, GREEN,
                   TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, SURFACE_0, BORDER_SUBTLE)
from portfolio.svg import document, text, node, panel, rule, arrow, pill

FLOWS = {
    'codeguard': {
        'en': (['LOCAL PROJECT','RUST SCANNER','FINDINGS','REVIEW / APPLY'], 'Optional OpenAI or Anthropic proposal enters the review path.'),
        'bg': (['ЛОКАЛЕН ПРОЕКТ','RUST СКЕНЕР','НАХОДКИ','ПРЕГЛЕД / ПРИЛАГАНЕ'], 'Незадължително предложение от OpenAI или Anthropic влиза в прегледа.'),
        'colors': [GREEN,PURPLE,RED,BLUE], 'branch': ('AI PROPOSAL','AI ПРЕДЛОЖЕНИЕ',VIOLET)},
    'rules': {
        'en': (['PUBLIC READER','NEXT.JS','EDITORIAL FLOW','POSTGRESQL'], 'Discord OAuth gates administration; server-side access checks protect edits.'),
        'bg': (['ПУБЛИЧЕН ЧИТАТЕЛ','NEXT.JS','РЕДАКТОРСКИ ПРОЦЕС','POSTGRESQL'], 'Discord OAuth ограничава администрацията; сървърни проверки пазят редакциите.'),
        'colors': [BLUE,PURPLE,VIOLET,CYAN], 'branch': ('DISCORD OAUTH','DISCORD OAUTH',AMBER)},
    'dmv': {
        'en': (['PLAYER / NUI','LUA SERVER','QBOX','MYSQL'], 'Registration and plate history cross the client/server boundary.'),
        'bg': (['ИГРАЧ / NUI','LUA СЪРВЪР','QBOX','MYSQL'], 'Регистрацията и историята на номерата преминават през границата клиент/сървър.'),
        'colors': [BLUE,PURPLE,GREEN,CYAN], 'branch': None},
    'registry': {
        'en': (['TABLET','SERVER VALIDATION','BUSINESS RECORDS','ACTIVITY LOG'], 'The repository documents server checks and persisted audit records.'),
        'bg': (['ТАБЛЕТ','СЪРВЪРНА ВАЛИДАЦИЯ','БИЗНЕС ЗАПИСИ','ЖУРНАЛ'], 'Хранилището описва сървърни проверки и постоянни одитни записи.'),
        'colors': [BLUE,RED,CYAN,GREEN], 'branch': None},
    'collaboration': {
        'en': (['CLIENT','SERVER RESOURCES','SHARED WORKFLOW','DATA'], 'A high-level map of a shared repository, not a claim of sole authorship.'),
        'bg': (['КЛИЕНТ','СЪРВЪРНИ РЕСУРСИ','ОБЩА РАБОТА','ДАННИ'], 'Обща схема на споделен проект, без твърдение за еднолично авторство.'),
        'colors': [BLUE,PURPLE,AMBER,CYAN], 'branch': None},
}


def render(key: str, lang: str, mobile: bool) -> str:
    config=FLOWS[key]; labels,note=config[lang]
    w,h=(600,690) if mobile else (1200,390)
    accent=config['colors'][1]
    body=text(34,46,('SYSTEM ARCHITECTURE / '+key.upper()) if lang=='en' else ('АРХИТЕКТУРА / '+key.upper()),19,accent,800,spacing=1)
    body+=text(35,82,'TRUST & DATA FLOW' if lang=='en' else 'ГРАНИЦИ И ПОТОК НА ДАННИ',16,TEXT_MUTED,700,spacing=1)
    if mobile:
        body+=panel(29,112,542,466,accent,SURFACE_0,20)
        if key != 'codeguard':
            body+=rule(47,228,47,558,RED,2,'6 6')
            body+=text(60,216,'CLIENT / SERVER BOUNDARY' if lang=='en' else 'ГРАНИЦА КЛИЕНТ / СЪРВЪР',14,RED,700)
        for i,(label,color) in enumerate(zip(labels,config['colors'])):
            y=147+i*102
            body+=node(76,y,448,70,label,color,size=18 if len(label)>20 else 20)
            if i<3: body+=arrow(300,y+73,300,y+99,color)
        branch=config['branch']
        if branch:
            body+=pill(72,593,branch[lang=='bg'],256,branch[2],16)
            body+=text(340,618,'OPTIONAL' if lang=='en' else 'ПО ИЗБОР',16,TEXT_MUTED,700)
        else:
            body+=text(36,618,'VERIFIED HIGH-LEVEL COMPONENTS' if lang=='en' else 'ПОТВЪРДЕНИ ОСНОВНИ ЧАСТИ',16,TEXT_MUTED,700)
        body+=text(36,663,note[:52]+'…' if len(note)>52 else note,16,TEXT_SECONDARY)
    else:
        body+=panel(29,111,1142,220,accent,SURFACE_0,20)
        if key != 'codeguard':
            body+=rule(306,124,306,317,RED,2,'7 7')
            body+=text(316,148,'CLIENT / SERVER BOUNDARY' if lang=='en' else 'ГРАНИЦА КЛИЕНТ / СЪРВЪР',14,RED,700)
        for i,(label,color) in enumerate(zip(labels,config['colors'])):
            x=52+i*278
            body+=node(x,203,244,79,label,color,size=17 if len(label)>18 else 19)
            if i<3: body+=arrow(x+247,243,x+275,243,color)
        branch=config['branch']
        if branch:
            body+=pill(776,120,branch[lang=='bg'],215,branch[2],15)
            body+=text(1010,146,'OPTIONAL' if lang=='en' else 'ПО ИЗБОР',14,TEXT_MUTED,700)
        body+=text(35,365,note,17,TEXT_SECONDARY)
    title=('Architecture of '+key) if lang=='en' else ('Архитектура на '+key)
    return document(w,h,title,note,body,accent,CYAN)
