from utils import parelles_apuntades

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



def main():
    parelles_apuntades(LINK_BACHATA_MODERNA, TITOL_BACHATA_MODERNA, CURSOS_BACHATA_MODERNA)
    parelles_apuntades(LINK_BACHATA_SENSUAL, TITOL_BACHATA_SENSUAL, CURSOS_BACHATA_SENSUAL)
    parelles_apuntades(LINK_BALLS_SALO, TITOL_BALLS_SALO, CURSOS_BALLS_SALO)
    parelles_apuntades(LINK_KIZOMBA, TITOL_KIZOMBA, CURSOS_KIZOMBA)
    parelles_apuntades(LINK_RODA_CUBANA, TITOL_RODA_CUBANA, CURSOS_RODA_CUBANA)
    parelles_apuntades(LINK_SALSA, TITOL_SALSA, CURSOS_SALSA)

if __name__ == "__main__":
    main()