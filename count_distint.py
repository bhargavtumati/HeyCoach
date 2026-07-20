"""
2261. K Divisible Elements Subarrays
Solved
Medium
Topics
Companies
Hint
Given an integer array nums and two integers k and p, return the number of distinct subarrays, which have at most k elements that are divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.

 

Example 1:

Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i], p <= 200
1 <= k <= nums.length
 

Follow up:

Can you solve this problem in O(n2) time complexity?

Hint 1
numerate all subarrays and find the ones that satisfy all the conditions.
Hint 2
Use any suitable method to hash the subarrays to avoid duplicates."""

from typing import List


class Solution:
    def count_distinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)                        
        sub_arrays = set()
        
		# generate all combinations of subarray
        for start in range(n):
            cnt = 0
            temp = ''
            for i in range(start, n):
                if nums[i]%p == 0:
                    cnt+=1                 
                temp+=str(nums[i]) + ',' # build the sequence subarray in CSV format          
                if cnt>k: # check for termination 
                    break
                sub_arrays.add(temp)                                    
                
        return len(sub_arrays)

if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,3,2,2]
    k = 2
    p = 2
    result = solution.countDistinct(nums, k, p)
    print(f"Number of distinct subarrays: {result}")

