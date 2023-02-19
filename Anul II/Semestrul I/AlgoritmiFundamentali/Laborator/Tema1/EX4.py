"""
Acest program foloeste algoritmul lui KOSARAJU.
Acesta consta in parcurgerea grafului cu un dfs si salvarea intr-o coada a nodurilor in ordinea parcursa.
Ulterior vom transpune graful, lucru facut in implementarea mea direct la citire,
iar mai apoi vom scoate unul cate unul nodurile din coada si vom face o noua parcurgere dfs, aceasta parcurgere
va salva in lista de liste numita lista_componente_tare_conexe pe pozitia numarului de componenta tare conexa
la care am ajuns fiecare nod parcurs cu dfs-ul.
Astfel in final voi avea o lista de liste, in care voi avea la fiecare index ce reprezinta numarul componentei tare
conexe gasite, lista nodurilor ce formeaza acea componenta tare conexa.
Complexitate algoritm: O(n+m)
"""


def citire_lista_adiacenta(fisier: str = "ctc.in"):
    with open(fisier) as f:
        nr_noduri, nr_muchii = [int(x) for x in f.readline().split()]
        graf = [[] for _ in range(nr_noduri + 1)]
        rev_graf = [[] for _ in range(nr_noduri + 1)]
        for _ in range(nr_muchii):
            linie = f.readline().split()
            x, y = int(linie[0]), int(linie[1])
            graf[x].append(y)
            rev_graf[y].append(x)
    return graf, rev_graf


graf, rev_graf = citire_lista_adiacenta()
vizitat = set([])
lista_componente_tare_conexe = [[] for _ in range(len(graf))]
coada = []


# Aceasta functie reprezinta prima parcurgere DFS in care salvam in coada nodurile in ordinea parcursa
def ordine(nod):
    vizitat.add(nod)
    for vecin in graf[nod]:
        if vecin not in vizitat:
            ordine(vecin)
    coada.append(nod)


# Aceasta functie reprezinta a doua parcurgere DFS in care salvam nodurile parcurse in lista de componente tare conexe
# conform numarului componentei tare conexe gasite
def dfs_conex(nod):
    vizitat.add(nod)
    lista_componente_tare_conexe[nr_componente_tare_conexe].append(nod)
    for vecin in rev_graf[nod]:
        if vecin not in vizitat:
            dfs_conex(vecin)


if __name__ == "__main__":
    nr_componente_tare_conexe = 0
    # Prima parcurgere dfs
    for i in range(1, len(graf)):
        if i not in vizitat:
            ordine(i)
    # resetam multimea vizitat
    vizitat = set([])

    # rulam al doilea dfs pana coada este goala
    while coada:
        nod = coada.pop()
        if nod not in vizitat:
            nr_componente_tare_conexe += 1
            dfs_conex(nod)

    # afisare
    with open("ctc.out", "w") as f:
        f.write(str(nr_componente_tare_conexe) + "\n")
        for i in range(1, nr_componente_tare_conexe + 1):
            f.write(" ".join(str(x) for x in lista_componente_tare_conexe[i]) + "\n")
