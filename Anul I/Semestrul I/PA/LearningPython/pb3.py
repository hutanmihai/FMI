def back(p):
    if p == k:
        print(*x[:k])
    elif p == 0:
        for i in range(1,n+1):
            x[p]=i
            back(p+1)
    elif p == 1:
        for i in range(n+1,n+m+1):
            x[p] = i
            back(p+1)
    else:
        for i in ls:
            if i not in x:
                x[p] = i
                back(p+1)

n = int(input("nrfete: "))
m = int(input("nrbaieti: "))
k = int(input("nrelevi in echipe: "))
ls = [i for i in range(1,n+m+1)]
print(*ls)
x = [0 for j in range(k+1)]
back(0)



