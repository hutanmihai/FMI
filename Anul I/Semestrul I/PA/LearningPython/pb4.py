def back(k):
    global suma
    if suma == s and k == n:
        print(*x[:k],sep='')
    elif k == 0:
        for i in range(1,10):
            if suma+i<=s:
                suma += i
                x[k] = i
                back(k+1)
                suma -= x[k]
    else:
        for i in range(10):
            if suma+i<=s and k<=n:
                x[k] = i
                suma += i
                back(k+1)
                suma -= x[k]

n = int(input("n = "))
s = int(input("s = "))
suma = 0
x = [0 for j in range(n+1)]
back(0)