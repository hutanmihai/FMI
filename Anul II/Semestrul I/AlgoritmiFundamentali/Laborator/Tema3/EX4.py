"""
Pentru rezolvarea acestei probleme am folosit DFS. Cazurile posibile (ciclu sau lant eulerian) sunt descrise in
comentariile din cod.
Complexitatea algoritmului este: O(n)
"""


from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for x, y in pairs:
            graph[x].append(y)
            degree[x] += 1
            degree[y] -= 1

        # cazul 1, exista ciclu eulerian => orice nod poate fi start
        start = pairs[0][0]

        # cazul 2, nu exista ciclu eulerian, dar avem lant eulerian (garantat din cerinta), gasim startul
        for node in degree.keys():
            if degree[node] == 1:
                start = node
                break

        res = []

        def euler(node):
            # parcurgem dfs cat timp avem vecini nevizitati
            while graph[node]:
                # luam un vecin nevizitat, si il vizitam
                euler(graph[node].pop())
            # adaugam nodul la rezultat
            res.append(node)

        euler(start)
        # rezultatul este inversat
        res = res[::-1]
        # reconstruim perechile
        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]


if __name__ == '__main__':
    pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
    print(Solution().validArrangement(pairs))
