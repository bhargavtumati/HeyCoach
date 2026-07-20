"""
Palindrome Op2
You are given a string s containing lowercase letters and an integer k.
You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

Example 1
Input
 s = "abc", k = 2
Output
1
Explanation:
You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2
Input
s = "aabbc", k = 3
Output
0
Explanation:
You can split the string into "aa", "bb" and "c", all of them are palindrome.

Constraints:
1 <= k <= s.length <= 100.
s only contains lowercase English letters."""

from cmath import inf
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def palindromePartition(self, s: str, k: int) -> int:

        n, ans = len(s), inf

        if n == k: return 0                         # <-- 1)

        if k == 1:                                  # <-- 2)
            return sum(s[i] != s[~i] for i in range(n//2))
    
        for i in range((n - k )+ 1):                      # <-- 3)
            sm = (self.palindromePartition(s[:i+1],     1) +
                  self.palindromePartition(s[i+1:], k - 1))

            if sm < ans: ans = sm                   # <-- 4)

        return ans 
    
if __name__=="__main__":
       s="abc"
       k=2
       f=Solution()
       print(f.palindromePartition(s,k))

"""
Here's the plan:

If the string is the length k, no are changes required, and we return 0.

If k == 1, we return the score of that string.

Other wise, we iteratively halve the string. We treat the left half as the left-most substring, 
and recurse the right half.

We determine the optimum answer from this iteration.

"""
