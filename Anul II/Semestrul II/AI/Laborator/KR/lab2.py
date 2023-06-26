class NodArbore:
    def __init__(self, info, parinte=None):
        self.info = info
        self.parinte = parinte

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

    def __repr__(self):
        return "{} ({})".format(
            self.info, "->".join([str(x) for x in self.drumRadacina()])
        )

    def __str__(self):
        return str(self.info)

    def afisSolFisier(self, f):
        def startAfisare(pozBarca, nrMisionari, nrCanibali):
            if pozBarca == 1:
                return f"(Stanga: <barca>) {nrCanibali} canibali {nrMisionari} misionari ...... (Dreapta) 0 canibali 0 misionari\n\n"
            else:
                f"(Stanga) 0 canibali 0 misionari ...... (Dreapta: <barca>) {nrCanibali} canibali {nrMisionari} misionari\n\n"

        def afisareMutare(pozBarca, misMutati, canMutati):
            to_write = f">>> Barca s-a deplasat de la malul "
            if pozBarca == 0:
                to_write += f"stang la malul drept cu {misMutati} misionari si {canMutati} canibali.\n"
            else:
                to_write += f"drept pe malul stang cu {misMutati} misionari si {canMutati} canibali.\n"
            return to_write

        def afisareRezultatStanga(pozBarca, mis, can):
            if pozBarca == 1:
                return f"(Stanga:<barca>) {mis} misionari {can} canibali ...... "
            else:
                return f"(Stanga) {mis} misionari {can} canibali ...... "

        def afisareRezultatDreapta(pozBarca, mis, can):
            if pozBarca == 1:
                return f"(Dreapta) {mis} misionari {can} canibali\n\n"
            else:
                return f"(Dreapta:<barca>) {mis} misionari {can} canibali\n\n"

        with open(f, "w") as f:
            drum = self.drumRadacina()
            nrMisionari = drum[0].info[0]
            nrCanibali = drum[0].info[1]
            barcaInitiala = drum[0].info[2]

            f.write(startAfisare(barcaInitiala, nrMisionari, nrCanibali))

            for nod in drum[1:]:
                canMutati = abs(nod.info[1] - nod.parinte.info[1])
                misMutati = abs(nod.info[0] - nod.parinte.info[0])

                f.write(afisareMutare(nod.info[2], misMutati, canMutati))

                f.write(
                    afisareRezultatStanga(nod.info[2], nod.info[0], nod.info[1])
                    + afisareRezultatDreapta(
                        nod.info[2],
                        nrMisionari - nod.info[0],
                        nrCanibali - nod.info[1],
                    )
                )


class Graf:
    def __init__(self, start, scopuri):
        self.start = start
        self.scopuri = scopuri

    def scop(self, informatieNod):
        return informatieNod in self.scopuri

    def succesori(self, nod):
        def test(m, c):
            return m == 0 or m >= c

        l = []
        if nod.info[2] == 1:  # mal initial = mal curent (cu barca)
            misMalCurent = nod.info[0]
            canMalCurent = nod.info[1]
            misMalOpus = Graf.N - nod.info[0]
            canMalOpus = Graf.N - nod.info[1]
        else:
            misMalCurent = Graf.N - nod.info[0]
            canMalCurent = Graf.N - nod.info[1]
            misMalOpus = nod.info[0]
            canMalOpus = nod.info[1]

        maxMisionariBarca = min(Graf.M, misMalCurent)

        for misBarca in range(maxMisionariBarca + 1):
            if misBarca == 0:
                minCanBarca = 1
                maxCanBarca = min(Graf.M, canMalCurent)
            else:
                minCanBarca = 0
                maxCanBarca = min(misBarca, Graf.M - misBarca, canMalCurent)

            misMalCurentNou = misMalCurent - misBarca
            misMalOpusNou = misMalOpus + misBarca

            for canBarca in range(minCanBarca, maxCanBarca + 1):
                canMalCurentNou = canMalCurent - canBarca
                canMalOpusNou = canMalOpus + canBarca

                if not test(misMalCurentNou, canMalCurentNou) or not test(
                    misMalOpusNou, canMalOpusNou
                ):
                    continue

                if nod.info[2] == 1:
                    infoNou = (misMalCurentNou, canMalCurentNou, 0)
                else:
                    infoNou = (misMalOpusNou, canMalOpusNou, 1)

                nodNou = NodArbore(infoNou, nod)
                if not nodNou.vizitat():
                    l.append(nodNou)
        return l


def BreadthFirst(graf, nrSolutii):
    coada = [NodArbore(graf.start)]
    while coada:
        nodCurent = coada.pop(0)
        if graf.scop(nodCurent.info):
            nodCurent.afisSolFisier("output.txt")
            nrSolutii -= 1
            if nrSolutii == 0:
                return
        listaSuccesori = graf.succesori(nodCurent)
        coada.extend(listaSuccesori)


with open("input.txt", "r") as f:
    continut = f.read().strip().split()
Graf.N = int(continut[0])
Graf.M = int(continut[1])

start = (Graf.N, Graf.N, 1)
scopuri = [(0, 0, 0)]
gr = Graf(start, scopuri)
BreadthFirst(gr, 2)
