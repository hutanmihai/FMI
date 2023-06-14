def test_orientare(pct1_dreapta, pct2_dreapta, punct):
    matrix = [
        [1, 1, 1],
        [pct1_dreapta[0], pct2_dreapta[0], punct[0]],
        [pct1_dreapta[1], pct2_dreapta[1], punct[1]]
    ]

    det = matrix[0][0] * matrix[1][1] * matrix[2][2] + \
          matrix[0][1] * matrix[1][2] * matrix[2][0] + \
          matrix[0][2] * matrix[1][0] * matrix[2][1] - \
          matrix[0][2] * matrix[1][1] * matrix[2][0] - \
          matrix[0][1] * matrix[1][0] * matrix[2][2] - \
          matrix[0][0] * matrix[1][2] * matrix[2][1]

    if det == 0:
        return "TOUCH"
    elif det > 0:
        return "LEFT"
    else:
        return "RIGHT"


if __name__ == '__main__':
    nr_teste = int(input())
    for i in range(nr_teste):
        p1, p2, q1, q2, r1, r2 = map(int, input().split())
        print(test_orientare((p1, p2), (q1, q2), (r1, r2)))
