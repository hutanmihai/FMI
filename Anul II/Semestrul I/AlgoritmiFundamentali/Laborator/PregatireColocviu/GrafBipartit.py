graph = {1: [2], 2: [3], 3: [4], 4: [1]}
colorare = [0] * (len(graph) + 1)


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


def is_bipartit():
    for nod in graph:
        if colorare[nod] == 0:
            colorare[nod] = 1
            if not dfs(nod):
                return False
    return True


if __name__ == '__main__':
    print(is_bipartit())
    color1 = []
    color2 = []
    for i, val in enumerate(colorare):
        if val == 1:
            color1.append(i)
        elif val == 2:
            color2.append(i)
    print(color1)
    print(color2)
