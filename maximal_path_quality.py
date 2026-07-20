"""
### Problem Statement

You are given an **undirected weighted graph** where:

* `values[i]` represents the value of node `i`.
* `edges[i] = [u, v, time]` represents a path between nodes `u` and `v` that takes `time`.
* You start at node `0` and must return to node `0` within `maxTime`.

Find the **maximum path quality**, which is the sum of values of all **unique nodes visited** during the path.

A node's value is counted only once even if it is visited multiple times.

### Example

**Input:**

```text
values = [5,10,15,20]

edges = [
 [0,1,10],
 [1,2,10],
 [0,3,10]
]

maxTime = 30
```

**Output:**

```text
50
```

### Explanation:

Possible path:

```text
0 → 1 → 2 → 1 → 0
```

Time:

```text
10 + 10 + 10 + 10 = 40
```

Exceeds maxTime, so invalid.

Valid path:

```text
0 → 1 → 0
```

Time:

```text
10 + 10 = 20
```

Values collected:

```text
5 + 10 = 15
```

Another valid path:

```text
0 → 3 → 0
```

Values:

```text
5 + 20 = 25
```

Maximum quality is the highest value collected while returning to node `0`.

### Approach

* Build an adjacency list for the graph.
* Use **BFS traversal** to explore possible paths.
* Store:

  * Current node
  * Time spent
  * Current collected value
  * Nodes already visited
* When reaching node `0`, update the maximum quality.
* Avoid unnecessary exploration using pruning:

  * Skip paths that already took more time and give less value than previously explored paths.

### Complexity

Let:

* `V` = number of nodes
* `E` = number of edges

Worst case:

* **Time Complexity:** `O(V!)` (all possible paths may be explored)
* **Space Complexity:** `O(V!)` (queue and visited path storage)

The pruning condition reduces the practical runtime significantly.

### Key Idea

The value of a node is counted only the **first time it is visited**, but the path must always end back at node `0` within the given time limit.
"""


import collections
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in edges :
            graph[u].append((v,t))
            graph[v].append((u,t))

        queue = collections.deque([(0, 0, values[0], [0])]) # (node, time, totalVal, path)
        valList = [(-1,-1)]*len(values)
        valList[0] = (values[0], 0)
        output = 0
        while queue :
            node, curTime, curVal, visited = queue.popleft()
            if node == 0 :
                output = max(output, curVal)
            for nxt, t in graph[node] :
                if curTime + t > maxTime :
                    continue
                nxtVal = curVal
                if nxt not in visited:
                    nxtVal += values[nxt]
                #This is the condition that significantly reduces the runtime
                if curTime+t >= valList[nxt][1] and nxtVal < valList[nxt][0] :
                    continue
                queue.append((nxt, curTime+t, nxtVal, visited + [nxt]))
                valList[nxt] = (nxtVal, curTime+t)
        return output

if __name__=="__main__":
    values=[5,10,15,20]
    edges=[[0,1,10],[1,2,10],[0,3,10]]
    maxTime=30
    s=Solution()
    print(s.maximalPathQuality(values,edges,maxTime))