

"""
### Problem Statement

There are `n` friends standing in a circle numbered from `1` to `n`. Starting from the first friend, every `k`-th friend
 is eliminated. The process continues until only one friend remains.

Return the **number of the last remaining friend (winner)**.

### Example

**Input:**

```text
n = 5
k = 2
```

**Process:**

```text
[1,2,3,4,5]

Remove 2 → [1,3,4,5]
Remove 4 → [1,3,5]
Remove 1 → [3,5]
Remove 5 → [3]
```

**Output:**

```text
3
```

### Approach

* Store friends in a list.
* Use modulo operation to calculate the next friend to remove.
* Continue removing until one friend remains.

### Complexity

* **Time Complexity:** `O(n²)` (because removing from a list takes `O(n)`)
* **Space Complexity:** `O(n)`

### Optimized Approach

The **Josephus formula** can solve it in:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

using:

```python
winner = (winner + k) % i
```

where `i` goes from `1` to `n`.
"""

class Solution:
    def find_the_winner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        index = 0

        while friends:
            index = (index + k-1) % len(friends)
            winner = friends.pop(index)
        
        return winner
    
if __name__=="__main__":
    n=5
    k=2
    f=Solution()
    print(f.find_the_winner(n,k))    