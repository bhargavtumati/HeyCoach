#sort the array using merge sort algorithm

def merge_sort(arr):
    if len(arr) <= 1:   # base condition
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])     # recursion
    right = merge_sort(arr[mid:])     # recursion

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [12, 56, 78, 96, 81]
print(merge_sort(arr))