"""
Pentru rezolvarea acestei probleme am folosit algoritmul de cuplaj maximal din graf bipartit. Graful bipartit fiind
de fapt graful initial de doua ori, netragand muchii intre nodurile din partea stanga si partea dreapta care reprezinta
de fapt acelas nod ("oras") Si legandu-le de un start si un end in modul specific algoritmului de cuplaj maximal.
In final afisam muchiile care fac parte din cuplajul maximal.
Complexitatea algoritmului este: O(n*m^2)
"""


from collections import defaultdict
from queue import Queue

with open("harta.in", "r") as fin:
    nr_noduri = int(fin.readline())
    start = 0
    end = nr_noduri * 2 + 1
    graph = defaultdict(list)
    capacity = defaultdict(dict)
    parent = [None] * (end + 1)

    for i in range(1, nr_noduri + 1):
        x, y = map(int, fin.readline().split())
        graph[start].append(i)
        graph[i].append(start)
        capacity[start][i] = x
        capacity[i][start] = 0

        graph[nr_noduri + i].append(end)
        graph[end].append(nr_noduri + i)
        capacity[nr_noduri + i][end] = y
        capacity[end][nr_noduri + i] = 0

    for i in range(1, nr_noduri + 1):
        for j in range(1, nr_noduri + 1):
            capacity[i][nr_noduri + j] = 0
            capacity[nr_noduri + j][i] = 0
            if i != j:
                graph[i].append(nr_noduri + j)
                graph[nr_noduri + j].append(i)
                capacity[i][nr_noduri + j] = 1


def bfs():
    vizitat = [False] * (end + 1)
    q = Queue(maxsize=end)
    q.put(start)
    vizitat[start] = True
    parent[start] = -1
    while not q.empty():
        nod = q.get()
        for vecin in graph[nod]:
            if not vizitat[vecin] and capacity[nod][vecin] > 0:
                parent[vecin] = nod
                if vecin == end:
                    return True
                q.put(vecin)
                vizitat[vecin] = True
    return False


def edmonds_karp():
    max_flow = 0
    min_flow = float("inf")
    while bfs():
        x = end
        while x != start:
            tata = parent[x]
            if capacity[tata][x] < min_flow:
                min_flow = capacity[tata][x]
            x = tata
        x = end
        while x != start:
            tata = parent[x]
            capacity[tata][x] -= min_flow
            capacity[x][tata] += min_flow
            x = tata
        max_flow += min_flow

    return max_flow


if __name__ == '__main__':
    with open("harta.out", "w") as fout:
        fout.write(f"{edmonds_karp()}\n")
        for i in range(1, nr_noduri + 1):
            for vecin in graph[i]:
                if vecin != start and capacity[i][vecin] == 0 and vecin != end:
                    fout.write(f"{i} {vecin-nr_noduri}\n")
