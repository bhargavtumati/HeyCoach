/*### Problem Statement: My Calendar II (Avoid Triple Booking)

Design a calendar system that allows events to be booked, but **no time interval can have three or more overlapping events**.

Implement a class `MyCalendarTwo` with a function:

```java
boolean book(int start, int end)
```

The function should:

* Add the event `[start, end)` if it does not create a **triple booking**.
* Return `true` if the event is successfully booked.
* Return `false` if adding the event would cause three events to overlap at the same time.

### Important:

* The interval is **half-open**: `[start, end)`
* The start time is included.
* The end time is excluded.

---

### Example:

**Input:**

```java
MyCalendarTwo calendar = new MyCalendarTwo();

calendar.book(10,20);
calendar.book(50,60);
calendar.book(10,40);
calendar.book(5,15);
calendar.book(5,10);
calendar.book(25,55);
```

---

### Explanation:

#### 1. Book `[10,20)`

```
10 -------- 20
```

No overlap.

Output:

```
true
```

---

#### 2. Book `[50,60)`

```
50 -------- 60
```

No overlap.

Output:

```
true
```

---

#### 3. Book `[10,40)`

```
10 -------- 20
10 ---------------- 40
```

Double booking between:

```
10 - 20
```

Allowed.

Output:

```
true
```

---

#### 4. Book `[5,15)`

Current events:

```
       10----20
5--------------15
10-------------40
```

Between:

```
10 - 15
```

There are 3 active events:

```
[10,20)
[10,40)
[5,15)
```

Triple booking occurs.

Output:

```
false
```

---

#### 5. Book `[5,10)`

```
5----10
```

No triple overlap.

Output:

```
true
```

---

### Output:

```
true
true
true
false
true
true
```

---

## Approach: Sweep Line Algorithm (TreeMap)

The idea is to store the **change in number of active events** at each time.

For every booking:

* At `start` time:

  ```
  +1 booking starts
  ```

* At `end` time:

  ```
  -1 booking ends
  ```

Example:

Booking:

```
[10,20)
```

TreeMap:

```
10 → +1
20 → -1
```

---

For:

```
[10,40)
```

TreeMap:

```
10 → +2
20 → -1
40 → -1
```

Sweep through times:

```
time 10:
active = 2

time 20:
active = 1

time 40:
active = 0
```

Maximum active bookings = 2, so allowed.

---

If active count reaches:

```
active >= 3
```

then a triple booking exists.

The code removes the added event and returns `false`.

---

### Complexity:

Let `N` be the number of bookings.

For every booking:

* Insert start/end into TreeMap:

```
O(log N)
```

* Traverse all events:

```
O(N)
```

Overall:

```
Time Complexity: O(N²)
```

Space:

```
O(N)
```

---

This is the standard **LeetCode 731 - My Calendar II** solution using a **Sweep Line + TreeMap** technique.
 */
import java.util.TreeMap;

class MyCalendarTwo {
    private TreeMap<Integer, Integer> delta; // Keeps track of the change in bookings

    public MyCalendarTwo() {
        delta = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        // Update the delta for the start and end times
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);

        int active = 0; // Number of active bookings
        for (int d : delta.values()) {
            active += d;
            if (active >= 3) {
                // Triple booking detected, revert the changes
                delta.put(start, delta.get(start) - 1);
                delta.put(end, delta.get(end) + 1);
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
        System.out.println(myCalendarTwo.book(10, 20)); // true
        System.out.println(myCalendarTwo.book(50, 60)); // true
        System.out.println(myCalendarTwo.book(10, 40)); // true
        System.out.println(myCalendarTwo.book(5, 15));  // false
        System.out.println(myCalendarTwo.book(5, 10));  // true
        System.out.println(myCalendarTwo.book(25, 55)); // true
    }
}
