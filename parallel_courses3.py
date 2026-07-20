"""### Problem Statement: Minimum Time to Complete All Courses

You are given `n` courses labeled from `1` to `n`.

Each course requires a certain amount of time to complete, given by the array `time`, where:

* `time[i]` is the time required to complete course `i + 1`.

You are also given prerequisite relationships in the form:

```
relations[i] = [a, b]
```

which means:

* Course `a` must be completed **before** course `b` can be started.

Multiple courses can be taken **simultaneously** if their prerequisites are satisfied.

Return the **minimum number of months required to complete all courses**.

---

### Example:

**Input:**

```python
n = 3

relations = [
    [1,3],
    [2,3]
]

time = [3,2,5]
```

---

### Explanation:

Courses:

```
Course 1 → takes 3 months
Course 2 → takes 2 months
Course 3 → takes 5 months
```

Dependencies:

```
1 → 3
2 → 3
```

Execution:

Month timeline:

```
Course 1:  [1 2 3]
Course 2:  [1 2]
Course 3:        [4 5 6 7 8]
```

Courses 1 and 2 can be completed together.

After both finish:

```
max(3,2) = 3 months
```

Then course 3 takes:

```
5 months
```

Total time:

```
3 + 5 = 8 months
```

---

### Output:

```python
8
```

---

### Approach Used: DFS + Memoization (Topological DP)

The graph represents:

```
Prerequisite → Course
```

Example:

```
1 → 3
2 → 3
```

Adjacency list:

```
1: [3]
2: [3]
3: []
```

For each course:

```
Time required =
course duration + maximum time of dependent courses
```

Formula:

```
dfs(course) = time[course] + max(dfs(next courses))
```

The answer is:

```
maximum time among all courses
```

because courses can run in parallel.

---

### Complexity:

Let:

* `N` = number of courses
* `E` = number of relations

Time Complexity:

```
O(N + E)
```

Each course and relation is visited once.

Space Complexity:

```
O(N + E)
```

For adjacency list and memoization.

---

This is the classic **LeetCode 2050 - Parallel Courses III** problem.
"""


from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # result = 0
        # start = [0] * n
        # parents = [0] * n
        children = [[] for _ in range(n)]

        for a, b in relations:
            a -= 1
            b -= 1
            # parents[b] += 1
            children[a].append(b)

        cache = [None] * n

        def dfs(node):
            if cache[node] is not None:
                return cache[node]

            res = time[node]

            child_max = 0
            for child in children[node]:
                child_time = dfs(child)
                if child_time > child_max:
                    child_max = child_time

            res += child_max

            cache[node] = res
            return res

        return max(dfs(i) for i in range(n))

        # stack = [i for i, val in enumerate(parents) if val == 0]

        # while stack:
        #     node = stack.pop()
        #     end = start[node] + time[node]
        #     if end > result:
        #         result = end

        #     for child in children[node]:
        #         if start[child] < end:
        #             start[child] = end
        #         parents[child] -= 1
        #         if parents[child] == 0:
        #             stack.append(child)

        # return result

if __name__=="__main__":
    n =3
    relations =[[1,3],[2,3]]
    time =[3,2,5]
    s=Solution()
    print(s.minimumTime(n,relations,time))