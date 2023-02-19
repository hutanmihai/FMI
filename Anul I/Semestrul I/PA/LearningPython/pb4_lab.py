def isprime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3,int(num**1/2)+1,2):
            if num % i == 0:
                return False
    return True

def back(k):
    global suma
    ultima = 0
    if suma == n:
        print(*x[:k],sep="+")
    else:
        for i in range(n+1):
            if isprime(i) == True and suma + i <= n and i >= x[k-1]:
                x[k] = i
                suma += i
                back(k+1)
                suma -= x[k]

n = int(input("n = "))
suma = 0
cn = n
x = [0 for i in range(n)]
back(0)
