"""### Problem Statement

Given a positive integer `n`, determine whether it is a **happy number**.

A number is called **happy** if repeatedly replacing it with the **sum of the squares of its digits** eventually reaches `1`.

If the process enters a cycle and never reaches `1`, the number is not happy.

### Example

**Input:**

```text
n = 7
```

**Process:**

```text
7 → 7² = 49
49 → 4² + 9² = 97
97 → 9² + 7² = 130
130 → 1² + 3² + 0² = 10
10 → 1² + 0² = 1
```

**Output:**

```text
True
```

### Approach

* Calculate the sum of squares of digits repeatedly.
* Store previously seen numbers.
* If the value becomes `1`, return `True`.
* If a value repeats, a cycle exists, so return `False`.

### Complexity

* **Time Complexity:** `O(log n)` per iteration (number of digits processed)
* **Space Complexity:** `O(log n)` for storing visited numbers.

**Optimization:** Floyd's Cycle Detection algorithm can reduce space complexity to `O(1)`.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        new=[n]
        while True:
           sum=0
           while n>0:
              r=n%10
              n=int(n/10)
              sum+=r**2
           if sum==1:
              return True
           if sum not in new:
              new.append(sum)
           else:
              break
           n=sum
        return False

if __name__ == "__main__":
    n=7
    h=Solution()
    print(h.isHappy(n))  
