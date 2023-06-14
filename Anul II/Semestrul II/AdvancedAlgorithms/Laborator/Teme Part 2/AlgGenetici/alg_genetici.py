import copy
from math import ceil, log2, pow
from random import uniform, random, randint, shuffle
from statistics import mean


class Individ:
    def __init__(
        self,
        valoare: float | None = None,
        cromozom: str | None = None,
    ):
        self.valoare = valoare
        self.cromozom = cromozom
        self.valoare = (
            self.decodificare(precizie=PRECIZIE, domeniu=DOMENIU)
            if self.valoare is None
            else self.valoare
        )
        self.cromozom = (
            self.codificare(precizie=PRECIZIE, domeniu=DOMENIU)
            if self.cromozom is None
            else self.cromozom
        )
        self.fitness = self.fit(coeficienti=COEFICIENTI)

    def __str__(self):
        return f"{self.cromozom} --> x = {self.valoare} --> fit = {self.fitness}"

    def __repr__(self):
        return f"{self.cromozom} --> x = {self.valoare} --> fit = {self.fitness}"

    def set_cromozom(self, cromozom: str):
        self.cromozom = cromozom
        self.valoare = self.decodificare(precizie=PRECIZIE, domeniu=DOMENIU)
        self.fitness = self.fit(coeficienti=COEFICIENTI)

    def codificare(self, precizie: int, domeniu: tuple):
        """
        Codificarea unui numar real intr-un numar binar
        :param precizie: precizia de codificare
        :param domeniu: domeniul de codificare
        :return: numarul codificat
        """
        lungimea_codificarii = ceil(log2((domeniu[1] - domeniu[0]) * pow(10, precizie)))

        pas_discretizare = (domeniu[1] - domeniu[0]) / pow(2, lungimea_codificarii)

        # Generarea intervalelor de discretizare
        intervale_discretizare = [
            (
                domeniu[0] + (i - 1) * pas_discretizare,
                domeniu[0] + i * pas_discretizare,
            )
            for i in range(1, ceil(pow(2, lungimea_codificarii)) + 1)
        ]

        # Determinarea indexului intervalului de discretizare in care se afla numarul
        index = 0
        for i, interval in enumerate(intervale_discretizare):
            if interval[0] <= self.valoare <= interval[1]:
                index = i
                if interval[0] == self.valoare:
                    break

        return bin(index)[2:].zfill(lungimea_codificarii)

    def decodificare(self, precizie: int, domeniu: tuple):
        """
        Decodificarea unui numar binar intr-un numar real
        :param precizie: precizia de codificare folosita initial
        :param domeniu: domeniul de codificare folosit initial
        :return: numarul decodificat
        """
        lungimea_codificarii = ceil(log2((domeniu[1] - domeniu[0]) * pow(10, precizie)))
        pas_discretizare = (domeniu[1] - domeniu[0]) / pow(2, lungimea_codificarii)

        # Generarea intervalelor de discretizare
        intervale_discretizare = [
            (
                domeniu[0] + (i - 1) * pas_discretizare,
                domeniu[0] + i * pas_discretizare,
            )
            for i in range(1, ceil(pow(2, lungimea_codificarii)) + 1)
        ]

        # Convertirea numarului binar in numar intreg
        index = int(self.cromozom, 2)

        numar_decodificat = intervale_discretizare[index][0]

        return numar_decodificat

    def fit(self, coeficienti: tuple):
        return (
            coeficienti[0] * pow(self.valoare, 2)
            + coeficienti[1] * self.valoare
            + coeficienti[2]
        )


