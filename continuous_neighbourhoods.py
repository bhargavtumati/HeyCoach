"""Continuous Neighborhoods
You're the architect of Harmony Hills, a quaint utopia where neighbors strive for peaceful coexistence. Each resident is represented by a number (in nums) reflecting their desired level of social interaction (the larger the number, the more social). Your goal? Build vibrant communities within this diverse population by grouping residents into "continuous" neighborhoods where everyone feels comfortable.

You're given an array nums representing the social preferences of Harmony Hills residents (positive integers between 1 and 10^9).
A "continuous" neighborhood is a group of residents where the difference in desired social interaction between any two residents is at most 2 (i.e., |resident1 preference - resident2 preference| <= 2). Your mission is to find the total number of possible continuous neighborhoods you can create within Harmony Hills. Remember, the more harmonious neighborhoods, the happier the residents!

Input/Output Format:
Input:
An array nums containing the social preferences of residents separated by spaces or commas.

Output:
Return a single integer representing the total number of possible continuous neighborhoods in Harmony Hills.

Examples:
Input:
5 4 2 4 (Resident preferences in Harmony Hills)
Output:
8 (As in the original example, there are 8 possible neighborhoods catering to everyone's social needs.)

Input:
1 2 3 (Another peaceful community)
Output:
6 (Similar to the first example, 6 neighborhoods can be formed to ensure everyone feels comfortable.)
Constraints:
1 <= n <= 10^5 (Number of residents in Harmony Hills)
1 <= nums[i] <= 10^9 (Individual resident's social preference)"""


from itertools import permutations
class Solution:
    def confi(self,nums)->int:
      hm={}
      co=0
      for c in nums:
        hm[c]=hm.get(c,0)+1
        if hm[c]>1:
          co+=2
      return co
    def ifconti(self,nums)->bool:
      for i in range(len(nums)-1):
        if abs(nums[i]-nums[i+1])>2:
          return False
      return True
    def continuous_neighbourhoods(self, nums):
       count=0
       for perm in set(list(permutations(nums))):
         if self.ifconti(perm):
           count+=1
       return count+self.confi(nums)
    
if __name__=="__main__":
  n=10
  Li=[14,4,14,7,1,1,5,9,3,10]
  s=Solution()
  print(s.continuous_neighbourhoods(Li))

