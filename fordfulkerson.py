"""### Problem Statement

Given a **flow network** with `n` nodes and `m` directed edges, where each edge has a certain capacity,
 find the **maximum possible flow** that can be sent from the **source node (1)** to the **sink node (n)**.

Use the **Ford-Fulkerson algorithm with BFS (Edmonds-Karp approach)** to calculate the maximum flow.

### Example

**Input:**

```text
n = 4

edges = [
(1,2,3),
(1,3,2),
(1,4,4),
(2,3,1),
(2,4,7),
(3,4,5)
]
```

**Output:**

```text
9
```

### Explanation

The maximum flow from node `1` to node `4` is achieved by sending flow through multiple paths:

* `1 → 4`
* `1 → 2 → 4`
* `1 → 3 → 4`

The total maximum flow is `9`.

### Approach

* Represent the network using a capacity matrix.
* Use BFS to find an augmenting path from source to sink.
* Find the minimum capacity (bottleneck) along that path.
* Update residual capacities.
* Repeat until no augmenting path exists.

### Complexity

For Edmonds-Karp algorithm:

* **Time Complexity:** `O(V × E²)`
* **Space Complexity:** `O(V²)`

Where:

* `V` = number of vertices
* `E` = number of edges
"""


from collections import deque


class Solution:

    def find_max_flow(self, n, m, edges):
        capacity = self.build_capacity_graph(n, edges)

        source = 1
        sink = n
        max_flow = 0

        while True:
            parent = [-1] * (n + 1)

            if not self.bfs(capacity, source, sink, parent, n):
                break

            flow = self.calculate_path_flow(capacity, source, sink, parent)
            self.update_residual_capacity(capacity, source, sink, parent, flow)

            max_flow += flow

        return max_flow


    def build_capacity_graph(self, n, edges):
        capacity = [[0] * (n + 1) for _ in range(n + 1)]

        for start, end, flow in edges:
            capacity[start][end] = flow

        return capacity


    def bfs(self, capacity, source, sink, parent, n):
        visited = [False] * (n + 1)

        queue = deque([source])
        visited[source] = True

        while queue:
            current = queue.popleft()

            for neighbor in range(1, n + 1):
                if not visited[neighbor] and capacity[current][neighbor] > 0:
                    parent[neighbor] = current
                    visited[neighbor] = True

                    if neighbor == sink:
                        return True

                    queue.append(neighbor)

        return False


    def calculate_path_flow(self, capacity, source, sink, parent):
        path_flow = float("inf")
        current = sink

        while current != source:
            previous = parent[current]
            path_flow = min(
                path_flow,
                capacity[previous][current]
            )
            current = previous

        return path_flow


    def update_residual_capacity(self, capacity, source, sink, parent, flow):
        current = sink

        while current != source:
            previous = parent[current]

            capacity[previous][current] -= flow
            capacity[current][previous] += flow

            current = previous


if __name__ == "__main__":

    edges = [
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 4),
        (2, 3, 1),
        (2, 4, 7),
        (3, 4, 5)
    ]

    solution = Solution()

    print(solution.find_max_flow(4, 6, edges))