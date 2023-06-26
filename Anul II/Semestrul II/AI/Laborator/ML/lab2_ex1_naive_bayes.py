# Se dă mulțimea de antrenare, reprezentând înălțimea în cm a unei persoane și eticheta corespunzătoare:
# [(160, F), (165, F), (155, F), (172, F), (175, B), (180, B), (177, B), (190, B)].
# Împărțind valorile continue (înălțimea) în 4 intervale (150-160, 161-170, 171- 180, 181-190),
# calculați probabilitatea ca o persoană având 178 cm, să fie fată sau să fie băiat, folosind regula lui Bayes.


def asignare_interval(n):
    if 150 <= n <= 160:
        return (150, 160)
    elif 161 <= n <= 170:
        return (161, 170)
    elif 171 <= n <= 180:
        return (171, 180)
    elif 181 <= n <= 190:
        return (181, 190)


test_set = [
    (160, "F"),
    (165, "F"),
    (155, "F"),
    (172, "F"),
    (175, "B"),
    (180, "B"),
    (177, "B"),
    (190, "B"),
]

nr_fete = 0
nr_baieti = 0

for set in test_set:
    if set[1] == "F":
        nr_fete += 1
    else:
        nr_baieti += 1

prob_fete = nr_fete / len(test_set)
prob_baieti = nr_baieti / len(test_set)

intervale = {
    (150, 160): (0, 0),
    (161, 170): (0, 0),
    (171, 180): (0, 0),
    (181, 190): (0, 0),
}

for set in test_set:
    for interval in intervale:
        if interval[0] <= set[0] <= interval[1]:
            if set[1] == "F":
                intervale[interval] = (
                    intervale[interval][0] + 1,
                    intervale[interval][1],
                )
            else:
                intervale[interval] = (
                    intervale[interval][0],
                    intervale[interval][1] + 1,
                )

intervale_fete = {
    (150, 160): intervale[(150, 160)][0] / nr_fete,
    (161, 170): intervale[(161, 170)][0] / nr_fete,
    (171, 180): intervale[(171, 180)][0] / nr_fete,
    (181, 190): intervale[(181, 190)][0] / nr_fete,
}

intervale_baieti = {
    (150, 160): intervale[(150, 160)][1] / nr_baieti,
    (161, 170): intervale[(161, 170)][1] / nr_baieti,
    (171, 180): intervale[(171, 180)][1] / nr_baieti,
    (181, 190): intervale[(181, 190)][1] / nr_baieti,
}

print(intervale_fete)
print(intervale_baieti)

n = int(input("Insereaza inaltimea ca int: "))
interval_actual = asignare_interval(n)
p_b, p_f = (
    prob_baieti * intervale_baieti[interval_actual],
    prob_fete * intervale_fete[interval_actual],
)

print(f"Probabilitate baiat: {p_b}")
print(f"Probabilitate fata: {p_f}")

if p_b > p_f:
    print("Baiat")
else:
    print("Fata")
