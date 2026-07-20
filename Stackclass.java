/*### Problem Statement: Stack Operations in Java

Implement and demonstrate various operations on a **Stack** data structure using Java's built-in `Stack` class.

A stack follows the **LIFO (Last In First Out)** principle, where the element inserted last is removed first.

Perform the following operations:

1. **Push elements** into the stack.
2. **Pop an element** from the top of the stack.
3. **View the first element** of the stack.
4. **Peek the top element** without removing it.
5. **Remove an element using an index.**
6. **Search and remove a specific value from the stack.**
7. **Insert an element at a specific index.**
8. **Traverse and display all stack elements.**

---

### Example

Initial stack:

```text
Push: 23, 6, 0, 80
```

Stack representation:

```
Top
 |
80
0
6
23
 |
Bottom
```

---

### Operations

#### 1. Pop

```java
st.pop();
```

Removes the top element:

```
Removed: 80
```

Stack becomes:

```
0
6
23
```

---

#### 2. Peek

```java
st.peek();
```

Returns the top element without removing it:

```
Top element: 0
```

---

#### 3. Remove by Index

```java
st.remove(0);
```

Removes the element at index `0`.

Before:

```
[23,6,0]
```

After:

```
[6,0]
```

---

#### 4. Remove Specific Value

Search for:

```java
targetValue = 6;
```

Remove it from the stack.

Before:

```
[6,0]
```

After:

```
[0]
```

---

#### 5. Insert Element at Index

```java
st.insertElementAt(90,0);
```

Before:

```
[0]
```

After:

```
[90,0]
```

---

### Final Output Example

```
removed this element: 80
The first element is: 23
view this last inserted element: 0
Removed element: 23
Removed element: 6
stack values are:
90 0
```

---

### Stack Methods Used

| Method                         | Description                          |
| ------------------------------ | ------------------------------------ |
| `push(x)`                      | Adds element to top of stack         |
| `pop()`                        | Removes and returns top element      |
| `peek()`                       | Returns top element without removing |
| `firstElement()`               | Returns bottom/first element         |
| `remove(index)`                | Removes element at given index       |
| `get(index)`                   | Retrieves element at index           |
| `insertElementAt(value,index)` | Inserts element at specific position |
| `iterator()`                   | Traverses stack elements             |

---

### Complexity

| Operation           | Time Complexity |
| ------------------- | --------------- |
| `push()`            | O(1)            |
| `pop()`             | O(1)            |
| `peek()`            | O(1)            |
| `get(index)`        | O(1)            |
| `remove(index)`     | O(n)            |
| `insertElementAt()` | O(n)            |

The stack internally uses a **dynamic array (Vector)** in Java.
 */

import java.util.*;
class Stackclass{
    public static void main(String args[]){
        Stack<Integer> st =new Stack<>();
       st.push(23);//0
       st.push(6);//1
       st.push(0);//2
       st.push(80);//3

       System.out.println("removed this element:  "+st.pop());

       ///inbuilt but can be built by yourself..

       System.out.println("The first element is: " + st.firstElement());

       System.out.println("view this last inserted element:  "+st.peek());

       int removedElement = st.remove(0);
        System.out.println("Removed element: " + removedElement);

        int targetValue=6;
        for (int i = 0; i < st.size(); i++) {
         if (st.get(i) == targetValue) {
             // Remove the element at index i
             
             System.out.println("Removed element: " + st.remove(i));
             break; // Stop iterating after removal
         }
        }

        int newElement =90, targetIndex =0;
        st.insertElementAt(newElement, targetIndex);

       Iterator<Integer> value = st.iterator();
       System.out.println("stack values are: ");
       while(value.hasNext()){
        
           System.out.print(value.next()+" ");
       }
      
    
    }
       
    }
