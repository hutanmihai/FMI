"""
Pentru rezolvarea acestei probleme am folosit BFS si cautarea binara. In bfs, consideram drumurile care
accepta greutatea primita ca parametru si returnam True daca putem ajunge la final cu acea greutate.
Cautarea binara o facem pe costul maxim, aflat la citirea datelor, incepem de la 0 la cost maxim, si apelam bfs-ul
cu mijlocul ca parametru, repetam, pana cand incercam toate variantele din cautarea binara, si returnam ultima valoare maxima
care a returnat adevarat din bfs.
Complexitatea algoritmului este: O(m*log(c)), unde m-nr muhcii, c-costul maxim
"""

from collections import defaultdict, deque


def bfs(greutate_max_curenta):
    visited = set()
    q = deque()

    q.append(start)
    visited.add(start)

    while q:
        nod = q.popleft()
        for vecin, cost_vecin in graph[nod]:
            if vecin not in visited and cost_vecin >= greutate_max_curenta:
                visited.add(vecin)
                q.append(vecin)
                if vecin == end:
                    return True
    return False


if __name__ == '__main__':
    with open("transport2.in", "r") as fin:
        nr_nodes, nr_edges = map(int, fin.readline().split())
        graph = defaultdict(list)
        start, end = 1, nr_nodes
        greutate_max = 0
        for _ in range(nr_edges):
            x, y, cost = map(int, fin.readline().split())
            graph[x].append((y, cost))
            graph[y].append((x, cost))
            greutate_max = max(greutate_max, cost)
    with open("transport2.out", "w") as fout:
        st = 0
        dr = greutate_max
        res = -1
        while (st <= dr):
            mid = (st + dr) // 2
            if bfs(mid):
                res = mid
                st = mid + 1
            else:
                dr = mid - 1
        fout.write(str(res))
