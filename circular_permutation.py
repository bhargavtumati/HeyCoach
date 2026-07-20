""" This code is the solution for:

* LeetCode 1238: Circular Permutation in Binary Representation

## Problem Statement

Given two integers `n` and `start`, return **any circular permutation** of the integers in the range `[0, 2ⁿ - 1]` such that:

1. The permutation starts with `start`.
2. Every integer from `0` to `2ⁿ - 1` appears exactly once.
3. The binary representations of every pair of adjacent integers differ by **exactly one bit**.
4. The binary representations of the **first and last** integers also differ by exactly one bit.

If there are multiple valid answers, return any of them.

---

### Example 1

**Input**

```text
n = 2
start = 3
```

**Output**

```text
[3,2,0,1]
```

**Explanation**

Binary representations:

```text
3 = 11
2 = 10   (1 bit differs)
0 = 00   (1 bit differs)
1 = 01   (1 bit differs)
3 = 11   (first and last differ by 1 bit)
```

---

### Example 2

**Input**

```text
n = 3
start = 2
```

**Output**

```text
[2,6,7,5,4,0,1,3]
```

---

### Constraints

```text
1 <= n <= 16
0 <= start < 2^n
```

---

### Idea Behind Your Code

Your code generates the **Gray code sequence**, where consecutive numbers differ by one bit:

For example:

```text
n = 1
0 1

n = 2
00 01 11 10

n = 3
000
001
011
010
110
111
101
100
```

It then **rotates** the Gray code sequence so that it starts with `start`, while preserving the property that adjacent elements (including the last and first) differ by exactly one bit. This is the standard approach for solving LeetCode 1238.
 """


from typing import List


class Solution:
    def circular_permutation(self, n: int, start: int) -> List[int]:
        # super brute force: DFS + backtracking
        # smarter: pattern

        # wlog we can make the permutation of 0..2^n-1 starting with zero, then cycle through to start at `start`

        # n = 1: 0, 1
        # n = 2: 00, 01, 11, 10
        # so take 0S_{n-1} and 1rev(S_{n-1}) (?)
        # because we know S_{n-1} has the right property, and same with rev(S_{n-1})
        # so S + rev(S) has that property, EXCEPT
        #   the outer two: same element
        #   and the inner two: same element
        #   so if we put a 1 in front of rev(S) then we're good

        if n == 1:
            if start == 0: return [0, 1]
            else: return [1, 0]

        S = [0, 1]
        for m in range(2, n+1):
            # existing S is S_{n-1}; we leave it as-is ("prepend 0")
            # then we append elements in reverse with a 1 in front, for m=2 we want to add 10 == 1 << (m-1)
            p = 1 << (m-1)
            S.extend(p + S[k] for k in range(len(S)-1, -1, -1))

        i = S.index(start)
        if i: return S[i:] + S[:i]
        else: return S

if __name__ =="__main__":
     cp=Solution()    
     n=2
     start=3
     print(cp.circular_permutation(n,start))