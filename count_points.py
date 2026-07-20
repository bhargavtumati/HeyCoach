
"""Your code solves:

* LeetCode 2103: Rings and Rods

## Problem Statement

There are **10 rods** labeled from `0` to `9`.

You are given a string `rings` of even length, where every **two characters** represent one ring:

* The **first character** is the color of the ring:

  * `'R'` = Red
  * `'G'` = Green
  * `'B'` = Blue
* The **second character** is the rod number (`'0'` to `'9'`) on which the ring is placed.

Return the number of rods that have **all three colors** of rings on them.

---

### Example 1

**Input**

```text
rings = "B0B6G0R6R0R6G9"
```

**Output**

```text
1
```

**Explanation**

The rings are:

| Ring | Rod |
| ---- | --- |
| B    | 0   |
| B    | 6   |
| G    | 0   |
| R    | 6   |
| R    | 0   |
| R    | 6   |
| G    | 9   |

* Rod `0` has **B, G, R** ✅
* Rod `6` has **B, R**
* Rod `9` has **G**

Only **one rod** contains all three colors.

---

### Example 2

**Input**

```text
rings = "B0R0G0R9R0B0G0"
```

**Output**

```text
1
```

---

### Example 3

**Input**

```text
rings = "G4"
```

**Output**

```text
0
```

---

### Constraints

```text
1 <= rings.length <= 100
rings.length is even.
rings consists only of the characters 'R', 'G', 'B', and digits '0' through '9'.
```

---

### Function Signature

```python
def countPoints(rings: str) -> int:
```

Return the number of rods that have **at least one Red, one Green, and one Blue ring**.


"""


from collections import defaultdict

class count_points:
    def solution(self, s: str) -> int:
        ans = 0
        r = defaultdict(str)
        print(r)
        for rod in range(1,len(s),2):
            ring = rod-1
            r[s[rod]] += s[ring]
            print(r)

        for key in r:
            if len(set(r[key])) >= 3:
                ans +=1

        return ans

if __name__ =="__main__":
     cp=count_points()
     rings="B0B6G0R6R0R6G9"
     print(cp.solution(rings))
