
"""### Problem Statement

Given a binary matrix containing only `'0'` and `'1'`, find the **largest rectangle containing only 1's** and return its area.

### Example

**Input:**

```text
matrix =
[
 ["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]
]
```

**Output:**

```text
6
```

### Explanation:

The largest rectangle of `1`s is:

```text
1 1 1
1 1 1
```

Area:

```text
3 × 2 = 6
```

### Approach

1. Treat each row as a **histogram**:

   * Maintain an array `height` where each value stores the consecutive number of `1`s above that cell.

2. For every row:

   * Update the histogram heights.
   * Find the largest rectangle area in the histogram.

3. For histogram calculation:

   * Use a **monotonic stack** to find:

     * Previous smaller element.
     * Next smaller element.
   * Calculate the width of the rectangle for each bar.

Formula:

```text
Area = height[i] × (next_small[i] - prev_small[i] - 1)
```

### Complexity

Let:

* `m` = number of rows
* `n` = number of columns

For each row, histogram processing takes `O(n)`.

**Time Complexity:**

```text
O(m × n)
```

**Space Complexity:**

```text
O(n)
```

(for height array and stack)

### Key Idea

Convert the 2D matrix problem into multiple **Largest Rectangle in Histogram** problems. The histogram height at each column represents how many consecutive `1`s exist vertically up to the current row.
"""

from typing import List


class Solution:
    def next_small(self, arr):
        n = len(arr)
        st = [-1]
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            curr = arr[i]
            
            while st[-1] != -1 and arr[st[-1]] >= curr:
                st.pop()
            
            ans[i] = st[-1]
            st.append(i)
        
        return ans
    
    def prev_small(self, arr):
        n = len(arr)
        st = [-1]
        ans = [0] * n
        
        for i in range(n):
            curr = arr[i]
            
            while st[-1] != -1 and arr[st[-1]] >= curr:
                st.pop()
            
            ans[i] = st[-1]
            st.append(i)
        
        return ans
    
    def largest_area(self, heights):
        n = len(heights)
        
        next_ = self.next_small(heights)
        prev = self.prev_small(heights)
        
        maxi = 0
        
        for i in range(n):
            length = heights[i]
            
            if next_[i] == -1:
                next_[i] = n
            
            breadth = next_[i] - prev[i] - 1
            area = length * breadth
            maxi = max(maxi, area)
        
        return maxi
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxi = 0
        height = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(height)):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            maxi = max(maxi, self.largest_area(height))
        
        return maxi
        
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]],  # Expected result is 6
         
        [["0", "1"],
         ["1", "0"]],  # Expected result is 1
         
        [["1"]],  # Expected result is 1
        
        [["0"]],  # Expected result is 0
    ]
    
    # Test the maximalRectangle method with the test cases
    for matrix in test_cases:
        result = solution.maximalRectangle(matrix)
        print(f"The maximal rectangle area for the given matrix is {result}.")
