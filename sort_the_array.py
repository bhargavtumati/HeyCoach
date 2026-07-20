"""
Sort the Array
You have to sort the string s in decreasing order based on the frequency of the characters. Return the sorted string. if frequency of two character are same then sort in alphabetical order.

Example 1
Input
s = "tree"
Output
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. "eetr" is not a valid answer as r appears before t.

Example 2
Input
 s = "cccaaa"
Output
"aaaccc"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is valid answer. Note that "cccaaa" is not a valid answer as both 'c' and 'a' appear three times but a comes before c in dictionary. Note that "cacaca" is incorrect, as the same characters must be together.

Example 3
Input
 s = "aA"
Output
"Aa"
Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""                




class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for c in s:
            hm[c] = hm.get(c, 0) + 1

        # Sort by frequency (descending) and then by character (ascending)
        sorted_items = sorted(hm.items(), key=lambda item: (-item[1], item[0]))

        k = ""
        for char, freq in sorted_items:
            k += char * freq

        return k

if __name__ == "__main__":
    f = Solution()
    s = "tree"
    print(f.frequencySort(s))
        
