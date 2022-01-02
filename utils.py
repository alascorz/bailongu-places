import requests
from constants import bcolors


def processar_places(text, index):
    primer = text[index + 7]
    if primer == '1':
        return int(text[index + 7] + text[index + 8])
    else:
        return int(text[index + 7])


def parelles_apuntades(url, titol, cursos, dades_anteriors):
    store_dict = {}
    print('-'*50)
    print(titol.upper())
    print('-' * 50)
    f = requests.get(url)
    text_web = f.text.lower()
    for curs in cursos:
        curs = curs.lower()
        index_curs = text_web.find(curs)
        index_places = text_web.find("queden ", index_curs)
        parelles_actuals = int((14 - processar_places(text_web, index_places)) / 2)
        text_mostrar = curs.capitalize() + ': ' + str(parelles_actuals)
        if curs in dades_anteriors.keys():
            diferencia_places = parelles_actuals - dades_anteriors[curs]
            if diferencia_places > 0:
                diferencia = f" {bcolors.OKGREEN}(+"
            elif diferencia_places == 0:
                diferencia = f" (+"
            else:
                diferencia = f" {bcolors.WARNING}("
            diferencia += f"{str(diferencia_places)}){bcolors.ENDC}"
            text_mostrar += diferencia
        print(text_mostrar)
        store_dict.update({curs: parelles_actuals})
    return store_dict
