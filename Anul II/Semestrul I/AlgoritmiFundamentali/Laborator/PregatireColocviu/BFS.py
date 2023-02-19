# O(n+m)

"""
Neorientat:
Muchiile din graf care nu apar in arborele BF inchid cicluri.
Orientat:
Arcele din graf care nu apar in arborele BF NU inchid neaparat cicluri.

Determinarea unui lanț/drum minim între două vârfuri date u și v se calculeaza verificand daca v este vizitat,
mai apoi luam tatal fiecarui nod plecand din v pana ajungem la u.

EX:
drum = []
nod = v
drum.append(nod)

BFS(u)

if v in vizitat:
    while nod != u:
        nod = tata[nod]
        drum.append(nod)
    print(reversed(drum))
else:
    print("Nu exista drum!")
"""

from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    vizitat.add(start)
    distanta[start] = 0
    while q:
        nod = q.popleft()
        for vecin in graph[nod]:
            if vecin not in vizitat:
                q.append(vecin)
                vizitat.add(vecin)
                distanta[vecin] = distanta[nod] + 1
                tata[vecin] = nod


if __name__ == '__main__':
    graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
    vizitat = set()
    tata = [0] * (len(graph) + 1)
    distanta = [float('inf')] * (len(graph) + 1)

    nr_componente_conexe = 0

    for nod in graph:
        if nod not in vizitat:
            bfs(nod)
            nr_componente_conexe += 1
