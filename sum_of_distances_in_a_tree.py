
"""
834. Sum of Distances in Tree
Solved
Hard
Topics
Companies
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""


from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [0] * N
        res = [0] * N
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs1(cur: int, parent: int) -> None:
            count[cur] = 1
            for child in graph[cur]:
                if child != parent:
                    dfs1(child, cur)
                    count[cur] += count[child]
                    res[cur] += res[child] + count[child]
        
        def dfs2(cur: int, parent: int) -> None:
            for child in graph[cur]:
                if child != parent:
                    res[child] = res[cur] + N - 2 * count[child]
                    dfs2(child, cur)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res
if __name__ == "__main__":
    f = Solution()
    n=6
    edges=[[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(f.sumOfDistancesInTree(n,edges))    
