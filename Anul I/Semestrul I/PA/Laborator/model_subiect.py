# EX1:

# def citire_matrice(nume_fisier):
#     f = open(nume_fisier, 'r')
#     matrice = []
#     s = f.readline().split()
#     nr = len(s)
#     matrice = [[int(x) for x in s]]
#     s = f.readline()
#     while s:
#         if len(s.split())!=nr:
#             return None
#         matrice.append([int(x) for x in s.split()])
#         s  = f.readline()
#     return matrice
#
# def multimi(matrice, *argv):
#     poz = [0]*len(argv)
#     neg = [0]*len(argv)
#     lsarg=[arg for arg in argv]
#     for i in range(len(lsarg)):
#         poz[i] = {x for x in matrice[lsarg[i]] if x > 0 and str(x)[0] == str(x)[-1]}
#         neg[i] = {x for x in matrice[lsarg[i]] if x < 0}
#     reuniune = poz[0]
#     intersectie = neg[0]
#
#     for i in range(1,len(lsarg)):
#         reuniune = reuniune | poz[i]
#         intersectie = intersectie & neg[i]
#
#     return intersectie, reuniune
#
#
# matrice=citire_matrice("matrice.in")
# print(matrice)
# inters1,reun1 = multimi(matrice,1,2,3)
# print(*reun1)
# inters2,reun2 = multimi(matrice,0,3)
# print(*inters2)

# EX2:
# def modifica_prefix(x, y, prop):
#     ls = prop.strip().split()
#     lsnou = []
#     nr = 0
#     lungx = len(x)
#     lungy = len(y)
#     for cuv in ls:
#         verif = cuv.startswith(x)
#         if verif == True:
#             nou = cuv.replace(x,y,1)
#             nr += 1
#         else:
#             nou = cuv
#         lsnou.append(nou)
#     sir = ' '.join(lsnou)
#     return sir, nr
#
# def poz_max(lista):
#     v = []
#     maxim = max(lista)
#     for i in range(len(lista)):
#         if lista[i] == maxim:
#             v.append(i)
#     return v
#
# f = open("propozitii.in", 'r')
# g = open("propozitii.out", 'w')
# ab = input("a si b = ")
# vec = ab.rstrip('\n').split()
# a = vec[0]
# b = vec[1]
# ls = [-1]
#
# s = 15
# while s:
#     s = f.readline()
#     smodif, nrmodif = modifica_prefix(a, b, s)
#     ls.append(nrmodif)
#     g.write(smodif)
#     g.write("\n")
# indici = poz_max(ls)
# print(*indici)


# EX3:

f = open("autori.in", 'r')
# ls = f.readline().split()
# n = int(ls[0])
# m = int(ls[1])
n, m = [int(x) for x in f.readline().split()]
d = {}
for rand in range(n):
    ls = f.readline().split(maxsplit=1)
    cod_autor = int(ls[0])
    # print(cod_autor)
    d[cod_autor] = [ls[1].rstrip('\n'), {}]

for rand in range(m):
    ls = f.readline().split(maxsplit=4)
    cod_autor = int(ls[0])
    codul_cartii = int(ls[1])
    an_aparitie = int(ls[2])
    nr_pagini = int(ls[3])
    titlu = ls[4].rstrip('\n')
    # d_carti = d[cod_autor][1]
    d[cod_autor][1][codul_cartii] = [an_aparitie,nr_pagini,titlu]
    # d_carti[codul_cartii]=[an_aparitie,nr_pagini,titlu]

def sterge_carte(d, cod_carte):
    for i in d:
        if cod_carte in d[i][1]:
            del d[i][1][cod_carte]
            return d[i][0]
        else:
            return "Cartea nu exista"
print(sterge_carte(d,101))
print(d)
