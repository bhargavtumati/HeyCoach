"""
Letter Tile Possibilities
Solved
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res=set()
        def dfs(path,tiles):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                dfs(path+tiles[i],tiles[:i]+tiles[i+1:])
            if not tiles:
                return
        dfs("",tiles)
        return len(res)
if __name__=="__main__":
       s="ABB"
       d=Solution()
       print(d.numTilePossibilities(s))

