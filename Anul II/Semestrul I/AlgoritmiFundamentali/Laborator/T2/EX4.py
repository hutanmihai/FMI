import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def dijkstra(start, end):
            dist[start] = 0
            q = [(0, start)]
            while q:
                nod = heapq.heappop(q)[1]
                for vecin, cost in graph[nod]:
                    if dist[nod] * cost < dist[vecin]:
                        dist[vecin] = dist[nod] * cost
                        heapq.heappush(q, (dist[vecin], vecin))
                    if vecin == end:
                        return

        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            x = edge[0]
            y = edge[1]
            graph[x].append((y, -succProb[i]))
            graph[y].append((x, -succProb[i]))

        dist = [float("inf")] * (len(graph) + 1)
        dijkstra(start, end)
        return -dist[end]


if __name__ == '__main__':
    print(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
