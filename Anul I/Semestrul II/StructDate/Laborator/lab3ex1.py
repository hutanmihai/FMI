# n = int(input())
# ls = []
# batut = []
# cuie = 0
# for i in range(n):
#     ls.append(list(map(int,input().split())))
# for x in ls:
#     if x[0]>x[1]:
#         (x[0],x[1])=(x[1],x[0])
#
# ls_sorted = sorted(ls,key=lambda x: (int(x[0]),int(x[1])))
# intersection = list(ls_sorted[0])
#
# if n>1:
#     for i in range(1,n):
#         if intersection[0]<=ls_sorted[i][0]<=ls_sorted[i][1]<=intersection[1]:
#             intersection=ls_sorted[i]
#             if i == n-1:
#                 cuie += 1
#                 batut.append(intersection[1])
#         elif intersection[0]<=ls_sorted[i][0]<=intersection[1]:
#             intersection[0] = ls_sorted[i][0]
#             if i == n-1:
#                 cuie += 1
#                 batut.append(intersection[1])
#         elif intersection[0]<=ls_sorted[i][1]<=intersection[1]:
#             intersection[1]=ls_sorted[i][1]
#             if i == n-1:
#                 cuie += 1
#                 batut.append(intersection[1])
#         else:
#             cuie += 1
#             batut.append(intersection[1])
#             intersection = ls_sorted[i]
#             if i == n-1:
#                 cuie += 1
#                 batut.append(intersection[1])
#     print(int(cuie))
#     print(*batut)
# else:
#     print(1)
#     print(intersection[1])