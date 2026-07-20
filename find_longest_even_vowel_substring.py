""" ### Problem Statement

Given a string `s` containing lowercase English letters, find the **length of the longest substring** in which 
**each vowel (`a`, `e`, `i`, `o`, `u`) appears an even number of times**.

Return the length of the longest valid substring.

### Example

**Input:**

```text
s = "eleetminicoworoep"
```

**Output:**

```text
13
```

### Explanation:

The longest substring is:

```text
"leetminicowor"
```

In this substring:

* `e` appears 2 times
* `i` appears 2 times
* `o` appears 2 times
* `a` and `u` appear 0 times

All vowels have even counts.

### Approach

* Use a **bitmask** to track the parity (odd/even) count of each vowel.
* Store the first occurrence index of each bitmask.
* If the same bitmask appears again, the substring between them has all vowels appearing an even number of times.

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` (for storing bitmask positions)

"""

class Solution:
    def find_the_longest_substring(self, s: str) -> int:
        dp={0:-1}  # creating dictionary 
        parity = 0
        ans = 0
        vowels = 'aeiou'
        for i,c in enumerate(s):  # getting index of each letter 
            if c in vowels:
                index = vowels.index(c)
                parity^=1<<index   #xor of 1 left shift index
            if parity in dp:
                ans=max(ans,i-dp[parity])
            else:
                dp[parity]=i
        return ans
    
if __name__=="__main__":
    s="eleetminicoworoep"
    f=Solution()
    print(f.find_the_longest_substring(s))