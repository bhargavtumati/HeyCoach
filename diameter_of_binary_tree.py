
"""
Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input :

[ 1 2 3 4 5 -1 -1 -1 -1 -1 -1]

Output:
3

        1
       / \
      2   3
     / \
    4   5
Input:

[10 5 20 3 7 -1 25 -1 -1 -1 -1 -1 -1]

Output:
4

         10
        /  \
       5    20
      / \     \
     3   7     25
Constraints:

The number of nodes in the tree is in the range [1, 3 * 10^4].
1 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class diameter_of_binary_tree:
    def solution(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1

        def diameter(node):
            if not node:
                return 0
            left_diameter = diameter(node.left)
            right_diameter = diameter(node.right)
            return max(left_diameter, right_diameter, height(node.left) + height(node.right))

        return diameter(root)

# Example usage

dia = diameter_of_binary_tree()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(dia.Solution(root1))  # Output: 3

# Example 2
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(20)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.right = TreeNode(25)
print(dia.Solution(root2))  # Output: 4
