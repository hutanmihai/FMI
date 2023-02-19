"""
Pentru rezolvarea acestei probleme am folosit algoritmul lui Dijkstra, nodurile de start fiind fortaretele si tinem
intr-o lista -> distanta_minima distantele minime de la un cutun la o fortareata. Fortaretele corespondente acelor
distante minime le vom salva in lista ans.

Complexitatea algoritmului este O(mlogn).
"""

import heapq
from typing import List


def dijkstra() -> None:
    while heap:
        nod: int = heapq.heappop(heap)[1]

        for v in graf[nod]:
            if distanta_minima[nod] + v[1] < distanta_minima[v[0]]:
                distanta_minima[v[0]] = distanta_minima[nod] + v[1]
                heapq.heappush(heap, (distanta_minima[v[0]], v[0]))
                ans[v[0]] = ans[nod]
            # daca distanta unui catun intre doua cetati este identica vom lua fortareata cu index mai mic
            elif distanta_minima[nod] + v[1] == distanta_minima[v[0]]:
                ans[v[0]] = min(ans[v[0]], ans[nod])


with open("catun.in", 'r') as f:
    n, m, k = map(int, f.readline().split())
    distanta_minima: List[int] = [float('inf')] * (n + 1)
    ans: List[int] = [0] * (n + 1)
    graf: dict[int, list[tuple[int, int]]] = {i: [] for i in range(1, n + 1)}

    fortarete = map(int, f.readline().split())

    heap: List[tuple[int, int]] = []
    heapq.heapify(heap)

    for fortareata in fortarete:
        ans[fortareata] = fortareata
        distanta_minima[fortareata] = 0
        heapq.heappush(heap, (0, fortareata))

    for i in range(m):
        line = [int(x) for x in f.readline().split()]
        graf[line[0]].append((line[1], line[2]))
        graf[line[1]].append((line[0], line[2]))

dijkstra()

with open("catun.out", 'w') as g:
    for i in range(1, n + 1):
        if ans[i] == i:
            g.write("0 ")
        else:
            g.write(f"{ans[i]} ")
