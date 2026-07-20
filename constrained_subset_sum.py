"""
1425. Constrained Subsequence Sum
Solved
Hard
Topics
Companies
Hint
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

Use dynamic programming.
Hint 2
Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.
Hint 3
dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])
Hint 4
Use a heap with the sliding window technique to optimize the dp.
"""


from typing import List


class Solution:
    def constrained_subset_sum(self, nums: List[int], k: int) -> int:
        deque=[]
        for i,num in enumerate(nums):
            while deque and deque[0]<i-k:
                deque.pop(0)
            if deque:
                nums[i]=nums[deque[0]]+num
            while deque and nums[deque[-1]]<nums[i]:
                deque.pop()
            if nums[i]>0:
                deque.append(i)
        return max(nums)                    

if __name__=="__main__":
    nums=[10,2,-10,5,20]
    k=2
    s=Solution()
    print(s.constrained_subset_sum(nums,k))

