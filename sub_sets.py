"""### Problem Statement: Subsets (Power Set)

Given an integer array `nums` containing **unique elements**, return all possible subsets (the power set).

The solution set must **not contain duplicate subsets**. The order of subsets does not matter.

---

### Example 1

**Input:**

```text
nums = [1,2,3]
```

**Output:**

```text
[
 [],
 [1],
 [2],
 [3],
 [1,2],
 [1,3],
 [2,3],
 [1,2,3]
]
```

**Explanation:**

The array has 3 elements, so the total number of possible subsets is:

```
2^3 = 8
```

---

### Example 2

**Input:**

```text
nums = [0]
```

**Output:**

```text
[
 [],
 [0]
]
```

---

### Constraints

```text
1 <= nums.length <= 10

-10 <= nums[i] <= 10
```

All elements in `nums` are unique.

---

### Function Signature

Python:

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
```

Return all possible subsets of `nums`.

---

## Approach Used in Your Code

Your solution uses **Backtracking (Depth First Search)**.

### Recursive State:

```python
backtrack(start, path)
```

* `start` → index from where to pick the next element
* `path` → current subset being built

---

### Working Example

For:

```python
nums = [1,2,3]
```

Start:

```
path = []
```

Add current path:

```
[]
```

Choose `1`:

```
[1]
```

Choose `2`:

```
[1,2]
```

Choose `3`:

```
[1,2,3]
```

Backtrack and explore other choices.

Final result:

```
[
[],
[1],
[1,2],
[1,2,3],
[1,3],
[2],
[2,3],
[3]
]
```

---

### Complexity Analysis

Number of subsets:

```
2^n
```

Each subset requires copying the path.

### Time Complexity:

```
O(n * 2^n)
```

### Space Complexity:

```
O(n)
```

for recursion depth (excluding output storage).
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result
    
if __name__ == "__main__":
    f = Solution()
    nums=[1,2,3]
    print(f.subsets(nums))