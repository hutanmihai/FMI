class Node:
    def __init__(self, info, parent=None):
        self.info = info
        self.parent = parent

    def __str__(self):
        return "a={} b={}".format(self.info, self.parent)

    def __repr__(self):
        return "({}, {})".format(self.info, self.parent)

    def path_root(self):
        """
        :return: List of nodes as Node objects from root to current node.
        """
        node = self
        path = []
        while node is not None:
            path.insert(0, node)
            node = node.parent
        return path

    def visited(self):
        """
        :return: True if the node has been visited on the current path, False otherwise.
        """
        node = self
        while node.parent is not None:
            if node.info == node.parent.info:
                return True
            node = node.parent
        return False

    def __repr__(self):
        return "{} ({})".format(
            self.info, "->".join([str(x) for x in self.path_root()])
        )

    def __str__(self):
        return str(self.info)


class Graph:
    def __init__(self, matrix, start, scopes):
        self.matrix = matrix
        self.start = start
        self.scopes = scopes

    def scope(self, info_node):
        return info_node in self.scopes

    def successors(self, node):
        list_successors = []
        for i in range(len(self.matrix[node.info])):
            if self.matrix[node.info][i] == 1:
                new_node = Node(i, node)
                if not new_node.visited():
                    list_successors.append(new_node)
        return list_successors


def bfs(graph, number_of_solutions):
    queue = [Node(graph.start)]

    while queue:
        current_node = queue.pop(0)
        if graph.scope(current_node.info):
            print(repr(current_node))
            number_of_solutions -= 1
            if not number_of_solutions:
                return
        list_successors = graph.successors(current_node)
        queue += list_successors


# DFS RECURSIV
def dfs(graph, node, visited, n, solutions):
    visited.add(node.info)

    if graph.scope(node.info):
        solutions.append(node)
        if len(solutions) == n:
            return

    list_successors = graph.successors(node)
    for successor in list_successors:
        if successor.info not in visited and len(solutions) < n:
            dfs(graph, successor, visited, n, solutions)


if __name__ == "__main__":
    m = [
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    start = 0
    scopes = [5, 9]
    n_sol = 2

    graph = Graph(m, start, scopes)

    print("BFS:")
    bfs(graph, n_sol)
    print("--------------------")
    print("DFS:")
    visited = set()
    solutions = []
    dfs(graph, Node(start), visited, n_sol, solutions)
    for solution in solutions:
        print(repr(solution))


# DFS ITERATIV
def dfs(graph, number_of_solutions):
    visited = set()
    stack = [Node(graph.start)]

    while stack:
        node = stack.pop()
        visited.add(node.info)

        if graph.scope(node.info):
            print(repr(node))
            number_of_solutions -= 1
            if not number_of_solutions:
                return

        list_successors = graph.successors(node)
        for successor in list_successors:
            if successor.info not in visited:
                stack.append(successor)
