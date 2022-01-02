import requests

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