# O(n+m)

from collections import deque


def sortare_topologica():
    ordine_topologica = []
    q = deque()
    indegree = {nod: 0 for nod in graph}

    for nod in graph:
        for vecin in graph[nod]:
            indegree[vecin] += 1

    for nod in indegree:
        if indegree[nod] == 0:
            q.append(nod)

    # BFS
    while q:
        nod = q.popleft()
        ordine_topologica.append(nod)

        for vecin in graph[nod]:
            indegree[vecin] -= 1

            if indegree[vecin] == 0:
                q.append(vecin)

    return ordine_topologica


if __name__ == '__main__':
    graph = {1: [5, 6], 2: [], 3: [5, 2], 4: [2], 5: [2, 4], 6: [2]}
    print(sortare_topologica())
