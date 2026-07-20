"""
Count the Number of Complete Components
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array of edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

Examples:

Input:

 n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]


Output:

3

Input:

n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output:

1
Constraints:

1<= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges.
"""




class Solution:
    def count_complete_components(self, n, edges):
        # Initialize adjacency list for the graph with n empty lists
        g = [[] for _ in range(n)]

        # Initialize two visited lists v1 and v2 with False values
        v1 = [False] * n
        v2 = [False] * n

        # Fill the adjacency list with the given edges
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        # Initialize y and x as lists with single elements to use as mutable counters
        y = [0]
        x = [0]
        ans = 0

        # Iterate through each node in the graph
        for i in range(n):
            if not v1[i]:
                # If the node i has not been visited in v1, it starts a new component
                y[0] = -1
                self.get(i, g, y, v1)
                x[0] = 1
                self.solve(i, g, x, y[0], v2)
                ans += x[0]

        return ans

    def get(self, s, g, y, v):  #start,graph,depth,visited
        # This function performs a DFS to count the number of vertices in the current component
        if v[s]:
            return
        v[s] = True
        y[0] += 1
        for i in g[s]:
            self.get(i, g, y, v)

    def solve(self, s, g, x, y, v):  #start ,graph,compete,depth,visited
        # This function performs a DFS to check if the component is complete
        if v[s]:
            return
        v[s] = True
        for i in g[s]:
            if len(g[i]) != y:
                x[0] = 0
            self.solve(i, g, x, y, v)


if __name__=="__main__":
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]
    s=Solution()
    print(s.count_complete_components(n,edges))

