/*### Problem Statement: Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within **D days**.

You are given an array `weights`, where:

* `weights[i]` represents the weight of the `i-th` package.
* Packages must be shipped **in the same order** as they appear in the array.
* The ship can carry a maximum weight capacity per day.

Find the **minimum ship capacity** required to ship all packages within `days` days.

---

### Example 1

**Input:**

```text
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
```

**Output:**

```text
15
```

**Explanation:**

With capacity `15`:

```
Day 1: 1 2 3 4 5  = 15
Day 2: 6 7         = 13
Day 3: 8           = 8
Day 4: 9           = 9
Day 5: 10          = 10
```

All packages are shipped in 5 days.

Any smaller capacity will require more than 5 days.

---

### Example 2

**Input:**

```text
weights = [3,2,2,4,1,4]
days = 3
```

**Output:**

```text
6
```

**Explanation:**

Capacity `6` allows:

```
Day 1: 3 2
Day 2: 2 4
Day 3: 1 4
```

---

### Example 3

**Input:**

```text
weights = [1,2,3,1,1]
days = 4
```

**Output:**

```text
3
```

---

### Constraints

```text
1 <= weights.length <= 50000

1 <= weights[i] <= 500

1 <= days <= weights.length
```

---

### Function Signature

C++:

```cpp
int Solution(vector<int>& weights, int days)
```

Return the minimum ship capacity needed.

---

### Approach Used in Your Code

Your solution uses **Binary Search on Answer**.

Search range:

```
start = maximum package weight
end = total weight of all packages
```

For each possible capacity (`mid`):

1. Simulate shipping with that capacity.
2. Count how many days are required.
3. If required days > given days:

   * Increase capacity.
4. Otherwise:

   * Try a smaller capacity.

---

### Complexity

**Time Complexity:**

```
O(N * log(S))
```

where:

* `N` = number of packages
* `S` = total weight of packages

**Space Complexity:**

```
O(1)
```

Only variables are used.
*/


#include <iostream>
#include <vector>

using namespace std;

class shipWithinDays {
public:
    int Solution(vector<int>& weights, int days) {
        int start = 0, end = 0;
        for (int weight : weights) {
            start = max(start, weight);
            end += weight;
        }

        while (start < end) {
            int mid = start + (end - start) / 2;
            int currWeight = 0, currDays = 1;

            for (int weight : weights) {
                if (currWeight + weight <= mid) {
                    currWeight += weight;
                } else {
                    currWeight = weight;
                    currDays++;
                }
            }

            if (currDays > days) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        return end;
    }
};

int main() {
    vector<int> weights1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int days1 = 5;
    shipWithinDays sh1;
    cout << "Example 1: " << sh1.Solution(weights1, days1) << endl;

    vector<int> weights2 = {3, 2, 2, 4, 1, 4};
    int days2 = 3;
    shipWithinDays sh2;
    cout << "Example 2: " << sh2.Solution(weights2, days2) << endl;

    vector<int> weights3 = {1, 2, 3, 1, 1};
    int days3 = 4;
    shipWithinDays sh3;
    cout << "Example 3: " << sh3.Solution(weights3, days3) << endl;

    return 0;
}
