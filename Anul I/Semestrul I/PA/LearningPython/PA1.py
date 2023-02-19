# Subiectul 1

# def vocale(*args):
#     d = {}
#     ls = []
#     lista_rez = [x for x in args if x[0] == x[-1]]
#     for arg in args:
#         nrvocale = 0
#         for x in arg:
#             if x in "aeiou":
#                 nrvocale += 1
#         ls.append((arg,nrvocale))
#     ls = sorted(ls, key=lambda x: x[1])
#     d = {j[1]: [i[0] for i in ls if i[1] == j[1]] for j in ls}
#     print(d)
#     print(lista_rez)
#
# vocale("acasa","masa","scaun","oaie","oare","este")


# Subiectul 2

# ls = [int(x) for x in input("Numerele intregi: ").split()]
# n = len(ls)
# ls = sorted(ls, key=lambda x: int(x))
# print(ls)
# nrneg, nrpoz, nrzero = 0, 0, 0
# for x in ls:
#     if x<0:
#         nrneg += 1
# produs = 1
#
# for i in range(0,2*(nrneg//2)):
#     ls[i] = ls[i]*-1
#
# print(ls)
# for x in ls:
#     if x > 0:
#         produs *= x
# print(produs)



# Subiectul 4

# def back(k):
#     global nr
#     if k==6:
#         par,impar = 0,0
#         for i in x:
#             if par == 1 and impar == 1:
#                 break
#             if i%2 == 0:
#                 par = 1
#             else:
#                 impar = 1
#         if par == 1 and impar == 1:
#             nr+=1
#             print(*x,sep=',')
#     elif k==0:
#         for i in range(1,n+1):
#             x[k]=i
#             back(k+1)
#     else:
#         for i in range(x[k-1]+2,n+1):
#             if i==13:
#                 continue
#             x[k] = i
#             back(k+1)

# n = int(input("n = "))
# x = [0 for x in range(6)]
# nr = 0
# back(0)
# print(nr)