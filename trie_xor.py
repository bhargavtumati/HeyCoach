"""### Problem Statement: Maximum XOR Pair Using Trie

Given an array of `n` integers, find the **maximum XOR value** that can be obtained by choosing any two elements from the array.

You need to use a **Binary Trie (Prefix Trie)** where each number is stored using its **32-bit binary representation**.

For two numbers `a` and `b`:

```
XOR = a ^ b
```

The goal is to find:

```
max(a[i] ^ a[j])
```

where:

```
i != j
```

---

### Example 1

**Input:**

```text
n = 3

arr = [1,2,3]
```

Binary representation:

```
1 = 001
2 = 010
3 = 011
```

Possible XOR values:

```
1 ^ 2 = 3

1 ^ 3 = 2

2 ^ 3 = 1
```

Maximum XOR:

```
3
```

**Output:**

```text
3
```

---

### Example 2

**Input:**

```text
n = 4

arr = [8,10,2,15]
```

Binary:

```
8  = 1000
10 = 1010
2  = 0010
15 = 1111
```

Maximum XOR:

```
8 ^ 15 = 7
```

**Output:**

```text
15
```

(Example depends on the chosen values; the task is to return the maximum XOR value.)

---

### Constraints

```
2 <= n <= 10^4

0 <= arr[i] <= 2^31
```

---

### Function Signature

Python:

```python
def solve(self, root, ar, n):
```

Return:

```
Maximum XOR value possible between any two elements.
```

---

## Approach: Binary Trie

### 1. Insert Numbers into Trie

Each number is converted into a 32-bit binary form.

Example:

```
num = 5

Binary:
00000000000000000000000000000101
```

Each bit is stored as:

```
0 → left child
1 → right child
```

---

### 2. Find Maximum XOR

For every number:

* Check each bit from left to right.
* To maximize XOR:

  * If current bit is `0`, try to go to a `1` branch.
  * If current bit is `1`, try to go to a `0` branch.

Because:

```
0 ^ 1 = 1
1 ^ 0 = 1
```

We always prefer opposite bits.

---

### Example Walkthrough

Array:

```
[1,2,3]
```

Insert:

```
1 = 001
2 = 010
3 = 011
```

For number `1`:

```
1 = 001
```

Trie finds:

```
010
```

XOR:

```
001
010
---
011 = 3
```

Maximum XOR:

```
3
```

---

### Complexity Analysis

Let:

* `n` = number of elements
* `32` = number of bits

### Time Complexity:

Insertion:

```
O(32 * n)
```

Searching:

```
O(32 * n)
```

Overall:

```
O(32n)
```

or simply:

```
O(n)
```

because 32 is constant.

---

### Space Complexity:

Trie stores:

```
O(32 * n)
```

nodes in the worst case.

---

### Key Idea

A normal brute-force solution checks every pair:

```
O(n²)
```

The Binary Trie reduces it to:

```
O(32n)
```

by greedily choosing opposite bits to maximize XOR.
"""

class TrieNode:
    def __init__(self):
        self.left = None  # Represents the presence of zero at ith bit
        self.right = None # Represents the presence of one at ith bit

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right

    def find_max_xor(self, root, num):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if node.right:
                    max_xor = (max_xor << 1) | 1
                    node = node.right
                else:
                    max_xor = (max_xor << 1)
                    node = node.left
            else:
                if node.left:
                    max_xor = (max_xor << 1) | 1
                    node = node.left
                else:
                    max_xor = (max_xor << 1)
                    node = node.right
        return max_xor

    def solve(self, root, ar, n):
        for num in ar:
            self.insert(root, num)
        
        max_xor = 0
        for num in ar:
            max_xor = max(max_xor, self.find_max_xor(root, num))
        
        return max_xor

# Example usage:
root = TrieNode()
solution = Solution()
ar = [1, 2, 3]
n = len(ar)
print(solution.solve(root, ar, n))  # Output: 3
"""
XOR Pair in Trie
You are given an array containing n number of elements. The elements of the array are inserted in a Trie data structure in the form of binary representation for example 1, 2 and 3 will be represented as:

                    0                   2nd bit
                 0>0   0>1
                 0      1               1st bit
                0>1  1>0  1>1   
                  1   0    1            0th bit
Note that the Trie is for 32-bit representation and out of those only first three are shown in the example above.

Your task is to use the trie in order to find the max XOR pair. This can also be done without using Trie but I encourage you to try and solve the question using trie.

Sample Input:

3

1 2 3

Sample Output: 3

Max XOR pair is 1 and 2 whose XOR is equal to 3.

Constraints:

2 <= n <= 10^4

2^0 <= A[i] <=2^31"""