
"""
### Problem Statement

Given a matrix, calculate the **k-th largest value** among all the coordinates `(row, column)` where the value at each coordinate is the **bitwise XOR of all elements in the rectangle from `(0,0)` to `(row,column)`**.

Return the `k`-th largest XOR coordinate value.

### Example

**Input:**

```text
matrix = [
 [5,2],
 [1,6]
]

k = 3
```

**XOR Matrix Calculation:**

```
(0,0) = 5

(0,1) = 5 ^ 2 = 7

(1,0) = 5 ^ 1 = 4

(1,1) = 5 ^ 2 ^ 1 ^ 6 = 0
```

XOR values:

```
[5, 7, 4, 0]
```

Sorted descending:

```
[7, 5, 4, 0]
```

3rd largest value:

```
4
```

**Output:**

```text
4
```

### Approach

* Convert the matrix into a **2D prefix XOR matrix**.
* Formula used:

[
prefix[i][j] = matrix[i][j] \oplus prefix[i-1][j] \oplus prefix[i][j-1] \oplus prefix[i-1][j-1]
]

* Store all prefix XOR values.
* Sort them in descending order.
* Return the `k-1` indexed value.

### Complexity

Let:

* `m` = number of rows
* `n` = number of columns

**Time Complexity:**
`O(m × n + m × n log(m × n))`

* Build prefix XOR: `O(m × n)`
* Sorting values: `O(m × n log(m × n))`

**Space Complexity:**
`O(m × n)` for storing XOR values.

**Optimization:** A min-heap of size `k` can reduce sorting overhead to `O(m × n log k)`.
"""

from typing import List


class Solution:
    def kth_largest_value(self, matrix: List[List[int]], k: int) -> int:
        
        for r in range(1,len(matrix)):
            matrix[r][0]^=matrix[r-1][0]
        for c in range(1,len(matrix[0])):
            matrix[0][c]^=matrix[0][c-1]
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                matrix[r][c]^=matrix[r-1][c]^matrix[r][c-1]^matrix[r-1][c-1]
        res=[]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res.append(matrix[r][c])
        res.sort(reverse=True)

        return res[k-1]
    
if __name__=="__main__":
       matrix=[[5,2],[1,6]]
       k=3
       s=Solution()
       print(s.kth_largest_value(matrix,k))
