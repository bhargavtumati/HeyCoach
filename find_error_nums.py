"""write a python program to find the duplicate and missing number in an array of integers from 1 to n. 
 The array contains n integers where one integer is duplicated and one integer is missing. 
 The function should return a list containing the duplicate number and the missing number.
"""

from typing import List
class find_error_nums:
    def solution(self, nums: List[int]) -> List[int]:
          nums.sort()
    
          num2=[]
          for i in range(len(nums)):
            if nums[i]!=i+1:
              num2=[nums[i],i+1]
              break
              
          return num2 

if __name__ == "__main__":
    image = [1,1]
    fm = find_error_nums()
    print(fm.solution(image))