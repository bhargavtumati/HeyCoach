"""### Problem Statement: Minimum Spanning Tree (Kruskal's Algorithm)

You are given an **undirected weighted graph** with `N` vertices and `M` edges.

Your task is to find the **Minimum Spanning Tree (MST)** of the graph.

A **Minimum Spanning Tree** is a subset of edges that:

1. Connects all the vertices of the graph.
2. Contains exactly `N - 1` edges.
3. Does not contain any cycle.
4. Has the minimum possible total edge weight.

Return the edges that form the Minimum Spanning Tree.

---

### Input:

* `N` → Number of vertices.
* `M` → Number of edges.
* `edges` → List of edges where each edge is represented as:

```
[u, v, w]
```

where:

* `u` = starting vertex
* `v` = ending vertex
* `w` = weight of the edge

---

### Example:

**Input:**

```python
n = 4
m = 5

edges = [
    [1, 2, 1],
    [1, 3, 2],
    [1, 4, 3],
    [2, 3, 5],
    [3, 4, 4]
]
```

Graph:

```
        1
      / | \
    1/ 2|  3
    /   |   \
   2----5----3
        \
         4
```

---

### Output:

```python
[
 [1,2,1],
 [1,3,2],
 [1,4,3]
]
```

---

### Explanation:

Sort edges by weight:

```
[1,2,1]
[1,3,2]
[1,4,3]
[3,4,4]
[2,3,5]
```

Pick edges one by one:

1. Take `(1,2)` weight 1
   → connects vertices 1 and 2

2. Take `(1,3)` weight 2
   → connects vertex 3

3. Take `(1,4)` weight 3
   → connects vertex 4

Now all vertices are connected with `N-1 = 3` edges.

Total MST weight:

```
1 + 2 + 3 = 6
```

---

### Algorithm Used:

**Kruskal's Algorithm**

Steps:

1. Sort all edges in increasing order of weight.
2. Use **Disjoint Set Union (DSU)** to detect cycles.
3. Add an edge if it does not create a cycle.
4. Stop when `N-1` edges are selected.

---

### Constraints:

```
1 ≤ N ≤ 10^5
1 ≤ M ≤ 10^5
1 ≤ weight ≤ 10^9
```

### Complexity:

* Sorting edges:

```
O(M log M)
```

* DSU operations:

```
O(M α(N))
```

Overall:

```
Time Complexity: O(M log M)
Space Complexity: O(N)
```
"""

class Solution:
    def minimum_spanning_tree(self, n, m, edges):
        # Sort edges based on their weight
        edges.sort(key=lambda x: x[2])
        
        # Helper function to find the root of a node
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])
        
        # Helper function to perform union of two sets
        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        # Initialize parent and rank arrays
        parent = [i for i in range(n)]
        rank = [0] * n
        
        mst = []
        for u, v, w in edges:
            root_u = find(parent, u - 1)
            root_v = find(parent, v - 1)
            
            # If including this edge does not cause a cycle
            if root_u != root_v:
                mst.append([u, v, w])
                union(parent, rank, root_u, root_v)
        
        return mst

# Example usage:
solution = Solution()
n = 4
m = 5
edges = [
    [1, 2, 1],
    [1, 3, 2],
    [1, 4, 3],
    [2, 3, 5],
    [3, 4, 4]
]
print(solution.minimum_spanning_tree(n, m, edges))
