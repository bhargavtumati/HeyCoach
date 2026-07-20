"""
Remove K digits
Given a non-negative integer represented as a string num and an integer k, remove k digits from the number so that the new number is the smallest possible. The remaining digits should maintain their original order in the string. Return the result as a string.

Input Format:

The first line contains the string num, representing the non-negative integer.
The second line contains the integer k.
Output Format:

Print the smallest possible integer as a string after removing k digits.
Sample Input 1:

1432219
3
Sample Output 1:

1219
Explanation:

Removing the digits 4, 3, and 2 from "1432219" leads to the new number "1219", which is the smallest possible result.

Sample Input 2:

10200
1
Sample Output 2:

200
Explanation:

Removing one digit (the leading 1) from "10200" results in "0200", and removing the leading zeroes gives "200" as the smallest possible result.

Constraints:
1<=k<= num.length<= 100000
num contains of only digits"""

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        stack = []
        for digit in s:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining k digits from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the result string
        result = ''.join(stack).lstrip('0')
        return result if result else "0"