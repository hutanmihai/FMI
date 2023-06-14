def test_orientare(pct1_dreapta, pct2_dreapta, punct):
    det = pct2_dreapta[0] * punct[1] + \
          pct1_dreapta[0] * pct2_dreapta[1] + \
          pct1_dreapta[1] * punct[0] - \
          pct2_dreapta[0] * pct1_dreapta[1] - \
          punct[0] * pct2_dreapta[1] - \
          punct[1] * pct1_dreapta[0]

    if det == 0:
        return 0
    elif det > 0:
        return 1
    else:
        return 2


def cel_mai_din_stanga(puncte, n):
    l = 0
    for i in range(1, n):
        if puncte[i][0] < puncte[l][0]:
            l = i
    return l


def dist(a, b):
    return ((puncte[b][0] - puncte[a][0]) ** 2 + (puncte[b][1] - puncte[a][1]) ** 2) ** 0.5


def afisare(lungime_raspuns, puncte):
    print(lungime_raspuns)
    for x, y in puncte:
        print(x, y)


def jarvis_march(puncte):
    n = len(puncte)

    if n < 3:
        afisare(n, puncte)
        return

    first = cel_mai_din_stanga(puncte, n)

    curent = first
    sol = []

    while True:
        sol.append(puncte[curent])
        pivot = (curent + 1) % n

        for i in range(n):
            orientare = test_orientare(puncte[curent], puncte[pivot], puncte[i])
            if pivot == curent or orientare == 2 or (orientare == 0 and dist(curent, i) > dist(curent, pivot)):
                pivot = i

        if pivot != first:
            curent = pivot
        else:
            break

    afisare(len(sol), sol)


if __name__ == '__main__':
    n = int(input())
    puncte = []
    for i in range(n):
        puncte.append(tuple(map(int, input().split())))

    jarvis_march(puncte)
