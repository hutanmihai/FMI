# O(m+n)

"""
Algoritmi pentru grafuri orientate fără circuite (cu ponderi reale) -> DAGs = Directed Acyclic Graphs
Pentru drumuri minime de sursa unica in grafuri aciclice.
Daca vrem drumuri maxime in grafuri aciclice modificam initializarea distantelor la -inf si schimbam semnul comparatiei.
"""
from collections import deque


def sortare_topologica():
    ordine_topologica = []
    q = deque()
    indegree = {nod: 0 for nod in graph}

    for nod in graph:
        for vecin in graph[nod]:
            indegree[vecin[0]] += 1

    for nod in indegree:
        if indegree[nod] == 0:
            q.append(nod)

    # BFS
    while q:
        nod = q.popleft()
        ordine_topologica.append(nod)

        for vecin in graph[nod]:
            indegree[vecin[0]] -= 1

            if indegree[vecin[0]] == 0:
                q.append(vecin[0])

    return ordine_topologica


if __name__ == '__main__':
    graph = {1: [(5, 2), (6, 1)], 2: [], 3: [(5, 4), (2, 3)], 4: [(2, 7)], 5: [(2, 1), (4, 6)], 6: [(2, 2)]}

    start = 1
    dist = [float("inf")] * (len(graph) + 1)
    tata = [0] * (len(graph) + 1)
    dist[start] = 0

    sort_top = sortare_topologica()

    for nod in sort_top:
        for vecin, cost in graph[nod]:
            if dist[nod] + cost < dist[vecin]:
                dist[vecin] = dist[nod] + cost
                tata[vecin] = nod

    print(*dist)
    print(tata)
