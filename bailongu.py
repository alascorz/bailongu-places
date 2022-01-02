import requests

LINK_BACHATA_MODERNA = 'https://bailongu.com/cursos-ball-barcelona/bachata?term=177&nC=39%3A36%3A32%3A12'
TITOL_BACHATA_MODERNA = 'Bachata moderna'
CURSOS_BACHATA_MODERNA = ['BACHATA MODERNA 2 DILLUNS 22-23H', 'BACHATA MODERNA 3 DIJOUS 21-22H']

LINK_BACHATA_SENSUAL = 'https://bailongu.com/cursos-ball-barcelona/bachata-sensual-1?term=177&nC=39%3A36%3A32%3A12'
TITOL_BACHATA_SENSUAL = 'Bachata sensual'
CURSOS_BACHATA_SENSUAL = ['BACHATA SENSUAL 1 DIMECRES 22-23H']

LINK_BALLS_SALO = 'https://bailongu.com/cursos-ball-barcelona/balls-de-salo?term=177&nC=39%3A36%3A32%3A12'
TITOL_BALLS_SALO = 'Balls de saló'
CURSOS_BALLS_SALO = ['BALLS DE SALÓ 1 DILLUNS 20-21H', 'BALLS DE SALÓ 1 DIMARTS 21-22H']

LINK_KIZOMBA = 'https://bailongu.com/cursos-ball-barcelona/kizomba?term=177&nC=39%3A36%3A32%3A12'
TITOL_KIZOMBA = 'Kizomba'
CURSOS_KIZOMBA = ['KIZOMBA 1 DIJOUS 20-21H']

LINK_RODA_CUBANA = 'https://bailongu.com/cursos-ball-barcelona/roda-cubana?term=177&nC=39%3A36%3A32%3A12'
TITOL_RODA_CUBANA = 'Roda cubana'
CURSOS_RODA_CUBANA = ['RODA CUBANA 1 DIJOUS 22-23H']

LINK_SALSA = 'https://bailongu.com/cursos-ball-barcelona/salsa?term=177&nC=39%3A36%3A32%3A12'
TITOL_SALSA = 'Salsa cubana'
CURSOS_SALSA = ['SALSA CUBANA 2 DIMARTS 22-23H', 'SALSA CUBANA 2 DIMECRES 21-22H']

def processar_places(text, index):
    primer = text[index + 7]
    if primer == '1':
        return int(text[index + 7] + text[index + 8])
    else:
        return int(text[index + 7])

def parelles_apuntades(url, titol, cursos):
    print('-'*50)
    print(titol.upper())
    print('-' * 50)
    f = requests.get(url)
    text_web = f.text.lower()
    for curs in cursos:
        curs = curs.lower()
        index_curs = text_web.find(curs)
        index_places = text_web.find('queden ', index_curs)
        places_restant = int((14 - processar_places(text_web, index_places)) / 2)
        print(curs.capitalize() + ': ' + str(places_restant))

parelles_apuntades(LINK_BACHATA_MODERNA, TITOL_BACHATA_MODERNA, CURSOS_BACHATA_MODERNA)
parelles_apuntades(LINK_BACHATA_SENSUAL, TITOL_BACHATA_SENSUAL, CURSOS_BACHATA_SENSUAL)
parelles_apuntades(LINK_BALLS_SALO, TITOL_BALLS_SALO, CURSOS_BALLS_SALO)
parelles_apuntades(LINK_KIZOMBA, TITOL_KIZOMBA, CURSOS_KIZOMBA)
parelles_apuntades(LINK_RODA_CUBANA, TITOL_RODA_CUBANA, CURSOS_RODA_CUBANA)
parelles_apuntades(LINK_SALSA, TITOL_SALSA, CURSOS_SALSA)