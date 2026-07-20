"""
Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note:
You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"

Output: 
2


Example 2:

Input: s = " 2-1 + 2 "
Output:
 3
Example 3:

Input:
s = "(1+(4+5+2)-3)+(6+8)"</br> 
Output:
  23
Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '. s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""




class calculate:
    def solution(self, s: str) -> int:
      #Write your code here

        stack, ans, num, sign = [], 0, 0, 1
        stack.append(sign)
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)    #if two three digits
            elif c == '(':
                stack.append(sign)    # separates for brackets
            elif c == ')':
                stack.pop()    #remove after bracket close
            elif c == '+' or c == '-':
                ans += sign * num       #updating answer
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0
        return ans + sign * num


if __name__ == "__main__":
    s = input("enter the string:")
    c = calculate()
    print(c.Solution(s))