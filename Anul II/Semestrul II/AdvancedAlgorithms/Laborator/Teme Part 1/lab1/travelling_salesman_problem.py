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


def tsp(points):
    # Build initial sub-tour using convex hull of all points
    tour = graham(points)

    # Add remaining points to sub-tour using nearest neighbor
    for r in points:
        if r not in tour:
            # Find nearest pair of nodes (i, j) in sub-tour
            min_distance = float('inf')
            for i in range(len(tour)):
                j = (i + 1) % len(tour)
                d = dist(tour[i], r) + dist(r, tour[j]) - dist(tour[i], tour[j])
                if d < min_distance:
                    min_distance = d
                    best_i = i
                    best_j = j

            # Find the insertion point (i*, r*, j*) that minimizes the tour length
            min_tour_length = float('inf')
            for i in range(len(tour)):
                j = (i + 1) % len(tour)
                if j == best_i or j == best_j:
                    continue
                tour_length = dist(tour[i], r) + dist(r, tour[j]) - dist(tour[i], tour[best_i]) - dist(
                    tour[best_j], tour[j])
                if tour_length < min_tour_length:
                    min_tour_length = tour_length
                    best_i_star = i
                    best_j_star = j

            # Insert node r* into sub-tour between nodes i* and j*
            tour = tour[:best_i + 1] + [r] + tour[best_j:]
            if best_i_star < best_j_star:
                tour = tour[:best_i_star + 1] + tour[best_j_star:]
            else:
                tour = tour[:best_j_star + 1] + tour[best_i_star:]

    return tour


if __name__ == '__main__':
    with open('tsp11.in', 'r') as f:
        n = int(f.readline())
        puncte = []
        for i in range(n):
            puncte.append(tuple(map(int, f.readline().split())))

        with open('tsp11.out', 'w') as g:
            for x, y in tsp(puncte):
                g.write(f'{x} {y}\n')
