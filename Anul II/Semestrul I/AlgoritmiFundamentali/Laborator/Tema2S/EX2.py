"""
Pentru rezolvarea acestei probleme sortam intai query-urile si muchiile dupa cost. Parcurgem query-urile si pentru fiecare query
conectam muchiile care se afla sub costul query-ului curent. La fiecare query verificam daca nodurile u si v sunt conectate in structura
UnionFind, daca da atunci adaugam True in lista de raspunsuri, altfel False.

Complexitatea algoritmului este O(nlogn) + O(mlogm).
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parinte = [x for x in range(n)]

    def find(self, x):
        if x == self.parinte[x]:
            return x
        self.parinte[x] = self.find(self.parinte[x])
        return self.parinte[x]

    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y:
            return
        self.parinte[y] = x


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = [(u, v, limit, index) for index, (u, v, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])  # sortam dupa limita
        edgeList.sort(key=lambda x: x[2])  # sortam dupa cost

        rez: List[bool] = [None] * len(queries)
        uf = UnionFind(n)

        for u, v, limit, i in queries:
            while edgeList and edgeList[0][2] < limit:
                uf.union(edgeList[0][0], edgeList[0][1])
                edgeList.pop(0)
            rez[i] = (uf.find(u) == uf.find(v))

        return rez
