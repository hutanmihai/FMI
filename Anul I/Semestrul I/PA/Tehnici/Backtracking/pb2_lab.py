def back(k):
    if k == n:
        print(*x,sep=',')
    else:
        for i in v[k]:
            x[k] = i
            back(k+1)

n = int(input("Numar multimi: "))
cn = n
v = []
while cn:
    v.append([int(x) for x in input("Multime: ").split()])
    cn -= 1
x = [0 for i in range(n)]
back(0)