"""### Problem Statement: Rotate Matrix by 90 Degrees

Given an **N × N matrix**, rotate the matrix **90 degrees clockwise**.

The rotation must be done **in-place**, meaning you should modify the original matrix without using another matrix.

---

### Example 1

**Input:**

```text
matrix =
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

**Output:**

```text
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

**Explanation:**

The matrix is rotated clockwise by 90 degrees.

Steps:

1. Transpose the matrix:

```
[
 [1,4,7],
 [2,5,8],
 [3,6,9]
]
```

2. Reverse each row:

```
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

---

### Example 2

**Input:**

```text
matrix =
[
 [5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]
]
```

**Output:**

```text
[
 [15,13,2,5],
 [14,3,4,1],
 [12,6,8,9],
 [16,7,10,11]
]
```

---

### Constraints

```
1 <= n <= 20

matrix.length == matrix[i].length == n

-1000 <= matrix[i][j] <= 1000
```

---

### Function Signature

Python:

```python
def rotate(self, matrix):
```

Return the rotated matrix after modifying it in-place.

---

### Approach Used in Your Code

Your solution uses the optimal approach:

1. **Transpose the matrix**

   * Convert rows into columns.

2. **Reverse each row**

   * Gives the clockwise 90° rotation.

### Time Complexity

```
O(n²)
```

Every element is visited once.

### Space Complexity

```
O(1)
```

Rotation is performed in-place.
"""

class Solution:
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
          for j in range(i,n):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
        for i in range(n):
          for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        return matrix
if __name__=="__main__":
   d=Solution()
   matrix=[[1,2,3],
           [4,5,6],
           [7,8,9]]
   print(d.rotate(matrix))