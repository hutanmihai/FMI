# O(mlogn)

import heapq

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)],
}


def prim():
    apcm = []
    vizitat = set()
    start = 0
    heap = [(0, -1, start)]
    while heap:
        cost, parinte, nod = heapq.heappop(heap)
        if nod not in vizitat:
            vizitat.add(nod)
            apcm.append((parinte, nod))
            for vecin, cost in graph[nod]:
                if vecin not in vizitat:
                    heapq.heappush(heap, (cost, nod, vecin))

    return apcm[1:]


if __name__ == '__main__':
    print(prim())
