from utils import parelles_apuntades
from constants import INPUT, PERSISTENCE_FILE_NAME
from datetime import datetime
import json

def main():
    now = datetime.now()
    store_dict = {'date': now.strftime("%m/%d/%Y, %H:%M:%S")}
    for (link, titol, cursos) in INPUT:
        info_cursos = parelles_apuntades(link, titol, cursos)
        store_dict.update(info_cursos)
    contingut = json.dumps(store_dict)
    with open(PERSISTENCE_FILE_NAME, "w") as file:
        file.write(contingut)


if __name__ == "__main__":
    main()
