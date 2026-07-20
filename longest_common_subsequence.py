"""### Problem Statement

Given two strings `text1` and `text2`, find the **length of their longest common subsequence (LCS)**.

A **subsequence** is a sequence that can be formed by deleting some characters from a string without changing the order of the remaining characters.

Return the length of the longest subsequence that appears in both strings.

### Example

**Input:**

```text
text1 = "ahcfe"
text2 = "ace"
```

**Output:**

```text
3
```

### Explanation:

The longest common subsequence is:

```text
a → c → e
```

Length:

```text
3
```

### Approach

* Use Dynamic Programming.
* Maintain a 1D `dp` array where `dp[i]` stores the LCS length ending at index `i` of `text1`.
* Traverse each character of `text2`.
* Update the values based on:

  * If characters match, increase the previous LCS length.
  * Otherwise, keep the maximum previous value.

### Complexity

Let:

* `m = len(text1)`
* `n = len(text2)`

**Time Complexity:** `O(m × n)`
**Space Complexity:** `O(m)`

### Key Idea

Instead of using a full `m × n` DP table, this approach compresses the state into a single array while maintaining the same result.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)
        
        return longest
    
    #Time complexity= O(len(text1)*len(text2))  
    #Space complexity=O(len(text1)) 
if __name__=="__main__":
    text1="ahcfe"
    text2="ace"
    s=Solution()
    print(s.longestCommonSubsequence(text1,text2))