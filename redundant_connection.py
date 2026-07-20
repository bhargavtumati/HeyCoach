"""
684. Redundant Connection
Attempted
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected."""


from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)] #creating array of i [0,1,2....]
        rank = [0] * n  #creating [0,0,0,....]

        def find(x):     #The find(x) function recursively finds the root (representative) of the set containing node x.
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):  #The union(x, y) function merges the sets containing nodes x and y. If the roots of x and y are different, we merge them. If the ranks of the roots are equal, we increment the rank of the new root.
            xroot, yroot = find(x), find(y)
            if xroot != yroot:
                if rank[xroot] > rank[yroot]:
                    parent[yroot] = xroot
                else:
                    parent[xroot] = parent[yroot]
                    if rank[xroot] == rank[yroot]:
                        rank[yroot] += 1

        for edge in edges:
            a, b = edge[0] - 1, edge[1] - 1
            if find(a) == find(b):
                return edge
            else:
                union(a, b)

        return None

if __name__=="__main__":
    s=Solution()
    edges=[[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(s.findRedundantConnection(edges))
