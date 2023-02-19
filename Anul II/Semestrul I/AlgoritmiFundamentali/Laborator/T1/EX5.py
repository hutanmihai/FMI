from collections import defaultdict

with open('graf.in') as fin:
    n, m = map(int, fin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, fin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    puncte_control = list(map(int, fin.readline().split()))

distante = [float('inf')] * (n + 1)
vizitat = set()


def dfs(nod):
    vizitat.add(nod)
    for vecin in graph[nod]:
        distante[vecin] = min(distante[vecin], distante[nod] + 1)
        if vecin not in vizitat and vecin not in puncte_control:
            dfs(vecin)


if __name__ == '__main__':
    for pc in puncte_control:
        distante[pc] = 0
        dfs(pc)
        vizitat.clear()

    with open('graf.out', 'w') as fout:
        for i in range(1, n + 1):
            print(distante[i], end=' ', file=fout)
