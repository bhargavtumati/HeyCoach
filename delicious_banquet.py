"""
Maximum Deliciousness
You're invited to a delicious banquet with n delectable dishes represented by their bitwise representation (numbers between 1 and 10^9). However, some dishes are hidden under silver cloches (k operations allowed). You can lift a cloche and double the bitwise representation of one hidden dish under it. Your goal is to maximize the overall "deliciousness" of the feast, measured by the bitwise OR of all dish values after lifting cloches.

Input:
n: Number of dishes (integers) - Integer between 1 and 10^5 (inclusive).
nums: Array of dish bitwise representations - Integers between 1 and 10^9 for each dish in the 0-based index of nums.
k: Number of cloches you can lift - Integer between 1 and 15 (inclusive).
Output:
max_deliciousness: The maximum possible bitwise OR of all dish values after lifting cloches at most k times.

Example 1:
Input:
n = 2, nums = [12, 9], k = 1

Output:
30 (Explanation: Lift the cloche on dish 1 to get [12, 18]. Then, max_deliciousness = 12 | 18 = 30)

Example 2:
Input:
n = 3, nums = [8, 1, 2], k = 2

Output:
35 (Explanation: Lift the cloche on dish 0 twice to get [32, 1, 2].
Then, max_deliciousness = 32 | 1 | 2 = 35).

Constraints:
n: Number of dishes (integers) must be an integer between 1 and 10^5 (inclusive).
nums: Array of dish bitwise representations must have a length equal to n. Each element in nums must be an integer between 1 and 10^9 (inclusive).
k: Number of cloches you can lift must be an integer between 1 and 15 (inclusive)."""

def prefix_or(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    prefix[1] = arr[0]
    for i in range(2, n + 1):
        prefix[i] = prefix[i - 1] | arr[i - 1]
    return prefix

def suffix_or(arr):
    n = len(arr)
    suffix = [0] * (n + 1)
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | arr[i]
    return suffix

def maximumDeliciousness(nums, k):
    n = len(nums)
    prefor = prefix_or(nums)
    suffor = suffix_or(nums)
    ans = 0
    for i in range(n):
        er = prefor[i] | suffor[i + 1]
        power = (2 ** k) * nums[i]
        tans = er | power
        ans = max(ans, tans)
    return ans


nums=[12, 9]
k=1
print(maximumDeliciousness(nums,k))