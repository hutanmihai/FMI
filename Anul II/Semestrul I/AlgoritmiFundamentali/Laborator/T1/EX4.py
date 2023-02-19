import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def create_reverse_graph():
    reverse_graph = defaultdict(list)
    for nod, vecini in graph.items():
        for vecin in vecini:
            reverse_graph[vecin].append(nod)
    return reverse_graph


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
    with open('ctc.in') as fin:
        n, m = map(int, fin.readline().split())
        graph = defaultdict(list)
        for _ in range(m):
            x, y = map(int, fin.readline().split())
            graph[x].append(y)

    reverse_graph = create_reverse_graph()
    vizitat = set()
    nr_componente_tare_conexe = 0
    componente_conexe = [[] for _ in range(n)]
    fin = deque()

    kosaraju()

    with open('ctc.out', 'w') as fout:
        print(nr_componente_tare_conexe, file=fout)
        for componenta in componente_conexe:
            print(*sorted(componenta), file=fout)
