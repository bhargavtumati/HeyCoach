"""### Problem Statement

Given `n` people and a list of pairs representing **dislikes**, determine whether it is possible to split all people into **two groups** such that no two people who dislike each other are in the same group.

Return `True` if such a partition is possible, otherwise return `False`.

### Example

**Input:**

```text
n = 4

dislikes = [
 [1,2],
 [1,3],
 [2,4]
]
```

**Output:**

```text
True
```

### Explanation:

Possible grouping:

```text
Group 1: [1,4]
Group 2: [2,3]
```

No pair of people who dislike each other appears in the same group.

### Approach

* Represent people and dislikes as an **undirected graph**.
* Use **BFS graph coloring**:

  * Assign one color to a person.
  * Assign the opposite color to all their neighbors.
  * If two connected people have the same color, bipartition is impossible.
* Check all components because the graph may be disconnected.

### Complexity

Let:

* `V` = number of people
* `E` = number of dislike relationships

**Time Complexity:** `O(V + E)`
**Space Complexity:** `O(V + E)`

### Key Idea

A graph can be divided into two groups **if and only if it is bipartite**, meaning it can be colored using exactly two colors without adjacent vertices having the same color.
"""



from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=[[] for _ in range(n+1)]
        for did in dislikes:
            graph[did[0]].append(did[1])
            graph[did[1]].append(did[0])
        colour=[-1]*(n+1)
        def bfs(graph,colour,queue):
          
            colour[queue[0]]=0
            while queue:
                
                for neigh in graph[queue[0]]:
                    if colour[queue[0]]==colour[neigh]:
                        return False
                    elif colour[neigh]==-1:
                        colour[neigh]=1-colour[queue[0]]
                        queue.append(neigh)
                    

                del(queue[0])
            return True
 
        for i in range(1,n+1):
          if colour[i]==-1:

              if not bfs(graph,colour,[i]):
                  return False
            
        return True
    
