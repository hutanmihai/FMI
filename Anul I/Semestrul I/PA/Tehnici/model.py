# Subiectul 1

# a)
# def isprim(num):
#         if num <= 1:
#             return False
#         elif num == 2:
#             return True
#         elif num % 2 == 0:
#             return False
#         else:
#             for i in range(3, int(num ** 1 / 2) + 1, 2):
#                 if num % i == 0:
#                     return False
#         return True

# def divizori(*args):
#     d = {}
#     for arg in args:
#         d[arg] = [int(x) for x in range(2,int(arg**1/2)) if arg % x == 0 and isprim(x) == True]
#     print(d)

# divizori(50,21)

# b)
# litere_10 = [chr(x) for x in range(97,107)]
# print(litere_10)


# Subiectul 2:
# n = int(input("Numarul spectacolelor: "))
# cn =  n
# ls = []
# while cn:
#     ls.append((int(input(f"Ora inceput spectacol nr{n-cn+1}: ")),int(input(f"Ora sfarsit: "))))
#     cn -= 1
# nr = 0
# ls = sorted(ls, key=lambda x: (x[1],int(x[1]-x[0])))
# nr += 1
# ultima = ls[0][1]
# for i in range(1,len(ls)):
#     if ls[i][0] >= ultima:
#         nr += 1
#         ultima = ls[i][1]
# print(nr)







# Subiectul 4:

# def back(k):
#     if k==n:
#         print(*x,sep=',')
#     else:
#         for i in range(1,n+1):
#             if i not in x:
#                 x[k]=i
#                 back(k+1)
#                 x[k]=0

# n = int(input("n = "))
# x = [0 for x in range(n)]
# print(x)
# back(0)


