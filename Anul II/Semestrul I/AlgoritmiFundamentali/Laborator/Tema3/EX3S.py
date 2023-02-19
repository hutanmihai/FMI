"""
Pentru rezolvarea acestei probleme am folosit din nou o abordare precum cea a cuplajului maxim, folosind algoritmul
 lui Edmonds-Karp. Detalii despre rezolvarea problemei sunt scrise pe parcursul codului.
Complexitatea algoritmului este: O(n^2*logn)
"""


from collections import deque, defaultdict


def bfs(capacity, start, end, parents):
    q = deque()
    q.append(start)
    parents[start] = None
    while q:
        current = q.popleft()
        for vecin in capacity[current]:
            if vecin not in parents and capacity[current][vecin] > 0:
                q.append(vecin)
                parents[vecin] = current
                if vecin == end:
                    return True
    return False


def edmonds_karp(capacity, start, end):
    parents = {}
    while bfs(capacity, start, end, parents):
        current = end
        bottleneck = float("inf")
        while current != start:
            previous = parents[current]
            bottleneck = min(bottleneck, capacity[previous][current])
            current = previous

        current = end
        while current != start:
            previous = parents[current]
            capacity[previous][current] -= bottleneck
            capacity[current][previous] += bottleneck
            current = previous

        parents = {}


# Cream lista cu toate numerele prime pana la 2000001, si retinem True daca este prim, False daca nu
# Pentru optimizarea timpului, (efect negativ asupra memoriei), dar este un tradeoff bun in problema aceasta
prime_numbers = [True] * 200001
for i in range(2, int(200000 ** 0.5) + 1):
    k = i
    if prime_numbers[i] is True:
        while k * i < 200001:
            prime_numbers[k * i] = False
            k += 1


# Citirea
n = int(input())
numbers = list(map(int, input().split()))
capacity = defaultdict(lambda: defaultdict(int))
start = 100001
end = 100002


# Legam numerele pare de start si cele impare de end (utilizam numerele sub forma unui graf bipartit par, impar)
for x in numbers:
    if x % 2 == 0:
        capacity[start][x] = 1
        capacity[x][start] = 0
    else:
        capacity[x][end] = 1
        capacity[end][x] = 0


# Am format graful bipartit astfel deoarece o suma intre par si par sau impar si impar este mereu para, deci nu poate
# da un numar prim (exceptand 2, dar ne este specificat in constraints ca numerele date sunt mai mari sau egale cu 2)

# Iteram toate numerele doua cate doua si vedem daca sunt prime
for i, vali in enumerate(numbers):
    for j, valj in enumerate(numbers[i + 1:]):
        suma = vali + valj
        # Daca suma celor doua da un numar prim, le legam in graf cu capacitatea 1, cu arcul par -> impar
        if prime_numbers[suma]:
            if vali % 2 == 0:
                capacity[vali][valj] = 1
                capacity[valj][vali] = 0
            else:
                capacity[valj][vali] = 1
                capacity[vali][valj] = 0

# Aplicam algoritmul lui Edmonds-Karp
edmonds_karp(capacity, start, end)

visited = set()
for x in capacity:
    if x == start or x == end:
        continue
    # Parcurgem folosind un BFS graful din fiecare nod par care are capacitatea reziduala ramasa 0 din start
    # si il marcam ca vizitat, si mai marcam nodurile impare care au capacitatea reziduala ramasa 0 din nodul par
    if x % 2 == 0:
        if capacity[x][start] == 0:
            coada = deque()
            coada.append(x)
            visited.add(x)
            while coada:
                current = coada.popleft()
                for vecin in capacity[current]:
                    if vecin == start or vecin == end or vecin in visited:
                        continue
                    if capacity[vecin][current] == 0:
                        if vecin not in visited:
                            coada.append(vecin)
                            visited.add(vecin)


numbers_to_remove = []
for x in capacity:
    if x == start or x == end:
        continue

    # Daca x este par si nu a fost vizitat, il stergem, deoarece acesta face parte din grupul de stergeri gasite
    # folosind cuplajul (parele ce au fost cuplate cu impare in cuplaj maxim vor fi sterse)
    if x % 2 == 0:
        if x not in visited:
            numbers_to_remove.append(x)
    else:
        # Daca x este impar si a fost vizitat, il stergem, deoarece acesta da nr prim la suma cu un numar par nesters
        # dupa cuplaj
        if x in visited:
            numbers_to_remove.append(x)

print(len(numbers_to_remove))
print(*numbers_to_remove)