class Populatie:
    def __init__(self, populatie: list[Individ] = None, fitness: list[float] = None):
        self.populatie = populatie or []
        self.fitness = fitness or []
        self.intervale_selectie = [0]
        self.probabilitate_selectie = []

    def genereaza_populatie_random(
        self, dimensiune: int, domeniu: tuple, write: bool = False
    ):
        print("POPULATIE INITIALA:", file=out) if write else None
        for _ in range(dimensiune):
            val_random = uniform(domeniu[0], domeniu[1])
            self.populatie.append(Individ(valoare=val_random))
            print(f"\t{_ + 1}: {self.populatie[-1]}", file=out) if write else None
        print(file=out) if write else None

    def fit(self, max_and_mean: bool = False):
        self.fitness = [individ.fitness for individ in self.populatie]
        if max_and_mean:
            print("MAX: ", max(self.fitness), file=out)
            print("MEAN: ", mean(self.fitness), file=out)
            print(file=out)

    def selectie(self, dimensiune: int, write: bool = False):
        def top_n_indici(lista, n):
            return sorted(range(len(lista)), key=lambda i: lista[i])[-n:][::-1]

        fitness_sum = sum(self.fitness)
        for i, fit in enumerate(self.fitness):
            suma_partiala = sum(self.fitness[: i + 1])
            self.intervale_selectie.append(suma_partiala / fitness_sum - 5e-5)

        print("PROBABILITATE SELECTIE:", file=out) if write else None
        for i, fit in enumerate(self.fitness):
            self.probabilitate_selectie.append(fit / fitness_sum)
            print(
                f"\t Cromozomul {i + 1} -> {self.probabilitate_selectie[-1]}", file=out
            ) if write else None
        print(file=out) if write else None

        print("SELECTIA ELITISTA:", file=out) if write else None
        n = 3
        top_n = top_n_indici(self.fitness, n)
        print(
            f"\tTOP {n} CROMOZOMI: {tuple(map(lambda x: x+1, top_n))}", file=out
        ) if write else None
        top_n = [copy.deepcopy(self.populatie[i]) for i in top_n]
        print(file=out) if write else None

        print("INTERVALE SELECTIE:", file=out) if write else None
        for val in self.intervale_selectie:
            print(f"{val}", end=" ", file=out) if write else None
        print(file=out) if write else None

        print("SELECTIE:", file=out) if write else None
        selected = top_n
        for _ in range(dimensiune - len(top_n)):
            random_number = uniform(0, 1)
            print(f"\trandom = {random_number}", end=" ", file=out) if write else None
            for i in range(len(self.intervale_selectie) - 1):
                if (
                    self.intervale_selectie[i]
                    <= random_number
                    < self.intervale_selectie[i + 1]
                ):
                    selected.append(self.populatie[i])
                    print(
                        f"--> Selectam cromozomul {i + 1}", file=out
                    ) if write else None
                    break
        print(file=out) if write else None

        self.populatie = selected
        self.fit()
        print("POPULATIA DUPA SELECTIE:", file=out) if write else None
        for i, individ in enumerate(self.populatie):
            print(f"\t{i + 1}: {individ}", file=out) if write else None
        print(file=out) if write else None

    def incrucisare(self, write: bool = False):
        def incrucisare_indivizi(
            individ1: Individ, individ2: Individ, punct: int
        ) -> tuple:
            return Individ(
                cromozom=individ1.cromozom[:punct] + individ2.cromozom[punct:]
            ), Individ(cromozom=individ2.cromozom[:punct] + individ1.cromozom[punct:])

        participanti = []
        print(
            f"PROBABILITATE INCRUCISARE = {PROB_RECOMBINARE}", file=out
        ) if write else None
        for i, individ in enumerate(self.populatie[3:], start=3):
            print(
                f"\t{i + 1}: {individ.cromozom}", end=" ", file=out
            ) if write else None
            rand_prob = uniform(0, 1)
            print(f"random = {rand_prob}", end=" ", file=out) if write else None
            if rand_prob < PROB_RECOMBINARE:
                print(
                    f"< {PROB_RECOMBINARE} --> PARTICIPA LA INCRUCISARE", file=out
                ) if write else None
                participanti.append((i + 1, individ))
            else:
                print(file=out) if write else None
        print(file=out) if write else None

        shuffle(participanti)

        print("INCRUCISARE:", file=out) if write else None
        for i in range(0, len(participanti) - 1, 2):
            punct = randint(1, len(participanti[0][1].cromozom) - 2)
            print(
                f"\tRecombinare intre cromozomul {participanti[i][0]} si cromozomul {participanti[i+1][0]} --> punct = {punct}",
                file=out,
            ) if write else None
            individ1, individ2 = incrucisare_indivizi(
                participanti[i][1], participanti[i + 1][1], punct
            )
            self.populatie[participanti[i][0] - 1] = individ1
            self.populatie[participanti[i + 1][0] - 1] = individ2
            print(
                f"REZULTAT --> {individ1.cromozom} si {individ2.cromozom}", file=out
            ) if write else None
        print(file=out) if write else None

        self.fit()
        print("POPULATIA DUPA RECOMBINARE:", file=out) if write else None
        for i, individ in enumerate(self.populatie):
            print(f"\t{i + 1}: {individ}", file=out) if write else None
        print(file=out) if write else None

    def mutatie(self, write: bool = False):
        print(
            f"PROBABILITATE MUTATIE PENTRU FIECARE GENA = {PROB_MUTATIE}", file=out
        ) if write else None
        print("AU FOST MODIFICATI CROMOZOMII:", file=out) if write else None
        for i, individ in enumerate(self.populatie[3:], start=3):
            flag = False
            new_cromozom = ""
            for bit in individ.cromozom:
                rand = random()
                if rand < PROB_MUTATIE:
                    flag = True
                    new_cromozom += "1" if bit == "0" else "0"
                else:
                    new_cromozom += bit
            if flag:
                print(
                    f"\t{i + 1}: {individ.cromozom} --> {new_cromozom}", file=out
                ) if write else None
                individ.set_cromozom(new_cromozom)
        print(file=out) if write else None

        self.fit()
        print("POPULATIA DUPA MUTATII:", file=out) if write else None
        for i, individ in enumerate(self.populatie):
            print(f"\t{i + 1}: {individ}", file=out) if write else None
        print(file=out) if write else None


def read():
    with open("input.txt") as f:
        dimensiune_populatie = int(f.readline())
        domeniu = tuple(map(int, f.readline().split()))
        parametrii_functie = tuple(map(int, f.readline().split()))
        precizie_discretizare = int(f.readline())
        probabilitate_recombinare = float(f.readline())
        probabilitate_mutatie = float(f.readline())
        numar_generatii = int(f.readline())
    return (
        dimensiune_populatie,
        domeniu,
        parametrii_functie,
        precizie_discretizare,
        probabilitate_recombinare,
        probabilitate_mutatie,
        numar_generatii,
    )


if __name__ == "__main__":
    (
        DIMENSIUNE_POPULATIE,
        DOMENIU,
        COEFICIENTI,
        PRECIZIE,
        PROB_RECOMBINARE,
        PROB_MUTATIE,
        NR_GENERATII,
    ) = read()

    out = open("output.txt", "w")

    print("GENERATIA 1", file=out)
    populatie = Populatie()
    populatie.genereaza_populatie_random(DIMENSIUNE_POPULATIE, DOMENIU, write=True)

    populatie.fit()
    populatie.selectie(DIMENSIUNE_POPULATIE, write=True)
    populatie.incrucisare(write=True)
    populatie.mutatie(write=True)
    for i in range(1, NR_GENERATII):
        print(f"GENERATIA {i + 1}", file=out)
        populatie.fit(max_and_mean=True)
        populatie.selectie(DIMENSIUNE_POPULATIE)
        populatie.incrucisare()
        populatie.mutatie()

    out.close()
