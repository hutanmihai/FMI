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


def afisare(lungime_raspuns, puncte):
    print(lungime_raspuns)
    for x, y in puncte:
        print(x, y)


def graham(puncte):
    puncte.sort(key=lambda x: (x[0], x[1]))

    def frontiera_inferioara():
        sol = [puncte[0], puncte[1]]
        for i in range(2, len(puncte)):
            sol.append(puncte[i])
            while len(sol) > 2 and test_orientare(sol[-3], sol[-2], sol[-1]) != 1:
                sol.pop(-2)
        return sol

    def frontiera_superioara():
        sol = [puncte[-1], puncte[-2]]
        for i in range(len(puncte) - 3, -1, -1):
            sol.append(puncte[i])
            while len(sol) > 2 and test_orientare(sol[-3], sol[-2], sol[-1]) != 1:
                sol.pop(-2)
        return sol[1:-1]

    sol = frontiera_inferioara() + frontiera_superioara()
    afisare(len(sol), sol)


if __name__ == '__main__':
    n = int(input())
    puncte = []
    for i in range(n):
        puncte.append(tuple(map(int, input().split())))

    graham(puncte)
