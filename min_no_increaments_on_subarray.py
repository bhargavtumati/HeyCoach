"""### Problem Statement: Minimum Number of Operations to Form Target Array

You are given an array `target` of positive integers.

Initially, you have an array `arr` of the same length as `target` where all elements are `0`.

In **one operation**, you can choose any contiguous subarray of `arr` and increase every element in that subarray by `1`.

Your task is to find the **minimum number of operations** required to transform `arr` into `target`.

---

### Example 1:

**Input:**

```python
target = [3,1,5,4,2]
```

**Output:**

```
7
```

**Explanation:**

Start:

```
arr = [0,0,0,0,0]
```

Operations:

1. Increase entire array:

```
[1,1,1,1,1]
```

2. Increase first element:

```
[2,1,1,1,1]
```

3. Increase first element:

```
[3,1,1,1,1]
```

4. Increase elements from index 2 to 3:

```
[3,1,2,2,1]
```

5. Increase elements from index 2 to 3:

```
[3,1,3,3,1]
```

6. Increase elements from index 2 to 3:

```
[3,1,4,4,1]
```

7. Increase element at index 2:

```
[3,1,5,4,1]
```

8. Increase last element:

```
[3,1,5,4,2]
```

Minimum operations = **8**.

(Using the formula, the answer is calculated as 8.)

---

### Logic Behind Your Code

For every increase in height compared to the previous element, we need extra operations.

Formula:

```
answer = target[0] + Σ(max(0, target[i] - target[i-1]))
```

For:

```
target = [3,1,5,4,2]
```

Calculation:

```
ans = 3

1 < 3 → no addition
5 > 1 → add 4
4 < 5 → no addition
2 < 4 → no addition

Total = 3 + 4 = 7
```

So your code returns:

```
7
```

---

### Time Complexity

* **Time:** `O(N)` (single loop through array)
* **Space:** `O(1)` (only variables are used)
"""

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        prev = target[0]
        
        for i in range(1, len(target)):
            if target[i] > prev:
                ans += target[i] - prev
            prev = target[i]
        
        return ans

if __name__ == "__main__":
         target=[3,1,5,4,2]
         d=Solution()
         print(d.minNumberOperations(target))