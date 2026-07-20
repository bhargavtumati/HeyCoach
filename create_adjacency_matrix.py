"""This code is **not from a specific LeetCode problem**. It demonstrates how to **create or copy an adjacency matrix** representation of an undirected graph.

> **Note:** In your example, the input `graph` is already an adjacency matrix, so `create_adjacency_matrix()` simply recreates the same matrix. Typically, an adjacency matrix is constructed from an edge list or adjacency list.

## Problem Statement

### Create an Adjacency Matrix of an Undirected Graph

Given an undirected graph with `V` vertices, construct its adjacency matrix.

An adjacency matrix is a `V × V` matrix where:

* `matrix[i][j] = 1` if there is an edge between vertices `i` and `j`.
* `matrix[i][j] = 0` otherwise.

For an undirected graph, the matrix is symmetric:

```text
matrix[i][j] = matrix[j][i]
```

---

### Example

**Input**

```text
V = 4

Edges:
(0,1)
(1,2)
(2,3)
```

**Output**

```text
0 1 0 0
1 0 1 0
0 1 0 1
0 0 1 0
```

---

### Explanation

The graph is:

```text
0 -- 1 -- 2 -- 3
```

The corresponding adjacency matrix is:

|       | 0 | 1 | 2 | 3 |
| ----- | - | - | - | - |
| **0** | 0 | 1 | 0 | 0 |
| **1** | 1 | 0 | 1 | 0 |
| **2** | 0 | 1 | 0 | 1 |
| **3** | 0 | 0 | 1 | 0 |

---

### Constraints

```text
1 <= V <= 1000
0 <= number of edges <= V * (V - 1) / 2
```

---

### Function Signature

```python
def create_adjacency_matrix(graph):
```

Return the adjacency matrix of the graph.

### Note about your code

Since your input:

```python
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
```

is **already an adjacency matrix**, the function doesn't transform the graph into a new representation—it effectively copies the matrix. A more typical implementation would take an **edge list** as input and build the adjacency matrix from those edges.
"""


def create_adjacency_matrix(edges, num_vertices):
    # Initialize the adjacency matrix with zeros
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Add edges
    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1  # For undirected graph

    return adj_matrix


if __name__ == "__main__":
    # Number of vertices
    num_vertices = 4

    # Edge list
    edges = [
        (0, 1),
        (1, 2),
        (2, 3)
    ]

    # Create the adjacency matrix
    adj_matrix = create_adjacency_matrix(edges, num_vertices)

    # Print the adjacency matrix
    for row in adj_matrix:
        print(" ".join(map(str, row)))