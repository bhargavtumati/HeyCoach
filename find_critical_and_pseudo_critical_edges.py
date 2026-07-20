"""

Code
Code Sample
Code Sample


Testcase
Testcase
Test Result
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
Solved
Hard
Topics
Companies
Hint
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:



Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
54.1K
Submissions
79.9K
Acceptance Rate
67.6%
Topics
Companies
Hint 1
Use the Kruskal algorithm to find the minimum spanning tree by sorting the edges and picking edges from ones with smaller weights.
Hint 2
Use a disjoint set to avoid adding redundant edges that result in a cycle.
Hint 3
To find if one edge is critical, delete that edge and re-run the MST algorithm and see if the weight of the new MST increases.
Hint 4
To find if one edge is non-critical (in any MST), include that edge to the accepted edge list and continue the MST algorithm, then see if the resulting MST has the same weight of the initial MST of the entire graph."""


from collections import defaultdict
from typing import List


class UnionFindSet:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0

        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1

        self.count -= 1
        return True


class Solution:

    def group_edges_by_weight(self, edges):
        grouped = defaultdict(list)

        for index, (u, v, w) in enumerate(edges):
            grouped[w].append((u, v, index))

        return grouped


    def build_weight_graph(self, edges, union_find, pseudo):
        connections = defaultdict(set)

        for u, v, index in edges:
            root_u = union_find.find(u)
            root_v = union_find.find(v)

            if root_u != root_v:
                connections[tuple(sorted((root_u, root_v)))].add(index)

        graph = defaultdict(list)
        weight_edges = []

        for (u, v), edge_ids in connections.items():

            if len(edge_ids) > 1:
                pseudo.update(edge_ids)

            edge_id = next(iter(edge_ids))

            graph[u].append((v, edge_id))
            graph[v].append((u, edge_id))

            weight_edges.append((u, v, edge_id))

            union_find.union(u, v)

        return graph, weight_edges


    def find_bridges(self, graph, edges, critical, pseudo, n):

        levels = [-1] * n

        def dfs(node, level, parent):

            levels[node] = level

            for child, edge_id in graph[node]:

                if child == parent:
                    continue

                if levels[child] == -1:
                    levels[node] = min(
                        levels[node],
                        dfs(child, level + 1, node)
                    )
                else:
                    levels[node] = min(
                        levels[node],
                        levels[child]
                    )

                if levels[child] > level and edge_id not in pseudo:
                    critical.add(edge_id)

            return levels[node]


        for u, v, edge_id in edges:
            if levels[u] == -1:
                dfs(u, 0, -1)


    def mark_pseudo_edges(self, edges, critical, pseudo):

        for _, _, edge_id in edges:
            if edge_id not in critical:
                pseudo.add(edge_id)


    def process_weight_group(
            self,
            edges,
            union_find,
            critical,
            pseudo,
            n
    ):

        graph, weight_edges = self.build_weight_graph(
            edges,
            union_find,
            pseudo
        )

        self.find_bridges(
            graph,
            weight_edges,
            critical,
            pseudo,
            n
        )

        self.mark_pseudo_edges(
            weight_edges,
            critical,
            pseudo
        )


    def find_critical_and_pseudo_critical_edges(
            self,
            n: int,
            edges: List[List[int]]
    ):

        critical = set()
        pseudo = set()

        grouped_edges = self.group_edges_by_weight(edges)

        union_find = UnionFindSet(n)

        for weight in sorted(grouped_edges):
            self.process_weight_group(
                grouped_edges[weight],
                union_find,
                critical,
                pseudo,
                n
            )

        return [critical, pseudo]


if __name__ == "__main__":

    connections = [
        [0, 1, 1],
        [1, 2, 1],
        [2, 3, 2],
        [0, 3, 2],
        [0, 4, 3],
        [3, 4, 3],
        [1, 4, 6]
    ]

    n = 5

    solution = Solution()

    print(
        solution.find_critical_and_pseudo_critical_edges(
            n,
            connections
        )
    )
    
