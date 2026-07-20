"""
Code
Testcase
Test Result
Test Result
784. Letter Case Permutation
Solved
Medium
Topics
Companies
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        lnth=len(s)
        if lnth==1:
            return [s] if s.isnumeric() else [s.lower(),s.upper()]
        else:
            ans=[]
            for i in self.letterCasePermutation(s[1:]):
                if s[0].isnumeric():
                    ans.append(s[0]+i)
                else:
                    ans.extend([s[0].lower()+i,s[0].upper()+i])
                
            return ans
if __name__=="__main__":
       v=Solution()
       s="mQe"
       print(v.letterCasePermutation(s))

