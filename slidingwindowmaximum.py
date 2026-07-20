"""### Problem Statement: Sliding Window Maximum

Given an integer array `nums` and an integer `k`, find the **maximum value in each sliding window of size `k`**.

A sliding window moves from left to right by one position at a time. For each window, return the maximum element.

---

### Example 1

**Input:**

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

**Output:**

```text
[3,3,5,5,6,7]
```

**Explanation:**

The windows are:

```
[1, 3, -1] → max = 3

[3, -1, -3] → max = 3

[-1, -3, 5] → max = 5

[-3, 5, 3] → max = 5

[5, 3, 6] → max = 6

[3, 6, 7] → max = 7
```

---

### Example 2

**Input:**

```text
nums = [1]
k = 1
```

**Output:**

```text
[1]
```

---

### Example 3

**Input:**

```text
nums = [9,11]
k = 2
```

**Output:**

```text
[11]
```

---

### Constraints

```text
1 <= nums.length <= 10^5

-10^4 <= nums[i] <= 10^4

1 <= k <= nums.length
```

---

### Function Signature

Python:

```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
```

Return a list containing the maximum value of every window of size `k`.

---

### Approach Used in Your Code

Your solution uses a **Monotonic Deque**.

The deque stores:

```
(value, index)
```

and maintains values in **decreasing order**.

Example:

```
nums = [1,3,-1,-3,5]

After processing:
deque = [(5,4), (3,3)]
```

The front always contains the maximum value of the current window.

---

### Steps:

1. Remove elements that are outside the current window:

```python
if i >= k and q[0][1] == i-k:
    q.popleft()
```

2. Remove smaller elements from the back because they can never become maximum:

```python
while q and q[-1][0] <= nums[i]:
    q.pop()
```

3. Add current element:

```python
q.append((nums[i], i))
```

4. When window size reaches `k`, add maximum:

```python
ans.append(q[0][0])
```

---

### Complexity

**Time Complexity:**

```
O(n)
```

Each element is added and removed from the deque at most once.

**Space Complexity:**

```
O(k)
```

The deque stores at most `k` elements.
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
        

        
        
        
if __name__=="__main__":
    s=Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(s.maxSlidingWindow(nums,k))