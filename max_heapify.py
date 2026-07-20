"""### Problem Statement

Given an array of `N` elements, convert the array into a **Max Heap**.

A Max Heap is a complete binary tree where:

* Every parent node is greater than or equal to its children.
* The largest element is always present at the root.

Return the array representation of the max heap.

### Example

**Input:**

```text id="8f3m1q"
arr = [5,3,2,1,6,7,8,9,4]
```

**Output:**

```text id="6m8h3s"
[9,6,8,5,3,7,2,1,4]
```

### Explanation:

Array representation of heap:

```text id="o4v1bw"
          9
        /   \
       6     8
      / \   / \
     5   3 7   2
    / \
   1   4
```

Every parent node is greater than its children.

### Approach

* Treat the array as a binary tree:

  * Left child index = `2*i + 1`
  * Right child index = `2*i + 2`
* Start from the last non-leaf node (`N/2 - 1`).
* Apply **heapify** from bottom to top.
* Swap the node with its largest child if the heap property is violated.
* Repeat until the whole array satisfies max heap property.

### Complexity

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(log N)` (recursion stack during heapify)

### Key Idea

Leaf nodes are already heaps, so we only need to heapify internal nodes from bottom to top. This builds the heap efficiently in linear time.
"""



class Solution:
    def buildHeap(self, arr, N):
        # Function to heapify a subtree rooted with node i which is an index in arr[]
        def heapify(arr, N, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # left = 2*i + 1
            right = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is greater than root
            if left < N and arr[i] < arr[left]:
                largest = left

            # See if right child of root exists and is greater than root
            if right < N and arr[largest] < arr[right]:
                largest = right

            # Change root, if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap

                # Heapify the root.
                heapify(arr, N, largest)

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            print(arr)
            heapify(arr, N, i)

        return arr

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 9
    arr = [5, 3, 2, 1, 6, 7, 8, 9, 4]
    max_heap = solution.buildHeap(arr, n)
    print("Max Heap:", max_heap)
