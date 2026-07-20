"""Your code solves:

* LeetCode 1638: Count Substrings That Differ by One Character

## Problem Statement

Given two strings `s` and `t`, return the number of pairs of **non-empty substrings** from `s` and `t` that differ by **exactly one character**.

A substring is a contiguous sequence of characters within a string.

Two substrings differ by exactly one character if:

* They have the same length.
* They differ at exactly one position.

---

### Example 1

**Input**

```text
s = "aba"
t = "baba"
```

**Output**

```text
6
```

**Explanation**

The valid pairs are:

* ("a", "b")
* ("ab", "bb")
* ("ba", "aa")
* ("b", "a")
* ("aba", "bba")
* ("aba", "bab")

Each pair differs by exactly one character.

---

### Example 2

**Input**

```text
s = "ab"
t = "bb"
```

**Output**

```text
3
```

**Explanation**

The valid pairs are:

* ("a", "b")
* ("ab", "bb")
* ("b", "bb")

---

### Example 3

**Input**

```text
s = "a"
t = "a"
```

**Output**

```text
0
```

**Explanation**

The only possible pair is `("a", "a")`, which differs by **zero** characters, so the answer is `0`.

---

### Constraints

```text
1 <= s.length <= 100
1 <= t.length <= 100
s and t consist of lowercase English letters.
```

---

### Function Signature

```python
def countSubstrings(s: str, t: str) -> int:
```

Return the number of pairs of non-empty substrings from `s` and `t` that differ by exactly one character.
"""


class Solution:
    def count_substrings(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                p = i
                l = j
                c = 0
                while p < n and l < m:
                    if s[p] != t[l]:
                        c+=1
                        if c > 1:
                            break
                    ans += c
                    l += 1
                    p += 1
        return ans
if __name__=="__main__":
    h=Solution()
    s="aba"
    t="baba"
    # s=input("enter s: ")
    # t=input("enter t: ")
    print(h.count_substrings(s,t))