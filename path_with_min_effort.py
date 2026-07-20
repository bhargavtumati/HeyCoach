"""### Problem Statement: Path With Minimum Effort

You are given a grid `heights` where:

* `heights[i][j]` represents the height of cell `(i, j)`.
* You can move **up, down, left, or right** between adjacent cells.

The **effort of a path** is defined as the maximum absolute difference in heights between two consecutive cells in that path.

Your task is to find the **minimum effort required to travel from the top-left cell `(0,0)` to the bottom-right cell `(m-1,n-1)`**.

---

### Example:

**Input:**

```python
heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]
```

---

### Explanation:

Possible paths:

Path 1:

```
1 → 2 → 2 → 2 → 5
```

Differences:

```
|1-2| = 1
|2-2| = 0
|2-2| = 0
|2-5| = 3
```

Effort:

```
max(1,0,0,3) = 3
```

---

Path 2:

```
1 → 3 → 5 → 3 → 5
```

Differences:

```
|1-3| = 2
|3-5| = 2
|5-3| = 2
|3-5| = 2
```

Effort:

```
2
```

Minimum effort:

```
2
```

---

### Output:

```python
2
```

---

## Approach: Dijkstra's Algorithm

Unlike normal shortest path problems where we add edge weights, here we minimize the **maximum edge difference** along the path.

For each cell:

* Store the minimum effort required to reach that cell.
* Use a min heap to always process the cell with the smallest current effort.

---

### State:

```python
dist[i][j]
```

represents:

> Minimum effort needed to reach cell `(i,j)`.

---

### Transition:

Moving from:

```
(x,y) → (nx,ny)
```

The effort becomes:

```python
new_effort = max(
    current_effort,
    abs(heights[x][y] - heights[nx][ny])
)
```

We update if:

```python
new_effort < dist[nx][ny]
```

---

### Example Heap Process:

Initial:

```
Heap = [(0,0,0)]
```

Meaning:

```
(effort, row, column)
```

The algorithm always chooses the path with the smallest effort first.

---

### Complexity:

Let:

```
R = number of rows
C = number of columns
```

Number of cells:

```
R × C
```

Time Complexity:

```
O(R × C × log(R × C))
```

Space Complexity:

```
O(R × C)
```

---

This is the classic **LeetCode 1631 - Path With Minimum Effort** problem using **Dijkstra's Algorithm**.
"""

from heapq import heappop, heappush
import math
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] 
        
        while minHeap:
            effort, x, y = heappop(minHeap)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(minHeap, (new_effort, nx, ny))

if __name__=="__main__":
   heights =  [[1,2,2],[3,8,2],[5,3,5]]
   s=Solution()
   print(s.minimumEffortPath(heights))