# Folosesc metoda greedy, metoda ce imi genereaza solutia pas cu pas, iar la fiecare pas extrag din vectorul sortat elementul cel mai optim pentru acel moment din program.
# Complexitate:

n = int(input("n = "))
g = float(input("g = "))
ob = []
ls = []
sol = []
nr = 0
cn = n

while cn:
    greutate = float(input(f"Greutatea obiectului cu nr {n-cn+1}: "))
    ob.append(greutate)
    cn -= 1
for i in range(len(ob)):
    ls.append([i+1])
    ls[i].append(ob[i])
ls = sorted(ls, key=lambda x: x[1])
print(ls)
for i in range(1,len(ls)):
    if abs(ls[i][1] - ls[i-1][1]) <= g:
        sol.append([ls[i-1][0]])
        sol[nr].append(ls[i][0])
        nr += 1
        ls[i][1] = 99999999

print(nr)
for x in sol:
    print(*x,sep="+")
