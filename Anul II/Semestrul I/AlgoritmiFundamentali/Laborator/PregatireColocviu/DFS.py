# O(n+m)

"""
Determinare de cicluri in graf neorientat:
Initializari:
ciclu = []

        elif vecin != tata[nod]:
            v = nod
            while v != vecin:
                ciclu.append(v)
                v = tata[v]
            ciclu.append(vecin)
            ciclu.append(nod)
            return ciclu


Determinare de circuit in grad orientat:
Initializari:
fin = set()
circuit = []

        elif vecin not in fin:
            v = nod
            while v != vecin:
                ciclu.append(v)
                v = tata[v]
            ciclu.append(vecin)
            ciclu.append(nod)
            return reversed(ciclu)
    fin.add(nod)
"""


def dfs(nod):
    vizitat.add(nod)
    for vecin in graph[nod]:
        if vecin not in vizitat:
            tata[vecin] = nod
            nivel[vecin] = nivel[nod] + 1
            dfs(vecin)


if __name__ == '__main__':
    graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
    vizitat = set()
    tata = [0] * (len(graph) + 1)
    nivel = [float('inf')] * (len(graph) + 1)

    nr_componente_conexe = 0

    for nod in graph:
        if nod not in vizitat:
            nivel[nod] = 1
            dfs(nod)
            nr_componente_conexe += 1
