"""
Problema ne cere sa sa gasim suma minima a drumurilor ce conecteaza toate punctele din plan, prin urmare
daca privim punctele din plan ca fiind noduri, si drumurile muchii, am folosit algoritmul lui Prim
pentru a gasi arborele de cost minim, care ne va oferi suma minima a drumurilor ce conecteaza toate
punctele din plan.

Salvam punctele din plan intr-un dictionar de forma {(coord1,coord2): cost}, unde cost este costul
ce va fi updatat la fiecare iteratie, cu distanta manhattan dintre punctul curent si punctul al carui cost il modificam.
Astfel vom putea alege mereu punctul urmator cu cost minim.

Complexitatea algoritmului este O(n^2).
"""


from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dictionar = {(x, y): float('inf') if i != 0 else 0 for i, (x, y) in enumerate(points)}
        suma_distanta = 0
        while dictionar:
            x, y = min(dictionar, key=dictionar.get)  # obtinem punctul cu distanta minima curenta
            suma_distanta += dictionar.pop((x, y))  # scoatem punctul din dictionar si adaugam distanta la rezultat
            for x1, y1 in dictionar:  # pentru fiecare punct din dictionar calculam distanta actualizata
                dictionar[(x1, y1)] = min(dictionar[(x1, y1)], abs(x - x1) + abs(y - y1))
        return suma_distanta
