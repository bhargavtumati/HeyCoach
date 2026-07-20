"""**Statement:**

**Depth First Search (DFS):** Write a program to traverse all vertices of a graph represented using an adjacency list.
 Visit each vertex exactly once by exploring as deep as possible before backtracking. If the graph has multiple 
 connected components, traverse each component.
"""

class Solution:
    def dfsvisit(self, adj, u, visited):
        visited[u] = True
        print(u, end="->")

        for v in adj[u]:
            if not visited[v]:
                self.dfsvisit(adj, v, visited)

    def dfs(self, adj):
        visited = [False] * len(adj)

        for i in range(len(adj)):
            if not visited[i]:
                self.dfsvisit(adj, i, visited)


if __name__ == "__main__":
    adj = [[1, 2], [3, 4], [], [], [0]]

    s = Solution()
    s.dfs(adj)
