# EX1:
# a = 45
# b = 75
# for i in range(0,99):
#     if i == 100:
#         break
#     if i % 5 == 0 and (i < a or i > b):
#         print(f"{i} ", end="")

# EX2:
# a = int(input("a = "))
# b = int(input("b = "))
# nr1 = 0
# nr2 = 1
# while (nr2 < a):
#     nr1, nr2 = nr2, nr2 + nr1
# if nr2 > b:
#     print("Nu exista numar fibonacci in acest interval")
# else:
#     print(nr2)

# EX3:
# n = int(input("n = "))
# nr1 = 0
# nr2 = 1
# while nr2 <= n:
#     nr2, nr1 = nr1 + nr2, nr2
# nr2, nr1 = nr1, nr2 - nr1
#
# while n > 0:
#     if (n - nr2) >= 0:
#         n -= nr2
#         print(nr2, end="+")
#         nr2, nr1 = nr1, nr2 - nr1
#         nr2, nr1 = nr1, nr2 - nr1
#     else:
#         nr2, nr1 = nr1, nr2 - nr1

# EX4:
# bancnote = [1, 5, 10 ,25]
# n = int(input("n = "))
# i = len(bancnote) - 1
# while n > 0:
#     counter = 0
#     if n - bancnote[i] >= 0:
#         while n - bancnote[i] >= 0:
#             n -= bancnote[i]
#             counter += 1
#     print(f"{counter} x {bancnote[i]}")
#     i -= 1

# EX5:
# n = int(input("n = "))
# primul = int(input("primul = "))
# minim = primul
# maxim = primul
# n -= 1
# while n > 0:
#     curent = int(input())
#     if curent > maxim:
#         maxim = curent
#     elif curent < minim:
#         minim = curent
#     n -= 1
# print(minim, maxim)

# EX6:
# s = input("cuvant = ")
# if len(s) % 2 == 0 and s == s[::-1]:
#     print(f"{s} este semipalindrom")
# elif len(s) % 2 == 1 and s == s[::-1]:
#     print(f"{s} este palindrom")
# else:
#     print(f"{s} nu este palindrom")

# EX7:
# s = input("cuvant = ")
# k = int(input("k = "))
# s_nou = s[0:k:] + s[k+1::]
# print(s_nou)

# EX8:
# s = input("cuvant = ")
# voc = "aeiouAEIOU"
# for i in range(len(s)):
#     if s[i] in voc:
#         s_nou = s[:i] + s[i+1:]
#         break
# print(s_nou)

# EX9:
# w = input("cuvant = ")
# p = int(input("p = "))
# n = int(input("n = "))
# sf = str(w[len(w) - p :])
# print(sf)
# while n > 0:
#     curent = str(input("curent = "))
#     if (curent.endswith(sf)) and (len(curent) >= p + 2) :
#         print(curent)
#     n -= 1

# EX10:
# s = input("s = ")
# for i in range(1, len(s) // 2 + 1, 1):
#     if len(s) % i == 0:
#         t = s[:i]
#         k = len(s) // i
#         if s == t * k:
#             print(f"Sirul gasit este {t} si se repeta de {k} ori")
#             break









