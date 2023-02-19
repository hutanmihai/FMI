# O(n+m)

"""
Determinarea componentelor tare conexe dintr-un graf orientat.
"""

from collections import defaultdict, deque


def create_reverse_graph():
    rev_graph = defaultdict(list)
    for nod, vecini in graph.items():
        for vecin in vecini:
            rev_graph[vecin].append(nod)
    return rev_graph


def dfs_ordine(nod):
    vizitat.add(nod)
    for vecin in graph[nod]:
        if vecin not in vizitat:
            dfs_ordine(vecin)
    fin.append(nod)


def dfs(nod):
    componente_conexe[nr_componente_tare_conexe].append(nod)
    vizitat.add(nod)
    for vecin in reverse_graph[nod]:
        if vecin not in vizitat:
            dfs(vecin)


def kosaraju():
    global nr_componente_tare_conexe
    for nod in graph.keys():
        if nod not in vizitat:
            dfs_ordine(nod)
    vizitat.clear()
    while fin:
        nod = fin.pop()
        if nod not in vizitat:
            dfs(nod)
            nr_componente_tare_conexe += 1


if __name__ == '__main__':
    graph = {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: [6], 6: [4, 7], 7: []}

    reverse_graph = create_reverse_graph()
    vizitat = set()
    nr_componente_tare_conexe = 0
    componente_conexe = [[] for _ in range(len(graph) + 1)]
    fin = deque()
