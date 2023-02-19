# Folosesc metoda backtracking, metoda ce imi genereaza pas cu pas toate solutiile posibile ce respecta conditiile date
# Reprezentarea solutiei se va face in lista x0,x1,...,xn-1
# Conditia finala: parcurgerea listei solutiei sa ajunga pe pozitia n-1 si Suma dorita sa fie egala cu suma curenta
# Conditia de continuare: suma curenta <= Suma dorita
# xk poate lua orice valoare atata timp cat suma este <= Suma dorita

# a)
# def back(k):
#     global suma
#     if k == n:
#         if S == suma:
#             print(*x, sep=",")
#     else:
#         for i in range(v[k]+1):
#             x[k] = i
#             suma += i*monede[k]
#             if suma <= S:
#                 back(k+1)
#             suma -= i*monede[k]
#
# S = int(input("Suma: "))
# n = int(input("Tipuri de monede: "))
# monede = [int(x) for x in input("Valorile monedelor: ").split()]
# suma = 0
# v = [S//j for j in monede]
# x = [0 for i in range(n)]
# back(0)

# b)
def back(k):
    global suma
    if k == n:
        if S == suma:
            print(*x, sep=",")
    else:
        for i in range(v[k]+1):
            x[k] = i
            suma += i*monede[k]
            if suma <= S:
                back(k+1)
            suma -= i*monede[k]

S = int(input("Suma: "))
n = int(input("Tipuri de monede: "))
monede = [int(x) for x in input("Valorile monedelor: ").split()]
suma = 0
v = [int(x) for x in input("Numarul de monede de fiecare tip: ").split()]
x = [0 for i in range(n)]
back(0)