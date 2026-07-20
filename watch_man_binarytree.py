"""
Watchmen of Binary Tree
Given HeyCoach land’s Binary Tree Society, we have to place watchmen to keep an eye on the whole Society, each watchman can keep an eye on itself, parent node and immediate children. Calculate minimum number of Watchmen required to keep an eye on all houses of the HeyCoach Land.

For example: Given the Binary Tree

       1
     /   \
   2       3
  /    
 6
The minimum number of watchmen would be two which can be placed at node value '2' and '3'.

Input Format:

A single line that represents the value of the nodes and the value of '- 1' denotes NULL node.
Output Format:

Return a single integer representing the minimum number of watchmen required to keep an eye on the society.
Sample Input:

1 2 3 6 -1 -1 -1 -1 -1

Sample Output:

2
Constraints:

0 <= N <= 10^4

0 <= data <= 10^3

Where 'N' denotes the total number of nodes and 'data' denotes the value of the node"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
  
    def __init__(self):
        self.cnt = 0
    
    def solve(self, root):
        def dfs(node):
            if not node:
                return 0, 0, float('inf')
            
            L = dfs(node.left)
            R = dfs(node.right)
            
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1], R[2]), R[2] + min(L[1], L[2]))
            dp2 = 1 + min(L) + min(R)
            
            return dp0, dp1, dp2
        
        return min(dfs(root)[1:])

# Example usage:
# Constructing the binary tree
#       0
#      / \
#     0   0
#    / \
#   0   0

root = Node(0)
root.left = Node(0)
root.right = Node(0)
root.left.left = Node(0)
root.left.right = Node(0)

solution = Solution()
print(solution.solve(root))  # Output: 1
