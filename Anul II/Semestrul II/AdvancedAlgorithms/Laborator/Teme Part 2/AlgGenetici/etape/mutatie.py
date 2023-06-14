def mutatie(cromozom: str, indici: tuple[int], nr_mutatii: int):
    """
    Functia de mutatie
    :param cromozom: cromozomul de mutat
    :param indici: indicii pe care se realizeaza mutatia
    :param nr_mutatii: numarul de biti de mutat
    :return: cromozomul mutat
    """
    for indice in indici:
        cromozom = (
            cromozom[:indice]
            + ("1" if cromozom[indice] == "0" else "0")
            + cromozom[indice + 1 :]
        )
        nr_mutatii -= 1
        if nr_mutatii == 0:
            return cromozom


if __name__ == "__main__":
    l, k = map(int, input().split())
    cromozom = input()
    indici_mutatie = tuple(map(int, input().split()))

    print(mutatie(cromozom, indici_mutatie, k))
