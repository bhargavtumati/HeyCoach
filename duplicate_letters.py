"""
Duplicate Letters
Dholu is very creative and wants to play with strings and he has a very good idea. You have given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order

Input Format:
first line consists of a string
Output Format:
print the output string
Sample Input:
cbacdcbc

Sample Output:
abcd

Explanation: Since if we only collect unique letters, they come out to be 'c', 'b', 'a' and 'd' and when they are arranged lexicographically the output is abcd.

Constraints:
1<= s.length<= 10000
Note: Input consists of only lower case letters.

"""
def find_unique(s):
    v=set()
    j=""
    for c in s:
        v.update((c,))
    li=[]
    for c in v:
        li.append(c)
    li.sort()
    for c in li:
         j+=c
    return j

s="cbacdcbc"

print(find_unique(s))