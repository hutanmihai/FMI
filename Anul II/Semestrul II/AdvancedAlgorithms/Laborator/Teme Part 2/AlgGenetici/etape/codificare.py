from math import ceil, log2, pow


def codificare(numar: float, precizie: float, domeniu: tuple):
    """
    Codificarea unui numar real intr-un numar intreg
    :param numar: numarul real de codificat
    :param precizie: precizia de codificare
    :return: numarul codificat
    """
    lungimea_codificarii = ceil(log2((domeniu[1] - domeniu[0]) * pow(10, precizie)))

    pas_discretizare = (domeniu[1] - domeniu[0]) / pow(2, lungimea_codificarii)

    # Generarea intervalelor de discretizare
    intervale_discretizare = [
        (domeniu[0] + (i - 1) * pas_discretizare, domeniu[0] + i * pas_discretizare)
        for i in range(1, ceil(pow(2, lungimea_codificarii)) + 1)
    ]

    # Determinarea indexului intervalului de discretizare in care se afla numarul
    index = 0
    for i, interval in enumerate(intervale_discretizare):
        if interval[0] <= numar <= interval[1]:
            index = i
            if interval[0] == numar:
                break

    return bin(index)[2:].zfill(lungimea_codificarii)


def decodificare(numar_bin: str, precizie: float, domeniu: tuple):
    """
    Decodificarea unui numar binar intr-un numar real
    :param numar_bin: numarul binar de decodificat
    :param precizie: precizia de codificare folosita initial
    :param domeniu: domeniul de codificare folosit initial
    :return: numarul decodificat
    """
    lungimea_codificarii = ceil(log2((domeniu[1] - domeniu[0]) * pow(10, precizie)))
    pas_discretizare = (domeniu[1] - domeniu[0]) / pow(2, lungimea_codificarii)

    # Generarea intervalelor de discretizare
    intervale_discretizare = [
        (domeniu[0] + (i - 1) * pas_discretizare, domeniu[0] + i * pas_discretizare)
        for i in range(1, ceil(pow(2, lungimea_codificarii)) + 1)
    ]

    # Convertirea numarului binar in numar intreg
    index = int(numar_bin, 2)

    numar_decodificat = intervale_discretizare[index][0]

    return numar_decodificat


if __name__ == "__main__":
    domeniu = tuple(map(int, input().split()))
    precizie = int(input())
    nr_teste = int(input())
    for _ in range(nr_teste):
        comanda = input()
        inp = input()
        if comanda == "TO":
            numar = float(inp)
            print(codificare(numar, precizie, domeniu))
        elif comanda == "FROM":
            numar = inp
            print(decodificare(numar, precizie, domeniu))
