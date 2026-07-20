"""### Problem Statement: Binary Tree Traversals

Given a binary tree, perform different types of tree traversals and return the order in which the nodes are visited.

A binary tree consists of nodes where each node has:

* A value (`data`)
* A left child
* A right child

Implement the following traversals:

1. **Level Order Traversal (BFS)**
2. **Preorder Traversal (DFS)**
3. **Inorder Traversal (DFS)**
4. **Postorder Traversal (DFS)**

---

## Example

Given the binary tree:

```
             1
           /   \
          2     3
         /     / \
        4     5   6
```

---

## 1. Level Order Traversal (BFS)

### Output:

```text
[
 [1],
 [2,3],
 [4,5,6]
]
```

### Explanation:

Nodes are visited level by level from top to bottom.

---

## 2. Preorder Traversal

Order:

```
Root → Left → Right
```

### Output:

```text
[1,2,4,3,5,6]
```

### Explanation:

Visit the root first, then left subtree, then right subtree.

---

## 3. Inorder Traversal

Order:

```
Left → Root → Right
```

### Output:

```text
[4,2,1,5,3,6]
```

### Explanation:

Visit the left subtree, then root, then right subtree.

---

## 4. Postorder Traversal

Order:

```
Left → Right → Root
```

### Output:

```text
[4,2,5,6,3,1]
```

### Explanation:

Visit both child subtrees before visiting the root.

---

## Constraints

```
1 <= Number of nodes <= 10^5

Node values can be integers.

The tree may be empty.
```

---

## Function Definitions

### Level Order Traversal

```python
def level_order_traversal(self):
```

Returns:

```text
List of lists containing nodes at each level.
```

---

### Preorder Traversal

```python
def preorder_traversal(self, root):
```

Returns:

```text
List containing nodes in Root → Left → Right order.
```

---

### Inorder Traversal

```python
def inorder_traversal(self, root):
```

Returns:

```text
List containing nodes in Left → Root → Right order.
```

---

### Postorder Traversal

```python
def postorder_traversal(self, root):
```

Returns:

```text
List containing nodes in Left → Right → Root order.
```

---

## Complexity Analysis

For all DFS traversals:

**Time Complexity:**

```
O(N)
```

Every node is visited once.

**Space Complexity:**

```
O(H)
```

where `H` is the height of the tree (recursion stack).

---

For Level Order Traversal:

**Time Complexity:**

```
O(N)
```

**Space Complexity:**

```
O(W)
```

where `W` is the maximum width of the tree (queue size).
"""


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_traversal(self):  #bfs
        # Formalities/Edge Cases
        if self.root is None:
            return []

        result = []

        # Main logic
        q = deque()
        q.append(self.root)

        while q:
            level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                # This is the place where you edit your elements
                level_nodes.append(curr.data)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            # This is the place where level shift happens
            result.append(level_nodes)

        return result
    
    def levels(self):
        result = self.level_order_traversal()
        return len(result)
    
    def preorder_traversal(self, root):   #dfs
        # formalities
        if root is None:
            return []
        
        result = []
        result.append(root.data)
        result.extend(self.preorder_traversal(root.left))
        result.extend(self.preorder_traversal(root.right))
        return result

    def inorder_traversal(self, root):   #dfs
        # formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.inorder_traversal(root.left))
        result.append(root.data)
        result.extend(self.inorder_traversal(root.right))
        return result
    
    def postorder_traversal(self, root):   #dfs
        # formalities
        if root is None:
            return []
        
        result = []
        result.extend(self.postorder_traversal(root.left))
        result.extend(self.postorder_traversal(root.right))
        result.append(root.data)
        return result

tree = BinaryTree()

tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)


print("level order traversal")
print(tree.level_order_traversal())
print("tree levels")
print(tree.levels())
print("pre order traversal")
print(tree.preorder_traversal(tree.root))
print("inorder traversal")
print(tree.inorder_traversal(tree.root))
print("postorder traversal")
print(tree.postorder_traversal(tree.root))