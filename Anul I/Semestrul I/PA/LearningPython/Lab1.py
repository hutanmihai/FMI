# OPERATORII PE BITI:

# EX1:

# a)

# V1:
# n = int(input("n = "))
# x = 1
# print(bin(n))
# while x < n:
#     x = (x << 1)
# if x == n:
#     print(n, "este o putere de 2")
# else:
#     print(n, "nu este o putere de 2")

# V2:
# n = int(input("n = "))
# if n & n - 1 == 0:
#     print(f" {n} este putere de 2")
# else:
#     print(f" {n} nu este putere de 2")

# V3:
# n = int(input("n = "))
# print(bin(n))
# cn = n
# while cn & 1 == 0:
#     cn = cn >> 1
# if cn == 1:
#     print(f" {n} este putere a lui 2")
# else:
#     print(f" {n} nu este putere de 2")

# b)
# n = int(input("n = "))
# print(bin(n))
# cn = n
# k = 0
# while cn & 1 == 0:
#     cn = cn >> 1
#     k += 1
# if cn == 1:
#     print(f" {n} este putere a lui {k}")
# else:
#     print(f" {n} nu este putere de {k}")


# EX2:
# n = int(input("n = "))
# print(bin(n))
# ans = 0
# i = 1
# while n:
#     x = int(input("x = "))
#     ans = ans ^ x
#     n = n - 1
# print(ans)



# EX3:

# V1:
# n = int(input("n = "))
# print(bin(n))
# nr = 0
# cn = n
# while cn:
#     if cn & 1 == 1:
#         nr = nr + 1
#     cn = cn >> 1
# print(f"{n} are {nr} biti de 1")

# V2:
# n = int(input("n = "))
# print(bin(n))
# cn = n
# nr = 0
# while cn:
#     nr = nr + 1
#     cn = cn & (cn - 1)
# print(f"{n} are {nr} biti de 1")


# OPERATORII ARITMETICI

# EX1:
# n = int(input("n = "))
# cn = n
# inv = 0
# while cn:
#     inv = inv * 10 + cn % 10
#     cn //= 10
# if inv == n:
#     print(f"{n} este palindrom")
# else:
#     print(f"{n} nu este palindrom")

# EX2:
# n = int(input("n = "))
# zia = float(input("curs ieri = "))
# n = n - 1
# max = -1.0
# i = 1
# while i <= n:
#     zib = float(input("curs azi = "))
#     if zib - zia > max:
#         max = zib - zia
#         poz1 = i
#         poz2 = i+1
#     zia = zib
#     i = i + 1
# print(f"cea mai mare diferenta de curs este {max} si are loc intre zilele {poz1} si {poz2}")

# EX4:
# n = int(input("n = "))
# max1 = None
# max2 = None
# while n:
#     x = int(input("x = "))
#     if max1 == None or x > max1:
#         max2 = max1
#         max1 = x
#     elif max2 == None or x > max2:
#         max2 = x
#     n = n - 1
# if max1 != max2:
#     print(f"{max1} {max2}")
# else:
#     print("Imposibil")


# TEMA

# OPERATORII PE BITI:

# EX4:

# V1:
# n = int(input("n = "))
# print(bin(n))
# nr = 0
# nrmax = 0
# while n:
#     if n & 1 == 1:
#         nr = nr + 1
#         if nr > nrmax:
#             nrmax = nr
#     else:
#         nr = 0
#     n = n >> 1
# print(f"cel mai mare sir de 1 din reprezentarea binara a lui n este de {nrmax}")

# V2:
# n = int(input("n = "))
# print(bin(n))
# cn = n << 1
# nr = 0
# aux = None
# while cn:
#     cn = n & cn
#     cn = cn << 1
#     nr += 1
# print(f"cel mai mare sir de 1 din reprezentarea binara a lui n este de {nr}")

# EX5:
# x = int(input("x = "))
# y = int(input("y = "))
# print(bin(x))
# print(bin(y))
# aux = x ^ y
# nr = 0
# while aux:
#     if aux & 1 == 1:
#         nr += 1
#     aux = aux >> 1
# print(f"este nevoie de {nr} operatii astfel incat x sa devina y in reprezentarea lor binara")

# EX 6:
# n = int(input(" n = "))
# cn = n
# aux = 1
# while cn:
#     aux = aux * 2
#     cn = cn - 1
# aux = aux - 1
# while aux:
#     caux = aux
#     nr = 1
#     while caux:
#         if caux & 1 == 1:
#             print(nr, end=',')
#         nr = nr + 1
#         caux = caux >> 1
#     print(" ")
#     aux = aux - 1

# EX5:
# import math
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# delta = b * b - 4 * a * c
# if delta > 0:
#     r1 = (-b + math.sqrt(delta)) / (2 * a)
#     r2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f"ecuatia are doua radacini reale de valoare {r1} respectiv {r2}")
# elif delta == 0:
#     r = -b / (2 * a)
#     print(f"ecuatia are o singura radacina reala de valoare {r}")
# else:
#     print("Ecuatia nu are radacini")

# EX6:

# a)
# n = int(input("n = "))
# cn = n
# nrmax = 0
# while cn:
#     if cn % 10 == 9:
#         nrmax = nrmax * 10 + 9
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 8:
#         nrmax = nrmax * 10 + 8
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 7:
#         nrmax = nrmax * 10 + 7
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 6:
#         nrmax = nrmax * 10 + 6
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 5:
#         nrmax = nrmax * 10 + 5
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 4:
#         nrmax = nrmax * 10 + 4
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 3:
#         nrmax = nrmax * 10 + 3
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 2:
#         nrmax = nrmax * 10 + 2
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 1:
#         nrmax = nrmax * 10 + 1
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 0:
#         nrmax = nrmax * 10 + 0
#     cn = cn // 10
# print(f"numarul maxim ce poate fi format din cifrele lui n este {nrmax}")

# b)
# n = int(input("n = "))
# cn = n
# nrmin = 0
# while cn:
#     if cn % 10 == 1:
#         nrmin = nrmin * 10 + 1
#         break
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 0:
#         nrmin = nrmin * 10 + 0
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 1:
#         nrmin = nrmin * 10 + 1
#     cn = cn // 10
# if nrmin % 10 == 1:
#     nrmin =  nrmin // 10
# while cn:
#     if cn % 10 == 2:
#         nrmin = nrmin * 10 + 2
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 3:
#         nrmin = nrmin * 10 + 3
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 4:
#         nrmin = nrmin * 10 + 4
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 5:
#         nrmin = nrmin * 10 + 5
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 6:
#         nrmin = nrmin * 10 + 6
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 7:
#         nrmin = nrmin * 10 + 7
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 8:
#         nrmin = nrmin * 10 + 8
#     cn = cn // 10
# cn = n
# while cn:
#     if cn % 10 == 9:
#         nrmin = nrmin * 10 + 9
#     cn = cn // 10
# print(f"cel mai mic numar ce poate fi format din cifrele lui n este {nrmin}")

# EX3:
# L1 = int(input("L1 = "))
# L2 = int(input("L2 = "))
# S = L1 * L2
# if L1 > L2:
#     l = L2
# else:
#     l = L1
# while L1 % l != 0 or L2 % l != 0:
#     l = l - 1
# nrbuc = S / l ** 2
# print(f"se folosesc {nrbuc} bucati de gresie de latime {l}")








