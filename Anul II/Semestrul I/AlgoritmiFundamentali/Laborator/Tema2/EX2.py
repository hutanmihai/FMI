"""
Pentru rezolvarea acestei probleme am folosit structura ajutatoare UnionFind. Operatia de tip 1 fiing echivalentul
metodei union, iar operatia de tip 2 fiind echivalentul metodei find.

Complexitatea algoritmului este O(mlogn).
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parinte = [x for x in range(n+1)]

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


with open("disjoint.in") as f, open("disjoint.out", 'w') as g:
    n, m = map(int, f.readline().split())
    uf = UnionFind(n)
    for i in range(n):
        while m:
            tip, x, y = map(int, f.readline().split())
            if tip == 1:
                uf.union(x, y)
            else:
                if uf.find(x) == uf.find(y):
                    g.write("DA\n")
                else:
                    g.write("NU\n")
            m -= 1
