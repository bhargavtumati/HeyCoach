"""### Problem Statement

Given an integer array `nums` and an index `k`, find the **maximum score** of a subarray that contains index `k`.

The score of a subarray is:

```text
minimum value in subarray × length of subarray
```

The chosen subarray must include `nums[k]`.

### Example

**Input:**

```text
nums = [1,4,3,7,4,5]
k = 3
```

**Output:**

```text
15
```

### Explanation:

Subarray containing index `3`:

```text
[4,3,7,4]
```

Minimum value:

```text
min = 3
```

Length:

```text
4
```

Score:

```text
3 × 4 = 12
```

The maximum scoring subarray is:

```text
[3,7,4,5]
```

Minimum:

```text
3
```

Length:

```text
5
```

Score:

```text
3 × 5 = 15
```

### Approach

* Start with two pointers at `k`:

  * `left = k`
  * `right = k`

* Expand the window outward until the whole array is covered.

* Always expand towards the side with the larger adjacent value because it gives a better chance of maintaining a larger minimum.

* Track:

  * Current minimum value in the window.
  * Maximum score found.

Formula:

```text
score = minimum_value × window_length
```

### Complexity

Let `n` be the length of `nums`.

* Each pointer moves at most `n` times.

**Time Complexity:**

```text
O(n)
```

**Space Complexity:**

```text
O(1)
```

### Key Idea

The subarray must contain index `k`, so instead of checking all subarrays, expand from `k` and greedily choose the side with the larger value to maximize the possible minimum.

"""



from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
       left,right =k,k
       min_val=nums[k]
       max_score=min_val
       while left>0 or right<len(nums)-1:
              if left==0 or (right<len(nums)-1 and nums[right+1]>nums[left-1]):
                  right+=1
              else:
                  left-=1
              min_val=min(min_val,nums[left],nums[right])
              max_score=max(max_score,min_val*(right-left+1))
       return max_score
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 4, 3, 7, 4, 5], 3),   # Expected score would be based on the subarray [4, 3, 7]
        ([5, 5, 4, 5, 4, 1, 1, 1], 2), # Expected score would be based on the subarray [5, 5, 4]
        ([1, 2, 3, 4, 5], 2),      # Expected score would be based on the subarray [1, 2, 3]
        ([5, 4, 3, 2, 1], 1),      # Expected score would be based on the subarray [5, 4]
    ]
    
    # Test the maximumScore method with the test cases
    for nums, k in test_cases:
        result = solution.maximumScore(nums, k)
        print(f"The maximum score for nums={nums} with k={k} is {result}.")
