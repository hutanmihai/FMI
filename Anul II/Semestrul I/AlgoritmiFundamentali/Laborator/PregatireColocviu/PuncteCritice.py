# O(n+m)

def dfs(nod):
    vizitat.add(nod)
    nivel_minim[nod] = nivel[nod]
    for vecin in graph[nod]:
        if vecin not in vizitat:
            nivel[vecin] = nivel[nod] + 1
            dfs(vecin)
            nivel_minim[nod] = min(nivel_minim[nod], nivel_minim[vecin])
            if nivel_minim[vecin] >= nivel[nod] and nod not in puncte_critice and nod != start:
                puncte_critice.add(nod)
        elif nivel[vecin] < nivel[nod] + 1:
            nivel_minim[nod] = min(nivel_minim[nod], nivel[vecin])


if __name__ == '__main__':
    graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
    puncte_critice = set()
    vizitat = set()
    nivel = [float('inf')] * (len(graph) + 1)
    nivel_minim = [float('inf')] * (len(graph) + 1)
    start = 1
    dfs(start)
    if len(puncte_critice) > 0:
        print("Punctele critice:", *puncte_critice)
    else:
        print("Nu avem puncte critice")
