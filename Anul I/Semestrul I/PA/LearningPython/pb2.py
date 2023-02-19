# Aranjamente - conteaza ordinea
# Submultimi distincte ale caror elemente dau suma m
# Reprezentare solutie: x0,x1,...,xk - cu x0+x1+..xk=m
# xk poate lua valori de la 1 la n
# Cond finala: x1+x2+x3+...+xk == m si valorile din x sa fie ordonate crescator
# Conditie de continuare: x0+x1+...+xk <= m si xk > x[k-1]

def back(k):
    global suma
    if suma == m:
        print(*x[:k])
    elif k == 0:
        for i in multime:
            if suma+i <= m:
                suma += i
                x[k] = i
                back(k+1)
                suma -= x[k]
    else:
        for i in multime:
            if x[k-1]<=i  and suma+i <= m:
                suma += i
                x[k] = i
                back(k+1)
                suma -= x[k]

m = int(input("m = "))
multime = [int(x) for x in input("Multimea data: ").split()]
print(multime)
suma = 0
x = [0 for j in multime]
back(0)