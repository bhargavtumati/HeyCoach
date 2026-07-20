"""
Scramble String Generator
Description:

You are tasked with writing a program to generate all possible scrambled versions of a given word. A scrambled version of a word is any permutation of its letters. Your program should remove duplicate permutations and return the unique permutations in lexicographical order.

Input:

The input consists of a single line containing a string word consisting of lowercase English letters. The length of word will not exceed 7 characters.

Output:

Your program should print all unique scrambled versions of the input word in lexicographical order. Each permutation should be separated by a comma and a space.

Example 1:

Input:

s = "cat"
Output:

All possible scrambled words:
act, atc, cat, cta, tac, tca
Example 2:

Input:

s = "aab"
Output:

aab, aba, baa
Constraints:
The input string s has a length between 1 and 7.
The string s consists of lowercase English letters."""

def findPermutations(word,string,vis,ans):
    if len(word)==len(string):
        ans.add(word)
        return
    for i in range(len(string)):
        if not vis[i]:
            vis[i]=1
            word+=string[i]
            findPermutations(word,string,vis,ans)
            word=word[:len(word)-1]
            vis[i]=0
    

string = list("ABC") 
vis=[0] * len(string)
ans=set()
word=""
findPermutations(word,string, vis,ans) 
print(ans)