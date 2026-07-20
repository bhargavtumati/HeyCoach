"""
Laser Maze
You're trapped in a high-tech laser grid maze. Each square in the maze contains a laser emitter or is empty. Laser emitters project beams horizontally or vertically across the grid, instantly deactivating any other emitters they encounter. Your goal is to escape the maze by deactivating the most laser emitters with a single well-placed shot from your own powerful laser cannon.

In other words You are given a 2D plane, we place n laser emitter at some integer coordinate points. Each coordinate point may have at most one laser emitter.A laser emitter can be removed if it shares either the same row or the same column as another laser emitter that has not been removed.

Given an array laser emitter of length n where grid[i] = [xi, yi] represents the location of the ith laser emitter, return the largest possible number of laser emitter that can be removed.

Input format:
A single line containing an integer N, the number of squares in which laser is there .
Following N lines, each containing two space-separated integers xi and yi, representing the coordinates of a laser emitter in the grid (0-based indexing).
A final line containing a single integer sx and sy, representing the starting coordinates of your laser cannon.
Output format:
A single integer representing the maximum number of laser emitters you can deactivate with one shot from your cannon.

Examples:
Example 1:

Input:
6
0 0
0 1
1 0
1 2
2 1
2 2

Output:
5

Explanation:
You can fire your cannon horizontally across row 2, deactivating emitters at (2,0), (2,1), and (2,2), then fire vertically down column 0, deactivating emitters at (0,0) and (1,0) for a total of 5 deactivated emitters.

Example 2:

Input:
5
0 0
0 2
1 1
2 0
2 2

Output:
3

Explanation:
You can fire your cannon horizontally across row 2, deactivating emitters at (2,0) and (2,2), then fire vertically down column 0, deactivating an emitter at (0,0) for a total of 3 deactivated emitters.

Constraints:
1 <= N <= 1000
0 <= xi, yi, sx, sy <= 10000
No two laser emitters occupy the same square.
Your starting position cannot be occupied by a laser emitter."""

class Solution:
    def LaserMaze():
        return            
if _name__=="__main__":
    n=9
    arr=[[] * n for i in range(n)]
    s=Solution()
    print(s.LaserMaze(n,arr))
