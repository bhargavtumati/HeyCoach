"""### Problem Statement: Palindrome Partitioning

Given a string `s`, partition the string into **one or more substrings** such that **every substring is a palindrome**.

Return **all possible palindrome partitioning combinations** of the string.

A palindrome is a string that reads the same forward and backward.

---

### Example 1:

**Input:**

```python
s = "abb"
```

**Output:**

```
a b b
a bb
```

---

### Explanation:

Possible partitions of `"abb"`:

1. Split every character:

```
a | b | b
```

All are palindromes.

2. Take `"bb"` together:

```
a | bb
```

`bb` is also a palindrome.

Other partitions:

```
ab | b
```

`ab` is not a palindrome, so it is invalid.

Therefore, the valid partitions are:

```
[
 ["a","b","b"],
 ["a","bb"]
]
```

---

### Example 2:

**Input:**

```python
s = "aab"
```

**Output:**

```
a a b
aa b
```

---

### Approach: Backtracking (DFS)

At every index:

1. Try every possible substring.
2. Check whether the substring is a palindrome.
3. If it is:

   * Add it to the current partition.
   * Continue partitioning the remaining string.
4. When the entire string is processed, store the partition.

---

### Example:

For:

```
s = "abb"
```

DFS tree:

```
                abb
              /     \
             a       ab
            /         \
          bb           (not palindrome)
        /    \
       b      bb
```

Valid paths:

```
a → b → b
a → bb
```

---

### Complexity:

Let `N` be the length of the string.

Number of possible partitions:

```
O(2^N)
```

Palindrome checking:

```
O(N)
```

Total Time Complexity:

```
O(N * 2^N)
```

Space Complexity:

```
O(N)
```

(for recursion stack and current partition)

---

This is the classic **LeetCode 131 - Palindrome Partitioning** problem.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        def dfs(index: int, path: List[str]):
            if index == len(s):
                ans.append(path[:])
                return
            for end in range(index, len(s)):
                if is_palindrome(s[index:end + 1]):
                    path.append(s[index:end + 1])
                    dfs(end + 1, path)
                    path.pop()

        ans = []
        dfs(0, [])
        return ans

# Example usage
s = "abb"
solution = Solution()
result = solution.partition(s)
for partition in result:
    print(*partition)
