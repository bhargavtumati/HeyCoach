#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def addsum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(addsum([2, 7, 11, 15], 9))