"""print all paths from a source to all other vertices in a graph"""

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_all_paths(self, s):
        visited = [False] * self.v
        path = [s]
        self.dfs(s, visited, path)

    def dfs(self, u, visited, path):
        visited[u] = True

        is_leaf = True

        for v in self.adj_list[u]:
            if not visited[v]:
                is_leaf = False
                path.append(v)
                self.dfs(v, visited, path)
                path.pop()

        if is_leaf:
            print(path)

        visited[u] = False


g = Graph(5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)

g.print_all_paths(1)