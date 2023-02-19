# Folosesc metoda backtracking, metoda ce imi genereaza element cu element in mod recursiv toate solutiile posibile ce respecta conditiile date.
# Reprezentarea solutiei se va face in vectorul x, cu elementele x0,x1...,xm-1
# Fiecare element xk poate la valori: de la 1 la 9 pt k==0 si de la 0 la 9 pt k!=0
# Conditii de continuare la pasul k: daca nu ne aflam pe prima sau pe ultima pozitie a vectorului solutie conditia de continuare este ca valoarea absoluta a diferentei dintre elementul curent si cel anterior sa fie <=1, in plus la ultima pozitie mai avem o conditie, cea ca valoarea absoluta a diferentei ultimului elem din vector si a primului sa fie <= 1
# Conditii finale: sa fim pe pozitia k==m, doar atat deoarece conditiile de continuare sunt suficiente


def back(k):
    if k==m:
        print(*x,sep='')
    elif k==0:
        for i in range(1,10):
            x[k]=i
            back(k+1)
    elif k==m-1:
        for i in range(0,10):
            if abs(i-x[k-1]) <= 1 and abs(i-x[0]) <= 1:
                x[k] = i
                back(k+1)
    else:
        for i in range(0,10):
            if abs(i-x[k-1]) <= 1:
                x[k] = i
                back(k+1)

m = int(input("m = "))
x = [0 for i in range(m)]
back(0)


# b) and i % 2 == 0 in if ul de la elif k==m-1