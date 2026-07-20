"""### Problem Statement

Given a binary matrix `image` containing only `0`s and `1`s, perform the following two operations on every row:

1. **Flip the row horizontally** (reverse the order of elements).
2. **Invert the image** by replacing every `0` with `1` and every `1` with `0`.

Return the modified binary matrix.

### Example

**Input:**

```text
[
 [1,1,0,0],
 [1,0,0,1],
 [0,1,1,1],
 [1,0,1,0]
]
```

**Output:**

```text
[
 [1,1,0,0],
 [0,1,1,0],
 [0,0,0,1],
 [1,0,1,0]
]
```

**Time Complexity:** `O(m × n)`
**Space Complexity:** `O(1)` (in-place), where `m` is the number of rows and `n` is the number of columns.
"""


from typing import List

class flip_and_invert_image:
    def solution(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        for i in range (rows):
           for j in range ((int)(cols/2)):    
               temp=image[i][j]
               image[i][j]=image[i][cols-1-j]
               image[i][cols-1-j]=temp
        

        for i in range (rows):
           for j in range(cols):
            if(image[i][j]==0):
               image[i][j]=1
            else:
               image[i][j]=0

        return image       
    
if __name__ == "__main__":
    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    fm = flip_and_invert_image()
    print(fm.solution(image))