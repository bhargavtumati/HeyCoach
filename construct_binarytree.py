"""
Your code is the solution for:

* LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement

Given two integer arrays:

* `preorder`, where `preorder` is the preorder traversal of a binary tree.
* `inorder`, where `inorder` is the inorder traversal of the same tree.

Construct and return the binary tree.

You may assume that all values in the tree are **unique**.

---

### Example 1

**Input**

```text
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

**Output**

```text
        3
       / \
      9   20
         /  \
        15   7
```

The returned tree has the structure:

```text
TreeNode(3)
├── left: TreeNode(9)
└── right: TreeNode(20)
    ├── left: TreeNode(15)
    └── right: TreeNode(7)
```

---

### Example 2

**Input**

```text
preorder = [-1]
inorder = [-1]
```

**Output**

```text
TreeNode(-1)
```

---

### Constraints

```text
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
```

---

### Function Signature

```python
def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
```

Return the root of the reconstructed binary tree.

---

### Traversal Reminder

For the tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

* **Preorder (Root → Left → Right):**

```text
[3, 9, 20, 15, 7]
```

* **Inorder (Left → Root → Right):**

```text
[9, 3, 15, 20, 7]
```

Using these two traversals, the binary tree can be uniquely reconstructed because all node values are distinct.
"""



from collections import deque
from typing import List, Optional

from binary_tree_paths import TreeNode


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        VAL_TO_INORDER_IDX = {inorder[i]: i for i in range(len(inorder))}

        def build_tree_partition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None

            root_val = preorder[0]
            root_inorder_idx = VAL_TO_INORDER_IDX[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None
            
            root = TreeNode(preorder.pop(0))
            root.left = build_tree_partition(preorder, inorder_start, root_inorder_idx - 1)
            root.right = build_tree_partition(preorder, root_inorder_idx + 1, inorder_end)

            return root

        return build_tree_partition(preorder, 0, len(inorder) - 1)
if __name__ == "__main__":    
   preorder=[3,9,20,15,7]
   inorder=[9,3,15,20,7]
   v=Solution()
   head=v.build_tree(preorder,inorder)
   
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
   print(level_order_traversal(head))
