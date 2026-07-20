"""
Code
Testcase
Testcase
Test Result
187. Repeated DNA Sequences
Solved
Medium
Topics
Companies
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'."""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        list1 = set()
        list2 = set()
        l = len(s)
        if l<=10:
            return list(list1)
        for i in range(0, l-9):
            stri = s[i:i+10]
            if stri in list1 and stri not in list2:
                list2.add(stri)
            elif stri not in list1:
                list1.add(stri)
        return list(list2)

if __name__=="__main__":
   d=Solution()
   s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
   print(d.findRepeatedDnaSequences(s))

