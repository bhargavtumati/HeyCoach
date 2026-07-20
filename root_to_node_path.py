"""### Problem Statement: Root to Node Path in a Binary Tree

Given a **binary tree** and a target node value `key`, find the path from the **root node to the given target node**.

Return the path as a list containing all node values from the root to the target node.

If the target node does not exist in the binary tree, return an empty list.

---

### Example

Given the binary tree:

```
          1
        /   \
      12     3
     /  \   / \
    4    6 5   7
```

### Input:

```
key = 6
```

### Output:

```
[1, 12, 6]
```

### Explanation:

The path from the root node `1` to the node `6` is:

```
1 → 12 → 6
```

---

### Example 2

### Input:

```
key = 5
```

### Output:

```
[1, 3, 5]
```

---

### Example 3

### Input:

```
key = 10
```

### Output:

```
[]
```

### Explanation:

Node `10` is not present in the binary tree, so no path exists.

---

### Constraints

```
1 <= Number of nodes <= 10^5

-10^9 <= Node value <= 10^9

All node values are unique.
```

---

### Function Signature

Python:

```python
def root_to_node_path(root, key):
```

Return:

* List of node values from root to target node if found.
* Empty list if the node does not exist.
"""


class Node:
    def __init__(self,data):
        self.data =data
        self.left =None
        self.right =None

class BinaryTree:
    def __init__(self):
      self.root = None



def root_to_node_path(root,key):
   ans = []
   def traverse(node,key,path):
       nonlocal ans

       if node is None:
           return
       
       path.append(node.data)
       #print(path)  #all path
       if node.data == key:
           ans = path.copy()
           return
       else: 
           traverse(node.left,key,path)
           traverse(node.right,key,path)

       path.pop()

   traverse(root,key,[])
   return ans

tree = BinaryTree()

tree.root = Node(1)
tree.root.left =Node(12)
tree.root.right =Node(3)
tree.root.left.left =Node(4)
tree.root.left.right = Node(6)
tree.root.right.left =Node(5)
tree.root.right.right =Node(7)
print(root_to_node_path(tree.root, 6))

