"""### Problem Statement: Number of Substrings Containing All Three Characters

Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`, return the **number of substrings that contain at least one occurrence of all three characters**.

A substring is a contiguous sequence of characters.

---

### Example 1:

**Input:**

```python
s = "abcabc"
```

**Output:**

```python
10
```

---

### Explanation:

All substrings containing at least one `a`, `b`, and `c` are:

```
abc
abca
abcab
abcabc
bca
bcab
bcabc
cab
cabc
abc
```

Total:

```
10
```

---

### Example 2:

**Input:**

```python
s = "aaacb"
```

**Output:**

```python
3
```

**Explanation:**

Valid substrings:

```
aaacb
aacb
acb
```

All contain:

```
a + b + c
```

Answer:

```
3
```

---

## Approach: Sliding Window

Maintain a window using two pointers:

* `left` → starting point of window
* `right` → ending point of window

Track the count of:

```
a, b, c
```

When the current window contains all three characters:

```
a > 0, b > 0, c > 0
```

move `left` forward while maintaining the condition.

For every `right`, the number of valid substrings ending at `right` is:

```
left
```

Add it to the answer.

---

### Example:

```
s = abcabc
```

At index `2`:

```
window = abc
```

Valid substrings ending at index 2:

```
abc
```

Count = 1

At index `3`:

```
window = abca
```

Valid substrings:

```
abc
abca
```

Count increases.

Final answer:

```
10
```

---

### Complexity:

Let `N` be the length of the string.

Time Complexity:

```
O(N)
```

Each character is processed at most twice.

Space Complexity:

```
O(1)
```

Only three character counts are stored.

---

This is the classic **LeetCode 1358 - Number of Substrings Containing All Three Characters** problem.
"""

class numberOfSubstrings:
    def Solution(self, s: str) -> int:
        n = len(s)
        char_count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        count = 0

        for right in range(n):
            char_count[s[right]] += 1

            # Slide the window to the right
            while all(char_count.values()):
                char_count[s[left]] -= 1
                left += 1

            # Update the count
            count += left

        return count

# Example usage:
noss = numberOfSubstrings()
print(noss.Solution("abcabc"))  # Output: 10
