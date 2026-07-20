/*### Problem Statement: Range Sum Query - Mutable (Segment Tree)

You are given an integer array `nums`.

You need to support two operations:

1. **Update operation**

```cpp
update(index, val)
```

Change the value of `nums[index]` to `val`.

2. **Range Sum Query**

```cpp
sumRange(left, right)
```

Return the sum of elements from index `left` to `right` (inclusive).

The array values can change multiple times, so the solution should efficiently handle both updates and queries.

---

### Example:

**Input:**

```cpp
nums = [1, 3, 5]

sumRange(0, 2)

update(1, 2)

sumRange(0, 2)
```

---

### Explanation:

Initial array:

```
[1, 3, 5]
```

Query:

```
sumRange(0,2)
```

Calculation:

```
1 + 3 + 5 = 9
```

Output:

```
9
```

---

Update:

```
update(1,2)
```

Index `1` value changes from `3` to `2`.

Array becomes:

```
[1,2,5]
```

---

Query again:

```
sumRange(0,2)
```

Calculation:

```
1 + 2 + 5 = 8
```

Output:

```
8
```

---

### Output:

```
9
8
```

---

## Approach: Segment Tree

A Segment Tree is a binary tree where:

* Each node stores the sum of a segment of the array.
* The root stores the sum of the entire array.
* Leaf nodes store individual array values.

Example:

Array:

```
[1,3,5]
```

Segment Tree:

```
             9
          /     \
        4         5
      /   \
     1     3
```

---

### Operations:

### 1. Build Tree

Create the segment tree from the given array.

Time:

```
O(N)
```

---

### 2. Update

When a value changes:

```
nums[index] = val
```

Only the path from the leaf node to the root needs updating.

Time:

```
O(log N)
```

---

### 3. Range Sum Query

To find sum between `left` and `right`, traverse only required segments.

Time:

```
O(log N)
```

---

### Complexity:

For `N` elements:

| Operation          | Complexity |
| ------------------ | ---------- |
| Build Segment Tree | O(N)       |
| Update             | O(log N)   |
| Sum Query          | O(log N)   |
| Space              | O(N)       |

---

This is the classic **LeetCode 307 - Range Sum Query: Mutable** problem.
*/

#include <iostream>
#include <vector>
using namespace std;

class NumArray {
private:
    vector<int> tree; // Segment tree
    int n; // Size of the input array

    // Build the segment tree
    void buildTree(vector<int>& nums) {
        for (int i = n; i < 2 * n; ++i) {
            tree[i] = nums[i - n];
        }
        for (int i = n - 1; i > 0; --i) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        tree.resize(2 * n);
        buildTree(nums);
    }

    void update(int index, int val) {
        index += n;
        tree[index] = val;
        while (index > 1) {
            index /= 2;
            tree[index] = tree[2 * index] + tree[2 * index + 1];
        }
    }

    int sumRange(int left, int right) {
        left += n;
        right += n;
        int sum = 0;
        while (left <= right) {
            if (left % 2 == 1) {
                sum += tree[left];
                ++left;
            }
            if (right % 2 == 0) {
                sum += tree[right];
                --right;
            }
            left /= 2;
            right /= 2;
        }
        return sum;
    }
};

int main() {
    vector<int> nums = {1, 3, 5};
    NumArray numArray(nums);
    cout << numArray.sumRange(0, 2) << endl; // Returns 9
    numArray.update(1, 2); // nums = [1, 2, 5]
    cout << numArray.sumRange(0, 2) << endl; // Returns 8
    return 0;
}
