
"""### Problem Statement

Given a circular integer array `nums`, find the **maximum possible sum of a non-empty subarray**.

A circular array means:

* The end of the array is connected to the beginning.
* A subarray can wrap around from the end to the start.

Return the maximum subarray sum.

### Example

**Input:**

```text
nums = [5, -3, 5]
```

**Output:**

```text
10
```

### Explanation:

Normal maximum subarray:

```text
[5]
```

Sum:

```text
5
```

Circular maximum subarray:

```text
[5] + [5]
```

Wrapping around gives:

```text
[5, -3, 5]
```

Total:

```text
5 + 5 = 10
```

### Approach

Use **Kadane's Algorithm** twice:

1. Find the normal maximum subarray sum:

```
max_sum
```

2. Find the minimum subarray sum:

```
min_sum
```

3. For circular cases:

```
circular_sum = total_sum - min_sum
```

because removing the minimum subarray leaves the maximum wrapping subarray.

4. Return:

```
max(max_sum, circular_sum)
```

Special case:

* If all numbers are negative, `total_sum - min_sum` becomes invalid, so return `max_sum`.

### Complexity

Let `n` be the size of the array.

**Time Complexity:**

```
O(n)
```

(Each element is processed once)

**Space Complexity:**

```
O(1)
```

### Key Idea

The maximum circular subarray is either:

1. A normal maximum subarray inside the array.
2. A wrapping subarray formed by taking the total sum and removing the minimum subarray.
"""

from typing import List

class Solution:
  def maxSubarraySumCircular(self,nums: List[int]) -> int:
    complete_sum = sum(nums)
    
    min_so_far = 10e5
    max_so_far = -1 * 10e5
    min_ending_here = max_ending_here = 0
    for num in nums:
        max_ending_here += num
        min_ending_here += num
        max_so_far = max(max_so_far, max_ending_here)
        min_so_far = min(min_so_far, min_ending_here)
        max_ending_here = max(0, max_ending_here)
        min_ending_here = min(0, min_ending_here)
    if complete_sum == min_so_far:
        return max_so_far
    return max(max_so_far, complete_sum - min_so_far)

if __name__ == "__main__":
    nums = [5, -3, 5]
    c = Solution()
    print(c.maxSubarraySumCircular(nums))
