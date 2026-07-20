"""Palindromic binary representation
Given an integer A find the Ath number whose binary representation is a palindrome.

NOTE:

Consider the 1st number whose binary representation is palindrome as 1, instead of 0
Do not consider the leading zeros, while considering the binary representation.
Example 1
Input
A = 1
Output
1
Explanation
1st Number whose binary representation is palindrome is 1

Example 2:

Input:

9
Output:

27
Explanation
9th Number whose binary representation is palindrome is 27 (11011)

Constraints:
1 <= A <= 20000"""

class Solution:
    def solve(self, a):
      self.bina=0  #for debugging
      if a == 1:   # base condition the first no and second no is known so we return them directly
        return 1
      elif a == 2:
        return 3
      count = [2]
      res = [0]

      for bit in range(2, 31): #checking with each bit setting 0th bit to (31)th bit
        num = 0
        num |= (1 << bit)
        num |= 1
        self.bina=bin(num)[2:] #for debugging
        self.rec(num, bit - 1, 1, count, res, a) # solving for next numbers  by setting bits within index 1 and bit -1
        if count[0] == a:  #if we have already found the Ath no then return it
          
          return res[0]

      return -1

    def rec(self, num, r, l, count, res, a):  #recursively checks #If r (right bit position) is less than l (left bit position), it increments the count and checks if it has reached the desired a. If so, it updates res
        if r < l:  # base condition a unique no is generated after this condition is made in sequential order
            count[0] += 1
            if count[0] == a:
                res[0] = num
            return

        self.rec(num, r - 1, l + 1, count, res, a) # not setting anything and moving forward
        
        if count[0] == a:  #if we have already found the Ath no then return it
            return
        num |= (1 << r)  # setting rth bit 
        num |= (1 << l) # setting lth bit
        self.bina=bin(num)[2:]   #debug here
        self.rec(num, r - 1, l + 1, count, res, a) # solving after setting them
        num ^= (1 << r) # desetting rth
        num ^= (1 << l) # desetting lth


if __name__ == "__main__":
    a=20000
    #int(input())
    obj = Solution()
 
    result = obj.solve(a)
    print(result)
#A 1  2   3    4    5     6     7      8      9      10     11      12      13      14
#N 1, 3,  5,   7,   9,    15,   17,    21,    27,    31,    33,     45,     51,     63
#B 1, 11, 101, 111, 1001, 1111, 10001, 10101, 11011, 11111, 100001, 101101, 110011, 111111