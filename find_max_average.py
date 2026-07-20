""" Problem Statement

Given an integer array nums and an integer k, find the contiguous subarray of length k that has the maximum average 
value and return that maximum average.

Example

Input:

nums = [1,12,-5,-6,50,3]
k = 4

Output:

12.75
Complexity

Your approach:

Time: O(n*k)

Sliding window approach:

Time: O(n)
Space: O(1)

The key idea is: instead of calculating every window sum again, remove the outgoing element and add the incoming element.
"""



from typing import List

class FindMaxAverage:
    def solution(self, nums: List[int], k: int) -> float:

        window_sum = sum(nums[:k])
        maximum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            maximum = max(maximum, window_sum)

        return maximum / k


if __name__ == "__main__":
    c = FindMaxAverage()

    nums = [5]
    k = 1

    print(c.solution(nums, k))

        
