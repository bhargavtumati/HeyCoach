"""### Problem Statement: Number of Sub-arrays With Sum Equal to Goal

Given a binary array `nums` (containing only `0` and `1`) and an integer `goal`, find the **number of non-empty contiguous subarrays** whose sum is exactly equal to `goal`.

Return the count of such subarrays.

---

### Example 1:

**Input:**

```python
nums = [1,0,1,0,1]
goal = 2
```

---

### Explanation:

Find all subarrays whose sum is `2`.

Subarrays:

```
[1,0,1]     → sum = 2
[1,0,1,0]   → sum = 2
[0,1,0,1]   → sum = 2
[1,0,1]     → sum = 2
```

Total number of valid subarrays:

```
4
```

---

### Output:

```python
4
```

---

### Approach: Prefix Sum + Hash Map

For every index, calculate the running sum:

```
prefix_sum[i] = sum of elements from start to i
```

If:

```
current_sum - goal
```

was seen before, then the subarray between that previous position and current position has sum equal to `goal`.

Formula:

```
Subarray Sum = Current Prefix Sum - Previous Prefix Sum
```

So:

```
Previous Prefix Sum = Current Prefix Sum - goal
```

---

### Example Walkthrough:

Input:

```
nums = [1,0,1,0,1]
goal = 2
```

Prefix sums:

```
Index:        0  1  2  3  4
nums:         1  0  1  0  1
prefix_sum:   1  1  2  2  3
```

At prefix sum `2`:

```
2 - goal = 0
```

Prefix sum `0` exists initially, so a valid subarray is found.

The hashmap stores how many times each prefix sum appears.

---

### Complexity:

Let `N` be the length of the array.

Time Complexity:

```
O(N)
```

(Only one pass through the array)

Space Complexity:

```
O(N)
```

(Hash map stores prefix sums)

---

This is the classic **LeetCode 930 - Binary Subarrays With Sum** problem.
"""

from collections import defaultdict
from typing import List


class numSubarraysWithSum:
    def Solution(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)  # creating array of nums length+1
        count = 0  
        sum_map = defaultdict(int)  # dict empty
        sum_map[0] = 1  # Initialize with one occurrence of prefix sum 0

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            if prefix_sum[i + 1] - goal in sum_map:  #if in map
                count += sum_map[prefix_sum[i + 1] - goal]   #count+
            sum_map[prefix_sum[i + 1]] += 1

        return count
if __name__ == "__main__":
    ns= numSubarraysWithSum()
    nums=[1,0,1,0,1]
    k=2
    print(ns.Solution(nums,k))
    