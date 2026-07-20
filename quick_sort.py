# Quick Sort Algorithm Implementation in Python

def partition(arr, low, high):
  
    pivot = arr[high]    # Choose the pivot
    
    i = low - 1
    
    for j in range(low, high):    # Traverse arr[low..high] and move all smaller
        if arr[j] < pivot:     # elements on the left side. Elements from low to 
            i += 1                 # i are smaller after every iteration
            arr[i], arr[j] = arr[j], arr[i]
     
    arr[i + 1], arr[high] = arr[high], arr[i + 1]     # Move pivot after smaller elements 
    return i + 1                # and return its position

def quick_sort(arr, low, high):     # The QuickSort function implementation
    if low < high:
       
        pi = partition(arr, low, high)        # pi is the partition return index of pivot

        quick_sort(arr, low, pi - 1)         # Recursion calls for smaller elements and 
        quick_sort(arr, pi + 1, high)        # greater or equals elements

def print_array(arr):      # Function to print an array
    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":     # Driver code
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is")
    print_array(arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print_array(arr)