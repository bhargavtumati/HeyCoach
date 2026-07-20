/*### Problem Statement: Minimum Moves to Seat Everyone

You are given two integer arrays:

* `seats[]` → represents the positions of available seats.
* `students[]` → represents the positions of students.

Each move allows a student to move **one position left or right**.

Your task is to find the **minimum number of moves required to make every student sit in a seat**.

Each seat can hold only one student.

---

### Example:

**Input:**

```java
seats = [3,1,5]
students = [2,7,5]
```

---

### Explanation:

Sort both arrays:

```
seats:
[1,3,5]

students:
[2,5,7]
```

Match students with seats:

```
Student 2 → Seat 1
Moves = |2 - 1| = 1

Student 5 → Seat 3
Moves = |5 - 3| = 2

Student 7 → Seat 5
Moves = |7 - 5| = 2
```

Total moves:

```
1 + 2 + 2 = 5
```

---

### Output:

```
5
```

---

### Algorithm:

1. Sort the `seats` array.
2. Sort the `students` array.
3. Pair each student with the seat at the same index.
4. Add the absolute difference between their positions.

Formula:

[
Answer = \sum |seats[i] - students[i]|
]

---

### Complexity:

Sorting:

```
O(N log N)
```

Loop:

```
O(N)
```

Overall:

```
Time Complexity: O(N log N)
Space Complexity: O(1)
```

---

Your Java code correctly implements the **greedy approach** for this problem.
 */


import java.util.Arrays;
class minMovesToSeat {
    public int Solution(int[] seats, int[] students) {
        int count=0;
        Arrays.sort(seats);
        Arrays.sort(students);
      for(int i=0;i<students.length;i++){
            
          
          count+=  Math.abs(seats[i] - students[i]);
           
             
            }
          
        
return count;
    }
    public static void main(String[] args) {
      int  arr[]={3,1,5};
      int arr2[]={2,7,5};
      minMovesToSeat k = new minMovesToSeat();
System.out.println(k.Solution(arr, arr2));
    }
}