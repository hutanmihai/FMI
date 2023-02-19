# O(n+m)

from collections import defaultdict


def dfs(nod):
    culoare_curenta = colorare[nod]
    for vecin in graph[nod]:
        if colorare[vecin] == culoare_curenta:
            return False
        if colorare[vecin] == 0:
            colorare[vecin] = 1 if culoare_curenta == 2 else 2
            if not dfs(vecin):
                return False
    return True


if __name__ == '__main__':
    graph = {1: [2], 2: [1]}

    colorare = [0] * (len(graph) + 1)

    ok = True
    for nod in graph:
        if colorare[nod] == 0:
            colorare[nod] = 1
            if not dfs(nod):
                print("Graful nu este bipartit")
                ok = False
                break
    if ok:
        print("Graful este bipartit")
