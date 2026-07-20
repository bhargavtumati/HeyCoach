#print all paths from root to leaf in a binary tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from binary_tree_paths import TreeNode


from typing import List, Optional

class Solution:

    def combine_trees(self, left_trees, right_trees):
        result = []
        for left in left_trees:
            for right in right_trees:
                result.append(TreeNode(0, left, right))
        return result

    def all_possible_full_binary_trees(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}

        def build(nodes):
            if nodes in memo:
                return memo[nodes]

            if nodes == 1:
                return [TreeNode(0)]

            result = []

            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - left_nodes - 1

                left_trees = build(left_nodes)
                right_trees = build(right_nodes)

                result.extend(
                    self.combine_trees(left_trees, right_trees)
                )

            memo[nodes] = result
            return result

        return build(n)
if __name__ == "__main__":
    n = 3

    s = Solution()
    trees = s.all_possible_full_binary_trees(n)

    def treetraversal(root: Optional[TreeNode]):
        if root is None:
            return

        print(root.val, end=" ")

        treetraversal(root.left)
        treetraversal(root.right)

    print(f"Number of Full Binary Trees: {len(trees)}")

    for i, tree in enumerate(trees, start=1):
        print(f"\nTree {i}: ", end="")
        treetraversal(tree)
        print()