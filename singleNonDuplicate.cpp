/*### Problem Statement: Single Element in a Sorted Array

You are given a **sorted array** where:

* Every element appears **exactly twice** except for **one element**.
* Find the element that appears only once.

Your algorithm should return the unique element.

---

### Example 1

**Input:**

```text
nums = [1,2,2,3,3]
```

**Output:**

```text
1
```

**Explanation:**

Pairs are:

```
2,2
3,3
```

Only `1` appears once, so the answer is `1`.

---

### Example 2

**Input:**

```text
nums = [1,1,2,3,3,4,4]
```

**Output:**

```text
2
```

**Explanation:**

All elements appear twice except `2`.

---

### Example 3

**Input:**

```text
nums = [7]
```

**Output:**

```text
7
```

**Explanation:**

The array contains only one element, so it is the unique element.

---

### Constraints

```text
1 <= nums.length <= 10^5

0 <= nums[i] <= 10^5

nums is sorted in ascending order.

Every element appears exactly twice except one element.
```

---

### Function Signature

C++:

```cpp
int Solution(vector<int>& nums)
```

Return the element that appears only once.

---

### Approach Used in Your Code

Your code uses **linear traversal**:

1. Start from the first element.
2. Compare each element with its neighbors.
3. Skip pairs.
4. The element without a pair is returned.

Example:

```
[1,2,2,3,3]

i=0 → 1 has no pair → answer = 1
```

---

### Complexity of Your Code

**Time Complexity:**

```
O(n)
```

because the array is scanned once.

**Space Complexity:**

```
O(1)
```

because only variables are used.

---

### More Optimal Approach

Since the array is sorted, this problem can be solved using **Binary Search**:

```
Time Complexity: O(log n)
Space Complexity: O(1)
```

because the pairs follow an index pattern:

Before the unique element:

```
even index → first of pair
odd index  → second of pair
```

After the unique element, the pattern breaks.
*/

#include <iostream>
#include <vector>
using namespace std;

class singleNonDuplicate {
public:
    int Solution(vector<int>& nums) {
        int uni=nums[0];
if(nums.size()==1)
return uni;
else{
for(int i=0;i<nums.size();i++){
            if(nums[i]==nums[i+1])
            i+=1;
            else if(i>=1&&nums[i]==nums[i-1])
                i++;
            
            else{
            uni=nums[i];
            break;
}

        }
}
return uni;
        
    }
};
int main()
{
    vector<int> ve={1,2,2,3,3};
    singleNonDuplicate ch;
    cout << ch.Solution(ve); 
    
}