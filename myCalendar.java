/*### Problem Statement: My Calendar I (Booking Events)

Design a calendar system that allows users to **book events**.

You are given a calendar that initially has no events. Implement a class `MyCalendar` with a function:

```java
boolean book(int start, int end)
```

The function should:

* Add the event `(start, end)` to the calendar if there is **no overlap** with existing events.
* Return `true` if the event is successfully booked.
* Return `false` if the event overlaps with an already booked event.

### Important:

* The event interval is **half-open**: `[start, end)`
* This means:

  * The event starts at `start`.
  * The event ends just before `end`.
  * Two events can share a boundary point.

---

### Example:

**Input:**

```java
MyCalendar calendar = new MyCalendar();

calendar.book(10, 20);
calendar.book(15, 25);
calendar.book(20, 30);
```

---

### Explanation:

First booking:

```
[10,20)
```

Calendar:

```
10 -------- 20
```

No conflict.

Output:

```
true
```

---

Second booking:

```
[15,25)
```

Existing event:

```
10 -------- 20
     15 -------- 25
```

They overlap between `15` and `20`.

Output:

```
false
```

---

Third booking:

```
[20,30)
```

Existing event:

```
10 -------- 20
             20 -------- 30
```

They only touch at `20`, so there is no overlap.

Output:

```
true
```

---

### Output:

```
true
false
true
```

---

### Overlap Condition:

Two events overlap when:

```java
start < existingEnd && end > existingStart
```

Example:

```
New Event:       [15,25)
Existing Event:  [10,20)

15 < 20  → true
25 > 10  → true

Overlap exists
```

---

### Algorithm:

1. Store all booked events in a list.
2. For every new booking:

   * Check it against all existing events.
   * If overlap exists, return `false`.
   * Otherwise add the event and return `true`.

---

### Complexity:

For `N` bookings:

* Each booking checks all previous events.

Time Complexity:

```
O(N)
```

per booking.

Space Complexity:

```
O(N)
```

because we store all booked events.

---

Your implementation correctly uses the **brute-force interval checking approach** for **LeetCode 729 - My Calendar I**.
 */

import java.util.ArrayList;
import java.util.List;

class MyCalendar {
    private List<int[]> events;

    public MyCalendar() {
        events = new ArrayList<>();
    }

    public boolean book(int start, int end) {
        for (int[] event : events) {
            int eventStart = event[0];
            int eventEnd = event[1];
            if (start < eventEnd && end > eventStart) {
                // Overlapping events, cannot book
                return false;
            }
        }
        events.add(new int[]{start, end});
        return true;
    }


// Example usage

    public static void main(String[] args) {
        MyCalendar calendar = new MyCalendar();
        System.out.println(calendar.book(10, 20)); // true
        System.out.println(calendar.book(15, 25)); // false (overlaps with [10, 20])
        System.out.println(calendar.book(20, 30)); // true
    }
}
