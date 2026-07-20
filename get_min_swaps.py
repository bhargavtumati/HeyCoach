"""
### Problem Statement

Given a number represented as a string `num` and an integer `k`, find the **minimum number of adjacent swaps** needed to transform `num` into the **k-th smallest permutation** of the number.

A swap can only be performed between **adjacent digits**.

Return the minimum number of adjacent swaps required.

### Example

**Input:**

```text
num = "5489355142"
k = 4
```

**Output:**

```text
2
```

### Explanation:

The 4th next permutation of:

```text
5489355142
```

is:

```text
5489355421
```

Moving digits using adjacent swaps requires minimum swaps.

### Approach

1. Generate the `k`-th next permutation of the number.
2. Compare the original number and target permutation.
3. Count the minimum adjacent swaps required to transform the original arrangement into the target.

### Complexity

Let `n` be the length of the number.

* **Generating k permutations:** `O(k × n²)`
* **Counting swaps:** `O(n²)`
* **Space Complexity:** `O(n)`

This approach works when `k` and `n` are small. For larger constraints, a greedy + Fenwick Tree approach is used.
"""

class Solution:

    def next_permutation(self, num):
        """Generate next lexicographically greater permutation"""
        n = len(num)

        # Find first decreasing element from right
        i = n - 2
        while i >= 0 and num[i] >= num[i + 1]:
            i -= 1

        # Find element just greater than num[i]
        j = n - 1
        while num[j] <= num[i]:
            j -= 1

        # Swap
        num[i], num[j] = num[j], num[i]

        # Reverse suffix
        num[i + 1:] = reversed(num[i + 1:])


    def count_swaps(self, original, target):
        """Count minimum adjacent swaps to convert original into target"""
        swaps = 0
        original = list(original)

        for i in range(len(target)):
            if original[i] == target[i]:
                continue

            j = i + 1
            while original[j] != target[i]:
                j += 1

            while j > i:
                original[j], original[j - 1] = original[j - 1], original[j]
                swaps += 1
                j -= 1

        return swaps


    def get_min_swaps(self, num: str, k: int) -> int:
        target = list(num)

        for _ in range(k):
            self.next_permutation(target)

        return self.count_swaps(num, target)


if __name__ == "__main__":
    num = "5489355142"
    k = 4

    solution = Solution()
    print(solution.get_min_swaps(num, k))