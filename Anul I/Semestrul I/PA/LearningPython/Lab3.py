# EX1:

# a)
# ls = [chr(x) for x in range(ord('a'),ord('z')+1)]
# print(ls)

# b)
# n = int(input("n = "))
# ls = [(x if x%2 != 0 else -x) for x in range(1,n+1)]
# print(ls)

# c)
# ls = [int(x) for x in input("lista = ").split()]
# lsimp = [x for x in ls if x%2 != 0]
# print(lsimp)

# d)
# ls = [int(x) for x in input("lista = ").split()]
# lspoz = [ls[i] for i in range(len(ls)) if i%2 != 0]
# print(lspoz)

# e)
# ls = [int(x) for x in input("lista = ").split()]
# lsrez = [ls[i] for i in range(len(ls)) if ls[i]%2 == i%2]
# print(lsrez)

# f)
# ls = [int(x) for x in input("lista = ").split()]
# lsrez = [(ls[i], ls[i+1]) for i in range(len(ls)-1)]
# print(lsrez)

# g)
# def tabla_inmultirii (n):
#     matr = [[f"{x} * {y} = {x*y}" for y in range(1, n+1)] for x in range(1, n+1)]
#     return matr
# def afisare_matrice (matrice):
#     lungime = max([max([len(str(x)) for x in linie]) for linie in matrice])
#     for x in matrice:
#         for y in x:
#             print(f"{y}".rjust(lungime), end = '\t')
#         print()
# n = int(input("n = "))
# M = tabla_inmultirii(n)
# afisare_matrice (M)

# h)
# sir = input("sir = ")
# lst = [sir[i:]+sir[:i] for i in range(len(sir))]
# print(lst)

# # i)
# n = int(input("n = "))
# lst = [[i] * i for i in range(n)]                              -- var1
# lst = [[i for x in range(i)] for i in range(n)]                -- var2 cu for
# print(lst)

# EX2:
# a)
# lista = [1, 34, 21, 44, 51, 52, 4, 764, 12, 34, 1234]
# lista_noua = sorted(lista)
# print(lista)
# print(lista_noua)
# def criteriu (x):
#     return str(x)
# lista_noua2 = sorted(lista, key = criteriu)
# print(lista_noua2)
# lista_noua3 = sorted(lista, key = lambda x : str(x))
# print(lista_noua3)

# b)
# lista = [1, 34, 21, 44, 51, 52, 4, 764, 12, 34, 1234]
# lista_noua = sorted(lista, key = lambda x : str(x)[::-1])
# print(lista_noua)

# c)
# lista = [1, 34, 21, 44, 51, 52, 4, 764, 12, 34, 1234]
# lista_noua = sorted(lista, key = lambda x : len(str(x)))
# print(lista_noua)

# d)
# lista = [1, 34, 21, 44, 51, 52, 4, 764, 12, 34, 1234]
# lista_noua = sorted(lista, key = lambda x : len(set(str(x))))
# print(lista_noua)

# e)
# lista = [1, 34, 21, 44, 51, 52, 4, 764, 12, 34, 1235, 45, 21, 2543, 1234, 352, 123, 321, 35, 64, 31]
# lista_noua = sorted(lista, key = lambda x: len(str(x)) and int(x))
# print(lista_noua)

# CONTINUARE

# EX1:

# n = int(input("n = "))
# ls1 = [input() for i in range(n)]
# ls2 = [input() for i in range(n)]
# ls1[::2] = ls2[::2]
# print(ls1)

# EX2:

# c = 0
# inceput = 0
# sfarsit = 0
# lista = [1, 3, 5, 6, 0, 1, 4, 6, 7, 3, 1, 5, 6, 1, 6, 0, 1, 4, 5, 0, 1, 4, 6]
# for i in range(len(lista)):
#     if lista[i] == 0 and c == 0:
#         inceput = i
#         c += 1
#     elif lista[i] == 0 and c == 1:
#         sfarsit = i
#         break
# lista[inceput:sfarsit+1] = []
# print(lista)

# EX3:

# ls = [1, 3, 5, 6, 0, 1, 4, 6, 7, 3, 1, 5, 6, 1, 6, 0, 1, 4, 5, 0, 1, 4, 6]
# ls = [x for x in ls if x != 0]
# print(ls)

