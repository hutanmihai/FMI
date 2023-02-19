# O(mlogn)

"""
Algoritmi pentru grafuri orientate cu circuite, dar cu ponderi pozitive – Dijkstra
"""
import heapq


def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]
    while q:
        nod = heapq.heappop(q)[1]
        for vecin, cost in graph[nod]:
            if dist[nod] + cost < dist[vecin]:
                dist[vecin] = dist[nod] + cost
                heapq.heappush(q, (dist[vecin], vecin))
                tata[vecin] = nod


if __name__ == '__main__':
    graph = {1: [(2, 1), (3, 4)], 2: [(1, 1), (3, 2), (4, 5)], 3: [(1, 4), (2, 2), (4, 1)], 4: [(2, 5), (3, 1)]}

    dist = [float("inf")] * (len(graph) + 1)
    tata = [0] * (len(graph) + 1)
    dijkstra(1)

    print(*dist)
    print(tata)
