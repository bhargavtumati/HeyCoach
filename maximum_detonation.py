"""
### Problem Statement

You are given a list of bombs where each bomb is represented as:

```text
[x, y, r]
```

* `(x, y)` → position of the bomb
* `r` → explosion radius

When a bomb explodes, it can trigger other bombs whose positions are within its radius.

Return the **maximum number of bombs that can be detonated** by choosing one bomb to start the chain reaction.

### Example

**Input:**

```text
bombs = [
 [1,2,3],
 [2,3,1],
 [3,4,2],
 [4,5,3],
 [5,6,4]
]
```

**Output:**

```text
5
```

### Explanation:

If bomb `0` is detonated:

```
Bomb 0 → Bomb 1 → Bomb 2 → Bomb 3 → Bomb 4
```

All bombs are triggered.

Maximum detonated bombs = `5`.

### Approach

1. Build a **directed graph**:

   * Each bomb is a node.
   * Add an edge `i → j` if bomb `i` can trigger bomb `j`.

2. For every bomb:

   * Run DFS to find all bombs reachable from it.
   * Count the number of detonated bombs.

3. Return the maximum count.

### Complexity

Let `n` be the number of bombs.

* Building graph:

  * **Time:** `O(n²)`

* DFS from each bomb:

  * **Time:** `O(n + e)`
    where `e` is the number of edges.

Overall:

* **Time Complexity:** `O(n × (n + e))`
  (Worst case `O(n³)`)

* **Space Complexity:** `O(n + e)`
  (Graph + DFS visited set)

### Key Idea

The explosion relationship is **directional**:

Example:

```
Bomb A radius reaches Bomb B
```

does not mean:

```
Bomb B radius reaches Bomb A
```

Therefore, the graph must be directed, and DFS is used to find the complete chain reaction.
"""

from math import sqrt
import collections
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj=collections.defaultdict(list)
        for i in range(len(bombs)):   # for each bomb no of bombs inside its radius creates a directed graph
            for j in range(i+1,len(bombs)):
                x1,y1,r1= bombs[i]
                x2,y2,r2= bombs[j]
                d=sqrt((x1-x2)**2+(y1-y2)**2)
                if d <=r1:
                    adj[i].append(j)
                if d <=r2:
                    adj[j].append(i)
        def dfs(i,visit):  #depth first search:creates a list of neighbours who are in range of their radii and dismisses the already added ones
            if i in visit:
                return 0
            visit.add(i)
            for nei in adj[i]:    # for each neighbour of ith defaultdict 
                dfs(nei,visit) 
            return len(visit)       # returns the length of maximum neighbours
        res=0
        for i in range(len(bombs)):
            res = max(res,dfs(i,set()))    # create new hashset everytime
            
        return res
    
if __name__ =="__main__":
    bombs=[[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    al=Solution()
    print(al.maximumDetonation(bombs))