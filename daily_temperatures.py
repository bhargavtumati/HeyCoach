
"""
739.Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)  # Initialize the answer array with 0s
        stack = []  # Stack to keep indices of temperatures
        for i, temp in enumerate(temperatures):    #map index to temperatures
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
if __name__ == "__main__":
    # Example temperatures list
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the daily_temperatures method and print the result
    result = solution.daily_temperatures(temperatures)
    print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

    
