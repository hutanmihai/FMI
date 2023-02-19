# COMPLEXITATEA ALGORITMULUI: 0(n*m)

from typing import List


class Solution:
    def maxAreaOfIsland(self, matrice: List[List[int]]) -> int:
        vizitat = set()

        def arie(lin, col):
            if not (0 <= lin < len(matrice) and 0 <= col < len(matrice[0]) and (lin, col) not in vizitat and matrice[lin][col]):
                return 0
            vizitat.add((lin, col))
            return (1 + arie(lin + 1, col) + arie(lin - 1, col) +
                    arie(lin, col - 1) + arie(lin, col + 1))

        return max(arie(lin, col) for lin in range(len(matrice)) for col in range(len(matrice[0])))
