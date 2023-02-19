"""
Pentru rezolvarea acestei probleme am folosit algortimul DFS pe fiecare nod din graf.
Pentru fiecare nod din graf, calculam recursiv in implementarea DFS-ului suma maxima din nodul curent.
La final rezultatul va fi suma maxima din lista de sume maxime in care am retinut suma maxima incepand din fiecare nod.
Diferenta fata de un DFS obisnuit este faptul ca parcurgem toti vecinii nodului curent indiferent daca au fost vizitati
sau nu, astfel garantand ca vom parcurge toate drumurile posibile si astfel afland suma maxima posibila
din nodul curent.

Complexitatea algoritmului este O(n^2).
"""

import copy
from typing import List


def dfs(nod: int):
    if not vizitat[nod]:
        for vecin in lista_adiacenta[nod]:
            dfs(vecin)
            suma[nod] = max(suma[nod], suma[vecin] + valori[nod])
        vizitat[nod] = True


with open("easygraph.in", 'r') as f:
    nr_teste = int(f.readline())
    for test in range(1, nr_teste + 1):
        n, m = map(int, f.readline().split())
        vizitat: List[bool] = [False] * (n + 1)
        lista_adiacenta: dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
        valori = [0] + [int(x) for x in f.readline().split()]
        suma = copy.deepcopy(valori)

        for muchie in range(m):
            x, y = map(int, f.readline().split())
            lista_adiacenta[x].append(y)

        for nod in range(1, n + 1):
            if not vizitat[nod]:
                dfs(nod)

        suma_maxima = max(suma)

        with open("easygraph.out", 'w') as g:
            g.write(f"{suma_maxima}")
