"""### Problem Statement: Shortest Path Visiting All Nodes

Given an **undirected connected graph** with `n` nodes labeled from `0` to `n-1`, find the **shortest path length** that visits **every node at least once**.

You can:

* Start from any node.
* Move between connected nodes using the given edges.
* Visit nodes multiple times if needed.

Return the minimum number of edges required to visit all nodes.

---

### Example 1

**Input:**

```text
graph = [[1,2,3],
         [0],
         [0],
         [0]]
```

**Graph:**

```
      1
      |
2 --- 0 --- 3
```

**Output:**

```text
4
```

**Explanation:**

One shortest path is:

```
1 → 0 → 2 → 0 → 3
```

Number of edges:

```
4
```

All nodes `{0,1,2,3}` are visited.

---

### Example 2

**Input:**

```text
graph = [[1],
         [0,2,4],
         [1,3,4],
         [2],
         [1,2]]
```

**Output:**

```text
4
```

**Explanation:**

A shortest path:

```
0 → 1 → 2 → 3 → 2 → 4
```

requires 4 edges to visit all nodes.

---

### Constraints

```text
1 <= n <= 12

n == graph.length

0 <= graph[i].length < n

graph[i] contains no duplicate nodes.

The graph is connected.
```

---

### Function Signature

Python:

```python
def shortestPathLength(self, graph):
```

Return:

* The length of the shortest path that visits all nodes.

---

### Approach Used in Your Code

Your solution uses:

**BFS + Bitmask Dynamic Programming**

#### Bitmask representation:

Each node is represented by a bit:

Example:

For 4 nodes:

```
Node 0 → 0001
Node 1 → 0010
Node 2 → 0100
Node 3 → 1000
```

All nodes visited:

```
1111
```

stored as:

```python
final_mask = (1 << n) - 1
```

---

### BFS State

Each queue entry stores:

```python
(node, mask, length)
```

Example:

```
(node=2, mask=1011, length=5)
```

means:

* Currently at node 2
* Nodes 0,1,3 are already visited
* Path length is 5

---

### Why Start BFS From Every Node?

The shortest path can start anywhere, so initialize:

```python
for i in range(n):
    queue.append((i, 1<<i, 0))
```

This treats every node as a possible starting point.

---

### Complexity

Number of possible states:

```
n * 2^n
```

because:

* `n` possible current nodes
* `2^n` possible visited node combinations

### Time Complexity:

```
O(n * 2^n)
```

### Space Complexity:

```
O(n * 2^n)
```

for the visited table and queue.
"""

from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        final_mask = (1 << n) - 1
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]
        
        # Initialize the queue with each node and its corresponding bitmask
        for i in range(n):
            queue.append((i, 1 << i, 0))  # (current_node, bitmask, path_length)
            visited[i][1 << i] = True
        
        while queue:
            node, mask, length = queue.popleft()
            
            # If all nodes are visited
            if mask == final_mask:
                return length
            
            # Visit all the neighbors
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if not visited[neighbor][next_mask]:
                    queue.append((neighbor, next_mask, length + 1))
                    visited[neighbor][next_mask] = True
        
        return -1  # This line is never reached because the graph is connected

# Example usage:
solution = Solution()
print(solution.shortestPathLength([[1,2,3],[0],[0],[0]]))  # Output: 4
print(solution.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))  # Output: 4