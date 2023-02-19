"""
Pentru rezolvarea acestei probleme am folosit parcurgere DFS obisnuita, diferenta fiind facuta
de faptul ca am sortat fiecare lista de vecini din lista de adiacenta in conformitate cu
lista de ordine pe care o avem din input, astfel fortand dfs-ul sa mearga in directia dorita intotdeauna.
La fiecare iteratie a DFS-ului adaugam nodul in care ne aflam la o lista numita final, pe care in final o comparam
cu inputul ce ne da ordinea dorita.
Complexitatea algoritmului: O(n log n)
"""

# folosim aceasta functie deoarece python trimite eroare pe unele exemple din cauza numarului prea mare de
# intrati in recursivitate, am ales 100001 deoarece pe site cel mai mare exemplu are 100000 de noduri
# si in cazul cel mai nefavorabil acesta va fi numarul de intrari in recursivitate
import sys

sys.setrecursionlimit(100001)


def citire_lista_adiacenta():
    nr_noduri, nr_muchii = [int(x) for x in input().split()]
    ordine = [int(x) for x in input().split()]
    lista = [[] for _ in range(nr_noduri + 1)]
    for _ in range(nr_muchii):
        linie = input().split()
        x, y = int(linie[0]), int(linie[1])
        lista[x].append(y)
        lista[y].append(x)
    return lista, ordine


lista, ordine = citire_lista_adiacenta()

# Urmatoarele bloc de cod a fost implementat manual, in locul folosirii functiei index din python in sortare
# deoarece este mai eficienta si astfel alg reuseste sa se incadreze in cele 2500ms.

# Generam lista cu pozitiile nodurilor in permutare
poz = [0] * len(lista)
for i in range(len(lista) - 1):
    poz[ordine[i]] = i


# Sortam dupa pozitia nodului in permutare
def sortare_lista_adiacenta():
    for lista_nod in lista:
        lista_nod.sort(key=lambda x: poz[x])


def dfs(nod):
    vizitat[nod] = 1
    final.append(nod)
    for vecin in lista[nod]:
        if vizitat[vecin] == 0:
            dfs(vecin)


vizitat = [0] * len(lista)
final = []
sortare_lista_adiacenta()
dfs(1)
# Verificam daca parcurgerea a fost facuta in aceeasi ordine precum permutarea data la input
if final == ordine:
    print(1)
else:
    print(0)
