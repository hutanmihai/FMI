"""
Pentru rezolvarea acestei probleme am folosit algoritmul lui Dijkstra. In cazul nostru nodul va fi de forma (cost, nod, k), unde cost este costul
acumulat pana in acel moment, nod este nodul curent si k este numarul de opriri pe care le mai avem la dispozitie.
Folosim o lista de vizitati pentru a evita parcurgerea multipla a acelorasi noduri. In lista de vizitati vom retine pentru fiecare nod
opririle ramase pentru a ajunge la acel nod, astfel evitam sa vizitam un caz mai defavorabil decat cel pe care l-am vizitat deja.
In momentul in care am folosit toate opririle disponibile sau opririle ramase dintr-un nod sunt mai mari decat opririle ramase curente, nu mai
adaugam nodul respectiv in coada de prioritati. In momentul in care varful heap-ului este nodul destinatie, am gasit un drum de cost minim.

Diferenta fata de algoritmul lui Dijkstra clasic este ca in cazul nostru daca dam pop la un nod deja vizitat nu il vom neglija deoarece
desi costul drumului poate este mai mare, trebuie sa verificam daca drumul consuma mai putine opriri.

Complexitatea algoritmului este O(k*mlogn), k-nr opriri, m-nr muchii, n-nr noduri.
"""

import collections
import heapq
from typing import List


class Solution(object):
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        start = src
        final = dst

        graf = collections.defaultdict(dict)
        for sursa, destinatie, cost in flights:
            graf[sursa][destinatie] = cost

        heap = [(0, start, k + 1)]
        vizitat = [0] * n

        while heap:
            cost, nod, pasi = heapq.heappop(heap)
            if nod == final:
                return cost
            if vizitat[nod] >= pasi:
                continue
            vizitat[nod] = pasi
            for vecin, cost_vecin in graf[nod].items():
                heapq.heappush(heap, (cost + cost_vecin, vecin, pasi - 1))
        return -1
