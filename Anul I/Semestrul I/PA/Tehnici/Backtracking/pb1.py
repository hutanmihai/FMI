# Combinari de n luate cate n
# Submultimi distincte cu n elemente (n == lungimea cuvantului)
# Reprezentare solutie: x0,x1,x2...xn-1 - o submultime cu n elemente
# Fiecare pozitie xk poate lua ca valoare orice litera din cuvant
# Cond finale: elementele apar de exact atatea ori de cate ori apar si in input
# Cond de continuare: sa nu se fi folosit deja acea litera de m-ori (m = numarul aparitiilor in input)

def back(k):
    if k == n:
        anagrama = ''.join(x)
        print(anagrama)
    else:
        for litera in ls:
            if d[litera] != 0:
                x.append(litera)
                d[litera] -= 1
                back(k+1)
                d[litera] += 1
                x.pop()

cuv = input("Cuvantul: ")
ls = [i for i in cuv.rstrip("\n")]
print(ls)
n = len(ls)
d = {x:0 for x in ls}
x = []
for m in ls:
    d[m]+=1
back(0)
