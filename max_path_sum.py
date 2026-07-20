"""### Problem Statement

Given the root of a **binary tree**, find the **maximum path sum**.

A path:

* Can start and end at any node.
* Must follow connected nodes through parent-child relationships.
* Cannot visit the same node more than once.

Return the maximum possible sum of node values along any path.

### Example

**Input:**

```text id="xv3qgd"
        1
       / \
      2   3
```

**Output:**

```text id="b4az0q"
6
```

### Explanation:

The maximum path is:

```text id="2c9n8k"
2 → 1 → 3
```

Sum:

```text id="u9p1b4"
2 + 1 + 3 = 6
```

### Approach

* Use **DFS recursion**.
* For every node:

  * Find the maximum path sum from the left subtree.
  * Find the maximum path sum from the right subtree.
  * Ignore negative paths by taking `max(value, 0)`.
  * Calculate the path passing through the current node:

```text id="h0a8ol"
node.val + leftMax + rightMax
```

* Update the global maximum result.
* Return the best single-side path to the parent:

```text id="52a6n9"
node.val + max(leftMax, rightMax)
```

### Complexity

Let `n` be the number of nodes.

* **Time Complexity:** `O(n)`
  (Each node is visited once)

* **Space Complexity:** `O(h)`
  (Recursion stack, where `h` is the tree height)

### Key Idea

A node can contribute to the final path from both sides, but when returning to its parent, it can only continue through **one side** (left or right).
"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binary_tree_paths import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(node):
            nonlocal res
            if not node: return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res = max(res, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax , rightMax)

        dfs(root)
        return res
if __name__ == "__main__":
    # Example usage: Create a sample binary tree
    #       1
    #      / \
    #     2   3
         
          
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    print(s.maxPathSum(root))
    