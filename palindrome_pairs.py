"""
336. Palindrome Pairs
Solved
Hard
Topics
Companies
Hint
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a 
palindrome
.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.
"""

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         res = []
#         for i in range(len(words) - 1):
#             for j in range(i + 1, len(words)):
#                 s1 = words[i] + words[j]
#                 s2 = words[j] + words[i]
#                 # if s1 == s1[::-1]: res.append([i, j])
#                 # if s2 == s2[::-1]: res.append([j, i])
#                 if s1 == s1[::-1]: yield [i, j]
#                 if s2 == s2[::-1]: yield [j, i]
#         # return res

from itertools import chain
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        
        words = sorted(chain(                                        # list of (index, word, is_reversed), `word` can be either a orginal word or a reversed word
            ((i, w, False) for i, w in enumerate(words)),              # the list is sorted so that words with similar prefix are consecutive
            ((i, w[::-1], True) for i, w in enumerate(words))),
            key=lambda x: x[1])
                      
        for i, (idx1, w1, is_reversed1) in enumerate(words):         # Loop through each word
            for j in range(i + 1, len(words)):                     # Look at each word (w2) after the current word (w1) to find a prefix of the current word
                idx2, w2, is_reversed2 = words[j]                    # When w1 is a prefix of w2 then w1 + w2[::-1] is a palindrome            
                if w2.startswith(w1):                                   # Because the words are sorted, if w1 is a prefix of w2 then w1 will come before w2, so we only need to start from i + 1
                    if is_reversed1 == is_reversed2:                              # we want one of w1 and w2 is a reversed word
                        continue                                          # because if w1 is a prefix of w2 but both w1 and w2 are in the orginal words then w1 + w2[::-1] cannot be a palindrome
                    rest = w2[len(w1):]                                     # check idx1 != idx2 for cases where a word is a palindrome itself
                    if idx1 != idx2 and rest == rest[::-1]:                   # then check whether the postfix of w2 is a palindrome
                        res += [(idx1, idx2) if is_reversed2 else (idx2, idx1)]          # if w1 is an original word and w2 is a reversed word, then w1 + w2[::-1] is a palindrome => return (idx1, idx2)
                else:                                                             # otherwise w1 + w2[::-1] = w2 + w1[::] is a palindrome => return (idx2, idx1)   
                    break                                                 # because the words are sorted, so if we found a word that is not a prefix of the curent word
        return res                                                         # then every word after that can't be a prefix of the current word
if __name__=="__main__":
    words=["abcd","dcba","lls","s","sssll"]
    s=Solution()
    print(s.palindromePairs(words))

