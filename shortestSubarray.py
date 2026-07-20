
"""
862. Shortest Subarray with Sum at Least K
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
"""


from cmath import inf
import collections
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        deque=collections.deque()
        preSum=[0]*n
        preSum[0]=nums[0]

        mini=float(inf)

        for i in range(1,n):
            preSum[i]=preSum[i-1]+nums[i]
        
        deque.append([0,-1])
        for i,num in enumerate(preSum):

            while deque and deque[-1][0]>=num:
                deque.pop()
            
            deque.append([num,i])

            while deque and deque[0][0] <= preSum[i]-k:
                mini=min(mini,i-deque[0][1])
                deque.popleft()

        
        return mini if mini!=float(inf) else -1

if __name__ == "__main__":

    nums=[1]
    k=1
    v=Solution()
    print(v.shortestSubarray(nums,k))


          