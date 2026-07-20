"""### Problem Statement: Minimum White Tiles After Covering With Carpets

You are given a **floor** represented by a binary string `floor`.

* `'1'` represents a **white tile**.
* `'0'` represents a **black tile**.

You are also given:

* `numCarpets` → Number of carpets available.
* `carpetLen` → Length of each carpet.

Each carpet can cover **consecutive tiles** of length `carpetLen`.

Your task is to place the carpets on the floor such that the **number of visible white tiles is minimized**.

Return the minimum number of white tiles that remain uncovered.

---

### Example:

**Input:**

```python
floor = "10110101"
numCarpets = 2
carpetLen = 2
```

---

### Explanation:

Initial floor:

```
1 0 1 1 0 1 0 1
```

Two carpets of length 2 can cover:

```
Carpet 1 → positions 2 to 3
Carpet 2 → positions 5 to 6
```

After placing carpets:

```
1 0 [1 1] 0 [1 0] 1
```

Visible white tiles:

```
1 + 0 + 0 + 0 + 1 = 2
```

Minimum uncovered white tiles:

```
2
```

---

### Output:

```python
2
```

---

### Approach Used: Dynamic Programming + Prefix Sum

#### DP State:

```
dp[i][k]
```

represents:

> Maximum number of white tiles that can be covered starting from index `i` using `k` carpets.

---

### Choices at every position:

#### 1. Place a carpet

Cover tiles from:

```
i → i + carpetLen - 1
```

Gain the number of white tiles covered:

```
white tiles in this range
```

Then continue with:

```
solve(i + carpetLen, k-1)
```

---

#### 2. Do not place a carpet

Move to the next tile:

```
solve(i+1, k)
```

---

The answer is:

```
Total white tiles - Maximum white tiles covered
```

---

### Example calculation:

```
floor = "10110101"

Total white tiles = 5
```

Maximum covered white tiles:

```
3
```

Therefore:

```
5 - 3 = 2
```

---

### Complexity:

Let:

```
N = length of floor
K = number of carpets
```

Time Complexity:

```
O(N * K)
```

Space Complexity:

```
O(N * K)
```

(using memoization table)

---

This is a classic **LeetCode 2209 - Minimum White Tiles After Covering With Carpets** problem.
"""

class Solution:
    def min(self, a: int, b: int) -> int:
        return a if a < b else b

    def solve(self, floor: str, i: int, numCarpets: int, carpetLen: int, prefix: list) -> int:
        if i >= len(floor) or numCarpets == 0:
            return 0
        if dp[i][numCarpets] != -1:
            return dp[i][numCarpets]
        if floor[i] == '0':
             dp[i][numCarpets] = self.solve(floor, i + 1, numCarpets, carpetLen, prefix)
             return dp[i][numCarpets]
        x = self.min(i + carpetLen, len(floor)) - 1
        white = prefix[x]
        if i != 0:
            white -= prefix[i - 1]
        ans1 = white + self.solve(floor, i + carpetLen, numCarpets - 1, carpetLen, prefix)
        ans2 = self.solve(floor, i + 1, numCarpets, carpetLen, prefix)
        dp[i][numCarpets] = max(ans1, ans2)
        return dp[i][numCarpets]

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        global dp
        dp = [[-1] * (numCarpets + 1) for _ in range(len(floor))]
        prefix = [0] * len(floor)
        if floor[0] == '1':
            prefix[0] = 1
        else:
            prefix[0] = 0
        for i in range(1, len(floor)):
            prefix[i] = prefix[i - 1] + (floor[i] == '1')
        if prefix[len(floor) - 1] == 0:
            return 0
        return prefix[len(floor) - 1] - self.solve(floor, 0, numCarpets, carpetLen, prefix)
if __name__ == "__main__":
         floor = "10110101"
         numCarpets = 2
         carpetLen = 2

         sol = Solution()
         result = sol.minimumWhiteTiles(floor, numCarpets, carpetLen)
         print(f"Maximum white tiles uncovered: {result}")