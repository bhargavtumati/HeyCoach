
"""2196. Create Binary Tree From Descriptions
Solved
Medium
Topics
Companies
Hint
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.

Hint 1
Could you represent and store the descriptions more efficiently?
Hint 2
Could you find the root node?
Hint 3
The node that is not a child in any of the descriptions is the root node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
from typing import List, Optional

from binary_tree_paths import TreeNode


class Solution:
    def create_binary_tree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        has_parent = set()

        for parent, child, is_left in descriptions:
            if child not in nodes: nodes[child] = TreeNode(child)
            if parent not in nodes: nodes[parent] = TreeNode(parent)

            if is_left: nodes[parent].left = nodes[child]
            else: nodes[parent].right = nodes[child]
            
            has_parent.add(child)
            
        for child in nodes.keys():
            if child not in has_parent:
                return nodes[child]
# Example usage:
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Example descriptions: [parent, child, isLeft]
    descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

    # Create the binary tree
    root = solution.create_binary_tree(descriptions)

    # Print the tree (for visualization)
    def level_order_traversal(root):
        # Formalities/Edge Cases
        if root is None:
            return []

        result = []

        # Main logic
        q = deque()
        q.append(root)

        while q:
            level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                # This is the place where you edit your elements
                level_nodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            # This is the place where level shift happens
            result.append(level_nodes)

        return result

    print(level_order_traversal(root)) # Output: 1 -> 2 -> 4 -> 5 -> 3 ->

    # You can perform other operations on the tree as needed



