# O(mlogn)

graph = {0: [(1, 2), (4, 1)], 1: [(2, 3), (3, 7)], 2: [(3, 1), (0, 5)], 3: [(4, 4)], 4: [(0, 1)]}
edges = []
apcm = []
for nod in range(len(graph)):
    for vecin, cost in graph[nod]:
        edges.append((nod, vecin, cost))


class UnionFind:
    def __init__(self, n):
        self.parinte = [x for x in range(n + 1)]
        self.inaltime = [0] * len(self.parinte)

    def find(self, x):
        if x == self.parinte[x]:
            return x
        self.parinte[x] = self.find(self.parinte[x])
        return self.parinte[x]

    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if self.inaltime[x] > self.inaltime[y]:
            self.parinte[y] = x
        else:
            self.parinte[x] = y
            if self.inaltime[x] == self.inaltime[y]:
                self.inaltime[y] += 1


def sort_edges():
    return sorted(edges, key=lambda x: x[2])


def kruskal():
    uf = UnionFind(len(graph))
    edges = sort_edges()
    nr_edges = 0
    for edge in edges:
        nod, vecin, cost = edge
        a = uf.find(nod)
        b = uf.find(vecin)

        if a != b:
            apcm.append(edge)
            uf.union(a, b)
            nr_edges += 1
            if nr_edges == len(graph) - 1:
                return


if __name__ == '__main__':
    kruskal()
    print(apcm)
