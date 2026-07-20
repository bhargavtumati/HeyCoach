"""### Problem Statement: Sliding Window Maximum

You are given an integer array `nums` and an integer `k`.

There is a sliding window of size `k` that moves from the left to the right of the array.

For each position of the window, find the **maximum element** inside that window.

Return an array containing the maximum value for each sliding window.

---

### Example

**Input:**

```python
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

**Sliding windows:**

```
[1, 3, -1]  → 3
[3, -1, -3] → 3
[-1,-3,5]   → 5
[-3,5,3]    → 5
[5,3,6]     → 6
[3,6,7]     → 7
```

**Output:**

```python
[3,3,5,5,6,7]
```

---

### Approach Used: Monotonic Decreasing Queue

Your solution uses a **deque** to maintain elements in decreasing order.

The deque stores:

```python
(value, index)
```

Example:

```
nums = [1,3,-1,-3,5]

deque after processing first elements:

(3,1)
(-1,2)
```

The largest value is always at the front:

```python
q[0][0]
```

---

### Algorithm

For every element:

1. Remove elements that are outside the current window:

```python
if i >= k and q[0][1] == i-k:
    q.popleft()
```

2. Remove smaller elements from the back:

```python
while q and q[-1][0] <= nums[i]:
    q.pop()
```

Because they can never become maximum while the current bigger element exists.

3. Add current element:

```python
q.append((nums[i], i))
```

4. Once the window reaches size `k`, add maximum:

```python
ans.append(q[0][0])
```

---

### Time Complexity

Each element:

* Enters deque once.
* Leaves deque once.

Therefore:

```
O(N)
```

where `N` is the length of `nums`.

---

### Space Complexity

Deque stores at most `k` elements:

```
O(K)
```

---

### Key Idea

The deque is always maintained in decreasing order:

Example:

```
nums = [4,2,1,5]

After processing 5:

Before:
[4,2,1]

Remove smaller:
[ ]

Add 5:
[5]
```

The front of the deque is always the maximum element of the current window.
"""


from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(nums)):
            if i >= k and q[0][1] == i - k:
                q.popleft()
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            if i >= k - 1:
                ans.append(q[0][0])
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.maxSlidingWindow(nums, k))
