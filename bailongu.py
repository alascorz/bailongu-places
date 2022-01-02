from utils import parelles_apuntades
from constants import INPUT, PERSISTENCE_FILE_NAME
from datetime import datetime
import json
from os.path import exists

def main():
    # Obtain previous values from execution
    if exists(PERSISTENCE_FILE_NAME):
        with open(PERSISTENCE_FILE_NAME) as file:
            dades_anteriors = json.load(file)
        print('Comparant dades amb les del ' + dades_anteriors['data'])
    else:
        dades_anteriors = {}

    # Store current date and time
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    store_dict = {'data': now}

    # Search and process dance classes
    for (link, titol, cursos) in INPUT:
        info_cursos = parelles_apuntades(link, titol, cursos, dades_anteriors)
        store_dict.update(info_cursos)

    # Store current values
    contingut = json.dumps(store_dict)
    with open(PERSISTENCE_FILE_NAME, "w") as file:
        file.write(contingut)


if __name__ == "__main__":
    main()
