from collections import defaultdict

interval = tuple(map(int, input().split()))
n = int(input())
intervale = defaultdict(tuple)
for i in range(n):
    intervale[i + 1] = tuple(map(int, input().split()))

intervale = sorted(intervale.items(), key=lambda x: (x[1][0], -x[1][1]))

sol = [intervale[0][0]]
last = intervale[0][1][1]
for i in range(1, n):
    if intervale[i][1][0] == last:
        sol.append(intervale[i][0])
        last = intervale[i][1][1]

if last < interval[1]:
    print(0)
else:
    print(len(sol))
    print(*sol)
