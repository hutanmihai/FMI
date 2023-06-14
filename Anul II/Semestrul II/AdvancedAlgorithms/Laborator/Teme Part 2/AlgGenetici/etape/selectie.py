from math import pow


def func(numar: float):
    return coeficienti[0] * pow(numar, 2) + coeficienti[1] * numar + coeficienti[2]


if __name__ == "__main__":
    coeficienti = tuple(map(int, input().split()))
    populatie = int(input())
    cromozomi = tuple(map(float, input().split()))
    fitness = tuple(map(func, cromozomi))
    fitness_sum = sum(fitness)

    p = [0]

    for i, fit in enumerate(fitness):
        suma_partiala = sum(fitness[: i + 1])
        p.append(round(suma_partiala / fitness_sum - 5e-5, 4))

    for x in p:
        print(x)
