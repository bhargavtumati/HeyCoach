""" Your code is for:

* LeetCode 257: Binary Tree Paths

## Problem Statement

Given the `root` of a binary tree, return **all root-to-leaf paths** in any order.

A **leaf** is a node with no children.

---

### Example 1

**Input**

```text
        1
       / \
      2   3
       \
        5
```

**Output**

```text
["1->2->5", "1->3"]
```

**Explanation**

There are two root-to-leaf paths:

* `1 -> 2 -> 5`
* `1 -> 3`

---

### Example 2

**Input**

```text
    1
```

**Output**

```text
["1"]
```

---

### Constraints

```text
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
```

---

### Function Signature

```python
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
```

Return a list of strings, where each string represents a path from the **root** to a **leaf**, with node values separated by `"->"`.

---

### Example

For the tree:

```text
       1
      / \
     2   3
      \
       5
```

The returned list should be:

```python
["1->2->5", "1->3"]
```

---

### Note about your code

Your algorithm is correct, but in your `main` function you call:

```python
paths = solution.binaryTreePaths(root)
```

However, your method is defined as:

```python
def binary_tree_paths(self, root):
```

So it should be:

```python
paths = solution.binary_tree_paths(root)
```

or rename the method to `binaryTreePaths` if you want to match the LeetCode function name.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: Optional[TreeNode], current_path: str, result: List[str]):
            current_path += "->" + str(root.val)
            if not root.left and not root.right:
                result.append(current_path)
            if root.left:
                dfs(root.left, current_path, result)
            if root.right:
                dfs(root.right, current_path, result)

        result = []
        if not root:
            return result
        current_path = str(root.val)
        if not root.left and not root.right:
            result.append(current_path)
        if root.left:
            dfs(root.left, current_path, result)
        if root.right:
            dfs(root.right, current_path, result)
        return result

if __name__ == "__main__":
    # Example usage: Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    solution = Solution()
    paths = solution.binaryTreePaths(root)
    for i in range(len(paths)):
        if i==0:
            print("["+paths[i],end='')
        if i>0 and i<len(paths)-1:
            print(","+paths[i],end='')
        if i==len(paths)-1:
            print(","+paths[i]+"]",end='')

