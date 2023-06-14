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
        return 0
    elif det > 0:
        return 1
    else:
        return -1


def incrementare_orientare(orientare):
    global stanga, dreapta, fata
    if orientare == 1:
        stanga += 1
    elif orientare == -1:
        dreapta += 1
    else:
        fata += 1


if __name__ == '__main__':
    nr_puncte = int(input())
    stanga = 0
    dreapta = 0
    fata = 0
    first = tuple(map(int, input().split()))
    last = first
    second_last = tuple(map(int, input().split()))
    for i in range(nr_puncte - 2):
        punct = tuple(map(int, input().split()))
        incrementare_orientare(test_orientare(last, second_last, punct))
        last = second_last
        second_last = punct
    incrementare_orientare(test_orientare(last, second_last, first))

    print(stanga, dreapta, fata)
