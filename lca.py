"""### Problem Statement

Given a binary tree and two nodes `n1` and `n2`, find their **Lowest Common Ancestor (LCA)**.

The **Lowest Common Ancestor** is the lowest node in the tree that has both given nodes as its descendants (where a node can be a descendant of itself).

### Example

**Binary Tree:**

```text
          1
        /   \
      12     3
     /  \   / \
    4    6 5   7
```

**Input:**

```text
n1 = 7
n2 = 5
```

**Output:**

```text
3
```

### Explanation:

Node `3` is the smallest node that contains both `5` and `7` in its subtree.

```text
        3
       / \
      5   7
```

Therefore, the Lowest Common Ancestor is `3`.

### Approach

* Recursively search the left and right subtrees.
* If the current node is one of the target nodes, return it.
* If both left and right subtrees return a node, the current node is the LCA.
* Otherwise, return the non-null subtree result.

### Complexity

Let `n` be the number of nodes.

* **Time Complexity:** `O(n)`
  (Each node is visited once)

* **Space Complexity:** `O(h)`
  (Recursion stack, where `h` is the height of the tree)

### Key Idea

The LCA is found when:

* One target node is found in the left subtree.
* The other target node is found in the right subtree.

The node where these paths meet is the Lowest Common Ancestor.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
#lowest common ancestor
def find_lca(root, n1, n2):
    if root is None:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    
    if left_lca is not None: 
        return left_lca
    else:
        return right_lca


tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(12)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(find_lca(tree.root, 7, 5).data)