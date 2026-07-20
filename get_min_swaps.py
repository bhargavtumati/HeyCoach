"""
### Problem Statement

Given a number represented as a string `num` and an integer `k`, find the **minimum number of adjacent swaps** needed to transform `num` into the **k-th smallest permutation** of the number.

A swap can only be performed between **adjacent digits**.

Return the minimum number of adjacent swaps required.

### Example

**Input:**

```text
num = "5489355142"
k = 4
```

**Output:**

```text
2
```

### Explanation:

The 4th next permutation of:

```text
5489355142
```

is:

```text
5489355421
```

Moving digits using adjacent swaps requires minimum swaps.

### Approach

1. Generate the `k`-th next permutation of the number.
2. Compare the original number and target permutation.
3. Count the minimum adjacent swaps required to transform the original arrangement into the target.

### Complexity

Let `n` be the length of the number.

* **Generating k permutations:** `O(k × n²)`
* **Counting swaps:** `O(n²)`
* **Space Complexity:** `O(n)`

This approach works when `k` and `n` are small. For larger constraints, a greedy + Fenwick Tree approach is used.
"""

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num=list(num)
        orig = num.copy()
        print(num)
        for _ in range(k):
            for i in reversed(range(len(num)-1)):
                if num[i]<num[i+1]:    #checks num[8,7,6,]>num[9,8,7,]
                    ii=i+1
                    while ii < len(num) and num[i] <num[ii]: 
                           ii +=1
                    num[i], num[ii-1] = num[ii-1], num[i]   #swap

                    lo, hi =i+1, len(num)-1
                    while lo< hi:
                        num[lo], num[hi] = num[hi], num[lo]  #swap
                        
                        lo+=1
                        hi-=1
                    print(num)
                    break
        ans=0
        for i in range(len(num)):
            ii=i
            while orig[i]!=num[i]:
                ans+=1
                ii+=1
                num[i],num[ii]=num[ii],num[i]
        return ans

if __name__=="__main__":
    num="5489355142"
    k=4
    s=Solution()
    print(s.getMinSwaps(num,k))