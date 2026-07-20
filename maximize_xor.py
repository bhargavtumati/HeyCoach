"""
### Problem Statement

Given an array `nums` and an integer `maximumBit`, perform `n` queries.

For each query:

* Consider the XOR of the remaining elements in `nums`.
* Find a number `k` (`0 <= k < 2^maximumBit`) that maximizes:

```text
xor_of_remaining_elements XOR k
```

Return the answers for all queries in reverse order.

### Example

**Input:**

```text
nums = [0,1,1,3]
maximumBit = 2
```

**Output:**

```text
[0,3,2,3]
```

### Explanation:

Initial XOR:

```text
0 ^ 1 ^ 1 ^ 3 = 3
```

For `maximumBit = 2`, the maximum possible value is:

```text
(1 << 2) - 1 = 3
```

To maximize XOR:

```text
answer = current XOR ^ 3
```

Queries are processed by removing elements from the end.

### Approach

* Calculate the XOR of all numbers.
* The maximum `maximumBit` number is:

```python
(1 << maximumBit) - 1
```

* For each query:

  * XOR the current value with this maximum mask.
  * Store the result.
  * Remove the last element from `nums` using XOR.

* Return the results.

### Complexity

Let `n` be the size of `nums`.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` (for storing results)

### Key Idea

For a `maximumBit` of `b`, the number with all bits set:

```text
111...111  (b bits)
```

always gives the maximum XOR value, so:

```python
answer = xorSum ^ ((1 << maximumBit) - 1)
```

is used to maximize the result.
"""



from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xorSum = 0
        result = []
        
        # Calculate the cumulative XOR of all elements in nums
        for num in nums:
            xorSum ^= num  #same means zero, diff means max of diff.
        
        # Process queries in reverse order
        for _ in range(len(nums)):
            # Calculate the answer for the current query
            answer = xorSum ^ ((1 << maximumBit) - 1)   #or you can use 2** maximumBit
            result.append(answer)
            
            # Update xorSum by removing the last element
            xorSum ^= nums.pop() #pop removes element and xorSum XOR nums.pop() i.e 3 XOR 3 i.e 0
        
        # Reverse the result list
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0, 1, 1, 3]
    maximumBit1 = 2
    print(solution.maximizeXor(nums1, maximumBit1))  # Expected output: [0, 3, 2, 3]
"""
    nums2 = [2, 3, 4, 7]
    maximumBit2 = 3
    print(solution.maximizeXor(nums2, maximumBit2))  # Expected output: [5, 2, 6, 5]

    nums3 = [0, 1, 2, 2, 5, 7]
    maximumBit3 = 3
    print(solution.maximizeXor(nums3, maximumBit3))  # Expected output: [4, 3, 6, 4, 6, 7]
"""