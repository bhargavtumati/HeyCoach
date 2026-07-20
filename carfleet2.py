""" Problem Details
Problem Number: 1776
Title: Car Fleet II
Difficulty: Hard
Problem Summary

You are given an array:

cars = [[position1, speed1], [position2, speed2], ...]

where:

positioni is the initial position of the ith car.
speedi is its speed.

All cars move in the same direction.

When a faster car catches a slower car ahead, they collide and form a fleet that continues at the slower car's speed.

For each car, return the time at which it collides with the next car ahead. If it never collides, return -1.

Example

Input

cars = [[1,2],[2,1],[4,3],[7,2]]

Output

[1.0, -1.0, 3.0, -1.0]"""

from json import loads
from sys import stdin
from typing import List


class Solution:
    def get_collision_times(self, cars: List[List[int]]) -> List[float]:
        n=len(cars)
        answer=[-1.0]*n 
        car_stack=[]  
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            while car_stack and (cars[car_stack[-1]][1] >= speed or (cars[car_stack[-1]][0] - position)/(speed - cars[car_stack[-1]][1]) >= answer[car_stack[-1]] >= 0):
                car_stack.pop()
            if car_stack:
                answer[i] = (cars[car_stack[-1]][0] - position)/(speed - cars[car_stack[-1]][1])
            car_stack.append(i)
        return answer
"""
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().get_collision_times(nums)).replace(" ", ""), file=f)
exit(0)"""

if __name__=="__main__":
   cars=[[1,2],[2,1],[4,3],[7,2]]
   s=Solution()
   print(s.get_collision_times(cars))