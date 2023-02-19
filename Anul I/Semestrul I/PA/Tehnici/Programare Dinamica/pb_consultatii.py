pozinit = int(input("Coloana de pe care pleaca beduinul: "))
m,n = int(input("m = ")), int(input("n = "))
mat = [[int(j) for j in input().split()] for i in range(m)]
print(mat)
pozinit += 1
for linie in mat:
    linie.append(0)
    linie.insert(0,0)

dp = [[999999 for j in range(n+2)] for i in range(m)]

dp[m-1][pozinit] = 0



