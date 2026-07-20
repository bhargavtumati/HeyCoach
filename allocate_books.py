"""
Book Allocation


You are given an array `arr[]` of size `N`, where `arr[i]` represents the number of pages in the `i`th book. There are `M` students, and the books must be allocated according to the following rules:

1. Each student must receive at least one book.
2. Each book must be allocated to exactly one student.
3. Books assigned to a student must be **contiguous** (consecutive books in the array).
4. The goal is to **minimize the maximum number of pages assigned to any student**.

Return the minimum possible value of the maximum pages assigned to a student. If it is not possible to allocate the books (i.e., `M > N`), return `-1`.

### Example 1

**Input:**

```text
N = 4
M = 2
arr = [12, 34, 67, 90]
```

**Output:**

```text
113
```

**Explanation:**

One optimal allocation is:

* Student 1 → `[12, 34, 67]` = 113 pages
* Student 2 → `[90]` = 90 pages

The maximum pages assigned to a student is `113`, which is the minimum possible.

---

### Example 2

**Input:**

```text
N = 3
M = 4
arr = [10, 20, 30]
```

**Output:**

```text
-1
```

**Explanation:**

There are more students than books, so it is impossible to give at least one book to every student.

---

### Constraints

```text
1 ≤ N ≤ 10^5
1 ≤ M ≤ 10^5
1 ≤ arr[i] ≤ 10^6
```

The expected time complexity is **O(N log(sum(arr)))**, which is achieved using **binary search on the answer** combined with a greedy feasibility check (`is_possible`).
"""

class Solution:
    def is_possible(self, arr, n, m, curr_min):
        students_required = 1
        curr_sum = 0

        # Iterate over all books
        for i in range(n):
            # Check if current number of pages is greater than curr_min
            # If so, we won't be able to allocate properly
            if arr[i] > curr_min:
                return False

            # Count how many students are required to distribute curr_min pages
            if curr_sum + arr[i] > curr_min:
                # Increment student count
                students_required += 1
                # Update curr_sum
                curr_sum = arr[i]
                # If students required becomes greater than given no. of students, return False
                if students_required > m:
                    return False
            else:
                # Else update curr_sum
                curr_sum += arr[i]

        return True

    def find_pages(self, arr, n, m):
        total_pages = sum(arr)

        # Return -1 if no. of books is less than no. of students
        if n < m:
            return -1

        # Initialize start as 0 pages and end as total pages
        start, end = 0, total_pages
        result = float('inf')

        # Traverse until start <= end
        while start <= end:
            mid = (start + end) // 2
            if self.is_possible(arr, n, m, mid):
                # Update result to current distribution (best found so far)
                result = mid
                # As we are finding the minimum and books are sorted,
                # reduce end = mid - 1
                end = mid - 1
            else:
                # If not possible, increase pages, so update start = mid + 1
                start = mid + 1

        # Return the minimum number of pages
        return result

# Example usage
N = 15
M = 4
book_pages = [3, 2, 6, 4, 8, 5, 9, 1, 7, 10, 11, 14, 13, 12, 15]

solution = Solution()
minimum_pages = solution.find_pages(book_pages, N, M)
print(f"Minimum pages needed for allocation: {minimum_pages}")
