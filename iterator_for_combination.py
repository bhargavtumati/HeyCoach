"""### Problem Statement

Design a **Combination Iterator** that generates all possible combinations of a given string of characters with a fixed length.

The iterator should support:

1. **next()**

   * Returns the next available combination in lexicographical order.

2. **hasNext()**

   * Returns `True` if there are more combinations available, otherwise `False`.

### Example

**Input:**

```text
characters = "abc"
combinationLength = 2
```

**Output:**

```text
ab ac bc
```

### Explanation:

All combinations of length `2` from `"abc"` are:

```text
ab
ac
bc
```

The iterator returns these combinations one by one.

### Approach

* Use **backtracking** to generate all possible combinations.
* Store generated combinations in a queue.
* `next()` removes and returns the first combination.
* `hasNext()` checks whether the queue still contains combinations.

### Complexity

Let:

* `n` = number of characters
* `k` = combination length

Number of combinations = `C(n, k)`

* **Initialization Time:** `O(C(n,k) × k)`
* **next():** `O(1)` (with deque instead of list)
* **hasNext():** `O(1)`
* **Space Complexity:** `O(C(n,k) × k)`

**Note:** For better memory efficiency, combinations can be generated lazily using an iterator instead of storing all combinations.
"""


class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.q=[]
        def getCombination(start,length,txt):
            if length == 0:
                self.q.append(txt)
                return
            for i in range(start,len(characters)-length+1):
                getCombination(i+1,length-1,txt+characters[i])
        getCombination(0,combinationLength,"")

            

    def next(self) -> str:
        str=self.q[0]
        self.q.pop(0)
        return str

    def hasNext(self) -> bool:
        return len(self.q)>0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()




# Example usage:
characters = "abc"
combinationLength = 2
obj = CombinationIterator(characters, combinationLength)

# Print the first few combinations
while obj.hasNext():
    print(obj.next()+" ",end='')

# Check if there are more combinations
print("\nHas next combination:", obj.hasNext())
