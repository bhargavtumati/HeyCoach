"""
## Problem Statement

### Create an Adjacency List of an Undirected Graph

Given an undirected graph with `V` vertices numbered from `0` to `V - 1` and a list of edges, construct and return the graph's adjacency list.

The adjacency list should contain all the neighboring vertices for each vertex.

---

### Input

* An integer `V` representing the number of vertices.
* A list `edges`, where each element `[u, v]` represents an undirected edge between vertices `u` and `v`.

---

### Output

Return the adjacency list of the graph.

---

### Example

**Input**

```text
V = 4

edges = [
    (0,1),
    (0,2),
    (1,2),
    (2,3),
    (3,1)
]
```

**Output**

```text
0 -> 1 2
1 -> 0 2 3
2 -> 0 1 3
3 -> 2 1
```

---

### Explanation

The graph is:

```text
      0
     / \
    1---2
     \ /
      3
```

Since the graph is **undirected**, every edge is stored in both directions:

* `(0,1)` ⇒ `0 → 1` and `1 → 0`
* `(0,2)` ⇒ `0 → 2` and `2 → 0`
* `(1,2)` ⇒ `1 → 2` and `2 → 1`
* `(2,3)` ⇒ `2 → 3` and `3 → 2`
* `(3,1)` ⇒ `3 → 1` and `1 → 3`

---

### Constraints

```text
1 <= V <= 10^5
0 <= edges.length <= 2 × 10^5
0 <= u, v < V
```

---

### Function Signature

```python
def create_adjacency_list(edges, num_vertices):
```

Return the adjacency list representing the given undirected graph.
"""




def create_adjacency_list(edges, num_vertices):
    # Initialize the adjacency list
    adj_list = [[] for _ in range(num_vertices)]

    # Fill the adjacency list based on the edges in the graph
    for u, v in edges:
        # Since the graph is undirected, push the edges in both directions
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

if __name__ == "__main__":
    # Undirected Graph of 4 nodes
    num_vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]

    # Create the adjacency list
    adj_list = create_adjacency_list(edges, num_vertices)

    # Print the adjacency list
    for i in range(num_vertices):
        print(f"{i} -> {' '.join(map(str, adj_list[i]))}")