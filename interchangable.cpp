/*### Problem Statement

Given a list of rectangles where each rectangle is represented by its **width** and **height**, 
sfind the number of pairs of rectangles that have the **same width-to-height ratio**.

Two rectangles are **interchangeable** if:

[
\frac{width_1}{height_1} = \frac{width_2}{height_2}
]

Return the total number of such pairs.

### Example

**Input:**

```text
rectangles = [
 [4,8],
 [3,6],
 [10,20],
 [15,30]
]
```

**Ratios:**

```text
4/8 = 0.5
3/6 = 0.5
10/20 = 0.5
15/30 = 0.5
```

All rectangles have the same ratio.

**Output:**

```text
6
```

### Explanation

Possible pairs:

```
(4,8) with (3,6)
(4,8) with (10,20)
(4,8) with (15,30)
(3,6) with (10,20)
(3,6) with (15,30)
(10,20) with (15,30)
```

Total pairs = `6`.

### Approach

* Calculate the width/height ratio of each rectangle.
* Store the frequency of each ratio using a hash map.
* When a ratio appears again:

  * Existing rectangles with the same ratio can form pairs with the current rectangle.
  * Add the current count to the answer.

### Complexity

Let `n` be the number of rectangles.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

### Note

Using `double` as a hash key can cause floating-point precision issues. A safer approach is to store the reduced fraction:

```text
width / gcd(width, height), height / gcd(width, height)
```

as the key.

*/
#include <bits/stdc++.h>
using namespace std;

class interchangable {
public:
    int interchangeableRectangles(vector<vector<int>>& rectangles) {
        int counts = 0;
        unordered_map<double, int> st;

        for (const vector<int>& rect : rectangles) {
            double ratio = static_cast<double>(rect[0]) / rect[1];
            if (st.find(ratio) == st.end()) {
                st[ratio] = 0;
            } else {
                counts += st[ratio] + 1;
                st[ratio]++;
            }
        }

        return counts;
    }
};

int main() {
    // Example usage:
    interchangable sol;
    vector<vector<int>> rectangles = {{4, 8}, {3, 6}, {10, 20}, {15, 30}};
    cout << "Interchangeable pairs: " << sol.interchangeableRectangles(rectangles) << endl;
    return 0;
}
