"""### Problem Statement

Given a **directed graph** with `n` vertices and a list of directed edges, find the **number of Strongly Connected Components 
(SCCs)** in the graph.

A **Strongly Connected Component** is a group of vertices where every vertex is reachable from every other 
vertex in the same group.

Use **Kosaraju's Algorithm** to find the SCC count.

### Example

**Input:**

```text
n = 5

edges = [
(5,5),
(1,3),
(1,4),
(2,1),
(3,2),
(4,5)
]
```

**Output:**

```text
2
```

### Explanation:

Graph:

```
1 → 3 → 2 → 1

4 → 5 → 5
```

SCCs:

```
{1,2,3}
{4,5}
```

Total SCCs = `2`

### Approach (Kosaraju Algorithm)

1. Perform DFS on the original graph and store vertices by finishing time.
2. Reverse all graph edges.
3. Perform DFS on the reversed graph in decreasing finishing-time order.
4. Each DFS traversal gives one SCC.

### Complexity

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V + E)`

Where:

* `V` = number of vertices
* `E` = number of edges
"""


from collections import defaultdict


class Solution:

    def build_graph(self, n, edges):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)

        return graph, reverse_graph


    def fill_order(self, node, graph, visited, stack):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.fill_order(neighbor, graph, visited, stack)

        stack.append(node)


    def reverse_dfs(self, node, reverse_graph, visited):
        visited[node] = True

        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                self.reverse_dfs(neighbor, reverse_graph, visited)


    def count_scc(self, stack, reverse_graph, n):

        visited = [False] * (n + 1)
        count = 0

        while stack:
            node = stack.pop()

            if not visited[node]:
                self.reverse_dfs(node, reverse_graph, visited)
                count += 1

        return count


    def find_scc(self, n, edges):

        graph, reverse_graph = self.build_graph(n, edges)

        visited = [False] * (n + 1)
        stack = []

        # Step 1: Get finishing order
        for node in range(1, n + 1):
            if not visited[node]:
                self.fill_order(node, graph, visited, stack)

        # Step 2 & 3: Count SCCs on reversed graph
        return self.count_scc(stack, reverse_graph, n)


if __name__ == "__main__":

    solution = Solution()

    n = 5

    edges = [
        (5, 5),
        (1, 3),
        (1, 4),
        (2, 1),
        (3, 2),
        (4, 5)
    ]

    print(
        "Number of Strongly Connected Components:",
        solution.find_scc(n, edges)
    )
