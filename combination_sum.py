"""
Combination sum
You have given an array arr consisting of N distinct integers and an integer target. Return a list of all unique combinations of numbers where the chosen numbers sum to target. The same number may be chosen from arr an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. Note :

Elements in each combination should be in non-decreasing order The combinations themselves must also be sorted in lexographically increasing order

Example 1:
Input :
arr = [2,3,6,7], target = 7

Output
[[2,2,3],[7]]

Explanation :
Above are all the unique combinations of numbers in array which sums up to target 7 and are in lexographically increasing order. Note:Here, [2,2,3] and [2,3,2] are different permutation of same combinations which sums up to 7. So you should output only one of this combination i.e.[2,2,3] as it is in non-decreasing order.

Constraints:
1 <= N <= 20  
2 <= arr[i] <= 30  
All elements are distinct  
1 <= target <= 100
Input format
first line contains two integers n(size of array ) and target
next line represents the elements of array separted by space.
Output format
k lines where each line reprsents an array"""


def find_numbers(ar, sum, res, r, i):
    if sum == 0:
        res.append(r[:])    #result gets appended when sum equals zero
        return
    while i < len(ar) and sum - ar[i] >= 0:
        r.append(ar[i])    #appends ith of arr
        find_numbers(ar, sum - ar[i], res, r, i)   #recursively calls
        i += 1
        r.pop()

def combination_sum(ar, sum):
    ar.sort()
    ar = list(set(ar))  # Remove duplicates
    r = []
    res = []
    find_numbers(ar, sum, res, r, 0)
    return res

# Example usage
ar = [2, 4, 6, 8]
target_sum = 8
result = combination_sum(ar, target_sum)

if not result:
    print("Empty")
else:
    for comb in result:
        print(comb)

