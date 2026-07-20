"""### Problem Statement

Given a **flow network** with `n` nodes and `m` directed edges, where each edge has a certain capacity, find the **maximum possible flow** that can be sent from the **source node (1)** to the **sink node (n)**.

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


import math
from collections import deque

class Solution:
    def findMaxFlow(self, n, m, edges):
        # Create adjacency matrix for capacities
        capacity = [[0] * (n + 1) for _ in range(n + 1)]
        for u, v, cap in edges:
            capacity[u][v] = cap

        def bfs(source, sink, parent):
            visited = [False] * (n + 1)
            queue = deque([source])
            visited[source] = True

            while queue:
                u = queue.popleft()

                for v in range(n + 1):
                    if not visited[v] and capacity[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == sink:
                            return True
            return False

        source, sink = 1, n
        parent = [-1] * (n + 1)
        max_flow = 0

        while bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = parent[v]

        return max_flow

edges = [
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 4),
    (2, 3, 1),
    (2, 4, 7),
    (3, 4, 5)
]
solution = Solution()
print(solution.findMaxFlow(4, 6, edges)) 