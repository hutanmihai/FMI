"""
Aceasta problema a fost rezolvata folosind algoritmul lui Dijkstra. In cazul nostru nodurile din heap vor fi de forma
(-probabilitate, nod). Folosim -probabilitate deoarece heap-ul este un min-heap si vrem sa avem maximul la varf.
La final cand gasim drumul cu cea mai mare probabilitate, returnam -probabilitatea drumului pentru a obtine probabilitatea
pozitiva.

Complexitatea algoritmului este O(n+mlogn).
"""

import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        lista_adiacenta = {i: [] for i in range(0, n)}

        for muchie, prob in zip(edges, succProb):
            v1, v2 = muchie
            lista_adiacenta[v1].append((prob, v2))
            lista_adiacenta[v2].append((prob, v1))

        heap = [(-1, start)]
        vizitat = set()

        while heap:
            prob, nod = heapq.heappop(heap)

            if nod in vizitat: continue
            if nod == end: return -prob

            vizitat.add(nod)

            for prob_vecin, vecin in lista_adiacenta[nod]:
                if vecin not in vizitat:
                    heapq.heappush(heap, (prob * prob_vecin, vecin))

        return 0.0
