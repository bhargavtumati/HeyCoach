/*### Problem Statement: Trapping Rain Water

Given an array `height` where each element represents the height of a vertical bar, calculate how much water can be trapped between the bars after raining.

* Each bar has a width of `1`.
* Water can be trapped only when there are taller bars on both the left and right sides of a lower bar.
* Return the total amount of trapped water.

---

### Example 1

**Input:**

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output:**

```text
6
```

**Explanation:**

The elevation map can trap water as follows:

```
        █
    █~~~█~█
█~~~█~█~█~█
----------------
0 1 0 2 1 0 1 3 2 1 2 1
```

The total trapped water is:

```
6 units
```

---

### Example 2

**Input:**

```text
height = [4,2,0,3,2,5]
```

**Output:**

```text
9
```

**Explanation:**

Water is trapped between the bars:

```
        █
█~~~    █
█~█~█  █
█~█~███
----------------
4 2 0 3 2 5
```

Total trapped water:

```
9 units
```

---

### Constraints

```text
1 <= height.length <= 2 * 10^4

0 <= height[i] <= 10^5
```

---

### Function Signature

Java:

```java
public int Solution(int[] height)
```

Return the total units of water that can be trapped.
*/

class trap {
    public int Solution(int[] height) {
        int trap=0;
        for(int i=0;i<height.length;i++){
            
            int yet=height[i];
            for(int j=i;j<height.length;j++){
                if(height[j]<yet){
                    trap+=yet-height[j];
                }
            }    
                
          
        }
         
        return trap;
    }
}