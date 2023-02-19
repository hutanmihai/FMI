entr=0.0


n=(int(input("Dati nr de evenimente: ")))

import math

for i in range(n):
    p=float(input())
    entr+=-(p * math.log(p,2))

print(entr)