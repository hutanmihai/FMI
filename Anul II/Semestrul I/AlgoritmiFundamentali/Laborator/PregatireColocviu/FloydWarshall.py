"""
Problema drumurilor minime între toate perechile de vârfuri
"""


def floyd_warshall():
    n = len(graph) + 1
    dist = [[float("inf") for x in range(n)] for y in range(n)]
    pred = [[0 for x in range(n)] for y in range(n)]
    for i in graph:
        dist[i][i] = 0
        for j, w in graph[i]:
            dist[i][j] = w
            pred[i][j] = i
    print(pred)
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    return dist[1:], pred[1:]


if __name__ == '__main__':
    # graph = {1: [(2, 1), (3, 4)], 2: [(1, 1), (3, 2), (4, 5)], 3: [(1, 4), (2, 2), (4, 1)], 4: [(2, 5), (3, 1)]}
    graph = {
        1: [(2, 5), (3, 10), (4, 1)],
        2: [(3, 3)],
        3: [(4, 2)],
        4: [(1, 3), (2, 20), (3, 16)],
    }
    print(floyd_warshall())
