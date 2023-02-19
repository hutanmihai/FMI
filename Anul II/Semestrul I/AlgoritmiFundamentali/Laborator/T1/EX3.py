from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        nr_of_prereq = [0] * numCourses
        fin = []

        for x, y in prerequisites:
            graph[y].append(x)
            nr_of_prereq[x] += 1

        def dfs(nod):
            fin.append(nod)
            nr_of_prereq[nod] = -1
            for vecin in graph[nod]:
                nr_of_prereq[vecin] -= 1
                if nr_of_prereq[vecin] == 0:
                    dfs(vecin)

        for i in range(numCourses):
            if nr_of_prereq[i] == 0:
                dfs(i)

        return fin if len(fin) == numCourses else []


if __name__ == '__main__':
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
