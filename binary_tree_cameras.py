""" Your code is the solution to:

* LeetCode 968: Binary Tree Cameras

## Problem Statement

You are given the `root` of a binary tree.

Install cameras on some of the tree's nodes so that **every node** in the tree is monitored.

A camera at a node can monitor:

* The node itself.
* Its parent.
* Its immediate left child.
* Its immediate right child.

Return the **minimum number of cameras** needed to monitor all nodes of the tree.

---

## Example 1

**Input**

```text
    0
   /
  0
 / \
0   0
```

**Output**

```text
1
```

**Explanation**

Placing a camera on the second node (the left child of the root) monitors:

* itself,
* its parent,
* its left child,
* its right child.

Thus, only **one camera** is needed.

---

## Example 2

**Input**

```text
      0
     /
    0
   /
  0
 /
0
```

**Output**

```text
2
```

**Explanation**

One camera cannot monitor all four nodes, so at least **two cameras** are required.

---

## Constraints

* The number of nodes in the tree is in the range **[1, 1000]**.
* Every node has a value of `0`.
* `Node.val == 0`.

---

## Function Signature

```python
def minCameraCover(root: Optional[TreeNode]) -> int:
```

Return the minimum number of cameras required to monitor the entire binary tree.

---

### Your approach

Your solution performs a **postorder DFS** and classifies each node into one of three states:

* **0** → Node is **not monitored**.
* **1** → Node **has a camera**.
* **2** → Node is **monitored** by one of its children.

After processing the tree, if the root is still unmonitored, you place one final camera at the root. 
This greedy postorder approach is the standard optimal solution for LeetCode 968.
"""

from typing import Optional
from binary_tree_paths import TreeNode


class Solution:
    def min_camera_cover(self, root: TreeNode) -> int:
        # set the value of camera nodes to 1
        # set the value of monitored parent nodes to 2
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            res = dfs(node.left)+dfs(node.right)
            # find out if current node is a root node / next node in line to be monitored
            curr = min(node.left.val if node.left else float('inf'), node.right.val if node.right else float('inf'))
            if curr == 0:
                # at least one child node requires monitoring, this node must have a camera
                node.val = 1
                res += 1
            elif curr == 1:
                # at least one child node is a camera, this node is already monitored
                node.val = 2
            # if curr == float('inf'), the current node is a leaf node; let the parent node monitor this node
            # if curr == 2, all child nodes are being monitored; treat the current node as a leaf node
            return res
        # ensure that root node is monitored, otherwise, add a camera onto root node
        return dfs(root)+(root.val == 0)
if __name__ =="__main__":
     cp=Solution()
     root = TreeNode(0)
     root.left = TreeNode(0)
     root.right = None
     root.left.left = TreeNode(0)
     root.left.right = TreeNode(0)
     print(cp.min_camera_cover(root))