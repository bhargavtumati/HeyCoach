"""
Count unique subsequences
Given a string s, your task is to calculate the number of distinct non-empty subsequences of s. Due to the potential size of the answer, return it modulo 1000000007 (1e9 + 7).

A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

Input Format:

A single line containing the string s.
Output Format:

An integer representing the number of distinct non-empty subsequences of smodulo1000000007.`
Sample Input 1:

abc
Sample Output 1:

7
Explanation:
The seven distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Sample Input 2:

aba
Sample Output 2:

6
Explanation:
The six distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters."""



class solution:
    def unique_subseq(self,s):
        li=[]

        def uniquelist(s,newword):
            if not s:
                if len(newword)==0:
                  li.append(newword)
                return
            uniquelist(s[1:],newword+s[0])
            uniquelist(s[1:],newword)
        uniquelist(s,"")
        return li
    
    
if __name__=="__main__":
    r=solution()
    s="abc"
    print(r.unique_subseq(s))

