"""### Problem Statement

Given a string `s`, find the **maximum product of lengths of two non-overlapping palindromic subsequences**.

A subsequence is created by deleting some characters without changing the order of the remaining characters.

The two palindromic subsequences:

* Must not share any character index.
* Their lengths are multiplied, and the maximum product is returned.

### Example

**Input:**

```text
s = "leetcodecom"
```

**Output:**

```text
9
```

### Explanation:

Two possible non-overlapping palindromic subsequences:

```text
"ete" → length 3
"cdc" → length 3
```

Product:

```text
3 × 3 = 9
```

### Approach

1. Use **bitmasking** to represent subsequences:

   * Each bit represents whether a character is selected.
   * Example:

   ```text
   mask = 1010
   ```

   selects characters at index `1` and `3`.

2. Generate all possible subsequences:

   * Check whether each subsequence is a palindrome.
   * Store:

   ```text
   bitmask → palindrome length
   ```

3. Compare every pair of palindromic subsequences:

   * If their bitmasks do not overlap:

   ```python
   mask1 & mask2 == 0
   ```

   they use different characters.

4. Calculate the maximum product.

### Complexity

Let `n` be the length of the string.

Number of possible subsequences:

```text
2^n
```

* Generating subsequences:

  * **Time:** `O(n × 2^n)`

* Comparing palindrome pairs:

  * **Time:** `O(4^n)` (worst case)

Overall:

* **Time Complexity:** `O(4^n)`
* **Space Complexity:** `O(2^n)`

### Key Idea

Bitmasking allows us to track which characters are used in each subsequence. Two subsequences are valid together only when their masks have no common bits:

```python
mask1 & mask2 == 0
```

meaning they do not share any character positions.
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali = len(s), {} # bitmask : length
        for mask in range(1, 1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]: # valid is palindromic
                pali[mask] = len(subseq)
        res = 0
        for mask1, length1 in pali.items():
            for mask2, length2 in pali.items():
                if mask1 & mask2 == 0: 
                    res = max(res, length1 * length2)
        return res
if __name__ =="__main__":
    s="leetcodecom"
    al=Solution()
    print(al.maxProduct(s))