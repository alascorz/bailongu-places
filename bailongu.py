from utils import parelles_apuntades
from constants import INPUT


def main():
    for (link, titol, curs) in INPUT:
        parelles_apuntades(link, titol, curs)


if __name__ == "__main__":
    main()
