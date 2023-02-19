# Subiect 1


# Subiectul 4

# def back(k):
#     global n
#     global m
#     global suma
#     if k==m:
#         if suma==n:
#             print(*x)
#     else:
#         for i in range(1, cap[k]+1):
#             if suma + i <= n:
#                 x[k] = i
#                 suma += x[k]
#                 back(k+1)
#                 suma -= x[k]
#
# n = int(input("Numar excursionisti: "))
# cap = [int(x) for x in input("Capacitatile corturilor: ").split()]
# m = len(cap)
# x = [0 for i in range(m)]
# suma = 0
# back(0)