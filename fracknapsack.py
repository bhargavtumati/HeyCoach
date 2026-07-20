

"""
Fractional knapsack
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note: Unlike 0/1 knapsack, you are allowed to break the item.

Example 1
Input
N = 3, W = 50
values = [60,100,120]
weight = [10,20,30]
Output
240.00
Explanation:
Initial W = 50. take item 1 with weight 10 and value 60 so W is now 50 - 10 = 40. take item 2 with weight 20 and value 100 so W is now 40 - 20 = 20. Now, we cannot take item 3 completely so we will just take W = 20 amount of it and the value we will get out of it is 80 and W becomes 20 - 20 = 0. so total value is 60 + 100 + 80 = 240. So,Total maximum value of item we can have is 240.00 from the given capacity of sack.

Example 2
Input
N = 2, W = 50
values = [60,100]
weight = [10,20]
Output
160.00
Explanation:
Total maximum value of item we can have is 160.00 from the given capacity of sack.

Constraints:
1 <= Items.length <= 10000
1 <= Items.value , Items.weight <= 100000"""


class Solution:
    def fractional_knapsack(self, N, W, values, weight):
        ans = 0
        curval = 0

        def frac(N, W, values, weight, curval):
            nonlocal ans
            if N == 0 or W == 0 or not values or not weight:
                ans = max(ans, curval)
                return
            frac(N, W, values[1:], weight[1:], curval)

            if W >= weight[0]:
                curval += values[0]
                frac(N - 1, W - weight[0], values[1:], weight[1:], curval)
            else:
                fraction = min(1, W / weight[0])
                curval += fraction * values[0]
                frac(N - 1, 0, values[1:], weight[1:], curval)

            

        frac(N, W, values, weight, curval)
        return round(ans, 2)  # Round the result to two decimal places


"""class Solution:
    def fractional_knapsack(self, N, W, values, weight):
        # Create a list of tuples (value, weight, ratio)
        items = [(values[i], weight[i], round(values[i] / weight[i],2)) for i in range(N)]

        # Sort items based on the ratio in descending order
        items.sort(key=lambda x: x[2], reverse=True)

        total_value = 0
        remaining_capacity = W
        print(items)
        for value, item_weight, _ in items:
            if remaining_capacity >= item_weight:
                # Take the whole item
                total_value += value
                remaining_capacity -= item_weight
            else:
                # Take a fraction of the item
                fraction = remaining_capacity / item_weight
                total_value += fraction * value
                break

        return round(total_value, 2)  # Round the result to two decimal places
        """
# Example usage
solution = Solution()
values = [30, 40, 50, 60]
weights = [5, 10, 15, 20]
N = len(values)
W = 25
print("Maximum value that can be obtained:", solution.fractional_knapsack(N, W, values, weights))
