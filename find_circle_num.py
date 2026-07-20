"""
547. Number of Provinces
Solved
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""


from typing import List

class Solution:
    def get_root(self, parent, x):
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.get_root(parent, x)
        root_y = self.get_root(parent, y)

        if root_x == root_y:
            return

        for i in range(len(parent)):
            if parent[i] == root_y:
                parent[i] = root_x

    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        parent = list(range(n))

        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j]:
                    self.union(parent, i, j)

        return len(set(parent))


if __name__ == "__main__":
    s = Solution()
    is_connected = [[1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]]
    print(s.find_circle_num(is_connected))
