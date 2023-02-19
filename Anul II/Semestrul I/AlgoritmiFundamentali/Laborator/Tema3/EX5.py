"""
Pentru rezolvarea acestei probleme am folosit BFS. Rulam acest algoritm din fiecare nod si consideram toate
combinatiile posibile de a vizita nodurile. Algoritmul se opreste cand masca, marcata in implementarea mea cu un set,
contine toate nodurile din graf si returnam pasii.
Complexitatea algoritmului este: O(n*2^n)
"""


from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph[0]) == 0:
            return 0
        n = len(graph)
        q = deque()
        for i in range(n):
            q.append((i, frozenset([i])))
        visited = set(q)
        pasi = 0
        while q:
            temp = deque()
            while q:
                nod, masca = q.popleft()
                masca = list(masca)
                for vecin in graph[nod]:
                    masca.append(vecin)
                    urm_masca = frozenset(masca)
                    if len(urm_masca) == n:
                        return pasi + 1
                    if (vecin, urm_masca) not in visited:
                        temp.append((vecin, urm_masca))
                        visited.add((vecin, urm_masca))
                    masca.pop()
            pasi += 1
            q = temp
        return pasi


if __name__ == "__main__":
    graph = [[1, 2, 3], [0], [0], [0]]
    print(Solution().shortestPathLength(graph))
