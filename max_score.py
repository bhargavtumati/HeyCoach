"""### Problem Statement

Given an array `card` where each element represents the points of a card, choose exactly `k` cards from either the **beginning or the end** of the array to get the maximum possible score.

Return the maximum score you can obtain.

### Example

**Input:**

```text
card = [1,2,3,4,5,6,1]
k = 5
```

**Output:**

```text
18
```

### Explanation:

Possible maximum selection:

```text
From left: 1 + 2 + 3 + 4
From right: 6 + 1
```

Better combination:

```text
1 + 2 + 3 + 4 + 6 + 1 (choose k cards by moving choices)
```

The maximum score is:

```text
18
```

### Approach

* Calculate the sum of the first `k` cards.
* Then slide the selection:

  * Remove one card from the left side.
  * Add one card from the right side.
* Track the maximum score during each step.

### Complexity

Let `n` be the number of cards.

* **Time Complexity:** `O(k)`
* **Space Complexity:** `O(1)`

### Key Idea

Instead of checking all possible combinations, use a **sliding window** by shifting cards from the left selection to the right selection.
"""


from typing import List

class maxScore:
    def Solution(self, card: List[int], k: int) -> int:
        s = 0
        for i in range(k):
            s+=card[i] #added first k
        k-=1 #  decreament k
        ans = s 
        while k>=0:
            s -= card[k]   #removed k elemnt
            s+=card.pop()  
            ans = max(ans,s)
            k-=1   
        return ans 
    
if __name__ =="__main__":
    card=[1,2,3,4,5,6,1]
    k=5
    al=maxScore()
    print(al.Solution(card,k))
    