# COMPLEXITATEA ALGORITMULUI: O(n+m)

from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graf = [[] for _ in range(n)]
        for a, b in connections:
            graf[a].append(b)
            graf[b].append(a)
        vizitat, nivel, nivel_minim, sol = [False] * n, [0] * n, [0] * n, []

        nivel[0] = 1

        def dfs(nod: int):
            vizitat[nod] = True
            nivel_minim[nod] = nivel[nod]
            for vecin in graf[nod]:
                if not vizitat[vecin]:
                    nivel[vecin] = nivel[nod] + 1
                    dfs(vecin)

                    nivel_minim[nod] = min(nivel_minim[nod], nivel_minim[vecin])

                    if nivel_minim[vecin] > nivel[nod]:
                        sol.append([nod, vecin])
                elif nivel[vecin] < nivel[nod] - 1:
                    nivel_minim[nod] = min(nivel_minim[nod], nivel[vecin])

        dfs(0)
        return sol
