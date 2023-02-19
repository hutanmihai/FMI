# Am ales metoda backtracking deoarece generez element cu element toate solutiile ce respecta conditiile date, in mod recursiv.
# Reprezentarea solutiei se va face in vectorul x cu elementele x0,x1...,xk
# Orice element xk poate lua valori de la 1, lungimea tevii div 2 + 1
# Conditiile finale sunt: sa fim pe pozitia k>= 2 deoarece nu avem voie sa avem teava netaiata, si ca suma sa fie egala cu lungimea tevii netaiate
# Conditiile de continuare sunt: xk >= xk-1 pentru ca sa nu generam modalitati de taieri identice dar in ordine diferita, suma curenta sa fie mai mica sau egala decat lungimea tevii (p) si x[k] sa fie divizor al lui p


def back(k):
    global S
    if S == p and k>=2 and len(set(x[:k])) == 2:
        print(*x[:k],sep="+")
    elif k == 0:
        for i in range(1,p//2+1):
            if S+i <= p:
                S += i
                x[k] = i
                back(k+1)
                S -= x[k]
    else:
        for i in range(1,p//2+1):
            if x[k-1]<=i  and S+i <= p and p%i == 0:
                S += i
                x[k] = i
                back(k+1)
                S -= x[k]

p = int(input("p = "))
S = 0
x = [0 for j in range(p)]
back(0)

# b)
