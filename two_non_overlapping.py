"""Your code is solving the **"Maximum Sum of Two Non-Overlapping Events"** problem.

### Problem Statement

You are given a list of events where:

```
events[i] = [startTime, endTime, value]
```

Each event has:

* `startTime` → when the event begins
* `endTime` → when the event ends
* `value` → reward/value obtained by attending the event

You can attend **at most two events** such that they **do not overlap**.

Return the **maximum total value** you can get by attending at most two events.

Two events do not overlap if:

```
first event endTime < second event startTime
```

### Example

**Input:**

```python
events = [
    [1,5,3],
    [1,5,1],
    [6,6,5]
]
```

**Explanation:**

Events:

| Event | Start | End | Value |
| ----- | ----- | --- | ----- |
| 1     | 1     | 5   | 3     |
| 2     | 1     | 5   | 1     |
| 3     | 6     | 6   | 5     |

Choose:

* Event 1: value = 3
* Event 3: value = 5

They don't overlap because:

```
5 < 6
```

Total:

```
3 + 5 = 8
```

**Output:**

```
8
```

### Approach Used

Your solution uses:

1. Sort events by start time.
2. Sort events by end time.
3. Keep track of the maximum value among events that have already ended.
4. For every current event, combine it with the best previous non-overlapping event.

### Time Complexity

Sorting:

```
O(N log N)
```

Loop:

```
O(N)
```

Overall:

```
O(N log N)
```

### Space Complexity

```
O(N)
```

because of the sorted lists.
"""


from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        mx, ans = 0, 0

        beg, end, val = zip(*events)
        beg2ndMtg = sorted(zip(beg, val))
        end1stMtg = iter(sorted(zip(end, val)))

        end1st, val1st = next(end1stMtg)

        for beg2nd, val2nd in beg2ndMtg:

            while end1st < beg2nd:
                mx = max(mx, val1st)
                end1st, val1st = next(end1stMtg)

            ans = max(ans, mx + val2nd)

        return ans  
if __name__=="__main__":
    events=[[1,5,3],[1,5,1],[6,6,5]]
    s=Solution()
    print(s.maxTwoEvents(events))