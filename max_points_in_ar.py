from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        # the idea is to recursively check 2^11 sets for including or excluding arrows
        # we keep track of the best score we have seen and return it at the end.

        results = []
        result_score = -1
        def dfs(partial: list[int], curr_ind, num_arrows, curr_score) -> None:
            nonlocal results
            nonlocal result_score
            nonlocal aliceArrows
            
            #backtracking
            if num_arrows < 0:
                return
            
            # base_case
            if curr_ind == 0:
                if curr_score < result_score:
                    return
                partial.append(num_arrows)
                results = list(reversed(partial))
                result_score = curr_score
                # every action must be undone on the partial
                # or subtle bugs can arise, this is required.
                partial.pop()
                return
            
            # recursive cases
            # include
            arrows_used = aliceArrows[curr_ind] + 1
            partial.append(arrows_used)
            dfs(partial, curr_ind - 1, num_arrows - arrows_used, curr_score + curr_ind)
            partial.pop()
           
            # exclude
            partial.append(0)
            dfs(partial, curr_ind - 1, num_arrows, curr_score)
            partial.pop()
        dfs([], 11, numArrows, 0)
        return results
if __name__ =="__main__":
   numArrows = 9
   aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
   al=Solution()
   print(al.maximumBobPoints(numArrows,aliceArrows))

"""2212. Maximum Points in an Archery Competition
Solved
Medium
Topics
Companies
Hint
Alice and Bob are opponents in an archery competition. The competition has set the following rules:

Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
The points are then calculated as follows:
The target has integer scoring sections ranging from 0 to 11 inclusive.
For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
However, if ak == bk == 0, then nobody takes k points.
For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.

You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.

Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.

If there are multiple ways for Bob to earn the maximum total points, return any one of them.

 

Example 1:


Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: [0,0,0,0,1,1,0,0,1,2,3,1]
Explanation: The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.
Example 2:


Input: numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
Output: [0,0,0,0,0,0,0,0,1,1,1,0]
Explanation: The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.
 

Constraints:

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows

Hint 1
To obtain points for some certain section x, what is the minimum number of arrows Bob must shoot?
Hint 2
Given the small number of sections, can we brute force which sections Bob wants to win?
Hint 3
For every set of sections Bob wants to win, check if we have the required amount of arrows. If we do, it is a valid selection.
"""