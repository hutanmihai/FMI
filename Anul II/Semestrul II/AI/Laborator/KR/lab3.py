class NodArbore:
    def __init__(self, info, parinte=None, g=0, h=0):
        self.info = info
        self.parinte = parinte
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def drumRadacina(self):
        l = []
        nod = self
        while nod is not None:
            l.insert(0, nod)
            nod = nod.parinte
        return l

    def vizitat(self):
        nod = self.parinte
        while nod is not None:
            if nod.info == self.info:
                return True
            nod = nod.parinte
        return False

    def __str__(self):
        return f"{self.info} ({self.g}, {self.h})"

    def __repr__(self):
        return "({}, ({}), cost: {})".format(
            self.info, "->".join([str(x) for x in self.drumRadacina()]), self.f
        )


class Graf:
    def __init__(self, matr, start, scopuri, h):
        self.matr = matr
        self.start = start
        self.scopuri = scopuri
        self.estimari = h

    def scop(self, infoNod):
        return infoNod in self.scopuri

    def succesori(self, nod):
        l = []
        for i in range(len(self.matr)):
            if self.matr[nod.info][i] != 0:
                nodNou = NodArbore(
                    i, nod, nod.g + self.matr[nod.info][i], self.calculeaza_h(i)
                )
                if not nodNou.vizitat():
                    l.append(nodNou)
        return l

    def calculeaza_h(self, info):
        return self.estimari[info]


def breadth_first(gr, nsol):
    c = [NodArbore(gr.start)]
    while c:
        nodCurent = c.pop(0)
        if gr.scop(nodCurent.info):
            print(repr(nodCurent))
            nsol -= 1
            if nsol == 0:
                return
        lSuccesori = gr.succesori(nodCurent)
        c += lSuccesori


def bin_search(listaNoduri, nodNou, ls, ld):
    if len(listaNoduri) == 0:
        return 0
    if ls == ld:
        if nodNou.f < listaNoduri[ls].f:
            return ls
        elif nodNou.f > listaNoduri[ls].f:
            return ld + 1
        else:  # f-uri egale
            if nodNou.g < listaNoduri[ls].g:
                return ld + 1
            else:
                return ls
    else:
        mij = (ls + ld) // 2
        if nodNou.f < listaNoduri[mij].f:
            return bin_search(listaNoduri, nodNou, ls, mij)
        elif nodNou.f > listaNoduri[mij].f:
            return bin_search(listaNoduri, nodNou, mij + 1, ld)
        else:
            if nodNou.g < listaNoduri[mij].g:
                return bin_search(listaNoduri, nodNou, mij + 1, ld)
            else:
                return bin_search(listaNoduri, nodNou, ls, mij)


def aStarSolMultiple(gr, nrSolutiiCautate=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodArbore(gr.start)]

    while len(c) > 0:
        # print("Coada actuala: " + str(c))
        # input()
        nodCurent = c.pop(0)

        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("cost:", nodCurent.g)
            print("\n----------------\n")
            # input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        # [2,4,7,8,10,14]
        # c+=gr.succesori(nodCurent)
        for s in gr.succesori(nodCurent):
            indice = bin_search(c, s, 0, len(c) - 1)
            if indice == len(c):
                c.append(s)
            else:
                c.insert(indice, s)


def a_star(graf):
    open_list = [NodArbore(graf.start)]
    closed_list = []

    while open_list:
        nod_curent = open_list.pop(0)
        closed_list.append(nod_curent)

        if graf.scop(nod_curent.info):
            drum = nod_curent.drumRadacina()
            print("Solutie:")
            print(("->").join([str(n.info) for n in drum]))
            print("Cost:", nod_curent.g)
            return

        succesori = graf.succesori(nod_curent)
        for s in succesori:
            in_open = False
            in_closed = False

            for nod in open_list:
                if nod.info == s.info:
                    in_open = True
                    if s.f < nod.f:  # actualizam f si parintele nodului din open_list
                        nod.g = s.g
                        nod.h = s.h
                        nod.f = s.f
                        nod.parinte = s.parinte
                        # Repozitionam nodul in lista astfel incat sa ramana ordonata crescator dupa f
                        open_list.sort(key=lambda x: (x.f, -x.g))
                    break

            for nod in closed_list:
                if nod.info == s.info:
                    in_closed = True
                    if s.f < nod.f:  # actualizam f si parintele nodului din closed_list
                        nod.g = s.g
                        nod.h = s.h
                        nod.f = s.f
                        nod.parinte = s.parinte
                        # Adaugam nodul inapoi in open_list si il scoatem din closed_list
                        open_list.append(nod)
                        closed_list.remove(nod)
                        # Repozitionam nodul in lista astfel incat sa ramana ordonata crescator dupa f
                        open_list.sort(key=lambda x: (x.f, -x.g))
                    break

            if (
                not in_open and not in_closed
            ):  # daca nu se afla in nicio lista, adaugam in open_list
                open_list.append(s)
                open_list.sort(key=lambda x: (x.f, -x.g))


m = [
    [0, 3, 5, 10, 0, 0, 100],
    [0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 4, 9, 3, 0],
    [0, 3, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 5],
    [0, 0, 3, 0, 0, 0, 0],
]

start = 0
scopuri = [4, 6]
h = [0, 1, 6, 2, 0, 3, 0]

gr = Graf(m, start, scopuri, h)
# aStarSolMultiple(gr, 2)
a_star(gr)
