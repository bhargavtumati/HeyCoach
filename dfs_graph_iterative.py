"""
## DFS (Depth First Search)

### Statement

Given a graph represented as an **adjacency list**, perform **Depth First Search (DFS)** traversal and visit every vertex exactly once. If the graph has multiple connected components, traverse each component.

### Why DFS is Used

* To traverse all vertices of a graph.
* To find connected components.
* To detect cycles in a graph.
* To check if a path exists between two vertices.
* Used in topological sorting and backtracking problems (e.g., maze solving, Sudoku).

### Algorithm

1. Mark the starting vertex as visited.
2. Push it onto a stack (or call recursively).
3. Visit the top vertex.
4. Visit all its unvisited adjacent vertices.
5. Repeat until the stack is empty.
6. If any vertex remains unvisited, start DFS from that vertex.

### Complexity

* **Time Complexity:** **O(V + E)**
* **Space Complexity:** **O(V)**

Where:

* **V** = Number of vertices
* **E** = Number of edges
"""


class Solution:
    def dfsvisit(self, adj, u, visited):
        stack = []
        stack.append(u)
        visited[u] = True

        while stack:
            u = stack.pop()      # Better than del(stack[-1])
            print(u, end=" -> ")

            for v in adj[u]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True

    def dfs(self, adj):
        visited = [False] * len(adj)

        for i in range(len(adj)):
            if not visited[i]:
                self.dfsvisit(adj, i, visited)


if __name__ == "__main__":
    adj = [[1, 2], [3, 4], [], [], [0]]

    s = Solution()
    s.dfs(adj)
