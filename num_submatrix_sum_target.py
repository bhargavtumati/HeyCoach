"""
1074. Number of Submatrices That Sum to Target
Solved
Hard
Topics
Companies
Hint
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i][j] <= 1000
-10^8 <= target <= 10^8
Hint 1
Using a 2D prefix sum, we can query the sum of any submatrix in O(1) time. Now for each (r1, r2), we can find the largest sum of a submatrix that uses every row in [r1, r2] in linear time using a sliding window.
"""

from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans=0
        for r in matrix:
            for i in range(1,len(r)):
                r[i]+=r[i-1]
        for start in range(m):
            for end in range(start,m):
                lookup=defaultdict(int)
                cumsum=0
                lookup[0]=1
                for k in range(n):
                    cumsum+=matrix[k][end] - (matrix[k][start-1] if start !=0 else 0)
                    if cumsum -target in lookup:
                        ans+=lookup[cumsum-target]
                    lookup[cumsum]+=1
        return ans                        

# Example usage
if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 1, 1],
        [1, -2, 1],
        [1, 1, 1]
    ]
    target = 0
    result = s.numSubmatrixSumTarget(matrix, target)
    print("Number of submatrices with sum equal to target:", result)
