"""
Calculam pentru fiecare pereche de cuvinte distanta Levenshtein. Apoi sortam lista de perechi dupa distanta.
Continuam prin a cauta primele 2 cuvinte cu cea mai mica distanta care nu apartin aceluiasi cluster.
Impreunam clusterele si calculam distanta minima dintre clustere.

Complexitatea algoritmului este O(n^2).
"""

from typing import List
import sys

sys.setrecursionlimit(100001)


def levenshtein_distance(cuv1: str, cuv2: str, cuv1_len: int, cuv2_len: int) -> int:
    if cuv1_len == 0:
        return cuv2_len
    if cuv2_len == 0:
        return cuv1_len
    if cuv1[cuv1_len - 1] == cuv2[cuv2_len - 1]:
        return levenshtein_distance(cuv1, cuv2, cuv1_len - 1, cuv2_len - 1)
    return 1 + min(
        levenshtein_distance(cuv1, cuv2, cuv1_len - 1, cuv2_len),
        levenshtein_distance(cuv1, cuv2, cuv1_len, cuv2_len - 1),
        levenshtein_distance(cuv1, cuv2, cuv1_len - 1, cuv2_len - 1)
    )


def main():
    k: int = int(input("k = "))
    cuvinte: List[str] = []
    cuvintePereche: List[tuple[str, str, int]] = []
    n = 0
    with open("cuvinte.in") as f:
        for linie in f:
            for cuvant in linie.split():
                cuvinte.append(cuvant)
                n += 1

    # folosim levenstein pentru a gasi perechi
    for i in range(n - 1):
        for j in range(i + 1, n):
            lev_dist: int = levenshtein_distance(cuvinte[i], cuvinte[j], len(cuvinte[i]), len(cuvinte[j]))
            cuvintePereche.append((cuvinte[i], cuvinte[j], lev_dist))

    # sortam perechile dupa distanta
    cuvintePereche.sort(key=lambda x: x[2])

    # asignam fiecarui cluster un cuvant
    cluster: dict[str, int] = {}
    for i in range(1, len(cuvinte) + 1):
        cluster[cuvinte[i - 1]] = i

    for i in range(1, n - k + 1):
        j: int = 0
        while cluster[cuvintePereche[j][0]] == cluster[cuvintePereche[j][1]]:
            j += 1

        cluster1: int = cluster[cuvintePereche[j][0]]
        cluster2: int = cluster[cuvintePereche[j][1]]
        min_cluster: int = min(cluster1, cluster2)
        for (k, v) in cluster.items():
            if v == cluster1 or v == cluster2:
                cluster[k] = min_cluster

    min_dif: int = 1000000000
    for (cluster1_k, cluster1_v) in cluster.items():
        for (cluster2_k, cluster2_v) in cluster.items():
            if cluster1_v != cluster2_v:
                min_dif = min(min_dif, levenshtein_distance(cluster1_k, cluster2_k, len(cluster1_k), len(cluster2_k)))

    with open("cuvinte.out", "w") as f:
        for i in range(1, n + 1):
            are_cuvant: bool = False
            for (k, v) in cluster.items():
                if v == i:
                    f.write(f"{str(k)} ")
                    are_cuvant = True
            if are_cuvant:
                f.write("\n")
        f.write(f"{str(min_dif)}")


if __name__ == "__main__":
    main()
