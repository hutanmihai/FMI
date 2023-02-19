def back(k):
    global suma
    if k == a:
        if suma == p:
            print("Intrebarile ",end="")
            print(*x,sep=",")
    else:
        for intrebare in lsmare:
            if intrebare[0] not in x and suma+intrebare[1]<=p and intrebare[0]>x[k-1]:
                x[k]=intrebare[0]
                suma += intrebare[1]
                back(k+1)
                suma -= intrebare[1]
                x[k] = 0

n = int(input("Numarul intrebarilor: "))
a = int(input("Numarul intrebarilor distincte/chestionar: "))
p = int(input("Punctaj maxim: "))
cn = n
lsmare = []
while cn:
    ls = [int(x) for x in input(f"Intrebarea (nr) are punctajul (nr): ").split()]
    lsmare.append(ls)
    cn -= 1
suma = 0
x = [0 for i in range(a)]
back(0)