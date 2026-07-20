
/*### Problem Statement: Queue Operations in Java

Implement a queue data structure using Java's `Queue` interface.

Perform the following operations:

1. **Add elements** to the queue.
2. **View the first element** of the queue without removing it.
3. **Remove the first element** from the queue.
4. **Traverse and print all queue elements**.
5. **Copy elements from one queue to another**.
6. **Clear all elements from a queue**.

---

### Example:

**Input Operations:**

```java
Queue<Integer> qu = new LinkedList<>();

qu.add(4);
qu.add(9);
qu.add(10);
qu.add(80);
```

Queue:

```
Front → 4 9 10 80 ← Rear
```

---

### 1. Peek Operation

```java
qu.peek()
```

Returns the first element without removing it.

Output:

```
returns first element for queue: 4
```

Queue remains:

```
4 9 10 80
```

---

### 2. Poll Operation

```java
qu.poll()
```

Removes and returns the first element.

Output:

```
removes the first element: 4
```

Queue becomes:

```
9 10 80
```

---

### 3. Iterator Traversal

```java
Iterator<Integer> value = qu.iterator();
```

Prints remaining elements:

Output:

```
queue elements:
9 10 80
```

---

### 4. Copy Queue

```java
qu2.addAll(qu);
```

Copies all elements from `qu` to `qu2`.

Before:

```
qu  = [9,10,80]
qu2 = []
```

After:

```
qu  = [9,10,80]
qu2 = [9,10,80]
```

---

### 5. Clear Queue

```java
qu.clear();
```

Removes all elements from `qu`.

After:

```
qu = []
```

---

### Queue Methods Used:

| Method       | Description                             |
| ------------ | --------------------------------------- |
| `add()`      | Inserts an element into queue           |
| `peek()`     | Returns front element without removing  |
| `poll()`     | Removes and returns front element       |
| `iterator()` | Traverses queue elements                |
| `addAll()`   | Adds all elements of another collection |
| `clear()`    | Removes all elements                    |

---

### Complexity:

| Operation    | Time Complexity |
| ------------ | --------------- |
| `add()`      | O(1)            |
| `peek()`     | O(1)            |
| `poll()`     | O(1)            |
| `iterator()` | O(N)            |
| `clear()`    | O(N)            |

---

This demonstrates basic **Queue implementation using LinkedList in Java**.
 */

import java.util.Queue;
import java.util.LinkedList;
import java.util.Iterator;
class QueueClass{
    public static void main(String args[]){
Queue<Integer> qu =new LinkedList<>();
Queue<Integer> qu2 =new LinkedList<>();
qu.add(4);
qu.add(9);
qu.add(10);
qu.add(80);

System.out.println("returns first element for queue  "+qu.peek());

System.out.println("removes the first element  "+qu.poll());


Iterator<Integer> value = qu.iterator();
System.out.println("queue elements: ");
while(value.hasNext()){
    System.out.print(value.next()+" ");
}
qu2.addAll(qu);//add elements of qu to qu2
qu.clear();//clears all elements;
    }
}