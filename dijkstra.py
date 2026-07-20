
"""
Dijkstras Algorithm
Given a weighted directed graph with N nodes and E edges, you need to find the shortest path from a given source node to all other nodes in the graph using Dijkstra's algorithm. The nodes are indexed from 0 to N−1, and the graph's edges have non-negative weights.

Sample Input-1:
The number of nodes (N). : 5
The number of edges (E). : 7
E triples of integers representing edges and their weights.
Source node (S). : 0

`

(0 1 2)
(0 2 4)
(1 2 1)
(1 3 7)
(2 3 3)
(2 4 5)
(3 4 2)

`

Sample Output-1:
Shortest distance from the source node to all other nodes.
(0 0)
(1 2)
(2 3)
(3 6)
(4 8) `

Sample input-2:
4 5
0 1 1
1 2 2
2 3 3
0 2 4
1 3 5
0
Sample Output-2
0 0
1 1
2 3
3 6
Constraints:
1 <= N <= 10^4 (number of nodes)

0 <= E <= 10^5 (number of edges)

0 <= u, v < N (node indices)

-10^9 <= weight <= 10^9 (edge weights)

The graph is guaranteed to be connected."""

import heapq

class Solution:
    @staticmethod
    def dijkstra(n, graph, start):
        # Priority queue to store (distance, vertex) pairs
        pq = [(0, start)]
        distances = {i: float('infinity') for i in range(n)}
        distances[start] = 0

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Nodes can only be visited once
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        # Return the distances in the specified format
        result = []
        for vertex in range(n):
            result.append(f"{vertex} {distances[vertex]}")
        return "\n".join(result)

# Example usage
n = 4
graph = [
    [(1, 1), (2, 4)],  # Neighbors for vertex 0
    [(0, 1), (2, 2), (3, 5)],  # Neighbors for vertex 1
    [(0, 4), (1, 2), (3, 1)],  # Neighbors for vertex 2
    [(1, 5), (2, 1)]  # Neighbors for vertex 3
]

start_vertex = 0
solution = Solution()
print(solution.dijkstra(n, graph, start_vertex))

