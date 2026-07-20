"""### Problem Statement: Maximum Width of Binary Tree

Given the root of a binary tree, return the **maximum width** of the binary tree.

The width of a level is defined as the number of nodes between the **leftmost non-null node** and the **rightmost non-null node** at that level, including the null positions between them.

The maximum width is the largest width among all levels.

---

### Example

**Input:**

```
        1
       / \
      2   3
     /     \
    4       5
```

**Output:**

```
4
```

### Explanation:

Level 1:

```
        1
```

Width = 1

Level 2:

```
      2   3
```

Width = 2

Level 3:

```
    4       5
```

Considering positions:

```
    4       5
```

Positions are:

```
4 _ _ 5
```

Width = 4

Therefore:

```
Maximum width = 4
```

---

### Approach Used: BFS + Position Indexing

Your code uses **Breadth First Search (Level Order Traversal)**.

Each node is assigned a position number like a complete binary tree:

For a node at index `num`:

* Left child:

```
2 * num
```

* Right child:

```
2 * num + 1
```

Example:

```
          1
        /   \
       2     3
      /       \
     4         7
```

Indexes:

```
          1
        /   \
       2     3
      /       \
     4         7
```

Width:

```
7 - 4 + 1 = 4
```

---

### Algorithm

1. Put the root into a queue with:

   ```
   [node, position, level]
   ```

2. For every level:

   * Track the first node's position (`prevNum`).
   * Calculate current width:

     ```
     current_width = current_position - first_position + 1
     ```

3. Add children with their calculated positions.

4. Return the maximum width found.

---

### Time Complexity

Every node is visited once:

```
O(N)
```

where `N` is the number of nodes.

---

### Space Complexity

Queue stores nodes of the largest level:

```
O(N)
```

---

### Note about your implementation

Your queue initialization:

```python
q = deque([[root,1,0]])
```

works, but if `root` is `None`, it will fail.

A safer version:

```python
if not root:
    return 0
```

should be added at the beginning.

Also, `level` does not need to be stored separately because BFS naturally processes levels. You can simplify it using a loop over `len(q)`.
"""
from collections import deque
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root,1,0]]) # [node,num,level]
        prevLevel,prevNum=0,1
        while q:
            node,num , level = q.popleft()

            if level>prevLevel:
                prevLevel=level
                prevNum=num
            res = max(res,num - prevNum+1)
            if node.left:
                q.append([node.left,2*num,level+1])
            if node.right:
                q.append([node.right,2*num+1,level+1])
        return res
    
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    
    # Create an instance of Solution
    s = Solution()
    
    # Calculate the width
    result = s.widthOfBinaryTree(root)
    print(f"Width of the binary tree: {result}")