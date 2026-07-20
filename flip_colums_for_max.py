"""### Problem Statement

Given a binary matrix, you can **flip any columns** (change all `0`s in a column to `1`s and all `1`s to `0`s).

Find the **maximum number of rows that can be made equal** after performing any number of column flips.

### Example

**Input:**

```text
matrix = [
 [0,1],
 [1,0]
]
```

**Output:**

```text
2
```

### Explanation:

Flip the first column:

```text
Before:
0 1
1 0

After flipping column 0:
1 1
0 0
```

Both rows can be made identical by choosing appropriate column flips, so the answer is `2`.

### Approach

* Rows that are complements of each other can become equal after column flips.
* Convert rows starting with `0` into their flipped form.
* Count the frequency of identical rows.
* Return the maximum frequency.

### Complexity

* **Time Complexity:** `O(m × n)`
  where `m` = number of rows and `n` = number of columns.
* **Space Complexity:** `O(m)` for storing row patterns.
"""


from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        ans = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                    elif matrix[i][j] == 1:
                        matrix[i][j] = 0
            if tuple(matrix[i]) in d:
                d[tuple(matrix[i])] += 1
            else:
                d[tuple(matrix[i])] = 1
        return max(d.values())
if __name__=="__main__":
    matrix=[[0,1],[1,0]]
    d=Solution()
    print(d.maxEqualRowsAfterFlips(matrix))