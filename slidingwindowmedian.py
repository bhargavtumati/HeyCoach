"""
480. Sliding Window Median
Solved
Hard
Topics
Companies
Hint
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

Hint 1
The simplest of solutions comes from the basic idea of finding the median given a set of numbers. We know that by definition, a median is the center element (or an average of the two center elements). Given an unsorted list of numbers, how do we find the median element? If you know the answer to this question, can we extend this idea to every sliding window that we come across in the array?
Hint 2
Is there a better way to do what we are doing in the above hint? Don't you think there is duplication of calculation being done there? Is there some sort of optimization that we can do to achieve the same result? This approach is merely a modification of the basic approach except that it simply reduces duplication of calculations once done.
Hint 3
The third line of thought is also based on this same idea but achieving the result in a different way. We obviously need the window to be sorted for us to be able to find the median. Is there a data-structure out there that we can use (in one or more quantities) to obtain the median element extremely fast, say O(1) time while having the ability to perform the other operations fairly efficiently as well?
"""


from heapq import heappop, heappush, heappushpop
from itertools import pairwise
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        if k == 2:
            return [(p + q) / 2 for p,q in pairwise(nums)]
        kodd = k % 2
        ref = sorted(nums[:k])
        hl = [-x for x in ref[:k//2]]
        hl.reverse()
        hr = ref[k//2:]
        if kodd:
            out = [hr[0]]
        else:
            out = [(hr[0] - hl[0]) / 2]
        hrd = []
        hld = []
        def cleanr():
            while hrd and hrd[0] == hr[0]:
                heappop(hrd)
                heappop(hr)
        def cleanl():
            while hld and hld[0] == hl[0]:
                heappop(hld)
                heappop(hl)
        for idx,x in enumerate(nums[k:]):
            y = nums[idx]
            mid = hr[0]
            if y >= mid:
                if x < mid:
                    x = -heappushpop(hl, -x)
                    cleanl()
                heappush(hr, x)
                heappush(hrd, y)
                cleanr()
            else:
                if x >= mid:
                    x = heappushpop(hr, x)
                    cleanr()
                heappush(hl, -x)
                heappush(hld, -y)
                cleanl()
            if kodd:
                out.append(hr[0])
            else:
                out.append((hr[0] - hl[0]) / 2)
        return out
    
if __name__ == "__main__":
    f = Solution()
    nums=[1,3,-1,-3,5,3,6,7]
    k=3
    print(f.medianSlidingWindow(nums,k))

