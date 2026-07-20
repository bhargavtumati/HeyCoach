"""### Problem Statement

Design a system to maintain the **inheritance order of a royal family**.

The system supports:

1. **Birth:** Add a child to a parent. Children inherit in the order they are born.
2. **Death:** Mark a person as deceased.
3. **Get Inheritance Order:** Return the current inheritance order following these rules:

   * Start from the king.
   * Visit children in birth order.
   * A deceased person is skipped, but their children remain in the order.

### Example

**Operations:**

```text
King: king

Birth:
king → andy
king → bob
king → catherine
andy → matthew
bob → alex
bob → asha

Death:
bob
```

**Output:**

```text
[
 "king",
 "andy",
 "matthew",
 "catherine",
 "alex",
 "asha"
]
```

### Approach

* Store the family tree using an adjacency list (`graph`).
* Store deceased people in a set.
* Use **DFS preorder traversal**:

  * Visit a person first.
  * Then visit their children in birth order.
  * Skip only deceased people.

### Complexity

Let `n` be the number of family members.

* **Birth:** `O(1)`
* **Death:** `O(1)`
* **Get Inheritance Order:** `O(n)`
* **Space Complexity:** `O(n)`

### Key Idea

The family tree is a **rooted tree**, and the inheritance order is simply a **preorder traversal** while ignoring deceased nodes.
"""
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.dead = set()
        self.graph = {kingName: []}
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph.setdefault(parentName, []).append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(n):
            """Pre-order traverse the graph."""
            if n not in self.dead:
                ans.append(n)
            for nn in self.graph.get(n, []):
                dfs(nn)

        ans = []
        dfs(self.root)
        return ans

# Example usage:
if __name__ == "__main__":
    # Create an instance of the ThroneInheritance class
    obj = ThroneInheritance("king")

    # Perform births
    obj.birth("king", "andy")
    obj.birth("king", "bob")
    obj.birth("king", "catherine")
    obj.birth("andy", "matthew")
    obj.birth("bob", "alex")
    obj.birth("bob", "asha")

    # Perform deaths
    obj.death("bob")

    # Get the inheritance order
    inheritance_order = obj.getInheritanceOrder()
    print(inheritance_order)  # Output: ['king', 'andy', 'matthew', 'catherine', 'asha']
