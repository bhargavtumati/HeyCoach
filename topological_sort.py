"""### Problem Statement: Topological Sort of a Directed Graph

Given a **Directed Acyclic Graph (DAG)** with `N` vertices and a list of directed edges, find a **topological ordering** of the vertices.

A topological ordering is a linear arrangement of vertices such that for every directed edge:

```
u → v
```

vertex `u` appears before vertex `v` in the ordering.

If the graph contains a cycle, a topological ordering is not possible, so return an empty list.

---

### Example

**Input:**

```text
N = 6

edges = [
(5,2),
(5,0),
(4,0),
(4,1),
(2,3),
(3,1)
]
```

Graph:

```
5 → 2 → 3 → 1
↓
0

4 → 0
↓
1
```

---

### Output:

```text
[4,5,2,0,3,1]
```

(or any other valid topological ordering)

---

### Explanation:

For every edge:

```
5 → 2
```

5 appears before 2.

```
2 → 3
```

2 appears before 3.

```
3 → 1
```

3 appears before 1.

All dependencies are satisfied.

---

### Constraints

```text
1 <= N <= 10^5

0 <= edges.length <= 10^5

0 <= u,v < N

The graph may contain cycles.
```

---

### Function Signature

Python:

```python
def topologicalSort(self, N, edges):
```

Return:

* A list containing vertices in topological order.
* An empty list `[]` if the graph contains a cycle.

---

## Approach Used in Your Code

Your solution uses **Kahn's Algorithm (BFS-based Topological Sort)**.

### Steps:

### 1. Build Graph and Calculate In-Degree

For every edge:

```python
u → v
```

Add:

```python
graph[u].append(v)
```

Increase:

```python
in_degree[v] += 1
```

Example:

```
5 → 2
```

means:

```
in_degree[2] = 1
```

---

### 2. Add Nodes With Zero In-Degree

Nodes with no dependencies can be processed first:

```python
queue = deque([i for i in range(N) if in_degree[i] == 0])
```

---

### 3. Process BFS

Remove a node:

```python
node = queue.popleft()
```

Add it to result:

```python
topo_sort.append(node)
```

Remove its dependency from neighbors:

```python
in_degree[neighbor] -= 1
```

When a neighbor becomes zero:

```python
queue.append(neighbor)
```

---

### 4. Detect Cycle

If all nodes are processed:

```python
len(topo_sort) == N
```

Topological ordering exists.

Otherwise:

```python
return []
```

because some nodes are stuck in a cycle.

---

### Complexity Analysis

Let:

* `N` = number of vertices
* `E` = number of edges

### Time Complexity:

```
O(N + E)
```

Each node and edge is processed once.

### Space Complexity:

```
O(N + E)
```

For:

* adjacency list
* in-degree array
* queue
* result list
"""


from collections import deque, defaultdict

class Solution:
    def topologicalSort(self, N, edges):
        # Initialize the graph and in-degree of each node
        graph = defaultdict(list)
        in_degree = [0] * N
        
        # Build the graph and compute in-degrees of nodes
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Initialize the queue with nodes having in-degree 0
        queue = deque([i for i in range(N) if in_degree[i] == 0])
        topo_sort = []
        
        # Process the nodes
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            
            # Decrease the in-degree of neighboring nodes
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if topological sort is possible (i.e., no cycle)
        if len(topo_sort) == N:
            return topo_sort
        else:
            return []  # Return an empty list if there is a cycle (shouldn't happen in a DAG)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    N = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print("Topological Sort:", solution.topologicalSort(N, edges))
