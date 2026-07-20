/*### Problem Statement: Queue Reconstruction by Height

You are given an array `people` where each person is represented by:

```java
[height, k]
```

where:

* `height` = height of the person.
* `k` = number of people in front of this person who have a height **greater than or equal to** this person's height.

Your task is to reconstruct the queue so that every person satisfies their `k` value.

Return the reconstructed queue.

---

### Example 1:

**Input:**

```java
people = [
 [7,0],
 [4,4],
 [7,1],
 [5,0],
 [6,1],
 [5,2]
]
```

---

### Explanation:

Sort people by:

1. Higher height first.
2. If heights are equal, smaller `k` first.

After sorting:

```
[7,0]
[7,1]
[6,1]
[5,0]
[5,2]
[4,4]
```

Insert each person at index `k`:

```
Insert [7,0]

Queue:
[7,0]


Insert [7,1]

Queue:
[7,0], [7,1]


Insert [6,1]

Queue:
[7,0], [6,1], [7,1]


Insert [5,0]

Queue:
[5,0], [7,0], [6,1], [7,1]


Insert [5,2]

Queue:
[5,0], [7,0], [5,2], [6,1], [7,1]


Insert [4,4]

Queue:
[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]
```

Final valid queue:

```
[
 [5,0],
 [7,0],
 [5,2],
 [6,1],
 [4,4],
 [7,1]
]
```

---

### Output:

```java
[
 [5,0],
 [7,0],
 [5,2],
 [6,1],
 [4,4],
 [7,1]
]
```

---

### Algorithm: Greedy Approach

#### Step 1: Sort people

Sort by:

* Height descending.
* If height is same, `k` ascending.

Example:

```
Height: 7 7 6 5 5 4
k:      0 1 1 0 2 4
```

---

#### Step 2: Insert based on k value

For each person:

```java
queue.add(person[k], person)
```

The `k` value tells the exact position where the person should be placed.

Because taller people are already placed first, inserting by `k` automatically maintains the condition.

---

### Complexity:

Let `N` be the number of people.

Sorting:

```
O(N log N)
```

Insertion into `ArrayList`:

```
O(N^2)
```

because shifting elements may be required.

Overall:

```
Time Complexity: O(N²)
Space Complexity: O(N)
```

---

This is the classic **LeetCode 406 - Queue Reconstruction by Height** problem using a **Greedy Algorithm**.
 */

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class QueueReconstruction {
    public int[][] reconstructQueue(int[][] people) {
        // Sort people in descending order of height and ascending order of ki
        Arrays.sort(people, (a, b) -> {
            if (a[0] != b[0]) {
                return b[0] - a[0];//sort by height(taller first)
            } else {
                return a[1] - b[1];//sort by number ki (smaller ki first)
            }
        });

        // Initialize an empty queue
        List<int[]> queue = new ArrayList<>();

        // Insert each person into the queue at the specified position
        for (int[] p : people) {
            queue.add(p[1], p);
        }

        // Convert List to array
        return queue.toArray(new int[people.length][]);
    }

    public static void main(String[] args) {
        QueueReconstruction solution = new QueueReconstruction();
        int[][] people1 = {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}};
        int[][] result1 = solution.reconstructQueue(people1);
        System.out.println(Arrays.deepToString(result1));

        int[][] people2 = {{6, 0}, {5, 0}, {4, 0}, {3, 2}, {2, 2}, {1, 4}};
        int[][] result2 = solution.reconstructQueue(people2);
        System.out.println(Arrays.deepToString(result2));
    }
}