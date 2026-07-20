"""
Greedy Factory Owner
You are a greedy factory owner and it is the month end and you have to distribute salary to your workers. Each worker gets a minimum wage of ₹1,000 and based on their performance he gets some extra money. All the workers are standing in a line and every worker knows the performance value of the worker just adjacent to him. They will be mad if they get less or equal amount of money compared to the worker adjacent to him if he had less performance value than them (They don't care if they had equal amount of performance).

That's why if the worker has a higher performance than their adjacent peers then they will have to get at least ₹1,000 extra. For example: performance value of three workers is given as [9, 5, 4] then you would distribute salary as [3000, 2000, 1000].

Return the minimum amount of total wage that you can give to your workers without them getting mad.

Input Format:

First Line contains a single integer 'n' denoting the number of workers.

Second line contains 'n' space separated integers denoting the performance value of the ith worker.

Output format:

Return a single integer denoting the minimum amount of total wage that you can give to your workers without them getting mad.

Sample Input:

4

5 6 6 4

Sample Output:

6000

Explanation: You can distribute salary as follows [1000, 2000, 2000, 1000] which totals to 6000 and is the minimum answer possible.

Constraints:

1<=n<=10^4

1<=ar[i]<=100
"""


class Solution:
    def solve(self, n, ar):
        # Initialize salaries with minimum wage
        salaries = [1000] * n
        
        # Left to right pass
        for i in range(1, n):
            if ar[i] > ar[i - 1]:
                salaries[i] = salaries[i - 1] + 1000
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ar[i] > ar[i + 1]:
                salaries[i] = max(salaries[i], salaries[i + 1] + 1000)
        
        # Calculate the total wage
        total_wage = sum(salaries)
        return total_wage

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 4
    ar = [5, 6, 6, 4]
    print(solution.solve(n, ar))  # Output: 6000

    
