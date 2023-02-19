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
