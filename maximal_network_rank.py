"""### Problem Statement

You are given `n` cities and a list of roads connecting them. The **network rank** of two different cities is the total number of roads connected to either city.

If there is a direct road between the two cities, it is counted only once.

Return the **maximum network rank** among any pair of cities.

### Example

**Input:**

```text
id="f8q8bf"
n = 4

roads = [
 [0,1],
 [0,3],
 [1,2],
 [1,3]
]
```

**Output:**

```text
id="lq6t1m"
5
```

### Explanation:

Connections:

```text
City 0 → 2 roads
City 1 → 3 roads
```

For cities `0` and `1`:

* Roads connected to city 0 = 2
* Roads connected to city 1 = 3
* Direct road between 0 and 1 exists, so subtract duplicate count once.

Network rank:

```text
2 + 3 - 1 = 4
```

Maximum pair gives the answer.

### Approach

* Build an adjacency matrix to check whether two cities have a direct road.
* Try every pair of cities.
* Count:

  * Roads connected to first city.
  * Roads connected to second city.
  * Add one extra check if both cities share a direct road.
* Keep the maximum rank.

### Complexity

Let `n` be the number of cities.

* **Time Complexity:** `O(n³)`
  (Checking every pair and scanning all cities)

* **Space Complexity:** `O(n²)`
  (Adjacency matrix)

### Key Idea

For two cities `i` and `j`:

```text
Network Rank = degree(i) + degree(j) - (1 if road exists between i and j else 0)
```

A more optimized approach stores the degree of each city and reduces the time complexity to `O(n²)`.
"""

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g=[[False]*n for _ in range(n)]
        for x,y in roads:
            g[x][y]=g[y][x]=True

        ans=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue

                cur=0
                for k in range(n):
                    if k!=i and k!=j:
                        if g[i][k]:
                            cur+=1

                        if g[j][k]:
                             cur+=1

                if g[i][j]:
                    cur+=1

                ans=max(cur,ans)

        return ans             
if __name__ == "__main__":
    s = Solution()
    n=4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    print(s.maximalNetworkRank(n,roads))