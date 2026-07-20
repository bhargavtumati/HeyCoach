/*### Problem Statement

Given an integer array `nums`, find the **number of longest increasing subsequences (LIS)**.

A subsequence is a sequence that can be obtained by deleting some elements without changing the order of the remaining elements.

Return the count of subsequences that have the maximum possible increasing length.

### Example

**Input:**

```text
nums = [1,3,5,4,7]
```

**Output:**

```text
2
```

### Explanation:

Longest increasing subsequences are:

```text
1 → 3 → 5 → 7
1 → 3 → 4 → 7
```

Both have length `4`, so the number of LIS is `2`.

### Approach

Use Dynamic Programming:

* `dp[i]` → length of the longest increasing subsequence ending at index `i`.
* `count[i]` → number of LIS of length `dp[i]` ending at index `i`.
* Compare every previous element `j` with current element `i` and update length and count.

### Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`
 */

import java.util.Arrays;

public class findNoOfLIS {
    public int Solution(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n]; // Length of LIS ending at index i
        int[] count = new int[n]; // Number of LIS of length i
        Arrays.fill(dp, 1);
        Arrays.fill(count, 1);

        int maxLen = 1; // Length of the longest increasing subsequence

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if (dp[j] + 1 == dp[i]) {
                        count[i] += count[j];
                    }
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == maxLen) {
                result += count[i];
            }
        }

        return result;
    }
    public static void main(String args[]){
        int[] nums={1,3,5,4,7};
findNoOfLIS fs =new findNoOfLIS();
        System.out.println(fs.Solution(nums));
        
    }
}


