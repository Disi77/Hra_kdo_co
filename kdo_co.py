# Hra Kdo, S kým, Co dělali ...
from random import choice
import json


def vytvor_slovnik(seznam_otazek):
    '''
    Funkce vytvoří slovník, kde klíče jsou ze seznamu "Seznam otázek"
    a hodnoty zadány uživatelem.
    '''
    slovnik_hra = {}
    for otazka in seznam_otazek:
        seznam_odpovedi = []
        while True:
            odpoved = input('Odpověz na otázku --> {}:  '.format(otazka))
            if odpoved == '':
                break
            seznam_odpovedi.append(odpoved)
        slovnik_hra[otazka.lower()] = list(seznam_odpovedi)

    # jakmile uživatel odpoví na všechny otázky, má možnost dohrát si i odpovědi uložené v hlavním slovníku hry
    if ano_ne('Chceš přidat odpovědi uložené z minulé hry? Ano/Ne: '):
        with open('hra_hlavni_slovnik.txt', encoding='utf') as json_data:
            slovnik_zminula = json.load(json_data)
        for otazka in slovnik_hra:
            if otazka in slovnik_zminula:
                slovnik_hra[otazka].extend(list(slovnik_zminula[otazka]))
    return slovnik_hra


def ano_ne(question):
    '''
    Funkce, která chce po uživateli ano (vrátí True) nebo ne (vrátí False).
    '''
    while True:
        answer = input(question)
        if answer.lower().strip() in ['ano', 'a']:
            return True
        elif answer.lower().strip() in ['ne', 'n']:
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


def vytvor_vetu(slovnik):
    '''
    Program vytvoří větu ze slovníku, kde otázky jsou klíče
    a odpovědi jsou hodnoty.
    Věta bude vytvořena v pořadí, v jakém jsou záznamy ve slovníku.
    '''
    veta = ''
    for klic, zaznam in slovnik.items():
        veta += choice(zaznam) + ' '
    print(veta.strip())


def hra():
    print('''
    Hrajeme hru Kdo, Co, S kým ... postupně budeš odpovídat na otázky
    a na konci si přečteš srandovní větu. Když už nechce odpovídat na
    otázky, zmáčkni ENTER.
    ******************************************************************
    ''')
    seznam_otazek = ['KDO?', 'S KÝM?', 'CO DĚLALI?', 'KDE?', 'KDY?', 'PROČ?']
    slovnik_hra = vytvor_slovnik(seznam_otazek)
    while True:
        vytvor_vetu(slovnik_hra)
        if not ano_ne('Chceš vytvořit novou větu? Ano/Ne: '):
            break
    if ano_ne('Chceš zapsat odpovědi do hlavního slovníku? Ano/Ne: '):
        with open('hra_hlavni_slovnik.txt', mode='w', encoding='utf-8') as soubor:
            soubor.write(json.dumps(slovnik_hra, ensure_ascii=False, indent=2))


hra()