# EX4:
# ls = [1, 3, 5, 6, 0, 1, 4, 6, 7, 3, 1, 5, 6, 1, 6, 0, 1, 4, 5, 0, 1, 4, 6]
# k = int(input("k = "))
# l = len(ls)
# minim = sum(ls[0:k])
# inceput = 0
# c = 1
# for c in range(1, l - k):
#     sumacurenta = sum(ls[c : k + c])
#     if sumacurenta < minim:
#         minim = sumacurenta
#         inceput = c
# ls = ls[:inceput] + ls[inceput + k :]
# print(ls)

# EX5:
# s = input("vector = ")
# ls = s.split()
# print(ls)
# numere = []
# ultima = -1
# for x in ls:
#     if x != ultima:
#         numere.append(x)
#         ultima = x
# print(numere)

# EX6:
# s = input("vector = ")
# ls = s.split()
# numere = []
# for x in ls:
#     if float(x) > 0:
#         numere.append(x)
#     if float(x) < 0:
#         numere.append(x)
#         numere.append(0)
# print(numere)

# SAU:

# ls = [int(x) for x in input("Dati lista: ").split()]
# c = len(ls)
# i = 0
# while i < c:
#     if ls[i] < 0:
#         list.insert(ls, i+1, 0)
#         c += 1
#     i += 1
# print(ls)


# SORTARI:

# EX1:
# s = input("text = ")
# ls = s.split()
# ls = sorted(ls, key = lambda x : len(str(x)), reverse= True)
# for i in range(len(ls)):
#     if len(str(ls[i])) < 2:
#         indice = i
#         break
# print(ls[:indice])

# EX2:
# s = input("vector = ")
# ls = s.split()
# def sumacifrelor (x):
#     cx = int(x)
#     suma = 0
#     while cx > 0:
#         suma += cx % 10
#         cx //= 10
#     return suma
#
# ls = sorted(ls, key = lambda x: (sumacifrelor(x), -int(x)))
# print(ls)

# EX3:
# a)
# n = int(input("n = "))
# ls = [[]] * n
# for i in range(0,n):
#     linie = input()
#     ls[i] = [x for x in linie.split(maxsplit = 3)]
#     ls[i][3] = [int(x) for x in ls[i][3].split()]
# print(ls)

# b)
# n = int(input("n = "))
# ls = [[]] * n
# for i in range(0,n):
#     linie = input()
#     ls[i] = [x for x in linie.split(maxsplit = 3)]
#     ls[i][3] = [int(x) for x in ls[i][3].split()]
#     contor = 0
#     for x in ls[i][3]:
#         if x >= 5:
#             contor += 1
#     if contor == int(len(ls[i][3])):
#         ls[i].append("TRUE")
#     else:
#         ls[i].append("FALSE")
# print(ls)

# c)
# n = int(input("n = "))
# ls = [[]] * n
# for i in range(0,n):
#     linie = input()
#     ls[i] = [x for x in linie.split(maxsplit = 3)]
#     ls[i][3] = [int(x) for x in ls[i][3].split()]
# ls = sorted(ls, key = lambda x: (int(x[2]), ord(x[0][0])))
# print(ls)

# d)
# n = int(input("n = "))
# ls = [[]] * n
#
# def medie(x):
#     contor = 0
#     suma = 0
#     for j in x:
#         suma += j
#         contor += 1
#     medie = 0
#     medie = suma / contor
#     return float(medie)
#
# def notesub5(x):
#     contor = 0
#     for j in x:
#         if j < 5:
#             contor += 1
#     return int(contor)
#
# for i in range(0,n):
#     linie = input()
#     ls[i] = [x for x in linie.split(maxsplit = 3)]
#     ls[i][3] = [int(x) for x in ls[i][3].split()]
#     contor = 0
#     for x in ls[i][3]:
#         if x >= 5:
#             contor += 1
#     if contor == int(len(ls[i][3])):
#         ls[i].append("true")
#     else:
#         ls[i].append("")
# ls = sorted(ls, key = lambda x: (int(x[2]),-bool(x[4]), -medie(x[3]), notesub5(x[3])))
# print(ls)

# e)
# n = int(input("n = "))
# ls = [[]] * n
# for i in range(0,n):
#     linie = input()
#     ls[i] = [x for x in linie.split(maxsplit = 3)]
#     ls[i][3] = [int(x) for x in ls[i][3].split()]
# def medie(x):
#      contor = 0
#      suma = 0
#      for j in x:
#          suma += j
#          contor += 1
#      medie = 0
#      medie = suma / contor
#      return float(medie)
# for i in range(n):
#     ls_nou = [medie(ls[i][3]) for i in range(n)]
# mediamaxima = max(ls_nou)
# maxim = [ls[i][0] + " " + ls[i][1] for i in range(n) if medie(ls[i][3]) == mediamaxima]
# print(maxim)

