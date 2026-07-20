"""### Problem Statement

Given the root of a **Binary Search Tree (BST)**, transform it into an **increasing order search tree** such that:

* The smallest node becomes the root.
* Every node has **no left child**.
* Each node has only a **right child** pointing to the next larger value.
* The nodes should appear in increasing order.

### Example

**Input BST:**

```text
        5
       / \
      3   6
     / \   \
    2   4   8
   /       / \
  1       7   9
```

**Output:**

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
             \
              8
               \
                9
```

### Approach

* Perform **inorder traversal** of the BST because it visits nodes in ascending order.
* Create a new tree where:

  * Left pointers are removed.
  * Nodes are connected using only right pointers.

### Complexity

* **Time Complexity:** `O(n)`
  (Visit each node once)

* **Space Complexity:** `O(h)`
  (Recursion stack, where `h` is tree height)

### Key Idea

**Inorder traversal of BST gives sorted order:**

```
Left → Root → Right
```

So we can directly rebuild the tree in increasing order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def increasingBST(root: TreeNode) -> TreeNode:   # no need to create class , if kept this definition in solution add self in attributes
        node =TreeNode(0)  # create node 0
        dummy = node  

        def inorder(node):
            nonlocal dummy
            if not node:
                return
            inorder(node.left)
            dummy.right = TreeNode(node.val)
            dummy = dummy.right
            inorder(node.right)
        inorder(root)
        return node.right

def construct_binary_tree(arr):
    if not arr:
        return None

    # Create the root node
    root = TreeNode(arr[0])
    queue = [root]  # Initialize a queue with the root

    i = 1
    while i < len(arr):
        current = queue.pop(0)  # Get the front node from the queue

        # Add left child if not null
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)

        i += 1

        # Add right child if not null
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)

        i += 1

    return root
def preorder_traversal(node):
    if node is None:
        return
    print(node.val, end=" ")  # Visit the root
    preorder_traversal(node.left)  # Recur on left subtree
    preorder_traversal(node.right) 

# Print the tree (inorder traversal for verification)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val, end=" ")

def level_order_traversal(root):
    if not root:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Given input array
input_array = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]

# Construct the binary tree
root_node = construct_binary_tree(input_array)

print("Level order traversal(breadth first traversal) of the constructed tree:")
level_order_traversal(root_node)
root_node=increasingBST(root_node)
print("\nLevel order traversal(breadth first traversal) of the inscreasing bst:")
level_order_traversal(root_node)
