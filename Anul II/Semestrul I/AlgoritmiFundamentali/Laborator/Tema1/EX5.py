"""
In acest program incepem cate un BFS din fiecare nod (resetam vectorul vizitat si distanta), iar in interiorul
acestui bfs calculam distantele de la nodul de plecare pana la fiecare nod, iar mai apoi returnam minimul din vectorul
distanta filtrandu-l pe acesta astfel incat sa avem doar distantele pana la puncte de control.
Astfel la fiecare iteratie a BFS-ului vom obtine distanta pana la cel mai apropiat punct de control.
Complexitatea algoritmului este: O(n*(n+m))
"""


def citire_lista_adiacenta(fisier: str = "graf.in"):
    with open(fisier) as f:
        nr_noduri, nr_muchii = [int(x) for x in f.readline().split()]
        lista = [[] for _ in range(nr_noduri + 1)]
        for _ in range(nr_muchii):
            linie = f.readline().split()
            x, y = int(linie[0]), int(linie[1])
            lista[x].append(y)
            lista[y].append(x)
        puncte_control = [int(x) for x in f.readline().split()]
    return lista, puncte_control


ls_graf, ls_pct_control = citire_lista_adiacenta()
vizitat = set([])
coada = []
distanta = [0] * len(ls_graf)


def bfs(i):
    coada.append(i)
    vizitat.add(i)
    distanta = [0] * len(ls_graf)
    distanta[i] = 0
    while coada:
        nod = coada.pop(0)
        for vecin in ls_graf[nod]:
            if vecin not in vizitat:
                coada.append(vecin)
                vizitat.add(vecin)
                distanta[vecin] = distanta[nod] + 1
    # returnam distanta cea mai scurta pana la un punct de control din nodul de start
    return min(distanta[i] for i in ls_pct_control)


if __name__ == "__main__":
    with open("graf.out", "w") as f:
        for nod in range(1, len(ls_graf)):
            # resetam vizitat coada si distanta pentru urmatoarea iteratie
            vizitat.clear()
            coada.clear()
            distanta.clear()
            # in res vom primi distanta minima
            res = bfs(nod)
            # scriem la fiecare iteratie distanta cea mai scurta pana la un punct de control
            f.write(str(res) + " ")

# expected output -> 2 1 3 2 2 1 2 0 0