# EX4:
# def cheie(x):
#     if int(x) % 2 == 1
#             return 0, x
#     else:
#         return 1, -x
# ls = [4, 5, 7, 1, 5, 2, 3 ,12 , 5, 6, 7, 11, 55, 13, 10, 13, 51, 3 ,13, 5, 6, 7]
# ls = sorted(ls, key = cheie)
# print(ls)

# SAU

# ls = [4, 5, 7, 1, 5, 2, 3 ,12 , 5, 6, 7, 11, 55, 13, 10, 13, 51, 3 ,13, 5, 6, 7]
# ls = sorted(ls, key = lamda x: (0,x) if x % 2 != 0 else (1, -x)
# print(ls)


# MATRICE , VECTORI

# EX1:
# m = int(input("m = "))
# n = int(input("n = "))
# matrix = [input().split(maxsplit=n) for i in range(m)]
# for x in range(m):
#     for y in range(n):
#         print(f"{matrix[x][y]:2}", end = "")
#     print()

#
# EX2:
# m = int(input("m = "))
# n = int(input("n = "))
# matrix = [[int(input()) for j in range(n)] for i in range(m)]
# matrix = sorted(matrix, key = lambda i: i[0])
# for x in range(m):
#      for y in range(n):
#         print(f"{matrix[x][y]:4}", end = "")
#      print()

# EX3:
# n = int(input("n = "))
# maxim = 0
# matrix = [[1]*(i+1) for i in range(n)]
# for i in range(2,n):
#     for j in range(1,i):
#         matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
#         ls_temp = [int(x) for x in str(matrix[i][j])]
#         if len(ls_temp) > maxim:
#             maxim = len(ls_temp)
# for i in range(n):
#     for j in range(i+1):
#         print(f"{matrix[i][j]:{maxim+1}}", end="")
#     print()

# EX4:
# a)
# n = int(input("n = "))
# matrix = [[i*n+j+1 for j in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(f"{matrix[i][j]:3}", end="")
#     print()

# b)
# if n%2 == 0:
#     nr = n//2
# else:
#     nr = n//2 + 1
# st = 0
# dr = n-1
# sus = 0
# jos = n-1
# ls_poz = []
# dir = 0
# while(st <= dr and sus <= jos):
#         if dir == 0:
#             for i in range(st,dr+1):
#                 ls_poz.append((sus , i))
#             dir = 1
#             sus += 1
#         elif dir == 1:
#             for i in range(sus,jos+1):
#                 ls_poz.append((i , dr))
#             dir = 2
#             dr -= 1
#         elif dir == 2:
#             for i in range(dr, st-1, -1):
#                 ls_poz.append((jos , i))
#             dir = 3
#             jos -= 1
#         elif dir == 3:
#             for i in range(jos, sus-1, -1):
#                 ls_poz.append((i , st))
#             dir = 0
#             st += 1
# print(ls_poz)

# c)
# spirala = []
# for i in ls_poz:
#     st, dr = i
#     spirala.append(matrix[st][dr])
# print(spirala)

# EX5:
# n = int(input("n = "))
# ls = []
# if n == 0 or n == 1:
#     print(f"Nu exista numere prime mai mici sau egale cu {n}")
# else:
#     ls.append(2)
#     for x in range(2, n+1):
#         c = 0
#         for i in range(2, x//2 + 2):
#             if x % i == 0:
#                 c += 1
#         if c == 0:
#             ls.append(x)
#     print(ls)

# EX6:
# m1 = {int(x) for x in input("Multimea1: ").split()}
# m2 = {int(x) for x in input("Multimea2: ").split()}
#
# # intersectia:
# m4 = { x for x in m1 if x in m2}
# print(f"Intersectie: {m4}")
#
# # reuniunea:
# m3 = { x for x in (m1 or m2)}
# print(f"Reuniune: {m3}")

n = int(input("n = "))
m = int(input("m = "))
sir = "1 0 0 0 0 0 3 0 0 0 0 0 0 4 5"
i = 0
v = [0 for i in range(n+1)]
lg_sir = 3*n
ls  = [int(x) for x in sir.split()]
for x in ls:
    v[x]+=1
print(v)
for nr in range(1,n):
    func1(nr)

def func1(nr):
    if v[nr] < 3:
        func2(nr)

def func2()





