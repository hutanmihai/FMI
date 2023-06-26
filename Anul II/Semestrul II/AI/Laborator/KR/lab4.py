import copy


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
    def __init__(self, start, scopuri):
        self.start = start
        self.scopuri = scopuri
        if not self.valideaza():
            exit(0)

    def scop(self, infoNod):
        return infoNod in self.scopuri

    def succesori(self, nod):
        l = []
        for istiva, stiva in enumerate(nod.info):
            if not stiva:
                continue
            stiveIntermediare = copy.deepcopy(nod.info)
            bloc = stiveIntermediare[istiva].pop()
            for istiva2, stiva2 in enumerate(stiveIntermediare):
                copieStive = copy.deepcopy(stiveIntermediare)
                if istiva == istiva2:
                    continue
                copieStive[istiva2].append(bloc)
                nodNou = NodArbore(copieStive, nod, nod.g + 1)
                if not nodNou.vizitat():
                    nodNou.h = self.calculeaza_h(nodNou, "euristica mutari")
                    l.append(nodNou)
        return l

    def calculeaza_h(self, nod, euristica="banala"):
        if euristica == "banala":
            if self.scop(nod.info):
                return 0
            else:
                return 1

        elif euristica == "euristica mutari":
            minim = float("inf")
            for scop in self.scopuri:
                nb = 0
                for stivaCurenta, stivaScop in zip(nod.info, scop):
                    nb += sum([1 for bloc in stivaCurenta if bloc not in stivaScop])
                minim = min(minim, nb)
            return minim

        elif euristica == "euristica costuri":
            minim = float("inf")
            for scop in self.scopuri:
                cost = 0
                for stivaCurenta, stivaScop in zip(nod.info, scop):
                    for bloc in stivaCurenta:
                        if bloc not in stivaScop:
                            cost += ord(bloc) - ord("A") + 1
                minim = min(minim, cost)
            return minim

        elif euristica == "euristica neadmisibila":
            return float("inf")

    def valideaza(self):
        cond1 = all([len(self.start) == len(scop) for scop in self.scopuri])
        listaBlocuri = sorted(sum(self.start, start=[]))
        cond2 = all(
            [listaBlocuri == sorted(sum(scop, start=[])) for scop in self.scopuri]
        )
        return cond1 and cond2


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
    c = [NodArbore(gr.start)]

    while len(c) > 0:
        nodCurent = c.pop(0)

        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("cost:", nodCurent.g)
            print("\n----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
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
        nodCurent = open_list.pop(0)
        closed_list.append(nodCurent)
        if graf.scop(nodCurent.info):
            print(repr(nodCurent))
            return
        succesori = graf.succesori(nodCurent)
        for s in succesori:
            in_open = False
            in_closed = False

            for nod in open_list:
                if nod.info == s.info:
                    in_open = True
                    if s.f < nod.f:
                        nod.g = s.g
                        nod.h = s.h
                        nod.f = s.f
                        nod.parinte = s.parinte
                        open_list.sort(key=lambda x: (x.f, -x.g))
                    break
            for nod in closed_list:
                if nod.info == s.info:
                    in_closed = True
                    if s.f < nod.f:
                        nod.g = s.g
                        nod.h = s.h
                        nod.f = s.f
                        nod.parinte = s.parinte
                        open_list.append(nod)
                        closed_list.remove(nod)
                        open_list.sort(key=lambda x: (x.f, -x.g))
                    break

            if not in_open and not in_closed:
                open_list.append(s)
                open_list.sort(key=lambda x: (x.f, -x.g))


def calculeazaStive(sirStiva):
    listaSiruriStive = sirStiva.strip().split("\n")
    return [sir.strip().split() if sir != "#" else [] for sir in listaSiruriStive]


with open("input.txt") as f:
    continut = f.read()

sirStart, sirScopuri = continut.strip().split("=========")
start = calculeazaStive(sirStart)
siruriScopuri = sirScopuri.split("---")
scopuri = [calculeazaStive(sir) for sir in siruriScopuri]

gr = Graf(start, scopuri)
a_star(gr)

# a
# c b
# d
# =========
# b c
# #
# d a
# ---
# a b c d
# #
# #
# ---
# #
# #
# d b c a
# ---
# c b d a
# #
# #
