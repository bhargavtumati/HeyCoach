"""
Your code is for:

* LeetCode 1008: Construct Binary Search Tree from Preorder Traversal

## Problem Statement

Given an array of integers `preorder`, which represents the **preorder traversal** of a Binary Search Tree (BST), construct the BST and return its root.

It is guaranteed that there is always a valid answer for the given preorder traversal.

A **Binary Search Tree (BST)** satisfies the following properties:

* The left subtree of a node contains only nodes with values **less than** the node's value.
* The right subtree of a node contains only nodes with values **greater than** the node's value.
* Both the left and right subtrees must also be binary search trees.

---

### Example 1

**Input**

```text
preorder = [8,5,1,7,10,12]
```

**Output**

```text
        8
       / \
      5   10
     / \    \
    1   7    12
```

The constructed BST is:

```text
TreeNode(8)
├── left: TreeNode(5)
│   ├── left: TreeNode(1)
│   └── right: TreeNode(7)
└── right: TreeNode(10)
    └── right: TreeNode(12)
```

---

### Example 2

**Input**

```text
preorder = [1,3]
```

**Output**

```text
    1
     \
      3
```

---

### Constraints

```text
1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.
```

---

### Function Signature

```python
def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
```

Return the root of the constructed Binary Search Tree.

---


"""


from typing import List, Optional

from binary_tree_paths import TreeNode


class Solution:
    def bst_from_preorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct_tree_util(pre, pre_index, low, high):
             if pre_index[0] >= len(pre) or low > high:
                  return None

             root = TreeNode(pre[pre_index[0]])
             pre_index[0] += 1

             i = low
             while i <= high:
                 if pre[i] > root.val:
                     break
                 i += 1

             root.left = construct_tree_util(pre, pre_index, pre_index[0], i - 1)
             root.right = construct_tree_util(pre, pre_index, i, high)

             return root

        pre_index = [0]
        return construct_tree_util(preorder, pre_index, 0, len(preorder) - 1)
    
if __name__=="__main__":    
   preorder = [8,5,1,7,10,12]
   c=Solution()
   root_node = c.bst_from_preorder(preorder)

   def level_order_traversal(root):
    if not root:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

   level_order_traversal(root_node)