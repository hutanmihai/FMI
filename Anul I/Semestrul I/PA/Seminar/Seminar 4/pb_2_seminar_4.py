def frecventa_dictionar(nume):
    f = open("C:\\Users\\Lenovo\\Desktop\\" + nume)

    dic = {}

    for s in f:
        for x in s:
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic[x] = 1

    #for x in dic:
    #    print(f"{repr(x)} apare de {dic[x]}")

    return dic

def cmp(x):
    if x.isalnum():
        return False, x
    else:
        return True, -ord(x)

d1 = frecventa_dictionar("caractere1.in")
d2 = frecventa_dictionar("caractere2.in")

#d = d1.keys() & d2.keys()

#for x in sorted(d, key=cmp):
#    print(f"{repr(x)} apare de {d1[x] + d2[x]}")

d = d1.keys() | d2.keys()

for x in sorted(d, key=cmp):
    print(f"{repr(x)} apare de {d1.get(x, 0) + d2.get(x, 0)}")

