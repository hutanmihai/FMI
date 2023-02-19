"""
Pentru rezolvarea acestui subpunct am adaugat fata de problema initiala o iteratie peste intregul graph, in care
verificam in ce noduri putem ajunge din start folosind bfs, tăietura determinată de vârfurile accesibile din s la
ultimul pas prin lanțuri f-nesaturate este tăietură minimă.
Complexitatea algoritmului este: O(n*m^2)
"""

from collections import defaultdict
from queue import Queue

with open("maxflow.in", 'r') as fin:
    nr_noduri, nr_muchii = map(int, fin.readline().split())
    start = 1
    end = nr_noduri
    graph = defaultdict(list)
    capacity = defaultdict(dict)
    parent = [None] * (nr_noduri + 1)
    for _ in range(nr_muchii):
        x, y, c = map(int, fin.readline().split())
        graph[x].append(y)
        capacity[x][y] = c
        capacity[y][x] = 0


def bfs():
    global visited
    visited = [False] * (nr_noduri + 1)
    q = Queue(maxsize=nr_noduri)
    q.put(start)
    visited[start] = True
    while not q.empty():
        node = q.get()
        for neighbour in graph[node]:
            if not visited[neighbour] and capacity[node][neighbour] > 0:
                q.put(neighbour)
                visited[neighbour] = True
                parent[neighbour] = node
                if neighbour == end:
                    return True
    return False


def edmonds_karp():
    max_flow = 0

    while bfs():
        path_flow = float("inf")
        nod = end

        while nod != start:
            path_flow = min(path_flow, capacity[parent[nod]][nod])
            nod = parent[nod]

        max_flow += path_flow
        nod = end

        while nod != start:
            tata = parent[nod]
            capacity[tata][nod] -= path_flow
            capacity[nod][tata] += path_flow
            nod = tata
    return max_flow


if __name__ == '__main__':
    max_flow = edmonds_karp()
    bfs()
    min_cut = []
    for x in graph:
        for y in graph[x]:
            if visited[x] and not visited[y]:
                min_cut.append((x, y))

    print("Min cut:", len(min_cut), min_cut)
