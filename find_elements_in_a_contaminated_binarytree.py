"""
1261. Find Elements in a Contaminated Binary Tree
Medium
Topics
Companies
Hint
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106

Hint 1
Use DFS to traverse the binary tree and recover it.
Hint 2
Use a hashset to store TreeNode.val for finding.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binary_tree_paths import TreeNode


class FindElements:
    def recover(self, node):
        if not node: 
            return node

        node.val = 0
        
        def dfs(node, val = 0):
            if not node:
                return 
            if node.left:
                node.left.val = val * 2 + 1
                self.set.add(node.left.val)
                dfs(node.left, node.left.val)
            if node.right:
                node.right.val = val * 2 + 2
                self.set.add(node.right.val)
                dfs(node.right, node.right.val)

        dfs(node)

    def __init__(self, root: Optional[TreeNode]):
        self.set = {0}
        self.recover(root)
        self.root = root

    def find(self, target: int) -> bool:
        return target in self.set
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

root = TreeNode(-1)
root.right = TreeNode(-1)
#root.right.left = TreeNode(1)
#root.right.right = TreeNode(2)

# Initialize FindElements
obj = FindElements(root)

# Check if 1 and 2 exist in the tree
print(obj.find(1))  # Output: True
print(obj.find(2))  # Output: True

