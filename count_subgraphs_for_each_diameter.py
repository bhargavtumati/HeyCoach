"""
1617. Count Subtrees With Max Distance Between Cities
Solved
Hard
Topics
Companies
Hint
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

 

Example 1:



Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.
Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]
Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]
"""

from collections import defaultdict
from typing import List
class Solution:
    def is_tree(self,bitmask):
            if bitmask.bit_count() < 2: return False
            created_edges = 0
            for edge in edges:
                if (1 << edge[0]) & bitmask and (1 << edge[1]) & bitmask:
                    created_edges += 1
            if created_edges == bitmask.bit_count() - 1:
                return True
            return False
        
    # create the tree:
    def create_tree(self,bitmask):
            tree = defaultdict(list)
            for edge in edges:
                if (1 << edge[0]) & bitmask and (1 << edge[1]) & bitmask:
                    tree[edge[0]].append(edge[1])
                    tree[edge[1]].append(edge[0])
            return tree

    # calculate the diameter;
    def dfs(self, tree, node) -> int:
            if not tree[node]: return 0
            max_height = 0
            second_height = 0
            self.visited.add(node)
            for child in tree[node]:
                if child in self.visited: continue
                height = 1 + self.dfs(tree, child)
                if max_height > height >= second_height:
                    second_height = height
                elif height >= max_height:
                    second_height = max_height
                    max_height = height
                diameter = max_height + second_height
                self.longest_diameter[0] = max(self.longest_diameter[0], diameter)
            return max_height
    
    def count_subgraphs_for_each_diameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # TC: O(m * (2**n)) SP: O(n + m)
        # diameters = defaultdict(int)
        # I hate node start with 1, so I decrease all of them
        for i in range(len(edges)):
            edges[i][0] -= 1
            edges[i][1] -= 1


        res = [0] * (n-1)
        for bitmask in range(1, 1<<n):
            if not self.is_tree(bitmask):
                continue
            # reset visited
            self.visited = set()
            # reset longest_diameter
            longest_diameter = [0]
            tree = self.create_tree(bitmask)
            # choose random node to start dfs
            root = next(iter(tree.keys()))
            self.dfs(tree, root)
            # res start from 0 diameter, so -1 to be fit into res
            res[longest_diameter[0]-1] += 1
        return res

if __name__ =="__main__":
     cp=Solution()    
     n=4
     edges=[[1,2],[2,3],[2,4]]
     print(cp.count_subgraphs_for_each_diameter(n,edges))

