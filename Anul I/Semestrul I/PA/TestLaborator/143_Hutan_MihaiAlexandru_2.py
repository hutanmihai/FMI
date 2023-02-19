def citire_matrice(numefisier):
    f = open(numefisier, 'r')
    s = -1
    ls = list()
    while s:
        s = f.readline().rstrip('\n').split()
        ls.append([x for x in s])
    ls.pop()
    f.close()
    return ls

def f(matrice, ch, *args):
    if ch=="d":
        for i in range(len(matrice)):
            for c in range(len(matrice[i])):
                if i+c == len(matrice)-1:
                    matrice[i][c], matrice[i][i] = matrice[i][i], matrice[i][c]
    elif ch=="l":
        ls = []
        for x in args:
            ls.append(x)
        x = ls[0]
        y = ls[1]
        matrice[x], matrice[y] = matrice[y], matrice[x]
    return matrice

matrice = citire_matrice("date.in")
g = open("date.out", 'w')
n = len(matrice)
for x in range(n//2):
    matrice = f(matrice, "l", x, n-x-1)
matrice = f(matrice, "d")

for coloana in range(n):
    if coloana % 2 == 0:
        for linie in range(n-1,-1,-1):
            g.write(matrice[linie][coloana])
            g.write(" ")
    else:
        for linie in range(n):
            g.write(matrice[linie][coloana])
            g.write(" ")
g.close()
