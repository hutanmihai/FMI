import sys
from collections import defaultdict

sys.setrecursionlimit(100001)

n, m = map(int, input().split())
permutare = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
vizitat = set()
ordine_finala = []


def sort_graph_by_permutation():
    # Generam lista cu pozitiile nodurilor in permutare
    poz = [0] * (len(graph)+1)
    for i in range(1, len(graph)):
        poz[permutare[i]] = i

    for nod in graph:
        graph[nod].sort(key=lambda x: poz[x])


def dfs(nod):
    vizitat.add(nod)
    ordine_finala.append(nod)
    for vecin in graph[nod]:
        if vecin not in vizitat:
            dfs(vecin)


sort_graph_by_permutation()
dfs(1)
if ordine_finala == permutare:
    print(1)
else:
    print(0)
