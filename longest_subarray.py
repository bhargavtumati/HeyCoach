"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.


Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.



Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

Hint 1
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.
Hint 2
More specifically, use the two pointer technique, moving the right pointer as far as possible to the right until the subarray is not valid (maxValue - minValue > limit), then moving the left pointer until the subarray is valid again (maxValue - minValue <= limit). Keep repeating this process.
"""

import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = collections.deque() 
        incQ = collections.deque() 
        ans = 0
        left = 0

        for right, num in enumerate(nums):
            while decQ and num > decQ[-1]:
                decQ.pop()

            decQ.append(num)

            while incQ and num < incQ[-1]:
                incQ.pop()

            incQ.append(num)

            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()

                if incQ[0] == nums[left]:
                    incQ.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans
if __name__=="__main__":
    k=Solution()
    nums=[8,2,4,7]
    limit=4
    print(k.longestSubarray(nums,limit))    

