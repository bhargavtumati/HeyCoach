/*### Problem Statement

Given an integer array `nums`, find the **maximum sum of a contiguous subarray**.

A contiguous subarray contains consecutive elements from the array.

Return the largest possible sum.

### Example

**Input:**

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

**Output:**

```text
6
```

### Explanation:

The subarray with the maximum sum is:

```text
[4,-1,2,1]
```

Sum:

```text
4 + (-1) + 2 + 1 = 6
```

### Approach

Use **Kadane's Algorithm**:

* Maintain `currentSum`:

  * Maximum sum of a subarray ending at the current position.
* At each element:

  * Either start a new subarray from the current element.
  * Or extend the previous subarray.

Formula:

```java
currentSum = max(num, currentSum + num)
```

* Update the global maximum:

```java
maxSum = max(maxSum, currentSum)
```

### Complexity

Let `n` be the size of the array.

**Time Complexity:**

```
O(n)
```

(Traverse the array once)

**Space Complexity:**

```
O(1)
```

### Key Idea

At every index, decide whether the current element alone gives a better sum or adding it to the previous subarray gives a better sum. This avoids checking all possible subarrays.
 */


class maxSubArray {
    public int Solution(int[] nums) {
        int maxSum = Integer.MIN_VALUE; // Initialize maxSum to negative infinity
        int currentSum = 0;

        for (int num : nums) {
            currentSum = Math.max(num, currentSum + num);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum; 
    }

   public static void main(String args[]){
    int ar[]={-2,-3,-1};
maxSubArray ms=new maxSubArray();
System.out.println(ms.Solution(ar));
   } 
}