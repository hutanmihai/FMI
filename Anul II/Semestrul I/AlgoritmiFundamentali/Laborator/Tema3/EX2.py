"""
Pentru rezolvarea acestei probleme am adaugat grafului bipartit doua noduri, unul de start si unul de final. Am legat
partea stanga a grafului bipartit de nodul de start si partea dreapta de nodul de final. Toate muchiile prezente in graf
au fost adaugate cu capacitatea 1. Am folosit algoritmul clasic Edmonds-Karp pentru a gasi fluxul maxim. In final, muchiile
care au fost folosite in flux sunt muchiile care fac parte din cuplajul maxim.
Complexitatea algoritmului este: O(n*m^2)
"""


from collections import defaultdict, deque

graph = defaultdict(list)
capacity = defaultdict(dict)


def add_edge(x, y):
    graph[x].append(y)
    graph[y].append(x)
    capacity[x][y] = 1
    capacity[y][x] = 0


with open("cuplaj.in", "r") as fin:
    n, m, e = map(int, fin.readline().split())
    start = 0
    end = n + m + 1
    parent = [None] * (end + 1)

    # Legam left side de start
    for i in range(1, n + 1):
        add_edge(start, i)

    # Legam right side de end
    for i in range(1, m + 1):
        add_edge(n + i, end)

    # Legam muchiile
    for i in range(e):
        x, y = map(int, fin.readline().split())
        add_edge(x, y + n)


def bfs():
    vizitat = [False] * (end + 1)
    q = deque()
    q.append(start)
    vizitat[start] = True
    while q:
        nod = q.popleft()
        for vecin in graph[nod]:
            if not vizitat[vecin] and capacity[nod][vecin] > 0:
                parent[vecin] = nod
                vizitat[vecin] = True
                q.append(vecin)
    return vizitat[end]


def cuplaj():
    max_flow = 0

    while bfs():
        path_flow = float("inf")
        nod = end

        while nod != start:
            tata = parent[nod]
            path_flow = min(path_flow, capacity[tata][nod])
            nod = tata

        max_flow += path_flow
        nod = end

        while nod != start:
            tata = parent[nod]
            capacity[nod][tata] += path_flow
            capacity[tata][nod] -= path_flow
            nod = tata
    return max_flow


if __name__ == '__main__':
    with open("cuplaj.out", "w") as fout:
        fout.write(str(cuplaj()) + "\n")
        for i in range(1, n + 1):
            for nod in graph[i]:
                if capacity[i][nod] == 0 and nod != end and nod != start:
                    fout.write(f"{i} {nod - n}\n")

# Expected output: 8906
