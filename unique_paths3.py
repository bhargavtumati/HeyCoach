"""### Problem Statement: Unique Paths III

You are given a grid where:

* `1` represents the **starting square**.
* `2` represents the **ending square**.
* `0` represents an **empty square** that must be visited.
* `-1` represents an **obstacle** that cannot be visited.

Return the number of **unique paths** from the starting square to the ending square such that:

1. You visit **every empty square exactly once**.
2. You reach the ending square after visiting all empty squares.
3. You cannot move through obstacles.
4. You can move only in four directions:

   * Up
   * Down
   * Left
   * Right

---

### Example 1

**Input:**

```python
grid = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,2,-1]
]
```

**Output:**

```python
2
```

### Explanation:

There are two valid paths:

Path 1:

```
(0,0) → (0,1) → (0,2) → (0,3)
        ↓
(1,3) → (1,2) → (1,1) → (1,0)
        ↓
(2,0) → (2,1) → (2,2)
```

Path 2:

```
(0,0) → (1,0) → (2,0) → (2,1)
        ↑
(1,1) → (1,2) → (1,3)
        ↑
(0,3) → (0,2) → (0,1)
        ↓
(2,2)
```

Both paths:

* Start at `1`
* Visit all `0` cells once
* End at `2`

---

### Constraints

* `1 <= grid.length, grid[0].length <= 20`
* There is exactly one starting square.
* There is exactly one ending square.
* The grid contains obstacles and empty cells.

---

### Algorithm Used

This solution uses **Backtracking (DFS)**:

1. Find:

   * Starting position
   * Ending position
   * Number of empty cells

2. Start DFS from the starting cell.

3. At each step:

   * Mark the cell as visited.
   * Move in four directions.
   * Backtrack by unmarking the cell.

4. When reaching the end:

   * Check if all empty cells were visited.
   * If yes, increment answer.

---

### Time Complexity

For a grid with `N` walkable cells:

```
O(4^N)
```

because each cell can branch into four possible directions.

### Space Complexity

```
O(N)
```

for:

* visited matrix
* recursion stack

---

### Difference Between Your Two Versions

First version:

```python
backtrack(i+1, j, visited, path+[(i,j)])
```

stores the complete path list.

Second version:

```python
backtrack(i+1, j, visited, walk+1)
```

only stores the number of visited cells.

The second version is better because:

* No list creation at every recursion.
* Less memory usage.
* Faster execution.

You only need the count, not the actual path, so `walk` is the preferred approach.
"""

class Solution:
    def __init__(self):
        self.ans = 0

    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        start_i, start_j = None, None
        end_i, end_j = None, None
        empty_cells = 0

        # Find the starting and ending squares
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j
                elif grid[i][j] == 0:
                    empty_cells += 1

        def backtrack(i, j, visited,path):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or visited[i][j]:
                return

            if (i, j) == (end_i, end_j):
                if len(path) == empty_cells + 1:  # +1 for end cell
                    self.ans += 1
                return

            visited[i][j] = True
            backtrack(i + 1, j, visited,path+[(i,j)])
            backtrack(i - 1, j, visited,path+[(i,j)])
            backtrack(i, j + 1, visited,path+[(i,j)])
            backtrack(i, j - 1, visited,path+[(i,j)])
            visited[i][j] = False

        visited = [[False] * cols for _ in range(rows)]
        backtrack(start_i, start_j, visited,[])
        return self.ans

# Example usage:
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
solution = Solution()
print(solution.uniquePathsIII(grid))  # Output: 2


"""
 def backtrack(i, j, visited,walk):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or visited[i][j]:
                return

            if (i, j) == (end_i, end_j):
                if walk == empty_cells + 1:  # +1 for end cell
                    self.ans += 1
                return

            visited[i][j] = True
            backtrack(i + 1, j, visited,walk+1)
            backtrack(i - 1, j, visited,walk+1)
            backtrack(i, j + 1, visited,walk+1)
            backtrack(i, j - 1, visited,walk+1)
            visited[i][j] = False

        visited = [[False] * cols for _ in range(rows)]
        backtrack(start_i, start_j, visited,0)
        return self.ans"""