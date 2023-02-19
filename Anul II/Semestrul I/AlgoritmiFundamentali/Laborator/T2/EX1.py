"""
Pentru rezolvarea acestei probleme am folosit algoritmul lui Prim. Intai calculam distanta minima de la fiecare bloc
la cea mai apropiata centrala. Iar mai apoi, nodurile ramase nevizitate le conectam la cei mai apropiati
vecini. Am garantat minim o centrala deoarece la prima iteratie se va adauga distanta minima din lista de distante
bloc-centrala. Iar mai apoi, algoritmul lui Prim genereaza arborele partial de cost minim cu minim o centrala.

Complexitatea algoritmului este O(n^2) .
"""

import math
from typing import List


def distanta_euclidiana(x: tuple[int, int], y: tuple[int, int]) -> float:
    return math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)


if __name__ == "__main__":
    with open("retea.in", 'r') as f:
        n, m = map(int, f.readline().split())
        centrale: List[tuple[int, int]] = []
        blocuri: List[tuple[int, int]] = []
        # distanta fiecarui nod pana la cea mai apropiata centrala
        distanta_centrala: List[float] = [float('inf')] * m
        vizitat: List[bool] = [False] * m
        distanta_finala: List[float] = [float('inf')] * m
        distanta_totala: float = 0
        # citirea datelor
        for i in range(n):
            x, y = map(int, f.readline().split())
            centrale.append((x, y))
        for i in range(m):
            x, y = map(int, f.readline().split())
            blocuri.append((x, y))

    # calculam distanta de la fiecare bloc la cea mai apropiata centrala
    for i in range(m):
        for j in range(n):
            distanta_centrala[i] = min(distanta_centrala[i], distanta_euclidiana(blocuri[i], centrale[j]))
        distanta_finala[i] = distanta_centrala[i]

    for i in range(m):
        dist: float = float('inf')
        ultim: int = -1
        # pentru fiecare nod care nu a fost vizitat il conectam la cel mai apropiat nod
        # calculam distantele intre blocuri
        for j in range(m):
            if not vizitat[j] and distanta_finala[j] < dist:
                dist = distanta_finala[j]
                ultim = j
        # crestem distanta totala
        distanta_totala += dist
        # modificam distanta_finala cu minimul dintre valorile existente si cele noi calculate
        for j in range(m):
            distanta_finala[j] = min(distanta_finala[j],
                                     distanta_centrala[j] + distanta_euclidiana(blocuri[j], blocuri[ultim]))
        vizitat[ultim] = True

    with open("retea.out", 'w') as g:
        g.write("%.6f" % distanta_totala)
