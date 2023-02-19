# O(nm)

"""
Algoritmi pentru grafuri orientate cu circuite și ponderi reale,
care detectează existența de circuite negative – Bellman-Ford.
"""


def bellman_ford(start):
    dist[start] = 0
    for i in range(len(graph) - 1):
        for nod in graph:
            for vecin, cost in graph[nod]:
                if dist[nod] + cost < dist[vecin]:
                    dist[vecin] = dist[nod] + cost
                    tata[vecin] = nod
    for nod in graph:
        for vecin, cost in graph[nod]:
            if dist[nod] + cost < dist[vecin]:
                print("Circuite negative!")
                return


if __name__ == '__main__':
    graph = {1: [(2, 1), (3, 4)], 2: [(1, 1), (3, 2), (4, 5)], 3: [(1, 4), (2, 2), (4, 1)], 4: [(2, 5), (3, 1)]}
    dist = [float("inf")] * (len(graph) + 1)
    tata = [0] * (len(graph) + 1)
    bellman_ford(1)
    print(tata)
    print(dist)
