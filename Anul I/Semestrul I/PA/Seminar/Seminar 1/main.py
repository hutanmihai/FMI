# EX1:
# x = int(input("n = "))
# xdiv4 = x>>2
# xx6 = (x << 2) + (x << 1)
# print(xdiv4)
# print(xx6)

# EX2:
# a = int(input("a = "))
# b = int(input("b = "))
# nr1 = 0
# nr2 = 1
# i = 0
# while i <= a:
#     i = nr1 + nr2
#     nr1 , nr2 = nr2 , i
# if i <= b:
#     print(i)
# else:
#     print("Nu exista.")

# EX3:
# n = int(input("n = "))
# nr1 = 0
# nr2 = 1
# while nr2 <= n:
#     nr1 , nr2 = nr2 , nr1 + nr2
# while n:
#     if nr1 <= n:
#         n -= nr1
#         print(nr1 , end=" + ")
#     nr1 , nr2 = nr2 - nr1 , nr1

# EX4:
# a)
# x=0b1001
# k=2
# x = x | (1 << (k-1))
# print(bin(x))

# b)
# x=0b1011
# k=2
# x = x & (~ (1 << (k-1)))
# print(bin(x))

# c)
# x=0b1001 # x=0b1011
# k=2
# x = x ^ (1 << (k-1))
# print(bin(x))

# EX5:
# V1:
# n = int(input("n = "))
# aux = n
# k = 0
# while (aux>0) and (aux & 1 == 0): #cat timp ultimul bit este 0
#     aux = aux >> 1
#     k = k + 1
#     if aux == 1:
#         print(n, " = 2**", k, sep="")
#     else:
#         print(n, "nu este o putere a lui 2")

# V2:
# import math
# n = int(input("n = "))
# if (n>0) and (n & (n-1) == 0):
#     print(n, "=2**", int(math.log2(n)), sep="")
# else:
#     print(n, "nu este o putere a lui 2")

# EX6:


