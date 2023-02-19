# PROBLEMA A

# n = int(input(" Numar activitati: "))
# ls = [int(x) for x in input("Duratele activitatilor: ").split()]
# t = [(i+1, ls[i]) for i in range(len(ls))]
# print(t)
# t = sorted(t, key=lambda x: x[1])
# print(t)
#
# suma = 0
# lssume = []
# print("Activitatile vor lua loc in urmatoare ordine: ",end='')
# for x in t:
#     print(x[0],end=" ")
#     suma += x[1]
#     lssume.append(suma)
# suma = 0
# for x in lssume:
#     suma += x
# print(f"Timpul mediu de asteptare este de {suma/n:.2f}")

# PROBLEMA B

# n = int(input("Numar spectacole = "))
# lstimpi = [int(timp) for timp in input("Intervale = ").split()]
# print(lstimpi)
# i = 0
# j = 0
# ls = []
#
# while i < n*2:
#     j += 1
#     ls.append((j,lstimpi[i],lstimpi[i+1]))
#     i += 2
# print(ls)
#
# ls = sorted(ls,key=lambda x: (x[2],x[1]))
# print(ls)
#
# print("Activitatile ce vor avea loc astazi sunt urmatoarele: ",end='')
# print(ls[0][0], end=', ')
# ua = ls[0]
# for x in ls:
#     if x[1] >= ua[2]:
#         print(x[0], end=', ')
#         ua = x

# PROBLEMA C

