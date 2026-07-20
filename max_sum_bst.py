"""
1373. Maximum Sum BST in Binary Tree
Solved
Hard
Topics
Companies
Hint
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104"""


import math
from typing import Optional

from binary_tree_paths import TreeNode


class T:
  def __init__(self, isBST: bool = False,
               max: Optional[int] = None,
               min: Optional[int] = None,
               sum: Optional[int] = None):
    self.isBST = isBST
    self.max = max
    self.min = min
    self.sum = sum


class Solution:
  def maxSumBST(self, root: Optional[TreeNode]) -> int:
    self.ans = 0

    def traverse(root: Optional[TreeNode]) -> T:
      if not root:
        return T(True, -math.inf, math.inf, 0)

      left: T = traverse(root.left)
      right: T = traverse(root.right)

      if not left.isBST or not right.isBST:
        return T()
      if root.val <= left.max or root.val >= right.min:
        return T()

      # The `root` is a valid BST.
      summ = root.val + left.sum + right.sum
      self.ans = max(self.ans, summ)
      return T(True, max(root.val, right.max), min(root.val, left.min), summ)

    traverse(root)
    return self.ans
if __name__=="__main__":
    root = TreeNode(4)
    root.left=TreeNode(3)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(2)
    v=Solution()
    print(v.maxSumBST(root))
