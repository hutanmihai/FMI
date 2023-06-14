from math import sqrt

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


def dist(pct1, pct2):
    return sqrt((pct1[0] - pct2[0]) ** 2 + (pct1[1] - pct2[1]) ** 2)


def afisare(puncte):
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
    return sol


def step2(sub_tour, puncte):
    dict_pct = {}
    for pct in puncte:
        dict_pct[pct] = (float("inf"), -1, -1)
        for i in range(len(sub_tour)):
            j = (i + 1) % len(sub_tour)
            d = dist(sub_tour[i], pct) + dist(sub_tour[j], pct) - dist(sub_tour[i], sub_tour[j])
            if d < dict_pct[pct][0]:
                dict_pct[pct] = (d, i, j)
    print(dict_pct)
    return dict_pct


def step3(sub_tour, puncte):
    dict_pct = step2(sub_tour, puncte)
    min_dist = float("inf")
    for k, tuplu in dict_pct.items():
        i, j = tuplu[1], tuplu[2]
        d = (dist(sub_tour[i], k) + dist(sub_tour[j], k)) / dist(sub_tour[i], sub_tour[j])
        if d < min_dist:
            poz_inserare = (k, i, j)
    return poz_inserare




def tsp_graham(puncte):
    sub_tour = graham(puncte)
    puncte_ramase = [punct for punct in puncte if punct not in sub_tour]
    while puncte_ramase:
        pct_de_inserat, poz_inserare_1, poz_inserare_2 = step3(sub_tour, puncte_ramase)
        # sub_tour = sub_tour[:poz_inserare_1 + 1] + [pct_de_inserat] + sub_tour[poz_inserare_2:]
        sub_tour.insert(poz_inserare_1 + 1, pct_de_inserat)
        puncte_ramase.remove(pct_de_inserat)
    sub_tour.append(sub_tour[0])
    return sub_tour


if __name__ == '__main__':
    # n = int(input())
    # puncte = []
    # for i in range(n):
    #     puncte.append(tuple(map(int, input().split())))
    # afisare(tsp_graham(puncte))
    #
    with open('tsp11.in', 'r') as f:
        n = int(f.readline())
        puncte = []
        for i in range(n):
            puncte.append(tuple(map(int, f.readline().split())))

        with open('tsp11.out', 'w') as g:
            for x, y in tsp_graham(puncte):
                g.write(f'{x} {y}\n')
