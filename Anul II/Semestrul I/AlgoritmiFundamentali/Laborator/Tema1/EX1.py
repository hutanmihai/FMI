"""
Pentru rezolvarea acestei probleme am folosit un algoritm BFS, diferenta fiind facuta de
utilizarea listei vizitat pentru atribuirea unui nod la un grup.
La fiecare nod verificam daca nodul parinte apartine aceluiasi grup,
daca e adevarat returnam fals, altfel, daca nodul curent nu este atribuit niciunui grup
il vom atribui grupului opus fata de cel al parintelui.
Daca reusim sa trecem prin toate nodurile fara a avea conflict de grupuri, respectiv sa intram in return False,
vom returna True.
Complexitatea algoritmului: O(n+m)
"""

from typing import List


# --------------------------SUBPUNCTUL A----------------------------------
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def citire_lista_adiacenta():
            nr_muchii: int = len(dislikes)
            nr_noduri = n
            lista = [[] for _ in range(nr_noduri + 1)]
            for _ in range(nr_muchii):
                x, y = dislikes[_][0], dislikes[_][1]
                lista[x].append(y)
                lista[y].append(x)
            return lista

        def bfs():
            lista = citire_lista_adiacenta()
            vizitat = [False] * len(lista)
            coada = []
            # Introducem algoritmul clasic BFS in acest for pentru a ne asigura ca trecem prin toate nodurile,
            # respectiv daca avem mai multe componente conexe vom trece prin toate.
            for i in range(1, len(lista)):
                if vizitat[i]:
                    continue
                vizitat[i] = 1
                coada.append(i)
                while coada:
                    nod = coada.pop(0)
                    current_group = vizitat[nod]
                    opposite_group = 1 if current_group == 2 else 2
                    for vecin in lista[nod]:
                        if vizitat[vecin] == current_group:
                            return False
                        if not vizitat[vecin]:
                            coada.append(vecin)
                            vizitat[vecin] = opposite_group
            return True

        return bfs()


# --------------------------SUBPUNCTUL B----------------------------------

"""
Singura diferenta a acestei implementari fata de cea anterioara consta in faptul ca dupa atribuirea grupurilor,
daca reusim sa trecem prin toate nodurile si impartirea in doua grupuri este posibila,
parcurg lista vizitat in care am salvat fiecare nod (indexul) cu grupul de care apartine (valoarea 1 sau 2)
si creez o lista de doua liste, separand astfel cele doua grupuri in cele doua liste 
si putand afisa pe fiecare in parte.
Complexitatea Algoritmului ramane O(n+m)
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def citire_lista_adiacenta():
            nr_muchii: int = len(dislikes)
            nr_noduri = n
            lista = [[] for _ in range(nr_noduri + 1)]
            for _ in range(nr_muchii):
                x, y = dislikes[_][0], dislikes[_][1]
                lista[x].append(y)
                lista[y].append(x)
            return lista

        def bfs():
            lista = citire_lista_adiacenta()
            vizitat = [False] * len(lista)
            coada = []
            for i in range(1, len(lista)):
                if vizitat[i]:
                    continue
                vizitat[i] = 1
                coada.append(i)
                while coada:
                    nod = coada.pop(0)
                    current_group = vizitat[nod]
                    opposite_group = 1 if current_group == 2 else 2
                    for vecin in lista[nod]:
                        if vizitat[nod] == vizitat[vecin]:
                            return False
                        if not vizitat[vecin]:
                            coada.append(vecin)
                            vizitat[vecin] = opposite_group
            groups = [[] for i in range(2)]
            for i in range(1, len(vizitat)):
                if vizitat[i] == 1:
                    groups[0].append(i)
                if vizitat[i] == 2:
                    groups[1].append(i)
            return groups

        return bfs()
