"""
Roommate Agreement
Leonard was always sickened by how Sheldon considered himself better than him. To decide once and for all who is better among them, they decided to ask each other a puzzle. Sheldon pointed out that according to the Roommate Agreement, Sheldon will ask first. Leonard seeing an opportunity decided that the winner will get to rewrite the Roommate Agreement.

Sheldon thought for a moment then agreed to the terms thinking that Leonard would never be able to answer right. For Leonard, Sheldon thought of a puzzle which is as follows. He gave Leonard n numbers, which can be both positive and negative. Leonard had to find the number of continuous sequences of numbers such that their sum is zero.

For example, if the sequence is- 5, 2, -2, 5, -5, 9

There are 3 such sequences

2, -2

5, -5

2, -2, 5, -5

Since this is a golden opportunity for Leonard to rewrite the Roommate Agreement and get rid of Sheldon's ridiculous clauses, he can't afford to lose. So he turns to you for help. Don't let him down.
Input Format
First line contains T - number of test cases

Second line contains n - the number of elements in a particular test case.

Next line contains n elements, ai (1 <= i <= n) separated by spaces.

Output Format
The number of such sequences whose sum if zero.
Sample Input
2
4
0 1 -1 0
6
5 2 -2 5 -5 9

Sample Output
6
3
Constraints:
1 <= t <= 5

1 <= n <= 10^6

-10 <= ai <= 10

"""

class Solution:
    def calculate_sum_pairs_count(self, a: list) -> int:
        count = 0
        if 0 in a:
            count = -1
            for c in a:
                if c == 0:
                    count += 1
        Li = []
        def knapsack(i, j, a, path):
            nonlocal count
            if not a:
                if sum(path) == 0:
                    path.sort()
                    if path not in Li and len(path) > 0:
                        Li.append(path)
                        count += 1
                return
            knapsack(i, j, a[1:], path)
            knapsack(i, j, a[1:], path + [a[0]])
        knapsack(0, 0, a, [])
        return count

if __name__ == "__main__":
    a = [0, -1, 1, 0]
    s = Solution()
    print(s.calculate_sum_pairs_count(a))
